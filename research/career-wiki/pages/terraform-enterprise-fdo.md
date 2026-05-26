# Terraform Enterprise — FDO 模式遷移與 Air-gap 安裝

> **Source positions**: Resolve Technology 2021–2022（Lead DevOps + Consultant）
> **Last ingested**: 2026-04-22（from UpNote BJJ Data Migration + BJJ New TFE Setup Steps）
> **Confidence**: high（Zeuik 親自執行客戶 TFE 遷移，BJJ 為客戶代號）
> **Linted**: 2026-04-22

---

## Context

Terraform Enterprise（TFE）歷史上有兩種執行模式：
- **Replicated 模式**（舊）：用 Replicated installer 管理，內建 Admin Console，黑盒程度高
- **FDO 模式（Flexible Deployment Options）**：用 Docker Compose 或 Kubernetes 管理，更透明、更易 air-gap 部署

Resolve 客戶 BJJ 於 2023 年從 Replicated 遷移至 FDO，並搭建新 TFE 實例（air-gap 環境，版本 v202309-1，DB 外接 PostgreSQL，Object Storage 外接 GCS）。

---

## Architecture（External Mode）

```
[TFE FDO Container]
    ├─ Runtime: Docker Compose（docker-compose.yml）
    ├─ DB: External PostgreSQL（on-prem，sslmode=require）
    ├─ Object Storage: GCS Bucket（service account JSON credentials）
    ├─ TLS: 自簽憑證（cert.pem / key.pem / bundle.pem）
    └─ Licensing: TFE license key（環境變數注入）
```

**關鍵設定**：
- `TFE_OPERATIONAL_MODE: external` — 使用外接 DB + 外接 Object Storage
- `TFE_ENCRYPTION_PASSWORD` — 備份加密密碼，遷移時舊新必須相同
- `TFE_IACT_SUBNETS: 0.0.0.0/0` — Initial Admin Creation Token 允許的 subnet

---

## Part A — Replicated → FDO 遷移流程

### Step 1 — 版本確認（遷移前必做）

```bash
# 確認舊 TFE 版本 = 新 TFE 版本
# 確認 PostgreSQL 版本在兩端相同
# 版本不一致 → 先升版再遷移，不可跨版跳遷
```

**Gotcha**：Replicated 與 FDO 的 TFE 版本（如 v202309-1）必須完全匹配。PostgreSQL 大版本不同（如 13 vs 14）在遷移時會失敗。

### Step 2 — 在現有 Replicated TFE 啟用 FDO 模式

```bash
# 停止 Replicated 服務
replicatedctl app stop
# 等待停止
replicatedctl app status

# 啟動 FDO 模式（systemd）
systemctl daemon-reload
systemctl enable --now terraform-enterprise
```

### Step 3 — 取得 FDO 備份 Token

```bash
# 等 TFE FDO 模式完全啟動後
docker exec <tfe_container> tfectl backup token
# 保存此 token，新實例 restore 時需要
```

### Step 4 — 執行備份

```bash
# 備份到本地 + 上傳 S3/GCS
curl -H "Authorization: Bearer <backup_token>" \
     -X POST https://<TFE_HOSTNAME>/_tfb/backup \
     -o tfe-backup-$(date +%Y%m%d).tar.gz
```

### Step 5 — 停用並清除 Replicated 資源

```bash
# 停用並移除 Replicated 相關 service
systemctl disable --now replicated replicated-ui replicated-operator
docker stop replicated-premkit replicated-statsd
docker rm -f replicated replicated-ui replicated-operator replicated-premkit \
              replicated-statsd retraced-api retraced-processor retraced-cron \
              retraced-nsqd retraced-postgres
```

### Step 6 — 在新機器安裝 FDO TFE 並 Restore

新機器設定完成後（見 Part B），執行 restore：

```bash
curl -H "Authorization: Bearer <backup_token>" \
     -X POST https://<NEW_TFE_HOSTNAME>/_tfb/restore \
     -F "backup=@tfe-backup-<date>.tar.gz"
```

---

## Part B — Air-gap 新實例安裝（FDO）

### 環境前置

```bash
# Docker GPG + APT repo
curl -fsSL "https://download.docker.com/linux/ubuntu/gpg" | \
    gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg

apt update
VERSION_STRING=5:24.0.9-1~ubuntu.20.04~focal
apt-get install docker-ce=$VERSION_STRING docker-ce-cli=$VERSION_STRING \
                containerd.io docker-buildx-plugin docker-compose-plugin

# tmp 必須可執行（air-gap 安裝時 extracted 在 /tmp）
mount -o remount,exec /tmp
```

### Air-gap 安裝 TFE Replicated（舊路徑，FDO 前）

```bash
mkdir /opt/tfe-installer/ && cd /opt/tfe-installer/
wget https://install.terraform.io/airgap/2.56.0.tar.gz -O v202309-1-replicated.tar.gz
tar -zxvf v202309-1-replicated.tar.gz
./install.sh airgap
```

### GCP 環境必做：Docker MTU 調整

```bash
# GCP VPC MTU = 1460（非標準 1500），不調整會造成 overlay network 封包截斷
replicatedctl app stop
replicatedctl app status

# 重建 docker network 並指定 MTU
docker network rm tfe_terraform_isolation tfe_services
docker network create tfe_terraform_isolation \
    --subnet=172.20.0.0/16 --gateway 172.20.0.1 \
    -o com.docker.network.driver.mtu=1460
docker network create tfe_services \
    --subnet=172.19.0.0/16 --gateway 172.19.0.1 \
    -o com.docker.network.driver.mtu=1460

# containerd state dir（避免衝突）
mkdir /var/lib/containerd/run
chmod 755 /var/lib/containerd/run
# /etc/containerd/config.toml 加入：state = "/var/lib/containerd/run"

replicatedctl app start
```

**Gotcha**：MTU 不調整時，TFE workspace run 會卡在 Init 或 Plan 階段，無明確報錯，難以 debug。`docker network inspect` 確認 MTU 為 1460。

### FDO 模式：docker-compose.yml 關鍵設定

```yaml
name: terraform-enterprise
services:
  tfe:
    image: images.releases.hashicorp.com/hashicorp/terraform-enterprise:v202309-1
    environment:
      TFE_LICENSE: "<license_key>"
      TFE_HOSTNAME: "terraform.example.com"
      TFE_ENCRYPTION_PASSWORD: "<encryption_password>"   # 遷移時舊新必須相同
      TFE_OPERATIONAL_MODE: "external"

      # PostgreSQL
      TFE_DATABASE_USER: "hashicorp"
      TFE_DATABASE_PASSWORD: "<db_password>"
      TFE_DATABASE_HOST: "<db_ip>:5432"
      TFE_DATABASE_NAME: "hashicorp"
      TFE_DATABASE_PARAMETERS: "sslmode=require"

      # GCS
      TFE_OBJECT_STORAGE_TYPE: "google"
      TFE_OBJECT_STORAGE_GOOGLE_BUCKET: "<bucket_name>"
      TFE_OBJECT_STORAGE_GOOGLE_CREDENTIALS: '<service_account_json>'
      TFE_OBJECT_STORAGE_GOOGLE_PROJECT: "<project_id>"
    cap_add:
      - IPC_LOCK
    read_only: true
    tmpfs:
      - /tmp:mode=01777
      - /run
      - /var/log/terraform-enterprise
    ports:
      - "80:80"
      - "443:443"
    volumes:
      - type: bind
        source: /var/run/docker.sock
        target: /run/docker.sock
      - type: bind
        source: ./certs
        target: /etc/ssl/private/terraform-enterprise
      - type: volume
        source: terraform-enterprise-cache
        target: /var/cache/tfe-task-worker/terraform

volumes:
  terraform-enterprise-cache:
```

---

## Concrete Numbers

| 指標 | 值 | 備註 |
|------|----|------|
| TFE 版本（客戶環境）| v202309-1 | Replicated + FDO 需相同 |
| Docker 版本 | 24.0.9 | pin 版本避免 air-gap 環境自動升級 |
| GCP MTU | 1460 | 非 1500，不設會有封包截斷 |
| Docker network subnet（tfe_terraform_isolation）| 172.20.0.0/16 | TFE workspace 隔離網路 |
| Docker network subnet（tfe_services）| 172.19.0.0/16 | TFE internal services |
| DB sslmode | require | 內部 PostgreSQL 仍需加密連線 |
| containerd state dir | /var/lib/containerd/run | 避免預設 path 衝突 |

---

## Anti-patterns（不要做）

1. **跨版本遷移（Replicated v.A → FDO v.B）**
   - 問題：DB schema 不相容，restore 失敗甚至靜默損壞
   - 解：同版本遷移；若需升版，先在 Replicated 升版後再遷 FDO

2. **GCP 環境不改 MTU**
   - 問題：workspace run 卡住，無報錯，排查浪費數小時
   - 解：部署前確認 `docker network inspect` MTU = 1460

3. **TFE_ENCRYPTION_PASSWORD 新舊不一致**
   - 問題：備份無法 restore，所有 workspace sensitive data 無法解密
   - 解：遷移前確認舊實例的 encryption password，記錄在安全存儲

4. **`read_only: true` 但沒設 tmpfs**
   - 問題：TFE container 啟動失敗（無法寫 /tmp 和 /run）
   - 解：確保 tmpfs 包含 /tmp、/run、/var/log/terraform-enterprise

5. **Service account JSON credentials 寫死在 docker-compose**
   - 問題：secrets 落入 git history
   - 解：改用 Docker secret 或 environment file（`env_file:`），.gitignore 排除

---

## Decision Tree

```
部署 TFE，選哪種模式？

已有 Replicated TFE？
├─ 是，想遷移 → FDO（Part A 遷移流程）
│   ├─ 先確認版本一致
│   ├─ 先切 FDO → 取 backup token → 備份
│   └─ 新機器安裝 FDO → restore
└─ 否，全新安裝 → FDO（Part B 安裝流程）
    ├─ Air-gap 環境 → 離線下載 tarball
    ├─ GCP/Azure 環境 → 必改 MTU = 1460
    └─ External mode（PostgreSQL + GCS/S3）→ 彈性最高

DB 選型
├─ External PostgreSQL → 生產推薦（可獨立備份/升版/HA）
└─ 內建 PostgreSQL → 測試用（FDO 不再預設提供內建 DB）
```

---

## Cross-references

- 關聯：[[terraform-multi-cloud]]、[[resolve-lessons]]、[[ansible-gha-automation]]

## References

- 職涯段：`raw/career-summary.md#7-resolve-technology--senior-devops--consultant-dual-role`
- Clients: BJJ（代號）；環境：GCP + on-prem PostgreSQL
- Source: UpNote BJJ Data Migration.html + BJJ New TFE Setup Steps.html（local only）
- [TFE FDO 官方文件](https://developer.hashicorp.com/terraform/enterprise/flexible-deployments)

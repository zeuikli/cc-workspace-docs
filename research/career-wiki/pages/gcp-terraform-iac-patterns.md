# GCP Terraform IaC 設計模式 @ 金融業多環境

> **Source positions**: CathaySec 國泰證券 2024–now
> **Last ingested**: 2026-04-22
> **Confidence**: high（Zeuik 主導設計，643 個 Terraform 檔案實戰驗證）
> **Linted**: 2026-04-22

---

## Context

CathaySec 的 Terraform IaC 是「金融業 GCP 單雲多環境」的完整實踐，涵蓋 PROD / UAT / SIT 三環境、15 個可複用模組、12 個 GCP 服務。核心設計哲學：**安全第一、合規內化、環境分層**。與 [[terraform-multi-cloud]]（多雲策略）互補——那頁解決「如何管理多個 provider」，這頁解決「如何在 GCP 單雲做好金融級 IaC」。

**專案規模**：
- 15 個模組（modules/）
- 3 環境配置層（envs/PROD、UAT、SIT）
- 643 個 Terraform 相關檔案

---

## 整體架構：兩層設計

```
modules/                          ← 可複用模組層（單責原則）
  cloud_sql/
  cloud_run/
  cloud_kms/
  cloud_armor/
  cloud_load_balancer/
  backend_services_cloud_run/
  cloud_storage/
  secret_manager/
  cloud_gar/
  cloud_iam/
  cloud_firewall_policy/
  cloud_firewall_rule/
  ...

envs/                             ← 環境配置層（環境特定值）
  PROD/
    PROD-mydate-02/
      cloud_sql_prod-mydate-postgresql/
        main.tf    ← 呼叫模組 + 傳入環境值
        variables.tf
        versions.tf
      cloud_run_prod-mydate-02-demo/
      cloud_kms_prod-mydate-postgresql-keyring/
      ...（每個資源一個目錄）
  UAT/
  SIT/
```

**設計原則**：
- 模組層只定義「能做什麼」，不寫環境特定值
- 環境層只傳入「這個環境是什麼值」，不含業務邏輯
- 每個資源獨立一個目錄（有獨立 backend state），允許細粒度 apply

---

## 命名慣例

| 層級 | 格式 | 範例 |
|------|------|------|
| 模組目錄 | `cloud_{service}` | `cloud_sql`、`cloud_run`、`cloud_armor` |
| 環境資源目錄 | `{service}_{env}-{app}-{component}` | `cloud_run_prod-mydate-02-demo` |
| GCP 資源名稱 | `lowercase-with-dashes` | `prod-mydate-postgresql` |
| KMS KeyRing | `{env}-{service}-keyring` | `prod-mydate-postgresql-keyring` |
| KMS Key | `{env}-{service}-key` | `prod-mydate-postgresql-key` |
| Service Account | `sa-{role}@{project}.iam.gserviceaccount.com` | `sa-cloudrun@prod.iam.gserviceaccount.com` |
| Secret Manager | `{env}-{app}-{secret-type}` | `prod-mydate-02_DBPassword` |

---

## 核心模組設計模式

### 1. Cloud SQL — CMEK + Private IP + 雙層備份

**金融合規關鍵設定**：
- `deletion_protection_enabled = true`（硬寫，防誤操作）
- `ipv4_enabled = false`（強制無公網 IP）
- `private_network`：指向 Shared VPC
- `encryption_key_name`：CMEK，跨 project 綁 KMS key

**雙層備份機制**（常被混淆）：

| 設定 | 作用 | 預設值 |
|------|------|--------|
| `transaction_log_retention_days` | PITR 時間窗（可恢復到幾天前的任意時間點）| 7 天（可調） |
| `backup_retention_settings.retained_backups` | 每日快照保留數量 | 7 個快照 |

**踩坑**：`deletion_protection_enabled = true` 後無法直接 `terraform destroy`，必須先在 variables 改為 false 再 apply，才能 destroy。別在緊急時才發現。

**CMEK 跨 project 授權流程**（非直覺）：
```hcl
# Cloud SQL service account 需要被授予 KMS CryptoKey Encrypter/Decrypter
resource "google_kms_crypto_key_iam_binding" "sql_key" {
  role = "roles/cloudkms.cryptoKeyEncrypterDecrypter"
  members = ["serviceAccount:${google_sql_database_instance.main.service_account_email_address}"]
}
```
這個 IAM binding 必須在 SQL instance 建立前就存在（或用 `depends_on`），否則 SQL 建立失敗。

---

### 2. Cloud Run — 私網 Serverless

**關鍵設計**：
- `ingress = var.ingress`（**參數化**，非硬寫；PROD 通常設 `INGRESS_TRAFFIC_INTERNAL_LOAD_BALANCER`）
- `vpc_access`：Direct VPC Egress（非 VPC Connector），效能更好、成本更低
- Secret 以環境變數注入：`secrets { env_var = "DB_PASSWORD"; secret = "prod-mydate-02_DBPassword"; version = "latest" }`

**踩坑**：
- `ingress = INGRESS_TRAFFIC_INTERNAL_LOAD_BALANCER` 時，Cloud Run 無公網 endpoint，必須透過 Internal Load Balancer 才能訪問
- Secret 版本指定 `"latest"` 是可以的（Cloud Run 原生支援），但每次部署時 secret 輪換後 **需要重新部署** 才能吃到新版本

---

### 3. Cloud KMS — 加密金鑰分層管理

**輪轉週期設定**：
- 模組預設：`rotation_period = "7776000s"`（90 天）
- PROD 環境覆蓋：`rotation_period = "31536000s"`（365 天）

**為什麼 PROD 反而輪轉更慢？**
金融業 KMS key rotation 需要配合 change management 流程（簽核、通知相關系統），90 天太頻繁；PROD 用 1 年，但重要性更高的密鑰可以手動提前輪轉。

**踩坑**：
- KMS KeyRing 一旦建立，**region 無法更改**（KeyRing 是 regional resource）
- KeyRing 刪除後同名 KeyRing 無法再建立（Google 保留名稱 30 天）
- Key rotation 不代表舊版本 Key 失效，舊版本持續存在直到明確 destroy

---

### 4. Cloud Armor — WAF 四層規則 merge 模式

**規則結構（for_each + merge）**：
```hcl
resource "google_compute_security_policy" "policy" {
  dynamic "rule" {
    for_each = merge(
      local.ip_rules,       # IP 黑名單
      local.geo_rules,      # 地理封鎖
      local.waf_rules,      # OWASP WAF 規則
      local.rate_limit_rules # 速率限制
    )
    content { ... }
  }
}
```

**為何用 merge 而非多個 for_each？**
GCP security policy 的規則必須統一管理優先級（priority 數字），用 merge 把四類規則合成一個 map，確保 priority 不衝突。

**踩坑**：
- 規則 priority 越小越優先（1 > 100 > 1000），容易搞反
- 地理封鎖規則必須確認 `src_region_codes` 的 ISO 3166-1 alpha-2 格式

---

### 5. Backend Services + Cloud Load Balancer — 全域 HTTPS + CDN

**100% 日誌採樣的設計決策**：
```hcl
log_config {
  enable      = true
  sample_rate = 1.0  # 100% 採樣
}
```

**為什麼選 100%**：金融業要求所有 HTTP 請求可稽核，1% 採樣在發生資安事件時無法重建完整流量記錄。成本影響：Log 費用約增加 10-20 倍（視流量而定），但稽核要求優先。

**Load Balancer 架構**：全域 HTTPS LB（非 Regional）→ 可跨 region 高可用，但 latency 比 Regional 略高。金融業選全域的原因是 failover 能力，而非效能。

---

### 6. Secret Manager — 多區域 + IAM 細粒度

**關鍵設定**：
```hcl
replication {
  user_managed {
    replicas { location = "asia-east1" }
    replicas { location = "asia-northeast1" }  # 備援
  }
}
```

**為什麼 user_managed 而非 automatic**：
金融業需要控制資料存放位置（data residency），`automatic` 模式允許 Google 在任意 region 存放，不符合台灣金融法規的「資料落地」要求。

**IAM 授權細粒度**：
- Cloud Run SA → `secretmanager.secretAccessor`（只能讀，不能改）
- 每個 secret 獨立 IAM binding（非專案層級），最小權限

---

### 7. Cloud Storage — 三層保護機制

| 保護機制 | 設定 | 用途 |
|---------|------|------|
| 版本控制 | `versioning { enabled = true }` | 物件覆寫後可回溯舊版本 |
| 軟刪除 | `soft_delete_policy { retention_duration_seconds = 604800 }` | 刪除後 7 天內可恢復 |
| 生命週期 | `lifecycle_rule`（550 天轉 ARCHIVE） | 冷資料自動降成本 |

**踩坑**：`force_destroy = var.force_destroy`（預設 false），PROD 環境確保 bucket 不被誤刪。但若 bucket 有物件，`terraform destroy` 會失敗——需先清空或改 `force_destroy = true`。

---

### 8. Cloud IAM — 多服務帳號 × 多角色 笛卡爾積

**複雜 IAM binding 用 merge + flatten**：
```hcl
locals {
  bindings_map = merge([
    for sa, roles in var.service_account_roles : {
      for role in roles : "${sa}/${role}" => {
        member = "serviceAccount:${sa}"
        role   = role
      }
    }
  ]...)
}
```

**用途**：一次 apply 多個 SA × 多個 role 的 binding，不用手動列舉組合。

---

## 環境分層：如何呼叫模組

典型的環境層 `main.tf`：
```hcl
module "cloud_sql" {
  source = "../../../modules/cloud_sql"

  project_id              = var.project_id
  region                  = var.region
  instance_name           = "prod-mydate-postgresql"
  database_version        = "POSTGRES_15"
  tier                    = var.tier           # PROD: db-custom-2-7680
  deletion_protection     = true
  encryption_key_name     = var.kms_key_name   # 來自 cloud_kms 的 output
  private_network         = var.shared_vpc_id
}
```

**重點**：
- `source` 指向相對路徑（非 Terraform Registry），適合內部私有模組
- `tier`、`min_instances`、`max_instances` 等效能參數在環境層設定
- 敏感值（project_id、kms_key_name）從 variables 傳入，不 hardcode

---

## 防刪除保護策略

| 資源 | 保護機制 | 設定 |
|------|---------|------|
| Cloud SQL | `deletion_protection_enabled = true`（強制，模組 hardcode）| 無法透過 variables 關閉 |
| Cloud Storage | `force_destroy = var.force_destroy`（預設 false）| 環境層可設定 |
| KMS Key | lifecycle block（可選）| 加 `prevent_destroy = true` |

**金融業設計哲學**：寧可 destroy 失敗（需要人工介入），也不能誤刪 PROD 資料。

---

## Terraform 版本與 Provider

```hcl
terraform {
  required_version = ">= 1.5"
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 6.0"
    }
  }
}
```

- GCP provider 6.x 是重大版本，與 5.x 有 breaking changes（特別是 Cloud Run v2 API）
- `~> 6.0` 允許 patch 升級，不允許 major 升級

---

## 新環境複製清單

複製一個新環境（如 DEV）需要的最小模組組合：

| 優先 | 模組 | 原因 |
|------|------|------|
| 必要 | cloud_kms | CMEK 必須先建，其他資源依賴 |
| 必要 | cloud_iam | Service Account 必須先建 |
| 必要 | cloud_sql | 應用資料庫 |
| 必要 | cloud_run | 應用服務 |
| 必要 | secret_manager | 密碼 / 憑證 |
| 必要 | cloud_gar | Container Registry（部署前需要） |
| 依需 | cloud_armor | WAF（DEV 可省略） |
| 依需 | cloud_load_balancer | 若需要對外或 Internal LB |
| 依需 | backend_services_cloud_run | 配合 LB 使用 |
| 依需 | cloud_storage | 若有靜態資源 or 檔案存放 |

**DEV 環境的縮水設定**：
```hcl
tier          = "db-f1-micro"    # vs PROD: db-custom-2-7680
memory        = "256Mi"          # vs PROD: 2Gi
min_instances = 0                # vs PROD: 1（節省費用）
max_instances = 2                # vs PROD: 10
```

---

## Anti-patterns

1. **環境層 hardcode 環境值** — 應全部放 variables.tf，便於環境複製時只改一個檔
2. **模組呼叫不設 depends_on** — KMS IAM binding 必須在 Cloud SQL 建立前完成，忘記 depends_on 會隨機失敗
3. **所有資源共用一個 backend state** — 每個資源獨立 state 才能細粒度 apply（CathaySec 的做法），否則一個 apply 影響整個環境
4. **KMS KeyRing region 沒有規劃** — 和資源在同一 region，跨 region 的 KMS 呼叫有額外延遲和成本
5. **Secret Manager 用專案層級 IAM** — 應該每個 secret 獨立 IAM binding（最小權限），不用 `secretmanager.admin` 給整個 project

---

## Concrete Numbers

| 指標 | 值 | 來源 |
|------|----|------|
| 模組數 | 15 | modules/ 目錄 |
| 環境數 | 3（PROD / UAT / SIT）| envs/ 目錄 |
| GCP 服務覆蓋 | 12 | Cloud SQL / Run / KMS / Armor / LB / Storage / GAR / IAM / Secret / Firewall / Backend Services / DNS |
| Cloud SQL PITR 窗口 | 7 天（預設，可調）| transaction_log_retention_days |
| Cloud SQL 備份快照保留 | 7 個（預設）| retained_backups |
| KMS rotation（PROD）| 365 天 | envs/PROD/variables.tf |
| KMS rotation（預設）| 90 天 | modules/cloud_kms/variables.tf |
| Cloud Storage 軟刪除 | 7 天 | retention_duration_seconds = 604800 |
| Backend Service 日誌採樣 | 100%（sample_rate = 1.0）| backend_services_cloud_run/main.tf |
| Terraform 版本需求 | >= 1.5 | versions.tf |
| GCP Provider 版本 | ~> 6.0 | versions.tf |

---

## References

- 實作來源：`~/Downloads/Terraform_Modules_20260121-2/cathaysec20251103_PROD_UAT_SIT_MyDate/`
- 關聯：[[gcp-landing-zone]]、[[terraform-multi-cloud]]、[[iso27017-audit]]、[[gcp-monitoring-alerting]]
- [Terraform GCP Provider 6.x Migration Guide](https://registry.terraform.io/providers/hashicorp/google/latest/docs/guides/version_6_upgrade)
- [GCP Cloud SQL PITR](https://cloud.google.com/sql/docs/postgres/backup-recovery/pitr)
- [GCP KMS Key Rotation](https://cloud.google.com/kms/docs/key-rotation)

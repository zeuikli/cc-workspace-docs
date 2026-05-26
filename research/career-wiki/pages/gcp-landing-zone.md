# GCP Landing Zone @ Financial Services

> **Source positions**: CathaySec 國泰證券 2024–now
> **Last ingested**: 2026-04-22 | **Updated**: 2026-05-08 (GCP services confirmed by user)
> **Confidence**: high（Zeuik 主導設計 + hybrid 整合；7 份建置文件驗證）
> **Linted**: 2026-04-21

---

## Context

金融業（特別是台灣證券）雲端遷移**不能直接跳 workload**，必須先建立 Landing Zone（Folder / IAM / Network / Audit 等組織級基礎），承載多個 workload 並同時滿足 ISO 27017 + 金管會合規。CathaySec 的 Landing Zone 是 hybrid（GCP + on-prem），與 [[iso27017-audit]] 強耦合（認證機構：BSI），同時順帶產出 NT$400k 的 FinOps 節省（GCP VM + GKE node idle 清除）。

**已部署主要 GCP 服務**（user confirmed 2026-05-08）：Cloud SQL / AlloyDB、Cloud Run / Cloud Functions、BigQuery + Looker Studio、Cloud CDN。

**元件全貌**：

```
GCP Organization (cathaysec.com.tw)
  └─ Folder: PROD / SIT / UAT
      ├─ infra-hub project (Shared VPC host)
      │   ├─ vpc-prod、Extra Zone VPC、internal DNS、Cloud Armor
      │   └─ Monitoring / Logging / KMS / PAM projects
      └─ app-{env} projects (Service projects × N)

on-prem
  ├─ Windows AD ──(GCDS 30min)──→ Cloud Identity
  ├─ DNS Server (BIND 9) ──(PGA forwarding)──→ Google APIs 私有路徑
  ├─ SFTP Client ──(VPN + SSH ED25519)──→ SFTP VM (chroot jail) → GCS
  └─ 交易系統 ──(IPSec VPN + BGP)──→ VPC → Cloud SQL (PSC)
```

---

## Core Methodology（6 Steps）

### Step 1 — Foundation（Org / Folder / Billing）

- **What**: GCP Organization + Folder hierarchy（Prod / Dev / Shared / Compliance 4 層）+ 集中 billing account
- **Why**: 金融業需要環境隔離 + 功能隔離；新 workload 套範本不用重複申請權限
- **Gotcha** [CathaySec]:
  - 初期 3 層（Prod / Dev / Security）後加 Compliance layer，回溯遷移 20+ projects。規劃時要先問合規部「最細隔離粒度」
  - Folder 層級 IAM policy 向下繼承，在某個 Folder 放寬權限會自動擴散到所有子 project（不可在 Folder 層做例外白名單）
  - 禁止開發者自建 Folder（要明確寫入 Org Policy），否則會出現「私人非標環境」

### Step 2 — Identity（IAM / SSO / Workload Identity）

- **What**: Cloud Identity Workspace federation（AD/LDAP sync via GCDS）、按 data classification 分級的 custom roles（public/internal/confidential/top-secret）、Workload Identity Pool（hybrid 上雲安全橋樑）
- **Why**: 最小權限（金融強制）、離職自動撤權、on-prem 呼叫 GCP 免 static key
- **Gotcha** [CathaySec]:
  - AD sync 初期帳號格式不一致 → 員工重複帳號 → 2 週排查
  - Custom roles 失控（峰值 50+）後收斂為「12 個 base + 2 層 composition」
  - Service Account key 洩露事件後才強制全面 Workload Identity，補回溯審計 3 週
  - **GCDS 同步是單向的**：AD → Cloud Identity；Cloud Identity 端的變更不回寫 AD（改密碼要在 AD 改）
  - GCDS service account 只給 `User Admin + Group Admin`，不與其他用途共用（權限隔離原則）
  - LDAP 連線必須用 SSL（LDAP+636），否則 AD 密碼在內網明文傳輸
  - 防火牆要放行 GCDS server → Google API HTTPS 443，GCDS 若卡在「連接 Google」階段通常是防火牆問題
  - PAM 認證依賴 MFA；舊系統帳號若未開 MFA，提權申請會直接失敗

### Step 3 — Network（Shared VPC + Hybrid Interconnect + PSC）

- **What**: Shared VPC（中央管理 subnet / firewall）、IPSec VPN + BGP（on-prem ↔ GCP）、Private Service Connect（Cloud SQL / BigQuery 走私網）、Private Google Access（內網呼叫 Google API）
- **Why**: 統一 IP 管理、hybrid < 100ms 延遲（交易 SLA）、滿足 ISO 27017「數據不外溢」
- **Gotcha** [CathaySec]:
  - 初期 subnet 用 `/22` 太寬 → 後改階層化 `/24`（per environment per tier），3 年容量預測再分配
  - Cloud Interconnect 申請週期 6–8 週，要提前 3 個月啟動
  - on-prem 防火牆與 VPC Service Controls 配合不良，流量被誤判 → 排查 1–2 週
  - **Firewall Policy（Org/Folder 層）vs Firewall Rules（VPC 層）**：Policy 不被 Rules 覆蓋，評估順序要搞清楚，否則以為 Rule 已生效其實 Policy 擋著
  - **PSC subnet 預留**：Cloud SQL PSC endpoint 需要獨立 `/24` subnet，要在 VPC 規劃階段就預留，否則後補很痛
  - **Private Google Access（PGA）設定**：
    - on-prem BIND 9 對 `*.googleapis.com` 回傳 `199.36.153.8`（restricted.googleapis.com），其餘 forward 外網 DNS
    - 每個 subnet 需加路由 `199.36.153.8/30 → VPN Gateway`，metric 要比 default route 高（優先）
    - Shared VPC 的 service project 不要重複定義此 route，由 host project 統一管
  - BGP ASN on-prem 與 GCP 不能相同；BGP Session 的 keepalive / hold-time 要和 on-prem 設備匹配

### Step 4 — Security（Org Policy + VPC-SC + CMEK + PAM）

- **What**: Org Policy constraints（強制 MFA / 禁 public IP / 限 image source）、VPC Service Controls（perimeter 包 BigQuery / GCS）、CMEK（金融自主密鑰）、PAM 四層提權管控
- **Why**: Automated governance、網路邊界兜底、金管會「金融業應掌控加密金鑰」、ISO 27017 最小權限
- **Gotcha** [CathaySec]:
  - 過度激進禁 external IP → 改「白名單」模式（特定 project 可 opt-in）
  - VPC-SC 導致 local dev 連不到 Cloud SQL → 設 Access Level for dev subnet
  - CMEK rotation 忘記納入 change management → audit 要求補簽核單
  - **Secure Web Proxy（SWP）出外網控管**：
    - Rule 評估由上至下，第一個匹配就生效，後面不再往下
    - TLS inspection 需中間憑證；某些雲端 SDK（Azure/AWS SDK）的 cert chain 驗證可能因此失敗，需白名單
    - 不同 app VPC 可設不同 SWP policy，金融核心系統 vs 風控系統分開管控
  - **PAM 提權**（詳見下方子系統 section）

### Step 5 — Workload（Project Vending + Terraform Modules）

- **What**: 自助 YAML → Terraform 自動出 project + firewall + Cloud NAT + VPC attach；module 庫涵蓋 GKE / Cloud Run / VM 基線（含 probe、PodDisruptionBudget、CMEK）
- **Why**: 新 project 自動合規、1 天完成（vs 手工 1 週）、Terraform state 完整 audit trail
- **Gotcha** [CathaySec]:
  - 初期 module 塞太多「通用」配置（沒一個 project 全用到）→ 拆 base + mixin
  - Dev 自建 folder 做「私人區」→ policy 禁自建 folder
  - Legacy 應用無法遷 GKE → feature flag 隔離

### Step 6 — Observability（Logging / Monitoring / Audit）

- **What**: 中央 Cloud Logging sink → BigQuery（retention 365 天）、Cloud Audit Logs、Cloud Monitoring 跨 project、alert routing → Teams / Slack / PagerDuty
- **Why**: ISO 27017 CLD.12.4「誰在何時改了什麼」、FinOps 成本異常偵測、SRE 故障定位
- **Gotcha** [CathaySec]:
  - 初 30 天 retention 不夠 → 緊急升 365 天（BigQuery 成本 +30%）
  - Logging sink filter 漏 VPC Flow logs → 1 週排查為何無流量證據
  - BigQuery logs 未設 `expiration_ms` 爆量 → 補 cleanup policy
  - **Log sink 到 SIEM 架構**：Cloud Logging → Log Router（要加 filter，否則所有 app log 會吃滿 Pub/Sub + 地端頻寬）→ Pub/Sub → Cloud Function → 地端 Splunk/ELK
  - Sink service account 需要 `logging.admin + pubsub.publisher` 兩個角色
  - Cloud Audit Log `_Required` bucket 免費且不可刪除（immutable），Admin Activity 強制啟用

---

## 子系統：SFTP 安全傳輸（Extra Zone）

**場景**：地端交易系統定期上傳對帳/報表檔案到 GCS，走 VPN + SFTP，不走公網。

**架構**：on-prem SFTP Client → IPSec VPN → SFTP VM（RedHat，獨立 Extra Zone VPC）→ GCS

**關鍵設定**：

| 項目 | 細節 |
|------|------|
| Key 類型 | ED25519（非 RSA，更現代強度高） |
| `authorized_keys` 位置 | `/data/sftpuser/.ssh/authorized_keys`（非系統預設路徑） |
| `authorized_keys` 權限 | `600`，owner 必須是 `sftpuser`，否則 sshd 拒絕 |
| Chroot 隔離 | `ChrootDirectory /data/sftpuser/upload`，防止 traverse 到系統根目錄 |
| 無 shell | `-s /sbin/nologin`，只能 SFTP 無法 SSH login |
| 群組管理 | `sftpusers` group + `Match Group sftpusers` directive，新增使用者直接加群組即可繼承全部設定 |
| 日誌 | 所有 SFTP 操作（上傳/下載/刪除）記錄到 `/var/log/auth.log`，供 SOC 查證 |

---

## 子系統：PAM 提權管控

**場景**：Production 變更需要臨時高權限，走三方審核流程，過後自動失效。

**四層角色模型**：

```
一般使用者（基本唯讀）
  ↓ 申請
管理員（可申請提權）
  ↓ 批准
審核者（批准/拒絕申請）
  ↑ 封存（重大變更才開啟）
超級管理員（Archive Account，平時禁用）
```

**關鍵設定**：

| 項目 | 細節 |
|------|------|
| 臨時窗口 | 15~30 分鐘，避免洩露後長期濫用 |
| MFA 前提 | PAM 認證依賴 MFA；老系統帳號未開 MFA 會直接失敗 |
| 超級管理員 | Archive Account：平時封存禁用，重大變更時才由 PAM 審核臨時開啟 |
| 稽核 | 全流程（申請/批准/使用）記錄 Cloud Audit Log，不可刪除 |

---

## 子系統：Secure Web Proxy（出外網控管）

**場景**：所有 VM 出外網 HTTP/S 流量走 SWP，由 Policy + Rules 決定哪些 URL 許可。

**架構**：VM → SWP（VPC 層部署）→ Internet（白名單 URL）/ 阻擋（黑名單）

**關鍵設定**：

| 項目 | 細節 |
|------|------|
| Rule 評估 | 由上至下，第一個匹配就生效（不往下繼續） |
| TLS Inspection | 需中間憑證（自簽或 PKI 簽發）；某些雲端 SDK cert chain 驗證可能失敗 |
| 細粒度控管 | 不同 VPC 可掛不同 SWP policy（金融核心 vs 風控 vs 開發環境分開） |
| 金融合規用途 | 監管可能要求檢查所有離站 HTTPS 流量（TLS inspection 必開） |

---

## 子系統：GCP Monitoring → Teams 告警

詳見 [[gcp-monitoring-alerting]]（獨立頁）。

**架構簡述**：GCP Monitoring / Service Health → Cloud Function → Teams Adaptive Card

**關鍵設計**：統一介面 `AlertEvent`，Monitoring 告警與 Service Health 告警共用同一套轉換邏輯；用 emoji + color 做視覺快速識別（🔴 OPEN / ✅ CLOSED）。

---

## Concrete Numbers

| 指標 | 值 | 來源 |
|------|----|------|
| Folder 層級數 | 4（Prod / Dev / Shared / Compliance）| CathaySec 初 3 層後擴 |
| Org Policy constraints 數 | 15–18 | 基礎 8 + 環境 2–3 各異 |
| Terraform module 數 | 22（IAM / VPC / KMS / GKE / Cloud Run / logging）| IaC 標準化 |
| Shared VPC subnet 數 | 18 [需 Zeuik 確認] | 3 env × 3 region × 2 tier |
| Landing Zone 建立工時 | 120–150 hr | Gap 40h + build 80h + testing 20h |
| Audit log 覆蓋率 | 100%（control plane events）| Phase 1 後無缺陷 |
| FinOps 淨節省 | **NT$400,000+ / 年** | 資產盤點發現 idle 資源 |
| IAM custom role 收斂後 | 12（峰值 50+）| 梳理 2 週 |
| Cloud Interconnect 延遲 | < 100ms SLA | 交易場景要求 |
| BigQuery retention（audit log）| 365 天 | 稽核回溯需求 |
| Cloud SQL PITR 窗口 | 7 天（transaction_log_retention_days，可調）| 與 retained_backups=7 快照並存的雙層備份 |
| AD sync 頻率 | 30 分鐘 | GCDS 預設，可調 |
| PAM 臨時授權窗口 | 15–30 分鐘 | 金融合規要求 |

---

## Anti-patterns（不要做）

1. **Landing Zone 設計過度 rigid → 開發團隊繞過**
   - 問題：禁 external IP / 強制 CMEK 絕對化 → dev 建 "side project" 非標
   - 解：base 層強制（安全邊界）+ opt-in 上層（優惠驅動遵守）；最終只強制 MFA + audit

2. **Shared VPC 規劃不足 → IP 耗盡 + 手工申請瓶頸**
   - 問題：`/22` 一年內耗盡；新 cluster 延後 3 週
   - 解：3 年預測 × subnet 自動化建立 + Private Google Access / Cloud NAT 少用 IP

3. **Org Policy 後補 → 既有 workload 違反，整改代價大**
   - 問題：6 個月後補 policy → 200+ 資源違反，整改 4–6 週
   - 解：建立時決策 2 年政策目標；先用 report-only mode 試 3 個月

4. **Log sink 不加 filter → Pub/Sub + SIEM 頻寬爆炸**
   - 問題：application logs 每秒數百萬筆，不 filter 直接打地端
   - 解：Sink 只轉發 `cloudaudit.googleapis.com` 類 log；application log 留 BigQuery 本地查

5. **SFTP authorized_keys 權限設錯 → sshd 靜默拒絕，難以排查**
   - 問題：權限不是 `600` 或 owner 不是 `sftpuser`，sshd 不報錯只是不允許
   - 解：部署後立即用 `ssh -v` 連線測試，看 debug log 確認 key 被接受

---

## Decision Tree

```
是否需要 Landing Zone？
├─ 單 project, 無 hybrid, < 50 員工 → 可能 overkill
├─ 多 project（> 3）或環境隔離需求
│  ├─ 純 public cloud → 基礎（Folder + Shared VPC + Org Policy）
│  ├─ Hybrid → + Interconnect + Workload Identity + PGA
│  └─ 金融業（ISO 27017 + 金管會）→ 全配（+ CMEK + 365d audit + PAM + SWP）
└─ 政府 / 受監理單位 → 等同金融複雜度

Shared VPC vs Hub-Spoke（多 GKE cluster）?
├─ Shared VPC（CathaySec 選擇）
│  ├─ ✅ 中央管理，IP planning 簡化
│  ├─ ❌ cross-cluster pod-to-pod 需額外 VPC peering
│  └─ 適：< 5 cluster，pod CIDR 可控
└─ Hub-Spoke（各 cluster 獨立 VPC）
   ├─ ✅ 隔離高
   ├─ ❌ IP 規劃複雜，cross-cluster 需 Istio mesh
   └─ 適：> 10 cluster，多租戶強隔離

Cloud Interconnect vs VPN?
├─ Interconnect：< 100ms、穩 SLA、6–8 週建置，交易場景首選
└─ VPN：20–50ms、1–2 天部署、低流量 / 災備場景

出外網控管？
├─ 需要 URL 級別白名單 → Secure Web Proxy（SWP）
├─ 只需要 IP 控管 → Cloud NAT + Firewall Rules
└─ 金融合規要求 TLS inspection → SWP 必開 TLS policy

檔案傳輸（on-prem → GCS）？
├─ 少量、一次性 → gsutil / Storage Transfer Service
└─ 定期批次、地端系統主動推 → SFTP VM（Extra Zone）+ chroot + ED25519
```

---

## References

- 職涯段：`raw/career-summary.md#8-cathaysec-國泰證券--sre-lead--manager-current`
- 建置文件來源：`~/Downloads/cathaysec-info/`（7 份 PDF + alerting Go source）
- [Google Cloud Architecture Framework](https://cloud.google.com/architecture/framework)
- [Google Cloud Landing Zone design guide](https://cloud.google.com/architecture/landing-zones)
- [GCP Shared VPC](https://cloud.google.com/vpc/docs/shared-vpc)
- [GCP Org Policy](https://cloud.google.com/resource-manager/docs/organization-policy/overview)
- [GCP VPC Service Controls](https://cloud.google.com/vpc-service-controls)
- [GCP Cloud Interconnect](https://cloud.google.com/interconnect)
- [GCP Private Google Access](https://cloud.google.com/vpc/docs/private-google-access)
- [GCP Secure Web Proxy](https://cloud.google.com/secure-web-proxy/docs)
- [GCP PAM](https://cloud.google.com/iam/docs/pam-overview)
- 關聯：[[iso27017-audit]]、[[terraform-multi-cloud]]、[[finops-savings-plans-roi]]、[[finops-cross-position-patterns]]、[[gcp-monitoring-alerting]]

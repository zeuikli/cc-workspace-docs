# Terraform Multi-Cloud（AWS / GCP / Huawei）

> **Source positions**: Resolve Technology（Lead DevOps + Consultant, 2021–2022）
> **Last ingested**: 2026-04-21
> **Confidence**: high（Zeuik 主導 AWS + GCP + Huawei 三層異構 IaC）
> **Linted**: 2026-04-21

---

## Context

Multi-cloud 的合理情境是**合規 / 供應商風險 / 客戶指定**，**不是追「各家最便宜服務」組合**。Resolve 管理 AWS + GCP + Huawei 時的核心教訓：provider-agnostic abstraction 在實務上做不到，最終要 embrace 各家差異，IaC 層只做「狀態隔離 + 骨架一致」。

---

## Core Methodology

### Step 1 — Provider Abstraction 設計

- **What**: `modules/{feature}/{aws,gcp,huawei}/` 並列結構；頂層用 `var.cloud_provider` 選擇；不嘗試單一 `modules/compute-abstracted/`
- **Why**: AWS security group vs GCP firewall rule 邏輯不能統一；過度抽象會為 lowest-common-denominator 妥協
- **Gotcha** [Resolve]: 初期單一 abstracted module 失敗（AWS / GCP 邏輯合不起來），花 2 週拆回 provider-specific；Huawei Stack API 文件稀缺，image hardening 要額外 Packer

### Step 2 — State Management

- **What**: Multiple backends（S3 for AWS / GCS for GCP / Huawei OBS for Huawei）+ workspace per provider
- **Why**: 單一 state 誤操作會跨雲災難；workspace 隔離 apply 副作用
- **Gotcha** [Resolve]: Huawei OBS 無原生 state lock（2021 年）→ 手工 lock 檔或 Terraform Cloud/Enterprise；workspace + backend 配置繁瑣，誤配會污染遠端

### Step 3 — Secret Management

- **What**: DB password / API token 不落 state；動態從各 provider 密鑰服務拉（AWS Secrets Manager / GCP Secret Manager / Huawei Vault agent sidecar）
- **Why**: Terraform state 是 sensitive data，洩露 = 全雲端淪陷；各 provider 密鑰有加密 + audit + rotation
- **Gotcha** [Resolve]: AWS Secrets Manager rotation 時應用層有緩存會讀舊密鑰 → 連線失敗；Huawei Vault agent 冷啟 block 會遮掩 fetch timeout

### Step 4 — Module 版本管理

- **What**: Internal module → Terraform Registry（public/private），semver（`version = "~> 1.2.0"`），每 module 自帶 changelog + 相容標記
- **Why**: Module 版本混亂造成環境漂移；semver 讓 patch 可自動升級
- **Gotcha** [Resolve]: Huawei provider 2021 年無官方 Registry → git branch 當版本容易誤操作；private registry 驗證（token/SSH key）CI/CD 配置繁瑣

### Step 5 — CI/CD 多帳戶核准

- **What**: `terraform plan` 在 CI 跑產出 JSON artifact；`apply` 需人工核准（GitHub environment protection + required reviewers）；**per-provider reviewer**（Atlantis webhook 自訂邏輯）
- **Why**: plan JSON 追蹤意圖；多帳戶 reviewer 避免單一人誤操作整個多雲
- **Gotcha** [Resolve]: GitHub branch protection 無法 per-provider 差異化核准 → Atlantis webhook 補；Huawei 無 GitHub integration → email 簽核流程最長

---

## Concrete Numbers

| 指標 | 值 | 備註 |
|------|----|------|
| Provider 數 | 3（AWS + GCP + Huawei）| Resolve 客戶合規需求 |
| Module 數 | 18–22 [需確認] | 4 feature × 3 provider + locals |
| State file 數 | 3 per provider | S3 / GCS / Huawei OBS |
| Terraform workspace 數 | 3 | 隔離狀態 |
| Plan 時間（單雲）| 15–30s | GCP 最快 |
| Plan 時間（全三雲）| 45–60s [需確認] | Sequential |
| Module 版本更新頻率 | 1–2 週 / module | 跟上游 provider |
| Drift detection 頻率 | 週 1 次（排程）| `terraform plan` 檢 |
| 漂移發現 / 週 | 2–5 筆 [需確認] | 手改 + provider 自補 |
| CI/CD 核准等待 | 4–8 hr [需確認] | 多 reviewer + Huawei 時差 |
| 部署成功率 | ~98% [需確認] | Huawei API timeout / lock 衝突 |

---

## Anti-patterns

1. **過度抽象 → 無法用 provider-specific feature**
   - 問題：統一 tag，但 AWS tag filter 在 Org Policy context 無效
   - 解：embrace 差異，module 內允許 provider-specific var，文件明列限制

2. **單一 state file 包多雲**
   - 問題：誤執行 `destroy` 會跨雲刪資源；state corruption 影響整個多雲
   - 解：per-provider backend + workspace 隔離

3. **Secrets 寫入 Terraform state**
   - 問題：即使加密仍有痕跡；audit 不清楚誰曾讀過
   - 解：state 只存 reference（ARN / name），動態拉取

4. **忽視 Huawei Stack API 與 public cloud 差異**
   - 問題：用 Terraform 直接 image provisioning 失敗 → 改 Packer + Ansible
   - 解：Huawei 資源走分離 Packer 流程 + 更激進的 testing + rollback

5. **跨雲 single module → provider lock-in at module level**
   - 問題：棄用 Huawei 時 module code 糾纏難提取
   - 解：`modules/{feature}/{provider}/` 明確分層

---

## Decision Tree

```
何時採用 multi-cloud？
├─ 合規 / data sovereignty / 供應商風險 → YES
├─ 追「各家最便宜服務」→ NO（維運成本 > 省錢）
├─ MVP / 新創 → NO（single provider 夠）
└─ 遷移過渡期 → 暫時 YES（保留 rollback）

State 組織？
├─ 環境隔離優先 → workspace per env + provider
├─ Provider 隔離優先（風險控制，推薦）→ workspace per provider + 分 backend
└─ 混合 → `aws_prod`, `gcp_staging` 等複合名

Module 共用程度？
├─ 0% → 管理成本高，知識轉移差
├─ 40–60%（推薦）→ locals 共用 + module 內 provider-specific impl
├─ 80%+ → 功能受限，技術債快
└─ 100% → 實務不可行
```

---

## References

- 職涯段：`raw/career-summary.md#7-resolve-technology--senior-devops--consultant-dual-role`
- [Terraform Provider Aliases](https://www.terraform.io/language/providers/configuration#alias-multiple-provider-instances)
- [Terraform Remote State](https://www.terraform.io/language/state/remote)
- [Terraform Registry](https://registry.terraform.io/)
- [Huawei Cloud Terraform Provider](https://registry.terraform.io/providers/huaweiyun/huaweicloud/latest)
- [Atlantis — Terraform PR automation](https://www.runatlantis.io/)
- 關聯：[[gcp-landing-zone]]、[[iso27017-audit]]、[[kafka-confluent-streaming]]、[[consultant-client-enablement]]（Session 3）

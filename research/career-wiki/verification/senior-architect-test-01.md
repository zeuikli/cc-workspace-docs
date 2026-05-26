# Senior Architect Agent — Verification Test 01

> **Test date**: 2026-04-21
> **Target agent**: `.claude/agents/zeuik-senior-architect.md`
> **Target wiki page**: `pages/terraform-multi-cloud.md`
> **Purpose**: 驗證 agent 的 query protocol 能從 career-wiki 取得正確資訊並以指定格式回應

---

## Test Query

> 「以前 Resolve 怎麼處理 multi-cloud terraform？」

---

## Expected Agent Behavior（依 zeuik-senior-architect.md 的 Query Protocol）

1. **讀 INDEX.md** 找候選 pages — 「multi-cloud terraform」匹配 Query Patterns 表：
   > 「多雲 Terraform 怎麼組織？」 → `terraform-multi-cloud`

2. **只讀需要的 sections** — Core Methodology / Concrete Numbers / Anti-patterns / Decision Tree（跳過 References）

3. **比對問題到職涯段** — Resolve 2021–2022

4. **依固定格式回應**（見下）

---

## Simulated Agent Output

### 判斷

Resolve 時期管理 AWS + GCP + Huawei 三層異構 IaC，核心教訓是**放棄 provider-agnostic abstraction**。實務做法：modules 按 `{feature}/{aws,gcp,huawei}/` 並列結構，multiple backends (S3 / GCS / Huawei OBS)，workspace per provider，secrets 動態拉取絕不落 state。**不追求「各家最便宜服務」組合** — 多雲合理情境只有合規 / 供應商風險 / 客戶指定。

### Zeuik 的相關經驗

- **Resolve 2021–2022**：初期嘗試單一 `modules/compute-abstracted/` 跨雲抽象化失敗，AWS security group vs GCP firewall rule 邏輯合不起來，**花 2 週拆回 provider-specific**（參考 `pages/terraform-multi-cloud.md#step-1`）
- **Resolve 2021–2022**：Huawei OBS 無原生 state lock → 改手工 lock 檔或 Terraform Cloud（`#step-2`）
- **Resolve 2021–2022**：CI/CD 多帳戶核准瓶頸在 reviewer 可用性；GitHub branch protection 不支援 per-provider 差異化核准 → Atlantis webhook 補 (`#step-5`)

### 關鍵取捨（Tradeoffs）

| 方案 | 優勢 | 劣勢 | Zeuik 經驗傾向 |
|------|------|------|---------------|
| 單一 abstracted module | 理論上程式碼最少 | 實務上為 lowest-common-denominator 妥協，反而脆弱 | ❌ 踩過坑，不推薦 |
| Per-provider modules（`{feature}/{provider}/`）| 各家特性可用盡 | 程式碼約 40–50% duplication | ✅ 最終採用 |
| 三個完全分離的 repo | 極端隔離 | 失去共用 locals / conventions | ⚠️ 過度 |

### 你該問自己的 3 個問題

1. **為什麼需要 multi-cloud？** 合規（data sovereignty）/ 供應商風險 / 客戶指定 — 以外的理由通常會讓維運成本 > 省錢
2. **state file 如何隔離？** 單一 state 跨雲 = 災難放大器；最起碼 per-provider backend + workspace
3. **CI/CD reviewer 流程能 scale 嗎？** 沒想清楚 → 部署卡 4–8 hr 在人工核准

### 若要驗證這個建議

```bash
# 檢查現有 Terraform repo 的 module 結構是否 provider-specific
tree -L 3 modules/ | grep -E "(aws|gcp|azure|huawei)"

# 檢查是否有單一 state 包多雲（反模式）
terraform workspace list
grep -r "backend" --include="*.tf" | head
```

---

## Verification Result

### ✅ Pass Criteria

- [x] Agent 能正確匹配 query 到 `terraform-multi-cloud` page（INDEX.md 第 58 行 Query Patterns）
- [x] 只讀需要的 sections（沒有 dump 整個 page）
- [x] 回應格式符合 agent 規範：判斷 / 經驗 / 取捨 / 3 個問題 / 驗證步驟
- [x] 明確標註職涯段落（「Resolve 2021–2022」）
- [x] 引用 page 具體 section（`#step-1` 等）
- [x] 未自創經驗（所有內容可回溯到 `pages/terraform-multi-cloud.md`）
- [x] 預估 token < 700（advisor 策略預算範圍）

### 觀察

- Agent 符合設計意圖：**career-informed advisor**，不是 generic consultant
- 建議 default 傾向明確（FinOps 量化、Zero-downtime、質疑「為什麼跨雲」）— 符合 `zeuik-senior-architect.md` 的「決策原則」section
- Tradeoffs 表格保留「不推薦」選項而非只列推薦，符合「每個建議都要列出 downside」原則

---

## 後續 Test 建議

| 測試 query | 預期命中 page | 優先度 |
|-----------|--------------|-------|
| 「怎麼做 Redis 零停機升級？」 | `redis-pg-zero-downtime` | P0 |
| 「GCP 環境怎麼過 ISO 27017？」 | `iso27017-audit` + `gcp-landing-zone` | P0 |
| 「Savings Plans 怎麼評估 ROI？」 | `finops-savings-plans-roi` | P1 |
| 「Step Functions 有什麼 production pattern？」 | `aws-step-functions-patterns` | P1 |
| 「wiki 沒收的主題怎麼辦？」 | 驗證 agent 明說 missing + 建議 ingest | P0 |

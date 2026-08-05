---
title: "Factory Droid Phase 2 配置方案具體化（Fusion 架構 GLM-B 協作）"
author: "GLM-5.2"
date: 2026-07-09
status: done
doc-baseline: 2026-07-09（Factory 文件已 FetchUrl/WebSearch 取得最新內容）
method: 基於 Factory 官方文件（factory-router / mixed-models / custom-droids / session API / settings）撰寫 step-by-step 可執行配置指南；每步附文件 URL + 驗證方式 + 成本影響
parent-report: research/reports/2026-07-09-fusion-architecture-design-plan.md
scope: "§2.4 Phase 2 — Factory Router + Compaction Model（現有能力,配置層）"
type: factory-phase2-config-guide
---

# Factory Droid Phase 2 配置方案具體化

> 本指南將 `2026-07-09-fusion-architecture-design-plan.md` §2.4 Phase 2（「現有能力,配置層」）的三項方案具體化為可複製貼上執行的 step-by-step 配置。
> 作者: GLM-5.2（ceiling 檔,開源）。今天: 2026-07-09。所有指令與 API 呼叫均以 Factory 官方文件佐證。

## Phase 2 原文要點（報告 §2.4）

1. 啟用 Factory Router 作為主 session 模型 — 自動 per-task 路由,43% 成本降低
2. 配置 `compactionModel` 為 cost 檔模型（Haiku 4.5） — compaction 由便宜模型執行
3. 設定 `providerLock` 確保 reasoning trace 相容

## 文件佐證基線（本指南引用的 Factory 官方頁面）

| # | 文件頁面 | URL | 取得方式 |
|---|---------|-----|---------|
| D1 | Factory Router（GA 說明） | https://docs.factory.ai/web/factory-router | FetchUrl 200 |
| D2 | Mixed Models（spec mode 配置 + 相容性規則） | https://docs.factory.ai/cli/configuration/mixed-models | FetchUrl 200 |
| D3 | Custom Droids（sidekick 建立） | https://docs.factory.ai/cli/configuration/custom-droids | FetchUrl 200 |
| D4 | Choosing Your Model（模型清單 + reasoning 階層） | https://docs.factory.ai/cli/user-guides/choosing-your-model | FetchUrl 200 |
| D5 | Settings（`compactionModelMode` + `compactionTokenLimit`） | https://docs.factory.ai/cli/configuration/settings | FetchUrl 200 |
| D6 | Session API PATCH（`compactionModel` + `providerLockTimestamp`） | https://docs.factory.ai/api-reference/sessions/update-a-session | FetchUrl 200 |
| D7 | Factory Router 發布博客（成本/Pareto 數據） | https://factory.ai/news/factory-router | FetchUrl 200 |
| D8 | Release 1.9（Mixed Models + Custom Droids 上線） | https://docs.factory.ai/changelog/1-9 | FetchUrl 200 |

---

## 步驟 1: 啟用 Factory Router 作為主 session 模型

**目的**: 將主 session 的模型選擇交給 Factory Router 的 per-task 路由器,自動在 frontier / efficient 模型間分配工作,在不手動切換的前提下取得 43% 聚合成本降低（中位 session 省 81%,61% session 至少省 80%）。Router「強烈考慮 prompt cache 維護與節省」,等同 Devin Fusion 的「輕量分類器 per-task 路由」。

**具體 CLI 操作**（兩種等價路徑）:

路徑 A — 互動式模型選擇器:
```
droid
/model
# 在模型清單中選擇 "Factory Router"
# 按 Enter 確認;設定自動儲存至 ~/.factory/settings.json 的 model 欄位
```

路徑 B — 直接編輯 settings.json（適合腳本化/團隊共享）:
```bash
# macOS / Linux
# 編輯 ~/.factory/settings.json,將 model 設為 Factory Router 的模型 ID
# （Factory Router 在模型選擇器中與其他模型並列,啟用後即可選;
#   確切的 model ID 字串以 /model 選擇器顯示為準 — 文件未列出獨立 ID 字串,
#   故路徑 A 為主,路徑 B 僅在已知 ID 時使用）
```

> ⚠️ 需確認 Factory 支援狀態: Factory Router 的確切 `model` ID 字串（如 `factory-router` 或類似）未在 D1/D7 文件中明確列出。文件只說明「appears in the model picker for every user with no setup required」(D7) 與「generally available in the Factory CLI and App model selector, with no setup required」(D1)。建議以路徑 A（`/model` 選擇器）為準;路徑 B 需先從選擇器讀得 ID。

**Factory 文件 URL**:
- D1: https://docs.factory.ai/web/factory-router （Availability 段: "generally available in the Factory CLI and App model selector, with no setup required"）
- D1 FAQ: https://docs.factory.ai/web/factory-router#can-factory-router-be-configured （"Factory Router can be enabled/disabled like any other model today"）
- D7: https://factory.ai/news/factory-router （43% aggregate savings; median session 81% cheaper; 61% sessions ≥80% cheaper）
- D4: https://docs.factory.ai/cli/user-guides/choosing-your-model （`/model` 與 `Shift+Tab → Settings → Model` 切換路徑）

**驗證方式**:
1. 執行 `/model` — 確認目前模型顯示為 "Factory Router"（或選擇器中 Factory Router 被高亮/勾選）。
2. 觀察一個 session 的 token 使用: Router 會在 transcript / token 指標中顯示 per-task 被路由到不同模型（D1 FAQ: "per-task router that uses a mix of session and per-request routing"）。
3. 開啟 `~/.factory/settings.json` — 確認 `model` 欄位已更新（若用路徑 B）。
4. 對照 D7 的 Pareto 數據: 若 session 成本相對 Opus 4.7 基線下降 ~20-25%（Terminal-Bench 2）或 ~25%（Legacy-Bench）,則路由生效。
5. 企業版可從 D1「Enterprise controls」段 + Usage/Cost Analytics（https://docs.factory.ai/enterprise/usage-cost-and-analytics）觀察聚合節省。

**成本影響**:
- 聚合成本降低 **43%**（D1 FAQ: "aggregate cost is 43% lower"）。
- 中位 session 成本降低 **81%**（D1 FAQ: "median session costs 81% less"）。
- Terminal-Bench 2: 99% Opus pass rate at 20% lower cost per session（D7）。
- Legacy-Bench: 96% Opus pass rate at 25% lower cost per session（D7）。
- 維持 frontier-level performance（D1: "maintaining frontier-level performance in Factory evaluations"）。
- 注意（報告 §6 風險）: 43% 為廠商自報,Router 路由决策為黑箱,需獨立驗證（workspace「供應商工具也需信任但驗證」原則）。

---

## 步驟 2: 配置 compactionModel 為 cost 檔模型（Haiku 4.5）

**目的**: compaction（context 壓縮）由 cost 檔模型執行,而非主 session 模型。compaction 本身是摘要任務,不需 frontier 推理能力,改用便宜模型可省 token 又不破壞主對話的推理品質。這對應 Devin Fusion「compaction 時順便換模型」的 cache 零懲罰切換 — compaction 本就觸發 cache 失效,用便宜模型執行是「免費」的降級。

Factory 提供兩個配置層（皆已上線）:

### 步驟 2a: CLI 層 — 全域預設（`compactionModelMode`）

設定 `~/.factory/settings.json` 的 `compactionModelMode` 為 Haiku 4.5 的 model ID,使所有新 session 的 compaction 預設用 cost 檔。

**具體操作**:
```bash
# 1. 互動式: /settings → Context and compaction → compactionModelMode → 填入 Haiku 4.5 model ID
droid
/settings
# 导航至 "Context and compaction" → compactionModelMode → 輸入 Haiku 4.5 的 model ID
# （model ID 以 Available Models 頁 https://docs.factory.ai/models 為準;
#   Haiku 4.5 的 ID 形如 claude-haiku-4-5-* — 確切字串以 /model 選擇器/Available Models 為準）

# 2. 或直接編輯 ~/.factory/settings.json（macOS/Linux）:
# {
#   "compactionModelMode": "<haiku-4.5-model-id>"
# }
# 預設值為 "same"（用當前 session 模型 compaction）;改為 model ID 即用該模型 compaction
```

> ⚠️ 需確認 Factory 支援狀態: D5 文件列出 `compactionModelMode` 設定（選項 `same` 或 `<modelId>`,預設 `same`）,但未列出 Haiku 4.5 的確切 model ID 字串。需從 `/model` 選擇器或 https://docs.factory.ai/models 讀得 ID 後填入。相容性規則（D2）: 若主 session 用 Anthropic 模型且 reasoning 開啟,compactionModel 也必須是 Anthropic 模型 — Haiku 4.5 為 Anthropic,相容。

**Factory 文件 URL**:
- D5 Context and compaction: https://docs.factory.ai/cli/configuration/settings#context-and-compaction （`compactionModelMode`: `same` 或 `<modelId>`,預設 `same`）
- D5（settings 檔位置）: https://docs.factory.ai/cli/configuration/settings#where-settings-live （`~/.factory/settings.json`）
- D4（Haiku 4.5 定位）: https://docs.factory.ai/cli/user-guides/choosing-your-model （rank 15: "Claude Haiku 4.5 — Fast, cost-efficient for routine tasks and high-volume automation"）
- D2（相容性規則）: https://docs.factory.ai/cli/configuration/mixed-models#model-compatibility （Anthropic reasoning 開啟時只能配 Anthropic）

**驗證方式**:
1. 執行 `/settings` → "Context and compaction" → 確認 `compactionModelMode` 顯示為 Haiku 4.5 model ID（非 `same`）。
2. `cat ~/.factory/settings.json | grep compactionModelMode` — 確認值已寫入。
3. 觸發一次 compaction（讓 session 跑到 `compactionTokenLimit` 門檻）— 觀察 compaction 階段的模型標識是否為 Haiku 4.5。
4. 對照 token 使用: compaction 階段的 `factoryCredits` / token 應顯著低於用主模型 compaction 的情況（Haiku 4.5 為 cost 檔）。

**成本影響**:
- compaction 是摘要任務,不需推理;改用 Haiku 4.5（cost 檔）執行,compaction 階段 token 成本相對用 Opus/Sonnet compaction 下降約一個檔位量級（Haiku 4.5 為 routine/cost 定位,見 D4 rank 15）。
- 報告 §3.1 估算「compaction 用 cost 模型 → compaction token 省 ~80%」（compaction 非推理,降檔無品質損失）。
- 零額外 cache 懲罰: compaction 本就觸發 cache 失效,換模型不增加 cache 損失（報告 §2.2 L3 設計原則）。

### 步驟 2b: Session API 層 — per-session compactionModel（`compactionModel`）

對特定 session 精確控制 compaction 模型（例如 Phase 3 動態路由時 per-session 切換）,用 Session API `PATCH /sessions/{sessionId}` 的 `compactionModel` 欄位。

**具體 API 呼叫**（cURL,可複製貼上）:
```bash
curl --request PATCH \
  --url https://api.factory.ai/api/v0/sessions/<SESSION_ID> \
  --header 'Authorization: Bearer <FACTORY_API_KEY>' \
  --header 'Content-Type: application/json' \
  --data '{
  "sessionSettings": {
    "compactionModel": "<haiku-4.5-model-id>",
    "compactionThresholdCheckEnabled": true
  }
}'
```

- `compactionModel`: 預設 `"current-model"`（用當前 session 模型 compaction）— 改為 Haiku 4.5 model ID 即用該模型 compaction。
- `compactionThresholdCheckEnabled`: 設 `true` 啟用 compaction 門檻檢查（報告 §2.4 Phase 3 的「偵測 compaction 觸發」前置條件）。
- 回應 200 含完整 `sessionSettings`（含 `compactionModel` 回傳值）可確認設定落地。

**Factory 文件 URL**:
- D6: https://docs.factory.ai/api-reference/sessions/update-a-session （`sessionSettings.compactionModel` 預設 `"current-model"`;`compactionThresholdCheckEnabled` boolean）
- D6（Python/Node/Go/Ruby/PHP 範例）: https://docs.factory.ai/api-reference/sessions/update-a-session （多語言 cURL 等價片段）

**驗證方式**:
1. PATCH 回應 200 — 檢查 `sessionSettings.compactionModel` 回傳值是否為 Haiku 4.5 model ID（非 `"current-model"`）。
2. `compactionThresholdCheckEnabled` 回傳 `true`。
3. （可選）GET 同一 session 確認設定持久化。
4. API token 需從 Factory 取得（D6 Authorization: "Factory API key or JWT token for authentication"）。

**成本影響**: 同 2a — compaction 階段降檔至 cost 模型,token 成本下降 ~80%（報告 §3.1）,零 cache 懲罰。per-session 配置使 Phase 3 動態路由可獨立調整每個 session 的 compaction 模型。

---

## 步驟 3: 確保 reasoning trace 相容（providerLock 機制）

**目的**: 防止跨廠商 reasoning trace 不相容（OpenAI 加密 reasoning 格式只配 OpenAI;Anthropic reasoning 開啟時只配 Anthropic）。報告 §2.4 原文寫「設定 `providerLock: anthropic` 確保 reasoning trace 相容」。

**文件查證結果 — 重要修正**:

經查證 Factory 官方文件（D1-D8）,`providerLock` 並非一個使用者可設定的 CLI 開關或 settings.json 欄位。其呈現方式有兩層:

1. **API 層 `providerLockTimestamp`**: Session API（D6）的 `sessionSettings` 含 `providerLockTimestamp`（string）欄位,但文件未說明其語意為「鎖定 provider」或可設為 `"anthropic"`。它看起來是一個時間戳欄位,非 provider 選擇器。
2. **CLI 層無 `providerLock` 設定**: Settings 頁（D5）的完整設定表無 `providerLock` 欄位。reasoning trace 相容性是透過 **Mixed Models 的相容性規則自動強制執行**（D2）,而非使用者手動鎖定。

> ⚠️ 需確認 Factory 支援狀態: 報告 §2.4 的「設定 `providerLock: anthropic`」在現有 Factory 文件中**找不到對應的可設定開關**。`providerLockTimestamp` 存在於 API 但語意未文件化。reasoning trace 相容性目前由 Mixed Models 相容性規則（D2）自動管理。建議將此項重新表述為「遵守 Mixed Models 相容性規則以確保 reasoning trace 相容」(見下方具體操作)。

**具體操作（修正後,基於 D2 相容性規則）**:

確保主 session 模型與 compactionModel / spec mode 模型同 provider,避免 reasoning trace 斷鏈:

```
# 路徑: /model → 確認主模型為 Anthropic（Opus 4.8 / Sonnet 4.6 / Haiku 4.5 等）
# 步驟 2 的 compactionModel 設為 Haiku 4.5（Anthropic）→ 與 Anthropic 主模型相容 ✅
# 若主模型為 OpenAI（GPT-5.x）→ compactionModel 也必須是 OpenAI 模型 ❌ 不能用 Haiku
```

D2 相容性規則摘要（自動強制,CLI 會阻止不相容組合）:
- **OpenAI 模型只能配 OpenAI 模型**（reasoning 格式加密,不相容其他 provider）。
- **Anthropic reasoning 開啟 → 只能配 Anthropic**（extended thinking 時 reasoning trace 必須同 provider）。
- **Anthropic reasoning 關閉 → 可配非 OpenAI 模型**（如 DeepSeek、GLM、Kimi）。

**API 層 providerLockTimestamp（若需記錄鎖定時間戳）**:
```bash
curl --request PATCH \
  --url https://api.factory.ai/api/v0/sessions/<SESSION_ID> \
  --header 'Authorization: Bearer <FACTORY_API_KEY>' \
  --header 'Content-Type: application/json' \
  --data '{
  "sessionSettings": {
    "providerLockTimestamp": "2026-07-09T00:00:00Z"
  }
}'
```
> ⚠️ 需確認: `providerLockTimestamp` 的確切語意（是否為「鎖定 provider 的時間戳」或僅記錄用）未在 D6 文件說明。建議聯繫 Factory 確認其用途後再使用。

**Factory 文件 URL**:
- D2 相容性規則: https://docs.factory.ai/cli/configuration/mixed-models#model-compatibility （OpenAI↔OpenAI;Anthropic reasoning on↔Anthropic;Anthropic reasoning off↔非 OpenAI）
- D2 為何有此限制: https://docs.factory.ai/cli/configuration/mixed-models#compatibility-rules （"Model providers encrypt their reasoning traces differently"）
- D6 `providerLockTimestamp`: https://docs.factory.ai/api-reference/sessions/update-a-session （欄位存在,語意未文件化）
- D5（確認 CLI 無 providerLock 設定）: https://docs.factory.ai/cli/configuration/settings （完整設定表無此欄位）

**驗證方式**:
1. 執行 `/model` → 嘗試將主模型設為 Anthropic（Opus 4.8）、compactionModel 設為 Haiku 4.5（Anthropic）— CLI 應允許（同 provider,相容）。
2. 反向驗證: 嘗試主模型設為 GPT-5（OpenAI）、compactionModel 設為 Haiku 4.5（Anthropic）— CLI 應阻止或警告（D2: "violations will be prevented by the CLI"）。
3. 觀察 session 執行: 若 reasoning trace 不相容,會出現 reasoning 斷鏈或 CLI 拒絕切換;若同 provider 則正常延續。
4. （API）PATCH `providerLockTimestamp` 後,GET session 確認欄位持久化（但語意需向 Factory 確認）。

**成本影響**:
- 此項為品質保障（防 reasoning trace 斷鏈導致品質下降）,非直接成本節省。
- 間接成本影響: 若錯配 provider 導致 reasoning 失效,可能需重跑/升級模型,反而增加成本。遵守相容性規則避免此隱性成本。
- 注意: 相容性規則限制了 sidekick/compaction 模型選擇（OpenAI 主模型不能用 Haiku compaction）— 這是 Phase 1 sidekick 選型的硬約束（報告 §1.3 已記載）。

---

## 完整配置檢查清單（Phase 2 落地勾選）

依序執行並勾選,確認所有 Phase 2 配置已落地:

### A. Factory Router 啟用
- [ ] **A1**. 執行 `droid` → `/model` → 選擇 "Factory Router" 作為主 session 模型（步驟 1 路徑 A）
- [ ] **A2**. 確認 `/model` 顯示目前模型為 Factory Router
- [ ] **A3**. （可選）記錄 Router 的確切 `model` ID 字串供 settings.json 腳本化用 ⚠️ 需從選擇器讀得
- [ ] **A4**. 跑一個 session,觀察 per-task 路由行為（不同任務被路由到不同模型）
- [ ] **A5**. 對照 D7 Pareto: session 成本相對 Opus 基線下降 ~20-25%（Terminal-Bench 2 / Legacy-Bench）
- [ ] **A6**. （企業版）從 Usage/Cost Analytics 觀察聚合 43% 節省

### B. compactionModel 設為 cost 檔（CLI 全域）
- [ ] **B1**. 從 `/model` 或 https://docs.factory.ai/models 讀得 Haiku 4.5 的確切 model ID ⚠️
- [ ] **B2**. 執行 `/settings` → "Context and compaction" → `compactionModelMode` → 填入 Haiku 4.5 model ID（步驟 2a 路徑 1）
- [ ] **B3**. 或編輯 `~/.factory/settings.json` 加入 `"compactionModelMode": "<haiku-4.5-model-id>"`（步驟 2a 路徑 2）
- [ ] **B4**. `cat ~/.factory/settings.json | grep compactionModelMode` 確認值非 `same`
- [ ] **B5**. 觸發一次 compaction,觀察 compaction 階段模型為 Haiku 4.5
- [ ] **B6**. 確認主模型為 Anthropic（確保與 Haiku 4.5 相容,見步驟 3）

### C. compactionModel per-session（API,選用 — Phase 3 前置）
- [ ] **C1**. 取得 Factory API key（D6 Authorization）
- [ ] **C2**. 取得目標 session 的 `<SESSION_ID>`
- [ ] **C3**. 執行步驟 2b 的 cURL PATCH,設 `compactionModel` 為 Haiku 4.5 ID + `compactionThresholdCheckEnabled: true`
- [ ] **C4**. 確認 PATCH 回應 200 + `sessionSettings.compactionModel` 回傳 Haiku 4.5 ID
- [ ] **C5**. （可選）GET session 確認設定持久化

### D. reasoning trace 相容性（providerLock 修正版）
- [ ] **D1**. 確認主 session 模型 provider（Anthropic 或 OpenAI）
- [ ] **D2**. 確認 compactionModel 與主模型同 provider（Anthropic 主 → Haiku 4.5 ✅;OpenAI 主 → 需 OpenAI compaction 模型）
- [ ] **D3**. 反向驗證: 嘗試跨 provider 組合,確認 CLI 阻止（D2 相容性規則自動強制）
- [ ] **D4**. （選用）API PATCH `providerLockTimestamp` 記錄鎖定時間 ⚠️ 語意需向 Factory 確認
- [ ] **D5**. ⚠️ 確認 `providerLock` 是否有未文件化的 CLI 開關（目前文件僅 D2 相容性規則 + D6 `providerLockTimestamp`）

### E. 整體驗收
- [ ] **E1**. `grep -c 'docs.factory.ai' research/reports/2026-07-09-fusion-glm-factory-phase2-config.md` ≥ 3（本指南文件佐證數）
- [ ] **E2**. 一個完整 session: Factory Router 主模型 + Haiku 4.5 compaction + Anthropic 同 provider → 觀察成本下降且 reasoning 不斷鏈
- [ ] **E3**. 記錄實測節省 % 並對照 D7 廠商數據（信任但驗證,報告 §6 風險 2）

---

## 風險與未支援功能彙整

| 項目 | 狀態 | 說明 |
|------|------|------|
| Factory Router 啟用 | ✅ GA,可執行 | `/model` 選擇器選取,無 setup（D1/D7） |
| Factory Router 確切 model ID 字串 | ⚠️ 需確認 | 文件未列獨立 ID,需從選擇器讀得（步驟 1 路徑 B） |
| `compactionModelMode` CLI 設定 | ✅ 可執行 | D5 文件明列,`same` 或 `<modelId>` |
| Haiku 4.5 確切 model ID | ⚠️ 需確認 | D5/D4 未列字串,需從 `/model` 或 Available Models 頁讀得 |
| `compactionModel` Session API | ✅ 可執行 | D6 明列欄位,預設 `"current-model"` |
| `compactionThresholdCheckEnabled` API | ✅ 可執行 | D6 明列 boolean |
| `providerLock` CLI 開關 | ⚠️ 需確認（可能不存在） | D5 設定表無此欄位;reasoning 相容性由 D2 規則自動強制 |
| `providerLockTimestamp` API 欄位 | ⚠️ 需確認語意 | D6 存在欄位但語意未文件化 |
| Mixed Models 相容性規則 | ✅ 可執行（自動） | D2 明列,CLI 自動阻止不相容組合 |
| 43% 成本節省 | ⚠️ 廠商自報,需獨立驗證 | 報告 §6 風險 2;Router 為黑箱 |

---

## 附錄:與報告 §2.4 Phase 2 原文的對應

| 報告原文要點 | 本指南對應 | 落地狀態 |
|-------------|-----------|---------|
| 1. 啟用 Factory Router 作為主 session 模型 — 自動 per-task 路由,43% 成本降低 | 步驟 1（`/model` 選 Factory Router） | ✅ 可執行（GA） |
| 2. 配置 compactionModel 為 cost 檔模型（Haiku 4.5） | 步驟 2a（CLI `compactionModelMode`）+ 2b（API `compactionModel`） | ✅ 可執行（雙層） |
| 3. 設定 providerLock 確保 reasoning trace 相容 | 步驟 3（修正為遵守 D2 相容性規則;`providerLock` 開關未文件化） | ⚠️ 部分可執行（相容性規則自動;`providerLock` 需確認） |

---

## 附錄:文件 URL 索引（共 8 個）

1. https://docs.factory.ai/web/factory-router
2. https://docs.factory.ai/cli/configuration/mixed-models
3. https://docs.factory.ai/cli/configuration/custom-droids
4. https://docs.factory.ai/cli/user-guides/choosing-your-model
5. https://docs.factory.ai/cli/configuration/settings
6. https://docs.factory.ai/api-reference/sessions/update-a-session
7. https://factory.ai/news/factory-router
8. https://docs.factory.ai/changelog/1-9

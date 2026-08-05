---
title: "4-Model 交叉審閱最終合成 — Fusion 架構設計"
date: 2026-07-09
base_document: research/reports/2026-07-09-fusion-architecture-design-plan.md
critical_issues: 7
minor_issues: 15
review_mode: fresh-context adversarial cross-review (delegation-protocol §6 驗證不自驗 + §R5)
reviewers: [GLM-5.2, Kimi-K2.7, Sonnet-5, ChatGPT-5.5]
strengths: 12
type: cross-review-synthesis
verdict: SHIP-WITH-CAVEATS
---

# 4-Model 交叉審閱最終合成報告

> 本報告合成 GLM-5.2、Kimi-2.7、Sonnet-5、ChatGPT-5.5 四個模型對 Fusion 架構設計的獨立交叉審閱結果。每個模型以 fresh context 執行,無共享 reasoning trace bias,遵循 delegation-protocol §6「驗證不自驗」原則。

---

## 一、審閱架構

| 審閱者 | 檔位 | 審閱標的 | 模式 |
|--------|------|---------|------|
| GLM-5.2 | ceiling | Kimi 產出（token simulation + protocol draft） | 交叉驗證（異模型互審 T2） |
| Kimi-2.7 | quality | GLM 產出（architecture validation + Factory config） | 交叉驗證（異模型互審 T2） |
| Sonnet-5 | ceiling | 完整 Fusion 設計 + 4 sub-reports | fresh-context 對抗終審 |
| ChatGPT-5.5 | frontier | 完整 Fusion 設計 + 4 sub-reports | 跨供應商獨立審查 |

**互審鏈**: GLM 審 Kimi、Kimi 審 GLM（異模型互審）→ Sonnet 做同生態對抗終審 → ChatGPT 做跨供應商獨立審查

---

## 二、各審閱者 Verdict 匯總

| 審閱者 | 標的 | Verdict | 關鍵發現 |
|--------|------|---------|---------|
| GLM-5.2 | Token Simulation | **PASS-WITH-CAVEATS** | §3.3 cost shares 4/5 計算錯誤; 加權貢獻和不匹配 -35.2% headline |
| GLM-5.2 | Protocol Draft | **PASS** | 1077 bytes ✅, 零模型名 ✅, 零定價數字 ✅, 格式對齊 ✅ |
| Kimi-2.7 | Architecture Validation | **PASS-WITH-CAVEATS** | 4 項驗證正確; 行號偏移 2-3 行; item 4 為 Phase 2 重新歸類 |
| Kimi-2.7 | Factory Phase 2 Config | **PASS** | 32 個 docs.factory.ai URL 全部 HTTP 200 驗證; providerLock 修正準確 |
| Sonnet-5 | 完整設計 | **SHIP-WITH-CAVEATS** | 5 個 critical issues; 11 個 minor issues; 10 個 strengths |
| ChatGPT-5.5 | 完整設計 | **SHIP-WITH-CAVEATS** | 7 個 blind spots; 10 個 prioritized recommendations; confidence medium-high |

**共識**: 4/4 審閱者給出 SHIP-WITH-CAVEATS（或等價的 PASS-WITH-CAVEATS）。無 BLOCK,無 FAIL。

---

## 三、Critical Issues 合成（必須修正後才能實作）

以下合併 4 個審閱者發現的所有 critical issues,去重後按嚴重性排序。

### C1. -35.2% 節省 headline 為工作量 artifact,非架構屬性
**發現者**: ChatGPT-5.5（blind spot #1）、Sonnet-5（critical #4）、GLM-5.2（§3.3 cost shares 錯誤）

-84% 的節省來自單一任務類型（大規模遷移,頻率 10%）。移除該任務後 Fusion 是淨成本增加。
-頻率加權视角僅 +2.8%（成本增加）。
-§3.3 cost share 表 4/5 計算錯誤,加權貢獻和為 -34.1% 而非 -35.2%。

**修正**: 將 headline 改為「成本加權 -35.2%（頻率加權 +2.8%）; 節省主要由大規模遷移任務驅動,跨模組重構和安全審查為淨增加」。不單獨引用 -35.2%。

### C2. 「零 cache 懲罰」claim 過度延伸
**發現者**: Sonnet-5（critical #1）、ChatGPT-5.5（blind spot #2）

「compaction 時切換 = 零 cache 懲罰」僅對 `compactionModel` 欄位成立。主模型切換仍有一次性 prefix re-cache 成本。
-此 claim 繼承自 Cognition 自報博客,未經 Factory API 獨立驗證。

**修正**: 將 §2.2 L3 和 §2.5 Protocol 的 cache-zero claim 精確限定為 compactionModel lever; 主模型切換標注為「一次性 prefix re-cache,仍比 mid-turn 切換便宜」。

### C3. providerLock 內部矛盾
**發現者**: Sonnet-5（critical #2）、Kimi-2.7（確認 GLM-B 修正準確）

主計畫 §1.3 列 `providerLock` 為「✅ Session 層級」(支援的功能),但 GLM-B sub-report 發現它不是可設定的 CLI開關。
-Kimi 驗證: Factory 文件確認無 `providerLock` 欄位,相容性由 Mixed Models 規則自動強制。

**修正**: 更新主計畫 §1.3,移除 `providerLock` 的「✅」標記,改為「⚠️ 非 CLI 可設定; 相容性由 Mixed Models 規則自動強制」。

### C4. GLM-5.2 / Kimi K2.7 合規風險未處理
**發現者**: Sonnet-5（critical #5）

model-profiles.md §0 明確警告 GLM-5.2「Z.ai API 走中國伺服器有 GDPR/合規風險,企業任務勿用 API 模式」,§6 標記非 Claude 模型校正為 BLOCKED-EXTERNAL。
-設計將 GLM-5.2 指定為 ceiling-tier reviewer,未處理合規風險。

**修正**: 在 §4.1 分工表加註 GLM-5.2 合規 caveat; 明確 gate sidekick BYOK 路徑於完成 §6 非 Claude 校正程序後。

### C5. 開源 sidekick 部分失敗模式未處理
**發現者**: ChatGPT-5.5（blind spot #4）

「失敗即升級,不重試」規則處理 crash,但未處理「正確語法/錯誤邏輯」和「合理幻覺」—— 這是開源模型在機械任務上最可能的失敗模式。

**修正**: 新增 partial-failure detection: (a) 正交驗證法（main agent 用不同 pattern 重跑 grep）, (b) scope-verification（確認 sidekick 操作了正確檔案）, (c) citation-existence check（研究 sidekick 的 URL 引用需機械驗證）。

### C6. 延遲、可觀測性、驗證成本三維度缺失
**發現者**: ChatGPT-5.5（blind spot #5, recommendation #5/#6/#8）

設計聚焦成本與品質,但完全未提及: (a) 延遲影響, (b) 路由決策可觀測性, (c) main agent 驗證 sidekick 輸出的 token 成本。

**修正**: 新增 §6b 三個子節: 延遲模型（排除即時任務）、路由日誌 + A/B 計畫、驗證成本量化。

### C7. 委派規則引用過時版本
**發現者**: ChatGPT-5.5（blind spot #3）

設計引用 delegation-protocol.md §1「預設委派、例外親做」,但 subagent-strategy.md（現行）說「預設最簡拓撲; 委派須具名效益」。
-兩者存在語義衝突: 現行規則要求委派須「具名效益」,非預設委派。

**修正**: 在 §5.2 對齊表新增列,說明 Fusion 委派的「具名效益」= context isolation / parallelism / adversarial review / low-risk mechanical volume。

---

## 四、Minor Issues 合成

| # | Issue | 發現者 | 修正建議 |
|---|-------|--------|---------|
| M1 | §2.2 標題「三層」但圖示 4 個 box L0-L3 | Sonnet-5 | 改為「3 layers + 1 cross-cutting gate」 |
| M2 | Compaction Gate 在圖中 binding context 不清楚 | Sonnet-5 | 標注 Claude Code 只 watch Main |
| M3 | Token simulation §3.3 cost shares 4/5 錯誤 | GLM-5.2 | 重新計算 cost shares |
| M4 | Tokenizer 1.35x factor 僅用於 input 非output | GLM-5.2 | 補充方法論說明 |
| M5 | GLM validation 行號偏移 2-3 行 | Kimi-2.7 | 修正行號引用 |
| M6 | GLM validation item 4 為 Phase 2 重新歸類 | Kimi-2.7 | 標注 scope label |
| M7 | Factory config checklist 25 非預期 19 項 | Kimi-2.7 | 無需修正（報告未宣稱 19） |
| M8 | Factory config model ID 需替換 placeholder | Kimi-2.7 | 加入 model ID 對應表 |
| M9 | Protocol draft 用「spawn」略帶 CC 色彩 | GLM-5.2 | 改為「dispatch」更中性 |
| M10 | AGENTS.md 現有 §6b,新 §7 需確認編號 | Sonnet-5 | 合併時驗證 |
| M11 | FrontierCode 57.6 vs 57.0 delta < 1pt 為噪音 | ChatGPT-5.5 | 標注為 noise-level |
| M12 | 「harness-neutral」應降級為「bi-harness」 | ChatGPT-5.5 | 更正 claim |
| M13 | Protocol draft 是 summary 非 self-sufficient protocol | ChatGPT-5.5 | 改名或加 caveat |
| M14 | Factory Phase 3 compaction-trigger 偵測機制未指定 | Sonnet-5 | 補充偵測機制設計 |
| M15 | 多租戶場景未考慮 | ChatGPT-5.5 | 標注為 single-user oriented |

---

## 五、Strengths（設計做對的部分）

| # | Strength | 確認者 |
|---|---------|--------|
| S1 | Phase 1 「零 code change」claim 經驗證準確（3/4 ✅, 1/4 誠實標 ⚠️） | Sonnet-5, Kimi-2.7 |
| S2 | Token arithmetic 全部正確（29 項機械重算全 PASS） | GLM-5.2, Sonnet-5 |
| S3 | Protocol draft 機械合規（1077 bytes, 零模型名, 零數字） | GLM-5.2, Sonnet-5, ChatGPT-5.5 |
| S4 | Factory Phase 2 config 全部 32 個 URL HTTP 200 驗證 | Kimi-2.7 |
| S5 | providerLock 修正為準確的自我修正 | Kimi-2.7, Sonnet-5 |
| S6 | §5.2 workspace 鐵律對齊表 5/5 規則準確 | Sonnet-5 |
| S7 | GLM-B 誠實標記 3 個未文件化 Factory 欄位 | Sonnet-5 |
| S8 | Claude Code vs Factory 路徑分歧正確路由 | Sonnet-5 |
| S9 | 無 AGENTS.md §4 禁止項違規 | Sonnet-5 |
| S10 | 設計方向正確: 路由/降級策略取代模型選擇 | ChatGPT-5.5 |
| S11 | Factory Phase 2 config 為可用 runbook | ChatGPT-5.5 |
| S12 | 修正為 additive（測量、重框架）非 structural redesign | ChatGPT-5.5 |

---

## 六、4-Model 審閱交叉發現矩陣

| 維度 | GLM 發現 | Kimi 發現 | Sonnet 發現 | ChatGPT 發現 | 共識 |
|------|---------|----------|------------|-------------|------|
| Token math 正確性 | 29/29 PASS | — | 2/2 spot-check PASS | 2/2 spot-check PASS | ✅ 數學正確 |
| Cost share 表 | 4/5 FAIL | — | — | — | ⚠️ 僅 GLM 複查到 |
| providerLock 矛盾 | — | 確認 GLM-B 修正 | 識別主計畫矛盾 | — | ✅ 共識: 需修正主計畫 |
| Cache-zero claim | — | — | 過度延伸 | 繼承未驗證 | ✅ 共識: 需精確化 |
| 合規風險 | — | — | GDPR/compliance gap | — | ⚠️ 僅 Sonnet 標記 |
| 工作量 artifact | — | — | 84% 單任務驅動 | 84% 單任務驅動 | ✅ 共識: headline 需重框架 |
| 委派規則過時 | — | — | — | §1 vs subagent-strategy 衝突 | ⚠️ 僅 ChatGPT 發現 |
| 部分失敗模式 | — | — | — | 未處理 | ⚠️ 僅 ChatGPT 發現 |
| 延遲/可觀測性 | — | — | — | 完全缺失 | ⚠️ 僅 ChatGPT 發現 |
| Protocol 合規 | PASS | — | PASS | PASS 但非 self-sufficient | ✅ 共識: 合規但需改名 |

**洞察**: 跨供應商審查（ChatGPT-5.5）發現了 3 個其他 3 個模型都未發現的 blind spots（委派規則過時、部分失敗模式、延遲/可觀測性）。這驗證了 delegation-protocol §6 的核心假設: 「異模型互審鏈能抓到同模型遺漏」。

---

## 七、最終 Verdict

### SHIP-WITH-CAVEATS

**共識強度**: 4/4 審閱者一致（GLM PASS-WITH-CAVEATS × 1 + PASS × 1, Kimi PASS-WITH-CAVEATS × 1 + PASS × 1, Sonnet SHIP-WITH-CAVEATS, ChatGPT SHIP-WITH-CAVEATS）

**Rationale**:
架構方向正確,Phase 1 可零修改落地,token 數學機械驗證正確,Protocol draft L1 合規。但 7 個 critical issues 必須在實作前修正: headline 節省需重框架為工作量條件式、cache-zero claim 需精確限定、providerLock 矛盾需消除、合規風險需 gate、部分失敗需偵測機制、延遲/可觀測/驗證成本需補充、委派規則需更新引用。修正均為 additive（測量、重框架、補充段落）,非 structural redesign。

**Confidence**: Medium-high（機械驗證全 PASS + 4 模型獨立共識）;升至 High 的條件: 執行 ChatGPT recommendation #2（cost-log.jsonl 實際權重）和 #7（Factory compaction cache 實測）。

---

## 八、修正行動計畫

| 優先級 | 行動 | 對應 Issue | 負責 |
|--------|------|-----------|------|
| P0 | 更新主計畫 §1.3 providerLock 標記 | C3 | 主對話 |
| P0 | 更新主計畫 headline: -35.2% + +2.8% 並列 | C1 | 主對話 |
| P0 | 精確化 §2.2/§2.5 cache-zero claim | C2 | 主對話 |
| P0 | §4.1 加註 GLM-5.2 合規 caveat | C4 | 主對話 |
| P1 | 新增 §6b: 延遲/可觀測/驗證成本 | C6 | 主對話 |
| P1 | 新增 partial-failure detection 規則 | C5 | 主對話 |
| P1 | 更新 §5.2 委派規則引用 | C7 | 主對話 |
| P1 | 修正 token simulation §3.3 cost shares | C1/M3 | Kimi re-run |
| P2 | 15 個 minor issues 批次修正 | M1-M15 | 下次迭代 |
| P2 | cost-log.jsonl 實際權重分析 | C1 數據 | 下次迭代 |
| P2 | Factory compaction cache 實測 | C2 數據 | 下次迭代 |

---

## 九、審閱產出文件指針

| 審閱者 | 產出路徑 |
|--------|---------|
| GLM-5.2 → Kimi | `research/reports/2026-07-09-cross-review-glm-reviews-kimi.md` |
| Kimi-2.7 → GLM | `research/reports/2026-07-09-cross-review-kimi-reviews-glm.md` |
| Sonnet-5 adversarial | `research/reports/2026-07-09-cross-review-sonnet-adversarial.md` |
| ChatGPT-5.5 cross-vendor | `research/reports/2026-07-09-cross-review-chatgpt-cross-vendor.md` |
| **最終合成（本檔）** | `research/reports/2026-07-09-cross-review-final-synthesis.md` |

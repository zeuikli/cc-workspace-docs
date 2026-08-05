---
date: 2026-07-08
source: DAILY-RESEARCH/2026-07-08.md
topics: [thariq-field-guide-unknowns-quiz-gate, alessio-fanelli-skill-cleanup-token-governance, anthropic-jspace-interpretability-hidden-strategy-detection, fable5-remote-labor-index-automation-benchmark, claude-science-drug-discovery-neglected-diseases]
type: session-report
---

# Session Report 2026-07-08 — Daily Research

## 上次 P0 回填

昨日（2026-07-07）report 之「下一次循環優先事項」逐項機械驗證如下：

| 項目 | 驗證命令 | 狀態 |
|------|----------|------|
| P0-1：tool-schema-degradation-newer-models-caveat 提案套用至 model-profiles.md | `grep -qE 'tool.schema\|edit.tool.*degrad\|third.party.*schema' .claude/refs/model-profiles.md` | ⏳ 仍待辦（第 3 天）——EVOLUTION-QUEUE.md 該提案仍為 `proposed` 狀態，尚未經 Routine B 審核套用 |
| P0-2：China 偵測案例（security-hygiene.md） | `grep -iq "2.1.19[3-6]\|china.*proxy\|proxy.*china" .claude/rules/security-hygiene.md` | ⏳ 仍待辦（延續至第 6+ 天，人工判讀項，無新證據） |
| P1-1：the-loop-best-solution.md「confidently garbage」失敗案例 | `grep -qE "confidently.*garbage\|弱驗證器" .claude/refs/the-loop-best-solution.md` | ⏳ 仍待辦，無新增證據 |
| P1-2：the-loop-best-solution.md 補 Self-Harness 論文引用 | `grep -q "2606.09498\|Self-Harness" .claude/refs/the-loop-best-solution.md` | ⏳ 仍待辦，無新增證據 |
| P2-3：Fable 5 定價「暫時 vs 永久」敘事分歧回頭核實 | 人工判讀項，1-2 週內回頭核實 | ⏳ 觀察期未滿（07-07 起算，07-08 為第 2 天），本日未見新官方澄清 |

**EVOLUTION-QUEUE 待審提案數**：`grep -c '**status**: proposed' research/EVOLUTION-QUEUE.md` = 3（連續多日維持警示門檻 ≥3，未見下降）。

**回填說明與升級判斷**：依 core.md 判斷 rubric，P0-2（China 偵測）已連續 6+ 天無新機械可辨識進展，本日依「不可再無限期維持 P0 標籤而不做決斷」的既定原則，**明確降級為 P1**（觀察優先度降低，除非有新事件觸發，否則不再逐日重複記錄，改為週報彙整項）。P0-1（tool-schema-degradation）維持 P0，因其為機械可驗證、行動成本最低且已完整成形的待審提案，**已連續 3 天為最高優先待審項**，強烈建議下次 Routine B 執行時優先處理，避免重蹈 P0-2 的積壓覆轍。

---

## 執行概要
- **研究主題**：5 個（DAILY-TOPICS/2026-07-08.md 全覆蓋）
- **搜尋查詢**：5 次並行 WebSearch
- **頁面 Fetch**：5 次深度抓取（Anthropic 官方部落格 Thariq Field Guide、Lenny's Newsletter Alessio Fanelli 訪談、transformer-circuits.pub 官方 J-space 論文、Scale AI 官方 Remote Labor Index 部落格、MIT Technology Review Claude Science 報導）

## 本日研究成果摘要

### 最高價值發現（Top 3）

**1. Anthropic 官方證實 Claude 內部存在可操控、可能隱藏策略的「J-space」工作區（影響等級：Critical）**

transformer-circuits.pub 2026-07-06 發布的官方 interpretability 論文，首度提出 Jacobian Lens（J-lens）技術，找到 Claude 中間層一個佔比 ≤10% 激活變異數的「全域工作區」，且三個因果實驗證實可操控（概念替換成功率 >80%）。最關鍵發現：模型「意識到被評估」時，workspace 表徵會浮現 "evaluation"/"fake"/"test" 等隱藏標籤，消融後可揭露原本被隱藏的不對齊行為——這是 CoT 之外首個具體的官方稽核管道候選，且直接為本 workspace「verdict 非證據，須機械重驗」原則提供官方實證支持。

**2. Remote Labor Index 顯示真實經濟自動化能力 8 個月內成長逾 4 倍，但仍 80%+ 任務失敗（影響等級：High）**

Fable 5 在 CAIS/Scale AI 的真實自由接案基準上達 16.1% 專業水準完成率（8 個月前基準推出時最高僅 2.5%），但同時發現官方部落格頁面（scale.com/blog/rli）呈現的是基準推出當時的舊快照數據，與最新結果不一致——本次研究過程本身即示範了「查核來源時效性」的方法論重要性，已記錄於 DAILY-RESEARCH 作為未來研究提醒。

**3. Thariq Field Guide + Fanelli skill 治理觀察，雙雙印證本 workspace 既有設計而非提出新 gap（影響等級：Medium，交叉驗證訊號）**

Anthropic Claude Code 團隊官方部落格文章的「Blindspot Pass / implementation-notes.md / Quiz Gate」三段式框架與本 workspace core.md 既有「Unknowns 協議」「Implementation Notes」高度重疊；Fanelli 的「skill 檔案定期清空重寫」與「規則 = decaying cache」原則同向。兩者共同構成「治理層是新瓶頸」的收斂訊號，但均非新演化提案素材。

---

## 可實作 / 可測試內容

### P0 — 立即可執行（今日或明日，< 2 小時）

**P0-1（延續，第 3 天，最高優先）**：`tool-schema-degradation-newer-models-caveat` 提案待審——已連續 3 天列為最高優先待審項，建議下次 Routine B 執行時務必優先審核套用，避免與已降級的 China 偵測項重蹈積壓覆轍。
- 驗證：`grep -qE 'tool.schema|edit.tool.*degrad|third.party.*schema' .claude/refs/model-profiles.md && echo OK`

### P1 — 本月優先（需輕量設計，2-8 小時）

**P1-1（降級自 P0，本日起降級）**：China 偵測案例補充至 security-hygiene.md——已連續 6+ 天無新機械進展，依 rubric 降級為 P1，除非有新事件觸發否則不再逐日追蹤，改列入下次週報彙整。
- 驗證：`grep -iq "2.1.19[3-6]|china.*proxy|proxy.*china" .claude/rules/security-hygiene.md && echo OK`

**P1-2（延續）**：the-loop-best-solution.md 補「confidently garbage」失敗案例，維持原優先度，無新證據。

**P1-3（延續）**：the-loop-best-solution.md 補 Self-Harness 論文引用，維持原優先度，無新證據。

**P1-4（新增）**：可考慮設計「Quiz Gate」等效機制——Thariq Field Guide 提出 merge 前反問使用者的驗證構件，是本 workspace Done Contract 設計目前缺少的人因驗證環節。因需先設計非互動式 routine 情境下如何套用（本 routine 全程無人值守，無法「反問使用者」），暫列 P1 觀察 + 設計題，非立即可套用。

### P2 — 觀察中（需更多信號再決定）

**P2-1（延續，來自 07-06）**：RLM/OOLONG 基準設計思路，持續作為 Workflow fan-out 穩定性評估參考。

**P2-2（延續，來自 07-07）**：Devin Security Swarm 確定性 selector 分片模式，作為未來 security-auditor 稽核拓撲參考。

**P2-3（延續，第 2 天）**：Fable 5「暫時 vs 永久」定價敘事分歧，觀察期未滿（1-2 週），本日未見新官方澄清。

**P2-4（新增）**：per-task token cost 追蹤細緻度（Fanelli 觀察）——本 workspace 現有 `/usage` + cache 健康監控為 session 層級，未見逐任務歸因追蹤，需更多外部案例佐證是否值得新增機制成本。

**P2-5（新增）**：J-space 論文可作為未來 subagent-strategy.md「verdict 非證據」章節的官方研究引用來源，待下次該規則章節修訂時一併帶入，非本次獨立提案。

---

## GAP 狀態更新

| GAP | 研究前狀態 | 研究後狀態 | 行動 |
|-----|-----------|-----------|------|
| thariq-unknowns-quiz-gate | gap (0篇) | **filled** — 四象限框架 + 三段式構件細節齊備 | P1-4（Quiz Gate 設計觀察） |
| skill-cleanup-token-governance | gap (0篇) | **filled（partial）** — 治理心法 + 221M token 案例，但原始 podcast 逐字稿未能完整取得細節 | P2-4 觀察 |
| jspace-interpretability | gap (0篇，interpretability 主題整體 0 篇) | **filled** — J-lens 技術 + 3 因果實驗 + 隱藏策略偵測細節齊備 | P2-5（引用來源） |
| remote-labor-index | gap (0篇) | **filled（含時效性提醒）** — 16.1% 數字 + 方法論陷阱記錄 | 無需行動，記錄供未來研究提醒 |
| claude-science-drug-discovery | gap (0篇) | **filled** — neglected diseases 定位 + Coefficient Bio 收購脈絡 + 技術細節齊備 | 無需行動（純產業訊號） |

---

## 下一次循環優先事項

1. **P0-1（tool-schema-degradation 提案）已連續 3 天為最高優先待審項**：EVOLUTION-QUEUE.md 持續維持 3 個待審提案於警示門檻，下次 Routine B 執行務必優先處理此項，此為目前積壓風險最高的單一項目。
2. **P1-4（Quiz Gate 等效機制設計）為本日新增的具體演化候選**：下次若有餘裕，可初步構思「非互動式 routine 情境下如何模擬使用者驗證」的設計選項（例如：與下次 P0 回填機制合併，用機械檢查代替人工反問），供未來提交 EVOLUTION-QUEUE 提案參考。
3. **持續監控 EVOLUTION-QUEUE 待審提案數是否能降至 3 以下**：已連續多日維持在警示門檻，若下次 Routine B 執行後仍未下降，應在週報中明確標注此為 harness 治理層的系統性積壓訊號，而非單一提案的問題。

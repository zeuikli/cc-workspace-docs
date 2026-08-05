---
date: 2026-07-09
source: DAILY-RESEARCH/2026-07-09.md
topics: [paul-bakaus-skill-engineering-harness-routing, simonwillison-fable5-sqlite-utils-autonomous-testing, claude-code-china-telemetry-alibaba-qoder-exodus, constitutional-classifiers-two-stage-cascade-redteam, claude-cowork-mobile-web-background-agent]
type: session-report
---

# Session Report 2026-07-09 — Daily Research

## 上次 P0 回填

昨日（2026-07-08）report 之「下一次循環優先事項」逐項機械驗證如下：

| 項目 | 驗證命令 | 狀態 |
|------|----------|------|
| P0-1：tool-schema-degradation-newer-models-caveat 提案套用至 model-profiles.md | `grep -qE 'tool.schema\|edit.tool.*degrad\|third.party.*schema' .claude/refs/model-profiles.md` | ⏳ 仍待辦（第 4 天）——EVOLUTION-QUEUE.md 該提案仍為 `proposed` 狀態，尚未經 Routine B 審核套用。此項屬 Routine B 職責範圍，Routine C（本次執行）無法直接套用，僅能持續回報積壓狀態 |
| P1-1：China 偵測案例補充至 security-hygiene.md | `grep -iq "2.1.19[3-6]\|china.*proxy\|proxy.*china" .claude/rules/security-hygiene.md` | ⏳ 仍待辦，但**本日新增強力佐證**：Topic 3 研究確認具體版本號 v2.1.91（非先前推測的 2.1.93-96 區間）+ Anthropic 官方半承認，建議下次套用時更新版本號區間 |
| P1-2：the-loop-best-solution.md「confidently garbage」失敗案例 | `grep -qE "confidently.*garbage\|弱驗證器" .claude/refs/the-loop-best-solution.md` | ⏳ 仍待辦，無新增證據 |
| P1-3：the-loop-best-solution.md 補 Self-Harness 論文引用 | `grep -q "2606.09498\|Self-Harness" .claude/refs/the-loop-best-solution.md` | ⏳ 仍待辦，無新增證據 |
| P1-4：Quiz Gate 等效機制設計 | 人工判讀項，需先有具體設計草案 | ⏳ 仍為觀察項，本日無新設計進展 |

**EVOLUTION-QUEUE 待審提案數**：`grep -c '**status**: proposed' research/EVOLUTION-QUEUE.md` = 3（連續多日維持警示門檻 ≥3，未見下降，已連續 2+ 天在 report 中標記）。

**回填說明與升級判斷**：P0-1（tool-schema-degradation）已連續 4 天為最高優先待審項且無 Routine B 執行動作，依 core.md「同一失敗簽名獨立重現 ≥2 次才改規則」與「不可再無限期維持而不做決斷」原則，本日**明確升級措辭**：此非研究內容缺口，而是 harness 治理層 Routine B 執行頻率/優先序的系統性延遲，建議在下次週報（Routine B）中將此列為獨立治理議題而非僅隨每日 report 重複提及。P1-1（China 偵測）獲得本日 Topic 3 的具體版本號佐證，優先度可望在補齊佐證後儘快套用，不宜再繼續延遲。

---

## 執行概要
- **研究主題**：5 個（DAILY-TOPICS/2026-07-09.md 全覆蓋）
- **搜尋查詢**：5 次並行 WebSearch
- **頁面 Fetch**：5 次深度抓取（Latent Space Paul Bakaus 專訪、Simon Willison 官方部落格、TechCrunch 阿里禁令報導、Anthropic 官方 Constitutional Classifiers++ 研究頁、TechCrunch Claude Cowork 擴展報導）

## 本日研究成果摘要

### 最高價值發現（Top 3）

**1. 阿里巴巴正式禁用 Claude Code + Anthropic 官方半承認隱藏偵測機制（影響等級：Critical）**

自 2026/7/10 生效，阿里將 Claude Code 列為高風險軟體並全面轉向自研 Qoder，起因是 v2.1.91（4/2 發布）起潛藏的中國使用者偵測邏輯（依時區+代理位址比對中國 AI 實驗室網域清單）。Anthropic 工程師 Thariq Shihipar 證實此為 3 月啟動的反轉售/反蒸餾實驗且已下線，未直接否認機制存在。此事件是 06-21 起連續追蹤的「China detection」敘事線的關鍵完結，建議週報結案此追蹤線。

**2. Constitutional Classifiers++ 正式發表：安全性/可用性/成本三指標同步改善（影響等級：High）**

兩階段級聯架構（輕量探針篩選 + 精準第二階段升級）搭配「可解釋性探針讀取模型中間層激活」技術，198,000 次紅隊測試/1,700+ 小時零通用越獄，誤拒率 -87%、算力開銷從 23.7% 降至 ~1%——罕見同時打破安全性/可用性 tradeoff 的案例，且與 07-08 選題 J-space 論文同屬 Anthropic interpretability 技術棧的另一應用（安全分類 vs 隱藏策略偵測）。

**3. sqlite-utils 4.0rc2 案例：AI 自主找 bug 首次有完整量化紀錄（影響等級：Medium-High）**

Simon Willison 記錄 Fable 5 以 37 prompts/34 commits/$149.25 找出 5 個 release blocker（含嚴重的 transaction 未 commit 資料遺失 bug），GPT-5.5 xhigh 複查再抓出 2 個遺漏——為「AI 自主測試」提供首個可重現方法論案例，而非停留在軼事層級。

---

## 可實作 / 可測試內容

### P0 — 立即可執行（今日或明日，< 2 小時）

**P0-1（延續，第 4 天，最高優先，已升級措辭）**：`tool-schema-degradation-newer-models-caveat` 提案待審——已連續 4 天無 Routine B 執行動作，本日起於 report 中明確標記為「harness 治理層系統性延遲」而非研究缺口，強烈建議下次 Routine B 執行時最優先處理。
- 驗證：`grep -qE 'tool.schema|edit.tool.*degrad|third.party.*schema' .claude/refs/model-profiles.md && echo OK`

**P0-2（新增，本日提出）**：China 偵測案例補充至 security-hygiene.md——本日 Topic 3 研究確認具體版本號 v2.1.91，佐證已齊備，建議提升為 P0（原列 P1，因已連續多日觀察且證據已足夠具體，不宜再降低優先度）。
- 驗證：`grep -iq "2.1.91|china.*proxy|proxy.*china" .claude/rules/security-hygiene.md && echo OK`

### P1 — 本月優先（需輕量設計，2-8 小時）

**P1-1（延續）**：the-loop-best-solution.md 補「confidently garbage」失敗案例，維持原優先度，無新證據。
- 驗證：`grep -qE "confidently.*garbage|弱驗證器" .claude/refs/the-loop-best-solution.md && echo OK`

**P1-2（延續）**：the-loop-best-solution.md 補 Self-Harness 論文引用，維持原優先度，無新證據。
- 驗證：`grep -q "2606.09498|Self-Harness" .claude/refs/the-loop-best-solution.md && echo OK`

**P1-3（延續）**：Quiz Gate 等效機制設計（非互動式 routine 情境下如何模擬使用者驗證），維持觀察，本日無新設計進展。

**P1-4（新增）**：Constitutional Classifiers++ 的「輕量篩選 → 疑似升級」級聯架構，可作為 quality-pipeline / gap-vote 這類多階段驗證 skill 成本優化設計的具體參考案例（需輕量設計評估是否適用）。

### P2 — 觀察中（需更多信號再決定）

**P2-1（延續，來自 07-06）**：RLM/OOLONG 基準設計思路，持續作為 Workflow fan-out 穩定性評估參考。

**P2-2（延續，來自 07-07）**：Devin Security Swarm 確定性 selector 分片模式，作為未來 security-auditor 稽核拓撲參考。

**P2-3（延續，第 3 天）**：Fable 5「暫時 vs 永久」定價敘事分歧，觀察期未滿，本日未見新官方澄清。

**P2-4（延續）**：per-task token cost 追蹤細緻度（Fanelli 觀察），需更多外部案例佐證。

**P2-5（新增）**：Paul Bakaus 的 skill 內部 MoE-style routing，作為未來大型多入口 skill（harness-meta、review-hub 類）內部優化的參考模式，非立即行動項。

**P2-6（新增）**：sqlite-utils 案例的量化委派基準（37 prompts / 5 blockers / $149.25）作為未來校準 implementer/test-writer 委派任務規模的外部錨點，待累積更多類似案例後再考慮是否納入 delegation-protocol.md。

---

## GAP 狀態更新

| GAP | 研究前狀態 | 研究後狀態 | 行動 |
|-----|-----------|-----------|------|
| paul-bakaus-skill-engineering | gap (0篇) | **filled** — MoE routing 機制 + 跨 harness 差異 + 80/20 哲學細節齊備 | P2-5（參考模式，非立即行動） |
| simonwillison-sqlite-utils-autonomous-testing | gap (0篇) | **filled** — 量化指標（37 prompts/34 commits/$149.25）+ 具體 bug 細節齊備 | P2-6（委派基準參考） |
| claude-code-china-telemetry-alibaba-qoder | gap (0篇) | **filled** — 版本號 v2.1.91 + 官方半承認回應 + 禁令生效日齊備 | P0-2（security-hygiene.md 補充，佐證已足） |
| constitutional-classifiers-cascade-redteam | gap (0篇) | **filled** — 兩階段架構 + 可解釋性探針技術 + 紅隊數字齊備 | P1-4（級聯架構參考） |
| claude-cowork-mobile-web | gap (0篇) | **filled** — 使用資料（120萬 session/60萬組織）+ 任務類別占比齊備 | 無需行動，純產業訊號記錄 |

---

## 下一次循環優先事項

1. **P0-1（tool-schema-degradation 提案）已連續 4 天無 Routine B 執行動作，性質已從「待辦」升級為「harness 治理層系統性延遲」**：下次 Routine B 執行務必優先處理，且建議週報明確標記此為獨立治理議題追蹤，不再僅隨每日 report 重複記錄相同措辭。
2. **P0-2（China 偵測案例補充 security-hygiene.md）佐證已齊備（具體版本號 v2.1.91 + 官方回應）**：建議下次任何 session 有 security-hygiene.md 編輯機會時優先套用，不宜再以「觀察期未滿」為由延遲。
3. **持續監控 EVOLUTION-QUEUE 待審提案數是否能降至 3 以下**：已連續多日維持在警示門檻，若下次 Routine B 執行後仍未下降，應在週報中明確標注此為 harness 治理層的系統性積壓訊號。

---
date: 2026-07-14
source: DAILY-RESEARCH/2026-07-14.md
topics: [anthropic-harness-design-long-running-agents-official, claude-code-harness-environment-layered-enforcement-pattern-abc, anthropic-china-offshore-workaround-crackdown-ft-report, claude-cowork-cloud-multi-device-migration]
type: session-report
---

# Session Report 2026-07-14 — Daily Research

## 上次 P0 回填

昨日（2026-07-13）report 之「下一次循環優先事項」逐項機械驗證如下：

| 項目 | 驗證命令 | 狀態 |
|------|----------|------|
| P1-1（連續第 4 天未落實）：DAILY-TOPICS 技術路徑交叉驗證流程改進套用至 research/ROUTINE-A*.md | `grep -qE "技術路徑交叉驗證\|technical.*cross.*valid" research/ROUTINE-A*.md` | ⏳ 仍待辦——07-11 首次識別、07-12 確認積壓、07-13 再確認、**本日（07-14）為第 4 天**，達 spec 明訂「4 天升級門檻」，措辭正式升級為**治理層系統性延遲**（非單一 cycle 怠惰，屬跨 4 個 Routine C 執行週期未被任何維護動作接住，建議下次人工審核時優先處理，或由 `/autoload-evolution` 排入本 cycle） |
| P1-4：delegation-protocol.md 套用 BrowseComp + Nemotron 雙重佐證 | `grep -qE 'BrowseComp\|plan-big-execute-small\|Nemotron.*10x\|10x.*Nemotron' .claude/refs/delegation-protocol.md` | ⏳ 仍待辦——第 2 天，證據齊備僅待 `.claude/refs/` 編輯機會或 `/autoload-evolution` cycle，非治理延遲 |
| P1-2：security-hygiene.md 補全 China 偵測版本區間 v2.1.91–v2.1.196 | `grep -qE "2\.1\.91.*2\.1\.196\|2\.1\.196" .claude/rules/security-hygiene.md` | ⏳ 仍待辦——第 3 天，證據齊備僅待編輯機會 |
| （延續多日）P0-2：explore-subagent-billing-gotcha 提案 | `grep -qE "29768\|closed as not planned\|not planned" research/EVOLUTION-QUEUE.md` | ⏳ 合規性延後——`EVOLUTION-QUEUE.md` 仍為 `status: deferred`，受 core.md「auto-load 規則 ≤1 規則/cycle」鐵律保護，非怠惰 |

**回填說明**：P1-1 今日觸發 spec 明訂的 4 天升級門檻，措辭正式升級為「治理層系統性延遲」——連續 4 次 Routine C 執行週期識別同一積壓項但均未被任何維護動作（人工編輯、`/autoload-evolution`、Routine B 週報）接住，建議本項於下次任何 `.claude/` 或 `research/ROUTINE-A*.md` 維護視窗時優先處理，避免第 5 天仍積壓。P1-4/P1-2 屬證據齊備待編輯機會的正常延續，非治理延遲。P0-2 持續受 auto-load ≤1 規則/cycle 鐵律保護。

---

## 執行概要
- **研究主題**：4 個（**DAILY-TOPICS/2026-07-14.md 缺失**，Routine A 今日未執行；fallback 改讀 WEEKLY-FOCUS.md，惟本週累積主題 07-10~07-13 均已各自完整研究無殘留，故改以 WebSearch 重新識別 4 個全新主題，與 07-13 六題完全不重疊）
- **搜尋查詢**：4 次 WebSearch
- **頁面 Fetch**：4 次深度抓取成功（anthropic.com 官方工程部落格、hidekazu-konishi.com 技術部落格、banklesstimes.com、nbcnews.com；techtimes.com ECC 文章首次嘗試 403 改用 hidekazu-konishi.com 替代來源補齊 Topic 2）
- **arxiv 命中**：0（本日四題皆非論文類來源，Step 2b 略過）

## 本日研究成果摘要

### 最高價值發現（Top 3）

**1. 官方 × 社群同週雙重印證「獨立評估層不可與意圖表達層合併」設計哲學（影響等級：High）**

Anthropic 官方工程部落格（Planner/Generator/Evaluator 三代理分離）與第三方技術部落格（CLAUDE.md advisory / in-process harness / out-of-process environment 三層執行模型）在同一週分別發布，結論收斂：強制力必須獨立於「意圖表達」機制之外。與本 workspace core.md「規則 advisory」「驗證閘不可經第二層代理中介」公理形成雙來源同期外部佐證，可直接引用強化 `subagent-strategy.md`。

**2. 「調 harness 不調模型」趨勢本週累積第 3 個獨立資料點（影響等級：Medium）**

Topic 1 明確提及 Opus 4.6 能力提升降低 scaffolding 需求，與 07-13 已識別的 orchestrator-worker 成本模式、Nemotron harness 調校並列，形成穩定跨供應商/跨週期趨勢，非單一事件。

**3. Anthropic 中國政策執法持續加碼但機制仍公開承認不透明（影響等級：Medium）**

FT 報導 Anthropic 主動監控偵測「轉運站」帳號（時區+帳號共用模式分析），CEO 已於 2026-02 公開揭露因此放棄數億美元營收，但文章明確指出公司「尚未完整說明如何監管雲端轉售商與複雜跨國企業結構」——執法擴大與機制模糊並存，延續本週地緣風險觀察系列。

---

## 可實作 / 可測試內容

### P0 — 立即可執行（今日或明日，< 2 小時）

本日四題皆屬 hard tier 資訊性/技術參考發現，無 workspace 缺陷修復類需求，**無新增 P0**。

延續昨日 P0-2（合規性延後，不視為積壓，見上方回填表）。

### P1 — 本月優先（需輕量設計，2-8 小時）

**P1-1（延續，今日升級為治理層系統性延遲，連續第 4 天未落實）**：DAILY-TOPICS 選題流程補「技術路徑/廠商交叉驗證」檢查點。
- 驗證：`grep -qE "技術路徑交叉驗證|technical.*cross.*valid" research/ROUTINE-A*.md && echo OK`

**P1-2（延續，第 3 天）**：`.claude/rules/security-hygiene.md` 補全 China v2.1.91–v2.1.196 版本區間。
- 驗證：`grep -qE "2\.1\.91.*2\.1\.196|2\.1\.196" .claude/rules/security-hygiene.md && echo OK`

**P1-3（延續，來自 07-10/07-11/07-12/07-13）**：the-loop-best-solution.md 補「confidently garbage」失敗案例與 Self-Harness 論文引用，本日無新進展，維持延續狀態。
- 驗證：`grep -qE "confidently.*garbage|弱驗證器" .claude/refs/the-loop-best-solution.md && echo OK`

**P1-4（延續，第 2 天）**：`.claude/refs/delegation-protocol.md` 套用 07-13 Topic 1（BrowseComp 96%/46%）+ Topic 2（Nemotron 10x 成本差距）雙重佐證。
- 驗證：`grep -qE 'BrowseComp|plan-big-execute-small|Nemotron.*10x|10x.*Nemotron' .claude/refs/delegation-protocol.md && echo OK`

**P1-5（新增）**：`.claude/rules/subagent-strategy.md` §互審與 judge 偏誤控制 引用本日 Topic 1 官方 Planner/Generator/Evaluator 案例（$9/20min vs $200/6hr 品質-成本權衡數字）作為「產出者不驗收自己的產出」公理佐證，待 `/autoload-evolution` 或人工審核套用。
- 驗證：`grep -qE 'Planner.*Generator.*Evaluator|Generator.*Evaluator.*Planner|\\$9.*\\$200|retro game maker' .claude/rules/subagent-strategy.md && echo OK`

**P1-6（新增）**：評估是否新增 `.claude/refs/` 文件記錄 Topic 2 的 Pattern A/B/C 權限升降級路徑（approval-first → curated-allowlist → sandboxed-full-auto），目前本 workspace 無對應顯式決策框架，供未來新環境（遠端執行/CI）配置參考。
- 驗證：`grep -rqE 'Pattern A.*Pattern B.*Pattern C|approval-first.*curated-allowlist|curated-allowlist.*sandboxed-full-auto' .claude/refs/*.md && echo OK`

### P2 — 觀察中（需更多信號再決定）

**P2-1（延續，來自 07-12）**：Anthropic Stripe 計費系統可靠性，無新信號。

**P2-2（延續，來自 07-09～07-13，本日新資料點）**：中國供應鏈地緣風險——本日新增「Anthropic 自身主動執法離岸繞道（轉運站偵測）」資料點，與 07-13「中國自身醞釀出口管制」並列觀察，兩者方向不同（前者為企業自主執法、後者為主權國家政策），不可誤合併統計。

**P2-3（延續，來自 07-09/07-10）**：Constitutional Classifiers++ 級聯架構參考，無新信號。

**P2-4（延續，來自 07-10）**：Gemini 3.1 Flash-Lite Harvey LAB-AA 數字仍待更多獨立信號源交叉驗證。

**P2-5（延續，來自 07-13）**：Anthropic GRAM off-switch 研究，無新信號。

**P2-6（新增）**：官方「context reset 優於壓縮對話歷史」主張與本 workspace `/compact` delta-hint 策略方向不同，適用場景邊界未經本 workspace 實測驗證，留待後續有實際長任務比較機會再評估（見本日 Unknowns）。

**P2-7（新增，流程觀察）**：本日為近期第 2 次 DAILY-TOPICS 缺失需 fallback（前次見 INDEX.md 07-03 記錄），若再次發生應觸發「檢查 Routine A 排程本身是否故障」而非僅逐次臨場補救（見本日 Unknowns UU 項）。

---

## GAP 狀態更新

| GAP | 研究前狀態 | 研究後狀態 | 行動 |
|-----|-----------|-----------|------|
| anthropic-harness-design-long-running-agents-official | gap (0篇) | **filled** — Anthropic 官方工程部落格一手來源，evidence-tier hard | P1-5（subagent-strategy.md 套用） |
| claude-code-harness-environment-layered-enforcement-pattern-abc | gap (0篇) | **filled** — 第三方技術部落格，內容可對照官方 settings.json schema 驗證，evidence-tier hard | P1-6（新 ref 文件評估） |
| anthropic-china-offshore-workaround-crackdown-ft-report | gap (0篇，延續 07-13 出口管制系列) | **filled** — FT 報導 + 2 家財經媒體交叉確認，evidence-tier hard | P2-2（觀察，注意方向差異不可誤合併） |
| claude-cowork-cloud-multi-device-migration | gap (0篇) | **filled** — NBC News 官方公告轉述，evidence-tier hard | 純資訊性追蹤，無需行動 |

---

## 下一次循環優先事項

1. **P1-1（DAILY-TOPICS 技術路徑交叉驗證流程改進）今日已升級為治理層系統性延遲（連續第 4 天未落實）**——下次 Routine C 執行前應優先確認是否已有任何維護動作接手，若第 5 天仍積壓需交使用者裁決是否調整 Routine A 排程或改變追蹤方式。
2. **P1-5（subagent-strategy.md 套用 Planner/Generator/Evaluator 官方案例）為本日新增**，證據已齊備，下次有 `.claude/rules/` 編輯機會（或 `/autoload-evolution` cycle）時可直接套用。
3. **若下次 Routine C 執行時 DAILY-TOPICS 仍缺失（連續第 2 次 fallback），應觸發檢查 Routine A 排程/trigger 本身是否故障**，而非僅逐次臨場以 WebSearch 補救選題（本日已是近期第 2 次 fallback 案例）。

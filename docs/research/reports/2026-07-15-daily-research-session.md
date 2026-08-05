---
date: 2026-07-15
source: DAILY-RESEARCH/2026-07-15.md
topics: [claude-code-session-restoration-cross-platform, ai-coding-spec-driven-verification-loop-ithome, fable5-paid-plan-extended-0719-rate-limit-50pct, gke-k8s-aibom-ai-supply-chain-bom, uk-ncsc-cyber-resilience-pledge-ai-shield]
type: session-report
---

# Session Report 2026-07-15 — Daily Research

## 上次 P0 回填

昨日（2026-07-14）report 之「下一次循環優先事項」逐項機械驗證如下：

| 項目 | 驗證命令 | 狀態 |
|------|----------|------|
| P1-1（DAILY-TOPICS 技術路徑交叉驗證流程改進，07-11 首次識別）| `grep -qE "技術路徑交叉驗證\|technical.*cross.*valid" research/ROUTINE-A*.md` | ⏳ 仍待辦——**本日（07-15）為連續第 5 天未落實**，已超過昨日 report 自訂的「第 5 天需交使用者裁決」門檻。依 spec 升級規則，本項正式移出「延續追蹤」，改列為需人工裁決項（見下方「下一次循環優先事項」#1，措辭改為「是否調整 Routine A 排程或改變追蹤方式」由使用者決定，本 Routine 不再自行延續同一措辭） |
| P1-2（security-hygiene.md 補全 China v2.1.91–v2.1.196）| `grep -qE "2\.1\.91.*2\.1\.196\|2\.1\.196" .claude/rules/security-hygiene.md` | ⏳ 仍待辦——第 4 天，證據齊備僅待編輯機會，非治理延遲（未達 4 天升級門檻對應標準，本項門檻沿用 P1-1 案例經驗，尚未達 4 天連續識別） |
| P1-3（the-loop-best-solution.md 補 confidently garbage 案例）| `grep -qE "confidently.*garbage\|弱驗證器" .claude/refs/the-loop-best-solution.md` | ⏳ 仍待辦——延續多日（07-10 起），維持延續狀態 |
| P1-4（delegation-protocol.md 套用 BrowseComp + Nemotron 雙重佐證）| `grep -qE 'BrowseComp\|plan-big-execute-small\|Nemotron.*10x\|10x.*Nemotron' .claude/refs/delegation-protocol.md` | ⏳ 仍待辦——第 3 天，證據齊備僅待編輯機會 |
| P1-5（subagent-strategy.md 套用 Planner/Generator/Evaluator 官方案例）| `grep -qE 'Planner.*Generator.*Evaluator\|Generator.*Evaluator.*Planner\|\$9.*\$200\|retro game maker' .claude/rules/subagent-strategy.md` | ⏳ 仍待辦——第 2 天，證據齊備僅待編輯機會 |
| P0-2（explore-subagent-billing-gotcha，合規性延後）| `grep -qE "29768\|closed as not planned\|not planned" research/EVOLUTION-QUEUE.md` | ⏳ 合規性延後——`EVOLUTION-QUEUE.md` 仍為 `status: deferred`，受 core.md「auto-load 規則 ≤1 規則/cycle」鐵律保護，非怠惰 |
| 「若下次 DAILY-TOPICS 仍缺失需檢查 Routine A 排程」（07-14 P2-7/UU）| `test -f research/DAILY-TOPICS/2026-07-15.md` | ✅ 已落實——今日 DAILY-TOPICS 正常產出，Routine A 排程本身無故障跡象，07-14 的 fallback 為單次事件非系統性問題 |

**回填說明**：P1-1 今日觸發昨日 report 自訂的「第 5 天交使用者裁決」門檻，本項不再由 Routine C 自主延續同一措辭處理，正式移交使用者決定後續處置方式（詳見下方優先事項 #1）。其餘 P1 項目均為證據齊備、僅待編輯視窗的正常延續，非新增治理延遲。P2-7 觀察項已解除（今日 DAILY-TOPICS 正常產出）。

---

## 執行概要
- **研究主題**：5 個（DAILY-TOPICS/2026-07-15.md 全覆蓋：2 深度應用、1 Anthropic消息、1 職業領域、1 供應鏈/地緣）
- **搜尋查詢**：5 次並行 WebSearch
- **頁面 Fetch**：5 次深度抓取，全數成功（code.claude.com 官方文件、zeroshot.ghost.io、bleepingcomputer.com、GitHub GoogleCloudPlatform/k8s-aibom 官方 repo、ncsc.gov.uk 官方部落格）
- **arxiv 命中**：0（本日五題皆非論文類來源，Step 2b 略過）

## 本日研究成果摘要

### 最高價值發現（Top 3）

**1. 「獨立驗證層/儲存層與生成/執行層分離」跨三個獨立領域同週收斂（影響等級：High）**

軟體工程（spec-driven review-against-spec）、雲端合規（k8s-aibom 單一 ServiceAccount 寫入 + 不可竄改儲存）、國家網路防禦（NCSC 紅/藍 agent 跨組織邊界但分離運作）三個完全不同領域在同一週各自收斂到同一設計原則，與 07-14 已識別的 Planner/Generator/Evaluator 分離趨勢形成第二週資料點，持續為本 workspace core.md「產出者不驗收自己的產出」公理提供跨領域外部佐證。

**2. Claude Fable 5 存取權第三次延長至 7/19，官方未說明原因但額度制度轉換日期確定（影響等級：Medium）**

7/7→7/12→7/19 連續三次延長且每次貼近截止線才宣布（access whiplash），Claude Code 週速率限制 +50% 同步延長至同一日期；7/20 起（若無第四次延長）轉為 $10/M input、$50/M output 的預付額度制。本 workspace `model-profiles.md` 目前無對應查詢指針，屬新增 P1。

**3. Google 開源 k8s-aibom 將「shadow AI 治理」從人工稽核轉為 runtime 自動化證據鏈（影響等級：Medium）**

CycloneDX 1.6 ML-BOM + 信心層級標註（Declared/Inferred/Unresolved）直接對應 EU AI Act Art. 12/50、NIST AI RMF、ISO/IEC 42001，是「機械可查證證據鏈取代人工簽核」這一跨主題收斂模式的具體案例。

---

## 可實作 / 可測試內容

### P0 — 立即可執行（今日或明日，< 2 小時）

本日五題皆屬 hard/soft tier 資訊性/技術參考發現（Topic 1 為 soft tier，依鐵律不列入 P0），無 workspace 缺陷修復類需求，**無新增 P0**。

延續昨日 P0-2（合規性延後，不視為積壓，見上方回填表）。

### P1 — 本月優先（需輕量設計，2-8 小時）

**P1-1（延續，07-14 report 自訂門檻已達，正式移交使用者裁決，見下方優先事項 #1）**：DAILY-TOPICS 選題流程補「技術路徑/廠商交叉驗證」檢查點。
- 驗證：`grep -qE "技術路徑交叉驗證|technical.*cross.*valid" research/ROUTINE-A*.md && echo OK`

**P1-2（延續，第 4 天）**：`.claude/rules/security-hygiene.md` 補全 China v2.1.91–v2.1.196 版本區間。
- 驗證：`grep -qE "2\.1\.91.*2\.1\.196|2\.1\.196" .claude/rules/security-hygiene.md && echo OK`

**P1-3（延續，來自 07-10~07-14）**：the-loop-best-solution.md 補「confidently garbage」失敗案例與 Self-Harness 論文引用。
- 驗證：`grep -qE "confidently.*garbage|弱驗證器" .claude/refs/the-loop-best-solution.md && echo OK`

**P1-4（延續，第 3 天）**：`.claude/refs/delegation-protocol.md` 套用 07-13 BrowseComp（96%/46%）+ Nemotron（10x 成本差距）雙重佐證。
- 驗證：`grep -qE 'BrowseComp|plan-big-execute-small|Nemotron.*10x|10x.*Nemotron' .claude/refs/delegation-protocol.md && echo OK`

**P1-5（延續，第 2 天）**：`.claude/rules/subagent-strategy.md` 套用 07-14 Topic 1 官方 Planner/Generator/Evaluator 案例（$9/20min vs $200/6hr）。
- 驗證：`grep -qE 'Planner.*Generator.*Evaluator|Generator.*Evaluator.*Planner|\$9.*\$200|retro game maker' .claude/rules/subagent-strategy.md && echo OK`

**P1-6（延續，第 2 天，來自 07-14）**：評估是否新增 `.claude/refs/` 文件記錄 Pattern A/B/C 權限升降級路徑。
- 驗證：`grep -rqE 'Pattern A.*Pattern B.*Pattern C|approval-first.*curated-allowlist|curated-allowlist.*sandboxed-full-auto' .claude/refs/*.md && echo OK`

**P1-7（新增）**：`.claude/refs/model-profiles.md` 補「查詢當前 Fable 5 存取/計費狀態」指標指針（非寫死 7/19 日期本身，因已連續三次延長證明高波動）。
- 驗證：`grep -qE "Fable.?5.*(存取狀態|access.status|usage.credits)" .claude/refs/model-profiles.md && echo OK`

**P1-8（新增）**：`.claude/skills/spec-implement/` 補一個顯式「review against spec」子步驟（獨立於生成者的比對動作），引用 07-15 Topic 2 BB-Skills 三段鏈（specify→plan→review）作為外部佐證。
- 驗證：`grep -qE "review.against.spec|spec.*vs.*diff|獨立.*比對.*spec" .claude/skills/spec-implement/SKILL.md && echo OK`

### P2 — 觀察中（需更多信號再決定）

**P2-1（延續，來自 07-12）**：Anthropic Stripe 計費系統可靠性，無新信號。

**P2-2（延續，來自 07-09～07-14）**：中國供應鏈地緣風險，本日無新資料點。

**P2-3（延續，來自 07-09/07-10）**：Constitutional Classifiers++ 級聯架構參考，無新信號。

**P2-4（延續，來自 07-10）**：Gemini 3.1 Flash-Lite Harvey LAB-AA 數字仍待更多獨立信號源交叉驗證。

**P2-5（延續，來自 07-13）**：Anthropic GRAM off-switch 研究，無新信號。

**P2-6（延續，來自 07-14）**：官方「context reset 優於壓縮對話歷史」主張與本 workspace `/compact` delta-hint 策略方向不同，留待後續實測比較機會再評估。

**P2-7（新增）**：`research/career-wiki/` 待補 AIBOM/K8s AI 供應鏈治理頁面，交 Routine F；一併整理今日 RSS digest 中的 etcd v3.7.0、EKS Auto Mode migration、Vault K8s key management beta 三則職業領域訊號（來自 DAILY-TOPICS 知識空缺區段，非獨立選題）。

**P2-8（新增）**：UK NCSC Cyber Shield 與本 workspace `sre` skill 的 red/blue agentic 攻防技術路線落差，觀察是否形成跨週趨勢再決定是否納入 SRE 能力路線圖參考。

---

## GAP 狀態更新

| GAP | 研究前狀態 | 研究後狀態 | 行動 |
|-----|-----------|-----------|------|
| claude-code-session-restoration | gap (0篇) | **partial** — 底層跨平台 shell 基礎設施經官方文件證實 hard，但「session 無損還原」核心宣稱仍僅單一 tweet 轉述，evidence-tier 維持 soft | 下次選題若再出現，優先查官方 release notes |
| spec-driven | gap (0篇) | **filled** — zeroshot.ghost.io + zencoder.ai + augmentcode 三方交叉確認，evidence-tier hard | P1-8（spec-implement skill 套用） |
| rate-limit/週速率限制 | gap (0篇) | **filled** — 官方 X 帳號一手來源 + BleepingComputer 交叉確認，evidence-tier hard | P1-7（model-profiles.md 指標指針） |
| aibom | gap (0篇) | **filled** — GitHub 官方 repo 一手來源，evidence-tier hard | P2-7（交 Routine F） |
| NCSC/cyber-resilience | gap (0篇) | **filled** — NCSC 官方部落格一手來源，evidence-tier hard，確認度中（與 Claude/Anthropic 無直接關聯） | P2-8（觀察） |

---

## 下一次循環優先事項

1. **P1-1（DAILY-TOPICS 技術路徑交叉驗證流程改進）今日達連續第 5 天未落實，已超過昨日 report 自訂的裁決門檻**——本項不再由 Routine C 自主延續，需使用者於下次互動時裁決：(a) 是否調整 Routine A 排程本身以留出實作視窗、(b) 是否改變追蹤方式（例如降級為觀察項而非每日重複回填）、或 (c) 維持現狀由後續 `/autoload-evolution` cycle 自然接手。
2. **P1-7/P1-8 為本日新增**，證據已齊備，下次有對應檔案編輯機會（或 `/autoload-evolution` cycle）時可直接套用。
3. **P2-7（career-wiki AIBOM 頁面 + etcd/EKS/Vault 三則職業訊號）待 Routine F 執行時一併處理**，本 Routine 僅負責交接標記，非自行深化職業領域內容。

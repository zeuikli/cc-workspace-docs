---
date: 2026-07-13
source: DAILY-RESEARCH/2026-07-13.md
topics: [anthropic-orchestrator-fable-sonnet-subagent-cost-pattern, harness-tuning-cost-parity-langchain-nemotron, anthropic-50b-us-infrastructure-terawulf-buildout, anthropic-gram-dual-use-knowledge-off-switch, cncf-ai-agent-network-boundary-nginx-otel, china-frontier-model-export-control-reuters-precedent]
type: session-report
---

# Session Report 2026-07-13 — Daily Research

## 上次 P0 回填

昨日（2026-07-12）report 之「下一次循環優先事項」逐項機械驗證如下：

| 項目 | 驗證命令 | 狀態 |
|------|----------|------|
| P1-1：DAILY-TOPICS 技術路徑交叉驗證流程改進（連續第 2 天出現實證案例，07-12 已上調至首位） | `grep -qE "技術路徑交叉驗證\|technical.*cross.*valid" research/ROUTINE-A*.md` | ⏳ 仍待辦——連續第 3 天未套用（07-11 首次識別、07-12 確認積壓、07-13 本次再確認），尚未達 tool-schema-degradation 案例的 4 天升級措辭門檻，但已逼近，下次仍未落實則於措辭升級為「治理層系統性延遲」 |
| P1-2：security-hygiene.md 補全 China 偵測版本區間 v2.1.91–v2.1.196 | `grep -qE "2\.1\.91.*2\.1\.196\|2\.1\.196" .claude/rules/security-hygiene.md` | ⏳ 仍待辦——第 2 天，證據（工信部官方文件+Anthropic 回應）已齊備，僅待編輯機會套用，非治理延遲 |
| P0-2（延續多日）：explore-subagent-billing-gotcha 提案 | `grep -qE "29768\|closed as not planned\|not planned" research/EVOLUTION-QUEUE.md` | ⏳ 合規性延後——EVOLUTION-QUEUE.md 現況仍為 `status: deferred（2026-07-11 審核）`，受 core.md「auto-load 規則 ≤1 規則/cycle」鐵律保護，非怠惰，不列入積壓 |

**回填說明**：P1-1 為本日唯一需留意的積壓項——今日雖無新增同類選題誤判實證案例（本日六題交叉查證結果皆屬 hard tier 且來源明確，Topic 6 的 Alibaba 呼應推論已於本日 Unknowns 標注為未經來源文本直接證實，但屬「引用謹慎度」問題而非「廠商歸屬誤判」，與 P1-1 情境不同類），但流程改進本身仍未套用至 `research/ROUTINE-A*.md`，維持積壓追蹤。P1-2 證據齊備僅待落地，非延遲訊號。P0-2 持續受合規門檻保護。

---

## 執行概要
- **研究主題**：6 個（DAILY-TOPICS/2026-07-13.md 全覆蓋：深度應用 2、Anthropic 消息 2、職業領域 1、供應鏈地緣 1）
- **搜尋查詢**：6 次並行 WebSearch
- **頁面 Fetch**：8 次深度抓取（anthropic.com×2 官方研究/新聞、langchain.com 官方部落格、cncf.io 官方部落格、datacenterdynamics.com、the-decoder.com、letsdatascience.com；皆一次成功，無 403/付費牆阻擋）
- **arxiv 命中**：0（本日六題來源皆非論文類，Step 2b 略過）

## 本日研究成果摘要

### 最高價值發現（Top 3）

**1. 「調 harness 不調模型」跨供應商同期互證（影響等級：High）**

Anthropic 官方 cookbook（Fable orchestrator + Sonnet worker，BrowseComp 96%/46%）與 LangChain 對開源 Nemotron 3 Ultra 的獨立 harness 調校（0.86 逼近 Opus 4.8 的 0.87、成本 1/10）在同一週內分別發布，結論一致：不動模型權重、純調 orchestration/scaffolding layer 即可取得顯著成本效益。兩者皆明確劃定「模型能力邊界」作為 harness 調校天花板，與本 workspace core.md「行為指導量與能力成反比」公理直接呼應，可作為外部佐證更新 delegation-protocol.md。

**2. Anthropic 基礎設施擴張規模持續加碼（影響等級：Medium）**

$50B 美國本土投資（德州+紐約，Fluidstack 合作）疊加 TeraWulf $19B/20年/401MW 肯塔基租約，顯示 Anthropic 產能布局進入實體基礎設施階段（非僅雲端容量合約）。時程分階段至 2028 年初全容量，屬長期資訊性追蹤項目。

**3. 中美模型主權化雙向收斂（影響等級：High）**

Reuters 報導中國商務部醞釀對前沿模型（含開源）出口管制討論，與 6 月美方限制 Anthropic Fable/Mythos 海外存取形成雙向呼應——兩大國同時將前沿模型視為戰略資產而非商用軟體出口。延續 P2-2 觀察項，本題為地緣風險系列的新資料點（不同於先前企業內部禁用系列）。

---

## 可實作 / 可測試內容

### P0 — 立即可執行（今日或明日，< 2 小時）

本日六題皆屬 hard tier 資訊性研究發現（無 soft tier，故無鐵律排除項），亦無 workspace 缺陷修復類需求，**無新增 P0**。

延續昨日 P0-2（合規性延後，不視為積壓，見上方回填表）。

### P1 — 本月優先（需輕量設計，2-8 小時）

**P1-1（延續，連續第 3 天未落實）**：DAILY-TOPICS 選題流程補「技術路徑/廠商交叉驗證」檢查點——尚未達 4 天升級門檻，下次仍未套用則措辭升級。
- 驗證：`grep -qE "技術路徑交叉驗證|technical.*cross.*valid" research/ROUTINE-A*.md && echo OK`

**P1-2（延續，第 2 天）**：`.claude/rules/security-hygiene.md` 補全 China v2.1.91–v2.1.196 版本區間。
- 驗證：`grep -qE "2\.1\.91.*2\.1\.196|2\.1\.196" .claude/rules/security-hygiene.md && echo OK`

**P1-3（延續，來自 07-10/07-11/07-12）**：the-loop-best-solution.md 補「confidently garbage」失敗案例與 Self-Harness 論文引用，本日無新進展，維持延續狀態。
- 驗證：`grep -qE "confidently.*garbage|弱驗證器" .claude/refs/the-loop-best-solution.md && echo OK`

**P1-4（新增）**：`.claude/refs/delegation-protocol.md` 套用本日 Topic 1（BrowseComp 96%/46%）+ Topic 2（Nemotron 10x 成本差距）雙重佐證，強化 DAILY-TOPICS 已提案的 evolution_candidates（delegation-protocol-orchestrator-subagent-cookbook-citation），待 `/autoload-evolution` 或人工審核套用。
- 驗證：`grep -qE 'BrowseComp|plan-big-execute-small|Nemotron.*10x|10x.*Nemotron' .claude/refs/delegation-protocol.md && echo OK`

### P2 — 觀察中（需更多信號再決定）

**P2-1（延續，來自 07-12）**：Anthropic Stripe 計費系統可靠性，無新信號。

**P2-2（延續，來自 07-09～07-12，本日新資料點）**：中國供應鏈地緣風險——本日新增「中國自身醞釀前沿模型出口管制」資料點（Topic 6），與先前企業禁用系列並行觀察，交使用者或 finops/sre skill 視實際業務曝險評估。

**P2-3（延續，來自 07-09/07-10）**：Constitutional Classifiers++ 級聯架構參考，無新信號。

**P2-4（延續，來自 07-10）**：Gemini 3.1 Flash-Lite Harvey LAB-AA 數字仍待更多獨立信號源交叉驗證。

**P2-5（新增）**：Anthropic GRAM off-switch 研究（Topic 4）——前瞻性安全研究，尚未套用生產模型，暫不需 workspace 層級行動，留供未來模型層級存取控制設計參考。

**P2-6（新增）**：TeraWulf $19B/401MW 具體數字來自第三方媒體交叉引用，未經官方投資人關係頁面一手驗證（見本日 Unknowns），若未來需用於高風險決策應補驗證。

---

## GAP 狀態更新

| GAP | 研究前狀態 | 研究後狀態 | 行動 |
|-----|-----------|-----------|------|
| anthropic-orchestrator-fable-sonnet-subagent-cost-pattern | gap (0篇) | **filled** — 官方 cookbook + 多家媒體交叉確認，evidence-tier hard | P1-4（delegation-protocol.md 套用） |
| harness-tuning-cost-parity-langchain-nemotron | gap (0篇) | **filled** — LangChain 官方部落格 + NVIDIA 官方部落格雙重確認，evidence-tier hard | P1-4（delegation-protocol.md 套用） |
| anthropic-50b-us-infrastructure-terawulf-buildout | gap (0篇) | **filled** — Anthropic 官方新聞稿 + 多家財經媒體交叉確認 TeraWulf 細節，evidence-tier hard | P2-6（觀察，官方一手驗證待補） |
| anthropic-gram-dual-use-knowledge-off-switch | gap (0篇) | **filled** — Anthropic 官方研究頁完整技術細節齊備 | P2-5（觀察） |
| cncf-ai-agent-network-boundary-nginx-otel | gap (0篇，→ Routine F) | **filled** — CNCF 官方部落格完整架構細節齊備 | 交 Routine F 深化（依原分工） |
| china-frontier-model-export-control-reuters-precedent | gap (0篇) | **filled** — 多家媒體交叉確認 Reuters 獨家內容 | P2-2（觀察項延續） |

---

## 下一次循環優先事項

1. **P1-1（DAILY-TOPICS 技術路徑交叉驗證流程改進）連續第 3 天未落實**——逼近 4 天升級門檻，下次若仍未套用需將措辭正式升級為「治理層系統性延遲」。
2. **P1-4（delegation-protocol.md 套用 BrowseComp + Nemotron 雙重佐證）為本日新增**，證據已齊備，下次有 `.claude/refs/` 編輯機會（或 `/autoload-evolution` cycle）時可直接套用。
3. **P1-2（security-hygiene.md 補全 China 版本區間）延續第 2 天**，證據齊備僅待編輯機會，優先度次於 P1-1。

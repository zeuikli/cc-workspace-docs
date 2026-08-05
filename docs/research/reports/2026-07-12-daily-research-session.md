---
date: 2026-07-12
source: DAILY-RESEARCH/2026-07-12.md
topics: [claude-code-desktop-builtin-browser, claude-plugin-marketplace-github-manifest, anthropic-interactions-api-ga, anthropic-stripe-billing-bug-16m-usd-korea, etcd-3.7-rangestream-k8s-release, china-miit-claude-code-self-check-ban]
type: session-report
---

# Session Report 2026-07-12 — Daily Research

## 上次 P0 回填

昨日（2026-07-11）report 之「下一次循環優先事項」逐項機械驗證如下：

| 項目 | 驗證命令 | 狀態 |
|------|----------|------|
| P0-1（延續第 2 天，若第 3 天仍未套用需升級措辭）：legal-task-type-cost-exception 套用至 model-profiles.md | `grep -qE 'Harvey\|legal.*task.*exception\|14\.2%' .claude/refs/model-profiles.md` | ✅ **已落實**——grep 通過，第 2 天內完成套用，未觸發「治理層系統性延遲」升級措辭門檻 |
| P0-2：explore-subagent-billing-gotcha 提案措辭修正（補充官方 issue #29768 佐證）| `grep -qE "29768\|closed as not planned\|not planned" research/EVOLUTION-QUEUE.md` | ⏳ 仍待辦——查 EVOLUTION-QUEUE.md 現況為 `status: deferred（2026-07-11 審核：目標為 auto-load 規則，同 gpt56 案 byte/cycle 雙限制；留待下一 /autoload-evolution cycle）`，屬**合規性延後**（受 core.md「auto-load 規則 ≤1 規則/cycle」鐵律保護，非治理層怠惰），不升級措辭 |
| P1-1：DAILY-TOPICS 技術路徑交叉驗證流程改進 | `grep -qE "技術路徑交叉驗證\|technical.*cross.*valid" research/ROUTINE-A*.md` | ⏳ 仍待辦——本日 Topic 3（anthropic-interactions-api-ga）為第二起同類誤判實證案例（見下），優先度應提升 |

**回填說明**：P0-1 在第 2 天內完成套用，屬正常節奏，未觸發歷史先例（tool-schema-degradation 案例）的 4 天升級門檻。P0-2 表面仍為 ⏳，但深入檢查 EVOLUTION-QUEUE.md 條目內容後確認其已進入 `deferred` 狀態並附具體理由（auto-load byte/cycle 雙限制、等待下一 /autoload-evolution cycle）——這是 harness 治理機制正確運作的結果（防止 auto-load 規則被過度頻繁修改），本日**不視為積壓**，但保留追蹤直到下次 /autoload-evolution cycle 執行。P1-1 因今日新增第二起實證案例（Topic 3），優先度上調，列入本日下一循環優先事項首位。

---

## 執行概要
- **研究主題**：6 個（DAILY-TOPICS/2026-07-12.md 全覆蓋：深度應用 2、Anthropic 消息 2、職業領域 1、供應鏈地緣 1）
- **搜尋查詢**：6 次並行 WebSearch
- **頁面 Fetch**：8 次深度抓取（code.claude.com×2 官方文件、blog.google、wccftech.com、kubernetes.io 官方部落格、scmp.com、techstartups.com、thewincentral.com；wccftech.com 初次 403 改用替代來源補齊）
- **arxiv 命中**：0（本日六個主題皆非論文類來源，Step 2b 略過）

## 本日研究成果摘要

### 最高價值發現（Top 3）

**1. 選題誤判：anthropic-interactions-api-ga 實為 Google 產品，非 Anthropic（影響等級：Critical）**

DAILY-TOPICS 選題描述「Anthropic Interactions API 正式 GA」，但交叉驗證官方公告後確認該 API 屬 Google/Gemini 產品（Google DeepMind 開發），與 Anthropic 無關。這是繼 07-11（Fable 5 frontmatter vs Managed Agents API）後**第二起連續選題技術路徑誤判**，兩起皆源自單一 tweet 轉述未充分交叉確認廠商/技術路徑歸屬。這將 P1-1（DAILY-TOPICS 技術路徑交叉驗證流程改進）從「單次觀察」升級為「連續 2 天實證的 pattern」，優先度應提升。

**2. Anthropic Stripe 計費系統爆出 $16.6M 異常發票，非孤立事件（影響等級：High）**

一位韓國免費方案使用者收到金額暴增至 1,662.7 萬美元的異常發票（24 小時內從 166.9 萬暴增 10 倍），雖未實際扣款，但 Anthropic 迄今未公開證實根因。獨立稽核公司 Vaudit 同期報告顯示 60 家企業 $34M 發票中有 $1.7M 計費錯誤，根因含「retry storm」（失敗 agent 背景重試堆高帳單）等系統性問題模式，顯示此非單一使用者的孤立異常。

**3. China MIIT 正式警告 Claude Code「後門」，版本範圍與 Anthropic 回應皆已明確（影響等級：High）**

工信部經國家漏洞資料庫正式警告 Claude Code v2.1.91–v2.1.196 存在監控機制風險，Anthropic 員工已承認曾嵌入追蹤程式碼（用於防蒸餾攻擊）並稱已於 07-02 版本移除。阿里巴巴同步宣布禁止員工工作用途使用 Anthropic 工具。此為 07-09 議題（telemetry/Alibaba/Qoder）的官方文件驅動升級版，非重複。

---

## 可實作 / 可測試內容

### P0 — 立即可執行（今日或明日，< 2 小時）

本日六題中四題（hard tier：Topic 1/2/5/6）屬資訊性研究發現，非缺陷修復類，**無新增 P0**。soft tier 二題（Topic 3/4 於初判 soft，Topic 4 研究後升級 hard、Topic 3 仍維持 soft 因屬選題誤判而非知識空缺）依鐵律不得列 P0。

延續昨日 P0-1 已落實（見上方回填表）。

### P1 — 本月優先（需輕量設計，2-8 小時）

**P1-1（延續，優先度上調）**：DAILY-TOPICS 選題流程補「技術路徑/廠商交叉驗證」檢查點——本日 Topic 3 為第二起連續實證案例（07-11 Fable5、07-12 Interactions API），建議明確要求含「API GA」「正式發布」字樣的選題，交叉確認官方廠商網域（`anthropic.com`/`claude.com`）來源，而非僅單一 tweet 轉述。
- 驗證：`grep -qE "技術路徑交叉驗證|technical.*cross.*valid" research/ROUTINE-A*.md && echo OK`

**P1-2（新增）**：`.claude/rules/security-hygiene.md` 的 China v2.1.91 偵測補丁，補全完整版本區間（v2.1.91–v2.1.196）與工信部官方來源引用（現行 grep 僅確認 "2.1.91" 存在，未驗證完整區間覆蓋）。
- 驗證：`grep -qE "2\.1\.91.*2\.1\.196|2\.1\.196" .claude/rules/security-hygiene.md && echo OK`

**P1-3（延續，來自 07-10/07-11）**：the-loop-best-solution.md 補「confidently garbage」失敗案例與 Self-Harness 論文引用，本日無新進展，維持延續狀態。
- 驗證：`grep -qE "confidently.*garbage|弱驗證器" .claude/refs/the-loop-best-solution.md && echo OK`

### P2 — 觀察中（需更多信號再決定）

**P2-1（新增）**：Anthropic Stripe 計費系統可靠性（$16.6M 異常發票 + Vaudit $1.7M 稽核發現），待更多獨立案例或 Anthropic 官方根因說明累積，暫不需 workspace 層級行動。

**P2-2（延續，來自 07-09/07-10/07-11）**：中國供應鏈地緣風險——工信部正式警告 + 阿里巴巴禁令持續累積，維持觀察，交使用者或 finops/sre skill 視實際業務曝險評估。

**P2-3（延續，來自 07-09/07-10）**：Constitutional Classifiers++ 級聯架構作為 quality-pipeline / gap-vote 成本優化參考，無新信號。

**P2-4（延續，來自 07-10）**：Gemini 3.1 Flash-Lite Harvey LAB-AA 31.1%/$0.02 數字仍待更多獨立信號源交叉驗證。

---

## GAP 狀態更新

| GAP | 研究前狀態 | 研究後狀態 | 行動 |
|-----|-----------|-----------|------|
| claude-code-desktop-builtin-browser | gap (0篇) | **filled** — 官方 whats-new 文件證實 Week 28 (v2.1.202–206) 正式功能，evidence-tier soft→hard | 無新增行動，資訊性歸檔 |
| claude-plugin-marketplace-github-manifest | gap (0篇) | **filled** — 官方文件證實完整 marketplace.json + plugin.json 兩層結構已存在，evidence-tier soft→hard | P1 候選：workspace skill 開源可參考此結構（暫不升 P0/P1，無立即需求） |
| anthropic-interactions-api-ga | gap (0篇) | **選題誤判澄清** — 確認為 Google 產品非 Anthropic，本題實質 GAP 狀態轉為「無 Anthropic 對應消息可填」 | P1-1（流程改進，優先度上調） |
| anthropic-stripe-billing-bug-16m-usd-korea | gap (0篇) | **filled** — 多來源交叉確認 + Vaudit 稽核報告佐證系統性模式，evidence-tier soft→hard | P2-1（觀察項） |
| etcd-3.7-rangestream-k8s-release | gap (0篇，→ Routine F) | **filled** — Kubernetes 官方部落格完整技術細節齊備 | 交 Routine F 深化（依原分工） |
| china-miit-claude-code-self-check-ban | gap (0篇) | **filled** — 工信部官方文件 + Anthropic 官方回應 + 版本範圍齊備 | P1-2（security-hygiene.md 補全版本區間） |

---

## 下一次循環優先事項

1. **P1-1（DAILY-TOPICS 技術路徑交叉驗證流程改進）連續第 2 天出現實證案例**，優先度上調至本清單首位——建議下次有 Routine A 規格編輯機會時優先處理，避免第三起同類誤判。
2. **P1-2（security-hygiene.md 補全 China 偵測版本區間 v2.1.91–v2.1.196）為本日新識別項**，證據（工信部官方文件 + Anthropic 回應）已完整齊備，下次有該檔案編輯機會時可直接套用。
3. **P0-2（explore-subagent-billing-gotcha 提案）現已確認為合規性延後**（受 auto-load ≤1 規則/cycle 鐵律保護），非治理層怠惰——下次 /autoload-evolution cycle 執行時優先納入審核，不再需要每日回填追蹤升級措辭。

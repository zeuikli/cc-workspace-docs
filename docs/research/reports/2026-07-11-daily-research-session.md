---
date: 2026-07-11
source: DAILY-RESEARCH/2026-07-11.md
topics: [fable5-orchestrator-sonnet-worker-cost-pattern, explore-subagent-model-inheritance-billing-gotcha, fable5-subscription-extended-july12-second-time, eks-auto-mode-migration-kiro-cli-mcp, microsoft-mai-anthropic-openai-elimination-bid]
type: session-report
---

# Session Report 2026-07-11 — Daily Research

## 上次 P0 回填

昨日（2026-07-10）report 之「下一次循環優先事項」逐項機械驗證如下：

| 項目 | 驗證命令 | 狀態 |
|------|----------|------|
| P0-1：legal-task-type-cost-exception（Harvey LAB-AA 14.2%）套用至 model-profiles.md | `grep -qE 'Harvey\|legal.*task.*exception\|14\.2%' .claude/refs/model-profiles.md` | ⏳ 仍待辦（第 2 天）——證據已於 07-10 完整交叉驗證，僅缺實際套用動作 |
| P0-2：China 偵測案例（v2.1.91）補充至 security-hygiene.md | `grep -iq "2.1.91" .claude/rules/security-hygiene.md` | ✅ **已落實**——連續 2 天佐證齊備後，本 session 之前已套用完成，grep 通過 |
| 監控 EVOLUTION-QUEUE 待審提案數 | `grep -c '**status**: proposed' research/EVOLUTION-QUEUE.md` | ⏳ 4（較昨日 3 上升 1，未降至觀察門檻以下，需留意是否形成新積壓） |

**回填說明**：P0-2（China 偵測）已在本次 session 觀察窗口內完成套用，驗證了「連續 2-3 天佐證齊備後即落實」的正常節奏，非治理層延遲案例。P0-1（legal-task-type-cost-exception）進入第 2 天仍未套用，證據狀態不變（07-10 已交叉驗證準確），本日不升級措辭（未達前次 4 天閾值），但列為本日 P0 延續項並提醒：若第 3 天仍未套用，應比照歷史先例（tool-schema-degradation 案例）採用「治理層系統性延遲」措辭。EVOLUTION-QUEUE 待審數字上升（3→4）為新增觀察點，非既有項目延遲，暫不視為警訊，僅記錄追蹤。

---

## 執行概要
- **研究主題**：5 個（DAILY-TOPICS/2026-07-11.md 全覆蓋：深度應用 2、Anthropic 消息 1、職業領域 1、供應鏈地緣 1）
- **搜尋查詢**：5 次並行 WebSearch
- **頁面 Fetch**：5 次深度抓取（the-decoder.com×2、GitHub 官方 issue #29768、digitalapplied.com、AWS 官方部落格）
- **arxiv 命中**：0（本日五個主題皆非論文類來源，Step 2b 略過）

## 本日研究成果摘要

### 最高價值發現（Top 3）

**1. Explore subagent 計費繼承問題已由官方確認「不修」（closed as not planned）（影響等級：Critical）**

GitHub issue #29768 顯示這不是等待修復的暫時性 bug，而是 Anthropic 已明確決定維持現狀的既定行為。這徹底改變了 workspace 端因應策略的定性——`.claude/rules/subagent-strategy.md` 演化候選中的「pin 至 cost 檔位」補丁，不應被視為「上游修復前的過渡緩解」，而必須是永久性防禦規則，否則未來稽核可能誤判此規則已過時可移除。

**2. Fable 5 orchestrator 技術路徑修正：Managed Agents API，非 Claude Code frontmatter（影響等級：High）**

DAILY-TOPICS 原選題描述「已可用 Claude Code `model:` frontmatter 落地」與官方實際技術路徑不符——96%/46% 數字的落地方式是 **Claude Managed Agents API**（API 層產品），而非 Claude Code CLI 的 frontmatter 設定。這是本日搜尋過程中發現的選題描述誤差，凸顯「先讀官方文件」不足以確認技術宣稱準確性的問題，需搭配交叉驗證。

**3. Microsoft/Fable 5/vendor lock-in 三則新聞共同指向 2026 下半年 AI 供應鏈成本結構重洗牌（影響等級：Medium）**

Topic 1（Fable 5 對抗中國開源模型定價壓力）、Topic 3（Fable 5 免費期二度延長後仍走向 7/13 metered $10/$50 費率）、Topic 5（Microsoft 主動降低 Anthropic 依賴）三者形成收斂信號：workspace 若有任何 model-profiles.md 成本假設，都應提高重審頻率而非視為穩定基準。

---

## 可實作 / 可測試內容

### P0 — 立即可執行（今日或明日，< 2 小時）

**P0-1（延續，第 2 天）**：legal-task-type-cost-exception（Harvey LAB-AA 14.2%）套用至 model-profiles.md，證據已於 07-10 完整交叉驗證，不宜再延遲。
- 驗證：`grep -qE 'Harvey|legal.*task.*exception|14\.2%' .claude/refs/model-profiles.md && echo OK`

**P0-2（新增，本日提出）**：`.claude/rules/subagent-strategy.md` 的 explore-subagent-billing-gotcha 演化候選提案措辭修正——由「暫時性緩解」改為「官方 issue #29768 closed as not planned 後的永久性規則」，避免未來稽核誤判為可移除的臨時補丁。
- 驗證：`grep -qE "29768|closed as not planned|not planned" research/EVOLUTION-QUEUE.md && echo OK`（提案內容補充佐證）

### P1 — 本月優先（需輕量設計，2-8 小時）

**P1-1（新增）**：DAILY-TOPICS 選題撰寫流程補一道「技術路徑交叉驗證」檢查——涉及「已可用 X 機制落地」的宣稱，應要求至少一個官方來源或 issue tracker 交叉確認技術路徑（本日 Topic 1 的 frontmatter vs Managed Agents API 誤差即為反例）。
- 驗證：`grep -qE "技術路徑交叉驗證|technical.*cross.*valid" research/ROUTINE-A*.md && echo OK`（若 Routine A 規格檔存在對應章節）

**P1-2（延續，來自 07-10）**：the-loop-best-solution.md 補「confidently garbage」失敗案例與 Self-Harness 論文引用，本日無新進展，維持延續狀態。
- 驗證：`grep -qE "confidently.*garbage|弱驗證器" .claude/refs/the-loop-best-solution.md && echo OK`

### P2 — 觀察中（需更多信號再決定）

**P2-1（延續，來自 07-09/07-10）**：Constitutional Classifiers++ 級聯架構作為 quality-pipeline / gap-vote 成本優化參考，無新信號。

**P2-2（延續，來自 07-10）**：Gemini 3.1 Flash-Lite Harvey LAB-AA 31.1%/$0.02 數字仍待更多獨立信號源交叉驗證。

**P2-3（新增）**：EKS Auto Mode 七階段驗證閘門設計（health check → CloudFormation complete → pod ready → ALB 200 → 手動確認除役）可作為 core.md APPLY 分級閘門章節的外部案例參考，若未來需要具體佐證可引用。

**P2-4（新增）**：Microsoft MAI vendor lock-in 風險為觀察類供應鏈信號，暫無直接 workspace 行動項，待 scored 庫累積 ≥3 篇同主題文章後再評估是否需要專門章節。

---

## GAP 狀態更新

| GAP | 研究前狀態 | 研究後狀態 | 行動 |
|-----|-----------|-----------|------|
| explore-subagent-billing-gotcha | gap (0篇) | **filled** — 官方 issue #29768 確認「closed as not planned」，定性由暫時 bug 轉為永久行為 | P0-2（提案措辭修正） |
| eks-auto-mode-career-wiki | gap (0篇) | **filled** — 完整七階段遷移流程 + 前置需求 + 安全/網路模型轉變資料齊備 | 交 Routine F 深化（依原分工） |
| vendor-lock-in-microsoft-mai | gap (0篇) | **filled** — Suleyman 表態 + 受影響產品清單 + 矛盾論點齊備 | P2-4（觀察項，累積信號中） |
| fable5-managed-agents-cost-pattern | partial (2篇) | **partial-filled** — 新增 Orchestrator/Advisor 兩種變體數字，但發現原選題技術路徑描述誤差需修正 | P1-1（流程改進提案） |

---

## 下一次循環優先事項

1. **P0-1（legal-task-type-cost-exception 套用至 model-profiles.md）進入第 2 天未套用**，若第 3 天仍未套用，下次 session 應採用「治理層系統性延遲」升級措辭（比照 07-09→07-10 tool-schema-degradation 案例的處理節奏）。
2. **P0-2（explore-subagent-billing-gotcha 提案措辭修正，補充官方 issue #29768 佐證）為本日新識別項**，建議下次有 EVOLUTION-QUEUE.md 或 subagent-strategy.md 編輯機會時優先處理，避免既有提案因缺乏「官方已確認不修」的關鍵佐證而被誤判優先度。
3. **P1-1（DAILY-TOPICS 技術路徑交叉驗證流程改進）為本日新識別的選題品質缺口**：本日發現至少一項選題描述（Fable 5 frontmatter vs Managed Agents API）與官方實際技術路徑不符，建議列入下次 Routine A 或 autoload-evolution 掃描候選，設計具體檢查點防止選題描述誤導後續研究方向。

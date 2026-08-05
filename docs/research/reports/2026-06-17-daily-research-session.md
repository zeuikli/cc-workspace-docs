---
date: 2026-06-17
source: DAILY-RESEARCH/2026-06-17.md
topics: [claude-code-architecture, anthropic-billing, generative-ui, software-factory, fable5-leak]
type: session-report
---

# Session Report 2026-06-17 — Daily Research Automation

## 執行概要

本 session 完整執行 DAILY-TOPICS → Web Research → DAILY-RESEARCH → 實作計畫 → Session Report 的全流程自動化。

- **研究主題**：5 個（DAILY-TOPICS/2026-06-17.md 全覆蓋）
- **搜尋查詢**：5 次並行 WebSearch
- **頁面 Fetch**：6 次深度抓取
- **輸出**：`research/DAILY-RESEARCH/2026-06-17.md`（含跨主題洞見合成）

---

## 本日研究成果摘要

### 最高價值發現（Top 3）

**#1 Claude Code 98% 非 AI 實證**（架構影響：Critical）
- 46 頁研究確認 Claude Code 核心 agent loop ≈ 50 行，其餘 98.4% 是 permission/compaction/tools 等確定性基礎設施
- 直接驗證 workspace 現有 The Loop「確定性代碼做決定，LLM 做判斷」準則
- Gap 填補：claude-code-internal-architecture（scored 庫原有 0 篇）

**#2 Fable 5 Workload Test**（harness 設計影響：High）
- 揭示「任務包裝比原始能力更重要」：完整 task brief 結構（目標/上下文/驗收條件/驗證步驟/交付物）
- Fable 5 ≥3 特徵才值得用的篩選原則——可直接轉化為 `spec-implement` skill 的任務分類前置檢查

**#3 Factory 2.0 Coordinator-Specialist 模式**（多 agent 設計影響：High）
- Coordinator 分解任務 → 專業化 Droid 執行（Code/Review/Test/Docs/Knowledge）
- 與 workspace fan-out 策略高度對應；提供評估多 agent 分解品質的參考框架

---

## 可實作 / 可測試內容

> 優先序：**P0**（本週）→ **P1**（本月）→ **P2**（觀察中）

### P0 — 立即可執行（低摩擦，無架構變更）

#### P0-A: 更新 TOML 權限規則支援

**背景**：Claude Code 2.1.178 新增 TOML 格式支援 `.claude/settings.toml`，目前 workspace 僅有 `settings.json`。

**實作步驟**：
```bash
# 1. 確認現有 settings.json
cat .claude/settings.json | jq '.permissions // empty'

# 2. 建立 settings.toml 等效版本（TOML 可讀性更高）
# settings.toml 支援陣列語法：
# [permissions]
# allow = ["Bash(git*)", "Read", "Glob"]
# deny = ["Bash(rm -rf*)"]
```

**驗證**：`claude --version` 確認 2.1.178+ 後，用 TOML 格式設定單一測試權限，確認生效。

**工時估算**：< 1 小時  
**風險**：低（不影響現有 JSON 設定，TOML 為補充格式）

---

#### P0-B: Fable 5 Workload Test 整合至 `spec-implement` skill

**背景**：Fable 5 分析揭示的 8 條 Workload Test 特徵是篩選任務是否值得用 Fable 5（或需要深度規格）的前置濾網。

**實作位置**：`.claude/skills/spec-implement/` 的任務分類前置步驟

**建議 Checklist 格式**：
```markdown
## Fable 5 Workload Gate（任務接收前執行）
符合 ≥3 項才進入 spec-implement 流程：
- [ ] 多執行階段（非單步完成）
- [ ] 需檢查多個文件/代碼來源
- [ ] 有可機械驗證的驗收標準
- [ ] 輸出為可重用 artifact（非一次性回應）
- [ ] 需跨多來源長 context 推理
- [ ] 有非同步 checkpoint 需求
- [ ] 錯誤成本高（wrong ≠ good enough）

未達 3 項 → 直接實作，不走 spec-implement。
```

**驗證**：取 3 個歷史任務，用此 checklist 分類，驗證分類結果符合直覺。

**工時估算**：1-2 小時  
**風險**：低

---

### P1 — 本月優先（需輕量設計）

#### P1-A: Permission 子系統設計文件

**背景**：Claude Code 逆向工程顯示 Permission System 是 7 種模式的 ML auto-classifier + 工具請求審批閘門，與 workspace 現有 `settings.json` permissio 系統在概念上對齊但設計深度不同。

**實作目標**：
- 建立 `.claude/refs/permission-subsystem.md` 文件，對照 Claude Code 的 7 種模式與本 workspace 現有 permission 結構
- 識別可從 Claude Code 架構借鑑的設計決策

**驗收條件**：
1. 列出 Claude Code 的 7 種 permission 模式（Plan/Default/AcceptEdits/DontAsk/BypassPermissions + 2 種）
2. 對照 workspace 的 `settings.json` allow/deny 清單
3. 識別 ≥1 個可以補強的設計 gap

**工時估算**：2-4 小時

---

#### P1-B: Coordinator-Specialist 多 agent 評估框架

**背景**：Factory 2.0 的 Droid 架構提供了一個「Coordinator 分解 → Specialist 執行 → 驗證閉環」的清晰模式，可轉化為本 workspace multi-agent 任務評估框架。

**實作目標**：建立任務分解品質的評估 checklist，整合至 `subagent-strategy.md` 的委派決策部分。

**評估維度（草稿）**：
```
Coordinator 品質：
- 任務是否分解為角色明確的子任務？
- 每個 sub-agent 是否有清晰的輸入/輸出規格？
- 是否指定驗證機制（非子任務自評）？

Specialist 品質：
- 子任務是否有獨立可測試的成功條件？
- 角色邊界是否明確（無跨 agent 依賴不清情況）？
```

**驗收條件**：修改 `subagent-strategy.md` 或建立 `refs/multi-agent-coordinator-pattern.md`，加入 ≥5 條評估準則。

**工時估算**：3-5 小時

---

#### P1-C: Claude Code 架構分析文章入庫

**背景**：今日研究填補了 `claude-code-internal-architecture` GAP，需將高分文章正式入庫至 `ai-articles/scored/`。

**候選文章**：
1. `vrungta.substack.com` — Claude Code Architecture (Reverse Engineered) → 建議評分：A
2. `qubytes.substack.com` — Inside Claude Code Architecture → 建議評分：B+
3. VILA-Lab GitHub 論文 → 建議加入 `agent-harness/references/`

**實作步驟**：
```bash
# 依現有格式建立 scored 文章 markdown
# 格式參考：research/ai-articles/scored/2026-02-01-agent-harness-2026-philschmid.md
```

**工時估算**：1-2 小時

---

### P2 — 觀察中（需更多信號）

#### P2-A: Generative UI Proof of Concept

**背景**：Vercel AI SDK 的 `streamUI()` 允許 agent 回傳 React component（即時渲染表單/圖表）。此能力標誌 agent 輸出從文字跨越至 UI 層，但目前 workspace 無 Next.js/React 技術棧。

**觀察條件**：若 Claude Code 官方文件出現 Generative UI 相關說明（≥2 次信號），再評估 PoC。

**技術 spike 構想（若啟動）**：
- 使用 Next.js App Router + Vercel AI SDK `streamUI()`
- 讓 agent 根據 DAILY-RESEARCH 文件動態渲染摘要卡片
- 驗證：執行 `npm run dev`，確認 agent response 包含渲染的 React component

---

#### P2-B: Fable 5 System Prompt 深度分析文章

**背景**：Fable 5 完整 system prompt（120k chars，1585 lines）已公開，但 Anthropic 未確認真實性。分析此 prompt 的深度文章目前 scored 庫有 0 篇。

**觀察條件**：等待 ≥1 篇由可信來源（LessWrong/Anthropic 關聯研究者）發表的驗證分析後，再入庫。

---

## GAP 狀態更新

| GAP | 研究前狀態 | 研究後狀態 | 行動 |
|-----|-----------|-----------|------|
| claude-code-internal-architecture | gap | 填補中（web 文章已獲取） | P1-C 入庫 |
| generative-ui-agents | gap | 初步理解 | P2-A 觀察 |
| software-factory-paradigm | gap | 填補中 | P1-B 框架化 |
| git-worktree-multi-agent | gap | 未觸及 | 下一日研究 |
| fable5-system-prompt-leak | gap | 填補中（web 分析已獲取） | P2-B 等確認 |

---

## 下一次循環優先事項

1. **執行 P0-A**（TOML 權限規則）— 30 分鐘快速完成
2. **執行 P0-B**（Workload Test 整合至 spec-implement）— 今日或明日
3. **DAILY-TOPICS/2026-06-18.md** 更新：補充 git-worktree-multi-agent 為明日研究目標

---

## 本次 Loop 自我評估

| 評估維度 | 評分 | 備注 |
|---------|------|------|
| 主題覆蓋率 | 5/5 | 全部 5 個主題均有 web 資料支撐 |
| 資料深度 | 4/5 | Generative UI 部分較淺（agentwiki 連線失敗） |
| 實作可行性 | 4/5 | P0 均有具體步驟；P1 需輕量設計 |
| 合成品質 | 4/5 | 跨主題洞見合成清晰；Factory→fan-out 對應關係有價值 |
| 回報延遲 | ✅ | 單 session 完成 5 主題研究 + 實作計畫 + 本報告 |

**[Checkpoint]** 完成研究 5 主題 / 建立 DAILY-RESEARCH/2026-06-17.md 含洞見合成 / 建立 Session Report 含 P0-P2 實作計畫 / 待 commit + push

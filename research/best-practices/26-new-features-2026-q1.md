# Claude Code 新功能彙整 2026 Q1 — /simplify · /batch · /insights

> 來源：
> - https://x.com/bcherny/status/2027534984534544489（2026-02-28）
> - https://x.com/trq212/status/2019173731042750509（2026-02-04）
> - https://x.com/trq212/status/1944877527044120655（2025-07-14）
> - https://x.com/trq212/status/2005315275026260309（Spec-based development）
> 收錄日期：2026-05-01
> 涵蓋：2025-07 至 2026-02，功能公告 + 使用模式

---

## 一、/simplify 與 /batch — 官方新 Skills（2026-02-28）

來源：Boris Cherny（Claude Code 創建者）推文

### 背景

> "Combined, these skills automate much of the work it used to take to (1) shepherd a pull request to production and (2) perform straightforward, parallelizable code migrations."
> — Boris Cherny

兩個 Skills 解決 PR 生命週期的兩大痛點，Boris 個人日常使用驗證。

### /simplify

**功能**：PR 完成後對已變更程式碼進行 review for reuse, quality, and efficiency，自動精煉並提交改善。

**適用時機**：
- PR 草稿完成後，發 PR 之前
- Code review 收到「這段能不能簡化」回饋後
- 任何「寫完能用，但可以更好」的情境

**使用方式**：
```
/simplify
```

**注意**：本 workspace 已有 `simplify` skill（`.claude/skills/simplify/`），與此官方 Skill 功能對應。

### /batch

**功能**：對可平行分解的程式碼遷移任務，fan-out 多個 subagent 各自處理一個遷移目標，並行完成。

**適用時機**：
- 把 API A 替換為 API B（跨多個檔案，每個檔案獨立處理）
- 依賴升級（語法變更可逐檔處理）
- 重新命名跨模組的 class/function
- 任何「每個目標可以獨立修改，不互相依賴」的遷移

**使用方式**：
```
/batch migrate all Python 2 modules to Python 3
/batch replace all usages of deprecated API X with Y
```

**限制**：只適合「parallelizable」遷移 — 目標之間有依賴關係時不適用。

**與 /loop 的差異**：
| | /batch | /loop |
|--|--------|-------|
| 執行模式 | 一次性 fan-out | 定時重複執行 |
| 適用任務 | 一次性遷移 | 持續性工作流 |
| 結束條件 | 完成即結束 | 手動停止或時限 |

---

## 二、/insights — 工作流自我診斷（2026-02-04）

來源：Thariq（@trq212，Anthropic Claude Code 核心成員）

### 功能

```bash
/insights
```

讀取過去一個月的 message history，輸出三份分析：

1. **專案摘要**：你這個月在做什麼（專案類型、主要任務）
2. **使用模式分析**：你怎麼用 Claude Code（哪些功能用得多、哪些沒用到）
3. **工作流改進建議**：基於你的使用模式提出具體改進

### 使用時機

- **Session 初期診斷**：剛開始新 session 時，了解上個月工作模式，確認方向
- **定期複查**（每週或每月）：檢視是否有工作流退步或可改進的地方
- **學習新功能前**：先看 /insights 的建議，確認哪些功能對你特別有價值

### 注意事項

- 一個月 message history 的 token 量可能相當大，初次執行前確認 context 用量
- 若常用 `/clear`，history 可能不連貫，建議品質會下降
- 此功能對 cc-workspace 用戶直接適用：可立即執行確認效果

---

## 三、Spec-Based Development — 大功能的最佳起點（2025）

來源：Thariq（@trq212），持續推薦的工作流

### 模式

```
1. 寫一個 minimal spec（一段話或幾個要點）
2. 讓 Claude 用 AskUserQuestionTool 訪問你（詳細澄清）
3. 整理訪問結果成完整 spec
4. 開新 session 執行 spec
```

**Thariq 的說法**：
> "my favorite way to use Claude Code to build large features is spec based — start with a minimal spec or prompt and ask Claude to interview you using the AskUserQuestionTool, then make a new session to execute the spec"

### 為什麼有效

- AskUserQuestionTool 會以結構化的 modal UI 詢問問題，強迫你釐清邊界
- Session 1（規劃）與 Session 2（執行）分開，避免規劃過程污染執行 context
- 對應 Karpathy 的「Think Before Coding」原則：假設顯露比直接衝更有效

### 使用方式

```bash
# Session 1 - 規劃
claude  # 開 session
"我想要建立一個 X 功能，請用 AskUserQuestionTool 詳細訪問我，包含技術實作、UI/UX、潛在問題、trade-offs"

# 整理訪問結果為 spec.md 或 SPEC.md

# Session 2 - 執行
claude  # 新 session
"Read SPEC.md and implement the feature"
```

---

## 四、Claude Code = 通用 Agent（2025-07-14）

來源：Thariq（@trq212），Note Tweet

**核心訊息**（第一手 Anthropic 內部人士確認）：

> "When I first joined Anthropic I was surprised to learn that lots of the team used Claude Code as a general agent, not just for code."

### 非程式碼的 Claude Code 使用案例（Anthropic 內部）

- 研究彙整（代替手動搜尋 + 整理）
- 寫作輔助（長文草稿 + 迭代修改）
- 數據分析（讀 CSV + 分析 + 可視化）
- 會議準備（讀相關文件 + 整理要點）
- 系統設計文件（訪問 → spec → 文件草稿）

### 啟示

在 CLAUDE.md 中不限制「只能用於程式碼任務」，讓 Claude 能處理任何需要 context + 工具的工作。

---

## 五、功能速查表

| 功能 | 類型 | 發布時間 | 主要用途 |
|------|------|---------|---------|
| `/simplify` | 官方 Skill | 2026-02-28 | PR 完成後程式碼精煉 |
| `/batch` | 官方 Skill | 2026-02-28 | 平行可分解的程式碼遷移 |
| `/insights` | Slash Command | 2026-02-04 | 工作流自我診斷 + 改進建議 |
| Spec-based | 工作模式 | 2025（持續推薦）| 大功能的訪問式規劃 |
| General Agent | 使用哲學 | 2025-07-14 | CC 不限於程式碼任務 |

---

## Known Gotchas

- `/batch` 要求目標之間無依賴關係；遷移前先確認是否真的 parallelizable
- `/insights` 依賴訊息歷史完整度，`/clear` 頻繁的用戶效果較差
- Note Tweet 的全文透過 API 無法完整取得（Thariq 的 "All You Need" 推文），完整內容需手動閱讀
- `/simplify` 與 `/batch` 是官方 Skills，本 workspace 的 `simplify` skill 已對應；`batch` 可從官方 repo 取得或評估自建

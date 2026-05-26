---
title: How Claude Code Works — Agentic Loop、Tools、Context 管理
source: "https://code.claude.com/docs/en/how-claude-code-works"
type: best-practices
---

# How Claude Code Works — Agentic Loop、Tools、Context 管理

> 來源：https://code.claude.com/docs/en/how-claude-code-works
> 收錄日期：2026-05-01
> 涵蓋：Agentic Loop 三階段、五類 Built-in Tools、Session 管理、Checkpoint、Permission Modes

---

## Agentic Loop

Claude Code 透過三個階段解決問題，且各階段會彼此交織：

| 階段 | 說明 |
|------|------|
| **Gather context** | 搜尋檔案、讀取程式碼、理解環境 |
| **Take action** | 編輯檔案、執行指令、查詢 web |
| **Verify results** | 跑測試、對比截圖、確認輸出 |

Loop 依任務自動調整：一個問題可能只需要 context gathering；一個 bug fix 則反覆循環三個階段數十次。你可以隨時中斷 Claude 重新引導。

**核心架構**：Claude Code 是 Claude 的 **agentic harness**，提供 tools、context 管理、執行環境，讓語言模型成為能力完整的 coding agent。

---

## Models

| 模型 | 適用 |
|------|------|
| Sonnet | 多數 coding 任務 |
| Opus | 複雜架構決策，需要更強推理 |

Session 內切換：`/model`；啟動時指定：`claude --model <name>`

---

## Built-in Tools（五類）

| 類別 | Claude 能做什麼 |
|------|---------------|
| **File operations** | 讀取、編輯、建立、重新命名與重組 |
| **Search** | 按 pattern 找檔案、regex 搜尋內容、探索 codebase |
| **Execution** | 執行 shell 指令、啟動 server、跑測試、使用 git |
| **Web** | 搜尋 web、抓取文件、查詢錯誤訊息 |
| **Code intelligence** | 看編輯後的 type errors 和 warnings、跳定義、找 references（需安裝 code intelligence plugins） |

Claude 還有 spawn subagents、向你提問等 orchestration 工具。完整清單：`/en/tools-reference`

**擴展基礎能力**：Skills 擴展知識、MCP 連接外部服務、Hooks 自動化工作流、Subagents 卸載任務。

---

## Claude Code 存取範圍

在目錄中執行 `claude` 後，Claude Code 可存取：

- **你的專案** — 目錄內及子目錄的檔案（其他路徑需授權）
- **你的 terminal** — 任何你能執行的指令（build tools、git、package managers、scripts）
- **你的 git state** — 當前 branch、未 commit 的變更、近期 commit history
- **CLAUDE.md** — 每次 session 都讀入的專案指令
- **Auto memory** — Claude 自動累積的學習（MEMORY.md 前 200 行或 25KB）
- **已設定的 extensions** — MCP servers、Skills、Subagents、Claude in Chrome

因為 Claude 看到整個專案，它能跨檔案工作：搜尋相關檔案、讀取多個檔案理解 context、協調修改多個檔案、跑測試驗證修正、依需求 commit。

---

## 執行環境

| 環境 | 程式碼在哪執行 | 用途 |
|------|-------------|------|
| **Local** | 你的機器 | 預設；完整存取檔案、工具、環境 |
| **Cloud** | Anthropic 管理的 VM | 卸載任務、操作你沒有 locally 的 repo |
| **Remote Control** | 你的機器，由瀏覽器控制 | 使用 web UI 同時保持一切在 local |

**Interface 選項**：terminal、desktop app、IDE extensions（VS Code、JetBrains）、claude.ai/code、Remote Control、Slack、CI/CD pipelines。

---

## Session 管理

對話 session 儲存在 `~/.claude/projects/` 的 JSONL 檔案中，支援 rewind、resume、fork。

**Sessions 是獨立的**：每個新 session 從乾淨的 context window 開始，不帶前次對話歷史。跨 session 的知識持久化靠 auto memory 和 CLAUDE.md。

### 跨 Branch 工作

Session 綁定到當前目錄。切換 branch 後 Claude 看到新 branch 的檔案，但對話歷史保持不變（Claude 還記得你說了什麼）。

平行 session：用 git worktrees 建立獨立目錄，各跑一個 Claude session。

### Resume 或 Fork Sessions

```bash
claude --continue   # 繼續最近的 session（同一 session ID）
claude --resume     # 選擇最近的 sessions
```

Fork（不影響原 session）：
```bash
claude --continue --fork-session
```

**同一 session 在多個 terminal**：訊息會交錯（像兩人寫同一本筆記本）。平行工作請用 `--fork-session`。

---

## Context Window 管理

Context 包含：對話歷史、檔案內容、指令輸出、CLAUDE.md、auto memory、loaded skills、system instructions。

**Context 填滿時**：Claude Code 先清除較舊的工具輸出，若有需要再摘要整個對話。重要的 code snippets 會保留；早期詳細指令可能遺失 → **把持久規則放進 CLAUDE.md**。

MCP tool definitions 預設延遲載入，透過 tool search 按需取得 schema，只有 tool 名稱佔用 context。

**管理 context 的工具**：
- Skills 按需載入（只有描述在 session 開始時載入）
- Subagents 有自己獨立的 context，不污染主對話

---

## 安全機制

### Checkpoints（Undo 檔案變更）

Claude 編輯任何檔案前先建立快照。出問題時：按 `Esc` 兩次 rewind 到前一狀態，或請 Claude undo。

Checkpoints 是 session local，獨立於 git。**只覆蓋檔案變更；影響遠端系統（資料庫、API、部署）的操作無法 checkpoint。**

### Permission Modes（`Shift+Tab` 循環切換）

| 模式 | 說明 |
|------|------|
| **Default** | 所有檔案編輯和 shell 指令都需確認 |
| **Auto-accept edits** | 自動接受檔案編輯和常見 filesystem 指令（`mkdir`、`mv`），其他指令仍詢問 |
| **Plan mode** | 只用 read-only 工具，建立計畫讓你審核後再執行 |
| **Auto mode** | 後台安全檢查評估所有操作（research preview） |

`.claude/settings.json` 可允許特定指令（如 `npm test`、`git status`）讓 Claude 不必每次詢問。

---

## 有效使用技巧

### 像對話一樣操作

不需要完美的 prompt。先說需要什麼，然後精煉：

```text
Fix the login bug
```
[Claude 調查、嘗試]
```text
That's not quite right. The issue is in the session handling.
```
[Claude 調整方法]

可以隨時中斷（不需等 Claude 完成）。

### 讓 Claude 從特定位置找答案

直接說：`Use 'foo-cli-tool --help' to learn about foo tool, then use it to solve A, B, C.`

### 先探索再實作

複雜問題用 Plan Mode（`Shift+Tab` 兩次）先分析 codebase：

```text
Read src/auth/ and understand how we handle sessions.
Then create a plan for adding OAuth support.
```

### 委派而非指揮

給 context 和方向，讓 Claude 決定細節：

```text
The checkout flow is broken for users with expired cards.
The relevant code is in src/payments/. Can you investigate and fix it?
```

---

## Related Resources

- [Common workflows](/en/common-workflows) — 逐步指南（debug、測試、PR 等）
- [Extend Claude Code](/en/features-overview) — Skills、MCP、自訂指令

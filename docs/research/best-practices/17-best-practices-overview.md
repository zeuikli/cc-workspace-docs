---
title: "Claude Code 最佳實踐官方總綱"
source: "https://code.claude.com/docs/en/best-practices"
type: best-practices
---

# Claude Code 最佳實踐官方總綱

> 來源：https://code.claude.com/docs/en/best-practices
> 收錄日期：2026-05-01
> 涵蓋：驗證工作流、探索→規劃→實作四階段、Context 管理、平行化與自動化、常見失敗模式

---

## 核心約束：Context Window 是最重要的資源

Claude 的 context window 包含整個對話、每次讀取的檔案、每次指令的輸出。**Context 愈滿，效能愈差。** 當 context 接近上限，Claude 可能開始「忘記」早期指令或犯更多錯誤。

**延伸閱讀**：
- 互動式 context window 視覺化：`/en/context-window`
- 自訂 status line 持續追蹤用量：`/en/statusline`
- 降低 token 用量策略：`/en/costs#reduce-token-usage`

---

## 1. 給 Claude 驗證機制（最高槓桿單一動作）

包含測試、截圖、預期輸出，讓 Claude 能自我驗證。

| 策略 | Before | After |
|------|--------|-------|
| **提供驗證標準** | "implement a function that validates email addresses" | "write a validateEmail function. example test cases: user@example.com is true, invalid is false, user@.com is false. run the tests after implementing" |
| **視覺驗證 UI 變更** | "make the dashboard look better" | "[paste screenshot] implement this design. take a screenshot of the result and compare it to the original. list differences and fix them" |
| **解決根因而非症狀** | "the build is failing" | "the build fails with this error: [paste error]. fix it and verify the build succeeds. address the root cause, don't suppress the error" |

UI 變更可用 **Claude in Chrome extension** 驗證（自動開新 tab、測試 UI、迭代到正確）。

驗證工具可以是測試套件、linter、或任何輸出可被驗證的 bash 指令。

---

## 2. 探索→規劃→實作→Commit 四階段工作流

用 Plan Mode 分離探索與執行，避免解決錯誤問題。

| 階段 | 說明 | 工具 |
|------|------|------|
| **探索（Explore）** | 進入 Plan Mode，Claude 僅讀取不修改 | `Shift+Tab` 進入 Plan Mode |
| **規劃（Plan）** | 請 Claude 建立詳細實作計畫 | 可按 `Ctrl+G` 在文字編輯器中直接編輯計畫 |
| **實作（Implement）** | 切回 Normal Mode，讓 Claude 依計畫寫程式 | 同時讓 Claude 跑測試驗證 |
| **Commit** | 讓 Claude 撰寫 commit message 並開 PR | "commit with a descriptive message and open a PR" |

**何時跳過 Plan Mode**：任務範圍清楚且改動小（改 typo、加 log、改名稱）時直接執行。規劃最有價值的場景：方法不確定、改動影響多個檔案、不熟悉被修改的程式碼。

---

## 3. 在 Prompt 中提供具體 Context

| 策略 | Before | After |
|------|--------|-------|
| **縮小範圍** | "add tests for foo.py" | "write a test for foo.py covering the edge case where the user is logged out. avoid mocks." |
| **指向來源** | "why does ExecutionFactory have such a weird api?" | "look through ExecutionFactory's git history and summarize how its api came to be" |
| **參照現有 pattern** | "add a calendar widget" | "look at how existing widgets are implemented on the home page to understand the patterns. HotDogWidget.php is a good example. follow the pattern to implement a new calendar widget…" |
| **描述症狀** | "fix the login bug" | "users report that login fails after session timeout. check the auth flow in src/auth/, especially token refresh. write a failing test that reproduces the issue, then fix it" |

### 提供豐富內容的方式

- 用 `@` 引用檔案（Claude 在回應前先讀）
- 直接貼上圖片（copy/paste 或拖放）
- 貼 URL（文件、API reference）；用 `/permissions` 加入常用 domain 白名單
- Pipe data：`cat error.log | claude`
- 讓 Claude 自行抓取：透過 bash 指令、MCP 工具或讀取檔案

---

## 4. 設定環境

### CLAUDE.md

```markdown
# Code style
- Use ES modules (import/export) syntax, not CommonJS (require)
- Destructure imports when possible (eg. import { foo } from 'bar')

# Workflow
- Be sure to typecheck when you're done making a series of code changes
- Prefer running single tests, and not the whole test suite, for performance
```

| ✅ 該放 | ❌ 不該放 |
|---------|---------|
| Claude 猜不到的 bash 指令 | Claude 讀程式碼就能知道的事 |
| 與預設不同的 code style 規則 | 標準語言慣例 |
| 測試指令與偏好的 test runner | 詳細 API 文件（改放連結） |
| Branch 命名、PR 慣例 | 頻繁變更的資訊 |
| 專案特定的架構決策 | 詳細教學 |
| 開發環境特殊性（必要的 env var） | 逐檔描述 codebase |
| 常見陷阱與非直覺行為 | 「寫乾淨程式碼」等不言而喻的事 |

**關鍵原則**：每行問自己「移除這行 Claude 會犯錯嗎？」不會就刪。CLAUDE.md 過長 = Claude 忽略你的實際指令。

CLAUDE.md 可放多個位置：`~/.claude/CLAUDE.md`（全局）、`./CLAUDE.md`（專案）、`./CLAUDE.local.md`（個人、加入 .gitignore）、子目錄（按需載入）。

可用 `@path/to/import` 語法引入其他檔案：
```markdown
See @README.md for project overview and @package.json for available npm commands.

# Additional Instructions
- Git workflow: @docs/git-instructions.md
```

### Permission 設定（三種降低中斷的方式）

| 方式 | 說明 |
|------|------|
| **Auto mode** | 獨立 classifier 模型審查指令，只 block 有風險的操作 |
| **Permission allowlists** | 允許特定已知安全的工具（如 `npm run lint`、`git commit`） |
| **Sandboxing** | OS 層隔離，限制 filesystem 和 network 存取範圍 |

詳細：`/en/permission-modes`、`/en/permissions`、`/en/sandboxing`

### CLI Tools

安裝 `gh`、`aws`、`gcloud`、`sentry-cli` 等 CLI 工具，讓 Claude 用最節省 context 的方式與外部服務互動。

Claude 也善於學習不熟悉的 CLI 工具：`Use 'foo-cli-tool --help' to learn about foo tool, then use it to solve A, B, C.`

### MCP Servers

`claude mcp add` 連接 Notion、Figma、資料庫等外部工具。

### Hooks

**Hooks 是確定性的**（不同於 CLAUDE.md 的建議性）。讓 Claude 撰寫 hook：

- "Write a hook that runs eslint after every file edit"
- "Write a hook that blocks writes to the migrations folder."

直接編輯 `.claude/settings.json`；用 `/hooks` 瀏覽已設定的 hooks。

### Skills

在 `.claude/skills/` 建立含 `SKILL.md` 的目錄：

```markdown
---
name: fix-issue
description: Fix a GitHub issue
disable-model-invocation: true
---
Analyze and fix the GitHub issue: $ARGUMENTS.

1. Use `gh issue view` to get the issue details
2. Understand the problem described in the issue
3. Search the codebase for relevant files
4. Implement the necessary changes to fix the issue
5. Write and run tests to verify the fix
6. Create a descriptive commit message
7. Push and create a PR
```

用 `/fix-issue 1234` 呼叫。`disable-model-invocation: true` 適用於有副作用、只想手動觸發的 workflow。

### 自訂 Subagents

在 `.claude/agents/` 建立 markdown 定義：

```markdown
---
name: security-reviewer
description: Reviews code for security vulnerabilities
tools: Read, Grep, Glob, Bash
model: opus
---
You are a senior security engineer. Review code for:
- Injection vulnerabilities (SQL, XSS, command injection)
- Authentication and authorization flaws
- Secrets or credentials in code
- Insecure data handling
```

明確告知 Claude 使用：`"Use a subagent to review this code for security issues."`

### Plugins

`/plugin` 瀏覽市場，免設定安裝 skills、tools、integrations。

---

## 5. 有效溝通

### 詢問 Codebase 問題

像問資深工程師一樣問 Claude：
- How does logging work?
- How do I make a new API endpoint?
- What edge cases does `CustomerOnboardingFlowImpl` handle?
- Why does this code call `foo()` instead of `bar()` on line 333?

### 讓 Claude 來問你（Interview 模式）

```text
I want to build [brief description]. Interview me in detail using the AskUserQuestion tool.

Ask about technical implementation, UI/UX, edge cases, concerns, and tradeoffs. Don't ask obvious questions, dig into the hard parts I might not have considered.

Keep interviewing until we've covered everything, then write a complete spec to SPEC.md.
```

完成 spec 後，開新 session 執行（乾淨 context 專注實作）。

---

## 6. 管理 Session

### 及早且持續地修正方向

| 操作 | 效果 |
|------|------|
| `Esc` | 停止 Claude，保留 context，可重新引導 |
| `Esc + Esc` 或 `/rewind` | 開啟 rewind 選單，恢復對話和程式碼狀態 |
| `"Undo that"` | 讓 Claude revert 其變更 |
| `/clear` | 重置 context（任務之間） |

**重要規則**：若對同一問題修正超過兩次 → 執行 `/clear`，用更具體的 prompt 重新開始。

### 積極管理 Context

- 不相關任務之間用 `/clear` 重置 context window
- auto compaction 觸發時 Claude 自動摘要（保留 code patterns、檔案狀態、關鍵決策）
- 更多控制：`/compact <instructions>`（例：`/compact Focus on the API changes`）
- 局部摘要：`Esc + Esc` → 選訊息 checkpoint → **Summarize from here**
- 在 CLAUDE.md 中自訂 compaction 行為：`"When compacting, always preserve the full list of modified files and any test commands"`
- 快速問題不需要留在 context：用 `/btw`（答案顯示在可關閉的 overlay，不進入對話歷史）

### 用 Subagents 調查

```text
Use subagents to investigate how our authentication system handles token
refresh, and whether we have any existing OAuth utilities I should reuse.
```

Subagent 在獨立的 context window 執行，回傳摘要，不污染主對話。也可用於驗證：`use a subagent to review this code for edge cases`

### Rewind Checkpoints

Claude 在每次改動前自動建立 checkpoint。按 `Esc Esc` 或 `/rewind` 開啟 rewind 選單，可：
- 只恢復對話
- 只恢復程式碼
- 兩者都恢復
- 從選定訊息開始摘要

Checkpoints 跨 session 持久，可隨時 rewind。**注意：Checkpoints 只追蹤 Claude 的改動，不追蹤外部程序，不能替代 git。**

### Resume Conversations

```bash
claude --continue    # 繼續最近的對話
claude --resume      # 從最近的 sessions 中選擇
```

用 `/rename` 給 session 取描述性名稱（如 `"oauth-migration"`）。把 session 當成 branch：不同工作流可以有各自持久的 context。

---

## 7. 自動化與擴展

### 非互動模式（CI / 腳本）

```bash
# 一次性查詢
claude -p "Explain what this project does"

# 結構化輸出（給腳本用）
claude -p "List all API endpoints" --output-format json

# 即時串流處理
claude -p "Analyze this log file" --output-format stream-json
```

### 平行 Claude Sessions（三種方式）

| 方式 | 說明 | 適用場景 |
|------|------|---------|
| **Claude Code desktop app** | 多個本地 session，各有獨立 worktree | 視覺化管理 |
| **Claude Code on the web** | Anthropic 安全雲端基礎設施，獨立 VM | 無本地環境 |
| **Agent teams** | 多 session 自動協調，共享 tasks | 複雜平行工作 |

**Writer/Reviewer pattern**：Session A 實作 → Session B 獨立 review（新 context 不受實作偏見影響）

### Fan-out 大規模作業

```bash
# 範例：大規模遷移
for file in $(cat files.txt); do
  claude -p "Migrate $file from React to Vue. Return OK or FAIL." \
    --allowedTools "Edit,Bash(git commit *)"
done
```

步驟：
1. 讓 Claude 列出所有需要遷移的檔案
2. 寫腳本 loop 處理
3. 先在 2-3 個檔案測試，再全面執行
4. `--allowedTools` 限制無人值守時 Claude 的操作範圍

也可整合到現有 pipeline：
```bash
claude -p "<prompt>" --output-format json | your_command
```

### Auto Mode

```bash
claude --permission-mode auto -p "fix all lint errors"
```

非互動模式下使用 `-p` 時，若 classifier 反覆 block 操作，auto mode 會 abort（沒有使用者可以 fallback）。

---

## 8. 常見失敗模式

| 模式 | 問題 | 修正 |
|------|------|------|
| **廚房水槽 session** | 混雜多個不相關任務，context 充斥不相關資訊 | 不相關任務之間執行 `/clear` |
| **不斷修正** | Claude 一再做錯，context 被失敗方法污染 | 兩次修正後 `/clear`，用涵蓋學到教訓的更好 prompt 重啟 |
| **過長的 CLAUDE.md** | 太長導致 Claude 忽略其中一半的規則 | 無情刪減；不需要的指令 → 刪除或轉成 hook |
| **信任但不驗證缺口** | Claude 產出看起來正確但有邊界情況的實作 | 永遠提供驗證（測試、腳本、截圖）；無法驗證就不上線 |
| **無限探索** | 沒有限定範圍的「調查」讓 Claude 讀數百個檔案填滿 context | 縮小調查範圍，或使用 subagents（探索留在 child context） |

---

## 9. 培養直覺

這份指南的 pattern 不是一成不變的，是起點：

- 有時讓 context 累積是對的（深陷複雜問題、歷史很有價值）
- 有時可以跳過規劃（探索性任務）
- 有時模糊的 prompt 剛好合適（想看 Claude 如何詮釋問題）

**注意什麼有用**：Claude 產出好結果時，記住你做了什麼（prompt 結構、提供的 context、當時的模式）。Claude 出問題時，問為什麼（context 太雜亂？prompt 太模糊？任務對一次完成太大？）

---

## Related Resources

- [How Claude Code works](/research/best-practices/18-how-claude-code-works) — agentic loop、tools、context 管理
- [Extend Claude Code](/research/best-practices/19-features-overview) — skills、hooks、MCP、subagents、plugins
- [Common workflows](/research/best-practices/20-common-workflows) — debug、testing、PR、session 管理等逐步指南
- [CLAUDE.md](/research/best-practices/21-memory-claudemd) — 儲存專案慣例與持久 context

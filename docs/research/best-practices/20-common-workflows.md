---
title: "Common Workflows — 逐步實戰指南"
source: "https://code.claude.com/docs/en/common-workflows"
type: best-practices
---

# Common Workflows — 逐步實戰指南

> 來源：https://code.claude.com/docs/en/common-workflows
> 收錄日期：2026-05-01
> 涵蓋：Codebase 探索、Bug Fix、Refactoring、Tests、PR、Plan Mode、Session 管理、Git Worktrees、平行化

---

## 理解新 Codebase

### 快速取得 Codebase 概觀

```text
give me an overview of this codebase
explain the main architecture patterns used here
what are the key data models?
how is authentication handled?
```

**技巧**：先問廣，再縮小；問 coding 慣例和 patterns；要求解釋專案專屬術語表。

### 找到相關程式碼

```text
find the files that handle user authentication
how do these authentication files work together?
trace the login process from front-end to database
```

**技巧**：用專案的領域術語；安裝 code intelligence plugin 取得精確的「跳定義」和「找 references」。

---

## 有效率地 Fix Bug

```text
I'm seeing an error when I run npm test
suggest a few ways to fix the @ts-ignore in user.ts
update user.ts to add the null check you suggested
```

**技巧**：
- 告知如何重現問題（指令 + stack trace）
- 說明錯誤是偶發還是必然
- 讓 Claude 知道任何重現步驟

---

## 重構程式碼

```text
find deprecated API usage in our codebase
suggest how to refactor utils.js to use modern JavaScript features
refactor utils.js to use ES2024 features while maintaining the same behavior
run tests for the refactored code
```

**技巧**：請 Claude 解釋新方法的優點；需要時要求維持向後相容；小批次、可測試地重構。

---

## 使用專業 Subagents

```bash
/agents    # 查看所有可用 subagents，並可建立新的
```

**自動委派**：Claude Code 會自動把適當的任務委派給專業 subagents：
```text
review my recent code changes for security issues
run all tests and fix any failures
```

**明確指定**：
```text
use the code-reviewer subagent to check the auth module
have the debugger subagent investigate why users can't log in
```

**建立自訂 subagent**：用 `/agents` → "Create New subagent"，定義：識別符、使用時機、可存取工具、system prompt。在 `.claude/agents/` 建立供團隊共用。

---

## Plan Mode — 安全的 Code 分析

**Shift+Tab 循環切換**：Normal → Auto-Accept（`⏵⏵ accept edits on`）→ Plan Mode（`⏸ plan mode on`）

```bash
# 以 Plan Mode 啟動新 session
claude --permission-mode plan

# 在 Plan Mode 中執行非互動查詢
claude --permission-mode plan -p "Analyze the authentication system and suggest improvements"
```

### 何時用 Plan Mode

- 多步驟實作（需要修改很多檔案）
- Code 探索（先研究 codebase，再做任何變更）
- 互動式開發（想與 Claude 一起迭代方向）

### 範例：規劃複雜重構

```text
I need to refactor our authentication system to use OAuth2. Create a detailed migration plan.
What about backward compatibility?
How should we handle database migration?
```

按 `Ctrl+G` 在預設文字編輯器中開啟計畫直接編輯。

接受計畫時，Claude 自動從計畫內容命名 session（除非你已用 `--name` 或 `/rename` 設名稱）。

### 設定 Plan Mode 為預設

```json
// .claude/settings.json
{
  "permissions": {
    "defaultMode": "plan"
  }
}
```

### Ultraplan（W15，雲端 Plan Mode）

從 terminal 在雲端啟動 plan mode，在瀏覽器中 review 計畫，支援對個別段落留 inline comment / 修改，再選擇遠端執行或送回 CLI：

```text
> /ultraplan <task>
```

v2.1.101 起首次執行自動建立預設雲端環境，不需要先在 Web 設定。

---

## 撰寫測試

```text
find functions in NotificationsService.swift that are not covered by tests
add tests for the notification service
add test cases for edge conditions in the notification service
run the new tests and fix any failures
```

Claude 會仿照現有測試的風格、framework 和 assertion patterns。讓它分析你的程式碼路徑並找出邊界情況。

---

## 建立 Pull Requests

```text
# 直接要求
create a pr for my changes

# 或逐步引導
summarize the changes I've made to the authentication module
create a pr
enhance the PR description with more context about the security improvements
```

用 `gh pr create` 建立 PR 時，session 自動與該 PR 連結。之後用 `claude --from-pr <number>` 或在 `/resume` 選單貼上 PR URL 來返回（支援 GitHub / GitHub Enterprise / GitLab / Bitbucket）。

### /autofix-pr（W15）

不用開瀏覽器，從 terminal 一鍵對當前分支的 PR 啟動 Auto-Fix：

```text
> /autofix-pr
```

---

## 處理文件

```text
find functions without proper JSDoc comments in the auth module
add JSDoc comments to the undocumented functions in auth.js
improve the generated documentation with more context and examples
check if the documentation follows our project standards
```

**技巧**：指定文件風格（JSDoc、docstrings）；要求在文件中加範例；特別要求為 public APIs、interfaces、複雜邏輯寫文件。

---

## 在筆記和非程式碼目錄工作

Claude Code 在任何目錄都能工作。在筆記 vault、文件資料夾、任何 markdown 檔案集合中執行，可以搜尋、編輯和重組內容。

`.claude/` 目錄和 `CLAUDE.md` 與其他工具的 config 目錄並列，不會衝突。Claude 每次 tool call 都重新讀取檔案，所以能看到你在其他應用程式的編輯。

---

## 使用圖片

加入圖片到對話的三種方式：
1. 拖放圖片到 Claude Code 視窗
2. 複製圖片後用 `Ctrl+V` 貼上（不要用 `Cmd+V`）
3. 提供圖片路徑："Analyze this image: /path/to/image.png"

```text
What does this image show?
Describe the UI elements in this screenshot
Here's a screenshot of the error. What's causing it?
Generate CSS to match this design mockup
What HTML structure would recreate this component?
```

Claude 參考圖片時（如 `[Image #1]`），`Cmd+Click`（Mac）或 `Ctrl+Click`（Windows/Linux）可開啟圖片。

---

## 引用檔案和目錄（`@` 語法）

```text
Explain the logic in @src/utils/auth.js       # 包含完整檔案內容
What's the structure of @src/components?      # 提供目錄清單
Show me the data from @github:repos/owner/repo/issues  # MCP 資源
```

**技巧**：
- 路徑可以是相對或絕對路徑
- `@` 檔案引用會同時帶入該目錄及父目錄的 CLAUDE.md
- 目錄引用顯示檔案清單，不是內容
- 可在一個訊息中引用多個檔案（`@file1.js and @file2.js`）

---

## Extended Thinking（思考模式）

Extended thinking 預設啟用，讓 Claude 在回應前逐步推理複雜問題。按 `Ctrl+O` 開啟 verbose mode 查看灰色斜體的內部推理（flicker-free 模式中，`Ctrl+O` 另有 **Focus view** 功能：折疊視圖為最後 prompt + 工具摘要 + 最終回應）。

**特別適合**：複雜架構決策、棘手 bugs、多步驟實作規劃、評估方法間的 tradeoffs。

> **注意**：輸入 "think"、"think hard"、"think more" 被解釋為普通 prompt 指令，不會分配 thinking tokens。

### 設定思考模式

| 範圍 | 設定方式 | 說明 |
|------|---------|------|
| **Effort level** | `/effort`、`/model`、`CLAUDE_CODE_EFFORT_LEVEL` | 控制支援模型的思考深度 |
| **`ultrathink` 關鍵字** | 在 prompt 中包含 "ultrathink" | 在那一輪加入更多推理的指令（不改變 effort level） |
| **切換快捷鍵** | `Option+T`（macOS）/ `Alt+T`（Windows/Linux） | 切換當前 session 的思考（所有模型） |
| **全域預設** | `/config` 切換思考模式 | 存為 `alwaysThinkingEnabled` 在 `~/.claude/settings.json` |
| **限制 token 預算** | `MAX_THINKING_TOKENS` env var | 限制思考預算。Opus 4.7 永遠使用 adaptive reasoning，不支援固定預算 |

**Adaptive reasoning**：Opus 4.7 依任務動態分配思考 tokens（基於 effort level），讓常規 prompt 更快回應，複雜步驟保留深度思考。

---

## Resume 之前的對話

```bash
claude --continue          # 繼續當前目錄最近的對話
claude --resume            # 開啟對話選擇器或依名稱 resume
claude --from-pr 123       # Resume 連結到特定 PR 的 sessions
```

Session 內：`/resume` 切換到其他對話

Session 太大時，`--resume`、`--continue`、`/resume` 會提供「從摘要 resume」的選項。Rewind 選單也新增了「**Summarize up to here**」選項（W20），可壓縮較早的 context 同時保留最近的 turns。

### `claude project purge`（W18，v2.1.126）

清除專案所有本地狀態（transcript / task / file history / config entry）：

```bash
claude project purge --dry-run   # 預覽將被刪除的內容
claude project purge             # 清除當前專案（會確認提示）
claude project purge -y          # 跳過確認
claude project purge --all       # 清除所有專案
```

### 命名 Sessions

```bash
claude -n auth-refactor                  # 啟動時命名

# 或在 session 中
/rename auth-refactor

# 之後 resume
claude --resume auth-refactor
/resume auth-refactor
```

### Session Picker 快捷鍵

| 快捷鍵 | 操作 |
|--------|------|
| `↑` / `↓` | 在 sessions 間導航 |
| `→` / `←` | 展開/收合分組 sessions |
| `Enter` | 選擇並 resume 高亮的 session |
| `Space` | 預覽 session 內容 |
| `Ctrl+R` | 搜尋所有專案歷史（W19，v2.1.129）；在 picker 中為重命名高亮 session |
| `Ctrl+S` | 搜尋中切換縮小到當前專案（W19） |
| `/` 或任意字元 | 進入搜尋模式 |
| `Ctrl+A` | 顯示此機器上所有專案的 sessions |
| `Ctrl+W` | 顯示當前 repo 所有 worktrees 的 sessions |
| `Ctrl+B` | 過濾到當前 git branch 的 sessions |
| `Esc` | 離開 picker 或搜尋模式 |

**貼 PR URL 進搜尋欄**（W18，v2.1.122）可找到建立那個 PR 的 session；支援 GitHub / GitHub Enterprise / GitLab / Bitbucket。Forked sessions 群組在根 session 下方。

---

## 用 Git Worktrees 平行化 Sessions

```bash
# 在 worktree 中啟動 Claude
claude --worktree feature-auth        # 建立 .claude/worktrees/feature-auth/
claude --worktree bugfix-123         # 另一個獨立 worktree

# 自動命名
claude --worktree
```

Worktrees 建立在 `<repo>/.claude/worktrees/<name>`，從預設遠端 branch 分支（`origin/HEAD`）。

**重新同步 origin/HEAD**（若遠端預設 branch 變更）：
```bash
git remote set-head origin -a
```

### Subagent Worktrees

讓 subagents 在各自的 worktree 中平行工作，不互相衝突：
```text
use worktrees for your agents
```
或在自訂 subagent frontmatter 中設定 `isolation: worktree`。

### Worktree 清理規則

| 狀態 | Claude 的行為 |
|------|-------------|
| 無變更 | 自動移除 worktree 和 branch |
| 有變更或 commits | 提示保留或移除 |

**手動管理**：
```bash
git worktree add ../project-feature-a -b feature-a  # 建立
git worktree remove ../project-feature-a             # 清理
```

### 複製 gitignored 檔案到 Worktrees

建立 `.worktreeinclude`（使用 `.gitignore` 語法）：

```text
.env
.env.local
config/secrets.json
```

只有符合 pattern 且已被 gitignored 的檔案才會複製。

> **建議**：把 `.claude/worktrees/` 加入 `.gitignore`，避免出現在主 repo 的 untracked files 中。

### `worktree.baseRef`（W19）

設定新 worktree 分支的基準點：

```json
// .claude/settings.json
{
  "worktree": {
    "baseRef": "fresh"
  }
}
```

| 值 | 行為 |
|----|------|
| `fresh`（預設）| 從遠端預設分支建立，確保新 worktree 不含未推送的 local commit |
| `head` | 從本地 HEAD 建立（含未推送 commit） |

---

## 通知（當 Claude 需要你的注意時）

用 `Notification` Hook event 設定桌面通知（`macOS`：

```json
// ~/.claude/settings.json
{
  "hooks": {
    "Notification": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "osascript -e 'display notification \"Claude Code needs your attention\" with title \"Claude Code\"'"
          }
        ]
      }
    ]
  }
}
```

**Matcher 可縮小觸發條件**：

| Matcher | 觸發時機 |
|---------|---------|
| `permission_prompt` | Claude 需要核准 tool use |
| `idle_prompt` | Claude 完成，等待下一個 prompt |
| `auth_success` | 認證完成 |
| `elicitation_dialog` | MCP server 開啟 elicitation 表單 |

---

## Claude 作為 Unix 工具

### 加入驗證流程

```json
// package.json
{
  "scripts": {
    "lint:claude": "claude -p 'you are a linter. please look at the changes vs. main and report any issues related to typos. report the filename and line number on one line, and a description of the issue on the second line. do not return any other text.'"
  }
}
```

### Pipe in / Pipe out

```bash
cat build-error.txt | claude -p 'concisely explain the root cause of this build error' > output.txt
```

### 控制輸出格式

| 格式 | 指令 | 說明 |
|------|------|------|
| Text（預設） | `--output-format text` | 純文字 Claude 回應 |
| JSON | `--output-format json` | 含 metadata（cost、duration）的 JSON array |
| Streaming JSON | `--output-format stream-json` | 即時輸出每個對話輪次的 JSON objects |

---

## 排程執行 Claude

| 選項 | 在哪執行 | 最適合 |
|------|---------|--------|
| [Routines](/en/routines) | Anthropic 管理的基礎設施 | 電腦關機仍能執行的任務；支援 API 呼叫和 GitHub events |
| [Desktop scheduled tasks](/en/desktop-scheduled-tasks) | 你的機器（desktop app） | 需要存取 local 檔案、工具或未 committed 變更 |
| [GitHub Actions](/en/github-actions) | CI pipeline | 連結到 repo events 或 cron 排程的任務 |
| [`/loop`](/en/scheduled-tasks) | 當前 CLI session | Session 開著時的快速輪詢（不提供 interval 時 Claude 自行決定下次觸發時機）；別名 `/proactive` |

**排程任務 prompt 要明確**：說明成功條件和如何處理結果（任務自動執行，無法問澄清問題）。

### Monitor Tool（W15，v2.1.98）

新 built-in tool：在背景啟動監控進程，每個 stdout 事件**即時**注入 conversation，Claude 立即回應，不需要 Bash sleep loop：

```text
> Tail server.log in the background and tell me the moment a 5xx shows up
```

### /batch（2026-02-28）

對可平行分解的遷移任務 fan-out 多個 subagent，各自獨立處理一個遷移目標：

```text
> /batch migrate all Python 2 modules to Python 3
> /batch replace all usages of deprecated API X with Y
```

**限制**：只適合目標之間無依賴關係的任務。

| | `/batch` | `/loop` |
|--|----------|---------|
| 執行模式 | 一次性 fan-out | 定時重複執行 |
| 適用任務 | 一次性遷移 | 持續性工作流 |
| 結束條件 | 完成即結束 | 手動停止或時限 |

### /goal（v2.1.139，W20）

設定完成條件，Claude 持續執行跨多個 turn 直到條件成立；每個 turn 後由 fast model 檢查條件：

```text
> /goal all tests in test/auth pass and the lint step is clean
```

在 interactive、`-p`、Remote Control 均可用。適合有可驗證結束狀態的大型工作。

---

## Related Resources

- [Best practices](/en/best-practices) — 高層次 patterns 和技巧
- [How Claude Code works](/en/how-claude-code-works) — Agentic loop 和 context 管理
- [Extend Claude Code](/en/features-overview) — 加入 skills、hooks、MCP、subagents、plugins
- [Reference implementation](https://github.com/anthropics/claude-code/tree/main/.devcontainer) — Development container 參考實作

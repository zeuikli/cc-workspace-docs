---
title: "Claude Code What's New — 週版本要點彙整（2026-W13 至 W17）"
source: "https://code.claude.com/docs/en/whats-new/2026-w13 至 w17"
type: best-practices
---

# Claude Code What's New — 週版本要點彙整（2026-W13 至 W17）

> 來源：https://code.claude.com/docs/en/whats-new/2026-w13 至 w17  
> 收錄日期：2026-05-01  
> 涵蓋：2026-03-23 至 2026-04-24，版本 v2.1.83 → v2.1.119，5 週 / 24 個主要功能

---

## 快速索引

| 週別 | 版本 | 主要功能 |
|------|------|---------|
| W13（Mar 23–27）| v2.1.83–85 | Auto mode、Computer use（Desktop）、PR auto-fix（Web）、Transcript search、PowerShell、Conditional hooks |
| W14（Mar 30–Apr 3）| v2.1.86–91 | Computer use（CLI）、/powerup、Flicker-free rendering、MCP result-size override、Plugin bin/ |
| W15（Apr 6–10）| v2.1.92–101 | Ultraplan、Monitor tool + /loop 自適應、/autofix-pr（CLI）、/team-onboarding |
| W16（Apr 13–17）| v2.1.105–113 | Claude Opus 4.7 + xhigh effort、Routines（Web）、/usage breakdown、/ultrareview、Native binaries |
| W17（Apr 20–24）| v2.1.114–119 | /ultrareview public preview、Session recap、Custom themes、Claude Code on the web 改版 |

---

## Week 13 · March 23–27（v2.1.83–85）

### Auto Mode（Permission 自動分類）

permissions classifier 接管 permission prompt：安全的 edit/command 自動放行，破壞性/可疑操作阻斷並顯示給用戶。介於「每次確認」和 `--dangerously-skip-permissions` 之間的中間選項。

啟用方式：`Shift+Tab` 循環切換，或設為預設：

```json
// .claude/settings.json
{
  "permissions": {
    "defaultMode": "auto"
  }
}
```

W16 更新：Max 訂閱者可在 Opus 4.7 上使用，`--enable-auto-mode` flag 不再需要。  
W17 更新：`"$defaults"` 可在 `autoMode.allow/soft_deny/environment` 中引用內建規則，不再需要完整替換。

### Computer Use（Desktop → CLI）

**W13**：Desktop app 中可控制真實桌面（原生 app、iOS simulator、硬體 control panel）。預設關閉，每次操作前詢問。  
**W14**：擴展到 CLI（research preview）：`/mcp` → 找到 `computer-use` → 開啟。

```text
> Open the iOS simulator, tap through onboarding, and screenshot each step
```

適合：沒有 API 的 app、專有工具、純 GUI 的工具。

### PR Auto-Fix（Web）

開啟 PR 時打開開關 → Claude 監控 CI，修復失敗，處理 review nit，持續 push 直到 green。  
Web UI：PR CI panel → Auto fix toggle。  
W15：CLI 也可用（見 `/autofix-pr`）。

### Transcript Search（v2.1.83）

在 transcript mode 按 `/` 搜尋，`n` / `N` 前後跳轉。

```text
Ctrl+O    # 開啟 transcript
/migrate  # 搜尋 "migrate"
n         # 下一個
N         # 上一個
```

### PowerShell Tool（v2.1.84，preview）

Windows 專屬，Claude 可執行 cmdlet、pipe 物件、使用 Windows 路徑。

```json
{
  "env": {
    "CLAUDE_CODE_USE_POWERSHELL_TOOL": "1"
  }
}
```

### Conditional Hooks（v2.1.85）

Hook 新增 `if` 欄位（permission rule 語法），只在特定條件下觸發：

```json
{
  "hooks": {
    "PreToolUse": [{
      "hooks": [{
        "if": "Bash(git commit *)",
        "type": "command",
        "command": ".claude/hooks/lint-staged.sh"
      }]
    }]
  }
}
```

### W13 其他更新

- `managed-settings.d/` 目錄：支援 layered policy fragments
- `CwdChanged` / `FileChanged` hook 事件（direnv 風格設定）
- Agents 可在 frontmatter 宣告 `initialPrompt`：session 啟動時自動送出第一個 turn
- `Ctrl+X Ctrl+E`：開啟外部編輯器（readline 相容）
- `/status` 支援 Claude 回應中使用
- 離開 75+ 分鐘後回來 → 提示 `/clear`

---

## Week 14 · March 30 – April 3（v2.1.86–91）

### /powerup — 互動式功能教學

內建動畫 demo 的互動式課程，直接在 terminal 中教學 Claude Code 功能。

```text
> /powerup
```

### Flicker-free Rendering（v2.1.89）

Alt-screen renderer + virtualized scrollback。prompt input 釘在底部，支援跨長對話的滑鼠選取，消除重繪 flicker。

```bash
export CLAUDE_CODE_NO_FLICKER=1
claude
```

取消：`unset CLAUDE_CODE_NO_FLICKER`。W16 新增 `/tui` command 可在 session 中切換。

### MCP Result-Size Override（v2.1.91）

MCP server 可對特定 tool 提高截斷上限（最高 500K 字元）。

```json
// tools/list 回應中
{
  "name": "get_schema",
  "description": "Returns the full database schema",
  "_meta": {
    "anthropic/maxResultSizeChars": 500000
  }
}
```

### Plugin bin/ — 執行檔加入 PATH（v2.1.91）

在 plugin root 放 `bin/` 目錄，plugin 啟用時該目錄自動加入 Bash tool 的 PATH：

```
my-plugin/
├── .claude-plugin/plugin.json
└── bin/
    └── my-tool     # 可直接以 my-tool 呼叫
```

### W14 其他更新

- `PermissionDenied` hook：Auto mode classifier 拒絕時觸發，可 return `retry: true` 讓 Claude 嘗試其他方法
- `defer` value for `permissionDecision`：`-p` session 在工具呼叫時暫停，以 `deferred_tool_use` payload 退出，讓 SDK 接手
- `disableSkillShellExecution`：阻止 skills/slash commands/plugin commands 中的 inline shell
- Thinking summaries 預設關閉（`showThinkingSummaries: true` 恢復）
- Hook output 超過 50K 字元時存磁碟並附路徑 + 預覽，不注入 context

---

## Week 15 · April 6–10（v2.1.92–101）

### Ultraplan（Research Preview）

從 terminal 在雲端啟動 plan mode，在瀏覽器中 review 計畫，支援對個別段落留 comment / 修改，再選擇遠端執行或送回 CLI。

```text
> /ultraplan migrate the auth service from sessions to JWTs
```

v2.1.101 更新：首次執行自動建立預設雲端環境，不需要先在 Web 設定。

### Monitor Tool（v2.1.98）

新 built-in tool：在背景啟動監控進程，每個 stdout 事件即時注入 conversation，Claude 立即回應。不需要 Bash sleep loop 佔住 turn。

```text
> Tail server.log in the background and tell me the moment a 5xx shows up
```

搭配 `/loop` 使用（現在可自適應排程：不提供 interval 時 Claude 自行決定下次觸發時機，或直接改用 Monitor tool 跳過 polling）：

```text
> /loop check CI on my PR
```

別名：`/proactive` = `/loop`。

### /autofix-pr（CLI）

從 terminal 一鍵對當前分支的 PR 啟動 Auto-Fix（不用開瀏覽器）：

```text
> /autofix-pr
```

### /team-onboarding（v2.1.101）

根據本地 Claude Code 使用紀錄生成新成員 onboarding 指南，讓隊友可以沿用你的設定而非從預設值開始。

```text
> /team-onboarding
```

### W15 其他更新

- Focus view：`Ctrl+O`（flicker-free 模式）折疊 view 為最後 prompt + 工具摘要 + 最終回應
- Bedrock / Vertex AI 設定精靈：login 畫面選「3rd-party platform」引導設定
- `/agents` 新增分頁：Running tab 顯示即時 subagents 數量
- Default effort 升為 `high`（API key、Bedrock、Vertex、Foundry、Team、Enterprise 用戶）
- `/cost` 顯示 per-model 和 cache-hit 明細
- `CLAUDE_CODE_PERFORCE_MODE`：Edit/Write 在唯讀檔案失敗時提示 `p4 edit` 而非靜默覆蓋
- OS CA certificate store 預設信任（enterprise TLS proxy 不需額外設定）
- `UserPromptSubmit` hook 可用 `hookSpecificOutput.sessionTitle` 設定 session 標題

---

## Week 16 · April 13–17（v2.1.105–113）

### Claude Opus 4.7 + xhigh Effort

Anthropic 最強 coding 模型，為 Max 和 Team Premium 的新預設。新增 `xhigh` effort level（介於 `high` 和 `max` 之間，多數 coding/agentic 任務的最佳選擇）。

```text
> /model opus
> /effort xhigh
```

`/effort` 無引數時開啟互動式 slider。詳見 `opus47-best-practices.md`（已在本 workspace 收錄）。

### Routines（Web UI 完整功能）

Web UI 建立排程代理：定時、GitHub event 觸發、API endpoint 觸發。每個 routine 有獨立的 tokened `/fire` endpoint。

```text
> /schedule daily PR review at 9am
```

詳見本 workspace `research/best-practices/11-routines.md`。

### /usage Breakdown（CLI）

`/usage` 現在顯示用量驅動因素分析：parallel sessions、subagents、cache misses、long context，各附百分比 + 優化提示。

```text
> /usage    # 按 d/w 切換 day/week 視圖
```

W17 更新：`/cost` 和 `/stats` 合併入 `/usage`，舊名稱仍可用（跳到對應 tab）。

### /ultrareview（v2.1.111）

在雲端平行執行多個 reviewer agent，再跑 adversarial critique pass 過濾誤報，結果回傳 CLI。

```text
> /ultrareview           # review 當前分支
> /ultrareview 1234      # review 指定 PR 號碼
```

W17：正式進入 public research preview，launch dialog 顯示 diffstat。

### Native Binaries（v2.1.113）

`claude` CLI 改為 native per-platform binary（非 bundled JavaScript）。npm 透過 optional dependency 安裝對應 binary（如 `@anthropic-ai/claude-code-darwin-arm64`）。升級方式不變：

```bash
claude update
claude --version
```

W17 補充：native macOS / Linux builds 中 Glob / Grep tool 替換為 embedded `bfs` / `ugrep`（更快搜尋，不需獨立 tool round-trip）。

### W16 其他更新

- Auto mode 對 Max 用戶開放 Opus 4.7，不再需要 `--enable-auto-mode` flag
- Session recap：切換回 session 時顯示一行摘要（`/recap` 手動觸發，`/config` 關閉）
- `/tui` command：session 中切換 classic / flicker-free renderer
- Push notification：Remote Control 連接 + 「Push when Claude decides」啟用 → Claude 可推播手機
- Plugin monitors：在 manifest 頂層加 `monitors` key，session 啟動或 skill invoke 時自動啟動
- `/fewer-permission-prompts`：掃描 transcript 找常見 read-only Bash/MCP 呼叫，自動生成 allowlist 建議
- `ENABLE_PROMPT_CACHING_1H`：API key / Bedrock / Vertex / Foundry 用戶啟用 1 小時 prompt cache TTL
- `PreCompact` hook 可 exit 2 或回傳 `{"decision":"block"}` 阻斷 compaction

---

## Week 17 · April 20–24（v2.1.114–119）

### Session Recap（正式功能）

切換 focus 後回來看到一行摘要，適合同時跑多個 Claude session。

```text
> /recap    # 手動觸發
# 顯示：* recap: Fixing the post-submit transcript shift bug. PR #29869. Next: ...
```

在 `/config` 關閉自動 recap。

### Custom Themes（v2.1.118）

在 `/theme` 建立命名 color scheme，或手動編輯 `~/.claude/themes/` 中的 JSON。每個 theme 選擇 base preset 並覆蓋特定 token。Plugin 也可以打包 theme。

```text
> /theme    # 開啟 theme picker
```

### Claude Code on the Web 改版

claude.ai/code 全新介面：sessions sidebar、drag-and-drop layout、routines view 更新。效能和可靠性提升。

### W17 其他更新

- Vim visual mode：在 prompt input 按 `v`（字元選取）或 `V`（行選取），支援 operator
- Hooks 可直接呼叫 MCP tools（`type: "mcp_tool"`），不需要 spawn process
- Forked subagents：`CLAUDE_CODE_FORK_SUBAGENT=1` 讓 fork 時繼承完整 parent context（詳見 `subagent-advanced.md`）
- Pro / Max 訂閱者在 Opus 4.6 / Sonnet 4.6 上 default effort 升為 `high`（原為 `medium`）
- `--from-pr` 支援 GitLab MR、Bitbucket PR、GitHub Enterprise URL
- `claude plugin tag` command：為 plugin 建立 release git tag（含 version validation）
- Opus 4.7 session 改用模型原生 1M context window 計算，修復 `/context` 百分比偏高問題
- `/resume` 對大型 session 提速 67%，並提供「先看摘要再決定」選項

---

## 功能演進對照表

| 功能 | 首次出現 | 後續更新 |
|------|---------|---------|
| Auto mode | W13（research preview）| W16 正式開放 Max |
| Computer use | W13 Desktop | W14 CLI |
| PR auto-fix | W13 Web | W15 /autofix-pr CLI 指令 |
| Flicker-free | W14 | W16 /tui 切換指令 |
| /ultrareview | W16 v2.1.111 | W17 public research preview |
| Session recap | W16（Other wins）| W17 正式功能 |
| Native binaries | W16 v2.1.113 | W17 macOS/Linux bfs+ugrep |

---

## 本 Workspace 整合建議

- **Auto mode** → 更新 `.claude/settings.json` 設 `"defaultMode": "auto"`（已在 W13 啟用）
- **Conditional hooks** → 現有 `pre-commit-review.sh` 可改用 `"if": "Bash(git commit *)"` 縮小觸發範圍
- **Monitor tool** → 搭配 `/deep-review` skill 用於 CI babysitting（`/loop check CI`）
- **`/ultrareview`** → PR merge 前的深度雲端 review，補充本地 `/deep-review`
- **1h prompt caching** → 若使用 API key，設 `ENABLE_PROMPT_CACHING_1H=1` 降低 cost
- **Session recap** → 多 session 工作流時啟用（`/config`）

# MCP Server 與 Skills

MCP（Model Context Protocol）是 AI 工具整合的開放標準，讓 Claude Code 連接外部工具、資料庫和 API。Skills 是輕量的可複用指令範本，不需要 MCP server 也能擴充 Claude 的能力。

## 什麼是 MCP？

**使用時機**：當你需要把資料從其他工具複製貼進 chat 時（issue tracker、監控儀表板），連接該工具的 MCP server 讓 Claude 直接存取和操作。

**可以做到的事**：

- `"Add the feature described in JIRA issue ENG-4521 and create a PR"` — 從 JIRA 實作 feature
- `"Check Sentry and Statsig to check the usage of feature ENG-4521"` — 分析監控資料
- `"Find emails of 10 random users who used feature ENG-4521"` — 查詢資料庫
- `"Update email template based on new Figma designs posted in Slack"` — 整合設計
- `"Create Gmail drafts inviting 10 users to a feedback session"` — 自動化工作流程

---

## 三種 Transport 安裝方式

### Option 1：Remote HTTP Server（推薦）

```bash
# 基本語法
claude mcp add --transport http <name> <url>

# 範例：連接 Notion
claude mcp add --transport http notion https://mcp.notion.com/mcp

# 帶 Bearer token
claude mcp add --transport http secure-api https://api.example.com/mcp \
  --header "Authorization: Bearer your-token"
```

### Option 2：Remote SSE Server（已棄用）

> **SSE transport 已棄用**，優先使用 HTTP。

```bash
claude mcp add --transport sse asana https://mcp.asana.com/sse
```

### Option 3：Local Stdio Server

在本地跑的 process，適合需要直接系統存取或自訂 script 的工具：

```bash
claude mcp add --transport stdio --env AIRTABLE_API_KEY=YOUR_KEY airtable \
  -- npx -y airtable-mcp-server
```

> **重要**：所有 option（`--transport`, `--env`, `--scope`, `--header`）必須在 server name **之前**；`--` 之後才是傳給 MCP server 的 command。

### 管理 Server

```bash
claude mcp list               # 列出所有已設定的 server
claude mcp get github         # 取得特定 server 詳情
claude mcp remove github      # 移除 server
/mcp                          # 在 Claude Code 內查看 server 狀態
```

---

## MCP Installation Scope

| Scope | 載入範圍 | 共享給團隊 | 儲存位置 |
|-------|---------|----------|---------|
| **Local**（預設）| 只在當前 project | 否 | `~/.claude.json` |
| **Project** | 只在當前 project | 是（via version control）| `.mcp.json`（project root）|
| **User** | 所有你的 project | 否 | `~/.claude.json` |

```bash
--scope local    # 預設，只在當前 project，不共享
--scope project  # 透過 .mcp.json 共享給整個 team
--scope user     # 跨所有 project，個人使用
```

### Project Scope 範例（`.mcp.json`）

```json
{
  "mcpServers": {
    "shared-server": {
      "type": "http",
      "url": "${API_BASE_URL:-https://api.example.com}/mcp",
      "headers": {
        "Authorization": "Bearer ${API_KEY}"
      }
    }
  }
}
```

支援環境變數展開語法：`${VAR}` 和 `${VAR:-default}`。

**Scope 優先序**：Local > Project > User > Plugin-provided > claude.ai connectors

---

## OAuth 認證

Claude Code 支援 OAuth 2.0 安全連接需要認證的 remote MCP server。

### 基本 OAuth 設定

```bash
# 1. 加入 server
claude mcp add --transport http sentry https://mcp.sentry.dev/mcp
# 2. 在 Claude Code 內觸發登入流程
/mcp
```

Token 儲存在系統 keychain（macOS）或 credentials 檔案，自動更新。

### 限制 OAuth Scopes

```json
{
  "mcpServers": {
    "slack": {
      "type": "http",
      "url": "https://mcp.slack.com/mcp",
      "oauth": {
        "scopes": "channels:read chat:write search:read"
      }
    }
  }
}
```

`oauth.scopes` 指定的 scope 優先於 server 自己 advertise 的 scope。

---

## Tool Search（大規模 MCP 工具管理）

Tool Search 讓 Claude 動態發現所需的 MCP 工具，降低 context window 使用：

| `ENABLE_TOOL_SEARCH` 值 | 行為 |
|------------------------|------|
| （未設定，預設）| 所有 MCP tool 延遲載入 |
| `true` | 強制所有 MCP tool 延遲載入，包含 Vertex AI |
| `auto` | Threshold 模式：工具符合 context window 10% 則 upfront 載入，否則延遲 |
| `auto:<N>` | 自訂 threshold 百分比（0-100）|
| `false` | 所有 MCP tool upfront 載入 |

```bash
ENABLE_TOOL_SEARCH=auto:5 claude    # 自訂 5% threshold
ENABLE_TOOL_SEARCH=false claude     # 停用 tool search
```

**需要 Sonnet 4 或 Opus 4 以上**；Haiku 不支援 tool search。

---

## 動態功能

### Dynamic Tool Updates

Claude Code 支援 MCP `list_changed` notification，允許 MCP server 動態更新工具列表，無需斷線重連。

### Automatic Reconnection

HTTP/SSE server 中斷時自動重連（exponential backoff）：

- 最多重試 5 次，初始延遲 1 秒，每次 double
- 重連中 server 在 `/mcp` 顯示為 pending
- 5 次失敗後標記為 failed，可從 `/mcp` 手動重試
- Auth error 和 not-found error 不重試（需修改設定）

---

## 實際範例

### 錯誤監控（Sentry）

```bash
claude mcp add --transport http sentry https://mcp.sentry.dev/mcp
/mcp  # 登入驗證
```

```text
What are the most common errors in the last 24 hours?
Which deployment introduced these new errors?
```

### GitHub Code Review

```bash
claude mcp add --transport http github https://api.githubcopilot.com/mcp/ \
  --header "Authorization: Bearer YOUR_GITHUB_PAT"
```

```text
Review PR #456 and suggest improvements
Create a new issue for the bug we just found
```

### 查詢 PostgreSQL 資料庫

```bash
claude mcp add --transport stdio db -- npx -y @bytebase/dbhub \
  --dsn "postgresql://readonly:pass@prod.db.com:5432/analytics"
```

```text
What's our total revenue this month?
Find customers who haven't made a purchase in 90 days
```

---

## Managed MCP（組織管控）

### Option 1：Exclusive Control（`managed-mcp.json`）

部署固定 MCP server 列表，**用戶無法修改或新增**：

| 平台 | 部署路徑 |
|------|---------|
| macOS | `/Library/Application Support/ClaudeCode/managed-mcp.json` |
| Linux / WSL | `/etc/claude-code/managed-mcp.json` |
| Windows | `C:\Program Files\ClaudeCode\managed-mcp.json` |

### Option 2：Policy-based Control（allowlists/denylists）

```json
{
  "allowedMcpServers": [
    { "serverName": "github" },
    { "serverUrl": "https://mcp.company.com/*" },
    { "serverUrl": "https://*.internal.corp/*" }
  ],
  "deniedMcpServers": [
    { "serverUrl": "https://*.untrusted.com/*" }
  ]
}
```

---

## Skills 設計

Skills 是輕量的可複用指令範本（Markdown 檔案），存放在 `.claude/skills/` 目錄。

### 基本結構

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
```

### Skills 設計原則

- **描述要清楚**：description 是 Claude 判斷何時使用的依據
- **`$ARGUMENTS`**：接收 slash command 的參數
- **`disable-model-invocation: true`**：跳過語言模型，直接執行指令文字（快速且節省 token）
- **範圍清晰**：一個 skill 只做一件事

### 在 Session 中使用

```text
/fix-issue 123           # 執行 fix-issue skill，參數為 "123"
/skills                  # 列出所有可用 skills
```

---

## 延伸閱讀

- [官方 MCP 文件](https://code.claude.com/docs/en/mcp)
- [MCP 官方規格](https://modelcontextprotocol.io/introduction)
- [Skills 文件](https://code.claude.com/docs/en/skills)
- [Lecture 05：記憶系統與工作區設計](/lectures/lecture-05-memory-workspace/)

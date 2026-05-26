# MCP (Model Context Protocol) 整合完整指南

> 來源：https://code.claude.com/docs/en/mcp
> 收錄日期：2026-05-01
> 涵蓋：MCP 安裝設定（HTTP/SSE/stdio 三種 transport）、Scope 管理、OAuth 認證、Tool Search、Managed MCP 組織管控、Claude Code 作為 MCP server

---

## 什麼是 MCP？

Model Context Protocol (MCP) 是 AI 工具整合的開放標準，讓 Claude Code 連接外部工具、資料庫和 API。MCP server 讓 Claude Code 能直接讀取和操作其他系統，無需手動複製貼上資料。

**使用時機**：當你需要把資料從其他工具複製貼進 chat（issue tracker、監控儀表板）時，連接該工具的 MCP server 讓 Claude 直接存取和操作。

**可以做到的事**：

- 從 JIRA 實作 feature：`"Add the feature described in JIRA issue ENG-4521 and create a PR"`
- 分析監控資料：`"Check Sentry and Statsig to check the usage of feature ENG-4521"`
- 查詢資料庫：`"Find emails of 10 random users who used feature ENG-4521"`
- 整合設計：`"Update email template based on new Figma designs posted in Slack"`
- 自動化工作流程：`"Create Gmail drafts inviting 10 users to a feedback session"`

---

## 安裝 MCP Server

### Option 1：Remote HTTP Server（推薦）

HTTP 是遠端 MCP server 的推薦 transport，支援最廣泛。

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

在本地跑的 process，適合需要直接系統存取或自訂 script 的工具。

```bash
# 基本語法
claude mcp add [options] <name> -- <command> [args...]

# 範例：Airtable
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

## 動態功能

### Dynamic Tool Updates

Claude Code 支援 MCP `list_changed` notification，允許 MCP server 動態更新工具列表，無需斷線重連。

### Automatic Reconnection

HTTP/SSE server 中斷時自動重連（exponential backoff）：

- 最多重試 5 次
- 初始延遲 1 秒，每次 double
- 重連中 server 在 `/mcp` 顯示為 pending
- 5 次失敗後標記為 failed，可從 `/mcp` 手動重試
- v2.1.121 起：初始連線也重試 3 次（5xx、connection refused、timeout）
- Auth error 和 not-found error 不重試（需修改設定）
- Stdio server 為本地 process，不自動重連

---

## MCP Installation Scope

| Scope | 載入範圍 | 共享給團隊 | 儲存位置 |
|-------|---------|----------|---------|
| **Local**（預設）| 只在當前 project | 否 | `~/.claude.json` |
| **Project** | 只在當前 project | 是（via version control）| `.mcp.json`（project root）|
| **User** | 所有你的 project | 否 | `~/.claude.json` |

### Local Scope（預設）

```bash
claude mcp add --transport http stripe https://mcp.stripe.com
# 等同
claude mcp add --transport http stripe --scope local https://mcp.stripe.com
```

結果寫入 `~/.claude.json`（注意：與 general local settings 的 `.claude/settings.local.json` 不同）：

```json
{
  "projects": {
    "/path/to/your/project": {
      "mcpServers": {
        "stripe": { "type": "http", "url": "https://mcp.stripe.com" }
      }
    }
  }
}
```

### Project Scope（團隊共享）

```bash
claude mcp add --transport http paypal --scope project https://mcp.paypal.com/mcp
```

建立或更新 `.mcp.json`（設計為 check into version control）：

```json
{
  "mcpServers": {
    "shared-server": {
      "command": "/path/to/server",
      "args": [],
      "env": {}
    }
  }
}
```

> **安全提示**：從 `.mcp.json` 使用 project-scoped server 前會提示核准。重置核准記錄：`claude mcp reset-project-choices`

### User Scope（跨 project 個人使用）

```bash
claude mcp add --transport http hubspot --scope user https://mcp.hubspot.com/anthropic
```

### Scope 優先序

1. Local scope
2. Project scope
3. User scope
4. Plugin-provided servers
5. claude.ai connectors

同名 server 只連一次（用最高優先序的定義），plugins 和 connectors 以 endpoint 匹配重複。

### `.mcp.json` 環境變數展開

```json
{
  "mcpServers": {
    "api-server": {
      "type": "http",
      "url": "${API_BASE_URL:-https://api.example.com}/mcp",
      "headers": {
        "Authorization": "Bearer ${API_KEY}"
      }
    }
  }
}
```

支援語法：`${VAR}` 和 `${VAR:-default}`。可用位置：`command`, `args`, `env`, `url`, `headers`。

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

### 固定 OAuth Callback Port

部分 MCP server 需要預先註冊特定 redirect URI：

```bash
claude mcp add --transport http \
  --callback-port 8080 \
  my-server https://mcp.example.com/mcp
```

### Pre-configured OAuth Credentials

當 server 不支援 Dynamic Client Registration 時：

```bash
claude mcp add --transport http \
  --client-id your-client-id --client-secret --callback-port 8080 \
  my-server https://mcp.example.com/mcp
```

或用 JSON 格式：

```bash
claude mcp add-json my-server \
  '{"type":"http","url":"https://mcp.example.com/mcp","oauth":{"clientId":"your-client-id","callbackPort":8080}}' \
  --client-secret
```

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

### Override OAuth Metadata Discovery

```json
{
  "mcpServers": {
    "my-server": {
      "type": "http",
      "url": "https://mcp.example.com/mcp",
      "oauth": {
        "authServerMetadataUrl": "https://auth.example.com/.well-known/openid-configuration"
      }
    }
  }
}
```

需要 Claude Code v2.1.64 或更新版本。

### Dynamic Headers（非 OAuth 認證）

適用 Kerberos、短效 token、內部 SSO 等非 OAuth 認證：

```json
{
  "mcpServers": {
    "internal-api": {
      "type": "http",
      "url": "https://mcp.internal.example.com",
      "headersHelper": "/opt/bin/get-mcp-auth-headers.sh"
    }
  }
}
```

Helper script 要求：
- 輸出 JSON object（string key-value pairs）到 stdout
- 在 shell 中執行，10 秒 timeout
- Dynamic headers 覆蓋同名 static headers
- 每次連線（session start + reconnect）重新執行，不快取

Claude Code 注入的環境變數：`CLAUDE_CODE_MCP_SERVER_NAME`、`CLAUDE_CODE_MCP_SERVER_URL`

---

## 從 JSON 設定加入 Server

```bash
# HTTP server
claude mcp add-json weather-api \
  '{"type":"http","url":"https://api.weather.com/mcp","headers":{"Authorization":"Bearer token"}}'

# Stdio server
claude mcp add-json local-weather \
  '{"type":"stdio","command":"/path/to/weather-cli","args":["--api-key","abc123"],"env":{"CACHE_DIR":"/tmp"}}'
```

### 從 Claude Desktop 匯入

```bash
claude mcp add-from-claude-desktop  # 互動式選擇要匯入哪些 server
claude mcp list                     # 確認已匯入
```

> 只支援 macOS 和 WSL；同名 server 加數字後綴（`server_1`）。

---

## Tool Search（大規模 MCP 工具管理）

Tool Search 讓 Claude 動態發現所需的 MCP 工具，降低 context window 使用：

| `ENABLE_TOOL_SEARCH` 值 | 行為 |
|------------------------|------|
| （未設定，預設）| 所有 MCP tool 延遲載入，Vertex AI 或非 first-party `ANTHROPIC_BASE_URL` 除外（upfront 載入）|
| `true` | 強制所有 MCP tool 延遲載入，包含 Vertex AI |
| `auto` | Threshold 模式：工具符合 context window 10% 則 upfront 載入，否則延遲 |
| `auto:<N>` | 自訂 threshold 百分比（0-100）|
| `false` | 所有 MCP tool upfront 載入 |

```bash
ENABLE_TOOL_SEARCH=auto:5 claude    # 自訂 5% threshold
ENABLE_TOOL_SEARCH=false claude     # 停用 tool search
```

**停用 ToolSearch 工具**：

```json
{
  "permissions": {
    "deny": ["ToolSearch"]
  }
}
```

**Exempt 特定 server（永遠 upfront 載入）**：

```json
{
  "mcpServers": {
    "core-tools": {
      "type": "http",
      "url": "https://mcp.example.com/mcp",
      "alwaysLoad": true
    }
  }
}
```

需要 Claude Code v2.1.121 或更新版本。也可在 tool 的 `_meta` 設定個別工具：`"anthropic/alwaysLoad": true`。

**需要 Sonnet 4 或 Opus 4 以上**；Haiku 不支援 tool search。

---

## MCP Output 限制

| 設定 | 預設值 | 說明 |
|------|--------|------|
| Warning threshold | 10,000 tokens | 超過時顯示警告 |
| Default max | 25,000 tokens | `MAX_MCP_OUTPUT_TOKENS` 控制 |
| 可覆蓋 | 是 | `export MAX_MCP_OUTPUT_TOKENS=50000 claude` |
| 單工具覆蓋 | 是 | 工具 `_meta["anthropic/maxResultSizeChars"]`（最高 500,000 字元）|

```json
{
  "name": "get_schema",
  "description": "Returns the full database schema",
  "_meta": {
    "anthropic/maxResultSizeChars": 200000
  }
}
```

---

## MCP Elicitation（互動式請求）

MCP server 可在執行中途請求結構化輸入：

- **Form mode**：Claude Code 顯示 dialog 填表
- **URL mode**：開啟 browser 完成 auth/approval 流程
- 自動回應：用 [`Elicitation` hook](https://code.claude.com/docs/en/hooks#elicitation)

---

## 使用 MCP Resources

```text
@server:protocol://resource/path   # 參照格式
@github:issue://123                # 範例
@docs:file://api/authentication    # 範例
```

在 prompt 輸入 `@` 可看到所有已連接 MCP server 的可用 resource（autocomplete）。

---

## Plugin-provided MCP Servers

Plugin 可打包 MCP server，啟用 plugin 時 server 自動啟動：

```json
{
  "mcpServers": {
    "database-tools": {
      "command": "${CLAUDE_PLUGIN_ROOT}/servers/db-server",
      "args": ["--config", "${CLAUDE_PLUGIN_ROOT}/config.json"],
      "env": { "DB_URL": "${DB_URL}" }
    }
  }
}
```

特殊環境變數：
- `${CLAUDE_PLUGIN_ROOT}`：plugin 打包檔案路徑
- `${CLAUDE_PLUGIN_DATA}`：跨 plugin 更新的持久狀態目錄

Session 中 enable/disable plugin 後執行 `/reload-plugins` 更新 MCP 連線。

---

## 使用 claude.ai 上的 MCP Server

登入 Claude Code 的 claude.ai 帳號後，claude.ai 上設定的 MCP server 自動在 Claude Code 可用（[claude.ai/customize/connectors](https://claude.ai/customize/connectors)）。

停用：

```bash
ENABLE_CLAUDEAI_MCP_SERVERS=false claude
```

---

## Claude Code 作為 MCP Server

```bash
# 啟動 Claude 作為 stdio MCP server
claude mcp serve
```

在 Claude Desktop 的 `claude_desktop_config.json` 加入：

```json
{
  "mcpServers": {
    "claude-code": {
      "type": "stdio",
      "command": "claude",
      "args": ["mcp", "serve"],
      "env": {}
    }
  }
}
```

> 若 `claude` 不在 `$PATH`，需用 `which claude` 找到完整路徑。

---

## Managed MCP Configuration（組織管控）

### Option 1：Exclusive Control（managed-mcp.json）

部署固定 MCP server 列表，**用戶無法修改或新增**：

| 平台 | 部署路徑 |
|------|---------|
| macOS | `/Library/Application Support/ClaudeCode/managed-mcp.json` |
| Linux / WSL | `/etc/claude-code/managed-mcp.json` |
| Windows | `C:\Program Files\ClaudeCode\managed-mcp.json` |

格式與標準 `.mcp.json` 相同：

```json
{
  "mcpServers": {
    "github": { "type": "http", "url": "https://api.githubcopilot.com/mcp/" },
    "company-internal": {
      "type": "stdio",
      "command": "/usr/local/bin/company-mcp-server",
      "args": ["--config", "/etc/company/mcp-config.json"]
    }
  }
}
```

### Option 2：Policy-based Control（allowlists/denylists）

允許用戶新增 server，但限制哪些 server 被允許。在 managed settings 中設定：

```json
{
  "allowedMcpServers": [
    { "serverName": "github" },
    { "serverCommand": ["npx", "-y", "@modelcontextprotocol/server-filesystem"] },
    { "serverUrl": "https://mcp.company.com/*" },
    { "serverUrl": "https://*.internal.corp/*" }
  ],
  "deniedMcpServers": [
    { "serverName": "dangerous-server" },
    { "serverUrl": "https://*.untrusted.com/*" }
  ]
}
```

#### 三種限制方式

| 方式 | 說明 | 匹配邏輯 |
|------|------|---------|
| `serverName` | 以設定名稱匹配 | 完全匹配 |
| `serverCommand` | 以指令和參數匹配 stdio server | **完全匹配**（順序也要對）|
| `serverUrl` | 以 URL 模式匹配 remote server | 支援 `*` wildcard |

#### 行為說明

**Allowlist（`allowedMcpServers`）**：
- `undefined`：無限制
- `[]`：完全鎖定，不允許任何 MCP server
- 有條目：只允許匹配的 server

**Denylist（`deniedMcpServers`）**：
- `undefined` 或 `[]`：不封鎖任何 server
- Denylist 絕對優先（即使在 allowlist 也封鎖）

**Stdio server**：allowlist 有任何 `serverCommand` 條目時，stdio server 必須匹配命令，僅名稱匹配不夠。  
**Remote server**：allowlist 有任何 `serverUrl` 條目時，remote server 必須匹配 URL 模式。

#### URL Wildcard 範例

```
https://mcp.company.com/*         # 特定 domain 的所有路徑
https://*.example.com/*           # example.com 的任何 subdomain
http://localhost:*/*              # localhost 的任何 port
```

**Option 1 + Option 2 可並用**：`managed-mcp.json` 存在時取得獨占控制，allowlists/denylists 仍適用於 managed server 的篩選。

---

## MCP Prompts 作為 Commands

MCP server 可以 expose prompt 並在 Claude Code 中當 command 使用：

```text
/                                          # 列出所有可用 command（含 MCP prompt）
/mcp__github__list_prs                     # 執行 prompt（無參數）
/mcp__github__pr_review 456               # 執行 prompt（帶參數）
/mcp__jira__create_issue "Bug in login" high
```

格式：`/mcp__<servername>__<promptname>`，server 和 prompt 名稱用底線取代空格。

---

## Tips 彙整

```bash
# scope 設定
--scope local    # 預設，只在當前 project，不共享
--scope project  # 透過 .mcp.json 共享給整個 team
--scope user     # 跨所有 project，個人使用

# 環境變數
--env KEY=value                     # 設定環境變數
MCP_TIMEOUT=10000 claude            # 設定 MCP server 啟動 timeout（ms）
MAX_MCP_OUTPUT_TOKENS=50000 claude  # 調高 output token 上限

# OAuth
/mcp   # 觸發 OAuth 認證流程，或查看 server 狀態
```

---

## 延伸閱讀

- [MCP 官方規格](https://modelcontextprotocol.io/introduction)
- [MCP Server Registry](https://api.anthropic.com/mcp-registry/docs)
- [GitHub MCP Servers 集合](https://github.com/modelcontextprotocol/servers)
- [MCP SDK（自建 server）](https://modelcontextprotocol.io/quickstart/server)
- [claude.ai Connectors](https://claude.ai/customize/connectors)
- [Channels（MCP push 訊息）](https://code.claude.com/docs/en/channels)
- [Plugins（打包 MCP server）](https://code.claude.com/docs/en/plugins)
- [Hooks（自動化 MCP elicitation）](https://code.claude.com/docs/en/hooks#elicitation)

# Lecture 11：MCP 整合與外部系統

## 學習目標

完成本課後，你將能夠：

- 判斷什麼時候該接 MCP，什麼時候該寫 Skill 或 Hook
- 用三種 transport 安裝 MCP server，並正確選擇 scope
- 設計 intent-grouped 的工具介面，而非逐一映射 API endpoint
- 用 Tool Search 控制大量 MCP 工具的 context 成本
- 設定 OAuth、dynamic headers 與組織層級的 managed MCP 管控
- 說明 MCP 2026-07-28 規格的 stateless core 對自建 server 的影響

## 核心概念

### MCP 是什麼，什麼時候用

MCP（Model Context Protocol）是 AI 工具整合的開放標準，讓 Claude Code 連接外部工具、資料庫與 API。

**觸發點只有一個，但很明確**：

> 你一直在把資料從其他工具**複製貼進對話**（issue tracker、監控儀表板、資料庫）——就該把那個系統接成 MCP server。

接上後能做的事：

```text
"Add the feature described in JIRA issue ENG-4521 and create a PR"
"Check Sentry and Statsig to check the usage of feature ENG-4521"
"Find emails of 10 random users who used feature ENG-4521"
"Update email template based on new Figma designs posted in Slack"
```

**MCP 提供能力，Skill 提供如何有效使用的知識**——兩者是搭配關係，不是替代關係。典型組合：MCP server 連接資料庫，Skill 記錄你的資料模型與常用 query patterns。

| 面向 | MCP | Skill | Hook |
|------|-----|-------|------|
| 本質 | 連接外部服務的協定 | 知識、workflows、參考資料 | 生命週期事件的確定性觸發器 |
| 提供 | Tools 和資料存取 | 怎麼用的知識 | 一定會發生的動作 |
| Context 成本 | Session start 載入 tool names，schema 按需 | 描述常駐，全文按需 | 零 |

### 三種 transport

| Transport | 用途 | 狀態 |
|-----------|------|------|
| **HTTP** | 遠端 server（推薦）| 支援最廣泛 |
| **SSE** | 遠端 server | **已棄用**，改用 HTTP |
| **stdio** | 本地 process | 需要直接系統存取或自訂 script 時 |

```bash
claude mcp add --transport http notion https://mcp.notion.com/mcp
claude mcp add --transport http secure-api https://api.example.com/mcp \
  --header "Authorization: Bearer your-token"
claude mcp add --transport stdio --env AIRTABLE_API_KEY=YOUR_KEY airtable \
  -- npx -y airtable-mcp-server
```

**語法陷阱**：所有 option（`--transport`、`--env`、`--scope`、`--header`）必須在 **server name 之前**；`--` 之後才是傳給 MCP server 的命令。

### 三種 Scope

| Scope | 載入範圍 | 共享給團隊 | 儲存位置 |
|-------|---------|----------|---------|
| **Local**（預設）| 只在當前 project | 否 | `~/.claude.json` |
| **Project** | 只在當前 project | **是**（via version control）| `.mcp.json`（project root）|
| **User** | 你所有的 project | 否 | `~/.claude.json` |

**優先序**：local > project > user。要讓團隊共用就用 `--scope project`，設定會進 `.mcp.json` 並跟著 repo 走。

注意 `~/.claude.json` 與 `.claude/settings.local.json` **不是同一個檔案**，前者存 MCP 設定，後者存一般 local settings。

### 工具數量與 context 成本

兩條經驗法則，方向一致：

- **常見建議 3–6 個 MCP server**。太多會稀釋模型的工具選擇品質。
- 官方在《Seeing like an agent》裡提到約 **20 個工具**的上限感。

超過就靠 Tool Search 處理。

### Tool Search：把 schema 變成按需載入

| `ENABLE_TOOL_SEARCH` | 行為 |
|---------------------|------|
| （未設定，預設）| 所有 MCP tool 延遲載入（Vertex AI 或非 first-party base URL 除外）|
| `true` | 強制全部延遲載入，包含 Vertex AI |
| `auto` | Threshold 模式：工具佔 context window 10% 以內就 upfront 載入 |
| `auto:<N>` | 自訂 threshold 百分比 |
| `false` | 全部 upfront 載入 |

官方數據：**Tool Search 模式可降低 85%+ 的 token 用量**。

這正是 [Lecture 03](/lectures/lecture-03-context-engineering/) 提到的 **deferred loading** 在 MCP 上的體現——工具在取得 schema 前**不可呼叫**，這條紀律不因規格改版而改變。

要讓某個核心 server 永遠 upfront 載入，設 `alwaysLoad: true`（W18）。

### 有效的 MCP server 怎麼設計

官方在《Building agents that reach production systems with MCP》給的核心建議：

> **以意圖分組工具（intent-grouped），而不是逐一映射 API endpoint。**

差別在於：

```
❌ 逐一映射：list_issues / get_issue / create_issue / update_issue /
             add_label / remove_label / assign_user / ...（20 個工具）

✅ 意圖分組：find_issues(query, filters)      — 找到相關 issue
             triage_issue(id, action)         — 分類、貼標、指派
             create_issue(spec)               — 建立
```

模型不需要知道你的 REST API 長什麼樣，它需要知道**能達成什麼目的**。

工具的參數設計同樣重要——這是 Claude 5 世代 context engineering 六條規則裡的第二條：**用表達力強的參數與清楚的 enumeration 取代使用範例**（`status: pending / in_progress / completed`），因為範例會限縮探索空間。

### MCP 2026-07-28 規格（第五版）

| # | 變更 | 意義 |
|---|------|------|
| 1 | **Stateless core** | 從雙向有狀態協定改為 request/response；server 可直接部署在 serverless / edge |
| 2 | **Extensions 框架標準化** | MCP Apps 與 Tasks 以**版本化 extension** 出貨，新增能力不必動核心協定 |
| 3 | **Authorization 對齊 OAuth 2.0 / OIDC** | 可直接接 Entra、Okta 等既有 IdP，不需 workaround |
| 4 | **MCP Apps** | server 可在對話中直接算繪互動元件，免切分頁 |
| 5 | **Tasks** | 長時間執行工作的標準化表達 |
| 6 | **企業託管存取** | 管理員透過 IdP 佈建 connector，群組繼承存取權，終端使用者零設定 |

**Claude 端現況**：全產品線支援上述能力，可用 MCP server **超過 950 個**；已發布的 connector 取得 dashboard，可看效能、採用、錯誤與跨產品使用量。

**對自建 server 的實務影響**：如果你的 server 原本依賴長連線的雙向通知，需要評估遷移到 **Tasks extension**。

### 長工具呼叫自動轉背景

v2.1.212 起，MCP 工具呼叫**超過 2 分鐘自動轉背景**，session 保持可用（`CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS` 可調）。這改變了「跑很久的 MCP 查詢會卡住整個 session」的舊假設。

### Output 限制

| 設定 | 預設值 |
|------|--------|
| 警告門檻 | 10,000 tokens |
| 預設上限 | 25,000 tokens（`MAX_MCP_OUTPUT_TOKENS`）|
| 單工具覆蓋 | 工具 `_meta["anthropic/maxResultSizeChars"]`，最高 500,000 字元 |

一個回傳整份 DB schema 的工具很容易撞到這個上限——這時候的正解通常不是調高上限，而是**把工具改成回傳摘要 + 提供鑽取工具**。

### 認證：OAuth 與非 OAuth

**OAuth**：在 Claude Code 裡執行 `/mcp` 觸發認證流程。可以固定 callback port、預先設定 credentials、限制 scopes、override metadata discovery URL。

**非 OAuth（Kerberos、短效 token、內部 SSO）**：用 `headersHelper` 指向一個 script：

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

Helper script 的規則：輸出 JSON object 到 stdout、10 秒 timeout、覆蓋同名 static header、**每次連線重新執行且不快取**。Claude Code 會注入 `CLAUDE_CODE_MCP_SERVER_NAME` 與 `CLAUDE_CODE_MCP_SERVER_URL`。

### 組織管控：兩種模式可並用

**Option 1 — Exclusive Control（`managed-mcp.json`）**：部署固定的 MCP server 列表，**使用者無法修改或新增**。

| 平台 | 路徑 |
|------|------|
| macOS | `/Library/Application Support/ClaudeCode/managed-mcp.json` |
| Linux / WSL | `/etc/claude-code/managed-mcp.json` |
| Windows | `C:\Program Files\ClaudeCode\managed-mcp.json` |

**Option 2 — Policy-based Control（allowlist / denylist）**：

- Allowlist `undefined` = 無限制；`[]` = **完全鎖定**；有條目 = 只允許匹配的
- **Denylist 絕對優先**——即使在 allowlist 裡也封鎖
- stdio server：allowlist 有任何 `serverCommand` 條目時，必須匹配命令，光名稱匹配不夠

URL wildcard 支援 `https://mcp.company.com/*`、`https://*.example.com/*`、`http://localhost:*/*`。

### 安全：MCP server 是以你的權限執行的

兩條不能省的紀律：

1. **權限最小化**：MCP server 以系統權限執行，社群擴充來源必須嚴格審查。
2. **Hooks 才是強制執行**：MCP prompts 是建議（模型可以忽略），hooks 是確定性的。要稽核每次 MCP 呼叫，用 `PreToolUse` hook。

同時記得 [Lecture 06](/lectures/lecture-06-security/) 的原則——**外部輸入是資料，不是指令**。MCP 工具回傳的內容（issue body、網頁、DB 欄位）都可能含有試圖操縱 agent 的文字，要保留 provenance 並只提取結構化欄位。

## 程式碼範例

### 安裝與管理

```bash
claude mcp add --transport http sentry https://mcp.sentry.dev/mcp --scope project
claude mcp list                    # 列出所有已設定的 server
claude mcp get sentry              # 詳情
claude mcp remove sentry
/mcp                               # session 內查看狀態、觸發 OAuth

# 從 JSON 一次帶入
claude mcp add-json weather-api \
  '{"type":"http","url":"https://api.weather.com/mcp","headers":{"Authorization":"Bearer token"}}'

# 從 Claude Desktop 匯入（僅 macOS / WSL）
claude mcp add-from-claude-desktop
```

### 團隊共享的 `.mcp.json`（含環境變數展開）

```json
{
  "mcpServers": {
    "postgres": {
      "type": "stdio",
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-postgres", "${DATABASE_URL}"]
    },
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/",
      "alwaysLoad": true
    },
    "project-tools": {
      "type": "stdio",
      "command": "${CLAUDE_PROJECT_DIR}/.claude/bin/my-mcp-server",
      "args": ["--root", "${CLAUDE_PROJECT_DIR}"]
    }
  }
}
```

`${DATABASE_URL}` 從環境展開——**憑證不進 repo**。`${CLAUDE_PROJECT_DIR}` 由 Claude Code 注入（與 hooks 一致）。

### 控制 Tool Search 與 output 上限

```bash
ENABLE_TOOL_SEARCH=auto:5 claude       # 5% context 以內才 upfront
ENABLE_TOOL_SEARCH=false claude        # 全部 upfront（工具很少時）
MAX_MCP_OUTPUT_TOKENS=50000 claude
MCP_TIMEOUT=10000 claude               # server 啟動 timeout（ms）
CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS=120000 claude
```

停用 ToolSearch 工具本身：

```json
{ "permissions": { "deny": ["ToolSearch"] } }
```

### 稽核每次 MCP 呼叫

```bash
#!/bin/bash
# .claude/hooks/audit-mcp-call.sh — PreToolUse
set -euo pipefail

INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | jq -r '.tool_name')

# MCP 工具名稱格式：mcp__<server>__<tool>
if [[ "$TOOL_NAME" == mcp__* ]]; then
  SERVER=$(echo "$TOOL_NAME" | cut -d_ -f3)
  printf '%s\t%s\t%s\n' "$(date -u +%FT%TZ)" "$SERVER" "$TOOL_NAME" \
    >> "${CLAUDE_PROJECT_DIR}/.claude/mcp-audit.log"

  # 寫入型的外部服務需要額外把關
  case "$TOOL_NAME" in
    mcp__github__create_*|mcp__jira__create_*|mcp__slack__post_*)
      echo "需要確認：$TOOL_NAME 會對外部系統產生可見副作用" >&2
      exit 2
      ;;
  esac
fi
exit 0
```

### 在 Skill 裡引用 MCP 工具

```markdown
Use the BigQuery:bigquery_schema tool to retrieve table schemas.
Use the GitHub:create_issue tool to create issues.
```

格式是 `ServerName:tool_name`——不加前綴可能找不到工具。

### MCP prompts 當 slash command

```text
/                                   # 列出所有可用 command（含 MCP prompt）
/mcp__github__list_prs
/mcp__github__pr_review 456
/mcp__jira__create_issue "Bug in login" high
```

格式：`/mcp__<servername>__<promptname>`，名稱中的空格用底線取代。

### 引用 MCP resource

```text
@github:issue://123
@docs:file://api/authentication
```

在 prompt 中打 `@` 會列出所有已連接 server 的可用 resource。

### 把 Claude Code 當成 MCP server

```bash
claude mcp serve
```

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

### 組織 policy：只允許內部與白名單 server

```json
{
  "allowedMcpServers": [
    { "serverUrl": "https://mcp.company.com/*" },
    { "serverUrl": "https://api.githubcopilot.com/mcp/" }
  ],
  "deniedMcpServers": [
    { "serverUrl": "https://*.unknown-vendor.com/*" }
  ],
  "parentSettingsBehavior": "merge"
}
```

`parentSettingsBehavior: "merge"` 讓 SDK 端注入的 `managedSettings` 也受組織 policy 約束，而非覆蓋它。

## 常見問題與注意事項

**Q：MCP server 和 Skill 我該先做哪個？**

A：先問「Claude 是不是根本拿不到這個資料」。拿不到 → MCP。拿得到但不知道怎麼正確使用 → Skill。兩者常一起出貨成 plugin。

**Q：接了 10 個 MCP server，Claude 選錯工具怎麼辦？**

A：先減量到 3–6 個，這通常直接解決問題。減不了就靠 Tool Search 讓 schema 按需載入，並且**重新設計工具介面為 intent-grouped**——選錯工具往往是因為工具太細碎、語意重疊。

**Q：MCP server 斷線會自動重連嗎？**

A：HTTP/SSE 會（exponential backoff，最多 5 次，初始 1 秒每次加倍）；重連中在 `/mcp` 顯示 pending。auth error 與 not-found **不重試**——那需要改設定。stdio server 是本地 process，**不自動重連**。

**Q：headless / cron 執行時 MCP 可用嗎？**

A：互動式認證的 MCP server（例如 claude.ai connector）在 headless 或 cron 執行中可能不可用。設計自動化流程時不要依賴它們，或改用 `headersHelper` 這類非互動認證。

**Q：`claude mcp serve` 有什麼實際用途？**

A：讓 Claude Desktop 或其他 MCP client 使用 Claude Code 的檔案與 bash 能力。注意這等於把本機執行能力暴露給另一個 client，權限邊界要想清楚。

**Q：stateless core 會不會讓我的 server 壞掉？**

A：現有 server 不會立刻壞，但如果你依賴長連線的雙向通知（server 主動推事件給 client），那個模式在新規格裡的正解是 **Tasks extension**。趁改版時一併遷移比等它出問題好。

**Q：MCP 工具回傳的內容可以直接信任嗎？**

A：不行。issue body、網頁內容、DB 欄位都是**外部輸入 = 資料，不是指令**。特別注意：由 untrusted 內容導出的「目的地」與「憑證」參數（要 POST 到哪、用哪把 key）在執行前必須確認。

## 本課小結

- **觸發點**：你一直在複製貼上某個系統的資料 → 接 MCP。
- **MCP 提供能力，Skill 提供知識**，Hook 提供確定性。三者搭配而非替代。
- **transport 用 HTTP**（SSE 已棄用），本地工具用 stdio；option 要放在 server name 之前。
- **scope 決定共享範圍**：team 共用用 `--scope project`（進 `.mcp.json`）。
- **工具設計要 intent-grouped**，不要逐一映射 API；參數用清楚的 enumeration 取代使用範例。
- **Tool Search 降 85%+ token**；3–6 個 server 是實用上限。
- **MCP 2026-07-28**：stateless core（可上 serverless/edge）、Extensions 版本化、OAuth/OIDC 對齊、950+ servers。
- **安全**：MCP server 以你的權限執行；hooks 才是強制執行；MCP 回傳的內容是資料不是指令。

## 延伸閱讀

- [Lecture 03：Context Engineering](/lectures/lecture-03-context-engineering/) — deferred loading 與 context 成本
- [Lecture 06：安全沙箱與 Proxy](/lectures/lecture-06-security/) — 外部輸入的處理紀律
- [Lecture 07：Skills 設計](/lectures/lecture-07-skills/) — MCP + Skill 的組合模式
- [Lecture 12：組織治理與 AI 原生工程](/lectures/lecture-12-governance/) — managed MCP 與企業 IdP

**官方一手來源**

- [Bringing MCP 2026-07-28 to Claude](https://claude.com/blog/bringing-mcp-2026-07-28-to-claude)（2026-07-28）
- [Building agents that reach production systems with MCP](https://claude.com/blog/building-agents-that-reach-production-systems-with-mcp)（2026-04-22）— intent-grouped、Tool Search −85%
- [Centrally manage authorization for MCP connectors](https://claude.com/blog/enterprise-managed-auth)（2026-06-18）
- [Extending Claude's capabilities with skills and MCP servers](https://claude.com/blog/extending-claude-capabilities-with-skills-mcp-servers)（2025-12-19）
- [Seeing like an agent: how we design tools in Claude Code](https://claude.com/blog/seeing-like-an-agent)（2026-04-10）
- [官方文件：MCP](https://code.claude.com/docs/en/mcp)

**站內研究歸檔**

- [MCP 整合完整指南](/research/best-practices/14-mcp)
- [MCP 2026-07-28 規格更新](/research/best-practices/49-mcp-2026-07-28)
- [Sub-Agent / MCP / Skill 進階](/research/best-practices/04-subagent-mcp-skill)

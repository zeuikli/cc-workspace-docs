---
title: Claude Code 官方 Hooks / Memory / Settings 最佳實踐
source: code.claude.com 官方文件
type: best-practices
---

# Claude Code 官方 Hooks / Memory / Settings 最佳實踐

> 來源：code.claude.com 官方文件（2026-04-25 抓取）
> 涵蓋：Hooks 架構、CLAUDE.md & Auto Memory、Settings 設定層級

---

## Hooks 最佳實踐

### 三層架構

```
Hook Event → Matcher Group → Handler
```

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "if": "Bash(rm *)",
            "command": "./.claude/hooks/block-rm.sh",
            "timeout": 10
          }
        ]
      }
    ]
  }
}
```

### 四種 Handler 類型

| 類型 | 說明 | 適用情境 |
|------|------|---------|
| `command` | 本地 bash 腳本 | 最常用；格式驗證、安全檢查 |
| `http` | 遠端驗證（含 `allowedEnvVars` 白名單）| 企業審批系統、外部 webhook |
| `mcp_tool` | 複用現有 MCP tool | 避免重複實作 |
| `prompt` | LLM 決策 | 需要主觀判斷的情境 |

### Exit Code 規約

| Exit Code | 效果 |
|-----------|------|
| `0` | 成功，繼續執行 |
| `1` | 警告，繼續執行（輸出顯示給使用者）|
| `2` | **阻斷**，停止工具執行 + 回饋錯誤訊息給 Claude |

### 關鍵設計模式

- **Matcher 優先**：先用 matcher 過濾（`Bash`、`Edit|Write`），再用 `if` 縮小範圍
- **Async for fire-and-forget**：通知、日誌等非關鍵任務加 `"async": true`，不卡 Claude
- **JSON 作決策**：PreToolUse 輸出結構化決策（allow/deny/ask/defer）

### Hook 生命週期

```
SessionStart
  → [UserPromptSubmit → PreToolUse → PostToolUse]*
  → Stop
  → SessionEnd
```

---

## CLAUDE.md & Auto Memory 最佳實踐

### CLAUDE.md 設定策略

- **長度目標**：≤200 行（超過用 `.claude/rules/` 拆分）
- **作用域優先級**：managed policy > 專案 CLAUDE.md > 用戶 `~/.claude/CLAUDE.md` > 本機 CLAUDE.local.md
- **import 語法**：`@path/to/file` 可引入外部規則檔

### Path-Scoped Rules（`.claude/rules/` frontmatter）

```markdown
---
paths:
  - "src/api/**/*.ts"
---

# API Development Rules
- All API endpoints must include input validation
- Use kebab-case for URL paths
```

### Auto Memory 運作機制

- 存放位置：`~/.claude/projects/<project>/memory/MEMORY.md`
- 每次 session 自動載入前 200 行或 25KB
- Claude 自動決定什麼值得記住（build 命令、除錯模式、偏好設定）
- 無需手動管理，純 Markdown 可隨時編輯（`/memory` 查看）
- `/clear` 與 `/compact` **不影響** Auto Memory

### CLAUDE.md 載入順序

1. 沿著目錄樹向上查找（CWD → 祖目錄）
2. 同層級：CLAUDE.md + CLAUDE.local.md 同時載入
3. 子目錄的 CLAUDE.md 按需載入（讀該目錄檔案時才載入）

---

## Settings 最佳實踐

### 完整設定層級（由高至低優先）

1. Managed settings（組織策略，不可覆蓋）
2. CLI 參數（`--model`, `--permission` 等）
3. Local settings（`.claude/settings.local.json`）
4. Project settings（`.claude/settings.json`）
5. User settings（`~/.claude/settings.json`）

### 核心設定範例

```json
{
  "$schema": "https://json.schemastore.org/claude-code-settings.json",
  "model": "claude-sonnet-4-6",
  "effortLevel": "xhigh",
  "permissions": {
    "allow": ["Bash(npm run *)", "Read(./src/**)"],
    "deny": ["Bash(rm -rf *)", "Read(./.env*)"],
    "ask": ["Bash(git push *)"]
  },
  "env": { "CUSTOM_VAR": "value" },
  "defaultShell": "bash",
  "autoMemoryEnabled": true,
  "attribution": {
    "commit": "🤖 Generated with Claude Code"
  }
}
```

### Sandbox 設定（Enterprise）

```json
{
  "sandbox": {
    "enabled": true,
    "filesystem": {
      "allowWrite": ["/tmp/build"],
      "denyRead": ["~/.aws/credentials"]
    },
    "network": {
      "allowedDomains": ["github.com", "*.npmjs.org"]
    }
  }
}
```

### Permission 模式

- `allow`：自動允許，無需確認
- `deny`：自動拒絕
- `ask`：每次詢問使用者

支援工具 + 命令模式：`Bash(npm run *)` 、`Read(./src/**)`

### 驗證設定

執行 `/status` 查看啟用的設定源及優先級

---

## Workspace 整合對照表

| 官方最佳實踐 | 本 Workspace 實現 |
|---|---|
| Hooks PreToolUse + command validation | `.claude/settings.json` hooks 設定 |
| Path-scoped rules | `.claude/rules/` 按觸發詞組織 |
| Auto Memory 存儲 | `~/.claude/projects/cc-workspace/memory/` |
| Managed CLAUDE.md 部署 | `/etc/claude-code/CLAUDE.md` 全組織 |
| Async hooks | notification 用途（Slack/Teams webhook）|

---

## 參考來源

- https://code.claude.com/docs/en/hooks
- https://code.claude.com/docs/en/memory
- https://code.claude.com/docs/en/settings

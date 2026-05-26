# Hooks 設計模式

Claude Code 支援 **25 種 hook 事件**，提供確定性的行為控制——不同於 CLAUDE.md 的建議性規則，hooks 是強制執行的。

## 25 種 Hook 事件分類

### Session 生命週期（3 種）

| 事件 | 觸發時機 |
|------|---------|
| `SessionStart` | 啟動或恢復 session 時 |
| `SessionEnd` | session 結束時 |
| `InstructionsLoaded` | CLAUDE.md / rules 載入後 |

### 每輪工作流（4 種）

| 事件 | 觸發時機 |
|------|---------|
| `UserPromptSubmit` | 使用者送出 prompt 前 |
| `Stop` | Claude 回應完成 |
| `StopFailure` | 輪次因 API 錯誤結束 |
| `Notification` | Claude Code 發出通知 |

### 工具執行 — Agentic Loop（5 種）

| 事件 | 觸發時機 |
|------|---------|
| `PreToolUse` | 工具執行**前**（可阻斷）|
| `PostToolUse` | 工具成功**後** |
| `PostToolUseFailure` | 工具失敗後 |
| `PermissionRequest` | 出現 permission dialog |
| `PermissionDenied` | auto mode 拒絕工具呼叫 |

### Subagent & 任務管理（6 種）

| 事件 | 觸發時機 |
|------|---------|
| `SubagentStart` / `SubagentStop` | Subagent 啟動/結束 |
| `TeammateIdle` | Agent team 成員閒置 |
| `TaskCreated` / `TaskCompleted` | Task 建立/完成 |
| `PreCompact` / `PostCompact` | Context 壓縮前後 |

### 檔案與設定（7 種）

`FileChanged`、`CwdChanged`、`ConfigChange`、`WorktreeCreate`、`WorktreeRemove`、`MCP Elicitation`、`ElicitationResult`

---

## Exit Code 規約

| Exit Code | 效果 |
|-----------|------|
| `0` | 成功，繼續執行 |
| `1` | 警告，繼續執行（輸出顯示給使用者）|
| `2` | **阻斷**，停止工具執行 + 回饋錯誤訊息給 Claude |

---

## PreToolUse Hooks — 執行前防守

### 阻斷危險命令

```bash
#!/bin/bash
set -euo pipefail

INPUT=$(cat)
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command')
BLOCKED=("rm -rf /" "DROP TABLE" "DROP DATABASE" "terraform destroy")

for b in "${BLOCKED[@]}"; do
  if echo "$COMMAND" | grep -qi "$b"; then
    echo "Blocked: dangerous command '$b' detected" >&2
    exit 2
  fi
done
exit 0
```

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "bash",
        "hooks": [{ "type": "command", "command": "/path/to/block-dangerous.sh" }]
      }
    ]
  }
}
```

### 阻止讀取 .env 檔

```bash
#!/bin/bash
INPUT=$(cat)
FILE=$(echo "$INPUT" | jq -r '.tool_input.file_path // ""')

if echo "$FILE" | grep -q '\.env'; then
  echo "Blocked: reading .env files is not allowed" >&2
  exit 2
fi
exit 0
```

### Git Push 前確認（警告不阻斷）

```bash
#!/bin/bash
INPUT=$(cat)
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // ""')

if echo "$COMMAND" | grep -q 'git push'; then
  echo "Warning: about to push to remote" >&1
  exit 1  # 警告但不阻斷
fi
exit 0
```

---

## PostToolUse Hooks — 執行後自動化

### 自動格式化（Prettier）

```bash
#!/bin/bash
FILE=$(jq -r '.tool_input.file_path // ""')
if [ -n "$FILE" ] && [[ "$FILE" =~ \.(js|ts|jsx|tsx)$ ]]; then
  npx prettier --write "$FILE"
fi
```

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [{ "type": "command", "command": "/path/to/prettier-hook.sh" }]
      }
    ]
  }
}
```

### Shell Script 語法驗證

```bash
#!/bin/bash
FILE=$(jq -r '.tool_input.file_path // ""')
if [[ "$FILE" =~ \.sh$ ]]; then
  if ! bash -n "$FILE" 2>&1; then
    echo "Shell syntax error in $FILE" >&2
    exit 2
  fi
fi
exit 0
```

### JSON 語法驗證

```bash
#!/bin/bash
FILE=$(jq -r '.tool_input.file_path // ""')
if [[ "$FILE" =~ \.json$ ]]; then
  if ! jq empty "$FILE" 2>&1; then
    echo "Invalid JSON in $FILE" >&2
    exit 2
  fi
fi
exit 0
```

### 命令日誌記錄

```bash
#!/bin/bash
INPUT=$(cat)
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // "N/A"')
echo "$(date '+%Y-%m-%d %H:%M:%S') | $COMMAND" >> ~/claude-commands.log
exit 0
```

---

## SessionStart Hooks — 環境初始化

### 自動拉取最新 CLAUDE.md

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "git -C ~/.claude pull origin main 2>/dev/null || echo 'Update skipped'"
          }
        ]
      }
    ]
  }
}
```

### 注入 Git Branch 信息

```bash
#!/bin/bash
BRANCH=$(git branch --show-current 2>/dev/null || echo "N/A")
echo "Current branch: $BRANCH"
echo "Last commit: $(git log --oneline -1 2>/dev/null || echo 'N/A')"
exit 0
```

---

## Stop Hooks — 任務完成通知

### 跨平台音效通知

```json
{
  "hooks": {
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "afplay /System/Library/Sounds/Glass.aiff 2>/dev/null || paplay /usr/share/sounds/freedesktop/stereo/complete.oga 2>/dev/null || printf '\\a'",
            "async": true
          }
        ]
      }
    ]
  }
}
```

### Slack Webhook 通知

```bash
#!/bin/bash
WEBHOOK_URL="${SLACK_WEBHOOK_URL:-}"
if [ -n "$WEBHOOK_URL" ]; then
  curl -s -X POST "$WEBHOOK_URL" \
    -H 'Content-type: application/json' \
    -d '{"text":"Claude Code task completed"}' || true
fi
exit 0
```

---

## UserPromptSubmit Hooks — 注入上下文

### 注入 Sub Agent 委派提醒

```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "echo '提醒：研究/實作/測試任務優先委派 Sub Agent。Commit 前跑 /deep-review。'"
          }
        ]
      }
    ]
  }
}
```

---

## 完整 .claude/settings.json 範本

```json
{
  "$schema": "https://json.schemastore.org/claude-code-settings.json",
  "model": "claude-sonnet-4-6",
  "effortLevel": "xhigh",
  "autoMemoryEnabled": true,
  "permissions": {
    "allow": [
      "Bash(git *)",
      "Bash(npm run *)",
      "Read(**)"
    ],
    "deny": [
      "Bash(rm -rf *)",
      "Read(.env*)"
    ],
    "ask": [
      "Bash(git push *)"
    ]
  },
  "hooks": {
    "SessionStart": [
      {
        "matcher": "",
        "hooks": [{ "type": "command", "command": "echo 'Session started: $(date)'", "async": true }]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "bash",
        "hooks": [{ "type": "command", "command": "~/.claude/hooks/block-dangerous.sh" }]
      },
      {
        "matcher": "Read",
        "hooks": [{ "type": "command", "command": "~/.claude/hooks/block-env-read.sh" }]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [{ "type": "command", "command": "~/.claude/hooks/validate-syntax.sh" }]
      }
    ],
    "Stop": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "afplay /System/Library/Sounds/Glass.aiff 2>/dev/null || printf '\\a'",
            "async": true
          }
        ]
      }
    ]
  }
}
```

---

## Hooks 最佳實踐

- **PreToolUse 用於防守**：阻斷危險操作（rm -rf、DROP、.env 讀取）
- **PostToolUse 用於自動化**：格式化、語法驗證、日誌
- **Exit code 規約明確**：0=成功、1=警告、2=阻斷
- **使用 jq 解析 stdin**：`jq -r '.tool_input.command // ""'`
- **matcher 精確化**：`Edit|Write` / `bash` 防止過度觸發
- **非阻斷操作加 async flag**：長時間任務不卡 Claude
- **Notification 跨平台**：macOS/Linux/Windows 兼容
- **SessionStart 注入 context**：git pull、環境變數、分支資訊
- **腳本加 `set -euo pipefail`**：防止靜默失敗

> **重要限制**：Hook 決策不 bypass permission 規則。Hook 返回 `allow` 仍受 deny/ask 規則約束；hook exit code 2 封鎖工具，即使 allow 規則存在也阻斷。

---

## 延伸閱讀

- [官方 Hooks 文件](https://code.claude.com/docs/en/hooks)
- [Permission 設定](/resources/best-practices/permissions)
- [Lecture 04：Harness 三層架構](/lectures/lecture-04-harness-architecture/)

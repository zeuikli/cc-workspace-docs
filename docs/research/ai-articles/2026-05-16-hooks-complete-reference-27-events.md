---
title: "Claude Code Hooks: The Complete 2026 Production Reference"
author: "The Prompt Shelf"
date: "2026-05-16"
source: "https://thepromptshelf.dev/blog/claude-code-hooks-complete-reference-2026/"
tags: "[claude-code, hooks, security, automation, exit-codes, lifecycle, MCP]"
topic: hooks
---

# Claude Code Hooks: The Complete 2026 Production Reference

Claude Code hooks 在 32+ lifecycle event 攔截點注入自訂邏輯，可用於封鎖指令、記錄工具呼叫、強制執行政策、觸發通知。本文是針對 v2.1.141+ 的完整生產參考，驗證於 Anthropic 2026 年 5 月文件。

## 27 個 Hook Events 分類

**Session-Level（3）**：SessionStart、Setup、SessionEnd

**Turn-Level（5）**：UserPromptSubmit、UserPromptExpansion、Stop、StopFailure

**Agentic Loop（7）**：PreToolUse、PostToolUse、PostToolUseFailure、PostToolBatch、PermissionRequest、PermissionDenied

**Agent/Team（5）**：SubagentStart、SubagentStop、TeammateIdle、TaskCreated、TaskCompleted

**File & Environment（6）**：InstructionsLoaded、ConfigChange、CwdChanged、FileChanged、WorktreeCreate、WorktreeRemove

**Context & Notification（6）**：PreCompact、PostCompact、Notification、Elicitation、ElicitationResult

## 五種 Handler 類型

1. **Command** — 執行 shell script，通過 stdin/stdout JSON 通訊
2. **HTTP** — POST 到 webhook（non-2xx 時非阻塞）
3. **MCP Tool** — 委派給 MCP server tools
4. **Prompt** — 使用指定模型的單輪 Claude 決策
5. **Agent** — 產生 sub-agent 進行多步驟推理

## Exit Code 語義（最關鍵的 gotcha）

> 「只有 exit code 2 會阻塞動作。Exit code 1 是非阻塞的——儘管違反 Unix 慣例，動作仍會繼續。」

| Exit Code | 行為 |
|-----------|------|
| **0** | 成功；解析 stdout JSON |
| **2** | 阻塞錯誤；停止可阻塞的動作 |
| **其他（含 1）** | 非阻塞；繼續執行 |

**用 `exit 1` 強制執行政策是最常見的實作錯誤**，危險動作會繼續執行而無警示。

## 決策輸出結構差異

- 大多數 event：頂層 `decision` 欄位
- `PreToolUse`：需要巢狀 `hookSpecificOutput.permissionDecision`
- `PermissionRequest`：使用 `hookSpecificOutput.decision`

Schema 不符會導致阻塞靜默失效。

## Matcher Pattern

```
# 工具名稱精確匹配
Bash
Edit|Write          # 正則 OR

# 前綴匹配
^Notebook

# MCP wildcard
mcp__server__tool__*
mcp__<server>__.*   # 整個 server 的所有工具
```

## 配置結構（三層）

```
event → matcher group → handler type
```

設定檔位置：
- `~/.claude/settings.json`（個人）
- `.claude/settings.json`（專案）
- 組織管理政策（不受 `disableAllHooks` 影響）

## 環境變數

| 變數 | 用途 |
|------|------|
| `$CLAUDE_EFFORT` | 當前 effort 等級 |
| `$CLAUDE_ENV_FILE` | 跨 hook 持久化環境變數 |
| `${CLAUDE_PROJECT_DIR}` | 專案根目錄路徑 |

## 常見生產 Pattern

- 封鎖危險 Bash 指令（`rm -rf`、force push）
- 檔案編輯後自動格式化
- 寫入前 secret 偵測
- Webhook 通知（Telegram、Slack）
- Cost/usage TSV 記錄（PostToolBatch）
- Git branch 保護（封鎖 main push）

## Key Insights
- 27 個獨立 hook events（32+ 含 subtype）：Session-Level、Turn-Level、Agentic Loop、Agent/Team、File & Environment、Context & Notification
- 關鍵 gotcha：exit 1 是非阻塞的（Unix 慣例），exit 2 才是阻塞——混用會靜默破壞政策強制執行
- `$CLAUDE_ENV_FILE` 用於跨 hook 持久化環境變數；`mcp__<server>__.*` wildcard 過濾整個 MCP server；PostToolBatch 可做 TSV 成本記錄

## Code Examples / Commands

```json
// .claude/settings.json hook 配置範例
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/block-dangerous-bash.sh"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/auto-format.sh"
          }
        ]
      }
    ]
  }
}
```

```bash
# block-dangerous-bash.sh 範例
#!/bin/bash
INPUT=$(cat)
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command // ""')

if echo "$COMMAND" | grep -qE 'rm -rf|git push --force|drop table'; then
  echo '{"decision": "block", "reason": "Dangerous command blocked"}' 
  exit 2  # 必須用 exit 2，不是 exit 1！
fi

exit 0
```

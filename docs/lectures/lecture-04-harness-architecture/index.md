# Lecture 04：Harness 三層架構

## 學習目標

完成本課後，你將能夠：

- 設計 Planner / Generator / Evaluator 三層 Harness 架構
- 解釋為什麼 Generator 不能自我評估
- 設定 Claude Code 的 25 種 Hooks 事件
- 使用 PreToolUse Hook 攔截危險指令

## 核心概念

### Planner / Generator / Evaluator：三層分離架構

來自 Anthropic engineering blog《Harness Design for Long-Running Apps》：

```
User Brief
  │
  ▼
PLANNER AGENT
  └─ 轉成細粒度 spec（防止 scope 爆炸）
  │
  ▼
GENERATOR AGENT
  └─ 逐項實作
  └─ 遇到 context limit → 完整 reset（不靠摘要）
  │
  ▼
EVALUATOR AGENT
  └─ Playwright / 外部工具（非模型自評）
  └─ Hard threshold：任一失敗 → sprint 失敗
  │
  ▼
(Feedback Loop)
```

每一層的職責嚴格分離：

| 層 | 職責 | 輸入 | 輸出 |
|----|------|------|------|
| **Planner** | 任務分解、spec 生成 | 用戶需求（可能模糊）| 細粒度可執行 spec |
| **Generator** | 實作 | spec 的一個 item | 程式碼變更 |
| **Evaluator** | 驗證 | 程式碼變更 | 通過/失敗 + 錯誤細節 |

### 為什麼 Generator 不能自評

這是三層架構最重要的設計原則，有量化依據支撐：

**Anthropic 的觀察**：Generator 「自信地稱讚自己的工作，即使品質明顯平庸」。

Self-evaluation 的結構性問題：
1. Generator 在生成過程中已經形成了一個「這樣是對的」的 prior
2. 讓它評估自己的輸出，等於用同一個 prior 驗證同一個輸出——feedback loop 封閉了
3. 這和讓學生自己批改自己的考卷是同一個問題

**Rajasekaran 案例的量化對比**：
- 單層（同一 agent 自評）：20 分鐘，$9，遊戲跑不起來
- 三層（planner + generator + evaluator）：6 小時，$200，遊戲可以正常遊玩

Evaluator 必須與 Generator 分離，且 Evaluator 應該使用**外部工具**（Playwright、pytest、mypy）而非模型自身判斷。

Eugene Yan 的原則：Evals pattern 是生產系統的基石——**評估的可信度取決於評估者與被評估者的獨立性**。

### Generator 的 Context Reset 策略

長任務中，Generator 遇到 context limit 時應該：

1. **完整 reset**（不靠摘要）：停下，新開一個 session，從 spec 的當前 item 重新開始
2. **不用 compaction**：因為 compaction 有損，可能丟失關鍵細節

這是 Anthropic 官方推薦的做法。之所以可行，是因為 Planner 已經把任務分解成了細粒度的 spec items，每個 item 都是可以在乾淨 context 中獨立執行的單元。

### Hooks 系統：25 種事件的防禦層

Claude Code 支援 **25 種 hook 事件**，分為五類：

#### Session 生命週期（3 種）

| 事件 | 觸發時機 |
|------|---------|
| `SessionStart` | 啟動或恢復 session 時 |
| `SessionEnd` | session 結束時 |
| `InstructionsLoaded` | CLAUDE.md / rules 載入後 |

#### 每輪工作流（4 種）

| 事件 | 觸發時機 |
|------|---------|
| `UserPromptSubmit` | 使用者送出 prompt 前 |
| `Stop` | Claude 回應完成 |
| `StopFailure` | 輪次因 API 錯誤結束 |
| `Notification` | Claude Code 發出通知 |

#### 工具執行 — Agentic Loop（5 種）

| 事件 | 觸發時機 |
|------|---------|
| `PreToolUse` | 工具執行**前**（可阻斷）|
| `PostToolUse` | 工具成功**後** |
| `PostToolUseFailure` | 工具失敗後 |
| `PermissionRequest` | 出現 permission dialog |
| `PermissionDenied` | auto mode 拒絕工具呼叫 |

#### Subagent & 任務管理（6 種）

| 事件 | 觸發時機 |
|------|---------|
| `SubagentStart` / `SubagentStop` | Subagent 啟動/結束 |
| `TeammateIdle` | Agent team 成員閒置 |
| `TaskCreated` / `TaskCompleted` | Task 建立/完成 |
| `PreCompact` / `PostCompact` | Context 壓縮前後 |

#### 檔案與設定（7 種）

`FileChanged`、`CwdChanged`、`ConfigChange`、`WorktreeCreate`、`WorktreeRemove`、`MCP Elicitation`、`ElicitationResult`

### Exit Code 規約（Hooks 行為控制）

| Exit Code | 效果 |
|-----------|------|
| `0` | 成功，繼續執行 |
| `1` | 警告，繼續執行（輸出顯示給使用者）|
| `2` | **阻斷**，停止工具執行 + 回饋錯誤訊息給 Claude |

### Hooks 設定位置

Hooks 設定在 `.claude/settings.json`（project level）或 `~/.claude/settings.json`（user level）：

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "bash",
        "hooks": [
          {
            "type": "command",
            "command": "/path/to/your-hook-script.sh"
          }
        ]
      }
    ]
  }
}
```

## 程式碼範例

### PreToolUse Hook：阻斷危險指令

```bash
#!/bin/bash
# /home/user/.claude/hooks/block-dangerous.sh
set -euo pipefail

INPUT=$(cat)
COMMAND=$(echo "$INPUT" | jq -r '.tool_input.command')
BLOCKED=("rm -rf /" "DROP TABLE" "DROP DATABASE" "terraform destroy" "git push --force")

for b in "${BLOCKED[@]}"; do
  if echo "$COMMAND" | grep -qi "$b"; then
    echo "Blocked: dangerous command '$b' detected" >&2
    exit 2  # exit 2 = 阻斷執行
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
        "hooks": [
          {
            "type": "command",
            "command": "/home/user/.claude/hooks/block-dangerous.sh"
          }
        ]
      }
    ]
  }
}
```

### PreToolUse Hook：阻止讀取 .env 檔案

```bash
#!/bin/bash
# 阻止 Claude 讀取包含敏感資料的 .env 檔案
set -euo pipefail

INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | jq -r '.tool_name')
FILE_PATH=$(echo "$INPUT" | jq -r '.tool_input.path // empty')

if [[ "$TOOL_NAME" == "read_file" ]] && [[ "$FILE_PATH" =~ \.env$ ]]; then
  echo "Blocked: reading .env files is not allowed" >&2
  exit 2
fi
exit 0
```

### SessionStart Hook：自動環境初始化

```bash
#!/bin/bash
# 每次 session 開始時自動執行環境檢查
set -euo pipefail

# 確認 node_modules 存在
if [ ! -d "node_modules" ]; then
  echo "Warning: node_modules not found, running npm install..."
  npm install
fi

# 確認 .env 存在
if [ ! -f ".env" ]; then
  echo "Warning: .env not found, copying from .env.example..."
  cp .env.example .env
fi

echo "Environment ready"
exit 0
```

```json
{
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "/path/to/session-init.sh"
          }
        ]
      }
    ]
  }
}
```

### Stop Hook：Session 結束時更新 MEMORY.md

```bash
#!/bin/bash
# 每次 Claude 完成回應後，提醒更新進度
# 注意：這個 hook 在每次 Claude 停止回應時都觸發（不只是 session 結束）
set -euo pipefail

INPUT=$(cat)
# 可以從 INPUT 中解析 session 資訊
echo "Claude response complete. Remember to update MEMORY.md if needed."
exit 0
```

### 完整的三層 Harness 配置示例

```json
{
  "hooks": {
    "SessionStart": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/session-init.sh"
          }
        ]
      }
    ],
    "PreToolUse": [
      {
        "matcher": "bash",
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/block-dangerous-commands.sh"
          }
        ]
      },
      {
        "matcher": "read_file",
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/block-sensitive-files.sh"
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "bash",
        "hooks": [
          {
            "type": "command",
            "command": "bash .claude/hooks/log-commands.sh"
          }
        ]
      }
    ]
  }
}
```

## 常見問題與注意事項

**Q：什麼時候應該用三層架構，什麼時候單層就夠了？**

A：
- **單層就夠**：30 分鐘內可完成的任務、任務邊界清晰、有完整測試套件
- **需要三層**：超過 1 小時的任務、需要多個 context window、任務分解複雜、高品質要求（不能接受偶發性錯誤）

一般原則：超過 30 分鐘的長任務就考慮引入三層架構。

**Q：Evaluator 一定要是獨立的 AI agent 嗎？**

A：不一定。Evaluator 可以是：
- 純工具鏈（pytest + mypy + playwright）— 最可靠
- 另一個 Claude agent（用不同的 session）— 有一定有效性
- 同一個 Claude session 但明確要求批判性評估 — 最不可靠

原則：Evaluator 的可信度取決於它與 Generator 的獨立性。

**Q：Hook 腳本失敗（非 0 exit code）對 Claude 有什麼影響？**

A：
- Exit 1：Claude 看到警告輸出，但繼續執行
- Exit 2：Claude **停止執行當前工具**，並將錯誤信息作為 context，可能嘗試用其他方式繼續

Exit 2 非常強力，應謹慎使用。只在真正需要阻斷的情況下用（如危險指令、敏感檔案讀取）。

**Q：可以在同一個事件上設定多個 hooks 嗎？**

A：可以。多個 hooks 按設定順序依次執行。任意一個返回 exit 2 都會阻斷執行。

**Q：Hook 腳本的 stdin 格式是什麼？**

A：Hook 通過 stdin 接收 JSON 格式的事件資料。`tool_name`、`tool_input` 是標準欄位。使用 `jq` 解析最方便。

```bash
INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | jq -r '.tool_name')
TOOL_INPUT=$(echo "$INPUT" | jq -r '.tool_input')
```

## 本課小結

- **三層分離是強制要求**：Planner（分解任務）→ Generator（實作）→ Evaluator（外部驗證）。Generator 不能自評。
- **量化支撐**：三層 vs 單層，同模型 6 小時可玩遊戲 vs 20 分鐘跑不起來。
- **Generator 遇到 context limit → 完整 reset**，不靠摘要，從 spec item 重新開始。
- **25 種 Hooks 事件**：PreToolUse（可阻斷）是最重要的防禦 hook。Exit 2 阻斷，Exit 1 警告，Exit 0 繼續。
- **Evaluator 用外部工具**（pytest、playwright）而非模型自評，獨立性是可信度的來源。

## 延伸閱讀

- [Lecture 03：Context Engineering](/lectures/lecture-03-context-engineering/) — Sub-agent 的 Context Firewall 原理
- [Lecture 06：安全沙箱與 Proxy](/lectures/lecture-06-security/) — Hooks 在安全層面的應用
- [Project 02：設計你的 Harness](/projects/project-02-harness-design/) — 動手實作三層架構
- [Anthropic: Harness design for long-running application development](https://www.anthropic.com/engineering/harness-design-long-running-apps)
- [官方文件：Claude Code Hooks](https://code.claude.com/docs/en/hooks)

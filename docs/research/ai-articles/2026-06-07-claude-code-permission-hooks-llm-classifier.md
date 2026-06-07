---
title: "AI-Powered Claude Code Permission Hooks"
author: "Dyad"
date: 2026-06-07
source: "https://www.dyad.sh/blog/claude-code-permission-hooks"
tags: [claude-code, hooks, permissions, llm-classifier, security]
topic: LLM 分類器做第二層 permission hook，GREEN/YELLOW/RED 三色分類
---

# AI-Powered Claude Code Permission Hooks

Dyad 設計了一套三層 defense 系統，使用規則式 + AI 分類器實作 Claude Code permission hook。系統在 `.claude/settings.json` 中定義三種 hook 類型：**PreToolUse**（攔截工具呼叫前）、**PermissionRequest**（fallback，當 permission dialog 即將出現時）、**Stop**（agent 完成任務時觸發）。

## 三層架構

**Layer 1：gh-permission-hook.py（規則式）**
- 確定性評估 GitHub CLI 指令
- Allow：讀取操作、PR workflow、安全 API call
- Deny：破壞性動作（`gh repo delete`、`gh release create`）
- Passthrough：未識別指令
- 攔截 shell injection metacharacter（`;`、`&&`、backtick、`$()`），豁免安全 pipe 至文字處理器
- 627 行 Python，含完整 regex pattern

**Layer 2：python-permission-hook.py（規則式）**
- 限制 Python 執行只能用 `.claude` 目錄下腳本與 `pytest`
- Deny：inline code（`-c`）、任意 module（`-m`）、interactive mode

**Layer 3：permission-request-hook.py（AI 驅動）**
- 規則式 hook 未匹配時，呼叫 Claude Sonnet + policy document 做最終分類
- 回傳三色分類：
  - **GREEN**：自動核准（不顯示 user dialog）
  - **YELLOW**：passthrough（顯示 user dialog）
  - **RED**：自動拒絕，錯誤訊息加 `[AI-RED]` 前綴

## Permission Policy DSL

使用 `permission-policy.md` 結構化 Markdown 定義三個領域：

- **Bash 指令**：GREEN = 讀取、文字處理、開發工具（npm/make/cargo）、git 操作；YELLOW = 套件管理、Docker；RED = 系統破壞、`.git` 操控、`curl | bash`、加密指令
- **GitHub 操作**：對應規則式分類的自然語言版
- **Edit/Write 操作**：原始碼 GREEN；shell scripts/CI YELLOW；系統檔/SSH keys RED

## 防遞迴循環的三重保護

1. Supervisor 以 `--print` mode 執行（無 tool 存取權）
2. `--no-session-persistence` 防止 session 累積
3. 環境變數 `DYAD_DISABLE_CLAUDE_CODE_HOOKS=true` kill switch

## 效能指標

- 規則式 hook：毫秒級執行
- AI fallback：最長 25 秒 timeout

## Key Insights
- **快確定，慢 AI**：設計哲學「快速確定性先行，AI 分類僅作兜底」——LLM 處理無限指令變體，而非做主要執法
- **三色分類優於二元**：GREEN/YELLOW/RED 比 allow/deny 更能細化處理「需要使用者判斷」的灰色地帶
- **防遞迴是必要設計**：AI hook 呼叫 LLM 時，若不加保護會引發無限循環，`--no-session-persistence` + env kill switch 是必要安全閥

## Code Examples / Commands

```json
// .claude/settings.json hook 設定範例
{
  "hooks": {
    "PreToolUse": ["python .claude/hooks/gh-permission-hook.py"],
    "PermissionRequest": ["python .claude/hooks/permission-request-hook.py"]
  }
}
```

```python
# AI hook 核心邏輯（permission-request-hook.py）
import subprocess, json, sys

def classify(request_json):
    policy = open("permission-policy.md").read()
    prompt = f"{policy}\n\nRequest: {json.dumps(request_json)}\nClassify as GREEN, YELLOW, or RED:"
    result = subprocess.run(
        ["claude", "--print", "--no-session-persistence"],
        input=prompt, capture_output=True, text=True,
        env={**os.environ, "DYAD_DISABLE_CLAUDE_CODE_HOOKS": "true"}
    )
    return result.stdout.strip()
```

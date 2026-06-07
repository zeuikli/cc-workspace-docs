---
title: "Claude Code HTTP Hooks × GitHub Actions CI/CD 整合指南"
author: "ClaudeLab"
date: 2026-06-07
source: "https://claudelab.net/en/articles/claude-code/claude-code-http-hooks-cicd-github-actions-guide"
tags: [claude-code, hooks, http-hooks, github-actions, cicd, self-healing, cloudflare-workers]
topic: HTTP hooks × GitHub Actions CI/CD，Block→Rewrite→Verify 自愈迴圈
---

# Claude Code HTTP Hooks × GitHub Actions CI/CD 整合指南

本文說明如何透過 HTTP Hooks 將 Claude Code AI agent 接入 CI/CD pipeline，實現自動 code review、測試失敗自修復、語意版本號決策。

## 核心架構

HTTP Hooks 將 JSON payload POST 到 webhook endpoint，讀取 response 決定 Claude 行為。

**三種主要 hook 類型：**
- **PreToolUse**：執行前攔截
- **PostToolUse**：執行後反應
- **Stop**：session 結束時觸發

**`decision` 欄位三選項：**
- `"proceed"`：繼續
- `"block"`：取消並注入原因到 Claude context
- `"approve"`：自動確認

## 三大生產模式

**Pattern 1 — 自動 Code Review**
PR 開啟/更新時，GitHub Actions 觸發 Claude Code，掃描變更檔案找 bug 與安全問題，結果自動發 PR comment。

**Pattern 2 — 測試失敗自修復**
CI 測試失敗時，Claude 分析 log 並直接在 PR 提出修正建議。

**Pattern 3 — 語意版本號**
Claude 讀取 commit history 與 file diff，自動判斷 patch/minor/major 版本升級。

## Block → Rewrite → Verify 自愈迴圈

工具呼叫被 `block` 後，reason text 注入 Claude 的 active context，Claude 讀取原因後自行決定如何處理——自主改寫程式碼直到品質檢查通過，無需人工介入。品質檢查項目：ESLint 驗證、TypeScript 型別檢查、安全 pattern 偵測、`console.log` 偵測、hardcoded secret 掃描。

## 安全層次

- Bearer Token 驗證 webhook endpoint
- HMAC SHA-256 簽名驗證
- GitHub Actions runner IP allowlist
- GitHub Actions Secrets 管理 env var
- settings.json 不 hardcode 憑證

## 可靠性設計

- Exponential backoff（處理 flaky downstream services）
- Idempotency cache（去重，5 分鐘 TTL）
- Webhook server 不可用時 graceful degradation
- Handler response 10 秒 default timeout

## 部署建議

**推薦：Cloudflare Workers**（每月 10 萬次免費請求，300+ edge locations，零 cold start）
**開發：ngrok**（local tunnel 測試用）

## Key Insights
- **Block 注入比 deny 更強**：`block` 會把 reason 注入 Claude context，讓 Claude 理解為何被阻擋並自行修正，形成真正的 self-healing loop，而非單純拒絕
- **CI/CD hook server 要做冪等**：同一事件可能重複觸發（GitHub Actions retry），5 分鐘 TTL dedup cache 是防止重複執行的關鍵
- **Edge deployment 優先**：Cloudflare Workers 的零 cold start 特性對 hook 的低延遲要求至關重要，傳統 serverless 的 cold start 可能導致 10 秒 timeout 失效

## Code Examples / Commands

```json
// .claude/settings.json — HTTP hook 設定
{
  "hooks": {
    "PreToolUse": [
      {
        "type": "http",
        "url": "https://hooks.example.com/pre-tool",
        "headers": {
          "Authorization": "Bearer ${CLAUDE_HOOK_SECRET}"
        },
        "timeout": 10000
      }
    ]
  }
}
```

```typescript
// Cloudflare Worker webhook handler (Hono)
import { Hono } from 'hono'

const app = new Hono()

app.post('/pre-tool', async (c) => {
  const payload = await c.req.json()
  const { tool_name, tool_input } = payload

  // 品質檢查
  if (tool_name === 'Write' && hasConsoleLog(tool_input.content)) {
    return c.json({
      decision: 'block',
      reason: 'Remove console.log statements before committing. Use a proper logger instead.'
    })
  }

  return c.json({ decision: 'proceed' })
})
```

```yaml
# GitHub Actions workflow — PR 觸發 Claude review
name: Claude Code Review
on:
  pull_request:
    types: [opened, synchronize]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Run Claude Code Review
        run: |
          claude -p "Review the changed files in this PR for bugs and security issues. Post findings as PR comments." \
            --allowedTools "Bash,Read,Grep" \
            --no-session-persistence
        env:
          ANTHROPIC_API_KEY: $
          CLAUDE_HOOK_SECRET: $
```

---
title: "Claude Code Routines：三類 trigger、雲端自動化、GitHub 8種 webhook 事件"
author: "claudeapi.com"
date: 2026-06-07
source: "https://www.claudeapi.com/en/blog/dev-guides/claude-code-routines-cloud-automation-2026/"
tags: [claude-code, routines, cloud-automation, github-webhook, scheduled-tasks, api-trigger]
topic: Routines 雲端自動化，三類 trigger，配額限制，GitHub webhook 8種事件
---

# Claude Code Routines：雲端自動化執行引擎

發佈日期：2026-05-28。Routines 是一種「儲存的 Claude Code 配置」，在 Anthropic 基礎設施上自動執行，無需本地機器或自管 cron jobs。每次執行均從 default branch 全新克隆 repository 開始。

## 三類 Trigger

| Trigger 類型 | 機制 | 使用場景 |
|------------|------|---------|
| **Scheduled** | 每小時/每日/工作日/每週 | 報告生成、夜間測試、摘要 |
| **API** | HTTP POST（bearer token 認證） | 外部系統、on-demand 觸發 |
| **GitHub** | Repository 事件 | PR review、CI 回應、Release 工作流 |

## 每日執行配額

| 方案 | 每日執行次數 |
|------|------------|
| Pro | 5 次 |
| Max | 15 次 |
| Team/Enterprise | 25 次 |

**重要**：互動式 session 與自動化執行共享同一配額池。高度使用互動式 Claude Code 的使用者需注意配額競爭。

## GitHub Webhook 支援的 8 種事件

1. Pull requests（PR 事件）
2. Pushes（推送）
3. Issues（Issue 事件）
4. Check runs（CI 檢查執行）
5. Workflow runs（工作流執行）
6. Discussions（討論）
7. Releases（發布）
8. Merge queue events（合併佇列事件）

進階過濾條件：作者、PR 標題、分支名稱、labels、draft 狀態、fork 來源。

## 安全設計

預設 Claude 只能推送到 `claude/` 前綴的分支，防止意外損壞主要分支。GitHub webhook 功能需先安裝 Claude GitHub App。

## API 整合範例

使用 Claude API 作為 Routine 觸發前的協調層，以 Haiku 模型進行低成本分類決策：

```python
import anthropic

client = anthropic.Anthropic()

def triage_alert(alert_data: dict) -> str:
    """使用 Haiku 分類 alert 嚴重程度，決定是否觸發 Routine"""
    response = client.messages.create(
        model="claude-haiku-4-5",
        max_tokens=100,
        messages=[{
            "role": "user",
            "content": f"Alert severity classification: {alert_data}"
        }]
    )
    return response.content[0].text

def trigger_routine(routine_id: str, payload: dict):
    """透過 API trigger 觸發特定 Routine"""
    import requests
    headers = {"Authorization": f"Bearer {ROUTINE_API_TOKEN}"}
    requests.post(
        f"https://api.claude.ai/routines/{routine_id}/trigger",
        json=payload,
        headers=headers
    )

# Alert triage 流程
alert = {"type": "cpu_spike", "value": 95, "service": "payment-api"}
severity = triage_alert(alert)
if "critical" in severity.lower():
    trigger_routine("incident-response-routine", alert)
```

## Key Insights
- 配額池共享（互動 + 自動化）是關鍵限制：Pro 用戶 5 次/天很快耗盡，高頻自動化需要 Team/Enterprise 方案
- 每次執行從 default branch 全新克隆的設計確保冪等性，但也意味著 Routine 不保留跨執行的工作狀態
- `claude/` 分支前綴限制是「最小許可權原則」的實踐，防止自動化程式破壞 main/master
- GitHub webhook 的 8 種事件覆蓋完整 DevOps 生命週期，可實現 PR 自動 review、release notes 自動生成等常見自動化

## Code Examples / Commands

```bash
# GitHub App 安裝（webhook 前提）
# 在 GitHub repository settings 安裝 Claude GitHub App

# Scheduled trigger 配置範例（每日）
# Routine 配置：
# trigger: daily
# time: "09:00 UTC"
# prompt: "Generate daily standup summary from yesterday's commits"

# API trigger
curl -X POST https://api.claude.ai/routines/{routine_id}/trigger \
  -H "Authorization: Bearer $ROUTINE_API_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"context": "Deploy completed for v2.3.1"}'
```

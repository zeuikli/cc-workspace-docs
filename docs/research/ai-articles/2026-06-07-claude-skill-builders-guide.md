---
title: "From Zero to Production-Ready Claude Skill: 步驟式建置指南"
author: "Mayur Panchal"
date: 2026-06-07
source: "https://medium.com/@mayurpanchal.x1/from-zero-to-production-ready-claude-skill-a-step-by-step-builders-guide-38487bf8e414"
tags: [claude-code, skills, skill-building, mcp, subagents, production, marketplace]
topic: "Skill 建置指南，SKILL.md description 'pushy' 策略，三種實作模式，production checklist"
---

# From Zero to Production-Ready Claude Skill

作者：Mayur Panchal，發布於 2026-05-09，約 8 分鐘閱讀。

## Skill 的核心概念

Claude Skill 是透過工作流程指引 Claude 行為的機制，採用**三階段資訊揭露模型**：

1. **Metadata**（元資料）：name + description，決定 Claude 是否觸發此 Skill
2. **SKILL.md body**：完整工作流程指令
3. **Bundled resources**：附帶的腳本、模板、資料

## Skill vs 相關工具的區別

| 工具 | 用途 |
|------|------|
| **Skills** | 透過工作流程 shaping Claude 行為 |
| **MCP servers** | 提供新的工具能力（tool capabilities） |
| **Subagents** | 啟用獨立平行處理 |

三者不互斥，Pattern C 就是組合使用。

## SKILL.md Description 的 'Pushy' 策略

Metadata（name/description）是最關鍵的設計決策——它決定 Claude 是否觸發 Skill。

**錯誤寫法**（模糊）：
```
description: "Analyze data files"
```

**正確寫法**（'pushy' 策略）：
```
description: "Analyze sales/revenue CSV and Excel files"
triggers: ["profit margins", "churn analysis", "revenue breakdown", "sales report"]
```

設計前應先回答：Who uses this? When? How will they phrase requests? What are inputs and outputs?

## 三種實作模式

**Pattern A（Prompt-Only）**：
- 純 Markdown 指令
- 適用：規範、格式化指引、簡單工作流程
- 無需外部依賴

**Pattern B（Prompt + Scripts）**：
- 指令 + Python/JavaScript 確定性處理
- 適用：資料轉換、驗證、文件生成
- Script 處理 deterministic 邏輯，Claude 處理語意判斷

**Pattern C（Integration）**：
- 協調 MCP servers 或 Subagents
- 適用：複雜外部工作流程
- 最高彈性，也最高複雜度

## 測試策略

有效測試使用**反映真實使用者行為**的 prompt，包含：
- 錯字（"analize" instead of "analyze"）
- 口語化語言（"can you check my csv thing"）
- 檔名不確定性（"the file from last week"）

避免使用「消毒後」的完美測試 prompt——它們無法反映真實觸發條件。

## 發布管道（四種）

1. **ZIP upload**：透過 claude.ai settings 上傳
2. **Repository**：放置於 `.claude/skills/` 目錄
3. **Plugin Marketplace**：開源分享
4. **Anthropic Official Marketplace**：更廣泛觸及

## Key Insights
- Description 的「pushy」策略是讓 Skill 被正確觸發的關鍵——含觸發關鍵字比模糊描述有效得多
- 三種模式對應三種使用場景：純規範 → Pattern A；含計算邏輯 → Pattern B；需外部整合 → Pattern C
- 三階段資訊揭露（metadata → body → resources）讓 token 消耗可控：先觸發，再載入完整指令
- 測試用真實口語 prompt（含錯字）比用乾淨 prompt 更能驗證觸發條件的健壯性

## Code Examples / Commands

```markdown
# SKILL.md 範例（Pattern B）
---
name: csv-revenue-analyzer
description: "Analyze sales/revenue CSV and Excel files. 
  Triggers on: profit margins, churn analysis, revenue breakdown, 
  sales report, financial data analysis"
version: 1.0.0
---

## Instructions
When analyzing revenue files:
1. Load the file using the bundled Python script
2. Identify columns: date, revenue, cost, customer_id
3. Calculate: MoM growth, churn rate, LTV
4. Generate insights in the format below

## Resources
- analyze.py: Core calculation logic
- report_template.md: Output format
```

```python
# Pattern B 附帶的 analyze.py
import pandas as pd
import sys

def analyze_revenue(filepath: str) -> dict:
    df = pd.read_csv(filepath)
    return {
        "mom_growth": df["revenue"].pct_change().mean(),
        "total_revenue": df["revenue"].sum(),
        "unique_customers": df["customer_id"].nunique()
    }

if __name__ == "__main__":
    result = analyze_revenue(sys.argv[1])
    print(result)
```

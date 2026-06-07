---
title: "Claude Code for Data Engineers: MCP Data Toolbox + OpenMetadata + Airflow + dbt"
author: "Alejandro Aboy"
date: 2026-06-07
source: "https://thepipeandtheline.substack.com/p/intro-claude-code-for-data-engineers"
tags: [claude-code, data-engineering, mcp, dbt, airflow, openmetadata, data-toolbox, hooks]
topic: Data Engineers 的 Claude Code，MCP Data Toolbox + OpenMetadata + Airflow，dbt agent skills
---

# Claude Code for Data Engineers

作者：Alejandro Aboy（The Pipe & The Line, Substack），發布於 2026-02-26。

本文以三種整合機制（MCP servers、Skills、Hooks）為框架，系統性地涵蓋現代資料堆疊的五大領域：Orchestration、Data Modeling、Databases、Quality Assurance、Documentation。

## MCP Data Toolbox（最廣泛的資料庫整合）

Google 的統一配置層，透過單一 `tools.yaml` 支援 **30+ 種資料庫**，提供：
- Schema discovery（結構探索）
- Query execution（查詢執行）
- Result caching（結果快取）

相較於為每個資料庫管理獨立 MCP，Data Toolbox 大幅降低配置複雜度。

## 資料建模（最成熟的整合領域）

**dbt Agent Skills** 提供 analytics engineering 的完整工作流程指令：
- 模型建置
- 單元測試
- CLI 指令執行
- 文件生成

**OpenMetadata MCP** 在 schema 變更前執行影響分析：
- 檢查下游依賴
- 確認資料所有權
- 避免破壞性變更

## Airflow 整合（Orchestration）

Airflow MCP 透過 REST API 連接，提供：
- DAG 探索
- Run 診斷
- 系統健康監控

相容 open-source Airflow 2.x 和 3.x。

## Hooks：Quality Gate 自動化

三種實際 Hook 配置：

| Hook 類型 | 觸發時機 | 用途 |
|-----------|---------|------|
| PreToolUse | Commit 前 | 執行 pytest，阻擋不合格代碼 |
| PostToolUse | 檔案儲存後 | 執行 sqlfluff 驗證 SQL |
| PostToolUse | 模型變更後 | 自動執行 dbt test |

## Visual Modeling（Miro MCP）

從業務需求 → 概念設計 → 實體 dbt 實作的完整鏈條，並結合 OpenMetadata 影響分析，形成端到端的可視化建模工作流。

## 作者建議

> "The only valid approach is the one that works for you."

不建議全部採用，而是**策略性組合 MCP**，根據實際資料堆疊選擇整合點。最成熟的起點：dbt Agent Skills + OpenMetadata MCP。

## Key Insights
- MCP Data Toolbox 的「30+ 資料庫單一 tools.yaml」解決了多 MCP 配置爆炸問題，是資料工程師最值得首先嘗試的整合
- OpenMetadata MCP 的 schema 變更前影響分析，將「資料治理」從事後修復轉為事前預防
- 三種 Hook（pytest/sqlfluff/dbt test）將品質檢查嵌入開發流程，而非依賴人工記得執行
- dbt Agent Skills 是「最成熟領域」的評語來自作者實測，其工作流程指令覆蓋 analytics engineering 的完整生命週期

## Code Examples / Commands

```yaml
# MCP Data Toolbox tools.yaml 配置範例
sources:
  - name: production_postgres
    type: postgresql
    connection: ${PROD_POSTGRES_URL}
  - name: analytics_bigquery
    type: bigquery
    project: my-analytics-project
  - name: data_warehouse
    type: snowflake
    account: ${SNOWFLAKE_ACCOUNT}
```

```bash
# dbt Agent Skill 典型工作流
# 1. 建置模型
dbt run --models staging.stg_orders

# 2. 執行單元測試
dbt test --models staging.stg_orders

# 3. 生成文件
dbt docs generate
```

```python
# Airflow MCP - DAG 診斷
# Claude Code 透過 Airflow REST API
GET /api/v1/dags/{dag_id}/runs
GET /api/v1/dags/{dag_id}/tasks
GET /api/v1/health
```

```bash
# .claude/settings.json Hook 配置
# sqlfluff on file save
{
  "hooks": {
    "PostToolUse": [{
      "matcher": ".*\\.sql$",
      "command": "sqlfluff lint $CLAUDE_TOOL_FILE"
    }]
  }
}
```

---
title: "57 個生產級 Claude Code Slash Commands：Workflows vs Tools 分類架構"
author: "wshobson"
date: 2026-06-07
source: "https://github.com/wshobson/commands"
tags: [claude-code, slash-commands, workflows, tools, multi-agent, context-management, production]
topic: 57 個生產級 slash commands，workflows vs tools 分類，context-save/restore
---

# 57 個生產級 Claude Code Slash Commands

一個提供 **57 個生產級 slash commands** 的 repository，包含 15 個 Workflows 和 42 個 Tools，透過多代理協作擴展 Claude Code 的自動化能力。

## 核心分類架構

### Workflows（15 個）：多代理協作的複雜任務

Workflows 實作多代理協調模式，分析需求、委派給專門代理、跨子系統協調執行。

**核心開發 Workflows**：

| 指令 | 用途 | 代理協調 |
|------|------|---------|
| `feature-development` | 端對端功能實作 | Backend、Frontend、Testing、Deployment |
| `full-review` | 多視角代碼分析 | Architecture、Security、Performance、Quality |
| `smart-fix` | 智慧問題解決 | 根據問題類型動態選擇代理 |
| `tdd-cycle` | TDD 協調 | Test writer、Implementer、Refactoring specialist |

**進階 Workflows**：`full-stack-feature`、`security-hardening`、`data-driven-feature`、`performance-optimization`、`incident-response` 等。

### Tools（42 個）：單一用途的精確工具

按領域分類：

| 類別 | 數量 | 代表指令 |
|------|------|---------|
| AI/ML | 4 | `ai-assistant`、`langchain-agent`、`prompt-optimize` |
| Agent 協作 | 3 | `multi-agent-review`、`smart-debug` |
| 架構/品質 | 4 | `code-explain`、`refactor-clean`、`tech-debt` |
| Data/DB | 3 | `data-pipeline`、`data-validation`、`db-migrate` |
| DevOps/Infrastructure | 5 | `docker-optimize`、`k8s-manifest`、`slo-implement` |
| 測試開發 | 6 | `api-scaffold`、`test-harness`、`tdd-red/green/refactor` |
| Security/Compliance | 3 | `security-scan`、`compliance-check`（GDPR/HIPAA/SOC2/PCI-DSS） |
| Context 管理 | 2 | **`context-save`、`context-restore`** |

## Context Save/Restore：跨 Session 狀態保留

`context-save` 和 `context-restore` 是跨多 session 專案的關鍵工具：

- **`context-save`**：保存架構決策、配置快照
- **`context-restore`**：重載 context、決策歷史、配置

適用於：Workflow 執行 30–90 秒、需要中斷再繼續的長期專案。

## Workflow vs Tool 決策矩陣

| 條件 | 使用 Workflows | 使用 Tools |
|------|--------------|-----------|
| 問題複雜度 | 跨域、橫切關注點 | 單一域、聚焦範圍 |
| 解法清晰度 | 探索性、未定義方法 | 明確的實作路徑 |
| 代理需求 | 需要多個專家協作 | 單一專業足夠 |
| 實作範圍 | 端對端功能 | 特定元件 |
| 控制層級 | 偏好自動化協調 | 需要手動控制 |

## 安裝方式

```bash
# Slash commands 方式
cd ~/.claude
git clone https://github.com/wshobson/commands.git

# Plugin Marketplace 方式（現代化）
/plugin marketplace add https://github.com/wshobson/agents
/plugin install claude-code-essentials
```

可用 collections：`claude-code-essentials`、`full-stack-development`、`security-hardening`、`data-ml-pipeline`、`infrastructure-devops`。

## Key Insights
- Workflows vs Tools 的二元分類是最核心的設計決策：Workflows 走多代理協調（30–90 秒），Tools 走單一精確執行（5–30 秒）
- `context-save`/`context-restore` 解決 Claude Code 多 session 狀態遺失問題，是長期專案的必備工具
- `smart-fix` 的「根據問題類型動態選擇代理」體現了 adaptive orchestration——問題先分類，再選對應專家
- Plugin Marketplace 版本（wshobson/agents）已是開發重心，slash commands 版本提供更直接的控制

## Code Examples / Commands

```bash
# Workflow 調用（多代理協調）
/workflows:feature-development OAuth2 authentication with JWT tokens
/workflows:smart-fix high memory consumption in production workers
/workflows:security-hardening implement zero-trust architecture

# Tool 調用（單一精確執行）
/tools:api-scaffold REST endpoints for user management with RBAC
/tools:k8s-manifest WebSocket service with session affinity
/tools:security-scan OWASP Top 10 vulnerability scan
/tools:compliance-check GDPR data handling requirements

# Context 管理
/tools:context-save                    # 儲存當前架構決策
/tools:context-restore                 # 下次 session 恢復狀態

# TDD 工作流（手動分段控制）
/tools:tdd-red create failing tests for order validation
/tools:tdd-green implement minimal order validation logic
/tools:tdd-refactor optimize validation performance

# 或一鍵完整 TDD
/workflows:tdd-cycle shopping cart with discount calculation logic

# 現代化安裝（Plugin Marketplace）
/plugin marketplace add https://github.com/wshobson/agents
/plugin install security-hardening
```

---
title: "Claude Code Spec Workflow: spec-driven 四代理分工與階層式 context 分發"
author: "Pimzino"
date: 2026-06-07
source: "https://github.com/Pimzino/claude-code-spec-workflow"
tags: [claude-code, spec-driven, multi-agent, workflow, context-optimization, steering-documents]
topic: spec-driven 四代理分工，hierarchical context distribution，三個 steering 文件
---

# Claude Code Spec Workflow: spec-driven 四代理分工

一個自動化的 spec-driven 開發工作流系統，將新功能開發拆解為 **Requirements → Design → Tasks → Implementation** 四階段，並透過 4 個專門化 AI agent 協作執行。同時提供 Bug Fix 工作流：**Report → Analyze → Fix → Verify**。

> 注意：開發重心已轉移至 MCP 版本（[spec-workflow-mcp](https://github.com/Pimzino/spec-workflow-mcp)），本 Claude Code 版本仍可用但更新有限。

## 四個專門化 Agent

| Agent | 職責 |
|-------|------|
| `spec-task-executor` | 執行具體實作任務 |
| `spec-requirements-validator` | 驗證需求完整性 |
| `spec-design-validator` | 驗證技術設計 |
| `spec-task-validator` | 驗證任務分解正確性 |

Agent 為選配——系統有 fallback 機制，不安裝 agent 也能運作。

## 三個 Steering 文件（Hierarchical Context Distribution）

Steering documents 提供持久的專案 context，引導所有 spec 開發：

- **`product.md`**：產品願景、目標使用者、核心功能、成功指標
- **`tech.md`**：技術堆疊與框架、開發工具與實踐、技術限制、第三方整合
- **`structure.md`**：檔案組織模式、命名慣例、import patterns、程式碼組織原則

透過 `/spec-steering-setup` 建立後，所有 spec 自動對齊這三份文件，減少重複說明、確保一致性。

## Context 最佳化機制

系統實現 60–80% token 減少：

- **Universal context sharing**：Steering、specification、template 文件全部優化
- **三組優化指令**：`get-steering-context`、`get-spec-context`、`get-template-context`
- **差異化處理**：Bug documents 直接讀取（無冗餘）；templates 批量載入（高冗餘）
- **Session-based caching**：智慧偵測檔案變更並失效快取

## 10 個 Slash Commands

**Spec Workflow（5 個）**：
```bash
/spec-steering-setup          # 建立三個 steering 文件
/spec-create feature-name "Description"  # 完整 spec 工作流（一鍵）
/spec-execute <task-id> feature-name     # 手動執行特定任務
/<name>-task-<id>             # 自動生成的任務指令
/spec-status                  # 進度檢視
```

**Bug Fix Workflow（5 個）**：
```bash
/bug-create issue-name "Description"
/bug-analyze
/bug-fix
/bug-verify
/bug-status
```

## 目錄結構

```
your-project/
├── .claude/
│   ├── commands/        # 14 slash commands + 自動生成
│   ├── steering/        # product.md, tech.md, structure.md
│   ├── templates/       # 文件模板
│   ├── specs/           # 生成的 specifications
│   ├── bugs/            # Bug fix 工作流
│   └── agents/          # AI agents（預設啟用）
```

## Real-Time Dashboard

```bash
npx -p @pimzino/claude-code-spec-workflow claude-spec-dashboard

# 帶 tunnel（外部分享）
npx -p @pimzino/claude-code-spec-workflow claude-spec-dashboard --tunnel --tunnel-password mySecret123
```

WebSocket 即時進度追蹤，支援 Git 整合，可透過 Cloudflare/ngrok tunnel 分享給外部關係人。

## 安裝

```bash
npm i -g @pimzino/claude-code-spec-workflow
claude-code-spec-workflow
```

## Key Insights
- Steering documents 是「hierarchical context distribution」的核心：一次定義，全部 spec 自動繼承，解決跨 spec 重複解釋問題
- 四代理分工讓驗證與執行分離——validator 類 agent 只做檢查，executor 只做實作，職責清晰
- 60–80% token 節省主要來自 session-based caching + bulk template loading，非逐行壓縮
- MCP 版本已是開發重心，slash command 版本適合不想引入 MCP 的使用者

## Code Examples / Commands

```bash
# 安裝
npm i -g @pimzino/claude-code-spec-workflow
claude-code-spec-workflow

# 建立 steering 文件
/spec-steering-setup

# 完整 spec 工作流（一鍵觸發四階段）
/spec-create oauth2-auth "Add OAuth2 authentication with JWT tokens"

# 執行特定任務
/spec-execute 1 oauth2-auth

# Bug fix 工作流
/bug-create login-timeout "Users getting logged out unexpectedly"
/bug-analyze
/bug-fix
/bug-verify
```

---
title: "The 'Virtual Monorepo' Pattern"
author: "Owen Zanzal"
date: 2026-03-23
source: "https://medium.com/devops-ai/the-virtual-monorepo-pattern-how-i-gave-claude-code-full-system-context-across-35-repos-43b310c97db8"
tags: [claude-code, monorepo, context, multi-repo, CLAUDE.md]
topic: orchestration
---

# The 'Virtual Monorepo' Pattern

Owen Zanzal 在管理 35 個分散式 repo 時發現 AI 工具的核心限制：當系統分散在多個 repository，AI 無法跨 repo 推理，無從追蹤完整資料流。他的解法是用三個本機檔案創造「虛擬 monorepo」視角，不需要改動任何 CI/CD pipeline 或現有架構。

## 三檔案模式

**1. `.repos` bash script**
包含按 domain 分組的 `git clone` 指令（services、infrastructure、frontends），在本機建立統一工作空間，每個 repo 維持獨立 git 歷史，對現有 CI/CD 與團隊流程零改動。

**2. `CLAUDE.md` System Map**
詳細記錄服務間的相互依賴與資料流。範例結構：`event-ingestion-service` 發布到 normalized events topic，由 `stream-processor` 消費後寫入 database cluster。這份文件讓 Claude 能在一個 session 中理解跨服務的資料流向。

**3. `README.md` Context Document**
提供架構敘事：為何系統如此設計、tech stack 決策背景、端到端資料流、操作約束。讓 AI 理解「為什麼這樣」而非只知道「是什麼」。

## 解決的核心問題

- **跨服務推理**：追蹤一筆資料在 35 個 repo 中的完整流向
- **協調變更**：schema 修改時自動找出所有受影響的下游服務
- **Infrastructure-Application 對齊**：連結 Terraform 配置與應用行為
- **分散式除錯**：跨 repo 追蹤 bug 根因

## 實際收益

過去需要資深工程師腦中龐大 mental model 才能回答的問題，現在 AI 可以直接推理，加速新人上手，減少因依賴關係未揭露導致的生產事故。

## 已知代價

- 需要 clone 所有 repo 的磁碟空間
- 隨 repo 增減需維護 `.repos` 同步
- 在非常大型系統中可能引入 context noise
- Context 管理不解決根本架構問題

## Key Insights
- 三檔案模式（`.repos` script + `CLAUDE.md` system map + `README.md` architecture doc）讓 Claude 跨 35 個 repo 取得完整 context，零 CI/CD 改動
- 核心原則：AI 的有效性上限等於它能看到的 context 品質，「context beats structure」
- 此模式使跨服務的 schema 變更影響分析、完整資料流追蹤成為可能

## Code Examples / Commands

```bash
# .repos script 範例結構
#!/bin/bash
# Services
git clone git@github.com:org/event-ingestion-service.git
git clone git@github.com:org/stream-processor.git
git clone git@github.com:org/database-cluster.git
# Infrastructure
git clone git@github.com:org/terraform-infra.git
# Frontends
git clone git@github.com:org/web-frontend.git
```

```markdown
# CLAUDE.md System Map 範例
## Service Dependencies
- event-ingestion-service → publishes to: normalized-events-topic
- stream-processor → consumes: normalized-events-topic → writes to: database-cluster
- web-frontend → reads from: database-cluster (via API)
```

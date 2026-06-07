---
title: "8 Claude Code Tips for Large Monorepo Projects"
author: "Diptendu Das"
date: 2026-05-18
source: "https://diptendud.medium.com/8-claude-code-tips-for-large-monorepo-projects-1f84a34316dd"
tags: [claude-code, monorepo, enterprise, CLAUDE.md, sub-agent, DRI]
topic: enterprise
---

# 8 Claude Code Tips for Large Monorepo Projects

Diptendu Das 從管理 10M+ LOC monorepo 的實務提煉出 8 個具體技巧，指出「預設的 Claude Code 工作流程在小專案有效，但在 monorepo 規模反而主動傷害你」。他的 monorepo 環境：多個 packages、三個 runtime、兩種語言。

## 8 個具體技巧

**Tip 1 — Nested CLAUDE.md Hierarchy**
不在 root 放單一 CLAUDE.md。在每個 package 目錄下各放一個 CLAUDE.md，只記錄該 package 的規範。Claude 會自動載入從當前目錄往上的 CLAUDE.md 層級，實現精準 context 注入。

**Tip 2 — Subdirectory Initialization**
避免從 repo root 啟動 Claude Code。在 package 子目錄啟動，避免 Claude 掃描整個 10M LOC 根目錄，把 context 浪費在無關的 package。

**Tip 3 — Per-Package Scoped Test/Lint Commands**
每個 package 的 CLAUDE.md 記錄該 package 的測試與 lint 指令，而非全局指令。避免 Claude 跑全 monorepo 的測試套件（可能耗時數十分鐘）。

**Tip 4 — Path-Glob Rules in `.claude/rules/*.md`**
用路徑 glob pattern 限定規則適用範圍。例如 `packages/api/**` 的規則只在 API package 觸發，不污染前端 package 的 context。

**Tip 5 — Sub-Agent Delegation for Research**
複雜的跨 package 調查任務委派給 sub-agent。主對話保持專注於當前 package，研究型任務（讀取 ≥10 個檔案）交給隔離的 sub-agent 處理。

**Tip 6 — Per-Package Skills**
每個 package 定義自己的 slash command skills，而非全局單一技能集。例如 `packages/api/.claude/commands/run-api-tests.md` 只對 API 開發者可見。

**Tip 7 — `/clear` Between Tasks**
切換不同 package 或不同任務類型時執行 `/clear`，重置 context window。不清除時，前一個 package 的 context 會影響當前任務的推理品質。

**Tip 8 — Designate a Claude Code DRI (Distinct Responsible Individual)**
指定一個人作為「agent manager / DRI」，負責協調跨團隊的 Claude Code 工作流程、維護 CLAUDE.md hierarchy、管理 skill 版本、仲裁跨 package 衝突。這是最獨特的建議，也是 10M+ LOC 規模下最容易被忽略的人力組織問題。

## Key Insights
- 10M+ LOC monorepo 需要 nested CLAUDE.md hierarchy + per-package skills + path-glob rules 三層結構，才能避免 context 污染
- Tip 8 最獨特：指定一個 Claude Code DRI 協調跨團隊工作流程，是組織治理問題而非技術問題
- `/clear` between tasks 是 context 管理的最低成本操作，切換 package 後必須執行

## Code Examples / Commands

```
# CLAUDE.md 層級結構
/repo-root/CLAUDE.md          # 全局規範（minimal）
/packages/api/CLAUDE.md       # API package 專屬規範
/packages/frontend/CLAUDE.md  # Frontend package 專屬規範
/packages/shared/CLAUDE.md    # Shared library 規範
```

```
# .claude/rules 路徑 glob 範例
# 在 rules/api-rules.md 中指定
path: packages/api/**
# 只在 API 目錄下的工作中載入此規則
```

```bash
# Per-package 測試指令（記錄在各 package 的 CLAUDE.md）
# packages/api/CLAUDE.md:
# Test command: pnpm --filter api test
# Lint command: pnpm --filter api lint
```

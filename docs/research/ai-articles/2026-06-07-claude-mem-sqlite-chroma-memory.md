---
title: "claude-mem: Persistent Memory for AI Agents with SQLite FTS5 + Chroma"
author: "thedotmack"
date: 2026-06-07
source: "https://github.com/thedotmack/claude-mem"
tags: [claude-code, memory, sqlite, chroma, mcp, lifecycle-hooks, persistent-context]
topic: SQLite FTS5 + Chroma 雙軌記憶系統，5 lifecycle hooks，progressive disclosure
---

# claude-mem: Persistent Memory for AI Agents

claude-mem 是一套讓 AI agent 跨 session 保留完整 context 的持久記憶系統，核心設計為「自動捕捉工具使用觀察、生成語意摘要，並於未來 session 自動注入」。

## 架構設計

系統由五大元件組成：

1. **Lifecycle Hooks（5 個鉤子）**：在 `SessionStart`、`UserPromptSubmit`、`PostToolUse`、`Stop`、`SessionEnd` 五個生命週期節點觸發對應腳本，實現自動記憶的零手動介入。

2. **Worker Service**：HTTP API 服務，運行於 port 37777，提供 web viewer UI，由 Bun 管理。

3. **SQLite Database**：持久儲存 sessions、observations、summaries，支援 FTS5 全文檢索（關鍵字搜尋）。

4. **Chroma Vector Database**：向量語意搜尋，實現混合搜尋模式——關鍵字（SQLite FTS5）+ 語意相似度（Chroma）雙軌並行。

5. **Search Capability**：透過 `mem-search` MCP skill 執行自然語言查詢。

## 三層 Progressive Disclosure 搜尋模式

系統採用 3-layer workflow pattern，約節省 ~10x token：

- `search`：compact index（最省 token，先過濾）
- `timeline`：chronological context（按時間序提供上下文）
- `get_observations`：full details（完整觀察紀錄，按需取用）

此設計實現「先篩選再取全文」，避免一次性載入大量記憶造成 context 膨脹。

## 隱私控制機制

用 `<private>` 標籤包裹的內容會被排除在記憶儲存之外，適用於敏感資訊（API keys、個人資料等）。

## 安裝與平台支援

```bash
# 最簡安裝
npx claude-mem install

# Gemini CLI
npx claude-mem install --ide gemini-cli

# OpenCode
npx claude-mem install --ide opencode
```

多平台支援：Claude Code、Gemini CLI、OpenCode、OpenClaw。亦可透過 Claude Code 內建 Marketplace 安裝。

## 系統需求

- Node.js 18.0+
- Bun（自動安裝）
- uv（用於 vector search）
- SQLite 3（bundled）

## Key Insights
- 雙軌搜尋（FTS5 關鍵字 + Chroma 語意）解決純向量搜尋的精確匹配盲點，也解決純關鍵字搜尋的語意理解缺失
- 5 個 lifecycle hooks 全程自動化，SessionStart 自動注入相關記憶，PostToolUse 自動捕捉工具結果，形成閉環
- Progressive Disclosure 三層模型使 token 消耗可控：先用 compact index 過濾，確認相關後再取 full observations
- Apache 2.0 授權設計目標是「易於嵌入企業系統、機器人堆疊、生產 agent harness」

## Code Examples / Commands

```bash
# 安裝
npx claude-mem install

# 搜尋記憶（透過 MCP skill）
# 層1：compact index（最省 token）
search "authentication flow"

# 層2：時間序 context
timeline --since "2 days ago"

# 層3：完整觀察
get_observations --id <observation-id>
```

Web Viewer 位於 `http://localhost:37777`，可瀏覽所有 sessions 及 observation IDs（供 citation 引用）。

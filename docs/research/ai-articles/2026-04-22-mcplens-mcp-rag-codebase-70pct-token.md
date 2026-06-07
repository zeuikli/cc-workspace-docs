---
title: "I built an MCP server to reduce Claude Code token usage (mcplens)"
author: "Vitor Figueredo"
date: 2026-04-22
source: "https://medium.com/@vmsfigueredo/i-built-an-mcp-server-to-reduce-claude-code-token-usage-using-claude-code-250ef7654e47"
tags: [claude-code, MCP, RAG, token-optimization, embeddings, ollama, sqlite, tree-sitter]
topic: MCP
---

# I built an MCP server to reduce Claude Code token usage (mcplens)

Vitor Figueredo 解決了 Claude Code 的核心低效：「問 authentication 怎麼運作，Claude 會在回答前打開 10-15 個甚至 20 個檔案。」解法是 mcplens，一個本機 MCP server，對 codebase 套用 RAG，達到 70-85% token 減少。

## 技術架構

### Embeddings 引擎
- **工具**：Ollama + `nomic-embed-text` 模型（270MB 本機模型）
- **優勢**：完全本機運算，無資料離開設備，替代 OpenAI embedding API
- **隱私保護**：對 NDA 專案或客戶程式碼的關鍵保護

### Vector Storage
- **技術**：SQLite + in-process cosine similarity
- **效能**：約 20,000 chunks 的相似度搜尋 ~50ms
- **部署優勢**：無需獨立服務或 Docker，零額外基礎設施

### 程式碼切塊（Chunking）
- **方法**：AST-aware chunking via `tree-sitter`
- **效益**：在 function/class 邊界切塊，保持語意完整性
- **fallback**：不支援的檔案類型使用 sliding window

### 增量索引
- **策略**：SHA-1 hash delta detection
- **效率**：1,400 個檔案、3 個變更的專案 sync 時間 ~2 秒

## 驗證指標

**生產環境測試（Laravel 12 + SvelteKit 5，~1,400 個檔案）**：

| 比較項目 | 傳統方式 | mcplens |
|---------|---------|---------|
| Token 數（架構描述）| 120,000-150,000 | 45,000 |
| 減少幅度 | — | 70% |
| 執行時間 | 5:00 分鐘 | 2:48 分鐘 |
| 速度提升 | — | 45% |

架構分析任務：14 queries，1.5K tokens，零檔案讀取。
模組遷移規劃：45 queries，5.3K tokens。

## 安裝與設定

```bash
npm install -g @vmsfigueredo/mcplens
mcplens init
ollama pull nomic-embed-text:latest
```

## Dashboard 介面

Port 3333 提供即時監控：
- 活躍 session 監控
- 即時 re-indexing 進度
- Index 概覽與統計
- Query 測試 playground

## 開源資訊
- Repo：github.com/vmsfigueredo/mcplens
- 相容：Claude Code、Cursor、Windsurf 及任何 MCP 相容 assistant
- 需求：Node.js + Ollama

## Key Insights
- RAG over codebase via MCP：Ollama nomic-embed-text（270MB 本機）+ SQLite vector store cosine similarity（~50ms）+ AST-aware chunking via tree-sitter
- 驗證：70-85% token 減少；45,000 vs 120,000-150,000 tokens；45% 速度提升（2:48 vs 5:00 min）
- 隱私優先：on-device embeddings 避免雲端資料外洩；SHA-1 hash delta detection 實現增量索引

## Code Examples / Commands

```bash
# 安裝
npm install -g @vmsfigueredo/mcplens

# 初始化（在 repo 根目錄執行）
mcplens init

# 下載 embedding 模型
ollama pull nomic-embed-text:latest

# 啟動 MCP server + dashboard
mcplens start
# Dashboard: http://localhost:3333
```

```json
// Claude Code settings.json 配置
{
  "mcpServers": {
    "mcplens": {
      "command": "mcplens",
      "args": ["serve"]
    }
  }
}
```

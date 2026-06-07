---
title: "Graphify: AST 知識圖譜讓 Claude Code Token 用量削減 71x"
author: "Manav Ghosh"
date: 2026-06-07
source: "https://medium.com/@manavghosh/graphify-claude-code-how-i-cut-token-usage-by-71x-on-a-50k-line-codebase-74868ac67fd1"
tags: [claude-code, graphify, ast, token-optimization, tree-sitter, knowledge-graph, pre-tool-use-hook]
topic: Graphify AST 知識圖譜，71x token 削減，Tree-sitter 解析，隱私邊界
---

# Graphify: 71x Token 削減的 AST 知識圖譜方案

作者：Manav Ghosh，發布於 Medium，2026-04。Graphify 是一個開源工具，透過預編譯 codebase 為知識圖譜，解決 Claude Code 在大型 codebase 上的 token 消耗爆炸問題。

## 核心問題

在 50K 行 codebase 上，每次 Claude Code 的 Glob/Grep 導航產生 12,000–18,000 tokens 的 overhead。Graphify 將此壓縮至 2,000 tokens 以下，實現 **71x token 削減**。

（以 20K 行 Python 專案 API2MCP 的實測數據：12,000–18,000 → 不到 2,000 tokens/session）

## 三階段分析 Pipeline

### Pass 1：AST Analysis（本地執行）
- 使用 **Tree-sitter** 解析原始碼（支援 25+ 語言）
- 提取：functions、classes、imports、call graphs
- **完全本地**，原始碼不離開機器

### Pass 2：Audio/Video Processing（選配）
- 使用 **Whisper**（本地）轉錄媒體檔案

### Pass 3：Semantic Analysis（最小化 LLM 呼叫）
- 僅發送 documentation + transcripts（非源碼）至 LLM API
- 提取關係、語意標籤

## 隱私邊界設計

原始碼在 Pass 1 本地解析，**永遠不離開機器**。只有文件字串和 transcript 文字發送至 LLM API，符合企業代碼保密需求。

## 知識圖譜核心概念

**三種邊類型**：
- `EXTRACTED`：AST 直接觀察到的關係
- `INFERRED`：上下文推斷的關係
- `AMBIGUOUS`：不確定的關係（保留但標記）

**God nodes**：高度連接的 hub，代表核心抽象（例如：`BaseModel`、`DatabaseConnection`）

**Community detection**：使用 **Leiden algorithm** 按連接性將模組聚類

## 與 Claude Code 的整合

透過 `PreToolUse` hook 攔截 Glob 和 Grep 操作：

```json
// .claude/settings.json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "(Glob|Grep)",
      "command": "graphify query --inject-context $CLAUDE_TOOL_INPUT"
    }]
  }
}
```

Hook 在搜尋執行前查詢預建圖譜，將相關 context 作為 system messages 注入——Claude Code 無需修改，透明整合。

## 三種輸出產物

| 產物 | 用途 |
|------|------|
| `graph.json` | 機器可讀，供 hook 查詢 |
| `graph.html` | 可視化探索器（瀏覽器開啟） |
| `GRAPH_REPORT.md` | 人類可讀摘要 |

## 效益的複利特性

Token 節省在跨多個 session 後才會完全顯現，單次互動的效益不明顯。對於長期維護的大型 codebase，效益逐 session 累積。

## Key Insights
- 71x 削減的來源是「預計算 vs 即時搜尋」的架構轉換：圖譜建一次，查詢成本 O(1) 而非 O(n)
- Tree-sitter 支援 25+ 語言使 Graphify 具有通用性，不限於 Python 或 JavaScript
- `PreToolUse` hook 攔截 Glob/Grep 是最小侵入的整合方式——不改 Claude Code 本身，只在工具呼叫前注入 context
- 隱私邊界（Pass 1 本地 → Pass 3 只傳文件）解決了企業代碼安全顧慮，使 AI 輔助可用於保密專案

## Code Examples / Commands

```bash
# 安裝（三步驟）
pip install graphify
graphify init              # 初始化配置
graphify build             # 分析 codebase 建構圖譜

# 查詢圖譜
graphify query "authentication flow"
graphify query --god-nodes              # 列出核心抽象
graphify query --community api.routes   # 探索模組聚類
```

```json
// .claude/settings.json - PreToolUse Hook 整合
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Glob",
        "command": "graphify intercept glob --query $CLAUDE_TOOL_PATTERN"
      },
      {
        "matcher": "Grep",
        "command": "graphify intercept grep --query $CLAUDE_TOOL_PATTERN"
      }
    ]
  }
}
```

```python
# graph.json 結構範例
{
  "nodes": {
    "auth.AuthService": {
      "type": "class",
      "file": "src/auth/service.py",
      "line": 42,
      "community": "authentication",
      "is_god_node": True,
      "connections": 47
    }
  },
  "edges": [
    {
      "from": "auth.AuthService",
      "to": "db.UserRepository",
      "type": "EXTRACTED",
      "relation": "dependency"
    }
  ]
}
```

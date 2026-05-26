---
url: "https://github.com/anthropics/claude-code/issues/7336"
source_file: ../2026-05-12-github-7336-mcp-lazy-loading.md
date: 2026-05-12
scored: 2026-05-16
source: GitHub Issues — anthropics/claude-code
source_tier: C
tags: [mcp, lazy-loading, token-overhead, context-management, feature-request]
---

# Feature Request: Lazy Loading for MCP Servers and Tools (#7336)

**原始來源**：https://github.com/anthropics/claude-code/issues/7336  
**狀態**：Feature request（尚未實作）

---

## TL;DR

量化了 MCP tool schema 的真實 token 成本：一個有 73 個 MCP tool 的環境，啟動時消耗 108k tokens（54% of 200k limit），僅剩 92k 可用。提出 lazy loading 方案（registry index ~5k tokens，按需載入），並有 PoC 實作。對 context-management 規則有直接補充價值。

---

## 核心數據（量化 token 成本）

| 組件 | Token 成本 | 佔比 |
|------|-----------|------|
| MCP tools（73 個） | 39,800t | 19.9% |
| Custom agents（56 個） | 9,700t | 4.9% |
| System tools | 22,600t | 11.3% |
| Memory files | 36,000t | 18.0% |
| **合計** | **~108,000t** | **54%** |

可用 context：**92k tokens**（46%）

Lazy loading 後預估：**195k tokens 可用**（5k registry + 按需載入）

---

## 核心提案

- **Registry index**：只載入 name + description + trigger keywords（~5k tokens）
- **On-demand loading**：偵測 user input keywords → 載入相關工具
- **Session cache**：已載入的工具 cache 整個 session

---

## cc-workspace 可行動性

1. `context-management.md` § Token Overhead 表格標記「MCP tool schemas 6%」——此 issue 提供精確的每工具 token 成本（平均 ~544t/tool）和具體量化數據
2. 在官方實作 lazy loading 前，可手動緩解：
   - 減少 MCP server 數量（只配置當前任務需要的）
   - 確認 MCP tool schemas 確實是瓶頸再配置

---

## 評分

| 維度 | 分數 | 理由 |
|------|------|------|
| A. Workspace 可行動性 | 7/10 | 提供 MCP token 成本的精確量化數據，可補充 context-management.md；lazy loading 尚未實作，短期只能手動緩解 |
| B. 創新性 | 7/10 | 量化「每個工具 ~544t」的具體數字是新數據；lazy loading 概念在 IDE 生態有先例（VSCode、JetBrains） |
| C. 證據品質 | 6/10 | 真實環境量測數據（單一用戶）+ PoC；非廣泛驗證，但數據點本身可信 |
| D. 技術深度 | 6/10 | 包含 JSON 配置範例、三階段實作計畫；PoC 存在但未附完整代碼 |
| E. 泛化性 | 8/10 | MCP token 成本問題適用所有重度 MCP 用戶 |
| **加權總分** | **6.8/10** | 7×0.3 + 7×0.2 + 6×0.2 + 6×0.15 + 8×0.15 = 2.10+1.40+1.20+0.90+1.20 |

**整合決策**：Rule（補充量化數據到現有 context-management 規則）  
**整合位置**：`.claude/rules/context-management.md` § Token Overhead 九大模式表格 — MCP tool schemas 行補充「平均 ~544t/tool，73 tools = 39.8k tokens」具體量化  
**整合狀態**：待實作

---

## TODO

- [ ] 更新 `context-management.md` § Token Overhead 表格，MCP tool schemas 欄位補充具體量化（39.8k tokens for 73 tools）
- [ ] 追蹤 GitHub issue #7336 狀態，官方實作後更新 workspace 配置建議

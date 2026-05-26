---
url: "https://medium.com/@adnanmasood/agent-harness-engineering-the-rise-of-the-ai-control-plane-938ead884b1d"
date: 2026-04-23
source: Medium (Adnan Masood, PhD)
authors: Adnan Masood
tags: [control-plane, harness-architecture, PEV-loop, cost-optimization, MCP]
related: research/agent-harness/references/2026-04-adnan-masood-agent-control-plane.md
---

# Agent Harness Engineering — The Rise of the AI Control Plane

**原始來源**：https://medium.com/@adnanmasood/agent-harness-engineering-the-rise-of-the-ai-control-plane-938ead884b1d  
**作者**：Adnan Masood, PhD  
**歸檔日期**：2026-05-10  
**Note**: 完整版在 `research/agent-harness/references/2026-04-adnan-masood-agent-control-plane.md`

---

## 評分摘要

| 維度 | 分數 | 理由 |
|------|------|------|
| A. Workspace 可行動性 | 8/10 | PEV loop + cost tactics 可直接套用 |
| B. 創新性 | 6/10 | 已知模式的整合，「Control Plane」框架是新穎標籤 |
| C. 證據品質 | 7/10 | 行業統計有引用，cost 數字有依據 |
| D. 技術深度 | 7/10 | 哈ness 架構清楚，但有些建議偏通用 |
| E. 泛化性 | 9/10 | Enterprise-focused，廣泛適用 |
| **加權總分** | **7.5/10** | 8×0.3 + 6×0.2 + 7×0.2 + 7×0.15 + 9×0.15 = 7.50 |

**整合決策**：RULE — PEV loop 補充進 `harness-design.md`，cost tactics 補充進 `subagent-strategy.md`  
**整合位置**：`.claude/refs/harness-design.md` §PGE 決策樹  
**整合狀態**：待實作

---

## TL;DR

Harness 是 AI 系統的「operating system」：管理 context、工具執行、安全控制、session memory。文章稱 65% 的企業 AI 失敗源於 harness 缺陷（非推理）。Plan-Execute-Verify (PEV) loop + human-in-the-loop gates 是核心設計模式。Token 成本優化：prefix stability + KV-cache → $3.00→$0.30 per million tokens (10x reduction)。

---

## 核心主張

### 1. Harness = AI Control Plane

5 層架構：
```
Layer 5: Observability (logs, traces, metrics)
Layer 4: Safety & Security (guardrails, sandboxing)
Layer 3: Context Management (prefix stability, KV cache)
Layer 2: Tool Execution (function calling, MCP)
Layer 1: Agent Loop (planner, executor, evaluator)
```

### 2. Plan-Execute-Verify (PEV) Loop

類似 Anthropic 的 PGE（Planner-Generator-Evaluator），但強調 human-in-the-loop gates：

```
Plan: 分解任務，識別高風險步驟
  ↓
Execute: 在沙箱環境執行
  ↓
Verify: 確定性工具驗證（非 LLM 自評）
  ↓ [如果高風險] ↓
Human Gate: 人類審批後繼續
```

### 3. 65% 失敗率的根因分析

65% 企業 AI 失敗來自 harness 缺陷：
- 35%：context 管理失效（token overflow、prefix 不穩定）
- 20%：工具執行錯誤（timeout、schema mismatch）
- 10%：安全控制不足（prompt injection、data leakage）

### 4. Token 成本優化策略

| 策略 | 效果 | 實作 |
|------|------|------|
| Prefix stability | 90%+ cache hit | 靜態 CLAUDE.md 不 mid-session 改 |
| KV-cache | 10x cost reduction | `settings.json` prompt caching |
| Deferred tool loading | -40% schema tokens | Claude Code ToolSearch 機制 |
| Context compaction | -60% context tokens | `/compact` 主動觸發 |

---

## 對 cc-workspace 的映射

| 文章概念 | cc-workspace 對應 | 對齊狀態 |
|---------|----------------|---------|
| Control Plane 5 層 | `.claude/` 多層架構 | ✅ |
| PEV Loop | PGE（plan-mode-expert + implementer + /deep-review）| ⚠️ 無決策樹 |
| Human-in-the-loop gates | 生產紅線（二次確認）| ✅ |
| Prefix stability | output-discipline.md（不 mid-session 改規則）| ✅ |
| 65% harness failure stat | 支持 workspace 的 harness 投資優先級 | ✅ 驗證 |

**Gap**：PEV Loop 沒有正式的「高風險步驟識別」決策樹（何時觸發 Human Gate？）

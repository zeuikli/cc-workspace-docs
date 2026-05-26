# Anthropic Code w/ Claude 2026 Live Blog — @simonw

**來源**：https://simonwillison.net/2026/May/6/code-w-claude-2026/
**作者**：Simon Willison（@simonw）
**發布日期**：2026-05-06
**收錄日期**：2026-05-10
**類型**：推文 + Live Blog 摘要
**分類**：claude-code-tips

---

## 核心推文

> "Live blogging Anthropic's Code w/ Claude 2026 event:
>
> - Rate limits doubled for Pro/Max/Enterprise (5-hour → 10-hour Claude Code sessions)
> - Claude Code Routines GA — scheduled / webhook-triggered automated tasks
> - Expanded MCP support with alwaysLoad:true for permanent tools
> - Extension model: skills + sub-agents + hooks + MCP all composable
>
> Key insight: extensibility is THE differentiator. Model is commodity now."

---

## 研究摘要

**TL;DR**：Anthropic Code w/ Claude 2026 活動的即時記錄。核心訊號：速率限制加倍（session 長度 5h → 10h），Routines GA，MCP alwaysLoad 機制上線。Simon 的核心洞見：**可擴充性（extensibility）是關鍵差異化，模型已成商品**。

### 重要功能更新

| 功能 | 變化 | Harness 意涵 |
|------|------|-------------|
| Session 長度 | 5h → 10h | 長任務 harness 需求增加 |
| Routines GA | Scheduled + Webhook | Harness 自動化觸發點增加 |
| `alwaysLoad: true` | MCP 永久工具常態可見 | Tool context 管理策略改變 |
| Extension model | skills + agents + hooks + MCP | Harness 組合性是設計核心 |

### Simon 的 harness 洞見

> "The model is the commodity. What differentiates teams is the harness they build around it — the skills, the context management, the integration patterns."

---

## 評分

| 維度 | 分數 | 理由 |
|------|------|------|
| 相關性 | 9/10 | Anthropic 官方功能更新直接影響 harness 設計 |
| 可行動性 | 8/10 | `alwaysLoad:true` + Routines 可立即應用 |
| 新穎性 | 7/10 | 功能更新報導，非新理論 |
| **總評** | **8/10** | — |

---

## 與 cc-workspace 的連結

- `research/best-practices/27-whats-new-w18-w19.md` 涵蓋相關功能
- `alwaysLoad: true` 影響 context-management.md §Prompt Caching 架構
- Routines GA 與 `research/best-practices/11-routines.md` 的更新對應

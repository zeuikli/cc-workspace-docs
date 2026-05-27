---
title: "Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for LLM Agents"
arxiv_id: 2601.01885
authors: "Yi Yu, Liuyi Yao, Yuexiang Xie, et al."
published: 2026-01-05
source: "https://arxiv.org/abs/2601.01885"
source_tier: P
---

# Agentic Memory: Learning Unified Long-Term and Short-Term Memory Management for LLM Agents

**ArXiv**: 2601.01885 | **Date**: 2026-01-05 (修訂 2026-04-30) | **Authors**: Yi Yu, Liuyi Yao, Yuexiang Xie, et al. | **Category**: cs.CL

## 摘要

解決 LLM agent 在有限 context window 內管理擴展推理任務的核心挑戰。現有架構通常「獨立優化長期與短期記憶，再以臨時方式結合」，導致記憶構建碎片化和次優性能。提出 AgeMem 框架，將兩種記憶統一整合到 agent 決策框架中。

## 核心創新：AgeMem

**關鍵設計**：將記憶操作暴露為**工具導向行動**，讓 LLM agent 自主決定何時且如何 store、retrieve、update、summarize 或 discard 資訊。

### 技術方法

三階段漸進強化學習策略 + step-wise GRPO（Group Relative Policy Optimization）：
- 解決記憶操作的稀疏和不連續獎勵挑戰
- 端對端學習記憶管理策略（而非依賴預定義 heuristics）

## 主要結果

在 5 個長視地平線基準上：
- 超越所有現有記憶增強基準
- 產生更高品質的長期記憶表示
- 更高效的 context 使用
- 跨多個 LLM 架構泛化

## 與現有方法的對比

| 方法 | 短期記憶 | 長期記憶 | 整合方式 |
|------|---------|---------|---------|
| 傳統方法 | 靜態 STM + 觸發式 LTM | 靜態 STM + agent-based LTM | 獨立優化後臨時組合 |
| AgeMem | 工具驅動統一管理 | 工具驅動統一管理 | 端對端聯合優化 |

## 與 AutoMode 概念的關係

與 `2026-05-13-useful-memories-faulty-llm` 中的 AutoMode 設計理念一致：
- 讓 agent 自主決定 Retain/Delete/Consolidate（而非強制整合）
- AgeMem 進一步通過 RL 優化此自主決策能力

## 代碼

公開可用，支持可重現性。

## 分類

**Memory Architecture** — 首個通過強化學習端對端統一長短期記憶管理的框架，為 AutoMode 概念提供了 RL 優化路徑。

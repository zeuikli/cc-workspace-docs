---
title: "MultiAgentBench: Evaluating the Collaboration and Competition of LLM Agents"
arxiv_id: 2503.01935
authors: "Kunlun Zhu, Hongyi Du, Zhaochen Hong, et al."
published: 2025-03-03
source: "https://arxiv.org/abs/2503.01935"
source_tier: P
---

# MultiAgentBench: Evaluating the Collaboration and Competition of LLM Agents

**ArXiv**: 2503.01935 | **Date**: 2025-03-03 | **Authors**: Kunlun Zhu, Hongyi Du, Zhaochen Hong, et al. | **Category**: cs.MA, cs.AI, cs.CL

## 摘要

全面評估框架，評估 LLM 多 agent 系統在多樣化互動場景中的協作與競爭能力。核心問題：「現有基準要麼只關注單 agent 任務，要麼僅限於特定領域」。引入里程碑式 KPI（Milestone-based Key Performance Indicators）捕捉超越傳統成功指標的細微協作面向。

## 評估方法

### 協調拓撲測試

| 拓撲結構 | 描述 |
|---------|------|
| 星形（Star） | 中央協調者 + 周圍 agents |
| 鏈形（Chain） | 序列傳遞 |
| 樹形（Tree） | 階層式協調 |
| 圖形（Graph） | 任意連接 |

此外測試：群體討論（Group discussion）、認知計畫（Cognitive planning）

## 主要發現

| 發現 | 量化結果 |
|------|---------|
| 最高任務分數模型 | **GPT-4o-mini**（非最強模型）|
| 最有效拓撲（研究場景）| **圖形結構**（Graph topology）|
| 認知計畫提升 | 里程碑達成率 **+3%** |

**關鍵洞見**：小型模型在適當協調下可勝過更大模型，協調架構本身是關鍵。

## 與 MAFBench 的關係

| | MultiAgentBench | MAFBench (2602.03128) |
|-|-|-|
| 焦點 | 協作與競爭場景 | 框架架構影響 |
| 指標 | 里程碑式 KPI | 延遲/準確率/協調成功率 |
| 發現方向 | 任務多樣性 | 架構選擇影響（100×）|

兩者互補：MultiAgentBench 提供任務覆蓋，MAFBench 提供框架架構洞察。

## 代碼與資料集

公開可用，支持可重現性。

## 分類

**Benchmark & Evaluation / Agent Architecture & Coordination** — 2025 年多 agent 評估的基礎基準，里程碑式 KPI 設計值得在評估 workspace 中的 sub-agent 性能時借鑑。

# Understanding Multi-Agent LLM Frameworks: A Unified Benchmark and Experimental Analysis

**ArXiv**: 2602.03128 | **Date**: 2026-02-03 | **Authors**: Abdelghny Orogat, Ana Rostam, Essam Mansour | **Category**: cs.AI

## 摘要

針對多 agent LLM 框架的評估進行系統性研究，填補「框架架構對性能的影響」這一重要空白。核心發現：「架構選擇本身可導致延遲和吞吐量的數量級差距」以及大幅度的準確性差異。

## 核心貢獻

### MAFBench 評估套件

統一評估平台，整合現有基準於標準化執行管道，解決碎片化的單能力評估問題。

### 架構分類法

建立系統性框架，比較多 agent LLM 系統的基本設計維度：
- 協調架構（星形/鏈形/樹形/圖形拓撲）
- 記憶行為
- 計畫效能
- agent 專業化程度
- 任務協調機制

## 主要量化發現

| 指標 | 框架架構影響 |
|------|------------|
| **延遲** | 純框架選擇即可增加 **>100×** 回應時間 |
| **計畫準確率** | 不同架構間最多降低 **30%** |
| **協調成功率** | 從 **>90% 降至 <30%**（僅因框架不同）|

**關鍵洞見**：框架架構本身（非模型）決定了大部分性能差異。25 頁，9 圖，13 表。

## 評估維度

1. 協調開銷（Orchestration overhead）
2. 記憶行為（Memory behavior）
3. 計畫效能（Planning effectiveness）
4. agent 專業化（Agent specialization）
5. 任務協調（Task coordination）

## 對 Workspace 的意義

確認「Harness > Model」原則在多 agent 框架層面的普適性：選擇正確的框架拓撲比選擇更強的模型更重要。

與現有論文 `2026-04-07-agent-harness-survey`（H=(E,T,C,S,L,V) 六元組）形成互補：本文提供多 agent 框架的 empirical 量化依據。

## 分類

**Agent Architecture & Coordination / Benchmark & Evaluation** — 多 agent 框架架構影響的首個系統性量化研究，100× 延遲差距是跨框架比較的重要基準。

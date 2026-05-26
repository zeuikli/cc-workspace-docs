---
title: "Agentic Harness for Real-World Compilers"
arxiv_id: 2603.20075
authors: "Yingwei Zheng, Cong Li, Shaohua Li, Yuqun Zhang, Zhendong Su"
published: 2026-03-20
source: "https://arxiv.org/abs/2603.20075"
source_tier: P
---

# Agentic Harness for Real-World Compilers

**ArXiv**: 2603.20075 | **Date**: 2026-03-20 | **Authors**: Yingwei Zheng, Cong Li, Shaohua Li, Yuqun Zhang, Zhendong Su | **Category**: cs.SE

## 摘要

首篇針對 LLM agent 理解和修復編譯器 bug 的 agentic harness 設計，以 LLVM（工業廣泛使用的編譯器基礎設施）為目標。揭示 frontier LLM 在編譯器問題上相比一般軟體 bug 存在**顯著性能差距**。

## 核心組件：llvm-autofix 系統

1. **Agent-friendly LLVM tools**：專為 LLM-compiler 互動設計的工具集
2. **llvm-bench**：可重現 LLVM bug 基準測試集
3. **llvm-autofix-mini**：專業化自動修復 agent

## 主要量化發現

| 指標 | 結果 |
|------|------|
| Frontier LLM 在編譯器 vs 一般軟體 bug 的性能差距 | **-60%** 性能退化 |
| llvm-autofix-mini vs SOTA 替代方案 | **+22%** 性能提升 |

## 核心洞察：域特化工具集的必要性

編譯器 bug 的獨特挑戰：
- 高技術複雜性
- 需要專業領域知識
- 歷史上 bug 文件稀疏或缺乏資訊

**一般 LLM 方法在專業工程域顯著退化**，需要域特化 harness。

## 對 Harness Engineering 的意義

與其他 harness 論文形成重要補充：
- 大多數 harness 研究聚焦通用軟體工程（SWE-bench）
- 本文展示**域特化 harness 設計**的必要性
- 60% 性能退化 = harness 工程在專業域的最大已知改進空間

### Harness 設計模式啟示

1. **工具域適配**：工具必須對目標域的知識和語言友好
2. **基準域對齊**：評估基準需反映真實的域特定挑戰
3. **Agent 特化**：通用 agent 不如域特化 agent

## 分類

**Harness Engineering** — 編譯器工程域的 agentic harness 研究，60% 域特化性能退化是最大的已知未開發 harness 優化空間，展示了域特化 harness 設計的必要性。

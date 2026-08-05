---
url: "https://arxiv.org/abs/2604.15679"
title: "Hierarchical Active Inference using Successor Representations"
archived_date: 2026-07-03
arxiv_id: 2604.15679
authors: ["Prashant Rangarajan", "Rajesh P. N. Rao"]
domain: active-inference
published_date: 2026-04-17
source_routine: routine-e
---

# Hierarchical Active Inference using Successor Representations

## 摘要 / 核心貢獻

本文提出一個結合階層式環境模型與 successor representations（後繼表徵）的階層式規劃架構，
根基於 active inference（主動推論）與自由能原理（Free Energy Principle, FEP）。
三項核心貢獻：(1) 展示低層 successor representations 如何使系統學習高層抽象狀態；
(2) 展示低層 active inference 如何 bootstrap 高層抽象動作；
(3) 展示這些抽象化如何提升規劃效率。研究團隊在 four-rooms、key-based navigation、
PointMaze 等導航任務、一個部分可觀測問題，以及 Mountain Car benchmark 上驗證框架。
作者宣稱這是 FEP-based 腦功能理論中，首次將「學習型階層狀態與動作抽象」應用於 active inference。

Active inference 是源於神經科學（Karl Friston 自由能原理）的另一套智能範式：
agent 透過最小化「預期自由能」（而非最大化獎勵）同時完成感知推論與行動選擇，
將感知、學習、規劃統一在同一個變分推論框架下，與主流強化學習 / LLM-based agent
的獎勵最大化範式有本質差異。

## 為何屬「新領域」

Workspace 現有 papers/ 451 篇集中於 LLM/agent/RAG/harness 等以 Transformer 為核心的範式；
`active-inference` / `free-energy` 關鍵詞在既有覆蓋集合（DAILY-TOPICS + WEEKLY-FOCUS +
papers 標題詞頻）命中 0 次 —— 是完全未觸及的替代智能理論框架。

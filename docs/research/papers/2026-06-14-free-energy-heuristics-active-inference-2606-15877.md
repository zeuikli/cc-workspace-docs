---
url: "https://arxiv.org/abs/2606.15877"
title: "Free Energy Heuristics: Fast-And-Frugal Cognition as Active Inference Under Uncertain Precision"
archived_date: 2026-07-03
arxiv_id: 2606.15877
authors: ["Alex Bogdan"]
domain: active-inference
published_date: 2026-06-14
source_routine: routine-e
---

# Free Energy Heuristics: Fast-And-Frugal Cognition as Active Inference Under Uncertain Precision

## 摘要 / 核心貢獻

本文探討為何 chain-of-thought（CoT）推理在某些任務上提升 LLM 表現，卻在另一些任務上使表現惡化。
作者提出「meta-uncertainty」（對自身證據可靠性的不確定性）是決定性因素，並證明：
在 precision prior 為 heavy-tailed 分佈時，最小化「預期自由能」的策略在累積有限數量的
高效度線索後便停止整合更多資訊 —— 此行為在特定條件下等同「take-the-best」捷思法，
統一了 fast-and-frugal cognition 與 active inference 兩套理論。

實證研究（FEH-79 benchmark）涵蓋 7 個模型、7,875 筆回應：
高 meta-uncertainty 題目隨推理鏈變長準確率顯著下降（高不確定性情境下降 17.3 個百分點），
而答案明確的題目則無此劣化。此框架調和了 Bayesian 與 fast-and-frugal 兩傳統，
將「less-is-more」現象重新詮釋為 meta-uncertainty 的指標，而非 Bayesian 認知的反例。

## 為何屬「新領域」

以 active inference / 自由能原理視角重新解釋 LLM CoT 推理的失效模式，
是「非主流智能理論框架 × 主流 LLM 現象」的交叉點，workspace 既有覆蓋集合中
`active-inference` / `free-energy` 命中 0 次，且此篇直接對應 workspace 高度關注的
CoT/reasoning 主題，提供全新理論透鏡，槓桿潛力高。

---
url: "https://arxiv.org/abs/2606.17115"
title: "Probing, Fusion, and Trustworthiness: A Systematic Evaluation of Foundation Model Representations for Multimodal Cancer Analysis"
archived_date: 2026-07-23
arxiv_id: 2606.17115
authors: ["Jingyu Hu", "Giuseppe Tripodi", "Reed Naidoo", "Sarah F. McGough", "Tapabrata Chakraborti"]
domain: genomic-biological-foundation-models
published_date: 2026-06-15
source_routine: routine-e
---

# Probing, Fusion, and Trustworthiness: A Systematic Evaluation of Foundation Model Representations for Multimodal Cancer Analysis

## 摘要 / 核心貢獻
本文系統性評測基礎模型在多模態癌症分析任務中的表徵品質，融合全切片病理影像（whole-slide images, WSI）與轉錄體（transcriptomic）資料。核心貢獻分三層：(1) probing——凍結表徵在下游癌症分類/預後任務上的可分性；(2) fusion——不同模態表徵的融合策略對表現的邊際貢獻；(3) trustworthiness——模型輸出在分布外（out-of-distribution）樣本與臨床決策情境下的可信度評估。論文指出多模態融合雖能提升平均表現，但可信度（校準度、對抗性穩健度）並未隨之同步提升，形成「表現提升 vs 可信度落後」的落差，呼應醫療 AI 部署的核心痛點。

## 為何屬「新領域」
多模態病理/癌症基礎模型的可信度評測，在 workspace 既有題庫（daily-topics/weekly-focus/papers）與 NEW-DOMAINS 既探勘領域紀錄中關鍵詞命中皆為 0，屬完全未觸及的生物醫療 AI 子領域。

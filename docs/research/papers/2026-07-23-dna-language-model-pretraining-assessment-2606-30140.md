---
url: "https://arxiv.org/abs/2606.30140"
title: "DNA Language Models: An Assessment of Pre-Training for Fine-Tuning Tasks"
archived_date: 2026-07-23
arxiv_id: 2606.3014
authors: ["Romain Karpinsky", "Julien Mozziconacci", "Mickaël Delcey"]
domain: genomic-biological-foundation-models
published_date: 2026-06-29
source_routine: routine-e
---

# DNA Language Models: An Assessment of Pre-Training for Fine-Tuning Tasks

## 摘要 / 核心貢獻
本文（arXiv Quantitative Biology > Genomics 分類）系統性評估 DNA 語言模型的預訓練對下游 fine-tuning 任務的實際貢獻度，比較 transformer-based 與傳統卷積式架構在基因體序列分析任務上的表現。核心發現對領域內「預訓練必然帶來下游增益」的預設提出質疑：部分任務上，預訓練帶來的提升相當有限，甚至不敵針對任務直接訓練的較簡單模型，顯示 DNA 語言模型的預訓練紅利可能存在遞減效應，且高度依賴任務類型與資料規模。

## 為何屬「新領域」
DNA 語言模型預訓練效益的實證評估，與 workspace 現有版圖（agent harness、雲端 FinOps、K8s/Kafka 維運）無內容重疊；核心關鍵詞於既有覆蓋集合與既探勘新領域紀錄命中皆為 0。

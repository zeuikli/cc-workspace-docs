---
url: "https://arxiv.org/abs/2603.11784"
title: "Language Generation with Replay: A Learning-Theoretic View of Model Collapse"
archived_date: 2026-07-31
arxiv_id: 2603.11784
authors: ["Giorgio Racca", "Michal Valko", "Amartya Sanyal"]
domain: model-collapse-recursive-training
published_date: 2026-03-12
source_routine: routine-e
---

# Language Generation with Replay: A Learning-Theoretic View of Model Collapse

## 摘要 / 核心貢獻

本文以學習理論框架研究 model collapse，形式化「replay adversary」——一個把生成器過去輸出重新注入訓練資料流的對手模型。核心發現是分離定理：replay 對不同「生成」概念的威脅程度不同——對 uniform generation（要求覆蓋所有合法輸出）沒有威脅，但對較弱的 non-uniform generation 與 generation-in-the-limit 這兩種較寬鬆的生成保證，replay 可證明地造成能力分離（即模型在這些較弱形式下的生成能力會被自產資料回流破壞）。

這把「模型會不會崩潰」從純粹經驗問題轉為「你要求的是哪一種生成保證」的定義問題：崩潰不是全有全無的現象，而是與具體生成目標的強度掛鉤。論文進一步將理論結果對應到業界既有防護手段（資料清洗、浮水印），並指出這些手段在特定條件下會失效——即當防護只針對「偵測合成內容」而非「保證特定生成強度」時。論文已被 ICML 2026 接受（v1 2026-03，v2 2026-07 修訂）。

## 為何屬「新領域」

Workspace 既有覆蓋的 machine-unlearning（2026-07-03，主動移除已學知識）與剛被 Routine E 本輪排除的 continual learning 候選（跨任務知識更新經濟學）皆非本文機制：本文談的是「生成保證的強度」在自產資料回流下如何被分離破壞，這是資料源頭純度與生成目標定義的問題，workspace 全庫對 `replay adversary`、`spectral characterization` 等本領域核心術語 0 命中。

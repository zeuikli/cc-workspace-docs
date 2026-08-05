---
url: "https://arxiv.org/abs/2607.17043"
title: "Learning from Synthetic Data without Model Collapse in Iterative Instruction Tuning"
archived_date: 2026-07-31
arxiv_id: 2607.17043
authors: ["Xiaonan Luo", "Yue Huang", "Kehan Guo", "Ping He", "Chuan Zou", "Ting Hua", "Xiangliang Zhang"]
domain: model-collapse-recursive-training
published_date: 2026-07-19
source_routine: routine-e
---

# Learning from Synthetic Data without Model Collapse in Iterative Instruction Tuning

## 摘要 / 核心貢獻

本文處理語言模型在遞增比例合成資料上訓練導致的 model collapse，核心觀察是：崩潰不只是單純的整體效能下降，而會呈現「能力極化（polarization of competence）」——合成訓練資料會強化模型本來就強的能力，同時讓本來就弱的能力進一步退化。這把 model collapse 從單一純量指標問題重新描述為能力分佈形狀的問題。

作者提出 KITE（Knowledge-boundary Instruction Tuning via Exploration），一個結合「失敗引導的資料生成」與「邊界感知的不確定性篩選」的兩階段方法：優先在模型現有失敗處取樣，並用不確定性篩選過濾低價值合成樣本。在多個資料集與開源語言模型上的測試顯示，相較其他合成資料訓練方法，KITE 展現更一致的改善，對「每一代都該超越前一代」的迭代式模型開發特別有價值。

## 為何屬「新領域」

本文的「能力極化」現象刻畫與 KITE 的失敗引導/邊界篩選配方是本次收錄三篇中最貼近實務配方層的一篇，與 workspace 既有覆蓋（continual learning 候選已被本輪排除、machine-unlearning）機制不同——本文談的是合成資料比例遞增下的資料品質退化與應對配方，非知識更新或刻意遺忘。`polarization of competence`／`KITE` 於全庫 0 命中。

---
url: "https://arxiv.org/abs/2605.01735"
title: "Less is More: Geometric Unlearning for LLMs with Minimal Data Disclosure"
archived_date: 2026-07-03
arxiv_id: 2605.01735
authors: ["Chenchen Tan", "Xinghao Li", "Shujie Cui", "Youyang Qu", "Cunjian Chen", "Longxiang Gao"]
domain: machine-unlearning
published_date: 2026-05-28
source_routine: routine-e
---

# Less is More: Geometric Unlearning for LLMs with Minimal Data Disclosure

## 摘要 / 核心貢獻

因應隱私與治理法規（如「被遺忘權」），LLM 需支援訓練後選擇性移除特定內容
（抑制某實體/主題資訊，同時保留模型整體效用）。本文提出 Geometric Unlearning (GU)：
直接操作模型 prompt-conditioned 隱藏狀態，不需存取原始訓練語料，
從少量「安全參考 prompt」蒸餾出一個緊緻的低秩 safe-behavior 子空間。
在 ToFU 與 UnlearnPII 兩個隱私導向 unlearning benchmark 上，
GU 以最少合成資料達成強力的目標抑制效果，且對非目標效能影響極小。

Machine unlearning（機器卸學習）是 AI 治理/合規的新興技術支柱：
如何在不重新訓練整個模型的前提下，讓模型「遺忘」特定資料點的影響，
直接對應 GDPR 被遺忘權、版權移除、有害記憶抹除等法規與安全需求。

## 為何屬「新領域」

Workspace 現有 security-hygiene / compliance 相關規則聚焦憑證/輸入驗證等傳統資安範疇，
`unlearn` 關鍵詞在既有覆蓋集合命中 0 次 —— machine unlearning 作為「模型層級的資料刪除機制」
是完全未觸及的 AI 治理技術領域，與 workspace 既有的合規/資安紀律有潛在互補關係。

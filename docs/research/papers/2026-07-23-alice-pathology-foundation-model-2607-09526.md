---
url: "https://arxiv.org/abs/2607.09526"
title: "ALICE: Learning a General-Purpose Pathology Foundation Model from Vision, Vision-Language, and Slide-Level Experts"
archived_date: 2026-07-23
arxiv_id: 2607.09526
authors: ["Jiawen Li", "Tian Guan", "Huijuan Shi", "Xitong Ling", "Mingxi Fu", "Anjia Han", "Chao He", "Yonghong He"]
domain: genomic-biological-foundation-models
published_date: 2026-07-10
source_routine: routine-e
---

# ALICE: Learning a General-Purpose Pathology Foundation Model from Vision, Vision-Language, and Slide-Level Experts

## 摘要 / 核心貢獻
ALICE 提出一個通用病理基礎模型，訓練策略融合三種「專家」來源：純視覺（vision）、視覺-語言（vision-language）、以及切片層級（slide-level）專家模型，目標是讓單一基礎模型同時具備細胞/組織層級的視覺辨識能力與切片層級的整體診斷推理能力。論文的核心論點是：既有病理基礎模型多半只針對單一粒度（patch-level 或 slide-level）優化，導致模型在跨粒度任務（例如「先定位可疑區域再給出切片層級診斷」）上表現受限；ALICE 透過多專家知識蒸餾/融合的訓練框架，於多個病理下游任務（分類、分割、切片級預後）上取得較單一粒度基線更一致的表現。

## 為何屬「新領域」
病理全切片影像的通用基礎模型訓練框架，屬生物醫療影像 AI 子領域，與 workspace 既有 harness/agent/FinOps 研究焦點無重疊；關鍵詞於既有覆蓋集合與 NEW-DOMAINS 既探勘領域紀錄命中皆為 0。

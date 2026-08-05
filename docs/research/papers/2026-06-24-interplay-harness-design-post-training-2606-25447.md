---
url: "https://arxiv.org/abs/2606.25447"
title: "The Interplay of Harness Design and Post-Training in LLM Agents"
archived_date: 2026-07-18
arxiv_id: 2606.25447
authors: ["Kyungmin Kim", "Youngbin Choi", "Seoyeon Lee", "Suhyeon Jun", "Dongwoo Kim", "Sangdon Park"]
pdf_path: pdfs/2606.25447.pdf
published_date: 2026-06-24
---

# The Interplay of Harness Design and Post-Training in LLM Agents

**Authors**: Kyungmin Kim, Youngbin Choi, Seoyeon Lee, Suhyeon Jun, Dongwoo Kim, Sangdon Park
**Published**: June 2026
**Source**: https://arxiv.org/abs/2606.25447
**arXiv ID**: 2606.25447
**Categories**: Machine Learning (cs.LG); Computation and Language (cs.CL)
**PDF**: [research/papers/pdfs/2606.25447.pdf](https://arxiv.org/abs/2606.25447)

---

## Abstract

Tool-integrated LLM agents operate within scaffolding that determines which tools are exposed, how they are described, and what auxiliary information accompanies each per-step observation. The researchers examine how harness design influences post-training performance. They extend the ALFWorld benchmark to treat harness design as a controllable dimension and evaluate performance under task and tool environment shifts. Their findings demonstrate that harness-aware post-training not only improves in-distribution performance but also enables agents to robustly adapt to OOD settings. The work reveals significant performance degradation when using minimally-engineered harnesses under substantial tool environment shifts, emphasizing the necessity of considering harness design during agent post-training processes.

---

## Core Thesis

- 把「harness 設計」當作可控變因（哪些工具暴露、描述方式、每步觀察附帶的輔助資訊），並延伸 ALFWorld benchmark 系統性測試其對 post-training 效果的影響。
- 發現 harness-aware post-training 不只改善 in-distribution 表現，也讓 agent 在工具環境分佈偏移（OOD）下更穩健；反之，minimal-engineered harness 在工具環境大幅變動時效能顯著下降。
- 隱含結論：模型能力與 harness 設計是**共同演化**變因，訓練階段忽略 harness 設計會低估／高估真實泛化能力。
- **Workspace 關聯**：呼應本庫既有 Harness Engineering 主題（如 HarnessX、Scaling-Harness）——harness 不是訓練後的外掛，而是與模型能力共同決定泛化上限的一階設計變數；對 `model-profiles.md` 換模型世代時「規則需重審」的立場提供額外實證支持。

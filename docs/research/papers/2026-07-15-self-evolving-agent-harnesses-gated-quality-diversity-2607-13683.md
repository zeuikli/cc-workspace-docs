---
url: "https://arxiv.org/abs/2607.13683"
title: "Self-Evolving Agent Harnesses via Gated Semantic Quality-Diversity"
archived_date: 2026-07-18
arxiv_id: 2607.13683
authors: ["Xiaotian Luo", "Fengxingyu Wang", "Chuanrui Hu", "Dizhan Xue", "Yafeng Deng"]
pdf_path: pdfs/2607.13683.pdf
published_date: 2026-07-15
---

# Self-Evolving Agent Harnesses via Gated Semantic Quality-Diversity

**Authors**: Xiaotian Luo, Fengxingyu Wang, Chuanrui Hu, Dizhan Xue, Yafeng Deng
**Published**: July 2026
**Source**: https://arxiv.org/abs/2607.13683
**arXiv ID**: 2607.13683
**Categories**: Computer Science > Computation and Language (cs.CL)
**PDF**: [research/papers/pdfs/2607.13683.pdf](https://arxiv.org/abs/2607.13683)

---

## Abstract

An LLM agent's real-task performance is shaped as much by the harness around its model as by the frozen model itself: its prompts, injected knowledge, runtime control, and configuration. In deployment the harness is often the only lever available, so improving it automatically is the natural way to raise performance without touching the weights. The hard part is not generating changes but knowing which one truly helped. Self-generated feedback is noisy, and an apparent gain can be a measurement artifact or an edit that merely overfits the tasks it was tuned on. We present a self-evolving agent-harness framework that separates proposing changes from crediting them: a language model diagnoses failures and proposes patches, while all sampling, measurement, and significance testing are owned by deterministic code, so every credited improvement is trustworthy by construction. Patches populate a gated, categorical quality-diversity archive (GSME) keyed on the (WHERE x WHY) pathology an edit addresses rather than the tasks it fixes, an anti-overfitting inductive bias; generalization is measured on a sealed test scored only after evolution. Across seven domains with a frozen open-weight model, the harness is train-selected and scored once on a sealed test; its credited gains there are +9 to +15.5pp and retain 86-147% of the training gain, evidence they generalize rather than overfit. The winning patch tracks the model's dominant pathology, not its size or family: changing the model can change the pathology and the patch, while the same pathology-to-patch match recurs across two model families. What transfers is the diagnose-and-credit loop, not any specific harness.

---

## Core Thesis

- 核心設計：把「提出變更」（LLM 判斷）與「認證變更」（確定性程式碼做取樣/測量/顯著性檢定）嚴格分離——LLM 只診斷失敗並提案 patch，是否真的有效由機械統計驗證，避免自報成功的測量假象。
- 用 gated categorical quality-diversity archive（GSME）以「(WHERE x WHY) 病理類型」而非「修了哪些任務」為 key，作為抗過擬合的歸納偏誤；泛化能力只在演化結束後於 sealed test 評一次分。
- 七個 domain 上實測：credited gain +9~15.5pp，且保留 86–147% 的訓練期增益，證明是真泛化而非過擬合；勝出的 patch 追蹤模型的主要病理類型而非模型大小/家族——換模型會換病理與 patch，但「診斷→認證」迴圈本身可遷移。
- **Workspace 關聯**：與 core.md 公理「判斷 vs 決定」幾乎逐字對應（LLM 判斷、確定性程式碼決定）；sealed-test-after-evolution 的做法直接印證同批次 2607.12227 對 harness evolution 評測方法論的批評，是該問題的一個正面解法範例，可供 `/autoload-evolution` 或 `harness-meta:self-audit` 未來設計「驗證後才記入」機制參考。

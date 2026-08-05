---
url: "https://arxiv.org/abs/2601.22305"
title: "BayesFlow: A Probability Inference Framework for Meta-Agent Assisted Workflow Generation"
archived_date: 2026-07-18
arxiv_id: 2601.22305
authors: ["Bo Yuan", "Yun Zhou", "Zhichao Xu", "Kiran Ramnath", "Aosong Feng", "Balasubramaniam Srinivasan"]
pdf_path: pdfs/2601.22305.pdf
published_date: 2026-01-29
---

# BayesFlow: A Probability Inference Framework for Meta-Agent Assisted Workflow Generation

**Authors**: Bo Yuan, Yun Zhou, Zhichao Xu, Kiran Ramnath, Aosong Feng, Balasubramaniam Srinivasan
**Published**: January 2026
**Source**: https://arxiv.org/abs/2601.22305
**arXiv ID**: 2601.22305
**Categories**: Computer Science > Machine Learning (cs.LG)
**PDF**: [research/papers/pdfs/2601.22305.pdf](https://arxiv.org/abs/2601.22305)

---

## Abstract

The research addresses automatic workflow generation—synthesizing sequences of LLM calls, tool invocations, and processing steps for complex tasks. Rather than treating this as a pure optimization problem, the authors reframe workflow generation as Bayesian inference over a posterior distribution on workflows. They introduce Bayesian Workflow Generation (BWG), a sampling framework that builds workflows step-by-step using parallel look-ahead rollouts for importance weighting. The instantiation called BayesFlow requires no training and achieved improvements of up to 9 percentage points over SOTA workflow generation baselines and by up to 65 percentage points over zero-shot prompting across six benchmark datasets. The authors provide theoretical convergence guarantees and have committed to releasing code.

---

## Core Thesis

- 把自動 workflow 生成（LLM call、工具呼叫、處理步驟序列的合成）從純最佳化問題重新框架為「workflow 後驗分佈上的貝氏推論」，而非搜尋單一最優解。
- 提出 Bayesian Workflow Generation (BWG)：用平行 look-ahead rollout 做重要性加權，逐步取樣建構 workflow；具體實作 BayesFlow 免訓練即可用。
- 六個 benchmark 上，相較 SOTA workflow 生成基準最多提升 9 個百分點，相較 zero-shot prompting 最多提升 65 個百分點；並提供理論收斂保證，程式碼承諾開源。
- **Workspace 關聯**：與本庫既有 Loop/Workflow Engineering 收錄論文（sew-2505-18646、workflow-opt-survey-2603-22386）互補——提供「用貝氏推論取代搜尋/RL」的另一種 workflow 生成理論視角，免訓練特性對成本敏感場景（如 `/pilot cost` 檔位任務規劃）有參考價值。

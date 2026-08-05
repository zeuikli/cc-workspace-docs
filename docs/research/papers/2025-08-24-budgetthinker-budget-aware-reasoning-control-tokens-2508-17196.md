---
url: "https://arxiv.org/abs/2508.17196"
title: "BudgetThinker: Empowering Budget-aware LLM Reasoning with Control Tokens"
archived_date: 2026-07-17
arxiv_id: 2508.17196
authors: ["Hao Wen", "Xinrui Wu", "Yi Sun", "Feifei Zhang", "Liye Chen", "Jie Wang", "Yunxin Liu", "Yunhao Liu", "Ya-Qin Zhang", "Yuanchun Li"]
domains: [cs.LG, cs.AI]
html: "https://arxiv.org/html/2508.17196v1"
pdf_path: pdfs/2508.17196.pdf
published_date: 2025-08-24
---

# BudgetThinker: Empowering Budget-aware LLM Reasoning with Control Tokens

**Authors**: Hao Wen, Xinrui Wu, Yi Sun, Feifei Zhang, Liye Chen, Jie Wang, Yunxin Liu, Yunhao Liu, Ya-Qin Zhang, Yuanchun Li
**Published**: August 24, 2025
**Source**: https://arxiv.org/abs/2508.17196 · [HTML](https://arxiv.org/html/2508.17196v1)
**arXiv ID**: 2508.17196
**Categories**: cs.LG, cs.AI
**PDF**: [research/papers/pdfs/2508.17196.pdf](https://arxiv.org/abs/2508.17196)

---

## Abstract (quoted)

> Recent advancements in Large Language Models (LLMs) have leveraged increased test-time computation to enhance reasoning capabilities, a strategy that, while effective, incurs significant latency and resource costs, limiting their applicability in real-world time-constrained or cost-sensitive scenarios. This paper introduces BudgetThinker, a novel framework designed to empower LLMs with budget-aware reasoning, enabling precise control over the length of their thought processes. We propose a methodology that periodically inserts special control tokens during inference to continuously inform the model of its remaining token budget. This approach is coupled with a comprehensive two-stage training pipeline, beginning with Supervised Fine-Tuning (SFT) to familiarize the model with budget constraints, followed by a curriculum-based Reinforcement Learning (RL) phase that utilizes a length-aware reward function to optimize for both accuracy and budget adherence. We demonstrate that BudgetThinker significantly surpasses strong baselines in maintaining performance across a variety of reasoning budgets on challenging mathematical benchmarks. Our method provides a scalable and effective solution for developing efficient and controllable LLM reasoning, making advanced models more practical for deployment in resource-constrained and real-time environments.

---

## 結構化摘要

### 核心貢獻

- 推理中週期性插入 control token 持續告知模型「剩餘 token budget」——把 budget 從 prompt 一次性提示升級為 inference 過程中的持續信號
- 兩階段訓練：SFT 熟悉 budget 約束 → curriculum RL（length-aware reward）同時優化 accuracy 與 budget adherence

### 關鍵結果

- 數學 benchmark 上跨多種 reasoning budget 均顯著優於 strong baselines；具體數字未取得（abstract 未含）

### 限制

- 需訓練介入（SFT+RL），閉源 API 模型無法直接套用
- 驗證集中於數學推理，agent/長文任務泛化未報

---

## Workspace 關聯（評估，非既成結論）

- 與 2412.18547 構成 token budget 研究線的 prompt 端 vs 訓練端對照；對 `.claude/skills/output-compress` 而言可落地的僅「持續回饋剩餘預算」的介面概念（如 checkpoint 中注入剩餘 budget 提示）。
- 「budget adherence 用機械 reward 驗證而非模型自報」與機械失真閘的零 LLM 自評原則同構。⚠️ 方法本體屬訓練側，workspace 不落地。

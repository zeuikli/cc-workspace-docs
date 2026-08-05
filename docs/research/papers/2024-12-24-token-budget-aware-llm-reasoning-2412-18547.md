---
url: "https://arxiv.org/abs/2412.18547"
title: "Token-Budget-Aware LLM Reasoning"
archived_date: 2026-07-17
arxiv_id: 2412.18547
authors: ["Tingxu Han", "Zhenting Wang", "Chunrong Fang", "Shiyu Zhao", "Shiqing Ma", "Zhenyu Chen"]
domains: [cs.CL, cs.AI, cs.LG]
html: "https://arxiv.org/html/2412.18547v1"
pdf_path: pdfs/2412.18547.pdf
published_date: 2024-12-24
---

# Token-Budget-Aware LLM Reasoning

**Authors**: Tingxu Han, Zhenting Wang, Chunrong Fang, Shiyu Zhao, Shiqing Ma, Zhenyu Chen
**Published**: December 24, 2024
**Source**: https://arxiv.org/abs/2412.18547 · [HTML](https://arxiv.org/html/2412.18547v1)
**arXiv ID**: 2412.18547
**Categories**: cs.CL, cs.AI, cs.LG
**PDF**: [research/papers/pdfs/2412.18547.pdf](https://arxiv.org/abs/2412.18547)

---

## Abstract (quoted)

> Reasoning is critical for large language models (LLMs) to excel in a wide range of tasks. While methods like Chain-of-Thought (CoT) reasoning enhance LLM performance by decomposing problems into intermediate steps, they also incur significant overhead in token usage, leading to increased costs. We find that the reasoning process of current LLMs is unnecessarily lengthy and it can be compressed by including a reasonable token budget in the prompt, but the choice of token budget plays a crucial role in the actual compression effectiveness. We then propose a token-budget-aware LLM reasoning framework that dynamically adjusts the number of reasoning tokens based on the reasoning complexity of each problem. Experiments show that our method effectively reduces token costs in CoT reasoning with only a slight performance reduction, offering a practical solution to balance efficiency and accuracy in LLM reasoning.

---

## 結構化摘要

### 核心貢獻

- 實證 CoT 推理過程「不必要地冗長」：在 prompt 中給合理 token budget 即可壓縮，且 budget 數值選擇是壓縮成效關鍵
- 提出 TALE（token-budget-aware）框架：依每題推理複雜度動態估算並注入 budget

### 關鍵結果

- 顯著降低 CoT token 成本、僅輕微效能下降；具體百分比未取得（abstract 未含）

### 限制

- budget 估算本身需要一次額外判斷；估太低會截斷關鍵推理步驟
- 2024 年模型世代的結果，對現代原生 reasoning 模型（有 effort 參數）的遷移性未知

---

## Workspace 關聯（評估，非既成結論）

- 支持 `.claude/skills/output-compress` 的檔位上限與 model-profiles「effort 先於 model」原則：token budget 是與檔位獨立的第一調節軸。
- 「budget 選擇決定壓縮成效」印證分級（lite/full/ultra）而非單一開關的設計；budget 由確定性規則指定、非 LLM 自選，契合「判斷 vs 決定」公理。

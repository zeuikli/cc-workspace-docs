---
url: "https://arxiv.org/abs/2503.19114"
title: "Understanding and Improving Information Preservation in Prompt Compression for LLMs"
archived_date: 2026-07-17
arxiv_id: 2503.19114
authors: ["Weronika Łajewska", "Momchil Hardalov", "Laura Aina", "Neha Anna John", "Hang Su", "Lluís Màrquez"]
domains: [cs.CL, cs.IR, cs.LG]
html: "https://arxiv.org/html/2503.19114v1"
pdf_path: pdfs/2503.19114.pdf
published_date: 2025-03-24
---

# Understanding and Improving Information Preservation in Prompt Compression for LLMs

**Authors**: Weronika Łajewska, Momchil Hardalov, Laura Aina, Neha Anna John, Hang Su, Lluís Màrquez
**Published**: March 24, 2025
**Source**: https://arxiv.org/abs/2503.19114 · [HTML](https://arxiv.org/html/2503.19114v1)
**arXiv ID**: 2503.19114
**Categories**: cs.CL, cs.IR, cs.LG
**PDF**: [research/papers/pdfs/2503.19114.pdf](https://arxiv.org/abs/2503.19114)

---

## Abstract (quoted)

> Recent advancements in large language models (LLMs) have enabled their successful application to a broad range of tasks. However, in information-intensive tasks, the prompt length can grow fast, leading to increased computational requirements, performance degradation, and induced biases from irrelevant or redundant information. Recently, various prompt compression techniques have been introduced to optimize the trade-off between reducing input length and retaining performance. We propose a holistic evaluation framework that allows for in-depth analysis of prompt compression methods. We focus on three key aspects, besides compression ratio: (i) downstream task performance, (ii) grounding in the input context, and (iii) information preservation. Using our framework, we analyze state-of-the-art soft and hard compression methods and show that some fail to preserve key details from the original prompt, limiting performance on complex tasks. By identifying these limitations, we are able to improve one soft prompting method by controlling compression granularity, achieving up to +23% in downstream performance, +8 BERTScore points in grounding, and 2.7x more entities preserved in compression. Ultimately, we find that the best effectiveness/compression rate trade-off is achieved with soft prompting combined with sequence-level training.

---

## 結構化摘要

### 核心貢獻

- 提出 prompt compression 的整體評估框架：壓縮率之外加三軸——downstream 表現、對輸入 context 的 grounding、資訊保留
- 分析 SOTA soft/hard 壓縮方法，證明部分方法無法保留原 prompt 關鍵細節，複雜任務表現受限
- 以「控制壓縮 granularity」改進一個 soft prompting 方法

### 關鍵結果

- 改進後：downstream 表現最高 +23%、grounding +8 BERTScore、entity 保留量 2.7×
- 最佳 effectiveness/compression 權衡 = soft prompting + sequence-level training

### 限制

- 評估集中於特定 soft/hard 壓縮方法組合，abstract 未列覆蓋模型與任務範圍
- soft prompting 改進需訓練介入，對閉源 API 模型不可直接套用

---

## Workspace 關聯（評估，非既成結論）

- 三軸評估框架（performance / grounding / preservation）可作為 `.claude/skills/output-compress` 機械失真閘的量測維度參考——entity 保留計數是可機械化的零 LLM 自評指標，契合「確定性程序做決定」公理。
- 「壓縮 granularity 控制」對應 output-compress 的分級壓縮（lite/full/ultra）設計：granularity 是保真的第一調節旋鈕。⚠️ soft prompting 屬訓練側方法，workspace 僅能借鑑其評估框架，不能落地其方法本體。

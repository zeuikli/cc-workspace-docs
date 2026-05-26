---
title: "Step-Back Profiling: Distilling User History for Personalized Scientific Writing"
authors: "Xiangru Tang, Xingyao Zhang, Yanjun Shao, Jie Wu, Yilun Zhao, Arman Cohan, Ming Gong, Dongmei Zhang, Mark Gerstein"
published: "2024-06-20"
source: "https://arxiv.org/abs/2406.14275"
venue: "arXiv"
arxiv_id: "2406.14275"
---

# Step-Back Profiling: Distilling User History for Personalized Scientific Writing

**Authors**: Xiangru Tang, Xingyao Zhang, Yanjun Shao, Jie Wu, Yilun Zhao, Arman Cohan, Ming Gong, Dongmei Zhang, Mark Gerstein

**Published**: June 20, 2024 (revised July 11, 2024)

**Source**: https://arxiv.org/abs/2406.14275

---

## Abstract

The researchers present a method to enhance language model personalization by condensing user history into focused profiles capturing key traits and preferences. They developed a Personalized Scientific Writing dataset for studying multi-user adaptation, requiring models to compose academic papers for diverse author groups. Their approach demonstrated substantial improvements, achieving gains of "up to 3.6 points on the general personalization benchmark (LaMP)" across seven tasks. The methodology validates how effectively user characteristics can be extracted for collaborative writing applications.

---

## Overview

This research paper introduces **Step-back Profiling**, a training-free framework for personalizing large language models by condensing user histories into concise profile representations. The authors also present the **Personalized Scientific Writing (PSW) dataset** to evaluate multi-user personalization in collaborative research contexts.

---

## Key Contributions

### Core Method

Step-back Profiling distills individual user histories into "gist" representations capturing high-level traits and preferences, enabling efficient multi-user personalization without extensive computation.

### New Dataset

The PSW benchmark contains research papers with multiple authors, featuring five tasks:
- UP-0: Research interest generation
- PSW-1 through PSW-4: Topic, question, abstract, and title generation

### Performance

The approach achieves 3.6-point improvements on LaMP benchmarks and demonstrates superior performance in collaborative writing scenarios.

---

## Technical Approach

The procedure involves four steps:

1. **User Profile Gisting**: Compress each user's history using an LLM-based abstraction function
2. **Multi-User Profile Concatenation**: Combine individual profiles preserving author order
3. **Retrieval-Augmented Generation** (optional): Retrieve relevant historical snippets
4. **Personalized Output Generation**: Condition LLM on augmented input and profiles

---

## Results

### LaMP Tasks
- 12.6% accuracy gains and 42.5% MAE reduction on classification tasks
- 15.2% ROUGE-1 and 19.5% ROUGE-L improvements on generation tasks

### PSW Tasks
- Multi-author setting consistently outperforms single-author and zero-shot baselines across all metrics

---

## Notable Findings

Author order significantly impacts performance—preserving original author sequence maintains expertise representation better than random shuffling. User profiles prove essential, with profile removal causing substantial performance degradation.

---

## Significance

This work addresses a significant challenge in making large language models more responsive to individual needs within specialized domains. The dataset and implementation code are publicly available, supporting reproducibility and further research in personalized AI systems.

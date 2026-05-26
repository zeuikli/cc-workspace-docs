---
title: "RouteLLM: Learning to Route LLMs with Preference Data"
authors: "Isaac Sim, Shuwen Sun, and others"
published: "2024-06-20"
source: "https://arxiv.org/abs/2406.18665"
venue: "arXiv"
arxiv_id: "2406.18665"
---

# RouteLLM: Learning to Route LLMs with Preference Data

**Authors**: Isaac Sim, Shuwen Sun, and others

**Published**: June 20, 2024

**Source**: https://arxiv.org/abs/2406.18665

---

## Abstract

This research paper introduces RouteLLM, a framework for training router models that dynamically select between strong (expensive, high-quality) and weak (cheap, lower-quality) LLMs during inference. The key innovation is leveraging human preference data to achieve significant cost savings while maintaining response quality.

---

## Core Problem & Solution

The paper addresses a fundamental challenge in LLM deployment: balancing performance against cost. Rather than routing all queries to expensive models or sacrificing quality with cheap ones, RouteLLM learns which queries genuinely need the stronger model.

The framework uses two components:
1. **Win Prediction Model**: Estimates probability that a strong model outperforms a weak model for a given query
2. **Cost Threshold (α)**: A parameter controlling the quality-cost tradeoff by determining routing decisions

---

## Key Contributions

### Data & Training Approaches

The researchers built training datasets from:
- 80K human preferences from Chatbot Arena
- Golden-labeled datasets (MMLU validation split)
- GPT-4 judge-labeled datasets (~120K samples)

They evaluated four router architectures: similarity-weighted ranking, matrix factorization, BERT classifier, and causal LLM classifier.

### Performance Results

The routers achieved remarkable efficiency gains. As stated in their findings: "routers achieve cost savings of up to 3.66x" while maintaining quality comparable to using only expensive models.

On MT Bench specifically, their best routers reduced GPT-4 calls by ~75% while recovering 95% of GPT-4's performance.

---

## Notable Findings

1. **Data Augmentation Matters**: Routers trained only on arena data performed poorly on specialized benchmarks (MMLU, GSM8K), but augmentation with domain-specific data dramatically improved performance.

2. **Generalization Across Models**: A single trained router maintained strong performance when routing between different model pairs (Claude 3, Llama 3.1) without retraining—crucial for real-world deployment.

3. **Benchmark-Dataset Similarity**: They introduced a quantitative similarity metric showing "strong correlation between similarity scores and router performance," helping explain performance variations across benchmarks.

4. **Minimal Overhead**: Routing adds less than 0.4% cost overhead compared to GPT-4 generation.

---

## Methodology Highlights

The similarity-weighted ranking approach adapted Bradley-Terry models from ranking theory, while matrix factorization techniques treated routing as a recommendation system problem. This diversity of approaches showed that simpler, parameter-efficient methods sometimes outperformed larger neural classifiers in low-data regimes.

---

## Limitations & Future Work

The authors acknowledge this work focuses on binary routing. Extending to N-way routing among multiple models remains an open challenge, as does understanding real-world query distributions that may differ from academic benchmarks.

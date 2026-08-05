---
url: "https://arxiv.org/abs/2408.03314"
title: "Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters"
archived_date: 2026-06-09
arxiv_id: 2408.03314
authors: ["Charlie Snell", "Jaehoon Lee", "Kelvin Xu", "Aviral Kumar"]
pdf_path: pdfs/2408.03314.pdf
published_date: 2024-08-06
---

# Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters

**Authors:** Charlie Snell, Jaehoon Lee, Kelvin Xu, Aviral Kumar
**Year:** 2024
**Submitted:** August 6, 2024
**Venue:** arXiv preprint
**ArXiv:** https://arxiv.org/abs/2408.03314

---

## Abstract

Enabling LLMs to improve their outputs by using more test-time computation is a critical step in the development of scalable oversight for AI. Unlike scaling model parameters, where improvements require expensive retraining, test-time compute scaling offers a more flexible path to enhanced performance. We investigate a fundamental question: can a fixed amount of test-time compute meaningfully improve LLM outputs on difficult prompts, without retraining?

We address two primary mechanisms for scaling test-time computation: (1) searching against dense process-based verifier reward models and (2) updating the model's distribution over a blockwise Monte Carlo tree search. Our key finding is that by allocating inference-time computation adaptively based on prompt difficulty, a smaller model can outperform one 14x larger on matched compute budgets — achieving more than 4x higher efficiency on difficult tasks. Crucially, we show that the optimal strategy for scaling test-time compute depends heavily on the difficulty of the prompt: easier problems benefit from best-of-N sampling with verifier re-ranking, while harder problems benefit from iterative refinement via adaptive distribution updates. These findings establish the empirical and theoretical foundation for the test-time compute scaling paradigm as a complement to — and at certain regimes, a replacement for — scaling model parameters.

---

## Key Contributions

- **Compute-optimal inference strategy**: Introduces difficulty-adaptive allocation of test-time compute, achieving more than 4x efficiency gains over fixed-budget baselines.
- **Two complementary scaling mechanisms**: Systematically analyzes process-based verifier reward models (for re-ranking generations) and adaptive distribution updates (for iterative refinement via MCTS-style search).
- **Small-model parity with large models**: Demonstrates that a smaller model with test-time compute can outperform a model 14x larger under matched compute budgets.
- **Difficulty-dependent strategy selection**: Shows that the optimal scaling method depends on prompt complexity — verifier re-ranking for easy prompts, distribution updates for hard prompts.
- **Foundational empirical basis**: Establishes rigorous benchmarks and theoretical framing for test-time compute scaling as a first-class scaling axis alongside parameter count and training data.
- **Implications for model development**: Challenges the assumption that larger base models are always preferable, suggesting that inference-time compute allocation is a viable design axis.

---

## Methodology

The paper investigates two primary mechanisms for scaling test-time compute. The first is **process-based verifier reward models (PRMs)**: a verifier scores intermediate reasoning steps, enabling best-of-N selection where N candidates are generated and the highest-scored is returned. The PRM provides dense step-level feedback rather than only evaluating final answers, allowing the model to identify and favor reasoning chains where each step is well-supported.

The second mechanism is **adaptive distribution updates**, implemented through a blockwise Monte Carlo Tree Search (MCTS) approach. Rather than generating N independent candidates, this approach iteratively refines the model's generation distribution by exploring promising reasoning branches and backtracking from unproductive ones. This sequential approach is particularly suited to problems where the model's initial distribution places low probability on correct solutions.

The core contribution is a **compute-optimal strategy** that selects between these mechanisms based on estimated prompt difficulty. Difficulty is estimated from the model's initial success rate on the prompt. For prompts where the base model has a moderate success rate, best-of-N with PRM re-ranking is most compute-efficient. For very hard prompts (low initial success rate), iterative distribution refinement via MCTS yields better returns. This adaptive allocation is shown to be significantly more efficient than applying either strategy uniformly.

---

## Main Results

- On MATH benchmark tasks, the compute-optimal approach enables a smaller model to match or exceed a model 14x larger in parameter count, under equivalent compute budgets.
- Adaptive allocation achieves more than 4x efficiency improvement over uniform budget allocation baselines.
- Process-based verifier reward models outperform outcome-based (final-answer-only) verification for best-of-N selection across difficulty ranges.
- Difficulty-adaptive strategy selection consistently outperforms using either mechanism alone across the difficulty spectrum.
- Results demonstrate that for a broad class of prompts, scaling test-time compute is a more efficient path to performance improvement than scaling model parameters.

---

## Limitations & Future Work

- Experiments are primarily conducted on mathematical reasoning benchmarks (MATH); generalization to other domains (code, science, open-ended generation) requires further study.
- The compute-optimal strategy requires reliable difficulty estimation, which itself introduces overhead and may be imperfect on out-of-distribution inputs.
- Process reward models require training data with step-level labels, which are expensive to collect; scaling PRM quality is a separate challenge.
- The comparison between test-time compute scaling and training-time scaling assumes fixed model weights; joint optimization across both axes is unexplored.
- Future work includes extending difficulty-adaptive strategies to non-verifiable tasks, improving PRM training efficiency, and studying the interaction between base model capability and test-time scaling ceiling.

---

## Why This Matters for AI Practitioners

This paper establishes a rigorous framework for **inference-time compute as a design axis** — alongside model size and training data. For practitioners, the key takeaway is that deploying a smaller, cheaper model with adaptive test-time compute can match the output quality of a much larger model at lower overall cost, particularly on structured tasks like math and reasoning. The work directly motivates architectures and serving systems that budget compute dynamically per query rather than statically. It also provides the theoretical grounding for subsequent work on reasoning models (o1, DeepSeek-R1, s1) that leverage extended inference-time computation. PRM-based verification pipelines and MCTS-style search, described here at a foundational level, have since become standard components in advanced reasoning systems.

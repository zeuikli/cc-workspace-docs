---
url: "https://arxiv.org/abs/2501.12948"
title: "DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning"
archived_date: 2026-06-09
arxiv_id: 2501.12948
authors: ["DeepSeek-AI — Daya Guo", "Dejian Yang", "Haowei Zhang", "et al. (200 co-authors)"]
pdf_path: pdfs/2501.12948.pdf
published_date: 2025-01-22
---

# DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning

**Authors:** DeepSeek-AI — Daya Guo, Dejian Yang, Haowei Zhang, et al. (200 co-authors)
**Year:** 2025
**Submitted:** January 22, 2025
**Venue:** Nature, Vol. 645, pp. 633–638 (2025)
**ArXiv:** https://arxiv.org/abs/2501.12948

---

## Abstract

We present DeepSeek-R1, a large language model trained to reason through reinforcement learning (RL), without relying on human-annotated chain-of-thought (CoT) supervision. Our approach incentivizes the model to develop reasoning capabilities emergently, through exposure to verifiable tasks with outcome-based reward signals. Starting from a pre-trained base model, RL training enables the spontaneous emergence of sophisticated reasoning behaviors — including self-reflection, solution verification, hypothesis backtracking, and adaptive strategy selection — which were not explicitly programmed or demonstrated.

DeepSeek-R1 achieves performance matching or exceeding OpenAI o1 on a suite of challenging benchmarks including AIME 2024 (competition mathematics), Codeforces (competitive programming), and a range of STEM reasoning evaluations. We further demonstrate that the extended chain-of-thought reasoning patterns learned by DeepSeek-R1 can be distilled into significantly smaller models, enabling efficient deployment of o1-class reasoning without full-scale RL training. We open-source the model weights and describe our training methodology in full, enabling community replication of o1-class reasoning capabilities.

---

## Key Contributions

- **Pure RL reasoning emergence**: Demonstrates that advanced multi-step reasoning — including self-reflection, backtracking, and verification — can emerge from RL training alone, without human-annotated CoT demonstrations.
- **Outcome-based reward signal**: Uses verifiable task outcomes (mathematical correctness, code execution pass/fail) as reward signals, eliminating the need for expensive human step-level labeling.
- **Benchmark parity with OpenAI o1**: Achieves performance matching or exceeding o1 on AIME 2024 (competition math), Codeforces (competitive coding), and STEM reasoning benchmarks.
- **Knowledge distillation of reasoning**: Shows that long chain-of-thought reasoning patterns from DeepSeek-R1 can be distilled into smaller models (1.5B–70B parameters), yielding efficient o1-class reasoning at reduced cost.
- **Full open-source release**: Publishes model weights and training methodology, enabling broad community replication — the first fully open reproduction of o1-class reasoning capability.
- **Nature publication**: Results published in Nature (Vol. 645, 2025), reflecting independent peer review of the core empirical claims.

---

## Methodology

DeepSeek-R1 is trained via **Group Relative Policy Optimization (GRPO)**, a variant of Proximal Policy Optimization (PPO) adapted for language model training. The training process starts from a pre-trained base model (DeepSeek-V3-Base) and applies RL with verifiable reward signals: for mathematics problems, correctness of the final numerical answer; for code, passing of test cases. No intermediate step-level human labels are used. The model is incentivized purely to produce sequences that lead to correct final outputs.

A critical intermediate stage, **DeepSeek-R1-Zero**, is trained with pure RL from the base model without any supervised fine-tuning warm-up. Analysis of R1-Zero reveals spontaneous emergence of self-verification, reflection, and backtracking behaviors — the model learns to reconsider incorrect intermediate steps and try alternative approaches. This finding demonstrates that reasoning capabilities are latent in the pre-trained base model and can be elicited through RL incentives alone.

The final **DeepSeek-R1** model introduces a cold-start phase with a small amount of curated long-CoT SFT data before RL, which stabilizes early training and improves final performance and readability of reasoning traces. The resulting model generates extended "thinking" sequences — similar in structure to o1's extended reasoning — before producing a final answer. **Knowledge distillation** is performed by using DeepSeek-R1's reasoning traces as synthetic SFT data for training smaller models (Qwen and Llama base models at 1.5B, 7B, 8B, 14B, 32B, 70B scales), achieving strong performance without RL training at smaller scales.

---

## Main Results

- **AIME 2024**: DeepSeek-R1 achieves 79.8% pass@1, comparable to OpenAI o1 (79.2%).
- **Codeforces**: Reaches the 96.3rd percentile among human competitors, matching o1 performance.
- **MATH-500**: Achieves 97.3% accuracy, exceeding o1 (96.4%).
- **MMLU**: 90.8% accuracy, competitive with top frontier models.
- **Distilled models**: DeepSeek-R1-Distill-Qwen-32B achieves 72.6% on AIME 2024, surpassing o1-mini; the 7B distilled model outperforms QwQ-32B-Preview.
- **DeepSeek-R1-Zero** (pure RL, no SFT): achieves 71.0% on AIME 2024, demonstrating that extended reasoning emerges from RL alone.

---

## Limitations & Future Work

- Language mixing: early RL training sometimes produces mixed-language outputs; the cold-start SFT phase mitigates but does not fully eliminate this.
- Function calling and multi-turn conversation capabilities are weaker than specialized instruction-tuned models; reasoning-focused training trades off against instruction-following breadth.
- Software engineering benchmarks (SWE-bench) show weaker relative performance compared to math/code competition tasks.
- The RL training process is computationally expensive; training recipes for reproducing R1-scale RL at lower cost remain an open problem.
- Future directions include extending verifiable reward signals to domains beyond math and code (e.g., science, law), and improving multi-modal reasoning.

---

## Why This Matters for AI Practitioners

DeepSeek-R1 is the most significant open-source development in inference-time reasoning to date. Its core finding — that o1-class reasoning emerges from RL on verifiable tasks without human CoT annotation — fundamentally changes the economics of training reasoning models. For practitioners, the open model weights enable direct deployment and fine-tuning of o1-class reasoning without API dependency. The distillation results are particularly actionable: a 7B or 32B model trained on R1's reasoning traces achieves performance that would have required a 70B+ model under standard SFT. The paper also validates the test-time compute scaling paradigm: R1's extended chain-of-thought generation is itself a form of inference-time compute allocation, confirming that longer reasoning traces correlate with higher accuracy on hard problems.

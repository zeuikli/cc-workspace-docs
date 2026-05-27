---
title: "HeavySkill: Heavy Thinking as the Inner Skill in Agentic Harness"
authors: Jianing Wang, Linsen Guo, Zhengyu Chen, Qi Guo, Hongyu Zang, Wenjie Shi, Haoxiang Ma, Xiangyu Xi, Xiaoyu Li, Wei Wang, Xunliang Cai
published: 2026-05-04
source: "https://arxiv.org/abs/2605.02396"
---

# HeavySkill: Heavy Thinking as the Inner Skill in Agentic Harness

**Authors**: Jianing Wang, Linsen Guo, Zhengyu Chen, Qi Guo, Hongyu Zang, Wenjie Shi, Haoxiang Ma, Xiangyu Xi, Xiaoyu Li, Wei Wang, Xunliang Cai
**Published**: May 4, 2026
**Source**: https://arxiv.org/abs/2605.02396
**arXiv ID**: 2605.02396
**Categories**: cs.AI
**Length**: 18 pages, 10 figures

---

## Abstract

HeavySkill proposes that **heavy/deep thinking is both a minimal execution unit in orchestration harness AND an inner skill internalized within the model** (not just an external orchestration layer). The two-stage pipeline (parallel reasoning → sequential deliberation) outperforms Best-of-N voting, with strong LLMs approaching theoretical Pass@K limits. The workflow is portable across any agent framework without modification.

---

## Core Thesis

Heavy thinking is not just an external orchestration mechanism—it is an **internalizable skill** that can be learned, scaled, and deployed independently of fragile coordination layers.

Two unified views:
1. **Orchestration view**: Minimal execution unit schedulable by any agentic harness
2. **Internalization view**: Parameterized skill embedded in model weights via RL

---

## Methodology

### Two-Stage Pipeline

**Stage 1 — Parallel Reasoning**: Generate K independent trajectories: `T_πθ(q,K) = {y₁, ..., yK}`

**Stage 2 — Sequential Deliberation**: Second LLM `πφ` processes serialized memory cache `xc` (pruned + shuffled trajectories) → produces synthesized output.

**Iterative Deliberation** (N iterations): At iteration t, cache modified by concatenating prior deliberation outputs: `C(x^(t)) = T_πφ(x_c^(t-1), K^(t-1)) || x^(t-1)` → recursive refinement.

### Readable Skill for Agentic Harness

Four components of the portable skill:
- **Activation Conditions**: Triggers on complex reasoning tasks
- **Parallel Reasoning Protocol**: Spawns K independent reasoning agents
- **Deliberation Prompt**: Templates guiding critical evaluation and synthesis (not naive concatenation)
- **Output Constraints**: Format requirements

Functions across Claude Code, custom orchestrations, any harness—without modification.

---

## Experiments

### Models Tested

**Closed-weight**: GPT-5-Thinking, Claude 4.5 Thinking, Gemini 3 Pro Preview
**Open-weight**: R1-Distill-Qwen variants, Qwen3, DeepSeek R1, Kimi K2 Thinking, GLM 4.6, DeepSeek V3.2

**Parameters**: Temperature=1.0, Top-p=0.95, K∈{8,16}, K^(1)=4

### Metrics

| Metric | Definition |
|--------|-----------|
| M@K | Mean accuracy across K trajectories |
| P@K | Proportion with ≥1 correct trajectory |
| V@K | Majority voting accuracy |
| HM@K | Mean accuracy after deliberation |
| HP@K | Proportion with ≥1 correct summary |

---

## Key Results

### STEM Tasks (AIME25, BeyondAIME, HMMT25-Feb, GPQA-Diamond)

1. **HM@4 consistently surpasses M@K** across all models and benchmarks — deliberation yields positive gains over baseline trajectory quality

2. **Scaling validated**: Performance improves with increased parallel trajectories (K) and deliberation — "width" (parallel) and "depth" (sequential) function as capability multipliers

3. **Outperforms voting**: Heavy thinking frequently exceeds Vote@K — advantages pronounced on harder benchmarks (BeyondAIME, HMMT, GPQA-Diamond)

4. **Surpasses intrinsic boundaries**: HP@4 exceeds P@K in ~50% of trials with frontier models — deliberation synthesizes cross-trajectory insights to generate correct solutions absent from any single trajectory

### General Reasoning (LiveCodeBench, Arena-Hard, IFEval, IMO)

- **LiveCodeBench**: "GPT-OSS-20B performance surges from 69.7% M@K to 85.5% HM@4"
- **Arena-Hard**: Marginal gains only (subjective tasks less suited)
- **IMO**: GLM 4.6 achieves 86.0% HP@4 vs. 75.1% P@K

**Conclusion**: Heavy thinking excels at correctness-oriented tasks, not preference-oriented tasks.

---

## Further Analysis

### Sequential Deliberation's Revision Capability (10K queries, R1-Distill-Qwen-7B)

- Pass rate <0.5: Heavy thinking corrects ~500 failures while leaving ~1,400 unresolved
- Pass rate >0.5: Success rate exceeds 98% despite ~30 degradations

### Optimal Deliberation Model

Counter-intuitive finding: Qwen2.5-32B-Instruct (weaker independent reasoner) yields expected gains as synthesizer. **Deliberation relies on analysis/synthesis ability, not peak reasoning power.**

### Iterative Deliberation Trade-off

- HM@K consistently improves with more iterations
- HP@K degrades: "subsequent steps susceptible to interference from earlier stages"
- Trade-off between depth and information consistency

### Tool-Use Adaptation (Qwen3-8B/32B, GPT-OSS-20B)

"GPT-OSS-20B achieves 90.0% under heavy thinking vs. 83.3% voting on AIME25" — deliberation effectively leverages tool execution feedback.

---

## RLVR Advancement (Appendix B)

~10% HM@4 improvement in initial 100 training steps. Stability issues at K=16 due to maximum sequence length limitations.

**Trajectory selection**: Max-Answer-Num (voting-based) significantly outperforms random sampling, max-diversity, and max-length approaches.

---

## Workspace Relevance

Directly validates `opus-pilot` **Mechanism #2 (Parallel Hypotheses + Synthesis)**: N=3 parallel candidates → synthesis is the same two-stage pattern. Paper confirms this is superior to Best-of-N selection.

For `haiku-pilot` / escalation gates: if the model has internalized heavy thinking (via RL training), the "escalate to Opus for deep reasoning" gate should account for whether the base model has this capability built in.

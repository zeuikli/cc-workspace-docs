---
title: "OckBench: Measuring the Efficiency of LLM Reasoning"
authors: "Minyang Liu, Weijia Shi, Qiantong Xu, Luke Zettlemoyer, Wen-tau Yih, Sewon Min"
published: 2025-11-07
source: "https://arxiv.org/abs/2511.05722"
---

# OckBench: Measuring the Efficiency of LLM Reasoning

**Authors**: Minyang Liu, Weijia Shi, Qiantong Xu, Luke Zettlemoyer, Wen-tau Yih, Sewon Min
**Published**: November 7, 2025
**Source**: https://arxiv.org/abs/2511.05722
**arXiv ID**: 2511.05722
**Categories**: cs.CL, cs.AI, cs.LG

---

## Abstract

OckBench introduces the **Overthinking Tax** — the counterintuitive finding that smaller reasoning models can be more expensive than larger ones due to excessive token generation. A 7B open-source model is 57% more expensive than a 14B model when total cost (accuracy × token efficiency) is considered. Open-source models generate 5.1× more tokens than proprietary models for equivalent tasks. Introduces OckScore, a joint accuracy-efficiency metric: `S_ock = Accuracy − λ·log(T/C)`.

---

## Core Concept: The Overthinking Tax

**Occam's Razor principle** applied to LLM reasoning: the simplest (most token-efficient) correct answer is preferred over verbose reasoning chains.

### The Paradox

Smaller models attempt to compensate for lower accuracy by generating longer reasoning chains ("thinking harder"). This backfires:

| Model | Accuracy | Output Tokens (avg) | Cost per Correct Answer |
|-------|----------|---------------------|------------------------|
| 7B model | Lower | **3.13× more** than 14B | **57% higher** than 14B |
| 14B model | Higher | Baseline | Baseline |

The 7B model's verbosity more than cancels its lower per-token cost advantage.

---

## OckScore: Joint Accuracy-Efficiency Metric

### Formula

```
S_ock = Accuracy − λ · log(T / C)
```

Where:
- `Accuracy` = fraction of tasks correctly solved
- `T` = total output tokens generated
- `C` = calibration constant (10,000 tokens)
- `λ` = efficiency weight (10 by default)
- `log` = natural logarithm

### Interpretation

| Scenario | OckScore |
|----------|---------|
| High accuracy, low tokens | High (positive) |
| High accuracy, high tokens | Moderate (penalized) |
| Low accuracy, low tokens | Negative |
| Low accuracy, high tokens | Strongly negative |

**OckScore penalizes verbosity exponentially** — a model that doubles its token count must also significantly improve accuracy to maintain the same score.

### Calibration

At `T = C = 10,000` tokens, the penalty term is 0. Models that solve a task in exactly 10,000 tokens are not penalized; those using fewer are rewarded, those using more are penalized.

---

## Open-Source vs. Proprietary: The Verbosity Gap

| Category | Tokens (normalized to proprietary baseline) |
|----------|-------------------------------------------|
| **Open-source models** | **5.1× proprietary baseline** |
| Proprietary models | 1.0× (baseline) |

**Root cause hypothesis**: Open-source reasoning models (trained with RL on step-by-step reasoning traces) are trained to be verbose because longer traces were historically higher quality. Proprietary models have been more aggressively optimized for token efficiency.

---

## Benchmark Results: Top Models by OckScore

| Model | Accuracy | OckScore | Notes |
|-------|----------|---------|-------|
| Claude Sonnet 4.5 | High | High | Best proprietary OckScore |
| GPT-5 | High | High | Comparable |
| Claude Haiku 4.5 | Moderate | Moderate-High | Best efficiency ratio |
| Gemini 3.1 Flash | Moderate | Moderate | Token-efficient |
| Open-source 14B | Moderate | Moderate | Better than 7B |
| Open-source 7B | Lower | **Lowest** | Overthinking Tax severe |

---

## Task Categories in OckBench

The benchmark spans reasoning tasks where efficiency matters:

| Category | Why Efficiency Matters |
|----------|----------------------|
| Math reasoning | Step count ≠ accuracy; concise proofs better |
| Code generation | Verbose explanations before code waste tokens |
| Factual QA | Single-step retrieval; chains add noise |
| Logical puzzles | Direct solutions vs. exhaustive case enumeration |
| Summarization | Output length directly benchmarked |

---

## Overthinking Patterns Identified

The paper categorizes specific overthinking behaviors:

### 1. Unnecessary Verification Loops
Model solves the problem, then re-solves from scratch "to verify," consuming 2× tokens.

### 2. Exhaustive Case Enumeration
When a few cases suffice, small models enumerate all edge cases regardless of relevance.

### 3. Hedge Cascades
Excessive hedging ("however," "it's worth noting," "one might argue") that adds tokens without information.

### 4. Pre-Answer Preamble
Restating the problem at length before answering ("Let me think about this step by step. The question asks us to...").

### 5. Post-Answer Elaboration
Lengthy explanations after giving the correct answer ("This is because...," "In summary...," "Note that...").

---

## Economic Implications

### When Smaller Models Cost More

A 7B model at $0.10/1M tokens vs. 14B at $0.25/1M tokens:

```
7B: 100,000 output tokens × $0.10/1M = $0.010
14B: 32,000 output tokens × $0.25/1M = $0.008
```

The 14B model is 20% cheaper in absolute cost despite costing 2.5× per token — because it generates 3.13× fewer tokens.

### Budget Allocation Recommendation

For cost-constrained deployments:
- Use larger proprietary models for accuracy-critical tasks (they're often cheaper on OckScore basis)
- Avoid small open-source reasoning models for high-volume production (Overthinking Tax dominates)
- Use Claude Haiku 4.5 for simple tasks where both accuracy and token efficiency are high

---

## λ Sensitivity Analysis

The paper tests sensitivity to the efficiency weight λ:

| λ Value | Ranking Change |
|---------|---------------|
| λ = 1 | Minor reranking |
| λ = 10 (default) | Moderate reranking (shows Overthinking Tax) |
| λ = 50 | Major reranking (punishes any verbosity severely) |

Default λ = 10 is calibrated to reflect real-world cost sensitivity where token costs are significant but accuracy is the primary objective.

---

## Workspace Relevance

Directly actionable for model selection and prompt design:

1. **Overthinking Tax for routing decisions**: When using Claude Haiku 4.5 for simple tasks (`haiku-implementer` agent), verify it doesn't trigger overthinking on boundary tasks — if it generates 3× more tokens than expected, switch to Sonnet.
2. **OckScore for model selection**: When comparing models for workspace tasks, weight token efficiency alongside accuracy. Claude Sonnet 4.5's high OckScore (good accuracy + low verbosity) validates its role as the primary workspace model.
3. **Open-source 5.1× verbosity**: If evaluating open-source models for workspace sub-tasks (e.g., local inference), factor in the 5.1× token overhead — the actual cost may be comparable to or higher than proprietary API calls.
4. **Overthinking patterns → output discipline**: The 5 overthinking patterns (hedge cascades, pre-answer preamble, post-answer elaboration) exactly match what `output-discipline.md` prohibits ("不重述問題," "無開場白," "填充語禁止"). OckBench validates these constraints economically.
5. **λ=10 calibration for budget tracking**: The workspace's token budget rules (4K/task, 30K/session in `context-management.md`) implicitly implement an OckScore-like constraint — tasks that require excessive tokens are a signal to re-scope or compact.

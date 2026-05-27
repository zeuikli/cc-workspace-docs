---
title: "Prompting Science Report 2: The Decreasing Value of Chain of Thought in Prompting"
arxiv_id: 2506.07142
authors: "Lennart Meincke, Ethan Mollick, Lilach Mollick, Dan Shapiro"
fetched: 2026-05-27
published: 2025-06-08
source: "https://arxiv.org/abs/2506.07142"
source_tier: P
---

# Prompting Science Report 2: The Decreasing Value of Chain of Thought in Prompting

**Authors**: Lennart Meincke¹², Ethan Mollick¹, Lilach Mollick¹, Dan Shapiro¹³
**Affiliations**:
1. Generative AI Labs, The Wharton School of Business, University of Pennsylvania
2. WHU–Otto Beisheim School of Management
3. Glowforge

**Published**: June 8, 2025
**Source**: https://arxiv.org/abs/2506.07142
**arXiv ID**: 2506.07142
**Categories**: cs.CL / cs.AI

---

## Abstract

This is the second in a series of short reports that seek to help business, education, and policy leaders understand the technical details of working with AI through rigorous testing. In this report, we investigate Chain-of-Thought (CoT) prompting, a technique that encourages a large language model (LLM) to "think step by step" (Wei et al., 2022). CoT is a widely adopted method for improving reasoning tasks, however, our findings reveal a more nuanced picture of its effectiveness. We demonstrate two things:

- The effectiveness of Chain-of-Thought prompting can vary greatly depending on the type of task and model. For non-reasoning models, CoT generally improves average performance by a small amount, particularly if the model does not inherently engage in step-by-step processing by default. However, CoT can introduce more variability in answers, sometimes triggering occasional errors in questions the model would otherwise get right. We also found that many recent models perform some form of CoT reasoning even if not asked; for these models, a request to perform CoT had little impact. Performing CoT generally requires far more tokens (increasing cost and time) than direct answers.
- For models designed with explicit reasoning capabilities, CoT prompting often results in only marginal, if any, gains in answer accuracy. However, it significantly increases the time and tokens needed to generate a response.

---

## Core Thesis

CoT prompting's utility has diminished as models have evolved: non-reasoning models already perform implicit CoT by default, making explicit CoT prompts redundant for recent models, while reasoning models see only marginal accuracy gains (RD ≤ 0.031) at a 20–80% time cost increase. The traditional CoT benefit applies mainly to older or smaller non-reasoning models that do not engage in step-by-step processing by default.

---

## Benchmark and Methodology

### Dataset

**GPQA Diamond** (Graduate-Level Google-Proof Q&A Benchmark, Rein et al. 2024): 198 multiple-choice PhD-level questions across biology, physics, and chemistry.

- PhD accuracy in corresponding domain: 65% (74% discounting identified mistakes)
- Highly skilled non-expert validators: 34% accuracy (with >30 min unrestricted web access)

### Models Tested

**Non-Reasoning Models:**
- Sonnet 3.5 (claude-3-5-sonnet-20240620)
- Gemini 2.0 Flash (gemini-2.0-flash-001)
- GPT-4o-mini (gpt-4o-mini-2024-07-18)
- GPT-4o (gpt-4o-2024-08-06)
- Gemini Pro 1.5 (gemini-1.5-pro-001)

**Reasoning Models:**
- o3-mini (o3-mini-2025-01-31)
- o4-mini (o4-mini-2025-04-16)
- Gemini Flash 2.5 (gemini-2.5-flash-preview-05-20)

### Experimental Design

- 25 trials per question per condition (4,950 runs per prompt per model)
- Temperature = 0
- Correlation between 25-trial and 100-trial results is very high (see Table S2)

### Performance Metrics

| Metric | Description |
|--------|-------------|
| **100% Correct** | Must get all 25/25 trials correct — strictest, zero-error tolerance |
| **90% Correct** | At least 23/25 trials correct — comparable to human acceptable error rates |
| **51% Correct** | Simple majority: at least 13/25 trials correct |
| **Average Rating** | Overall mean across all trials and all questions (N = 4,950) |

*Note: PASS@N and CONSENSUS metrics excluded as not useful for real-world benchmarking.*

### Prompt Conditions

| Condition | Prompt |
|-----------|--------|
| **Direct** | "Answer directly without any explanation or thinking. Just provide the answer." |
| **Step by step** | "Think step by step" appended to question |
| **Default** | No suffix, no formatting constraint — model chooses reply format |

Different CoT prompt variants (Step by Step, Think Carefully, Decompose Problem, Weigh Paths) showed negligible differences (Figure S3).

---

## Results

### Non-Reasoning Models: Direct vs. CoT (Step by Step)

CoT generally improved **Average** performance but had mixed effects on **100% Correct** metric:

| Model | Average RD | p | 100% Correct RD | p |
|-------|-----------|---|-----------------|---|
| Sonnet 3.5 | +0.117 | <0.001 | +0.101 | 0.001 |
| Gemini 2.0 Flash | +0.135 | <0.001 | **−0.131** | <0.001 |
| GPT-4o-mini | +0.044 | 0.067 (ns) | **−0.091** | 0.001 |
| GPT-4o | +0.072 | 0.003 | +0.010 | 0.624 (ns) |
| Gemini Pro 1.5 | +0.071 | 0.014 | **−0.172** | <0.001 |

Key finding: In 3 of 5 non-reasoning models, CoT **harmed** perfect-accuracy performance while raising average performance — models introduced new errors on questions they previously got consistently right.

CoT latency overhead for non-reasoning models: **35–600% longer** (5–15 seconds per question).

### Non-Reasoning Models: Default vs. CoT

Gains from CoT relative to the **default** (unprompted) behavior were much smaller:

| Model | Average RD | p |
|-------|-----------|---|
| Sonnet 3.5 | −0.019 | 0.189 (ns) |
| Gemini 2.0 Flash | +0.062 | <0.001 |
| GPT-4o-mini | +0.004 | 0.728 (ns) |
| GPT-4o | +0.069 | 0.003 |

Reason: Many non-reasoning models already perform CoT implicitly when unprompted. Explicit CoT instruction adds little value.

Additional finding: Prompting a model to answer *only* (no reasoning tokens) likely harms non-reasoning model performance by suppressing implicit CoT.

### Reasoning Models: Direct vs. CoT

| Model | Average RD | p | 100% Correct RD | p |
|-------|-----------|---|-----------------|---|
| o3-mini | +0.029 | 0.024 | +0.015 | 0.738 (ns) |
| o4-mini | +0.031 | 0.003 | +0.010 | 0.731 (ns) |
| Gemini Flash 2.5 | **−0.033** | 0.005 | **−0.131** | 0.001 |

CoT on reasoning models: marginal or negative accuracy impact, with **20–80% longer** response time (10–20 seconds per question).

---

## Discussion and Conclusion

**Non-reasoning models:**
- CoT is still a useful tool for boosting *average* performance, especially for older/smaller models without implicit step-by-step processing
- CoT introduces higher variability — can harm "easy" question accuracy while improving "hard" question accuracy
- Many recent non-reasoning models already perform implicit CoT, making explicit prompting redundant
- CoT increases token count, time, and cost

**Reasoning models:**
- Benefits of explicit CoT on answer accuracy are marginal at best
- Given substantial increases in response time and tokens, CoT utility for reasoning models is questionable for most practical purposes

**Decision framework:** CoT prompting decisions should be guided by:
1. The specific model's characteristics
2. Task requirements
3. Balance between accuracy improvement, tolerance for variability, and acceptable response latency

### Limitations

- Limited set of models tested
- Single benchmark (GPQA Diamond)
- Simple CoT variant used (though sophisticated variants showed negligible differences in Figure S3)
- Highly customized, task-specific CoT may yield larger benefits than generic approaches

---

## Supplementary Data

### Table S2: 25 vs. 100 Trials Comparison (GPT-4o-mini, Direct Condition)

| N Trials | Metric | Estimate [95% CI] |
|----------|--------|-------------------|
| 25 | Average | 0.389 [0.382, 0.396] |
| 100 | Average | 0.389 [0.385, 0.393] |
| 25 | 100% | 0.185 [0.162, 0.207] |
| 100 | 100% | 0.147 [0.136, 0.162] |
| 25 | 51% | 0.380 [0.364, 0.394] |
| 100 | 51% | 0.377 [0.369, 0.389] |
| 25 | 90% | 0.247 [0.227, 0.263] |
| 100 | 90% | 0.249 [0.237, 0.263] |

*No metric reached statistical significance at α=0.05; 25 trials provide comparable precision to 100 trials.*

### Table S3: Full Pairwise Comparisons — Non-Reasoning Models (Direct vs. CoT)

| Model | Metric | RD [95% CI] | p |
|-------|--------|-------------|---|
| Sonnet 3.5 | Average | 0.117 [0.069, 0.166] | <0.001 |
| Sonnet 3.5 | 100% | 0.101 [0.040, 0.162] | 0.001 |
| Sonnet 3.5 | 90% | 0.136 [0.071, 0.202] | <0.001 |
| Sonnet 3.5 | 51% | 0.131 [0.056, 0.207] | 0.001 |
| Gemini 2.0 Flash | Average | 0.135 [0.076, 0.199] | <0.001 |
| Gemini 2.0 Flash | 100% | −0.131 [−0.207, −0.056] | <0.001 |
| Gemini 2.0 Flash | 90% | −0.030 [−0.101, 0.045] | 0.381 (ns) |
| Gemini 2.0 Flash | 51% | 0.136 [0.061, 0.212] | <0.001 |
| GPT-4o-mini | Average | 0.044 [−0.003, 0.090] | 0.067 (ns) |
| GPT-4o-mini | 100% | −0.091 [−0.141, −0.035] | 0.001 |
| GPT-4o-mini | 90% | −0.066 [−0.126, −0.010] | 0.033 |
| GPT-4o-mini | 51% | 0.020 [−0.045, 0.086] | 0.609 (ns) |
| GPT-4o | Average | 0.072 [0.028, 0.118] | 0.003 |
| GPT-4o | 100% | 0.010 [−0.040, 0.061] | 0.624 (ns) |
| GPT-4o | 90% | 0.035 [−0.015, 0.086] | 0.150 (ns) |
| GPT-4o | 51% | 0.071 [0.000, 0.141] | 0.042 |
| Gemini Pro 1.5 | Average | 0.071 [0.018, 0.128] | 0.014 |
| Gemini Pro 1.5 | 100% | −0.172 [−0.242, −0.101] | <0.001 |
| Gemini Pro 1.5 | 90% | −0.131 [−0.197, −0.066] | <0.001 |
| Gemini Pro 1.5 | 51% | 0.056 [−0.015, 0.126] | 0.097 (ns) |

### Table S4: Full Pairwise Comparisons — Non-Reasoning Models (Default vs. CoT)

| Model | Metric | RD [95% CI] | p |
|-------|--------|-------------|---|
| Sonnet 3.5 | Average | −0.019 [−0.047, 0.009] | 0.189 (ns) |
| Gemini 2.0 Flash | Average | 0.062 [0.028, 0.095] | <0.001 |
| Gemini 2.0 Flash | 100% | 0.071 [0.005, 0.136] | 0.039 |
| Gemini 2.0 Flash | 90% | 0.111 [0.045, 0.177] | <0.001 |
| GPT-4o-mini | Average | 0.004 [−0.021, 0.031] | 0.728 (ns) |
| GPT-4o | Average | 0.069 [0.023, 0.113] | 0.003 |

### Table S5: Full Pairwise Comparisons — Reasoning Models (Direct vs. CoT)

| Model | Metric | RD [95% CI] | p |
|-------|--------|-------------|---|
| o3-mini | Average | 0.029 [0.003, 0.053] | 0.024 |
| o3-mini | 100% | 0.015 [−0.056, 0.086] | 0.738 (ns) |
| o3-mini | 90% | 0.030 [−0.025, 0.086] | 0.332 (ns) |
| o3-mini | 51% | 0.000 [−0.040, 0.040] | 1.000 (ns) |
| o4-mini | Average | 0.031 [0.010, 0.052] | 0.003 |
| o4-mini | 100% | 0.010 [−0.061, 0.081] | 0.731 (ns) |
| o4-mini | 90% | 0.051 [−0.005, 0.106] | 0.106 (ns) |
| o4-mini | 51% | 0.056 [0.015, 0.096] | 0.003 |
| Gemini Flash 2.5 | Average | −0.033 [−0.056, −0.010] | 0.005 |
| Gemini Flash 2.5 | 100% | −0.131 [−0.207, −0.056] | 0.001 |
| Gemini Flash 2.5 | 90% | −0.071 [−0.131, −0.010] | 0.016 |
| Gemini Flash 2.5 | 51% | −0.035 [−0.076, 0.005] | 0.060 (ns) |

---

## Key References

- **Wei et al. (2022)** — Chain-of-thought prompting elicits reasoning in large language models. *NeurIPS 2022*, 24824–24837.
- **Rein et al. (2024)** — GPQA: A Graduate-Level Google-Proof Q&A Benchmark. *First Conference on Language Modeling.*
- **Miller (2024)** — Adding Error Bars to Evals: A Statistical Approach to Language Model Evaluations. arXiv:2411.00640.
- **Meincke et al. (2025)** — Prompting Science Report 1: Prompt Engineering is Complicated and Contingent. SSRN:5165270.

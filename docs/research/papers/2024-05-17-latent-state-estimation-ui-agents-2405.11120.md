---
title: "Latent State Estimation Helps UI Agents to Reason"
arxiv_id: 2405.11120
authors: William E Bishop, Alice Li, Christopher Rawles, Oriana Riva
published: 2024-05-17
source: "https://arxiv.org/abs/2405.11120"
venue: arXiv
---

# Latent State Estimation Helps UI Agents to Reason

**Authors**: William E Bishop, Alice Li, Christopher Rawles, Oriana Riva

**Published**: May 17, 2024

**Source**: https://arxiv.org/abs/2405.11120

**Subject Classification**: Artificial Intelligence (cs.AI); Machine Learning (cs.LG)

**License**: Creative Commons BY 4.0

---

## Abstract

The research explores whether large language models can estimate and reason about latent environmental state—aspects of a task environment that are uncertain or obscured. The investigators focused on autonomous UI agents operating in real-world settings where "the response of an environment to their actions may be non-deterministic and observed through noise."

The team demonstrated that appropriately prompted LLMs achieve over 76% accuracy when estimating latent state aspects like actual versus intended actions and task completion status. Across multiple benchmarks and reasoning approaches, agents employing explicit latent state estimation "are able to successfully complete up to 1.6x more tasks than those that do not."

---

## Core Contribution

This research demonstrates that LLMs can estimate hidden aspects of UI state—such as performed actions, screen summaries, task progression, mistakes, and completion status—despite noisy and partial screen representations. The paper shows incorporating these latent state estimates improves UI agent task success rates by up to 1.6x.

---

## Key Findings

### Latent State Estimation Accuracy

The LLM achieved high accuracy across five state aspects, ranging from "76.8%–97.3%" depending on the aspect. Performance matched or exceeded human experts on most measures, particularly for inferring task progression.

### Performance Improvements

When agents explicitly reasoned about latent state, task success increased substantially:
- Zero-shot: 28.1% → 45.9%
- CoT-SC: 28.1% → 42.2%
- ReAct: 35.6% → 43.7%

### Evaluation Methodology

The work uniquely emphasizes online end-to-end testing rather than offline pre-recorded data, using three Android benchmarks totaling 135 tasks across 48 apps.

---

## Technical Approach

The method formalizes latent state estimation as calculating "point estimates...from noisy observations" by prompting LLMs to infer hidden variables through zero-shot reasoning. Estimates chain together—earlier inferences inform later ones—without requiring task-specific training data.

### Zero-Shot Reasoning Method

The approach relies on:
- Zero-shot prompting functioning as point estimation in textual space
- Chain-of-thought with self-consistency for enhanced reasoning
- ReAct approaches for integrated act-reason integration

---

## Significance

This work bridges reasoning methodology and content: showing that *what* LLMs reason about (latent state) matters as much as *how* they reason, with benefits consistent across multiple reasoning approaches.

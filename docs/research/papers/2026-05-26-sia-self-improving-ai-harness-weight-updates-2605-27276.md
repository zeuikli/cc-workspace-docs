---
url: "https://arxiv.org/abs/2605.27276"
title: "SIA: Self Improving AI with Harness & Weight Updates"
archived_date: 2026-06-14
arxiv_id: 2605.27276
authors: ["Prannay Hebbar", "Yogendra Manawat", "Samuel Verboomen", "Alesia Ivanova", "Selvam Palanimalai", "Kunal Bhatia", "Vignesh Baskaran"]
domains: [self-improving-agents, harness-engineering, test-time-training, reinforcement-learning]
pdf_path: pdfs/2605.27276.pdf
published_date: 2026-05-26
---

# SIA: Self Improving AI with Harness & Weight Updates

**Authors**: Prannay Hebbar, Yogendra Manawat, Samuel Verboomen, Alesia Ivanova, Selvam Palanimalai, Kunal Bhatia, Vignesh Baskaran  
**Published**: May 26 2026 (v1); revised May 28 2026 (v2)  
**Source**: https://arxiv.org/abs/2605.27276  
**arXiv ID**: 2605.27276  
**Categories**: cs.AI, cs.CL

---

## Abstract

Humans are the bottleneck in building and improving AI. Two largely disjoint research silos exist: the harness-update school (meta-agent rewrites scaffold while weights are fixed) and the test-time training school (RL pipeline updates model weights while harness is fixed). SIA proposes a self-improving loop in which a Feedback-Agent updates **both** the harness and the weights of a task-specific agent. Evaluated across three contrasting domains: Chinese legal charge classification (LawBench), low-level GPU kernel optimisation (AlphaEvolve TriMul), and single-cell RNA denoising (MAGIC scRNA-seq). SIA-W+H (harness + weight updates) outperforms SIA-H (harness only) on all three benchmarks.

---

## Core Architecture

### Two-Lever Loop

SIA operates three LLM components in a step-budget loop:

1. **Meta-Agent** — Initialises the first scaffold from task specification and reference implementations.
2. **Task-Specific Agent** — Executes against dataset inside a sandbox; produces trajectory.
3. **Feedback-Agent** — Reads trajectory, selects at each step between two actions:
   - **Harness update**: scaffold evolution (prompts/tools/retry logic/parsing), weights fixed.
   - **Weight update**: RL-based LoRA update, scaffold fixed.

The Feedback-Agent's action selection is dynamic, conditioned on observed reward landscape (density, rollout cost, pass-rate distribution, regression risk). The two levers are interleaved freely, not locked into sequential phases.

### Harness Update Recurrence

```
A_{g+1} = F(A_g, τ_g(π_θ), E_g, U)
```

Where `τ_g(π_θ)` = full trajectory (prompt, model response, tool call, tool result, extracted answer for every instance). Feedback-Agent diagnoses failure modes from full trajectory, not summary statistics.

### Weight Update Algorithms (Feedback-Agent selects per task)

| Algorithm | When selected |
|-----------|--------------|
| **GRPO** | Rollouts cheap to sample; verifier fires at episode end (classification, short-answer, unit-test). Advantages normalised within rollout group of size G: `Â_i = (r_i − r̄)/σ_r`. No value network. |
| **PPO with GAE** | Dense step-level rewards; training stability is binding constraint (multi-step tool-use, long code-generation). Clipped surrogate with value head. |
| **Entropic advantage weighting** | Heavily right-skewed reward histogram (rare correct solutions). Gradient mass via softmax with adaptive temperature β: `w_i ∝ exp(r_i/β)`. |
| **REINFORCE + KL-to-base** | Dense reward; primary risk is capability regression. No critic, no grouping; KL penalty `α KL(π_θ ‖ π_θ₀)`. |
| **Best-of-N behavioural cloning** | Cold-start: `E[r] ≈ 0` across all rollouts. Top-k rollouts distilled via cross-entropy to raise baseline pass rate before RL phase. |
| **DPO** | Verifier ranks but cannot score absolutely. Ordinal signal without reward model. |

Base model throughout: `gpt-oss-120b` (internal 120B instruction-tuned). LoRA rank 32 on H100 via Modal. Meta-Agent and Feedback-Agent use **Claude Sonnet 4.6**.

---

## Experimental Results

### Setup

| Task | Domain | Metric | Previous SOTA |
|------|--------|--------|--------------|
| LawBench (191-class) | Chinese legal | top-1 accuracy | 0.450 |
| AlphaEvolve TriMul | GPU kernel | 1500/runtime (higher = faster) | 1.292 |
| MAGIC scRNA-seq | Single-cell RNA | mse_norm ∈ [0,1] (higher = better) | 0.240 |

### Ablation: SIA-H vs SIA-W+H

| Task | Initial | Prev. SOTA | SIA-H (harness only) | SIA-W+H (harness + weights) |
|------|---------|-----------|----------------------|------------------------------|
| LawBench (top-1 acc) | 13.5% | 45.0% | 50.0% | **70.1%** (+20.1 pp over SIA-H) |
| AlphaEvolve TriMul (reward) | 0.105 | 1.292 | 0.120 (12,483 μs) | **1.475** (1,017 μs; 91.9% runtime reduction) |
| Denoising (mse_norm) | 0.048 | 0.240 | 0.241 | **0.289** (+20% over SIA-H) |

Over initial baseline: +56.6% on LawBench, 91.9% runtime reduction on GPU kernels (14.02× final speedup), +502% on denoising.

### Per-Domain Analysis

**LawBench**: Harness converged at 50.0% (TF-IDF + LinearSVC pipeline, iterative n-gram/regulariser tuning). Feedback-Agent switched to GRPO for the 191-class charge taxonomy; gradient pressure sharpened disambiguation of adjacent charge categories. Final 70.1%.

**AlphaEvolve TriMul**: Harness converged at 12,483 μs (1.14× speedup) via compilation-error parser and timing harness. Feedback-Agent applied GRPO with entropic utility objective (up-weights high-reward rollouts, discounts near-zero noise). Weights internalised H100-specific patterns (shared-memory tiling, fp32 register accumulation, block-size selection) unreachable by scaffold. Final 1,017 μs (14.02×).

**MAGIC scRNA-seq**: Harness swept coupled hyperparameter space (k, t, α), plateaued at mse_norm 0.241. First weight-update checkpoint introduced `np.clip + np.rint` post-processing — a biological invariant (non-negative integer counts) the scaffold never proposed across all iterations. Final 0.289.

---

## Discussion

### What Each Lever Changes

**Harness updates** → externalised changes: new tools, tighter parsers, search procedures, retry policies, prompt structure. All gains come from how the scaffold mediates between model and task environment; model checkpoint unchanged.

**Weight updates** → internalised knowledge: domain-specific patterns encoded into parameters unreachable by any scaffold edit. Emerges from direct gradient pressure on task verifier, not from human-authored instruction.

"The harness shapes how the agent searches; weight updates change what the model knows."

### Feedback-Agent Lever Selection Logic

The Feedback-Agent does not run a fixed RL procedure. At each weight-update step it selects algorithm conditioned on: reward density, rollout cost, pass-rate distribution, risk of capability regression. Selection is made at runtime from observed trajectory, not hard-coded by system designer.

### Limitations

**Coupled co-evolutionary Goodhart**: Harness search and RL weight updates both optimise against the same fixed verifier `V`. The joint fixed point is a Nash equilibrium between two optimisers blind to each other's update history — not a global optimiser of `V`. This can produce systems that appear strong on training verifier but are fragile under perturbation to either component. Standard Goodhart analyses assume a single optimiser; this two-lever setting produces a coupled variant.

---

## Comparison: Harness-Only vs Weight-Update Schools

| System | Edits harness | Edits weights |
|--------|--------------|--------------|
| **SIA (ours)** | Yes | Yes |
| Hyperagents (Zhang et al., 2026) | Yes | No |
| Darwin Gödel Machine (Zhang et al., 2025) | Yes | No |
| Meta-Harness (Lee et al., 2026) | Yes | No |
| TTRL (Zuo et al., 2025) | No | Yes |
| Discover-TTT | No | Yes |
| EUREKA (Ma et al., 2023) | Partial | Yes |

SIA is the only system that updates both scaffold and weights in a single self-improving loop.

---

## Key Quotes

> "Harness updates make the model agentic, shaping how it searches and acts, while weight updates build the domain intuition that no prompt or scaffold can instil."

> "Scaffold edits concentrate on software-engineering hygiene — parsing, retries, dispatch — and rarely deliver domain-specific reasoning that the base model could not produce given any prompt."

> "The Feedback-Agent dynamically selects between scaffold and weight updates in a closed feedback loop, with each update type informed by trajectories produced under the current state of both components."

---

## Related Work Connections

- **Meta-Harness** (2603.28052): SIA harness update step is closest in spirit; difference = SIA follows harness convergence with weight updates rather than further mutation.
- **Hyperagents** (2603.19461): Closest concurrent work; adds expressivity to scaffold edits but leaves weights fixed. SIA adds weight lever.
- **TTRL** (Zuo et al., 2025): RL on unlabelled test data; single-prompt, single-response, no scaffold.
- **Discover-TTT** (Yuksekgonul et al., 2026): Entropic utility objective reused by SIA for weight updates.

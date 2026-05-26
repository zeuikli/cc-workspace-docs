---
title: "HARBOR: Automated Harness Optimization"
authors: "Biswa Sengupta, Jinhua Wang"
published: "2026-04-22"
source: "https://arxiv.org/abs/2604.20938"
---

# HARBOR: Automated Harness Optimization

**Authors**: Biswa Sengupta, Jinhua Wang
**Published**: April 22, 2026
**Source**: https://arxiv.org/abs/2604.20938
**arXiv ID**: 2604.20938
**Categories**: cs.LG, cs.AI
**Benchmark**: Terminal-Bench 2.0 (89 tasks)

---

## Abstract

Long-horizon LLM agents are dominated not by their underlying model but by the harness that wraps it (~98.4% of Claude Code's codebase is deterministic harness code). HARBOR formalizes **Automated Harness Optimization (AHO)** as a constrained Bayesian optimization problem and provides a reference solver with cold-start correction, cost-aware acquisition, and safety constraints.

---

## Problem Formulation

```
maximize: μ(c) = E_t[R(c,t)]
subject to: E_t[cost(c,t)] ≤ B_dep
            μ(c) ≥ R_0 - δ
```

Where `c` is a configuration from a mixed Boolean/categorical/numeric space, `R(c,t)` is Bernoulli task outcome, constraints enforce cost budgets and safety margins.

---

## Motivation: Manual Tuning Failure

Four rounds of human-guided harness enhancement on Terminal-Bench 2 (all-flags-off baseline: 15/89):

| Round | Result | Cause |
|-------|--------|-------|
| B | +2 passes (15→17) ✓ | Clean improvement |
| C | -4 passes (17→13) ✗ | Low-capability self-evaluators |
| D | -5 passes (12/89) ✗ | ACON cache corruption + integration bugs |

**Oracle (union of all flags)**: 81/89 — massive headroom unreachable via manual tuning.

---

## Three Structural Properties

### Property I — Cold-Start Correction

Cross-session features (memory, compression) suffer from empty state in task-independent benchmarks. Mixture model:

```
E[R(c,t)|n] = w(c,n)·p_∞(c) + (1-w(c,n))·p_base
```

### Property II — Block-Additive Surrogate

Sparse Axis-aligned Subspace (SAAS) prior with per-layer kernels + controlled cross-layer interactions. Handles ~40 nominal dimensions while exploiting sparsity via axis-aligned contraction.

### Property III — Multi-Fidelity Cost-Aware Acquisition

Task subsets at m∈{8, 22, 44, 89} enable cheap early exploration:

```
maximize: qNEHVI_m(c_{1:q}) / Cost(c_{1:q}, m)
```

Information-per-dollar efficiency over standard acquisition.

---

## HARBOR Algorithm

1. Initialize with SAAS-prior GP on mixed-variable block-additive kernel
2. Place M trust regions via TuRBO at top incumbents
3. Loop while search budget permits:
   - Select batch maximizing cost-normalized qNEHVI
   - Apply per-candidate safety constraint: lower credible bound ≥ R_0 - δ
   - Invert warm-start mixture model + attach heteroscedastic variance
   - Refit with NUTS sampling; update trust regions
   - Freeze silent dimensions after n_min observations

**Key innovation**: Posterior chance constraint structurally prevents C-style regressions by rejecting candidates whose lower credible bound violates the safety margin.

---

## Harness Configuration Space

**Agent**: codex-py (52K Python LOC) with gpt-5.4-nano

**9 flag-gated extensions**:
- Native flags (5): semantic cache, cross-session memory, tiered compression, trajectory replay, speculative prediction
- Published-technique flags (4): Reflexion, ACON, PASTE, self-evaluation gate

**Telemetry counters**: cache_hits, token_savings, reflections_written, reflections_retrieved, predictions_fired — enables silent bug detection via read/write asymmetry.

---

## Results

| Configuration | Passes / 89 | % |
|--------------|------------|---|
| All-flags-off baseline | 15 | 16.85% |
| Manual Round B (peak) | 17 | 19.10% |
| Manual Round D (all-on) | 12 | 13.48% |
| **HARBOR (~3.5 budget)** | **17** | **19.10%** |

- HARBOR matched manual peak using **2 flags instead of 8**
- Against Round D: +5 passes (+37% relative improvement)
- Mean across 5 full-suite evaluations: 16.6/89 (18.65%)

**HARBOR selected**: cross-session memory + tiered compression only. Correctly disabled self-eval gate, ACON, Reflexion, PASTE.

---

## Critical Discoveries

### 1. Integration Bugs as Signal

Two silent failures invisible to pass rates, caught by telemetry:
- `reflections_written=80, reflections_retrieved=0` → container non-persistence
- `PASTE_invocations=0` → feature never activated

"Observability doubles as a bug-detector for the engineering loop."

### 2. ACON-Cache Coupling

Observation-compression gate stored compressed summaries in cache instead of raw outputs → corrupted downstream reads. An architectural invariant violation only visible via telemetry.

### 3. Model-Dependent Feature Interactions

Self-evaluation helps stronger models (Claude Sonnet) but hurts weaker ones (gpt-5.4-nano). Feature interactions depend on latent model capability.

### 4. Sparsity in Practice

SAAS prior discovered only ~5 of ~40 nominal dimensions carry signal — structural lesson: **flag-space composition dominates per-flag tuning**.

---

## Discussion

**AHO scope**: Runs once per (agent, task-suite, model) epoch—not continuously. Amortizes meta-learned posteriors across related configurations.

**Prerequisite**: Structured telemetry with read/write counters is required for the bug-detection loop that manual ablation misses.

**Task-agnostic**: Formulation applicable to any agent harness with bounded configuration space and reproducible task suites.

---

## Conclusion

Harness engineering has matured from a systems problem into a **hyperparameter optimization problem** requiring principled automation. Manual stacking of published techniques produced diminishing returns; HARBOR's automated Bayesian optimizer with safety constraints recovered the manual peak from 2 flags instead of 8, while identifying integration bugs the manual loop missed across four rounds.

---

## Workspace Relevance

Complements `harness-meta` skill's Harness Audit (static gap analysis + CAR framework) with a principled **search algorithm** for configuration optimization once gaps are identified. The Ratchet principle in `harness-meta` is the manual version of HARBOR's automated loop.

HARBOR's safety constraint (posterior chance constraint) is directly analogous to `autoresearch`'s Guard: discard changes whose lower bound violates the safety margin.

---
title: "AgentOpt v0.1 Technical Report: Client-Side Optimization for LLM-Based Agent"
authors: Wenyue Hua, Sripad Karne, Qian Xie, Armaan Agrawal, Nikos Pagonas, Kostis Kaffes, Tianyi Peng
published: 2026-04-07
source: "https://arxiv.org/abs/2604.06296"
---

# AgentOpt v0.1 Technical Report: Client-Side Optimization for LLM-Based Agent

**Authors**: Wenyue Hua, Sripad Karne, Qian Xie, Armaan Agrawal, Nikos Pagonas, Kostis Kaffes, Tianyi Peng  
**Published**: April 7, 2026 (v1); revised April 15, 2026 (v2)  
**Source**: https://arxiv.org/abs/2604.06296  
**arXiv ID**: 2604.06296  
**Categories**: cs.LG, cs.AI, cs.MA, cs.SE  
**Code**: https://agentoptimizer.github.io/agentopt/  
**License**: CC BY 4.0

## Abstract

AI agents are increasingly deployed in real-world applications, including systems such as Manus, OpenClaw, and coding agents. Existing research has primarily focused on server-side efficiency, proposing methods such as caching, speculative execution, traffic scheduling, and load balancing to reduce the cost of serving agentic workloads. However, as users increasingly construct agents by composing local tools, remote APIs, and diverse models, an equally important optimization problem arises on the client side.

AgentOpt is introduced as a framework-agnostic Python package for client-side optimization of LLM-based agent pipelines. Across four benchmarks, the cost gap between the best and worst model combinations at matched accuracy ranges from 13× to 32×. Critically, optimal model combinations often differ from predictions based on standalone model capability rankings, demonstrating that models must be evaluated in workflow context, not isolation. The UCB-E algorithm achieves a 62–76% reduction in evaluation budget relative to brute-force search while recovering near-optimal accuracy.

## 1. Introduction

As AI agents become more prevalent in real-world deployments, developers increasingly compose pipelines from heterogeneous components: local tools, remote APIs, and diverse language models. While server-side optimization (caching, speculative execution, traffic scheduling, load balancing) has received significant research attention, client-side optimization — how developers should allocate resources across pipeline stages — remains underexplored.

AgentOpt formalizes this as a client-side optimization problem: given a multi-step agent pipeline, a pool of candidate models, and a labeled evaluation set, find the assignment of models to pipeline stages that maximizes accuracy subject to cost and latency constraints (or, equivalently, constructs the Pareto frontier over these objectives).

The key insight motivating this work is that **individual model capability does not predict combination performance**. A stronger model assigned to the wrong pipeline role can actively harm end-to-end accuracy. The most striking demonstration: on HotpotQA, Claude Opus 4.6 used as the planner in a 2-stage planner-solver pipeline achieves only 31.71% accuracy — it ranks worst among all 81 model combinations tested — because it attempts to answer queries directly rather than delegating to the downstream solver. Replacing it with Ministral 3 8B as planner (while keeping Opus 4.6 as solver) yields 74.27% accuracy.

### 1.1 Problem Distinction from LLM Routing

AgentOpt addresses a fundamentally different problem from per-query LLM routing:

| LLM Routing | AgentOpt (Pipeline Optimization) |
|-------------|----------------------------------|
| Per-query decisions | Pipeline-level optimization |
| Single LLM call | Multi-stage pipeline with coupled assignments |
| No inter-stage dependency | Downstream quality depends on upstream output |
| Query-time selection | Design-time configuration search |

Client-side optimization is "the layer at which application-specific objectives can be expressed directly," complementing server-side efficiency improvements.

## 2. Problem Formulation

Given:
- An agent pipeline $P$ consisting of $k$ stages, each invoking an LLM
- A candidate model pool $\mathcal{M}$ of size $n$
- A labeled evaluation set $\mathcal{D}$ of input/output pairs
- A utility function $U$ over (accuracy, cost, latency)

AgentOpt searches for the assignment $\mathbf{m} = (m_1, \ldots, m_k) \in \mathcal{M}^k$ that maximizes $U$, or equivalently constructs the Pareto frontier over accuracy, cost, and latency objectives.

The combinatorial search space has size $n^k$. For a 2-stage pipeline with 9 models, this yields 81 combinations. Exhaustive evaluation is prohibitively expensive; AgentOpt uses bandit-style algorithms to achieve sample-efficient search.

## 3. Technical Architecture

### 3.1 Framework-Agnostic HTTP Interception

AgentOpt intercepts LLM calls at the **httpx transport layer** by patching `httpx.Client.send()`. This approach:

- Requires **no modifications to agent code**
- Works with any framework that uses httpx for HTTP (LangChain, AutoGen, CrewAI, custom pipelines)
- Attributes each LLM call to specific (datapoint, combination) pairs using Python `contextvars`

The interception layer transparently replaces model identifiers in outgoing requests, routing calls to the assigned model for each stage.

### 3.2 Combination Evaluation

For each candidate combination $\mathbf{m}$, AgentOpt:
1. Sets the model assignment via context variables
2. Runs the pipeline on a batch of evaluation datapoints
3. Records per-call costs, latencies, and final accuracy
4. Aggregates results to estimate the combination's utility

The cost of a combination is computed as the sum of per-call costs across all stages. Latency is measured end-to-end.

### 3.3 Pareto Frontier Export

Results are exported as a Pareto frontier over (accuracy, cost, latency), enabling transparent tradeoff analysis. Developers can inspect dominated combinations and select configurations matching their deployment constraints.

## 4. Search Algorithms

Eight algorithms are implemented for sample-efficient exploration of the combination space:

| Algorithm | Type | Key Characteristic |
|-----------|------|--------------------|
| **Arm Elimination** | Bandit | Progressively eliminates combinations whose UCB falls below the leader |
| **UCB-E** | Bandit | Upper Confidence Bound for Exploration; best in v2 |
| **UCB-E + Low-Rank Factorization** | Bandit | Extends UCB-E with factorized uncertainty estimates |
| **Epsilon-LUCB** | Bandit | Epsilon-greedy variant of Lower Upper Confidence Bound |
| **Threshold Successive Elimination** | Bandit | Eliminates arms below a quality threshold |
| **Bayesian Optimization** | BO | Effective on smooth quality landscapes |
| **Hill Climbing** | Local search | Greedy local improvement; sensitive to local optima |
| **LM Proposal** | LM-driven | Uses an LLM to propose candidate combinations |
| **Random Search** | Baseline | Uniform random sampling |
| **Brute-Force** | Baseline | Evaluates all combinations exhaustively |

**Primary result**: UCB-E recovers near-optimal accuracy while reducing the evaluation budget by **62–76%** relative to brute-force search (v2 results). In v1, Arm Elimination provides the most consistent tradeoff, reducing budget by **24–67%** across three of four benchmarks.

Bayesian Optimization excels on smooth landscapes but struggles with concentrated quality distributions. Hill Climbing is sensitive to neighborhood topology and local optima. LM Proposal fails when optimal combinations depend on non-obvious role interactions.

## 5. Experimental Setup

### 5.1 Benchmarks

Four benchmarks span reasoning, science QA, math, and tool-use:

| Benchmark | Domain | Pipeline Type | Combinations |
|-----------|--------|---------------|--------------|
| **HotpotQA** | Multi-hop QA | 2-stage planner-solver | 81 (9×9 models) |
| **MathQA** | Math reasoning | 2-stage answer-critic | 81 (9×9 models) |
| **GPQA Diamond** | Graduate science QA | Single model | 9 |
| **BFCL v3** | Tool-use / function-calling | Single-model agent | 9 |

### 5.2 Model Pool

Nine models were evaluated, spanning capability tiers from small open-source models to frontier closed models. The pool includes Ministral 3 8B, Claude Haiku 4.5, Claude Sonnet 4.6, Claude Opus 4.6, and others.

## 6. Results

### 6.1 Main Performance Results

| Benchmark | Best Combination | Best Accuracy | Worst Accuracy | Cost Ratio (best/worst at matched accuracy) |
|-----------|-----------------|---------------|----------------|----------------------------------------------|
| HotpotQA | Ministral 3 8B (planner) + Claude Opus 4.6 (solver) | 74.27% | — | — |
| MathQA | Claude Opus 4.6 (answer) + Claude Haiku 4.5 (critic) | 98.84% | — | — |
| GPQA Diamond | Claude Opus 4.6 | 74.75% | — | — |
| BFCL v3 | Multiple models | 70.00% | — | 32× |

**Headline finding**: Across all four benchmarks, the cost gap between best and worst model combinations at matched accuracy ranges from **13× to 32×**.

### 6.2 The Planner Role Inversion (HotpotQA)

The HotpotQA results provide the most striking illustration of the core thesis:

- **Claude Opus 4.6 as planner**: ranks **71st–81st** out of 81 combinations
- **Ministral 3 8B as planner** (with Opus 4.6 as solver): **74.27%** — best overall
- **Claude Opus 4.6 solo** (planner + solver): **31.71%**

Root cause: Opus 4.6 in the planner role answers queries directly rather than formulating sub-queries for the solver. This "bypasses downstream search tools," producing poor end-to-end accuracy despite the model's high individual capability. A weaker planner that properly delegates outperforms a strong one that hoards work.

### 6.3 MathQA Role Specialization

On MathQA (answer-critic pipeline):
- **Best configuration**: Opus 4.6 (answer) + Haiku 4.5 (critic) — 98.84%
- The critic role benefits from a lighter model that efficiently validates rather than regenerates answers
- This matches the intuition that verification is computationally cheaper than generation

### 6.4 Search Algorithm Efficiency

Arm Elimination (v1) and UCB-E (v2) consistently outperform baselines:

- **UCB-E** (v2): 62–76% budget reduction vs brute-force
- **Arm Elimination** (v1): 24–67% budget reduction across 3/4 benchmarks
- **Bayesian Optimization**: strong on smooth landscapes, weak on discontinuous quality distributions
- **LM Proposal**: poor when optimal combinations are role-interaction-dependent (LLM cannot anticipate counter-intuitive role dynamics)

## 7. Design Principles

AgentOpt is built around three core requirements:

1. **Framework-agnosticism**: No custom wrappers or agent code modifications required; httpx-layer interception ensures compatibility with any LLM framework
2. **Non-intrusiveness**: Transparent model substitution; existing pipelines work unchanged
3. **Unified execution substrate**: Single evaluation harness supports all eight search strategies, enabling fair algorithm comparison

## 8. Implications for Agent System Design

### 8.1 Evaluate Pipelines, Not Models

The 13–32× cost gap and the planner inversion phenomenon demonstrate that per-model benchmarks (MMLU, GPQA, SWE-bench) are insufficient for pipeline design decisions. End-to-end evaluation on representative data is necessary.

### 8.2 Weak Planner + Strong Solver > Strong Solo Agent

The HotpotQA result (Ministral 3 8B planner + Opus 4.6 solver: 74.27% vs Opus 4.6 solo: 31.71%) empirically validates the "weak planner + smart delegation" architecture. This is the AgentOpt thesis: optimizing the planner's delegation behavior, not its raw capability, determines pipeline performance.

### 8.3 Search Algorithms Enable Practical Optimization

Without sample-efficient search, the combinatorial space ($n^k$ combinations) is intractable. UCB-E and Arm Elimination reduce the evaluation budget by 62–76%, making pipeline optimization practical for real-world deployments with limited labeled data.

## 9. Conclusion

AgentOpt introduces client-side optimization as a complement to server-side efficiency research for LLM-based agents. The framework demonstrates that:

1. Individual model capability rankings do not predict combination performance
2. Cost gaps of 13–32× exist between optimal and suboptimal configurations at matched accuracy
3. Sample-efficient bandit algorithms (UCB-E, Arm Elimination) recover near-optimal configurations with 62–76% fewer evaluations than brute-force
4. The optimal assignment of models to pipeline roles is often counter-intuitive and requires empirical search

AgentOpt is open-sourced at https://agentoptimizer.github.io/agentopt/ to enable reproducibility and community adoption.

## References

- Agrawal et al. (2024). "Taming Throughput-Latency Tradeoff in LLM Inference with Sarathi-Serve." OSDI.
- Bubeck et al. (1996–2012). Bandit algorithms survey: UCB, Arm Elimination, Epsilon-LUCB, Successive Elimination.
- Chen et al. (2024). "BFCL: Berkeley Function-Calling Leaderboard." UC Berkeley.
- Firoozi et al. (2024). "Foundation Models in Robotics." arXiv:2312.07843.
- Ho et al. (2024). "HotpotQA." EMNLP 2018 (original benchmark).
- Kwon et al. (2023). "Efficient Memory Management for Large Language Model Serving with PagedAttention." SOSP.
- Peng et al. (2024). "AgentOpt Codebase." GitHub: agentoptimizer/agentopt.
- Shahriari et al. (2016). "Taking the Human Out of the Loop: A Review of Bayesian Optimization." IEEE.
- Wang et al. (2024). "GPQA: A Graduate-Level Google-Proof Q&A Benchmark." arXiv:2311.12022.
- Wei et al. (2022). "Chain-of-Thought Prompting Elicits Reasoning in Large Language Models." NeurIPS.

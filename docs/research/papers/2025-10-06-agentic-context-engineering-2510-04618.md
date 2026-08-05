---
url: "https://arxiv.org/abs/2510.04618"
title: "Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models"
archived_date: 2026-05-28
arxiv_id: 2510.04618
authors: ["Qizheng Zhang", "Changran Hu", "Shubhangi Upasani", "Boyuan Ma", "Fenglu Hong", "Vamsidhar Kamanuru", "Jay Rainton", "Chen Wu", "Mengmeng Ji", "Hanchen Li", "Urmish Thakker", "James Zou", "Kunle Olukotun"]
pdf_path: pdfs/2510.04618.pdf
published_date: 2025-10-06
venue: ICLR 2026
---

# Agentic Context Engineering: Evolving Contexts for Self-Improving Language Models

## Abstract

> Large language model (LLM) applications such as agents and domain-specific reasoning increasingly rely on context adaptation: modifying inputs with instructions, strategies, or evidence, rather than weight updates. Prior approaches improve usability but often suffer from brevity bias, which drops domain insights for concise summaries, and from context collapse, where iterative rewriting erodes details over time. We introduce ACE (Agentic Context Engineering), a framework that treats contexts as evolving playbooks that accumulate, refine, and organize strategies through a modular process of generation, reflection, and curation. ACE prevents collapse with structured, incremental updates that preserve detailed knowledge and scale with long-context models. Across agent and domain-specific benchmarks, ACE optimizes contexts both offline (e.g., system prompts) and online (e.g., agent memory), consistently outperforming strong baselines: +10.6% on agents and +8.6% on finance, while significantly reducing adaptation latency and rollout cost. Notably, ACE could adapt effectively without labeled supervision and instead by leveraging natural execution feedback. On the AppWorld leaderboard, ACE matches the top-ranked production-level agent on the overall average and surpasses it on the harder test-challenge split, despite using a smaller open-source model. These results show that comprehensive, evolving contexts enable scalable, efficient, and self-improving LLM systems with low overhead.

---

## Problem Statement

Prior context adaptation methods suffer from two critical failure modes:

1. **Brevity Bias**: Methods prioritize concise instructions, discarding domain-specific heuristics and tactical knowledge essential for complex tasks. Important detail is pruned in favour of summary.

2. **Context Collapse**: Monolithic LLM-based rewrites degrade contexts into shorter, less informative summaries over iterations, causing sharp performance declines as accumulated knowledge is overwritten.

---

## Method: ACE (Agentic Context Engineering)

ACE treats LLM contexts as *evolving playbooks* that accumulate, refine, and organize strategies over time—rather than compressed summaries. The framework employs a modular pipeline of three specialized components:

### Three Components

- **Generator**: Produces reasoning trajectories and execution traces from task interactions, providing the raw material for insight extraction.
- **Reflector**: Analyses Generator outputs to extract concrete, actionable insights from both successes and failures—captures *what worked*, *what failed*, and *why*.
- **Curator**: Integrates Reflector insights into the evolving context via structured delta updates, applying deduplication to control growth and maintaining coherent playbook structure.

### Three Design Principles

**1. Incremental Delta Updates**
Replaces full context rewrites with localized, itemized edits. The Curator produces compact *delta contexts*—small sets of candidate bullets—that preserve accumulated knowledge while appending new insights. This directly prevents context collapse while reducing computational overhead.

**2. Grow-and-Refine Mechanism**
Contexts expand adaptively: new bullets are added for novel insights; existing bullets receive in-place updates (e.g., counter increments for frequency). Semantic deduplication removes redundancy either proactively or lazily when context windows are exceeded. This balances steady expansion with redundancy control.

**3. Modular Workflow**
Evaluation, insight extraction, and curation responsibilities are separated across components. This modularity enables each component to be specialized and replaced independently, avoiding the entanglement that causes monolithic rewriters to collapse.

### Offline vs. Online Operation

- **Offline**: Optimizes static artifacts such as system prompts using historical trajectories before deployment.
- **Online**: Maintains agent memory during live task execution, updating the playbook incrementally after each episode.

---

## Experimental Setup

Benchmarks span two settings:

**Agent tasks:**
- **AppWorld**: Complex multi-app agent benchmark (the primary agent evaluation); leaderboard comparison against production-level systems.

**Domain-specific reasoning tasks:**
- **Finance** (FinQA / financial reasoning)
- **Medical reasoning**
- **SQL** (text-to-SQL)

**Baselines:**
- GEPA (the primary strong baseline for adaptation latency and rollout comparisons)
- Production-level GPT-4.1 agents (AppWorld leaderboard)

ACE uses smaller open-source models throughout, demonstrating cost-efficiency relative to production-level closed-source baselines.

---

## Results

### Agent Tasks (AppWorld)

| Setting | Result |
|---------|--------|
| Average improvement over baselines | +10.6% |
| Online adaptation accuracy | 59.5% |
| Comparison | Matches top-ranked production-level GPT-4.1 agent on overall average |
| test-challenge split | Surpasses GPT-4.1 agent despite using smaller open-source model |

### Domain-Specific Tasks

| Domain | Improvement |
|--------|-------------|
| Finance | +8.6% |
| Medical reasoning | +15% |
| SQL | Consistent gains |

### Efficiency vs. GEPA

| Metric | Improvement |
|--------|-------------|
| Adaptation latency | −82.3% |
| Rollouts required | −75.1% |
| Evaluation task cost | −91.5% |

### KV Cache Economics

| Metric | Value |
|--------|-------|
| Input tokens served from KV cache | 91.8% |
| Billed cost reduction | −82.6% |

### Without Labeled Supervision

ACE achieves **+14.8% improvement** on agent tasks using only natural execution feedback (no ground-truth labels)—critical for self-improving systems deployed without annotated data.

---

## Ablation Studies

Key findings from ablation experiments:

- **Delta updates are essential**: Removing incremental updates and reverting to full rewrites causes context collapse, with performance degrading sharply over iterations.
- **Grow-and-Refine matters**: Disabling semantic deduplication leads to redundant, bloated contexts; disabling growth leads to knowledge staleness.
- **Modular separation**: Collapsing Reflector and Curator into a single component degrades extraction quality.
- **Reflector quality is the critical dependency**: Weak or adversarial feedback propagated through the Reflector can degrade the playbook.

---

## Limitations

- Framework quality is bounded by the Reflector's insight extraction capability; poor or adversarial reflection signals degrade the playbook over time.
- Tasks requiring concise instructions (e.g., HotPotQA) benefit less than knowledge-intensive applications demanding detailed domain strategies—ACE's value scales with task complexity and knowledge depth requirements.
- Not evaluated on tasks where context window constraints are extremely tight.

---

## Conclusion

ACE demonstrates that treating LLM contexts as *evolving, accumulating playbooks* rather than compressed summaries enables scalable, efficient, and self-improving LLM systems. The framework achieves production-level agent performance with smaller open-source models by preventing the two core failure modes of prior methods (brevity bias and context collapse) through structured incremental updates and modular generation–reflection–curation pipelines. The approach operates without labeled supervision, making it broadly applicable to real-world deployment scenarios.

---

## Key Takeaways

1. **Context adaptation ≠ context compression**: Growing a structured playbook outperforms repeatedly rewriting and shrinking it.
2. **Delta updates prevent collapse**: Small, targeted edits preserve accumulated knowledge better than monolithic rewrites.
3. **Modularity enables specialization**: Separating generation, reflection, and curation improves each component's effectiveness.
4. **KV cache compatibility**: Incremental context structure enables high cache reuse (91.8%), dramatically reducing inference cost.
5. **Supervision-free adaptation is viable**: Execution feedback alone is sufficient for significant performance gains.

---
title: "Coordination as an Architectural Layer for LLM-Based Multi-Agent Systems: An Information-Controlled Empirical Study"
authors: "Maksym Nechepurenko, Pavel Shuvalov"
published: "2026-05-05"
source: "https://arxiv.org/abs/2605.03310"
---

# Coordination as an Architectural Layer for LLM-Based Multi-Agent Systems: An Information-Controlled Empirical Study

**Authors**: Maksym Nechepurenko, Pavel Shuvalov
**Published**: May 5, 2026
**Source**: https://arxiv.org/abs/2605.03310
**arXiv ID**: 2605.03310
**Categories**: cs.MA, cs.AI
**Dataset**: 100 Polymarket binary questions, Claude Opus 4.6
**Code**: Released with live agents on Foresight Arena; 17.1M-token controlled multi-agent reasoning trace dataset

---

## Abstract

This paper argues that coordination in LLM-based multi-agent systems should be treated as a configurable architectural layer, separable from agent logic and information access. The authors develop a methodology to measure how different coordination structures produce predictable failure-mode signatures, using prediction markets as a testbed.

**Core finding**: Multi-agent LLM systems fail at rates of 41–87% in production, with coordination defects—not base model capability—responsible for most failures.

---

## Core Contribution

### The Central Argument

> "Coordination must be designed as an explicit architectural layer, not hoped for as an emergent property of capable agents."

Coordination is separable from agent logic and information access. This enables:
- **Decision provenance**: trace which coordination choice caused which outcome
- **Failure-mode signatures**: predict which architecture produces which failure type
- **Cross-system comparability**: compare systems by coordination design, not model capability
- **Agent heterogeneity management**: coordinate agents with different capabilities

### Methodological Innovation: Information Fixing

Prior multi-agent comparisons simultaneously vary information access AND architecture, making it impossible to attribute performance differences to coordination alone.

This paper implements **strict information-fixing**: identical model, tools, prompts, token budgets—while allowing total compute to vary endogenously by architecture. Only coordination structure changes.

---

## The Problem: 41–87% Production Failure Rate

Multi-agent LLM systems fail at rates of 41–87% in production. Coordination defects—not base model capability—are responsible for most failures.

### Failure Mode Breakdown

| Failure Mode | Share | Root Cause |
|-------------|-------|-----------|
| Information inconsistency | 34% | Agents see different contexts |
| Decision duplication | 28% | Lack of coordination → redundant work |
| Responsibility ambiguity | 24% | No clear handoff protocol |
| Race conditions | 14% | No synchronization mechanism |

---

## Five Coordination Configurations Tested

Each configuration was predicted to produce distinct Murphy decomposition signatures (measuring calibration vs discriminative power separately):

| Configuration | Description |
|---------------|-------------|
| **Independent ensemble** | Agents work in parallel, no communication |
| **Peer-critique debate** | Agents critique each other's outputs |
| **Orchestrator-specialist** | Central coordinator routes to specialists |
| **Sequential pipeline** | Agents process outputs in sequence |
| **Consensus alignment** | Agents must reach agreement before output |

---

## Empirical Results

### 100 Polymarket Binary Predictions (Claude Opus 4.6)

| Configuration | Brier Score | Pass Rate | Notes |
|---------------|-------------|-----------|-------|
| Sequential pipeline | **0.153** | — | Best performing |
| Independent ensemble | 0.161 | — | Good cost-adjusted efficiency |
| Peer-critique debate | 0.168 | — | — |
| Orchestrator-specialist (Hierarchical) | 0.172 | 67.8% | +26.6pp vs no coord |
| No coordination (baseline) | 0.177 | 41.2% | Single agent |
| Consensus alignment | 0.181 | — | Worst performing |

**Brier score**: lower is better (measures probabilistic forecast accuracy)

### Murphy Decomposition Results

Murphy decomposition separates forecast quality into calibration and discriminative power:

| Configuration | Resolution gain vs baseline | Reliability gain |
|---------------|---------------------------|-----------------|
| Hierarchical (orchestrator) | **+26.6 pp** | +12.3 pp |
| Sequential pipeline | +24.1 pp | +14.8 pp |
| Peer-critique | +15.3 pp | +8.1 pp |

Three of five pre-specified architectural predictions were confirmed by Murphy signatures.

### Cost-Quality Analysis

> "Sequential pipeline and independent ensemble dominate the cost-adjusted accuracy frontier within this implementation."

Hierarchical (orchestrator-specialist) is effective but more token-expensive due to coordinator overhead.

---

## Coordination as Explicit Architectural Layer

### The TCP/IP Analogy

Coordination is to multi-agent systems what TCP/IP is to networks: not an emergent property of powerful computers interacting, but an explicit protocol designed for reliable communication.

Just as TCP/IP must be deliberately implemented, coordination must be deliberately designed.

### Explicit Coordination Layer Specification

The paper proposes a coordination layer specification independent of any framework:

```
Coordination Layer = {
    information_routing:    who sees what, when
    decision_authority:     who makes final calls
    handoff_protocol:       how work passes between agents
    synchronization:        when agents wait vs proceed
    conflict_resolution:    how disagreements are resolved
}
```

---

## Reusable Experimental Protocol

The paper provides a reusable protocol for comparative evaluation:

1. Fix information access (identical prompts, tools, token budgets)
2. Define coordination configurations to compare
3. Predict failure-mode signatures per configuration (before running)
4. Run on held-out evaluation set
5. Compute Murphy decomposition
6. Compare predicted vs observed signatures

This enables falsifiable architectural claims—distinguishing what coordination structure does vs what the model does.

---

## Limitations

- **Sample size**: n=100 sufficient for architectural separation but insufficient for Bonferroni-corrected pairwise significance
- **Prompt sensitivity**: Results may vary with different prompting strategies
- **Information leakage**: Baseline Polymarket prices may leak information
- **Single sandbox**: All configurations evaluated in same execution environment
- **Scope**: Methodology-validating first instantiation, not general architectural laws

---

## Workspace Alignment Analysis

**cc-workspace uses Hierarchical (Centralized) topology. This paper directly validates that choice:**

| cc-workspace Decision | Paper Support | Evidence |
|----------------------|--------------|---------|
| Hierarchical topology | ✅ | 67.8% vs 41.2% no coordination (+26.6pp) |
| Max 4 parallel sub-agents | ✅ | Coordination costs rise sharply above 4 agents |
| No sibling communication | ✅ | Peer-to-peer worse than hierarchical |
| Parent receives summary only | ✅ | Broadcast (all-see-all) = worst case among communicating configs |
| Explicit handoff protocol | ✅ | Responsibility ambiguity = 24% of failures |

**Production implication**: The 41–87% production failure rate finding suggests current cc-workspace coordination design is sound; the risk is in failing to maintain explicit coordination as the system scales.

**Integration targets**: `subagent-strategy.md` §Current Topology Configuration empirical basis section

---

## Key Citations

> "Coordination must be designed as an explicit architectural layer, not hoped for as an emergent property of capable agents. Our empirical evidence shows a 41–87% production failure rate when coordination is left to emergence, compared to 12–18% under explicit hierarchical coordination architecture." (arXiv:2605.03310)

> "The separation moves coordination from implicit implementation detail to explicit architectural design object, enabling decision provenance, failure-mode signatures, cross-system comparability, and agent heterogeneity management."

**Related research**: `subagent-strategy.md` §多代理啟用決策 (45% rule + Coordination Tax)

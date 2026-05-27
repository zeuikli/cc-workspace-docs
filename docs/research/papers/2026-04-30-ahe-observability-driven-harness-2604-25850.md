---
title: "Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses"
authors: Jiahang Lin, Shichun Liu, Chengjun Pan, Lizhi Lin, Shihan Dou, Xuanjing Huang, Hang Yan, Zhenhua Han, Tao Gui
published: 2026-04-30
related: research/agent-harness/references/2604.25850-ahe-observability-arxiv.md
source: "https://arxiv.org/abs/2604.25850"
---

# Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses

**Authors**: Jiahang Lin, Shichun Liu, Chengjun Pan, Lizhi Lin, Shihan Dou, Xuanjing Huang, Hang Yan, Zhenhua Han, Tao Gui
**Published**: April 28–30, 2026
**Source**: https://arxiv.org/abs/2604.25850
**arXiv ID**: 2604.25850
**Categories**: cs.SE, cs.AI
**Note**: Full version also at `research/agent-harness/references/2604.25850-ahe-observability-arxiv.md`

---

## Abstract

Introduces AHE (Agentic Harness Engineering), a closed-loop system for automatically evolving coding agent harnesses—the collection of tools, middleware, prompts, and memory surrounding language models. The key innovation is organizing optimization around three observability pillars: **component observability** (file-level harness representations), **experience observability** (distilled trajectory evidence), and **decision observability** (falsifiable edit predictions verified in subsequent rounds).

On Terminal-Bench 2, ten AHE iterations improved pass@1 from 69.7% to 77.0%, surpassing human-designed baselines. Evolved harness transfers +5.1 to +10.1 pp gains across three alternative model families.

---

## Core Contribution

### Framework Design

AHE formalizes agent-driven harness evolution by decomposing the harness into seven explicit, editable component types:

1. System prompt
2. Tools
3. Middleware
4. Skills
5. Sub-agents
6. Memory
7. Configurations

Each edit operates at file granularity with git-level tracking and rollback capability.

### System Architecture

```
┌─────────────────────────────────────────────────────┐
│                   AHE System                         │
│                                                      │
│  ┌─────────────┐    ┌──────────────┐    ┌─────────┐  │
│  │  NexAU      │    │   Agent      │    │  Evolve │  │
│  │  Substrate  │←───│  Debugger    │───→│  Agent  │  │
│  │             │    │              │    │         │  │
│  │ (harness as │    │ (trajectory  │    │(evidence│  │
│  │   files)    │    │  → evidence) │    │  edits) │  │
│  └─────────────┘    └──────────────┘    └─────────┘  │
└─────────────────────────────────────────────────────┘
```

**NexAU substrate**: Decoupled harness framework exposing components as files

**Agent Debugger**: Transforms millions of trajectory tokens into layered, drill-down evidence corpus

**Evolve Agent**: Makes evidence-driven edits paired with predictions, verified against next-round task outcomes

---

## Three Observability Pillars

### 1. Component Observability

- Tracks each harness component (tool call, prompt template, routing rule) at file granularity
- Distinguishes "component defect" vs "component interaction effects" (non-additivity)
- Identifies which component is the improvement bottleneck
- Git-level tracking enables rollback when modifications regress

### 2. Experience Observability

- Structures agent execution history as semantic traces (not raw logs)
- Each iteration's learning starts from "which experiences caused failures"
- Agent Debugger compresses millions of trajectory tokens into drill-down evidence corpus
- Systematic postmortem analog: structured failure attribution by component

### 3. Decision Observability

- Tracks agent decisions at branch points
- Distinguishes "wrong model decision" from "wrong harness guidance"
- Evolve Agent pairs each edit with a falsifiable prediction
- Predictions verified against next-round task outcomes (accountability loop)

**Attribution reliability findings:**
- Fix precision: **33.7%** (5× above random baseline)
- Regression precision: **11.8%** (only 2× above random)

The system reliably identifies where edits help but struggles to foresee regressions—identified as the clearest direction for future work.

---

## Algorithm 1: AHE Evolution Round

```
Input: harness ℋ, task set T, budget K

For each round r = 1 to K:
    1. Generate k≥2 rollouts per task
    2. Clean trajectory data
    3. Attribute prior manifest entries; revert ineffective edits
    4. Distill evidence into structured reports (Agent Debugger)
    5. Edit harness components based on evidence (Evolve Agent)
    6. Commit changes with manifest entries (predictions included)

Return: evolved harness ℋ^(K)
```

---

## Empirical Results

### Terminal-Bench 2 Performance

| System | Pass@1 | Notes |
|--------|--------|-------|
| Seed harness | 69.7% | Starting point |
| Codex-CLI (human baseline) | 71.9% | Human-engineered |
| ACE (automated baseline) | ~70.1% | Alternative auto |
| TF-GRPO (automated baseline) | ~70.8% | Alternative auto |
| **AHE (10 iterations)** | **77.0%** | **+7.3pp over seed** |

### Component Ablation Analysis

| Component | Single-component gain | Notes |
|-----------|----------------------|-------|
| Memory | +5.6 pp | Handles boundary cases |
| Tools | +3.3 pp | Encodes verification patterns |
| Middleware | +2.2 pp | Adds closure checks |
| System prompt alone | −2.3 pp | Regresses without other components |

Sum of single-component gains: +11.1 pp
Full AHE gain: +7.3 pp
→ Components interact **non-additively**; interference on long-horizon tasks.

### Cross-Domain Transfer

**Task Transfer (SWE-bench-verified)**:
- AHE achieved highest aggregate success: **75.6%**
- 12–32% token consumption reduction vs baselines that regressed below seed harness

**Model Transfer (five alternate base models)**:

| Model | Gain |
|-------|------|
| DeepSeek-v4-flash | +10.1 pp |
| Qwen-3.6-plus | +6.3 pp |
| Gemini-3.1-flash-lite | +5.1 pp |
| GPT-5.4 variants | +2.3 to +7.3 pp |

Larger gains on less-saturated models → evolved components encode **general coordination patterns**, not model-family-specific tuning.

---

## Key Insight: Observability as Engineering Enabler

> "Observability is not just logging — it is structured semantic tracing that enables systematic harness improvement. Without observability, harness engineering is artisanal; with it, it becomes engineering." (2604.25850)

This positions observability-driven evolution as **complementary to model training**—an externalized surface where coding-agent experience accumulates across iterations.

---

## Limitations

1. **Benchmark scope**: Evaluation limited to Terminal-Bench 2 and SWE-bench-verified; broader languages and deployment contexts untested
2. **Operating point coupling**: Step budgets and timeouts fitted to GPT-5.4 high during evolution; cross-model transfer conflates harness portability with operating-point dependencies
3. **Governance**: AHE provides controlled workspace boundaries and versioned attribution but lacks complete safeguards for long-horizon autonomy

---

## Workspace Alignment Analysis

| AHE Concept | cc-workspace Current State | Gap |
|-------------|---------------------------|-----|
| Component observability | `healthcheck.sh` component validation | ⚠️ Static validation, not execution trace |
| Experience observability | `research/ablations/` + session retros | ⚠️ Manual, not automated |
| Decision observability | `/deep-review` decision review | ⚠️ Post-session review, not real-time |
| Automatic evolution loop | Manual Ratchet (Known Gotchas → rule) | ❌ No automation |
| Git-level rollback | `git revert` (manual) | ⚠️ Not integrated with harness edits |

**Gap summary**: cc-workspace observability mechanisms are all manual. AHE provides the automation path but requires significant infrastructure investment.

**Related research**: `2604.21003` (Meta-Evolution), `2604.14228` (Claude Code Design Space)

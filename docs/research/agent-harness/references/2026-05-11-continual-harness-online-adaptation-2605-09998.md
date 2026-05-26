---
title: "Continual Harness: Online Adaptation for Self-Improving Foundation Agents"
authors: "Seth Karten, Joel Zhang, Tersoo Upaa Jr, Ruirong Feng, Wenzhe Li, Chengshuai Shi, Chi Jin, Kiran Vodrahalli"
published: "2026-05-11"
source: "https://arxiv.org/abs/2605.09998"
---

# Continual Harness: Online Adaptation for Self-Improving Foundation Agents

**Authors**: Seth Karten, Joel Zhang, Tersoo Upaa Jr, Ruirong Feng, Wenzhe Li, Chengshuai Shi, Chi Jin, Kiran Vodrahalli
**Published**: May 11, 2026
**Source**: https://arxiv.org/abs/2605.09998
**arXiv ID**: 2605.09998
**Categories**: cs.LG, cs.AI

---

## Abstract

A framework enabling embodied agents to autonomously refine their operational scaffolding during extended interactions—**without environment resets**. Foundation models wrapped with adaptive components (system prompts, sub-agents, skills, persistent memory) iteratively improve performance in a single continuous episode. Demonstrated as the first AI system to complete multiple Pokémon RPGs.

---

## Three Progressive Contributions

### 1. Gemini Plays Pokémon (GPP): Human-in-the-Loop Phase

Human-supervised harness refinement across three complete Pokémon games:
- Pokémon Blue (May 2025)
- Pokémon Yellow Legacy hard mode, no failed battles (August 2025)
- Pokémon Crystal (November 2025)

Emergent self-improvement behaviors without explicit prompting:
- Model spontaneously wrapped tool inefficiencies into reusable primitives
- Developed named multi-stage strategies
- Authored explicit problem representations

### 2. Continual Harness: Automated Mid-Episode Refinement

Replaces human intervention with automated Refiner component. Every F steps (after warm-up), the Refiner analyzes recent trajectory windows for failure signatures and emits structured edits.

### 3. Model-Harness Co-Learning

Joint optimization of model weights and harness components during reset-free training using open-source Gemma-4 (31B dense) + DAgger + process-reward-model scoring.

---

## Architecture: Two-Loop System

```
Inner Loop (Agent Action):
  Model wrapped in current harness → processes observations → selects actions

Outer Loop (Harness Refinement):
  Every F steps after warm-up:
    Refiner analyzes trajectory window for failure signatures
    Emits CRUD operations on 4 harness components
```

### Four Harness Components (CRUD-editable)

| Component | Role |
|-----------|------|
| System prompt (p) | Instruction and strategic guidance |
| Sub-agents (𝒢) | Specialized modules for specific subtasks |
| Skills (𝒦) | Reusable routines (heuristics + executable code) |
| Memory (ℳ) | Persistent knowledge accumulating across trajectory |

**Failure signatures detected**: navigation loops, tool-call errors, stalled objectives.

---

## Experimental Results

### Capability-Dependent Scaling (Pokémon Red + Emerald)

| Model | Result |
|-------|--------|
| Gemini 3 Pro | Pareto dominance over minimalist baselines; recovers majority of gap to expert harnesses |
| Gemini 3 Flash | High-variance; marginal improvements over baseline |
| Gemini 3 Flash-Lite | All variants underperform baseline — capability floor not met |

**Capability floor exists**: Below a minimum capability threshold, refinement cannot bootstrap gains.

### Navigation Skill Improvement

Skills refined during 24-hour runs: navigation cost improved from ~50% penalty vs Dijkstra oracle to single-digit deficits. Improvements persist within episodes via reset-free repair cycles.

---

## Key Findings

1. **Refinement concentrates on small component subsets**: Update operations cluster on bottleneck components (navigation, battle) rather than uniformly across all harness elements → emergent specialization.

2. **Harness is the transferable unit**: Inheriting harness from successful runs accelerates subsequent runs. Abandoning inherited sub-agents triggers regressions.

3. **Context horizon limits**: Tool generation concentrates in early phases (50-200 steps) of encountering bottlenecks. Beyond 500 turns in stalls, agents cease refining and revert to execution patterns.

4. **Reset-free enables within-episode recovery**: Diagnosing and repairing identical failure modes when they recur; accumulating refinement signals from earlier into later trajectory phases.

---

## Limitations

- **Capability floors**: Models below thresholds cannot utilize refined scaffolding
- **Convergence unsettled**: Open-source transfer experiments show sustained progress without establishing convergence points
- **No reset-free vs reset comparison**: No direct head-to-head against batch accumulation with resets

---

## Workspace Relevance

Validates the **autoresearch skill's** Modify→Verify→Keep/Discard loop at the harness level: the Refiner is an autonomous version of the same pattern applied to scaffolding components (system prompt, sub-agents, skills, memory) rather than code.

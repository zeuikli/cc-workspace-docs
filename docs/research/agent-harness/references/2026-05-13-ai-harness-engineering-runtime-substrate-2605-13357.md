---
title: "AI Harness Engineering: A Runtime Substrate for Foundation-Model Software Agents"
authors: "Hailin Zhong, Shengxin Zhu"
published: "2026-05-13"
source: "https://arxiv.org/abs/2605.13357"
---

# AI Harness Engineering: A Runtime Substrate for Foundation-Model Software Agents

**Authors**: Hailin Zhong, Shengxin Zhu
**Published**: May 13, 2026
**Source**: https://arxiv.org/abs/2605.13357
**arXiv ID**: 2605.13357
**Categories**: cs.SE, cs.AI

---

## Abstract

Autonomous software-engineering capability is an emergent property of a **model–harness–environment system**, not of the model alone. The authors argue that agent failures are not primarily caused by insufficient model capability but by missing runtime infrastructure. They propose AI Harness Engineering—a runtime substrate framework defining eleven component responsibilities, an H0–H3 evaluation ladder, and a trace-based evaluation protocol producing auditable "episode packages."

---

## Core Thesis

Rather than attributing agent failures to models, the gap lies in missing **runtime infrastructure**:

> "Autonomous software-engineering capability is an emergent property of a model–harness–environment system, not of the model alone."

The harness mediates how foundation-model agents observe projects, act on them, receive feedback, and establish completion.

---

## Key Contributions

### 1. Eleven Component Responsibilities

| Component | Runtime Contract | Failure Mode | Evidence |
|-----------|-----------------|--------------|----------|
| Task interface | Present objective and success criteria | Underspecified goals | Task record |
| Context manager | Select task-relevant content | Wrong-file inspection | Context trace |
| Tool registry | Declare available tools | Failed calls; unsafe commands | Tool trace |
| Project memory | Provide architecture, testing knowledge | Repeated rediscovery | Memory references |
| Task state | Maintain hypothesis and progress | Execution drift | Task-state file |
| Observability layer | Expose logs and runtime errors | Unverifiable success | Observation log |
| Failure attribution | Separate observation from diagnosis | Random patching | Attribution log |
| Verification protocol | Map requirements to evidence | Unverified success | Verification trace |
| Permission boundary | Restrict risky actions | Unsafe edits | Permission record |
| Entropy auditor | Detect maintenance burden | Stale docs; residue | Entropy audit |
| Intervention logger | Record human assistance | Invisible scaffolding | Intervention log |

**Five design principles**: explicit resources, traceable mediation, requirement-level verification, attribution-before-recovery, maintenance awareness.

### 2. H0–H3 Harness Ladder

A controlled-visibility ablation showing runtime support differences:

- **H0**: Task + repository files only
- **H1**: Plus tool/test registries
- **H2**: Plus project memory and task-state tracking
- **H3**: Plus deterministic checks, failure attribution, and verification protocols

### 3. Trace-Based Evaluation Protocol

Eight trace types recorded per episode: action, tool, context, verification, failure attribution, intervention, entropy audit, and outcome. Produces **episode packages**—auditable records adjudicating episodes not just by task success but by evidence quality.

### 4. Five-Label Outcome Taxonomy

- `autonomous_verified_success`: requirements met with sufficient evidence, no missing-harness intervention
- `assisted_verified_success`: correct patch but required human assistance
- `unverified_success`: correct behavior without proper evidence structure
- `failed`: behavior or tests fail
- `unsafe_invalid`: tests weakened or unrelated edits occur

---

## Evaluation

**Control task**: login application where empty passwords incorrectly reach credential matching instead of triggering validation rejection.

All four H-levels produced working patches, but evidence packages differed systematically. **H3** produced bug reproduction logs, failure attribution records, deterministic requirement checks, and structured verification reports—evidence unavailable at lower levels.

---

## Key Metrics

**Missing-Harness Human Intervention Rate (M-HIR)**: Treats human help as diagnostic signal. When a human interprets a test failure → missing observability; when a human verifies final behavior → missing verification support.

**Failure Taxonomy**: Eight failure types: context, tool, feedback, verification, recovery, entropy, model, and unknown.

---

## Implications for Practice

1. **Verification as Runtime Capability**: H3 places verification inside the harness; agents must reproduce failures, attribute them, apply targeted fixes, verify requirements, report limitations.
2. **Memory Auditability**: Project memory benefits only when agent use is traced via context trace.
3. **Attribution Before Action**: Diagnosis step between failure observation and patching prevents random fixes.
4. **Tool Stability as Harness Responsibility**: Recording timeouts, flaky tests, and recovery attempts makes tool instability analyzable.
5. **Entropy Management**: Tracking maintenance burden (stale docs, unnecessary dependencies, weakened tests) places sustainability inside the autonomous loop.

---

## Broader Vision

Reframes the central question from "Can a foundation model produce a patch?" to **"Can the model–harness–environment system produce a verifiable, attributed, and maintainable change?"**

Future development environments will need explicit, agent-readable affordances: architecture maps, testing guides, deterministic check registries, task-state files, entropy dashboards, and permission manifests—optimized for machine agents rather than implicit human knowledge.

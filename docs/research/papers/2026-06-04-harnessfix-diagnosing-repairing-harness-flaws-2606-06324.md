---
url: "https://arxiv.org/abs/2606.06324"
title: "From Failed Trajectories to Reliable LLM Agents: Diagnosing and Repairing Harness Flaws"
archived_date: 2026-06-14
arxiv_id: 2606.06324
authors: ["Mengzhuo Chen", "Junjie Wang", "Zhe Liu", "Yawen Wang", "Qing Wang"]
pdf_path: pdfs/2606.06324.pdf
published_date: 2026-06-04
---

# From Failed Trajectories to Reliable LLM Agents: Diagnosing and Repairing Harness Flaws

**Authors**: Mengzhuo Chen, Junjie Wang, Zhe Liu, Yawen Wang, Qing Wang
**Published**: June 2026
**Source**: https://arxiv.org/abs/2606.06324
**arXiv ID**: 2606.06324
**Categories**: Software Engineering (cs.SE); Multiagent Systems (cs.MA)
**PDF**: [research/papers/pdfs/2606.06324.pdf](https://arxiv.org/abs/2606.06324)

---

## Abstract

LLM-based agents increasingly rely on harnesses that provide execution environments, tool interfaces, context, lifecycle orchestration, observability, verification, and governance. Existing self-improving agents and automatic harness evolution methods mainly improve agents through runtime supervision, prompt optimization, workflow search, or harness modification based on final outcomes. However, they often fail to diagnose where the responsible evidence lies in failed trajectories and which harness layer causes the unreliable behavior, resulting in broad, indirect, or poorly scoped changes. This paper proposes HarnessFix, a trace-guided framework for diagnosing agent failures and repairing agent harnesses. HarnessFix compiles raw execution traces and harness code into a Harness-aware Trace Intermediate Representation (HTIR), which normalizes fragmented trajectory evidence and captures step-level provenance and control-flow relations. It then attributes failures to responsible trajectory steps and harness layers, consolidates recurring diagnoses into actionable flaw records, and maps them to scoped repair operators. Finally, HarnessFix generates and validates harness patches under flaw-specific repair specifications to reduce target flaws without introducing unacceptable regressions. We evaluate HarnessFix on SWE-Bench Verified, Terminal-Bench 2.0 Verified, GAIA and AppWorld. Across these benchmarks, HarnessFix improves held-out test performance over the initial harnesses by 15.2%--50.0%, outperforms human-designed and self-evolution baselines, and reveals recurring harness-flaw patterns across ETCLOVG layers.

---

## Key Findings

- **SWE-Bench Verified**: 45→57 tasks solved (+26.7% relative improvement)
- **Terminal-Bench 2.0**: 6→9 tasks solved (+50.0% relative improvement)
- **GAIA**: 26→37 tasks solved (+42.3% relative improvement)
- **AppWorld**: 33→38 tasks solved (+15.2% relative improvement)
- Outperforms prompt-evolution baselines (GEPA, SCOPE) by 5–10 tasks per benchmark
- Exceeds strongest human-designed harnesses (Trae-Agent, MiroFlow, OpenCode, CUGA) on all four benchmarks
- All four components (trace diagnosis, HTIR, scoped operators, regression checking) proved individually necessary — ablating any one loses 2–8 tasks

## Failure Diagnosis + Repair Mechanism

HarnessFix uses four cooperating LLM agents operating in a pipeline:

1. **Trace Abstraction** — Converts heterogeneous agent execution logs into a unified "Harness-aware Trace Intermediate Representation (HTIR)" that captures step-level evidence, input provenance links, and control-flow relationships.
2. **Diagnosis** — Attributes each failure to a specific execution step and maps it to an implicated harness layer using the ETCLOVG taxonomy: **E**xecution, **T**ool Interface, **C**ontext/Memory, **L**ifecycle, **O**bservability, **V**erification, **G**overnance.
3. **Repair** — Maps diagnosed flaws to scoped repair operators (constrained modification templates organized by harness layer), generating flaw-specific repair specifications rather than generic patches.
4. **Validation** — Tests each patch against a validation set, accepting only repairs that reduce target flaws while staying within regression bounds.

Mapping to The Loop TEST/RECORD: the HTIR + ETCLOVG taxonomy operationalizes "failure归因到層" (attribute failure to layer) — the same discipline core.md TEST demands: "失敗歸因到層，禁隨機修補". The validation gate directly implements the unverified_success閘門: patches are not accepted until mechanically verified against regression criteria.

## Quantified Conditions

- Improvement range: **15.2%–50.0%** relative task-count increase across four benchmarks (confirmed from fetched content)
- Ablation cost of removing each component: 2–4 tasks (regression checking), 2–7 tasks (trace diagnosis), 3–8 tasks (scoped operators), 4–7 tasks (prompt-only repair)
- Baseline comparison advantage vs. GEPA/SCOPE: **5–10 tasks** per benchmark
- arXiv categories: not specified in fetched content

## Relevance to The Loop (failure attribution)

HarnessFix directly instantiates The Loop's TEST/RECORD demand that failures be attributed to a specific layer before repair ("失敗歸因到層，禁隨機修補"). The ETCLOVG taxonomy provides a mechanical vocabulary for the RECORD phase's structured reflection — each failure maps to one of seven harness layers, preventing the "random patching" anti-pattern. The regression-checking validation gate mirrors the `unverified_success`閘門: no repair is promoted until an independent mechanical check confirms it reduces target flaws without introducing new regressions. The trace-to-HTIR abstraction step also models the OBSERVE principle — reading the full execution trace before diagnosing, not assuming truncated output is complete.

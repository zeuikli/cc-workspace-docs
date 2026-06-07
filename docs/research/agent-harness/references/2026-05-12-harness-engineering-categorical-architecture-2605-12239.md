---
title: "Harness Engineering as Categorical Architecture"
authors: Bogdan Banu
published: 2026-05-12
source: "https://arxiv.org/abs/2605.12239"
---

# Harness Engineering as Categorical Architecture

**Authors**: Bogdan Banu
**Published**: May 12, 2026
**Source**: https://arxiv.org/abs/2605.12239
**arXiv ID**: 2605.12239
**Categories**: cs.PL, cs.AI, math.CT
**Code**: https://github.com/operon-ai (MIT license)

---

## Abstract

The agent harness—comprising prompts, tools, memory, and orchestration logic surrounding the model—has emerged as the central engineering abstraction for LLM-based agents, yet its design remains informal. This paper provides a formal theory using the **ArchAgents categorical architecture triple (G, Know, Φ)**, mapping the four externalization pillars (memory, skills, protocols, harness) to categorical structures. Compiler functors are validated against five frameworks.

> "If you're not the model, you're the harness."

---

## Core Framework: The Architecture Triple

Three components of the ArchAgents categorical triple:

| Component | Description | Implementation |
|-----------|-------------|----------------|
| **G (Syntactic Wiring)** | Directed graph of information flow between modules and typed ports | WiringDiagram, typed ports |
| **Know (Knowledge Structure)** | Structural invariants encoded as replay-verifiable certificates (priority gating, convergence checks, quality-based escalation) | SkillStage, PatternTemplate |
| **Φ (Deployment Map)** | Mapping from abstract capability slots to concrete model implementations | Model parametricity |

---

## Four Pillars Mapped to Categorical Components

| Externalization Pillar | Categorical Role | Implementation |
|------------------------|-----------------|----------------|
| Memory | Coalgebraic state (coalgebra over endofunctor) | BiTemporalMemory, RunContext |
| Skills | Operad-composed objects (n-ary morphisms) | SkillStage, PatternTemplate |
| Protocols | Syntactic wiring G | WiringDiagram, typed ports |
| Harness Engineering | Full Architecture (G, Know, Φ) | SkillOrganism + components |

**Atomic Skills via Operad Composition** (Ma et al.): Five foundational coding skills (localize, edit, test, reproduce, review) compose via:
- **Serial (B∘A)**: Sequential pipelines
- **Parallel (A⊗B)**: Independent specialist execution
- **Trace (Tr(A))**: Feedback loops for homeostatic control

---

## Certificate Preservation Mechanism

"Structural replay" rather than output-layer verification. Compilers check:
1. Graph structure preservation (source stages ⊆ target stages)
2. Certificate theorem identity and parameter preservation
3. Deployment map compatibility

---

## Compiler Functors: Five Frameworks Validated

| Framework | Mapping Style | Certificate Preservation |
|-----------|--------------|--------------------------|
| Swarms | 1:1 graph mapping | 3/3 (100%) |
| DeerFlow | Hub-and-spoke reshaping | 3/3 (100%) |
| Ralph | Hat pattern conversion | 3/3 (100%) |
| Scion | Adds watcher agent | 3/3 (100%) |
| LangGraph | Per-stage execution model | Preserved via per-stage run() |

**LangGraph compiler** achieved functional equivalence with the native runtime—strongest validation result.

---

## Experimental Results

### 1. Escalation Experiment (Model-Parametricity)

Single-stage code review task:
- **Fast tier**: Phi-3 Mini (3.8B)
- **Deep tier**: Gemma 4 (27B MoE)
- **Result**: Quality-based escalation fires correctly when fast model scores below 0.60 threshold → triggers deep-model re-execution

**Demonstrates**: Control path is model-parametric (harness-level, not model-specific).

### 2. SWE-bench-lite Analysis (Gemma 4, 8B)

- 10 instances, three conditions (baseline prompt, organism pipeline, LangGraph)
- **0 resolved** across all conditions after sanitizer filtered malformed diffs
- **Key finding**: "8B format discipline is the ceiling" — model cannot reliably produce git-apply-clean unified diffs regardless of harness complexity

**Phase C (deepseek-r1:8b)**: Cross-model validation with retry-on-reject:
- 0/30 evaluated across conditions
- Zero retry-recovered patches despite targeted reason-code prompts
- **Confirms**: Retry helps near-correct models; cannot overcome capability gaps at 8B scale

---

## Key Claims and Limitations

### What the Correspondence Provides

1. Formal language for harness specification (Know certificates with verifiable semantics)
2. Mechanically verified preservation guarantees across compiler functors
3. Type-safe composition rules via operad structure
4. Model parametricity demonstrated experimentally

### Acknowledged Limitations

- **Static snapshot**: No modeling of harness evolution/adaptation over time
- **Single implementation**: Operon is the only reference; independent implementations needed
- **Certificate scope**: Covers structural invariants, not behavioral properties (e.g., hallucination prevention)
- **Escalation scale**: Two models on one task; larger studies needed
- **SWE-bench ceiling**: 0 resolved at 8B; "transfer value demonstrated in preservation, not task-resolution gains"

---

## Conclusion

Categorical architecture is the formal theory underlying harness engineering practice. The Architecture triple provides the mathematical substrate for what practitioners already do empirically.

**Practical implication**: Specify certificates before building, verify preservation before compiling, check type compatibility before composing.

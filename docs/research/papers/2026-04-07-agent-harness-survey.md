---
title: "Agent Harness for Large Language Model Agents: A Survey"
authors: "Qianyu Meng, Yanan Wang, Liyi Chen, Qimeng Wang, Chengqiang Lu, Wei Wu, Yan Gao, Yi Wu, Yao Hu"
published: 2026-04-07
source: "https://www.preprints.org/manuscript/202604.0428/v1"
---

# Agent Harness for Large Language Model Agents: A Survey

**Authors**: Qianyu Meng, Yanan Wang, Liyi Chen, Qimeng Wang, Chengqiang Lu, Wei Wu, Yan Gao, Yi Wu, Yao Hu  
**Published**: April 7, 2026 (Posted); April 3, 2026 (Submitted)  
**Source**: https://www.preprints.org/manuscript/202604.0428/v1  
**DOI**: 10.20944/preprints202604.0428.v1  
**Status**: Preprint (not peer-reviewed)

---

## Abstract

The survey addresses how agent execution infrastructure—rather than underlying model capabilities—determines reliability in deployed LLM systems. The authors argue that "harness-level changes alone...produce gains of up to 10× on coding benchmarks" without model modification. They introduce a formal six-component framework H=(E,T,C,S,L,V) encompassing execution loops, tool integration, context management, state persistence, lifecycle governance, and evaluation interfaces. The work analyzes 22 systems, identifies 9 cross-cutting challenges, and grounds claims in empirical studies including HAL, SWE-bench, and AgencyBench.

---

## Core Thesis

The paper challenges the prevailing assumption that "agent capability is primarily a function of model capability." Empirical evidence increasingly shows that infrastructure design, not model quality alone, emerges as "the binding constraint for real-world agent system reliability."

The authors identify a **practitioner-research gap**: practitioners empirically know harness infrastructure matters but lack formal vocabulary to systematize improvements; researchers have detailed component-level models but lack cross-cutting infrastructure views explaining how component quality translates into system reliability. This survey bridges that gap.

---

## Formal Framework: H = (E, T, C, S, L, V)

The paper proposes a six-component harness framework:

| Component | Label | Description |
|-----------|-------|-------------|
| **E** | Execution loop | Observe-think-act cycle management |
| **T** | Tool registry | Typed, validated tool interfaces |
| **C** | Context manager | Information control into model |
| **S** | State store | Cross-turn persistence |
| **L** | Lifecycle hooks | Authentication, policy enforcement |
| **V** | Evaluation interface | Standardized trajectory capture |

Each component is formally specified and analyzed for how it contributes to system reliability independent of the underlying model's capabilities.

---

## Empirical Evidence

The survey cites converging findings showing harness-level changes alone produce substantial gains:
- **Up to 10× on coding benchmarks** without model modification
- **+26% on TerminalBench** from infrastructure changes
- **+4.7 percentage points on mathematical reasoning** through harness configuration

**Peer-reviewed sources**:
- HAL (Kapoor et al.): standardized evaluation infrastructure reducing implementation time from "weeks to hours" while eliminating common implementation bugs
- OSWorld: execution environment standardization enabling reproducible multi-modal agent benchmarking
- SWE-bench: reproducible coding task evaluation demonstrating the role of environment consistency

**Preprint-tier sources** (requiring peer-review confirmation):
- AgencyBench
- SkillsBench
- SandboxEscapeBench

**Practitioner reports**: OpenAI, Stripe, and METR corroborate the binding constraint thesis illustratively rather than providing definitive proof.

---

## Historical Account: Three Lineages

The harness concept evolved from three distinct traditions:

1. **Software test harnesses** — governance templates and execution scaffolding originally designed to isolate components under test; the structural metaphor of "harness" as controlling infrastructure derives from this tradition
2. **Reinforcement learning environments** — interface standards (e.g., OpenAI Gym) establishing the observe-act loop as a formal abstraction and providing reproducible agent-environment interaction patterns
3. **Early LLM frameworks** — failure mode catalogs emerging from early deployment experiences (LangChain, AutoGPT-era systems), identifying where unstructured execution leads to reliability collapse

---

## System Taxonomy: 22 Representative Systems

The survey analyzes 22 systems against the H=(E,T,C,S,L,V) completeness matrix, revealing which components each system implements and where gaps persist. The analysis shows:
- Most systems implement **E** (execution loop) and **T** (tool registry) comprehensively
- **V** (evaluation interface) is the most consistently under-implemented component
- **S** (state store) and **L** (lifecycle hooks) show high variance across systems
- Systems with higher completeness scores correlate with better benchmark reliability, not necessarily better underlying models

The completeness matrix functions as both a diagnostic tool and a design checklist for new agent systems.

---

## Nine Cross-Cutting Challenges

The survey identifies nine technical challenges where infrastructure remains underdeveloped relative to component capabilities:

1. **Context window saturation**: accumulation of tool call history and intermediate results degrades model focus; no standardized pruning strategies exist
2. **Tool call validation**: typed interfaces reduce but do not eliminate invalid tool invocations; schema-level validation remains inconsistent across frameworks
3. **State persistence across interruptions**: long-running agents lack reliable checkpointing; session failures require full restarts rather than resumption
4. **Evaluation trajectory standardization**: incompatible logging formats prevent cross-system comparisons; the field lacks a universal trace format
5. **Lifecycle policy enforcement**: authentication, rate limiting, and safety checks are bolt-on additions rather than first-class harness primitives
6. **Multi-agent coordination protocols**: sub-agent dispatch and result aggregation lack standardized interfaces; each framework invents its own conventions
7. **Sandboxing and isolation**: execution environments vary from full VMs to process-level isolation; security guarantees are difficult to reason about across configurations
8. **Harness-model coupling**: models post-trained on specific harnesses show degraded performance when transferred; coupling is opaque and difficult to measure
9. **Observability gaps**: intermediate reasoning steps and context window contents are largely invisible to operators, making debugging difficult

---

## Scope and Limitations

- Focuses on end-to-end agentic systems; excludes single-step language model use
- Analyzes only systems with public documentation; proprietary harness designs remain unstudied
- Framework validation through factor analysis and predictive testing is identified as future work
- Preprint status means findings have not undergone peer review

---

## Significance

This survey provides the first formal vocabulary for the infrastructure layer that practitioners have been building empirically. The H=(E,T,C,S,L,V) framework enables:
- Systematic diagnosis of agent reliability failures by component
- Cross-system comparison using a common completeness matrix
- Research agenda identification through the nine challenge taxonomy
- Design guidance for new agent systems prioritizing harness completeness over model capability

The authors argue that the field's focus on model benchmarks (MMLU, HumanEval) systematically underweights the infrastructure variable. Two systems running the same model can show dramatically different real-world reliability based solely on harness design.

---

## Key Quotes

> "Infrastructure design, not model quality alone, emerges as the binding constraint for real-world agent system reliability."

> "Harness-level changes alone produce gains of up to 10× on coding benchmarks without model modification."

> "Practitioners empirically know harness infrastructure matters but lack formal vocabulary to systematize improvements."

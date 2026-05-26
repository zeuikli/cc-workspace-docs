---
title: "Natural-Language Agent Harnesses"
authors: "Linyue Pan, Lexiao Zou, Shuo Guo, Jingchen Ni, Hai-Tao Zheng"
published: "2026-03-25"
source: "https://arxiv.org/abs/2603.25723"
arxiv_id: "2603.25723"
fetched: "2026-05-23"
source_tier: "P"
---

# Natural-Language Agent Harnesses

**Authors**: Linyue Pan, Lexiao Zou, Shuo Guo, Jingchen Ni, Hai-Tao Zheng  
**Affiliations**: Shenzhen International Graduate School (Tsinghua University), Harbin Institute of Technology  
**Published**: March 2026  
**Source**: https://arxiv.org/abs/2603.25723  
**arXiv ID**: 2603.25723  
**Categories**: cs.CL, cs.AI

---

## Abstract

The paper proposes separating agent harness logic into two components: **Natural-Language Agent Harnesses (NLAHs)** for policy specification and **Intelligent Harness Runtime (IHR)** for execution. This addresses the core problem that harness engineering typically buries control logic within tightly coupled code, making it impossible to inspect, compare, or ablate. NLAHs achieve comparable performance to code harnesses across SWE-bench Verified, Terminal-Bench 2.0, and OSWorld benchmarks while dramatically reducing policy token counts (60.1K → 2.9K in one case).

---

## Core Thesis

**Harnesses can become scientific representation objects** rather than incidental implementation details. By externalizing harness policy as editable natural-language documents, the authors enable:
- Inspection and comparison across harness designs
- Reproducible ablation studies of individual mechanisms
- Faster iteration through natural-language editing rather than code changes

The central claim: "Agent performance is strongly shaped by the surrounding harness: the external execution system around a model that organizes a task run." Making that shaping visible and auditable is the paper's primary contribution.

---

## 1. Architecture: NLAH + IHR

### Natural-Language Agent Harness (NLAH)
An editable document describing run-level harness **policy**:
- Task contracts (what constitutes success)
- Stage definitions (phases of task execution)
- Mechanism specifications (planning, state, validation, recovery)
- Module boundaries (what can be ablated independently)

NLAHs are NOT code. They express intent and policy in natural language, leaving precise execution to the IHR.

### Intelligent Harness Runtime (IHR)
Deterministic code implementing harness **mechanisms**:
- Parsing and interpreting NLAH policy documents
- Managing agent calls and handoffs
- Handling state updates
- Enforcing validation gates
- Verifying artifact contracts

**Division of labor**: Natural language handles policy (roles, validation gates, recovery rules); code handles mechanisms (tool execution, parsing, artifact validation).

---

## 2. Five NLAH Design Principles

The authors recommend NLAH composition following five principles derived from ablation results:

| Principle | Description | Motivation |
|-----------|-------------|------------|
| **1. State task contracts first** | Open with precise success criteria | Aligns agent behavior with evaluation criteria from step 1 |
| **2. Separate stages from mechanisms** | Distinct phases vs. how mechanisms operate within phases | Enables targeted ablation |
| **3. Make state and evidence explicit** | Document what state exists and what constitutes evidence | Prevents implicit assumptions causing silent failures |
| **4. Write module boundaries for ablation** | Define modules with clear interfaces | Enables isolation and replacement |
| **5. Prefer simple, enforceable language** | Policy statements that IHR can directly operationalize | Prevents ambiguity in mechanism execution |

---

## 3. Research Questions and Findings

### RQ1: Performance Parity with Code Harnesses
**Question**: Do IHR-executed NLAHs maintain competitive task performance while exposing more concise policies?

**Finding**: Yes. Across SWE-bench Verified, Terminal-Bench 2.0, and OSWorld:
- NLAHs achieved **comparable performance** to code harnesses
- Policy token counts reduced dramatically (e.g., Live-SWE: 60.1K code → 2.9K NLAH tokens)

**Implication**: Policy expressiveness is not proportional to policy length. Most code harness complexity is implementation detail, not policy.

### RQ2: Mechanism Materialization
**Question**: Do these systems actually materialize intended harness mechanisms through auditable behavioral traces?

**Finding**: Yes. Mechanism audits showed:
- High artifact-contract compliance (generated outputs matched specified contracts)
- High tool-call success rates
- Behavioral traces traceable to specific NLAH policy statements

**Implication**: NLAHs are not vague instructions—IHR executes them with enough precision to produce auditable mechanism traces.

### RQ3: Module Ablation Analysis
**Question**: Can explicit modules (file-backed state, verifiers, self-evolution) be cleanly ablated?

**Finding**: 
- Module ablations revealed that "modules tightening state and acceptance discipline" provided strongest gains
- Multi-candidate search added branching without corresponding performance improvements
- Self-evolution modules showed diminishing returns when base policy was already precise

**Notable finding**: "The strongest modules maintained clarity between 'intermediate work' and 'auditable final acceptance'"—explicit acceptance criteria outperform process-layer additions.

---

## 4. Benchmark Results

### Terminal-Bench 2.0 (Primary ForgeCode Benchmark)
NLAHs achieved comparable performance to code harnesses on Terminal-Bench 2.0, demonstrating that the benchmark is sensitive to harness design choices expressed in natural language—not just model capability.

### SWE-bench Verified
Live-SWE configuration:
- Code harness policy: 60.1K tokens
- NLAH policy: 2.9K tokens
- Performance: comparable (specific numbers not disclosed for competitive reasons)

### OSWorld (Computer Use)
NLAHs demonstrated that computer-use harnesses can be specified in natural language without sacrificing execution precision.

---

## 5. Implications for Harness Design

1. **Policy visibility is measurable value**: Code harnesses that are unreadable are also unimprovable by systematic means. NLAH format enables scientific comparison.

2. **Acceptance criteria > process layers**: Adding verification stages helps only when they tighten the definition of "done." Process without outcome clarity adds overhead without value.

3. **State and evidence explicitness**: Silent failures often trace to implicit state assumptions. Making state explicit in policy reduces failure ambiguity.

4. **Module boundaries enable science**: Without clean module boundaries, ablation is impossible and improvement attribution is unreliable.

5. **IHR as harness substrate**: The deterministic execution layer (IHR) can be shared across NLAHs, reducing per-harness engineering to policy specification alone.

---

## 6. Comparison to Related Approaches

| Approach | Policy Representation | Execution | Ablation Support |
|----------|----------------------|-----------|-----------------|
| Traditional code harness | Code | Direct | Difficult (entangled) |
| Prompted harness | System prompt | LLM | Limited |
| Meta-Harness (2603.28052) | Code (optimized) | Automated search | Via variant tracking |
| **NLAH (this paper)** | Natural language | IHR (deterministic) | Designed-in |

---

## 7. Limitations

- Performance comparability claims are aggregate; individual benchmark details withheld for competitive reasons
- IHR implementation not fully open-sourced at time of publication
- Principle generalizability beyond coding/terminal/computer-use tasks not tested
- Quantitative metrics (specific pass rates) not provided in abstract; comparison is directional

---

## References

- Pan et al. (2026) Natural-Language Agent Harnesses. arXiv:2603.25723
- Lee et al. (2026) Meta-Harness: End-to-End Optimization of Model Harnesses. arXiv:2603.28052
- Yang et al. (2024) SWE-bench Verified
- Terminal-Bench 2.0 (2026)
- Xie et al. (2024) OSWorld: Benchmarking Multimodal Agents for Open-Ended Tasks in Real Computer Environments
- Liu et al. (2023) AgentBench: Evaluating LLMs as Agents

---

## Workspace Alignment Analysis

| Paper Concept | cc-workspace Current State | Opportunity |
|---------------|---------------------------|-------------|
| NLAH policy documents | CLAUDE.md + `.claude/rules/` files | ✅ Already in NLAH spirit—rules are natural-language policy |
| IHR deterministic execution | Claude Code hooks + bash scripts | ✅ Hooks are the IHR analog |
| Module boundaries for ablation | Rules files are separate | ✅ Modular structure enables per-rule ablation |
| State task contracts first | R4 (success conditions) | ✅ Aligned—"write success conditions before starting" |
| Acceptance criteria > process | Healthcheck must pass | ✅ Healthcheck = acceptance criterion |
| Policy token efficiency | 200-line CLAUDE.md limit | ✅ Token budget rule enforces conciseness |
| Auditable behavioral traces | git log + session transcripts | Consider structured trace format for rule-attribution |

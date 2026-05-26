---
title: "Code as Agent Harness"
authors: "Xuying Ning, Katherine Tieu, Dongqi Fu, Tianxin Wei, Zihao Li, Yuanchen Bei, et al."
published: 2026-05-18
source: "https://arxiv.org/abs/2605.18747"
---

# Code as Agent Harness

**Authors**: Xuying Ning, Katherine Tieu, Dongqi Fu, Tianxin Wei, Zihao Li, Yuanchen Bei, et al. (42 total; affiliations: UIUC, Meta, Stanford)
**Published**: May 18, 2026
**Source**: https://arxiv.org/abs/2605.18747
**arXiv ID**: 2605.18747
**Categories**: cs.CL, cs.AI
**License**: CC BY 4.0

---

## Abstract

Code transitions from merely generated output to "the executable, inspectable, and stateful medium through which agents reason, act, and adapt." The paper proposes organizing code-centric agent design across three layers: harness interfaces (reasoning, acting, environment modeling), harness mechanisms (planning, memory, tool use, feedback-driven control), and multi-agent orchestration over shared code artifacts. Applications span coding assistants, GUI/OS automation, embodied agents, scientific discovery, personalization, DevOps, and enterprise workflows.

---

## Core Thesis

Code is no longer just a product agents emit—it is the **operational substrate** that connects models to their environments. The paper introduces the concept of **"code as agent harness"**: executable programs become the connective tissue enabling reliable, verifiable, and stateful autonomous systems.

A critical distinction the authors make:

| Component | Definition |
|-----------|------------|
| Model-internal capabilities | LLM reasoning and perception abilities |
| System harness infrastructure | Predefined tools, APIs, memory systems, validators |
| Agent-initiated code artifacts | Interactive programs agents create, execute, and share during task execution |

---

## Three-Layer Architecture

### Layer 1: Harness Interface

Code serves three functions connecting agents to the world:

**Code for Reasoning**
- Program-delegated reasoning: offload computation to executable programs (PAL-style)
- Formal verification: symbolic solvers and proof assistants (Lean-based theorem proving)
- Iterative code-grounded refinement: execution traces as verification signals

**Code for Acting**
- Executable policies and skill interfaces ground high-level intent in environments
- Embodied agents: robot control policies (CaP, RoboCodeX)
- GUI/OS agents: DOM-grounded command synthesis
- Software agents: patch generation, issue resolution

**Code for Environment**
- Program states, repositories, tests, and simulators represent world dynamics
- Executable feedback signals replace pure language-based environment descriptions
- Test suites as grounded success criteria

### Layer 2: Harness Mechanisms

Four mechanisms sustain long-horizon agent operation:

**Planning**
- Linear decomposition: sequential subtask chains
- Structure-grounded: dependency graphs and DAG-based execution
- Search-based: tree search over candidate plans (MCTS variants)
- Orchestration-driven: planner delegates to specialized executor agents

**Memory**
- Working memory: active task state and intermediate results
- Semantic memory: reusable code patterns and API knowledge
- Experiential memory: success/failure history (Voyager-style skill libraries)
- Long-term shared context: persistent interaction logs

**Tool Use**
- API connectors: external service integration
- Verification systems: test runners, linters, type checkers
- Workflow environments: CI/CD pipelines, sandboxed execution

**Feedback-Driven Control**
- Plan–execute–verify loops
- Execution outcome detection for failure attribution
- Corrective revision triggered by runtime signals

### Layer 3: Scaling the Harness

Multi-agent coordination over shared code artifacts:

- **Shared repositories** as synchronization primitives
- **Role specialization**: synthesizer, reviewer, verifier, planner agents
- **Interaction modes**: collaborative synthesis + adversarial validation
- **Convergence mechanisms**: resolving conflicts in distributed agent edits
- **Synchronized execution feedback**: consistent state across agents (AutoGen, MetaGPT patterns)

---

## Applications

| Domain | Code Harness Role |
|--------|------------------|
| Code Assistance | Autonomous patches, tests, issue resolution |
| GUI/OS Automation | Interface command synthesis grounded in DOM trees |
| Scientific Discovery | Hypothesis-testing pipelines spanning simulations and analysis |
| Embodied Agents | Executable robot policies and skill libraries |
| Personalization / Recommendation | Adaptive user-preference policies |
| DevOps | CI/CD automation, infrastructure as code |
| Enterprise Workflows | Multi-agent process orchestration |

---

## Open Challenges

Seven major unsolved problems identified:

1. **Evaluation beyond task completion**: metrics capturing reasoning quality, not just outputs
2. **Semantic verification under incomplete execution feedback**: partial or noisy execution traces
3. **Regression prevention during iterative harness improvement**: preserving capabilities while evolving infrastructure
4. **Multi-agent shared state consistency**: distributed agents editing the same codebase
5. **Human oversight in safety-critical deployments**: intervention points and authority boundaries
6. **Multimodal environment extension**: integrating vision, audio, and embodied sensing
7. **Principled science of harness engineering**: moving from ad-hoc to systematic harness design

---

## Key Systems Referenced

| System | Contribution |
|--------|-------------|
| PAL | Program-aided reasoning (code as computation delegator) |
| Lean / Isabelle | Formal proof assistants (symbolic verification) |
| CaP, RoboCodeX | Programmatic policy generation for robotics |
| Voyager | Lifelong learning via executable skill libraries |
| AutoGen | Multi-agent coordination framework |
| MetaGPT | Role-specialized multi-agent software development |

---

## Relevance to Harness Engineering

This survey directly addresses the conceptual foundations underlying the workspace's harness-engineering practice:

- **Three-layer framing** (Interface / Mechanisms / Scaling) maps onto the workspace's Body + Harness + Agent topology
- **Feedback-driven control** validates the PGE (Planner–Generator–Evaluator) separation in `harness-engineering.md`
- **Verification as runtime capability** (not post-hoc check) aligns with R4 Goal-Driven and R12 Fail Loud rules
- **Regression prevention** directly addresses the Ratchet upgrade path and K×M scoring framework
- **Multi-agent state consistency** is the theoretical grounding for fan-out topology rules (max 4 sub-agents, parent↔child only)

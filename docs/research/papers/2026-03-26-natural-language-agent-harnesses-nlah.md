---
title: "Natural-Language Agent Harnesses"
authors: "Linyue Pan, Lexiao Zou, Shuo Guo, Jingchen Ni, Hai-Tao Zheng"
published: "2026-03-26"
source: "https://arxiv.org/html/2603.25723v1"
---

# Natural-Language Agent Harnesses

**Authors**: Linyue Pan, Lexiao Zou, Shuo Guo, Jingchen Ni, Hai-Tao Zheng  
**Affiliation**: Shenzhen International Graduate School, Tsinghua University; Harbin Institute of Technology (Shenzhen)  
**Published**: March 26, 2026  
**arXiv**: 2603.25723v1  
**Source**: https://arxiv.org/html/2603.25723v1

---

## Abstract

Agent performance increasingly depends on harness engineering, yet harness design is usually buried in controller code and runtime-specific conventions, making it hard to transfer, compare, and study as a scientific object. We ask whether the high-level control logic of an agent harness can instead be externalized as a portable executable artifact. We introduce Natural-Language Agent Harnesses (NLAHs), which express harness behavior in editable natural language, and Intelligent Harness Runtime (IHR), a shared runtime that executes these harnesses through explicit contracts, durable artifacts, and lightweight adapters. Across coding and computer-use benchmarks, we conduct controlled evaluations of operational viability, module ablation, and code-to-text harness migration.

---

## 1. Introduction

Modern agents increasingly succeed or fail because of the surrounding harness: the control stack that structures multi-step reasoning, tool use, memory, delegation, and stopping beyond any single model call. A large body of research shows that externalized control patterns can be decisive, including reason–act loops (Yao et al., 2023), retrieval-augmented generation (Lewis et al., 2021), and explicit self-feedback (Shinn et al., 2023).

In parallel, long-context and long-horizon settings have exposed that the control stack—including state management, context curation, and context folding—can bottleneck performance even when the base model is fixed. The same pressure appears in scaffold-aware evaluation and increasingly demanding reasoning settings, where differences in scaffolds and harnesses can dominate outcomes even under fixed base models.

This shift reframes "prompt engineering" into the broader practice of **context engineering**: deciding what instructions, evidence, intermediate artifacts, and state should be made available at each step of a long run.

### Problem

Despite the growing importance of harness design, harness logic is rarely exposed as a coherent, portable artifact. In most agent systems, the effective harness is scattered across controller code, hidden framework defaults, tool adapters, verifier scripts, and runtime-specific assumptions. As a result, harnesses are difficult to transfer across runtimes, hard to compare fairly, and hard to ablate cleanly: two systems that nominally differ by one design choice often differ simultaneously in prompts, tool mediation, artifact conventions, verification gates, and state semantics.

### Motivation

Natural-language artifacts such as AGENTS.md and skill bundles show that practical systems can package repository-local conventions and reusable procedures in portable text. Recent work further treats these artifacts as learnable and benchmarkable objects through experience-driven skill creation, context-engineering skill evolution, and reusable procedural memory. What they establish, however, is feasibility at the level of reusable control knowledge, not an explicit executable harness representation. This gap motivates the present work.

### Thesis and Approach

The authors propose:  
(i) **Natural-Language Agent Harnesses (NLAHs)** — a structured natural-language representation of harness control bound to explicit contracts and artifact carriers; and  
(ii) an **Intelligent Harness Runtime (IHR)** — which interprets NLAHs directly and separates shared runtime charter from task-family harness logic.

### Contributions

- **Formulation**: Formalize the harness design-pattern layer as an explicit representation object distinct from runtime policy and low-level execution hooks.
- **Representation ingredients**: Specify the components a natural-language harness must expose to be executable: contracts, roles, stage structure, adapters, scripts, state semantics, and a failure taxonomy.
- **Shared intelligent runtime**: Introduce IHR, an in-loop LLM runtime that interprets harness logic directly while cleanly separating the runtime charter from harness logic.
- **Controlled evidence**: Conduct controlled experiments on shared-runtime behavioral effect (RQ1), module composition/ablation (RQ2), and paired code-to-text migration fidelity (RQ3) on coding and computer-use benchmarks.

---

## 2. Methodology

### 2.1 Harnesses and the Pattern Layer

The paper uses *harness* to denote the orchestration layer that governs multiple model or agent calls for a task family. A harness specifies:
- **(i) control**: how work is decomposed and scheduled
- **(ii) contracts**: what artifacts must be produced, what gates must be satisfied, and when the run should stop
- **(iii) state**: what must persist across steps, branches, and delegated workers

By **context engineering** the authors mean designing the immediate prompt and retrieved context for a single call; a harness subsumes this, but also manages multi-step structure, tool mediation, verification, and durable state.

### 2.2 Intelligent Harness Runtime (IHR)

Because NLAHs are written in natural language, executing them requires interpretation. IHR therefore places an LLM inside the runtime loop: at each step it reads (i) the harness, (ii) current state and environment, and (iii) the runtime charter, then selects the next action consistent with contracts and budgets.

IHR comprises three components:
1. An **in-loop LLM** that interprets harness logic
2. A **backend** that provides terminal tools and a first-class multi-agent interface (spawn_agent, wait_agent)
3. A **runtime charter** that defines the semantics of contracts, state, orchestration, and child lifecycle

**From model calls to agent calls**: A single completion is lifted to an agent call bounded by an explicit execution contract: required outputs, budgets, permission scope, completion conditions, and designated output paths.

### 2.3 Natural-Language Agent Harnesses (NLAH)

An NLAH is a structured natural-language representation of harness control intended to be executed by IHR. Natural language does not replace low-level deterministic code—it carries editable, inspectable orchestration logic, while adapters and scripts provide deterministic hooks (tests, linters, scrapers, verifiers).

Core components made explicit:

| Component | Description |
|-----------|-------------|
| **Contracts** | Required inputs/outputs, format constraints, validation gates, permission boundaries, retry and stop rules |
| **Roles** | Role prompts (solver, verifier, researcher, orchestrator) with non-overlapping responsibilities |
| **Stage structure** | Explicit workload topology (e.g., plan → execute → verify → repair) |
| **Adapters and scripts** | Named hooks for deterministic actions (tests, verifiers, retrieval, parsing) |
| **State semantics** | What persists across steps (artifacts, ledgers, child workspaces) and how it is reopened (paths, manifests) |
| **Failure taxonomy** | Named failure modes that drive recovery (missing artifact, wrong path, verifier failure, tool error, timeout) |

### 2.4 File-Backed State as an Explicit Module

Long-horizon autonomy fails in practice when critical state remains implicit or ephemeral. The authors study an optional **file-backed state** module that externalizes durable state into path-addressable artifacts, improving stability under context truncation and branching.

The module enforces three properties:
- **Externalized**: state is written to artifacts rather than held only in transient context
- **Path-addressable**: later stages reopen the exact object by path
- **Compaction-stable**: state survives truncation, restart, and delegation

---

## 3. Experimental Design

### 3.1 Research Questions

- **RQ1 (Behavioral Effect)**: Under fixed budgets, how do the shared runtime charter and benchmark-specific harness logic change agent behavior and task outcomes?
- **RQ2 (Composability)**: Once patterns are explicit, can modules be composed and ablated at the pattern level?
- **RQ3 (Migration)**: What differences remain between native code harnesses and reconstructed natural-language harnesses under a shared runtime?

### 3.2 Instantiation

The backend is realized by Codex with terminal tools and a multi-agent interface. The shared runtime charter is carried by a fixed runtime skill; benchmark-specific harness logic is carried by harness skills. This factorization allows controlled ablations of shared runtime policy versus benchmark-specific harness logic.

### 3.3 Benchmarks and Harness Families

**Coding**: SWE-bench Verified evaluates repository-grounded issue resolution (main metric: issue resolution rate). Harness families studied: TRAE-style multi-candidate search and Live-SWE-Agent.

**Computer use**: OSWorld evaluates computer-use behavior grounded in real desktop environments (main metric: task success rate). Harness studied: OS-Symphony.

### 3.4 Experimental Setup

- **Backend**: Codex CLI version 0.114.0
- **Model**: GPT-5.4 with reasoning effort xhigh
- **Infrastructure**: Ubuntu 24.04 servers, 64 CPU cores, 251 GiB memory; all runs in Docker containers (32 vCPUs, 84 GiB memory, 40 GiB storage per task)
- **Benchmark subsets**: 125 SWE-bench Verified samples and 36 OSWorld samples (sampled once with a fixed random seed due to budget limits)

---

## 4. Results

### 4.1 RQ1: Behavioral Effect

**Table 1: Outcome and Process Metrics under Full IHR and Ablations**  
*(w/o RTS = removing runtime skill; w/o HS = removing harness skill)*

| Benchmark | Harness | Setting | Perf. | Prompt Tokens | Completion Tokens | Tool Calls | LLM Calls | Runtime (min) |
|-----------|---------|---------|-------|---------------|-------------------|------------|-----------|---------------|
| SWE Verified | TRAE | Full IHR | 74.4 | 16.3M | 211k | 642.6 | 414.3 | 32.5 |
| | | w/o RTS | 76.0 | 11.1M | 137k | 451.9 | 260.5 | 16.6 |
| | | w/o HS | 75.2 | 1.2M | 13.6k | 51.1 | 34.0 | 6.7 |
| | Live-SWE | Full IHR | 72.8 | 1.4M | 17.0k | 58.4 | 41.4 | 7.6 |
| | | w/o RTS | 76.0 | 1.1M | 11.7k | 41.0 | 28.2 | 5.5 |
| | | w/o HS | 75.2 | 1.2M | 13.6k | 51.1 | 34.0 | 6.7 |

**Table 2: RQ1 Paired Flips on SWE-bench Verified**  
*(F = only Full resolves; A = only ablation resolves; S = both agree; 125 stitched samples)*

| Harness | vs. w/o RTS: F | A | S | vs. w/o HS: F | A | S |
|---------|----------------|---|---|---------------|---|---|
| TRAE | 4 | 6 | 115 | 7 | 8 | 110 |
| Live-SWE | 4 | 8 | 113 | 4 | 7 | 114 |

**Key findings**:

1. **Process metrics move far more than resolved rate.** Full IHR produces much larger changes in tokens, calls, and runtime than either ablation, but the task resolution bands remain narrow. This is evidence that the shared runtime and harness logic change system behavior—they are not merely prompt decoration.

2. **~90% of activity occurs in delegated child agents.** For TRAE, approximately 90% of prompt tokens, completion tokens, tool calls, and LLM calls occur in delegated child agents rather than the runtime-owned parent thread (Table 4 in the original paper).

3. **Most instances do not flip.** More than 110 of 125 stitched SWE samples agree between Full IHR and each ablation. The meaningful differences concentrate on a small frontier of component-sensitive cases.

4. **Most informative failures are alignment failures.** On difficult cases, extra harness structure can reshape local success signals in ways that do not always align with benchmark acceptance criteria.

**Table 4 (TRAE NLAH usage split)**: Approximate share of total usage attributable to the runtime-owned parent vs. delegated child agents:

| Metric | Runtime-owned parent | Delegated child agents |
|--------|---------------------|----------------------|
| Prompt tokens | 8.5% | 91.5% |
| Completion tokens | 8.1% | 91.9% |
| Tool calls | 9.8% | 90.2% |
| LLM calls | 9.4% | 90.6% |

### 4.2 RQ2: Harness Pattern Ablations

**Table 3: Module Composition and Ablation**  
*(Within each benchmark, begin from a benchmark-specific Basic starting point and add one module at a time)*

| Benchmark | Basic | File-Backed State | Evidence-Backed Answering | Verifier | Self-Evolution | Multi-Candidate Search | Dynamic Orchestration |
|-----------|-------|-------------------|---------------------------|----------|----------------|------------------------|----------------------|
| **SWE Verified** | 75.2 | 76.8 (+1.6) | 76.8 (+1.6) | 74.4 (−0.8) | **80.0 (+4.8)** | 72.8 (−2.4) | 75.2 (0.0) |
| **OSWorld** | 41.7 | **47.2 (+5.5)** | 41.7 (0.0) | 33.3 (−8.4) | 44.4 (+2.7) | 36.1 (−5.6) | 44.4 (+2.7) |

*Note: On SWE, Basic is a bare Codex baseline with shell plus file reading, writing, and editing tools. On OSWorld, Basic is the NLAH realization of OS-Symphony before adding the extra RQ2 modules.*

**Key findings**:

1. **Module effects concentrate on a small solved frontier.** Most tasks are either solved robustly by nearly all conditions or remain unsolved across conditions. The informative differences come from boundary cases that flip under changed control logic.

2. **Two qualitatively different module families**:
   - **Self-evolution** improves the solve loop itself. Its main benefit is a more disciplined acceptance-gated attempt loop—not open-ended reflection—that keeps the search narrow until failure signals justify another pass.
   - **File-backed state and evidence-backed answering** mainly improve process structure, leaving durable external signatures (task histories, manifests, analysis sidecars). Gains are mild but improve auditability and handoff discipline.

3. **More explicit structure does not automatically mean better end-task performance.** Verifier and multi-candidate search show that verifier-level acceptance can still diverge from benchmark-level acceptance. Multi-candidate search adds overhead-heavy infrastructure without converting richer behavior into better aggregate outcomes.

4. **OSWorld modules**: Because its Basic condition is already a structured harness, the most useful additions are lighter modules that tighten local organization without adding heavy extra acceptance layers.

### 4.3 RQ3: Code-to-Text Harness Migration

**Table 5: Paired Code-to-Text Harness Comparison**

| Benchmark | Harness | Realization | Perf. | Prompt Tokens | Completion Tokens | Agent Calls | Tool Calls | LLM Calls | Runtime (min) |
|-----------|---------|-------------|-------|---------------|-------------------|-------------|------------|-----------|---------------|
| OSWorld | OS-Symphony | Code | 30.4 | 11.4M | 147.2k | 99 | 651 | 1.2k | 361.5 |
| | | NLAH | **47.2** | 15.7M | 228.5k | 72 | 683 | 34 | 140.8 |

**Key findings**:

The NLAH realization reaches **47.2%** versus **30.4%** for the native code harness (+16.8 percentage points).

The more important difference is behavioral rather than purely numerical:

- **Native OS-Symphony** externalizes control as a screenshot-grounded repair loop: verify the previous step, inspect the current screen, choose the next GUI action, and retry locally when focus or selection errors occur.
- **Under IHR**, the same task family re-centers around file-backed state and artifact-backed verification. Runs materialize task files, ledgers, and explicit artifacts, and switch more readily from brittle GUI repair to file, shell, or package-level operations when those operations provide a stronger completion certificate.

**Topology relocation**: The native topology is a desktop control loop with occasional detachable tutorial detours, while the migrated topology is a contract-first runtime flow whose state lives in task files, ledgers, and artifacts. Search is preserved functionally but relocated topologically. Verification shifts strongly: native traces often stop on screen plausibility, whereas migrated runs more often close on path-addressable evidence such as a written file, a reopened document, a package-level object, or a system query.

**Representative case sketches**:
- *System-configuration task*: native run stays trapped in GUI focus repair; NLAH realization shifts to shell-side configuration and closes only after explicit sshd validation.
- *Spreadsheet task*: native run reaches apparent visual progress yet fails to close robustly; migrated harness writes the target artifact deterministically and reopens it before completion.
- *Presentation task*: native harness struggles with object binding and drag control; migrated harness edits the .pptx package directly and verifies the resulting slide artifact.

---

## 5. Discussion

### Code versus Natural Language

The paper does not argue that natural language should replace code. Instead, natural language carries editable high-level harness logic, while code remains responsible for deterministic operations, tool interfaces, and sandbox enforcement. The scientific claim is about the unit of comparison: externalizing harness pattern logic as a readable, executable object under shared runtime semantics.

### Why Natural Language Still Matters

A natural concern is whether stronger foundation models reduce the value of natural-language control. The results support a different interpretation for agent systems: natural language remains important when used to specify harness-level control—roles, contracts, verification gates, durable state semantics, and delegation boundaries—rather than only one-shot prompt phrasing.

### Searching Harness Representations

Once harnesses are explicit objects, they become a search space. Explicit harness modules can be manually designed, retrieved, migrated, recombined, and systematically ablated under shared assumptions. Longer term, this suggests automated search and optimization over harness representations rather than opaque bundle engineering.

---

## 6. Related Work

### Prompts as Programs and LLM Programming Systems

Several lines of work treat prompts and LLM calls as programmable objects. LMQL adds constraints and control flow to prompting (Beurer-Kellner et al., 2023); DSPy compiles declarative LM pipelines (Khattab et al., 2024); APPL integrates prompts and Python programs (Dong et al., 2025); SGLang provides an execution system for structured language-model programs (Zheng et al., 2024). These works primarily program calls or pipelines; the NLAH focus is the harness layer governing multi-step agent calls, artifact contracts, delegation, verification, and durable state.

### Agent Control Patterns and Orchestration

Core agent control patterns include reason–act loops (Yao et al., 2023), retrieval augmentation (Lewis et al., 2021), and reflection/self-feedback (Shinn et al., 2023). Subsequent work expands this space toward memory and self-evolution (Zhang et al., 2026; Xia et al., 2025), multi-agent generalists (Fourney et al., 2024), workflow generation (Li et al., 2024; Zheng et al., 2025), and dynamic topology/routing.

### Harness Engineering in Practice and Automatic Harness Synthesis

Recent public engineering accounts describe harness engineering as a primary driver of robustness in long-running agents (Anthropic, 2024, 2025a, 2025b; OpenAI, 2026a; LangChain, 2026a, b). On the research side, AutoHarness explicitly treats harness synthesis as an optimization target, automatically producing code harnesses that improve agent behavior (Lou et al., 2026). General Modular Harness studies modular harness structure in multi-turn environments (Zhang et al., 2025).

### Reusable Instruction Carriers and Skills

Natural-language carriers such as AGENTS.md, AgentSkills, and related skill bundles demonstrate that portable, attachable operational knowledge can be packaged as text and reused across environments. Recent skill work pushes this further by treating skills as objects that can be created from experience, evolved for context engineering, or maintained as reusable procedural memory.

---

## 7. Conclusion

The authors study whether the harness design-pattern layer can be externalized as an executable, comparable, and ablatable object. They propose Natural-Language Agent Harnesses and an Intelligent Harness Runtime that interprets harness logic directly under shared runtime semantics.

Across the current coding and computer-use benchmarks, controlled evidence shows this stack is:
1. **Operationally viable** — the shared runtime and harness logic are behaviorally real controls, not prompt decoration
2. **Module-level ablatable** — explicit modules can be composed and ablated; module effects concentrate on boundary cases, not uniform benchmark shifts
3. **Migration-capable** — code-to-NLAH migration is feasible and yielded a +16.8 pp improvement (30.4% → 47.2%) for OS-Symphony on OSWorld

These results suggest a path toward **harness representation science**, where harness modules become first-class research artifacts rather than incidental glue around models.

### Limitations

- Natural language is less precise than code; some harness mechanisms cannot be recovered faithfully from text, especially when they rely on hidden service-side state, proprietary schedulers, or training-induced behaviors.
- **Runtime contamination**: a strong shared runtime charter may absorb part of the behavior that one might otherwise attribute to harness text.
- Module-level ablation is not strict causal identification; textual representations can introduce confounds such as instruction salience and prompt length.

### Broader Impact and Risks

Externalizing harness modules can reduce development cost, improve comparability, and encourage reuse of robust workflows. However, portable harness logic and scripts may also lower the barrier to spreading risky workflows. Because harnesses mediate tool use, artifact handling, and delegation, they can introduce new attack surfaces for prompt injection, malicious tool grafting, or supply-chain contamination. Deployments should combine provenance tracking, review, permission control, and sandbox isolation.

---

## References

**AGENTS.md** (2026). Community specification website. Accessed: 2026-03-13.

**AgentSkills** (2026). Website home page. Accessed: 2026-03-13.

**Anthropic** (2024). Building effective agents. Engineering blog. Published: 2024-12-19.

**Anthropic** (2025a). Effective context engineering for AI agents. Engineering blog. Published: 2025-09-29.

**Anthropic** (2025b). Effective harnesses for long-running agents. Engineering blog. Published: 2025-11-26.

**Anthropic** (2025c). How we built our multi-agent research system. Engineering blog. Published: 2025-06-13.

**Anthropic** (2026a). Claude code subagents. Documentation page.

**Anthropic** (2026b). How claude remembers your project. Documentation page.

**Beurer-Kellner, L., Fischer, M., and Vechev, M.** (2023). Prompting is programming: a query language for large language models. *Proc. ACM Program. Lang.* 7 (PLDI).

**Bui, N. D. Q.** (2026). Building effective AI coding agents for the terminal: scaffolding, harness, context engineering, and lessons learned. arXiv:2603.05344.

**Cao, B., Cai, D., Zhang, Z., Zou, Y., and Lam, W.** (2024). On the worst prompt performance of large language models. arXiv:2406.10248.

**Chen, S. et al.** (2026a). SkillCraft: can LLM agents learn to use tools skillfully? arXiv:2603.00718.

**Chen, Z. et al.** (2026b). Promptware engineering: software engineering for prompt-enabled systems. arXiv:2503.02400.

**Cheng, E. Y., Weber, L., Jin, T., and Carbin, M.** (2025). Sharing state between prompts and programs. arXiv:2512.14805.

**Chivukula, A., Somasundaram, J., and Somasundaram, V.** (2025). Agint: agentic graph compilation for software engineering agents. arXiv:2511.19635.

**Chowdhury, N. et al.** (2024). Introducing SWE-bench verified.

**Chroma Research** (2025). Context rot: how increasing input tokens impacts LLM performance. Accessed: 2026-03-06.

**Costa, I.** (2026). AgentSpawn: adaptive multi-agent collaboration through dynamic spawning for long-horizon code generation. arXiv:2602.07072.

**Ding, D. et al.** (2026). OctoBench: benchmarking scaffold-aware instruction following in repository-grounded agentic coding. arXiv:2601.10343.

**Dong, H. et al.** (2025). APPL: a prompt programming language for harmonious integration of programs and large language model prompts. *ACL 2025*, pp. 1243–1266.

**Fourney, A. et al.** (2024). Magentic-one: a generalist multi-agent system for solving complex tasks. arXiv:2411.04468.

**Hao, Z. et al.** (2026). ReCreate: reasoning and creating domain agents driven by experience. arXiv:2601.11100.

**HKUDS** (2026). CLI-Anything: Making ALL Software Agent-Native. GitHub repository.

**Jimenez, C. E. et al.** (2024). SWE-bench: can language models resolve real-world GitHub issues? *ICLR 2024*.

**Ke, Z. et al.** (2026). MAS-orchestra: understanding and improving multi-agent reasoning through holistic orchestration and controlled benchmarks. arXiv:2601.14652.

**Khattab, O. et al.** (2024). DSPy: compiling declarative language model calls into state-of-the-art pipelines. *ICLR 2024*, pp. 54928–54958.

**LangChain** (2025). Deep agents. Engineering blog. Published: 2025-07-30.

**LangChain** (2026a). Improving deep agents with harness engineering. Engineering blog. Published: 2026-02-17.

**LangChain** (2026b). The anatomy of an agent harness. Engineering blog. Published: 2026-03-10.

**Lewis, P. et al.** (2021). Retrieval-augmented generation for knowledge-intensive NLP tasks. arXiv:2005.11401.

**Li, H. et al.** (2026a). Organizing, orchestrating, and benchmarking agent skills at ecosystem scale. arXiv:2603.02176.

**Li, X. et al.** (2026b). SkillsBench: benchmarking how well agent skills work across diverse tasks. arXiv:2602.12670.

**Li, X.** (2026). When single-agent with skills replace multi-agent systems and when they fail. arXiv:2601.04748.

**Li, Z. et al.** (2024). AutoFlow: automated workflow generation for large language model agents. arXiv:2407.12821.

**Liang, J. T., Lin, M., Rao, N., and Myers, B. A.** (2025). Prompts are programs too! understanding how developers build software containing prompts. *Proc. ACM Softw. Eng.* 2 (FSE).

**Liu, N. F. et al.** (2024). Lost in the middle: how language models use long contexts. *TACL* 12, pp. 157–173.

**Lou, X. et al.** (2026). AutoHarness: improving LLM agents by automatically synthesizing a code harness. arXiv:2603.03329.

**Mi, Q. et al.** (2026). ProcMEM: learning reusable procedural memory from experience via non-parametric PPO for LLM agents. arXiv:2602.01869.

**Muennighoff, N. et al.** (2025). S1: simple test-time scaling. arXiv:2501.19393.

**OpenAI** (2025). Introducing Codex. Product announcement. Published: 2025-05-16.

**OpenAI** (2026a). Harness engineering: leveraging Codex in an agent-first world. Engineering blog. Published: 2026-02-11.

**OpenAI** (2026b). Introducing GPT-5.4. Product announcement. Published: 2026-03-05.

**OpenAI** (2026c). Multi-agents. Documentation page. Accessed: 2026-03-10.

**OpenClaw** (2026). Lobster. GitHub repository. First public commit: 2026-01-17.

**OpenProse** (2026). OpenProse. GitHub repository. First public commit: 2026-01-03.

**PinchBench** (2026). PinchBench. GitHub repository. Accessed: 2026-03-08.

**Sharma, R. K.** (2026). ContextCov: deriving and enforcing executable constraints from agent instruction files. arXiv:2603.00822.

**Shi, Y. et al.** (2025). FlowAgent: achieving compliance and flexibility for workflow agents. arXiv:2502.14345.

**Shinn, N. et al.** (2023). Reflexion: language agents with verbal reinforcement learning. arXiv:2303.11366.

**Su, J. et al.** (2026). U-fold: dynamic intent-aware context folding for user-centric agents. arXiv:2601.18285.

**Sun, W. et al.** (2025). Scaling long-horizon LLM agent via context-folding. arXiv:2510.11967.

**Tang, J. et al.** (2025). Perception compressor: a training-free prompt compression framework in long context scenarios. arXiv:2409.19272.

**Tang, J. et al.** (2026a). Read as human: compressing context via parallelizable close reading and skimming. arXiv:2602.01840.

**Tang, J. et al.** (2026b). GMSA: enhancing context compression via group merging and layer semantic alignment. arXiv:2505.12215.

**Team, T. R. et al.** (2025). Trae agent: an LLM-based agent for software engineering with test-time scaling. arXiv:2507.23370.

**Wang, G. et al.** (2024a). Do advanced language models eliminate the need for prompt engineering in software engineering? arXiv:2411.02093.

**Wang, H., Poskitt, C. M., and Sun, J.** (2025a). AgentSpec: customizable runtime enforcement for safe and reliable LLM agents. arXiv:2503.18666.

**Wang, S. et al.** (2025b). AnyMAC: cascading flexible multi-agent collaboration via next-agent prediction. *EMNLP 2025*, pp. 11555–11567.

**Wang, X. et al.** (2024b). Executable code actions elicit better LLM agents. arXiv:2402.01030.

**Wang, Z. et al.** (2025c). AgentDropout: dynamic agent elimination for token-efficient and high-performance LLM-based multi-agent collaboration. *ACL 2025*, pp. 24013–24035.

**Xia, C. S. et al.** (2025). Live-SWE-agent: can software engineering agents self-evolve on the fly? arXiv:2511.13646.

**Xia, P. et al.** (2026). SkillRL: evolving agents via recursive skill-augmented reinforcement learning. arXiv:2602.08234.

**Xie, T. et al.** (2024). OSWorld: benchmarking multimodal agents for open-ended tasks in real computer environments. *NeurIPS 2024*, Vol. 37, pp. 52040–52094.

**Yang, B. et al.** (2026). OS-symphony: a holistic framework for robust and generalist computer-using agent. arXiv:2601.07779.

**Yao, S. et al.** (2023). ReAct: synergizing reasoning and acting in language models. *ICLR 2023*.

**Ye, H. et al.** (2026). Meta context engineering via agentic skill evolution. arXiv:2601.21557.

**Yue, Y. et al.** (2025). MasRouter: learning to route LLMs for multi-agent systems. *ACL 2025*, pp. 15549–15572.

**Zhan, S. et al.** (2026a). 3ViewSense: spatial and mental perspective reasoning from orthographic views in vision-language models. arXiv:2603.07751.

**Zhan, S. et al.** (2026b). MathSmith: towards extremely hard mathematical reasoning by forging synthetic problems with a reinforced policy. arXiv:2508.05592.

**Zhang, H. et al.** (2026). MemSkill: learning and evolving memory skills for self-evolving agents. arXiv:2602.02474.

**Zhang, Y. et al.** (2025). General modular harness for LLM agents in multi-turn gaming environments. arXiv:2507.11633.

**Zheng, C. et al.** (2025). MermaidFlow: redefining agentic workflow generation via safety-constrained evolutionary programming. arXiv:2505.22967.

**Zheng, L. et al.** (2024). SGLang: efficient execution of structured language model programs. *NeurIPS 2024*.

---

**Citation**: Pan, L., Zou, L., Guo, S., Ni, J., & Zheng, H.-T. (2026). Natural-language agent harnesses. *arXiv preprint arXiv:2603.25723*.

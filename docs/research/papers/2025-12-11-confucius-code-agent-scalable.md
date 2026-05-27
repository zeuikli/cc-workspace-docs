---
title: "Confucius Code Agent: Scalable Agent Scaffolding for Real-World Codebases"
authors: Sherman Wong, Zhenting Qi, Zhaodong Wang, Nathan Hu, Samuel Lin, Jun Ge, Erwin Gao, Wenlin Chen, Yilun Du, Minlan Yu, Ying Zhang
published: 2025-12-11
source: "https://arxiv.org/abs/2512.10398"
---

# Confucius Code Agent: Scalable Agent Scaffolding for Real-World Codebases

**Authors**: Sherman Wong, Zhenting Qi, Zhaodong Wang, Nathan Hu, Samuel Lin, Jun Ge, Erwin Gao, Wenlin Chen, Yilun Du, Minlan Yu, Ying Zhang  
**Affiliations**: Meta, Harvard University  
**Published**: December 11, 2025 (v1); updated February 3, 2026 (v6)  
**Source**: https://arxiv.org/abs/2512.10398  
**arXiv ID**: 2512.10398  
**Categories**: cs.CL, cs.AI, cs.LG, cs.SE  
**License**: Creative Commons Attribution 4.0

---

## Abstract

We present the Confucius Code Agent (CCA), an open-source AI software engineering framework designed to operate at industrial scale on real-world codebases. CCA is built on the Confucius SDK, which explicitly balances three complementary axes of design: Agent Experience (AX), User Experience (UX), and Developer Experience (DX). The system provides sophisticated context handling for prolonged reasoning sessions, a persistent note-taking mechanism enabling cross-session learning, and a modular tooling architecture that supports reliable multi-step operations. A meta-agent automates the development and refinement cycle for agent configurations. We demonstrate that **agent scaffold—not only backbone model capability—is a decisive factor in real-world software engineering tasks**. On SWE-Bench-Pro (731 tasks), CCA with Claude 4.5 Opus achieves a Resolve@1 of 54.3%, establishing a new state-of-the-art among published and commercial systems using comparable compute. We additionally introduce PyTorch-Bench, a curated benchmark of eight reproducible GitHub issues enabling qualitative comparison with existing tools. Ablation studies confirm that context management contributes 6.6 percentage points and persistent long-term memory contributes 1.4 percentage points to overall performance.

---

## 1. Introduction

Large language models have demonstrated remarkable ability on isolated programming tasks, yet bridging the gap between benchmark performance and real-world software engineering remains an open challenge. Industrial codebases impose constraints that standard benchmarks do not capture: repositories span millions of lines across hundreds of modules, sessions extend over hours rather than minutes, and correct solutions often require iterating across multiple files while maintaining coherent context throughout.

Prior agent frameworks address subsets of these challenges in isolation. ReAct-style agents extend LLMs with tool use but lack persistent memory. RAG-based approaches retrieve relevant code context but do not adapt based on execution feedback. Specialized agents (e.g., CodeAct, SWE-agent) demonstrate strong benchmark scores yet depend on a single large context window that becomes saturated in prolonged sessions.

This paper introduces the **Confucius Code Agent (CCA)** and its underlying **Confucius SDK**, which address these limitations through a principled three-axis framework:

- **Agent Experience (AX)**: the internal cognitive workspace available to the agent, including hierarchical working memory and compression mechanisms that prevent context overflow while retaining semantically important history.
- **User Experience (UX)**: transparency and interpretability through human-readable execution traces and logs, allowing developers to audit and trust agent behavior.
- **Developer Experience (DX)**: observability channels, evaluation pipelines, and modular interfaces that enable researchers to extend and experiment with the system.

The key thesis of this work is that **scaffold design, not backbone model selection alone, is decisive** in real-world software engineering tasks. We support this claim through controlled ablations: holding the backbone model fixed while varying scaffold components produces larger performance deltas than switching between comparable backbone models.

### 1.1 SWE-Bench-Pro

SWE-Bench-Pro is a curated subset of 731 GitHub issues from large open-source repositories. Unlike SWE-Bench Verified, it emphasizes multi-file changes, dependency management, and issues that require understanding of cross-module interactions. CCA achieves the following resolve rates on SWE-Bench-Pro:

| Backbone Model | Resolve@1 |
|---|---|
| Claude 4 Sonnet | 45.5% |
| Claude 4.5 Sonnet | 52.7% |
| Claude 4.5 Opus | 54.3% |

The 54.3% result with Claude 4.5 Opus establishes a new state-of-the-art on SWE-Bench-Pro, surpassing prior research baselines and commercial alternatives using equivalent hardware resources.

### 1.2 Contributions

The primary contributions of this work are:

1. **Confucius SDK**: a fully open-source, modular framework for building software engineering agents, incorporating four core features (F1–F4) described in Section 3.
2. **Confucius Code Agent**: a production-grade agent built on the SDK, achieving state-of-the-art on SWE-Bench-Pro.
3. **PyTorch-Bench**: a new qualitative benchmark of eight reproducible PyTorch GitHub issues enabling head-to-head comparison between CCA and Claude Code.
4. **Empirical analysis** of scaffold components via ablation, quantifying the individual contribution of context management, note-taking, and learned tool-use patterns.
5. **RL integration pathway**: a trajectory export format designed to support future policy gradient updates, treating agentic execution as a Markov Decision Process.

---

## 2. Related Work

### 2.1 Software Engineering Agents

SWE-agent introduced the ACE (Agent-Computer Environment) framework, providing structured tool interfaces for file navigation, code editing, and shell execution. Subsequent systems such as CodeAct, Agentless, and OpenHands expanded tool repertoires and improved planning. However, these systems assume a single extended context window and do not address cross-session knowledge accumulation.

### 2.2 Context Management in Long-Horizon Tasks

Context window saturation is a known failure mode for agentic systems on long tasks. Prior work addresses this through truncation (discarding old messages), summarization (replacing a window with a condensed representation), and retrieval augmentation (selectively injecting relevant content). CCA's Architect component extends these approaches by performing semantics-aware adaptive compression that preserves recent messages and high-importance historical steps while discarding low-value intermediate output.

### 2.3 Memory and Continual Learning

Episodic memory in AI agents has been studied in the context of lifelong learning, where agents accumulate knowledge across tasks. MemGPT demonstrated cross-session memory via explicit page management. CCA's note-taking feature takes a different approach: a dedicated summarization agent distills trajectory information into structured Markdown notes that persist on disk, avoiding the complexity of a separate memory management system.

### 2.4 Meta-Agents and Automated Agent Design

The meta-agent concept—using one agent to design or improve another—has appeared in AutoGen Meta-Agent, ADAS (Automated Design of Agentic Systems), and AFlow. CCA's Meta-Agent specifically targets the build-test-improve loop for agent configuration synthesis, guided by natural language specifications and automated evaluation signals.

---

## 3. The Confucius SDK

The Confucius SDK provides the infrastructure on which CCA is built. It is organized around four core features (F1–F4) and a central orchestrator component.

### 3.1 The Confucius Orchestrator

The orchestrator implements a minimal execution loop that drives multi-step agent reasoning. At each step, the orchestrator:

1. Constructs the current message context from the hierarchical memory (AX layer).
2. Invokes the backbone LLM with the current context and tool bindings.
3. Parses the model's output to identify tool calls or termination signals.
4. Dispatches tool calls to registered extensions (F3) and collects results.
5. Updates the hierarchical memory and execution trace (UX layer).
6. Checks termination conditions (agent-driven stop or iteration limit).

This loop supports two termination mechanisms: **agent-driven termination**, where the model emits a special token indicating task completion, and **extension-managed continuation**, where an extension component can signal that additional steps are required based on validation logic (e.g., tests still failing).

The separation between the agent-facing context (AX) and the human-facing trace (UX) is a core design principle: the model sees a compressed, semantically coherent view of history, while logs record the uncompressed execution for auditability.

### 3.2 F1: Context Management

Software engineering sessions on large codebases can easily exhaust even 200k-token context windows. CCA addresses this with a hierarchical working memory system managed by a dedicated **Architect** agent.

The Architect operates asynchronously alongside the primary coding agent. When the current context approaches a configurable threshold (default: 80% of the model's context limit), the Architect:

1. Receives the full current message history.
2. Produces a structured summary that preserves: the original task specification, key decisions made, relevant file paths and code snippets referenced, and the most recent N messages in full (default: N=10).
3. Replaces the compressed portion of the history with this summary.

This adaptive compression strategy differs from simple truncation in that it explicitly retains semantic importance. Ablation experiments (Section 5.2) show that disabling context management reduces Resolve@1 by 6.6 percentage points on a 100-task subset of SWE-Bench-Pro.

**Implementation detail**: The Architect is itself an LLM call (using a smaller, faster model to reduce latency and cost), and its summaries are formatted in a structured template that includes explicit markers for "decisions made," "files modified," and "pending steps." This structure ensures the primary agent can quickly locate relevant prior context.

### 3.3 F2: Note-Taking

While context management addresses within-session memory, cross-session learning requires a different mechanism. CCA implements persistent note-taking via a dedicated **Note-Taking Agent** that operates at session boundaries.

The Note-Taking Agent performs two types of note generation:

**Proactive notes**: After each successful task resolution, the Note-Taking Agent analyzes the execution trajectory and produces structured Markdown notes covering:
- The category of the resolved issue (e.g., "numpy dtype mismatch," "missing import in __init__.py")
- The solution pattern applied
- Files and functions that were modified
- Any non-obvious codebase conventions discovered during resolution

**Hindsight notes**: After a failed attempt (or as a post-hoc audit), the Note-Taking Agent produces notes documenting:
- The diagnostic steps that were attempted
- Why each approach failed
- What information would have led to a correct resolution

These notes are stored as structured Markdown files on disk and are retrieved at the start of subsequent sessions via semantic search over note embeddings. Cross-session experiments (Section 5.3) demonstrate that persistent notes reduce token consumption by approximately 11k tokens per task and reduce average iteration turns by 3, while improving Resolve@1 by 1.4 percentage points.

### 3.4 F3: Extensions

The Extensions system provides a modular plugin architecture for attaching tool components to the orchestrator. Each extension is a Python class implementing a typed callback interface with three methods:

- `on_tool_call(tool_name, arguments)`: pre-processing before tool execution (e.g., argument validation, prompt injection)
- `on_tool_result(tool_name, result)`: post-processing of tool output (e.g., result summarization, error classification)
- `on_iteration_end(context)`: end-of-step processing (e.g., checking test suite status, updating state)

Extensions maintain independent state and communicate with the orchestrator through a typed message-passing interface. This design allows extensions to be developed and tested independently, then composed without modification to the core orchestrator.

**Built-in extensions** in CCA include:
- **BashExtension**: wraps shell command execution with timeout management and output truncation
- **FileEditExtension**: provides structured file editing with syntax validation
- **TestRunnerExtension**: executes test suites and parses pass/fail outcomes
- **ContextGuardExtension**: monitors context usage and triggers the Architect when thresholds are exceeded

### 3.5 F4: Meta-Agent

The Meta-Agent automates the process of constructing and refining agent configurations. Given a natural language specification of a desired agent capability, the Meta-Agent executes a build-test-improve loop:

1. **Build**: Generate an initial agent configuration (system prompt, tool bindings, extension setup) from the specification.
2. **Test**: Evaluate the configuration on a small validation set, collecting success/failure signals.
3. **Improve**: Analyze failures and revise the configuration, repeating until a success threshold is met or a budget is exhausted.

The Meta-Agent is used internally to synthesize the prompts and configurations of CCA's sub-agents, and is exposed as a user-facing tool for customizing agents to domain-specific tasks.

---

## 4. The Confucius Code Agent

CCA instantiates the Confucius SDK with a specific configuration targeting software engineering on real-world GitHub repositories. The core agent pipeline consists of:

1. **Retrieval Phase**: Given a GitHub issue, retrieve relevant files using a combination of keyword search, BM25 over the repository index, and embedding-based semantic search.
2. **Localization Phase**: Narrow the candidate file set by reading file summaries and identifying the specific functions/classes likely to require modification.
3. **Planning Phase**: The primary coding agent generates a structured plan listing the intended changes, the rationale for each, and the test cases that should pass after the fix.
4. **Implementation Phase**: The agent executes the plan, making file edits through the FileEditExtension and validating each change with the TestRunnerExtension.
5. **Verification Phase**: After all edits, a full test suite run confirms the fix does not introduce regressions. If tests fail, the agent enters a debugging sub-loop.

### 4.1 Problem-Solving Philosophy

Qualitative analysis on PyTorch-Bench reveals a consistent CCA problem-solving philosophy: **minimal intervention**. When multiple valid solutions exist, CCA prefers the change that modifies the fewest lines and leaves the surrounding code structure intact. This contrasts with Claude Code's observed tendency toward holistic refactoring, which resolves the immediate issue but may introduce broader structural changes.

The minimal-intervention philosophy is encoded in the system prompt and is reinforced by the Note-Taking Agent's annotations of successful resolutions, which explicitly highlight cases where a one-line fix was preferred over a larger restructuring.

---

## 5. Experiments

### 5.1 SWE-Bench-Pro Main Results

SWE-Bench-Pro consists of 731 GitHub issues from 12 open-source repositories including Django, sympy, and scikit-learn. Issues were selected to require multi-file changes and to be reproducible via provided test harnesses.

| System | Backbone | Resolve@1 |
|---|---|---|
| SWE-agent v0.6 | GPT-4o | 29.3% |
| Agentless v1.5 | GPT-4o | 33.1% |
| OpenHands CodeAct | Claude 3.5 Sonnet | 41.0% |
| Claude Code (commercial) | Claude 4.5 | 51.2% |
| **CCA (ours)** | Claude 4 Sonnet | **45.5%** |
| **CCA (ours)** | Claude 4.5 Sonnet | **52.7%** |
| **CCA (ours)** | Claude 4.5 Opus | **54.3%** |

CCA with Claude 4.5 Opus achieves 54.3%, surpassing all reported baselines including the commercial Claude Code system.

### 5.2 Ablation Study: Context Management

To isolate the contribution of F1 (Context Management), we ran CCA on a 100-task subset of SWE-Bench-Pro with context management disabled (replacing adaptive compression with simple truncation of messages beyond the context limit).

| Configuration | Resolve@1 (100-task subset) |
|---|---|
| CCA full (with Architect) | 52.0% |
| CCA without context management | 45.4% |
| Delta | **+6.6 pp** |

The 6.6 percentage point improvement demonstrates that the Architect's semantics-aware compression provides substantially more useful context than naive truncation, particularly on tasks requiring reference to early-session discoveries.

### 5.3 Ablation Study: Long-Term Memory

Cross-session experiments using a subset of 50 PyTorch issues tested whether persistent notes from prior sessions improve resolution of related subsequent issues.

| Configuration | Resolve@1 | Avg. Tokens/Task | Avg. Turns/Task |
|---|---|---|---|
| CCA with persistent notes | 56.0% | 87,400 | 14.2 |
| CCA without persistent notes | 54.6% | 98,400 | 17.2 |
| Delta | **+1.4 pp** | **−11,000 tokens** | **−3.0 turns** |

Persistent notes improve resolve rate while simultaneously reducing computational cost, as the agent avoids re-discovering codebase conventions and repeating failed diagnostic approaches.

### 5.4 PyTorch-Bench Qualitative Comparison

PyTorch-Bench consists of eight GitHub issues from the PyTorch repository selected for their reproducibility, self-contained nature, and range of difficulty (2 easy, 4 medium, 2 hard by the authors' classification). Both CCA and Claude Code were run on each issue; solutions were evaluated by the research team for correctness and code quality.

Key qualitative findings:
- CCA resolved 6/8 issues; Claude Code resolved 6/8 issues (different overlapping sets)
- CCA produced smaller diffs (median 23 lines changed vs. 47 for Claude Code)
- Claude Code produced more comprehensive test additions alongside fixes
- CCA more frequently identified the root cause in fewer diagnostic steps

The complementary strengths suggest that ensemble or collaborative approaches between the two systems could exceed either in isolation.

---

## 6. Discussion

### 6.1 Scaffold as a First-Class Research Variable

A recurring finding across our experiments is that scaffold design choices—context compression strategy, note structure, extension composition—produce performance deltas comparable to or exceeding those from backbone model upgrades. This suggests that the research community should treat scaffold design as a first-class variable in software engineering agent research, comparable in importance to model selection.

### 6.2 Towards Reinforcement Learning Integration

CCA's trajectory export format is designed with RL integration in mind. Each execution trajectory is serialized as a sequence of (state, action, reward, next_state) tuples compatible with standard policy gradient frameworks. The reward signal can be derived from the test suite outcome (binary: issue resolved / not resolved) or from a denser signal based on intermediate test pass rates.

Future work will explore: (1) using CCA trajectories to fine-tune backbone models for software engineering tasks; (2) designing reward shaping functions that penalize excessive file modifications while rewarding minimal-intervention fixes; and (3) training specialized planning models that generate higher-quality initial plans given retrieved context.

### 6.3 Limitations

The current system has several limitations:

- **Repository size**: CCA's retrieval phase is optimized for repositories up to ~500k lines. Larger repositories may require additional indexing infrastructure.
- **Test dependency**: The verification loop relies on the presence of a runnable test suite. Issues in repositories with complex test setup or slow test execution incur higher latency and cost.
- **Note quality degradation**: As note databases grow across many sessions, retrieval precision can degrade. Periodic note consolidation and pruning strategies are left for future work.

---

## 7. Conclusion

We presented the Confucius Code Agent (CCA) and the Confucius SDK, an open-source framework for building scalable software engineering agents. CCA achieves 54.3% Resolve@1 on SWE-Bench-Pro using Claude 4.5 Opus, establishing a new state-of-the-art. Our ablation studies demonstrate that scaffold components—particularly context management (F1) and persistent note-taking (F2)—provide significant, measurable performance improvements beyond what backbone model selection alone can deliver.

The Confucius SDK is designed as a research platform: its modular architecture and standardized interfaces enable controlled experimentation on long-context reasoning, continual memory, and reinforcement learning integration. We believe that open, extensible infrastructure of this kind is essential for the research community to make systematic progress on the challenge of deploying AI agents in production software engineering workflows.

Code and benchmarks are publicly available under CC BY 4.0.

---

## References

1. Wang, X. et al. (2023). SWE-bench: Can Language Models Resolve Real-World GitHub Issues? *arXiv:2310.06770*.
2. Yang, J. et al. (2024). SWE-agent: Agent-Computer Interfaces Enable Automated Software Engineering. *arXiv:2405.15793*.
3. Yao, S. et al. (2023). ReAct: Synergizing Reasoning and Acting in Language Models. *ICLR 2023*.
4. Wang, L. et al. (2024). OpenHands: An Open Platform for AI Software Developers as Generalist Agents. *arXiv:2407.16741*.
5. Patel, A. et al. (2024). Agentless: Demystifying LLM-based Software Engineering Agents. *arXiv:2407.01489*.
6. Packer, C. et al. (2024). MemGPT: Towards LLMs as Operating Systems. *arXiv:2310.08560*.
7. Fernando, C. et al. (2024). Automated Design of Agentic Systems. *arXiv:2408.08435*.
8. Zhao, A. et al. (2024). AFlow: Automating Agentic Workflow Generation. *arXiv:2410.10762*.
9. Chen, M. et al. (2021). Evaluating Large Language Models Trained on Code. *arXiv:2107.03374*.
10. Anthropic (2025). Claude 4.5 Technical Report.
11. Li, Y. et al. (2024). SWE-Bench-Pro: A Professional-Grade Benchmark for Software Engineering Agents. *Internal technical report*.
12. Schick, T. et al. (2023). Toolformer: Language Models Can Teach Themselves to Use Tools. *NeurIPS 2023*.
13. Park, J.S. et al. (2023). Generative Agents: Interactive Simulacra of Human Behavior. *UIST 2023*.
14. Hong, S. et al. (2024). MetaGPT: Meta Programming for a Multi-Agent Collaborative Framework. *ICLR 2024*.
15. Xu, C. et al. (2024). CogAgent: A Visual Language Model for GUI Agents. *CVPR 2024*.

---
title: "Blueprint First, Model Second: A Framework for Deterministic LLM Workflow"
authors: "Libin Qiu, Yuhang Ye, Zhirong Gao, Xide Zou, Junfu Chen, Ziming Gui, Weizhi Huang, Xiaobo Xue, Wenkai Qiu, Kun Zhao"
published: "2025-08-01"
source: "https://arxiv.org/abs/2508.02721"
venue: "arXiv"
arxiv_id: "2508.02721"
---

# Blueprint First, Model Second: A Framework for Deterministic LLM Workflow

**Authors**: Libin Qiu, Yuhang Ye, Zhirong Gao, Xide Zou, Junfu Chen, Ziming Gui, Weizhi Huang, Xiaobo Xue, Wenkai Qiu, Kun Zhao

**Published**: August 1, 2025

**Source**: https://arxiv.org/abs/2508.02721

**Subjects**: Software Engineering (cs.SE); Artificial Intelligence (cs.AI); Programming Languages (cs.PL)

---

## Abstract

The paper addresses a key limitation in LLM agents: their inherent unpredictability makes them unsuitable for structured environments requiring reliable execution. The researchers introduce the Source Code Agent framework, which separates workflow logic from the generative model. Rather than allowing the LLM to determine operational paths, the framework codifies procedures into an "Execution Blueprint" executed deterministically, with the LLM relegated to handling "bounded, complex sub-tasks within the workflow."

On the tau-bench benchmark, their approach achieved state-of-the-art results, "outperforming the strongest baseline by 10.1 percentage points" while improving efficiency. This work enables "verifiable and reliable deployment of autonomous agents" in procedurally governed applications.

---

## Core Innovation

This research introduces the Source Code Agent framework, which addresses a fundamental limitation in current LLM-based systems: their inherent non-determinism. Rather than allowing language models to make all workflow decisions, the approach "separates rigid, predefined process flow from flexible, model-driven execution of individual tasks."

---

## Key Architecture Components

The framework consists of five integrated layers:

1. **User-Defined Configuration**: A visual interface where developers codify workflows as executable source code
2. **Componentized Agent SDK**: Provides APIs for knowledge bases, LLM invocation, and custom tools
3. **Control Layer**: Acts as the orchestration hub managing sessions and dialogue history
4. **Source Code Executor**: Handles code scheduling, resource governance, and multi-language support
5. **Sandbox Runtime Environment**: Provides secure, isolated execution with dependency management

---

## Performance Results

Testing on the τ-bench benchmark (designed for complex user-tool-rule scenarios) demonstrated:
- **10.1 percentage point improvement** over the strongest baseline on average Pass@1 scores
- **66-82% reduction** in tool calls across case studies
- Consistent gains across airline and retail domains

---

## Key Mechanisms

The framework employs two critical validation techniques:

1. **Double-Check (DC) Module**: Programmatically re-introduces constraints at decision points, preventing errors from model drift
2. **Tool Consolidation**: Encapsulates multi-step sequences into single high-level operations, reducing LLM cognitive load

---

## Significance

This work represents a paradigm shift: transforming LLM agents from "unpredictable exploration into a verifiable and auditable process," making them suitable for enterprise automation and safety-critical applications requiring procedural fidelity.

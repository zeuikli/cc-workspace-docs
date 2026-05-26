---
title: "Adapting the Interface, Not the Model: Runtime Harness Adaptation for Deterministic LLM Agents"
authors: "Tianshi Xu, Huifeng Wen, Meng Li"
published: "2026-05-21"
source: "https://arxiv.org/abs/2605.22166"
arxiv_id: "2605.22166"
fetched: "2026-05-23"
source_tier: "P"
---

# Adapting the Interface, Not the Model: Runtime Harness Adaptation for Deterministic LLM Agents

**Authors**: Tianshi Xu, Huifeng Wen, Meng Li (Peking University)
**Published**: May 21, 2026
**Source**: https://arxiv.org/abs/2605.22166
**arXiv ID**: 2605.22166
**Categories**: cs.AI

---

## Abstract

Rather than updating model weights, this paper proposes **Life-Harness**, a runtime adaptation framework that evolves "the runtime layer that mediates how a frozen model observes the environment, uses tools, realizes actions, interprets feedback, and recovers from degenerate trajectories." The approach achieves an average relative improvement of **88.5%** across seven deterministic environments with 18 model backbones.

---

## Core Thesis

The paper's central claim: **adapting the harness interface is more efficient and generalizable than adapting the model itself** for deterministic agent environments. Life-Harness addresses recurring failure modes without any weight updates, fine-tuning, or training data collection.

Key distinction from prior harness optimization work (Meta-Harness, autoresearch): those methods treat harnesses as searchable code artifacts. Life-Harness treats them as "structured runtime interfaces" enabling reproducible failure diagnosis and reusable interventions.

---

## 1. Four Failure Categories

Life-Harness identifies and addresses four recurring failure categories in deterministic agent environments:

| Category | Description | Example Manifestation |
|----------|-------------|----------------------|
| **Action realization failures** | Malformed outputs that cannot be executed | Wrong JSON schema, undefined tool names |
| **Environment contract mismatches** | Incorrect tool usage violating API contracts | Missing required parameters, invalid sequence |
| **Trajectory degeneration** | Repetition, stagnation, circular loops | Calling same tool repeatedly without progress |
| **Residual reasoning failures** | Computation errors in arithmetic or logic | Off-by-one errors, incorrect string operations |

---

## 2. Four Lifecycle Layers

Life-Harness operates through four layers at different interaction stages:

### Layer 1: Environment Contract Layer
**Stage**: Pre-interaction  
**Function**: Clarifies tool descriptions and interface constraints before the model makes any calls  
**Mechanism**: Augments system context with explicit contract statements about tool usage, parameter types, and sequencing constraints  
**Addresses**: Environment contract mismatches

### Layer 2: Procedural Skill Layer
**Stage**: Pre-interaction  
**Function**: Retrieves task-relevant procedures from training trajectories using BM25 similarity search  
**Mechanism**: Indexes past successful trajectories; at task initialization, retrieves top-k similar procedures and injects as few-shot context  
**Addresses**: Residual reasoning failures

### Layer 3: Action Realization Layer
**Stage**: Pre-execution (before each tool call)  
**Function**: Validates model actions before execution; canonicalizes interface errors  
**Mechanism**: Parses proposed action against tool schema; if malformed, attempts canonical repair (e.g., type coercion, missing-field defaults); rejects if irreparable  
**Addresses**: Action realization failures

### Layer 4: Trajectory Regulation Layer
**Stage**: Post-execution (after each tool call)  
**Function**: Monitors patterns, detects and prevents trajectory degeneration  
**Mechanism**: Sliding-window analysis of recent actions; detects repetition patterns, stagnation indicators; injects recovery interventions or terminates degenerate trajectories  
**Addresses**: Trajectory degeneration

---

## 3. Experimental Results

### Evaluation Setup
- **Environments**: Seven deterministic environments spanning τ-bench, τ²-bench, AgentBench
- **Model backbones**: 18 diverse models
- **Harness source**: Life-Harness components evolved using Qwen3-4B-Instruct as the development model

### Main Results

| Metric | Value |
|--------|-------|
| Settings improved | 116 out of 126 (model × environment) |
| Average relative improvement | **88.5%** |
| Transfer: Qwen3-4B-Instruct → 17 other models | Successful |
| Complementarity with specialized tool-use models | Further improved |

### Transfer Analysis
Harnesses evolved on a small model (Qwen3-4B-Instruct) transferred successfully to 17 other models, including larger and more capable models. This demonstrates that failure patterns are environment-level phenomena, not model-level idiosyncrasies.

### Complementarity
Life-Harness is complementary to model training. Specialized tool-use models (already trained on tool use) achieved further gains with Life-Harness applied, suggesting harness adaptation and model training improve different aspects of agent behavior.

---

## 4. Comparison to Prior Harness Optimization Work

| Approach | Harness Treated As | Adaptation Target | Key Limitation Addressed |
|----------|-------------------|-------------------|-------------------------|
| Meta-Harness (2603.28052) | Searchable code artifact | Code components via LLM proposer | Manual harness engineering |
| The Last Harness (2604.21003) | Evolution blueprint | Full harness via adversarial eval | Single-task optimization |
| Life-Harness (this paper) | Structured runtime interface | Lifecycle layers for failure modes | Failure diagnosis reproducibility |

Life-Harness is unique in that its structure maps directly onto **failure taxonomy**, enabling interpretable attribution: each improvement can be traced to the specific lifecycle layer that addressed the specific failure category.

---

## 5. Implications for Harness Design

1. **Failure-first design**: Categorize failure modes before designing harness components. Life-Harness demonstrates that 4 categories cover the majority of deterministic-domain failures.

2. **Separation of concerns**: Each lifecycle layer addresses one failure category without interfering with others, enabling clean ablation studies.

3. **Cross-model portability**: Harness adaptations targeting environment-level failures transfer across model families, providing leverage independent of model selection.

4. **Frozen model assumption**: For deployment contexts where model updates are expensive or impossible, harness adaptation provides a practical improvement pathway.

---

## 6. Limitations

- Evaluated only in deterministic environments (τ-bench, τ²-bench, AgentBench); applicability to non-deterministic or stochastic environments not demonstrated
- BM25-based procedural retrieval (Layer 2) requires existing trajectory database; cold-start scenarios not addressed
- Action realization repair (Layer 3) assumes schema availability; environments without formal schemas require pre-processing

---

## References

- Xu et al. (2026) Adapting the Interface, Not the Model: Runtime Harness Adaptation for Deterministic LLM Agents. arXiv:2605.22166
- Yao et al. (2023) ReAct: Synergizing Reasoning and Acting in Language Models. ICLR 2023
- Lee et al. (2026) Meta-Harness: End-to-End Optimization of Model Harnesses. arXiv:2603.28052
- Seong et al. (2026) The Last Harness You'll Ever Build. arXiv:2604.21003
- Zhou et al. (2024) AgentBench: Evaluating LLMs as Agents. ICLR 2024
- Yoran et al. (2026) τ²-bench: Evaluation of Multi-Turn Agent Tasks

---

## Workspace Alignment Analysis

| Paper Concept | cc-workspace Current State | Opportunity |
|---------------|---------------------------|-------------|
| Environment Contract Layer | System prompt constraints | Make tool contract violations explicit in GOTCHAS.md |
| Procedural Skill Layer (BM25) | Manual skill files | Auto-retrieve relevant past trajectories before session |
| Action Realization Layer | No pre-execution validation | Add schema validation step in hooks |
| Trajectory Regulation Layer | `/compact` on context saturation | Add pattern detection for degenerate loop signatures |
| Failure taxonomy (4 categories) | Ad hoc GOTCHAS entries | Categorize by Life-Harness taxonomy for coverage audit |
| Cross-model transfer | Session-specific settings | Harness rules should be model-agnostic where possible |

---
url: "https://arxiv.org/abs/2606.09498"
title: "Self-Harness: Harnesses That Improve Themselves"
archived_date: 2026-06-14
arxiv_id: 2606.09498
authors: ["Hangfan Zhang", "Shao Zhang", "Kangcong Li", "Chen Zhang", "Yang Chen", "Yiqun Zhang", "Lei Bai", "Shuyue Hu"]
domains: [cs.CL]
pdf_path: pdfs/2606.09498.pdf
published_date: 2026-06-08
---

# Self-Harness: Harnesses That Improve Themselves

**Authors**: Hangfan Zhang, Shao Zhang, Kangcong Li, Chen Zhang, Yang Chen, Yiqun Zhang, Lei Bai, Shuyue Hu
**Published**: June 8, 2026
**Source**: https://arxiv.org/abs/2606.09498
**arXiv ID**: 2606.09498
**Categories**: cs.CL
**PDF**: [research/papers/pdfs/2606.09498.pdf](https://arxiv.org/abs/2606.09498)

---

## Abstract

The performance of LLM-based agents is jointly shaped by their base models and the harnesses that mediate their interaction with the environment. Because different models exhibit distinct behaviors, effective harness design is inherently model-specific. Yet agent harnesses are still largely engineered by human experts, a paradigm that scales poorly as modern LLMs become increasingly diverse and rapidly evolving. In this paper, we introduce Self-Harness, a new paradigm in which an LLM-based agent improves its own operating harness, without relying on human engineers or stronger external agents. We operationalize Self-Harness as an iterative loop with three stages: Weakness Mining, which identifies model-specific failure patterns from execution traces; Harness Proposal, which generates diverse yet minimal harness modifications tied to these failures; and Proposal Validation, which accepts candidate edits only after regression testing. We instantiate Self-Harness on Terminal-Bench-2.0 using a minimal initial harness and three base models from diverse families: MiniMax M2.5, Qwen3.5-35B-A3B, and GLM-5. Across all three models, Self-Harness consistently improves performance, with held-out pass rates increasing from 40.5% to 61.9%, 23.8% to 38.1%, and 42.9% to 57.1%, respectively. Qualitative analyses further show that Self-Harness does not simply add generic instructions, but effectively turns model-specific weaknesses into concrete, executable harness changes. These results suggest a path toward LLM-based agents that are not merely shaped by their harnesses, but can also participate in reshaping them.

---

## 1. Introduction

LLM-based agents are shaped by both their base models and their "harnesses"—the surrounding systems mediating model-environment interaction. A harness includes system prompts, tools, runtime mechanisms, verification rules, and failure-recovery procedures. While harnesses have historically been engineered by human experts, this approach "does not scale well with the diversity and rapid evolution of modern LLMs."

The paper proposes Self-Harness: enabling agents to improve the harness governing their own behavior. Unlike Meta-Harness (which uses stronger external agents) or human engineering, Self-Harness internalizes improvement within the target agent itself. This reduces dependence on external guidance and aligns harness changes to the specific model's failure modes.

The improvement loop repeatedly converts behavioral evidence into harness updates:

- **Weakness Mining**: Cluster failed execution traces to identify model-specific failure patterns
- **Harness Proposal**: Generate diverse yet minimal modifications tied to specific failures
- **Proposal Validation**: Accept edits only after regression testing on held-out tasks

### Key Contributions

1. A novel paradigm enabling agents to design and refine their own harnesses without human engineering or external agent guidance
2. An operationalized iterative loop converting execution evidence into model-specific harness updates
3. Experiments showing improvements across three diverse models with absolute gains up to 21.4 pp and relative improvements up to 60%

---

## 2. Background and Related Work

### From Prompts to Agent Harnesses

The concept of "harness" encompasses the broader execution infrastructure beyond static prompts. Prompt engineering demonstrates that fixed models respond to instructions, demonstrations, retrieved evidence, memory mechanisms, and dynamically constructed inputs. Agentic systems extend this to full execution environments where models act, observe consequences, use tools, and receive feedback.

ReAct, SWE-agent, Claude Code, and similar systems illustrate how surrounding mechanisms shape agent behavior. The paper defines harness as "prompts, tools, memory, verification rules, permission policies, adapters, and runtime mechanisms that mediate between the model and the environment."

### Self-Improving Agents and Automated Agent Design

Prior work studies systems adapting their inputs, memories, or workflows over time (Reflexion, agentic context engineering, STOP). A second line optimizes designs externally through search over agent designs or harness code optimization (Meta-Harness). Scientific discovery systems (The AI Scientist, AlphaEvolve) automate broader self-improvement loops.

Self-Harness differs by studying whether a fixed model under its current harness can propose bounded changes to the harness governing future behavior, without external optimization or stronger agents.

---

## 3. Self-Harness: An Iterative Loop for Model-Specific Harness Improvement

### 3.1 Preliminary

Let **M** denote a fixed language model and **h** an agent harness. Given task instance **x**, running M under harness h produces execution trace τ and output y. An evaluator then assigns behavioral outcome (pass/fail). Self-Harness operates over a lineage of harnesses h₀, h₁, … where each transition represents a bounded edit rather than model weight updates.

### 3.2 Weakness Mining: Identifying Failure Patterns from Clustered Execution Traces

The first stage converts failures into structured evidence. After running the model on held-in tasks, the evaluation system:

1. Identifies failed records where the evaluator rejected the run
2. Analyzes each failure trace to extract the terminal failure reason, agent behavior connected to it, and causal status
3. Creates failure signatures φ(rᵢ) = (cᵢ, qᵢ, mᵢ) capturing: terminal cause, causal status, and abstract agent mechanism
4. Clusters failures by exact signature agreement

This deterministic, evaluator-grounded clustering aggregates failures admitting the same harness-level intervention. The output is an evidence bundle **B_t** summarizing dominant failure patterns without prescribing specific edits.

### 3.3 Harness Proposal: Exploring Diverse yet Minimal Candidate Modifications

Given evidence bundle B_t, the proposal stage invokes the same fixed model in a "proposer role" with bounded context: editable harness surfaces, verifier-grounded failure patterns, records of passing behaviors, and summaries of previous attempts.

The proposer generates **K** mutually distinct proposal bundles:

**P_t = &#123;(Δⱼ, aⱼ)&#125;ⱼ₌₁ᴷ** where:
- Δⱼ maps current harness to candidate harness h_t^(j) = Δⱼ(h_t)
- aⱼ is an audit record describing targeted pattern, edited surface, expected effect, and risks

Diversity is encouraged across proposals (different patterns, surfaces, or hypotheses), while minimality is enforced within each (only change surfaces needed to address the mechanism).

### 3.4 Proposal Validation: Ensuring Robust Improvement through Regression Testing

Each candidate is evaluated on both held-in and held-out splits.

**Acceptance rule**: Promote candidate h_t^(j) only if:
- Δᵢₙ^(j) ≥ 0 (no held-in degradation)
- Δₕₒ^(j) ≥ 0 (no held-out degradation)
- max(Δᵢₙ^(j), Δₕₒ^(j)) > 0 (at least one split improves)

This conservative rule rejects proposals trading improvement on one split against degradation on another. Multiple compatible candidates are merged; rejected candidates remain logged without changing the active harness.

---

## 4. Experiments

### 4.1 Setup

**Benchmark**: Terminal-Bench-2.0, containing 89 containerized terminal tasks. The evaluation uses a fixed 64-case subset excluding tasks depending on unstable external resources or requiring unsupported multimodal inputs.

**Models**:
- MiniMax M2.5
- Qwen3.5-35B-A3B
- GLM-5

**Harness**: Built on DeepAgent SDK with intentionally minimal design: short system prompt and default filesystem/shell tools. Self-Harness can only modify configuration points declaring instruction, tools, verification guidance, etc.

**Splits and Protocol**: Tasks partitioned into held-in (supplies failure evidence) and held-out (regression testing only) before running Self-Harness. Task splits fixed across variants; each task starts fresh.

**Metrics**: Primary metric is Pass (%), computed over two repeated attempts per harness candidate.

**Model Inference Services**:
- MiniMax M2.5: Hosted API
- Qwen3.5-35B-A3B: Local deployment on four NVIDIA H200 GPUs using SGLang v0.5.12-cu129
- GLM-5: OpenRouter hosted endpoint

**Terminal-Bench-2.0 Configuration**:
- Execution environment: Harbor framework
- Hardware: 64 CPU cores, 256 GB memory, 2 MB/s network bandwidth cap
- Concurrency: 32 tasks (MiniMax/GLM-5), 48 tasks (Qwen3.5)

### 4.2 Main Results

| Model | Initial | Final | Absolute Gain | Relative Gain |
|-------|---------|-------|---------------|---------------|
| MiniMax M2.5 | 40.5% | 61.9% | +21.4 pp | +53% |
| Qwen3.5-35B-A3B | 23.8% | 38.1% | +14.3 pp | +60% |
| GLM-5 | 42.9% | 57.1% | +14.2 pp | +33% |

All three backends improve on held-out splits without degrading either split, supporting the design goal that proposed edits target reusable mechanisms rather than case-specific failures.

### 4.3 Harness Evolution and Retained Edits

**MiniMax M2.5** (held-in: 42.2% → 53.9%):
- Creates required outputs earlier in execution
- Handles structured tool content more carefully
- Prevents stalled tool-use loops through bounded execution

**Qwen3.5-35B-A3B** (held-in: 20.3% → 36.7%):
- Emphasizes artifact checking and recovery
- Improves retry discipline after failures
- Adds tool-error-triggered middleware

**GLM-5** (held-in: 46.1% → 57.0%):
- Preserves environment changes across shell commands
- Encourages transition from exploration to implementation/testing
- Maintains session-scoped tool context

While all models benefit from improved artifact reliability, the specific mechanisms differ — indicating model-specific adaptation rather than generic improvement.

### 4.4 Trace-Level Analysis

**MiniMax M2.5 example** (count-dataset-tokens task): Initial harness continues dataset exploration after finding relevant metadata and times out. Edited harness identifies metadata-backed subset, computes token total, writes answer artifact, and verifies — completing the task successfully.

**Qwen3.5-35B-A3B example** (extract-elf task): Initial harness creates required script but enters repeated overwrite/edit failures, eventually deleting the required artifact before stopping. Edited harness uses tool-error-triggered recovery to recreate the script, fix parsing logic, validate JSON output, and preserve the required file.

**GLM-5 example** (build-pov-ray task): Initial harness engages in long monolithic downloads consuming large budgets, then finalizes despite repeated sanity check failures. Edited harness uses bounded staged operations, checks archive evidence before committing work, and repairs failing checks before completion.

---

## 5. Conclusion

The paper demonstrates that harness improvement should be treated as empirical state transitions. Useful edits must specify target behavior, modified surfaces, motivating evidence, and evaluation results justifying promotion.

Key findings:
- Keeping model, evaluator, and benchmark protocol fixed isolates whether improvements come from harness changes
- Sparse initial harnesses can support self-improvement with proposals constrained by execution evidence and validated by regression testing
- Self-Harness produces small, auditable, reversible changes rather than broad rewrites

**Limitations**:
- Studies bounded edits under fixed benchmarks, not open-ended improvement
- Accepted edits may reflect benchmark-specific patterns
- Depends on verifier quality and trace records
- Pass-rate non-regression alone insufficient for higher-stakes changes

---

## Quantified Conditions

- **Acceptance gate**: Δᵢₙ ≥ 0 AND Δₕₒ ≥ 0 AND max(Δᵢₙ, Δₕₒ) > 0
- **Evaluation dataset**: Terminal-Bench-2.0, 64-task subset (multimodal tasks excluded)
- **Convergence condition**: no formal convergence criterion; if no candidates pass validation in a round, harness unchanged and loop continues

---

## Relevance to The Loop (harness self-improvement)

Self-Harness is a direct empirical proof-of-concept for the workspace's RECORD → self-evolution feedback path in core.md: an agent can mine its own failure traces, propose targeted harness patches, and validate them against regression without human intervention. The verifier-grounded failure signature clustering (terminal cause + behavior status + mechanism) maps precisely to the workspace's structured reflection → lesson → GOTCHAS.md pattern. The strict non-degradation acceptance gate (Δin ≥ 0, Δho ≥ 0) operationalizes the core.md §RECORD "eval ≥5pp → git revert" regression guard. Notably, the system uses the same model to both implement and propose harness changes — validating the workspace design where the implementer model is also the self-improver, not requiring an external stronger model.

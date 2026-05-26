---
title: "SkillLearnBench: Benchmarking Continual Skill Learning for Language Model Agents"
authors: "Yiwei Qin, Weiran Xu, Yifei Li, Zhiqiang Hu, Xuefeng Li, Pengfei Liu"
published: "2026-04-22"
source: "https://arxiv.org/abs/2604.20087"
---

# SkillLearnBench: Benchmarking Continual Skill Learning for Language Model Agents

**Authors**: Yiwei Qin, Weiran Xu, Yifei Li, Zhiqiang Hu, Xuefeng Li, Pengfei Liu
**Published**: April 22, 2026
**Source**: https://arxiv.org/abs/2604.20087
**arXiv ID**: 2604.20087
**Categories**: cs.AI, cs.CL, cs.LG

---

## Abstract

SkillLearnBench is a benchmark and methodology for continual skill acquisition in LLM agents — teaching agents to learn new procedural skills from experience. Baseline (no skill): 10.17%. Human-authored skills: 74.50%. Automated skill-learning methods: ~30% (ceiling). External feedback outperforms self-feedback for skill refinement. No automated method dominates across task types. Stronger base models don't reliably produce better learned skills.

---

## Problem Setting: Continual Skill Learning

Traditional agents rely on static, pre-authored skill libraries. SkillLearnBench evaluates whether agents can **learn new skills from experience** — analogous to how a human employee learns new procedures over time through practice and feedback.

### Task Setup

1. Agent receives a task that requires a skill it doesn't currently have
2. Agent attempts the task (often failing or performing poorly)
3. Agent receives feedback (success/failure signal, external critique, or self-generated)
4. Agent updates its skill representation
5. Agent attempts similar tasks — does performance improve?

---

## Baseline Performance

| Condition | Performance |
|-----------|-------------|
| **No skills (baseline)** | **10.17%** |
| Best automated skill-learning method | ~30% |
| **Human-authored skills** | **74.50%** |

The 74.50% → 10.17% gap (64.3pp) represents the current ceiling on automated skill learning — a large open research problem.

---

## Feedback Sources Compared

| Feedback Source | Performance | Notes |
|----------------|-------------|-------|
| **External feedback** | **Higher** | Human critique, test suites, environment signals |
| Self-feedback | Lower | Agent critiques its own outputs |
| No feedback | Lowest | One-shot skill extraction |

**External feedback > self-feedback**: When agents critique their own skill-learning, they amplify existing biases rather than correcting them. External signals (test pass/fail, human review, environment rewards) provide genuine correction.

---

## Why Self-Feedback Fails

Self-feedback in skill learning fails for the same reasons as SkillsBench's self-generated skills:

1. **Recursive echo chamber**: The agent evaluates its own skill using the same priors that created the flawed skill
2. **No ground truth**: Without external reference, the agent can't detect systematic blind spots
3. **Coherence ≠ correctness**: Self-generated critiques tend to focus on surface consistency rather than functional correctness

---

## No Method Dominates Across Task Types

The paper tests multiple automated skill-learning methods:

| Method | Best Domain | Worst Domain |
|--------|-------------|--------------|
| In-context learning from demonstrations | Procedural tasks | Creative tasks |
| Error-driven refinement | Debugging tasks | Open-ended reasoning |
| Reward signal distillation | RL-compatible tasks | Natural language tasks |
| Constitutional self-revision | Alignment-sensitive tasks | Technical precision |

**Finding**: No single automated method wins across all task types. Human-authored skills remain the only approach that generalizes well.

---

## Base Model Strength ≠ Better Learned Skills

A counterintuitive finding: stronger base models (measured by standard benchmarks) do **not** reliably produce better learned skills.

| Model Size / Capability | Skill Learning Rate |
|------------------------|---------------------|
| Smaller/weaker models | Comparable or sometimes better |
| Larger/stronger models | Not reliably better |

**Hypothesis**: Stronger models may over-rely on their pre-existing knowledge and resist updating toward the task-specific skill. Weaker models, having less prior knowledge, may be more receptive to learned procedures.

---

## Skill Representation Formats Evaluated

| Format | Learnability | Executability |
|--------|-------------|--------------|
| Natural language prose | High | Low |
| Numbered steps | High | High |
| Pseudocode | Moderate | High |
| Code | Low | Highest |
| Structured JSON/YAML | Low | High |

**Numbered step format** balances learnability (easy to generate from demonstrations) with executability (easy for the agent to follow during task execution).

---

## Key Metric: Skill Transfer Rate

The benchmark introduces **Skill Transfer Rate (STR)**: the fraction of learned skill improvements that transfer to structurally similar but unseen tasks.

High STR = skill generalizes well (good)
Low STR = skill overfits to training examples (bad)

Best automated methods achieve STR ~0.4–0.6 vs. human-authored skills at ~0.8.

---

## Continual Learning Without Forgetting

The benchmark also evaluates catastrophic forgetting — do newly learned skills degrade previously learned ones?

- **Isolated skill updates**: No forgetting (adding new skill file doesn't affect old ones)
- **In-context refinement**: Low forgetting risk (skills stored as separate context blocks)
- **Fine-tuning approaches**: Significant forgetting risk (weight updates affect all skills)

Context-storage skill representations (skills as markdown files) are catastrophic-forgetting-resistant by design.

---

## Workspace Relevance

Critical calibration for workspace skill lifecycle management:

1. **10.17% (no skill) → 74.50% (human-authored)**: The 64pp gap confirms that investing in high-quality human-authored skills (like the workspace's `research-hub`, `autoresearch`, `harness-meta`) is the highest-leverage improvement available.
2. **Automated methods plateau at ~30%**: Don't automate skill generation for production use — current automated methods can't approach human-authored quality. Human gate on new skills remains mandatory.
3. **External feedback > self-feedback**: When refining skills (e.g., improving `research-hub` after observing failures), use external feedback (user reports, task success rates) not self-generated critiques.
4. **No method dominates across task types**: The workspace skill library needs different approaches for different domains — a research skill and a security-review skill can't use the same generation methodology.
5. **Context-storage is forgetting-resistant**: Workspace skills as `.md` files in `.claude/skills/` (context-storage) are correctly designed — no catastrophic forgetting risk unlike fine-tuned approaches.
6. **Numbered step format**: The existing workspace skill format (numbered steps + I/O contracts) is empirically the best balance of learnability and executability.

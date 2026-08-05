---
url: "https://arxiv.org/abs/2606.05922"
title: "Evolving Agents in the Dark: Retrospective Harness Optimization via Self-Preference"
archived_date: 2026-06-14
arxiv_id: 2606.05922
authors: ["Wenbo Pan", "Shujie Liu", "Chin-Yew Lin", "Jingying Zeng", "Xianfeng Tang", "Xiangyang Zhou", "Yan Lu", "Xiaohua Jia"]
pdf_path: pdfs/2606.05922.pdf
published_date: 2026-06-04
---

# Evolving Agents in the Dark: Retrospective Harness Optimization via Self-Preference

**Authors**: Wenbo Pan, Shujie Liu, Chin-Yew Lin, Jingying Zeng, Xianfeng Tang, Xiangyang Zhou, Yan Lu, Xiaohua Jia
**Published**: June 2026
**Source**: https://arxiv.org/abs/2606.05922
**arXiv ID**: 2606.05922
**Categories**: not specified in fetched content

---

## Abstract

RHO (Retrospective Harness Optimization) is a self-supervised technique for improving AI agent capabilities through past task data rather than requiring labeled validation sets. The method selects challenging previous tasks, re-executes them, and leverages the agent's own judgment to identify and implement the most beneficial harness updates, achieving significant performance gains on software engineering benchmarks without external evaluation.

*(Note: verbatim abstract not available in fetched content; above is a summary reconstruction from cached fetch.)*

---

## Key Findings

- **SWE-Bench Pro**: Baseline 59% → RHO 78% (+19 percentage points), using 103 agent calls, zero validation labels required.
- **Terminal-Bench 2**: Baseline 71% → RHO 76% (+5 percentage points).
- **GAIA-2**: Baseline 29% → RHO 37% (+8 percentage points).
- **vs. Meta-Harness (1 round, with labels)**: RHO 78% vs. Meta-Harness 62%, despite Meta-Harness requiring held-out labeled data; RHO uses 103 vs. 41 agent calls (2.5× more calls, but label-free).
- **vs. Multi-round Meta-Harness (10 rounds)**: Meta-Harness reached 80% but required ~320 agent calls (3.1× RHO's budget) plus held-out labels.
- **Ablation — coreset strategy** (Figure 5): Pure difficulty = no improvement (stayed at ~59%); pure diversity = suboptimal; DPP balance at θ=0.7 = optimal +19% gain.
- **Ablation — diagnostic signals** (Table 4, SWE-Bench Pro): Full diagnosis = 78%; without self-consistency = 56%; without self-validation = 70%; raw trajectory (no diagnosis) = 60%.
- **Candidate variance** (Table 3): Lowest-scoring candidate still improved over baseline (0.73 vs. 0.59); selected candidate = 0.78; std ~0.06 across three candidates.

## Self-Preference Mechanism (no ground-truth)

RHO operates in three stages using only past trajectories, with no external oracle:

**1. Coreset Selection**: Selects k=10 challenging, diverse tasks from past trajectories using a Determinantal Point Process (DPP) kernel (θ=0.7 difficulty, 0.3 diversity). A language model "difficulty judge" scores complexity and extracts failure-mode fingerprints.

**2. Group Rollout & Diagnosis**: For each coreset task, the agent generates G=3 parallel solution attempts. Two self-referential diagnostic signals are extracted:
- *Self-validation*: Agent inspects each trajectory for correctness issues — "incorrect tool invocations, false assumptions, and premature stopping."
- *Self-consistency*: Agent identifies contradictions across parallel trajectories, flagging "divergent plans, tool sequences, or final answers." Diagnosed issues are ranked by severity ∈ [0,1] as soft attention weights.

**3. Best-of-N Harness Selection**: N=3 candidate harnesses are generated from diagnosed weaknesses. Each candidate is tested on the 10 coreset tasks. **Acceptance gate**: pairwise ranking where the agent compares candidate trajectories against baseline trajectories on the same task, producing scores in [−10, 10]. A candidate is accepted **only if mean pairwise score > 0**; zero or negative scores trigger no update (rejection).

**Core principle**: "The agent's own trajectories already contain the signal needed to improve it, since re-solving past tasks and comparing the outcomes exposes where the harness fails."

**Critical limitation**: RHO assumes environments that "reset cleanly and tolerate repeated attempts," excluding one-shot or irreversible tasks. In open environments, past trajectories can embed adversarial content injected mid-task, requiring "human approval for sensitive harness edits."

## Quantified Conditions

- **Coreset size**: k = 10 tasks
- **Parallel rollouts per task**: G = 3
- **Candidate harnesses generated**: N = 3
- **Acceptance threshold**: mean pairwise ranking score strictly > 0 (integer scale [−10, 10])
- **DPP balance parameter**: θ = 0.7 (70% difficulty, 30% diversity)
- **Severity weighting**: soft attention weights ∈ [0, 1], not hard thresholds
- **Orbit timeout**: 900 seconds (SWE-Bench Pro), 300 seconds (Terminal-Bench 2), dataset-specific for GAIA-2

## Relevance to The Loop (harness self-improvement)

RHO is a direct empirical instantiation of the RECORD→OBSERVE→APPLY loop for harness self-improvement: it replaces external ground-truth labels with self-consistency signals across multiple rollouts, addressing precisely the `unverified_success` problem. The acceptance gate (pairwise score > 0, agent-judged) is an oracle-free verdict mechanism — analogous to the workspace rule that "subagent/workflow verdict ≠ evidence; must grep-verify." The critical caveat that RHO requires clean-resettable environments and excludes one-shot/irreversible tasks directly maps to The Loop's "APPLY gate for destructive/irreversible changes" — self-preference cannot substitute for external verification in non-resettable contexts. The human-approval requirement for sensitive harness edits in open environments mirrors the workspace's P0 hotfix gate and production safety redlines.

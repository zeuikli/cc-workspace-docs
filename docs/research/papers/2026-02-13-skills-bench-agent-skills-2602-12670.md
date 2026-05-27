---
title: "SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks"
authors: Samuel Schmidgall, Michael Moor, Hamed Nilforoshan, Jure Leskovec
published: 2026-02-13
source: "https://arxiv.org/abs/2602.12670"
---

# SkillsBench: Benchmarking How Well Agent Skills Work Across Diverse Tasks

**Authors**: Samuel Schmidgall, Michael Moor, Hamed Nilforoshan, Jure Leskovec
**Published**: February 13, 2026
**Source**: https://arxiv.org/abs/2602.12670
**arXiv ID**: 2602.12670
**Categories**: cs.AI, cs.LG

---

## Abstract

SkillsBench is the first benchmark specifically designed to evaluate how well agent **Skills** (structured packages of procedural knowledge) improve performance across diverse tasks. Across 84 tasks in 11 domains, curated skills increase performance by +16.2 percentage points while self-generated skills decrease performance by −1.3pp. Optimal skill count is 2–3; beyond that, performance degrades from context overload. Healthcare tasks benefit most (+51.9pp); software engineering benefits least (+4.5pp).

---

## Benchmark Design

| Parameter | Value |
|-----------|-------|
| Total tasks | 84 |
| Domains | 11 |
| Skill types evaluated | No skills, curated skills, self-generated skills |
| Models tested | Claude Sonnet 4.5, GPT-5, Gemini 3.1 Pro (primary) |

### Domains Covered

| Domain | Task Examples |
|--------|--------------|
| Healthcare | Medical diagnosis, treatment planning |
| Software Engineering | Code generation, debugging |
| Legal | Contract review, case analysis |
| Finance | Investment analysis, risk assessment |
| Education | Curriculum design, problem explanation |
| Scientific Research | Hypothesis generation, literature synthesis |
| Data Analysis | Statistical analysis, visualization |
| Creative Writing | Story generation, editing |
| Customer Service | Query resolution, escalation |
| Logistics | Route optimization, supply chain |
| Cybersecurity | Threat analysis, incident response |

---

## Key Results

### Skills vs. No Skills

| Condition | Performance Delta |
|-----------|------------------|
| **Curated skills** | **+16.2 pp** |
| No skills (baseline) | 0 pp |
| Self-generated skills | **−1.3 pp** |

**Critical finding**: Self-generated skills (where the agent writes its own skill documentation) underperform baseline. Only externally curated skills reliably improve performance.

### Performance by Domain

| Domain | Curated Skill Gain |
|--------|-------------------|
| **Healthcare** | **+51.9 pp** |
| Legal | +38.7 pp |
| Scientific Research | +29.4 pp |
| Finance | +22.1 pp |
| Education | +18.6 pp |
| Data Analysis | +15.3 pp |
| Customer Service | +12.8 pp |
| Creative Writing | +9.2 pp |
| Logistics | +7.6 pp |
| Cybersecurity | +6.1 pp |
| **Software Engineering** | **+4.5 pp** |

### Why Healthcare Gains Most, SWE Gains Least

**Healthcare**: Domain knowledge is highly specialized and not uniformly present in model pretraining. Skills provide critical procedural knowledge (clinical guidelines, diagnostic frameworks) that models lack or underweight.

**Software Engineering**: Models are extensively pretrained on code — SWE knowledge is already densely represented in weights. Skills add marginal procedural information on top of existing strong priors.

---

## Optimal Skill Count

| Number of Skills | Performance (vs. Baseline) |
|-----------------|---------------------------|
| 0 | Baseline |
| 1 | +8.4 pp |
| **2** | **+15.9 pp** |
| **3** | **+16.2 pp (peak)** |
| 4 | +12.7 pp |
| 5 | +9.1 pp |
| 6+ | Degrading further |

**Finding**: 2–3 skills is the empirical optimum. Beyond 3 skills, context overload reduces performance — the model's attention is diluted across too many procedural specifications.

---

## Why Self-Generated Skills Fail (−1.3 pp)

When agents generate their own skills from examples or task descriptions, performance drops below baseline. Root causes identified:

1. **Recursive drift**: Self-generated skills reflect the model's existing biases, amplifying errors rather than correcting them
2. **Circular reasoning**: The model generates skills based on what it already does, not what it should do differently
3. **Overfitting to examples**: Self-generated skills overfit to the specific examples used in generation, reducing generalization
4. **False confidence**: Skills authored by the model create false confidence, causing the model to skip verification steps it would otherwise perform

---

## Skill Quality Dimensions

The paper proposes three dimensions for evaluating skill quality:

| Dimension | Description | Correlates With |
|-----------|-------------|-----------------|
| **Specificity** | Concrete procedural steps vs. vague guidance | Higher performance gains |
| **Groundedness** | Based on verified domain knowledge | Reliability |
| **Orthogonality** | Skills don't overlap significantly | Efficiency at 2-3 count |

Low-quality skills (high vagueness, ungrounded assertions, high overlap) explain the self-generated skill failure mode.

---

## Implications for Skill Design

1. **Curate, don't generate**: Human-authored skills with domain expert review outperform agent-generated skills by 17.5pp
2. **Domain matters**: Prioritize skills for high-knowledge-barrier domains (healthcare, legal, science) over domains with dense pretraining (coding, math)
3. **Limit to 2-3 skills per session**: Loading more degrades performance through context dilution
4. **Structure over prose**: Skills with numbered steps, decision criteria, and explicit procedures outperform narrative-style skills

---

## Workspace Relevance

Directly validates and calibrates workspace skill design:

1. **+16.2pp curated skills vs. −1.3pp self-generated**: The workspace skill design (human-authored, structured, with I/O contracts) is the right approach. Avoid having agents auto-generate new skills at runtime.
2. **2-3 skills optimal**: When loading context into a session via `@rules/`, load only the most relevant 2-3 skills per task. CLAUDE.md's lazy-load approach (on-demand skill triggers) correctly avoids the context overload trap.
3. **+51.9pp Healthcare, +4.5pp SWE**: Most workspace skills focus on SWE (implementer, test-writer, review-hub) — the lowest-gain domain. Workspace ROI from skills would be higher in security, architecture, and research domains where knowledge is more specialized.
4. **Self-generated skill risk for autoresearch**: The autoresearch loop should NOT be configured to write new skills to `.claude/skills/` without human review — recursive drift is empirically confirmed to hurt performance.
5. **Skill quality dimensions (specificity, groundedness, orthogonality)**: Useful checklist for evaluating existing workspace skills and identifying which ones to refactor or remove.

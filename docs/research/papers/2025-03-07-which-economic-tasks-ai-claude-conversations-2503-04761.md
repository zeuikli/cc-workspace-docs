---
title: "Which Economic Tasks are Performed with AI? Evidence from Millions of Claude Conversations"
authors: "Kunal Handa, Alex Tamkin, Miles McCain, Saffron Huang, Esin Durmus, et al."
published: 2025-03-07
source: "https://arxiv.org/abs/2503.04761"
---

# Which Economic Tasks are Performed with AI? Evidence from Millions of Claude Conversations

**Authors**: Kunal Handa, Alex Tamkin, Miles McCain, Saffron Huang, Esin Durmus, Sarah Heck, Jared Mueller, Jerry Hong, Stuart Ritchie, Tim Belonax, Kevin K. Troy, Dario Amodei, Jared Kaplan, Jack Clark, Deep Ganguli (all Anthropic)
**Submitted**: February 11, 2025 (appeared on arxiv March 2025)
**Source**: https://arxiv.org/abs/2503.04761
**arXiv ID**: 2503.04761
**Data period**: December 2024 – January 2025

---

## Abstract

First large-scale empirical analysis of how AI systems are actually used across economic tasks, using privacy-preserving Clio analysis of 4+ million Claude.ai conversations mapped to the U.S. Department of Labor's O*NET Database. AI usage concentrates in software development and writing (~50% combined). Approximately 36% of occupations use AI for at least 25% of their tasks. 57% of usage is augmentative; 43% automative.

---

## Methodology

**Dataset**: 1 million Claude.ai Free/Pro conversations (December 2024 – January 2025)
**Mapping tool**: Clio (privacy-preserving) → O*NET Database (~20,000 task statements)
**Hierarchy**: 3 levels — 12 top-level / 474 middle-level / 19,530 O*NET base tasks

### Classification accuracy (human validation, 150 examples)
| Level | Accuracy |
|-------|----------|
| Top level | 95.3% |
| Middle level | 91.3% |
| O*NET base level | 86.0% |

---

## Task Concentration

### Top-Level Distribution

| Category | Share of AI Usage |
|----------|------------------|
| Computer and Mathematical | **37.2%** |
| Arts, Design, Entertainment, Media | 10.3% |
| Education | significant |
| Business/Finance | significant |
| Physical labor occupations | minimal |

### Middle-Level Tasks (most common)

| Task | Share |
|------|-------|
| Software development & website maintenance | ~14% |
| Computer systems programming & debugging | ~11% |
| System administration, hardware/software troubleshooting | 4–6% |
| Marketing/promotional strategies | ~2–3% |
| Data science & ML applications | ~2% |

---

## Depth of AI Use Within Occupations

| Threshold (tasks with AI usage) | % of Occupations |
|----------------------------------|-----------------|
| At least 75% of tasks | **4%** |
| At least 50% of tasks | 11% |
| At least 25% of tasks | **36%** |
| At least 10% of tasks | ~57% |

**Key finding**: Deep AI integration (>75% task coverage) is rare. AI primarily assists specific tasks within occupations, not wholesale job automation.

---

## Skills Distribution

### Highest AI presence
Critical Thinking, Reading Comprehension, Programming, Writing

### Lowest AI presence
Installation, Equipment Maintenance, Repairing (physical interaction skills)

---

## Usage by Wage & Barrier to Entry

**Wage**: Peaks in upper wage quartile (Computer Programmers, Web Developers). Drops off at both extremes — waiters and anesthesiologists both show low usage.

**Job Zone (preparation required)**:
- Zone 1–3 (little/medium prep): Lower AI usage
- **Zone 4 (considerable prep / bachelor's degree): Peak usage**
- Zone 5 (extensive prep / advanced degrees): Falls below Zone 4

Human barriers to entry may be significantly different from barriers for language models.

---

## Automation vs. Augmentation

57% augmentative, 43% automative split across all conversations.

### Five Collaboration Patterns

| Pattern | Type | % | Characteristics |
|---------|------|---|-----------------|
| Directive | Automative | — | Complete task delegation, minimal interaction (e.g., "Format this doc in Markdown") |
| Feedback Loop | Automative | — | Task completion guided by iterative error feedback (e.g., debugging) |
| Task Iteration | Augmentative | — | Collaborative refinement (e.g., draft → refine marketing strategy) |
| Learning | Augmentative | — | Knowledge acquisition (e.g., "Explain how neural networks work") |
| Validation | Augmentative | smallest | Work verification (e.g., checking SQL logic) |

### Automation-heavy tasks: writing, content generation, schoolwork, coding/debugging
### Augmentation-heavy tasks: front-end development, professional communication, general education

---

## Model Specialization (Claude 3 Opus vs Claude 3.5 Sonnet)

Dataset: ~54% Sonnet (new), ~46% Opus

| Model | Usage Profile |
|-------|---------------|
| Claude 3 Opus | Higher for creative/educational work — reflects unique character/writing style |
| Claude 3.5 Sonnet (new) | Preferred for coding/software development — reflects stronger coding abilities |

---

## Comparison to Predictive Studies

| Study | Prediction | Actual Finding |
|-------|-----------|---------------|
| Webb (2019) | Highest AI exposure at 90th wage percentile | Actual peak at mid-to-high wage (upper quartile, not top) |
| Eloundou et al. (2023) | 80% of workers could have 10%+ tasks affected | **Actual: ~57%** of occupations using AI for 10%+ tasks |
| Eloundou et al. (2023) | Higher healthcare usage predicted | Healthcare usage not yet materialized; scientific usage higher than predicted |

---

## Dataset Validation

Non-work conversations: only **23%** of dataset. Coursework: **5–10%**. The majority of non-work interactions still mapped to occupational tasks (nutrition planning → dietitian tasks; trading strategy → financial analyst tasks).

---

## Limitations

- Snapshot (Dec 2024–Jan 2025) may not represent longer time windows
- Claude.ai text-only; excludes image/video output modalities
- Model classification introduces noise
- Cannot track what users do with AI outputs (copy-paste rates unknown)
- O*NET is U.S.-centric; misses global occupational categories

---

## Conclusion

Current AI usage peaks in software development and technical writing. Deep integration (>75% task coverage) affects only ~4% of occupations. The 57/43 augmentation/automation split suggests AI is primarily a collaborative tool, not yet a wholesale job replacer. Empirical tracking frameworks are essential as AI capabilities expand.

---

## Workspace Relevance

This is the primary empirical data on **how Claude is actually used in practice**. Key calibrations for workspace:

1. **Software development = 37% of Claude usage**: validates focus on `implementer`, `test-writer`, `review-hub` as primary workflow skills
2. **Opus preferred for creative/educational; Sonnet for coding**: aligns with `sonnet-pilot`'s coding-heavy design and `opus-pilot`'s architecture/creative use cases
3. **57% augmentative**: `autoresearch` and `research-hub` are augmentation tools — consistent with design
4. **4% deep integration**: AI is not yet replacing whole jobs — workspace skill design (individual task-level) is correct granularity
5. **36% occupations at 25% task threshold**: broad adoption, but still task-selective — task-level harness design remains correct approach

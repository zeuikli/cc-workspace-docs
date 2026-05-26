---
title: "SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?"
authors: "Xiang Deng, Jeff Da, Edwin Pan, Yannis Yiming He, Charles Ide, Kanak Garg, Niklas Lauffer, Andrew Park, Nitin Pasari, Chetan Rane, Karmini Sampath, Maya Krishnan, Srivatsa Kundurthy, Sean Hendryx, Zifan Wang, Vijay Bharadwaj, Jeff Holm, Raja Aluri, Chen Bo Calvin Zhang, Noah Jacobson, Bing Liu, Brad Kenstler"
published: "2025-09-21"
source: "https://arxiv.org/abs/2509.16941"
---

# SWE-Bench Pro: Can AI Agents Solve Long-Horizon Software Engineering Tasks?

**Authors**: Xiang Deng, Jeff Da, Edwin Pan, Yannis Yiming He, Charles Ide, Kanak Garg, Niklas Lauffer, et al. (22 authors)
**Published**: September 21, 2025 (v2: November 14, 2025)
**Source**: https://arxiv.org/abs/2509.16941
**arXiv ID**: 2509.16941
**Categories**: cs.SE, cs.CL
**License**: CC BY 4.0

---

## Abstract

SWE-Bench Pro is a substantially more challenging benchmark that builds upon SWE-Bench's best practices but is explicitly designed to capture **realistic, complex, enterprise-level problems** beyond the scope of SWE-Bench. The dataset contains 1,865 problems from 41 actively maintained repositories, targeting long-horizon tasks that may require hours to days for a professional software engineer to complete.

---

## Motivation: Limitations of SWE-Bench (Verified)

SWE-Bench Verified has become the de facto coding benchmark, but frontier models now score 80%+. The benchmark has three gaps:
1. **Scale**: Original SWE-Bench tasks are resolved by small, localized patches
2. **Realism**: Enterprise codebases involve multi-file, multi-component changes
3. **Contamination**: Public benchmark data may be in training sets

SWE-Bench Pro addresses all three with copyleft-licensed and proprietary repositories.

---

## Dataset Design

### Scale

| Metric | SWE-Bench | SWE-Bench Pro |
|--------|-----------|---------------|
| Problems | 2,294 | 1,865 |
| Repositories | 12 | 41 |
| Avg lines changed | ~30 | **107.4** |
| Avg files changed | ~1–2 | **4.1** |
| Tasks >100 lines | few | **100+** |

### Partitions

| Set | Size | Access |
|-----|------|--------|
| Public | 731 | Open |
| Held-out | 858 | Evaluated by maintainers |
| Commercial | 276 | Proprietary codebases (GPL + startup partners) |

### Contamination Resistance

- **Public/Held-out**: GPL-licensed repositories (model training data typically excludes GPL)
- **Commercial**: Proprietary codebases from early-stage startup partnerships — never in any training set

### Human Verification

Three-stage augmentation per problem:
1. Problem statement with explicit requirements
2. Interface specifications
3. Thoroughly vetted test suites

---

## Evaluation Results

### Public Set Performance (N=731)

| Model | Resolution Rate |
|-------|----------------|
| GPT-5 | **23.3%** |
| Claude Opus 4.1 | 22.7% |
| Claude Sonnet 4 | 17.6% |
| Gemini 2.5 Pro | 13.5% |
| GPT-4o | 4.9% |

*Note: For context, Claude Opus 4.7 improved from 53.4% → 64.3% on SWE-Bench Pro per the Opus 4.7 System Card (April 2026)*

### Commercial Set Performance (N=276)

| Model | Resolution Rate |
|-------|----------------|
| Claude Opus 4.1 | **17.8%** |
| GPT-5 | 14.9% |
| Gemini 2.5 Pro | 10.1% |

### Language Performance

- **High resolution**: Python and Go (30%+)
- **Variable**: JavaScript and TypeScript

---

## Failure Mode Analysis (LLM-as-a-judge)

| Model | Primary Failure Mode | Rate |
|-------|---------------------|------|
| Claude Opus 4.1 (frontier) | **Semantic understanding** | 35.9% |
| Qwen3 32B (smaller) | Syntax errors + tool-use | 42% |

Frontier models understand the task but fail semantically; smaller models fail on basic execution — different capability gaps require different interventions.

---

## Limitations and Future Directions

- **Incomplete language coverage**: Primarily Python/Go/JS/TS
- **Test-suite verification**: May miss functionally correct but test-incompatible patches
- **Over-specification risk**: Human augmentation may constrain valid solution space
- **Needs expansion**: More languages, alternative evaluation metrics, collaborative scenarios

---

## Workspace Relevance

SWE-Bench Pro is the **successor benchmark to SWE-Bench Verified** and the primary long-horizon coding evaluation for frontier models. Key numbers for calibration:

- Claude Opus 4.7 (April 2026): **64.3%** on SWE-Bench Pro (per system card)
- GPT-5.5 (April 2026): **58.6%** on SWE-Bench Pro (per OpenAI announcement)
- These rates are ~3× harder than SWE-Bench Verified (Opus 4.7: 87.6%)

For `opus-pilot`: SWE-Bench Pro is the relevant benchmark when using Opus for long-horizon software tasks. The 64.3% rate means ~1 in 3 enterprise-scale tasks still fails — set expectations accordingly.

Complements `harness-meta` CAR framework: the 4.1-file, 107.4-line average change scope is exactly the range where harness-level verification protocols (H3 from `2605.13357`) matter most.

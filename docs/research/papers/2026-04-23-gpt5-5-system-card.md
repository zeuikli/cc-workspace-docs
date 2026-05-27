---
title: "GPT-5.5 System Card"
authors: OpenAI
published: 2026-04-23
source: "https://deploymentsafety.openai.com/gpt-5-5"
---

# GPT-5.5 System Card

**Authors**: OpenAI
**Published**: April 23, 2026 (updated April 24, 2026 with API safeguard details)
**Source**: https://deploymentsafety.openai.com/gpt-5-5
**PDF**: https://deploymentsafety.openai.com/gpt-5-5/gpt-5-5.pdf
**Announcement**: https://openai.com/index/introducing-gpt-5-5/

---

## Abstract

GPT-5.5 is OpenAI's model designed for **complex, real-world workflows**: code writing, web research, multi-step document and spreadsheet creation, and tool-enabled tasks. Priced higher than GPT-5.4 but 40% more token-efficient, resulting in ~20% higher operational cost overall. Achieves state-of-the-art on Terminal-Bench Hard, GDPval-AA, and APEX-Agents-AA.

---

## Model Variants

| Variant | Notes |
|---------|-------|
| GPT-5.5 | Standard API model |
| GPT-5.5 Pro | Same underlying model + enhanced parallel test-time compute |

---

## Pricing

| Tier | Input | Output | vs GPT-5.4 |
|------|-------|--------|------------|
| GPT-5.5 | $5 / 1M | $30 / 1M | 2× cost per token |
| Effective cost (with efficiency) | ~20% higher overall | | -40% tokens used |

**Cost-performance tradeoffs** (from Artificial Analysis benchmarks):
- GPT-5.5 (medium effort) ≈ Claude Opus 4.7 performance at ~¼ the cost
- GPT-5.5 (low effort) ≈ comparable performance at ~½ the cost

---

## Benchmark Results

### Agent and Reasoning Benchmarks

| Benchmark | GPT-5.5 | Notes |
|-----------|---------|-------|
| Terminal-Bench Hard | **SoTA** | Best-in-class |
| GDPval-AA | **1785 Elo** | Leading by significant margin |
| APEX-Agents-AA | **SoTA** | Best-in-class |
| AA-Omniscience | **57%** | Highest factual accuracy |
| SWE-bench Pro | **58.6%** | Single-pass, end-to-end |

### Coding Benchmark

| Benchmark | Score | Notes |
|-----------|-------|-------|
| SWE-bench Pro | 58.6% | End-to-end single pass |

*For comparison: Claude Opus 4.7: 64.3% on SWE-bench Pro*

### Health

| Benchmark | Score | Delta |
|-----------|-------|-------|
| HealthBench length-adjusted | 56.5 | +2.5 pts vs predecessor |
| HealthBench Professional | 51.8% | +3.7 pts |

### Hallucination

| Model | Hallucination Rate |
|-------|------------------|
| GPT-5.5 | **86%** (high — individual claims correct rate: +23%) |
| Claude Opus 4.7 (max) | 36% |

**Note**: Despite 23% improvement in individual claim factual accuracy, the overall hallucination rate of 86% is substantially higher than Claude Opus 4.7. Artificial Analysis notes the model "may provide confident answers even without reliable knowledge."

---

## Safety Evaluation

### Disallowed Content
- Performance "on par with GPT-5.4-Thinking" across challenging prompts
- Category regressions statistically insignificant

### Robustness
- Jailbreak evaluations: defender success rates comparable to predecessors
- Prompt injection resistance robust across connector-based attacks

### Cybersecurity (High Capability, Sub-Critical)
- Measurable improvements in vulnerability identification and exploitation tasks
- Cannot independently produce functional full-chain exploits against hardened real-world systems
- Cyber range: **93.33% pass rate** (up from 73.33% for GPT-5.4-Thinking)

### Biological/Chemical (High Capability)
- Hard-negative protein binding prediction below concerning thresholds
- DNA sequence design significantly underperforms baseline methods

### AI Self-Improvement
- Does not meet High capability thresholds
- Falls short of mid-career research engineer performance levels

---

## Key Safety Findings

### CoT Controllability
Lower ability to reshape reasoning traces compared to predecessors — **suggests improved monitoring reliability** (reasoning is more stable and predictable).

### Red Teaming
~200 early-access partners provided feedback; public jailbreak bounty program used for universal jailbreak research.

---

## Safeguards

- Model safety training + conversation monitoring + actor-level enforcement
- Expanded safeguards for biological and cybersecurity domains
- Trusted access program for defenders (less restricted model variants)

---

## Third-Party Assessment

From Artificial Analysis (April 2026):
- GPT-5.5 **leads the Intelligence Index**, ending a three-way tie among OpenAI, Anthropic, and Google
- Dominates Terminal-Bench Hard, GDPval-AA, APEX-Agents-AA
- Leads 5 of 8 key evaluations; 2nd place on the remaining 3

From Zvi (independent reviewer):
- "Solid improvement"; performs competitively with Claude Opus 4.7 on straightforward tasks
- Claude may excel on open-ended interpretation work
- System card "provides less detail than Anthropic's Mythos and Opus model cards"

---

## Transparency Note

The GPT-5.5 system card is notably shorter than Anthropic's system cards. Several reviewers noted reduced transparency compared to Claude system cards regarding alignment issues.

---

## Workspace Relevance

GPT-5.5 is the primary OpenAI competitor reference for May 2026:

1. **Benchmark calibration**: GPT-5.5 leads on Terminal-Bench Hard and GDPval-AA; Claude Opus 4.7 leads on SWE-bench Pro (64.3% vs 58.6%)
2. **Hallucination gap**: GPT-5.5 at 86% vs Claude Opus 4.7 at 36% — significant reliability difference for factual tasks in `research-hub` and `autoresearch`
3. **Cost-efficiency**: GPT-5.5 (medium) ≈ Opus 4.7 at ¼ the cost — relevant for `finops` when choosing provider
4. **Terminal-Bench SoTA**: GPT-5.5 is the current best agent on Terminal-Bench Hard, above Claude Code + Opus 4.5 (58% in the Terminal-Bench paper from January 2026)
5. **CoT stability**: Lower CoT controllability = more predictable reasoning chains — favorable for monitoring in `harness-meta` observability design

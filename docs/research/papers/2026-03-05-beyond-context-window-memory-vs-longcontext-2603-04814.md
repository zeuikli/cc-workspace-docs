---
title: "Beyond the Context Window: Memory vs. Long-Context for LLM Agents"
authors: "Tian Luo, Yijun Yang, Jiarui Liu, Yuhui Zhang, Hang Li"
published: "2026-03-05"
source: "https://arxiv.org/abs/2603.04814"
---

# Beyond the Context Window: Memory vs. Long-Context for LLM Agents

**Authors**: Tian Luo, Yijun Yang, Jiarui Liu, Yuhui Zhang, Hang Li
**Published**: March 5, 2026
**Source**: https://arxiv.org/abs/2603.04814
**arXiv ID**: 2603.04814
**Categories**: cs.AI, cs.CL, cs.LG

---

## Abstract

Systematic empirical comparison of memory-based and long-context approaches for LLM agents operating over multi-turn conversations. Long-context (keeping full history in context window) outperforms memory-based compression by 33.4–35.2 percentage points in accuracy. However, memory becomes economically favorable after approximately 10 conversation turns at 100K token context sizes. Memory systems achieve 35:1 compression but with significant information loss.

---

## Problem Setting

As conversations grow longer, agents face a fundamental choice:

| Approach | Mechanism | Cost | Risk |
|----------|-----------|------|------|
| **Long-context** | Keep full conversation in context window | Grows linearly with turns | None (no information loss) |
| **Memory-based** | Compress older turns into memory representations | Near-constant after compression | Information loss from 35:1 compression |

This paper is the first large-scale empirical comparison of these two strategies across multiple task types, conversation lengths, and model sizes.

---

## Core Results: Accuracy Comparison

### Long-Context Outperforms Memory

| Metric | Long-Context | Memory | Delta |
|--------|-------------|--------|-------|
| **Overall accuracy** | Higher | Lower | **+33.4–35.2pp (long-context wins)** |
| Short conversations (≤5 turns) | High | High | ~Equivalent |
| Medium conversations (10–20 turns) | High | Moderate | +25–35pp |
| Long conversations (30+ turns) | Moderate | Low | +35pp+ |

**Key finding**: Long-context consistently outperforms memory-based approaches. The performance gap grows with conversation length.

---

## Economic Break-Even Analysis

### When Memory Becomes Cost-Effective

At a 100K token context window model:

| Conversation Length | Long-Context Cost | Memory Cost | Winner |
|---------------------|------------------|-------------|--------|
| 5 turns | Low | Moderate (compression overhead) | Long-context |
| **10 turns** | Moderate | **~Equal** | **Break-even** |
| 20 turns | High | Lower | **Memory (26% cheaper)** |
| 30 turns | Very high | Lower | Memory (40%+ cheaper) |

**Break-even point: ~10 turns at 100K token context**. Below 10 turns, long-context is both better and cheaper. Above 10 turns, memory costs less but sacrifices accuracy.

### Memory Cost Advantage at 20 Turns

At 20 conversation turns:
- Long-context: full 20-turn history in context (expensive)
- Memory: compressed representation (~35:1) + recent turns (cheap)
- **Memory is 26% cheaper** at 20 turns
- But accuracy is 25–35pp lower

---

## The 35:1 Compression Problem

Memory systems achieve 35:1 compression ratio — compressing 35 tokens of conversation into 1 token of memory representation.

### Information Loss at 35:1

| Information Type | Preservation Rate at 35:1 |
|-----------------|--------------------------|
| Main topic/intent | High (~90%) |
| Specific facts (names, numbers, dates) | Moderate (~60%) |
| Reasoning chains | Low (~40%) |
| Nuanced constraints | Very low (~25%) |
| Exact wording | Minimal (<10%) |

**Key finding**: The 35:1 compression ratio preserves broad topics but loses specific facts and nuanced constraints — exactly the information that matters for accurate task completion.

---

## Task-Type Sensitivity

Different tasks show different sensitivity to memory compression:

| Task Type | Long-Context Advantage |
|-----------|----------------------|
| **Multi-step reasoning** | Highest (+45pp) |
| **Fact-dependent tasks** | High (+38pp) |
| **Code with context dependencies** | High (+35pp) |
| Creative tasks | Moderate (+20pp) |
| Simple retrieval | Low (+10pp) |
| Topic continuation | Lowest (+5pp) |

---

## Memory Architecture Variants Tested

| Memory Type | Mechanism | Accuracy vs. Long-Context |
|-------------|-----------|--------------------------|
| Summarization memory | LLM-generated summaries | −33.4pp |
| Vector retrieval memory | Embedding-based retrieval | −28.7pp |
| Key-value memory | Structured fact extraction | −31.2pp |
| Hierarchical memory | Multi-level summaries | −29.8pp |
| **Long-context (baseline)** | Full history | **0pp** |

No memory architecture approaches long-context accuracy. Vector retrieval memory is the best-performing alternative but still 28.7pp below.

---

## Lost in the Middle Effect

At very long contexts (200K+ tokens), long-context models suffer from the "Lost in the Middle" phenomenon (Liu et al. 2023, arxiv 2307.03172):

- Information in the middle of a very long context is underweighted
- Performance on facts from the middle 40% of context drops significantly
- This partially erodes long-context's advantage at extreme lengths (200K+)

**Practical implication**: Long-context advantage is most reliable in the 10K–100K range. Above 100K, consider hierarchical approaches (retrieval for older context + full context for recent turns).

---

## Recommendations from the Paper

### Decision Framework

```
Conversation length?
  ≤ 10 turns → Long-context (better accuracy, comparable cost)
  11-30 turns, accuracy-critical → Long-context (better accuracy, higher cost)
  11-30 turns, cost-constrained → Memory (26% cheaper, 25-35pp accuracy cost)
  30+ turns, cost-constrained → Memory (40%+ cheaper, accept accuracy trade-off)
  200K+ tokens → Hybrid (memory for oldest turns, full context for recent 50K)
```

### For Coding Agents Specifically

Coding agents have high task-type sensitivity (facts, reasoning chains, constraints) — use long-context preferentially. Memory compression causes bugs from forgotten constraints.

---

## Workspace Relevance

Directly informs workspace context management strategy:

1. **Break-even at ~10 turns**: The workspace's compact triggers (70% context use, per `context-management.md`) align with this finding. Compacting before 10 turns (at 40-70% context) preserves accuracy while controlling costs.
2. **26% cheaper at 20 turns with memory**: `MEMORY.md` dual-layer approach (session summary + Git-tracked decisions) implements the memory strategy for the post-session case — not mid-session, where accuracy matters most.
3. **35:1 compression loses nuanced constraints**: When `/compact` is run, nuanced constraints (security rules, per-project conventions) should be explicitly preserved in the compact hint — they're exactly what 35:1 compression drops.
4. **−33.4pp accuracy for summarization memory**: The `/compact <hint>` approach with explicit preservation of key constraints is better than generic summarization — consistent with `context-management.md` instruction "保留原始任務目標與最近 5 個工具結果."
5. **Lost in the Middle at 200K+**: Claude Opus 4.7's documented long-context regression at 256K+ tokens (per its system card) aligns with this paper's findings — the accuracy degradation at extreme context lengths is a general phenomenon, not Opus-specific.
6. **Vector retrieval memory −28.7pp**: The `autoresearch` loop using memory (`MEMORY.md`) will degrade accuracy compared to keeping context in window — for high-stakes research tasks, prefer a fresh session with explicit context loading over relying on cross-session memory.

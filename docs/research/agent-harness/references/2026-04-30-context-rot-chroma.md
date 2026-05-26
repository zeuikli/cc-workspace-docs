---
title: "Context Rot: How Increasing Input Tokens Impacts LLM Performance"
source: "https://www.trychroma.com/research/context-rot"
author: "Chroma Research"
date: "2026-04-30"
tags: [agent-harness, research]
---

# Context Rot: How Increasing Input Tokens Impacts LLM Performance

## Core Discovery

The report reveals that **LLMs do not process context uniformly**. Despite claims of handling long contexts reliably, models exhibit "increasingly unreliable" performance as input length grows, even on simple tasks.

## Primary Quantified Metrics

**Performance Degradation Patterns:**
- Models show non-uniform performance decay across different input lengths
- Lower needle-question similarity accelerates performance decline
- Even single distractors measurably reduce accuracy compared to baseline

**Model-Specific Behaviors:**
- Claude models demonstrate conservative responses under ambiguity, often abstaining when uncertain
- GPT models show highest hallucination rates when distractors present
- Gemini and Qwen models generate spurious content at extended lengths (500+ words)

## NIAH Benchmark Extensions

The researchers tested beyond traditional lexical-matching NIAH by examining:

### 1. Semantic Similarity
Needle-question pairs ranging from 0.445-0.829 cosine similarity showed faster degradation at lower similarity scores

### 2. Distractors Impact
Adding four topically-related distractors caused compounded performance drops, with individual distractors showing non-uniform impact

### 3. Structural Effects
Surprisingly, shuffled haystacks consistently outperformed logically coherent ones across all 18 models tested

### 4. LongMemEval Results
On conversational QA with 113k tokens, focused prompts (~300 tokens) substantially outperformed full prompts, with Claude Opus 4 showing the largest gap

## Repeated Words Task

Models failed to accurately replicate simple repeated-word sequences beyond 2,500 tokens, with position-accuracy declining as length increased and random word generation appearing at extended lengths.

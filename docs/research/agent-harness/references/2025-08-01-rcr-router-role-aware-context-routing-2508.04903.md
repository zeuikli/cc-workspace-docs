---
title: "RCR-Router: Role-Aware Context Routing for Multi-Agent Systems"
arxiv_id: 2508.04903
authors: Research team
published: 2025-08-01
source: "https://arxiv.org/abs/2508.04903"
venue: arXiv
---

# RCR-Router: Role-Aware Context Routing for Multi-Agent Systems

**Published**: August 1, 2025

**Source**: https://arxiv.org/abs/2508.04903

---

## Abstract

RCR-Router is a framework designed to improve efficiency in multi-agent large language model systems. The approach addresses a key limitation in existing systems: they typically rely on "static or full-context routing strategies, which lead to excessive token consumption." The system introduces dynamic memory selection based on agent roles and task stages while maintaining strict token budgets.

---

## Overview

This paper introduces RCR-Router, a framework that optimizes how multiple language model agents access shared memory during collaborative tasks. The system dynamically selects relevant information for each agent based on their assigned role and current task phase, while respecting strict token budgets.

---

## Key Innovation

The primary contribution addresses a critical limitation in existing multi-agent LLM systems: "excessive token consumption, redundant memory exposure, and limited adaptability across interaction rounds." Rather than giving all agents access to complete memory (full-context routing) or using fixed, static allocations, RCR-Router implements semantic-aware, role-conditioned memory filtering.

---

## Core Mechanism

The framework operates through three components:

1. **Token Budget Allocator**: Assigns maximum token limits to each agent based on role requirements
2. **Importance Scorer**: Ranks memory items by relevance using role-specific keywords, task stage priority, and recency signals
3. **Semantic Filter**: Greedily selects the highest-scoring items until token budgets are exhausted

The system continuously updates shared memory with agent outputs, enabling iterative refinement across multiple reasoning rounds.

---

## Performance Results

Testing across three question-answering benchmarks (HotPotQA, MuSiQue, 2WikiMultihop) demonstrates that RCR-Router achieves:

- **25-47% token reduction** compared to full-context approaches
- **Improved answer quality scores** while consuming fewer resources
- **Faster runtime** with lower computational overhead

Ablation studies confirm that performance saturates around 3-4 iterations, and diminishing returns appear with token budgets above 2,048 tokens per agent.

---

## Evaluation Methodology

The researchers introduced an Answer Quality Score metric that evaluates LLM-generated explanations beyond standard accuracy metrics, providing more nuanced assessment of model behavior.

---

## Theoretical Grounding

The authors prove that optimal context selection is NP-hard (equivalent to the 0/1 Knapsack problem), justifying their greedy heuristic approach. They also establish that iterative feedback loops monotonically improve expected context quality over interaction rounds.

---

## Technical Approach

The framework combines lightweight scoring policies for memory selection with structured memory storage to support adaptive multi-agent collaboration across interaction rounds.

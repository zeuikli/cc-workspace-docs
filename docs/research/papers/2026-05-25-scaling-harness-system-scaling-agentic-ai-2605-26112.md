---
url: "https://arxiv.org/abs/2605.26112"
title: "From Model Scaling to System Scaling: Scaling the Harness in Agentic AI"
archived_date: 2026-07-09
arxiv_id: 2605.26112
authors: ["Shangding Gu"]
domains: [cs.AI, cs.LG]
license: arXiv non-exclusive
pdf_path: pdfs/2605.26112.pdf
published_date: 2026-05-25
tags: [harness-scaling, system-scaling, dynamic-skill-routing, context-governance, trustworthy-memory, agent-harness, cheetahclaws]
---

# From Model Scaling to System Scaling: Scaling the Harness in Agentic AI

**arXiv**: https://arxiv.org/abs/2605.26112  
**Code**: https://github.com/SafeRL-Lab/cheetahclaws  
**PDF**: pdfs/2605.26112.pdf

---

## 中文說明（workspace 意涵）

本論文提出「system scaling」概念: agentic AI 的下一個瓶頸不是模型規模,而是 harness（結構化執行層）的設計品質。作者定義 agent harness = 基礎模型 + 記憶基質 + context 建構器 + skill-routing 層 + 編排迴圈 + 驗證治理層的組合體,並提出三個核心瓶頸: context governance、trustworthy memory、dynamic skill routing。

**對 Fusion 架構的直接意義**: 論文 §4.3 "Dynamic Skill Routing and Verification" 正是 Devin Fusion sidekick 路由和 workspace multi-mode-skill 路由的學術框架化。作者主張「skill routing across tools and subagents」是 harness-level 的 first-class 設計對象,非模型層的附屬品。這為本 workspace 的 Fusion 架構提供了學術 ground truth: 路由策略不是「選模型」的優化,而是「scaling the harness」的系統級設計。

**與 workspace 既有研究的對齊**: 論文的「harness-level benchmarks」議程（trajectory quality、memory hygiene、context efficiency、verification cost）與 workspace DeepSWE 實證（harness quality = 評測第一獨立變數,同模型跨 harness 差 23.8pt）完全一致。CheetahClaws 參考實現與 Claude Code 的對比分析,可作為 workspace 跨 harness 可攜性（Omnigent）研究的補充參考。

---

## Abstract

This paper studies the next major bottleneck in agentic AI as *system scaling*, not only model scaling: the design of auditable, persistent, modular, and verifiable architectures around foundation models. We refer to this shift as *scaling the harness*: treating the structured execution layer around a foundation model as a first-class object of design, evaluation, and optimization. Recent progress in large language models (LLMs) has enabled agents that use tools, retrieve information, maintain memory, and execute long-horizon workflows. Yet evaluation remains largely model-centric, reducing agents to final-task success or benchmark accuracy while treating memory, retrieval, tool use, orchestration, verification, and governance as secondary implementation details. This framing is increasingly inadequate: agent performance emerges from the interaction among the foundation model, memory substrate, context constructor, skill-routing layer for tools and subagents, orchestration loop, and verification-and-governance layer. Together, these components form the agent harness, the system that translates model capability into long-horizon agent behavior. We therefore study *scaling the harness* through three core bottlenecks in agentic AI: *context governance*, *trustworthy memory*, and *dynamic skill routing*, together with the orchestration and governance mechanisms that coordinate and constrain them. We further outline a research agenda for harness-level benchmarks that operationalize system scaling, going beyond one-shot task success to measure trajectory quality, memory hygiene, context efficiency, communication fidelity, verification cost, and safe evolution over time. Alongside the framework, we develop and release `CheetahClaws`, a Python-native reference harness, and use it together with Claude Code and OpenClaw as concrete points of comparison that make harness-level design choices explicit. Our main claim is that future progress in agentic AI will depend as much on system design as on stronger foundation models.

## 1 Introduction

The dominant story of recent AI progress has been *model scaling*: larger models, more data, stronger post-training, and higher benchmark scores. For agentic AI, this story is now incomplete. Once foundation models are embedded into tools, terminals, browsers, repositories, memory stores, and external services, their behavior is no longer determined by the model alone. It is determined by a *system*: how context is constructed, how memory is retrieved, how tools are invoked, how subagents are routed, how actions are verified, and how failures are audited.

Our key claim is therefore that **agentic AI should be studied and evaluated as a system-scaling problem, not merely as a model-scaling problem.** By *model scaling*, we refer to improvements in the standalone foundation model. By *system scaling*, we refer to improvements in the surrounding architecture, including memory, context construction, skill routing across tools and subagents, orchestration, and verification-and-governance, and how these components adapt over time.

Modern agentic systems already illustrate what scaling the harness looks like in practice. Production harnesses such as Claude Code and OpenClaw couple foundation models to tools, subagents, and persistent project memory. Research-side harnesses such as SWE-agent further show that careful tool-schema design alone can improve benchmark accuracy substantially even with a fixed backbone model.

This perspective is highlighted by recent empirical findings: what is often reported as a model score is in fact a **model-plus-harness score**. Context length does not guarantee effective information access because attention dilutes over long inputs. Multi-agent systems can outperform single agents on breadth-first tasks but introduce coordination failures that single-agent metrics miss.

### Three Main Contributions

1. **System-scaling framing.** Progress depends on *scaling the harness*, not only scaling the model.
2. **Harness-level framework.** Separates base-model reasoning from system factors including memory, context construction, skill routing, orchestration, and verification-and-governance.
3. **Evaluation agenda and reference harness.** Future benchmarks should measure process-level and longitudinal properties such as trajectory quality, memory hygiene, context efficiency, verification cost, safe evolution, and robustness under repeated use. `CheetahClaws` is developed as a Python-native reference harness, compared against Claude Code and OpenClaw.

## 3 System Scaling: A Framework for Agentic AI

### 3.1 Agent Harnesses as System Infrastructure

The agent harness is the structured execution layer that translates model capability into long-horizon agent behavior. It comprises six core components:

1. **Foundation model**: The base LLM providing reasoning and generation
2. **Memory substrate**: Persistent storage for facts, decisions, and trajectories
3. **Context constructor**: Assembles prompts from memory, tools, and current state
4. **Skill-routing layer**: Routes tasks to appropriate tools, subagents, or models
5. **Orchestration loop**: Manages the agent's think-act-observe cycle
6. **Verification-and-governance layer**: Validates outputs and enforces safety constraints

### 3.2 Prompt, Skill, and Memory as Temporal Layers

The harness manages three temporal layers of information:
- **Prompt** (immediate): Current user request and system instructions
- **Skill** (medium-term): Reusable procedures and tool-use patterns
- **Memory** (long-term): Persistent knowledge accumulated across sessions

## 4 Three Bottlenecks in System Scaling

### 4.1 Context Governance

Context governance addresses what should be retrieved, compressed, ordered, refreshed, trusted, and kept active at each step. Key challenges include:
- Attention dilution over long inputs (lost-in-the-middle effect)
- Context window management vs. effective information access
- Dynamic context construction based on task demands

### 4.2 Trustworthy Memory

Memory quality involves:
- What to store and what to discard
- How to retrieve the right information at the right time
- Avoiding staleness, drift, contamination, and over-generalization
- Memory as a first-class data management system, not just a storage layer

### 4.3 Dynamic Skill Routing and Verification

**中文說明**: 本節是 Fusion 架構的學術對應。Skill routing 不只是「選哪個模型」,而是跨工具、跨 subagent、跨模型的動態分配,且需驗證路由決策本身是否正確。

Dynamic skill routing determines how tasks are dispatched across tools, subagents, and potentially different models. Key challenges:
- Routing decisions must consider task complexity, model capability, and cost
- Verification of routing decisions: was the right agent/model selected?
- Fallback mechanisms when initial routing proves inadequate
- Cost-quality tradeoffs in routing decisions

This directly corresponds to the "sidekick" pattern in production systems (e.g., Devin Fusion), where a frontier model delegates mechanical work to a cost-effective model while maintaining planning and review ownership.

## 5 Toward System-Level Evaluation and Agent Evolution

### 5.1 From Outcome Metrics to Process Metrics

Future benchmarks should measure:
- **Trajectory quality**: Are the intermediate steps efficient and correct?
- **Memory hygiene**: Is memory accurate, non-redundant, and non-stale?
- **Context efficiency**: Is the context window used effectively?
- **Communication fidelity**: In multi-agent systems, is information accurately transmitted?
- **Verification cost**: How much overhead does verification add?

### 5.2 From Single Episodes to Longitudinal Evaluation

Pass^k evaluation (probability of succeeding on k independent rollouts) exposes reliability gaps that single-shot accuracy hides. Longitudinal evaluation tracks:
- Skill drift over time
- Memory staleness
- Adaptation quality

### 5.3 Standards for Safe Agent Evolution

Agent evolution requires standards for:
- How agents update skills
- How agents refine memory
- How agents communicate across roles
- How agents remain auditable as they adapt

## 6 Discussion: Alternative Views and Limitations

The system-scaling framing does not claim model scaling no longer matters. Rather, once models reach a sufficient capability threshold, many additional gains in long-horizon agent performance increasingly depend on system design. The framework is also limited by the immaturity of harness-level benchmarks — most existing benchmarks remain model-centric.

## 7 Conclusion

Future progress in agentic AI will depend as much on system design as on stronger foundation models. The agent harness — encompassing memory, context, skill routing, orchestration, and verification — should be treated as a first-class object of design, evaluation, and optimization. The release of `CheetahClaws` provides a concrete reference point for harness-level design choices, and the proposed evaluation agenda offers a path toward benchmarks that measure what actually matters for long-horizon agent performance.

---

> **PDF**: `pdfs/2605.26112.pdf` (419 KB, 11 pages)  
> **Figures**: `pdfs/figures/2605.26112/` (9 PNG images)  
> **Code**: https://github.com/SafeRL-Lab/cheetahclaws  

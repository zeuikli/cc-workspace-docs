---
url: "https://moonsat.medium.com/thin-harness-fat-skills-a3dd6d2fe2af"
title: "Thin Harness, Fat Skills — Steve Yegge's Framework"
author: "Moonsat"
date: 2026-04-13
status: SUCCESS
---

# Thin Harness, Fat Skills

## Core Thesis

The author argues that dramatic productivity gains in AI coding (described as "10x to 100x" improvement) stem not from model intelligence but from system architecture. The key principle is "thin harness, fat skills"—minimizing the wrapper around AI while maximizing structured procedural knowledge.

## Five Foundational Concepts

### Skill Files

Reusable markdown documents encoding processes rather than prescribing actions. They function like methods with parameters, applying the same procedure across different contexts. The same investigation skill produces medical analysis or forensic research depending on the dataset and query provided.

### The Harness

A minimal program (approximately 200 lines) that loops through model execution, manages file I/O, handles context, and enforces safety boundaries. The anti-pattern involves bloated tool definitions consuming excessive tokens and introducing latency through MCP round-trips.

### Resolvers

Context routing systems that load relevant documents based on task type. Rather than maintaining enormous reference files, resolvers dynamically surface appropriate guidance. The author reduced a 20,000-line knowledge document to 200 lines of pointers.

### Latent vs. Deterministic Work

Intelligence (reading, judgment, synthesis) belongs in latent space where models excel. Optimization problems, arithmetic, and SQL queries belong in deterministic layers for reliability. Misalignment causes hallucinations and failures.

### Diarization

Synthesizing structured profiles from multiple documents—the gap between what founders claim and what they're building, extracted through holistic reading rather than database queries or RAG systems.

## Three-Layer Architecture

The system stacks as:
- **Top:** Fat skills encoding domain judgment
- **Middle:** Thin CLI harness for orchestration  
- **Bottom:** Deterministic application layer

This directional principle ensures model improvements automatically elevate all skills while maintaining reliability.

## Real-World Example: Startup School Matching

The article demonstrates the framework through a system managing 6,000 founder applications:

- **Enrichment phase:** Skills aggregate GitHub commits, advisor transcripts, and applications to identify patterns humans miss—distinguishing founders claiming similar domains but solving different problems.

- **Matching strategies:** The same skill invoked three ways produces different clustering logic, each incorporating human judgment about sector relationships and serendipity.

- **Learning loop:** Post-event surveys identify marginal experiences, which get codified into updated matching rules within skill files, improving future iterations without code rewrites.

## Key Insight on Permanence

Skills represent permanent system upgrades that compound over time. Once codified, they:
- Never degrade
- Improve automatically with new model versions
- Run on schedules without human intervention
- Scale from initial manual instances to automated processes

The author emphasizes the discipline of refusing one-off work: manually perform a task 3-10 times, approve the pattern, then codify it into a skill.

---

**Core Message:** Superhuman AI productivity emerges from rigorous architectural choices about what stays thin (the harness) and what stays fat (reusable procedural knowledge), not from raw model capability.

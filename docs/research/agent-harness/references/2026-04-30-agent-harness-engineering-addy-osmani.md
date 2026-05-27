---
title: "Agent Harness Engineering"
author: "Addy Osmani"
date: 2026-04-30
source: "https://addyosmani.com/blog/agent-harness-engineering/"
tags: [agent-harness, research]
---

# Agent Harness Engineering

## Central Thesis

"A decent model with a great harness beats a great model with a bad harness." The article argues that AI agent capability emerges primarily from the scaffolding surrounding the model, not the model itself.

## Key Definition

**Agent Harness** = Model + all surrounding infrastructure

The harness encompasses: system prompts, tools, execution sandboxes, feedback loops, hooks, memory systems, and observability—everything except the model weights.

## Core Equation

```
coding agent = AI model(s) + harness
```

## Essential Components

**Filesystem & Git**: Durable state and versioning foundation

**Bash & Code Execution**: General-purpose tool capability

**Sandboxes**: Safe, isolated execution environments

**Memory Systems**: Continual learning via `AGENTS.md` and context injection

**Context Management**: Compaction, tool offloading, skill disclosure

**Long-Horizon Execution**: Ralph Loops, planning, verification cycles

**Hooks**: Enforcement layer (typecheck, linting, destructive-action blocks)

## Notable Quote

"Every line in a good `AGENTS.md` should be traceable back to a specific thing that went wrong."

## The "Ratchet" Principle

Convert each agent failure into permanent rules—the harness tightens with every mistake.

## Critical Data Point

Claude Opus 4.6 in Claude Code scores lower than the same model in custom harnesses optimized for specific tasks (Top 30 → Top 5 on Terminal Bench 2.0 by harness changes alone).

## Architecture Pattern

Harnesses now follow convergent design: input layers, knowledge layers, integration with MCPs, execution dispatch, output verification, and multi-agent orchestration.

---
title: "Skill Issue: Harness Engineering for Coding Agents"
source: "https://www.humanlayer.dev/blog/skill-issue-harness-engineering-for-coding-agents"
author: "Human Layer"
date: "2026-04-30"
tags: [agent-harness, research]
---

# Skill Issue: Harness Engineering for Coding Agents

## Core Thesis

Rather than waiting for superior AI models to solve coding agent failures, teams should focus on **harness engineering**—optimizing the configuration and runtime environment surrounding the model to dramatically improve performance and reliability.

## Key Definition

**Harness Engineering**: The practice of systematically addressing agent mistakes through deliberate configuration adjustments. As Mitchell Hashimoto framed it, it means taking "time to engineer a solution such that the agent never makes that mistake again."

The article presents harness engineering as a subset of context engineering, addressing:
- Capability expansion
- Codebase-specific knowledge injection
- Deterministic behavior beyond prompts
- Task success rate improvement
- Context window efficiency

## Primary Configuration Levers

### 1. **CLAUDE.md/AGENTS.md Files**

Markdown files injected deterministically into system prompts. Keep them under 60 lines, concise, universally applicable, and avoid auto-generation.

### 2. **MCP Servers**

Primary purpose: extending capabilities with tools. Cautions include:
- Tool descriptions consume context budget
- Limit to actively-used servers
- Prefer CLI tools when models already understand them
- Never connect to untrusted servers (prompt injection risk)

### 3. **Skills**

Enable **progressive disclosure**—agents access knowledge only when needed. Bundle related instructions, knowledge files, and tools within skill directories for selective activation.

### 4. **Sub-Agents**

Provide **context firewall functionality**:
- Isolate discrete tasks in separate context windows
- Prevent intermediate noise accumulation
- Maintain coherency across many sessions
- Support cost optimization (cheaper models for simpler sub-tasks)

Research validates this: Chroma's context rot studies show performance degrades at longer context lengths, especially when low semantic similarity exists between questions and context.

### 5. **Hooks**

Automated scripts triggered at lifecycle events:
- Run silently on success
- Surface only errors/actionable feedback
- Control permissions and integrations
- Verify work (typechecks, builds)

## Architecture Insight: Context Firewall

Sub-agents function as isolated context environments, preventing intermediate tool calls and results from polluting parent sessions. This enables longer problem-solving sequences without degradation.

```
Parent Agent (orchestration) → Sub-Agent 1 (research) → Condensed result
                             → Sub-Agent 2 (implementation) → Condensed result
```

## Back-Pressure Mechanisms

Verification systems enable self-checking:
- Typechecks and builds
- Unit/integration tests
- Code coverage
- UI interaction testing

**Critical**: Keep verification output context-efficient—surface only errors, silence on success.

## Notable Quote

"It's not a model problem. It's a **configuration problem.**"

## Practical Approach

- **Start simple**, add configuration only when failures occur
- Optimize iteration speed over single-attempt success
- Distribute battle-tested configs team-wide
- Test ruthlessly and discard ineffective optimizations

## What Didn't Work

- Pre-designing ideal configurations
- Installing numerous unused tools
- Running full test suites per session
- Micro-optimizing tool access across sub-agents

This represents a paradigm shift: agent performance bottlenecks exist primarily in orchestration and context management, not raw model capability.

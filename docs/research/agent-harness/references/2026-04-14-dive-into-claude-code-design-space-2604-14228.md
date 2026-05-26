---
title: "Dive into Claude Code: The Design Space of Today's and Future AI Agent Systems"
authors: "Jiacheng Liu, Xiaohan Zhao, Xinyi Shang, Zhiqiang Shen"
published: "2026-04-14"
source: "https://arxiv.org/abs/2604.14228"
---

# Dive into Claude Code: The Design Space of Today's and Future AI Agent Systems

**Authors**: Jiacheng Liu, Xiaohan Zhao, Xinyi Shang, Zhiqiang Shen
**Published**: April 14, 2026
**Source**: https://arxiv.org/abs/2604.14228
**arXiv ID**: 2604.14228
**Categories**: cs.SE, cs.AI, cs.HC

---

## Abstract

Comprehensive architectural analysis of Claude Code, Anthropic's agentic coding tool, by examining publicly available TypeScript source code. Rather than merely describing features, the authors trace design decisions from underlying human values through specific implementation choices. Maps 98.4% of production codebase as operational infrastructure, only 1.6% as AI logic. Compares with OpenClaw and outlines six design directions for future systems.

---

## Five Foundational Values

The architecture reflects five core commitments:

1. **Human Decision Authority** — Users retain ultimate control through informed observation, approval/rejection capabilities, and auditable records
2. **Safety, Security, and Privacy** — Protection mechanisms operate independently of user vigilance, addressing overeager behavior and prompt injection
3. **Reliable Execution** — Multi-turn coherence with environmental feedback at each step
4. **Capability Amplification** — Enabling qualitatively new workflows (approximately 27% of tasks wouldn't be attempted otherwise)
5. **Contextual Adaptability** — Configuration at multiple levels with trust trajectories improving over time

---

## Architectural Components

Seven functional elements:

- User interfaces (CLI, IDE, SDK)
- Shared agent loop
- Permission system
- Tool pool
- State and persistence mechanisms
- Execution environment

### Five-Layer Subsystem Structure

**Surface layer**: Multiple entry points (CLI, IDE, SDK) converging on identical logic

**Core layer**: Simple reactive loop with five-stage context management pipeline

**Safety/action layer**: Deny-first permission evaluation, ML-based classifier, hooks, tools, sandboxing, subagent spawning

**State layer**: CLAUDE.md hierarchy, append-only transcripts, memory mechanisms

**Backend layer**: Shell execution, filesystem operations, MCP connections, tool implementations

---

## The 98.4% Infrastructure Ratio

Claude Code v2.1.88 codebase decomposition:

- **98.4% = operational infrastructure**: context management, tool routing, error recovery, session management
- **1.6% = AI reasoning logic**: actual model calls

> "98.4% of Claude Code's production codebase is operational infrastructure—context management, routing, and recovery—while only 1.6% is AI reasoning logic."

This ratio validates that harness engineering, not prompt engineering or model selection, is the primary determinant of agent system quality.

---

## Key Design Decisions

### Permission Architecture

Seven independent safety layers operating in parallel:

1. Pre-filtering (deny-list patterns)
2. Deny-first rules (explicit block rules)
3. Permission modes (plan/auto/bypassPermissions)
4. ML classifier (behavioral evaluation)
5. Shell sandboxing (execution isolation)
6. Non-restoration on resume (audit continuity)
7. Hooks (programmatic interception)

Any single layer can block execution. The system implements graduated autonomy:
- **plan**: user approves plans first
- **auto**: ML evaluation
- **bypassPermissions**: minimal prompting

### Context Management Pipeline

The binding resource constraint is the context window. Five sequential shapers manage pressure before each model call:

| Stage | Mechanism | Trigger |
|-------|-----------|---------|
| 1 | Budget reduction | Caps individual tool outputs |
| 2 | Snip | Removes older history |
| 3 | Microcompact | Fine-grained compression |
| 4 | Context collapse | Read-time projections |
| 5 | Auto-compact | Semantic summarization (last resort) |

### Extensibility Mechanisms

Four complementary mechanisms at different context costs:

| Mechanism | Cost | Use Case |
|-----------|------|----------|
| MCP servers | Medium | External tool integration |
| Plugins | Medium | Reusable component packages |
| Skills | Low | Domain-specific instruction injection |
| Hooks | Zero runtime | Execution lifecycle interception (27 event types) |

### Subagent Delegation

Subagents operate in isolated context windows with separate transcripts (sidechains). Return only summaries to parents rather than full conversation histories. Permission escalation flows through "bubble" mode.

---

## Thirteen Design Principles

Recurring principles operationalizing the five values:

1. Deny-first with human escalation
2. Graduated trust spectrum reflecting relationship evolution
3. Defense in depth via layered mechanisms
4. Externalized programmable policy
5. Context as scarce resource with progressive management
6. Append-only durable state (auditable history)
7. Minimal scaffolding, maximal operational harness
8. Values over rules (contextual judgment within deterministic guardrails)
9. Composable multi-mechanism extensibility
10. Reversibility-weighted risk assessment
11. Transparent file-based configuration
12. Isolated subagent boundaries
13. Graceful recovery and resilience

---

## Claude Code vs OpenClaw Comparison

Six comparative dimensions:

| Dimension | Claude Code | OpenClaw |
|-----------|-------------|---------|
| Deployment model | Closed-source, optimized harness | Open-source, portable |
| Trust architecture | Per-action evaluation | Perimeter-level access control |
| Agent runtime | CLI reactive loop | Embedded in gateway control plane |
| Extension mechanisms | MCP + Plugins + Skills + Hooks | Modular plugin system |
| Memory management | Prefix caching + auto-compact | Manual management |
| Multi-agent routing | Subagent sidechains | Gateway-level routing |

Same design questions yield different answers under different contexts. Neither is universally superior.

---

## Six Future Design Directions

1. **Observability-evaluation gap**: Silent failures where safety mechanisms work but produce undetected suboptimal results
2. **Cross-session persistence**: Longitudinal colleague relationships and accumulated learning
3. **Harness boundary evolution**: Expanding where, when, and with whom agents act
4. **Horizon scaling**: From single sessions to sustained scientific programs
5. **Governance at scale**: Oversight mechanisms for high-autonomy deployments
6. **Long-term capability preservation**: Tension between short-term amplification and sustained human understanding

---

## Running Example Traced Through System

The paper traces "Fix the failing test in auth.test.ts" through all major subsystems:

```
User input → Surface layer (CLI)
    → Core layer (reactive loop, context pipeline)
        → Safety/action layer (permission check, ML classifier)
            → Tool execution (bash, read, edit)
                → State layer (transcript append, memory update)
                    → Backend layer (filesystem ops)
                        → Model call (1.6% of system)
                            → Response rendering
```

---

## Long-Term Human Capability Concern

The paper identifies an open tension: while the architecture substantially amplifies short-term programmer productivity, it offers limited explicit mechanisms supporting long-term human improvement, codebase coherence, or developer pipeline sustainability.

Empirical research documenting skill atrophy under AI assistance frames a critical question for future agent system design. This is identified as the most significant unresolved design challenge.

---

## Workspace Alignment Analysis

| Paper Claim | cc-workspace | Gap |
|-------------|--------------|-----|
| 98.4% infrastructure ratio | `.claude/` directory complexity >> AI logic | ✅ |
| Human Decision Authority | PreToolUse hooks + CLAUDE.md production red lines | ✅ |
| Contextual Adaptability | CLAUDE.md three-layer loading strategy | ✅ |
| Deny-first architecture | `settings.json` permission modes | ✅ |
| Long-horizon state management | `schemas/progress.schema.json` | ⚠️ Partial |
| Evaluation-integrated development | `/deep-review` + healthcheck.sh (manual trigger) | ⚠️ Partial |
| Cross-session persistence | Auto Memory (flat accumulation, no consolidation) | ⚠️ Partial |

Integration targets: `ANTHROPIC-ALIGNMENT.md` §一 核心主張 + `HARNESS-CARD.md`

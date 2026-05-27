---
title: "Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering"
authors: "Chenyu Zhou, Huacan Chai, Wenteng Chen, et al. (20 authors)"
published: 2026-04-09
source: "https://arxiv.org/abs/2604.08224"
---

# Externalization in LLM Agents: A Unified Review of Memory, Skills, Protocols and Harness Engineering

**Authors**: Chenyu Zhou, Huacan Chai, Wenteng Chen, et al. (20 authors)
**Published**: April 9, 2026
**Source**: https://arxiv.org/abs/2604.08224
**arXiv ID**: 2604.08224
**Categories**: cs.AI, cs.LG, cs.MA

---

## Core Thesis

The paper argues that LLM agent progress increasingly depends on **externalization**—relocating cognitive burdens from model parameters into persistent external infrastructure (memory, skills, protocols, harness). This mirrors human cognitive history: just as writing transformed recall into recognition, agent infrastructure transforms hard internal tasks into forms models handle more reliably.

> "Infrastructure matters because it transforms hard cognitive burdens into forms the model can solve more reliably."

---

## Memory: Externalizing State Across Time

Memory externalizes state across time through four components:

- **Working context**: Active session information within the context window
- **Episodic experience**: Records of past interactions and their outcomes
- **Semantic knowledge**: Structured factual and procedural knowledge bases
- **Personalized memory**: User-specific preferences and behavioral patterns

Architecture evolution trajectory:

```
Monolithic context
    → Retrieval stores (RAG, vector DBs)
        → Hierarchical systems (tiered by recency/importance)
            → Adaptive architectures (dynamic load/evict based on task)
```

Key tensions:
- **Recency vs relevance**: Recent information is not always most relevant; retrieval strategies must balance both
- **Compression fidelity**: Summarization loses nuance; raw storage is token-expensive
- **Cross-session continuity**: Episodic memory degrades without active consolidation mechanisms (see Memory Survey 2603.07670: removing reflection → 48h behavioral degradation)

---

## Skills: Externalizing Procedural Expertise

Skills externalize procedural expertise through specification, discovery, and composition. Four development stages:

1. **Atomic execution primitives**: Single-action tools (bash, read, write)
2. **Packaged expertise**: Multi-step workflows authored as skills (SKILL.md pattern)
3. **Distilled capability**: Skills learned from successful trajectories
4. **Composed ensembles**: Skills that invoke other skills hierarchically

Skill governance gap identified: most systems have skill creation mechanisms but lack lifecycle management for deprecated or contradictory skills.

Protocol for skill quality: skill descriptions must be precise enough to distinguish them from adjacent skills; ambiguous descriptions cause selection errors under tool competition.

---

## Protocols: Externalizing Interaction Structure

Protocols externalize interaction structure through machine-readable contracts:

- **Agent-tool protocols**: JSON Schema tool calling (OpenAI FC, Anthropic Tool Use), MCP
- **Agent-agent protocols**: A2A (Google), structured handoff formats
- **Agent-user protocols**: Permission prompts, approval flows, audit trails

Protocol standardization pressure: MCP vs A2A competitive dynamics, but open standards enable cross-harness portability that proprietary protocols cannot.

Critical insight: poorly specified protocols are as damaging as no protocols—ambiguous tool schemas produce the same accuracy collapse as missing tools (see TSCG paper 2605.04107 for empirical evidence: Phi-4 14B drops to 0% on malformed schemas).

---

## Harness Engineering: The Unification Layer

Harness is the runtime layer that unifies Memory, Skills, and Protocols:

### Five Harness Functions

| Function | Description | Example |
|----------|-------------|---------|
| **Orchestration** | Coordinates agent subcomponents and tool dispatch | subagent-strategy.md dispatch table |
| **Sandboxing** | Isolates execution from environment damage | Docker integration, path restrictions |
| **Observability** | Tracks component performance and execution traces | healthcheck.sh, session retros |
| **Governance** | Enforces permission policies and safety constraints | PreToolUse hooks, CLAUDE.md rules |
| **Context Budget Management** | Controls token allocation across the window | compact triggers, tool output limits |

### 98.4% Infrastructure Ratio

Empirical analysis of Claude Code v2.1.88 (cross-referenced with 2604.14228):
- **98.4%** of production codebase = operational infrastructure (context management, routing, recovery)
- **1.6%** = AI reasoning logic (actual model calls)
- Implication: harness engineering quality determines agent success more than model capability selection

### Context Engineering vs Prompt Engineering

> "Context Engineering = filling the context window with just the right information for the next step" (Karpathy 2025)

The paper frames Context Engineering as the operationalization of externalization—deciding which external components (memory, skills, protocol schemas) to load at which moment. This is system architecture, not prompt crafting.

---

## Parametric vs External Capability Tradeoff

| Dimension | Parametric (in-weights) | External (in-harness) |
|-----------|------------------------|----------------------|
| **Access cost** | Zero (always available) | Token budget |
| **Update cost** | Fine-tuning (expensive) | File edit (cheap) |
| **Specificity** | General | Task-specific |
| **Governance** | Opaque | Auditable |
| **Failure mode** | Hallucination | Loading error |

Key finding: for domain-specific tasks, external capability consistently outperforms equivalent parametric capability. A well-designed harness enables Haiku-class models to reach Sonnet-class quality on structured tasks.

---

## Governance Challenges

Three governance challenges identified across all four dimensions:

1. **Ownership ambiguity**: In multi-tenant environments, "who owns externalized knowledge?" is a security question, not just an organizational one
2. **Skill lifecycle management**: Most systems create skills but lack deprecation, versioning, or conflict resolution
3. **Protocol lock-in**: Early protocol adoption creates migration debt; open standards reduce but don't eliminate this

---

## Four-Dimension Unified Framework

```
                    ┌─────────────────────────────────┐
                    │         HARNESS LAYER            │
                    │  (orchestration, sandbox, govern) │
                    └──────────────┬──────────────────┘
                                   │ unifies
           ┌───────────────────────┼───────────────────────┐
           ▼                       ▼                       ▼
    ┌─────────────┐       ┌─────────────────┐     ┌─────────────────┐
    │   MEMORY    │       │     SKILLS      │     │   PROTOCOLS     │
    │ (state/time)│       │  (procedural    │     │  (interaction   │
    │             │       │   expertise)    │     │   structure)    │
    └─────────────┘       └─────────────────┘     └─────────────────┘
```

---

## Workspace Alignment Analysis

| Framework Concept | cc-workspace Implementation | Alignment |
|-------------------|----------------------------|-----------|
| Memory externalization | `schemas/progress.schema.json` + Auto Memory | ✅ |
| Skills externalization | `.claude/skills/` + SKILL.md pattern | ✅ |
| Protocol externalization | MCP servers + `settings.json` permissions | ✅ |
| Harness as unification | `subagent-strategy.md` + harness-design rules | ✅ |
| Context budget management | compact triggers + tool output limits | ✅ |
| Skill lifecycle management | Missing deprecation/versioning mechanism | ⚠️ Gap |
| Observability (structured) | healthcheck.sh = static, not semantic trace | ⚠️ Gap |

---

## Key Citation

> "Infrastructure matters because it transforms hard cognitive burdens into forms the model can solve more reliably." (arXiv:2604.08224)

Integration targets: `research/agent-harness/FRAMEWORK.md` §理論基礎 + `ANTHROPIC-ALIGNMENT.md` §二映射表

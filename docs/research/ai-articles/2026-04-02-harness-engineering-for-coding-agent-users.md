---
url: "https://martinfowler.com/articles/harness-engineering.html"
title: "Harness Engineering for Coding Agent Users"
author: "Birgitta Böckeler"
archived: 2026-05-27
domain: martinfowler.com
published: 2026-04-02
tags: [harness-engineering, llm-agents, coding-agents, context-engineering, feedforward-feedback, maintainability, architecture]
word_count: 約 2500 字
---

# Harness Engineering for Coding Agent Users

> **來源**：[martinfowler.com](https://martinfowler.com/articles/harness-engineering.html)
> **作者**：Birgitta Böckeler（Distinguished Engineer, Thoughtworks）
> **發布日期**：2026-04-02
> **收錄日期**：2026-05-27

---

## Overview

本文提出一個信心建立框架：透過「harness engineering」讓 coding agent 在較少人工監督下運作。核心論點是：Agent = Model + Harness，而 user harness 的工程是 context engineering 的具體形式——人類的工作是不斷迭代 harness 以引導 agent。文章區分三類 regulation（maintainability、architecture fitness、behaviour），並誠實指出 behaviour harness 仍是最難解的開放問題。

---

## The Core Equation

The term **harness** has emerged as a shorthand to mean everything in an AI agent except the model itself — **Agent = Model + Harness**. In coding agents, part of the harness is already built in (e.g. system prompt, code retrieval mechanism, orchestration system). But coding agents also provide users with features to build an **outer harness** specifically for their use case.

A well-built outer harness serves two goals:
1. Increases the probability the agent gets it right in the first place
2. Provides a feedback loop that self-corrects as many issues as possible before they reach human eyes

This reduces review toil, increases system quality, and wastes fewer tokens.

---

## Feedforward and Feedback

To harness a coding agent we both anticipate unwanted outputs and prevent them, and put sensors in place to allow self-correction:

- **Guides (feedforward controls)** — anticipate the agent's behaviour and aim to steer it before it acts. Guides increase the probability of good results in the first attempt.
- **Sensors (feedback controls)** — observe after the agent acts and help it self-correct. Particularly powerful when they produce signals optimised for LLM consumption, e.g. custom linter messages that include self-correction instructions — a positive kind of prompt injection.

Without feedback: an agent that keeps repeating the same mistakes.
Without feedforward: an agent that encodes rules but never finds out whether they worked.

---

## Computational vs Inferential

| Type | Execution | Examples | Properties |
|------|-----------|----------|-----------|
| **Computational** | CPU (deterministic) | Tests, linters, type checkers, structural analysis | Milliseconds–seconds; results reliable |
| **Inferential** | GPU/NPU (non-deterministic) | AI code review, LLM as judge, semantic analysis | Slower, more expensive, non-deterministic but richer |

Examples table:

| Direction | Type | Example Implementations |
|-----------|------|------------------------|
| Coding conventions | feedforward / Inferential | AGENTS.md, Skills |
| Instructions to bootstrap a new project | feedforward / Both | Skill with instructions + bootstrap script |
| Code mods | feedforward / Computational | Tool with OpenRewrite recipes |
| Structural tests | feedback / Computational | Pre-commit hook running ArchUnit tests |
| Instructions how to review | feedback / Inferential | Skills |

---

## How Harness Engineering Relates to Context Engineering

Context engineering provides the means to make guides and sensors available to the agent. Engineering a user harness for a coding agent **is a specific form of context engineering**. The human's job is to steer the agent by iterating on the harness.

---

## The Steering Loop

Whenever an issue happens multiple times, feedforward and feedback controls should be improved to make it less probable — or prevent it entirely.

In the steering loop, AI can also help improve the harness itself. Coding agents make it cheaper to build:
- Custom controls and custom static analysis
- Structural tests
- Draft rules generated from observed patterns
- Custom linters scaffolded by agents
- How-to guides created from codebase archaeology

---

## Timing: Keep Quality Left

Controls should be distributed across the development lifecycle:

**Feedforward and feedback in the change lifecycle:**
- **Pre-commit / pre-integration:** Reasonably fast — linters, fast test suites, basic code review agent
- **Post-integration (pipeline):** More expensive — mutation testing, broader code review with bigger picture

**Continuous drift and health sensors:**
- **Continuous (outside change lifecycle):** Drift that accumulates gradually — dead code detection, test coverage quality analysis, dependency scanners
- **Runtime feedback:** Agents monitoring degrading SLOs, AI judges sampling response quality, log anomaly flagging

---

## Regulation Categories

The agent harness acts like a **cybernetic governor**, combining feedforward and feedback to regulate the codebase toward its desired state.

### Maintainability Harness

The easiest type — we have a lot of pre-existing tooling.

- **Computational sensors catch reliably:** Duplicate code, cyclomatic complexity, missing test coverage, architectural drift, style violations — cheap, proven, deterministic
- **LLMs partially address (expensively, probabilistically):** Semantically duplicate code, redundant tests, brute-force fixes, over-engineered solutions
- **Neither catches reliably:** Misdiagnosis of issues, overengineering, misunderstood instructions — correctness is outside any sensor's remit if the human didn't clearly specify

### Architecture Fitness Harness

Guides and sensors that define and check the architecture characteristics of the application — essentially **Fitness Functions**.

Examples:
- Skills that feed forward performance requirements + performance tests that feed back if improved/degraded
- Skills describing logging standards (observability conventions) + debugging instructions for the agent to reflect on log quality

### Behaviour Harness

The elephant in the room — functional correctness.

Current common approach:
- **Feedforward:** Functional specification (short prompt to multi-file descriptions)
- **Feedback:** Check if AI-generated test suite is green, has reasonably high coverage; some add mutation testing; combine with manual testing

Problem: This approach puts too much faith in AI-generated tests. Some teams use the **approved fixtures pattern** selectively where it fits, but it's not a wholesale answer to the test quality problem.

Overall: We still have a lot to figure out for good behaviour harnesses that reduce supervision and manual testing.

---

## Harnessability

Not every codebase is equally amenable to harnessing:
- Strongly typed language → type-checking as sensor
- Clearly definable module boundaries → architectural constraint rules
- Frameworks like Spring → abstract away details, implicitly increase agent success chances

**Greenfield vs legacy:**
- Greenfield teams can bake harnessability in from day one — technology decisions determine how governable the codebase will be
- Legacy teams with accumulated technical debt face the harder problem: the harness is most needed where it is hardest to build

### Ambient Affordances (Ned Letcher)

"Structural properties of the environment itself that make it legible, navigable, and tractable to agents operating within it."

---

## Harness Templates

Most enterprises have a few common service topologies that cover 80% of what they need (business API services, event processing, data dashboards). These might evolve into **harness templates**: a bundle of guides and sensors that leash a coding agent to the structure, conventions and tech stack of a topology.

Teams may start picking tech stacks and structures partly based on what harnesses are already available.

### Ashby's Law of Requisite Variety

A regulator must have at least as much variety as the system it governs, and can only regulate what it has a model of. An LLM coding agent can produce almost anything, but committing to a topology **narrows that space**, making a comprehensive harness more achievable. Defining topologies is a variety-reduction move.

---

## The Role of the Human

Human developers bring an **implicit harness** to every codebase:
- Absorbed conventions and good practices
- Felt cognitive pain of complexity
- Organisational alignment — awareness of technical debt tolerance, what "good" looks like in this specific context
- Human pace creates thinking space for experience to be triggered

A coding agent has none of this: no social accountability, no aesthetic disgust at a 300-line function, no intuition that "we don't do it that way here," no organisational memory.

Harnesses attempt to externalise what human developer experience brings, but can only go so far. **A good harness should not aim to fully eliminate human input, but to direct it to where input is most important.**

---

## Starting Point and Open Questions

Real-world harness examples from the current discourse:

- **OpenAI team:** Layered architecture enforced by custom linters and structural tests, recurring "garbage collection" that scans for drift and has agents suggest fixes. Conclusion: "Our most difficult challenges now center on designing environments, feedback loops, and control systems."
- **Stripe's minions:** Pre-push hooks running relevant linters via heuristic; highlighting how important "shift feedback left" is; "blueprints" integrating feedback sensors into agent workflows
- **Mutation and structural testing:** Underused in the past, now having a resurgence as computational feedback sensors
- **LSP / code intelligence integration:** Increased chatter about computational feedforward guides
- **Thoughtworks teams:** Tackling architecture drift with computational + inferential sensors — increasing API quality with mix of agents and custom linters; "janitor army" for code quality

**Open questions:**
- How do we keep a harness coherent as it grows, with guides and sensors in sync and not contradicting each other?
- How far can we trust agents to make sensible trade-offs when instructions and feedback signals point in different directions?
- If sensors never fire, is that high quality or inadequate detection mechanisms?
- We need a way to evaluate **harness coverage and quality** similar to what code coverage and mutation testing do for tests
- Feedforward and feedback controls are currently scattered across delivery steps — potential for tooling that helps configure, sync, and reason about them as a system
- Building this outer harness is emerging as an ongoing engineering practice, not a one-time configuration

---

## Acknowledgements

Big thanks to the Doppler team, in particular Kief Morris for bringing up cybernetics. Thanks to Ned Letcher, Chris Ford and Ben O'Mahoney for conversations about what a harness even is, and to Matteo Vaccari for insights on the behaviour harness.

GenAI (Claude and Claude Code) was used for research, pulling in relevant ideas from existing notes, and polishing the language.

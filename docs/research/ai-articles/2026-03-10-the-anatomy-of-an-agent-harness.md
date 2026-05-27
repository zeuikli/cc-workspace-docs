---
url: "https://www.langchain.com/blog/the-anatomy-of-an-agent-harness"
title: "The Anatomy of an Agent Harness"
author: "Vivek Trivedy (LangChain)"
archived: 2026-05-27
domain: blog.langchain.com
published: 2026-03-10
tags: [harness-engineering, llm-agents, agent-architecture, context-management, sandboxes, long-horizon, langchain]
word_count: 約 2200 字
---

# The Anatomy of an Agent Harness

> **來源**：[langchain.com](https://www.langchain.com/blog/the-anatomy-of-an-agent-harness)
> **作者**：Vivek Trivedy（LangChain）
> **發布日期**：2026-03-10
> **收錄日期**：2026-05-27

---

## Overview

本文定義「agent harness」的解剖結構，以「Behavior we want → Harness Design」的反向推導方式，逐一解釋 harness 各元件存在的原因。核心等式：Agent = Model + Harness；harness 是除模型本身以外的一切程式碼、設定與執行邏輯，讓模型智能在實作上可用。

**Key Takeaways:**
- Break down complex objectives: Planning tools let agents decompose tasks, track progress, and adapt as they learn
- Delegate work in parallel: Spawn subagents for independent subtasks, each with isolated context
- TLDR: Agent = Model + Harness. Harness engineering is how we build systems around models to turn them into work engines.

---

## Can Someone Please Define a "Harness"?

**Agent = Model + Harness**

If you're not the model, you're the harness.

A harness is **every piece of code, configuration, and execution logic that isn't the model itself.** A raw model is not an agent. But it becomes one when a harness gives it things like state, tool execution, feedback loops, and enforceable constraints.

Concretely, a harness includes:
- System Prompts
- Tools, Skills, MCPs and their descriptions
- Bundled Infrastructure (filesystem, sandbox, browser)
- Orchestration Logic (subagent spawning, handoffs, model routing)
- Hooks/Middleware for deterministic execution (compaction, continuation, lint checks)

This is the cleanest definition because it **forces us to think about designing systems around model intelligence.**

---

## Why Do We Need Harnesses? From a Model's Perspective

Models take in data (text, images, audio, video) and output text. Out of the box they cannot:
- Maintain durable state across interactions
- Execute code
- Access realtime knowledge
- Setup environments and install packages to complete work

These are all **harness-level features.**

For example, to get a "chatting" UX, we wrap the model in a while loop to track previous messages and append new user messages — that's already a harness.

The main idea: **convert desired agent behavior into an actual feature in the harness.**

---

## Working Backwards from Desired Agent Behavior

The pattern throughout this article:

> **Behavior we want (or want to fix) → Harness Design to help the model achieve this.**

Harness Engineering helps humans inject useful priors to guide agent behavior. As models have gotten more capable, harnesses have been used to surgically extend and correct models to complete previously impossible tasks.

---

## Filesystems for Durable Storage and Context Management

**We want agents to have durable storage** to interface with real data, offload information that doesn't fit in context, and persist work across sessions.

Models can only directly operate on knowledge within their context window. Before filesystems, users had to copy/paste content directly to the model — clunky UX that doesn't work for autonomous agents.

**Harnesses ship with filesystem abstractions and tools for fs-ops.**

What the filesystem unlocks:
- Agents get a workspace to read data, code, and documentation
- Work can be incrementally added and offloaded instead of holding everything in context; agents can store intermediate outputs and maintain state that outlasts a single session
- **The filesystem is a natural collaboration surface** — multiple agents and humans can coordinate through shared files (architectures like Agent Teams rely on this)

Git adds versioning to the filesystem so agents can track work, rollback errors, and branch experiments.

---

## Bash + Code as a General Purpose Tool

**We want agents to autonomously solve problems** without humans needing to pre-design every tool.

The main agent execution pattern today is a **ReAct loop**: model reasons → takes action via tool call → observes result → repeats.

But harnesses can only execute the tools they have logic for. Instead of forcing users to build tools for every possible action, the better solution is to give agents a general-purpose tool like bash.

**Harnesses ship with a bash tool so models can solve problems autonomously by writing & executing code.**

Bash + code exec is a big step toward giving models a computer and letting them figure out the rest. The model can **design its own tools on the fly** via code instead of being constrained to fixed pre-configured tools.

Harnesses still ship with other tools, but code execution has become the default general-purpose strategy for autonomous problem solving.

---

## Sandboxes and Tools to Execute & Verify Work

**Agents need an environment with the right defaults** so they can safely act, observe results, and make progress.

Running agent-generated code locally is risky, and a single local environment doesn't scale to large agent workloads.

**Sandboxes give agents safe operating environments.** Instead of executing locally, the harness connects to a sandbox to run code, inspect files, install dependencies, and complete tasks. This creates:
- Secure, isolated execution of code
- Allow-listed commands and network isolation for more security
- Scale — environments created on demand, fanned out across many tasks, torn down when done

**Good environments come with good default tooling.** Harnesses are responsible for:
- Pre-installing language runtimes and packages
- CLIs for git and testing
- Browsers for web interaction and verification

Tools like browsers, logs, screenshots, and test runners give agents a way to **observe and analyze their work**, creating self-verification loops: write code → run tests → inspect logs → fix errors.

---

## Memory & Search for Continual Learning

**Agents should remember what they've seen** and access information that didn't exist when they were trained.

Models have no additional knowledge beyond their weights and current context. Without access to edit model weights, the only way to "add knowledge" is via **context injection.**

**For memory:** The filesystem is again a core primitive. Harnesses support memory file standards like `AGENTS.md` which get injected into context on agent start. As agents add and edit this file, harnesses load the updated file into context — a form of continual learning where agents durably store knowledge from one session and inject it into future sessions.

**For up-to-date knowledge:** Knowledge cutoffs mean models can't directly access new data like updated library versions. Web Search and MCP tools like Context7 help agents access information beyond the knowledge cutoff.

> Web Search and tools for querying up-to-date context are useful primitives to bake into a harness.

---

## Battling Context Rot

**Agent performance shouldn't degrade** over the course of work.

**Context Rot** describes how models become worse at reasoning and completing tasks as their context window fills up. Context is a precious and scarce resource.

> Harnesses today are largely delivery mechanisms for good context engineering.

**Compaction:** Addresses what to do when the context window is close to filling up. Without compaction, the API errors. The harness intelligently offloads and summarizes the existing context window so the agent can continue working.

**Tool call offloading:** Reduces the impact of large tool outputs that clutter the context window without providing useful information. The harness keeps head and tail tokens of tool outputs above a threshold, offloads the full output to the filesystem for the model to access if needed.

**Skills:** Address the issue of too many tools or MCP servers loaded into context on agent start, which degrades performance before the agent can even start working. Skills are a harness-level primitive that solve this via **progressive disclosure** — the model didn't choose to have Skill front-matter loaded into context, but the harness can support this to protect the model against context rot.

---

## Long Horizon Autonomous Execution

**We want agents to complete complex work, autonomously, correctly, over long time horizons.**

Autonomous software creation is the holy grail for coding agents. But today's models suffer from:
- Early stopping
- Issues decomposing complex problems
- Incoherence as work stretches across multiple context windows

This is where earlier harness primitives start to **compound.**

**Filesystems and git for tracking work across sessions.** Agents produce millions of tokens over a long task; the filesystem durably captures work. Adding git allows new agents to quickly get up to speed on history. For multiple agents working together, the filesystem acts as a **shared ledger of work**.

**Ralph Loops for continuing work.** The Ralph Loop is a harness pattern that:
1. Intercepts the model's exit attempt via a hook
2. Reinjects the original prompt in a clean context window
3. Forces the agent to continue its work against a completion goal

The filesystem makes this possible — each iteration starts with fresh context but reads state from the previous iteration.

**Planning and self-verification to stay on track:**
- **Planning:** Model decomposes a goal into steps. Harnesses support this via good prompting and injecting reminders on how to use a plan file in the filesystem.
- **Self-verification:** Hooks in harnesses can run a pre-defined test suite and loop back to the model on failure, or models can be prompted to self-evaluate their code independently. Verification grounds solutions in tests and creates a feedback signal for self-improvement.

---

## The Future of Harnesses

### The Coupling of Model Training and Harness Design

Today's agent products like Claude Code and Codex are **post-trained with models and harnesses in the loop.** This helps models improve at actions that harness designers think they should be natively good at: filesystem operations, bash execution, planning, parallelizing work with subagents.

This creates a feedback loop: useful primitives are discovered, added to the harness, and then used when training the next generation of models. As this cycle repeats, models become more capable within the harness they were trained in.

**Side effects for generalization:** This co-evolution shows up in ways like how changing tool logic leads to worse model performance. Example from the Codex-5.3 prompting guide: the `apply_patch` tool logic for editing files — a truly intelligent model should have little trouble switching between patch methods, but training with a harness in the loop creates overfitting.

**But the best harness for your task is not necessarily the one a model was post-trained with.** The Terminal Bench 2.0 Leaderboard is a good example — Opus 4.6 in Claude Code scores far below Opus 4.6 in other harnesses. LangChain improved their coding agent from Top 30 to Top 5 on Terminal Bench 2.0 **by only changing the harness.**

### Where Harness Engineering is Going

As models get more capable, some of what lives in the harness today will get absorbed into the model. Models will get better at planning, self-verification, and long-horizon coherence natively.

That suggests harnesses should matter less over time. But just as prompt engineering continues to be valuable, **harness engineering will continue to be useful for building good agents.**

Harnesses today patch over model deficiencies, but they also engineer systems around model intelligence to make them more effective. A well-configured environment, the right tools, durable state, and verification loops make any model more efficient regardless of its base intelligence.

**Active research areas at LangChain (deepagents library):**
- Orchestrating hundreds of agents working in parallel on a shared codebase
- Agents that analyze their own traces to identify and fix harness-level failure modes
- Harnesses that dynamically assemble the right tools and context just-in-time for a given task instead of being pre-configured

---

## Conclusion

The model contains the intelligence and the harness is the system that makes that intelligence useful. Harness engineering is the discipline of thoughtful system design around model intelligence.

> The model contains the intelligence and the harness makes that intelligence operationally useful through thoughtful system design.

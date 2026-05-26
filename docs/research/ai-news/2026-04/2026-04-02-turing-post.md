---
title: Turing Post — 2026-04-02
date: 2026-04-02
source: Turing Post
type: ai-news
---

# 🏛️ Turing Post — 2026-04-02

> Ksenia Se 主持，95k+ 訂閱；AI/ML 政策、地緣政治與深度洞察
> 來源：[Turing Post](https://turingpost.substack.com/feed)

---

## [AI 101: Hermes Agent – OpenClaw’s Rival? Differences and Best Use Cases](https://turingpost.substack.com/p/ai-101-hermes-agent-openclaws-rival)
*🏛️ Turing Post | 2026-04-02*

There is a familiar pattern in AI, as in many fast-moving fields: one project helps define a category, and the next wave starts to explore different tradeoffs and directions. [OpenClaw](https://www.turingpost.com/p/openclaw) helped make the idea of a personal, self-hosted agent feel practical. For the first time, agents were helpful, proactive, and felt like a real extension of the workforce. OpenClaw truly conquered the space in a matter of weeks. And now it is time to challenge it. Quite a few people have reported switching to Hermes Agent by Nous Research, and we are here to investigate why, and whether it is worth it.

A lot of agents today have memory, but not many have a built-in mechanism for turning experience into reusable procedures automatically. Hermes Agent is asking: what happens if a local agent can improve through use, not just execute tasks and store memory? That sounds ambitious, and it is, because making that work requires more than just adding memory. It depends on a fairly sophisticated stack for capturing experience, organizing it, and turning it into behavior the agent can reuse.

In this piece, we will look at what it takes to build a self-improving local agent, how Hermes is designed to accumulate capabilities and skills over time, and what kind of memory system supports that process. We will also compare Hermes with OpenClaw to see where it actually stands, where it differs, and what each system is better suited for in a personal workflow.

In today’s episode:

A few words about Nous Research

How Hermes Agent works

Inside the new architecture

Self-improvement and procedural knowledge: how Hermes remembers methods

The layered memory stack

Agent personality: another SOUL.md variant

Automation: schedule support 

Safety becomes a default

Build-in tools and research

Easy adoption (how-to)

Hermes vs. OpenClaw: side-by-side

Best use cases for Hermes Agent

Is Hermes a real rival to OpenClaw?

Not without limitations

Conclusion

Sources and further reading

A few words about Nous Research

Nous Research emerged informally in 2022 as an internet-native collective formed across Discord and Twitter, and was later formalized in 2023 with founders including Jeff Quesnelle, Karan Malhotra, Teknium, and Shivani Mitra. From the beginning, they positioned themselves as an open-source-first and decentralization-focused lab. Their goal was to build user-controlled AI, making intelligence widely accessible rather than concentrated in a few closed companies. 

Their early work concentrated on the Hermes model series, but in parallel, Nous Research invested heavily in infrastructure and systems questions. With DisTrO (Distributed Training Over the Internet), they explored training models across globally distributed consumer GPUs, treating model training as a decentralized network problem. They developed large-scale simulation environments (e.g. WorldSim, Doomscroll), focusing on multi-agent interaction, long-horizon behavior, and emergent strategies.

Around 2024–2025, their work converges:

Atropos reinforcement learning environments for trajectories and reasoning

Forge API / inference research improving multi-step reasoning at runtime

Hermes models more persistent, reasoning-capable, tool-using. The latest Hermes 4, released in 2025, introduces hybrid reasoning and large-scale synthetic data generation.

Hermes Agent is the logical synthesis of all prior threads. Now it is gaining popularity because it is the first real alternative to the OpenClaw local agent. And “real” means that before we’ve seen a lot of OpenClaw-style agents built around the same idea as OpenClaw. Hermes introduces many changes in the agent’s architecture, betting on another focus – everything is built around self-evaluation and for self-evaluation. Basically, it is an open-source autonomous agent that runs persistently on your own machine or server designed to remember across sessions, learn from experience in self-improvement loop, create and reuse skills, and use scheduled automation. But there is much more under the hood → 

How Hermes Agent works

Inside the new architecture

From the architectural side, Hermes chooses a new center of gravity, probably fulfilling the hopes of many users and developers who have been waiting for self-improving systems. But first, let’s refresh how today’s most popular [OpenClaw](https://www.turingpost.com/p/openclaw) agent is built. 

For OpenClaw, the Gateway is a control plane – a single long-running process that owns sessions, routing, tool execution, and state. Everything flows through it.

Hermes, by contrast, defines the AIAgent loop itself as the core synchronous orchestration engine, with gateway, cron scheduler, tooling runtime, ACP (Agent Communication Protocol – a standardized way for external tools like code editors to talk to the agent) integration, SQLite-backed session persistence and Reinforcement Learning (RL) environments structured around it.

The difference is this: OpenClaw is organized around a central controller that coordinates everything, while Hermes puts the focus on the agent’s own execution loop – a repeatable “do, learn, improve” cycle – and builds the system around that.

Image Credit: Hermes Agent Docs, Architecture

Hermes Agent is portable and it is not tied to one app or one machine. You can simply run it:

locally in a terminal

on a VPS

in Docker

over SSH

on serverless infrastructure

or on bigger GPU-backed systems

While Hermes runs anywhere (see above), you can interact with it via messaging apps – Telegram, Discord, Slack, WhatsApp, Signal, and other connected interfaces – or through CLI. This decouples the assistant from your laptop: the compute happens remotely, but the interface stays lightweight and always available.

Hermes is model-agnostic, as well. You can plug in models from services like OpenAI, OpenRouter, Kimi Moonshot, MiniMax, GLM models, Nous Portal or your own custom endpoint. And notably, model selection is treated as configuration. So you can switch models with a command like “hermes model” instead of changing application code. 

Hermes Agent is also a step toward a real interactive development environment for agents, because it includes a text user interface (TUI) with things like multiline editing, autocomplete for commands, conversation history, interrupting a running task, redirecting the agent mid-process, streaming tool output.

But these are not the features that make Hermes especially distinctive today → 

Self-improvement and procedural knowledge: how Hermes remembers methods

The biggest focus and a defining feature at the heart of Hermes is self-improvement. Every set of interactions and tries, Hermes evaluates what worked, what didn’t work, what was useful, what user asked to correct. And here is the moment when we meet with agent’s “skills” again. OpenClaw also works with skills, which are reusable, mostly human-authored tool/workflow instructions loaded from several scopes like workspace, personal, shared, or plugins. Hermes has a different idea:

---

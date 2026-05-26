---
url: "https://www.forbes.com/sites/josipamajic/2026/04/12/the-yc-chief-who-codes-10000-lines-a-day-has-a-simple-secret/"
title: The YC Chief Who Codes 10,000 Lines A Day Has A Simple Secret
author: Josipa Majic Predin (Forbes Contributor)
date: 2026-04-12
status: SUCCESS
---

# The YC Chief Who Codes 10,000 Lines A Day Has A Simple Secret

Garry Tan runs Y Combinator, the accelerator that launched Airbnb, Stripe, and Coinbase. He also claims to ship 600,000 lines of production code every 60 days, part-time, while running that organization full-time. The number sounds fabricated until you understand the architecture behind it, and the architecture fits on an index card.

In a widely circulated post on X, Tan laid out a framework he calls thin harness, fat skills: a design philosophy for AI agents that the March 31 accidental leak of Claude Code's 512,000-line TypeScript source confirmed in unexpected detail. The insight is that you can use the same model, but increase it's output significantly by leveraging scaffolding.

## The Leak That Proved the Point

When security researcher Chaofan Shou discovered that Anthropic had accidentally published a 59.8 MB source map file alongside version 2.1.88 of Claude Code on npm, the immediate story was the security lapse. The story was what the 1,906-file codebase revealed about how production AI products actually work.

Claude Code, as TechTalks analyzed, is not a thin wrapper around a language model. It is a self-healing query loop, a background memory daemon called autoDream, concurrency-safe tool batching, compile-time feature gating, and a context management system that prevents the model from drowning in its own history. The model sits at the center of all of it and the harness does everything else.

Anthropic's head of Claude Code, Boris Cherny, confirmed the incident was a plain developer error in a statement on X, and added a note that has since circulated widely: "100% of my contributions to Claude Code were written by Claude Code."

## Five Definitions Investors Should Understand

Tan's framework, articulated in the X post and instantiated in gstack, his open-source Claude Code configuration that accumulated 66,000 GitHub stars within weeks of release, rests on five concepts that reframe how AI development tools should be evaluated.

**Skill files** are reusable markdown documents that encode process, not content. The same /investigate skill, pointed at a safety scientist or at FEC filings, produces radically different outputs because the skill describes judgment and the invocation supplies the world. Tan frames these as method calls, with markdown as the programming language and human judgment as the runtime.

**The harness** runs the model in a loop, manages context, reads and writes files, and enforces safety. The anti-pattern Tan explicitly calls out is a fat harness: 40-plus tool definitions eating half the context window, god-tools with multi-second MCP round-trips, REST API wrappers that turn every endpoint into a separate tool. The Claude Code source confirms this discipline: opinionated, narrow tooling throughout.

**Resolvers** are routing tables for context. When task type X appears, load document Y. The embedded resolver in Claude Code matches user intent to skill descriptions automatically. Tan's CLAUDE.md went from 20,000 lines to roughly 200, with pointers to documents rather than the documents themselves.

**Latent versus deterministic** is the most consequential distinction in agent design. Judgment, synthesis, and pattern recognition belong in latent space. SQL queries, arithmetic, and combinatorial optimization belong in deterministic tooling. Forcing a deterministic problem through a model produces outputs that look plausible and are wrong. The best systems are ruthless about which work goes where.

**Diarization** is the step that turns document retrieval into genuine analysis. The model reads everything about a subject and produces a structured single-page brief, a distillation no SQL query or RAG pipeline replicates. Tan uses it throughout his YC Startup School matching system: 6,000 founder profiles, running nightly, surfacing the gap between what founders say they are building and what the commit history shows.

## The VC Angle

The framework matters to investors for a reason that has little to do with software architecture. The companies that understand this distinction, model versus harness, are compounding in ways that companies chasing raw model capability are not.

The productivity gains have a direct implication for how investors evaluate AI-native teams. The question is no longer which model a company uses. Model capability is table stakes and commoditizing faster than most forecasts expected. The question is whether the team has built the surrounding architecture with the same rigor they applied to the product itself. Skill files that encode domain judgment and context management that scales beyond a single developer.

The Claude Code leak made this legible in a way that blog posts could not. Anthropic's moat is not the model but "the self-healing loop, the memory architecture, the anti-distillation mechanisms," the years of engineering judgment baked into 1,906 TypeScript files. Competitors can read the source now but the judgment encoded in it took years to accumulate.

## What This Means Going Forward

Steve Yegge, whose productivity estimates Tan cites, puts well-harnessed AI agents at 10x to 100x the productivity of developers using standard chat tools, and roughly 1,000x relative to baseline knowledge workers in 2005. The 2x people and the 100x people use the same underlying models.

For founders; every repeatable task that crosses your desk should become a skill file, not a recurring prompt. If you ask your agent for the same thing twice, you are already losing. For investors performing due diligence on AI-native companies, the question to ask is whether the team's productivity claims survive a harness audit. Whose context management sits in a 20,000-line CLAUDE.md that degrades with scale, and whose sits in 200 lines of pointers to purpose-built skills.

Tan's gstack is MIT-licensed, installs in thirty seconds, and has already been forked more than 9,100 times. The architecture it embodies will outlast any model generation currently in production.

---
title: "AlphaSignal — 2026-05-24"
date: 2026-05-24
source: AlphaSignal
type: ai-news
---

# 📡 AlphaSignal — 2026-05-24

> 200k+ 訂閱；最新 AI 研究 / repos / 模型的 5 分鐘技術日報
> 來源：[AlphaSignal](https://alphasignalai.substack.com/feed)

---

## [Spec-Driven Development is the New Default for AI Coding](https://alphasignalai.substack.com/p/spec-driven-development-is-the-new)
*📡 AlphaSignal | 2026-05-22*

In ~8 mins: what SDD is, why it became the default for AI coding, how the 5 leading repos implement it, and the one critic saying the whole category is wrong.

Spec-driven development crossed from blog-post topic to default architecture for AI coding in the last 12 months.

Thoughtworks, Martin Fowler, GitHub, Amazon, and a 67-source academic review all agreed in 2025 and 2026.

The question stopped being whether to use SDD and became which implementation.

What happened

Multiple independent sources converged on the same recommendation inside 18 months.

Thoughtworks listed spec-driven development in Technology Radar Vol. 32 as a technique worth adopting. Martin Fowler covered it on his site.

GitHub shipped Spec Kit, an MIT-licensed toolkit framed as the answer to vibe coding. Amazon launched Kiro, an agentic tool that walks users through requirements, design, and tasks before any code generation. Tessl launched at the radical end, with specs positioned as the new source code.

Red Hat published enterprise SDD guidance. InfoQ covered it at the architecture level.

Bryan Finster pushed back with the right critique. SDD is not a revolution, it’s just BDD with branding.

That critique strengthens the case. The idea is not new. The context is.

BDD was an optional discipline that teams could adopt or ignore. With 84% of professional developers using or planning to use AI tools (Stack Overflow, 2025) and 46% of code output now AI-generated (GitHub, 2025), specification discipline became structurally necessary.

Why it became necessary

Four academic papers landed in 12 months, mapping the same problem from different angles.

Sabry Farrag at the University of East London ran a 67-source systematic review of the productivity paradox. AI coding tools deliver real individual-level gains and real system-level damage at the same time.

Peng et al. measured 55.8% faster completion in a 95-developer RCT. Becker et al.’s METR study found a 19% slowdown for experienced developers working on mature codebases.

DORA reported that 25% AI adoption correlates with a 7.2% drop in delivery stability. Faros AI tracked over 10,000 developers and saw 98% more merged PRs, 91% more review time, and 9% more bugs.

Shuvendu Lahiri at Microsoft Research named the underlying gap. AI-generated code is plausible by construction, not correct by construction. The semantic distance between what a user means and what a program does is the central reliability bottleneck.

An AIware 2026 vision paper named a second gap. Code review evaluates plausibility, not compliance. Most AI-generated changes pass tests, look reasonable, and still drift from the rules they were supposed to follow.

Deepak Babu Piskala wrote the practitioner manual that ties it together. He frames SDD across three rigor levels and a four-phase workflow.

Farrag’s economic argument closes the loop. Code generated for a specific codebase has high asset specificity. LLMs introduce high behavioral uncertainty.

Developers invoke AI hundreds of times daily. In Transaction Cost Economics terms, that combination makes a written, executable contract the rational governance response. SDD is that contract.

How it actually works

SDD compresses to three things a practitioner needs to hold.

A four-phase workflow. Specify what the software should do. Plan how to build it. Implement in small, validated increments. Validate that the code meets the spec. Each phase produces an artifact that constrains the next.

Three rigor levels. Spec-first means a specification is written before coding but may drift after. Spec-anchored means the spec lives alongside the code and tests enforce alignment. Spec-as-source means the spec is the only artifact humans edit, with code regenerated rather than manually changed.

A governance spectrum. Farrag’s paper ranks four mechanisms by constraint intensity:

Post-hoc review is the loosest, where a developer reviews AI output after the fact.

Natural-language specification is next, putting requirements before generation.

Executable contract follows, with tests and structured spec documents the agent must satisfy.

Constitutional governance is the tightest, a meta-specification of non-negotiable principles that every change must honor.

The higher the asset specificity, behavioral uncertainty, and frequency, the further up the spectrum the rational choice sits. Production code in a mature codebase invoked by AI hundreds of times daily lands at constitutional. A throwaway prototype lands at post-hoc.

The five SDD repos, by philosophy

Each repo encodes a different theory of where complexity belongs.

Full comparison table at the end. Links are in replies.

Spec Kit: constitution as authority

GitHub’s official toolkit, MIT-licensed, Python CLI (specify init).

The theory of complexity: put it in the constitution. A non-negotiable principles file at .specify/memory/[constitution.md](http://constitution.md/) sits above every spec and every implementation. The agent obeys it on every change, every session.

The workflow runs through nine slash commands:

/speckit.constitution

/speckit.specify

/speckit.clarify

/speckit.plan

/speckit.tasks

/speckit.taskstoissues

/speckit.checklist

/speckit.analyze

/speckit.implement

The constitution and analyze steps are where the formal governance lives.

Farrag’s paper evaluates Spec Kit as the direct instantiation of constitutional governance. The reported result: 12 hours to 15 minutes for upstream artifact production (PRD, design, structure, technical specs, test plans).

A pilot study saw late-stage hotfixes drop from 3-to-5 per sprint to 1-to-2, and rollbacks drop from 2-to-4 per month to 0-to-1.

30+ AI agent integrations including Claude, Codex, Copilot, Cursor, Gemini.

This is the only repo with explicit constitutional governance. The highest tier on Farrag’s spectrum, and the steepest setup cost.

BMAD-METHOD: named agents as authority

BMad Code LLC, MIT, npm (npx bmad-method install). V6, with 34+ workflows.

The theory of complexity: put it in the roles. Six named personas, each with domain expertise:

Analyst Mary handles brainstorming and research.

PM John owns PRDs.

Architect Winston runs the 8-step architecture workflow.

Developer Amelia handles dev stories, sprint planning, and code review.

UX Designer Sally owns interface decisions.

Tech Writer Paige owns documentation.

Party Mode brings multiple personas into one session to argue from different professional perspectives.

The lifecycle has four phases: Analysis, Planning, Solutioning, Implementation. Each phase has its own workflows.

A .[decision-log.md](http://decision-log.md/) records every decision as an audit trail. An implementation-readiness gate (PASS, CONCERNS, or FAIL) blocks the move to code if anything is missing.

Planning depth auto-adjusts to project stakes. A hobby project gets a 2-page PRD. A launch project gets full specs. The bmad-help skill answers free-form questions about what to do next.

The module ecosystem extends the core with specialized domains: BMM (core), BMB (custom agents), TEA (test architecture), BMGD (game dev), CIS (creative intelligence).

This is the only repo that treats specifications as the inter-agent communication protocol of a multi-agent organization.

OpenSpec: change folders as the unit

Fission AI, MIT, npm (openspec init).

The theory of complexity: put it in the change. Each feature gets its own folder containing [proposal.md](http://proposal.md/) (why this change), specs/ (requirements and scenarios), [design.md](http://design.md/) (technical approach), and [tasks.md](http://tasks.md/) (implementation checklist).

When the change ships, /opsx:archive folds the change spec into a growing source-of-truth document.

The core surface is three commands:

/opsx:propose creates the change folder.

/opsx:apply has the AI implement the task checklist.

/opsx:archive closes it out.

An opt-in expanded profile adds six more: /opsx:new, /opsx:continue, /opsx:ff, /opsx:verify, /opsx:bulk-archive, /opsx:onboard.

The positioning is explicitly brownfield-first. Most SDD tools optimize for greenfield projects. OpenSpec is built to retrofit existing codebases. The delta-spec format (additions, modifications, removals tracked per change) is what makes that work.

Works with 25+ AI assistants via slash commands.

Executable contract at the lightest possible weight. No constitution, no named agents, no ceremony. The spec discipline survives without the process.

GSD: context as the bottleneck

TÂCHES, MIT, npm (npx get-shit-done-cc@latest). Built by a solo developer for solo developers.

The theory of complexity: put it in context engineering. The main session context stays at 30 to 40 percent. Heavy work runs in fresh subagent contexts, each getting a full 200K-token window.

The hypothesis the rest of the architecture rests on: as a session grows, AI output degrades, so the architecture should keep the session small.

The loop is six commands:

/gsd-new-project runs questions, research, requirements, roadmap.

/gsd-map-codebase does the same for existing code.

/gsd-discuss-phase captures decisions before planning.

/gsd-plan-phase runs research, plan, verify in a loop.

/gsd-execute-phase dispatches parallel waves of subagents.

/gsd-verify-work walks through what was built and diagnoses failures.

Five persistent state files survive session boundaries: [PROJECT.md](http://project.md/) (vision), [REQUIREMENTS.md](http://requirements.md/) (scope), [ROADMAP.md](http://roadmap.md/) (direction), [STATE.md](http://state.md/) (current position), [CONTEXT.md](http://context.md/) (per-phase decisions).

The .planning/config.json controls mode (interactive or yolo), model profiles (quality, balanced, budget), and quality-agent toggles. Package legitimacy checks are built into the install path.

Executable contract delivered through context discipline rather than process ceremony. The repo treats the context window as the bottleneck, not the methodology.

Superpowers: auto-triggering as discipline

Built by Jesse Vincent and Prime Radiant. MIT, zero-dependency plugin.

The theory of complexity: put it in the agent’s behavior shaping. Skills auto-trigger at the right moments. No manual invocation. Mandatory workflows, not suggestions.

The using-superpowers skill loads at session start and is what makes auto-triggering work. Copying skill files alone is not a real integration.

Seven core skills run the workflow:

brainstorming refines rough ideas before any code.

using-git-worktrees isolates the workspace.

writing-plans breaks work into 2 to 5 minute tasks with exact file paths and complete code.

subagent-driven-development dispatches a fresh subagent per task with two-stage review (spec compliance, then code quality).

test-driven-development deletes any code written before its test.

requesting-code-review blocks critical issues.

finishing-a-development-branch verifies tests and presents merge options.

The TDD enforcement is the unusual move. Most TDD tooling encourages the loop. Superpowers’ skill deletes code that violates it.

Distributed through the official Claude plugin marketplace, the official Codex plugin marketplace, Factory Droid, Gemini extensions, Cursor, GitHub Copilot CLI, and OpenCode.

Executable contract enforced at the agent layer rather than the user layer. The user never has to remember to invoke the right skill.

The sixth repo, and the case against the category

Matt Pocock’s Skills For Real Engineers sits on the same list of repos by accident. He argues against the category.

His talk Software Fundamentals Matter More Than Ever lands the thesis directly. “Code is not cheap. In fact, bad code is the most expensive it’s ever been.”

On the spec-driven movement specifically: “Specs to code, we are not investing in the design of the system. We are divesting from it.”

His position rests on a software-engineering claim. Bad codebases have always been expensive because they resist change. AI accelerates that. A bad codebase compounded by AI throughput is the most expensive failure mode of the new era.

His repo is composable practices, not a workflow framework. Each skill stands alone:

/grill-me runs a relentless interview to establish what Frederick Brooks calls a shared design concept.

/grill-with-docs adds a Domain-Driven Design ubiquitous language file that humans and AI both reference.

/tdd enforces red-green-refactor as the rate limiter on AI speed.

/improve-codebase-architecture rebuilds shallow modules into deep modules, per John Ousterhout.

The default pattern is gray boxes: design the interface, delegate the implementation.

The data on his side: the METR finding that experienced developers on mature codebases were 19% slower with AI suggests the bottleneck is codebase quality, not specification quality. His argument is that the five SDD repos optimize for the wrong thing.

His repo went viral on the strength of /grill-me alone. The position is worth taking seriously.

The AlphaSignal take

The five SDD repos and Pocock’s dissent are not answering the same question.

SDD optimizes for the plausibility-to-correctness gap. Pocock optimizes for the design-entropy gap. Both gaps are real. Both data sets support both positions.

A team that picks one and ignores the other is solving half the problem.

The reliability case for SDD is strongest at the constitutional and executable-contract levels. Spec Kit’s constitution mechanism and BMAD’s implementation-readiness gate are where the math actually pays off.

The case is weakest at the natural-language end, where SDD collapses into renamed prompt engineering.

Three things none of the six repos solve, drawn from the open problems sections of the four papers.

Oracle adequacy. Current evaluations collapse model quality, tool reliability, and harness quality into one end-task number. There is no metric for what a specification is actually worth.

Evidence bundles. Every accepted change should ship with a record of what was checked, what was not, and what risks remain. No current SDD tool produces this.

Self-evolving harnesses. The SDD frameworks themselves are software. They will change. None of them have a change-contract for their own evolution.

Read each of these repos as a specific theory of where reliability comes from. Pick the one whose theory matches the bottleneck you actually have. If you don’t know your bottleneck, Pocock’s critique applies first.

Which theory of reliability does your stack depend on, constitution, roles, change folders, context, auto-triggering, or design discipline?

Full breakdown of recent updates + daily signals in our newsletter (link in bio).

---

## [The Three Harness Layers and How to Audit Your Stack](https://alphasignalai.substack.com/p/the-three-harness-layers-and-how)
*📡 AlphaSignal | 2026-05-21*

Most agent failures aren’t reasoning failures. They’re harness failures.

An agent that passes every test while looping between two failing strategies, because the harness has no dead-end detection.

A new 100-page survey from UIUC, Meta, and Stanford spells out why.

Paper

It’s called “Code as Agent Harness.” 40+ researchers from UIUC, Meta, and Stanford wrote it, and it synthesizes 400+ papers under a single taxonomy with the harness, not the model, as the subject.

The anchor systems are the familiar ones: Claude Code, Codex, SWE-agent, Voyager, MetaGPT, OpenHands. What’s been a Twitter-thread topic for the last six months now has academic scaffolding around it. The contribution is the synthesis, not the discovery.

Core thesis

Long-running agents fail at state, feedback, and verification. Not at reasoning. The bottleneck of autonomy is whether the system around the model can hold its outputs accountable to something executable.

The paper splits any agent system into three coupled pieces.

First is model-internal capabilities: reasoning, planning, perception.

The second is system-provided infrastructure: tools, sandboxes, memory, permission tiers, telemetry.

And third, the underexplored one, is agent-initiated code artifacts: regression tests, temporary tools, DSL programs, executable workflows, and reusable skills the agent itself authors mid-task. Voyager’s skill library and Claude Code’s skill files are early instances.

Above this distinction sit three layers.

Harness Interface, puts code at the center as the medium for reasoning, action, and environment state.

Harness Mechanisms, covers planning, memory, tool use, and the plan-execute-verify loop.

Scaling the Harness, extends the picture to multi-agent systems coordinating over shared code artifacts.

How to audit your stack

Three questions, one per layer. They map to where most stacks actually break.

I

nterface.

Does your agent’s reasoning, action, and environment state pass through code something can actually execute and inspect? A healthy stack has tool calls, generated programs, repo state, traces, and tests. An unhealthy stack runs on natural-language plans the agent never has to defend against execution.

If unhealthy: have the model output executable code as its reasoning, give the agent a structured Agent-Computer Interface like SWE-agent’s shell + edit + search commands, and let it operate on real repo state rather than text descriptions of it.

Mechanisms.

When something fails, what does the harness do about it? A healthy stack runs a plan-execute-verify loop with named verifiers (unit tests, type checks, linters, runtime monitors), durable memory across sessions, and feedback that closes the loop. An unhealthy stack retries with more tokens and a longer context window.

If unhealthy: add named verifiers as gates between generation steps, not just at the end. Most agents only have working memory, which is whatever sits in the current prompt. The paper names four more types that decide whether yesterday’s debugging session helps today: semantic memory of the repo, experiential memory of past trajectories, long-term memory with a compression policy, and multi-agent memory for shared state. OpenHands’ stateful workspace and CodeMem’s budgeted memory slots are reference implementations to study.

Scaling.

When two agents work on the same task, what’s the shared substrate? A healthy stack uses shared code artifacts (repos, tests, traces, structured workflows) with a conflict policy. An unhealthy stack passes messages back and forth with no shared state both can safely modify.

If unhealthy: replace direct message-passing with shared artifacts both agents can read and write. AgentCoder’s programmer-tester-executor split and MetaGPT’s role-specialized agents over a shared message pool are the patterns the paper highlights.

If any of these answers feel unhealthy, the paper has already named the failure mode.

Also, the paper covers

Five application domains. Code assistants, GUI/OS agents, scientific discovery, embodied agents, personalization.

Self-evolving harnesses. AutoHarness, Meta-Harness, Agentic Harness Engineering (AHE) (related article down below), GEPA, EvoMAC, and SEW. The harness itself as the object of optimization, with the agent’s task code as a downstream effect.

[Post link.](https://x.com/AlphaSignalAI/status/2049900160080077229)

Workflow topologies. Five patterns for multi-agent code work: waterfall, cyclic, hierarchical (related article down below), star, adaptive.

[Post link.](https://x.com/AlphaSignalAI/status/2051352235926249945)

Planning paradigms. Four categories, from ReAct-style linear decomposition to tree-search-based exploration across candidate paths.

Three more open problems. Harness evolution that doesn’t break old behaviors, shared state across agents with safe coordination, and multimodal harnesses for screenshots and physical state.

The AlphaSignal take

The most useful vocabulary the field has had for what practitioners are already building. Just not a build plan. Three gaps from the paper’s open problems. Each one is a design warning for what’s already in your stack.

Oracle adequacy.

If your eval is pass/fail on unit tests, you’re measuring the wrong thing. Every agent evaluation today collapses model quality, tool reliability, and harness quality into one end-task number. The paper names this as the central bottleneck and offers no metric that fixes it.

The verification gap.

Green tests are not a correct specification. Every accepted action should ship with an evidence bundle: which checks ran, which assumptions held, which parts of the code stayed untested, what risks remain. No current harness does this. The architecture pattern is sitting there, waiting for someone to ship it.

Approvals that don’t reset.

If approvals vanish after the session ends, your agent will repeat the same unsafe action next time. Permission rules should mutate in response to human decisions, not reset. The paper flags this and stops there.

Read it as a vocabulary, not a roadmap. The harness is the layer teams now invest in optimizing. The taxonomy will sharpen how you talk about your stack. It won’t tell you what to build on Monday.

Does your agent have a verifier that isn’t just the model judging its own output?

[Paper Link](https://arxiv.org/abs/2605.18747)

Full breakdown of recent updates + daily signals in our newsletter (link in bio).

---

## [How OpenHuman Works, And How to Set It Up in 5 Minutes](https://alphasignalai.substack.com/p/how-openhuman-works-and-how-to-set)
*📡 AlphaSignal | 2026-05-20*

In 5 minutes, you will know what OpenHuman is, how its memory works, how it compares to OpenClaw and Hermes Agent, and you will have it running locally with Gmail, Notion, or Slack connected.

OpenHuman crossed +20k GitHub stars in days.

Most of those stars came during a GitHub Trending run the founder marked at seven days at #1 on May 18, 2026, when he also posted that the project had hit #1 on Product Hunt’s daily, weekly, and monthly leaderboards.

@ProductHunt on both weekly AND monthly.\n\nThis means we are number one on daily, weekly, monthly and just a few upvotes away from being the number one product of the entire year! WTF 😳\n\nMajor release and bug fixes tomorrow ⛴️ ","username":"senamakel","name":"Steven Enamakel","profile_image_url":"https://pbs.substack.com/profile_images/2036165243068620801/5YuqzEEs_normal.jpg","date":"2026-05-18T02:48:45.000Z","photos":[{"img_url":"https://pbs.substack.com/media/HIkb10paUAAR3Jl.jpg","link_url":"https://t.co/ESVVjSdwSG"}],"quoted_tweet":{},"reply_count":19,"retweet_count":10,"like_count":78,"impression_count":9123,"expanded_url":null,"video_url":null,"belowTheFold":false}" data-component-name="Twitter2ToDOM">

Steven Enamakel, the founder, tried to set up an open-source AI agent for his dad earlier this year. Three hours of API keys, YAML, and a terminal his dad had never opened later, they both gave up. OpenHuman is what came out of that.

OpenClaw (+373k stars, MIT) and Hermes Agent (+157k stars, MIT) are the two open-source agents OpenHuman is now compared with. Both are great. Neither walks your tools and writes the memory before you start prompting.

This morning at 07:17 UTC, v0.54.0 shipped, with fully-local voice and a shared-memory bridge to Claude Code, Cursor, Codex, and OpenCode.

What OpenHuman is

OpenHuman is an open-source (GPL-3.0) desktop AI agent from TinyHumans AI.

It is written in Rust (65.2% of the codebase) with a TypeScript + React 19 frontend, packaged as a native Tauri v2 desktop app. It ships on macOS, Windows, and Linux. No mobile.

The pitch in one line: most agents start cold, OpenHuman walks your tools every 20 minutes and writes the memory into Markdown files you can open and edit.

Five things ship in the box:

A clean desktop UI with a mascot that can speak, react, and join Google Meet as a real participant.

A 118+ Composio toolkit catalog for one-click OAuth integrations.

A Memory Tree plus an Obsidian-compatible Markdown vault as the local knowledge base.

Batteries-included native tools: web search, web-fetch scraper, full coder toolset, native voice.

TokenJuice, a token compression layer that runs on every tool result before it touches an LLM.

The whole project is three months old. The public repo was created on February 18, 2026.

Why it matters

Most open-source agents bet on the wrong half of the problem.

They get smarter at planning. They add more tools. They wire up more channels. They still know nothing about you until you paste your week into the prompt.

OpenHuman is betting the other way. Structured local memory beats embedding-bag retrieval when the agent needs to navigate your day, not similar text. The founder’s framing, from the Product Hunt launch:

“Every powerful AI agent today is built for the 0.01% who can spin up their own runtime. The other 99.99% are watching the agent revolution from the sidelines.“

Early traction tracks that bet. 5,000+ users in the first 7 days and 150% week-over-week growth, per the founder’s Product Hunt post.

OpenClaw and Hermes Agent take different bets. OpenClaw is a multi-channel gateway across 20+ messaging surfaces. Hermes Agent is a self-improving runtime with a closed learning loop. Neither tries to walk your tools and write the memory before you prompt. Full head-to-head comparison further down.

How it works

Not here for the internals? Skip to How to Get Started below.

Nine pieces. The memory pipeline is the spine. Everything else hangs off it.

4.1 Memory Tree

A deterministic, bucket-sealed pipeline, not a vector-store wrapper.

source adapters → canonicalize → chunker → content_store → store → score → source/topic/global trees → retrieval

Data is canonicalized to Markdown, split into ≤ 3,000-token chunks with deterministic IDs, scored, and folded into three trees: source (one per source, L0 → L1 → L2 cascade), topic (one per high-hotness entity), global (one node per UTC day). Three background workers run heavy work behind a semaphore. A daily scheduler at 00:00 UTC enqueues the global digest and stale-flush.

Storage layout:

`<workspace>`/memory_tree/chunks.db: SQLite, holds chunks, scores, summaries, entity index, jobs, hotness.

`<workspace>`/wiki/: the Obsidian-compatible Markdown vault.

`<workspace>` defaults to ~/.openhuman, overridable with OPENHUMAN_WORKSPACE. The vault is the point: you can open it in Obsidian, edit a wrong line, and the next retrieval is correct.

4.2 Auto-fetch on a 20-minute tick

The constant lives in src/openhuman/composio/periodic.rs:

One global tick walks every active connection. Per-(toolkit, connection_id) state holds the cursor, last-sync, dedup set, and daily budget. Errors are swallowed so the loop never panics out.

The native registry today (src/openhuman/composio/providers/registry.rs::init_default_providers):

Auto-ingest covers Gmail, Notion, Slack only. The 118+ figure is the Composio catalog reach as proxied tools. Tool calls work everywhere, memory ingest fires on the three.

4.3 Integrations (native vs proxied)

Every connected service surfaces four ways: agent tool, memory source (native only), profile signal, trigger source (HMAC-verified webhooks).

23 toolkits ship as curated proxied tool sets without auto-ingest yet:

Shopify, Stripe, HubSpot, Salesforce, Airtable, Figma, GoogleCalendar, GoogleDrive, GoogleDocs, GoogleSheets, Discord, Telegram, WhatsApp, Microsoft Teams, Outlook, Linear, Jira, Trello, Asana, Dropbox, Twitter, Spotify, YouTube.

Three channels talk back: Telegram (two-way, 80+ actions), Discord (send/receive), Web (in-app local chat).

4.4 TokenJuice

A Rust port of vincentkoc/tokenjuice in the tool-execution path. Every tool result hits a rule overlay before it reaches an LLM. Three layers, later layers override earlier ones:

Builtin (shipped with the binary): git, npm, cargo, docker, kubectl, ls defaults.

User (~/.config/tokenjuice/rules/): personal overrides across every project.

Project (.tokenjuice/rules/): repo-specific overrides, checked in.

HTML → Markdown. Long URLs shortened. CJK and emoji preserved grapheme-by-grapheme. Project claim: up to 80% reduction in cost and latency. PrimeAIcenter measured ~70%. Realistic range: 70–80%, biggest wins on log-heavy and HTML-heavy payloads.

4.5 Model routing

One subscription brokers 30+ providers. The agent loop emits a hint: prefix per task. The router resolves it.

Top five hints:

hint:reasoning: strong reasoning model.

hint:fast: fast / cheap model.

hint:vision: vision-capable model.

hint:summarize: compression model.

hint:code: code-tuned model.

Lighter hints (hint:reaction, hint:classify, hint:sentiment, hint:medium, hint:tool_lite) prefer the local provider when Local AI is on. Heavy hints stay cloud. The task picks the model, not the user. Full hint reference in the appendix.

4.6 Local AI (optional, off by default)

Two flags switch it on:

Defaults: all-minilm:latest (~23 MB) for embeddings, gemma3:1b-it-qat (~700 MB) for summary-tree building. Heartbeat, learning, and subconscious can also move on-device. Chat, vision, STT, TTS, and web search stay cloud. “Local-first” means memory, not the whole stack.

4.7 Voice, mascot, and the Meet agent

The mascot lip-syncs to TTS and shifts through six mood states (idle, thinking, listening, talking, surprised, dreaming). The Meet agent joins Google Meet through an embedded CEF webview as a real participant: a name, a face, a tile in the grid.

Mid-meeting it can:

Listen. Inbound audio streams through STT, diarized per speaker, into the Memory Tree live.

Speak. Replies stream into the call as an outbound mic feed, not bounced through your speakers.

Animate. The mascot canvas is piped as the outbound camera, lip-synced to the TTS audio everyone else hears.

Use tools. Memory recall, auto-fetch, native tools, subconscious outputs, all reachable mid-call.

v0.54.0 added fully-local STT and TTS via Whisper and Piper. Prior path required ElevenLabs cloud for TTS.

4.8 Subconscious loop

A background tick (default 5 min, minimum 5 min) that loads due tasks, builds a situation report from memory plus workspace state, and returns one of three decisions:

Skip. Nothing relevant right now.

Act. Execute the task.

Escalate. Hand off to the cloud agent.

Local model evaluates, cloud agent escalates. Write tasks you asked for need no approval. Unsolicited writes open an approval card.

4.9 Skills (in transition)

The QuickJS / rquickjs runtime that executed skill packages was removed. Today’s skills surface is metadata-only:

Discover and parse SKILL.md files.

Resolve scope (User / Project / Legacy) and trust markers.

Install from URL (HTTPS only, no private hosts, .md only, max 1 MiB body).

Read resources (cap 128 KiB), uninstall, per-turn prompt injection (cap 8 KiB).

Registry repo: tinyhumansai/openhuman-skills. Runtime is being rebuilt. Treat skills as catalog + prompt-injection today, not a third-party plugin runtime.

What v0.54.0 shipped

Released 2026-05-19 07:17 UTC, the morning after the Product Hunt #1 post. 230 commits, 1,271 files changed against v0.53.43 six days earlier.

Voice. Fully-local STT and TTS via Whisper / Piper. Configurable mascot voice with ElevenLabs picker.

Memory. Optional agentmemory backend bridge: set memory.backend = “agentmemory” in config.toml and the Memory Tree shares a durable store with Claude Code, Cursor, Codex, and OpenCode. Plus MCP stdio memory server, NotebookLM-style folder ingestion, cross-chat context retrieval, per-(row, model) embedding storage.

Agents. Dedicated crypto_agent for wallet and market ops (#1397). Cursor Cloud Agents parallel workflow. Global tool registry. Task board CRUD. Gmail Unsubscribe Agent.

Integrations. Bring-your-own Composio direct mode (#1710). Seltz as direct-API search. Discord webview transcript ingestion. WeChat embedded webview.

Providers. Unified per-workload routing. LM Studio local provider support. New reasoning-quick-v1 route for low-latency chat.

UX and i18n. Onboarding redesign. Dark mode standardization. ~3,900 strings across nine locales. Italian and Indonesian added.

Security. Path traversal prevention in agent prompt loading. DNS-aware URL validation. Audio base64 max-size check. Self-repair for locked .secret_key on Windows. Linux AppImage NSS fix.

Local main is already past v0.54.0 at 0.54.2. Post-release: Polymarket integration (#2145), explicit user-preference tool (#2150), Ollama context-window gating (#2122).

OpenHuman vs Hermes Agent vs OpenClaw

6.1 The README’s own framing

6.2 What independent reviewers found

The May 2026 reviews land in roughly the same spot.

PrimeAIcenter (five-day test, Gmail + Notion + GitHub + Calendar): Memory Tree useful after three days, TokenJuice measured ~70% (not 80%), two sync failures in the window. Read on the Meet mascot: sounds gimmicky, isn’t.

TechTimes (May 16): framed OpenHuman as inverting the playbook, flagged three risks, piped-shell install as a supply-chain vector, OAuth aggregation across email, code, calendar, and payments, and no formal independent audit.

Julian Goldie (three-agent SEO test): OpenHuman wins on UI, setup, and voice. Hermes wins on long autonomous tasks. OpenClaw wins on scheduling.

HackerNoon (OpenClaw context): 138+ disclosed CVEs and 341 malicious ClawHub skills out of 2,857 scanned as of May 2026. Hermes: 3 CVEs. OpenHuman: no published CVEs, no skill marketplace today.

6.3 Pick which one

Three different shapes of the same problem. Pick by use case:

Pick OpenHuman if you want a desktop agent that reads your email, calendar, Slack, and Notion within minutes, plus a memory you can open as Markdown.

Pick Hermes Agent if you want an always-on server-side agent with a self-improving learning loop and six terminal backends (local, Docker, SSH, Daytona, Singularity, Modal) for long-running autonomous workflows.

Pick OpenClaw if you want a channel-heavy gateway agent across 20+ messaging surfaces with Git-versioned config. Audit the marketplace and skill set carefully given the recent CVE and ClawHub reporting.

How to Get Started

Here is the command you came for:

That single line installs OpenHuman on macOS or Linux. The full hint table, Local AI presets, native vs proxied list, and troubleshooting all live in the Reference Appendix at the end of this piece.

7.1 Pick an install path

Three options. Pick by tradeoff.

Option A: Download a signed binary (recommended for non-developers).

Go to tinyhumans.ai/openhuman and pick DMG (macOS), MSI or EXE (Windows), or AppImage / .deb (Linux). This avoids the piped-shell install path TechTimes flagged as a supply-chain risk vector.

Option B: One-line installer (recommended for the demo path).

macOS / Linux x64:

Windows PowerShell:

Option C: Build from source (for contributors).

Git, Node.js 24+, pnpm 10.10.0, Rust 1.93.0 + rustfmt + clippy, CMake, Ninja, ripgrep, plus your platform’s desktop build prerequisites.

7.2 First-run flow

Six steps. None of them require a terminal after step 1.

Launch the app. Sign in.

Click Connect on Gmail, Notion, or Slack. These are the three native providers that auto-ingest into the Memory Tree today.

Wait one auto-fetch tick (up to 20 minutes) or trigger a manual ingest from the Intelligence tab in the app.

Open the Obsidian vault at ~/.openhuman/wiki/ via the in-app deep link or any file browser.

Ask a context-heavy prompt: “What did I commit to in email last week?”

Open a chunk file in the vault before you trust the answer. The whole point is that the memory is readable. If something is wrong, fix the file, and the next retrieval is correct.

That is the golden path. Five minutes of real time, twenty minutes of wall-clock if you wait for the first sync tick.

7.3 (Optional) Turn on Local AI

Local AI is off by default. Two flags switch it on:

Then go to Settings → AI & Skills → Local AI and pick one of three presets:

Embeddings only. all-minilm:latest (~23 MB) for memory embeddings.

Memory + reflection. Embeddings + summary-tree building (gemma3:1b-it-qat, ~700 MB) + learning.

Everything local. All five workloads: embeddings, summary, heartbeat, learning, subconscious.

Hardware floor: 8 GB RAM minimum, 16 GB+ ideal. LM Studio is supported as the alternative provider with default base URL http://localhost:1234/v1.

Skip Local AI if you only have a few sources connected. The cloud path is faster and the privacy benefit is small in that case.

7.4 (Optional) Send the mascot into a Meet

Hand the mascot a Google Meet link from the desktop app.

It opens the embedded Meet webview, joins with the configured display name, switches its tile to the mascot canvas, and is now in the participant grid. The mic is the TTS injection stream (not your real microphone). The camera is the mascot frame producer (not your real webcam). Mute the agent’s mic from the app the same way you would mute yourself in Meet.

Required OS permissions: Camera, Microphone. On macOS, also Accessibility and Input Monitoring for desktop hotkeys.

7.5 (Optional) Bridge to agentmemory across other coding agents

If you already self-host agentmemory for Claude Code, Cursor, Codex, or OpenCode, set this in config.toml:

OpenHuman’s Memory Tree now proxies to that store. The same durable memory powers OpenHuman alongside the other four agents. This is new in v0.54.0.

7.6 Build from source (contributors)

Quality gates before opening a PR: pnpm typecheck, pnpm lint, pnpm format:check, cargo check -p openhuman --lib, pnpm test, pnpm test:rust. PRs need at least 80% coverage on changed lines or the merge gate blocks them.

7.7 Save this

Save the command. The full Reference Appendix below covers workspace structure, every model routing hint, the Local AI presets matrix, the native vs proxied integration list, and a troubleshooting table.

Current Limitations

Auto-fetch covers three integrations today. The 118+ headline is the Composio catalog reach, not the count of toolkits that auto-ingest into the Memory Tree. Today’s native providers: Gmail, Notion, Slack.

Local-first is not fully local. Memory Tree and the Obsidian vault are local. Default chat, vision, web search, integration OAuth proxying, and TTS streaming all go through the OpenHuman backend.

Skill execution is being rebuilt. The QuickJS runtime is gone. Today’s skills surface is metadata-only (discover, parse, install, uninstall, prompt injection). No executable third-party skill packages today.

80% token compression is a project claim. PrimeAIcenter measured around 70% in their five-day independent test. Realistic range: 70 to 80%, biggest wins on log-heavy or HTML-heavy payloads.

No published independent security audit. v0.54.0 adds meaningful hardening (path traversal prevention, DNS rebinding guard, bearer token redaction, Windows ACL self-repair), but the OAuth surface across email, code, calendar, and payments is wide and concentrated.

So the best recommendation is to install it this week if you are evaluating personal-agent UX or memory ingestion patterns, treat it as active beta for anything production-adjacent, and revisit auto-fetch coverage and the skill runtime in 60 days.

AlphaSignal Take

Verdict: Worth Watching.

The Memory Tree, the Obsidian vault, the 20-minute auto-fetch, and the v0.54.0 agentmemory bridge are real and source-verifiable. The caveats: only Gmail, Notion, and Slack auto-ingest today (not 118), and “local-first” applies to memory, not to LLM calls or OAuth proxying.

Not production-ready. 148 open issues, no published security audit, a skill runtime in transition, beta-grade onboarding bugs. What would change the verdict: native sync providers across the top ten integrations, a published audit, public pricing, and a stable skill runtime. Watch the v0.55 release.

Full breakdown of recent updates + daily signals in our newsletter (link in bio).

If OpenHuman is the third entrant after OpenClaw and Hermes Agent, which one are you actually running right now, and what made you pick it?

Reference Appendix

13.1 System requirements

RAM. 4 GB minimum. 8 GB recommended with Local AI. 16 GB+ for large mailboxes or full local AI.

Disk. ~500 MB for the binary. +23 MB for all-minilm, +700 MB for gemma3:1b-it-qat, several GB more for full mailbox memory.

OS. macOS 12+ (Apple Silicon or Intel), Windows 10+ (x64 or ARM64), Linux x64 with libssl.

macOS permissions. Camera and Microphone for the Meet agent. Accessibility and Input Monitoring for desktop hotkeys.

Build-from-source toolchain. Node.js 24+, pnpm 10.10.0, Rust 1.93.0 + rustfmt + clippy, CMake, Ninja, ripgrep.

13.2 Workspace structure

`<workspace>`/memory_tree/chunks.db: SQLite, holds chunks, scores, summaries, entity index, jobs, hotness.

`<workspace>`/wiki/: Obsidian-compatible Markdown vault.

~/.config/tokenjuice/rules/: User-level TokenJuice rule overrides.

.tokenjuice/rules/: Project-level TokenJuice rule overrides.

Defaults: `<workspace>` is ~/.openhuman. Override with OPENHUMAN_WORKSPACE.

13.3 Memory Tree internals

Leaf lifecycle.

The deep score decides admitted vs dropped. Admitted leaves enter a buffer (buffered). When the buffer seals, every leaf inside flips to sealed. Dropped leaves stop, the chunk row stays for provenance.

Job queue kinds.

extract_chunk: Deep score + entity extraction. Decides admitted vs dropped.

append_buffer: Adds an admitted leaf to the source (or topic) L0 buffer. May trigger a seal.

seal: Compresses an L0 buffer into an L1 summary. Cascades up if the parent is full.

topic_route: Routes a leaf into per-entity topic trees, gated by a hotness check.

digest_daily: Builds the global daily digest node.

flush_stale: Force-seals buffers that have been sitting too long.

Three background workers pick jobs. Semaphore caps concurrent LLM-bound calls. On startup, any job whose worker lease has expired (crash, kill) returns to the queue.

13.4 Model routing hints

hint:reasoning: strong reasoning model. Multi-step planning, math, code-heavy turns.

hint:fast: fast / cheap model. UI helpers, autocompletes, small classification.

hint:vision: vision-capable model. Screenshots, image attachments, OCR.

hint:summarize: compression model. Memory tree summary builders.

hint:code: code-tuned model. Native coder turns.

hint:reaction: lightweight model. Quick reactions.

hint:classify: lightweight model. Classification tasks.

hint:sentiment: lightweight model. Sentiment analysis.

hint:medium: medium model. Medium-complexity tasks.

hint:tool_lite: lightweight model. Lightweight tool calls.

Override globally in config.toml. Override per call by passing a concrete model name (no hint: prefix). Override per skill via the manifest.

13.5 Local AI presets

Embeddings only. Memory embeddings run local. Everything else stays cloud.

Memory + reflection. Embeddings, summary-tree building, and learning passes run local. Heartbeat and subconscious stay cloud.

Everything local. All five workloads run local: embeddings, summary-tree, heartbeat, learning, subconscious.

Models: all-minilm:latest (~23 MB) for embeddings, gemma3:1b-it-qat (~700 MB) for summary-tree building. Provider switch: local_ai.provider = “ollama” or local_ai.provider = “lm_studio”. Base URL override: local_ai.base_url.

13.6 Configuration reference

Environment variables.

OPENHUMAN_WORKSPACE: override default workspace path (default ~/.openhuman).

OPENHUMAN_CORE_TOKEN: per-launch bearer for HTTP JSON-RPC to the in-process core.

OPENHUMAN_CORE_REUSE_EXISTING=1: attach to an externally-started openhuman-core process.

OPENHUMAN_APP_ENV=staging: use the staging workspace at ~/.openhuman-staging/.

OPENHUMAN_LM_STUDIO_BASE_URL: override LM Studio endpoint (default http://localhost:1234/v1).

LM_STUDIO_BASE_URL: alias for the above.

GGML_NATIVE=OFF: disable -mcpu=native on macOS builds that fail.

RUST_LOG=openhuman_core::openhuman::tokenjuice=debug: trace TokenJuice rule matches and reductions.

Useful config.toml keys.

local_ai.runtime_enabled (default false): master switch for the local provider.

local_ai.opt_in_confirmed (default false): explicit opt-in. Bootstrap forces back to false until you re-opt.

local_ai.provider (default “ollama”): local provider, “ollama” or “lm_studio”.

local_ai.base_url (unset): provider URL override. LM Studio default http://localhost:1234/v1.

local_ai.usage.embeddings (default false): use local for memory embeddings.

local_ai.usage.heartbeat (default false): use local for the heartbeat loop.

local_ai.usage.learning_reflection (default false): use local for learning passes.

local_ai.usage.subconscious (default false): use local for the subconscious loop.

memory.backend (default “memory_tree”): switch to “agentmemory” to proxy to a self-hosted store.

composio.mode (default “tinyhumans”): switch to “direct” to use your own Composio v3 tenant.

13.7 Native vs proxied integrations

Native (auto-ingest into Memory Tree). Gmail, Notion, Slack.

Curated proxied (callable, no auto-ingest). Shopify, Stripe, HubSpot, Salesforce, Airtable, Figma, GoogleCalendar, GoogleDrive, GoogleDocs, GoogleSheets, Discord, Telegram, WhatsApp, Microsoft Teams, Outlook, Linear, Jira, Trello, Asana, Dropbox, Twitter, Spotify, YouTube.

Catalog reach (Composio). 118+ services via OAuth, a subset of the wider catalog.

13.8 Skill install constraints

Scheme: HTTPS only.

Hosts: private and local hosts rejected.

URL shape: GitHub blob URLs normalized, path must end in .md.

Max URL length: 2,048 chars.

Default fetch timeout: 60 seconds.

Max fetch timeout: 600 seconds.

Max SKILL.md body: 1 MiB.

Per-resource read cap: 128 KiB.

Per-turn injection cap: 8 KiB.

Writes are atomic.

Source: src/openhuman/skills/ops_install.rs, src/openhuman/skills/inject.rs, src/openhuman/skills/ops.rs.

13.9 Troubleshooting

First sync feels slow. Large mailboxes take hours on first ingest. Watch the Intelligence tab heatmap.

Locked .secret_key on Windows. v0.54.0 ships self-repair plus Windows ACL hints. Restart the app.

Linux AppImage will not launch on Arch or rolling distro. v0.54.0 excluded bundled NSS libs. Re-download.

Onboarding stuck after Google auth on Windows. Tracking as issue #2215, labeled priority: critical. Subscribe to the issue for the fix.

Sync failure on one integration. Per-connection state rebuilds on the next tick. A missed periodic sync is harmless.

macOS build fails with -mcpu=native. Set GGML_NATIVE=OFF before cargo check or cargo test.

13.10 Build-from-source quickref

Coverage gate on changed lines: ≥ 80%. CI enforces.

---

## [RAG and Long Context Aren't Enough for Agent Memory. δ-mem Is a Third Option](https://alphasignalai.substack.com/p/rag-and-long-context-arent-enough)
*📡 AlphaSignal | 2026-05-20*

δ-mem stores an LLM’s conversation history inside an 8×8 matrix and uses it to steer attention.

The backbone stays frozen. No prompt growth. No fine-tuning.

On Qwen3-4B-Instruct, that small matrix lifts the average score across five benchmarks from 46.79% to 51.66%, with 4.87M trainable parameters (0.12% of the model).

The adapter is public on Hugging Face under CC-BY-4.0. The arXiv paper landed on May 12, 2026.

For most agent workloads, RAG is overbuilt and longer context is wasteful. δ-mem suggests a third path.

What this article covers (~7 min read)

How δ-mem works in four steps, what it moves on five benchmarks, how to load the Qwen3-4B adapter in ten minutes, and where 64 numbers stop being enough. A reference guide for engineers sits at the end as an appendix.

Context

The research is authored by Mind Lab (Soujanya Poria’s group at NTU, with co-authors from Fudan University, Shanghai Jiao Tong, CUHK, and HKUST-GZ) and titled “δ-mem: Efficient Online Memory for Large Language Models.” Ten authors. arXiv submission on May 12, 2026.

The repo at declare-lab/delta-Mem has +100 GitHub stars at time of writing. The Hacker News thread has +230 points and +50 comments. The Hugging Face paper page has +110 upvotes.

The problem it’s pushing at: agents and long-running assistants need to reuse old information, and the three default answers all hit walls.

If your agent is still doing RAG on every turn, you’re paying token cost for retrieval noise on every turn. Longer context hits quadratic attention cost and context rot. LoRA-style adapters are static after training and can’t adapt to a live conversation.

δ-mem proposes a fourth path. It keeps a tiny memory state inside the model, updates it as new tokens arrive, and lets that state shape attention at runtime. The backbone weights never move.

How δ-mem works

δ-mem runs the same four steps at every token position. The frozen backbone runs its normal attention in parallel.

Step 1: Project

At a selected Transformer layer, δ-mem takes the current hidden state and projects it into three 8-dimensional vectors: a memory query, a memory key, and a memory value. The query and key go through tanh and L2 normalization. The value is a plain linear projection.

Step 2: Read

Multiply the previous 8×8 state by the current memory query. Out comes a small read vector. The state size is fixed, so this read cost is the same whether the conversation has 100 turns or 10,000.

Step 3: Steer

The read vector passes through two learned linear maps to produce a query-side correction and an output-side correction, each scaled by α/r (default 2). The corrected query goes into attention. The output-side correction is added after.

The key difference from LoRA: LoRA’s low-rank update is fixed after training. δ-mem’s correction comes from a state that changes every token, so the same parameters produce different steering effects under different histories.

Step 4: Write

After attention, the state updates with a gated delta rule borrowed from Qwen-Next’s gated retention. Three things happen in one update: keep part of the old state, erase the old prediction along the current key direction, and write the new value along that same direction. Two per-dimension gates (β for writes, λ = 1 − β for retention) control how much to overwrite versus retain.

Three write granularities

The paper studies three variants of step 4.

What it actually moves

On Qwen3-4B, an 8×8 matrix beats BM25 RAG by 7.1 points and Context2LoRA by 6.8 points. Same backbone. Same evaluator. Headline numbers from Table 1 of the paper:
In relative terms: 1.10× the frozen backbone, 1.15× the strongest non-δ-mem baseline (Context2LoRA), 1.31× on MemoryAgentBench, 1.20× on LoCoMo.

The most under-reported number in the paper: the Test-Time Learning subtask nearly doubles, 26.14 → 50.50. That’s the one to watch if you care about agents that learn during a session.

Cross-backbone, the biggest absolute jump isn’t on Qwen3-4B or Qwen3-8B. It’s on SmolLM3-3B, where MSW lifts the average from 26.08 to 36.96, a +10.88 point gain. Qwen3-8B goes from 47.20 to 50.86 with SSW. Smaller models benefit more from MSW because four parallel states reduce interference inside a single state.

GPU memory matches vanilla inference at every prompt length tested. Decoding throughput is the tradeoff: at 32k prompt and 64-token decode, vanilla runs 22.60 TPS and δ-mem TSW runs 13.68 TPS. The state read-and-write loop runs every step.

How to run it

Step-by-step setup below. For day-two patterns (preloading history, base-vs-δ-mem comparison, session save and resume, training your own adapter).

See the How to use it appendix at the end.

Clone and install:

You need Python 3.10 or newer, an NVIDIA GPU with CUDA PyTorch, and FlashAttention plus DeepSpeed for training. CPU is not the target path.

Download the adapter and load it in Python:

Important: δ-mem is not a standard PEFT adapter. Do not load it with PeftModel. Do not call merge_and_unload(). The runtime read/write path is part of model execution.

Run the chat demo:

Inside the demo, /reset clears the state, /stats prints state statistics, and /save_session `<dir>` plus /load_session `<dir>` checkpoint the state to disk.

Once the chat demo loads, the How to use it appendix covers the engineering patterns most teams need next.

Current Limitations

Adapter coverage. The only public adapter today is Qwen3-4B-Instruct TSW. The Qwen3-8B and SmolLM3-3B variants need to be retrained from the repo. That means 8× A800 GPUs in the paper’s recipe and a memory-heavy training set.

Decoding overhead. δ-mem TSW runs about 40% slower than the base model at 32k prompt and 64-token decode (13.68 TPS versus 22.60 TPS). The state read-and-write loop runs at every step. GPU memory stays flat.

Context recovery is partial. When the original context is removed and only the compressed state is injected, HotpotQA EM goes from 0.08% to 6.48%. That’s real signal, not full recall. The state cannot replace explicit context for retrieval-style tasks.

Not standard PEFT. The adapter requires a custom runtime path. Standard shortcuts like PeftModel.from_pretrained and merge_and_unload() will not work. CPU-only inference is not supported.

AlphaSignal Take

The sharpest critique on Hacker News (236 points, 59 comments) was a capacity question. One commenter put it plainly: “This doesn’t solve the capacity problem of memory...there’s a fundamental limit on how much information can go into it.”

The paper’s answer is partial. The no-context recall ablation shows the 8×8 state carries usable signal (HotpotQA EM rises from 0.08% to 6.48%, LoCoMo from 3.49 to 8.05). But the absolute floor is low.

This is the line most engineers will miss: an 8×8 state is a steering signal, not a fact store. Treat it like one or it’ll bite you.

The right pattern is to pair δ-mem with retrieval. Use the state to steer the model on what the user has been talking about. Keep exact facts, policies, and audit trails in a search index or vector store. So the best recommendation is to prototype with the released Qwen3-4B adapter and treat the state as an attention bias, not a fact database.

The next thing to watch is a Qwen3-8B δ-mem adapter on Hugging Face. The cross-backbone results already show SSW wins on 8B, and an official adapter at that scale would double the practical surface area of δ-mem overnight.

Who benefits and who doesn’t

This is for ML engineers prototyping memory-heavy agents, researchers comparing latent memory against RAG and LoRA, and developers running Qwen3-4B-class models on a single GPU who want history-conditioned behavior without growing the prompt.

It is not for teams that need auditable retrieval (citations, deletion, exact match), teams without NVIDIA GPUs, teams whose conversations fit comfortably inside a long-context window, or teams that need a larger-model adapter today.

Practitioner Implication

Most teams will not train this from scratch. The real test is whether the released Qwen3-4B adapter beats your current RAG baseline by Friday, without growing the context window or fine-tuning the backbone.

Links

[arXiv paper](https://arxiv.org/abs/2605.12357) (paper, ~25 min read)

[GitHub repo](https://github.com/declare-lab/delta-Mem) (repo, ~10 min setup)

[Hugging Face adapter](https://huggingface.co/declare-lab/delta-mem_qwen3_4b-instruct) (Qwen3-4B TSW)

Follow @AlphaSignalAI for more content like this.

Subscribe at [AlphaSignal.ai](https://alphasignal.ai/) for daily AI signals. Read by 300,000+ subscribers.

Questions?

Q: What is δ-mem? A: A memory mechanism that adds a small 8×8 matrix alongside a frozen LLM and uses its readout to inject low-rank corrections into the model’s attention. It stores history as a latent state, not as retrieved text.

Q: Does δ-mem replace RAG? A: No. δ-mem does not retrieve documents and cannot produce citations. The cleanest stack for an agent pairs δ-mem with a retrieval index. The state handles steering. The index handles exact recall.

Q: How big is δ-mem’s memory state? A: A single 8×8 matrix by default (rank 8, 64 entries). The MSW variant keeps 4 parallel 8×8 states. Trainable parameter cost is 4.87M for TSW or SSW (0.12% of the Qwen3-4B backbone), 19.47M for MSW.

Q: Can developers use δ-mem today? A: Yes, on Qwen3-4B-Instruct. The official Qwen3-4B TSW adapter is on Hugging Face under CC-BY-4.0. The repo targets NVIDIA GPUs with bfloat16, FlashAttention, and DeepSpeed.

Q: What are the main limitations? A: Public adapter coverage is narrow (Qwen3-4B TSW only), decoding is about 40% slower than the base model at 32k context, the adapter is not standard PEFT, and no-context recall is still low in absolute terms.

Where do you put memory in your agent stack today? Prompt, vector store, fine-tune, or something else? Which one would you swap out for δ-mem first?

Appendix: how to use it

A reference guide for teams that already cleared the chat demo. Skim once, return to specific sections as needed.

A.1 Mental model

δ-mem is an in-process side-state, not a database. The state matrix lives inside the model object, persists across model.generate() calls in the same Python process, and resets when you re-attach. There is no separate process and no network hop.

One state matrix is allocated per attached layer per state head, all on the same GPU as the model.

A.2 Preloading history into the state

The most common day-one mistake is forgetting that δ-mem only sees what passes through forward(). To preload history, run the historical context through the model in a context-only pass before the user’s first real query. The state advances. The output is discarded.

The paper trained with an 8,192-token write budget per example. Inference is not hard-capped at that length, but the trailing tokens dominate the state.

A.3 Verifying the state is actually doing something

Three quick checks.

First, run the demo in MODE=base and compare answers on the same prompts. If responses look identical to δ-mem mode, the adapter is not attached or model.eval() was skipped.

Second, use /stats in the chat demo or call collect_delta_mem_state_stats() in Python. The state should be non-zero within the first few tokens of context.

Third, run one short benchmark and confirm the result lands near the paper’s headline. For Qwen3-4B TSW, that’s roughly 51.66% average across the five-eval suite.

A.4 Session save and resume

Use /save_session `<dir>` and /load_session `<dir>` inside the chat demo, or the equivalent Python helpers, to checkpoint and restore the state across processes. The save captures the exact state matrix at that point in the conversation.

A saved session is tied to the base model it came from. Loading a Qwen3-4B session into a different base will fail.

A.5 Benchmarking against your current memory stack

Run the same task three ways with the same evaluator: base + RAG, base + long context, base + δ-mem. The bundled suite at scripts/run_qasper_multimodel_write8192_benchmark_suite.sh runs all five evals.

To scope it to one task and one variant:

For reference, on Qwen3-4B the paper reports BM25 RAG 44.56 avg, Context2LoRA 44.90 avg, and δ-mem TSW 51.66 avg.

A.6 Choosing TSW, SSW, or MSW

The cross-backbone results give the rule of thumb.

TSW wins on Qwen3-4B (51.66 avg). Pick it when local detail matters and the model is mid-sized.

SSW wins on Qwen3-8B (50.86 avg). Pick it when token-level noise drags the state and the model has more reasoning to spare.

MSW wins on SmolLM3-3B (36.96 avg) and on memory-heavy benchmarks. Pick it when interference between memory types matters more than per-token detail.

Only TSW is on Hugging Face today. SSW and MSW need the training script.

A.7 Cost reality

GPU memory at inference matches vanilla at every prompt length tested. At a 32k-token prompt, δ-mem’s footprint lands on the same value as the base model in the paper’s table, with no measurable overhead from the state.

Decoding throughput is ~40% slower than base at 32k prompt and 64-token decode (22.60 → 13.68 TPS).

Trainable parameters: 4.87M for TSW or SSW (0.12% of Qwen3-4B), 19.47M for MSW (0.48%).

Training in the paper used 8× A800 GPUs, bfloat16, DeepSpeed ZeRO-2, fused AdamW, peak LR 2e-4, one epoch on the shortest 2,219-sample QASPER split, effective batch size 32.

A.8 Training your own adapter

The realistic floor is multi-GPU bf16. The paper’s exact recipe was 8× A800, but the script supports fewer devices through DeepSpeed.

Training data should be memory-heavy SFT examples where the context tokens carry the signal that the model needs at response time. QASPER fits because the question is short and the supporting context is long.

Per-backbone scripts exist for Qwen3-8B and SmolLM3-3B.

A.9 Compatibility constraints

Not a PEFT adapter. Never load with PeftModel. Never call merge_and_unload().

GPU-only target path. CPU is not supported.

Released adapter is fixed to Qwen/Qwen3-4B-Instruct-2507. Other Qwen versions are not guaranteed.

Adapter files are delta_mem_adapter.pt and delta_mem_config.json. Do not rename.

The required load path is deltamem.core.attach_delta_mem followed by load_delta_mem_adapter. Standard AutoModel.from_pretrained(adapter_dir) will not work.

A.10 When to reach for δ-mem versus an alternative

Reach for RAG or vector search when you need exact retrieval, citations, deletion, or an audit trail.

Reach for longer context when the full history fits in budget and latency is acceptable.

Reach for δ-mem when you want online, history-conditioned steering without fine-tuning the backbone or growing the prompt.

These are not mutually exclusive. The cleanest agent stack is δ-mem on the model and a retrieval index on the side.

---

## [11 Open-Source Repos Every AI Infra Engineer Should Bookmark](https://alphasignalai.substack.com/p/11-open-source-repos-every-ai-infra)
*📡 AlphaSignal | 2026-05-19*

You built an AI agent this weekend.

It writes code.
Browses the web.
Uses MCP tools.
Maybe even touches production data.

Now ask yourself:

What isolates it from the host?

What stops credential leaks?

Who controls tool permissions?

What happens after prompt injection?

Where is the audit trail?

Most AI engineers answer these questions after the first incident.

Meanwhile, open source quietly built an entire infrastructure and security stack for AI agents.

Here are 11 repos every AI infra engineer should bookmark:

Each one covers a gap that frameworks don’t.

Open Source AI Agent Infrastructure & Security

1. ProjectRecon/awesome-ai-agents-security

Living Map of the AI Agent Security Ecosystem

What it does: Curated, maintained index of the AI agent security ecosystem, organized by security lifecycle: red teaming, runtime protection, sandboxing, governance, middleware.

Everything categorized, linked, and kept current. The starting point when you need to understand the full landscape or find tools for a specific security problem.

Why it matters for AI infra: This space moves faster than any single article. This repo is the durable index. Watch it. The delta between its last commit and today is your reading list.

🔗: https://github.com/ProjectRecon/awesome-ai-agents-security

2. promptfoo/promptfoo

Automated Red Teaming and Evals for LLM Applications

What it does: The standard framework for automated LLM red teaming, security testing, and model evaluation.

Covers prompt injection, jailbreaks, PII leakage, model regression, and multi-model performance comparison across GPT, Claude, Gemini, Llama, and more. Declarative YAML configs. Native CI/CD integration. Used internally by OpenAI and Anthropic. MIT licensed, fully open source.

Why it matters for AI infra: You test your code before shipping. You should test your prompts and agent security boundaries too. Promptfoo makes red teaming systematic, scriptable, and integrated into your existing CI pipeline. Shipping agent features without automated security evals is the equivalent of shipping code without tests.

🔗: https://github.com/promptfoo/promptfoo

3. aquasecurity/trivy

Supply Chain Vulnerability Scanner for AI Infrastructure

What it does: All-in-one vulnerability scanner for container images, git repos, and filesystems.

One tool catches: vulnerable base images, misconfigured Terraform, insecure Kubernetes manifests, leaked secrets in git history, vulnerable application dependencies. SARIF output feeds directly into the GitHub Security tab. 10 lines of YAML for GitHub Actions integration.

Why it matters for AI infra: You can write perfect agent code and still ship a vulnerable base image or misconfigured infrastructure module. Supply chain attacks are the dominant attack vector now. Trivy catches them in CI before they reach production. It’s automated, with zero manual review overhead.

🔗: https://github.com/aquasecurity/trivy

4. open-policy-agent/opa

Policy-as-Code for AI Agent Infrastructure

What it does: Universal policy engine for your entire stack. Express security policy as readable, testable Rego code.

Kubernetes admission control, API authorization, infrastructure configuration validation, one engine. Decouple security policy from application code. Write once, enforce everywhere. When your AI agent calls a tool, hits an API, or requests a resource and OPA decides whether it’s allowed.

Why it matters for AI infra: OPA isn’t agent-specific, which is exactly why it belongs here. Your agent infrastructure sits inside your existing cloud stack. OPA gives you a consistent, auditable policy layer that spans both traditional infrastructure and agentic workloads without maintaining two separate security systems.

🔗: https://github.com/open-policy-agent/opa

5. AgentGateway (Linux Foundation)

RBAC Proxy for MCP and A2A Agent Protocols

What it does: AI-native proxy for A2A and MCP protocol traffic. RBAC, observability, and policy enforcement on agent-to-tool interactions.

Donated to the Linux Foundation. Sits between your agents and their tools. Only the right agents can call the right tools with the right permissions. Full observability on the protocol layer.

Why it matters for AI infra: MCP is the emerging standard for agent-tool connectivity. Most teams wire MCP directly with no access control layer, a significant and growing attack surface. AgentGateway is the purpose-built solution. Linux Foundation stewardship means production-grade stability and long-term maintenance.

🔗: https://github.com/agentgateway/agentgateway

6. microsoft/agent-governance-toolkit

Runtime Security Middleware for AI Agents

What it does: Runtime policy engine mapped directly to the OWASP Agentic AI Top 10.

When [OWASP](https://genai.owasp.org/) published the first formal taxonomy of agentic AI risks listing goal hijacking, tool misuse, identity abuse, rogue agents Microsoft shipped a toolkit that addresses every single one. Sub-millisecond governance latency (<0.1ms p99). Deploys as a sidecar container or middleware layer.

Goal hijacking → semantic intent classifier

Tool misuse → capability sandboxing + MCP security gateway

Memory poisoning → Cross-Model Verification Kernel with majority voting

Rogue agents → ring isolation, trust decay, automated kill switch

Why it matters for AI infra: The [EU AI Act’](https://artificialintelligenceact.eu/)s high-risk AI obligations take effect August 2026. The Colorado AI Act enforces January 2027. Agentic AI governance is moving from best practice to legal requirement. This is the most comprehensive open source implementation aligned with the formal risk taxonomy.

🔗: https://github.com/microsoft/agent-governance-toolkit

7. anthropics/claude-code-security-review

AI-Powered PR Security Review

What it does: GitHub Action that runs Claude Code on every pull request and posts security findings as inline review comments.

Diff-aware: only analyzes changed files. Semantic reasoning, not pattern matching, to identify high-confidence, exploitable vulnerabilities. Calibrated false positive filtering: no theoretical issues, no rate-limiting noise. Just vulnerabilities a senior security engineer would flag in review.

One YAML file to add to any repository.

Why it matters for AI infra: Security review is the step most teams skip because it’s expensive and slow. This makes it automatic and free on every PR. The semantic analysis quality using actual LLM reasoning rather than regex, catches logic-level security issues that static analysis tools miss entirely.

🔗: github.com/anthropics/claude-code-security-review

8. vercel-labs/deepsec

Agent Powered Vulnerability Scanner

What it does: An AI agent that scans your entire codebase for vulnerabilities that have been sitting there for years.

Fast regex matchers find candidates, the Claude/Codex investigates at maximum thinking levels. Work fans out across parallel workers for large single repos. You can interrupt or restart the jobs, it picks up where it left off.

Why it matters for AI infra: Every other tool on this list protects agents at runtime. Deepsec goes one layer earlier. It clears the vulnerabilities already living in the codebase your agents will read, modify, and deploy.

🔗: https://github.com/vercel-labs/deepsec

9. dagger/container-use

Containerized Environments for Coding Agents

What it does: Persistent, isolated container environments for coding agents.

From the Dagger team. Each coding agent gets its own container. Multiple agents run in parallel without conflict. Environments persist across sessions. Resume any task mid-flight with an existing env ID.

The differentiator: full OpenTelemetry instrumentation on every agent run. Every LLM decision, tool call, error, and retry appears in the build trace. When something goes wrong, you don’t guess, you see it.

Why it matters for AI infra: “It works on my machine” is not a deployment model. Container Use brings the isolation and reproducibility guarantees that containerization gave to software builds to agent execution. The observability layer alone makes debugging agentic systems tractable.

🔗: https://github.com/dagger/container-use

10. meta-llama/PurpleLlama/LlamaFirewell

Prompt Injection Defense for LLM Agents

What it does: Meta’s open source guardrail system for LLM agents. Blocks prompt injection, scans LLM-generated code for vulnerabilities, detects misaligned reasoning.

A single prompt injection can flip an agent’s intent cause it to leak private data, execute unauthorized commands, operate far outside scope. LlamaFirewall sits at the application layer and intercepts this before it reaches execution. It also scans code the agent generates for critical vulnerabilities before shipping to production, a gap most guardrail systems ignore entirely.

Open-weight guardrail models on HuggingFace. Run on your own infrastructure at 50–100ms latency. No API calls. No data leaving your environment.

Why it matters for AI infra: Prompt injection is the SQL injection of the agentic era. It’s being exploited in production systems today. LlamaFirewall is the most rigorous open source defense available, built by a security team that has worked through the actual LLM agent threat model.

🔗: https://github.com/meta-llama/PurpleLlama/tree/main/LlamaFirewall

11. microsandbox/microsandbox

Self-Hostable AI Code Execution Sandbox

What it does: Open source, self-hostable alternative to E2B for AI agent code execution. Multi-language SDKs. Hardware-level isolation.

Docker and Kubernetes runtimes. gVisor, Kata Containers, and Firecracker isolation layers, pick the isolation level that matches your threat model. Multi-language SDK support. CNCF Landscape project.

Why it matters for AI infra: Not every team wants an external SaaS dependency in their agent execution path. Microsandbox gives you the same isolation guarantees inside your own infrastructure, with no external API in the hot path, and with full control over your data residency.

🔗: https://github.com/superradcompany/microsandbox

The Bigger Shift

Most teams still think of AI agents as applications.

The infrastructure ecosystem increasingly treats them as autonomous systems that require isolation, observability, security, and governance.

That shift is changing how AI systems get deployed in production.

And increasingly, it is becoming mandatory.

The EU AI Act enters full enforcement on August 2, 2026 with high-risk AI system obligations, transparency requirements, penalties up to €35M or 7% of global turnover

[Colorado’s replacement AI law](https://www.forbes.com/sites/alonzomartinez/2026/05/15/colorado-rewrites-its-ai-law-before-it-takes-effect/) is heading to the Governor’s desk now, with a January 2027 effective date. Every version of every bill, in every jurisdiction, requires the same things: documentation, audit trails, risk management, human oversight. The exact same artifacts this infrastructure stack produces.

The teams building this layer now will not only ship safer systems. When the compliance conversation arrives from customers, auditors, regulators, or enterprise buyers, they will have artifacts to show instead of promises to make.

The next generation of AI companies will not only build better models or better prompts.

They will build the infrastructure required to operate autonomous systems safely at scale.

Thanks for reading!

Follow [@AlphaSignalAI](https://x.com/AlphaSignalAI) for more content like this.

Check out [AlphaSignal.ai](http://alphasignal.ai/) to get a daily summary of top models, repos, and papers in AI. Read by 300,000+ devs.

---

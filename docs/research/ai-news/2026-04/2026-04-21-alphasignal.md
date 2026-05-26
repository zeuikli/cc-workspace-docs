---
title: AlphaSignal — 2026-04-21
date: 2026-04-21
source: AlphaSignal
type: ai-news
---

# 📡 AlphaSignal — 2026-04-21

> 200k+ 訂閱；最新 AI 研究 / repos / 模型的 5 分鐘技術日報
> 來源：[AlphaSignal](https://alphasignalai.substack.com/feed)

---

## [A Closer Look at Harness Engineering from Top AI Companies](https://alphasignalai.substack.com/p/a-closer-look-at-harness-engineering)
*📡 AlphaSignal | 2026-04-21*

In February 2026, OpenAI quietly published a [blog post](https://openai.com/index/harness-engineering/) that changed how a lot of us think about software engineering. The title was just two words: “Harness Engineering.”

The post described a small team that shipped a million lines of production code without typing any of it by hand. They didn’t write the code. They designed the environment the agents wrote it inside: the rules, the feedback loops, the docs structure, the dependency order. The agents did the coding. The humans built the scaffolding that made the agents reliable.

A few weeks later, Anthropic dropped three engineering [papers](https://www.anthropic.com/engineering/harness-design-long-running-apps) on the same idea. ThoughtWorks also [published a framework](https://martinfowler.com/articles/harness-engineering.html) about harness engineering.

The numbers explain why everyone is paying attention. LangChain tested the same model on Terminal Bench 2.0 twice. Same weights, different harness. The score moved from 52.8% to 66.5%. Vercel did the opposite thing and deleted 80% of their agent’s tools. Performance went up, not down.

We’ve also discussed in a similar post why the technical and economic moat in AI is shifting to “harness engineering.” You can read about it in the post below.

If 2025 was the year agents proved they could write code, 2026 is the year we figured out that the agent was never really the hard part.

What a harness actually is

[Vivek Trivedy at LangChain](https://blog.langchain.com/the-anatomy-of-an-agent-harness/) wrote down the cleanest definition so far:

“If you’re not the model, you’re the harness.”

That’s it. Everything around the model is the harness. System prompts. Tools. Middleware hooks. The file system the agent reads from. The documentation it sees at boot. The verification loops that catch mistakes before they ship.

If you’ve used Claude Code, Cursor, or Codex, you’ve been using a harness. The question is whether you’re building one deliberately.

The evidence this matters is unusually concrete. LangChain [kept GPT-5.2-Codex fixed](https://blog.langchain.com/improving-deep-agents-with-harness-engineering/) and only modified the harness around it. On Terminal Bench 2.0, the same model climbed from 52.8% to 66.5%. From outside the top 30 to rank 5.

They also found that maxing out reasoning effort at every stage scored the worst (53.9%). A “reasoning sandwich” (high reasoning for planning, reduced for building, high again for verifying) scored 66.5%. More reasoning wasn’t better. The harness had to be choosy about when to spend it.

OpenAI: push everything into the repo

OpenAI’s Codex team hit a problem that kept getting worse as it scaled. Their agents were writing everything. Application logic, tests, CI configs, docs, internal tooling. A million lines across five months, with zero written by human hands.

At that scale, the old review loop falls apart. Three engineers can’t meaningfully read a million lines of code. What they can do is shape the environment well enough that whatever the agents produce is reviewable in the first place.

[Ryan Lopopolo’s writeup](https://openai.com/index/harness-engineering/) summarized the lesson as giving Codex a map, not a manual.

The agent doesn’t need more instructions. It needs a world where the right thing to do is obvious and the wrong thing is hard.

In practice, that meant encoding architectural rules as code, not prose. Strict dependency flows (Types, then Config, then Repo, then Service, then Runtime, then UI). Structural tests that fail the build if a layer imports from the wrong direction. AGENTS.md files embedded throughout the repo as distributed documentation, one per module. Every change running through CI automatically.

The linters themselves were written by Codex.

The philosophy shakes out to one line: design the environment thoroughly, then let the agent work inside it. The human becomes the architect, not the coder.

The proof showed up in the Sora Android build. Four engineers, 28 days, an app that hit #1 on the Play Store with a 99.9% crash-free rate. Codex handled 70% of internal pull requests weekly.

Anthropic: decouple the brain from the hands

Anthropic’s problem was different.

Their agents could write code fine. What they couldn’t do was evaluate their own work honestly. Ask the agent if the output was good and it would say yes, even when the output was obviously broken to any human watching.

Their fix was inspired by GANs. Separate the thing doing the work from the thing judging it. A Planner turns a short prompt into a real spec. A Generator implements one feature at a time. An Evaluator uses Playwright to interact with the running app like an actual user and grades the work against explicit criteria.

On April 9, Anthropic [launched Claude Managed Agents](https://www.anthropic.com/engineering/managed-agents) as a public beta. They call it a “meta-harness.”

The idea is that instead of shipping one opinionated harness, they ship the interfaces any harness needs. The brain (Claude) is decoupled from the hands (a secure sandbox) which are decoupled from the session (a durable event log). Crash the brain and it recovers from the log. Lose a sandbox and it surfaces as a tool error instead of a system failure.

Internal testing showed structured file generation tasks improving by up to 10 points over standard prompting loops, with the [biggest gains on the hardest problems](https://www.helpnetsecurity.com/2026/04/09/claude-managed-agents-bring-execution-and-control-to-ai-agent-workflows/).

ThoughtWorks: classify before you build

ThoughtWorks didn’t ship a system. They shipped a vocabulary.

Birgitta Böckeler’s framework puts every harness control on two axes. Is it a guide (applied before the agent acts) or a sensor (applied after)? Is it computational (a linter or test, runs in milliseconds, deterministic) or inferential (another LLM checking the first one’s work, slower, semantic)?

This sounds academic until you try to audit a real harness.

Most teams discover they have three computational sensors (tests, linters, CI) and no computational guides at all. Or they have inferential guides everywhere and nothing checking whether the guides actually worked. Feedforward-only harnesses never validate themselves. Feedback-only harnesses let the agent repeat the same mistakes.

You need both axes, layered. That’s the whole point of the framework.

ThoughtWorks also introduced the idea of “harnessability.” Strongly-typed languages, clear module boundaries, and well-structured frameworks make agent work inherently more reliable. If you’re picking a tech stack for a greenfield project right now, that matters more than it used to.

The weakness, which ThoughtWorks admits, is that today’s tools are fine at checking maintainability but weak at confirming whether the agent actually did what was asked. Behavior verification is the frontier nobody has really cracked.

Where each approach breaks

None of these three is a universal answer.

OpenAI’s approach scales to huge codebases because the constraints live in the repo itself. It struggles on greenfield projects where the architecture hasn’t settled yet. Tests catch whether code is correct, not whether it’s a good design choice.

Anthropic’s multi-agent approach catches quality issues that tests alone miss, but it costs more and takes longer. Their published comparison showed a solo agent producing a broken demo for $9, and the full managed harness producing working software for $200. Whether 22x is worth it depends entirely on what broken output costs you.

ThoughtWorks’ framework is a blueprint, not a building. It tells you what kinds of controls exist. It doesn’t tell you which specific tools to wire together or how much each one is worth. For teams that want turnkey, this isn’t it.

What Opus 4.7 just did to the playbook

Opus 4.7 [shipped on April 16](https://platform.claude.com/docs/en/release-notes/overview) with real benchmark gains. SWE-bench Verified went from 80.8% to 87.6%. CursorBench from 58% to 70%.

But the line that matters most for harness design is in Anthropic’s release notes:

“Opus 4.7 handles complex, long-running tasks with rigor and consistency, pays precise attention to instructions, and devises ways to verify its own outputs before reporting back.”

Self-verification.

That single sentence puts pressure on a big piece of the playbook. A lot of teams built separate evaluator agents specifically because the model couldn’t critique its own work. If 4.7 can, the evaluator is carrying less weight than it was two weeks ago.

LangChain [saw this coming](https://blog.langchain.com/the-anatomy-of-an-agent-harness/). They wrote that harness components are a bet on what the model can’t do yet, and “as models get more capable, some of what lives in the harness today will get absorbed into the model.”

That’s the uncomfortable part of building in this space. Whatever harness you build today, some of it will become dead weight in two months.

What’s your take? Are you building a harness deliberately, or is your agent running on whatever defaults it came with? Drop your thoughts in the comments.

Join 250k+ developers staying ahead in AI. We curate the latest models, repos, and research — so you don’t miss what matters: [AlphaSignal.ai](http://alphasignal.ai/)

---

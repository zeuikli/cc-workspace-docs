---
title: Chain of Thought — 2026-05-24
date: 2026-05-24
source: Chain of Thought
type: ai-news
---

# ⛓️ Chain of Thought — 2026-05-24

> Dan Shipper（Every.to）的 AI 與策略 / 社會交點深度週報
> 來源：[Chain of Thought](https://every.to/chain-of-thought/feed.xml)

---

## [Inside Anthropic’s 2026 Developer Conference](https://every.to/chain-of-thought/inside-anthropic-s-2026-developer-conference)
*⛓️ Chain of Thought*

by [Dan Shipper](https://every.to/@danshipper), [Marcus Moretti](https://every.to/@marcus_fd8302_1), and [Katie Parrott](https://every.to/@katie.parrott12)in [Chain of Thought](https://every.to/chain-of-thought)Midjourney/Every illustration.
Was this newsletter forwarded to you? [Sign up](https://every.to/account) to get it in your inbox.

To our surprise, the biggest launch from Anthropic’s [developer conference](https://claude.com/code-with-claude) in San Francisco yesterday wasn’t a model or a feature. Instead, it was the company’s announcement of [a deal with SpaceX](https://www.anthropic.com/news/higher-limits-spacex) to allocate all of the capacity in the latter’s Colossus supercluster to Claude.

Anthropic has been riding a historic demand surge over the last year as Claude Code opened up a new wave of agentic coding for engineers and non-engineers alike. But compute constraints have caused friction even amongst its most die-hard fans—we’ve written previously about [being frustrated](https://every.to/context-window/get-your-hands-dirty#signal) with its OpenClaw restrictions and the speed of its latest models like [Opus 4.7](https://every.to/vibe-check/opus-4-7).

The deal with SpaceX changes that equation. Anthropic has already doubled rate limits for subscription plans, removed peak-hour limits on Pro and Max accounts, and raised API rate limits by as much as almost 17 times for certain tiers.

Other than that, the big story is Claude Managed Agents, Anthropic’s hosted agent product. The company released [three new features](https://claude.com/blog/new-in-claude-managed-agents):

Multi-agent orchestration: a coordinator agent that spins up subagents in parallel baked into the platform

Dreaming: Anthropic’s general-purpose version of [compound engineering](https://every.to/guides/compound-engineering), a feature that allows agents to learn from past sessions to improve between runs

Outcomes: Anthropic’s answer to Codex’s /goals command, allowing developers to specify an outcome and run an agent in a loop until the outcome is achieved

By themselves, these features are nice but not groundbreaking. What’s more important is that what an AI platform is has changed. In the GPT-3 days, the platform was a text completion end-point: Send text in, get text out. Now, with Claude Managed Agents, the platform is an AI model with a harness and host computer—all provided with unlimited scaling by the model companies.

[Cora](https://cora.computer) general manager [Kieran Klaassen](https://every.to/@kieran_1355) and I reported live from conference with our biggest takeaways, including the xAI compute deal, doubled Claude usage limits, Claude Managed Agents, and why the battle lines between OpenAI and Anthropic are starting to become clearer. Watch now:

[

](https://www.youtube.com/watch?v=4YNHb0XNV1A)

We also recorded a conversation with Angela Jiang, head of product for the Claude platform, and Katelyn Lesse, head of platform engineering. The full episode drops tomorrow on [AI & I](https://every.to/podcast)—highlights below.—[Dan Shipper](https://every.to/@danshipper)

Vibe Check: Claude Managed Agents 

Spiral general manager Marcus Moretti uses the platform’s new features

Anthropic launched Claude Managed Agents in April, and since then, Every’s AI writing tool [Spiral](https://writewithspiral.com/) has used the platform to power its API and command line interface (CLI), which lets developers and other agents talk to Spiral outside the web app. Claude Managed Agents run on Anthropic’s servers, instead of us having to run them on our own.

We set up a new Managed Agent in an afternoon and [deployed it to power our API](https://every.to/context-window/the-missing-layer-in-ai-adoption#spiral-is-experimenting-with-agent-to-agent-workflows) the next day. We’ve incorporated two of the new features Anthropic announced yesterday (memory and multi-agent orchestration) and are deploying the third (outcomes) soon.

Memory: Every’s editorial and social expertise—how to write a good X post, for example—lives in...

Become a [paid subscriber to Every](https://every.to/subscribe) to unlock this piece and learn about:

How Spiral is already using the new features announced this week

How Claude’s new “Dreaming” feature takes a page out of compound engineering

Why Anthropic says building a model-agnostic harness is a losing strategy

[Subscribe](https://every.to/subscribe?source=post_button)

[Click here](https://every.to/chain-of-thought/inside-anthropic-s-2026-developer-conference) to read the full post

Want the full text of all articles in RSS? [Become a subscriber](https://every.to/subscribe), or [learn more](https://every.to).

---

## [When Your Vibe Coded App Goes Viral—And Then Goes Down](https://every.to/chain-of-thought/when-your-vibe-coded-app-goes-viral-and-then-goes-down)
*⛓️ Chain of Thought*

by [Dan Shipper](https://every.to/@danshipper)in [Chain of Thought](https://every.to/chain-of-thought)Midjourney/Every illustration.
Was this newsletter forwarded to you?[ ](https://every.to/account)[Sign up](https://every.to/account) to get it in your inbox.

At 4 a.m. on the day after we launched our [agent-native](https://every.to/guides/agent-native) document editor, [Proof](https://proofeditor.ai), I watched yet another [Codex](https://every.to/vibe-check/codex-vibe-check) agent try to revive our server. 

Over 4,000 documents had been created since launch, but the app had been mysteriously crashing all day. This left users with crucial documents that they couldn’t access, and me with egg on my face.

I hadn’t slept for almost 24 hours, and all I could do was nervously munch trail mix as Codex investigated yet another bug buried deep in a codebase that I didn’t understand. It felt less like programming and more like being the dumbest participant at a math Olympiad. Needless to say, I was reconsidering my life choices. 

Today, almost a week later, Proof is more or less stable. And I’ve learned a lot about both building and launching a purely vibe coded app. Perhaps more importantly, I’ve also learned what happens once that app goes live—and then goes down.

My current opinion is this: If you can vibe code it, you can vibe fix it. You just might not be able to fix it quickly. 

Software engineering is changing rapidly as a discipline. The days of typing code into a computer manually seem to be over, and the current conversation on X is around “zero-human startups.” My experience with Proof, though, is a good reality check. 

It demonstrates both what is truly possible with vibe coded apps, and where human engineers will continue to be critical now and in the future.

What’s possible at the edge

I’ve been writing about how AI is changing programming [for a few years now](https://every.to/chain-of-thought/i-spent-24-hours-with-github-copilot-workspaces), and my experience with Proof confirms a lot of my thoughts...

Become a [paid subscriber to Every](https://every.to/subscribe) to unlock this piece and learn about:

What it took to bring a crashing, vibe coded app back from the brink

The specific failure modes coding models keep hitting

Why allocation is the new key skill for human engineers

[Subscribe](https://every.to/subscribe?source=post_button)

[Click here](https://every.to/chain-of-thought/when-your-vibe-coded-app-goes-viral-and-then-goes-down) to read the full post

Want the full text of all articles in RSS? [Become a subscriber](https://every.to/subscribe), or [learn more](https://every.to).

---

## [The Two-slice Team](https://every.to/chain-of-thought/the-two-slice-team)
*⛓️ Chain of Thought*

by [Dan Shipper](https://every.to/@danshipper)in [Chain of Thought](https://every.to/chain-of-thought)Midjourney/Every illustration.
​​TLDR: Today we’re launching a new experiment: Proof, an agent-native markdown editor that lets you collaborate on documents with multiple humans and AI agents—and tracks who wrote what. It’s available now for paid Every subscribers.

Try Proof

For the past two decades, Amazon’s “two-pizza rule” has been the gold standard for team size.

The story goes like this: At a company retreat in 2002, when Amazon managers wanted more communication, Jeff Bezos fired back that “communication is terrible!” A few weeks later, he restructured the company around small autonomous teams. If a team had more than 10 people—more than could be fed by two pizzas—it was too big.

Twenty-four years later, two-pizza teams are now themselves too big for building software products. When each employee is armed with Opus 4.6 and Codex 5.3, the ideal team size shrinks even further.

[Click here](https://every.to/chain-of-thought/the-two-slice-team) to read the full post

Want the full text of all articles in RSS? [Become a subscriber](https://every.to/subscribe), or [learn more](https://every.to).

---

## [OpenAI Has Some Catching Up to Do](https://every.to/chain-of-thought/openai-has-some-catching-up-to-do)
*⛓️ Chain of Thought*

by [Dan Shipper](https://every.to/@danshipper)in [Chain of Thought](https://every.to/chain-of-thought)Midjourney / Every Illustration.
Was this newsletter forwarded to you? [Sign up](https://every.to/account) to get it in your inbox.

This morning I hit my usage limit on [Codex](https://every.to/vibe-check/gpt-5-codex-knows-when-to-think-hard-and-when-not-to), OpenAI’s competitor to Claude Code. I’m building an [agent-native](https://every.to/guides/agent-native) Markdown editor for the Every team. It’s exactly the kind of complex, detail-heavy project where Codex shines.

But this week was an exception. Most of my coding happens in Claude Code now—and I’m not alone.

On Tuesday night, we had about 20 founders over to the office for a dinner on the future of AI. I asked everyone what their daily driver AI tools were. Of the programmers, almost everyone said Claude Code with Opus 4.5. The lone holdout was [Naveen Naidu](https://every.to/@naveen_6804)—general manager of [Monologue](https://www.monologue.to)—who still prefers Codex.

A month ago, the room would have been split between Codex CLI, GPT 5.1 in Cursor, and Claude Code—with some [Droid](https://every.to/vibe-check/vibe-check-i-canceled-two-ai-max-plans-for-factory-s-coding-agent-droid) sprinkled in. 

A year ago, the whole room would have been using GPT models.

This might not surprise you if you’ve been on X lately. It seems the only thing on everyone’s mind is Claude Code. This audience is obviously a narrow slice of the market, but it’s [the same slice](https://every.to/p/ai-can-build-anything-social-dandelions-decide-what-spreads) that was excited about ChatGPT when it first came out. 

So, what explains Claude Code and Opus’s sudden rise in startup circles? It’s not better marketing. Sure, Anthropic has their [“thinking” caps](https://www.instagram.com/p/DPW0CJQkmAq/). But compared to the high-profile livestreams we’ve gotten used to for important model releases, they barely promoted [Opus 4.5](https://every.to/vibe-check/vibe-check-opus-4-5-is-the-coding-model-we-ve-been-waiting-for) at launch. Instead, it’s who they decided to build for—and how that’s shaping the direction of the whole tech industry.

How Claude Code happened

When Anthropic first released Claude Code along with Sonnet 3.7 in late February of 2025, it was a bold bet. At a time when existing code editors were firmly stuck in building AI agents crammed into a sidebar, they went terminal-first and bypassed the code editor altogether. It signaled, “We’re moving to a world where code doesn’t matter.” At the time, we [wrote](https://every.to/vibe-check/vibe-check-claude-3-7-sonnet-and-claude-code) that while it was incredible at vibe coding new projects from scratch, it wasn’t yet good enough to work with large codebases on its own. Still, we were impressed.

Become a [paid subscriber to Every](https://every.to/subscribe) to unlock this piece and learn about:

The dramatic shift in AI tool preferences among startup founders—and why nearly everyone has abandoned what they used a year ago

Why OpenAI’s bet on professional developers may be targeting a market that’s about to shrink

The unexpected reason the winner of “vibe coding” might determine how everyone works on computers

[Subscribe](https://every.to/subscribe?source=post_button)

[Click here](https://every.to/chain-of-thought/openai-has-some-catching-up-to-do) to read the full post

Want the full text of all articles in RSS? [Become a subscriber](https://every.to/subscribe), or [learn more](https://every.to).

---

## [Agent-native Architectures: How to Build Apps After the End of Code](https://every.to/chain-of-thought/agent-native-architectures-how-to-build-apps-after-the-end-of-code)
*⛓️ Chain of Thought*

by [Dan Shipper](https://every.to/@danshipper)in [Chain of Thought](https://every.to/chain-of-thought)Midjourney/Every illustration.
Was this newsletter forwarded to you? Sign up to get it in your inbox. Plus: Help us scale the only subscription you need to stay at the edge of AI. Explore open roles at Every.

Traditional software is built like a skyscraper. 

Any application you use daily—whether it’s Word, Figma, or Gmail—is a bronze and glass facade towering 500 feet above the street. It is a lobby with travertine walls that smells faintly of sandalwood. Every beam is load-tested. Every force and flow obeys the blueprint. 

Just to be real with you, I am jealous of architects. I often moonlight as one, but as a programmer, my skyscrapers are shoddy. I start before the blueprint is final; I dig a foundation and sink some beams, but they are usually off by an eighth of an inch. By the time we get to the fifth story, I need a real architect to take over. 

But AI enables a new kind of software, one that’s more like growing a garden than it is building a skyscraper. I’ve been calling it an agent-native architecture—and we’ve pivoted our whole software strategy at Every around it.

The core of an agent-native architecture is not code. Instead, as the name implies, the core is an agent—something squishy and alive, planted in sun and soil. Each feature of the app is a prompt to the agent that names the result to achieve, not a set of steps to follow. That’s why I often think of agent-native apps as Claude Code in a trenchcoat. 

[Click here](https://every.to/chain-of-thought/agent-native-architectures-how-to-build-apps-after-the-end-of-code) to read the full post

Want the full text of all articles in RSS? [Become a subscriber](https://every.to/subscribe), or [learn more](https://every.to).

---

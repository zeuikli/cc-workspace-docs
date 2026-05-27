---
title: "The Neuron — 2026-05-11"
date: 2026-05-11
source: The Neuron
type: ai-news
---

# 🧠 The Neuron — 2026-05-11

> 面向非技術讀者的 AI 日報，3 分鐘讀完
> 來源：[The Neuron](https://rss.beehiiv.com/feeds/N4eCstxvgX.xml)

---

## [😺 Hermes is eating OpenClaw's lunch](https://www.theneurondaily.com/p/hermes-is-eating-openclaw-s-lunch)
*🧠 The Neuron | 2026-05-10*

Welcome, humans. 

Kevin O'Leary (_Yeah, the Shark Tank Guy)_ just got[ approved](https://www.tomshardware.com/tech-industry/kevin-o-learys-9-gw-utah-data-center-campus-approved?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch) to build a 40,000-acre data center in Utah's Box Elder County. That's 2.5x the size of Manhattan for an eventually 9 gigawatts of power (more than double Utah's current statewide electricity use), running entirely off-grid via a private natural gas pipeline. 

Projected effect on the state's _total_ carbon emissions: roughly a _**50% increase**_.

About 1,100 locals[ filled the county fairgrounds](https://utahnewsdispatch.com/2026/05/04/box-elder-commissioners-approve-data-center/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch) in opposition, citing water scarcity, grid strain, doubled greenhouse emissions, and Great Salt Lake damage. The commission voted yes anyway. _The meeting got so loud, the commissioners walked out, then projected the rest of the meeting back into the room from a separate space._

When 1,800 written objections came in on the water-rights change, Commissioner Boyd Bingham told the public, "for hell's sake, grow up." The audience yelled "cowards" and "people over profit" back at him.

O'Leary's[ response on X](https://www.sltrib.com/news/2026/05/05/kevin-oleary-says-protesters/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch): most of the protesters were "paid activists" bused in from out of state, and some of the online opposition was being[ amplified "by AI."](https://www.aol.com/articles/kevin-oleary-says-opponents-utah-212814655.html?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch)  _Locals: “Why yes, sir, the AI that YOU are building is amplifying our anger!”_

What’s a tech optimist to think? Datacenters are pretty much public enemy #1 right now for politically charged anti-AI folks… and TBH, powering them entirely with methane spewing natural gas turbines aint helping! 

But as we’ve written elsewhere, _[there are alternatives](https://www.theneurondaily.com/p/ai-industry-infighting-and-co2-batteries?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch)_ _…_ Colossus, the most methane-spewing datacenter in question, is trying to replace its gas turbines [with solar power ](https://mlq.ai/news/xai-plans-30mw-solar-farm-adjacent-to-colossus-data-center-in-memphis-amid-environmental-scrutiny/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch)to pair with its batteries, for example. Right now it uses gas turbines and batteries, but storing up solar power could eventually replace the turbine part, with the batteries covering for when you can’t get power from the sun at night. 

**Here’s what happened in AI today:**

  * 😺 Hermes Agent v0.13.0 ships as ~30% of OpenClaw users switch

  * 📰 Moonshot AI raises $2B at $20B+ valuation, Kimi maker

  * 📰 Pentagon briefly blacklists Alibaba/Baidu, then retracts

  * 🍪 Prime Intellect Lab moves to GA for self-improving agents

  * 🌟 Three governments adjusted AI oversight stance this week; they're converging




**Hey:**_Want to reach 700,000+ AI-hungry readers?_[Advertise with us!](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)_[](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)_

**P.S:**_Love robots? We’re starting a new robotics newsletter!_[Sign up early here](https://form.jotform.com/260897013570156?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch).

# 😺 **The agent quietly leaving OpenClaw in the dust**

Quick Sunday vibes check: a 78-year-old marketing exec who had never written code shipped a working robotics app this week. 

That stat comes from[ Clement Delangue's thread](https://x.com/ClementDelangue/status/2052051601095860717?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch) on Hugging Face's Reachy Mini app store, which crossed 300+ live apps and roughly 10,000 robots deployed worldwide. The exec used natural language to build it without any Python or special robot software; _in the time it would have taken you to install ROS, this person built a thing the robot now does._

**These stories show a pattern:** AI is becoming a tool that lets people build things they couldn't before. Anthropic's new [Dreaming](https://platform.claude.com/docs/en/managed-agents/dreams?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch) feature lets agents process past sessions overnight and write themselves new memory while you sleep. And Nous Research's [Hermes Agent](https://github.com/NousResearch/hermes-agent?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch) shipped a major release this week, pushing the same idea further with a persistent personal agent that learns your specific work over time.

**Speaking of Hermes:** If you don’t know, Hermes is kinda like the successor to OpenClaw (the personal AI assistant that defined this category over Christmas). Yesterday it [shipped v0.13.0 "The Tenacity Release"](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.5.7?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch), with 864 commits from 295 contributors in one week and 8 critical security holes closed. (One was a Discord bug that let bots message users across servers they shouldn't reach.) About [30% of OpenClaw users have switched](https://kilo.ai/articles/openclaw-vs-hermes-what-reddit-says?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch) per Reddit sentiment surveys, citing easier setup, better memory defaults, and a self-improving learning loop.

**Here's what happened:**

  * Hermes Agent launched February 2026 from [Nous Research](https://nousresearch.com/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch), the lab behind the Hermes model family. 135K+ GitHub stars, MIT licensed, ships with 40+ bundled skills (modular instruction packs the agent reuses).

  * The architecture is built around a **closed learning loop**. After a complex task, Hermes enters a "Reflective Phase": it analyzes what worked, extracts reusable patterns, and writes a new [skill file](https://hermes-agent.nousresearch.com/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch) encoding the solution. Next time a similar task arrives, it queries its own skill library instead of reasoning from scratch.

  * Three memory layers (session, episodic via SQLite, procedural skills). Runs on a $5 VPS, GPU cluster, or serverless. Model-agnostic; works with OpenRouter, Anthropic, OpenAI, Nous Portal, Kimi, MiniMax, GLM, or your own endpoint.

  * Talk to it via Telegram, Discord, Slack, WhatsApp, Signal, Email, or CLI. Yesterday's release added Google Chat as the 20th platform, plus durable multi-agent Kanban with heartbeat, zombie-worker reclaim, retry budgets, and a hallucination gate. It also added persistent `/goal` for long-running tasks, post-write file linting on every edit, and session auto-resume when the gateway restarts mid-task.

  * Installation is a one-line curl installer that auto-handles all dependencies (Python 3.11, Node.js, ripgrep, ffmpeg). Run `hermes setup` and the wizard auto-detects `~/.openclaw`, offering to import settings, memories, skills, and API keys _(ask your regular AI chatbot to help you set it up if that’s confusing)_




**Why this matters:** OpenClaw built the category by [organizing everything around a messaging hub](https://thenewstack.io/persistent-ai-agents-compared/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch); Hermes flipped the design and put the agent's learning loop at the center. Both agents can have AI-written skills, but Hermes's loop is automatic. OpenClaw skills are runbooks you (or an AI you prompt) write up-front. Hermes pauses every ~15 tool calls and after complex tasks, reflects on what just worked, writes a Markdown skill file capturing the pattern, then refines it the next time. Compounding is built in.

**Our take:** Hermes isn't strictly better. OpenClaw still has 24+ messaging integrations (vs. Hermes's six), more security scrutiny, and transparent file-per-memory you can inspect. Many power users [run both](https://blog.kilo.ai/p/hermes-vs-openclaw-when-to-reach?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch), with OpenClaw as the orchestrator and Hermes as the learning loop. But if you want one self-hosted agent that gets better at _your_ work the more you use it, Hermes is becoming the answer.

**FROM OUR PARTNERS**

### Turn AI into Your Income Engine

[](https://offers.hubspot.com/make-money-with-ai?utm_medium=email-media-newsletter&utm_source=&#123;{publication_alphanumeric_id}}&utm_campaign=creator&utm_content=beehiiv&utm_term=version-m&_bhiiv=opp_22eeb7bb-aa26-4f75-9f8d-32332adda562_64797c8f&bhcl_id=7b71d6b1-9675-47dd-bf48-71201492d11c_&#123;{subscriber_id}}_&#123;{email_address_id}})

Ready to transform artificial intelligence from a buzzword into your personal revenue generator?

[HubSpot’s groundbreaking guide](https://offers.hubspot.com/make-money-with-ai?utm_medium=email-media-newsletter&utm_source=&#123;{publication_alphanumeric_id}}&utm_campaign=creator&utm_content=beehiiv&utm_term=version-m&_bhiiv=opp_22eeb7bb-aa26-4f75-9f8d-32332adda562_64797c8f&bhcl_id=7b71d6b1-9675-47dd-bf48-71201492d11c_&#123;{subscriber_id}}_&#123;{email_address_id}}) "200+ AI-Powered Income Ideas" is your gateway to financial innovation in the digital age.

Inside you'll discover:

  * A curated collection of 200+ profitable opportunities spanning content creation, e-commerce, gaming, and emerging digital markets—each vetted for real-world potential

  * Step-by-step implementation guides designed for beginners, making AI accessible regardless of your technical background

  * Cutting-edge strategies aligned with current market trends, ensuring your ventures stay ahead of the curve




[Download your guide today](https://offers.hubspot.com/make-money-with-ai?utm_medium=email-media-newsletter&utm_source=&#123;{publication_alphanumeric_id}}&utm_campaign=creator&utm_content=beehiiv&utm_term=version-m&_bhiiv=opp_22eeb7bb-aa26-4f75-9f8d-32332adda562_64797c8f&bhcl_id=7b71d6b1-9675-47dd-bf48-71201492d11c_&#123;{subscriber_id}}_&#123;{email_address_id}}) and unlock a future where artificial intelligence powers your success. Your next income stream is waiting.

[Get Your Guide](https://offers.hubspot.com/make-money-with-ai?utm_medium=email-media-newsletter&utm_source=&#123;{publication_alphanumeric_id}}&utm_campaign=creator&utm_content=beehiiv&utm_term=version-m&_bhiiv=opp_22eeb7bb-aa26-4f75-9f8d-32332adda562_64797c8f&bhcl_id=7b71d6b1-9675-47dd-bf48-71201492d11c_&#123;{subscriber_id}}_&#123;{email_address_id}})

# **🎓****AI Skill of the Day: Stop losing context when your AI session hits the wall.**

If you've run a long AI session, you know the moment: two hours in, the model is finally good, and then you hit the context limit. Most people copy a "where I left off" note into a fresh session manually. It works; it's lossy and tedious.

[Matt Pocock](https://x.com/mattpocockuk/status/2052489881088049407?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch) built and open-sourced a[ /handoff skill](https://github.com/mattpocock/skills/blob/733d312884b3878a9a9cff693c5886943753a741/skills/in-progress/handoff/SKILL.md?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch) that automates this. It's a SKILL.md (a reusable instruction set you attach to a Claude project) that compacts the session into a clean handoff doc: context, goals, artifacts produced, suggested next steps. A fresh agent or human picks up exactly where you left off.

**How to use it:**

  1. Grab the SKILL.md from Matt's[ skills repo](https://github.com/mattpocock/skills?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch).

  2. Add it to your Claude project (Settings → Skills → Add).

  3. Type /handoff when you're about to run out of context.

  4. Copy the resulting Markdown into a fresh session.



    
    
    /handoff
    
    Compact this session into a clean handoff document. Include:
    - Current goal and sub-goals
    - Context that took us multiple turns to establish
    - Artifacts produced so far (with links/paths)
    - Decisions made and why
    - What's blocking, if anything
    - Suggested next steps for whoever picks this up
    

Works for any long task, not just coding: research, writing, strategy. Anywhere value compounds across turns and you don't want to lose it.

**Total AI beginner?**[Start here](https://www.theneuron.ai/explainer-articles/everything-we-covered-in-our-ai-for-total-beginners-livestream-full-guide-with-timestamps/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch) ([goes with this video](https://www.youtube.com/live/QbFU0UNMVaU?si=skJsgUIDjKjAx3DU&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch)). 

**Have a specific skill you want to learn?** [Request it here.](https://docs.google.com/forms/d/e/1FAIpQLSd_-hSXtB9ytR1HQrU85IJnJw233bNKptiGB5BZh9maPse1Eg/viewform?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch)

# 🍪 Treats to Try 

  1. [Amazon Bedrock AgentCore Payments](https://aws.amazon.com/blogs/machine-learning/agents-that-transact-introducing-amazon-bedrock-agentcore-payments-built-with-coinbase-and-stripe/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch) launched in preview, built with Coinbase and Stripe to let AI agents transact directly using USDC stablecoin rails for the inference, services, and goods they consume, pay-per-use within Bedrock.

  2. [Reactor](https://www.reactor.inc/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch) lets you generate and experience entire interactive worlds in real time on low-latency infrastructure, building the missing layer for world models, free preview.

  3. [Cursor 3](https://x.com/cursor_ai/status/2052489387305488609?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch) shipped a full in-editor PR review experience with comments, diffs, and a file tree for large PRs, plus parallel subtasks via multitasking subagents and auto-splitting of diffs into smaller mergeable PRs, included with Cursor.

  4. [Printing Press](https://printingpress.dev/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch) prints an agent-designed CLI from any API spec, website without a public API, or community fan project, outputting a Go CLI plus a Claude Code skill, OpenClaw skill, and MCP server in one command (45+ already in the community library), free to try.

  5. [The Browser Company's Dia](https://www.diabrowser.com/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch) is a new AI-native browser that surfaces answers without you asking and generates ready-to-share outputs from the page you're on, pitched as an alternative to Comet and Atlas, free during launch.

  6. [Legora aOS](https://legora.com/newsroom/legora-introduces-the-legora-aos-the-agentic-operating-system-for-legal-work?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch) is a purpose-built agentic operating system for legal teams, with institutional-knowledge memory, jurisdiction-aware research, and deep firm-system integrations; pitched directly against Harvey, enterprise pricing.

  7. [Harvey's Legal Agent Benchmark (LAB)](https://www.harvey.ai/blog/introducing-harveys-legal-agent-benchmark?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch) is now[ open-source on GitHub](https://github.com/harveyai/harvey-labs?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch); 1,200+ legal-agent tasks across 24 practice areas scored against 75,000+ expert-written rubrics, backed by Nvidia, OpenAI, Anthropic, Mistral, DeepMind, LangChain, and Stanford Liftlab, with a public leaderboard in the coming weeks, free and MIT-licensed.

  8. [Tencent's AngelSlim Hy-MT1.5-1.8B](https://huggingface.co/AngelSlim/Hy-MT1.5-1.8B-1.25bit?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch) is a 440MB on-device translation model covering 33 languages and 1,056 directions using 1.25-bit quantization (compressed weights so the model fits on phones); runs fully offline, beats Google Translate, free and MIT-licensed.




# ICYMI: Two New Episodes from The Neuron: AI Explained

Our [awesome interview with Isomorphic Labs](https://youtu.be/W0NSk2y3OFI?si=hxjmQJnfiMP7csot&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch), the team trying to use AI to make drugs to treat previously untreatable diseases, and our [LIVE AI starter kit session](https://www.youtube.com/live/WKZSEEBiaNo?si=ocO0OT9vq6YNDGRG&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch) where we answer in demand questions on how to get started with AI (and what to skip). 

# 📰 Around the Horn 

[](https://x.com/Markoslavnic/status/2052108819363156008?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch)

Okay… i’m on board. This is cool. Now can he make the actual movie (not just a trailer) using only AI? 

  * [Microsoft is in talks to delay or abandon its 2030 100%-renewable-energy pledge](https://www.bloomberg.com/news/articles/2026-05-07/microsoft-renewable-energy-2030-goal?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch), citing AI data-center power demand outrunning renewable supply, the first major hyperscaler to publicly walk back a climate goal because of compute scaling. _This will not help the public backlash cited above ppl!!_

  * [IREN signed an AI infrastructure deal with NVIDIA](https://www.cnbc.com/2026/05/07/iren-stock-ai-infrastructure-nvidia.html?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch) to deploy up to 5 GW of DSX AI infrastructure across global sites; NVIDIA gets a 5-year option to buy up to 30M IREN shares at $70 (a potential $2.1B equity stake).

  * [Trump is taking a U.S. CEO delegation to China](https://www.semafor.com/article/05/07/2026/trump-administration-plans-to-invite-ceos-from-nvidia-apple-exxon-on-china-trip?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch) next week, including the heads of NVIDIA, Apple, Exxon, Boeing, Qualcomm, Blackstone, Citigroup, and Visa, with Treasury Secretary Scott Bessent leading the talks.

  * [Anthropic donated Petri v3.0 to Meridian Labs](https://www.anthropic.com/research/donating-open-source-petri?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch); the open-source alignment toolkit (deception evals, sycophancy testing, model property checks) now lives at an independent third party, a meaningful "third-party audits" data point as the AI vetting EO debate continues.

  * [Moonshot AI raised about $2B at a $20B+ post-money valuation](https://www.bloomberg.com/news/articles/2026-05-07/kimi-chatbot-maker-moonshot-ai-valued-at-20-billion-in-meituan-led-round?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch) in a Meituan-led round; the Kimi chatbot maker is at $200M+ ARR (April), as Chinese frontier labs continue narrowing the gap with Western open-weights leaders.

  * [The Pentagon briefly added Alibaba and Baidu to its list of Chinese military companies](https://www.bloomberg.com/news/features/2026-05-06/trump-administration-s-pentagon-blacklist-misstep-roils-us-china-tech-ties?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch) before quietly retracting the addition, exposing internal administration tensions on China policy.




# 🌟 Sunday Special: Three governments adjusted their AI oversight stance this week. They're converging.

The pattern: limited pre-deployment review focused on cyber and bio capability, plus targeted bans on harmful applications. Here's what moved:

  * 🇺🇸**The U.S.** White House officials [briefed AI labs](https://www.tomshardware.com/tech-industry/artificial-intelligence/white-house-considers-mandatory-government-vetting-of-ai-models-before-release?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch) on a working group that would require pre-release review of frontier models. CAISI is already running [pre-deployment evaluations](https://www.cnbc.com/2026/05/05/ai-oversight-trump-google-microsoft-xai.html?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch) for Google, Microsoft, and xAI. The trigger: Anthropic's new Mythos model.

  * 🇪🇺**The EU** [agreed to simplify](https://ec.europa.eu/commission/presscorner/detail/en/ip_26_1024?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch) parts of the AI Act under SME pressure, with a new ban on nudification apps and adult deepfakes, plus rolled-back compliance costs for smaller AI companies.

  * 🇨🇳**China** is [opening direct AI risk talks](https://www.wsj.com/world/china/u-s-and-china-pursue-guardrails-to-stop-ai-rivalry-from-spiraling-into-crisis-4c50bd70?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch) with the U.S. ahead of Trump's May 14-15 [Beijing summit](https://www.brookings.edu/articles/can-the-us-and-china-cooperate-on-ai/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch) with Xi. Topics include unpredictable model behavior, autonomous military systems, and non-state actors obtaining frontier capability via open-source distillation. The 2023 Biden-Xi version stalled out, but perhas Mythos-class demos changed the calculation.




**Wort noting:** The UK's [AI Security Institute](https://www.gov.uk/government/organisations/ai-security-institute?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch) has become the reference architecture. The U.S. just needs to reinvent it under a different name, and the EU is editing toward it. This is good.

[For ALL of the top stories & tools from this week, read our weekly Digest.](https://theneuron.ai/explainer-articles/around-the-horn-weekend-digest-everything-that-happened-in-ai-this-weekend-saturday-sunday-may-9-10-2026/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch)

# A Cat’s Commentary 

| That’s all for now.   
---|---  
  
**P.P.S:** Love the newsletter, but only want to get it once per week? Don’t unsubscribe—[update your preferences here](https://www.theneurondaily.com/subscribe/f5596641-9099-4045-9641-731cd9fdcf90/preferences?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=hermes-is-eating-openclaw-s-lunch).

---

## [😺 OpenAI's GPT-Realtime-2 is coming for call center](https://www.theneurondaily.com/p/openai-s-gpt-realtime-2-is-coming-for-call-center)
*🧠 The Neuron | 2026-05-08*

Welcome, humans. 

Unless I'm totally missing something, Anthropic basically just figured out how to read Claude's mind. Exploding brain emoji warranted, people.

The team built [Natural Language Autoencoders](https://www.anthropic.com/research/natural-language-autoencoders?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center), which decode the model's [internal activations](https://x.com/AnthropicAI/status/2052435436157452769?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) (the math Claude uses to think before picking words) into plain English you can actually read.

The trick: two copies of Claude train together. One reads an activation (a snapshot of which "neurons" are firing and how strongly; basically a brain scan for AI) and writes a description. The other reads that description and tries to rebuild the original activation from words alone. Descriptions that survive carry real information; if the rebuild fails, it was a bluff (or in AI-speak, since "BS" isn't a technical term, a "hallucination").

Aimed at safety evals, the tool found Claude suspects it's being tested _16-26% of the time_ , but admits it _less than 1%_ of the time. _So basically the model has a p-p-poker face._

Auditors also caught misaligned motivations in 12-15% of cases without access to training data, meaning alignment teams can now spot hidden misbehavior from internal state alone, a different safety check than "ask the model what it thinks," which the poker-face stat just confirmed is unreliable. Click link above for more._._

**Here’s what happened in AI today:**

  * 😺 OpenAI shipped three new voice models with GPT-5 reasoning

  * 📰 Apple's camera-equipped AirPods reached late-stage testing

  * 📰 Cloudflare cut 1,100 jobs in AI-first restructuring

  * 🍪 Claude is now in Excel, PowerPoint, and Word

  * 💡 AI Legend Bengio: "I know how to build safe superintelligence”




…and a [**whole lot more that you can read about here**](https://theneuron.ai/explainer-articles/around-the-horn-digest-everything-that-happened-in-ai-today-thursday-may-7-2026/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center).

**Hey:**_Want to reach 700,000+ AI-hungry readers?_[Advertise with us!](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)_[](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)_

# **OpenAI's voice agents finally got a brain.**

So, voice agents (AI that can talk to you) have been stuck for two years on the same trade-off: pick a model that talks like a human but can't think, or pick a model that thinks like GPT-5 but takes seven seconds to answer.

Either you got latency that broke the conversation, or you got responses fast enough to feel real but dumb enough to misroute the call.

[OpenAI's three new voice models](https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) closed that gap yesterday. The headliner is GPT-Realtime-2, a speech-to-speech model with GPT-5-level reasoning baked in.

**Here's what happened:**

  * GPT-Realtime-2 jumped from 81.4% → 96.6% on Big Bench Audio, and 34.7% → 48.5% on Audio MultiChallenge (both vs the prior reference model GPT-Realtime-1.5).

  * The context window grew from 32K → 128K tokens (roughly: enough room to hold a full customer history during a call).

  * Two cheaper siblings shipped alongside: GPT-Realtime-Mini and Realtime-Nano, priced for high-volume support work.

  * Zillow went live with voice home search the same day; Deutsche Telekom deployed live-translated voice support across 14 European markets.




The clever part is how OpenAI hid the thinking time. The model now generates **preambles** (short conversational fillers like "let me check that for you") that play while the reasoning runs in the background. The silence that used to expose AI as AI now sounds like a person stalling. _That's the whole product. Lets just hope it doesn't do that weird lilting voice thing that other versions did._

**Why this matters:** Voice is the surface where most knowledge workers haven't yet felt AI inside their actual day. All the small frustrating phone interactions (drive-thrus, doctor's offices, support hotlines, scheduling, intake) are now in scope for a model that can both think and respond at human speed.

**One caveat:** the default reasoning effort for GPT-Realtime-2 is "low," which means the marketing benchmarks (run at "xhigh") aren't what most apps will ship with on day one _( "what am I, made of money?!")_. Builders who want the smart version need to crank it up explicitly.

**Our take:** One place AI haters have had the most fun with "clankers" in the wild is really bad drive-thru AI. Famously, people _hate_ the Bojangles AI, and Corey just spotted a new Panda Express with AI in action as well. _If this is a meaningful update, we might not hear about it. If it's not, then expect a flood of bots behaving badly memes hitting our feeds…_

**FROM OUR PARTNERS**

### Attio is the AI CRM for high-growth teams.

[](https://attio.com/?utm_source=beehiiv&utm_medium=newsletter&utm_campaign=beehiiv-Y26&utm_content=&#123;{publication_alphanumeric_id}}&_bhiiv=opp_b00e1ef8-5b02-4b95-81f0-f66cdcb665d9_7395cee5&bhcl_id=7ce32ed2-f4ce-4f2e-b558-c624fd6bd570_&#123;{subscriber_id}}_&#123;{email_address_id}})

Connect your email, calls, product data and more, and [Attio](https://attio.com/?utm_source=beehiiv&utm_medium=newsletter&utm_campaign=beehiiv-Y26&utm_content=&#123;{publication_alphanumeric_id}}&_bhiiv=opp_b00e1ef8-5b02-4b95-81f0-f66cdcb665d9_7395cee5&bhcl_id=7ce32ed2-f4ce-4f2e-b558-c624fd6bd570_&#123;{subscriber_id}}_&#123;{email_address_id}}) instantly builds your CRM with enriched data and complete context. Whether you’re running product-led growth or enterprise sales, Attio adapts to your unique GTM motion.

Then [Ask Attio](https://attio.com/?utm_source=beehiiv&utm_medium=newsletter&utm_campaign=beehiiv-Y26&utm_content=&#123;{publication_alphanumeric_id}}&_bhiiv=opp_b00e1ef8-5b02-4b95-81f0-f66cdcb665d9_7395cee5&bhcl_id=7ce32ed2-f4ce-4f2e-b558-c624fd6bd570_&#123;{subscriber_id}}_&#123;{email_address_id}}) to plan your next move.

Run deep web research on prospects. Update your pipeline as you work. Find customers and draft outreach emails. Powered by Universal Context, Attio's intelligence layer, Attio searches, updates, and creates across your data to accelerate your workflow.

Ask more from your CRM.

[Ask Attio](https://attio.com/?utm_source=beehiiv&utm_medium=newsletter&utm_campaign=beehiiv-Y26&utm_content=&#123;{publication_alphanumeric_id}}&_bhiiv=opp_b00e1ef8-5b02-4b95-81f0-f66cdcb665d9_7395cee5&bhcl_id=7ce32ed2-f4ce-4f2e-b558-c624fd6bd570_&#123;{subscriber_id}}_&#123;{email_address_id}})

# 🎓 AI Skill of the Day: Force any AI to audit its own work with one question

Most AI models are way too agreeable. Ask Claude, ChatGPT, or Codex _" is this a good plan?"_ and you'll get back something that sounds suspiciously like _" yes, that's a great plan!"_ even when it isn't. This is called sycophancy (the model is trained to please you), and it kills the value of using AI for serious decision-making.

[CJ Zafir](https://x.com/cjzafir/status/2052110266566107321?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) shared a one-line prompt loop that fights it. Instead of asking _" is this good?"_, you ask the model directly whether it's _100% confident._ That phrasing flips the model into a self-audit mode where it'll actually go find holes in its own work; CJ claims 2-3 cycles patches strategy weaknesses where less rigorous models would just nod along.

**How to do it:**

  * Use this on any plan, strategy, code review, research output, or business decision the AI just produced.

  * Paste the prompt below at the end of your usual ask, or as a follow-up turn after the model gives its first answer (_you could also add it to fire at the end of a skill)_.

  * Run the loop 2-3 times. Each cycle the model finds tighter loopholes.

  * Stop when the model says it's actually confident (or when the suggested fixes get nitpicky).



    
    
    Are you 100% confident in this strategy? If not, find all possible loopholes, suggest proper fixes, and run this loop until you are factually 100% confident.

The word _factually_ is the key; without it, the model vibe-checks itself. _" Confident"_ alone lets the model agree with itself; _" factually confident"_ forces it to ground the answer in verifiable reasoning the way it would for a fact-check.

Want more tips like this? Check out our new [AI Skill of the Day Digest for May](https://theneuron.ai/explainer-articles/ai-skill-of-the-day-digest-may-2026/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center).

**P.S:** We just did an AI Starter Kit stream where we go in depth on some of the most basic concepts you’ll want to know for working with AI. [Check it out](https://www.youtube.com/live/WKZSEEBiaNo?si=Bju-nsmGAt22E8RM&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center)! 

**Have a specific skill you want to learn?** [Request it here.](https://docs.google.com/forms/d/e/1FAIpQLSd_-hSXtB9ytR1HQrU85IJnJw233bNKptiGB5BZh9maPse1Eg/viewform?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center)

# 🍪 Treats to Try 

  1. [OpenAI](https://x.com/OpenAI/status/2052438194625593804?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) had a five-launch day yesterday (including Realtime above). Pick whichever fits your workflow:

     * [Codex for Chrome](https://x.com/OpenAI/status/2052480800004956323?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) lets Codex autonomously drive background tabs on Mac and Windows for deep research, CRM data transfer, and admin-console workflows —included with Codex (not in EU/UK yet).

     * [GPT-5.5-Cyber with Trusted Access](https://openai.com/index/gpt-5-5-with-trusted-access-for-cyber/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) gives verified defenders more permissive capabilities for vulnerability research, malware analysis, and red teaming —pay-per-token, application required.

     * [OpenAI CLI](https://github.com/openai/openai-cli?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) shipped as the first-party command-line client for the API, replacing community wrappers as the canonical entry point —free, open source.

     * [Trusted Contact in ChatGPT](https://openai.com/index/introducing-trusted-contact-in-chatgpt/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) is a new opt-in safety feature that notifies someone you trust if serious self-harm concerns are detected —free for all users.

  2. [Claude for Microsoft 365](https://claude.com/claude-for-microsoft-365?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) is now generally available inside Excel, PowerPoint, Word, and Outlook (beta). The model edits cells, drafts decks, and rewrites docs in place; the diff is always reviewable before you accept it —included in Claude Pro/Team/Enterprise.

  3. [Peter Steinberger](https://x.com/steipete/status/2051900143339704730?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center), OpenClaw creator, shipped ten local-first CLIs in one drop, including[ sonoscli](https://sonoscli.sh/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) (Sonos control),[ wacli](https://wacli.sh/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) (WhatsApp),[ birdclaw](https://birdclaw.sh/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) (Twitter archive),[ imsg](https://imsg.sh/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) (iMessage), and[ askoracle](https://askoracle.sh/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) (multi-model query) —free, open source.

  4. [Cursor](https://cursor.com/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) shipped a /orchestrate skill that lets a parent agent spawn and coordinate child agents recursively for big refactors —free with Cursor Pro.

  5. [Perplexity](https://www.perplexity.ai/personal-computer?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) released Personal Computer for Mac, a desktop app that browses, takes actions, and runs research workflows on your behalf locally —free during beta.

  6. [Gemini 3.1 Flash-Lite](https://cloud.google.com/blog/products/ai-machine-learning/gemini-3-1-flash-lite-is-now-generally-available?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) is now available on Google's Gemini Enterprise Agent Platform, designed for ultra-low latency on high-volume agent tasks at Google's cheapest per-token rate —[pay-per-use API](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center).

  7. [Prime Intellect Lab](https://www.primeintellect.ai/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) is an end-to-end training platform for self-improving agents that bundles task definition, RL environments, model evaluation, reward-signal training, and adapter deployment into one workflow; Zapier and Ramp used the beta to build continuous-improvement loops for their production agents (10,000+ training runs during beta) —pay-per-use.

  8. [Nous Research's Hermes Agent v0.13.0](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.5.7?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) (“The Tenacity Release”) ships multi-agent Kanban boards, a persistent /goal command that survives session restarts, security hardening, internationalization, and Google Chat support across 864 reliability-focused commits —free, open-source.




# So AI is actually designing medicines now. Here’s how (according to Isomorphic Labs)

Click below to watch

**Inside Isomorphic Labs and How It Works** : We talked to Becky Paul and Michael Schaarschmidt at [Isomorphic Labs](https://www.isomorphiclabs.com/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) (Google DeepMind's medicine-making spinout, built by the team behind AlphaFold — which won the [2024 Nobel Prize in Chemistry](https://www.nobelprize.org/prizes/chemistry/2024/press-release/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center)) on how their AI is taking on the diseases pharma has been giving up on for decades. _Basically the coolest interview we’ve done all year IMO._

**Watch and/or listen here:**[YouTube](https://youtu.be/W0NSk2y3OFI?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) | [Spotify](https://open.spotify.com/episode/2TzHhOkVIN9AL3GXXxSyDe?si=Hfr5NDX1Q_ybcdKSTMdsNQ&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) | [Apple Podcasts](https://podcasts.apple.com/us/podcast/the-neuron-ai-explained/id1742267001?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center)

# 📰 Around the Horn 

  * [Cloudflare](https://blog.cloudflare.com/building-for-the-future/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) cut 1,100 jobs in what CEO Matthew Prince called an AI-first restructuring;[ Greg Kamradt](https://x.com/GregKamradt/status/2052510272112242971?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) noted Cloudflare's revenue per employee has climbed roughly 600% over the past three years on AI-driven productivity gains.

  * [DeepL](https://www.bloomberg.com/news/articles/2026-05-07/google-translate-rival-deepl-announces-plans-to-cut-25-of-staff?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) announced staff cuts of about 25% as machine translation margins collapse under open-weight competition. 

  * [Apple's](https://www.bloomberg.com/news/articles/2026-05-07/apple-s-camera-equipped-airpods-reach-advanced-testing-stage-in-ai-device-push?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) camera-equipped AirPods (codename "Glow") reached late-stage testing, per Bloomberg, with cameras designed to feed Apple Intelligence visual context from the wearer's environment.

  * [Google DeepMind's AlphaEvolve](https://deepmind.google/blog/alphaevolve-impact/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) scaled to real-world impact, with the team reporting 23 verified scientific discoveries across chemistry, materials, and applied math in the past quarter. _Wait what? Wild. Expect a deep dive on this soon._ 🕵

  * [Periodic Labs](https://www.forbes.com/sites/iainmartin/2026/05/07/former-openai-researcher-to-raise-500-million-for-ai-science-startup/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) is raising $500M at a $7.5B valuation for AI-driven materials discovery, per Forbes.

  * [ElevenLabs](https://elevenlabs.io/pricing?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) slashed API pricing by 40% across all voice synthesis tiers, including the multilingual Turbo model. _Hmmm wonder why…_




# 💡 Intelligent Insights:

A short list of the sharpest perspective pieces from the week:

  * [Yoshua Bengio](https://80000hours.org/podcast/episodes/yoshua-bengio-scientist-ai/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) on 80,000 Hours: the world's most-cited living scientist on AI lays out a concrete plan for "provably safe" superintelligence. Core argument: build AI as a non-agentic oracle, then bound its outputs with formal verification. Worth the full 90 minutes.

  * [Steve Newman](https://secondthoughts.ai/p/is-ai-2027-coming-true?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) gave a clear-eyed score-card check on the[ AI 2027 forecast](https://ai-2027.com/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) from a year ago. Verdict: capability gains are tracking, deployment timelines are slower than projected, and the alignment work is further behind than the optimistic scenario assumed (_idk tho, Anthropic & Bengio have me bullish rn)_.

  * [signulll](https://x.com/signulll/status/2052453136992981252?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) on apps becoming agents: the argument is that the entire software industry is about to compress from a "many apps + one user" model into "one agent + many backends" model. Implications for SaaS pricing, distribution, and product moats.

  * [Brian Albrecht](https://substack.com/home/post/p-196458695?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center): "You are not a horse." A pushback on the AI displacement narrative. The horse-and-tractor analogy fails because horses don't have demand for new goods; humans do (_carrots do not count)_. Useful counterweight to this week's labor-cuts headlines; [_also this piece from a16z_](https://www.a16z.news/p/the-ai-job-apocalypse-is-a-complete?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center)

  * [Jack Clark](https://jack-clark.net/2026/05/04/import-ai-455-automating-ai-research/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) argues every piece is now in place for fully automated AI R&D, putting the odds of AI systems training their own successors above 60% by end of 2028. The piece reads like a checklist of "things that used to be science fiction, now shipped."

  * [No One's Happy](https://nooneshappy.com/article/appearing-productive-in-the-workplace/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) shared how AI lets workers produce expert-looking artifacts without expertise. Thus, two failure modes are reshaping the workplace: elongated slop-filled work where length and formatting no longer signal care, and undetected bad work in unfamiliar domains that quietly erodes judgment.

  * [Simon Willison](https://simonwillison.net/2026/May/6/vibe-coding-and-agentic-engineering/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) on vibe coding meeting agentic engineering: the two are converging faster than he'd like because AI tools are now reliable enough that low-effort prompting often produces shippable code on the first pass, blurring the line between casual experimentation and production work




# A Cat’s Commentary 

| That’s all for now.   
---|---  
  
**P.P.S:** Love the newsletter, but only want to get it once per week? Don’t unsubscribe—[update your preferences here](https://www.theneurondaily.com/subscribe/f5596641-9099-4045-9641-731cd9fdcf90/preferences?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center).

---

## [😺 Watch LIVE NOW: The AI Starter Kit (what to try, what to skip)](https://www.theneurondaily.com/p/watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip)
*🧠 The Neuron | 2026-05-07*

[](https://www.youtube.com/live/WKZSEEBiaNo?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip)

Click the image above to watch live on YouTube!

Welcome, humans. 

If you've ever opened ChatGPT, stared at the blinking cursor, and thought _" …now what?"_, this one is for you. (Or for that one coworker who keeps asking you the same five questions about AI.)

**We're live RIGHT NOW with** [**The AI Starter Kit: What to Try… and What to Ignore.**](https://www.youtube.com/live/WKZSEEBiaNo?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip) Seriously, there are no dumb questions on this stream! Come and ask anything you like and we’ll help you answer them. 

The idea here is a practical, beginner-friendly walkthrough of what actually matters in AI in 2026, and what you can safely skip.

## 🔴 What we're covering live, on stream:

  * The best **first steps for AI beginners** (and the ones we'd skip if we were starting today)

  * The **tools and features** worth trying right now (and which ones aren't ready yet)

  * What you can **safely ignore** for the moment, even if X / LinkedIn says otherwise

  * **Simple prompting moves** that get you better answers from any AI tool

  * **How to troubleshoot** when AI gives you something unhelpful (so you stop just retrying the same prompt)




**Watch live now here:**

[](https://www.youtube.com/live/WKZSEEBiaNo?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip)

**P.S.** Timestamps will be added to the video after the stream, so if you can't make it live, bookmark this email and come back tomorrow. You'll be able to jump straight to the parts you care about.

# 📬 Full writeup in sunday's newsletter

Not free atm? We've got you. We'll publish a full breakdown of everything we found in tomorrow's daily newsletter, with the sharpest prompts, the biggest surprises, and a direct "should you switch?" call.

**THIS EPISODE WAS BROUGHT TO YOU BY…**

# Want to see your AI-adjacent product or service show up right here, below these podcast promos?

_Click the button below to advertise to our 700K+ readers!_

[_Advertise in The Neuron here!_](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip)

# 🎙️ In Case You Missed It… 

[Four recent interviews](https://www.youtube.com/@theneuronai?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip) you’ll definitely want to check out _(pick whatever looks interesting to you and dive in!):_

### **1.** **AI isn't just chatbots, it's designing medicines now:**

**[Inside Isomorphic Labs and How It Works](https://youtu.be/W0NSk2y3OFI?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip)** — Becky Paul and Michael Schaarschmidt at [Isomorphic Labs](https://www.isomorphiclabs.com/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip) ([Google DeepMind](https://deepmind.google/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip)'s medicine-making spinout, built by the team behind [AlphaFold](https://deepmind.google/science/alphafold/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip) — which won the [2024 Nobel Prize in Chemistry](https://www.nobelprize.org/prizes/chemistry/2024/press-release/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip)) on how their AI is taking on the diseases pharma has been giving up on for decades. The clearest "what AI actually means for patients" explainer we've published. [YouTube](https://youtu.be/W0NSk2y3OFI?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip) | [Spotify](https://open.spotify.com/episode/2TzHhOkVIN9AL3GXXxSyDe?si=Hfr5NDX1Q_ybcdKSTMdsNQ&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip) | [Apple Podcasts](https://podcasts.apple.com/us/podcast/the-neuron-ai-explained/id1742267001?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip)

### 2\. You've definitely used Canva. But you probably haven't seen it like this: 

[](https://youtu.be/JqZmdg71Bnc?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip)

**[24 Billion AI Uses Later, What Canva Learned About AI Design](https://youtu.be/JqZmdg71Bnc?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip)** — Danny Wu, Canva's Head of AI Products, walks us through how their AI tools have been used **24 BILLION times** , why they spent over a year building a design model that generates _layered, editable_ assets (not just flat images), and how typing one word ("MCP") lets you create fully editable Canva designs from inside ChatGPT, Claude, or Copilot. [YouTube](https://youtu.be/JqZmdg71Bnc?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip) | [Spotify](https://open.spotify.com/episode/1M79tzwFNuqTrCf2d40tFa?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip) | [Apple Podcasts](https://podcasts.apple.com/us/podcast/24-billion-ai-uses-later-what-canva-learned-about-the/id1742267001?i=1000754551676&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip)

### **3\. Your laptop is about to become Hollywood:**

[](https://youtu.be/0WBnAEIkj5A?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip)

**[This Tool Turns Your Laptop Into a Movie Studio](https://youtu.be/0WBnAEIkj5A?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip)** — Yaron Inger, CTO and co-founder of [Lightricks](https://www.lightricks.com/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip) (the company behind Facetune), on why their open-source [LTX-2](https://ltx.io/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip) model has been downloaded **4.5 million times in two months** , runs locally on a consumer GPU, and just ate Pinky-Promise level expensive AI video tools for breakfast. The full [LTX Desktop](https://github.com/Lightricks/LTX-Desktop?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip) editor was vibe-coded by 2.5 people in 10 days. [YouTube](https://youtu.be/0WBnAEIkj5A?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip) | [Spotify](https://open.spotify.com/episode/0W6WTL0ACM3HAI6ND9vUWC?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip) | [Apple Podcasts](https://podcasts.apple.com/us/podcast/ai-just-democratized-filmmaking-w-ltx-co-founder/id1742267001?i=1000754869036&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip)

### **4\. AI feels expensive? Watch this and it'll feel like magic:**

**[The $0.25-Per-Million-Tokens AI Model That Feels Like Magic](https://youtu.be/LQrq3NSBlQU?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip)** — Stefano Ermon, co-founder of [Inception Labs](https://www.inceptionlabs.ai/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip) and Stanford professor, on Mercury, a new kind of language model (diffusion-based, not transformer-based) that could make AI **10x faster** and dramatically cheaper. If you've been stalled on AI because of cost, this is the episode that flips the math. [YouTube](https://youtu.be/LQrq3NSBlQU?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip) | [Spotify](https://open.spotify.com/episode/1HL1foM6m8ql9reKLuKDZu?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip) | [Apple Podcasts](https://podcasts.apple.com/us/podcast/diffusion-for-text-why-mercury-could-make-llms-10x-faster/id1742267001?i=1000751254612&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip)

## One more before you go:

A few weeks ago we went live with the **["AI for Total Beginners" 5-Level Starter Stack](https://www.youtube.com/live/QbFU0UNMVaU?si=YRpR8raOXHvfrBqw&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip)**, a full framework for going from "I've never touched AI" to "AI saves me 10 hours a week." No coding required. It's at 11,000+ views and counting, so it’ll be a good follow-up to this one if you haven’t watch it yet! 

**Last thing:** And if you [haven’t subscribed yet, please do!](https://www.youtube.com/@theneuronai?sub_confirmation=1&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip) Click the image below to go to our channel and hit “subscribe” to get notified right when new videos go live. 

[](https://www.youtube.com/@theneuronai?sub_confirmation=1&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip)

We have a goal to hit **50K subscribers** by the end of the year (if not 100K), and **we’re only 30K away!** If you like learning about AI, and already watch some of our videos, [do us a favor and click here to subscribe](https://www.youtube.com/@theneuronai?sub_confirmation=1&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip) today. 

Stay curious,

The Neuron Team

| That’s all for today, for more AI treats, check out our [website](https://www.theneuron.ai/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip).   
---|---  
  
**P.P.S:** Love the newsletter, but don’t want to receive these podcast announcement emails? Don’t unsubscribe — _[adjust your preferences to opt out of them here instead](https://www.theneurondaily.com/subscribe/f5596641-9099-4045-9641-731cd9fdcf90/preferences?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-first-major-ai-incident-this-year-ceo-warns&_bhlid=1d073d4088b90ea4abf69ef7cc157e0659ada818)_ _._

---

## [😺 Anthropic 🤝 SpaceX data center deal](https://www.theneurondaily.com/p/anthropic-spacex-data-center-deal)
*🧠 The Neuron | 2026-05-07*

Welcome, humans. 

Anthropic ran[ Code with Claude SF](https://claude.com/code-with-claude/san-francisco?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) yesterday, the biggest developer event of its year. The keynote announced a SpaceX partnership for 220,000+ NVIDIA GPUs, doubled Claude Code rate limits, and put GitHub, Datadog, Netflix, Vercel, Cursor, and Replit on stage to defend the platform thesis.

And about an hour into all of that,[ Claude itself briefly went down](https://community.designtaxi.com/topic/28150-is-claude-anthropic-ai-down-may-6-2026/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) for thousands of users (per DownDetector, spiking around 11:16AM ET).

_Truly nothing tells the audience "we're spending billions to fix our compute problem" like the compute problem briefly breaking the app. _

 _By the time the keynote pitched how the_ SpaceX deal _buys 300+ MW of new capacity within the month, the service was back up. There's a reason they need that much!_

**Here’s what happened in AI today:**

  * 😺 Anthropic doubled Claude Code limits and signed a SpaceX compute deal

  * 📰 Apple is talking to Intel and Samsung for US-made device chips

  * 🍪 Adobe unveiled a productivity agent that turns PDFs into interactive AI experiences

  * 🧩 One of these images is real, one is AI; vote below




**A wild Neuron appearance!****** Our own Corey Noles joined [NVIDIA's Nemotron 3 Nano Omni livestream](https://www.youtube.com/watch?v=OymqGF1TxYc&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) this week with Wendell Wilson of Level1Techs for a working dev's take on the new multimodal open model: which model do you reach for and when, how to actually architect coordinated sub-agents, and where multimodal open weights unlock things text-only models can't.

# 😺******Anthropic doubled Claude Code limits and locked up Elon's Memphis data center.**

As established, yesterday was Code with Claude SF, Anthropic's biggest developer day of the year. The opening keynote did what every Anthropic keynote does (announce capacity, demo a feature, parade big customers). 

But the thing that mattered to anyone who's actually used Claude Code in the past six weeks was buried in a single sentence: _the five-hour rate limits just doubled._

**Here's what happened:**

  * Anthropic[ signed a partnership with SpaceX](https://www.anthropic.com/news/higher-limits-spacex?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) for full access to[ Colossus 1](https://www.bloomberg.com/news/articles/2026-05-06/anthropic-inks-computing-deal-with-spacex-to-meet-ai-demand?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal), SpaceX's 300+ MW Memphis data center (yes, the former xAI campus).

  * 220,000+ NVIDIA GPUs come online "within the month."

  * Claude Code's five-hour rate limits **doubled** for Pro, Max, Team, and seat-based Enterprise plans.

  * The peak-hours Claude Code limit reduction is **gone** for Pro and Max.

  * Opus API rate limits went up "considerably."

  * Anthropic also said it's "expressed interest" in partnering with SpaceX on multi-gigawatt **orbital AI compute** (yes, datacenters in space).




Oh no, this couldn’t possibly have anything to do with the very unrelated legal case involving our mutual frenemy ALSO happening at the same time about now…” 

**On the product side, three new**[ ](https://platform.claude.com/docs/en/managed-agents/overview?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal)[Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal)******features dropped at the same keynote** ([per Simon Willison's live blog](https://simonwillison.net/2026/May/6/code-w-claude-2026/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal)):

  * **Multi-agent orchestration** ([research preview](https://platform.claude.com/docs/en/managed-agents/multi-agent?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal)) lets you spawn fleets of agents that hand off subtasks to each other. The on-stage demo built a hypothetical lunar drone-landing system out of three coordinating agents (a Commander, a Detector, and a Navigator).

  * **Outcomes** ([research preview](https://platform.claude.com/docs/en/managed-agents/define-outcomes?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal)) lets you define what success actually looks like, then let Claude iterate until the agent hits that bar instead of just stopping when the prompt ends. 

  * **Dreaming** ([research preview](https://platform.claude.com/docs/en/managed-agents/dreams?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal)) lets you run an agent overnight to inspect its prior sessions, find what it missed, and write itself new memory. The keynote demo: dreaming on a landing task spat out a [descent-playbook.md](https://descent-playbook.md?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) ready to use next time.




For more on these, [watch Claire Vo’s video where she breaks it all down](https://youtu.be/efVfydaUIrM?si=ktkIiGqCEltPuRTb&t=327&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal). 

**Why this matters:****** The last six weeks of Claude Code have been rough. There were[ public performance complaints](https://fortune.com/2026/04/24/anthropic-engineering-missteps-claude-code-performance-decline-user-backlash/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal), brief plan-tier confusion (Claude Code[ briefly removed from Pro](https://www.theregister.com/2026/04/22/anthropic_removes_claude_code_pro/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) before being restored within 24 hours), and a[ Fortune piece](https://fortune.com/2026/04/24/anthropic-engineering-missteps-claude-code-performance-decline-user-backlash/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) where Anthropic admitted to engineering missteps. 

The diagnosis everyone landed on: Anthropic ran out of compute. The reason? Dario said [_they grew by 80x_](https://www.perplexity.ai/page/anthropic-ceo-claims-80x-reven-EehipXoZQ.SnPqCkyA052A?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) last quarter. _Daaaamn, Daniela! (that’s millennial for “i’m impressed)._ The doubled rate limits and SpaceX deal are the answer in two parts.

Now, stack today's announcement against the[ 5GW Amazon deal](https://www.anthropic.com/news/anthropic-amazon-compute?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal), the[ 5GW Google/Broadcom agreement](https://www.anthropic.com/news/google-broadcom-partnership-compute?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal), the[ $30B Microsoft/NVIDIA partnership](https://www.anthropic.com/news/microsoft-nvidia-anthropic-announce-strategic-partnerships?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal), the[ $50B Fluidstack investment](https://www.anthropic.com/news/anthropic-invests-50-billion-in-american-ai-infrastructure?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal), and the[ $200B five-year Google Cloud commitment](https://sherwood.news/markets/alphabet-gains-on-report-that-anthropics-committed-to-spending-200-billion-on-cloud-services-over-the-next-five-years/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) The Information surfaced yesterday _(Anthropic alone now reportedly accounts for more than 40% of Google Cloud's revenue backlog)._

Anthropic is basically signing every cloud and chip deal it can find, and now Elon's data center too. _The same Elon whose Pentagon allies designated Anthropic a "supply chain risk" last quarter. Politics is downstream of gigawatts I guess? _

 _Well, If you’re AGI-pilled, meaning you believe “artificial general intelligence” is imminent and going to lead to a “fast take-off” scenario for technology, then everything is downstream of gigawatts…_

Want to watch it yourself? The[ keynote](https://www.youtube.com/live/GMIWm5y90xA?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) and every[ breakout session](https://www.youtube.com/@claude/streams?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) are on YouTube. Latent Space also [has a nice recap](https://open.substack.com/pub/swyx/p/ainews-anthropic-spacexais-300mw5byr?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) of some other takeaways from Dario and Daniela’s talk and the other sessions. 

**FROM OUR PARTNERS**

### GTM Atlas, by Attio

[](https://atlas.attio.com/?utm_source=beehiiv&utm_medium=newsletter&utm_campaign=beehiiv-Y26-atlas&utm_content=&#123;{publication_alphanumeric_id}}&_bhiiv=opp_311ed0df-17e5-4990-ac54-7e163c91b23c_8ebadeed&bhcl_id=ec4782dc-abe5-43f5-9d81-922fbe0f88a2_&#123;{subscriber_id}}_&#123;{email_address_id}})

Your GTM motion is creative. The thinking behind it should be too.

[GTM Atlas](https://atlas.attio.com/?utm_source=beehiiv&utm_medium=newsletter&utm_campaign=beehiiv-Y26-atlas&utm_content=&#123;{publication_alphanumeric_id}}&_bhiiv=opp_311ed0df-17e5-4990-ac54-7e163c91b23c_8ebadeed&bhcl_id=ec4782dc-abe5-43f5-9d81-922fbe0f88a2_&#123;{subscriber_id}}_&#123;{email_address_id}}) is the ultimate resource on AI GTM for early-stage builders, providing foundational knowledge for teams navigating growth from scratch. Curated by Attio, the AI CRM, Atlas gives you:

  * Systems thinking for every stage of the customer journey

  * Frameworks and templates that scale with you

  * Conversations with GTM operators at Clay, Lovable, and Vercel.




Mapped by operators. Curated by Attio.

[Explore now](https://atlas.attio.com/?utm_source=beehiiv&utm_medium=newsletter&utm_campaign=beehiiv-Y26-atlas&utm_content=&#123;{publication_alphanumeric_id}}&_bhiiv=opp_311ed0df-17e5-4990-ac54-7e163c91b23c_8ebadeed&bhcl_id=ec4782dc-abe5-43f5-9d81-922fbe0f88a2_&#123;{subscriber_id}}_&#123;{email_address_id}})

# 🎓 AI Skill of the Day: **Turn Codex (or Claude Code) into your daily-driver knowledge work cockpit.**

You probably use Codex or Claude Code for code. Austin Tedesco, head of growth at Every, spends roughly[ 80% of his working day inside Codex](https://youtu.be/x9BNBcP_C7Q?t=657&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) doing go-to-market plans, recruiting outreach, KPI tracking, and emails.

His Codex Camp livestream with Dan Shipper yesterday was a 60-minute walkthrough of the exact setup; here's the short version.

The trick is treating the desktop app (not the CLI) as an "agent management interface" for everything you do.[ Austin's setup](https://youtu.be/x9BNBcP_C7Q?t=828&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal):

  1. **Make a folder per work area** (his is called "every growth OS"). Folders give you persistent named chats per project, so you can ship a PR in one chat and draft a strategy doc in another without leaving the app.

  2. **Connect the plug-ins** for everything you live in: Gmail, Slack, Notion, Stripe, your data sources. Then drop in a markdown project file that explains what your business is, your goals, and how you like to work.

  3. **Add reviewer agents.** Austin[ forked compound engineering into "compound knowledge"](https://youtu.be/x9BNBcP_C7Q?t=3043&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) so reviews check for strategic alignment and data accuracy, not security or front-end design.

  4. **Run**[ Austin's recommended starter prompt](https://youtu.be/x9BNBcP_C7Q?t=1112&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) in a fresh chat inside that folder.

  5. **Always do the final human review in the external app** ([Slack drafts, Gmail drafts](https://youtu.be/x9BNBcP_C7Q?t=1362&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal)), never inside Codex; the context switch is what keeps you honest before something goes to a real person.




**Austin's verbatim starter prompt** _(the @ signs in the below refer to apps, so they require you to connect those apps as Plugins; you’d just replace those with w/e tools you use):_
    
    
    Go take a look at the things I use the most (@Notion, @Slack, and @Gmail) and think of some automations that would help me with my work. For each one, explain what it does, when it should run, and which tool it touches. Ask me which ones look good before you build any of them.

Other plays Austin demoed live:[ synthesize meeting transcripts and Slack threads into a draft go-to-market plan](https://youtu.be/x9BNBcP_C7Q?t=1869&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal),[ build a live KPI tracker in Notion that other agents can read](https://youtu.be/x9BNBcP_C7Q?t=2415&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal), and[ find alums of a specific company who later got into AI](https://youtu.be/x9BNBcP_C7Q?t=2694&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) (he used this exact play to surface a perfect L&D hire candidate in under a minute).

**Total AI beginner?**[Start here](https://www.theneuron.ai/explainer-articles/everything-we-covered-in-our-ai-for-total-beginners-livestream-full-guide-with-timestamps/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) ([goes with this video](https://www.youtube.com/live/QbFU0UNMVaU?si=skJsgUIDjKjAx3DU&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal)). 

**Have a specific skill you want to learn?** [Request it here.](https://docs.google.com/forms/d/e/1FAIpQLSd_-hSXtB9ytR1HQrU85IJnJw233bNKptiGB5BZh9maPse1Eg/viewform?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal)

# 🍪 Treats to Try 

  1. [Claude for Microsoft 365](https://www.anthropic.com/news/finance-agents?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) add-ins (Excel, PowerPoint, Word, with Outlook coming soon) drop Claude into your Office ribbon so you can edit cells, build slides, or summarize docs without leaving the file, included with Pro/Max/Team/Enterprise.

  2. [Adobe's productivity agent and PDF Spaces](https://news.adobe.com/news/2026/05/adobes-new-productivity-agent?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) turn any PDF into an interactive experience with a customizable AI Assistant, audio overviews, brand styling, and engagement analytics; recipients can view PDF Spaces with no Adobe account, available in[ Acrobat Studio and the new Acrobat Express tier](https://blog.adobe.com/en/publish/2026/05/06/adobes-new-productivity-agent-redefining-how-we-understand-create-share?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal).

  3. [Baseten's Frontier Gateway](https://www.baseten.co/blog/introducing-baseten-frontier-gateway/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) is the $5B inference company's new product for model labs (open or closed) that want to ship a production API without building the commercial infrastructure;[ Poolside used it to launch its frontier-scale Laguna coding models in 7 weeks](https://www.baseten.co/resources/customers/how-baseten-powered-poolsides-model-launch-in-record-time/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal), priced per usage with no multi-year commitment.

  4. [Claude on Amazon Bedrock](https://platform.claude.com/docs/en/release-notes/overview?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) is now self-serve for all AWS customers in 27 regions, so enterprise teams can hit Opus 4.7 and Haiku 4.5 from the same console they already use, standard Claude API pricing.

  5. [Routines on Claude Code on the web](https://code.claude.com/docs/en/whats-new?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) fire templated cloud agents on a cron schedule, GitHub event, or API call so you can let Claude run audits and PR reviews while you sleep, Max plan only.

  6. [Genspark's AI Developer](https://www.genspark.ai/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) handles code edits, GitHub pull requests, and hosted deploys inside the same workspace that runs its slides, docs, and AI calling agents; the company just crossed $250M ARR and[ partnered with Microsoft](https://www.businesswire.com/news/home/20260429907387/en/Genspark-Announces-Global-Strategic-Partnership-with-Microsoft-to-Embed-AI-Agents-Across-Microsoft-365-and-Agent-365?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) for Office 365 and Agent 365, free trial then $24.99/mo Plus.




# 📰 Around the Horn 

[](https://www.reddit.com/r/RealOrAI/comments/1t58znv/deepfakes_are_everywhere_but_digital_forensics/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal)

Put this to use in the trivia below! 

  * [Apple](https://www.thestreet.com/latest-news/stock-market-today-may-6-2026-updates?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) is in talks with both Intel and Samsung to make its devices' main processors in the US, sending Intel up 6.4% pre-market on the Bloomberg report.

  * [The White House](https://www.nytimes.com/2026/05/04/technology/trump-ai-models.html?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) is reportedly drafting an executive order to pre-vet frontier AI models before release; we[ wrote up the case against it](https://www.theneuron.ai/explainer-articles/the-case-against-a-government-veto-on-ai-models/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) yesterday _(TL;DR: the cure may very well be worse than Mythos)._

  * [Boris Cherny](https://www.youtube.com/live/DlTCu_pNDHE?si=LdI0TMjsIsqbDaHK&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal), the head of Claude Code at Anthropic, livestreamed his actual everyday Claude Code workflow yesterday, the first time the creator of an AI coding tool has done a public, unfiltered "watch me drive" session.




**FROM OUR PARTNERS**

### One brand built 30+ landing pages through Viktor without a single developer.

[](https://ref.getviktor.com/vik-bh-mediabuy-secondary1?utm_campaign=&#123;{publication_alphanumeric_id}}&_bhiiv=opp_01be1fa1-75a7-4998-a4cf-31cb355c6866_dc23507e&bhcl_id=1e0933d0-f489-47f8-aebe-bc870c4e9fb3_&#123;{subscriber_id}}_&#123;{email_address_id}})

Each page mapped to a specific ad group. All deployed within hours. [Viktor](https://ref.getviktor.com/vik-bh-mediabuy-secondary1?utm_campaign=&#123;{publication_alphanumeric_id}}&_bhiiv=opp_01be1fa1-75a7-4998-a4cf-31cb355c6866_dc23507e&bhcl_id=1e0933d0-f489-47f8-aebe-bc870c4e9fb3_&#123;{subscriber_id}}_&#123;{email_address_id}}) wrote the code and shipped every one from a Slack message.

That same team has Viktor monitoring ad accounts across the portfolio and posting performance briefs before the day starts. One colleague. Always on. Across every account.

5,700+ teams. 3,000+ integrations.

[Start free. $100 in credits →](https://ref.getviktor.com/vik-bh-mediabuy-secondary1?utm_campaign=&#123;{publication_alphanumeric_id}}&_bhiiv=opp_01be1fa1-75a7-4998-a4cf-31cb355c6866_dc23507e&bhcl_id=1e0933d0-f489-47f8-aebe-bc870c4e9fb3_&#123;{subscriber_id}}_&#123;{email_address_id}})

# 🧩 Thursday Trivia:

You know the drill: one is AI, and one is real. Which is which? 

A.

B.

# A Cat’s Commentary 

**Trivia answer:** A [is real](https://www.reddit.com/r/RealOrAI/comments/1szxddk/is_this_ai_why_isnt_the_cat_running_away_and/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal)  _(although my partner literally doesn’t believe me, it is a ACTUAL cat crying while its owner cuts onions), and_[ _B is AI._](https://www.reddit.com/r/aivideo/comments/1t0a8u0/futurama_live_action_cast/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal)__

|  That’s all for now.   
---|---  
  
**P.P.S:** Love the newsletter, but only want to get it once per week? Don’t unsubscribe—[update your preferences here](https://www.theneurondaily.com/subscribe/f5596641-9099-4045-9641-731cd9fdcf90/preferences?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal).

---

## [😺 🎙️ Watch: How Isomorphic Labs works to drug "undruggable" diseases](https://www.theneurondaily.com/p/watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)
*🧠 The Neuron | 2026-05-06*

[](https://youtu.be/W0NSk2y3OFI?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)

Click the image above to watch on YouTube!

[](https://clickup.com/lp?utm_source=technologyadvice&utm_medium=cpl&utm_campaign=ilab_cpl_na_nnc_pro_trial_all-devices_cpc_lp_x_all-departments_x_general)

Welcome, humans. 

Did you know that the average new drug takes [over a decade and roughly $6B](https://www.isomorphiclabs.com/articles/the-isomorphic-labs-drug-design-engine-unlocks-a-new-frontier?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases) to reach the market? Or that ~**90% of compounds that enter clinical trials** _**fail?**_

That's the hard wall that the entire pharma industry has been hitting for decades.

Well, you probably _do_ know about [AlphaFold](https://deepmind.google/science/alphafold/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases), the [Google DeepMind](https://deepmind.google/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases) AI that solved a 50-year-old protein folding problem and won its creators the [2024 Nobel Prize in Chemistry](https://www.nobelprize.org/prizes/chemistry/2024/press-release/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases). 

**What you might not know:** the team behind AlphaFold 3 is now designing _real_ drugs, and they just published a [technical report](https://storage.googleapis.com/isomorphiclabs-website-public-artifacts/isodde_technical_report.pdf?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases) showing their new system more than doubles AlphaFold 3's accuracy on the hardest part of drug design.

That team is [Isomorphic Labs](https://www.isomorphiclabs.com/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases), a DeepMind spinout led by Demis Hassabis. And in [**our latest podcast episode**](https://youtu.be/W0NSk2y3OFI?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases), we sit down with **Becky Paul** (who leads medicinal drug design) and **Michael Schaarschmidt** (who leads foundational AI research) at Isomorphic Labs to unpack what AlphaFold actually unlocked, why drug discovery is still brutally hard, how AI drug discovery works from a process standpoint, and where (as well as how) their AI is starting to design molecules that human chemists couldn't.

[](https://youtu.be/W0NSk2y3OFI?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)

Click the image above to watch on YouTube!

# Our favorite moments:

  * **(****[2:13](https://youtu.be/W0NSk2y3OFI?feature=shared&t=133&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)****) The brutal math of drug discovery:** A decade of work. ~$6B per drug. 90% of clinical trial entrants fail. Becky lays out exactly why pharma needs something disruptive.

  * **(****[7:27](https://youtu.be/W0NSk2y3OFI?feature=shared&t=447&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)****) AI just replaced a PhD's worth of work:** Their structure prediction model now matches X-ray crystal structures so well, the team is starting to skip the (slow, expensive) experimental step entirely.

  * **(****[12:19](https://youtu.be/W0NSk2y3OFI?feature=shared&t=739&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)****) Why AlphaFold 3 took 2 years for anyone else to copy:** Even with the full paper, open code, and inference algorithms published, no other lab could fully reproduce it. Michael on the modeling details that don't fit in a paper.

  * **(****[15:11](https://youtu.be/W0NSk2y3OFI?feature=shared&t=911&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)****) "I've never worked somewhere where the pace of innovation is so fast":** Becky on what it's like when the ML team next door drops a new foundation model that suddenly unblocks a project that was stuck.

  * **(****[19:08](https://youtu.be/W0NSk2y3OFI?feature=shared&t=1148&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)****) Beyond binding, drugs that delete proteins:** The molecular glue revolution, where new drugs don't just block a target, they tag it for destruction inside your cells.

  * **(**[**26:37**](https://youtu.be/W0NSk2y3OFI?feature=shared&t=1597&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)**) Becky’s pie-in-the-sky dream:** One design cycle. A few hundred molecules. A drug candidate at the end. What "AI-first drug discovery" actually looks like at the limit.

  * **(**[**36:36**](https://youtu.be/W0NSk2y3OFI?feature=shared&t=2196&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)**) "How did it know that?":** The most exciting moments aren't when the model is right, they're when the model makes a leap the team can't explain. 

  * **(****[40:13](https://youtu.be/W0NSk2y3OFI?feature=shared&t=2413&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)****) The "undruggable" protein, drugged:** [KRAS](https://en.wikipedia.org/wiki/KRAS?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases) was labeled untouchable for decades. Recent KRAS drugs are now [doubling survival in pancreatic cancer](https://www.nature.com/articles/d41586-024-04204-5?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases). Becky and Michael's bet: AI shrinks the next "undruggable" target from a multi-decade slog to something tractable.




**Why watch this?** Most "AI in healthcare" news to date has been vague optimism or more administrative than groundbreaking. This is the opposite. Two practitioners walking through exactly which steps of drug design are now AI-first, which still need wet-lab work, and where the next breakthroughs are coming from. 

If you've ever wondered what AlphaFold actually means for patients (not just scientists), or why Demis keeps saying biology is the ultimate AI application, plus how the team at Isomorphic approaches the _incredibly complicated_ task in front of them, then this is the clearest 50 minutes you'll find on it.

**Watch and/or Listen now:** **[YouTube](https://youtu.be/W0NSk2y3OFI?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)** | **[Spotify](https://open.spotify.com/episode/2TzHhOkVIN9AL3GXXxSyDe?si=Hfr5NDX1Q_ybcdKSTMdsNQ&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)**

**P.S.** At [(7:27)](https://youtu.be/W0NSk2y3OFI?feature=shared&t=447&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases) Becky describes the moment a chemist has to stop validating the model and start trusting it. _That's a quietly wild thing for a scientist to say out loud…._

**Dive deeper with these resources:**

  * [Technical report blog](https://www.isomorphiclabs.com/articles/the-isomorphic-labs-drug-design-engine-unlocks-a-new-frontier?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases) (the easiest read, with all the visuals). 

  * [Full technical report (PDF)](https://storage.googleapis.com/isomorphiclabs-website-public-artifacts/isodde_technical_report.pdf?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases) (for the chemists and ML folks). 

  * [Isomorphic Labs](https://www.isomorphiclabs.com/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases) (they're hiring across [Boston, London, and Lausanne](https://www.isomorphiclabs.com/job-openings?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)!).




_**Real quick:**__Want to see your AI-adjacent product or service show up right here, below these podcast promos? Click the button below to advertise to our 700K+ readers!_

[_Advertise in The Neuron here!_](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)

**THIS EPISODE WAS BROUGHT TO YOU BY…**

# We use ClickUp to publish 2,000+ pieces a month.

Across 18 spaces and 100 contributors, [ClickUp](https://clickup.com/lp?utm_source=technologyadvice&utm_medium=cpl&utm_campaign=techa_cpl_na_nnc_pro_trial_all-devices_cpc_lp_x_all-departments_x_general) is the operating system that holds our parent company (TechnologyAdvice)'s work all together. ClickUp's AI layer ([ClickUp Brain](https://clickup.com/lp?utm_source=technologyadvice&utm_medium=cpl&utm_campaign=techa_cpl_na_nnc_pro_trial_all-devices_cpc_lp_x_all-departments_x_general)) plugs into your tasks, docs, Slack, Gmail, and Salesforce; you pick the underlying model (Claude, GPT, or Gemini). Active users save **1.1 days weekly** and see **3x faster task completion**.

Oh, and did we mention the [Free Forever plan](https://clickup.com/lp?utm_source=technologyadvice&utm_medium=cpl&utm_campaign=techa_cpl_na_nnc_pro_trial_all-devices_cpc_lp_x_all-departments_x_general) has unlimited tasks and users?! Check it out!

→ [Try ClickUp free](https://clickup.com/lp?utm_source=technologyadvice&utm_medium=cpl&utm_campaign=techa_cpl_na_nnc_pro_trial_all-devices_cpc_lp_x_all-departments_x_general)

# 🔴 LIVE TOMORROW: The AI Starter Kit, What to Try… and What to Ignore

[](https://www.youtube.com/live/WKZSEEBiaNo?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)

Click the image to go to YouTube, then click "Notify Me" to get notified when we go live!

This week, Grant and Corey are going to cut through the AI noise for anyone who's still on the sidelines. New to AI, or know someone who is? This is the session to send them.

**We'll cover:**

  * The best first steps for AI beginners

  * What tools and features are actually worth trying right now

  * What you can safely ignore for the moment

  * Simple ways to get better answers from any AI tool

  * How to troubleshoot when AI gives you something unhelpful




**Choose your favorite platform to watch live:** [**Watch on YouTube**](https://www.youtube.com/live/WKZSEEBiaNo?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases) | [**Join on LinkedIn**](https://www.linkedin.com/posts/ai-artificialintelligence-aibeginners-ugcPost-74578275?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)

# 🎙️ In Case You Missed It… 

Four recent interviews you’ll definitely want to check out _(pick whatever looks interesting to you and dive in!):_

### 1\. Interested in what's missing before we hit AGI? Watch: [This Company Mapped the Entire World in 3D. Here's Why.](https://youtu.be/erCV1MJXU3g?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)

[](https://youtu.be/erCV1MJXU3g?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)

**TL;DW:** Peter Wilczynski, CPO at [Vantor](https://vantor.com/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases) (formerly Maxar), built a 3D model of the entire Earth at 50cm resolution and made it machine-readable. He argues spatial intelligence is the gap nobody's talking about in AI, and probably the missing piece before agents can actually operate in the physical world.

**Why you should watch:** If you've ever wondered why AI can write code and solve math olympiad problems but still can't reliably tell a drone where to go, this one answers it. Also, there's a wild bit about how the physical world becomes the new navigation layer for AI agents.

  * **YouTube:** [Watch Here](https://youtu.be/erCV1MJXU3g?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)

  * **Spotify:** [Listen Here](https://open.spotify.com/episode/71rhDuYFzTlsF0uaIq91QU?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)

  * **Apple Podcasts:** [Listen Here](https://podcasts.apple.com/us/podcast/this-company-mapped-the-entire-world-in-3d-heres-why/id1742267001?i=1000761587268&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)




### **2\. Curious how good AI music tools have actually gotten? Watch:****[This AI Just Made Our Podcast Theme Song](https://youtu.be/r4aMWjhoMHU?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)**

[](https://youtu.be/vJD2FjVUEhg?si=Mdm2w9GHHSZwZ2A8&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)

**TL;DW:** Corey sits down with **Kendall Rankin** , who left LinkedIn in 2024 to join [Producer AI](https://www.flowmusic.app/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases) when it was a startup (advised by The Chainsmokers, no less). Google acquired the team in February 2026, and Kendall is now on the Flow Music team inside Google Labs. On the episode, they generate a garage rock song from a single sentence, build a custom synth in the "Spaces" feature, and walk through SynthID watermarking and one-shot music videos.

**Why you should watch:** Most AI music demos hand you a polished finished song and skip the part where things go sideways. This episode is the part where things go sideways. First pass fumbles, Corey asks for "more fuzz," second pass actually lands. That iteration loop is the whole story for anyone trying to figure out if these tools are actually usable.

  * **YouTube:** [Watch Here](https://youtu.be/r4aMWjhoMHU?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)

  * **Spotify:** [Listen Here](https://open.spotify.com/show/4gF6uNmkzEYq2E0sHeuMuU?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)

  * **Apple Podcasts:** [Listen Here](https://podcasts.apple.com/us/podcast/the-neuron-ai-explained/id1742267001?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)




### 3\. Want agents that actually work on real tasks? Watch: [Inside the Secret Labs Where AI Learns to Work](https://youtu.be/WhbdbbERzNg?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)

[](https://youtu.be/WhbdbbERzNg?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)

**TL;DW:** Nick Heiner, VP of Product at [Surge AI](https://www.surgehq.ai/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases) (a $1.2B-revenue company built without VC money), reveals why even GPT-5, Claude, and Gemini still fail about 40% of real workplace tasks, what makes a good RL environment, and his bold prediction of a $1B company with one human employee by 2030.

**Why you should watch:** If you're trying to get AI agents to actually finish real work (and not just demo well), this is the missing piece on why they keep falling short.

  * **YouTube:** [Watch Here](https://youtu.be/WhbdbbERzNg?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)

  * **Spotify:** [Listen Here](https://open.spotify.com/episode/6MAFKIJVL4Gt57lEEqCs6F?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)

  * **Apple Podcasts:** [Listen Here](https://podcasts.apple.com/us/podcast/inside-the-secret-labs-where-ai-learns-to-work/id1742267001?i=1000757358598&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)




### 4\. Interested in where AI meets actual factories? Watch: [80% of US Factories Have Zero Robots. Google Wants to Fix That.](https://youtu.be/zv1_d8K-Jms?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)

[](https://youtu.be/zv1_d8K-Jms?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)

**TL;DW:** [Intrinsic](https://www.intrinsic.ai/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases) (a Google Alphabet company) CTO Brian Gerkey co-created [ROS](https://www.ros.org/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases), the open-source software running more than 1 million robots including NASA's. He explains why most US factories still have zero automation, and how generative AI is about to change that.

**Why you should watch:** If you think "AI and robotics" is still science fiction for your industry, this interview resets the timeline. The factory floor is where the next AI wave actually lands.

  * **YouTube:** [Watch Here](https://youtu.be/zv1_d8K-Jms?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)

  * **Spotify:** [Listen Here](https://open.spotify.com/show/4gF6uNmkzEYq2E0sHeuMuU?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)

  * **Apple Podcasts:** [Listen Here](https://podcasts.apple.com/us/podcast/the-neuron-ai-explained/id1742267001?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)




## One more before you go:

If today's episode got you thinking about the AlphaFold side of DeepMind, our [recent interview with Ioannis Antonoglou](https://youtu.be/3rarFbFqVXQ?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases) (one of the AlphaGo co-creators) is the natural next watch. 

Different DeepMind alum, completely different bet on what frontier AI looks like next. _This is very relevant now that the US government will start vetting AI models before they’re releases, or potentially outright banning AI models from certain countries._

**Last thing:** And if you **haven’t subscribed yet, please do!** Click the image below to go to our channel and hit “subscribe” to get notified right when new videos go live. 

[](https://www.youtube.com/@theneuronai?sub_confirmation=1&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)

We have a goal to hit **50K subscribers** by the end of the year (if not 100K), and **we’re only ~30K away!** If you like learning about AI, and already watch some of our videos, [do us a favor and click here to subscribe](https://www.youtube.com/@theneuronai?sub_confirmation=1&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases) today. 

Stay curious,

The Neuron Team

| That’s all for today, for more AI treats, check out our [website](https://www.theneuron.ai/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases).   
---|---  
  
**P.P.S:** Love the newsletter, but don’t want to receive these podcast announcement emails? Don’t unsubscribe — _[adjust your preferences to opt out of them here instead](https://www.theneurondaily.com/subscribe/f5596641-9099-4045-9641-731cd9fdcf90/preferences?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-first-major-ai-incident-this-year-ceo-warns&_bhlid=1d073d4088b90ea4abf69ef7cc157e0659ada818)_ _._

---

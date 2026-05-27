---
title: "TheSequence — 2026-05-24"
date: 2026-05-24
source: TheSequence
type: ai-news
---

# 🔢 TheSequence — 2026-05-24

> 165k+ 訂閱；ML / 企業 AI 應用週報，Jesus Rodriguez 主筆
> 來源：[TheSequence](https://thesequence.substack.com/feed)

---

## [The Sequence Opinion #864: Every AI Agent Needs a Computer](https://thesequence.substack.com/p/the-sequence-opinion-864-every-ai)
*🔢 TheSequence | 2026-05-21*

The next phase of AI agents will not be defined only by better models, longer context windows, or more elegant tool-calling APIs, but by something much more primitive: access to a computer. An agent that can only emit tokens is a brilliant brain in a jar; an agent with a filesystem, terminal, browser, network, package manager, credentials, memory, and guardrails becomes a worker inside a real execution environment. This is the core thesis: every serious AI agent needs a computer, not metaphorically, but architecturally. It needs a safe, isolated, programmable space where it can write code, run commands, inspect outputs, manipulate files, browse the web, recover from errors, and iterate through the same feedback loops that make software useful. The emerging market for micro-containers, sandboxes, browser runtimes, and agent workspaces is really the market for giving intelligence a body.

The Brain in the Jar Problem

[
Read more
](https://thesequence.substack.com/p/the-sequence-opinion-864-every-ai)

---

## [The Sequence AI of the Week #863: The Model is the Interface: Inside Thinking Machines' Interactive Models](https://thesequence.substack.com/p/the-sequence-ai-of-the-week-863-the)
*🔢 TheSequence | 2026-05-20*

For this week in AI’s essay, I would like to discuss Thinking Machines’ work on interactive models which takes multi-modality to a new level. I’ve been diving as much as possible on their ideas and wanted to share some thoughts. The work is early but so impressive. Check it out to get started: 

For the last few years, the default mental model for large language models has been embarrassingly simple: concatenate tokens, predict the next token, repeat. The human writes a message, the model replies, the human writes again. This works surprisingly well for many tasks because text is forgiving. Text can wait. It can be buffered, edited, compressed, and serialized into one neat causal stream.

But collaboration is not text. Collaboration is temporal.

[
Read more
](https://thesequence.substack.com/p/the-sequence-ai-of-the-week-863-the)

---

## [The Sequence Knowledge #862: Learning About Text Diffusion Models](https://thesequence.substack.com/p/the-sequence-knowledge-862-learning)
*🔢 TheSequence | 2026-05-19*

💡 AI Concept of the Day: What are Text Diffusion Models

If you look at the architecture of the modern AI boom, it is heavily bifurcated by modality. In the visual domain, we are entirely ruled by diffusion models. From Midjourney to Stable Diffusion to OpenAI’s Sora, the paradigm of starting with pure noise and iteratively denoising it into a high-fidelity image or video has proven to be unreasonably effective.

But in the realm of text, diffusion has historically been an afterthought. Large Language Models (LLMs) like GPT-4, Claude, and LLaMA are staunchly autoregressive (AR). They are sequence predictors. They look at the context, predict the next token, append it to the context, and repeat. It is a strictly left-to-right, causal process.

For years, the consensus was simple: autoregression is just the native physics of language. But this sequential paradigm has glaring pathologies. Because AR models generate blindly from left to right, they cannot easily engage in global planning. If they make a slight logical error early in a sequence, that error is committed to the context window permanently, leading to cascading failures—a phenomenon often critiqued as “generation drift.” Furthermore, AR models suffer from the “reversal curse”; they can easily recite a poem forward, but if you ask them to recite it backward, their causal attention mechanisms break down entirely.

[
Read more
](https://thesequence.substack.com/p/the-sequence-knowledge-862-learning)

---

## [The Sequence Radar #861: Last Week in AI: IPOs, Interactive Models, and Recursive Dreams](https://thesequence.substack.com/p/the-sequence-radar-861-last-week)
*🔢 TheSequence | 2026-05-17*

Next Week in The Sequence:

We continue our series about trasnformer alternatives. 

In our opinion section, we discuss the thesis that “every agent needs a computer” 

In the AI of the Week section, we dive into Thinking Machines’ interactive models which can think and listen and same time. 

Subscribe and don’t miss out:

📝 Editorial: Last Week in AI: IPOs, Interactive Models, and Recursive Dreams

This week in AI felt less like a product cycle and more like a philosophical provocation wrapped in a market event, a demo, and a few delightfully ambitious lab announcements. The common thread was not bigger models, larger context windows, or yet another benchmark victory. It was agency. Who gets to shape intelligence? Who gets to improve it? And, slightly more ominously, what happens when the tools begin improving the tools?

Start with Cerebras. The IPO was not just a financing milestone for an AI chip company; it was a reminder that the AI race is still brutally physical. Behind every magical chatbot sits an industrial stack of silicon, power, networking, cooling, capital markets, and geopolitical anxiety. Cerebras has always been the wonderfully weird character in the AI hardware opera: instead of making chips modestly larger, it went all-in on the wafer-scale computer, basically asking, “What if the chip were the data center?” That sounds like something invented after too much espresso at a semiconductor conference, but it captures an important truth. If intelligence is becoming a commodity, compute remains the refinery. Public markets are now voting on which refineries matter.

Then came Thinking Machines with its interaction models, and the shift in mood was immediate. While much of the industry keeps celebrating autonomous agents that disappear into the cloud and return with a spreadsheet, Thinking Machines is betting on the opposite: AI that stays present. Not “prompt, wait, receive,” but continuous, multimodal collaboration. The model listens, watches, interrupts, yields, and reacts in real time. In other words, it treats interaction not as a UI layer bolted onto intelligence, but as part of intelligence itself. This is a subtle but profound idea. Human cognition is social before it is computational. We think through gestures, pauses, corrections, shared context, and awkward silences. Making AI more useful may require making it less like an oracle and more like a very fast, very attentive collaborator who knows when not to talk.

The most intellectually spicy developments, however, came from the new “AI scientist” movement. Recursive emerged with the grand ambition of building systems that improve themselves through automated experimentation. Adaption’s AutoScientist pointed in a similarly important direction, automating the loop behind training, alignment, and model adaptation. The dream here is intoxicating: research no longer as a linear human process, but as a compounding machine of hypotheses, experiments, evaluations, and refinements.

That dream also deserves a raised eyebrow. Recursive self-improvement has long lived somewhere between computer science, science fiction, and existential risk seminar. Turning it into a venture-backed product category is both thrilling and slightly unhinged — which, frankly, is how many important technologies begin. The question is not whether AI can help with research. It already does. The question is whether we can build systems that improve capabilities without eroding grounding, safety, diversity, or human judgment.

Another signal came from China, where Junyang Lin, the former lead researcher behind Alibaba’s Qwen models, is reportedly raising several hundred million dollars for a new AI lab at a valuation that could land around $2 billion. That number is almost rude for a brand-new lab — especially in China, where AI startup valuations tend to be more earthbound than in the U.S. — but Lin has the rare credential that matters in frontier AI: he has already helped turn a model family into an ecosystem. His departure also exposes a delicious tension inside Chinese AI: as Alibaba shifts more energy toward proprietary models and monetization, the open-source talent orbit may be ready to spin out into independent labs. But this is not simply a “raise money, buy GPUs, train model, repeat” story. New Chinese AI labs must navigate U.S. chip export controls, constrained compute access, and the tricky problem of building research agendas that do not merely overlap with giants like Alibaba and ByteDance. In that sense, Lin’s new lab is less another shiny founder myth than a test case for whether China’s open-model momentum can become a venture-scale company.

The machine is no longer just answering. It is listening, adapting, experimenting — and, perhaps, beginning to ask what it should become next.

🔎 AI Research

[MemEye: A Visual-Centric Evaluation Framework for Multimodal Agent Memory](https://arxiv.org/html/2605.15128v1)[ ](https://arxiv.org/html/2605.15128v1)

AI Lab: Rutgers, Notre Dame, Princeton, UMN, SAMD 

Summary: MemEye is a novel evaluation framework and benchmark designed to assess whether multimodal AI agents can effectively preserve and reason over fine-grained visual evidence in long-term interactions. By evaluating 13 memory methods, the authors reveal a critical trade-off where text-based memory loses visual details while native image memory struggles with tracking temporal state changes.

[EVOLVEMEM: Self-Evolving Memory Architecture via AutoResearch for LLM Agents](https://arxiv.org/html/2605.13941v1)[ ](https://arxiv.org/html/2605.13941v1)

AI Lab: UNC-Chapel Hill, UC Berkeley, UCSC 

Summary: EVOLVEMEM introduces a self-evolving memory architecture that uses an LLM-powered diagnosis module to autonomously optimize its own retrieval configuration based on failure logs. This closed-loop process allows the system to discover and refine effective retrieval strategies dynamically, significantly outperforming static baseline models on long-term memory benchmarks.

[Orchard: An Open-Source Agentic Modeling Framework](https://arxiv.org/html/2605.15040v1)[ ](https://arxiv.org/html/2605.15040v1)

AI Lab: Microsoft Research, Columbia University, UIUC 

Summary: Orchard is an open-source framework built around a lightweight, Kubernetes-native environment service that decouples sandbox management from agent harnesses to enable scalable, cost-effective agentic training. The framework includes specialized training recipes for software engineering, web navigation, and personal assistant tasks, demonstrating state-of-the-art performance and strong generalization across diverse agent domains.

[NEXUS: An Agentic Framework for Time Series Forecasting](https://arxiv.org/html/2605.14389v1)[ ](https://arxiv.org/html/2605.14389v1)

AI Lab: Google, Pennsylvania State University 

Summary: NEXUS is a multi-agent framework that improves time series forecasting by explicitly decomposing the task into macro-level trend projection, micro-level granular analysis, and dynamic synthesis of numerical and textual contexts. By separating these reasoning stages and incorporating a calibration loop, the system matches or exceeds the accuracy of dedicated numerical foundation models while providing highly interpretable forecasting rationales.

[GLiGuard: Schema-Conditioned Classification for LLM Safeguard](https://arxiv.org/abs/2605.07982)[ ](https://arxiv.org/abs/2605.07982)

AI Lab: Fastino Labs 

Summary: GLiGuard is a highly efficient, 0.3B-parameter bidirectional encoder designed for real-time LLM content moderation by encoding task definitions and label semantics directly into the input schema. This non-autoregressive architecture evaluates prompt safety, response safety, harm categories, and jailbreak strategies simultaneously in a single forward pass, achieving competitive accuracy with models up to 90 times larger while drastically reducing inference latency.

🤖 AI Tech Releases

Interaction Models

Thinking Machines [unveiled a research preview of Interaction Models](https://thinkingmachines.ai/blog/interaction-models/): frontier models in which interactions is built in the model and not in the harness. 

📡10 AI News You Need to Know About

[Cerebras IPO debut](https://www.cerebras.ai/press-release/cerebras-systems-announces-pricing-of-initial-public-offering)[ ](https://www.cerebras.ai/press-release/cerebras-systems-announces-pricing-of-initial-public-offering): Cerebras priced its IPO at $185/share to raise $5.55B, and shares then soared 68% in their Nasdaq debut on May 14, pushing the AI chipmaker’s market cap to roughly $95B.

[Recursive Superintelligence emerges from stealth](https://www.recursive.com/): Former Salesforce chief scientist Richard Socher launched Recursive Superintelligence with $650M at a $4.65B valuation — led by GV and Greycroft with Nvidia and AMD Ventures participating — to build AI systems that recursively improve themselves through open-ended algorithms, starting with automating AI research itself.

[OpenAI weighs suing Apple](https://techcrunch.com/2026/05/14/openai-is-reportedly-preparing-legal-action-against-apple-it-wouldnt-be-the-first-partner-to-feel-burned/): OpenAI has hired an outside law firm and is considering legal action against Apple over the ChatGPT-Siri integration, which it claims has been buried in the UI and has fallen far short of projected subscription revenue.

[Cisco cuts ~4,000 jobs while posting record revenue](https://blogs.cisco.com/news/our-path-forward): Cisco is cutting roughly 5% of its workforce to redirect spending toward AI and cybersecurity, even as it touts record quarterly revenue and double-digit growth.

[Adaption launches AutoScientist](https://www.adaptionlabs.ai/blog/autoscientist): Sara Hooker’s Adaption Labs unveiled AutoScientist, an automated fine-tuning system that co-optimizes data and model recipes and which the company says outperformed its in-house researchers by 35% (lifting win-rates from 48% to 64%), free for 30 days.

[Musk v. Altman closing arguments](https://www.bloomberg.com/news/articles/2026-05-14/musk-altman-make-final-pitches-to-jury-in-battle-over-openai): Lawyers for Musk and OpenAI delivered closing arguments in Oakland federal court on May 14, with the nine-person jury set to begin deliberating Monday on whether Altman and Brockman breached commitments to keep OpenAI a nonprofit.

[xAI launches Grok Build](https://x.ai/news/grok-build-cli): xAI rolled out an early beta of Grok Build, a new terminal-based coding agent and CLI for SuperGrok Heavy subscribers ($300/month), as Musk tries to close the coding-quality gap with Anthropic’s Claude.

[Nebius Q1 sales up 684%](https://nebius.com/newsroom/nebius-reports-first-quarter-2026-financial-results): Nebius reported Q1 2026 revenue of $399M (up 684% YoY) and adjusted EBITDA of $129.5M, and announced it has secured up to 1.2 GW of power and land for a new owned AI factory in Pennsylvania.

[Wispr in funding talks at $2B](https://www.bloomberg.com/news/articles/2026-05-12/ai-dictation-startup-wispr-in-funding-talks-at-2-billion-value): Wispr AI, maker of the Wispr Flow voice dictation tool, is in talks for a ~$260M round led by Menlo Ventures that would value the company near $2B — nearly triple its $700M valuation from late 2025.

[Former Alibaba Qwen lead launches new AI lab at ~$2B valuation](https://x.com/theinformation/status/2054645118758433089)[ ](https://x.com/theinformation/status/2054645118758433089): Junyang Lin, the former lead researcher behind Alibaba’s open-source Qwen models, is in talks with Chinese VCs Gaorong Ventures and HongShan to raise several hundred million dollars for a new AI lab at a roughly $2B post-money valuation — a level almost unheard of for a brand-new Chinese AI startup.

---

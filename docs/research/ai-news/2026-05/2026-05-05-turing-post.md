---
title: Turing Post — 2026-05-05
date: 2026-05-05
source: Turing Post
type: ai-news
---

# 🏛️ Turing Post — 2026-05-05

> Ksenia Se 主持，95k+ 訂閱；AI/ML 政策、地緣政治與深度洞察
> 來源：[Turing Post](https://turingpost.substack.com/feed)

---

## [FOD#151: Recursive Self-Learning: Why It Matters Now](https://turingpost.substack.com/p/fod151-recursive-self-learning-why)
*🏛️ Turing Post | 2026-05-05*

This Week in Turing Post:

Wednesday / AI 101 series: Agentic Vector Database (it’s new and hot!)

Friday / The Org Age of AI: we continue our series 

🔥 Which AI skills will actually matter in 2026?

That’s one of the most important questions! On May 14, I’m co-hosting AI Skills Conf – a practical online conference on the workflows, tools, and decisions professionals will actually need in 2026. 

You should[ join me.](https://conf.cosprints.ai/?37) The sessions I’d most recommend: 

How to become irreplaceable with AI 

The 2026 AI tool stack for founders and small-business owners 

AI ROI reality check: which use cases are delivering business value?

As we know, the professionals who stay irreplaceable are not the ones who fear AI. They’re the ones who learn how to use it before everyone else does.

The event is free and super practical. You should be there →

[REGISTER NOW](https://conf.cosprints.ai/?37)

To the main topic → Everyone talks about Recursive Self-Learning

Loops are the basic unit of machine learning. A model predicts, gets feedback, updates.

An agent does a bit of the same: writes code, runs tests, edits, runs the tests again. A system catalogues its own failure, stores the lesson, and tries a different route next time.

For most of AI’s history, there has been a constant outside that loop: a human – Human in the Loop, in the field’s vocabulary. Now the human is the bottleneck.

Recursive self-learning (RSL) is a way to change it, and it’s already shifting that boundary.

In his recent tweet, Jack Clark, Anthropic co-founder and now Head of Public Benefit, wrote: 

What is recursive self-learning, anyway?

The idea has been in the air lately even without the name. Andrej Karpathy’s [autoresearch](https://github.com/karpathy/autoresearch) is the cleanest small example. An agent is given a real LLM training script, edits the code, runs a fixed five-minute experiment, measures validation bits-per-byte, keeps the change if it improves the result, discards it if it does not, and repeats. What autoresearch removes from the loop is Karpathy – because Karpathy is the bottleneck. He still sets the metric, the budget, and the initial research program. He is no longer inside every iteration. He has moved up one level, from tuning the experiment to designing the loop that tunes it. 

That is the useful way to think about recursive self-learning. It is not a model waking up and choosing to become a better model. It is a system beginning to automate parts of the process by which the system – or systems like it – get better: writing code, generating training data, running experiments, optimizing kernels, fine-tuning models, building evaluations, improving prompts, improving tools, and eventually helping train successor systems.

The history of recursive self-learning

The idea is older than the field. In 1950, Alan Turing proposed building a “child machine” and educating it, rather than programming adult intelligence directly. Arthur Samuel’s checkers program in the late 1950s improved through self-play and showed that a machine could get better at a task without each improvement being hand-coded. I.J. Good made the strongest version of the argument in 1965: if designing better machines is itself an intellectual task, then a machine better than humans at intellectual tasks would design an even better one. Jürgen Schmidhuber gave the loop a formal expression in 2003 with the [Gödel Machine](https://arxiv.org/abs/cs/0309048) – a system that rewrites its own code once it can prove the rewrite is an improvement. For over six decades, almost all of this remained theoretical.

The practical versions were narrow. AlphaGo Zero improved through self-play, but Go is a closed world: fixed rules, clean reward, no hidden state. AutoML, neural architecture search, self-distillation, and synthetic-data pipelines all added components – proof that machines could help improve machine-learning systems, always inside a frame a human had built.

What is changing now is that the loop is moving into AI R&D itself 

AI research has an unusual property: most of the work is already digital. Code, data, training runs, evaluation scripts, benchmarks, logs, dashboards. The day-to-day is not lightning-strike insight; it is running variants, finding errors, improving throughput, testing ideas, comparing scores, and deciding what to try next. That makes it tractable for automation in a way that, for example, biology research is not.

This is the spine of Jack Clark’s latest [Import AI](https://importai.substack.com/p/import-ai-455-automating-ai-research) essay. His headline claim is a 60%+ probability that “no-human-involved AI R&D” – a system capable of training its own successor – arrives by the end of 2028. The argument is not one benchmark but the accumulation: SWE-Bench, METR time horizons, CORE-Bench, MLE-Bench, PostTrainBench, kernel optimization, automated alignment research, and AI systems managing other AI systems. The case is a mosaic of partial loops beginning to connect.

From the [No Priors podcast](https://www.youtube.com/watch?v=kwSVtQ7dziU), we learn that, according to Karpathy, the most interesting version of RSL is probably what frontier labs are already working on: experiment on smaller models, make the process as autonomous as possible, and remove researchers from as much of the execution loop as you can. Researchers can still contribute ideas, but they should not be manually enacting every idea. That changes a researchers job a lot. 

The academic community has begun catching up to the framing as well. The [ICLR 2026 workshop on recursive self-improvement](https://recursive-workshop.github.io/) describes the field as moving from speculative vision to a concrete systems problem: what changes, when it changes, how the change is produced, where the system operates, and how alignment, evaluation, and rollback should work. Recursive self-learning has gained some practical weight and is becoming a design problem with parameters. 

There is even a month old startup with the name “Recursive Superintelligence” that just raised $500 million for self-learning AI. So, you know, it’s all serious. 

I want to leave you with this

For decades, we built systems that learned inside loops. We are now building systems that may learn how to build the loops. And we will be learning alongside them: what “better” means once the system is also helping decide what “better” counts as.

There is another obligation here. When a system begins evolving autonomously, it needs rigorous, continuous verification and alignment, so its improvement loop remains anchored to human safety and well-being. Both are very hard problems, because we still do not really know how these machines “think.”

If any of those thoughts resonate with you – share them across your social networks. Let’s keep the conversation going. 

Topic 2: That used to be a great, impactful writing! And now it’s a sign of slop. How did that happen? featuring Apostle Paul. [Watch →](https://youtu.be/_pdVPTL_1tI)

Follow us on 🎥[ YouTube](https://www.youtube.com/@RealTuringPost) [Twitter](https://x.com/TheTuringPost) [ Hugging Face ](https://huggingface.co/Kseniase)🤗

Twitter Library

[9 New Approaches to Multi-Agent Systems](https://www.turingpost.com/p/9masmethods)

We are reading/watching/learning:

[AI’s moats, myths and moral loopholes](https://www.exponentialview.co/p/ev-572) by Azeem Azhar

[The Distillation panic ](https://www.interconnects.ai/p/the-distillation-panic)by Nathan Lambert

On SFT, RL, and on-policy distillation by Will Brown

News from the usual suspects ™

Anthropic is building an enterprise deployment arm with Wall Street
Anthropic [announced ](https://www.anthropic.com/news/enterprise-ai-services-company?ref=diffuse.design)a new enterprise AI services company with Blackstone, Hellman & Friedman, and Goldman Sachs; WSJ reports the venture is expected to total about $1.5B. This is Claude moving into the implementation layer, where the real enterprise money and pain live.

OpenAI is widening distribution beyond Microsoft with AWS
OpenAI [says](https://openai.com/index/openai-on-aws/) its models, Codex, and Managed Agents are coming to AWS so enterprises can use them inside existing AWS security and compliance environments. OpenAI’s enterprise strategy is no longer only “come to ChatGPT”; it is “we will show up where your stack already is.”

Google DeepMind is pushing medical AI into “co-clinician” research
DeepMind [shared](https://deepmind.google/blog/ai-co-clinician/) an AI co-clinician research initiative that tests evidence-grounded clinical reasoning and real-time multimodal telemedicine simulations. The careful wording matters: supportive tool under physician authority, not replacement doctor. Sensible, because “move fast and break patients” is a bad slogan.

Microsoft is turning agent governance into a product category
Agent 365 is now generally available, with Microsoft [framing](https://www.microsoft.com/en-us/security/blog/2026/05/01/microsoft-agent-365-now-generally-available-expands-capabilities-and-integrations/) it as a control plane to observe, govern, and secure AI agents across delegated agents, autonomous agents, local agents, SaaS agents, and “shadow AI.” It explicitly mentions discovery for tools like OpenClaw, Claude Code, and GitHub Copilot CLI. This is very relevant for the organizational AI story: once agents spread, visibility becomes infrastructure.

The Pentagon AI story escalates
Reuters [reported](https://www.reuters.com/technology/google-signs-classified-ai-deal-with-pentagon-information-reports-2026-04-28/) on Apr 28 that Google signed a classified AI agreement with the Pentagon for “any lawful government purpose,” including sensitive classified work, while retaining stated limits around domestic mass surveillance and autonomous weapons without human oversight. Then The Verge reported on May 1 that the Pentagon had [struck](https://www.theverge.com/ai-artificial-intelligence/922113/pentagon-ai-classified-openai-google-nvidia) classified AI deals with OpenAI, Google, Microsoft, Amazon, Nvidia, xAI, and Reflection, while excluding Anthropic after the dispute over its red lines. This is the governance story hiding inside the model race

Musk [said](https://www.wired.com/story/elon-musk-distill-openai-models-partly-xai/) xAI “partly” used OpenAI models to train Grok, in court testimony about model distillation (everyone does it!)

Models

GLM-5V-Turbo – Pushes multimodal perception into the core agent loop: reasoning, planning, tool use, execution, coding, GUI work, webpages, documents, images, and video. This is worth highlighting because it treats vision as part of agency rather than as a side input to a language model [→read the paper](https://arxiv.org/abs/2604.26752?utm_source=chatgpt.com)

NVIDIA Nemotron 3 Nano Omni – Unifies vision, audio, video, documents, charts, graphical interfaces, and text input into one open omni-modal reasoning model for agentic workflows. The strong angle is efficiency: NVIDIA frames it as a perception sub-agent for computer use, document intelligence, and audio-video reasoning, with up to 9x higher throughput than other open omni models [→read the release](https://blogs.nvidia.com/blog/nemotron-3-nano-omni-multimodal-ai-agents/?utm_source=chatgpt.com)

Mistral Medium 3.5 – Consolidates instruction-following, reasoning, and coding into one opened-weight 128B dense model with a 256K context window. This is interesting as a product-direction signal: fewer specialized public models, more unified generalist weights for agents and coding workflows [→see the model](https://huggingface.co/mistralai/Mistral-Medium-3.5-128B?utm_source=chatgpt.com)

Research 

Trends we see looking at every paper related to AI and ML published last week: 

Self-improvement is becoming the dominant design pattern.

Heterogeneous systems are also everywhere.

Efficiency is now part of intelligence research.

The bigger picture: AI research is moving toward systems that improve themselves, coordinate across heterogeneous components, and leave behind machine-readable traces of what they did and why it worked.

---

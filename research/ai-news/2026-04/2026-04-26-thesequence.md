# 🔢 TheSequence — 2026-04-26

> 165k+ 訂閱；ML / 企業 AI 應用週報，Jesus Rodriguez 主筆
> 來源：[TheSequence](https://thesequence.substack.com/feed)

---

## [The Sequence Radar #849: Last Week in AI: OpenAI Ships Agents, xAI Eyes Cursor, DeepSeek and Kimi Advance](https://thesequence.substack.com/p/the-sequence-radar-849-last-week)
*🔢 TheSequence | 2026-04-26*

Next Week in The Sequence:

Our series about transformer alternatives starts by exploring the comeback of RNNs.

We dive into DeepSeek v4 and GPT 5.5. 

The opinion section we dive into an interesting thesis: a CLI for evertyhing 

Subscribe and don’t miss out:

📝 Editorial: OpenAI Ships Agents, xAI Eyes Cursor, DeepSeek and Kimi Advance

This week in AI felt less like another cycle of model launches and more like a shift in the substrate of software itself. The important story is not simply that new models are becoming more capable. That has been the default trajectory for several years. The more interesting development is that models are becoming increasingly entangled with the systems where work actually happens: code editors, enterprise workflows, cloud environments, collaboration tools, and agentic interfaces.

OpenAI’s GPT-5.5 release is the obvious center of gravity. It represents the continued expansion of frontier-model capability across reasoning, coding, tool use, long-context work, and professional tasks. But the benchmark narrative is almost becoming secondary. A frontier model is no longer just a model. It is a runtime. It is the intelligence layer inside coding environments, research workflows, enterprise assistants, and autonomous systems. The model is becoming less like a smarter chatbot and more like a computational engine that can coordinate action.

OpenAI’s other releases made that thesis even clearer. Workspace Agents push ChatGPT from an individual productivity tool into a shared organizational substrate: Codex-powered agents that can live inside a company, run in the cloud, operate across tools like ChatGPT and Slack, follow permissions, remember context, and execute long-running workflows. This is not just “custom GPTs with enterprise packaging.” It is the beginning of AI as reusable institutional process. At the same time, ChatGPT Images 2.0 expands the surface area of AI work from language and code into visual production, with stronger text rendering, multilingual support, visual reasoning, and “images with thinking,” where the model can spend more time planning and refining before generating. Put together, these releases show OpenAI trying to make ChatGPT less like an app and more like a multimodal work environment: one place where text, code, images, tools, memory, approvals, and agents begin to converge.

The xAI deal with Cursor fits perfectly into this larger pattern. Cursor has become one of the clearest examples of AI-native software development moving from novelty to infrastructure. Code is the ideal environment for agents because it is explicit, testable, composable, and economically valuable. A coding agent can propose, edit, run, debug, and verify. It operates in a loop where progress can be measured. Whoever owns that loop owns one of the most important surfaces in the future of AI.

Meanwhile, DeepSeek V4 and Kimi 2.6 show how quickly the open and semi-open model ecosystem is compressing the frontier from below. The new competition is not merely about chat quality or leaderboard theater. It is about long context, coding performance, tool use, latency, cost, and agentic reliability. In other words, the battleground is shifting from intelligence as conversation to intelligence as execution.

This is the real theme of the week: AI is becoming operational. The model is no longer the product by itself. The product is the model plus the harness, the tools, the memory, the permissions, the environment, and the feedback loop. We are moving from models that answer questions to systems that perform work.

🔎 AI Research

[Decoupled DiLoCo for Resilient Distributed Pre-training](https://deepmind.google/blog/decoupled-diloco/)

AI Lab: Google DeepMind, Google Research

Summary: This paper introduces Decoupled DiLoCo, an evolution of the DiLoCo framework designed to improve the resilience of large language model pre-training against hardware failures and network issues. By separating compute across independent, asynchronously communicating "learners," the framework achieves significant improvements in training efficiency (goodput) while maintaining competitive model performance, even in highly fault-prone environments simulated through chaos engineering.

[LLaDA2.0-Uni: Unifying Multimodal Understanding and Generation with Diffusion Large Language Model](https://arxiv.org/abs/2604.20796)

AI Lab: Inclusion AI, Ant Group 

Summary: This paper introduces LLaDA2.0-Uni, a unified discrete diffusion large language model that seamlessly integrates multimodal understanding and generation within a single framework. By discretizing visual inputs into semantic tokens and employing block-level masked diffusion, the model matches specialized vision-language models while supporting interleaved generation and reasoning.

[SkillLearn Bench: Benchmarking Continual Learning Methods for Agent Skill Generation on Real-World Tasks ](https://arxiv.org/html/2604.20087v1)

AI Lab: Carnegie Mellon University, Amazon AGI 

Summary: The authors present SkillLearnBench, the first benchmark designed to evaluate continual learning methods for agent skill generation across 20 real-world tasks. Their evaluation reveals that while continual learning methods improve performance over no-skill baselines, they still fall short of human-authored skill levels and struggle with open-ended tasks.

[Scaling Test-Time Compute for Agentic Coding](https://arxiv.org/abs/2604.16529) 

AI Lab: Meta Superintelligence Labs, University of Washington, New York University, Google DeepMind, Carnegie Mellon University, Princeton University 

Summary: This paper proposes a test-time scaling framework for long-horizon coding agents by converting noisy rollout trajectories into compact, structured summaries. Utilizing Recursive Tournament Voting (RTV) for parallel scaling and Parallel-Distill-Refine (PDR) for sequential scaling, this representation-centric approach significantly boosts the performance of frontier models on challenging agentic benchmarks.

[SWE-chat: Coding Agent Interactions From Real Users in the Wild ](https://arxiv.org/html/2604.20779v1)

AI Lab: Stanford University 

SWE-chat introduces the first large-scale dataset of real-world coding agent sessions, capturing over 6,000 interactions, 63,000 user prompts, and 355,000 tool calls from open-source developers. Analyzing this data reveals that while “vibe coding” is increasingly popular, it remains costly and introduces more security vulnerabilities, frequently prompting users to interrupt or correct the agent.

[AutoAdapt: An Automated Domain Adaptation Framework for Large Language Models ](https://www.microsoft.com/en-us/research/blog/autoadapt-automated-domain-adaptation-for-large-language-models/)

AI Lab: Microsoft 

Summary: AutoAdapt is an end-to-end automated framework designed to optimize the complex domain adaptation process for large language models under tight resource constraints. By employing a multi-agent debating system to navigate best practices and an LLM-based surrogate for efficient hyperparameter tuning, the framework achieves a 25% relative accuracy improvement over state-of-the-art automated baselines.

🤖 AI Tech Releases

DeepSeek v4

The [new version of DeepSeek is here ](https://x.com/deepseek_ai/status/2047516922263285776)with 1M context length and impressive agentic capabilities. 

Kimi 2.6

[Kimi 2.6 launched ](https://www.kimi.com/blog/kimi-k2-6)with marquee capabilities in agentic coding. 

ChatGPT Images 2.0

OpenAI [released incredibly enhanced image generation capabilities in ChatGPT](https://openai.com/index/introducing-chatgpt-images-2-0/). 

Workspace Agents

OpenAI [unveiled Workspace Agents](https://openai.com/index/introducing-workspace-agents-in-chatgpt/), a new experience for creating agents that can handle complex workflows inside ChatGPT.

ML Intern

Hugging Face [open sourced ML Intern](https://github.com/huggingface/ml-intern), an agent that researchs and write ML related code. 

📡10 AI News You Need to Know About

SpaceX preempted Cursor’s nearly-closed $2B funding round at a $50B valuation [by offering a $60B post-IPO acquisition option](https://www.bloomberg.com/news/articles/2026-04-22/musk-makes-60-billion-gamble-after-xai-slips-behind-in-coding) — paying $10B as a “collaboration” fee in the interim — as the post-xAI-merger SpaceX scrambles to position itself as an AI company.

[Infosys and OpenAI announced a strategic collaboration](https://www.infosys.com/newsroom/press-releases/2026/collaboration-accelerate-enterprise-ai-transformation.html) combining Infosys Topaz Fabric with OpenAI’s Codex and frontier models to drive enterprise software engineering, legacy modernization, and DevOps automation at scale.

NeoCognition, an AI agent lab founded by Ohio State professor Yu Su with co-founders Xiang Deng and Yu Gu, [emerged from stealth with a $40M seed ](https://www.prnewswire.com/news-releases/neocognition-emerges-from-stealth-with-40-million-seed-round-to-advance-specialized-intelligence-and-expert-agents-302749108.html)co-led by Cambium Capital and Walden Catalyst Ventures to build self-learning agents that develop world models of specific work environments.

[Anthropic took an additional $5B from Amazon ](https://www.anthropic.com/news/anthropic-amazon-compute)(bringing total Amazon investment to $13B) in exchange for a $100B+ ten-year AWS commitment covering up to 5GW of Trainium2-through-Trainium4 capacity to train and serve Claude.

[ Microsoft committed A$25B (~US$18B) to Australia by end-2029,](https://news.microsoft.com/source/asia/features/investing-in-australias-ai-future/) expanding Azure AI supercomputing capacity by over 140%, deepening cyber defense work with the ASD, and pledging workforce-ready AI training for three million Australians by 2028.

Jeff Bezos and Vik Bajaj’s physical-AI lab Project Prometheus [closed a $10B round at a ~$38B valuation ](https://www.bloomberg.com/news/articles/2026-04-23/bezos-s-physical-ai-lab-has-closed-round-at-38-billion-value)with JPMorgan and BlackRock among participants, while separately exploring up to $100B for a holding company to acquire industrial businesses whose operational data would feed back into the lab’s models.

Bret Taylor and Clay Bavor’s Sierra [acquired Paris-based, YC-backed Fragment ](https://sierra.ai/blog/sierra-acquires-fragment-in-france)— its third acquisition of 2026 after Opera Tech and Receptive AI — bringing co-founders Olivier Moindrot and Guillaume Genthial onto the team to anchor Sierra’s agent development efforts in France.

[ComfyUI raised $30M at a $500M valuation ](https://blog.comfy.org/p/comfyui-raises-30m-to-scale-open)in a round led by Craft (with Pace Capital, Chemistry, and TruArrow), capitalizing on an open-source community of 4M users and 60,000+ nodes that has made its node-based workflow the de facto control layer for production-grade generative media.

[Google committed up to $40B in Anthropic ](https://www.bloomberg.com/news/articles/2026-04-24/google-plans-to-invest-up-to-40-billion-in-anthropic)— $10B now at a $350B valuation, with $30B more contingent on performance milestones — alongside an expanded Google Cloud arrangement providing 5GW of TPU-based compute over the next five years.

[Meta signed a multi-year, multi-billion-dollar deal](https://about.fb.com/news/2026/04/meta-partners-with-aws-on-graviton-chips-to-power-agentic-ai/) to bring tens of millions of AWS Graviton5 cores into its compute portfolio for agentic-AI inference workloads, becoming one of AWS’s largest Graviton customers and validating the thesis that agentic AI is shifting demand back toward CPUs.

---

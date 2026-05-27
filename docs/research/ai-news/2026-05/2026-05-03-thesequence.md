---
title: "TheSequence — 2026-05-03"
date: 2026-05-03
source: TheSequence
type: ai-news
---

# 🔢 TheSequence — 2026-05-03

> 165k+ 訂閱；ML / 企業 AI 應用週報，Jesus Rodriguez 主筆
> 來源：[TheSequence](https://thesequence.substack.com/feed)

---

## [The Sequence Radar #853: Last Week in AI: The Great AI Fundraising Wars and a New Frontier Lab](https://thesequence.substack.com/p/the-sequence-radar-853-last-week)
*🔢 TheSequence | 2026-05-03*

Next Week in The Sequence:

We continue our series about alternatives to the transformer architecture. 

In our opinion section, we are going to dive into the thesis of building software for AI agents instead of human consumers. 

The AI of the weeks dive into NVIDIA’s new Nemotron model. 

Subscribe and don’t miss out:

📝 Editorial: Last Week in AI: The Great AI Fundraising Wars and a New Frontier Lab

This week in AI felt less like a product cycle and more like a sovereign debt auction for the future of cognition. The models are still improving, the demos are still fun, and yes, the agents are still occasionally lost in the hallway holding a JSON object. But the real story is that frontier AI is becoming an industrial-scale capital formation game.

The center of gravity was Anthropic. Reports this week said the Claude maker is weighing a new round that could value the company above $900 billion, potentially surpassing OpenAI’s most recent reported valuation and becoming the world’s most valuable AI startup. Reuters reported that Anthropic is considering offers at more than double its prior valuation, with TechCrunch adding that the round could be in the $40 billion to $50 billion range. 

This is not just investor exuberance. It is the market trying to price a new kind of company: part model lab, part cloud tenant, part developer platform, part enterprise operating system. Anthropic’s recent strategic deals tell the story. Google committed up to $40 billion to Anthropic, while Amazon recently announced up to $25 billion in additional investment tied to a much larger cloud partnership. Anthropic has also been securing compute through Broadcom, CoreWeave, Amazon chips, and its own data-center ambitions. 

The competition with OpenAI is now less about whose chatbot writes the better poem and more about who can assemble the stronger industrial stack. OpenAI, for its part, just renegotiated its Microsoft relationship to gain more flexibility to court Amazon and other cloud providers, while Microsoft keeps long-term economics through 2030. Reuters framed the change explicitly as helping OpenAI secure more compute and compete better with Anthropic in enterprise markets. 

So the frontier race is mutating. The old question was: who has the best model? The new question is: who has the best capital structure, compute supply chain, cloud distribution, developer wedge, enterprise trust layer, and agent ecosystem? Intelligence is becoming infrastructure, and infrastructure has a balance sheet.

The same pattern is now showing up in vertical AI. Legal AI startup Legora extended its Series D by $50 million, bringing the total round to $600 million and reaching a $5.6 billion valuation, with Atlassian and Nvidia’s NVentures joining as investors. Legora has reportedly surpassed $100 million ARR, scaled to more than 1,000 organizations across 50 markets, and is positioning itself as an agentic operating system for legal work. 

That makes the Harvey versus Legora battle one of the most interesting application-layer fights in AI. Harvey has the U.S. legal-tech aura, the elite law-firm mindshare, and an $11 billion valuation. Legora has the European-born insurgent energy, rapid ARR growth, and now corporate investors that understand workflow and compute. The punchline is not that lawyers will use chatbots. That is too small. The real punchline is that legal work is being decomposed into agentic workflows: research, drafting, diligence, review, negotiation, precedent search, risk analysis, and eventually entire deal rooms with AI copilots quietly moving the machinery.

Another signal came from London, where Ineffable Intelligence launched with a spectacular $1.1 billion seed round at a reported $5.1 billion valuation—Europe’s largest seed financing to date. Founded by former DeepMind researcher David Silver, one of the central figures behind AlphaGo, Ineffable is not pitching another chatbot, but a return to a more radical AI thesis: reinforcement-learning systems that learn through experience rather than merely compressing human-generated data. In a week dominated by Anthropic and OpenAI’s capital wars, Ineffable felt like the research-world version of the same phenomenon: frontier AI companies are now being funded not as startups, but as civilizational-scale experiments. The market is placing billion-dollar bets not only on who wins the current LLM race, but on what might come after it.

This week’s lesson is simple: AI is leaving the toy-box phase. Frontier labs are becoming trillion-dollar infrastructure companies. Vertical AI startups are becoming operating systems for professional work. The intelligence explosion may still be debated philosophically, but the capitalization explosion is already here.

🔎 AI Research

[The Last Human-Written Paper: Agent-Native Research Artifacts ](https://arxiv.org/abs/2604.24658)

AI Lab: Orchestra Research, Stanford University, and others 

Summary: This paper introduces the Agent-Native Research Artifact (ARA), a protocol that replaces traditional linear narrative papers with an executable, four-layer knowledge package optimized for AI agents. By preserving scientific logic, executable code, the branching exploration history, and grounded evidence, the ARA framework significantly improves an agent’s ability to extract knowledge, reproduce experiments, and extend prior research.

[GLM-5V-Turbo: Toward a Native Foundation Model for Multimodal Agents ](https://arxiv.org/abs/2604.26752)

AI Lab: Z.ai & Tsinghua University 

Summary: This technical report presents GLM-5V-Turbo, a multimodal foundation model designed to deeply integrate vision and language across perception, reasoning, planning, and execution. Through a novel CogViT vision encoder, Multimodal Multi-Token Prediction, and joint reinforcement learning over diverse tasks, the model achieves strong performance in multimodal coding and GUI agent tasks without sacrificing text-only capabilities.

[Length Value Model: Scalable Value Pretraining for Token-Level Length Modeling ](https://arxiv.org/abs/2604.27039)

AI Lab: University of California, Santa Barbara, Apple Inc., and others

Summary: This paper proposes the Length Value Model (LenVM), which frames autoregressive generation length modeling as a token-level value estimation problem by predicting a discounted return for remaining generation steps. This annotation-free and scalable approach enables continuous control over the performance-efficiency trade-off during inference, allowing for highly accurate length constraint matching and generation horizon prediction.

[Synthetic Computers at Scale for Long-Horizon Productivity Simulation ](https://arxiv.org/abs/2604.28181)

AI Lab: Microsoft 

Summary: This paper introduces a scalable methodology to create realistic, user-specific synthetic computer environments populated with diverse directory structures and content-rich artifacts. By running long-horizon productivity simulations within these environments, the system generates rich experiential signals that significantly improve agent performance on both in-domain and out-of-domain productivity evaluations.

[CO-DIRECTOR: Agentic Generative Video Storytelling ](https://arxiv.org/abs/2604.24842)

AI Lab: Google 

Summary: This paper introduces CO-DIRECTOR, a hierarchical multi-agent framework that formalizes video storytelling as a global optimization problem to overcome semantic drift and cascading failures in current agentic pipelines. By combining multi-armed bandit optimization with a local multimodal self-refinement loop, the system dynamically explores creative trajectories and ensures consistent narrative and visual styles across sub-agents.

[Recursive Multi-Agent Systems ](https://arxiv.org/abs/2604.25917)

AI Lab: UIUC, Stanford University, NVIDIA, MIT 

Summary: This paper presents RecursiveMAS, a framework that scales multi-agent collaboration by casting the entire system as a unified latent-space recursive computation using a lightweight RecursiveLink module. Through an inner-outer loop learning algorithm, the system enables efficient cross-agent interaction and shared gradient-based credit assignment without text-based latency, leading to significant improvements in accuracy, inference speed, and token reduction across diverse benchmarks.

🤖 AI Tech Releases

Nemotron 3 Nano Omni Model

NVIDIA [released Nemotron 3 Nano Omni Model](https://blogs.nvidia.com/blog/nemotron-3-nano-omni-multimodal-ai-agents/), a multimodal, long-context model optimized for agentic tasks. 

Claude Security

Anthropic [announced Claude Security’s Beta](https://claude.com/product/claude-security), an addition to its enterprise solution focused on security vulnerability scanning. 

Claude for Creative Work

Anthropic [released Claude for Creative Work](https://www.anthropic.com/news/claude-for-creative-work), a series of tools and connectors for creative and design platforms. 

📡10 AI News You Need to Know About

[Anthropic potential $900B+ valuation round](https://techcrunch.com/2026/04/30/anthropic-potential-900b-valuation-round-could-happen-within-two-weeks/) — Anthropic is asking investors to submit allocations within 48 hours for an estimated ~$50B round at a targeted ~$900B valuation, expected to close within two weeks and likely to be its last private round before a planned IPO. 

[Legora hits $5.6B valuation](https://legora.com/newsroom/legora-extends-series-d-with-additional-50-million-welcomes-atlassian-and-nventures-as-investors) — Swedish legal AI startup Legora extended its Series D by $50M, adding Nvidia’s NVentures and Atlassian as investors at a $5.6B post-money valuation after crossing $100M ARR, narrowing the gap with US rival Harvey. → [Legora newsroom announcement](https://legora.com/newsroom/legora-extends-series-d-with-additional-50-million-welcomes-atlassian-and-nventures-as-investors)

[Flourish targets $2.5B valuation](https://www.bloomberg.com/news/articles/2026-04-30/startup-bringing-brains-to-ai-aims-for-2-5-billion-valuation?srnd=phx-ai)[ ](https://www.bloomberg.com/news/articles/2026-04-30/startup-bringing-brains-to-ai-aims-for-2-5-billion-valuation?srnd=phx-ai)— Thomas Reardon, who led work on Meta’s Neural Band, is raising for a new energy-efficient AI startup called Flourish at a $2.5B valuation. 

[Parallel Web Systems hits $2B valuation](https://parallel.ai/blog/series-b)[ ](https://parallel.ai/blog/series-b)— Parag Agrawal’s AI agent web-search/research API startup raised a $100M Series B led by Sequoia at a $2B valuation, just five months after its $740M Series A. 

[David Silver’s Ineffable Intelligence raises $1.1B](https://www.wired.com/story/david-silver-ai-ineffable-intelligence-reinforcement-learning/)[ ](https://www.wired.com/story/david-silver-ai-ineffable-intelligence-reinforcement-learning/)— Former DeepMind reinforcement learning lead David Silver’s new UK-based AI lab raised $1.1B at a $5.1B valuation from Sequoia, Lightspeed, Nvidia, Google and others to build a “superlearner” that learns without human data. 

[China vetoes Meta’s $2B Manus deal](https://www.reuters.com/world/asia-pacific/china-blocks-foreign-acquisition-ai-startup-manus-2026-04-27/) — China’s National Development and Reform Commission ordered Meta and AI agent startup Manus to unwind their ~$2B acquisition, citing prohibition of foreign investment in the Manus project. 

[Amazon offers new OpenAI products on AWS](https://www.aboutamazon.com/news/aws/bedrock-openai-models)[ ](https://www.aboutamazon.com/news/aws/bedrock-openai-models)— Days after OpenAI ended Microsoft’s exclusivity, AWS announced that Bedrock now hosts OpenAI’s latest models, Codex, and a new “Bedrock Managed Agents” service built on OpenAI’s reasoning models.

---

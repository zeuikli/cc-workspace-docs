# 🔢 TheSequence — 2026-04-05

> 165k+ 訂閱；ML / 企業 AI 應用週報，Jesus Rodriguez 主筆
> 來源：[TheSequence](https://thesequence.substack.com/feed)

---

## [The Sequence Radar #837: Last Week in AI: From Model Releases to Market Structure](https://thesequence.substack.com/p/the-sequence-radar-837-last-week)
*🔢 TheSequence | 2026-04-05*

Next Week in The Sequence:

We continue our series about world models

The AI of the week section will dive into the amazing Gemma4. 

The opinion section will discuss why every piece of software infrastructure needs to be rewritten for AI agents. 

Subscribe and don’t miss out:

📝 Editorial: Last Week in AI: From Model Releases to Market Structure

This week in AI was not really a product week. It was a market-structure week. OpenAI’s massive new funding round, Microsoft’s release of new models, Google’s expansion of Gemma 4, and the arrival of GLM-5V Turbo all pointed to the same conclusion: the center of gravity in AI is shifting. The industry is no longer organized around who has the most impressive demo. It is being reorganized around who can finance, deploy, compress, distribute, and operationalize intelligence at scale. AI is starting to look less like software and more like infrastructure.

OpenAI’s round was the loudest signal. At some level, every frontier AI company is now running two races at once: a research race and a capital race. The models matter, of course, but so does the ability to fund the machine behind the models: training clusters, inference capacity, developer ecosystems, enterprise sales, consumer distribution, and increasingly the tooling layer around coding and automation. That is what makes this moment important. Frontier AI is becoming less like launching an app and more like building a power grid. The technology may feel abstract, but the economics are becoming brutally concrete. Intelligence is expensive to manufacture, even more expensive to serve, and the companies that can keep feeding that loop are building an advantage that is not easy to copy.

Microsoft’s releases made a different point, but one that is just as important. With MAI-Transcribe-1, MAI-Voice-1, and MAI-Image-2, Microsoft is signaling that it does not want to be merely the best host for other people’s intelligence. It wants to own more of the intelligence layer itself. That is a meaningful shift. In the first phase of the generative AI boom, large platforms won by embedding frontier models into existing products. In the next phase, they may win by controlling the core modalities that define how software feels and behaves. Speech, voice, and image generation are no longer side features. They are becoming native interfaces. The future office suite may not be built around files and menus, but around systems that can hear, speak, see, and create in real time.

Google’s Gemma 4 pushes from the opposite direction and, in some ways, makes the market more interesting. If OpenAI represents scale and Microsoft represents vertical integration, Gemma 4 represents the growing strategic importance of openness. Open models are no longer just the rebel wing of AI. They are becoming essential pieces of the deployment stack, especially for developers and companies that want control, portability, and lower-cost inference. That matters because the next AI wave will not be won on raw benchmark prestige alone. It will be won on usability. Small, efficient, customizable models that can run closer to the edge may shape more real products than the most powerful model in the world sitting behind a distant API.

Then there is GLM-5V Turbo, which quietly points to where the agent era is going. Its importance is not just that it is multimodal. It is the type of multimodality that matters: interfaces, files, screens, visual reasoning, coding workflows. That is a different category of capability. It suggests a future in which models do not just generate text, but operate across software environments with something closer to functional competence. They do not merely describe what is on the screen. They begin to work through it.

That is why this week felt bigger than the individual announcements. The AI market is maturing from spectacle to systems. OpenAI is consolidating the economics of scale. Microsoft is building first-party control across modalities. Google is making the open layer harder to ignore. GLM-5V Turbo is pushing models closer to action. For the last two years, AI has often been discussed as if it were a product category. This week was a reminder that it is becoming something much larger: a new computing substrate. And once a technology becomes substrate, the real competition is no longer about who is smartest. It is about who becomes unavoidable.

🔎 AI Research

[TRIBE: TRImodal Brain Encoder for whole-brain fMRI response prediction](https://arxiv.org/html/2507.22229v1)

AI Lab: FAIR at Meta

Summary: TRIBE v2 is a tri-modal foundation model trained on over 1,000 hours of fMRI data to accurately predict human brain activity in response to video, audio, and language stimuli. It drastically outperforms traditional linear encoding models and enables in-silico neuroscience experiments by successfully replicating classic visual and neuro-linguistic findings while revealing the fine-grained topography of multisensory integration.

[Terminal Agents Suffice for Enterprise Automation](https://arxiv.org/html/2604.00073v1)

AI Lab: ServiceNow, Mila Quebec AI Institute, Université de Montréal

Summary: This paper challenges the necessity of complex web and tool-augmented agents for enterprise tasks by demonstrating that minimal coding agents equipped only with a terminal and direct API access perform just as well or better. By evaluating across diverse production-grade platforms, the authors show that these simpler terminal agents are significantly more cost-efficient and resilient without sacrificing effectiveness.

[QUITOBENCH: A High-Quality Open Time Series Forecasting Benchmark](https://arxiv.org/html/2603.26017v1)

AI Lab: Ant Group

Summary: To address the scarcity of reliable time series forecasting evaluations, this paper introduces QUITOBENCH, a regime-balanced benchmark derived from a billion-scale corpus of Alipay application traffic. The evaluation reveals that context length and forecastability are primary drivers of performance, demonstrating that smaller, task-specific deep learning models can actually match or outperform much larger foundation models.

[Embarrassingly Simple Self-Distillation Improves Code Generation](https://arxiv.org/html/2604.01193v1)

AI Lab: Apple

Summary: This research demonstrates that large language models can substantially improve their code generation capabilities by fine-tuning exclusively on their own raw, unverified outputs. This simple self-distillation approach works by resolving the precision-exploration conflict, allowing the model to suppress distractor tokens at rigid syntactic checkpoints while preserving diverse alternatives at creative branching points.

[General scales unlock AI evaluation with explanatory and predictive power](https://arxiv.org/html/2503.06378v2)

AI Lab: Princeton University, University of Cambridge, Microsoft Research Asia

Summary: The authors introduce a new methodology using 18 standardized rubrics to systematically profile both the cognitive demands of tasks and the intrinsic capabilities of AI models. This approach yields high predictive power for AI performance on unseen, out-of-distribution tasks by evaluating fundamental abilities rather than relying on easily saturated and heavily confounded benchmark aggregates.

[Forest vs Tree: The (N, K) Trade-off in Reproducible ML Evaluation](https://ojs.aaai.org/index.php/AAAI/article/view/39659)

AI Lab: Rochester Institute of Technology, Google Research

Summary: This study investigates the trade-off between the number of evaluation items and the number of human annotations per item when operating under a fixed budget for machine learning model assessment. The findings indicate that strategically collecting a higher number of annotations per item—rather than just scaling the total number of items—provides more statistically reliable evaluations, especially for metrics sensitive to human disagreement.

🤖 AI Tech Releases

Microsoft New AI Models

Microsoft [announced 3 state-of-the-art models](https://microsoft.ai/news/today-were-announcing-3-new-world-class-mai-models-available-in-foundry/), MAI-Transcribe-1, MAI-Voice-1 and MAI-Image-2 that enable transcruption, audio processing and image generation capabilities. 

Gemma 4

Google DeepMind [released Gemma 4](https://blog.google/innovation-and-ai/technology/developers-tools/gemma-4/), its highly efficient small model optimized for reasoning. 

GLM-5V Turbo

Z.ai [open sourced GML-5V Turbo ](https://x.com/Zai_org/status/2039371126984360085)with new multimodal coding capabilities and optimization for Claw scenarios. 

Trinity Large Thinking 

Arcee AI [open sourced Trinity Large Thinking](https://www.arcee.ai/blog/trinity-large-thinking), its largest open source frontier agent.

📡AI News You Need to Know About

[OpenAI closed a $122 billion funding ](https://openai.com/index/accelerating-the-next-phase-ai/)round at an $852 billion valuation, backed by Amazon, NVIDIA, SoftBank, and Microsoft, to scale compute infrastructure, expand its API and Codex platforms, and build toward a unified AI “superapp.”

[India’s Sarvam AI is nearing a $300–350M raise at a ~$1.5B valuation ](https://www.bloomberg.com/news/articles/2026-04-02/india-ai-startup-sarvam-raises-funds-at-1-5-billion-valuation)led by Bessemer Venture Partners, with NVIDIA, Amazon, and Prosperity7 also participating, positioning it as a domestic AI challenger with voice-first, multilingual models covering 22 Indian languages.

[OpenAI acquired TBPN](https://openai.com/index/openai-acquires-tbpn/), a popular daily tech/business talk show hosted by founders John Coogan and Jordi Hays, marking the AI company’s first media acquisition ahead of its planned IPO; the show will report to OpenAI’s strategy team under Chris Lehane.

[Yupp, the crowdsourced AI model evaluation startup that raised $33M from a16z crypto’s Chris Dixon, is shutting down](https://blog.yupp.ai/winddown) less than a year after launch, citing insufficient product-market fit as the industry shifted toward agentic systems and expert-led feedback.

[ScaleOps raised $130M in Series C ](https://scaleops.com/blog/scaleops-series-c/)funding at a valuation above $800M, led by Insight Partners, for its platform that autonomously manages and reallocates Kubernetes-based cloud and AI compute resources in real time, claiming up to 80% cost reduction.

[South Korean fabless AI chip startup Rebellions raised $400M ](https://rebellions.ai/newsroom/rebellions-closes-400-million-pre-ipo-and-launches-rebelrack-and-rebelpod-to-accelerate-global-expansion/)in a pre-IPO round led by Mirae Asset and the Korea National Growth Fund, reaching a $2.34B valuation and $850M in total funding, while launching new inference infrastructure products and expanding into the U.S., Japan, and Saudi Arabia.

[French AI lab Mistral raised $830M in debt financing ](https://www.reuters.com/business/finance/frances-mistral-raises-830-million-debt-ai-data-centre-build-up-2026-03-30/)to build a new Nvidia-powered data center near Paris, expected to become operational in Q2 2026.

[Qodo raised $70M in Series B ](https://www.qodo.ai/blog/qodo-70m-series-b-shift-to-artificial-wisdom/)funding led by Qumra Capital, bringing total funding to $120M, to scale its AI-powered code review and governance platform that verifies AI-generated code against organizational standards, used by enterprises like NVIDIA, Walmart, and Red Hat.

[Y Combinator alum Starcloud raised $170M in a Series A ](http://businesswire.com/news/home/20260330024111/en/Starcloud-Raises-%24170M-Series-A-at-%241.1bn-Valuation-Led-by-Benchmark-and-EQT-Ventures)led by Benchmark and EQT Ventures at a $1.1B valuation, becoming one of the fastest YC startups to reach unicorn status, as it develops orbital data centers designed to launch aboard SpaceX’s Starship.

[Anthropic acquired Coefficient Bio](https://www.rdworldonline.com/anthropics-400m-acquisition-of-coefficient-bio-signals-a-deeper-push-into-drug-discovery/), a Dimension-backed stealth biotech AI startup founded roughly eight months ago with fewer than 10 employees, for approximately $400M in stock, bringing in a team of former Genentech researchers building biology-specific AI models to join Anthropic’s Health Care Life Sciences group as the company pushes to make Claude the leading model for drug discovery, R&D planning, and clinical regulatory strategy.

---

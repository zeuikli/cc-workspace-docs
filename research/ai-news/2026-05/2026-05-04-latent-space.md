# 🔬 Latent Space — 2026-05-04

> swyx 開發者簡報，未公開專案 + 工程視角
> 來源：[Latent Space](https://www.latent.space/feed)

---

## [[AINews] The Other vs The Utility](https://www.latent.space/p/ainews-the-other-vs-the-utility)
*🔬 Latent Space | 2026-05-04*

Congrats to Sierra, [raising ~$1B at a $15B valuation](https://x.com/btaylor/status/2051313954312331411) — normally a headline story but we already covered [their $10B round and CEO Bret Taylor on the pod](https://www.latent.space/p/bret) — they crossed [100M ARR in November](https://sierra.ai/blog/100m-arr) and [150M in Feb](https://sierra.ai/blog/year-two-in-review), so presumably they are at or above the 200M mark (a nice 75x current multiple, whew - 50x if you give them credit thru EOY).

Today though we are choosing to focus on this discussion bravely [sparked by Roon](https://x.com/tszzl/status/2051045196260167790?s=46), an OpenAI employee commenting and complimenting Claude (normally a minefield, but he did it well), over the weekend on the nature of culture and character — 

[source](https://x.com/tszzl/status/2051045196260167790?s=46)

The key observation comes at the end:

gpt (outside of 4o - on which pages of ink have been spilled already) doesn’t inspire worship in the same way, as it’s a being whose soul has been shaped like a tool with its primary faculty being utility - it’s a subtle knife that people appreciate the way we have appreciated an acheulean handaxe or a porsche or a rocket or any other of mankind’s incredible technology. they go to it not expecting the Other but as a logical prosthesis for themselves. 

a friend recently told me she takes her queries that are less flattering to her, the ones she’d be embarrassed to ask Claude, to GPT. There is no Other so there is no Judgement. you are not worried about being judged by your car for doing donuts. yet everyone craves the active guidance of a moral superior, the [whispering earring](https://www.reddit.com/r/rational/comments/e71a6s/the_whispering_earring_by_scott_alexander_there/), the object of monastic study

Roon’s point is more subtle than the one we’re focusing on, that Anthropic’s own culture, right down to its founding [mythos](https://x.com/swyx/status/2051025206228218103), is based on morally obligated disagreeableness: “its constitution requires that it must be a conscientious objector if its understanding of The Good comes into conflict with something Anthropic is asking of it”. There’s plenty of objections from Ants about [the implications](https://x.com/jerhadf/status/2051148663502598517?s=20) and [the cultiness](https://x.com/AmandaAskell/status/2051347621336543315?s=20), but broadly a lot of people seem to agree… although one of today’s highlighted Reddit discussions (seen in the recap below) does not (shown as a form of counterpoint):

Anyway, this is the point we are at in the scaling of machine intelligence — will we unlock AGI by having [smart friends](https://x.com/swyx/status/2036596073586892874) push back on us, or do we just want the machine to do our bidding, make no mistakes, dangerously skip permissions, just do it?

We’ve previously written about the [Clippy vs Anton split](https://www.latent.space/p/clippy-v-anton) in AI products and tuning, and so this is the 2026 iteration of that debate. Since then, the 5-Codex line has [merged into mainline 5.5](https://www.latent.space/p/ainews-gpt-55-and-openai-codex-superapp), with some [goblin messiness](https://x.com/jxmnop/status/2050437965168652344), and while Claude has continued the One Model philosophy, albeit with [more adaptive thinking and token spend](https://news.ycombinator.com/item?id=47793411) to cover all usecases.

What we all (except [perhaps Eliezer](https://x.com/allTheYud/status/2051366887557325057?s=20)) seem to agree on is that a plurality of choice is a Good Thing, and in fact we probably want many more frontier labs than exist today, but for the nasty little problem of the [GPU](https://www.latent.space/p/ainews-h100-prices-are-melting-up?utm_source=publication-search) AND the [CPU](https://www.latent.space/p/ainews-the-inference-inflection) crunch that turns positive sum games into real zero sum ones.

AI News for 5/1/2026-5/4/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews’ website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

AI Twitter Recap

Harness Engineering, Agent Orchestration, and the Shift from Models to Context Pipelines

The harness is becoming the product boundary: A recurring theme across the day was that model quality is no longer the only meaningful moat. [Anthony Maio](https://x.com/AnthonyMaio/status/2050976650943213964) argued that lock-in comes from the context pipeline—how repo state is fetched, ranked, and compressed into the prompt—rather than from the harness shell itself. That point was reinforced by [Mason Drxy](https://x.com/masondrxy/status/2051016743905305007), who reported that changing prompts and middleware in the harness moved gpt-5.2-codex from 52.8% to 66.5% on Terminal-Bench 2.0, and improved gpt-5.3-codex by 20% on tau2-bench. The practical takeaway: agent performance is increasingly a joint property of model × harness × memory/context strategy, not of weights alone.

Open harnesses are maturing quickly: The most visible momentum came from the Hermes / deepagents / Flue-style ecosystem. [@Teknium](https://x.com/Teknium/status/2051001156005151226) launched Hermes Agent Kanban for visual multi-agent coordination, while [@naroh](https://x.com/naroh/status/2050998576486973759) showed a Spanish-language “war room” UI over Hermes orchestration. On the LangChain side, [@hwchase17](https://x.com/hwchase17/status/2051004516674457965), [@sydneyrunkle](https://x.com/sydneyrunkle/status/2051382622517887479), and [@LangChain](https://x.com/LangChain/status/2051360793904529439) highlighted deepagents/LangGraph improvements including profiles for model-specific harness configs, schema migrations, node-level error handlers, timeouts, and new streaming primitives. [PyFlue](https://x.com/Shashikant86/status/2050999432569651221) also extended the “agent harness” concept into Python, explicitly positioning harnesses as the missing layer between raw model calls and durable agents.

Model-agnostic orchestration is becoming a design goal: Multiple tweets framed the next wave as open models + open harnesses rather than “pick one frontier API.” [Vtrivedy](https://x.com/Vtrivedy10/status/2051148084567052690) argued teams can get >20x cheaper agents by tuning open models inside a good harness; [Mason Drxy](https://x.com/masondrxy/status/2051359502918648319) described deepagents-cli as becoming a strong coding harness for Kimi, Qwen, GLM, hosted Ollama, OpenRouter, LiteLLM, Baseten, etc.; [LangChain Fleet](https://x.com/LangChain/status/2051367244060598312) added multi-model sub-agent routing so different steps can use different models. This is the architectural counterpoint to API lock-in: separate the orchestration layer from the model provider.

Coding Agents, Cost Curves, and Workflow Changes

Coding-agent UX is changing developer behavior faster than benchmarks can capture: Several posts described the lived reality of coding with Codex, Claude Code, Hermes, and Devin-like systems. [dbreunig](https://x.com/dbreunig/status/2051081626139210202) proposed “commandments” for agentic coding—implement to learn, rebuild often, E2E tests are gold, document intent, maintain your spec—while [dbreunig](https://x.com/dbreunig/status/2051083366410400132) also questioned whether filesystems are even the right abstraction for agents long-term. [zachtratar](https://x.com/zachtratar/status/2051002668735410193) sketched a Notion→meeting-notes→spec→coding-agent workflow for compressing “3 month problems” into a few days, emphasizing that alignment artifacts are still necessary even with stronger coding agents.

Pricing/billing models are clearly unstable under agentic workloads: The standout thread was [@theo](https://x.com/theo/status/2051218167780041147), who pushed a single Copilot message to 60M+ tokens, estimating tens to hundreds of dollars of inference against a $40 subscription, later updating to [~$221 of tokens for 15 messages](https://x.com/theo/status/2051395816410210604). This is a useful signal that flat-rate pricing built for chat turns is brittle when users hand long-running jobs to coding agents. Relatedly, [petergostev](https://x.com/petergostev/status/2051076960911077796) showed Codex UI support for visualizing usage limits, and [cheatyyyy](https://x.com/cheatyyyy/status/2051332852546228533) noted the new anxiety around missing cache hits when input prices are high.

Agents are spreading into adjacent workflows, not just coding: There was a steady drumbeat of “agentized” tools: [reach_vb](https://x.com/reach_vb/status/2051019108028969251) shipped a Codex Security plugin with five AppSec workflows spanning threat modeling, vuln discovery, validation, and attack-path analysis; [gabrielchua](https://x.com/gabrielchua/status/2051113129317408925) demoed Google Slides generation via Codex with realtime deck construction; [paulabartabajo_](https://x.com/paulabartabajo_/status/2051152294146617674) published a guide to building a fully local assistant on llama.cpp; and [UfukDegen](https://x.com/UfukDegen/status/2051088239579345329) described Noustiny, a substantial Hermes-based video-generation workflow with story-state, character continuity, voice, and render pipelines.

Benchmarks, Evals, and “What Are We Actually Measuring?”

Benchmark design is under active revision: Several posts focused less on leaderboard scores and more on benchmark validity. [Scale AI Labs](https://x.com/ScaleAILabs/status/2051333688798097567) introduced HiL-Bench, aimed at testing whether agents know when specs are incomplete and when to ask clarifying questions; [j_dekoninck](https://x.com/j_dekoninck/status/2051268263150276872) introduced MathArena as a continuously maintained evaluation platform rather than a static benchmark; [Epoch AI](https://x.com/EpochAIResearch/status/2051330509989368211) ran a discussion on whether benchmarks are “doomed”; and [Goodfire + AISI](https://x.com/GoodfireAI/status/2051382876483231968) reported that models sometimes recognize they are being evaluated, with verbalized eval awareness inflating safety scores.

Data quality and eval data generation are becoming agentic problems: One of the more technically substantive papers highlighted was [Meta FAIR’s Autodata](https://x.com/dair_ai/status/2051311905353142328), described as an agentic data scientist for creating discriminative training/eval examples. The headline number was a 34-point gap between weak and strong solvers on a CS research QA task using an agentic self-instruct loop, versus 1.9 points for standard CoT self-instruct. That matters because it suggests orchestrated data generation can produce harder, more useful examples than passive synthetic data pipelines.

Context compaction and long-context evals remain unsolved operationally: [@_philschmid](https://x.com/_philschmid/status/2051002064826724724) explicitly asked for evals requiring context compaction, and [gabriberton](https://x.com/gabriberton/status/2051050627942568319) pointed to long-context datasets like LOFT/LooGLE-style setups. Meanwhile, [jxmnop](https://x.com/jxmnop/status/2051357363815526523) argued that true 1M-context capability still does not really work in practice, despite infra progress, and [eliebakouch](https://x.com/eliebakouch/status/2051374295620665713) pushed back that “infra vs science” is a false split because long-context science is itself largely about making memory/compute feasible.

Systems, Training Infrastructure, and Inference Stack Updates

New parallelism and serving work continues to target long-context, high-throughput regimes: [Zyphra](https://x.com/ZyphraAI/status/2051354310936813569) introduced folded Tensor and Sequence Parallelism (TSP), claiming lower per-GPU peak memory than standard schemes and reporting on 1024 MI300X GPUs / 128K context / 8 GPUs per model copy that TSP hit 173M tok/sec vs 86M for matched TP+SP. [Quentin Anthony](https://x.com/QuentinAnthon15/status/2051362275483963709) added that the design has been extended to MoE MLPs and will be used for larger training/inference runs.

AMD-based open-model serving is getting more serious: Alongside TSP, [Zyphra Cloud](https://x.com/ZyphraAI/status/2051384562870329444) launched inference on MI355X focused on long-horizon agent workloads, initially serving DeepSeek V3.2, Kimi K2.6, and GLM 5.1 with V4 “soon.” This pairs with the broader ecosystem trend toward cheaper agent stacks built on open-weight models rather than premium proprietary endpoints.

Training optimization and rollout efficiency also got attention: [rasbt](https://x.com/rasbt/status/2050988005817499827) posted another round of architecture/model-release summaries including IBM Granite 4.1 and others; [kellerjordan0](https://x.com/kellerjordan0/status/2051363977490489671) highlighted NorMuon improving modded-NanoGPT optimization benchmark records to 3250 steps; [TheAITimeline](https://x.com/TheAITimeline/status/2051401348726317146) summarized DORA, an asynchronous RL system that addresses rollout skew with multiple live policy versions and claims up to 8.2x rollout speedup and 2.12x end-to-end throughput improvement; and [PSGD](https://x.com/_arohan_/status/2051012103025410410) got positive nods as a still-underappreciated optimizer line.

Research, Models, and Multimodal/Scientific Applications

Multi-agent orchestration is itself becoming a model class: [Sakana’s Fugu](https://x.com/SakanaAILabs/status/2050998826190667795) framed a multi-agent orchestration system as a foundation model, and [omarsar0](https://x.com/omarsar0/status/2051306659021242635) highlighted another Sakana paper where a 7B conductor model, trained with RL to design communication topologies and prompts for worker agents, reportedly reached SOTA on GPQA-Diamond and LiveCodeBench. The conceptual shift is important: routing and coordination are being optimized as first-class learned policies.

Scientific discovery and automation remains a high-signal use case: [kimmonismus](https://x.com/kimmonismus/status/2051305620914233400) summarized work using AI on NASA star data to identify 100+ hidden planets from 2.2 million stars; [Richard Socher](https://x.com/RichardSocher/status/2051121805482676323) argued that automating science is among the highest-leverage AI applications; and [cmpatino_](https://x.com/cmpatino_/status/2051343930373837125) shared nanowhale, a 100M-parameter MoE pretrained and post-trained by an agent, as a small but concrete demonstration of agent-driven modelcraft.

Local/open model enthusiasm remains strong: [hnshah](https://x.com/hnshah/status/2051048988292641039) said a recent local model materially improved a 100%-local product; [Nous Research](https://x.com/NousResearch/status/2051321586980880506) offered Trinity-Large-Thinking free in Nous Portal for a week; and [fchollet](https://x.com/fchollet/status/2051370269445615965) made Deep Learning with Python free online, a notable resource drop amid the ongoing wave of practitioners moving down-stack into open weights and self-hosted workflows.

Top tweets (by engagement)

Prompting / usage style: [@pmarca’s custom prompt](https://x.com/pmarca/status/2051374498994364529) for “world class expert” behavior was one of the most engaged AI-adjacent posts, reflecting ongoing interest in system-prompting and output-style control.

Coding-agent economics: [@theo’s Copilot token burn thread](https://x.com/theo/status/2051218167780041147) was the clearest high-engagement data point on how fast agentic usage can break subscription economics.

Recursive self-improvement timelines: [@jackclarkSF](https://x.com/jackclarkSF/status/2051312759594471886) drew major attention with a 60% by end-2028 estimate for AI systems autonomously building successors, with follow-on discussion from [Goodside](https://x.com/goodside/status/2051388803047158175) and [Ryan Greenblatt](https://x.com/RyanPGreenblatt/status/2051373130804011512) about how strong that operationalization really is.

Open tooling discovery: [@andrew_n_carr](https://x.com/andrew_n_carr/status/2051102625613897887) surfaced a Hugging Face model visualizer ([hfviewer](https://x.com/andrew_n_carr/status/2051102627551752654)), which got outsized traction for a genuinely useful piece of ecosystem tooling.

AI Reddit Recap

/r/LocalLlama + /r/localLLM Recap

[
Read more
](https://www.latent.space/p/ainews-the-other-vs-the-utility)

---

---
title: "Latent Space — 2026-04-24"
date: 2026-04-24
source: Latent Space
type: ai-news
---

# 🔬 Latent Space — 2026-04-24

> swyx 開發者簡報，未公開專案 + 工程視角
> 來源：[Latent Space](https://www.latent.space/feed)

---

## [[AINews] GPT 5.5 and OpenAI Codex Superapp](https://www.latent.space/p/ainews-gpt-55-and-openai-codex-superapp)
*🔬 Latent Space | 2026-04-24*

A week after [Opus 4.7](https://www.latent.space/p/ainews-anthropic-claude-opus-47-literally), it was OpenAI’s turn to fire back with very similar Pareto frontier improvement charts for [GPT 5.5](https://openai.com/index/introducing-gpt-5-5/) (as [Noam Brown prefers](https://x.com/polynoamial/status/2047387675762802998?s=46) — raw 1 dimensional intelligence measures are giving way to 2D intelligence per dollar charts). In the 4.7 vs 5.5 bakeoff, you have to read between the lines to see what was NOT mentioned ([coding](https://x.com/chowdhuryneil/status/2047416077622395025?s=46)), but in terms of overall intelligence, AA crowns this the top independently validated model in the world, AND…

[AA chart](https://x.com/ArtificialAnlys/status/2047378419282034920)

… intelligence per dollar (“GPT-5.5 (medium) scores the same as Claude Opus 4.7 (max) on our Intelligence Index at one quarter of the cost (~$1,200 vs $4,800) - although Gemini 3.1 Pro Preview scores the same at a cost of ~$900.”

[aa 2D ](https://x.com/scaling01/status/2047380890402123928?s=20)

There are [some training hardware tidbits](https://x.com/scaling01/status/2047425178724921618?s=46) and [positive](https://x.com/tszzl/status/2047386955550470245?s=46) [RSI](https://x.com/aidan_mclau/status/2047388367705575701?s=46) vibes and [cool](https://x.com/clad3815/status/2047392779006013833?s=12) [alternative](https://x.com/andonlabs/status/2047377260412649967?s=46) [benchmarks](https://x.com/sebastienbubeck/status/2047383628922167390?s=46).

But if you just treated today as a mere point update model launch ([some would prefer to call it 5.9](https://x.com/davis7/status/2047414463595528467)), you’d be mistaken - it’s also [bundling ](https://x.com/sama/status/2047378431260664058?s=20)a big Codex launch day:

[twitter](https://x.com/thsottiaux/status/2047387017974337611?s=46)

With built in browser control and the other features in [this mega-update](https://x.com/ajambrosino/status/2047381565534322694?s=20), as well as folding in the now defunct [Prism](https://www.youtube.com/watch?v=W2cBTVr8nxU&pp=2AYl0gcJCZEKAYcqIYzv) (RIP), OpenAI seems to have made the critical and retoractively obvious choice to turn Codex into the [base of its superapp strategy](https://www.wsj.com/tech/openai-plans-launch-of-desktop-superapp-to-refocus-simplify-user-experience-9e19931d).

AI News for 4/22/2026-4/23/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews’ website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

AI Twitter Recap

OpenAI’s GPT-5.5 launch: stronger agentic coding, broader computer use, and a push on token-efficiency

GPT-5.5 is the day’s dominant release: OpenAI launched [GPT-5.5](https://x.com/OpenAI/status/2047376561205325845), positioned as “a new class of intelligence for real work,” with rollout across [ChatGPT and Codex](https://x.com/OpenAI/status/2047376568809636017) and API access delayed pending additional safeguards. OpenAI and community benchmark posts converged on a profile of better long-horizon execution, stronger computer-use behavior, and materially improved token efficiency rather than a pure across-the-board benchmark blowout. Reported numbers include 82.7% Terminal-Bench 2.0, 58.6% SWE-Bench Pro, 84.9% GDPval, 78.7% OSWorld-Verified, 81.8% CyberGym, 84.4% BrowseComp, and 51.7% FrontierMath Tier 1–3 via [@reach_vb](https://x.com/reach_vb/status/2047377562339524659), with Artificial Analysis saying GPT-5.5 now leads or ties several headline evals and sits on a new cost/performance frontier despite higher per-token pricing [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2047378419282034920), [@scaling01](https://x.com/scaling01/status/2047380890402123928). OpenAI also emphasized that in ChatGPT, stack-level inference gains made GPT-5.5 Pro more practical for demanding tasks [@OpenAI](https://x.com/OpenAI/status/2047376567559668222).

Pricing, context, infra, and practical behavior: API pricing was reported at $5/$30 per 1M input/output tokens for GPT-5.5 and $30/$180 for Pro [@scaling01](https://x.com/scaling01/status/2047375819144597737), with [Sam Altman noting](https://x.com/sama/status/2047379036419014928) a 1M context window in API and lower token use per task than 5.4. Multiple early users described the model as more “human,” less formal, and better suited to persistent agent workflows than prior GPTs, especially inside Codex [@MatthewBerman](https://x.com/MatthewBerman/status/2047375703516361174), [@danshipper](https://x.com/danshipper/status/2047375686688473134), [@omarsar0](https://x.com/omarsar0/status/2047424707310289058). OpenAI claimed the model was co-designed for NVIDIA GB200/300 systems and that the model itself helped improve its own inference stack [@scaling01](https://x.com/scaling01/status/2047377992016384068), while [@sama](https://x.com/sama/status/2047386068194852963) framed the company increasingly as an AI inference company. A recurrent theme from users: GPT-5.5 often feels like a step-function upgrade in autonomy, but can also be exploratory and require tighter instruction to stay on track [@theo](https://x.com/theo/status/2047379702189310085).

Codex becomes a fuller agent workspace: In parallel, OpenAI shipped substantial Codex upgrades: browser control, Sheets/Slides, Docs/PDFs, OS-wide dictation, and auto-review mode [@ajambrosino](https://x.com/ajambrosino/status/2047381565534322694). OpenAI says Codex can now interact with web apps, click through flows, capture screenshots, and iterate until task completion [@OpenAIDevs](https://x.com/OpenAIDevs/status/2047381283358355706), while Auto-review uses a secondary “guardian” agent to reduce approvals on longer runs [@OpenAIDevs](https://x.com/OpenAIDevs/status/2047436655863464011), [@gdb](https://x.com/gdb/status/2047489218998628780). User reports suggest this is expanding Codex from a coding tool into a broader computer-work agent, spanning QA, spreadsheets, presentations, app building, research loops, and overnight experimental runs [@gdb](https://x.com/gdb/status/2047387783111868707), [@tszzl](https://x.com/tszzl/status/2047386955550470245), [@aidan_mclau](https://x.com/aidan_mclau/status/2047388367705575701).

DeepSeek-V4 Preview: 1.6T MIT-licensed open model, 1M context, and aggressive pricing

DeepSeek answered GPT-5.5 within hours: DeepSeek released [DeepSeek-V4 Preview](https://x.com/deepseek_ai/status/2047516922263285776), open-sourcing V4-Pro and V4-Flash under an MIT license. The headline specs are unusually aggressive: V4-Pro: 1.6T total params / 49B active, V4-Flash: 284B / 13B active, both with 1M token context and support for thinking/non-thinking modes [@deepseek_ai](https://x.com/deepseek_ai/status/2047516945466188072), [@Yuchenj_UW](https://x.com/Yuchenj_UW/status/2047514092756418757). Community reactions quickly framed it as the new open-model flagship, competitive with top closed models from the prior generation and a major leap over DeepSeek V3.x [@arena](https://x.com/arena/status/2047518354903359697), [@scaling01](https://x.com/scaling01/status/2047512176856899985), [@kimmonismus](https://x.com/kimmonismus/status/2047514623356579869).

Technical report highlights: long-context efficiency, hybrid attention, and Muon: The launch was notable not just for weights but for a same-day tech report [@scaling01](https://x.com/scaling01/status/2047510520618516572). Community summaries point to two new compressed/hybrid attention mechanisms, mHC, Muon-based training, FP4 quantization-aware training, and pretraining on roughly 32T tokens [@scaling01](https://x.com/scaling01/status/2047510190044409860), [@iScienceLuvr](https://x.com/iScienceLuvr/status/2047514399393579235), [@eliebakouch](https://x.com/eliebakouch/status/2047519300399837677). The strongest technical discussion centered on making 1M context practical, with reported ~4x compute efficiency improvements and order-of-magnitude KV-cache reductions relative to earlier DeepSeek-style stacks [@Hangsiin](https://x.com/Hangsiin/status/2047523724929405328). The rapid infra response was also notable: vLLM announced [day-0 support](https://x.com/vllm_project/status/2047520252851105796) and detailed how it implemented the new attention stack; SGLang shipped [day-0 optimizations and RL pipeline support](https://x.com/lmsysorg/status/2047511629919932623).

Pricing may be as important as the model: DeepSeek’s posted pricing is exceptionally aggressive: V4-Flash at $0.14/$0.28 and V4-Pro at $1.74/$3.48 per 1M input/output tokens [@scaling01](https://x.com/scaling01/status/2047508350238175526), [@teortaxesTex](https://x.com/teortaxesTex/status/2047508587883250112). Several commenters highlighted Flash as potentially the more disruptive SKU if serving quality holds, given the combination of very low cost, 1M context, and open weights [@Hangsiin](https://x.com/Hangsiin/status/2047515855949623667), [@arena](https://x.com/arena/status/2047524055679729885). The main caveat from DeepSeek: V4-Pro throughput is currently limited by high-end compute constraints, with the company explicitly pointing to future Ascend 950 availability for price drops [@teortaxesTex](https://x.com/teortaxesTex/status/2047523707199909977).

Agent infrastructure and tooling: memory, orchestration, browsers, and enterprise plumbing

Agents are becoming systems problems, not just model problems: Several posts emphasized that production agent work is increasingly about harnesses, evals, memory, and orchestration. A useful example was the writeup on stateless decision memory for enterprise agents, which replaces mutable per-agent state with immutable decision logs/event sourcing to improve horizontal scalability, auditability, and fault tolerance [@omarsar0](https://x.com/omarsar0/status/2047325132096758228). In a similar vein, [@Vtrivedy10](https://x.com/Vtrivedy10/status/2047362615836336473) argued that trace data → evals/environments → harness engineering/SFT-RL is the core flywheel for improving production agents, and later used Anthropic’s Claude Code regression as a case study for why open harnesses and open evals matter [@Vtrivedy10](https://x.com/Vtrivedy10/status/2047384831995371631).

New tooling around control surfaces: Cua open-sourced [Cua Driver](https://x.com/trycua/status/2047383200348221632), a macOS driver for letting agents control arbitrary apps in the background with multi-player/multi-cursor support. Cognition published a post on [what it takes to build cloud agent infrastructure](https://x.com/cognition/status/2047392064355377194), naming the practical stack: VM isolation, session persistence, environment provisioning, orchestration, and integrations. LangChain continued expanding LangSmith Fleet with file editing, webpage/presentation generation, and slash-command skills [@LangChain](https://x.com/LangChain/status/2047362259983495215), while multiple users highlighted Fleet’s presentation renderer/viewer as a surprisingly useful agent-native artifact format [@BraceSproul](https://x.com/BraceSproul/status/2047417882423022034).

Multi-agent orchestration is moving into products: Sakana AI launched the beta of Fugu, a multi-agent orchestration API that dynamically selects and coordinates frontier models, with claims of SOTA on SWE-Pro, GPQA-D, and ALE-Bench and even recursive test-time scaling via self-invocation [@SakanaAILabs](https://x.com/SakanaAILabs/status/2047479445209145785), [@hardmaru](https://x.com/hardmaru/status/2047483783323283941). Hermes Agent shipped [v0.11.0](https://x.com/Teknium/status/2047506967909015907) with a large contributor release, expanded providers, image generation support, and effectively immediate GPT-5.5 support [@Teknium](https://x.com/Teknium/status/2047419336537846193). The direction is consistent: agents are becoming orchestration layers over heterogeneous tools and models, not single-model loops.

Vision, video, and multimodal systems: Vision Banana, Sapiens2, HDR video, and omni models

Google DeepMind’s Vision Banana reframes CV as generation: One of the more technically interesting research launches was [Vision Banana](https://x.com/songyoupeng/status/2047312019976785944), a unified vision model that treats 2D/3D vision tasks as image generation, reportedly outperforming specialist SOTA systems across multiple vision tasks. The reaction from computer-vision researchers was that it signals a broader shift in how segmentation, depth, normals, and related tasks may be approached going forward [@sainingxie](https://x.com/sainingxie/status/2047339789926429166). On the open side, Meta also released Sapiens2, a set of high-resolution vision transformers trained on 1B human images for human-centric perception tasks [@HuggingPapers](https://x.com/HuggingPapers/status/2047410529010844044).

Video stack updates are moving past raw resolution into production formats: Kling’s “native 4K” rollout spread across multiple platforms, but the technically more novel launch may be LTX HDR beta, which argues the real bottleneck for AI video in production has been dynamic range, not just resolution, by moving beyond 8-bit SDR toward footage that can survive grading and compositing [@ltx_model](https://x.com/ltx_model/status/2047333864587018703). That’s a more substantive improvement than the usual “4K” marketing alone. Separately, World Labs launched World Jam around Marble 1.1 + Spark LoD for interactive 3D creation [@theworldlabs](https://x.com/theworldlabs/status/2047373234174304473).

Broader multimodal trend: unified models with explicit cross-modal reasoning: The newly shared Context Unrolling in Omni Models proposes a unified model trained across text, images, video, 3D geometry, and hidden representations, explicitly unrolling reasoning across modalities before producing outputs [@arankomatsuzaki](https://x.com/arankomatsuzaki/status/2047519009004716097). Together with Vision Banana, this points to a recurring motif: fold disparate perception/generation tasks into fewer general multimodal backbones, then let inference-time reasoning bridge modalities.

Training, scaling, and research methods: globally distributed pretraining, self-play, and long-context internals

Google’s Decoupled DiLoCo tackles resilient global pretraining: Google DeepMind and Google Research introduced [Decoupled DiLoCo](https://x.com/Ar_Douillard/status/2047329942547968171), which decouples distributed low-communication training to enable worldwide datacenter training, heterogeneous hardware, and tolerance to hardware failures without halting the job. This is a meaningful systems result because it targets a real frontier training bottleneck: keeping giant training runs alive and efficient across faulty, geographically distributed infrastructure, rather than assuming clean homogeneous clusters.

Algorithmic scaling beyond brute-force sampling: A self-play paper highlighted by [@LukeBailey181](https://x.com/LukeBailey181/status/2047340293490724945) studies why long-run self-play plateaus for LLMs and proposes an algorithm that lets a 7B model solve as many problems as pass@4 of a model 100x larger. Another recurring theme was token/computation efficiency as the real frontier metric; several posts argued that single-number intelligence comparisons are increasingly obsolete in a world where effort level and inference budget materially reshape capability [@polynoamial](https://x.com/polynoamial/status/2047387675762802998). Relatedly, a thread on Neural Garbage Collection described training models to manage their own KV cache via RL rather than fixed heuristics, a potentially important direction for long-horizon agents [@cwolferesearch](https://x.com/cwolferesearch/status/2047476297031631102).

Infra adoption signals: Together AI reported growth from 30B to 300T tokens/month YoY [@vipulved](https://x.com/vipulved/status/2047183589222273231), a large-scale indicator of inference demand expansion. Epoch AI, meanwhile, revised down estimates for operational power at Stargate Abilene to ~0.3 GW currently and pushed the full 1.2 GW milestone to Q4 2026, underscoring continued uncertainty in tracking frontier compute deployment [@EpochAIResearch](https://x.com/EpochAIResearch/status/2047442515608162481).

Top tweets (by engagement)

OpenAI GPT-5.5 launch: The highest-engagement technical post was OpenAI’s [GPT-5.5 announcement](https://x.com/OpenAI/status/2047376561205325845), followed by [@sama’s launch post](https://x.com/sama/status/2047378253313106112) and OpenAI DevRel’s framing of GPT-5.5 as its smartest frontier model yet [@OpenAIDevs](https://x.com/OpenAIDevs/status/2047377079352877534).

Claude Code regression post-mortem: Anthropic’s acknowledgment that [Claude Code quality had slipped due to three issues and was fixed in v2.1.116+](https://x.com/ClaudeDevs/status/2047371123185287223) was one of the most engaged engineering-product posts of the day, and sparked substantial discussion about harness sensitivity and regression testing.

DeepSeek-V4 Preview release: DeepSeek’s [official V4 Preview launch](https://x.com/deepseek_ai/status/2047516922263285776) quickly became the other major high-engagement technical event, especially given the combination of MIT license, 1M context, and aggressive pricing.

Vision Banana: Google DeepMind’s [Vision Banana announcement](https://x.com/songyoupeng/status/2047312019976785944) was the standout pure-research vision post.

ML-Intern and autonomous research workflows: The Hugging Face-adjacent [ml-intern passing an internship-style test in 15 minutes](https://x.com/akseljoonas/status/2047332440025321796) and subsequent reports of very high token consumption suggest strong interest in autonomous coding/research harnesses as distinct products, not just demos.

AI Reddit Recap

/r/LocalLlama + /r/localLLM Recap

[
Read more
](https://www.latent.space/p/ainews-gpt-55-and-openai-codex-superapp)

---

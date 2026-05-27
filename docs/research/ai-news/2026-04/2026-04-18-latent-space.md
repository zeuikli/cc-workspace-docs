---
title: "Latent Space — 2026-04-18"
date: 2026-04-18
source: Latent Space
type: ai-news
---

# 🔬 Latent Space — 2026-04-18

> swyx 開發者簡報，未公開專案 + 工程視角
> 來源：[Latent Space](https://www.latent.space/feed)

---

## [[AINews] The Two Sides of OpenClaw](https://www.latent.space/p/ainews-the-two-sides-of-openclaw)
*🔬 Latent Space | 2026-04-18*

In an opportune coinciding of big three letter conferences, the [TED talk](https://x.com/bilawalsidhu/status/2045291456630509709) and the [AIE talks](https://www.youtube.com/watch?v=zgNvts_2TUE&t=2087s&pp=ygUVcGV0ZXIgc3RlaW5iZXJnZXIgdGVk) of Peter Steinberger dropped today. To the general public, the inspiring story of OpenClaw was delightfully [told onstage](https://www.ted.com/talks/peter_steinberger_how_i_created_openclaw_the_breakthrough_ai_agent), which recaps all the highs:

To the engineering audience, it was more sober, talking about the unprecedented levels of security incidents (60x more reports than curl, at least 20% of skill contributions malicious) and scaling issues involved in maintaining the fastest growing open source project in history: 

An AMA moderated by me is included at the end.

Contrast them, thoughts welcome.

AI News for 4/16/2026-4/17/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews’ website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

AI Twitter Recap

Anthropic’s Claude Opus 4.7 and Claude Design rollout

Claude Design launched as Anthropic’s first design/prototyping surface: [@claudeai](https://x.com/claudeai/status/2045156267690213649) announced Claude Design, a research-preview tool for generating prototypes, slides, and one-pagers from natural-language instructions, powered by Claude Opus 4.7. The launch immediately framed Anthropic as moving beyond chat/coding into design tooling; multiple observers called it a direct shot at Figma/Lovable/Bolt/v0, including [@Yuchenj_UW](https://x.com/Yuchenj_UW/status/2045158071950033063), [@kimmonismus](https://x.com/kimmonismus/status/2045162358004216134), and [@skirano](https://x.com/skirano/status/2045192705941106992). The market reaction itself became part of the story, with [@Yuchenj_UW](https://x.com/Yuchenj_UW/status/2045161719547445426) and others noting Figma’s sharp drawdown after the announcement. Product details surfaced via [@TheRundownAI](https://x.com/TheRundownAI/status/2045176722476208454): inline refinement, sliders, exports to Canva/PPTX/PDF/HTML, and handoff to Claude Code for implementation.

Opus 4.7 looks stronger overall, but the rollout was noisy: third-party benchmark posts were broadly favorable. [@arena](https://x.com/arena/status/2045177492936532029) put Opus 4.7 #1 in Code Arena, +37 over Opus 4.6 and ahead of non-Anthropic peers there; the same account also had it at #1 overall in Text Arena with category wins across coding and science-heavy domains [here](https://x.com/arena/status/2045177497378316597). [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2045292578434875552) reported a near three-way tie at the top of its Intelligence Index—Opus 4.7 57.3, Gemini 3.1 Pro 57.2, GPT-5.4 56.8—while also placing Opus 4.7 first on GDPval-AA, their agentic benchmark. They also noted ~35% fewer output tokens than Opus 4.6 at higher score, and introduction of task budgets plus full removal of extended thinking in favor of adaptive reasoning. But user experience was mixed in the first 24 hours: [@VictorTaelin](https://x.com/VictorTaelin/status/2045139180359942462) reported regressions and context failures, [@emollick](https://x.com/emollick/status/2045147490316374414) said Anthropic had already improved adaptive thinking behavior by the next day, and [@alexalbert__](https://x.com/alexalbert__/status/2045159041283064095) confirmed that many initial bugs had been fixed. There were also complaints about product stability in Design itself from [@theo](https://x.com/theo/status/2045310884717981987) and account-level safety issues from the same account [here](https://x.com/theo/status/2045317666383204423).

Cost/efficiency discussion became almost as important as raw quality: [@scaling01](https://x.com/scaling01/status/2045160883010081237) claimed ~10x fewer tokens for some ML problem runs versus prior high-end models while maintaining similar performance, while [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2045206342173086156) placed Opus 4.7 on the price/performance Pareto frontier for both text and code. Not every benchmark agreed on absolute leadership—e.g. [@scaling01](https://x.com/scaling01/status/2045178622617498084) noted it still trails Gemini 3.1 Pro and GPT-5.4 on LiveBench—but the consensus from these posts is that Anthropic materially improved the model’s agentic utility and efficiency.

Computer use, coding agents, and harness design

Computer-use UX is becoming a mainstream product category: OpenAI’s Codex desktop/computer-use updates drew unusually strong practitioner reactions. [@reach_vb](https://x.com/reach_vb/status/2045151640802771394) called subagents + computer use “pretty close” to AGI in practical feel; [@kr0der](https://x.com/kr0der/status/2045154074337710136), [@HamelHusain](https://x.com/HamelHusain/status/2045191726495846459), [@mattrickard](https://x.com/mattrickard/status/2045218583882633412), and [@matvelloso](https://x.com/matvelloso/status/2045209294942142860) all emphasized that Codex Computer Use is not just flashy but fast, able to drive Slack, browser flows, and arbitrary desktop apps, and may be the first genuinely usable computer-use platform for enterprise legacy software. [@gdb](https://x.com/gdb/status/2045375289560007029) explicitly framed Codex as becoming a full agentic IDE.

The field is converging on “simple harness, strong evals, model-agnostic scaffolding”: several high-signal posts argued that reliability gains now come more from harnesses than from chasing the very largest models. [@AsfiShaheen](https://x.com/AsfiShaheen/status/2045072599508508914) described a three-stage financial analyst pipeline—router / lane / analyst—with strict context boundaries and gold sets for each stage, arguing that many bugs were actually instruction/interface bugs. [@AymericRoucher](https://x.com/AymericRoucher/status/2045176781414527305) extracted the same lesson from the leaked Claude Code harness: simple planning constraints plus a cleaner representation layer outperform “fancy AI scaffolds.” [@raw_works](https://x.com/raw_works/status/2045208764509470742) showed an even starker example: Qwen3-8B scored 33/507 on LongCoT-Mini with dspy.RLM, versus 0/507 vanilla, arguing the scaffold—not fine-tuning—did “100% of the lifting.” LangChain shipped more of these patterns into product: [@sydneyrunkle](https://x.com/sydneyrunkle/status/2045209395881980276) added subagent support to deepagents deploy, and [@whoiskatrin](https://x.com/whoiskatrin/status/2045139949939200284) announced memory primitives in the Agents SDK.

Open-source agent stacks continue to proliferate: Hermes Agent remained a focal point. Community ecosystem overviews from [@GitTrend0x](https://x.com/GitTrend0x/status/2045142797439922337) highlighted derivatives like Hermes Atlas, Hermes-Wiki, HUDs, and control dashboards. [@ollama](https://x.com/ollama/status/2045282803387158873) then shipped native Hermes support via ollama launch hermes, which [@NousResearch](https://x.com/NousResearch/status/2045304840645939304) amplified. Nous and Kimi also launched a $25k Hermes Agent Creative Hackathon [@NousResearch](https://x.com/NousResearch/status/2045225469088326039), signaling a push from coding/productivity into creative agent workflows.

Agent research: self-improvement, monitoring, web skills, and evaluation

A cluster of papers pushed agent robustness and continual improvement forward: [@omarsar0](https://x.com/omarsar0/status/2045139481779696027) summarized Cognitive Companion, which monitors reasoning degradation either with an LLM judge or a hidden-state probe. The headline result is notable: a logistic-regression probe on layer-28 hidden states can detect degradation with AUROC 0.840 at zero measured inference overhead, while the LLM-monitor version cuts repetition 52–62% with ~11% overhead. Separate work on web agents from [@dair_ai](https://x.com/dair_ai/status/2045139481892880892) described WebXSkill, where agents extract reusable skills from trajectories, yielding up to +9.8 points on WebArena and 86.1% on WebVoyager in grounded mode. And [@omarsar0](https://x.com/omarsar0/status/2045241905227915498) also highlighted Autogenesis, a protocol for agents to identify capability gaps, propose improvements, validate them, and integrate working changes without retraining.

Open-world evals are becoming a serious theme: several posts argued current benchmarks are too narrow. [@CUdudec](https://x.com/CUdudec/status/2045139195220431022) endorsed open-world evaluations for long-horizon, open-ended settings; [@ghadfield](https://x.com/ghadfield/status/2045245020429570505) connected this to regulation and “economy of agents” questions; and [@PKirgis](https://x.com/PKirgis/status/2045265295649231354) discussed CRUX, a project for regular open-world evaluations of AI agents in messy real environments. On the measurement side, [@NandoDF](https://x.com/NandoDF/status/2045063560716296450) proposed broad NLL/perplexity-based eval suites over out-of-training-domain books/articles across 2500 topic buckets, though that sparked debate about whether perplexity remains informative after RLHF/post-training from [@eliebakouch](https://x.com/eliebakouch/status/2045115926123520100), [@teortaxesTex](https://x.com/teortaxesTex/status/2045139476972745120), and others.

Document/OCR and retrieval evals also got more agent-centric: [@llama_index](https://x.com/llama_index/status/2045145054772183128) expanded on ParseBench, an OCR benchmark centered on content faithfulness with 167K+ rule-based tests across omissions, hallucinations, and reading-order violations—explicitly reframing the bar from “human-readable” to “reliable enough for an agent to act on.” In retrieval, [@Julian_a42f9a](https://x.com/Julian_a42f9a/status/2045200413402493064) noted new work showing late-interaction retrieval representations can substitute for raw document text in RAG, suggesting some RAG pipelines may be able to bypass full-text reconstruction.

Open models, local inference, and inference systems

Qwen3.6 local/quantized workflows were a practical bright spot: [@victormustar](https://x.com/victormustar/status/2045068986446958899) shared a concrete llama.cpp + Pi setup for Qwen3.6-35B-A3B as a local agent stack, emphasizing how viable local agentic systems now feel. Red Hat quickly followed with an NVFP4-quantized Qwen3.6-35B-A3B checkpoint [@RedHat_AI](https://x.com/RedHat_AI/status/2045153791402520952), reporting preliminary GSM8K Platinum 100.69% recovery, and [@danielhanchen](https://x.com/danielhanchen/status/2045169369723064449) benchmarked dynamic quants, claiming many Unsloth quants sit on the Pareto frontier for KLD vs disk space.

Consumer-hardware inference keeps improving: [@RisingSayak](https://x.com/RisingSayak/status/2045114073000657316) announced work with PyTorch/TorchAO enabling offloading with FP8 and NVFP4 quants without major latency penalties, explicitly targeting consumer GPU users constrained by memory. Apple-side local inference also got a showcase with [@googlegemma](https://x.com/googlegemma/status/2045204738720084191), which demoed Gemma 4 running fully offline on iPhone with long context.

Inference infra updates worth noting: [@vllm_project](https://x.com/vllm_project/status/2045381618928582995) highlighted MORI-IO KV Connector with AMD/EmbeddedLLM, claiming 2.5× higher goodput on a single node via a PD-disaggregation-style connector. Cloudflare continued its agent/AI-platform push with isitagentready.com [@Cloudflare](https://x.com/Cloudflare/status/2045126394418503846), Flagship feature flags [@fayazara](https://x.com/fayazara/status/2045133183575113771), and shared compression dictionaries yielding dramatic payload reductions such as 92KB → 159 bytes in one example [@ackriv](https://x.com/ackriv/status/2045177696506794336).

AI for science, medicine, and infrastructure

Scientific discovery and personalized health were prominent applied themes: [@JoyHeYueya](https://x.com/JoyHeYueya/status/2045147082546462860) and [@Anikait_Singh_](https://x.com/Anikait_Singh_/status/2045149764636094839) posted about insight anticipation, where models generate a downstream paper’s core contribution from its “parent” papers; the latter introduced GIANTS-4B, an RL-trained model that reportedly beats frontier models on this task. On the health side, [@SRSchmidgall](https://x.com/SRSchmidgall/status/2045023895041061353) shared a biomarker-discovery system over wearable data whose first finding was that “late-night doomscrolling” predicts depression severity with ρ=0.177, p<0.001, n=7,497—notable because the model itself named the feature. Separately, [@patrickc](https://x.com/patrickc/status/2045164908912968060) argued current coding agents are already highly useful for personalized genome interpretation, describing <$100 analysis runs that surfaced a roughly 30× elevated melanoma predisposition plus follow-on interventions.

Large-scale compute buildout remains a core meta-story: [@EpochAIResearch](https://x.com/EpochAIResearch/status/2045258390147088764) surveyed all 7 US Stargate sites and concluded the project appears on track for 9+ GW by 2029, comparable to New York City peak demand. [@gdb](https://x.com/gdb/status/2045279841482928271) framed Stargate as infrastructure for a “compute-powered economy,” while [@kimmonismus](https://x.com/kimmonismus/status/2045206835238441332) put today’s annual global datacenter capex at roughly 5–7 Manhattan Projects per year in inflation-adjusted terms.

Top tweets (by engagement)

Claude Design / Anthropic product expansion: [@claudeai launches Claude Design](https://x.com/claudeai/status/2045156267690213649), by far the day’s biggest pure-AI product launch signal.

Model benchmarking / rankings: [@ArtificialAnlys on Opus 4.7 tying for #1 overall and leading GDPval-AA](https://x.com/ArtificialAnlys/status/2045292578434875552).

Coding agents / computer use: [@cursor_ai doubles Composer 2 limits in the new agents window](https://x.com/cursor_ai/status/2045236540784492845) and [@HamelHusain on Codex Computer Use](https://x.com/HamelHusain/status/2045191726495846459).

Open-source agents: [@ollama ships native Hermes Agent support](https://x.com/ollama/status/2045282803387158873).

Applied AI in medicine: [@patrickc on coding agents for genome analysis and personalized prevention](https://x.com/patrickc/status/2045164908912968060).

Infra / power scaling: [@EpochAIResearch on Stargate’s 9+ GW trajectory](https://x.com/EpochAIResearch/status/2045258390147088764).

AI Reddit Recap

/r/LocalLlama + /r/localLLM Recap

1. Qwen3.6 Model Launch and Features

[
Read more
](https://www.latent.space/p/ainews-the-two-sides-of-openclaw)

---

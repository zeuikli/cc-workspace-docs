---
title: "Latent Space — 2026-04-29"
date: 2026-04-29
source: Latent Space
type: ai-news
---

# 🔬 Latent Space — 2026-04-29

> swyx 開發者簡報，未公開專案 + 工程視角
> 來源：[Latent Space](https://www.latent.space/feed)

---

## [[AINews] not much happened today](https://www.latent.space/p/ainews-not-much-happened-today)
*🔬 Latent Space | 2026-04-29*

When we made the AINews → Substack move, we committed to having Matt Levine style op-eds every day, but some days there just isn’t much going on and we will just say so - we are working on small essays around inference demand and multiagents, but today is not that day.

Interesting model releases from [Nvidia Nemotron](https://x.com/NVIDIAAI/status/2049159441870717428?s=20), [Poolside](https://x.com/poolsideai/status/2049144111626670282?s=20), and [Alec Radford](https://x.com/status_effects/status/2048878495539843211), but it’s unclear any of them will stand the test of time. [GPT-6 hype](https://x.com/sama/status/2049241518540808440?s=20) is beginning.

AI News for 4/27/2026-4/28/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews’ website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

AI Twitter Recap

Inference Systems, vLLM 0.20, and the Hardware/Kernel Race Around DeepSeek V4

vLLM’s latest release is heavily about memory and MoE serving efficiency: [vLLM v0.20.0](https://x.com/TeksEdge/status/2048983564801450315) shipped with TurboQuant 2-bit KV cache for 4× KV capacity, FA4 re-enabled for MLA prefill on SM90+, a new vLLM IR foundation, fused RMSNorm for a reported 2.1% end-to-end latency improvement, plus support updates spanning DeepSeek V4 MegaMoE on Blackwell, Jetson Thor, ROCm, Intel XPU, and easier GB200/Grace-Blackwell setup. In parallel, [SemiAnalysis](https://x.com/SemiAnalysis_/status/2048957715955765284) highlighted early DeepSeek V4 Pro serving results on B200/B300/H200/GB200 disaggregated setups, claiming B300 can be up to 8× faster than H200 for this workload and pointing to upcoming vLLM 0.20 benchmarking with DeepGEMM MegaMoE, which fuses EP dispatch + EP combine + GEMMs + SwiGLU into a single mega-kernel.

DeepSeek support: several posts focused on serving tradeoffs: [Jeremy Howard noted DeepSeek V4’s support for prefill](https://x.com/jeremyphoward/status/2049098509530583199) as a capability many providers have dropped, while [Maharshi](https://x.com/maharshii/status/2049058891389108640) pointed out the overheads of dynamic activation quantization, arguing that static quantization often wins on inference speed despite calibration cost. There was also growing interest in alternate stack portability: [teortaxesTex argued DeepSeek is structurally moving away from CUDA lock-in via TileKernels](https://x.com/teortaxesTex/status/2049185408785998217), suggesting model vendors may increasingly optimize for heterogeneous or domestic accelerator fleets rather than NVIDIA-only deployment.

Open Model Releases: Poolside Laguna XS.2, NVIDIA Nemotron 3 Nano Omni, and TRELLIS.2

Poolside made its first public model release with an unusually deployment-friendly open-weight coder: [@poolsideai announced Laguna XS.2](https://x.com/poolsideai/status/2049144111626670282), a 33B total / 3B active MoE coding model trained fully in-house, released under Apache 2.0, and advertised as able to run on a single GPU. [Poolside’s broader release](https://x.com/eisokant/status/2049142230397370537) also included Laguna M.1 and an agent harness, emphasizing that the company trained from scratch on its own data, training infra, RL, and inference stack. Community summaries added more color: [Aymeric Roucher](https://x.com/AymericRoucher/status/2049156715304935451) described two coder models—225B/23B active and 33B/3B active—with hybrid attention, FP8 KV cache, and claimed performance near Qwen-3.5; [Ollama](https://x.com/ollama/status/2049184817603031463) shipped it immediately.

NVIDIA’s Nemotron 3 Nano Omni was the day’s biggest infra-native model launch: [@NVIDIAAI introduced Nemotron 3 Nano Omni](https://x.com/NVIDIAAI/status/2049159441870717428), an open 30B / A3B multimodal MoE with 256K context built for agentic workloads spanning text, image, video, audio, and documents. Distribution was immediate across the stack: [OpenRouter](https://x.com/OpenRouter/status/2049164366218772526), [LM Studio](https://x.com/lmstudio/status/2049172192705864091), [Ollama](https://x.com/ollama/status/2049194377751437470), [Unsloth](https://x.com/UnslothAI/status/2049161390150365344), [fal](https://x.com/fal/status/2049160999442198632), [Fireworks](https://x.com/FireworksAI_HQ/status/2049159136802398546), [DeepInfra](https://x.com/DeepInfra/status/2049158141070524815), [Together](https://x.com/togethercompute/status/2049160446708711883), [Baseten](https://x.com/baseten/status/2049160818575749300), [Canonical](https://x.com/Canonical/status/2049159988174602712), and others all announced same-day availability. Key specs surfaced in follow-on posts: [Piotr Żelasko](https://x.com/PiotrZelasko/status/2049162049599455725) described it as NVIDIA’s first omni release with speech/audio understanding backed by a Parakeet encoder, English-only for now, and a 5.95% WER on the Open ASR leaderboard. Several hosts cited ~9× throughput versus comparable open omni models.

Other notable model/paper releases: [Microsoft’s TRELLIS.2](https://x.com/kimmonismus/status/2049099376476459372) is an open-source 4B image-to-3D model producing up to 1536³ PBR textured assets, built on native 3D VAEs with 16× spatial compression. On the world-model side, [World-R1](https://x.com/wjwang2003/status/2049136028968272260) claims existing video models already encode 3D structure and can be “woken up” with RL, requiring no architecture changes, no extra video training data, and no added inference cost.

Agents, Local-First Tooling, and Production Orchestration

Agent builders are shifting from demos to production primitives: [Mistral launched Workflows in public preview](https://x.com/MistralAI/status/2049128071874179091) as an orchestration layer aimed at turning enterprise AI processes into durable, observable, fault-tolerant production systems. Related posts echoed the same theme: [Sydney Runkle framed durable execution](https://x.com/sydneyrunkle/status/2049132897227936073) as a key requirement for long-running agents, and [threepointone described work on subagents / agents-as-tools with persistence, streaming, and resumption](https://x.com/threepointone/status/2049088722835042475).

Local/offline agents moved from aspiration to credible workflow: [Teknium asserted “totally offline agents are possible”](https://x.com/Teknium/status/2048975223853350976), while [Niels Rogge demoed Pi + local models](https://x.com/NielsRogge/status/2049128153658839324) for desktop cleanup and [Google Gemma shared a tutorial for local coding agents](https://x.com/googlegemma/status/2049163687639007451). Hugging Face’s local push also showed up in adoption numbers: [Clement Delangue said 300,000 users have added hardware specs to the Hub](https://x.com/ClementDelangue/status/2049139562929143917) to discover what can run locally. Complementing this, [Ammaar open-sourced a vibe-coding app running Gemma 4 fully on-device with MLX](https://x.com/ammaar/status/2049169134429073471), and [Kimmonismus highlighted Sigma](https://x.com/kimmonismus/status/2049244932477759767), a private browser-based local-agent concept using open models.

Hermes and adjacent agent harnesses are gaining real-world traction: multiple posts reported Hermes outperforming OpenClaw in instruction-following or practical workflows, including [SecretArjun](https://x.com/SecretArjun/status/2049006382763110639), [somewheresy](https://x.com/somewheresy/status/2049089485938315614), and users deploying Hermes through [Telegram](https://x.com/lizliz404/status/2049084890717806877) or for [medical literature extraction](https://x.com/bobvarkey/status/2049120693649125687). On the research-agent side, [Hugging Face’s ML Intern](https://x.com/_lewtun/status/2049021398312468815) was trending among Spaces, and later gained [native metric logging + Trackio integration](https://x.com/akseljoonas/status/2049183527703396699) to make its training jobs observable rather than black-box.

Benchmarks, Evals, and Research Findings Worth Watching

Model benchmarking remains fragmented, but a few signals stood out: [Epoch reported GPT-5.5 Pro reaching ](https://x.com/EpochAIResearch/status/2049186851844771888)[159 on the Epoch Capabilities Index](https://x.com/EpochAIResearch/status/2049186851844771888) and new highs on FrontierMath—52% on Tiers 1–3 and 40% on Tier 4—including two Tier 4 problems not previously solved by any model. Separately, [Greg Kamradt said ARC-AGI-3 testing for GPT-5.5 and Opus 4.7 had completed](https://x.com/GregKamradt/status/2049121093307547654), with failure modes now under analysis.

Several new benchmarks target more realistic agent and engineering behavior: [Lysandre announced a benchmark for making Transformers more agent-friendly](https://x.com/LysandreJik/status/2049053056814436352), and [VibeBench](https://x.com/jpschroeder/status/2049139723776495800) proposed subjective testing by 1,000 qualified software engineers to measure how models actually feel in real work. On document intelligence, [LlamaIndex’s ParseBench](https://x.com/llama_index/status/2049139409316946011) emphasized that OCR benchmarks miss semantic formatting such as strikethroughs and superscripts, which materially alter meaning for agents.

Research notes with concrete engineering implications: [Rosinality flagged bugs in DeepSpeed and OpenRLHF that reduce SFT performance](https://x.com/rosinality/status/2049024030749970699), with implications for prior studies. [Arjun Kocher published a faithful implementation of Compressed Sparse Attention from the DeepSeek-V4 paper](https://x.com/arjunkocher/status/2049066844925936041). [che_shr_cat showed single-block transformers can solve Extreme Sudoku only with an explicit scratchpad and inverted routing init](https://x.com/che_shr_cat/status/2049081240762876261), otherwise performance is zero. On optimization, [Keller Jordan released a lightweight Modded-NanoGPT optimizer benchmark](https://x.com/kellerjordan0/status/2049193527440187494) designed to compare methods like Muon and AdamW on a reproducible speedrun-style task.

Platform Economics, API Pricing, and Closed-Model Reliability Concerns

[
Read more
](https://www.latent.space/p/ainews-not-much-happened-today)

---

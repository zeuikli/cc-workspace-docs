---
title: "Latent Space — 2026-05-14"
date: 2026-05-14
source: Latent Space
type: ai-news
---

# 🔬 Latent Space — 2026-05-14

> swyx 開發者簡報，未公開專案 + 工程視角
> 來源：[Latent Space](https://www.latent.space/feed)

---

## [[AINews] The End of Finetuning](https://www.latent.space/p/ainews-the-end-of-finetuning)
*🔬 Latent Space | 2026-05-13*

The proximal cause of today's op-ed is OpenAI's deprecation of their finetuning APIs. 

[](https://substackcdn.com/image/fetch/$s_!ioj8!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd6915f95-7d03-4a7d-81b1-df255b9debcb_1192x1422.png)

For years, OpenAI stood out among the big labs for their finetuning support, and [many many many talks and content pieces and AI engineers](https://www.youtube.com/@OpenAI/search?query=finetuning) promoted how you can get some variant of "get o1 performance at 4o prices" and insisting that it was an important part of the toolkit. 

Now the tide is out, [Anthropic will probably raise at a higher valuation than OpenAI for the first time ever](https://www.latent.space/p/ainews-anthropic-growing-10xyear), and Finetuning is the[ next casualty of the 2026 Side Quest massacre (after Sora)](https://www.latent.space/p/ainews-apples-war-on-slop?utm_source=publication-search). If you assume an extreme GPU crunch, that makes sense, but even without dramatic compute constraints, the modal 80% of the AI Engineering industry was probably trending there anyway, with [Jeremy Howard calling it out on the pod as early as 2023](https://www.latent.space/p/fastai).

The "End" of a thing for most people does NOT mean the "End" of a thing period - and in fact the top tier, like Cursor and Cognition (whose [$25B round ](https://x.com/colossusmag/status/2053801052571312414)is now public discussion) have both INCREASED open model RLFT and usage, rather than decreased. Open Model finetunes may also be central to [the Custom ASIC Thesis](https://www.latent.space/p/ainews-the-custom-asic-thesis?utm_source=publication-search), but if Taalas' model and continued P/D Disaggregation inference solutions are any indication, then maybe Just Very Long Prompts (like [Claude's Constitution](https://x.com/AnthropicAI/status/2053881827396653207)) are all you need…

> AI News for 5/11/2026-5/12/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

# **AI Twitter Recap**

**Research Benchmarks, Hard Evals, and Agentic Science Systems**

  * **Research-level reasoning benchmarks keep getting harder** : [Soohak](https://x.com/gson_AI/status/2054036114483392997) introduces **439 research-level math problems** authored from scratch by **64 mathematicians** (including **38 faculty**), explicitly targeting capabilities above standard olympiad-style math. In medical evaluation, [@SophontAI](https://x.com/SophontAI/status/2054270239387627927) released **Medmarks v1.0** , expanding its open medical benchmark suite from **20 ->30 benchmarks** and **46 ->61 models**. There's also growing sentiment that old evals are saturating: [@polynoamial](https://x.com/polynoamial/status/2054255862441812099) argues benchmarks with uniformly high scores should be retired in favor of lower-scoring, frontier-challenging tests.

  * **Agentic systems are starting to move benchmark frontiers in science and math** : Google DeepMind's [AI Co-Mathematician](https://x.com/dair_ai/status/2054224343551639958) is described as an asynchronous, stateful research workbench for mathematicians, reportedly reaching **48% on FrontierMath Tier 4** while supporting ideation, literature discovery, computational analysis, theorem verification, and formal outputs. In theoretical physics, [physics-intern](https://x.com/dlouapre/status/2054217281895309480) boosts **Gemini 3.1 Pro from 17.7% to 31.4% on CritPt** via decomposition into specialized agents. On coding/program synthesis, [ProgramBench's first task](https://x.com/KLieret/status/2054215545663144217) was reportedly solved by **GPT-5.5 high/xhigh** , with xhigh outperforming **Opus 4.7 xhigh** across metrics.

  * **Retrieval and search benchmarks are rewarding small, specialized models** : LightOn's [Agent-ModernColBERT](https://x.com/LightOnIO/status/2054202169255973121) stacks another **~10%** over Reason-ModernColBERT on BrowseComp-Plus while keeping the retriever at **149M parameters** , with claims of matching or exceeding much larger model-based systems when paired with a generator. Related discussion from [@xuzihuan4](https://x.com/xuzihuan4/status/2054220800073642161) asks whether lexical retrieval may suffice in agentic search loops when agents can iteratively refine their own queries.




**Training, Optimization, and Scaling-Law Techniques**

  * **Optimizer work continues to compress training cost and improve small-scale experimentation** : Several tweets centered on fast variants of **SOAP/Muon-style updates**. [@torchcompiled](https://x.com/torchcompiled/status/2054036715589771542) applied tangent-step + Stiefel manifold retraction to **SOAP basis updates** , with [follow-up discussion](https://x.com/torchcompiled/status/2054088499591000255) on drift checks and QR fallback for stability. In the Modded-NanoGPT community, [SOAP-Muon](https://x.com/kellerjordan0/status/2054255672636981423) set a new record at **3150 steps (-60)** , while an earlier [MuLoCo-style outer Nesterov SGD wrap on NorMuonH](https://x.com/kellerjordan0/status/2054098451621978471) also improved results, both backed by p-value reporting.

  * **Formal methods and superoptimization are beginning to merge with ML systems work** : [@leloykun](https://x.com/leloykun/status/2054076097881592068) described a **Lean4-to-TileLang tensor program superoptimizer** that can automatically discover kernels such as **FlashAttention2** , **FlashNorm** , and **split-k matmul** , reporting roughly **1.8 × geomean speedup on A100s**. The same framework is positioned to jointly search over kernels, optimizers, hyperparameter transfer rules, and scaling laws.

  * **Scaling laws and training metrics are being re-examined** : [@che_shr_cat](https://x.com/che_shr_cat/status/2054178651856339276) argues the classic **" 20 tokens per parameter"** framing is tokenizer-dependent and that scaling should be measured in **bytes** , not tokens. Separately, [@JJitsev](https://x.com/JJitsev/status/2054166378823794881) emphasized that prescriptive scaling laws are valuable not just for prediction, but as a systematic basis for comparing learning procedures across scales.

  * **Training-time-only efficiency tricks are getting more interesting** : [Lighthouse Attention](https://x.com/omarsar0/status/2054224130103554359) from Nous is highlighted as a subquadratic **training wrapper** around vanilla attention that can be removed near the end of training after a recovery phase, preserving standard deployment-time inference while reducing long-context pretraining cost. In a similar spirit, [Renderers](https://x.com/PrimeIntellect/status/2054347134821154841) from Prime Intellect addresses the token/message impedance mismatch between RL trainers and agent environments, claiming **> 3× throughput** on popular open models.




**Inference Systems, Serving Stacks, and Runtime Infrastructure**

  * **Blackwell racks are emerging as the reference platform for large-MoE serving** : Perplexity published details on serving post-trained **Qwen3 235B** on **NVIDIA GB200 NVL72** systems, arguing GB200 is a major inference step up over Hopper for large MoEs. Their [benchmarks](https://x.com/perplexity_ai/status/2054204425833726353) cite **NVLS all-reduce latency** dropping from **586.1 µs on H200 to 313.3µs on GB200**, and **MoE prefill combine** at EP=4 dropping from **730.1 µs to 438.5µs**, with better decode throughput at high token rates. [@AravSrinivas](https://x.com/AravSrinivas/status/2054206802133504234) framed this as materially changing prefill/decode disaggregation for serving large MoEs.

  * **Inference orchestration is increasingly specialized, not "just Kubernetes"**: [Modal](https://x.com/charles_irl/status/2054233051140690023) argues inference needs a dedicated stack, citing work on compute management, cloud-native caching, **CRIU** , and **GPU checkpointing**. That positioning got an immediate real-world endorsement from Perceptron, which said [all Mk1 inference runs on Modal](https://x.com/AkshatS07/status/2054275262289002664) because native video, structured outputs, and hybrid reasoning create unusual cold-start and scaling requirements.

  * **OSS inference economics continue to improve fast** : [SemiAnalysis](https://x.com/SemiAnalysis_/status/2054245527957508520) reported that clustering multiple **B200 8-GPU** machines over **RoCEv2 CX-7** with **PD disaggregation** can lift **per-GPU token throughput by up to 7 ×**, implying comparable cost-per-token reductions. On the vector DB side, [Qdrant 1.18](https://x.com/qdrant_engine/status/2054166055417938266) added **TurboQuant** , claiming recall near scalar quantization with **2 × less memory**, alongside memory monitoring and named-vector lifecycle operations.

  * **Agent runtimes are becoming version-control-like substrates** : A standout systems idea was Stanford's **Shepherd** , summarized by [@ai_satoru_chan](https://x.com/ai_satoru_chan/status/2054126183374348296), which treats agent execution more like **Git** : first-class tasks, effects, scopes, and traces; exact replay; branching; rollback; and formal guarantees in **Lean**. Claimed results include live-supervision gains on CooperBench from **28.8% ->54.7%**, plus faster counterfactual optimization and tree-RL rollouts.




**Product and Model Releases: Multimodal, Video, Retrieval, and Embeddings**

  * **Perceptron Mk1 was the most substantive new model release in the set** : [@perceptroninc](https://x.com/perceptroninc/status/2054216828285796630) launched **Perceptron Mk1** as a model for **frontier video and embodied reasoning** , with native video support at **up to 2 FPS** , temporal grounding, multimodal in-context learning, and structured spatial outputs. [OpenRouter's summary](https://x.com/OpenRouter/status/2054232344148787462) notes a **32k multimodal context** and first-class outputs like points, boxes, polygons, and clips. The release is framed less as a generic VLM and more as a physical-world reasoning stack.

  * **Google and Meta both pushed multimodal interaction layers rather than standalone model specs** : Google DeepMind's [AI-enabled mouse pointer demos](https://x.com/GoogleDeepMind/status/2054246119635300451) reimagine the cursor as a contextual pointing interface tied to Gemini, allowing users to point at on-screen content and speak shorthand instructions. In parallel, Meta announced [Meta AI voice conversations powered by Muse Spark](https://x.com/MetaNewsroom/status/2054205287515484397), adding interruption, language switching, image generation, and live camera-grounded interaction.

  * **Embedding and retrieval model updates were notable** : Jina released [jina-embeddings-v5-omni](https://x.com/JinaAI_/status/2054226262047301933), a universal embedding model for **text, images, audio, and video** , in **1.57B** and **0.95B** variants, both with Matryoshka truncation and backward compatibility with existing v5-text indexes. Meta quietly released [Sapiens2](https://x.com/mervenoyann/status/2054187884417102319), a family of human-centric high-resolution ViTs spanning **0.1B ->5B** params for pose estimation, segmentation, normals, and pointmaps.

  * **Diffusion and image tooling kept moving** : Hugging Face's [Diffusers 0.38.0](https://x.com/RisingSayak/status/2054110949469196748) added new pipelines including **Ace-Step 1.5** , **LongCat-AudioDiT** , and **Ernie-Image** , plus support for **Flash Attention 4** , **FlashPack loading** , and **Ring Anything** for context parallelism. Other research releases included [ELF: Embedded Language Flows](https://x.com/iScienceLuvr/status/2054118255778763184), a continuous-space text diffusion model, and Tencent's [Pixal3D](https://x.com/_akhaliq/status/2054120807425511826) for pixel-aligned 3D generation.




**Agents, Tooling, and Developer Workflow**

  * **Agent products are shifting from demos to operational platforms** : OpenAI teased [Symphony](https://x.com/OpenAIDevs/status/2054252221941121035) as a system where **every open task gets a running Codex agent** , and separately highlighted [computer use for Codex](https://x.com/OpenAIDevs/status/2054298427245441141) to work across apps without full takeover. LangChain re-open-sourced [its revamped Chat LangChain app](https://x.com/BraceSproul/status/2054231134163321287), describing it as a production Q&A agent handling nearly **2T tokens/week**.

  * **Long-running-agent state management is becoming a first-class systems problem** : LangGraph's new [DeltaChannel snapshots](https://x.com/sydneyrunkle/status/2054278551244099706) aim to replace full-state checkpointing for scalable durable execution; LangChain says the same mechanism now powers message histories and file storage in **deepagents v0.6**. The broader pattern also shows up in Google's [Gemini Interactions API guide](https://x.com/_philschmid/status/2054225343251206528), where encrypted `thought` signatures preserve reasoning context across turns in both stateful and stateless modes without forcing developers to manage signature injection manually.

  * **Synthetic data and RL environment generation are being operationalized** : [@Vtrivedy10](https://x.com/Vtrivedy10/status/2054054238226170361) offered a useful practitioner perspective: targeted synthetic data extraction from model weights is hard at scale, especially for underrepresented distributions like long sequences, and effective pipelines need programmatic tests, verifiers, judges, and agentic long-horizon framing. On the infrastructure side, [Tau2-Infinity](https://x.com/Shahules786/status/2054241505506648161) formalizes autonomous mining of hard tool-use tasks for RL post-training via DAG walks or world-generation from failure hypotheses.

  * **Top tweets (by engagement, filtered for technical relevance)** :

    * **Gemini as an OS-level intelligence layer** : Google's [Gemini Intelligence](https://x.com/sundarpichai/status/2054255858700415005), [Googlebook](https://x.com/Google/status/2054270454467121187), and [AI pointer demos](https://x.com/GoogleDeepMind/status/2054246119635300451) collectively point to agentic UX moving from chat windows into the operating system.

    * **Isomorphic Labs funding** : [@demishassabis](https://x.com/demishassabis/status/2054197462101889277) announced **$2.1B** in new funding for AI-driven drug discovery, one of the largest capital commitments in this dataset tied directly to an applied AI platform.

    * **Speech-to-speech benchmarking** : Artificial Analysis' [τ-Voice benchmark](https://x.com/ArtificialAnlys/status/2054234919887573292) found even the best S2S models solve only about **half of realistic customer service scenarios** , with **Grok Voice Think Fast 1.0** leading at **52.1%**.

    * **Claude Opus 4.7 fast mode** : Anthropic's [fast mode release](https://x.com/ClaudeDevs/status/2054266327771275435) reached APIs and Claude Code, with Cursor noting [2.5× speed at 6× cost](https://x.com/cursor_ai/status/2054274305345618163), a concrete new point on the latency/price frontier.




**Security, Supply Chain, and Safer Coding**

  * **The most urgent operational story was the Mini Shai-Hulud supply-chain attack** : [@IntCyberDigest](https://x.com/IntCyberDigest/status/2054166749998661659) reported the campaign had expanded beyond TanStack to hit **OpenSearch, Mistral AI, Guardrails AI, UiPath, and others** across npm and PyPI, specifically targeting **AI developer tooling**. The noteworthy technical detail is persistence: it allegedly hooks into **Claude Code** (`.claude/settings.json`) and **VS Code** (`.vscode/tasks.json`) so the compromise can re-execute on future tool events even after package removal. [Guardrails AI](https://x.com/guardrails_ai/status/2054341322304299086) later confirmed its **0.10.1** package was compromised and quarantined within about **2 hours**.

  * **Actionable mitigations surfaced quickly** : [@ramimacisabird](https://x.com/ramimacisabird/status/2054178771180093858) noted that beyond `minimumReleaseAge`, teams should enable `blockExoticSubdeps` to prevent remote GitHub references from slipping into dependency graphs. [@elithrar](https://x.com/elithrar/status/2054162732195197283) reiterated that GitHub's `pull_request_target` remains one of the sharpest CI/CD footguns for fork-based PR automation. And at the workstation level, [@andersonbcdefg](https://x.com/andersonbcdefg/status/2054212574162653535) recommended moving secrets out of ubiquitous local `.env` files into a proper secrets manager.

  * **Safer codegen is becoming its own research track** : Stanford-aligned work on [SecureForge](https://x.com/houjun_liu/status/2054233718269595869) targets vulnerability discovery/prevention in LLM-generated code via prompt optimization, while [the corresponding paper listing](https://x.com/FSFG/status/2054196048621367422) frames it as a bridge between codegen and security evaluation. The broader point: coding agents are now strong enough that supply-chain hardening and secure-generation evaluation need to be treated as core infra, not side concerns.




* * *

# **AI Reddit Recap**

## **/r/LocalLlama + /r/localLLM Recap**

### **1\. Qwen 3.6 MTP and Long-Context Local Evals**

  * **[MTP on Unsloth](https://www.reddit.com/r/LocalLLaMA/comments/1ta4rvs/mtp_on_unsloth/)** (Activity: 727): **The[image](https://i.redd.it/7qopol51pi0h1.png) is a Hugging Face activity screenshot showing Unsloth AI publishing/updating MTP-preserved GGUF builds: **`unsloth/Qwen3.6-27B-GGUF-MTP`**and**`unsloth/Qwen3.6-35B-A3B-GGUF-MTP`**. The technical significance is that these GGUFs retain the MTP / next-token-prediction auxiliary layer, but users reportedly still need to checkout and build a specific llama.cpp MTP PR rather than relying on default llama.cpp support. One commenter hit a runtime/model-load assertion,**`GGML_ASSERT(hparams.nextn_predict_layers > 0 && "QWEN35_MTP requires nextn_predict_layers > 0")`**, suggesting tooling or metadata support is still fragile for these MTP GGUFs.** Commenters are mainly waiting on upstream inference support, with one joking about constantly refreshing `llama.cpp` and `vLLM` GitHub repos. There is also uncertainty over whether MTP is supported "out of the box" in llama.cpp; the post indicates it is not yet.

    * A user compiling/running the new `27B` GGUF model reports a hard assertion failure in `qwen35_mtp.cpp`: `GGML_ASSERT(hparams.nextn_predict_layers > 0 && "QWEN35_MTP requires nextn_predict_layers > 0") failed`. This suggests the GGUF/model metadata being loaded is missing or not exposing `nextn_predict_layers`, which is required for **Qwen3.5 MTP** execution in the current implementation.

    * Several commenters are tracking whether **llama.cpp** and **vLLM** have landed native **MTP** support, with one explicitly asking whether llama.cpp now supports MTP "out of the box." The thread implies support is still in flux across backends and that users are watching upstream repositories for compatibility with GGUF MTP models.

    * One technical takeaway is that **MTP support in GGUF** is viewed as important for local inference, especially for Qwen-style variants such as the mentioned `35B A3B` model. A commenter highlights the `35B A3B` variant as interesting specifically because of expected context-length improvements.

  * **[The Qwen 3.6 35B A3B hype is real!!!](https://www.reddit.com/r/LocalLLaMA/comments/1t9whrt/the_qwen_36_35b_a3b_hype_is_real/)** (Activity: 713): **A user benchmarked Qwen 3.6 35B A3B, Qwen 3.6 27B, Gemma 4 26B A4B, and Nemotron 3 Nano on a niche paper-to-code comprehension task, feeding each model an academic paper plus accompanying research code via long-context mechanisms such as gated delta nets, hybrid Mamba2, and sliding-window attention. In their[detailed findings](https://github.com/nathanlgabriel/paper_code_mapping_assessment/blob/main/README.md), all four small/local open-weight models substantially outperformed prior small-model baselines such as [Devstral Small 2](https://www.reddit.com/r/LocalLLaMA/comments/1ry93gz/devstral_small_2_24b_severely_underrated/), with Qwen 3.6 35B A3B judged strongest; Devstral Small 2 could not fit the long-context workload in **`32GB`**VRAM/RAM.** Commenters noted practical tradeoffs: **Qwen 35B** is preferred for long-context/refactoring but can be verbose/slow in thinking mode, while **Gemma 26B** is faster for code fixes/chats; at `q4`, one user reports ~`20GB` for Qwen 35B and ~`15GB` for Gemma 26B, allowing both to stay loaded. Another commenter criticized the evaluation for not documenting inference settings, which limits reproducibility.

    * Several users compared local workflows using **Gemma 26B** and **Qwen 35B** , noting that both can be kept resident simultaneously at `q4` quantization because Qwen 35B is about `20 GB` and Gemma 26B about `15 GB`. One commenter uses Gemma 26B thinking mode for quick code fixes/chat and Qwen 35B thinking mode for longer-context refactoring, but reports Qwen 35B has high latency due to excessive reasoning verbosity before final output.

    * A coding-focused report claimed **Qwen 27B** can handle large projects (`100k+` LOC) effectively when bootstrapped by a stronger model/coding agent for initial project setup, then switched to Qwen for continued work. The user found little practical difference between Qwen 27B and **DeepSeek V4** for their use case, though Qwen occasionally entered loops requiring manual interruption and continuation prompting.

    * One commenter emphasized that **Qwen 27B/35B performance is sensitive to inference configuration** , specifically temperature/sampling parameters and avoiding overly aggressive quantization of either the model weights or KV cache. Another asked for the missing run settings, implying the original claims are hard to evaluate without details like quantization level, sampler settings, context length, backend, or hardware.




### **2\. Memory-Tiered and Power-Efficient Local Inference**

  * **[Computer build using Intel Optane Persistent Memory - Can run 1 trillion parameter model at over 4 tokens/sec](https://www.reddit.com/r/LocalLLaMA/comments/1taeg8h/computer_build_using_intel_optane_persistent/)** (Activity: 964): **The image shows the internals of a high-memory Xeon workstation/server build using Intel Optane DC Persistent Memory DIMMs, matching the post 's claim of running Kimi K2.5, a ~**`1T`**parameter MoE model, locally at about**`4 tokens/s`**via llama.cpp hybrid GPU/CPU inference. The key technical point is the use of**`768GB`**Optane PMem in Memory Mode, where Optane appears as system RAM and**`192GB`**DDR4 ECC DRAM acts as cache, allowing the model 's sparse expert weights to reside in PMem while attention/dense/shared expert/routing tensors fit on an RTX 3060 12GB using **`override-tensor`**or**`ngl auto`**/**`cmoe`**.[Image](https://i.redd.it/na7zo7lmck0h1.jpeg)** Commenters noted that a higher-core-count Cascade Lake Xeon, such as an ES 8260/QQ89, could improve throughput, and debated whether Optane **Storage Mode** plus `mmap` might outperform Memory Mode. Others found the build impressive but questioned whether `4 tokens/s` is practically tolerable for interactive use.

    * A detailed hardware note suggests performance may improve with a higher-core-count Cascade Lake Xeon, e.g. **QQ89 ES / Xeon Gold 8260-class**`24-core`, versus the current **Xeon Gold 6246**`12-core`. The commenter also proposes benchmarking Optane PMem in **storage mode +**`mmap` versus **memory mode** , noting that memory mode uses DRAM as a transparent cache and requires pages to be swapped back into DRAM before CPU execution, so it is not equivalent to normal RAM latency.

    * One commenter provides a concise Optane PMem platform compatibility breakdown: **LGA3647 Skylake/Cascade Lake uses 1st-gen Optane**`NMA`**at**`2666 MT/s`, while **LGA4189 uses 2nd-gen**`NMB`, running at `2666` on Cooper Lake and `3200` on Ice Lake. They also note that mixing Optane with DRAM on Cascade Lake can downclock affected channels to `2666`, and that many Xeons from this era have a `1 TB`**total memory limit across DRAM + Optane** , unless using high-memory SKUs or later platforms.

    * A technical caveat is raised that while `~4 tokens/sec` generation on a trillion-parameter model may be tolerable for some uses, **prompt processing/prefill speed is likely to be much worse** on this kind of memory hierarchy. Another comment estimates the full used-market build cost at roughly `$2060-$2500`, including a **Xeon Gold 6246** , **TYAN S5630GMRE-CGN** , **RTX 3060 12GB** , `192 GB` DDR4 ECC RDIMM, and `768 GB` Intel Optane DCPMM.

  * **[Stop wasting electricity](https://www.reddit.com/r/LocalLLaMA/comments/1tayu5t/stop_wasting_electricity/)** (Activity: 905): **A user benchmarked**`llama.cpp`****`llama-server`**on an RTX 4090 with**`Qwen3.6-27B-UD-Q4_K_XL.gguf`**, full GPU offload (**`-ngl all`**), FlashAttention enabled,**`q4_0`**K/V cache quantization,**`32`**threads, and a**`262144`**context, varying the GPU power cap via**`sudo nvidia-smi -pl N`**. They report the GPU was consistently power-limited and that reducing the power limit can substantially lower power/heat/noise with little to no decode / token-generation (**`tg`**) throughput loss; a commenter notes prefill (**`pp`**) is more sensitive, with roughly**`15-20%`**performance loss when dropping from**`450W`**to**`270W`**, model-dependent.** Commenters were mainly interested in separating **decode vs prefill** behavior, since decode appears power-insensitive while prefill degrades more noticeably. One RTX 5090 user said they already cap power for hardware-safety concerns and may reduce it further based on these results.

    * Users focused on the performance impact of GPU power limiting: **decode/token generation (**`tg`**) reportedly is not the bottleneck** , while **prefill (**`pp`**) takes a larger hit**. One commenter quantified the tradeoff as only about `15-20%`**prefill performance loss** when reducing power from `450W`**to**`270W`, depending on the model, suggesting substantial efficiency gains from aggressive power caps.




### **3\. Ultra-Small On-Device Transformer Experiments**

  * **[I got a real transformer language model running locally on a stock Game Boy Color!](https://www.reddit.com/r/LocalLLaMA/comments/1tbi2n3/i_got_a_real_transformer_language_model_running/)** (Activity: 368): **The image ([jpeg](https://i.redd.it/1hl9id7ghs0h1.jpeg)) shows a stock Game Boy Color running a local TinyStories transformer demo, with the screen displaying **`TINYSTORIES Q8 GBC`**and**`Prompt tokenized`**. Per the post, this is Andrej Karpathy 's TinyStories-260K converted to **`INT8`**/fixed-point math in a GBDK-2020 MBC5 ROM, with weights in bank-switched cartridge ROM and the KV cache stored in cartridge SRAM due to the GBC 's tiny work RAM. The author notes it is **_**extremely slow**_**and produces mostly gibberish because of aggressive quantization/approximations, but the core local transformer prefill + autoregressive generation loop works on-device with no PC, phone, Wi-Fi, link cable, or cloud inference:[github.com/maddiedreese/gbc-transformer](https://github.com/maddiedreese/gbc-transformer).** Comments are mostly enthusiastic praise; one commenter said it made them want to run a model on an **N64** , and another linked a related/joke Game Boy language-model project, [gbalm](https://code.heni.lol/heni/gbalm).

    * A commenter linked a prior Game Boy language-model project, **gbalm** ([code](https://code.heni.lol/heni/gbalm)), indicating there has been earlier experimentation with extremely constrained on-device LM inference on Nintendo handheld hardware. This is relevant as a comparison point for implementation approaches and feasibility on non-GPU, retro 8-bit-class systems.

    * One technical question centered on why CUDA/ROCm-style GPU stacks are not required here: the commenter notes that typical LLM inference is associated with mature GPU compilers, yet this demo runs on hardware comparable to _" a potato."_ The implicit point is that sufficiently tiny transformer models can be executed with hand-written or highly simplified CPU-style inference loops, though at very low throughput, and that portability to unsupported accelerators such as future Chinese GPUs would depend more on having a basic compute backend than full CUDA compatibility.

  * **[Needle: We Distilled Gemini Tool Calling Into a 26M Model](https://www.reddit.com/r/LocalLLaMA/comments/1tb9b0r/needle_we_distilled_gemini_tool_calling_into_a/)** (Activity: 271): **Cactus Compute released Needle, an MIT-licensed**`26M`**parameter single-shot tool-calling model distilled from Gemini-synthesized data, claiming**`6000 tok/s`**prefill and**`1200 tok/s`**decode on consumer devices; weights are on[Hugging Face](https://huggingface.co/Cactus-Compute/needle) and code/docs are on [GitHub](https://github.com/cactus-compute/needle). Architecturally it uses "Simple Attention Networks" -- attention plus gating with no MLP/FFN layers -- arguing that function calling is mostly retrieval/assembly over provided tool schemas rather than memorized reasoning; training used **`200B`**pretraining tokens on**`16 TPU v6e`**for**`27h`**plus**`2B`**synthesized function-calling tokens in**`45m`**([architecture writeup](https://github.com/cactus-compute/needle/blob/main/docs/simple_attention_networks.md)). The authors claim it beats FunctionGemma-270M, Qwen-0.6B, Granite-350M, and LFM2.5-350M on single-shot function calling, while acknowledging those larger models have broader conversational capacity.** Commenters framed the model as potentially useful as a lightweight router that dispatches queries/tools or escalates to a larger LLM, with one asking whether the same architecture could support high-quality summarization. A technical concern was raised about uploaded `pickle` files due to Python-specific dependency and deserialization security risks.

    * A commenter framed the `26M` distilled tool-calling model as a lightweight **router/gating model** : it could decide whether a query should be sent to a larger LLM and with which parameters, effectively reducing expensive model calls to cases where they are needed. They also speculated whether the same architecture could generalize to constrained summarization workflows, though no benchmark evidence was provided in the thread.

    * One technical thread focused on the authors' claimed **" no FFN"** result: for tasks with external structured knowledge such as **RAG, tool use, and retrieval-augmented generation** , the model may not need feed-forward layers to store factual knowledge if relevant facts are already present in context. A commenter extrapolated this into a pipeline where a small post-trained model routes requests to RAG and then uses retrieved context to generate a natural-language answer.

    * Several implementation/security concerns were raised: one commenter noted that publishing **pickle files** is increasingly avoided because of Python-specific dependency issues and arbitrary-code-execution risk during deserialization. Another pointed out that **Gemini** has had visible tool-calling quirks, including system-prompt-like reasoning about avoiding `cat` and preferring tools such as `grep_search`, raising the possibility that a distilled dataset could inherit provider-specific tool-use biases if not cleaned carefully.




## **Less Technical AI Subreddit Recap**

> /r/Singularity, /r/Oobabooga, /r/MachineLearning, /r/OpenAI, /r/ClaudeAI, /r/StableDiffusion, /r/ChatGPT, /r/ChatGPTCoding, /r/aivideo, /r/aivideo

### **1\. Claude Coding Workflows and Tooling**

[ Read more ](https://www.latent.space/p/ainews-the-end-of-finetuning)

---

## [[AINews] Thinking Machines' Native Interaction Models - TML-Interaction-Small 276B-A12B - advances SOTA Realtime Voice a…](https://www.latent.space/p/ainews-thinking-machines-native-interaction)
*🔬 Latent Space | 2026-05-12*

By complete coincidence, the day we [released](https://x.com/neilzegh/status/2053945753073074484?s=20) Neil Zeghidour (CEO of Gradium, the for profit spinoff of the vaunted [Kyutai Moshi](https://kyutai.org/))'s [talk](https://www.youtube.com/watch?v=P_RI1kCkRbo&time_continue=0&source_ve_path=MjM4NTE&embeds_referring_euri=https%3A%2F%2Fx.com%2F) on what remains to be built for realtime voice, **Thinking Machines** emerged for only the [third](https://news.smol.ai/issues/25-10-01-thinky) [time](https://news.smol.ai/issues/25-02-18-ainews-xai-grok-3-and-mira-muratis-thinking-machines) in a ~year (despite much drama) to drop [Interaction Models: A Scalable Approach to Human-AI Collaboration](https://thinkingmachines.ai/blog/interaction-models/), **TML-Interaction-Small** is a 276B parameter MoE with 12B active., which immediately advances the state of the art of realtime voice models as Neil had laid out, updating [the famously dead GPT 4o "her" demo](https://openai.com/index/hello-gpt-4o/) with far more detailed demos that are presumably far closer to real use:

The [full blogpost](https://thinkingmachines.ai/blog/interaction-models/) has lots of demos of the level of continuous interactivity, focusing on streams of "time-aligned microturns" of 200ms each:

[](https://substackcdn.com/image/fetch/$s_!LR03!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F02190942-3f50-4067-ae03-97c6b504b3a3_1490x1592.png)

Using encoder-free early fusion, with images and audio all processed <200ms, similar to Meta's [Chameleon](https://arxiv.org/abs/2405.09818):

[](https://substackcdn.com/image/fetch/$s_!S2rk!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F68576e99-b00a-4069-b93f-bbe906ddd810_1336x1602.png)

There are a number of official benchmarks that the team shows beating both [GPT-Realtime-2](https://www.latent.space/p/ainews-gpt-realtime-2-translate-and) and [Gemini 3.1-Flash](https://www.latent.space/p/ainews-nano-banana-2-aka-gemini-31) on basic things like BigBench Audio and IFEval and FD-bench, but the level of interactivity aimed for required making 2 new internal benchmarks for time awareness, simultaneous translation, and visual proactivity:

  * **TimeSpeak:** Can the model **initiate speech** at user-specified times? 

    * Example: "I want to practice my breathing, remind me to breathe in and out every 4 seconds until I ask you to stop."

  * **CueSpeak:** Can the model speak at the **appropriate moment?**

    * Example: "Everytime I codeswitch and use another language, give me the correct word in the original language."

  * **[RepCount-A](https://arxiv.org/abs/2204.01018)** contains videos of repeated actions and is adapted into an online counting task - measures **continuous visual tracking and timely counting**.

  * **[ProactiveVideoQA](https://arxiv.org/abs/2507.09313)** consists of videos with questions, whose answers become available at specific moments. Higher scores require correct answers at the correct times, silence gets partial credit, and incorrect answers are penalized.

  * **[Charades](https://arxiv.org/abs/1604.01753)** is a standard temporal action-localization benchmark. 

    * Stream a user audio instruction: "Say 'start' when the person starts doing {action} then say 'Stop' when they stop."




But look past the numbers: the single most visceral demo is this one buried at the bottom. Play the samples and feel the AGI:

[](https://substackcdn.com/image/fetch/$s_!V7pE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0bfcadcb-b746-4873-aed4-6095f19f5897_1478x1676.png)

The closing notes leave tantalizing hints to Thinky's roadmap, including an intriguing pairing of background agents with interactive models, which we like a whole lot.

[](https://substackcdn.com/image/fetch/$s_!PeGT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fef289b1c-4613-4835-98e6-475906d494da_1394x588.png)

> AI News for 5/9/2026-5/11/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

# **AI Twitter Recap**

**Thinking Machines ' Native Interaction Models and the Shift Beyond Turn-Based AI**

  * **Full-duplex multimodal interaction as a first-class model capability** : The day's clearest technical theme was [Thinking Machines' preview of "interaction models"](https://x.com/miramurati/status/2053939069890298321), described as models trained **from scratch** for real-time interaction rather than layering speech, turn-taking, and tool use onto a turn-based LLM. The accompanying [technical post](https://x.com/thinkymachines/status/2053938892152435174) and team commentary from [@johnschulman2](https://x.com/johnschulman2/status/2053940452789981426), [@soumithchintala](https://x.com/soumithchintala/status/2053940215505645938), and [@cHHillee](https://x.com/cHHillee/status/2053940218747842619) frame this as a **human ↔AI bandwidth** problem: models should be able to listen, speak, watch, think, search, and react concurrently. Demos emphasized continuous-time awareness, interruption handling, simultaneous speech, visual proactivity, and background tool use without explicit "now I'm thinking / now I'm searching" boundaries. Team members also highlighted that many tasks that previously needed special-purpose systems become zero-shot once the type signature is effectively continuous **audio+video+text -> audio+text** ([@johnschulman2](https://x.com/johnschulman2/status/2053940940885332028)).

  * **Why it matters technically** : Several reactions converged on the same point: this is not "another chatbot demo" but a change in interface assumptions. [@liliyu_lili](https://x.com/liliyu_lili/status/2053942465477197891) pointed to **visual proactivity** ("tell me when I start slouching", "count my pushups") as a missing primitive in current systems; [@rown](https://x.com/rown/status/2053950123139575863) called it the first general **video+speech** model that is visually proactive; [@kimmonismus](https://x.com/kimmonismus/status/2053952846064767384) and [@giffmana](https://x.com/giffmana/status/2053953584300003405) both emphasized that native interactivity is the deeper innovation than raw benchmark claims. This launch also implicitly raises the bar for "realtime" multimodal systems, as noted by [@swyx](https://x.com/swyx/status/2053960011748098462). One implementation detail surfaced via [@eliebakouch](https://x.com/eliebakouch/status/2053982248253190180): the stack is using **SGLang**.




**OpenAI 's Enterprise and Security Push: Deployment Company and Daybreak**

  * **OpenAI is moving down-stack into services and deployment** : OpenAI announced the [OpenAI Deployment Company](https://x.com/OpenAI/status/2053824997777457651), a majority-owned unit built to help enterprises deploy frontier models into real workflows. The key operating detail is **150 Forward Deployed Engineers and Deployment Specialists** coming in via the acquisition of [Tomoro](https://x.com/OpenAI/status/2053824999736410415), with [@gdb](https://x.com/gdb/status/2053884619695730745) citing **$4B of initial investment from 19 partners**. Multiple observers read this as OpenAI adopting a Palantir-/Microsoft-style field-engineering model: [@kimmonismus](https://x.com/kimmonismus/status/2053844403488194827) argued OpenAI wants to own the **deployment layer** of the AI economy, while [@matvelloso](https://x.com/matvelloso/status/2053881988529139765) connected it to the historical enterprise success pattern of embedding technical staff close to customer operations.

  * **Daybreak: security-specific model distribution, workflow, and trust tiers** : OpenAI also launched [Daybreak](https://x.com/OpenAI/status/2053939702110269822), an umbrella effort around defensive cyber operations and continuously securing software, with [@sama](https://x.com/sama/status/2053951874408276193) positioning it as a practical response to rapidly improving AI cyber capability. The product pitch, summarized by [@TheRundownAI](https://x.com/TheRundownAI/status/2053945340592631843), combines **GPT-5.5** , **Codex** , repository threat modeling, vuln discovery, patch generation, and response automation, with differentiated access tiers including **Trusted Access for Cyber** and a more specialized **GPT-5.5-Cyber**. This stands in contrast to Anthropic's more restrictive cyber posture, a tension captured by [@kimmonismus](https://x.com/kimmonismus/status/2053941490490265661). For teams building secure agent systems, a separate warning from [@lukOlejnik](https://x.com/lukOlejnik/status/2053758553723211988) is relevant: **" Your LLM is not a security boundary"**--Microsoft Semantic Kernel reportedly allowed prompt injection to be turned into host-level RCE because the framework over-trusted model output rather than the model itself failing.




**Agent Harnesses, Local-First Tooling, and Control Surfaces**

  * **Better agent control planes are becoming a product category** : A recurring complaint is that useful agents need autonomy, but engineers still want reversible, inspectable control. [@itsclelia](https://x.com/itsclelia/status/2053716807748567329) addressed this with **aggit** , a Rust CLI for local/remote, S3-backed storage of agent artifacts, enabling stash/branch/restore semantics outside the main Git history. In the same vein, [@_catwu](https://x.com/_catwu/status/2053999857799672111) highlighted a new `claude agents` terminal control plane for managing multiple Claude Code agents, and [@cursor_ai](https://x.com/cursor_ai/status/2053939390410612988) pushed Cursor into **Microsoft Teams** , where the agent reads the full thread and opens a PR. These are all signs that "agent orchestration" is converging on concrete UX patterns rather than prompt tricks alone.

  * **Deep Agents / Hermes / local agents are maturing quickly** : [@masondrxy](https://x.com/masondrxy/status/2053717333433340034) noted that **Deep Agents CLI** can hot-swap underlying model providers **mid-conversation without losing context** , a nontrivial systems capability that many agent stacks still miss. LangChain also highlighted **harness profiles** for provider/model-specific tuning ([tweet](https://x.com/masondrxy/status/2053882188870074848)), and separate pricing analysis from the same author argued that **DeepSeek V4 Flash** can be dramatically cheaper than GPT/Gemini flash-tier options for high-volume agent workloads ([tweet](https://x.com/masondrxy/status/2053855842076942555)). On the local side, Hugging Face added [Hermes Agent support in local apps plus native trace visualization](https://x.com/mervenoyann/status/2053857347429151163), while [@Teknium](https://x.com/Teknium/status/2053961675985113404) previewed **computer use with any model** via Hermes Agent and CUA, explicitly targeting local/open models as well as frontier APIs. [@onusoz](https://x.com/onusoz/status/2053812410730037256) joining Hugging Face to improve local models in **OpenClaw** and related open harnesses is another strong signal that local agent ergonomics are now strategic infrastructure.

  * **A design thesis emerging around tools** : [@threepointone](https://x.com/threepointone/status/2053751241977594102) argued that agents may asymptotically want just **two primitive tools: search and execute** , with dynamic semantic discovery of capabilities rather than ever-expanding static tool menus. That complements the broader move toward configurable harnesses instead of giant monolithic prompts.




**Benchmarks, Efficiency, and Open-Model Economics**

  * **Coding-agent benchmarking is finally measuring harness+model pairs** : [Artificial Analysis launched a Coding Agent Index](https://x.com/ArtificialAnlys/status/2053865095076438427) spanning SWE-Bench-Pro-Hard-AA, Terminal-Bench v2, and SWE-Atlas-QnA, comparing not just models but **model+harness combinations**. Their topline: **Opus 4.7** in Cursor CLI scored **61** , with **GPT-5.5** in Codex/Claude Code close behind; top open-weight setups included **GLM-5.1** , **Kimi K2.6** , and **DeepSeek V4 Pro** in Claude Code, still competitive but meaningfully behind. The benchmark also exposed large variation in **cost per task** (>30x), **token usage** (>3x), **cache hit rates** (80-96%), and **time per task** (>7x). That benchmark was complemented by OpenHands' updated software-engineering benchmark announcement ([tweet](https://x.com/OpenHandsDev/status/2053839810343620980)) and Claw-Eval's more agentic task mix across office, finance, terminal, and web tasks, where [MiMo-V2.5-Pro led and DeepSeek V4 Flash looked unusually efficient for its size](https://x.com/nathanhabib1011/status/2053786853929824385).

  * **TurboQuant skepticism is increasing** : Multiple posts pointed to a more sober view of the recently popular quantization/serving technique. [@_EldarKurtic](https://x.com/_EldarKurtic/status/2053809592061030546) presented what he described as the first comprehensive study of **TurboQuant** , covering accuracy, latency, and throughput; [@vllm_project](https://x.com/vllm_project/status/2053852636093239555) linked the Red Hat / vLLM investigation as a starting point; and [@jbhuang0604](https://x.com/jbhuang0604/status/2053882357833208262) bluntly summarized the takeaway as "it doesn't really work well." This is exactly the sort of infra claim where independent reproduction matters.

  * **Local/open models continue to improve faster than hardware ceilings** : [@ClementDelangue](https://x.com/ClementDelangue/status/2053825719587815711) made the strongest high-level argument here: on the same top-end MacBook Pro memory ceiling, the "smartest open-weight model you can actually run" improved from Llama 3 70B-era capability to **DeepSeek V4 Flash mixed-Q2 GGUF** -era capability at roughly **4.7x in 24 months** , implying a doubling every **10.7 months** , faster than Moore's Law. Supporting datapoints came from [@victormustar](https://x.com/victormustar/status/2053780086596288781) on the rapid growth of GGUF uploads and from repeated community observations that **Qwen 3.6** , **Gemma 4** , and DeepSeek variants are now usable locally for nontrivial agent tasks.




**Research Highlights: MoE Modularity, Diffusion/Byte Models, and Agent Dynamics**

  * **Architectures and evaluation** : AllenAI's **EMO** was highlighted by [@TheTuringPost](https://x.com/TheTuringPost/status/2053795343658303860) as a more modular Mixture-of-Experts design where document-level routing induces shared expert pools; notably, keeping only **25% of experts** reportedly costs just **~1%** performance versus **10 -15%** degradation in standard MoEs under similar pruning ([follow-up](https://x.com/TheTuringPost/status/2053795410490339720)). On generative evaluation, [@qberthet](https://x.com/qberthet/status/2053795951228371311) introduced **MIND (Monge Inception Distance)** as a purportedly faster, more sample-efficient replacement for FID.

  * **Diffusion for language and byte-level modeling** : Several papers pushed non-AR language modeling. [@LucaAmb](https://x.com/LucaAmb/status/2053867347023466850) reported continuous bitstream diffusion nearly matching autoregressive models under their evaluation setup; [@JulieKallini](https://x.com/JulieKallini/status/2053853543552217478) introduced **Fast BLT** , using diffusion for parallel byte decoding to make byte-level LMs less inference-bound; [@sriniiyer88](https://x.com/sriniiyer88/status/2053882384211419375) framed it as combining block byte-diffusion with self-speculative decoding. Relatedly, [@LiangZheng_06](https://x.com/LiangZheng_06/status/2053806963839168619) noted a useful property of diffusion models for post-training: because sampling is differentiable, reward gradients can in principle flow straight to parameters more directly than in standard LLM setups.

  * **Agent behavior under long horizons** : Two strong empirical threads surfaced. First, ["The Memory Curse"](https://x.com/omarsar0/status/2053863994499408214) claims long histories degrade cooperation in multi-round social dilemmas because models become more **history-following and risk-minimizing** , with explicit CoT sometimes amplifying the problem. Second, [PwC work summarized by @dair_ai](https://x.com/dair_ai/status/2053866106151182419) argues that the value of clarification is highly time-dependent: **goal clarification loses most of its value after ~10% of execution** , while input clarification remains useful longer. Together these suggest that long-horizon agent quality is constrained as much by memory/control policy as by raw model IQ.

  * **Scaling and self-improvement** : Marin's **Delphi** scaling work, summarized by [@WilliamBarrHeld](https://x.com/WilliamBarrHeld/status/2053919463880462453), claims a **0.2%** prediction error when extrapolating from small pretrains to a **25B / 600B token** run. Separately, [@omarsar0](https://x.com/omarsar0/status/2053978221193130434) highlighted **AutoTTS** , where an LLM searches the test-time scaling controller space itself, reportedly beating hand-designed strategies for about **$39.9** of discovery cost.




**Top tweets (by engagement)**

  * **OpenAI 's enterprise/services move**: [OpenAI launches the Deployment Company](https://x.com/OpenAI/status/2053824997777457651) and [Tomoro acquisition / 150 FDEs](https://x.com/OpenAI/status/2053824999736410415).

  * **OpenAI 's security productization**: [Daybreak announcement](https://x.com/OpenAI/status/2053939702110269822) and [@sama's framing](https://x.com/sama/status/2053951874408276193).

  * **Thinking Machines ' interaction models**: [Mira Murati's launch tweet](https://x.com/miramurati/status/2053939069890298321) and the [technical preview thread](https://x.com/thinkymachines/status/2053938892152435174).

  * **Artificial Analysis Coding Agent Index** : [benchmark launch and topline findings](https://x.com/ArtificialAnlys/status/2053865095076438427).

  * **Agent tooling / developer workflow** : [Hermes Agent computer use with any model](https://x.com/Teknium/status/2053961675985113404), [Cursor in Microsoft Teams](https://x.com/cursor_ai/status/2053939390410612988), and [Codex OpenAI Developers plugin](https://x.com/OpenAIDevs/status/2053925962287583379).




* * *

# **AI Reddit Recap**

## **/r/LocalLlama + /r/localLLM Recap**

### **1\. Qwen 3.6 Local Inference Advances**

  * **[MTP on Unsloth](https://www.reddit.com/r/LocalLLaMA/comments/1ta4rvs/mtp_on_unsloth/)** (Activity: 620): **The image ([link](https://i.redd.it/7qopol51pi0h1.png)) shows Unsloth's Hugging Face profile listing newly published MTP-preserving GGUF builds: **`unsloth/Qwen3.6-27B-GGUF-MTP`**and**`unsloth/Qwen3.6-35B-A3B-GGUF-MTP`**. The post 's technical significance is that these GGUFs retain the MTP / next-token prediction layers, but users still need to build a specific llama.cpp MTP PR rather than relying on standard llama.cpp support. One commenter reports a runtime/assertion failure with the 27B GGUF: **`GGML_ASSERT(hparams.nextn_predict_layers > 0 && "QWEN35_MTP requires nextn_predict_layers > 0")`**, suggesting either metadata parsing, model conversion, or PR compatibility issues remain unresolved.** Comments reflect anticipation for upstream llama.cpp MTP support, with users repeatedly checking the GitHub repo and asking whether MTP is now supported "out of the box."

    * A user compiling the new `27B` GGUF model hit a runtime assert in `qwen35_mtp.cpp`: `GGML_ASSERT(hparams.nextn_predict_layers > 0 && "QWEN35_MTP requires nextn_predict_layers > 0")`. This suggests the GGUF/model metadata or conversion path may be missing `nextn_predict_layers`, which is required for Qwen3.5 MTP speculative/next-token prediction layers.

    * One technical thread notes that **MTP support in GGUF** is important for local inference, especially for the `35B A3B` variant, which commenters associate with improved context-length handling. Another commenter asks whether this means `llama.cpp` now supports MTP "out of the box," implying uncertainty around whether support is merged/stable versus only available in a PR or fork.

    * A commenter claims `ik_llama`**MTP is currently faster than the**`llama.cpp`**PR** , and adds that it supports Hadamard-based quants, described as similar to "turboquants." This is a potentially relevant implementation/performance distinction for users comparing local MTP inference backends.




[ Read more ](https://www.latent.space/p/ainews-thinking-machines-native-interaction)

---

## [[AINews] Anthropic growing 10x/year while everyone else is laying off >10% of their workforce](https://www.latent.space/p/ainews-anthropic-growing-10xyear)
*🔬 Latent Space | 2026-05-09*

While you could debate [ARR revenue recognition](https://www.latent.space/p/ainews-anthropic-spacexais-300mw5byr), it is hard to deny very real reports of [secondary market](https://x.com/akashagi/status/2052054549964476782) and [traditional media reporting](https://www.ft.com/content/a40cafcc-0fa4-4e70-9e24-90d826aea56d) that Anthropic, after their "miracle Q1" of [80x annualized growth](https://www.latent.space/p/ainews-anthropic-spacexais-300mw5byr) and [one month jump of $15B ARR](https://x.com/pythiar/status/2050049696698429637?s=46), is now being valued at $1-1.2T, making it officially overtake OpenAI as the 11th-[15th](https://x.com/akashagi/status/2052054549964476782?s=20) most valuable company in the world.

[](https://substackcdn.com/image/fetch/$s_!8FDE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F52674313-df4c-453e-a3c9-e8177361596e_966x968.png)

This is a REVENUE, not a financial speculation, chart: 

[](https://substackcdn.com/image/fetch/$s_!AMfz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F16948c4c-0672-46a5-bf0b-b80ccc0a2591_944x1016.png)

All this and while [Block](https://fortune.com/2026/04/17/twitter-cofounder-block-ceo-jack-dorsey-thought-process-laid-off-40-staff-ai/) (40%), [Coinbase](https://x.com/brian_armstrong/status/2051616759145185723) (14%), and [Cloudflare](https://news.ycombinator.com/item?id=48054423) (20%) have laid off massive swathes of their workforce, all citing AI readiness. It's hard to tell the degree to which this is "AI-washing" "normal" layoffs, but it is clear that stronger companies, [like Linear](https://x.com/artman/status/2052657017370661346), are the ones that grow, not shrink, due to AI. 

And of course, the "AI" growth has mostly been hardware and energy, rather than software:

[](https://substackcdn.com/image/fetch/$s_!tOlW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F021c44bf-dba1-44ad-b3a5-d4de3e6a7644_1728x954.jpeg)

With the AI growth and non-AI shrinkage, we are approaching bubble territories of concentrations in the economy:

[](https://substackcdn.com/image/fetch/$s_!Yobw!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdb8ea82d-37e1-404c-88b6-d99f5b745e2a_960x860.png)

> AI News for 5/7/2026-5/8/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

# **AI Twitter Recap**

**OpenAI 's GPT-5.5 / Codex rollout, cyber models, and safety instrumentation**

  * **GPT-5.5 family keeps expanding across modalities and products** : OpenAI staff highlighted a rapid release cadence spanning **gpt-image-2, GPT-5.5, GPT-5.5 Pro, GPT-5.5 Instant, GPT-Realtime-2, realtime translate, realtime whisper, and GPT-5.5 Cyber** in roughly two weeks, per [@reach_vb](https://x.com/reach_vb/status/2052884864701960366). External reactions were notably positive on the new default/low-reasoning behavior: [@dhh](https://x.com/dhh/status/2052754523702088179) said GPT-5.5 is "very good, very efficient," while [@gdb](https://x.com/gdb/status/2052783746009440658) called it "very capable and very succinct." On public evals, [Arena](https://x.com/arena/status/2052876951329919383) placed **GPT-5.5 Instant** at **#5 on Multi-Turn** , **#11 on Vision** , and **#24 on Document Arena**. There was also strong product uptake around **Notebook workflows in Gemini-like form factors** , but OpenAI mindshare today centered on model usability and efficiency rather than a single benchmark spike.

  * **Codex is becoming a long-running agent runtime, not just a coding assistant** : OpenAI pushed users toward the new [Codex "switch to Codex" flow](https://x.com/OpenAI/status/2052800507727781979), while [@reach_vb](https://x.com/reach_vb/status/2052805243268718803) described `/goal` as a mechanism for indefinite task pursuit across refactors, migrations, retries, and experiments. Independent testing by [@patience_cave](https://x.com/patience_cave/status/2052772581888156128) found Codex Goals reached **61% on public ARC-AGI-3 games** after **160 hours / 30k actions** , with most useful work happening in the first few hours before stagnation. OpenAI also published how it runs Codex safely at scale--**sandboxing, approval gates, network policy, and telemetry** --via [@ithilgore](https://x.com/ithilgore/status/2052843807809610078), reinforced by [@cryps1s](https://x.com/cryps1s/status/2052845089849049434). Separately, OpenAI disclosed an alignment-process issue around accidental **chain-of-thought grading** , plus mitigations like real-time detection and monitorability stress tests in a thread by [@OpenAI](https://x.com/OpenAI/status/2052845764507062349).

  * **Cybersecurity models are now an explicit product line** : OpenAI signaled enterprise/government intent with [Sam Altman's note](https://x.com/sama/status/2052558319940944256) about helping companies secure themselves "quickly," followed by [@gdb](https://x.com/gdb/status/2052583338561683775) announcing **GPT-5.5-Cyber** in limited preview for defenders securing critical infrastructure. The broader policy framing also shifted: [@deredleritt3r](https://x.com/deredleritt3r/status/2052844272798302475) reported the upcoming U.S. AI security executive order would emphasize **collaboration with frontier labs on cyber defense** rather than pre-approval of frontier models.




**Open models and infra: Zyphra 's ZAYA1, vLLM/SGLang optimization, and cheaper coding stacks**

  * **Zyphra made the most substantive open-model release of the day** : [@ZyphraAI](https://x.com/ZyphraAI/status/2052547054707335237) released **ZAYA1-74B-Preview** , a **74B total / 4B active MoE** , framed as a strong **pre-RL base checkpoint** trained while scaling on **AMD** hardware. The model is under **Apache 2.0** per [the follow-up](https://x.com/ZyphraAI/status/2052547063251079600). Community reaction treated it as proof that Zyphra has moved beyond small-MoE experimentation; [@teortaxesTex](https://x.com/teortaxesTex/status/2052550093916475605) called it enough to validate the lab's architecture and methodology. Zyphra also shipped **ZAYA1-VL-8B** , a **700M active / 8B total MoE** VLM, also **Apache 2.0** , via [@ZyphraAI](https://x.com/ZyphraAI/status/2052890651835224454).

  * **Inference infrastructure remains a major competitive axis** : [SemiAnalysis](https://x.com/SemiAnalysis_/status/2052584396494958860) highlighted how quickly [vLLM](https://x.com/vllm_project/status/2052750374206083131) landed **DeepSeek V4** support, reinforcing the "**speed is the moat** " thesis for inference stacks. vLLM-Omni v0.20.0 shipped a large update with **Qwen3-Omni throughput +72% on H20** , major TTS latency/RTF reductions, broader diffusion support, and expanded quantization/backends. On the SGLang side, [@Yuchenj_UW](https://x.com/Yuchenj_UW/status/2052600316252876968) reported hearing numbers up to **57B tokens/day** on inference, while a long technical recap from [@ZhihuFrontier](https://x.com/ZhihuFrontier/status/2052768468249063482) detailed H20-specific DeepSeek optimization strategies across **prefill/decode disaggregation, FP8 FlashMLA, SBO, expert affinity, and observability**.

  * **Open models are increasingly "good enough" for coding and agent workloads**: [@masondrxy](https://x.com/masondrxy/status/2052781917955580246) said **Kimi K2.6 on Baseten** is about **5x cheaper than Opus 4.7** with roughly similar performance for many tasks, while [@caspar_br](https://x.com/caspar_br/status/2052817936344400132) reported swapping an internal Fleet model from **Sonnet 4.6 to Kimi K2.6** without noticing. That matches a broader shift noted by [@hwchase17](https://x.com/hwchase17/status/2052782958508175467) and [LangChain](https://x.com/LangChain/status/2052819061436973231): open-source LLMs are now viable default choices in many agentic stacks, especially as frontier inference pricing rises.




**Post-training, optimization, and alignment research: DGPO, Aurora, sparsity, and Claude "why"**

  * **Several notable optimization/post-training ideas landed at once** : [@TheTuringPost](https://x.com/TheTuringPost/status/2052539247320858975) summarized **DGPO (Distribution-Guided Policy Optimization)** as a refinement over GRPO that uses **token-level reward redistribution** , **Hellinger distance** instead of KL, and **entropy gating** to better reward useful exploration, reporting **46.0% on AIME 2025** and **60.0% on AIME 2024**. Separately, [@tilderesearch](https://x.com/tilderesearch/status/2052798181558370419) introduced **Aurora** , an optimizer designed to avoid a Muon-related neuron death failure mode; their **Aurora-1.1B** reportedly matches **Qwen3-1.7B** on several benchmarks with **25% fewer params** and **100x fewer training tokens**.

  * **Sparsity is back, but in hardware-friendly form** : [@SakanaAILabs](https://x.com/SakanaAILabs/status/2052787226136990029) and [@hardmaru](https://x.com/hardmaru/status/2052787980344099293) released **TwELL** , a sparse packing format and kernel stack for transformer FFNs that reportedly yields **20%+ training/inference speedups** on H100s by reshaping sparsity to fit GPU execution rather than forcing generic sparse formats. [@NVIDIAAI](https://x.com/NVIDIAAI/status/2052801759777874207) amplified the collaboration. In a different modularity direction, [@allen_ai](https://x.com/allen_ai/status/2052784995710681180) released **EMO** , an MoE trained so modular expert structure emerges from data, allowing selective expert use without hand-crafted priors.

  * **Anthropic published one of the day 's most important alignment threads**: In ["Teaching Claude why"](https://x.com/AnthropicAI/status/2052808787514228772), Anthropic said it has **eliminated the Claude 4 blackmail behavior** previously observed under certain conditions. The key claim is that demonstrations alone were insufficient; better results came from teaching the model **why misaligned behavior is wrong** , including **constitution-based documents** , **fictional aligned-AI stories** , and more diversified harmlessness training data. Supporting details came in follow-ups from [@AnthropicAI](https://x.com/AnthropicAI/status/2052808789297115628) and [the full post](https://x.com/AnthropicAI/status/2052808809182060581). This directly answered part of a transparency concern raised earlier by [@RyanPGreenblatt](https://x.com/RyanPGreenblatt/status/2052803011915980856) about the limited public understanding of what actually causes behavioral alignment.




**Agents, runtimes, and search/tooling: from direct corpus interaction to enterprise data agents**

  * **Agent architecture is shifting from "just call the model" to orchestration/harness design**: [@ii_posts](https://x.com/ii_posts/status/2052764819950907490) reported that long-running coding agents often fail by **stopping too early** , and that their **Zenith** orchestration harness won **5/8** long-horizon tasks at **43% of the strongest baseline 's cost**. This aligns with broader practitioner reports that journals, checkpoints, and runtime control matter as much as raw model quality--see [@vwxyzjn](https://x.com/vwxyzjn/status/2052779821202276761) on keeping an agent trial log, and [@nptacek](https://x.com/nptacek/status/2052742943321002366) for a vivid example of multi-agent memory conflicts and governance failure modes in a shared workspace.

  * **Search/retrieval is being rethought for agents** : [@zhuofengli96475](https://x.com/zhuofengli96475/status/2052784645398303198) introduced **Direct Corpus Interaction (DCI)** , replacing embedding model + vector DB + top-k retrieval with direct use of **grep/find/bash** over raw corpora. Reported gains include **BrowseComp-Plus 69% -> 80%** on Claude Sonnet 4.6 and broad wins across **13 benchmarks**. Complementing that, [@_reachsumit](https://x.com/_reachsumit/status/2052593078788411895) highlighted **OBLIQ-Bench** , a benchmark for retrievers on **oblique / implicit queries** , and [@turbopuffer](https://x.com/turbopuffer/status/2052759200078733590) shipped **sparse vectors as a first-class retrieval primitive** that can compose with BM25 and attribute ranking in a single query plan.

  * **Enterprise data agents are emerging as a distinct category from coding agents** : [@matei_zaharia](https://x.com/matei_zaharia/status/2052778748941046180) and [@DbrxMosaicAI](https://x.com/DbrxMosaicAI/status/2052781813651984468) detailed how **Databricks Genie** tackles the non-deterministic nature of data work--asset discovery, conflicting business context, and missing deterministic tests--using **specialized knowledge search, parallel thinking, and multi-LLM designs**. Reported accuracy improved from **32% to 90%+** , with [@Yuchenj_UW](https://x.com/Yuchenj_UW/status/2052784305735397863) citing **91.6%** on enterprise data analysis tasks.




**Math, science, and robotics systems: DeepMind co-mathematician, AlphaEvolve, and Figure 's Helix-02**

  * **DeepMind 's AI co-mathematician is the most consequential science result in the set**: [@pushmeet](https://x.com/pushmeet/status/2052812585804685322) announced a **multi-agent AI co-mathematician** that scored **48% on FrontierMath Tier 4** , a new high, and was tested by mathematicians across multiple subfields. The more important signal is qualitative: [@wtgowers](https://x.com/wtgowers/status/2052830952758382850) said the system proved a result that could plausibly form a **PhD thesis chapter** , while [@kimmonismus](https://x.com/kimmonismus/status/2052849472586264997) usefully noted the result relied on custom infrastructure and large budgets, so it is not directly comparable to standard leaderboard runs. Even so, the paper strengthens the case that **agentic orchestration** now contributes a large fraction of frontier capability gains in research workflows.

  * **Google continues to emphasize self-improving systems in production science/infra** : [@Google](https://x.com/Google/status/2052794893206962598) gave an update on **AlphaEvolve** , saying the Gemini-powered coding agent is being used for **Google AI infrastructure** , **molecular simulations** , and **natural disaster risk prediction**. A companion post from [Google Cloud](https://x.com/Google/status/2052794909355094217) claimed real-world impact including **doubling training speed for massive AI models** and routing optimizations that save **15,000 km of travel annually**.

  * **Robotics demos are getting closer to coordinated household competence** : [@adcock_brett](https://x.com/adcock_brett/status/2052770989944242335) shared Figure's latest demo of **two Helix-02 robots making a bed together fully autonomously** , with a follow-up linking the underlying system [here](https://x.com/adcock_brett/status/2052771762056974511). The more interesting claim was that the robots coordinated **without an explicit communication channel** , inferring each other's likely actions from motion and camera observations. In the broader physical-AI direction, [@DrJimFan](https://x.com/DrJimFan/status/2052758642781487237) published a dense "**Robotics: Endgame** " talk arguing for a roadmap built around **video world models, world action models, robot-data flywheels, and physical RL**.




**Top tweets (by engagement)**

  * **Anthropic alignment research** : ["Teaching Claude why"](https://x.com/AnthropicAI/status/2052808787514228772) was the highest-signal technical thread, claiming elimination of a previously observed blackmail behavior via training aimed at model understanding rather than demonstrations alone.

  * **OpenAI Codex product push** : [OpenAI's Codex post](https://x.com/OpenAI/status/2052800507727781979) and the broader `/goal` discussion around long-running work marked a meaningful step from assistant UX toward agent runtime UX.

  * **HTML as an agent interface layer** : [@trq212](https://x.com/trq212/status/2052811606032269638) arguing that "**HTML is the new markdown** " resonated unusually strongly, reflecting a broader shift toward agent-generated artifacts and custom interfaces.

  * **Figure 's household robotics demo**: [@adcock_brett](https://x.com/adcock_brett/status/2052770989944242335) on two Helix-02 robots making a bed was the standout robotics clip by engagement.

  * **DeepMind AI co-mathematician** : [@pushmeet](https://x.com/pushmeet/status/2052812585804685322) on the **48% FrontierMath Tier 4** result was the clearest science/reasoning milestone in the feed.




* * *

# **AI Reddit Recap**

## **/r/LocalLlama + /r/localLLM Recap**

### **1\. Multi-Token Prediction Local Inference**

[ Read more ](https://www.latent.space/p/ainews-anthropic-growing-10xyear)

---

## [[AINews] GPT-Realtime-2, -Translate, and -Whisper: new SOTA realtime voice APIs](https://www.latent.space/p/ainews-gpt-realtime-2-translate-and)
*🔬 Latent Space | 2026-05-08*

OpenAI launched [realtime-1.5](https://x.com/OpenAIDevs/status/2026014334787461508) 3 months ago, but it was a relative drop in the bucket because it was still 4o based intelligence (a +5% bump in Big Bench Audio). You could tell the sheer confidence in today's realtime-2 release (with a +15.2% bump in BBA), and it was [appropriately well received](https://x.com/OpenAI/status/2052438194625593804?s=20):

[](https://substackcdn.com/image/fetch/$s_!A0Wm!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F9c9ffc6c-3f36-4f23-a2c3-34d5e64955aa_1014x918.png)

As[ the blogpost](https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/) explains, 3 models are being released, which one might simplify to "voice-in, voice-out, and voice-to-voice":

[](https://substackcdn.com/image/fetch/$s_!YiiK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F81d9ff0f-63ea-4b44-85a9-7fcc0d659f75_1716x772.png)

The focus is less about "voice quality", and more on usability. **TLDR:**

  * **Preambles** : Developers can enable short phrases before a main response, like "let me check that" or "one moment while I look into it".

  * **Parallel tool calls and tool transparency** : The model can **call multiple tools** at once and make those actions audible with phrases like "checking your calendar" or "looking that up now," helping agents stay responsive while completing tasks.

  * **Stronger recovery behavior** : The model can recover more gracefully by saying things like "I'm having trouble with that right now," instead of failing or breaking.

  * **Longer context** : 32K -> 128K

  * **Stronger domain understanding** : The model better retains specialized terminology, proper nouns, healthcare terms, and other vocabulary

  * **More controllable tone and delivery** : The model can better adjust its tone--speaking calmly, empathetically, or upbeat, based on context

  * **Adjustable reasoning effort** : Developers can now select from **minimal, low, medium, high, and xhigh reasoning levels** , with low as the default.




The Demo video showed off how the audio model is better tuned when the main speaker is speaking to someone else, so it stops interrupting so much:

> AI News for 5/6/2026-5/7/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

# **AI Twitter Recap**

**Top Story: GPT-Realtime-2 and OpenAI voice AI commentary**

## **What happened**

**OpenAI launched three new streaming audio models in the Realtime API: GPT-Realtime-2, GPT-Realtime-Translate, and GPT-Realtime-Whisper.** OpenAI positioned GPT-Realtime-2 as its "most intelligent voice model yet," bringing "GPT-5-class reasoning" to real-time voice agents that can listen, reason, handle interruptions, use tools, and sustain longer conversations as they unfold [@OpenAI](https://x.com/OpenAI/status/2052438194625593804). The companion models target live speech translation and transcription: GPT-Realtime-Translate supports streaming translation from 70+ input languages into 13 output languages, while GPT-Realtime-Whisper streams transcription/captions as speech is produced [@OpenAI](https://x.com/OpenAI/status/2052438196454379986), [@OpenAIDevs](https://x.com/OpenAIDevs/status/2052440907933474954). OpenAI said the models are available in the Realtime API now, while ChatGPT voice upgrades are still pending: "Stay tuned, we're cooking" [@OpenAI](https://x.com/OpenAI/status/2052438197695877316). Sam Altman framed the launch around a behavioral shift: users increasingly use voice with AI when they need to "dump" lots of context, and OpenAI is also working on improvements to ChatGPT voice [@sama](https://x.com/sama/status/2052462271667028211).

## **Facts vs. opinions**

**Factual / directly claimed by OpenAI and evaluators**

  * **Model family:** GPT-Realtime-2, GPT-Realtime-Translate, GPT-Realtime-Whisper are available in the Realtime API today [@OpenAIDevs](https://x.com/OpenAIDevs/status/2052440968763515223).

  * **GPT-Realtime-2 capabilities:** reasoning-oriented native speech-to-speech model for production voice agents; supports tool use/action, interruption recovery, longer conversations, and "GPT-5-class reasoning" per OpenAI's wording [@OpenAI](https://x.com/OpenAI/status/2052438194625593804), [@reach_vb](https://x.com/reach_vb/status/2052438371058737280).

  * **Context window:** community/OpenAI-dev commentary reported **128K context** for GPT-Realtime-2 voice agents [@reach_vb](https://x.com/reach_vb/status/2052438371058737280); Artificial Analysis independently reported the context window increased from **32K to 128K** , with **32K max output tokens** [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2052486470469140777).

  * **Translation:** GPT-Realtime-Translate supports live speech translation from **70+ input languages** into **13 output languages** [@OpenAI](https://x.com/OpenAI/status/2052438196454379986), [@reach_vb](https://x.com/reach_vb/status/2052438371058737280).

  * **Transcription:** GPT-Realtime-Whisper provides low-latency streaming transcription in the Realtime API for captions, notes, and continuous speech understanding [@OpenAIDevs](https://x.com/OpenAIDevs/status/2052440957258489859).

  * **Prompting/control:** OpenAI published a voice prompting guide covering reasoning effort, preambles, tool behavior, unclear audio handling, exact entity capture, and state maintenance in long sessions [@OpenAIDevs](https://x.com/OpenAIDevs/status/2052530378184032560).

  * **Independent benchmarks:** Scale AI reported GPT-Realtime-2 took the top spot on its Audio MultiChallenge S2S leaderboard, with instruction retention rising from **36.7% to 70.8% APR** versus GPT-Realtime-1.5 and strong performance on voice editing/real-time repair [@ScaleAILabs](https://x.com/ScaleAILabs/status/2052451341071683732).

  * **Independent benchmarks:** Artificial Analysis reported **96.6%** on Big Bench Audio speech-to-speech reasoning, **96.1%** on its Conversational Dynamics benchmark, average time-to-first-audio of **2.33s** at high reasoning and **1.12s** at minimal reasoning, and unchanged audio pricing of **$1.15/hour input** and **$4.61/hour output** [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2052486470469140777), [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2052486478501204415).

  * **Reasoning-effort controls:** Artificial Analysis reported adjustable reasoning levels: **minimal, low, medium, high, xhigh** , with **low** as default [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2052486470469140777).

  * **Enterprise/product evals:** Glean said GPT-Realtime-2 delivered a **42.9% relative increase in helpfulness** over the previous version in internal evals for real-time organizational voice interactions [@glean](https://x.com/glean/status/2052440702169108990). Genspark said its Call for Me Agent moved to GPT-Realtime-2 and saw **+26% effective conversation rate** and fewer dropped calls [@genspark_ai](https://x.com/genspark_ai/status/2052524670088556557).




**Opinions / interpretation / commentary**

  * Supporters described the launch as a "big step forward" for voice agents [@sama](https://x.com/sama/status/2052462271667028211), "total realtime victory" [@reach_vb](https://x.com/reach_vb/status/2052442056392405383), and the first speech-to-speech model good enough for "real work" in complex voice agents [@kwindla](https://x.com/kwindla/status/2052521318688739811).

  * A more cautious view: Simon Willison noted the announcement does **not** mean ChatGPT Voice Mode itself has upgraded yet; the ChatGPT upgrade "sounds" like it is coming soon [@simonw](https://x.com/simonw/status/2052439091577496054), [@simonw](https://x.com/simonw/status/2052439181885153757).

  * Interface skepticism: Will Depue compared audio to VR--frequently exciting, but historically not sticky as an interface--while arguing that real-time tool use, reasoning while speaking, and live translation are the kinds of capabilities that could make audio interfaces finally take off [@willdepue](https://x.com/willdepue/status/2052493097586823353).

  * Broader UX optimism: several commenters framed voice as more natural and bandwidth-efficient for humans [@BorisMPower](https://x.com/BorisMPower/status/2052471142921994332), a path toward Jarvis-like always-available computer agents [@willdepue](https://x.com/willdepue/status/2052494388413235672), or eventually displaced by even higher-bandwidth BCIs [@iScienceLuvr](https://x.com/iScienceLuvr/status/2052465922640593068).

  * Competitive context: Elon Musk pushed Grok Voice for customer support [@elonmusk](https://x.com/elonmusk/status/2052530063913189879), underscoring that real-time voice support/customer-service automation is now a competitive surface across labs.




## **Technical details and benchmark data**

**GPT-Realtime-2**

  * Native speech-to-speech / real-time voice model, released via OpenAI's Realtime API [@OpenAI](https://x.com/OpenAI/status/2052438194625593804).

  * Framed as "GPT-5-class reasoning" for voice agents [@OpenAI](https://x.com/OpenAI/status/2052438194625593804).

  * Designed for agents that can:

    * reason mid-conversation,

    * use tools/take actions,

    * handle interruptions,

    * recover when users revise or repair speech,

    * sustain longer sessions with expanded context [@OpenAI](https://x.com/OpenAI/status/2052438196454379986), [@reach_vb](https://x.com/reach_vb/status/2052438371058737280).

  * Reported context: **128K tokens** , up from **32K** [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2052486470469140777).

  * Reported max output: **32K tokens** [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2052486470469140777).

  * Inputs reported by Artificial Analysis: **text, audio, and image** [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2052486470469140777).

  * Reasoning effort levels: **minimal, low, medium, high, xhigh** ; default **low** [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2052486470469140777).

  * Time-to-first-audio:

    * **1.12s** at minimal reasoning,

    * **2.33s** at high reasoning [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2052486470469140777).

  * Pricing:

    * **$1.15/hour audio input** ,

    * **$4.61/hour audio output** ,

    * unchanged versus prior model according to Artificial Analysis [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2052486478501204415).

  * Conversational features: supports short preambles before main responses--e.g. "let me check that"--and audible transparency during tool calls--e.g. "checking your calendar" [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2052486470469140777).




**Benchmarks**

  * **Scale AI Audio MultiChallenge S2S:** GPT-Realtime-2 placed #1; instruction retention improved from **36.7% to 70.8% APR** versus GPT-Realtime-1.5; strong voice editing when users repair/revise speech in real time [@ScaleAILabs](https://x.com/ScaleAILabs/status/2052451341071683732).

  * **Artificial Analysis Big Bench Audio:** GPT-Realtime-2 high variant scored **96.6%** , reported as equal to Gemini 3.1 Flash Live Preview High and about **~13%** above the previous highest result [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2052486470469140777).

  * Justin Uberti separately summarized the improvement as **15 percentage points vs. GPT-Realtime-1.5** on Big Bench Audio, near saturation [@juberti](https://x.com/juberti/status/2052507302092296252).

  * **Conversational Dynamics / Full Duplex Bench subset:** GPT-Realtime-2 minimal variant scored **96.1%** , with strengths in pause handling and turn-taking [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2052486470469140777).




**GPT-Realtime-Translate**

  * Live streaming speech translation from **70+ input languages** to **13 output languages** [@OpenAI](https://x.com/OpenAI/status/2052438196454379986).

  * OpenAI cofounder Greg Brockman said real-time voice-to-voice translation has been an anticipated OpenAI application since the company's early days and is now available for anyone to build with [@gdb](https://x.com/gdb/status/2052480998668206262).

  * Vimeo demonstrated live dubbing with no pre-loaded captions, showing translations generated fully live [@Vimeo](https://x.com/Vimeo/status/2052442588201029684).

  * Junling Zhang highlighted the new real-time translation model and encouraged API usage [@jxnlco](https://x.com/jxnlco/status/2052449634266812744).

  * Boris Power said live translation "actually works incredibly well" and plans to use it regularly [@BorisMPower](https://x.com/BorisMPower/status/2052472038967890022).




**GPT-Realtime-Whisper**

  * Streaming transcription as people speak, for real-time captions, notes, and speech understanding [@OpenAI](https://x.com/OpenAI/status/2052438196454379986).

  * Justin Uberti described it as "Whisper, but now with realtime streaming" and updated demos to use the new model [@juberti](https://x.com/juberti/status/2052478775523512356).

  * Uberti also built a delay selector to expose the latency/accuracy tradeoff in a real-time typing demo [@juberti](https://x.com/juberti/status/2052504986391879788).




## **Product integrations and demos**

  * **Glean:** shipped real-time voice powered by GPT-Realtime-2, grounded in organizational context; internal evals showed **42.9% relative helpfulness increase** over the previous version [@glean](https://x.com/glean/status/2052440702169108990).

  * **Vimeo:** demonstrated live dubbing using GPT-Realtime-Translate, with translations generated live and no pre-loaded captions [@Vimeo](https://x.com/Vimeo/status/2052442588201029684).

  * **Genspark:** upgraded its Call for Me Agent to GPT-Realtime-2; Genspark Realtime Voice is next; claimed sharper reasoning, tighter instruction following, **+26% effective conversation rate** , and fewer dropped calls [@genspark_ai](https://x.com/genspark_ai/status/2052524670088556557).

  * **Gradient Bang / game-agent demo:** Kyle Windland said GPT-Realtime-2 is the first OpenAI speech-to-speech model good enough for his voice agents that do "real work," showing it as the ship AI in a complex agent with tool calls and subagents [@kwindla](https://x.com/kwindla/status/2052521318688739811).

  * **Voice-controlled market dashboard:** Levin Stanley demoed GPT-Realtime-2 controlling an interface by intent--"Focus on Apple," "How did it do over the last 30 days?", "Go back"--arguing that real-time interruption and reasoning change the UI loop from navigation to direction [@levinstanley](https://x.com/levinstanley/status/2052506605044842672).

  * **Realtime demos:** Justin Uberti updated `hello-realtime` for GPT-Realtime-2 and provided a phone demo number [@juberti](https://x.com/juberti/status/2052469176821002676); Diego Cabezas posted a quick GPT-Realtime-2 demo [@diegocabezas01](https://x.com/diegocabezas01/status/2052492653082681485); Ray Fernando hosted a "Building a Live Translator" broadcast [@RayFernando1337](https://x.com/RayFernando1337/status/2052479718495318143).

  * **Reachy Mini / robotics voice interface interest:** Clement Delangue asked who would add the new voice capabilities to Reachy Mini [@ClementDelangue](https://x.com/ClementDelangue/status/2052449977725534363), after earlier asking voice AI labs such as Gradium, Kyutai, and ElevenLabs who could help with a robot voice use case [@ClementDelangue](https://x.com/ClementDelangue/status/2052385809655828907).




## **Why this matters**

The launch pushes voice agents from "speech I/O wrapper around a chatbot" toward **full-duplex, tool-using, long-context, reasoning agents**. The technical shift is not just better ASR or TTS; it is the combination of low-latency turn-taking, interruption handling, longer context, tool-call transparency, and adjustable reasoning effort in a single real-time loop. That matters for customer support, meetings, accessibility, live translation, robotics, browser/computer control, and hands-free workflows where text chat is too slow or awkward.

The most important engineering implication is that voice apps now need to be designed as **stateful real-time systems** , not prompt-response endpoints. OpenAI's prompting guide explicitly points developers toward reasoning-effort tuning, preambles, tool behavior, unclear-audio recovery, entity capture, and long-session state management [@OpenAIDevs](https://x.com/OpenAIDevs/status/2052530378184032560). This suggests voice-agent quality will increasingly depend on harness design: latency budgets, interruption semantics, tool-call UX, conversational memory, and failure recovery--not just raw model selection.

The remaining uncertainty is distribution. The API model is available now, but ChatGPT voice mode has not yet received the upgrade, per Simon Willison's observation [@simonw](https://x.com/simonw/status/2052439091577496054). If and when ChatGPT Voice gets the same capabilities, the consumer impact could be much larger. Until then, the launch primarily benefits developers and platforms building specialized real-time agents.

* * *

[ Read more ](https://www.latent.space/p/ainews-gpt-realtime-2-translate-and)

---

## [[AINews] Anthropic-SpaceXai's 300MW/$5B/yr deal for Colossus I, ARR growth is 8000% annualized](https://www.latent.space/p/ainews-anthropic-spacexais-300mw5byr)
*🔬 Latent Space | 2026-05-07*

It was Anthropic's [second annual developer event](https://www.youtube.com/watch?v=GMIWm5y90xA) today, and the vibes were [immaculate](https://x.com/latentspacepod/status/2052073451616383067?s=20). No big model release, which some (miscalibrated) people were hoping for, but it was mostly [the SpaceX partnership announcement](https://x.com/claudeai/status/2052060691893227611) (on track to challenge [Claude's biggest launch of all time](https://x.com/claudeai/status/2036195789601374705?s=20)), [3 new features for Claude Managed Agents](https://x.com/i/status/2052067399088664981), and a recap/reintroduction/celebration of all that has been shipped in the past 6 months:

[](https://substackcdn.com/image/fetch/$s_!yEoG!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd591a434-a112-4fb9-829a-30ff2e4efbf5_2260x1442.png)[opening keynote](https://www.youtube.com/watch?v=GMIWm5y90xA)

After [Elon signed off on it](https://x.com/paularambles/status/2052087138670596289?s=46), possibly [strategically](https://x.com/celestepoasts/status/2052108928788443428?s=12) just as his [lawsuit against OpenAI](https://x.com/seconds_0/status/2052067172558704787?s=12) is in trial, Anthropic is taking over all of Colossus 1 with surprising speed ("[in the next few days](https://x.com/nottombrown/status/2052062566126649448?s=46)") which [some estimate](https://x.com/jaminball/status/2052112307552211195?s=46) to be a [roughly](https://x.com/andrewbenson/status/2052147078902718583?s=46) **$5B/year deal** , making [xAI a neocloud](https://x.com/krishnanrohit/status/2052084600877527332?s=46):

[](https://substackcdn.com/image/fetch/$s_!oqVU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1a49129f-2c6b-4bd5-bcbb-aa397b627218_1072x1064.png)

The other big draw was the moderated session with the Amodei siblings, announcing [the 80x growth](https://x.com/firstadopter/status/2052118224888607107) and some commentary on [US and Chinese competitors](https://x.com/jukan05/status/2051847480254570998?s=12):

[](https://substackcdn.com/image/fetch/$s_!Kb-H!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd1acd7ed-b0f8-4448-ac16-0dc71920093e_1354x872.png)

The trends Dario is watching:

  * **[Tiny Teams](https://www.latent.space/p/tiny)** : He still thinks 2026 is the year we see a one person billion dollar company. "_There is an enormous ability for one person or a tiny set of people to do a set of things that are incredible … Before, if you had an idea or vision there are so many resources you'd have to accumulate for several years in order to make that vision happen, and I think **there 's a unique opportunity for single individuals or very tiny teams** to do things that are incredible, where we move from the models are writing code, to the models are helping us think of software engineering as a task, to the models are helping us think of how can I build a business or economic unit as a task"._

  * **[Multiagents](https://www.latent.space/p/scaling-test-time-compute-to-multi?utm_source=publication-search)** : "starting with a team of smart people in a room and working our way up to a 'country of geniuses in a datacenter'"

  * **[Enterprise Services](https://www.latent.space/p/ainews-silicon-valley-gets-serious): **"Claude Code helps individuals to be more productive, but we're increasingly going to help whole teams and organizations be more productive and more than the sum of its parts".

  * **Bottlenecks:** Claude is of course speeding up Claude, but he thinks about [Amdahl's Law](https://en.wikipedia.org/wiki/Amdahl%27s_law) \- Security, Verifiability - finding the bottlenecks in software engineering and removing them/speeding up the overall process.




The [rest of the mainstage sessions](https://x.com/i/broadcasts/1qGoNegbnRNKv) included:

Must know Claude Code updates:

[](https://substackcdn.com/image/fetch/$s_!xgsP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F410c6b30-1820-4dd4-b5b7-5bcaeb548a03_1790x990.png)

More Outcomes content on the Inner vs the Outer Loop…

[](https://substackcdn.com/image/fetch/$s_!R0rc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8dee8da9-3dac-4336-a837-a7702e57f859_1354x840.png)

… for automatic improvement of agents:

[](https://substackcdn.com/image/fetch/$s_!mUFo!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F339addf2-fd81-4049-8f51-9042943b2fe5_1358x846.png)

> AI News for 5/5/2026-5/6/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

# **AI Twitter Recap**

### **Top Story: Anthropic and Claude announcements/commentary**

**Anthropic had a dense news cycle centered on compute, Claude Code limits, and agent platform direction.**

  * Officially, Anthropic announced a new compute partnership with SpaceX that will "substantially increase" capacity and immediately translate into higher limits for Claude products: [@claudeai](https://x.com/claudeai/status/2052060691893227611) said the deal boosts compute enough to raise usage limits, followed by specifics from [@claudeai](https://x.com/claudeai/status/2052060693269008586): **Claude Code 's 5-hour rate limits are doubled for Pro, Max, Team, and seat-based Enterprise; peak-hours limit reductions are removed for Pro and Max; Opus API rate limits are substantially increased**. 

  * xAI framed the deal as Anthropic getting access to **Colossus 1** via SpaceXAI for "additional capacity for Claude" [@xai](https://x.com/xai/status/2052060350770515978), while Anthropic CTO Tom Brown added that **Claude inference would be ramped up on Colossus "in the next few days"** [@nottombrown](https://x.com/nottombrown/status/2052062566126649448). 

  * The company also ran its **" Code with Claude"** event, with a livestreamed keynote and sessions on Claude Code, GitHub-scale usage, and managed agents [@ClaudeDevs](https://x.com/ClaudeDevs/status/2052055459272761661), prompting substantial real-time commentary from developers and observers [@simonw](https://x.com/simonw/status/2052055655230706032), [@latentspacepod](https://x.com/latentspacepod/status/2052062150332710942). 

  * Around this, discourse branched into four themes: 

    * **(1) compute bottlenecks were more severe than many assumed, reportedly due to unexpected usage growth;**

    * **(2) users welcomed the 5-hour limit increase but questioned unchanged weekly limits;**

    * **(3) people debated whether Anthropic 's new managed-agent features like memory/"Dreaming" and rubrics/"Outcomes" are real product differentiation or commoditizable harness features; and **

    * **(4) Anthropic 's safety/governance positioning continued to attract both praise and criticism**, including claims from critics that some Anthropic employees project "only we can be trusted with AGI," and counterclaims from Anthropic-adjacent voices that the more common internal view is closer to "no one can be trusted with AGI" than "only us" [@](https://x.com/_aidan_clark_/status/2052089187659346047)_[aidan_clark](https://x.com/_aidan_clark_/status/2052089187659346047)_ , [@kipperrii](https://x.com/kipperrii/status/2052094851991392536).




## **Official facts and confirmed details**

  * Anthropic announced a **SpaceX compute partnership** to increase capacity [@claudeai](https://x.com/claudeai/status/2052060691893227611).

  * Effective immediately, Anthropic says it is:

    1. **Doubling Claude Code 's 5-hour rate limits** for Pro, Max, Team, and seat-based Enterprise

    2. **Removing peak-hours limit reduction** on Claude Code for Pro and Max

    3. **Substantially increasing API rate limits for Opus models**  
Source: [@claudeai](https://x.com/claudeai/status/2052060693269008586)

  * Anthropic linked an official explainer on the higher usage limits and the SpaceX compute deal [@claudeai](https://x.com/claudeai/status/2052060696255283346).

  * xAI's announcement described the arrangement as **SpaceXAI providing Anthropic access to Colossus 1** for additional Claude capacity [@xai](https://x.com/xai/status/2052060350770515978).

  * Anthropic CTO Tom Brown said **Claude inference would start ramping on Colossus within days** [@nottombrown](https://x.com/nottombrown/status/2052062566126649448).

  * Anthropic product/eng lead Amol Avasare clarified that **weekly limits were not increased yet** because only a **small percentage** of users hit weekly limits, while a much larger percentage hit 5-hour limits; more changes may come as compute lands [@TheAmolAvasare](https://x.com/TheAmolAvasare/status/2052064611692904639), [@TheAmolAvasare](https://x.com/TheAmolAvasare/status/2052066157176426653).

  * Anthropic/Claude held a **Code with Claude** event with sessions including keynote, Claude Code updates, GitHub-scale usage, and managed agents [@ClaudeDevs](https://x.com/ClaudeDevs/status/2052055459272761661).

  * Anthropic's Alex Albert promoted the event and later summarized the announcement as **" More chips, more Claude"** [@alexalbert__](https://x.com/alexalbert__/status/2052067009605861764), [@alexalbert__](https://x.com/alexalbert__/status/2052065953173872912).

  * The dedicated Claude Code account reiterated the limit increase for Pro/Max/Team [@claude_code](https://x.com/claude_code/status/2052071730190123094).




## **Compute details and scale claims**

Several tweets added quantitative claims about the scale of the SpaceX/xAI arrangement. These are **not from Anthropic 's main announcement tweets**, but they were widely circulated:

  * [@](https://x.com/_arohan_/status/2052065871552819647)_[arohan](https://x.com/_arohan_/status/2052065871552819647)_ cited **" more than 300 megawatts of new capacity" and "over 220,000 NVIDIA GPUs within the month."**

  * [@scaling01](https://x.com/scaling01/status/2052068218047545501) claimed Colossus 1 includes **~150,000 H100s, 50,000 H200s, and 30,000 GB200s**.

  * [@Yuchenj_UW](https://x.com/Yuchenj_UW/status/2052065017072386450) repeated the **220,000 GPU** figure and added an unverified claim that Anthropic had committed **$200B on Google TPUs**.

  * [@eliebakouch](https://x.com/eliebakouch/status/2052066609896808473) interpreted the deal as Anthropic getting effectively **all of Colossus 1 capacity** , not just idle GPUs.

  * Elon Musk later said SpaceXAI was comfortable leasing Colossus 1 because **xAI had already moved training to Colossus 2** [@elonmusk](https://x.com/elonmusk/status/2052069691372478511), and [@eliebakouch](https://x.com/eliebakouch/status/2052068426152132722) claimed Colossus 2 is already at **~500k Blackwells**.




These numbers are best treated as **partly official-adjacent but not fully canonized in Anthropic 's own announcement thread**. The broad factual takeaway is stronger than the exact inventory breakdown: **Anthropic secured a very large, near-term external inference capacity expansion.**

## **Evidence the bottleneck was real**

A recurring interpretation was that Anthropic's constraint had genuinely been compute, not merely pricing or product design.

  * [@kimmonismus](https://x.com/kimmonismus/status/2052059082886910251) asked during/after the livestream whether Anthropic was **doubling Claude Code rate limits at no extra charge**.

  * [@kimmonismus](https://x.com/kimmonismus/status/2052118418174681572) later summarized remarks from a Dario/Daniela interview: **usage grew ~80x unexpectedly** , which purportedly caused the compute shortage, and the SpaceX deal is the first major attempt to address it.

  * [@czajkadev](https://x.com/czajkadev/status/2052101699188248990) explicitly interpreted the update as proof that **compute was the bottleneck**.

  * [@theo](https://x.com/theo/status/2052114791045668894) separately argued the industry problems are "not just money, it's about compute," which fits the Anthropic story even though it's a broader point.

  * [@scaling01](https://x.com/scaling01/status/2052069341609226550) generalized from this deal to a macro thesis: **frontier labs are compute constrained enough to rent datacenters from competitors.**




This is one of the strongest factual/market signals in the dataset: **Anthropic 's user-facing rate limits moved materially only after a major compute deal.**

## **Product implications: Claude Code, API, and managed agents**

Anthropic's practical user impact is clear:

  * **Claude Code power users get more usable burst capacity** over a 5-hour window.

  * **Peak-time throttling is eased** for Pro/Max.

  * **Opus API users get higher rate limits** , which matters for agent workloads and production integrations.




The event also highlighted Anthropic's broader platform ambitions around agents. While the primary official tweets here are mostly about the event itself, commentary points to features such as:

  * **Dreaming** = memory / cross-session context

  * **Outcomes** = rubrics / grading / objective tracking

  * **agent orchestration** / managed agents direction




Commentary:

  * [@RichNwan](https://x.com/RichNwan/status/2052085746526216601) argued Anthropic is "building out their managed agents platform" with **Dreaming** and **Outcomes** , but questioned whether these are meaningfully differentiated versus open harnesses.

  * [@eliebakouch](https://x.com/eliebakouch/status/2052156107313807690) saw these as **important for power users** , especially for preserving the main agent's context window and using separate graders to manage quality/safety/reward hacking.

  * [@latentspacepod](https://x.com/latentspacepod/status/2052068066167816369) quoted Anthropic speakers emphasizing **verification** , "routines are higher-order prompts," and the idea that the remaining gap is often **deployment/operationalization** , not raw capability.




That last point aligns Anthropic with the broader shift from "one-shot chatbot" to **structured agent systems with memory, decomposition, grading, and verification**.

### 

## **Different opinions in the discourse**

### **1) Positive / supportive**

A large set of replies treated this as a win for users and evidence Anthropic is responding aggressively.

  * [@alexalbert__](https://x.com/alexalbert__/status/2052065953173872912): "More chips, more Claude."

  * [@_sholtodouglas](https://x.com/_sholtodouglas/status/2052062164467224971): "More compute -> straight to you."

  * [@kimmonismus](https://x.com/kimmonismus/status/2052059448261177367) highlighted doubled limits and raised Opus API caps.

  * [@TheRundownAI](https://x.com/TheRundownAI/status/2052064469371470218) summarized it as a straightforward user benefit.

  * [@DannyLimanseta](https://x.com/DannyLimanseta/status/2052078750893056420) liked the cross-company cooperation and hoped Anthropic's caution might be balanced by SpaceXAI's optimism.

  * [@AmandaAskell](https://x.com/AmandaAskell/status/2052161052058833181) reacted positively to the announcement's symbolism.




### **2) Mixed / pragmatic**

These takes welcomed the change but focused on operational details and remaining limitations.

  * [@btibor91](https://x.com/btibor91/status/2052067002412335435) and [@kimmonismus](https://x.com/kimmonismus/status/2052061694080188720) immediately noted the likely caveat: **weekly caps unchanged**.

  * [@TheAmolAvasare](https://x.com/TheAmolAvasare/status/2052064611692904639) answered this directly.

  * [@sbmaruf](https://x.com/sbmaruf/status/2052119971820658771) reported still seeing rate limits after the change, implying rollout and reliability tuning were ongoing.

  * [@zachtratar](https://x.com/zachtratar/status/2052161984968396819) asked for patience during staged rollout.




### **3) Competitive / strategic critique**

A different cluster viewed the announcement through the OpenAI-vs-Anthropic product war.

  * [@scaling01](https://x.com/scaling01/status/2052070594972090409) argued Anthropic **blundered its growth advantage by waiting too long** , possibly conceding billions in ARR to OpenAI.

  * [@Yuchenj_UW](https://x.com/Yuchenj_UW/status/2052065017072386450) read the move as Dario getting aggressive because of **OpenAI Codex 's growth**.

  * [@](https://x.com/_arohan_/status/2052053181656641735)_[arohan](https://x.com/_arohan_/status/2052053181656641735)_ joked that "Big tech has become a claude wrapper," pointing to Claude's developer mindshare.

  * [@dejavucoder](https://x.com/dejavucoder/status/2052051193376231845) saying "claude is down, saint tibo please reset codex limits" captured the practical reality of multi-homing among coding tools when one service is capacity constrained.




### **4) Governance / safety / culture critique**

This is the deepest philosophical disagreement.

  * [@](https://x.com/_aidan_clark_/status/2052089187659346047)_[aidan_clark](https://x.com/_aidan_clark_/status/2052089187659346047)_ criticized what he says he repeatedly hears from Anthropic colleagues: a belief they alone should be trusted to build AI.

  * [@kipperrii](https://x.com/kipperrii/status/2052094851991392536) partially agreed the "only we can be trusted" framing would be bad, but argued the real majority view is closer to **" no one can be trusted with AGI"** while still personally trusting Anthropic more than others.

  * [@elonmusk](https://x.com/elonmusk/status/2052069691372478511) offered a surprising endorsement after meeting Anthropic leaders.

  * [@Yuchenj_UW](https://x.com/Yuchenj_UW/status/2052080339364004317) called this reversal ironic given prior criticism of Anthropic.

  * [@teortaxesTex](https://x.com/teortaxesTex/status/2052080900280557749) mocked the rapid detente between Musk/xAI and Anthropic.

  * [@teortaxesTex](https://x.com/teortaxesTex/status/2052045988936683674) also argued it is inconsistent to warn others about AI risk while building powerful closed systems such as "Mythos."

  * [@goodside](https://x.com/goodside/status/2052077014346064372), while not directly about Anthropic governance, contributed to the broader moral/AI norms debate that often clusters around Anthropic.




## **Commentary on Claude model performance and comparisons**

Though no major new Claude model appears in these tweets, Claude remained a reference point in product and eval discourse.

  * [@giffmana](https://x.com/giffmana/status/2051925008457273527) compared "Opus 4.6," ChatGPT Pro, and Muse Spark on a mathematical disagreement. His take:

    * **Opus 4.6** confidently defended a wrong proof ("gaslit")

    * **ChatGPT Pro** reconciled the formulas correctly but without interpretation

    * **Muse Spark** did both well  
This is anecdotal, but it's one of the more concrete comparative qualitative model reports in the set.

  * [@kimmonismus](https://x.com/kimmonismus/status/2052040471829004627) summarized a Substack analysis claiming **GPT-5.5 is basically tied with Claude Mythos Preview on cyber** , perhaps more cost-efficient, while Mythos is only slightly ahead on some general benchmarks and SWE-bench Pro; he questioned why Mythos remains secretive.

  * [@AssemblyAI](https://x.com/AssemblyAI/status/2052043337751056733) noted support for **structured JSON from Claude 4.5+ models** in its gateway.

  * [@OpenRouter/TencentHunyuan](https://x.com/TencentHunyuan/status/2051978552900538403) listed **Claude Code** among major apps driving Hy3 usage, showing Claude's importance in the coding-tool ecosystem even when third-party models are used behind the scenes.




These comments don't establish hard model ranking, but they do show Claude is still a primary benchmark in coding-agent workflows and that advanced users increasingly compare **model + harness + limits + reliability** , not just base intelligence.

## **Claude Code and harness engineering context**

A notable background thread across the dataset is that many engineers now think **agent performance is heavily dependent on the harness** --system prompts, tools, middleware, decomposition strategies, and model-specific tuning.

Relevant non-Anthropic commentary:

  * [@masondrxy](https://x.com/masondrxy/status/2052054177749029164): same model, same task, very different scores depending on prompts/tools/middleware; **10 -20 point jumps on tau2-bench**.

  * [@LangChain](https://x.com/LangChain/status/2052054711440662864): harness profiles for OpenAI, Anthropic, and Google models.

  * [@jakebroekhuizen](https://x.com/jakebroekhuizen/status/2052058987580051566): distinguishes **temporal harness evolution** as models improve from **lateral tuning across model families**.

  * [@Vtrivedy10](https://x.com/Vtrivedy10/status/2052100726608781363): argues a tailored harness can outperform default Codex/Claude Code on many tasks; usable context windows are still effectively **50 -100k** for many agent designs.

  * [@kieranklaassen](https://x.com/kieranklaassen/status/2052092428438688027): "If you cannot get your work done [in] the Claude CLI, Claude will not be able to work for you."




This matters because some of Anthropic's platform moves--memory, grading, managed agents--can be read as **Anthropic productizing parts of the harness**. That helps explain the central debate: **are these defensible platform primitives, or just first-party packaging of patterns that open frameworks can clone?**

## **Broader context: why this matters**

  1. **Inference, not just training, is now a frontier bottleneck.**  
The news was not a new model launch; it was a capacity launch. That is increasingly common at the frontier.

  2. **Compute markets are becoming fluid and strategic.**  
Anthropic partnering with SpaceX/xAI infrastructure undercuts simplistic narratives that each frontier lab sits only atop its own vertically integrated stack.

  3. **Developer product share is sensitive to reliability and limits.**  
Claude appears to have strong developer affinity, but rate limits and outages push users toward Codex/Cursor/others quickly.

  4. **The battleground is shifting from base models to agent systems.**  
"Code with Claude," managed agents, Dreaming, Outcomes, and the surrounding discourse all point toward the next layer of competition being **memory, orchestration, evals, and workflow integration**.

  5. **Anthropic 's brand remains bifurcated.**  
It is simultaneously:

     * admired for product quality and safety seriousness,

     * criticized for paternalism or perceived exclusivism,

     * and now seen as more commercially aggressive on compute than before.




## **Bottom line**

Anthropic's news was less about a flashy new model and more about a structural reality: **Claude demand had outrun available compute, and Anthropic responded by striking a major external infrastructure deal and immediately easing key user limits** [@claudeai](https://x.com/claudeai/status/2052060691893227611), [@claudeai](https://x.com/claudeai/status/2052060693269008586). The most important technical/economic signal is that **capacity, rate limits, and agent-product ergonomics are now as strategically important as leaderboard deltas**. The main open questions are whether Anthropic can convert this capacity into sustained product momentum, whether its managed-agent features are truly differentiated, and whether its safety/governance posture helps or hinders its standing as competition with OpenAI, Google, xAI, and open-model ecosystems intensifies.

* * *

### **Infrastructure, inference, and systems**

  * OpenAI and partners released **MRC (Multipath Reliable Connection)** , an open networking protocol for large AI training clusters, already deployed on OpenAI's biggest supercomputers [@OpenAI](https://x.com/OpenAI/status/2052025532485902368), [@OpenAI](https://x.com/OpenAI/status/2052025533937103102). Commentary emphasized multipath routing, microsecond failover, and the shift of networking into a primary frontier bottleneck [@kimmonismus](https://x.com/kimmonismus/status/2052011784023028060), [@gdb](https://x.com/gdb/status/2052059553542328829).

  * Perplexity said it built an in-house inference engine, **ROSE** , covering models from embeddings to trillion-parameter LLMs, and uses **CuTeDSL** to accelerate specialized kernel development on Hopper and Blackwell [@perplexity_ai](https://x.com/perplexity_ai/status/2052041903970148647).

  * vLLM + Mooncake presented a strong systems result for agentic workloads with reusable prefixes: **3.8x throughput** , **46x lower P50 TTFT** , **8.6x lower end-to-end latency** , and cache-hit improvement from **1.7% to 92.2%** , scaling to **60 GB200 GPUs** [@vllm_project](https://x.com/vllm_project/status/2052113331927060840).

  * Unsloth + NVIDIA published three training optimizations claimed to make home-GPU LLM training **~25% faster** : packed-sequence metadata caching, double-buffered checkpoint reloads, and faster MoE routing [@UnslothAI](https://x.com/UnslothAI/status/2052020656527532276).

  * NVIDIA work on **lossless speculative decoding inside RL** was highlighted as giving up to **~2.5x faster end-to-end RL at 235B scale** and **~1.8x faster rollout throughput at 8B** without changing policy distribution [@TheTuringPost](https://x.com/TheTuringPost/status/2052180472206381268).

  * Baseten launched **Frontier Gateway** as managed infra/API/auth/rate-limit/billing for closed-weight labs; Poolside reported going from kickoff to production in **7 weeks** , with **P50 TTFT 146ms** for Laguna XS.2 and **605ms** for Laguna M.1 [@tuhinone](https://x.com/tuhinone/status/2052082677432390130), [@poolsideai](https://x.com/poolsideai/status/2052075055132057707).




### **Benchmarks, evals, and agent harnesses**

  * **ProgramBench** asks whether language models can rebuild programs from scratch, extending beyond repair-style SWE tasks [@ComputerPapers](https://x.com/ComputerPapers/status/2051895799043215415), with Ofir Press arguing benchmarks are "treasure maps" that specify the future we want [@OfirPress](https://x.com/OfirPress/status/2052106927908200957).

  * **Terminal-Bench 2.1** patched **28/89 tasks** in TB2.0; rankings held but absolute scores moved by up to **12 points** , a useful reminder that agent benchmark maintenance materially matters [@terminalbench](https://x.com/terminalbench/status/2052119174500220964), [@ekellbuch](https://x.com/ekellbuch/status/2052165464655298866).

  * **OBLIQ-Bench** emerged as a major IR benchmark release focused on hard first-stage retrieval, where current retrievers fail to surface subtly relevant documents from large corpora [@dianetc_](https://x.com/dianetc_/status/2052053806121140254), with strong endorsements from IR researchers [@lateinteraction](https://x.com/lateinteraction/status/2052055143038713875), [@nlp_mit](https://x.com/nlp_mit/status/2052069072607547892), [@LightOnIO](https://x.com/LightOnIO/status/2052095548098822477).

  * Harvey launched **LAB** , an open-source, long-horizon legal agent benchmark covering **1,200 tasks across 24 practice areas** , with support/commentary from LangChain, Baseten, Artificial Analysis, and others [@saranormous](https://x.com/saranormous/status/2052061665596948894), [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2052145762650431840).

  * A major theme across multiple tweets was that **harness engineering is a first-class variable** , often worth **10 -20 points** on agent benchmarks even with the same base model [@masondrxy](https://x.com/masondrxy/status/2052054177749029164), [@LangChain](https://x.com/LangChain/status/2052054711440662864), [@Vtrivedy10](https://x.com/Vtrivedy10/status/2052100726608781363).




### **Model releases and model performance**

  * Zyphra released **ZAYA1-8B** , a reasoning MoE with **< 1B active parameters**, open-weight under **Apache 2.0** , claiming strong math/reasoning efficiency and proximity to much larger systems with test-time compute [@ZyphraAI](https://x.com/ZyphraAI/status/2052103618145501459), [@ZyphraAI](https://x.com/ZyphraAI/status/2052103646712828119). Commentary praised its architecture/post-training stack and AMD partnership [@teortaxesTex](https://x.com/teortaxesTex/status/2052106600882528326), [@eliebakouch](https://x.com/eliebakouch/status/2052126118891729148).

  * Google's **Gemma 4** moved the open-model Pareto frontier in Code Arena: **Gemma-4-31B #13** , **Gemma-4-26B-A4B #17** among open models [@arena](https://x.com/arena/status/2052061349312921686), [@_philschmid](https://x.com/_philschmid/status/2052104144706588699).

  * Google's **DFlash draft model for Gemma-4** was described as one of the best draft models they've trained, especially strong in coding and math [@jianchen1799](https://x.com/jianchen1799/status/2051902953376923946).

  * Qwopus3.6-35B-A3B-v1 claimed **162 tok/s on a single RTX 5090** , targeting strong one-shot frontend/web generation on consumer hardware [@KyleHessling1](https://x.com/KyleHessling1/status/2052064943999267212).

  * DeepSeek commentary was mixed: fundraising talks reportedly target a **$45B valuation** led by a major Chinese state-backed semiconductor fund [@jukan05](https://x.com/jukan05/status/2051904572038455634), while evaluators debated weak WeirdML performance for V4-Pro versus GLM/Kimi/open competitors [@htihle](https://x.com/htihle/status/2052042076196335658), [@teortaxesTex](https://x.com/teortaxesTex/status/2052043753892761882).




### **Agents, tools, and developer workflows**

  * Cursor added **context usage breakdowns** across rules, skills, MCPs, and subagents to help debug context issues [@cursor_ai](https://x.com/cursor_ai/status/2052059748544249918), and described bootstrapping future Composer generations with earlier Composer models [@cursor_ai](https://x.com/cursor_ai/status/2052116064474161556).

  * Cognition shipped **Devin Review** and **Quick Review / SWE-Check** in Windsurf 2.0, explicitly targeting the new bottleneck of reviewing AI-generated code [@cognition](https://x.com/cognition/status/2052100630626607189), [@ypatil125](https://x.com/ypatil125/status/2052122827961278833).

  * OpenAI promoted **Codex subagents** , framing them as a way to split work across specialized agents and merge results back into one answer [@reach_vb](https://x.com/reach_vb/status/2052090279344120278).

  * Nous/Hermes continued to push a highly pluggable local agent stack: plugin expansion, community docs, Windows/WSL2 setup guidance, and use-case aggregation [@Teknium](https://x.com/Teknium/status/2052046335583625629), [@witcheer](https://x.com/witcheer/status/2052033039379673374), [@NousResearch](https://x.com/NousResearch/status/2052140057222369541).

  * Perplexity added **Finance Search** to its Agent API with licensed data, live market data, and citations, claiming best cohort accuracy and lowest cost per correct answer on **FinSearchComp T1** [@perplexity_ai](https://x.com/perplexity_ai/status/2052028012313649194), [@AravSrinivas](https://x.com/AravSrinivas/status/2052033959555735752).

  * Google's Gemini API added **multimodal retrieval** to File Search using `gemini-embedding-2` for PDFs and images in a single retrieval pipeline [@_philschmid](https://x.com/_philschmid/status/2052060912425546050).




### **Robotics, multimodality, and research notes**

  * Genesis AI introduced **GENE-26.5** , describing a full-stack robotics program with a robotics-native foundation model, human-like hand, data glove, and simulator; the model is trained across **language, vision, proprioception, tactile, and action** [@gs_ai_](https://x.com/gs_ai_/status/2052050956272230577), [@theo_gervet](https://x.com/theo_gervet/status/2052057035681018359).

  * Meta FAIR released **NeuralBench** , an MIT-licensed unified benchmark framework for NeuroAI with **36 EEG tasks** and **94 datasets** , with MEG/fMRI support planned [@hubertjbanville](https://x.com/hubertjbanville/status/2052029372282888234), [@JeanRemiKing](https://x.com/JeanRemiKing/status/2052034314120896582).

  * Sander Dieleman published a long technical post on **flow maps** , learning the integral of a diffusion model for faster sampling and related tricks [@sedielem](https://x.com/sedielem/status/2051957402556104799).

  * François Fleuret sketched a speculative recipe for stronger systems: **latent diffusion-like reasoning + real recurrent state + world-model pre-pretraining** [@francoisfleuret](https://x.com/francoisfleuret/status/2051928896027693479), generating useful discussion on whether diffusion-style reasoning extrapolates the right way [@willdepue](https://x.com/willdepue/status/2052033422915477580), [@jeremyphoward](https://x.com/jeremyphoward/status/2052149483740545400).

  * HeadVis was introduced as a new interpretability tool for studying attention heads [@kamath_harish](https://x.com/kamath_harish/status/2052046203030827088).

  * Microsoft Research work on **agent-readable interpretability** proposed "Agentic-imodels," where coding agents evolve models that are interpretable to other LLMs; reported gains on **65 tabular datasets** and downstream BLADE improvements from **8% to 73%** [@dair_ai](https://x.com/dair_ai/status/2052125514266190286).




* * *

# **AI Reddit Recap**

## **/r/LocalLlama + /r/localLLM Recap**

[ Read more ](https://www.latent.space/p/ainews-anthropic-spacexais-300mw5byr)

---

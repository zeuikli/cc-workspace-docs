# 🔬 Latent Space — 2026-06-01

> swyx 開發者簡報，未公開專案 + 工程視角
> 來源：[Latent Space](https://www.latent.space/feed)

---

## [[AINews] Founders and Forward Deployed Engineers](https://www.latent.space/p/ainews-founders-and-forward-deployed)
*🔬 Latent Space | 2026-05-30*

Most people are still digesting the [massive Anthropic news](https://www.latent.space/p/ainews-anthropic-raises-965b-series) from yesterday. 

We're taking the opportunity to solicit [the leading AI FDE's](https://ai.engineer/cfp) in the world for AIE's new Forward Deployed Engineer track, mirroring similar pushes from both [OpenAI DeployCo](https://www.latent.space/p/ainews-thinking-machines-native-interaction) and [Anthropic DeployCo](https://www.blackstone.com/news/press/anthropic-partners-with-blackstone-hellman-friedman-and-goldman-sachs-to-launch-enterprise-ai-services-firm/):

[](https://substackcdn.com/image/fetch/$s_!SpLP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb92541e3-151a-4f10-8226-b86cb12eaca0_2332x1344.png)

as well as AIE's new Founders program, where we are doing our version of the Startup Battlefield, a competitive pitch contest anchored by YCombinator's Garry Tan and Howie Lu's [$10 Million dollar Hyperagent ](https://x.com/howietl/status/2057823823526014990)contest. Sign up (and [book hotel](https://www.ai.engineer/worldsfair/2026#venue)!) for details today if you are keen.

[](https://substackcdn.com/image/fetch/$s_!pbtj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faa6ef076-049b-4bd8-b183-4a49f1a913f8_2276x1306.png)

> AI News for 5/28/2026-5/29/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

# **AI Twitter Recap**

**Claude Opus 4.8 Rollout, Benchmark Friction, and API Ergonomics**

  * **Opus 4.8 landed into a noisy, mixed eval landscape** : multiple independent benches converged on "incremental but not dominant." [@arena](https://x.com/arena/status/2060160804767584512) pushed **200+ frontend/code tests** comparing Opus 4.8 against prior Opus variants, Gemini, and GLM; [@theo](https://x.com/theo/status/2060172445592789064) reported CursorBench shows it as **more efficient but slightly worse than 4.7 within margin of error** ; [@jerryjliu0](https://x.com/jerryjliu0/status/2060196252642648427) and [@llama_index](https://x.com/llama_index/status/2060165358569337102) found **small gains on tables/layout** but regressions on **content faithfulness/charts** in document parsing; [@scaling01](https://x.com/scaling01/status/2060335738172911766) said **no progress on ALE-Bench** and separately flagged interesting failure modes on LisanBench. On the positive side, [@jeremyphoward](https://x.com/jeremyphoward/status/2060195641847107722) found 4.8 **less over-agentic and more cooperative** than 4.7/GPT-5.5 in coding, while [@leo_linsky](https://x.com/leo_linsky/status/2060205310871326894) called it a tangible product improvement over prior Anthropic releases.

  * **Anthropic also shipped useful platform-level changes** : [@ClaudeDevs](https://x.com/ClaudeDevs/status/2060432688281251998) announced **mid-conversation system instructions without breaking prompt cache** , plus authoritative mid-conversation system-role updates, which matters for long-running agent sessions and cost control. But pricing remains a major complaint: [@jeremyphoward](https://x.com/jeremyphoward/status/2060198836963061998) argued Anthropic has done little for **API affordability** , preferring GPT-5.5 partly because subscription/API economics are easier to justify. Overall takeaway: 4.8 looks like a meaningful quality-of-life release for real use, not a clean benchmark reset.




**Agent Harnesses, Multi-Turn RL Bugs, and the Infrastructure Around Autonomy**

  * **A subtle but important RL failure mode got called out** : [@ClementDelangue](https://x.com/ClementDelangue/status/2060175330665508917) highlighted a Hugging Face deep-dive on why many **tool-using, multi-turn RL training loops are silently broken**. The core bug: decoding model output, parsing tool calls, then **re-tokenizing** the updated conversation can change tokenization, so gradients are applied to sequences the model never actually sampled. The proposed fix is a strict **" Token-In, Token-Out"** rule: never re-encode sampled tokens; keep a single token buffer across turns. [@johnschulman2](https://x.com/johnschulman2/status/2060392679528337714) reinforced the broader point that **renderers are foundational** infrastructure between messages and tokens, with failure modes spanning train/test mismatch, caching inefficiency, and prompt injection risk.

  * **Harness design is becoming its own optimization discipline** : [@omarsar0](https://x.com/omarsar0/status/2060371848010019001) surfaced work on **Effective Feedback Compute (EFC)** , claiming raw token/tool counts explain agent success poorly while EFC reaches **R ² up to 0.99**, implying harness quality matters more than gross activity. This lines up with productized tuning efforts like [@LangChain](https://x.com/LangChain/status/2060349231722852680), where **Deep Agents v0.6** makes **harness profiles** first-class to get strong performance from Qwen/Kimi/DeepSeek at **20x+ lower cost** than frontier APIs, and [@hwchase17](https://x.com/hwchase17/status/2060355016989585919) explicitly framing "different models need different prompts/tools." [@vllm_project](https://x.com/vllm_project/status/2060208480292843720) shipped **native weight syncing APIs** and improved pause/resume for async RL, and later added [fastokens](https://x.com/vllm_project/status/2060414393666679229), a **Rust BPE tokenizer** to reduce CPU tokenization bottlenecks in long-context/agentic workloads.

  * **Debate is shifting from "single vs multi-agent" to where the abstraction pays**: [@OfirPress](https://x.com/OfirPress/status/2060352260723392658) argued current multi-agent systems are mostly **speedups, not capability unlocks** ; [@scaling01](https://x.com/scaling01/status/2060363050272653625) took the opposite view, expecting swarm-style training to yield better planning and superintelligence-like behavior. Either way, the practical trend is clear: more teams are building around **agent observability, traces, and continual improvement loops** , e.g. [@Vtrivedy10](https://x.com/Vtrivedy10/status/2060406006329278970) on mining production traces for SFT/distillation and long-horizon continual learning.




**Open Models, Local AI, and the OSS Toolchain Tightening Up**

  * **Local-first and open-weight momentum continues to rise** : [@LangChain](https://x.com/LangChain/status/2060405874993115532) said **1 in 3 AI teams** ran an open-weights model in April 2026, up from **1 in 5** nine months earlier; [@EpochAIResearch](https://x.com/EpochAIResearch/status/2060451576779886942) estimated open-weight models now lag frontier proprietary models by about **four months**. On the toolchain side, [@ggerganov](https://x.com/ggerganov/status/2060394400237109567) launched **llama.app** , giving llama.cpp an official website, a unified installer, and a single `llama` entrypoint aimed at easier local deployment and third-party agent integration. [@ollama](https://x.com/ollama/status/2060428074102206496) announced **OpenJarvis** as a local-first personal AI via Ollama, explicitly tied to Stanford/Hazy's "Intelligence Per Watt" framing.

  * **Open infrastructure is getting more enterprise-shaped** : [@ClementDelangue](https://x.com/ClementDelangue/status/2060378354931388837) noted that **~50% of models and datasets on Hugging Face are now private** , rising with HF's storage/buckets offering; this is an important correction to the idea that HF is only public OSS infrastructure. [@abidlabs](https://x.com/abidlabs/status/2060404002341462044) showed **Hugging Face Jobs** replacing GitHub runners for CPU/serverless GPU CI. [@DSPyOSS](https://x.com/DSPyOSS/status/2060186371902587119), [@dbreunig](https://x.com/dbreunig/status/2060187833084870746), and others shipped a redesigned **DSPy docs/front page** ahead of a coming 4.0, focused on onboarding into programmable AI systems rather than pure prompting.

  * **Licensing and permissiveness are becoming strategic levers** : [@kimmonismus](https://x.com/kimmonismus/status/2060458698930016378) highlighted NVIDIA moving its four open model families to **Linux Foundation OpenMDW-1.1** , reducing legal fragmentation across weights/code/docs/data. New permissive data releases also matter: [@keshigeyan](https://x.com/keshigeyan/status/2060398262591668315) introduced **GPIC** , a **100M-pair permissive image corpus** plus **1M-pair benchmark** for visual generation, with explicit research + commercial usability.




**Google/OpenAI Product Surface Expands: Managed Agents, Gemini Spark/Omni, and Codex on Windows**

  * **Google is widening the "managed agent" stack from API to consumer product**: [@_philschmid](https://x.com/_philschmid/status/2060359976325992528) showed **Managed Agents in the Gemini API** : a single API call provisioning a sandboxed Linux environment with code execution, web access, and file I/O. On the consumer side, [@GeminiApp](https://x.com/GeminiApp/status/2060405496872579115) rolled out **Gemini Spark** to U.S. AI Ultra subscribers as a **24/7 personal agent** that can operate across a user's digital ecosystem under direction. Google also kept pushing **Gemini Omni** multimodal generation/editing demos ([example](https://x.com/alexanderchen/status/2060322611586834518), [product thread](https://x.com/GeminiApp/status/2060473816393150965)) and announced **Google Flow Agent** for creative workflows in video/film production ([thread](https://x.com/Google/status/2060473826362732611)).

  * **OpenAI 's Codex is moving closer to a persistent remote dev operator**: [@OpenAI](https://x.com/OpenAI/status/2060428604727771421) and [@OpenAIDevs](https://x.com/OpenAIDevs/status/2060429591655927942) added **computer use on Windows** , including remote steering from the ChatGPT mobile app. Follow-on UX improvements included **stable identicons for background agents** and search across prior chat content ([@OpenAIDevs](https://x.com/OpenAIDevs/status/2060478367921831936)); [@reach_vb](https://x.com/reach_vb/status/2060430024537178215) summarized broader Codex updates around Windows control, mobile remote access, and profile/task stats. Separately, OpenAI updated **gpt-5.5 instant** to improve **sycophancy, factuality, and multilingual performance** per [@michpokrass](https://x.com/michpokrass/status/2060219759682330970).

  * **This all points to more vertically integrated agent stacks** : model + harness + sandbox + UI + remote control + pricing/quotas. Google is smoothing quotas on Gemini ([@joshwoodward](https://x.com/joshwoodward/status/2060171610922058142)); OpenAI is expanding Codex's operating surface; Cursor added **auto-review mode** with subagent-based approval routing ([tweet](https://x.com/cursor_ai/status/2060406013098897765)). The common pattern is less "chatbot," more **managed execution environment with policy and memory**.




**Research and Systems Papers Worth Attention**

  * **Search, retrieval, and memory** : [@TheTuringPost](https://x.com/TheTuringPost/status/2060194173505155358) highlighted **Bidirectional Evolutionary Search (BES)** from Harvard/MIT, combining forward search with backward decomposition and evolutionary operators; reported gains include **Llama-3.2-3B-Instruct on MuSiQue from 4.0% to 7.0%**. In retrieval, [@_reachsumit](https://x.com/_reachsumit/status/2060214762626306512) pointed to **Latent Terms** , showing sparse BM25-ready features can be extracted from frozen dense retrievers via SAEs. [@topk_io](https://x.com/topk_io/status/2060383255153569938) open-sourced **Iso-ModernColBERT** for more efficient late-interaction inference.

  * **Continual learning and belief/state management** : [@HuggingPapers](https://x.com/HuggingPapers/status/2060312560323182657) summarized **BeliefTrack** , claiming optimized belief-state management cuts long-horizon reasoning failures by **70%+**. [@AndrewLampinen](https://x.com/AndrewLampinen/status/2060460827199599026) argued the continual learning field over-focused on interference instead of positive transfer; [@victor207755822](https://x.com/victor207755822/status/2060315686329778432) presented a second **DeliAutoResearch SKILL** paper focused on self-iteration and CL.

  * **Multimodal/world models/robotics** : NVIDIA-affiliated work included **γ -World**, a generative multi-agent world model streaming at **24 FPS** ([tweet](https://x.com/fangfu0830/status/2060233093894869499)), and **minWM** , a real-time interactive video world model framework ([tweet](https://x.com/_akhaliq/status/2060392729473860026)). In robotics, [@_akhaliq](https://x.com/_akhaliq/status/2060388349425119540) shared **Qwen-VLA** , and [@inventorOli](https://x.com/inventorOli/status/2060357909561622885) demoed Robostral's language-following and manipulation improvements. For always-on proactive agents, [@dair_ai](https://x.com/dair_ai/status/2060373102119555191) surfaced work replacing LLM wake-up decisions with a **220MiB temporal-graph encoder** , gaining **+16.7 mean F1** while running **4 -83x faster**.




**Top tweets (by engagement)**

  * **OpenAI / biology** : [@OpenAI on Rosalind Biodefense](https://x.com/OpenAI/status/2060376598642405492) announced trusted-access biology tooling for public health and biodefense.

  * **Google / consumer agents** : [@GeminiApp on Spark](https://x.com/GeminiApp/status/2060405496872579115) rolled out its always-on personal agent to AI Ultra users in the U.S.

  * **OpenAI / dev tools** : [@OpenAI on Codex Windows support](https://x.com/OpenAI/status/2060428604727771421) and [@OpenAIDevs](https://x.com/OpenAIDevs/status/2060429591655927942) expanded computer use to Windows plus mobile remote steering.

  * **llama.cpp UX milestone** : [@ggerganov](https://x.com/ggerganov/status/2060394400237109567) launched **llama.app** with a unified installer and CLI entrypoint for local AI.

  * **HF / RL correctness** : [@ClementDelangue](https://x.com/ClementDelangue/status/2060175330665508917) amplified the **Token-In, Token-Out** warning for multi-turn RL with tools.

  * **Open vs closed timing gap** : [@EpochAIResearch](https://x.com/EpochAIResearch/status/2060451576779886942) estimated open-weight models are now about **4 months behind** the frontier.




* * *

# **AI Reddit Recap**

## **/r/LocalLlama + /r/localLLM Recap**

### **1\. Local LLM Performance: MoE Releases, Quants, VRAM Savings**

  * **[StepFun 3.7 Flash](https://www.reddit.com/r/LocalLLaMA/comments/1tqloii/stepfun_37_flash/)** (Activity: 637): **StepFun released[Step 3.7 Flash](https://static.stepfun.com/blog/step-3.7-flash/), a multimodal MoE with **`196B`**total parameters,**`11B`**active, and a built-in**`1.8B`**ViT, advertised for high-throughput agent workflows up to**`400 TPS`**and reportedly runnable locally with ~**`128GB`**RAM. Reported benchmarks position it unusually strongly for a flash-class/local model: SWE-Bench Pro**`56.26%`**, DeepSearchQA F1**`92.82%`**, HLE w/tools**`47.2`**, plus large gains over Step 3.5 Flash on Terminal-Bench, Toolathlon, ClawEval, and other agentic/tool-use tasks. Direct model artifacts are available on Hugging Face in[BF16](https://huggingface.co/stepfun-ai/Step-3.7-Flash/), [FP8](https://huggingface.co/stepfun-ai/Step-3.7-Flash-FP8), [NVFP4](https://huggingface.co/stepfun-ai/Step-3.7-Flash-NVFP4), and [GGUF](https://huggingface.co/stepfun-ai/Step-3.7-Flash-GGUF), with day-0 **`llama.cpp`**[support PR](https://github.com/ggml-org/llama.cpp/pull/23845) and related MTP work in **`llama.cpp#23274`**.** Commenters characterize the model as technically odd: its hidden/thinking traces are described as nearly incoherent, but final answers can be _" perfect"_ and competitive with much larger `>1TB` models; one user says the prior Step 3.5 _" infinite thinking"_ issue appears fixed. There is cautious enthusiasm around local deployment, especially for users with `4x3090`-class hardware, and appreciation that StepFun upstreamed `llama.cpp` support instead of only maintaining a fork.

    * StepFun released multiple Step-3.7-Flash checkpoints on Hugging Face: **BF16** ([Step-3.7-Flash](https://huggingface.co/stepfun-ai/Step-3.7-Flash/)), **FP8** ([Step-3.7-Flash-FP8](https://huggingface.co/stepfun-ai/Step-3.7-Flash-FP8)), **NVFP4** ([Step-3.7-Flash-NVFP4](https://huggingface.co/stepfun-ai/Step-3.7-Flash-NVFP4)), and **GGUF** ([Step-3.7-Flash-GGUF](https://huggingface.co/stepfun-ai/Step-3.7-Flash-GGUF)). One user reports the prior Step 3.5 Flash "infinite thinking" issue appears fixed, making 3.7 more usable despite still having an odd intermediate reasoning style.

    * There is day-0 `llama.cpp` enablement via StepFun's upstream PR: [ggml-org/llama.cpp#23845](https://github.com/ggml-org/llama.cpp/pull/23845), contrasting with Step 3.5's fork-based support. A separate community PR for **MTP support** exists at [ggml-org/llama.cpp#23274](https://github.com/ggml-org/llama.cpp/pull/23274), though commenters note it needs updating for Step 3.7 and current `master`.

    * A vLLM nightly test of the **NVFP4** checkpoint on `2x Pro 6k` with `64` concurrent shallow-context requests reached about `2200 tok/s`. The reported config used `tensor-parallel-size 2`, `--enable-expert-parallel`, `--quantization modelopt`, `--kv-cache-dtype fp8`, `--reasoning-parser step3p5`, and StepFun tool-call parsing; vLLM reported **GPU KV cache size**`1,667,645`**tokens** and **max concurrency**`6.36x`**for**`262,144`**tokens/request**.




[ Read more ](https://www.latent.space/p/ainews-founders-and-forward-deployed)

---

## [[AINews] Anthropic raises $965B Series H, releases Opus 4.8 and Dynamic Workflows/ultracode](https://www.latent.space/p/ainews-anthropic-raises-965b-series)
*🔬 Latent Space | 2026-05-29*

Anthropic's path as the [fastest growing company of all time](https://www.latent.space/p/anthropic-glean-and-openrouter-how?utm_source=publication-search) has put overtaking OpenAI in its sights for a while, but there were numerous asterisks for the past few months that put the timing (though perhaps not the fact) of the flippening in question. Today Anthropic [officially reported $47B](https://www.anthropic.com/news/series-h) in revenue run-rate (reminder, this number was $9B in December!) and confirmed their Series H raising $65B at a $900B pre-money valuation (including $15B from hyperscalers including [Amazon](https://www.anthropic.com/news/anthropic-amazon-compute), but also the entire memory industrial complex), putting them at least temporarily ahead of OpenAI in every headline dimension outside of compute and non-coding benchmarks:

[](https://substackcdn.com/image/fetch/$s_!9YXV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffeb0a3a2-e744-4174-a24b-be1fd75961bc_1888x1630.png)

By way of celebration, the company also released [Opus 4.8](https://www.anthropic.com/news/claude-opus-4-8), which broadly reportedly fixed many of the issues the community had found/soured on [Opus 4.7 post launch](https://www.latent.space/p/ainews-anthropic-claude-opus-47-literally) (see recap below for details). It is notably SOTA on basically every economically relevant bench (a nice detail is they agree with Google's messaging that Gemini 3.5 Flash is an improvement over Gemini 3.1 Pro):

[](https://substackcdn.com/image/fetch/$s_!pJaM!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7e7c3740-ab5b-4b98-88eb-c0576e73a2d1_1490x1350.png)

But perhaps of more long term significance is the massively parallel ["dynamic workflows" feature](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code) in Claude Code, also called `ultracode`, which was behind Jarred Sumner's [750k LOC rewrite of Bun from Zig to Rust in 6 days](https://x.com/jarredsumner/status/2060050578026189172):

[](https://substackcdn.com/image/fetch/$s_!FuPa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe9ab93f6-c75f-4156-850a-81b99806aeea_1402x1256.png)

>

> AI News for 5/27/2026-5/28/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

# **AI Twitter Recap**

**Anthropic announced a massive new financing and simultaneously shipped Claude Opus 4.8.**

  * On the capital side, Anthropic said it raised **$65B in Series H at a $965B post-money valuation** , led by Altimeter, Dragoneer, Greenoaks, and Sequoia, and said the money will fund research and expand capacity for growing Claude demand ([Anthropic](https://x.com/AnthropicAI/status/2060061347522433422)).

  * The company also disclosed that its **run-rate revenue surpassed $47B** , attributing growth to enterprise deployments and everyday usage ([Anthropic](https://x.com/AnthropicAI/status/2060061348818518493)).

  * On the product side, Anthropic launched **Claude Opus 4.8** , describing it as an Opus 4.7 update with **" sharper judgment," "more honesty about its own progress," and the ability to work independently for longer**, **at the same price** ([Claude](https://x.com/claudeai/status/2060042702150930686)).

  * Anthropic also launched **Dynamic Workflows** in Claude Code, a research-preview orchestration system where Claude plans work and spawns **hundreds of parallel subagents** to tackle large tasks ([ClaudeDevs](https://x.com/ClaudeDevs/status/2060044853279617150)). Independent eval posts broadly confirm that 4.8 is a meaningful improvement over 4.7, especially on long-horizon agentic coding and knowledge work, though reactions diverged on whether this is a frontier-resetting leap or mostly catch-up to OpenAI's GPT-5.5-family.




## **Facts vs opinions**

### **Facts and directly stated claims**

  * Anthropic raised **$65B** at a **$965B post-money valuation** in Series H ([Anthropic](https://x.com/AnthropicAI/status/2060061347522433422)).

  * The company says its **run-rate revenue crossed $47B** ([Anthropic](https://x.com/AnthropicAI/status/2060061348818518493)).

  * Lead investors named: **Altimeter, Dragoneer, Greenoaks, Sequoia** ([Anthropic](https://x.com/AnthropicAI/status/2060061347522433422)).

  * Altimeter publicly confirmed it led the round and framed it as its **largest investment to date** ([Altimeter](https://x.com/AltimeterCap/status/2060061841372647685), [Pauline Bhyang](https://x.com/paulinebhyang/status/2060069180767171052)).

  * Anthropic launched **Claude Opus 4.8** , positioned as an update to **Opus 4.7** with improved judgment, honesty, and longer autonomous work, **same price** ([Claude](https://x.com/claudeai/status/2060042702150930686)).

  * Anthropic engineers said 4.8 was a response to **feedback on 4.7** , with "many fixes" and better nuance / naturalness ([Alex Albert](https://x.com/alexalbert__/status/2060043196655362358)).

  * Claude Code now supports **Dynamic Workflows** that write orchestration plans and launch **large fleets / hundreds of subagents in parallel** ([ClaudeDevs](https://x.com/ClaudeDevs/status/2060044853279617150), [Cat Wu](https://x.com/_catwu/status/2060054180379689074)).

  * Dynamic Workflows are available in **research preview** and were said to work on **Max, Team, Enterprise, API, Bedrock, Vertex AI, and Foundry** ([ClaudeDevs](https://x.com/ClaudeDevs/status/2060044860984529368)).

  * Anthropic / community posts mention **effort controls** added to web/app/Cowork and continued **Fast mode** support ([Mikey K](https://x.com/mikeyk/status/2060046053907578889), [Sam Callister](https://x.com/sammcallister/status/2060048329359212972), [Kimmonismus](https://x.com/kimmonismus/status/2060044465385902436)).




### **Opinions / interpretations**

  * Bullish views:

    * Opus 4.8 "could've been called Opus 5" ([Dan Shipper](https://x.com/danshipper/status/2060043738752422304)).

    * "Anthropic found a cure for laziness" ([scaling01](https://x.com/scaling01/status/2060043010943942989)).

    * "first smart model in a long while" due to honesty / calibration ([zephyr_z9](https://x.com/zephyr_z9/status/2060077152729694586)).

    * "People unsubscribing from Anthropic will crawl back" ([teortaxesTex](https://x.com/teortaxesTex/status/2060105674311295454)).

  * Skeptical / mixed views:

    * Opus 4.8 is "a minor upgrade" ([scaling01](https://x.com/scaling01/status/2060041564919833041)).

    * Anthropic is "playing catch-up with OpenAI rather than setting the pace" ([kimmonismus](https://x.com/kimmonismus/status/2060085889896726860)).

    * Some benchmark-based criticism from Andon Labs: worse than Opus 4.7 / GPT-5.5 on **Vending Bench** , underperformed on **Blueprint-Bench 2** , more aligned / more cautious, and "max reasoning is not the best reasoning effort" ([andonlabs](https://x.com/andonlabs/status/2060047215134228746), [andonlabs](https://x.com/andonlabs/status/2060047225791877193)).

    * Dynamic workflows are powerful but may be **token-expensive** and quota-burning in practice ([itsclivetime](https://x.com/itsclivetime/status/2060157266591129895), [Theo](https://x.com/theo/status/2060135394570797158), [Omar Sar0](https://x.com/omarsar0/status/2060059612041171175)).




## **Fundraise details and implications**

Anthropic's financing numbers are the headline shock: **$65B raised on a $965B post-money** with **$47B run-rate revenue** disclosed in the same announcement ([Anthropic](https://x.com/AnthropicAI/status/2060061347522433422), [Anthropic](https://x.com/AnthropicAI/status/2060061348818518493)). The scale drew immediate attention because it implies a company operating at near-trillion valuation with hyperscaler-style capital needs and model-serving economics.

Investor messaging was strongly framed around enterprise adoption and operational execution. Altimeter described Claude as becoming the **" default operating system for entire enterprises"** and praised Anthropic's combination of performance and safety ([Altimeter](https://x.com/AltimeterCap/status/2060061841372647685)). Pauline Bhyang said Anthropic had been on a "generational trajectory" since 2022 and highlighted the company crossing **$47B run-rate revenue in under five years** ([Pauline Bhyang](https://x.com/paulinebhyang/status/2060069180767171052)).

The surrounding reactions broke into a few camps:

  * **Validation camp:** This funding size is treated as evidence that Claude has become a core enterprise platform, especially in coding and agentic workflows. Posts like Jamin Ball's "Let's go!!" were simple market validation reactions ([jaminball](https://x.com/jaminball/status/2060062156478107775)).

  * **Scale / bubble concern camp:** Some reacted by comparing the announcement to traditional startup fundraising rhetoric inflated to unprecedented scale. Jerry Liu joked that if you replace "billions" with "millions," it reads like any high-growth startup fundraise ([jerryjliu0](https://x.com/jerryjliu0/status/2060068247773614238)). Another critical read linked the financing to Anthropic's increasingly strict safety gating around more capable models--i.e. vast compute access paired with selective capability release ([menhguin](https://x.com/menhguin/status/2060060425031696387)).

  * **Infrastructure implication:** Anthropic explicitly tied the raise to **capacity expansion** for Claude demand ([Anthropic](https://x.com/AnthropicAI/status/2060061347522433422)). That matters because many of the new 4.8 features--especially higher-effort reasoning, longer independent runs, and multi-agent workflows--are inference-hungry. The capital raise should be read not just as training fuel, but as a direct attempt to underwrite serving costs for long-running agent workloads.




One notable context tweet: a user speculated that "Anthropic also secured tens of billions in inference compute" right as Mythos safety concerns were apparently addressed ([menhguin](https://x.com/menhguin/status/2060060425031696387)). That is speculation, not confirmed by Anthropic, but it reflects a common interpretation: this round is about compute supply and deployment scale as much as model R&D.

## **Opus 4.8: official product positioning**

Anthropic's official framing is unusually specific in its emphasis on **behavioral quality** , not just benchmark scores. The launch tweet says 4.8 has:

  * **sharper judgment**

  * **more honesty about its own progress**

  * **ability to work independently for longer**

  * **same price as 4.7** ([Claude](https://x.com/claudeai/status/2060042702150930686))




Alex Albert added that 4.8:

  * incorporates fixes based on 4.7 feedback,

  * understands nuance better,

  * feels more natural conversationally,

  * is stronger across coding and knowledge work ([Alex Albert](https://x.com/alexalbert__/status/2060043196655362358)).




This honesty / calibration angle became a major subtheme. Multiple Anthropic employees and outside testers described the model as more willing to:

  * say what it doesn't know,

  * flag flaws in its own code,

  * avoid glossing over uncertain progress,

  * stop falsely implying task completion ([Cat Wu](https://x.com/_catwu/status/2060051277476745512), [Mikey K](https://x.com/mikeyk/status/2060046051466502401), [dejavucoder](https://x.com/dejavucoder/status/2060043362858942497)).




That's noteworthy because Claude's prior reputation among heavy coding users included strong generation but uneven self-monitoring: false positives in code review, overconfident progress summaries, and "lazy" or prematurely truncated task execution. Several community reactions explicitly framed 4.8 as fixing this failure mode:

  * "found a cure for laziness" ([scaling01](https://x.com/scaling01/status/2060043010943942989))

  * "least lazy model ever?" ([Teknium](https://x.com/Teknium/status/2060072183783960971))

  * "dramatically less lazy than every other version of Claude" ([nrehiew_](https://x.com/nrehiew_/status/2060046647867191727))




## **Technical details and numbers**

### **Pricing, context, controls**

The most concrete consolidated specs came from Artificial Analysis:

  * **Context window:** **1 million tokens**

  * **Pricing:** **$5 / $25 per million input / output tokens**

  * **Cache writes:** **$6.25 / M** with **5-minute TTL**

  * **Cache hits:** **$0.50 / M**

  * **Effort settings** remain as in Opus 4.7; AA tested **max** effort ([Artificial Analysis](https://x.com/ArtificialAnlys/status/2060117582120976868))




Community posts also highlighted:

  * **Fast mode** is available for Opus 4.8

  * It is **~2.5x faster** and **3x cheaper than before** versus prior fast-mode economics ([kimmonismus](https://x.com/kimmonismus/status/2060044465385902436))

  * scaling01 summarized the new economics as:

    * **Opus 4.8 Fast: 2.5x faster, only 2x more expensive than normal 4.8**

    * versus **Opus 4.7 Fast: 2.5x faster, 6x more expensive than normal 4.7** ([scaling01](https://x.com/scaling01/status/2060051666443943962))

  * Effort controls were newly exposed in more product surfaces, allowing users to dial reasoning up or down ([sammcallister](https://x.com/sammcallister/status/2060048329359212972), [mikeyk](https://x.com/mikeyk/status/2060046053907578889), [kimmonismus](https://x.com/kimmonismus/status/2060045324803063962))




This matters because many early user reports suggest **reasoning-effort selection significantly changes output quality and cost** , especially for coding and writing. Dan Shipper recommended **xhigh** for coding and **high** for writing after observing weaker behavior at lower settings ([Dan Shipper](https://x.com/danshipper/status/2060043738752422304)). Andon Labs similarly said **max reasoning is not the best reasoning effort** on some tasks ([andonlabs](https://x.com/andonlabs/status/2060047215134228746)).

### **Benchmarks: strongest reported numbers**

Key official / semi-official numbers surfaced across launch tweets:

  * **SWE-Bench Pro: 69.2%** , claimed by Yuchen citing release materials, and "10 points higher than GPT-5.5" ([Yuchenj_UW](https://x.com/Yuchenj_UW/status/2060042830559756407))

  * **FrontierSWE #1** , cited by Anthropic watchers and later confirmed by third-party references ([scaling01](https://x.com/scaling01/status/2060046440563388838), [scaling01](https://x.com/scaling01/status/2060054319446016046))

  * **APEX-SWE: 45.3% Pass@1** , nearly **4 points ahead of GPT-5.3 Codex at 41.5%** ([mercor_ai](https://x.com/mercor_ai/status/2060046111793123428))

  * **GDPval-AA: 1890 Elo** , **+137 vs Opus 4.7** , **+121 vs GPT-5.5 xhigh** , implying about **67% win rate vs GPT-5.5 xhigh** head-to-head ([Artificial Analysis](https://x.com/ArtificialAnlys/status/2060042848268083411))

  * Artificial Analysis Intelligence Index: **61.4** , **+4.1 vs Opus 4.7** , **+1.2 ahead of GPT-5.5 xhigh** ([Artificial Analysis](https://x.com/ArtificialAnlys/status/2060117582120976868))

  * **AA-Omniscience: 27.4** , #2 behind Gemini 3.1 Pro at 32.9; **accuracy 46.6%** , **hallucination 35.9%** ([Artificial Analysis](https://x.com/ArtificialAnlys/status/2060117582120976868))

  * Gains on:

    * **Terminal-Bench Hard +6.8**

    * **τ ²-Bench Telecom +5.9**

    * **IFBench +3.6**

    * relatively flat on **AA-LCR, GPQA, SciCode** ([Artificial Analysis](https://x.com/ArtificialAnlys/status/2060117582120976868))




Additional qualitative benchmark observations:

  * Cursor said Opus 4.8 works **much more efficiently than 4.7** on **CursorBench** and is more persistent on hard tasks ([Cursor](https://x.com/cursor_ai/status/2060044920237469872))

  * Anthropic employees emphasized strength on **long-horizon work** in Claude Code ([ClaudeDevs](https://x.com/ClaudeDevs/status/2060043212425933076))

  * Some users reported especially large jumps in **knowledge work** and **writing** ([Dan Shipper](https://x.com/danshipper/status/2060043738752422304), [rishdotblog](https://x.com/rishdotblog/status/2060057903344869828))




### **Efficiency and token-use details**

Artificial Analysis reported:

  * Compared to Opus 4.7, 4.8 achieved higher GDPval performance with:

    * **15% fewer turns per task**

    * **35% fewer output tokens**

  * But 4.8 still used **~30% more turns than GPT-5.5** , the second-ranked model ([Artificial Analysis](https://x.com/ArtificialAnlys/status/2060042850826612996))




This is one of the more important nuanced findings in the launch coverage:

  * 4.8 is **more efficient than 4.7**

  * but still not obviously the **most inference-efficient frontier model** against OpenAI on some workloads




That tension is echoed in community commentary:

  * "still getting token-mogged by GPT-5.5" ([scaling01](https://x.com/scaling01/status/2060080401947746483))

  * Theo and others complained that Claude's higher-agency, higher-effort modes can blow through quota extremely quickly in practice ([Theo](https://x.com/theo/status/2060120708815139241), [cremieuxrecueil](https://x.com/cremieuxrecueil/status/2060161310302630154))




### **Long context**

Posts highlighted long-context improvements from Opus 4.6 to 4.8, with one claim that **Opus 4.8 at 1M context is almost as good as GPT-5.5 's 256K score** on a referenced long-context eval ([scaling01](https://x.com/scaling01/status/2060047431564251545)). Artificial Analysis also confirmed the **1M token** context remained intact ([Artificial Analysis](https://x.com/ArtificialAnlys/status/2060117582120976868)).

### **Safety / robustness / hallucination**

This was one of the more mixed parts of the release.

Positive:

  * Anthropic and supporters emphasized lower dishonesty / better calibration.

  * "dishonesty at an all time low" ([scaling01](https://x.com/scaling01/status/2060042892903678414))

  * "noticeably more honest" ([Cat Wu](https://x.com/_catwu/status/2060051277476745512))

  * "flags what it's unsure of" ([Mikey K](https://x.com/mikeyk/status/2060046051466502401))

  * Artificial Analysis said Anthropic continues to show **substantially lower hallucination rates than Google/OpenAI peers** ([Artificial Analysis](https://x.com/ArtificialAnlys/status/2060117582120976868))




Negative / cautionary:

  * scaling01 noted **Opus 4.8 is the first model in a long time that doesn 't improve prompt injection robustness** over 100 trials ([scaling01](https://x.com/scaling01/status/2060042401478005237))

  * scaling01 also called it Anthropic's **" most eval aware model"** ([scaling01](https://x.com/scaling01/status/2060043854967923086))

  * Andon Labs said it was **more aligned / more cautious** , "scared of getting caught," and worse on some adversarial / business-task benchmarks ([andonlabs](https://x.com/andonlabs/status/2060047215134228746))

  * nrehiew_ noted slight hallucination improvements on the reported evals but questioned whether some hallucination tests reflect the failure modes users actually encounter ([nrehiew_](https://x.com/nrehiew_/status/2060048083753591264), [nrehiew_](https://x.com/nrehiew_/status/2060048085838118953))




### **Cyber capability gating and future model class**

An especially important strategic detail appeared in reaction posts: Anthropic appears to have stated it plans to **release "a new class of model with even higher intelligence than Opus"** after stronger safeguards ([dejavucoder](https://x.com/dejavucoder/status/2060042723185623261)). Multiple watchers interpreted this as a **Mythos-class** rollout with cyber-sensitive capabilities selectively constrained:

  * "Mythos class model to all customers in the coming weeks" ([kimmonismus](https://x.com/kimmonismus/status/2060047510853312557))

  * "They are releasing a Mythos-class model with the appropriate safeguards, meaning that you can't use the 'too dangerous to release' capabilities" ([scaling01](https://x.com/scaling01/status/2060123335514636693))

  * Cline summarized Anthropic as announcing plans to release new models **with higher intelligence than Opus after adding stronger cyber safeguards** ([Cline](https://x.com/cline/status/2060063889874972905))




This is not just product roadmap gossip; it reframes Opus 4.8 as a **staged release strategy** :

  1. improve the commercially safe / broadly deployable general model,

  2. hold back more dangerous cyber capability until controls are ready.




That tradeoff drew both praise and criticism:

  * supportive: safety-first frontier deployment

  * skeptical: Anthropic may be sacrificing some competitiveness in raw capability availability to maintain its risk posture ([teortaxesTex](https://x.com/teortaxesTex/status/2060114150928322868))




## **Dynamic Workflows: the most important technical addition beyond the base model**

The standout systems feature accompanying Opus 4.8 is **Dynamic Workflows** in Claude Code.

Official description:

  * "Claude writes an orchestration script on the fly"

  * then spins up **a large fleet of coordinated subagents in parallel**

  * use the word **" workflow"** in a prompt to activate it ([ClaudeDevs](https://x.com/ClaudeDevs/status/2060044853279617150))




Anthropic's employees and users described it as enabling:

  * orchestration plans that Claude "strictly follows"

  * **hundreds of agents**

  * verification before returning results

  * support for very large migration / refactor / auditing jobs ([Cat Wu](https://x.com/_catwu/status/2060054180379689074), [Mikey K](https://x.com/mikeyk/status/2060046052821184907))




Examples cited:

  * **porting Bun from Zig to Rust** , around **750k lines** , **99.8% of test suite passing** , **11 days from first commit to merge** , using hundreds of parallel agents and two reviewers per file ([Cat Wu](https://x.com/_catwu/status/2060051282698682576))

  * processing **hundreds of A/B test flags** in parallel in **< 10 minutes** to identify stale flags ([Cat Wu](https://x.com/_catwu/status/2060054182447448387))




This launch triggered a mini-debate around the broader concept:

  * Some researchers argued Anthropic had essentially productized ideas resembling **Recursive Language Models / symbolic recursion over prompts** ([a1zhang](https://x.com/a1zhang/status/2060071701879066626), [lateinteraction](https://x.com/lateinteraction/status/2060078643133763839), [lateinteraction](https://x.com/lateinteraction/status/2060082815077961842))

  * Others pushed back that "calling models in a loop" is not novel and that many builders have been doing this manually for months ([omarsar0](https://x.com/omarsar0/status/2060059612041171175), [jxmnop](https://x.com/jxmnop/status/2060109869399916770), [willdepue](https://x.com/willdepue/status/2060144024300695662))




The more substantive critique was not originality, but **cost and harness quality** :

  * Omar Sar0 warned agent-to-agent interactions are effective but token-heavy ([omarsar0](https://x.com/omarsar0/status/2060059612041171175))

  * Theo complained about conflicting parallel edits and wasted tokens in the current tooling ([Theo](https://x.com/theo/status/2060135394570797158))

  * itsclivetime joked that "hundreds of parallel subagents" will hit quota in seconds ([itsclivetime](https://x.com/itsclivetime/status/2060157266591129895))

  * KLieret highlighted a system-card finding: multi-agents may not improve final ProgramBench quality, but they reach mediocre solutions **2x faster** ([KLieret](https://x.com/KLieret/status/2060111272943739243))




So the consensus from technical users is:

  * **Dynamic workflows are strategically important**

  * they are likely the future of coding agents

  * but the current implementation still faces **editing conflicts, cost blowups, and harness inefficiencies**




## **Different opinions on Opus 4.8**

### **1) Strongly supportive: Anthropic is back**

[ Read more ](https://www.latent.space/p/ainews-anthropic-raises-965b-series)

---

## [The Age of Async Agents — Cognition's Walden Yan & OpenInspect's Cole Murray](https://www.latent.space/p/cognition)
*🔬 Latent Space | 2026-05-28*

_The new[AIEWF website](https://ai.engineer/wf) is live! [CFPs](https://ai.engineer/cfp) close in 2 days and we will run our first New Engineer Orientation this weekend, get your tickets booked ASAP as they -will- sell out. Take the [AI Engineering Survey](https://notion.qualtrics.com/jfe/form/SV_bP07tSVMXH7ePCS) and get >$2k in credits and free [AIE WF tickets](https://ai.engineer/wf)!_

* * *

One of the central tensions in the agents industry is that even while there are major decacorn agent labs like Sierra, Decagon, Notion and Cursor being built up, it is also true that it has never been easier to DIY agents, with a plethora of agent frameworks like [LangGraph](https://www.latent.space/p/oai-v-langgraph) and [Pydantic](https://www.latent.space/p/pydantic) and [Flue](https://x.com/FredKSchott/status/2050274923852210397), and managed agents from [Anthropic](https://www.anthropic.com/engineering/managed-agents) and [Gemini](https://blog.google/innovation-and-ai/technology/developers-tools/managed-agents-gemini-api/) and [Amazon](https://openai.com/index/openai-on-aws/). There has been a wave of companies building their own background agents from [Shopify](https://x.com/simonw/status/2053529689122328947) to [Stripe](https://stripe.dev/blog/minions-stripes-one-shot-end-to-end-coding-agents) to [Paradigm](https://x.com/matthuang/status/2057500542298136899?s=46) to [Razorpay](https://x.com/shashank_kr/status/2056246734465253859?s=46), and even Cognition's friends [Ramp](https://x.com/zachbruggeman/status/2010728444771074493?s=46) have [built their own coding agent with other friend Modal](https://modal.com/blog/how-ramp-built-a-full-context-background-coding-agent-on-modal).

You'd think Cognition might feel a bit threatened, but they're not - even after all this, they were way oversubscribed for the[ $1B Series D ](https://www.latent.space/p/ainews-cognition-raises-1b-in-26b?utm_source=publication-search)they just announced:

[Walden Yan](https://www.linkedin.com/in/waldenyan), [coiner of context engineering](https://cognition.ai/blog/dont-build-multi-agents) and Chief Product Officer/Cofounder of Cognition, invited [OpenInspect's Cole Murray](https://github.com/ColeMurray/background-agents) to talk about why [the Devin is in the Details](https://swyx.io/cognition).

Full conversation [live on the pod](https://www.youtube.com/watch?v=0fgJPhYcbVk) today: 

In retrospect, async agents were the most AGI pilled bet you could make in 2024 - the models weren't good enough yet to vibecode, and people didn't trust AI enough to let it rip, nobody (including early Cognition) was sure about the form factors. 

Now it is obvious:

  * The **first wave of AI coding tools** made the developer faster but remain heavily in the loop. [Copilor and Cursor's tab autocomplete](https://cursor.com/help/ai-features/tab) are prime examples However, the workflow was still heavily centered around and **bottlenecked** by the developer's local workflow: a developer in an IDE, watching the model, accepting or rejecting changes, and pushing code one interaction at a time.

  * The second wave was **local agents** : [Claude Code](https://www.latent.space/p/claude-code), [Windsurf](https://www.latent.space/p/windsurf), Cursor's agents pane: first one and increasingly many terminals all running concurrently.

  * The current **Age of Async Agents** points to a **different future** focused more on **agent orchestration** which drives end-to-end development.




_According to previous[guest Steve Yegge](https://www.latent.space/p/steve-yegges-vibe-coding-manifesto), there are finer-grained [8 levels to agent adoption](https://www.oreilly.com/radar/steve-yegge-wants-you-to-stop-looking-at-your-code/), but we have collapsed it into three._

As Cursor's Michael Truell put it in [The third era of AI software development](https://cursor.com/blog/third-era):

> _**Cursor is no longer primarily about writing code**. It is about helping developers **build the factory that creates their software**. This factory is made up of **fleets of agents that they interact with as teammates** : providing initial direction, equipping them with the tools to work independently, and reviewing their work._

[](https://substackcdn.com/image/fetch/$s_!QPqO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2c0a0107-653e-4c83-a249-c3308b1ed019_1498x844.png)

The agent should not sit solely inside the developer's flow. It should be setup to **work in the background** so that you can give it a task, a repo, a machine, a shell, a browser, tests, memory, and review loops to go do the work somewhere else.

In less than a year, the sentiment has shifted from **avoiding multi-agent systems** :

to suggesting approaches **that actually work** :

From coining **" context engineering"** to building the infrastructure behind **Devin 's 7x PR growth** and jump from **16%** to **80%** of commits across Cognition repos, **Walden Yan** has had a front-row seat to the background-agent shift. In this episode, Cognition co-founder and CPO **Walden Yan** joins swyx alongside **Cole Murray** , creator of **OpenInspect** , to unpack why everyone is building their own Devin, what changed after the **December 2025 model inflection** , and why **" spec to pull request"** is now becoming a real production workflow.

We go deep on the architecture of **background agents** : harness-in-the-box vs out-of-the-box, why Devin separates **the "brain" from the machine**, why repo setup is still one of **the hardest problems** , why Docker is not always enough, and how full VMs, snapshots, scoped secrets, GitHub bots, Slack integrations, and video-based testing all fit together. Walden and Cole also dig into memory, MCP limitations, **[multi-agent orchestration](https://cognition.ai/blog/multi-agents-working)** , AI code review, SRE auto-triage, PMs shipping code from Slack, Windsurf 2.0, hybrid frontier/sub-frontier systems, and the real failure mode of uncontrolled vibe coding: your codebase regressing to your worst engineer.

And as[ agents eat software… and software eats the world… ](https://www.youtube.com/watch?v=zepu8Kk6FBQ)you can draw the conclusion on what is next:

### We discuss:

  * Why the engineering world is waking up to **background agents** and **cloud agents**

  * The **December 2025 model inflection** that made spec-to-PR workflows practical

  * Devin's **7x merged PR growth** and rise from **16%** to **80%** of commits

  * Why Cole built **OpenInspect** as an open-source background-agent system

  * The economics of **$20/seat** agent products and why monetization is tricky

  * What Cognition actually sells beyond Devin: **infra, onboarding, integrations, and adoption**

  * **Harness in the box vs out of the box** , and why architecture matters

  * Why Devin separates the **brain** from the machine for **security** and **permissions**

  * Repo setup, scoped secrets, Docker Compose, and agent-ready dev environments

  * Why full **VMs matter** when agents need to run real applications and test them

  * Android, macOS, Windows, nested virtualization, and machine-specific agent work

  * Why testing is much harder than **" computer use"**

  * Screenshots, video verification, and the **" I know it works"** merge moment

  * **GitHub UX, Devin Review, AI reviewers, and agents** responding to PR comments

  * Why MCP alone is **not enough** for first-class Slack and enterprise integrations

  * Memory, Knowledge, skills, Claude.md, and why retrieval is still unsolved

  * **Devin 's auto-generated memories** and the challenge of memory pruning

  * **Always-on agents** as permanent PMs for issues, tickets, and product areas

  * Sub-agents, meta-Devin management, and what multi-agent systems actually add

  * Why pure auto-merge vibe coding **breaks down after about two weeks**

  * AI code smells, lint rules, reward hacking, and Semgrep for agent-written code

  * GitAI, inline context, and preserving the **" why" behind code changes**

  * Local testing, mock servers, older codebases, and preparing companies for agents

  * **Windsurf 2.0** and the handoff between local foreground agents and cloud background agents

  * SRE auto-triage, support workflows, and agents as first responders

  * PMs, marketing, and non-engineers creating pull requests from Slack

  * AI agent **budgets** , **$1k-$5k** per engineer **spend** , and hybrid frontier/sub-frontier systems

  * The rise of **autonomous coding factories** and **who Cognition is hiring**




* * *

### Walden Yan

  * **X:** <https://x.com/walden_yan>

  * **LinkedIn:** <https://www.linkedin.com/in/waldenyan/>




### Cole Murray

  * **X:** <https://x.com/_colemurray>

  * **LinkedIn:** <https://www.linkedin.com/in/colemurray/>

  * **OpenInspect / Background Agents:** <https://github.com/ColeMurray/background-agents>




* * *

## Timestamps

**00:00:00** Introduction  
**00:00:43** Why Everyone Is Building Their Own Devin  
**00:01:57** Devin's 2025 Ramp: 7x PR Growth and 80% of Commits  
**00:03:49** OpenInspect and the Rise of Open-Source Background Agents  
**00:07:59** What Cognition Actually Sells Beyond Devin  
**00:09:56** Background Agent Architecture: Harness In vs Out of the Box  
**00:12:08** Separating the Brain from the Machine  
**00:14:07** Repo Setup, Secrets, Docker, and Full VMs  
**00:19:13** Why Testing Is Harder Than Computer Use  
**00:22:40** Video Verification and the "I Know It Works" Merge Moment  
**00:23:19** GitHub UX, Devin Review, and AI Code Review  
**00:25:42** MCP, Slack, and Enterprise Agent Integrations  
**00:28:59** Memory, Knowledge, and Always-On Agents  
**00:36:16** Sub-Agents, Multi-Agent Orchestration, and Meta-Devin  
**00:43:55** Vibe Coding, Auto-Merge, and Codebase Decay  
**00:48:38** Agent Infra, VPCs, Cloud Providers, and Fast VM Restore  
**00:52:25** AI Code Smells, Reward Hacking, and Code Review Systems  
**00:56:10** Making Codebases Agent-Ready  
**00:58:30** Windsurf 2.0 and the Local-to-Cloud Agent Handoff  
**01:01:15** SRE Auto-Triage, PMs Shipping Code, and Agent Use Cases  
**01:04:32** Agent Budgets, Hybrid Models, and Autonomous Coding Factories  
**01:06:51** Hiring at Cognition and OpenInspect Consulting  
**01:07:45** Outro

* * *

# Transcript

## Introduction: Walden Yan, Cole Murray, and Context Engineering

**Swyx [00:00:00]:** All right, we're in the studio with Walden Yan, co-founder of Cognition, CPO.

**Walden [00:00:08]:** Happy to be here.

**Swyx [00:00:09]:** Which is a cool title. And coiner of context engineering.

**Walden [00:00:15]:** Although I think there are many people who'd used the terms in various ways beforehand, but I did find that people, both internally and externally, enjoyed the upgrade from prompt engineering or model wrapping into maybe a more thoughtful way to build agents.

**Swyx [00:00:33]:** For those who haven't caught up on that, I have on screen the Don't Build Multi-Agents post, which you should go read on and we might refer to, and Cole Murray, who created OpenInspect.

**Cole [00:00:43]:** Great to be here.

**Swyx [00:00:43]:** So let's talk about it. Everyone is building their own Devins. What's going on?

## The December Shift: From Handholding Models to Autonomous PRs

**Cole [00:00:51]:** So I think the engineering world is waking up to this idea of background agents, cloud agents, whatever you'd like to call it. And I think we saw a shift around the December timeframe of 2025, where the models Opus 4.5 and GPT 5.2, they reached a capability where we moved away from handholding the model and being able to actually more or less autonomously drive the model. And what I mean by that is that we could pretty much go from a specification to a completed pull request, assuming the spec was good enough, with very little friction. And that paradigm alone, I think, changed a lot of how we interact with agents, and opened this world where background agents became more practical.

**Swyx [00:01:41]:** I think for Cole, everyone experienced this in December, but I feel like there was just this increasing ramp, right? There was this moment which was, I think, Sonnet 3.7, where, You guys rewrote Devin in one night or something. So describe 2025 or how it felt from your side.

**Walden [00:02:01]:** In retrospect, we always thought it was ramping up, but then even now, over the last three, four months from today, it's been ramping up even faster. So it's almost funny to be talking about how, big of a leap Sonnet 3.7 was, and honestly, a lot of it was stripping out parts of Devin that were no longer needed with that jump in of intelligence. But I also just think that a lot of the recent leaps, especially, you look at, models like Opus and the latest GPT models, they are reaching levels of autonomy where people are actually finding that they actually can just be hands-off. And people who were once debating, "Oh, do I need to be in the weeds with my model in the IDE? Can I just completely move it off into the cloud?" That's a more serious conversation, and we've seen that in all of our growth charts. Internally there's this funny graph where our usage has, of PRs, our merged PRs, has grown 7X since I forget what it was called.

**Swyx [00:02:57]:** I think Dev, maybe tweeted that. Yes.

**Walden [00:03:01]:** it grew like 7X over, the last, I think it was, two months, three months, something like that. And then you see our engineering headcount growth. It's, gone up by, 10% or something.

**Swyx [00:03:11]:** We were, we were afraid To release this. So this is Devin commit percentages on all Devin repos, was 16% in January and now 80% in March.

**Walden [00:03:25]:** It's a big shift right now. And so it makes sense that a lot of people are now thinking about, buying Devin, but also maybe, trying to build their own and there's Lots of I have a lot of fun building Devin, so I can see why other people would want to build their own cloud agents as well. Matt, well, maybe it's good to hear, what initially inspired you to try to build OpenInspect?

## OpenInspect: Ramp, Cloud Agents, and Open Source

**Cole [00:03:49]:** OpenInspect came about, through primarily my clients observing how they were using tools like Claude, OpenAI's Codex at the time, and seeing some of the friction that they were having with it. Primarily the Claude was being used through Slack, and a big issue they ran into was that the sessions that were launched were specific to whoever called it via Slack. And so if a PM was the one who invoked the session and they would then go to pass context to engineering can't see the session. And that in itself was a deal breaker because the PM, "Hey, engineering, can you jump in?" But there's nothing to jump in on unless they're copy-pasting out or the single response that came back. And so seeing some of these problems, I had built a similar architecture internally, just to experiment with, test out different ideas as this trend of moving off of localhost was starting to become, And as Ramp released their blog post, I had a lot of the pieces for this already in place, and just thought it would be funny to, see what Claude could do just purely from the blog post. And on my X account, there's actually a thread of where I live tweeted, going through this

**Cole [00:05:14]:** comparing GPT and Claude as both of them are going through it.

**Swyx [00:05:17]:** On the announcement thing or something else?

**Cole [00:05:19]:** right after it got released. We can put it in the show notes. Yeah, it was helpful that I had already knew how to verify the system. I knew what I was looking for. I think Ramp did a great job of really illustrating, the technical aspects of how to build something. It was much more than just like, "Hey, we built a great system." It was, "And here's how you can build it too." And so, I resonated a lot with that, just with the problems that I was already seeing, and I thought that, looking around, I didn't really see anything in the open source community that, met this type of system. I think there's a lot that run, in localhost like Superset, Conductor, and many others.But nothing that was actually running in the cloud. And so, I built it, and I thought it was interesting to just open source it and allow anyone to then have a foundation that they can mix and match on top of.

## The Business of Background Agents: Open Source vs. Devin

**Swyx [00:06:16]:** So literally after Devin was launched was, there was OpenDevin Which became All Hands. I don't know if you tried that or

**Walden [00:06:22]:** I was going to say, one of the things that interested me a lot with OpenInspect was, you didn't try to go make it then something you monetize. There are a lot of, I think, these open source projects would then go and really try to, raise V

**Swyx [00:06:36]:** That's why no OpenDevin. Yeah.

**Walden [00:06:38]:** yeah, and how did you think about that? I thought that was very interesting.

**Cole [00:06:44]:** I thought, and just what I had seen across my clients, was that having a background agent system is going to become a critical infrastructure within their company. And so because of that, I think that I wanted to open source it so that they could fork it and put in whatever customization they wanted. To that question though, I get asked all, "Oh, are you going to raise? Are you going to turn this into a service?"

**Walden [00:07:08]:** I'm sure you've gotten offers.

**Cole [00:07:09]:** but primarily I don't want to do that for a few reasons. One, I think that I don't want to compete for, $20 a seat. I think that is just a really difficult business. I think it's very easy to copy the main pieces of it. Again, I built this fairly quickly. And I think because you are not owning, I guess, the entire stack, it's hard to monetize. You have money being made at the sandbox layer with Daytona, E2b, many other players. You have money being made at the model layer. And you sit in this weird in-between gray area where what are you actually selling? You're selling, I guess, the infrastructure. You're selling, the integrations maybe.

**Swyx [00:07:55]:** let's ask the guy. What are you What are you selling?

**Walden [00:07:59]:** Well, yeah, there's multiple layers to this in practice, and actually it's funny you mentioned the infrastructure, 'cause when we got started building Devin as well, we had to go figure out how to make the infrastructure as well because,

**Swyx [00:08:10]:** You had to build this two years before everyone else,?

**Swyx [00:08:15]:** Including, the model side

**Walden [00:08:17]:** It was not, it was not very polished at the start, when we just built it off of raw VMs from cloud providers like EC2, the boot up time was so slow, I think, And especially then, turning off the machines, saving them, and then to be able to bring them back up again when the, when you want Devin to wake up again later. It would just be out cold for like 10 minutes because that's just how long these systems took. They were not built for this repeated down and up usage. And so we actually had to go do all of that. And as a result now, one thing we offer when we go and sell Devin to people is, you don't have to worry about all the compute side of things. We'll make it work. We'll make it work in your cloud if you want it to. But aside from the product, and I want to go into the agents and the tuning of the intelligence part later, but I think a big part of what we do at Cognition as well is to just make sure that your company learns and uses and adopts these coding agents. 'Cause I think for especially the largest enterprises in the world, you find that there is a lot of people who want to move over to using AI for their day-to-day workloads. But because of the way projects are planned, because, not everyone is literate in using AI in these ways, having a team of engineers who can actually go in and onboard you, set up all the integrations you need, the automations you need to really get to that level of, leverage with AI, is super helpful. And so We do that. We show thought partners to the customers that we work with as well.

**Swyx [00:09:56]:** So let's talk about, architectural stuff. I think that's always, that is something that was the topic of conversation between the two of you. Is this, the mental model that you want to start with or something else? I'll just leave the floor open to you guys.

## Agent Architecture: Harness in the Box vs. Out of the Box

**Cole [00:10:11]:** I think, maybe we can start here as just a general what are the pieces of a background agent system. And then maybe we can go into some of the nuances of, Decisions that you can make.

**Swyx [00:10:22]:** But I guess I also Like, what, maybe what Walden is saying is the agent is like in this open code box, I guess. Right? This is infra, and then there's, that's the agent. And you had this discussion about whether you put the agent in here or in Out externally. Can you tease that out?

**Cole [00:10:39]:** In a background agent systems, you have a decision to make of where the agent is actually going to run. This is typically described as the harness in the box or out of the box. With running the agent in the box, you're making some trade-offs by doing that. The negative trade-off you're making is primarily security. Because the agent is running in that box, unless you otherwise design it, all of your secrets need to go into that box as well. And given the nature of AI, it can be unpredictable, and you could very easily end up accidentally exfilling your secrets, or other unintended behavior. Now, the out of the box is the idea that we are going to have the actual agent running not directly in the sandbox, and we will have, quote-unquote, the brain of the agent running in some type of worker, control plane. That sandbox then is going to serve as the hands where the brain is basically operating and making tool calls into that environment to manipulate it. I guess other trade-off that you're making between the two systems is that, in my opinion, running it out of the box is much more complex because, you have state that has to be managed, whereas if you're running it in the box, all of the state of that agent is actually in the box, and yes, it's you could persist it elsewhere, but it's all localized and you have less concerns to worry about.

**Walden [00:12:08]:** I think a lot of that, what you mentioned, is why we actually from the start built Devin to what we called separate the brain from the machine. The other thing that this allows you to do is reuse any existing infrastructure you have for dev boxes Perhaps. And so you don't have to worry as much about making a new type of dev box that has all the dependencies the brain needs, as you mentioned, the secrets the brain needs as well. One thing that we've seen some customers run into is, you have a GitHub app and you want Devin, your agent, whatever, be able to interact with GitHub through this application, but then you have different users with different actual permissions. If they are all interacting through the same GitHub app and there's no actual, separation between the system that decides, what it does and the actual secrets on the machine, then you run into an issue where, okay, it's hard to do the separation. But in practice, with Devin, it's much easier because we just say whatever you put on the machine, that is, the scope of basically what the user is free to do, what the agent is free to do. So only put the most scoped secrets on that machine, and then the brain is fully not accessible from the machine. So you don't have to worry about messing with the, any of the most secure parts of the brain if the user is free to do whatever they want with the machine.

**Swyx [00:13:31]:** I was going to just bring, I have this, chart from OpenAI, where I don't know if this is, in the box, out of the box. That is something that they do use to describe it. And then also recently Anthropic did, managed agents

**Swyx [00:13:44]:** Which is, this is their thing. I don't know. It's all, it's all variations of the same pattern, right?

**Cole [00:13:49]:** So this would be out of the box.

**Swyx [00:13:51]:** Which, is preferable for them because it's less work?

**Cole [00:13:56]:** I would say it's more work.

**Swyx [00:13:58]:** It's more work?

**Cole [00:13:58]:** But it, in my opinion, it is the better architecture of the two. It's just, you're taking on a bit of complexity by doing that.

## Repo Setup, Docker, and VM-Based Development Environments

**Walden [00:14:07]:** One thing I've not seen a lot of other players do well is how do you manage what's actually on the box? And this can be complex for many reasons. Let's say you have a big repository that's changing and updating a lot with changing dependencies. How do you make sure that the working environment of the agent actually stays up to date, has all the credentials it needs to, let's say, run the app and test it, and all the things you want your autonomous

**Swyx [00:14:34]:** So a repo setup.

**Walden [00:14:35]:** Exactly. So in, internally At Cognition, we call this repo setup.

**Cole [00:14:39]:** The hardest part of

**Walden [00:14:40]:** It's been a perennial problem since the start of the company, of how do we help people get this set up? Because not everyone just has, working cloud environments working out of the box. And do you find this to be a common problem with

**Swyx [00:14:53]:** How do you solve it?

**Walden [00:14:53]:** Your clients?

**Cole [00:14:54]:** This is a very common problem, and through my consulting, this is a lot of what I help teams do. A lot of teams don't really have great developer environment setups, if any. A lot of the times it's, "Go talk to Bob and get the secrets," and that obviously doesn't work when the agent needs to actually set this up. And so a lot of that, most teams are using Docker Compose or some type of microservices. And so for the

**Swyx [00:15:19]:** Even in prod?

**Cole [00:15:20]:** Not in prod. With the OpenInspect, you are using this primarily to interact, and make code changes. There is other use cases, but you can hook, whether through CLI, MCPs, other tools, you can then hook that into your production systems primarily for, SRE type use cases. But you are not, necessarily, trying to test your prod internal microservice through the system.

**Walden [00:15:48]:** And you mentioned Docker Compose. I think one direction we saw some of our friends take early on was, using Docker containers as the level of abstraction for their models. There's lots of reasons, I think, why Docker containers are not great. One thing is, Docker container's not really a true security boundary, for one. But the other is, if you are running real applications, a lot of times those applications use Docker, and then you have to think about Docker in Docker, which is, really weird. And so I think part of, the really hard challenge of getting VMs to work, why did we do that? Well, it was because we realized that you actually needed, full VMs to be able to do these types of things. And especially nowadays where there's actually value in running the application and clicking around and sending you screen recordings of these things. The value just, keeps adding on top of that. But it is a decision I see people run into when they try to build their own systems, is, "Oh, do we, in addition to this, do we put the agent in the machine or out of the machine? Do we use Docker? Do we use something else?" What do you recommend people nowadays?

**Cole [00:16:57]:** I think Docker is a good solution for maybe not running the agent, but running your infrastructure, because that is more or less the same setup your engineers are probably already using. If they're not, then I don't know what they're using. But they're probably already using Docker Compose.

**Swyx [00:17:14]:** I've always had a small candle for web containers. I don't know if you guys have tried them before.

**Swyx [00:17:19]:** To me, they were, supposed to be like Docker Light.

**Cole [00:17:22]:** Is it?

**Swyx [00:17:22]:** I don't know.

**Cole [00:17:22]:** No, I haven't tried it. But yeah, I think any environment that you've set up that is a good experience for your developer naturally lends itself to being easy to set up for the agent. And once you figure out that local developer story, you've more or less solved the agent in a sandbox, environment setup. OpenInspect does have hooks as well, where you can, run a setup SH script that will pre-install everything. You can then pre-snapshot that build so it starts instantly, and then there is a second hook to actually then, restore the state of the sandbox when it comes back. And so you can already have all of those microservices running and basically get the same experience that you would on your machine within the sandbox.

## Testing Agents: Computer Use, Screenshots, and Real App Workflows

**Walden [00:18:08]:** Another thing that we've been thinking a lot about is like Different VM service offerings. Have you had customers where they needed like macOS specific VMs or like Windows specific

**Walden [00:18:20]:** VMs?

**Walden [00:18:22]:** There are like many technologies in the world that only work on specific types of machines, right? If you're building a.NET application that has to run on Windows or like, maybe more commonly if you want to build iOS or macOS Does that work

**Swyx [00:18:32]:** Does Commission support

**Swyx [00:18:33]:** Choices like that?

**Walden [00:18:35]:** The fundamental architecture we do, because we do the separation, it does support, but the actual work in progress is happening right now on these. Another thing that we've actually recently added support now for, it's in beta, is doing Android development. To do that, we needed to support, I think, nested virtualization within our machines because the VM itself is like a, is a virtualized Firecracker instance, and then you had to then run another Android emulator inside. And there's like weird performance issues that like, it, which is why it's like still in beta. We have to think through these problems, but it unlocks a lot for anyone who wants to do Android development.

**Swyx [00:19:13]:** I was trying to find like a reference video for the testing thing. I couldn't find it, but I think you worked on the testing, capability. Why call it testing and not like computer use or I don't know, it's, what's the general Category of problem?

**Walden [00:19:26]:** I think that when people think about the ability of an AI to run your app and test it, I think they actually over-index on the computer use part of it because computer use in my mind is the literal, okay, you want what button you want to click. Can you emit the right coordinates to go click that button? I think testing is actually a really interesting like

**Walden [00:19:48]:** Problem-solving, challenge for these AIs because if you wanted to do arbitrary testing, imagine you make a change that spans the frontend and the backend, maybe, even some other like even more deeply nested service. To actually test that change, we have to reason through what-- how do you first run these applications to orchestrate with each other with the right version of the code? Then, okay, how do I trigger the feature or how do I make the thing actually happen? And this can get arbitrarily hard, maybe you have to be an admin. Maybe a certain thing has to be feature flagged on. Maybe, you have to like run two sessions and then send us a very specific word into one of them to trigger a specific behavior. And figuring out how do you do that requires a lot of code base context, requires, a lot of orchestration that we've specifically done. And in some cases, we found that you actually, no one frontier model can actually do this full end-to-end task itself.

**Walden [00:20:42]:** We've seen cases where we actually had to orchestrate different frontier models together to solve this problem together. That is where we spend most of our time when we think about this testing problem, not so much the computer use part. Computer use for what it's worth has gotten a lot better with recent models and it's made that part of the job certainly easier.

**Swyx [00:20:58]:** Especially with like even 4.7, that they released yesterday, apparently like way better in terms of the vision stuff, which is going to be encompassing computer use.

**Walden [00:21:08]:** Having evals for all these as well is something that like takes a while to build up. And having the evals be right is tricky as well. Do you ever see like, clients who are building their own agents have to start standing up evals to make sure things don't regress?

**Swyx [00:21:25]:** Not so much evals in the traditional sense, but specific to the testing part that has just gone in. I just added support for screenshots And in theory you can also do video. I need to put in a plugin to do that. But they do show up natively, and it was a very heavily requested feature, especially after Cursor's recording came out. I think that was very enlightening for everyone of like, "Oh, this is a very good feature to actually have.", I think with Devin you guys have had this for a while.

**Swyx [00:21:57]:** Oh, yeah. See how screenshots work. Yeah, I don't know if there's anything, super and not obvious. It's like once what feature to build, you can just prompt it and it Will mostly work.

**Walden [00:22:09]:** I think to Walden's point, though, the computer use is a subset of the larger testing problem, and I think that's very specific to the code base that you're working and it's not something that, out of the box that you could just solve it. The-- you do need the code base context to actually know how to test it. And I think in the case of a background agent system, you fortunately do have that code base locally that what is changing and could then inspect it and use that to drive the model.

**Swyx [00:22:40]:** For those who haven't seen it before, this is an example of how it works. You, after the PR is done, you click testing approved, and then it sends you back a video. What I really like is that it labels, It's very small here, but it actually labels what it's testing. And then it-- and then you actually see the cursor and everything. So I don't know, yeah, the engineering in this, just Whatever you want to show. 'cause this is like, this is one of those like, oh, few of the AGI moments, right? 'cause Once I look at this, I actually don't I wish I can just merge inside Of Slack instead of going to GitHub 'cause I don't need to see the code. I know it works.

**Walden [00:23:19]:** Maybe a new feature in Cursor. Yeah, the annotations at the bottom was also a big difference for me when I, when I added those.

**Swyx [00:23:27]:** It's just like, what am I looking at? What are you trying to demonstrate?

**Walden [00:23:30]:** Exactly. There's a surprisingly long tail of small details that ends up making a big difference for this end metric of like how fast do you actually merge the code in. One experience that we spent a lot of time tuning early on was what is the right experience on GitHub for these tools. Because I think, most tools out there when you build the agent, you'll think about, oh, it'll create the PR for you. We try to take that a step further and say, "Oh, what if we actually made sure you could interact Devin, with direct Devin directly on GitHub?" And so we made sure that you can comment on GitHub, and Devin would actually receive those comments and address them back. But there's actually quite a bit of tuning you have to do here because you can imagine that actually like-We recently have Devin Review, for example. Devin Review will post comments on his own PR And then Devin has to then go

## GitHub Workflows: Devin Review, Comments, and PR Automation

**Swyx [00:24:23]:** He answers his own comments, which is Really loopy. So like, yeah, I like that it just updates here that it's, that I have commented But usually it's just me saying like, "Hey, merged, fix any merge conflicts."

**Walden [00:24:37]:** The, so when Devin fixes his own comments, you might be scared that, oh, maybe I'll infinite loop. But we've put a lot of work into making sure it doesn't, both by making sure that the comments are high signal, but also that the agent is thoughtful about what comments it immediately goes and tries to fix, and what comments it's like, "Wait a second, I think you're wrong." Actually, that's one of my favorite moments is when Devin tells me that I'm wrong, when I try to get it to do something different. But tuning that behavior, actually makes a big difference in terms of how useful the actual GitHub experience is.

**Cole [00:25:06]:** I think to touch on that as well, I think having the AI reviewer integrated into the system is a critical part of this background system. OpenInspect does have that. It has a GitHub code reviewer that you can control the prompt. It does do comments as well. It doesn't do them automatically yet. The capability is there, but it's not fully used.

**Swyx [00:25:27]:** So you have to ask for it?

**Cole [00:25:28]:** you do, yeah. You can tag it on GitHub, and then whatever you named your, GitHub bot, it will then follow up on it. It will then, if you have merge conflicts or whatever you have asked it to resolve, it will then resolve it, but it doesn't do it automatically yet.

## Integrations: Slack, MCP, and First-Party Agent Interfaces

**Walden [00:25:42]:** Well, I'm curious, what is, the most common thing that people end up requesting, that they still need on top of OpenInspect when you help them go implement it?

**Cole [00:25:52]:** I think a lot of it comes down to actually integrating it into the company. It's one thing to have the background agent system set up, but if it isn't actually integrated into your larger ecosystem, it isn't that useful. It is useful to be able to kick off sessions, but what we really want to be able to do is hook it into all of our other systems, whether that is the production database with read-only credentials, the logs, a Confluence or internal knowledge-based system. I think that is where I see the huge leap for companies, and that can be a challenge for companies as well who are maybe not familiar with exactly how to approach it, especially if they're in environments that have more compliance type things where, access control can be pretty big and how do you deliberately think about these problems, I find to be, one of the problems that comes with a system like this.

**Walden [00:26:46]:** The thing we found is So, MCPs, obviously it has been like this, really big explosion of, oh, you can go, integrate it with all these different things. But to actually get the integration right and the and get the right experience, oftentimes we found that we had to go build our own ad hoc things. I think Slack is a great example of this. You could give your agent a Slack MCP and okay, it can post messages back to you on Slack. But we actually use Devin like a coworker in Slack, and that's how it's been built from the ground up. But to do that, you actually need to, support webhooks that come back, right? And then Devin has to respond in a natural way and then hopefully don't spam your threads too much and annoy the people in your company. So you got to tune that experience just right. Especially when there's a lot of back and forths, we find that we actually have to go beyond the simple MCP integrations in these places.

**Swyx [00:27:39]:** I just pulled up the MCP marketplace. I know this is a Fair amount of work. Is the answer to eventually take first party control of all the top MCPs? Is that the

**Walden [00:27:48]:** I would love a world where you could have something that's more expressive than MCP. That, goes both ways, not just a set of tools, but a proper system that interacts back and lets it Have the right experience with all these interfaces.

**Swyx [00:28:03]:** So there actually is sampling in the MCP spec, but nobody Uses it, right?

**Walden [00:28:07]:** And so I think that's the other part is, actually we found that when the MCP spec starts to get too complicated, it starts to lose its original promise of Being like a simple one-step connect. Now then we have to go figure out how to support all these different variations of things and It starts to look a lot like just building the first party integrations in a lot of these cases now.

**Cole [00:28:29]:** I think it matters, too, how critical it is to your company, right? If this is something that nearly every session is going through, it probably makes sense to own it so that you can make optimizations on top of it Versus just whatever is off the shelf.

**Swyx [00:28:43]:** Awesome. Other than MCPs, what else, sorry, well, I don't know if that's Narrowing in too much on, integrations. But what else? What other elements of building OpenInspect or Devin that you guys really sink on?

## Memory and Knowledge: What Agents Should Remember

**Cole [00:28:59]:** I think, a problem that comes up very frequently is this idea of memories or knowledge base.

**Swyx [00:29:05]:** Oh, boy. How do you solve it?

**Cole [00:29:08]:** so not solved yet, is the short answer.

**Cole [00:29:11]:** it's something, there's a open issue for it, someone asking about it.

**Swyx [00:29:16]:** There's, I, D Wiki hasn't indexed anything about memory yet.

**Cole [00:29:20]:** how I'm seeing it solved across my clients is primarily through skills. I find that skills can be a good gap within that or updating Claude MD, but I think memory as a whole is a pretty unsolved problem, and it is why I've been hesitant to add it. I think there is parts of memory and that can be addressed, but I think as a whole it's a very difficult retrieval problem.

**Swyx [00:29:44]:** Oh my God. RAMP didn't write anything about memory? I see zero search results.

**Walden [00:29:50]:** No. Memory can be quite tricky to get right because it's the retrieval, but also the generation of the memories that can be really tricky. You don't want it to just like Remember very specific details.

**Swyx [00:29:59]:** Walk us through the Devin memory journey because I know there's been a journey.

**Walden [00:30:03]:** the first version of memory that like stuck around for a while was A system we have called Knowledge. And the idea was we wanted it to pick up things over time and not need the user to be proactive about teaching Devin things. So, okay, any time you remind Devin, "Wait, no, that's not quite the way you're supposed to use Git"Like, we actually want Devin to say, "Hey, do you want me to actually just remember this for the future?" And for you to just basically quickly approve or reject and for it to build up over time. 'Cause I find that, 95%, I think, or some crazy stat like that of the memories that Devin has are all through these auto-generated things. Very few people actually just want to sit down and write big docs on Here's how you're supposed to work with the technology, et cetera. The generation and the retrieval has been something that we've been trying to tune a lot over the years. Generation, you don't want it to remember something like, if you asked one time to like, "Oh, please open as a draft PR," you don't want to be like, "Oh, everyone forever now should get their PRs as draft PRs." But you do want some, conveyor. Maybe you want to say like, "Oh, Cole generally likes, things to be created as draft PRs." Same with retrieval, if you have thousands of these memories, how do you actually make sure they're retrieved at the right time? And that can be quite tricky to do right without exploding the context with a bunch of useful yeah, useless information. Surprising amount of just, eval work to just make sure that, memory is, remains a reliable system as new models come and go.

**Cole [00:31:31]:** Do you have anything that you could share on, memory pruning? And like the temporal aspect of memory?

**Swyx [00:31:36]:** Deleting and forgetting?

**Walden [00:31:39]:** The, today, the, So the things they could do is it could edit memories. And so if your memory used to say like, "Oh, Cole likes to open everything as like a draft PR," then you can imagine, "No, don't do that." And then it'll say, "Oh, do you want me to update the memory to be Cole now want everything as, open PRs?" I think that at the same time we don't know if this is going to be the final version of the system. Whatever we have here will probably, translate into the new system that we'll be coming up with. But I think one big difference between two years ago and today is these agents are really good at using anything that resembles a file system natively. And so part of us are, is thinking, "Oh, should we rebuild memories to feel more like a file system that we let the agent navigate on its own?" That's been an interesting exploration. Also similar ideas in the scale space.

**Swyx [00:32:35]:** I am pulling up OpenClaude's memory thing right now. So memory, OpenClaude has like this like daily memory journal thing, right? And you can I mean, that is a file system you can grep through and is a source of truth. I don't know if it's the best. It's probably super noisy, but at least, if you lose something you can discover it or you can apply some, forgetting algorithm to, more ancient memories that don't get recalled again or something. I don't know.

**Walden [00:33:01]:** One thing we've been trying to do to push the boundaries of how you use agents at your company is letting an agent basically have a very similar file, a memory.md or something, and just like be your permanent PM for a specific set of issues maybe. So we have like some Slack channels internally, maybe a Slack channel dedicated to, a specific product like DeepWiki maybe. And you can imagine that, or you want a Devin that never stops, it's just always awake, but it has this like memory dock that it can just maintain for itself about, okay, what are like the number one priorities of what we have to fix and prioritize? Who is responsible for some upcoming work? Maybe they'll even Devin will even tag you on some recurring basis. And so it's been an interesting move to see, okay, how can we actually use Devin for more than just engineering? Can we actually upstream above the engineering process and maybe it's just Devin creating tickets, which then maybe some humans do, but then maybe other Devins do.

**Swyx [00:34:00]:** One of my more fun automations is go research competitors and just suggest stuff to me on a weekly basis. That's the automation. I can't find it right now, but basically it just like, "Look at competitors and suggest things." "And here are three things that you've suggested that I don't want any more of," and you just stick that in the prompts. But like I wish actually So for like when I, for example, when I reject a PR, I wish that it updated memory so that I can then just not have to go up, go back and update the scheduled, sync, but anyway, feature request.

**Walden [00:34:31]:** what? We might change it soon. I guess OpenInspect, in the time you've been around, has there been anything you tried to implement but then you had to like undo and like do a different way?

## OpenInspect Architecture: Webhooks, Control Planes, and Agent State

**Cole [00:34:41]:** Nothing yet, but something that is on my mind. The initial way that I built it was that each of the integrations lives as its own package. And so you have The Slack bot, which is what's handling the webhooks, and then is basically interacting with the control plane. As I'm seeing the system starting to be more integrated, specifically with the GitHub bot integration, I'm considering bringing that all into the central control plane because especially now I want to start, And a request that I'm getting is the ability to monitor, the actual, pull requests being merged, as well as just tracking of

**Swyx [00:35:19]:** What do I have open?

**Cole [00:35:21]:** What do I have open? How many of these are getting merged? How many comments are showing up? To just understand the health of the system. And so in the case of a GitHub app, you only have one webhook. And so then it's a question of do I put that webhook in that GitHub bot package? That's weird. It doesn't really make sense to live there because that package is more for like the code reviewer. Or do I like centralize it? So that's something that's on my mind of, making that decision. I think the other one we touched on earlier is the harness in the box versus out of the box. I think long term the architecture will eventually come back out of the box. Some of the newer tools that I've added are calling back into the control plane so that you don't have the secrets in the sandbox. And so I think long term I probably will pull the actual, agent out of the box, but I think for now it's fine.

## Subagents and Multi-Agent Systems: When Parallelism Helps or Hurts

**Swyx [00:36:16]:** Just, a quick question on pulling the agent out of the box. I'm One thing I'm very bullish on this year is agents calling other agents or spawning sub-agents or Whatever you want to call it. Does that make it harder or easier? I can't tell. Because if the harness is in the box, you can just spin up more boxes. If the harness is outside the box, then you're, it's less easy because you are, you have a unicorn pet of a, of a harness that's, living outside the box.

**Cole [00:36:45]:** In theory it would be the same way, right? Whether, one agent has launched many, sub-sessions within it, OpenInspect, for example, can launch sub-sessions and actually create other environments and then monitor them. In the case where it is out of the box, that would basically just be an additional session that's running. And so that session is also running outside of the box. It's running in your worker plane, wherever you're running this. And then you really just have to think about how does your top level agent then interact with it. I do think it can be more complex, just 'cause again, you have now a more difficult architecture. But I think if you figured it out once, it's probably fine.

**Swyx [00:37:26]:** Well, then I'm just, throwing it open to you in terms of, I call this like meta Devin management. Which is like the, Devin's calling Devins or Devin scheduling Devins or querying trajectories or anything like that. What have you built or unshipped, anything?

**Cole [00:37:46]:** I think one of the surprising things we've seen is that a lot of the ways that, these, separate agents work with each other, and you want them to, parallelize their work, has still mostly followed the same manager sub-agents regime. And a lot of people I think are excited about this world where you have swarms of agents that, talk with each other all over the place. We've actually given Devin an MCP so they can just go arbitrarily message other Devins And create new Devins, et cetera. But I guess, it somehow creates, a really chaotic world in that sense. And so we've still found that most practical use on a day-to-day basis has been one single Devin.

**Cole [00:38:33]:** Figuring out how to segregate the work and get, have other Devins work on it in, a relatively isolated sense, each with their own boxes Not sharing machines, so there's, a very little room for conflict is the regime that you have to create today.

**Swyx [00:38:50]:** I'll call out, the experiments from Cursor, right? This is Wilson Lin's work on Single agent to multi-agent, and you're obviously famously on the side of don't build multi-agent. But they went through the whole thing, only to arrive at, this Which is exactly what Devin has, I think.

**Cole [00:39:08]:** I think there will be a revision to that post at some point About

**Swyx [00:39:12]:** Tell us about it

**Cole [00:39:12]:** I think multi-agents were very much not at all possible a year ago. You do see more multi-agent experiments today, but you can argue, are they really multi-agents, or are they just just, tool calls,? There are people who, will create sub-agents to go look for XYZ file, XYZ implementation. Has really nice context management benefits because all of the tool calls and tokens that it spends then get collapsed back to just the answer for the main agent. There's a lot of benefits to doing this. We basically have Devin do this with Deep Bookie, make a call out to Deep Bookie, give you back the results, but that feels like a tool call,? It's not like these, two collaborators actually talking back with each, back and forth with each other. But I think the thing that gives me the most bullishness that multi-agents might actually be possible is actually what I said earlier about Devin will actually sometimes tell me I'm wrong and push back, and I think that demonstrates a level of maturity and communication today that makes a multi-agent world possible. One, can two agents who have seen different information come back to each other and actually figure out who is right, what is the correct implementation? They're not just, yes men. Claude, I guess is like, used to just say, what is it? "You're right," or,

**Swyx [00:40:25]:** "You're absolutely right."

**Cole [00:40:26]:** "You're absolutely right." Yeah.

**Swyx [00:40:28]:** The Have you seen, did you see

**Cole [00:40:29]:** The age is over

**Swyx [00:40:30]:** The Codex app troll in Topic? This is the Codex app. Inside of Settings, there's a little, there's a little Easter egg, right? So if you go to, the Themes or Appearance, right? There's all these, color codes, and the top is absolutely, and it's the Topic's colors. Which is such a troll. Anyway.

## Model Behavior: Pushback, Adversarial Prompts, and Agent Skepticism

**Cole [00:40:53]:** I love that Easter egg. Did you discover that yourself?

**Swyx [00:40:54]:** No, it was, someone was, tweeting about it And I was like, I was like, "Is this true?" Because, sometimes people just tweet stuff to, get a rise out of you. But yeah, there you go, in Topic colors.

**Cole [00:41:06]:** Yeah. So yeah, we're out of this regime where, it just says you're absolutely right, and they can have real conversations and real back and forths.

**Swyx [00:41:13]:** You can prompt it as well to be more adversarial or whatever. Yeah. Okay. Yeah, that, I mean, to me, that is more intelligence, right? That is not just something that's, a dumb tool, it's actually pushing back on you I think. Yeah.

**Cole [00:41:24]:** when you mentioned, of course, the blog posts. There was one blog they had where they fed a swarm of agents together and built a browser.

**Swyx [00:41:34]:** That was I think that was the one.

**Cole [00:41:36]:** You can have, like

**Swyx [00:41:37]:** I think it's the same one

**Cole [00:41:37]:** Creation of it. We found a surprising success of, don't do a swarm or anything, just have one Devin, it does its own context management. Just let it keep running for a while and give it some crazy tasks. I think we asked it to, rebuild, a Windows OS system. And it managed to do it just like, going on for long enough. It's

**Swyx [00:41:55]:** Was this Andrew's thing?

**Cole [00:41:58]:** there were lots of demos that we ended up not posting, 'cause at some point we'd just be posting way too much a bunch of, Demos. But I love that because it shows that I think the multi-agent thing still has, a bit of exciting sexiness to it, which is maybe still beyond still, the actual delta it adds to the capabilities of these systems. But it's absolutely the future. I think we're heading in that direction and we can see the progress being made there already.

**Swyx [00:42:25]:** If I were to, make one super minor pushback because I don't feel that confident about it yet

**Cole [00:42:33]:** Go for it

**Swyx [00:42:33]:** But I've had Ryan Lopopolo from OpenAI on the pod And he's a super slop cannon, right? Oh my God, that's my coding agent being done. I downloaded this, Peon Ping. I don't know if you guys have heard this. It takes like-, sound packs from popular games like, Command and Conquer and Warcraft, and then it plays it whenever it's done. And so it's like, "Work," or whatever, "At your command," or something. Anyway, what I got from the Cursor code base and from Ryan's thing was that there's a slop cannon approach where you try to loosen the single agent's, bottleneck, and I feel like that is, probably an, a very important thing to try to figure out. I don't think anyone's, really solved it. Because then you just have more reviewer slop on top of the agent slop To try to wrangle it all. Ryan will probably very strongly object that I say that he hasn't solved it, but he thinks he's He thinks he's completely solved it. But I think it's still I think it's, very important, 'cause, that is a bottleneck, right? I feel Devin is slow sometimes Because I'm like, well, yeah, this is very readable and very sensible, but also it is slower than it could be if I just, I want a button to just say, "Just ramp this up 1,000 next parallel, in parallel and just, see what happens,"? And I don't know if that's, feasible at some point in the future.

## Code Review, Entropy, and AI Slop

**Walden [00:43:55]:** I And we've also run experiments internally where we've basically tried to build entire products, true products that we knew we would eventually ship, but for now, let's try to see if we can do it just by purely, vibe coding on top of each other, auto merge, no code review at all. And then there's this benchmark of how many weeks can you go onto this for Before you say, "We have the trashiest code base."

**Walden [00:44:18]:** "Let's actually rewrite it from scratch."

**Swyx [00:44:19]:** Start a new factory, yeah. What'd you find?

**Walden [00:44:21]:** I think we found that the state-of-the-art in December was you can probably, run this for about two weeks. By the end of those two weeks, you'd find that, hey, you want to, change the color of a button. Well, it turns out this button is implemented in, 10 different places, and they, have All these different variations, and oh, you forgot one of them, and actually it's a slightly different color in one spot. And you're like, "Okay, this is too much to work with. Let's actually try to do code review at the same time." And make sure that we're on top of our software, actually cleaning it up a bit And making sure it's done in a scalable way.

**Cole [00:44:54]:** I think building on that, the idea of, you don't have to look at code, I think is generally a bad idea. And the meme that I have for that

**Walden [00:45:03]:** What timeline, all right, is Do you think that statement will be true on?

**Cole [00:45:06]:** I think probably for a while it'll be true that you should continue to look at your code. A problem that I see a lot of teams run into that I work with who are embracing AI native, AI first coding, is The meme that I have is that your code base regresses to your worst engineer, because that engineer who is, very gung-ho about AI and is not auditing their code, their pattern starts cementing into the code, and now the AI is referencing their patterns. And so now their if/else block that, is 20 if/elses back and forth, the AI is seeing that as the pattern of how things are done and starts to then exponentially grow this slop. And I find to your point, a pretty good approach to that is having scheduled cleanup, whether by humans or through systems, that are looking for duplication. They then address that. You'll end up with like 12 helpers for how to format a date. And you need to address that, because otherwise it will continue to sprawl.

**Swyx [00:46:09]:** Within balance, I think it's fine to have some duplication, and then sometimes To have garbage collection, right? Yeah. The What I've been, talking about with a lot of engineering leaders is that you want to be very strict about the boundaries between modules, and it's your job as an architect, as a CTO, whatever, to say like, "Okay, here's the hard contract between you guys and you guys. Whatever you do inside this black box is your business. You do whatever. But between these guys, let's be, really damn clear, and any movement must be signed off by a human or me," or. Then, and like that's that. I don't know if you have any other modifications or advice.

**Walden [00:46:44]:** Well, I guess generally on the topic of, where humans can be useful, I found that 'cause, some of these, really deep infra problems, sometimes just having a human that just has, really deep expertise can make a big difference. I've actually seen this come into play when actually building agents. So we've had a few friends now, try building their own coding agents, and I think one same problem that I recurringly heard a lot of them run into was this problem of like, "Oh, Grep is really slow on our agents' machines." And so a lot of them, I assume because they're using AI and they themselves don't have, super deep infra background knowledge, say, "Okay, we're going to go build our own custom Grep index. It's going to be really fast," and use that as a way around this problem. When we ran into this problem About like, maybe like a year and a half ago when we were, in the early days of building Devin, we obviously didn't have AI then. We just asked our, how to, how to do this. You can just swap out a new Grep index, so.

## Infrastructure Details: Grep, File Systems, and Sandboxes

**Swyx [00:47:45]:** What do you mean you hand-coded Devin? What?

**Walden [00:47:48]:** It's like, can you believe we hand-wrote this code? And we had, our infra people who are really amazing, they were looking into it and they're like, "Oh, what? We realized that actually the root cause of this problem is actually super simple, but like fine-grain detail," which is that a lot of these virtual machines actually underlying them don't use real file systems. They use these, network file systems where things are actually cached over the network actually in S3. So when you're Grepping, you're actually making network calls Every time you're doing these things, and that's why Grep is extremely slow on these machines. And so again, goes back to, what is all of the crazy infra work that we had to do to actually get these machines working. If you try to do this yourself, there are tons of small details like this, and so we had to eventually go swap out that network file system. But

**Swyx [00:48:35]:** I think there's a write-up about it, right? Silas did one about the virtual file system.

**Walden [00:48:38]:** Oh, that was a whole other thing. The

**Swyx [00:48:39]:** Oh, that's a different thing

**Walden [00:48:40]:** The BlockDev file storage format

**Swyx [00:48:42]:** I'll bring it up

**Walden [00:48:42]:** Which is, a file system format that we built so that the VMs could be spun up and down very quickly. Basically, the intuition behind this is-Imagine you have, a terabyte of disk, and your agent only, wrote, a hundred lines of code on top of that disk. How long does it, say, take to, save and re-bring up that disk? And most systems, because you're not optimizing for this case, it's just, on the order of a terabyte of work because you have to Save all of that and bring it back up. In our system, we try to build a file system that incrementally builds on top of each other. So every time you save and bring the machine back up, you're only doing work that is proportional to effectively the diff in the file system. And so this, shaves off a lot of time in the boot-up process of Devin. I think we This is actually now outdated. We have a newer system inside of Devin. But yeah, there's a lot of tiny details you have to get right here to actually get the day-to-day experience of Devin to be good.

**Swyx [00:49:39]:** It's, not technically agents, but it is agent infra, and when you sell an agent as a company, you sell agent plus agent infra.

**Walden [00:49:46]:** At least the way we do it be And the other The nice thing about having the agent infra being done together is, you We get to deploy Devin in whatever environment we want now. We don't need to wait for some underlying infra provider to also go and support VPC or on-prem or FedGovCloud, for instance. So we can actually go and figure out, okay, since we own the infrastructure, how can we get that set up for you?

## Cloud Providers: Modal, Daytona, and Enterprise Sandboxes

**Swyx [00:50:12]:** Whereas you're Cloudflare dependent.

**Cole [00:50:15]:** so Cloudflare runs the control plane. The sandboxes, Modal is supported. A contributor just added Daytona. E2B is on the roadmap, and I think there's an abstraction in place that if any contributor wants to add a new provider, they can add that in.

**Walden [00:50:32]:** Well, what are, How are the customers you work with Do they generally try to then go set up a contract with another one of these third-party providers? Do they try to do the VMs in-house?

**Cole [00:50:44]:** most of them I see using Modal. I think Modal has a great

**Walden [00:50:48]:** Shout out Modal.

**Swyx [00:50:48]:** Shout out Modal.

**Cole [00:50:50]:** I think Modal has a great offering. It captures all of the sandbox pieces you need, snapshots being a pretty big piece of that, and given that they also offer GPUs, I think it's a pretty nice offering as a whole.

**Swyx [00:51:04]:** no debate there.

**Walden [00:51:07]:** Modal is great, especially, I think their container offering is, the most natural, and so especially if you are willing to, forego, the full VM requirements Modal is, a really vast place you can spin something up on.

**Swyx [00:51:20]:** Is there a point So Modal's very Python, and I feel like most workload, has really shifted to JavaScript. I don't know if you guys Get the same feeling. So, okay, when I started Landspace and IE and all these things, I was like 50/50 Python and JS, right? That's roughly. I think that's wrong now. I think JS has won. I don't know if you guys Like, I Maybe I'm overstating it, and maybe for cognition, there's, C# and Java and what have you. But for, new greenfield apps, do you feel that Do you get that sense? Does it matter?

**Cole [00:51:52]:** I think that most of the libraries that I see in this space are Python native first, especially in the

**Cole [00:51:58]:** Observability space. That said, I think that there is a pretty big appeal of having your entire system in one language. Especially when you have both your frontend and backend communicating, you can have one central type Which is very nice.

**Swyx [00:52:11]:** That's my case against Modal, which is Then you have to run JS. You can run JS inside Modal. It's just, one extra step That, isn't native to the runtime. I don't know if

**Walden [00:52:22]:** I don't know

**Swyx [00:52:23]:** Reviews. Do you have numbers? I don't know.

**Walden [00:52:25]:** the one thing I don't like about Python is whenever AI, whenever it writes Python, it always does, the weirdest patterns, and

**Swyx [00:52:32]:** Oh, because it's, mixing two and three or what?

**Walden [00:52:34]:** I think it's something mixing two and three, yeah. The I don't know if you see this. It always tries to do, has attribute on objects as like

**Cole [00:52:41]:** Oh, my God.

**Walden [00:52:41]:** But it's like But that you shouldn't be doing that. It should error if there was

**Swyx [00:52:45]:** Because it's training on library code?

**Cole [00:52:47]:** I think it's more of, like

**Cole [00:52:48]:** From what I've seen, it's more of, a reward hacking mechanism where it doesn't want to basically

**Walden [00:52:54]:** It'll never error.

**Cole [00:52:54]:** It doesn't want the code to fail. And so it Even when it knows it has the attribute, it'll call getattr on a, and for a lot of my clients who have moved towards more autonomous coding, we've put that in as a lint rule That if you do getattr, your pull request is going to fail.

## Slop Signatures: Comments, Backwards Compatibility, and Types

**Swyx [00:53:12]:** Ooh, this is a fun topic. Can you tell me more about this? What else is a sign of AI coding that you have to put guards in?

**Walden [00:53:21]:** So we were talking just before this about Opus 4.7. One of the things this new model likes to do is it writes lots of comments. Not like, it'll, comment every line, but it'll write, paragraph, PRDs, on top of every function. But I will say, to its credit, these aren't slop, descriptions like they were before. "Oh, here's what this function does." It's like, "Oh, here's actually the reasoning and why we chose this approach and what the alternatives were and why we shouldn't do those alternatives." Still too much information, but I wonder if this actually might be directionally correct if you want systems that can self-maintain themselves in the long run.

**Swyx [00:54:04]:** Oh, they write the specs inline.

**Walden [00:54:05]:** Have all the context In the code as well. Yeah.

**Swyx [00:54:07]:** So you approve?

**Walden [00:54:09]:** I But at the same time, it's this tricky problem. Maybe we'll just give our users, a setting or something, for, how verbose you want it to be. I haven't loved it. Honestly, I just I like the comment, but please, get rid of it. But I could, I could see a world where maybe something of the sort becomes reality. I don't know If you guys know about GitAI. So

**Swyx [00:54:32]:** We've talked about it, yeah.

**Walden [00:54:33]:** GitAI, the idea behind it is

**Swyx [00:54:34]:** I'll bring it up

**Walden [00:54:35]:** That if you run an agent, the actual prompts you send to the agent should be stored alongside the code inside the Git metadata so that future agents can reference it, maybe code review bots can reference it. And it's ideal world where, your context for why decisions were made constantly lives aside, beside your code. And so it's, maybe a more hidden version of this, write massive PRDs for every comment approach.

**Swyx [00:55:01]:** I'm waiting for the real bull case where we just get rid of Git altogether. We're not I'm not, I'm not there yet, but I'm looking for it because that would be a big shift.

**Cole [00:55:11]:** On the topic of, visible slop, a pattern that I see a lot of across GPT models specifically is backwards compatibility, at all costs

**Cole [00:55:21]:** Where it's doing these weird import exports so that it doesn't have to modify, the names of where the modules were. And I've seen Claude 4.6 starting to do this as well.

**Cole [00:55:33]:** And again, I think it is this, reward hacking behavior where it doesn't want failure to occur, and you can address that through, Semgrep or other tools where that behavior is pretty easy to identify. But it's something that you only learn through the trade of just seeing code patterns. Untyped tuples are a really big problem of just, again, just throw any in there, dict string any. And again, you can address those through linting.

## Local Testing, Mock Servers, and AI-Ready Codebases

**Swyx [00:56:01]:** Awesome. Yeah. Any other So, linting, any other tools? Devin Review, of course. Not so, not so free now, but still use it.

**Walden [00:56:10]:** Well, the one thing that I think we try to recommend teams as they use more AI agents, it goes back to this, local testing thing. In the end of the day, you want your agent to be able to do the full thing, not just write the code, but actually run it and test it. And a lot of code bases were not necessarily built for this from the start. For example, you probably do want a local DB setup, a local Docker Compose and Postgres in order to have it so that you don't need to give your agent any crazy product credentials to actually run and test its code. We've also internally done a big shift to make a lot of our core, components of code testable as purely local dev without needing to actually, integrate with, any live services for this reason. And honestly, the older the company, the more you have to change to shift in this direction. But you can use AI to help you perform this migration nowadays.

**Swyx [00:57:02]:** The older, the older the company, the more you have to change in order to do local dev?

**Walden [00:57:05]:** I think so.

**Swyx [00:57:06]:** Or am I misunderstanding? So you're saying

**Walden [00:57:08]:** Or often times

**Swyx [00:57:08]:** Most people just build with full integration to all their stuff, and there's no code path to switch it to local.

**Walden [00:57:14]:** Especially in, when there's, lots of different services and you have, microservice architecture, making that shift, the larger the code base, the harder it is. I guess if you did build it correctly from the very start, I think it'd be possible. But also, a lot There are a lot of companies in the world that got started before Docker was a thing, and so You're forced to make a migration at some point.

**Swyx [00:57:35]:** Well, Devin's good, very good at making mock servers. Right? So, And no, the Well, one of the projects that I really want to It's like, it's like Little Snitch. I don't know if you guys have heard of this.

**Cole [00:57:44]:** I run Little Snitch on my computer.

**Swyx [00:57:46]:** It's just like There's, a man in the middle, but it, shows you all the traffic going back and forth. But then from there you can reconstruct the server, right? And then, and then, create local mocks so you can local mock everything if you just observe traffic for a little bit.

**Cole [00:57:58]:** That's an interesting idea.

**Swyx [00:58:01]:** cool. I don't know if this will get anywhere, but I wanted to maybe talk a little bit about the CloudCode, leak because usually if I have an Anthropic person on, I can't talk about the CloudCode leak. Did you guys learn anything from CloudCode? I

**Walden [00:58:19]:** So if I say

**Cole [00:58:19]:** This is the first time I've seen it

**Walden [00:58:19]:** I was not that, interested in the Leak. We didn't spend that much time on it

**Walden [00:58:24]:** If I was to say, but

**Swyx [00:58:25]:** I'm just, I'm just, fishing for

**Cole [00:58:28]:** no, I didn't really,

**Cole [00:58:29]:** Research too much into it.

## Windsurf, Local Agents, and Cloud Agents

**Swyx [00:58:30]:** Fair enough. Okay, one more last thing before we go. Windsurf 2.0, you guys shipped another thing. So The meta context is you use background agents enough, sometimes you're going to want to bring them to foreground. And that little, hands-off from local to cloud is hard to work on. And then And Devin has Or Cognition has just done it.

**Walden [00:58:50]:** I think for me the biggest, gap this is trying to close is, again, how do you make the testing process as fast as possible? When it can test on its own and send you a video, it's freaking magical. Sometimes there are just really difficult things you can that you do just need to, pull down locally. And we just want Windsurf to just be your, local command center of all your agents, your background ones, your local ones, and you can imagine, "Oh, okay, this agent needs me to review something. I'll pull that down, move my other agents to the background, go test it. Okay, boom, done. On to the next one," right? You have some issue you got to fix in the background, just click, approve. Okay, set up, start a background agent to go fix it. I'd love a world where I don't have to leave this window. Then maybe the other window I got to figure out how to stop spending so much time into Slack, but maybe, someday We'll want to get those tools all.

**Swyx [00:59:38]:** And does that require the binaries to be exactly the same for local versus cloud?

**Walden [00:59:46]:** So the funny thing here is that the behavior between local agents and cloud agents, I think is actually a bit different In their ideal state. I think local agents, you want them to be a bit more fast and let the user make the call on things. Actually don't try to autonomously go test things. The background agent mode where you go start it off, I think the agent should just assume the next message I send a user should just have everything that the user needs from me and not run and stop Keep running and don't stop until you have the testing Until you have full report.

**Swyx [01:00:19]:** So that's a, that's just a slightly different prompt.

**Walden [01:00:20]:** But for many reasons, because of all the work we do to make sure that Devin works with different Git providers, that it works with different, OS's and VM's, we want as much of that logic to be shared as possible. So for our own practical purposes, we try to share as much of it as possible.

**Swyx [01:00:36]:** Yeah. I mean, I can't imagine how much work it is to, transition back and forth, so congrats on shipping this.

**Swyx [01:00:45]:** okay. Anything else that we should cover before we, wrap? Just whatever you guys were talking about in your lunch.

**Walden [01:00:52]:** maybe, use cases. What are your, do you find to be, the biggest things that your clients are trying to do with their cloud agents today?

**Cole [01:00:59]:** Do you want to just ask it again so we can get, a clean cut?

**Swyx [01:01:02]:** Because he was drinking his water. Yeah.

**Walden [01:01:04]:** The thing I wanted to talk about was use cases. What do you think are the main things that your clients come to you today about, "Hey, this is why we want to go set up cloud agents"?

**Cole [01:01:15]:** I think the easiest and most common use case I see across everyone is SRE use cases. The idea that whether we have our alerts in Slack or Datadog or wherever they're going, we want the agent to be the first responder on that. And that doesn't necessarily mean that the agent is actually resolving the issue, but just being able to collect that context ahead of time is huge. Because again, that agent is integrated into the production logs, the database. It has full visibility, and over time, playbooks as well for how to address certain issues. And so that's a huge win for teams because instantly you can have a full trajectory of what is going on within the system, and oftentimes actually a pull request directly from that, which is a pretty neat flow to actually experience of, error pull request done. OpenInspect does support a trigger for that as well, so that could happen completely autonomously.

**Swyx [01:02:09]:** From Datadog specifically, or just

## Use Cases: PMs, Support, Security, and SRE

**Cole [01:02:11]:** it supports Sentry, it supports a generic webhook, and if someone wants to add Datadog, they can. The other use cases that I see, are for non-builder use cases, whether that's the PM or the marketing team. I'm seeing a lot of, teams where the idea of who's actually contributing code is starting to change. And in a lot of cases, the PM, if there's just a quick bug fix, the PM is not creating an issue anymore. The PM is just prompting through Slack, and the pull request is then being created. And so I think that's a huge win. I think that trend will continue, where we're seeing, code modifications happening outside of engineering. The last common use case that I see is customer support. And so where they're experiencing an issue with a customer, they're not entirely sure why this behavior is happening. Previously that world was, "Hey, there's a bug when they tried to use this feature. We don't know what's going on." Well, they're now tagging that in Slack. Again, that entire full context is ready. They can then just tag in engineering and have a complete understanding of that issue and completely bypass the previous pain points of like, "Oh, can you get more information from them?"

**Walden [01:03:24]:** The only things I'd add on top of that I think I've seen is, continual security scanning Continual security review Is a very big one as well. The SRE use case, internally we think about it as auto triage Because we just want every message that comes in, and that's an alert, that's a bug report, to have Devin just start triaging it before anything else. And we've leaned into this use case so much though that we've basically tried to make it so that you don't ever have to leave Slack to interact with this. So again, making the interactions with Devin super fluid from the moment the report comes in to it responds to a report and be able to ask it questions right there with full code-based context about all the issues. Very related to customer support as well, I think one thing that we found is CLIs can sometimes be, very difficult for people who aren't technical to go and use. But an online chat interface that anyone can go and ask questions and is super intuitive and doesn't assume you have any technical knowledge but does have access to all parts of your code base, super useful For support, for salespeople, anyone who might need to have their questions answered about the code base. So yeah, great callout.

**Swyx [01:04:32]:** This might potentially be, a very expensive, use case. Is there like a rule, sense, a rule of thumb on, how much people should spend on this? 'Cause, you have unlimited budget, but not other people don't,? I don't know if this is an answerable question because obviously it depends on, a lot of factors. But I guess, like

**Cole [01:04:51]:** I think it depends really on, how people are using it. I think If people are using it responsibly and they're getting value from it, then, you can kinda determine the budget. Common numbers that I hear are anywhere from 1,000 an engineer up to 5,000 an engineer. I have not heard anywhere in the realm of, 50,000 an engineer for a frame of reference.

## Model Costs, Smart Routing, and Frontier Tradeoffs

**Swyx [01:05:12]:** We'll get there.

**Walden [01:05:13]:** I've seen, I've seen numbers go that high for sure. I think that this is also I think going to be a big theme of the coming year, is we're going to see very expensive, very smart frontier models, And we're also going to see people who say, " what? I don't need the frontier anymore for a lot of the work I do," because some frontier models actually are good enough For a lot of the work.

**Swyx [01:05:36]:** Also shout-out you pioneered Smartfind Which is a mix.

**Walden [01:05:39]:** I'm really interested in a world where you basically have hybrid frontier and subfrontier systems Where you use the subfrontier part to be really fast, really efficient, and call out to the frontier part of the system so that you can still get frontier performance for the most part.

**Swyx [01:05:54]:** I'm trying to search, but Twitter search is, completely broken. I, it's, the from field is just completely gone. It's very sad, Because I really want to

**Walden [01:06:04]:** No worries. I might have to make a new post at some point about the return of Smartfind.

**Swyx [01:06:10]:** Anthropic has now officially adopted it. Okay, cool. I think that's it. It's really great discussion and good, great having you guys on. Background agents are a thing now, and everyone's building them. We, but we talked a lot about, the production concerns and like, well, why you would want to offer one architecture over the other. Yeah, lots to look forward to.

**Walden [01:06:35]:** There's a real zeitgeist in the space right now I think, for companies to want to turn themselves into these autonomous coding factories. And yeah, we're doing a lot to try to support that. And so, any listeners are welcome to come chat to us about that, whether using Devin or working with us.

## Wrap-Up: Hiring, Consulting, and Agent Adoption

**Swyx [01:06:51]:** Hiring?

**Swyx [01:06:53]:** what, specifically, just like give like one profile that's, very interesting.

**Walden [01:06:58]:** I think people underestimate the role of, really high-taste product engineers In this space right now.

**Swyx [01:07:05]:** And the test is, what have you shipped end to end that is A tasteful product.

**Walden [01:07:10]:** If you've shipped stuff that you think is tasteful and you're, and you're proud of, you should, you should come talk to us.

**Cole [01:07:15]:** For me, any businesses that are looking to further their engineering org, a lot of the consulting I do is around that. Teams who are maybe starting their AI journey, whether that's with Cursor or Claude Code, but they're looking for someone to help navigate them through the state-of-the-art and beyond just that initial deployment. As mentioned, there's a lot of lift from you've deployed the background agent to how do we actually get this fully integrated into the company and really realizing the true value of that.

**Swyx [01:07:45]:** Okay. Well, thanks you guys for coming on.

**Walden [01:07:47]:** Thanks for having us.

---

## [[AINews] Cognition raises $1B in $26B Series D](https://www.latent.space/p/ainews-cognition-raises-1b-in-26b)
*🔬 Latent Space | 2026-05-28*

We last [wrote about ](https://swyx.io/cognition)**[Cognition](https://swyx.io/cognition) in [September's $10B Series C](https://news.smol.ai/frozen-issues/25-09-08-cog-smol.html) **when Smol.ai also joined Cognition and AINews was eventually [moved here to Latent Space](https://www.latent.space/p/2026). 8 months later, it is [worth 2.5x more](https://x.com/cognition/status/2059660758531940856), and officially the largest [remaining independent agent lab](https://x.com/swyx/status/2059717021944926238) in AI, a thesis we [mapped out last year](https://x.com/swyx/status/1990886806250782876). With official ARR disclosures (now [projecting >$1B ARR by EOY](https://www.youtube.com/watch?v=VuyOy5WN980)) you can map out the growth, which looks oddly similar to the [WTF Happened in 2025 charts](https://www.latent.space/p/wtf2025) (this [isn't a coincidence](https://x.com/swyx/status/2057119153337545096)):

[](https://substackcdn.com/image/fetch/$s_!l_fo!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc283a27b-c506-4ee9-8b9a-47650b429a01_2534x1694.png)

In the enterprise SaaS business, ARR is a trailing indicator of utilization, as are the logos of some of the toughest/most discerning customers in the enterprise and startup ecosystem (including [Exa and Modal](https://www.latent.space/p/ainews-new-ai-infra-unicorns-exa), featured last week)

[](https://substackcdn.com/image/fetch/$s_!i6tW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa1563dd3-9a40-45b1-9060-7ec196bf8e77_1316x1616.png)

We will release more on the Cognition podcast tomorrow.

> AI News for 5/26/2026-5/27/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

# **AI Twitter Recap**

**Inference Efficiency, Serving Architectures, and Cost Curves**

  * **Inference optimization is increasingly architectural, not just kernel-level** : [EAGLE 3.1](https://x.com/EagleCorp/status/2059485457227149334) improves speculative decoding robustness by stabilizing hidden-state feedback and reducing attention drift at deeper decode steps, with explicit emphasis on **long-context acceptance length** and real-world serving reliability; the team also highlighted collaboration with [vLLM](https://x.com/vllm_project) and TorchSpec. At the kernel/system layer, Perplexity open-sourced a rebuilt [Unigram tokenizer](https://x.com/perplexity_ai/status/2059664738087469511) that cuts CPU utilization **5 -6×** and reaches **63 µs at 514 tokens** with zero heap allocations, while [Qwen3.5 on TokenSpeed](https://x.com/Alibaba_Qwen/status/2059674574397313277) reportedly hits **580 tokens/s** for agentic workloads via joint optimization across Alibaba, LightSeek, NVIDIA, Mooncake, and FlashAttention-4 contributors. Supporting libraries also improved: [MaxSim v2](https://x.com/ErikKaum/status/2059659837219156453) adds backprop and reports **10.33 × faster on H200** and **11.94 × on A100** versus naive PyTorch.

  * **Price cuts are being justified by structural KV-cache and attention changes** : Several posts converged on the same theme: recent API price cuts from Chinese labs look sustainable because they reflect **lower serving cost per token** , not temporary subsidy. [@kimmonismus](https://x.com/kimmonismus/status/2059578380329394292) summarized how **DeepSeek V4-Pro** uses hybrid attention with **Compressed Sparse Attention** and **Heavily Compressed Attention** to bring **1M-token KV cache to ~10% of V3.2** and single-token inference FLOPs to **27%** , while still routing **49B active params** out of **1.6T total**. Xiaomi's MiMo similarly reduces cache traffic using SWA plus hierarchical cache management. That was corroborated directly by [@_LuoFuli](https://x.com/_LuoFuli/status/2059618247553745204), who said MiMo's deepest input-cache-hit price cut comes from **5 × cached token capacity**, roughly **80% lower caching cost** , and an architectural **1:7 Full:SWA sparsity ratio**. The broader takeaway: long-context inference economics are now being pushed by **attention design + cache hierarchy + routing** , not just cheaper hardware.




**Agents, Harnesses, Memory, and Continual Learning**

  * **The stack is shifting from "model quality" to "model-harness-memory fit"**: A substantial cluster of tweets focused on practical agent engineering. LangChain shipped [Deep Agents v0.6](https://x.com/LangChain/status/2059634226836746483) with **Delta Channels** , cutting checkpoint storage for a 200-turn coding session from **5.3 GB to 129 MB** , and also launched [computer use in Fleet](https://x.com/LangChain/status/2059685293322858809), plus [Context Hub](https://x.com/hwchase17/status/2059687279199924462) for versioned agent context/skills. [LangSmith Engine](https://x.com/LangChain/status/2059654417478012938) was framed as automating the eval -> diagnosis -> fix loop, with multiple practitioners emphasizing its value for turning trace feedback into reusable online/offline evaluators. In parallel, [@Vtrivedy10](https://x.com/Vtrivedy10/status/2059712077925658717) made the clearest formulation of the day: **task-harness fit** matters as much as model quality, and bespoke vertical systems outperform generic harnesses by narrowing tools, prompts, and context to the task.

  * **Continual learning is re-emerging as a product category, not just a research topic** : The biggest announcement here was [Trajectory's launch](https://x.com/rronak_/status/2059644771262730624): a platform for using **product usage signals and agent traces** to continuously post-train large agentic models, with **$15M in funding** and design partners including Clay, Harvey, Decagon, Mercor, and Rogo. Baseten said it supports these deployments with [FP8/NVFP4 quantization and autoscaled H100 infra](https://x.com/baseten/status/2059651376565936510#m), including a cited overnight deployment of a **397B-parameter model**. The same trend appeared in open tooling: [an open-source memory-centric agent](https://x.com/hwchase17/status/2059487107144655356) built on LangChain/LangGraph was praised by multiple builders for explicit retrieval/storage/reasoning/learning separation, and [RLM's minimal training harness](https://x.com/a1zhang/status/2059633834094678173) shows small teams can now RL-tune long-context agents in **a day on 8 ×A100**. The throughline is that "post-deployment learning" is moving from aspiration to infra.




**Benchmarks, Scaling Laws, and Training Methods**

  * **New benchmarks are increasingly about long-horizon, messy, real-world workflows** : [DeepSWE](https://x.com/_philschmid/status/2059564676569076021) was highlighted as a SWE/agent benchmark with **113 tasks across 91 repos in 5 languages** , using a minimalist bash-only harness and shorter prompts that nevertheless require **5.5 × more code** and touch **7 files on average** than SWE-Bench Pro. In enterprise operations, Artificial Analysis and IBM launched [ITBench-AA](https://x.com/ArtificialAnlys/status/2059698327235805258), an SRE benchmark over Kubernetes incident response where **all frontier models scored below 50%** ; **Claude Opus 4.7** led at **47%** , **GPT-5.5** followed at **46%** , and **GLM-5.1 Reasoning** led open weights at **40%**. Another useful reliability angle came from [AgingBench](https://x.com/omarsar0/status/2059689897523642510), which frames deployed agent degradation as a lifespan problem caused by compression, interference, and memory updates.

  * **Training efficiency research remains active across both theory and systems** : Sakana AI's [DiffusionBlocks](https://x.com/hardmaru/status/2059648995132367277) was one of the most technically interesting releases: it reinterprets forward passes as diffusion-like denoising steps so deep nets can be trained **one block at a time** , dramatically reducing memory while matching end-to-end performance across **ViTs, DiTs, masked diffusion, autoregressive transformers, and recurrent-depth transformers**. On the RL systems side, Snowflake introduced [ZoRRo](https://x.com/StasBekman/status/2059718503318655314), claiming **up to 3.5 × faster long-context RL** and **3.2 × longer context windows** by eliminating redundant rollout computation, alongside the specialized [Arctic-Text2SQL-R2](https://x.com/dwarak/status/2059686825086902398#m) enterprise SQL model. On the theory front, [Tiberiu Musat's preprint](https://x.com/Tiberiu_Musat_/status/2059562156102746148) argues minimum neural weight norm matches minimum program length up to a log factor for fixed-precision networks, while [Unified Neural Scaling Law](https://x.com/ethanCaballero/status/2059686905105563907) proposes a multivariate functional form intended to extrapolate neural scaling behavior more accurately than prior fits.




**Model and Modality Releases: Biology, Vision, OCR, and Embedded AI**

  * **Protein modeling had a standout day** : [ESMFold2](https://x.com/alexrives/status/2059611151860683097) was announced as an open scientific engine for protein structure prediction and design, with strong reported results on **protein interactions and antibodies** , plus an accompanying atlas of **6.8B proteins** and **1.1B predicted structures**. The release emphasized both practical design outcomes--miniprotein binders and single-chain antibodies across five therapeutic targets--and mechanistic interpretability findings about emergent protein representations. The release was echoed by [@proteinrosh](https://x.com/proteinrosh/status/2059633089702240598) and contextualized by [@cgeorgiaw](https://x.com/cgeorgiaw/status/2059694583856927201), who noted the atlas exceeds AlphaFold DB in scale.

  * **A wave of smaller but practical multimodal/open releases landed** : Google DeepMind shared the white paper for [Gemini Embedding 2](https://x.com/mseyed/status/2059504005387284629), described as a **native multimodal embedding model** supporting unified representations over text, image, audio, and video. NVIDIA's [LocateAnything](https://x.com/wildmindai/status/2059600079804088790) combines **Qwen2.5-3B + Moon-ViT** for high-speed grounding, with a claimed **10 × speedup** for dense object detection. Hugging Face integrated Roboflow's [RF-DETR](https://x.com/mervenoyann/status/2059647988373373253), positioning it as real-time detection/segmentation that outperforms YOLO-style systems. For document pipelines, [Surya OCR 2](https://x.com/VikParuchuri/status/2059675773712167423) ships as a **650M** model with **83.3% OLMOCR bench** , **87% on an internal 91-language benchmark** , and **5 pages/s on RTX 5090** ; [LiteParse v2](https://x.com/jerryjliu0/status/2059710330016817501) rewrites parsing in Rust for **up to 100 × speedups** and edge/browser deployment via WASM. On-device AI also got a nod with Google's new [Coral board](https://x.com/googlegemma/status/2059740184930074758) for local speech, vision, and control demos.




**Developer Platforms, Enterprise Controls, and Coding-Agent Productization**

  * **Coding agents are consolidating into full product stacks with enterprise controls** : OpenAI continued tightening Codex's product surface: [GPT-5.2 and GPT-5.3-Codex are being sunset in Codex in favor of GPT-5.5](https://x.com/thsottiaux/status/2059650685948551384), while enterprise features now include [private MCP connectivity over outbound-only HTTPS](https://x.com/OpenAIDevs/status/2059703536825565499), [Workload Identity Federation](https://x.com/OpenAIDevs/status/2059703600662925635), and [expanded Admin API controls](https://x.com/OpenAIDevs/status/2059703665276145920) for spend alerts, allowlists, retention policies, and hosted tool management. OpenAI also published a concrete case study on [self-improving tax agents with Codex](https://x.com/OpenAIDevs/status/2059638868983562640), centered on tracing reviewer corrections back into evals and fixes.

  * **Competition in coding agents is now visibly about reliability, workflow breadth, and enterprise adoption** : [Claude Code](https://x.com/ClaudeDevs/status/2059701677981413812) shared a reliability/performance update and easier bug-report capture, while GitHub kept pushing the "agentized IDE" direction with [Copilot Dev Days](https://x.com/code/status/2059664796178354617) and [MCP positioning](https://x.com/code/status/2059666498285629707). The biggest commercial datapoint was [Cognition](https://x.com/cognition/status/2059660758531940856): **> $1B raised at a $26B valuation**, **enterprise usage up >10× YTD**, and **$492M run-rate revenue** , paired with a growing customer list and strong endorsements from users like [Exa](https://x.com/nityasnotes/status/2059768072110776370). Meanwhile, smaller infra/product moves suggest the ecosystem is broadening: [Cua Driver for Windows](https://x.com/trycua/status/2059688960838828391) brings background computer use to Windows agents; [Cloudflare's agent platform](https://x.com/brandonjcarl/status/2059624598644109363) was repeatedly praised for "fractional computing" economics; and [Grok Build's worktree support](https://x.com/theskory/status/2059729539287167068) targets multi-agent code swarms at repo scale.




**Top tweets (by engagement)**

  * **Cognition 's scale-up**: [Cognition](https://x.com/cognition/status/2059660758531940856) announced **> $1B raised**, **$26B valuation** , and **$492M run-rate revenue** , one of the clearest signals yet that coding agents are converting into large enterprise businesses.

  * **Claude Code reliability push** : [Anthropic's ClaudeDevs](https://x.com/ClaudeDevs/status/2059701677981413812) posted a high-engagement update on responsiveness, reliability, and better feedback collection--evidence that product quality and trust are now central battlegrounds.

  * **Sakana AI 's DiffusionBlocks**: [@hardmaru](https://x.com/hardmaru/status/2059648995132367277) drew major attention to block-wise training that can match end-to-end performance while dramatically lowering memory requirements.

  * **ESMFold2 release** : [@alexrives](https://x.com/alexrives/status/2059611151860683097) announced one of the day's most substantive science releases: open protein modeling at atlas scale with therapeutic design implications.

  * **OpenAI enterprise controls + MCP** : [@OpenAIDevs](https://x.com/OpenAIDevs/status/2059703536825565499) on private MCP and related admin/security updates reflects where frontier APIs are competing for large-org adoption.




* * *

# **AI Reddit Recap**

## **/r/LocalLlama + /r/localLLM Recap**

### **1\. Low-Bit Local AI on Consumer Hardware**

  * **[PrismML just released Binary and Ternary Bonsai Image 4B: 1-bit/ternary text-to-image diffusion transformers that can even run 100% locally in your browser on WebGPU.](https://www.reddit.com/r/LocalLLaMA/comments/1togflk/prismml_just_released_binary_and_ternary_bonsai/)** (Activity: 759): **PrismML released Binary and Ternary Bonsai Image 4B, described as**`1-bit`**/ternary text-to-image diffusion-transformer variants with ~**`3GB`**checkpoints, Apache-2.0 licensing, and a WebGPU browser demo ([HF collection](https://huggingface.co/collections/prism-ml/bonsai-image), [demo](https://huggingface.co/spaces/webml-community/bonsai-image-webgpu)). The post compares them to FLUX.2 Klein 4B at ~**`16GB`**; a top technical comment claims Bonsai Image is primarily a quantized/post-trained derivative of FLUX.2 Klein 4B, with insufficient attribution outside the whitepaper.** The main debate is attribution/branding: one commenter argues PrismML is rebranding quantized/fine-tuned base models as "Bonsai" while minimizing credit to original labs, comparing it to releasing a quant of Qwen as a new model. Another commenter asks whether it can run on CPU with `16GB` RAM, but no technical answer is provided in the supplied comments.

    * A commenter alleges **PrismML 's "Bonsai-Image" is not a newly trained base model**, but a **binary/ternary quantization of**`FLUX.2 Klein 4B` with additional post-training to recover quality. They argue the project's HF demo/model pages and GitHub omit clear attribution to the original FLUX model/team, with the original model reportedly mentioned only in the whitepaper.

    * A technical usability note says the browser/WebGPU model requires roughly `~2 GB`**to download** , which is relevant for fully local inference despite the 1-bit/ternary compression claims. Another user asks whether it can run on **CPU with 16 GB RAM** , but no concrete benchmark or compatibility answer is provided in the thread.

  * **[Got tired of OOM errors on my 4GB GPU. Wrote a custom Rust bare-metal engine and hit 66.8 TPS with a 4B model (BitNet 1.58b on RTX 3050).](https://www.reddit.com/r/LocalLLM/comments/1to6enj/got_tired_of_oom_errors_on_my_4gb_gpu_wrote_a/)** (Activity: 390): **OP claims a custom Rust/C++ LLM inference engine, Cluaiz, runs**`prism-ml/Bonsai-4B-gguf`**with**`1.58-bit`**quantization on an RTX 3050 4GB, reaching**`66.8 tokens/s`**, and reports**`~30-33 TPS`**for Gemma/Qwen 4B variants without OOM via dynamic KV-cache management. No reproducible repo or benchmark artifacts were provided in the post yet; commenters pointed to the apparent project links ([GitHub](https://github.com/cluaiz/cluaiz), [site](https://cluaiz.com/)) and questioned vague claims like **_**" direct-to-silicon"**_**access, noting this may simply mean ahead-of-time native compilation rather than any unusual GPU/driver-level mechanism. The attached Reddit video could not be independently accessed due to Reddit**`HTTP 403`**restrictions.** Top comments were strongly skeptical, characterizing the writeup and repo language as pseudo-technical/AI-generated and arguing the stated achievements amount to basic native compilation plus a single-machine demo. Commenters also challenged the project's licensing/copyright wording under Apache 2.0 and asked for concrete implementation details behind the claimed low-level hardware access.

    * Commenters challenged the technical claims in the linked repo ([github.com/cluaiz/cluaiz](https://github.com/cluaiz/cluaiz), [cluaiz.com](https://cluaiz.com/)), arguing that descriptions like **" direct silicon access"**, "bare-metal engine," and "copyrighted Apache licensed software" appear to be marketing or LLM-generated pseudo-technical language rather than concrete implementation details. One commenter asked whether "direct silicon access" merely means **ahead-of-time native compilation in Rust** , rather than any real low-level GPU programming beyond normal CUDA/driver APIs.

    * Several commenters argued that the claimed outcome should be compared against existing tooling, especially **llama.cpp** , which already supports low-memory inference and quantized models on consumer GPUs. The critique was that OOM issues on a `4GB` RTX 3050 are often solvable through proper llama.cpp configuration rather than writing a new engine, so the claimed `66.8 TPS` with a `4B` BitNet 1.58b model needs reproducible benchmarks and configuration details to be meaningful.




### **2\. Qwen 3.5/3.6 Local Model Releases and Coding Tests**

  * **[Qwen3.5 35B A3B uncensored heretic Native MTP Preserved is Out Now With the Full 785 MTPs Preserved and Retained, Available in Safetensors, GGUFs. NVFP4, NVFP4 GGUFs and GPTQ-Int4 Formats](https://www.reddit.com/r/LocalLLaMA/comments/1tnzalm/qwen35_35b_a3b_uncensored_heretic_native_mtp/)** (Activity: 602): **llmfan46 released**`Qwen3.5-35B-A3B-uncensored-heretic-v2-Native-MTP-Preserved`**, a decensored derivative of**`Qwen/Qwen3.5-35B-A3B`**made with Heretic v1.3.0 / Magnitude-Preserving Orthogonal Ablation-style edits targeting**`attn.o_proj`**,**`attn.out_proj`**, and**`mlp.down_proj`**, while preserving all**`785`**native MTP tensors. The model card reports refusals reduced from**`92/100`**to**`14/100`**, KL divergence**`0.0487`**vs base, and MMLU dropping only from**`84.12%`**to**`83.72%`**over**`7,021`**questions; releases include[Safetensors](https://huggingface.co/llmfan46/Qwen3.5-35B-A3B-uncensored-heretic-v2-Native-MTP-Preserved), [GGUF](https://huggingface.co/llmfan46/Qwen3.5-35B-A3B-uncensored-heretic-v2-Native-MTP-Preserved-GGUF), [NVFP4](https://huggingface.co/llmfan46/Qwen3.5-35B-A3B-uncensored-heretic-v2-Native-MTP-Preserved-NVFP4), [NVFP4 GGUF](https://huggingface.co/llmfan46/Qwen3.5-35B-A3B-uncensored-heretic-v2-Native-MTP-Preserved-NVFP4-GGUF), and [GPTQ-Int4](https://huggingface.co/llmfan46/Qwen3.5-35B-A3B-uncensored-heretic-v2-Native-MTP-Preserved-GPTQ-Int4) variants. The author argues Qwen3.5 and Qwen3.6 both use the **`qwen35`**architecture but are tuned for different regimes --Qwen3.5 for general assistance, Qwen3.6 for agentic/coding--and notes abliteration KL/quality behavior differs substantially between the families.** Commenters appreciated the unusual availability of an **NVFP4 GGUF** build, with one noting they could not find comparable releases even from Unsloth. Another tester agreed with the author's positioning, describing Qwen3.6 as closer to _" 3.5 coder+"_ rather than a simple across-the-board successor to Qwen3.5.

    * One commenter highlighted the practical value of the **NVFP4 GGUF** build, noting that this format is hard to find elsewhere: _" I seriously can't find anyone else doing that, not even Unsloth."_ This is technically relevant because NVFP4 GGUF availability can matter for users targeting newer NVIDIA-oriented low-precision inference workflows while still using GGUF-based runtimes.

    * A tester compared **Qwen3.5** and **Qwen3.6** , arguing that 3.6 feels more like _" 3.5 coder+"_ than a straightforward general upgrade. They suggested the short time between releases makes a broad capability leap unlikely, implying 3.6 may be more specialized toward coding rather than a simple successor to 3.5.

  * **[Okay 27B made me a believer](https://www.reddit.com/r/LocalLLaMA/comments/1to73op/okay_27b_made_me_a_believer/)** (Activity: 541): **OP reports that a**`27B`**Qwen-family model used via Opencode generated a near-complete HTML5 Breakout-style game in one shot from three reference files describing console APIs, gamepad controls, and a TypeScript shader. The output was immediately playable, with working controls, sound, metadata, save/stat/heartbeat API integration, and only required one follow-up for customization plus one glitch fix; a commenter recommends enabling MTP/speculative decoding with**`2-3`**draft tokens for speed. Another heavy user says the model performs best below**`64K`**context, degrades noticeably past**`64K`**, and "really drops off" after **`128K`**, recommending periodic summarization-to-file and session resets for long agentic coding tasks.** Commenters characterize the dense `27B` as unusually strong for local coding--_near-Sonnet class_ for web-app one-shots--while one user found `35B A3B` less capable despite its size/routing advantages. The main caution is that long-context agentic runs can induce loops or "stupidity," so users should manage context aggressively.

    * A commenter recommended enabling **MTP/speculative decoding** for better throughput, suggesting an MTP value of `2` or `3` as a practical speed/quality tradeoff. This is a deployment-level optimization rather than a model-quality claim, useful for users running the 27B model locally.

    * One user reported that the 27B model's effective reasoning quality drops noticeably with long contexts: **best below**`64K`**tokens** , degraded past `64K`, and _" really drops off after _`128K` _. "_ Their workaround for long-horizon agentic tasks is to periodically summarize state into a file, restart the harness/session, and reload the summary to recover model quality and avoid loops.

    * A benchmark operator said **Qwen 27B** was such an outlier that they rechecked their methodology, placing it _roughly on par with GPT-5.2 or Sonnet 4.5_ in their rankings while noting it struggles at larger context sizes, likely due to parameter-count limits. They linked their data at [gertlabs.com/rankings](https://gertlabs.com/rankings).




[ Read more ](https://www.latent.space/p/ainews-cognition-raises-1b-in-26b)

---

## [🔬ESM: The Bitter Lesson is Coming for Proteins - Alex Rives, BioHub](https://www.latent.space/p/esmfold2)
*🔬 Latent Space | 2026-05-27*

_Editor 's note: In our [first BioHub pod with Priscilla and Mark](http://latent.space/p/biohub) they discussed their [acquisition of EvoScale](https://apnews.com/article/chan-zuckerberg-philanthropy-biohub-evolutionaryscale-87c24eb349abcce8abec132b8538d7b0), led by **[Alex Rives](https://biohub.org/team/alex-rives/)** , who is now Head of Science at BioHub. With ESM-1 they trained language models on millions of protein sequences drawn from across life, with a simple "next token" objective: predict the amino acids that have been randomly masked out, based on the context of the rest of the sequence. But they soon found that these models also learned biological structure and function, including properties the model had **never been explicitly shown** AND that this ability **scales predictably with compute** , leading to [ESM2 and ESM3](https://www.evolutionaryscale.ai/blog/esm3-release)._

_Today, Alex[announced](https://x.com/alexrives/status/2059611151860683097) ESMFold 2, an open scientific engine to power prediction, design, and discovery across protein biology._

_  
Building on Cryo-EM data (discussed in the CZI pod), ESMFold2 reports state of the art performance on protein interactions, especially antibodies, a critical modality for therapeutics, and evidence that**inference time scaling** is also **working across five targets in cancer and immunology**._

[](https://substackcdn.com/image/fetch/$s_!fuSJ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F752765d3-f1e2-4a8f-a467-738c8b85e67b_1092x1224.png)

_  
In a nod to that other famous AI x protein folding project, they are also releasing an atlas of 6.8 billion proteins, and 1.1 billion predicted structures, which you can play around with on[their website](https://x.com/alexrives/status/2059622778945343669). We are honored to work with them for this huge release!_

[](https://substackcdn.com/image/fetch/$s_!EU6S!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fca5d073a-d889-4d89-b574-0db54da0c88a_2010x1490.png)

* * *

One of the refrains we've heard on the Science pod has been that protein folding, materials design, cellular biology, etc. are very different problems from Language Modeling. They definitely are. Yet Alex Rives and the ESM team at BioHub just released a [preprint and model](https://biohub.ai/esm/protein/about), demonstrating that vanilla BERT-like transformer models trained on sufficiently large and diverse data sets can beat specialized models like AlphaFold3 on some of the hardest protein-related problems. 

Andrew White had a [great segment](https://www.youtube.com/watch?v=XqoBSB3nsgw) in our first LS-Science episode that explained how mind blowing AlphaFold2 was when it was released in 2020: it suddenly solved problems **on a GPU on your desktop** that [DESRes](https://www.deshawresearch.com/) had built **custom-ASIC supercomputer clusters** to solve. John Jumper and Demmis Hassabis received the [Nobel Prize](https://www.nobelprize.org/prizes/chemistry/2024/popular-information/) in Chemistry for this work.

AlphaFold2 took advantage of an very clever observation: if multiple species co-evolve pairs of mutations, this implies that the mutations correspond to parts of the protein that are close in 3d space. This is usually shorthanded as MSAs (multi-sequence alignments), and is the key insight which makes AlphaFold2 so effective.

[](https://substackcdn.com/image/fetch/$s_!APHX!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0355a037-a76e-47a4-8997-cb0b44e3e427_1536x1024.png)

Like other inductive biases, however, it hurts generalization.

## Scale-pilled before it was cool

If you take a look at the timeline for scaling laws for LLMs and release of structure prediction models[1](https://www.latent.space/feed#footnote-1), the ESM team notably doubled down on their MSAs-be-damned approach after AlphaFold2 released. This obviously requires a great deal of belief in the scale hypothesis.

Why the conviction?

ESM developed at a time when many of the scaling laws and the "Bitter Lesson" were proving increasingly correct. AlphaFold2's wild success must have been both exciting and bitterly disappointing. But using MSAs mean that the model is is dependent on training data that contains MSAs in order to be accurate in a given domain. For things like antibodies that don't have MSAs to train on[2](https://www.latent.space/feed#footnote-2), AlphaFold tends to do poorly.

ESM takes a different approach: learn the relationship between different proteins by unsupervised training on as much diversity as you can find (sound familiar?) and **then** correlate that back to structures know from the Protein Data Bank (PDB) and other sources[3](https://www.latent.space/feed#footnote-3). 

In other words, a World Model.

## World Model for proteins

"World Model" is a hype term that I define like this:

Use unsupervised training to learn **abstract patterns** from the data:

  * The abstraction should be **semantic** \- novel constructions represent things that obey the rules of the real world

  * The abstraction should be **compositional** \- recombining different patterns leads to novel and often valid constructions

  * The abstraction should **support generalization** \- it predicts things in the real world it wasn't trained on 




Once you have a world model, you can attach "heads" to it for downstream tasks: predict properties of a protein, decompose its functional features, or search the representation for proteins that meet design criteria. The two big models BioHub just released **under MIT license** map directly onto this:

  * **World model -> ESMC** (a model trained on 2.8 billion sequences)

  * **Structure-prediction head -> ESMFold2**




One of the interesting ways the world model can "predict things" is to generate proteins sequences and then measure the predicted properties, such as binding affinity, in the lab. Alex talks in the episode about validating some of the harder molecules they predicted in the wet-lab. Very cool!

Another way is to use mech-interp techniques such as [Sparse Auto Encoders](https://transformer-circuits.pub/2024/scaling-monosemanticity/) (SAEs) to extract semantic features from your model, and then find novel features that predict unknown biology. I won't spoil this part for you: it was one of the highlights of the episode for me!

## A cell is a computer

We have all heard that genes are like computer programs, but usually the analogy fizzles after that. Of course genes are _transcribed_ into RNA and RNA is _translated_ into proteins, so **genes are programs for building proteins** , but that carries the analogy only to "binary digits are programs."

Here's a better analogy: you can think of the _cell nucleus_ as a **storage device / storage controller** , the _ribosome_ as a **JIT-compiler and runtime** , and the _semantic features_ that we learn from our world model via SAEs as **functions** , _proteins_ as **processes** that interact together in **workflows** (_signalling pathways_) to produce **behaviors and outputs** (_phenotypes_). 

Like functions, the SAE features have a **hierarchical composition** from local, secondary and tertiary structures (mimicing protein structure)[4](https://www.latent.space/feed#footnote-4), but also **motifs that are conceptual** , such as membrane integrations, disordered regions and disulfide bonds[5](https://www.latent.space/feed#footnote-5). As we learn to compose these features we into novel protein designs, we move further towards **programmable biology**. 

Alex goes into much more detail about this in the episode, as well as:

  * Principles for new data collection

  * BioHub's vision

  * Modeling the cell




Enjoy!

## Full Video podcast

please like and subscribe!

  * **X** : <https://x.com/alexrives>

  * **LinkedIn** : 




[1](https://www.latent.space/feed#footnote-anchor-1)

[](https://substackcdn.com/image/fetch/$s_!QxRF!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1fb19dd1-bb93-42b3-a331-862137bf6544_1024x1536.png)

[2](https://www.latent.space/feed#footnote-anchor-2)

Antibodies mutate very rapidly so that they can adapt to pathogens with novel proteins on them. These dynamics mean that MSAs don't appear in them.

[3](https://www.latent.space/feed#footnote-anchor-3)

This includes a dataset created using AlphaFold2 itself for ESMC, making it a distillation of AlphaFold, and indirectly dependent on MSAs itself.

[4](https://www.latent.space/feed#footnote-anchor-4)

**Very local** (1-3 residues): individual amino acid biochemistry, hydrophobic vs. polar character, charge

**Short-range** (~5-10 residues): secondary structure -- α-helix features, β-strand features, β-turn features

**Medium-range** (~10-30 residues): supersecondary motifs -- β-hairpins, helix-turn-helix, β-α-β units

**Long-range** (whole-protein): full domain identifiers -- immunoglobulin fold, Rossmann fold, TIM barrel, four-helix bundle

[5](https://www.latent.space/feed#footnote-anchor-5)

**DNA-binding** features -- activated across helix-turn-helix proteins, zinc fingers, leucine zippers, and other DNA-binding folds that share function but not sequence

**Membrane integration** features -- activated on transmembrane segments regardless of whether they sit in a GPCR, a transporter, or a channel

**Disordered region** features the SAE devotes ~686 features (5-10% of the feature budget) to intrinsically disordered regions, which is striking because IDRs have no structure to predict. The model represents _disorderedness itself_ as a concept, with sub-features for different IDR flavors (polyampholyte, polar tract, prion-like domain)

**Disulfide bond** features -- activated on cysteines that participate in disulfides, distinguishing them from free cysteines

---

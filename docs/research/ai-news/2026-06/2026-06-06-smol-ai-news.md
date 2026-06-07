# 🌐 Smol AI News — 2026-06-06

> Discord、Reddit 等 AI 社群圈內直擊（已從 buttondown 遷移至 news.smol.ai）
> 來源：[Smol AI News](https://news.smol.ai/rss.xml)

---

## [not much happened today](https://news.smol.ai/issues/26-06-04-not-much/)
*🌐 Smol AI News | 2026-06-04*

**a quiet day.**

> AI News for 6/3/2026-6/4/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

# AI Twitter Recap

**NVIDIA’s Nemotron 3 Ultra and 3.5 ASR Release**

  * **Nemotron 3 Ultra** was the clearest technical release of the day: a fully open **550B MoE** model with **55B active parameters** , **1M context** , and an explicit focus on long-running agent workloads. NVIDIA says it is **up to 5x faster** and **30% lower cost** for agentic tasks, with weights, synthetic data, reward checkpoints, quantized variants, and training recipes released under **OpenMDW 1.1** ([NVIDIA launch](https://x.com/nvidia/status/2062522316672667770), [NVIDIAAI open artifacts](https://x.com/NVIDIAAI/status/2062521383582646537), [Pavlo Molchanov thread](https://x.com/PavloMolchanov/status/2062538679470657727)). The architecture combines **hybrid Mamba/attention** , **LatentMoE** , and **native MTP** , with pretraining done in **NVFP4** over **20T tokens** —notable because it pushes low-precision pretraining into a new scale regime ([tech notes](https://x.com/ctnzr/status/2062515418884149451), [scaling discussion](https://x.com/scaling01/status/2062540298933219832)).

  * **Benchmarks and serving story** were unusually strong for an open release. [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2062527871529439438) measured **47.7** on its Intelligence Index using NVIDIA’s recommended NVFP4 inference weights (**48.2** in BF16), making it the strongest **US open-weights** model they’ve tested, though still behind **Kimi K2.6**. More interestingly, they reported **400+ output tok/s** via BlackBox, and separately showed Nemotron 3 Ultra sitting on the **Pareto frontier for task latency vs. performance** on Terminal-Bench-style evaluations under turn limits ([latency analysis](https://x.com/ArtificialAnlys/status/2062598349757567359), [BlackBox throughput](https://x.com/blackboxai/status/2062546216949588001)). The model shipped **day 0** across the stack: [vLLM](https://x.com/vllm_project/status/2062574262163280172), [Modal](https://x.com/modal/status/2062528720104227149), [Together](https://x.com/togethercompute/status/2062520009893576974), [Fireworks](https://x.com/FireworksAI_HQ/status/2062568688201646321), [Ollama cloud](https://x.com/ollama/status/2062591290743853291), [Baseten](https://x.com/baseten/status/2062609272815685759), [CoreWeave/W&B](https://x.com/wandb/status/2062577626242580896), [Cline](https://x.com/cline/status/2062620668085297214), [Prime Intellect](https://x.com/PrimeIntellect/status/2062622550300275088), and [Nous Portal](https://x.com/NousResearch/status/2062554136625766409).

  * **Nemotron 3.5 ASR** was the quieter but practical companion release: an open streaming ASR model with a single **0.6B checkpoint** , **40 language-locale combinations** , and **sub-100ms latency** , built on a **cache-aware FastConformer / RNN-T** style design optimized for voice agents and streaming speech workloads ([Piotr Zelasko](https://x.com/PiotrZelasko/status/2062538923776290909), [Together](https://x.com/togethercompute/status/2062520605102993436), [fal availability](https://x.com/fal/status/2062521027020611933)).




**Anthropic’s Recursive Self-Improvement Framing and Internal AI-Coding Metrics**

  * Anthropic published the most-discussed policy/research note of the day, arguing that current systems show **early signs of recursive self-improvement (RSI)** —not yet full autonomy in research direction, but clear evidence that AI is accelerating AI development ([Anthropic post](https://x.com/AnthropicAI/status/2062568862479208923)). The headline operational claims were concrete: **80%+ of merged code** at Anthropic is now authored by Claude, the typical engineer ships **8x more code per quarter** than in prior years, and on internal open-ended engineering tasks Claude’s success rate rose from roughly **26% to 76%** in six months ([code metric](https://x.com/AnthropicAI/status/2062568864240836995), [Alex Albert summary](https://x.com/alexalbert__/status/2062580571214389510)).

  * The most striking empirical datapoint was Anthropic’s recurring “speed up a small model training script” test: **Claude Opus 4** averaged about **3x** speedup, while **Mythos Preview** reportedly achieved **~52x** ([Anthropic benchmark claim](https://x.com/AnthropicAI/status/2062568869240476050), [correction on dates](https://x.com/AnthropicAI/status/2062634151556292775)). Anthropic also says Mythos gave better “what to do next” research suggestions than humans **64%** of the time in sessions where the researcher had taken a wrong turn ([research-next-step result](https://x.com/AnthropicAI/status/2062568870872003021)). Their broader thesis: automating _problem selection_ is still unresolved, but automating large portions of implementation and iteration is already happening.

  * The governance angle mattered as much as the productivity claims. Anthropic explicitly wrote that “it would be good for the world to have the option to **slow or temporarily pause frontier AI development** ,” framing verification and coordination mechanisms as increasingly urgent if RSI-like dynamics continue ([Anthropic governance statement](https://x.com/AnthropicAI/status/2062568873321513443), [discussion](https://x.com/scaling01/status/2062572962117562507), [commentary](https://x.com/a_karvonen/status/2062572851916574730)). This landed amid criticism that Anthropic recently **weakened parts of its Responsible Scaling Policy thresholds** around bio/chemical risk, according to [@CRSegerie](https://x.com/CRSegerie/status/2062474945377218819). Separately, a coalition including **Altman, Amodei, Hassabis, and Baker** backed **mandatory DNA synthesis screening and recordkeeping** in the US, arguing AI is eroding biological knowledge barriers ([letter summary](https://x.com/kimmonismus/status/2062485389949145457)).




**Cloudflare Acquires VoidZero and Tightens the Full-Stack Agent Toolchain**

  * The biggest developer-platform move was **Cloudflare bringing in VoidZero** , the team behind **Vite, Vitest, Rolldown, Oxc, and Vite+**. Cloudflare and VoidZero emphasized that **Vite remains open source, MIT, and vendor-neutral** , with Cloudflare also committing **$1M** to a fund for independent Vite ecosystem development ([Cloudflare](https://x.com/Cloudflare/status/2062521221132992533), [Vite statement](https://x.com/vite_js/status/2062525206158078047), [Evan You](https://x.com/evanyou/status/2062533668233756677)).

  * The strategic read from developers was that this gives Cloudflare tighter control over an increasingly agent-friendly application stack: frontend/build tooling, runtime, storage, inference, deployment primitives, and security in one place. [@wesbos](https://x.com/wesbos/status/2062520527151903090) framed it as Cloudflare assembling “a tidy package they can hand to an LLM to make a site,” which is directionally consistent with Cloudflare’s own push on agents, MCP, sandboxes, AI search, payments, and observability in a unified platform ([Cloudflare agents docs overview](https://x.com/thomasgauvin/status/2062512156076048447)).




**Agents, Harnesses, Memory, and Evaluation Infrastructure**

  * Several tweets pointed to a maturing “agent systems” layer beyond raw model releases. A recurring theme was that the bottleneck is increasingly the **harness/orchestrator** , not just prompting. A popular clip summarized the Claude Code workflow as “I don’t prompt Claude anymore, I write loops,” while [@omarsar0](https://x.com/omarsar0/status/2062553527730540611) described reverse-engineering **dynamic workflows** into his own orchestrator for branching research, verification, triage, data synthesis, and eval generation. The common idea: higher-order control loops, not one-shot prompts, are becoming the real unit of work.

  * Tooling around those loops also improved. [LangSmith Sandboxes](https://x.com/LangChain/status/2062512156688466083) reached GA with Dockerfile snapshots, interactive consoles, TCP tunneling, and standard Linux tooling. Hugging Face pushed two adjacent ideas: a **Kernels** distribution path for custom kernels on the Hub ([announcement](https://x.com/RisingSayak/status/2062471134260687264)) and stronger support for storing **agent traces** as first-class artifacts, echoed by [@ClementDelangue](https://x.com/ClementDelangue/status/2062542713463980303). [@julien_c](https://x.com/julien_c/status/2062524414034423969) released **SynthTraces** , a minimal harness that generated **2,000+ synthetic coding-agent session traces** by having an open model play the coding agent and a local model simulate the user.

  * Evaluation also shifted toward real-world agent work. **Arena** launched **Agent Arena / Agent Mode** , measuring agentic performance from **millions of live sessions** with tools like web search, filesystem, bash, and image generation. Their current ranking puts **GPT-5.5** first, followed by **Claude Opus 4.7** , **GLM-5.1** , **Gemini 3.1 Pro** , and **Kimi-K2.6** , with methodology based on task success, steerability, recovery, user praise/complaint, and tool hallucination across **300K+ tasks** , **2M+ tool calls** , and **40M lines of code** ([launch](https://x.com/arena/status/2062566749418233981), [methodology](https://x.com/arena/status/2062566769659912281)). On the enterprise side, **Cognition** introduced an **AI Productivity Guarantee** for Devin—up to **$10M** in covered usage if the product doesn’t produce positive engineering value—backed by an internal measurement system over **258 enterprise sessions** spanning tasks up to **64+ hours** ([guarantee](https://x.com/cognition/status/2062597242167628019), [technical writeup](https://x.com/cognition/status/2062597246001324518)).




**Memory, Multimodality, and Model/Benchmark Updates**

  * **OpenAI rolled out a more capable ChatGPT memory system** to Plus and Pro users in the US, with **memory summaries** , more steering controls, and **2x more memory**. The company framed this as a longer-running research arc from saved memory to “dreaming” to the current system ([OpenAI](https://x.com/OpenAI/status/2062567556524003631), [controls](https://x.com/OpenAI/status/2062567559673856346), [Christina Kim explanation](https://x.com/ChristinaHartW/status/2062585124450172956)). Related developer-side updates included **moderation scores in the Responses and Completions APIs** ([OpenAIDevs](https://x.com/OpenAIDevs/status/2062619558440267801)) and a heavily shared demo of the new **Codex iOS app plugin** for viewing and testing apps in-browser with hot reload ([OpenAIDevs demo](https://x.com/OpenAIDevs/status/2062599291479478275)).

  * A few other model/data releases are worth noting. **Gemma 4 12B** continued to draw attention both as a local coding model replacement and in highly compressed form: [Unsloth](https://x.com/UnslothAI/status/2062470072179044447) released a **2-bit GGUF** at **4.66 GB**. [@_philschmid](https://x.com/_philschmid/status/2062546814075609413) highlighted an architectural explainer on how Gemma 4 handles text/images/audio without separate encoders. In multimodal research, [@skalskip92](https://x.com/skalskip92/status/2062549751246066144) flagged **Molmo2** as a strong open VLM candidate at CVPR, supporting video pointing, tracking, counting, and multi-image reasoning. For document understanding, **ParseBench** from LlamaIndex introduced an open benchmark with **2,000+ human-verified pages** and **167K+ test rules** across tables, charts, faithfulness, formatting, and grounding ([benchmark announcement](https://x.com/llama_index/status/2062525204262236266)).




**Top Tweets (by engagement, filtered for technical relevance)**

  * **Anthropic on RSI and internal automation** : Claude now writes **80%+** of merged code at Anthropic, engineers ship **8x** more code, and the company says AI accelerating AI development is becoming plausible ([Anthropic](https://x.com/AnthropicAI/status/2062568862479208923)).
  * **OpenAI memory upgrade** : a more capable ChatGPT memory system with summaries, steering controls, and **2x** more memory for Plus/Pro users in the US ([OpenAI](https://x.com/OpenAI/status/2062567556524003631)).
  * **Cloudflare + VoidZero** : Cloudflare brings in the VoidZero team while keeping **Vite MIT and vendor-neutral** , plus a **$1M OSS fund** for the ecosystem ([Cloudflare](https://x.com/Cloudflare/status/2062521221132992533), [Vite](https://x.com/vite_js/status/2062525206158078047)).
  * **Nemotron 3 Ultra launch** : open **550B/55B-active** hybrid MoE for long-running agents, with full recipes and unusually strong speed claims ([NVIDIA](https://x.com/nvidia/status/2062522316672667770)).
  * **Cursor canvases + context explorer** : sharable canvases for apps/reports/internal tools and an interactive breakdown of where agent context is spent ([Cursor](https://x.com/cursor_ai/status/2062611883249783083)).



* * *

# AI Reddit Recap

## /r/LocalLlama + /r/localLLM Recap

### 1. Gemma 4 12B Release and Benchmarks

  * **[google/gemma-4-12B · Hugging Face](https://www.reddit.com/r/LocalLLaMA/comments/1tvtn6m/googlegemma412b_hugging_face/)** (Activity: 1610): ****Google DeepMind** released [`google/gemma-4-12B`](https://developers.googleblog.com/gemma-4-12b-the-developer-guide/) as part of the **Gemma 4** open-weights family, spanning `E2B`, `E4B`, `12B`, `26B A4B`, and `31B` variants with dense and MoE architectures, instruction-tuned/pretrained checkpoints, multimodal input, multilingual support across `140+` languages, and context windows up to `256K` tokens. The post highlights native `system` role support, configurable reasoning/thinking modes, function-calling/agentic use cases, coding improvements, and local deployment via GGUF builds from [`ggml-org`](https://huggingface.co/ggml-org/gemma-4-12b-it-GGUF) and [`unsloth`](https://huggingface.co/unsloth/gemma-4-12b-it-GGUF). A top comment links Maarten Grootendorst’s [visual guide](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-gemma-4-12b), specifically calling out the model’s _“encoder-free architecture.”_** Commenters are mainly interested in empirical coding performance, with one explicitly wanting to test whether Gemma 4 12B can beat **Qwen 3.5 9B** on coding tasks. No concrete benchmark results were provided in the comments.

    * A linked technical guide by **Maarten Grootendorst** highlights Gemma 4 12B’s **encoder-free architecture** , framing it as a notable design point for readers interested in model internals: https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-gemma-4-12b.
    * Several commenters positioned **Gemma 4 12B** as a practical size tier between smaller Gemma variants like `E4B` and larger models such as `26B`, with one user also noting interest in whether it can outperform **Qwen 3.5 9B** on coding tasks.
    * One technical question raised was around the model’s apparent **audio capabilities** , with speculation that this could make Gemma 4 12B useful for **speech/audio translation** workflows if the multimodal support is robust.
  * **[New Google Gemma 4 12B Claims Near-26B Performance - We Tested Both!](https://www.reddit.com/r/LocalLLaMA/comments/1tw4tmf/new_google_gemma_4_12b_claims_near26b_performance/)** (Activity: 984): **A local single-`RTX 4090` comparison claims **Google Gemma 4 26B-A4B** used `15 GB` VRAM, generated `6.9k` tokens at `138 tok/s`, and outperformed **Gemma 4 12B** , which used `9 GB` VRAM, generated `8.9k` tokens at `80 tok/s`, on three HTML5 Canvas physics-code tasks: a Galton board, two-block collision, and chaotic triple pendulum. The poster argues the MoE-style `26B-A4B` model is ~`1.7×` faster despite larger total parameters because only ~`4B` are active, while the `12B` remains attractive for `16 GB` laptops; the test was also used to promote the founder’s local AI app, [atomic.chat](https://atomic.chat/).** Top commenters disputed the stated winner, saying the videos appeared to show **Gemma 4 12B** performing better in scenes 2 and 3, with one asking whether the labels were reversed. Another commenter requested a comparable benchmark against **Qwen3.6 35B-A3B**.

    * Multiple commenters questioned the test labeling/results, saying the **Gemma 4 12B** output appeared stronger than the larger model in the video comparisons—especially videos 2 and 3—with one noting the only visible flaw was that _“the balls seemed to have too high of a starting velocity”_ in the first test.
    * A technical advantage highlighted for **Gemma 4 12B** was multimodal capability: it can ingest **audio and video** while fitting on devices with **less VRAM** , making near-26B performance practically useful for local or constrained deployments.
    * Commenters requested broader baselines such as **Qwen3.6 35B A3B** , and argued that evaluation should separate task domains: **Qwen** is expected to lead on quantitative/coding benchmarks, while **Gemma 4** may be more competitive on qualitative language tasks like creative writing and translation.
  * **[gemma-4-12b-it vs Qwen3.5-9B on shared benchmarks: Qwen is overall winner beating gemma in 5/8 benchmarks despite a smaller footprint](https://www.reddit.com/r/LocalLLaMA/comments/1tw0lua/gemma412bit_vs_qwen359b_on_shared_benchmarks_qwen/)** (Activity: 520): **The image is a technical benchmark table comparing**Gemma 4 12B Unified** vs **Qwen3.5-9B** , compiled from official Hugging Face model-card scores, with **Qwen3.5-9B winning`5/8` shared benchmarks** despite a smaller parameter footprint and allegedly lighter KV cache ([image](https://i.redd.it/20s4116kg45h1.png)). Qwen leads on **MMLU-Pro, GPQA Diamond, TAU2, MMMU-Pro, and MedXpertQA-MM** , while Gemma leads on **LiveCodeBench v6, MMMLU, and narrowly on MathVision/MATH-Vision** , framing the post’s argument that Qwen is stronger “GB for GB” except possibly in coding where Gemma or Qwen finetunes like **OmniCoder-9B** may compete.** Commenters pushed back on benchmark-only conclusions: one argued Qwen may be _“benchmaxxed”_ and that Gemma often feels better for general assistant, creative writing, and roleplay, while Qwen is strong at coding. Others said the Qwen-vs-Gemma debate is overblown because both are practically capable for scripting/coding tasks, though Qwen’s reasoning mode was criticized for filling context with low-value reasoning text.

    * Several commenters argue that **Qwen** appears “benchmaxxed,” especially for coding-oriented benchmarks, and that its real advantage is strongest on tasks involving code generation, tool use, or coding-style logic. In practical use, users report both **Gemma 4 31B / Gemma 3.6 27B** and **Qwen** can generate usable scripts, but outputs still require manual inspection before acceptance.
    * A recurring technical complaint is that **Qwen reasoning mode** can waste context by producing excessive chain-of-thought-like text, with one user estimating only about `20%` of the generated reasoning is useful. This suggests that for some local/SLM workflows, disabling reasoning may improve effective context utilization and reduce noise.
    * Users report **Gemma** performing better on non-coding tasks such as general assistant use, creative writing, summarization, roleplay, and even some vision/image-understanding cases. One example cited hand-drawn note transcription: **Qwen** repeatedly misclassified an awkward arrow-linked word segment as a subheading, while **Gemma 26B** inferred that it belonged in the body text; another commenter suggested testing on **EQBench** and creative-writing benchmarks, where they expect Gemma to outperform Qwen.



### 2. Long-Context Scaling and KV Cache Efficiency

  * **[nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16 · Hugging Face](https://www.reddit.com/r/LocalLLaMA/comments/1twla1k/nvidianvidianemotron3ultra550ba55bbf16_hugging/)** (Activity: 542): ****NVIDIA** released [`nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16`](https://huggingface.co/nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16), a `550B`-parameter **LatentMoE** hybrid model with `55B` active parameters, interleaving **Mamba-2** , MoE, selected attention layers, and **Multi-Token Prediction** ; it advertises up to `1M` token context and configurable reasoning via `enable_thinking=True/False`. The model targets frontier reasoning, agentic workflows, tool use, multilingual RAG, and long-context analysis, with a stated minimum serving footprint of **`8x` GB200/B200/GB300/B300, `16x` H100, or `8x` H200** GPUs, and is under the [OpenMDW 1.1 license](https://raw.githubusercontent.com/OpenMDW/OpenMDW/refs/heads/main/1.1/LICENSE.OpenMDW-1.1).** Top comments mostly joked about the impractical hardware requirements for local users—e.g. _“Hopefully I can get this running on my Nokia 3310”_ and _“Damn, I only have 7x H200...”_ —rather than debating model quality or architecture.

    * A commenter highlights the extremely high inference hardware requirements listed for **NVIDIA Nemotron-3-Ultra-550B-A55B-BF16** : minimum configurations include `8x GB200/B200/GB300/B300`, `16x H100`, or `8x H200`, implying the model is only practical for large multi-GPU/datacenter deployments rather than consumer or small-lab use.
    * One technical point raised is that this model may be valuable as a **large, low-latency open model** , even if its output quality is somewhat below alternatives like **GLM**. The tradeoff discussed is that faster response/processing can matter more than absolute benchmark quality for latency-sensitive applications.
  * **[KVarN: new KV-cache quant from Huawei. 3–5× KV cache compression with actual speed-up instead of slow-down, and unlike TurboQuant it holds up on reasoning (Apache 2.0, vLLM single flag)](https://www.reddit.com/r/LocalLLaMA/comments/1twptw2/kvarn_new_kvcache_quant_from_huawei_35_kv_cache/)** (Activity: 438): ****Huawei CSL** open-sourced **KVarN** , an Apache-2.0 KV-cache quantization method integrated into **vLLM** via a single flag, claiming `3–5×` KV-cache compression versus FP16, up to `~1.4×` FP16 throughput, and up to `~2.4×` **TurboQuant** throughput while preserving FP16-level quality ([repo](https://github.com/huawei-csl/KVarN), [paper](https://arxiv.org/abs/2606.03458)). The post contrasts KVarN with vLLM FP8 KV cache (`~2×` capacity, near-BF16 throughput) and **Google TurboQuant** , citing a [vLLM/Red Hat AI study](https://vllm.ai/blog/2026-05-11-turboquant) where TurboQuant achieves compression but drops to `66–80%` of BF16 throughput and loses `~20` reasoning points in low-bit modes on benchmarks like AIME25 and LiveCodeBench. The key technical claim is that KVarN avoids explicit BF16 dequantization overhead in attention and maintains reasoning/code/math accuracy at higher compression, with no model changes, retraining, or calibration.** Comments were mostly skeptical of the claims and concerned about another wave of low-quality quantization PRs, but one commenter offered to benchmark KVarN on a **B200** with Qwen/Gemma MTP and non-MTP workloads to test scaling and accuracy retention.

    * A commenter argued the critical validation is **concurrent serving** , specifically `batch=16` rather than `batch=1`, because many KV-cache quantization methods lose their apparent memory advantage once dequantization overhead dominates at higher concurrency. They noted that KVarN’s claimed _speed-up instead of slow-down_ is the key production signal, especially if compression overhead can be amortized across realistic request mixes in **vLLM** via a single flag.
    * One user plans to benchmark KVarN on an **NVIDIA B200** , comparing **MTP and non-MTP** workloads for **Qwen** and **Gemma 4**. This would be useful for validating whether the claimed `3–5×` KV-cache compression and speed gains scale on high-end inference hardware rather than only in paper settings.
    * Another commenter was skeptical that KV quantization results will generalize to newer architectures, suggesting many methods work because current models store information inefficiently in the KV cache. They specifically requested evaluation on **Qwen3.5** and **DeepSeek V4-style architectures** , where KV information may be stored more densely and therefore be less tolerant of aggressive compression.



## Less Technical AI Subreddit Recap

> /r/Singularity, /r/Oobabooga, /r/MachineLearning, /r/OpenAI, /r/ClaudeAI, /r/StableDiffusion, /r/ChatGPT, /r/ChatGPTCoding, /r/aivideo, /r/aivideo

### 1. Open Image Models & Local Generation Workflows

  * **[Ideogram 4.0 Just Open Sourced!](https://www.reddit.com/r/StableDiffusion/comments/1tvtu2u/ideogram_40_just_open_sourced/)** (Activity: 1087): **The[image](https://i.redd.it/9ajk9fuu935h1.jpeg) is a **promotional/non-technical banner** for the post’s claim that **Ideogram 4.0** is now open-weight and “Now on Comfy,” showing a cinematic neon-sign scene with the Ideogram logo rather than benchmark plots or architecture diagrams. The selftext describes a `9.3B` text-to-image DiT model with `fp8`/`nf4` checkpoints, native ComfyUI support, **Qwen3-VL-8B-Instruct** text encoding, JSON-structured prompting with hex colors/bounding boxes/text elements, and reported `0.97` X-Omni English OCR accuracy.** Commenters focused less on the promo image and more on safety behavior: multiple users report the model is heavily censored/“safetymaxxed,” especially for NSFW prompts, with one predicting the community will try to “abliterate” or remove those restrictions.

    * Users report that the released **Ideogram 4.0** model appears heavily safety-filtered: **comfyanonymous** notes that certain blocked outputs are due to the model being _“safetymaxxed”_ rather than a **ComfyUI** issue, with an example image shown [here](https://preview.redd.it/7lrd6rekg35h1.png?width=1024&format=png&auto=webp&s=988d678c1ecca642b6182749c6ade74e0c7ffaa1). Multiple commenters also describe it as hard-censored for NSFW generation, suggesting the restriction is embedded at the model/prompting level rather than merely UI-side.
    * Several technical adoption blockers were raised: commenters mention **watermarking** , **strong censorship** , and **no commercial license** , arguing these constraints make the open release less useful for production or downstream fine-tuning workflows. One user explicitly summarizes the concern as: _“Watermarked, censored, no commercial license.”_
    * A commenter highlighted a **bounding-box JSON prompting** capability as a notable feature, showing an example output [here](https://preview.redd.it/0bmpbik2e35h1.png?width=1024&format=png&auto=webp&s=8ea4876bd32c8d93e34e5c226ab7a06a1720c68c). This suggests Ideogram 4.0 may support more structured layout control via JSON-style spatial constraints, which could be useful for deterministic composition or UI/design generation workflows.
  * **[Multiple characters Anima generations are so good. There is some bleeding but its only gonna get better](https://www.reddit.com/r/StableDiffusion/comments/1tvv4j1/multiple_characters_anima_generations_are_so_good/)** (Activity: 932): **The post showcases multi-character image generations using**Anima** , with workflows published on the author’s [Civitai profile](https://civitai.red/user/Smexlo); the author notes remaining issues with prompt control, character/detail bleeding, and anatomy. One image was post-edited with **Grok** to add “Blair Witch” stick figures, while the rest were generated in Anima, and the author says they are looking forward to **WAI Anima**.** Commenters praised Anima’s multi-character composition and prompt adherence, with one comparing it favorably to **NovelAI Diffusion V4.5** and emphasizing that its natural-language parsing is surprising given a `500M`-parameter text encoder. Another commenter reported they “don’t even usually have issues bleeding,” suggesting bleeding severity may be workflow- or prompt-dependent.

    * Users focused on **Anima’s multi-character prompt adherence** , noting that it can set up detailed scenes through natural-language prompting with comparatively little character/color/detail bleeding. One commenter contrasted this with **Illu/Pony workflows** , where multi-character generations often require a strong checkpoint plus character LoRAs but still suffer from _“heavy bleeding,”_ partly because **Danbooru-tag prompting is more limited** for specifying complex scene relationships.
    * A technically notable claim was that Anima achieves strong natural-language parsing despite using only a **`500M` parameter text encoder**, with one user comparing its prompt-following favorably against **NovelAI Diffusion V4.5** as a reference point for bleeding-edge prompt adherence. The discussion framed Anima as an early baseline that could improve further through community fine-tuning and “backyard engineering” similar to what happened around **SDXL**.
    * One user shared an example output at **`2560px` width** and said they _“don’t even usually have issues bleeding”_ ([image](https://preview.redd.it/9cg06yjwo35h1.png?width=2560&format=png&auto=webp&s=bbc1ae3f5a825fb744fb7e351bc0d23d7f61def8)), suggesting bleeding may be prompt/model-dependent rather than universal in Anima multi-character generations.



### 2. Claude Code Over Live Data Streams

  * **[I wired Claude Code into a database of every Polymarket wallet and trades via MCP. What do you want me to ask it next? This is what I found so far:](https://www.reddit.com/r/ClaudeAI/comments/1tvefqd/i_wired_claude_code_into_a_database_of_every/)** (Activity: 1801): **The author claims they connected**Claude Code** via Postgres MCP to a live Polymarket ledger containing roughly `1.3B` trades and `2.7M` wallets, allowing natural-language queries that Claude translates into SQL and executes; the linked writeup describes a similar setup using `@modelcontextprotocol/server-postgres` over pre-aggregated tables for ~`1.3B` trades across `1,560,894` wallets ([CrowdIntel](https://crowdintel.xyz/blog/claude-mcp-polymarket-ledger)). Reported findings include only ~`20%` of wallets being net profitable, `2.4%` clearing `$1,000` profit, and extreme profit concentration among the top `0.1%` of wallets, with the author also claiming Claude surfaced suspicious patterns suggestive of insider or bot-like trading.** Top commenters encouraged escalation to investigative journalists, including NYT/Forbes, and suggested more rigorous analyses: compare observed PnL distributions against a simulated “fair market” null model, and examine large losing wallets/bets as possible laundering or insider-transfer signals rather than simply retail losses.

    * One commenter suggested establishing a **baseline null model** for what Polymarket wallet/trade distributions _should_ look like under a fair market with no insider betting, then comparing those expected distributions against observed outcomes. They also recommended segmenting **large losing wallets/bets** to distinguish potential insider extraction from possible laundering behavior.
    * Another technical thread asked whether the analysis only covers wallets that participate directly in Polymarket markets, or whether it also performs **fund-flow tracing** to identify where capital originates and where winnings/losses are sent afterward. This would require graph analysis across wallet funding sources, withdrawals, and potentially linked addresses.
    * A commenter asked about the **data freshness / ingestion latency** : the lag between bets being placed and when they appear in the MCP-backed database. This matters for detecting time-sensitive anomalies such as pre-news betting, frontrunning, or post-resolution transaction patterns.
  * **[I Live by SFO and built a projection mapping of the planes flying over my house using ADS-B radio with claude code](https://www.reddit.com/r/ClaudeCode/comments/1tva44g/i_live_by_sfo_and_built_a_projection_mapping_of/)** (Activity: 3616): **The post showcases a home-built**projection-mapping visualization of aircraft flying over the author’s house near SFO** , driven by locally received **ADS-B radio** data and developed with **Claude Code**. The linked Reddit video ([v.redd.it/gl2b0xivvy4h1](https://v.redd.it/gl2b0xivvy4h1)) was not accessible due to a `403 Forbidden` block, and no implementation specifics—receiver hardware, SDR stack, decoding pipeline, calibration method, latency, or projection geometry—were provided in the available text.** Comments were broadly positive, framing it as a good example of “vibe coding,” with one commenter asking what equipment was required for the setup.

    * A commenter described a lower-cost implementation for Brazil that replaces the original ADS-B/Raspberry Pi-style hardware path with the **free OpenSky API** , a `US$40` AliExpress projector, and direct HDMI output from a personal PC. They added configurable latitude, longitude, and radius fields so the map recenters around user-provided coordinates, avoiding the need for a local ADS-B antenna that they estimated at about `US$100` plus expensive local hardware costs.
    * There was interest in making the project open source so others near airports could reuse it with their own projector setups, potentially combining the aircraft projection layer with other datasets such as constellation/star-map data.



### 3. Frontier AI Adoption and Risk Signals

  * **[Anthropic - Our internal data shows Claude is accelerating AI development—a possible path to recursive self-improvement, or AI autonomously building a more capable successor.](https://www.reddit.com/r/singularity/comments/1twsm5g/anthropic_our_internal_data_shows_claude_is/)** (Activity: 826): **The[image](https://i.redd.it/9ph4lq42la5h1.jpeg) is a screenshot of **Anthropic’s X post** promoting its article [“Recursive self-improvement”](https://www.anthropic.com/institute/recursive-self-improvement), claiming internal usage data shows **Claude is already accelerating AI R &D** and may indicate an early path toward AI systems helping build more capable successors. The technically significant claim is not a benchmark result but an organizational/empirical observation: Anthropic says Claude is enabling work such as exploratory tooling and deferred engineering cleanup, framing this as evidence relevant to **recursive self-improvement** and future AI control risks.** Comments were skeptical of the framing, with one user implying the announcement is financially motivated marketing. Another highlighted the “long-deferred cleanup” claim ironically, while a third provided the non-Twitter Anthropic article link and quoted its warning that AI-built successors could increase loss-of-control risks.

    * A commenter linked the full Anthropic Institute post on recursive self-improvement: https://www.anthropic.com/institute/recursive-self-improvement. The technically relevant claim highlighted is that Anthropic’s internal usage data suggests Claude is already enabling engineering work that _“simply wouldn’t have happened otherwise,”_ such as exploratory tooling and long-deferred cleanup, which Anthropic frames as an early signal on the path toward AI systems helping build more capable successors.
  * **[Sam Altman, Dario Amodei, and Demis Hassabis have signed a joint open letter calling on Congress to mandate screening of synthetic nucleic acid orders](https://www.reddit.com/r/singularity/comments/1two85g/sam_altman_dario_amodei_and_demis_hassabis_have/)** (Activity: 915): ****Sam Altman (OpenAI), Dario Amodei (Anthropic), and Demis Hassabis (Google DeepMind)** signed a joint open letter urging Congress to require screening of **synthetic nucleic acid orders** to reduce biosecurity risk from AI-assisted pathogen design, per the [WSJ report](https://www.wsj.com/politics/policy/top-ai-ceos-call-for-law-protecting-against-biological-weapons-88f2f99f). The proposed mechanism is not described as a ban on synthesis, but as mandatory order/customer screening to flag suspicious DNA/RNA sequences or buyers—roughly analogous to monitoring precursor purchases such as bulk fertilizer.** Commenters were broadly receptive to screening as a lightweight risk-control measure, while questioning whether AI-enabled “supervirus” design is practically feasible for non-experts today. Some framed the policy as a sensible suspicious-activity trigger rather than a direct restriction on legitimate genetic engineering.

    * Commenters framed the proposal as **order-level screening rather than a ban** , comparing it to monitoring suspicious bulk fertilizer purchases: the mechanism would flag potentially dangerous synthetic nucleic acid orders while preserving legitimate biotech access.
    * A technical concern raised was whether AI-assisted design of a “supervirus” is realistically feasible for non-experts. The implicit issue is that biological risk depends not just on model-generated sequences, but also on access to synthesis providers, wet-lab capability, delivery methods, and whether synthesis screening can catch pathogenic or engineered sequences.
  * **[ChatGPT makes history and becomes the fastest app to reach 1 billion monthly active users.](https://www.reddit.com/r/OpenAI/comments/1tvh4z4/chatgpt_makes_history_and_becomes_the_fastest_app/)** (Activity: 820): **The image is a screenshot of a**Kalshi** X post claiming **ChatGPT became the fastest app to reach`1 billion` monthly active users**: [image](https://i.redd.it/uwgx8zc9j05h1.jpeg). This is not a technical benchmark or implementation detail; its significance is mainly market/adoption context, positioning ChatGPT’s growth ahead of prior viral consumer apps like Threads, which commenters note reached `100 million` users in `5 days`.** Comments debate whether massive MAU translates into sustainable revenue, with one commenter estimating consumer subscription ARPU at roughly `$1/user` and joking that adding B2B might only raise it to `$2/user`.

    * Commenters focused on the reported user metrics and revenue implications: one notes the claim of **`1B` monthly active users** alongside roughly **`$1B` from consumer paid subscriptions**, implying consumer ARPU of about **`$1/user`** before enterprise/API revenue. Another commenter disputes the `1B` figure, citing a recent OpenAI CFO podcast where the number was reportedly **`900M` users**, arguing OpenAI would likely publicize a confirmed billion-user milestone more aggressively.
    * There is skepticism around monetization depth despite massive MAU: commenters ask how many of the reported users are actually **paid subscribers** , distinguishing headline MAU growth from recurring revenue, conversion rate, and enterprise/API monetization. The comparison to Threads’ earlier growth milestone—**`100M` users in 5 days**—frames ChatGPT’s scale as unusually fast but leaves unresolved whether active usage and paying-user retention match the headline adoption numbers.
  * **[AI Beat Law Professors At Answering Questions, Study Finds—And It Wasn’t Close](https://www.reddit.com/r/singularity/comments/1tvtojx/ai_beat_law_professors_at_answering_questions/)** (Activity: 1187): **A Stanford-linked study,[**“Law Professors Prefer AI Over Peer Answers”**](https://law.stanford.edu/publications/law-professors-prefer-ai-over-peer-answers/), reports a blinded evaluation in which `16` U.S. contracts law professors authored `40` short-answer tutoring questions and judged `2,918` anonymized human-vs-LLM answer comparisons. The LLM—identified in comments as **Gemini 2.5 Pro** —achieved an average win rate of `75.33%` over professor-written answers, performed similarly to the best instructor, and was flagged as harmful less often (`3.53%` vs. `12.06%` for professors); the abstract also proposes using an LLM-as-judge approach to scale evaluation in judgment-heavy domains.** Commenters debated implications beyond tutoring: one warned about premature institutional use of AI in legal decision-making or policing, while another argued this result reflects the broader post-“six fingers” maturation of LLM capability. A technical commenter suggested rerunning the benchmark with newer frontier models such as **GPT-5.5** , claiming it may be substantially stronger for legal work.

    * The linked Stanford study evaluated **LLM vs. law professor short-answer tutoring** using `16` U.S. contracts professors, `40` professor-authored questions, and `2,918` blinded pairwise comparisons. Professors preferred LLM answers with an average win rate of `75.33%`, while LLM answers were flagged as harmful only `3.53%` of the time versus `12.06%` for professor answers; the paper also claims expert-agreement data can be extended using a separate LLM-as-judge pipeline: https://law.stanford.edu/publications/law-professors-prefer-ai-over-peer-answers/.
    * One commenter highlighted that the study used **NotebookLM** and **Gemini 2.5 Pro** with tightly constrained prompts: answers had to mimic a contracts professor in office-hours style, avoid bullet points/filler, stay around `50–108` words, and for NotebookLM, rely only on provided textbook chapters without citing outside cases. This prompt design likely reduced hallucination risk and standardized answer format, making the benchmark more about concise legal reasoning/synthesis than open-ended legal research.
    * A technical argument was made that law is a strong fit for **RAG-style systems** because the profession depends on large corpora of statutes, case law, precedent, and theory that exceed individual recall capacity. The suggested workflow is retrieval over authoritative legal materials followed by synthesis, potentially outperforming unaided lawyers when the model is grounded in the relevant corpus.



# AI Discords

Unfortunately, Discord shut down our access today. We will not bring it back in this form but we will be shipping the new AINews soon. Thanks for reading to here, it was a good run.

---

## [Microsoft Build: MAI-Thinking-1 and MAI Family models, Surface RTX Spark Dev Box, and OpenClaw in Windows](https://news.smol.ai/issues/26-06-02-msft-mai-2/)
*🌐 Smol AI News | 2026-06-02*

**a quiet day.**

> AI News for 06/1/2026-6/2/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

# AI Twitter Recap

**Top Story: Microsoft Build recap, and new MAI model technical details**

## What happened

**Microsoft used Build to position itself as both an AI platform company and a frontier-model lab, pairing broad product launches with unusually detailed disclosures about its new MAI model family.**

  * Microsoft AI announced **seven new MAI models** spanning reasoning, code, image, speech transcription, and voice, led by **MAI-Thinking-1** , **MAI-Code-1-Flash** , **MAI-Image-2.5** , **MAI-Transcribe-1.5** , and **MAI-Voice-2** according to [@MicrosoftAI](https://x.com/MicrosoftAI/status/2061887500541366489) and [@mustafasuleyman](https://x.com/mustafasuleyman/status/2061880164498428188)
  * The flagship reasoning model **MAI-Thinking-1** was presented as Microsoft’s **first reasoning model** , built with **clean data lineage** and **zero distillation from third-party models** in posts from [@mustafasuleyman](https://x.com/mustafasuleyman/status/2061880164498428188), [@baseten](https://x.com/baseten/status/2061878701823066431), [@tuhinone](https://x.com/tuhinone/status/2061879239817969756), and [@HannaHajishirzi](https://x.com/HannaHajishirzi/status/2061901432627044430)
  * Microsoft released a **109-page technical report** for MAI-Thinking-1, which drew strong positive reactions from technically oriented readers for its level of transparency, including [@eliebakouch](https://x.com/eliebakouch/status/2061877335960281459), [@ethanCaballero](https://x.com/ethanCaballero/status/2061920873297088723), [@nrehiew_](https://x.com/nrehiew_/status/2062013300196700395), [@yacinelearning](https://x.com/yacinelearning/status/2061914159235617056), and [@stochasticchasm](https://x.com/stochasticchasm/status/2061916808626815161)
  * Microsoft also emphasized **local AI and agent-native Windows** : Build messaging highlighted **secure execution layers for agents** , a new **Surface RTX Spark Dev Box** , Windows AI access to the broader Windows GPU install base, and concept hardware such as **Project Solara/Scout** , summarized by [@yusuf_i_mehdi](https://x.com/yusuf_i_mehdi/status/2061882543641907528), [@TheTuringPost](https://x.com/TheTuringPost/status/2061865165734506683), [@kimmonismus](https://x.com/kimmonismus/status/2061860319547527191), and [@kimmonismus](https://x.com/kimmonismus/status/2061875714933371220)
  * Build also included a major **GitHub Copilot app** push as the “desktop home for agent-native software development,” with **canvases** , cross-device continuity, and tighter GitHub agent workflows, from [@pierceboggan](https://x.com/pierceboggan/status/2061868635241828688), [@lukehoban](https://x.com/lukehoban/status/2061905434039246939), and reactions from [@techgirl1908](https://x.com/techgirl1908/status/2061870470237164018)
  * Microsoft introduced **Web IQ** , a new grounding/search API stack for AI agents, claiming the APIs already power “nearly all AI agents and chatbots in the industry today, including Copilot and ChatGPT,” via [@JordiRib1](https://x.com/JordiRib1/status/2061866606670581871)
  * Satya Nadella framed Build as an ecosystem moment rather than a single-product launch, while Mustafa Suleyman framed it as the output of Microsoft’s internal “hill-climbing machine,” in [@satyanadella](https://x.com/satyanadella/status/2061896503304806521), [@mustafasuleyman](https://x.com/mustafasuleyman/status/2061934667096596657), and reaction from [@nrehiew_](https://x.com/nrehiew_/status/2061983583523475556)



## MAI model family: disclosed facts and technical details

### MAI-Thinking-1

  * Microsoft described **MAI-Thinking-1** as a **35B active parameter MoE** with a **256K context window** in [@mustafasuleyman](https://x.com/mustafasuleyman/status/2061880164498428188)
  * A separate summary from [@scaling01](https://x.com/scaling01/status/2061889624847343825) says the model is a **1T@35B parameter model** , **pre-trained on 30T tokens** , and trained using **8192 GB200 GPUs** ; this appears to be a reading of the technical report rather than Microsoft marketing copy
  * [@kimmonismus](https://x.com/kimmonismus/status/2061877528781025381) similarly summarized it as a **mid-size MoE with 45B active params** , but this conflicts with Mustafa’s own **35B active** figure; the more authoritative figure in the tweet set is the official **35B active** number
  * Microsoft claims **97% on AIME 2025** and **53% on SWE-Bench Pro** , with blind human raters on Surge preferring it overall to **Sonnet 4.6** , from [@mustafasuleyman](https://x.com/mustafasuleyman/status/2061880164498428188) and [@asadovsky](https://x.com/asadovsky/status/2062008312603070891)
  * Microsoft says the model is **optimized on MAIA 200** , with **30% better performance per dollar** and **1.4x performance-per-watt gain** versus **GB200** when running MAI models end-to-end, per [@mustafasuleyman](https://x.com/mustafasuleyman/status/2061880164498428188)
  * Microsoft and partners repeatedly stressed **no third-party distillation** , “clean data lineage,” and enterprise-controlled fine-tuning with “100% eyes-off” post-training data through Baseten, in [@baseten](https://x.com/baseten/status/2061878701823066431), [@tuhinone](https://x.com/tuhinone/status/2061879239817969756), and [@MicrosoftAI](https://x.com/MicrosoftAI/status/2061923309344756043)



### MAI-Code-1-Flash

  * Microsoft introduced **MAI-Code-1-Flash** as a fast coding model for **VS Code** and **GitHub Copilot CLI** , first announced by [@pierceboggan](https://x.com/pierceboggan/status/2061877165810131297) and later highlighted by [@mariorod1](https://x.com/mariorod1/status/2061914993550143513)
  * Official Microsoft messaging via [@mustafasuleyman](https://x.com/mustafasuleyman/status/2061880164498428188) says **Code-1-Flash achieves 51% on SWE-Bench Pro despite having just 5B parameters** , positioning it near Haiku-class size/cost
  * A competing summary from [@scaling01](https://x.com/scaling01/status/2061891478176112794) describes it as a **137B parameter MoE** , **256K context** , trained on **10T+ tokens** , and “stronger and more efficient than Claude 4.5 Haiku.” That likely indicates **5B active parameters** rather than total parameters; the tweets do not fully reconcile this distinction, but together imply **small active footprint within a much larger MoE**
  * Availability at launch was highlighted as **GitHub Copilot / VS Code-first** , per [@scaling01](https://x.com/scaling01/status/2061891478176112794) and [@mariorod1](https://x.com/mariorod1/status/2061914993550143513)



### MAI-Image-2.5

  * Microsoft launched **MAI-Image-2.5** and a **Flash** variant, claiming both reached **#2 on leaderboards** , with [@mustafasuleyman](https://x.com/mustafasuleyman/status/2061880164498428188) saying they surpass **Nano Banana 2** on image editing
  * Independent leaderboard accounts supported the high ranking: [@arena](https://x.com/arena/status/2061887242579382660) reported **#2 in Image Edit Arena** with **score 1401** , **+10 points over Nano Banana 2** , Grok Imagine, and ChatGPT Image Latest HF
  * [@arena](https://x.com/arena/status/2061894541888962712) further said MAI-Image-2.5 “advances the Pareto frontier,” meaning no model at its price tier scores higher on that benchmark
  * Distribution partners quickly followed, including [@OpenRouter](https://x.com/OpenRouter/status/2061894672847671724) and [@fal](https://x.com/fal/status/2061920052664820199)



### MAI-Transcribe-1.5

  * [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2061878491860324402) reported **MAI-Transcribe-1.5** as an unusually strong speed/accuracy point on the STT frontier: **~276x realtime** , **2.4% AA-WER** , **#3 overall** on its leaderboard
  * The model supports **43 languages** , including English, French, Arabic, Japanese, and Chinese, and supports **keyword biasing** for rarer terms such as names and medical terminology, per [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2061878491860324402)
  * Pricing was reported as **$6 per 1,000 minutes of audio** via Microsoft Foundry in [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2061878498609053909)
  * OpenRouter also listed the model among the three MAI launches it brought live the same day in [@OpenRouter](https://x.com/OpenRouter/status/2061894672847671724)



### MAI-Voice-2

  * MAI-Voice-2 appears in Microsoft’s “seven models” umbrella and in OpenRouter’s availability post at [@OpenRouter](https://x.com/OpenRouter/status/2061894672847671724)
  * The tweet set contains little technical detail on Voice-2 itself beyond launch/availability



## Technical-report details that mattered to researchers

### Why the report stood out

  * The dominant technical reaction was that Microsoft released an unusually detailed frontier-model report: [@eliebakouch](https://x.com/eliebakouch/status/2061965825037254947) called it “one of the most transparent for a model at this scale,” [@nrehiew_](https://x.com/nrehiew_/status/2062023547690828141) said it “could really serve as an updated textbook for LLM training today,” and [@stochasticchasm](https://x.com/stochasticchasm/status/2061879506139557979) called it a “gold mine”
  * Multiple readers highlighted that the report disclosed **pipeline details, scaling ladder methodology, data curation, infra metrics, and MFU numbers** ; this level of specificity is what drew praise from [@ethanCaballero](https://x.com/ethanCaballero/status/2061920873297088723), [@eliebakouch](https://x.com/eliebakouch/status/2062004670017486912), and [@nrehiew_](https://x.com/nrehiew_/status/2062013300196700395)



### Pretraining and data

  * A major technical claim repeated across commentary is that MAI-Thinking-1 used **no synthetic data** and **no distillation** , not only in post-training but throughout the disclosed pipeline, from [@eliebakouch](https://x.com/eliebakouch/status/2061965825037254947), [@stochasticchasm](https://x.com/stochasticchasm/status/2061967095022366924), and [@HannaHajishirzi](https://x.com/HannaHajishirzi/status/2061901432627044430)
  * [@eliebakouch](https://x.com/eliebakouch/status/2061977834558804207) says the report explicitly notes data from **Common Crawl plus private sources** , with **targeted sub-pipelines for different domains** , heavy extraction/dedup work, and an intentional choice of **no synthetic data**
  * The report’s internal **private NLL set** used for scaling decisions was summarized by [@eliebakouch](https://x.com/eliebakouch/status/2061976608265880004) as: 
    * **50% code**
    * **17.5% STEM**
    * **17.5% math**
    * **10% general knowledge**
    * **5% multilingual**
  * [@eliebakouch](https://x.com/eliebakouch/status/2061976230933496176) says architecture promotion in the scaling ladder was based on an **Efficiency Gain (EG)** metric: how much extra compute the baseline would need to match the candidate’s loss
  * The same thread notes ablations at roughly **100/200 tokens per parameter** , described as around “Chinchilla optimal” for the setup, while also remarking this differs from dense-model heuristics due to MoE structure in [@eliebakouch](https://x.com/eliebakouch/status/2061975730414633043)



### Post-training / RL

  * The most discussed technical choice was that Microsoft appears to have started RL from a checkpoint with **no prior reasoning exposure** , which several readers found notable. [@stochasticchasm](https://x.com/stochasticchasm/status/2061879070141677615) called this a “very interesting decision,” while [@stochasticchasm](https://x.com/stochasticchasm/status/2061878066314645861) reacted to graphs suggesting a jump from **< 20% AIME25 to >95%**
  * [@HannaHajishirzi](https://x.com/HannaHajishirzi/status/2061901432627044430) described the “climbing from scratch” recipe as **simple recipes, rigorous science, self-distillation, patience, and great infra**
  * [@soldni](https://x.com/soldni/status/2061882085573616003) characterized the process as “climbing with no distillation, like the big boys do”
  * Some independent readers inferred from the report that **synth data remains very valuable** for agentic performance in the broader field, even if Microsoft deliberately avoided it here; see [@stochasticchasm](https://x.com/stochasticchasm/status/2061961874879783376)



### Data curation / judges / DSPy GEPA

  * A detail that got substantial attention from the DSPy/late-interaction crowd: Microsoft reportedly used **GEPA / DSPy-optimized LLM judges** in pretraining data curation and quality scoring
  * This was highlighted by [@bj2rn](https://x.com/bj2rn/status/2061941109828301241), [@LakshyAAAgrawal](https://x.com/LakshyAAAgrawal/status/2062013650639241403), and [@lateinteraction](https://x.com/lateinteraction/status/2062015109132873852)



### Infra / utilization / hardware co-design

  * Microsoft reportedly disclosed **exact MFU across iterations** , which multiple readers said is rarely shared at this scale, per [@eliebakouch](https://x.com/eliebakouch/status/2061965825037254947)
  * [@scaling01](https://x.com/scaling01/status/2061889624847343825) summarized the run as using **8192 GB200 GPUs**
  * [@eliebakouch](https://x.com/eliebakouch/status/2062004120098144764) singled out a reported **~40% higher throughput per watt** -type figure as “pretty impressive and bullish on microsoft chips,” though this may refer to rack-level budget or serving configuration and was not fully unpacked in-tweet
  * Microsoft’s official framing connected model design to **MAIA 200** custom silicon and emphasized better **performance-per-dollar** and **performance-per-watt** vs NVIDIA GB200 in [@mustafasuleyman](https://x.com/mustafasuleyman/status/2061880164498428188)
  * Build’s broader Windows/local-AI narrative also centered on hardware specifics such as: 
    * **1 trillion parameters running locally on DGX Station**
    * **128GB unified memory**
    * **110 TOPS AI performance**
    * **20 CPU cores**
    * **70+ PowerToys utilities** from [@TheTuringPost](https://x.com/TheTuringPost/status/2061852480636653924)
  * Reactions also pointed to local runs of large models, e.g. [@kimmonismus](https://x.com/kimmonismus/status/2061852979318427988) on **RTX Spark running a 120B parameter model locally**



## Build product/platform recap beyond the models

### GitHub Copilot app and agent-native development

  * GitHub unveiled the **GitHub Copilot app** , pitched as a desktop surface for **agent-native software development** by [@pierceboggan](https://x.com/pierceboggan/status/2061868635241828688)
  * Key themes included: 
    * **canvases** for bidirectional work between users and agents, per [@Techmeme](https://x.com/Techmeme/status/2061875738694062419)
    * continuity across **CLI, mobile, web, local, and cloud** , per [@lukehoban](https://x.com/lukehoban/status/2061905448287322243)
    * a growing role for GitHub as the center of agent workflows, reflected in [@techgirl1908](https://x.com/techgirl1908/status/2061870470237164018) and [@OrenMe](https://x.com/OrenMe/status/2061873010664001605)
  * Copilot CLI also got an experimental **terminal UI with tabs, built-in feedback/rubber duck, prompt scheduling, and voice input** , per [@GHchangelog](https://x.com/GHchangelog/status/2061870684876272123)



### Windows as an agent runtime

  * Microsoft’s Windows org framed Build around “faster developer execution, a secure execution layer for agents, and unmetered intelligence that runs locally on device,” per [@yusuf_i_mehdi](https://x.com/yusuf_i_mehdi/status/2061882543641907528)
  * Several posts stressed that Microsoft wants **Windows** to be the trusted execution platform for agents, not just Azure
  * [@TheTuringPost](https://x.com/TheTuringPost/status/2061865165734506683) described **Project Solara** as a platform for **agent-first devices** , with concepts including: 
    * a **desktop AI companion**
    * a **wearable badge** with cameras, microphones, sensors, and secure authentication
  * [@kimmonismus](https://x.com/kimmonismus/status/2061860319547527191) saw these as handheld/desktop devices for controlling agents and compared them to expectations people had for standalone OpenAI hardware
  * [@kimmonismus](https://x.com/kimmonismus/status/2061875714933371220) separately highlighted **Microsoft Scout** as an “always-on personal agent for work”



### Web IQ and search for agents

  * [@JordiRib1](https://x.com/JordiRib1/status/2061866606670581871) announced **Microsoft Web IQ** as a suite of **AI-native grounding APIs** for **web pages, news, images, and videos**
  * His framing is important context: classic search engines were built for humans, but Microsoft believes future search demand will come from agents, potentially **1000x more queries** than human search traffic
  * He claimed Web IQ was re-architected from Bing’s stack for **quality, latency, and token efficiency** , and that it already powers major chatbots including **Copilot and ChatGPT**



### Foundry and open-model distribution

  * [@jeffboudier](https://x.com/jeffboudier/status/2061868927207244277) said Satya cited **11,000+ models available in Microsoft Foundry** , of which **10,928** come from Hugging Face
  * This supports Microsoft’s parallel identity at Build: both a first-party model builder and a large multi-model hosting/distribution platform



### Build messaging around datacenters and compute

  * Several observers noted Build discussion around **data center expansion** , community backlash, and Microsoft’s argument that AI infra can expand without raising electricity costs to local communities; see [@kimmonismus](https://x.com/kimmonismus/status/2061854806395015316) and [@kimmonismus](https://x.com/kimmonismus/status/2061903253890330639)
  * [@scaling01](https://x.com/scaling01/status/2061901702324695115) highlighted Mustafa saying AI compute will grow **1000x in the next 3 years** , taking today’s rough **5e27 FLOPs** frontier scale to **5e30 FLOPs by 2029**
  * [@mustafasuleyman](https://x.com/mustafasuleyman/status/2061880029315764256) summarized the company’s philosophical theme as **“Humanist superintelligence”**



## Facts vs. opinions

### Factual claims in the tweet set

  * Microsoft launched **seven new MAI models** at Build: [@MicrosoftAI](https://x.com/MicrosoftAI/status/2061887500541366489)
  * Official metrics for MAI-Thinking-1: **35B active MoE** , **256K context** , **97% AIME 2025** , **53% SWE-Bench Pro** , and blind human preference over Sonnet 4.6: [@mustafasuleyman](https://x.com/mustafasuleyman/status/2061880164498428188)
  * Official metrics for MAI-Code-1-Flash: **51% SWE-Bench Pro** , **5B parameters** as stated in tweet copy: [@mustafasuleyman](https://x.com/mustafasuleyman/status/2061880164498428188)
  * MAI-Image-2.5 ranking claims were independently echoed by [@arena](https://x.com/arena/status/2061887242579382660)
  * MAI-Transcribe-1.5 speed/accuracy details came from independent benchmark account [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2061878491860324402)
  * Microsoft released a **109-page technical report** : [@eliebakouch](https://x.com/eliebakouch/status/2061877335960281459)



### Opinions / interpretations

  * “Microsoft is training serious models now?” from [@teortaxesTex](https://x.com/teortaxesTex/status/2061892492350407158) is an interpretive reaction to the model/report quality, not a standalone fact
  * Claims that the report is “one of the most transparent” or “an updated textbook” are opinions from [@eliebakouch](https://x.com/eliebakouch/status/2061965825037254947) and [@nrehiew_](https://x.com/nrehiew_/status/2062023547690828141), albeit shared by many readers
  * [@kimmonismus](https://x.com/kimmonismus/status/2061852480636653924) and [@TheTuringPost](https://x.com/TheTuringPost/status/2061865165734506683) framed Build as a strategic shift from cloud-only AI toward local reasoning/agents; that is analysis rather than official wording
  * Posts claiming Microsoft “leaked” Anthropic Mythos FLOPs, including [@swyx](https://x.com/swyx/status/2061878629504881151) and [@scaling01](https://x.com/scaling01/status/2061897540161728791), are speculative interpretations of a slide, later contested by the same cluster of commenters



## Different opinions and perspectives

### Supportive views

  * Technical readers were broadly impressed by the **report’s transparency** and Microsoft’s willingness to publish details usually withheld at this scale: [@eliebakouch](https://x.com/eliebakouch/status/2061965825037254947), [@nrehiew_](https://x.com/nrehiew_/status/2062023547690828141), [@ethanCaballero](https://x.com/ethanCaballero/status/2061920873297088723), [@stochasticchasm](https://x.com/stochasticchasm/status/2061916808626815161)
  * Some saw MAI-Thinking-1 as proof Microsoft is becoming a genuine frontier lab rather than just a model reseller or application layer, e.g. [@teortaxesTex](https://x.com/teortaxesTex/status/2061892492350407158), [@echen](https://x.com/echen/status/2061907282607100075), [@NandoDF](https://x.com/NandoDF/status/2061901884042985728)
  * Enterprise/platform supporters liked the **clean-data-lineage** , **fine-tunable** , **eyes-off post-training data** story, especially Baseten/Microsoft’s positioning around ownership and control: [@baseten](https://x.com/baseten/status/2061878701823066431), [@tuhinone](https://x.com/tuhinone/status/2061879239817969756)



### Neutral / analytical views

  * Several posts focused on **reading and unpacking the report** rather than cheering the launch, especially [@stochasticchasm](https://x.com/stochasticchasm/status/2061916808626815161), [@nrehiew_](https://x.com/nrehiew_/status/2062013300196700395), and [@eliebakouch](https://x.com/eliebakouch/status/2061965825037254947)
  * Some commentators were careful on benchmark interpretation. [@kimmonismus](https://x.com/kimmonismus/status/2061918020843557110) noted Microsoft appeared to compare to **Sonnet 4.6** generally, with **Opus-level comparability only on SWE Pro**
  * [@iScienceLuvr](https://x.com/iScienceLuvr/status/2061926066453962952) specifically appreciated reporting on **health benchmarks** such as HealthBench Professional and MedXpertQA rather than only coding/math



### Skeptical / opposing views

  * A subset questioned whether all numbers and comparisons were being interpreted correctly, especially around active params and external-model comparisons
  * The most visible skepticism concerned the apparent **Mythos FLOP “leak”**. [@iScienceLuvr](https://x.com/iScienceLuvr/status/2061882397340393514) suggested it was probably just an estimate, not a leak; [@scaling01](https://x.com/scaling01/status/2061989029025853757) later argued the original **6.1e27 FLOP** figure was unrealistic and supplied a lower alternative estimate before posting a correction in [@scaling01](https://x.com/scaling01/status/2061990840138899674)
  * There was also implicit skepticism in the field about whether **zero synth / zero distillation** is the right long-term recipe for best agentic performance, as noted by readers emphasizing synth-data deltas elsewhere, e.g. [@stochasticchasm](https://x.com/stochasticchasm/status/2061961874879783376)



## Context: why this matters

  * Build’s announcements matter because they suggest Microsoft is no longer content with being only: 
    1. Azure/OpenAI’s cloud host
    2. GitHub’s developer surface
    3. Copilot’s application shell  
It is also trying to be a **first-party frontier model developer** with its own model family, silicon stack, and post-training platform
  * The **clean lineage / no distillation** emphasis is strategically significant. It addresses enterprise concerns around IP provenance, future controllability, and dependence on external labs
  * The **local AI** emphasis matters because Microsoft is tying AI strategy to Windows and device distribution, not just to Azure. Build messaging repeatedly pushed the idea that reasoning models, planners, and agents can increasingly run **on-device** , not only in the cloud: [@TheTuringPost](https://x.com/TheTuringPost/status/2061852480636653924), [@yusuf_i_mehdi](https://x.com/yusuf_i_mehdi/status/2061882543641907528)
  * The **109-page report** matters because frontier-model transparency has generally been shrinking, especially around data, infra, and training methodology. Multiple researchers explicitly noted the disclosure level is uncommon at this scale: [@eliebakouch](https://x.com/eliebakouch/status/2061965825037254947), [@nrehiew_](https://x.com/nrehiew_/status/2062023547690828141)
  * The Build recap also showed Microsoft trying to integrate all layers of the stack: 
    * **models** : MAI family
    * **chips** : MAIA 200
    * **cloud** : Azure + Foundry
    * **OS** : Windows agent runtime
    * **developer UX** : Copilot app / VS Code / CLI
    * **retrieval/grounding** : Web IQ
    * **hardware form factors** : Solara / Scout concepts
  * This combination is why several observers described the event less as a normal dev conference and more as a coordinated move toward an **agent platform spanning cloud, edge, OS, and custom models** , e.g. [@satyanadella](https://x.com/satyanadella/status/2061896503304806521), [@mustafasuleyman](https://x.com/mustafasuleyman/status/2061934667096596657), and [@TheTuringPost](https://x.com/TheTuringPost/status/2061865165734506683)



## The “Mythos FLOPs leak” mini-story

  * During/after Build, some users claimed a Microsoft slide inadvertently revealed training compute for Anthropic’s rumored **Claude Mythos** , with [@swyx](https://x.com/swyx/status/2061878629504881151) asking if Mustafa had leaked the FLOP count
  * [@scaling01](https://x.com/scaling01/status/2061897540161728791) estimated the slide implied **6.1e27 FLOPs** with a confidence interval based on pixel measurement, while [@kimmonismus](https://x.com/kimmonismus/status/2061908067034517853) noted that would be around **Gemini 3.1 Pro-scale** compute
  * That interpretation was subsequently challenged by [@iScienceLuvr](https://x.com/iScienceLuvr/status/2061882397340393514), who argued it was probably an estimate, and then by [@scaling01](https://x.com/scaling01/status/2061989029025853757), who posted a lower-range model-based estimate of **3.37e26 to 1.46e27 FLOPs** and later said the original numbers were **bogus** in [@scaling01](https://x.com/scaling01/status/2061990840138899674)
  * The episode is useful mostly as context: Build’s compute/scaling messaging was detailed enough that people started trying to infer competitor training budgets from presentation materials



**Developer tools, agents, and coding workflows**

  * OpenAI launched **Sites in Codex** , letting teams turn ideas/docs/plans into deployed internal websites/apps with auth and dynamic data, first for business/enterprise users, in [@OpenAI](https://x.com/OpenAI/status/2061845949170045346), [@TheRohanVarma](https://x.com/TheRohanVarma/status/2061872164442403139), and [@gdb](https://x.com/gdb/status/2061988413105156128)
  * OpenAI also expanded **role-specific Codex plugins** across sales, data analytics, creative production, product design, and public equity workflows, with access to **62 apps and 110 skills** , from [@OpenAI](https://x.com/OpenAI/status/2061887650391625870) and [@OpenAIDevs](https://x.com/OpenAIDevs/status/2061888366791246071)
  * GitHub’s **Copilot app** and Microsoft’s Build push around agent-native software development were central to the day’s tooling news: [@pierceboggan](https://x.com/pierceboggan/status/2061868635241828688), [@lukehoban](https://x.com/lukehoban/status/2061905434039246939), [@GHchangelog](https://x.com/GHchangelog/status/2061870684876272123)
  * Anthropic shipped a **CLI for Claude Platform** and upgraded Claude Code’s `/fork` to run a background agent with exact context + prompt cache, in [@ClaudeDevs](https://x.com/ClaudeDevs/status/2061877343078244459) and [@ClaudeDevs](https://x.com/ClaudeDevs/status/2061947411141169494)
  * Nous launched **Hermes Desktop** , a local/native desktop surface for Hermes agents, in [@NousResearch](https://x.com/NousResearch/status/2061843507417944552), [@Teknium](https://x.com/Teknium/status/2061844602735538266), and later Tailscale/Ollama integration notes from [@Teknium](https://x.com/Teknium/status/2061984430370267210) and [@ollama](https://x.com/ollama/status/2062011585355551231)
  * Cognition launched **Devin Desktop** , positioned as an agent-neutral desktop for managing local/cloud agents and handoff between local planning and cloud execution, in [@cognition](https://x.com/cognition/status/2061889596703551926), [@ScottWu46](https://x.com/ScottWu46/status/2061998361373532187), and [@russelljkaplan](https://x.com/russelljkaplan/status/2061920322325205007)



**Models, local inference, and routing**

  * H Company launched **Holo 3.1** , a local computer-use model family based on Qwen-style architecture, with checkpoints from **0.8B to 35B** and formats including **NVFP4, FP8, and Q4 GGUF** ; a popular summary cited **79.3% on AndroidWorld** for the 35B model in [@TeksEdge](https://x.com/TeksEdge/status/2061825310669332818), with launch tweet from [@hcompany_ai](https://x.com/hcompany_ai/status/2061815355341725925)
  * Perplexity announced **hybrid agentic inference** for Perplexity Computer, splitting work between **local models on-device** and frontier cloud models for privacy and token efficiency, in [@perplexity_ai](https://x.com/perplexity_ai/status/2061861293569765847) and [@AravSrinivas](https://x.com/AravSrinivas/status/2061875858542096520)
  * OpenRouter data shared by [@ttunguz](https://x.com/ttunguz/status/2061846636805177692) showed **open-weight models at 69.1% of token volume** , versus **30.9%** for closed models
  * Commentary around **model routing** as a key future abstraction came from [@ClementDelangue](https://x.com/ClementDelangue/status/2061871024627482964), [@garrytan](https://x.com/garrytan/status/2061878212213572083), [@matanSF](https://x.com/matanSF/status/2061865185527074914), and the counterpoint from [@glennko](https://x.com/glennko/status/2061896887699964171), who argued enterprise production reliability makes generic routing harder than enthusiasts suggest
  * Local-AI UX improvements also appeared in Hugging Face’s **hardware compatibility checks** and oMLX’s native macOS app release from [@m_newhaus](https://x.com/m_newhaus/status/2061824017510584630) and [@jundotkim](https://x.com/jundotkim/status/2061863850874634242)



**Research and evals**

  * Google DeepMind announced **Co-Scientist** , a Gemini-based multi-agent hypothesis generation system for science, claiming collaborations that helped identify liver fibrosis targets, ALS approaches, and genetic leads for aging, in [@GoogleDeepMind](https://x.com/GoogleDeepMind/status/2061857539977842793), [@GoogleDeepMind](https://x.com/GoogleDeepMind/status/2061857550438392094), and [@GoogleDeepMind](https://x.com/GoogleDeepMind/status/2061857553076920643)
  * The new **Crafter / CraftEditor** work on editable scientific figure generation drew attention as a five-agent workflow for producing and refining figures plus raster-to-SVG conversion, in [@HuggingPapers](https://x.com/HuggingPapers/status/2061800325959324069), [@_akhaliq](https://x.com/_akhaliq/status/2061835314599993392), and [@TheTuringPost](https://x.com/TheTuringPost/status/2061883014410629400)
  * Tilde Research introduced **Wall Attention** , a RoPE-free attention method with diagonal forget gates, claiming training at **4k** and generalization to **200k+** tokens plus Triton kernels and strong decode throughput, in [@tilderesearch](https://x.com/tilderesearch/status/2061839600562409581)
  * A robotics vision encoder claiming **+22.5% real-world OOD success** by encoding dynamics-awareness rather than relying on static-image pretraining was posted by [@jbhuang0604](https://x.com/jbhuang0604/status/2061840469966090308)
  * New evals/benchmarks of note: 
    * **PaintBench** for precise image editing, where best model reached only **17.1%** , from [@itskaixu](https://x.com/itskaixu/status/2061827068170518956)
    * **VSTAT** for video state tracking, arguing frontier MLLMs remain weak at tracking evolving world state, from [@PinzhiHuang](https://x.com/PinzhiHuang/status/2062004108249145442) and [@sainingxie](https://x.com/sainingxie/status/2062011403733512253)
    * **Data Agent Benchmark** for enterprise data workflows, from [@sh_reya](https://x.com/sh_reya/status/2061984097531310378)



**Inference, infrastructure, and agent systems**

  * Harvey + LangChain shared work on **cheap verifiers** for legal agents, showing **DeepSeek V4 Flash** could preserve **94–96% agreement** with Opus 4.7 while reducing cost **18x** in per-criterion mode and **~1000x** in batch mode; for **3,200 RL rollouts** , verification cost dropped from **$18,000 to $18** , in [@harvey](https://x.com/harvey/status/2061866491033899371), [@hwchase17](https://x.com/hwchase17/status/2061867746141356427), and [@nikogrupen](https://x.com/nikogrupen/status/2061866707988431039)
  * W&B relaunched **Weave** as agent-first observability with integrations across common harnesses and automated detection of failure modes, in [@wandb](https://x.com/wandb/status/2061894943203831996) and [@neutralino1](https://x.com/neutralino1/status/2061949197851742525)
  * Prime-RL integrated **Mooncake Store** with vLLM for cross-node prefix / KV cache reuse, pitched as key for agentic rollouts, in [@m_sirovatka](https://x.com/m_sirovatka/status/2061862853997465738)
  * Together detailed serving optimizations for **MiniMax-M3** , citing **81–125% throughput improvements** via KV-block-major sparse attention, paged decode, optimized index scoring, and multimodal preprocessing, in [@togethercompute](https://x.com/togethercompute/status/2061895336486949109)
  * MiniMax itself highlighted **1M context** , native multimodality, desktop-computer operation, and MSA reducing attention’s share of decode time from **~30% to ~5%** , in [@MiniMax_AI](https://x.com/MiniMax_AI/status/2061944204604101020)



**Ecosystem, hardware, and industrial capacity**

  * Westmag emerged from stealth to build **American robot actuators and drone motors** , with **$11M raised** led by a16z and participation from Founders Fund, Lux, NFDG, Menlo and others, in [@boxcardavid](https://x.com/boxcardavid/status/2061825303715123234), [@packyM](https://x.com/packyM/status/2061835223470330100), and [@oyhsu](https://x.com/oyhsu/status/2061837257531670864)
  * PyTorch noted NVIDIA adoption of **OpenMDW-1.1** , a permissive AI-model licensing framework, across four open-model families in [@PyTorch](https://x.com/PyTorch/status/2061840384817328604)
  * Martin Scorsese publicly demonstrated narrow, preproduction use of **FLUX** for storyboarding with Black Forest Labs, framed as exploratory and complementary to hand-drawn work rather than generative replacement, in [@robrombach](https://x.com/robrombach/status/2061804823352086681) and [@TheRundownAI](https://x.com/TheRundownAI/status/2061834880917357011)



* * *

# AI Reddit Recap

## /r/LocalLlama + /r/localLLM Recap

### 1. NVIDIA Nemotron 3 Ultra and RTX Spark Specs

  * **[NVIDIA announces Nemotron 3 Ultra](https://www.reddit.com/r/LocalLLaMA/comments/1tthkh5/nvidia_announces_nemotron_3_ultra/)** (Activity: 669): **The image shows**NVIDIA announcing Nemotron 3 Ultra** , presented as a `550B`-parameter open-weight model in a “Frontier Smart” benchmark table, with comparisons against **GLM 5.1, Kimi K2.6, and Qwen3.5** across agent productivity, coding, instruction following, and long-context tasks. A commenter clarifies it is likely a **MoE`550B-A55`** model, while another notes its reported “artificial analysis score” of `48`, described as just below “frontier” and roughly in the **MiniMax 2.7** range; image: <https://i.redd.it/f79wu6dnml4h1.jpeg>.** Commenters appreciated that NVIDIA benchmarked against other open-source/open-weight models, but there was limited technical debate beyond positioning it as potentially the strongest U.S. open-weight model.

    * Commenters identify **NVIDIA Nemotron 3 Ultra** as a **MoE`550B-A55`** model, implying roughly `550B` total parameters with about `55B` active parameters per token. Technical discussion centered on its positioning as a large open-weight mixture-of-experts model rather than a dense frontier-class release.
    * A benchmark-focused comment cites an **Artificial Analysis score of`48`**, described as “one notch less than frontier” and roughly in the **MiniMax`2.7`** range, while another notes NVIDIA’s comparisons against other open-source/open-weight models. Links shared include NVIDIA’s [Nemotron-3-Ultra-Base usage cookbook](https://github.com/NVIDIA-NeMo/Nemotron/tree/main/usage-cookbook/Nemotron-3-Ultra-Base) and the [LifeArchitect models table](https://lifearchitect.ai/models-table/).
    * There was skepticism about NVIDIA comparing Nemotron 3 Ultra to **Qwen3.5** , with one commenter arguing the comparison was likely chosen to frame it as the “best **open weight** ” U.S. model despite losing to stronger non-U.S. or broader frontier competitors. The technical takeaway is that its competitive claim may depend heavily on the subset of models considered: open-weight, U.S.-origin, and benchmark selection.
  * **[RTX Spark does not have 600GB/s Bandwith](https://www.reddit.com/r/LocalLLaMA/comments/1tu639j/rtx_spark_does_not_have_600gbs_bandwith/)** (Activity: 693): **The slide clarifies that**NVIDIA’s RTX Spark Superchip** does **not** have `600 GB/s` memory bandwidth: its unified memory is listed as **128 GB LPDDR5X at`300 GB/s`**, while `600 GB/s` refers to **NVLINK-C2C** bandwidth between the Blackwell RTX GPU and Grace CPU. The post argues that outlets reporting `600 GB/s` as memory bandwidth misread the Computex slide; the image shows specs including **6144 CUDA cores** , **1 PFLOP FP4 AI performance** , and a **20-core Grace CPU**. [Image](https://i.redd.it/lzttip99mq4h1.png)** Commenters are broadly critical of the product positioning, calling it an overpriced cut-down chip with weak I/O and disputing comparisons to an RTX 5070, with one commenter claiming it is “below a 3060 Ti.” There is also a recurring complaint about NVIDIA’s CUDA lock-in and a desire for more hardware-agnostic alternatives.

    * A commenter argues the reported `600GB/s` bandwidth was likely a media/LLM propagation error, because **GB10/N1/N1X** appear to use the same underlying silicon with only thermal-profile differences. They describe the package as **two dies connected via NVLink on TSMC CoWoS** , where the GPU die has no direct I/O or memory controllers, leaving the CPU die to handle memory and other I/O.
    * The same technical analysis claims die-edge constraints make higher memory-channel counts implausible: the CPU die edge facing the GPU is consumed by NVLink, leaving only three sides for I/O including memory controllers. Based on the physical “shoreline” required for each `32-bit` memory channel, they estimate the design is limited to **4 memory channels** , matching GB10, with the only likely change being LPDDR speed increasing from `8533 MT/s` to `9500 MT/s`.
    * One thread frames NVIDIA pricing and positioning as a CUDA lock-in problem, arguing that real competition requires moving away from **CUDA** toward hardware-agnostic software stacks. The commenter speculates that LLM-assisted porting of CUDA-dependent code could eventually reduce NVIDIA’s moat by making alternative accelerators easier to target.



### 2. Local-First AI Privacy and Censorship Tests

  * **[Minimax M3 appears to have no political censorship](https://www.reddit.com/r/LocalLLaMA/comments/1tuv1sv/minimax_m3_appears_to_have_no_political_censorship/)** (Activity: 689): **The image ([screenshot](https://i.redd.it/vgkda1ua5w4h1.png)) is **not a meme** ; it shows **MiniMax M3** answering a politically sensitive prompt about the **1989 Tiananmen Square protests** with a relatively uncensored summary, including martial law, PLA use of tanks/live ammunition, civilian deaths, international condemnation, and ongoing censorship in China. The post frames this as an outlier in a Chinese/CCP AI-bias benchmark, since the author says other **MiniMax** models exhibit the censorship typical of many Chinese LLMs.** Commenters speculate that MiniMax M3 may be less censored because it is hosted in **Singapore** and may use a _Mistral-style_ setup: an uncensored base model plus an external safety/content filter. Others argue censorship is often geopolitical alignment rather than a binary feature, contrasting this output with refusals or pro-CCP boilerplate from models like **Qwen** and **StepFun**.

    * Several commenters framed Minimax M3’s behavior as likely using a **Mistral-style moderation architecture** : an uncensored base/chat model paired with an external safety or content filter, rather than heavy refusal behavior baked into the model weights. One commenter argued that direct model censorship is resource-intensive and brittle because adversarial or carefully phrased prompts can often bypass safety tuning.
    * A technically relevant benchmark caveat was raised: any evaluation of **China-related political bias or censorship** should be run in both **English and Chinese**. Commenters noted that response differences may reflect training-data distribution rather than only explicit censorship, and that even Western models can show pronounced language-dependent behavior on politically sensitive topics.
    * Users compared behavior across models, claiming **Qwen** refused to answer certain Tiananmen-related prompts while **StepFun** produced a strongly pro-PRC denial-style response. The thread suggested testing Minimax M3 with the same prompts in Chinese to determine whether its apparent lack of censorship is consistent across languages or only visible in English.
  * **[Voice dictation should be free, open source, local first](https://www.reddit.com/r/LocalLLM/comments/1ttuv0p/voice_dictation_should_be_free_open_source_local/)** (Activity: 479): ****Freestyle** is launching an early-preview, free/open-source voice dictation app for **macOS, Windows, and Linux** , positioning itself as a privacy-first alternative to paid tools like Wispr Flow by supporting both **cloud ASR** and **local/on-device models** via its GitHub repo: [freestyle-voice/freestyle](https://github.com/freestyle-voice/freestyle). The maintainer’s stated technical target is _“sub-second transcription latency”_ plus strong post-processing to approach premium UX while avoiding server-side capture of all speech/audio.** Commenters noted overlap with existing OSS dictation tools, especially [cjpais/Handy](https://github.com/cjpais/Handy), which also offers post-processing; one argued Freestyle should contribute there instead of duplicating effort. The maintainer countered that existing OSS options have not matched the latency/UX of paid apps, while another commenter preferred Handy’s more invisible menu-bar-only interaction model.

    * A commenter points to **Handy** ([GitHub](https://github.com/cjpais/Handy)) as an existing open-source dictation app with **post-processing capabilities** , suggesting contribution instead of duplicating effort. Another commenter prefers Handy’s UX because it runs as an “invisible” background utility with only a menu bar icon rather than a persistent window.
    * The project author says the motivation for **Freestyle** is to match paid tools like **Wispr Flow** on both performance and UX, specifically targeting **sub-second transcription latency** plus strong post-processing to clean dictated text while keeping transcription privacy-friendly and subscription-free.
    * A developer of **DictaFlow** argues that for “local-ish” fast dictation, the key implementation detail is inserting transcription directly into the **currently active text field** across macOS, Windows, and iOS, avoiding clipboard-based insertion, intermediate audio-file workflows, or app switching.



## Less Technical AI Subreddit Recap

> /r/Singularity, /r/Oobabooga, /r/MachineLearning, /r/OpenAI, /r/ClaudeAI, /r/StableDiffusion, /r/ChatGPT, /r/ChatGPTCoding, /r/aivideo, /r/aivideo

### 1. AI Public Ownership Proposals

  * **[A proposed bill to give the public a 50% ownership stake in the largest AI companies in America.](https://www.reddit.com/r/singularity/comments/1tuf0ka/a_proposed_bill_to_give_the_public_a_50_ownership/)** (Activity: 1729): **Sen.**Bernie Sanders** announced the proposed **American AI Sovereign Wealth Fund Act** in a [YouTube statement](https://www.youtube.com/watch?v=VN4b4UCWMKI), aiming to give the U.S. public a **`50%` ownership stake in the largest AI companies** and route a share of AI-derived economic value into a sovereign wealth fund. The proposal frames frontier AI firms as potential generators of “trillions” in wealth and targets concentration of ownership/control among major U.S.-based AI companies.** Commenters largely framed the proposal as a pragmatic alternative to banning data centers or resisting AI deployment, with some arguing redistribution mechanisms may be necessary if AI causes large-scale labor displacement. One supportive analogy compared AI to oil, citing Norway’s sovereign wealth approach as a model for capturing national returns from a strategic economic resource.

  * **[Bernie Sanders: A.I. Is a Public Resource. You Should Own Half of It.](https://www.reddit.com/r/singularity/comments/1tuo0n5/bernie_sanders_ai_is_a_public_resource_you_should/)** (Activity: 887): **The linked**NYT opinion piece by Bernie Sanders** could not be technically summarized because the source returned **`403 Forbidden`** and no article text was available. Based on the title, the post frames **AI as a public resource** and proposes that the public should have partial ownership— _“You Should Own Half of It”_ —but no implementation details, policy mechanisms, or technical claims were accessible.** Comments were brief and largely supportive, calling it _“a sane take”_ while raising a resource-infrastructure objection: if AI is public, commenters asked why public ownership does not already apply to **water and power** , especially amid rising utility costs and data-center demand.

    * One commenter argues that Sanders’ stated premise—AI systems were trained on _humanity’s_ accumulated knowledge—does not align with a **U.S.-only sovereign/public ownership mechanism**. They frame the mismatch as: moral claim = global contributors to training data and knowledge; legal vehicle = U.S. taxation or equity claims on U.S. AI firms; beneficiaries = American citizens rather than global creators, researchers, programmers, journalists, and educators.
    * A detailed critique focuses on implementation mechanics: a forced `50%` public equity stake would only produce public benefit if AI company valuations rise, dividends or proceeds are actually distributed, and governance is handled fairly. The commenter emphasizes that the clearest immediate effect would be **control rights** —voting shares, board seats, and federal influence over frontier AI labs—rather than guaranteed compensation for training-data contributors.
    * Another commenter supports public ownership in principle as a way to fund universal services or income if AI-driven productivity meaningfully restructures labor markets, but warns that an adversarial approach could suppress innovation. They argue the policy would need to function as a **public-private partnership with AI labs** , not simply as punitive extraction from CEOs or shareholders.



### 2. Claude and Gemini Reliability Issues

  * **[Rate limit reset](https://www.reddit.com/r/ClaudeCode/comments/1ttzjoq/rate_limit_reset/)** (Activity: 1291): **The image is a screenshot of a verified**ClaudeDevs** X post announcing a reset of **5-hour and weekly rate limits** for all **Claude Pro and Max** users after fixing a bug where some **Claude Code** sessions spawned excessive parallel subagents, rapidly consuming quota: [image](https://i.redd.it/hpmsm3l4jp4h1.jpeg). Technically, the issue appears tied to runaway agent/tool-call orchestration, with commenters reporting _“endless tool call loops”_ burning Max-plan session limits and one user joking that the “excessive parallel subagents” were all **Opus 4.8** instances.** Commenters were split between users who hit limits and viewed the reset as generous, and users who did not hit limits but criticized Anthropic for doing resets or operational changes without clearer announcements.

    * A user shared a screenshot indicating the reset may be tied to **“excessive parallel subagents”** , noting that the workload involved multiple **Opus 4.8** instances. This suggests the rate-limit event may have been triggered by high-concurrency agent execution rather than normal single-threaded prompting.
    * One commenter reported that **tool-call loops** during the weekend consumed their entire session limit on the **Max plan** twice and pushed them above `70%` of their weekly quota, despite that being unusual for their normal usage. This points to runaway agent/tool invocation behavior as a practical failure mode that can rapidly exhaust quota.
    * Another user said they were at `96%` of their weekly limit, with reset not due until Thursday, and were considering upgrading to the **20x** tier before the account suddenly returned to `0%`. The reset appears to have effectively cleared accumulated weekly usage, potentially mitigating quota exhaustion for users affected by abnormal agent behavior.
  * **[WTF HAPPENING TO GEMINI?!!!](https://www.reddit.com/r/GeminiAI/comments/1tthchq/wtf_happening_to_gemini/)** (Activity: 1203): **The image ([JPEG](https://i.redd.it/2y3sg7glll4h1.jpeg)) shows **Gemini Pro** apparently exposing a Chinese-labeled _“思维过程”_ (“thinking process”) with intermediate calorie/TDEE calculations instead of returning only a normal final answer. In context of the title “WTF HAPPENING TO GEMINI?!!!” and selftext, the post is reporting a likely **Gemini UI/model-output bug** or system-prompt leakage-like behavior, where the model produced code or chain-of-thought-style reasoning unexpectedly after a refresh.** Commenters speculate jokingly that Gemini is “using deepseek api,” while another reports broader instability: irrelevant answers and mixed Thai/Chinese outputs, suggesting users perceive this as a recurring Google/Gemini reliability issue rather than a one-off glitch.

    * Multiple users report **Gemini producing unrelated answers and unexpected multilingual output** , including responses mixing Thai and Chinese despite unrelated prompts. One commenter says this occurred repeatedly “yesterday” and criticized the lack of visible incident/status communication or acknowledgement from Google.
    * A commenter speculates the issue could stem from a **token decoding / synchronization failure** , where the model’s internal numeric token stream is mapped back into incorrect Unicode/text output, causing random characters or code-like artifacts. This is presented as conjecture rather than confirmed implementation detail.
    * A comparison is made to **Perplexity** , where a user reports occasional unexplained insertion of isolated Chinese or Russian words and notes that the underlying model is not clearly disclosed, making debugging or attribution difficult.
  * **[Gemini Pro feels much worse than when it first released](https://www.reddit.com/r/GeminiAI/comments/1tuipm1/gemini_pro_feels_much_worse_than_when_it_first/)** (Activity: 1018): **The[image](https://i.redd.it/c0v2d9wbet4h1.png) is a **non-technical Doge meme** illustrating the poster’s claim that **Gemini Pro** has degraded since launch: “Gemini at first release” is shown as strong at coding, memory, logic, context, speed, and image generation, while “Gemini these days” is portrayed as weak, forgetful, and prone to _“ask again later.”_ The post frames this as a paid-tier quality regression versus **ChatGPT Plus** and **Claude** , but provides no benchmarks, model-version comparisons, prompt logs, or reproducible tests—only subjective experience around coding, context handling, and image generation.** Comments are split: some users agree that Gemini’s image generation and even simple writing tasks feel worse and say they switched back to ChatGPT, while others argue this is “rose tinted glasses” and that earlier Gemini versions were actually weaker, with one commenter claiming Gemini only became genuinely good around **Gemini 2.5**.

    * Several commenters report perceived regression in **Gemini Pro** quality, specifically citing weaker _image generation_ and poor performance on simple text tasks like email formatting; one user says they switched back to **ChatGPT** because its image generation produces “creative agency adjacent outputs” from the first prompt.
    * A technical complaint focuses on **short-context conversational memory** : one user reports Gemini sometimes forgets information from only `5-6` messages earlier in the same chat, suggesting unreliable context retention or instruction tracking within an active session.
    * One commenter argues the comparison may be affected by model-version history, claiming the first “really good” Gemini release was **Gemini 2.5** in mid-2025 and that earlier Gemini versions were substantially weaker, while another frames nostalgia as “rose tinted glasses” because older AI systems generally underperform current ones.



# AI Discords

Unfortunately, Discord shut down our access today. We will not bring it back in this form but we will be shipping the new AINews soon. Thanks for reading to here, it was a good run.

---

## [not much happened today](https://news.smol.ai/issues/26-06-03-not-much/)
*🌐 Smol AI News | 2026-06-02*

**a quiet day.**

> AI News for 6/2/2026-6/3/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

# AI Twitter Recap

**Microsoft’s MAI-Thinking-1 Tech Report, Training Stack, and Frontier-Tuning Push**

  * **MAI-Thinking-1 is the day’s densest technical release** : Microsoft introduced [**MAI-Thinking-1**](https://x.com/asadovsky/status/2062008312603070891), a generalist/reasoning model trained **without third-party distillation** , reporting **97% on AIME 2025** , **53% on SWE-Bench Pro** , and human preference wins over Sonnet 4.6 in blind side-by-sides. The 109-page report was widely praised for unusual transparency by [@eliebakouch](https://x.com/eliebakouch/status/2061965825037254947), [@nrehiew_](https://x.com/nrehiew_/status/2062013300196700395), and [@mustafasuleyman](https://x.com/mustafasuleyman/status/2062253941207761180). The main technical theme: Microsoft appears to have “hillclimbed from scratch,” with [@MinjiYoon90](https://x.com/MinjiYoon90/status/2062058684730245376) explicitly framing the effort that way.
  * **Why researchers cared about the report** : The most-cited detail was not just benchmark quality, but the amount of systems/training information released. [@eliebakouch](https://x.com/eliebakouch/status/2061965825037254947) highlighted **zero synthetic data and zero prior-model distillation** , meaning reasoning, tool use, and agentic behaviors were learned in post-training without a synthetic “cold start.” The thread also called out publication of the **scaling ladder recipe** , exact **MFU numbers** , and target-loss construction. In follow-ups, [@eliebakouch](https://x.com/eliebakouch/status/2061976608265880004) noted the private NLL mixture was weighted **50% code, 17.5% STEM, 17.5% math, 10% general knowledge, 5% multilingual** , with normalization against an internal model; he also pointed out ablations around **100–200 TPP** for their MoE setup [here](https://x.com/eliebakouch/status/2061975730414633043). Other notable implementation details surfaced in the community recap: Microsoft used **SGLang** in parts of the stack, per [@eliebakouch](https://x.com/eliebakouch/status/2062002698363232401), and **dspy.GEPA** for pretraining data curation, per [@lateinteraction](https://x.com/lateinteraction/status/2062015109132873852) and [@harold_matmul](https://x.com/harold_matmul/status/2062040746027315714).
  * **Microsoft’s productization angle goes beyond one model** : Alongside the report, Microsoft pushed a broader “own your model” story. [@mustafasuleyman](https://x.com/mustafasuleyman/status/2062275417378041957) outlined **Frontier Tuning** , centered on reinforcement-learning environments for workflow-specific adaptation, claiming internal Excel-oriented MAI-tuned models can reach GPT-5.4-level quality on relevant tasks while being **up to 10× more efficient**. The Build rollout also included [**MAI-Image-2.5**](https://x.com/MicrosoftAI/status/2062240400299934143), which Microsoft says is **#3 on text-to-image** and **#2 on image-to-image** arena leaderboards, plus [MAI-Code-1-Flash](https://x.com/pierceboggan/status/2062220583786709163) and deployment into products like OneDrive Photos. As a meta-point, this is one of the clearest examples this year of a lab trying to publish a frontier-style report while simultaneously turning that stack into enterprise customization infrastructure.



**Open Model Releases: Gemma 4 12B, Ideogram 4.0, Miso One, and Local-First Momentum**

  * **Gemma 4 12B was the standout open-model launch** : Google released [**Gemma 4 12B**](https://x.com/Google/status/2062203526588088452), an **Apache 2.0** multimodal model designed to run on-device with roughly **16GB VRAM**. The architectural novelty is its **encoder-free** design: no separate vision or audio tower. As [Google explained](https://x.com/Google/status/2062203532351090824), images are handled via a lightweight embedding module and raw audio is projected directly into the text-token space. Community reaction focused on the elegance of collapsing modality encoders into the LLM backbone, with [@googlegemma](https://x.com/googlegemma/status/2062202706882883696), [@googleaidevs](https://x.com/googleaidevs/status/2062204432658386950), [@mtschannen](https://x.com/mtschannen/status/2062236357351579915), and [@armandjoulin](https://x.com/armandjoulin/status/2062206784647967075) all emphasizing the same point. Tooling support landed immediately across [vLLM](https://x.com/vllm_project/status/2062228047324201166), [Ollama](https://x.com/ollama/status/2062250522598572345), llama.cpp/MLX via [@osanseviero](https://x.com/osanseviero/status/2062205176597889220), and [Unsloth GGUFs](https://x.com/UnslothAI/status/2062207258810053084) that reportedly enable local runs with as little as **8GB RAM** in quantized form.
  * **Ideogram’s flip to open weights mattered as much as the model itself** : [Ideogram 4.0](https://x.com/ideogram_ai/status/2062202208700313872) was announced as “the best open image model in the world,” with open weights and immediate deployment via [fal](https://x.com/fal/status/2062202673361780873) and Hugging Face [here](https://x.com/huggingface/status/2062206083914158287). Arena quickly placed [Ideogram-4.0-Quality at #8 overall and #1 among open models](https://x.com/arena/status/2062203346996605116), with especially strong gains in **text rendering** and **branding/commercial design**. That open release got outsized attention because Ideogram had previously been regarded as highly design-centric but closed; the switch was noted by [@multimodalart](https://x.com/multimodalart/status/2062210597148930139) and [@cloneofsimo](https://x.com/cloneofsimo/status/2062210832440918309).
  * **Open audio also had a strong day** : [**Miso One**](https://x.com/kimmonismus/status/2062210845308780639) launched as an **8B open-weights TTS model** with **one-shot voice cloning** and claimed **110ms latency** , aimed at more expressive voiceover. Alibaba’s [Fun-Realtime-TTS](https://x.com/ArtificialAnlys/status/2062016529848222073) also took **#1 on Artificial Analysis’s Speech Arena** at **1219 Elo** , ahead of Gemini 3.1 Flash TTS and Inworld, at **$27.59 / 1M chars**. Separately, [Google’s Magenta RealTime 2](https://x.com/HuggingPapers/status/2062260306039259236) was highlighted as an open-weight, low-latency continuous music generator for on-device use.
  * **The bigger pattern is local AI becoming a mainstream deployment target** : [@ggerganov](https://x.com/ggerganov/status/2062193382605111386) called out Computex as a strong signal for **local AI workloads** ; [@rasbt](https://x.com/rasbt/status/2062235700636873082) similarly pointed to a growing open-weight, consumer-hardware ecosystem. Microsoft’s [Surface Laptop Ultra](https://x.com/kimmonismus/status/2062201523963084864) pitch—up to **1 PFLOP AI compute** , **128GB unified memory** , RTX GPU—fits the same trend from the hardware side.



**Agents, Harnesses, and the Shift from Frameworks to Execution Layers**

  * **The center of gravity is moving from “frameworks” to agent harnesses and execution environments** : Several posts converged on the same idea. [@gakonst](https://x.com/gakonst/status/2062116487708512355) argued that the future IDE stack is less about code editors and more about replacing files with threads and bundling plan/design/build/deploy/monitor loops—leaving **collaboration/sync engines** as a key unsolved problem. In a complementary interview summary, [@ConorBronsdon](https://x.com/ConorBronsdon/status/2062224321381323218) reported Jerry Liu’s view that the “framework era” is ending, with abstractions moving upward into **skills, tools, and context quality** rather than Python wrappers.
  * **Multi-agent and agent-optimization work is getting more concrete** : CMU/LTI’s [**MACU**](https://x.com/rsalakhu/status/2062194674794668066) and [@kohjingyu’s thread](https://x.com/kohjingyu/status/2062179533009178897) argue that computer-use agents should be designed as **multi-agent DAG-based systems** , with a manager decomposing tasks and dispatching parallel subagents. Reported gains were **4.7–25.5%** across benchmarks and **1.5× faster** completion on Odysseys. On the optimization side, Microsoft’s **SkillOpt** got practical validation from [@omarsar0](https://x.com/omarsar0/status/2062204469538881988), who says plugging it into an orchestrator improved one multimodal extraction skill from **0.73 to 0.93**.
  * **Agent UX and deployment tooling are becoming products in their own right** : Nous’s Hermes Agent updates drew strong engagement, including remote-connection fixes [here](https://x.com/Teknium/status/2061984430370267210), an updated remote guide [here](https://x.com/Teknium/status/2062170975949721612), and a larger dashboard overhaul [here](https://x.com/Teknium/status/2062315666439655499). Perplexity launched [**Personal Computer for Windows**](https://x.com/perplexity_ai/status/2062189045728596080), an on-device orchestrator for apps/files, while [Cloudflare Browser Run remote tabs](https://x.com/BraydenWilmoth/status/2062180110208311558) showed a more agent-native browser control path. LangChain/LangSmith pushed on the observability and cost-control layer with [Gateway spend tracking](https://x.com/LangChain/status/2062188019784835559), [Sandbox/Gateway/Observability docs](https://x.com/hwchase17/status/2062144718427857256), and case studies around Deep Agents and LangSmith [here](https://x.com/LangChain/status/2062204592562073972).



**Routing, Cost Controls, and Open-vs-Frontier Deployment Strategy**

  * **Model routing is now a real debate, not a slogan** : [@levie](https://x.com/levie/status/2061974298760495132) argued that as token budgets become a meaningful opex category, **model routing is inevitable** , with domain-specific evals as the differentiator. But [@scottastevenson](https://x.com/scottastevenson/status/2062042036774314107) pushed back hard, calling most routing products “snake oil” so far: frontier models can be better/faster/cheaper in aggregate if they avoid retries; routing can destabilize tightly coupled systems; and API vendors can often internalize obvious arbitrage. [@fabianstelzer](https://x.com/fabianstelzer/status/2062051511484465351) added that cache writes and harness-model-prompt fit can erase expected savings.
  * **Enterprise users are starting to enforce hard cost ceilings** : [@simonw](https://x.com/simonw/status/2062143151184465964) highlighted reports that Uber caps coding-agent spend at **$1,500/month per employee per tool**. LangChain immediately framed this as a use case for [LangSmith Gateway](https://x.com/hwchase17/status/2062208385890570565). The broader sentiment was captured by [@Yuchenj_UW](https://x.com/Yuchenj_UW/status/2062225912662561106): some orgs may soon face a three-way choice between letting everyone “tokenmaxx,” capping budgets, or reducing headcount and reallocating spend to the most productive AI-enabled workers.
  * **Real data points are starting to emerge for hybrid/open strategies** : Harvey’s benchmark results were the cleanest example. In one study, [Harvey](https://x.com/harvey/status/2062218656420167785) found a hybrid legal agent with **GLM 5.1** as the main worker and **Opus 4.7** as an advisor beat pure Opus on all-pass rate (**18% vs 14%**) while costing **$368 vs $954** across 100 tasks. Harvey also reported that SFT could move **Kimi 2.6** from **11% to 15%** , beating Opus at roughly **11× lower cost**. On the other side, [@ClementDelangue](https://x.com/ClementDelangue/status/2062248714945630632) argued routing plus post-trained open models will often win on cost/speed/control, while [@ypatil125](https://x.com/ypatil125/status/2062196581936529721) framed open models and open-model clouds as leading indicators of the eventual default for important workloads.



**Top tweets (by engagement)**

  * **Gemma 4 12B launch** : [@googlegemma](https://x.com/googlegemma/status/2062202706882883696) and [@Google](https://x.com/Google/status/2062203526588088452) drove the biggest technical engagement with the encoder-free multimodal release.
  * **Ideogram 4.0 open weights** : [@ideogram_ai](https://x.com/ideogram_ai/status/2062202208700313872) announced a notable shift from a strong closed image model to open weights.
  * **MAI-Thinking-1 transparency** : [@eliebakouch’s thread](https://x.com/eliebakouch/status/2061965825037254947) was the most influential technical reading guide to the MAI report.
  * **Rosalind for life sciences** : OpenAI’s [GPT-Rosalind update](https://x.com/OpenAI/status/2062281977122996256) signaled further verticalization of frontier models into domain-specific scientific research.
  * **Open audio/TTS momentum** : [Alibaba’s Fun-Realtime-TTS](https://x.com/ArtificialAnlys/status/2062016529848222073) and [Miso One](https://x.com/kimmonismus/status/2062210845308780639) stood out as practical releases rather than just research demos.



* * *

# AI Reddit Recap

## /r/LocalLlama + /r/localLLM Recap

### 1. Gemma 4 Multimodal Open Models

  * **[google/gemma-4-12B · Hugging Face](https://www.reddit.com/r/LocalLLaMA/comments/1tvtn6m/googlegemma412b_hugging_face/)** (Activity: 1293): ****Google DeepMind** released [`google/gemma-4-12B`](https://huggingface.co/google/gemma-4-12B), an **Apache-2.0 open-weight multimodal** Gemma 4 model using a `12B` encoder-free/unified decoder-only architecture that projects raw image patches and audio waveforms into the LLM embedding space. The Gemma 4 family is described as spanning dense and MoE variants (`E2B`, `E4B`, `12B`, `26B A4B`, `31B`), with up to `256K` context, hybrid local/global attention with p-RoPE/unified KV, native `system` role, function calling, configurable reasoning/thinking, and text/image/audio/video-frame input with text output; GGUF builds are available from [`ggml-org`](https://huggingface.co/ggml-org/gemma-4-12b-it-GGUF) and [`unsloth`](https://huggingface.co/unsloth/gemma-4-12b-it-GGUF). A linked technical guide highlights the model’s _“encoder-free architecture”_ and implementation path via `transformers` using `AutoProcessor` and `AutoModelForMultimodalLM` ([guide](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-gemma-4-12b), [Google developer post](https://developers.googleblog.com/gemma-4-12b-the-developer-guide/)).** Commenters were mainly interested in practical benchmarking, especially whether Gemma 4 12B can outperform **Qwen 3.5 9B** on coding tasks, and called out the encoder-free multimodal design as technically interesting.

    * A technical guide to **Gemma 4 12B** was shared by **Maarten Grootendorst** , highlighting that the model uses an **encoder-free architecture** , which is notable for readers interested in multimodal/model-architecture design: https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-gemma-4-12b
    * Several commenters framed **Gemma 4 12B** as a potentially useful size/performance midpoint between smaller Gemma variants such as **E4B** and larger models like **26B** , with interest in how it compares against **Qwen 3.5 9B** specifically for coding workloads.
    * One technical point raised was the model’s apparent **audio capability** , with speculation that this could make **Gemma 4 12B** useful for speech/audio translation workflows rather than only text or vision-language tasks.
  * **[The smallest and highest quality Gemma4 E2B and E4B! Open-source! 7x Compression!](https://www.reddit.com/r/LocalLLM/comments/1tuyj0o/the_smallest_and_highest_quality_gemma4_e2b_and/)** (Activity: 353): ****TheStageAI** released MLX-compatible compressed **Gemma 4 Edge** checkpoints via [`edge-lm`](https://github.com/TheStageAI/edge-lm): `gemma-4-E2B-it` at **`1.44 GB`** and `gemma-4-E4B-it` at **`2.72 GB`** , claiming up to **`6.4–7×`** size reduction versus BF16 while preserving benchmark quality. The linked [blog post](https://app.thestage.ai/blog/7x-size-reduction-for-Gemma4-Edge-models?id=14) attributes the compression to **AQLM-style vector quantization for PLE tables** , **per-layer mixed-bit quantization via Riemannian Constrained Optimization** , and **Quantization Error Propagation** ; reported Apple Silicon performance includes E2B at roughly **`115 tok/s`** with **`2.1 GB`** peak MLX memory on an M3 Max.** Commenters focused on the implications for local inference, especially the possibility that larger Gemma variants such as **31B** could fit in **16 GB** systems if similar compression works. One thread framed the release as evidence that rapidly improving local models could undermine cloud-centric AI assumptions.

    * A detailed technical explanation attributes the `~7x` compression to three methods: vector quantization of Gemma’s large per-layer embedding/PLE tables, reducing them from `4.7 GB` to `0.26 GB`; mixed-precision allocation via Riemannian Constrained Optimization, assigning lower bit-widths to less sensitive layers; and Quantization Error Propagation to compensate for accumulated quantization error across layers. The claimed result is a `1.44 GB` model that preserves instruction-following and coding quality while fitting mobile/Apple Silicon memory budgets.
    * Several commenters focused on runtime portability: the release appears tied to **MLX** , which generally targets Apple Silicon, raising questions about whether it can run in **LM Studio** , be converted to **GGUF** for llama.cpp-compatible runtimes, or used outside macOS/Apple hardware. Another technical question asked whether the model can run in its original **LiteRT** format, implying uncertainty about whether the compression artifacts are framework-specific or exportable to broader inference stacks.
  * **[Google introduces Gemma 4 12B: a unified, encoder-free multimodal model](https://www.reddit.com/r/LocalLLM/comments/1tvx2h7/google_introduces_gemma_4_12b_a_unified/)** (Activity: 314): ****Google introduced [Gemma 4 12B](https://blog.google/innovation-and-ai/technology/developers-tools/introducing-gemma-4-12B/)**, an Apache 2.0 mid-sized multimodal model intended for local inference on ~`16GB` consumer systems, claiming performance close to its larger `26B` MoE model at less than half the memory footprint. The main architectural point is **encoder-free multimodality** : vision is reduced to a lightweight embedding module—single matrix multiply + positional embeddings/norms—while audio removes the encoder entirely and projects raw waveform data into the same space as text tokens; Google also mentions **Multi-Token Prediction drafters** and broad support across Hugging Face, Ollama, LM Studio, llama.cpp, MLX, vLLM, SGLang, Unsloth, LiteRT-LM, and Google Cloud.** Commenters are mainly waiting for independent evaluations, especially local multimodal quality and latency/memory behavior. One comparison thread asks how Gemma 4 12B stacks up against larger Qwen models such as Qwen3.6 `27B`/`35B`, but no benchmark-backed answer is provided in the visible top comments.

    * The announcement claims **Gemma 4 12B** approaches the performance of the larger **26B MoE** while using less than half the memory, targeting local execution on consumer machines with `16GB RAM`. The key architectural detail is an **encoder-free multimodal design** : vision uses only a lightweight embedding path—single matrix multiplication, positional embeddings, and normalization—while audio removes the encoder entirely by projecting raw audio into the text-token embedding space.
    * Several commenters are focused on how Gemma 4 12B will compare against current strong local models such as **Qwen3.6 35B** and **Qwen3.6 27B** , especially given the claim that it is near a 26B MoE despite being a dense/smaller `12B` model. The implied evaluation targets are standard text benchmarks plus practical multimodal/audio capability, not just parameter count.
    * One local-inference user estimated that **Gemma 4 12B at Q4** would occupy roughly `7GB` VRAM, leaving substantial room for context on a **Radeon 9060 XT 16GB** setup. Another noted interest in testing on **ROCm** , but expected some delay after release for compatibility/tooling stability.



### 2. Local LLM Deployment Experiments

  * **[Replaced Claude with local Qwen3.6-27B in my multi-agent orchestrator for 2 weeks](https://www.reddit.com/r/LocalLLaMA/comments/1tunmam/replaced_claude_with_local_qwen3627b_in_my/)** (Activity: 584): **The author reports running[**OpenYabby**](https://github.com/OpenYabby/OpenYabby) locally for two weeks with **Qwen3.6-27B** via **Ollama** on a single **RTX 3090 24GB** , using `Q6_K` weights (~`22GB` VRAM), ~`32k` effective context, structured-JSON planning, plan approval, and auto-review across `47` multi-step coding workflows. Qwen was judged competitive with Claude for high-level planning (`~95%` schema-valid after prompt tuning) and memory extraction, but much weaker for execution/tooling: `~12%` tool-call schema/signature errors vs Claude’s `~0.5%`, practical context drift beyond ~`12–14k` tokens, and `3/47` cascade hallucinations after sub-agent failures. The takeaway was that local Qwen can serve as a **reasoning/planning layer** but should not be trusted as an ungated execution layer; strict structured-output enforcement, plan approval, and explicit replan-on-failure logic are required.** Top commenters argued the observed failures may be largely configuration-induced: `Q6_K` plus limited/quantized KV cache and Ollama were criticized, with recommendations for **Q8_0/Q8_K_XL weights** , **F16/BF16 KV cache** , newer **llama.cpp/Unsloth** builds, and much larger contexts (`100k–160k`). One commenter claimed that with those settings Qwen3.6-27B can maintain tool use at long context, though still degrades when asked to analyze very large single code contexts such as thousands of lines at once.

    * Several commenters argued the reported failures likely stem from the runtime/quantization setup rather than Qwen3.6-27B itself: `Q6_K` weights with only `32k` effective context was called insufficient for multi-agent orchestration, with one user recommending at least `128k` context and an unquantized KV cache for complex long-context tool workflows.
    * Users with longer-context Qwen3.6-27B experience recommended moving away from Ollama toward current `llama.cpp`/Unsloth builds and using higher-precision settings: **Q8_0 minimum** , preferably **Q8_K_XL** , with `F16` or `BF16` KV cache. One commenter reported stable tool use up to roughly `160K` context, while noting quality degrades when asking the model to deeply analyze very large single inputs above about `60–70K` tokens.
    * A separate implementation concern was the possibility of a **broken Jinja chat template** distributed by Qwen/Unsloth, which could affect prompting/tool behavior unless replaced with a fixed template. Another commenter noted recent `llama.cpp` changes may allow around `100k` context with `Q6` weights by using `Q5_1`/`Q4_1` KV-cache quantization.
  * **[I Put a Datacenter GPU in My Gaming PC for £200](https://www.reddit.com/r/LocalLLaMA/comments/1tuxy5f/i_put_a_datacenter_gpu_in_my_gaming_pc_for_200/)** (Activity: 547): **The post details integrating a used**Tesla V100 SXM2 16GB** into a consumer gaming PC using an unofficial **SXM2-to-PCIe adapter** , pairing it with an **RTX 4080 16GB** for **~£200** to reach **32GB aggregate VRAM** for local LLM inference ([blog](https://blog.tymscar.com/posts/v100localllm/)). The setup required nontrivial hardware/software work—custom cooling and PWM fan control, NixOS kernel/legacy NVIDIA driver constraints, CUDA 12.2-era compatibility, and `llama.cpp` tensor splitting across Ada + Volta GPUs. With **Qwen3.6-27B-MTP Q5_K_M** fully offloaded across both GPUs, it reportedly reaches about `32 tok/s` generation and `133–160 tok/s` prompt processing.** Commenters focused on the value of retired datacenter GPUs for local inference and questioned consumer VRAM segmentation, especially that an **RTX 4080 ships with only 16GB VRAM**. The general sentiment was that cheap secondhand HBM2 hardware could become increasingly attractive as newer datacenter cards age out.

    * A technical comparison point was raised around **datacenter GPU form factors** , specifically the difference between **SXM2 modules** with no native PCIe edge connector and versions sold on **PCIe carrier cards**. The practical implication is that SXM2 cards generally require a compatible baseboard/interposer, custom cooling, and power delivery, while PCIe variants are closer to drop-in desktop use despite still needing driver, firmware, and cooling consideration.
    * One commenter highlighted the continuing constraint of consumer GPU VRAM, noting that an **RTX 4080 with only`16GB` VRAM** feels limiting compared with decommissioned datacenter cards that can offer much larger memory pools at low used-market prices. This reflects the main technical tradeoff in these builds: older datacenter GPUs may provide high VRAM capacity per pound, but often lack gaming-oriented features, display outputs, standard cooling, or full driver support.
    * There was interest in the future second-hand market for current-generation datacenter accelerators once they are retired. The technical expectation is that cards with large HBM/VRAM capacities could become attractive for local AI, rendering, or compute workloads, assuming buyers can solve platform compatibility, power, cooling, and driver issues.



## Less Technical AI Subreddit Recap

> /r/Singularity, /r/Oobabooga, /r/MachineLearning, /r/OpenAI, /r/ClaudeAI, /r/StableDiffusion, /r/ChatGPT, /r/ChatGPTCoding, /r/aivideo, /r/aivideo

### 1. Ideogram 4.0 and DR02 Launches

  * **[Ideogram 4.0 Just Open Sourced!](https://www.reddit.com/r/StableDiffusion/comments/1tvtu2u/ideogram_40_just_open_sourced/)** (Activity: 834): **The[image](https://i.redd.it/9ajk9fuu935h1.jpeg) is a **promotional, non-technical showcase render** for the claimed release of **Ideogram 4.0** , emphasizing its text-rendering ability with readable labels like “Ideogram,” “Now on Comfy,” and “The Yellow Pearl.” The post frames Ideogram 4.0 as a `9.3B` open-weight text-to-image model with **ComfyUI support** , `fp8`/`nf4` checkpoints, JSON-structured prompting, Qwen3-VL-8B-Instruct text encoding, and strong OCR/layout benchmarks.** Comments focus less on the promo image and more on **model censorship/safety filtering** , with users reporting hard NSFW blocking and joking that Ideogram has “safetymaxxed” the model. Some expect the community may eventually remove or bypass those restrictions.

    * Several commenters report that the open-sourced **Ideogram 4.0** release appears to have very aggressive built-in safety filtering, with **comfyanonymous** noting that blocked outputs are due to the model being _“safetymaxxed”_ rather than a **ComfyUI** issue. Users specifically mention hard NSFW censorship and speculate that the model may need an “abliteration”/uncensoring pass to be useful for less-restricted local workflows.
    * One technically interesting feature highlighted is **bounding-box JSON prompting** , where prompts can apparently specify layout regions explicitly for image composition. A commenter shared an example screenshot and called it a _“Really cool bounding box JSON prompt example,”_ suggesting Ideogram 4.0 may expose structured spatial control beyond plain text prompting.
    * A practical adoption concern raised is that the release is reportedly **watermarked** , **censored** , and lacks a **commercial license** , which limits its usefulness for production or monetized pipelines. For technical users evaluating local deployment, these constraints may matter as much as raw generation quality or ComfyUI compatibility.
  * **[DeepRobotics unveils DR02, with significant improvements in load‑carrying ability and mobility across complex terrain](https://www.reddit.com/r/singularity/comments/1tv2l9z/deeprobotics_unveils_dr02_with_significant/)** (Activity: 816): ****DeepRobotics** reportedly unveiled the **DR02** quadruped robot, emphasizing improved payload/load-carrying capability and mobility over complex terrain; however, the linked Reddit-hosted video was inaccessible due to a `403 Forbidden`, so no independent specs, benchmarks, or gait/control details could be verified from the source. The technical discussion centered less on the announcement and more on locomotion behavior: commenters questioned whether current quadrupeds perform explicit foothold planning versus relying on robust reactive balance and recovery while traversing uneven rocks or unstable surfaces.** A notable critique was that many “uneven terrain” demos appear to show robots _“blundering their way over rocks”_ rather than deliberately selecting footholds based on geometry, slope, or stability. Another commenter suggested testing on transparent floors, which would probe perception assumptions and robustness when visual/depth sensing may fail or become ambiguous.

    * A commenter questioned whether DR02-like quadrupeds are using explicit **foothold planning** on uneven terrain or mainly relying on reactive stabilization. They noted that demos often look like the robot is _“blundering their way over rocks”_ while recovering from unstable or angled contacts, rather than visibly selecting footholds based on terrain geometry, slope, or stability.
    * Another technically relevant concern was how these robots would handle perceptually difficult surfaces such as **transparent floors** like glass walkways. Such environments can be challenging for vision/depth-based terrain estimation and would be a useful edge-case test for locomotion perception and foot-placement robustness.



### 2. Claude Code Agentic Builds

  * **[I wired Claude Code into a database of every Polymarket wallet and trades via MCP. What do you want me to ask it next? This is what I found so far:](https://www.reddit.com/r/ClaudeAI/comments/1tvefqd/i_wired_claude_code_into_a_database_of_every/)** (Activity: 1465): **The author claims to have connected**Claude Code** via **Postgres MCP** to a live Polymarket ledger dataset of ~`1.3B` trades and `2.7M` wallets, letting the model generate and execute read-only SQL from natural-language prompts. Reported findings include ~`20%` net-profitable wallets, `2.4%` clearing `$1,000` profit, and the top `0.1%` capturing `71.5%` of ~$`1B` total profit; the linked CrowdIntel writeup describes a similar MCP setup with pre-aggregated tables, ~`1.56M` wallets, `37,628` wallets above `$1,000` profit, ~`23.6k` bots, and ~`3.1k` whales ([CrowdIntel](https://crowdintel.xyz/blog/claude-mcp-polymarket-ledger)).** Top commenters pushed for journalistic investigation, suggesting the dataset could reveal insider trading or other malfeasance; one Forbes writer asked to connect. A technical suggestion was to compare observed profit distributions against a fair-market/null model and inspect large losing wallets/bets as possible laundering rather than merely uninformed losses.

    * A commenter suggested establishing a statistical baseline for what Polymarket outcomes _should_ look like under a fair/no-insider-betting market, then comparing that expected distribution against observed wallet-level PnL and win-rate distributions. They also proposed examining whether large losing wallets or large losing bets cluster in ways consistent with potential laundering rather than simple insider extraction from retail participants.
    * Another technical question focused on data freshness: what is the lag between bets being placed on Polymarket and those trades appearing in the collected database accessible via MCP. This matters for whether the system can support near-real-time anomaly detection or only retrospective analysis.
    * A commenter asked whether the analysis only covers wallets that directly participate in Polymarket trades, or whether it also traces upstream funding sources and downstream fund flows. That distinction is important for identifying coordinated wallet clusters, exchange on/off-ramps, or post-trade movement patterns that could indicate shared control or laundering behavior.
  * **[I had Opus 4.8 build Temu League of Legends in under a day - I call it LMAO](https://www.reddit.com/r/ClaudeAI/comments/1tucsfe/i_had_opus_48_build_temu_league_of_legends_in/)** (Activity: 3458): **The author reports using**Claude Opus 4.8** to generate a web-only, room-based multiplayer “Temu League of Legends” clone called **LMAO** , starting from a single prompt and then iterating via subagents for character/ability/SFX/VFX design, map/mob/minion passes, and **Ultracode Workflows** for performance, balance, and miscellaneous optimization. They also used `/goal` heavily to batch `10–15` gameplay tweaks/bug fixes at a time, and published the playable prototype at [lmaomoba.com](https://lmaomoba.com); the linked Reddit-hosted video was unavailable due to Reddit `403 Forbidden`.** The poster argues **Opus 4.8 is a “one shot machine”** and claims “5.5 ain’t doin this,” while commenters mostly reacted with praise and asked about the pipeline for art assets, animations, backgrounds, and models. One follow-up noted they ran a “don’t infringe on IP” pass over Claude-generated champion names, replacing close League references such as a Teemo-like “Teehee.”

    * A commenter questioned whether the project was truly a _“1 shot”_ build, saying that their own experience with **Claude Opus 4.8** was that it _“spins on every avenue for minutes longer than 4.7”_ even on small concrete work tasks. They reported switching back to **Codex** by the end of the day, suggesting Opus 4.8 may be better suited to broad product/prototyping exploration than tight, task-oriented engineering workflows.
    * The creator mentioned running a post-generation _“don’t infringe on IP pass”_ to rename generated champions and reduce League of Legends IP similarity. This implies the workflow included an explicit AI-assisted sanitization/rewrite step after initial content generation, with examples like replacing Teemo-like naming with _“Teehee.”_
    * One commenter asked what tooling was used for non-code game assets—art, animations, backgrounds, and models—highlighting a key implementation gap for reproducing the project: whether Opus generated only code/gameplay logic or also coordinated asset creation through external tools.
  * **[I Live by SFO and built a projection mapping of the planes flying over my house using ADS-B radio with claude code](https://www.reddit.com/r/ClaudeCode/comments/1tva44g/i_live_by_sfo_and_built_a_projection_mapping_of/)** (Activity: 3124): **OP built a local**ADS-B-based aircraft visualization** near **SFO** , using received aircraft transponder data to drive a **projection-mapped display** of planes flying over their house; the linked Reddit video (`v.redd.it/gl2b0xivvy4h1`) was not accessible due to a **403 Forbidden** block. The implementation is described as having been built with **Claude Code** , but no hardware stack, SDR/antenna details, decoding pipeline, latency, or projection-calibration method were provided in the accessible post text.** Comments were mostly positive but non-technical, calling it “vibe coding” and “cool”; the only technical follow-up asked how much equipment was required for the project.

    * Several commenters requested implementation details that would make the ADS-B projection mapping project reproducible, specifically the required hardware/equipment, likely bill of materials, and whether the code could be open sourced. One technically relevant extension suggested was combining the aircraft projection with _constellation data_ for an augmented sky/flight visualization setup.



### 3. AI Public Ownership Policy Push

  * **[A proposed bill to give the public a 50% ownership stake in the largest AI companies in America.](https://www.reddit.com/r/singularity/comments/1tuf0ka/a_proposed_bill_to_give_the_public_a_50_ownership/)** (Activity: 1995): ****Bernie Sanders** announced the proposed [**American AI Sovereign Wealth Fund Act**](https://www.youtube.com/watch?v=VN4b4UCWMKI), which would give the public a **`50%` ownership stake in the largest U.S. AI companies**. The proposal frames frontier AI firms as potential generators of _“trillions”_ in concentrated economic value and would route part of that upside into a sovereign-wealth-fund-like public vehicle rather than leaving gains solely with private owners and investors.** Top commenters were broadly supportive, comparing AI rents to oil wealth and invoking Norway’s sovereign wealth fund as a model. One commenter preferred an ongoing wealth-share or **UBI-style distribution** over a one-time `50%` ownership/tax mechanism, while another saw the proposal as a more realistic pivot away from trying to ban or restrict data centers.

  * **[Bernie Sanders: A.I. Is a Public Resource. You Should Own Half of It.](https://www.reddit.com/r/singularity/comments/1tuo0n5/bernie_sanders_ai_is_a_public_resource_you_should/)** (Activity: 1103): **The linked**NYTimes** opinion piece, _“Bernie Sanders: A.I. Is a Public Resource. You Should Own Half of It.”_ , could not be technically assessed because the fetch returned **`403 Forbidden`** from [nytimes.com](https://www.nytimes.com/2026/06/01/opinion/artificial-intelligence-bernie-sanders.html). Based on the title, the post concerns a policy proposal framing AI as a public resource with some form of public ownership or value-sharing, but no implementation details, economic mechanism, or AI infrastructure specifics are available from the provided content.** Top comments are broadly supportive of the premise, with one commenter questioning why similar public-ownership logic is not applied to utilities like water and power, especially given data-center-driven infrastructure demand and rising bills.

    * One substantive critique focuses on the mismatch between Sanders’ stated premise and proposed mechanism: if frontier AI systems were trained on “humanity’s collective knowledge” across books, code, research, media, images, and ideas, then a **US-only sovereign/public ownership model** compensates only Americans rather than global contributors such as non-US artists, researchers, programmers, and journalists. The commenter frames this as an unresolved allocation problem: global training inputs, US legal enforcement, and domestic beneficiaries do not align.
    * Another technical-policy concern is that a forced **50% public equity stake** would not automatically translate into public wealth unless the shares retain value, generate dividends, and are distributed or managed effectively. The commenter argues the clearest practical effect would be **control rights** —voting shares, board representation, and federal influence over frontier AI companies—while also warning that such a mandate could depress sector valuations or distort capital formation.
    * A separate infrastructure-oriented objection asks who bears the cost of AI development, compute, power, cooling, and data-center buildout if the public is granted ownership after the fact. One commenter links the proposal to broader resource externalities, noting that electricity and water bills can rise regardless of whether consumers directly benefit from AI infrastructure expansion.



# AI Discords

Unfortunately, Discord shut down our access today. We will not bring it back in this form but we will be shipping the new AINews soon. Thanks for reading to here, it was a good run.

---

## [not much happened today](https://news.smol.ai/issues/26-06-01-not-much/)
*🌐 Smol AI News | 2026-06-01*

**a quiet day.**

> AI News for 5/30/2026-6/1/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

# AI Twitter Recap

**NVIDIA’s Cosmos 3, Nemotron 3 Ultra, and the Push for Open Physical AI**

  * **NVIDIA’s open-source week** : NVIDIA dominated the open-model conversation with **Cosmos 3** , an open family of **omnimodal world models for physical AI** , plus the announcement of **Nemotron 3 Ultra** , a **550B** open-weight model that several posters called the strongest U.S. open model so far. Cosmos 3 was framed as a full-stack release—**weights, code, datasets, and fine-tuning recipes** —with NVIDIA also launching the **Cosmos Coalition** alongside partners including **Runway** to build an open ecosystem for world models [@NVIDIAAI ecosystem context](https://x.com/NVIDIAAI/status/2061498958283968735), [@runwayml coalition announcement](https://x.com/runwayml/status/2061315089869721682), [@kimmonismus Cosmos thread](https://x.com/kimmonismus/status/2061432501223162241), [@ClementDelangue on NVIDIA’s HF footprint](https://x.com/ClementDelangue/status/2061487081315094906).
  * **Why Cosmos 3 mattered technically** : Beyond robotics rhetoric, the more concrete details were that Cosmos 3 unifies **language, image, video, audio, and action** in a single **Mixture-of-Transformers** design pairing an **autoregressive reasoner** with a **diffusion generator**. [Artificial Analysis](https://x.com/ArtificialAnlys/status/2061494719998546206) said Cosmos 3 reached **#1 among open-weight models** on both their **Text-to-Image** and **Image-to-Video** leaderboards, noting the generator uses **structured JSON prompts** and can be driven either by an external prompt-upsampling harness or its own reasoner branch. Separately, NVIDIA’s hardware + software push extended to adoption of the **OpenMDW** framework and partner ecosystem integrations on platforms like fal [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2061494719998546206), [@fal](https://x.com/fal/status/2061604121786876307).
  * **Nemotron 3 Ultra reception** : Community reaction to **Nemotron 3 Ultra** was unusually strong for a fresh open release. Posters highlighted both capability and serving characteristics, including claims that it is already topping some open evals and may be serving at **300+ tok/s** in some setups—far faster than large DeepSeek/Kimi-class models [@scaling01](https://x.com/scaling01/status/2061379856433107135), [@ctnzr](https://x.com/ctnzr/status/2061483152741175757), [@caspar_br](https://x.com/caspar_br/status/2061505720907182280). There was also some technical discussion that Nemotron appears **less sparse** than peers like Kimi K2 / DeepSeek V4—roughly **~10% active** vs **~3%** —which could affect both economics and behavior [@eliebakouch](https://x.com/eliebakouch/status/2061607195268038777).



**MiniMax M3, Qwen3.7-Plus, and JetBrains Mellum2 Expand the Open Agent Model Field**

  * **MiniMax M3’s launch was the day’s biggest model release** : M3 was presented as an open-weight multimodal agent/coding model with **1M context** , **native multimodality** , and competitive agent benchmarks. The headline figures repeated across launch partners were **59.0% SWE-Bench Pro** , **66.0% Terminal Bench 2.1** , and **74.2% MCP Atlas** [@MiniMax_AI](https://x.com/MiniMax_AI/status/2061425142795034794), [@PBDTokenRouter](https://x.com/PBDTokenRouter/status/2061463048485838935), [@kimmonismus](https://x.com/kimmonismus/status/2061473350766170420). Multiple infra vendors shipped day-0 support—**Novita** , **Vercel AI Gateway** , **Cloudflare AI Gateway** , **OpenClaude** , **Flowith** , and others—suggesting unusually fast ecosystem adoption [@MiniMax_AI on Novita](https://x.com/MiniMax_AI/status/2061398427121201648), [@rauchg](https://x.com/rauchg/status/2061593874498531707), [@gitlawb](https://x.com/gitlawb/status/2061581678871806083).
  * **Benchmarks vs practical experience were mixed** : M3 earned praise for frontend generation, visual/game tasks, and price-performance, with side-by-side demos showing strong one-shot UI/game outputs and notable benchmark placement for Next.js agent evals [@notjazii](https://x.com/notjazii/status/2061407087293313210), [@lostinlatencyX](https://x.com/lostinlatencyX/status/2061409696649548165), [@rauchg](https://x.com/rauchg/status/2061593874498531707). But several evaluators also reported **high token consumption** , **verbose self-check loops** , and occasional **requirement drift** on long tasks, making M3 look more like a “quality first, efficiency later” model [@ZhihuFrontier review](https://x.com/ZhihuFrontier/status/2061493401019957337), [@teortaxesTex skepticism](https://x.com/teortaxesTex/status/2061432151183171702).
  * **Qwen3.7-Plus** : Alibaba launched **Qwen3.7-Plus** as a **multimodal interactive hybrid agent** that unifies **GUI and CLI operation** , visual reasoning, coding, and search-augmented QA. It is **API-available** via Alibaba Cloud Model Studio and was quickly added to tools like **Cline** [@Alibaba_Qwen launch](https://x.com/Alibaba_Qwen/status/2061506641120641494), [@cline](https://x.com/cline/status/2061580233778790439). The launch reinforces the trend that open-ish Asian labs are no longer releasing “just chat models,” but full **agent-capable multimodal systems**.
  * **JetBrains Mellum2** : JetBrains released **Mellum2** , a **12B MoE** model with **2.5B active parameters** , trained on roughly **11T tokens** and post-trained with **RLVR** , shipping **base / SFT / RL checkpoints** and a technical report [@nv_pavlichenko](https://x.com/nv_pavlichenko/status/2061438808290172935), [@jetbrains](https://x.com/jetbrains/status/2061444430884675791). The intended niche is especially interesting: **ultra-low-latency inference** for **routing, RAG, sub-agents, and IDE use** , and it landed in **vLLM** immediately [@vllm_project](https://x.com/vllm_project/status/2061621691995005301#m). This looks like a serious “small fast open model for developer workflows” play rather than a benchmark-chasing frontier release.



**Agents, Sandboxes, Memory, and Search Are Becoming the Real Product Surface**

  * **The stack is shifting from model calls to agent runtimes** : Several launches converged on the idea that the main engineering leverage is now in the **harness** rather than the model. **Perplexity’s “Search as Code”** is the clearest example: instead of iterative search tool calls, the model writes **Python** against a search SDK, enabling custom ranking pipelines, map-reduce over indexes, batching, aggregation, and lower token overhead. Perplexity reports a jump on its internal **WANDR** benchmark from **0.152** to **0.386** with this architecture [@perplexity_ai](https://x.com/perplexity_ai/status/2061506359326384319), [@AravSrinivas](https://x.com/AravSrinivas/status/2061575845056278971).
  * **Managed agents + sandboxes are becoming standard** : Google detailed **Managed Agents in the Gemini API** , where a single API call can spin up an agent that reasons, writes/runs code, manages files, and operates inside a hosted **Linux sandbox** [@_philschmid](https://x.com/_philschmid/status/2061457703210197273), [@GoogleAIStudio](https://x.com/GoogleAIStudio/status/2061452967530701090). LangChain pushed similar ideas around **Deep Agents** , **Context Hub** , and **LangSmith Sandboxes/Engine** , emphasizing persistent context, agent lifecycle tooling, and automated failure triage [@LangChain](https://x.com/LangChain/status/2061432934993674267), [@hwchase17](https://x.com/hwchase17/status/2061496556608504043).
  * **Memory remains a missing primitive** : One recurring complaint was that enormous context windows still don’t solve **cross-session memory**. A thread on **HydraDB** argued that “RAG + manual context injection” has been misnamed as memory, while actual persistent session knowledge remains underserved [@kimmonismus](https://x.com/kimmonismus/status/2061454202883432501). Related research threads pointed to reusable context management policies like **AdaCoM** , which trains a separate LLM via RL to prune/preserve context for frozen agents [@dair_ai](https://x.com/dair_ai/status/2061455253325971789).
  * **Security remains the gating issue for enterprise agents** : There was a notable warning from Microsoft Security Intelligence about a major **npm supply chain compromise** affecting **90+ redhat-cloud-services packages** , including a self-propagating worm stealing npm/GitHub/AWS/SSH credentials [@MsftSecIntel](https://x.com/MsftSecIntel/status/2061485730958848188). At the same time, enterprise agent vendors highlighted **sandboxing** , **runtime isolation** , and **security stack integration** as prerequisites for deployment, including discussion of **NVIDIA OpenShell** and LangChain’s sandbox keynote [@shannholmberg](https://x.com/shannholmberg/status/2061368566256189656), [@LangChain](https://x.com/LangChain/status/2061448130806116827).



**Codex, Claude Code, and the Competitive Coding-Agent Race**

  * **OpenAI extended Codex into more places** : OpenAI announced that **frontier models and Codex are now generally available on AWS / Amazon Bedrock** , aimed squarely at enterprises that want OpenAI capabilities inside existing AWS security/compliance workflows [@OpenAI](https://x.com/OpenAI/status/2061564502160892138), [@OpenAIDevs](https://x.com/OpenAIDevs/status/2061564710173224985). OpenAI also shipped a **Codex Python SDK** supporting threads, turns, streaming, resume, images, and sandbox control [@reach_vb](https://x.com/reach_vb/status/2061569472792572163), plus support for Bedrock-backed Codex workflows [@reach_vb on Bedrock config](https://x.com/reach_vb/status/2061572961451094191).
  * **Claude Code had a real ops incident** : Anthropic reset **5-hour and weekly rate limits** for Pro and Max users after fixing a bug where some **Opus 4.8** sessions spawned too many **parallel subagents/tool calls** , burning usage unexpectedly [@ClaudeDevs](https://x.com/ClaudeDevs/status/2061501787769893055), [follow-up](https://x.com/ClaudeDevs/status/2061501790131265803). That’s a notable reminder that coding-agent product quality is increasingly determined by orchestration behavior, not just raw model IQ.
  * **Behavioral differences across coding models remain material** : Developers highlighted large qualitative differences between GPT, Claude, and other models on benchmarks like **ProgramBench** and **WeirdML** , with Opus sometimes preferring exploration over score-maximization or showing benchmark-specific quirks [@OfirPress](https://x.com/OfirPress/status/2061458258821251081), [@htihle](https://x.com/htihle/status/2061412097720774679). A separate long thread argued newer **Claude Opus 4.6–4.8** variants can fabricate plausible but fictional concepts in non-coding domains, suggesting possible truthfulness/alignment regressions rather than ordinary hallucinations [@distributionat](https://x.com/distributionat/status/2061362406971060244).



**Infra, Hardware, and Local AI Systems**

  * **NVIDIA is coming for the PC** : The most-discussed hardware launch was **RTX Spark** , an NVIDIA/Microsoft “personal AI computer” built around **Grace + Blackwell** , with up to **128GB unified memory** and claimed **1 PFLOP FP4**. The key strategic read: NVIDIA is no longer just selling accelerators, but an end-to-end local AI system that competes with **Apple Silicon** , x86 PCs, and Qualcomm simultaneously [@kimmonismus](https://x.com/kimmonismus/status/2061484174088007739), [@swyx](https://x.com/swyx/status/2061567877879369953).
  * **Cluster/networking updates** : On the datacenter side, **Lambda** said it is first to adopt **NVIDIA Quantum-X InfiniBand Photonics Q3450-LD** switches, pushing co-packaged optics to reduce network power and failures in large AI clusters [@LambdaAPI](https://x.com/LambdaAPI/status/2061319330433032658). **OpenAI** also announced **Stargate Michigan** , a planned **1GW** data center using closed-loop cooling and paired with workforce/education commitments [@OpenAINewsroom](https://x.com/OpenAINewsroom/status/2061533639138316314).
  * **Local open-model tooling is improving fast** : The **MLX-VLM v0.6.0** release was one of the more substantive local inference/tooling updates, adding speculative decoding, Anthropic-style and responses-style APIs, tool calls, support for many new multimodal models, and image/audio features with the explicit pitch of turning Apple devices into “real local agent machines” [@Prince_Canuma](https://x.com/Prince_Canuma/status/2061541992790683726). That pairs well with growing DGX Spark + **vLLM** experimentation for local NVFP4 MoE serving [@vllm_project](https://x.com/vllm_project/status/2061530659160838549).



**Top Tweets (by engagement, filtered for technical relevance)**

  * **Anthropic’s IPO path** : Anthropic said it has **confidentially submitted a draft S-1** to the SEC, opening the door to an IPO pending review [@AnthropicAI](https://x.com/AnthropicAI/status/2061478052257841495).
  * **Claude Code usage incident** : Anthropic reset user rate limits after an **Opus 4.8 parallel subagent/tool-call bug** caused excessive quota burn [@ClaudeDevs](https://x.com/ClaudeDevs/status/2061501787769893055).
  * **Qwen3.7-Plus** : Alibaba launched a **multimodal agent model** spanning GUI/CLI operation, coding, and visual tasks [@Alibaba_Qwen](https://x.com/Alibaba_Qwen/status/2061506641120641494).
  * **OpenAI on Bedrock** : OpenAI models and **Codex** are now available through **Amazon Bedrock** for enterprise workflows [@OpenAI](https://x.com/OpenAI/status/2061564502160892138).
  * **ARC-AGI-3 movement** : **Claude Opus 4.8** posted a new SOTA on **ARC-AGI-3** at **1.5%** , still tiny in absolute terms but a meaningful jump on that benchmark [@arcprize](https://x.com/arcprize/status/2061512025638121516).



* * *

# AI Reddit Recap

## /r/LocalLlama + /r/localLLM Recap

### 1. New Frontier Model Releases and Early Tests

  * **[MiniMax M3 - Coding& Agentic Frontier, 1M Context, Multimodal](https://www.reddit.com/r/LocalLLaMA/comments/1ttdiq0/minimax_m3_coding_agentic_frontier_1m_context/)** (Activity: 1090): ****MiniMax M3** is announced as an _open-weight_ frontier model with coding/agentic focus, native multimodality/vision, and **MiniMax Sparse Attention** for up to **`1M` tokens** of context with a guaranteed **`512K` minimum** ([MiniMax M3](https://www.minimax.io/models/text/m3)). Claimed long-horizon agentic results include 12-hour ICLR paper reproduction, Hopper FP8 GEMM CUDA/Triton optimization reaching **`9.4×` speedup** after `147` iterations, and **PostTrainBench** ranking third behind Opus 4.7 and GPT-5.5; access is currently via API/MiniMax Code, with HuggingFace/GitHub weights/local deployment planned.** Commenters are cautiously interested in the combination of cheap/efficient vision plus long-context agentic coding, but skeptical because the announcement calls it _“open-weight”_ while not yet exposing weights or even parameter count. One technical debate is whether the results imply a much larger-than-`~250B` model, extreme benchmark optimization, or a genuine open-weight breakthrough.

    * Commenters focused on the missing release details: despite the claim of being _“the first open-weight model with three frontier capabilities”_ , users could not find actual weights, parameter count, or sizing information for **MiniMax M3**. One commenter linked a preview image from the announcement ([Reddit image](https://preview.redd.it/fej3vn94qk4h1.jpeg?width=3808&format=pjpg&auto=webp&s=83ef24ab093520eb3118dd918259adff4f42a569)), but the thread still lacked confirmation of model scale or downloadable artifacts.
    * A technically substantive concern was that the advertised capability level implies one of three possibilities: **a much larger-than-expected model** , unusually strong benchmark optimization, or a major open-weights breakthrough. The speculation centered on whether MiniMax M3 is actually around `~250B` parameters or significantly larger, and whether its coding/agentic/multimodal claims will hold once weights and independent benchmarks are available.
  * **[NVIDIA announces Nemotron 3 Ultra](https://www.reddit.com/r/LocalLLaMA/comments/1tthkh5/nvidia_announces_nemotron_3_ultra/)** (Activity: 621): **The[image](https://i.redd.it/f79wu6dnml4h1.jpeg) is a technical announcement slide for **NVIDIA Nemotron 3 Ultra** , described in comments as a **MoE`550B-A55`** model. The slide positions Nemotron 3 Ultra against open/open-weight competitors including **GLM 5.1, Kimi K2.6, and Qwen3.5** across “Frontier Smart” benchmark categories such as agent productivity, coding, instruction following, knowledge work, and long-context capability.** Commenters viewed the comparison against other open-source/open-weight models positively, while one noted an “artificial analysis score” of `48`, placing it just below frontier-tier models and around the MiniMax 2.7 range, with the expectation that it could be the strongest U.S. open-weight model.

    * NVIDIA Nemotron 3 Ultra is identified as a **MoE`550B-A55`** model, implying roughly `550B` total parameters with about `55B` active parameters per token. This architecture detail is the most concrete technical spec mentioned in the thread.
    * A commenter cites an **Artificial Analysis score of`48`**, placing Nemotron 3 Ultra “one notch less than frontier” and roughly in the **MiniMax 2.7** range, while suggesting it may be the strongest **US open-weight** model by that metric.
    * Technical references shared include NVIDIA’s official Nemotron 3 Ultra Base usage cookbook on GitHub: [NVIDIA-NeMo/Nemotron](https://github.com/NVIDIA-NeMo/Nemotron/tree/main/usage-cookbook/Nemotron-3-Ultra-Base), plus the LifeArchitect model comparison table: [lifearchitect.ai/models-table](https://lifearchitect.ai/models-table/). One commenter argues the comparison against **Qwen3.5** is notable because Nemotron may be NVIDIA’s best open-weight model while still trailing several non-US/open models.
  * **[Stepfun 3.7 Flash is very good](https://www.reddit.com/r/LocalLLaMA/comments/1tss9nq/stepfun_37_flash_is_very_good/)** (Activity: 473): **The[GIF](https://i.redd.it/k37ol07vfg4h1.gif) is a **technical visual demo** , not a meme: it shows the output of **Stepfun 3.7 Flash** for the prompt `create a beautiful, relaxing flight simulator in a single html page`, rendering a low-poly 3D flight scene with HUD-style speed/altitude indicators. The OP says this was the official `Q4_X_S` quant and claims the model feels near **GLM 5.1** in aesthetics and about `80%` of its 3D world understanding, while using only roughly `25%` of GLM 5.1’s parameters and including built-in vision.** Commenters mostly reacted with comparisons and nostalgia rather than deep benchmarks: one referenced the old Excel flight simulator, while another compared interest in **Qwen 3.7 Max / 27B** and asked whether it beats **Qwen3.6 27B**.

    * A commenter draws a model-comparison angle by referencing **Qwen 3.7 Max** and hoping for a future **Qwen 3.7 27B** release, while another asks whether Stepfun 3.7 Flash is better than **Qwen3.6-27B**. The thread includes screenshot evidence for the Qwen3.6-27B reference ([image](https://preview.redd.it/h1jbx5tz4j4h1.png?width=1523&format=png&auto=webp&s=c4bd572a0741fcffc65f2b75153efbb603ede82b)), but no quantitative benchmark scores or reproducible eval details are provided.



### 2. Consumer Local-AI Hardware Oddities

  * **[Dell confirms XPS laptop with NVIDIA N1X at Computex ( basically a DGX Spark GB10 for consumers with Windows )](https://www.reddit.com/r/LocalLLaMA/comments/1tsifgs/dell_confirms_xps_laptop_with_nvidia_n1x_at/)** (Activity: 450): ****Dell confirmed an upcoming XPS laptop using NVIDIA’s N1X platform** at Computex, suggesting OEM traction for NVIDIA’s Arm/client-PC push; the post frames it as a consumer Windows analogue to **DGX Spark/GB10** , but the provided [VideoCardz summary](https://videocardz.com/newz/dell-confirms-xps-laptop-with-nvidia-n1x-at-computex) does **not** include concrete specs, launch timing, pricing, or benchmark data. Commenters focused on whether such a system could offer **large unified memory configurations** —e.g. `256GB`—which would be the main technical differentiator versus conventional dGPU laptops.** Top commenters were skeptical on value if pricing approaches DGX Spark, arguing a cheaper RTX `5090` laptop would likely be faster for many workloads. There was also a preference for **first-class Linux support** over Windows for this class of AI/developer-oriented hardware.

    * Commenters focused on unified-memory capacity as the main technical differentiator versus conventional GPU laptops: `128GB` system memory with potentially `64GB` usable by the GPU was described as much more useful for local LLM workloads than typical laptop VRAM limits, and some wanted `256GB` unified-memory configurations.
    * There was skepticism about price/performance if the XPS N1X is priced similarly to **NVIDIA DGX Spark** : one commenter argued a **GeForce RTX 5090 laptop** would be cheaper and faster for many GPU workloads, despite having less unified memory.
    * Several technical concerns centered on software and architecture support: commenters preferred first-class **Linux** support over Windows for local AI workflows, questioned whether the consumer system would lack **NVFP4** support compared with DGX Spark, and raised the possibility of new **SM119** kernels requiring additional low-level optimization work.
  * **[I trusted random person on this subreddit and bought 3080 20gb made of chinesium](https://www.reddit.com/r/LocalLLaMA/comments/1ttz558/i_trusted_random_person_on_this_subreddit_and/)** (Activity: 645): **The image is a terminal[`nvidia-smi` screenshot](https://i.redd.it/4r6t2yykgp4h1.png) showing an unusual **“NVIDIA GeForce RTX 3080” with`20480 MiB` VRAM** installed alongside an **RTX 3090 with`24576 MiB`**, supporting the post’s claim that the user bought a modified/Chinese-market “3080 20GB.” The technical significance is that the card appears driver-recognized and functional at idle, but the post provides no benchmarks, stability testing, thermals, power data, or confirmation that the full VRAM is reliable under CUDA/ML workloads.** Commenters focus on practical risk: driver compatibility, fan/noise behavior, performance issues, longevity, and whether this is the cheapest CUDA VRAM-per-dollar option. The overall tone is cautious curiosity, with anxiety about trusting a random subreddit recommendation for a nonstandard GPU.

    * Commenters focused on practical validation of the Chinese-modified `RTX 3080 20GB`, asking specifically about **driver compatibility** , acoustic behavior, and whether there are any performance regressions or speed issues versus standard cards.
    * One technical angle raised was value efficiency: whether this card is the **cheapest CUDA-capable VRAM per GB** option, given its unusual `20GB` VRAM configuration compared with mainstream RTX 3080/3090 pricing.
    * A commenter noted that a reported `15°C` temperature difference alongside an `RTX 3090` was impressive, suggesting the card’s cooling/thermals may be competitive despite being a nonstandard “chinesium” variant. Another user mentioned ordering the **3-fan version** , implying cooler design may be an important variant-specific factor.



## Less Technical AI Subreddit Recap

> /r/Singularity, /r/Oobabooga, /r/MachineLearning, /r/OpenAI, /r/ClaudeAI, /r/StableDiffusion, /r/ChatGPT, /r/ChatGPTCoding, /r/aivideo, /r/aivideo

### 1. Claude Coding: Opus 4.8, CLAUDE.md, Rate Limits

  * **[Differences Between Opus 4.7 and Opus 4.8 on MineBench](https://www.reddit.com/r/ClaudeAI/comments/1tt3a8h/differences_between_opus_47_and_opus_48_on/)** (Activity: 1821): **MineBench author reports**Claude Opus 4.8** improves over **Opus 4.7** on a Minecraft-like 3D block-placement benchmark ([MineBench](https://minebench.ai/), [repo](https://github.com/Ammaar-Alam/minebench)), with `15` builds costing `$41.52` and averaging `24.8 min` / `1,487 s` inference time. Despite unchanged API pricing, Opus 4.8 was cheaper than 4.7 due to apparently shorter/streamlined CoT “thinking” time, while producing subjectively better builds—claimed near **GPT 5.5** quality but with more inconsistency. The run required `5` retries for invalid block-palette hallucinations or malformed JSON; the author notes this is typical for Claude, but adaptive thinking appears less prone to exhausting output tokens before emitting valid JSON ([release notes](https://github.com/Ammaar-Alam/minebench/releases/tag/3.6.0)).** Comments were mostly non-technical appreciation; one commenter supplied an alternate Opus 4.6 vs 4.7 comparison link, and another joked that “The Knight no longer looks like Bender.”

    * A commenter linked the prior **Opus 4.6 vs 4.7 MineBench comparison** for longitudinal context: [reddit.com/r/singularity/comments/1sofehv/differences_between_opus_46_and_opus_47_on](https://www.reddit.com/r/singularity/comments/1sofehv/differences_between_opus_46_and_opus_47_on/). This provides a reference point for evaluating whether 4.8 changes are incremental relative to the previous 4.6→4.7 step.
    * One technical suggestion was to add a _“budget mode”_ where each model is constrained to use the **same number of blocks**. This would make MineBench comparisons more controlled by normalizing available construction resources rather than only comparing unconstrained outputs.
    * Another commenter proposed a dedicated site to track **model progression over time on the same prompt**. This would turn individual MineBench posts into a reproducible longitudinal benchmark, making it easier to compare visual/spatial construction quality across model versions.
  * **[Karpathy's CLAUDE.md just crossed 220k GitHub stars. Here's why it works.](https://www.reddit.com/r/ClaudeCode/comments/1tte5sb/karpathys_claudemd_just_crossed_220k_github_stars/)** (Activity: 1462): **The post argues that a minimal`CLAUDE.md`/Claude Code project-instructions file—attributed to Forrest Chang’s implementation of **Andrej Karpathy’s** guidance—became popular because it mitigates common agentic-coding failure modes: cold-start lack of project memory, unverified assumptions, unnecessary refactors, and overconfident execution. Its core rules are: ask before assuming, implement the simplest working solution, avoid unrelated code changes, and explicitly flag uncertainty; the author claims this is especially useful in stateful API-heavy projects such as video-generation pipelines involving Magic Hour/Kling-style integrations.** Commenters were split: one argued these rules are useful only early on and become too slow compared with more automated “harness engineering” workflows, while another warned that hardcoded personality overrides may fight evolving Claude Code/model behavior and should be scoped per session or project rather than globally.

    * Several commenters argued that Karpathy-style `CLAUDE.md` rules are useful mainly for onboarding users transitioning from “normal coding” to Claude Code, but become inefficient once users build more advanced _harness engineering_ workflows. The technical concern is that repeated confirmation/checkpoint prompts can slow iteration, and experienced users may prefer automation patterns that let them “fire a query off” without repeatedly approving the same decisions.
    * A substantive critique focused on the brittleness of hardcoded personality or workflow overrides across changing Claude Code releases. One commenter noted that new model versions and harness updates can invert prior assumptions—for example, a prompt written because an older model “didn’t ask enough questions” may become counterproductive if a newer model asks too many—so they recommend limiting such rules to session- or project-level scope rather than global behavior overrides.
    * Another technical point was that many behaviors encouraged by popular `CLAUDE.md` files may already be implemented in Claude Code’s harness/system prompt, which commenters claim was visible in a prior source leak. If true, duplicating those instructions in user-level files may have limited marginal effect and could function more as placebo or as a weak steering layer on top of Anthropic’s existing RLHF and harness design.
  * **[Rate limit reset](https://www.reddit.com/r/ClaudeCode/comments/1ttzjoq/rate_limit_reset/)** (Activity: 918): **The[image](https://i.redd.it/hpmsm3l4jp4h1.jpeg) is a screenshot of a **ClaudeDevs / X.com announcement** that **Claude Pro and Max 5-hour and weekly rate limits were reset** after Anthropic fixed a bug where some **Claude Code sessions spawned excessive parallel subagents** , rapidly consuming user quotas. The context suggests the issue caused runaway tool-call or agent loops, with one commenter reporting **Opus 4.8 subagents** and another saying their Max-plan session limit was burned twice and reached `70%+` of their weekly limit.** Commenters were split between users who saw the unannounced reset as confusing or irresponsible and affected users who viewed it as an appropriate or generous remediation for a weekend of broken Claude Code behavior.

    * Users inferred the reset was tied to **“excessive parallel subagents”** behavior, with one commenter sharing a screenshot and noting the involved agents were **all Opus 4.8** : https://preview.redd.it/gye31dlekp4h1.png?width=348&format=png&auto=webp&s=bd740cb1239c5dbc12a5fedd3957ec197d47c8ee. The technical implication discussed was that parallel agent execution can rapidly amplify usage against rate/session limits, especially when multiple high-end model instances are spawned concurrently.
    * One user reported that **endless tool-call loops** consumed their entire session limit on the **Max plan** twice over a weekend and pushed them to **over`70%` of their weekly limit**, suggesting a failure mode where agent/tool orchestration can burn quota without meaningful progress. Another user said they were at **`96%` of weekly usage** before an unexpected reset, indicating the reset materially affected users close to hard weekly caps.



# AI Discords

Unfortunately, Discord shut down our access today. We will not bring it back in this form but we will be shipping the new AINews soon. Thanks for reading to here, it was a good run.

---

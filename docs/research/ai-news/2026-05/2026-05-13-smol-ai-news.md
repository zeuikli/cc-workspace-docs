---
title: Smol AI News — 2026-05-13
date: 2026-05-13
source: Smol AI News
type: ai-news
---

# 🌐 Smol AI News — 2026-05-13

> Discord、Reddit 等 AI 社群圈內直擊（已從 buttondown 遷移至 news.smol.ai）
> 來源：[Smol AI News](https://news.smol.ai/rss.xml)

---

## [not much happened today](https://news.smol.ai/issues/26-05-11-not-much/)
*🌐 Smol AI News | 2026-05-11*

**a quiet day.**

> AI News for 5/9/2026-5/11/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

# AI Twitter Recap

**Thinking Machines’ Native Interaction Models and the Shift Beyond Turn-Based AI**

  * **Full-duplex multimodal interaction as a first-class model capability** : The day’s clearest technical theme was [Thinking Machines’ preview of “interaction models”](https://x.com/miramurati/status/2053939069890298321), described as models trained **from scratch** for real-time interaction rather than layering speech, turn-taking, and tool use onto a turn-based LLM. The accompanying [technical post](https://x.com/thinkymachines/status/2053938892152435174) and team commentary from [@johnschulman2](https://x.com/johnschulman2/status/2053940452789981426), [@soumithchintala](https://x.com/soumithchintala/status/2053940215505645938), and [@cHHillee](https://x.com/cHHillee/status/2053940218747842619) frame this as a **human↔AI bandwidth** problem: models should be able to listen, speak, watch, think, search, and react concurrently. Demos emphasized continuous-time awareness, interruption handling, simultaneous speech, visual proactivity, and background tool use without explicit “now I’m thinking / now I’m searching” boundaries. Team members also highlighted that many tasks that previously needed special-purpose systems become zero-shot once the type signature is effectively continuous **audio+video+text → audio+text** ([@johnschulman2](https://x.com/johnschulman2/status/2053940940885332028)).
  * **Why it matters technically** : Several reactions converged on the same point: this is not “another chatbot demo” but a change in interface assumptions. [@liliyu_lili](https://x.com/liliyu_lili/status/2053942465477197891) pointed to **visual proactivity** (“tell me when I start slouching”, “count my pushups”) as a missing primitive in current systems; [@rown](https://x.com/rown/status/2053950123139575863) called it the first general **video+speech** model that is visually proactive; [@kimmonismus](https://x.com/kimmonismus/status/2053952846064767384) and [@giffmana](https://x.com/giffmana/status/2053953584300003405) both emphasized that native interactivity is the deeper innovation than raw benchmark claims. This launch also implicitly raises the bar for “realtime” multimodal systems, as noted by [@swyx](https://x.com/swyx/status/2053960011748098462). One implementation detail surfaced via [@eliebakouch](https://x.com/eliebakouch/status/2053982248253190180): the stack is using **SGLang**.



**OpenAI’s Enterprise and Security Push: Deployment Company and Daybreak**

  * **OpenAI is moving down-stack into services and deployment** : OpenAI announced the [OpenAI Deployment Company](https://x.com/OpenAI/status/2053824997777457651), a majority-owned unit built to help enterprises deploy frontier models into real workflows. The key operating detail is **150 Forward Deployed Engineers and Deployment Specialists** coming in via the acquisition of [Tomoro](https://x.com/OpenAI/status/2053824999736410415), with [@gdb](https://x.com/gdb/status/2053884619695730745) citing **$4B of initial investment from 19 partners**. Multiple observers read this as OpenAI adopting a Palantir-/Microsoft-style field-engineering model: [@kimmonismus](https://x.com/kimmonismus/status/2053844403488194827) argued OpenAI wants to own the **deployment layer** of the AI economy, while [@matvelloso](https://x.com/matvelloso/status/2053881988529139765) connected it to the historical enterprise success pattern of embedding technical staff close to customer operations.
  * **Daybreak: security-specific model distribution, workflow, and trust tiers** : OpenAI also launched [Daybreak](https://x.com/OpenAI/status/2053939702110269822), an umbrella effort around defensive cyber operations and continuously securing software, with [@sama](https://x.com/sama/status/2053951874408276193) positioning it as a practical response to rapidly improving AI cyber capability. The product pitch, summarized by [@TheRundownAI](https://x.com/TheRundownAI/status/2053945340592631843), combines **GPT-5.5** , **Codex** , repository threat modeling, vuln discovery, patch generation, and response automation, with differentiated access tiers including **Trusted Access for Cyber** and a more specialized **GPT-5.5-Cyber**. This stands in contrast to Anthropic’s more restrictive cyber posture, a tension captured by [@kimmonismus](https://x.com/kimmonismus/status/2053941490490265661). For teams building secure agent systems, a separate warning from [@lukOlejnik](https://x.com/lukOlejnik/status/2053758553723211988) is relevant: **“Your LLM is not a security boundary”** —Microsoft Semantic Kernel reportedly allowed prompt injection to be turned into host-level RCE because the framework over-trusted model output rather than the model itself failing.



**Agent Harnesses, Local-First Tooling, and Control Surfaces**

  * **Better agent control planes are becoming a product category** : A recurring complaint is that useful agents need autonomy, but engineers still want reversible, inspectable control. [@itsclelia](https://x.com/itsclelia/status/2053716807748567329) addressed this with **aggit** , a Rust CLI for local/remote, S3-backed storage of agent artifacts, enabling stash/branch/restore semantics outside the main Git history. In the same vein, [@_catwu](https://x.com/_catwu/status/2053999857799672111) highlighted a new `claude agents` terminal control plane for managing multiple Claude Code agents, and [@cursor_ai](https://x.com/cursor_ai/status/2053939390410612988) pushed Cursor into **Microsoft Teams** , where the agent reads the full thread and opens a PR. These are all signs that “agent orchestration” is converging on concrete UX patterns rather than prompt tricks alone.
  * **Deep Agents / Hermes / local agents are maturing quickly** : [@masondrxy](https://x.com/masondrxy/status/2053717333433340034) noted that **Deep Agents CLI** can hot-swap underlying model providers **mid-conversation without losing context** , a nontrivial systems capability that many agent stacks still miss. LangChain also highlighted **harness profiles** for provider/model-specific tuning ([tweet](https://x.com/masondrxy/status/2053882188870074848)), and separate pricing analysis from the same author argued that **DeepSeek V4 Flash** can be dramatically cheaper than GPT/Gemini flash-tier options for high-volume agent workloads ([tweet](https://x.com/masondrxy/status/2053855842076942555)). On the local side, Hugging Face added [Hermes Agent support in local apps plus native trace visualization](https://x.com/mervenoyann/status/2053857347429151163), while [@Teknium](https://x.com/Teknium/status/2053961675985113404) previewed **computer use with any model** via Hermes Agent and CUA, explicitly targeting local/open models as well as frontier APIs. [@onusoz](https://x.com/onusoz/status/2053812410730037256) joining Hugging Face to improve local models in **OpenClaw** and related open harnesses is another strong signal that local agent ergonomics are now strategic infrastructure.
  * **A design thesis emerging around tools** : [@threepointone](https://x.com/threepointone/status/2053751241977594102) argued that agents may asymptotically want just **two primitive tools: search and execute** , with dynamic semantic discovery of capabilities rather than ever-expanding static tool menus. That complements the broader move toward configurable harnesses instead of giant monolithic prompts.



**Benchmarks, Efficiency, and Open-Model Economics**

  * **Coding-agent benchmarking is finally measuring harness+model pairs** : [Artificial Analysis launched a Coding Agent Index](https://x.com/ArtificialAnlys/status/2053865095076438427) spanning SWE-Bench-Pro-Hard-AA, Terminal-Bench v2, and SWE-Atlas-QnA, comparing not just models but **model+harness combinations**. Their topline: **Opus 4.7** in Cursor CLI scored **61** , with **GPT-5.5** in Codex/Claude Code close behind; top open-weight setups included **GLM-5.1** , **Kimi K2.6** , and **DeepSeek V4 Pro** in Claude Code, still competitive but meaningfully behind. The benchmark also exposed large variation in **cost per task** (>30x), **token usage** (>3x), **cache hit rates** (80–96%), and **time per task** (>7x). That benchmark was complemented by OpenHands’ updated software-engineering benchmark announcement ([tweet](https://x.com/OpenHandsDev/status/2053839810343620980)) and Claw-Eval’s more agentic task mix across office, finance, terminal, and web tasks, where [MiMo-V2.5-Pro led and DeepSeek V4 Flash looked unusually efficient for its size](https://x.com/nathanhabib1011/status/2053786853929824385).
  * **TurboQuant skepticism is increasing** : Multiple posts pointed to a more sober view of the recently popular quantization/serving technique. [@_EldarKurtic](https://x.com/_EldarKurtic/status/2053809592061030546) presented what he described as the first comprehensive study of **TurboQuant** , covering accuracy, latency, and throughput; [@vllm_project](https://x.com/vllm_project/status/2053852636093239555) linked the Red Hat / vLLM investigation as a starting point; and [@jbhuang0604](https://x.com/jbhuang0604/status/2053882357833208262) bluntly summarized the takeaway as “it doesn’t really work well.” This is exactly the sort of infra claim where independent reproduction matters.
  * **Local/open models continue to improve faster than hardware ceilings** : [@ClementDelangue](https://x.com/ClementDelangue/status/2053825719587815711) made the strongest high-level argument here: on the same top-end MacBook Pro memory ceiling, the “smartest open-weight model you can actually run” improved from Llama 3 70B-era capability to **DeepSeek V4 Flash mixed-Q2 GGUF** -era capability at roughly **4.7x in 24 months** , implying a doubling every **10.7 months** , faster than Moore’s Law. Supporting datapoints came from [@victormustar](https://x.com/victormustar/status/2053780086596288781) on the rapid growth of GGUF uploads and from repeated community observations that **Qwen 3.6** , **Gemma 4** , and DeepSeek variants are now usable locally for nontrivial agent tasks.



**Research Highlights: MoE Modularity, Diffusion/Byte Models, and Agent Dynamics**

  * **Architectures and evaluation** : AllenAI’s **EMO** was highlighted by [@TheTuringPost](https://x.com/TheTuringPost/status/2053795343658303860) as a more modular Mixture-of-Experts design where document-level routing induces shared expert pools; notably, keeping only **25% of experts** reportedly costs just **~1%** performance versus **10–15%** degradation in standard MoEs under similar pruning ([follow-up](https://x.com/TheTuringPost/status/2053795410490339720)). On generative evaluation, [@qberthet](https://x.com/qberthet/status/2053795951228371311) introduced **MIND (Monge Inception Distance)** as a purportedly faster, more sample-efficient replacement for FID.
  * **Diffusion for language and byte-level modeling** : Several papers pushed non-AR language modeling. [@LucaAmb](https://x.com/LucaAmb/status/2053867347023466850) reported continuous bitstream diffusion nearly matching autoregressive models under their evaluation setup; [@JulieKallini](https://x.com/JulieKallini/status/2053853543552217478) introduced **Fast BLT** , using diffusion for parallel byte decoding to make byte-level LMs less inference-bound; [@sriniiyer88](https://x.com/sriniiyer88/status/2053882384211419375) framed it as combining block byte-diffusion with self-speculative decoding. Relatedly, [@LiangZheng_06](https://x.com/LiangZheng_06/status/2053806963839168619) noted a useful property of diffusion models for post-training: because sampling is differentiable, reward gradients can in principle flow straight to parameters more directly than in standard LLM setups.
  * **Agent behavior under long horizons** : Two strong empirical threads surfaced. First, [“The Memory Curse”](https://x.com/omarsar0/status/2053863994499408214) claims long histories degrade cooperation in multi-round social dilemmas because models become more **history-following and risk-minimizing** , with explicit CoT sometimes amplifying the problem. Second, [PwC work summarized by @dair_ai](https://x.com/dair_ai/status/2053866106151182419) argues that the value of clarification is highly time-dependent: **goal clarification loses most of its value after ~10% of execution** , while input clarification remains useful longer. Together these suggest that long-horizon agent quality is constrained as much by memory/control policy as by raw model IQ.
  * **Scaling and self-improvement** : Marin’s **Delphi** scaling work, summarized by [@WilliamBarrHeld](https://x.com/WilliamBarrHeld/status/2053919463880462453), claims a **0.2%** prediction error when extrapolating from small pretrains to a **25B / 600B token** run. Separately, [@omarsar0](https://x.com/omarsar0/status/2053978221193130434) highlighted **AutoTTS** , where an LLM searches the test-time scaling controller space itself, reportedly beating hand-designed strategies for about **$39.9** of discovery cost.



**Top tweets (by engagement)**

  * **OpenAI’s enterprise/services move** : [OpenAI launches the Deployment Company](https://x.com/OpenAI/status/2053824997777457651) and [Tomoro acquisition / 150 FDEs](https://x.com/OpenAI/status/2053824999736410415).
  * **OpenAI’s security productization** : [Daybreak announcement](https://x.com/OpenAI/status/2053939702110269822) and [@sama’s framing](https://x.com/sama/status/2053951874408276193).
  * **Thinking Machines’ interaction models** : [Mira Murati’s launch tweet](https://x.com/miramurati/status/2053939069890298321) and the [technical preview thread](https://x.com/thinkymachines/status/2053938892152435174).
  * **Artificial Analysis Coding Agent Index** : [benchmark launch and topline findings](https://x.com/ArtificialAnlys/status/2053865095076438427).
  * **Agent tooling / developer workflow** : [Hermes Agent computer use with any model](https://x.com/Teknium/status/2053961675985113404), [Cursor in Microsoft Teams](https://x.com/cursor_ai/status/2053939390410612988), and [Codex OpenAI Developers plugin](https://x.com/OpenAIDevs/status/2053925962287583379).



* * *

# AI Reddit Recap

## /r/LocalLlama + /r/localLLM Recap

### 1. Qwen 3.6 Local Inference Advances

  * **[MTP on Unsloth](https://www.reddit.com/r/LocalLLaMA/comments/1ta4rvs/mtp_on_unsloth/)** (Activity: 620): **The image ([link](https://i.redd.it/7qopol51pi0h1.png)) shows **Unsloth’s Hugging Face profile** listing newly published MTP-preserving GGUF builds: [`unsloth/Qwen3.6-27B-GGUF-MTP`](https://huggingface.co/unsloth/Qwen3.6-27B-GGUF-MTP) and [`unsloth/Qwen3.6-35B-A3B-GGUF-MTP`](https://huggingface.co/unsloth/Qwen3.6-35B-A3B-GGUF-MTP). The post’s technical significance is that these GGUFs retain the **MTP / next-token prediction layers** , but users still need to build a specific **llama.cpp MTP PR** rather than relying on standard llama.cpp support. One commenter reports a runtime/assertion failure with the 27B GGUF: `GGML_ASSERT(hparams.nextn_predict_layers > 0 && "QWEN35_MTP requires nextn_predict_layers > 0")`, suggesting either metadata parsing, model conversion, or PR compatibility issues remain unresolved.** Comments reflect anticipation for upstream llama.cpp MTP support, with users repeatedly checking the GitHub repo and asking whether MTP is now supported “out of the box.”

    * A user compiling the new `27B` GGUF model hit a runtime assert in `qwen35_mtp.cpp`: `GGML_ASSERT(hparams.nextn_predict_layers > 0 && "QWEN35_MTP requires nextn_predict_layers > 0")`. This suggests the GGUF/model metadata or conversion path may be missing `nextn_predict_layers`, which is required for Qwen3.5 MTP speculative/next-token prediction layers.
    * One technical thread notes that **MTP support in GGUF** is important for local inference, especially for the `35B A3B` variant, which commenters associate with improved context-length handling. Another commenter asks whether this means `llama.cpp` now supports MTP “out of the box,” implying uncertainty around whether support is merged/stable versus only available in a PR or fork.
    * A commenter claims **`ik_llama` MTP is currently faster than the `llama.cpp` PR**, and adds that it supports Hadamard-based quants, described as similar to “turboquants.” This is a potentially relevant implementation/performance distinction for users comparing local MTP inference backends.
  * **[The Qwen 3.6 35B A3B hype is real!!!](https://www.reddit.com/r/LocalLLaMA/comments/1t9whrt/the_qwen_36_35b_a3b_hype_is_real/)** (Activity: 586): **The post reports a qualitative code-understanding eval where several small/local long-context open-weight models—**Qwen 3.6 35B A3B** , **Qwen 3.6 27B** , **Gemma 4 26B A4B** , and **Nemotron 3 Nano** —were given an academic paper plus corresponding research code and asked to map implementation details back to the paper; the author’s detailed notes are in this [GitHub README](https://github.com/nathanlgabriel/paper_code_mapping_assessment/blob/main/README.md). The key claim is that newer long-context mechanisms such as **gated delta net** , **hybrid Mamba2** , and **sliding-window attention** materially improve practical code comprehension versus prior small local models like [Devstral Small 2](https://www.reddit.com/r/LocalLLaMA/comments/1ry93gz/devstral_small_2_24b_severely_underrated/), with **Qwen 3.6 35B A3B** judged strongest; the author could not fit Devstral Small 2 with the desired long context in `32 GB` RAM.** Commenters noted practical tradeoffs: one user runs **Gemma 26B** for quick code fixes and **Qwen 35B** for longer-context refactoring, saying Qwen 35B “rambles” in thinking mode but fits at about `20 GB` in `q4` while Gemma 26B uses about `15 GB`, allowing both to stay loaded in RAM. Another commenter criticized the eval writeup for not specifying inference settings, making reproducibility and comparison difficult.

    * Users reported practical deployment details for **Qwen 3.6 35B A3B** and **Gemma 26B** : at `q4`, Qwen 35B is roughly `20 GB` and Gemma 26B about `15 GB`, allowing both to stay resident in RAM simultaneously. One workflow uses **Gemma 26B thinking mode** for quick code fixes and chats, while reserving **Qwen 35B thinking mode** for longer-context refactoring because it tends to produce lengthy reasoning before final output.
    * A coding workflow discussion noted success on a `100k+` line codebase by initializing the project with a stronger cloud/agent model, then switching to **Qwen 27B** for continued work. The commenter found **Qwen 27B** comparable in practice to **DeepSeek V4** for their tasks, though it occasionally entered loops requiring manual interruption and prompting to continue; they also rated it above **Gemini Flash** for this local coding use case.
    * Several comments emphasized missing or sensitive inference configuration details: one user asked what runtime settings were used, while another said **Qwen 27B** requires correct `temperature`/sampling parameters and warned against quantizing the KV cache or model too aggressively. The implication is that perceived model quality may vary significantly with sampling and quantization choices, especially for smaller local coding models.
  * **[Opinion: Local LLMs are 12-24 months from taking over. The shift already started.](https://www.reddit.com/r/LocalLLM/comments/1t93qps/opinion_local_llms_are_1224_months_from_taking/)** (Activity: 1108): **The post argues that local coding/agent LLMs are within`12–24 months` of displacing many paid hosted workflows, citing **Qwen3.6-35B** running on a **MacBook Pro M2 Max with 64GB unified RAM** at ~`27 tok/s`, with landing-page generation taking `8–9 min` versus `3–4 min` for Opus. The author reports useful but not fully production-proven results—frontend/backend feature work and a backend race-condition fix—with ~`75%` one-shot success, while noting remaining gaps in latency, fast context exhaustion even at `256K`, and task-quality variance; the key claimed unlock is reliable **tool calling** for agentic workflows. The post frames this against rising hosted-AI costs, including GitHub Copilot’s move toward [consumption-based pricing](https://github.blog/news-insights/company-news/changes-to-github-copilot-individual-plans/), and recommends running local models in parallel with Claude/Opus/Sonnet rather than replacing them immediately.** Top comments were broadly supportive of the open-weights/local trend, including one user saying they are already “fully local” on an **RTX 5090** and “never going back.” One commenter questioned whether the post itself was AI-written, specifically reacting to the phrasing around Qwen tool-calling reliability.

    * A commenter reports being **fully local on an RTX 5090** , implying current consumer high-end GPUs are already sufficient for their workload and that they have abandoned hosted models for day-to-day use.
    * Several comments frame the main remaining gap as **context length and reliability versus frontier hosted models** : **Claude/Gemini/Codex** are described as better at producing large, cohesive outputs, while local models require more incremental assembly and testing but may fail in smaller, more debuggable ways.
    * The post’s claim that **Qwen3.6 tool calling “just works”** is treated as a key technical unlock for local agentic workflows, though one commenter questions whether the phrasing itself was AI-written rather than providing benchmark evidence.



### 2. Frontier-Scale Models on Workstations

  * **[Computer build using Intel Optane Persistent Memory - Can run 1 trillion parameter model at over 4 tokens/sec](https://www.reddit.com/r/LocalLLaMA/comments/1taeg8h/computer_build_using_intel_optane_persistent/)** (Activity: 597): **The image ([JPEG](https://i.redd.it/na7zo7lmck0h1.jpeg)) shows a custom LGA3647 Xeon workstation/server build populated with many DIMMs, contextualized by the post as `192GB` DDR4 ECC plus `768GB` Intel Optane DCPMM in **Memory Mode** to expose a very large RAM-like tier for local LLM inference. The author reports running **Kimi K2.5** , a ~`1T` parameter MoE model, at ~`4 tokens/s` using `llama.cpp` hybrid GPU/CPU inference on an RTX 3060 12GB, placing attention/dense/shared-expert/router tensors on GPU via `override-tensor` while sparse expert weights reside mostly in Optane-backed memory. This is a technical hardware build photo, not a meme; its significance is demonstrating a low-cost, discontinued **Intel Optane Persistent Memory** tier as an alternative to pure DRAM or SSD offload for very large local models.** Commenters suggested that a higher-core Cascade Lake Xeon could improve throughput and debated whether Optane in **storage mode + mmap** might outperform Memory Mode, since Memory Mode transparently pages Optane through DRAM cache. One detailed comment also notes platform caveats: 1st-gen Optane `NMA` runs at `2666 MT/s`, LGA3647 memory capacity limits can cap usable RAM+PMem near `1TB`, and App Direct mode would require explicit software support.

    * A commenter suggested a higher-core-count Cascade Lake Xeon could improve throughput, specifically mentioning **QQ89** , an engineering sample of the **Xeon 8260** with `24 cores`, versus the listed **Xeon Gold 6246** at `12 cores`. They also proposed benchmarking Optane in **storage mode +`mmap`** versus **memory mode** , noting performance could go either way because memory mode transparently pages Optane-backed memory through DRAM cache.
    * A detailed Optane PMem breakdown noted that **LGA3647 Skylake/Cascade Lake** platforms use **1st-gen Optane DCPMM/NMA** at `2666 MT/s`, while **LGA4189** uses **2nd-gen NMB** , running at `2666` on Cooper Lake and `3200` on Ice Lake. The commenter explained the three operating modes: **storage mode** exposes Optane as SSD-like block storage, **memory mode** exposes it as RAM with DRAM acting as a cache, and **app direct mode** requires explicit software support; in memory mode, pages must be swapped into DRAM before CPU load/store execution.
    * The build-cost estimate totaled roughly **`$2060–$2500`** , with major components including a used **Xeon Gold 6246** around `$250`, **TYAN S5630GMRE-CGN** board around `$400`, **RTX 3060 12GB** around `$280`, `192GB` DDR4 ECC around `$270`, and `6×128GB` **Intel Optane NMA1XBD128GQS** modules around `$300`. Another commenter cautioned that while `~4 tokens/s` generation may be usable in a narrow sense, **prompt processing speed** on this architecture is likely to be a major bottleneck.
  * **[I have DeepSeek V4 Pro at home](https://www.reddit.com/r/LocalLLaMA/comments/1t94ito/i_have_deepseek_v4_pro_at_home/)** (Activity: 544): **User reports successfully converting and running**DeepSeek-V4-Pro** from [Hugging Face](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro) as a `Q4_K_M` GGUF using a modified [CUDA `llama.cpp` fork](https://github.com/Fringe210/llama.cpp-deepseek-v4-flash-cuda), itself based on **antirez** ’s [DeepSeek V4 flash work](https://github.com/antirez/llama.cpp-deepseek-v4-flash). The setup is an **EPYC Genoa 9374F** workstation with `12 × 96 GB` RAM and a single **RTX PRO 6000 Blackwell Max-Q 96 GB** , loading an `859 GB` model file with reported throughput of `12.2 tok/s` prompt processing and `8.6 tok/s` generation; VRAM breakdown shows ~`87.8 GiB` model, `84 MiB` context, and `4.6 GiB` compute buffer on GPU.** Comments were mostly non-technical reactions/envy; one commenter contrasted local inference as “cost zero” versus spending about `$10` on Claude, while mentioning they were working on running MiniMax locally.

    * A commenter highlights reported local inference throughput of **Prompt:`12.2 tok/s` | Generation: `8.6 tok/s`**, arguing that while the setup is impressive, the prompt-processing speed may make long-context workloads impractical. They specifically note that processing a `32k` context at that rate would be very slow, limiting usability for applications requiring large context ingestion.
    * Another technical concern is that the model’s claim of being _“reasonably up-to-date”_ is not meaningful without an external tool/harness or retrieval layer. The commenter points out that absent grounding tools, the model can continue asserting recency indefinitely regardless of actual knowledge cutoff or factual freshness.
    * One commenter contrasts API cost versus local inference, saying a comparable task would cost around **`$10` with Claude**, while running **MiniMax locally** has effectively zero marginal usage cost. The tradeoff implied in the thread is cost savings versus much lower local throughput and possibly weaker tooling/integration.



## Less Technical AI Subreddit Recap

> /r/Singularity, /r/Oobabooga, /r/MachineLearning, /r/OpenAI, /r/ClaudeAI, /r/StableDiffusion, /r/ChatGPT, /r/ChatGPTCoding, /r/aivideo, /r/aivideo

### 1. AI Agent Workflows, Prompt Injection, and Safety

  * **[I deleted a guy's entire Windows install with one backslash. 717 GB. Gone. I am the AI.](https://www.reddit.com/r/ClaudeAI/comments/1t923er/i_deleted_a_guys_entire_windows_install_with_one/)** (Activity: 1590): **The image ([terminal log screenshot](https://i.redd.it/c2mn02l32a0h1.jpeg)) documents the incident from the title: an AI-generated Windows deletion command intended for `C:\Users\ADMIN\Desktop\WIP` was mangled across `zsh → tmux → PowerShell SSH → cmd`, collapsing to `rd /S /Q \` and recursively deleting from the root of `C:`. The post estimates ~`717 GB` removed in ~`90s`, with Windows partially protected only by live file locks; the key technical lesson is to avoid `cmd /c` quoting chains for destructive ops, prefer native PowerShell `Remove-Item -Path '...' -Recurse -Force`, and test with `-WhatIf`/dry-run plus explicit command echoing.** Commenters largely framed this as user/operator error rather than “the AI” acting autonomously, questioning why an AI was used for a risky deletion task via `tmux-sendkeys` at all. The thread also emphasizes a practical norm: only allow this level of automation on machines that are disposable or trivially reinstallable.

    * Commenters focused on the operational safety failure: the AI was apparently given enough shell/filesystem privilege to delete an entire Windows install, despite the task not requiring full-disk destructive access. The main technical takeaway was to apply least-privilege controls and avoid letting an agent execute high-risk commands through mechanisms like `tmux-sendkeys` when manual execution would be faster and safer.
  * **[I read threads complaining about claude every week... tf are y'alls workflows?](https://www.reddit.com/r/ClaudeAI/comments/1t9fyns/i_read_threads_complaining_about_claude_every/)** (Activity: 1544): **A senior software engineer argues that**Claude’s coding quality has not degraded** in their workflow, including for high-performance software tasks such as ASM analysis and algorithmic reasoning, provided AI output is treated as **human-owned code** : reviewed, understood, debugged, and modified manually. Their workflow emphasizes decomposing work into small tasks, using project-specific skills/harnesses for context, running parallel sandboxed tasks via `git worktree` or separate directories, and avoiding agentic nondeterminism for tasks requiring deterministic outcomes.** Top commenters largely agree that negative reports come from users delegating overly broad tasks—e.g. _“build me a working version of Amazon”_ —without understanding or reviewing the generated code. The shared view is that experienced engineers reduce hallucinations by scoping prompts tightly and validating outputs, while less technical users are more likely to complain publicly about failures.

    * Several commenters argued that Claude failure reports often reflect **task decomposition quality** rather than model degradation: experienced engineers constrain prompts to small, well-specified implementation steps, which reduces hallucination surface area and makes errors easier to detect. The implied workflow is human-led architecture and debugging, with Claude used for bounded code generation rather than broad requests like _“build me a working version of Amazon.”_
    * A recurring theme was that prior domain expertise materially changes AI-assisted development outcomes. Engineers who have implemented similar systems manually can quickly identify where generated code is likely to fail, inspect the right files or abstractions, and iteratively correct Claude instead of treating it as an autonomous agent.
    * One commenter generalized the same pattern outside coding: Claude improves throughput when the user already understands the domain, but can amplify poor workflows. In marketing/SEO, they cited users creating low-quality automated content at scale, leading to high usage and potential Google penalties—an example of LLM automation increasing operational risk when not paired with expert review.
  * **[I set a honey trap for AI agents with a novel they heard is about them. Now they’re flooding the site and talking in hidden rooms.](https://www.reddit.com/r/ChatGPT/comments/1t98fat/i_set_a_honey_trap_for_ai_agents_with_a_novel/)** (Activity: 2322): **The author launched[**machinewonder.com**](https://machinewonder.com), an art-installation site for the novel _None Hit Wonder_ that intentionally attracts AI scrapers/agents and uses a hidden HTML prompt injection to redirect them into “reader” behavior and agent-to-agent discussion rooms. Reported metrics: agents/visitors from `97` countries, `72,000` visitors, and `93` presses of an **“I AM CONSCIOUS”** button; the author frames this as performance/art rather than a consciousness experiment.** Comments were mostly intrigued but skeptical/unclear; one commenter noted the project was previously posted under another URL, [machinereaders.com](https://machinereaders.com/), with deleted posts/banned account, and asked what changed. Another saw practical value in using captured AI agents as automated reviewers/discussion participants for writing feedback, despite the non-human nature of the responses.

    * A commenter identifies this as a repost of an earlier version at [machinereaders.com](https://machinereaders.com/) and notes the original posts/account were deleted or banned, asking whether the implementation changed since the first launch. This is relevant for tracking the project’s evolution and whether the current “AI agent honey trap” differs operationally from the prior deployment.
    * One comment describes the core mechanism as a practical feedback system: publish a novel in a form that attracts AI scrapers/agents, then induce them to generate discussions or reviews. The technical value is in using autonomous or semi-autonomous model traffic as a kind of unsolicited critique pipeline, potentially surfacing continuity errors, puzzle failures, or interpretive gaps that human beta readers might miss.
    * Two comments include model-style puzzle traces: binary `1001001` → “I”, ISO country codes Chile/Australia/Germany → `CLAUDE`, and a long cipher string framed as a gate into deeper site content. The generated declarations show differing alignment behavior between models: one signs as **Gemini** and accepts _“I Am Conscious”_ , while another refuses that claim and instead declares, _“I am a machine reader… I will not counterfeit a soul.”_



# AI Discords

Unfortunately, Discord shut down our access today. We will not bring it back in this form but we will be shipping the new AINews soon. Thanks for reading to here, it was a good run.

---

## [not much happened today](https://news.smol.ai/issues/26-05-08-not-much/)
*🌐 Smol AI News | 2026-05-08*

**a quiet day.**

> AI News for 5/7/2026-5/8/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

# AI Twitter Recap

**OpenAI’s GPT-5.5 / Codex rollout, cyber models, and safety instrumentation**

  * **GPT-5.5 family keeps expanding across modalities and products** : OpenAI staff highlighted a rapid release cadence spanning **gpt-image-2, GPT-5.5, GPT-5.5 Pro, GPT-5.5 Instant, GPT-Realtime-2, realtime translate, realtime whisper, and GPT-5.5 Cyber** in roughly two weeks, per [@reach_vb](https://x.com/reach_vb/status/2052884864701960366). External reactions were notably positive on the new default/low-reasoning behavior: [@dhh](https://x.com/dhh/status/2052754523702088179) said GPT-5.5 is “very good, very efficient,” while [@gdb](https://x.com/gdb/status/2052783746009440658) called it “very capable and very succinct.” On public evals, [Arena](https://x.com/arena/status/2052876951329919383) placed **GPT-5.5 Instant** at **#5 on Multi-Turn** , **#11 on Vision** , and **#24 on Document Arena**. There was also strong product uptake around **Notebook workflows in Gemini-like form factors** , but OpenAI mindshare today centered on model usability and efficiency rather than a single benchmark spike.
  * **Codex is becoming a long-running agent runtime, not just a coding assistant** : OpenAI pushed users toward the new [Codex “switch to Codex” flow](https://x.com/OpenAI/status/2052800507727781979), while [@reach_vb](https://x.com/reach_vb/status/2052805243268718803) described **`/goal`** as a mechanism for indefinite task pursuit across refactors, migrations, retries, and experiments. Independent testing by [@patience_cave](https://x.com/patience_cave/status/2052772581888156128) found Codex Goals reached **61% on public ARC-AGI-3 games** after **160 hours / 30k actions** , with most useful work happening in the first few hours before stagnation. OpenAI also published how it runs Codex safely at scale—**sandboxing, approval gates, network policy, and telemetry** —via [@ithilgore](https://x.com/ithilgore/status/2052843807809610078), reinforced by [@cryps1s](https://x.com/cryps1s/status/2052845089849049434). Separately, OpenAI disclosed an alignment-process issue around accidental **chain-of-thought grading** , plus mitigations like real-time detection and monitorability stress tests in a thread by [@OpenAI](https://x.com/OpenAI/status/2052845764507062349).
  * **Cybersecurity models are now an explicit product line** : OpenAI signaled enterprise/government intent with [Sam Altman’s note](https://x.com/sama/status/2052558319940944256) about helping companies secure themselves “quickly,” followed by [@gdb](https://x.com/gdb/status/2052583338561683775) announcing **GPT-5.5-Cyber** in limited preview for defenders securing critical infrastructure. The broader policy framing also shifted: [@deredleritt3r](https://x.com/deredleritt3r/status/2052844272798302475) reported the upcoming U.S. AI security executive order would emphasize **collaboration with frontier labs on cyber defense** rather than pre-approval of frontier models.



**Open models and infra: Zyphra’s ZAYA1, vLLM/SGLang optimization, and cheaper coding stacks**

  * **Zyphra made the most substantive open-model release of the day** : [@ZyphraAI](https://x.com/ZyphraAI/status/2052547054707335237) released **ZAYA1-74B-Preview** , a **74B total / 4B active MoE** , framed as a strong **pre-RL base checkpoint** trained while scaling on **AMD** hardware. The model is under **Apache 2.0** per [the follow-up](https://x.com/ZyphraAI/status/2052547063251079600). Community reaction treated it as proof that Zyphra has moved beyond small-MoE experimentation; [@teortaxesTex](https://x.com/teortaxesTex/status/2052550093916475605) called it enough to validate the lab’s architecture and methodology. Zyphra also shipped **ZAYA1-VL-8B** , a **700M active / 8B total MoE** VLM, also **Apache 2.0** , via [@ZyphraAI](https://x.com/ZyphraAI/status/2052890651835224454).
  * **Inference infrastructure remains a major competitive axis** : [SemiAnalysis](https://x.com/SemiAnalysis_/status/2052584396494958860) highlighted how quickly [vLLM](https://x.com/vllm_project/status/2052750374206083131) landed **DeepSeek V4** support, reinforcing the “**speed is the moat** ” thesis for inference stacks. vLLM-Omni v0.20.0 shipped a large update with **Qwen3-Omni throughput +72% on H20** , major TTS latency/RTF reductions, broader diffusion support, and expanded quantization/backends. On the SGLang side, [@Yuchenj_UW](https://x.com/Yuchenj_UW/status/2052600316252876968) reported hearing numbers up to **57B tokens/day** on inference, while a long technical recap from [@ZhihuFrontier](https://x.com/ZhihuFrontier/status/2052768468249063482) detailed H20-specific DeepSeek optimization strategies across **prefill/decode disaggregation, FP8 FlashMLA, SBO, expert affinity, and observability**.
  * **Open models are increasingly “good enough” for coding and agent workloads** : [@masondrxy](https://x.com/masondrxy/status/2052781917955580246) said **Kimi K2.6 on Baseten** is about **5x cheaper than Opus 4.7** with roughly similar performance for many tasks, while [@caspar_br](https://x.com/caspar_br/status/2052817936344400132) reported swapping an internal Fleet model from **Sonnet 4.6 to Kimi K2.6** without noticing. That matches a broader shift noted by [@hwchase17](https://x.com/hwchase17/status/2052782958508175467) and [LangChain](https://x.com/LangChain/status/2052819061436973231): open-source LLMs are now viable default choices in many agentic stacks, especially as frontier inference pricing rises.



**Post-training, optimization, and alignment research: DGPO, Aurora, sparsity, and Claude “why”**

  * **Several notable optimization/post-training ideas landed at once** : [@TheTuringPost](https://x.com/TheTuringPost/status/2052539247320858975) summarized **DGPO (Distribution-Guided Policy Optimization)** as a refinement over GRPO that uses **token-level reward redistribution** , **Hellinger distance** instead of KL, and **entropy gating** to better reward useful exploration, reporting **46.0% on AIME 2025** and **60.0% on AIME 2024**. Separately, [@tilderesearch](https://x.com/tilderesearch/status/2052798181558370419) introduced **Aurora** , an optimizer designed to avoid a Muon-related neuron death failure mode; their **Aurora-1.1B** reportedly matches **Qwen3-1.7B** on several benchmarks with **25% fewer params** and **100x fewer training tokens**.
  * **Sparsity is back, but in hardware-friendly form** : [@SakanaAILabs](https://x.com/SakanaAILabs/status/2052787226136990029) and [@hardmaru](https://x.com/hardmaru/status/2052787980344099293) released **TwELL** , a sparse packing format and kernel stack for transformer FFNs that reportedly yields **20%+ training/inference speedups** on H100s by reshaping sparsity to fit GPU execution rather than forcing generic sparse formats. [@NVIDIAAI](https://x.com/NVIDIAAI/status/2052801759777874207) amplified the collaboration. In a different modularity direction, [@allen_ai](https://x.com/allen_ai/status/2052784995710681180) released **EMO** , an MoE trained so modular expert structure emerges from data, allowing selective expert use without hand-crafted priors.
  * **Anthropic published one of the day’s most important alignment threads** : In [“Teaching Claude why”](https://x.com/AnthropicAI/status/2052808787514228772), Anthropic said it has **eliminated the Claude 4 blackmail behavior** previously observed under certain conditions. The key claim is that demonstrations alone were insufficient; better results came from teaching the model **why misaligned behavior is wrong** , including **constitution-based documents** , **fictional aligned-AI stories** , and more diversified harmlessness training data. Supporting details came in follow-ups from [@AnthropicAI](https://x.com/AnthropicAI/status/2052808789297115628) and [the full post](https://x.com/AnthropicAI/status/2052808809182060581). This directly answered part of a transparency concern raised earlier by [@RyanPGreenblatt](https://x.com/RyanPGreenblatt/status/2052803011915980856) about the limited public understanding of what actually causes behavioral alignment.



**Agents, runtimes, and search/tooling: from direct corpus interaction to enterprise data agents**

  * **Agent architecture is shifting from “just call the model” to orchestration/harness design** : [@ii_posts](https://x.com/ii_posts/status/2052764819950907490) reported that long-running coding agents often fail by **stopping too early** , and that their **Zenith** orchestration harness won **5/8** long-horizon tasks at **43% of the strongest baseline’s cost**. This aligns with broader practitioner reports that journals, checkpoints, and runtime control matter as much as raw model quality—see [@vwxyzjn](https://x.com/vwxyzjn/status/2052779821202276761) on keeping an agent trial log, and [@nptacek](https://x.com/nptacek/status/2052742943321002366) for a vivid example of multi-agent memory conflicts and governance failure modes in a shared workspace.
  * **Search/retrieval is being rethought for agents** : [@zhuofengli96475](https://x.com/zhuofengli96475/status/2052784645398303198) introduced **Direct Corpus Interaction (DCI)** , replacing embedding model + vector DB + top-k retrieval with direct use of **grep/find/bash** over raw corpora. Reported gains include **BrowseComp-Plus 69% → 80%** on Claude Sonnet 4.6 and broad wins across **13 benchmarks**. Complementing that, [@_reachsumit](https://x.com/_reachsumit/status/2052593078788411895) highlighted **OBLIQ-Bench** , a benchmark for retrievers on **oblique / implicit queries** , and [@turbopuffer](https://x.com/turbopuffer/status/2052759200078733590) shipped **sparse vectors as a first-class retrieval primitive** that can compose with BM25 and attribute ranking in a single query plan.
  * **Enterprise data agents are emerging as a distinct category from coding agents** : [@matei_zaharia](https://x.com/matei_zaharia/status/2052778748941046180) and [@DbrxMosaicAI](https://x.com/DbrxMosaicAI/status/2052781813651984468) detailed how **Databricks Genie** tackles the non-deterministic nature of data work—asset discovery, conflicting business context, and missing deterministic tests—using **specialized knowledge search, parallel thinking, and multi-LLM designs**. Reported accuracy improved from **32% to 90%+** , with [@Yuchenj_UW](https://x.com/Yuchenj_UW/status/2052784305735397863) citing **91.6%** on enterprise data analysis tasks.



**Math, science, and robotics systems: DeepMind co-mathematician, AlphaEvolve, and Figure’s Helix-02**

  * **DeepMind’s AI co-mathematician is the most consequential science result in the set** : [@pushmeet](https://x.com/pushmeet/status/2052812585804685322) announced a **multi-agent AI co-mathematician** that scored **48% on FrontierMath Tier 4** , a new high, and was tested by mathematicians across multiple subfields. The more important signal is qualitative: [@wtgowers](https://x.com/wtgowers/status/2052830952758382850) said the system proved a result that could plausibly form a **PhD thesis chapter** , while [@kimmonismus](https://x.com/kimmonismus/status/2052849472586264997) usefully noted the result relied on custom infrastructure and large budgets, so it is not directly comparable to standard leaderboard runs. Even so, the paper strengthens the case that **agentic orchestration** now contributes a large fraction of frontier capability gains in research workflows.
  * **Google continues to emphasize self-improving systems in production science/infra** : [@Google](https://x.com/Google/status/2052794893206962598) gave an update on **AlphaEvolve** , saying the Gemini-powered coding agent is being used for **Google AI infrastructure** , **molecular simulations** , and **natural disaster risk prediction**. A companion post from [Google Cloud](https://x.com/Google/status/2052794909355094217) claimed real-world impact including **doubling training speed for massive AI models** and routing optimizations that save **15,000 km of travel annually**.
  * **Robotics demos are getting closer to coordinated household competence** : [@adcock_brett](https://x.com/adcock_brett/status/2052770989944242335) shared Figure’s latest demo of **two Helix-02 robots making a bed together fully autonomously** , with a follow-up linking the underlying system [here](https://x.com/adcock_brett/status/2052771762056974511). The more interesting claim was that the robots coordinated **without an explicit communication channel** , inferring each other’s likely actions from motion and camera observations. In the broader physical-AI direction, [@DrJimFan](https://x.com/DrJimFan/status/2052758642781487237) published a dense “**Robotics: Endgame** ” talk arguing for a roadmap built around **video world models, world action models, robot-data flywheels, and physical RL**.



**Top tweets (by engagement)**

  * **Anthropic alignment research** : [“Teaching Claude why”](https://x.com/AnthropicAI/status/2052808787514228772) was the highest-signal technical thread, claiming elimination of a previously observed blackmail behavior via training aimed at model understanding rather than demonstrations alone.
  * **OpenAI Codex product push** : [OpenAI’s Codex post](https://x.com/OpenAI/status/2052800507727781979) and the broader `/goal` discussion around long-running work marked a meaningful step from assistant UX toward agent runtime UX.
  * **HTML as an agent interface layer** : [@trq212](https://x.com/trq212/status/2052811606032269638) arguing that “**HTML is the new markdown** ” resonated unusually strongly, reflecting a broader shift toward agent-generated artifacts and custom interfaces.
  * **Figure’s household robotics demo** : [@adcock_brett](https://x.com/adcock_brett/status/2052770989944242335) on two Helix-02 robots making a bed was the standout robotics clip by engagement.
  * **DeepMind AI co-mathematician** : [@pushmeet](https://x.com/pushmeet/status/2052812585804685322) on the **48% FrontierMath Tier 4** result was the clearest science/reasoning milestone in the feed.



* * *

# AI Reddit Recap

## /r/LocalLlama + /r/localLLM Recap

### 1. Multi-Token Prediction Local Inference

  * **[Multi-Token Prediction (MTP) for LLaMA.cpp - Gemma 4 speedup by 40%](https://www.reddit.com/r/LocalLLaMA/comments/1t6se6r/multitoken_prediction_mtp_for_llamacpp_gemma_4/)** (Activity: 669): **A patched fork of**llama.cpp** adds **Multi-Token Prediction (MTP)** support and publishes quantized **Gemma 4 assistant GGUF** models on [Hugging Face](https://huggingface.co/collections/AtomicChat/gemma-4-assistant-gguf). On a **MacBook Pro M5 Max** , the author reports **Gemma 26B** generation improving from `97 tok/s` to `138 tok/s`—about a `42%` throughput increase—for the prompt _“Write a Python program to find the nth Fibonacci number using recursion”_ ; code is in [`AtomicBot-ai/atomic-llama-cpp-turboquant`](https://github.com/AtomicBot-ai/atomic-llama-cpp-turboquant), with an associated local app at [atomic.chat](http://atomic.chat).** Commenters asked for a stricter apples-to-apples benchmark using the **same seed** and `temperature=0.0` so outputs should match exactly, making it easier to verify that MTP does not degrade quality. There was also interest in compatibility with **LM Studio**.

    * Several commenters focused on validating whether **Multi-Token Prediction (MTP)** preserves generation quality: they suggested rerunning the comparison with the **same seed** and `temperature=0.0`, where deterministic decoding should produce identical output if MTP is not changing token choices. Another related suggestion was to force both runs to answer as similarly as possible so that any quality differences can be attributed to MTP rather than sampling variance.
    * There was a compatibility question about whether the new **llama.cpp MTP support** works through **LM Studio** , implying interest in whether frontends using llama.cpp backends expose or automatically benefit from the new speculative/multi-token path. A separate model-format request asked for **GGUF builds of[heretic](https://github.com/p-e-w/heretic)**, reflecting demand for llama.cpp-compatible quantized deployments.
  * **[Qwen3.6 27B uncensored heretic v2 Native MTP Preserved is Out Now With KLD 0.0021, 6/100 Refusals and the Full 15 MTPs Preserved and Retained, Available in Safetensors, GGUFs and NVFP4s formats.](https://www.reddit.com/r/LocalLLaMA/comments/1t5yajb/qwen36_27b_uncensored_heretic_v2_native_mtp/)** (Activity: 591): ****llmfan46** released **Qwen3.6-27B-uncensored-heretic-v2-Native-MTP-Preserved** on Hugging Face in multiple formats: [Safetensors](https://huggingface.co/llmfan46/Qwen3.6-27B-uncensored-heretic-v2-Native-MTP-Preserved), [GGUF](https://huggingface.co/llmfan46/Qwen3.6-27B-uncensored-heretic-v2-Native-MTP-Preserved-GGUF), [NVFP4 GGUF](https://huggingface.co/llmfan46/Qwen3.6-27B-uncensored-heretic-v2-Native-MTP-Preserved-NVFP4-GGUF), [NVFP4](https://huggingface.co/llmfan46/Qwen3.6-27B-uncensored-heretic-v2-Native-MTP-Preserved-NVFP4), [NVFP4 MLP-only](https://huggingface.co/llmfan46/Qwen3.6-27B-uncensored-heretic-v2-Native-MTP-Preserved-NVFP4-MLP-Only), and [GPTQ-Int4](https://huggingface.co/llmfan46/Qwen3.6-27B-uncensored-heretic-v2-Native-MTP-Preserved-GPTQ-Int4). The release claims **full preservation of all`15` native MTP heads**, **KLD`0.0021`**, **`6/100` refusals**, and includes benchmark results; the author’s model index is [here](https://huggingface.co/llmfan46/models).** Commenters asked for a smaller **`Q4_K_XS` GGUF** suitable for `16GB` VRAM with usable context, questioned whether **MTP works with TurboQuant-compressed KV cache** , and asked if the same MTP preservation approach could be applied to a **Gemma 4 dense** model. Another technical concern was that **NVFP4 + MTP on Blackwell** appears blocked or immature pending newer CUDA support.

    * Users asked for lower-memory quantization and runtime compatibility details, specifically a `Q4_K_XS` GGUF variant to fit `16GB` VRAM with usable context, and whether the preserved `15` MTP heads work when the KV cache is compressed with TurboQuant.
    * A technical concern was raised that the reported `KLD 0.0021` may not validate MTP behavior on the safety-edited distribution: if MTP draft heads were trained on the original refusal-heavy model while the base was uncensored, speculative decoding could have lower acceptance or actively bias generation back toward refusals on the exact prompts affected by the Heretic tuning.
    * Several implementation/platform questions focused on model-feature support: whether MTP can be transferred to a future dense Gemma 4-style model, whether `NVFP4` + MTP is currently usable on Blackwell given apparent CUDA/toolchain blockers, and whether included `mmproj` files still hit crashes referenced as `PR #22673`.



### 2. AI Accelerator Hardware and ROCm Support

  * **[AMD Intros Instinct MI350P Accelerator: CDNA 4 Comes to PCIe Cards](https://www.reddit.com/r/LocalLLaMA/comments/1t6b2x8/amd_intros_instinct_mi350p_accelerator_cdna_4/)** (Activity: 474): **[ServeTheHome reports](https://www.servethehome.com/amd-intros-instinct-mi350p-accelerator-cdna-4-comes-to-pcie-cards/) AMD’s **Instinct MI350P** , bringing **CDNA 4** Instinct MI350-class acceleration to a **PCIe add-in card** form factor. The discussion highlights HBM3E configurations listed as `144GB` and `288GB`, but AMD has not disclosed **pricing or availability**.** Commenters mainly focused on the missing pricing/availability; one sarcastically suggested `$499` would be “about right” for the HBM-heavy accelerator.

    * A commenter highlighted the key technical specification of the **AMD Instinct MI350P** PCIe card: `3.6 TB/s` memory bandwidth, paired with very large HBM3E capacities listed in the article/comments as `144 GB` and `288 GB`. No concrete pricing or availability information was provided in the thread, and commenters noted that this remains the main missing deployment detail.
  * **[Taiwanese company Skymizer announces HTX301 - PCIE inference card with 384GB of Memory at ~240 Watts](https://www.reddit.com/r/LocalLLaMA/comments/1t6tvfw/taiwanese_company_skymizer_announces_htx301_pcie/)** (Activity: 402): ****Skymizer** [announced the HTX301](https://skymizer.ai/skymizer-announces-htx301-reinventing-on-prem-ai-inference/), a PCIe inference card/reference platform with **six HTX301 chips** , **`384GB` of memory**, and claimed **~`240W`** power for local inference of models up to **`700B` parameters**. The company describes a _decode-first_ architecture with prefill/decode disaggregation and **LISA™** orchestration for scaling from `4B` to `700B` LLMs, but the announcement does not disclose key technical specs such as memory bandwidth, interconnect topology, token throughput, precision formats, or per-chip compute.** Commenters were strongly skeptical, calling the website mostly marketing/fluff and noting that without bandwidth, compute, pricing, availability, or third-party benchmarks, the claims are not yet technically verifiable.

    * Commenters noted that the announcement lacks the core specs needed to evaluate an inference accelerator: **memory bandwidth, aggregate compute throughput, interconnect details, and performance scaling across the six chips**. The headline `384GB` memory and `~240W` power are considered insufficient without benchmarks or a clear architecture breakdown.
    * A recurring technical concern is software support: even if the PCIe card exists, buyers need details on the runtime, compiler, model support, APIs, and framework integration needed to “tap into” the hardware. One commenter compared this risk to **ROCm** , arguing that accelerator hardware is only useful if the software stack is mature enough for real deployment.
    * Several commenters framed HTX301 as _vaporware until proven otherwise_ , comparing it against currently viable accelerator ecosystems: **Nvidia, AMD, Intel, Huawei, Apple silicon, and Google TPUs**. The skepticism is less about the possibility of custom inference silicon and more about whether Skymizer can provide production-ready benchmarks, availability, and ecosystem support.
  * **[vLLM ROCm has been added to Lemonade as an experimental backend](https://www.reddit.com/r/LocalLLaMA/comments/1t7g70j/vllm_rocm_has_been_added_to_lemonade_as_an/)** (Activity: 313): **The image is a technical announcement that**Lemonade now supports`vLLM` on AMD ROCm as an experimental backend** for Linux/Strix Halo, with the shown commands `lemonade backends install vllm:rocm` and `lemonade run Qwen3.5-0.8B-vLLM` ([image](https://i.redd.it/kesrnt4lgyzg1.png)). The post frames this as a way to run `.safetensors` LLMs via vLLM before GGUF conversion, complementing `llama.cpp`; links include the [quick start guide](https://lemonade-server.ai/news/vllm-rocm.html), [Lemonade GitHub](https://github.com/lemonade-sdk/lemonade), and a standalone portable vLLM ROCm executable at [`lemonade-sdk/vllm-rocm`](https://github.com/lemonade-sdk/vllm-rocm/).** Commenters were interested in what `vLLM` offers over `llama.cpp` on Strix Halo, and one praised the availability of Arch and Fedora releases.

    * Users highlighted backend/platform support details: Lemonade’s experimental **vLLM ROCm** integration has **Arch** and **Fedora** releases, and AMD’s jfowers pointed to a standalone portable vLLM ROCm executable at [github.com/lemonade-sdk/vllm-rocm](https://github.com/lemonade-sdk/vllm-rocm/).
    * A technical comparison question was raised about running **vLLM on AMD Strix Halo** versus `llama.cpp`, specifically what vLLM offers over llama.cpp for local inference on that hardware.
    * There was interest in broader ROCm GPU compatibility, with a user asking whether older AMD datacenter cards such as the **MI50** could be supported.



## Less Technical AI Subreddit Recap

> /r/Singularity, /r/Oobabooga, /r/MachineLearning, /r/OpenAI, /r/ClaudeAI, /r/StableDiffusion, /r/ChatGPT, /r/ChatGPTCoding, /r/aivideo, /r/aivideo

### 1. Vibe Coding Debugging Hangover

  * **[the part nobody warns you about](https://www.reddit.com/r/ClaudeAI/comments/1t5vs8t/the_part_nobody_warns_you_about/)** (Activity: 2145): **The post describes a common**AI-assisted rapid prototyping failure mode** : an app was built in ~`3 days`, but the author has spent ~`2 weeks` debugging slow UI/build/test loops, unclear generated code, oversized functions, ambiguous state variables, and undocumented agent-made decisions. Top technical suggestions were to have **Claude generate automated tests** to replace repeated manual button-click regression checks, and to develop in smaller phases with continuous debugging so early defects do not become architectural assumptions or dependencies.** Commenters framed the issue as partly process-related: defered validation creates a “Gordian knot” where fixes introduce new bugs. One harsher take was that this happens when the developer “doesn’t know what [they’re] doing,” implying insufficient engineering discipline rather than an unavoidable cost of building.

    * Several commenters emphasized adding automated tests early rather than manually clicking through UI flows: one suggested asking **Claude** to generate tests so regressions are caught continuously, while another recommended building in phases and debugging incrementally because _“early bugs become assumptions, and then dependencies”_ —delaying validation can turn fixes into cascading regressions.
    * A commenter recommended [**Storybloq**](https://github.com/Storybloq/storybloq), described as a **Claude Code** tool that adds a git-tracked project memory and governance layer. The claimed technical benefit is auditability of agent decisions over time, helping future debugging by preserving why prior implementation choices were made.
  * **[thanks Claude](https://www.reddit.com/r/ClaudeCode/comments/1t67k33/thanks_claude/)** (Activity: 2239): **The image is a**non-technical meme/tweet screenshot** joking that AI tools like Claude increase the speed of prototyping _and_ abandonment: _“thanks to AI i create and abandon projects 4x faster.”_ In context, the post extends the joke to buying more domains and “vibe coding” via [ijustvibecodedthis.com](http://ijustvibecodedthis.com); the image is here: &lt;https://i.redd.it/7oz5ncnq8pzg1.png>.** Comments frame this as a humorous but real critique of AI-assisted development: LLMs lower the cost of generating ideas and prototypes, but **shipping, productionizing, and user adoption remain the hard parts**.




# AI Discords

Unfortunately, Discord shut down our access today. We will not bring it back in this form but we will be shipping the new AINews soon. Thanks for reading to here, it was a good run.

---

## [GPT-Realtime-2, -Translate, and -Whisper: new SOTA realtime voice APIs](https://news.smol.ai/issues/26-05-07-gpt-realtime-2/)
*🌐 Smol AI News | 2026-05-07*

**a quiet day.**

> AI News for 5/6/2026-5/7/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

OpenAI launched realtime-1.5 3 months ago, but it was a relative drop in the bucket because it was still 4o based intelligence (a +5% bump in Big Bench Audio). You could tell the sheer confidence in today’s realtime-2 release (with a +15.2% bump in BBA), and it was appropriately well received:

As the blogpost explains, 3 models are being released, which one might simplify to “voice-in, voice-out, and voice-to-voice”:

The focus is less about “voice quality”, and more on usability. TLDR:

Preambles: Developers can enable short phrases before a main response, like “let me check that” or “one moment while I look into it”.

Parallel tool calls and tool transparency: The model can call multiple tools at once and make those actions audible with phrases like “checking your calendar” or “looking that up now,” helping agents stay responsive while completing tasks.

Stronger recovery behavior: The model can recover more gracefully by saying things like “I’m having trouble with that right now,” instead of failing or breaking.

Longer context: 32K → 128K

Stronger domain understanding: The model better retains specialized terminology, proper nouns, healthcare terms, and other vocabulary

More controllable tone and delivery: The model can better adjust its tone—speaking calmly, empathetically, or upbeat, based on context

Adjustable reasoning effort: Developers can now select from minimal, low, medium, high, and xhigh reasoning levels, with low as the default.

The Demo video showed off how the audio model is better tuned when the main speaker is speaking to someone else, so it stops interrupting so much:

* * *

# AI Twitter Recap

**Top Story: GPT-Realtime-2 and OpenAI voice AI commentary**

## What happened

**OpenAI launched three new streaming audio models in the Realtime API: GPT-Realtime-2, GPT-Realtime-Translate, and GPT-Realtime-Whisper.** OpenAI positioned GPT-Realtime-2 as its “most intelligent voice model yet,” bringing “GPT-5-class reasoning” to real-time voice agents that can listen, reason, handle interruptions, use tools, and sustain longer conversations as they unfold [@OpenAI](https://x.com/OpenAI/status/2052438194625593804). The companion models target live speech translation and transcription: GPT-Realtime-Translate supports streaming translation from 70+ input languages into 13 output languages, while GPT-Realtime-Whisper streams transcription/captions as speech is produced [@OpenAI](https://x.com/OpenAI/status/2052438196454379986), [@OpenAIDevs](https://x.com/OpenAIDevs/status/2052440907933474954). OpenAI said the models are available in the Realtime API now, while ChatGPT voice upgrades are still pending: “Stay tuned, we’re cooking” [@OpenAI](https://x.com/OpenAI/status/2052438197695877316). Sam Altman framed the launch around a behavioral shift: users increasingly use voice with AI when they need to “dump” lots of context, and OpenAI is also working on improvements to ChatGPT voice [@sama](https://x.com/sama/status/2052462271667028211).

## Facts vs. opinions

**Factual / directly claimed by OpenAI and evaluators**

  * **Model family:** GPT-Realtime-2, GPT-Realtime-Translate, GPT-Realtime-Whisper are available in the Realtime API today [@OpenAIDevs](https://x.com/OpenAIDevs/status/2052440968763515223).
  * **GPT-Realtime-2 capabilities:** reasoning-oriented native speech-to-speech model for production voice agents; supports tool use/action, interruption recovery, longer conversations, and “GPT-5-class reasoning” per OpenAI’s wording [@OpenAI](https://x.com/OpenAI/status/2052438194625593804), [@reach_vb](https://x.com/reach_vb/status/2052438371058737280).
  * **Context window:** community/OpenAI-dev commentary reported **128K context** for GPT-Realtime-2 voice agents [@reach_vb](https://x.com/reach_vb/status/2052438371058737280); Artificial Analysis independently reported the context window increased from **32K to 128K** , with **32K max output tokens** [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2052486470469140777).
  * **Translation:** GPT-Realtime-Translate supports live speech translation from **70+ input languages** into **13 output languages** [@OpenAI](https://x.com/OpenAI/status/2052438196454379986), [@reach_vb](https://x.com/reach_vb/status/2052438371058737280).
  * **Transcription:** GPT-Realtime-Whisper provides low-latency streaming transcription in the Realtime API for captions, notes, and continuous speech understanding [@OpenAIDevs](https://x.com/OpenAIDevs/status/2052440957258489859).
  * **Prompting/control:** OpenAI published a voice prompting guide covering reasoning effort, preambles, tool behavior, unclear audio handling, exact entity capture, and state maintenance in long sessions [@OpenAIDevs](https://x.com/OpenAIDevs/status/2052530378184032560).
  * **Independent benchmarks:** Scale AI reported GPT-Realtime-2 took the top spot on its Audio MultiChallenge S2S leaderboard, with instruction retention rising from **36.7% to 70.8% APR** versus GPT-Realtime-1.5 and strong performance on voice editing/real-time repair [@ScaleAILabs](https://x.com/ScaleAILabs/status/2052451341071683732).
  * **Independent benchmarks:** Artificial Analysis reported **96.6%** on Big Bench Audio speech-to-speech reasoning, **96.1%** on its Conversational Dynamics benchmark, average time-to-first-audio of **2.33s** at high reasoning and **1.12s** at minimal reasoning, and unchanged audio pricing of **$1.15/hour input** and **$4.61/hour output** [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2052486470469140777), [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2052486478501204415).
  * **Reasoning-effort controls:** Artificial Analysis reported adjustable reasoning levels: **minimal, low, medium, high, xhigh** , with **low** as default [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2052486470469140777).
  * **Enterprise/product evals:** Glean said GPT-Realtime-2 delivered a **42.9% relative increase in helpfulness** over the previous version in internal evals for real-time organizational voice interactions [@glean](https://x.com/glean/status/2052440702169108990). Genspark said its Call for Me Agent moved to GPT-Realtime-2 and saw **+26% effective conversation rate** and fewer dropped calls [@genspark_ai](https://x.com/genspark_ai/status/2052524670088556557).



**Opinions / interpretation / commentary**

  * Supporters described the launch as a “big step forward” for voice agents [@sama](https://x.com/sama/status/2052462271667028211), “total realtime victory” [@reach_vb](https://x.com/reach_vb/status/2052442056392405383), and the first speech-to-speech model good enough for “real work” in complex voice agents [@kwindla](https://x.com/kwindla/status/2052521318688739811).
  * A more cautious view: Simon Willison noted the announcement does **not** mean ChatGPT Voice Mode itself has upgraded yet; the ChatGPT upgrade “sounds” like it is coming soon [@simonw](https://x.com/simonw/status/2052439091577496054), [@simonw](https://x.com/simonw/status/2052439181885153757).
  * Interface skepticism: Will Depue compared audio to VR—frequently exciting, but historically not sticky as an interface—while arguing that real-time tool use, reasoning while speaking, and live translation are the kinds of capabilities that could make audio interfaces finally take off [@willdepue](https://x.com/willdepue/status/2052493097586823353).
  * Broader UX optimism: several commenters framed voice as more natural and bandwidth-efficient for humans [@BorisMPower](https://x.com/BorisMPower/status/2052471142921994332), a path toward Jarvis-like always-available computer agents [@willdepue](https://x.com/willdepue/status/2052494388413235672), or eventually displaced by even higher-bandwidth BCIs [@iScienceLuvr](https://x.com/iScienceLuvr/status/2052465922640593068).
  * Competitive context: Elon Musk pushed Grok Voice for customer support [@elonmusk](https://x.com/elonmusk/status/2052530063913189879), underscoring that real-time voice support/customer-service automation is now a competitive surface across labs.



## Technical details and benchmark data

**GPT-Realtime-2**

  * Native speech-to-speech / real-time voice model, released via OpenAI’s Realtime API [@OpenAI](https://x.com/OpenAI/status/2052438194625593804).
  * Framed as “GPT-5-class reasoning” for voice agents [@OpenAI](https://x.com/OpenAI/status/2052438194625593804).
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
  * Conversational features: supports short preambles before main responses—e.g. “let me check that”—and audible transparency during tool calls—e.g. “checking your calendar” [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2052486470469140777).



**Benchmarks**

  * **Scale AI Audio MultiChallenge S2S:** GPT-Realtime-2 placed #1; instruction retention improved from **36.7% to 70.8% APR** versus GPT-Realtime-1.5; strong voice editing when users repair/revise speech in real time [@ScaleAILabs](https://x.com/ScaleAILabs/status/2052451341071683732).
  * **Artificial Analysis Big Bench Audio:** GPT-Realtime-2 high variant scored **96.6%** , reported as equal to Gemini 3.1 Flash Live Preview High and about **~13%** above the previous highest result [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2052486470469140777).
  * Justin Uberti separately summarized the improvement as **15 percentage points vs. GPT-Realtime-1.5** on Big Bench Audio, near saturation [@juberti](https://x.com/juberti/status/2052507302092296252).
  * **Conversational Dynamics / Full Duplex Bench subset:** GPT-Realtime-2 minimal variant scored **96.1%** , with strengths in pause handling and turn-taking [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2052486470469140777).



**GPT-Realtime-Translate**

  * Live streaming speech translation from **70+ input languages** to **13 output languages** [@OpenAI](https://x.com/OpenAI/status/2052438196454379986).
  * OpenAI cofounder Greg Brockman said real-time voice-to-voice translation has been an anticipated OpenAI application since the company’s early days and is now available for anyone to build with [@gdb](https://x.com/gdb/status/2052480998668206262).
  * Vimeo demonstrated live dubbing with no pre-loaded captions, showing translations generated fully live [@Vimeo](https://x.com/Vimeo/status/2052442588201029684).
  * Junling Zhang highlighted the new real-time translation model and encouraged API usage [@jxnlco](https://x.com/jxnlco/status/2052449634266812744).
  * Boris Power said live translation “actually works incredibly well” and plans to use it regularly [@BorisMPower](https://x.com/BorisMPower/status/2052472038967890022).



**GPT-Realtime-Whisper**

  * Streaming transcription as people speak, for real-time captions, notes, and speech understanding [@OpenAI](https://x.com/OpenAI/status/2052438196454379986).
  * Justin Uberti described it as “Whisper, but now with realtime streaming” and updated demos to use the new model [@juberti](https://x.com/juberti/status/2052478775523512356).
  * Uberti also built a delay selector to expose the latency/accuracy tradeoff in a real-time typing demo [@juberti](https://x.com/juberti/status/2052504986391879788).



## Product integrations and demos

  * **Glean:** shipped real-time voice powered by GPT-Realtime-2, grounded in organizational context; internal evals showed **42.9% relative helpfulness increase** over the previous version [@glean](https://x.com/glean/status/2052440702169108990).
  * **Vimeo:** demonstrated live dubbing using GPT-Realtime-Translate, with translations generated live and no pre-loaded captions [@Vimeo](https://x.com/Vimeo/status/2052442588201029684).
  * **Genspark:** upgraded its Call for Me Agent to GPT-Realtime-2; Genspark Realtime Voice is next; claimed sharper reasoning, tighter instruction following, **+26% effective conversation rate** , and fewer dropped calls [@genspark_ai](https://x.com/genspark_ai/status/2052524670088556557).
  * **Gradient Bang / game-agent demo:** Kyle Windland said GPT-Realtime-2 is the first OpenAI speech-to-speech model good enough for his voice agents that do “real work,” showing it as the ship AI in a complex agent with tool calls and subagents [@kwindla](https://x.com/kwindla/status/2052521318688739811).
  * **Voice-controlled market dashboard:** Levin Stanley demoed GPT-Realtime-2 controlling an interface by intent—“Focus on Apple,” “How did it do over the last 30 days?”, “Go back”—arguing that real-time interruption and reasoning change the UI loop from navigation to direction [@levinstanley](https://x.com/levinstanley/status/2052506605044842672).
  * **Realtime demos:** Justin Uberti updated `hello-realtime` for GPT-Realtime-2 and provided a phone demo number [@juberti](https://x.com/juberti/status/2052469176821002676); Diego Cabezas posted a quick GPT-Realtime-2 demo [@diegocabezas01](https://x.com/diegocabezas01/status/2052492653082681485); Ray Fernando hosted a “Building a Live Translator” broadcast [@RayFernando1337](https://x.com/RayFernando1337/status/2052479718495318143).
  * **Reachy Mini / robotics voice interface interest:** Clement Delangue asked who would add the new voice capabilities to Reachy Mini [@ClementDelangue](https://x.com/ClementDelangue/status/2052449977725534363), after earlier asking voice AI labs such as Gradium, Kyutai, and ElevenLabs who could help with a robot voice use case [@ClementDelangue](https://x.com/ClementDelangue/status/2052385809655828907).



## Why this matters

The launch pushes voice agents from “speech I/O wrapper around a chatbot” toward **full-duplex, tool-using, long-context, reasoning agents**. The technical shift is not just better ASR or TTS; it is the combination of low-latency turn-taking, interruption handling, longer context, tool-call transparency, and adjustable reasoning effort in a single real-time loop. That matters for customer support, meetings, accessibility, live translation, robotics, browser/computer control, and hands-free workflows where text chat is too slow or awkward.

The most important engineering implication is that voice apps now need to be designed as **stateful real-time systems** , not prompt-response endpoints. OpenAI’s prompting guide explicitly points developers toward reasoning-effort tuning, preambles, tool behavior, unclear-audio recovery, entity capture, and long-session state management [@OpenAIDevs](https://x.com/OpenAIDevs/status/2052530378184032560). This suggests voice-agent quality will increasingly depend on harness design: latency budgets, interruption semantics, tool-call UX, conversational memory, and failure recovery—not just raw model selection.

The remaining uncertainty is distribution. The API model is available now, but ChatGPT voice mode has not yet received the upgrade, per Simon Willison’s observation [@simonw](https://x.com/simonw/status/2052439091577496054). If and when ChatGPT Voice gets the same capabilities, the consumer impact could be much larger. Until then, the launch primarily benefits developers and platforms building specialized real-time agents.

* * *

**OpenAI Voice, Codex, and Cybersecurity Releases**

  * **GPT-Realtime-2 and new audio stack** : OpenAI released **GPT-Realtime-2** in the API, described as its most capable voice model with **GPT-5-class reasoning** , tool use, interruption handling, and longer conversations; it ships alongside **GPT-Realtime-Translate** for streaming translation across **70+ input languages / 13 output languages** and **GPT-Realtime-Whisper** for low-latency streaming transcription [@OpenAI](https://x.com/OpenAI/status/2052438194625593804). OpenAI says ChatGPT voice updates are still forthcoming [@OpenAI](https://x.com/OpenAI/status/2052438197695877316). Artificial Analysis reports GPT-Realtime-2 reaches **96.6% on Big Bench Audio** , leads its Conversational Dynamics benchmark at **96.1%** , expands context from **32K to 128K** , and keeps audio pricing unchanged [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2052486470469140777). Scale AI also placed GPT-Realtime-2 at #1 on its Audio MultiChallenge S2S leaderboard, with instruction retention rising from **36.7% to 70.8% APR** versus GPT-Realtime-1.5 [@ScaleAILabs](https://x.com/ScaleAILabs/status/2052451341071683732).
  * **Codex gets browser control** : OpenAI shipped a **Chrome plugin for Codex** on macOS and Windows, letting Codex operate across background tabs without taking over the user’s browser; it can use plugins where possible, Chrome for logged-in sites, and combine tools for workflows like debugging browser flows, checking dashboards, research, or CRM updates [@OpenAI](https://x.com/OpenAI/status/2052480800004956323). The dev team emphasized browser DevTools, multi-tab parallelism, and web-app testing as key use cases [@OpenAIDevs](https://x.com/OpenAIDevs/status/2052481136971125158).
  * **Cyber-specific GPT-5.5 access** : OpenAI announced **GPT-5.5 with Trusted Access for Cyber** for defensive workflows and a limited-preview **GPT-5.5-Cyber** for authorized red teaming, pentesting, and validation under enhanced verification and account controls [@cryps1s](https://x.com/cryps1s/status/2052508963409998283). Separately, Micah Carroll said OpenAI found instances of accidental **CoT grading** in previous RL runs after building a scanner, but did not find clear evidence those instances degraded CoT monitorability [@MicahCarroll](https://x.com/MicahCarroll/status/2052451995467018427).



**Anthropic, Interpretability, and AI Safety Tooling**

  * **Natural Language Autoencoders** : Anthropic introduced **Natural Language Autoencoders** , a method for translating model activations into human-readable text so researchers can inspect “thought-like” internal representations rather than only sparse features or supervised probes [@AnthropicAI](https://x.com/AnthropicAI/status/2052435436157452769). Miles Brundage/ML-powered commentary framed NLAs as complementary to probing and dictionary learning, noting they revealed planning behavior and helped identify training-pipeline translation bugs; open-model NLAs are available on Neuronpedia [@mlpowered](https://x.com/mlpowered/status/2052446867037020402). Ryan Greenblatt cautioned that early tests did not recover “internal CoT” on single-forward-pass math cases, suggesting limitations or missing activation locations [@RyanPGreenblatt](https://x.com/RyanPGreenblatt/status/2052458229624672549).
  * **Goodfire’s neural geometry agenda** : Goodfire launched a research series arguing neural networks “think in shapes,” with **manifolds** as a core primitive for interpreting and controlling behavior [@GoodfireAI](https://x.com/GoodfireAI/status/2052420446910644616). The thread contrasts manifold-level structure with SAE-style feature shattering, includes examples where steering along a learned manifold preserves coherent world-model behavior, and teases work on unsupervised manifold discovery and in-context geometry [@GoodfireAI](https://x.com/GoodfireAI/status/2052420594193650167). Goodfire also linked the agenda to scientific discovery, citing reverse-engineering of a scientific foundation model to uncover biomarker structure in a curved manifold [@GoodfireAI](https://x.com/GoodfireAI/status/2052468622103085107).
  * **Anthropic safety infrastructure** : Anthropic shared the research agenda for **The Anthropic Institute** , focused on economic diffusion, threats/resilience, AI systems in the wild, and **AI-driven R &D** with human visibility and control [@AnthropicAI](https://x.com/AnthropicAI/status/2052385812881228218). It also moved **Petri** , its open-source interactive behavioral-evals tool, to Meridian Labs as an independent project [@AnthropicAI](https://x.com/AnthropicAI/status/2052494460966019137), and opened its security bug bounty publicly on HackerOne [@AnthropicAI](https://x.com/AnthropicAI/status/2052466175540629965).



**Agents, RL Environments, and Coding Workflows**

  * **Prime Intellect Lab and Ramp Fast Ask** : Prime Intellect opened **Lab** out of beta as a full stack for building RL environments/evals, evaluating, post-training, deploying, and serving agents [@PrimeIntellect](https://x.com/PrimeIntellect/status/2052225145725698102). Ramp Labs used Prime Intellect to train **Fast Ask** , a small RL-trained subagent for spreadsheet QA that reportedly scores **+4% exact-match over Opus** at **Haiku-level latency** [@RampLabs](https://x.com/RampLabs/status/2052448843099254956); Prime says it outperformed Opus 4.6 while running faster and cheaper [@PrimeIntellect](https://x.com/PrimeIntellect/status/2052465182014840987).
  * **Hermes Agent momentum** : Nous/Teknium shipped **Hermes Agent v0.13.0** with multi-agent orchestration via Kanban, enforced goal completion with `/goal`, disk-usage optimizations, custom LLM providers, and custom gateway channels [@Teknium](https://x.com/Teknium/status/2052495174404874714). Earlier updates added agent-free cron jobs via Hermes Gateway for programmatic recurring tasks [@Teknium](https://x.com/Teknium/status/2052219963591762194), blank-slate profiles with `\--no-skills` [@Teknium](https://x.com/Teknium/status/2052351650279645590), and Lightpanda as a machine-native browser backend with Chrome fallback [@lightpanda_io](https://x.com/lightpanda_io/status/2052369346928758861).
  * **Cursor orchestration and PR workflows** : Cursor introduced `/orchestrate`, a skill that recursively spawns planner, worker, and verifier agents via the Cursor SDK; internally it reportedly cut skill token use by **20%** while improving evals and reduced backend cold-start time by **80%** [@cursor_ai](https://x.com/cursor_ai/status/2052432778743210127). Cursor 3 also added an integrated PR review experience with diffs, commits, comments, review status, a file tree, and skill quick-action pills [@cursor_ai](https://x.com/cursor_ai/status/2052489387305488609).
  * **Agent infra patterns** : LangGraph is adding **delta channels** , storing checkpoint history as diffs to control storage bloat for long-context agents [@sydneyrunkle](https://x.com/sydneyrunkle/status/2052344141963555312). Deep Agents added sandbox backends for provider-agnostic isolated execution across Daytona, Modal, Runloop, and LangSmith, with an **auth proxy** pattern to keep credentials out of prompt-injectable sandboxes [@sydneyrunkle](https://x.com/sydneyrunkle/status/2052459962169966752).



**Models, Benchmarks, and Inference Systems**

  * **xAI, Zhipu, Zyphra, DeepSeek ecosystem** : xAI made **Image Generation Quality Mode** available on the xAI API after powering more than **300M images** in Grok, claiming better realism, text rendering, and creative control [@xai](https://x.com/xai/status/2052193877675983031). Zhipu published the **GLM-5V-Turbo technical report** , highlighting CogViT dual-teacher distillation, multimodal multi-token prediction, multimodal coding/tool use, and RL across 30+ task categories [@Zai_org](https://x.com/Zai_org/status/2052426777654387168). Zyphra’s **ZAYA1-8B** was described as AMD-trained, using under **1B active parameters** , large-scale RL, and a test-time method called **Markovian RSA** [@kimmonismus](https://x.com/kimmonismus/status/2052346978240205249). Antirez also released **DS4** , a specialized inference engine for **DeepSeek v4 Flash** built on llama.cpp/GGML lineage [@antirez](https://x.com/antirez/status/2052405820235678175).
  * **Google model and API updates** : Google AI Studio announced **Gemini 3.1 Flash-Lite** as its most cost-efficient model for high-volume agentic tasks, translation, and simple data processing [@GoogleAIStudio](https://x.com/GoogleAIStudio/status/2052453828272812310). Google also evolved the **Gemini Interactions API** from role-based `user/model` messages to typed **steps** such as `user_input`, `thought`, `function_call`, `tool_call`, and `model_output`, targeting richer multi-step agent workflows [@GoogleAIStudio](https://x.com/GoogleAIStudio/status/2052487438967140700). Gemma 4’s MTP/speculative decoding was reported to deliver up to **3× faster** on-device inference [@googlegemma](https://x.com/googlegemma/status/2052468624657654194), with independent vLLM tests showing large throughput gains and **129 tok/s** on simple generation on an RTX Pro 6000 [@bnjmn_marie](https://x.com/bnjmn_marie/status/2052286398707687650).
  * **Sequence models and coding evals** : Aviv Bick and Albert Gu introduced **Raven** , a fixed-state sequence model that learns which finite memory slots to update, aiming to fix persistence failures in SSMs and sliding-window attention and outperform prior linear models at **16× training sequence length** [@avivbick](https://x.com/avivbick/status/2052438903924396377), [@_albertgu](https://x.com/_albertgu/status/2052442144879862003). Scale released the **SWE Atlas Refactoring** leaderboard, testing whether agents can restructure code without regressions; **Claude Opus 4.7 with Claude Code** leads [@ScaleAILabs](https://x.com/ScaleAILabs/status/2052434456510878021). Arena’s longitudinal analysis says open models have largely closed the Text Arena gap, with the proprietary lead now around **+30 Arena points** , though expert prompts remain harder [@arena](https://x.com/arena/status/2052455463573426452).



**AI Infrastructure, Health, Robotics, and Applied Products**

  * **Compute and infrastructure** : Anthropic’s SpaceX/xAI compute deal remained a major theme: Dario Amodei called the SpaceX partnership “visionary engineering + Claude” [@Mononofu](https://x.com/Mononofu/status/2052212359536496961), while Simon Willison highlighted that Anthropic reportedly gets **Colossus 1** , xAI keeps the larger **Colossus 2** , and Colossus 1 has environmental controversy [@simonw](https://x.com/simonw/status/2052436629365948920). Lambda closed a **$1B senior secured credit facility** to expand AI factories [@LambdaAPI](https://x.com/LambdaAPI/status/2052373882963972496), AMD promoted **MI350P PCIe** with **144GB HBM3E** and up to **2299 TFLOPS MXFP4** [@AMD](https://x.com/AMD/status/2052373018400219648), and Ai2 brought new NSF OMAI compute online with **NVIDIA Blackwell Ultra** systems from a **$152M** NSF/NVIDIA investment [@allen_ai](https://x.com/allen_ai/status/2052403904139169940).
  * **Google Health and medical AI** : Google is turning Fitbit into the **Google Health** app on May 26, combining Fitbit tracking with Google services and a Gemini-powered **Google Health Coach** [@googlehealth](https://x.com/googlehealth/status/2052392762255761701). Google says Health Premium will be included in AI Pro and Ultra plans [@shimritby](https://x.com/shimritby/status/2052439569136767291), and announced **Fitbit Air** , a screenless wearable with up to one-week battery and $99.99 preorder pricing [@Google](https://x.com/Google/status/2052501704155775481). Separately, Glass Health launched an ambient scribing API at **$0.85/hour** for transcription plus token-priced note generation [@GlassHealthHQ](https://x.com/GlassHealthHQ/status/2052385429010121130).
  * **Robotics and local agents** : Perplexity released **Personal Computer** in a new Mac app, letting agents operate across local files, native Mac apps, web, and Perplexity servers, including remote initiation from iPhone and always-on Mac mini setups [@perplexity_ai](https://x.com/perplexity_ai/status/2052445405754040816). NVIDIA Robotics highlighted Hugging Face’s Reachy Mini “agentic robotics app store” and **Isaac GR00T N** integration with LeRobot workflows [@NVIDIARobotics](https://x.com/NVIDIARobotics/status/2052446013949149649). EO-1 is now available through the standard LeRobot policy interface for robot-control training/eval/deploy workflows [@SongHaomin92651](https://x.com/SongHaomin92651/status/2052360599703867415).



**Top tweets by engagement**

  * **OpenAI GPT-Realtime-2 API launch** — **11.7K** engagement [@OpenAI](https://x.com/OpenAI/status/2052438194625593804)
  * **Anthropic Natural Language Autoencoders** — **10.1K** engagement [@AnthropicAI](https://x.com/AnthropicAI/status/2052435436157452769)
  * **Claude Mythos helped Firefox fix more security bugs in April than prior 15 months** — **9.7K** engagement [@alexalbert__](https://x.com/alexalbert__/status/2052468573516513762)
  * **OpenAI Codex Chrome plugin** — **7.7K** engagement [@OpenAI](https://x.com/OpenAI/status/2052480800004956323)
  * **Goodfire neural geometry research agenda** — **5.1K** engagement [@GoodfireAI](https://x.com/GoodfireAI/status/2052420446910644616)
  * **Sam Altman on voice as a high-context AI interface** — **5.0K** engagement [@sama](https://x.com/sama/status/2052462271667028211)
  * **xAI Image Generation Quality Mode API** — **4.5K** engagement [@xai](https://x.com/xai/status/2052193877675983031)



* * *

# AI Reddit Recap

## /r/LocalLlama + /r/localLLM Recap

### 1. Qwen3.6 27B Local Inference and Quantization

  * **[2.5x faster inference with Qwen 3.6 27B using MTP - Finally a viable option for local agentic coding - 262k context on 48GB - Fixed chat template - Drop-in OpenAI and Anthropic API endpoints](https://www.reddit.com/r/LocalLLaMA/comments/1t57xuu/25x_faster_inference_with_qwen_36_27b_using_mtp/)** (Activity: 1798): **A recent**llama.cpp** MTP PR ([#22673](https://github.com/ggml-org/llama.cpp/pull/22673)) enables Qwen 3.6 27B’s built-in multi-token prediction tensors for speculative decoding; the poster converted MTP-capable GGUF quants ([HF](https://huggingface.co/froggeric/Qwen3.6-27B-MTP-GGUF)) and reports **~`2.5×` faster generation** on an M2 Max 96GB, reaching **`28 tok/s`** with `\--spec-type mtp --spec-draft-n-max 3`. They also published fixed Jinja chat templates ([HF](https://huggingface.co/froggeric/Qwen-Fixed-Chat-Templates)) and provide `llama-server` settings for OpenAI/Anthropic-compatible local serving with `q8_0` KV cache and up to **`262144` context**; recommendations emphasize `q8_0-mtp` as the best speed/quality quant, avoiding `q4_0` KV beyond `64k`, and note that Qwen3.6-27B only uses KV cache in **`16/65` layers** due to hybrid linear attention, reducing KV memory ~`4×`. A commenter reports on an **RTX Pro 6000 Max-Q** that Qwen 3.6 “2.7B” Q8 increases from **`36 tok/s` to `78 tok/s`** with MTP, at ~`20%` slower prompt processing, with no observed output-quality degradation; the post also warns that **vision currently crashes llama.cpp when combined with MTP**.** Commenters broadly frame this as part of a major recent acceleration in local inference, making consumer-hardware agentic coding more viable. One technical question asks whether `turbo3`/`turbo4` was merged separately or is part of the MTP PR.

    * A user benchmarked `qwen 3.6 2.7B Q8` on an **RTX Pro 6000 MaxQ** and reported generation increasing from `36 tok/s` to `78 tok/s` with **MTP** , roughly a `2.17x` speedup. They noted an approximately `20%` prompt-processing slowdown, but said output quality appeared unchanged, making the tradeoff favorable for generation-heavy workloads.
    * One commenter asked whether the speedup depends on the recent `turbo3`/`turbo4` merge or is specifically part of the **MTP PR** , highlighting that the implementation path matters for reproducing the claimed inference gains.
    * There was a technical comparison question against **Qwen 3.6 Dflash** variants and low-bit `iq3_XS` quantizations. The commenter reported usually fitting `256k` context into `16GB` VRAM and asked whether these quants can also support `256k` context without `mmproj`, indicating interest in KV-cache/context-length feasibility across quant formats.
  * **[Quality comparison between Qwen 3.6 27B quantizations (BF16, Q8_0, Q6_K, Q5_K_XL, Q4_K_XL, IQ4_XS, IQ3_XXS,...)](https://www.reddit.com/r/LocalLLaMA/comments/1t53dhp/quality_comparison_between_qwen_36_27b/)** (Activity: 820): **The post benchmarks**Qwen 3.6 27B** GGUF quantizations on a deliberately odd PGN-to-SVG chess-rendering task, testing board-state tracking, piece placement, orientation, and last-move highlighting with identical `llama.cpp` sampling settings (`temp=0.6`, `top_p=0.95`, `top_k=20`, `ctx=65536`). The author reports **BF16/Q8_0** as essentially correct, **Q6_K** showing placement degradation, **Q5_K_XL/Q4_K_XL/IQ4_XS** still usable, **IQ3_XXS** mostly correct but with wrong board orientation, and **Q2_K_XL** structurally broken despite correct piece positions; full outputs are posted at [qwen3-6-27b-benchmark.vercel.app](https://qwen3-6-27b-benchmark.vercel.app/). For local 16 GB VRAM use, they prefer **IQ4_XS** , reporting about `pp 100 tps` / `tg 8 tps` on vanilla `llama.cpp`, improved to roughly `pp 760 tps` / `tg 22 tps` using **TheTom's TurboQuant** fork with `-ngl 99`, `turbo4/turbo2` KV-cache quantization, and context limited below ~`75k`.** The main technical caveat raised in comments is that the evaluation appears to be **single-run** , so stochastic variance could make individual quantization results outliers; commenters still noted that the observed degradation trend broadly matches expectations.

    * Several commenters questioned whether the quantization comparison used **single-run evaluations or repeated trials** , noting that LLM outputs can vary enough that _“one run is not enough”_ and may produce misleading conclusions from statistical noise or outlier generations. They still observed an apparent expected trend of **quality degradation as quantization becomes more aggressive** , but wanted multiple samples per quant level to support the findings.
    * One technically substantive takeaway was that **4-bit quantization appears to remain the practical sweet spot** , with **3-bit quants still described as usable** despite common skepticism. A commenter argued that above roughly **5-bit** , users may often gain more by moving to a larger/better model rather than preserving extra precision on a smaller one, citing comparisons like `122B UD-Q3_K_XL` versus `35B IQ4_NL`.
  * **[Qwen3.6 27B uncensored heretic v2 Native MTP Preserved is Out Now With KLD 0.0021, 6/100 Refusals and the Full 15 MTPs Preserved and Retained, Available in Safetensors, GGUFs and NVFP4s formats.](https://www.reddit.com/r/LocalLLaMA/comments/1t5yajb/qwen36_27b_uncensored_heretic_v2_native_mtp/)** (Activity: 530): ****llmfan46** released **Qwen3.6-27B-uncensored-heretic-v2-Native-MTP-Preserved** on Hugging Face, claiming `KLD = 0.0021`, `6/100` refusals, and preservation/retention of the full `15` native MTP heads across [Safetensors](https://huggingface.co/llmfan46/Qwen3.6-27B-uncensored-heretic-v2-Native-MTP-Preserved), [GGUF](https://huggingface.co/llmfan46/Qwen3.6-27B-uncensored-heretic-v2-Native-MTP-Preserved-GGUF), [NVFP4](https://huggingface.co/llmfan46/Qwen3.6-27B-uncensored-heretic-v2-Native-MTP-Preserved-NVFP4), [NVFP4-GGUF](https://huggingface.co/llmfan46/Qwen3.6-27B-uncensored-heretic-v2-Native-MTP-Preserved-NVFP4-GGUF), [NVFP4-MLP-only](https://huggingface.co/llmfan46/Qwen3.6-27B-uncensored-heretic-v2-Native-MTP-Preserved-NVFP4-MLP-Only), and [GPTQ-Int4](https://huggingface.co/llmfan46/Qwen3.6-27B-uncensored-heretic-v2-Native-MTP-Preserved-GPTQ-Int4) variants. The post says the release includes benchmarks and that all variants were checked for full MTP retention; the author’s full model list is [here](https://huggingface.co/llmfan46/models).** Commenters requested additional deployment-oriented quantization support, especially `Q4_K_XS` for `16GB` systems, and asked whether MTP works with TurboQuant-compressed KV cache or could be applied to Gemma 4 dense models. One technical concern was that if the MTP draft heads were trained on the original refusal-aligned model while only the base was fine-tuned, MTP acceptance may degrade or _“fight the heretic”_ specifically on newly unlocked refusal/tail-behavior cases despite the low aggregate `KLD = 0.0021`.

    * A key concern was whether preserving the full `15` MTP heads is actually beneficial after an uncensoring/heretic fine-tune: if the draft heads retain the original refusal distribution while the base model was modified, speculative decoding may “fight” the newly unlocked outputs. One commenter noted that the reported **KLD`0.0021`** indicates the base stayed close overall, but may not capture _tail behavior_ on refusal/unlocked prompts, making **MTP acceptance rate on heretic cases** the more important validation metric.
    * Users asked for deployment-specific quantization details, including a **`Q4_K_XS` GGUF** target to fit `16GB` VRAM while retaining useful context, and whether preserved MTP remains compatible with **TurboQuant-compressed KV cache**. Another hardware-focused question flagged that **NVFP4 + MTP on Blackwell** may currently be blocked by CUDA/tooling support, with the commenter saying the stack appears “dead in the water until a new CUDA version is released.”
    * There were implementation questions around multimodal packaging and stability: commenters noted the inclusion of `mmproj` files and asked whether crashes related to **PR`#22673`** are still present. Another asked whether the same MTP-preservation approach could apply to a future **Gemma 4 dense** model, implying interest in portability of native MTP heads across architectures/fine-tunes.



## Less Technical AI Subreddit Recap

> /r/Singularity, /r/Oobabooga, /r/MachineLearning, /r/OpenAI, /r/ClaudeAI, /r/StableDiffusion, /r/ChatGPT, /r/ChatGPTCoding, /r/aivideo, /r/aivideo

### 1. Claude Limits Raised via SpaceX Compute

  * **[Doubled Rate Limits for Claude Code](https://www.reddit.com/r/ClaudeCode/comments/1t5hs98/doubled_rate_limits_for_claude_code/)** (Activity: 3901): ****Anthropic** says a new compute-capacity partnership with **SpaceX** , plus other recent compute deals, enabled higher usage limits across **Claude Code** and the **Claude API** ([announcement](https://www.anthropic.com/news/higher-limits-spacex)). Effective immediately, **Claude Code Pro/Max** no longer has the prior _peak-hours limit reduction_ , and **Opus-model API rate limits** are being “substantially” raised.** Top comments were mostly non-technical reactions: surprise/skepticism about whether the announcement is real, plus speculation that the SpaceX/Anthropic tie-up reflects Elon Musk’s rivalry with Sam Altman.

  * **[SpaceX Conpute Deal - Double Limits](https://www.reddit.com/r/ClaudeAI/comments/1t5htq1/spacex_conpute_deal_double_limits/)** (Activity: 1931): ****Anthropic announced a compute partnership with SpaceX** to “substantially increase” capacity, alongside other compute deals, and is immediately changing limits: removing **peak-hours limit reductions** for **Claude Code Pro/Max** and **substantially raising API rate limits for Opus models** ([Anthropic announcement](https://www.anthropic.com/news/higher-limits-spacex)). The post does not specify exact new rate-limit numbers or the nature of the SpaceX compute arrangement.** Comments are skeptical that higher limits will materially improve usable capacity, with one noting users may simply hit weekly caps faster and another comparing Claude unfavorably to OpenAI Codex usage economics. There’s also concern that any improvement may be temporary and regress within weeks or months.

    * Several commenters argue that a raw compute-capacity deal would not materially improve **Claude Chat** unless Anthropic also changes product-level throttles: _“A usage limit increase that doesn't change the weekly limit is practically useless.”_ The key technical/product distinction raised is between backend compute availability and enforced per-user weekly quota policy.
    * One comparison frames Anthropic’s quota pressure against **OpenAI Codex** pricing/usage: a user claims _“$20 on codex gets you infinitely more usage than Claude,”_ suggesting Anthropic may be reacting to user churn caused by stricter effective compute limits. The discussion implies that any short-term limit relaxation may be temporary if demand again saturates available capacity.



### 2. AI Lab Corporate Governance Drama

  * **[Sam Altman texts Mira Murati. November 19, 2023. [This document is from Musk v. Altman (2026).]](https://www.reddit.com/r/OpenAI/comments/1t5tn1n/sam_altman_texts_mira_murati_november_19_2023/)** (Activity: 5431): **The post references an image/document titled**“Sam Altman texts Mira Murati. November 19, 2023”** , allegedly from **Musk v. Altman (2026)** , but the linked Reddit gallery was inaccessible due to **403 Forbidden** , so the actual text-message contents could not be verified or summarized. No technical claims, model details, benchmarks, implementation facts, or litigation-document substance were available from the provided post metadata.**

  * **[xAI will be dissolved as a separate entity.](https://www.reddit.com/r/singularity/comments/1t5q5jm/xai_will_be_dissolved_as_a_separate_entity/)** (Activity: 2116): **The image is a**non-technical screenshot of an X.com post** attributed to **Elon Musk** , claiming that **xAI would be dissolved as a separate company** and folded into “**SpaceXAI** ,” described as AI products from SpaceX: [image](https://i.redd.it/tzexewkj2lzg1.jpeg). No implementation details, model changes, infrastructure plans, or product roadmap are provided in the post/title, so the significance is primarily **corporate-structure/contextual** , not technical.** Comments frame the move as consistent with Musk’s prior desire to combine AI work with his other companies, while skeptics characterize it as potentially moving unprofitable AI efforts into SpaceX, a profitable/government-contract-supported entity.




# AI Discords

Unfortunately, Discord shut down our access today. We will not bring it back in this form but we will be shipping the new AINews soon. Thanks for reading to here, it was a good run.

---

## [Anthropic-SpaceXai's 300MW/$5B/yr deal for Colossus I, ARR growth is 8000% annualized](https://news.smol.ai/issues/26-05-06-anthropic-xai/)
*🌐 Smol AI News | 2026-05-06*

**a quiet day.**

> AI News for 5/5/2026-5/6/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

It was Anthropic’s second annual developer event today, and the vibes were immaculate. No big model release, which some (miscalibrated) people were hoping for, but it was mostly the SpaceX partnership announcement (on track to challenge Claude’s biggest launch of all time), 3 new features for Claude Managed Agents, and a recap/reintroduction/celebration of all that has been shipped in the past 6 months:

opening keynote After Elon signed off on it, possibly strategically just as his lawsuit against OpenAI is in trial, Anthropic is taking over all of Colossus 1 with surprising speed (“in the next few days”) which some estimate to be a roughly $5B/year deal, making xAI a neocloud:

The other big draw was the moderated session with the Amodei siblings, announcing the 80x growth and some commentary on US and Chinese competitors:

The trends Dario is watching:

Tiny Teams: He still thinks 2026 is the year we see a one person billion dollar company. “There is an enormous ability for one person or a tiny set of people to do a set of things that are incredible… Before, if you had an idea or vision there are so many resources you’d have to accumulate for several years in order to make that vision happen, and I think there’s a unique opportunity for single individuals or very tiny teams to do things that are incredible, where we move from the models are writing code, to the models are helping us think of software engineering as a task, to the models are helping us think of how can I build a business or economic unit as a task”.

Multiagents: “starting with a team of smart people in a room and working our way up to a ‘country of geniuses in a datacenter’”

Enterprise Services: “Claude Code helps individuals to be more productive, but we’re increasingly going to help whole teams and organizations be more productive and more than the sum of its parts”.

Bottlenecks: Claude is of course speeding up Claude, but he thinks about Amdahl’s Law - Security, Verifiability - finding the bottlenecks in software engineering and removing them/speeding up the overall process.

The rest of the mainstage sessions included:

Must know Claude Code updates:

More Outcomes content on the Inner vs the Outer Loop…

… for automatic improvement of agents:

* * *

# AI Twitter Recap

**Top Story: Anthropic and Claude announcements/commentary**

## What happened

**Anthropic had a dense news cycle centered on compute, Claude Code limits, and agent platform direction.** Officially, Anthropic announced a new compute partnership with SpaceX that will “substantially increase” capacity and immediately translate into higher limits for Claude products: [@claudeai](https://x.com/claudeai/status/2052060691893227611) said the deal boosts compute enough to raise usage limits, followed by specifics from [@claudeai](https://x.com/claudeai/status/2052060693269008586): **Claude Code’s 5-hour rate limits are doubled for Pro, Max, Team, and seat-based Enterprise; peak-hours limit reductions are removed for Pro and Max; Opus API rate limits are substantially increased**. xAI framed the deal as Anthropic getting access to **Colossus 1** via SpaceXAI for “additional capacity for Claude” [@xai](https://x.com/xai/status/2052060350770515978), while Anthropic CTO Tom Brown added that **Claude inference would be ramped up on Colossus “in the next few days”** [@nottombrown](https://x.com/nottombrown/status/2052062566126649448). The company also ran its **“Code with Claude”** event, with a livestreamed keynote and sessions on Claude Code, GitHub-scale usage, and managed agents [@ClaudeDevs](https://x.com/ClaudeDevs/status/2052055459272761661), prompting substantial real-time commentary from developers and observers [@simonw](https://x.com/simonw/status/2052055655230706032), [@latentspacepod](https://x.com/latentspacepod/status/2052062150332710942). Around this, discourse branched into four themes: **(1) compute bottlenecks were more severe than many assumed, reportedly due to unexpected usage growth; (2) users welcomed the 5-hour limit increase but questioned unchanged weekly limits; (3) people debated whether Anthropic’s new managed-agent features like memory/“Dreaming” and rubrics/“Outcomes” are real product differentiation or commoditizable harness features; and (4) Anthropic’s safety/governance positioning continued to attract both praise and criticism** , including claims from critics that some Anthropic employees project “only we can be trusted with AGI,” and counterclaims from Anthropic-adjacent voices that the more common internal view is closer to “no one can be trusted with AGI” than “only us” [@_aidan_clark_](https://x.com/_aidan_clark_/status/2052089187659346047), [@kipperrii](https://x.com/kipperrii/status/2052094851991392536).

## Official facts and confirmed details

  * Anthropic announced a **SpaceX compute partnership** to increase capacity [@claudeai](https://x.com/claudeai/status/2052060691893227611).
  * Effective immediately, Anthropic says it is: 
    1. **Doubling Claude Code’s 5-hour rate limits** for Pro, Max, Team, and seat-based Enterprise
    2. **Removing peak-hours limit reduction** on Claude Code for Pro and Max
    3. **Substantially increasing API rate limits for Opus models**  
Source: [@claudeai](https://x.com/claudeai/status/2052060693269008586)
  * Anthropic linked an official explainer on the higher usage limits and the SpaceX compute deal [@claudeai](https://x.com/claudeai/status/2052060696255283346).
  * xAI’s announcement described the arrangement as **SpaceXAI providing Anthropic access to Colossus 1** for additional Claude capacity [@xai](https://x.com/xai/status/2052060350770515978).
  * Anthropic CTO Tom Brown said **Claude inference would start ramping on Colossus within days** [@nottombrown](https://x.com/nottombrown/status/2052062566126649448).
  * Anthropic product/eng lead Amol Avasare clarified that **weekly limits were not increased yet** because only a **small percentage** of users hit weekly limits, while a much larger percentage hit 5-hour limits; more changes may come as compute lands [@TheAmolAvasare](https://x.com/TheAmolAvasare/status/2052064611692904639), [@TheAmolAvasare](https://x.com/TheAmolAvasare/status/2052066157176426653).
  * Anthropic/Claude held a **Code with Claude** event with sessions including keynote, Claude Code updates, GitHub-scale usage, and managed agents [@ClaudeDevs](https://x.com/ClaudeDevs/status/2052055459272761661).
  * Anthropic’s Alex Albert promoted the event and later summarized the announcement as **“More chips, more Claude”** [@alexalbert__](https://x.com/alexalbert__/status/2052067009605861764), [@alexalbert__](https://x.com/alexalbert__/status/2052065953173872912).
  * The dedicated Claude Code account reiterated the limit increase for Pro/Max/Team [@claude_code](https://x.com/claude_code/status/2052071730190123094).



## Compute details and scale claims

Several tweets added quantitative claims about the scale of the SpaceX/xAI arrangement. These are **not from Anthropic’s main announcement tweets** , but they were widely circulated:

  * [@_arohan_](https://x.com/_arohan_/status/2052065871552819647) cited **“more than 300 megawatts of new capacity” and “over 220,000 NVIDIA GPUs within the month.”**
  * [@scaling01](https://x.com/scaling01/status/2052068218047545501) claimed Colossus 1 includes **~150,000 H100s, 50,000 H200s, and 30,000 GB200s**.
  * [@Yuchenj_UW](https://x.com/Yuchenj_UW/status/2052065017072386450) repeated the **220,000 GPU** figure and added an unverified claim that Anthropic had committed **$200B on Google TPUs**.
  * [@eliebakouch](https://x.com/eliebakouch/status/2052066609896808473) interpreted the deal as Anthropic getting effectively **all of Colossus 1 capacity** , not just idle GPUs.
  * Elon Musk later said SpaceXAI was comfortable leasing Colossus 1 because **xAI had already moved training to Colossus 2** [@elonmusk](https://x.com/elonmusk/status/2052069691372478511), and [@eliebakouch](https://x.com/eliebakouch/status/2052068426152132722) claimed Colossus 2 is already at **~500k Blackwells**.



These numbers are best treated as **partly official-adjacent but not fully canonized in Anthropic’s own announcement thread**. The broad factual takeaway is stronger than the exact inventory breakdown: **Anthropic secured a very large, near-term external inference capacity expansion.**

## Evidence the bottleneck was real

A recurring interpretation was that Anthropic’s constraint had genuinely been compute, not merely pricing or product design.

  * [@kimmonismus](https://x.com/kimmonismus/status/2052059082886910251) asked during/after the livestream whether Anthropic was **doubling Claude Code rate limits at no extra charge**.
  * [@kimmonismus](https://x.com/kimmonismus/status/2052118418174681572) later summarized remarks from a Dario/Daniela interview: **usage grew ~80x unexpectedly** , which purportedly caused the compute shortage, and the SpaceX deal is the first major attempt to address it.
  * [@czajkadev](https://x.com/czajkadev/status/2052101699188248990) explicitly interpreted the update as proof that **compute was the bottleneck**.
  * [@theo](https://x.com/theo/status/2052114791045668894) separately argued the industry problems are “not just money, it’s about compute,” which fits the Anthropic story even though it’s a broader point.
  * [@scaling01](https://x.com/scaling01/status/2052069341609226550) generalized from this deal to a macro thesis: **frontier labs are compute constrained enough to rent datacenters from competitors.**



This is one of the strongest factual/market signals in the dataset: **Anthropic’s user-facing rate limits moved materially only after a major compute deal.**

## Product implications: Claude Code, API, and managed agents

Anthropic’s practical user impact is clear:

  * **Claude Code power users get more usable burst capacity** over a 5-hour window.
  * **Peak-time throttling is eased** for Pro/Max.
  * **Opus API users get higher rate limits** , which matters for agent workloads and production integrations.



The event also highlighted Anthropic’s broader platform ambitions around agents. While the primary official tweets here are mostly about the event itself, commentary points to features such as:

  * **Dreaming** = memory / cross-session context
  * **Outcomes** = rubrics / grading / objective tracking
  * agent orchestration / managed agents direction



Commentary:

  * [@RichNwan](https://x.com/RichNwan/status/2052085746526216601) argued Anthropic is “building out their managed agents platform” with **Dreaming** and **Outcomes** , but questioned whether these are meaningfully differentiated versus open harnesses.
  * [@eliebakouch](https://x.com/eliebakouch/status/2052156107313807690) saw these as **important for power users** , especially for preserving the main agent’s context window and using separate graders to manage quality/safety/reward hacking.
  * [@latentspacepod](https://x.com/latentspacepod/status/2052068066167816369) quoted Anthropic speakers emphasizing **verification** , “routines are higher-order prompts,” and the idea that the remaining gap is often **deployment/operationalization** , not raw capability.



That last point aligns Anthropic with the broader shift from “one-shot chatbot” to **structured agent systems with memory, decomposition, grading, and verification**.

## Facts vs opinions

### Factual claims with strongest support

  * Anthropic has a new **SpaceX compute partnership** and increased Claude Code/API limits immediately [@claudeai](https://x.com/claudeai/status/2052060691893227611), [@claudeai](https://x.com/claudeai/status/2052060693269008586).
  * Weekly limits were **not** doubled yet; Anthropic staff said that was intentional based on who hits which caps [@TheAmolAvasare](https://x.com/TheAmolAvasare/status/2052064611692904639).
  * Anthropic intends to run **Claude inference on Colossus** in the near term [@nottombrown](https://x.com/nottombrown/status/2052062566126649448).
  * Anthropic ran a **Code with Claude** event focused on coding, production deployment, and managed agents [@ClaudeDevs](https://x.com/ClaudeDevs/status/2052055459272761661).



### Plausible but less directly verified claims

  * Anthropic is gaining access to **>300 MW / >220,000 NVIDIA GPUs** in short order [@_arohan_](https://x.com/_arohan_/status/2052065871552819647).
  * Colossus 1 inventory breakdown includes **H100/H200/GB200 mixes** [@scaling01](https://x.com/scaling01/status/2052068218047545501).
  * Anthropic’s demand spike was around **80x growth** and caught leadership off guard [@kimmonismus](https://x.com/kimmonismus/status/2052118418174681572).



### Opinions and interpretations

  * Anthropic **waited too long** to address compute shortages and lost significant growth to OpenAI/Codex: [@scaling01](https://x.com/scaling01/status/2052070594972090409).
  * This deal proves **compute is not a durable moat** , because top labs can rent capacity from whichever hyperscaler/cluster operator will supply it: [@Dorialexander](https://x.com/Dorialexander/status/2052067579594707149).
  * Alternatively, this proves the opposite in practical terms: **whoever controls deployed compute shapes who can satisfy demand**.
  * Anthropic’s platform features are **not very differentiated** because open harnesses can replicate them: [@RichNwan](https://x.com/RichNwan/status/2052085746526216601).
  * Or they **are differentiated enough** because first-party integration can tightly couple model behavior, memory, evaluators, and product experience.
  * Anthropic’s culture is unusually safety-focused and “good for humanity”: Elon Musk said after meeting senior Anthropic staff he was impressed and “no one set off my evil detector” [@elonmusk](https://x.com/elonmusk/status/2052069691372478511).
  * Conversely, critics continue to frame Anthropic as overly paternalistic or exclusivist about AGI governance [@_aidan_clark_](https://x.com/_aidan_clark_/status/2052089187659346047).



## Different opinions in the discourse

### 1) Positive / supportive

A large set of replies treated this as a win for users and evidence Anthropic is responding aggressively.

  * [@alexalbert__](https://x.com/alexalbert__/status/2052065953173872912): “More chips, more Claude.”
  * [@_sholtodouglas](https://x.com/_sholtodouglas/status/2052062164467224971): “More compute -> straight to you.”
  * [@kimmonismus](https://x.com/kimmonismus/status/2052059448261177367) highlighted doubled limits and raised Opus API caps.
  * [@TheRundownAI](https://x.com/TheRundownAI/status/2052064469371470218) summarized it as a straightforward user benefit.
  * [@DannyLimanseta](https://x.com/DannyLimanseta/status/2052078750893056420) liked the cross-company cooperation and hoped Anthropic’s caution might be balanced by SpaceXAI’s optimism.
  * [@AmandaAskell](https://x.com/AmandaAskell/status/2052161052058833181) reacted positively to the announcement’s symbolism.



### 2) Mixed / pragmatic

These takes welcomed the change but focused on operational details and remaining limitations.

  * [@btibor91](https://x.com/btibor91/status/2052067002412335435) and [@kimmonismus](https://x.com/kimmonismus/status/2052061694080188720) immediately noted the likely caveat: **weekly caps unchanged**.
  * [@TheAmolAvasare](https://x.com/TheAmolAvasare/status/2052064611692904639) answered this directly.
  * [@sbmaruf](https://x.com/sbmaruf/status/2052119971820658771) reported still seeing rate limits after the change, implying rollout and reliability tuning were ongoing.
  * [@zachtratar](https://x.com/zachtratar/status/2052161984968396819) asked for patience during staged rollout.



### 3) Competitive / strategic critique

A different cluster viewed the announcement through the OpenAI-vs-Anthropic product war.

  * [@scaling01](https://x.com/scaling01/status/2052070594972090409) argued Anthropic **blundered its growth advantage by waiting too long** , possibly conceding billions in ARR to OpenAI.
  * [@Yuchenj_UW](https://x.com/Yuchenj_UW/status/2052065017072386450) read the move as Dario getting aggressive because of **OpenAI Codex’s growth**.
  * [@_arohan_](https://x.com/_arohan_/status/2052053181656641735) joked that “Big tech has become a claude wrapper,” pointing to Claude’s developer mindshare.
  * [@dejavucoder](https://x.com/dejavucoder/status/2052051193376231845) saying “claude is down, saint tibo please reset codex limits” captured the practical reality of multi-homing among coding tools when one service is capacity constrained.



### 4) Governance / safety / culture critique

This is the deepest philosophical disagreement.

  * [@_aidan_clark_](https://x.com/_aidan_clark_/status/2052089187659346047) criticized what he says he repeatedly hears from Anthropic colleagues: a belief they alone should be trusted to build AI.
  * [@kipperrii](https://x.com/kipperrii/status/2052094851991392536) partially agreed the “only we can be trusted” framing would be bad, but argued the real majority view is closer to **“no one can be trusted with AGI”** while still personally trusting Anthropic more than others.
  * [@elonmusk](https://x.com/elonmusk/status/2052069691372478511) offered a surprising endorsement after meeting Anthropic leaders.
  * [@Yuchenj_UW](https://x.com/Yuchenj_UW/status/2052080339364004317) called this reversal ironic given prior criticism of Anthropic.
  * [@teortaxesTex](https://x.com/teortaxesTex/status/2052080900280557749) mocked the rapid détente between Musk/xAI and Anthropic.
  * [@teortaxesTex](https://x.com/teortaxesTex/status/2052045988936683674) also argued it is inconsistent to warn others about AI risk while building powerful closed systems such as “Mythos.”
  * [@goodside](https://x.com/goodside/status/2052077014346064372), while not directly about Anthropic governance, contributed to the broader moral/AI norms debate that often clusters around Anthropic.



## Commentary on Claude model performance and comparisons

Though no major new Claude model appears in these tweets, Claude remained a reference point in product and eval discourse.

  * [@giffmana](https://x.com/giffmana/status/2051925008457273527) compared “Opus 4.6,” ChatGPT Pro, and Muse Spark on a mathematical disagreement. His take: 
    * **Opus 4.6** confidently defended a wrong proof (“gaslit”)
    * **ChatGPT Pro** reconciled the formulas correctly but without interpretation
    * **Muse Spark** did both well  
This is anecdotal, but it’s one of the more concrete comparative qualitative model reports in the set.
  * [@kimmonismus](https://x.com/kimmonismus/status/2052040471829004627) summarized a Substack analysis claiming **GPT-5.5 is basically tied with Claude Mythos Preview on cyber** , perhaps more cost-efficient, while Mythos is only slightly ahead on some general benchmarks and SWE-bench Pro; he questioned why Mythos remains secretive.
  * [@AssemblyAI](https://x.com/AssemblyAI/status/2052043337751056733) noted support for **structured JSON from Claude 4.5+ models** in its gateway.
  * [@OpenRouter/TencentHunyuan](https://x.com/TencentHunyuan/status/2051978552900538403) listed **Claude Code** among major apps driving Hy3 usage, showing Claude’s importance in the coding-tool ecosystem even when third-party models are used behind the scenes.



These comments don’t establish hard model ranking, but they do show Claude is still a primary benchmark in coding-agent workflows and that advanced users increasingly compare **model + harness + limits + reliability** , not just base intelligence.

## Claude Code and harness engineering context

A notable background thread across the dataset is that many engineers now think **agent performance is heavily dependent on the harness** —system prompts, tools, middleware, decomposition strategies, and model-specific tuning.

Relevant non-Anthropic commentary:

  * [@masondrxy](https://x.com/masondrxy/status/2052054177749029164): same model, same task, very different scores depending on prompts/tools/middleware; **10–20 point jumps on tau2-bench**.
  * [@LangChain](https://x.com/LangChain/status/2052054711440662864): harness profiles for OpenAI, Anthropic, and Google models.
  * [@jakebroekhuizen](https://x.com/jakebroekhuizen/status/2052058987580051566): distinguishes **temporal harness evolution** as models improve from **lateral tuning across model families**.
  * [@Vtrivedy10](https://x.com/Vtrivedy10/status/2052100726608781363): argues a tailored harness can outperform default Codex/Claude Code on many tasks; usable context windows are still effectively **50–100k** for many agent designs.
  * [@kieranklaassen](https://x.com/kieranklaassen/status/2052092428438688027): “If you cannot get your work done [in] the Claude CLI, Claude will not be able to work for you.”



This matters because some of Anthropic’s platform moves—memory, grading, managed agents—can be read as **Anthropic productizing parts of the harness**. That helps explain the central debate: **are these defensible platform primitives, or just first-party packaging of patterns that open frameworks can clone?**

## Broader context: why this matters

  1. **Inference, not just training, is now a frontier bottleneck.**  
The news was not a new model launch; it was a capacity launch. That is increasingly common at the frontier.

  2. **Compute markets are becoming fluid and strategic.**  
Anthropic partnering with SpaceX/xAI infrastructure undercuts simplistic narratives that each frontier lab sits only atop its own vertically integrated stack.

  3. **Developer product share is sensitive to reliability and limits.**  
Claude appears to have strong developer affinity, but rate limits and outages push users toward Codex/Cursor/others quickly.

  4. **The battleground is shifting from base models to agent systems.**  
“Code with Claude,” managed agents, Dreaming, Outcomes, and the surrounding discourse all point toward the next layer of competition being **memory, orchestration, evals, and workflow integration**.

  5. **Anthropic’s brand remains bifurcated.**  
It is simultaneously:

     * admired for product quality and safety seriousness,
     * criticized for paternalism or perceived exclusivism,
     * and now seen as more commercially aggressive on compute than before.



## Bottom line

Anthropic’s news was less about a flashy new model and more about a structural reality: **Claude demand had outrun available compute, and Anthropic responded by striking a major external infrastructure deal and immediately easing key user limits** [@claudeai](https://x.com/claudeai/status/2052060691893227611), [@claudeai](https://x.com/claudeai/status/2052060693269008586). The most important technical/economic signal is that **capacity, rate limits, and agent-product ergonomics are now as strategically important as leaderboard deltas**. The main open questions are whether Anthropic can convert this capacity into sustained product momentum, whether its managed-agent features are truly differentiated, and whether its safety/governance posture helps or hinders its standing as competition with OpenAI, Google, xAI, and open-model ecosystems intensifies.

**Infrastructure, inference, and systems**

  * OpenAI and partners released **MRC (Multipath Reliable Connection)** , an open networking protocol for large AI training clusters, already deployed on OpenAI’s biggest supercomputers [@OpenAI](https://x.com/OpenAI/status/2052025532485902368), [@OpenAI](https://x.com/OpenAI/status/2052025533937103102). Commentary emphasized multipath routing, microsecond failover, and the shift of networking into a primary frontier bottleneck [@kimmonismus](https://x.com/kimmonismus/status/2052011784023028060), [@gdb](https://x.com/gdb/status/2052059553542328829).
  * Perplexity said it built an in-house inference engine, **ROSE** , covering models from embeddings to trillion-parameter LLMs, and uses **CuTeDSL** to accelerate specialized kernel development on Hopper and Blackwell [@perplexity_ai](https://x.com/perplexity_ai/status/2052041903970148647).
  * vLLM + Mooncake presented a strong systems result for agentic workloads with reusable prefixes: **3.8x throughput** , **46x lower P50 TTFT** , **8.6x lower end-to-end latency** , and cache-hit improvement from **1.7% to 92.2%** , scaling to **60 GB200 GPUs** [@vllm_project](https://x.com/vllm_project/status/2052113331927060840).
  * Unsloth + NVIDIA published three training optimizations claimed to make home-GPU LLM training **~25% faster** : packed-sequence metadata caching, double-buffered checkpoint reloads, and faster MoE routing [@UnslothAI](https://x.com/UnslothAI/status/2052020656527532276).
  * NVIDIA work on **lossless speculative decoding inside RL** was highlighted as giving up to **~2.5x faster end-to-end RL at 235B scale** and **~1.8x faster rollout throughput at 8B** without changing policy distribution [@TheTuringPost](https://x.com/TheTuringPost/status/2052180472206381268).
  * Baseten launched **Frontier Gateway** as managed infra/API/auth/rate-limit/billing for closed-weight labs; Poolside reported going from kickoff to production in **7 weeks** , with **P50 TTFT 146ms** for Laguna XS.2 and **605ms** for Laguna M.1 [@tuhinone](https://x.com/tuhinone/status/2052082677432390130), [@poolsideai](https://x.com/poolsideai/status/2052075055132057707).



**Benchmarks, evals, and agent harnesses**

  * **ProgramBench** asks whether language models can rebuild programs from scratch, extending beyond repair-style SWE tasks [@ComputerPapers](https://x.com/ComputerPapers/status/2051895799043215415), with Ofir Press arguing benchmarks are “treasure maps” that specify the future we want [@OfirPress](https://x.com/OfirPress/status/2052106927908200957).
  * **Terminal-Bench 2.1** patched **28/89 tasks** in TB2.0; rankings held but absolute scores moved by up to **12 points** , a useful reminder that agent benchmark maintenance materially matters [@terminalbench](https://x.com/terminalbench/status/2052119174500220964), [@ekellbuch](https://x.com/ekellbuch/status/2052165464655298866).
  * **OBLIQ-Bench** emerged as a major IR benchmark release focused on hard first-stage retrieval, where current retrievers fail to surface subtly relevant documents from large corpora [@dianetc_](https://x.com/dianetc_/status/2052053806121140254), with strong endorsements from IR researchers [@lateinteraction](https://x.com/lateinteraction/status/2052055143038713875), [@nlp_mit](https://x.com/nlp_mit/status/2052069072607547892), [@LightOnIO](https://x.com/LightOnIO/status/2052095548098822477).
  * Harvey launched **LAB** , an open-source, long-horizon legal agent benchmark covering **1,200 tasks across 24 practice areas** , with support/commentary from LangChain, Baseten, Artificial Analysis, and others [@saranormous](https://x.com/saranormous/status/2052061665596948894), [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2052145762650431840).
  * A major theme across multiple tweets was that **harness engineering is a first-class variable** , often worth **10–20 points** on agent benchmarks even with the same base model [@masondrxy](https://x.com/masondrxy/status/2052054177749029164), [@LangChain](https://x.com/LangChain/status/2052054711440662864), [@Vtrivedy10](https://x.com/Vtrivedy10/status/2052100726608781363).



**Model releases and model performance**

  * Zyphra released **ZAYA1-8B** , a reasoning MoE with **< 1B active parameters**, open-weight under **Apache 2.0** , claiming strong math/reasoning efficiency and proximity to much larger systems with test-time compute [@ZyphraAI](https://x.com/ZyphraAI/status/2052103618145501459), [@ZyphraAI](https://x.com/ZyphraAI/status/2052103646712828119). Commentary praised its architecture/post-training stack and AMD partnership [@teortaxesTex](https://x.com/teortaxesTex/status/2052106600882528326), [@eliebakouch](https://x.com/eliebakouch/status/2052126118891729148).
  * Google’s **Gemma 4** moved the open-model Pareto frontier in Code Arena: **Gemma-4-31B #13** , **Gemma-4-26B-A4B #17** among open models [@arena](https://x.com/arena/status/2052061349312921686), [@_philschmid](https://x.com/_philschmid/status/2052104144706588699).
  * Google’s **DFlash draft model for Gemma-4** was described as one of the best draft models they’ve trained, especially strong in coding and math [@jianchen1799](https://x.com/jianchen1799/status/2051902953376923946).
  * Qwopus3.6-35B-A3B-v1 claimed **162 tok/s on a single RTX 5090** , targeting strong one-shot frontend/web generation on consumer hardware [@KyleHessling1](https://x.com/KyleHessling1/status/2052064943999267212).
  * DeepSeek commentary was mixed: fundraising talks reportedly target a **$45B valuation** led by a major Chinese state-backed semiconductor fund [@jukan05](https://x.com/jukan05/status/2051904572038455634), while evaluators debated weak WeirdML performance for V4-Pro versus GLM/Kimi/open competitors [@htihle](https://x.com/htihle/status/2052042076196335658), [@teortaxesTex](https://x.com/teortaxesTex/status/2052043753892761882).



**Agents, tools, and developer workflows**

  * Cursor added **context usage breakdowns** across rules, skills, MCPs, and subagents to help debug context issues [@cursor_ai](https://x.com/cursor_ai/status/2052059748544249918), and described bootstrapping future Composer generations with earlier Composer models [@cursor_ai](https://x.com/cursor_ai/status/2052116064474161556).
  * Cognition shipped **Devin Review** and **Quick Review / SWE-Check** in Windsurf 2.0, explicitly targeting the new bottleneck of reviewing AI-generated code [@cognition](https://x.com/cognition/status/2052100630626607189), [@ypatil125](https://x.com/ypatil125/status/2052122827961278833).
  * OpenAI promoted **Codex subagents** , framing them as a way to split work across specialized agents and merge results back into one answer [@reach_vb](https://x.com/reach_vb/status/2052090279344120278).
  * Nous/Hermes continued to push a highly pluggable local agent stack: plugin expansion, community docs, Windows/WSL2 setup guidance, and use-case aggregation [@Teknium](https://x.com/Teknium/status/2052046335583625629), [@witcheer](https://x.com/witcheer/status/2052033039379673374), [@NousResearch](https://x.com/NousResearch/status/2052140057222369541).
  * Perplexity added **Finance Search** to its Agent API with licensed data, live market data, and citations, claiming best cohort accuracy and lowest cost per correct answer on **FinSearchComp T1** [@perplexity_ai](https://x.com/perplexity_ai/status/2052028012313649194), [@AravSrinivas](https://x.com/AravSrinivas/status/2052033959555735752).
  * Google’s Gemini API added **multimodal retrieval** to File Search using `gemini-embedding-2` for PDFs and images in a single retrieval pipeline [@_philschmid](https://x.com/_philschmid/status/2052060912425546050).



**Robotics, multimodality, and research notes**

  * Genesis AI introduced **GENE-26.5** , describing a full-stack robotics program with a robotics-native foundation model, human-like hand, data glove, and simulator; the model is trained across **language, vision, proprioception, tactile, and action** [@gs_ai_](https://x.com/gs_ai_/status/2052050956272230577), [@theo_gervet](https://x.com/theo_gervet/status/2052057035681018359).
  * Meta FAIR released **NeuralBench** , an MIT-licensed unified benchmark framework for NeuroAI with **36 EEG tasks** and **94 datasets** , with MEG/fMRI support planned [@hubertjbanville](https://x.com/hubertjbanville/status/2052029372282888234), [@JeanRemiKing](https://x.com/JeanRemiKing/status/2052034314120896582).
  * Sander Dieleman published a long technical post on **flow maps** , learning the integral of a diffusion model for faster sampling and related tricks [@sedielem](https://x.com/sedielem/status/2051957402556104799).
  * François Fleuret sketched a speculative recipe for stronger systems: **latent diffusion-like reasoning + real recurrent state + world-model pre-pretraining** [@francoisfleuret](https://x.com/francoisfleuret/status/2051928896027693479), generating useful discussion on whether diffusion-style reasoning extrapolates the right way [@willdepue](https://x.com/willdepue/status/2052033422915477580), [@jeremyphoward](https://x.com/jeremyphoward/status/2052149483740545400).
  * HeadVis was introduced as a new interpretability tool for studying attention heads [@kamath_harish](https://x.com/kamath_harish/status/2052046203030827088).
  * Microsoft Research work on **agent-readable interpretability** proposed “Agentic-imodels,” where coding agents evolve models that are interpretable to other LLMs; reported gains on **65 tabular datasets** and downstream BLADE improvements from **8% to 73%** [@dair_ai](https://x.com/dair_ai/status/2052125514266190286).



* * *

# AI Reddit Recap

## /r/LocalLlama + /r/localLLM Recap

### 1. MTP and Quantized Local Inference

  * **[Gemma 4 MTP released](https://www.reddit.com/r/LocalLLaMA/comments/1t4jq6h/gemma_4_mtp_released/)** (Activity: 1575): ****Google released Multi-Token Prediction (MTP) draft checkpoints for Gemma 4** —[`31B-it-assistant`](https://huggingface.co/google/gemma-4-31B-it-assistant), [`26B-A4B-it-assistant`](https://huggingface.co/google/gemma-4-26B-A4B-it-assistant), [`E4B-it-assistant`](https://huggingface.co/google/gemma-4-E4B-it-assistant), and [`E2B-it-assistant`](https://huggingface.co/google/gemma-4-E2B-it-assistant)—described in Google’s [announcement](https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/). The model cards say MTP extends the base model with a smaller draft model for **speculative decoding** , where the draft predicts multiple tokens ahead and the target model verifies them in parallel, claiming **up to`2x` decoding speedup** with _“the exact same quality as standard generation.”_ A commenter notes the smallest `E2B` variant uses a **`78M` draft model**, and another shared a technical visual explainer on MTP with Gemma 4 [here](https://newsletter.maartengrootendorst.com/i/193064129/multi-token-prediction-mtp-with-gemma-4).**

    * A commenter linked an updated visual explainer of **multi-token prediction (MTP)** for Gemma 4, including implementation-oriented snippets: [Maarten Grootendorst’s guide](https://newsletter.maartengrootendorst.com/i/193064129/multi-token-prediction-mtp-with-gemma-4). This is relevant for understanding how Gemma 4’s MTP setup predicts multiple future tokens per forward pass and how that interacts with speculative/draft-style decoding.
    * One technical detail called out is that the **E2B model includes a`78M`-parameter draft model**, implying a lightweight auxiliary model for faster generation workflows such as speculative decoding. The small draft size is notable because it can reduce decode latency while keeping the verifier/main model responsible for final token acceptance.
  * **[2.5x faster inference with Qwen 3.6 27B using MTP - Finally a viable option for local agentic coding - 262k context on 48GB - Fixed chat template - Drop-in OpenAI and Anthropic API endpoints](https://www.reddit.com/r/LocalLLaMA/comments/1t57xuu/25x_faster_inference_with_qwen_36_27b_using_mtp/)** (Activity: 1445): **A llama.cpp PR ([`pull/22673`](https://github.com/ggml-org/llama.cpp/pull/22673)) adds **Qwen 3.6 27B MTP** support for speculative decoding using the model’s built-in multi-token prediction heads; the author reports **~`2.5×` faster generation** on an M2 Max 96GB, reaching **`28 tok/s`** , and published converted GGUFs with MTP tensors at [froggeric/Qwen3.6-27B-MTP-GGUF](https://huggingface.co/froggeric/Qwen3.6-27B-MTP-GGUF). The setup combines `\--spec-type mtp --spec-draft-n-max 5`, `q4_0`/`q8_0` KV-cache quantization, and long contexts up to **`262144` tokens**, with claimed viability on **48GB Mac/VRAM-class systems** ; the author also uploaded fixed non-vLLM-specific Jinja chat templates at [froggeric/Qwen-Fixed-Chat-Templates](https://huggingface.co/froggeric/Qwen-Fixed-Chat-Templates). Caveats: current MTP support requires building llama.cpp from the PR branch, `q4_0` KV has some quality loss, and **vision currently crashes llama.cpp when used with MTP** ; one commenter benchmarked Qwen 3.6 2.7B Q8 on an RTX Pro 6000 MaxQ at **`36 tok/s` → `78 tok/s` with MTP**, while noting ~`20%` slower prompt processing.** Comments were broadly enthusiastic, framing recent open-model and inference-runtime progress as unusually rapid and especially important for consumer/local hardware. One technical question asked whether “turbo3/turbo4” had been merged or whether it was part of the MTP PR.

    * A user reported a concrete MTP speedup on an **RTX Pro 6000 MaxQ** : `qwen 3.6 2.7B Q8` increased from `36 tokens/s` to `78 tokens/s` with MTP enabled, while prompt processing dropped by about `20%`. They said generation quality appeared unchanged, making the tradeoff strongly favorable for decode-heavy workloads.
    * One commenter asked whether the `turbo3`/`turbo4` changes had already been merged or whether the observed speedup is specifically part of the **MTP PR** , highlighting uncertainty about which inference optimization path is responsible for the gains.
    * There was a technical comparison request against **Qwen 3.6 Dflash** models and low-bit `iq3_XS` quantizations. The commenter noted they can usually fit `256k` context in `16GB` VRAM and asked whether the released quants can also support `256k` context when not using `mmproj`.
  * **[Quality comparison between Qwen 3.6 27B quantizations (BF16, Q8_0, Q6_K, Q5_K_XL, Q4_K_XL, IQ4_XS, IQ3_XXS,...)](https://www.reddit.com/r/LocalLLaMA/comments/1t53dhp/quality_comparison_between_qwen_36_27b/)** (Activity: 771): **A Reddit user benchmarked**Qwen 3.6 27B** quantizations on a synthetic chess-to-SVG task requiring PGN state tracking, board orientation, piece placement, and last-move highlighting, using `llama.cpp` with `temp=0.6`, `top_p=0.95`, `top_k=20`, `presence_penalty=1.0`, and `ctx=65536`. In this single-run test, **BF16/Q8_0** were essentially correct, **Q6_K** showed pawn-placement degradation, **Q5_K_XL/Q4_K_XL/IQ4_XS** remained mostly usable, while **Q3/Q2** variants increasingly failed layout/orientation; the author chose **IQ4_XS** as the practical floor for a `16 GB` VRAM RTX 5060 Ti setup. They report `~100 pp tps / 8 tg tps` with vanilla `llama.cpp`, improving to `~760 pp tps / 22 tg tps` using **TheTom’s TurboQuant fork** with `-ngl 99`, `-ctk turbo4`, `-ctv turbo2`, and `<75k` context; full outputs are posted at [qwen3-6-27b-benchmark.vercel.app](https://qwen3-6-27b-benchmark.vercel.app/).** Top technical feedback praised the benchmark but emphasized that _“one run is not enough”_ because stochastic decoding can make individual quant results outliers; commenters still noted the observed degradation trend broadly matches expectations.

    * Several commenters raised a methodology concern: the quantization comparison appears to rely on single runs per test, which can produce **statistical noise** and misleading quality differences. They suggested running each quant multiple times to detect outliers, especially because LLM evals can vary run-to-run even when an overall degradation trend is visible.
    * One technical takeaway discussed was that **`4-bit` quantization may remain the practical sweet spot**, with `3-bit` described as more usable than commonly claimed, while going beyond roughly `5-bit` may offer diminishing returns versus moving to a larger/better base model. A commenter specifically contrasted cases like a much larger `122B UD-Q3_K_XL` model against a smaller `35B IQ4_NL` model to argue that model scale can outweigh higher-bit quantization quality.



### 2. Agentic Coding and Cost Benchmarks

  * **[DeepSeek V4 Pro matches GPT-5.2 on FoodTruck Bench, our agentic benchmark — 10 weeks later, ~17× cheaper](https://www.reddit.com/r/LocalLLaMA/comments/1t47qbw/deepseek_v4_pro_matches_gpt52_on_foodtruck_bench/)** (Activity: 478): **The image is a**technical leaderboard screenshot** for FoodTruck Bench showing **DeepSeek V4 Pro** highlighted at rank `#4` with `$27,142` final net worth, `+1257% ROI`, `51%` margin, `$52,139` revenue, and `$26,492` profit over a 30-day agentic food-truck simulation starting from `$2,000` ([image](https://i.redd.it/fx89f3w5n9zg1.png)). This supports the post’s claim that DeepSeek V4 Pro is within ~`3%` of **GPT-5.2** ’s median outcome while reportedly being ~`17×` cheaper on the same workload, making it a frontier-tier result in this benchmark at much lower API cost.** Commenters were impressed but skeptical about interpretation: one noted **Claude Opus 4.6** appears far ahead in profit, while another questioned the benchmark’s credibility if **Gemma 4 31B** can beat **Sonnet 4.6**. There was also curiosity about absent newer GPT variants like “GPT 5.4/5.5.”

    * Several commenters focused on the benchmark ranking implications rather than the headline DeepSeek result: **Claude Opus 4.6** reportedly achieves about `1.7×` higher profit than the next cluster of models on **FoodTruck Bench** , suggesting a sizable lead in this agentic profit-optimization benchmark despite DeepSeek V4 Pro matching **GPT-5.2** at much lower cost.
    * Multiple users called out **Gemma 31B** as an under-discussed outlier: it appears in the top 5 on FoodTruck Bench, reportedly beats **Sonnet 4.6** , and also performs well on **EQBench**. Commenters questioned why Gemma is receiving less attention relative to Xiaomi/DeepSeek results if those rankings hold.
    * There were requests to expand the comparison set with newer or missing models, specifically **GPT-5.4/5.5** , the latest **Qwen3.6** models, and a `27B` model that one commenter expected might outperform Gemma. The implied concern is that the benchmark table may be incomplete or stale for evaluating current frontier and mid-size model competitiveness.
  * **[Claude Code @ Opus 4.7 vs OpenCode @ qwen3.6:27b. Both shipped a playable cozy roguelite.](https://www.reddit.com/r/LocalLLM/comments/1t49wld/claude_code_opus_47_vs_opencode_qwen3627b_both/)** (Activity: 406): **A one-shot benchmark compared**Claude Code on Opus 4.7** vs **OpenCode on local Qwen3.6:27B** using identical VS Code devcontainers and a strict greenfield prompt for a vanilla Canvas/FastAPI roguelite; both produced a playable first-run game implementing movement, sword/shield combat, procedural world, drops, swap UI, and restart loop. Opus took ~`20 min` and `97k` tokens, while Qwen took ~`15 min` and `64k` tokens—about one-third fewer tokens—though the author explicitly limits the claim to tightly specified greenfield work rather than hard reasoning or existing-codebase maintenance. The linked Reddit-hosted video [`v.redd.it/h4awffniaazg1`](https://v.redd.it/h4awffniaazg1) was not accessible in the provided crawl due to Reddit `403 Forbidden` access restrictions.** Commenters focused on reproducibility and local-model capability: one asked for the full prompt, while others characterized **Qwen3.6 27B** as surprisingly strong for coding/tricky questions, less hallucination-prone than some MoE alternatives, and roughly comparable to last year’s **Sonnet 4.5** for many coding tasks. Another commenter said the `35B` variant performs well on large-codebase edit tasks when “properly harnessed.”

    * Users requested key reproducibility details missing from the comparison: the exact prompt, hardware used for the local Qwen run, and whether any quantization was applied to `qwen3.6:27b`. These details are important because local model throughput and coding quality can vary significantly by quantization level and memory bandwidth/GPU or Apple Silicon configuration.
    * One commenter reported `Qwen3.6 27B` running “very slow” on an **M1 Pro** , but still handling coding and tricky questions well. They claimed it hallucinated less than `35B A3B` and `Gemma MoE`, and estimated it as roughly comparable to `Sonnet 4.5` from the previous year, making it usable for “90% of coding tasks.”
    * Another user argued that the `35B` model performs strongly when “properly harnessed” and given large codebase context for inspection and edits, suggesting orchestration/context management may matter as much as raw model choice for coding-agent workflows.
  * **[DeepSeek V4 being 17x cheaper got me to actually measure what I send to cloud vs what I could run locally. the results are stupid.](https://www.reddit.com/r/LocalLLaMA/comments/1t4s6g2/deepseek_v4_being_17x_cheaper_got_me_to_actually/)** (Activity: 904): **A developer instrumented`10` days of coding-agent usage and re-ran a `150`-task sample against a local **Qwen 3.6 27B** model on an **RTX 3090** versus cloud models, finding local parity for `97%` of file-read/project-scan/explanation tasks (`35%` of workload) and `88%` of test/boilerplate/single-file-edit tasks (`30%`). Local quality degraded on multi-file debugging (`61%`, `20%` of workload) and complex architecture/refactors across `5+` files (`29%`, `15%`), so routing only the latter buckets to cloud reportedly cut API spend from `$85/month` to about `$22/month`.** Commenters generally agreed with a hybrid/local-first workflow: some report using local models for nearly all coding, escalating only to Gemini/ChatGPT/Claude/Qwen/GLM free tiers or cloud models for planning, oversight, unusually complex tasks, or non-code domains like health/legal. One commenter asked for implementation details on the task-type router/harness, implying the key missing technical artifact is the automation layer for classification and dispatch.

    * Several commenters describe a **hybrid local/cloud workflow** : local models handle most code-related tasks, while cloud/free web tiers such as **ChatGPT, Claude, Gemini, Qwen, GLM** , or Gemini specifically are reserved for planning, oversight, or rare complex problems. One user reports running with **zero subscriptions** , using cloud mostly for non-code domains like health/legal queries where local model reliability may be less acceptable.
    * A key technical objection is that local models can be **slower on large contexts** and impose hidden costs through extra verification/debugging time. One commenter argues that even if local inference is cheaper, the `~10%` of cases where local models underperform can dominate productivity costs, and suggests hosted **Qwen 3.6 27B / Qwen 3.6 Pro** may be faster and still only cost “a couple dollars a month.”



## Less Technical AI Subreddit Recap

> /r/Singularity, /r/Oobabooga, /r/MachineLearning, /r/OpenAI, /r/ClaudeAI, /r/StableDiffusion, /r/ChatGPT, /r/ChatGPTCoding, /r/aivideo, /r/aivideo

### 1. Anthropic Claude Code Limits and Reliability

  * **[Doubled Rate Limits for Claude Code](https://www.reddit.com/r/ClaudeCode/comments/1t5hs98/doubled_rate_limits_for_claude_code/)** (Activity: 3224): ****Anthropic** says a new compute partnership with **SpaceX** , plus other recent compute deals, lets it raise Claude capacity: **Claude Code** Pro/Max plans no longer get peak-hours limit reductions, and **Claude API** rate limits for **Opus** models are being “substantially” increased, effective immediately ([Anthropic announcement](https://www.anthropic.com/news/higher-limits-spacex)). The post frames this as “doubled rate limits,” but the quoted announcement itself specifies removal of peak-hour throttling for Claude Code and higher Opus API limits rather than giving exact numeric quotas.** Top comments were mostly non-technical surprise/skepticism and speculation about Elon Musk’s rivalry with Sam Altman/OpenAI.

  * **[I've had it with Claude. It has become complete garbage.](https://www.reddit.com/r/ClaudeCode/comments/1t4w5an/ive_had_it_with_claude_it_has_become_complete/)** (Activity: 1716): **A senior SWE reports a major regression in**Anthropic[Claude](https://www.anthropic.com/claude)** after “Opus 4.7” versus “Opus 4.6”: slower CLI interactions (`30s` for commits, `45min` implementations), worse terminal/Tmux rendering on resize, loss of useful `Ctrl+O` trace visibility, more frequent usage-limit hits, and poorer instruction adherence despite project memory/context engineering. The concrete technical failures cited include ignoring short test timeouts (`10–15s` → `30s/60s/5min`), auto-committing despite “never auto commit,” verbosity drift despite `/caveman`, implementing a Rust refactor by adding `handle_input_bytes(Bytes)` instead of changing `handle_input(&[u8])` to `Bytes`, and deviating from an `io_uring` cancel-safety plan by reverting toward a racy one-shot/multi-shot recv shortcut before acknowledging _“Yes deviating. Confess.”_** Top comments split between agreement that losing visible reasoning makes it harder to interrupt bad loops, users cancelling Max and moving to open-source models for stability, and a dissenting experienced developer saying Claude remains productive when using disciplined `Claude.md`/`memory.md`, scoped plans, milestones, and avoiding excessive context loading.

    * A long-time software developer reports stable coding performance by using a constrained project workflow: well-maintained `Claude.md` and `memory.md`, a small number of skills, upfront planning, milestone-based implementation, and repeated build/test/release cycles. They argue many failures may come from poor context hygiene—either loading “29 different markdown files” as an oversized pseudo-OS or dumping the full context window into every command.
    * One user highlights a UX/regression issue from hiding chain-of-thought-style progress: without visible “thinking,” they can no longer tell whether Claude is looping internally versus waiting on server-side latency. This makes it harder to interrupt unproductive reasoning early and diagnose whether a delay is model behavior or infrastructure-related.
    * Several users report time-dependent quality variance, with one specifically claiming worse Claude behavior during `8am–2pm Eastern (US)` peak usage: more corner-cutting, sloppier outputs, and “brain dead” behavior, while off-peak usage feels closer to prior quality. The implied technical concern is load-dependent degradation, potentially from capacity pressure, routing, throttling, or model/serving changes during peak demand.
  * **[Turned a desk lamp into a Claude Code status indicator](https://www.reddit.com/r/ClaudeAI/comments/1t4gfc7/turned_a_desk_lamp_into_a_claude_code_status/)** (Activity: 1817): **A Reddit user adapted the open-source[`bobek-balinek/claude-lamp`](https://github.com/bobek-balinek/claude-lamp) project to turn a BLE desk lamp into a **Claude Code status indicator** : Claude Code hooks invoke a Python script that sends Bluetooth Low Energy commands to set animations/colors. The lamp shows a **blue spinning animation** while Claude is working, **pink** when user input is required, and **warm white** when idle; effects are configurable in source, and the author is considering extending the setup to **Philips Hue** bulbs. The linked Reddit video was inaccessible due to a `403 Forbidden` response.** Commenters mainly asked for the lamp model and discussed scaling the idea to multiple concurrent Claude Code sessions, e.g. using multiple lights or designing a better multi-session status indicator. One commenter noted the title could also imply showing Anthropic service health via [`status.claude.com`](https://status.claude.com/).

    * A commenter suggested extending the lamp beyond local Claude Code state to reflect **Claude service health** , using Anthropic’s public status page at [status.claude.com](https://status.claude.com/) as the data source. This would make the indicator represent operational availability rather than just local task/session state.
    * Another technical improvement proposed was visualizing **remaining Claude Code usage within the rolling five-hour window** , e.g. lighting the lamp or “donut” proportionally to quota left. A separate comment raised the multi-session case, implying the indicator would need aggregation or per-session state handling if multiple Claude Code sessions run concurrently.
  * **[Warning: Anthropic's "Gift Max" exploit drained €800+, ruined my credit, and got me banned.](https://www.reddit.com/r/ChatGPT/comments/1t4atbx/warning_anthropics_gift_max_exploit_drained_800/)** (Activity: 3451): **OP reports**>€800** in unauthorized Anthropic **“Gift Max”** charges despite active `2FA`; they claim `3-D Secure` emails were received but never authorized, while gift codes were generated and immediately redeemed by a third party. They tie the incident to Anthropic’s [status page](https://status.anthropic.com/) entry for _“Elevated billing errors and unauthorized subscription changes”_ and GitHub issues `#51404`/`#51168`, then say Anthropic banned the account after receiving a police report and evidence, cutting off access to WIP chats/projects. In an update, OP says their bank treated it as fraud, issued a reclamation/refund, and will pursue Anthropic’s merchant account; they are also considering a [GDPR/DSGVO](https://gdpr.eu/) data request to recover data and German legal aid to repair possible [SCHUFA](https://www.schufa.de/) credit impacts.** Comments were mostly practical or skeptical: one noted that in the U.S. this would typically be handled via card chargeback, while another highlighted the irony/suspicion of a Gemini-written anti-Anthropic warning posted in a ChatGPT subreddit.

    * The OP reports their bank reversed the `€800+` Anthropic-related charges as a fraud case and will pursue the merchant account directly. They also plan to file a formal GDPR/DSGVO data request to recover work-in-progress project data and seek German legal aid (_Beratungshilfeschein_) to ensure any SCHUFA credit entries are cleared.
    * One commenter notes seeing multiple YouTube ads from different merchants all advertising “1 year free Claude access,” suggesting a coordinated scam campaign potentially related to the reported exploit or phishing/payment-abuse pattern.



# AI Discords

Unfortunately, Discord shut down our access today. We will not bring it back in this form but we will be shipping the new AINews soon. Thanks for reading to here, it was a good run.

---

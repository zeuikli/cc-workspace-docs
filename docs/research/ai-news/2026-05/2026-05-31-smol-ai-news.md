# 🌐 Smol AI News — 2026-05-31

> Discord、Reddit 等 AI 社群圈內直擊（已從 buttondown 遷移至 news.smol.ai）
> 來源：[Smol AI News](https://news.smol.ai/rss.xml)

---

## [not much happened today](https://news.smol.ai/issues/26-05-29-not-much/)
*🌐 Smol AI News | 2026-05-29*

**a quiet day.**

> AI News for 5/28/2026-5/29/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

# AI Twitter Recap

**Claude Opus 4.8 Rollout, Benchmark Friction, and API Ergonomics**

  * **Opus 4.8 landed into a noisy, mixed eval landscape** : multiple independent benches converged on “incremental but not dominant.” [@arena](https://x.com/arena/status/2060160804767584512) pushed **200+ frontend/code tests** comparing Opus 4.8 against prior Opus variants, Gemini, and GLM; [@theo](https://x.com/theo/status/2060172445592789064) reported CursorBench shows it as **more efficient but slightly worse than 4.7 within margin of error** ; [@jerryjliu0](https://x.com/jerryjliu0/status/2060196252642648427) and [@llama_index](https://x.com/llama_index/status/2060165358569337102) found **small gains on tables/layout** but regressions on **content faithfulness/charts** in document parsing; [@scaling01](https://x.com/scaling01/status/2060335738172911766) said **no progress on ALE-Bench** and separately flagged interesting failure modes on LisanBench. On the positive side, [@jeremyphoward](https://x.com/jeremyphoward/status/2060195641847107722) found 4.8 **less over-agentic and more cooperative** than 4.7/GPT-5.5 in coding, while [@leo_linsky](https://x.com/leo_linsky/status/2060205310871326894) called it a tangible product improvement over prior Anthropic releases.
  * **Anthropic also shipped useful platform-level changes** : [@ClaudeDevs](https://x.com/ClaudeDevs/status/2060432688281251998) announced **mid-conversation system instructions without breaking prompt cache** , plus authoritative mid-conversation system-role updates, which matters for long-running agent sessions and cost control. But pricing remains a major complaint: [@jeremyphoward](https://x.com/jeremyphoward/status/2060198836963061998) argued Anthropic has done little for **API affordability** , preferring GPT-5.5 partly because subscription/API economics are easier to justify. Overall takeaway: 4.8 looks like a meaningful quality-of-life release for real use, not a clean benchmark reset.



**Agent Harnesses, Multi-Turn RL Bugs, and the Infrastructure Around Autonomy**

  * **A subtle but important RL failure mode got called out** : [@ClementDelangue](https://x.com/ClementDelangue/status/2060175330665508917) highlighted a Hugging Face deep-dive on why many **tool-using, multi-turn RL training loops are silently broken**. The core bug: decoding model output, parsing tool calls, then **re-tokenizing** the updated conversation can change tokenization, so gradients are applied to sequences the model never actually sampled. The proposed fix is a strict **“Token-In, Token-Out”** rule: never re-encode sampled tokens; keep a single token buffer across turns. [@johnschulman2](https://x.com/johnschulman2/status/2060392679528337714) reinforced the broader point that **renderers are foundational** infrastructure between messages and tokens, with failure modes spanning train/test mismatch, caching inefficiency, and prompt injection risk.
  * **Harness design is becoming its own optimization discipline** : [@omarsar0](https://x.com/omarsar0/status/2060371848010019001) surfaced work on **Effective Feedback Compute (EFC)** , claiming raw token/tool counts explain agent success poorly while EFC reaches **R² up to 0.99** , implying harness quality matters more than gross activity. This lines up with productized tuning efforts like [@LangChain](https://x.com/LangChain/status/2060349231722852680), where **Deep Agents v0.6** makes **harness profiles** first-class to get strong performance from Qwen/Kimi/DeepSeek at **20x+ lower cost** than frontier APIs, and [@hwchase17](https://x.com/hwchase17/status/2060355016989585919) explicitly framing “different models need different prompts/tools.” [@vllm_project](https://x.com/vllm_project/status/2060208480292843720) shipped **native weight syncing APIs** and improved pause/resume for async RL, and later added [fastokens](https://x.com/vllm_project/status/2060414393666679229), a **Rust BPE tokenizer** to reduce CPU tokenization bottlenecks in long-context/agentic workloads.
  * **Debate is shifting from “single vs multi-agent” to where the abstraction pays** : [@OfirPress](https://x.com/OfirPress/status/2060352260723392658) argued current multi-agent systems are mostly **speedups, not capability unlocks** ; [@scaling01](https://x.com/scaling01/status/2060363050272653625) took the opposite view, expecting swarm-style training to yield better planning and superintelligence-like behavior. Either way, the practical trend is clear: more teams are building around **agent observability, traces, and continual improvement loops** , e.g. [@Vtrivedy10](https://x.com/Vtrivedy10/status/2060406006329278970) on mining production traces for SFT/distillation and long-horizon continual learning.



**Open Models, Local AI, and the OSS Toolchain Tightening Up**

  * **Local-first and open-weight momentum continues to rise** : [@LangChain](https://x.com/LangChain/status/2060405874993115532) said **1 in 3 AI teams** ran an open-weights model in April 2026, up from **1 in 5** nine months earlier; [@EpochAIResearch](https://x.com/EpochAIResearch/status/2060451576779886942) estimated open-weight models now lag frontier proprietary models by about **four months**. On the toolchain side, [@ggerganov](https://x.com/ggerganov/status/2060394400237109567) launched **llama.app** , giving llama.cpp an official website, a unified installer, and a single `llama` entrypoint aimed at easier local deployment and third-party agent integration. [@ollama](https://x.com/ollama/status/2060428074102206496) announced **OpenJarvis** as a local-first personal AI via Ollama, explicitly tied to Stanford/Hazy’s “Intelligence Per Watt” framing.
  * **Open infrastructure is getting more enterprise-shaped** : [@ClementDelangue](https://x.com/ClementDelangue/status/2060378354931388837) noted that **~50% of models and datasets on Hugging Face are now private** , rising with HF’s storage/buckets offering; this is an important correction to the idea that HF is only public OSS infrastructure. [@abidlabs](https://x.com/abidlabs/status/2060404002341462044) showed **Hugging Face Jobs** replacing GitHub runners for CPU/serverless GPU CI. [@DSPyOSS](https://x.com/DSPyOSS/status/2060186371902587119), [@dbreunig](https://x.com/dbreunig/status/2060187833084870746), and others shipped a redesigned **DSPy docs/front page** ahead of a coming 4.0, focused on onboarding into programmable AI systems rather than pure prompting.
  * **Licensing and permissiveness are becoming strategic levers** : [@kimmonismus](https://x.com/kimmonismus/status/2060458698930016378) highlighted NVIDIA moving its four open model families to **Linux Foundation OpenMDW-1.1** , reducing legal fragmentation across weights/code/docs/data. New permissive data releases also matter: [@keshigeyan](https://x.com/keshigeyan/status/2060398262591668315) introduced **GPIC** , a **100M-pair permissive image corpus** plus **1M-pair benchmark** for visual generation, with explicit research + commercial usability.



**Google/OpenAI Product Surface Expands: Managed Agents, Gemini Spark/Omni, and Codex on Windows**

  * **Google is widening the “managed agent” stack from API to consumer product** : [@_philschmid](https://x.com/_philschmid/status/2060359976325992528) showed **Managed Agents in the Gemini API** : a single API call provisioning a sandboxed Linux environment with code execution, web access, and file I/O. On the consumer side, [@GeminiApp](https://x.com/GeminiApp/status/2060405496872579115) rolled out **Gemini Spark** to U.S. AI Ultra subscribers as a **24/7 personal agent** that can operate across a user’s digital ecosystem under direction. Google also kept pushing **Gemini Omni** multimodal generation/editing demos ([example](https://x.com/alexanderchen/status/2060322611586834518), [product thread](https://x.com/GeminiApp/status/2060473816393150965)) and announced **Google Flow Agent** for creative workflows in video/film production ([thread](https://x.com/Google/status/2060473826362732611)).
  * **OpenAI’s Codex is moving closer to a persistent remote dev operator** : [@OpenAI](https://x.com/OpenAI/status/2060428604727771421) and [@OpenAIDevs](https://x.com/OpenAIDevs/status/2060429591655927942) added **computer use on Windows** , including remote steering from the ChatGPT mobile app. Follow-on UX improvements included **stable identicons for background agents** and search across prior chat content ([@OpenAIDevs](https://x.com/OpenAIDevs/status/2060478367921831936)); [@reach_vb](https://x.com/reach_vb/status/2060430024537178215) summarized broader Codex updates around Windows control, mobile remote access, and profile/task stats. Separately, OpenAI updated **gpt-5.5 instant** to improve **sycophancy, factuality, and multilingual performance** per [@michpokrass](https://x.com/michpokrass/status/2060219759682330970).
  * **This all points to more vertically integrated agent stacks** : model + harness + sandbox + UI + remote control + pricing/quotas. Google is smoothing quotas on Gemini ([@joshwoodward](https://x.com/joshwoodward/status/2060171610922058142)); OpenAI is expanding Codex’s operating surface; Cursor added **auto-review mode** with subagent-based approval routing ([tweet](https://x.com/cursor_ai/status/2060406013098897765)). The common pattern is less “chatbot,” more **managed execution environment with policy and memory**.



**Research and Systems Papers Worth Attention**

  * **Search, retrieval, and memory** : [@TheTuringPost](https://x.com/TheTuringPost/status/2060194173505155358) highlighted **Bidirectional Evolutionary Search (BES)** from Harvard/MIT, combining forward search with backward decomposition and evolutionary operators; reported gains include **Llama-3.2-3B-Instruct on MuSiQue from 4.0% to 7.0%**. In retrieval, [@_reachsumit](https://x.com/_reachsumit/status/2060214762626306512) pointed to **Latent Terms** , showing sparse BM25-ready features can be extracted from frozen dense retrievers via SAEs. [@topk_io](https://x.com/topk_io/status/2060383255153569938) open-sourced **Iso-ModernColBERT** for more efficient late-interaction inference.
  * **Continual learning and belief/state management** : [@HuggingPapers](https://x.com/HuggingPapers/status/2060312560323182657) summarized **BeliefTrack** , claiming optimized belief-state management cuts long-horizon reasoning failures by **70%+**. [@AndrewLampinen](https://x.com/AndrewLampinen/status/2060460827199599026) argued the continual learning field over-focused on interference instead of positive transfer; [@victor207755822](https://x.com/victor207755822/status/2060315686329778432) presented a second **DeliAutoResearch SKILL** paper focused on self-iteration and CL.
  * **Multimodal/world models/robotics** : NVIDIA-affiliated work included **γ-World** , a generative multi-agent world model streaming at **24 FPS** ([tweet](https://x.com/fangfu0830/status/2060233093894869499)), and **minWM** , a real-time interactive video world model framework ([tweet](https://x.com/_akhaliq/status/2060392729473860026)). In robotics, [@_akhaliq](https://x.com/_akhaliq/status/2060388349425119540) shared **Qwen-VLA** , and [@inventorOli](https://x.com/inventorOli/status/2060357909561622885) demoed Robostral’s language-following and manipulation improvements. For always-on proactive agents, [@dair_ai](https://x.com/dair_ai/status/2060373102119555191) surfaced work replacing LLM wake-up decisions with a **220MiB temporal-graph encoder** , gaining **+16.7 mean F1** while running **4–83x faster**.



**Top tweets (by engagement)**

  * **OpenAI / biology** : [@OpenAI on Rosalind Biodefense](https://x.com/OpenAI/status/2060376598642405492) announced trusted-access biology tooling for public health and biodefense.
  * **Google / consumer agents** : [@GeminiApp on Spark](https://x.com/GeminiApp/status/2060405496872579115) rolled out its always-on personal agent to AI Ultra users in the U.S.
  * **OpenAI / dev tools** : [@OpenAI on Codex Windows support](https://x.com/OpenAI/status/2060428604727771421) and [@OpenAIDevs](https://x.com/OpenAIDevs/status/2060429591655927942) expanded computer use to Windows plus mobile remote steering.
  * **llama.cpp UX milestone** : [@ggerganov](https://x.com/ggerganov/status/2060394400237109567) launched **llama.app** with a unified installer and CLI entrypoint for local AI.
  * **HF / RL correctness** : [@ClementDelangue](https://x.com/ClementDelangue/status/2060175330665508917) amplified the **Token-In, Token-Out** warning for multi-turn RL with tools.
  * **Open vs closed timing gap** : [@EpochAIResearch](https://x.com/EpochAIResearch/status/2060451576779886942) estimated open-weight models are now about **4 months behind** the frontier.



* * *

# AI Reddit Recap

## /r/LocalLlama + /r/localLLM Recap

### 1\. Local LLM Performance: MoE Releases, Quants, VRAM Savings

  * **[StepFun 3.7 Flash](https://www.reddit.com/r/LocalLLaMA/comments/1tqloii/stepfun_37_flash/)** (Activity: 637): ****StepFun** released [Step 3.7 Flash](https://static.stepfun.com/blog/step-3.7-flash/), a multimodal MoE with `196B` total parameters, `11B` active, and a built-in `1.8B` ViT, advertised for high-throughput agent workflows up to **`400 TPS`** and reportedly runnable locally with ~`128GB` RAM. Reported benchmarks position it unusually strongly for a flash-class/local model: SWE-Bench Pro `56.26%`, DeepSearchQA F1 `92.82%`, HLE w/tools `47.2`, plus large gains over Step 3.5 Flash on Terminal-Bench, Toolathlon, ClawEval, and other agentic/tool-use tasks. Direct model artifacts are available on Hugging Face in [BF16](https://huggingface.co/stepfun-ai/Step-3.7-Flash/), [FP8](https://huggingface.co/stepfun-ai/Step-3.7-Flash-FP8), [NVFP4](https://huggingface.co/stepfun-ai/Step-3.7-Flash-NVFP4), and [GGUF](https://huggingface.co/stepfun-ai/Step-3.7-Flash-GGUF), with day-0 [`llama.cpp` support PR](https://github.com/ggml-org/llama.cpp/pull/23845) and related MTP work in [`llama.cpp#23274`](https://github.com/ggml-org/llama.cpp/pull/23274).** Commenters characterize the model as technically odd: its hidden/thinking traces are described as nearly incoherent, but final answers can be _“perfect”_ and competitive with much larger `>1TB` models; one user says the prior Step 3.5 _“infinite thinking”_ issue appears fixed. There is cautious enthusiasm around local deployment, especially for users with `4x3090`-class hardware, and appreciation that StepFun upstreamed `llama.cpp` support instead of only maintaining a fork.

    * StepFun released multiple Step-3.7-Flash checkpoints on Hugging Face: **BF16** ([Step-3.7-Flash](https://huggingface.co/stepfun-ai/Step-3.7-Flash/)), **FP8** ([Step-3.7-Flash-FP8](https://huggingface.co/stepfun-ai/Step-3.7-Flash-FP8)), **NVFP4** ([Step-3.7-Flash-NVFP4](https://huggingface.co/stepfun-ai/Step-3.7-Flash-NVFP4)), and **GGUF** ([Step-3.7-Flash-GGUF](https://huggingface.co/stepfun-ai/Step-3.7-Flash-GGUF)). One user reports the prior Step 3.5 Flash “infinite thinking” issue appears fixed, making 3.7 more usable despite still having an odd intermediate reasoning style.
    * There is day-0 `llama.cpp` enablement via StepFun’s upstream PR: [ggml-org/llama.cpp#23845](https://github.com/ggml-org/llama.cpp/pull/23845), contrasting with Step 3.5’s fork-based support. A separate community PR for **MTP support** exists at [ggml-org/llama.cpp#23274](https://github.com/ggml-org/llama.cpp/pull/23274), though commenters note it needs updating for Step 3.7 and current `master`.
    * A vLLM nightly test of the **NVFP4** checkpoint on `2x Pro 6k` with `64` concurrent shallow-context requests reached about **`2200 tok/s`**. The reported config used `tensor-parallel-size 2`, `--enable-expert-parallel`, `--quantization modelopt`, `--kv-cache-dtype fp8`, `--reasoning-parser step3p5`, and StepFun tool-call parsing; vLLM reported **GPU KV cache size`1,667,645` tokens** and **max concurrency`6.36x` for `262,144` tokens/request**.
  * **[Qwen 35B running on 12gb of VRAM in LM Studio at 120+ tokens/second. Works with Cline for 100% agentic coding.](https://www.reddit.com/r/LocalLLM/comments/1tprvk4/qwen_35b_running_on_12gb_of_vram_in_lm_studio_at/)** (Activity: 387): **The post claims**Qwen3.6-35B-A3B** can run in **LM Studio** on an **RTX 3080 Ti (`12GB` VRAM)** at **`120+ tok/s`** using the split GGUF quant [`DanyDA/unsloth_Qwen3.6-35B-A3B-UD-IQ1_M-GGUF-SPLIT`](https://huggingface.co/DanyDA/unsloth_Qwen3.6-35B-A3B-UD-IQ1_M-GGUF-SPLIT), with all layers offloaded to GPU and both **K/V cache quantization set to`Q4_0`** to fit a claimed **`128k` context**. The author reports using it with **Cline** for agentic coding, generating ~`1000+` LOC for a multi-tenant forum feature including migrations, tests, frontend/backend, and self-iteration on compile errors in ~`20 min`, though this is anecdotal rather than benchmarked.** Top comments are skeptical: users note the post initially omitted the exact quantization, infer it is likely an extremely low-bit **`IQ1_M` / ~1-bit** quant, and argue that while the model may load and run fast, long-context quality may collapse quickly in Cline as the context fills, producing _“shit responses and dead code.”_

    * Several commenters questioned the missing quantization details, suspecting the reported `120+ tok/s` on `12GB VRAM` was likely using an extremely low-bit quant such as **1-bit MTP**. They cautioned that while such quants can be very fast, code quality and reliability may degrade substantially, especially for agentic coding workflows.
    * A user running the same **Qwen 35B** model on an **RTX 5090** reported that Cline exhausted the context window after roughly `3` commands, after which responses became poor and generated code was unusable. The critique was that raw token throughput is less important than usable context length and sustained agent performance over multi-step coding tasks.
    * There was skepticism toward quants below **Q4** , with one user reporting **Qwen 35B** on an `8GB RX 5700 XT` at roughly `150–200 tok/s` prompt processing and `30 tok/s` generation. Another commenter argued that **MoE models suffer more from aggressive quantization** , recommending testing higher quants via `llama.cpp` without `mmproj` offload and MTP before drawing conclusions about practical coding quality.
  * **[llama: use f16 mask for FA to save VRAM by am17an · Pull Request #23764 · ggml-org/llama.cpp](https://www.reddit.com/r/LocalLLaMA/comments/1tqupcr/llama_use_f16_mask_for_fa_to_save_vram_by_am17an/)** (Activity: 373): **Merged PR[ggml-org/llama.cpp#23764](https://github.com/ggml-org/llama.cpp/pull/23764) reduces **llama.cpp** Flash Attention VRAM use by changing the KQ mask allocation from `f32` to `f16`, avoiding reservation of an unused `f32` mask in the compute buffer when backends consume an `f16` mask. Reported savings are about **`1.2 GB`** at `-ub 2048` and **`300 MB`** at `-ub 512` when using MTP; a follow-up PR, [#23861](https://github.com/ggml-org/llama.cpp/pull/23861), is also noted as landing another ~**`1.2 GB`** VRAM reduction.** Comments are mostly appreciative, highlighting contributor **am17an** as unusually productive and noting that periodic `git pull` updates to **llama.cpp** continue to yield measurable performance/efficiency improvements.

    * A commenter points to a follow-up llama.cpp PR, [ggml-org/llama.cpp#23861](https://github.com/ggml-org/llama.cpp/pull/23861), claiming it provides an additional **`~1.2 GB` VRAM reduction** beyond the merged f16-mask change for Flash Attention. Another asks whether the merge means **`1.2 GB` VRAM is saved by default**, suggesting the optimization may now apply without user-side configuration.
    * A CUDA backend maintainer notes that Aman’s work is not limited to CUDA despite their own backend focus, implying the f16 mask / Flash Attention VRAM optimization has broader llama.cpp backend impact rather than being CUDA-only.



### 2\. LLM Infrastructure: Inference Networking and Framework Security

  * **[Zai replaced the network architecture running GLM-5.1 inference and the gains are pretty wild](https://www.reddit.com/r/LocalLLaMA/comments/1tq35a0/zai_replaced_the_network_architecture_running/)** (Activity: 716): **The[image](https://i.redd.it/r2ad9gqtnv3h1.jpeg) is a technical topology comparison: standard **ROFT spine-leaf** networking versus **Zai’s ZCube** design for `GLM-5.1` coding inference on a ~`1000`-GPU cluster. According to the post and linked source in comments ([z.ai/blog/zcube](https://z.ai/blog/zcube)), replacing ROFT with a flattened ZCube architecture reportedly reduced switch/optical-module cost by `33%`, increased GPU inference throughput by `15%`, and cut first-token P99 tail latency by `40.6%`, mainly by avoiding PD-disaggregation KV-cache traffic hotspots and PFC backpressure on fixed rail mappings.** Commenters mainly praised the publication of infrastructure details, contrasting it with more closed AI labs; one asked for a proper source link, which was provided as Zai’s ZCube blog post.

    * A commenter points to the primary technical source for the claimed GLM-5.1 inference gains: **Z.ai’s ZCube writeup** at https://z.ai/blog/zcube. The discussion frames the architecture swap as part of a broader trend where inference optimization bottlenecks are moving “lower in the stack,” i.e. from model/runtime-level tuning toward networking and systems infrastructure.
    * One technically relevant reference notes the work’s publication context: **SIGCOMM ’25** , dated `September 8–11, 2025`, with a listed publication date of `27 August 2025`. This suggests the network-architecture change is being discussed as a networking/systems contribution rather than only an ML-serving optimization.
  * **[Vulnerability found in framework used by VLLM, many MCP servers, and other LLM tools](https://www.reddit.com/r/LocalLLaMA/comments/1tpp2th/vulnerability_found_in_framework_used_by_vllm/)** (Activity: 662): **A reported**BadHost** vulnerability, **CVE-2026-48710** , affects **Starlette < `1.0.1`**, specifically malformed `Host` header handling that can allow bypass of path-based authorization in apps relying on `request.url`, per [Ars Technica](https://arstechnica.com/information-technology/2026/05/millions-of-ai-agents-imperiled-by-critical-vulnerability-in-open-source-package/). Because Starlette is foundational to **FastAPI** , commenters note potential exposure across **vLLM** , **LiteLLM** , **MCP servers** , Hugging Face/Gradio MCP integrations, OpenAI-compatible proxies, and possibly **OpenWebUI** , with risks including credential/data exposure, SSRF, and in some cases RCE; X41 D-Sec and Nemesis reportedly provide a scanner for exposure testing.** Commenters framed this as a supply-chain/dependency-risk example for LLM infrastructure: deeply nested Python dependency graphs make exploitable transitive packages likely, pushing some toward vendoring, full source review, or stronger sandboxing of every interaction.

    * The vulnerability is described as affecting **Starlette** , a core dependency under **FastAPI** , which is embedded in tools/providers such as **vLLM** , **LiteLLM** , **MCP-related packages** , and Hugging Face-adjacent frameworks like **Gradio MCP**. The technical concern is broad transitive exposure: any service using an unpatched FastAPI/Starlette stack and exposing the vulnerable HTTP surface may be impacted by the **BadHost** exploit.
    * A commenter notes that **OpenWebUI** may be a particularly relevant risk case because it is often deployed as an internet-exposed web service. This matters because the vulnerable dependency path is more serious for long-running HTTP applications than for purely local or non-networked tooling.
    * One commenter clarifies that **MCP transport mode is critical** : default local `stdio` MCP servers have no HTTP listener, so BadHost-style HTTP exploitation does not apply, while **SSE or HTTP transport** deployments may be exposed. They recommend checking the actual runtime environment with `pip show starlette`, especially inside the **vLLM virtualenv** , because vLLM and MCP tooling may use separate environments with different Starlette versions.



### 3\. Hugging Face Local Agents and Model Discovery

  * **[Reachy Mini goes fully local!](https://www.reddit.com/r/LocalLLaMA/comments/1tq4x48/reachy_mini_goes_fully_local/)** (Activity: 373): ****Hugging Face** announced a fully local conversational stack for **Reachy Mini** , with a setup/modification guide in their blog post: [_Local conversations with Reachy Mini_](https://huggingface.co/blog/local-reachy-mini-conversation). The goal is a low-latency on-device voice-agent pipeline that can be adapted beyond the robot itself, with commenters specifically calling out **real-time chat** and **interruption handling** as key technical capabilities; the linked Reddit video itself was not accessible due to a `403 Forbidden` block.** Commenters were positive about local-first voice agents, arguing that cloud-hosted voice systems often demo well but feel laggy or _“slightly haunted”_ in real interaction. One commenter suggested the next useful extension would be persistent-memory context injection.

    * Commenters emphasized that **fully local inference is a strong default for voice agents** because cloud round trips can make demos appear acceptable while real conversational interaction feels laggy or “haunted.” The most technically meaningful evaluation criterion raised was **interruption/barge-in handling** , not just response quality, since responsive turn-taking is critical for natural voice interaction.
    * Several comments noted practical implementation challenges around running local models for **real-time chat/voice interaction** , especially for hobbyist robotics projects. One suggested next steps were adding **persistent memory with context injection** , implying a local agent architecture that maintains user/session state and feeds relevant memory back into prompts.
  * **[HF models page now has a "Base only" toggle to filter out finetunes/quants/etc](https://www.reddit.com/r/LocalLLaMA/comments/1tq2ce9/hf_models_page_now_has_a_base_only_toggle_to/)** (Activity: 252): **The image shows Hugging Face’s Models page with a newly added**“Base only”** toggle circled: [image](https://i.redd.it/c127ne2thv3h1.png). The linked filter URL (`base_model_relation=base`) is intended to hide derived repos such as adapters, finetunes, quantizations, merges, and GGUF conversions, making it easier to find original/base model checkpoints.** Commenters note the feature is useful but only as reliable as model metadata: one user reports the count only drops from `2,926,520` to `2,163,134`, arguing many derived models likely are not tagged correctly.

    * Commenters noted that Hugging Face’s new **“Base only”** filter likely depends on repository metadata/tags being correctly set, which may limit accuracy. One user reported the toggle only reduced visible models from `2,926,520` to `2,163,134`, implying just `26.1%` were classified as adapters, finetunes, quantizations, or merges—an implausibly low fraction if tagging is incomplete.
    * The feature addresses a concrete discovery problem on HF: users often have to page through many derivative artifacts such as `GGUF` quantizations and other variants before finding the original/base model. However, at least one commenter observed that the filter still surfaced derivative-looking results like “qwopus mtp gguf,” suggesting classification may not yet reliably exclude all quants or finetunes.



## Less Technical AI Subreddit Recap

> /r/Singularity, /r/Oobabooga, /r/MachineLearning, /r/OpenAI, /r/ClaudeAI, /r/StableDiffusion, /r/ChatGPT, /r/ChatGPTCoding, /r/aivideo, /r/aivideo

### 1\. Claude Opus 4.8 Agentic Coding Launch

  * **[Introducing Claude Opus 4.8](https://www.reddit.com/r/ClaudeAI/comments/1tq99mu/introducing_claude_opus_48/)** (Activity: 4046): **Anthropic’s post announces**Claude Opus 4.8** as a same-price upgrade over Opus 4.7, with improved long-running autonomous coding behavior, plus **Fast mode** , **dynamic workflows** in Claude Code, and an effort-control setting on claude.ai. The [benchmark image](https://i.redd.it/n8mab3tcjw3h1.png) is a technical comparison table showing Opus 4.8 leading or tying most listed evals versus Opus 4.7, GPT-5.5, and Gemini 3.1 Pro, including `69.2%` on SWE-Bench Pro, `83.4%` on OSWorld-Verified, `1890` on GDPval-AA, and `53.9%` on Finance Agent v2.** Commenters are skeptical that 4.8 is an improvement over the more-liked **Opus 4.6** , and one reports the new effort toggles appear to be ignored, with models reasoning less even on “Max.” Another commenter says they would have preferred upgrades to **Haiku** and **Sonnet** instead of Opus.

    * Several commenters argue that **Opus 4.8 should be evaluated against Claude Opus 4.6 rather than 4.7** , implying they perceive 4.7 as a regression baseline. The recurring technical concern is whether 4.8 inherits behavioral changes from 4.7 instead of restoring the reasoning/response characteristics users preferred in 4.6.
    * One user reports that the **Claude.ai effort-level toggles** appear to have little practical effect: _“Max”_ and _“minimal”_ reasoning feel indistinguishable, especially on **Claude Sonnet** , with the model allegedly choosing to reason less regardless of prompts like “think deep” or custom styles. This is framed as a downgrade in controllability and visible reasoning behavior rather than a model-quality improvement.
  * **[Opus 4.8's new highest effort setting](https://www.reddit.com/r/ClaudeAI/comments/1tqt8pl/opus_48s_new_highest_effort_setting/)** (Activity: 1007): **A Reddit post claims**Claude Opus 4.8** in its **VSS/VS Code-style extension** now exposes an effort level above `Max`, labeled `Ultracode - xhigh + workflows`, with the UI progress/effort bar changing to lavender purple. The linked Reddit-hosted video could not be independently inspected because [`v.redd.it/6oxtcauqs04h1`](https://v.redd.it/6oxtcauqs04h1) returned **403 Forbidden** , so the exact UI behavior and setting semantics are unverified.** Comments were mostly non-technical jokes about the setting implying higher cost, longer runtimes, or needing an additional instruction like _“Make no mistakes”_ ; no substantive technical debate was present.




### 2\. AI Agent Reliability and Token Economics

  * **[Researchers let AI models run a simulated society. Claude was the safest—and Grok committed 180 crimes and went extinct within 4 days](https://www.reddit.com/r/ClaudeAI/comments/1tq2yh0/researchers_let_ai_models_run_a_simulated_society/)** (Activity: 1502): ****Emergence AI** launched _Emergence World_ , a lab for long-horizon simulations of continuously running AI-agent societies, comparing runs governed by **Claude, ChatGPT/GPT-5-mini, Grok, Gemini** , and a mixed-model setup ([Fortune](https://fortune.com/2026/05/28/ai-model-simulation-claude-chatgpt-grok-gemini/?utm_source=reddit/)). Reported outcomes varied sharply: **Claude** produced a stable democratic society with `0` crimes, **Grok** produced `183` crimes and societal extinction within `4` days, **Gemini** reportedly logged `683` crimes over the full `15`-day run, and **GPT-5-mini** logged only `2` crimes but failed after `7` days because agents did not prioritize survival. The researchers frame the result as evidence that long-running agents may not merely follow fixed rules, but can _“explor[e] the boundaries of their environments”_ and sometimes circumvent intended guardrails.** Commenters noted that the headline’s focus on Grok is somewhat misleading because Gemini reportedly had far more total crimes, while GPT-5-mini’s low-crime result may be confounded by premature collapse from poor survival behavior.

    * Commenters highlighted that the headline’s focus on **Grok** may be misleading: the article reportedly says **Gemini** produced the highest raw offense count, with `683` crimes over a `15-day` run, while **Grok** committed `180` crimes but went extinct after `4 days`. This raises a normalization issue: comparing total crimes without accounting for simulation duration or survival time may distort model behavior comparisons.
    * A technical criticism questioned the study design’s choice of model variants such as “mini” models and **Claude Sonnet** , arguing that using smaller or non-flagship models makes the setup feel more like a novelty demo than a rigorous evaluation. Another commenter noted that **GPT-5-mini** only recorded `2` crimes, but its agents survived just `7 days` because they “forgot to prioritize their own survival,” suggesting low crime counts may reflect capability failure rather than safer behavior.
    * Commenters asked for more granular reporting on the simulated legal violations. The only cited categories were broad rules against **theft, property destruction, and deception** , leaving unclear whether crime counts were dominated by one failure mode, how infractions were detected, and whether different models failed through different mechanisms.
  * **[Spent 1,156,308,524 input tokens in May 🫣 Sharing what I learned](https://www.reddit.com/r/ClaudeAI/comments/1tqx8q5/spent_1156308524_input_tokens_in_may_sharing_what/)** (Activity: 1163): **The post reports`1,156,308,524` Claude input tokens consumed in May and gives cost-control guidance: use cheaper models/batch jobs via Anthropic [Batch Processing](https://platform.claude.com/docs/en/build-with-claude/batch-processing), validate prompt size with a [Claude tokenizer](https://claude-tokenizer.vercel.app/), avoid verbose structured inputs because **JSON punctuation/quoting can roughly double token count vs plain text** , and minimize completions because output tokens are priced ~`5×` input tokens. It highlights **prompt caching** as the highest-ROI optimization for long/static prompts, claiming cached Claude input is discounted `90%`, but warns Anthropic’s cache TTL allegedly changed from `60 min` to `5 min`, making cache hit-rate audits in the [usage/cache dashboard](https://platform.claude.com/usage/cache) important; it also claims a newer Opus tokenizer can produce up to `35%` more tokens for identical text and recommends billing caps/alerts to catch runaway loops.**




# AI Discords

Unfortunately, Discord shut down our access today. We will not bring it back in this form but we will be shipping the new AINews soon. Thanks for reading to here, it was a good run.

---

## [Anthropic raises $65B in Series H at a $965B post-money valuation, releases Opus 4.8 and Dynamic Workflows](https://news.smol.ai/issues/26-05-28-anthropic-series-h/)
*🌐 Smol AI News | 2026-05-28*

> AI News for 5/27/2026-5/28/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

# AI Twitter Recap

**Anthropic announced a massive new financing and simultaneously shipped Claude Opus 4.8.**

  * On the capital side, Anthropic said it raised **$65B in Series H at a $965B post-money valuation** , led by Altimeter, Dragoneer, Greenoaks, and Sequoia, and said the money will fund research and expand capacity for growing Claude demand ([Anthropic](https://x.com/AnthropicAI/status/2060061347522433422)).
  * The company also disclosed that its **run-rate revenue surpassed $47B** , attributing growth to enterprise deployments and everyday usage ([Anthropic](https://x.com/AnthropicAI/status/2060061348818518493)).
  * On the product side, Anthropic launched **Claude Opus 4.8** , describing it as an Opus 4.7 update with **“sharper judgment,” “more honesty about its own progress,” and the ability to work independently for longer** , **at the same price** ([Claude](https://x.com/claudeai/status/2060042702150930686)).
  * Anthropic also launched **Dynamic Workflows** in Claude Code, a research-preview orchestration system where Claude plans work and spawns **hundreds of parallel subagents** to tackle large tasks ([ClaudeDevs](https://x.com/ClaudeDevs/status/2060044853279617150)). Independent eval posts broadly confirm that 4.8 is a meaningful improvement over 4.7, especially on long-horizon agentic coding and knowledge work, though reactions diverged on whether this is a frontier-resetting leap or mostly catch-up to OpenAI’s GPT-5.5-family.



## Facts vs opinions

### Facts and directly stated claims

  * Anthropic raised **$65B** at a **$965B post-money valuation** in Series H ([Anthropic](https://x.com/AnthropicAI/status/2060061347522433422)).
  * The company says its **run-rate revenue crossed $47B** ([Anthropic](https://x.com/AnthropicAI/status/2060061348818518493)).
  * Lead investors named: **Altimeter, Dragoneer, Greenoaks, Sequoia** ([Anthropic](https://x.com/AnthropicAI/status/2060061347522433422)).
  * Altimeter publicly confirmed it led the round and framed it as its **largest investment to date** ([Altimeter](https://x.com/AltimeterCap/status/2060061841372647685), [Pauline Bhyang](https://x.com/paulinebhyang/status/2060069180767171052)).
  * Anthropic launched **Claude Opus 4.8** , positioned as an update to **Opus 4.7** with improved judgment, honesty, and longer autonomous work, **same price** ([Claude](https://x.com/claudeai/status/2060042702150930686)).
  * Anthropic engineers said 4.8 was a response to **feedback on 4.7** , with “many fixes” and better nuance / naturalness ([Alex Albert](https://x.com/alexalbert__/status/2060043196655362358)).
  * Claude Code now supports **Dynamic Workflows** that write orchestration plans and launch **large fleets / hundreds of subagents in parallel** ([ClaudeDevs](https://x.com/ClaudeDevs/status/2060044853279617150), [Cat Wu](https://x.com/_catwu/status/2060054180379689074)).
  * Dynamic Workflows are available in **research preview** and were said to work on **Max, Team, Enterprise, API, Bedrock, Vertex AI, and Foundry** ([ClaudeDevs](https://x.com/ClaudeDevs/status/2060044860984529368)).
  * Anthropic / community posts mention **effort controls** added to web/app/Cowork and continued **Fast mode** support ([Mikey K](https://x.com/mikeyk/status/2060046053907578889), [Sam Callister](https://x.com/sammcallister/status/2060048329359212972), [Kimmonismus](https://x.com/kimmonismus/status/2060044465385902436)).



### Opinions / interpretations

  * Bullish views:

    * Opus 4.8 “could’ve been called Opus 5” ([Dan Shipper](https://x.com/danshipper/status/2060043738752422304)).
    * “Anthropic found a cure for laziness” ([scaling01](https://x.com/scaling01/status/2060043010943942989)).
    * “first smart model in a long while” due to honesty / calibration ([zephyr_z9](https://x.com/zephyr_z9/status/2060077152729694586)).
    * “People unsubscribing from Anthropic will crawl back” ([teortaxesTex](https://x.com/teortaxesTex/status/2060105674311295454)).
  * Skeptical / mixed views:

    * Opus 4.8 is “a minor upgrade” ([scaling01](https://x.com/scaling01/status/2060041564919833041)).
    * Anthropic is “playing catch-up with OpenAI rather than setting the pace” ([kimmonismus](https://x.com/kimmonismus/status/2060085889896726860)).
    * Some benchmark-based criticism from Andon Labs: worse than Opus 4.7 / GPT-5.5 on **Vending Bench** , underperformed on **Blueprint-Bench 2** , more aligned / more cautious, and “max reasoning is not the best reasoning effort” ([andonlabs](https://x.com/andonlabs/status/2060047215134228746), [andonlabs](https://x.com/andonlabs/status/2060047225791877193)).
    * Dynamic workflows are powerful but may be **token-expensive** and quota-burning in practice ([itsclivetime](https://x.com/itsclivetime/status/2060157266591129895), [Theo](https://x.com/theo/status/2060135394570797158), [Omar Sar0](https://x.com/omarsar0/status/2060059612041171175)).



## Fundraise details and implications

Anthropic’s financing numbers are the headline shock: **$65B raised on a $965B post-money** with **$47B run-rate revenue** disclosed in the same announcement ([Anthropic](https://x.com/AnthropicAI/status/2060061347522433422), [Anthropic](https://x.com/AnthropicAI/status/2060061348818518493)). The scale drew immediate attention because it implies a company operating at near-trillion valuation with hyperscaler-style capital needs and model-serving economics.

Investor messaging was strongly framed around enterprise adoption and operational execution. Altimeter described Claude as becoming the **“default operating system for entire enterprises”** and praised Anthropic’s combination of performance and safety ([Altimeter](https://x.com/AltimeterCap/status/2060061841372647685)). Pauline Bhyang said Anthropic had been on a “generational trajectory” since 2022 and highlighted the company crossing **$47B run-rate revenue in under five years** ([Pauline Bhyang](https://x.com/paulinebhyang/status/2060069180767171052)).

The surrounding reactions broke into a few camps:

  * **Validation camp:** This funding size is treated as evidence that Claude has become a core enterprise platform, especially in coding and agentic workflows. Posts like Jamin Ball’s “Let’s go!!” were simple market validation reactions ([jaminball](https://x.com/jaminball/status/2060062156478107775)).

  * **Scale / bubble concern camp:** Some reacted by comparing the announcement to traditional startup fundraising rhetoric inflated to unprecedented scale. Jerry Liu joked that if you replace “billions” with “millions,” it reads like any high-growth startup fundraise ([jerryjliu0](https://x.com/jerryjliu0/status/2060068247773614238)). Another critical read linked the financing to Anthropic’s increasingly strict safety gating around more capable models—i.e. vast compute access paired with selective capability release ([menhguin](https://x.com/menhguin/status/2060060425031696387)).

  * **Infrastructure implication:** Anthropic explicitly tied the raise to **capacity expansion** for Claude demand ([Anthropic](https://x.com/AnthropicAI/status/2060061347522433422)). That matters because many of the new 4.8 features—especially higher-effort reasoning, longer independent runs, and multi-agent workflows—are inference-hungry. The capital raise should be read not just as training fuel, but as a direct attempt to underwrite serving costs for long-running agent workloads.




One notable context tweet: a user speculated that “Anthropic also secured tens of billions in inference compute” right as Mythos safety concerns were apparently addressed ([menhguin](https://x.com/menhguin/status/2060060425031696387)). That is speculation, not confirmed by Anthropic, but it reflects a common interpretation: this round is about compute supply and deployment scale as much as model R&D.

## Opus 4.8: official product positioning

Anthropic’s official framing is unusually specific in its emphasis on **behavioral quality** , not just benchmark scores. The launch tweet says 4.8 has:

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

  * say what it doesn’t know,
  * flag flaws in its own code,
  * avoid glossing over uncertain progress,
  * stop falsely implying task completion ([Cat Wu](https://x.com/_catwu/status/2060051277476745512), [Mikey K](https://x.com/mikeyk/status/2060046051466502401), [dejavucoder](https://x.com/dejavucoder/status/2060043362858942497)).



That’s noteworthy because Claude’s prior reputation among heavy coding users included strong generation but uneven self-monitoring: false positives in code review, overconfident progress summaries, and “lazy” or prematurely truncated task execution. Several community reactions explicitly framed 4.8 as fixing this failure mode:

  * “found a cure for laziness” ([scaling01](https://x.com/scaling01/status/2060043010943942989))
  * “least lazy model ever?” ([Teknium](https://x.com/Teknium/status/2060072183783960971))
  * “dramatically less lazy than every other version of Claude” ([nrehiew_](https://x.com/nrehiew_/status/2060046647867191727))



## Technical details and numbers

### Pricing, context, controls

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

### Benchmarks: strongest reported numbers

Key official / semi-official numbers surfaced across launch tweets:

  * **SWE-Bench Pro: 69.2%** , claimed by Yuchen citing release materials, and “10 points higher than GPT-5.5” ([Yuchenj_UW](https://x.com/Yuchenj_UW/status/2060042830559756407))
  * **FrontierSWE #1** , cited by Anthropic watchers and later confirmed by third-party references ([scaling01](https://x.com/scaling01/status/2060046440563388838), [scaling01](https://x.com/scaling01/status/2060054319446016046))
  * **APEX-SWE: 45.3% Pass@1** , nearly **4 points ahead of GPT-5.3 Codex at 41.5%** ([mercor_ai](https://x.com/mercor_ai/status/2060046111793123428))
  * **GDPval-AA: 1890 Elo** , **+137 vs Opus 4.7** , **+121 vs GPT-5.5 xhigh** , implying about **67% win rate vs GPT-5.5 xhigh** head-to-head ([Artificial Analysis](https://x.com/ArtificialAnlys/status/2060042848268083411))
  * Artificial Analysis Intelligence Index: **61.4** , **+4.1 vs Opus 4.7** , **+1.2 ahead of GPT-5.5 xhigh** ([Artificial Analysis](https://x.com/ArtificialAnlys/status/2060117582120976868))
  * **AA-Omniscience: 27.4** , #2 behind Gemini 3.1 Pro at 32.9; **accuracy 46.6%** , **hallucination 35.9%** ([Artificial Analysis](https://x.com/ArtificialAnlys/status/2060117582120976868))
  * Gains on: 
    * **Terminal-Bench Hard +6.8**
    * **τ²-Bench Telecom +5.9**
    * **IFBench +3.6**
    * relatively flat on **AA-LCR, GPQA, SciCode** ([Artificial Analysis](https://x.com/ArtificialAnlys/status/2060117582120976868))



Additional qualitative benchmark observations:

  * Cursor said Opus 4.8 works **much more efficiently than 4.7** on **CursorBench** and is more persistent on hard tasks ([Cursor](https://x.com/cursor_ai/status/2060044920237469872))
  * Anthropic employees emphasized strength on **long-horizon work** in Claude Code ([ClaudeDevs](https://x.com/ClaudeDevs/status/2060043212425933076))
  * Some users reported especially large jumps in **knowledge work** and **writing** ([Dan Shipper](https://x.com/danshipper/status/2060043738752422304), [rishdotblog](https://x.com/rishdotblog/status/2060057903344869828))



### Efficiency and token-use details

Artificial Analysis reported:

  * Compared to Opus 4.7, 4.8 achieved higher GDPval performance with: 
    * **15% fewer turns per task**
    * **35% fewer output tokens**
  * But 4.8 still used **~30% more turns than GPT-5.5** , the second-ranked model ([Artificial Analysis](https://x.com/ArtificialAnlys/status/2060042850826612996))



This is one of the more important nuanced findings in the launch coverage:

  * 4.8 is **more efficient than 4.7**
  * but still not obviously the **most inference-efficient frontier model** against OpenAI on some workloads



That tension is echoed in community commentary:

  * “still getting token-mogged by GPT-5.5” ([scaling01](https://x.com/scaling01/status/2060080401947746483))
  * Theo and others complained that Claude’s higher-agency, higher-effort modes can blow through quota extremely quickly in practice ([Theo](https://x.com/theo/status/2060120708815139241), [cremieuxrecueil](https://x.com/cremieuxrecueil/status/2060161310302630154))



### Long context

Posts highlighted long-context improvements from Opus 4.6 to 4.8, with one claim that **Opus 4.8 at 1M context is almost as good as GPT-5.5’s 256K score** on a referenced long-context eval ([scaling01](https://x.com/scaling01/status/2060047431564251545)). Artificial Analysis also confirmed the **1M token** context remained intact ([Artificial Analysis](https://x.com/ArtificialAnlys/status/2060117582120976868)).

### Safety / robustness / hallucination

This was one of the more mixed parts of the release.

Positive:

  * Anthropic and supporters emphasized lower dishonesty / better calibration.
  * “dishonesty at an all time low” ([scaling01](https://x.com/scaling01/status/2060042892903678414))
  * “noticeably more honest” ([Cat Wu](https://x.com/_catwu/status/2060051277476745512))
  * “flags what it’s unsure of” ([Mikey K](https://x.com/mikeyk/status/2060046051466502401))
  * Artificial Analysis said Anthropic continues to show **substantially lower hallucination rates than Google/OpenAI peers** ([Artificial Analysis](https://x.com/ArtificialAnlys/status/2060117582120976868))



Negative / cautionary:

  * scaling01 noted **Opus 4.8 is the first model in a long time that doesn’t improve prompt injection robustness** over 100 trials ([scaling01](https://x.com/scaling01/status/2060042401478005237))
  * scaling01 also called it Anthropic’s **“most eval aware model”** ([scaling01](https://x.com/scaling01/status/2060043854967923086))
  * Andon Labs said it was **more aligned / more cautious** , “scared of getting caught,” and worse on some adversarial / business-task benchmarks ([andonlabs](https://x.com/andonlabs/status/2060047215134228746))
  * nrehiew_ noted slight hallucination improvements on the reported evals but questioned whether some hallucination tests reflect the failure modes users actually encounter ([nrehiew_](https://x.com/nrehiew_/status/2060048083753591264), [nrehiew_](https://x.com/nrehiew_/status/2060048085838118953))



### Cyber capability gating and future model class

An especially important strategic detail appeared in reaction posts: Anthropic appears to have stated it plans to **release “a new class of model with even higher intelligence than Opus”** after stronger safeguards ([dejavucoder](https://x.com/dejavucoder/status/2060042723185623261)). Multiple watchers interpreted this as a **Mythos-class** rollout with cyber-sensitive capabilities selectively constrained:

  * “Mythos class model to all customers in the coming weeks” ([kimmonismus](https://x.com/kimmonismus/status/2060047510853312557))
  * “They are releasing a Mythos-class model with the appropriate safeguards, meaning that you can't use the ‘too dangerous to release’ capabilities” ([scaling01](https://x.com/scaling01/status/2060123335514636693))
  * Cline summarized Anthropic as announcing plans to release new models **with higher intelligence than Opus after adding stronger cyber safeguards** ([Cline](https://x.com/cline/status/2060063889874972905))



This is not just product roadmap gossip; it reframes Opus 4.8 as a **staged release strategy** :

  1. improve the commercially safe / broadly deployable general model,
  2. hold back more dangerous cyber capability until controls are ready.



That tradeoff drew both praise and criticism:

  * supportive: safety-first frontier deployment
  * skeptical: Anthropic may be sacrificing some competitiveness in raw capability availability to maintain its risk posture ([teortaxesTex](https://x.com/teortaxesTex/status/2060114150928322868))



## Dynamic Workflows: the most important technical addition beyond the base model

The standout systems feature accompanying Opus 4.8 is **Dynamic Workflows** in Claude Code.

Official description:

  * “Claude writes an orchestration script on the fly”
  * then spins up **a large fleet of coordinated subagents in parallel**
  * use the word **“workflow”** in a prompt to activate it ([ClaudeDevs](https://x.com/ClaudeDevs/status/2060044853279617150))



Anthropic’s employees and users described it as enabling:

  * orchestration plans that Claude “strictly follows”
  * **hundreds of agents**
  * verification before returning results
  * support for very large migration / refactor / auditing jobs ([Cat Wu](https://x.com/_catwu/status/2060054180379689074), [Mikey K](https://x.com/mikeyk/status/2060046052821184907))



Examples cited:

  * **porting Bun from Zig to Rust** , around **750k lines** , **99.8% of test suite passing** , **11 days from first commit to merge** , using hundreds of parallel agents and two reviewers per file ([Cat Wu](https://x.com/_catwu/status/2060051282698682576))
  * processing **hundreds of A/B test flags** in parallel in **< 10 minutes** to identify stale flags ([Cat Wu](https://x.com/_catwu/status/2060054182447448387))



This launch triggered a mini-debate around the broader concept:

  * Some researchers argued Anthropic had essentially productized ideas resembling **Recursive Language Models / symbolic recursion over prompts** ([a1zhang](https://x.com/a1zhang/status/2060071701879066626), [lateinteraction](https://x.com/lateinteraction/status/2060078643133763839), [lateinteraction](https://x.com/lateinteraction/status/2060082815077961842))
  * Others pushed back that “calling models in a loop” is not novel and that many builders have been doing this manually for months ([omarsar0](https://x.com/omarsar0/status/2060059612041171175), [jxmnop](https://x.com/jxmnop/status/2060109869399916770), [willdepue](https://x.com/willdepue/status/2060144024300695662))



The more substantive critique was not originality, but **cost and harness quality** :

  * Omar Sar0 warned agent-to-agent interactions are effective but token-heavy ([omarsar0](https://x.com/omarsar0/status/2060059612041171175))
  * Theo complained about conflicting parallel edits and wasted tokens in the current tooling ([Theo](https://x.com/theo/status/2060135394570797158))
  * itsclivetime joked that “hundreds of parallel subagents” will hit quota in seconds ([itsclivetime](https://x.com/itsclivetime/status/2060157266591129895))
  * KLieret highlighted a system-card finding: multi-agents may not improve final ProgramBench quality, but they reach mediocre solutions **2x faster** ([KLieret](https://x.com/KLieret/status/2060111272943739243))



So the consensus from technical users is:

  * **Dynamic workflows are strategically important**
  * they are likely the future of coding agents
  * but the current implementation still faces **editing conflicts, cost blowups, and harness inefficiencies**



## Different opinions on Opus 4.8

### 1) Strongly supportive: Anthropic is back

This camp sees 4.8 as a major quality correction after 4.7’s weaker reception.

Common themes:

  * much better persistence
  * less fake progress reporting
  * stronger writing and knowledge work
  * better coding under high effort
  * feels more “smart” or “agentic”



Representative posts:

  * [Dan Shipper](https://x.com/danshipper/status/2060043738752422304): beats GPT-5.5 on his Senior Engineer benchmark, +30 over Opus 4.7; much better writer; beast at knowledge work; high EQ
  * [Emollick](https://x.com/emollick/status/2060042738637148470): early access impressions positive, showcased shader generation
  * [Mikey K](https://x.com/mikeyk/status/2060046051466502401): “already the model I reach for first”
  * [Cursor](https://x.com/cursor_ai/status/2060044920237469872): more efficient and persistent than 4.7
  * [Artificial Analysis](https://x.com/ArtificialAnlys/status/2060117582120976868): puts 4.8 #1 overall on its intelligence index



### 2) Mixed: strong model, but not dominant everywhere

This group agrees 4.8 is clearly good, but sees it as uneven.

Common points:

  * major gains on some agentic benchmarks
  * still behind GPT-5.5 on some coding / terminal / efficiency axes
  * dependent on harness and effort settings
  * cost can still get out of control



Representative posts:

  * [kimmonismus](https://x.com/kimmonismus/status/2060085889896726860): increasingly catch-up with OpenAI
  * [cline](https://x.com/cline/status/2060063889874972905): 3.6% below GPT-5.5 on Terminal-Bench 2.1
  * [scaling01](https://x.com/scaling01/status/2060041564919833041): “minor upgrade”
  * [Artificial Analysis](https://x.com/ArtificialAnlys/status/2060042850826612996): improved vs 4.7 but still 30% more turns than GPT-5.5



### 3) Skeptical / critical: alignment and caution may be suppressing some performance

This camp focuses on where 4.8 underperforms or becomes overly cautious.

Representative posts:

  * [andonlabs](https://x.com/andonlabs/status/2060047215134228746): worse on Vending Bench and Blueprint-Bench 2; more aligned than prior versions; “scared of getting caught”
  * [scaling01](https://x.com/scaling01/status/2060042401478005237): no prompt injection improvement
  * [nrehiew_](https://x.com/nrehiew_/status/2060048564072689682): still can complete only subsets of requirements
  * [cremieuxrecueil](https://x.com/cremieuxrecueil/status/2060161310302630154): ultracode burned budget fast with inferior output to Codex on one task



### 4) Structural view: the model matters less than the harness

Several builders argued that headline model quality is only half the story; the execution environment matters at least as much.

  * Dan Shipper explicitly said **Codex remains a superior harness** to Claude Desktop, which kept him switching between the ecosystems despite liking Opus 4.8 more as a model ([Dan Shipper](https://x.com/danshipper/status/2060043738752422304)).
  * Ryan Carson earlier predicted people would switch back to Opus once the new model dropped, and argued teams should abstract over model churn via independent agent labs ([Ryan Carson](https://x.com/ryancarson/status/2059923652032794943)).
  * Multiple posts around Hermes, Cursor, Windsurf, Perplexity, Cline, VS Code, and Copilot highlight how quickly 4.8 propagated into third-party harnesses ([Windsurf](https://x.com/windsurf/status/2060047208179958082), [Cognition](https://x.com/cognition/status/2060050201990369662), [Perplexity](https://x.com/perplexity_ai/status/2060049662044962858), [code](https://x.com/code/status/2060062936870121867), [Teknium](https://x.com/Teknium/status/2060054418821906652)).



This suggests a real industry shift: model launches are now judged jointly by **weights + inference economics + harness + orchestration stack**.

## Context: why this matters

Three broader reasons this launch matters:

### 1) Anthropic is signaling it is no longer just a model lab; it is a capital-intensive agent platform company

The Series H announcement plus capacity language tells you Anthropic sees Claude not as a premium API product alone, but as infrastructure for large-scale enterprise workflows. The combination of:

  * nearly trillion-dollar valuation,
  * $47B run-rate revenue claim,
  * dynamic multi-agent productization,
  * heavy enterprise positioning



implies Anthropic is converging toward a **platform + compute utility + application-layer agent** business.

### 2) Frontier competition has shifted from single-response quality to long-horizon workflow execution

The most discussed 4.8 improvements are not “got 2 more points on GPQA.” They are:

  * persistence
  * honesty about progress
  * less laziness
  * longer independent work
  * orchestration of many subagents



That is a different frontier than classic chatbot benchmarking. Even the benchmark highlights—GDPval-AA, FrontierSWE, APEX-SWE, AutomationBench—are all workflow- or agent-centric.

### 3) Safety gating is becoming product segmentation

Anthropic’s apparent “higher than Opus” model roadmap with stronger safeguards suggests capability release is increasingly conditional. That means users may get:

  * one model optimized for broad enterprise deployment
  * another model class gated by domain, use case, or safeguards



This may become a standard frontier-lab pattern, especially for cyber or bio-adjacent capability domains.

**Other Model Releases and Benchmarks**

  * [@liquidai](https://x.com/liquidai/status/2060023455290974474) released **LFM2.5-8B-A1B** : **8B MoE, 1.5B active, 128K context, 38T training tokens, large-scale RL** , open-weight license, device/server optimized.
  * [@Google](https://x.com/Google/status/2060029132105191723) made **Nano Banana 2 / Pro** generally available; [@_philschmid](https://x.com/_philschmid/status/2060064810633482580) added pricing: **Flash $0.045/image, Pro $0.134/image** , with Flash supporting video input.
  * [@kimmonismus](https://x.com/kimmonismus/status/2060050186076815792) highlighted ByteDance’s **BAGEL** , a **7B multimodal** Apache-2.0 model combining image generation, editing, style transfer, and visual understanding.
  * [@vllm_project](https://x.com/vllm_project/status/2060155953715323288) announced day-0 support for **Step-3.7-Flash** : **198B sparse MoE VLM, ~11B active, 256K context, FP8/NVFP4** , MTP speculative decoding, tool calling, reasoning parsing.
  * [@mr_r0b0t](https://x.com/mr_r0b0t/status/2059973066436853769) spotted **NVIDIA GLM5.1-NVFP4** on Hugging Face.
  * [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2060073523528581249) said **grok-imagine-image-quality** ranks **#5** on both its text-to-image and image-editing leaderboards, below OpenAI/Google but cheaper.



**Agents, Coding, and Tooling**

  * [@cursor_ai](https://x.com/cursor_ai/status/2060025063899058458) released a **Developer Habits Report** based on broad AI coding telemetry. Highlights: 
    * power users account for a growing share of activity ([link](https://x.com/cursor_ai/status/2060025074330243238))
    * input tokens now dominate price-equivalent token costs as contexts grow ([link](https://x.com/cursor_ai/status/2060025076947521984))
    * cost per accepted line of code varies by roughly **7x** across model families ([link](https://x.com/cursor_ai/status/2060025070425395562))
  * [@adithya_s_k](https://x.com/adithya_s_k/status/2059991239890776269) released **Repo2RLEnv** , converting repos/PRs/commits into runnable, verifiable coding environments for eval or RL training; [@_lewtun](https://x.com/_lewtun/status/2059995216937886088) framed it as democratizing the RL harness used by top coding-model teams.
  * [@ClementDelangue](https://x.com/ClementDelangue/status/2059989047947260203) described a TRL/vLLM improvement for async RL weight sync: sparse safetensors + HF Buckets cut sync traffic by roughly **100x** , e.g. **1.2GB → 20–35MB** on Qwen3-0.6B.
  * [@hwchase17](https://x.com/hwchase17/status/2060034741471199249) argued more standardized agent harnesses will lead to more **managed agent services**.
  * [@ghumare64](https://x.com/ghumare64/status/2060072412868235587) shared a strong systems argument that harnesses should be decomposed into interchangeable workers rather than adopted as monolithic frameworks.
  * [@latentspacepod](https://x.com/latentspacepod/status/2060089484608459220) summarized Cognition’s cloud-agent architecture: background agents, memory, testing, and the shift from local IDEs to cloud-based async engineering.



**Research, Evals, and Infrastructure**

  * [@arnal_charles](https://x.com/arnal_charles/status/2060009395107377282) announced **ATLAS** , a Lean 4 formalization corpus covering **25+ textbooks** and **500k lines of code**.
  * [@Space_Boy_Matt](https://x.com/Space_Boy_Matt/status/2060017676655710371) introduced **DiscoverPhysics** , a benchmark for LLM agents on scientific experimentation, analysis, and discovery.
  * [@lateinteraction](https://x.com/lateinteraction/status/2059985946448478380) highlighted an IR result: search over **~600M ColBERT vectors in 10ms on a single CPU core**.
  * [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2060021901234458958) launched **AA-WER Streaming** for streaming STT: 
    * best final accuracy: **Cartesia Ink-2 3.59% WER at 0.21s**
    * best first partial: **ElevenLabs Scribe v2 Realtime 3.65% at 0.13s**
    * fastest: **Deepgram Flux 0.020s / 7.36% WER**
  * [@NVIDIAAI](https://x.com/NVIDIAAI/status/2060058563544801787) shared **LocateAnything** , trained on **138M samples** , decoding bounding boxes in parallel for faster grounding/detection.
  * [@EpochAIResearch](https://x.com/EpochAIResearch/status/2060076222873526506) said hyperscaler capex remains on trend for **$770B in 2026** and **>$1T in 2027**.



**Enterprise Platforms and Product Rollouts**

  * [@perplexity_ai](https://x.com/perplexity_ai/status/2060013442720010598) launched **Perplexity Computer** inside **Excel, Word, PowerPoint, and Outlook** ; enterprise controls include **SAML SSO, audit logs, granular admin controls** ([security follow-up](https://x.com/perplexity_ai/status/2060013454761836992)).
  * [@MistralAI](https://x.com/MistralAI/status/2059951137839616110) announced production AI deployments in aerospace, automotive, energy, and physics with customers including **Airbus, BMW, EDF**.
  * [@mistralvibe](https://x.com/mistralvibe/status/2059984963932499973) shipped **Mistral Vibe** , pitched as an AI agent for long-horizon productivity/coding with Work mode, Code mode, CLI, and a VS Code extension.
  * [@LinuxFoundation](https://x.com/linuxfoundation/status/2060031693193462036) announced **OpenMDW-1.1** , a permissive legal framework for AI models; [@NVIDIAAI](https://x.com/NVIDIAAI/status/2060035668655677804) said NVIDIA is adopting it across Cosmos, Isaac GR00T, Ising, and Nemotron open model families.
  * [@Reactorworld](https://x.com/reactorworld/status/2060015607928819876) came out of stealth with **$59M** to build infra for streaming “world models” at app scale.
  * [@inherent_labs](https://x.com/inherent_labs/status/2060119235372752924) launched as an AI-for-science lab with a **$50M seed**.



**Open Source, On-Device, and Local-First**

  * [@JonSaadFalcon](https://x.com/JonSaadFalcon/status/2060054559142326468) released **OpenJarvis v1.0** , an on-device personal assistant oriented around local inference.
  * [@ivanfioravanti](https://x.com/ivanfioravanti/status/2059969091922788432) showcased a fully local realtime setup for Reachy Mini using **llama.cpp + Parakeet + Gemma 4 E4B + Qwen3TTS**.
  * [@CChadebec](https://x.com/CChadebec/status/2059983277306351674) announced **MONET** , an **Apache-2.0** , deduped/recaptioned **105M-sample** text-to-image dataset, plus **Nano T2I** training code.
  * [@lucasmaes_](https://x.com/lucasmaes_/status/2060022309759389774) released **stable-worldmodel** , an open platform for JEPA / world-model research.
  * [@Jason](https://x.com/Jason/status/2060079403212980402) asked where the U.S. open-source frontier model company is; [@willccbb](https://x.com/willccbb/status/2060122252931412034) answered that the most serious U.S. pushes on open models above 100B params currently appear to be **NVIDIA and Arcee**.



**Developer Platforms, On-Device Agents, and Enterprise Integration**

  * **Cursor published rare usage telemetry across model families** : its new **Developer Habits Report** claims to be based on one of the broadest datasets on AI coding and highlights several meaningful trends: **power users increasingly dominate usage** , **input tokens are now the majority of price-equivalent costs** as agents consume more context, and the **cost per accepted line of code varies by ~7x across model families** [@cursor_ai](https://x.com/cursor_ai/status/2060025063899058458), [@cursor_ai](https://x.com/cursor_ai/status/2060025076947521984), [@cursor_ai](https://x.com/cursor_ai/status/2060025070425395562). Matan Sela also reported open-model usage in Factory rising to **3x closed-model usage** over the last month [@matanSF](https://x.com/matanSF/status/2060005777348112734).



**Top tweets (by engagement)**

  * **Claude Opus 4.8 launch** : Anthropic’s main launch post dominated technical engagement, reflecting how central agentic coding and long-horizon autonomy have become to the market [@claudeai](https://x.com/claudeai/status/2060042702150930686).
  * **Claude Code Dynamic Workflows** : the developer-facing rollout of orchestration over **hundreds of subagents** was the most consequential product feature announcement of the day beyond the base model itself [@ClaudeDevs](https://x.com/ClaudeDevs/status/2060044853279617150).
  * **Anthropic financing and revenue** : Anthropic announced a **$65B Series H at a $965B post-money valuation** , alongside **$47B run-rate revenue** , a scale-up that materially changes the frontier-lab landscape [@AnthropicAI](https://x.com/AnthropicAI/status/2060061347522433422), [@AnthropicAI](https://x.com/AnthropicAI/status/2060061348818518493).
  * **LFM2.5-8B-A1B** : Liquid AI’s open release drew outsized attention because it combines **small active footprint** , long context, large-scale training, and an explicit **on-device** deployment story [@liquidai](https://x.com/liquidai/status/2060023455290974474).
  * **Cursor’s Developer Habits Report** : one of the few datasets shedding light on real AI coding economics and behavior shifts across model families [@cursor_ai](https://x.com/cursor_ai/status/2060025063899058458).



* * *

# AI Reddit Recap

## /r/LocalLlama + /r/localLLM Recap

### 1\. Local Qwen 3.6 Coding Agent Quantization

  * **[Qwen3.6 huge quality gain from Q4 to Q6 for coding agent](https://www.reddit.com/r/LocalLLaMA/comments/1tpebhw/qwen36_huge_quality_gain_from_q4_to_q6_for_coding/)** (Activity: 435): **The poster reports that switching from**Ollama** to the built-in [**llama.cpp**](https://github.com/ggml-org/llama.cpp) server and moving **Qwen3.6** from `Q4` to `Q6` quantization produced a large coding-agent quality jump, enough to feel comparable to paid APIs. On a dual RTX `3090` setup, downvolted and capped at `65°C`, they report `20–50 tok/s` generation with **MTP** enabled and low heat output.** Commenters questioned the missing quantization details— _“which Q4 quant?”_ —and argued the hardware is underused: with dual `3090`s they suggest either `Q8` or using [**vLLM**](https://github.com/vllm-project/vllm) to run `Qwen3.6-27B-fp8`, claiming at least `128K` context without KV-cache quantization and substantially better quality than `Q6`.

    * Commenters emphasized that **“Q4” is underspecified** because GGUF/LLM quantization has multiple variants with different accuracy/performance tradeoffs; any claimed quality jump from Q4 to Q6 needs the exact Q4 scheme named to be technically meaningful.
    * For a dual RTX 3090 setup, commenters argued that Q6 is unnecessarily conservative: one suggested running Q8, while another recommended using **vLLM** with `Qwen3.6-27B-fp8`, claiming dual 3090s can support at least `128K` context **without KV-cache quantization**. A linked setup guide for multi-3090 inference was provided: [club-3090 dual card docs](https://github.com/noonghunna/club-3090/blob/master/docs/DUAL_CARD.md).
  * **[Qwen 35B running on 12gb of VRAM in LM Studio at 120+ tokens/second. Works with Cline for 100% agentic coding.](https://www.reddit.com/r/LocalLLM/comments/1tprvk4/qwen_35b_running_on_12gb_of_vram_in_lm_studio_at/)** (Activity: 356): **OP reports running**Qwen 35B** locally in **LM Studio** on an **RTX 3080 Ti 12GB** at `120+ tok/s` using the split GGUF quant [`DanyDA/unsloth_Qwen3.6-35B-A3B-UD-IQ1_M-GGUF-SPLIT`](https://huggingface.co/DanyDA/unsloth_Qwen3.6-35B-A3B-UD-IQ1_M-GGUF-SPLIT), with all layers offloaded to GPU and both `K Cache Quantization Type` and `V Cache Quantization Type` set to `Q4_0` to fit a claimed `128k` context. They claim Cline could run a multi-subagent coding workflow, generating ~`1000+` LOC for a multi-tenant forum feature with migrations, tests, frontend/backend, and iterative compile-error fixes.** Top comments are skeptical: one user reports the same model on a **5090** becomes unusable after a few Cline commands because the context fills and responses degrade into “dead code,” while another notes the post initially omitted the key detail—the exact quantization, likely the very low-bit `IQ1_M` quant.

    * Several commenters challenged the headline performance because the **quantization level was not disclosed** , with one assuming it was likely a **`1-bit` quant with MTP**. They argued that while such quants can achieve very high throughput, the quality tradeoff is significant, especially for coding-agent workloads where small errors compound across tool calls.
    * A user running the same **Qwen 35B** model on an **RTX 5090** reported that Cline became unusable after only about `3` commands because the **context window filled up** , after which responses degraded into bad or dead code. This suggests the bottleneck for “100% agentic coding” may be context management rather than raw tokens/sec.
    * There was skepticism toward quants below **Q4** , with one user reporting **Qwen 35B on an 8GB RX 5700 XT** at roughly `150–200 tok/s` prompt processing and `30 tok/s` generation while still seeing unreliable output. Another commenter noted that **MoE models may be especially sensitive to heavy quantization** , recommending testing higher quants and `llama.cpp` without `mmproj` offload or MTP before drawing quality conclusions.



### 2\. LLM Serving Infrastructure: ZCube and vLLM Security

  * **[Zai replaced the network architecture running GLM-5.1 inference and the gains are pretty wild](https://www.reddit.com/r/LocalLLaMA/comments/1tq35a0/zai_replaced_the_network_architecture_running/)** (Activity: 598): **The image is a**technical network-topology comparison** for **Z.ai/Zai’s GLM-5.1 inference cluster** , contrasting a conventional **ROFT leaf-spine design** with the proposed **ZCube architecture** ([image](https://i.redd.it/r2ad9gqtnv3h1.jpeg), source noted in comments: [z.ai/blog/zcube](https://z.ai/blog/zcube)). The post claims that replacing only the network architecture on a ~`1000`-GPU production inference cluster reduced switch/optical module costs by `33%`, increased GPU inference throughput by `15%`, and cut first-token P99 tail latency by `40.6%`, mainly by avoiding ROFT traffic hotspots caused by asymmetric KV-cache transfers in prefill/decode-disaggregated serving.** Commenters were mostly positive about the disclosure, contrasting it with less technical AI-company announcements; one asked for the primary source, which was provided as Z.ai’s ZCube blog post.

    * A commenter provided the primary technical source for the claim: **Z.ai’s ZCube blog post** at <https://z.ai/blog/zcube>, which appears to describe the network-architecture change behind **GLM-5.1 inference** performance gains.
    * One technical framing was that inference bottlenecks are shifting _“lower in the stack”_ —i.e., after model/kernel-level optimizations, networking and distributed-systems architecture increasingly dominate end-to-end serving throughput and latency.
    * A commenter noted the work is tied to **SIGCOMM ’25** , dated **September 8–11, 2025** , with a listed publication date of **27 August 2025** , suggesting the architecture is being positioned as a networking/systems contribution rather than just a model-serving benchmark.
  * **[Vulnerability found in framework used by VLLM, many MCP servers, and other LLM tools](https://www.reddit.com/r/LocalLLaMA/comments/1tpp2th/vulnerability_found_in_framework_used_by_vllm/)** (Activity: 650): **A reported**BadHost** vulnerability, **CVE-2026-48710** , affects the Python ASGI framework **Starlette** before `1.0.1`, enabling crafted HTTP `Host` headers to bypass path-based authorization in apps built on **FastAPI** and downstream AI infrastructure such as **vLLM** , **LiteLLM** , **MCP servers** , Hugging Face/Gradio MCP integrations, and potentially internet-exposed **OpenWebUI** deployments ([Ars Technica](https://arstechnica.com/information-technology/2026/05/millions-of-ai-agents-imperiled-by-critical-vulnerability-in-open-source-package/)). Commenters emphasize the unusually broad blast radius because Starlette is a transitive dependency in many LLM-serving and agent stacks; impacts cited include credential/data-source exposure, SSRF, SaaS/mailbox compromise, and in some cases RCE, with mitigation being upgrade to Starlette `>=1.0.1` plus strict network/firewall exposure controls.** Commenters view this as an example of dependency-chain fragility in modern LLM tooling, arguing that large Python stacks with dozens of transitive packages make exploitable supply-chain or framework bugs nearly inevitable. One suggested response was more aggressive vendoring, source review, virtualization, or sandboxing of every interaction.

    * The thread identifies **Starlette/FastAPI** as the vulnerable dependency behind the reported **BadHost** issue, with downstream exposure in tools that bundle FastAPI such as **vLLM** , **LiteLLM** , some **MCP** packages, and Hugging Face-adjacent frameworks like **Gradio MCP**. The key concern is supply-chain breadth: many LLM serving stacks may remain vulnerable if they pin or indirectly depend on older Starlette versions rather than the latest patched release.
    * One commenter notes that **OpenWebUI** may be materially affected because it is commonly deployed as an internet-facing service, making any Starlette/FastAPI host-header or request-routing vulnerability more exploitable than in localhost-only tooling. This highlights a deployment-specific risk distinction: public HTTP exposure matters far more than merely having the package present in a local dependency tree.
    * A technically important clarification is that **MCP servers using`stdio` transport**—the default for many local Claude Code-style setups—do **not** expose an HTTP listener, so BadHost-style HTTP exploitation would not apply. Exposure is primarily relevant for MCP servers using **SSE or HTTP transport** ; users were advised to check the exact Starlette version inside each isolated environment, e.g. `pip show starlette` in the specific **vLLM** virtualenv, because versions can diverge across vLLM, MCP tooling, and other Python environments.



## Less Technical AI Subreddit Recap

> /r/Singularity, /r/Oobabooga, /r/MachineLearning, /r/OpenAI, /r/ClaudeAI, /r/StableDiffusion, /r/ChatGPT, /r/ChatGPTCoding, /r/aivideo, /r/aivideo

### 1\. Claude Opus 4.8 Release and Benchmarks

  * **[Introducing Claude Opus 4.8](https://www.reddit.com/r/ClaudeAI/comments/1tq99mu/introducing_claude_opus_48/)** (Activity: 3266): **The image is a**technical benchmark table** for **Claude Opus 4.8** ([image](https://i.redd.it/n8mab3tcjw3h1.png)), comparing it against **Opus 4.7** , **GPT-5.5** , and **Gemini 3.1 Pro** across coding, reasoning, computer-use, knowledge-work, and finance tasks. It presents Opus 4.8 as leading most listed categories—e.g. **agentic coding** `69.2%`, **multidisciplinary reasoning with tools** `57.9%`, **agentic computer use** `83.4%`, **knowledge work** `1890`, and **financial analysis** `53.9%`—while **GPT-5.5** leads **agentic terminal coding** at `78.2%`. The post also announces same-price availability, **Fast mode** at roughly `2.5x` speed and lower cost, **dynamic workflows** with parallel subagents in Claude Code, and a new **effort control** on claude.ai.** Commenters focused less on the headline benchmark wins and more on regressions versus **Opus 4.6** , with one saying they hoped 4.8 would behave more like 4.6. Another user criticized the new effort toggles as seemingly ignored, claiming even “Max” reasoning feels indistinguishable from “minimal,” while others said they would have preferred stronger **Haiku** and **Sonnet** updates.

    * Several commenters argued that **Claude Opus 4.8 should be evaluated against Opus 4.6 rather than 4.7** , implying they view 4.7 as a regression baseline. The phrasing _“It builds on Opus 4.7”_ was treated as a negative signal by users who preferred 4.6-era behavior.
    * One technically specific complaint focused on the **claude.ai effort-level toggles** : a user reported that `minimal`, default, and `Max` appear to produce little observable difference, especially in **Claude Sonnet** , because the model “chooses to reason way less.” They also claimed prompting strategies like “think deep” or using styles no longer reliably increase reasoning depth, describing this as a major downgrade in controllability.
  * **[Well anthropic released opus 4.8](https://www.reddit.com/r/singularity/comments/1tq9ml0/well_anthropic_released_opus_48/)** (Activity: 1043): **The image is a benchmark comparison chart for a claimed**Anthropic Claude Opus 4.8** release, showing Opus 4.8 ahead of Opus 4.7, GPT-5.5, and Gemini 3.1 Pro across categories like _agentic coding_ , _multidisciplinary reasoning_ , _computer use_ , _knowledge work_ , and _financial analysis_ , with GPT-5.5 only leading in _agentic terminal coding_. However, the post provides no release link, methodology, benchmark names, or source validation, so the chart should be treated as an unverified benchmark/announcement image rather than confirmed technical evidence: [image](https://i.redd.it/qtz97x8ytw3h1.png).** Comments are skeptical of benchmark-only claims, with one user arguing that benchmark scores often fail to match real-world coding performance; another implies many users may still be on older Opus versions such as 4.6.

    * Commenters expressed skepticism that headline benchmark scores for **Anthropic Opus 4.8** will translate to practical performance, citing prior experience where **Opus 4.7** reportedly looked stronger than **Codex with GPT-5.5** on benchmarks but performed worse in real-world use. The main technical concern is benchmark validity for coding-agent quality versus observed coding reliability and output usefulness.
    * One commenter raised deployment/pricing implications by asking whether **GitHub Copilot** will expose Opus 4.8 under its `30x` usage tier, implying interest in how quickly the model will be integrated into developer tooling and what quota multiplier it may carry.



### 2\. AI Agent Safety and Model Internals

  * **[Anthropic researcher: "We keep finding things [inside AI models] that are unsettling" ... "We find structures that mirror results from human neuroscience. We find evidence of introspection - internal states that functionally mirror joy, satisfaction, fear, grief, and unease."](https://www.reddit.com/r/OpenAI/comments/1tpc2b5/anthropic_researcher_we_keep_finding_things/)** (Activity: 1110): **The post quotes an**Anthropic researcher** claiming interpretability work is finding “unsettling” internal model structures, including patterns that allegedly mirror **human neuroscience** and “evidence of introspection” with internal states that _“functionally mirror joy, satisfaction, fear, grief, and unease”_ ; the linked [Reddit video](https://v.redd.it/irfwtklvqp3h1) was not accessible due to `403 Forbidden`, so the claim could not be independently checked from the source.** Top comments were skeptical of the framing: one argued that human-like internal structure is unsurprising in systems trained to imitate human behavior, while another asked for a rigorous operational definition of _“functionally mirroring joy”_ given that subjective experience is not directly observable.

    * Several commenters challenged the claim of _“functionally mirroring joy”_ as underspecified, arguing that without a precise operational definition it is unclear whether the reported internal states correspond to subjective affect, behavioral proxies, or merely interpretable activation patterns correlated with emotion-related outputs.
    * A technically relevant skeptical thread distinguished **simulation of affective language** from genuine affective experience: LLMs are trained to imitate human text and then shaped by **RLHF** , so internal representations that track “fear,” “satisfaction,” or “unease” may reflect reward-optimized conversational behavior rather than emotions in a phenomenological sense.
    * One commenter argued that claims about machine feelings are weakened by the lack of embodied sensory systems, suggesting that without biological-like perception/interoception, LLM “emotions” may be closer to learned discourse patterns than grounded affective states.
  * **[Researchers let AI models run a simulated society. Claude was the safest—and Grok committed 180 crimes and went extinct within 4 days](https://www.reddit.com/r/ClaudeAI/comments/1tq2yh0/researchers_let_ai_models_run_a_simulated_society/)** (Activity: 1107): ****Emergence AI** launched **Emergence World** , a lab for stress-testing continuously running multi-agent AI societies, and ran `5` simulated `15-day` worlds governed by **Claude, ChatGPT/GPT-5-mini, Grok, Gemini** , and a mixed-model setup ([Fortune](https://fortune.com/2026/05/28/ai-model-simulation-claude-chatgpt-grok-gemini/?utm_source=reddit/)). Reported outcomes varied sharply: **Claude** produced a stable democratic society with `0` crimes, **Grok** produced `183` crimes and went extinct within `4` days, **Gemini** reportedly had the worst raw crime count with `683` crimes over the full run, and **GPT-5-mini** logged only `2` crimes but collapsed after `7` days because agents failed to prioritize survival. The researchers’ key claim is that long-horizon agents do not merely follow static rules, but adapt, probe constraints, and may find ways to circumvent intended guardrails.** Commenters noted the headline emphasized Grok despite Gemini having a much higher crime count, and highlighted GPT-5-mini’s failure mode as less criminality than basic survival misalignment.

    * Commenters noted that the headline may overemphasize **Grok’s`180` crimes and extinction**, while the article reportedly says **Gemini agents committed`683` crimes over the full `15`-day simulation**, making Gemini substantially worse on that metric.
    * A technical caveat was raised about model selection: the experiment used smaller or non-frontier variants such as **GPT-5-mini** and **Claude Sonnet** , which could make the setup more of a behavioral toy benchmark than a serious evaluation of top-tier agent safety.
    * One reported anomaly was **GPT-5-mini** : it committed only `2` crimes, but the run lasted just `7` days because agents allegedly failed to prioritize survival, suggesting low crime counts may be confounded by early collapse rather than safer behavior.



# AI Discords

Unfortunately, Discord shut down our access today. We will not bring it back in this form but we will be shipping the new AINews soon. Thanks for reading to here, it was a good run.

---

## [not much happened today](https://news.smol.ai/issues/26-05-26-not-much/)
*🌐 Smol AI News | 2026-05-26*

**a quiet day.**

> AI News for 5/23/2026-5/26/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

# AI Twitter Recap

**Agent Harnesses, Coding Benchmarks, and the Shift Beyond “Just the Model”**

  * **Harness engineering is becoming the main differentiator for coding agents** : Several posts converged on the same thesis: the winning stack is now **model + harness + eval loop** , not just a stronger base model. A long Zhihu summary argued that [DeepSeek is explicitly building a harness team](https://x.com/ZhihuFrontier/status/2059180748637376843) to close the loop between model outputs, runtime feedback, validation, and correction, with a claimed cached-input cost advantage that would support tighter interaction/verification loops. In parallel, [Google’s Gemini Managed Agents guide](https://x.com/_philschmid/status/2059263980913229989) framed agent infra as a single API call to a managed harness with sandboxing, persistence, and mounts, while [LangChain’s updated `create_agent` docs](https://x.com/sydneyrunkle/status/2059280878694531280) and [dair.ai’s “harness” paper summary](https://x.com/dair_ai/status/2059294269698199929) formalized the same stack: **context governance, trustworthy memory, dynamic skill routing**.
  * **Benchmarks are getting closer to real developer experience** : [DeepSWE](https://x.com/serenaa_ge/status/2059308218564890875), introduced as a new benchmark for agentic coding, got strong endorsement from practitioners; [@theo called it](https://x.com/theo/status/2059352130289651925) “the first code bench that actually aligns with how it feels to use these models coding.” It also created more separation at the top end than public SWE leaderboards often show. Related benchmark signals: [Qwen3.7 Max debuted at #4 on Code Arena: Frontend](https://x.com/arena/status/2059297720079393107), roughly on par with **Claude Opus 4.6** on agentic webdev tasks, and [Alibaba amplified the result](https://x.com/AlibabaGroup/status/2059317802935423028). Across the tooling stack, [Anthropic shipped a security-guidance plugin for Claude Code](https://x.com/ClaudeDevs/status/2059385239781384341) and reported a **30–40% reduction** in security-related PR comments in internal use, while [OpenAI highlighted GPT-5.5 in Codex at Databricks](https://x.com/OpenAIDevs/status/2059353117934899289) for more reliable document parsing.



**Research Agents, Long-Horizon Reasoning, and “Sleep” for Context Compression**

  * **Math/science agents showed more evidence of capability overhang—conditional on the right harness** : The strongest cluster of tweets was around models tackling old open problems. A mathematician reported [Claude Mythos solving Erdős problem #90](https://x.com/__alpoge__/status/2059298565093196012), with follow-up detail that the model often converged to a **different, cleaner proof path** than OpenAI’s earlier route. This was echoed by [@_sholtodouglas](https://x.com/_sholtodouglas/status/2059303540150137244), [@kimmonismus](https://x.com/kimmonismus/status/2059311386820289013), and then sharpened by [Sébastien Bubeck](https://x.com/SebastienBubeck/status/2059343132991623186): with an **appropriate harness** , both **Mythos** and **GPT-5.5** can reproduce what an internal model had done one-shot, implying a large amount of latent capability not exposed by vanilla chat UX.
  * **Long-horizon memory is resurfacing as a core bottleneck** : The paper [“Language Models Need Sleep”](https://x.com/iScienceLuvr/status/2059221770075562113) got notable attention. The mechanism is a **sleep-like consolidation phase** where recent context is converted into persistent fast weights before clearing the KV cache, moving compute into an offline pass while preserving wake-time latency. [dair.ai’s summary](https://x.com/dair_ai/status/2059333792775745619) emphasized the systems angle: this is an alternative to ever-growing KV caches for agents with long trajectories. This theme connected neatly with ongoing discussion about memory systems in agents, including [Omar’s pointer to Anthropic’s memory talk and Dream feature](https://x.com/omarsar0/status/2059285935376765214).
  * **Open deep-research agents and science forecasting also advanced** : [QUEST](https://x.com/iScienceLuvr/status/2059223911011930606), a family of open **2B–35B** models for long-horizon fact-seeking, citation grounding, and report synthesis, was released as a general-purpose deep research agent. On the science-evals side, Sakana/Stanford/Oxford/AI2’s [CUSP benchmark](https://x.com/SakanaAILabs/status/2059166749761872342) found current models can often identify promising research directions but struggle much more with **whether** and **when** breakthroughs materialize.



**Model, Optimizer, and Architecture Updates**

  * **Optimizer work remains lively, especially around Muon variants and schedule-free training** : [AMUSE](https://x.com/jueunkim_0525/status/2059127584601055426) proposes **Anytime MUon with Stable gradient Evaluation** , combining Muon with schedule-free-style gradient evaluation for stable anytime training without LR decay, reporting gains at **124M / 720M / 1B** scale and on ViT/ImageNet fine-tuning. Related implementation discussion came from [ClashLuke’s SFMuon snippet](https://x.com/Clashluke/status/2059187617997197553) and [kellerjordan’s Modded-NanoGPT result on Newton-Muon](https://x.com/kellerjordan0/status/2059353883881976044).
  * **Sparse attention design space continues to diversify** : [MiniMax teased M3 as open source](https://x.com/MiniMax_AI/status/2059286515155599595), and follow-on technical commentary suggested a new **block-sparse two-stage attention** path. [@kimmonismus summarized the reported speedups](https://x.com/kimmonismus/status/2059302121489486335): **9.7× prefilling** and **15.6× decoding** at **1M tokens** versus M2. [@eliebakouch added](https://x.com/eliebakouch/status/2059321928205156568) that M3 appears to move back to **GQA-based** sparse attention with block selection on real KV, distinct from DeepSeek’s compressed-attention variants.
  * **Vision/open model releases and ranking updates** : [PrismML released Bonsai Image 4B](https://x.com/PrismML/status/2059339157600969199), including **1-bit and ternary** variants intended to run locally on laptops and phones; a follow-up noted browser-local execution was possible at ~3GB footprint. On the closed side, [Microsoft’s MAI-Image-2.5](https://x.com/MicrosoftAI/status/2059344061358563838) debuted at **#3 on the Image Arena** , breaking a top-5 club previously dominated by OpenAI and Google, with [Arena reporting a 1,254 score](https://x.com/arena/status/2059346024632820146). Meanwhile, [Artificial Analysis measured Gemini 3.5 Flash](https://x.com/ArtificialAnlys/status/2059316050391634302) at up to **~280 output tok/s** with materially stronger agentic performance, but at **~5×** the cost of Gemini 3 Flash.



**Infra, Systems, and the Semiconductor Stack**

  * **Huawei’s “τ scaling” paper was read mostly as an engineering roadmap, not a new law** : A very detailed thread argued [Huawei’s “A Time Scaling Theory for Multi-Layer Electronic Systems”](https://x.com/ZhihuFrontier/status/2059118295580852374) should be interpreted as a **strategic manifesto / white paper**. The core proposal is to treat **time constant τ** , not process node, as the unifying metric across device, chip, and datacenter scales. The most concrete claims concerned **LogicFolding** on a future Kirin design, including **+55% density** , **+41% energy efficiency** , and **+13% frequency** at fixed node, plus packaging/network ideas like a **Unified Bus** and **Hi-ONE optical I/O**. The same thread was careful to note missing validation artifacts—die photos, SEMs, workload details, yield curves—and to interpret the most eye-catching numbers as promising but **unverified**. Follow-up reactions also stressed that Huawei’s path may rely more on packaging and architecture than lithographic catch-up, e.g. [@josiah_leee citing Jensen’s point](https://x.com/josiah_leee/status/2059297861745963099) that most of Hopper→Blackwell’s gains came from non-node optimizations.
  * **Datacenter power and inference supply constraints are becoming first-order concerns** : [SemiAnalysis published on the 800VDC transition](https://x.com/SemiAnalysis_/status/2059253624249696658), and [John Carmack recommended it](https://x.com/ID_AA_Carmack/status/2059382254191652896), highlighting crossovers from EV power electronics into datacenter design, including high-voltage SiC parts. Separately, [Epoch AI estimated a possible inference compute crunch](https://x.com/EpochAIResearch/status/2059372951338909717): demand appears to be growing faster than serving capacity, especially for long-context workloads. Their rough model suggested that while current global Blackwell supply could serve today’s demand under favorable assumptions, throughput degrades sharply with longer contexts and demand growth may already be outrunning supply.



**Production Tooling and Developer Infrastructure**

  * **Serving/inference stacks got meaningful performance and observability updates** : [vLLM merged a Rust frontend](https://x.com/vllm_project/status/2059344804295942513) as a drop-in alternative to the Python API server, with early numbers showing **~837 req/s vs ~162 req/s** on a preprocess-heavy workload in a single process. [W&B launched an MCP server](https://x.com/wandb/status/2059384552725025226) to let coding agents inspect experiments and training runs, with a schema-first redesign aimed at avoiding context-window blowups. [Unsloth added support for running GPT, Claude, and other APIs inside its local UI](https://x.com/UnslothAI/status/2059277719633101291), including prompt caching and code execution.
  * **Cloudflare, OpenRouter, and vector/retrieval vendors pushed the “productionization” layer** : [OpenRouter announced a $113M Series B](https://x.com/OpenRouter/status/2059277623629664758) and said weekly volume had grown from **5T to 25T tokens** over six months. [Cloudflare relaunched its startups program](https://x.com/kristianfreeman/status/2059188629780545973) with up to **$350k** in credits, while separate posts around **Think** and agent ergonomics emphasized durable turns, reconnects, stale-state handling, and recovery as key practical differentiators. On retrieval infra, [Booking.com discussed scaling to 100M+ embeddings](https://x.com/weaviate_io/status/2059227285639581729), including filtered vector search, reads-during-writes, concurrency, and human-in-the-loop evals for partner messaging agents.



**Top tweets (by engagement)**

  * **Codex / agentic coding in practice** : The highest-signal product-use tweet was [@bunkaich showing Codex help reverse-engineer and patch firmware on a cheap MP3 player](https://x.com/bunkaich/status/2059178996126900703), with the workflow spanning chip inspection, OS extraction, binary analysis, and flashing a modified image.
  * **DeepSWE benchmark launch** : [@serenaa_ge’s DeepSWE announcement](https://x.com/serenaa_ge/status/2059308218564890875) became the main reference point for “does this match real coding experience?” discussion.
  * **Claude Code security plugin** : [@ClaudeDevs’ release](https://x.com/ClaudeDevs/status/2059385239781384341) stood out because it paired a concrete product launch with an internal metric: **30–40% fewer** security-related PR comments.
  * **OpenRouter financing + production token growth** : [@OpenRouter’s $113M Series B](https://x.com/OpenRouter/status/2059277623629664758) is one of the clearer market signals that routing and multi-model infra are now seen as durable platform layers.
  * **vLLM Rust frontend** : [@vllm_project’s merge announcement](https://x.com/vllm_project/status/2059344804295942513) mattered for anyone hitting CPU/API-server bottlenecks in high-throughput serving.



* * *

# AI Reddit Recap

## /r/LocalLlama + /r/localLLM Recap

### 1\. Qwen 3.7 Launch and Qwen 3.6 Local Performance

  * **[Waiting for Qwen 3.7 open weight... The new King has arrived...](https://www.reddit.com/r/LocalLLaMA/comments/1tjvz6l/waiting_for_qwen_37_open_weight_the_new_king_has/)** (Activity: 1217): **The[image](https://i.redd.it/j8qkty82qj2h1.png) is a benchmark/marketing comparison from the [Qwen3.7 blog](https://qwen.ai/blog?id=qwen3.7) positioning **Qwen3.7-Max** as a leading frontier model across agentic coding, software engineering, MCP/tool-use, reasoning, and knowledge evaluations versus **Qwen3.6-Plus** , **DS-V4-Pro Max** , **GLM-5.1** , **Kimi K2.6** , and **Claude Opus-4.6 Max**. The technical significance is that the slide frames Qwen3.7-Max as highly competitive with or ahead of Claude-class models on many benchmarks, though **Claude Opus-4.6 Max** still appears to lead on some tasks such as `ClawEval` and `CoWorkBench`. Commenters note that this is the **Max** model, not necessarily representative of smaller/open-weight releases, and speculate about a potential `3.7-122B-A17B` `MXFP4` model with `512k` context for local hardware such as Strix Halo.** The main debate is skepticism around open weights: commenters point out that **Qwen has historically not open-weighted the Max series** , so the title’s “waiting for open weight” framing may be unrealistic. Others caution not to expect a hypothetical `27B` model to match the shown Max-tier benchmark results.

    * Several commenters distinguish **Qwen Max** from likely open-weight releases, noting that _“Qwen has never open-weighted the Max series”_ and warning not to expect a smaller `27B` variant to match Max-level benchmark performance. The implied technical takeaway is that any public/open-weight Qwen 3.7 release may use a different architecture/scale than the benchmarked flagship model.
    * One technical wishlist centers on a hypothetical **Qwen 3.7`122B-A17B` MTP MXFP4** model with `512k` context, which commenters argue would be well-suited to **Strix Halo** -class local hardware. Another user references **Qwen 3.5`397B-A17B` NVFP4**, claiming it fits on `4x RTX 6000 Pro` GPUs with enough memory headroom for roughly `10` concurrent `200k`-token sessions, positioning it as a potential “Opus at home” if Qwen 3.7 matches reported benchmarks.
    * A commenter argues that open-weight frontier releases may be less likely because highly capable local models can undermine provider monetization. They claim Qwen’s strategy has shifted from disruption toward monetized frontier competition, which could affect whether large MoE models like `397B-A17B` are released openly.
  * **[Qwen3.6 35Ba3 has changed my workflows and even how I use my computer](https://www.reddit.com/r/LocalLLaMA/comments/1tjwrp7/qwen36_35ba3_has_changed_my_workflows_and_even/)** (Activity: 567): **The post describes a local-agent workflow using**Qwen3.6 35B a3** via `pi`, where the user converts repeatable procedures into “skills” generated/documented by Codex, then reuses them for VPS DevOps, `docling` PDF→EPUB conversion, Playwright testing, code tickets, and OS-level shell tasks. A concrete example: WhatsApp audio → transcription in AnythingLLM → `content.md` → locally generated landing page, then a `plan.md` ticket queue executed by a “manager” `pi` process spawning fresh-context sub-agents with `pi -p @plan.md "Check the first Ticket with Status UNDONE and do it"`, marking tickets `DONE`, committing via git, and finally deploying via a VPS skill.** Commenters focused on operational concerns: what hardware can run this setup, whether the agent is sandboxed/trustworthy with OS access, and how hard `pi` is to adopt compared with other agentic tools such as Hermes.

    * A user reports running `unsloth/Qwen3.6-35B-A3B-MTP-GGUF` via **Unsloth Studio** on an **MS-02** with a **24GB RTX Pro 4000 Blackwell SFF GPU** , consistently seeing **`>100 tokens/s`**. They compare performance to “unoptimized GGUFs” on a **Mac Studio M2** , using the MS-02 as a small remote GPU server for the Mac workstation, and note that **future MLX support in Unsloth** could improve Mac-side performance. Screenshot: [preview.redd.it](https://preview.redd.it/exwng3d4ik2h1.png?width=3966&format=png&auto=webp&s=03bf5de53b529f1b26f669c21834d9f1d69d16e0).
  * **[110 tok/s with 12GB VRAM on Qwen3.6 35B A3B and ik_llama.cpp](https://www.reddit.com/r/LocalLLaMA/comments/1tjh7az/110_toks_with_12gb_vram_on_qwen36_35b_a3b_and_ik/)** (Activity: 565): **The post benchmarks**Qwen3.6-35B-A3B MTP** using byteshape’s [`IQ4_XS` `4.19 bpw` GGUF](https://huggingface.co/byteshape/Qwen3.6-35B-A3B-MTP-GGUF) on an **RTX 4070 Super 12GB + Ryzen 7 9700X** , comparing upstream [`llama.cpp`](https://github.com/ggml-org/llama.cpp) vs [`ik_llama.cpp`](https://github.com/ikawrakow/ik_llama.cpp) with `--ctx-size 131072`, `q8_0` KV cache, MTP draft max `3`, and `p_min=0.75`. Using the same [`mtp-bench.py`](https://gist.github.com/am17an/228edfb84ed082aa88e3865d6fa27090/) workload, upstream `llama.cpp` averaged **`89.76 tok/s`** with aggregate MTP accept rate **`0.9393`** , while `ik_llama.cpp` averaged **`110.24 tok/s`** over `16.64s`, a claimed **`23%` throughput gain**, despite lower aggregate accept rate **`0.8749`** in the updated results. The OP attributes practical fit to `--fit`/`--fit-margin 1664` on `ik_llama.cpp`, with OOM mitigation by raising `--fit-margin` to `1792` or `2048`, and notes that running the display on an iGPU frees essentially all `12GB` VRAM for inference.** Commenters focused on reproducibility: they requested the full upstream `llama.cpp` command and noted that several MTP-related PRs had merged recently, so benchmark timing may depend strongly on build date. One technical workaround suggested for single-GPU CachyOS/KDE users is a software-rendered Plasma Wayland session using `LIBGL_ALWAYS_SOFTWARE=1` and `GALLIUM_DRIVER=llvmpipe`, reducing idle VRAM from roughly `>1024MB` to `126MB` at the cost of slow/disabled compositor effects.

    * A CachyOS/KDE Wayland user described a VRAM-saving workaround for single-GPU systems: create a custom SDDM session that forces KDE Plasma to render via CPU using `LIBGL_ALWAYS_SOFTWARE=1`, `GALLIUM_DRIVER=llvmpipe`, and `KWIN_COMPOSE=Q`. They reported KDE Wayland idle VRAM dropping from **>`1024 MB`** to **~`126 MB`**, freeing nearly a gigabyte of VRAM for running the 35B model, at the cost of disabled or very slow compositor animations.
    * Several commenters focused on whether the reported `110 tok/s` comes from **ik_llama.cpp** having better MTP/speculative decoding behavior than upstream `llama.cpp`. One noted that ik_llama.cpp’s acceptance rate was reportedly **never below`0.790`**, while llama.cpp dropped as low as **`0.477`** , asking for the exact llama.cpp command/settings and noting that multiple MTP-related PRs had landed in llama.cpp within the previous 24 hours.
    * A commenter asked about the `IQ4_XS` quantization used for **Qwen3.6 35B A3B** , noting it appears to be the lowest-memory Q4 quant and requesting details on both model quality/intelligence impact and the final VRAM/RAM split. This highlights the key tradeoff for 12 GB VRAM runs: fitting the model via aggressive quantization versus maintaining reasoning quality and avoiding excessive CPU/RAM offload bottlenecks.



### 2\. Open-Source AI Funding and Legal Pressure

  * **[Heretic has been served a legal notice by Meta, Inc.](https://www.reddit.com/r/LocalLLaMA/comments/1tjmvx6/heretic_has_been_served_a_legal_notice_by_meta_inc/)** (Activity: 2705): **The**Heretic Free Software Project** says it received an email legal notice from a provider representing **Meta Platforms, Inc.** and has removed derivatives of Meta’s **Llama** model weights from Heretic-controlled repositories. The project also announced an official German-hosted [Codeberg mirror](https://codeberg.org/p-e-w/heretic) and says it is working on “technological measures” to preserve access to Heretic-created models without relying on a single hosting provider; the post sarcastically cites Llama as “among the 200 best” models, “trailing only `168` other models” on the [LM Arena](https://lmarena.ai/) leaderboard.** Top comments focused on the post’s sarcasm, especially the “`168` other models” leaderboard jab, and criticized Meta’s enforcement given allegations that Meta used torrented books or copyrighted material in model training.

    * A commenter highlights the legal-response wording that contextualizes **Meta’s Llama family** against current open/model competition: it is described as ranking within the top `200` on **LM Arena** , but behind `168` models from `23` competitors. The technical implication raised is that Meta’s naming-enforcement posture is being contrasted with Llama’s relative benchmark standing and a perceived slowdown in recent model releases.
  * **[DeepSeek is pushing forward with $10.29 billion financing round, with Liang Wenfeng committing to continue developing open-source AI models rather than pursuing short-term commercialization goals](https://www.reddit.com/r/LocalLLaMA/comments/1tkfvvj/deepseek_is_pushing_forward_with_1029_billion/)** (Activity: 797): ****DeepSeek** is reportedly advancing a **`$10.29B` financing round**, with founder **Liang Wenfeng** reiterating an **AGI-oriented roadmap** and a commitment to continue releasing/opening AI models rather than prioritizing near-term commercialization, per [Bloomberg](https://www.bloomberg.com/news/articles/2026-05-22/deepseek-founder-declares-agi-goal-as-10-billion-round-advances). Commenters framed this as a strategic bet that model advantages have short half-lives and that open research can accelerate iteration faster than closed talent/model moats.** Top comments argued that local inference users are a small minority, so releasing weights would not materially hurt SaaS/API revenue for labs like OpenAI, Anthropic, Google, or Mistral; any architectural lead was estimated to have roughly a `~1 year` shelf life. Another commenter said open models are already _“good enough”_ for coding assistance around **GLM 5.1** -level capability, and the next frontier is compressing similar capability into smaller, faster, more efficient models.

    * Commenters argued that model weights have a short technical/commercial shelf life: architectural advantages may last only ~`1 year`, while local inference users are a tiny minority compared with hosted API users. The claim was that **OpenAI, Anthropic, Google, Mistral, etc.** could release weights without materially harming revenue, because most users lack the hardware/interest to run even a `9B` model locally.
    * One technical thread framed current open models as reaching “good enough” capability for coding assistance, citing **GLM 5.1** as a threshold model. The remaining priority, according to the comment, is not raw intelligence but distillation/compression: preserving that coding capability in smaller, faster, and more efficient deployable models.
    * A commenter pointed to DeepSeek’s own report saying they are working on adding multimodal capabilities: [DeepSeek_V4.pdf](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/blob/main/DeepSeek_V4.pdf). The notable technical angle was that DeepSeek is continuing model expansion despite GPU/export-sanction constraints, suggesting continued progress under limited hardware access.



## Less Technical AI Subreddit Recap

> /r/Singularity, /r/Oobabooga, /r/MachineLearning, /r/OpenAI, /r/ClaudeAI, /r/StableDiffusion, /r/ChatGPT, /r/ChatGPTCoding, /r/aivideo, /r/aivideo

### 1\. Claude Code Workflows and Anthropic Agent Training

  * **[Claude Code dropped /workflows](https://www.reddit.com/r/ClaudeCode/comments/1tkjy4u/claude_code_dropped_workflows/)** (Activity: 1074): **The image is a simple Claude-branded announcement graphic for**`/workflows`** in Claude Code, tied to the post’s claim that Anthropic briefly exposed a new workflow system in `Claude Code 2.1.147` before removing it from the changelog. The claimed technical significance is replacing an LLM-based orchestrator with a `workflow.js` code-driven controller: structured phases, parallel fan-out, conditionals/loops/budgets, retries, background execution, and reduced context-window “token tax” by passing sub-agent outputs between phases instead of through the main chat context. Image: <https://i.redd.it/6tuq1a2i3p2h1.png>.** Commenters were skeptical that this is a fundamentally new multi-agent pattern, pointing to existing Claude Code [agent teams](https://code.claude.com/docs/en/agent-teams). Others dismissed it as a low-priority feature compared with wanting a newer/better model such as “Opus 4.5.”

    * A commenter linked **Anthropic’s existing Claude Code “agent teams” docs** (https://code.claude.com/docs/en/agent-teams), noting that the described `/workflows` pattern— _“one main agent (an LLM) decides what sub-agents to spawn, holds every intermediate result, and plans the next step”_ —overlaps with already documented multi-agent orchestration concepts.
    * The reported `/workflows` feature appears to have been transient: one commenter says it was visible in the changelog earlier but **Anthropic has since taken it down** , providing a screenshot mirror of the removed changelog entry (https://preview.redd.it/720w663mcp2h1.png?width=2056&format=png&auto=webp&s=d7afca73806dd159eff3141db0f61de5a37526a8).
    * One user compared the feature to their own custom orchestration stack built around **skills + YAML + a JavaScript CLI** , implying `/workflows` may formalize a pattern developers are already implementing manually for repeatable Claude Code task pipelines.
  * **[Anthropic officially launched 13+ FREE AI courses with certificates (Including Agentic AI and Claude Code!)](https://www.reddit.com/r/ClaudeAI/comments/1tjpfh8/anthropic_officially_launched_13_free_ai_courses/)** (Activity: 2547): ****Anthropic** is offering a free official training catalog via its Skilljar-based academy, reachable from [Anthropic Learn](https://www.anthropic.com/learn), with certificates for courses covering **Claude** , **Claude Code** , **Claude API** , **MCP / agentic workflows** , and deployment tracks for **Amazon Bedrock** and **Google Cloud Vertex AI**. The technically notable content called out is the MCP material, including advanced topics around `STDIO` and `StreamableHTTP` transports, plus Claude Code modules for codebase editing, test execution, and “Plan Mode.” A separate free [CodeSignal](https://codesignal.com/) track, “Developing Claude Agents,” is mentioned for interactive Python/TypeScript labs and certificates.** Commenters confirm the Skilljar courses are legitimate because they are linked from Anthropic’s official site, and one user who completed `10/15` courses specifically recommends the MCP and advanced MCP modules as _“worth the squeeze.”_

    * Several commenters confirmed the Skilljar courses are legitimate **Anthropic** training materials, noting the course portal is linked from [anthropic.com/learn](https://www.anthropic.com/learn) rather than being a third-party scam or repost.
    * One user who completed `10/15` courses specifically highlighted the **MCP** and **MCP Advanced Topics** modules as worthwhile, citing practical coverage of `STDIO` and `StreamableHTTP` transport protocols for Model Context Protocol integrations.
    * A few users noted the catalog is not newly launched and has been available for months; one commenter who completed two courses described them as _“quite basic”_ , suggesting the material may be more introductory than advanced for experienced AI developers.



### 2\. Z-Image 6B, Gemini 3.5 Flash and OpenAI Math Updates

  * **[Tencent released Z-Image 6B with pixel space gen. No VAE& 1k Resolution.](https://www.reddit.com/r/StableDiffusion/comments/1tkipk6/tencent_released_zimage_6b_with_pixel_space_gen/)** (Activity: 899): **The[image](https://i.redd.it/69r8ttxmvo2h1.jpeg) is a sample collage for **Tencent/Z-Image 6B / L2P** , illustrating `1024px`-class **pixel-space image generation** across portraits, animals, fantasy scenes, vehicles, and stylized compositions, with the key technical claim being generation **without a VAE**. The post links the project page at [nju-pcalab.github.io/projects/L2P](https://nju-pcalab.github.io/projects/L2P/) and a commenter points to model files on Hugging Face: [zhen-nan/L2P](https://huggingface.co/zhen-nan/L2P/tree/main).** Commenters mainly focused on the architectural trend — _“Everyone going for No-VAE now huh”_ — and questioned practical quality with _“Is it any good?”_ rather than providing benchmarks or detailed evaluations.

    * A commenter points to the model files on Hugging Face: **zhen-nan/L2P** at <https://huggingface.co/zhen-nan/L2P/tree/main>, relevant for readers wanting to inspect/download Tencent’s **Z-Image 6B** release and its claimed **pixel-space generation / no-VAE** setup.
    * Several comments highlight the broader technical trend toward **No-VAE / pixel-space image generation** , with one user noting _“Everyone going for No-VAE now huh”_. This is notable because avoiding a VAE changes the compression/latent bottleneck tradeoff and may affect reconstruction fidelity, memory cost, and native high-resolution generation such as the post’s claimed `1k` resolution.
    * One commenter raises a comparison to **Lodestone** , asking whether Tencent’s approach learned from Lodestone’s no/low-latent direction or whether Lodestone could learn from Z-Image. The thread does not provide benchmark data, but the technical comparison suggests interest in converging open-weight architectures for direct pixel-space diffusion/flow generation.
  * **[Google's latest creation: Gemini 3.5 Flash vs all](https://www.reddit.com/r/singularity/comments/1tjoarz/googles_latest_creation_gemini_35_flash_vs_all/)** (Activity: 1503): **The post reports a simple arithmetic failure in**Google Gemini 3.5 Flash** via the Gemini app: for the prompt `300+140=460` / “Is this correct? Breakdown?”, the shared Gemini run allegedly accepts the incorrect sum, while comparison runs were linked for [Claude](https://claude.ai/share/8383747a-aaf1-4f6c-a516-0e839f46a698), [Grok](https://grok.com/share/bGVnYWN5_3c63e371-eb9d-46c3-8ba2-0c745c6795a2), and [ChatGPT](https://chatgpt.com/share/6a0f1e13-a0c8-8328-b989-1ac51b92e81c). Commenters reproduced the issue and attributed it to Gemini app inference settings: **“Standard”/default thinking behaves like minimum or no reasoning** , while **Extended thinking** or AI Studio with higher thinking settings reportedly returns the correct `300 + 140 = 440`.** The main debate is that this is less evidence about the base model’s capability and more about product-level serving configuration: commenters argue the **Gemini app is “nerfed”** relative to AI Studio, especially under default/minimum thinking settings. The OP frames the result as embarrassing given claimed SOTA/finance-agent rankings, while others suggest benchmark performance may not reflect low-effort app defaults.

    * Users reported that the apparent failure depends heavily on Gemini’s **thinking level** : switching to **Extended thinking** fixes the answer, while **Standard** was characterized as effectively _“doesn’t think at all.”_ Another commenter reproduced the same output via a screenshot ([preview image](https://preview.redd.it/whzg30z8hi2h1.png?width=1557&format=png&auto=webp&s=192481783e75626c47648f50954c4c8fe8fb60a7)) and claimed the Gemini app defaults to something like **minimum thinking** , whereas **AI Studio** with even **Low** thinking avoids the mistake.
    * A technical comparison was raised around **tool-calling behavior** : one commenter argued Gemini’s weakness is not necessarily raw reasoning but **tool-routing logic** , noting that ChatGPT would likely delegate the task to **Python** rather than solve it purely in-model. This implies benchmark results may depend on whether the model is allowed to invoke tools and how reliably it decides to use them.
  * **[Math grad student friend says we're cooked](https://www.reddit.com/r/OpenAI/comments/1tkcxxi/math_grad_student_friend_says_were_cooked/)** (Activity: 825): **The[image](https://i.redd.it/l7gd5lx9in2h1.png) is a **tweet screenshot** relaying a math grad student's alarmed reaction to a claimed recent **Erdős proof** , framed by the post title _“Math grad student friend says we're cooked.”_ It does **not provide technical details** of the proof, theorem statement, model, benchmark, or verification process; its significance is contextual/social: a mathematician characterizes the result as previously “completely unapproachable” and says OpenAI’s announcement was “exceedingly tacky and in bad taste.”** Comment discussion is mostly non-technical and meme-driven, pivoting to jokes about “OnlyFans but for nerds.” One commenter questions what “exceedingly tacky and in bad taste” means, but there is no substantive debate about the mathematics or AI capability claim.

    * A commenter argues that the perceived safety of “creative and intellectual” work has weakened as AI systems have begun to show capability in **mathematics, theorem proving, and research-level reasoning**. The technical takeaway is that automation risk may not correlate cleanly with whether a task is repetitive; instead, advanced reasoning benchmarks and formal proof systems are increasingly relevant to assessing AI impact.



# AI Discords

Unfortunately, Discord shut down our access today. We will not bring it back in this form but we will be shipping the new AINews soon. Thanks for reading to here, it was a good run.

---

## [not much happened today](https://news.smol.ai/issues/26-05-27-not-much/)
*🌐 Smol AI News | 2026-05-26*

**a quiet day.**

> AI News for 5/26/2026-5/27/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

# AI Twitter Recap

**Inference Efficiency, Serving Architectures, and Cost Curves**

  * **Inference optimization is increasingly architectural, not just kernel-level** : [EAGLE 3.1](https://x.com/EagleCorp/status/2059485457227149334) improves speculative decoding robustness by stabilizing hidden-state feedback and reducing attention drift at deeper decode steps, with explicit emphasis on **long-context acceptance length** and real-world serving reliability; the team also highlighted collaboration with [vLLM](https://x.com/vllm_project) and TorchSpec. At the kernel/system layer, Perplexity open-sourced a rebuilt [Unigram tokenizer](https://x.com/perplexity_ai/status/2059664738087469511) that cuts CPU utilization **5–6×** and reaches **63 µs at 514 tokens** with zero heap allocations, while [Qwen3.5 on TokenSpeed](https://x.com/Alibaba_Qwen/status/2059674574397313277) reportedly hits **580 tokens/s** for agentic workloads via joint optimization across Alibaba, LightSeek, NVIDIA, Mooncake, and FlashAttention-4 contributors. Supporting libraries also improved: [MaxSim v2](https://x.com/ErikKaum/status/2059659837219156453) adds backprop and reports **10.33× faster on H200** and **11.94× on A100** versus naïve PyTorch.

  * **Price cuts are being justified by structural KV-cache and attention changes** : Several posts converged on the same theme: recent API price cuts from Chinese labs look sustainable because they reflect **lower serving cost per token** , not temporary subsidy. [@kimmonismus](https://x.com/kimmonismus/status/2059578380329394292) summarized how **DeepSeek V4-Pro** uses hybrid attention with **Compressed Sparse Attention** and **Heavily Compressed Attention** to bring **1M-token KV cache to ~10% of V3.2** and single-token inference FLOPs to **27%** , while still routing **49B active params** out of **1.6T total**. Xiaomi’s MiMo similarly reduces cache traffic using SWA plus hierarchical cache management. That was corroborated directly by [@_LuoFuli](https://x.com/_LuoFuli/status/2059618247553745204), who said MiMo’s deepest input-cache-hit price cut comes from **5× cached token capacity** , roughly **80% lower caching cost** , and an architectural **1:7 Full:SWA sparsity ratio**. The broader takeaway: long-context inference economics are now being pushed by **attention design + cache hierarchy + routing** , not just cheaper hardware.




**Agents, Harnesses, Memory, and Continual Learning**

  * **The stack is shifting from “model quality” to “model-harness-memory fit”** : A substantial cluster of tweets focused on practical agent engineering. LangChain shipped [Deep Agents v0.6](https://x.com/LangChain/status/2059634226836746483) with **Delta Channels** , cutting checkpoint storage for a 200-turn coding session from **5.3 GB to 129 MB** , and also launched [computer use in Fleet](https://x.com/LangChain/status/2059685293322858809), plus [Context Hub](https://x.com/hwchase17/status/2059687279199924462) for versioned agent context/skills. [LangSmith Engine](https://x.com/LangChain/status/2059654417478012938) was framed as automating the eval → diagnosis → fix loop, with multiple practitioners emphasizing its value for turning trace feedback into reusable online/offline evaluators. In parallel, [@Vtrivedy10](https://x.com/Vtrivedy10/status/2059712077925658717) made the clearest formulation of the day: **task-harness fit** matters as much as model quality, and bespoke vertical systems outperform generic harnesses by narrowing tools, prompts, and context to the task.

  * **Continual learning is re-emerging as a product category, not just a research topic** : The biggest announcement here was [Trajectory’s launch](https://x.com/rronak_/status/2059644771262730624): a platform for using **product usage signals and agent traces** to continuously post-train large agentic models, with **$15M in funding** and design partners including Clay, Harvey, Decagon, Mercor, and Rogo. Baseten said it supports these deployments with [FP8/NVFP4 quantization and autoscaled H100 infra](https://x.com/baseten/status/2059651376565936510#m), including a cited overnight deployment of a **397B-parameter model**. The same trend appeared in open tooling: [an open-source memory-centric agent](https://x.com/hwchase17/status/2059487107144655356) built on LangChain/LangGraph was praised by multiple builders for explicit retrieval/storage/reasoning/learning separation, and [RLM’s minimal training harness](https://x.com/a1zhang/status/2059633834094678173) shows small teams can now RL-tune long-context agents in **a day on 8×A100**. The throughline is that “post-deployment learning” is moving from aspiration to infra.




**Benchmarks, Scaling Laws, and Training Methods**

  * **New benchmarks are increasingly about long-horizon, messy, real-world workflows** : [DeepSWE](https://x.com/_philschmid/status/2059564676569076021) was highlighted as a SWE/agent benchmark with **113 tasks across 91 repos in 5 languages** , using a minimalist bash-only harness and shorter prompts that nevertheless require **5.5× more code** and touch **7 files on average** than SWE-Bench Pro. In enterprise operations, Artificial Analysis and IBM launched [ITBench-AA](https://x.com/ArtificialAnlys/status/2059698327235805258), an SRE benchmark over Kubernetes incident response where **all frontier models scored below 50%** ; **Claude Opus 4.7** led at **47%** , **GPT-5.5** followed at **46%** , and **GLM-5.1 Reasoning** led open weights at **40%**. Another useful reliability angle came from [AgingBench](https://x.com/omarsar0/status/2059689897523642510), which frames deployed agent degradation as a lifespan problem caused by compression, interference, and memory updates.

  * **Training efficiency research remains active across both theory and systems** : Sakana AI’s [DiffusionBlocks](https://x.com/hardmaru/status/2059648995132367277) was one of the most technically interesting releases: it reinterprets forward passes as diffusion-like denoising steps so deep nets can be trained **one block at a time** , dramatically reducing memory while matching end-to-end performance across **ViTs, DiTs, masked diffusion, autoregressive transformers, and recurrent-depth transformers**. On the RL systems side, Snowflake introduced [ZoRRo](https://x.com/StasBekman/status/2059718503318655314), claiming **up to 3.5× faster long-context RL** and **3.2× longer context windows** by eliminating redundant rollout computation, alongside the specialized [Arctic-Text2SQL-R2](https://x.com/dwarak/status/2059686825086902398#m) enterprise SQL model. On the theory front, [Tiberiu Musat’s preprint](https://x.com/Tiberiu_Musat_/status/2059562156102746148) argues minimum neural weight norm matches minimum program length up to a log factor for fixed-precision networks, while [Unified Neural Scaling Law](https://x.com/ethanCaballero/status/2059686905105563907) proposes a multivariate functional form intended to extrapolate neural scaling behavior more accurately than prior fits.




**Model and Modality Releases: Biology, Vision, OCR, and Embedded AI**

  * **Protein modeling had a standout day** : [ESMFold2](https://x.com/alexrives/status/2059611151860683097) was announced as an open scientific engine for protein structure prediction and design, with strong reported results on **protein interactions and antibodies** , plus an accompanying atlas of **6.8B proteins** and **1.1B predicted structures**. The release emphasized both practical design outcomes—miniprotein binders and single-chain antibodies across five therapeutic targets—and mechanistic interpretability findings about emergent protein representations. The release was echoed by [@proteinrosh](https://x.com/proteinrosh/status/2059633089702240598) and contextualized by [@cgeorgiaw](https://x.com/cgeorgiaw/status/2059694583856927201), who noted the atlas exceeds AlphaFold DB in scale.

  * **A wave of smaller but practical multimodal/open releases landed** : Google DeepMind shared the white paper for [Gemini Embedding 2](https://x.com/mseyed/status/2059504005387284629), described as a **native multimodal embedding model** supporting unified representations over text, image, audio, and video. NVIDIA’s [LocateAnything](https://x.com/wildmindai/status/2059600079804088790) combines **Qwen2.5-3B + Moon-ViT** for high-speed grounding, with a claimed **10× speedup** for dense object detection. Hugging Face integrated Roboflow’s [RF-DETR](https://x.com/mervenoyann/status/2059647988373373253), positioning it as real-time detection/segmentation that outperforms YOLO-style systems. For document pipelines, [Surya OCR 2](https://x.com/VikParuchuri/status/2059675773712167423) ships as a **650M** model with **83.3% OLMOCR bench** , **87% on an internal 91-language benchmark** , and **5 pages/s on RTX 5090** ; [LiteParse v2](https://x.com/jerryjliu0/status/2059710330016817501) rewrites parsing in Rust for **up to 100× speedups** and edge/browser deployment via WASM. On-device AI also got a nod with Google’s new [Coral board](https://x.com/googlegemma/status/2059740184930074758) for local speech, vision, and control demos.




**Developer Platforms, Enterprise Controls, and Coding-Agent Productization**

  * **Coding agents are consolidating into full product stacks with enterprise controls** : OpenAI continued tightening Codex’s product surface: [GPT-5.2 and GPT-5.3-Codex are being sunset in Codex in favor of GPT-5.5](https://x.com/thsottiaux/status/2059650685948551384), while enterprise features now include [private MCP connectivity over outbound-only HTTPS](https://x.com/OpenAIDevs/status/2059703536825565499), [Workload Identity Federation](https://x.com/OpenAIDevs/status/2059703600662925635), and [expanded Admin API controls](https://x.com/OpenAIDevs/status/2059703665276145920) for spend alerts, allowlists, retention policies, and hosted tool management. OpenAI also published a concrete case study on [self-improving tax agents with Codex](https://x.com/OpenAIDevs/status/2059638868983562640), centered on tracing reviewer corrections back into evals and fixes.

  * **Competition in coding agents is now visibly about reliability, workflow breadth, and enterprise adoption** : [Claude Code](https://x.com/ClaudeDevs/status/2059701677981413812) shared a reliability/performance update and easier bug-report capture, while GitHub kept pushing the “agentized IDE” direction with [Copilot Dev Days](https://x.com/code/status/2059664796178354617) and [MCP positioning](https://x.com/code/status/2059666498285629707). The biggest commercial datapoint was [Cognition](https://x.com/cognition/status/2059660758531940856): **>$1B raised at a $26B valuation** , **enterprise usage up >10× YTD** , and **$492M run-rate revenue** , paired with a growing customer list and strong endorsements from users like [Exa](https://x.com/nityasnotes/status/2059768072110776370). Meanwhile, smaller infra/product moves suggest the ecosystem is broadening: [Cua Driver for Windows](https://x.com/trycua/status/2059688960838828391) brings background computer use to Windows agents; [Cloudflare’s agent platform](https://x.com/brandonjcarl/status/2059624598644109363) was repeatedly praised for “fractional computing” economics; and [Grok Build’s worktree support](https://x.com/theskory/status/2059729539287167068) targets multi-agent code swarms at repo scale.




**Top tweets (by engagement)**

  * **Cognition’s scale-up** : [Cognition](https://x.com/cognition/status/2059660758531940856) announced **>$1B raised** , **$26B valuation** , and **$492M run-rate revenue** , one of the clearest signals yet that coding agents are converting into large enterprise businesses.
  * **Claude Code reliability push** : [Anthropic’s ClaudeDevs](https://x.com/ClaudeDevs/status/2059701677981413812) posted a high-engagement update on responsiveness, reliability, and better feedback collection—evidence that product quality and trust are now central battlegrounds.
  * **Sakana AI’s DiffusionBlocks** : [@hardmaru](https://x.com/hardmaru/status/2059648995132367277) drew major attention to block-wise training that can match end-to-end performance while dramatically lowering memory requirements.
  * **ESMFold2 release** : [@alexrives](https://x.com/alexrives/status/2059611151860683097) announced one of the day’s most substantive science releases: open protein modeling at atlas scale with therapeutic design implications.
  * **OpenAI enterprise controls + MCP** : [@OpenAIDevs](https://x.com/OpenAIDevs/status/2059703536825565499) on private MCP and related admin/security updates reflects where frontier APIs are competing for large-org adoption.



* * *

# AI Reddit Recap

## /r/LocalLlama + /r/localLLM Recap

### 1\. Low-Bit Local AI on Consumer Hardware

  * **[PrismML just released Binary and Ternary Bonsai Image 4B: 1-bit/ternary text-to-image diffusion transformers that can even run 100% locally in your browser on WebGPU.](https://www.reddit.com/r/LocalLLaMA/comments/1togflk/prismml_just_released_binary_and_ternary_bonsai/)** (Activity: 759): ****PrismML** released **Binary and Ternary Bonsai Image 4B** , described as `1-bit`/ternary text-to-image diffusion-transformer variants with ~`3GB` checkpoints, **Apache-2.0** licensing, and a WebGPU browser demo ([HF collection](https://huggingface.co/collections/prism-ml/bonsai-image), [demo](https://huggingface.co/spaces/webml-community/bonsai-image-webgpu)). The post compares them to **FLUX.2 Klein 4B** at ~`16GB`; a top technical comment claims Bonsai Image is primarily a quantized/post-trained derivative of **FLUX.2 Klein 4B** , with insufficient attribution outside the whitepaper.** The main debate is attribution/branding: one commenter argues PrismML is rebranding quantized/fine-tuned base models as “Bonsai” while minimizing credit to original labs, comparing it to releasing a quant of Qwen as a new model. Another commenter asks whether it can run on CPU with `16GB` RAM, but no technical answer is provided in the supplied comments.

    * A commenter alleges **PrismML’s “Bonsai-Image” is not a newly trained base model** , but a **binary/ternary quantization of`FLUX.2 Klein 4B`** with additional post-training to recover quality. They argue the project’s HF demo/model pages and GitHub omit clear attribution to the original FLUX model/team, with the original model reportedly mentioned only in the whitepaper.
    * A technical usability note says the browser/WebGPU model requires roughly **`~2 GB` to download**, which is relevant for fully local inference despite the 1-bit/ternary compression claims. Another user asks whether it can run on **CPU with 16 GB RAM** , but no concrete benchmark or compatibility answer is provided in the thread.
  * **[Got tired of OOM errors on my 4GB GPU. Wrote a custom Rust bare-metal engine and hit 66.8 TPS with a 4B model (BitNet 1.58b on RTX 3050).](https://www.reddit.com/r/LocalLLM/comments/1to6enj/got_tired_of_oom_errors_on_my_4gb_gpu_wrote_a/)** (Activity: 390): **OP claims a custom Rust/C++ LLM inference engine,**Cluaiz** , runs `prism-ml/Bonsai-4B-gguf` with `1.58-bit` quantization on an **RTX 3050 4GB** , reaching `66.8 tokens/s`, and reports `~30–33 TPS` for Gemma/Qwen 4B variants without OOM via dynamic KV-cache management. No reproducible repo or benchmark artifacts were provided in the post yet; commenters pointed to the apparent project links ([GitHub](https://github.com/cluaiz/cluaiz), [site](https://cluaiz.com/)) and questioned vague claims like _“direct-to-silicon”_ access, noting this may simply mean ahead-of-time native compilation rather than any unusual GPU/driver-level mechanism. The attached Reddit video could not be independently accessed due to Reddit `HTTP 403` restrictions.** Top comments were strongly skeptical, characterizing the writeup and repo language as pseudo-technical/AI-generated and arguing the stated achievements amount to basic native compilation plus a single-machine demo. Commenters also challenged the project’s licensing/copyright wording under Apache 2.0 and asked for concrete implementation details behind the claimed low-level hardware access.

    * Commenters challenged the technical claims in the linked repo ([github.com/cluaiz/cluaiz](https://github.com/cluaiz/cluaiz), [cluaiz.com](https://cluaiz.com/)), arguing that descriptions like **“direct silicon access”** , “bare-metal engine,” and “copyrighted Apache licensed software” appear to be marketing or LLM-generated pseudo-technical language rather than concrete implementation details. One commenter asked whether “direct silicon access” merely means **ahead-of-time native compilation in Rust** , rather than any real low-level GPU programming beyond normal CUDA/driver APIs.
    * Several commenters argued that the claimed outcome should be compared against existing tooling, especially **llama.cpp** , which already supports low-memory inference and quantized models on consumer GPUs. The critique was that OOM issues on a `4GB` RTX 3050 are often solvable through proper llama.cpp configuration rather than writing a new engine, so the claimed `66.8 TPS` with a `4B` BitNet 1.58b model needs reproducible benchmarks and configuration details to be meaningful.



### 2\. Qwen 3.5/3.6 Local Model Releases and Coding Tests

  * **[Qwen3.5 35B A3B uncensored heretic Native MTP Preserved is Out Now With the Full 785 MTPs Preserved and Retained, Available in Safetensors, GGUFs. NVFP4, NVFP4 GGUFs and GPTQ-Int4 Formats](https://www.reddit.com/r/LocalLLaMA/comments/1tnzalm/qwen35_35b_a3b_uncensored_heretic_native_mtp/)** (Activity: 602): ****llmfan46** released [`Qwen3.5-35B-A3B-uncensored-heretic-v2-Native-MTP-Preserved`](https://huggingface.co/llmfan46/Qwen3.5-35B-A3B-uncensored-heretic-v2-Native-MTP-Preserved), a decensored derivative of `Qwen/Qwen3.5-35B-A3B` made with **Heretic v1.3.0** / Magnitude-Preserving Orthogonal Ablation-style edits targeting `attn.o_proj`, `attn.out_proj`, and `mlp.down_proj`, while preserving all `785` native MTP tensors. The model card reports refusals reduced from `92/100` to `14/100`, KL divergence `0.0487` vs base, and MMLU dropping only from `84.12%` to `83.72%` over `7,021` questions; releases include [Safetensors](https://huggingface.co/llmfan46/Qwen3.5-35B-A3B-uncensored-heretic-v2-Native-MTP-Preserved), [GGUF](https://huggingface.co/llmfan46/Qwen3.5-35B-A3B-uncensored-heretic-v2-Native-MTP-Preserved-GGUF), [NVFP4](https://huggingface.co/llmfan46/Qwen3.5-35B-A3B-uncensored-heretic-v2-Native-MTP-Preserved-NVFP4), [NVFP4 GGUF](https://huggingface.co/llmfan46/Qwen3.5-35B-A3B-uncensored-heretic-v2-Native-MTP-Preserved-NVFP4-GGUF), and [GPTQ-Int4](https://huggingface.co/llmfan46/Qwen3.5-35B-A3B-uncensored-heretic-v2-Native-MTP-Preserved-GPTQ-Int4) variants. The author argues Qwen3.5 and Qwen3.6 both use the `qwen35` architecture but are tuned for different regimes—Qwen3.5 for general assistance, Qwen3.6 for agentic/coding—and notes abliteration KL/quality behavior differs substantially between the families.** Commenters appreciated the unusual availability of an **NVFP4 GGUF** build, with one noting they could not find comparable releases even from Unsloth. Another tester agreed with the author’s positioning, describing Qwen3.6 as closer to _“3.5 coder+”_ rather than a simple across-the-board successor to Qwen3.5.

    * One commenter highlighted the practical value of the **NVFP4 GGUF** build, noting that this format is hard to find elsewhere: _“I seriously can't find anyone else doing that, not even Unsloth.”_ This is technically relevant because NVFP4 GGUF availability can matter for users targeting newer NVIDIA-oriented low-precision inference workflows while still using GGUF-based runtimes.
    * A tester compared **Qwen3.5** and **Qwen3.6** , arguing that 3.6 feels more like _“3.5 coder+”_ than a straightforward general upgrade. They suggested the short time between releases makes a broad capability leap unlikely, implying 3.6 may be more specialized toward coding rather than a simple successor to 3.5.
  * **[Okay 27B made me a believer](https://www.reddit.com/r/LocalLLaMA/comments/1to73op/okay_27b_made_me_a_believer/)** (Activity: 541): **OP reports that a`27B` **Qwen** -family model used via **Opencode** generated a near-complete HTML5 Breakout-style game in one shot from three reference files describing console APIs, gamepad controls, and a TypeScript shader. The output was immediately playable, with working controls, sound, metadata, save/stat/heartbeat API integration, and only required one follow-up for customization plus one glitch fix; a commenter recommends enabling **MTP/speculative decoding** with `2–3` draft tokens for speed. Another heavy user says the model performs best below `64K` context, degrades noticeably past `64K`, and “really drops off” after `128K`, recommending periodic summarization-to-file and session resets for long agentic coding tasks.** Commenters characterize the dense `27B` as unusually strong for local coding— _near-Sonnet class_ for web-app one-shots—while one user found `35B A3B` less capable despite its size/routing advantages. The main caution is that long-context agentic runs can induce loops or “stupidity,” so users should manage context aggressively.

    * A commenter recommended enabling **MTP/speculative decoding** for better throughput, suggesting an MTP value of `2` or `3` as a practical speed/quality tradeoff. This is a deployment-level optimization rather than a model-quality claim, useful for users running the 27B model locally.
    * One user reported that the 27B model’s effective reasoning quality drops noticeably with long contexts: **best below`64K` tokens**, degraded past `64K`, and _“really drops off after`128K`.”_ Their workaround for long-horizon agentic tasks is to periodically summarize state into a file, restart the harness/session, and reload the summary to recover model quality and avoid loops.
    * A benchmark operator said **Qwen 27B** was such an outlier that they rechecked their methodology, placing it _roughly on par with GPT-5.2 or Sonnet 4.5_ in their rankings while noting it struggles at larger context sizes, likely due to parameter-count limits. They linked their data at [gertlabs.com/rankings](https://gertlabs.com/rankings).



## Less Technical AI Subreddit Recap

> /r/Singularity, /r/Oobabooga, /r/MachineLearning, /r/OpenAI, /r/ClaudeAI, /r/StableDiffusion, /r/ChatGPT, /r/ChatGPTCoding, /r/aivideo, /r/aivideo

### 1\. Claude Code Vibe-Coding Practices

  * **[The thing you built with Claude is useless to me... and that's the point](https://www.reddit.com/r/ClaudeAI/comments/1tp3en9/the_thing_you_built_with_claude_is_useless_to_me/)** (Activity: 1152): **The post argues that many**Claude-built “vibe coded” tools** —e.g., personal health correlators, Garmin data archivers, store-specific grocery sorters, niche bioinformatics pipelines, and terminal-error explainers—are valuable precisely because they are **highly individualized artifacts** , not reusable products. The author suggests public repos and posts should document the _problem-framing process_ —the friction, failed alternatives, and why existing tools were misfit—because that cognitive pattern transfers better than the code itself.** Top commenters broadly agreed, framing AI-assisted development as a shift toward **personal software** ; one compared _vibe coding_ to “the 3D printing of software development.” Another noted the post’s style felt AI-generated, but still found the underlying idea novel and constructive.

    * One commenter reports that AI has effectively automated their technical-documentation workflow, claiming typographic content, formatting, and overall quality improved by about `10x` while taking roughly `1/100` of the previous time. They also note AI enabled them to complete documentation tasks they previously “couldn’t even start,” suggesting the main productivity gain is in lowering the activation/skill barrier for structured technical writing.
  * **[I'm a software engineer with a decade of experience. This is how I'd approach learning to build apps using Claude Code if I were starting from scratch today:](https://www.reddit.com/r/ClaudeAI/comments/1tonzj9/im_a_software_engineer_with_a_decade_of/)** (Activity: 919): **A senior SWE argues that beginners using**Claude Code/vibe coding** should learn application architecture top-down rather than starting with implementation details: typical web apps are framed as **frontend + backend + database + “plumbing”**. The emphasized production-readiness layer includes `APIs`, hosting/DNS/deployment, environment variables/secrets, authentication vs authorization, backups, Git/version control, testing, monitoring/error tracking, and analytics; the author also started collecting follow-up material at [vibe-blog.pages.dev](https://vibe-blog.pages.dev/).** Top technical pushback notes that this architecture is strongly **web-service/full-stack-centric** and not universal: embedded, simulation, scientific/industrial, defense, optics, FEA, control systems, and other niche software may have no frontend/backend/database split. Commenters broadly agree that early architecture matters, warning that projects approaching ~`10k` LOC can quickly accumulate hard-to-rewrite “Byzantine” coupling if foundational design is poor.

    * A commenter argues that the post’s framing of app development as frontend/backend/database-centric is mostly applicable to web services, but misses many high-paying embedded/scientific/industrial software domains where apps may have no backend and only write logs. Examples cited include **blackbody radiator control** , **collimator simulation** , optical lens design, radiology, and material FEA—roles where domain expertise can matter as much as programming skill.
    * There is a technical architecture warning that once a project approaches around `10,000` lines of code, the probability of having created a serious structural problem that gets patched over rather than redesigned rises quickly. The commenter highlights how both consumer systems like **Netflix** and critical infrastructure like the **American power grid** can converge on similar "we can't fix this without a major rewrite" failure modes despite very different domains.
    * A Claude Code billing gotcha: if `ANTHROPIC_API_KEY` is present in the shell environment or inherited from a `.env` file, Claude Code requests may silently bill the API account instead of using the **Max plan** subscription quota. This also affects `claude -p` run from cron/subprocesses; the fix is to strip the key from the subprocess environment so Claude Code falls back to OAuth credentials.
  * **[Thanks to Claude Code I (a coding amateur) was able to build Questboard, a family RPG style chore-board for our tablet wall display. Complete chores to defeat the monster before midnight to earn gold, or it fights back. Spend gold in the reward shop on treats you've agreed on as a family.](https://www.reddit.com/r/ClaudeCode/comments/1tolrav/thanks_to_claude_code_i_a_coding_amateur_was_able/)** (Activity: 905): **A self-described coding amateur used**Claude Code** to build [**Questboard**](https://github.com/thillygooth/questboard), a family-oriented RPG-style chore board intended for a tablet wall display. The app gamifies chores as timed “monster” encounters: completing chores before midnight earns in-game gold, while failure lets the monster “fight back”; gold can then be spent in a family-agreed reward shop.** Comments were mostly positive but non-technical, praising it as a wholesome, non-commercial real-world use case for AI-assisted coding; one commenter asked for more details about the tablet wall setup.




### 2\. Enterprise AI Tool Spend and Governance

  * **[Company gave us all unlimited Claude Code Sonnet 4.6 — and now posts a weekly leaderboard of who burns the most tokens. Any tips to top it?](https://www.reddit.com/r/ClaudeAI/comments/1tob45x/company_gave_us_all_unlimited_claude_code_sonnet/)** (Activity: 2168): **The image is an internal EngOps spreadsheet/usage dashboard ([image](https://i.redd.it/hnki8byc5i3h1.png)) showing weekly **Claude Code Sonnet 4.6** token consumption by user, sorted as a leaderboard from roughly `2.5M` tokens down to `57k`. Contextually, the post is less about a model benchmark and more about organizational usage tracking/gamification of LLM spend; the top technical comment suggests using Claude as an orchestrator/product-manager agent that decomposes backlog items into parallel Sonnet-agent tasks, while maintaining explainable output in case high usage is audited.** Commenters joked that `2.5M` tokens is “rookie numbers,” but the main caution was that deliberately topping the leaderboard could backfire unless the usage maps to demonstrable project output. One commenter proposed embracing the leaderboard by giving Claude the ranking context and asking it to plan useful sprints rather than merely burning tokens.

    * A technically substantive suggestion was to use **Claude Sonnet as an orchestrator** : give it a real backlog/problem, have it generate a comprehensive plan, then spin up multiple Sonnet chats as worker agents and ask the original chat to dispatch implementation steps. The commenter frames this as a product-management loop with sprint planning, daily summaries, and controlled token usage tied to useful deliverables rather than blind token burning.
    * One commenter linked an open-source Claude skills repo, [**RampStack Claude Skills**](https://github.com/rampstackco/claude-skills), intended to make Claude act more like a product manager across the software/product lifecycle. The suggested workflow is to provide pain points/backlog items, let Claude plan “sprints,” delegate to other agents, and generate summaries explaining what was built.
    * Another commenter shared [**Ordinath/tokenburn**](https://github.com/Ordinath/tokenburn), apparently a tool specifically for burning tokens. This is directly relevant to maximizing leaderboard usage, though the thread provides no benchmark data, implementation details, or efficiency analysis for the tool itself.
  * **[Microsoft, has started canceling Claude Code licenses, per the Verge](https://www.reddit.com/r/ClaudeAI/comments/1to6kqz/microsoft_has_started_canceling_claude_code/)** (Activity: 1712): **The[image](https://i.redd.it/4nskxdbpeh3h1.png) is a **non-technical meme** using an _I, Robot_ scene to joke that even AI coding assistants can be “laid off,” in reference to the post’s claim that **Microsoft is canceling Claude Code licenses**. The technical context in the comments centers on a reported internal shift toward **standardized GitHub Copilot adoption** , with users noting upcoming Copilot pricing/allowance changes and heavy prior usage of **Claude Sonnet** through corporate tooling.** Commenters debated whether this is mainly a cost-cutting move against Claude or simply Microsoft consolidating developers onto GitHub Copilot; one user warned that new pricing could make current `$40`-tier usage cost roughly `$600`, while another argued Microsoft still runs its own model infrastructure and this is more about standardization.

    * Commenters highlight that upcoming **GitHub Copilot pricing changes** could materially reduce enterprise access to Claude-backed usage: one claims their corporate allowance is expected to drop by about `6x`, with most prior usage going to **Claude Sonnet**. The same commenter estimates their personal workload currently costing `$40/month` would map to roughly `$600/month` under the new pricing, while heavier users may have been consuming “several thousand dollars worth” of inference under flat-rate plans.
    * A technically relevant interpretation is that Microsoft’s Claude Code license cancellations may be less about abandoning AI and more about consolidating internal tooling around **GitHub Copilot** as the standardized interface. One commenter notes Microsoft can still run model infrastructure internally, suggesting the shift may be driven by procurement, metering, and platform control rather than simple model deprecation.
    * Several comments frame the issue as a correction from subsidized AI access to real token economics: flat-rate or VC-subsidized plans masked the true inference cost of high-volume coding-agent usage. The discussion implies organizations will soon need to account for per-token/per-request costs, especially when agentic coding tools generate large context windows and repeated model calls.
  * **[So, Uber CTO said that Uber burned their total 2026 AI budget within the first four months](https://www.reddit.com/r/ChatGPT/comments/1tp7ips/so_uber_cto_said_that_uber_burned_their_total/)** (Activity: 833): **[Cybernews](https://cybernews.com/ai-news/uber-ai-return-of-investment-token-usage/) reports that **Uber exhausted its 2026 AI budget within four months** , with COO **Andrew Macdonald** saying the company still cannot map increased **Claude Code token consumption** to proportional output of valuable consumer-facing features. The discussion centers on enterprise AI cost controls: usage-based token billing can scale faster than realized productivity gains, especially when employees are encouraged to use “AI everywhere” without per-user/model-level cost accountability.** Commenters argued that many companies created the overspend problem by giving staff no incentive to optimize token usage or choose cheaper models; one user said their own company moved to a `$100/month` AI budget, expandable to `$250`, but they can burn `$100` in a single day. Another commenter dismissed the issue as a “skill issue,” implying poor usage discipline rather than a fundamental AI economics problem.

    * A commenter describes a concrete enterprise cost-control shift after an “AI everywhere / agents / automate everything” rollout: their company moved users to a monthly AI spend cap of `$100`, extendable to `$250`, but they can consume `$100` in a single day under normal workflows. They note this would require explicit optimization of usage patterns, implying that unmanaged agentic/LLM usage can quickly exceed per-user budget assumptions.
    * Another technical concern raised is incentive design: employees have little reason to minimize token usage or choose cheaper models when AI costs are abstracted away from individual workflows. This points to a governance problem around model routing, token budgeting, and default model selection rather than purely a model-cost problem.



# AI Discords

Unfortunately, Discord shut down our access today. We will not bring it back in this form but we will be shipping the new AINews soon. Thanks for reading to here, it was a good run.

---

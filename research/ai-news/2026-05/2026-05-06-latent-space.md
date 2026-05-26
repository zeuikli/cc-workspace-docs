# 🔬 Latent Space — 2026-05-06

> swyx 開發者簡報，未公開專案 + 工程視角
> 來源：[Latent Space](https://www.latent.space/feed)

---

## [[AINews] Silicon Valley gets Serious about Services](https://www.latent.space/p/ainews-silicon-valley-gets-serious)
*🔬 Latent Space | 2026-05-06*

We’ve written separately about 1) how [model labs will tack on an agent lab](https://www.latent.space/p/agent-labs?utm_source=publication-search) to pursue last mile revenue and differentiated data/monetization, 2) how [coding agents breaking containment will pursue the rest of knowledge work](https://www.latent.space/p/ainews-agents-for-everything-else) this year, and both themes unite this week with both Anthropic and OpenAI announcing services companies:

[Anthropic’s unnamed JV with Blackstone, Hellman & Friedman, and Goldman Sachs](https://www.anthropic.com/news/enterprise-ai-services-company) - funded with [$1.5B ($300m each](https://www.wsj.com/business/deals/anthropic-nears-1-5-billion-joint-venture-with-wall-street-firms-8f5448ee) from main participants) “A typical engagement starts with a small team working closely with the customer to understand where Claude can have the biggest impact. From there, the company’s engineers—alongside Anthropic Applied AI staff—will develop Claude-powered systems tailored to each organization’s operations.” 

[OpenAI’s The Deployment Company, backed by 19 investors, including TPG, Brookfield Asset Management, Advent, and Bain Capital](https://www.msn.com/en-us/money/general/openai-launches-10b-ai-venture-backed-by-tpg-bain-softbank-bloomberg/ar-AA22miSj) - raised about $4B so far at a $10B premoney valuation: “Microsoft-backed OpenAI last month said that its chief operating officer, Brad Lightcap, will shift into a new role and lead special projects while reporting directly to CEO Sam Altman. Lightcap would oversee OpenAI’s push to sell software to businesses through a joint venture with a private equity firm.”

As Aaron Levie [says](https://x.com/levie/status/2051344780328858040?s=46), 

“As agents enter knowledge work beyond coding, there is very real work to upgrade IT systems, get agents the context they need, modernize the workflows to work with agents, figure out the human-agent relationship in the workflow, drive adoption and do change management, and much more. 

While AI models have an incredible amount of capability packed into them, there’s no shortcut to getting that intelligence applied to a business process in a stable way. This is creating tons of opportunities across the market for new jobs and firms, and the labs are equally recognizing the criticality here.”

While these companies are likely more PE focused services, both companies have been pushing other vertical services initiatives for a while, and [Anthropic held a Financial Services event](https://x.com/TechFundies/status/2051733955049853053) in New York today with an extremely stacked guest list, noting that Finance is Anthropic’s [second highest](https://x.com/madisonmills22/status/2051688936053813661?s=46) revenue segment:

Other startups, like Tessera raising a [Series A for System Integration today](https://x.com/kabirnagrecha/status/2051719069448196366?s=46), will try to compete, with a fraction of the funding.

AI News for 5/4/2026-5/5/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews’ website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

AI Twitter Recap

OpenAI’s GPT-5.5 Instant, personalization rollout, and voice/agent infrastructure updates

GPT-5.5 Instant becomes ChatGPT’s new default: OpenAI rolled out GPT-5.5 Instant to ChatGPT and the API as gpt-5.5-chat-latest, positioning it as a broad upgrade in factuality, baseline intelligence, image understanding, and tone. The launch also bundled stronger personalization: ChatGPT can now use saved memories, past chats, files, and connected Gmail, while exposing “memory sources” so users can see what context influenced a reply. See the main launch thread from [@OpenAI](https://x.com/OpenAI/status/2051709028250915275), rollout details from [@OpenAI](https://x.com/OpenAI/status/2051709035347694047), product commentary from [@michpokrass](https://x.com/michpokrass/status/2051709536130802022), and reactions from [@ericmitchellai](https://x.com/ericmitchellai/status/2051711459886059963) and [@sama](https://x.com/sama/status/2051716909629153573).

OpenAI also published more infra detail around real-time products: [@OpenAIDevs](https://x.com/OpenAIDevs/status/2051453905343828350) shared a writeup on rebuilding the WebRTC stack for ChatGPT voice and the Realtime API using a thin relay plus a stateful transceiver to reduce latency and keep conversations at speech pace. This fits the broader signal around an imminent voice refresh, noted by [@kimmonismus](https://x.com/kimmonismus/status/2051571219040735423) and [@sama](https://x.com/sama/status/2051464865634742334).

Developer-side OpenAI agent tooling keeps expanding: [@OpenAIDevs](https://x.com/OpenAIDevs/status/2051725072873001338) announced the Agents SDK for TypeScript, including sandbox agents and an open-source harness. Separately, OpenAI continued pushing Codex UX and automation, including task progress UI highlighted by [@reach_vb](https://x.com/reach_vb/status/2051655026574057593) and Auto Review for lower-friction approvals in [@reach_vb](https://x.com/reach_vb/status/2051782942314078553). Community sentiment suggests 5.5 is especially strong for high-token-budget coding and non-coding workflows, per [@sama](https://x.com/sama/status/2051724685231214650) and [@sama](https://x.com/sama/status/2051783339502375418).

Coding agents, harness design, and benchmark pressure

Harness quality is becoming a first-class differentiator: A recurring theme across the day was that model quality alone no longer explains agent performance. [@Vtrivedy10](https://x.com/Vtrivedy10/status/2051451869017584112) argued the field is mixing incompatible assumptions about native post-trained harnesses, open harnesses, and “AGI-like” model generalization; the practical takeaway is that Model–Harness–Task fit matters more than abstract benchmark narratives. A complementary post from [@Vtrivedy10](https://x.com/Vtrivedy10/status/2051674478648742002) emphasized that talking to base or minimally wrapped models makes clear how much productized agents depend on instructions, tools, context packing, and measurement loops. [@sydneyrunkle](https://x.com/sydneyrunkle/status/2051637638239567953) pointed to a LangChain post on the “anatomy” of long-running harnesses, while [@masondrxy](https://x.com/masondrxy/status/2051714091924828480) argued for ACP-style decoupling so teams can swap CLI/TUI/GUI/IDE frontends without changing the underlying harness.

Agent coding UX is fragmenting, with real disagreement on winners: There were multiple anecdotal comparisons of agent shells and coding assistants. [@0xSero](https://x.com/0xSero/status/2051689733793755405) ranked Droid above Pi, Amp, OpenCode, and Codex CLI. [@teortaxesTex](https://x.com/teortaxesTex/status/2051549309707928028) said Hermes currently beats deepseek-tui and OpenCode on success rate, speed, and cost, adding cache-hit details in a follow-up [comparison](https://x.com/teortaxesTex/status/2051551506134896976). On the commercial side, [@kimmonismus](https://x.com/kimmonismus/status/2051515496567292310) cited TickerTrends data claiming Codex surpassed Claude Code in downloads after late-April releases, while several developers reported that Claude Code utility feels relatively flat versus last fall, e.g. [@TheEthanDing](https://x.com/TheEthanDing/status/2051516204607578132) and [@finbarrtimbers](https://x.com/finbarrtimbers/status/2051652067480179020).

New coding benchmark: ProgramBench shows how far “whole-repo from scratch” still is: Meta researchers introduced ProgramBench, a 200-task benchmark asking models to generate substantial software artifacts like SQLite, FFmpeg, and a PHP compiler from an executable spec and without starter code or internet access. [@jyangballin](https://x.com/jyangballin/status/2051677497562210552) presented it as an end-to-end repo generation test; [@OfirPress](https://x.com/OfirPress/status/2051678633035809159) summarized the headline result bluntly: top accuracy is 0%. Discussion quickly focused on whether the headline metric is too harsh: [@scaling01](https://x.com/scaling01/status/2051733949877985349) noted models can still pass >50% of tests per task on average, while [@OfirPress](https://x.com/OfirPress/status/2051757679283143089) defended the all-tests criterion as necessary because partial implementations can game average-pass metrics.

Practical coding automation keeps moving into CI/security: [@cursor_ai](https://x.com/cursor_ai/status/2051739625958584659) launched agents that monitor GitHub and automatically fix CI failures. [@cognition](https://x.com/cognition/status/2051708729880416614) introduced Devin for Security, including claims of automated vuln remediation at enterprise scale and an example where Devin Review flagged a malicious axios release before public disclosure in [@cognition](https://x.com/cognition/status/2051708731671331171).

Inference, systems, and efficiency: Gemma 4 drafters, SGLang/RadixArk, and provider economics

Gemma 4 gets multi-token prediction drafters across the open stack: Google released Gemma 4 MTP drafters, promising up to 3× faster decoding with no quality degradation. The launch came through [@googlegemma](https://x.com/googlegemma/status/2051713412431007808), [@googledevs](https://x.com/googledevs/status/2051700498328346945), and ecosystem posts from [@osanseviero](https://x.com/osanseviero/status/2051695861801820475), [@mervenoyann](https://x.com/mervenoyann/status/2051702372339003841), and [@_philschmid](https://x.com/_philschmid/status/2051752856319926475). The key engineering detail is that this is speculative-style decoding integrated into open tooling, with day-0 or near-day-0 support in Transformers, vLLM, MLX, SGLang, Ollama, and AI Edge. [@vllm_project](https://x.com/vllm_project/status/2051744111116574950) specifically announced a ready Docker image for Gemma 4 on vLLM.

RadixArk raises a massive seed around SGLang + Miles: One of the bigger infra financings was RadixArk’s $100M seed, built around the SGLang inference stack and Miles for large-scale RL/post-training. [@BanghuaZ](https://x.com/BanghuaZ/status/2051650922892476904) framed the company as spanning inference, training, RL, orchestration, kernels, and multi-hardware systems; [@Arpan_Shah_](https://x.com/Arpan_Shah_/status/2051651802484150278) and [@GenAI_is_real](https://x.com/GenAI_is_real/status/2051703162722263180) emphasized the goal of making frontier-grade infrastructure open and production-grade, rather than forcing every team to rebuild scheduling, KV-cache management, and rollout systems from scratch. Community endorsements came from [@ibab](https://x.com/ibab/status/2051690211873308892) and [@multiply_matrix](https://x.com/multiply_matrix/status/2051698056316526651).

Inference economics are now highly provider-specific: [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2051735255044997215) compared MiniMax-M2.7 across six providers and found major differences in tokens/sec, cache discounting, and blended cost. SambaNova led raw speed at 435 output tok/s, while Fireworks looked stronger on the speed/price frontier for many workloads. Separately, [@teortaxesTex](https://x.com/teortaxesTex/status/2051525774851682409) highlighted how cache-hit rates dominate cost on some agent workloads, calling cache optimization “the main axis of cost reduction with V4.”

Cold-start and distributed training remain active systems bottlenecks: [@kamilsindi](https://x.com/kamilsindi/status/2051674592750494094) described a system that cut model cold starts 60×, from minutes to seconds, by serving weights from GPUs already holding them rather than cloud storage. On the training side, [@dl_weekly](https://x.com/dl_weekly/status/2051693914868871205) highlighted Google DeepMind’s Decoupled DiLoCo, which reportedly achieved 88% goodput vs. 27% for standard data parallel at scale while using ~240× less inter-datacenter bandwidth.

Agents, RL environments, observability, and long-horizon research

RL infra is shifting from “single generation + reward” to long-running action systems: [@adithya_s_k](https://x.com/adithya_s_k/status/2051660068471603352) released a guide comparing RL environment frameworks for the LLM era, focusing on what scales to thousands of environments. A detailed survey by [@ZhihuFrontier](https://x.com/ZhihuFrontier/status/2051691071634301064) contrasted traditional RLVR with agentic RL, pointing to systems such as Forge, ROLL, Slime, and Seer and recurring concerns like TITO consistency, rollout latency, prefix-tree merging, and global KV caches.

Long-horizon failures are increasingly framed as horizon problems, not just capacity problems: [@dair_ai](https://x.com/dair_ai/status/2051679862788878354) summarized a Microsoft Research paper arguing that goal horizon alone can be the training bottleneck, with macro actions / horizon reduction stabilizing training and improving long-horizon generalization. This rhymes with broader frustration that current benchmarks and public evals still underweight true long-horizon behavior.

Observability is maturing into a feedback-driven improvement loop: [@hwchase17](https://x.com/hwchase17/status/2051708980435853513) and [@LangChain](https://x.com/LangChain/status/2051709642716135729) argued that traces alone are insufficient; the key is attaching direct, indirect, or generated feedback so observability becomes a learning system. [@benhylak](https://x.com/benhylak/status/2051727888639250450) launched Raindrop Triage, an agent dedicated to finding and investigating bad agent behavior. [@Vtrivedy10](https://x.com/Vtrivedy10/status/2051727418134593632) laid out the practical loop explicitly: gather data → mine errors → localize which component failed → apply fix → test → repeat.

Enterprise verticalization: finance, legal, and proactive assistants

Anthropic and Perplexity both pushed hard into finance workflows: Anthropic launched financial-services agent templates for work such as pitch generation, valuation review, KYC screening, and month-end close, with integrations into providers like FactSet, S&P Global, and Morningstar, via [@claudeai](https://x.com/claudeai/status/2051679629488865498) and summarized by [@kimmonismus](https://x.com/kimmonismus/status/2051681279582540114). Perplexity announced Perplexity Computer for Professional Finance, bringing in licensed data and 35 dedicated workflows for repeat analyst work, in [@perplexity_ai](https://x.com/perplexity_ai/status/2051693893473935372) and [@AravSrinivas](https://x.com/AravSrinivas/status/2051694381137350661). Both launches reflect a clearer move from generic copilots to workflow-packaged vertical products.

Perplexity also expanded into medical/professional health sources: [@perplexity_ai](https://x.com/perplexity_ai/status/2051710342242480538) announced premium access to NEJM, BMJ, and additional medical journals/databases, enabling “deep and wide research” on trusted clinical sources; [@AravSrinivas](https://x.com/AravSrinivas/status/2051711236224761983) framed this as a product for healthcare-grade information retrieval.

Proactive assistant surfaces are becoming a product category: [@kimmonismus](https://x.com/kimmonismus/status/2051618156385366305) reported a leak around Anthropic Orbit, described as a proactive assistant that synthesizes data from Gmail, Slack, GitHub, Calendar, Drive, and Figma without explicit prompting. Manus also added recommended connectors that are suggested in context when needed, per [@ManusAI](https://x.com/ManusAI/status/2051681463389610209).

Top tweets (by engagement)

Anthropic’s finance template launch drew outsized attention: [@claudeai](https://x.com/claudeai/status/2051679629488865498) announced ready-to-run Claude agent templates for financial services with 22.9K engagement, one of the biggest clearly technical/AI-product posts in the set.

OpenAI’s GPT-5.5 Instant launch dominated discussion: the main rollout thread from [@OpenAI](https://x.com/OpenAI/status/2051709028250915275) exceeded 8.2K engagement, with follow-on personalization details also performing strongly.

Gemma 4 speedups landed as a major open-model systems update: [@googledevs](https://x.com/googledevs/status/2051700498328346945) on 3× faster Gemma 4 and [@googlegemma](https://x.com/googlegemma/status/2051713412431007808) both broke through, reflecting strong interest in inference improvements that preserve quality.

Perplexity’s finance launch also resonated broadly: [@perplexity_ai](https://x.com/perplexity_ai/status/2051693893473935372) reached 2.5K engagement, suggesting that licensed-data workflow products are now seen as strategically important, not just niche enterprise packaging.

AI Reddit Recap

/r/LocalLlama + /r/localLLM Recap

1. Gemma 4 MTP and llama.cpp Speculative Decoding

[Gemma 4 MTP released](https://www.reddit.com/r/LocalLLaMA/comments/1t4jq6h/gemma_4_mtp_released/) (Activity: 1116): Google released Multi-Token Prediction (MTP) drafter checkpoints for Gemma 4, with Hugging Face model cards for gemma-4-31B-it-assistant, gemma-4-26B-A4B-it-assistant, gemma-4-E4B-it-assistant, and gemma-4-E2B-it-assistant, described in Google’s [blog post](https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/). The MTP setup adds a smaller/faster draft model for speculative decoding, where several draft tokens are proposed and then verified in parallel by the target model, claiming “up to 2x” decoding speedups while preserving identical output quality versus standard generation; one commenter notes the E2B drafter is only 78M parameters. A technical commenter also shared an updated visual explainer of MTP/speculative decoding for Gemma 4: [Maarten Grootendorst’s guide](https://newsletter.maartengrootendorst.com/i/193064129/multi-token-prediction-mtp-with-gemma-4).

A commenter linked a technical visual guide explaining multi-token prediction (MTP) with Gemma 4, including implementation snippets and diagrams: [Maarten Grootendorst’s guide](https://newsletter.maartengrootendorst.com/i/193064129/multi-token-prediction-mtp-with-gemma-4). This is the main substantive resource in the thread for understanding how Gemma’s MTP-style decoding/drafting works.

One technical detail noted is that the E2B model includes a 78M draft model, implying a relatively small auxiliary model used for speculative or multi-token drafting. The comment highlights the draft model size as unusually compact, which is relevant for latency/throughput tradeoffs in MTP-style inference.

[Llama.cpp MTP support now in beta!](https://www.reddit.com/r/LocalLLaMA/comments/1t3guzw/llamacpp_mtp_support_now_in_beta/) (Activity: 1103): llama.cpp has beta MTP (Multi-Token Prediction) support via [PR #22673](https://github.com/ggml-org/llama.cpp/pull/22673), initially targeting Qwen3.x MTP models and loading the MTP component as a separate model from the same GGUF, with its own context/KV cache rather than a separate GGUF artifact. The PR adds post-ubatch MTP consumption to propagate hidden features correctly across ubatches and a small speculative decoding path depending on partial seq_rm support; reported Qwen3.6 27B / 35B-A3B tests show ~75% steady-state acceptance with 3 draft tokens and usually >2× token-generation throughput over baseline. Commenters view this as potentially one of the largest llama.cpp performance improvements to date, especially for dense models, and expect it to narrow token-generation speed gaps with vLLM alongside tensor parallelism. There is demand for a technical comparison of speculative decoding methods—MTP, EAGLE-3, DFlash, DTree, n-gram—covering draft-model requirements, context reuse, and model suitability.

Commenters frame MTP / multi-token prediction as potentially a major llama.cpp throughput improvement, especially for dense models, while expecting less benefit for MoE architectures. There is interest in comparing it against other speculative decoding approaches such as EAGLE-3, DFlash, DTree, and ngram, particularly around whether they require separate draft models and how well they reuse existing context.

One tester reported llama.cpp’s beta MTP support is “way faster than ik_llama.cpp implementation currently” in quick local testing. They linked a GGUF surgery script that extracts the MTP layer from am17an’s Q8_0 model and injects it into an existing Qwen 3.6 27B GGUF: [gist.github.com/buzz/1c439684d5e3f36492ae9f64ef7e3f67](https://gist.github.com/buzz/1c439684d5e3f36492ae9f64ef7e3f67), reportedly working with Bartowski’s Q6_K quantization.

[
Read more
](https://www.latent.space/p/ainews-silicon-valley-gets-serious)

---

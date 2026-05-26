# 🔬 Latent Space — 2026-05-10

> swyx 開發者簡報，未公開專案 + 工程視角
> 來源：[Latent Space](https://www.latent.space/feed)

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

## [[AINews] Silicon Valley gets Serious about Services](https://www.latent.space/p/ainews-silicon-valley-gets-serious)
*🔬 Latent Space | 2026-05-06*

We've written separately about 1) how [model labs will tack on an agent lab](https://www.latent.space/p/agent-labs?utm_source=publication-search) to pursue last mile revenue and differentiated data/monetization, 2) how [coding agents breaking containment will pursue the rest of knowledge work](https://www.latent.space/p/ainews-agents-for-everything-else) this year, and both themes unite this week with both Anthropic and OpenAI announcing services companies:

  * [Anthropic's unnamed JV with Blackstone, Hellman & Friedman, and Goldman Sachs](https://www.anthropic.com/news/enterprise-ai-services-company) \- funded with [$1.5B ($300m each](https://www.wsj.com/business/deals/anthropic-nears-1-5-billion-joint-venture-with-wall-street-firms-8f5448ee) from main participants) "_A typical engagement starts with a small team working closely with the customer to understand where Claude can have the biggest impact. From there, the company 's engineers--alongside Anthropic Applied AI staff--will **develop Claude-powered systems tailored to each organization 's operations.**_"

  * [OpenAI's The Deployment Company, backed by 19 investors, including TPG, Brookfield Asset Management, Advent, and Bain Capital](https://www.msn.com/en-us/money/general/openai-launches-10b-ai-venture-backed-by-tpg-bain-softbank-bloomberg/ar-AA22miSj) \- raised about $4B so far at a $10B premoney valuation: "_Microsoft-backed OpenAI last month said that its chief operating officer, Brad Lightcap, will shift into a new role and lead special projects while reporting directly to CEO Sam Altman.**Lightcap would oversee OpenAI 's push to sell software to businesses through a joint venture with a private equity firm.**_"




[](https://substackcdn.com/image/fetch/$s_!MR33!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa0374389-0ce7-4d8c-828c-335d3846130a_889x500.jpeg)

As Aaron Levie [says](https://x.com/levie/status/2051344780328858040?s=46), 

> _" As agents enter knowledge work beyond coding, there is very real work to upgrade IT systems, get agents the context they need, modernize the workflows to work with agents, figure out the human-agent relationship in the workflow, drive adoption and do change management, and much more.   
>   
> While AI models have an incredible amount of capability packed into them, there's no shortcut to getting that intelligence applied to a business process in a stable way. This is creating tons of opportunities across the market for new jobs and firms, and the labs are equally recognizing the criticality here."_

While these companies are likely more PE focused services, both companies have been pushing other vertical services initiatives for a while, and [Anthropic held a Financial Services event](https://x.com/TechFundies/status/2051733955049853053) in New York today with an extremely stacked guest list, noting that Finance is Anthropic's [second highest](https://x.com/madisonmills22/status/2051688936053813661?s=46) revenue segment:

Other startups, like Tessera raising a [Series A for System Integration today](https://x.com/kabirnagrecha/status/2051719069448196366?s=46), will try to compete, with a fraction of the funding.

> AI News for 5/4/2026-5/5/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

# **AI Twitter Recap**

**OpenAI 's GPT-5.5 Instant, personalization rollout, and voice/agent infrastructure updates**

  * **GPT-5.5 Instant becomes ChatGPT 's new default**: OpenAI rolled out **GPT-5.5 Instant** to ChatGPT and the API as `gpt-5.5-chat-latest`, positioning it as a broad upgrade in **factuality, baseline intelligence, image understanding, and tone**. The launch also bundled stronger personalization: ChatGPT can now use **saved memories, past chats, files, and connected Gmail** , while exposing **" memory sources"** so users can see what context influenced a reply. See the main launch thread from [@OpenAI](https://x.com/OpenAI/status/2051709028250915275), rollout details from [@OpenAI](https://x.com/OpenAI/status/2051709035347694047), product commentary from [@michpokrass](https://x.com/michpokrass/status/2051709536130802022), and reactions from [@ericmitchellai](https://x.com/ericmitchellai/status/2051711459886059963) and [@sama](https://x.com/sama/status/2051716909629153573).

  * **OpenAI also published more infra detail around real-time products** : [@OpenAIDevs](https://x.com/OpenAIDevs/status/2051453905343828350) shared a writeup on rebuilding the **WebRTC stack** for ChatGPT voice and the Realtime API using a **thin relay** plus a **stateful transceiver** to reduce latency and keep conversations at speech pace. This fits the broader signal around an imminent voice refresh, noted by [@kimmonismus](https://x.com/kimmonismus/status/2051571219040735423) and [@sama](https://x.com/sama/status/2051464865634742334).

  * **Developer-side OpenAI agent tooling keeps expanding** : [@OpenAIDevs](https://x.com/OpenAIDevs/status/2051725072873001338) announced the **Agents SDK for TypeScript** , including **sandbox agents** and an **open-source harness**. Separately, OpenAI continued pushing Codex UX and automation, including task progress UI highlighted by [@reach_vb](https://x.com/reach_vb/status/2051655026574057593) and **Auto Review** for lower-friction approvals in [@reach_vb](https://x.com/reach_vb/status/2051782942314078553). Community sentiment suggests 5.5 is especially strong for **high-token-budget coding and non-coding workflows** , per [@sama](https://x.com/sama/status/2051724685231214650) and [@sama](https://x.com/sama/status/2051783339502375418).




**Coding agents, harness design, and benchmark pressure**

  * **Harness quality is becoming a first-class differentiator** : A recurring theme across the day was that model quality alone no longer explains agent performance. [@Vtrivedy10](https://x.com/Vtrivedy10/status/2051451869017584112) argued the field is mixing incompatible assumptions about **native post-trained harnesses** , **open harnesses** , and "AGI-like" model generalization; the practical takeaway is that **Model -Harness-Task fit** matters more than abstract benchmark narratives. A complementary post from [@Vtrivedy10](https://x.com/Vtrivedy10/status/2051674478648742002) emphasized that talking to base or minimally wrapped models makes clear how much productized agents depend on **instructions, tools, context packing, and measurement loops**. [@sydneyrunkle](https://x.com/sydneyrunkle/status/2051637638239567953) pointed to a LangChain post on the "anatomy" of long-running harnesses, while [@masondrxy](https://x.com/masondrxy/status/2051714091924828480) argued for **ACP-style decoupling** so teams can swap **CLI/TUI/GUI/IDE** frontends without changing the underlying harness.

  * **Agent coding UX is fragmenting, with real disagreement on winners** : There were multiple anecdotal comparisons of agent shells and coding assistants. [@0xSero](https://x.com/0xSero/status/2051689733793755405) ranked **Droid** above Pi, Amp, OpenCode, and Codex CLI. [@teortaxesTex](https://x.com/teortaxesTex/status/2051549309707928028) said **Hermes** currently beats deepseek-tui and OpenCode on **success rate, speed, and cost** , adding cache-hit details in a follow-up [comparison](https://x.com/teortaxesTex/status/2051551506134896976). On the commercial side, [@kimmonismus](https://x.com/kimmonismus/status/2051515496567292310) cited TickerTrends data claiming **Codex surpassed Claude Code in downloads** after late-April releases, while several developers reported that **Claude Code utility feels relatively flat** versus last fall, e.g. [@TheEthanDing](https://x.com/TheEthanDing/status/2051516204607578132) and [@finbarrtimbers](https://x.com/finbarrtimbers/status/2051652067480179020).

  * **New coding benchmark: ProgramBench shows how far "whole-repo from scratch" still is**: Meta researchers introduced **ProgramBench** , a 200-task benchmark asking models to generate substantial software artifacts like **SQLite, FFmpeg, and a PHP compiler** from an executable spec and without starter code or internet access. [@jyangballin](https://x.com/jyangballin/status/2051677497562210552) presented it as an end-to-end repo generation test; [@OfirPress](https://x.com/OfirPress/status/2051678633035809159) summarized the headline result bluntly: **top accuracy is 0%**. Discussion quickly focused on whether the headline metric is too harsh: [@scaling01](https://x.com/scaling01/status/2051733949877985349) noted models can still pass **> 50% of tests per task on average**, while [@OfirPress](https://x.com/OfirPress/status/2051757679283143089) defended the all-tests criterion as necessary because partial implementations can game average-pass metrics.

  * **Practical coding automation keeps moving into CI/security** : [@cursor_ai](https://x.com/cursor_ai/status/2051739625958584659) launched agents that monitor GitHub and **automatically fix CI failures**. [@cognition](https://x.com/cognition/status/2051708729880416614) introduced **Devin for Security** , including claims of automated vuln remediation at enterprise scale and an example where Devin Review flagged a malicious axios release before public disclosure in [@cognition](https://x.com/cognition/status/2051708731671331171).




**Inference, systems, and efficiency: Gemma 4 drafters, SGLang/RadixArk, and provider economics**

  * **Gemma 4 gets multi-token prediction drafters across the open stack** : Google released **Gemma 4 MTP drafters** , promising **up to 3 × faster decoding with no quality degradation**. The launch came through [@googlegemma](https://x.com/googlegemma/status/2051713412431007808), [@googledevs](https://x.com/googledevs/status/2051700498328346945), and ecosystem posts from [@osanseviero](https://x.com/osanseviero/status/2051695861801820475), [@mervenoyann](https://x.com/mervenoyann/status/2051702372339003841), and [@_philschmid](https://x.com/_philschmid/status/2051752856319926475). The key engineering detail is that this is **speculative-style decoding integrated into open tooling** , with day-0 or near-day-0 support in **Transformers, vLLM, MLX, SGLang, Ollama, and AI Edge**. [@vllm_project](https://x.com/vllm_project/status/2051744111116574950) specifically announced a ready Docker image for Gemma 4 on vLLM.

  * **RadixArk raises a massive seed around SGLang + Miles** : One of the bigger infra financings was **RadixArk 's $100M seed**, built around the **SGLang** inference stack and **Miles** for large-scale RL/post-training. [@BanghuaZ](https://x.com/BanghuaZ/status/2051650922892476904) framed the company as spanning inference, training, RL, orchestration, kernels, and multi-hardware systems; [@Arpan_Shah_](https://x.com/Arpan_Shah_/status/2051651802484150278) and [@GenAI_is_real](https://x.com/GenAI_is_real/status/2051703162722263180) emphasized the goal of making frontier-grade infrastructure **open and production-grade** , rather than forcing every team to rebuild scheduling, KV-cache management, and rollout systems from scratch. Community endorsements came from [@ibab](https://x.com/ibab/status/2051690211873308892) and [@multiply_matrix](https://x.com/multiply_matrix/status/2051698056316526651).

  * **Inference economics are now highly provider-specific** : [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2051735255044997215) compared **MiniMax-M2.7** across six providers and found major differences in **tokens/sec, cache discounting, and blended cost**. **SambaNova** led raw speed at **435 output tok/s** , while **Fireworks** looked stronger on the speed/price frontier for many workloads. Separately, [@teortaxesTex](https://x.com/teortaxesTex/status/2051525774851682409) highlighted how **cache-hit rates** dominate cost on some agent workloads, calling cache optimization "the main axis of cost reduction with V4."

  * **Cold-start and distributed training remain active systems bottlenecks** : [@kamilsindi](https://x.com/kamilsindi/status/2051674592750494094) described a system that cut model cold starts **60 ×**, from minutes to seconds, by serving weights from **GPUs already holding them** rather than cloud storage. On the training side, [@dl_weekly](https://x.com/dl_weekly/status/2051693914868871205) highlighted Google DeepMind's **Decoupled DiLoCo** , which reportedly achieved **88% goodput vs. 27%** for standard data parallel at scale while using ~**240 × less inter-datacenter bandwidth**.




**Agents, RL environments, observability, and long-horizon research**

  * **RL infra is shifting from "single generation + reward" to long-running action systems**: [@adithya_s_k](https://x.com/adithya_s_k/status/2051660068471603352) released a guide comparing **RL environment frameworks** for the LLM era, focusing on what scales to **thousands of environments**. A detailed survey by [@ZhihuFrontier](https://x.com/ZhihuFrontier/status/2051691071634301064) contrasted traditional RLVR with **agentic RL** , pointing to systems such as **Forge, ROLL, Slime, and Seer** and recurring concerns like **TITO consistency** , rollout latency, prefix-tree merging, and global KV caches.

  * **Long-horizon failures are increasingly framed as horizon problems, not just capacity problems** : [@dair_ai](https://x.com/dair_ai/status/2051679862788878354) summarized a Microsoft Research paper arguing that **goal horizon alone can be the training bottleneck** , with **macro actions / horizon reduction** stabilizing training and improving long-horizon generalization. This rhymes with broader frustration that current benchmarks and public evals still underweight true long-horizon behavior.

  * **Observability is maturing into a feedback-driven improvement loop** : [@hwchase17](https://x.com/hwchase17/status/2051708980435853513) and [@LangChain](https://x.com/LangChain/status/2051709642716135729) argued that traces alone are insufficient; the key is attaching **direct, indirect, or generated feedback** so observability becomes a **learning system**. [@benhylak](https://x.com/benhylak/status/2051727888639250450) launched **Raindrop Triage** , an agent dedicated to finding and investigating bad agent behavior. [@Vtrivedy10](https://x.com/Vtrivedy10/status/2051727418134593632) laid out the practical loop explicitly: **gather data -> mine errors -> localize which component failed -> apply fix -> test -> repeat**.




**Enterprise verticalization: finance, legal, and proactive assistants**

  * **Anthropic and Perplexity both pushed hard into finance workflows** : Anthropic launched **financial-services agent templates** for work such as **pitch generation, valuation review, KYC screening, and month-end close** , with integrations into providers like **FactSet, S &P Global, and Morningstar**, via [@claudeai](https://x.com/claudeai/status/2051679629488865498) and summarized by [@kimmonismus](https://x.com/kimmonismus/status/2051681279582540114). Perplexity announced **Perplexity Computer for Professional Finance** , bringing in **licensed data** and **35 dedicated workflows** for repeat analyst work, in [@perplexity_ai](https://x.com/perplexity_ai/status/2051693893473935372) and [@AravSrinivas](https://x.com/AravSrinivas/status/2051694381137350661). Both launches reflect a clearer move from generic copilots to **workflow-packaged vertical products**.

  * **Perplexity also expanded into medical/professional health sources** : [@perplexity_ai](https://x.com/perplexity_ai/status/2051710342242480538) announced premium access to **NEJM, BMJ** , and additional medical journals/databases, enabling "deep and wide research" on trusted clinical sources; [@AravSrinivas](https://x.com/AravSrinivas/status/2051711236224761983) framed this as a product for healthcare-grade information retrieval.

  * **Proactive assistant surfaces are becoming a product category** : [@kimmonismus](https://x.com/kimmonismus/status/2051618156385366305) reported a leak around **Anthropic Orbit** , described as a proactive assistant that synthesizes data from **Gmail, Slack, GitHub, Calendar, Drive, and Figma** without explicit prompting. Manus also added **recommended connectors** that are suggested in context when needed, per [@ManusAI](https://x.com/ManusAI/status/2051681463389610209).




**Top tweets (by engagement)**

  * **Anthropic 's finance template launch** drew outsized attention: [@claudeai](https://x.com/claudeai/status/2051679629488865498) announced ready-to-run Claude agent templates for financial services with **22.9K engagement** , one of the biggest clearly technical/AI-product posts in the set.

  * **OpenAI 's GPT-5.5 Instant launch** dominated discussion: the main rollout thread from [@OpenAI](https://x.com/OpenAI/status/2051709028250915275) exceeded **8.2K engagement** , with follow-on personalization details also performing strongly.

  * **Gemma 4 speedups landed as a major open-model systems update** : [@googledevs](https://x.com/googledevs/status/2051700498328346945) on **3 × faster Gemma 4** and [@googlegemma](https://x.com/googlegemma/status/2051713412431007808) both broke through, reflecting strong interest in inference improvements that preserve quality.

  * **Perplexity 's finance launch** also resonated broadly: [@perplexity_ai](https://x.com/perplexity_ai/status/2051693893473935372) reached **2.5K engagement** , suggesting that **licensed-data workflow products** are now seen as strategically important, not just niche enterprise packaging.




* * *

# **AI Reddit Recap**

## **/r/LocalLlama + /r/localLLM Recap**

### **1\. Gemma 4 MTP and llama.cpp Speculative Decoding**

  * **[Gemma 4 MTP released](https://www.reddit.com/r/LocalLLaMA/comments/1t4jq6h/gemma_4_mtp_released/)** (Activity: 1116): **Google released Multi-Token Prediction (MTP) drafter checkpoints for Gemma 4, with Hugging Face model cards for**`gemma-4-31B-it-assistant`**,**`gemma-4-26B-A4B-it-assistant`**,**`gemma-4-E4B-it-assistant`**, and**`gemma-4-E2B-it-assistant`**, described in Google 's [blog post](https://blog.google/innovation-and-ai/technology/developers-tools/multi-token-prediction-gemma-4/). The MTP setup adds a smaller/faster draft model for speculative decoding, where several draft tokens are proposed and then verified in parallel by the target model, claiming **_**" up to 2x"**_**decoding speedups while preserving identical output quality versus standard generation; one commenter notes the E2B drafter is only**`78M`**parameters. A technical commenter also shared an updated visual explainer of MTP/speculative decoding for Gemma 4:[Maarten Grootendorst's guide](https://newsletter.maartengrootendorst.com/i/193064129/multi-token-prediction-mtp-with-gemma-4).**

    * A commenter linked a technical visual guide explaining **multi-token prediction (MTP) with Gemma 4** , including implementation snippets and diagrams: [Maarten Grootendorst's guide](https://newsletter.maartengrootendorst.com/i/193064129/multi-token-prediction-mtp-with-gemma-4). This is the main substantive resource in the thread for understanding how Gemma's MTP-style decoding/drafting works.

    * One technical detail noted is that the **E2B model includes a**`78M`**draft model** , implying a relatively small auxiliary model used for speculative or multi-token drafting. The comment highlights the draft model size as unusually compact, which is relevant for latency/throughput tradeoffs in MTP-style inference.

  * **[Llama.cpp MTP support now in beta!](https://www.reddit.com/r/LocalLLaMA/comments/1t3guzw/llamacpp_mtp_support_now_in_beta/)** (Activity: 1103): `llama.cpp`**has beta MTP (Multi-Token Prediction) support via[PR #22673](https://github.com/ggml-org/llama.cpp/pull/22673), initially targeting Qwen3.x MTP models and loading the MTP component as a separate model from the same GGUF, with its own context/KV cache rather than a separate GGUF artifact. The PR adds post-**`ubatch`**MTP consumption to propagate hidden features correctly across ubatches and a small speculative decoding path depending on partial**`seq_rm`**support; reported Qwen3.6 27B / 35B-A3B tests show ~**`75%`**steady-state acceptance with**`3`**draft tokens and usually >2× token-generation throughput over baseline.** Commenters view this as potentially one of the largest `llama.cpp` performance improvements to date, especially for dense models, and expect it to narrow token-generation speed gaps with vLLM alongside tensor parallelism. There is demand for a technical comparison of speculative decoding methods--MTP, EAGLE-3, DFlash, DTree, n-gram--covering draft-model requirements, context reuse, and model suitability.

    * Commenters frame **MTP / multi-token prediction** as potentially a major llama.cpp throughput improvement, especially for **dense models** , while expecting less benefit for **MoE** architectures. There is interest in comparing it against other speculative decoding approaches such as **EAGLE-3** , **DFlash** , **DTree** , and `ngram`, particularly around whether they require separate draft models and how well they reuse existing context.

    * One tester reported llama.cpp's beta MTP support is _" way faster than ik_llama.cpp implementation currently"_ in quick local testing. They linked a GGUF surgery script that extracts the MTP layer from **am17an 's Q8_0 model** and injects it into an existing **Qwen 3.6 27B GGUF** : [gist.github.com/buzz/1c439684d5e3f36492ae9f64ef7e3f67](https://gist.github.com/buzz/1c439684d5e3f36492ae9f64ef7e3f67), reportedly working with **Bartowski 's Q6_K** quantization.




[ Read more ](https://www.latent.space/p/ainews-silicon-valley-gets-serious)

---

## [🔬Doing Vibe Physics — Alex Lupsasca, OpenAI](https://www.latent.space/p/lupsasca)
*🔬 Latent Space | 2026-05-05*

Some people are going crazy over GPT 5.5. _Some_ people. This is the story of the [Jagged](https://www.notion.so/Tanishq-https-x-com-iScienceLuvr-2c312774e7a88187a391e2a67b42cd56?pvs=21) [Frontier](https://www.hbs.edu/faculty/Pages/item.aspx?num=64700). People who use AI to write emails or even code implementation work [find the lift moderate](https://www.reddit.com/r/codex/comments/1su4jik/did_gpt55_actually_impress_you_or_does_it_feel/) whereas people pushing the limits of the model are figuring out that the [limits just moved outwards](https://www.youtube.com/watch?v=kCMgUvnpzsM).

[Alex Lupsaska](https://lupsasca.com/) has been tracking this limit for a year and a half now. "When GPT5 came out, it was **able to reproduce one of my best papers**(that took a very long time to come up with)**in 30 minutes**."

But Alex also notes that this shift was mostly invisible.

> _I remember when GPT-5 came out … on Twitter, the reception was lukewarm. A lot of people were like, well, we expected a lot more, and it's not better at writing email. And I remember thinking, well, okay, GPT-3 could write email. How much better can it get at writing email? That's not the point. **But at the science frontier, the capabilities were really taking off.**_

We walk through his paper and more with him in today's Science pod! [Watch here](https://youtu.be/9d899Ram9Bs).

## The "Oscar for physics"

Alex made an early splash in his career with breakthroughs in our understanding of black holes. He's also known for [Black Hole Explorer](https://www.sciencenews.org/article/alex-lupsasca-black-hole-photon-ring) and [an iPhone app that makes visualizing black holes fun and interactive to regular audiences](https://arxiv.org/abs/2603.05810). Alex won the 2024 New Horizons in Fundamental Physics Breakthrough Prize. Known as the "Oscar for physics" this is arguably the most prestigious prize an early stage theoretical physicist can win.[1](https://www.latent.space/feed#footnote-1)

Alex first saw promise for AI in theoretical physics after he asked o3 for help on his research. In the podcast, Alex recalls asking GPT for help with a calculation that would have taken days, and getting a result in eleven minutes. 

[](https://substackcdn.com/image/fetch/$s_!xPdC!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4e4bb428-23e6-47d2-b229-007983cd5d80_1070x1528.png)[tweets](https://x.com/ALupsasca/status/1978823200986316870)

He immediately recognized how impactful AI would be for his work even as though his physicist colleagues and the larger community gave it a lukewarm or skeptical reception.

## The Move 37 Moment for AI x Physics

GPT-5 had just been released, and Alex tried asking it to solve a problem in a just published paper. GPT-5 said no answer. But [Mark Chen, CRO of OpenAI](https://www.linkedin.com/in/markchen90), pushed a bit harder, and had Alex prime the model with a textbook warmup problem, which it easily solved[2](https://www.latent.space/feed#footnote-2). After using this "priming" trick, GPT-5 was able to reproduce his full result in eleven minutes (yes, the paper was released after the model's training cutoff).

"This changes everything." Alex notes that **we seem to be on the edge of a massive change in theoretical physics reasoning.** A year prior LLMs were just starting do correct math. Now ChatGPT could reproduce his hardest paper in the time it takes to get a coffee.

Alex was on sabbatical at Vanderbilt, and he joined OpenAI to start pushing the boundary of AI's ability to accelerate physics.

## "AI solved the problem before the plane landed"

Alex began to put GPT through it's paces, reaching out to colleagues for problems they were stuck on. His old PhD advisor ([Prof. Andrew Storminger at Harvard](https://en.wikipedia.org/wiki/Andrew_Strominger)) had an insidght about certain physical quantities known as "single-minus gluon tree amplitudes". 

In certain cases, these amplitudes [may be non-zero](https://x.com/OpenAI/status/2022390100055986540?s=20) when previously shown to always vanish[3](https://www.latent.space/feed#footnote-3). The team pushed this intuition forward, and came up with a formula for these quantities that appeared nonzero, but which was otherwise completely intractable. 

[](https://substackcdn.com/image/fetch/$s_!9aPW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa9025108-2fce-4803-aed3-0ff1f7d0579b_1314x452.png)A key equation [from the paper](https://arxiv.org/pdf/2602.12176) spans a quarter of a page, involving a sum of 32 terms, each of which is a product of four terms, each encoding a complicated formula. Just computing this by hand was a Herculean effort by the lead author!

Spending over a year on this problem, no real progress was made.

Prof. Storminger planned to visit OpenAI to work on the problem the week after the initial conversation started. In that one week ChatGPT fully solved the problem, as Alex recalled, **before Prof. Storminger 's plane even landed.**

What was interesting is not only that ChatGPT solved this problem, but how it solved it. The model quickly realized found a limiting case (known as the "half-collinear regime"), that in hindsight has a nice intuitive explanation[4](https://www.latent.space/feed#footnote-4). Taking this limit, the gnarly results collapsed down to a simple and intuitive formula!

The last step was to prove this intuitive formula. The team started with a fresh session, gave a prompt with the context of what they previously learned, and let the model loose. Not only was ChatGPT able to reproduce the previous result, it was able to prove it using a technique unknown to the authors!

## The Vibe Physics moment

With a concrete success in the bag, the team asked if they could generate new physics from scratch using ChatGPT. They took on what they felt to be a harder problem, looking at the graviton, a proposed particle that should appear when one combines gravity and quantum mechanics.[5](https://www.latent.space/feed#footnote-5) They wrote up a simple prompt asking ChatGPT to perform the same research as the gluon paper but instead for gravitons. And then hit go!

What came next was truly "vibe physics", with ChatGPT pushing out 110 pages of novel physics, new calculations, and novel techniques. This was over the course of a day, with most interactions the familiar following the now familiar pattern for anyone who uses a coding agent:
    
    
    GPT: Here's your <long, detailed, awesome result>. 
         Would you like me to do <another really cool thing>?
    Alex: Yes, please do!
    GPT: <does the really cool thing>

And for those who look deeply, this really was not just a direct 1-1 mapping between gluons and gravitons. **ChatGPT imported new techniques that were necessary due to the nature of gravitons** , and used them flawlessly.

[](https://substackcdn.com/image/fetch/$s_!y4QO!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F217edc89-2b63-4f7e-8c76-0918aaa14efd_1116x1326.png)[context](https://x.com/ALupsasca/status/2029256973473239041)

They spent the next three weeks verifying all the results. And voila! A [new paper](https://arxiv.org/abs/2603.04330) featuring novel results in quantum gravity, generated in less than three days total. Truly a "Feel the AGI moment".

[](https://substackcdn.com/image/fetch/$s_!PvEP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4f1c005a-8a1d-44e1-969e-3ec5534dbc06_1412x1052.png)

For those interested, there's a [blog post](https://openai.com/index/extending-single-minus-amplitudes-to-gravitons/) with the [full transcript](https://cdn.openai.com/pdf/gluon-to-graviton-paper.pdf) from initial prompt to final paper. Even if you know no physics, it's crazy seeing pages of correct calculations fall out of simple prompts such as "Yes calculate outside of SD first. This is the first step."

## Out-of-domain = new knowledge

The thing that is qualitatively different between **Vibe Physics** and Vibe Coding is that **Vibe Physics means actually extending the frontier of human knowledge**. Looking at the Gluon and Graviton results, they seem in retrospect, like many results in physics and math, like natural extensions of what we already know. This is in fact part of what makes them beautiful. But this was a problem that stumped experts in the domain for a year. Although it does still have a bit of a recombinant flavor, _this thing has never been done before._

It may be that there are still large classes of problems that AI won't do well on, and approaches that an AI might not think to take. This is the "taste" that everyone has been talking about. Alex told us that these capabilities, however, allow him to explore many possible avenues in order to map out much more ambitious problems to tackle. With AI able to output results basically as fast as we can conceive and validate them, the scope of what one theorist can hope to achieve has just gotten a lot, lot bigger.

# 

[1](https://www.latent.space/feed#footnote-anchor-1)

When doing research for this podcast, we asked AI if this was the case, and it suggested the IUPAP award, which it turns out Alex also won in 2024.

[2](https://www.latent.space/feed#footnote-anchor-2)

This is an interesting prompting trick. Get the model thinking along the right lines by solving an easier, but related problem.

[3](https://www.latent.space/feed#footnote-anchor-3)

To be pedantic, the original claim is still true in the case of "3+1 dimensional spacetime", the spacetime that models our reality. The insight here was that if we have two dimensions of time and two dimensions of space, some magic happens with the math which breaks the original assumption. What does it mean to have two time dimensions and two space dimensions? This is a fun discussion we unfortunately didn't have time to get into.

[4](https://www.latent.space/feed#footnote-anchor-4)

For experts, this is the equivalent to one particle decaying into n-1 other particles.

[5](https://www.latent.space/feed#footnote-anchor-5)

Much has been written about this particle, and there are better references than this blog. The only thing relevant for this is that gravitons are an analog to gluons, but for gravity. And that the concept of helicity is more complicated, but one can still define a meaningful analog to the gluon paper.

---

---
title: "Latent Space — 2026-05-18"
date: 2026-05-18
source: Latent Space
type: ai-news
---

# 🔬 Latent Space — 2026-05-18

> swyx 開發者簡報，未公開專案 + 工程視角
> 來源：[Latent Space](https://www.latent.space/feed)

---

## [[AINews] Cerebras' $60B IPO: Slowly, then All at Once](https://www.latent.space/p/ainews-cerebras-60b-ipo-slowly-then)
*🔬 Latent Space | 2026-05-16*

We normally focus on technical stories, but occasional large fundraisings are noteworthy in themselves, and the Cerebras IPO (after one [pulled S-1](https://www.youtube.com/watch?v=7UGjf080qag) and a fantastic [750MW partnership](https://openai.com/index/cerebras-partnership/) and [$10-$20B stake/deal](https://www.reuters.com/technology/openai-spend-more-than-20-billion-cerebras-chips-receive-equity-stake-2026-04-17/) with OpenAI) this week, certainly qualifies as a growing theme supporting [the Inference Inflection](https://www.latent.space/p/ainews-the-inference-inflection), just 6 months after [the shock execuhire of Groq by NVIDIA for $20B](https://news.smol.ai/issues/25-12-24-nvidia-groq).  ended today at $280, a market cap of $60 billion, which is tremendous validation for [Big Chip](https://x.com/vikramskr/status/2054264737400328678?s=12) and [their believers](https://x.com/shenlucinda/status/2055033736031592843?s=12).

This image [from Amir Efrati](https://x.com/amir/status/2054940414688494029?s=12) summarizes the Decade of Cerebras:

[](https://substackcdn.com/image/fetch/$s_!vBnf!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5fea6bb8-3298-434e-afef-3eea148ba10c_2048x1263.png)

Cerebras' [financials](https://x.com/negligible_cap/status/2045239088169828550?s=12) are now fully public, but the focus of discussions center around the supply:

More details below, and the Head Research Scientist of Cerebras speaks at AIE Singapore later today on the livestream:

> AI News for 5/14/2026-5/15/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

## **Headline Story: Cerebras IPO recap, technical details, and company journey**

**Cerebras returned to the timeline as an IPO story, with investors and adjacent infra voices framing the company as a long-running contrarian hardware bet that finally looks vindicated.** The most directly relevant tweet is from investor Ishan N. Taneja, who said he "didn't believe" early Cerebras claims, then concluded the skeptic he doubted "was totally right," praising Cerebras for persistence, execution, and for having "built a banger chip," while noting this was Hanabi's first IPO [@ishanit5](https://x.com/ishanit5/status/2055000270837543052). A second Cerebras-specific datapoint came from CNBC's Deirdre Bosa quoting Cerebras CFO Bob Komin pushing back on the "small models only" narrative: Komin said Cerebras serves models of all sizes, that there is "no limit" to the size of models it can serve, and that Cerebras is currently serving **trillion-parameter models** , including internal OpenAI models, specifically naming **" OpenAI 5.4 and 5.5"** [@dee_bosa](https://x.com/dee_bosa/status/2055351401472020949). A nearby contextual tweet from Apoorv Vyas explicitly linked "the Cerebras IPO" to a Stanford discussion on compute scarcity, inference demand, routing, and open source, suggesting the IPO was being interpreted not as a generic capital-markets event but as part of the inference infrastructure cycle [@apoorv03](https://x.com/apoorv03/status/2055479206545646040).

## **Facts vs. opinions**

### **Facts directly stated in tweets**

  * Cerebras is being discussed in the context of an **IPO** [@ishanit5](https://x.com/ishanit5/status/2055000270837543052), [@apoorv03](https://x.com/apoorv03/status/2055479206545646040).

  * Cerebras CFO **Bob Komin** said:

    * Cerebras serves **all model sizes**.

    * There is **" no limit"** to model size it can serve.

    * Cerebras is serving **trillion-parameter models**.

    * It is serving **internal OpenAI models** , specifically **OpenAI 5.4 and 5.5** [@dee_bosa](https://x.com/dee_bosa/status/2055351401472020949).




### **Opinions / interpretations**

  * Cerebras "did controversial things for the right reasons," "the team slaps," and "they built a banger chip" are investor judgments, not independently verified facts [@ishanit5](https://x.com/ishanit5/status/2055000270837543052).

  * The implication that the IPO is a validation of Cerebras's long-term strategy is an interpretation emerging from the investor tone and surrounding infra discourse, not a formal claim from the company in these tweets.

  * The CFO's claim that there is "no limit" to model size is partly factual framing and partly marketing language; engineers should read it as "the company believes its serving architecture scales to current frontier workloads," not literally unbounded compute.




## **Technical details and numbers surfaced in the discussion**

The tweet corpus is light on historical specs, but it does contain several notable **operational claims** relevant to Cerebras's technical positioning:

  * **Trillion-parameter model serving** : Cerebras CFO says the company is currently serving trillion-parameter models [@dee_bosa](https://x.com/dee_bosa/status/2055351401472020949).

  * **Named customers/workloads** : Komin specifically says these include **internal OpenAI 5.4 and 5.5** [@dee_bosa](https://x.com/dee_bosa/status/2055351401472020949).

  * **Strategic wedge** : The framing is clearly **inference/serving** , not just training. Apoorv ties the IPO discussion to "compute scarcity," "rising inference demand," and "model routing" [@apoorv03](https://x.com/apoorv03/status/2055479206545646040).




Those tweets align with Cerebras's broader known positioning in the market: wafer-scale hardware, extreme on-chip memory bandwidth, and system architectures optimized to reduce the bottlenecks that appear when serving large models with low latency. Even though those specific chip specs are not in the tweet set, the CFO's "trillion-parameter" comment is technically meaningful because it implies the company wants to be understood as a serious serving platform for frontier-scale models, not a niche accelerator for mid-sized open models.

## **Cerebras 's journey: why this IPO resonated**

Cerebras has spent years in the "ambitious but contentious" bucket in AI hardware. The investor comment captures the core narrative arc well: the company took a path that many found implausible or commercially dubious, but did so with persistence and enough execution to stay alive through multiple compute cycles [@ishanit5](https://x.com/ishanit5/status/2055000270837543052).

The subtext of that praise is important for hardware engineers:

  * Cerebras has long represented a **non-NVIDIA architectural thesis**.

  * Its strategy has been to attack the scaling problem with a **different physical and system design philosophy** , rather than merely competing on conventional accelerator economics.

  * That made it inherently controversial, because the market often discounts bespoke architectures unless they win a very specific workload.




The IPO recap chatter suggests the company's story has shifted from "can this architecture survive?" to "is this exactly the kind of differentiated serving stack the market now needs?"

That shift is happening because the AI infra market has also shifted:

  * From pure training prestige toward **inference economics**.

  * From benchmark snapshots toward **serving giant models in production**.

  * From GPU abundance assumptions toward **compute scarcity and routing discipline** [@apoorv03](https://x.com/apoorv03/status/2055479206545646040).




In that environment, a company that can credibly say it serves **trillion-parameter internal frontier models** gets a very different hearing than it would have a few years ago [@dee_bosa](https://x.com/dee_bosa/status/2055351401472020949).

## **Different perspectives**

### **Supportive / bullish**

  * The most bullish take is from investor Ishan N. Taneja: skepticism gave way to admiration, with emphasis on **persistence** , **execution** , and a **successful contrarian chip bet** [@ishanit5](https://x.com/ishanit5/status/2055000270837543052).

  * Bob Komin's quote is also strategically bullish: it reframes Cerebras as a platform for **frontier-scale inference** , not a side player [@dee_bosa](https://x.com/dee_bosa/status/2055351401472020949).

  * Apoorv's comment places Cerebras in the center of a live systems question--**compute scarcity amid rising inference demand** --which is where a differentiated serving architecture could matter most [@apoorv03](https://x.com/apoorv03/status/2055479206545646040).




### **Neutral / analytical**

  * A neutral read is that Cerebras's IPO matters less as a public-markets event than as a signal that investors believe there is room for **non-GPU-default infra companies** in the frontier stack.

  * Another neutral takeaway: even if Cerebras has genuine technical differentiation, the important question is not "is the chip elegant?" but "can it sustain utilization, software compatibility, and commercial adoption in a market increasingly organized around incumbent ecosystems?"




### **Skeptical / implicit counterpoints**

No tweet in the supplied set directly attacks the Cerebras IPO. But there are implicit reasons an expert audience would remain cautious:

  * "No limit to model size" is standard executive rhetoric; in practice, limits show up in **memory hierarchy, batch/latency tradeoffs, interconnect behavior, software ergonomics, and workload mix**.

  * Serving internal OpenAI workloads is a strong claim, but without details on **share of traffic, latency tier, cost/token, utilization, or exact deployment role** , it is hard to know whether this reflects broad strategic reliance or narrower targeted usage.

  * The history of AI hardware is full of technically impressive architectures that failed commercially because software, developer adoption, or ecosystem gravity overwhelmed raw hardware merit.




## **Why it matters now**

The Cerebras IPO story lands at a moment when AI infra is being repriced around a few hard truths visible elsewhere in the tweet set:

  * **Inference is becoming the dominant compute market**. Pearl, Together, and others are explicitly talking about inference economics and token costs [@prlnet](https://x.com/prlnet/status/2055339314205139226), [@simran_s_arora](https://x.com/simran_s_arora/status/2055348155051569474).

  * **Serving giant models is now a product requirement** , not just a lab flex. Multiple tweets discuss trillion-scale models, large-model cadence, and rapid RL/post-training-driven improvements [@scaling01](https://x.com/scaling01/status/2055018330365345896), [@kimmonismus](https://x.com/kimmonismus/status/2055197338092662824).

  * **Capital intensity is under scrutiny**. Kimmonismus notes hyperscaler capex crossing **$600B** and a large gap between AI infra spending and AI revenue, warning that the market is watching infra economics closely [@kimmonismus](https://x.com/kimmonismus/status/2055293526125232332).




In that context, Cerebras matters if--and only if--it can make a durable case that a nonstandard architecture can improve the economics or latency profile of frontier inference enough to justify ecosystem switching costs.

## **Broader context: official claims vs independent validation**

Officially, the strongest claim in the tweet set is from CFO Bob Komin: **Cerebras already serves trillion-parameter OpenAI internal models** [@dee_bosa](https://x.com/dee_bosa/status/2055351401472020949).

What is missing from the tweet set is independent benchmark-style validation:

  * no cost-per-token comparison,

  * no latency percentile data,

  * no throughput numbers,

  * no context-length specifics,

  * no software compatibility details,

  * no utilization figures.




So the right technical posture is:

  * treat the OpenAI-serving claim as **important and credible enough to watch** ;

  * do **not** overread it as full proof of broad superiority.




The IPO recap, then, is less "Cerebras won" and more "Cerebras stayed alive long enough for the market to become more favorable to its thesis."

# **AI Twitter Recap**

**Codex, GitHub Copilot App, and the New Coding-Agent Surface Area**

  * OpenAI's Codex mobile/app rollout dominated product chatter. Users described building websites from a bar, controlling Macs from iPhone, and treating laptops as "satellite devices" while an always-on Mac mini runs sessions in the background [@flavioAd](https://x.com/flavioAd/status/2055021982601605225), [@nickbaumann_](https://x.com/nickbaumann_/status/2055066537002725393), [@PaulSolt](https://x.com/PaulSolt/status/2055057277334208987), [@rileybrown](https://x.com/rileybrown/status/2055093278161428726).

  * **Codex is rapidly becoming a multi-surface agent platform** : tweets this cycle point to a meaningful broadening of where and how coding agents run: mobile-first workflows via [Codex Mobile walkthroughs](https://x.com/rileybrown/status/2055093278161428726), iPad/VPS session management from [@npew](https://x.com/npew/status/2055131618789265779), Telegram/home-server remote setups from [@itsclivetime](https://x.com/itsclivetime/status/2055144998270824515), and hints of "locked use" for Mac control while the machine is locked from [@kimmonismus](https://x.com/kimmonismus/status/2055262250701574359). OpenAI's dev team also shared adoption figures via [@etnshow](https://x.com/etnshow/status/2055220392030278100): **4M+ weekly active users** , **5x more messages per user** , and **1M+ app downloads in the first week**.

  * **The surrounding ecosystem is moving quickly to plug into Codex rather than compete only at the app layer** : [Ollama added Codex app support](https://x.com/ollama/status/2055100589428658462) with local/open-model launch paths and cloud model recommendations; [Zed now supports ChatGPT subscription access in its agent](https://x.com/zeddotdev/status/2055335727483781624), preserving the same subscription/rate-limit model as Codex; and third-party extensions are appearing, including [MagicPath as a native canvas inside Codex](https://x.com/skirano/status/2055364115560878480) and a portable `/goal` command extracted into MCP/slash-command form by [@secemp9](https://x.com/secemp9/status/2055339137318724047). Community momentum was visible in meetup reports from [London](https://x.com/Andy_AJT/status/2055297191128768576), [Portugal](https://x.com/TimHaldorsson/status/2055206416747507785), and [Paris planning](https://x.com/borvibe/status/2055322241340960810).

  * **GitHub is making a parallel bet on the coding harness, not just the model** : the VS Code/Copilot team emphasized that the user experience is shaped by the **coding harness** --context assembly, tool use, execution loops, memory--more than by the base model alone in [their behind-the-scenes post shared by @code](https://x.com/code/status/2055317356910367189) and [@pierceboggan](https://x.com/pierceboggan/status/2055322165969604966). Product features highlighted this week include **agent merge** from [@davidfowl](https://x.com/davidfowl/status/2055148986340905020), and **terminal risk assessment badges** with AI explanations for commands from [@code](https://x.com/code/status/2055408023506469337). The broader trend is clear: the competitive frontier is shifting from "best model" toward **best harness + UX + integrations**.




**Agent Harnesses, Search, Evaluation, and Reliability Engineering**

  * **Search for coding agents is being rethought around primitives, not embeddings** : the strongest thread here is the "grep/search over vector DBs" argument. [@omarsar0 highlighted](https://x.com/omarsar0/status/2055317577031975269) a paper showing **grep-style text search, wrapped in the right agent harness, can match or beat embedding-based retrieval on coding-agent tasks** ; [@dair_ai echoed the takeaway](https://x.com/dair_ai/status/2055318144592289847). Relatedly, [@lintool joked](https://x.com/lintool/status/2055316434171879757) that the "two-parameter model" for agentic search is **BM25** , and maybe the zero-parameter version is **grep**. This aligns with Cloudflare-adjacent experimentation too: [@YoniBraslaver compared SDK vs MCP on monday.com's GraphQL API](https://x.com/YoniBraslaver/status/2055260079700791544), finding **1 step / 15k tokens** for SDK versus **4 steps / 158k tokens** for a real MCP server--**8.4x token cost** for the same output.

  * **Agent evals and observability are becoming first-class infra problems** : several posts converged on the same theme that evals for autonomous systems are harder, not easier, as agents get longer-horizon and more tool-rich. [@palashshah](https://x.com/palashshah/status/2055410769387303004) called out the difficulty of modern eval design; [@cwolferesearch](https://x.com/cwolferesearch/status/2055437703823372728) compiled a broad benchmark map spanning **Terminal-Bench, Tau-Bench, GAIA, WorkArena, OSWorld, MLE-Bench, PaperBench, GDPval** , and others. New benchmark proposals included [FutureSim](https://x.com/ShashwatGoel7/status/2055336064378720412), which replays real-world events temporally to test continual updating and forecasting in native harnesses like Codex/Claude Code, and follow-up commentary from [@nikhilchandak29](https://x.com/nikhilchandak29/status/2055357580436783595) arguing that **test-time compute scales gracefully in forecasting** too.

  * **Reliability concerns are shifting from hallucinations to system-level failure modes** : [@random_walker](https://x.com/random_walker/status/2055271764662296580) argued that black-box "genie" interfaces increase the verification burden because users can't see reasoning traces, tool use, memory, or intermediate state. [@mitchellh](https://x.com/mitchellh/status/2055380239711457578) made the sharper infra analogy: companies may be drifting into an **" MTTR is all you need"** mindset for AI-generated software, creating resilient catastrophe machines where local metrics look fine while global system comprehensibility decays. On the tooling side, LangChain pushed the other direction with [Interrupt announcements](https://x.com/LangChain/status/2055314236050690086) covering **LangSmith Engine, SmithDB, managed Deep Agents, sandboxes, gateway, and context hub** , while [@ankush_gola11](https://x.com/ankush_gola11/status/2055368456342745098) emphasized **sub-second median write latency** for trace ingestion as a practical requirement for agent observability.




**Training, Optimization, and Inference Efficiency**

  * **Optimizer work is broadening beyond the Adam family again** : [@zacharynado](https://x.com/zacharynado/status/2055077098327285804) summarized the zeitgeist succinctly: the "sloptimizer" field is just getting started with **Shampoo** and **Muon-gen** style methods after the graveyard of Adam variants. Two concrete updates landed: [SODA](https://x.com/tmpethick/status/2055271381890138560), a wrapper that **adds no hyperparameters, removes weight-decay tuning, and improves a base optimizer** , with the notable claim that **SODA[Muon] beats Muon even when Muon gets a tuned weight-decay sweep** ; and general continued interest in Muon/Shampoo from replies and references.

  * **Fast/slow learning and pedagogical supervision were notable training ideas this cycle** : [@agarwl_ described "Learning, Fast and Slow"](https://x.com/agarwl_/status/2055081573083402434), combining **slow learning in weights via RL** with **fast learning in context/prompt ( "fast weights") optimized with GEPA**, claiming better data efficiency, adaptability, and less forgetting than RL alone. On the supervision side, [Pedagogical RL](https://x.com/NoahZiems/status/2055091478024565214) and [Late Interaction's explainer](https://x.com/lateinteraction/status/2055278862255185936) argue for learning not merely from correct outputs but from **correct, teachable rollout distributions** , while [@bradenjhancock summarized](https://x.com/bradenjhancock/status/2055079214156853325) related work on teacher models that are penalized for taking leaps students can't follow.

  * **Inference optimization remains highly active at both systems and model levels** : [@ariG23498 recommended a deep dive on continuous batching](https://x.com/ariG23498/status/2055106570971975977), specifically the need to understand **CUDA streams, events, synchronization, and CPU/GPU decoupling** to avoid idle GPUs in dynamic batching regimes. Meta researchers proposed [Self-Pruned KV attention](https://x.com/ManuelFaysse/status/2055214689613664303), where the model learns which keys/values to keep in persistent cache to reduce **KV cache size** and improve decoding speed. On the local inference side, [@danielhanchen reported](https://x.com/danielhanchen/status/2055274688025378854) that **Qwen small-model MTP GGUFs now run 1.8x faster** , up from **1.4x** two days prior, thanks to new llama.cpp speculative-decoding parameters.




**Open Models, Serving Stacks, and the Agent Toolchain**

  * **Open/local agent stacks are tightening around Hermes, Ollama, and portable runtimes** : [ClawRouter integrating Hermes Agent](https://x.com/ClawRou/status/2055078292567597253), [Teknium's claims of surpassing OpenClaw in token volume](https://x.com/Teknium/status/2055125356554899865), and [Grok support in Hermes Agent via SuperGrok subscriptions](https://x.com/Teknium/status/2055373314399650230) all point to continued consolidation around interoperable agent shells. NVIDIA published a practical deployment path to [run Hermes Agent locally on DGX Spark via Ollama](https://x.com/NVIDIA_AI_PC/status/2055317325444710872). [@onusoz](https://x.com/onusoz/status/2055120477648261502) also highlighted a major usability gap: **one-click local model deployment for end users still doesn 't really exist**, despite increasing demand.

  * **Serving infrastructure around open multimodal and scientific models continues to mature** : [vLLM highlighted Baseten's production deployment of vLLM-Omni](https://x.com/vllm_project/status/2055136943550427242) for **multi-stage audio, streaming multimodal, and real-time TTS** workloads often dominated by closed APIs. They also shipped [day-0 support for Intern-S2-Preview](https://x.com/vllm_project/status/2055148034124894395), described as an **open-source scientific multimodal foundation model** with an early capability in **material crystal structure generation**. Additional tooling updates included Hugging Face's call for [agentic kernel development in the kernels project](https://x.com/RisingSayak/status/2055187769266434101), and [Capa](https://x.com/acoyfellow/status/2055235076820971872), which turns **OpenAPI specs into Cloudflare service bindings** with **5,852 generated methods** across platforms like Stripe, GitHub, Slack, Twilio, and Kubernetes.

  * **Document/search infra also saw concrete product work** : [Weaviate v1.37](https://x.com/weaviate_io/status/2055276211681579242) added **per-property accent folding** , **per-property stopword presets** , and a **/v1/tokenize** endpoint for debugging BM25 tokenization. Cohere pushed [Compass](https://x.com/cohere/status/2055343638360752351) as a stack for retrieval over difficult documents using visual parsing plus search embeddings. On the benchmarking side, [ParseBench leaders Infinity-Parser2-Pro (35B) and Flash (2B)](https://x.com/jerryjliu0/status/2055405690538070340) were credited with **5M+ synthetic parsing samples** and a **joint RL algorithm** across document/element/chart parsing tasks.




**Anthropic, OpenAI, xAI, and Competitive Dynamics**

  * **The strongest competitive signal was around developer-product pressure, not just benchmark pressure** : [@Yuchenj_UW framed Anthropic's recent moves as "running the Codex playbook" after getting xAI GPU capacity](https://x.com/Yuchenj_UW/status/2055349045556814029), and the most visible user-facing change was [Anthropic resetting everyone's 5-hour and weekly Claude rate limits](https://x.com/ClaudeDevs/status/2055347539923308703), amplified by [@kimmonismus](https://x.com/kimmonismus/status/2055364277234528399) as a likely response to competition and/or increased compute availability. Separate reports from [@kimmonismus](https://x.com/kimmonismus/status/2055222524774846576) cited FT numbers putting **Anthropic valuation at $900B** and **ARR at $45B** by end of May, up sharply from earlier checkpoints.

  * **On model perception, several tweets point to widening domain specialization and frontier gaps** : [Epoch AI's domain-specific ECI](https://x.com/EpochAIResearch/status/2055349241300898273) suggests Claude has a **software-engineering advantage** relative to its own general capability index, but **under-indexes in math**. At the same time, multiple posters were impressed by **Claude/Mythos-level** capability jumps: [@scaling01](https://x.com/scaling01/status/2055362921803211248) called Mythos "insane," while [@teortaxesTex](https://x.com/teortaxesTex/status/2055330529583489406) said Mythos appears meaningfully stronger than GPT-5.5 in at least some use. The speculative next step on the xAI side is larger scale still: [@scaling01 expects a new ](https://x.com/scaling01/status/2055320443129581647)**[1.5T xAI model](https://x.com/scaling01/status/2055320443129581647)**[ soon](https://x.com/scaling01/status/2055320443129581647).

  * **OpenAI expanded the "ChatGPT as personal agent" thesis into finance**: [ChatGPT announced](https://x.com/ChatGPTapp/status/2055317612687675545) a **personal finance experience** for **Pro users in the U.S.** , with secure financial-account connections, spending analysis, and grounded Q&A over user-authorized data. [@fidjissimo](https://x.com/fidjissimo/status/2055384863155610068) tied it to the same pattern as health-record integrations: more structured personal context flowing into the agent. [@kimmonismus](https://x.com/kimmonismus/status/2055320528198521041) argued this could compress parts of the fintech assistant layer, citing internal finance benchmarks where **GPT-5.5 Thinking scored 79/100** and **GPT-5.5 Pro 82.5/100** on complex personal-finance tasks.




**Top tweets (by engagement)**

  * **Codex/agent adoption** : [ChatGPT personal finance preview](https://x.com/ChatGPTapp/status/2055317612687675545) was the highest-engagement directly AI-relevant product launch in the set.

  * **Developer rate limits as product signal** : [Claude resetting 5-hour and weekly rate limits](https://x.com/ClaudeDevs/status/2055347539923308703) drew major attention, likely because it directly affects developer throughput.

  * **Practical prompt-injection example** : [@tmuxvim's LinkedIn bio prompt-injection joke](https://x.com/tmuxvim/status/2055275374905307216) went massively viral and resonated because it maps cleanly onto current concerns about agent ingestion of untrusted text.

  * **Reliability backlash to AI-maximalist engineering culture** : [@mitchellh's "AI psychosis" thread](https://x.com/mitchellh/status/2055380239711457578) was one of the most substantive high-engagement posts, articulating a systems-engineering critique of "ship bugs, agents will fix them" thinking.

  * **Open-vs-closed/policy framing** : [Dan Jeffries' long thread against anti-open-source AI policy](https://x.com/Dan_Jeffries1/status/2055241272038691133) had unusually high engagement for a policy argument and reflects how export controls, open weights, and industrial policy remain deeply entangled with engineering discourse.




* * *

# **AI Reddit Recap**

## **/r/LocalLlama + /r/localLLM Recap**

[ Read more ](https://www.latent.space/p/ainews-cerebras-60b-ipo-slowly-then)

---

## [[AINews] Everything is Conductor](https://www.latent.space/p/ainews-everything-is-conductor)
*🔬 Latent Space | 2026-05-15*

_If you 're interested in how AI is improving Healthcare, tune in to our [first pod on it](https://www.latent.space/p/abridge) out today, and if you want to meet other top engineers in the field, [apply to speak](https://ai.engineer/cfp)!_

* * *

There's an ongoing joke in evolutionary biology that "Everything is Crab": [the Crab form factor](https://en.wikipedia.org/wiki/Carcinisation) has independently evolved at least 7 times on earth:

[](https://substackcdn.com/image/fetch/$s_!-UVS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc44b00aa-b057-4698-a9c6-f8e73c7aaaf7_2289x1342.jpeg)

The proximate cause of today's op-ed is GitHub [announcing the new GitHub App](https://x.com/github/status/2054959324485628120) \- as Oren Melamed says, "_If you are**code first** you might wanna stay on good ol' VS Code, but if you are **agent first** and GitHub first you are in for a treat!_"

[](https://substackcdn.com/image/fetch/$s_!8awu!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcc0e389d-df44-481c-998d-5524cf58e696_1194x1250.png)

Hmm. That looks familiar…

[](https://substackcdn.com/image/fetch/$s_!DOb8!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F98d6e93c-4e99-4ff0-8a20-74c75f3a54b8_2310x1298.png)

This is of course very nice for [Conductor](https://conductor.build/), which pioneered this form factor, and now has a loudly vocal fan in Garry Tan, the AI pilled CEO of Y Combinator:

Now for two billion dollar questions:

  * if you pioneered a form factor, how do you monetize it while others copy it?

  * what's next after this one?




For those interested in alternate histories, here's what happened with the Kanban board form factor that briefly trended last year:

And here is Maggie Appleton breaking down the design thinking [behind GitHub Ace](https://www.youtube.com/watch?v=ClWD8OEYgp8&t=372s):

> AI News for 5/13/2026-5/14/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

# **AI Twitter Recap**

**Coding Agent Tooling: Codex Mobile, GitHub 's New App, VS Code Multi-Agent UX, and Hermes/Codex Interop**

  * **OpenAI pushed Codex further into day-to-day workflows** : the biggest product launch in this set was **Codex in the ChatGPT mobile app** , letting users start tasks, review outputs, approve commands, and steer execution remotely while Codex continues running on a laptop, Mac mini, or devbox. OpenAI also noted **Remote SSH is now generally available** for managed remote environments, and later added **hooks** plus **programmatic access tokens** for Business/Enterprise automation around the Codex loop ([OpenAI](https://x.com/OpenAI/status/2055016850849993072), [OpenAI follow-up](https://x.com/OpenAI/status/2055016852133417389), [@OpenAIDevs on mobile workflow](https://x.com/OpenAIDevs/status/2055016926213181608), [@OpenAIDevs on Remote SSH](https://x.com/OpenAIDevs/status/2055016938217377945), [@OpenAIDevs on hooks/tokens](https://x.com/OpenAIDevs/status/2055032115964870838)). Separately, OpenAI published a technical writeup on the **Wi`ndows sandbox for Codex** , focused on the tradeoff between utility and constrained machine access for coding agents ([OpenAI Devs](https://x.com/OpenAIDevs/status/2054735161166819377), [@gdb](https://x.com/gdb/status/2054744721570820444)).

  * **The broader IDE/app ecosystem is converging on "agent-first" UX**: GitHub announced a technical preview of the **GitHub Copilot App** , described as a desktop environment for parallel workstreams, repo/PR lifecycle management, and model flexibility ([GitHub](https://x.com/github/status/2054959324485628120), [@adrianmg](https://x.com/adrianmg/status/2054961575929508067), [@OrenMe](https://x.com/OrenMe/status/2054959549413503308)). **VS Code** shipped a new **Agents window** for multi-agent, multi-project workflows, browser/mobile support via **vscode.dev/agents** , BYOK improvements, and token-efficiency features like compressed terminal output ([VS Code](https://x.com/pierceboggan/status/2054775908586934440), [remote/browser support](https://x.com/pierceboggan/status/2054778014135902715), [BYOK updates](https://x.com/pierceboggan/status/2054778582216622579), [terminal compression](https://x.com/pierceboggan/status/2054779764523815264)). On the open side, **Nous/Hermes Agent** added **Codex runtime integration** , effectively routing OpenAI-backed turns through Codex CLI/app-server and reusing ChatGPT subscription-backed execution in Hermes sessions ([Nous Research](https://x.com/NousResearch/status/2054958564951912714), [@Teknium](https://x.com/Teknium/status/2054958835547443553), [@HermesAgentTips](https://x.com/HermesAgentTips/status/2054963533800992962)). Kimi also shipped **Kimi Web Bridge** , a browser extension exposing human-like web interaction to Kimi Code CLI, Claude Code, Cursor, Codex, Hermes, and others ([Moonshot AI](https://x.com/Kimi_Moonshot/status/2054918374837322140)).




**Agent Infrastructure and Self-Improvement Loops: LangSmith Engine, SmithDB, Sandboxes, and Continual Learning**

  * **LangChain 's launch stack was the most substantive agent-infra release cluster**: **SmithDB** is a database purpose-built for **agent trace data** , while **LangSmith Engine** consumes traces, clusters failures, identifies likely code issues, and proposes fixes/evals--turning observability into an improvement loop rather than passive inspection ([@hwchase17](https://x.com/hwchase17/status/2054754206926700914), [@caspar_br on Engine](https://x.com/caspar_br/status/2054726851659248068), [@bentannyhill](https://x.com/bentannyhill/status/2054949581679653326)). Community commentary emphasized SmithDB's architectural shift toward object storage and a custom storage/query path for this workload shape ([@caspar_br on SmithDB](https://x.com/caspar_br/status/2054773536603144458), [@ngates_](https://x.com/ngates_/status/2054859033488580721), [Chinese summary](https://x.com/0xLogicrw/status/2054852978243404008)).

  * **LangChain also announced LangChain Labs** , an applied research effort around **continual learning** for agents, with the thesis that production traces should become training signal, evals, and targeted capability improvements over long horizons ([LangChain](https://x.com/LangChain/status/2054971487694749898), [@jakebroekhuizen](https://x.com/jakebroekhuizen/status/2054973621312073832), [@willccbb](https://x.com/willccbb/status/2054983266046996839), [Prime Intellect partnership](https://x.com/PrimeIntellect/status/2054986817779425579)).

  * **Execution isolation for agents continues to mature** : W&B/CoreWeave launched **CoreWeave Sandboxes** for isolated execution in RL, tool use, and eval workloads, explicitly testing destructive commands like `rm -rf /` at scale ([Weights & Biases](https://x.com/wandb/status/2054958004118724672)). In a similar spirit, open-source/local dev tooling surfaced around agent debugging: [@benhylak](https://x.com/benhylak/status/2054987683928383872) highlighted a free local agent debugging stack with traces exposed to Codex/Claude Code for automated eval authoring.




**Anthropic Claude Code Restrictions and the Developer Backlash**

  * **The sharpest ecosystem reaction was to Anthropic restricting/reshaping Claude Code usage** , especially for third-party wrappers and high-volume programmatic workflows. Theo's thread became the focal point: he argued users of T3 Code were effectively hit with dramatic rate-limit reductions despite integrating through the officially supported path, and he subsequently cancelled his subscription while encouraging others to post cancellation screenshots for open-source donations ([@theo initial thread](https://x.com/theo/status/2054731856248283318), [subscription cancellation](https://x.com/theo/status/2054732997287625013), [donation thread](https://x.com/theo/status/2054734057368621176), [T3 Code clarification](https://x.com/theo/status/2054737293186126056)). Other prominent builders echoed the complaint that Anthropic had effectively cut off open-source devs/apps and destabilized harnesses built around `claude -p` ([@theo](https://x.com/theo/status/2054728187498946969), [@andersonbcdefg](https://x.com/andersonbcdefg/status/2054721558141403242)).

  * **There was also a more strategic counterargument** : some users argued Anthropic does not owe developers heavily subsidized flat-fee tokens for third-party apps, and that the ecosystem will likely shift toward more explicit API economics and smarter routing between expensive and cheap models ([Sentdex](https://x.com/Sentdex/status/2054925517426491739), [@tadasayy](https://x.com/tadasayy/status/2054922713857462487)). Still, the visible churn signal was nontrivial, including users estimating meaningful ARR loss from reply-thread cancellations alone ([@thegenioo](https://x.com/thegenioo/status/2054919696663663009), [Uncle Bob Martin](https://x.com/unclebobmartin/status/2054970327592042661), [Theo later](https://x.com/theo/status/2055022768262144102)). For agent engineers, the practical takeaway is straightforward: **subscription-backed harnesses are not stable platform primitives** ; provider/model abstraction and BYOK paths look increasingly mandatory.




**Robotics and Embodied AI: Figure 's 24/7 Sorting Stream and the Broader Automation Signal**

  * **Figure 's livestream dominated robotics discussion**. The company first showed **8 hours of fully autonomous, unsupervised work** , then extended to a **24/7 livestream** , eventually reporting **24+ hours of continuous autonomous operation without failure** , around **human-parity throughput** on small package sorting, and operation by **Helix-02 running entirely onboard** with automatic resets for OOD cases--explicitly claiming **no teleoperation** ([Figure CEO Brett Adcock](https://x.com/adcock_brett/status/2054729581391962353), [24h update](https://x.com/adcock_brett/status/2054946098431881720), [detailed technical clarifications](https://x.com/adcock_brett/status/2054973511572271172), [Day 2 livestream](https://x.com/adcock_brett/status/2054970993442169230)). The repeated "Bob, Frank, and Gary" updates were fluffier, but the core signal was sustained autonomous operation at production-like uptime.

  * **Interpretation split between skepticism about Figure specifically and broader conviction about robotics acceleration**. Some commenters argued that critics were underestimating what these demonstrations imply for near-term labor substitution, while others noted skepticism was directed more at **Figure** than at **robotics as a category** ([@cloneofsimo](https://x.com/cloneofsimo/status/2054712329431109708), [@iScienceLuvr](https://x.com/iScienceLuvr/status/2054715505982743009), [@kimmonismus](https://x.com/kimmonismus/status/2054947354625630462)). Either way, this was one of the clearest "continuous uptime" demos in the batch.




**Research, Benchmarks, and Open Models: Diffusion LMs, Time-Series FMs, Mechanistic Interpretability, and RL/Search**

  * **A few technically significant model/research releases stood out** :

    * **Zyphra 's ZAYA1-8B-Diffusion-Preview** claims a **4.6 -7.7x decoding speedup** versus autoregressive generation with limited quality loss, making the usual case that diffusion LMs enable cheaper rollouts and richer generation modes ([Zyphra](https://x.com/ZyphraAI/status/2055038845809480113)).

    * **Datadog 's Toto 2.0** released **5 open-weights time-series forecasting models** from **4M to 2.5B params** under **Apache 2.0** , claiming #1 on **BOOM, GIFT-Eval, and TIME** and, more importantly, evidence that scaling laws may finally hold cleanly for TSFMs ([Datadog](https://x.com/datadoghq/status/2054929795385893108), [@atalwalkar](https://x.com/atalwalkar/status/2054941930497142826), [@ClementDelangue](https://x.com/ClementDelangue/status/2054991352295731619)).

    * **Goodfire 's interpretability post** argued that Llama uses a geometric "shape-rotating calculator" / Fourier-feature-like mechanism for arithmetic, with steering-based evidence rather than pure post-hoc description ([GoodfireAI](https://x.com/GoodfireAI/status/2054962242022777189), [follow-up](https://x.com/GoodfireAI/status/2054962356162363599)).

  * **On RL/search and optimizer-style progress** , several threads were notable: a survey framing LLM RL as **rollout engineering** across **Generate / Filter / Control / Replay** rather than just PPO-vs-GRPO ([The Turing Post](https://x.com/TheTuringPost/status/2054713822343266365)); **Pedagogical RL** using privileged information to actively find useful rollouts ([Souradip Chakraborty](https://x.com/SOURADIPCHAKR18/status/2055057138070733176), [@lateinteraction](https://x.com/lateinteraction/status/2055065846389649436)); and **Prime Intellect 's autonomous optimizer search** on the nanoGPT speedrun benchmark, where **Opus 4.7 reached 2930 steps** and **GPT-5.5 2950** , beating the **2990 human baseline** after ~10k runs / ~14k H200 hours ([Prime Intellect](https://x.com/PrimeIntellect/status/2055056380881744365), [@eliebakouch](https://x.com/eliebakouch/status/2055059154738278851)). Also noteworthy: **Kimi K2.6** was reported as **#1 open-weight model on Finance Agent Benchmark V2** ([Moonshot AI](https://x.com/Kimi_Moonshot/status/2054803169994272819)), and **Ring-2.6-1T** got day-0 vLLM support as an open release ([vLLM](https://x.com/vllm_project/status/2054968127298150506)).




**Top Tweets (by engagement)**

  * **OpenAI 's Codex mobile launch** was the clearest product winner by engagement and practical relevance: remote control/review of running coding-agent sessions from ChatGPT mobile ([OpenAI](https://x.com/OpenAI/status/2055016850849993072)).

  * **Theo 's Claude Code backlash threads** captured the strongest developer sentiment shift around platform risk and subscription-backed agent workflows ([@theo](https://x.com/theo/status/2054731856248283318), [@theo donations thread](https://x.com/theo/status/2054734057368621176)).

  * **Figure 's autonomous humanoid sorting livestream** remained one of the most discussed embodied-AI demos, especially once it crossed the 24-hour mark with detailed claims about onboard policy execution and no teleop ([Brett Adcock](https://x.com/adcock_brett/status/2054973511572271172)).

  * **GitHub 's Copilot App** and **LangChain 's Engine/SmithDB/Labs** were the most important non-OpenAI tooling launches for agent engineers this cycle ([GitHub](https://x.com/github/status/2054959324485628120), [LangChain](https://x.com/LangChain/status/2054971487694749898), [@hwchase17](https://x.com/hwchase17/status/2054754206926700914)).

  * **Prime Intellect 's autonomous optimizer-search result** is worth watching as a concrete example of coding agents being looped into open-ended ML optimization, not just app dev ([Prime Intellect](https://x.com/PrimeIntellect/status/2055056380881744365)).




* * *

# **AI Reddit Recap**

## **/r/LocalLlama + /r/localLLM Recap**

### **1\. Qwen 3.6 Local Inference Speedups and Quantization**

  * **[Multi-Token Prediction (MTP) for Qwen on LLaMA.cpp + TurboQuant](https://www.reddit.com/r/LocalLLaMA/comments/1tckzy2/multitoken_prediction_mtp_for_qwen_on_llamacpp/)** (Activity: 514): **A patched llama.cpp fork adds Multi-Token Prediction (MTP) support for Qwen plus TurboQuant, reporting**`21 tok/s`** -> **`34 tok/s`**on a MacBook Pro M5 Max 64GB, with a claimed**`90%`**MTP acceptance rate; note the raw speedup is ~**`62%`**, not**`40%`**. Code is published at**`AtomicBot-ai/atomic-llama-cpp-turboquant`**, with GGUF MTP quantizations for Qwen 3.6 27B/35B in the**`AtomicChat/qwen-36-udt-mtp`**HF collection.** Commenters questioned the TurboQuant framing, arguing it is often slower than `f16`, `q8`, or `q4`; one noted a TurboQuant PR to llama.cpp was rejected because existing Q4 KV-quant rotation support already covered most benefits, with gains mainly at Q3 where quality degradation becomes a concern. Others asked for quality/eval data, since higher speculative/MTP acceptance and tokens/s do not alone establish output parity.

    * Several commenters argued that **TurboQuant is not generally faster in llama.cpp** , with one noting it can be slower than `f16`, `q8`, or `q4`. A prior TurboQuant PR to **llama.cpp** was reportedly rejected because llama.cpp already implements rotations for `Q4` KV-cache quantization, where standard `Q4` was faster and showed little gain; TurboQuant may only help around `Q3`, but with notable quality degradation.

    * Users distinguished between speed, quality, and context tradeoffs: **MTP without TurboQuant** was suggested for speed, while standard `Q4_1` or `Q4_0` quantization was recommended for longer context/quality retention. One commenter questioned whether TurboQuant had any Mac-specific advantage, implying the benefit is hardware- or workload-dependent rather than broadly useful.

    * A commenter recommended using **dflash** instead of built-in MTP, claiming it is `30-40%` faster. They also mentioned that a pull request for this already existed, suggesting the implementation work may duplicate prior llama.cpp integration efforts.




[ Read more ](https://www.latent.space/p/ainews-everything-is-conductor)

---

## [AI-Native Healthcare: 100M Doctor Visits, 10–20 Hours Saved, Prior Auth in Minutes — Janie Lee & Chai Asawa, Abridge](https://www.latent.space/p/abridge)
*🔬 Latent Space | 2026-05-14*

_Special discounts up for[AIE Melbourne](http://ai.engineer/melbourne) ([LS discount](http://ai.engineer/mb)) and [AIE World's Fair](http://ai.engineer/wf) (group discounts up to 25% - [CFPs still open for Autoresearch and Vertical AI](https://www.latent.space/p/ainews-ai-engineer-worlds-fair-autoresearch)) Cya there!_

* * *

Abridge **did not** start as an "GPT wrapper". It was founded in 2018, years before the Cambrian explosion of AI application layer companies. OpenAI launched ChatGPT publicly on November 30, 2022 and by then, **[Abridge](https://www.abridge.com/about)** had already spent years doing the unglamorous work of building trust for one of the highest context, most important workflows in healthcare: **the conversation between a patient and a clinician.**

[](https://substackcdn.com/image/fetch/$s_!MX36!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F967bcd77-27ed-4487-bcc1-28c3d66d057c_2018x1576.png)

Abridge's original wedge was **clinical documentation**. Listen to the visit, generate the note, reduce the clerical burden, and let clinicians spend more time with patients instead of the EHR. By focusing on how doctors actually document, how health systems actually buy, how EHR integration actually works, how clinicians verify outputs, and how missing context during a visit turns into downstream friction across billing, prior authorization, quality, and follow-up, **the adoption of LLMs became a force multiplier** on a workflow already optimized for sensitive context gathering.

The company has scaled fast: Abridge says it is projected to support **80M+ patient-clinician conversations** this year across **250** large and complex U.S. health systems, with support for **28+ languages** and **50+ specialties**. It raised **[$300M at a $5.3B valuation](https://www.abridge.com/blog/series-e)**[ in June 2025](https://www.abridge.com/blog/series-e), after a [$250M round earlier that year](https://www.abridge.com/blog/series-d).

[](https://substackcdn.com/image/fetch/$s_!EAxq!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F994c46e8-d0f0-44ad-96e0-6531a31268b0_1962x1718.png)

Today, **Janie Lee** and **Chaitanya "Chai" Asawa** of Abridge join us for [another crossover pod](https://www.latent.space/p/unsupervised-learning-2026) with **Redpoint 's** **Jacob** **Effron** (who is on the board of Abridge) to dive into how Abridge is building the clinical intelligence layer for healthcare starting with ambient documentation, then expanding into clinical decision support, prior authorization, payer/provider/pharma workflows, and eventually real-time agents that act before, during, and after the patient conversation. 

We go inside the product, data, infra, **evals** , workflow, privacy, and org design choices behind bringing AI into one of the highest-stakes enterprise environments from 100M+ medical conversations and specialty-specific evals to real-time alerts, EHR integration, de-identification, clinician-scientist teams, and why healthcare may solve some of the hardest AI problems first.

We discuss:

  * Why Abridge started with **clinical documentation, "pajama time," and saving clinicians 10-20 hours a week**

  * **The transition from ambient scribe to clinical intelligence layer:** save time, save money, and save lives

  * Why conversations between patients and clinicians may be **the most important workflow** in healthcare ([patient visit summary feature](https://www.abridge.com/blog/patient-visit-summaries--now-generated-in-real-time))

  * **Chai 's "healthcare-coded Glean" framing:** context is king, but healthcare raises the stakes on safety, evals, and rollout

  * **Why Abridge wants AI to feel like "air conditioning":** always in the background, but only interrupting when it truly matters

  * **The prior authorization example:** turning a denied MRI weeks later into real-time guidance while the patient is still in the room

  * Why payer policies, EHR data, medical literature, and hospital-specific guidelines make the problem hard, and also create **the moat**

  * **How Abridge thinks about ambient form factors:** mobile, desktop, in-room devices, nursing workflows, multimodality, and future AR

  * **The multi-sided healthcare customer:** CMIOs, CFOs, CIOs, clinicians, patients, payers, and pharma

  * **The hardest AI problem at Abridge:** high-quality, low-latency, low-cost real-time support in a high-stakes clinical setting

  * When Abridge uses **frontier models vs proprietary models** , and why its unique data from medical conversations matters

  * Why **" every agent is a coding agent underneath,"** and how the EHR can be thought of as a filesystem for healthcare agents

  * How Abridge approaches personalization across individual doctors, specialties, and health systems

  * Why **" AI slop" is AI without context**, and how edits, memories, and clinician preferences create a data flywheel

  * **Abridge 's eval stack:** LFDs, LLM judges, in-house clinicians, third-party evaluators, specialty-specific evals, and progressive rollout

  * HIPAA, PHI, de-identification, one-way anonymization, customer contracts, and learning from healthcare data safely

  * **What changes when you operate at 100M+ conversations:** reliability, cost, post-training, model routing, and infrastructure optimization

  * Why the same clinical conversation can serve doctors, patients, payers, pharma, and future clinical-trial workflows

  * How Abridge works with **EHRs** , and why deep interoperability is table stakes for clinician adoption

  * Why healthcare AI has **regulatory tailwinds, why 80/20 does not work here** , and why high-stakes domains may drive AI forward

  * Why Abridge embeds **" clinician scientists"** into product and eval teams

  * What Chai learned from **Glean** about search, quality, and durable AI infrastructure

  * Why the future of AI infra may look like **context layers** , event-driven systems, Kafka, Temporal, sockets, CRDTs, and tools built for humans

  * Why Janie changed her mind on "**PRDs are dead, "** and why crisp written clarity matters more in complex AI products

  * How Abridge uses **Claude Code, Cursor, and coding agents** internally




* * *

**Abridge:**

  * **Website:** &lt;https://www.abridge.com/>

  * **X:** &lt;https://x.com/AbridgeHQ>




**Janie Lee:**

  * **LinkedIn:** &lt;https://www.linkedin.com/in/janiejlee>




**Chaitanya "Chai" Asawa:**

  * **LinkedIn:** &lt;https://www.linkedin.com/in/casawa>




* * *

## Timestamps

00:00:00 Introduction and what Abridge does

00:02:05 From ambient documentation to clinical intelligence

00:04:04 Clinical decision support and context as king

00:06:57 Alert fatigue, proactive intelligence, and prior authorization

00:12:36 Ambient AI form factors and healthcare customers

00:16:59 The hardest AI problems in healthcare

00:18:26 Frontier models, proprietary data, and model strategy

00:21:07 The EHR as a filesystem for agents

00:24:03 Personalization, memory, and clinician preferences

00:30:40 Evals, LLM judges, and progressive rollout

00:36:47 HIPAA, de-identification, and privacy

00:39:21 100M conversations and operating at scale

00:44:10 EHR integration and the clinical intelligence layer

00:46:39 Healthcare regulation, latency, and high-stakes AI

00:50:11 Clinician scientists and long-tail quality

00:53:04 Lessons from Glean and durable AI infrastructure

00:57:03 The future of agentic healthcare workflows

00:57:34 PRDs, product clarity, and building serious AI products

01:03:11 AI coding tools at Abridge

01:04:06 Outro

* * *

# Transcript

## Introduction: Abridge, Clinical Intelligence, and the Latent Space x Unsupervised Learning Crossover

**Swyx [00:00:00]:** Okay. This is a special crossover Latent Space Unsupervised Learning pod.

**Jacob [00:00:07]:** Very excited to do this.

**Jacob [00:00:08]:** At this point, we get together once a year.

**Swyx [00:00:10]:** Once a year

**Jacob [00:00:11]:** And this is a fun occasion to get to do it on.

**Swyx [00:00:13]:** I really wanted to talk to Abridge but I felt very underqualified because healthcare is not something we cover very intensely. It just so happens that Redpoint's our big investors and supporters of Abridge.

**Jacob [00:00:27]:** Anytime you want to have a portfolio company on your podcast

**Jacob [00:00:29]:** Please, by all means.

**Swyx [00:00:31]:** So we'll introduce our guests. Chai and Janie, welcome to the pod.

**Janie [00:00:34]:** Thanks for having us.

**Chai [00:00:35]:** Thank you.

**Janie [00:00:35]:** We're excited to be here.

**Chai [00:00:36]:** Thank you.

**Swyx [00:00:36]:** So for listeners, what do you guys do, just to situate you guys in the company?

**Janie [00:00:42]:** Abridge is a clinical intelligence layer for health systems. We really started with documentation and building for clinicians and as we think about reducing the burden that clinicians have, they're spending 10 to 20 hours a week on documentation. There's a massive doctor shortage in the country. We also think that conversations between patients and clinicians are probably the most important workflow in healthcare. It's where care is given and received but if you think about the 20% of our GDP that goes towards healthcare, almost everything is a derivative of that conversation, whether it's the claim, the payment, the actual diagnosis given, the treatment. And we've started with a conversation to reduce the burden for doctors on documentation but we're really excited about the path ahead as we become this broader clinical intelligence layer.

**Chai [00:01:34]:** I'm Chai. I work on clinical decision support at Abridge.

**Swyx [00:01:37]:** Yes.

**Chai [00:01:37]:** And so as Janie said, we're uniquely situated where we started off with the clinical note. What I'm really excited about and where we're expanding towards is what are all the things you can do before the conversation, during the conversation and after the conversation if you did have access to all the context about patients, payer guidelines, medical literature and put that together and to serve, how healthcare could look fundamentally different.

**Swyx [00:02:01]:** And that's the context engine that you guys have?

**Chai [00:02:04]:** Yes.

**Swyx [00:02:04]:** Is that what it's called? Okay.

**Swyx [00:02:05]:** So historically, as I understand it, the company started in 2018. A lot of people would be familiar with the AI voice notes form factor that doctors would be "Well, do you consent to being recorded?" It replaces handwriting and what have you. But it sounds like more recently there's been a big transition in the company. Tell me about the broader transition.

## From Documentation to Clinical Intelligence: Save Time, Save Money, Save Lives

**Janie [00:02:26]:** So from a transition perspective, we really think about our journey as The first act was: how do we help save time? And that's where a lot of that original product was.

**Swyx [00:02:37]:** By the way, one of those interesting stats

**Swyx [00:02:39]:** On your landing page was, doctors spend time after hours.

**Janie [00:02:43]:** They call it pajama time.

**Swyx [00:02:44]:** Why is that pajama time?

**Janie [00:02:46]:** Doctors after work in their pajamas

**Swyx [00:02:48]:** In their pajamas. Oh

**Janie [00:02:49]:** At home are just writing and catching up on their notes every day.

**Janie [00:02:53]:** Some of our favorite customer love stories, we have a Slack channel called Love Stories. We have clinicians telling us, "Abridge has helped us, from retiring early or we're now finally able to

**Janie [00:03:06]:** go home and eat dinner with our kids for the first time."

**Chai [00:03:08]:** Save the marriage in some cases.

**Swyx [00:03:10]:** One of the quotes was "We're not divorcing anymore."

**Swyx [00:03:12]:** I'm asking, "Why?"

**Swyx [00:03:14]:** Because they're working too much.

**Janie [00:03:16]:** But, in terms of where we're going and where we're expanding, we really think about our second and third acts around how do we help health systems save and make more money. Health systems are operating with record-low operating margins. It's getting harder and harder to serve patients and they have regulatory, some tailwinds but also a lot of headwinds coming their way and AI is ripe for helping on the saving and make-more-money piece. And then ultimately, how do we help save lives? The fact that our software and our product is open millions of times a week before, during and after a patient walks in the room, gives us massive opportunity with products like clinical decision support, which Chai is building but so many others to improve patient outcomes and probably one of the most important workflows and problems to be going after right now.

## From Glean to Healthcare: Context Is King

**Jacob [00:04:04]:** One thing that's interesting, Chai, is you came over to Abridge from Glean and clinical decision support, which for our listeners is, in the context of a visit, helping a doctor figure out the right type of care. It's really a search problem in many ways, going through lots of different data sources. Very analogous to your previous role as one of the earliest engineers over at Glean. I'm sure a lot of our listeners are curious what's similar about the problems that you're going after now and what feels different, now that you're in healthcare.

**Chai [00:04:33]:** Very similar. Taking a step back, with every wave, there's a lot of very similar patterns that happen across different products. A lot of social networking products look the same. A lot of credit-based products look the same. And we're seeing that very similar in the agent era with many companies, of course, in Redpoint's portfolio and so forth. And the key insight between both companies is that you have amazing models but context is king. Context is what puts them to work. So I see it in a lot of ways, a lot of similarities in this is a healthcare-coded version of Glean but the differences are really interesting. A couple things that come to mind. First and foremost, the rigor of the setting we're in. The downside risk is extremely high here in healthcare. It can be fatal in some cases. You prescribe something that the patient is allergic to for example. Whereas at Glean, it's "Oh, you got the question wrong." It wasn't the end of the world in most cases. And so what does that mean? That shapes our evaluation strategy, both offline evaluation, progressive rollout and there's a lot more we could go into there. Second thing that comes to mind is, vertical versus horizontal. In both cases, there's a large variance but when Glean is, it's a much more horizontal company, there's a variance of personas, companies that you're working with. We also have a variance of personas, different types of specialties, different hospital systems. But the variance is a little more narrow. So from a product perspective, you're able to focus far more, especially when you have a maturing technology and you're building new products that never existed before. It lets you go after them much more easily and especially in healthcare where so many problems were solved with labor and process, that it's extremely ripe for AI to keep helping augment and enable. And the final thing that's really interesting, Abridge specifically compared to many other companies in the AI area, is the modality we started with where we're ambient and we're always listening in the background. And many more AI products will go that way but it's how we started. And that's the greatest form of AI we can create, AI that's seamless. You're not looking at your screen. It's always there. It's always helping you out and being proactive. The Jarvis vision that, every hackathon I went to over the past decade, there was always a Jarvis competitor. But Abridge very much started from the opportunity and continues to go that way.

## Ambient AI and Alert Fatigue: When Should the Product Interrupt?

**Jacob [00:06:57]:** One thing that is super interesting then from a product perspective is you have this always-on seamless in the background and then you have to decide when you break the wall almost and say, "Hey, clinician, you might not have thought about X," or whatever it is that you want to do. And in healthcare traditionally there's been this idea of alert fatigue and a million pop-ups and then a doctor just ignores all of them. It's probably a pattern that a lot of builders are thinking through now. How do you think about the right way to intervene or to pop up in a doctor visit?

**Janie [00:07:26]:** It's such a good question. Alerts are notorious in healthcare specifically. Over 90% of alerts are ignored. The first and most important thing is context is everything, as Chai alluded to and I also think about how do we go from being reactive alerting to really proactive intelligence at the point at which it matters most. One thing we like to say is we want our product to feel like air conditioning. It should be in the background just making things better and if there is something that has great clinical risk and we're acutely aware that intervening now and not later is incredibly important, we should decide to act. But if you think about proactive versus reactive, instead of alerting a clinician during a visit when they're with their patient having a pretty serious and sensitive conversation, how do we prep a clinician before they walk into the room with that patient? And so historically, clinicians might have to manually go through charts with a patient that they've had over the course of months or years and they'll try to suss out what are the things they should be doing. You can imagine a world with Abridge. We'll summarize all of the most recent context for you, tell you based on the reason for a visit the patient is coming in for the types of things you should be discussing. And so you're going into that conversation prepped rather than walking in cold to that patient visit and then having this product interrupt you five or 10 times throughout the visit. And there might be times where it's really important to interrupt. We have a product called Prior Authorization and so this is when you may go into a doctor's office with knee pain. They'll prescribe you an MRI and so many of us have had this experience before, where in four weeks you'll get a call saying, "Hey, Sean, that MRI that you were prescribed wasn't approved and why don't you come back in? We'll figure it out." In a world with Abridge, we might choose to quietly but still alert a doctor in that visit. And alert is probably not even the word we would want to use. Before a patient leaves, we would want to tell the doctor, "Hey, Doctor, before Sean leaves, you should ask him, has he had physical therapy and has his pain lasted for more than six weeks? Because the Aetna plan that he's on in California requires six things. We've already confirmed four of them have been met 'cause we have all the context. But these two last criteria, if you can address with Sean before he leaves the room, we could guarantee that your MRI is approved before you leave." And so when you think about clinical usefulness, impact to the patient, there are instances in which if we can catch a doctor while the patient is still in the room, as we think about save time, save money, save lives, we get to check all of those boxes. But when doctors have 15 minutes between visits, we have to be really thoughtful about when it matters.

## Prior Authorization: Reducing Latency in Care

**Chai [00:10:23]:** There's this interesting product opportunity AI has is reducing latency in the world. For example, prior authorization is an example of where care gets delayed and so great AI can reduce that. And the problem with alerts before partially is a technical problem: the quality of your alerts really matters. They're going to get ignored if you get alerts that... Similarly in engineering, where they're noisy alerts that you can't act on. But if you can make really high-quality alerts with both the context, as Janie said, and really high-quality models, then you can create a whole other game.

**Janie [00:10:53]:** And I really like that experience because it starts to tease apart, what makes this so hard and unique. One, to make that prior authorization example possible, think about all the data that you need to have. You need to integrate with the electronic health record to know all of the patient context. Do we have access to your previous labs, previous imaging? And then to match you and to know that you're on Aetna, we have to collect all of the different payer policies and they vary by state. Some of these payer policies live on websites. Some of them live in unstructured 50-page PDF files.

**Jacob [00:11:31]:** I thought this episode was

**Jacob [00:11:31]:** To make sure we didn't scare people from healthcare.

**Janie [00:11:34]:** But when you think about the things that make it hard, it also gives you the moat.

**Janie [00:11:39]:** And then the second is the AI and the model quality we need to be able to hang our hat on. And so the bar, similarly when I worked at Opendoor, I worked on pricing models. Every outlier wiped out the margins of 30 and so similarly here in healthcare, the bar for accuracy is so high. And then I'd say the last is workflow is everything. If insurance companies deploy AI, it typically happens too late and this is when you have the notorious comical examples of AI just fighting each other when it's too late. But if we can pull forward the use of both the AI but also the ability to solve problems when the patient's in the room, you can start to collapse what typically takes weeks or months after your visit, ideally down to minutes or real-time. And it's where healthcare is both very difficult but also extremely rewarding if you can crack it.

## Product Form Factors: Mobile, Desktop, In-Room Devices, and AR

**Swyx [00:12:36]:** Just to get some baseline on the form factors, because I've seen some videos on your website and stuff. You guys talk a lot about ambient AI. Is it primarily on the phone? Is there any other form factor that people get Abridge in? Is there an Abridge room setup where it's always on? I don't know.

**Jacob [00:12:55]:** An Abridge podcast studio.

**Janie [00:12:58]:** Primary form factor is mobile and desktop. Usually

**Janie [00:13:00]:** Clinicians are walking in and out of rooms with mobile but at the end of the day, when they're closing out their notes or wanting to prep for the day ahead, they might use desktop. We have been having a lot of really interesting partnership conversations with a lot of these in-room device companies as you think about the power of multimodality and even more data, as you think about all of what is not captured today. It is fascinating to think about, especially even as we go into building and scaling our nursing product. It's one where nurses constantly, as they're walking in to check in on a patient for two minutes or maybe even 30 seconds,

**Janie [00:13:43]:** Starting an Abridge experience is probably going to take longer than the visit. And so what can we do with in-room devices that are always on starts to raise really interesting and fun product questions.

**Swyx [00:13:54]:** I was thinking, the way in tech companies we have all these Google Meet

**Swyx [00:13:58]:** And other things, we might as well set up entire rooms with just Abridge tech.

**Chai [00:14:02]:** Very much. AR glasses and related form factors are also relevant: how do we bring the information to the clinician in real-time without a screen, while still letting them focus on the patient?

**Swyx [00:14:18]:** Do you think they want that? I'm skeptical of AR, but I'm curious what you've tried.

**Chai [00:14:26]:** Admittedly, it's not a near-term product roadmap

**Chai [00:14:29]:** By any means. I'm being far-fetched.

**Jacob [00:14:31]:** There's some sick AR stuff for surgeries.

**Swyx [00:14:33]:** Really?

**Jacob [00:14:33]:** When people are trying to visualize, you're about to make an incision but you want to see, what the cut might look or what the body might look like inside and they can layer in imaging.

**Swyx [00:14:43]:** That's cool.

**Chai [00:14:45]:** At some point in the future.

**Janie [00:14:46]:** But there are a lot of our largest customers and at the largest health systems integrating already and so even as we think about building into it, unlocks a lot of product capabilities.

**Swyx [00:14:57]:** And just to establish the terminology. Sorry, and I know I'm asking basic questions somewhat for myself but also for the audience who might be

## Health Systems, Buyers, Clinicians, Patients, and Payers

**Swyx [00:15:05]:** Less integrated. When you say health systems, it's like the Johns Hopkins, the Kaiser Permanentes.

**Janie [00:15:09]:** Mayos, the Kaisers of the world.

**Swyx [00:15:10]:** These are your customers, right? And the outcome that you deliver for them is happier doctors, reduced cost of processing, reduced mistakes. It's weird in a sense that I feel like there's also, a secondary customer, the customer of the customer and I don't know if you -- do you think about it that way?

**Janie [00:15:28]:** The other interesting and complex part of building product is we have our buyers, who are the chief medical information officers

**Janie [00:15:39]:** The chief financial officers, the CIOs of these large health systems. Our users today are clinicians but if you think about who downstream is impacted, it's patients. And so as we build, with every product in mind, we think about who we're building for, who the secondary user is and what does that mean either in terms of experience, security compliance, ROI that we have to make tangible. And so like you said, time savings is one of them. But for CFOs, they care a lot more than just time savings. We have to show for every dollar you put into Abridge, because you have more compliant documentation or because you have fewer queries coming from your billing team, we save or add real dollars to your bottom line or top line, are things that we're constantly thinking about because of the dynamic across all three sets of users.

**Chai [00:16:32]:** There's a whole other axis too with the payers and pharma

**Chai [00:16:35]:** as well. Connecting all these three big stakeholders in healthcare is

**Swyx [00:16:39]:** Do the payers ever see your data? Sorry, the payers meaning the insurers, right?

**Chai [00:16:44]:** Yes.

**Swyx [00:16:44]:** They also see Abridge data?

**Chai [00:16:47]:** No

**Swyx [00:16:47]:** Like the direct integration to you guys

**Chai [00:16:48]:** They wouldn't see the raw Abridge data but when you're working together on something like prior authorization, whatever information they need, we'd communicate to them.

**Jacob [00:16:59]:** That's cool. I would love to dig into the AI side. You still have a lot of problems on the AI side. And so maybe to start at the highest level, what's one of the hardest problems you have to solve in AI at Abridge today?

## The Hardest AI Problems: Quality, Latency, and Cost

**Chai [00:17:11]:** To make things simple, let's take, building off the prior auth example. So one thing Janie talked about is okay, this data is all over the place and there's this combinatorial explosion of procedures, payer policies and even sometimes different health systems. There can be some cross-product of all of these different considerations you have to take into account. But what's really hard about this problem is doing it real-time in the conversation. So, in any AI product, usually the three KPIs you care about are quality, latency and cost. Now, what we're saying is we want you to do this real-time in the conversation, guiding the clinician. How do we do it in a way that does not break the bank? But we're using -- But we also need very intelligent models because you're working with this cross-product of data and this, all this context layer as well. So you need high intelligence and high-quality because you don't want the alert fatigue but you also need to be fast and cost-effective. And so that's where a lot of clever engineering goes. It's okay, without getting into all the details here, can you model these policies in some intermediate representation or other things that you can do that can make this problem tractable? And of course, the Pareto frontier is always changing but we are also trying to do this now.

## Model Strategy: Third-Party Models, Proprietary Data, and Medical Conversations

**Jacob [00:18:26]:** What implications has that had for what you take off-the-shelf and say, " what? We don't need to be world-class at X. We'll just take this from the model providers or from some infrastructure player," and what you're "No, this is where we spend most of our time focused on"?

**Chai [00:18:38]:** This is, the fun challenge in AI?

**Jacob [00:18:42]:** It changes every three months? So

**Chai [00:18:42]:** Of course, with the shifting landscape, we try to be extremely thoughtful on predicting the trends of where third-party models are going and where we can uniquely go. And, sometimes when you talk about AI models, we're the models are just going to get infinitely better. But I don't think... It may be in the grandness of time you could say that but, within every month, every quarter, there's specific ways they're getting better. They're training on a lot more, coding data to be better coding agents, for example. And so

**Chai [00:19:14]:** We have to think about where are the things that won't -- unique data that we're uniquely training on or to step back a little, where is a proprietary model bringing advantage to us is if it can give higher quality or lower cost and latency for similar quality, very similar to many other companies. And when we can do that is when we have proprietary data. So, for example, we have on the order of eighty million or hundreds of millions now getting close to of medical conversations.

**Jacob [00:19:44]:** It's insane.

**Chai [00:19:45]:** This is a unique data set. And this data set, it's very interesting because this data set is effectively a large part of the trace between the patient and the provider. That's where the quote-unquote debugging happens in healthcare. We have these traces at scale, as in as, our CEOs even called it, an exhaust that comes out of our product. And so when you have these traces, that's how you can train better agents on certain use cases, whether it's your transcription diarization use cases or so on or like note generation models and we can do that much cheaper and faster. But we're always also working with these third-party model providers. We closely collaborate with them and that's how we predict where the trends are going. The thing that I think about a lot is that, I know that the model providers are going to train much more on agentic workflows and so forth, so that's great, so that you have a better agentic harness. But the other thing that's interesting is that the model providers, because a large class of the consumer model providers is healthcare queries, that they might, optimize to train a lot of healthcare data to encode the knowledge in its weights. And this is just a great thing for us as well, where the off-the-shelf models can keep bett-getting better at general healthcare information, such that what our strategy is, we have a constellation of models, we can use something for this, that and, we only care about, at the end of the day, the best product experience.

## EHR as File System: Agentic Workflows and Real-Time Interfaces

**Jacob [00:21:07]:** And, you have, overall capabilities improving. I'm curious, as these models get better, is there something you look at and you're ", three months ago, we really couldn't do that but God, the the latest models really allow us to do it"?

**Chai [00:21:19]:** So here's something interesting that I've, been toying with. So all models are... This wasn't super obvious a year ago but now it's become clear and clear that almost every agent is a coding agent underneath the hood? So you give it whatever file system, it can write its own code and so forth. So when you think about within healthcare and the use case that we have, you can think of the EHR effectively like a file system. It's just -- it's a storage of all this information. It's a lot of information there that cannot fit into the context window, at least of today's models and you want to use that context effectively for all these product use cases we're talking about. And so if you have better agents that can, manipulate data, read that data, treat it as a file system as we see they're going and we know model companies are investing this way, then that very directly benefits us.

**Swyx [00:22:09]:** Yeah. Okay, cool. Again, just establishing basic things. But we're going back to the model stuff. I'm really interested in double-clicking more on the real-time, element, which is pretty important for both of you. Is it -- Is real-time just batches of every one minute, every five minutes? Is that how we do it? Or is there some more native, genuinely real-time in the sense that OpenAI has a real-time API or Gemini has a real-time API?

**Chai [00:22:35]:** Yeah. Yeah. So today it is more on the on the batch basis but there's interesting

**Chai [00:22:41]:** Prototypes that we have that we're still not fully, full time, voice in text out or in that sense. But, can you trigger your models, your agents or agentic workflows, depending on the right times in the conversation?

**Chai [00:22:58]:** And so you can imagine, different techniques to bring this latency down and, you want to bring the feedback loop down as much as you can. And so a lot of clever engineering there without fully... Maybe one day we'll do full voice in and text out, train a model to do something like that.

**Swyx [00:23:15]:** You do -- People don't want voice in voice out?

**Chai [00:23:18]:** Now we aren't creating experiences that are, during the conversation, inter -- It's almost like

**Swyx [00:23:25]:** Might be too disruptive

**Chai [00:23:26]:** Too disruptive until, who knows, maybe eventually you could have full voice agents once we -- the quality and we improve the comfort of the technology. But right now gra -- that change is much more gradual and it's more text focus, text out.

**Janie [00:23:42]:** And so much of currently what our product is trying to do is allow a clinician to focus on their patient and maybe at some point but right now patients, clinicians don't want a third voice, at least in a literal voice in that room. And so how do we be there with all the contacts and information ready at hand when there's the right moment?

## Personalization: Individual Doctors, Specialties, and Health Systems

**Jacob [00:24:03]:** Jenny, one thing I'm curious about is how you think about, personalization in the product. I imagine, every doctor is a special snowflake in their own way, has their own way they like to do things. There are probably a bunch of different approaches you could take to doing that, both within the model layer itself but then also just with clever prompting or engineering. How do you

**Jacob [00:24:20]:** Deliver on that?

**Janie [00:24:21]:** It's such a good question. Personalization is massive for us. We think about personalization at three levels. The first is at the individual, the second is at the specialty level and then the third is at the health system or the organization level. To your point, there are a lot of individual preferences. You-When a note is produced, it almost is a reflection that is so deeply personal of a doctor's work and how they give care. And so do they have preferences on things like style? They might want bullets versus paragraphs, really concise versus comprehensive. They also might have phrases that they really like to use or the templates that they want every note to be structured. And, we see it in our feedback all the time. We want two spaces in between sentences or I refuse to use this tool. And so that's something that we've had to build in. And the tricky part is how do you make sure that stylistic preferences don't interrupt accuracy and quality and that's something that we've really had to refine and hone over time. Second is at the specialty level. A cardiologist note or workflow is going to look very different from a dermatologist workflow.

**Jacob [00:25:32]:** I assume cardiology notes are the highest stakes for you guys, given your CEO is a cardiologist.

**Jacob [00:25:36]:** It's "Oh my God, make sure we get this one."

**Janie [00:25:37]:** Shiv, our CEO, is still a practicing cardiologist. He rounds once a month. And so, first call when we want just quick and easy user feedback too.

**Janie [00:25:46]:** But, specialties require a lot of personalization, both in terms of what does the product look and so we make sure that as new users onboard, we catch that and the product proportionally reflects that. But also on the back end, evals at the specialty level, they are hard-earned to calibrate and get. What does a really great dermatology note look like? What makes it complete? What makes it compliant and billable is very different than a primary care doctor. And so it's not just about what does the product experience look but on the back end tuning and really deepening our understanding for the specialists. What does great output look like? And that's, a problem that we need to calibrate internally, externally, online, offline but, takes lots of cycles but is necessary in a high-stakes environment. And then at the health system level, for products like clinical decision support, you have health systems who've spent years or decades refining their best practices and they want to know, "Hey, we love your clinical decision support product but how do we embed our own hospital guidelines into them to inform clinicians before, during or after a visit what brest -- best practices should look like?" And as you think about, deepening moats as well, when health systems, trust us with that data, allow us to productize it and directly into the clinical workflow, makes us a really great partner to health systems who want to build something that truly meets their needs, their practicing guidelines.

## AI Slop, Memory, and Product Data Flywheels

**Chai [00:27:23]:** And I want to add onto that. The for the clinical documentation problem, it's very similar to AI writing that doesn't feel like your own and then we call that slop. But the way I describe one framing of slop is like AI without context. But we have all that context and both the clinicians, can have it and can guide it. And so part of the other interesting exhaust for us is, memory is, one of these new systems records

**Chai [00:27:49]:** Almost.

**Janie [00:27:50]:** And we also have all the edits people make on our product and when you think about a data flywheel and how we get better over time becomes really powerful as a mechanism to just going deeper in personalization.

**Jacob [00:28:04]:** It's interesting. I love this idea of working with systems on the guidelines they built up over a long time. I feel like so many of the best AI app companies today are... The question is: How do you take the expertise that a law firm or a bank has built up over many years and then add that as context and also a special sauce over, a an AI tool? And so seems like y'all are really doing that very effectively.

**Janie [00:28:24]:** We're now starting to have our customers ask, "What are other customers doing?"

**Janie [00:28:28]:** "And how are they doing it?"

**Janie [00:28:30]:** And as we think about having visibility across such a large set of care being delivered right now, a really interesting place we could also partner.

**Swyx [00:28:40]:** I'm just curious. I -- This may be a nothing question but, how different are health system guidelines from each other? Don't they all converge to the same thing? And if not, where do they differ?

**Chai [00:28:52]:** At a really high level, they're going to talk about very similar things but the difference is probably in some more of the details. "Oh, you should refer to specialists only when XYZ conditions are met," or so forth and maybe different organizations have different practices and guidelines around that. But high level, talking about similar things but the details are what, of course, that shapes the context and the decisions you make.

**Swyx [00:29:15]:** And this all goes into the context engine and it might affect the notes but maybe not.

**Chai [00:29:21]:** The -- For these local pathways, we're definitely thinking about it a little more for our clinical decision support product.

**Chai [00:29:26]:** So yeah.

**Swyx [00:29:27]:** Which is your stuff, yeah.

**Swyx [00:29:28]:** And then the memory which you raised, let's just tell us more about that. What have you tried in memory? What's the structure of the memory? What works? What doesn't work?

**Chai [00:29:38]:** There's, of course, many different ways you could do memory, where it's okay, can you bake it into the model weights or can you do it in some external store? For us, what's interesting is, of course, when you think the models are rapidly changing, whether it's in-house or third-party, baking into the model weights, sometimes you worry that it could be a little throwaway. And so, how do you... You need to find a way that you decompose the problem, the preferences from the underlying models and so forth. The thing we're right now most both that's easiest to start with and we're excited about is having, a separate store for memory, where you have, for example, a memory sub-agent that's, working in the background, figuring out what are the important parts of the clinician's actions that we want to remember for the long term. And then you can also imagine, other things where in the -- you have background jobs that are running that are collating these, memories similar to Sleep, of course and what other pattern, patterns products do as well. Learning over all these action, all the action data we have, again, note edits, the conversations they did and the actual transcripts.

## Evals: LFD, LLM Judges, and Clinical Safety

**Jacob [00:30:40]:** What about evals? How in the world do you... It is such a complex product surface area. We would love to hear you riff on that and also how has that evolved? I'm sure you've gotten better at it, so any learnings along the way.

**Janie [00:30:50]:** From an evals perspective, we, from day one when we build any new product or feature, we think about, what does good look like? And there are table stakes things like clinical safety but then you start to get deeper into what does good quality look like. And when you go into something like our core product, there's stuff like style and completeness and there's things like does this note become something that can be billable, which is very high stakes for a health system. We have a number of ways in which we get confidence for this. We have, internal in-house clinicians who do what we call an LFD process to give us our very first pass at is this or isn't this a good enough output, look at the effing data.

**Jacob [00:31:41]:** LFD?

**Chai [00:31:42]:** That's why I was smiling. I was "Is Janie going to mention what it stands for?"

**Jacob [00:31:46]:** I was not... There's like a million acronyms.

**Jacob [00:31:48]:** How am I supposed to know that I don't? So "Oh yeah, of course, an LFD."

**Swyx [00:31:51]:** I've never heard of LFDs.

**Chai [00:31:53]:** It's a bridge for sure.

**Janie [00:31:55]:** I got through three days and then I had to ask someone.

**Janie [00:31:58]:** I thought it was just me that didn't know

**Janie [00:32:01]:** It's our internal process.

**Swyx [00:32:02]:** But look at the data as a meme in ML, 'cause you tend to not look at it. You just want to look at number go up.

**Chai [00:32:06]:** Exactly.

**Swyx [00:32:07]:** But yes.

**Janie [00:32:08]:** But so, we make sure we look at the data and then as we think about all of the components of good output, we, one, create LLM judges across all of these and we make sure with annotated data and either internal or external evaluators, we feel like these judges are calibrated. And then depending on the stakes, we also work with in-house and third-party evaluators across all of these before we ship any big change. And the goal is, in terms of evolution, how do you go from this process taking months, down to weeks, down to days? Some of it is, a true science and ML problem. A lot of it's also just, hard operational work. Have you planned ahead in terms of what you need? Have you really optimized the capacity that you need across all of the different specialties you need? Have you gotten a really good sense of which third parties are great to work with for what use cases? This takes a lot of domain, expertise and, lots of mistakes and errors in figuring that out. And so as much of it is an ML problem, so much of it has also been operational gains that are hugely important, where domain-specific expertise is everything.

## Specialty-Level Evaluation and Progressive Rollouts

**Jacob [00:33:23]:** But it's funny, 'cause I feel like people talk about healthcare like it's one giant market and the reality is

**Jacob [00:33:26]:** It's, dozens and dozens of sub-markets. And so it feels like in your evals you have to build that up across the board, probably.

**Swyx [00:33:34]:** And is specialization the primary cardinality at... That's the word that comes to mind.

**Janie [00:33:40]:** Sometimes, depending on the product or the use case. And so if we're making a note improvement or feature for a particular specialty, definitely but we have products that are for nurses. We have products that, are really aimed at making the document or the output a lot more billable. And so we'll want to work with coding teams and not necessary clinicians. And so like

**Jacob [00:34:05]:** Coding meaning healthcare coding.

**Janie [00:34:06]:** Yes. Yes.

**Jacob [00:34:07]:** Not

**Chai [00:34:07]:** Yes. I see you.

**Swyx [00:34:07]:** Other kinds.

**Janie [00:34:09]:** But is this output proportional to the work that was delivered? Is there sufficient documentation to justify the amount that a health system may end up charging? And so, specialty sometimes but also domain, very different across all of the different products that we're working for. And building out that network is, not easy and is where a lot of our operational investments have gone into.

**Chai [00:34:35]:** And I view a lot of analogies to self-driving cars here, where, part of it is we really want progressive rollout of features to test in the real world is this useful? Is this going to work? One big difference compared to past lives is before I'd build a product, maybe I'd alpha it and then I'd like GA it the next week, 'cause I'm "Go, move fast, ship," and whatnot. But the mentality is like you... I want to make contact with the reality as quick as possible but I want a progressive rollout. Because as much as I get as large of an offline eval set, I want the distribution of that to match real-life distribution. And over time, by rolling out early, similar to Waymo has a tagline, "The world's most experienced driver," another thing that can, at least linearly increase for us is, both the size of our evaluation offline and online, that and it all feeds back.

**Janie [00:35:25]:** Something that's been earned over time, speaking of evolution, is just the trust we've gotten with customers. Historically, a lot of these health systems, when they bring on new vendors, their release cycles are quarters, sometimes twice a year. We've gotten our customers onto monthly release cycles, which is pretty fast for health systems but what is more exciting over the last, call it, few quarters, has been, a subset of our customers have said, "We want to innovate with you. We trust you," and we have a pretty, decent chunk of our customers who say, "We'll develop with you outside of these monthly release cycles. We have a higher tolerance. We know that the stakes are very high but we want to be the first ones using these products, giving you feedback." And so for a pretty substantial set of our customers, we've been able to convince them to be able to ship, in this gradual way before GA. Something we talk about a lot internally is, trust is earned in drops, earned in buckets and so we still can't do what I used to do when I worked at Loom. We had 30 million users. I'd just be, rolling out experiments left and. The bar is still quite high for iterative rollout but because of the trust we've earned, we're able to learn at pretty high volume very quickly.

## Privacy, HIPAA, and De-Identification

**Swyx [00:36:45]:** Your scale is still pretty huge.

**Swyx [00:36:47]:** One thing I want to... We were going to go into scale? In a sec. One thing I wanted to call up, follow up on evals, which, again, just coming from a generalist engineer point of view, just thinking through what would people be scared of in doing this, the privacy and HIPAA

**Jacob [00:37:00]:** Elements of this. I have zero experience in that. What do you have to do? What is surprisingly not that bad?

**Chai [00:37:06]:** So one thing that's really important here from a compliance perspective is very much that any of the data we use needs to be de-identified, any real-world data we use as a basis of online eval sets we're learning from. And so you have to -- And there's, very clear, government guidelines, what counts as PHI. And so we've even have built models that can take, for example, a clinical transcript and remove all the key PHI indicators and so you have a scrubbed/de-identified version. And then once you... And so one thing that's important is first you've got to get confidence in that model in the first place? And prove that out. Because, now you have, multiple probabilistic systems on top of each other.

**Chai [00:37:46]:** But once you have that, then you can train on it use it for evaluation and so forth, provided one of the cool things also that you can do from a business side is the right data contracting as well with your partners.

**Jacob [00:37:57]:** Is the anonymization one way? Once it's done, you cannot undo it? Or is there someone

**Chai [00:38:01]:** Yes

**Jacob [00:38:02]:** Who holds the master key that can... Yeah, okay. So it's one way.

**Chai [00:38:05]:** It's one way. Yeah.

**Jacob [00:38:06]:** That's how it works. I just wanted to... Because, there's a lot of this, learning from feedback and everything that, you would want to debug more but you can't because you just physically don't allow yourself to.

**Janie [00:38:17]:** Some of it's also written in our customer contracts in terms of who can or can't access PHI data, how long do we retain it,

**Jacob [00:38:27]:** Very good

**Janie [00:38:27]:** Before it gets de-identified. And so we have a pretty high bar for who can access that PHI data, just to make sure that we always respect our customer data and privacy. But that's something that we partner with our customers on too, to make sure that as we want full, as close to precision as possible in that quality

**Janie [00:38:48]:** We can still use it.

**Jacob [00:38:50]:** But it'll be fascinating to see how that space evolves? Because you think about, I used to work at a company that, did a lot of healthcare data in the cancer space and if you asked, the average cancer patient, "Hey, do you want people, do you want other patients to be able to learn-"

**Chai [00:39:03]:** Take it.

**Jacob [00:39:03]:** "... Learn from your experience?"

**Chai [00:39:04]:** Take it all.

**Jacob [00:39:05]:** They're "Please."

**Jacob [00:39:06]:** "I'd love, nothing more than for other people to be able to learn from

**Jacob [00:39:10]:** The experience that I had." And so in the past it was a lot harder to do that learning. But with this technology, that might really be practical and so it'll be fascinating to see how that continues to evolve.

**Chai [00:39:21]:** There's so much in our data set of 100 million conversations.

**Chai [00:39:26]:** You can imagine things like insights that you can give to the clinician. How could you, oh, how could you have reacted to this? In coaching or insights around, which treatments are effective or, like... Because you have this, again, this data source that was never captured before but that's, where, intuition or experience is created from, going back to this idea that the conversation is the agent of truth.

## Operating at Scale: Reliability, Cost, and Token Efficiency

**Jacob [00:39:46]:** Back to the 100 million conversations, I feel like you have this insane scale that maybe only a few other AI app companies have and everyone else dreams of. So not everyone has had to confront this yet but maybe just talk about some of the challenges of operating at that scale and what, our listeners have to look forward to if they ever get to this level of scale.

**Chai [00:40:05]:** At large and larger in scale, so of course there's a general, infrastructure reliability. When you... In any given startup, you're building the plane while it's flying. So there's some notion of that. But what gets interesting on the AI and ML side for sure is this, as you get at more and more scale, so one, you have the data to first and foremost do this. But, you start thinking about costs or infrastructure in a whole different way at scale versus, a prototype.

**Chai [00:40:34]:** You can use the most expensive model, you can burn as many tokens as you want but when you're doing 100 million conversations

**Jacob [00:40:41]:** Token max on leaderboards are less upsetting than that context.

**Chai [00:40:45]:** . When you're doing that and so that comes for we have the data and we also have the team that's able to post-train based on this and you can optimize for efficiency, especially in areas where you believe that maybe a lot of the quality headroom is less so and you don't expect the other off-the-shelf models to go that way, such that you want to do, efficiency maximization, in terms of compute and tokens.

**Jacob [00:41:08]:** I feel like you guys live in the future in some way where most use cases today are really just in use case discovery mode, where it's "God, I really hope I can find something that can get to scale," and so you're always going to use the most powerful model. And then the few things that do get to this level of scale, you start to do those optimizations.

**Chai [00:41:22]:** It's a natural trajectory where it's like zero-to-one, we're not talking about any of these optimizations.

**Chai [00:41:26]:** But when maybe we're in the one-to-100 or so forth, then we're in optimization mode and, what works out really well is you've got all this data from zero-to-one that lets you do this.

## What Comes Next: The Conversation as the Shared Healthcare Platform

**Jacob [00:41:36]:** That's fascinating. I feel like one thing that's so interesting about the Abridge footprint is that you're in the doctor-patient visit in real-time. I always like to say, there's like probably 50 years' worth of product you could build on top of that. What gets each of you, I don't know, what are you most excited about building, either in the short term or medium term or even, long down the line?

**Janie [00:41:53]:** Something that I get really excited about is that the same conversation can serve so many stakeholders. If you think about the conversation, a doctor needs to know what is the documentation, how do I make sure that this fully represent the care I gave? A patient needs to know, "What the heck just happened? This was really overwhelming. What are my next steps?" A payer needs to know, was this the proper and appropriate care given? A pharma company might want to know why isn't this drug being properly used or is there a good candidate for this clinical trial that I'm about to run? And where I get excited is that our product and our platform and our infrastructure can be the same product across all of those things and start to what's today, separate, very expensive, complex systems that serve each one of these stakeholders in very different ways, start to collapse all of that into a singular platform that enables not just more efficiency across the board but also better outcomes for everyone. And, all of us experience healthcare in probably very painful ways and knowing that there is a world in which we can simplify a lot is really exciting to me and it all starts with the conversation.

**Chai [00:43:15]:** It's interesting. Of it very similar to going back to the KPIs that any AI product cares about. How do you increase quality of care? How do you reduce latency to care? And how do you reduce costs? Which is a huge, in healthcare

**Jacob [00:43:28]:** They call it the triple aim in healthcare.

**Chai [00:43:30]:** But very similar to building AI products and the thing that really excites me is when we talk about that latency piece, we talked about one example earlier of prior authorization, can you reduce the latency to care? But you can imagine so much more. Oh, as soon as the lab value gets updated, do you have like a background agent that, kicks off and uses all the context to be "Oh, hey, the patient should do this next," for example. And of flagging that to the clinician who's always in the loop but reducing that latency, to care. And then you can imagine this is much further down the road but it's like even connecting that to the direct patient and the consumer. And so how can you, how can you build a bridge to all of these things?

## EHR Partnerships and the Clinical Intelligence Layer

**Jacob [00:44:10]:** Very cool. The connections piece is just an ever-growing thing. And one of the key partners is the EHR and I wonder what that relationship is like. Will they, look at this as, something that is valuable enough that they want to own someday?

**Janie [00:44:29]:** Our partnerships with the EHR is, we know that we have to be extremely close partners with all the EHRs who we partner with. Being able to not only pull and push all of the data into the right places is, not only table stakes, if we can't do that, health systems don't want to use us. The second and the reality of today is clinicians spend a lot of their days in the EHR. So much of what allowed us to win in the largest health systems was pretty direct and, very close partnerships with some of the largest electronic health records that allowed us to pull and push data with APIs that weren't ready out of the box. And clinicians want to save clicks. Anytime we introduce a new product that, adds two clicks for them in their day, they're "We're not going to use it."

**Janie [00:45:21]:** They have 15-minute back-to-back appointments with their patients. They're spending, hours during pajama time doing documentation. Every second and every minute counts and so we really think about being deeply integrated into the EHR as also table stakes to getting real usage and adoption. And anything that we build or introduce, we really talk about earn the right internally a lot, which is we have to provide so much value or save so much time that people will use us. But those are the two things that are close to us, is we know that the product won't be used unless it is deeply interoperable.

**Chai [00:46:01]:** And strategically, to your point, it's like what does EHR want to own versus us? EHRs are really focused on the clinical workflows and so forth but some of the things that we're talking about here, I do these traditionally are outside of the domain where it's oh, connecting pairs and providers together with provider policies or the clinical trial matching, as Janie brought up. And so these are, entirely -- we position ourselves as building this entirely new intelligence, clinical intelligence layer across, again, providers, pharma and, payers.

**Chai [00:46:33]:** And so that's a it's a whole different ballgame that we try to play

**Chai [00:46:36]:** In combination with them.

**Jacob [00:46:37]:** But it's like a different layer of scope.

## Healthcare AI Regulation, Technical Depth, and What Changed Their Minds

**Jacob [00:46:39]:** I'm curious, you are both relatively newcomers to healthcare. People have these, there's lots of futuristic healthcare AI takes of "Oh, everything will look different.", now that you've been in healthcare for a bit, you live at the edge of AI, what have you, changed your mind on around this, as you think about what healthcare looks like in ten, 20 years? Any updates to your mental model from the time being close to the problems?

**Chai [00:47:02]:** One thing that I

**Chai [00:47:04]:** Was hesitant about before and it's a common thing when I'm trying to recruit engineers that people ask me around, is definitely oh, healthcare, heavily regulated space. And it is, rightfully so. You want to keep, the patients at the end of the day safe. But one of the interesting things that, is a that surprised me how much it is coming to the company is there's a lot of really favorable regulatory tailwinds as well. Where you think about, government really wants interoperability between all these systems that we talked about and so agents can access this information. The government just in January, the FDA released updated guidance on clinical decision support, what I work on in such a way that they used to have guidance from like 2022 that required you to have, mention all these options and do all these other things but it's a very forward and forward-looking way. And so for me, what's been really cool to work on is this, there's this very special moment both in AI in general, we all know that but there's a special moment also regulatory in healthcare as well.

**Janie [00:48:05]:** One thing I would call out is for the very reasons things are higher stakes or, potentially considered more difficult in healthcare, it's where some of the hardest AI problems will get solved first, just because the bar is so high. When I first joined, I was "Oh, this is where we'll be on the tail end of where, all of the AI innovation will be able to be applied." But when you think about, zero error evals or multi-step workflows that have really low tolerance, a lot of the innovation will happen here just because we have to or else we can't ship.

**Jacob [00:48:42]:** 'Cause like in other domains, you'd much rather just solve the 80%-is-good-enough problems first

**Janie [00:48:46]:** 80/20 doesn't work here

**Chai [00:48:48]:** And building off that, traditionally, there was a bit of stigma that, oh, healthcare companies are not that interesting from a technical perspective or I've seen that or faced that myself. But these are really hard and fun problems from a pure technical perspective beyond just the impact. How do you bring the latency of this thing down and make it really high-quality?

## Reducing Latency: Clinical Workflows, Agents, and Implementation Reality

**Jacob [00:49:07]:** How do you bring the latency of things down?

**Chai [00:49:10]:** Yeah. Yeah. Yeah. So okay, let's answer the latency question. And maybe hopefully not too redundant with some of the things I've said earlier but some part of it is with any latency, you have to like what is, what is really your bottleneck. In a lot of workflows, it's sometimes it's the model itself. And so that's where like our data flywheel, our post-training team and so forth come in so that can you make the models far more efficient. So that's one aspect of latency. But there's whole other aspects of latency where it's okay, on top of that, if you use a constellation of different models, can you use -- can you first use like a -- it's like thinking fast and slow. Can you use a cheap, fast model that triages and hands it off to a larger model where you get more intelligence and so forth and so all these

**Chai [00:49:56]:** Clever tricks to make it work.

**Chai [00:49:58]:** And by the way, we are totally -- we also realize that the parameter frontier is changing and so these tricks will -- may not get us to where we want to be in five years but we need to if we want to build a useful product right now.

**Jacob [00:50:11]:** Should we go to the quick-fire or you want to ask more about Abridge? We can stuff everything that's not Abridge into the quick-fire

**Swyx [00:50:16]:** I don't mind. I was -- I feel like Janie was on the topic of more long tail stuff, which is

**Swyx [00:50:21]:** Not the eighty/twenty thing and that really matters. And I'll --, if you have any tips or cool stories or just general approaches that have worked for you that's interesting to dig into.

**Janie [00:50:32]:** One of them is even just how we staff our teams looks different than a traditional software engineering team, I'd say.

**Swyx [00:50:40]:** Let's go.

## Clinician Scientists, Edge Cases, and Evals at Scale

**Janie [00:50:41]:** We have a bunch of folks with different roles who are clinicians and so we have this role called the clinician scientist and I heard one of our leaders refer to them as mutants recently. But they are people who've had clinical backgrounds, so MDs typically, who are also deeply technical, somewhere, on the spectrum of like a full stack engineer all the way to like extremely scrappy prompter. But having each of these people embedded within our teams instantly raises the bar for everything that we build because not only are they determining, is this product clinically useful but they're deeply embedded in our whole evals process. And so when we talk about LFDs, when we talk about what is our actual evaluation criteria, you don't want Chai or me creating what those are because we don't have clinical background. But is probably unique to Abridge but has been game changing. And when you think about where the puck is going, you have people build with clinical backgrounds who are technical and where AI tools are going, they just become

**Janie [00:51:53]:** More and more, critical and like the killers of the team. And so that's one. And then the second is just the scale at which we do evals to catch that long tail up front before anything ever gets into production is something that we've pretty much like really started to fine-tune, both from a scale but when do we know we need to get several hundred versus several thousand offline responses, what helps us make that quick decision and make this less of an art and as much of a science as possible. But that's also been something we've had to tune over time.

**Swyx [00:52:27]:** And you have partners who opted in to give you those evals.

**Janie [00:52:31]:** So we work either internally or with third-party for offline evals and then we have customers who also agree to give us, whether it's like thumbs up, thumbs down to like choose this or that, a lot of data to get us to what is as close to fully confident as possible.

**Swyx [00:52:51]:** The term that comes to mind is

**Swyx [00:52:53]:** Like active learning on things where you're weak. I feel like it's a lost art

**Swyx [00:52:58]:** Is a lot of the polish that comes into doing something like this.

**Janie [00:53:02]:** Really.

**Chai [00:53:03]:** Hundred percent.

## Lessons from Glean: Technical Foundations and AI App Infrastructure

**Jacob [00:53:04]:** Maybe, on a totally unrelated note, Chai, you had a very, storied run at Glean before heading over to Abridge. And so, I'm curious like that -- it's was one of the early AI app success stories. As reflecting back on that experience, what do you think Glean got most, maybe most wrong? Yeah, curious for your reflections.

**Chai [00:53:24]:** The... I attribute Glean's success really to very strong technical foundations, that have really stood the test of time. And so it started with -- it started with a known problem and like finding information where work is hard. The best technology at the time was to build really high-quality search. A lot of times enterprise search startups failed because the quality wasn't great enough. But the learning that people took away from that is, oh, enterprise search is not good enough. And so like quality, really changes the game of like if something can be useful or not. It's like similarly like people may have taken it that way, "Oh, Alexa voice assistants are not that useful." But when you have quality, things can change the game. And so Glean's early foundations, by bringing people who had built search at Google, the best place to have ever built search and being really creative and having a very concrete problem to solve but with the right technical backgrounds, laid the foundation for all of its success for the many years to come. And what's interesting is always figuring out, hey, how does a company adapt in this, as we all know and we've talked many times, in this changing landscape. And so for Glean, how do you put this context layer to the use, has been the thing that we've really, the last few years, has been the fun from the challenge. That where like you could say, that's been the opportunity for the company as well as the challenge as well.

**Jacob [00:54:46]:** Definitely a competitive market. It feels like one at the epicenter of the foundation models and, the hyperscalers, so it'll be interesting to see how it all plays out.

**Chai [00:54:55]:** When you think about can you build something that helps everyone at knowledge work as well is a massive opportunity.

**Jacob [00:55:02]:** Always my mental model is like there's a few markets that are like the foundation model companies have to win or are like big enough to go after and It's probably like consumer code and that.

**Jacob [00:55:11]:** And so it would definitely be interesting to see how it plays out. One thing we often think about on the investing side is, the pace of progress in models changes so fast and so the building patterns adjust so fast. And it's always hard to figure out, what pieces of the way people are building today, the infrastructure tools they use, are going to prove persistent versus, okay, six months later we're doing something completely different because

**Jacob [00:55:31]:** Models have improved. I'm curious of the stuff you use today, how do you think about the pieces of AI infrastructure software that feel a little bit more persistent?

**Chai [00:55:40]:** So generally, if you take the thesis that the models are going to be more and more agentic, before we had to build a lot of scaffolding around that. In previous gigs, I've -- we've effectively, we made our own DSL effectively and you can view the because the models were not capable enough, so you needed to simplify things. And you can view it similar to other agent frameworks. But over time, if the models become more and more agentic and can use the similar tools that we already have, where it's like computer use, writing code itself in sandbox, much more around, far more about, what are the right context layers and the tools to give agents. And then the other things that I think about are how do you really build truly event-driven real-time systems and especially at Abridge, again, where you're doing something real-time in the conversation. And so there's a lot of event-driven technology. And by the way, stuff that we've always used in the past, whether it's Kafka, Temporal, Sockets and so forth, how do you bring that together is also durable. Or thinking about patterns in which humans collaborated with each other on Google Docs. How do you think about like CRDT and so forth when you have conflicts, when you have multi-agent systems? So all these things that we've built for -- the things we've built for humans are the things that are going to be, continue to be durable.

**Jacob [00:56:55]:** . Just with like 1,000 times more the scale of agents running at them instead.

**Jacob [00:56:58]:** They're going to really work.

**Chai [00:56:58]:** So make sure that they scale, of course and fast and whatnot. Without a doubt, yes.

## How Agentic Does Abridge Become?

**Swyx [00:57:03]:** Does Abridge become more agentic over time than, what is the next more agentic version of that look like?

**Swyx [00:57:10]:** 'Cause you're already pretty proactive it's, with like the notifications.

**Chai [00:57:15]:** And so I view that as like a piece of being agentic but I also view it as maybe some of the things we mentioned before, oh, reacting to labs or, doing work in the background or doing

**Chai [00:57:25]:** Even more capabilities on behalf of the clinician, who we believe has a super important role to play as, in terms of patient connection and so forth.

## What They Changed Their Minds On: PRDs, Prototypes, and Judgment

**Jacob [00:57:34]:** I'm curious for both of you, what's one thing you've changed your mind on in AI in the past year?

**Janie [00:57:39]:** The one I flopped on and this is much more product specific, is, probably the hotter take is that prototypes are the end all be all and that PRDs are dead.

**Janie [00:57:51]:** We've tried switching and... We continue to evolve the way product is developed and, the products that we're building are extremely complicated and nuanced and it is very difficult for a prototype to capture the full complexity of what can we or can't we do with this data. What and who... Is this the actual right problem to be solving for in a world where software has become so cheap? Yes, this is a cool looking prototype but should we be spending any of our precious hours here? If so, why? And how does this deepen our moat in a world of decreasing moats? Does this require custom implementation from our customer to use? None of that gets captured in a prototype and so we've, we're continuously evolving the way that we develop product here but even if not written in the same traditional ways as it was two years ago, as a team we've gotten pretty, high conviction that in a world of so much noise, crisp written clarity is more important than ever. It might now live in a markdown file that more teams and systems can use as context but that's probably one that is much more

**Swyx [00:59:06]:** So you're

**Janie [00:59:06]:** Function specific to me.

**Jacob [00:59:08]:** I love that.

**Swyx [00:59:09]:** You're disagreeing with the consensus

**Janie [00:59:10]:** That PRDs are dead

**Swyx [00:59:11]:** That's great, yeah.

**Swyx [00:59:12]:** So you are like

**Janie [00:59:14]:** That prototypes are the thing.

**Janie [00:59:14]:** We should partner with AI to create great documentation but first, probably most important, is strategically answering like why is this problem the one our company and our product should solve? What happens if the next 20 competitors build this? Why, what is our right to win and does this help us differentiate in any way or are we just adding noise? It's important

**Swyx [00:59:39]:** That's a high bar. I don't know if I could answer that

**Swyx [00:59:41]:** Because a lot of the times the answer is let's do it first.

**Janie [00:59:44]:** And when the cost of doing it first is so expensive, we just talked through the process of getting something out to customers. You need to have a higher bar for as a business, should we invest here? And as all of our roles evolve, one of product or like all of our jobs become should we do this thing? And that's something that is worth the time spending up front on. And then, as you think about prototypes, it's still really valuable to quickly show, "Here are the 20 ways we could do it. Clinician, I would love your feedback, which one resonates more?" Or as you get into deeper fidelity, you can also make the prototypes deeper fidelity and like get it as close to production ready as possible. But, beyond that, to get it out to customers, there's a lot of implementation details, security compliance, edge cases, things that never get caught in a prototype that need to be written out somewhere. And so they look different but still more important than ever.

**Jacob [01:00:52]:** It's interesting. I imagine a lot of that also is like given the context of the stage that Abridge is at.

**Jacob [01:00:58]:** I feel like for so many early stage companies, it's just a desperate race to... You throw like 30 things at the wall, you're "Please, something just like resonate with my end buyer." and, you find something and that's, why the prototype first approach is so powerful. But for you all, it's like anything you're going to do is across 200 systems, there's like a whole, implementation change management side of things and you get a few big bullets to fire at at what you want those systems to do. And so being really thoughtful about that.

**Chai [01:01:25]:** It makes a ton of sense and maybe the prototype first takes will all grow into your view of the world when they're a bit more scaled.

**Janie [01:01:32]:** The weekend demo versus it works at the largest health systems is, a massive gap. I don't think it means we can't go fast. This is the fastest I've built in my career, right now and the

**Chai [01:01:47]:** Compared to Loom?

**Janie [01:01:48]:** From a the complexity and the scale of the products we're trying to build and the problems we're trying to solve, I'd say, yes, maybe I, updated a flow or, shipped a new feature pretty quickly but if you think about some of the products we're building, we're trying to collapse prior authorization, things that used to take 45 days across maybe 20 different touch points into one. I'm building faster than I ever have and so the thoughtfulness allows us just to go fast at the right things. It sounds contradictory but that

**Chai [01:02:28]:** No

**Janie [01:02:28]:** Thought up front

**Chai [01:02:28]:** Go slow to go fast.

**Janie [01:02:29]:** Exactly.

**Chai [01:02:30]:** It's interesting. In the... When a lot of things are changing and in the AI discourse, sometimes we lose sight of things that always stood the test of time. Judgment and clarity always matters. As an engineer, sometimes I don't want a prototype. I would like to see... I want the written, the clarity that comes from writing and then we build that. And again, for some things, of course, where it's a small thing, yeah, just ship the prototype. That's why, don't sweat the details. So the interesting thing, the nuance that gets lost sometimes in discussion is, sometimes we need to recalibrate our judgment for sure because the costs and gains have changed but that doesn't mean we go all the way on one spectrum or the other.

## AI Tools, Claude Code, and Closing Notes

**Chai [01:03:11]:** Outside of your specific tool, I always like to ask this question, any other AI tools that you guys are enjoying?

**Chai [01:03:16]:** Claude Code. But, that feels, too basic of an answer.

**Chai [01:03:20]:** Is all of Abridge engineering very built on Claude Code?

**Chai [01:03:23]:** Yes.

**Chai [01:03:23]:** Wow.

**Chai [01:03:23]:** Very much so. I won't

**Chai [01:03:26]:** We also have Cursor as well.

**Chai [01:03:28]:** Many of the

**Chai [01:03:29]:** I'm just checking the boxes here.

**Chai [01:03:30]:** Many of the tools available but it's like you look at just earlier in the day, you see an engineer's screen. You see, six different, Claudes running at it. Sometimes the same person, I've seen them on the sofa now with the remote control as well on the mobile. But, very much so. One of the interesting things for me is, as a relatively new person to companies, Claude Code helps me onboard much faster or any of these AI code... And, I feel like I learn so much. I do love the memes of "Claude's going to do this." So, I'd like to see Claude,

**Chai [01:04:00]:** The venture equivalent is "I'd like to see Claude go do a company at a billion dollars pre-revenue." Like

## Where to Learn More: Whitepapers, Research, and AbridgeHQ

**Chai [01:04:06]:** We always like to leave the last word in these conversations to you both. And so, any place you want to point folks where they can go learn more about Abridge, the work you're doing, any of the research you guys have done, whatever. The floor is yours.

**Chai [01:04:18]:** A couple places. If you... On our Abridge website, we have a lot of our whitepapers where we've done a lot of interesting work, such as, reducing a hallucination objection.

**Chai [01:04:27]:** Very well-presented, by the way. I liked it. Yeah.

**Chai [01:04:29]:** Thank you. Our science team rigorously defined what is the problem. And one of the interesting things, by the way, at Abridge, is we have multiple, stats professors on staff as well. So in that specific whitepaper, Michael Oberst, who's a professor at JHU. And so we have multiple... And from that comes, very high rigor and then also our taste for design comes from really good presentation. But setting that aside and we're going to have many more technical topics there, please follow our Twitter account as well, AbridgeHQ. And then the other thing I'll plug a little is, we have a open house of diving deep into AI and healthcare coming up with Andreessen Horowitz.

**Chai [01:05:07]:** Amazing. Well, thanks so much.

**Janie [01:05:09]:** Thanks.

**Chai [01:05:09]:** This was super fun.

**Chai [01:05:10]:** Thanks so much.

**Chai [01:05:10]:** Thank you.

---

## [[AINews] Codex Rises, Claude Meters Programmatic Usage](https://www.latent.space/p/ainews-codex-rises-claude-meters)
*🔬 Latent Space | 2026-05-14*

It has been a tale of two cities in the past 3 weeks since the launch of GPT 5.5; while the finance folks fall in love with [Anthropic's growth](https://www.latent.space/p/ainews-anthropic-growing-10xyear) and [CFO](https://x.com/anquetil/status/2054637012850970631) ahead of its likely October IPO, there has been a notable rise in pro-Codex sentiment among AI Engineers, likely a combination of GPT 5.5 being a really good (in [some scenarios Mythos-tier](https://x.com/mschoening/status/2054565859491029497?s=12)) model, launch of [Codex for Everything Else](https://www.latent.space/p/ainews-agents-for-everything-else), and, a third thing, which is the trigger for today's op-ed: more generous limits.

[](https://substackcdn.com/image/fetch/$s_!uqHa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1f3bb92f-f1bd-4329-9b9c-64c681eec378_1290x874.png)

The messaging for Claude's pricing change was generally pretty well done, it is simply not what uses of alternative harnesses wanted to hear: [every Claude subscription now gets a monthly credit of API tokens equal to the dollar amount of the Claude subscription plan.](https://x.com/ClaudeDevs/status/2054610152817619388) So you pay $200, you get BOTH a Claude subscription with its own limits for using Claude on Anthropic-owned harnesses like Claude.ai and Claude Code ("interactive usage"), AND $200 worth of API credits for using Claude everywhere else including `claude-p`, OpenClaw and others ("programmatic usage"). 

If things had worked this way from the start, it would have been viewed as a very good deal:

[](https://substackcdn.com/image/fetch/$s_!XQLi!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F148215c3-6a2e-4a77-b243-630d5c9c7247_1228x1640.png)

However, because of the historical subsidy/pricing advantages (estimated between 70-90% discount from API pricing), people are viewing it [as a "rug pull" of sorts](https://x.com/ClaudeDevs/status/2054610152817619388/quotes) -- however it's nice to have an official policy in place as opposed to the selective targeting of [OpenClaw](https://x.com/kloss_xyz/status/2040211360156700843), [OpenCode](https://x.com/thdxr/status/2034730036759339100?s=20), and uncertain status of less popular harnesses.

[](https://substackcdn.com/image/fetch/$s_!w6yx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F041d6b0a-7ea1-4e96-82ad-750ed4e73f25_1208x1394.png)

That these headlines come on the same day as [OpenAI launches their enterprise switch](https://x.com/OpenAIDevs/status/2054586214112780518/quotes) promo is an incredible coincidence:

[](https://substackcdn.com/image/fetch/$s_!6upS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8449d76d-2f12-4dde-a825-744697b02502_1192x1116.png)

At the end of the day, we would caution against reading too much into swings either way - both labs are doing very well, and these are in the grand scheme of things normal pricing shifts by people inventing the future of coding while figuring out optimal pricing as they shake up a decades-old industry. Anthropic was more liberal in the beginning, but now that Claude Code has a sustainable brand and clout as an agent harness, Anthropic is putting its most favorable pricing behind its own tools and metering everything else, whereas Codex as the challenger is being more liberal with everything.

Perhaps hardware is destiny, perhaps this is part of a longer 6 month alternating cycle of the "[mandate equinox](https://x.com/irl_danB/status/2050051868597080482)":

> AI News for 5/12/2026-5/13/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

# **AI Twitter Recap**

**Agent Infrastructure, Harnesses, and Developer Platforms**

  * **Cline, LangChain, Notion, and Cursor all pushed deeper into agent platform territory** : [Cline](https://x.com/cline/status/2054580767779700775) open-sourced a rebuilt **Cline SDK** and refreshed CLI with a TUI, agent teams, scheduled jobs, and connectors, positioning its harness as a reusable substrate for custom coding agents. [LangChain](https://x.com/LangChain/status/2054617687238865013) shipped a large batch of agent lifecycle infrastructure at Interrupt: **LangSmith Engine** , **SmithDB** , **Sandboxes** , **Managed Deep Agents** , **LLM Gateway** , **Context Hub** , and **Deep Agents 0.6**. The most technically notable piece is [SmithDB](https://x.com/LangChain/status/2054658661776244936), a purpose-built observability database for nested, long-running traces with large payloads, reportedly yielding **12 -15×** faster access on key workloads; the team says it is built atop [Apache DataFusion and Vortex](https://x.com/ankush_gola11/status/2054681251513254260). In parallel, [Notion's External Agents API](https://x.com/NotionDevs/status/2054600524423733307) lets third-party agents such as Claude, Codex, Cursor, Decagon, Warp, and Devin operate directly inside Notion as a shared, reviewable context layer rather than another silo. [Cursor](https://x.com/cursor_ai/status/2054651526715502998) expanded cloud agents with fully configured **development environments** including cloned repos, dependencies, version history, rollback, scoped egress, and isolated secrets.

  * **Agent UX is increasingly about long-running state, streaming, and orchestration rather than chat** : Several launches converged on the same design direction. [Duet Agent](https://x.com/dzhng/status/2054619807715348779) proposes a state-machine harness for jobs that last **weeks or months** , with parent/sub-agent coordination and memory replacing compaction. LangChain's OSS updates added [streaming typed projections, checkpoint storage, code interpreter, harness profiles, and model-specific tuning](https://x.com/LangChain_OSS/status/2054641656222388700), all aimed at richer agent event streams than plain tokens. [Tabracadabra](https://x.com/oshaikh13/status/2054613590695641269) moved from autocomplete to a context-aware assistant in any textbox, while [VS Code](https://x.com/code/status/2054669377367064613) introduced an Agents window and better multi-project task review. The architectural message across these releases is that production agents increasingly need **durable execution, inspectable intermediate state, and tool-native UI surfaces** rather than stateless prompt/response loops.




**Model Training, Architecture, and Data Efficiency**

  * **Pretraining efficiency and architectural experimentation were the strongest research throughline** : [Nous Research's Token Superposition Training](https://x.com/NousResearch/status/2054610062836892054) modifies the early phase of pretraining so the model reads/predicts contiguous bags of tokens before reverting to standard next-token prediction; they report **2 -3× wall-clock speedup at matched FLOPs** with no inference-time architecture change, validated from **270M to 3B dense** and **10B-A1B MoE**. [Jonas Geiping et al.](https://x.com/jonasgeiping/status/2054600427128201688) argued current message-based/chat training overly constrains agents to a single stream and released a **multi-stream LLM** paper claiming lower latency, cleaner separation of concerns, and more legible parallel reasoning/tool use; paper and code are linked [here](https://x.com/jonasgeiping/status/2054600457746579816). [δ-mem](https://x.com/dair_ai/status/2054600147020222630) proposed an external online associative memory attached to a frozen full-attention backbone, with an **8 ×8 state** reportedly improving average score by **1.10 ×** and beating non-δ-mem baselines by **1.15 ×**, with larger gains on memory-heavy benchmarks.

  * **Post-training/compression and data curation also produced notable results** : NVIDIA's [Star Elastic](https://x.com/PavloMolchanov/status/2054607257166553292) claims one post-training run can derive a family of reasoning model sizes, at **360 × lower cost than pretraining a family** and **7 × better than SOTA compression**. Datology's VLM work, highlighted by [Siddharth Joshi](https://x.com/sjoshi804/status/2054566179369574419) and [Pratyush Maini](https://x.com/pratyushmaini/status/2054607891202777192), argues **data curation alone** can produce major multimodal gains: **+11.7 points across 20 public VLM benchmarks at 2B** , beating InternVL3.5-2B by roughly **10 points** at about **17 × less training compute**, and near-frontier 4B performance with **3.3 × lower response FLOPs** than Qwen3-VL-4B. On the open data side, [Percy Liang](https://x.com/percyliang/status/2054550981527146942) said the next **Marin** run already has **18T tokens** in its mix and is still seeking more pretraining, mid-training, and SFT data, with a companion token viewer [shared here](https://x.com/percyliang/status/2054550984597328101).

  * **Open evaluation and dataset work is maturing alongside model building** : [Kevin Li's SWE-ZERO-12M-trajectories](https://x.com/kevin_x_li/status/2054600962137100493) is positioned as the largest open agentic trace dataset: **112B tokens, 12M trajectories, 122K PRs, 3K repos, 16 languages**. [Victor Mustar](https://x.com/victormustar/status/2054495700822478943) flagged **llama-eval** as a step toward more comparable llama.cpp community evals. Meanwhile, [Steve Rabinovich](https://x.com/steverab/status/2054564579573698921) and [Sayash Kapoor](https://x.com/sayashk/status/2054569643080077576) argued credible agent evaluation requires **log analysis** , not outcome-only metrics, because stronger agents expose hidden benchmark bugs and reward-hacking paths.




**Enterprise AI Pricing, Platform Competition, and Distribution**

  * **Anthropic vs OpenAI competition sharpened around enterprise distribution and developer lock-in** : [Ramp data cited by Andrew Curran](https://x.com/AndrewCurran_/status/2054582686698848294) showed **Anthropic at 34.4%** of businesses vs **OpenAI at 32.3%** in April, the first apparent lead change in business adoption; [The Rundown](https://x.com/TheRundownAI/status/2054588969044627906) amplified the same figures. At the same time, Anthropic changed plan economics: [ClaudeDevs announced](https://x.com/ClaudeDevs/status/2054610152817619388) that paid Claude plans will get a dedicated monthly credit for programmatic usage across the **Agent SDK** , `claude -p`, GitHub Actions, and third-party SDK apps. This was immediately read by power users as a major restriction on subscription-subsidized harnesses, with criticism from [Theo](https://x.com/theo/status/2054620998205624746), [Jeremy Howard](https://x.com/jeremyphoward/status/2054682882753597603), [Matt Pocock](https://x.com/mattpocockuk/status/2054655310388674693), and [Omar Sanseviero](https://x.com/omarsar0/status/2054679776397300188). Anthropic partially offset that backlash with a separate [50% increase in Claude Code weekly limits](https://x.com/ClaudeDevs/status/2054639777685934564) through July 13, stacked on the previously announced 2× 5-hour limit increase.

  * **OpenAI responded aggressively with Codex enterprise incentives** : [OpenAI Devs](https://x.com/OpenAIDevs/status/2054586214112780518) and [Sam Altman](https://x.com/sama/status/2054626219858293128) offered **two months of free Codex usage** for enterprise customers switching in the next 30 days. OpenAI also published more technical platform detail, including a [Windows sandbox design write-up](https://x.com/reach_vb/status/2054655421013434510) describing the combination of local users, firewall rules, ACLs, write-restricted tokens, DPAPI, and helper executables needed to safely run coding agents with local filesystem/tool access. The competitive dynamic now looks less like "best model wins" and more like **subsidy + workflow control + harness compatibility**.

  * **Enterprise adoption is increasingly tied to runtime/security assurances** : [Perplexity](https://x.com/perplexity_ai/status/2054608966148374715) described a hardware-isolated sandbox architecture with VPC-level separation, short-lived proxy tokens, and scanning of external content before agent actions, with [additional details](https://x.com/perplexity_ai/status/2054608978680873457) on encryption and auto-deletion. [Aravind Srinivas](https://x.com/AravSrinivas/status/2054619058650411174) framed this as foundational to Perplexity becoming an enterprise knowledge/research platform. The broader pattern: agent vendors are no longer selling only intelligence; they're selling **bounded execution environments**.




**Autonomous Science, Cyber Capability, and Robotics**

  * **Recursive self-improvement moved from idea to startup cluster** : The largest single meta-theme was the launch of [Recursive](https://x.com/_rockt/status/2054491251345391852), founded to build AI that automates science and safely improves itself. Launch posts from [Richard Socher](https://x.com/_rockt/status/2054491251345391852), [Josh Tobin](https://x.com/josh_tobin_/status/2054576051431616873), [Dominik Schmidt](https://x.com/schmidtdominik_/status/2054498117416808727), [Jenny Zhang](https://x.com/jennyzhangzt/status/2054603211798147436), and [Shengran Hu](https://x.com/shengranhu/status/2054630820305088739) suggest a team drawn from open-endedness, AI Scientist, and research automation work. In adjacent work, [Adaption's AutoScientist](https://x.com/adaption_ai/status/2054532113316434061) aims to automate the full training-research loop outside frontier labs, with [Sarah Hooker](https://x.com/sarahookr/status/2054551263275254084) arguing that most model training failures are due to research-loop brittleness rather than mere compute scarcity.

  * **Cyber capability evaluations continue to steepen** : The UK [AI Security Institute](https://x.com/AISecurityInst/status/2054589758043496567) said the length of cyber tasks frontier models can complete has been doubling every few months, and that recent models are beating prior trends. Anthropic/Glasswing's [Logan Graham](https://x.com/logangraham/status/2054613618168082935) said **Claude Mythos Preview** is the first model to solve both AISI end-to-end cyber ranges, including **Cooling Tower** , and the only one to clear every task under the institute's **2.5M-token** cap. XBOW reportedly found "token-for-token, unprecedented precision," and partner usage allegedly surfaced **thousands of high/critical vulnerabilities** in weeks. Independent commentary from [scaling01](https://x.com/scaling01/status/2054594892903436553) claimed a newer Mythos version completed a cyber range **6/10 times vs 3/10** for the preview baseline.

  * **Robotics got a concrete long-horizon deployment demo** : [Figure's Brett Adcock](https://x.com/adcock_brett/status/2054603963996278786) streamed humanoid robots running a full **8-hour autonomous shift** on package sorting using **Helix-02** , with follow-up details that the robots reason from camera pixels, operate around **human parity (~3s/package)** , perform **on-device inference** , coordinate as a networked fleet, autonomously swap for low battery, and self-diagnose/fail over to maintenance when needed [here](https://x.com/adcock_brett/status/2054615837903048807). This is one of the clearer public demonstrations of **multi-robot, long-duration, no-human-in-the-loop orchestration** rather than a short benchmark clip.




**Top tweets (by engagement)**

  * **Claude Code pricing and limits** : [@ClaudeDevs on 50% higher weekly limits](https://x.com/ClaudeDevs/status/2054639777685934564), [@ClaudeDevs on programmatic credits](https://x.com/ClaudeDevs/status/2054610152817619388), and the ensuing developer backlash from [@theo](https://x.com/theo/status/2054620998205624746) made pricing policy the day's most consequential developer story.

  * **Codex enterprise push** : [@sama offering two free months of Codex usage for switchers](https://x.com/sama/status/2054626219858293128) and [@OpenAIDevs' enterprise call-to-action](https://x.com/OpenAIDevs/status/2054586214112780518) signaled an unusually direct go-to-market counterpunch.

  * **Figure 's 8-hour humanoid shift**: [@adcock_brett's livestream post](https://x.com/adcock_brett/status/2054603963996278786) drew enormous attention and is one of the few viral posts in the set with clear technical substance.

  * **Cline SDK launch** : [@cline's SDK release](https://x.com/cline/status/2054580767779700775) was one of the highest-engagement genuinely technical launches, reflecting demand for open coding-agent harnesses.

  * **Token Superposition Training** : [@NousResearch's TST post](https://x.com/NousResearch/status/2054610062836892054) stood out as a rare pretraining-method tweet that broke through widely, likely because the claim--**2 -3× training speedup without changing inference-time architecture**--is concrete and economically important.




* * *

# **AI Reddit Recap**

## **/r/LocalLlama + /r/localLLM Recap**

### **1\. Efficient On-Device LLM Inference**

[ Read more ](https://www.latent.space/p/ainews-codex-rises-claude-meters)

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

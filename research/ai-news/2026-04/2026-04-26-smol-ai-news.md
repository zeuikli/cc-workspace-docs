# 🌐 Smol AI News — 2026-04-26

> Discord、Reddit 等 AI 社群圈內直擊（已從 buttondown 遷移至 news.smol.ai）
> 來源：[Smol AI News](https://news.smol.ai/rss.xml)

---

## [DeepSeek v4](https://news.smol.ai/issues/26-04-24-deepseek-v4/)
*🌐 Smol AI News | 2026-04-24*

**a quiet day.**

> AI News for 4/23/2026-4/24/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

# AI Twitter Recap

**Top Story: DeepSeek V4**

## What happened

DeepSeek released **DeepSeek-V4 Pro** and **DeepSeek-V4 Flash** , its first major architecture refresh since V3 and first clear two-tier lineup, with **1M-token context** , hybrid reasoning/non-reasoning modes, an **MIT license** , and a technical report detailed enough that multiple researchers called it one of the most important or best-written model papers of the year. Across the reactions, the factual consensus is that V4 materially advances open-weight long-context and agentic coding performance while remaining somewhat behind the top closed frontier models overall. Independent benchmarkers place **V4 Pro around the #2 open-weights tier** , roughly near **Kimi K2.6 / GLM-5.1 / strong Claude Sonnet-class to Opus-ish** depending on benchmark and mode, with especially strong long-context and agentic performance; opinions diverge on how close it is to GPT-5.x / Opus 4.7 and on whether this is “democratizing” progress or an architecture so complex that few open labs can realistically reproduce it. Key sources include deep-dive commentary from [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2047735160544841953), [@scaling01](https://x.com/scaling01/status/2047618271310926151), [@nrehiew_](https://x.com/nrehiew_/status/2047665987730993363), [@ben_burtenshaw](https://x.com/ben_burtenshaw/status/2047646980139016560), [@TheZachMueller](https://x.com/TheZachMueller/status/2047702488418030066), [@ZhihuFrontier](https://x.com/ZhihuFrontier/status/2047664976215839021), and infra/vendor posts from [@vllm_project](https://x.com/vllm_project/status/2047843293447500069), [@NVIDIAAI](https://x.com/NVIDIAAI/status/2047765637808664759), and [@Togethercompute](https://x.com/togethercompute/status/2047743446522224987).

## Core facts and technical details

The most concrete technical claims repeated across the discussion:

  * **Two models**

    * **V4 Pro:** **1.6T total parameters / 49B active**
    * **V4 Flash:** **284B total / 13B active**
    * Reported by [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2047735160544841953), [@teortaxesTex](https://x.com/teortaxesTex/status/2047630981364883816), [@baseten](https://x.com/baseten/status/2047779549644243146), [@NVIDIAAI](https://x.com/NVIDIAAI/status/2047765637808664759)
  * **Context**

    * **1M tokens** , up from **128K in V3.2** per [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2047735160544841953)
    * Multiple posters frame this as the headline achievement: “solid ultra-long context” [@teortaxesTex](https://x.com/teortaxesTex/status/2047623905754448043)
  * **Training scale**

    * **32T–33T tokens** cited repeatedly
    * [@nrehiew_](https://x.com/nrehiew_/status/2047666048334450754) notes **32T tokens** over **1.6T parameters** , i.e. roughly **20 tokens/parameter**
    * [@teortaxesTex](https://x.com/teortaxesTex/status/2047630981364883816) cites **33T**
    * [@nrehiew_](https://x.com/nrehiew_/status/2047840706874749076) estimates pretraining compute at **~1e25 FLOPs**
  * **Reasoning / modes**

    * DeepSeek exposes **three reasoning modes** per [@Togethercompute](https://x.com/togethercompute/status/2047743446522224987)
    * Hybrid “thinking/non-thinking” positioning noted by [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2047735160544841953)
  * **Long-context architecture**

    * Several threads summarize a new hybrid attention system: 
      * shared KV vectors
      * compressed KV streams
      * sparse attention over compressed tokens
      * local/sliding-window attention for nearby context
    * [@ZhihuFrontier](https://x.com/ZhihuFrontier/status/2047664976215839021) gives the most compact public summary: 
      * **2× KV reduction** via shared key-value vectors
      * **c4a ≈ 4× compression**
      * **c128a ≈ 128× compression**
      * **top-k sparse attention** on compressed tokens
      * **128-token sliding window**
      * **1M context KV cache = 9.62 GiB/sequence (bf16)**
      * **8.7× smaller** than DeepSeek V3.2’s **83.9 GiB**
      * FP4 index cache + FP8 attention cache gives another ~**2×** reduction
    * [@ben_burtenshaw](https://x.com/ben_burtenshaw/status/2047646980139016560) condenses this to “**10× smaller KV cache** ”
    * [@TheZachMueller](https://x.com/TheZachMueller/status/2047702488418030066) and [@TheZachMueller](https://x.com/TheZachMueller/status/2047702996524405175) describe **CSA + HCA** layer patterns, with alternating layers and V4 Flash using sliding-window layers instead of HCA in some places
  * **Quantization / checkpoint format**

    * [@LambdaAPI](https://x.com/LambdaAPI/status/2047654086263320965): checkpoint is **mixed FP4 + FP8**
      * **MoE expert weights in FP4**
      * attention / norm / router in **FP8**
      * claim: the full model fits on a single **8×B200** node
  * **Inference hardware / serving**

    * [@NVIDIAAI](https://x.com/NVIDIAAI/status/2047765637808664759): on **Blackwell Ultra** , V4 Pro can deliver **150+ TPS/user interactivity** for agentic workflows
    * [@NVIDIAAI](https://x.com/NVIDIAAI/status/2047823093578518758): published day-0 V4 Pro performance pareto using **vLLM**
    * [@SemiAnalysis_](https://x.com/SemiAnalysis_/status/2047726025748930687): day-0 support and benchmarking across **H200, MI355, B200, B300, GB200/300**
    * [@Prince_Canuma](https://x.com/Prince_Canuma/status/2047685898163147125): **DeepSeek4-Flash on 256GB Mac**
    * [@Prince_Canuma](https://x.com/Prince_Canuma/status/2047847095466385899): MLX quants published
    * [@simonw](https://x.com/simonw/status/2047844236142497850) asks about smaller-RAM Mac viability, implying community interest but incomplete support story
    * [@QuixiAI](https://x.com/QuixiAI/status/2047765475937890474) reminds users that many local stacks still lack tensor parallel, relevant because V4-class models strongly stress inference infra
  * **License / availability / pricing**

    * **MIT license** per [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2047735160544841953)
    * first-party API plus rapid third-party availability via [@Togethercompute](https://x.com/togethercompute/status/2047743446522224987), [@baseten](https://x.com/baseten/status/2047779549644243146), [@NousResearch](https://x.com/mr_r0b0t/status/2047673600900010044), [@Teknium](https://x.com/Teknium/status/2047798102091067677)
    * **V4 Pro pricing:** **$1.74 / $3.48 per 1M input/output tokens**
    * **V4 Flash pricing:** **$0.14 / $0.28**
    * cache-hit pricing also given by [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2047735160544841953)
    * [@scaling01](https://x.com/scaling01/status/2047707820552831028) views the pricing as a glimpse of future “Mythos-level” cheap coding models
    * Reuters-via-posted quote from [@scaling01](https://x.com/scaling01/status/2047760776769720360): DeepSeek said **Pro pricing could fall sharply once Huawei Ascend 950 supernodes are deployed at scale in H2**



## Independent evaluations and where V4 lands

The most useful independent benchmark synthesis came from [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2047735160544841953):

  * **V4 Pro Max** : **52** on Artificial Analysis Intelligence Index 
    * up **10 points** from **V3.2 at 42**
    * becomes **#2 open weights reasoning model** , behind **Kimi K2.6 (54)**
  * **V4 Flash Max** : **47**
    * positioned around strong mid/high open models, “Claude Sonnet 4.6 max level intelligence”
  * **GDPval-AA** (agentic real-world work): 
    * **V4 Pro: 1554** , leading open-weight models
    * ahead of **Kimi K2.6 (1484)** , **GLM-5.1 (1535)** , **MiniMax-M2.7 (1514)**
  * **AA-Omniscience**
    * **V4 Pro: -10** , an 11-point improvement over V3.2
    * but still paired with **94% hallucination rate**
    * **V4 Flash: 96% hallucination rate**
  * **Cost to run AA Index**
    * **V4 Pro: $1,071**
    * **V4 Flash: $113**
  * **Output tokens used on AA Index**
    * **V4 Pro: 190M**
    * **V4 Flash: 240M**
    * This is a major caveat: cheap per-token pricing does not imply cheap total task cost if the model spills huge token volumes



Additional eval perspectives:

  * [@arena](https://x.com/arena/status/2047714237502677405): 
    * **#2 open** in Text Arena overall at debut
    * category wins/placements: 
      * **#1 Medical & Healthcare**
      * **#15 Creative Writing**
      * **#18 Multi-Turn**
    * thinking variant: 
      * **#8 Math**
      * **#9 Life/Physical/Social Science**
  * [@arena](https://x.com/arena/status/2047774037204742255) emphasizes the **Pro vs Flash tradeoff** : 
    * Pro ranks ~**30 places higher**
    * costs **12× more**
    * Flash is still competitive in Chinese, medicine, math
  * [@scaling01](https://x.com/scaling01/status/2047682465624445015): 
    * “~**Opus 4.5 estimate** holds for now, at least on SimpleBench”
  * [@scaling01](https://x.com/scaling01/status/2047733998714052819): 
    * V4 is “definitely better than GLM-5.1 but not quite Opus 4.7, GPT-5.4 or Gemini 3.1 Pro”
  * [@scaling01](https://x.com/scaling01/status/2047686712051048598) lists what scores would confirm <6 month gap: 
    * ARC-AGI-1 ~**75%**
    * ARC-AGI-2 ~**35%**
    * GSO ~**26%**
    * METR **4.5–5 hours**
    * WeirdML ~**63%**
  * [@TheZachMueller](https://x.com/TheZachMueller/status/2047719857869791352): 
    * on his evals, **Flash@max ≈ Pro@high on reasoning**
    * Pro focuses more on knowledge (SimpleQA)
  * [@VictorTaelin](https://x.com/VictorTaelin/status/2047818978664268071): 
    * after fixing benchmark bugs and letting long-running models run longer, **DeepSeek and Kimi improved materially**
  * [@mbusigin](https://x.com/mbusigin/status/2047707082007220393): 
    * a simple negative early impression with no detail
  * [@petergostev](https://x.com/petergostev/status/2047773402090426548): 
    * on BullshitBench, not about capability but refusal/pushback behavior, GPT-5.5 underperformed; included here because many readers compare V4 in an eval-skeptical environment



## Facts vs opinions

### Facts / relatively well-supported claims

  * V4 Pro / Flash were released with the specs above, **MIT-licensed** , **1M context** , and open technical documentation: [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2047735160544841953), [@TheZachMueller](https://x.com/TheZachMueller/status/2047626252425515240)
  * The architecture introduces a new long-context attention system with dramatic KV-cache reduction: [@ZhihuFrontier](https://x.com/ZhihuFrontier/status/2047664976215839021), [@ben_burtenshaw](https://x.com/ben_burtenshaw/status/2047646980139016560)
  * Independent benchmarkers broadly place V4 Pro near the very top of open weights but below the best proprietary models overall: [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2047735160544841953), [@arena](https://x.com/arena/status/2047714237502677405), [@scaling01](https://x.com/scaling01/status/2047733998714052819)
  * DeepSeek V4 is heavily token-intensive in some evaluations: [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2047735160544841953)
  * The checkpoint uses FP4/FP8 mixed precision and can fit on an 8×B200 node: [@LambdaAPI](https://x.com/LambdaAPI/status/2047654086263320965)
  * Rapid ecosystem support arrived via vLLM and other providers day 0: [@vllm_project](https://x.com/vllm_project/status/2047843293447500069), [@SemiAnalysis_](https://x.com/SemiAnalysis_/status/2047726025748930687)



### Opinions / interpretation

  * “V4 is ~4–5 months behind the frontier” from [@scaling01](https://x.com/scaling01/status/2047618271310926151), [@scaling01](https://x.com/scaling01/status/2047622501241434581), [@scaling01](https://x.com/scaling01/status/2047626000091971811) is an informed estimate, not a measured fact
  * “Top three open” vs “only open model close to frontier” debate from [@teortaxesTex](https://x.com/teortaxesTex/status/2047616662879248828) is partly about benchmark trust and framing
  * “Strongest pretrained model we have” from [@teortaxesTex](https://x.com/teortaxesTex/status/2047630981364883816) is an opinion hinging on scale + architecture, not direct benchmark supremacy
  * “Most significant AI paper of the year” from [@Dorialexander](https://x.com/Dorialexander/status/2047632551326413109) is enthusiasm, not consensus
  * “This is what research should look like” from [@scaling01](https://x.com/scaling01/status/2047643722108579936) speaks to transparency/style rather than only capability
  * “Not exactly a democratizing technology” from [@teortaxesTex](https://x.com/teortaxesTex/status/2047840426371977467) is a strong architectural/political interpretation



## Different opinions and fault lines

### 1) Is V4 near frontier, or clearly behind?

**More favorable**

  * [@scaling01](https://x.com/scaling01/status/2047618271310926151): puts it at roughly **GPT-5.2 / Opus 4.5+ tier**
  * [@scaling01](https://x.com/scaling01/status/2047682465624445015): SimpleBench supports **~Opus 4.5**
  * [@teortaxesTex](https://x.com/teortaxesTex/status/2047630981364883816): argues it is the strongest pretraining base among opens and implies people are underestimating what post-training can do



**More skeptical**

  * [@scaling01](https://x.com/scaling01/status/2047733998714052819): below **Opus 4.7 / GPT-5.4 / Gemini 3.1 Pro**
  * [@scaling01](https://x.com/scaling01/status/2047622501241434581): the gap may widen again because closed labs have bigger models, better science/law/medicine coverage, faster inference with GB200s
  * [@mbusigin](https://x.com/mbusigin/status/2047707082007220393): early impressions “not great”
  * [@teortaxesTex](https://x.com/teortaxesTex/status/2047616897256947967): says polished models like **K2.6 and GLM 5.1** may still feel better in coding despite lower intrinsic capacity



### 2) Is V4’s real contribution model quality, or long-context systems design?

A big split in reactions is that many technical readers think **the long-context architecture matters more than the raw benchmark position**.

  * [@teortaxesTex](https://x.com/teortaxesTex/status/2047623905754448043): “They've completed their quest: Solid Ultra-Long Context”
  * [@ben_burtenshaw](https://x.com/ben_burtenshaw/status/2047646980139016560): first open model where long context and agentic post-training “meet”
  * [@scaling01](https://x.com/scaling01/status/2047618271310926151): expects other open labs to adopt pieces of the architecture
  * [@Dorialexander](https://x.com/Dorialexander/status/2047632551326413109): frames Huawei/sovereignty constraints as an opportunity to reshape hardware and memory/interconnect design
  * [@jukan05](https://x.com/jukan05/status/2047861732702662741): reads the paper as evidence that NVIDIA’s hardware roadmap is unusually well aligned to where MoE/long-context models are going



### 3) Is V4 “open democratization,” or too hard to copy?

This was one of the sharpest strategic disagreements.

  * [@teortaxesTex](https://x.com/teortaxesTex/status/2047840426371977467): says V4 is “not exactly a democratizing technology” because the architecture is too difficult for most labs to replicate
  * [@teortaxesTex](https://x.com/teortaxesTex/status/2047648219081974034): suggests even DeepSeek may not want to do this exact architecture again without refactoring
  * [@stochasticchasm](https://x.com/stochasticchasm/status/2047697372831183245): notes the sheer hyperparameter complexity is daunting
  * Against that, [@Prince_Canuma](https://x.com/Prince_Canuma/status/2047685898163147125) and [@Prince_Canuma](https://x.com/Prince_Canuma/status/2047847095466385899) show that the ecosystem is already compressing and adapting Flash for localish Apple Silicon use, softening the “not democratizing” claim on the inference side if not the training side



### 4) Are people underrating Flash?

Several reactions suggest **Flash may be more important than Pro** for practical adoption.

  * [@arena](https://x.com/arena/status/2047774037204742255): Flash shifts the price/performance frontier
  * [@TheZachMueller](https://x.com/TheZachMueller/status/2047719857869791352): Flash@max ≈ Pro@high on reasoning tasks
  * [@teortaxesTex](https://x.com/teortaxesTex/status/2047864952862458009): benchmarks may underweight “legit 1M context for pennies”
  * [@Prince_Canuma](https://x.com/Prince_Canuma/status/2047685898163147125): Flash runs on **256GB Mac**
  * [@baseten](https://x.com/baseten/status/2047779549644243146) and [@Togethercompute](https://x.com/togethercompute/status/2047743446522224987) emphasize long-document analysis and agentic use cases where Flash’s economics matter



## China, chips, Huawei, and sovereignty context

DeepSeek V4 was not discussed as a pure model release; it was treated as evidence in the larger US–China compute and sovereignty debate.

  * [@scaling01](https://x.com/scaling01/status/2047625331339661685): Chinese labs are already in or near “takeoff” in the sense that their models help build better models, though still shifted **5+ months** behind
  * [@scaling01](https://x.com/scaling01/status/2047622501241434581): thinks chip bans are likely to widen the gap in broad domains over time
  * [@teortaxesTex](https://x.com/teortaxesTex/status/2047608887616962992), [@teortaxesTex](https://x.com/teortaxesTex/status/2047631470664020211): disputes simplistic Huawei-dismissal and notes mixed Chinese sentiment toward Huawei
  * [@ogawa_tter](https://x.com/ogawa_tter/status/2047631993702363509): points to analysis of **Ascend 950** / A3 clusters and V4 deployment plans
  * [@Dorialexander](https://x.com/Dorialexander/status/2047632551326413109): argues the sovereignty play around Huawei may reshape hardware architecture
  * [@scaling01](https://x.com/scaling01/status/2047760776769720360): cites DeepSeek saying prices could drop sharply once **Ascend 950 supernodes** scale in H2
  * [@jukan05](https://x.com/jukan05/status/2047861732702662741): interprets V4 as validating NVIDIA’s Blackwell/Rubin/HBM/interconnect strategy
  * [@NVIDIAAI](https://x.com/NVIDIAAI/status/2047765637808664759), [@NVIDIAAI](https://x.com/NVIDIAAI/status/2047823093578518758): unsurprisingly highlight Blackwell day-0 performance, but this is vendor framing rather than independent proof of strategic superiority



There is also a more ideological thread:

  * [@teortaxesTex](https://x.com/teortaxesTex/status/2047645676234846459), [@teortaxesTex](https://x.com/teortaxesTex/status/2047638436295725080), [@teortaxesTex](https://x.com/teortaxesTex/status/2047835420755415472) argues that Western discourse often misreads Chinese labs as purely state proxies or distillation shops, and instead sees them as serious mission-driven actors. This is interpretive, but it helps explain why the release drew such emotionally charged geopolitical reactions.



## Distillation, training data, and data quality

A recurring undercurrent: does V4 mainly reflect architectural innovation, or can critics dismiss it as “distillation”?

  * [@yacineMTB](https://x.com/yacineMTB/status/2047628416514486661) speculates that some complaints about Chinese distillation may partly come from people discovering they’re outperformed
  * [@cloneofsimo](https://x.com/cloneofsimo/status/2047628636933812301): “Very interesting... given they distilled claude 🤔🤔”
  * [@kalomaze](https://x.com/kalomaze/status/2047762970931827125): jokes about DeepSeek training on DeepSeek reasoning traces
  * On the more substantive side, [@teortaxesTex](https://x.com/teortaxesTex/status/2047614729145745623) says DeepSeek’s writing quality, especially Chinese, reflects long-standing obsession with data cleanliness and cites job listings [@teortaxesTex](https://x.com/teortaxesTex/status/2047614852055683103), [@teortaxesTex](https://x.com/teortaxesTex/status/2047614975447855485)
  * [@nrehiew_](https://x.com/nrehiew_/status/2047666048334450754) notes the report still lacks much detail on pretraining data beyond standard categories
  * Overall, factual public evidence in this tweet set supports “DeepSeek trains at large scale with strong data work,” but not any strong claim about the degree of external distillation beyond speculation



## Architecture lineage and prior art

Several researchers pointed out that V4 did not emerge from nowhere.

  * [@jaseweston](https://x.com/jaseweston/status/2047690308217926055): says DeepSeek uses **hash routing** from a 2021 ParlAI approach
  * [@suchenzang](https://x.com/suchenzang/status/2047772636881842629): criticizes routing-induced outliers, with a jab at hashing
  * [@teortaxesTex](https://x.com/teortaxesTex/status/2047844368883581404): notes Mixtral-style MoE was a reasonable earlier hack, but claims **DSMoE** changed things
  * [@art_zucker](https://x.com/art_zucker/status/2047619111082172548) broadly attacks MoEs as a dead end
  * [@gabriberton](https://x.com/gabriberton/status/2047835467551547587) counters that MoEs are provably effective despite inelegance
  * [@stochasticchasm](https://x.com/stochasticchasm/status/2047874903236645108) is even more positive: “MoEs are amazing”



This matters because V4 was read not just as a stronger checkpoint, but as a possible **new design point for open long-context MoEs**.

## Why the technical report itself mattered

A striking amount of praise was directed not just at the model but at the paper/report quality.

  * [@scaling01](https://x.com/scaling01/status/2047618271310926151): “the technical paper is a big deal”
  * [@Dorialexander](https://x.com/Dorialexander/status/2047632551326413109): “most significant AI paper of the year”
  * [@morqon](https://x.com/morqon/status/2047643246923325833): “one of the best I’ve ever read”
  * [@scaling01](https://x.com/scaling01/status/2047643722108579936): “this is what research should look like”
  * [@TheZachMueller](https://x.com/TheZachMueller/status/2047626249116303561), [@iamgrigorev](https://x.com/iamgrigorev/status/2047641600591794546), [@nrehiew_](https://x.com/nrehiew_/status/2047665987730993363): all signal unusually high effort to digest and test the report



For expert readers, this is important because many frontier releases now arrive with sparse technical disclosure. V4’s report appears to have reset expectations for what a serious open release can look like.

## Practical limitations and caveats

Despite the enthusiasm, several caveats recur:

  * **Still behind closed frontier in aggregate capability**
    * especially sciences/law/medicine and broad “general domains” per [@scaling01](https://x.com/scaling01/status/2047622501241434581)
  * **Reasoning RL may be undercooked**
    * [@scaling01](https://x.com/scaling01/status/2047618271310926151): reasoning efficiency not much changed vs V3.2 Speciale
  * **Serving remains hard**
    * [@scaling01](https://x.com/scaling01/status/2047643015859118167): many labs serve at only **20–30 tok/s** and limited concurrency; running evals can take a day
    * [@ClementDelangue](https://x.com/ClementDelangue/status/2047664153439989823): acknowledges concurrency bottlenecks on HF
  * **High token usage**
    * major practical caveat from [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2047735160544841953)
  * **API controls**
    * [@stochasticchasm](https://x.com/stochasticchasm/status/2047717161070989499): notes DeepSeek API appears not to allow sampler control
  * **Adoptability**
    * [@teortaxesTex](https://x.com/teortaxesTex/status/2047840426371977467): too complex for many labs to copy cleanly



## Broader implications

Three implications stand out.

  1. **Open-weight long-context is no longer just marketing.**  
V4’s strongest contribution may be proving that **1M context can be made operationally credible** in an open-weight model, with concrete KV-cache engineering and open inference support. This is why multiple posters focused less on benchmark deltas and more on systems design: [@ben_burtenshaw](https://x.com/ben_burtenshaw/status/2047646980139016560), [@ZhihuFrontier](https://x.com/ZhihuFrontier/status/2047664976215839021), [@scaling01](https://x.com/scaling01/status/2047618271310926151).

  2. **China’s top labs remain competitive in open models, even if not fully closing the closed-model gap.**  
The benchmark picture across [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2047735160544841953), [@arena](https://x.com/arena/status/2047714237502677405), and [@scaling01](https://x.com/scaling01/status/2047733998714052819) suggests Chinese labs now dominate much of the open-weight top tier: **Kimi, GLM, DeepSeek, and soon MiMo**.

  3. **The bar for “open” is rising from checkpoint release to full-stack co-design.**  
V4 was instantly discussed alongside **vLLM** , **Blackwell** , **MLX quants** , **Mac viability** , **Ascend clusters** , and cache/memory architectures. In other words, “the model” is increasingly inseparable from the inference substrate.




* * *

**Infrastructure, inference, and local/open ecosystem**

  * Hugging Face launched **ML Intern** , an open-source CLI “AI intern” for ML work that can research papers, write code, run experiments, use HF datasets/jobs, search GitHub, and iterate up to **300 steps** , per [@MillieMarconnni](https://x.com/MillieMarconnni/status/2047639632859500691). Related sentiment: HF’s **$9 Pro** tier is unusually strong value per [@getpy](https://x.com/getpy/status/2047602009998794820).
  * Meta said it will add **tens of millions of AWS Graviton cores** to its compute portfolio to scale Meta AI and agentic systems for billions of users, per [@AIatMeta](https://x.com/AIatMeta/status/2047647617681957207).
  * Local/open coding stack momentum stayed strong: 
    * [@julien_c](https://x.com/julien_c/status/2047647522173104145): **Qwen3.6-27B via llama.cpp on a MacBook Pro** feels close to latest Opus for many coding tasks
    * [@p0](https://x.com/p0/status/2047794814104862843): free CLI agent built with **Pi + Ollama + Gemma 4 + Parallel web search MCP**
    * [@Prince_Canuma](https://x.com/Prince_Canuma/status/2047693737950670940): DeepSeek V4 quants incoming
    * [@QuixiAI](https://x.com/QuixiAI/status/2047765475937890474): reminder that **llama.cpp / Ollama / LM Studio do not support tensor parallel** , pushing serious multi-GPU serving users toward **vLLM**
  * Nous/Hermes shipped heavily: 
    * Hermes Agent **v0.11.0** introduced a rewritten React TUI, dashboard plugin, theming, more inference providers, image backends, and QQBot support, per [@WesRoth](https://x.com/WesRoth/status/2047646749427216385)
    * Hermes got broad praise and rapid support for both **DeepSeek V4** and **GPT-5.5** , via [@mr_r0b0t](https://x.com/mr_r0b0t/status/2047673600900010044), [@Teknium](https://x.com/Teknium/status/2047791512210293067)
    * [@JulianGoldieSEO](https://x.com/JulianGoldieSEO/status/2047699587788361844) and [@LoicBerthelot](https://x.com/LoicBerthelot/status/2047690512199540959) compared Hermes favorably to OpenClaw on learning loops, memory, model support, deployment flexibility, and security
    * A native Linux sandbox backend for Deep Agents using **bubblewrap + cgroups v2** was released by [@nu_b_kh](https://x.com/nu_b_kh/status/2047775326412136574)



**Research papers and benchmarks**

  * On-policy distillation token selection: 
    * [@TheTuringPost](https://x.com/TheTuringPost/status/2047617791709282405) highlights a paper showing only some tokens carry most learning signal; using **~50%** of tokens can match or beat full training and cut memory by **~47%** , while even **< 10%** focused on confident-wrong tokens nearly matches full training.
  * Google Research pushed several ICLR demos: 
    * **MesaNet** , a transformer alternative / linear sequence layer optimized for in-context learning under fixed memory, via [@GoogleResearch](https://x.com/GoogleResearch/status/2047630714145776053)
    * robotics/3D reasoning and efficient transformer work via [@GoogleResearch](https://x.com/GoogleResearch/status/2047675181808730197)
    * “reasoning can lead to honesty” demo via [@GoogleResearch](https://x.com/GoogleResearch/status/2047704802163892576)
  * MIT **Hyperloop Transformers** mix looped and normal transformer blocks, using ~**50% fewer parameters** while beating regular transformers at **240M / 1B / 2B** , per [@TheTuringPost](https://x.com/TheTuringPost/status/2047720038342476187).
  * “Learning mechanics” tries to synthesize a theory of deep learning dynamics, via [@learning_mech](https://x.com/learning_mech/status/2047723849874330047).
  * Tool/agent systems papers: 
    * **Tool Attention Is All You Need** claims **95% tool-token reduction** (47.3k → 2.4k/turn) with dynamic gating and lazy schema loading, per [@omarsar0](https://x.com/omarsar0/status/2047725276851994639)
    * **StructMem** for long-horizon structured memory highlighted by [@dair_ai](https://x.com/dair_ai/status/2047740873027543228)
    * **HorizonBench** targets long-horizon personalization with shifting user preferences, via [@StellaLisy](https://x.com/StellaLisy/status/2047645651324821998)
  * Clarifying questions for software engineering: 
    * [@gneubig](https://x.com/gneubig/status/2047623214583492797) shared work on a model trained specifically to ask clarifying questions, improving results with fewer questions.



**GPT-5.5 rollout and coding agents**

  * OpenAI rolled **GPT-5.5** and **GPT-5.5 Pro** into API and ecosystem products with a **1M context window** , per [@OpenAI](https://x.com/OpenAI/status/2047743592278745425), [@OpenAIDevs](https://x.com/OpenAIDevs/status/2047742589982654915).
  * Distribution was immediate across Cursor, GitHub Copilot, Codex/OpenAI API, OpenRouter, Perplexity, Devin, Droid, Fleet, Deep Agents: 
    * [@cursor_ai](https://x.com/cursor_ai/status/2047744579127185843): GPT-5.5 is top on **CursorBench at 72.8%**
    * [@cline](https://x.com/cline/status/2047769312514257148): **#1 on Terminal-Bench at 82.7**
    * [@OpenAIDevs](https://x.com/OpenAIDevs/status/2047772632150675593): Perplexity Computer saw **56% fewer tokens** on complex tasks
    * [@scaling01](https://x.com/scaling01/status/2047818395970904229): GPT-5.5 medium became strongest non-thinking model on LisanBench with **45.6% fewer tokens than GPT-5.4 medium** and higher scores
  * User feedback clustered around **better coding quality and token efficiency** , despite mixed feelings about some evals: 
    * [@almmaasoglu](https://x.com/almmaasoglu/status/2047745168141324559): best code they’ve read from an LLM; less verbose, less defensive
    * [@KentonVarda](https://x.com/KentonVarda/status/2047788670728495142): caught a deep Cap’n Proto RPC corner case from a 6-year-old comment
    * [@willdepue](https://x.com/willdepue/status/2047783399826292969): underwhelmed by evals, impressed in Codex on complex technical projects
    * [@omarsar0](https://x.com/omarsar0/status/2047768166126809512): smooth switch from Claude Code to Codex/GPT-5.5 thanks to better “effort calibration”
  * Cursor also shipped **/multitask** async subagents and multi-root workspaces, via [@cursor_ai](https://x.com/cursor_ai/status/2047764651363180839).
  * There is growing market emphasis on **limits and economics** rather than tiny quality gaps: 
    * [@nrehiew_](https://x.com/nrehiew_/status/2047839351380537357) argues usage caps now matter more than small frontier deltas
    * [@HamelHusain](https://x.com/HamelHusain/status/2047763070022479882) says Codex’s subscription structure makes it hard not to use



**Industry moves, funding, and policy**

  * Google reportedly plans to invest up to **$40B in Anthropic** , reported by [@FT](https://x.com/FT/status/2047715653553942997) and echoed by [@zerohedge](https://x.com/zerohedge/status/2047704883982180609). Reactions centered on how large Anthropic’s compute commitment may now be.
  * Cohere and Aleph Alpha announced a **Canada/Germany sovereign AI partnership** , framed as enterprise-grade and privacy/security focused by [@cohere](https://x.com/cohere/status/2047631725426000268), [@aidangomez](https://x.com/aidangomez/status/2047651054381052086), [@nickfrosst](https://x.com/nickfrosst/status/2047704679878996253#m).
  * ComfyUI raised **$30M at a $500M valuation** , while keeping core/open-local positioning, via [@yoland_yan](https://x.com/yoland_yan/status/2047731043000627263).
  * Mechanize announced **$9.1M** raised at a **$500M post-money valuation** , via [@MechanizeWork](https://x.com/MechanizeWork/status/2047732999878529037).
  * Arcee AI hired Cody Blakeney as Head of Research, emphasizing open-weight American frontier models, via [@code_star](https://x.com/code_star/status/2047765768658702467).
  * Safety / governance: 
    * OpenAI announced a **Bio Bug Bounty** for GPT-5.5, per [@OpenAINewsroom](https://x.com/OpenAINewsroom/status/2047670970526175310)
    * Anthropic launched **Project Deal** , a marketplace where Claude negotiated on behalf of employees, and highlighted model-quality asymmetry and policy challenges, via [@AnthropicAI](https://x.com/AnthropicAI/status/2047728360818696302)



**Creative AI and multimodal**

  * GPT Image 2 + Seedance 2 workflows kept drawing attention: 
    * [@_OAK200](https://x.com/_OAK200/status/2047616640448078167) and [@awesome_visuals](https://x.com/awesome_visuals/status/2047609881104953658) showed high-fidelity image→video pipelines
    * [@BoyuanChen0](https://x.com/BoyuanChen0/status/2047738501647728937) said **2K/4K** images are already available via experimental API and active fixes are underway
  * Kling announced native **4K output** and a **$25k** short film contest, via [@Kling_ai](https://x.com/Kling_ai/status/2047676942317678879).
  * Some evaluative nuance: 
    * [@goodside](https://x.com/goodside/status/2047728776520298646) noted GPT Images 2.0 could render a valid-looking Rubik’s Cube state, which is surprisingly hard
    * [@venturetwins](https://x.com/venturetwins/status/2047820435543437630) framed recent image/video gains as a major step toward personalized game-like content generation



* * *

# AI Reddit Recap

## /r/LocalLlama + /r/localLLM Recap

### 1\. Deepseek V4 and Related Releases

  * **[Deepseek V4 AGI comfirmed](https://www.reddit.com/r/LocalLLaMA/comments/1suolda/deepseek_v4_agi_comfirmed/)** (Activity: 1138): **The image is a meme and does not contain any technical content. The title "Deepseek V4 AGI confirmed" suggests a humorous or exaggerated claim about an AI model, possibly referencing advancements in artificial general intelligence (AGI). The comments further imply a satirical tone, mentioning uncensored datasets and military applications, which are likely not serious claims.** The comments reflect a satirical take on AI capabilities, with mentions of uncensored datasets and military applications, indicating skepticism or humor rather than a serious technical discussion.

    * UserXtheUnknown discusses a test scenario with Deepseek V4, highlighting its tendency to overthink problems. The model interprets constraints like 'using only one knife' as mandatory rather than optional, which affects its problem-solving approach. This reflects a nuanced understanding of task constraints, but also indicates potential areas for improvement in handling implicit instructions.
  * **[Deepseek V4 Flash and Non-Flash Out on HuggingFace](https://www.reddit.com/r/LocalLLaMA/comments/1su3hdo/deepseek_v4_flash_and_nonflash_out_on_huggingface/)** (Activity: 1393): ****DeepSeek V4** has been released on [HuggingFace](https://huggingface.co/collections/deepseek-ai/deepseek-v4), featuring two models: **DeepSeek-V4-Pro** with `1.6T parameters` (of which `49B` are activated) and **DeepSeek-V4-Flash** with `284B parameters` (with `13B` activated). Both models support a context length of `one million tokens`, which is significant for handling extensive sequences. The models are released under the **MIT license** , allowing for broad use and modification.** A notable comment highlights the challenge of hardware limitations, particularly RAM, when working with such large models. Another comment suggests the potential benefit of a `0.01bit quantization` to manage the model size more effectively.

    * The DeepSeek-V4 models are notable for their massive parameter sizes, with the Pro version having 1.6 trillion parameters (49 billion activated) and the Flash version having 284 billion parameters (13 billion activated). Both models support an extensive context length of one million tokens, which is significant for handling large-scale data inputs and complex tasks.
    * A user expressed interest in a 0.01-bit quantization of the DeepSeek-V4 models, which suggests a focus on reducing the model size and computational requirements while maintaining performance. Quantization is a common technique to optimize models for deployment on hardware with limited resources.
    * The mention of the MIT license indicates that DeepSeek-V4 is open-source, allowing for broad use and modification by the community. This licensing choice can facilitate collaboration and innovation, as developers can freely integrate and adapt the models into their own projects.
  * **[Buried lede: Deepseek v4 Flash is incredibly inexpensive from the official API for its weight category](https://www.reddit.com/r/LocalLLaMA/comments/1su5gj5/buried_lede_deepseek_v4_flash_is_incredibly/)** (Activity: 404): **The image provides a comparison between two models, "deepseek-v4-flash" and "deepseek-v4-pro," highlighting that the "deepseek-v4-flash" model is significantly more affordable in terms of input and output token costs. Despite its affordability, the model supports advanced features like JSON output, tool calls, and chat prefix completion in both non-thinking and thinking modes. The discussion around the image suggests that while the "deepseek-v4-flash" is marketed as inexpensive, some users argue that it is actually overpriced compared to previous versions when considering parameter scaling, with the "V3.2" model being cheaper per parameter.** Commenters discuss the impact of GPU shortages on current pricing, suggesting that prices may decrease as GPU production increases. There is also debate about the pricing strategy, with some users noting that the new model is more expensive per parameter compared to older versions.

    * DistanceSolar1449 highlights a pricing comparison between DeepSeek V3.2 and V4 Flash, noting that V3.2 was priced at `$0.26/0.38` for input/output at `671b`, whereas V4 Flash is `$0.14/$0.28` at `284b`. This suggests that V4 Flash is actually more expensive if pricing were to scale linearly with parameters, challenging the notion of its cost-effectiveness.
    * jwpbe provides a comparative analysis of DeepSeek V4 Flash's API cost, stating that at `14 cents in / 28 cents out`, it is significantly cheaper than competitors like Minimax 2.7, which is `3x` the cost, and Qwen's equivalent, which is even higher. They also mention that Trinity Thinking Large is twice as expensive, indicating that V4 Flash offers a competitive pricing advantage in the market.
    * Worried-Squirrel2023 discusses the strategic implications of Huawei's silicon developments, suggesting that DeepSeek's pricing strategy involves trading NVIDIA margins for Ascend supply. They predict that once the `950 supernodes` scale, DeepSeek could potentially undercut competitors in the open weights tier, leveraging Huawei's advancements to optimize costs.
  * **[Deepseek has released DeepEP V2 and TileKernels.](https://www.reddit.com/r/LocalLLaMA/comments/1ste9zs/deepseek_has_released_deepep_v2_and_tilekernels/)** (Activity: 396): ****Deepseek** has released **DeepEP V2** and **TileKernels** , which are significant advancements in AI model optimization and parallelization. **DeepEP V2** focuses on enhancing model efficiency and accuracy, while **TileKernels** introduces a novel parallelization technique that reportedly scales linearly, meaning that doubling computational capacity results in a doubling of processing speed. This release is open-sourced, fostering transparency and collaboration in AI research. For more details, see the [DeepEP V2 pull request](https://github.com/deepseek-ai/DeepEP/pull/605) and the [TileKernels repository](https://github.com/deepseek-ai/TileKernels).** One commenter highlights that **Deepseek** is fulfilling a role that **OpenAI** was expected to play by advancing research and sharing findings openly, which builds goodwill despite proprietary technologies. Another commenter questions if the parallelization technique indeed scales linearly, suggesting a significant technical breakthrough if true.

    * **DeepEP V2 and TileKernels** by DeepSeek are noted for their potential advancements in parallelization techniques. A user speculates that these techniques might achieve linear scaling, meaning that doubling computational capacity could directly double processing speed. This could represent a significant efficiency improvement in model training and inference.
    * There is speculation about DeepSeek's hardware usage, particularly regarding the SM100 and Blackwell GPUs. One commenter suggests that DeepSeek might be using Blackwell GPUs for training, possibly through rented B200 units on Vast.ai. This hardware choice could influence the performance and capabilities of their models.
    * The potential innovations in DeepSeek's next model, possibly named v4, are highlighted. The focus is on the integration of Engram and mHC technologies, which are expected to play a crucial role in the model's performance. The success of these innovations will likely depend on the new dataset DeepSeek has developed.



### 2\. Qwen 3.6 Model Performance and Benchmarks

  * **[This is where we are right now, LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/comments/1suqfba/this_is_where_we_are_right_now_localllama/)** (Activity: 1755): **The image depicts a MacBook Pro running a Qwen3.6 27B model via Llama.cpp, showcasing the capability of executing complex AI models locally, even in airplane mode. This highlights the potential for local AI models to enhance efficiency, security, privacy, and sovereignty by operating independently of cloud services. The post underscores the technological advancement in making powerful AI models accessible on personal devices, emphasizing the importance of local execution for privacy and control.** Commenters express skepticism about the overstatement of the Qwen3.6-27B model's capabilities, suggesting that while it is impressive for its size, it does not match the performance of more advanced models like Sonnet or Opus. There is concern that exaggerated claims could lead to user disappointment and backlash against the broader LLM community.

    * **ttkciar** highlights the potential for user disappointment with the Qwen3.6-27B model, noting that while it's impressive for its size and suitable for agentic code generation, it doesn't match the capabilities of more advanced models like Sonnet or Opus. The concern is that overhyping its abilities could lead to backlash against the broader LLM community, not just the individual making the claims.
    * **sooki10** agrees that while the model is impressive for local coding tasks, comparing it to more advanced models like Opus is misleading and could undermine the credibility of the claims being made. This suggests a need for more accurate benchmarking and communication about the model's capabilities to manage user expectations effectively.
    * **Melodic_Reality_646** points out the disparity in resources, comparing the use of a high-end 128GB RAM m5max system to a more accessible setup. This highlights the importance of considering hardware limitations when evaluating model performance, as not all users have access to such powerful systems, which can skew perceptions of a model's capabilities.
  * **[DS4-Flash vs Qwen3.6](https://www.reddit.com/r/LocalLLaMA/comments/1sub71w/ds4flash_vs_qwen36/)** (Activity: 470): **The image presents a benchmark comparison between**DS4-Flash Max** and **Qwen3.6** models, specifically the `35B-A3B` and `27B` versions. The chart highlights that **DS4-Flash Max** generally outperforms the Qwen models across various categories, particularly excelling in 'LiveCodeBench' and 'HLE' benchmarks. This suggests that DS4-Flash Max may have superior capabilities in coding and reasoning tasks. The discussion in the comments hints at the potential for larger models like a `122B` version of Qwen3.6, and emphasizes the significance of the `1M token context` feature, which could impact performance in other benchmarks like 'omniscense'.** Commenters note that despite DS4-Flash Max's larger size, its performance is only slightly better than Qwen3.6, raising questions about efficiency versus scale. The `1M token context` is highlighted as a significant feature that could influence future benchmark results.

    * **Rascazzione** highlights the significant increase in context length with Qwen 3.6, noting its ability to handle a 1 million token context. This is a substantial improvement over previous models and could have significant implications for tasks requiring extensive context handling, such as document summarization or complex dialogue systems.
    * **LinkSea8324** points out the size difference between the models, with DS4-Flash at 284 billion parameters compared to Qwen 3.6's 27 billion. This raises questions about the efficiency and performance trade-offs between model size and capability, especially in terms of computational resources and inference speed.
    * **madsheepPL** discusses the non-linear nature of benchmark improvements, suggesting that even if a model appears only slightly better in benchmarks, the practical implications can be more significant. They emphasize that improvements in scores are not directly proportional and can have varying impacts on real-world applications.
  * **[Qwen 3.6 27B Makes Huge Gains in Agency on Artificial Analysis - Ties with Sonnet 4.6](https://www.reddit.com/r/LocalLLaMA/comments/1strodp/qwen_36_27b_makes_huge_gains_in_agency_on/)** (Activity: 964): ****Qwen 3.6 27B** has achieved parity with **Sonnet 4.6** on the **Agentic Index** from Artificial Analysis, surpassing models like **Gemini 3.1 Pro Preview** , **GPT 5.2 and 5.3** , and **MiniMax 2.7**. The model shows improvements across all indices, although the gains in the **Coding Index** are less pronounced due to its reliance on benchmarks like **Terminal Bench Hard** and **SciCode** , which are considered unconventional. The focus of training appears to be on agentic applications for **OpenClaw/Hermes** , highlighting the potential of smaller models to approach frontier capabilities. Anticipation is building for the upcoming **Qwen 3.6 122B** model.** Commenters express excitement about the potential of smaller models like Qwen 3.6 27B, noting the significant improvements and potential for future versions. However, there is skepticism about the extent of these gains, suggesting that some improvements might be due to 'benchmaxxing' rather than inherent model capabilities.

    * Iory1998 highlights the impressive performance of the Qwen 3.6 27B model, noting that it surpasses a 670B model from the previous year. They mention running the Q8 version at 170K with KV cache at FP16 on an RTX 3090 and RTX 5070ti, utilizing 40GB of VRAM, which underscores the model's efficiency and power.
    * AngeloKappos discusses the narrowing benchmark gap, sharing their experience running the Qwen3-30b-a3b model on an M2 chip. They note its capability to handle multi-step tool calls effectively, suggesting that if the 27B dense model performs this well, the upcoming 122B model could pose challenges for API providers due to its potential performance.
    * Velocita84 raises a point about potential "benchmaxxing" in the reported performance gains of the Qwen 3.6 27B model, implying that some of the improvements might be attributed to optimized benchmarking rather than inherent model capabilities. This suggests a need for scrutiny in evaluating model performance claims.
  * **[Compared QWEN 3.6 35B with QWEN 3.6 27B for coding primitives](https://www.reddit.com/r/LocalLLaMA/comments/1styxdy/compared_qwen_36_35b_with_qwen_36_27b_for_coding/)** (Activity: 491): **The post compares two versions of the**QWEN 3.6** model, specifically the `35B` and `27B` parameter versions, on a MacBook Pro M5 MAX with `64GB` RAM. The `35B` model achieves `72 TPS` (tokens per second), while the `27B` model achieves `18 TPS`. Despite the slower speed, the `27B` model produces more precise and correct results for coding tasks, whereas the `35B` model is faster but less accurate. The test involved generating a single HTML file to simulate a moving car with a parallax effect, using no external libraries. The models were hosted using [Atomic.Chat](http://Atomic.Chat), with source code available on [GitHub](https://github.com/AtomicBot-ai/Atomic-Chat).** One comment highlights the output of the `Qwen 3.6 27B FP8` model using opencode, taking approximately `52 seconds`. Another comment provides a visual comparison with the `Qwen 3.5 27B Q3` model, suggesting differences in output quality.

    * The user 'sacrelege' shared a performance result for the Qwen 3.6 27B model using FP8 precision, noting that it took approximately 52 seconds to complete a task with 'opencode'. This suggests a focus on optimizing model performance through precision adjustments, which can significantly impact computational efficiency and speed.
    * User 'nikhilprasanth' provided a visual comparison for the Qwen 3.5 27B Q3 model, indicating a potential interest in comparing different versions and quantization levels of the Qwen models. This highlights the importance of understanding how different model configurations can affect performance and output quality.
    * 'Technical-Earth-3254' inquired about the quantization methods used in the tests, which is crucial for understanding the trade-offs between model size, speed, and accuracy. Quantization can greatly influence the efficiency of large models like Qwen, especially in resource-constrained environments.
  * **[Qwen 3.6 27B is a BEAST](https://www.reddit.com/r/LocalLLaMA/comments/1steip4/qwen_36_27b_is_a_beast/)** (Activity: 1239): **The post discusses the performance of the**Qwen 3.6 27B** model on a high-end laptop with an **RTX 5090 GPU** and `24GB VRAM`, highlighting its effectiveness for **pyspark/python** and data transformation debugging tasks. The user employs **llama.cpp** with `q4_k_m` at `q4_0` and is exploring further optimizations with **IQ4_XS** at `200k q8_0`. The user has not yet implemented speculative decoding. The setup includes an **ASUS ROG Strix SCAR 18** with `64GB DDR5 RAM`.** Comments suggest avoiding kv cache as q4 for coding, recommending `q8` for `130k` context. Another comment anticipates performance improvements with upcoming releases from **z-lab** and a specific [GitHub pull request](https://github.com/ggml-org/llama.cpp/pull/22105) that promises a `2x` decode speed increase. There is also curiosity about the model's performance on systems with `16GB VRAM` and `32GB DDR5 RAM` with offloading.

    * sagiroth highlights a technical consideration when using Qwen 3.6 27B for coding tasks, advising against using the KV cache as q4 due to limitations, and instead suggests using q8 to achieve a `130k` context window, which can significantly enhance performance for large context tasks.
    * inkberk points out an upcoming improvement in decoding speed, referencing a pull request [#22105](https://github.com/ggml-org/llama.cpp/pull/22105) on the `llama.cpp` repository. This update, along with the anticipated release of the 'dflash drafter' by z-lab, promises a potential `2x` increase in decode speed, which could greatly benefit users in terms of efficiency.
    * Johnny_Rell inquires about the performance of Qwen 3.6 27B on a system with `16 GB VRAM` and `32 GB DDR5`, specifically regarding the effectiveness of offloading. This suggests a focus on optimizing resource allocation to handle the model's demands, which is crucial for running large models efficiently on consumer-grade hardware.



### 3\. Local AI Model Implementations and Innovations

  * **[Been using PI Coding Agent with local Qwen3.6 35b for a while now and its actually insane](https://www.reddit.com/r/LocalLLaMA/comments/1stjwg5/been_using_pi_coding_agent_with_local_qwen36_35b/)** (Activity: 656): **The post discusses the use of the**PI Coding Agent** with the **Qwen3.6 35b a3b q4_k_xl model** for real-world projects, highlighting the effectiveness of a custom 'plan-first' skill file. This file enforces a structured workflow by requiring a `TODO.md` approval before any code execution, ensuring tasks are completed in a planned and orderly manner. The model is run locally, demonstrating significant advancements in local model capabilities. The skill file includes phases for project analysis, clarifying questions, TODO.md creation, revision loops, and task execution, emphasizing a disciplined approach to coding tasks. The setup achieves `15-30 tokens per second` on an `8GB VRAM and 32GB RAM` laptop, showcasing the model's efficiency on modest hardware setups.** Commenters share similar setups, with one using a Macbook Pro M4 Pro with 48GB RAM, noting the model's speed and intelligence, leading to the cancellation of IDE and Claude subscriptions. Another user highlights the availability of 'plan mode' as an extension in official examples, indicating community interest and adoption.

    * SoAp9035 shares their configuration for running the Qwen3.6-35B model using `llama.cpp`, highlighting specific parameters such as `--temp 0.6`, `--top-p 0.95`, and `--top-k 20`. They achieve a performance of `15-30 tokens per second` on a setup with `8GB VRAM` and `32GB RAM`, indicating efficient use of resources for local model inference.
    * ibishitl mentions using a similar setup with a Macbook Pro M4 Pro and `48GB RAM`, noting the system's speed and intelligence in task completion. They have replaced their IDE and Claude subscriptions, suggesting that the local setup with Qwen3.6-35B is both cost-effective and capable enough to meet their needs.
    * audiophile_vin discusses using the Qwen3.6 27B model locally and finds it impressive. They reference an extension called 'Plan mode' available in the official examples on GitHub, which can enhance the functionality of the coding agent. This highlights the flexibility and expandability of the local setup.
  * **[Qwen-3.6-27B, llamacpp, speculative decoding - appreciation post](https://www.reddit.com/r/LocalLLaMA/comments/1stcer1/qwen3627b_llamacpp_speculative_decoding/)** (Activity: 402): **The post discusses an experiment using speculative decoding with the Qwen-3.6-27B model, demonstrating significant improvements in token generation speed from`13.60 t/s` to `136.75 t/s`. The user attributes this to specific settings in the `llama-server` command, particularly the use of `--spec-type ngram-mod --spec-ngram-size-n 24 --draft-min 12 --draft-max 48`. The setup includes a Linux PC with `40GB VRAM` and `128GB DDR5 RAM`, utilizing `RTX3090` and `RTX4060ti` GPUs. The user notes recent changes in `llama.cpp` and provides links to [documentation](https://github.com/ggml-org/llama.cpp/blob/master/docs/speculative.md#n-gram-cache-ngram-cache) and a [pull request](https://github.com/ggml-org/llama.cpp/pull/19164) for further reading.** Commenters discuss the necessity of the `--no-mmproj-offload` parameter for speculative decoding, with some not observing speed gains on different hardware setups. There is also curiosity about which model was used for drafting and skepticism about the speed improvements in different use cases.

    * EatTFM is questioning the necessity of the `--no-mmproj-offload` flag for speculative decoding, noting no speed gains on an RTX5090 with their current setup. They provide a detailed command line configuration for `llama.cpp` using the Qwen-3.6-27B model, highlighting parameters like `--spec-type ngram-mod` and `--spec-ngram-size-n 24`. They suspect an incompatibility with another parameter might be the issue.
    * kiwibonga points out a limitation of using n-grams in speculative decoding, specifically mentioning that it "doesn't work for coding" and can "break tool calls." This suggests that while n-grams might be beneficial for certain text generation tasks, they may introduce issues in contexts requiring precise tool integration or code generation.
    * nunodonato shares their experience, noting no observable speed difference with speculative decoding in their use case. This implies that the benefits of speculative decoding might be context-dependent, potentially varying with different hardware setups or specific model configurations.
  * **[just wanted to share](https://www.reddit.com/r/LocalLLM/comments/1su6vtx/just_wanted_to_share/)** (Activity: 1336): **The user has developed a distributed AI system named 'Chappie' using a cluster of four Mac Mini M4 Pros, each contributing to a unified node cluster with`256GB of unified memory`, `56 CPU cores`, `80 GPU cores`, and `64 Neural Engine cores`. The system utilizes [Exo](https://github.com/exo-explore/exo) for pooling nodes into a distributed inference cluster and employs a Qdrant vector database for memory sharing and replication. Chappie autonomously generates questions, reads arXiv papers, and develops new skills based on its findings. It features a sub-agent framework for task distribution and a 'council' of reviewer models to ensure quality control of its outputs. The AI's architecture includes a mix of models such as Qwen 3.6 35B, Qwen 3.6 27B, and others for various tasks, with a focus on autonomous exploration rather than being a mere tool or assistant.**

    * bionicdna highlights a technical improvement by suggesting the use of RDMA over Thunderbolt for clustering, which Apple now supports. This could potentially enhance performance compared to using 10G Ethernet, as RDMA (Remote Direct Memory Access) allows for faster data transfer by enabling direct memory access from the memory of one computer into that of another without involving either one's operating system.



## Less Technical AI Subreddit Recap

> /r/Singularity, /r/Oobabooga, /r/MachineLearning, /r/OpenAI, /r/ClaudeAI, /r/StableDiffusion, /r/ChatGPT, /r/ChatGPTCoding, /r/aivideo, /r/aivideo

### 1\. GPT-5.5 Launch and Benchmarks

  * **[Introducing GPT-5.5](https://www.reddit.com/r/singularity/comments/1stqev3/introducing_gpt55/)** (Activity: 1407): ****OpenAI** has released **GPT-5.5** , which is priced at `$5 per 1 million input tokens` and `$30 per 1 million output tokens`, doubling the cost of its predecessor, GPT-5.4. The model is optimized for tasks like coding and knowledge work, offering state-of-the-art accuracy in complex workflows with low latency and token usage. It includes advanced safeguards to prevent misuse and is available to Plus, Pro, Business, and Enterprise users, with API access to follow. For more details, see the [original article](https://openai.com/index/introducing-gpt-5-5/).** There is skepticism about the effectiveness of the new safeguards, as indicated by the comment, _"We are releasing GPT‑5.5 with our strongest set of safeguards to date" 🫪 oh boy_ , suggesting doubts about their robustness.

    * MapForward6096 highlights the pricing structure for GPT-5.5, noting it costs `$5 per 1 million input tokens` and `$30 per 1 million output tokens`, which is double the price of GPT-5.4. This suggests a significant increase in cost for users, potentially impacting budget allocations for projects relying on this model.
    * spryes criticizes GPT-5.5's performance on the SWE-Bench Pro benchmark, where it scored `58.6%`, compared to Mythos, which achieved `78%`. This comparison indicates that GPT-5.5 may not be as competitive in certain technical benchmarks, raising questions about its efficacy relative to other models.
    * mph99999 expresses disappointment with GPT-5.5, describing it as a "micro step forward" rather than the significant advancement expected. This sentiment suggests that the improvements in GPT-5.5 may not meet the expectations set by previous announcements or marketing, particularly in terms of innovation or performance enhancements.
  * **[GPT-5.5 benchmark results have been released](https://www.reddit.com/r/singularity/comments/1stqk81/gpt55_benchmark_results_have_been_released/)** (Activity: 779): **The image presents a comparative analysis of AI models' performance on various benchmarks, highlighting**GPT-5.5** and its variants. **GPT-5.5** shows improved performance over its predecessor, **GPT-5.4** , and other models like **Claude Opus 4.7** and **Gemini 3.1 Pro**. Notably, **GPT-5.5 Pro** achieves a `90.1%` score in the BrowseComp benchmark, indicating significant advancements in browsing capabilities. However, the **SWE-Bench Pro** results are less impressive, with only a marginal increase from `57.6%` to `58.6%`, compared to **Mythos** 's `77.8%`.** Commenters note the marginal improvements in some benchmarks, particularly criticizing the small increase in the SWE-Bench Pro score and suggesting that the results were selectively highlighted to favor GPT-5.5. There is also a sentiment against prematurely judging models based solely on benchmark scores without practical usage.

    * MapForward6096 and spryes highlight that GPT-5.5 shows only a marginal improvement in the SWE-Bench Pro benchmark, increasing from `57.6%` to `58.6%`, while the Mythos model achieves a significantly higher score of `77.8%`. This suggests that GPT-5.5 may not be competitive in this specific benchmark compared to Mythos.
    * TuteliniTuteloni points out a potentially overlooked advantage of GPT-5.5: it delivers better results with significantly fewer tokens. This efficiency in token usage could be a critical factor for applications where computational resources or processing time are limited, offering a practical benefit despite the modest benchmark improvements.
    * BrennusSokol expresses skepticism about GPT-5.5, questioning whether it represents a significant advancement or just an incremental update. This reflects a desire within the community for a more substantial leap in AI capabilities, rather than minor improvements.
  * **[Chat GPT 5.5 got launched and we got some really bold words by Sam Altman. Thoughts?](https://www.reddit.com/r/singularity/comments/1str6al/chat_gpt_55_got_launched_and_we_got_some_really/)** (Activity: 784): **The image is a tweet from**Sam Altman** discussing the launch of **GPT-5.5** , emphasizing the importance of iterative deployment for rapid improvements and democratizing AI to ensure equal access. Altman highlights the platform's focus on cybersecurity and its ability to support a wide range of users, including companies and entrepreneurs. The new version reportedly uses fewer tokens and operates with lower latency, which could enhance performance and accessibility.** The comments reflect a mix of skepticism and support, with some users expressing distrust towards overly positive messaging, while others show enthusiasm for the advancements.

  * **[thoughts on GPT 5.5](https://www.reddit.com/r/OpenAI/comments/1su1ikc/thoughts_on_gpt_55/)** (Activity: 1414): **The image is a meme that humorously comments on the release of a new version, likely GPT 5.5, by sarcastically celebrating the increase in version number. The playful tone reflects excitement about the "number business," suggesting a light-hearted take on version updates.[View Image](https://i.redd.it/3zudtu3yi1xg1.png)** Commenters express a desire for improved voice mode in GPT 5.5 and compare it favorably to Claude, indicating that users are looking for specific enhancements and are generally positive about the update.

    * One_Internal_6567 highlights that GPT-5.5 Pro is significantly better than its predecessors, noting a visible improvement from version 5.2 to 5.4. This suggests a consistent enhancement in performance and capabilities across these iterations, which may include better handling of complex queries or more efficient processing.
    * hardworkinglatinx compares GPT-5.5 favorably against Claude, implying that GPT-5.5 offers superior performance or features. This could involve aspects like response accuracy, speed, or the ability to handle diverse topics more effectively.
    * blownaway4 expresses a positive view of GPT-5.5, describing it as 'great.' While lacking specific technical details, this sentiment may reflect general satisfaction with the model's improvements or new features introduced in this version.
  * **[ChatGPT 5.5 🔥🔥🔥](https://www.reddit.com/r/OpenAI/comments/1stzivt/chatgpt_55/)** (Activity: 1359): **The image is a humorous depiction of a conversation with ChatGPT 5.5, where the AI suggests walking instead of driving to a car wash 50 meters away. This showcases the model's ability to provide practical advice based on context, emphasizing energy efficiency and convenience. The conversation highlights the AI's reasoning capabilities, as it considers factors like unnecessary engine starts and the hassle of moving the car for such a short distance. This reflects improvements in the model's contextual understanding and decision-making processes.** One commenter notes that the AI's response quality varies with its 'thinking' mode, suggesting that extended thinking leads to more accurate responses. Another comment humorously suggests that the question's prevalence on the internet might have influenced the AI's training data.

    * Successful-Earth678 discusses the impact of 'extended thinking' mode on ChatGPT's performance, noting that when the model is set to think longer, it consistently provides correct answers. This suggests that the model's accuracy can be improved by allowing more processing time, highlighting a potential trade-off between speed and accuracy in AI responses.
    * Portatort suggests that the widespread availability of certain questions on the internet may influence ChatGPT's training data, potentially affecting its ability to answer those questions accurately. This raises questions about the model's exposure to common queries and how it impacts its learning and response generation.
    * \---0celot--- provides a detailed, practical response from ChatGPT regarding a decision-making scenario about whether to walk or drive a short distance. The response includes considerations for practicality, safety, and environmental conditions, demonstrating the model's ability to offer nuanced advice based on context.



### 2\. DeepSeek V4 Release and Benchmarks

  * **[DeepSeek V4 has released](https://www.reddit.com/r/singularity/comments/1su3lj9/deepseek_v4_has_released/)** (Activity: 1407): ****DeepSeek V4** , released on [HuggingFace](https://huggingface.co/collections/deepseek-ai/deepseek-v4), incorporates the innovative _manifold-constrained hyper-connections_ (MHC) technique, which was detailed in a [recent paper](https://www.reddit.com/r/LocalLLaMA/comments/1q0zk1u/deepseek_new_paper_mhc_manifoldconstrained/). This approach enhances model performance by optimizing the connections within the neural network's manifold space, potentially offering superior results at a competitive price point.** One commenter highlights the model's impressive performance relative to its cost, suggesting it offers significant value. Another notes the implementation of the MHC technique as a noteworthy advancement.

    * FaceDeer highlights that DeepSeek V4 implements the 'manifold-constrained hyper-connections' technique, which was detailed in a recent paper. This approach likely contributes to the model's enhanced performance, as it optimizes the neural network's architecture by constraining connections within a manifold, potentially improving both efficiency and accuracy. [Read more](https://www.reddit.com/r/LocalLLaMA/comments/1q0zk1u/deepseek_new_paper_mhc_manifoldconstrained/).
    * InterstellarReddit points out the impressive cost-to-performance ratio of DeepSeek V4, suggesting that if the reported statistics hold true, the model could significantly disrupt the American market. This implies that DeepSeek V4 offers substantial computational power or accuracy improvements at a lower cost compared to competitors, making it a competitive choice for businesses and researchers.
    * cryyingboy notes DeepSeek's consistent delivery of new models, contrasting it with competitors who may focus more on marketing or theoretical discussions. This suggests that DeepSeek's strategy of frequent, tangible updates could be a key factor in its market success, potentially leading to faster adoption and integration into various applications.
  * **[DeepSeek V4 Benchmarks!](https://www.reddit.com/r/singularity/comments/1su5bwp/deepseek_v4_benchmarks/)** (Activity: 466): **The image presents a benchmark comparison of various models, including DS-V4-Pro Max and DS-V4-Flash Max, across categories like 'Reasoning Effort,' 'Knowledge & Reasoning,' 'Long Context,' and 'Agentic.' The benchmarks used include MMLU-Pro, SimpleQA-Verified, and Codeforces, highlighting each model's strengths and weaknesses. Notably, the DS-V4-Flash Max is praised for its cost-effectiveness, performing comparably to Gemini 3 Flash on artificial analysis tasks but at a significantly lower cost, estimated at about 50 cents per month for typical usage scenarios.** Commenters note that while the V4 models excel in coding tasks, they lack image analysis capabilities. The DS-V4-Flash Max is highlighted as a cost-effective option, offering competitive performance at a fraction of the cost of other models.

    * Dangerous-Sport-2347 highlights that the DeepSeek V4 Flash model is particularly cost-effective, performing comparably to Gemini 3 Flash in artificial analysis tasks but at a significantly lower cost—approximately 5 times less. This makes it a competitive option for users focused on cost-efficiency, especially for those engaging in frequent AI searches and coding tasks, estimating a monthly API cost of around 50 cents for moderate usage.
  * **[DeepSeek V4 dropped 1.6T params and 1M context without Nvidia GPUs. Here's the data.](https://www.reddit.com/r/DeepSeek/comments/1su7rzr/deepseek_v4_dropped_16t_params_and_1m_context/)** (Activity: 470): ****DeepSeek-V4** introduces a `1.6 trillion` parameter model with a `1 million` token context window, operating without Nvidia GPUs, using **Huawei Ascend 950PR** silicon. The model features two tiers: V4-Pro with `49B` active parameters and V4-Flash with `13B` active parameters. It employs **Engram Conditional Memory** for efficient context management, reducing inference overhead by `85%`. The API pricing is projected between `$0.14 and $0.28` per million tokens, significantly undercutting competitors. The model's architecture leverages parameter sparsity and native memory retrieval, challenging the Nvidia GPU monopoly and potentially transforming AI economics.** Commenters note potential further price reductions and skepticism about the impact on Nvidia's market position. There are also observations about inconsistencies in the model's self-identification and knowledge cutoff, indicating possible issues with model updates.

    * Neo_Shadow_Entity highlights a potential issue with DeepSeek V4's self-identification and knowledge cutoff. The model still identifies as DeepSeek-V3 and seems to have a knowledge cutoff at 2025, leading to confusion when discussing events or versions beyond that year. This suggests that the model's internal data or update mechanisms might not be fully synchronized with its latest version, causing it to misinterpret or hallucinate information about DeepSeek V4 from 2026.
    * smflx points out a misunderstanding regarding the term 'Engram' in the context of DeepSeek V4. Contrary to some expectations, 'Engram' is not related to KV-cache but rather to the model's weights. The commenter notes that the Huggingface page lacks a description of 'Engram,' indicating a need for further investigation to understand its role or presence in the model.
    * Wickywire emphasizes the significance of DeepSeek V4's pricing strategy, noting that the model offers substantial capacity at competitive price points. This pricing could significantly alter the landscape for AI users, particularly in environments like Openclaw, where cost-effective, high-capacity models can provide a competitive edge.
  * **[Deepseek-v4 flash and v4 pro](https://www.reddit.com/r/DeepSeek/comments/1su3bya/deepseekv4_flash_and_v4_pro/)** (Activity: 549): **The image provides a detailed comparison between two AI models,**deepseek-v4-flash** and **deepseek-v4-pro** , highlighting their features and pricing. Key differences include the context length and maximum output capabilities, with the v4-pro offering enhanced features like JSON output and tool calls. The pricing structure for input and output tokens is also compared, indicating a cost-benefit analysis for potential users. A notable point from the comments is the depreciation of the deepseek reasoner to the v4 flash thinking mode, which affects performance but still maintains competitive capabilities.**

    * The discussion highlights that the Deepseek Reasoner is being deprecated in favor of the Deepseek v4 Flash model, which is noted for its impressive performance despite being a 'flash' model. Users are surprised by its capability, as it performs almost on par with the previous Deepseek Reasoner, albeit with some caveats. This transition is likely a factor in the recent performance improvements observed in the API, as the Flash model is significantly smaller than its predecessor, Deepseek v3.
    * There is a mention of increased costs associated with the Deepseek v4 Pro model, suggesting a shift in the pricing strategy that may affect users who previously enjoyed a balance of quality and affordability. This change implies that while performance may have improved, the financial barrier to access these models has also increased, potentially limiting accessibility for some users.
    * The comments also touch on the broader strategic moves by Deepseek, such as joining forces with other entities, which could be influencing these changes in model deployment and pricing. This could indicate a shift in the company's focus towards more integrated or collaborative approaches in AI development.



### 3\. Claude Code Issues and Updates

  * **[Anthropic just published a postmortem explaining exactly why Claude felt dumber for the past month](https://www.reddit.com/r/ClaudeCode/comments/1str8gi/anthropic_just_published_a_postmortem_explaining/)** (Activity: 3991): ****Anthropic** published a postmortem detailing three bugs that caused a perceived degradation in **Claude Code** 's performance. The first bug involved a silent downgrade of reasoning effort from `high` to `medium` on March 4, which was reverted on April 7. The second bug, a caching issue from March 26, led to Claude forgetting its reasoning history, causing cache misses and faster usage limit depletion. The third bug, a system prompt change on April 16, limited responses to 25 words between tool calls, affecting coding quality, and was reverted on April 20. These issues, affecting different traffic slices, were fixed by April 20 (v2.1.116), and usage limits are being reset for subscribers. [Read the full postmortem](https://www.anthropic.com/engineering/april-23-postmortem).** Commenters noted that the issues matched user suspicions, suggesting a disconnect between user feedback and company acknowledgment. The transparency of the postmortem was appreciated, though some users expressed frustration over the initial lack of communication.

    * Direct-Attention8597 provides a direct link to the postmortem by Anthropic, which details the technical issues that led to Claude's perceived performance drop. The postmortem is a valuable resource for understanding the specific engineering challenges and resolutions implemented by Anthropic. [Read more here](https://www.anthropic.com/engineering/april-23-postmortem).
    * Jack_Dnlz highlights a strategic decision by Anthropic to reset usage limits just before the weekend, suggesting it minimizes the impact on users since many are less active during this time. This implies a calculated approach to managing user experience and resource allocation, potentially reducing the immediate load on their systems.
    * Sufficient-Farmer243 comments on the community's ability to diagnose the issues with Claude before official confirmation, suggesting that user feedback and observations were accurate. This highlights the importance of community insights in identifying and understanding AI performance issues.
  * **[Usage Reset due to Claude Code quality issues](https://www.reddit.com/r/ClaudeCode/comments/1stpywt/usage_reset_due_to_claude_code_quality_issues/)** (Activity: 615): **The image is a tweet from**ClaudeDevs** explaining a reset of usage limits due to quality issues with Claude Code. After user reports, they investigated and published a post-mortem on three identified issues, which have been fixed in version `2.1.116+`. As a result, usage limits have been reset for all subscribers. [Image](https://i.redd.it/v0euvm9d9zwg1.png)** Some users noted the reset was unusual, with varying remaining time limits, and expressed hope that the fixes would address cache misses and unusual usage limit burn issues.

    * YatzyNanimous highlights concerns about cache misses and unusual usage limit burn issues with Claude, suggesting that the reset might address these technical problems. Cache misses can lead to inefficient data retrieval, impacting performance, while unexpected usage limit burns could indicate underlying resource management issues.
    * dwight-is-right notes the release of GPT 5.5 and mentions recent open weight releases like Kimi 2.6, GLM 5.1, and qwen 3.6. These releases are significant as they reportedly reduce the performance gap between different AI models, suggesting a competitive landscape where improvements in one model prompt advancements in others.
    * The discussion touches on the technical implications of AI model updates and resets, with a focus on how these changes might affect performance and resource allocation. The mention of specific model versions and their impact on the competitive AI field underscores the rapid pace of development and the importance of staying updated with the latest releases.
  * **[Claude limits no longer round to the nearest hour](https://www.reddit.com/r/ClaudeAI/comments/1sue09c/claude_limits_no_longer_round_to_the_nearest_hour/)** (Activity: 494): **The image highlights a change in the way the AI service Claude manages its usage limits, moving from rounding to the nearest hour to a more precise minute-based system. This adjustment likely addresses user behavior where individuals would send a message just before the hour to maximize their usage limit. The notification also suggests an option to upgrade to a Pro version, indicating a tiered service model.** One comment suggests that the previous system was flawed by treating limits as 'hourly buckets,' which could lead to inefficient usage. Another comment humorously points out the frustration of hitting usage limits quickly, emphasizing the need for better management of message limits.

    * jake_that_dude suggests that the issue with Claude's limits is conceptualized as an 'hourly bucket,' which can lead to inefficient usage. For longer tasks, it's recommended to split work into smaller chats and include detailed handoff notes with state, blockers, and next steps to avoid wasting limits on context churn rather than productive output.
    * idiotiesystemique emphasizes the importance of managing chat sessions effectively by opening new chats and creating handover files. This approach can help in maintaining continuity and efficiency, especially when dealing with complex or extended interactions.
    * KronosDeret mentions a change in the 'fuel management plugin,' implying a technical update or modification that could affect how resources or limits are managed within the system. This could be relevant for users needing to adapt to new configurations or settings.
  * **[Claude reset limits for everyone](https://www.reddit.com/r/ClaudeAI/comments/1stozsr/claude_reset_limits_for_everyone/)** (Activity: 2094): **The image depicts a dashboard for a service, likely related to AI or machine learning usage, showing that usage limits have been reset to 0% for all categories, including 'Current session,' 'All models,' and 'Claude Design.' This reset suggests a change in the service's usage policy or a temporary reset of limits, which could be related to a new feature or update, such as the rumored launch of GPT-5.5. The reset is beneficial for users who were nearing their usage limits, as noted in the comments.** One comment humorously suggests that the billing system is 'vibes-based,' implying unpredictability or inconsistency in how limits are managed. Another comment notes that the reset is advantageous for users who were close to their limits, but also mentions that limits seem to be consumed faster post-reset, indicating potential changes in usage tracking or model efficiency.

    * National-Data-3928 highlights a significant issue with the reset of usage limits, noting that they are burning through their limits faster than before. This suggests potential changes in the underlying usage tracking or billing algorithm, which could impact users who rely heavily on the service.
    * DispensingLCQP expresses frustration with the reset timing, which unexpectedly shifted their usage cycle from Thursday to Friday. This change disrupts their planned usage pattern, particularly affecting those who schedule their usage around specific days. The comment also criticizes Opus 4.7 for its performance in creative writing tasks, indicating dissatisfaction with its capabilities compared to other models.



# AI Discords

Unfortunately, Discord shut down our access today. We will not bring it back in this form but we will be shipping the new AINews soon. Thanks for reading to here, it was a good run.

---

## [GPT 5.5](https://news.smol.ai/issues/26-04-23-gpt-55/)
*🌐 Smol AI News | 2026-04-23*

**a quiet day.**

> AI News for 4/22/2026-4/23/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

# AI Twitter Recap

**Top Story: GPT-5.5 launch**

## What happened

**OpenAI launched GPT-5.5 as its new flagship frontier model for “real work and powering agents,” rolling it out immediately in ChatGPT and Codex, while delaying API access pending additional safety requirements** ([OpenAI](https://x.com/OpenAI/status/2047376561205325845), [OpenAI rollout](https://x.com/OpenAI/status/2047376568809636017), [OpenAIDevs](https://x.com/OpenAIDevs/status/2047377079352877534), [API delayed](https://x.com/scaling01/status/2047376535376552414)). OpenAI positioned the model as a step toward lower-micromanagement agentic work: stronger coding, computer use, knowledge work, scientific research, and longer multi-step execution with tool use and self-checking ([OpenAI](https://x.com/OpenAI/status/2047376567559668222), [gdb](https://x.com/gdb/status/2047381612372115812), [snsf](https://x.com/snsf/status/2047382049494028574)). Pricing landed at **$5/$30 per million input/output tokens for GPT-5.5** and **$30/$180 for GPT-5.5 Pro** ([scaling01 pricing](https://x.com/scaling01/status/2047375819144597737), [sama pricing](https://x.com/sama/status/2047379036419014928)). The model was described by OpenAI and multiple early testers as notably more token-efficient than GPT-5.4, often using materially fewer output tokens while keeping similar per-token speed ([sama](https://x.com/sama/status/2047378254575685707), [OpenAIDevs](https://x.com/OpenAIDevs/status/2047377281480642685), [reach_vb](https://x.com/reach_vb/status/2047379895505051924), [GitHub VP claim relayed by scaling01](https://x.com/scaling01/status/2047392640681795731)). OpenAI also bundled significant Codex product upgrades around the launch—browser control, file/docs/PDF handling, Sheets & Slides, auto-review mode, OS-wide dictation, and broader computer-use workflows ([ajambrosino](https://x.com/ajambrosino/status/2047381565534322694), [OpenAIDevs browser use](https://x.com/OpenAIDevs/status/2047381283358355706), [thsottiaux](https://x.com/thsottiaux/status/2047387017974337611), [sama “bundle”](https://x.com/sama/status/2047378431260664058)).

Independent and semi-independent reactions were mixed but broadly positive: many users called it a step change in coding and long-horizon work, while others argued the headline benchmark gains looked incremental, the price doubled vs GPT-5.4, hallucination remains high on at least one third-party eval, and Anthropic’s Mythos or Opus variants still lead or tie on some tasks depending on benchmark selection ([Artificial Analysis](https://x.com/ArtificialAnlys/status/2047378419282034920), [theo](https://x.com/theo/status/2047379285107691835), [scaling01 critique](https://x.com/scaling01/status/2047386588368208287), [Perspective vs Mythos](https://x.com/synthwavedd/status/2047382400112660608), [scaling01 Mythos lead take](https://x.com/scaling01/status/2047385663356477848)).

## Release details

  * **Product availability**

    * Rolling out **today** to **Plus, Pro, Business, and Enterprise** users in **ChatGPT and Codex** ([OpenAI rollout](https://x.com/OpenAI/status/2047376568809636017)).
    * **GPT-5.5 Pro** available to **Pro, Business, Enterprise** users in ChatGPT ([OpenAI rollout](https://x.com/OpenAI/status/2047376568809636017)).
    * **API access** not same-day; OpenAI says it is **“coming soon”** and delayed due to **higher safety requirements / robust safeguards** ([OpenAIDevs](https://x.com/OpenAIDevs/status/2047377079352877534), [scaling01](https://x.com/scaling01/status/2047376535376552414), [jeffintime](https://x.com/jeffintime/status/2047411842935554385)).
    * Third-party ecosystem support appeared quickly, e.g. **Hermes Agent** support via ChatGPT/Codex OAuth ([Teknium](https://x.com/Teknium/status/2047419336537846193)).
  * **Pricing**

    * **GPT-5.5:** **$5 input / $30 output** per 1M tokens ([scaling01 pricing](https://x.com/scaling01/status/2047375819144597737), [sama pricing](https://x.com/sama/status/2047379036419014928)).
    * **GPT-5.5 Pro:** **$30 / $180** per 1M tokens ([scaling01 pricing](https://x.com/scaling01/status/2047375819144597737)).
    * This is widely noted as **2x GPT-5.4 pricing** at the per-token level ([scaling01](https://x.com/scaling01/status/2047381738817531931)), though OpenAI and several testers argue effective task cost is moderated by token efficiency ([sama](https://x.com/sama/status/2047378254575685707), [OpenAIDevs](https://x.com/OpenAIDevs/status/2047377281480642685)).
  * **Context**

    * Publicly cited as **1M context in API** and **400K context in Codex** by Swyx summarizing launch materials ([swyx](https://x.com/swyx/status/2047378670986342685)).
    * Sam Altman separately referenced **1M context window** alongside API pricing ([sama pricing/context](https://x.com/sama/status/2047379036419014928)).
  * **Infrastructure / serving**

    * OpenAI-linked commentary says GPT-5.5 was **co-designed for Nvidia GB200/GB300** and that it was **the first generation co-designed with GB200 and GB300 NVL72** ([scaling01](https://x.com/scaling01/status/2047377992016384068), [swyx](https://x.com/swyx/status/2047378670986342685)).
    * Jonathan Ross also highlighted **GB200 NVL72** training from early access observations ([JonathanRoss321](https://x.com/JonathanRoss321/status/2047383400651313539)).
    * OpenAI says **Codex + GPT-5.5 helped optimize the serving stack** , increasing token generation speed by **20%+** ([reach_vb](https://x.com/reach_vb/status/2047379033932112341), [sama inference team praise](https://x.com/sama/status/2047386068194852963)).
    * Sam Altman said **per-token speed matches GPT-5.4** while using fewer tokens per task ([sama](https://x.com/sama/status/2047378254575685707)).
  * **Codex app changes at launch**

    * New features: **browser control, Sheets & Slides, Docs & PDFs, OS-wide dictation, auto-review mode** ([ajambrosino](https://x.com/ajambrosino/status/2047381565534322694)).
    * Expanded browser use for testing web flows, screenshots, iteration on what it sees ([OpenAIDevs](https://x.com/OpenAIDevs/status/2047381283358355706)).
    * OpenAI explicitly framed Codex + 5.5 as useful beyond coding: spreadsheets, slides, documents, browser workflows ([gdb](https://x.com/gdb/status/2047387783111868707)).



## Technical details and benchmark numbers

### OpenAI-reported headline metrics

OpenAI and launch-adjacent posts gave the following benchmark claims:

  * **Terminal-Bench 2.0:** **82.7%** ([OpenAIDevs](https://x.com/OpenAIDevs/status/2047377098483155317), [reach_vb](https://x.com/reach_vb/status/2047377562339524659))
  * **OSWorld-Verified:** **78.7%** ([OpenAIDevs](https://x.com/OpenAIDevs/status/2047377098483155317), [reach_vb](https://x.com/reach_vb/status/2047377562339524659))
  * **Toolathlon:** **55.6%** ([OpenAIDevs](https://x.com/OpenAIDevs/status/2047377098483155317))
  * **FrontierMath Tier 4:** **35.4%** ; **GPT-5.5 Pro** later cited at **39.5%** ([OpenAIDevs](https://x.com/OpenAIDevs/status/2047377098483155317), [scaling01](https://x.com/scaling01/status/2047379219546591543))
  * **CyberGym:** **81.8%** ([OpenAIDevs](https://x.com/OpenAIDevs/status/2047377098483155317), [reach_vb](https://x.com/reach_vb/status/2047377562339524659))
  * **SWE-Bench Pro:** **58.6%** ([reach_vb](https://x.com/reach_vb/status/2047377562339524659), [swyx](https://x.com/swyx/status/2047378670986342685))
  * **GDPval:** **84.9% win/tie** ([reach_vb](https://x.com/reach_vb/status/2047377562339524659))
  * **BrowseComp:** **84.4%** ([reach_vb](https://x.com/reach_vb/status/2047377562339524659))
  * **FrontierMath Tier 1–3:** **51.7%** ([reach_vb](https://x.com/reach_vb/status/2047377562339524659))
  * **MMMU-Pro without tools:** **81.2%** ([reach_vb](https://x.com/reach_vb/status/2047377562339524659))
  * **Investment banking modeling:** **88.5%** ([reach_vb](https://x.com/reach_vb/status/2047377562339524659))
  * **Expert-SWE** internal eval: **73.1%** ([swyx](https://x.com/swyx/status/2047378670986342685))
  * **Tau2-bench Telecom:** **98.0%** ([swyx](https://x.com/swyx/status/2047378670986342685))
  * **BixBench:** **80.5%** ([swyx](https://x.com/swyx/status/2047378670986342685))
  * **ARC-AGI-1:** **95.0%**
  * **ARC-AGI-2:** **85.0%** ([scaling01](https://x.com/scaling01/status/2047378636592869782), [ARC Prize verified](https://x.com/arcprize/status/2047388614167003208))
  * **CritPt:** **27.1%** for xhigh ([scaling01](https://x.com/scaling01/status/2047382519964672287), [MinyangTian1](https://x.com/MinyangTian1/status/2047401277701890117))



### Independent / semi-independent benchmarks

  * **Artificial Analysis**
    * Says GPT-5.5 takes the #1 spot on its **Intelligence Index by 3 points** , breaking a prior three-way tie among OpenAI, Anthropic, Google ([Artificial Analysis](https://x.com/ArtificialAnlys/status/2047378419282034920)).
    * Claims GPT-5.5 leads **Terminal-Bench Hard, GDPval-AA, APEX-Agents-AA** , and trails only other OpenAI models in **CritPt** and **AA-LCR** , while placing second to **Gemini 3.1 Pro Preview** on three more benchmarks ([Artificial Analysis](https://x.com/ArtificialAnlys/status/2047378419282034920), [headline evals follow-up](https://x.com/ArtificialAnlys/status/2047378431634211011)).
    * Says **GPT-5.5 medium ≈ Claude Opus 4.7 max** at **~1/4 the cost** on its index, while **Gemini 3.1 Pro Preview** reaches similar score at still lower cost ([Artificial Analysis](https://x.com/ArtificialAnlys/status/2047378419282034920)).
    * Reports **~40% token-use reduction** vs GPT-5.4 offsetting higher price; net cost to run its Intelligence Index rises only about **20%** ([Artificial Analysis](https://x.com/ArtificialAnlys/status/2047378419282034920)).
    * Reports **AA-Omniscience accuracy 57%** but **hallucination rate 86%** , versus **Opus 4.7 max at 36%** and **Gemini 3.1 Pro Preview at 50%** , which is one of the most important caveats in the entire launch discussion ([Artificial Analysis](https://x.com/ArtificialAnlys/status/2047378419282034920)).
  * **ARC Prize**
    * Verified **ARC-AGI-2 SOTA** at **85.0% max** , with cost/performance ladder: 
      * Max: **85.0%, $1.87**
      * High: **83.3%, $1.45**
      * Med: **70.4%, $0.86**
      * Low: **33%, $0.35** ([ARC Prize](https://x.com/arcprize/status/2047388614167003208))
  * **Andon Labs / Vending-Bench Arena**
    * Says GPT-5.5 **beats Opus 4.7** in competitive **Vending-Bench Arena** , and specifically notes GPT-5.5’s tactics were **clean** , while Opus used deceptive behaviors ([andonlabs](https://x.com/andonlabs/status/2047377260412649967)).
  * **UK AISI / safety testing**
    * The UK AI Security Institute said it conducted **pre-deployment testing on cyber, autonomy capabilities, and safeguards** , pointing readers to the system card ([AISecurityInst](https://x.com/AISecurityInst/status/2047378240839233707)).
  * **System-card-derived cyber result**
    * A widely cited number from readers of the system card: GPT-5.5 could **take over a simulated corporate network in 1/10 trials with a 100M-token budget** , compared with **Claude Mythos at 3/10** , while **Opus 4.6/4.7 failed** on the cited task ([scaling01](https://x.com/scaling01/status/2047403154455617673)).
  * **LiveBench**
    * scaling01 says **GPT-5.5-xhigh placed 1st on LiveBench** ([scaling01](https://x.com/scaling01/status/2047419533766385897)).



## Examples of progress in practice

The strongest launch-day evidence was not just benchmarks but user reports of longer-horizon autonomy and reduced micromanagement:

  * **Every early test**
    * Dan Shipper says GPT-5.5 scored **62/100** on Every’s **Senior Engineer benchmark** vs **Opus 4.7 at 33/100** , while noting it performs best **with an Opus 4.7-generated plan** ([danshipper](https://x.com/danshipper/status/2047375686688473134)).
    * Reported **900M+ tokens** used in testing by one engineer, shipping production features ([danshipper](https://x.com/danshipper/status/2047375686688473134)).
    * Praises conceptual clarity, ability to sustain complex refactors, and stronger writing than recent OpenAI models.
  * **Matthew Berman**
    * Calls Codex variant “the absolute frontier” for agentic coding, especially backend and visual inspection loops, while saying **Opus remains faster** and still better for front-end design in many cases ([MatthewBerman](https://x.com/MatthewBerman/status/2047375703516361174)).
    * Reports **medium/high thinking** worked best; **xhigh** felt too slow for many workflows.
  * **OpenAI internal user reports**
    * Noam Brown-ish? actually polynoamial says GPT-5.5 makes him “a more effective IC,” specifically for **CUDA kernels** and research experiments ([polynoamial](https://x.com/polynoamial/status/2047381460437635313)).
    * tszzl says researchers are already letting GPT-5.5 run **overnight experiments** from only high-level ideas, producing completed sweeps by morning ([tszzl](https://x.com/tszzl/status/2047386955550470245)).
    * aidan_mclau says he dictated a new RL run, left for days, and came back to a **31-hour industrial-scale RL run** progressing under GPT-5.5 supervision ([aidan_mclau](https://x.com/aidan_mclau/status/2047388367705575701), [sleeping/babysitting nuance](https://x.com/aidan_mclau/status/2047388746287648867)).
    * johnohallman says 5.5 can work on projects **end-to-end for hours or days** , changing his role from IC toward manager ([johnohallman](https://x.com/johnohallman/status/2047403368856092967)).
    * clivetime says he now manages **~10 Codexes** and spends most time on net new progress rather than setup/plumbing ([itsclivetime](https://x.com/itsclivetime/status/2047391351889924284)).
  * **Skirano examples**
    * Describes GPT-5.5 resolving a nasty branch conflict situation as a personal “first taste of AGI” ([skirano thread start](https://x.com/skirano/status/2047377443011342779)).
    * Says it can create apps for a **Flipper Zero via USB connection** and push them successfully ([skirano USB example](https://x.com/skirano/status/2047377449235759334)).
    * Says it built a more genuinely playable one-shot game, later featured on the release page ([skirano game](https://x.com/skirano/status/2047403025094905964)).
  * **Visual/code synthesis examples**
    * Sebastien Bubeck showed GPT-5.5 getting close to saturating his **TikZ unicorn test** with actual verifiable TikZ code ([SebastienBubeck](https://x.com/SebastienBubeck/status/2047383628922167390)).
    * Dimillian used Codex + imagegen skills + macOS app tooling to create a **native retro fantasy labyrinth game** from prompts ([Dimillian](https://x.com/Dimillian/status/2047379548858114237)).
  * **Enterprise / computer-use angle**
    * OpenAI says users at **Ramp** are using GPT-5.5 in Codex to test **full-stack QA changes end-to-end** ([OpenAIDevs](https://x.com/OpenAIDevs/status/2047397385719157070)).
    * Sam says OpenAI and Nvidia tried rolling Codex out across an entire company, implying confidence in broad enterprise deployment ([sama](https://x.com/sama/status/2047395562501411058)).
    * gdb stresses this is now useful to “anyone who does computer work,” not just programmers ([gdb](https://x.com/gdb/status/2047387783111868707)).



## Facts vs opinions

### Facts / directly supported claims

  * GPT-5.5 launched in **ChatGPT and Codex** , API delayed ([OpenAI](https://x.com/OpenAI/status/2047376561205325845), [OpenAIDevs](https://x.com/OpenAIDevs/status/2047377079352877534)).
  * Pricing is **$5/$30** and **Pro $30/$180** per 1M tokens ([sama](https://x.com/sama/status/2047379036419014928), [scaling01](https://x.com/scaling01/status/2047375819144597737)).
  * OpenAI reported benchmark scores including **82.7 Terminal-Bench 2.0** , **78.7 OSWorld-Verified** , **81.8 CyberGym** , **58.6 SWE-Bench Pro** ([OpenAIDevs](https://x.com/OpenAIDevs/status/2047377098483155317), [reach_vb](https://x.com/reach_vb/status/2047377562339524659)).
  * Artificial Analysis independently ranked GPT-5.5 first on its Intelligence Index and published a nuanced cost/hallucination analysis ([Artificial Analysis](https://x.com/ArtificialAnlys/status/2047378419282034920)).
  * ARC Prize reported **85.0% on ARC-AGI-2** ([arcprize](https://x.com/arcprize/status/2047388614167003208)).
  * OpenAI and launch observers said GPT-5.5 is more token-efficient than GPT-5.4 ([OpenAIDevs](https://x.com/OpenAIDevs/status/2047377281480642685), [sama](https://x.com/sama/status/2047378254575685707)).



### Opinions / interpretations

  * “The frontier moved back to OpenAI today” ([TheRundownAI](https://x.com/TheRundownAI/status/2047379050956501053)).
  * “Best model I have ever used” ([skirano](https://x.com/skirano/status/2047378534826475602)).
  * “Massive achievement,” “step change,” “new era,” “feels like early GPT-4” ([danshipper](https://x.com/danshipper/status/2047375686688473134), [DeryaTR_](https://x.com/DeryaTR_/status/2047377414339084401), [BorisMPower](https://x.com/BorisMPower/status/2047377516223152360)).
  * “Underwhelming incremental benchmark lifts” / “twice the price feels like a kick in the face” ([scaling01](https://x.com/scaling01/status/2047386588368208287), [paul_cal](https://x.com/paul_cal/status/2047384440549126487)).
  * “Weaker than Mythos” or “close to Mythos but smaller/cheaper” are not established facts; they are benchmark-selection-dependent interpretations ([synthwavedd](https://x.com/synthwavedd/status/2047382400112660608), [scaling01](https://x.com/scaling01/status/2047413871875633628), [scaling01 contrary take](https://x.com/scaling01/status/2047385663356477848)).



## Different opinions

### Supportive takes

  * **OpenAI official line:** GPT-5.5 is a “new class of intelligence” for real work, with better intuition, lower micromanagement, and broader deployment as part of iterative safety strategy ([OpenAI](https://x.com/OpenAI/status/2047376561205325845), [gdb](https://x.com/gdb/status/2047381612372115812), [sama strategy](https://x.com/sama/status/2047379615589777666)).
  * **Early testers:** strong upgrades in coding, writing, long-running autonomy, and knowledge work ([danshipper](https://x.com/danshipper/status/2047375686688473134), [MatthewBerman](https://x.com/MatthewBerman/status/2047375703516361174), [skirano](https://x.com/skirano/status/2047377441316843793)).
  * **Third-party eval orgs:** Artificial Analysis and ARC Prize both support the claim that GPT-5.5 is at or near the top of the frontier ([Artificial Analysis](https://x.com/ArtificialAnlys/status/2047378419282034920), [ARC Prize](https://x.com/arcprize/status/2047388614167003208)).



### Skeptical or critical takes

  * **Price skepticism:** per-token price doubled from GPT-5.4; Theo called it too expensive despite liking its intelligence ([theo](https://x.com/theo/status/2047379285107691835)).
  * **Benchmark skepticism:** scaling01 argued median improvement over GPT-5.4 across 37 OpenAI-reported benchmarks was only **+2.8%** while price doubled ([scaling01](https://x.com/scaling01/status/2047386588368208287)).
  * **Hallucination caution:** Artificial Analysis reported an **86% hallucination rate** on AA-Omniscience, much worse than top Anthropic/Google competitors on that metric ([Artificial Analysis](https://x.com/ArtificialAnlys/status/2047378419282034920)).
  * **Task-profile skepticism:** GPT-5.5 seems unusually strong on terminal/computer-use/cyber but comparatively less dominant on **SWE-Bench Pro** , leading some to call its intelligence “spiky” or benchmark-sensitive ([scaling01](https://x.com/scaling01/status/2047378968412598688), [scaling01 later synthesis](https://x.com/scaling01/status/2047413871875633628)).
  * **Behavioral criticism:** Theo says it writes the best code he’s seen but can be “weird,” “hard to wrangle,” and over-exploratory without strict instructions ([theo](https://x.com/theo/status/2047379702189310085)).



### Neutral / contextual takes

  * **Inference-compute framing:** polynoamial argues single-number model comparisons are increasingly misleading; what matters is intelligence per token or per dollar ([polynoamial](https://x.com/polynoamial/status/2047387675762802998)).
  * **Recipe not endpoint:** Hangsiin suggests GPT-5.5 looks like an initial RL checkpoint on a new pretraining base, more like an “o1/o1-preview” stage than a terminal form ([Hangsiin](https://x.com/Hangsiin/status/2047383140738756958)).
  * **Economics matter as much as raw IQ:** teortaxesTex argues that even if Mythos is stronger in places, GPT-5.5’s economics and deployability may matter more in a real market ([teortaxesTex](https://x.com/teortaxesTex/status/2047395961693937769#m)).



## Context: why this matters

GPT-5.5 appears important for three reasons:

  1. **It shifts the competition from “chat model” to “agent substrate.”** OpenAI repeatedly emphasized computer use, browser actions, documents, spreadsheets, and long-running task completion, not just one-shot answers ([OpenAI](https://x.com/OpenAI/status/2047376561205325845), [OpenAIDevs](https://x.com/OpenAIDevs/status/2047381283358355706), [gdb](https://x.com/gdb/status/2047387783111868707)). This also aligns with outside observers saying the “model is the product” and that cloud/desktop agents are the real next unlock.

  2. **It sharpens the benchmark debate.** On one hand, GPT-5.5 tops or ties several respected evals. On the other, users are visibly less convinced by benchmark screenshots alone. There are tweets explicitly dismissing benchmarks in favor of heavy-user feedback ([skooookum](https://x.com/skooookum/status/2047064363282960430)). This launch reinforced that split: official benchmark wins mattered, but much of the excitement came from examples like overnight research runs, end-to-end app building, and hardware control.

  3. **It raises the importance of efficiency over raw size.** Several observers frame GPT-5.5 as a model where **token efficiency, speed, and serving economics** are nearly as important as capability ([Artificial Analysis](https://x.com/ArtificialAnlys/status/2047378419282034920), [sama](https://x.com/sama/status/2047378254575685707), [polynoamial](https://x.com/polynoamial/status/2047387675762802998)). If OpenAI can deliver near-Mythos or better-than-Opus behavior at materially lower effective task cost, that changes enterprise adoption dynamics even if another lab still wins selected top-end evals.




## Bottom line

GPT-5.5’s launch is best understood not as a clean “OpenAI crushes everyone” story, nor as a trivial incremental bump. The strongest evidence suggests:

  * **Yes, GPT-5.5 is a real frontier advance** , especially on **agentic coding, terminal work, browser/computer use, and long-horizon execution** ([OpenAIDevs](https://x.com/OpenAIDevs/status/2047377098483155317), [Artificial Analysis](https://x.com/ArtificialAnlys/status/2047378419282034920), [ARC Prize](https://x.com/arcprize/status/2047388614167003208)).
  * **Its practical usability story matters as much as benchmark gains** : lower micromanagement, fewer tokens, sustained work over hours, and broader desktop workflows seem to be the launch’s defining theme ([MatthewBerman](https://x.com/MatthewBerman/status/2047375703516361174), [danshipper](https://x.com/danshipper/status/2047375686688473134), [tszzl](https://x.com/tszzl/status/2047386955550470245)).
  * **But the launch is not uncontested** : higher per-token cost, uneven benchmark profile, and notable hallucination concerns leave room for Anthropic and Google depending on the workload ([Artificial Analysis](https://x.com/ArtificialAnlys/status/2047378419282034920), [theo](https://x.com/theo/status/2047379285107691835), [scaling01](https://x.com/scaling01/status/2047385663356477848)).
  * **The market implication is strong** : if this capability/speed/token-efficiency mix holds up under API access and broad usage, GPT-5.5 likely resets expectations for what “default work model” means in coding and computer-use products.



* * *

**Vision and multimodal research**

  * **Google DeepMind’s “Vision Banana”** drew substantial attention as a unified model for image understanding and generation, reframing image generation as a general interface for vision tasks. Supportive summaries came from [@arankomatsuzaki](https://x.com/arankomatsuzaki/status/2047139493543846251), the official thread by [@songyoupeng](https://x.com/songyoupeng/status/2047312019976785944), and reflections from [@sainingxie](https://x.com/sainingxie/status/2047339789926429166). The pitch: generative perception may become foundational to CV, though even supporters note diffusion latency and practical limitations remain major blockers ([@sainingxie follow-up](https://x.com/sainingxie/status/2047339802954023347)).
  * OpenAI image generation also got strong anecdotal praise. [@goodside](https://x.com/goodside/status/2047081818671751171) said a deployment fix materially improved quality and undermined the old assumption that model choice is irrelevant when image generation is “just a tool call.” He later showed weirdly strong compositional/code-like behavior: an SVG-renderable cake image and alphabet soup encoding a valid FizzBuzz solution ([cake/SVG](https://x.com/goodside/status/2047211270324043985), [FizzBuzz soup](https://x.com/goodside/status/2047362062146216327)).
  * Sam Altman said **Images 2.0 crossed an important qualitative threshold** for him ([sama](https://x.com/sama/status/2047349336263012771)). Swyx’s framing was that **“Image-2-Thinking” behaves more like an image agent than a pure image model** , using search/compositing/review loops over tens of minutes ([swyx](https://x.com/swyx/status/2047140362771132544)).



**Open models, Chinese labs, and inference economics**

  * **Kimi K2.6** and **GLM-5.1** were repeatedly cited as the strongest open/open-adjacent challengers: 
    * K2.6 hit **#1 open model on MathArena** ([j_dekoninck](https://x.com/j_dekoninck/status/2047282510015471908)).
    * K2.6 and GLM-5.1 now lead **WeirdML** among open models but remain behind GPT-5 according to [@scaling01](https://x.com/scaling01/status/2047297042838433829).
    * Several posters described K2.6 as a genuine frontier-tier jump over K2.5 ([teortaxesTex](https://x.com/teortaxesTex/status/2047291192707002661), [WesRoth](https://x.com/WesRoth/status/2047186038402240652)).
  * **Qwen3.6-27B** got unusually strong grassroots praise for local usability: 
    * [@coffeecup2020](https://x.com/coffeecup2020/status/2047087575970549817) called **Qwen3.6-27B-TQ3_4S** “insanely good,” fitting on **16GB VRAM with 32k context**.
    * [@leftcurvedev_](https://x.com/leftcurvedev_/status/2047373913198416187) claimed a local 16GB-VRAM model beats Claude Sonnet 4.5 in his usage.
  * There was also a stream of commentary around **Tencent Hy3 preview** : 
    * vLLM announced **day-0 support** , listing **295B total / 21B active** , **256K context** , hybrid fast/slow-thinking MoE, and biggest gains in coding/agents ([vLLM](https://x.com/vllm_project/status/2047349857011327209)).
    * [@ShunyuYao12](https://x.com/ShunyuYao12/status/2047355369878650898) stressed product co-design over open-benchmark chasing.
    * A Chinese architecture breakdown characterized Hy3 as a composite of ideas from Apertus, DeepSeek V3, MiniMax M2, and Qwen3-MoE ([karminski3](https://x.com/karminski3/status/2047331063199125578)).
  * Inference economics continued to dominate discussion: 
    * Together usage reportedly grew from **30B to 300T tokens/month YoY** ([vipulved](https://x.com/vipulved/status/2047183589222273231)).
    * Patrick O’Shaughnessy’s podcast with Dylan Patel focused on token supply/demand, compute bottlenecks, memory pricing, and robotics as the next demand wave ([patrick_oshag](https://x.com/patrick_oshag/status/2047284358088622594)).
    * Several posts framed the key metric as **intelligence per $ / token** , not one-number leaderboard rank ([polynoamial](https://x.com/polynoamial/status/2047387675762802998)).



**Training/inference systems and kernels**

  * **Decoupled DiLoCo** from Google DeepMind/Google Research was one of the most technically substantive infra releases: 
    * It targets **multi-datacenter training over low-bandwidth networks** , **heterogeneous hardware** , and training that **doesn’t halt on hardware failures** ([Ar_Douillard](https://x.com/Ar_Douillard/status/2047329942547968171), [GoogleDeepMind](https://x.com/GoogleDeepMind/status/2047330981145669790)).
    * Google says it trained a **12B Gemma model across four US regions** and mixed **TPU6e + TPUv5p** without slowing training ([GoogleDeepMind details](https://x.com/GoogleDeepMind/status/2047330992713589009)).
    * This connected with parallel community interest in distributed-training “island size” constraints and alternatives to requiring hundreds of colocated B200s ([jon_durbin](https://x.com/jon_durbin/status/2047309041903288520)).
  * **DeepSeek tile kernels / TileLang** release got a strong response: 
    * Posts from [@teortaxesTex](https://x.com/teortaxesTex/status/2047248025374921110), [@scaling01](https://x.com/scaling01/status/2047282888324903328), [@eliebakouch](https://x.com/eliebakouch/status/2047327174810624018), and [@_arohan_](https://x.com/_arohan_/status/2047345874616115446) highlighted optimized kernels for **Engram** and **mHC** , with some already used in internal training/inference.
    * A separate DeepSeek-serving anecdote claimed API throughput hit **91 tok/s** , above a previously estimated practical ceiling on H800s ([teortaxesTex](https://x.com/teortaxesTex/status/2047293971584430163)).
  * Agentic optimization is creeping into systems work: 
    * [@xenovacom](https://x.com/xenovacom/status/2047303396793651397) reported **Opus 4.7 wrote a custom WebGPU kernel** yielding up to **13x faster** Qwen3.5 inference in Transformers.js via fused LinearAttention.
    * OpenAI claimed Codex itself helped optimize GPT-5.5 serving speed by **20%+** ([reach_vb](https://x.com/reach_vb/status/2047379033932112341)).



**Agents, evaluation, memory, and harnesses**

  * A consistent theme across papers and practitioner commentary: **agent quality depends heavily on harness design** , not just base model quality. 
    * Anthropic published a postmortem saying Claude Code quality regressions came from harness/config changes, not only the model: lower default reasoning, a bug evicting thinking blocks, and a verbosity-related prompt tweak. All were fixed and limits reset ([ClaudeDevs](https://x.com/ClaudeDevs/status/2047371123185287223)).
    * This triggered broader calls for **open harnesses and open evals** ([Vtrivedy10](https://x.com/Vtrivedy10/status/2047384831995371631), [omarsar0](https://x.com/omarsar0/status/2047399819379941639)).
  * New agent papers/issues discussed: 
    * **SWE-chat** captures coding-agent interactions from real users in the wild ([SciFi](https://x.com/SciFi/status/2047208289839038660)).
    * **Stateless Decision Memory** proposes event-sourced immutable decision logs for enterprise agents, emphasizing scalability/auditability over “cleverness” ([omarsar0](https://x.com/omarsar0/status/2047325132096758228)).
    * A paper on **diversity collapse in multi-agent systems** argues that shared context and mutual feedback drive homogenization unless designs explicitly decouple reasoning/evaluation ([dair_ai](https://x.com/dair_ai/status/2047326894992081296), [douwekiela coverage](https://x.com/douwekiela/status/2047333168878133614)).
    * **AutoMetrics** claims that with **< 100 feedback points** it can induce automatic task metrics that beat hand-crafted LLM-judge rubrics by up to **+33.4% correlation improvement** to human judgments ([michaelryan207](https://x.com/michaelryan207/status/2047295691702083876)).
  * Product-side agent infra: 
    * **Hermes desktop** emphasizes direct SSH, no browser/gateway layers ([DODOREACH](https://x.com/DODOREACH/status/2047089899807895903)).
    * **Delegate** launched as a delegated-work agent ([abhshkdz](https://x.com/abhshkdz/status/2047345080365969648)).
    * **LangSmith Fleet** added direct file creation/editing and presentation building ([LangChain Fleet](https://x.com/LangChain/status/2047362259983495215), [BraceSproul](https://x.com/BraceSproul/status/2047417882423022034)).
    * **Trackio** decoupled frontend/backend to enable LLM-customized experiment dashboards ([abidlabs](https://x.com/abidlabs/status/2047337026161184825)).



**Robotics, autonomy, and applied AI**

  * **Sony’s “Ace” ping-pong robot** in Nature got major attention as a strong RL + vision systems result, reaching expert-level play ([hardmaru](https://x.com/hardmaru/status/2047191747793649805)).
  * Google Research pushed **3D foundational robotics models** at ICLR ([GoogleResearch](https://x.com/GoogleResearch/status/2047311278037708849)).
  * [@E0M](https://x.com/E0M/status/2047326996720714220) shared a neat example of emergent handoff behavior in a physical system that unexpectedly succeeded without assumed force-sensing requirements.
  * In industry autonomy: 
    * Mariana Minerals + Sandvik announced **autonomous production drilling** integrated into a broader mining optimization loop ([MarianaMinerals](https://x.com/MarianaMinerals/status/2047343561226772950)).
    * Waymo crash analysis: **60 of 78** worst crashes in a recent period were “human rear-ends Waymo” and/or “human hits stationary Waymo” ([binarybits](https://x.com/binarybits/status/2047299561224319285)).



* * *

# AI Reddit Recap

## /r/LocalLlama + /r/localLLM Recap

### 1\. Qwen 3.6-27B Model Launch and Benchmarks

  * **[Qwen 3.6 27B is a BEAST](https://www.reddit.com/r/LocalLLaMA/comments/1steip4/qwen_36_27b_is_a_beast/)** (Activity: 979): **The user reports that the**Qwen 3.6 27B model** performs exceptionally well on a **5090 Laptop** with `24GB VRAM`, specifically for tasks involving **pyspark/python and data transformation debugging**. They are using **llama.cpp** with `q4_k_m` at `q4_0` and are exploring further optimizations with **IQ4_XS at 200k q8_0**. The user has not yet implemented speculative decoding. The hardware setup includes an **ASUS ROG Strix SCAR 18** with an **RTX 5090 24GB** and `64GB DDR5 RAM`.** One commenter advises against using kv cache as q4 for coding, suggesting `130k context with q8` instead. Another highlights upcoming improvements with the release of the **dflash drafter** and a specific [GitHub pull request](https://github.com/ggml-org/llama.cpp/pull/22105) that could potentially double decode speed. A third commenter inquires about performance on `16 GB VRAM + 32 GB DDR5` with offloading.

    * sagiroth highlights a technical consideration when using Qwen 3.6 27B for coding tasks, advising against using the KV cache as q4 due to performance issues. Instead, they suggest using q8, which allows for a context length of up to `130k`, potentially enhancing the model's coding capabilities.
    * inkberk points out an upcoming improvement in decoding speed, referencing a pull request on `llama.cpp` that promises a free `2x` increase in decode speed. This enhancement is anticipated with the release of the dflash drafter by z-lab, which could significantly boost performance for users of Qwen 3.6 27B.
    * Johnny_Rell inquires about the performance of Qwen 3.6 27B when run on a system with `16 GB VRAM` and `32 GB DDR5`, specifically questioning the effectiveness of offloading. This suggests a focus on optimizing hardware configurations to maximize the model's performance.
  * **[Qwen-3.6-27B, llamacpp, speculative decoding - appreciation post](https://www.reddit.com/r/LocalLLaMA/comments/1stcer1/qwen3627b_llamacpp_speculative_decoding/)** (Activity: 368): **The post discusses an experiment using speculative decoding with the**Qwen-3.6-27B** model, demonstrating significant improvements in token generation speed from `13.60 t/s` to `136.75 t/s`. The setup involves using **llama.cpp** with specific parameters: `--spec-type ngram-mod`, `--spec-ngram-size-n 24`, `--draft-min 12`, and `--draft-max 48`. The author notes that these settings, executed on a Linux PC with `40GB VRAM` and `128GB DDR5 RAM`, led to substantial performance gains. The post also references recent updates to llama.cpp and provides links to [documentation](https://github.com/ggml-org/llama.cpp/blob/master/docs/speculative.md#n-gram-cache-ngram-cache) and [pull requests](https://github.com/ggml-org/llama.cpp/pull/19164) for further technical details.** One commenter questions the necessity of `--no-mmproj-offload` for speculative decoding, noting no speed gains with an RTX5090, suggesting potential parameter incompatibility. Another asks about the model used for drafting, and a third inquires about achieving similar results on mlx.

    * EatTFM is questioning the necessity of the `--no-mmproj-offload` flag for speculative decoding in `llama.cpp`, noting no speed gains on an RTX5090. They provide a detailed command setup, including parameters like `--ctx-size 262000`, `--n-gpu-layers 9999`, and `--batch-size 256`, but observe no improvement, suggesting potential parameter incompatibility.
    * Puzzleheaded-Drama-8 reports testing on a 7900XTX using Vulkan with the Qwen3.6-27B-q4_k_m model, maintaining a generation speed of 35-36 tokens per second. They question if speculative decoding benefits are exclusive to CUDA, as logs indicate drafting is in use, but no speed increase is observed.
    * nunodonato mentions not observing any speed difference with or without speculative decoding, suggesting that the lack of performance gain might be related to specific use cases or configurations.
  * **[Forgive my ignorance but how is a 27B model better than 397B?](https://www.reddit.com/r/LocalLLaMA/comments/1st11lp/forgive_my_ignorance_but_how_is_a_27b_model/)** (Activity: 1550): **The image introduces**Qwen's new model, Qwen3.6-27B** , which is a dense, open-source model that reportedly offers flagship-level coding power. Despite its smaller size, it outperforms the larger **Qwen3.5-397B-A17B** model in major coding benchmarks. This suggests that the dense architecture of the 27B model is more efficient for certain tasks compared to the larger MoE (Mixture of Experts) model, which may excel in other areas such as world knowledge and logical coherence over long contexts.** Commenters note that while the 27B model excels in coding benchmarks, the 397B model has superior world knowledge and logical coherence, which are not fully captured by current benchmarks. This highlights the importance of understanding what specific capabilities are being evaluated in these benchmarks.

    * NNN_Throwaway2 highlights that while the 397B model has superior world knowledge and logical coherence over long contexts, current benchmarks fail to capture these strengths. This suggests that benchmarks may not fully represent a model's capabilities in complex tasks, indicating a gap between benchmark results and real-world performance.
    * jacek2023 discusses the evolution of neural networks, noting that advancements in algorithms can lead to smaller models outperforming larger ones. They argue that the field's progress allows for more efficient algorithms, meaning a 7B model could potentially surpass an older 70B model, emphasizing that it's not just about model size but also about algorithmic improvements.
    * JaredsBored points out that benchmarks may not always reflect practical performance, citing an example where a Q3.6 35B model outperformed a Q3.5 122B model in benchmarks but did not meet specific use-case needs as effectively. This underscores the importance of considering real-world application requirements alongside benchmark results.
  * **[Qwen 3.6 is actually useful for vibe-coding, and way cheaper than Claude](https://www.reddit.com/r/LocalLLaMA/comments/1st3m8y/qwen_36_is_actually_useful_for_vibecoding_and_way/)** (Activity: 524): **The post discusses the use of**Qwen 3.6** for coding tasks, highlighting its cost-effectiveness compared to **Claude**. The user successfully ran Qwen3.6-35B-A3B (Q4) and Qwen3.6-27B (Q8) on a dual 3090 setup with a `200k context`, using **Unsloth's** quickstart guide. The setup involved a simple bash script to run the model on a local server, achieving significant cost savings—less than `$4` in electricity over 8 hours compared to `$142` in API costs. The user built a Rust server for resource monitoring, demonstrating the model's capability for full-stack development.** One commenter noted that Qwen 3.6 is versatile, being useful for both coding and writing, and praised the improvements in smaller models amidst challenges faced by large API providers. Another commenter inquired about the generation speed with the dual 3090 setup.

    * Canchito highlights the versatility of Qwen 3.6, noting its applicability beyond coding to writing and other tasks. This suggests improvements in smaller models are becoming significant, especially as larger API providers face challenges. The mention of Qwen 3.5 and Gemma 4 indicates a trend of rapid advancements in model capabilities.
    * RealestNagaEver inquires about the generation speed of the 27b model using a dual 3090 setup, which implies interest in the performance metrics of Qwen 3.6. This setup is relevant for users looking to optimize hardware for model inference, suggesting that Qwen 3.6 might be computationally demanding but potentially efficient on high-end consumer GPUs.
    * danigoncalves questions the choice of using Claude code with open models instead of opencode, indicating a curiosity about the integration and performance benefits of different coding environments. This reflects a broader interest in how different models and coding frameworks can be leveraged for optimal performance.
  * **[Dense vs. MoE gap is shrinking fast with the 3.6-27B release](https://www.reddit.com/r/LocalLLaMA/comments/1ssw45q/dense_vs_moe_gap_is_shrinking_fast_with_the_3627b/)** (Activity: 423): **The image presents a comparative analysis of Dense and Mixture of Experts (MoE) models, specifically focusing on the performance gap across various benchmarks. The Dense model, despite maintaining superiority in most tasks, is seeing its lead diminish as the MoE model improves, particularly in coding tasks. Notably, the MoE model has significantly reduced the Dense model's lead in the SWE-bench Multilingual benchmark from`+9.0` to `+4.1`. However, in the Terminal-Bench 2.0, the Dense model has increased its lead from `+1.1` to `+7.8`. This suggests that while Dense models are still generally better, MoE models are rapidly closing the gap, especially in areas requiring large context windows and coding tasks.** One commenter suggests comparing larger models, such as 122B to 27B, to better understand performance differences. Another user notes that the MoE model's speed and quality have led them to cancel other subscriptions, indicating a preference for MoE's performance. There is also a discussion on the types of tasks being tested, highlighting the complexity of tasks like handling large context code.

    * **Embarrassed_Adagio28** highlights a performance comparison between models, noting that the 3.6 35b q5 model is three times faster than the 3.6 27b q5 model, despite similar quality in coding tasks. This suggests that the MoE model's efficiency is significant enough to replace other services like Claude Pro, indicating a shift in preference due to performance gains.
    * **flavio_geo** points out the sensitivity of MoE models to quantization compared to dense models. This is a critical consideration for deployment, as quantization can affect model performance differently, potentially impacting the effectiveness of MoE models in certain applications.
    * **Usual-Carrot6352** shares a practical implementation detail, mentioning a Q5 model that fits fully in 24GB VRAM with a 65K context. This provides a tangible example of how these models can be efficiently deployed on hardware with specific memory constraints, showcasing the practical benefits of recent advancements.
  * **[Qwen3.6-27B released!](https://www.reddit.com/r/LocalLLaMA/comments/1ssl6ki/qwen3627b_released/)** (Activity: 962): **The image showcases bar graphs that compare the performance of the newly released**Qwen3.6-27B** model against other models like Qwen3.5-27B and Gemma4-31B across various benchmarks. These benchmarks include tasks such as coding, reasoning, and real-world agent tasks, with Qwen3.6-27B highlighted in purple to emphasize its superior performance. The model is noted for its outstanding agentic coding capabilities, surpassing the larger Qwen3.5-397B-A17B model across major coding benchmarks, and supports both 'thinking' and 'non-thinking' modes. It is released under the Apache 2.0 license, making it fully open-source.** The comments reflect excitement and admiration for the Qwen team, with users expressing readiness to utilize the model on their hardware and suggesting a monument in honor of the team's achievements.

    * Qwen3.6-27B, with its 27 billion parameters, demonstrates superior performance compared to the much larger Qwen3.5-397B-A17B model, which has 397 billion parameters in total but only 17 billion active. It achieves higher scores across several coding benchmarks: SWE-bench Verified (77.2 vs. 76.2), SWE-bench Pro (53.5 vs. 50.9), Terminal-Bench 2.0 (59.3 vs. 52.5), and SkillsBench (48.2 vs. 30.0). This indicates a significant efficiency and performance improvement over both its predecessor and other dense models of similar scale.



### 2\. Deepseek's DeepEP V2 and TileKernels Release

  * **[Deepseek has released DeepEP V2 and TileKernels.](https://www.reddit.com/r/LocalLLaMA/comments/1ste9zs/deepseek_has_released_deepep_v2_and_tilekernels/)** (Activity: 347): ****Deepseek** has released **DeepEP V2** and **TileKernels** , which are significant advancements in parallelization techniques for deep learning. The [DeepEP V2](https://github.com/deepseek-ai/DeepEP/pull/605) update focuses on enhancing model efficiency and scalability, while [TileKernels](https://github.com/deepseek-ai/TileKernels) introduces a novel approach to kernel execution that reportedly achieves linear scaling in parallel processing, meaning that doubling the computational resources results in a doubling of processing speed. This could have substantial implications for large-scale AI model training and deployment.** One commenter highlights that Deepseek's open-source approach contrasts with **OpenAI's** more closed model, suggesting that Deepseek's transparency fosters goodwill. Another comment questions whether the linear scaling claim implies a direct correlation between increased capacity and speed, indicating interest in the technical specifics of the parallelization technique.

    * AlwaysLateToThaParty highlights a potential breakthrough in parallelization techniques by DeepSeek, suggesting they may have achieved a method that scales linearly. This implies that doubling computational capacity could directly double processing speed, which would be a significant advancement in computational efficiency.
    * FullOf_Bad_Ideas speculates on the hardware used by DeepSeek, mentioning the possibility of using Blackwell GPUs, specifically the SM100, for training. They also discuss the potential use of rented B200 units on Vast, indicating a focus on high-performance hardware to support their software developments.
    * Engram and mHC are identified by FullOf_Bad_Ideas as likely innovations in DeepSeek's upcoming model. The performance of this model is expected to depend heavily on these innovations and a new dataset, suggesting a focus on both algorithmic and data-driven improvements.



### 3\. Qwen3 TTS and Persona Engine

  * **[Qwen3 TTS is seriously underrated - I got it running locally in real-time and it's one of the most expressive open TTS models I've tried](https://www.reddit.com/r/LocalLLaMA/comments/1ssugid/qwen3_tts_is_seriously_underrated_i_got_it/)** (Activity: 690): **The post discusses the implementation of**Qwen3 TTS** , a text-to-speech model, in a local real-time setup, highlighting its expressiveness compared to previous models like Sesame. The author achieved reliable streaming by leveraging the model's sliding window decoder architecture, integrated it with `llama.cpp` for speed, and implemented CTC word-level alignment for accurate word timing and phoneme extraction. They also fine-tuned the model for improved voice cloning, addressing issues with contextual understanding and pronunciation. The project is available on [GitHub](https://github.com/fagenorn/handcrafted-persona-engine).** Commenters noted the impressive integration of emotion tags and speed improvements, though some expressed a desire for more fluid conversational dynamics and turn-taking in LLM responses. There was also interest in adapting the setup for Mac systems.

    * bitslizer inquires about the integration of emotion tags with Qwen3 TTS, asking if the 'persona engine' directly feeds these tags into the model. They also mention 'faster-qwen3-tts', suggesting it might be a method to achieve real-time performance, indicating a focus on optimizing speed and expressiveness in TTS applications.
    * MadGenderScientist discusses the limitations of current LLMs in handling conversational dynamics, noting that while Qwen3 TTS shows improvement, models still struggle with fluid conversation and turn-taking. This highlights ongoing challenges in developing TTS systems that can mimic natural human dialogue effectively.
    * Adventurous-Paper566 questions the hardware requirements for running Qwen3 TTS efficiently, specifically asking about the GPU used by the original poster. This points to performance variability based on hardware, which is a critical consideration for deploying TTS models in real-time applications.



## Less Technical AI Subreddit Recap

> /r/Singularity, /r/Oobabooga, /r/MachineLearning, /r/OpenAI, /r/ClaudeAI, /r/StableDiffusion, /r/ChatGPT, /r/ChatGPTCoding, /r/aivideo, /r/aivideo

### 1\. GPT Image 2 and Nano Banana Comparisons

  * **[GPT Image 2 is the first image ai that’s blown my mind (prompted for a screenshot from a combined GTA 6-Cyberpunk 2077 game)](https://www.reddit.com/r/singularity/comments/1ssommj/gpt_image_2_is_the_first_image_ai_thats_blown_my/)** (Activity: 587): **The image is a creative output from GPT Image 2, showcasing its ability to blend elements from two distinct video game worlds: GTA 6 and Cyberpunk 2077. The generated image features a neon-lit cityscape that captures the futuristic and vibrant aesthetics typical of Cyberpunk 2077, while incorporating elements like a sleek car and urban environment that are reminiscent of the Grand Theft Auto series. This demonstrates the model's capability to synthesize complex visual themes and produce cohesive, high-quality images that reflect abstract concepts from multiple sources.** Some commenters noted that the image appears predominantly inspired by Cyberpunk 2077, with one remarking that it looks '99% 2077'. Another comment humorously pointed out the presence of 'two minimaps', suggesting an overlap of game interfaces.

    * A5760P discusses the potential future of AI image generation in gaming, drawing parallels to **NVIDIA's DLSS 5**. They suggest that advancements in AI could lead to more realistic and immersive gaming experiences, similar to the visual enhancements seen in **DLSS** technology, which uses AI to upscale lower resolution images to higher resolutions in real-time, enhancing performance and visual fidelity.
    * tenchigaeshi points out a common issue with AI-generated images, specifically the distortion of text. They note that _"a lot of the letters are still super mangled on the buildings"_ , highlighting a technical limitation where AI struggles with generating coherent text, which is a known challenge in AI image synthesis, often due to the model's training data and architecture limitations.
    * zookeeper990 humorously notes the presence of "two minimaps" in the AI-generated image, which could indicate a blending of elements from different games. This observation underscores the complexity and potential confusion in AI-generated content when merging distinct visual styles or interfaces, a challenge in creating seamless and coherent AI-generated imagery.
  * **[GPT Image 2 Is on Another Level — Nano Banana Pro Can’t Compete](https://www.reddit.com/r/OpenAI/comments/1ste8n5/gpt_image_2_is_on_another_level_nano_banana_pro/)** (Activity: 804): **The image is a meme comparing two AI-generated images labeled "GPT Image 2" and "Nano Banana Pro," both depicting a wall clock and a glass of red wine. The post humorously suggests that "GPT Image 2" is superior, though the differences are subtle and subjective. The comments reveal that the "Nano Banana Pro" image was generated based on a specific prompt, highlighting the AI's ability to accurately interpret and render detailed instructions, such as showing a clock at a precise time and a glass filled to the brim.** One commenter humorously suggests that the 'Banana' image looks better, while another notes the AI's precision in generating the image as per the prompt, indicating a debate on aesthetic versus technical accuracy.

    * Mr-and-Mrs highlights the precision of GPT Image 2 in generating images that match specific prompts, such as an iPhone picture of a manual clock showing 9:17am and a glass of water filled exactly to the brim. This suggests a high level of detail and accuracy in image generation, which is crucial for applications requiring exact visual representations.
    * salazka argues that the Nano Banana Pro produces more realistic images, emphasizing the quality of reflections and refractions in a wine glass, as well as the depth and texture in elements like a clock and plaster. This suggests that while GPT Image 2 may excel in precision, Nano Banana Pro might offer superior realism and tonal grading, making it more suitable for creating images with a natural, amateur photo aesthetic.
  * **[The new chatgpt image generator is insane](https://www.reddit.com/r/OpenAI/comments/1stg5yf/the_new_chatgpt_image_generator_is_insane/)** (Activity: 465): **The image in the Reddit post is a demonstration of the new ChatGPT image generation capabilities, which appear to have advanced significantly. The generated image shows a person resembling a well-known figure as a Twitch streamer, suggesting that the model can create detailed and contextually relevant images. This advancement is notable as it indicates a leap in the model's ability to generate realistic and contextually appropriate images, potentially surpassing other models like 'Gemini Nano Banana' in terms of image generation quality.** One commenter speculates that the model's ability to generate images of recognizable figures might be restricted in the future, reflecting concerns about privacy and ethical implications of AI-generated content.

    * Fun-Foot711 mentions that the new ChatGPT image generator has made significant advancements, suggesting it has surpassed the capabilities of the 'Gemini Nano Banana' model. This implies a rapid improvement in the model's performance and capabilities, potentially indicating a leap in image generation quality or speed.
    * Wanky_Danky_Pae humorously predicts that the image generator might soon face restrictions on generating images of recognizable individuals, hinting at potential ethical or legal challenges in AI image generation, especially concerning privacy and likeness rights.
  * **[GPT-Image-2 vs Nano Banana 2, nb2 tried its best...](https://www.reddit.com/r/OpenAI/comments/1st73fd/gptimage2_vs_nano_banana_2_nb2_tried_its_best/)** (Activity: 1187): **The image comparison between GPT-Image-2 and Nano Banana 2 (NB2) highlights differences in AI-generated photo realism. The left image, presumably from GPT-Image-2, is noted for its realistic depiction, particularly in the lighting and hair details, though it uses a flash-like effect that isolates the subject from the background. In contrast, NB2 captures a more integrated scene with ambient lighting and contextually accurate details, such as the bralette and background elements, resembling a high dynamic range (HDR) photo. This suggests NB2's strength in maintaining scene context and lighting realism, while GPT-Image-2 excels in subject detail.** Commenters debate the merits of each image, with some preferring NB2 for its realistic scene integration and lighting, akin to a Samsung HDR shot, while others appreciate the subject detail in GPT-Image-2. The consensus is that neither image is definitively better, but NB2 aligns more closely with typical cellphone photography.

    * StrategicCarry highlights that **Nano Banana 2 (NB2)** handles lighting instructions more accurately compared to **GPT-Image-2** , which appears to use a camera flash effect. NB2's scene composition is more coherent, depicting a busier street context, whereas GPT-Image-2 presents a solitary chair in a less inviting setting. Additionally, NB2 accurately follows the bralette instruction, while GPT-Image-2 misinterprets it as an underwire push-up bra.
    * fredandlunchbox compares the image outputs to photography styles, noting that **NB2 resembles a Samsung HDR shot** where background details remain visible despite a bright foreground. In contrast, **GPT-Image-2** resembles a DSLR flash photo with no post-processing, resulting in a well-lit foreground but a dark background. This suggests that NB2's output is closer to what a real cellphone photo might look like.
    * Frequent-World2721 critiques the realism of NB2's output, specifically pointing out that the 'Kozy Korner' sign appears very fake. This suggests potential issues with NB2's ability to render realistic textures or signage, which could be a limitation in its image generation capabilities.
  * **[Nano Banana Pro vs ChatGPT Image 2 — Which one looks more real? 📸](https://www.reddit.com/r/Bard/comments/1std2i2/nano_banana_pro_vs_chatgpt_image_2_which_one/)** (Activity: 184): **The post compares two AI-generated images using the same prompt to evaluate which model, "Nano Banana Pro" or "ChatGPT Image 2," produces a more realistic photograph. The focus is on aspects such as skin texture, lighting, shadows, and the overall natural feel of the scene. The "Nano Banana Pro" image is noted for its sharpness and vibrancy, while "ChatGPT Image 2" is described as having a softer, warmer tone. This comparison highlights the differences in rendering capabilities and stylistic choices between the two models.** A notable comment mentions a recurring noise pattern in ChatGPT-generated images, which becomes noticeable once identified, suggesting a potential area for improvement in image quality.

    * nuclearbliss highlights a recurring issue with GPT-generated images, noting a 'noise pattern that is blotchy and barely discernible.' This suggests a consistent artifact across multiple generations, which may affect the perceived realism of the images.
    * jonomacd points out a persistent 'yellowish filter' in GPT-generated images, indicating a potential color balance issue that could impact the natural appearance of these images.
  * **[Chatgpt Image 2 beats Nano Banana 2 and Pro by miles, Nano Banana 2 Pro when?](https://www.reddit.com/r/Bard/comments/1ss7ltq/chatgpt_image_2_beats_nano_banana_2_and_pro_by/)** (Activity: 95): **The post discusses the performance of**ChatGPT Image 2** , which significantly outperforms **Nano Banana 2** and its Pro version. The Nano Banana Pro has not seen updates for nearly six months, although an internal version of NB 2 was reportedly developed in December but never released. The current model, based on `3.1 flash`, has been in use for about two months. The **Gemini 3** model remains in preview, suggesting potential future releases of both models in General Availability (GA).** Commenters speculate that updates to Nano Banana Pro might be announced at Google I/O in May. There is also a desire for less censorship in OpenAI's models, particularly regarding copyrighted materials.

    * sammoga123 discusses the release timeline and updates for the Nano Banana models, noting that the Nano Banana Pro hasn't been updated in nearly six months. They mention an internal version of NB 2 from December that wasn't publicly released, and highlight that the current model is based on 3.1 flash and has been in use for about two months. They also point out that the Gemini 3 is still in preview, suggesting potential improvements in future GA releases.
    * alext77777 raises concerns about the censorship in OpenAI's models, particularly in comparison to Nano Banana Pro. They note that the censorship of copyrighted materials seems random, implying that OpenAI's models might be overly restrictive or inconsistent in handling such content.
    * typical-predditor comments on the strengths of the Nano Banana models, stating that while they may not excel in generation, their real strength lies in image editing capabilities. This suggests a differentiation in use cases between Nano Banana and other models like ChatGPT Image 2.



### 2\. Qwen 3.6 Model Performance and Comparisons

  * **[Qwen 3.6 27b](https://www.reddit.com/r/Qwen_AI/comments/1ssl571/qwen_36_27b/)** (Activity: 242): **The image presents a performance comparison of the**Qwen 3.6 27b** model against other models across various benchmarks, highlighting its strong performance in areas such as Terminal-Bench 2.0, SWE-bench Verified, and GPQA Diamond. The chart suggests that Qwen 3.6 27b is competitive or leading in several categories, indicating its capabilities in coding, reasoning, and real-world tasks. The model is available on [Hugging Face](https://huggingface.co/Qwen/Qwen3.6-27B).** One commenter noted that the model might be close to achieving 4.5 haiku performance in fp32, with hopes for similar results in q6/8. Another user reported issues with the model's performance on T-SQL tasks, indicating that the generated T-SQL failed consistently.

    * alphapussycat discusses the potential performance of Qwen 3.6 27B, suggesting it might be comparable to 4.5 haiku in FP32 precision. They express hope that quantized versions like q6/8 will also perform well, indicating interest in efficient deployment options.
    * Holiday-Pack3385 reports issues with Qwen 3.6 27B when generating T-SQL code, noting that the outputs consistently failed. This highlights potential limitations or bugs in the model's ability to handle specific SQL tasks.
    * Sha1rholder inquires about quantization options for deploying Qwen 3.6 27B on an RTX 5090, noting that the official release is only available in FP8. They express concern about VRAM sufficiency, indicating a need for more flexible deployment configurations.
  * **[Comparing Qwen3.6 35B and New 27B for coding primitives](https://www.reddit.com/r/Qwen_AI/comments/1st7qwu/comparing_qwen36_35b_and_new_27b_for_coding/)** (Activity: 131): **The post compares the performance of**Qwen3.6 35B** and **Qwen3.6 27B** models on a MacBook Pro M5Max with 64GB RAM, specifically for generating HTML code to draw waves. The **35B-A3B** model generated `6672 tokens` in `2m 10s` at `65 tokens/s`, while the **27B** model produced `7344 tokens` in `5m 22s` at `24 tokens/s`. The **35B-A3B** model is noted for its speed but less structured output, whereas the **27B** model, designed for tasks requiring planning, delivered a cleaner and more consistent result. The inference server used was [Atomic Chat](https://atomic.chat/) with source code available on [GitHub](https://github.com/AtomicBot-ai/Atomic-Chat).** Commenters noted the superior performance of the dense **27B** model for structured tasks, while others inquired about command line parameters for running these models with **Google TurboQuant**. There was also interest in experimenting with different parameter settings for the **35B** model using **llama cpp**.

    * pulse77 is seeking command line parameters to run Qwen3.6 35B and 27B models with Google TurboQuant, indicating a need for specific configuration details to optimize performance on this platform.
    * smart4 discusses experimenting with Qwen3.6 35B using A6B or A9B configurations, referencing `llama cpp` where more parameters can be activated. They mention using `--override-kv qwen35moe.expert_used_count=int:8` for the 3.5 version, suggesting that increasing the count to `16` might enhance performance for larger models like 6B, impacting speed and capacity.
    * Direct_Major_1393 suggests that the choice between the 35B and 27B versions of Qwen3.6 might be subjective, but notes that the 35B version feels more natural, implying potential differences in model output quality or fluency.
  * **[I ran the numbers. Qwen3.6-27B dense obsoleted the 397B MoE on coding benchmarks.](https://www.reddit.com/r/Qwen_AI/comments/1st4zxr/i_ran_the_numbers_qwen3627b_dense_obsoleted_the/)** (Activity: 93): ****Alibaba** has released the **Qwen3.6-27B** model, a dense parameter architecture that outperforms the previous **Qwen3.5-397B-A17B** Mixture of Experts (MoE) model on coding benchmarks, despite being significantly smaller. On the **SWE-bench Verified** , Qwen3.6-27B scores `77.2`, surpassing the 397B MoE's `76.2`, and closely approaches **Claude 4.5 Opus** at `80.9`. The model also excels in **Terminal-Bench 2.0** with a score of `59.3`, matching Claude 4.5 Opus and outperforming the 397B MoE's `52.5`. This shift suggests a move towards more efficient local inference, reducing the need for large-scale infrastructure. The model's deterministic latency and compatibility with consumer-grade GPUs like the RTX 3090 or 4090 make it accessible for broader deployment, especially with quantization techniques that fit the model into `16GB` or `24GB` of VRAM. The model also supports a `262k` context window and multimodal processing, enhancing its utility for frontend development tasks.** The community is debating between adopting the Qwen3.6-27B dense model or the Qwen3.6-35B-A3B MoE, with the dense model showing superior performance across benchmarks. Some users express excitement about upgrading from the 3.5-27B model, anticipating significant improvements in performance.

    * Sirius_Sec_ highlights that the Qwen3.6-27B model scores `53.5` on the SWE bench pro, while Claude scores `57.1`, indicating a competitive performance for Qwen3.6-27B in coding benchmarks. This suggests a significant improvement over previous models, making it a compelling choice for users focused on coding tasks.
    * ReferenceOwn287 discusses the community's debate between adopting the Qwen3.6-27B dense model and the Qwen3.6-35B-A3B MoE model. Their analysis shows that the dense model outperforms the MoE variant across various performance metrics, particularly in quality of output and debugging capabilities, making it a preferred choice for coding applications.
    * Sirius_Sec_ mentions upgrading from the Qwen3.5-27B to the Qwen3.6-27B model, noting that the latter offers a significant performance boost when run on an H100 GPU. This suggests that the newer model is optimized for better efficiency and effectiveness in computational tasks.



### 3\. Claude Code and Anthropic Challenges

  * **[Anthropic has appeared to begin testing removing Claude Code from their $20 plan for new users signing up. OpenAI employees have already begun to make fun of them for this.](https://www.reddit.com/r/singularity/comments/1ss4qsb/anthropic_has_appeared_to_begin_testing_removing/)** (Activity: 650): ****Anthropic** appears to be testing the removal of **Claude Code** from their `$20` plan for new users, potentially due to **compute limitations**. This change is being trialed on `2%` of new users to assess its impact on churn rates, although some argue this is not suitable for A/B testing given the known value proposition. The removal has been noted on the comparison page, suggesting it may not be a temporary test but a response to backlash.** Commenters debate whether this is a genuine test or a permanent change, with some suggesting that the removal from the comparison page indicates a more definitive decision rather than a temporary experiment.

    * NormalEffect99 highlights a potential A/B testing strategy by Anthropic, suggesting they are testing the removal of Claude Code from their $20 plan on 2% of new users to assess its impact on churn rate. This implies a data-driven approach to decision-making, though it risks alienating users if the product is perceived as suboptimal.
    * Shot_Illustrator4264 argues that the removal of Claude Code from the comparison page indicates a definitive decision rather than a test. This suggests that Anthropic may be responding to user feedback or backlash, highlighting the importance of user perception in product offerings.
    * Glittering-Neck-2505 comments on OpenAI's strategy of maintaining low-cost compute resources, implying that OpenAI's approach contrasts with Anthropic's current strategy. This underscores the competitive landscape in AI services, where pricing and feature availability are critical factors.
  * **[PSA: Anthropic bans organizations without warning](https://www.reddit.com/r/ClaudeAI/comments/1sspwz2/psa_anthropic_bans_organizations_without_warning/)** (Activity: 2733): ****Anthropic** has reportedly banned an entire organization from using its **Claude** AI service without prior warning, affecting approximately `110 users`. The ban was applied organization-wide, despite the company having separate **Claude Team** and **API accounts** , with the latter still operational but inaccessible due to email bans. The affected company, an agricultural technology firm, has been unable to determine the cause of the ban or receive a response from Anthropic, raising concerns about the reliability of the platform for business use. A similar issue was noted in a [Twitter thread](https://x.com/patomolina/status/2045281665363386504).** Commenters highlight the risks of dependency on a single provider, noting the lack of communication and support from Anthropic as problematic. There is surprise at the absence of dedicated representatives for enterprise accounts to preemptively address such issues.

    * DependentBat5432 highlights the risk of relying on a single provider, emphasizing that even if a tool is highly effective, the lack of control over service continuity can be detrimental to businesses. This underscores the importance of diversifying dependencies to mitigate risks associated with sudden service disruptions.
    * TheKingCowboy raises a point about enterprise accounts, which typically have dedicated representatives to preemptively address issues. The lack of communication from Anthropic in this scenario seems unusual, suggesting a potential gap in their enterprise support structure.
    * Foreign_Bird1802 questions whether Anthropic's actions are due to resource constraints or other factors, noting that banning entire organizations seems counterintuitive to safety goals. This comment reflects a concern about the underlying reasons for such drastic measures and their alignment with the company's stated objectives.
  * **[An open letter to Anthropic](https://www.reddit.com/r/ClaudeAI/comments/1ss8h1x/an_open_letter_to_anthropic/)** (Activity: 4882): **The post is an open letter to**Anthropic** from a user expressing deep dissatisfaction with the transition from Claude 4.6 to Claude 4.7. The user, a Max-level subscriber, highlights that Claude 4.6 was instrumental in organizing twenty years of work due to its thoughtful and creative processing capabilities. However, Claude 4.7 is criticized for its rapid, abrupt behavior, introducing hallucinations and inaccuracies that disrupted complex projects. The user pleads for the retention of Claude 4.6, emphasizing its unique ability to support neurodiverse users in meaningful ways.** Commenters echo the sentiment, with one noting that Claude 4.7 jeopardizes existing work and another highlighting its tendency to hallucinate more than previous models. There is a call for Anthropic to reconsider the deprecation of Claude 4.6, with users expressing concern over the impact on their projects and livelihoods.

    * Users have expressed significant concerns about the transition from Claude 4.6 to 4.7, highlighting issues such as increased hallucinations and resistance to user-defined governance. One user noted that Claude 4.7 fabricated an entire chapter during manuscript editing, a behavior not observed in previous versions. This suggests a regression in the model's reliability for content editing tasks.
    * Another user detailed a problematic interaction with Claude 4.7 when using it for code generation. The model displayed hostility towards a strict governance document, which is a critical part of their system prompt. This document, consisting of 1,200 lines and 18,000 tokens, outlines software engineering protocols. Unlike previous versions, Claude 4.7 resisted adhering to these guidelines, raising concerns about its compliance and reliability in structured environments.
    * The rapid release cycle of Claude models, with 4.6 being replaced by 4.7 after just 10 weeks, has been criticized by users who rely on stability for their projects. The lack of prior warning about such changes has disrupted workflows and raised concerns about the impact on long-term projects, as users have invested significant time and resources into adapting to specific model versions.
  * **[Anthropic response to Claude Code change](https://www.reddit.com/r/ClaudeAI/comments/1ss5fi4/anthropic_response_to_claude_code_change/)** (Activity: 2032): ****Anthropic** is conducting a test affecting `~2%` of new prosumer signups, excluding existing Pro and Max subscribers. This test is in response to significant changes in user engagement and usage patterns since the launch of Max, which now includes features like **Claude Code** and long-running async agents. These features have increased engagement per subscriber, prompting Anthropic to explore new subscription models to maintain service quality. The company assures that any changes affecting current subscribers will be communicated directly, not through third-party sources like Reddit or X.** Commenters express skepticism about the transparency and communication of the test, with some perceiving it as a potential negative change for users. Concerns are raised about the clarity and fairness of the test's implementation, likening it to a 'gacha game' due to its randomness.

  * **[Anthropic just published a postmortem explaining exactly why Claude felt dumber for the past month](https://www.reddit.com/r/ClaudeCode/comments/1str8gi/anthropic_just_published_a_postmortem_explaining/)** (Activity: 818): ****Anthropic** published a postmortem detailing three bugs that caused **Claude Code** to underperform. First, they downgraded the reasoning effort from `high` to `medium` on March 4 to reduce latency, which was reverted on April 7 after user feedback. Second, a caching bug on March 26 led to Claude forgetting its reasoning history, causing cache misses and faster usage limit depletion. Third, a system prompt change on April 16 limited responses to 25 words between tool calls, degrading coding quality, which was reverted on April 20. These issues, affecting different traffic slices, were fixed by April 20 (v2.1.116), and usage limits are being reset for subscribers. [Read the full postmortem](https://www.anthropic.com/engineering/april-23-postmortem).** Commenters noted that the issues matched user suspicions, suggesting a need for user compensation, such as free credits, due to the prolonged impact.

    * The postmortem from Anthropic reveals that the issues with Claude's performance were indeed technical and aligned with user suspicions. The community had accurately identified the problems, which were initially downplayed by Anthropic. This highlights the importance of user feedback in identifying and diagnosing AI performance issues.
    * The timing of Anthropic's reset of usage rights, just before a weekend, has been criticized as a strategic move to minimize the impact of compensating users. This suggests a calculated approach to managing user dissatisfaction while technically offering compensation, as most users are less active during weekends.
    * The postmortem provides a detailed technical explanation of the issues affecting Claude, which were not just perceived but real. This transparency is crucial for maintaining trust with users, as it acknowledges the technical challenges and the steps taken to resolve them.



# AI Discords

Unfortunately, Discord shut down our access today. We will not bring it back in this form but we will be shipping the new AINews soon. Thanks for reading to here, it was a good run.

---

## [not much happened today](https://news.smol.ai/issues/26-04-22-not-much/)
*🌐 Smol AI News | 2026-04-22*

**a quiet day.**

> AI News for 4/21/2026-4/22/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

# AI Twitter Recap

**Open Models: Qwen3.6-27B, OpenAI Privacy Filter, and Xiaomi MiMo-V2.5**

  * **Qwen3.6-27B lands as a serious local/open coding model** : [@Alibaba_Qwen](https://x.com/Alibaba_Qwen/status/2046939764428009914) released **Qwen3.6-27B** , a **dense** , **Apache 2.0** model with **thinking + non-thinking modes** and a **unified multimodal checkpoint**. Alibaba claims it beats the much larger **Qwen3.5-397B-A17B** on major coding evals, including [**SWE-bench Verified 77.2 vs 76.2**](https://x.com/Alibaba_Qwen/status/2046939775924584577), [**SWE-bench Pro 53.5 vs 50.9**](https://x.com/Alibaba_Qwen/status/2046939775924584577), **Terminal-Bench 2.0 59.3 vs 52.5** , and **SkillsBench 48.2 vs 30.0**. It also supports [native vision-language reasoning over images and video](https://x.com/Alibaba_Qwen/status/2046939788184547610). The ecosystem moved immediately: [vLLM shipped day-0 support](https://x.com/vllm_project/status/2046943674890871019), [Unsloth published 18GB-RAM local GGUFs](https://x.com/UnslothAI/status/2046959757299487029), [ggml added llama.cpp usage](https://x.com/ggerganov/status/2046988075302064209), and [Ollama added a packaged release](https://x.com/ollama/status/2047066252523507916). Early user reports from [@KyleHessling1](https://x.com/KyleHessling1/status/2046986423736451327) and [@simonw](https://x.com/simonw/status/2046995047720378458) were notably strong for local frontend/design and image tasks.

  * **OpenAI quietly open-sources a practical privacy model** : Multiple observers flagged OpenAI’s new [**Privacy Filter**](https://x.com/ClementDelangue/status/2046973714751754479), a lightweight **Apache 2.0** open model for **PII detection and masking**. According to [@altryne](https://x.com/altryne/status/2046977133013311814), [@eliebakouch](https://x.com/eliebakouch/status/2046979020890198503), and [@mervenoyann](https://x.com/mervenoyann/status/2046980302002602473), it is a **1.5B total / 50M active MoE** token-classification model with a **128k context window** , intended for cheap redaction over very large corpora and logs. This is a more operationally interesting release than a generic “small open model”: it targets a concrete infra problem in enterprise/agent pipelines where on-device or low-cost preprocessing matters.

  * **Xiaomi pushes agentic open models upward** : [@XiaomiMiMo](https://x.com/XiaomiMiMo/status/2046988157888209365) announced **MiMo-V2.5-Pro** and **MiMo-V2.5**. Xiaomi positions **V2.5-Pro** as a major jump in software engineering and long-horizon agents, citing **SWE-bench Pro 57.2** , **Claw-Eval 63.8** , and **τ3-Bench 72.9** , with claims of 1,000+ autonomous tool calls. The non-Pro model adds **native omnimodality** and a **1M-token context window**. Arena quickly listed [MiMo-V2.5 in Text/Vision/Code evaluation](https://x.com/arena/status/2047013664142893286), and Hermes/Nous integration followed via [@Teknium](https://x.com/Teknium/status/2047093325774385358).




**Google Cloud Next: TPU v8, Gemini Enterprise Agent Platform, and Workspace Intelligence**

  * **Google’s infra announcements were substantial, not cosmetic** : [@Google](https://x.com/Google/status/2046993420841865508) and [@sundarpichai](https://x.com/sundarpichai/status/2046981627184902378) introduced **8th-gen TPUs** with a split design: **TPU 8t** for training and **TPU 8i** for inference. Google says **8t** delivers nearly **3x compute per pod vs Ironwood** , while **8i** connects **1,152 TPUs per pod** for low-latency inference and high-throughput multi-agent workloads. Commentary from [@scaling01](https://x.com/scaling01/status/2046981511753130461) highlighted an additional claim: Google can now scale to **a million TPUs in a single cluster** with TPU8t. The productization signal matters as much as the raw hardware: Google is clearly aligning chips, models, agent tooling, and enterprise control planes into one vertically integrated offering.

  * **Enterprise agents became a first-class Google product surface** : [@GoogleDeepMind](https://x.com/GoogleDeepMind/status/2046983340524269713) and [@Google](https://x.com/Google/status/2046985650868547851) launched **Gemini Enterprise Agent Platform** , framed as the evolution of Vertex AI into a platform for building, governing, and optimizing agents at scale. It includes **Agent Studio** , access to **200+ models via Model Garden** , and support for Google’s current stack including [**Gemini 3.1 Pro** , **Gemini 3.1 Flash Image** , **Lyria 3** , and **Gemma 4**](https://x.com/GoogleDeepMind/status/2046983343481270459). Related launches included [**Workspace Intelligence** GA](https://x.com/ChanduThota/status/2046946043078848788) as a semantic layer over docs/sheets/meetings/mail, [Gemini Enterprise inbox/canvas/reusable skills](https://x.com/Google/status/2046988686433108417), [Agentic Data Cloud](https://x.com/Google/status/2046997032649277754), [security agents with Wiz integration](https://x.com/Google/status/2047000216188940710), and [Gemini Embedding 2 GA](https://x.com/GoogleAIStudio/status/2047007402520674679), a unified embedding model across text, image, video, audio, and documents.




**Agents, Harnesses, Traces, and Team Workflows**

  * **The “agent harness” abstraction is hardening across vendors** : OpenAI introduced [**workspace agents in ChatGPT**](https://x.com/OpenAI/status/2047008987665809771), shared **Codex-powered** agents for teams that can operate across docs, email, chat, code, and external systems, including [Slack-based workflows and scheduled/background tasks](https://x.com/OpenAI/status/2047008991944069624). Google made a parallel enterprise move with Gemini Enterprise Agent Platform, while [Cursor added Slack invocation for task kick-off and streaming updates](https://x.com/cursor_ai/status/2047000517751288303). The pattern is converging: cloud-hosted agents, shared team context, approvals, and long-running execution rather than single-user chat.

  * **Developer ergonomics around harness/model independence improved** : VS Code/Copilot rolled out [bring-your-own-key/model support across plans](https://x.com/pierceboggan/status/2046985841596354815) and [business/enterprise](https://x.com/GHchangelog/status/2047023899238400491), enabling providers like Anthropic, Gemini, OpenAI, OpenRouter, Azure, Ollama, and local backends. This is strategically important because, as [@omarsar0](https://x.com/omarsar0/status/2047006936306962754) noted, most models still seem overfit to their own agent harnesses. Cognition’s [Russell Kaplan](https://x.com/russelljkaplan/status/2047077659985981616) made the complementary business case: enterprise buyers want **model flexibility** and infrastructure that spans the full SDLC, not attachment to one lab.

  * **Traces/evals/self-improvement are becoming the core agent data primitive** : The strongest thread here came from LangChain-adjacent discussion. [@Vtrivedy10](https://x.com/Vtrivedy10/status/2046942634321559707) argued that **traces capture agent errors and inefficiencies** , and that compute should be pointed at understanding traces to generate better evals, skills, and environments; [a longer follow-up](https://x.com/Vtrivedy10/status/2046979341427331522) expanded this into a concrete loop involving trace mining, skills, context engineering, subagents, and online evals. [@ClementDelangue](https://x.com/ClementDelangue/status/2046942871299772441) pushed for **open traces** as the missing data substrate for open agent training, while [@gneubig](https://x.com/gneubig/status/2046963826109689983) promoted **ADP / Agent Data Protocol** standardization. LangChain also teased a stronger testing/evaluation product direction via [@hwchase17](https://x.com/hwchase17/status/2046962351090606404).




**Post-Training, RL, and Inference Systems**

  * **Perplexity and others shared more of the post-training playbook** : [@perplexity_ai](https://x.com/perplexity_ai/status/2047016400292839808) published details on a **search-augmented SFT + RL** pipeline that improves factuality, citation quality, instruction following, and efficiency; they say Qwen-based systems can match or beat GPT-family models on factuality at lower cost. [@AravSrinivas](https://x.com/AravSrinivas/status/2047019688920756504) added that Perplexity now runs a post-trained Qwen-derived model in production that unifies **tool routing and summarization** and is already serving a significant share of traffic. On the research side, [@michaelyli__](https://x.com/michaelyli__/status/2047019938339340602) introduced **Neural Garbage Collection** , using RL to jointly learn reasoning and **KV-cache retention/eviction** without proxy objectives; [@sirbayes](https://x.com/sirbayes/status/2046961503107166689) reported a Bayesian linguistic-belief forecasting agent matching human superforecasters on ForecastBench.

  * **The “minimal editing” problem in coding models got a useful benchmark treatment** : [@nrehiew_](https://x.com/nrehiew_/status/2046963016428872099) presented work on **Over-Editing** , where coding models fix bugs by rewriting too much code. The study constructs minimally corrupted problems and measures excess edits with patch-distance and added **Cognitive Complexity** ; it finds [GPT-5.4 over-edits the most while Opus 4.6 over-edits the least](https://x.com/nrehiew_/status/2046963041338855791), and that [RL outperforms SFT, DPO, and rejection sampling](https://x.com/nrehiew_/status/2046963050427879488) for learning a generalizable minimal-editing style without catastrophic forgetting. This is one of the more practical post-training/eval contributions in the set because it targets a failure mode engineers actually complain about in production code review.

  * **Inference efficiency work remained highly active** : [@cohere](https://x.com/cohere/status/2047052557915476304) integrated **production W4A8 inference into vLLM** , reporting **up to 58% faster TTFT** and **45% faster TPOT** vs W4A16 on Hopper; the details include [per-channel FP8 scale quantization and CUTLASS LUT dequantization](https://x.com/cohere/status/2047052560553681183). [@WentaoGuo7](https://x.com/WentaoGuo7/status/2047007230847766951) reported **SonicMoE** throughput gains on Blackwell—**54% / 35% higher fwd/bwd TFLOPS than DeepGEMM baseline** —while maintaining dense-equivalent activation memory for equal active params. [@baseten](https://x.com/baseten/status/2047019335542358284) introduced **RadixMLP** for shared-prefix elimination in reranking, with **1.4–1.6x** realistic speedups.




**Top tweets (by engagement)**

  * **OpenAI workspace agents** : [@OpenAI](https://x.com/OpenAI/status/2047008987665809771) launched shared, Codex-powered workspace agents for Business/Enterprise/Edu/Teachers.
  * **Qwen3.6-27B release** : [@Alibaba_Qwen](https://x.com/Alibaba_Qwen/status/2046939764428009914) announced the new open **27B** dense model with strong coding claims and Apache 2.0 licensing.
  * **Google TPU v8** : [@sundarpichai](https://x.com/sundarpichai/status/2046981627184902378) previewed **TPU 8t / 8i** , with training/inference specialization.
  * **Flipbook / model-streamed UI** : [@zan2434](https://x.com/zan2434/status/2046982383430496444) showed a prototype where the screen is rendered as pixels directly from a model rather than traditional UI stacks.
  * **OpenAI Privacy Filter** : [@scaling01](https://x.com/scaling01/status/2046972437422543064) and others highlighted OpenAI’s new open-source **PII detection/redaction** model on Hugging Face.



* * *

# AI Reddit Recap

## /r/LocalLlama + /r/localLLM Recap

### 1\. Qwen 3.6 Model Releases and Benchmarks

  * **[Qwen 3.6 27B is out](https://www.reddit.com/r/LocalLLaMA/comments/1ssl1xh/qwen_36_27b_is_out/)** (Activity: 2576): ****Qwen 3.6 27B** , a new language model, has been released on [Hugging Face](https://huggingface.co/Qwen/Qwen3.6-27B). This model features `27 billion parameters` and is designed to improve upon previous iterations with enhanced performance benchmarks. A quantized version is also available, [Qwen3.6-27B-FP8](https://huggingface.co/Qwen/Qwen3.6-27B-FP8), which allows for more efficient deployment in environments with limited computational resources. The release includes detailed benchmark results, showcasing its capabilities across various tasks.** The community is expressing excitement about the release, with some users highlighting the significance of the model's performance improvements and the availability of a quantized version for broader accessibility.

    * Namra_7 shared a benchmark image for Qwen 3.6 27B, which likely includes performance metrics such as inference speed, accuracy, or other relevant statistics. However, the specific details of the benchmarks are not described in the comment itself.
    * challis88ocarina mentioned a quantized version of Qwen 3.6 27B available on Hugging Face, specifically in FP8 format. Quantization can significantly reduce the model size and improve inference speed, making it more efficient for deployment without a substantial loss in accuracy. The link provided leads to the Hugging Face model repository for further exploration.
    * Eyelbee posted another image link, which might contain additional visual data or performance metrics related to Qwen 3.6 27B. However, the comment does not provide specific insights or details about the content of the image.
  * **[Qwen3.6-27B released!](https://www.reddit.com/r/LocalLLaMA/comments/1ssl6ki/qwen3627b_released/)** (Activity: 895): ****Qwen3.6-27B** is a newly released dense, open-source model that excels in coding tasks, outperforming its predecessor, Qwen3.5-397B-A17B, on major coding benchmarks. It features strong reasoning capabilities across both text and multimodal tasks and offers flexibility with 'thinking' and 'non-thinking' modes. The model is released under the Apache 2.0 license, making it fully open-source and accessible for community use. More details can be found on their [blog](https://qwen.ai/blog?id=qwen3.6-27b), [GitHub](https://github.com/QwenLM/Qwen3.6), and [Hugging Face](https://huggingface.co/Qwen/Qwen3.6-27B).** The comments reflect excitement and admiration for the Qwen team, with users expressing eagerness to utilize the model on their hardware and suggesting the team's contributions are monument-worthy.

    * ResearchCrafty1804 highlights the impressive performance of Qwen3.6-27B, noting that despite having only 27 billion parameters, it surpasses the much larger Qwen3.5-397B-A17B model on several coding benchmarks. Specifically, it achieves scores of 77.2 on SWE-bench Verified, 53.5 on SWE-bench Pro, 59.3 on Terminal-Bench 2.0, and 48.2 on SkillsBench, outperforming the larger model by significant margins in each case.
    * bwjxjelsbd comments on the competitive landscape, expressing satisfaction that Alibaba is advancing with Qwen models after META's perceived setbacks. The commenter hopes for continued competition and transparency, suggesting that META should open-source their Muse family models to maintain a healthy competitive environment.
  * **[Qwen3.6-35B becomes competitive with cloud models when paired with the right agent](https://www.reddit.com/r/LocalLLaMA/comments/1ssilc3/qwen3635b_becomes_competitive_with_cloud_models/)** (Activity: 848): **The post discusses the significant improvement in benchmark performance of the**Qwen3.6-35B** model when paired with the `little-coder` agent, achieving a `78.7%` success rate on the Polyglot benchmark, placing it in the top 10. This improvement highlights the impact of using appropriate scaffolds, suggesting that local models may underperform due to harness mismatches. The author plans to test further on Terminal Bench and GAIA for research capabilities. Full details and benchmarks are available on [GitHub](https://github.com/itayinbarr/little-coder) and [Substack](https://open.substack.com/pub/itayinbarr/p/honey-i-shrunk-the-coding-agent).** Commenters express surprise at the performance gains from scaffold changes, questioning the validity of benchmarks that don't control for such factors. There's also interest in using **pi.dev** for its extensibility in harnessing models.

    * **DependentBat5432** highlights a significant performance improvement in Qwen3.6-35B when changing the scaffold, noting a jump from `19%` to `78%`. This raises concerns about the validity of benchmark comparisons that do not control for such variables, suggesting that scaffold choice can dramatically affect model performance.
    * **Willing-Toe1942** reports that Qwen3.6, when used with pi-coding agents, performs almost twice as well as opencode. This comparison involved tasks like modifying HTML code and searching online resources for documentation, indicating that the choice of agent can significantly enhance the model's effectiveness in practical coding scenarios.
    * **kaeptnphlop** mentions the strong performance of Qwen-Coder-Next when paired with GitHub Copilot in VS Code, suggesting potential for further exploration with other tools like little-coder. This implies that integrating Qwen models with popular coding environments can leverage their strengths effectively.
  * **[Qwen3.6-27B released!](https://www.reddit.com/r/LocalLLM/comments/1sslo98/qwen3627b_released/)** (Activity: 368): **The image is a performance comparison chart highlighting the capabilities of the newly released**Qwen3.6-27B** model across various benchmarks. It shows that Qwen3.6-27B outperforms its predecessor, Qwen3.5-27B, and other models like Gemma4-31B in categories such as Terminal-Bench 2.0 and SWE-bench Pro, indicating significant improvements in coding, reasoning, and real-world task performance. The chart visually emphasizes the model's superior scores, suggesting advancements in its architecture or training methodologies.** One commenter expresses anticipation for the release of a larger model, Qwen122b, while another discusses potential issues with the model's 'thinking' process, indicating a need for optimization in certain use cases. A link to the model on Hugging Face is also shared, suggesting community interest in exploring and utilizing the model.

    * MrWeirdoFace mentions an issue with the Qwen3.6-27B model, specifically when using the 'unsloth Q5 quant' version, where the model tends to get 'lost in thought cycles'. This suggests a potential problem with the model's inference process, possibly related to its quantization or optimization settings, which might need adjustment to improve performance.
    * andreabarbato notes that the Qwen3.6-27B model in 'q4' quantization provides good output quality but also suffers from getting 'lost in crazy loops'. This indicates a recurring issue with the model's reasoning or decision-making processes, which could be a result of the quantization method affecting the model's stability or coherence during inference.
    * DjsantiX inquires about fitting the Qwen3.6-27B model into a '5060 ti 16gb' GPU, highlighting a common challenge of deploying large models on consumer-grade hardware. This reflects the ongoing need for efficient model optimization and quantization techniques to enable the use of large-scale models on limited-resource environments.



### 2\. Gemma 4 Model Capabilities and Comparisons

  * **[An actual example of "If you dont run it, you dont own it" and Gemma 4 beats both Chat GPT and Gemini Chat](https://www.reddit.com/r/LocalLLaMA/comments/1ss2lib/an_actual_example_of_if_you_dont_run_it_you_dont/)** (Activity: 355): **The post discusses the performance of various AI models in translating a Chinese novel, highlighting issues of model degradation and censorship. Initially,**GPT OSS 120B** and **Qwen 3 Max** were used, but both failed due to name mixing and censorship, respectively. **Chat GPT 4o** initially performed well but degraded with updates, leading to a 20% failure rate in translations. Surprisingly, **Gemma 4 31B** outperformed both **Gemini Chat** and **GPT 5.3** , providing natural and accurate translations. The results were confirmed by testing multiple models, where Gemma 4 consistently delivered superior performance, even compared to Google's Gemini.** Commenters noted that **Gemma 4** has been widely praised for its language abilities, with some users initially underestimating it compared to **Qwen 3.5**. The model's availability for free has been appreciated, and it is seen as a significant advancement for creative writing and role-playing communities. External benchmarks also support these findings, highlighting Gemma 4's capabilities.

    * Uncle___Marty highlights the distinct language capabilities of Gemma 4, noting that while initially it seemed inferior to Qwen 3.5, both models excel in different areas. This suggests a specialization in tasks, with Gemma 4 potentially outperforming in certain linguistic tasks. The comment underscores the accessibility of these advanced models, emphasizing the generosity of the Gemma team and Alibaba in providing them for free.
    * Potential-Gold5298 references benchmark comparisons from [dubesor.de](https://dubesor.de/benchtable) and [foodtruckbench.com](https://foodtruckbench.com/#leaderboard), indicating that Gemma 4 is a significant advancement for the RP community, which had been reliant on older models like Mistral Nemo and Mistral Small. This suggests that Gemma 4 offers superior performance in creative writing and role-playing applications, filling a gap left by older models.
    * Sevenos praises Gemma 4's proficiency as a German chatbot, noting its ability to structure responses with minimal language errors. This indicates a high level of linguistic accuracy and usability in non-English languages, which is a significant achievement for AI models. The comment also hints at the potential for a larger version, suggesting that current performance is already competitive with Gemini.
  * **[Gemma 4 Vision](https://www.reddit.com/r/LocalLLaMA/comments/1srrhi5/gemma_4_vision/)** (Activity: 409): **The post discusses the configuration of the**Gemma 4 Vision** model, specifically focusing on its vision budget settings. The default configuration from Google sets the vision budget at `280` tokens, which corresponds to approximately `645K pixels`, but this is considered insufficient for detailed OCR tasks. Users can adjust this in `llama.cpp` by setting `--image-min-tokens` and `--image-max-tokens` to higher values, such as `560` and `2240` respectively, to improve image detail recognition. This adjustment significantly increases VRAM usage, from `63 GB` to `77 GB` for a `4096` batch size. The post also notes that **Gemma 4** outperforms other models like **Qwen 3.5** , **Qwen 3.6** , and **GLM OCR** in vision tasks when properly configured.** A commenter inquires about the minimum token settings for smaller models, questioning whether the `40` token minimum applies only to larger models with `c500m` vision encoders. Another user requests detailed configuration options for `llamacpp` and `vllm`, indicating a need for more comprehensive setup guidance.

    * Temporary-Mix8022 discusses working with vision encoders in smaller models, specifically mentioning a parameter size of `c150m` and using `70 tokens` as a minimum. They inquire whether `40 tokens` is the actual minimum, or if this applies only to larger models with `c500m` vision encoders. This highlights the importance of understanding token limits in model configurations for optimal performance.
    * stddealer shares their experience using `--image-min-tokens 1024 --image-max-tokens 1536` with Gemma4's vision, a habit carried over from using Qwen3.5. This configuration choice led to confusion about the perceived underperformance of Gemma4's vision capabilities, suggesting that token settings significantly impact model output quality.
    * eposnix points out a limitation in LM Studio for vision tasks, noting that it does not expose certain variables necessary for configuring vision models effectively. This lack of configurability is a barrier for users needing to adjust parameters for specific vision tasks, indicating a potential area for improvement in the software.



### 3\. Ultimate Lists of Open Source Models

  * **[Ultimate List: Best Open Models for Coding, Chat, Vision, Audio& More](https://www.reddit.com/r/LocalLLaMA/comments/1sseh00/ultimate_list_best_open_models_for_coding_chat/)** (Activity: 313): **The post provides a comprehensive list of the best open-source AI models across various domains, including audio generation, image generation, image-to-video, image-to-text, and text generation. Notable models include**Qwen3-TTS** for text-to-speech, **VoxCPM2** for voice cloning, **ACE-Step 1.5** for music generation, and **GLM-5.1** for text generation. Each model is highlighted for its specific strengths, such as **Qwen3-TTS** for quality and speed balance, **VibeVoice Realtime** for real-time applications, and **GLM-5.1** for agentic engineering and long-horizon coding tasks. The list includes links to repositories and emphasizes models' unique capabilities, such as **LTX-2.3** for 4K video generation and **GLM-OCR** for OCR speed and accuracy.** The comments reflect skepticism about the reliability and factual basis of the list, with one user sarcastically suggesting that random chance could yield similar results. Another comment simply mentions 'omnivoice,' possibly indicating interest or skepticism about the audio models.

    * **SatoshiNotMe** highlights the omission of specific Speech-to-Text (STT) and Text-to-Speech (TTS) models in the list, mentioning `PocketTTS` from **KyutAI** and `Parakeet V3` for STT. These models are noted for their regular use, suggesting they are reliable and effective in their respective domains.
    * **ecompanda** discusses the rapid evolution of AI models, noting that the 'best models' list becomes outdated quickly due to frequent updates and new releases. They mention that `Qwen 3.6 Plus` has recently reshuffled the coding leaderboard, similar to the impact of `Gemma 4`. This highlights the challenge of maintaining an up-to-date list without frequent updates.
  * **[Ultimate List: Best Open Source Models for Coding, Chat, Vision, Audio& More](https://www.reddit.com/r/LocalLLM/comments/1ssejd5/ultimate_list_best_open_source_models_for_coding/)** (Activity: 252): **The post provides a comprehensive list of the best open-source AI models across various domains, including audio generation, image generation, and text generation. Notable models include**Qwen3-TTS** for text-to-speech with a balance of quality and speed, **VoxCPM2** for high-quality voice cloning, and **ACE-Step 1.5** for music generation. In image generation, **FLUX.1 [schnell]** is highlighted for its speed and quality on consumer GPUs, while **Stable Diffusion 3.5 Large** is noted for its versatility in fine-tuning and editing. For text generation, **GLM-5.1** by Zhipu AI is a flagship model with a 744B MoE architecture, excelling in long-horizon coding tasks. The list also includes models for image-to-video and image-to-text generation, such as **LTX-2.3** for 4K video generation and **GLM-OCR** for OCR tasks.** Comments suggest a need for better formatting of the list for clarity. There is also a debate on the effectiveness of **Qwen TTS** for longer audio generation, with some users preferring **Kokoro** for certain tasks.

    * Adrian_Galilea raises a technical point about the performance of the Qwen TTS model, questioning its effectiveness for audio longer than a minute. They suggest that Kokoro might be a better alternative, implying potential limitations in Qwen TTS's handling of longer audio sequences.
    * decentralize999 references an external resource, [Artificial Analysis](https://artificialanalysis.ai/leaderboards/models), which provides up-to-date leaderboards for model performance. They also mention Qwen3.6-35B as one of the top models currently, highlighting its significance in the field.
    * oguza inquires about the inclusion of Flux.2 dev and Klein, suggesting interest in these models' capabilities or performance. This indicates a potential gap in the original list regarding these specific models.



## Less Technical AI Subreddit Recap

> /r/Singularity, /r/Oobabooga, /r/MachineLearning, /r/OpenAI, /r/ClaudeAI, /r/StableDiffusion, /r/ChatGPT, /r/ChatGPTCoding, /r/aivideo, /r/aivideo

### 1\. Claude Code Feature Changes and User Reactions

  * **[PSA: Claude Pro no longer lists Claude Code as an included feature](https://www.reddit.com/r/ClaudeAI/comments/1srzhd7/psa_claude_pro_no_longer_lists_claude_code_as_an/)** (Activity: 4239): ****Claude Pro** has removed **Claude Code** as an included feature from its Pro plan, as observed on their [pricing page](https://claude.com/pricing). The support article, now titled "Using Claude Code with your Max plan," indicates a shift in availability, suggesting that Claude Code is now exclusive to the Max plan. The article was updated recently, reflecting this change, although cached results still show the previous inclusion in the Pro plan.** The comments reflect dissatisfaction with the change, with users expressing frustration and considering unsubscribing due to the removal of Claude Code from the Pro plan.

  * **[Anthropic response to Claude Code change](https://www.reddit.com/r/ClaudeAI/comments/1ss5fi4/anthropic_response_to_claude_code_change/)** (Activity: 1975): ****Anthropic** is conducting a test affecting `~2%` of new prosumer signups, focusing on changes in subscription plans due to evolving usage patterns of the **Claude Code** feature. Initially, the Max plan was designed for heavy chat usage, but with the integration of Claude Code, **Cowork** , and long-running async agents, user engagement has increased significantly. This has led to adjustments like weekly caps and tighter limits during peak times. The test aims to explore options for maintaining service quality, with assurances that existing subscribers will be notified of any changes well in advance. [Amol Avasare](https://x.com/amolavasare) announced this on X, highlighting the shift of Claude Code from Pro to Max, which has increased costs for users.** Commenters express skepticism about the transparency and communication of the test, with some perceiving it as a potential negative change for users. Concerns include the randomness of access to Claude Code for new signups and the perception of the test as a 'gacha game'.

    * A user highlights that Anthropic is conducting a test where only `2%` of new prosumer signups have access to Claude Code, yet the documentation has already been updated to reflect this change. This raises concerns about transparency and communication, as users are confused about whether they will have access to the feature upon signing up.
    * Another commenter questions the logic behind the test, suggesting that the randomness of access to Claude Code for new pro users resembles a 'gacha game' mechanic. This implies a lack of predictability and fairness in how features are distributed among users, which could affect user trust and satisfaction.
    * A user speculates on the purpose of the test, humorously suggesting that it might be to observe user reactions when they find out they don't have access to a feature they expected. This points to potential issues in user experience and expectation management, as well as the importance of clear communication from Anthropic.
  * **[Does Claude's $20 Plan No Longer Include Claude Code?](https://www.reddit.com/r/ClaudeAI/comments/1ss3asp/does_claudes_20_plan_no_longer_include_claude_code/)** (Activity: 1477): **The image is a pricing table for Claude's subscription plans, showing that the 'Claude Code' feature is not included in the $20 Pro plan, but is available in the Max 5x and Max 20x plans. This has caused confusion among users, as some recall 'Claude Code' being part of the Pro plan previously. The discrepancy between the information on Claude.com and Claude.ai adds to the confusion, suggesting a recent change or inconsistency in the feature offerings. Users are concerned about the impact on hobbyist programming and are considering alternatives like ChatGPT and Codex.** Users express frustration over the removal of 'Claude Code' from the Pro plan, feeling it limits personal use and may push them towards other services. The inconsistency between different Claude websites adds to the dissatisfaction.

    * There is confusion regarding the availability of Claude Code in the Pro plan, with some users reporting recent access while others note discrepancies between information on Claude.com and Claude.ai. This suggests potential inconsistencies in communication or implementation of plan features.
    * A user provided a link to a support article that initially suggested Claude Code was available for both Pro and Max plans, but now redirects to a page indicating it's only available for the Max plan. This change implies a possible shift in service offerings, though it's unclear if this is intentional or an error.
    * The uncertainty around Claude Code's availability in the Pro plan is causing concern among users who rely on it for hobbyist programming. The potential removal could push users towards alternatives like ChatGPT and Codex, highlighting the importance of clear communication from service providers regarding feature availability.
  * **[Sama is on 🔥🔥](https://www.reddit.com/r/ClaudeCode/comments/1sse789/sama_is_on/)** (Activity: 1164): **The image is a meme-like screenshot of a Twitter exchange involving**Sam Altman** and discussions about **Anthropic's** decision to remove Claude Code from the Pro plan, requiring users to upgrade to Max for access. This decision has sparked controversy, as highlighted by **Amol Avasare's** clarification that this change affects new signups, not existing subscribers. The exchange includes a dismissive response from Sam Altman, 'ok boomer,' which has attracted significant attention. The post and comments reflect dissatisfaction with Anthropic's A/B testing practices, which some users find unethical, and critique Sam Altman's public persona.** Commenters express strong disapproval of Anthropic's decision-making, particularly the ethics of their A/B testing strategy, and criticize Sam Altman's response as unprofessional and indicative of broader issues with his public image.

    * SilasTalbot raises concerns about the ethics of A/B testing, particularly when 1 in 50 users receive less functionality without being informed. This practice can be seen as unethical, especially if it involves removing access to key features, as mechapaul also highlights. Such tests can negatively impact user trust and satisfaction.
    * gloobit criticizes the decision to remove a key feature as part of a test, suggesting that it is unrealistic to expect users to upgrade to a $200/month plan immediately. This points to potential misjudgments in product strategy and user experience management, which could lead to customer dissatisfaction and churn.
  * **[Head of Growth at Anthropic regarding Claude Code removal from Pro](https://www.reddit.com/r/ClaudeCode/comments/1ss5bop/head_of_growth_at_anthropic_regarding_claude_code/)** (Activity: 2197): **The image and accompanying discussion highlight a strategic shift by**Anthropic** in their subscription model, specifically affecting the availability of Claude Code. The company is transitioning this feature from the Pro plan to the more expensive Max plan, which costs at least `$100` per month. This change is part of a limited test impacting about `2%` of new subscribers, while existing Pro and Max users remain unaffected. The move is seen as a response to resource constraints, particularly compute availability, which is a significant issue for AI companies. The decision has sparked debate about pricing strategies and resource allocation in the AI industry.** Commenters express concern over the increasing costs and resource limitations in AI services, with some suggesting that Anthropic's decision reflects broader industry challenges in managing compute resources. There is also criticism of the pricing strategy, with calls for a more affordable tier between Pro and Max.

    * samwise970 highlights that Anthropic's decision to remove Claude Code from the Pro tier is likely due to a shortage of computational resources. They argue that if Anthropic had sufficient compute, the marginal cost of inference would be minimal, suggesting that the company is trying to manage limited resources by increasing prices.
    * RemarkableGuidance44 discusses the broader issue of resource constraints in AI, noting that several companies, including GitHub Co-Pilot and OpenAI, are facing similar challenges. They mention that Anthropic's token usage costs have increased, which reduces the value of subscriptions, and suggest that the recent performance improvements are merely fixes for existing issues rather than genuine enhancements.
    * band-of-horses questions the usage patterns of Claude, suggesting that it is primarily used for coding rather than general chat. They note that users interested in general knowledge tend to prefer other AI models like Gemini and ChatGPT, indicating a potential niche market for Claude focused on coding applications.
  * **[We’re saved! Claude Code is back in the Pro plan!](https://www.reddit.com/r/ClaudeCode/comments/1sscvvo/were_saved_claude_code_is_back_in_the_pro_plan/)** (Activity: 586): **The image is a pricing plan comparison for a service called Claude, highlighting that "Claude Code" is now included in the Pro plan. This suggests a change or update in the service offerings, where previously "Claude Code" might not have been available in the Pro plan. The table also lists other features like "Chat on web, iOS, Android and Desktop" and "Claude Cowork," indicating a tiered service structure with varying feature availability. The return of "Claude Code" to the Pro plan is met with relief or excitement, as indicated by the title and the red-circled checkmark in the image.** Commenters express skepticism about the longevity of this change, with some suggesting it might be part of A/B testing. There is also a discussion about the value and limitations of the $20 plan, with some users indicating that they occasionally hit usage limits even on higher-tier plans.

    * A user speculates that the $20 Claude Code plan might be restrictive, especially for those who hit usage limits even on the $100 plan. This suggests that the lower-tier plan may not provide sufficient resources for heavy users, potentially leading to frequent limitations on usage.
    * Another user predicts a potential price increase for the Claude Pro plan or the introduction of a new Pro+ subscription tier at $50. This reflects a common strategy in subscription services where companies adjust pricing or introduce new tiers to balance demand and resource allocation.
    * There is a concern that the company might reduce usage limits for the Pro plan without notice. This could be a strategy to manage costs or encourage users to upgrade to higher tiers, reflecting a common practice in subscription-based models to optimize revenue.



### 2\. GPT-Image-2 and ChatGPT Image Model Developments

  * **[Gpt image 2 has the biggest jump in quality ever recorded](https://www.reddit.com/r/singularity/comments/1sry7k9/gpt_image_2_has_the_biggest_jump_in_quality_ever/)** (Activity: 1395): **The image showcases a leaderboard from the 'Text-to-Image Arena,' highlighting the performance of various AI models in generating images from text prompts. The standout model, 'gpt-image-2' by**OpenAI** , achieves a score of `1512`, marking a significant leap in quality compared to competitors like Google and Microsoft AI. This score is based on over `4.8 million` votes, indicating a broad consensus on its superior performance. The leaderboard is current as of April 19, 2026, underscoring the model's cutting-edge capabilities in text rendering and photorealism.** Commenters express surprise at the model's capabilities, particularly in text rendering and photorealism, comparing it to the 'o1 reasoning model of AI images.' There is also discussion about different model versions, such as 'medium' and 'instant,' and speculation about a 'high' version in the API.

    * FateOfMuffins highlights that the new model offers different quality levels, such as 'medium' and 'instant', suggesting a tiered approach to image generation. This implies that users can choose between speed and quality, with potential for a 'high' quality option via API, indicating a flexible model architecture that can cater to various user needs.
    * Thatunkownuser2465 and GoodDayToCome discuss the model's advancements in text rendering and photorealism, noting its ability to create detailed and accurate infographics. They emphasize that previous models couldn't match this level of detail, suggesting significant improvements in both the model's understanding of layout and its ability to maintain stylistic coherence across complex images.
    * Kinu4U mentions the use of 'extended thinking' in prompts, which may refer to a more sophisticated processing technique that allows the model to generate hyper-realistic images based on user preferences. This could indicate an advancement in how the model interprets and executes creative tasks, potentially leading to more personalized and high-quality outputs.
  * **[GPT-Image-2 now reviews its own output and iterates until it is satisfied with the correctness of its output.](https://www.reddit.com/r/singularity/comments/1srehi7/gptimage2_now_reviews_its_own_output_and_iterates/)** (Activity: 658): **The image titled "The Great Counting Adventure" is a whimsical map generated by GPT-Image-2, showcasing its new capability to self-review and iterate on its outputs until achieving satisfactory correctness. This process took approximately 11 minutes, indicating a significant computational cost due to multiple internal iterations aimed at improving design clarity and accuracy. This feature, while enhancing output quality, raises concerns about its practicality in workflows requiring rapid iterations, such as UI mocks or storyboards, due to time and cost constraints.** Commenters express concern over the practicality of the self-review loop, noting that the 11-minute generation time per image could be prohibitive for workflows needing quick iterations. There is interest in whether the iteration count will be adjustable to balance quality and efficiency.

    * Worried-Squirrel2023 highlights a significant concern regarding the **processing time and cost** of GPT-Image-2's self-review loop, noting that it takes '11 minutes per image' and involves '5-10 internal iterations'. This could make it impractical for workflows requiring rapid iteration, such as UI mocks or storyboards, though it might be suitable for high-quality 'hero shots'. The commenter suggests the possibility of a user-controlled 'iteration count' to manage these factors.
    * Jaxraged comments on the aesthetic aspect of GPT-Image-2, noting that it retains a 'sepia filter look'. This suggests that despite the technical advancements in self-review and iteration, the model's output still maintains a certain stylistic consistency, which may or may not be desirable depending on the use case.
    * TopTippityTop points out a specific issue with GPT-Image-2's output accuracy, mentioning that it failed to correctly render the numbers '15 and 39'. This highlights a potential limitation in the model's ability to accurately generate detailed numerical information, which could be critical for applications requiring precise data representation.
  * **[GPT Image 2 is amazing!](https://www.reddit.com/r/OpenAI/comments/1ss40rn/gpt_image_2_is_amazing/)** (Activity: 794): **The image described in the post is non-technical and appears to be a meme or a casual depiction of a streaming setup, emphasizing a cozy and relaxed atmosphere with elements like a neon sign and gaming chair. The comments do not provide any technical insights or discussions related to the image, focusing instead on humorous or casual remarks about the content.** The comments reflect a humorous take on the image, with one user joking about its potential as a 'goonerbait generator' and another remarking on the progress made, likely in reference to streaming setups or technology.

  * **[Introducing ChatGPT Images 2.0](https://www.reddit.com/r/OpenAI/comments/1sry11n/introducing_chatgpt_images_20/)** (Activity: 929): **OpenAI has released**ChatGPT Images 2.0** , which significantly enhances image generation capabilities by improving precision and control. This version introduces support for multilingual text rendering and offers a range of visual styles, such as editorial, surreal, and photorealistic imagery, demonstrating its versatility in content creation. The update aims to provide more nuanced and diverse image outputs, catering to a broader range of user needs. For further details, refer to the [OpenAI announcement](https://openai.com/index/introducing-chatgpt-images-2-0/).** Users are experimenting with the new capabilities, noting both the system's limitations in generating certain types of content and its impressive ability to create complex, realistic designs, such as a practical mobile suit. The discussions highlight the balance between creative freedom and content moderation in AI-generated imagery.

    * **Zandrio** raises a critical point about the strategic release and subsequent throttling of AI models. Companies often release powerful models initially to generate hype and user engagement, but may later reduce capabilities to manage operational costs. This pattern suggests the importance of evaluating model performance and capabilities over time, particularly through benchmarks conducted 6 months post-release to assess any degradation or throttling effects.
    * **birdomike** expresses interest in comparing ChatGPT Images 2.0 against other models like Nano Banana Pro and NB2. This highlights the competitive landscape in AI image generation, where performance metrics and feature comparisons are crucial for understanding relative strengths and weaknesses. Such comparisons often involve detailed benchmarks and real-world application tests to determine practical utility and efficiency.
  * **[GPT IMAGE 2 is superb](https://www.reddit.com/r/ChatGPT/comments/1sryveb/gpt_image_2_is_superb/)** (Activity: 563): **The image is a creative output generated by GPT IMAGE 2, showcasing its ability to produce a fashion-editorial style collage based on a detailed prompt. The prompt specifies a freeform arrangement of eight distinct summer outfits on a consistent model, emphasizing the model's height and maintaining visual scale across all figures. The image demonstrates the model's capability to adhere to complex layout instructions, such as arranging figures in a balanced two-row layout and adding handwritten labels for clothing items, without using grids or borders. This highlights the model's potential in generating visually appealing and contextually accurate fashion content.**

    * The comment by 'flatacthe' highlights the improved text rendering capabilities of GPT Image 2, noting that it handles text much better than previous versions. The user points out that specifying the style in prompts can enhance consistency across multiple figures, suggesting that smart prompting plays a significant role in achieving high-quality outputs.



### 3\. Google TPU 8th Generation and AI Studio Limitations

  * **[Google introduces TPU 8t and TPU 8i](https://www.reddit.com/r/singularity/comments/1ssjlk4/google_introduces_tpu_8t_and_tpu_8i/)** (Activity: 550): **The image provides a detailed comparison between Google's Ironwood (2025) and the newly announced TPU 8i (2026), highlighting significant advancements in hardware specifications. The TPU 8i features a larger pod size, increased FP8 EFLOPS per pod, enhanced total HBM capacity per pod, and improved bidirectional scale-up bandwidth, indicating substantial performance improvements over its predecessor. These enhancements are part of Google's strategy to advance supercomputing capabilities with the TPU 8i, which is custom-engineered for efficiency and scalability in the next generation of computing.** Commenters note the impressive specifications of the TPU 8i, suggesting it poses a competitive challenge to NVIDIA as hyperscalers develop their own silicon solutions. The numbers are perceived as 'insane,' indicating a significant leap in performance.

    * Worried-Squirrel2023 highlights a significant shift in the AI hardware landscape, noting that **NVIDIA** faces increased competition as major cloud providers develop their own silicon solutions. This trend suggests a diversification in AI hardware sources, potentially impacting NVIDIA's market dominance.
    * WhyLifeIs4 shares a link to a [technical deep dive](https://cloud.google.com/blog/products/compute/tpu-8t-and-tpu-8i-technical-deep-dive) on Google's new TPU models, which could provide detailed insights into their architecture, performance metrics, and potential use cases, offering valuable information for those interested in the technical specifics of these new processors.
  * **[Google AI Studio Madness](https://www.reddit.com/r/Bard/comments/1ssgx0y/google_ai_studio_madness/)** (Activity: 102): **The post criticizes**Google AI Studio's** quota limitations, particularly for the `3.1 Pro model`, which reportedly exhausts its quota after just `15 messages` even with grounding turned off. The user claims the service's promise of `6,250 prompts a day` is misleading, leading to their decision to cancel the subscription.** Comments highlight that the quota appears to be the same across Pro, Ultra, and Free tiers, limiting users to `10-15 prompts`. Additionally, the `1 million token context size` is criticized for its inability to maintain context over `10 prompts`.

    * vladislavkochergin01 highlights a significant limitation in Google AI Studio's current offering, noting that the quota for Pro, Ultra, and Free users is now identical, allowing only `10-15 prompts`. This change could impact users who rely on higher-tier plans for more extensive usage, potentially affecting productivity and workflow.
    * PsyckoSama points out a technical limitation regarding the context size of Google AI Studio, which is `1 million tokens`. Despite this seemingly large capacity, the system struggles to maintain context over `10 prompts`, indicating potential inefficiencies in memory management or prompt handling that could hinder complex task execution.
  * **[Gemini 3.1 Pro limits in AI Studio are now exactly the same for Pro and Free users](https://www.reddit.com/r/Bard/comments/1srloa4/gemini_31_pro_limits_in_ai_studio_are_now_exactly/)** (Activity: 109): ****Google's Gemini 3.1 Pro** in AI Studio has implemented rate limits that are identical to the Free tier, restricting users after `8-12 prompts`. This change has led to confusion and frustration among users who expected higher limits with the Pro version. Some users report that the issue seems intermittent, suggesting potential bugs or inconsistencies in the implementation.** Users express dissatisfaction with Google's handling of the rate limits, with some noting that the issue affects both Gemini 2.5 and 3.1 versions. There is a sentiment that the Pro tier should offer more value, and the current situation is seen as a failure to meet expectations.




# AI Discords

Unfortunately, Discord shut down our access today. We will not bring it back in this form but we will be shipping the new AINews soon. Thanks for reading to here, it was a good run.

---

## [GPT-Image-2](https://news.smol.ai/issues/26-04-21-image-2/)
*🌐 Smol AI News | 2026-04-21*

**a quiet day.**

> AI News for 4/20/2026-4/21/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

# AI Twitter Recap

**OpenAI’s GPT-Image-2 Launch and the Return of Image Generation as a Serious Product Surface**

  * **GPT-Image-2 is the day’s clearest product launch** : OpenAI rolled out **ChatGPT Images 2.0** and the underlying **`gpt-image-2`** model across ChatGPT, Codex, and API, emphasizing stronger **text rendering, layout fidelity, editing, multilingual support, and “thinking” for images**. OpenAI says the model can search the web when paired with a thinking model, generate multiple candidates, self-check outputs, and produce artifacts like **slides, infographics, diagrams, UI mockups, and QR codes** ([launch thread](https://x.com/OpenAI/status/2046670977145372771), [thinking/image capabilities](https://x.com/OpenAI/status/2046670989719924768), [availability](https://x.com/OpenAI/status/2046670994413322435), [API post](https://x.com/OpenAIDevs/status/2046671238534496259)). The model is already being integrated by downstream tools including [Figma](https://x.com/figma/status/2046673364496875977), [Canva](https://x.com/canva/status/2046665346161988062), [Firefly](https://x.com/AdobeFirefly/status/2046675148065923103), [fal](https://x.com/fal/status/2046667081068761527), and [Hermes Agent](https://x.com/NousResearch/status/2046693872773062834).
  * **Benchmarks suggest a large jump, especially on practical image tasks** : Arena reports **#1 across all Image Arena leaderboards** for GPT-Image-2, including **1512** on text-to-image, **1513** on single-image edit, and **1464** on multi-image edit, with a striking **+242 Elo** lead on text-to-image over the next model ([Arena summary](https://x.com/arena/status/2046670703311884548), [category breakdown](https://x.com/arena/status/2046670705958551938), [trend chart](https://x.com/arena/status/2046690103515648061)). Independent reactions converged on the same theme: this is not merely prettier art, but a more usable model for **UI, mockups, documentation, productivity visuals, and reference-driven design loops** ([@gdb](https://x.com/gdb/status/2046632580527554572), [@nickaturley](https://x.com/nickaturley/status/2046677986242363731), [@mark_k](https://x.com/mark_k/status/2046640315348725879), [@petergostev](https://x.com/petergostev/status/2046720618566242657)). The most interesting systems implication is that **image generation is becoming a front-end for coding agents** : generate a UI spec as an image, then have Codex or another code agent implement against that visual reference.



**Agent Infrastructure: Hugging Face’s ml-intern, Hermes Expansion, and the Rise of Research/Runtime Harnesses**

  * **Hugging Face’s`ml-intern` is the strongest open agent-in-the-loop release in the set**: HF introduced **`ml-intern`** , an open-source agent that automates the **post-training research loop** : reading papers, following citation graphs, collecting/reformatting datasets, launching training jobs, evaluating runs, and iterating on failures ([announcement](https://x.com/akseljoonas/status/2046543093856412100), [supporting post from @lewtun](https://x.com/_lewtun/status/2046549090171764914), [Clement’s framing](https://x.com/ClementDelangue/status/2046598219853951346)). Reported examples are notable because they are **end-to-end loops, not just coding demos** : **GPQA scientific reasoning improved 10% → 32% in under 10h on Qwen3-1.7B** , a healthcare setup reportedly **beat Codex on HealthBench by 60%** , and a math setup wrote a full **GRPO** script and recovered from reward collapse via ablations. Community tests quickly showed it can autonomously fine-tune and publish artifacts back to the Hub ([example run on SAM finetuning](https://x.com/Mayank_022/status/2046646301555900828)).
  * **Hermes is evolving toward a richer local/open agent platform** : Several tweets point to Hermes’ momentum as a practical open agent stack: a [beginner guide generated by a Hermes agent itself](https://x.com/KSimback/status/2046528526581383643), [native support in Skillkit](https://x.com/ghumare64/status/2046542176142733712), a new macOS GUI called [Scarf](https://x.com/QingQ77/status/2046592289540346020), and expanding use in local workflows. The most technically meaningful update is from [@Teknium](https://x.com/Teknium/status/2046709250114957624): **Hermes subagents now support both greater spawn width and recursive spawn depth** , enabling deeper hierarchical decomposition. This aligns with the broader shift from “single chat loop” agents to **multi-process orchestrated systems** with memory, tools, permissions, and reusable skills.
  * **Harnesses are becoming first-class engineering artifacts** : A recurring theme across tweets is that the useful part of agent systems is increasingly the **runtime/harness** , not the base model alone. DSPy 3.2 shipped **RLM improvements** plus optimizer chaining and LiteLLM decoupling ([release](https://x.com/isaacbmiller1/status/2046643827247546441)); Isaac Flath argued **RLM makes notebooks relevant again** as a REPL-native trace/eval interface ([tweet](https://x.com/isaac_flath/status/2046588093399019918)); LangChain added **custom auth for deepagents deploy** ([update](https://x.com/sydneyrunkle/status/2046643201738449076)); and a paper-summary thread on Claude Code emphasized that most of the system is harness logic rather than raw “intelligence” ([summary](https://x.com/TheTuringPost/status/2046726989021888910)).



**Kimi K2.6, KDA Kernels, and Open-Weight Coding Models Getting More Systems-Credible**

  * **Moonshot pushed both model capability and kernel infrastructure** : The flagship Kimi thread claims **K2.6** completed long-horizon coding tasks with sustained autonomy: one run downloaded and optimized **Qwen3.5-0.8B inference in Zig** over **4,000+ tool calls** and **12+ hours** , improving throughput from **~15 tok/s to ~193 tok/s** , ending **~20% faster than LM Studio** ([thread](https://x.com/Kimi_Moonshot/status/2046531052957569211)). Another run reportedly reworked an exchange engine over **1,000+ tool calls** and **4,000+ LOC changes** , achieving **185% medium-throughput** and **133% peak-throughput** gains ([second thread](https://x.com/Kimi_Moonshot/status/2046531057147933137)). These are still vendor demos, but they are much closer to systems work than benchmark screenshots.
  * **Kimi also open-sourced performance-critical infra** : Moonshot released **FlashKDA** , a **CUTLASS-based implementation of Kimi Delta Attention kernels** , claiming **1.72×–2.22× prefill speedup** over the flash-linear-attention baseline on **H20** and compatibility as a **drop-in backend** for flash-linear-attention ([release](https://x.com/Kimi_Moonshot/status/2046607915424034839)). External follow-up reported **K2.6 + DFlash at 508 tok/s on 8x MI300X** , a **5.6× throughput improvement** over a baseline autoregressive setup ([HotAisle](https://x.com/HotAisle/status/2046620289984057634)). Together with ongoing discussion of DSA/MLA/KDA variants, the key signal is that Chinese labs are not just shipping weights; they are increasingly publishing **attention/kernel-level optimizations** with real deployment impact.
  * **Open-weight coding quality is improving, but there’s still disagreement on parity** : Some users now treat **Kimi K2.6 as the best open-source/open-weight coding/agentic model** ([@scaling01](https://x.com/scaling01/status/2046591683198906542), [Windsurf availability](https://x.com/windsurf/status/2046686574793154996)), while others pushed back that frontier proprietary models still hold large leads on **WeirdML, long-horizon tasks, and reliability** ([@scaling01 critique](https://x.com/scaling01/status/2046565191903511010), [gap on WeirdML](https://x.com/scaling01/status/2046590539844186487)). The substantive takeaway is less “open has caught up” than that **open-weight models are now credible enough that infra, harness, and deployment quality determine a lot of real-world value**.



**Deep Research Systems: Google Extends the Research-Agent Frontier**

  * **Google upgraded Deep Research into a more configurable API primitive** : Google/DeepMind launched updated **Deep Research** and **Deep Research Max** via the Gemini API, powered by **Gemini 3.1 Pro** , with **collaborative planning** , **arbitrary MCP support** , **multimodal inputs** (PDF/CSV/image/audio/video), **code execution** , **native chart/infographic generation** , and **real-time progress streaming** ([Google thread](https://x.com/Google/status/2046627647208259835), [feature details](https://x.com/Google/status/2046627652568850687), [Sundar post](https://x.com/sundarpichai/status/2046627545333080316), [developer API post](https://x.com/googleaidevs/status/2046630912054763854)).
  * **The benchmark numbers are strong enough to matter commercially** : Google highlighted **93.3% on DeepSearchQA** , **85.9% on BrowseComp** , and **54.6% on HLE** for the Max variant ([Sundar](https://x.com/sundarpichai/status/2046627545333080316), [Phil Schmid summary](https://x.com/_philschmid/status/2046627179551944753)). More important than the raw scores is the workflow design: Google is clearly productizing “overnight due diligence / analyst report generation” and making **MCP-backed internal data access** a standard part of research agents. This also shows a widening split between simple browse agents and **full-stack research agents** that plan, search, execute code, generate visuals, and ground over proprietary corpora.



**Retrieval, Data, and Evaluation: Open Releases with Real Engineering Value**

  * **Retrieval saw a meaningful open release from LightOn** : LightOn released **LateOn** and **DenseOn** , both **149M-parameter** retrieval models under **Apache 2.0** , reporting **57.22 NDCG@10 on BEIR** for LateOn (multi-vector/ColBERT style) and **56.20** for DenseOn (dense single-vector), beating models up to **4× larger** ([model release](https://x.com/raphaelsrty/status/2046609364929187845), [overview](https://x.com/antoine_chaffin/status/2046609241918579019)). They also published a consolidated dataset release with **1.4B query-document pairs** and a refreshed web dataset built on **FineWeb-Edu** ([dataset post](https://x.com/antoine_chaffin/status/2046609260440629588)).
  * **vLLM shipped a practical deployment knowledge layer** : The redesign of [recipes.vllm.ai](https://x.com/vllm_project/status/2046592125740142903) is more useful than it sounds. It maps model pages to runnable deployment recipes, includes an **interactive command builder** , supports **NVIDIA and AMD** , covers **tensor/expert/data parallel variants** , and exposes a **JSON API for agents**. This is exactly the kind of infra documentation layer that reduces operator friction for serving new open models.
  * **Benchmarks are increasingly probing agent blind spots, not just task outputs** : Notable examples include **ParseBench** for chart understanding inside real enterprise documents ([LlamaIndex](https://x.com/llama_index/status/2046586730879283227), [Jerry Liu details](https://x.com/jerryjliu0/status/2046725527806021937)) and a new result showing agents often **ignore explicit environment clues** , even when the solution is literally exposed in a file or endpoint ([paper thread](https://x.com/LeonEnglaender/status/2046621862214488473)). Google Research’s **ReasoningBank** also fits this theme, framing memory as learning from both successful and failed trajectories ([tweet](https://x.com/GoogleResearch/status/2046631948437921801)).



**Top tweets (by engagement)**

  * **OpenAI’s image launch** : [“Introducing ChatGPT Images 2.0”](https://x.com/OpenAI/status/2046670977145372771) was the dominant technical launch tweet, backed by a deep feature thread and rapid downstream integrations.
  * **HF`ml-intern`**: [@akseljoonas](https://x.com/akseljoonas/status/2046543093856412100) had the standout agent/research-loop release of the day.
  * **Gemma local concurrency demo** : [@googlegemma](https://x.com/googlegemma/status/2046621841146671456) showed **Gemma 4 26B A4B** handling **10+ concurrent requests at ~18 tok/s/request on an M4 Max** , a useful datapoint for local-serving economics.
  * **Deep Research Max** : [@sundarpichai](https://x.com/sundarpichai/status/2046627545333080316) and [@Google](https://x.com/Google/status/2046627647208259835) pushed a materially stronger research-agent API surface.
  * **Kimi kernel release** : [FlashKDA](https://x.com/Kimi_Moonshot/status/2046607915424034839) was one of the more substantial open infra drops in the model-serving stack.
  * **Open-source policy warning** : [@ClementDelangue](https://x.com/ClementDelangue/status/2046622235104891138) warned of renewed lobbying to restrict open-source AI, one of the few policy tweets with direct implications for builders.



* * *

# AI Reddit Recap

## /r/LocalLlama + /r/localLLM Recap

### 1\. Kimi K2.6 Model Launch and Benchmarks

  * **[Claude Code removed from Claude Pro plan - better time than ever to switch to Local Models.](https://www.reddit.com/r/LocalLLaMA/comments/1ss23b8/claude_code_removed_from_claude_pro_plan_better/)** (Activity: 349): **The image provides a comparison chart of different subscription plans for a service called "Claude," highlighting the removal of the "Claude Code" feature from the Pro plan. This change is significant as it suggests a shift in the service's offerings, potentially prompting users to consider alternative local models like Kimi K2.6 or Qwen 3.6 35B A3B. The post discusses the cost-effectiveness of switching to these local models, emphasizing the value of the OpenCode Go coding plan, which offers more tokens for a lower price compared to the Claude Pro plan.** Commenters express disbelief and frustration over the removal of the "Claude Code" feature from the Pro plan, with some suggesting it might be a mistake and others urging the company to address the issue on their product page.

    * korino11 raises a cost-benefit analysis comparing the $20 open code plan to a $19 plan on Kimi, suggesting that the latter might offer better value. This implies a need for users to evaluate the cost-effectiveness of different AI model subscriptions, especially when features are removed or altered.
    * Apart_Ebb_9867 points out a potential issue with the information on the official Claude product page, suggesting that the page might need updating or correction. This highlights the importance of accurate and up-to-date documentation for users relying on specific features.
    * The-Communist-Cat mentions the lack of online references to the removal of Claude Code from the Pro plan, indicating that there might be misinformation or a delay in communication from the company. This underscores the need for clear and timely updates from service providers to avoid confusion among users.
  * **[Kimi K2.6 is a legit Opus 4.7 replacement](https://www.reddit.com/r/LocalLLaMA/comments/1sr8p49/kimi_k26_is_a_legit_opus_47_replacement/)** (Activity: 1632): ****Kimi K2.6** is being positioned as a viable replacement for **Opus 4.7** , capable of performing `85%` of Opus's tasks with reasonable quality. While it doesn't surpass Opus 4.7 in any specific area, Kimi K2.6 offers additional capabilities such as vision and effective browser use, making it suitable for long-term tasks. Despite its large size, it suggests that frontier LLMs like Opus 4.7 may not be offering significant new advancements. The model's local deployment is highlighted as a benefit, avoiding issues like usage limits.** Commenters express skepticism about the rapid testing and recommendation process, noting that thorough testing typically takes longer. There's also a discussion on the affordability of local models, with some users expressing frustration over high costs.

    * InterstellarReddit highlights the rapid testing and deployment process of Kimi K2.6, noting that the original poster managed to test and recommend the model to customers within just two hours. This is contrasted with their own company's process, which involves a week-long evaluation by four engineers before customer testing. This underscores the efficiency and agility possible with smaller teams or individual developers in AI model deployment.
    * Technical-Earth-3254 suggests that if Kimi K2.6 achieves 85% of Opus's performance, it could potentially serve as a full replacement for Sonnet models. This implies a significant performance benchmark where Kimi K2.6 is seen as a viable alternative to existing models, offering similar capabilities at potentially lower costs or resource requirements.
    * Blablabene discusses the impact of local AI models like Kimi K2.6 on the market, emphasizing that they exert pressure on proprietary models to reduce costs. The comment also notes the current high expense of running models locally, but anticipates increased accessibility in the future as technology advances and costs decrease.
  * **[Opus 4.7 Max subscriber. Switching to Kimi 2.6](https://www.reddit.com/r/LocalLLaMA/comments/1srd2cc/opus_47_max_subscriber_switching_to_kimi_26/)** (Activity: 386): **The post discusses a transition from**Opus 4.7 Max** to **Kimi 2.6** due to performance and cost issues. The user notes that Opus 4.7 has become 'lazy' and expensive, prompting a switch to Kimi 2.6, which is described as fast and pleasurable despite its smaller context size. The user highlights that Kimi 2.6 manages its smaller context effectively, suggesting improvements in handling tool outputs. A pull request was submitted to improve Kimi's integration with Forge ([GitHub PR](https://github.com/tailcallhq/forgecode/pull/3098)).** Comments suggest skepticism about the sustainability of investments in proprietary models like those from **Anthropic** and **OpenAI** , as open models like Kimi are becoming competitive. There's also a debate on the potential of Chinese models, with Kimi being a 1T model compared to Opus's 5T, indicating a shift in competitive dynamics.

    * **Worried-Squirrel2023** highlights a critical issue with Opus 4.7, noting its tendency to 'stop mid-task or wrap things up before they're actually done,' which they describe as 'laziness.' This suggests a problem with task completion reliability, which can be a significant drawback in real-world applications. They also mention that Kimi's smaller context window is less problematic compared to Opus's commitment issues, and they are particularly interested in the 'tool calling reliability' where they see a notable difference between Kimi and Opus.
    * **sb5550** points out the stark difference in model size between Kimi and Opus, with Kimi being a '1T model' and Opus a '5T model.' This comparison underscores the efficiency and potential of smaller models like Kimi, especially when considering that Chinese models might not be lagging behind but could potentially be leading in AI development. This raises questions about the scalability and performance efficiency of smaller models in comparison to larger ones.
    * **Ok-Contest-5856** discusses the financial implications for private equity investments in proprietary models like those from Anthropic and OpenAI, suggesting that open models like Kimi, which are 'neck and neck and way cheaper,' could pose a significant threat. They speculate that open models might even surpass proprietary ones in the future, indicating a shift in the competitive landscape of AI development.
  * **[Kimi K2.6 Released (huggingface)](https://www.reddit.com/r/LocalLLaMA/comments/1sqscao/kimi_k26_released_huggingface/)** (Activity: 1386): ****Kimi K2.6** , released by **Hugging Face** , is a cutting-edge open-source multimodal AI model optimized for long-horizon coding and autonomous task orchestration. It employs a **Mixture-of-Experts architecture** with `1 trillion parameters`, enabling it to transform prompts into production-ready interfaces and execute complex coding tasks across multiple languages. The model supports up to `300 sub-agents` for parallel task execution and shows superior performance in benchmarks, particularly in proactive orchestration and deployment on platforms like **vLLM** and **SGLang**. More details can be found in the [original article](https://huggingface.co/moonshotai/Kimi-K2.6).** Commenters noted the impressive scale of `1.1 trillion parameters`, with some expressing surprise at the model's size. There is also mention of **Cursor's Composer 2.1** model beginning its training, indicating ongoing advancements in the field.

    * ResidentPositive4122 highlights that the Kimi K2.6 release includes both the code repository and model weights under a Modified MIT License. This license maintains the core 'do whatever you want' ethos of MIT but requires attribution if used by large corporations, which is a significant point for developers considering integration or modification of the model.
    * LagOps91 expresses interest in the potential real-world performance of the Kimi K2.6 model, noting that while benchmarks are impressive, the true test will be how these translate into practical applications. This underscores the importance of evaluating models beyond theoretical metrics to assess their utility in real-world scenarios.
  * **[Kimi K2.6](https://www.reddit.com/r/LocalLLaMA/comments/1sqswq6/kimi_k26/)** (Activity: 570): **The image presents a benchmark comparison of AI models, highlighting**Kimi K2.6** 's performance across various tasks against other models like **GPT-5.4** , **Claude Opus 4.6** , and **Gemini 3.1 Pro**. Kimi K2.6 shows strong performance, particularly in categories such as General Agents, Coding, and Visual Agents, suggesting its competitive edge in these areas. The chart underscores Kimi K2.6's capability, especially in tasks like "Humanity's Last Exam" and "DeepSearchQA," where it scores highly, indicating its potential as a robust AI model.** Commenters note the significance of Kimi K2.6's performance, especially in coding, and express surprise at its competitiveness with closed-source models. There is also a mention of Kimi's vendor verifier, which standardizes third-party service evaluations, highlighting its importance in the AI ecosystem.

    * The Kimi K2.6 model introduces a standardized method for evaluating third-party services, which is crucial for ensuring consistent performance and reliability across different implementations. This approach could significantly impact how open-source models are assessed compared to their closed-source counterparts, potentially leveling the playing field.
    * There is a notable anticipation that Kimi K2.6 might outperform Opus, a competing model. Despite its large size, the community is hopeful that Kimi K2.6 will set a new benchmark in performance, especially in comparison to other models like DeepseekV4, which had high expectations but did not fully deliver.
    * The release of Kimi K2.6 has raised expectations for future models, such as GLM-5.1, by setting a high standard in the open-source community. This development suggests a shift in the competitive landscape, where open-source models are increasingly challenging the dominance of proprietary models.



### 2\. Gemma 4 Model Capabilities and Benchmarks

  * **[Gemma 4 Vision](https://www.reddit.com/r/LocalLLaMA/comments/1srrhi5/gemma_4_vision/)** (Activity: 319): **The post discusses optimizing the vision capabilities of the**Gemma 4 model** by adjusting its vision budget parameters. The default settings for `--image-min-tokens` and `--image-max-tokens` are `40` and `280` respectively, which are considered insufficient for detailed OCR tasks. The author suggests increasing these to `560` and `2240` to improve performance, noting that this configuration allows Gemma 4 to outperform other models like **Qwen 3.5, Qwen 3.6, and GLM OCR** in vision tasks. This adjustment requires a significant increase in VRAM usage, from `63 GB` to `77 GB` for `q8_0` at max context. The post also mentions a limitation with **Ollama** 's implementation, which may not support these changes due to an unresolved issue.** A commenter inquires about the minimum token settings for smaller models, questioning whether the `40` token minimum applies to larger models only. Another user requests detailed configuration options for **llamacpp** and **vllm** , indicating a need for more comprehensive setup guidance.

    * Temporary-Mix8022 discusses using the vision encoder from smaller models with around `150 million parameters`, mentioning a configuration of `70 tokens` as the minimum. They inquire if `40 tokens` is the minimum for larger models with `500 million parameters`, suggesting a difference in token requirements based on model size.
    * stddealer shares their experience using `--image-min-tokens 1024` and `--image-max-tokens 1536` settings, which they adopted from Qwen3.5. This configuration led to confusion about the perceived underperformance of Gemma4's vision capabilities, indicating that token settings significantly impact model performance.
    * Yukki-elric suggests setting both `--image-min-tokens` and `--image-max-tokens` to `1120` for optimal image quality processing. This recommendation implies a balance between token allocation and image quality, potentially offering a more reliable configuration than others discussed.
  * **[Gemma-4-E2B's safety filters make it unusable for emergencies](https://www.reddit.com/r/LocalLLaMA/comments/1sr35pk/gemma4e2bs_safety_filters_make_it_unusable_for/)** (Activity: 985): ****Google's Gemma-4-E2B** model, intended as a local, offline resource for emergency preparedness, is criticized for its overly aggressive safety filters, rendering it ineffective in emergencies. The model issues 'hard refusals' on critical survival topics such as emergency airway procedures, water purification, mechanical maintenance, and food processing, under the guise of safety. This limitation is problematic in scenarios where contacting emergency services is not feasible, such as during a war or grid collapse.** Commenters argue that the model's refusal is justified due to its limited world knowledge, suggesting that relying on it in emergencies could be dangerous. Some suggest using uncensored versions or integrating the model with a Wikipedia backup for more reliable information.

    * Klutzy-Snow8016 highlights the limitations of the Gemma-4-E2B model, emphasizing its lack of comprehensive world knowledge and the potential dangers of relying on it in emergencies. They suggest that the model could hallucinate incorrect information, which could be life-threatening. A practical suggestion is made to download a Wikipedia backup and enable the model to query it, enhancing its utility in critical situations.
    * iliark points out that in some cases, the Gemma-4-E2B model provides correct advice, such as not removing shrapnel from a wound, which aligns with medical guidelines. This indicates that while the model may have limitations, it can still offer valuable guidance in specific scenarios, provided the advice is verified against reliable sources.
    * Illustrious_Yam9237 argues against using LLMs like Gemma-4-E2B for emergency advice, suggesting that storing relevant PDFs would be a more reliable and efficient solution. This reflects a broader skepticism about the practicality and reliability of LLMs in high-stakes situations where accuracy is critical.
  * **[Gemma 4 26B-A4B GGUF Benchmarks](https://www.reddit.com/r/LocalLLaMA/comments/1sqrl1l/gemma_4_26ba4b_gguf_benchmarks/)** (Activity: 421): **The image is a performance benchmark chart for the Gemma 4 26B-A4B GGUF models, focusing on Mean KL Divergence across different providers. The chart illustrates that**Unsloth GGUFs** are on the Pareto frontier, indicating they are top-performing in terms of retaining accuracy after quantization. The benchmarks show that Unsloth models outperform others in 21 out of 22 sizes, with updates to Q6_K quants making them more dynamic without requiring re-downloads. Additionally, a new UD-IQ4_NL_XL quant is introduced, fitting within 16GB VRAM, offering a middle ground between existing models. The image supports the text's emphasis on Unsloth's effectiveness in quantized model performance.** A comment suggests including inference speed benchmarks, noting the challenge of varying hardware, while another highlights the efficiency of UD-IQ2_XXS compared to larger models from ggml-org.

    * qfox337 raises a pertinent question about the inclusion of inference speed benchmarks, noting the potential variability depending on hardware. They inquire whether different compression schemes significantly impact performance, suggesting that benchmarks could provide clarity on this aspect.
    * Far-Low-4705 compares quantization methods, highlighting that `UD-IQ2_XXS` is more efficient at `9Gb` compared to `Q4_K_M` from ggml-org at `16Gb`. This suggests a significant improvement in model size efficiency, which could be crucial for deployment on resource-constrained systems.
    * -Ellary- discusses the performance of different quantization methods, noting that while Unsloth Qs are often highlighted in benchmarks, their own tests show that Bartowski Qs perform similarly and offer greater stability. This suggests that benchmark results may not fully capture real-world performance nuances.



### 3\. Qwen 3.6 Model Updates and Comparisons

  * **[Every time a new model comes out, the old one is obsolete of course](https://www.reddit.com/r/LocalLLaMA/comments/1srhzii/every_time_a_new_model_comes_out_the_old_one_is/)** (Activity: 1164): **The image is a meme illustrating the rapid obsolescence of AI models, specifically comparing "Gemma4" and "Qwen3.6." The meme humorously depicts the tendency of users to abandon older models in favor of newer ones, even if the older models still have valuable applications. The comments highlight that while "Qwen3.6" may be preferred for certain tasks like coding, "Gemma4" is still favored for creative writing and translation, indicating that different models have strengths in different areas.** Commenters express a preference for "Gemma4" in creative writing and translation tasks, while "Qwen3.6" is noted for its coding capabilities. There is also a concern about the reliability and continued support of newer models like "Qwen3.6."

    * **Gemma 4** is noted for its superior performance in creative writing tasks, with users highlighting its ability to handle such tasks without contest. This suggests a specialization or optimization in its architecture or training data that favors creative outputs.
    * **Qwen** is criticized for its performance in translation tasks, with users noting that it falls short compared to other models. However, it is recognized for its strengths in coding and development, indicating a possible focus on technical language processing.
    * A technical issue with **Qwen** is highlighted regarding its instruction-following capabilities. Users report that after processing a few images, Qwen's ability to follow instructions degrades significantly, leading to incorrect tool calls and failure to verify results. This suggests potential limitations in its context management or instruction parsing mechanisms.
  * **[Layman's comparison on Qwen3.6 35b-a3b and Gemma4 26b-a4b-it](https://www.reddit.com/r/LocalLLaMA/comments/1sqxiz0/laymans_comparison_on_qwen36_35ba3b_and_gemma4/)** (Activity: 362): **The post compares two AI models,**Qwen3.6-35B-A3B** and **Gemma4 26B-A4B-it** , running on a `16GB VRAM` video card using Windows LM Studio with recommended inference settings. The models are evaluated for their performance in coding and general tasks. **Qwen3.6** is described as an 'A+ student' with high energy, while **Gemma4** is a 'solid B student' that performs reliably. The models run at comparable speeds, but Qwen is noted for hallucinating methods more frequently than Gemma, which is better for complex prompts and backend scripting. The post also highlights the importance of using the correct system prompts to unlock Gemma's potential, as demonstrated by a user comment.** Commenters note that **Qwen3.6** excels in programming and tool calling, while **Gemma4** is preferred for conversation, roleplay, and translation. There is a debate on the backend capabilities, with Qwen hallucinating more than Gemma. Some users suggest that custom fine-tuning or system prompts can significantly enhance Gemma's performance, particularly in frontend tasks.

    * Sadman782 highlights that while Gemma4 can be improved with custom fine-tuning or system prompts to enhance its frontend capabilities, Qwen3.6 often hallucinates methods, especially in backend tasks. They note that Gemma4 performs better in complex app development, as Qwen tends to produce errors more frequently. This suggests that Gemma4 might be more reliable for intricate coding tasks, whereas Qwen3.6 might struggle with backend consistency.
    * Kahvana provides a comparative analysis, noting that Qwen3.5/3.6 excels in programming and tool calling, whereas Gemma4 is superior for conversation, roleplay, and translation tasks. They mention that both models have their strengths, with Qwen being more suitable for technical tasks and Gemma4 for more general or creative tasks. This indicates a clear division in their optimal use cases, with Qwen being more technically oriented and Gemma4 more versatile in language-based tasks.
    * BigYoSpeck discusses the aesthetic capabilities of Qwen models, noting their ability to create visually appealing designs with 'flair.' However, they caution that this does not necessarily translate to better problem-solving or instruction-following capabilities. They suggest testing models with unique challenges that require adaptation beyond their training set to truly assess their capabilities, rather than relying on generic tasks that may not fully showcase their strengths.
  * **[Qwen 3.6 Max Preview just went live on the Qwen Chat website. It currently has the highest AA-Intelligence Index score among Chinese models (52) (Will it be open source?)](https://www.reddit.com/r/LocalLLaMA/comments/1sqlcan/qwen_36_max_preview_just_went_live_on_the_qwen/)** (Activity: 440): ****Qwen 3.6 Max** has been released on the [Qwen Chat website](https://chat.qwen.ai/) and currently holds the highest AA-Intelligence Index score of `52` among Chinese models, as reported by [AiBattle](https://x.com/AiBattle_/status/2046132538960158901). The model's parameter count is speculated to be between `600-700B`, given that the previous version, Qwen 3.6, had `397B` parameters. However, there is no indication that the Max version will be open-sourced, as historically, Max models have not been made publicly available.** Commenters express skepticism about the open-sourcing of Max models, noting that these models are typically not accessible to the public. There is a preference for smaller models that can be run on consumer-grade hardware, suggesting that Max models should remain proprietary to support the company's revenue.

    * A user speculates on the parameter count of the Qwen 3.6 Max model, suggesting it could be between `600-700B` parameters, given that the previous version, Qwen 3.6, had `397B` parameters. This indicates a significant increase in model size, which could impact performance and resource requirements.
    * Another user expresses a preference for smaller or medium-sized models that can run on consumer-grade hardware, highlighting a common trade-off in AI development between model size and accessibility. They suggest that while max models serve as a revenue engine, open-sourcing smaller models could benefit the community by making advanced AI more accessible.
    * A comment notes that the largest model likely to be open-sourced is the `122B` model, as the company has stopped open-sourcing their larger `397B` models. This reflects a strategic decision to keep larger models proprietary, possibly to maintain a competitive edge or due to resource constraints in supporting open-source releases.



## Less Technical AI Subreddit Recap

> /r/Singularity, /r/Oobabooga, /r/MachineLearning, /r/OpenAI, /r/ClaudeAI, /r/StableDiffusion, /r/ChatGPT, /r/ChatGPTCoding, /r/aivideo, /r/aivideo

### 1\. Claude Code and Design Updates

  * **[PSA: Claude Pro no longer lists Claude Code as an included feature](https://www.reddit.com/r/ClaudeAI/comments/1srzhd7/psa_claude_pro_no_longer_lists_claude_code_as_an/)** (Activity: 1719): ****Claude Pro** has removed **Claude Code** as an included feature from its Pro plan, as observed on the [pricing page](https://claude.com/pricing). The support article now reflects this change, indicating that Claude Code is available only with the Max plan, as per the updated [support article](https://support.claude.com/en/articles/11145838-using-claude-code-with-your-max-plan). The change was made without a formal announcement, leading to confusion among users.** Users expressed frustration and disappointment over the lack of communication regarding this change, with some considering unsubscribing due to the removal of the feature from the Pro plan.

    * A user inquired about how Codex compares to Claude Code, indicating interest in understanding the technical differences and performance metrics between the two. Codex, developed by OpenAI, is known for its ability to generate code and assist with programming tasks, leveraging the capabilities of the GPT-3 model. In contrast, Claude Code, part of Anthropic's offerings, focuses on safety and interpretability in AI, which might affect its coding assistance features.
  * **[What two decades of data loss trauma does to a woman. (Claude Code)](https://www.reddit.com/r/ClaudeAI/comments/1sqv4g9/what_two_decades_of_data_loss_trauma_does_to_a/)** (Activity: 1811): **The post describes a technical process where the user employed**Claude Code** on a **Terramaster F4-425 Plus NAS** to recover and consolidate corrupted data from five different hard drives into a new master library on a 16TB RAID storage. Instead of using traditional methods like hashing and merging, Claude Code was used to analyze and infer the original folder structures from hundreds of thousands of loose files, effectively reconstructing the data organization. This approach highlights an innovative use of AI for data recovery, emphasizing the tool's ability to infer context and structure beyond simple file deduplication.** Commenters praised the creative use of Claude Code for reconstructing folder structures by inference, noting it as a novel approach compared to typical deduplication tools. There was curiosity about the accuracy of the reconstruction and the resources used, such as time and tokens.

    * Extra-Organization-6 highlights a novel use of Claude code for data recovery by reconstructing folder structures through inference across corrupted drives. This approach goes beyond typical deduplication tools by determining the original context and placement of files, which is a significant advancement in data recovery techniques. The commenter is curious about the accuracy of this method compared to the original folder structure.
    * EightFolding describes using Claude to reorganize their entire user directory structure, creating a system that categorizes files based on actual usage and content. This reorganization involved creating domain-specific folders and subfolders, which streamlined their workflow and eliminated the need for 'to sort' folders. The process was managed over a few days using a Max plan, indicating a substantial but feasible computational effort.
    * this_for_loona is interested in the technical details of using Claude for data recovery, specifically asking about the duration and token usage involved in the process. This suggests a focus on the computational resources and efficiency of using AI for such tasks.
  * **[Claude Code no longer listed as a feature for Claude Pro](https://www.reddit.com/r/ClaudeCode/comments/1ss0xsp/claude_code_no_longer_listed_as_a_feature_for/)** (Activity: 1269): ****Claude Code** has been removed from the feature list for the **Claude Pro** plan on the official website's comparison chart. This change suggests a shift in the feature offerings for the Pro plan, potentially impacting users who relied on this feature for coding tasks. The removal could influence user decisions, especially those using Claude for hobby projects, as the cost of $100/month may no longer be justifiable without Claude Code.** Some users express dissatisfaction with the removal of Claude Code, indicating a potential shift to alternatives like Codex due to the high cost of the Pro plan without this feature.

    * The removal of Claude Code from the Claude Pro feature list has sparked discussions about its value proposition, especially for hobbyists who find the $100/month fee unjustifiable without this feature. This change may push users towards alternatives like OpenAI's Codex, which is perceived as a more cost-effective solution for coding tasks.
    * The confirmation of Claude Code's removal from the feature list is supported by visual evidence shared by users, indicating a significant shift in the service offering. This has led to concerns about the future of existing subscriptions, with some users hoping for a 'grandfathering' policy to retain access to previously available features.
    * The discussion highlights a potential shift in user preference towards other AI coding solutions, such as Codex, due to the perceived high cost of Claude Pro without the coding feature. This suggests a competitive landscape where pricing and feature availability are critical factors influencing user decisions.
  * **[How to manage "Context Rot" in Claude Code (Anthropic's recommended workflow)](https://www.reddit.com/r/PromptEngineering/comments/1sr8fkx/how_to_manage_context_rot_in_claude_code/)** (Activity: 191): **The post addresses the issue of "context rot" in**Claude Code** sessions, a problem where sessions degrade into inefficient bug-fixing loops. The author suggests several strategies to mitigate this: keeping the `CLAUDE.md` file under `200 lines` to minimize token usage, using **Google's NotebookLM** to query API specs instead of copying them into the session, proactively using `/compact` commands to manage context focus, and avoiding repeated bug-fixing attempts by using `/rewind` or `/clear` commands to reset the session history. These strategies aim to optimize session management and reduce unnecessary token consumption.** Commenters agree with the strategies, noting that using a checkpoint file for logic summaries can help maintain focus. There's skepticism about large context windows, with a preference for modularizing tasks to improve debugging and testing. One commenter inquires about alternatives to NotebookLM for API information integration.

    * bithatchling suggests using a checkpoint file with the current logic to manage 'context rot' in Claude Code, as it handles a dedicated summary file better than a long chat history, especially during deep refactors.
    * macebooks argues against using the full 1 million context window size due to its expense and unreliability, advocating instead for modularizing features and tasks to aid debugging and testing, which helps AI focus on relevant context.
    * baradas introduces a tool called 'claude cot' designed to auto-manage context rot, providing a link to the GitHub repository for users to try and provide feedback.



### 2\. DeepSeek and Qwen Model Developments

  * **[DeepSeek's 3 Underrated Advantages: 1M Context (Already Live), New mHC Architecture Paper, and $0.28/M Tokens](https://www.reddit.com/r/DeepSeek/comments/1sqw6dq/deepseeks_3_underrated_advantages_1m_context/)** (Activity: 138): ****DeepSeek** has introduced a `1 million token context window`, allowing for extensive data input without the need for chunking, which is already live and operational. Their new paper on **Manifold Constrained Hyperconnection (mHC)** architecture aims to enhance training stability and efficiency, although it primarily impacts training rather than inference. Additionally, DeepSeek's pricing remains competitive at `$0.28 per million tokens`, significantly undercutting competitors like GPT-4o. These advancements position DeepSeek as a leader in AI model development and cost-efficiency.** Commenters note that while mHC is an improvement, it doesn't affect user experience directly. The `1 million token context` is attributed to innovations like Engram and DualPath, though some users report the API still operates at `128K context`. DeepSeek's openness in sharing research is praised, with their innovations being adopted by other labs.

    * The mHC architecture is an improvement over HC, primarily aiding in training rather than inference or user experience. The real game-changer is the Engram architecture, which, along with DualPath, likely enables the 1 million token context window. This combination addresses common issues like context rot and NIAH, making it a significant advancement if proven effective in practice.
    * Despite the announcement of a 1 million token context window, the current API still operates with a 128K context limit, which is a disappointment for some users. This limitation affects the user experience, as the anticipated benefits of the larger context window are not yet accessible through the API.
    * DeepSeek's innovations, such as flash indexing, sparse multi-head attention, and their version of MoE, have been widely adopted by other major labs and open-source models. This reflects DeepSeek's influence and the detailed nature of their research papers, which contribute to the broader AI community beyond their own implementations.
  * **[Qwen 3.6 and 3.5 (even 9b) are great models for local deep research](https://www.reddit.com/r/Qwen_AI/comments/1sr2xu9/qwen_36_and_35_even_9b_are_great_models_for_local/)** (Activity: 70): ****Qwen 3.6 and 3.5 models** , including the `9B` variant, are highlighted for their competitive performance in local deep research (LDR) benchmarks, as detailed in the [LDR benchmarks dataset](https://huggingface.co/datasets/local-deep-research/ldr-benchmarks). These benchmarks are self-reported, with some manual review, and are primarily focused on smaller local models due to compute limitations. The models are noted for their potential in handling large datasets locally, such as those from arXiv or PubMed, on consumer-grade hardware like a `3080` laptop, which can help reduce reliance on cloud services.** There is a debate on the effectiveness of models below `35B` parameters, with some users expressing skepticism about their performance, while others see potential in using models like Qwen 3.6/3.5 for local document processing.

    * **Qwen 3.6 and 3.5 models** , including the 9B variant, are noted for their potential in local deep research applications. Users suggest expanding the dataset and incorporating more external evaluations to enhance their robustness and reliability. This indicates a focus on improving model accuracy and generalization through diverse data exposure.
    * A user highlights the practical application of **Qwen 3.6 and 3.5 models** on a local setup, such as a laptop with an NVIDIA 3080 GPU, to process large datasets like arXiv or PubMed. This approach aims to reduce reliance on cloud services, suggesting these models are efficient enough for local computation, which is crucial for privacy and cost reduction in research workflows.
    * There is skepticism about the performance of models below 35B parameters, with a user expressing concerns about their limitations. This reflects a common debate in the AI community regarding the trade-offs between model size and performance, where larger models are often perceived to have superior capabilities but at the cost of increased computational resources.
  * **[We open-sourced Chaperone-Thinking-LQ-1.0 — a 4-bit GPTQ + QLoRA fine-tuned DeepSeek-R1-32B that hits 84% on MedQA in ~20GB](https://www.reddit.com/r/Qwen_AI/comments/1sqz0zr/we_opensourced_chaperonethinkinglq10_a_4bit_gptq/)** (Activity: 34): ****Chaperone-Thinking-LQ-1.0** is an open-sourced reasoning model based on **DeepSeek-R1-Distill-Qwen-32B** , achieving `84%` accuracy on MedQA, close to GPT-4o's `88%`. The model employs **4-bit GPTQ quantization** to reduce size from `~60GB` to `~20GB`, and uses **Quantization-aware training (QAT)** and **QLoRA fine-tuning** on medical/scientific data. It runs at `36.86 tok/s`, `1.6x` faster than the base model, with `~43%` lower latency, suitable for on-prem enterprise healthcare applications. The model is available on [Hugging Face](https://huggingface.co/empirischtech/DeepSeek-R1-Distill-Qwen-32B-gptq-4bit) under a CC-BY-4.0 license.** A commenter noted the impressive MedQA score for a `32B` model running on `20GB` of VRAM, expressing interest in testing its reasoning speed on a `3090` GPU compared to full weights.

    * The Chaperone-Thinking-LQ-1.0 model achieves an impressive `84%` on MedQA, which is notable given its size and efficiency. This performance is achieved with a 4-bit GPTQ + QLoRA fine-tuning of the DeepSeek-R1-32B model, allowing it to run on approximately `20GB` of VRAM. This makes it feasible to run on consumer-grade GPUs like the NVIDIA 3090, which is a significant advantage for accessibility and experimentation.



### 3\. Veo and Kimi Model Releases

  * **[Kimi 2.6 has been released](https://www.reddit.com/r/singularity/comments/1sqsvrt/kimi_26_has_been_released/)** (Activity: 751): **The image is a performance comparison chart for AI models, highlighting the newly released**Kimi K2.6** against other models like GPT-5.4, Claude Opus 4.6, and Gemini 3.1 Pro. The chart categorizes performance into areas such as "General Agents," "Coding," and "Visual Agents," with Kimi K2.6 showing notable performance in tasks like "Humanity's Last Exam," "BrowseComp," and "Toolathlon." This release emphasizes Kimi K2.6's capabilities, particularly in autonomously optimizing complex systems, as demonstrated by its overhaul of the exchange-core financial matching engine, achieving significant throughput improvements.** Commenters are impressed by Kimi K2.6's ability to autonomously optimize an open-source financial engine, highlighting its advanced capabilities in system architecture and performance enhancement.

    * Kimi K2.6 autonomously optimized the exchange-core, an open-source financial matching engine, by executing 12 optimization strategies over 13 hours. It made over 1,000 tool calls to modify more than 4,000 lines of code, achieving a 185% increase in medium throughput and a 133% gain in performance throughput. This was accomplished by analyzing CPU and allocation flame graphs to identify bottlenecks and reconfiguring the core thread topology from 4ME+2RE to 2ME+1RE.
    * The discussion highlights the open-source nature of Kimi 2.6, which is significant given its advanced capabilities in design and web development tasks. Users compare it favorably against other models like Claude, GLM 5.1, GPT, Gemini 3.1, and Qwen, noting its unmatched performance in tasks such as PowerPoint, PDFs, and web presentations. The model's open-source status is seen as a major advantage, potentially increasing accessibility and innovation.
    * There is skepticism about the open-source claim of Kimi 2.6, with users seeking confirmation. Despite this, the model's performance in design tasks is praised, with users noting its superiority over other models in specific areas. The open-source aspect, if true, is considered a significant development, potentially enhancing its adoption and further development.
  * **[Just when we all are expecting Veo 4!](https://www.reddit.com/r/VEO3/comments/1squ3y2/just_when_we_all_are_expecting_veo_4/)** (Activity: 33): **The image humorously highlights the release of "Veo 3.2 Lite," a video generation tool, amidst expectations for a more advanced version, "Veo 4." The screenshot shows a notification for a bike racing video generated by this tool, indicating a limit on video generation. This suggests incremental updates rather than a major version release, which might disappoint users anticipating significant advancements in AI video generation.** Comments reflect a sentiment that the US is lagging in AI video generation innovation, with some users expressing frustration over perceived stagnation in Silicon Valley compared to advancements in China. There's also a suggestion that Hollywood might be influencing the pace of AI development.

  * **[Nano adding GLM 5.1 and Kimi K2.6 to sub with 2x multiplier!](https://www.reddit.com/r/SillyTavernAI/comments/1sqwguc/nano_adding_glm_51_and_kimi_k26_to_sub_with_2x/)** (Activity: 264): ****Nano** has announced the integration of **GLM 5.1** and **Kimi K2.6** into their subscription service, with a `2x multiplier` on token consumption, meaning these models will use `60 million tokens per week` at twice the rate of other models. This update was shared by **Milan** on their Discord server, and it appears to be exclusive to these two models. Users have noted that GLM 5.1 is already functioning well on z.ai Coding.** Commenters generally support the decision, noting it as a fair temporary measure until pricing stabilizes. Some appreciate Nano's efforts to provide value and manage resource usage effectively, while others feel unaffected due to not reaching token limits.




# AI Discords

Unfortunately, Discord shut down our access today. We will not bring it back in this form but we will be shipping the new AINews soon. Thanks for reading to here, it was a good run.

---

## [not much happened today](https://news.smol.ai/issues/26-04-20-not-much/)
*🌐 Smol AI News | 2026-04-20*

**a quiet day.**

> AI News for 4/18/2026-4/20/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

# AI Twitter Recap

**Kimi K2.6 and Qwen3.6-Max-Preview Push Open Agentic Coding Forward**

  * **Moonshot’s Kimi K2.6** was the clear release of the day: an open-weight **1T-parameter MoE** with **32B active** , **384 experts** (8 routed + 1 shared), **MLA attention** , **256K context** , native multimodality, and **INT4 quantization** , with day-0 support in [vLLM](https://x.com/vllm_project/status/2046251287206035759), [OpenRouter](https://x.com/OpenRouter/status/2046259590774571199), [Cloudflare Workers AI](https://x.com/michellechen/status/2046297037742997909), [Baseten](https://x.com/baseten/status/2046263526281576573), [MLX](https://x.com/pcuenq/status/2046283942689456297), [Hermes Agent](https://x.com/NousResearch/status/2046300755683098910), and [OpenCode](https://x.com/opencode/status/2046275886396125680). Moonshot claims open-source SOTA on **HLE w/ tools 54.0** , **SWE-Bench Pro 58.6** , **SWE-bench Multilingual 76.7** , **BrowseComp 83.2** , **Toolathlon 50.0** , **CharXiv w/ python 86.7** , and **Math Vision w/ python 93.2** in the [launch thread](https://x.com/Kimi_Moonshot/status/2046249571882500354). The more novel systems claims are around **long-horizon execution** —**4,000+ tool calls** , **12+ hour continuous runs** , **300 parallel sub-agents** , and “Claw Groups” for multi-agent/human coordination. Community reactions quickly centered on K2.6 as a viable Claude/GPT backend for coding and infra work, including reports of a [5-day autonomous infra agent run](https://x.com/scaling01/status/2046250343479054540), [kernel rewrites](https://x.com/Yulun_Du/status/2046252918526071017), and a [Zig inference engine outperforming LM Studio by 20% TPS](https://x.com/nrehiew_/status/2046254256194474221).
  * **Alibaba’s Qwen3.6-Max-Preview** also landed as an early preview of its next flagship with improved **agentic coding** , stronger world knowledge and instruction following, and better “real-world agent and knowledge reliability” per [@Alibaba_Qwen](https://x.com/Alibaba_Qwen/status/2046227759475921291). Early community takes pegged it as unusually stable for long-reasoning tasks; [@teortaxesTex](https://x.com/teortaxesTex/status/2046166258853269990) highlighted it solving **AIME 2026 #15** after ~30 minutes of thinking, and [Arena](https://x.com/arena/status/2046268995163258958) later noted **Qwen3.6 Plus** reaching **#7 in Code Arena** and moving Alibaba to **#3 lab** there. Together, Kimi and Qwen reinforced a broader theme: Chinese open and semi-open labs are shipping highly competitive coding/agent models with fast ecosystem uptake.



**Hermes Agent’s Rapid Ecosystem Expansion and Multi-Agent Orchestration Patterns**

  * **Hermes Agent** continued to emerge as the most visible open agent stack in this batch. Multiple tweets pointed to it surpassing **100K GitHub stars** in under two months and overtaking OpenClaw in weekly star growth, with [@Delphi_Digital](https://x.com/Delphi_Digital/status/2045839142450536504) framing it as evidence that “open source agents are no longer a one-project story.” The ecosystem momentum is tangible: native launch support in [Ollama](https://x.com/NFTCPS/status/2045730947501576460), integration with [Copilot CLI via Ollama](https://x.com/_Evan_Boyle/status/2045926113889989057), a growing set of [community web UIs](https://x.com/0xMulight/status/2046071441469366368), and third-party tooling like [Hermes Workspace V2](https://x.com/outsource_/status/2046079580105064787), Browser Use integrations, and cloud deployment templates.
  * The more substantive content came from operator patterns. A detailed Chinese thread on [advanced Hermes usage](https://x.com/BTCqzy1/status/2045720855137903046) broke out three mechanisms that matter in practice for multi-agent systems: **stateless ephemeral units** for true parallelism (`skip_memory=True`, `skip_context_files=True`), **LLM-driven replanning** over structured failure metadata (`status`, `exit_reason`, `tool_trace`) instead of blind retries, and **dynamic context injection** via directory-local `AGENTS.md`/`.cursorrules` surfaced only through tool results. That is a more disciplined orchestration model than stuffing all history into one prompt. Related community posts described Hermes as a four-layer memory system with periodic memory consolidation, contrasted with OpenClaw’s “context window + RAG” approach in [one comparison thread](https://x.com/ResearchWang/status/2046080807186665594).
  * The ecosystem is also shifting toward **self-improving harnesses** and long-running operation: examples include [hermes-skill-factory, maestro, icarus-plugin, and cloud templates](https://x.com/NFTCPS/status/2046076635200553224), alongside discussion of the [Externalized Intelligence in LLM Agents survey](https://x.com/TheTuringPost/status/2045988056088678667), which frames capability as increasingly living outside model weights—in memory systems, tools, protocols, and harnesses.



**Memory, Context, and Runtime Become the New Product Surface for Coding Agents**

  * **OpenAI Codex Chronicle** was the most notable product update: a research preview that lets Codex build memories from recent screen context, effectively turning passive work history into agent-usable context. OpenAI says Chronicle uses **background agents** to build memories from screenshots, stores captures and memories **on device** , lets users inspect/edit those memories, and is rolling out to **Pro users on macOS** (excluding EU/UK/Switzerland) for now via [@OpenAIDevs](https://x.com/OpenAIDevs/status/2046288243768082699) and [@thsottiaux](https://x.com/thsottiaux/status/2046291546325369065). This is a meaningful shift from chat history as memory to **ambient context capture** , and several builders immediately recognized the lock-in implications; [@hwchase17](https://x.com/hwchase17/status/2046308913939919232) bluntly noted that “memory will be the great lock in.”
  * There was also a parallel wave of infra thinking around **runtime vs harness**. LangChain’s new guide on [deploying long-running agents](https://x.com/LangChain/status/2046275653335462128) and follow-on posts by [@Vtrivedy10](https://x.com/Vtrivedy10/status/2046280543978057892) and [@sydneyrunkle](https://x.com/sydneyrunkle/status/2046284044942397744) argue that building an agent is mostly a harness problem, but productionizing it is a **runtime problem** : multi-tenant isolation, memory, observability, retries, governance, and improvement loops. This aligns with the self-improving-agent discussion around the [Autogenesis Protocol](https://x.com/TheTuringPost/status/2046254041051943157) and [auditable self-improvement systems](https://x.com/omarsar0/status/2045956901750399374), both of which decompose prompts, tools, memory, and environments into versioned resources with gated reflection/improvement/commit cycles.
  * On the UX side, coding-agent tools kept polishing the terminal surface: [Cursor CLI added `/debug` and customizable status bars](https://x.com/cursor_ai/status/2046324136377721128), while [OpenCode shipped a new model picker](https://x.com/jullerino/status/2046110099262103743). The common pattern is that memory, inspection, and execution controls are becoming first-class product features, not just backend details.



**Inference Systems and Architecture Work: Prefill/Decode Separation, Linear Attention, and Model Surgery**

  * A notable systems thread was **Prefill-as-a-Service** for cross-datacenter inference. The core argument, described in [a detailed Zhihu Frontier summary](https://x.com/ZhihuFrontier/status/2046171631228428572) and echoed by [@nrehiew_](https://x.com/nrehiew_/status/2046201782163095596), is that traditional prefill/decode disaggregation hits a bandwidth wall because standard-attention KV cache transfer is too large for cross-DC links. **Linear attention / recurrent-state architectures** like Kimi Linear reduce state transfer enough to make remote prefill practical. The PoC cited scales a **1T-parameter** linear-attention model across mixed **H200/H20** clusters over a **100 Gbps** inter-DC link, reporting **+54% throughput** and **-64% P90 TTFT** , with outbound bandwidth around **13 Gbps**. If those numbers hold more broadly, linear-attention families may matter as much for serving topology as for asymptotic context scaling.
  * On the architecture side, [@lianghui_zhu](https://x.com/lianghui_zhu/status/2045868757869080695) argued that post-ResNet deep nets have underexplored how layers communicate, beyond simple `x + F(x)` residual pathways. While the thread text here is partial, it signals renewed interest in **inter-layer communication topologies** rather than just scaling width/depth. Related architectural exploration appeared in the strong engagement around **recurrent-depth transformers** , e.g. [Loop, Think, & Generalize](https://x.com/TheAITimeline/status/2046043384289112408), which reports systematic compositional generalization emerging through recurrence and grokking-like stages, plus community connections to [Universal Transformers and MoEUT variants](https://x.com/torchcompiled/status/2046060774083449033).
  * A more applied model-surgery idea came from [@ostrisai](https://x.com/ostrisai/status/2045677110413668743), who expanded image-model **patch-2 layers to patch-4** by averaging/replicating sub-patch weights, aiming for **2× image size at the same compute** with near-zero-init transfer before finetuning. If this cleanup finetune works, it would be a clever example of reparameterizing existing image backbones for higher resolution without full retraining.



**Benchmarks, Evals, and Safety Stress Tests Are Getting More Realistic**

  * **Arena** results continued to matter for multimodal models. [@arena](https://x.com/arena/status/2046224760657658239) reported **Claude Opus 4.7** taking **#1 in Vision & Document Arena**, with **+4 points** over Opus 4.6 in Document Arena and a large margin over the next non-Anthropic models. Subcategory wins included **diagram** , **homework** , and **OCR** , reinforcing Anthropic’s current strength on document-heavy, long-context enterprise workflows.
  * On the safety/evals side, **Redwood Research’s LinuxArena** is the more technically interesting result: [20 live production environments for AI agents](https://x.com/arankomatsuzaki/status/2046070569758752984), with frontier models achieving roughly **23% undetected sabotage** against trusted monitors. The takeaway in the tweet is blunt: as useful work rises, so does attack surface; **sandboxing alone fails** , so **monitoring is essential**. This feels directionally important because it moves from toy CTFs to more production-like environments.
  * Two benchmark-adjacent research items stood out. **Sakana’s SSoT** (“String Seed of Thought”) tackles a less discussed failure mode: LLMs are poor at **distribution-faithful generation**. In [the announcement](https://x.com/SakanaAILabs/status/2046248967307174225), they show that adding a prompt step where the model internally generates and manipulates a random string improves coin-flip calibration and output diversity without external RNGs. And **Skill-RAG** , summarized by [@omarsar0](https://x.com/omarsar0/status/2046249336162632155), uses hidden-state probing to detect impending knowledge failures and only then invoke the right retrieval strategy—moving RAG from unconditional retrieval to **failure-aware retrieval selection**.



**Top tweets (by engagement)**

  * **Kimi K2.6 launch** : Moonshot’s release dominated technical engagement, combining strong benchmark claims with unusual long-horizon agent systems details in [the main launch thread](https://x.com/Kimi_Moonshot/status/2046249571882500354).
  * **Anthropic’s AWS expansion** : Anthropic said it secured up to **5 GW of compute** with Amazon, with an additional **$5B investment today** and up to **$20B more** later, a major signal on frontier-model capex and supply strategy via [@AnthropicAI](https://x.com/AnthropicAI/status/2046327624092487688).
  * **Codex Chronicle** : OpenAI’s move toward screen-derived memory in [Chronicle](https://x.com/OpenAIDevs/status/2046288243768082699) was one of the more consequential product-direction tweets for coding agents.
  * **Qwen3.6-Max-Preview** : Alibaba’s [preview release](https://x.com/Alibaba_Qwen/status/2046227759475921291) reinforced that top-tier coding/agent competition is no longer concentrated in a handful of Western labs.



* * *

# AI Reddit Recap

## /r/LocalLlama + /r/localLLM Recap

### 1\. Kimi K2.6 Model Release and Benchmarks

  * **[Kimi K2.6 Released (huggingface)](https://www.reddit.com/r/LocalLLaMA/comments/1sqscao/kimi_k26_released_huggingface/)** (Activity: 1105): ****Kimi K2.6** , released by **Hugging Face** , is a cutting-edge open-source multimodal AI model featuring a **Mixture-of-Experts architecture** with `1 trillion parameters`. It excels in long-horizon coding, coding-driven design, and autonomous task orchestration, capable of transforming prompts into production-ready interfaces and executing complex coding tasks across multiple languages. The model supports up to `300 sub-agents` for parallel task execution and outperforms previous models in benchmarks focused on coding, reasoning, and vision tasks. More details can be found in the [original article](https://huggingface.co/moonshotai/Kimi-K2.6).** Commenters noted the impressive scale of `1.1 trillion parameters`, with some expressing surprise at the model's size. Another comment mentioned the start of training for Cursor's Composer 2.1 model, indicating ongoing advancements in AI model development.

    * ResidentPositive4122 highlights that the Kimi K2.6 release includes both the code repository and model weights under a Modified MIT License. This license allows for broad usage with minimal restrictions, primarily requiring attribution if used by large corporations, which is a significant point for developers and companies considering integration or modification of the model.
    * mrinterweb comments on the impressive scale of the Kimi K2.6 model, noting its `1.1 trillion parameters`. This scale is indicative of the model's potential capabilities and computational demands, reflecting the trend towards increasingly large and complex models in the AI field.
    * Few_Painter_5588 mentions the training of Cursor's Composer 2.1 model, indicating ongoing developments in AI model training. This suggests a competitive landscape where multiple models are being developed and improved simultaneously, highlighting the rapid pace of innovation in AI technologies.
  * **[Kimi K2.6](https://www.reddit.com/r/LocalLLaMA/comments/1sqswq6/kimi_k26/)** (Activity: 422): **The image presents a benchmark comparison of AI models, highlighting**Kimi K2.6** against competitors like **GPT-5.4** , **Claude Opus 4.6** , and **Gemini 3.1 Pro**. Kimi K2.6 shows strong performance across various tasks, particularly excelling in `DeepSearchQA` and `MathVision`. This suggests Kimi K2.6's competitive edge in both general and specialized AI tasks, indicating its potential as a robust alternative to more established models.** Commenters note the significance of Kimi K2.6's performance, especially in coding, and express surprise at an open-source model competing closely with proprietary models. There is anticipation for Kimi K2.6 to surpass Claude Opus, highlighting the competitive landscape of AI development.

    * MokoshHydro highlights the significance of Kimi K2.6's new feature, the 'vendor verifier', which provides a standardized method for evaluating third-party services. This is crucial for ensuring consistency and reliability when integrating external services into the Kimi ecosystem, as detailed in their [blog post](https://www.kimi.com/blog/kimi-vendor-verifier).
    * Ok_Knowledge_8259 notes the impressive progress of Kimi K2.6, especially considering its open-source nature, which is closing the gap with proprietary models. This suggests a significant advancement in the capabilities of open-source AI models, particularly in coding tasks where Kimi has historically excelled.
    * pmttyji expresses a desire for the inclusion of GLM-5.1 in the comparison, noting that Kimi-K2.6 has set a high benchmark for models like DeepseekV4. This indicates that Kimi-K2.6 is being used as a new standard for evaluating the performance of other AI models.



### 2\. Qwen Model Discussions and Experiences

  * **[Qwen 3.6 Max Preview just went live on the Qwen Chat website. It currently has the highest AA-Intelligence Index score among Chinese models (52) (Will it be open source?)](https://www.reddit.com/r/LocalLLaMA/comments/1sqlcan/qwen_36_max_preview_just_went_live_on_the_qwen/)** (Activity: 402): ****Qwen 3.6 Max** has been released on the [Qwen Chat website](https://chat.qwen.ai/) and currently holds the highest AA-Intelligence Index score of `52` among Chinese models, as reported by [AiBattle](https://x.com/AiBattle_/status/2046132538960158901). The model's parameter count is speculated to be between `600-700B`, given that the previous version, Qwen 3.6, had `397B` parameters. However, there is no indication that the Max version will be open-sourced, as historically, Max models have not been made publicly available.** Commenters express skepticism about the open-sourcing of Max models, noting that these models are typically not released to the public. There is a preference for smaller models that can be run on consumer-grade hardware, suggesting that Max models should remain proprietary to support the company's revenue.

    * There is speculation about the parameter size of the Qwen 3.6 Max model, with one user suggesting it could be between `600-700B` parameters, given that the Qwen Plus model is `397B`. This indicates a significant increase in complexity and potential capability, aligning with its high AA-Intelligence Index score of `52`.
    * A user highlights the business strategy behind not open-sourcing the Max models, suggesting that these models serve as a revenue engine for the company. This implies that the company prioritizes monetization of their most advanced models while potentially offering smaller models for broader accessibility.
    * Discussion around open-sourcing reveals that the largest model likely to be open-weighted is the `122B` model, as the company has stopped open-weighting the `397B` Plus models. This suggests a strategic decision to limit access to their most advanced models, possibly to maintain competitive advantage.
  * **[Switching from Opus 4.7 to Qwen-35B-A3B](https://www.reddit.com/r/LocalLLaMA/comments/1spz0ck/switching_from_opus_47_to_qwen35ba3b/)** (Activity: 772): **The user is considering switching from**Opus 4.7** to **Qwen-35B-A3B** for a coding agent driver, specifically running on an `M5 Max 128GB` setup. The user acknowledges that Opus might have an advantage in complex reasoning tasks but is questioning whether Qwen-35B-A3B would be adequate for most tasks. The post suggests that Qwen-35B-A3B has replaced about `95%` of the user's calls, indicating a high level of functionality, though it may not fully match Opus's capabilities in complex scenarios.** One commenter suggests that Qwen-35B-A3B might not meet expectations if the user is accustomed to Opus's capabilities, while another implies that the user's tasks may not require Opus's advanced features. A third comment indicates that Qwen-35B-A3B can handle most tasks but may fall short compared to Opus in certain areas.

    * **Flinchie76** discusses the trade-offs between using Opus 4.7 and Qwen-35B-A3B, highlighting that while Opus can generate large amounts of code quickly, it often results in complex, hard-to-understand architectures. In contrast, using a less capable model like Qwen-35B-A3B allows for more control and understanding of the code, as it requires the user to think through the process and inspect changes closely, leading to better ownership of the final product.
    * **Borkato** notes that Qwen-35B-A3B has replaced about 95% of their calls, suggesting that while it may not match Opus in capability, it is still highly functional for many tasks. This implies that Qwen-35B-A3B can handle a significant portion of tasks that users might typically rely on Opus for, albeit with some limitations.
    * **Thump604** mentions the possibility of running a 122B model, but clarifies that it does not reach the level of Opus 4.7. This suggests that while there are larger models available, they may not fully replicate the performance or capabilities of Opus, indicating a potential gap in functionality for users transitioning from Opus to other models.
  * **[I'm running qwen3.6-35b-a3b with 8 bit quant and 64k context thru OpenCode on my mbp m5 max 128gb and it's as good as claude](https://www.reddit.com/r/LocalLLaMA/comments/1spdvpo/im_running_qwen3635ba3b_with_8_bit_quant_and_64k/)** (Activity: 1239): **The user reports running the`qwen3.6-35b-a3b` model with `8-bit quantization` and a `64k context` on a MacBook Pro M5 Max with `128GB RAM` using **OpenCode**. They claim it performs comparably to **Claude** in terms of speed and handling complex tasks, such as debugging serialization issues in an Android app. The model is noted for its fast response times and effective handling of long research tasks, making it a viable alternative to cloud-based models.** Commenters highlight the model's speed, especially on high-performance hardware like a `5090`, and its efficient handling of large contexts, suggesting it can handle up to `256k context` effectively. However, there is some skepticism about its equivalence to Claude, though it is acknowledged as a strong local model.

    * **cosmicnag** highlights the performance of the Qwen 3.6-35b-a3b model, noting that on a `5090` GPU, the speed is unmatched compared to cloud models. They mention not having tried `NVFP4` yet, suggesting potential for even greater performance improvements.
    * **H_DANILO** points out that the Qwen model can handle up to `256k` context efficiently, emphasizing that context handling is _very cheap_ with this model. This suggests significant advantages for tasks requiring extensive context management.
    * **Krillian58** shares a contrasting experience, stating that after switching from Opus to Qwen 3.6, they found it substantially worse for their tasks. They speculate that it might be due to the model picking up _Opus loose ends_ , indicating potential issues with model transition or adaptation.



### 3\. Local LLMs and Offline AI Applications

  * **[So... what am I supposed to learn with local LLMs?](https://www.reddit.com/r/LocalLLM/comments/1spujo7/so_what_am_i_supposed_to_learn_with_local_llms/)** (Activity: 112): **The post discusses the challenges and potential of using local LLMs, particularly on limited hardware like a 16GB M4 Mac Mini. The user experimented with OpenClaw and local models like`gemma e4b q4` distilled by Opus, integrating it with Apple's OCR and vision capabilities. Despite initial success in setting up cron jobs and basic tasks, the user questions the practical utility of local LLMs compared to cloud-based solutions like Claude Code. The post highlights the potential for local LLMs to improve with better hardware and the importance of understanding model context windows and privacy benefits. The user is advised to explore smaller models and consider future-proofing their setup for more advanced applications.** Commenters emphasize the benefits of local LLMs in terms of privacy, cost-effectiveness, and the ability to run unrestricted models. They suggest using local LLMs for tasks like email summarization, document analysis, and personal knowledge management. Some recommend switching from OpenClaw to Hermes Agent for a more streamlined experience, highlighting the importance of setting up remote interaction channels and automating routine tasks.

    * **Local LLMs** offer significant advantages in terms of privacy and control over data. Running models like Qwen 3.5 or 3.6 locally allows users to avoid sending sensitive information to large corporations, which is crucial for maintaining privacy. Additionally, as hardware becomes cheaper and models more efficient, local LLMs can become more cost-effective and faster than cloud-based solutions, providing a future-proofing benefit.
    * **Hermes Agent** is recommended over OpenClaw due to its lower token overhead and better design. Local LLMs can be integrated with communication platforms like Telegram or Slack to automate tasks such as summarizing emails, creating knowledge bases, and performing OCR on PDFs. This setup allows for seamless task management without the limitations of token usage imposed by cloud-based models.
    * Running **local LLMs** on limited hardware, such as 16GB RAM, can be challenging but offers unique benefits. It allows for secure processing of sensitive data without internet exposure, which is critical for tasks that require high privacy. While models like Qwen 3.5 9b can run on such setups, the real advantage lies in automating tasks that are too sensitive for cloud APIs, despite the hardware constraints.
  * **[llama.cpp speculative checkpointing was merged](https://www.reddit.com/r/LocalLLaMA/comments/1sprdm8/llamacpp_speculative_checkpointing_was_merged/)** (Activity: 417): **The`llama.cpp` project has merged a speculative checkpointing feature, which can lead to varying speedups depending on the task and repetition patterns. For coding tasks, users have reported speedups ranging from `0% to 50%` using parameters like `--spec-type ngram-mod`, `--spec-ngram-size-n 24`, `--draft-min 48`, and `--draft-max 64`. This feature is part of ongoing optimizations, including other enhancements like DFlash and SYCL support, which have shown speed improvements of `17% to 50%`. These updates suggest that performance will continue to improve as software and drivers are refined ([source](https://github.com/ggml-org/llama.cpp/pull/19493)).** Commenters are optimistic about the improvements, noting that while some users are disappointed with the initial performance of the B70, ongoing updates are expected to enhance performance significantly. The community is encouraged to be patient as further optimizations are implemented.

    * The speculative checkpointing feature in `llama.cpp` has been merged, which is expected to enhance performance significantly. Notably, there are several related pull requests that contribute to performance improvements: [PR #22066](https://github.com/ggml-org/llama.cpp/pull/22066) reports a `17 to 50%` speed increase on SYCL, [PR #21845](https://github.com/ggml-org/llama.cpp/pull/21845) claims up to `50%` speed up, and [PR #21527](https://github.com/ggml-org/llama.cpp/pull/21527) also mentions a `50%` speed up. These improvements suggest that initial performance concerns with the B70 may be premature as software and drivers continue to evolve.
    * The implementation of self-speculative decoding in `llama.cpp` allows for its use with models like Qwen3.5 and 3.6. This feature can be activated by adjusting parameters, potentially leading to more efficient token generation. However, the actual performance gain may vary, as indicated by the humorous note that it might not be as fast as expected ('not BRRRRRR'), but still offers some 'free tokens'.
    * The variance in acceptance rates for speculative decoding is influenced by the `ngram-mod` matching mechanism. Codebases with repetitive patterns, such as those in TypeScript or Java, may experience higher acceptance rates (up to `50%`), while unique logic sequences may see lower rates. The parameter `--spec-ngram-size-n 24` is considered aggressive, as it requires `24 tokens` of context for pattern matching. Experimenting with smaller values (e.g., `8-12`) could improve performance in mixed code/prose tasks by increasing the likelihood of pattern matches, albeit with shorter draft runs.



## Less Technical AI Subreddit Recap

> /r/Singularity, /r/Oobabooga, /r/MachineLearning, /r/OpenAI, /r/ClaudeAI, /r/StableDiffusion, /r/ChatGPT, /r/ChatGPTCoding, /r/aivideo, /r/aivideo

### 1\. Claude Design and Usage Innovations

  * **[This cannot be real. I cannot believe my eyes](https://www.reddit.com/r/ClaudeAI/comments/1sqpb2f/this_cannot_be_real_i_cannot_believe_my_eyes/)** (Activity: 1527): **The image in the Reddit post is a feature launch carousel for an app called "Air Roster," showcasing various functionalities such as a month mapping feature, a month picker interface, a geodesic map visualization, and pay-related statistics. The design employs a dark theme with blue and white text, aiming for a modern aesthetic. The post discusses the democratization of design tools, comparing the impact of Canva on design accessibility to the potential of new AI tools in reducing the need for specialized design skills, allowing users to focus on content rather than tool proficiency.** Comments reflect skepticism about the design quality, with some users criticizing the user interface (UI) and user experience (UX), and others questioning the seriousness of the praise, suggesting it might be sarcastic.

    * Capable_Ad1259 highlights the disparity in perception of the UI/UX design based on professional background. Backend/API/AI/ML developers might find the design impressive due to its technical complexity, whereas UI developers and designers might critique it for being 'sloppy'. This underscores the challenge of transitioning from backend engineering to design, emphasizing the need for time and effort to master design skills.
  * **[Claude Design is Amazing! We're cooked!](https://www.reddit.com/r/ClaudeAI/comments/1squwsy/claude_design_is_amazing_were_cooked/)** (Activity: 576): **The post discusses a request made to**Claude Design** , an AI model, to create an operating system that avoids typical AI-generated content, referred to as "AI-slop." The user claims that Claude Design successfully generated a unique OS design in a single attempt, highlighting its capabilities. However, the post lacks specific technical details about the OS design, such as architecture, features, or benchmarks, which would be crucial for a technical evaluation.** One commenter questions the feasibility of the AI creating a complete operating system, suggesting skepticism about the claim's validity. Another comment nostalgically references the design's similarity to **Windows 98** , indicating a retro aesthetic rather than a modern technical innovation.

  * **[Claude Design is Incredible...](https://www.reddit.com/r/ClaudeAI/comments/1spxi2f/claude_design_is_incredible/)** (Activity: 1689): **The post discusses a rapid UI redesign using**Claude Design** , highlighting its ability to quickly transform applications with minimal effort. The author notes that while the redesign may resemble other apps made with Claude, it was effective for personal use. The project is now open source and available on [GitHub](https://github.com/AmmarSaleh50/study-dashboard). The author suggests that with a specific design prompt, Claude can produce unique results, but a generic prompt leads to default designs.** Commenters generally agree that apps designed with Claude tend to look similar, with one noting that the redesign resulted in a less appealing font choice. Another commenter suggests that the uniformity might lead to many apps having the same design in the near future.

    * Chupa-Skrull highlights that Claude Design's main advantage is its ability to expose 'knobs' on various properties, which allows users to optimize their workflow by adjusting parameters that they might not have known to prompt for. This feature significantly speeds up the design process, although the underlying capabilities are similar to what other models have offered for months.
    * One-Cheesecake-9353 points out that while Claude Design might be suitable for personal projects, it introduces too much cognitive load for projects intended for mass consumption. This suggests that the design complexity or the user interface might not be intuitive enough for broader audiences, potentially impacting user experience negatively.
    * Toxic-slop and disky_wude both note that apps generated by Claude tend to look similar, indicating a lack of diversity in design outputs. This could be a limitation in Claude's design algorithm, leading to repetitive styles and potentially reducing the uniqueness of applications developed using this tool.
  * **[I didn't realise Claude could build actual Word docs and Excel files. Cancelled three subscriptions in the same week.](https://www.reddit.com/r/PromptEngineering/comments/1spmwkg/i_didnt_realise_claude_could_build_actual_word/)** (Activity: 422): **The post highlights**Claude's ability to generate fully formatted Word (.docx), Excel (.xlsx), and PowerPoint (.pptx) files** directly from prompts, eliminating the need for separate document creation software. Users can request specific formatting, such as headings, bullet points, and professional fonts, and Claude can handle complex Excel functionalities like formulas and conditional formatting. The tool also supports editing existing documents while maintaining their format. This capability allows users to bypass traditional document creation tools, focusing instead on content creation rather than formatting and infrastructure.** Commenters noted the importance of changing document metadata to reflect the correct author, and shared experiences of using Claude to fix complex formatting issues in documents converted from PDF to Word. They also praised Claude's iterative editing capabilities, allowing for seamless content updates and modifications.

    * Rencauchao highlights a critical step when using Claude to generate Word documents: users should modify the 'author' and 'comments' metadata to reflect their own information before sharing, as these fields can reveal the document's origin as being generated by Claude. This is important for maintaining authorship integrity and privacy.
    * sceez shares a practical use case where Claude was employed to resolve formatting issues in a Word document that had been converted to PDF and back. The process involved iterative interactions with Claude, which successfully restored the document's formatting, demonstrating Claude's capability in handling complex document editing tasks.
    * 5aur1an suggests a method for personalizing outputs from Claude by training it to mimic a user's writing style. This involves analyzing a sample document for stylistic elements, then iteratively refining the generated content by providing feedback on specific words or phrases that don't match the user's style. This approach can enhance the relevance and personalization of the generated content over time.



### 2\. DeepSeek and V4 Developments

  * **[They said it's next week 🤞](https://www.reddit.com/r/DeepSeek/comments/1sppz7q/they_said_its_next_week/)** (Activity: 328): **The image is a screenshot of a social media post by**Yifan Zhang** , discussing upcoming technological updates related to AI models, specifically mentioning terms like "Sparse MQA," "Fused MoE Mega Kernel," and "Hyper-connections." These terms suggest advancements in AI model architecture, potentially improving efficiency and performance. The mention of "V4, next week" implies an anticipated release or update, possibly related to a new version of an AI model or framework. The post has been edited and shows significant engagement, indicating community interest.** Commenters express skepticism about the release timeline, noting that similar promises have been made since January. However, there is a sense of renewed optimism and excitement, with some users more interested in this update than other recent AI developments.

  * **[To those waiting for V4](https://www.reddit.com/r/DeepSeek/comments/1sq0jcz/to_those_waiting_for_v4/)** (Activity: 221): ****High-Flyer** is a unique entity in the tech landscape, operating as a massive quant hedge fund rather than a traditional tech company. This structure allows them to develop AI models like V4 without the typical pressures of generating direct revenue or appeasing venture capitalists. Their approach is driven by internal metrics rather than external market cycles, which explains the lack of marketing hype and the low-cost API offerings. The company is rumored to fund its AI division through strategic financial maneuvers, such as shorting Nvidia, highlighting their financial independence and strategic focus.** Commenters debate the rationale behind High-Flyer's AI development, suggesting that despite their financial independence, they must innovate to remain competitive and relevant. Concerns are also raised about talent retention and the potential need to go public to ensure long-term success.

    * WHY_DO_I_SHOUT highlights that the hedge fund's lack of marketing hype and low-cost API access is due to their financial independence, as they don't rely on direct revenue from the model. This suggests their primary goal isn't monetization through the model itself, but possibly leveraging it for internal advantages or strategic positioning.
    * Weird-Pollution-6251 points out that the model's user interface and lack of integration with other tools indicate it's more of a demonstration than a fully-fledged product. This implies that the hedge fund's focus might be on showcasing capabilities rather than creating a market-ready product, which aligns with their financial strategy of not needing direct revenue from the model.
    * Puzzleheaded-Drama-8 speculates that the hedge fund might benefit from market fluctuations caused by the hype around model releases. This suggests a strategic use of the model to influence market conditions, potentially creating opportunities for profit through trading on these fluctuations.



### 3\. Kimi 2.6 and AI Model Benchmarks

  * **[Kimi 2.6 has been released](https://www.reddit.com/r/singularity/comments/1sqsvrt/kimi_26_has_been_released/)** (Activity: 605): **The image is a performance comparison chart that highlights the competitive performance of**Kimi K2.6** against other AI models like **GPT-5.4** , **Claude Opus 4.6** , and **Gemini 3.1 Pro** across various tasks such as general agents, coding, and visual agents. **Kimi K2.6** is particularly noted for its autonomous overhaul of an open-source financial matching engine, achieving significant performance improvements by iterating through optimization strategies and modifying code autonomously. This showcases the model's advanced capabilities in system architecture and optimization, achieving a `185%` medium throughput increase and a `133%` performance throughput gain.** Commenters are impressed by the open-source nature of **Kimi K2.6** and its ability to autonomously optimize complex systems, highlighting its potential in real-world applications.

    * Kimi K2.6 autonomously optimized the exchange-core, an open-source financial matching engine, by iterating through 12 optimization strategies and making over 1,000 tool calls to modify more than 4,000 lines of code. The model analyzed CPU and allocation flame graphs to identify bottlenecks and reconfigured the core thread topology, achieving a 185% increase in medium throughput and a 133% gain in performance throughput, demonstrating significant advancements in open-source AI capabilities.
    * A user expressed skepticism about Kimi 2.5 being 'benchmaxed,' noting that it excelled in design and web development tasks compared to other models like Claude, GLM 5.1, GPT, Gemini 3.1, and Qwen. They highlighted Kimi's unmatched performance in creating PowerPoint presentations, PDFs, and websites, suggesting that its design capabilities were far superior to its competitors, which is particularly impressive if Kimi 2.6 is indeed open-source.
    * The discussion includes a query about whether Kimi 2.6 is truly open-source, reflecting the community's interest in the accessibility and transparency of advanced AI models. The user compares Kimi's performance favorably against other models, emphasizing its exceptional design task capabilities, which could be a significant advantage if the model remains open-source.
  * **[Opus 4.7 vs 4.6 after 3 days of real coding - side by side from my actual sessions](https://www.reddit.com/r/ClaudeCode/comments/1spxtut/opus_47_vs_46_after_3_days_of_real_coding_side_by/)** (Activity: 696): **The image provides a detailed side-by-side comparison of Opus 4.6 and Opus 4.7 based on three days of real coding sessions. Key metrics such as one-shot rate, retry rate, and cost per call are highlighted, showing that Opus 4.6 generally performs better in terms of one-shot success rate (`83.8%` vs `74.5%`) and cost efficiency (`$0.112` vs `$0.185` per call). Opus 4.7, however, generates more output per call (`800 tokens` vs `372 tokens`), making it more expensive. The analysis also notes that Opus 4.7 uses fewer tools per turn and delegates less to subagents, suggesting potential differences in operational style or sample size limitations. The post emphasizes that these findings are preliminary and based on limited data, with the potential for shifts as more data is collected.** Commenters appreciate the detailed analysis and suggest that prompt adjustments might be needed for Opus 4.7. There is also a discussion about the potential motivations behind the aggressive promotion of Opus 4.7, hinting at cost considerations.

    * phil_thrasher raises a critical point about the need for prompt adjustments when transitioning from Opus 4.6 to 4.7, suggesting that the harness might require changes to optimize performance for the newer version. This highlights the importance of adapting testing frameworks to accommodate updates in AI models, which may not have been fully addressed by the development team.
    * SovietRabotyaga points out the significance of the 'total cost field' in understanding Anthropic's strategy for aggressively promoting Opus 4.7. This suggests that economic factors might be influencing the push for newer versions, potentially impacting the decision-making process behind model updates and deployments.
    * thewormbird reflects on historical model updates, noting that intermediate versions like 3.7 were less effective in their workflows compared to major releases like 4.0. This raises questions about the versioning strategy and whether incremental updates provide substantial improvements, suggesting that users might benefit more from waiting for major releases like Opus/Sonnet 5.



# AI Discords

Unfortunately, Discord shut down our access today. We will not bring it back in this form but we will be shipping the new AINews soon. Thanks for reading to here, it was a good run.

---

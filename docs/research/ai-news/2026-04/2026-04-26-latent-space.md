---
title: "Latent Space — 2026-04-26"
date: 2026-04-26
source: Latent Space
type: ai-news
---

# 🔬 Latent Space — 2026-04-26

> swyx 開發者簡報，未公開專案 + 工程視角
> 來源：[Latent Space](https://www.latent.space/feed)

---

## [[AINews] DeepSeek V4 Pro (1.6T-A49B) and Flash (284B-A13B), Base and Instruct — runnable on Huawei Ascend chips](https://www.latent.space/p/ainews-deepseek-v4-pro-16t-a49b-and)
*🔬 Latent Space | 2026-04-25*

After a couple months' delay and lots of speculation, [DeepSeek finally released the heavily anticipated DSV4](https://x.com/deepseek_ai/status/2047516922263285776?s=20), the first major version model since DSV3 (Dec 2024) and DSR1 (Jan 2025). It brings the DeepSeek family up in line with [Kimi K2.6](https://www.latent.space/p/ainews-moonshot-kimi-k26-the-worlds?utm_source=publication-search), the current open model leader, and [Xiaomi Mimo 2.5](https://x.com/ArtificialAnlys/status/2047799218828665093?s=20), a lesser known family [released 2 days ago](https://x.com/XiaomiMiMo/status/2046988157888209365?s=20).

[](https://substackcdn.com/image/fetch/$s_!2kgW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa10f0270-c9c4-481b-962a-fcba50a2418b_1022x1104.png)

The DSV4 family is roughly a Gemini 3.1, GPT 5.4, Opus 4.6 level model, up to 1.6T MOE withtrained on 32T tokens with [FP4](https://x.com/iscienceluvr/status/2047514399393579235?s=46), with 1M token context (supported by their new Compressed Sparse Attention (CSA) and Heavily Compressed Attention (HCA) techniques), and incredibly rarely, they released both the Base and Instruct versions - surely setting the stage for a possible "DeepSeek R2" in future, though this one already has reasoning effort.

[](https://substackcdn.com/image/fetch/$s_!IADX!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff028c03e-53a7-4615-af85-fc5e6e11dab0_1226x940.png)

The [technical report](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/blob/main/DeepSeek_V4.pdf) is a typically dense 58 pages, demonstrating training and inference insights and improvements from [the Manifold Constrained Hyper-Connections (mHC) paper](https://arxiv.org/pdf/2512.24880) they released in January, continued usage of [Moonshot's Muon](https://news.smol.ai/frozen-issues/25-07-11-kimi-k2.html), and CSA/HCA's overall INCREDIBLE efficiency improvements on [DeepSeek 3.2-Exp's already impressive Sparse Attention](https://news.smol.ai/frozen-issues/25-12-01-deepseek-32.html) \- at 1M tokens, requiring only 27% of FLOPs and 10% of KV cache memory compared with DeepSeek-V3.2:

[](https://substackcdn.com/image/fetch/$s_!ICSA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff73baf75-34a0-46e8-8452-7cccd7481ba9_1156x730.png)

The geopolitical backdrop behind the [Huawei CANN compatibility](https://x.com/jukan05/status/2047823601462812932) is DeepSeek weaning dependence off export-controlled NVIDIA/CUDA chips -- Ascends are still [a quarter the supply](https://x.com/PalwinderCFA/status/2047614823102619974) of H100s, but this is an important milestone for Chinese total independence.

> AI News for 4/23/2026-4/24/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

# **AI Twitter Recap**

**Top Story: DeepSeek V4**

DeepSeek released **DeepSeek-V4 Pro** and **DeepSeek-V4 Flash** , its first major architecture refresh since V3 and first clear two-tier lineup, with **1M-token context** , hybrid reasoning/non-reasoning modes, an **MIT license** , and a technical report detailed enough that multiple researchers called it one of the most important or best-written model papers of the year. Across the reactions, the factual consensus is that V4 materially advances open-weight long-context and agentic coding performance while remaining somewhat behind the top closed frontier models overall. Independent benchmarkers place **V4 Pro around the #2 open-weights tier** , roughly near **Kimi K2.6 / GLM-5.1 / strong Claude Sonnet-class to Opus-ish** depending on benchmark and mode, with especially strong long-context and agentic performance; opinions diverge on how close it is to GPT-5.x / Opus 4.7 and on whether this is "democratizing" progress or an architecture so complex that few open labs can realistically reproduce it. Key sources include deep-dive commentary from [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2047735160544841953), [@scaling01](https://x.com/scaling01/status/2047618271310926151), [@nrehiew_](https://x.com/nrehiew_/status/2047665987730993363), [@ben_burtenshaw](https://x.com/ben_burtenshaw/status/2047646980139016560), [@TheZachMueller](https://x.com/TheZachMueller/status/2047702488418030066), [@ZhihuFrontier](https://x.com/ZhihuFrontier/status/2047664976215839021), and infra/vendor posts from [@vllm_project](https://x.com/vllm_project/status/2047843293447500069), [@NVIDIAAI](https://x.com/NVIDIAAI/status/2047765637808664759), and [@Togethercompute](https://x.com/togethercompute/status/2047743446522224987).

## **Core facts and technical details**

The most concrete technical claims repeated across the discussion:

  * **Two models**

    * **V4 Pro:** **1.6T total parameters / 49B active**

    * **V4 Flash:** **284B total / 13B active**

    * Reported by [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2047735160544841953), [@teortaxesTex](https://x.com/teortaxesTex/status/2047630981364883816), [@baseten](https://x.com/baseten/status/2047779549644243146), [@NVIDIAAI](https://x.com/NVIDIAAI/status/2047765637808664759)

  * **Context**

    * **1M tokens** , up from **128K in V3.2** per [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2047735160544841953)

    * Multiple posters frame this as the headline achievement: "solid ultra-long context" [@teortaxesTex](https://x.com/teortaxesTex/status/2047623905754448043)

  * **Training scale**

    * **32T -33T tokens** cited repeatedly

    * [@nrehiew_](https://x.com/nrehiew_/status/2047666048334450754) notes **32T tokens** over **1.6T parameters** , i.e. roughly **20 tokens/parameter**

    * [@teortaxesTex](https://x.com/teortaxesTex/status/2047630981364883816) cites **33T**

    * [@nrehiew_](https://x.com/nrehiew_/status/2047840706874749076) estimates pretraining compute at **~1e25 FLOPs**

  * **Reasoning / modes**

    * DeepSeek exposes **three reasoning modes** per [@Togethercompute](https://x.com/togethercompute/status/2047743446522224987)

    * Hybrid "thinking/non-thinking" positioning noted by [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2047735160544841953)

  * **Long-context architecture**

    * Several threads summarize a new hybrid attention system:

      * shared KV vectors

      * compressed KV streams

      * sparse attention over compressed tokens

      * local/sliding-window attention for nearby context

    * [@ZhihuFrontier](https://x.com/ZhihuFrontier/status/2047664976215839021) gives the most compact public summary:

      * **2 × KV reduction** via shared key-value vectors

      * **c4a ≈ 4× compression**

      * **c128a ≈ 128× compression**

      * **top-k sparse attention** on compressed tokens

      * **128-token sliding window**

      * **1M context KV cache = 9.62 GiB/sequence (bf16)**

      * **8.7 × smaller** than DeepSeek V3.2's **83.9 GiB**

      * FP4 index cache + FP8 attention cache gives another ~**2 ×** reduction

    * [@ben_burtenshaw](https://x.com/ben_burtenshaw/status/2047646980139016560) condenses this to "**10 × smaller KV cache**"

    * [@TheZachMueller](https://x.com/TheZachMueller/status/2047702488418030066) and [@TheZachMueller](https://x.com/TheZachMueller/status/2047702996524405175) describe **CSA + HCA** layer patterns, with alternating layers and V4 Flash using sliding-window layers instead of HCA in some places

  * **Quantization / checkpoint format**

    * [@LambdaAPI](https://x.com/LambdaAPI/status/2047654086263320965): checkpoint is **mixed FP4 + FP8**

      * **MoE expert weights in FP4**

      * attention / norm / router in **FP8**

      * claim: the full model fits on a single **8 ×B200** node

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

    * [@scaling01](https://x.com/scaling01/status/2047707820552831028) views the pricing as a glimpse of future "Mythos-level" cheap coding models

    * Reuters-via-posted quote from [@scaling01](https://x.com/scaling01/status/2047760776769720360): DeepSeek said **Pro pricing could fall sharply once Huawei Ascend 950 supernodes are deployed at scale in H2**




## **Independent evaluations and where V4 lands**

The most useful independent benchmark synthesis came from [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2047735160544841953):

  * **V4 Pro Max** : **52** on Artificial Analysis Intelligence Index

    * up **10 points** from **V3.2 at 42**

    * becomes **#2 open weights reasoning model** , behind **Kimi K2.6 (54)**

  * **V4 Flash Max** : **47**

    * positioned around strong mid/high open models, "Claude Sonnet 4.6 max level intelligence"

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

    * costs **12 × more**

    * Flash is still competitive in Chinese, medicine, math

  * [@scaling01](https://x.com/scaling01/status/2047682465624445015):

    * "~**Opus 4.5 estimate** holds for now, at least on SimpleBench"

  * [@scaling01](https://x.com/scaling01/status/2047733998714052819):

    * V4 is "definitely better than GLM-5.1 but not quite Opus 4.7, GPT-5.4 or Gemini 3.1 Pro"

  * [@scaling01](https://x.com/scaling01/status/2047686712051048598) lists what scores would confirm <6 month gap:

    * ARC-AGI-1 ~**75%**

    * ARC-AGI-2 ~**35%**

    * GSO ~**26%**

    * METR **4.5 -5 hours**

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




## **Facts vs opinions**

### **Facts / relatively well-supported claims**

  * V4 Pro / Flash were released with the specs above, **MIT-licensed** , **1M context** , and open technical documentation: [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2047735160544841953), [@TheZachMueller](https://x.com/TheZachMueller/status/2047626252425515240)

  * The architecture introduces a new long-context attention system with dramatic KV-cache reduction: [@ZhihuFrontier](https://x.com/ZhihuFrontier/status/2047664976215839021), [@ben_burtenshaw](https://x.com/ben_burtenshaw/status/2047646980139016560)

  * Independent benchmarkers broadly place V4 Pro near the very top of open weights but below the best proprietary models overall: [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2047735160544841953), [@arena](https://x.com/arena/status/2047714237502677405), [@scaling01](https://x.com/scaling01/status/2047733998714052819)

  * DeepSeek V4 is heavily token-intensive in some evaluations: [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2047735160544841953)

  * The checkpoint uses FP4/FP8 mixed precision and can fit on an 8×B200 node: [@LambdaAPI](https://x.com/LambdaAPI/status/2047654086263320965)

  * Rapid ecosystem support arrived via vLLM and other providers day 0: [@vllm_project](https://x.com/vllm_project/status/2047843293447500069), [@SemiAnalysis_](https://x.com/SemiAnalysis_/status/2047726025748930687)




### **Opinions / interpretation**

  * "V4 is ~4-5 months behind the frontier" from [@scaling01](https://x.com/scaling01/status/2047618271310926151), [@scaling01](https://x.com/scaling01/status/2047622501241434581), [@scaling01](https://x.com/scaling01/status/2047626000091971811) is an informed estimate, not a measured fact

  * "Top three open" vs "only open model close to frontier" debate from [@teortaxesTex](https://x.com/teortaxesTex/status/2047616662879248828) is partly about benchmark trust and framing

  * "Strongest pretrained model we have" from [@teortaxesTex](https://x.com/teortaxesTex/status/2047630981364883816) is an opinion hinging on scale + architecture, not direct benchmark supremacy

  * "Most significant AI paper of the year" from [@Dorialexander](https://x.com/Dorialexander/status/2047632551326413109) is enthusiasm, not consensus

  * "This is what research should look like" from [@scaling01](https://x.com/scaling01/status/2047643722108579936) speaks to transparency/style rather than only capability

  * "Not exactly a democratizing technology" from [@teortaxesTex](https://x.com/teortaxesTex/status/2047840426371977467) is a strong architectural/political interpretation




## **Different opinions and fault lines**

### **1) Is V4 near frontier, or clearly behind?**

**More favorable**

  * [@scaling01](https://x.com/scaling01/status/2047618271310926151): puts it at roughly **GPT-5.2 / Opus 4.5+ tier**

  * [@scaling01](https://x.com/scaling01/status/2047682465624445015): SimpleBench supports **~Opus 4.5**

  * [@teortaxesTex](https://x.com/teortaxesTex/status/2047630981364883816): argues it is the strongest pretraining base among opens and implies people are underestimating what post-training can do




**More skeptical**

  * [@scaling01](https://x.com/scaling01/status/2047733998714052819): below **Opus 4.7 / GPT-5.4 / Gemini 3.1 Pro**

  * [@scaling01](https://x.com/scaling01/status/2047622501241434581): the gap may widen again because closed labs have bigger models, better science/law/medicine coverage, faster inference with GB200s

  * [@mbusigin](https://x.com/mbusigin/status/2047707082007220393): early impressions "not great"

  * [@teortaxesTex](https://x.com/teortaxesTex/status/2047616897256947967): says polished models like **K2.6 and GLM 5.1** may still feel better in coding despite lower intrinsic capacity




### **2) Is V4 's real contribution model quality, or long-context systems design?**

A big split in reactions is that many technical readers think **the long-context architecture matters more than the raw benchmark position**.

  * [@teortaxesTex](https://x.com/teortaxesTex/status/2047623905754448043): "They've completed their quest: Solid Ultra-Long Context"

  * [@ben_burtenshaw](https://x.com/ben_burtenshaw/status/2047646980139016560): first open model where long context and agentic post-training "meet"

  * [@scaling01](https://x.com/scaling01/status/2047618271310926151): expects other open labs to adopt pieces of the architecture

  * [@Dorialexander](https://x.com/Dorialexander/status/2047632551326413109): frames Huawei/sovereignty constraints as an opportunity to reshape hardware and memory/interconnect design

  * [@jukan05](https://x.com/jukan05/status/2047861732702662741): reads the paper as evidence that NVIDIA's hardware roadmap is unusually well aligned to where MoE/long-context models are going




### **3) Is V4 "open democratization," or too hard to copy?**

This was one of the sharpest strategic disagreements.

  * [@teortaxesTex](https://x.com/teortaxesTex/status/2047840426371977467): says V4 is "not exactly a democratizing technology" because the architecture is too difficult for most labs to replicate

  * [@teortaxesTex](https://x.com/teortaxesTex/status/2047648219081974034): suggests even DeepSeek may not want to do this exact architecture again without refactoring

  * [@stochasticchasm](https://x.com/stochasticchasm/status/2047697372831183245): notes the sheer hyperparameter complexity is daunting

  * Against that, [@Prince_Canuma](https://x.com/Prince_Canuma/status/2047685898163147125) and [@Prince_Canuma](https://x.com/Prince_Canuma/status/2047847095466385899) show that the ecosystem is already compressing and adapting Flash for localish Apple Silicon use, softening the "not democratizing" claim on the inference side if not the training side




### **4) Are people underrating Flash?**

Several reactions suggest **Flash may be more important than Pro** for practical adoption.

  * [@arena](https://x.com/arena/status/2047774037204742255): Flash shifts the price/performance frontier

  * [@TheZachMueller](https://x.com/TheZachMueller/status/2047719857869791352): Flash@max ≈ Pro@high on reasoning tasks

  * [@teortaxesTex](https://x.com/teortaxesTex/status/2047864952862458009): benchmarks may underweight "legit 1M context for pennies"

  * [@Prince_Canuma](https://x.com/Prince_Canuma/status/2047685898163147125): Flash runs on **256GB Mac**

  * [@baseten](https://x.com/baseten/status/2047779549644243146) and [@Togethercompute](https://x.com/togethercompute/status/2047743446522224987) emphasize long-document analysis and agentic use cases where Flash's economics matter




## **China, chips, Huawei, and sovereignty context**

DeepSeek V4 was not discussed as a pure model release; it was treated as evidence in the larger US-China compute and sovereignty debate.

  * [@scaling01](https://x.com/scaling01/status/2047625331339661685): Chinese labs are already in or near "takeoff" in the sense that their models help build better models, though still shifted **5+ months** behind

  * [@scaling01](https://x.com/scaling01/status/2047622501241434581): thinks chip bans are likely to widen the gap in broad domains over time

  * [@teortaxesTex](https://x.com/teortaxesTex/status/2047608887616962992), [@teortaxesTex](https://x.com/teortaxesTex/status/2047631470664020211): disputes simplistic Huawei-dismissal and notes mixed Chinese sentiment toward Huawei

  * [@ogawa_tter](https://x.com/ogawa_tter/status/2047631993702363509): points to analysis of **Ascend 950** / A3 clusters and V4 deployment plans

  * [@Dorialexander](https://x.com/Dorialexander/status/2047632551326413109): argues the sovereignty play around Huawei may reshape hardware architecture

  * [@scaling01](https://x.com/scaling01/status/2047760776769720360): cites DeepSeek saying prices could drop sharply once **Ascend 950 supernodes** scale in H2

  * [@jukan05](https://x.com/jukan05/status/2047861732702662741): interprets V4 as validating NVIDIA's Blackwell/Rubin/HBM/interconnect strategy

  * [@NVIDIAAI](https://x.com/NVIDIAAI/status/2047765637808664759), [@NVIDIAAI](https://x.com/NVIDIAAI/status/2047823093578518758): unsurprisingly highlight Blackwell day-0 performance, but this is vendor framing rather than independent proof of strategic superiority




There is also a more ideological thread:

  * [@teortaxesTex](https://x.com/teortaxesTex/status/2047645676234846459), [@teortaxesTex](https://x.com/teortaxesTex/status/2047638436295725080), [@teortaxesTex](https://x.com/teortaxesTex/status/2047835420755415472) argues that Western discourse often misreads Chinese labs as purely state proxies or distillation shops, and instead sees them as serious mission-driven actors. This is interpretive, but it helps explain why the release drew such emotionally charged geopolitical reactions.




## **Distillation, training data, and data quality**

A recurring undercurrent: does V4 mainly reflect architectural innovation, or can critics dismiss it as "distillation"?

  * [@yacineMTB](https://x.com/yacineMTB/status/2047628416514486661) speculates that some complaints about Chinese distillation may partly come from people discovering they're outperformed

  * [@cloneofsimo](https://x.com/cloneofsimo/status/2047628636933812301): "Very interesting... given they distilled claude 🤔🤔"

  * [@kalomaze](https://x.com/kalomaze/status/2047762970931827125): jokes about DeepSeek training on DeepSeek reasoning traces

  * On the more substantive side, [@teortaxesTex](https://x.com/teortaxesTex/status/2047614729145745623) says DeepSeek's writing quality, especially Chinese, reflects long-standing obsession with data cleanliness and cites job listings [@teortaxesTex](https://x.com/teortaxesTex/status/2047614852055683103), [@teortaxesTex](https://x.com/teortaxesTex/status/2047614975447855485)

  * [@nrehiew_](https://x.com/nrehiew_/status/2047666048334450754) notes the report still lacks much detail on pretraining data beyond standard categories

  * Overall, factual public evidence in this tweet set supports "DeepSeek trains at large scale with strong data work," but not any strong claim about the degree of external distillation beyond speculation




## **Architecture lineage and prior art**

Several researchers pointed out that V4 did not emerge from nowhere.

  * [@jaseweston](https://x.com/jaseweston/status/2047690308217926055): says DeepSeek uses **hash routing** from a 2021 ParlAI approach

  * [@suchenzang](https://x.com/suchenzang/status/2047772636881842629): criticizes routing-induced outliers, with a jab at hashing

  * [@teortaxesTex](https://x.com/teortaxesTex/status/2047844368883581404): notes Mixtral-style MoE was a reasonable earlier hack, but claims **DSMoE** changed things

  * [@art_zucker](https://x.com/art_zucker/status/2047619111082172548) broadly attacks MoEs as a dead end

  * [@gabriberton](https://x.com/gabriberton/status/2047835467551547587) counters that MoEs are provably effective despite inelegance

  * [@stochasticchasm](https://x.com/stochasticchasm/status/2047874903236645108) is even more positive: "MoEs are amazing"




This matters because V4 was read not just as a stronger checkpoint, but as a possible **new design point for open long-context MoEs**.

## **Why the technical report itself mattered**

A striking amount of praise was directed not just at the model but at the paper/report quality.

  * [@scaling01](https://x.com/scaling01/status/2047618271310926151): "the technical paper is a big deal"

  * [@Dorialexander](https://x.com/Dorialexander/status/2047632551326413109): "most significant AI paper of the year"

  * [@morqon](https://x.com/morqon/status/2047643246923325833): "one of the best I've ever read"

  * [@scaling01](https://x.com/scaling01/status/2047643722108579936): "this is what research should look like"

  * [@TheZachMueller](https://x.com/TheZachMueller/status/2047626249116303561), [@iamgrigorev](https://x.com/iamgrigorev/status/2047641600591794546), [@nrehiew_](https://x.com/nrehiew_/status/2047665987730993363): all signal unusually high effort to digest and test the report




For expert readers, this is important because many frontier releases now arrive with sparse technical disclosure. V4's report appears to have reset expectations for what a serious open release can look like.

## **Practical limitations and caveats**

Despite the enthusiasm, several caveats recur:

  * **Still behind closed frontier in aggregate capability**

    * especially sciences/law/medicine and broad "general domains" per [@scaling01](https://x.com/scaling01/status/2047622501241434581)

  * **Reasoning RL may be undercooked**

    * [@scaling01](https://x.com/scaling01/status/2047618271310926151): reasoning efficiency not much changed vs V3.2 Speciale

  * **Serving remains hard**

    * [@scaling01](https://x.com/scaling01/status/2047643015859118167): many labs serve at only **20 -30 tok/s** and limited concurrency; running evals can take a day

    * [@ClementDelangue](https://x.com/ClementDelangue/status/2047664153439989823): acknowledges concurrency bottlenecks on HF

  * **High token usage**

    * major practical caveat from [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2047735160544841953)

  * **API controls**

    * [@stochasticchasm](https://x.com/stochasticchasm/status/2047717161070989499): notes DeepSeek API appears not to allow sampler control

  * **Adoptability**

    * [@teortaxesTex](https://x.com/teortaxesTex/status/2047840426371977467): too complex for many labs to copy cleanly




## **Broader implications**

Three implications stand out.

  1. **Open-weight long-context is no longer just marketing.**  
V4's strongest contribution may be proving that **1M context can be made operationally credible** in an open-weight model, with concrete KV-cache engineering and open inference support. This is why multiple posters focused less on benchmark deltas and more on systems design: [@ben_burtenshaw](https://x.com/ben_burtenshaw/status/2047646980139016560), [@ZhihuFrontier](https://x.com/ZhihuFrontier/status/2047664976215839021), [@scaling01](https://x.com/scaling01/status/2047618271310926151).

  2. **China 's top labs remain competitive in open models, even if not fully closing the closed-model gap.**  
The benchmark picture across [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2047735160544841953), [@arena](https://x.com/arena/status/2047714237502677405), and [@scaling01](https://x.com/scaling01/status/2047733998714052819) suggests Chinese labs now dominate much of the open-weight top tier: **Kimi, GLM, DeepSeek, and soon MiMo**.

  3. **The bar for "open" is rising from checkpoint release to full-stack co-design.**  
V4 was instantly discussed alongside **vLLM** , **Blackwell** , **MLX quants** , **Mac viability** , **Ascend clusters** , and cache/memory architectures. In other words, "the model" is increasingly inseparable from the inference substrate.




* * *

**Infrastructure, inference, and local/open ecosystem**

  * Hugging Face launched **ML Intern** , an open-source CLI "AI intern" for ML work that can research papers, write code, run experiments, use HF datasets/jobs, search GitHub, and iterate up to **300 steps** , per [@MillieMarconnni](https://x.com/MillieMarconnni/status/2047639632859500691). Related sentiment: HF's **$9 Pro** tier is unusually strong value per [@getpy](https://x.com/getpy/status/2047602009998794820).

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

    * "reasoning can lead to honesty" demo via [@GoogleResearch](https://x.com/GoogleResearch/status/2047704802163892576)

  * MIT **Hyperloop Transformers** mix looped and normal transformer blocks, using ~**50% fewer parameters** while beating regular transformers at **240M / 1B / 2B** , per [@TheTuringPost](https://x.com/TheTuringPost/status/2047720038342476187).

  * "Learning mechanics" tries to synthesize a theory of deep learning dynamics, via [@learning_mech](https://x.com/learning_mech/status/2047723849874330047).

  * Tool/agent systems papers:

    * **Tool Attention Is All You Need** claims **95% tool-token reduction** (47.3k -> 2.4k/turn) with dynamic gating and lazy schema loading, per [@omarsar0](https://x.com/omarsar0/status/2047725276851994639)

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

    * [@almmaasoglu](https://x.com/almmaasoglu/status/2047745168141324559): best code they've read from an LLM; less verbose, less defensive

    * [@KentonVarda](https://x.com/KentonVarda/status/2047788670728495142): caught a deep Cap'n Proto RPC corner case from a 6-year-old comment

    * [@willdepue](https://x.com/willdepue/status/2047783399826292969): underwhelmed by evals, impressed in Codex on complex technical projects

    * [@omarsar0](https://x.com/omarsar0/status/2047768166126809512): smooth switch from Claude Code to Codex/GPT-5.5 thanks to better "effort calibration"

  * Cursor also shipped **/multitask** async subagents and multi-root workspaces, via [@cursor_ai](https://x.com/cursor_ai/status/2047764651363180839).

  * There is growing market emphasis on **limits and economics** rather than tiny quality gaps:

    * [@nrehiew_](https://x.com/nrehiew_/status/2047839351380537357) argues usage caps now matter more than small frontier deltas

    * [@HamelHusain](https://x.com/HamelHusain/status/2047763070022479882) says Codex's subscription structure makes it hard not to use




**Industry moves, funding, and policy**

  * Google reportedly plans to invest up to **$40B in Anthropic** , reported by [@FT](https://x.com/FT/status/2047715653553942997) and echoed by [@zerohedge](https://x.com/zerohedge/status/2047704883982180609). Reactions centered on how large Anthropic's compute commitment may now be.

  * Cohere and Aleph Alpha announced a **Canada/Germany sovereign AI partnership** , framed as enterprise-grade and privacy/security focused by [@cohere](https://x.com/cohere/status/2047631725426000268), [@aidangomez](https://x.com/aidangomez/status/2047651054381052086), [@nickfrosst](https://x.com/nickfrosst/status/2047704679878996253#m).

  * ComfyUI raised **$30M at a $500M valuation** , while keeping core/open-local positioning, via [@yoland_yan](https://x.com/yoland_yan/status/2047731043000627263).

  * Mechanize announced **$9.1M** raised at a **$500M post-money valuation** , via [@MechanizeWork](https://x.com/MechanizeWork/status/2047732999878529037).

  * Arcee AI hired Cody Blakeney as Head of Research, emphasizing open-weight American frontier models, via [@code_star](https://x.com/code_star/status/2047765768658702467).

  * Safety / governance:

    * OpenAI announced a **Bio Bug Bounty** for GPT-5.5, per [@OpenAINewsroom](https://x.com/OpenAINewsroom/status/2047670970526175310)

    * Anthropic launched **Project Deal** , a marketplace where Claude negotiated on behalf of employees, and highlighted model-quality asymmetry and policy challenges, via [@AnthropicAI](https://x.com/AnthropicAI/status/2047728360818696302)




**Creative AI and multimodal**

  * GPT Image 2 + Seedance 2 workflows kept drawing attention:

    * [@_OAK200](https://x.com/_OAK200/status/2047616640448078167) and [@awesome_visuals](https://x.com/awesome_visuals/status/2047609881104953658) showed high-fidelity image->video pipelines

    * [@BoyuanChen0](https://x.com/BoyuanChen0/status/2047738501647728937) said **2K/4K** images are already available via experimental API and active fixes are underway

  * Kling announced native **4K output** and a **$25k** short film contest, via [@Kling_ai](https://x.com/Kling_ai/status/2047676942317678879).

  * Some evaluative nuance:

    * [@goodside](https://x.com/goodside/status/2047728776520298646) noted GPT Images 2.0 could render a valid-looking Rubik's Cube state, which is surprisingly hard

    * [@venturetwins](https://x.com/venturetwins/status/2047820435543437630) framed recent image/video gains as a major step toward personalized game-like content generation




* * *

# **AI Reddit Recap**

## **/r/LocalLlama + /r/localLLM Recap**

### **1\. Deepseek V4 and Related Releases**

  * **[Deepseek V4 AGI comfirmed](https://www.reddit.com/r/LocalLLaMA/comments/1suolda/deepseek_v4_agi_comfirmed/)** (Activity: 1138): **The image is a meme and does not contain any technical content. The title "Deepseek V4 AGI confirmed" suggests a humorous or exaggerated claim about an AI model, possibly referencing advancements in artificial general intelligence (AGI). The comments further imply a satirical tone, mentioning uncensored datasets and military applications, which are likely not serious claims.** The comments reflect a satirical take on AI capabilities, with mentions of uncensored datasets and military applications, indicating skepticism or humor rather than a serious technical discussion.

    * UserXtheUnknown discusses a test scenario with Deepseek V4, highlighting its tendency to overthink problems. The model interprets constraints like 'using only one knife' as mandatory rather than optional, which affects its problem-solving approach. This reflects a nuanced understanding of task constraints, but also indicates potential areas for improvement in handling implicit instructions.

  * **[Deepseek V4 Flash and Non-Flash Out on HuggingFace](https://www.reddit.com/r/LocalLLaMA/comments/1su3hdo/deepseek_v4_flash_and_nonflash_out_on_huggingface/)** (Activity: 1393): **DeepSeek V4 has been released on[HuggingFace](https://huggingface.co/collections/deepseek-ai/deepseek-v4), featuring two models: DeepSeek-V4-Pro with **`1.6T parameters`**(of which**`49B`**are activated) and DeepSeek-V4-Flash with**`284B parameters`**(with**`13B`**activated). Both models support a context length of**`one million tokens`**, which is significant for handling extensive sequences. The models are released under the MIT license, allowing for broad use and modification.** A notable comment highlights the challenge of hardware limitations, particularly RAM, when working with such large models. Another comment suggests the potential benefit of a `0.01bit quantization` to manage the model size more effectively.

    * The DeepSeek-V4 models are notable for their massive parameter sizes, with the Pro version having 1.6 trillion parameters (49 billion activated) and the Flash version having 284 billion parameters (13 billion activated). Both models support an extensive context length of one million tokens, which is significant for handling large-scale data inputs and complex tasks.

    * A user expressed interest in a 0.01-bit quantization of the DeepSeek-V4 models, which suggests a focus on reducing the model size and computational requirements while maintaining performance. Quantization is a common technique to optimize models for deployment on hardware with limited resources.

    * The mention of the MIT license indicates that DeepSeek-V4 is open-source, allowing for broad use and modification by the community. This licensing choice can facilitate collaboration and innovation, as developers can freely integrate and adapt the models into their own projects.

  * **[Buried lede: Deepseek v4 Flash is incredibly inexpensive from the official API for its weight category](https://www.reddit.com/r/LocalLLaMA/comments/1su5gj5/buried_lede_deepseek_v4_flash_is_incredibly/)** (Activity: 404): **The image provides a comparison between two models, "deepseek-v4-flash" and "deepseek-v4-pro," highlighting that the "deepseek-v4-flash" model is significantly more affordable in terms of input and output token costs. Despite its affordability, the model supports advanced features like JSON output, tool calls, and chat prefix completion in both non-thinking and thinking modes. The discussion around the image suggests that while the "deepseek-v4-flash" is marketed as inexpensive, some users argue that it is actually overpriced compared to previous versions when considering parameter scaling, with the "V3.2" model being cheaper per parameter.** Commenters discuss the impact of GPU shortages on current pricing, suggesting that prices may decrease as GPU production increases. There is also debate about the pricing strategy, with some users noting that the new model is more expensive per parameter compared to older versions.

    * DistanceSolar1449 highlights a pricing comparison between DeepSeek V3.2 and V4 Flash, noting that V3.2 was priced at `$0.26/0.38` for input/output at `671b`, whereas V4 Flash is `$0.14/$0.28` at `284b`. This suggests that V4 Flash is actually more expensive if pricing were to scale linearly with parameters, challenging the notion of its cost-effectiveness.

    * jwpbe provides a comparative analysis of DeepSeek V4 Flash's API cost, stating that at `14 cents in / 28 cents out`, it is significantly cheaper than competitors like Minimax 2.7, which is `3x` the cost, and Qwen's equivalent, which is even higher. They also mention that Trinity Thinking Large is twice as expensive, indicating that V4 Flash offers a competitive pricing advantage in the market.

    * Worried-Squirrel2023 discusses the strategic implications of Huawei's silicon developments, suggesting that DeepSeek's pricing strategy involves trading NVIDIA margins for Ascend supply. They predict that once the `950 supernodes` scale, DeepSeek could potentially undercut competitors in the open weights tier, leveraging Huawei's advancements to optimize costs.

  * **[Deepseek has released DeepEP V2 and TileKernels.](https://www.reddit.com/r/LocalLLaMA/comments/1ste9zs/deepseek_has_released_deepep_v2_and_tilekernels/)** (Activity: 396): **Deepseek has released DeepEP V2 and TileKernels, which are significant advancements in AI model optimization and parallelization. DeepEP V2 focuses on enhancing model efficiency and accuracy, while TileKernels introduces a novel parallelization technique that reportedly scales linearly, meaning that doubling computational capacity results in a doubling of processing speed. This release is open-sourced, fostering transparency and collaboration in AI research. For more details, see the[DeepEP V2 pull request](https://github.com/deepseek-ai/DeepEP/pull/605) and the [TileKernels repository](https://github.com/deepseek-ai/TileKernels).** One commenter highlights that **Deepseek** is fulfilling a role that **OpenAI** was expected to play by advancing research and sharing findings openly, which builds goodwill despite proprietary technologies. Another commenter questions if the parallelization technique indeed scales linearly, suggesting a significant technical breakthrough if true.

    * **DeepEP V2 and TileKernels** by DeepSeek are noted for their potential advancements in parallelization techniques. A user speculates that these techniques might achieve linear scaling, meaning that doubling computational capacity could directly double processing speed. This could represent a significant efficiency improvement in model training and inference.

    * There is speculation about DeepSeek's hardware usage, particularly regarding the SM100 and Blackwell GPUs. One commenter suggests that DeepSeek might be using Blackwell GPUs for training, possibly through rented B200 units on Vast.ai. This hardware choice could influence the performance and capabilities of their models.

    * The potential innovations in DeepSeek's next model, possibly named v4, are highlighted. The focus is on the integration of Engram and mHC technologies, which are expected to play a crucial role in the model's performance. The success of these innovations will likely depend on the new dataset DeepSeek has developed.




### **2\. Qwen 3.6 Model Performance and Benchmarks**

  * **[This is where we are right now, LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/comments/1suqfba/this_is_where_we_are_right_now_localllama/)** (Activity: 1755): **The image depicts a MacBook Pro running a Qwen3.6 27B model via Llama.cpp, showcasing the capability of executing complex AI models locally, even in airplane mode. This highlights the potential for local AI models to enhance efficiency, security, privacy, and sovereignty by operating independently of cloud services. The post underscores the technological advancement in making powerful AI models accessible on personal devices, emphasizing the importance of local execution for privacy and control.** Commenters express skepticism about the overstatement of the Qwen3.6-27B model's capabilities, suggesting that while it is impressive for its size, it does not match the performance of more advanced models like Sonnet or Opus. There is concern that exaggerated claims could lead to user disappointment and backlash against the broader LLM community.

    * **ttkciar** highlights the potential for user disappointment with the Qwen3.6-27B model, noting that while it's impressive for its size and suitable for agentic code generation, it doesn't match the capabilities of more advanced models like Sonnet or Opus. The concern is that overhyping its abilities could lead to backlash against the broader LLM community, not just the individual making the claims.

    * **sooki10** agrees that while the model is impressive for local coding tasks, comparing it to more advanced models like Opus is misleading and could undermine the credibility of the claims being made. This suggests a need for more accurate benchmarking and communication about the model's capabilities to manage user expectations effectively.

    * **Melodic_Reality_646** points out the disparity in resources, comparing the use of a high-end 128GB RAM m5max system to a more accessible setup. This highlights the importance of considering hardware limitations when evaluating model performance, as not all users have access to such powerful systems, which can skew perceptions of a model's capabilities.

  * **[DS4-Flash vs Qwen3.6](https://www.reddit.com/r/LocalLLaMA/comments/1sub71w/ds4flash_vs_qwen36/)** (Activity: 470): **The image presents a benchmark comparison between DS4-Flash Max and Qwen3.6 models, specifically the**`35B-A3B`**and**`27B`**versions. The chart highlights that DS4-Flash Max generally outperforms the Qwen models across various categories, particularly excelling in 'LiveCodeBench' and 'HLE' benchmarks. This suggests that DS4-Flash Max may have superior capabilities in coding and reasoning tasks. The discussion in the comments hints at the potential for larger models like a **`122B`**version of Qwen3.6, and emphasizes the significance of the**`1M token context`**feature, which could impact performance in other benchmarks like 'omniscense'.** Commenters note that despite DS4-Flash Max's larger size, its performance is only slightly better than Qwen3.6, raising questions about efficiency versus scale. The `1M token context` is highlighted as a significant feature that could influence future benchmark results.

    * **Rascazzione** highlights the significant increase in context length with Qwen 3.6, noting its ability to handle a 1 million token context. This is a substantial improvement over previous models and could have significant implications for tasks requiring extensive context handling, such as document summarization or complex dialogue systems.

    * **LinkSea8324** points out the size difference between the models, with DS4-Flash at 284 billion parameters compared to Qwen 3.6's 27 billion. This raises questions about the efficiency and performance trade-offs between model size and capability, especially in terms of computational resources and inference speed.

    * **madsheepPL** discusses the non-linear nature of benchmark improvements, suggesting that even if a model appears only slightly better in benchmarks, the practical implications can be more significant. They emphasize that improvements in scores are not directly proportional and can have varying impacts on real-world applications.

  * **[Qwen 3.6 27B Makes Huge Gains in Agency on Artificial Analysis - Ties with Sonnet 4.6](https://www.reddit.com/r/LocalLLaMA/comments/1strodp/qwen_36_27b_makes_huge_gains_in_agency_on/)** (Activity: 964): **Qwen 3.6 27B has achieved parity with Sonnet 4.6 on the Agentic Index from Artificial Analysis, surpassing models like Gemini 3.1 Pro Preview, GPT 5.2 and 5.3, and MiniMax 2.7. The model shows improvements across all indices, although the gains in the Coding Index are less pronounced due to its reliance on benchmarks like Terminal Bench Hard and SciCode, which are considered unconventional. The focus of training appears to be on agentic applications for OpenClaw/Hermes, highlighting the potential of smaller models to approach frontier capabilities. Anticipation is building for the upcoming Qwen 3.6 122B model.** Commenters express excitement about the potential of smaller models like Qwen 3.6 27B, noting the significant improvements and potential for future versions. However, there is skepticism about the extent of these gains, suggesting that some improvements might be due to 'benchmaxxing' rather than inherent model capabilities.

    * Iory1998 highlights the impressive performance of the Qwen 3.6 27B model, noting that it surpasses a 670B model from the previous year. They mention running the Q8 version at 170K with KV cache at FP16 on an RTX 3090 and RTX 5070ti, utilizing 40GB of VRAM, which underscores the model's efficiency and power.

    * AngeloKappos discusses the narrowing benchmark gap, sharing their experience running the Qwen3-30b-a3b model on an M2 chip. They note its capability to handle multi-step tool calls effectively, suggesting that if the 27B dense model performs this well, the upcoming 122B model could pose challenges for API providers due to its potential performance.

    * Velocita84 raises a point about potential "benchmaxxing" in the reported performance gains of the Qwen 3.6 27B model, implying that some of the improvements might be attributed to optimized benchmarking rather than inherent model capabilities. This suggests a need for scrutiny in evaluating model performance claims.

  * **[Compared QWEN 3.6 35B with QWEN 3.6 27B for coding primitives](https://www.reddit.com/r/LocalLLaMA/comments/1styxdy/compared_qwen_36_35b_with_qwen_36_27b_for_coding/)** (Activity: 491): **The post compares two versions of the QWEN 3.6 model, specifically the**`35B`**and**`27B`**parameter versions, on a MacBook Pro M5 MAX with**`64GB`**RAM. The**`35B`**model achieves**`72 TPS`**(tokens per second), while the**`27B`**model achieves**`18 TPS`**. Despite the slower speed, the**`27B`**model produces more precise and correct results for coding tasks, whereas the**`35B`**model is faster but less accurate. The test involved generating a single HTML file to simulate a moving car with a parallax effect, using no external libraries. The models were hosted using[Atomic.Chat](http://atomic.chat/), with source code available on [GitHub](https://github.com/AtomicBot-ai/Atomic-Chat).** One comment highlights the output of the `Qwen 3.6 27B FP8` model using opencode, taking approximately `52 seconds`. Another comment provides a visual comparison with the `Qwen 3.5 27B Q3` model, suggesting differences in output quality.

    * The user 'sacrelege' shared a performance result for the Qwen 3.6 27B model using FP8 precision, noting that it took approximately 52 seconds to complete a task with 'opencode'. This suggests a focus on optimizing model performance through precision adjustments, which can significantly impact computational efficiency and speed.

    * User 'nikhilprasanth' provided a visual comparison for the Qwen 3.5 27B Q3 model, indicating a potential interest in comparing different versions and quantization levels of the Qwen models. This highlights the importance of understanding how different model configurations can affect performance and output quality.

    * 'Technical-Earth-3254' inquired about the quantization methods used in the tests, which is crucial for understanding the trade-offs between model size, speed, and accuracy. Quantization can greatly influence the efficiency of large models like Qwen, especially in resource-constrained environments.

  * **[Qwen 3.6 27B is a BEAST](https://www.reddit.com/r/LocalLLaMA/comments/1steip4/qwen_36_27b_is_a_beast/)** (Activity: 1239): **The post discusses the performance of the Qwen 3.6 27B model on a high-end laptop with an RTX 5090 GPU and**`24GB VRAM`**, highlighting its effectiveness for pyspark/python and data transformation debugging tasks. The user employs llama.cpp with**`q4_k_m`**at**`q4_0`**and is exploring further optimizations with IQ4_XS at**`200k q8_0`**. The user has not yet implemented speculative decoding. The setup includes an ASUS ROG Strix SCAR 18 with**`64GB DDR5 RAM`**.** Comments suggest avoiding kv cache as q4 for coding, recommending `q8` for `130k` context. Another comment anticipates performance improvements with upcoming releases from **z-lab** and a specific [GitHub pull request](https://github.com/ggml-org/llama.cpp/pull/22105) that promises a `2x` decode speed increase. There is also curiosity about the model's performance on systems with `16GB VRAM` and `32GB DDR5 RAM` with offloading.

    * sagiroth highlights a technical consideration when using Qwen 3.6 27B for coding tasks, advising against using the KV cache as q4 due to limitations, and instead suggests using q8 to achieve a `130k` context window, which can significantly enhance performance for large context tasks.

    * inkberk points out an upcoming improvement in decoding speed, referencing a pull request [#22105](https://github.com/ggml-org/llama.cpp/pull/22105) on the `llama.cpp` repository. This update, along with the anticipated release of the 'dflash drafter' by z-lab, promises a potential `2x` increase in decode speed, which could greatly benefit users in terms of efficiency.

    * Johnny_Rell inquires about the performance of Qwen 3.6 27B on a system with `16 GB VRAM` and `32 GB DDR5`, specifically regarding the effectiveness of offloading. This suggests a focus on optimizing resource allocation to handle the model's demands, which is crucial for running large models efficiently on consumer-grade hardware.




[ Read more ](https://www.latent.space/p/ainews-deepseek-v4-pro-16t-a49b-and)

---

## [[AINews] GPT 5.5 and OpenAI Codex Superapp](https://www.latent.space/p/ainews-gpt-55-and-openai-codex-superapp)
*🔬 Latent Space | 2026-04-24*

A week after [Opus 4.7](https://www.latent.space/p/ainews-anthropic-claude-opus-47-literally), it was OpenAI's turn to fire back with very similar Pareto frontier improvement charts for [GPT 5.5](https://openai.com/index/introducing-gpt-5-5/) (as [Noam Brown prefers](https://x.com/polynoamial/status/2047387675762802998?s=46) -- raw 1 dimensional intelligence measures are giving way to 2D intelligence per dollar charts). In the 4.7 vs 5.5 bakeoff, you have to read between the lines to see what was NOT mentioned ([coding](https://x.com/chowdhuryneil/status/2047416077622395025?s=46)), but in terms of overall intelligence, AA crowns this the top independently validated model in the world, AND…

[](https://substackcdn.com/image/fetch/$s_!0uGP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2f9f5845-e1e6-497a-9bed-f6457169247c_2048x684.png)[AA chart](https://x.com/ArtificialAnlys/status/2047378419282034920)

… intelligence per dollar ("_**GPT-5.5 (medium)** scores the same as **Claude Opus 4.7 (max)** on our Intelligence Index at **one quarter of the cost (~$1,200 vs $4,800)** \- although Gemini 3.1 Pro Preview scores the same at a cost of **~$900**._"

[](https://substackcdn.com/image/fetch/$s_!-taB!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F39e50c45-bc8a-4f60-a562-026d1c7bd14d_1026x662.png)[aa 2D ](https://x.com/scaling01/status/2047380890402123928?s=20)

There are [some training hardware tidbits](https://x.com/scaling01/status/2047425178724921618?s=46) and [positive](https://x.com/tszzl/status/2047386955550470245?s=46) [RSI](https://x.com/aidan_mclau/status/2047388367705575701?s=46) vibes and [cool](https://x.com/clad3815/status/2047392779006013833?s=12) [alternative](https://x.com/andonlabs/status/2047377260412649967?s=46) [benchmarks](https://x.com/sebastienbubeck/status/2047383628922167390?s=46).

But if you just treated today as a mere point update model launch ([some would prefer to call it 5.9](https://x.com/davis7/status/2047414463595528467)), you'd be mistaken - it's also [bundling ](https://x.com/sama/status/2047378431260664058?s=20)a big Codex launch day:

[](https://substackcdn.com/image/fetch/$s_!BWef!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fec7c1f27-a6ba-4a70-ba86-24eb303591c8_1030x1254.png)[twitter](https://x.com/thsottiaux/status/2047387017974337611?s=46)

With built in browser control and the other features in [this mega-update](https://x.com/ajambrosino/status/2047381565534322694?s=20), as well as folding in the now defunct [Prism](https://www.youtube.com/watch?v=W2cBTVr8nxU&pp=2AYl0gcJCZEKAYcqIYzv) (RIP), OpenAI seems to have made the critical and retoractively obvious choice to turn Codex into the [base of its superapp strategy](https://www.wsj.com/tech/openai-plans-launch-of-desktop-superapp-to-refocus-simplify-user-experience-9e19931d).

[](https://substackcdn.com/image/fetch/$s_!F1N8!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcabd0f35-0766-4080-82b3-c90f52faa849_954x1416.png)

> AI News for 4/22/2026-4/23/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

# **AI Twitter Recap**

**OpenAI 's GPT-5.5 launch: stronger agentic coding, broader computer use, and a push on token-efficiency**

  * **GPT-5.5 is the day 's dominant release**: OpenAI launched [GPT-5.5](https://x.com/OpenAI/status/2047376561205325845), positioned as "a new class of intelligence for real work," with rollout across [ChatGPT and Codex](https://x.com/OpenAI/status/2047376568809636017) and API access delayed pending additional safeguards. OpenAI and community benchmark posts converged on a profile of **better long-horizon execution, stronger computer-use behavior, and materially improved token efficiency** rather than a pure across-the-board benchmark blowout. Reported numbers include **82.7% Terminal-Bench 2.0** , **58.6% SWE-Bench Pro** , **84.9% GDPval** , **78.7% OSWorld-Verified** , **81.8% CyberGym** , **84.4% BrowseComp** , and **51.7% FrontierMath Tier 1 -3** via [@reach_vb](https://x.com/reach_vb/status/2047377562339524659), with Artificial Analysis saying GPT-5.5 now leads or ties several headline evals and sits on a new cost/performance frontier despite higher per-token pricing [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2047378419282034920), [@scaling01](https://x.com/scaling01/status/2047380890402123928). OpenAI also emphasized that in ChatGPT, stack-level inference gains made **GPT-5.5 Pro more practical** for demanding tasks [@OpenAI](https://x.com/OpenAI/status/2047376567559668222).

  * **Pricing, context, infra, and practical behavior** : API pricing was reported at **$5/$30 per 1M input/output tokens** for GPT-5.5 and **$30/$180** for Pro [@scaling01](https://x.com/scaling01/status/2047375819144597737), with [Sam Altman noting](https://x.com/sama/status/2047379036419014928) a **1M context window** in API and lower token use per task than 5.4. Multiple early users described the model as more "human," less formal, and better suited to persistent agent workflows than prior GPTs, especially inside Codex [@MatthewBerman](https://x.com/MatthewBerman/status/2047375703516361174), [@danshipper](https://x.com/danshipper/status/2047375686688473134), [@omarsar0](https://x.com/omarsar0/status/2047424707310289058). OpenAI claimed the model was **co-designed for NVIDIA GB200/300 systems** and that the model itself helped improve its own inference stack [@scaling01](https://x.com/scaling01/status/2047377992016384068), while [@sama](https://x.com/sama/status/2047386068194852963) framed the company increasingly as an **AI inference company**. A recurrent theme from users: GPT-5.5 often feels like a **step-function upgrade in autonomy** , but can also be exploratory and require tighter instruction to stay on track [@theo](https://x.com/theo/status/2047379702189310085).

  * **Codex becomes a fuller agent workspace** : In parallel, OpenAI shipped substantial Codex upgrades: **browser control** , **Sheets/Slides** , **Docs/PDFs** , **OS-wide dictation** , and **auto-review mode** [@ajambrosino](https://x.com/ajambrosino/status/2047381565534322694). OpenAI says Codex can now interact with web apps, click through flows, capture screenshots, and iterate until task completion [@OpenAIDevs](https://x.com/OpenAIDevs/status/2047381283358355706), while **Auto-review** uses a secondary "guardian" agent to reduce approvals on longer runs [@OpenAIDevs](https://x.com/OpenAIDevs/status/2047436655863464011), [@gdb](https://x.com/gdb/status/2047489218998628780). User reports suggest this is expanding Codex from a coding tool into a broader **computer-work agent** , spanning QA, spreadsheets, presentations, app building, research loops, and overnight experimental runs [@gdb](https://x.com/gdb/status/2047387783111868707), [@tszzl](https://x.com/tszzl/status/2047386955550470245), [@aidan_mclau](https://x.com/aidan_mclau/status/2047388367705575701).




**DeepSeek-V4 Preview: 1.6T MIT-licensed open model, 1M context, and aggressive pricing**

  * **DeepSeek answered GPT-5.5 within hours** : DeepSeek released [DeepSeek-V4 Preview](https://x.com/deepseek_ai/status/2047516922263285776), open-sourcing **V4-Pro** and **V4-Flash** under an **MIT license**. The headline specs are unusually aggressive: **V4-Pro: 1.6T total params / 49B active** , **V4-Flash: 284B / 13B active** , both with **1M token context** and support for thinking/non-thinking modes [@deepseek_ai](https://x.com/deepseek_ai/status/2047516945466188072), [@Yuchenj_UW](https://x.com/Yuchenj_UW/status/2047514092756418757). Community reactions quickly framed it as the new **open-model flagship** , competitive with top closed models from the prior generation and a major leap over DeepSeek V3.x [@arena](https://x.com/arena/status/2047518354903359697), [@scaling01](https://x.com/scaling01/status/2047512176856899985), [@kimmonismus](https://x.com/kimmonismus/status/2047514623356579869).

  * **Technical report highlights: long-context efficiency, hybrid attention, and Muon** : The launch was notable not just for weights but for a same-day tech report [@scaling01](https://x.com/scaling01/status/2047510520618516572). Community summaries point to **two new compressed/hybrid attention mechanisms** , **mHC** , **Muon-based training** , **FP4 quantization-aware training** , and pretraining on roughly **32T tokens** [@scaling01](https://x.com/scaling01/status/2047510190044409860), [@iScienceLuvr](https://x.com/iScienceLuvr/status/2047514399393579235), [@eliebakouch](https://x.com/eliebakouch/status/2047519300399837677). The strongest technical discussion centered on making **1M context practical** , with reported **~4x compute efficiency improvements** and **order-of-magnitude KV-cache reductions** relative to earlier DeepSeek-style stacks [@Hangsiin](https://x.com/Hangsiin/status/2047523724929405328). The rapid infra response was also notable: **vLLM** announced [day-0 support](https://x.com/vllm_project/status/2047520252851105796) and detailed how it implemented the new attention stack; **SGLang** shipped [day-0 optimizations and RL pipeline support](https://x.com/lmsysorg/status/2047511629919932623).

  * **Pricing may be as important as the model** : DeepSeek's posted pricing is exceptionally aggressive: **V4-Flash at $0.14/$0.28** and **V4-Pro at $1.74/$3.48 per 1M input/output tokens** [@scaling01](https://x.com/scaling01/status/2047508350238175526), [@teortaxesTex](https://x.com/teortaxesTex/status/2047508587883250112). Several commenters highlighted Flash as potentially the more disruptive SKU if serving quality holds, given the combination of **very low cost** , **1M context** , and open weights [@Hangsiin](https://x.com/Hangsiin/status/2047515855949623667), [@arena](https://x.com/arena/status/2047524055679729885). The main caveat from DeepSeek: **V4-Pro throughput is currently limited by high-end compute constraints** , with the company explicitly pointing to future **Ascend 950** availability for price drops [@teortaxesTex](https://x.com/teortaxesTex/status/2047523707199909977).




**Agent infrastructure and tooling: memory, orchestration, browsers, and enterprise plumbing**

  * **Agents are becoming systems problems, not just model problems** : Several posts emphasized that production agent work is increasingly about **harnesses, evals, memory, and orchestration**. A useful example was the writeup on **stateless decision memory** for enterprise agents, which replaces mutable per-agent state with immutable decision logs/event sourcing to improve **horizontal scalability, auditability, and fault tolerance** [@omarsar0](https://x.com/omarsar0/status/2047325132096758228). In a similar vein, [@Vtrivedy10](https://x.com/Vtrivedy10/status/2047362615836336473) argued that **trace data -> evals/environments -> harness engineering/SFT-RL** is the core flywheel for improving production agents, and later used Anthropic's Claude Code regression as a case study for why **open harnesses and open evals** matter [@Vtrivedy10](https://x.com/Vtrivedy10/status/2047384831995371631).

  * **New tooling around control surfaces** : Cua open-sourced [Cua Driver](https://x.com/trycua/status/2047383200348221632), a macOS driver for letting agents control arbitrary apps in the background with multi-player/multi-cursor support. Cognition published a post on [what it takes to build cloud agent infrastructure](https://x.com/cognition/status/2047392064355377194), naming the practical stack: **VM isolation, session persistence, environment provisioning, orchestration, and integrations**. LangChain continued expanding **LangSmith Fleet** with file editing, webpage/presentation generation, and slash-command skills [@LangChain](https://x.com/LangChain/status/2047362259983495215), while multiple users highlighted Fleet's **presentation renderer/viewer** as a surprisingly useful agent-native artifact format [@BraceSproul](https://x.com/BraceSproul/status/2047417882423022034).

  * **Multi-agent orchestration is moving into products** : Sakana AI launched the beta of **Fugu** , a multi-agent orchestration API that dynamically selects and coordinates frontier models, with claims of SOTA on **SWE-Pro, GPQA-D, and ALE-Bench** and even **recursive test-time scaling** via self-invocation [@SakanaAILabs](https://x.com/SakanaAILabs/status/2047479445209145785), [@hardmaru](https://x.com/hardmaru/status/2047483783323283941). Hermes Agent shipped [v0.11.0](https://x.com/Teknium/status/2047506967909015907) with a large contributor release, expanded providers, image generation support, and effectively immediate GPT-5.5 support [@Teknium](https://x.com/Teknium/status/2047419336537846193). The direction is consistent: **agents are becoming orchestration layers over heterogeneous tools and models** , not single-model loops.




**Vision, video, and multimodal systems: Vision Banana, Sapiens2, HDR video, and omni models**

  * **Google DeepMind 's Vision Banana reframes CV as generation**: One of the more technically interesting research launches was [Vision Banana](https://x.com/songyoupeng/status/2047312019976785944), a **unified vision model** that treats **2D/3D vision tasks as image generation** , reportedly outperforming specialist SOTA systems across multiple vision tasks. The reaction from computer-vision researchers was that it signals a broader shift in how segmentation, depth, normals, and related tasks may be approached going forward [@sainingxie](https://x.com/sainingxie/status/2047339789926429166). On the open side, Meta also released **Sapiens2** , a set of high-resolution vision transformers trained on **1B human images** for human-centric perception tasks [@HuggingPapers](https://x.com/HuggingPapers/status/2047410529010844044).

  * **Video stack updates are moving past raw resolution into production formats** : Kling's "native 4K" rollout spread across multiple platforms, but the technically more novel launch may be **LTX HDR beta** , which argues the real bottleneck for AI video in production has been **dynamic range** , not just resolution, by moving beyond 8-bit SDR toward footage that can survive grading and compositing [@ltx_model](https://x.com/ltx_model/status/2047333864587018703). That's a more substantive improvement than the usual "4K" marketing alone. Separately, World Labs launched **World Jam** around **Marble 1.1 + Spark LoD** for interactive 3D creation [@theworldlabs](https://x.com/theworldlabs/status/2047373234174304473).

  * **Broader multimodal trend: unified models with explicit cross-modal reasoning** : The newly shared **Context Unrolling in Omni Models** proposes a unified model trained across text, images, video, 3D geometry, and hidden representations, explicitly unrolling reasoning across modalities before producing outputs [@arankomatsuzaki](https://x.com/arankomatsuzaki/status/2047519009004716097). Together with Vision Banana, this points to a recurring motif: **fold disparate perception/generation tasks into fewer general multimodal backbones** , then let inference-time reasoning bridge modalities.




**Training, scaling, and research methods: globally distributed pretraining, self-play, and long-context internals**

  * **Google 's Decoupled DiLoCo tackles resilient global pretraining**: Google DeepMind and Google Research introduced [Decoupled DiLoCo](https://x.com/Ar_Douillard/status/2047329942547968171), which decouples distributed low-communication training to enable **worldwide datacenter training** , **heterogeneous hardware** , and tolerance to hardware failures without halting the job. This is a meaningful systems result because it targets a real frontier training bottleneck: keeping giant training runs alive and efficient across **faulty, geographically distributed infrastructure** , rather than assuming clean homogeneous clusters.

  * **Algorithmic scaling beyond brute-force sampling** : A self-play paper highlighted by [@LukeBailey181](https://x.com/LukeBailey181/status/2047340293490724945) studies why long-run self-play plateaus for LLMs and proposes an algorithm that lets a **7B model solve as many problems as pass@4 of a model 100x larger**. Another recurring theme was **token/computation efficiency** as the real frontier metric; several posts argued that single-number intelligence comparisons are increasingly obsolete in a world where effort level and inference budget materially reshape capability [@polynoamial](https://x.com/polynoamial/status/2047387675762802998). Relatedly, a thread on **Neural Garbage Collection** described training models to manage their own KV cache via RL rather than fixed heuristics, a potentially important direction for long-horizon agents [@cwolferesearch](https://x.com/cwolferesearch/status/2047476297031631102).

  * **Infra adoption signals** : Together AI reported growth from **30B to 300T tokens/month YoY** [@vipulved](https://x.com/vipulved/status/2047183589222273231), a large-scale indicator of inference demand expansion. Epoch AI, meanwhile, revised down estimates for operational power at **Stargate Abilene** to **~0.3 GW** currently and pushed the full **1.2 GW** milestone to **Q4 2026** , underscoring continued uncertainty in tracking frontier compute deployment [@EpochAIResearch](https://x.com/EpochAIResearch/status/2047442515608162481).




**Top tweets (by engagement)**

  * **OpenAI GPT-5.5 launch** : The highest-engagement technical post was OpenAI's [GPT-5.5 announcement](https://x.com/OpenAI/status/2047376561205325845), followed by [@sama's launch post](https://x.com/sama/status/2047378253313106112) and OpenAI DevRel's framing of GPT-5.5 as its smartest frontier model yet [@OpenAIDevs](https://x.com/OpenAIDevs/status/2047377079352877534).

  * **Claude Code regression post-mortem** : Anthropic's acknowledgment that [Claude Code quality had slipped due to three issues and was fixed in v2.1.116+](https://x.com/ClaudeDevs/status/2047371123185287223) was one of the most engaged engineering-product posts of the day, and sparked substantial discussion about harness sensitivity and regression testing.

  * **DeepSeek-V4 Preview release** : DeepSeek's [official V4 Preview launch](https://x.com/deepseek_ai/status/2047516922263285776) quickly became the other major high-engagement technical event, especially given the combination of **MIT license** , **1M context** , and aggressive pricing.

  * **Vision Banana** : Google DeepMind's [Vision Banana announcement](https://x.com/songyoupeng/status/2047312019976785944) was the standout pure-research vision post.

  * **ML-Intern and autonomous research workflows** : The Hugging Face-adjacent [ml-intern passing an internship-style test in 15 minutes](https://x.com/akseljoonas/status/2047332440025321796) and subsequent reports of very high token consumption suggest strong interest in autonomous coding/research harnesses as distinct products, not just demos.




* * *

# **AI Reddit Recap**

## **/r/LocalLlama + /r/localLLM Recap**

[ Read more ](https://www.latent.space/p/ainews-gpt-55-and-openai-codex-superapp)

---

## [AIE Europe Debrief + Agent Labs Thesis: Unsupervised Learning x Latent Space Crossover Special (2026)](https://www.latent.space/p/unsupervised-learning-2026)
*🔬 Latent Space | 2026-04-23*

Today, we check in a year after the [first ](https://www.latent.space/p/unsupervised-learning)**[Unsupervised Learning x Latent Space Crossover special](https://www.latent.space/p/unsupervised-learning) **to discuss everything that has changed (there is a lot) in the world of AI. _This episode was recorded just after[AIE Europe](https://www.ai.engineer/europe/), but before [the Cursor-xAI deal](https://cursor.com/blog/spacex-model-training)._

**Unsupervised Learning** is a podcast that interviews the sharpest minds in AI about what's real today, what will be real in the future and what it means for businesses and the world - helping builders, researchers and founders deconstruct and understand the biggest breakthroughs.

**Thanks to Jacob and the UL production team for hosting and editing this!**

* * *

**Jacob Effron**

  * **LinkedIn:** <https://www.linkedin.com/in/jacobeffron/>

  * **X:** <https://x.com/jacobeffron>




* * *

## Full Episode on Their YouTube

## We discuss:

  * swyx's view from the center of the AI engineering zeitgeist: OpenClaw, harness engineering, context engineering, evals, observability, GPUs, multimodality, and why conference tracks now reveal what matters most in AI

  * Whether AI infrastructure has finally stabilized: why "skills" may be the minimal viable packaging format for agents, why infra companies have had to reinvent themselves every year, and why application companies have had an easier time surviving model volatility

  * The vertical vs. horizontal AI startup debate: why application companies can act as the outsourced AI team for enterprises, why some horizontal companies still matter, and why sandboxes may be the clearest reinvention of classic cloud infrastructure for the AI era

  * The "agent lab" playbook: starting with frontier models, specializing for your domain, then training your own models once you have enough data, workload, and user behavior to justify the cost and latency savings

  * Why domain-specific model training is real, not just marketing: how companies like Cursor and Cognition can get users to choose their in-house models, and why search, domain specialization, and distillation are becoming more important

  * Open models, custom chips, and alternative inference infrastructure: why swyx has turned more bullish on open source, why non-NVIDIA hardware is suddenly getting real attention, and why every 10x speedup can unlock new product experiences

  * What it means to sell to agents instead of humans: why agent experience may mostly just be good developer experience by another name, why APIs and docs matter more than ever, and how pretraining-data incumbents are compounding advantages in an agent-first world

  * Why memory and personalization may become the next big wedge: today's models mostly reward frequency of mentions, but in the future, swyx expects product choice to be shaped much more by personalized memory systems

  * The state of the AI coding wars: why coding has become one of the largest and fastest-growing categories in AI, how Anthropic, OpenAI, Cursor, and Cognition have all ridden the wave, and why the category may still have more room to run

  * Capability exploration vs. efficiency: why the industry is still in a token-maxing, experiment-heavy phase where people are rewarded for spending more rather than less

  * Claude Code vs. Codex and the strange stickiness of coding products: why first magical product experiences may matter more than expected, and why the bigger mystery may be why only a few names have emerged as real winners so far

  * What the end state of the coding market might look like: two major players, a longer tail of niche products, and possible disruption if Microsoft, Mistral, xAI, or the Chinese labs push harder into coding

  * Where application companies still have room against the labs: why frontier labs are trying to expand into verticals like finance and healthcare, but still leave space for focused companies that own the workflow and the last mile

  * Why coding may be a preview of every other AI market: the first category to truly go parabolic, the clearest example of foundation model companies colliding with application companies, and a template for how future vertical AI markets may develop

  * Why AI valuations now feel unbounded: from billion-dollar ARR products built in a year to trillion-dollar market caps, swyx and Jacob unpack how the AI market has broken traditional startup intuitions about scale and durability

  * Consumer AI vs. coding AI: why ChatGPT's consumer category may have plateaued on frequency and product design, while coding continues to feel like a daily-use category with real momentum

  * The next product frontier beyond coding: consumer agents, computer use, and "coding agents breaking containment," with swyx's thesis that 2025 was the year of coding agents and 2026 may be the year they begin to do everything else

  * Whether foundation models are really killing startup categories: why swyx is less worried for early founders, more worried for mid-size startups and traditional SaaS, and why building something ambitious may now be the best job interview for a frontier lab

  * AI vs. SaaS and the internal culture war around adoption: the tension between AI-native employees who want to rip out expensive software and skeptics who think quick AI-built replacements create fragile systems

  * Why traditional SaaS may be under real pressure: swyx's own experience spending six figures on event and sponsor management software, the temptation to rebuild it cheaply with AI, and the broader question of whether teams will trust custom AI-native replacements

  * Biosafety, security, and frontier model access: why swyx raised biosafety at a dinner with Anthropic's Mike Krieger, why Krieger argued security is the bigger issue, and what restricted model releases reveal about Anthropic vs. OpenAI

  * The era of giant models: why 10T+ parameter systems may only be a temporary rationing phase before bigger clusters arrive, why labs may increasingly keep their most powerful models private for distillation, and why scale alone no longer feels like a complete answer

  * Memory as the slowest scaling factor in AI: why context windows have improved far more slowly than people hoped, why million-token context still has not changed most real workflows, and why memory may be the key bottleneck for the next generation of systems

  * What swyx changed his mind on in the past year: becoming more bullish on open models, more convinced that the top tier of agent startups behaves very differently from the median AI company, and more optimistic about fine-tuning and specialized model adaptation

  * "Dark factories" and zero-human-review coding: the next frontier after zero human-written code, where models not only write the code but ship it without human review, forcing companies to rethink testing and verification from first principles

  * Why RL and post-training may matter more than people assumed: even if the resulting models get thrown out every few months, the data, workflows, and domain-specific improvements persist

  * Synthetic rubrics, Doctor GRPO, and multi-turn RL: why reinforcement learning is becoming much more domain-specific and multi-step than many people realize, opening the door to much deeper customization

  * The next frontier after coding: memory, personalization, and world models, including why swyx thinks world models matter not just for robotics or gaming, but for giving AI something closer to lived understanding

  * Fei-Fei Li, spatial intelligence, and the Good Will Hunting analogy: the idea that today's LLMs may know everything by reading it all, but still lack the lived experience that turns knowledge into a deeper kind of intelligence




* * *

## Timestamps

  * **00:00:00** Intro preview: AI coding wars, startup pressure, and market structure

  * **00:00:28** Welcome to the Latent Space × Unsupervised Learning crossover

  * **00:01:17** What AI builders are focused on now: OpenClaw, harnesses, and infra

  * **00:04:33** Why AI infra is harder than apps, and where startups can still win

  * **00:06:39** Should companies train their own models?

  * **00:09:28** Open models, custom chips, and the new inference race

  * **00:11:25** Designing products for agents, not just humans

  * **00:16:49** The state of the AI coding wars in 2026

  * **00:19:27** Capability exploration, token-maxing, and why coding is going parabolic

  * **00:21:41** What the end state of the coding market could look like

  * **00:23:50** Where app companies still have room against the labs

  * **00:27:02** Why AI valuations and market swings feel unprecedented

  * **00:28:56** Consumer AI vs. coding AI, and why sticky products still matter

  * **00:32:28** What the next breakthrough product experience might be

  * **00:32:53** 2026 thesis: coding agents break containment and eat the world

  * **00:35:27** Are foundation models wiping out startup categories?

  * **00:37:33** AI vs. SaaS, vibe coding, and internal team tensions

  * **00:40:01** Biosafety, security, and the politics of restricted model releases

  * **00:42:19** Giant models, compute constraints, and the limits of scale

  * **00:44:30** Memory as the real bottleneck in AI

  * **00:44:57** Why swyx changed his mind on open models

  * **00:47:44** Dark factories and the future of zero-human-review coding

  * **00:49:36** Why post-training and RL may matter more than people think

  * **00:51:50** Memory, world models, and the next frontier of intelligence

  * **00:53:54** The Good Will Hunting analogy for LLMs

  * **00:54:21** Outro




## Transcript

[00:00:00] **swyx** : Isn't that crazy? That number is just mind boggling.

[00:00:03] **Jacob Effron** : What is the state of the AI coding wars today?

[00:00:05] **swyx** : We're in a phase of sort of like capability exploration. The general thesis that I have been pursuing now is that the same way that 2025 was a year coding agents 2026 is coding agents breaking containments to do everything else.

[00:00:16] **Jacob Effron** : Do you worry about the foundation models just getting into a bunch of these startup categories?

[00:00:21] **swyx** : Mid-size startups. Yes.

[00:00:23] **Jacob Effron** : What do you think the end state of this market is

[00:00:25] **swyx** : for the market structure to, to significantly change? There would be

[00:00:28] **Jacob Effron** : today on unsupervised learning. We had a, a fun episode and what's really become an annual tradition, a crossover episode with our friends at Latent space.

Swix and I sat down and we talked about everything happening in the AI ecosystem today. What we thought of the various changes at the model layer, what's happening in the infra world, the coding wars, and a bunch of other things. It's a ton of fun to do this with someone I really respect and another great podcaster in the game.

Without further ado, here's our episode. Well switch. This is, uh, super fun to be back with another unsupervised learning, uh, latent space crossover episode.

[00:01:02] **swyx** : Yeah,

[00:01:02] **Jacob Effron** : I feel like a lot of places we could start, but you know, one thing I always find fascinating, uh, about the way you spend your time is you obviously are like at the epicenter of this engineering movement and community, and you run these events and conferences and put on these.

Awesome talks and, and I think just have a great pulse on the zeitgeist of what's going on.

[00:01:16] **swyx** : Yeah.

[00:01:17] **Jacob Effron** : Maybe to, to start just what are the biggest topics people are thinking about right now?

[00:01:21] **swyx** : Yeah, so I just came back from London, uh, where we did a IE Europe and we're doing roughly one per quarter now, which Yeah, you've

[00:01:27] **Jacob Effron** : really up

[00:01:27] **swyx** : the, hopefully

[00:01:28] **Jacob Effron** : up the, up the pace.

[00:01:29] **swyx** : It's trying. We're trying to match AI speed, you

know?

[00:01:30] **Jacob Effron** : Yeah, exactly. The tops would be completely different, I imagine. Uh,

[00:01:33] **swyx** : yeah. You know, I definitely curate the tracks, like you can see what I think. When you see the track list and the, the speakers that I invite, obviously Open Claw is like the story of the last four or five months, and then be, be just below that.

I would consider harness engineering, context engineering to be two related topics in agents and rag. And then there's a long tail of Evergreen stuff like evals, observability, GPUs, uh, and uh, LM infra and just general, just in general. We also have other updates on like multimodality and, uh, generative media, let's call it.

Um, but I definitely, the, the first three that I mentioned are top of mind people. Yeah.

[00:02:13] **Jacob Effron** : I think harness is particular like, so interesting. Um, you know, there was this tweet from Harrison Chase, the, the lane chain, CEO, that, that caught my eye recently where he said, you know, it finally feels like we have stability, uh, around the infrastructure for, uh, you know, around ai.

And I think what. He basically was implying his like, look over the past two, three years as a company at the epicenter of AI infrastructure, it was a bit like playing whack-a-mole, right? You were constantly moving around with, however, the building patterns were evolving

[00:02:36] **swyx** : for Harrison for sure. Right? Like he's basically had to reinvent the company every year since he started Lang Chain.

Right? It was Lang chain, Ang graph and LP agents and like, uh, I think he's like one of the most nimble, adept sharp people about this. Yeah. Yeah.

[00:02:49] **Jacob Effron** : Saying now, now is finally the time stability

[00:02:51] **swyx** : this. Yeah.

[00:02:52] **Jacob Effron** : Yeah. Um, do you buy that or what have you kind of make of that take?

[00:02:56] **swyx** : I think that. It, it's very expensive to say this Time is different sometimes, but when you're just writing code, like it's actually okay to just like try to make a call and I think it may not even matter if this call is right or not.

Like I just don't even care that much because you can be right on a thesis, but if you don't, you don't figure out how to monetize the thesis, then who cares if you said something first that said, um, it does feel like, for example. Uh, we went through a lot of different ways of passion packaging integrations up with, uh, with agents.

And it feels like we've landed at skills, which is like the minimal viable format. Yeah. Which is just a markdown file, uh, with some scripts attached to it, and I don't see how it can be more simple than that. And so there is some justification for. The stability around harnesses. I feel like there may be more adaptation with regards to maybe like the real time elements or subagents or memory or any of those like agent disciplines, let's call it in, in agent engineering.

Uh, but if, if the thesis is that, okay, you just want agents are LMS with tools in the loop with a file system, what they can do. Retrieval with, with skills and all these like standard tooling that now seems to be relatively consensus then probably. That makes sense. Um, I just think like there's no point trying to stake your reputation on this thesis that we're there because if it changes again, just change with it.

It's fine.

[00:04:33] **Jacob Effron** : Yeah. It's always, you know, I've always been struck by how that is. Much more challenging for infrastructure companies and application companies. Like obviously I think, yeah. You know, on the application side you've seen, you know, Brett Taylor from Sierra Max, from Lara. Like, they're like, look, we build, you know, what's ahead of the models and we're willing to throw everything out every three months, you know, as the models get better and better.

Exactly. Yeah. But the thing you at least have there is you have. Uh, you have an end customer, right? That's like decently sticky. Um, you know, they will mostly stick, you know, they'll, they'll give you a shot at least of, of building these things. What I've always found more challenging, uh, at, at the kind of like, you know, reinvent yourself every three months of the infrastructure layer, it's like, you know, developers are definitely a, a pickier audience maybe than an accounting firm or, uh, you know, a bank.

Yeah. And so it's definitely a, a, a more challenging position to be in to, to have to constantly reinvent yourself.

[00:05:17] **swyx** : Yeah. Yeah. Yeah. And, and like when they turn, it's like. Very complete. Like, they'll leave to like the, the hot new thing, uh, because there's like no defensibility, I guess. Like e even, even if you are a database, like, uh, people can migrate workloads off databases.

Like it's, it's a, it's a known thing. Uh, so I think like basically what we're talking about is the vertical versus horizontal, uh, debate in, in AI startups. And uh, the way I think about it also is just that like when you are. Um, Lara, when you are a bridge, like you are the outsource AI team, right? You, you are, your job is to apply whatever state ofthe art AI methods.

[00:05:55] **Jacob Effron** : Yeah. Like this translation layer between model capabilities and your

[00:05:57] **swyx** : own customers. Yeah. To, to the end customers and like, well, if they didn't have you, they would've to hire in house and they're not gonna hire in house so they have you. And like, I think that's like a reasonable, like very robust to any whatever trends and, and discoveries that people make in, in the engineering layer.

I do think like there is, um. It like sort of useful horizontal companies being built, but they're all. Very much like, sort of like the reinventions of classic cloud in the AI era and the, the primary one being sandboxes. Yeah. Um, which like, it's another form of compute guys, like, let's not get too excited about it.

But I mean, like the, the workloads are enormous.

[00:06:38] **Jacob Effron** : Right.

[00:06:38] **swyx** : Yeah.

[00:06:39] **Jacob Effron** : It's interesting, and I feel like as, as part of this, you know, the questions that folks are asking around infrastructure, there's a lot around, you know, the extent to which companies should have their own AI teams and what they should be doing in-house.

And, you know, uh, I think there's questions around should people be training their own models? Should people be doing, you know, rl, uh, in-house based on the data they have? I feel like, you know, one has to evolve their takes on this every, every three months with paces. But where, where are you at on this today?

[00:07:00] **swyx** : I think, well, I mean actually all models have gone up. Um, and obviously I'm involved in cognition and also cursors doing, doing, uh, a lot of own model training. And I think that that is some part of the, what I've been calling the agent lab playbook, where you start off with the state of the art models from, uh, from the big labs and you, uh, specialize for your domain.

But once you have enough workload and enough high quality data from your users, then you can obviously train your own models and like save a lot on cost and latency and all that, all that good stuff. Um, you also get like a marketing bonus of like calling it some fancy name and putting out some research

[00:07:38] **Jacob Effron** : from my seat.

I can't tell how much of it is like actual, you know, value that's provided to the end user. And how much of it is that marketing bonus? Right. It seems some combination of the

[00:07:45] **swyx** : I think it's both.

[00:07:46] **Jacob Effron** : Yeah.

[00:07:46] **swyx** : Um, no, no. There, there actually is real value. Um, and you, you know that for a number of reasons. Like one, even when it's not subsidized, people do choose it as like one of the top four or five.

This is both composer two and, uh, suite 1.6 I one of the top five models. Like in a, in a fair market? In a free market, yeah. In a, in a, in a model switch. Or people do choose it and like, it's not subsidized. Like, so that's as good as it gets. Uh, but beyond that, like domain specific models, for example. For search with, with both, which both companies have absolutely makes, makes a ton of sense.

Everyone says like, yeah, we should always, always do this. And honestly like, I think the infrastructure for that is becoming easier with, um, like thinking machines tinker thing as well as primary like, uh, lab stuff. Yeah, I mean like, this is one of those like reversal of the, the bitter lesson where you first bootstrap on the large models and the general purpose models to get big.

And as you get very well-defined workloads that are just high quantity but not high variance, um, then you just distill down to a smaller model and run that on your own. Right. Which like totally makes sense.

[00:08:50] **Jacob Effron** : What I'm less clear on is the kind of DIY RL use case, which I think is really mostly around, you know, improved, uh, quality for, for different things.

Obviously there's probably like more efficient ways to, you know, get a smaller model that's that's faster and cheaper. And it'll be interesting to see whether. You know, obviously you had, you know, uh, two, three years ago this whole case of companies that were, you know, pre-training and claiming better outcomes in, in their domains than getting kind of cooked as each model iteration improved.

You know, I wonder whether that's a, a similar story plays out in the, uh, in, in the, our all space. Yeah, for the focus on, on on pure outcomes and quality, not the cost side, which clearly your own models for cost at scale makes a ton of sense.

[00:09:28] **swyx** : I think there are this, there are two sides of the same coin.

Like you basically always want to hold, uh, quality constant or trade off a little bit of quality for a drastic decreasing cost. And that's true for everyone. Uh, one element I wanted to bring out, which is very much in favor of open models, is custom chips. So this would be cereus, but also talu. And then there's a huge range of stuff in between.

This has been a huge story this past year on just like everything non Nvidia is getting bid up, including like freaking MatX is working for, which is very, which is very rewarding for me, but I think one of those things where like, oh, like the suddenly, because the number of alternative. Hard, uh, hardware is increasing and the inference that you can get is insanely high.

Like, um, we're talking thousands of tokens per second instead of less than a hundred. So the trade off for qua quality doesn't hold as much anymore because the speed is so high.

[00:10:24] **Jacob Effron** : Have you seen a lot of companies go all in on the alternative chip?

[00:10:26] **swyx** : So cognition has Yeah. On Cerebras, uh, and, and so has OpenAI

Um, uh, and so no, I don't think so beyond that, uh, and that, do you think that's like a, that's mostly, that's foreshadowing of, that's, yeah. I used to be kind of a skeptic in terms of like, okay, so what if I get my inference at a hundred to a hundred tokens per second sped up to 200 tokens per second. It's only two X faster.

It's not that big a deal. Um, but when you, uh, I think every 10 x does unlock a different usage pattern. Um, and you, we have proof in Talas and, and some of the others. That you can actually, um, drastically imp improve inference speed and what happens from there? I don't even really know, like it's, it's so hard to predict when entire applications just appear at once.

Yeah. Uh, and it also isn't that expensive, right? So like, um, this is one of those things where like, I, I think the, the investment cycle is gonna be multi-year. Um, and I. Would caution people to not dismiss it too, too quickly.

[00:11:25] **Jacob Effron** : Yeah. I mean, one other like infra question I was curious to get your thoughts on is obviously it seems increasingly a lot of the cutting edge infra companies are building for agents as the buyers of their product or users of their product, right?

[00:11:35] **swyx** : Ooh,

[00:11:36] **Jacob Effron** : and

[00:11:37] **swyx** : another huge theme. Yeah. Yeah.

[00:11:38] **Jacob Effron** : And I'm trying to figure out like what. What, what do you have to do differently about selling into agents? Um, are they just the ultimate rational developers? Uh, or is there, you know,

[00:11:46] **swyx** : no, absolutely not. Um, I think they are easily prompt, injected and, uh, very tuned towards like, basically com compounding existing winners.

[00:11:57] **Jacob Effron** : Yeah,

[00:11:57] **swyx** : so like if, like, congrats if you won the lottery for getting into the training data right before 2023, because now you're like installed in there for the foreseeable future. But yeah. Uh, you know, one stat that Versal, uh, CTO Malta dropped at my conference was that there are now, uh, 60% of traffic to Elle's, um, like app arch, like admin app architecture for like configuring versal applications, uh, is bought.

It's not, it's not human. Uh, so like your primary customer is agents now. Um, and it's mostly co like mostly coding agents, mostly people using CLI on CP or whatever. But yeah, I mean, I think. More. I, I think step one, if it doesn't exist as an API that agents can use, it doesn't exist. Right, right. Which I think is like, uh, it's a good hygiene thing anyway, to, to make everything API available, but not as like an extra, um.

Push on like products, people to not only work on the ui, um, you should probably work on the on SCLI stuff. Beyond that, I think honestly there is like, so I, I come from the sensibility of, I think everything that you are trying to do for agents experience now, which is the term that Matt Bowman and Nullify is trying to coin, is the same thing that you should have been doing for developer experience.

That you should have had good docs, you should have had a consistent API, uh, that is. Mostly stateless. Um, you should have, I guess, discoverable or progressive disclosure or like search or like whatever. And so now that people have energy in like finding these customers to do that, that's great. Um, do I believe in.

Extending beyond that into something like a EO, um, for gaming The chatbots? Not necessarily, but obviously there's gonna be huge advantages when people who figure out the short term wins. Yeah. And short term wins can compound.

[00:13:43] **Jacob Effron** : Do you think these compounding advantages to like the, the pre-training data cutoff companies, like, you know, obviously over some period of time, I imagine that doesn't persist.

And so as you think about like. I dunno, three, four years from now what the, you know, selection criteria end up being. Do you think it still mirrors exactly what you were saying before? Like it's exactly what you should have been doing all along to sell a good product to developers?

[00:14:01] **swyx** : It could be, except that I think in three, four years we'll probably have much better memory and personalization.

So then general a EO or GEO doesn't really matter as much. So I think whatever memory or personalization system we end up with will probably d determine what you end up choosing much more. Than, than what is currently the case, which is just frequency of mentions, let's call it. Yeah,

[00:14:26] **Jacob Effron** : yeah.

[00:14:26] **swyx** : Uh, so you just spa quantity and I think that's, I mean, that's something I'm looking forward to.

I do think, like, like, you know, I, I think that the fundamental exercise to work through for yourself is if you start a new, um, sort of. Uh, disruptor company. Now there's a, there's a big incumbent that everyone knows, like, like superb base. Super base is like, kind of like the Postgres, like database, uh, incumbent.

If you wanna start like new superb base, how would you compete with them? And I don't necessarily have the answer, but I, I, I do think like people, like resend like relatively new. I think they would start like 20, 23 and still there was, there was a recent survey where like, people. Checked what Claude recommends by default.

If you just don't prompt it with anything, just say, gimme an email provider and says, resent as in like 70, 70% of each cases. Like the fact that you can get in there with like such a relatively short existence, I think is, is encouraging.

[00:15:14] **Jacob Effron** : Yeah.

[00:15:14] **swyx** : I do think like. Um, you do want to do whatever it is to, to like to, to get in that Very short mentions this because, um, it's not gonna be 20 of them, it's gonna be like three.

[00:15:26] **Jacob Effron** : No, definitely. It feels like, uh, you know, probably more, more consolidation than ever. Uh, or, or kind of like, you know, uh, a winner take most market than maybe the, the, the physics of go-to market in the past. Yeah. Might have, uh, enabled.

[00:15:38] **swyx** : The other thing also is like, semantic association is gonna be very important, uh, in the sense that like, you want to do like the combo articles where you're like, use my thing with for sale, with blah, blah.

And like that all gets picked up in a, in a corpus. And so that's. Probably one thing that you, you wanna do? Well, I don't know what else. Uh, it's, it's, it's, it's one of those things where like, I think I feel, I feel I'm behind, uh, I don't know how you feel about this, but like,

[00:16:04] **Jacob Effron** : I think AI is just everyone constantly feeling like they're behind some, uh,

[00:16:08] **swyx** : yeah.

With,

[00:16:09] **Jacob Effron** : I wanna meet the person that doesn't feel behind,

[00:16:11] **swyx** : but like with, with ax, right? Like, so, so like, my, my stance was that exactly what I said before, like everything that you, that you should do for agents is something that you should have done for humans anyway. Yeah. And so. To the extent that you're just getting it more energy to, to do things for agents, great.

But like, uh, it's hard to articulate what new thing apart from just like more spam, um, that you should be doing. Anyway, that would be my take right now. Um, I I, I do think like there, there will be more turns at this. I think the personalization turn that is coming, um, will be big. And I don't know what that looks like because like basically we're kind of, we feel kind of tapped out on the memory side of things.

[00:16:49] **Jacob Effron** : Yeah. I, I guess since we last chatted, you know, you, you took this role over at cognition, um, and you've obviously have a, have a front row seat to the AI coding space today. You know, I feel like coding in many ways. You know, people view it as this, like, I mean, besides being like the, the mother of all markets and this massive opportunity, I think it's kinda a preview of like, what's to come for many other spaces.

Both. Yeah. You know, I feel like agents are most advanced in coding. I also feel like the, you know, competition between foundation models and application companies, you know, and, uh, mirrors what we may see in other spaces. And so maybe for our listeners, can you just lay out like what is the state of the AI coding wars today?

[00:17:25] **swyx** : Um, it is massive, right? Like, uh, and I don't think necessarily, last time we talked about this, we appreciated the size of what

[00:17:32] **Jacob Effron** : No, I wish we did.

[00:17:33] **swyx** : I state of AI coding wars today, um, both opening eye philanthropic have made it their p serials to competing coding. Um, and. Tropic is like 2.5 billion in a RR just from Cloud Code.

The way they recognize a RR is. Opt for debate, uh, open ai. I don't think the, a public number is known, but let's call it 2 billion as well. And then cursor is like, rumored to be 2 billion, you know? And, and those, those are like the public numbers that are known? Yeah. Um, so like huge markets that have just been created in the past one year.

Like, like anthropic, just like Claude Code just recently celebrated their one year anniversary, which is, yeah, pretty nice. Um, so, and then I think, like the other thing that I see is there's, there's some other people who are like, oh, here's like the, the sort of relative penetration of, uh, Claude use cases, right?

Like, and it's like coding 50% and then legal, whatever. Health, uh, it's like the, the remaining ones. And there was a very popular tweet that was like, okay, I'll look at the, the empty space and all these other use cases. If you are a new founder today, you should be betting on the other stuff because on, on a sort of catch up Yeah.

Theory and my. Consider my, my pushback is the same pushback that, uh, I had on app over Google, which is like, well, well why is this time different? Like, why, if it went from let's say 10 to 50% in the past year, why can't I keep going? Uh, and like getting that wrong is actually a very painful one because you could have just did, did the momentum bet.

Instead of the mean reversion bed. So I, I, I think that that is the, the state of things now that people are very, very much into psychosis. Um, they're are getting rewarded for spending more rather than spending less. And I think we're not in that phase of efficiency. We're in a phase of sort of like capability exploration.

So I think people who are more crazy, who are more. Uh, creative, um, get rewarded comparatively. Yeah.

[00:19:27] **Jacob Effron** : Well, it's interesting. I mean, it feels like behind these like token maxing, leaderboards and whatnot is this, it's like the first phase of this transition from a workforce perspective is you just gotta show your employer like, Hey, I, I use these tools.

[00:19:37] **swyx** : Here's my nu number of tokens I cost, and that's it. They don't care about the quality. Right. It is, uh, maybe distasteful to someone who cares about the craft and, and all that. Um, but directionally everyone just wants you to go up regardless. And so, um, there it is not very discerning. It's, and it's probably very sloppy, but I think it's net fine because we're still probably underusing ai just in generally.

Yeah. Um, and so I think that's like very interesting. Like we had on the podcast, uh, Ryan La Poplar from OBI, who spends a billion tokens a day. Yeah. Um, and that's for those county home, it's like something like 10,000 worth, $10,000 worth a day of API tokens. If they, they did market rates, um, and like most of us can't afford that.

Yeah. But like. And, and, and probably a lot of what he does is slop.

[00:20:25] **Jacob Effron** : Right.

[00:20:25] **swyx** : But like, he's going to dis, he's like, if there were a new capability, he would discover it first before you because he was, he was trying and you were not trying. Right. And like, you only do things that work like, well, good for you.

But like the, the people who are going to discover the next hot thing are living at the edge.

[00:20:42] **Jacob Effron** : Right and increase in living at the edge of just having the compute budget to like run these experiments. I mean, kind of similar to what living at the edge on the research side has always been. You know, it was constrained in many ways by the amount of compute you had to run these experiments.

It feels similarly on the, almost on the builder or like actualizing these tools now.

[00:20:56] **swyx** : Yeah. The other thing that's, I mean, very obvious is philanthropic is kind of like the high price premium player. Um, that where, you know. Restricting limits or restricting model releases even is like the name of the game.

Whereas Codex is like, come on in guys, use our SDK, use our login and we don't care. We're gonna reset limits. Whatever you do want to try to exploit the subsidies where you can get it. And definitely Codex is super subsidized right now. Gemini also very subsidized. Um, and. Comparatively, like, I think you should make, Hey, I guess while, while that's going on, it's not that bad to be a capabilities explorer on just the $200 a month plan from Cloud Code or from OpenAI.

Um, and, uh, I I, I, my sense is that people aren't even there yet.

[00:21:41] **Jacob Effron** : How do you think this, like, market ultimately plays? I mean, it's obviously such a big market that, you know, any slice of that market is interesting for, for anyone going after it. But I think what, what makes people so interesting in the coding market particularly is it feels like it's kind of this.

Foreshadowing of what will happen in other, you know, any other kind of application market that the foundation models eventually turn to and are all their models against and gather data around. And so how do you think, you know, like does there end up being room for lots of different kinds of players or like, what do you think the end state of this market is and is that, do you think that's applicable to other markets?

[00:22:10] **swyx** : I feel like there will be, I mean. Status quo is probably the most likely outcome, which is there are two big players and there's a small range of longer tail people that, um, fit other use cases that the, the two big players don't. That feels right to me. I think that, um, for it to, for the market structure to, to significantly change there would be, there needs to be significant change in like the economics or like the, the brand building or like the, the, the, the value propositions of the, of the companies involved and I.

Haven't seen any in the last six months that, that have really changed the stories materially. So I feel like they would just keep going until something, something else happens. Something else happens, meaning like Microsoft wakes up and like goes like. Guys, we have GitHub, we have, uh, you know, we, we, we'll, we'll do something much bigger here than other, other than just copilot.

Um, and, uh, that would be a big change. Um, MSL has put out a model now, and I was in a breakfast with, uh, Alex Wang, where they were like, yeah, like, we, we really, really want to go after the coding use case. We haven't done anything yet, but like, don't underestimate them. Right. Um, and, and similarly for the Chinese labs.

Um, I think they're trying to go after it. Like ZAI is doing stuff. GLM uh, ZI and GLM is same thing. Um, uh, and, and so it's, so like everyone's trying to get a piece of that pie. I, I feel like the, the status quo has been pretty stable for the past, like almost a year I'll say.

[00:23:39] **Jacob Effron** : Yeah. And is the room for the, not like, you know, for, for the application companies more on like the enterprise side or like where do the, where do the, like what surface area do the model companies leave for application companies?

[00:23:50] **swyx** : Yeah, that's a good one. Um. It's very much evolving. Um, it, I, I, I will say because opening I did not have this, the, this level of attention on coding. Yeah. Uh, a year ago. We just don't have that much history. Right. Um, and it seems like, for example, so the big push at Open I now is the Super app. Um, is that a consumer thing?

Is that like a products like. Portfolio rationalization thing, how much is that gonna take away attention from coding at the time when they actually do want to put more coding? I think it's, it's very unclear. So I do think like there's, there's all these, like in both big labs, there's. Uh, sorry. Both of the, and, and drop and, and deep minus and XAI are are separate cases.

Um, they are trying to see the other time expansion areas. So cloud code for finance. Yeah. Um, uh, cloud cowork, all those, all those things. Whereas I think cursor and cognition are like comparatively just focused on coding and so I, I do think they leave space and I do think for the other verticals that also means the same thing.

Right. That, uh, that they're not gonna be that. Um, intensely focused on, on, on that domain. Except for, I, I think I would mark out finance and healthcare as like the next ones, um, that they're clearly going after. Uh, I, I would say comparatively, healthcare seems more thorny. There, there, there've been some announcements about it, but like, I would respect the, the finance work a lot more just because like the, the path to money is a lot clearer.

[00:25:12] **Jacob Effron** : Yeah, no, I mean, obviously like, I, I think, you know, maybe similar to, to the space that's being left in these other domains, you know, there's obviously. Uh, a lot that's required to actually implement these tools in enterprises, uh, versus, you know, maybe just giving them, uh, giving model access to, to folks outta the box.

[00:25:27] **swyx** : Yeah, yeah. Yeah. So the, the agent lab thing is like, we'll do the last mile for you. Whereas I think the model labs tend to just trust the model and, and be minimalist about it. Both of them work.

[00:25:38] **Jacob Effron** : Yeah.

[00:25:38] **swyx** : I, I don't, I don't necessarily think one, uh, beats the other, uh, for every, for every use case. Um, all I, all I do know is that it does seem like.

Uh, the large enterprises do want a dedicated partner that isn't just the model labs, which is kind of interesting.

[00:25:55] **Jacob Effron** : We, we've been in this phase of, of pure capability exploration. And so I think nothing has been, you know, better for the large labs, right? I mean, they're always gonna be, uh, uh, the frontier of, of capability exploration.

And so I think have a very good relationship with a lot of these enterprises. But ultimately over time, like. The, uh, the incentive structure of these labs is always gonna be maximal, you know, token consumption for, uh, for the end customers they work with. And there's just, I think, so few companies that have actually gotten to massive scale.

Maybe coding again is the most interesting. So it's the first space that really is just completely gone, you know? Yeah. You must love it every day. Like absolutely insane. And. I think it

[00:26:32] **swyx** : gets even. Okay. I mean, like, I think we, we say good things about crystal cognition, but the sheer liftoff of like both end UPIC and open ai.

'cause they, they, they have independent valuations. I mean, let's throw an XEI in there because it's now I ping at 1.2 trillion. That number is just mind boggling. Like I, I feel like in normal investing or normal startups, there's kind of like a ceiling market cap or valuation. Totally. That, that like you, you reach and you go like, all right, let's, it's gonna be chiller from now on.

And these guys are not slow down. No.

[00:27:02] **Jacob Effron** : Well, I also think the dynamic is fascinating about some of these later stage companies is, is, you know, in the past, I feel like in, in venture world, if you got to a certain level of scale, the question around you was really more a valuation question. And this is like why there was different phase, like, you know, types of venture people did and like the late stage growth people were just incredible at like, you know, a little bit of what's the ultimate market opportunity of this company, but also what's the right way to, to value it.

Like we know it's, it's in some bands of an outcome that is like. Sure there's some variance to it, but it's like relatively understood what that bands is and then maybe you get over time surprised to the upside. Whereas any kind of like later, even the labs themselves, any later stage company, the bands of which that company might be worth right now, even in a year or two years are so massive because of how fast the ecosystem changes that it's like.

Even for later stage companies, every three months could be an existential level event to the upside to the downside. Yeah. Um, and I think that, like, you are obviously seeing it in the, in the positive with code, which, you know, if you think about a company like philanthropic, you know, that. For a while, it was like unclear if they were going to have access to enough capital, um, to really stay in the, in the race, right?

And then coding hit at the exact right time. They had the perfect model for it. They executed brilliantly. Um, and you know, now are, are, you know, uh, you know, one of the most valuable companies in the world.

[00:28:13] **swyx** : Uh, at the same time, I, I don't find, I, I have zero sympathy for opening eye because they're crushing it and they're all rich.

You know, this is like a high class champagne problem to have to, uh, to be number two at coding or whatever. Like, who cares? Like, you're, you're doing great.

[00:28:27] **Jacob Effron** : Yeah. It's funny though. I can't even, I mean, you would be closer to this, uh, you know, even that you're in the AI coding space, but it's like a lot of people I talk to think Codex is just as good, if not better than Claude Code.

Right. I think one thing that I've been really surprised by, and maybe, maybe Cloud Code is a better product in some ways, I'm curious your thoughts is just in consumer AI with chat GBT. You saw this big first mover advantage, right? Where admittedly today, like, I don't know, Claude Gemini. Great products.

Not sure, not abundantly clear chat GBTs any better, but like. People stick with chat, GBT, it's the first thing to introduce them.

[00:28:56] **swyx** : They stay, but they're not growing anymore. I don't know if you've seen

[00:28:59] **Jacob Effron** : Right. But that to me is more of like a, a, a product problem than it is. They're not like, it's not like they've like lost share to someone else.

My understanding is the overall problem with consumer AI today is much more of a how do you take this tool and, you know, for, for folks like us, like knowledge workers, it's like this incredible magic tool, but it's not necessarily a daily active use tool for a lot of people around the world today. And what are the like products?

It's, it's kind of a category wide problem. Like in coding, for example, like. The entire space has gone parabolic. There may be some relative growth in, uh, in other consumer AI players, but it's not like consumer AI as a category is like going parabolic and they're not capturing most of that thing. I think it's actually the larger problem is much more, hey, the category has kind of hit a bit of a plateau of people haven't figured out how to bring, you know, tons more users on board.

Yeah, yeah. Or increase the frequency of those users. And so it seems more of a category wide problem than it is, you know, a massive market share of change. I was gonna draw the comparison to, to the coding space where Claude Co is the first product, obviously, to introduce people to this magical experience.

You know, by all accounts, codex is, is pretty damn close to as good, if not better. Um, but like still that first product, you, you would've thought that would not be a super sticky, uh, you know, product surface area. And it actually has, it turns out, I, it feels like the first lab to introduce you and experience really does, uh, keep a lot of, uh, a lot of the focus.

[00:30:12] **swyx** : I, I think. M maybe it's like still, still early days. You know, Chad, BT is like three plus years old and Yeah. Cloud code is only one. Just turned a year. Yeah. So give it time, you know? Yeah. Like, yeah. I mean, definitely sometimes a lot of people have switched from to Codex. Maybe that will keep going. I, it's like really hard to tell.

Uh, yeah. I, I, I do, I do think that. Because we are in this like, high volatility, high temperature phase. Um, the loyalty and stickiness to first movers and category creators, I don't think is as high as it might be in some other, uh, areas in our careers that we've looked at.

[00:30:47] **Jacob Effron** : Yeah. Though, I mean, I've been surprised by the cloud code thing.

I, I would've thought that, like, in many ways I always worried about the

[00:30:52] **swyx** : enterprise. You think you would've been gone by now?

[00:30:53] **Jacob Effron** : Not gone. But I would've, I I always worried that the, that the consumer business of these companies would be quite sticky. And then the enterprise API business. Uh, was actually like, you know, in some ways like your least loyal buyers, like they would, they would move to,

[00:31:05] **swyx** : right, right.

But, but they worked out that it wasn't the enterprise API it was enterprise product.

[00:31:09] **Jacob Effron** : Totally. And maybe that was the, that was the secret that like, but the amount of lock-in or just default behavior that has happened in that space, uh, is, is more than I might've imagined with two products that by all accounts are pretty damn similar.

Yeah.

[00:31:22] **swyx** : No fight there. Uh, I will say I do think that Codex is still in like a catch up. Like in terms of personal experience. Um, the only thing I like out of, out of Codex is the, is like Spark and like yeah. Uh, the, I, I feel like the skills integration is a little bit better. I feel like, uh, the, the speed is a bit better.

Maybe 'cause it's in, is written in rust or whatever. Um, very minor things that you like. Almost like telling yourself rather than like objectively assessing between two, two of them. I, I, I do think, like vibes wise, I think that's going on. Um, the, the, you know, I, I feel like the, the missing questions, uh, in, in this whole debate is like, why is this so concentrated in only two names, right?

Yeah. Like, um, how, where, like, where is the Gemini? You know, presence, where's the Xai presence? Um, and like they are trying, it's just they haven't made that much progress yet.

[00:32:12] **Jacob Effron** : But what the, what the Claude Co moment does show, and it actually in some ways makes you a little more bullish on the potential for someone else to catch up because it does feel like if you're the first person to introduce some magical net new product experience, that that actually might be stickier than one might have imagined.

[00:32:27] **swyx** : Right, right, right. Okay. Yeah.

[00:32:28] **Jacob Effron** : And so it's, everyone can believe they have shot

[00:32:29] **swyx** : that. What do you think that new product experience might be like? I, I, it's, it's like, and this is a failure of imagination on my part. Like, I always wonder, like, people always say this like, well, the, the thing that will save us is like being first to the next new thing.

Like what is it?

[00:32:41] **Jacob Effron** : Yeah.

[00:32:42] **swyx** : It's like,

[00:32:45] **Jacob Effron** : I dunno, something around like, uh, consumer agent, computer use, like hybrid. I think, obviously, I think we're like scratching the surface on the consumer side.

[00:32:53] **swyx** : So my, my current theory is like the. Open claw is like a vision of things to come.

[00:32:58] **Jacob Effron** : Totally.

[00:32:58] **swyx** : Um, and uh, it's good that O open I has like the association with open claw, but by no means do they have the rights to win it.

The general thesis that I have been pursuing now is that the year the same way that 2025 was the year of coding agents, 2026 is coding agents breaking containment to do everything else. Um, and so coding agents continue to still win, but because they generate software and software eats the world, so like, it's kind of like the trans.

Associated property of like software, eat the world, coding agents, eat software, therefore coding agents eat the world. Um, which is like an interesting,

[00:33:30] **Jacob Effron** : yeah, and breaking containment always an easier phase phrase in the consumer context than the enterprise one. You've seen people run these really cool, uh, experiments in their own personal lives.

I think like,

[00:33:37] **swyx** : yes.

[00:33:38] **Jacob Effron** : Figuring out, you know, how you, obviously everyone's focused, you know, on the enterprise side now around how you create these experiences. I feel like the vibes, you know, people love to have these narratives of like, everything is completely shifted. It's like I actually, you know, open AI.

Organizationally, uh, you know, volatility aside is, you know, great products, great team, great models like everyone else in the world is incentivized for there to be. Two, three more. Everyone would love more like great model companies. And so I feel like the, the natural forces of the world revolt when any one company, you know, is too much the star of the show, right?

There's so many people in the ecosystem that are incentivized for that not to happen. And so I think I'd be shocked if we don't have. Uh, uh, reversion of vibes, not maybe completely the other way, but at least a little bit more equal at some point over the next six, 12 months.

[00:34:24] **swyx** : I, I think there's just a kind of different stages when, when you talk about the world, one wanting more model companies, I talked think about like the neo labs.

[00:34:30] **Jacob Effron** : Yeah.

[00:34:31] **swyx** : And I mean, I don't know, is it fair to say none of them have really broken through in the past year?

[00:34:35] **Jacob Effron** : I think that's totally fair,

[00:34:37] **swyx** : which is rough. Um, and well, how are we gonna, how are we gonna grow that diversity in, in, in choice, like. Um, that's, this is it.

[00:34:46] **Jacob Effron** : Yeah. It'll be really interesting to see what, what, what ends up happening with that.

And you've seen, you know, folks like Nvidia, you know, very incentivized to make sure there's, there's a broader platform of, of other model providers.

[00:34:57] **swyx** : I think, uh, I don't know people say this, but I, I, I don't think they try it hard. Nvidia tries harder to build neo clouds

[00:35:05] **Jacob Effron** : Yeah.

[00:35:06] **swyx** : Than neo labs.

[00:35:07] **Jacob Effron** : Well, they try pretty damn hard to build neo Cloud, so

[00:35:09] **swyx** : that's,

[00:35:09] **Jacob Effron** : yeah.

[00:35:10] **swyx** : But like, you know, let's call it like the, the core weaves of the world, much happier place in the, you know, than any neo lab built on top of them.

[00:35:18] **Jacob Effron** : Yeah. That one might argue it's, it's easier to, to enable a neo cloud to be successful than it is. Uh, you can't will a neo lab into existence the same way you, so

Nvidia

[00:35:25] **swyx** : has more direct control over it.

Uh, for sure.

[00:35:27] **Jacob Effron** : What else is kind of catching your eye today on the startup side? I mean, you worry, there's obviously this whole narrative of like, you know, the foundation models, you know, they announced a product and every stock goes down 15%. Like

[00:35:36] **swyx** : Yeah.

[00:35:37] **Jacob Effron** : Do you, do you worry about the foundation models just kind of eating into to a bunch of these startup categories?

[00:35:43] **swyx** : Not really. I, I think actually like. As, uh, there's, there's, okay, there's, there's, there's the, there's the point of view of like being an investor in startups, and there's a point of view of like, do you wanna start something? And I think honestly, like the, the downside for all these is so. Minimal in, in a sense of like, the worst you do is you just get hired into one of these labs anyway.

So I, I think the, the market for people who just do things and try things and try to execute in like a competent way, even if like it doesn't work out commercially, even if it just wasn't that great anyway. Like, but like that's your job interview to go into, into one of these things anyway, so, um, I don't feel that.

From a, from a very, very small startup perspective, mid-size startups. Yes. Uh, I will say there's been a lot of dead, um, LM Infra, a lot of LM infra consolidation like the, the, uh, lang fuses of the world getting absorbed into, into click house. And I, I think. Like people have maybe worked out the domain specific playbook, uh, and like, I think that's okay.

Um, and, and yeah, I'm not that, not that worried about, uh, okay. So, um, I, I would say I'd be more worried about traditional SaaS, like low NPSS. This is the whole AI versus SaaS debate that has, that's been going on. Uh, and, and like literally I'm going through that exact thing in my company where, so I like kind of.

Thinking through this on a very visceral, visceral level, right? On one hand you have the people who say you vibe coders don't appreciate the amount of work that goes into A-A-C-R-M and like, yeah, you think you can rip out Salesforce? So did the 30 entrepreneurs before you, right? Like, like, you know, you classically underestimate the things that you don't.

Deeply, no. And, and, and target audience is not you. Uh, at the same time, like we have never been able to build software so easily and customize software so easily and like Yeah, you're not gonna use 90% of the things in Salesforce. So like, yeah. What's the typical, so what have you, what

[00:37:33] **Jacob Effron** : have you done internally?

[00:37:34] **swyx** : So we have there the main SaaS that we do for event management and sponsor management. That's, and we paid 200 KA year for that. Not, not huge, but like chunky for, for, for my, my scale. Um, and like, yeah, I could probably spend 2000 and, and build like a custom version of that. Um, the, the, the trick has been dealing with my, the rest of my team and getting them on board.

Yeah. 'cause I'm the most ethical person on my team, but like, I can't make that decision myself. And I think in the same way I've been telling with other CEOs team leaders as well, it's like, well you can be super cloud pilled. You can be super LM psychosis and that you think that's okay, but you like you have to bring your team with you.

And I think like there, the sort of widening disparity in LM psychosis in companies is causing real s real riffs because. And on one hand, on one hand, the people who are less AI native are not getting with the picture. They're not, they're actually like behind, they're actually not waking up to the fact that like you, everything you think is necessary is not actually that necessary.

And in fact, exactly would be better of you if you just like held your nose and went in and when came out the other side. Yeah, only talking to agents in natural language and like your life would actually be better and you just, you're just like close-minded. There's that perspective. The other perspective is, oh, you vibe coder.

You, you did this in a weekend and you got the 80% solution and now the rest of your employees. Have to pick up the rest of your shit, right, that you, that you thought you were, you were such hot, amazing, uh, uh, at, but like, actually you didn't figure it out. And like, actually LMS are still useless at this and blah, blah, blah.

So like, I think there's this huge debate going on in every company right now. Um, and like, um, you know, I have a small microcosm of it, but like, yeah, it, it's making me hesitate to, to pull the trigger. But like I will at some point, it's like maybe I've put it off for one year, but not like five. Yeah, but like, so, so like SaaS is definitely getting squeezed.

Um, it does make me wonder, like, I, I do think that there's an opportunity for a more AI native, um, system of record thing that is not just Postgres. Um, or not just MongoDB, although both are very good. Maybe it's like a convex or like people Yeah. Bring up convex a lot. I don't know, like, like, I, I just feel like the sort of quote unquote firebase of, of AI apps isn't really a thing yet.

Um, beyond what we have. Uh, which, which is fine. It's, it's, it's just. We could probably start in a more sort of rapid iteration cycle first before scaling up to like a Postgres or MongoDB, which are more sort of old tech. I was at a dinner with, uh, Mike Krieger, the CPO of en philanthropic, and, and he, we were just kind of going around the room going like, what are people most worried about?

Yeah. And, uh, for me, uh, I, instead of security, I brought up biosafety. Yeah,

[00:40:21] **Jacob Effron** : classic.

[00:40:22] **swyx** : Um, actually, like I said, it was. Cliche and classic, and the rest of the table were, were like, what do you mean? Someone sitting at home can manufacture a virus that wipes out half of humanity,

[00:40:32] **Jacob Effron** : almost like the OG Jeffrey Hinton.

Like, this is why you should be scared.

[00:40:35] **swyx** : I'm like, yeah, like the read the, you know, risk reports. Like this is like the thing. Um, I think, and Mike was just sitting there knowing he was sitting on Mythos and going like, actually it's security. Um, and I think like, um, I think the, there's, there's, part of it is.

A very good marketing. Like too good. Yeah, like I would actually advise and topic to tune down the marketing because also it's, it is just a very good model and you don't have to make so many marketing claims around it. At the same time, it is not really a private model. If you give it to 40 companies.

Each of whom have like 10,000 employees or whatever. Right. It's not, it's not private, it's, it's like there's bad actors in there.

[00:41:18] **Jacob Effron** : Yeah. Hopefully, hopefully not as, uh, as bad as releasing it widely, but, uh, no, I mean, it's an interesting. You know, it's an interesting case study for how all, I mean, many model releases might, I mean, you know, this might be the first model release that looks like the rest of 'em from from now on, right?

[00:41:31] **swyx** : It, it, so it's, it's the, there's an overall product strategy, uh, for anthropic of like bundle, uh, you know, restrict access bundle, uh, product with model maybe.

Whereas, uh, OpenAI has definitely been a lot more sort of. Philosophically aligned on like, we will just enable access everywhere and we don't know what you, what will come out of it. Right.

[00:41:51] **Jacob Effron** : Right. Though, I mean, this current moment, uh, obviously the cynical take is also just ties to the amount of compute that both companies

[00:41:56] **swyx** : Yeah.

Right, right, right. Yeah, I think, I think that's true. I I do think like the, the, this is the, the, the scale, the dawn of like larger than 10 trillion parameter models is very interesting. I don't think it, I think it's a temporary phenomenon because we have much larger compute clusters coming online for everyone over the next like three, five years.

It's, and this is like already written in, in the cards.

[00:42:18] **Jacob Effron** : Yeah.

[00:42:19] **swyx** : So to the extent that like, you know, will we have rationing of models, uh, above 10 trillion, uh, in like two years? I don't think so. I think everyone will have no, we'll just

[00:42:29] **Jacob Effron** : have rationing of the next phase.

[00:42:30] **swyx** : Right. Right. But like, that's as it should be almost like, um.

My, my classic example, which I, this is just me theorizing, not anything confirmed by Google. When Google announced Gemini, they actually announced three sizes, which was Flash Pro Ultra. They never released Ultra. They only have Pro and Flash. Um, so my theory is they have ultra sitting in a basement and they just could distilling from it for, for flashing pro.

Um, which like, yeah, I mean, I, I actually think that's. As it should be for any lab that they, that they do that.

[00:43:02] **Jacob Effron** : Yeah. Just because those are the models that people actually wanna end up using. And it's just like cost prohibit.

[00:43:06] **swyx** : It is more, yeah, it's cost. Yeah. It's, it's not the want, it's just, just, just the cost.

Um, I do think, like, uh, it is interesting that, uh, for a while I was, I was considering the theory that models capped out at two, 2 trillion, and I think that's proving to be wrong. And well then if I'm wrong, how wrong? How wrong am I? Do we do 200 trillion? Do we do two quarter trillion, whatever? Um, and I don't think we have the straight answer to that, but like, uh, it's interesting that we are continuing to scale number of pers when everyone kind of assu like can see that we're not going to get like the next thousand or 1 million x from this paradigm.

So like the others, like the alias of the world are working on other. Um, model architecture improvements. We need a different scaling law, I guess, because like, we're, I, I feel like people already already feel like we're tapped out on this. Like the, the end, the end state of this is we turn most of the world into data centers and like, I don't know.

I don't know if we want that.

[00:44:08] **Jacob Effron** : Yeah, I mean, uh, if the, if, if, if the return of intelligence are there, maybe, uh, maybe not so bad.

[00:44:13] **swyx** : I, I, I think there, there's just a sheer amount of like, like un scalability that like is wrangling people's sensibilities right now. Um, especially in terms of like context lengths.

Um, my classic quote is that context length is like the slowest scaling factor in, in lms.

[00:44:30] **Jacob Effron** : Yeah.

[00:44:30] **swyx** : Um, we, like, we took maybe. Three years to go from like 4,000 context length to a million and that's about it. Yeah. Like Gemini has had a million token context length for two years now. Um, and no one's using it.

Like, so like yeah, it's memory. Memory is probably gonna be the, the biggest limiting constraint on all these things.

[00:44:50] **Jacob Effron** : Yeah. Certainly seems that way. I guess I'm curious over the last year since you recorded last, like what's one thing you've changed your mind on?

[00:44:57] **swyx** : I feel like I was kind of bearish on open models like last year.

Um, in a sense of, like, I, I had just done the podcast with an Al

[00:45:07] **Jacob Effron** : Yeah.

[00:45:08] **swyx** : Of Braintrust where he, and he, I mean, you know, he has a good cross section of all the top AI companies and he says market share of open source is 5% and going down. Um, I think that's changed. I think it's going up. Um, and even if,

[00:45:22] **Jacob Effron** : even though the capability gap does seem to be increasing.

Spending on the

[00:45:26] **swyx** : time. It's hard to tell. Yeah, it's, it's really hard to tell. 'cause like, okay, for, for listeners, capability gap increasing is like on public benchmarks. And let's say you're comparing mythos versus like, I don't know, G-T-O-S-S or like GLM 5.1. And, um, it's, it is really hard to tell. 'cause even if they were closing, you will also not believe that they were closing that much because it's very easy to gain the benchmarks.

Yeah. So you just don't really, really know. Um, all you know is like. Uh, there's somewhat objective open router stats on like what people choose in a free market. And people do choose some of these open models in significant volume, except that a lot of them are heavily discounted. So you need to kind of like price adjust, uh, these things.

So even if, even if that were true, which I, I'm not sure, like I, I, I feel like the numbers just up now instead of down. Uh, I think the. Separation between what the top tier agent labs are doing versus the average startup in ai or the average GPT wrapper is significant enough that you should not worry about the, the, the sort of mean industry number.

And you should, you should cohort things into like, here's the median here, here's like the bottom 80% and here's the top 20%. And top 20% acts very differently than the pome percent. And so top 20% is, which is what I all I care about, um, is. Definitely going towards more open models. Um, the fireworks and the togethers are crushing.

Um, and, uh, and so will all the fine tuners, right? So like, um, I think maybe last time we even said things like, fine tuning is a service doesn't work. Well, now it's gonna work. It's, it's a derivative of the open market, uh, open models market.

[00:47:01] **Jacob Effron** : Well, and also in the workload scaling to the point where people care about cost and speed, you know, more and more.

[00:47:06] **swyx** : Yeah.

[00:47:06] **Jacob Effron** : And that like the, you know, moving from just pure use case discovery of like, what can these models do to, okay, we know what they're gonna do at scale now let's do 'em cheaper and faster.

[00:47:14] **swyx** : Yeah. Yeah. Um, so, so like, uh, that change I, I think, is probably the most significant in, in my mind. And like, I, I always like to do the mental math of like, uh, this is what.

Think about, uh, scheduling a learning rate, like when you've been wrong once. Yeah. What else were you wrong on? Um, and I, I'm kind of working through it. I, I, to me, the, the, the other thing was the coding one, um, which obviously I, I have now come full 360 on, but I think like. People are not appreciating dark factories enough, which I don't know if you've discussed in the pod yet.

[00:47:44] **Jacob Effron** : No.

[00:47:45] **swyx** : Um, uh, and so this is a kind of a strong DM slash Simon Willis term. Uh, the, the general idea is, okay, there's different levels of AI coding psychosis. You can have, um, the, the very first level, which I, I, by the way I encountered first in cognition five months ago was zero. Uh, human written code. Yeah.

Right. Which like, seems like a reasonable thing now was less reasonable five months ago. The next frontier that sounds as crazy today as it as, as zero coding was in in the past is zero Human review.

[00:48:17] **Jacob Effron** : Yeah.

[00:48:18] **swyx** : Like, just, just check it in without even. Reviewing it, and very few people are doing that, but opening Eyes is, is exploring this and I feel like it's, it's definitely the only scalable way to do this.

Uh, which it just means like you have to just kind of like flip the S-S-D-L-C or change large amounts of what, what you normally do. Um. Which is probably things you should have done anyway. More testing, more, you know, more automated verification or whatever. But like that is a frontier at which, like when you have unlocked that in your companies, um, you are just gonna produce much more quantity of software than than you've ever had.

Uh, and it's gonna be like so much, so disposable, so cheap that you can probably innovate in quality a lot as well. Like that that quantity helps you get to quality.

[00:49:00] **Jacob Effron** : Yeah.

[00:49:01] **swyx** : Which I think people are very uncomfortable with. 'cause like people associate more quantity with slop.

[00:49:07] **Jacob Effron** : Right. No, it's back to exactly the discussion we're having on like the reaction to these token maxing scoreboards and the, and the idea that like, today, maybe that's not the most, uh, the, the, the, the best sign of, of, of productivity in efficiency, but going forward

[00:49:18] **swyx** : yeah, you, but you still get rewarded for it.

So they're like, fuck it, whatever. But like, uh, I, I, I think like the, the, the people who are, who are doing well, who do well, who do most well in 2026, are not the cynics who go like, oh, that's just slop. I'm not gonna participate in that. They're like, okay, like this is happening with, with or without me. Bend this the right way.

[00:49:36] **Jacob Effron** : Yeah, no, I love that. Um, I mean, I think for, for me, like any kind of related thing on, on the open source model side is for so long, I really didn't think it made any sense to do any sort of RL post-training, pre-training, anything you could do to like improve kind of overall quality. Certainly for like latency and cost, it always made sense to me.

But for overall quality, like God, you just get that for free in the models like three, six months later. I, I think what I'm starting to change my tune on a little bit is. You know, hearing all these app companies talk about, like, you know, we build stuff and then we throw it out three months later, as, as like the models improve.

You're like, okay, well then what you're doing for capability improvement is just another version of that, right? Like, I still don't think that like your RL or like post train is gonna make you have a better model for like. Years and years to come. But maybe I, I think you still have to be pretty rigorous on like, is that the single best thing you can do to solve a customer problem?

And like, you know, oftentimes, like, it's literally just like now, like add more data and like feed more data even via connectors to these models or like, I don't know, do some clever engineering on the back end or whatever it is. But at the single best thing you can do for that three month time period to improve your customer's outcomes is, you know, post-training in some way that like really improves the output of model even if you throw it out three months later because the general models get up there.

It still might have been worth doing. And so I think I'm like more open to

[00:50:45] **swyx** : you, you throw out the results, but you don't throw out the raw data.

[00:50:47] **Jacob Effron** : Totally.

[00:50:48] **swyx** : And like, so like

[00:50:48] **Jacob Effron** : Right. Then you just run it again. And so basically there's some, obviously at the level of cost of like $10 million, maybe that's too much, but there's some level of cost where

[00:50:55] **swyx** : No,

[00:50:55] **Jacob Effron** : it's the, it's

[00:50:56] **swyx** : not even 10 million,

[00:50:56] **Jacob Effron** : right?

No, of course it's not. Uh, you know,

[00:50:58] **swyx** : yeah.

[00:50:58] **Jacob Effron** : There's obviously some level of investment, uh, at which it's the equivalent of just like staffing four engineers to go build something for three months.

[00:51:04] **swyx** : Yeah. Uh, so the other thing I really, uh, for, for listeners, I'm just gonna leave some, some droplets of info. Uh, look into like the, the long trajectory, the synthetic rubrics work that people are doing is very important, uh, including, uh, something that's called Doctor GRPO.

I'll just, I'll just leave those key search terms in there. Um, I, I think it, what it means is that RL is going much more multi turn than. People think, and that means that you can customize the models in way more specific dimensions than traditional, let's call it SFT, or uh, uh, you know, like a, a sort of shallow rl, um, that was done in a year ago.

Um, so like hundreds of turns.

[00:51:44] **Jacob Effron** : Yeah.

[00:51:45] **swyx** : Uh, and, and, and I think that that leads you down a path of like complete domain specificity.

[00:51:50] **Jacob Effron** : What else? Like are you, you know, uh, of these like unanswered questions in AI today? Are you like looking for, you know, in the next year? Are you, you, uh, you know, paying close attention to,

[00:51:58] **swyx** : I, I have a few thesis for like, what?

Is the sort of next frontier. Uh, one is memory, which memory and personalization we talked about. The other is really, uh, world models, which we've done a small little series on from Fefe Lee. Yeah, of course. To, uh, even Moon Lake. Um, and, uh, general intuition and there's a lot of debate as to like. The relative importance of this.

I think a lot of it, it manifests as like 3D static walls that you kind of inhabit for a little bit and you walk around and they're like, cool, but like, how does this help me with my B2B SaaS? Right. And

[00:52:29] **Jacob Effron** : it's like all the hype now is robotics, right?

[00:52:31] **swyx** : Yeah. Um, and there's a, obviously a correlation between, uh, role models and embodied.

Uh, vision and experiences, which leads to robotics. Uh, but I think role models is very interesting in just in improving intelligence itself. Um, from the next, from the next token prediction paradigm. Um, and so I think people are kind of testing their edges around that. One of our top articles this year so far has been on adversarial award models.

Um. I, I do think, like, uh, if you don't do anything else, just read FE'S essay on spatial intelligence on why, um, LMS don't need, don't have it. And she is, she may, she may not have the solution yet, but she has the right problems statement. Yeah. And so everyone else is trying to solve that problem statement in their own way.

Um. And let's see who wins. But like, I, I don't think it does you any favor to equate role models to robotics or role models to gaming or some kind of like, uh, or like the current manifestations because what is at stake is a much more important. Conception of intelligence than just answering questions.

It is, does, does, does, does the AI understand what a table is? Like, what, what matter is, what physics is? It is almost like for, for those who are movie fans, it's like Google Hunting where, um, Matt Damon like knows everything because he read it in a book, but he's never lived. Great,

[00:53:54] **Jacob Effron** : great scene with

[00:53:55] **swyx** : Robin Williams.

With Robin Williams and I, I look at that scene and I go like, that's exactly the, the, the difference between like a very intelligent LLM who knows everything but hasn't experienced anything.

[00:54:04] **Jacob Effron** : Wow. That's an awesome note to end on. Uh, that's a, have you used that before? That's great.

[00:54:08] **swyx** : Yeah. So, so one thing I've done with Lean Space is I moved to like, uh, adding daily writeups.

Yeah. And so one, one of the times I was doing this daily writeup, I wrote that.

[00:54:16] **Jacob Effron** : That's a great

[00:54:17] **swyx** : one. I love

[00:54:17] **Jacob Effron** : that. Um, well, so it's been a ton of fun. Thanks so much

[00:54:19] **swyx** : for, for Coming Man.

[00:54:21] **Jacob Effron** : I'm Jacob Effron and this has been Unsupervised Learning. A podcast where I get to talk to the smartest people in AI and ask them tons of questions about what's happening with models and what it means for businesses in the world.

As I hope is clear, I have a ton of fun doing this. It's a nights and weekends project in addition to my day job as an investor at RedPoint, but our ability to get these incredible guests on really comes from folks like you subscribing to the podcast, sharing it with friends. It's really what ultimately makes this whole thing work.

And so please consider doing that. And thank you so much for your support and listening. We'll see you next episode.

---

## [[AINews] Tasteful Tokenmaxxing](https://www.latent.space/p/ainews-tasteful-tokenmaxxing)
*🔬 Latent Space | 2026-04-23*

It is Cloud Next today and Google TPUv8's (training and inference iterations) were [announced as expected](https://cloud.google.com/blog/products/compute/tpu-8t-and-tpu-8i-technical-deep-dive), though the numbers are mindboggling, they mostly serve to reinforce the sheer hardware advantage that a decade of investment has given to GDM and any models they train and serve.

Over the last 2 days with **[AIE Miami](https://www.youtube.com/watch?v=6IxSbMhT7v4)** concluding ([Singapore](https://ai.engineer/sg) is next!) the top conversations we have been hearing from AI leadership (CTOs, VPs, Founders) have all centered around the concept of "Tokenmaxxing" and how leaders want to get their teams using more AI, WITHOUT the downside of incentivizing the kinds of horrendous waste our friend  described at [his AIE keynote](https://www.youtube.com/watch?v=CS5Cmz5FssI).

Dex Horthy, coiner of Context Engineering and "the Dumb Zone", [publicly retracted ](https://www.youtube.com/live/6IxSbMhT7v4?si=tMzmqM103KDbPyE6&t=3424)his extremely vibe-coding-pilled call 6 months ago and encouraged people to **please read the code,** citing 's [Z/L continuum from AIE Europe](https://x.com/altryne/status/2046246775414276142)**:**

[](https://substackcdn.com/image/fetch/$s_!4_2l!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fcb2b6f77-150d-4fb4-a74a-259318cba0dd_1698x1172.png)[timestamp](https://www.youtube.com/live/6IxSbMhT7v4?si=tMzmqM103KDbPyE6&t=3424)

Off the record, many senior leaders I talk to are more on [the Zechner side](https://www.youtube.com/watch?v=RjfbvDXpFls) than [the Lopopolo side](https://www.youtube.com/watch?v=am_oeAoUhew&pp=0gcJCcMKAYcqIYzv) of the Z/L spectrum -- this does not mean that one side is true for every one in every situation, nor does it mean it will continue to be true with advancing model progress! To point out the most obvious, engineers and engineering leaders are the ones most setup to make a big deal out of minor architectural quality issues that sheer quantity of cheap code generation and code review _might_ overcome.

Today's LS guest, Mikhail Parakhin, CTO of Shopify, had another take on the "tasteful tokenmaxxing" \- you want to go for depth (e.g. do more serial autoresearch loops) than go for breadth (e.g. solve a problem by kicking off 5, 10, 50, 500 parallel runs of the LLM slot machine). Worth thinking through.

> AI News for 4/21/2026-4/22/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

# **AI Twitter Recap**

**Open Models: Qwen3.6-27B, OpenAI Privacy Filter, and Xiaomi MiMo-V2.5**

  * **Qwen3.6-27B lands as a serious local/open coding model** : [@Alibaba_Qwen](https://x.com/Alibaba_Qwen/status/2046939764428009914) released **Qwen3.6-27B** , a **dense** , **Apache 2.0** model with **thinking + non-thinking modes** and a **unified multimodal checkpoint**. Alibaba claims it beats the much larger **Qwen3.5-397B-A17B** on major coding evals, including **[SWE-bench Verified 77.2 vs 76.2](https://x.com/Alibaba_Qwen/status/2046939775924584577)** , **[SWE-bench Pro 53.5 vs 50.9](https://x.com/Alibaba_Qwen/status/2046939775924584577)** , **Terminal-Bench 2.0 59.3 vs 52.5** , and **SkillsBench 48.2 vs 30.0**. It also supports [native vision-language reasoning over images and video](https://x.com/Alibaba_Qwen/status/2046939788184547610). The ecosystem moved immediately: [vLLM shipped day-0 support](https://x.com/vllm_project/status/2046943674890871019), [Unsloth published 18GB-RAM local GGUFs](https://x.com/UnslothAI/status/2046959757299487029), [ggml added llama.cpp usage](https://x.com/ggerganov/status/2046988075302064209), and [Ollama added a packaged release](https://x.com/ollama/status/2047066252523507916). Early user reports from [@KyleHessling1](https://x.com/KyleHessling1/status/2046986423736451327) and [@simonw](https://x.com/simonw/status/2046995047720378458) were notably strong for local frontend/design and image tasks.

  * **OpenAI quietly open-sources a practical privacy model** : Multiple observers flagged OpenAI's new **[Privacy Filter](https://x.com/ClementDelangue/status/2046973714751754479)** , a lightweight **Apache 2.0** open model for **PII detection and masking**. According to [@altryne](https://x.com/altryne/status/2046977133013311814), [@eliebakouch](https://x.com/eliebakouch/status/2046979020890198503), and [@mervenoyann](https://x.com/mervenoyann/status/2046980302002602473), it is a **1.5B total / 50M active MoE** token-classification model with a **128k context window** , intended for cheap redaction over very large corpora and logs. This is a more operationally interesting release than a generic "small open model": it targets a concrete infra problem in enterprise/agent pipelines where on-device or low-cost preprocessing matters.

  * **Xiaomi pushes agentic open models upward** : [@XiaomiMiMo](https://x.com/XiaomiMiMo/status/2046988157888209365) announced **MiMo-V2.5-Pro** and **MiMo-V2.5**. Xiaomi positions **V2.5-Pro** as a major jump in software engineering and long-horizon agents, citing **SWE-bench Pro 57.2** , **Claw-Eval 63.8** , and **τ 3-Bench 72.9**, with claims of 1,000+ autonomous tool calls. The non-Pro model adds **native omnimodality** and a **1M-token context window**. Arena quickly listed [MiMo-V2.5 in Text/Vision/Code evaluation](https://x.com/arena/status/2047013664142893286), and Hermes/Nous integration followed via [@Teknium](https://x.com/Teknium/status/2047093325774385358).




**Google Cloud Next: TPU v8, Gemini Enterprise Agent Platform, and Workspace Intelligence**

  * **Google 's infra announcements were substantial, not cosmetic**: [@Google](https://x.com/Google/status/2046993420841865508) and [@sundarpichai](https://x.com/sundarpichai/status/2046981627184902378) introduced **8th-gen TPUs** with a split design: **TPU 8t** for training and **TPU 8i** for inference. Google says **8t** delivers nearly **3x compute per pod vs Ironwood** , while **8i** connects **1,152 TPUs per pod** for low-latency inference and high-throughput multi-agent workloads. Commentary from [@scaling01](https://x.com/scaling01/status/2046981511753130461) highlighted an additional claim: Google can now scale to **a million TPUs in a single cluster** with TPU8t. The productization signal matters as much as the raw hardware: Google is clearly aligning chips, models, agent tooling, and enterprise control planes into one vertically integrated offering.

  * **Enterprise agents became a first-class Google product surface** : [@GoogleDeepMind](https://x.com/GoogleDeepMind/status/2046983340524269713) and [@Google](https://x.com/Google/status/2046985650868547851) launched **Gemini Enterprise Agent Platform** , framed as the evolution of Vertex AI into a platform for building, governing, and optimizing agents at scale. It includes **Agent Studio** , access to **200+ models via Model Garden** , and support for Google's current stack including **[Gemini 3.1 Pro](https://x.com/GoogleDeepMind/status/2046983343481270459)**[, ](https://x.com/GoogleDeepMind/status/2046983343481270459)**[Gemini 3.1 Flash Image](https://x.com/GoogleDeepMind/status/2046983343481270459)**[, ](https://x.com/GoogleDeepMind/status/2046983343481270459)**[Lyria 3](https://x.com/GoogleDeepMind/status/2046983343481270459)**[, and ](https://x.com/GoogleDeepMind/status/2046983343481270459)**[Gemma 4](https://x.com/GoogleDeepMind/status/2046983343481270459)**. Related launches included **[Workspace Intelligence](https://x.com/ChanduThota/status/2046946043078848788)**[ GA](https://x.com/ChanduThota/status/2046946043078848788) as a semantic layer over docs/sheets/meetings/mail, [Gemini Enterprise inbox/canvas/reusable skills](https://x.com/Google/status/2046988686433108417), [Agentic Data Cloud](https://x.com/Google/status/2046997032649277754), [security agents with Wiz integration](https://x.com/Google/status/2047000216188940710), and [Gemini Embedding 2 GA](https://x.com/GoogleAIStudio/status/2047007402520674679), a unified embedding model across text, image, video, audio, and documents.




**Agents, Harnesses, Traces, and Team Workflows**

  * **The "agent harness" abstraction is hardening across vendors**: OpenAI introduced **[workspace agents in ChatGPT](https://x.com/OpenAI/status/2047008987665809771)** , shared **Codex-powered** agents for teams that can operate across docs, email, chat, code, and external systems, including [Slack-based workflows and scheduled/background tasks](https://x.com/OpenAI/status/2047008991944069624). Google made a parallel enterprise move with Gemini Enterprise Agent Platform, while [Cursor added Slack invocation for task kick-off and streaming updates](https://x.com/cursor_ai/status/2047000517751288303). The pattern is converging: cloud-hosted agents, shared team context, approvals, and long-running execution rather than single-user chat.

  * **Developer ergonomics around harness/model independence improved** : VS Code/Copilot rolled out [bring-your-own-key/model support across plans](https://x.com/pierceboggan/status/2046985841596354815) and [business/enterprise](https://x.com/GHchangelog/status/2047023899238400491), enabling providers like Anthropic, Gemini, OpenAI, OpenRouter, Azure, Ollama, and local backends. This is strategically important because, as [@omarsar0](https://x.com/omarsar0/status/2047006936306962754) noted, most models still seem overfit to their own agent harnesses. Cognition's [Russell Kaplan](https://x.com/russelljkaplan/status/2047077659985981616) made the complementary business case: enterprise buyers want **model flexibility** and infrastructure that spans the full SDLC, not attachment to one lab.

  * **Traces/evals/self-improvement are becoming the core agent data primitive** : The strongest thread here came from LangChain-adjacent discussion. [@Vtrivedy10](https://x.com/Vtrivedy10/status/2046942634321559707) argued that **traces capture agent errors and inefficiencies** , and that compute should be pointed at understanding traces to generate better evals, skills, and environments; [a longer follow-up](https://x.com/Vtrivedy10/status/2046979341427331522) expanded this into a concrete loop involving trace mining, skills, context engineering, subagents, and online evals. [@ClementDelangue](https://x.com/ClementDelangue/status/2046942871299772441) pushed for **open traces** as the missing data substrate for open agent training, while [@gneubig](https://x.com/gneubig/status/2046963826109689983) promoted **ADP / Agent Data Protocol** standardization. LangChain also teased a stronger testing/evaluation product direction via [@hwchase17](https://x.com/hwchase17/status/2046962351090606404).




**Post-Training, RL, and Inference Systems**

  * **Perplexity and others shared more of the post-training playbook** : [@perplexity_ai](https://x.com/perplexity_ai/status/2047016400292839808) published details on a **search-augmented SFT + RL** pipeline that improves factuality, citation quality, instruction following, and efficiency; they say Qwen-based systems can match or beat GPT-family models on factuality at lower cost. [@AravSrinivas](https://x.com/AravSrinivas/status/2047019688920756504) added that Perplexity now runs a post-trained Qwen-derived model in production that unifies **tool routing and summarization** and is already serving a significant share of traffic. On the research side, [@michaelyli__](https://x.com/michaelyli__/status/2047019938339340602) introduced **Neural Garbage Collection** , using RL to jointly learn reasoning and **KV-cache retention/eviction** without proxy objectives; [@sirbayes](https://x.com/sirbayes/status/2046961503107166689) reported a Bayesian linguistic-belief forecasting agent matching human superforecasters on ForecastBench.

  * **The "minimal editing" problem in coding models got a useful benchmark treatment**: [@nrehiew_](https://x.com/nrehiew_/status/2046963016428872099) presented work on **Over-Editing** , where coding models fix bugs by rewriting too much code. The study constructs minimally corrupted problems and measures excess edits with patch-distance and added **Cognitive Complexity** ; it finds [GPT-5.4 over-edits the most while Opus 4.6 over-edits the least](https://x.com/nrehiew_/status/2046963041338855791), and that [RL outperforms SFT, DPO, and rejection sampling](https://x.com/nrehiew_/status/2046963050427879488) for learning a generalizable minimal-editing style without catastrophic forgetting. This is one of the more practical post-training/eval contributions in the set because it targets a failure mode engineers actually complain about in production code review.

  * **Inference efficiency work remained highly active** : [@cohere](https://x.com/cohere/status/2047052557915476304) integrated **production W4A8 inference into vLLM** , reporting **up to 58% faster TTFT** and **45% faster TPOT** vs W4A16 on Hopper; the details include [per-channel FP8 scale quantization and CUTLASS LUT dequantization](https://x.com/cohere/status/2047052560553681183). [@WentaoGuo7](https://x.com/WentaoGuo7/status/2047007230847766951) reported **SonicMoE** throughput gains on Blackwell--**54% / 35% higher fwd/bwd TFLOPS than DeepGEMM baseline** --while maintaining dense-equivalent activation memory for equal active params. [@baseten](https://x.com/baseten/status/2047019335542358284) introduced **RadixMLP** for shared-prefix elimination in reranking, with **1.4 -1.6x** realistic speedups.




**Top tweets (by engagement)**

  * **OpenAI workspace agents** : [@OpenAI](https://x.com/OpenAI/status/2047008987665809771) launched shared, Codex-powered workspace agents for Business/Enterprise/Edu/Teachers.

  * **Qwen3.6-27B release** : [@Alibaba_Qwen](https://x.com/Alibaba_Qwen/status/2046939764428009914) announced the new open **27B** dense model with strong coding claims and Apache 2.0 licensing.

  * **Google TPU v8** : [@sundarpichai](https://x.com/sundarpichai/status/2046981627184902378) previewed **TPU 8t / 8i** , with training/inference specialization.

  * **Flipbook / model-streamed UI** : [@zan2434](https://x.com/zan2434/status/2046982383430496444) showed a prototype where the screen is rendered as pixels directly from a model rather than traditional UI stacks.

  * **OpenAI Privacy Filter** : [@scaling01](https://x.com/scaling01/status/2046972437422543064) and others highlighted OpenAI's new open-source **PII detection/redaction** model on Hugging Face.




* * *

# **AI Reddit Recap**

## **/r/LocalLlama + /r/localLLM Recap**

### **1\. Qwen 3.6 Model Releases and Benchmarks**

  * **[Qwen 3.6 27B is out](https://www.reddit.com/r/LocalLLaMA/comments/1ssl1xh/qwen_36_27b_is_out/)** (Activity: 2576): **Qwen 3.6 27B, a new language model, has been released on[Hugging Face](https://huggingface.co/Qwen/Qwen3.6-27B). This model features **`27 billion parameters`**and is designed to improve upon previous iterations with enhanced performance benchmarks. A quantized version is also available,[Qwen3.6-27B-FP8](https://huggingface.co/Qwen/Qwen3.6-27B-FP8), which allows for more efficient deployment in environments with limited computational resources. The release includes detailed benchmark results, showcasing its capabilities across various tasks.** The community is expressing excitement about the release, with some users highlighting the significance of the model's performance improvements and the availability of a quantized version for broader accessibility.

    * Namra_7 shared a benchmark image for Qwen 3.6 27B, which likely includes performance metrics such as inference speed, accuracy, or other relevant statistics. However, the specific details of the benchmarks are not described in the comment itself.

    * challis88ocarina mentioned a quantized version of Qwen 3.6 27B available on Hugging Face, specifically in FP8 format. Quantization can significantly reduce the model size and improve inference speed, making it more efficient for deployment without a substantial loss in accuracy. The link provided leads to the Hugging Face model repository for further exploration.

    * Eyelbee posted another image link, which might contain additional visual data or performance metrics related to Qwen 3.6 27B. However, the comment does not provide specific insights or details about the content of the image.

  * **[Qwen3.6-27B released!](https://www.reddit.com/r/LocalLLaMA/comments/1ssl6ki/qwen3627b_released/)** (Activity: 895): **Qwen3.6-27B is a newly released dense, open-source model that excels in coding tasks, outperforming its predecessor, Qwen3.5-397B-A17B, on major coding benchmarks. It features strong reasoning capabilities across both text and multimodal tasks and offers flexibility with 'thinking' and 'non-thinking' modes. The model is released under the Apache 2.0 license, making it fully open-source and accessible for community use. More details can be found on their [blog](https://qwen.ai/blog?id=qwen3.6-27b), [GitHub](https://github.com/QwenLM/Qwen3.6), and [Hugging Face](https://huggingface.co/Qwen/Qwen3.6-27B).** The comments reflect excitement and admiration for the Qwen team, with users expressing eagerness to utilize the model on their hardware and suggesting the team's contributions are monument-worthy.

    * ResearchCrafty1804 highlights the impressive performance of Qwen3.6-27B, noting that despite having only 27 billion parameters, it surpasses the much larger Qwen3.5-397B-A17B model on several coding benchmarks. Specifically, it achieves scores of 77.2 on SWE-bench Verified, 53.5 on SWE-bench Pro, 59.3 on Terminal-Bench 2.0, and 48.2 on SkillsBench, outperforming the larger model by significant margins in each case.

    * bwjxjelsbd comments on the competitive landscape, expressing satisfaction that Alibaba is advancing with Qwen models after META's perceived setbacks. The commenter hopes for continued competition and transparency, suggesting that META should open-source their Muse family models to maintain a healthy competitive environment.

  * **[Qwen3.6-35B becomes competitive with cloud models when paired with the right agent](https://www.reddit.com/r/LocalLLaMA/comments/1ssilc3/qwen3635b_becomes_competitive_with_cloud_models/)** (Activity: 848): **The post discusses the significant improvement in benchmark performance of the Qwen3.6-35B model when paired with the**`little-coder`**agent, achieving a**`78.7%`**success rate on the Polyglot benchmark, placing it in the top 10. This improvement highlights the impact of using appropriate scaffolds, suggesting that local models may underperform due to harness mismatches. The author plans to test further on Terminal Bench and GAIA for research capabilities. Full details and benchmarks are available on[GitHub](https://github.com/itayinbarr/little-coder) and [Substack](https://open.substack.com/pub/itayinbarr/p/honey-i-shrunk-the-coding-agent).** Commenters express surprise at the performance gains from scaffold changes, questioning the validity of benchmarks that don't control for such factors. There's also interest in using **pi.dev** for its extensibility in harnessing models.

    * **DependentBat5432** highlights a significant performance improvement in Qwen3.6-35B when changing the scaffold, noting a jump from `19%` to `78%`. This raises concerns about the validity of benchmark comparisons that do not control for such variables, suggesting that scaffold choice can dramatically affect model performance.

    * **Willing-Toe1942** reports that Qwen3.6, when used with pi-coding agents, performs almost twice as well as opencode. This comparison involved tasks like modifying HTML code and searching online resources for documentation, indicating that the choice of agent can significantly enhance the model's effectiveness in practical coding scenarios.

    * **kaeptnphlop** mentions the strong performance of Qwen-Coder-Next when paired with GitHub Copilot in VS Code, suggesting potential for further exploration with other tools like little-coder. This implies that integrating Qwen models with popular coding environments can leverage their strengths effectively.




[ Read more ](https://www.latent.space/p/ainews-tasteful-tokenmaxxing)

---

## [Shopify’s AI Phase Transition: 2026 Usage Explosion, Unlimited Opus-4.6 Token Budget, Tangle, Tangent, SimGym — with Mik…](https://www.latent.space/p/shopify)
*🔬 Latent Space | 2026-04-22*

_Early bird discounts for[the San Francisco World's Fair](https://www.ai.engineer/wf), the biggest AIE gathering of the year, end today - prices will go up by ~$500 tonight so do please lock in ASAP!_

* * *

From near-universal AI tool adoption inside Shopify to internal systems for ML experimentation, auto-research, customer simulation, and ultra-low-latency search, Mikhail Parakhin joins us for a deep dive into what it actually looks like when **a 20-year-old, $200B software company goes all-in on AI**. We cover why Shopify has become much more vocal about its internal stack, what changed after the **[December model-quality inflection](https://www.latent.space/p/wtf2025?utm_source=publication-search)** , and why the **real bottleneck in AI coding is no longer generation** , but review, CI/CD, and deployment stability.

We also go inside **[Tangle](https://shopify.engineering/tangle), [Tangent](https://apps.shopify.com/tangent-1), [SimGym](https://apps.shopify.com/simgym), **which are three major AI initiatives that Shopify is doing to make experimentation reproducible, optimization automatic, customer behavior simulatable, and search and catalog intelligence faster and cheaper at scale. Along the way, Mikhail explains **[UCP](https://www.shopify.com/ucp), [Liquid AI](https://www.liquid.ai/blog/liquid-ai-announces-multi-year-partnership-with-shopify-to-bring-sub-20ms-foundation-models-to-core-commerce-experiences)**, and why **token budgets** are directionally right but often measured badly, why AI-written code can still increase bugs in production, what makes Shopify's customer simulation defensible, and what he learned from the **Sydney era at Bing**.

**We discuss:**

  * Mikhail's path from running a major Microsoft business unit spanning Windows, Edge, Bing, and ads to becoming CTO of Shopify

  * Why Shopify is talking more publicly about AI now, and why staying at the frontier has become necessary for the company

  * Shopify's internal AI adoption curve, the December inflection, and why CLI-style tools are rising faster than traditional IDE-based tools

  * Why Jensen Huang is directionally right on token budgets, but raw token count is still the wrong way to evaluate engineering output

  * Why the real unlock is not more agents in parallel, but better critique loops, stronger models, and spending more on review than generation

  * Why AI coding can still lead to more bugs in production even if models write cleaner code on average than humans

  * Why Shopify built its own PR review flow, and why Mikhail thinks most off-the-shelf review tools miss the point

  * How PR volume, test failures, and deployment rollback are becoming the real bottlenecks in the agent era

  * Why Git, pull requests, and CI/CD may need a new metaphor once code is written at machine speed

  * What Tangle is, and how Shopify uses it to make ML and data workflows reproducible, collaborative, and production-ready from the start

  * Why Tangle is different from Airflow, and why content-addressed caching creates network effects across teams

  * What Tangent is, and how Shopify is using auto-research loops to optimize search, themes, prompt compression, storage, and more

  * Why Tangent is becoming a democratizing tool for PMs and domain experts, not just ML engineers

  * Why AutoML finally feels real in the LLM era, and where auto-research still falls short today

  * Why Tangle, Tangent, and SimGym become much more powerful when combined into one system

  * What SimGym is, why simulated customers only work if you have real historical behavior, and why Shopify's data gives it a moat

  * How SimGym evolved from comparing A/B variants to telling merchants what to change on a single live storefront to raise conversions

  * Why customer simulation is so expensive, from multimodal models to browser farms to serving and distillation costs

  * How Shopify models merchant and buyer trajectories, runs counterfactuals, and thinks about interventions like discounts, campaigns, and notifications

  * Why category-level behavior is so different across commerce, and why ideas like Chinese Restaurant Processes are showing up again in practice

  * Shopify's new UCP and catalog work, including runtime product search, bulk lookups, and identity linking

  * Why Shopify is using Liquid AI, and why Mikhail sees it as the first genuinely competitive non-transformer architecture he has used in practice

  * Where Liquid already works inside Shopify today, from low-latency query understanding to large-scale catalog and Sidekick Pulse workloads

  * Whether Liquid could become frontier-scale with enough compute, and why Shopify remains pragmatic and merit-based about model choice

  * Who Shopify is hiring right now across ML, data science, and distributed databases

  * The Sydney story at Bing, why its personality was not an accident, and what Mikhail learned from deliberately shaping AI character early on




* * *

**Mikhail Parakhin**

  * **LinkedIn** : <https://www.linkedin.com/in/mikhail-parakhin/>

  * **X** : <https://x.com/MParakhin>




* * *

## Timestamps

00:00:00 Introduction: Mikhail Parakhin, Microsoft, and Shopify

00:01:16 Why Shopify Is Talking More About AI

00:02:29 Internal AI Adoption at Shopify and the December Inflection

00:06:54 Token Budgets, Jensen Huang, and Why Usage Metrics Can Mislead

00:10:55 Why Shopify Built Its Own AI PR Review System

00:12:38 AI Coding, More Bugs, and the Real Deployment Bottleneck

00:14:11 Why Git, PRs, and CI/CD May Need to Change for Agents

00:18:24 Tangle: Shopify's Reproducible ML and Data Workflow Engine

00:21:19 Why Tangle Is Different from Airflow

00:26:14 Tangent: Auto Research for Optimization and Experimentation

00:30:07 How Tangent Democratizes Experimentation Beyond ML Engineers

00:33:06 The Limits of Auto Research

00:36:36 Why Tangle, Tangent, and SimGym Compound Together

00:37:20 SimGym: Simulating Customers with Shopify's Historical Data

00:42:47 The Infra Behind SimGym

00:46:00 Why SimGym Gets Better with Real Customer History

00:47:30 Counterfactuals, HSTU, and Modeling Merchant Trajectories

00:51:55 CRPs, Clustering, and Category-Level Customer Behavior

00:53:30 UCP, Shopify Catalog, and Identity Linking

00:55:07 Liquid AI: Why Shopify Uses Non-Transformer Models

00:59:13 Real Shopify Use Cases for Liquid

01:03:00 Can Liquid Scale into a Frontier Model?

01:09:49 Hiring at Shopify: ML, Data Science, and Databases

01:10:43 Sydney at Bing: Personality Shaping and AI Character

01:13:32 Closing Thoughts

* * *

## Transcript

[00:00:00] **swyx** : Okay. We're here in the studio, a remote studio, with Mikhail Parakhin, CTO of Shopify. Welcome.

[00:00:08] **Mikhail Parakhin** : Thank you. Welcome.

[00:00:10] **swyx** : I don't even know if I should introduce you as CTO of Shopify. I feel like you have many identities. Uh, you led sort of the, the Bing ML team, I guess, uh, uh, or ads team. I, I don't know, I don't know, uh, you know, it's, uh, people va-variously refer you as like CEO or, or, uh, I don't know what that, that, that said previous role at Microsoft was.

[00:00:29] **Mikhail Parakhin** : Uh, that was... Yeah, my previous role w- at Microsoft was the-- I actually was the CEO of one of Microsoft's business units, which included, as I, you know, as we discussed, all the things that people like to laugh about, uh, including Windows and Edge and Bing and ads and everything.

[00:00:47] **swyx** : Yeah, yeah. What a, what a, what a wild time.

You've obviously, uh, done a lot since you landed at Shopify. Uh, one of the reasons I reached out was because you started promoting more sort of internal tooling, uh, primarily Tangle, but also a lot of people have seen and adopted Tobi's QMD, uh, and obviously, I think, uh, Shopify has always been sort of leading in terms of, uh, engineering.

I think more-- it's just more recent that you guys have been more vocal about your sort of AI adoption. Is that, is that true?

[00:01:16] **Mikhail Parakhin** : Well, I think AI tools in general are fairly recent development, uh, and we've-- Shopify, you know, at this stage of its development, we're developing AI in-in-house and other, uh, building tools that use AI and, you know, interfacing with the wider AI community, uh, you know, are on the sort of the, uh, runaway trajectory.

So it just did by sort of natural byproduct. We, we talk about it more also. We just, uh, just even yesterday, Andrej Karpathy was famous in tweeting about, oh, are there some, uh, ways, uh, that, that you can organize your agents to store the data and then, uh, look up the data so that you don't have to research or, or lose context every- Yes

time. And a little bit tongue in cheek, I tweeted that, "Hey, we've, we've done it much earlier, and we even have different approaches, Tobi and I." Tobi, of course, is a big fan of QMD, and I'm more of a SQL, SQLite fan. But, uh, yeah, very similar things that we've already done here. The point is, yeah, we're very dynamic, you know, explosively growing company, and we have to be at the forefront of AI adoption, obviously.

[00:02:29] **swyx** : Yeah. Yeah. Um, you, your team kindly prepared some slides actually that we were gonna bring up on to, uh, the screen. I think I can, I can screen share, and then we can kind of go through some of the shocking stats that maybe, maybe put some numbers to what exactly is going on. So here we have, uh- An internal AI tool adoption chart.

What are we looking at here? What ?

[00:02:54] **Mikhail Parakhin** : Yeah, this is very interesting statistics. Uh, this is number of daily active workers, you know, think of, uh, DAO, basically the active users of-

[00:03:05] **swyx** : Yeah ...

[00:03:05] **Mikhail Parakhin** : AI tool as a percentage of all the people in the company, right? And then- Yeah ... different AI tools. And, uh, you could see two things here is that one is the green is total.

Uh, green is just total. So you could see that it approaches really % by now. It's hard not to do your job now without interacting deeply, at least with one tool. You could see another interesting thing is just as many people commented in December was the phase transition when suddenly models gotten good enough that, that everything took off and started growing.

Uh, it, it was many people noticed that the thing is that small improvements accumulated into this big change in Sep- December roughly timeframe.

[00:03:52] **swyx** : Yeah.

[00:03:52] **Mikhail Parakhin** : The other thing I would claim you could see is that, uh, CLI-based tools and tools that don't require you to look at the code becoming more popular, and you could see, yeah, various versions of, uh, Cloud Code and Codex and Pi and internal development tools taking off.

Uh, exactly, yeah, uh, and blue is our River, just internal agent for coding, where tools, uh, that require IDEs such as, uh, GitHub, Copilot or Cursor, they're not exactly shrinking, but they're not growing as fast. Like, uh, red, red line is, is the IDE kind of tools. So you could see that they're, they're not experiencing as, as fast of a growth.

[00:04:37] **swyx** : As I understand it, basically, every employee has their choice, right? Of choose whatever tool you use, and then you're just kind of doing a, a daily sur-survey or something.

[00:04:47] **Mikhail Parakhin** : Exactly. And, uh, we- Yeah ... the, the push is to get your job done, you can use any tool, and we effectively fund unlimited tokens for everybody.

Uh, we, we do, we do try to control the models that, uh, people use, but from the bottom, not from top. Like we basically say, "Hey, please don't use anything less than Opus four point six."

[00:05:09] **swyx** : Oh .

[00:05:10] **Mikhail Parakhin** : Some people, some people end up using GPT five point four extra high. Some people use Opus four point six. Um, uh, you know, uh, there are some, uh, there are plus and minuses in going for full one million context window versus not.

But, uh, we try to discourage people from using anything less than that.

[00:05:28] **swyx** : Yeah, yeah. Got it, got it. Uh, I mean, uh, that's, you know... The, the next chart here, it really kind of shows the expansion and the sort of December twenty twenty-five inflection, right? That, uh, people are using a lot of tokens. I think it's also really interesting that no one was kind of abusing it in twenty twenty-five.

Like it was- Had comparatively, uh, to this year, there was almost no growth. I mean, it's still like, you know, probably, probably gave fifty percent.

[00:05:56] **Mikhail Parakhin** : Yeah. This is just a different scale. It's still exponential- Yeah, yeah ...growth at just a different- ...rate of expansion. Uh, there was inflection point, and Sean, I would claim the, the super interesting part here is that you could see that the distribution becoming more and more skewed.

Yes. The top percentiles grow faster. So that means- Yeah ...the people in the top ten percentile, they, their consumption grows faster than seventy-five and so forth. So, uh, the distribution skews more and more towards the highest users, which is... I don't know what it tells me. It's like it feels not ideal, to be honest.

Or maybe it's okay. We'll see.

[00:06:36] **swyx** : Why does it feel not ideal? Is, is it because of, um, quantity over quality, or what's the concern?

[00:06:42] **Mikhail Parakhin** : Because take it to the limit. That means, you know, if, if this rate of separation continued- Ah, yes ...a year, there will be one person consuming all the tokens. So it's just, it's kinda strange.

[00:06:54] **swyx** : Yeah, I mean, um, uh, I, I think internal like teaching and all that, uh, will, will help sort of distribute things more widely. But in, in the early days, of course, the people who are sort of more AI-pilled will obviously find more ways to use it than the people who are less AI-pilled. Maybe let's, let's call it that.

I'll just, I'll just kinda quickly, uh, pause from the, the... You know, we will go back to the rest of the slides, but I just wanna, um, review, you know, there are a lot of CTOs of, of large companies like yourself where they're all considering some kind of token budget, right? Like I think it's something, something that Jensen Huang has been talking about, where like if your 200K engineer is not using 100K of tokens every year, like they're, they're underutilizing coding agents.

Of course, Jensen Huang would say that, but like it seems a very quantity over quality approach and like some, some people are basically saying like, well, is this comparable to judging engineer quality by lines of code, right? Which we also know is like kind of flawed, but better than nothing. So I, I don't know if you have like a sort of management take here on, on how to view this kind of, uh, metrics.

[00:08:02] **Mikhail Parakhin** : Well, I mean, you're, you're baiting me. I, I like... This is my favorite topic. Uh, if you let me, I'll probably talk for two hours on just this. I have a lot of things to say. Like I do think Jensen gotten a lot of bad press saying, "Oh, of course you're, you know, this, uh, the- ...the cake seller says you don't need enough cakes."

You know? Like, of course. Uh, but, uh, I actually, uh, think that's undeserved. I think he, he's actually right. Uh, I do think- He,

[00:08:33] **swyx** : he's directionally correct.

[00:08:35] **Mikhail Parakhin** : Yeah. Yeah. He's directionally correct for sure. Uh-

[00:08:37] **swyx** : Who knows what the right number is? Yeah.

[00:08:39] **Mikhail Parakhin** : The thing that I do Uh, want to say, and this is something that we learned through trial and error and very important is like two things.

One is that it's not about just consuming tokens. Uh, you can consume tokens and, and in fact, the anti-pattern is running multiple agents, too many agents in parallel that don't communicate with each other. That's almost useless, uh, compared to just fewer agents and burns tokens very efficiently. Uh, setting up the right critique loop, especially with the high quality models, where one agent does something, the other one, ideally with a different model, critiques it, uh, suggests ways to improve it, the agent redoes it with this critique and, and so it takes much longer.

So people don't like it because latency goes up. You know, they, they have to wait until this debate is happening. But, uh, the quality of the code is much higher. And another thing, just since you mentioned like, look, uh, uh, yeah, the overall budget is just like, uh, lines of codes. Lines of codes are exploding for everybody right now, or partially because AI is really mover balls, but partially just because AI can write a lot more code, you know, doesn't get tired.

And so you have to have to have a very strong narrow waist during PR review. Otherwise, just the number of bugs will go through the roof. It's, uh, it's this unexpected consequence of the just volume trumping everything. I would claim by now good model writes code on average with fewer bugs than, than the average human.

But since they write so much more of it, like more of it will make it into production. So you have to- You still

[00:10:26] **swyx** : have

[00:10:26] **Mikhail Parakhin** : more bugs. Yeah. Have to have a very rigorous PR reviews, also automated of course. But, uh, yeah, that to spend a lot budget there. Like this, this for me, for me, actually, the important metric is the ratio of budget spent during code generation versus, uh, spent, uh, expensive tokens like GPT, uh, five point four Pro or, uh, uh, Deep Think from Gemini, you know, checking on PR reviews.

[00:10:55] **swyx** : Yeah, totally. Uh, I noticed in your chart you didn't have any review tools. Do you just use like, like let's say a Claude code to review tools? Or do you have another set of review tools like the Greptiles, the Code Rabbits, uh, Devin Reviews has a review tool. I don't know if you've had those specialist review tools.

[00:11:13] **Mikhail Parakhin** : You are a little bit jumping on my store tool right now because the graphs I was only showing public tools. Uh, uh, the-- I haven't found a good PR review tool that, that does what I think should be done. And, uh, partially my, my thinking is because it's so... It just goes against both what people feel like emotionally they prefer and, uh, some of the, uh, you know, frankly Even business models that, that the companies run.

At peer review tool, uh, time, you want to run the largest models. That means, I don't know, Codex or, or, uh, Cloud Code is not gonna cut it. You need to have pro-level models if you really want to, uh, stand the tide of bots from going into production. And you need us to spend a lot of time, the models taking turns, but you don't want, like, a big swarm of, uh, of, uh, agents.

So in fact, you end up in a different dual-dualistic world where you generate not that many tokens. You, in fact, generate few tokens, but it takes f-a long time because these are expensive models taking turns rather than many, many agents trying to do many things in parallel. So that's, that's why I feel like I haven't found good tools, so we are using our own for peer review for now.

[00:12:33] **swyx** : Yeah. Yeah. I mean, uh, I think a lot of companies are building their own, uh, especially to their needs, right?

[00:12:38] **Mikhail Parakhin** : Mm-hmm.

[00:12:38] **swyx** : Um, I, uh, you also have a chart here going back to the slides on, uh, PR merge growth, where we're now at thirty percent, uh, month on month rather than ten percent. Uh, and also the, the estimated complexity is going up.

You know, this is productivity, right? 'Cause y- presumably there's more stuff going into the code base and more, more features getting worked on. I'm curious about the backlog, right? Like the, the, the-- I actually don't mind a pro-level model taking an hour or two hours to review my PR, because I've dealt with humans who take a week to review my PR, right?

And I keep pinging them on Slack, "Hey, hey, review my PR." So, you know, I think there's some trade-off here where, like, it still doesn't make sense.

[00:13:18] **Mikhail Parakhin** : Exactly. That, that's exactly m-my point. Uh, that on one hand, you can tolerate longer latencies at, uh, PR. On the other hand, like right now, the real problem is not in spending time waiting for PR.

It's real problem is since there's so much more code than- Yeah ... uh, probability of at least some tests failing going up, and then you, like, keep de-failing, then you have to find the offending PR, evict it, retest it without that PR, and so deployment cycle becomes much longer. Uh, so it actually, in terms of the overall time to deploy, it's total time savings if you spend more time on a longer model, like thinking for an hour, because then, then you, you don't have to spend all that time during testing and rolling, you know, rolling back the deployment.

[00:14:03] **swyx** : Yeah, totally. That's still worth it. You know, you don't look at the individual, look at the aggregate, and look at the, the, the change in the aggregate system.

[00:14:11] **Mikhail Parakhin** : Exactly.

[00:14:11] **swyx** : I'm kind of curious if, like, there's this PR mentality and, like, c-- the, the, the CICD paradigm will be changed eventually. Some people are like, obviously a lot of people want new GitHub, but I even wonder if, like, Git is the problem, right?

Like, is that the bottleneck? Is the concept of a PR a bottleneck? Do you guys use stack diffs? I don't know if, uh, that's a, like, a merge queue stack diff type of thing.

[00:14:34] **Mikhail Parakhin** : We, we use, we use Stacks, we u- we use Graphite. We worked with, uh, Graphite a lot. Uh, so we use Stack, uh, PRs. I think, uh, like that's clearly the overall CICD in general, and the interaction with the code repository right now is the, clearly the sort of the, the main issue and the bottleneck for us, uh, and highest top of mind.

I would say we probably need a different metaphor or different whole design of how to process it in new agentic world. I haven't seen anything dramatically better yet. I, I think everybody right now is just trying to keep their head above the water 'cause, 'cause there, there's so many PRs and then everybody's CICD pipelines start creaking, the, the times are increasing, the number of bugs slipping by increasing, and you have to, have to clap on down.

And so we are a little bit in this situation when we need to first stabilize that story and then start thinking, hey, what, what it could be a completely different and new world, which I haven't... I know some people working on it. I haven't seen something, like anything super compelling yet, but clearly the old thing were designed for humans will need to be morphed into something new.

[00:15:53] **swyx** : One of the thing that I, I think about is kind of like the merge conflict is basically a global mutex on the whole system, right? And in, in hu- in human organizations, we do have something like that. It's the company standup. But like, other than that, it's like it's actually fitting for us to be somewhat decentralized, somewhat plugged into one stream of information source, but somewhat lossy.

Like it's okay, you know, that, that not every delivery is like atomic consistency. Like we're not dealing with a database sometimes.

[00:16:27] **Mikhail Parakhin** : This is a very good point, uh, because since humans don't write code too fast, you know that global mutex is not too bad. Once you-

[00:16:36] **swyx** : Yes ...

[00:16:37] **Mikhail Parakhin** : start writing code at the speed of machine, it becomes the, you know, the bottleneck.

Then what do you do? Maybe, and I can't believe I'm saying this because I, I'm long-- lifelong opponent of, uh, microservices, and I always thought that was, like, a really bad idea. And now that you're saying it, like, maybe in new guys like microservices will make a comeback, you know, because then you, you can ship things independently in tiny things and, and the managing all that complexity automatically will be much easier.

I don't know. Like, we'll s-- we'll have to see.

[00:17:10] **swyx** : Yeah. I mean, I don't know what the Microsoft or, or Shopify thing is, but I, I read this paper from Google where they have a monorepo that deploys into microservices, right? And then, uh, the other concept that I think about a lot is the Chaos Monkey concept from, from Netflix.

Being able to create, like, this robust system where, um, uh, you know, you, you have the service discovery, you have the, uh, the independent, independent microservices discovery and, and, uh, you know, probably going to be a fair amount of duplication. That's how an organic system sort of scales, uh, that, that you have that...

I don't know how you call it. Slack? Robustness? Depend-- uh, d-duplication. I, I, I forget the-- I, I'm-- And this-- those-- these are not exactly the terms- Hmm ... I'm looking for, but I c-can't really think of the words. Okay. I was gonna go into Tangent and Tangle. Uh, so, uh, we, we sort of discussed the overall stats that, uh, Shopify has.

Uh, but, you know, I, I think some, some pretty cool stuff that you guys are working on is your ML experimentation, uh, and your, your sort of auto tr-research training pipeline. Presumably you're much closer to this one because it's, it's a sort of personal hobby of yours. How, how would you explain them in, together?

I thought we have a slide that, like, uh, has the s- the system diagram.

[00:18:24] **Mikhail Parakhin** : Yeah. Tangle first and then Tangent as a-

[00:18:27] **swyx** : Yeah ...

[00:18:28] **Mikhail Parakhin** : as a thing on top of Tangle. And, uh, Tangle is the third generation, I claim, of, uh, systems of, uh, running any data processing, but a bit with a skew for ML experiments, but not necessarily. Any sort of data processing tasks where you need to iterate, share, and you have scale so that you want maximum efficiency.

You know how, like, normally you would work, you would-- Imagine you're a data scientist or an ML practitioner, you would get Jupiter notebooks or, or maybe you would get, uh, you know, Pyth- your Python scripts, and you would manage the data, and you produce those TSV files, and you put them in some JFS or something.

Then you would notice that, oh, it has this, uh, weird missing values. You go and write another script that, uh, goes and replaces them with, uh-

[00:19:20] **swyx** : Ah ...

[00:19:21] **Mikhail Parakhin** : dash S. And then, then you, then you run some, some, uh, "Oh, I need to filter bots." And so you run some light GBM model that, uh, removes the bots. And then, then you like-- And then you, you kind of like get into shape, and then you start experimenting, and you run multiple experiments, and then you're like, "Oh my God," like, "this experiment is worse."

You undo, and you cannot get to previous result. And like, "Ah, what did I do?" Like that. Again, then, then you finally like get everything working. Then you like start throwing it over the fence to production. You, you replicate it, those things don't work, and then sometimes you like don't notice that you forgot some feature naming and the, the features don't match.

But then, like imagine you, you did everything, and then six months later you're like, have to repeat it because now there's more data, or you wanted to do another pass, and you're like, "What, what did I do?" Or like, or like, "This script crashes now," or the, "the path has changed." And then, then you're trying to, like you spend another month just doing ar- digital archeology on your own, you know, history, right?

Now multiply that by many, many teams. Now imagine you got an intern that you wanna ramp up. Now you have to show that intern, "Oh, you know, look, here's the folder, there's the scripts, you know, ask your cloud agent to do, and then, uh, to, to figure it out." And then cloud agent does something, and then you're, "Ah, yeah, right, right, it was the wrong folder.

I forgot to tell you, I actually have this other thing I forgot myself." And, and that's, that's the, like, the daily life we all, uh, all know it, uh, if, if you're a data scientist, machine practitioner, ma- machine learning practitioner or, uh, or even like any data managing, uh, person.

[00:21:00] **swyx** : Yeah. So I, I used to do this, uh, f- uh, on the quant finance side, uh, in, in my hedge fund.

So we did this before Airflow, and then, uh, obviously Airflow came along and, uh, then more recently Dagster, uh, I would say is like, in my mind, what I would use for that shape of problem, uh, where you had to materialize assets and create a pipeline.

[00:21:19] **Mikhail Parakhin** : And that's, that's very good segue because... So Airflow is great, but Airflow is more about you, you have something and you wanna repeatedly run it in production on schedule.

It's less about you as a team developing things and being able to share, and you grabbing the standard pipeline and saying, "Hey, I wanna change this tiny little component in the huge sea of data processing, and I don't wanna-- I wanna run ten experiments on this, and I wanna do hyperparameter optimization."

All that is very hard to do with Airflow. It's very easy to do with Tango. Tango is m- more about, it's everything about group of people Running experiments, it might be agents too nowadays. Uh, running experiments cheaply, collaborating, sharing results. Uh, you don't need to understand fully. You, you grab-- you clone somebody else's experiment or somebody else's pipeline, uh, run, uh, change small piece, run it, be, like, get it to production state, and then ship in one click.

So then the... You don't have to port it into any other system to, to run in production. You can just run the same experiment. It's, it's fully production ready. And, and it's, uh, it has lots of... Again, as I said, it's third generation system. The original one was, I would claim there was Ether and then, uh, at least in my career, Ether was the first, first, uh, that pioneered this type of approach.

And then there was, uh, Nirvana, which, uh, uh, at Yandex, which did kind of sec-second take on this. And now this one aggregates the, the learnings from all of those and, and Airflow as well to, to get to the state where you try it, it, it feels kind of magical. Uh, 'cause now everything is based on content, uh, hashes.

So even if the version changed, but if the output didn't change, nothing is being rerun. It's very efficient. If you... Multiple people start experiment that needs the same sort of data preprocessing, it's not repeated multiple times. It's automatically done only once. If you start ten experiments that all require, you know, some, some data preparation first as the first step, and you don't have to coordinate for that.

Like, you don't have to know that other people are starting it. You now, it's very easy compos-, uh, composability, any language you can u- uh, you wanna use, and it's very visual. So you can see immediately, you can edit it easily, you can assemble small things with just even mouse clicks if you want to, and, uh, share, clone.

And everybody knows also it's fully kind of static in the sense that we rerun it second time, it will exactly have the same results. Like, you will never have to do digital archeology. So full versioning and everything is also there.

[00:24:06] **swyx** : Uh, so, so people can, uh... It's open source. Go to the GitHub repo and, and, uh, check it out.

Uh, and it is also a really good, uh, blog post about it. I think all these is, like, really appealing. The, the, the, the thing that I think sells me the most about it is that, um, sort of development to production transition, right? Which I think, um, a lot of people haven't really solved that, uh, strictly, right?

Like, we develop really, really well in, in Python notebooks, but then, you know, that's obviously not a sort of production ready process. I think that, like, any way in which that is solved, I think is, is very appealing. Then the other thing that you mentioned, which also raised my eyebrows, was content-based caching, which you mentioned is, is, um, you know, is ve-very much, uh, um, a sort of efficiency measure about, uh, you know, just like recalculation only on, on sort of content addressing Which I think makes sense.

Uh, it surprised me that the savings could be this much, but maybe I just haven't worked at your scale where there's so much duplication, uh, that people just rerun because they change a single ID upstream.

[00:25:10] **Mikhail Parakhin** : It does, yeah. But it's not only you rerun. The, the main savings are coming from the fact that you ran it, you got your job done, and you moved on.

Then- Yeah ... somebody else in some department you don't know existed runs the same task, but on a newer version.

[00:25:27] **swyx** : Yeah.

[00:25:27] **Mikhail Parakhin** : Like right now, you can't, in, in most of the organizations, you can't even find out about it so that you can't even measure that you're spending that time twice, right? Here- Yeah ... if everybody's on Tango, that's detected automatically and detected that the output is the same.

And then for that person, all it looks like is like experiment just suddenly moved, jumped forward, right? Uh, uh- Yeah ... so that's because, because the, there's network effect of multiple people helping each other.

[00:25:51] **swyx** : Yeah. This is one of those things where it's designed to be a platform from the beginning rather than an individual developer's tool from the beginning, right?

And, and everything's gonna streams down from there. That is the sort of Tango, uh, orchestrator, and it's, it manages jobs. We've seen a few versions of this, and this is obviously, uh, uh, the sort of, uh, unique approaches that you guys have, have, uh, figured out. And then there's Tangent.

[00:26:14] **Mikhail Parakhin** : Yeah. And Tangent is basically an automatic auto research loop that can help and kind of do your work for you.

Uh- ... you know, uh, effectively, effectively, Andrej Karpathy recently popularized it with auto research. Yes. Remember he said like he was, uh, speed running this, uh... Yeah, uh, you know the story. The, here we're basically bringing the same capability into Tango so that, uh, the, uh, Tangent can analyze it. It's just an agent that can run multiple experiments, figure out what can be changed, and keep on rerunning it, keep on modifying until, uh, maximizing some goal, some loss function, whatever you need to, to achieve.

And in general, I would say if you're not using auto research-like approach in whatever you do, like literally whatever you do, then you're missing out. We saw at Shopify that taking like a wildfire, anything where you can put measurements can be done dramatically better. Our-

[00:27:19] **swyx** : Mm-hmm ...

[00:27:20] **Mikhail Parakhin** : uh, speed of, uh, templatization HTML, uh, completely new UX tem- uh, templatization of, uh, reducing latency for liquid themes.

Uh, we-- Our, uh, search, uh, recently we moved from It's hard even, uh, quote from eight hundred QPS to forty-two hundred QPS with the same quality just by pure optimizations and not a research loop that kept running and changing code in our index serve on the same number of machines, just increasing the throughput.

We, we managed to improve the quality of gisting and machine learning process. Uh, you know, gisting is the prompt compression technique that

[00:27:59] **swyx** : allows for

[00:28:00] **Mikhail Parakhin** : lower latency and, and lower and, uh, actually higher quality slightly. So like literally whatever different walks of life, and it doesn't have to be AI related.

Uh, we, we had a reduction in, uh, storage because the agents would go and find data sets that clearly are derivative, uh, and then you don't need to store things twice. You know, we, we, we found somewhat embarrassingly that it was one of the largest tables was hashing random IDs into another random ID, and we literally- Oof

put only one. So it was translating, yeah, two random IDs hashed

[00:28:36] **swyx** : into

[00:28:37] **Mikhail Parakhin** : each. So, so

[00:28:37] **swyx** : it has access to the code as well, so it can, it can check the, like what, what the hell is it doing?

[00:28:42] **Mikhail Parakhin** : So there, there cou- it could be run in two levels. You, uh, you know, at the superficial level, it could just use ex-existing components and, uh, reshuffle them.

Uh, you know, like you can grab- Yeah ... uh, XGBoost, and you can grab some, some Py- PyTorch module, and then can grab some, you know, grab another tools and, and combine them. At a deeper level, since Tangle is all sort of CLI based underneath you, every, every component is a wrapped really CLI, uh, call and a YAML file, it can analyze code and create new components and, and, uh, keep on iterating as well.

So, so you can, you can both have quick modifications of existing t- uh, pipelines with the, with components that are already there pre-baked, or you can create new components, uh, and-

[00:29:29] **swyx** : Yeah ...

[00:29:29] **Mikhail Parakhin** : keep iterating on those. So auto research is, again, this is probably the, the thing I was excited the most in the last two months happening, and we see it taking like, like totally like a wildfire.

Just, uh, everybody, every day, every... well, every day, every minute, I would, uh, have somebody Slack message saying, "Oh, look how much better I made it." And, uh, it's all throughout the research.

[00:29:53] **swyx** : Is this democratized in some way in, in the sense that like is it your ML, uh, engineers and researchers doing this, or is it your regular PMs and software engineers also have the ability to auto-- to use Tangent?

[00:30:07] **Mikhail Parakhin** : This is an awesome question. Like, Tango in general and Tangent in particular are extremely democratizing. Like they- Yeah ... they are the main tools for- 'Cause I don't

[00:30:15] **swyx** : need the details.

[00:30:16] **Mikhail Parakhin** : Yeah. Exactly. Initially used by ML and AI engineers, but then literally, as you said, PMs are like the highest user right now is one of PMs on our org, uh, Sartak and he was, he was number one by, by usage of, of this 'cause they're just, uh, energetic and knowledgeable, and now it, it unlocks a lot of capability where you don't have to co-change code manually.

[00:30:39] **swyx** : I mean, I mean, because it kind of cuts out the ML, ML engineer from the process because the, the, the PMs have the domain knowledge and the ability to think about, uh, from first principles about, okay, what, what results do I want? And they can-- they even have the access to the data that, that needs to go in.

So it's like in some ways, like this is the magic black box that we've always wanted for, for training and, and for, uh, I guess, uh, uh, hill climbing, whatever.

[00:31:04] **Mikhail Parakhin** : It's basically cloud code for your AI development- ... uh, situation, right? Like now, now you don't have to know exactly how algorithms work. You can just, uh, bring your domain knowledge and expertise and product knowledge and iterate within Tangent until you've gotten the results that you need.

[00:31:21] **swyx** : In my previous roles, every time that someone has pitched AutoML, you know, I've always been like, "Uh, this is not, this is not gonna work. It's, you know, it's, it's always gonna be a flop." Somehow it's working now. I mean, presumably the answer is now we have LLMs and it's good enough, right? It's, it's an emergent property that we can do auto research, but like, it doesn't feel that satisfying that how come we didn't do this before, right?

Like we just did like parameter search and like, I don't know. That's maybe that's it.

[00:31:48] **Mikhail Parakhin** : Yeah. Bayesian optimization and hyperparameter optimization was, was the one that, or facet of AutoML that was used very actively, which incidentally also built into, uh, Tango. But, you know, I know Patrice Simard very well, and, uh, he was such a, uh, such a proponent of AutoML, and he put, like literally spent careers trying to democratize it.

Without LLMs, it just turned out to be very hard. Like it, you, you would have flexibility within certain narrow domain, but it was hard to wider scale, and now with LLMs suddenly it's like magic wand, and so suddenly everybody- ... is an AutoML expert.

[00:32:28] **swyx** : Yeah, I, I think it's multiple things, right? Like I'm, I'm just gonna bring up the, the, the chart again, right?

Like LLMs can do the monitoring very well. That is the very potentially unbounded, super unstructured. It can do the analysis very well, it can do the... Uh, and basically it is much more intelligence poured into every single step. Uh, there's maybe nothing structurally changed about AutoML, but this is just m-more intelligent and more unstructured.

[00:32:53] **Mikhail Parakhin** : Exactly.

[00:32:54] **swyx** : Any flaws that you've run into? Like everyone is like drinking the Kool-Aid, oh my God, time savings, uh, you know, performance improvements. Like what, what, uh, issues have you have, uh, come up?

[00:33:06] **Mikhail Parakhin** : This is really cool. It's not a solution to all the world's problems for sure. The limitations are usually the ones I-- And this is where we get into a bit of a subjective territory.

Uh, I can only share what I've, I've seen so far, and I'm sure the situation, uh, is changing, and, you know, maybe after I say it, like many people will reach out and say, "Hey, what about this?" And you don't know that, and then, then we'll be probably right. But what I've seen is auto research is very good at doing kind of obvious things that you don't have bandwidth to do or you didn't notice or maybe you're not aware of like the-- some standard practices.

It is not good at doing something completely out of distribution, something that, you know, you have to think for, for multiple days, uh, and, and do something like none of this. So, so it's, uh, I, uh, set an experiment once, uh, on, on my sort of, uh, hobby thing, and I let it run for, uh, ended up, uh, several weeks run, uh, you know, it's like full production kind of scale, so it, you know, slow runs and, and it ex-- it performed in the end, uh, over four hundred experiments, and only one was successful.

I'm like, "Okay, that's, that's good." But-

[00:34:18] **swyx** : But it saved time.

[00:34:19] **Mikhail Parakhin** : Yeah, I saved time. Like it, it was the, that thing. Yeah, if I, if I were doing four hundred experiments myself, my betting average, as I said, would have been much higher, I'm sure. But also, first of all, it would take me like three years to do four hundred experiments.

And, uh, I didn't have to do them. Like the machines were just, uh, the price of electricity did that. So, and I got one improvement, uh, that in, uh, my, my-- Honestly, when I was starting that experiment, my thinking was to go and show that, "Hey, Andre, maybe you just don't know how to optimize." And I was super smart because in, in my pro-problem, it was optimized for many years, and it was like fully improved.

Uh, and I didn't expect it, you know, auto research to find anything at all. Yet it did. So instead of making fun of Andre, I ended up, uh, a big, big supporter. Yeah, that's exactly the tweet. Yes.

[00:35:10] **swyx** : You and Toby really, really go back and forth on-online a lot, which is really funny. Uh, think of it as, as an eval for the optimalness of the code it's running on.

Uh, it's almost like it reminds me of like a Kolmogorov complexity thing, but, uh, I guess it's-- there's some optimal thing that you're trying to sort of reduce down to, I guess. Um, and so, so you, you, you know, you should congratulate yourself that you had, uh, you know, uh, ninety-nine percent, uh, optimality.

[00:35:36] **Mikhail Parakhin** : Exactly, yeah. I think Andre really deserves a lot of credit for popularizing this approach. This is, uh, this is incredibly, I think, powerful and cool and You know, the, uh, even him, him just mentioning it led to a lot of gains in a lot of places in the industry, so we should be thankful.

[00:35:56] **swyx** : Yeah. I think he also has a just...

I don't know what it is. Like, um, you know, it, it is a simple self-contained project that people can take and apply to other things, which is, is, is one thing, but also just the name. Just like somehow no one, no one managed to call their thing auto research. It's just naming things is very important. I think that that is mostly, uh, our coverage of Tango and, and, uh, Tangents.

I think obviously, you know, there's a lot of, uh, ML infra at, at Shopify that people can, uh, dive into. We're about to go into SimGym, but before I do that, any, any other sort of broader comments around this whole effort? Like where is it, where is it leading to?

[00:36:36] **Mikhail Parakhin** : As a segue to SimGym, like all those things start composing strongly.

And, uh, you could see a huge unlock when you can look at each one of the tools and, and you see, oh, they're extremely useful. Uh, Tango is useful by itself. Auto Research is useful by itself. SimGym is useful by itself. If you combine all three, you create like synergetic effect. I think that's why we wanted to even, uh, cover them today is because this is something that if you go back even, you know, five years ago, would've been unthinkable.

Uh, replicating that, uh, would, would be either incredibly costly or impossible, right? With probably thousands of people are required.

[00:37:20] **swyx** : Well, we have serverless human, uh, serverless intelligence, right? Like, uh, so yes, you do have thousands of hu-- of, of intelligences, not just, not humans. And that's, that's close enough, right?

Even if they're not AGI, they're, they're close enough to do the, the task that you need them to do. And, and, you know, that's, there's plenty for, for a lot of routine work, knowledge work. Okay, let's get into SimGym. Um, this is one of those things I, I was surprised to see actually it's apparently your, uh, one of your most popular launches, and I think something that, uh, I think Sim AI, I think Yunjun Park, who did the Smallville thing, there's a very small cottage industry of people trying to do like the simulate customer thing.

I think a lot of people maybe don't super trust this yet because they're like, well, obviously they would just do what you prompt them to do, right? But maybe just think, uh, tell us about the sort of inspiration or origin story.

[00:38:10] **Mikhail Parakhin** : That's exactly actually the thing I wanted to cover, because if you don't have the historical data, all you can do is prompt a-agents in a vacuum, and they will do exactly what you prompt them to do.

In fact, when I first proposed it, and this is a bit of, um, my brainchild initially, if I, I can boast, even Toby said like, "But wouldn't they, they just repeat what, what you tell them?" And, uh, but I'm like, "Yes, except Shopify has decades of history of how people made changes and what there is, uh, there, what it resulted in terms of sales."

So now what we can do is we can-- we have this... It's not, it's a noisy data. There's a small, usually websites, uh, you know, like things, things are never in isolation. It's almost never AB experiment. It's always AA experiment when there's has two meanings, but basically, you know, in different time you run two different things.

But if you aggregate in general, uh, like everything together, and you apply, uh, denoising and collaborative filtering like approach, you can extract a very clear signal. And then you can optimize your agents. And that's why it took so long. It took almost a year of that optimization of just us sitting and fiddling, and, and we had this internal goals of correlation of hitting-- internal goal was to hit zero point seven correlation with, uh, add to cart events, for example.

Like that, that if we run real AB test experiment, that it should, it should go and, and rep-uh, replicate, uh, same sort of success that, that humans had or lack thereof. And it, it took forever, and I don't think that's easily replicatable because, uh, like who else would have that data? You have to have this historic, you know, decades, uh, worth of data.

And now, now the, like the other thing you need is in-infrastructure and the scale, right? Because, uh, w- again, what we found, uh, stat sig results, you need to run a lot of simulations, a lot of agents, and, and it's-- Those are expensive things. Like you're, you're making actions in the browser because you want a real friction.

You want to, to be able to get the image like of what humans will see because you wanna, uh, detect effects like, "Hey, if I make my images larger, will I have more sales or l- uh, fewer sales?" And like usually people's intuition here, by the way, is that I increase my images, I will have more because they look nicer.

You know, designers all look sparse and big images. Like usually your sales tank, right? But, but, uh, you know, from HTML, all the characters look the same only the, the size tag looks different, right? So it's very hard. So you have to take visual information, you have to run this in simulated browser environment on the big farm and, and of course, you have to have, uh, like very, very expensive model, good model with multi-model model.

So all this it's-- is what's taken so long and, uh, to share my personal fail a little bit there, Sean, is like, you know, we always had this bias to-- for like large company bias. You know, we always, uh, whenever you-- we do, we're like, "Hey, we'll run an experiment," right? We make, make a change, and we will run an experiment and then, uh, see, uh, see which one's better or like, "No, this is worse," and most of them are worse, so you discard it and keep iterating, hill climbing.

And we're like, "Oh, like smaller merchants, they cannot get stat sig results. They cannot really run experiments simply because, you know, in a week there would be not enough data for them." So we thought from this perspective. What we didn't realize is that most people don't have A and B, they just have one thing, and they need suggestions of What A and B should be.

So, uh, we first build this, hey, we run simulation on two separate teams and, and, uh, say, "Hey, which one is better?" We then morphed it into, and very recently just released it, when you have just your site, your theme, we run over it and we say, "Hey, here's what predicted values of, of, uh, uh, conversions are, and here's how we think you should modify it to increase your conversions."

And then circling back to what you started with, the proof is in the pudding. Like, if we are not correlating with reality, like, people will not be using it. And, uh, thankfully, we see literally every day more users than the previous day. So, so right now, uh, right now- It's working. Yeah. I'm-- Right now my problem is how to pay for it all because the so our major thing is how to optimize the LLMs, do distillation, how to run the headless browsers, uh, and handful browsers, uh, uh, cheaper so that we can accommodate the increase in traffic.

[00:42:47] **swyx** : Yeah. I, I understand that you, uh, you published a lot of technical detail at GTC, so I was just gonna bring it up a little bit. I think s- was this in, in con-conjunction with some kind of GTC presentation? Or something like that, right?

[00:42:59] **Mikhail Parakhin** : Well, we, yeah, we, we did it in several place, but yeah, we had the engineering- Yeah

blog, uh, as well. Yeah.

[00:43:05] **swyx** : Yeah. So you're running, uh, GPT OSS. Uh,

[00:43:08] **Mikhail Parakhin** : the, this is an older version. You know, now we run multimodal model. But yeah- Yeah ... GPT OSS, we still run GPT OSS as well for

[00:43:15] **swyx** : And then you have the VMs, and you also have browser-based. I really like this one where it you said, "It violates almost every assumption that standard LLM serving is designed for."

And then you had like, basically orders of magnitude differences between everything.

[00:43:29] **Mikhail Parakhin** : Exactly. Which is, which, uh, which was, you know, a bit of a challenge to implement, like when, like even simple things. Uh, be- since it violates all the assumptions, for example, multi-instance GPUs, like MIGs don't work as well.

But we needed, uh, to get MIG to work because, 'cause otherwise it's way too expensive. And so we had to deal with the, yeah, with, uh, lots of infrastructure and, and, uh, work with, uh, uh, Fireworks and CentML, uh, you know, to help with optimizations and browser-based, as you mentioned. Yeah, like, takes a village.

[00:44:04] **swyx** : Okay. So there's a lot of like, I guess, experimentation in the infrastructure so far, and you've published more or less what you have here. I guess I'm, I'm less familiar with CentML. I, I don't do, uh, that much work in this, this part of the stack. But why was it the sort of preferred instance platform?

[00:44:22] **Mikhail Parakhin** : There are really three probably top companies. There used to be, uh, uh- Three top companies, uh, at least I was aware of that did, uh, LM optimization. You know, together Fireworks and Santa ML, not necessarily in that order. Santa ML recently got acquired by NVIDIA. Uh, what they did is if you have a model and you want to optimize it to a specific prof-- uh, profile of usage, uh, they would go and do it.

And, uh, we work with, with those companies, uh, this was work particularly in with Santa ML and NVIDIA to get them the best possible results out of it. And, and sometimes you, you have to retune depending on, like sometimes you want the maximum throughput, sometimes you want minimal latency, sometimes you want like the cheapest, right?

And, yeah, or some combination. And so yeah, these are people who would come and help you.

[00:45:14] **swyx** : I see. I see. Yeah, yeah. I'm familiar with these people for the LLM, you know, autoregressive stack. But the other interesting category of these optimizers is also the diffusion people, whereas like Fel and, you know, uh, Pruna recently has come up a lot as well, which I think is like really underappreciated, uh, at least by myself, because I, I thought, oh, all the workload would be LLMs, but actually there's a lot of diffusion as well.

[00:45:38] **Mikhail Parakhin** : Exactly.

[00:45:38] **swyx** : There's a lot here, so I, I, I... it's, it's, uh, it's, it's, it's hard to cover. But I, I do think like people underappreciate the importance of customer simulation, basically. I think this is something that I'm candidly still getting to terms with. Uh, you know, uh, you also-- your team also like prepared this, like, really nice diagram.

Uh, I, I assume this is AI generated.

[00:46:00] **Mikhail Parakhin** : Yeah, it looks-

[00:46:01] **swyx** : Maybe it's not.

[00:46:01] **Mikhail Parakhin** : Yeah, it looks, uh, Gemini-ish. Yeah, but, uh, uh, honestly, I, I don't know where, where the hell they generated. It looks, look, uh, looks like it's, uh, Google. But the interesting part, John, that, that, uh, we haven't covered, but I, I wanted to mention is if your store had previous customers, rather than it's a new store, you're like new merchant just launching things, it helps tremendously in just correlation and forecast.

Yeah, we take your previous, uh, customer's behavior, and we create agents that replicate those specific distribution of, of customers that you get, and then we a- we apply those to your changes, and then that, that raised raw, you know, the re-- uh, just correlation with the add to cart events or to-- with conversion or whatever it, it, it may be, uh, quite dramatically.

So, uh, replicating humans in general seems like an interesting, cool challenge.

[00:46:58] **swyx** : As a shareholder, I think this is the-- like if people are Shopify shareholders, they should really deeply understand this because this is basically the moat. The, the more you use Shopify, the more it will just automatically improve, right?

Like you're, you're doing the job for them.

[00:47:13] **Mikhail Parakhin** : Yeah, that's what we started with. Like, uh- ... uh, otherwise, if you're just a startup, I wouldn't do it if, uh, you know, if it was my startup because Without the data, it, yeah, as, as you said, it's, it's exactly the case that, uh, whatever you say in prompt, that's, that's what the agents will be doing.

[00:47:30] **swyx** : The statistician in me wants to like really satisfy the sort of, um, statistical intuition, I guess. Um, to me it's kind of, uh, the, the word that comes to mind is, um, ergodicity. Uh, so let's say a, a customer takes this path, customer takes this path, customer takes this path, right? Um, the... In my mind, the way I explain it is like, okay, here, here's the ninety-five percentile, here's the five percentile, and here's the median, right?

Um, but to me, what SimGym is potentially doing is that it can, uh, modify... It can sort of model the sort of in-between sort of journeys as well, that, that maybe are dependent on the previous states. This may be like a very RL-type conclusion where like basically the summary statistics, if you only did naive AB testing, you only have the, the statistics at, at, at a certain point, and you only judge based on the sort of overall summary statistics.

But here you can actually model trajectories. Does that make sense? Or-

[00:48:31] **Mikhail Parakhin** : That makes total sense because like, well, that, that makes even more sense that maybe even you realize bec- because-

[00:48:38] **swyx** : Okay. Please,

[00:48:38] **Mikhail Parakhin** : please. Yes ... we do-- Yeah. The, so internally, uh, we have this system, we talked about it briefly once at NeurIPS.

We have a huge HSTU-based system that models the whole companies, uh, and their possible paths. And like- Yeah ... what you are, what you are showing, like actually at any point of time, you can either model the user's behavior or you mo- can also think about, uh, the whole merchant as a company, as the entity that acts in the world.

You can model that as well. And then you can do, can do counterfactuals. In your graph, like in your blue graph, uh, if you're... Imagine in the center there, uh, somewhere in the middle, you would have an intervention. I give that person a coupon, or I don't know, I send a personal thank you card, or give a discount in some- somewhere.

And then you can, uh, then you can do forward rollouts from that counterfactual. So what would have happened with that intervention or without the intervention? And you can even ch- change where that intervention, uh, in time can happen, right? Like some- where, where in this journey. So we, we do this at the Shopify scale for our merchants, and then if we notice that something that they can be fixing, like there's a strong counterfactual, like we have Shopify policy, they basically get a notification like, "Hey, we think your...

something is wrong with your-" I don't know, Canadian sales. Like, uh, it looks like it's misconfigured. Here's what you need to do. Or do you think like, uh, you have to set up this campaign with these parameters? And we do that at the buyer level to literally offer discounts or cashback or, or things to buyers.

So this is-- I'm getting very excited. Like this is my sort of area of, uh, interest, I guess, and, and hobby. But being able to m-model something complex as human beings or companies and model counterfactuals on it, where you can have interventions in the future and optimize when to make intervention, what kind inter-- uh, what kind of intervention to make.

It's such an unlock that previously was completely impossible. Like the-- it was, it was always dreamed of, but never... Like how would you even simulate it without LLMs or HTUs? I think very, very exciting times.

[00:50:59] **swyx** : I just wanted to, uh, to maybe illustrate this. I, I'm not the best illustrator, but I, I am a conceptual statistics guy.

And y-you know, you cannot just do this. Like this is a dimensionality AB test doesn't do, right? Like, uh, because it doesn't have the, the, the change over time, uh, stochastic nature, uh, and it doesn't have the sort of contextual like... Here's all the context to this point. Um, okay, cool. Um, that's SimGym.

You're, you're gonna burn a lot of tokens on this thing. But you're, you're one of the, the only scale platforms in the world that can, uh, that can do this across a huge variety of workloads, right? I'm even curious on a sort of human, uh, research level of like, well, do, does retail behave d-differently from like clothing sales?

D-does that behave differently from electronic sales? I, I don't know. I don't know what else you guys... The Kardashian shoppers, do they differ from like people who buy, uh, I don't know, cars and, uh, whatever.

[00:51:55] **Mikhail Parakhin** : Well, very different, and different sensitivities and different modes of, uh, shopping and, and different levels of what's important.

Now, to-totally, you can do aggregations at, uh, at a store level. You can do aggregations at a different, uh, category level. I don't know if, uh, you know, for our statisticians among us, I couldn't believe, but we-- recently we're looking at it, and we had to bring back, uh, CRPs, you know, Chinese restaurant process.

It's a, like, way of aggregating and, like, naturally grow clustering. So across... Specifically to answer questions that, uh, like you were just posing on how, how if, if buyers behave different categories. And I'm like, "I haven't seen CRP since two thousand and one." It's

[00:52:37] **swyx** : so What? It's so- What is... No, I haven't, I haven't seen this.

No. This is not in my training. Uh,

[00:52:44] **Mikhail Parakhin** : but, but yeah, it, uh, uh, it actually, like the, the-- there was a very popular kind of theory, popular neurips HTML circles in early two thousands, uh, kind of nice. And now, now it has practical applications, uh- Yeah ... that we were resurrecting.

[00:53:03] **swyx** : Yeah, amazing. Uh, I, I can see, I can see how this is like a, uh, a fun job for you where you get to apply all these things.

Um, yeah, yeah, so super cool. Super cool. So, okay, so, so anyone who, who knows what CRPs are and has always wanted to use them at work, uh, they should, they should definitely join Shopify. Okay, so w-we have a lot and but I, I'm, I'm being mindful of the time. I, I do wanted to, to sort of cover some other things.

Um, I-I'll give you a choice, UCP or Liquid?

[00:53:30] **Mikhail Parakhin** : Liquid. I think, I think on UCP, you know, like UCP is very important for us and, and it just we are-- UCP, we have a structured, uh, discussions, and you can read about them, and we have, uh, blog posts, and we have a big release this week, in fact, like with our catalog.

Oh,

[00:53:46] **swyx** : okay.

[00:53:46] **Mikhail Parakhin** : Uh, yeah,

[00:53:46] **swyx** : but- Le-I mean, we, we can, we can discuss the, the, the release briefly because we'll release this after the-- after it's already announced so whatever. There's a catalog that you guys are doing?

[00:53:55] **Mikhail Parakhin** : Yeah. So we are, we are- Okay ... we are bringing in capabilities of a whole, uh, Shopify catalog.

Basically, you now you can search for products, you can do lookups by specific ID, you can do bulk lookups when you need to bring m-multiple products. You don't need to know in ad-in advance what you're trying to show or to sell or check out. Like, you can now, you can now have this decided at, at runtime, and this big area for investment for us for both non-personalized and personalized searches, trying to provide basically a win-window into whole universe of products that are being sold everywhere in the world.

And Shopify is really not exactly, but almost like a super set of any-anything being sold. Now we are bringing it into UCP and, uh, and, uh, identity linking is another big thing for us, uh, so that you, you can use, uh, like Google or whatever, whatever identity you have, uh, they're minimizing friction.

[00:54:56] **swyx** : Yeah. So

[00:54:57] **Mikhail Parakhin** : yeah, big release for us.

But Liquid AI of course we never talk about, and the problem might be more, more aligned with what we d-discussed previously on this chat.

[00:55:07] **swyx** : Sure. The main thing that everyone understands about Liquid is that it is inspired by Worm, and I still don't know why. I'm curious on your explanation. I think you, you, uh, you can make things very approachable.

And also I think like what is the potential of like the, the level of efficiency that you get out of Liquid?

[00:55:23] **Mikhail Parakhin** : You- we all familiar with transformer architectures. And, uh, for the longest time, there was a competing architecture, it's called the state space models. So, so Sams, uh, you know, Chris, Chris Reyes, one of the pioneers and, and lots of startups, uh, trying to make those realities.

They have, uh, significant benefits being main being, uh, being much faster and, uh, lower footprint and not quadratic in length, you know, sort of, uh, linear in, in, uh, in your context length. But with state space models- They never quite made it. Like they're used-- They have, uh, certain niches when they thrive, their hybrid architectures are useful, but they never quite made it.

And liquid neural networks are, you can think of them as a next step, like, uh, sort of, uh, state-space model square. It's non-transformer architecture that's more complicated than sta-state space and really difficult to code if you-- if I'm being honest. But it's, um, very efficient. It's, uh, subline-- sub, uh, quadratic in, in length of your context.

Uh, it's very compact way to represent things, and that's a liquid AI company. They... Their goal is to productize it, and very often you have this need, uh, when you need to have long context and small model, and you want to have low latency. Like in general, it's basically on par with transformers, and if you do hybrids with transformers, it's, it's even better.

That's why we at Shopify, when we tried multiple and we constantly try multiple models, multiple companies, we found that for small, particularly with low latency applications, when you have low latency and/or if you need longer context lengths, liquid was the best. And so we still use the whole zoo and always like obviously test and use everything, uh, every open source model and, you know, it feels like sometimes even every private model.

Uh, but liquid's been taking quite a bit of, uh, at least internal Shopify share. And the reason I'm excited is, yeah, because it's, it's the only non-transformer architecture that I found being genuinely competitive. Uh, and, uh, you know, for we use it for search and for, for long context, uh, pulse distilling and others.

This is the overview. I don't know how approachable Sha, sorry. Maybe, maybe still too obtuse.

[00:57:51] **swyx** : I, I mean, I think they haven't been that open about their implementation details. I think the... I would say like liquid hasn't been like if there's a lot of technical detail published, I haven't read like a, a formal sort of paper on the implementation details.

Uh, but I, I did get the sort of relationship between the SSMs and the others. This is one of the sort of, uh, charts that was, you know, showing the relationship between like full attention versus Something that's, uh, more like a RNN type in terms of their, their efficiency. Um, and then the, the other chart was this old one, uh, where it compares versus, uh, some of the other models.

Uh, doesn't exactly have the correct Y-axis, but close enough where you can see like it's basically a, a step change difference in terms of the efficiency. I think the surprise to me was that you guys are, uh, actively using it already in internally inside of Shopify. And like I, I'm curious, like what are the constraints that you're optimizing for, right?

Is it when you say smaller, is it like the 1B size? Uh, what kind of like latency constraint are you, are you optimizing for? What kind of context length, um, sort of considerations, right? Like I think for example, right, like in the audio kind, kind of use cases, the SSMs ef-effectively have unbounded context length because they, they just have to operate on like the most, the sliding window of the most recent stuff.

Uh, I'm just kinda curious, like w-what do you see the potential here?

[00:59:13] **Mikhail Parakhin** : Yeah. The SSMs are effectively because, yeah, because the state embeds all the, all the previous information needed, or that's the assumption. SSMs effectively have infinite context length. The, the problem with, uh, with them is that expressiveness is not there.

The, uh, uh, Liquids are effectively souped up SSMs. We are much more expressive, m-uh, com-more complicated again to code. There is, there is a paper on it. You can, you can see it. Differential equation rolled out and, and then computed as a, uh, as really as a convolution. It's a bit involved. The thing where we, we use it is specifically either for where we need super low latency, and we're-- there was a lot of very fun project with, uh, Santa ML and Liquid AI themselves.

We run it at, uh, thirty milliseconds, a, a tiny model, like three hundred million parameters in, but we run it in thirty milliseconds, uh, end to end for search when you, when you type a query, and then we produce all the possible things what you, what you can mean by that query and some, you know, uh, not only synonyms, but, but, uh, a que-kind of full query understanding the, the whole tree of what you might need and including your personal personalization because you might have done like previous queries and lowering it all down into the search server so that the requirements on latency obviously they are very, uh, very strict.

So, so then we are able to run it under thirty milliseconds because, 'cause at Liquid, you know, Qwen doesn't run on this. And even Liquid, we had to work a lot with NVIDIA and to... because almost everything is not designed in CUDA for or in, in the current stack for, for low latency. Like small things that don't matter with large models, you know, start mattering a lot, and we had to optimize it.

There is different end of the spectrum where this is maximum through, uh, bandwidth throughput for things like, for example, offline categorization when A new product appears. We need to do analysis. We need to assign where it is in taxonomy. We need to extract and normalize attributes. We need to do, uh, you know, clusters like, oh, it's the same thing as that other merchant is selling, right?

That is like un-- like almost unbounded, uh, amount of energy you need to spend on it because it's, uh, you know, it's quadratic kind of, uh, problem, and we have billions and billions of products. So you don't care about latency as much. You know, it's kind of an overnight batch job, but you, you want to maximum throughput.

And you usually in those cases, you also sometimes like for, uh, Sidekick Pulse, you also need long context. These are... We are talking models in maybe seven, eight billion, uh, parameter range, uh, where we would, we would take a large model, like we would take something huge, largest we can, we can find. We would distill into liquid for a specific task, such as, for example, for our catalog, uh, formulation or for, for Pulse.

And then we run it at a very large scale, like in batch jobs. Because just running... And, and it beats in that situation beat very often beats, uh, Qwen or, yeah, Kimi is more on the reasoning side. So Qwen, Qwen I would say is probably their major alternative. That's when we use it. I mean, not a, not a panacea, not, not really, uh, I wouldn't say that it's frontier model in the sense of it's not gonna suddenly compete with, uh, GPT 5.4.

Uh, but, but, uh, uh, it is a phenomenal target for distillation, which is right now becoming more and more important with, uh, explosion of token usage.

[01:03:00] **swyx** : Is that a, a now only thing or do you think you give Liquid a hundred billion dollars and they will do... Is it, is it just more scale or like what, what is limiting it?

You know, what prevents it from running into the same issues that SSMs had?

[01:03:14] **Mikhail Parakhin** : Their scale is already much larger than the largest SSM I, I'm aware of. Uh, uh- Wow, okay. So yeah. So, uh, SSM was just, was just not expressive enough or in my opinion. Like, um, again, I'm sure I've-- I'll get a lot of pushback and probably accurately so.

But in my opinion, SSMs are not expressive enough and, uh, liquid models are. I think, uh, especially in their hybrid form when with combined with the transformer, like in Mamba fashion, they probably the best architecture I'm aware of like period. But of course, Liquid AI is not at the scale of, uh, you know, Anthropic or, or Google or OpenAI in terms of compute.

So I don't think, uh, they... I think if, if they, uh, if they had similar level of compute, they, they would be very competitive and maybe even beat the, uh, the largest models, at least from what I've seen. They don't have, uh, this level of, uh, investment But they still have decent investment and, and it's, uh, it's, uh, definitely for this scenario of smaller models and distilling into their second to none very often.

We are very omnivorous, and we're on purely merit-based. So the moment they will start being competitive, we're like, we will switch to something else, and we constantly test. But, but so far, if you see progression, if I draw a graph of our workloads on Liquid versus our workloads on, I would say Qwen, which is another awesome model and probably, uh, another kind of standard within Shopfy, I would say, uh, Liquid's been definitely taking share

[01:04:48] **swyx** : I think that's very promising and probably the best explanation I've heard, uh, directly from, from someone involved in Liquid.

Um, I, I do have Maxime Lebon coming to, uh, my conference in London, uh, this week, so I, um, we'll- Oh, that's great ... hear more from him. I-- 'cause, uh, there was this, like Liquid, uh, investor day or something like a, a year or, or a year and a half ago, and I, I think there just wasn't that much technical detail that I think was, was sort of speaking to my crowd of like potential customers and users, right?

Which like, yeah, it's fine. Like, you know, maybe, maybe, uh, there, uh, we, we still need to wait for more results that come out, uh, before, before this. But I think it would be news to a lot of people that you guys are actually actively already using it for high-frequency use cases. I also wanted to highlight Psychic Pulse, which, uh, we didn't cover, and we probably don't have time to cover, but it's something that you also launched, uh, recently.

Basically REXIS, um, but also something that like I've-- the, the other REXIS trend I've been c- I've been covering a lot, uh, from like the YouTube side, even xAI's, uh, REXIS has been LLM-based REXIS, right? Uh, which I think you are also effectively using liquid models for, but they are just throwing transformers at, at the problem.

And maybe this is, uh, eh, the sort of hybrid architecture shift that will happen in order to accommodate the kind of long context and, and lo- and high efficiency that, that you need. I don't really have a strong opinion there, like apart from I would highlight to anyone the, the, the work that the LLM base-- LLM-based REXIS community is doing is, is also very interesting there.

[01:06:22] **Mikhail Parakhin** : Yeah. The-- again, the thing to get you excited is that it's not just LLMs looking at things, it's also HSTU model doing that counterfactual analysis- Yeah ... where we model the whole, uh, enterprise as an entity and, and its actions and then see what, what will, what will happen.

[01:06:39] **swyx** : Overall, I think it, it pre-- this all presents like, uh, an enormous like...

I think, uh, you know, uh, there, there was not that deep of a AI story to Shopify when it started. Uh, it was just a WordPress plugin, right? But now, you know, you are the sh- the, the storefronts, uh, e-commerce, you know, uh, guardians to s- like so many, so many people, and you're, you're really like applying all the AI, uh, methods and the state-of-the-art stuff.

Uh, so like I, I think, you know, our conversation like today has like really, uh, oh, I guess opened my eyes to a lot. So thank you for doing this. Uh, this is a really amazing, um, overview of, uh, what you're doing.

[01:07:15] **Mikhail Parakhin** : Okay. Thank you for saying that, Shawn, and, uh, thank you for having me. Of course, it's always a pleasure to talk to people who, you know, deeply technical and know what they're talking about.

[01:07:25] **swyx** : Yeah. I mean, uh, very few people are as technical as you but at least I can, I, I can like somewhat fo-- uh, vaguely follow along. Yeah. So, so, okay, um, there, there is a hi- there's a hiring call, uh, you know, uh, any, any particular roles that you're looking for that you're like, "Okay, if you know the-- how to solve, um, this problem, uh, reach out"?

[01:07:45] **Mikhail Parakhin** : Yeah. Uh, the, the things I would definitely call out that if you're an ML person or if you're data science person and, uh, uh, we, we, we have huge need for more, more people munching data, so to speak. Or surprisingly, if you're a distributed database person and, uh, uh, you know, we, we think that there is a way to use LLMs to reimagine how we do distributed databases, and we're working a lot with Yugabyte there.

And so if you're-- have interest in those areas, we've-- like ShortFi might be the best place in the world for you. That's pretty good place for other, you know, other disciplines as well.

[01:08:24] **swyx** : Cool. Um, I think that that was all the questions I had. I said I, I have one sort of a bonus thing if you, if you wanna indulge in, uh, some Bing history.

What is your, uh, I guess, takeaways or any, any fun anecdotes about Sydney?

[01:08:38] **Mikhail Parakhin** : Any fun anecdotes about Sydney? Well-

[01:08:41] **swyx** : Yeah, it was a very interesting, you know-- I, I think it, like, woke up people to, like, this personality that, that, that it w-- emerged.

[01:08:48] **Mikhail Parakhin** : The, the funny thing, like, I mean, the, the most interesting anecdote is that Sydney was first shipped, uh, in India for, uh-- and, uh, it was, uh, not noticed for a long time.

And first implementation of Sydney didn't even have OpenAI model under it. It was, it was, uh, Turing Megatron, um, Microsoft, uh, and NVIDIA collaboration model. Uh, and there were, uh, yeah, exactly. That's, that's the, that's the one people thought it was a prank, uh, because it was, like, not many people were familiar with the LLMs at, at that point yet, and thought like, "That cannot be automatic.

You, you must have, uh, you know, people thinking." And then even they were complaining that, "Oh, the-- my-- this, this chatbot is gaslighting me." And then, then people like what, what almost everybody doesn't fully realize is that it wasn't by accident that, uh, Sydney was Sydney. I mean, we spent a lot, a lot of effort on personality shaping.

Uh, we-- I mean, it, it was a bit of my Yandex legacy, where previously we did this Alice, uh, uh, digital assistant, uh, which we learned the- Chatbot, yeah ... yeah. We, we learned the importance of, uh, personality shaping, and so here we brought, did a lot of personality shaping. Uh, so it was not fully an emerging scenario.

It was, it was also a little bit edgy. What, what we learned in, in those experiments is you want to be polite, but you want to be a little bit on edge, and that draws people in. I haven't seen, ever since the, uh, kind of those days, I haven't seen anybody trying exactly that mode. I think we will see, we will see more of this at some point, but, uh, yeah.

A lot, lots of good memories, you know. And by the way, the very first Sydney dev lead Is, uh, uh, Andrew McNamara is working in ShopFind, uh, and the head of Sidekick and, and our-- and the Pulse- Oh. And lots of these are actually, yeah, in his pur-purview.

[01:10:53] **swyx** : Oh, okay. Uh, I-- That, that's another fun fact. You're, you're- Yeah

assembling the team again. Yeah. Yeah, it's cool. Like, I think a lot of, uh, people woke up to the, the idea of AI personality for the first time there. And, like, I think now with maybe OpenClaw, like explicitly prompting a, a fun personality, I think that, that is a real selling point for, for people, right? And then I, I guess maybe the only other time that it's like really emerged into public consciousness is Go to Gate Clawed.

But yeah, I think, uh, you know, hopefully someday we'll get Shopify Sydney.

[01:11:23] **Mikhail Parakhin** : Well, we have Sidekick. It's a- Yeah ... it's a different, different thing a little bit. Yeah.

[01:11:28] **swyx** : Yeah. Si-Sidekick was like your, your original big launch for, for AI stuff. Uh, yeah, cool. Uh, amazing. Uh, thank you so much. You guys do amazing work.

Uh, honestly, if I was a Shopify customer, Shopify investor, um, hearing all the work that you guys are doing o-on this technical side, it, like, m-makes me feel more confident in like, okay, just choose Shopify, right? Like, like you're never gonna do this in-house, which is obviously what you want. But like, uh, yeah, I mean, like, that-that's, that's what an ideal platform is, like, that you're doing all the things that no individual could do at their scale, but you can at your scale.

Uh, very exciting problems.

[01:12:01] **Mikhail Parakhin** : Exactly. Exactly. Yeah. And creating network effect and hard to disagree. If you're not using Shopify, you should.

[01:12:09] **swyx** : Yeah, amazing. Okay, well, that's it. Thank you so much.

---

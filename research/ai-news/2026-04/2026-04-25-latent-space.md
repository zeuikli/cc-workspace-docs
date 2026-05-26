# 🔬 Latent Space — 2026-04-25

> swyx 開發者簡報，未公開專案 + 工程視角
> 來源：[Latent Space](https://www.latent.space/feed)

---

## [[AINews] DeepSeek V4 Pro (1.6T-A49B) and Flash (284B-A13B), Base and Instruct — runnable on Huawei Ascend chips](https://www.latent.space/p/ainews-deepseek-v4-pro-16t-a49b-and)
*🔬 Latent Space | 2026-04-25*

After a couple months’ delay and lots of speculation, [DeepSeek finally released the heavily anticipated DSV4](https://x.com/deepseek_ai/status/2047516922263285776?s=20), the first major version model since DSV3 (Dec 2024) and DSR1 (Jan 2025). It brings the DeepSeek family up in line with [Kimi K2.6](https://www.latent.space/p/ainews-moonshot-kimi-k26-the-worlds?utm_source=publication-search), the current open model leader, and [Xiaomi Mimo 2.5](https://x.com/ArtificialAnlys/status/2047799218828665093?s=20), a lesser known family [released 2 days ago](https://x.com/XiaomiMiMo/status/2046988157888209365?s=20).

The DSV4 family is roughly a Gemini 3.1, GPT 5.4, Opus 4.6 level model, up to 1.6T MOE withtrained on 32T tokens with [FP4](https://x.com/iscienceluvr/status/2047514399393579235?s=46), with 1M token context (supported by their new Compressed Sparse Attention (CSA) and Heavily Compressed Attention (HCA) techniques), and incredibly rarely, they released both the Base and Instruct versions - surely setting the stage for a possible “DeepSeek R2” in future, though this one already has reasoning effort.

The [technical report](https://huggingface.co/deepseek-ai/DeepSeek-V4-Pro/blob/main/DeepSeek_V4.pdf) is a typically dense 58 pages, demonstrating training and inference insights and improvements from [the Manifold Constrained Hyper-Connections (mHC) paper](https://arxiv.org/pdf/2512.24880) they released in January, continued usage of [Moonshot’s Muon](https://news.smol.ai/frozen-issues/25-07-11-kimi-k2.html), and CSA/HCA’s overall INCREDIBLE efficiency improvements on [DeepSeek 3.2-Exp’s already impressive Sparse Attention](https://news.smol.ai/frozen-issues/25-12-01-deepseek-32.html) - at 1M tokens, requiring only 27% of FLOPs and 10% of KV cache memory compared with DeepSeek-V3.2:

The geopolitical backdrop behind the [Huawei CANN compatibility](https://x.com/jukan05/status/2047823601462812932) is DeepSeek weaning dependence off export-controlled NVIDIA/CUDA chips — Ascends are still [a quarter the supply](https://x.com/PalwinderCFA/status/2047614823102619974) of H100s, but this is an important milestone for Chinese total independence.

AI News for 4/23/2026-4/24/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews’ website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

AI Twitter Recap

Top Story: DeepSeek V4

DeepSeek released DeepSeek-V4 Pro and DeepSeek-V4 Flash, its first major architecture refresh since V3 and first clear two-tier lineup, with 1M-token context, hybrid reasoning/non-reasoning modes, an MIT license, and a technical report detailed enough that multiple researchers called it one of the most important or best-written model papers of the year. Across the reactions, the factual consensus is that V4 materially advances open-weight long-context and agentic coding performance while remaining somewhat behind the top closed frontier models overall. Independent benchmarkers place V4 Pro around the #2 open-weights tier, roughly near Kimi K2.6 / GLM-5.1 / strong Claude Sonnet-class to Opus-ish depending on benchmark and mode, with especially strong long-context and agentic performance; opinions diverge on how close it is to GPT-5.x / Opus 4.7 and on whether this is “democratizing” progress or an architecture so complex that few open labs can realistically reproduce it. Key sources include deep-dive commentary from [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2047735160544841953), [@scaling01](https://x.com/scaling01/status/2047618271310926151), [@nrehiew_](https://x.com/nrehiew_/status/2047665987730993363), [@ben_burtenshaw](https://x.com/ben_burtenshaw/status/2047646980139016560), [@TheZachMueller](https://x.com/TheZachMueller/status/2047702488418030066), [@ZhihuFrontier](https://x.com/ZhihuFrontier/status/2047664976215839021), and infra/vendor posts from [@vllm_project](https://x.com/vllm_project/status/2047843293447500069), [@NVIDIAAI](https://x.com/NVIDIAAI/status/2047765637808664759), and [@Togethercompute](https://x.com/togethercompute/status/2047743446522224987).

Core facts and technical details

The most concrete technical claims repeated across the discussion:

Two models

V4 Pro: 1.6T total parameters / 49B active

V4 Flash: 284B total / 13B active

Reported by [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2047735160544841953), [@teortaxesTex](https://x.com/teortaxesTex/status/2047630981364883816), [@baseten](https://x.com/baseten/status/2047779549644243146), [@NVIDIAAI](https://x.com/NVIDIAAI/status/2047765637808664759)

Context

1M tokens, up from 128K in V3.2 per [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2047735160544841953)

Multiple posters frame this as the headline achievement: “solid ultra-long context” [@teortaxesTex](https://x.com/teortaxesTex/status/2047623905754448043)

Training scale

32T–33T tokens cited repeatedly

[@nrehiew_](https://x.com/nrehiew_/status/2047666048334450754) notes 32T tokens over 1.6T parameters, i.e. roughly 20 tokens/parameter

[@teortaxesTex](https://x.com/teortaxesTex/status/2047630981364883816) cites 33T

[@nrehiew_](https://x.com/nrehiew_/status/2047840706874749076) estimates pretraining compute at ~1e25 FLOPs

Reasoning / modes

DeepSeek exposes three reasoning modes per [@Togethercompute](https://x.com/togethercompute/status/2047743446522224987)

Hybrid “thinking/non-thinking” positioning noted by [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2047735160544841953)

Long-context architecture

Several threads summarize a new hybrid attention system:

shared KV vectors

compressed KV streams

sparse attention over compressed tokens

local/sliding-window attention for nearby context

[@ZhihuFrontier](https://x.com/ZhihuFrontier/status/2047664976215839021) gives the most compact public summary:

2× KV reduction via shared key-value vectors

c4a ≈ 4× compression

c128a ≈ 128× compression

top-k sparse attention on compressed tokens

128-token sliding window

1M context KV cache = 9.62 GiB/sequence (bf16)

8.7× smaller than DeepSeek V3.2’s 83.9 GiB

FP4 index cache + FP8 attention cache gives another ~2× reduction

[@ben_burtenshaw](https://x.com/ben_burtenshaw/status/2047646980139016560) condenses this to “10× smaller KV cache”

[@TheZachMueller](https://x.com/TheZachMueller/status/2047702488418030066) and [@TheZachMueller](https://x.com/TheZachMueller/status/2047702996524405175) describe CSA + HCA layer patterns, with alternating layers and V4 Flash using sliding-window layers instead of HCA in some places

Quantization / checkpoint format

[@LambdaAPI](https://x.com/LambdaAPI/status/2047654086263320965): checkpoint is mixed FP4 + FP8

MoE expert weights in FP4

attention / norm / router in FP8

claim: the full model fits on a single 8×B200 node

Inference hardware / serving

[@NVIDIAAI](https://x.com/NVIDIAAI/status/2047765637808664759): on Blackwell Ultra, V4 Pro can deliver 150+ TPS/user interactivity for agentic workflows

[@NVIDIAAI](https://x.com/NVIDIAAI/status/2047823093578518758): published day-0 V4 Pro performance pareto using vLLM

[@SemiAnalysis_](https://x.com/SemiAnalysis_/status/2047726025748930687): day-0 support and benchmarking across H200, MI355, B200, B300, GB200/300

[@Prince_Canuma](https://x.com/Prince_Canuma/status/2047685898163147125): DeepSeek4-Flash on 256GB Mac

[@Prince_Canuma](https://x.com/Prince_Canuma/status/2047847095466385899): MLX quants published

[@simonw](https://x.com/simonw/status/2047844236142497850) asks about smaller-RAM Mac viability, implying community interest but incomplete support story

[@QuixiAI](https://x.com/QuixiAI/status/2047765475937890474) reminds users that many local stacks still lack tensor parallel, relevant because V4-class models strongly stress inference infra

License / availability / pricing

MIT license per [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2047735160544841953)

first-party API plus rapid third-party availability via [@Togethercompute](https://x.com/togethercompute/status/2047743446522224987), [@baseten](https://x.com/baseten/status/2047779549644243146), [@NousResearch](https://x.com/mr_r0b0t/status/2047673600900010044), [@Teknium](https://x.com/Teknium/status/2047798102091067677)

V4 Pro pricing: $1.74 / $3.48 per 1M input/output tokens

V4 Flash pricing: $0.14 / $0.28

cache-hit pricing also given by [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2047735160544841953)

[@scaling01](https://x.com/scaling01/status/2047707820552831028) views the pricing as a glimpse of future “Mythos-level” cheap coding models

Reuters-via-posted quote from [@scaling01](https://x.com/scaling01/status/2047760776769720360): DeepSeek said Pro pricing could fall sharply once Huawei Ascend 950 supernodes are deployed at scale in H2

Independent evaluations and where V4 lands

The most useful independent benchmark synthesis came from [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2047735160544841953):

V4 Pro Max: 52 on Artificial Analysis Intelligence Index

up 10 points from V3.2 at 42

becomes #2 open weights reasoning model, behind Kimi K2.6 (54)

V4 Flash Max: 47

positioned around strong mid/high open models, “Claude Sonnet 4.6 max level intelligence”

GDPval-AA (agentic real-world work):

V4 Pro: 1554, leading open-weight models

ahead of Kimi K2.6 (1484), GLM-5.1 (1535), MiniMax-M2.7 (1514)

AA-Omniscience

V4 Pro: -10, an 11-point improvement over V3.2

but still paired with 94% hallucination rate

V4 Flash: 96% hallucination rate

Cost to run AA Index

V4 Pro: $1,071

V4 Flash: $113

Output tokens used on AA Index

V4 Pro: 190M

V4 Flash: 240M

This is a major caveat: cheap per-token pricing does not imply cheap total task cost if the model spills huge token volumes

Additional eval perspectives:

[@arena](https://x.com/arena/status/2047714237502677405):

#2 open in Text Arena overall at debut

category wins/placements:

#1 Medical & Healthcare

#15 Creative Writing

#18 Multi-Turn

thinking variant:

#8 Math

#9 Life/Physical/Social Science

[@arena](https://x.com/arena/status/2047774037204742255) emphasizes the Pro vs Flash tradeoff:

Pro ranks ~30 places higher

costs 12× more

Flash is still competitive in Chinese, medicine, math

[@scaling01](https://x.com/scaling01/status/2047682465624445015):

“~Opus 4.5 estimate holds for now, at least on SimpleBench”

[@scaling01](https://x.com/scaling01/status/2047733998714052819):

V4 is “definitely better than GLM-5.1 but not quite Opus 4.7, GPT-5.4 or Gemini 3.1 Pro”

[@scaling01](https://x.com/scaling01/status/2047686712051048598) lists what scores would confirm <6 month gap:

ARC-AGI-1 ~75%

ARC-AGI-2 ~35%

GSO ~26%

METR 4.5–5 hours

WeirdML ~63%

[@TheZachMueller](https://x.com/TheZachMueller/status/2047719857869791352):

on his evals, Flash@max ≈ Pro@high on reasoning

Pro focuses more on knowledge (SimpleQA)

[@VictorTaelin](https://x.com/VictorTaelin/status/2047818978664268071):

after fixing benchmark bugs and letting long-running models run longer, DeepSeek and Kimi improved materially

[@mbusigin](https://x.com/mbusigin/status/2047707082007220393):

a simple negative early impression with no detail

[@petergostev](https://x.com/petergostev/status/2047773402090426548):

on BullshitBench, not about capability but refusal/pushback behavior, GPT-5.5 underperformed; included here because many readers compare V4 in an eval-skeptical environment

Facts vs opinions

Facts / relatively well-supported claims

V4 Pro / Flash were released with the specs above, MIT-licensed, 1M context, and open technical documentation: [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2047735160544841953), [@TheZachMueller](https://x.com/TheZachMueller/status/2047626252425515240)

The architecture introduces a new long-context attention system with dramatic KV-cache reduction: [@ZhihuFrontier](https://x.com/ZhihuFrontier/status/2047664976215839021), [@ben_burtenshaw](https://x.com/ben_burtenshaw/status/2047646980139016560)

Independent benchmarkers broadly place V4 Pro near the very top of open weights but below the best proprietary models overall: [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2047735160544841953), [@arena](https://x.com/arena/status/2047714237502677405), [@scaling01](https://x.com/scaling01/status/2047733998714052819)

DeepSeek V4 is heavily token-intensive in some evaluations: [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2047735160544841953)

The checkpoint uses FP4/FP8 mixed precision and can fit on an 8×B200 node: [@LambdaAPI](https://x.com/LambdaAPI/status/2047654086263320965)

Rapid ecosystem support arrived via vLLM and other providers day 0: [@vllm_project](https://x.com/vllm_project/status/2047843293447500069), [@SemiAnalysis_](https://x.com/SemiAnalysis_/status/2047726025748930687)

Opinions / interpretation

“V4 is ~4–5 months behind the frontier” from [@scaling01](https://x.com/scaling01/status/2047618271310926151), [@scaling01](https://x.com/scaling01/status/2047622501241434581), [@scaling01](https://x.com/scaling01/status/2047626000091971811) is an informed estimate, not a measured fact

“Top three open” vs “only open model close to frontier” debate from [@teortaxesTex](https://x.com/teortaxesTex/status/2047616662879248828) is partly about benchmark trust and framing

“Strongest pretrained model we have” from [@teortaxesTex](https://x.com/teortaxesTex/status/2047630981364883816) is an opinion hinging on scale + architecture, not direct benchmark supremacy

“Most significant AI paper of the year” from [@Dorialexander](https://x.com/Dorialexander/status/2047632551326413109) is enthusiasm, not consensus

“This is what research should look like” from [@scaling01](https://x.com/scaling01/status/2047643722108579936) speaks to transparency/style rather than only capability

“Not exactly a democratizing technology” from [@teortaxesTex](https://x.com/teortaxesTex/status/2047840426371977467) is a strong architectural/political interpretation

Different opinions and fault lines

1) Is V4 near frontier, or clearly behind?

More favorable

[@scaling01](https://x.com/scaling01/status/2047618271310926151): puts it at roughly GPT-5.2 / Opus 4.5+ tier

[@scaling01](https://x.com/scaling01/status/2047682465624445015): SimpleBench supports ~Opus 4.5

[@teortaxesTex](https://x.com/teortaxesTex/status/2047630981364883816): argues it is the strongest pretraining base among opens and implies people are underestimating what post-training can do

More skeptical

[@scaling01](https://x.com/scaling01/status/2047733998714052819): below Opus 4.7 / GPT-5.4 / Gemini 3.1 Pro

[@scaling01](https://x.com/scaling01/status/2047622501241434581): the gap may widen again because closed labs have bigger models, better science/law/medicine coverage, faster inference with GB200s

[@mbusigin](https://x.com/mbusigin/status/2047707082007220393): early impressions “not great”

[@teortaxesTex](https://x.com/teortaxesTex/status/2047616897256947967): says polished models like K2.6 and GLM 5.1 may still feel better in coding despite lower intrinsic capacity

2) Is V4’s real contribution model quality, or long-context systems design?

A big split in reactions is that many technical readers think the long-context architecture matters more than the raw benchmark position.

[@teortaxesTex](https://x.com/teortaxesTex/status/2047623905754448043): “They’ve completed their quest: Solid Ultra-Long Context”

[@ben_burtenshaw](https://x.com/ben_burtenshaw/status/2047646980139016560): first open model where long context and agentic post-training “meet”

[@scaling01](https://x.com/scaling01/status/2047618271310926151): expects other open labs to adopt pieces of the architecture

[@Dorialexander](https://x.com/Dorialexander/status/2047632551326413109): frames Huawei/sovereignty constraints as an opportunity to reshape hardware and memory/interconnect design

[@jukan05](https://x.com/jukan05/status/2047861732702662741): reads the paper as evidence that NVIDIA’s hardware roadmap is unusually well aligned to where MoE/long-context models are going

3) Is V4 “open democratization,” or too hard to copy?

This was one of the sharpest strategic disagreements.

[@teortaxesTex](https://x.com/teortaxesTex/status/2047840426371977467): says V4 is “not exactly a democratizing technology” because the architecture is too difficult for most labs to replicate

[@teortaxesTex](https://x.com/teortaxesTex/status/2047648219081974034): suggests even DeepSeek may not want to do this exact architecture again without refactoring

[@stochasticchasm](https://x.com/stochasticchasm/status/2047697372831183245): notes the sheer hyperparameter complexity is daunting

Against that, [@Prince_Canuma](https://x.com/Prince_Canuma/status/2047685898163147125) and [@Prince_Canuma](https://x.com/Prince_Canuma/status/2047847095466385899) show that the ecosystem is already compressing and adapting Flash for localish Apple Silicon use, softening the “not democratizing” claim on the inference side if not the training side

4) Are people underrating Flash?

Several reactions suggest Flash may be more important than Pro for practical adoption.

[@arena](https://x.com/arena/status/2047774037204742255): Flash shifts the price/performance frontier

[@TheZachMueller](https://x.com/TheZachMueller/status/2047719857869791352): Flash@max ≈ Pro@high on reasoning tasks

[@teortaxesTex](https://x.com/teortaxesTex/status/2047864952862458009): benchmarks may underweight “legit 1M context for pennies”

[@Prince_Canuma](https://x.com/Prince_Canuma/status/2047685898163147125): Flash runs on 256GB Mac

[@baseten](https://x.com/baseten/status/2047779549644243146) and [@Togethercompute](https://x.com/togethercompute/status/2047743446522224987) emphasize long-document analysis and agentic use cases where Flash’s economics matter

China, chips, Huawei, and sovereignty context

DeepSeek V4 was not discussed as a pure model release; it was treated as evidence in the larger US–China compute and sovereignty debate.

[@scaling01](https://x.com/scaling01/status/2047625331339661685): Chinese labs are already in or near “takeoff” in the sense that their models help build better models, though still shifted 5+ months behind

[@scaling01](https://x.com/scaling01/status/2047622501241434581): thinks chip bans are likely to widen the gap in broad domains over time

[@teortaxesTex](https://x.com/teortaxesTex/status/2047608887616962992), [@teortaxesTex](https://x.com/teortaxesTex/status/2047631470664020211): disputes simplistic Huawei-dismissal and notes mixed Chinese sentiment toward Huawei

[@ogawa_tter](https://x.com/ogawa_tter/status/2047631993702363509): points to analysis of Ascend 950 / A3 clusters and V4 deployment plans

[@Dorialexander](https://x.com/Dorialexander/status/2047632551326413109): argues the sovereignty play around Huawei may reshape hardware architecture

[@scaling01](https://x.com/scaling01/status/2047760776769720360): cites DeepSeek saying prices could drop sharply once Ascend 950 supernodes scale in H2

[@jukan05](https://x.com/jukan05/status/2047861732702662741): interprets V4 as validating NVIDIA’s Blackwell/Rubin/HBM/interconnect strategy

[@NVIDIAAI](https://x.com/NVIDIAAI/status/2047765637808664759), [@NVIDIAAI](https://x.com/NVIDIAAI/status/2047823093578518758): unsurprisingly highlight Blackwell day-0 performance, but this is vendor framing rather than independent proof of strategic superiority

There is also a more ideological thread:

[@teortaxesTex](https://x.com/teortaxesTex/status/2047645676234846459), [@teortaxesTex](https://x.com/teortaxesTex/status/2047638436295725080), [@teortaxesTex](https://x.com/teortaxesTex/status/2047835420755415472) argues that Western discourse often misreads Chinese labs as purely state proxies or distillation shops, and instead sees them as serious mission-driven actors. This is interpretive, but it helps explain why the release drew such emotionally charged geopolitical reactions.

Distillation, training data, and data quality

A recurring undercurrent: does V4 mainly reflect architectural innovation, or can critics dismiss it as “distillation”?

[@yacineMTB](https://x.com/yacineMTB/status/2047628416514486661) speculates that some complaints about Chinese distillation may partly come from people discovering they’re outperformed

[@cloneofsimo](https://x.com/cloneofsimo/status/2047628636933812301): “Very interesting... given they distilled claude 🤔🤔”

[@kalomaze](https://x.com/kalomaze/status/2047762970931827125): jokes about DeepSeek training on DeepSeek reasoning traces

On the more substantive side, [@teortaxesTex](https://x.com/teortaxesTex/status/2047614729145745623) says DeepSeek’s writing quality, especially Chinese, reflects long-standing obsession with data cleanliness and cites job listings [@teortaxesTex](https://x.com/teortaxesTex/status/2047614852055683103), [@teortaxesTex](https://x.com/teortaxesTex/status/2047614975447855485)

[@nrehiew_](https://x.com/nrehiew_/status/2047666048334450754) notes the report still lacks much detail on pretraining data beyond standard categories

Overall, factual public evidence in this tweet set supports “DeepSeek trains at large scale with strong data work,” but not any strong claim about the degree of external distillation beyond speculation

Architecture lineage and prior art

Several researchers pointed out that V4 did not emerge from nowhere.

[@jaseweston](https://x.com/jaseweston/status/2047690308217926055): says DeepSeek uses hash routing from a 2021 ParlAI approach

[@suchenzang](https://x.com/suchenzang/status/2047772636881842629): criticizes routing-induced outliers, with a jab at hashing

[@teortaxesTex](https://x.com/teortaxesTex/status/2047844368883581404): notes Mixtral-style MoE was a reasonable earlier hack, but claims DSMoE changed things

[@art_zucker](https://x.com/art_zucker/status/2047619111082172548) broadly attacks MoEs as a dead end

[@gabriberton](https://x.com/gabriberton/status/2047835467551547587) counters that MoEs are provably effective despite inelegance

[@stochasticchasm](https://x.com/stochasticchasm/status/2047874903236645108) is even more positive: “MoEs are amazing”

This matters because V4 was read not just as a stronger checkpoint, but as a possible new design point for open long-context MoEs.

Why the technical report itself mattered

A striking amount of praise was directed not just at the model but at the paper/report quality.

[@scaling01](https://x.com/scaling01/status/2047618271310926151): “the technical paper is a big deal”

[@Dorialexander](https://x.com/Dorialexander/status/2047632551326413109): “most significant AI paper of the year”

[@morqon](https://x.com/morqon/status/2047643246923325833): “one of the best I’ve ever read”

[@scaling01](https://x.com/scaling01/status/2047643722108579936): “this is what research should look like”

[@TheZachMueller](https://x.com/TheZachMueller/status/2047626249116303561), [@iamgrigorev](https://x.com/iamgrigorev/status/2047641600591794546), [@nrehiew_](https://x.com/nrehiew_/status/2047665987730993363): all signal unusually high effort to digest and test the report

For expert readers, this is important because many frontier releases now arrive with sparse technical disclosure. V4’s report appears to have reset expectations for what a serious open release can look like.

Practical limitations and caveats

Despite the enthusiasm, several caveats recur:

Still behind closed frontier in aggregate capability

especially sciences/law/medicine and broad “general domains” per [@scaling01](https://x.com/scaling01/status/2047622501241434581)

Reasoning RL may be undercooked

[@scaling01](https://x.com/scaling01/status/2047618271310926151): reasoning efficiency not much changed vs V3.2 Speciale

Serving remains hard

[@scaling01](https://x.com/scaling01/status/2047643015859118167): many labs serve at only 20–30 tok/s and limited concurrency; running evals can take a day

[@ClementDelangue](https://x.com/ClementDelangue/status/2047664153439989823): acknowledges concurrency bottlenecks on HF

High token usage

major practical caveat from [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2047735160544841953)

API controls

[@stochasticchasm](https://x.com/stochasticchasm/status/2047717161070989499): notes DeepSeek API appears not to allow sampler control

Adoptability

[@teortaxesTex](https://x.com/teortaxesTex/status/2047840426371977467): too complex for many labs to copy cleanly

Broader implications

Three implications stand out.

Open-weight long-context is no longer just marketing.
V4’s strongest contribution may be proving that 1M context can be made operationally credible in an open-weight model, with concrete KV-cache engineering and open inference support. This is why multiple posters focused less on benchmark deltas and more on systems design: [@ben_burtenshaw](https://x.com/ben_burtenshaw/status/2047646980139016560), [@ZhihuFrontier](https://x.com/ZhihuFrontier/status/2047664976215839021), [@scaling01](https://x.com/scaling01/status/2047618271310926151).

China’s top labs remain competitive in open models, even if not fully closing the closed-model gap.
The benchmark picture across [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2047735160544841953), [@arena](https://x.com/arena/status/2047714237502677405), and [@scaling01](https://x.com/scaling01/status/2047733998714052819) suggests Chinese labs now dominate much of the open-weight top tier: Kimi, GLM, DeepSeek, and soon MiMo.

The bar for “open” is rising from checkpoint release to full-stack co-design.
V4 was instantly discussed alongside vLLM, Blackwell, MLX quants, Mac viability, Ascend clusters, and cache/memory architectures. In other words, “the model” is increasingly inseparable from the inference substrate.

Infrastructure, inference, and local/open ecosystem

Hugging Face launched ML Intern, an open-source CLI “AI intern” for ML work that can research papers, write code, run experiments, use HF datasets/jobs, search GitHub, and iterate up to 300 steps, per [@MillieMarconnni](https://x.com/MillieMarconnni/status/2047639632859500691). Related sentiment: HF’s $9 Pro tier is unusually strong value per [@getpy](https://x.com/getpy/status/2047602009998794820).

Meta said it will add tens of millions of AWS Graviton cores to its compute portfolio to scale Meta AI and agentic systems for billions of users, per [@AIatMeta](https://x.com/AIatMeta/status/2047647617681957207).

Local/open coding stack momentum stayed strong:

[@julien_c](https://x.com/julien_c/status/2047647522173104145): Qwen3.6-27B via llama.cpp on a MacBook Pro feels close to latest Opus for many coding tasks

[@p0](https://x.com/p0/status/2047794814104862843): free CLI agent built with Pi + Ollama + Gemma 4 + Parallel web search MCP

[@Prince_Canuma](https://x.com/Prince_Canuma/status/2047693737950670940): DeepSeek V4 quants incoming

[@QuixiAI](https://x.com/QuixiAI/status/2047765475937890474): reminder that llama.cpp / Ollama / LM Studio do not support tensor parallel, pushing serious multi-GPU serving users toward vLLM

Nous/Hermes shipped heavily:

Hermes Agent v0.11.0 introduced a rewritten React TUI, dashboard plugin, theming, more inference providers, image backends, and QQBot support, per [@WesRoth](https://x.com/WesRoth/status/2047646749427216385)

Hermes got broad praise and rapid support for both DeepSeek V4 and GPT-5.5, via [@mr_r0b0t](https://x.com/mr_r0b0t/status/2047673600900010044), [@Teknium](https://x.com/Teknium/status/2047791512210293067)

[@JulianGoldieSEO](https://x.com/JulianGoldieSEO/status/2047699587788361844) and [@LoicBerthelot](https://x.com/LoicBerthelot/status/2047690512199540959) compared Hermes favorably to OpenClaw on learning loops, memory, model support, deployment flexibility, and security

A native Linux sandbox backend for Deep Agents using bubblewrap + cgroups v2 was released by [@nu_b_kh](https://x.com/nu_b_kh/status/2047775326412136574)

Research papers and benchmarks

On-policy distillation token selection:

[@TheTuringPost](https://x.com/TheTuringPost/status/2047617791709282405) highlights a paper showing only some tokens carry most learning signal; using ~50% of tokens can match or beat full training and cut memory by ~47%, while even <10% focused on confident-wrong tokens nearly matches full training.

Google Research pushed several ICLR demos:

MesaNet, a transformer alternative / linear sequence layer optimized for in-context learning under fixed memory, via [@GoogleResearch](https://x.com/GoogleResearch/status/2047630714145776053)

robotics/3D reasoning and efficient transformer work via [@GoogleResearch](https://x.com/GoogleResearch/status/2047675181808730197)

“reasoning can lead to honesty” demo via [@GoogleResearch](https://x.com/GoogleResearch/status/2047704802163892576)

MIT Hyperloop Transformers mix looped and normal transformer blocks, using ~50% fewer parameters while beating regular transformers at 240M / 1B / 2B, per [@TheTuringPost](https://x.com/TheTuringPost/status/2047720038342476187).

“Learning mechanics” tries to synthesize a theory of deep learning dynamics, via [@learning_mech](https://x.com/learning_mech/status/2047723849874330047).

Tool/agent systems papers:

Tool Attention Is All You Need claims 95% tool-token reduction (47.3k → 2.4k/turn) with dynamic gating and lazy schema loading, per [@omarsar0](https://x.com/omarsar0/status/2047725276851994639)

StructMem for long-horizon structured memory highlighted by [@dair_ai](https://x.com/dair_ai/status/2047740873027543228)

HorizonBench targets long-horizon personalization with shifting user preferences, via [@StellaLisy](https://x.com/StellaLisy/status/2047645651324821998)

Clarifying questions for software engineering:

[@gneubig](https://x.com/gneubig/status/2047623214583492797) shared work on a model trained specifically to ask clarifying questions, improving results with fewer questions.

GPT-5.5 rollout and coding agents

OpenAI rolled GPT-5.5 and GPT-5.5 Pro into API and ecosystem products with a 1M context window, per [@OpenAI](https://x.com/OpenAI/status/2047743592278745425), [@OpenAIDevs](https://x.com/OpenAIDevs/status/2047742589982654915).

Distribution was immediate across Cursor, GitHub Copilot, Codex/OpenAI API, OpenRouter, Perplexity, Devin, Droid, Fleet, Deep Agents:

[@cursor_ai](https://x.com/cursor_ai/status/2047744579127185843): GPT-5.5 is top on CursorBench at 72.8%

[@cline](https://x.com/cline/status/2047769312514257148): #1 on Terminal-Bench at 82.7

[@OpenAIDevs](https://x.com/OpenAIDevs/status/2047772632150675593): Perplexity Computer saw 56% fewer tokens on complex tasks

[@scaling01](https://x.com/scaling01/status/2047818395970904229): GPT-5.5 medium became strongest non-thinking model on LisanBench with 45.6% fewer tokens than GPT-5.4 medium and higher scores

User feedback clustered around better coding quality and token efficiency, despite mixed feelings about some evals:

[@almmaasoglu](https://x.com/almmaasoglu/status/2047745168141324559): best code they’ve read from an LLM; less verbose, less defensive

[@KentonVarda](https://x.com/KentonVarda/status/2047788670728495142): caught a deep Cap’n Proto RPC corner case from a 6-year-old comment

[@willdepue](https://x.com/willdepue/status/2047783399826292969): underwhelmed by evals, impressed in Codex on complex technical projects

[@omarsar0](https://x.com/omarsar0/status/2047768166126809512): smooth switch from Claude Code to Codex/GPT-5.5 thanks to better “effort calibration”

Cursor also shipped /multitask async subagents and multi-root workspaces, via [@cursor_ai](https://x.com/cursor_ai/status/2047764651363180839).

There is growing market emphasis on limits and economics rather than tiny quality gaps:

[@nrehiew_](https://x.com/nrehiew_/status/2047839351380537357) argues usage caps now matter more than small frontier deltas

[@HamelHusain](https://x.com/HamelHusain/status/2047763070022479882) says Codex’s subscription structure makes it hard not to use

Industry moves, funding, and policy

Google reportedly plans to invest up to $40B in Anthropic, reported by [@FT](https://x.com/FT/status/2047715653553942997) and echoed by [@zerohedge](https://x.com/zerohedge/status/2047704883982180609). Reactions centered on how large Anthropic’s compute commitment may now be.

Cohere and Aleph Alpha announced a Canada/Germany sovereign AI partnership, framed as enterprise-grade and privacy/security focused by [@cohere](https://x.com/cohere/status/2047631725426000268), [@aidangomez](https://x.com/aidangomez/status/2047651054381052086), [@nickfrosst](https://x.com/nickfrosst/status/2047704679878996253#m).

ComfyUI raised $30M at a $500M valuation, while keeping core/open-local positioning, via [@yoland_yan](https://x.com/yoland_yan/status/2047731043000627263).

Mechanize announced $9.1M raised at a $500M post-money valuation, via [@MechanizeWork](https://x.com/MechanizeWork/status/2047732999878529037).

Arcee AI hired Cody Blakeney as Head of Research, emphasizing open-weight American frontier models, via [@code_star](https://x.com/code_star/status/2047765768658702467).

Safety / governance:

OpenAI announced a Bio Bug Bounty for GPT-5.5, per [@OpenAINewsroom](https://x.com/OpenAINewsroom/status/2047670970526175310)

Anthropic launched Project Deal, a marketplace where Claude negotiated on behalf of employees, and highlighted model-quality asymmetry and policy challenges, via [@AnthropicAI](https://x.com/AnthropicAI/status/2047728360818696302)

Creative AI and multimodal

GPT Image 2 + Seedance 2 workflows kept drawing attention:

[@_OAK200](https://x.com/_OAK200/status/2047616640448078167) and [@awesome_visuals](https://x.com/awesome_visuals/status/2047609881104953658) showed high-fidelity image→video pipelines

[@BoyuanChen0](https://x.com/BoyuanChen0/status/2047738501647728937) said 2K/4K images are already available via experimental API and active fixes are underway

Kling announced native 4K output and a $25k short film contest, via [@Kling_ai](https://x.com/Kling_ai/status/2047676942317678879).

Some evaluative nuance:

[@goodside](https://x.com/goodside/status/2047728776520298646) noted GPT Images 2.0 could render a valid-looking Rubik’s Cube state, which is surprisingly hard

[@venturetwins](https://x.com/venturetwins/status/2047820435543437630) framed recent image/video gains as a major step toward personalized game-like content generation

AI Reddit Recap

/r/LocalLlama + /r/localLLM Recap

1. Deepseek V4 and Related Releases

[Deepseek V4 AGI comfirmed](https://www.reddit.com/r/LocalLLaMA/comments/1suolda/deepseek_v4_agi_comfirmed/) (Activity: 1138): The image is a meme and does not contain any technical content. The title “Deepseek V4 AGI confirmed” suggests a humorous or exaggerated claim about an AI model, possibly referencing advancements in artificial general intelligence (AGI). The comments further imply a satirical tone, mentioning uncensored datasets and military applications, which are likely not serious claims. The comments reflect a satirical take on AI capabilities, with mentions of uncensored datasets and military applications, indicating skepticism or humor rather than a serious technical discussion.

UserXtheUnknown discusses a test scenario with Deepseek V4, highlighting its tendency to overthink problems. The model interprets constraints like ‘using only one knife’ as mandatory rather than optional, which affects its problem-solving approach. This reflects a nuanced understanding of task constraints, but also indicates potential areas for improvement in handling implicit instructions.

[Deepseek V4 Flash and Non-Flash Out on HuggingFace](https://www.reddit.com/r/LocalLLaMA/comments/1su3hdo/deepseek_v4_flash_and_nonflash_out_on_huggingface/) (Activity: 1393): DeepSeek V4 has been released on [HuggingFace](https://huggingface.co/collections/deepseek-ai/deepseek-v4), featuring two models: DeepSeek-V4-Pro with 1.6T parameters (of which 49B are activated) and DeepSeek-V4-Flash with 284B parameters (with 13B activated). Both models support a context length of one million tokens, which is significant for handling extensive sequences. The models are released under the MIT license, allowing for broad use and modification. A notable comment highlights the challenge of hardware limitations, particularly RAM, when working with such large models. Another comment suggests the potential benefit of a 0.01bit quantization to manage the model size more effectively.

The DeepSeek-V4 models are notable for their massive parameter sizes, with the Pro version having 1.6 trillion parameters (49 billion activated) and the Flash version having 284 billion parameters (13 billion activated). Both models support an extensive context length of one million tokens, which is significant for handling large-scale data inputs and complex tasks.

A user expressed interest in a 0.01-bit quantization of the DeepSeek-V4 models, which suggests a focus on reducing the model size and computational requirements while maintaining performance. Quantization is a common technique to optimize models for deployment on hardware with limited resources.

The mention of the MIT license indicates that DeepSeek-V4 is open-source, allowing for broad use and modification by the community. This licensing choice can facilitate collaboration and innovation, as developers can freely integrate and adapt the models into their own projects.

[Buried lede: Deepseek v4 Flash is incredibly inexpensive from the official API for its weight category](https://www.reddit.com/r/LocalLLaMA/comments/1su5gj5/buried_lede_deepseek_v4_flash_is_incredibly/) (Activity: 404): The image provides a comparison between two models, “deepseek-v4-flash” and “deepseek-v4-pro,” highlighting that the “deepseek-v4-flash” model is significantly more affordable in terms of input and output token costs. Despite its affordability, the model supports advanced features like JSON output, tool calls, and chat prefix completion in both non-thinking and thinking modes. The discussion around the image suggests that while the “deepseek-v4-flash” is marketed as inexpensive, some users argue that it is actually overpriced compared to previous versions when considering parameter scaling, with the “V3.2” model being cheaper per parameter. Commenters discuss the impact of GPU shortages on current pricing, suggesting that prices may decrease as GPU production increases. There is also debate about the pricing strategy, with some users noting that the new model is more expensive per parameter compared to older versions.

DistanceSolar1449 highlights a pricing comparison between DeepSeek V3.2 and V4 Flash, noting that V3.2 was priced at $0.26/0.38 for input/output at 671b, whereas V4 Flash is $0.14/$0.28 at 284b. This suggests that V4 Flash is actually more expensive if pricing were to scale linearly with parameters, challenging the notion of its cost-effectiveness.

jwpbe provides a comparative analysis of DeepSeek V4 Flash’s API cost, stating that at 14 cents in / 28 cents out, it is significantly cheaper than competitors like Minimax 2.7, which is 3x the cost, and Qwen’s equivalent, which is even higher. They also mention that Trinity Thinking Large is twice as expensive, indicating that V4 Flash offers a competitive pricing advantage in the market.

Worried-Squirrel2023 discusses the strategic implications of Huawei’s silicon developments, suggesting that DeepSeek’s pricing strategy involves trading NVIDIA margins for Ascend supply. They predict that once the 950 supernodes scale, DeepSeek could potentially undercut competitors in the open weights tier, leveraging Huawei’s advancements to optimize costs.

[Deepseek has released DeepEP V2 and TileKernels.](https://www.reddit.com/r/LocalLLaMA/comments/1ste9zs/deepseek_has_released_deepep_v2_and_tilekernels/) (Activity: 396): Deepseek has released DeepEP V2 and TileKernels, which are significant advancements in AI model optimization and parallelization. DeepEP V2 focuses on enhancing model efficiency and accuracy, while TileKernels introduces a novel parallelization technique that reportedly scales linearly, meaning that doubling computational capacity results in a doubling of processing speed. This release is open-sourced, fostering transparency and collaboration in AI research. For more details, see the [DeepEP V2 pull request](https://github.com/deepseek-ai/DeepEP/pull/605) and the [TileKernels repository](https://github.com/deepseek-ai/TileKernels). One commenter highlights that Deepseek is fulfilling a role that OpenAI was expected to play by advancing research and sharing findings openly, which builds goodwill despite proprietary technologies. Another commenter questions if the parallelization technique indeed scales linearly, suggesting a significant technical breakthrough if true.

DeepEP V2 and TileKernels by DeepSeek are noted for their potential advancements in parallelization techniques. A user speculates that these techniques might achieve linear scaling, meaning that doubling computational capacity could directly double processing speed. This could represent a significant efficiency improvement in model training and inference.

There is speculation about DeepSeek’s hardware usage, particularly regarding the SM100 and Blackwell GPUs. One commenter suggests that DeepSeek might be using Blackwell GPUs for training, possibly through rented B200 units on Vast.ai. This hardware choice could influence the performance and capabilities of their models.

The potential innovations in DeepSeek’s next model, possibly named v4, are highlighted. The focus is on the integration of Engram and mHC technologies, which are expected to play a crucial role in the model’s performance. The success of these innovations will likely depend on the new dataset DeepSeek has developed.

2. Qwen 3.6 Model Performance and Benchmarks

[This is where we are right now, LocalLLaMA](https://www.reddit.com/r/LocalLLaMA/comments/1suqfba/this_is_where_we_are_right_now_localllama/) (Activity: 1755): The image depicts a MacBook Pro running a Qwen3.6 27B model via Llama.cpp, showcasing the capability of executing complex AI models locally, even in airplane mode. This highlights the potential for local AI models to enhance efficiency, security, privacy, and sovereignty by operating independently of cloud services. The post underscores the technological advancement in making powerful AI models accessible on personal devices, emphasizing the importance of local execution for privacy and control. Commenters express skepticism about the overstatement of the Qwen3.6-27B model’s capabilities, suggesting that while it is impressive for its size, it does not match the performance of more advanced models like Sonnet or Opus. There is concern that exaggerated claims could lead to user disappointment and backlash against the broader LLM community.

ttkciar highlights the potential for user disappointment with the Qwen3.6-27B model, noting that while it’s impressive for its size and suitable for agentic code generation, it doesn’t match the capabilities of more advanced models like Sonnet or Opus. The concern is that overhyping its abilities could lead to backlash against the broader LLM community, not just the individual making the claims.

sooki10 agrees that while the model is impressive for local coding tasks, comparing it to more advanced models like Opus is misleading and could undermine the credibility of the claims being made. This suggests a need for more accurate benchmarking and communication about the model’s capabilities to manage user expectations effectively.

Melodic_Reality_646 points out the disparity in resources, comparing the use of a high-end 128GB RAM m5max system to a more accessible setup. This highlights the importance of considering hardware limitations when evaluating model performance, as not all users have access to such powerful systems, which can skew perceptions of a model’s capabilities.

[DS4-Flash vs Qwen3.6](https://www.reddit.com/r/LocalLLaMA/comments/1sub71w/ds4flash_vs_qwen36/) (Activity: 470): The image presents a benchmark comparison between DS4-Flash Max and Qwen3.6 models, specifically the 35B-A3B and 27B versions. The chart highlights that DS4-Flash Max generally outperforms the Qwen models across various categories, particularly excelling in ‘LiveCodeBench’ and ‘HLE’ benchmarks. This suggests that DS4-Flash Max may have superior capabilities in coding and reasoning tasks. The discussion in the comments hints at the potential for larger models like a 122B version of Qwen3.6, and emphasizes the significance of the 1M token context feature, which could impact performance in other benchmarks like ‘omniscense’. Commenters note that despite DS4-Flash Max’s larger size, its performance is only slightly better than Qwen3.6, raising questions about efficiency versus scale. The 1M token context is highlighted as a significant feature that could influence future benchmark results.

Rascazzione highlights the significant increase in context length with Qwen 3.6, noting its ability to handle a 1 million token context. This is a substantial improvement over previous models and could have significant implications for tasks requiring extensive context handling, such as document summarization or complex dialogue systems.

LinkSea8324 points out the size difference between the models, with DS4-Flash at 284 billion parameters compared to Qwen 3.6’s 27 billion. This raises questions about the efficiency and performance trade-offs between model size and capability, especially in terms of computational resources and inference speed.

madsheepPL discusses the non-linear nature of benchmark improvements, suggesting that even if a model appears only slightly better in benchmarks, the practical implications can be more significant. They emphasize that improvements in scores are not directly proportional and can have varying impacts on real-world applications.

[Qwen 3.6 27B Makes Huge Gains in Agency on Artificial Analysis - Ties with Sonnet 4.6](https://www.reddit.com/r/LocalLLaMA/comments/1strodp/qwen_36_27b_makes_huge_gains_in_agency_on/) (Activity: 964): Qwen 3.6 27B has achieved parity with Sonnet 4.6 on the Agentic Index from Artificial Analysis, surpassing models like Gemini 3.1 Pro Preview, GPT 5.2 and 5.3, and MiniMax 2.7. The model shows improvements across all indices, although the gains in the Coding Index are less pronounced due to its reliance on benchmarks like Terminal Bench Hard and SciCode, which are considered unconventional. The focus of training appears to be on agentic applications for OpenClaw/Hermes, highlighting the potential of smaller models to approach frontier capabilities. Anticipation is building for the upcoming Qwen 3.6 122B model. Commenters express excitement about the potential of smaller models like Qwen 3.6 27B, noting the significant improvements and potential for future versions. However, there is skepticism about the extent of these gains, suggesting that some improvements might be due to ‘benchmaxxing’ rather than inherent model capabilities.

Iory1998 highlights the impressive performance of the Qwen 3.6 27B model, noting that it surpasses a 670B model from the previous year. They mention running the Q8 version at 170K with KV cache at FP16 on an RTX 3090 and RTX 5070ti, utilizing 40GB of VRAM, which underscores the model’s efficiency and power.

AngeloKappos discusses the narrowing benchmark gap, sharing their experience running the Qwen3-30b-a3b model on an M2 chip. They note its capability to handle multi-step tool calls effectively, suggesting that if the 27B dense model performs this well, the upcoming 122B model could pose challenges for API providers due to its potential performance.

Velocita84 raises a point about potential “benchmaxxing” in the reported performance gains of the Qwen 3.6 27B model, implying that some of the improvements might be attributed to optimized benchmarking rather than inherent model capabilities. This suggests a need for scrutiny in evaluating model performance claims.

[Compared QWEN 3.6 35B with QWEN 3.6 27B for coding primitives](https://www.reddit.com/r/LocalLLaMA/comments/1styxdy/compared_qwen_36_35b_with_qwen_36_27b_for_coding/) (Activity: 491): The post compares two versions of the QWEN 3.6 model, specifically the 35B and 27B parameter versions, on a MacBook Pro M5 MAX with 64GB RAM. The 35B model achieves 72 TPS (tokens per second), while the 27B model achieves 18 TPS. Despite the slower speed, the 27B model produces more precise and correct results for coding tasks, whereas the 35B model is faster but less accurate. The test involved generating a single HTML file to simulate a moving car with a parallax effect, using no external libraries. The models were hosted using [Atomic.Chat](http://atomic.chat/), with source code available on [GitHub](https://github.com/AtomicBot-ai/Atomic-Chat). One comment highlights the output of the Qwen 3.6 27B FP8 model using opencode, taking approximately 52 seconds. Another comment provides a visual comparison with the Qwen 3.5 27B Q3 model, suggesting differences in output quality.

The user ‘sacrelege’ shared a performance result for the Qwen 3.6 27B model using FP8 precision, noting that it took approximately 52 seconds to complete a task with ‘opencode’. This suggests a focus on optimizing model performance through precision adjustments, which can significantly impact computational efficiency and speed.

User ‘nikhilprasanth’ provided a visual comparison for the Qwen 3.5 27B Q3 model, indicating a potential interest in comparing different versions and quantization levels of the Qwen models. This highlights the importance of understanding how different model configurations can affect performance and output quality.

‘Technical-Earth-3254’ inquired about the quantization methods used in the tests, which is crucial for understanding the trade-offs between model size, speed, and accuracy. Quantization can greatly influence the efficiency of large models like Qwen, especially in resource-constrained environments.

[Qwen 3.6 27B is a BEAST](https://www.reddit.com/r/LocalLLaMA/comments/1steip4/qwen_36_27b_is_a_beast/) (Activity: 1239): The post discusses the performance of the Qwen 3.6 27B model on a high-end laptop with an RTX 5090 GPU and 24GB VRAM, highlighting its effectiveness for pyspark/python and data transformation debugging tasks. The user employs llama.cpp with q4_k_m at q4_0 and is exploring further optimizations with IQ4_XS at 200k q8_0. The user has not yet implemented speculative decoding. The setup includes an ASUS ROG Strix SCAR 18 with 64GB DDR5 RAM. Comments suggest avoiding kv cache as q4 for coding, recommending q8 for 130k context. Another comment anticipates performance improvements with upcoming releases from z-lab and a specific [GitHub pull request](https://github.com/ggml-org/llama.cpp/pull/22105) that promises a 2x decode speed increase. There is also curiosity about the model’s performance on systems with 16GB VRAM and 32GB DDR5 RAM with offloading.

sagiroth highlights a technical consideration when using Qwen 3.6 27B for coding tasks, advising against using the KV cache as q4 due to limitations, and instead suggests using q8 to achieve a 130k context window, which can significantly enhance performance for large context tasks.

inkberk points out an upcoming improvement in decoding speed, referencing a pull request [#22105](https://github.com/ggml-org/llama.cpp/pull/22105) on the llama.cpp repository. This update, along with the anticipated release of the ‘dflash drafter’ by z-lab, promises a potential 2x increase in decode speed, which could greatly benefit users in terms of efficiency.

Johnny_Rell inquires about the performance of Qwen 3.6 27B on a system with 16 GB VRAM and 32 GB DDR5, specifically regarding the effectiveness of offloading. This suggests a focus on optimizing resource allocation to handle the model’s demands, which is crucial for running large models efficiently on consumer-grade hardware.

[
Read more
](https://www.latent.space/p/ainews-deepseek-v4-pro-16t-a49b-and)

---

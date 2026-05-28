---
title: Latent Space — 2026-05-27
date: 2026-05-27
source: Latent Space
type: ai-news
---

# 🔬 Latent Space — 2026-05-27

> swyx 開發者簡報，未公開專案 + 工程視角
> 來源：[Latent Space](https://www.latent.space/feed)

---

## [[AINews] All Model Labs are now Agent Labs](https://www.latent.space/p/ainews-all-model-labs-are-now-agent)
*🔬 Latent Space | 2026-05-23*

Ahead of OpenAI's [likely IPO filing](https://aitoolsrecap.com/Blog/openai-ipo-2026-valuation-timeline-what-investors-need-to-know) next week, Greg makes the latest in a series of comments where [Model Labs are increasingly also building Agents](https://www.latent.space/p/agent-labs) as the product:

[](https://substackcdn.com/image/fetch/$s_!TLyU!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F348d0573-16b0-46d0-a852-ccaae2b6ff4f_1122x534.png)

The quote is a big reversal of stance from a position ~uniformly held by anyone who worked at **[Team Big Model](https://www.latent.space/p/oai-v-langgraph?utm_source=publication-search)** , including [his previous head of OpenAI Labs](https://x.com/CoreAutoAI/status/2056442820022747444):

[](https://substackcdn.com/image/fetch/$s_!cKHI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff0b62ab4-065e-4317-857e-6483330aeb08_1088x1308.png)

This comes with the shuttering of AI21's model team, which is now pivoting to agents:

[](https://substackcdn.com/image/fetch/$s_!EsgI!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff8ba4c74-81d3-4163-a6c3-752ef8ec9fe6_1076x1362.png)

and even the venerable DeepSeek is now building a "Harness team" for the first time:

[](https://substackcdn.com/image/fetch/$s_!GILi!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F77b428e9-bb30-464c-8dc2-827ae5accf1f_1084x426.png)

The "Systems over Models" people will take this as a point of validation of what they have been saying all along… except for the nuance that models cotrained with harnesses does open the door for closing access to models even further -- if you can effectively posttrain a model to only meaningfully perform with your closed source agent, then you get to funnel the majority of users to your agent at the expense of your model/API co-opetition.

But that's a topic of a much larger discussion…

> AI News for 5/4/2026-5/5/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

# **AI Twitter Recap**

**Agent Products, Harnesses, and the Shift Beyond "Just the Model"**

  * **The product surface is moving up-stack** : A recurring theme was that model quality alone is no longer the moat; the winning product is increasingly **model + harness + workflow + UI + memory + economics**. [@gdb](https://x.com/gdb/status/2057670776803996110) put it bluntly: "the model alone is no longer the product," while [@dzhng](https://x.com/dzhng/status/2057748510947082539) argued top-tier products need **model <> harness <> product symbiosis**. The same pattern shows up in practice: [@signulll](https://x.com/signulll/status/2057850735048458639) framed ambient AI and agentic AI as the new seam of computing interfaces, and [@teortaxesTex](https://x.com/teortaxesTex/status/2057770692112798209) noted that harness research still risks converging on "replicate Claude Code" instead of exploring broader interfaces.

  * **Coding-agent product differentiation is becoming concrete** : OpenAI shipped another substantial Codex update via ["codex thursday no. 6"](https://x.com/ajambrosino/status/2057716220963803577) with **appshots, /goal improvements, remote computer use while locked, annotation mode, plugin sharing, and analytics**. [@gdb](https://x.com/gdb/status/2057802037757157838) separately highlighted **Appshots** , while users reported meaningful workflow shifts: [@gdb](https://x.com/gdb/status/2057704270531903811) said it's hard to remember coding before Codex, and [@reach_vb](https://x.com/reach_vb/status/2057830243201622368) said they haven't opened an IDE in over a month. But product rough edges remain: [@theo](https://x.com/theo/status/2057960907997876412) praised **T3 Code 's remote feature** as ahead of alternatives, then contrasted it with buggy remote workflows in Codex in a follow-up [post](https://x.com/theo/status/2057961165175873930). On the Claude side, [@ClaudeDevs](https://x.com/ClaudeDevs/status/2057946803685974482) expanded **auto mode** to the Pro plan and added **Sonnet 4.6** support; [@_mohansolo](https://x.com/_mohansolo/status/2057910616153882949) also had to clarify and patch IDE support in **Antigravity 2.0** after user backlash.




**Model Performance, Cost Curves, and Frontier Competition**

  * **DeepSeek 's pricing move was the biggest market signal**: [@deepseek_ai](https://x.com/deepseek_ai/status/2057854261699195173) made the **75% DeepSeek-V4-Pro discount permanent** , triggering strong reactions because it materially changes the **cost/performance frontier**. [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2058021452465799403) quantified first-party pricing at **$0.435/M input, $0.87/M output, $0.0036/M cached input** , estimating a blended **~$0.18/M** and placing V4 Pro on the Pareto frontier for intelligence vs run cost. They estimate running their Intelligence Index on V4 Pro costs **~3x less than Gemini 3.1 Pro Preview, ~12x less than GPT-5.5, and ~19x less than Claude Opus 4.7**. Community reaction centered on DeepSeek's push toward "**intelligence too cheap to meter** ," as [@scaling01](https://x.com/scaling01/status/2057835507858518178) put it. [@Yuchenj_UW](https://x.com/Yuchenj_UW/status/2057855546460676410) and [@kimmonismus](https://x.com/kimmonismus/status/2057868472965640194) both emphasized the magnitude of the cut.

  * **Gemini Flash improved, but usage feedback was mixed** : [@OfficialLoganK](https://x.com/OfficialLoganK/status/2057682092583227881) reported **Gemini 3.5 Flash** making major progress over **3.1 Pro on GDPval** , claiming Flash is now "competing at the frontier," and [@Designarena](https://x.com/Designarena/status/2057885688125968660) placed it **16th overall** on Design Arena, a **16-position jump** from Gemini 3 Flash Preview. But several builders pushed back on usefulness vs benchmark gains: [@Alezander907](https://x.com/Alezander907/status/2057686331380359566) saw only slight browser-agent improvement at higher cost, [@giffmana](https://x.com/giffmana/status/2057714729762627950) argued this isn't "Flash progress" if the brand still implies cheapness, and [@jeremyphoward](https://x.com/jeremyphoward/status/2057923197639840033) said the model feels optimized to **max evals rather than cooperate with humans**. That aligns with broader eval skepticism from [@HamelHusain](https://x.com/HamelHusain/status/2057875320011882923), who argued current tooling underweights qualitative, HITL judgment.

  * **Qwen and Chinese frontier models keep compressing the race** : The official [@Alibaba_Qwen](https://x.com/Alibaba_Qwen/status/2057767604048240987) teasers and a long third-party review from [@ZhihuFrontier](https://x.com/ZhihuFrontier/status/2057772126162354660) portrayed **Qwen3.7-Max** as a meaningful step up, especially in **instruction following, context reliability, and stability** , while still suffering from **verbosity and high token usage**. Elsewhere, [@scaling01](https://x.com/scaling01/status/2057937081070944709) claimed recent ALE-Bench runs show Chinese models like **Kimi-K2.6, DeepSeek-V4, GLM-5.1** outperforming several Western releases in that setting. [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2057914437156409577) also reported **Cursor Composer 2.5** as **3 -18x cheaper than Opus 4.7** and **5 -32x cheaper than GPT-5.5** on Coding Agent benchmarks, with notably lower token use.




**Protocols, Infra, and Agent Runtime Tooling**

  * **MCP 's new release candidate is a substantive protocol simplification**: [@dsp_](https://x.com/dsp_/status/2057780712187580924) announced the **MCP 2026-07-28 release candidate** , with the key change that the protocol is now **stateless** : **no handshake, no session ID, and any request can hit any server instance**. The RC also introduces **first-class extensions** like **MCP Apps** and **Tasks** , plus auth hardening and a clearer deprecation policy. For infra teams, statelessness is a big operational shift: easier scaling, simpler load balancing, fewer sticky-session concerns.

  * **Sandboxes and managed execution are becoming first-class primitives** : [@_philschmid](https://x.com/_philschmid/status/2057833963633418426) demoed **Gemini Managed Agents + Interactions API** to give an agent a secure hosted Linux sandbox with memory and code execution. [@CoreWeave](https://x.com/CoreWeave/status/2057852737073942634) launched **CoreWeave Sandboxes** in public preview for **RL, agent tool use, and model eval** , while [@cnakazawa](https://x.com/cnakazawa/status/2057823910574588238) released **Cloudsail** for per-task Cloudflare sandboxes with shell, Codex, and GitHub access without exposing tokens. At the orchestration layer, [@skypilot_org](https://x.com/skypilot_org/status/2057854003648598312) argued **RL doesn 't work on Slurm** because modern RL is a multi-service system with heterogeneous hardware and recovery needs.

  * **Open-source harnesses and memory layers are proliferating** : [@NVIDIAAI](https://x.com/NVIDIAAI/status/2057855521193881773) open-sourced **AI-Q agent skills** for portable deep-research pipelines that can plug into arbitrary harnesses. [@Teknium](https://x.com/Teknium/status/2057880570160701852) added **Bitwarden support** for key management in Hermes and later restored **256K context** for **Grok Build v0.1** in Hermes [here](https://x.com/Teknium/status/2057930638632812642). [@shannholmberg](https://x.com/shannholmberg/status/2057821004676956586) described a **shared-memory "gBrain" layer** under Hermes agents, with typed folders and read-first access for specialist agents. [@aakashadesara](https://x.com/aakashadesara/status/2057809590616461399) updated **CTOP** to support **Devin** and a CLI for listing, searching, and killing agent sessions.




**Research: RL, Distillation, Architectures, and Evaluation**

  * **RL post-training and reward design are under active reconsideration** : [@RyanBoldi](https://x.com/RyanBoldi/status/2057847412819906658) introduced **Vector Policy Optimization (VPO)** , arguing scalar reward collapse during RL can sabotage test-time scaling. VPO instead optimizes **vector-valued rewards** , improving search performance even on the original scalar objective. [@lateinteraction](https://x.com/lateinteraction/status/2057854814395019623) framed this as a way to train LLMs for more diverse environments and goals, while [@FeiziSoheil](https://x.com/FeiziSoheil/status/2057889865362993561) connected it to broader moves toward **structured feedback** instead of a single reward number. Separately, [@jsuarez](https://x.com/jsuarez/status/2057828106023703037) teased a solution to a long-standing RL problem involving extreme sparsity, with initial sweeps showing SOTA on one internal environment.

  * **Agent compilation/distillation is emerging as a serious economic idea** : [@dair_ai](https://x.com/dair_ai/status/2057846601843146760) highlighted a paper showing a **full agentic workflow** --multi-step calls, tool use, scratchpads, decision structure--can be **distilled into weights** and run at **~100x lower inference cost** while preserving near-frontier quality. This is one of the clearest technical arguments yet for compiling expensive runtime agent loops into cheaper deployable models.

  * **Architecture work remains lively beyond vanilla transformers** : [@ChunyuanDeng](https://x.com/ChunyuanDeng/status/2057826955236462715) introduced **LT2** , a **linear-time looped transformer** combining sparse and linear attention to make looping practical, along with a distilled **Ouro-hybrid-1.4B**. [@ZyphraAI](https://x.com/ZyphraAI/status/2057854519732847029) shared work extending **Equilibrium Propagation** beyond energy-based models toward biologically realistic neurons. On MoE, [@Jianlin_S](https://x.com/Jianlin_S/status/2057719868917793221) proposed **Moving Quantile Balancing** for **sequence-level load balancing without a loss penalty**. Meanwhile [@allen_ai](https://x.com/allen_ai/status/2057838486204326078) launched **ArtifactLinker** , which predicts which benchmarks a model is likely to set SOTA on before running them--a useful meta-eval tool amid growing benchmark sprawl.

  * **Math and reasoning capability discourse shifted again** : [@cozyblaze265065](https://x.com/cozyblaze265065/status/2057739317649588558) reported **99.46%** on a multi-digit multiplication experiment using **gpt-5.5** with medium reasoning and no tools, and [@teortaxesTex](https://x.com/teortaxesTex/status/2057826903721951273) noted modern LLMs can now do **100-digit multiplication** without tools. That's not a complete theory of reasoning, but it further weakens old "autoregression can't do arithmetic" talking points.




**Multimodal Systems: Video, Speech, World Models, and Imaging**

  * **Google 's I/O stack pushed toward persistent agents and world simulators**: [@Google](https://x.com/Google/status/2057841803550683336) introduced **Gemini Spark** , a **24/7 personal AI agent** for recurring tasks, skills, and workflows. [@GoogleDeepMind](https://x.com/GoogleDeepMind/status/2057842131142590512) also launched **Project Genie + Street View** , letting users turn real U.S. locations into interactive worlds; follow-up posts confirm rollout to **Google AI Ultra** subscribers via Google Labs. The multimodal side was reinforced by [@Google](https://x.com/Google/status/2057881884219035752) announcing **Gemini Omni** for conversational video creation/editing and custom avatars, while [@emollick](https://x.com/emollick/status/2057874739817808223) emphasized the significance of a **fully multimodal** system that can natively edit video.

  * **Runway and image/video tooling keep raising editability** : [@runwayml](https://x.com/runwayml/status/2057826728769134599) released **Aleph 2.0** , supporting **multishot sequences up to 30s at 1080p** with targeted edits that preserve the rest of the scene. [@CuriousRefuge](https://x.com/CuriousRefuge/status/2057920807389806699) highlighted **SeeDance 2 Stitcher** for seamlessly extending AI-generated cinematic clips using Omni-generated continuations.

  * **Speech and image generation saw notable jumps** : [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2057878247782908109) ranked **Cartesia Sonic-3.5** as the new **#1 TTS model** on their Speech Arena, citing an **Elo of 1218** , support for **42 languages** , and strong naturalness/transcript following. Cartesia claims **82ms end-to-end first audio** in production [here](https://x.com/cartesia/status/2057880195403800633). In image generation, [@wildmindai](https://x.com/wildmindai/status/2057797994242523317) flagged Tencent's **Z-Image 6B** as a **pixel-space generator** with **no VAE** , **1K resolution** , and a transfer framework for converting Flux/SD models; related ecosystem work included Pixal3D demos from [@victormustar](https://x.com/victormustar/status/2057752615396557225) and training support for **Z-Image L2P 1k** in AI Toolkit from [@ostrisai](https://x.com/ostrisai/status/2057931161889095928).




**Security, Cyber, and Policy Pressure**

  * **Cybersecurity is quickly becoming a proving ground for advanced agents** : [@AnthropicAI](https://x.com/AnthropicAI/status/2057909102542549503) said **Project Glasswing** and partners found **more than ten thousand high- or critical-severity vulnerabilities** in essential software within a month, and explicitly warned the industry will need to adapt to the volume of vulnerabilities that models like **Claude Mythos Preview** can find. Security productization is following: [@perplexity_ai](https://x.com/perplexity_ai/status/2057869990536360334) open-sourced **Bumblebee** , a read-only scanner for macOS/Linux to detect risky packages, extensions, and AI tool configs; [@AravSrinivas](https://x.com/AravSrinivas/status/2057873563156402448) said enterprise deployment will require **agentic sandboxes** plus continuous security engineering.

  * **US immigration policy changes triggered sharp backlash from AI leaders** : Several high-engagement posts argued a proposed rule forcing green-card applicants to apply from outside the US would directly damage the AI talent pipeline. See [@Nick_Davidov](https://x.com/Nick_Davidov/status/2057842593850118286), [@AndrewYNg](https://x.com/AndrewYNg/status/2057907324380217821), [@theo](https://x.com/theo/status/2057911377151582437), [@garrytan](https://x.com/garrytan/status/2057958284410380793), and [@togelius](https://x.com/togelius/status/2057912236262453607). The common argument: the rule punishes **legal high-skill immigrants** , undermines startups and research, and harms US competitiveness in AI.




**Top tweets (by engagement)**

  * [@deepseek_ai on making the V4-Pro discount permanent](https://x.com/deepseek_ai/status/2057854261699195173) -- the clearest single-market signal in this batch around **LLM inference economics**.

  * [@gdb on "the model alone is no longer the product"](https://x.com/gdb/status/2057670776803996110) -- concise articulation of the current **agent/harness product thesis**.

  * [@AnthropicAI on Glasswing finding 10,000+ critical vulnerabilities](https://x.com/AnthropicAI/status/2057909102542549503) -- one of the strongest data points for **AI-driven cyber capability** moving into production.

  * [@dsp_ on MCP 2026-07-28 RC](https://x.com/dsp_/status/2057780712187580924) -- important protocol update: **stateless MCP** plus first-class extensions.

  * [@GoogleDeepMind on Project Genie + Street View](https://x.com/GoogleDeepMind/status/2057842131142590512) -- notable step toward **consumer-facing world models**.

  * [@cursor_ai on opening the Cursor SDK for custom agents](https://x.com/cursor_ai/status/2057913121558413770) -- relevant for teams building on top of coding-agent infrastructure.




* * *

# **AI Reddit Recap**

## **/r/LocalLlama + /r/localLLM Recap**

[ Read more ](https://www.latent.space/p/ainews-all-model-labs-are-now-agent)

---

## [[AINews] New AI Infra unicorns: Exa, Modal, TurboPuffer](https://www.latent.space/p/ainews-new-ai-infra-unicorns-exa)
*🔬 Latent Space | 2026-05-22*

_Take the[2026 AI Engineering Survey](https://notion.qualtrics.com/jfe/form/SV_bP07tSVMXH7ePCS) and get >$2k in credits and [AIE WF tickets](https://ai.engineer/wf)!_

* * *

[](https://substackcdn.com/image/fetch/$s_!3ckl!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0607846c-4654-4352-83ef-e0dd6e2b580a_1086x280.png)

Congrats to all our past guests who reached huge milestones this week:

  * **[Turbopuffer](https://x.com/Sirupsen/status/2057470756070781400)** : $100M ARR and profitable ([our podcast](https://www.latent.space/p/turbopuffer))

  * **[Exa](https://exa.ai/blog/announcing-series-c)** : $250M@$2.2B Series C ([our podcast](https://www.latent.space/p/exa))

  * **[Modal](https://x.com/bernhardsson/status/2057530320790995262?s=12)** : $355M@$4.7B Series C ([our podcast](https://www.latent.space/p/modal)) 




We really need to be raising that Latent Space fund soon… but meanwhile.. **help us out** by taking the [2026 AI Engineering Survey](https://notion.qualtrics.com/jfe/form/SV_bP07tSVMXH7ePCS) and get >$2k in Notion and Vercel credits and [AIE WF tickets](https://ai.engineer/wf)!

> AI News for 5/20/2026-5/21/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

# **AI Twitter Recap**

**Model, Benchmark, and Research Updates: RAEv2, Gated DeltaNet-2, Data Filtering, and Open Math**

  * **RAEv2 and representation-first tokenization** : Several researchers highlighted **RAEv2** as a meaningful follow-on to Representation Autoencoders for unified vision understanding and generation. [@1jaskiratsingh](https://x.com/1jaskiratsingh/status/2057568174590304421) says the update yields **> 10x faster convergence**, better reconstruction, and better generation, with tests extending to **text-to-image and world models**. A Chinese summary from [@recatm](https://x.com/recatm/status/2057456332861567359) usefully extracts the three main findings: summing the last **K encoder layers** instead of only the final layer improves both reconstruction and generation without added inference cost; **RAE and REPA are complementary** across semantics vs. spatial structure; and REPA can be reformulated as an internal self-guidance mechanism, avoiding extra weak-model guidance passes. [@sainingxi`e](https://x.com/sainingxie/status/2057595509519311077) also points to new evaluation views beyond FID, arguing there is still underexplored headroom in representation-powered pixel decoders.

  * **Alternatives to standard attention and tokenizer assumptions** : NVIDIA's **[Gated DeltaNet-2](https://x.com/ahatamiz1/status/2057586630450610673)** decouples **erase** and **write** operations in linear attention with channel-wise gates, outperforming **KDA** and **Mamba-3** at **1.3B** parameters on language modeling and commonsense reasoning, with notable long-context retrieval gains on **RULER** ; [@rasbt](https://x.com/rasbt/status/2057599925878169761) called it one of the more interesting hybrid-attention directions. On tokenization, [@NousResearch](https://x.com/NousResearch/status/2057610978934546805) released a controlled study of why **subword tokenization** helps, simulating seven hypothesized benefits inside a **1.7B byte-level** pipeline; only **three of seven** interventions moved validation loss at that scale. Separately, [@tatsu_hashimoto](https://x.com/tatsu_hashimoto/status/2057489411768803526) reported a surprising scaling result on **DCLM** : with enough compute, the best data filter may be **no filter** , with projections suggesting the crossover for internet-scale pools lands around **1e30 FLOPs** ; downstream evals appear noisy but directionally consistent ([follow-up](https://x.com/tatsu_hashimoto/status/2057489440273322447)).

  * **Mechanistic interpretability and geometry** : [@GoodfireAI](https://x.com/GoodfireAI/status/2057487848258101551) argues the dominant "models think in curved manifolds, SAEs use straight-line features" critique is only partly right. Their proposed fix is to cluster SAE features by **joint firing patterns** , recovering geometry through **feature groups** rather than isolated atoms ([thread continuation](https://x.com/GoodfireAI/status/2057487927089954962), [post](https://x.com/GoodfireAI/status/2057487939836502461)). This is a useful update to the current SAE discourse: not a rejection of sparse features, but a warning that interpretation should move from single features to structured ensembles.

  * **Math as an AI research domain** : The biggest scientific discussion centered on OpenAI's reported result on an Erdős unit-distance problem. [@markchen90](https://x.com/markchen90/status/2057517045575774598) framed it as evidence that mathematics is currently the domain most amenable to AI-assisted research breakthroughs, while [@wtgowers](https://x.com/wtgowers/status/2057536069218742518) noted that if the reported low human interaction level holds, the result is genuinely interesting. The discourse was immediately shaped by skepticism and benchmark/gameability concerns, with [@memecrashes](https://x.com/memecrashes/status/2057478155246440929) joking that the result was "outdated not even 3 hours later by a human," and [@cloneofsimo](https://x.com/cloneofsimo/status/2057486750004756524) pointing out the predictable "goalpost moving" around what counts as legitimate AI mathematics. The interesting technical meta-point is that math continues to function as a relatively legible frontier for AI co-research because outputs can be checked, debated, and extended.




**Agents, Harnesses, and Developer Tooling: Codex, Gemini, Devin, and Agent Infrastructure**

  * **Harnesses are still a major source of capability gains** : [@lvwerra](https://x.com/lvwerra/status/2057476832664953225) released **physics-intern** , a science-problem harness that boosts models like **Gemini 3.1 Pro from 17.7 to 31.4** , surpassing **GPT 5.5 Pro** in that setup. The notable nuance is that GPT 5.5 Pro itself did **not** benefit from the harness, suggesting model-specific absorption of scaffolding tricks. In the same spirit, [@KLieret](https://x.com/KLieret/status/2057471442066030795) made **mini-swe-agent** runnable on **ProgramBench** , explicitly aiming to improve harness innovation around software engineering agents.

  * **Agent design patterns are maturing from "single agent first" to explicit subagent orchestration**: [@cwolferesearch](https://x.com/cwolferesearch/status/2057486293882282293) gives a practical synthesis: start with **single-agent systems** , and only move to **manager/sub-agent** or decentralized multi-agent topologies when tool sprawl or prompt bloat becomes unmanageable. That advice lines up with more operational observations from users of subagents: [@andrew_locke](https://x.com/andrew_locke/status/2057537633555993058) describes Cognition's sub-Devin workflow as a step change, compressing what previously looked like **2+ engineer-weeks** into a couple of hours.

  * **Codex shipped a substantial product layer on top of the model** : OpenAI's "Codex Thursday" updates matter less as standalone features than as signs of where coding agents are going. [@OpenAIDevs](https://x.com/OpenAIDevs/status/2057530207976989179) launched **Appshots** , which capture both screenshot and text from Mac app windows for richer working context; they also added **team plugin sharing** ([link](https://x.com/OpenAIDevs/status/2057530212339097994)) and more detailed **org analytics** ([link](https://x.com/OpenAIDevs/status/2057530213974814844)). The more important systems shift is remote computer use: [@OpenAIDevs](https://x.com/OpenAIDevs/status/2057536706778378692) says Codex can now securely use apps on your Mac **from your phone even when the Mac is locked**. This is a strong signal that the agent product surface is moving from chat IDEs to persistent cross-device operator workflows.

  * **Gemini 's agent/tool story is broadening quickly**: [@OfficialLoganK](https://x.com/OfficialLoganK/status/2057460544643404125) highlighted that **Gemini 3.5 Flash** ranks **#1 on APEX-Agents-AA** , outperforming larger models. On the applied side, [@_philschmid](https://x.com/_philschmid/status/2057513254856151339) shows a GitHub issue triage agent built with a **single Gemini API call** and no orchestration framework, while [@skalskip92](https://x.com/skalskip92/status/2057502215506473121) demonstrates Gemini 3.5 Flash replacing a custom vision pipeline for lane/car reasoning with one multimodal API call. Google also expanded action surfaces: **Daily Brief** ([announcement](https://x.com/GeminiApp/status/2057500470147698936)) and connected-app actions with **OpenTable, Canva, and Instacart** ([announcement](https://x.com/GeminiApp/status/2057550225863246236)) are essentially consumer-facing agent workflows.

  * **Developer infra is converging around retrieval, streaming, sandboxes, and security boundaries** : Weaviate shipped a built-in **MCP server** inside the database so coding agents can ingest a repo and use **hybrid BM25 + vector retrieval** without extra processes ([announcement](https://x.com/weaviate_io/status/2057476556449010024)). LangChain introduced both a **sandbox Auth Proxy** for controlling agent-world boundaries ([announcement](https://x.com/LangChain/status/2057508777759236401)) and a new **typed streaming protocol** for rendering tools, subagents, media, and interrupts as first-class projections rather than token streams ([overview](https://x.com/bromann/status/2057507753191518602)). vLLM's **Elastic Expert Parallelism** is also notable systems work: [@vllm_project](https://x.com/vllm_project/status/2057602243860574463) describes live resizing of MoE **DP/EP topology** without full restarts, using direct GPU-to-GPU transfers over **NVLink/RDMA** --important not just for scaling but for future fault-tolerant serving.




**Infrastructure, Compute, and AI Business Signals: Modal, Turbopuffer, Hark, and the Compute Race**

  * **The infra layer had one of its clearest "this is where the money is" days**: [@Sirupsen](https://x.com/Sirupsen/status/2057470756070781400) said **turbopuffer** crossed **$100M run-rate** in March, just **19 months after $1M** , while being **profitable** and raising **< $1M**. The company's positioning is straightforward and timely: frontier teams know "the magic happens with AI when it draws in just the right context," which turns a lot of product differentiation into a **search/retrieval problem** ([follow-up](https://x.com/Sirupsen/status/2057470791516844188)). That aligns with broader sentiment from [@swyx](https://x.com/swyx/status/2057543654340710556) that "boring" AI infrastructure, not only glamorous frontier research, is where wealth creation is accruing.

  * **Modal raised big and continues to look like a core AI cloud winner** : [@bernhardsson](https://x.com/bernhardsson/status/2057530320790995262) announced a **$355M Series C at a $4.65B valuation**. Investors and users emphasized the same thesis: rebuilding the cloud stack for AI workloads from the ground up, with strong performance and developer experience ([Redpoint](https://x.com/Redpoint/status/2057532087570166134), [user endorsement](https://x.com/mathemagic1an/status/2057534253790097788)). This sits alongside other signals that agent-native compute is emerging as its own category; [@latentspacepod](https://x.com/latentspacepod/status/2057565350187995260) summarized Daytona's pitch around **60ms sandboxes** , **50K startups in 75 seconds** , and RL/evals workloads now representing roughly **half** of usage.

  * **Compute remains the strategic bottleneck, and the market appears tiered** : [@AymericRoucher](https://x.com/AymericRoucher/status/2057492189626720729) sketched a useful compute taxonomy: **US leaders** (OpenAI, Anthropic, Google, with Meta/xAI joining) in the **multi-gigawatt** class; **Chinese giants** scaling from hundreds of MW toward multi-GW, increasingly on domestic stacks; and **European contenders** such as Mistral at around **90 MW** today aiming for **1 GW by 2029**. The exact numbers are debatable, but the framing is consistent with [@EpochAIResearch](https://x.com/EpochAIResearch/status/2057499893854536185), which notes that even if OpenAI kicked off the recent compute buildout, frontier labs still use well under all global compute capacity, leaving open the question of how much further the buildout can accelerate. Component economics also continue to shift toward memory: [@EpochAIResearch](https://x.com/EpochAIResearch/status/2057531410030997789) reports **HBM** grew from **52% to 63%** of total AI chip component spending from Q1 2024 to Q4 2025.

  * **Capital is flowing to interface/hardware bets as well as infra** : [@adcock_brett](https://x.com/adcock_brett/status/2057462134989263047) announced **Hark** raised **$700M at a $6B valuation** , aimed at GPU infrastructure, future model development, hardware, and multimodal/personal intelligence products. The details are sparse beyond hiring areas--foundation models, infra, speech, computer-use agents, hardware--but the size of the raise shows investor appetite for vertically integrated AI-device bets. Hark also reported a **200-hour** uninterrupted autonomous run for **F.03** ([announcement](https://x.com/adcock_brett/status/2057651077928145235)), though without enough technical detail yet to evaluate the underlying robotics stack.




**Multimodal, Video, Biology, and Robotics: Runway, Carbon, Earth Models, and Open Humanoids**

  * **Video editing and generation are getting more compositional** : Runway launched **Aleph 2.0** and the new **Edit Studio** , letting users edit a single frame and propagate that edit through the rest of the video ([Runway](https://x.com/runwayml/status/2057530497597600169), [product lead](https://x.com/iamneubert/status/2057535909524824226)). This is a practical productization of the "reference-guided edit propagation" problem that multimodal builders care about. Separately, Alibaba researchers' **MIGA** was flagged by [@HuggingPapers](https://x.com/HuggingPapers/status/2057506246899724355) as a **train-free** method for **infinite-frame** video generation with a two-stage alignment mechanism for temporal consistency. On the open-source avatar side, Meituan released **LongCat-Video-Avatar 1.5** with **Whisper-Large** replacing Wav2Vec2, **8-step inference** , long-video identity consistency, and broader stylized-domain generalization ([announcement](https://x.com/Meituan_LongCat/status/2057494106889486646)).

  * **Foundation models for biology and Earth observation continue to become more usable** : Hugging Face Bio's **Carbon** DNA model family got follow-on demos and infra validation. [@LoubnaBenAllal1](https://x.com/LoubnaBenAllal1/status/2057488110263435640) highlighted applications in **sequence design, variant effect prediction, and learned representations** , while [@Shekswess](https://x.com/Shekswess/status/2057468970471448787) showed **Carbon-500M, 3B, and 8B** compiling and running on a single **Trainium2 trn2.3xlarge** with NxD Inference on day one. For geospatial modeling, [@cgeorgiaw](https://x.com/cgeorgiaw/status/2057481909802774664) reported **OlmoEarth v1.1** is **3x cheaper/faster** by changing the tokenization of multi-resolution Sentinel-2 inputs into **3x fewer tokens** , exploiting the quadratic compute savings.

  * **Open robotics is getting more buildable** : Hugging Face's **LeRobot Humanoid** drew attention as a genuinely full-stack open release rather than a showcase demo. [@robotsdigest](https://x.com/robotsdigest/status/2057507896129380581) and [@lukas_m_ziegler](https://x.com/lukas_m_ziegler/status/2057515219946205399) both emphasize the same package: roughly **$2.5k** , **3D-printed** , complete hardware/CAD, calibration/runtime, simulation, identification tools, and training pipelines. The key point is not just affordability; it's repairability and iteration speed for real robot learning workflows.




**Top tweets (by engagement)**

  * **OpenAI / Codex product expansion** : [Codex can securely use apps on your Mac from your phone, even when the Mac is locked](https://x.com/OpenAIDevs/status/2057536706778378692), plus [Appshots](https://x.com/OpenAIDevs/status/2057530207976989179) for richer app context.

  * **Infrastructure winners** : [turbopuffer at $100M run-rate, profitable, < $1M raised](https://x.com/Sirupsen/status/2057470756070781400); [Modal raises $355M Series C at $4.65B](https://x.com/bernhardsson/status/2057530320790995262); [Hark raises $700M at $6B](https://x.com/adcock_brett/status/2057462134989263047).

  * **Research discussions with broad technical resonance** : [OpenAI's Erdős-related math result discussion](https://x.com/markchen90/status/2057517045575774598); [RAEv2 release](https://x.com/1jaskiratsingh/status/2057568174590304421); ["no filter" scaling result for LM data curation](https://x.com/tatsu_hashimoto/status/2057489411768803526).

  * **Agent capability trendlines** : [Gemini 3.5 Flash tops APEX-Agents-AA](https://x.com/OfficialLoganK/status/2057460544643404125); [Gemma 4 E4B driving an iOS simulator on-device via Argent](https://x.com/googlegemma/status/2057570113390551452); [Devin for Windows](https://x.com/cognition/status/2057496130225668360).




* * *

# **AI Reddit Recap**

[ Read more ](https://www.latent.space/p/ainews-new-ai-infra-unicorns-exa)

---

## [Giving Agents Computers — Ivan Burazin, Daytona](https://www.latent.space/p/daytona)
*🔬 Latent Space | 2026-05-21*

_Take the[2026 AI Engineering Survey](https://notion.qualtrics.com/jfe/form/SV_bP07tSVMXH7ePCS) and get >$2k in credits and [AIE WF tickets](https://ai.engineer/wf)!_

* * *

On the product side, everyone is getting Computer - [Perplexity](https://www.perplexity.ai/computer), [Manus](https://manus.im/blog/manus-cloud-computer), [Cursor](https://www.latent.space/p/cursor-third-era), and so on. Meanwhile on the research side, agentic evals like TerminalBench and GDPVal are also assuming computer ([Harbor](https://x.com/swyx/status/2027213347570188635)). On both ends, the consolidating [LLM OS stack ](https://news.smol.ai/frozen-issues/25-05-27-mistral-agents.html)has become a standard toolkit, and Daytona is one of a small set of AI Infra companies that are booming because of it.

_**" The end of localhost"**_ has been Ivan Burazin's obsession for more than a decade.

Something that is all too familiar…

[](https://substackcdn.com/image/fetch/$s_!67Tl!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe0cf76d9-c44f-4ffa-82e5-602a03bae88b_620x412.jpeg)Infobip Shift 2022

Long before agents became the default way people talked about software development, Ivan was already chasing the idea that **development should not depend on a fragile local machine**. _[CodeAnywhere](https://codeanywhere.com/)_ , one of the first browser-based IDEs, was an early attempt at that future: move the development environment into the cloud, make setup reproducible, and free developers from the endless "works on my machine" tax.

The thesis was directionally right, but the market wasn't ready yet.  
  
However, agents changed that. **They do not care about a laptop, desk setup, or favorite editor.** They need a computer they can access through an API: something stateful enough to keep working, fast enough to spin up instantly, flexible enough to resize, isolated enough to be safe, and composable enough to run the messy real-world workflows that real software engineering actually requires.  
  
Daytona isn't just selling _" sandboxes"_ in the narrow code-execution sense. It is **the latest version of Ivan 's original localhost thesis**.

In this episode, Daytona's CEO joins swyx to explain **why AI agents need more than code execution boxes** : they need composable computers, stateful sandboxes, instant startup, dynamic resources, and infrastructure that can survive workloads going from **zero to 100,000 CPUs.**

We go deep on the **new agent compute market** : Daytona's hard pivot from human dev environments to AI sandboxes, **the New Year 's Eve MVP** that customers begged for, why Daytona runs on bare metal with its own scheduler, **how one customer runs almost 850,000 sandboxes a day** , and why RL/eval workloads went from 0% to roughly 50% of usage in just months. Ivan also explains **why agents need Windows and macOS machines** , why CLI may matter more than MCP, why Kubernetes is painful for this workload, and why the future AI cloud may look more like Stripe than AWS.

* * *

**We discuss:**

  * How Daytona **grew out of CodeAnywhere** , Shift, and the "end of localhost" thesis

  * **Why Daytona pivoted** from human dev environments to AI sandboxes

  * Why agents **need composable computers** instead of **disposable code execution boxes**

  * **The New Year 's Eve MVP** that customers chased API keys for

  * Why Daytona chose **bare metal, stateful snapshots, and its own scheduler**

  * How Daytona spins up one sandbox in **~60ms and 50,000 sandboxes in ~75 seconds**

  * Why Daytona's biggest customer runs **~850,000 sandboxes a day**

  * How RL/eval workloads create **zero-to-100,000 CPU spikes**

  * Why RL workloads went from **0% to roughly 50%** of Daytona usage

  * Why customers compare Daytona against **EKS/GKS** and say they're **" never going back"**

  * **Why every AI agent may need a computer** , including Windows and macOS environments

  * The Apple licensing constraints that make macOS sandboxes hard

  * Why **CLI** gives agents more power than **MCP**

  * How **open source** helps agents integrate Daytona

  * Why agent-generated PRs may **break today 's CI/CD assumptions**

  * Why AI SaaS companies **reselling tokens** may face a cold shower

  * Why the AI cloud may look more like Stripe than AWS




* * *

**Ivan Burazin**

  * **LinkedIn:** &lt;https://www.linkedin.com/in/ivanburazin>

  * **X:** &lt;https://x.com/ivanburazin>




**Daytona**

  * **Website:** &lt;https://www.daytona.io>

  * **X:** &lt;https://x.com/daytonaio>




* * *

## Timestamps

  * 00:00:00 Hook

  * 00:01:12 Introduction

  * 00:03:15 CodeAnywhere, Shift, and the end of localhost

  * 00:05:58 What Daytona is: composable computers for AI agents

  * 00:08:07 The pivot from dev environments to AI sandboxes

  * 00:10:17 The New Year's Eve MVP and customers begging for API keys

  * 00:12:56 Bare metal, stateful sandboxes, and Daytona's scheduler

  * 00:17:28 60ms startup, 50,000 sandboxes, and 850K daily runs

  * 00:21:53 Spiky RL/eval workloads and the new agent infra problem

  * 00:28:12 RL workloads, Kubernetes pain, and dynamic resizing

  * 00:33:31 Why every AI agent needs a computer

  * 00:38:48 macOS sandboxes and Apple's licensing problem

  * 00:44:28 Why CLI may matter more than MCP

  * 00:48:11 Open source, GitHub stars, and agent integration

  * 00:53:11 Git, CI/CD, and agent collaboration bottlenecks

  * 00:58:15 Founder life and building a 25-person infra company

  * 01:02:44 AI SaaS, token resale, and API-first business models

  * 01:06:10 GPU sandboxes, data centers, and compute growth

  * 01:09:48 Why the AI cloud may look more like Stripe than AWS

  * 01:11:26 Closing thoughts




* * *

# Transcript

## Introduction: Daytona, CodeAnywhere, and the End of Localhost

**Swyx [00:00:02]:** Okay, we're in the studio with Ivan Burazin, CEO of Daytona. Welcome.

**Ivan [00:00:07]:** Thanks for having me, man.

**Swyx [00:00:08]:** Ivan, you and I go back.

**Ivan [00:00:10]:** Way back.

**Swyx [00:00:11]:** How I don't even know how, you found, did you reach out or, for Shift.

**Ivan [00:00:17]:** I reached out to you. The reason was you - we were just - we were thinking about I was one of the co-founders of CodeAnywhere, the first browser-based IDE, and so we were thinking a long time of, localhost should die. And you had this article.

**Swyx [00:00:29]:** End of localhost.

**Ivan [00:00:30]:** Then I reached out to you because of that, and then we talked, and I was actually at a different job and learning about I was the head of, developer experience, and you were quite well-versed in that, and I actually reached out to you, among other people, how do we go about that? What are the key things and whatnot at this point in time? And you were nice enough to take the call, and I remember I was late on your call with you.

**Swyx [00:00:51]:** I don't remember.

**Ivan [00:00:52]:** I remember because I was with my then I'm thinking of a girlfriend or wife at that point in time, I'm not sure. It's the same person, so that's great, and I was late 'cause we were, in, Italy on, vacation, and then I was late for something. I felt so bad, and you were so nice to be, good about.

**Swyx [00:01:10]:** The reason I'm nice is because I'm also late to other people, so it's like, who's, who's without sin here, yeah, so I have to, for those who don't know, InfoBip Shift, there's this whole thing that, you did in the past, and, and that was basically one of the inspirations for me starting AI Engineer, which is like, I have to thank you for giving me that push to be like, "Oh, you can, you can build and sell conferences?"

**Ivan [00:01:34]:** I remember you asked you asked me at the beginning to give me advisory shares, and I was so focused on what we were doing, I said no, and I should've took the advisory shares. So I'm sorry, dude. But anyway.

**Swyx [00:01:43]:** We're not, we're not venture backed.

**Ivan [00:01:44]:** No, it doesn't matter.

**Swyx [00:01:45]:** It's Yeah, anyway, so I think what's impressive about you is that CodeAnywhere is the thing that you've been trying to build, and, you kind of put it on hold and then came back after InfoBip. Just give us the story, do you - the story and the origin story, going into Daytona.

## From CodeAnywhere and Shift to Daytona

**Ivan [00:02:05]:** Sure. Like, really way back, me and my co-founder have been together. I say this, I've said this multiple times, it's like we were married and divorced and married. Some people actually ask me is my co-founder my partner. they thought it literally. It's not literally, but we have done multiple companies together, and to your point, we had this shift where we went from the CodeAnywhere to the conference called Shift, and then back to, Daytona. We originally started stacking servers, doing like virtualization in the early 2000s and, routers and doing basically all these things, at a foundational level, and that was a services company which we sold to focus on what my co-founder actually invented, which was the very first browser-based IDE, right, I say the first. Before us was actually Heroku. They did it for a very short time until they became Heroku. But outside of them, we were the only one, and it was called.

**Swyx [00:02:55]:** There was Cloud9.

**Ivan [00:02:57]:** Cloud9 came out slightly after us. There was Replit, which came out when we stopped doing it, Replit came out, and they have been successful since then, which is great. There was Nitrous.io. There was quite a few that existed at the time, but it was like too early. But the interesting part is that we, at that point in time, because there was no VS Code, there was no Kubernetes, and Docker had just started when we Or I'm not sure if it was even public at that point in time. And so we had to build everything to the whole stack ourselves and that was the key learning that we brought into and that we've been using in Daytona today. So it was super early. There's about 3 million people used CodeAnywhere. It was slightly, it was angel-backed more than venture-backed. We ended up paying everyone back because it didn't have that sort of scale. But, three years ago, we started something similar with Daytona, which is not what we are today, but it was automating dev environments for human engineers, the basically the underlying stack of CodeAnywhere. And then we did a hard pivot last January to sandboxes. And so here we are.

**Swyx [00:04:01]:** Historic pivot, yeah, and, it's one of those things where, I had independently invested in CodeAnywhere, but also in E2B, and then both of you pivoted into the same thing, and I'm like, "Fuck."

**Ivan [00:04:12]:** You invested, you invested in Daytona. You invested in Daytona. But you were the first If we had not got your check, we wouldn't have done it.

**Swyx [00:04:18]:** No way.

**Ivan [00:04:19]:** No, it was like, "We have to get him on board first," and you were that kicker that we, that got us off the ground.

**Swyx [00:04:23]:** No, because you were putting me on your pitch deck, man. I was like, "Man, this is like a good trip if I don't invest."

**Ivan [00:04:29]:** That's because it was your quote. It's like we.

**Swyx [00:04:30]:** Yeah. It's the end of localhost.

**Ivan [00:04:31]:** Did a bunch of research about end of localhost and who was interested in that,.

**Swyx [00:04:34]:** No, that's like, I put, I wrote that blog post, and every single company in that field reached out to me, and then every VC who was receiving those pitches then also had to call me and, talk it, talk through it with me.

**Ivan [00:04:47]:** It's finally happening though.

**Swyx [00:04:48]:** It was really super interesting.

**Ivan [00:04:48]:** It's finally happening.

**Swyx [00:04:49]:** It's finally happening.

**Ivan [00:04:49]:** Yeah, it's finally.

**Swyx [00:04:49]:** It's finally happening, with maybe sort of non-human users. Yeah, so what is Daytona today? Let's get like a quick description. I'm wearing the shirt.

## What Daytona Is Today: Composable Computers for AI Agents

**Ivan [00:04:58]:** You're wearing the shirt. Yes,.

**Swyx [00:04:59]:** It says, I think your branding is very good. Like, it's very consistent. It runs AI code. Like, it cannot be simpler.

**Ivan [00:05:05]:** Exactly, but we're gonna probably have to change that.

**Swyx [00:05:07]:** Oh, shit.

**Ivan [00:05:07]:** It's also a subset of what we do. Unfortunately, we really love this, Run AI Code is super simple. People interpret it different ways. I think we've given out 5,000, 6,000 of these shirts. People wear them with pride because it doesn't really market about us.

**Swyx [00:05:21]:** Yeah, Daytona's on the back.

**Ivan [00:05:22]:** It markets the back. It markets to the person itself, so I think we did a really good job on that one. But it is also a subset of what we do, because people, when they think about Run AI Code, they just think about these small, let's call it isolates, code execution boxes that, you send some code, you get an output. Whereas what Daytona is today is essentially composable computers for AI agents. It is, the market calls them sandboxes which can be misleading.

**Swyx [00:05:44]:** All these things. All these things on.

**Ivan [00:05:45]:** Yeah, exactly, 'cause it can be misleading 'cause people usually think about sandboxes as a demo or a test environment versus a production-grade environment. But what Daytona does, if you think of the laptop that you have in front of you or the computer that's over there, or, my wife is an architect, so she has like a Windows with a 3D graphics card inside to do 3D rendering. Like, as humans, we have different computers or different compositions of computers. And our belief is strongly that agents today and going forward will need all these different compositions of computers to do different types of tasks. And so we offer that basically through an API.

**Swyx [00:06:19]:** Yeah, to give people - I'm trying to sort of front-load all the aha moments or the wow moments so that people can, stay engaged and click like and subscribe. the market is exploding, right? Like, you have been reporting 74% month-on-month growth, and it also, it's just been growing for a while. Like, it's been going like this. And every single - It's not just you guys. It's every single.

**Ivan [00:06:41]:** Everyone, yeah.

**Swyx [00:06:42]:** Sort of, compute provider. I don't know if you agree with me saying compute provider or not.

**Ivan [00:06:48]:** It's fine.

**Swyx [00:06:48]:** Yeah. So like organically PLG-driven growth, but also enterprise is doing super well, I think I wanna rewind to January of last year when you did the pivot. Like, so you obviously called this market early, and you were positioned for it, and you are now one of the market leaders. But what was the insight that made you do the pivot?

## The Pivot: From Human Dev Environments to Agent Sandboxes

**Ivan [00:07:06]:** The insight that made us do this pivot is the quarter before that, so end of 2024, when we had - Basically, we did a demo with - I don't I think we discussed this as well, Devin was not public. You actually gave me access to Devin at that time. So Devin.

**Swyx [00:07:25]:** I did?

**Ivan [00:07:26]:** Yeah, you gave me access.

**Swyx [00:07:26]:** I don't think I was supposed.

**Ivan [00:07:27]:** Yeah, exactly.

**Swyx [00:07:28]:** Yeah, I.

**Ivan [00:07:28]:** So it doesn't matter. You.

**Swyx [00:07:29]:** Yeah. I gave like three friends access.

**Ivan [00:07:31]:** Yeah, or it was a call and you showed it to me. It doesn't matter. but OpenDevin was available, which is now called OpenHands. And so we're like, "Oh, this seems to be a thing. This is not public. Let's take our for human automation of dev environments and take, OpenDevin and launch that as a SaaS." And we did that. Not very many people signed up and used it, but a lot of people reached out that were building agents, and they were like, "Hey, my agent needs a compute sandbox runtime," whatever you wanna call it. I forgot what it was called at that point. And then we were like, "Oh, amazing. This is a new market. Here is our infrastructure. Here's our product, and go." And what we found really fast, soon, was that people did not like what we had built. It didn't work. And I remember talking to people at the beginning when we're doing this, the sandbox we're building for agents. People were like, "Oh, why is it different? It's the same thing. We have like EC2, we have VMs, we have all these things." But we saw that everyone we gave it to, it was like 20, 30 people, they all said, "No." Like, "This is not what we need. This sort of breaks." And basically, me and my co-founder not knowing a lot about - 'cause we're infra people. We're not AI people. So I basically took it upon myself to like watch every single podcast that exists, including all of, all of these and all that, and sort of get up to date, read all the blogs, like get, understand what's going on.

**Swyx [00:08:45]:** Do you wanna shout out who else was useful, just in case people are also looking.

**Ivan [00:08:49]:** Generally we -, I looked at There's a few of podcast, different segments and different types. So there's you guys, No Priors, Bill Gurley's was great while.

**Swyx [00:09:04]:** VG2, yeah.

**Ivan [00:09:05]:** Yeah, while it was around. So there's a few. 20VC is interesting from a different dynamic, and some are different dynamic. But there was, also Red Points.

**Swyx [00:09:14]:** We're not really about the compute market.

**Ivan [00:09:15]:** It was also already - Sorry?

**Swyx [00:09:16]:** You're, you want - You're looking at the agent infra market.

**Ivan [00:09:19]:** I was looking at the agent market and the AI market in general and sort of understanding who are the players, what the perception, and how that goes. And like obviously you complement this with like going to conferences, going to events, going to meetups, reading white papers, like doing all the things that you have to do to understand what's happening. And so when we figured, when we sort of had an idea of what we had to build, literally over the New Year's Eve, literally on New Year's Eve, I half vibe coded the first MVP, first minimal viable product of what Daytona is today. And I went to sleep at like 3:00 AM or something like that. I was doing - I just put my like baby daughter and wife to sleep and, Happy New Year's, and go back to just, doing this. And I sent it to my co-founder, my CTO, and he saw it in the morning. He's like, "This is absolute garbage." "Do not show this to anybody at all, but the idea is good." And so he took two weeks, and he rebuilt it.

**Swyx [00:10:09]:** Did it like look like that? Listen, I - It was rough idea.

**Ivan [00:10:12]:** Oh, not even, not even close. Like it was it was way worse. But it was like a very - It was a simplistic view of what it should be. Like, it worked, but it was not ideal. And so he went, we went down the whole, which is his job as CTO, to go, and he came back with this version. We then called all the people that had said like, "This is garbage," a quarter ago. And we set up these calls, and we gave it to - We just demoed it to everyone. And all the calls went long, every single one. They were 15-minute calls, and they all went to like 25, 30 minutes or whatnot. And everyone said, "We need, we want access." There was no login, just an API key, 'cause it was just a beta or an alpha. And they said, "Oh, we want access." And we're like, "Sure, yeah. Okay, thank you very much." But after like the next day, if we'd not send it, every single one, like every call that we did, everyone came back, "Where is my API key?" Like everyone wanted it. We're like, "Shit." Like this is it. Like I've never felt So one, the understanding to your point was like most people thought it was the same infrastructure for humans and agents. We understood a quarter ago it's not. We just didn't know what was the right primitive. And then when we came, and we can talk about what that is, and we gave it to these people, I've never seen, I've never experienced - I've done multiple companies in my life. I've never experienced this, that people literally call you if you do not give them access. Like they want access right now. And so it's like, okay, they don't want this. the thing that they want doesn't seem to exist, or they have not found it, and they really want what we want. And then when we understood that we're onto something, and then when you think about the size of the market, like the market for human engineers and enterprise is a very large market, so think GitLab or whatnot. But the market for every single agent that will exist ever in the future is just like, what is that market? How big is that? And we're like, "We are all in on this." And so that is where we made sort of the cut between the old product and the new one.

## Bare Metal, Stateful Sandboxes, and the Lambda + EC2 Model

**Swyx [00:12:02]:** Yeah. But it wasn't composable at the time?

**Ivan [00:12:05]:** It was very - It was basically just a Linux box that you could change, that you could define number of CPUs, disk, and RAM. Like that is what you could do, but you couldn't have multiple operating systems, you couldn't resize it on the fly, you couldn't add a GPU, you couldn't do like all the things. It was just the, just the first sort of variation of that, yeah.

**Swyx [00:12:22]:** Was it bare metal from the start?

**Ivan [00:12:24]:** It was bare metal from the start. And so the interesting thing that we thought about right away, so our.

**Swyx [00:12:29]:** Which, give people the background, what is the normal path?

**Ivan [00:12:32]:** Yeah, so, basically most providers run this on top of VMs. And also.

**Swyx [00:12:37]:** Firecracker.

**Ivan [00:12:38]:** Yeah, they run on Firecracker and VM. And so we also fire - We can get - We have multiple isolation layers and we can do that. But the common way to do it is that they, one, that the state of the machine, or the hard disk is not part of the sandbox itself. And the other thing is they're not meant to last forever. So most of them are preemptible, like they can There's a time that they can live. And so our thought was when we were going into this is, agents will be like humans in the sense of you don't want your laptop to be shut down until you're done with work. Like, and you want to close the lid and open the lid, it's the same state. So you - Agents would want that, like the pause and come back. They want those two things. But also agents really want speed, right? Can they get it? So when we thought about it's like we need something insanely fast, how to make it fast, how to make it long-running, and stateful. And so those two things, it's like combining a Lambda and an EC2, right? Those two things together. And so we didn't have an idea how others did it, 'cause we didn't know too that there was a market around this. It was more like, okay, this is what we need, what they need. And we looked at Kubernetes, it wasn't wasn't good enough for that. We looked at Nomad, it didn't enable that. And so our history in rewriting our own scheduler at CodeAnywhere is basically what my CTO came up with. Like, he's like, "Oh, the learnings from there," and he brought it. And the funny thing is, our third co-founder, when he saw it, he's like, "Dude, what is this? This is like 2008." Like, we went back in time, and he's like, "Exactly." And so the reason why Daytona is like super fast, and you see this on benchmarks, is we essentially, we run on bare metal. We have our own scheduler, we use the underlying, disk, CPU, and RAM of the underlying machine, which means your IOPS are insanely fast because there's no, there's no network between an EBS or something like that. But also the snapshot, the point in time, the templates, are also preloaded on the bare metal machines. So when you fire off a sandbox from a template or a snapshot, you're essentially directed to the bare metal machine where that snapshot is based on that NVMe drive, and then it literally just turns on that machine, and it's local. There's no network latency, anything on there. And so that is sort of the specificities that we, when we're thinking from first principles, what a computer would look like for an agent, that is what we came up with, and that's what we created.

## Benchmarks, 60ms Startup, and 50,000 Sandboxes

**Swyx [00:15:02]:** Yeah. I should maybe, I don't know if you endorse this, but there's someone that does compute SDK, you guys do very well on there, with like the TTI, right? I. is this a, is this a is this a relevant benchmark for you guys? I don't know.

**Ivan [00:15:16]:** I don't know, and it changes every day. So today RKL is.

**Swyx [00:15:18]:** I don't know what RKL is. Never heard of it.

**Ivan [00:15:20]:** Yeah. RK, yeah, so it is there.

**Swyx [00:15:22]:** You are, at least a third of the next tier of performance, and then, there's a lot of other better-known names that are very slow to start.

**Ivan [00:15:31]:** Yeah. We've been the number one by far for a long time, and now there's different, there's different definitions also of sandboxes, different isolation patterns, different other things. So RKL runs it literally on the S3, the data, so it's very different, and they spin up a sandbox, spin up a container for that, so it's a different type of thing. So the definition of a sandbox is something that we can all, we all need to get along with. But yeah, we're insanely fast on getting these things, up and running. And so you can see even there that it's a zero point 0.10 to 0.11, so.

**Swyx [00:16:03]:** Close enough. Yeah. what else do you need, right?

**Ivan [00:16:05]:** Yeah. So the benchmarks itself, so, in this, in I don't think the benchmarks equate to market ownership or revenue or anything like that. and I've seen this with multiple benchmarks, not just in sandboxes, but in general benchmarks around.

**Swyx [00:16:20]:** It's table stakes. It's just like.

**Ivan [00:16:21]:** Exactly. But it doesn't hurt.

**Swyx [00:16:22]:** Just roughly check.

**Ivan [00:16:22]:** Like you definitely have to be up there and you have to be competing so that people know that, oh, this is definitely one of the top. Because this is only one dimension of what customers look for. There's other things like how many can you spin up consecutively? There's a feature set, there's support, there's like all different things that people look at, but you definitely have to be there, on the benchmarks.

**Swyx [00:16:40]:** How many people do people spin up consecutively?

**Ivan [00:16:43]:** So we have.

**Swyx [00:16:43]:** Or concurrently, is the Concurrency, right?

**Ivan [00:16:45]:** There's three metrics that we look at. And so one is like time to spin up one, and so our time to spin up one is 60 milliseconds with network latency. So request, spin up, reply, 60, the whole thing, 60 milliseconds. That is one. But if you wanna spin up 50,000 at once, we are now at about 75 seconds. So it takes about 75 seconds to spin up concurrently 50,000. Some others, there's public data around this, like take 2,000 seconds, which is 30 minutes. Like there's different variations of that. And then there is the so it is speed of one, speed of like multiple, and then how many can you consistently have up and running. And so we basically have right now no limit to how much we can add because we basically own our own metal. But the biggest customer of ours does like about 850,000 every single day is sort of where they're, where they're just shy of a million every single day that they're running, we do have a request for half a million concurrent, which is literally half a million CPUs somewhere running. So that's an interesting.

**Swyx [00:17:44]:** They pay by like vCPU seconds.

**Ivan [00:17:47]:** By seconds, yeah.

**Swyx [00:17:47]:** Or whatever. Yeah. Okay, and so and then, and the other thing is, the sleeping and the resuming, 'cause it's all the stateful resumption of all these things, how, what kind of workload are people putting through this, right? Like how is it Do we measure by gigabytes in memory, gigabytes in storage? I don't In like network attached storage. I, what are the costly ones of, out of all these features?

## Workload Economics: CPU, RAM, Network, and Storage

**Ivan [00:18:15]:** The most expensive thing are CPU.

**Swyx [00:18:18]:** Okay. Yeah, of course.

**Ivan [00:18:18]:** The second one, yeah Then it's RAM, then it's disk. We actually don't charge.

**Swyx [00:18:22]:** Which is snapshotting, right?

**Ivan [00:18:23]:** No, it's actually the, snapshotting's part of it, but basically the size of your hard disk, of your machine. So do you have 10 gigabytes, do you have 20, do you have 50, do you have whatever? And then the transference of that. Right now, currently we don't charge for, network at all at Polychron.

**Swyx [00:18:37]:** Oh, you gotta, yeah, you gotta fix.

**Ivan [00:18:38]:** Yeah. It is very much a it's a larger and larger part of our bill, so we're working around, that part there. Obviously, that is the least, expensive, so the hard disk is the least expensive, so it's basically CPU, RAM, for us network, 'cause we don't charge the customer, and then hard disk, is how it's split up. But there's also different types of workloads, so we basically split it up into two types of workloads in Daytona. One is what we call background agents or long-running agents. and the other is, basically RLs and evals, which I put sort of together. And so they have very different patterns of usage, and if you look at the usage of a background And I'll just name names of companies, not specifically.

## Background Agents vs. RL/Evals: Two Usage Shapes

**Swyx [00:19:21]:** Yeah, open, all hands.

**Ivan [00:19:23]:** Yeah. So like a background agent's a Cognition, a Lovable, a like all these things are Harvey. These are all long-running, background agents. And so if you look at their usage patterns, their usage patterns are similar to human, which is like follow the sun. Basically, the usage patterns of that is like noon is probably the highest, and the midnight is the lowest, and then weekends are lower. weekday is higher.

**Swyx [00:19:42]:** Yeah, that's a fun question. How global is it? Is it very US-centric or?

**Ivan [00:19:46]:** The US is a large part, but we have currently, we have Asia, Europe, and the US regions.

**Swyx [00:19:52]:** So it's quite global.

**Ivan [00:19:53]:** Yeah, it's quite global. We have it all over. It's interesting that our I talked to you a bit about this. Our number one city by user.

**Swyx [00:20:01]:** Hmm.

**Ivan [00:20:02]:** Is Singapore.

**Swyx [00:20:04]:** Oh, wow. Amazing.

**Ivan [00:20:05]:** Which is an interesting one, right? Not by revenue, just by just like by individual head count.

**Swyx [00:20:09]:** Really?

**Ivan [00:20:09]:** Just like an interesting thing.

**Swyx [00:20:10]:** Singapore is, Singapore is weirdly high in the adoption charts of AI for the population. It's like an, seven, eight million population. And it's like keeps showing up.

**Ivan [00:20:20]:** No, it's quite interesting. We were quite shocked, and I was like, "Oh, this is interesting." And also one that's up there.

**Swyx [00:20:24]:** There's a reason I'm doing AI using Singapore. it's because I'm from there.

**Ivan [00:20:27]:** We're there. We're gonna, we're gonna be there as well. and it's interesting that Japan is in the top or like Tokyo's in the top, which is in all the tech cycles it has never been. It has never been, so it's quite interesting that they're.

**Swyx [00:20:39]:** I think the Japanese just love AI. Yeah. It's that, and then it's Brazil. That's it.

**Ivan [00:20:44]:** Brazil has always been in.

**Swyx [00:20:45]:** I think.

**Ivan [00:20:46]:** Even when I look, if you look at like GitHub's data and ask historically with CodeAnywhere, it was always like US, Western Europe, and then you'd have like India, Brazil, China, like that would be there. But like Singapore was not in, specifically Japan was never in sort of that top, that top.

**Swyx [00:21:01]:** Yeah. Weird pockets.

**Ivan [00:21:01]:** Weird. Yeah, so it's very global.

**Swyx [00:21:02]:** Okay, so actually that, but that's helps you to distribute your load through, all time?

**Ivan [00:21:08]:** The interesting thing is like we have those kind of loads, but if you look at the researcher loads, they're quite different. So what they are is like if you give them concurrency of 10,000 or 50,000 or 100,000 CPUs at ARMb, when they fire off a run, it's just 100%. And then it just runs, and then it stops. So it's very, the usage pattern is squares basically, right? And it's also not follow the sun, because people will fire it off at midnight before they go to sleep but then wake up and so it's very unpredictable, so you don't know where that is. So the shapes of the usage are quite different than we have had before. And also what's interesting is when it's sort of a follow the sun, even if you have a high growth company, you can sort of predict your usage patterns and have enough capacity for that, because it's sort of, it grows in a, in a way you can project. When you have companies doing sort of like evals and RL, they're super spiky. So they're gonna come in, it's like, "We're gonna use nothing, then can we have 100,000?" Right? And then go back down. And then 100,000, go back down. So it's very different, right? And.

**Swyx [00:22:09]:** Do you want to lock them into commits so.

**Ivan [00:22:11]:** Yeah, we do.

**Swyx [00:22:12]:** Yeah, okay.

**Ivan [00:22:12]:** We so we have to lock them into some sort of commits to have that capacity, because we have to have, basically we have to have the capacity for peak. Right? And so right now, Daytona's mean utilization is 15%, 1-5.

**Swyx [00:22:25]:** Oh my God.

**Ivan [00:22:26]:** So it's very low.

**Swyx [00:22:27]:** Because it's very spiky.

**Ivan [00:22:27]:** It's very spiky, but we get up to 90%. so we have these things. And so what we're, what we're looking at right now as a company is similar to Cloudflare where you can like geo move things around, but that works really well for basically the background agent where it's follow the sun. But this, it's not. Like it's a very different shape. Obviously with scale you figure these things out, but that's an interesting new problem that we have, as a compute provider in the agent space. And when we were doing the conference recently, and so we talked to like Nikita from Neon and.

**Swyx [00:22:57]:** I should bring it up.

**Ivan [00:22:58]:** Parag from Parallel and whatnot, everyone has the same problem. Whereas the usage is super spiky, and this is something that has not happened before, that you have these types of like it was always, it the amplitudes were not this high, right? So it's quite interesting use case and problem solve.

## Compute Conference and Spiky Agent Infrastructure

**Swyx [00:23:12]:** Yeah, I don't know if we're gonna bring this up again, but let's just talk about the conference, you had like 1,000 something people at the Warriors game, at the Sorry, where is it? What's.

**Ivan [00:23:22]:** Chase Center.

**Swyx [00:23:23]:** Chase Center.

**Ivan [00:23:23]:** Chase Center.

**Swyx [00:23:24]:** I went. It was, it was very impressive. Obviously, you can, how to throw a conference, what did you learn? you put, you pulled together all these impressive names.

**Ivan [00:23:33]:** What I.

**Swyx [00:23:34]:** What were you looking for?

**Ivan [00:23:35]:** My thesis behind the Compute Conference was let's bring together people that are building infrastructure for AI agents. Because when I think of what we're building, it is the agent is the primary user, what are the ergonomics and usage patterns of agents, and so we can do that. And what I found, this was a theory, it wasn't proven, is that we all have these problems, as I touched onto. And I was, as I was talking on stage, it was like we all have the same underlying infra problems, which is this spiky workloads, unpredictable workloads that we've never had before, in human, compute or human infrastructure. And it's, again, it's the same when I was talking to Parag or when I was talking.

**Swyx [00:24:20]:** Lynn. Nikita.

**Ivan [00:24:21]:** Lynn, Nikita. Lynn especially, I was talking to her the other day as well. Like the It is a very interesting type of problem to solve because I can touch on Cloudflare because there's a lot of like talk about that recently as to how they solve that, which is they have a bunch of geos, and basically, as users work in different places, and depending on your tier, they can move you around the geos. And so that how, that's how they get the higher utilization. But you can sort of predict these, and it's If it's something in You'll rarely get a spike that is 10 orders of magnitude. Like you'll get a like let's say one of your customers has some like an exponential curve. What is that to I'm using Cloudflare as an example. 10%, 20%, whatever it is. I don't, I don't have this data, I'm just assessing. It's surely not 10x, right? It's surely not something there. And so how do you go out and solve this problem? And we're all solving this in different ways. So we have.

**Swyx [00:25:11]:** She also has the same thing.

**Ivan [00:25:12]:** Yeah, I know specifically that like Neon had that issue as well. Like how are we solving these spiky loads and things like that 'cause we talked about it. And so the interesting thing for me to actually internalize was, yes, everyone that's building for agents first is going through this, and we're all solving similar problems, which is quite.

**Swyx [00:25:28]:** Let me let me double-click on this. Okay. So for example, Neon, I happen to know that they're very sort of S3 oriented, right? so they're just like fully bet on S3. And you get to benefit from S3's distribution and infrastructure. So I would imagine that Neon doesn't have to care, whereas Lynn maybe has to care a bit more because obviously she's doing GPU inference. And, for listeners, we did an episode with her, one and a half years ago. And you have to care. But like, right?

**Ivan [00:25:54]:** Parag cares for sure, and Nikita.

**Swyx [00:25:58]:** And Parag is C of, Parallel.

**Ivan [00:25:59]:** Parallel, yeah.

**Swyx [00:26:00]:** Former CTO of Twitter.

**Ivan [00:26:01]:** Twitter, yeah.

**Swyx [00:26:02]:** They are the search.

**Ivan [00:26:03]:** Yeah, they're search, yeah.

**Swyx [00:26:03]:** I You and I know but the listeners don't know.

**Ivan [00:26:08]:** Yeah, we can put it down in the screen, and so 'cause we, when we were talking.

**Swyx [00:26:11]:** I'll put it up on the, on the screen.

**Ivan [00:26:12]:** Yeah, right.

**Swyx [00:26:12]:** People can look it up if they need.

**Ivan [00:26:14]:** Look it up. And, yes, but they still have CPU and RAM, allocation that you have to have up and running. And so CPU and RAM, you have to allocate that and have that ready. And so there's basically two ways to do it. One is you either over-provision and you can handle the bursts, or two, you basically have, I don't know if this is a term, just-in-time compute, which is like as your load becomes, as your usage comes in, you can fire off requests for VMs or bare metals at other cloud providers and then get them up and running.

**Swyx [00:26:43]:** This is if you go above 100%, right?

**Ivan [00:26:45]:** Yeah, this is.

**Swyx [00:26:46]:** Like your overflow.

**Ivan [00:26:46]:** If your overflow, like spillage or whatever you do.

**Swyx [00:26:48]:** You probably lose money on it, but it doesn't matter, right?

**Ivan [00:26:50]:** It, not Well, you might, you might not That is a more cost-effective way to do it but it's a slower way to do it. Because basically what you have to do is you have to like queue your requests, spin up these just-in-time compute, get it all ready, provision it, and then get your workload there. And so if the time isn't important that much, that's fine, and you can do that. But if your customer, and especially for, let's say, the RL training runs, the reason why a lot of people come to us is because GPUs are more expensive than CPUs, right? So you want your GPU running at, what, 100% the entire time. And so when you're running runs on CPUs, when the when the CPU cycle is like down and spinning up the next one, you want that to be instantaneous so that your GPU doesn't go down, right? And if you then have to like go out and provision machines, you're essentially telling the GPU that it has to wait, and that's incurring our cost. So there's things that you have to try to solve for there.

## RL Workloads, Declarative Images, and Kubernetes Replacement

**Swyx [00:27:43]:** Yeah, let's talk about the different workload, right? You said that, what was it? A few months ago, you had zero RL workload and now it's 50%.

**Ivan [00:27:52]:** It will be this one, 50%, yeah.

**Swyx [00:27:54]:** Let's talk about how different it is, right? Like I imagine, for example, a lot less dynamic code generation of like arbitrary code. Like here, it's probably all the same code. You're just doing parallel runs or something, I don't know.

**Ivan [00:28:05]:** Yeah. So you'll have multiple Depends on the like for each run, you'll have a snapshot. And they, for the most part, they actually do use our declarative image builder, which is like, "Oh, we, the agent wants these dependencies, these env vars."

**Swyx [00:28:17]:** These ones, yeah.

**Ivan [00:28:18]:** Yeah, the declarative image builder, it.

**Swyx [00:28:20]:** Which is a very modal like thing that they.

**Ivan [00:28:22]:** Yeah. And so we build it on the fly and then we propagate that snapshot, and you can spin up as many sandboxes as you want against that snapshot. And then if you have to do changes, the model can, or like it could be also be automated. It's like, "Oh, now for the next run, we need to install these things or remove these things or whatever to get, a task done," and then it goes off and runs that. So yes, that is something that it seems that they prefer. The number one reason I found, or should I say, let's take a step back. What we are competing against in that environment is essentially managed Kubernetes. So EKS, GKE, whatever. That is what the vast majority run on. And anyone that has tried Daytona versus GKE, EKS is like, "I'm never going back." That has always been. There's a few reasons. One is the ergonomics. So if you have, if you're using Kubernetes to spin that up, you have to essentially manage the interface interactions with that. Daytona, although as a compute provider, it's more akin to a Twilio and Stripe from a consumption perspective than it is an AWS. Like you have an API, an SDK, it's quite like easy and seamless to get these things up and running, that's one. The other is the speed to which we spin up, which we mentioned earlier, which is much faster, and the scale to which we can go to. We haven't got into features, but an interesting feature is that it's very hard to OOM, or out of memory, our sandboxes, because we can dynamically on the fly.

**Swyx [00:29:48]:** Resize.

**Ivan [00:29:49]:** Resize, which is like impossible on almost any other thing. There are some technologies that enable you to do that, but it's like a very hard thing. And so we actually saw this when, the Terminal Revenge team is, brought us actually. So thank you, Alex and the team, that brought us into this whole space.

**Swyx [00:30:05]:** It's just very rare that, a framework would just say, "Guys, just use Daytona."

**Ivan [00:30:11]:** Yeah, I think it says it somewhere. Yeah.

**Swyx [00:30:13]:** Yeah. I was like, "What is this?"

**Ivan [00:30:15]:** There's all, there's multiple there, but they also mention a few other places. and so Daytona specifically-We have, the, just jumping on themes here We, I don't know where it says Data Center.

**Swyx [00:30:27]:** I, there.

**Ivan [00:30:27]:** Doesn't matter.

**Swyx [00:30:28]:** There's a very strong recommendation, which is, very unusual. Which is, it's.

**Ivan [00:30:33]:** We do not pay them for this, just.

**Swyx [00:30:34]:** I know, yeah. They just like you.

**Ivan [00:30:35]:** Yeah, they like us. yeah, and also a thing, so, Data Center has multiple isolation sets underneath. The customer doesn't have to know what they are. But basically we have Docker, which is a container, that's hardened with Sysbox. So it's Docker's, isolation that is a security equivalent to a VM, but it's still a container. And that is the default, and they, especially in these training workloads, really like that as an interface to be able to use just a basic Docker container, and we enable Docker and Docker. Which for these RL runs, if you need to do a Docker compose or Kubernetes, you can spin up a K3S inside of these things, which unlocks a huge amount of workloads that you can do that you cannot do on other providers. So just on that part is much more interesting. And so we went that, through that. We showed them that we could do that, and they enjoyed that quite a bit. They being the general venture people.

**Swyx [00:31:28]:** Those people, yeah.

**Ivan [00:31:29]:** And Harbor people.

**Swyx [00:31:29]:** Harbor people, do are they, are they a company yet?

**Ivan [00:31:33]:** As far, I do not know.

## Customer Pull, Slack Connect, and the Computer Use Bet

**Swyx [00:31:35]:** Okay. All right. Yeah. It's like super obvious that like, there's a lot of excitement and success around these things, okay, so yeah, tell us more, right? Like, this is an exploding workload, Harbor adopted you, which helped speed things along. But what are you learning as this new workload comes online?

**Ivan [00:31:53]:** There's a couple things that we learned, which we chat about in the beginning. We, and this has led our story, as we mentioned, we like talked to a lot of customers along the way, and we add more features and more tool sets as we talk to customers. And it's interesting that And I think it's that the ecosystem is so small and/or the models get smarter, where when we see one user come with a request, we know it goes on a roadmap if like three to five customers come with the same request in that week. It's like very bizarre. It happens so many times, which is.

**Swyx [00:32:27]:** Because they're all friends.

**Ivan [00:32:28]:** Sorry?

**Swyx [00:32:28]:** They all, they're all friends. They're all in the same group chat.

**Ivan [00:32:30]:** Yeah, probably, yeah. 'Cause and they're like, "Oh, can you do this?" And I'm like, "Okay, this is interesting. We'll put it on a feature request." And then the next one's like, "Oh, can you do this?" "Okay." It's all the same, right? It's always the same. And so what we try to do, and I personally try to do, I try to be on as many call, quote-unquote "sales calls" I can. I'm in every Slack channel. We literally have about 1,000 Slack Connect channels, something like that. It's an interesting, there's so many interesting things you find out when you have all the Slack channels. You can also see where people, transfer between companies. You see leave Slack channel, enter Slack channel. It's an interesting thing. Also, just I digress, I feel that Slack Connect is literally LinkedIn what it should be. You have a list.

**Swyx [00:33:08]:** LinkedIn charges you to, use your own connections, but Slack doesn't, right? Slack is like, do it for free. It's more lock-in. It's great.

**Ivan [00:33:15]:** Yeah. It's amazing. Yeah. It's one of the reasons.

**Swyx [00:33:17]:** You're gonna pay Slack for life.

**Ivan [00:33:18]:** Exactly. You're there for life. So that's interesting. And so one of the things, the newer things we were talking about earlier is we made a big bet and put a lot of investment on computer use. that is not seen publicly the light of day. We haven't GA'd that yet, but we have.

**Swyx [00:33:32]:** Is there a thing I can pull up?

**Ivan [00:33:33]:** There is computer use there. It's right up a bit.

**Swyx [00:33:36]:** Oh, yeah. Okay.

**Ivan [00:33:38]:** What we have, what we talked about and what we've seen publicly is there's this theme now about, the human emulator where And Elon from XAI has talked about this publicly, and if you think about the models today, they're actually quite sophisticated and they can do a lot of work, but they still don't have access to all the tools. Like, I'm a strong believer that the most efficient way for an agent to work is essentially headless or through, terminal or whatnot. But if we, if we look at knowledge work in general, there's about 100 million knowledge workers in the US, about a billion in the world, and knowledge workers, and the salaries of them aggregate to 10 trillion in the US 50 trillion worldwide.

**Swyx [00:34:24]:** Wow.

**Ivan [00:34:25]:** Something like that. And if we look at, the five most important sectors of that, so like healthcare and government and financial services and whatnot, that's about 56% of that. So let's say it's about half of that. So in the US it's about 25 trillion, and most of them, most of that work is actually still locked into legacy apps inside of Windows, which is not going anywhere for a very long time. Like, people just won't invest in that. How much of it? our assumption is the following: if, in the RPA market, which is similar market, well, not the same 25% of, these white collar, workers', work is automated. If an agent is more sophisticated, can go through more runs, figure stuff out, let's say it's, 40%, right? And so if you take 40% of that, you get to essentially, $10 trillion a year.

**Swyx [00:35:17]:** That's a TAM.

**Ivan [00:35:18]:** That is a that is a TAM. So that's the TAM of the models, right? That's not our, essentially ours. But you get to that size, and to be able to do that, you essentially have to give agents these computers with the legacy. So computer use, either Mac or Windows or Linux. Linux we also obviously have and others have. But Windows specifically is something very new, and the only option right now is an EC2 with, Windows or on Azure. Both of them take anywhere from three to five minutes to spin up. We've created an actual sandbox, so it's a second instead of milliseconds, but you have, point in time snapshots, you have, forking, you have all the things that you have from a sandbox, but essentially enables you to hopefully unlock all this value. And so that's been our big push and bet, but we've sort of, kept our ear to the ground. What is sort of the next things in the market?

## RPA Returns: Why Agents Still Need Computers

**Swyx [00:36:06]:** Yeah, knowledge work, and building, and sort of RPA, the next wave of RPA. I got very excited about RPA kind of during COVID times. The UI path was IPO-ing. And it was, a very hot Isn't it, Eastern European?

**Ivan [00:36:20]:** It is, Romanian.

**Swyx [00:36:21]:** Romanian?Yeah, it might be the only Romanian, big unicorn okay, yeah. This I don't I don't, I don't have like a I think there's, I think there's a stage being set for the resurgence of RPA, 'cause everyone understands that, yeah, no one wants to deal with these shitty apps and no one's gonna rewrite them. Like, you just have to do, a remote operation and programmatic operation of them.

**Ivan [00:36:45]:** If you wanna unlock it, my own setup was basically the following. So I was doing a board deck recently, last month, whatever, and I'm like, "Okay, let's just, let's just do automated." So, all our data's in, ClickHouse and PostHog and QuickBooks, where everyone else's is, and I'm basically, connected that all to, my Cloud code, like go off and go Cloud code whatever. Go off and, here's the integrations, go do that. It pulled out the first report, which was great. It connected to Brex and all these things, pulled it, which was great, and then I say, "Okay, now pull out this, and this," and I kept getting, really well McKinsey-style design reports, but the data said partial data. all the missing data, partial data. Like, it can't access all the things, and I got so frustrated, and so I got, I got, my Mac Mini virtual sandbox with OpenClaw. I gave it its own account in our company, and then I went to all these services and created a read-only account, so literally like an intern in your company. And so I would say, "Now go and do this report," and it would get the same, or like, "I can't via the MCP or the API or whatever. I can't get all the information." I'm like, "Go log in." And it will log into the website, then go in, export the data. It'll export the data and do the thing end to end. So even for things that have today APIs, not all of it is exposed, and I to get value, I get immense value right now, but it has to be a computer usage, unfortunately, and so I spend a bunch of tokens just on that, but I get the job done. And so if even a startup like ours, and using all the hottest tools, still needs a computer agent what hope does, Goldman have to have a headless, right?

**Swyx [00:38:22]:** Yeah, what a - Why isn't Microsoft doing this?

**Ivan [00:38:27]:** I'm pretty sure, Satya had a post yesterday.

**Swyx [00:38:29]:** Oh, okay. I see.

**Ivan [00:38:29]:** Which was like, "Every agent needs a computer."

**Swyx [00:38:31]:** I see, I see.

**Ivan [00:38:32]:** So they have launched something recently.

**Swyx [00:38:34]:** Yeah, they have Microsoft Power Automate, I'm sure, I'm sure, they're gonna have their version.

## macOS Sandboxes, Apple Constraints, and the Windows Opportunity

**Ivan [00:38:39]:** Version of that, yeah.

**Swyx [00:38:39]:** You're gonna try to do yours, and it - I always know there's always demand for Mac, but I know it's, tricky to host, macOS sandboxes.

**Ivan [00:38:49]:** We will have macOS sandboxes fairly soon. The problem with macOS, OS sandboxes is, I'm deep in this, I don't know how much interesting is.

**Swyx [00:38:55]:** No, it's.

**Ivan [00:38:56]:** MacOS has this problem.

**Swyx [00:38:57]:** It's a licensing thing, right?

**Ivan [00:38:58]:** Licensing thing. So one, you're allowed to run only two parallel VMs per machine, so that's one. Two, you can only license to a different user every 24 hours. So if you come in and theoretically, if I wanna charge you per second and I charge you one second, I have to have it idle for the rest of the day. I can't have anyone else doing that. So the pricing will be different in the sense that I will have to - we would have to charge for 24 hours, and that's not even, that's not even the most difficult thing. But the, thing above that is, from a security perspective, they enable you to do memory snapshot, pause, resume, but only on the same physical drive, physical machine. And so what you can do in, Windows world or Linux world is that I can move in the background, your snapshot from one to the other and manage load, right? Here, if you wanna do that, you essentially have to have your.

**Swyx [00:39:49]:** Yeah, snapshots. Yeah.

**Ivan [00:39:50]:** Your.

**Swyx [00:39:51]:** It's like.

**Ivan [00:39:51]:** Physical machine.

**Swyx [00:39:52]:** You can't break it up.

**Ivan [00:39:53]:** You can't, you can't move things around that, and all of that is, that part is, from a security standpoint, if it is written. Like, I understand the security aspect of that, but it disables you from doing these agentic, like really scalable agentic workloads.

**Swyx [00:40:08]:** You need to do a vibe-coded, clean room implementation on macOS that you can then - That's like Clean OS or something. I don't know.

**Ivan [00:40:17]:** So. We have.

**Swyx [00:40:18]:** 'cause like Linux was originally like a clean room rewrite of Unix.

**Ivan [00:40:21]:** Okay. Yeah.

**Swyx [00:40:21]:** Or something like that, right? Like same thing to macOS. Someone needs to do it.

**Ivan [00:40:25]:** Someone will do that, and someone will have some long-running agents for a few days to figure this stuff out. But yeah. So definitely we - we're really close to offering something 'cause people do want it, but the pricing will be different, and the feature set will be sort of stringent.

**Swyx [00:40:38]:** Yeah, nobody's gonna use this. like, the labs, the labs will because they want to automate macOS.

**Ivan [00:40:42]:** They have to do RL. They have to do RL again. But even if you The - So the point is with the RL part, if you, if you do RL on macOS, then the next iteration of the model comes out, it will be able to use these tools significantly. Then you actually need to run those, that somewhere. So you're gonna have to have that, later on. And from, if anyone at Apple is listening, I very much feel that they are shooting themselves in the foot of the scale of the revenue of compute or licensing they could get if they would just enable a concurrency model similar to what you can get on a Windows and a, and Linux.

**Swyx [00:41:17]:** Yeah. Yeah. And I'm sure they've heard this before. They just don't care. Yeah, it's And maybe they will change their mind with the new CEO.

**Ivan [00:41:24]:** Yeah. We'll see.

**Swyx [00:41:25]:** We'll see.

**Ivan [00:41:25]:** High hopes.

**Swyx [00:41:26]:** High hopes.

**Ivan [00:41:26]:** High hopes.

**Swyx [00:41:27]:** Okay. But I, it's very clear the market opportunity is huge in Windows, and you can go for a long time on just Windows, but your customers are gonna want both. and I think, it is interesting to me that, this is the sort of God application of agents, right? Like, I don't It was - How big was OpenClaw for you guys? Like, was it, was there, a significant bump.

## OpenClaw, Agent Labs, and the B2B2C Sandbox Market

**Ivan [00:41:54]:** Not for us because we.

**Swyx [00:41:54]:** Because you already.

**Ivan [00:41:55]:** We're kind of positioned differently. Whereas although it's completely PLG and we have individual developers that use it, most of the users that use Daytona are sort of a B2B2C. Sort of it's either B2B or B2B2C. So, in the researcher world, it's B2B, so you're selling to, labs and neo labs and things like that. But on the long-running agents, it's mostly, from a scale revenue perspective, it's mostly B2B2C, where you have a app layer agent that uses you at a big scale.

**Swyx [00:42:26]:** Like a Manus. Yeah.

**Ivan [00:42:28]:** Like a Manus Lovable type of thing.

**Swyx [00:42:31]:** Yeah. I think that's the question of, well how, um-Uh, yeah, B2B to C is basically to me what I've been calling an agent lab, which is kind of like you're not in a model lab, but you're making a very good wrapper that is a platform that other people can sign up so they don't have to code those things. Yeah, it sound, it sounds like a much better market than the direct OpenClaw market.

**Ivan [00:42:56]:** I've like - We I've done multiple things. So the CodeAnywhere's part of our career path R in the calendar, was very much an end user developer product. And so that is great. It You can get a lot of developer love, and I feel that we do as a company have a bunch of developer love. But it's a different type, where it's people building these things. Again, it's more akin to a Twilio because you don't really run - As a person, you wouldn't run Twilio. I don't know how many people remember. It was like ask your developer billboard and whatnot. And people really love Twilio, but they only used it inside of like, "Oh, I'm building this app or service for thing." And so we're very much directly to that. And you also know that I used to work for a competitor for Twilio, so it's kind of ingrained, in my DNA.

**Swyx [00:43:35]:** People don't know InfoBip is that big.

**Ivan [00:43:38]:** Yeah, it's.

**Swyx [00:43:39]:** Because.

**Ivan [00:43:40]:** It's a billion euro.

**Swyx [00:43:40]:** They're all American. They're like, "Whatever's in Europe doesn't matter to me." But like it's the, it's the same size or bigger? Same size?

**Ivan [00:43:46]:** It's about half the size.

**Swyx [00:43:47]:** Half the size?

**Ivan [00:43:48]:** Yeah, about half the size.

**Swyx [00:43:48]:** It's like, yeah.

**Ivan [00:43:48]:** Still huge. Multiple billions a year. Yes.

**Swyx [00:43:51]:** That's crazy.

**Ivan [00:43:51]:** Exactly, and so that - These are like really interesting and large revenue-generating, very sticky businesses. Whereas when you're selling to the - When your focus is the end developer, it is a very hard sell because they're very price sensitive, very price conscious, very around that. And there's very It's very hard to scale. Your cap is the number of people that are willing to spin up - First of all, wanna spin that up, and then spin up multiple of these. Whereas if you're in the enterprise one, like we know everyone's talking about like how many tokens they're spending, I'm spending. Like a lot of companies today are like, "If this is our company, spend as much as you can." Like basically that is where we're going. And so if you think about that paradigm, where you're selling to companies that say, "Spend as much as you can to generate, productivity," versus, "Oh, I'm a single person. I have this much budget, and I'm doing this thing because it's fun or it's helping me out or whatever." Like it is a different, it's a different go-to-market, I think, strategy.

## MCP, CLIs, and Sandboxes as the Agent Runtime

**Swyx [00:44:50]:** Yeah, there's a lot of discussion. I'm just kind of going through like the mental list of things that are in your favor, which is, for example, MCP versus CLI. Like obviously you want CLI. It's been very good for you. I feel like it's maybe a drop in the bucket or maybe it's huge. I'm just checking whether it's like these are big trends.

**Ivan [00:45:10]:** Those things you - work well in our favor, to your point just because every.

**Swyx [00:45:13]:** They're kind of drop in the bucket, right?

**Ivan [00:45:15]:** I think it's like sort of all the things come together. And so there's so many things that impact that. To your point, like OpenClaw wasn't huge for us, but like having the agent SDK, from Anthropic, so or Cloud Claude Code was very interesting. The reason why it was interesting is that a lot of, let's call them app I don't know what to call them, app layer agent companies, essentially they are like, "Oh, I can create this new app, this new agent. All I need, I just use Claude Code, and I throw it into a sandbox, and then I have my interface to the human to that." And so that enabled so many more companies to actually offer this, and then they would pull on sandbox. So that was, that was interesting. And to your point, like MCP, versus the CLI, the MCP is an interface against an API, whereas the CLI is like you can actually go do things. Like this is it. The difference between integrations and actually running scripts or data or analysis against a thing. So being able to use a CLI very well enables the agent to do more things, and it's because that people will invoke a sandbox, they'll run it in the CLI, and but it'll do anal-analysis on that data and then give you an actual result versus just, pulling data from an API source.

**Swyx [00:46:29]:** Yeah, it's a layer of indirection basically, it's the same thing as agentic search versus RAG, which where you're.

**Ivan [00:46:34]:** Exactly, yeah.

**Swyx [00:46:34]:** Just like you just win whenever people put more agents into their workflow. And so like it doesn't really matter, but I'm just kinda teasing out like what else have people heard about that like it's sort of, "Oh yeah, this is another sandbox use case. Oh yeah, that's another one." Am I, am I missing any big ones?

**Ivan [00:46:51]:** The thing, the thing that people, which is the computer use stuff, which I think is probably the most interesting one, is, and to your point, we've talked to so many people over the last year. It's like, "Oh, like why do you need a sandbox? Why do you need this? Why this?" And to your point, it's like, "Oh, I need sandbox for this. I need sandbox for that. I need sandbox-" It's like, "Oh, I need it for every single thing." And so basically what I, what I - and it sounds like a broken record, it's like you use a laptop every single day, right? And you are n of one. It's just you. But now imagine how And by the way, the laptop, the computer PC market, the PC market is about equal to the cloud market in total. So it's about 150, 180 billion a year. Something like that. It's about roughly the three cloud hyperscalers is about equal to like Apple, HP, Lenovo, whatever, It's a little bit less, but it's sort of like that. And now imagine And that's just like, so how big is the addressable market? What, how many people are there in the world now? What's the last data?

**Swyx [00:47:45]:** Let's call it eight billion.

**Ivan [00:47:46]:** Eight billion. And so let's say you can have two computer, like you have one personal and one business, whatever. Like so it's double that, right? and so that's 16 billion, right? How many agents are gonna be running in two years, in 10 years, in 100 years? Like And for every single task, they will need one of these. And so how big is that? That market is essentially quote unquote "infinite". You will get to the point, and Dylan Patel was at the conference talking about, from SemiAnalysis, that talks usually about GPUs, was also talking about how CPUs will now be a bottleneck because it will be the constraint. You won't be able to grow, or we won't be able to have enough of these because there won't be enough CPUs to basically do.

**Swyx [00:48:23]:** Yeah. Well, I actually had a really good podcast with Doug Oliphant, who, which was his president at SemiAnalysis, where they've basically been like, yeah, it's been a GPU shortage first, but then it's cascaded down to memory and now to CPUs.

**Ivan [00:48:35]:** CPU, yeah.

**Swyx [00:48:35]:** It-What's next? So networking. So, networking actually has been in shortage for a while if you're looking at, just GPU networking. But, yeah, it's really crazy the amount of computer use that's going on, yeah, cool. I, other questions are, just the one very big part is the open sourceness which you didn't have to do, your competitors don't do, like it's not, a lot of people are worried about keeping their projects open source because some competitor can just slot fork it. I don't know if there's any reflections on just being an open source company.

## Open Source, Trust, and Enterprise Procurement

**Ivan [00:49:15]:** Yeah. There's a bunch. So we the original product that we did was open source.

**Swyx [00:49:19]:** Yeah. CodeAnywhere.

**Ivan [00:49:20]:** So doing that was actually very good for us. There's basically a saying of, What's the saying? Like, companies that are, that are doing really well, measure themselves against, free cashflow, that are kinda okay, it's EBITDA, then, it's, it goes all the way down.

**Swyx [00:49:36]:** The worst is like GitHub stars.

**Ivan [00:49:37]:** GitHub stars. GitHub stars are the worst, yeah. So you go all the way down to GitHub stars. And so our original one was GitHub stars. That's what we talked about, we're at the point we're talking about revenue, so we're we've gone up the stack on that. And so we started.

**Swyx [00:49:47]:** No, profit.

**Ivan [00:49:48]:** Yeah. We haven't, we're, we'll get there. We'll get there. But basically at that point we did stars and GitHub and it was useful, and the original variation that we did, it we split the core into its own repo and it was Apache 2.0, so very, permissive. And then we basically would bundle that on the enterprise side with a proprietary repo. So it was like open core, but it didn't, it didn't fill out the repository was very clean. When we did the pivot, we didn't have time to rethink this, and we wanted to We had this open source community. It felt a shame not to do that, and so, but we still did want to add some restrictions, so in the new sandbox product we did add a AGPL 3, which is, it's a kind of a shortcut way to do that where you are open source. And it is true open source in the sense of an enterprise can use it if it, if it wants, but you essentially can't make a competitor without open sourcing your stuff, which.

**Swyx [00:50:42]:** It's one of, three approaches. Like, there's, BSL and some of the other sort of, elastic license.

**Ivan [00:50:47]:** Yeah. There's some others there. So pure open source believers agree that this is not full open source and I totally respect that. That is absolutely true, but we did leave that. And Daytona, in its essence everything outside of what's under a feature flag today, which is like the Windows stuff, GPU stuff, and whatever, it is in this open source. It is there. So everything is there, like our own scheduler, everything's there. So we are I've had some competitors say, "You guys are actually open source open source. Like, you're real." "Like, you can actually see that." And people do like that, and it has helped a bit, but it's actually more helped in the consumption of our cloud product than actually transferring people over. The reason is you can actually You send the repository to your agent when you're integrating Daytona and it just has more context. It's like, "Oh, okay. This is why this is happening. This is why this, that."

**Swyx [00:51:41]:** You could equivalently just have docs that you can Yeah, so, okay.

**Ivan [00:51:45]:** I agree, but I, it to be fair, and so it actually doesn't really help the growth significantly today. We've had this conversation with, investors and other people is like, "How do you convert people.

**Swyx [00:51:56]:** Dude,.

**Ivan [00:51:56]:** From open source?"

**Swyx [00:51:57]:** The open source business conversation is so all over the place, right? Okay, on and I would just, for listeners who maybe they haven't thought this through, a lot of people say, "Oh, it's our free tier," right? Like, "Oh, if you run it yourself, but if when you get serious, call us." Right? And then other, And then me personally, 'cause of my Temporal experience, it actually is the way that, it's the, it's GTM into some of the largest companies where we wouldn't pass their, review process maybe 'cause we're too young of a company or, there's, parts of the stack that we haven't, that just doesn't work with them. But because it's open source, then they, then they adopt it, and then later on we figure it out. Like, that's the low end and the high end. I don't know if it.

**Ivan [00:52:37]:** No, absolutely, and that has been historically. The thing that we have found in this AI transition is, and so we haven't talked about this, Daytona's customers are everything from, the single developer, the YC startup, to people say Fortune 500, I'll say Fortune 5, like the biggest companies in the world.

**Swyx [00:52:55]:** Big Neo labs. You told me about the, we're gonna keep them anonymous.

**Ivan [00:52:59]:** All, the enormous companies, right? And because the market pull is so strong, we're able to circumvent these processes. I'm not saying We go, we pass security audits, we pass all these things, but as you mentioned, like Temporal way back in the way, day, in our old version of Daytona, like it took us months, and usually at the end they would churn off because just like, "Oh, you're too small of a company," like, "We don't trust you" "enough." Whereas today we've had these large companies push us, like they would push us through. Like, usually when you would go through procurement to become a vendor of large companies, it would take you like two, three months. We get it done in five days now. And this is not saying that maybe we're great, but it's more, I think, a sign of the market where it is today. And so when you think about that, the open source is something that we, from a go-to-market perspective, don't think about that much because everything that we've created right now has been PLG through the cloud product, people signing up and just pulling us inwards.

## GitHub, Agent-First Versioning, and CI Bottlenecks

**Swyx [00:53:53]:** Yeah, this is a personal interest, and I don't know if you have an answer, but, do you have problems with GitHub?

**Ivan [00:54:02]:** I do. A little bit. A little bit.

**Swyx [00:54:04]:** Yeah. Tell me, tell me. 'Cause I'm thinking about, well, okay, what would it take to replace GitHub?

**Ivan [00:54:09]:** There's a lot of things. I've thought about this, and I've talked, I've tweeted about this, and I looked at some. I've actually invested personally in some.

**Swyx [00:54:17]:** Is it, Entire?

**Ivan [00:54:18]:** No, I haven't done it.

**Swyx [00:54:18]:** No? Okay.

**Ivan [00:54:19]:** Yeah, so I, and I've met Thomas or virtually and we've talked. So I really think that And this was my reason for that. Because we have a bunch of background long-run agents, and for our time most of them are coding agents. Like, everyone was building up a competitor to Lovable or Devin or whatnot. What we saw from our customers was that they were all trying to figure out how to do, versioningLike, everyone is doing it in different ways. There was like some really weird ways where people were doing that, and the reason was that GitHub as is was an overhead. Like, it wasn't fast enough what they needed, it didn't solve the problem that they needed. And to be fair, like GitHub is for post your the inner loop, right? It is post your laptop, right?

**Swyx [00:55:07]:** Yeah, GitHub is the point at which the outer loop starts.

**Ivan [00:55:11]:** So people started using that for sandboxes, which is inner loop, which is usually, it's on your laptop, right? And so that is not what it's made for, and then we had everything from people Actually, the most interesting one is we had one customer that would literally take the entire code base inside the sandbox and every I forgot what the time sequence was, they would just dump it all into a JSON and then push that to S3. And that's it.

**Swyx [00:55:37]:** Make your own Git.

**Ivan [00:55:38]:** It's, it But it's not, there's not even diffs, it's just a whole thing every single time. It's just every Because it was super fast. Like, it didn't matter. And then they would go back and search and find, sort of what the file was and write it, and whatnot. Because there's text file, there's JSON, like they're very small so the network cost is very low, and they didn't care, and they just did it that way. And I'm like, if people are doing this, that means there needs to be a new solution to this problem, right? And so for me, it's quite interesting to look at who is building these types of new things. Agent first. I think Git as is still exists in the future, maybe even GitHub exists, but there will be a whole new sort.

**Swyx [00:56:15]:** Yeah, exactly. Git is like the deploy artifact to kick off CI/CD. But then there's a layer before that is like the agent collaboration layer.

**Ivan [00:56:23]:** Yeah. And so I think something needs to be said there, but on the other side, like there's issues with Another interesting thing is just like CI right now. So the amount of PRs being created is insane right now, right? In general.

**Swyx [00:56:33]:** Even for you guys, right?

**Ivan [00:56:34]:** Everyone's creating a bunch of PRs. everyone. And then all that has to go through CI, and then that's the bottleneck. Like, everyone's bottleneck. Like, not just like, not just actions, but like go to any CI provider, you will not be able to, if you have a high throughput of PRs There's one company we're talking to, they do 1,000 PRs a day. Which means like And they're just waiting. They have just a queue on that, right?

**Swyx [00:56:55]:** What do they use, Buildkite.

**Ivan [00:56:58]:** I don't know what they.

**Swyx [00:56:59]:** Circle?

**Ivan [00:57:00]:** They're, whatever.

**Swyx [00:57:00]:** Technically your tech can be used for CI.

**Ivan [00:57:03]:** That's, that was the conversation. That was the conversation.

**Swyx [00:57:06]:** Is that a serious conversation?

**Ivan [00:57:08]:** We'll, we'll see how that goes. We've had quite a few conversations around that. We're we are not a CI provider by any means, right?

**Swyx [00:57:13]:** But what is what's missing?

**Ivan [00:57:15]:** No, so essentially.

**Swyx [00:57:17]:** Nothing.

**Ivan [00:57:18]:** You, essentially you could use a Daytona sandbox instead of whatever you use for, your GitHub runners essentially.

**Swyx [00:57:27]:** Like, yeah, I'm The only thing I would say is like maybe CI machines are supposed to be very cheap, maybe it's like the low end because it's supposed to be like, non-blocking or like something like a, like a background job. Like, it's, the urgency is not that important for CI.

**Ivan [00:57:45]:** Performance is, though. Performance is, yeah.

## What Sells Daytona: Responsiveness, Support, and Customer Trust

**Swyx [00:57:48]:** Yeah, okay, that is interesting, and yeah, I think, like before we leave Daytona and go into like sort of broader like founder takes and what have you, any other Daytona elements that, is interesting that we haven't touched on?

**Ivan [00:58:04]:** Interesting Daytona things. There's, there.

**Swyx [00:58:06]:** I can, I can give you more prompts if you want.

**Ivan [00:58:07]:** Yeah, I'd love more prompts, actually.

**Swyx [00:58:09]:** Okay. So when startups evaluate you, so you have, you have all these like names and you have more that you can't, you can't even name, they see all your wall of competitors. and yeah, you have differentiation versus, many of these, but like what sells them?

**Ivan [00:58:26]:** The thing that we found that sells people the most, this is more maybe a day two thing instead of a day one thing. And we've seen this again and again. So we have a bunch of case studies, and we have a bunch of them still coming out. They're all done by a third party, so we don't do the case studies, and it's actually interesting to watch those cases. I watch, they're recorded, and because it's a third party, people are actually more open, and they will tell you, "Oh, we use this competitor," or, "We like this competitor more," or this thing or whatever. And the number one thing that people come back to us for is that our, we have an insane responsiveness.

**Swyx [00:58:57]:** In terms of your team?

**Ivan [00:58:58]:** In terms of the team, yeah. Insane responsiveness has been by far the Now, we can talk about like features and breadth of product and concurrency and CPUs and like all those things, but I feel that would probably So if all other things are equal, that is very much a differentiator I've found. And I didn't know.

**Swyx [00:59:15]:** Is that entirely Slack or Slack plus email?

**Ivan [00:59:18]:** It is, there's email there as well, there's calls, but the vast majority is like on Slack. So it's Slack. Like, we have had customers like, "Hey, we have a problem. Can you get on Huddle?" Like, we will get on that Huddle like in five minutes, literally. I've done this multiple times, so yeah.

**Swyx [00:59:31]:** Wait, okay, so how big are you?

**Ivan [00:59:33]:** 25 today.

**Swyx [00:59:34]:** How do you do this kind of support like this?

**Ivan [00:59:36]:** We're insane. We don't sleep. 007, have you heard the new thing?

**Swyx [00:59:40]:** 007\. like I've met your team. They're very impressive, they're very dedicated, but like also how do you get a team to do that? it's.

## Startup Culture, Family Tradeoffs, and Enjoying the Pain

**Ivan [00:59:48]:** So there's.

**Swyx [00:59:49]:** I have Slack exhaustion?

**Ivan [00:59:51]:** Yeah, we all have Slack exhaustion. We're very tired. the thing that is unique, I don't know unique about us, but unique, I would say unique about any successful, serial founder is that you're able to pull in people that you've worked with before, and so you can't do that as a first-time founder. Like, I couldn't have done that or not. But of the 25 people in Daytona, I think about 13 of them we have worked with seven years plus. So it's like high trust, high throughput, high we know what we're signing off to do. And especially these people worked with us when we were starting, and we were actually hustling. hungry for food hustling type level, and so those are the people that work with us. The, now the new segment that has come is almost everyone is sort of, one degree of separation, so it's like someone that someone has known, and so they sort of come into this org. And we've had people that have like not fit into org as well. It's just like, it's type of culture where there is a high expectation of, being online, replying for these things, and I do that first. You if you ask any engineer, they're like, "You never sleep," like, about me. And so then I do that as an I don't do it as an example. That's just how I'm wired. My wife doesn't appreciate that I have to tell you. My wife doesn't appreciate that. I told her about 996, she said, "I wish."

**Swyx [01:01:09]:** It's like these Chinese people are slacking.

**Ivan [01:01:13]:** Yeah. So, that is something there. And so I think every company has their own culture, and that's something very deep, ours. And it's something that's come up again and again, and every single day we're reminded about that. And I didn't go out thinking that is how I'm gonna build it. It's just how I've built these things right now.

**Swyx [01:01:29]:** Yeah. so okay, I'll transition a little bit on the founder side. Like, I'm very impressed by you in general of, your sort of balance, you have, you have a young family.

**Ivan [01:01:38]:** Two kids, yeah.

**Swyx [01:01:39]:** Two kids now.

**Ivan [01:01:40]:** Yeah, two kids now. Yeah.

**Swyx [01:01:41]:** I think a lot of people I meet, they're like, "Oh, I'm starting a family. I can't be a founder," and all that, what's your advice to those people?

**Ivan [01:01:48]:** Everyone has their own I, it's a hard, it's a hard, they Every single day, so my family, they're here right now, but they're usually I fly between Croatia and here. Like, a lot of our team is in Croatia. A part of our team, and are growing, is here now in San Francisco. And so I spend a lot of time away from my family, and that is hard. Like, that is a sacrifice that you have to. But going in, people say, on your deathbed, you're gonna miss some of those things. The thing that, and probably might be true, but the thing that going into this, I already said, I know that this is gonna hurt, and everything has to hurt. By the way, I'm very much of a feeling that everything has to hurt. Going to the gym hurts. Losing weight hurts. Like, everything has to hurt, right? It does. Like, we all.

**Swyx [01:02:32]:** No pain, no gain.

**Ivan [01:02:33]:** It is literally, but you actually have to enjoy the pain and just, if you don't enjoy the pain, it's not for you. And so you get accustomed to that pain. And so love the kids, especially I have a daughter and a son. Daughter is the eldest, love her and do miss her when she's not here, but it's like, that's what I signed up for, and there is a plan and target of what I'm trying to achieve. And now hopefully with my wife, which does support me, we can get ourselves together more, so it doesn't there. But she takes a large part portion of that. And so if you have a partner on the other side that is okay with that, then you can do that. But even if they do, you have to be okay with not being there, right?

**Swyx [01:03:11]:** Yeah. This is my vision for you, this meme.

**Ivan [01:03:15]:** Yeah. I.

**Swyx [01:03:15]:** That's your kids in the future.

**Ivan [01:03:18]:** Yeah, I think.

**Swyx [01:03:18]:** It's like this,.

**Ivan [01:03:18]:** We have to teach them that they're not rich.

**Swyx [01:03:19]:** Because Dad, built the compute sandboxes.

**Ivan [01:03:21]:** Yeah, you built compute sandboxes. Dad made sandboxes. Dad made sandboxes.

**Swyx [01:03:25]:** Built the spiritual successor to serverless and Kubernetes and for agents, any other sort of, hot topics, trends? You have a lot of hot takes, actually, you are best known for, you were, you were, you were sort of in sort of hustle culture mode, right? And someone quoted you and said, "I haven't even heard of you, bro." "Just log off and take the, take the Christmas off." And then your response was?

**Ivan [01:03:53]:** Oh, my response was, "That's why I can't."

**Swyx [01:03:56]:** Like, I think that's, very typical of you. I don't have it here. I can't, I can't bring it up. But, I think that's very typical of the culture. But, I think you have a lot of, interesting hot takes like that. Any other sort of takes on, the startup ecosystem?

## SaaS Token Resellers, API Revenue, and Startup Hot Takes

**Ivan [01:04:11]:** Oh, yeah, the startup ecosystem. And this was the recent one, which is I think that And this is general, business. I feel that the It didn't come off, I think, well on Twitter. Some people at least misread it. Which is, the market is adding premium to SaaS vendors that are reselling tokens. And I think that's incorrect.

**Swyx [01:04:34]:** Why?

**Ivan [01:04:35]:** Because I think So what I think, why I think that's incorrect is that if you look at, one, your pricing depends on what the price is, if it's public market or if it's private or whatever. You're saying, the person that's reading that the re-acceleration of revenue is equal to the old revenue, which it's not even close. Because one, you had on SaaS, you had typical SaaS margins, whatever it was, right? Stickiness and all these things. Now what you're doing is you are saying, "Here is my agent, and I have whatever the margin is." It's way worse, right? And now you're using Anthropic or OpenAI or whatever through me, the SaaS product, and then we as a community are saying now that is re-acceleration. And so one, I think that's wrong because it, first, it's not the same. The makeup is not the same. The other thing is, and go back to, what I mentioned earlier is, the Kua and how I set up OpenCloud and whatever. I don't want your agent, essentially, because what happens, right now we have a problem that, and this has historically been, you have data siloed in, again, ClickHouse, QuickBooks, it's all siloed, and now you're giving me an agent that'll give me the data, but it's still siloed, right? And so now I have to, take that data and then get another agent.

**Swyx [01:05:52]:** Just expose the data to my agent.

**Ivan [01:05:53]:** Just expose the data. Just expose it. And one thing I have to and so I'm like, "Just expose everything and charge me for that." So charge me for consumption of API. So you'll have your old seat-based pricing for humans. Charge me for this. The number of agents will skyrocket, and essentially you'll have more usage, and charge for more if your product has value. So, there's arguments some of them do have value. It's a database, not database. We can get into that. But some of them really do, and I was actually shocked that the first person to do this was Benioff.

**Swyx [01:06:24]:** Salesforce, yeah.

**Ivan [01:06:25]:** Sales.

**Swyx [01:06:25]:** Agentforce?

**Ivan [01:06:26]:** It, there was a tweet, I think three days ago, where she said every product in Salesforce has been exposed via an API.

**Swyx [01:06:33]:** Wow.

**Ivan [01:06:33]:** Everything. And I'm like, now I understand why this person has built.

**Swyx [01:06:38]:** This guy's king.

**Ivan [01:06:38]:** This insane. Kudos to him. Amazing. It's like, thank you. I don't know if you listen to me or someone else, but like thank you for someone This is the direction of the world, and so if you can get real acceleration against that, against consumption of API, that is actual revenue, and that is actual real acceleration, and that is where value come from. And I think that there will be cold shower when people understand, no one's actually gonna use and pay for these agents and tokens, and that wasn't actually really a solution, but it'll drop back down.

**Swyx [01:07:05]:** Yeah. Yeah, look, obviously, I think generally correct, and I agree. I think - But people are going to try to become an AI company.

**Ivan [01:07:15]:** No, absolutely. And nothing against that. And I - this is no, - To be very clear, this is not a downer on anyone that's building this thing. Everyone has to get to, get to the revenues, get to the multiples, get the valuations, do what you have to get to the next step. Absolutely agree. But we, as a community, are now, saying, "Oh, this is, the magical way to get out." This is not. Like, that is not what is happening, right?

**Swyx [01:07:35]:** Yeah. No, I think, there was like this kitchen appliance company that put out some AI nonsense recently.

**Ivan [01:07:42]:** It was also the sneaker as well. It was called Allbirds.

**Swyx [01:07:44]:** Allbirds. No, Allbirds is pivoting to GPU. That's fine. It's like, I have - I can - I have some money left, I'm just gonna, do some lottery tickets, would you go into offering GPUs?

## GPU Sandboxes, Data Centers, and Bare Metal Economics

**Ivan [01:07:55]:** Oh, yeah, we will. But not for inference. Like, essentially, what we think about is, the GPU sandbox. So, if you think of, if you have a GPU in your computer, that is what you have a GPU in the sandbox. So, there are workloads that do need GPUs. Again, I always go back to 3D rendering 'cause it's the easiest one to comprehend. But, if you wanna do any type of RL on, CAD or something like that, you will need a GPU in the sandbox, and so that's coming now as well, yeah.

**Swyx [01:08:18]:** How about own data centers?

**Ivan [01:08:20]:** Own data centers. So we run on co-location providers, bare metal machines. Data centers, we technically can run on that or our own data center. Like, that's how we architected it. Today, from a gross profit margin perspective, it doesn't make sense for us to get in that. You have to raise a large amount of capital, a large amount of risk for, single-digit percentage points. So today, that doesn't make sense, but we are fundamentally architected so that we can do that if we want.

**Swyx [01:08:47]:** Yeah. you're a large customer of these guys now. Do you see any opportunity?

**Ivan [01:08:51]:** We will see. We will see, yeah.

**Swyx [01:08:54]:** Yeah. I see a lot of people, trying to do the bare metal thing, we talked to Railway, the other day and they're also doing a very similar, strategy.

**Ivan [01:09:04]:** They think - I think they're building out something or they have their own sort of data centers now.

**Swyx [01:09:07]:** Yeah, they have majority their own data centers, I - But I do think, they still use Equinix and all those things. So I think it's just interesting that this model basically hasn't changed. It's basically a real estate model. They manage the facilities and then you do everything else, I wonder how it can be changed for the, for the future 'cause, the AI wave is the opportunity to reinvent everything, yeah. anything else, cool. I think that's about it. I didn't have any other, topics. I think this is, as best and comprehensive, if you have, any questions about the compute market, and sandboxing and Daytona, this is the best place to start. Where does this go, man? Like, we're here in April. Things are growing 75% month to month. Like, where are we, where are we gonna be by end of year?

## The Agent Cloud: New AWS, New Stripe, or Something Else

**Ivan [01:09:58]:** It's an insane number. I'm sort of scared to say it out loud. So, it is - It's very big, just the sandbox market on - And we - There - We talked about this in general. The entire infrastructure market is growing 40% plus or minus month over month. Everyone is growing 40% month to month. And that's also a hot take, is like if you're not growing 40%-ish, it's not that - It's just the market. You might as well - You don't have to come to work to grow that amount, basically. I'm half kidding, but that's where it's going. And so where does it end? We will see. The thing that I think about from at least a CPU perspective, a GPU is even crazier, but from a CPU perspective, it is like there's a high probability that actually owning the CPUs beforehand will be a go-to-market tactic, and it will probably - 'Cause I - You - As you do probably talk to a lot of GPU providers, their growth is hindered by the amount of GPUs that you have right now, right?

**Swyx [01:10:47]:** Yeah. It's just like, it's whatever NVIDIA decides to bless that day.

**Ivan [01:10:51]:** That's how much, that's how much they're gonna grow, right? And so where - The CPU market in general, be it like something like Railway, for example, or Vercel or whatnot, or Deployment, or it's like the sandboxes, they're still CPUs. So, each is growing at the pace of the of their - the market and what their, plus or minus of that market. But it's still not constrained by that. And so my thought is, for all of us in this market, and databases fall into that as well 'cause databases also run on CPUs. And it's like we all have to grow as fast as we can so we can get enough of, CPUs tomorrow from Intel or from NVIDIA, 'cause they have now CPUs and everyone else later on. So it'll be interesting when we get to that cap.

**Swyx [01:11:30]:** Okay. maybe one version I'll phrase this is like, are you, is the potential new Heroku, new AWS or new, what's it? New Stripe but compute? Or like what's the, what's the analogy that is most appropriate?

**Ivan [01:11:48]:** There's interesting. There's like analogies of like - So the, there's new Cloudflare, but new Cloudflare is new Cloudflare.

**Swyx [01:11:54]:** New Cloudflare.

**Ivan [01:11:54]:** They're actually doing a really good job about,.

**Swyx [01:11:56]:** Cloudflare owns networking. No one can fight. it's like, come on.

**Ivan [01:11:59]:** They're doing - No, they're doing really well. No, what I said is in the sense of their whole agent portfolio is actually really good. And I should say there are some technical I think, personally, around, everything's under constrained under Workers. Like, Workers is their thing. But from a go-to-market vision perspective, I think they're actually really good. I think they actually get it, unlike some other companies, and to your question is like, what is gonna be - There will be an equivalent, everyone says like an AWS for AI agents, but your answer, it might look more like Stripe than AWS, in a sense. So there will be a cloud built out specifically for agents. And so that cloud will have sandboxes, and it will have web search, and it'll have, databases like SQLite or Neon or whatever, specifically for agent and other things. We are not at the end of the new infrastructure primitives for agents. There are more coming. So people think like, "Oh, there's nothing else. This it." There are more. Like, we have some ideas about the next ones. We don't have time to do them, but there are definitely more primitives that are being built out for agents, and there will be, I think, a cloud that runs all that together.

**Swyx [01:13:07]:** Yeah. Yeah, OpenAI has said AI cloud, Vercel has said AI cloud, and you are potentially also one of the other, the prospective AI clouds. I think it's a very big prize to win, well, thanks for coming on.

**Ivan [01:13:18]:** Thank you for having me. It's been amazing.

**Swyx [01:13:19]:** Yeah. Okay. That's it.

---

## [[AINews] OpenAI GPT-next disproves 80 year old Erdős planar unit distance problem for under $1000](https://www.latent.space/p/ainews-openai-gpt-next-disproves)
*🔬 Latent Space | 2026-05-21*

We will leave coverage of the [SpaceXAI IPO filing](https://x.com/eliebakouch/status/2057222864332320999?s=12) for the actual day of IPO. Today we celebrate OpenAI's result, speculated to be [GPT 5.6 running for <32 hours or <$1000](https://x.com/willdepue/status/2057213893857165701), on [the planar unit distance problem](https://openai.com/index/model-disproves-discrete-geometry-conjecture/). Similar to the 2025 [IMO Gold](https://news.smol.ai/issues/25-08-11-ioi-gold) result, this is a general purpose LLM, [not an AlphaProof/Lean style dedicated model](https://x.com/polynoamial/status/2057179104315670826), which lends hope that this extended reasoning will generalize beyond math:

[](https://substackcdn.com/image/fetch/$s_!BIRC!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0ff7bdc0-79ef-49ce-a5c0-f7db89d60637_1098x1582.png)

Among the 125 pages of output, there exists a "[page 39 moment](https://x.com/voooooogel/status/2057198687307362642)" that is getting some attention:

[](https://substackcdn.com/image/fetch/$s_!aLpj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8288cdb3-1d89-4582-9d70-0f251a57d477_753x620.png)

As the authors of [the opinion letter](https://cdn.openai.com/pdf/74c24085-19b0-4534-9c90-465b8e29ad73/unit-distance-remarks.pdf) note, this is a disproof, not a proof, which would have been more impressive, but nevertheless points towards the way of things to come:

[](https://substackcdn.com/image/fetch/$s_!Q2Fl!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff77d343f-e4c1-4125-b78a-33728e06a6ba_1778x1490.png)

[](https://substackcdn.com/image/fetch/$s_!oa2I!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc9cfd22b-4a17-47a2-a2b0-d2ae5a911ece_1654x352.png)

> AI News for 5/4/2026-5/5/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

# **AI Twitter Recap**

**OpenAI 's Math Breakthrough on the Erdős Unit Distance Problem**

  * **A general-purpose reasoning model produced a new research result in discrete geometry** : OpenAI announced that an internal model disproved a long-standing belief around the planar **unit distance problem** , a famous Erdős problem from 1946, discovering a new family of constructions that improves on square-grid-style solutions [@OpenAI](https://x.com/OpenAI/status/2057176201782075690). OpenAI emphasized this was a **general-purpose model** , not a domain-specific math system or scaffolded solver [@OpenAI](https://x.com/OpenAI/status/2057176203166171317), and said the result points to stronger long-horizon reasoning for science broadly [@OpenAI](https://x.com/OpenAI/status/2057176204541866087).

  * The result drew unusually strong validation from mathematicians and adjacent researchers. **Timothy Gowers** called it the first really clear example of AI solving a **well-known** open math problem [@wtgowers](https://x.com/wtgowers/status/2057175729008153069), while OpenAI researcher **Hongxun Wu** described it as an internal reasoning-LLM milestone on "the hardest problems" [@HongxunWu](https://x.com/HongxunWu/status/2057176383106027567). Additional reactions from [@thomasfbloom](https://x.com/thomasfbloom/status/2057177152894771631), [@gdb](https://x.com/gdb/status/2057182650784452925), [@alexwei_](https://x.com/alexwei_/status/2057182873208369485), and [@polynoamial](https://x.com/polynoamial/status/2057178198228586824) converged on the same point: this appears qualitatively beyond prior "AI does olympiad math" milestones.

  * **Notable technical subtext** : OpenAI says the model was not pushed to the limit and is intended for eventual public use [@polynoamial](https://x.com/polynoamial/status/2057179104315670826). The published reasoning summary itself is reportedly massive--around **125 pages** per [@voooooogel](https://x.com/voooooogel/status/2057198687307362642)--which helped fuel discussion about the practical role of **test-time compute** in frontier reasoning. Some observers explicitly framed this as further evidence that inference-time scaling is the paradigm carrying current progress [@](https://x.com/_arohan_/status/2057188616099725525)_[arohan](https://x.com/_arohan_/status/2057188616099725525)_ , with others extrapolating to faster future gains in formal science and mathematics [@scaling01](https://x.com/scaling01/status/2057246143881609510), [@sama](https://x.com/sama/status/2057203171198636251).




**Cohere Command A+ Open Release and Architecture Discussion**

  * **Cohere released Command A+ as Apache 2.0 open weights** , positioning it as its most powerful model yet and explicitly optimized for low hardware requirements [@cohere](https://x.com/cohere/status/2057120818551734589), with the licensing clarified in a follow-up [@cohere](https://x.com/cohere/status/2057122131410813016). The release is significant partly because it is Cohere's **first fully open Apache 2 model** per [@aidangomez](https://x.com/aidangomez/status/2057142232860258527). Community reaction focused on this as a meaningful shift toward more permissive, deployable enterprise-grade open models [@nickfrosst](https://x.com/nickfrosst/status/2057132425310851104), [@ClementDelangue](https://x.com/ClementDelangue/status/2057180057756467671).

  * The model details repeated across multiple posts: roughly **218B MoE / 25B active** , **multimodal** , **48 languages** , and runnable on relatively modest setups [@JayAlammar](https://x.com/JayAlammar/status/2057145838011564126), [@mervenoyann](https://x.com/mervenoyann/status/2057128432190787643). **vLLM day-0 support** landed quickly, including a note that it can run on as little as **2 × H100s at W4A4** [@vllm_project](https://x.com/vllm_project/status/2057206049665622070).

  * **Benchmarks painted a mixed but credible picture** : Artificial Analysis placed Command A+ at **37 on its Intelligence Index** , around Claude 4.5 Haiku territory, with especially strong **non-hallucination** behavior and decent speed, but weaker scientific reasoning and coding than top peer models [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2057123594162077837). The community also dug into the architecture: unusual choices called out include a **parallel transformer block** , large **shared expert** usage, **LayerNorm over RMSNorm** , relatively low **32-layer** depth, and atypical head/expert configurations [@eliebakouch](https://x.com/eliebakouch/status/2057198733759008989), [@rasbt](https://x.com/rasbt/status/2057241574161932339), [@stochasticchasm](https://x.com/stochasticchasm/status/2057150551696261607). This made the release notable not just as a model drop but as an architectural data point.




**Benchmarks for Agents, Memory, and Scientific Workflows**

  * **InferenceBench** is one of the day's most technically substantive releases. It targets **AI R &D automation** through open-ended inference optimization tasks, and the headline is negative for current frontier agents: they struggle with **system-level engineering** , dependency management, and broad exploration, underperforming a simple baseline of **vLLM/SGLang hyperparameter tuning** [@maksym_andr](https://x.com/maksym_andr/status/2057106398228439148). The thread also reports an apparent **inverse scaling** effect, where models like **Claude Sonnet 4.6** and **GLM-5** rank well because they preserve robust final states, while larger models often produce brittle end configurations.

  * **Terminal-Bench Science** extends agent evaluation from coding into **real scientific workflows** , with task contributions now open [@StevenDillmann](https://x.com/StevenDillmann/status/2057144415513420049). In parallel, **MINTEval** targets long-context memory systems under frequent updates and interference: average instance length is **138.8k tokens** with up to **1.8M** , yet across 7 systems the average accuracy is only **27.9%** , with the best at **33.4%** [@hyunji_amy_lee](https://x.com/hyunji_amy_lee/status/2057141349166768233). This complements a growing line of work arguing that memory should be a dedicated learned subsystem rather than just RAG/context stuffing [@dair_ai](https://x.com/dair_ai/status/2057182105671750047).

  * On the human side of interaction research, **ThoughtTrace** introduced a large-scale dataset of users' **self-reported thoughts during real LLM conversations** : **10,174 thought annotations** , **2,155 multi-turn conversations** , **1,058 users** , **20 models**. Reported gains include **+41.7%** for user behavior prediction and **+25.6%** for alignment [@chuanyang_jin](https://x.com/chuanyang_jin/status/2057111965101670842). This is one of the more concrete attempts to instrument the "latent user state" that conversation logs alone miss.




**Google I/O Follow-Through: Gemini 3.5 Flash, Omni, AI Studio, and Antigravity**

  * **Gemini 3.5 Flash** began broader rollout in the Gemini app, including free access globally [@GeminiApp](https://x.com/GeminiApp/status/2057140474192994356), [@GeminiApp](https://x.com/GeminiApp/status/2057237126526517727). Google framed it as its strongest **agentic and coding** model yet, claiming frontier performance at **4 × the speed** of comparable models and under half the cost [@Google](https://x.com/Google/status/2057257773868388448). However, external discussion was much more mixed, with multiple posts questioning **real-world cost/performance** and token efficiency despite favorable launch-stage benchmark positioning [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2057181290412261557), [@scaling01](https://x.com/scaling01/status/2057177354582020362), [@giffmana](https://x.com/giffmana/status/2057155343390494949).

  * **Gemini Omni** appears to have made the bigger qualitative impression than 3.5 Flash. Google positioned it as a conversational multimodal creation/editing model for video and mixed-input workflows [@Google](https://x.com/Google/status/2057180052979409172), with Gemini app demos showing conversational video editing [@GeminiApp](https://x.com/GeminiApp/status/2057159933934907825). Early reactions generally treated Omni as a more differentiated product than the core LLM refresh [@scaling01](https://x.com/scaling01/status/2057143531622334678).

  * On tooling, **AI Studio** pushed harder toward end-to-end developer workflow and mobile access [@GoogleAIStudio](https://x.com/GoogleAIStudio/status/2057122673558434205), while several posts tried to decode the relation between **Gemini Spark** , **Antigravity** , and Google's internal/external agent harnesses [@simonw](https://x.com/simonw/status/2057115921551098211), [@_philschmid](https://x.com/_philschmid/status/2057136375988912176). A more concrete Antigravity-adjacent update was the launch of **Science Skills** for Google's agent stack, integrating 30+ life-science sources such as **UniProt** and **AlphaFold DB** [@GoogleDeepMind](https://x.com/GoogleDeepMind/status/2057256257153884161).




**Agent Infrastructure, Retrieval, and Dev Tooling**

  * Several posts converged on the same operational lesson: **agents fail on infra reality before they fail on demos**. That theme shows up in the qualitative thread on research agents fighting dependency conflicts and configs [@jehyeoky248](https://x.com/jehyeoky248/status/2057103859927941153), in LangChain's push for **LangSmith Sandboxes GA** [@LangChain](https://x.com/LangChain/status/2057152025058558072), and in newer lighter-weight **code interpreter** support for deepagents as a middle ground between pure tool execution and full sandboxes [@sydneyrunkle](https://x.com/sydneyrunkle/status/2057179305948647775), [@hwchase17](https://x.com/hwchase17/status/2057214077114679386).

  * In retrieval/search infra, **Perplexity** described a productionized **query-aware, citation-preserving context compression** system that cuts context tokens by up to **70%** while improving answer quality, and claims **50 × compression** on SimpleQA at frontier-level performance [@perplexity_ai](https://x.com/perplexity_ai/status/2057151002105753950). **Weaviate 1.37** added **MMR reranking** to improve diversity in vector retrieval for RAG/agents [@weaviate_io](https://x.com/weaviate_io/status/2057117923416629676), while **SID-1** was presented as an RL-trained agentic search model with **1.9 × recall over RAG+rerank**, **24 × faster**, and **99% cheaper** than GPT-5.1 in the cited setup [@turbopuffer](https://x.com/turbopuffer/status/2057166836031193523).

  * **Cursor** , **VS Code** , and **Codex** all shipped notable workflow updates. Cursor added **automations** in the agents workspace [@cursor_ai](https://x.com/cursor_ai/status/2057167359593603471), VS Code shipped better markdown/HTML previews, remote session continuity, and utility-model configurability [@code](https://x.com/code/status/2057195516123808070), [@pierceboggan](https://x.com/pierceboggan/status/2057204489661407365). On the model side, **Composer 2.5** posted a strong coding-agent showing--**62** on the Artificial Analysis Coding Agent Index at much lower cost than top Opus/GPT-5.5 variants [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2057277363789197561). OpenAI also shipped **Codex on mobile** [@OpenAIDevs](https://x.com/OpenAIDevs/status/2057142816497906045).




**Top Tweets (by engagement)**

  * **OpenAI math milestone** : OpenAI's announcement of the unit-distance breakthrough was the most consequential technical post in the set, both for scientific novelty and for what it implies about long-horizon reasoning [@OpenAI](https://x.com/OpenAI/status/2057176201782075690).

  * **Cohere Command A+ open release** : One of the largest model-release stories of the day, mainly because of the **Apache 2.0** license and unusual architecture [@cohere](https://x.com/cohere/status/2057120818551734589).

  * **Anthropic compute expansion with SpaceX/Colossus** : Anthropic is reportedly scaling up on **Colossus 2** capacity [@nottombrown](https://x.com/nottombrown/status/2057194829986300375), with follow-on posts citing a filing that values the SpaceX compute agreement at **$1.25B/month through May 2029** [@SemiAnalysis_](https://x.com/SemiAnalysis_/status/2057218890288030110).

  * **Exa funding** : Exa raised **$250M Series C at a $2.2B valuation** , explicitly framing itself as a search lab organizing web data for agents [@ExaAILabs](https://x.com/ExaAILabs/status/2057132080317042697).




* * *

# **AI Reddit Recap**

## **/r/LocalLlama + /r/localLLM Recap**

### **1\. Qwen3.7 Preview and 27B Roadmap**

  * **[Qwen is cooking hard](https://www.reddit.com/r/LocalLLaMA/comments/1theffd/qwen_is_cooking_hard/)** (Activity: 1292): **The image is a screenshot of Chujie Zheng teasing that Qwen is "cooking hard", quoting an announcement that Qwen3.7 Preview is now on Arena with Qwen3.7-Max-Preview and Qwen3.7-Plus-Preview; the post claims Alibaba ranks **`#6`**in Text and**`#5`**in Vision. In context, the Reddit title/selftext indicate users are anticipating larger and refreshed open-weight models --especially 122B and a new 27B--though the screenshot itself is mainly a teaser rather than a technical benchmark breakdown. [Image](https://i.redd.it/cefjio15g12h1.png)** Commenters are split between excitement for high-end models and practical interest in smaller local models: some want **9B/4B** variants for low-end hardware, while others hope for **122B** , a better **35B** , or joke that Qwen may soon be "cooking" their GPU.

    * Several commenters focused on **model-size coverage** rather than the current `27B` release, saying they cannot practically run it and are hoping for smaller **Qwen**`4B`**/**`9B` variants for low-end or laptop GPUs. There was also interest in larger `122B` and improved `35B` checkpoints, though one commenter noted prior `122B` mentions around Qwen 3.6 never materialized, raising uncertainty about whether a Qwen 3.7 `122B` will actually ship.

  * **[Qwen3.7 Max scored by Artificial Analysis, 27B/35B waiting room](https://www.reddit.com/r/LocalLLaMA/comments/1tie6gy/qwen37_max_scored_by_artificial_analysis_27b35b/)** (Activity: 553): **A Reddit post highlights an[Artificial Analysis leaderboard screenshot](https://preview.redd.it/42ak5qmus82h1.png?width=1133&format=png&auto=webp&s=744ea3dfc06c83d0c4d8aa128c39b3238b17d7be) where Qwen3.7 Max ranks **`5th`**, roughly level with GPT 5.4 (xhigh) and slightly ahead of Gemini 3.5 Flash. The author notes Qwen3.6 27B trails its Max counterpart by exactly**`6`**points and hopes upcoming Qwen3.7 27B/35B variants land close to the Max model 's performance.** Commenters are mainly _" waiting eagerly for the open weight models"_ and view the score as evidence that the **Qwen** team is now competitive with major labs, despite concerns that the Max model is not open-source. One technical concern raised is whether Qwen has fixed its prior tendency toward _" overthinking."_

    * Commenters focused on whether **Qwen3.7 Max** represents a genuine architectural update versus another finetune/iteration of the **Qwen3.5/Qwen3.6** architecture; one noted that extracting more performance from the same base architecture would still be technically notable.

    * Several users are waiting for potential **open-weight 27B/35B variants** , but one commenter speculated there may be no **Qwen 3.7 27B** at all, arguing that "Qwen 3.7" could simply be a private large model similar to **Qwen 3.6 390B A30B** rather than a full public model family.

    * A technical concern raised was whether the Qwen team has addressed the model's reported **" overthinking"** behavior, implying interest in improvements to reasoning-token efficiency, response latency, and controllability rather than just benchmark gains.

  * **[Qwen will release another 27B with high probability](https://www.reddit.com/r/LocalLLaMA/comments/1tiwnpc/qwen_will_release_another_27b_with_high/)** (Activity: 1162): **The[image](https://i.redd.it/g5uabdvdic2h1.jpeg) is a screenshot of an X/Twitter exchange where xiong-hui (barry) chen says Qwen is **_**" waiting for the exact roadmap"**_**but believes there is a high probability of another**`27B`**release, framed by the post title as a likely follow-up to the highly regarded Qwen 3.6 27B. The technical significance is speculation around Qwen continuing to optimize parameter efficiency / "intelligence density" in the mid-size dense-model range rather than only scaling to much larger MoE models.** Commenters mostly discuss local-inference practicality: some want a larger `122B-A10B`**MoE** model, while others argue that `27B` is too heavy for `16GB` VRAM users and prefer a `35B`/`A3B`-style MoE that can run on consumer gaming laptops or hybrid CPU/GPU setups.

    * Several commenters discussed the **local-inference gap around 27B models** : users with `16GB VRAM` argued that a `27B` model is difficult to run at a usable quantization level, while a hypothetical **Qwen 35B MoE / A3B-style model** could be more practical via hybrid CPU/GPU inference and would remain accessible on gaming laptops.

    * There was interest in larger **dense Qwen variants** , especially `50B`-`80B`, with one commenter noting that **Qwen 27B is already very fast with MTP** and they would trade some generation speed for higher parameter count and potentially better quality.

    * Model-size requests clustered around both **MoE and dense scaling paths** : proposed targets included **Qwen 3.7 122B-A10B** , `50B`-`80B` MoE, and dense `10B`, `20B`, `30B`, `50B`, or `80B` releases, reflecting demand for both high-end quality and locally runnable tiers.




[ Read more ](https://www.latent.space/p/ainews-openai-gpt-next-disproves)

---

## [Railway: The Agent-Native Cloud — Jake Cooper](https://www.latent.space/p/railway)
*🔬 Latent Space | 2026-05-20*

_Take the[2026 AI Engineering Survey](https://notion.qualtrics.com/jfe/form/SV_bP07tSVMXH7ePCS) and get >$2k in credits and [AIE WF tickets](https://ai.engineer/wf)!_

_This was recorded before Railway suffered a[major GCP outage](https://x.com/JustJake/status/2056881510939283776) on May 19, despite being a multi-AZ, multi-zone mesh ring, with HA fiber interconnects between their Metal <> GCP <> AWS, because workload discoverability was unintentionally still tied to GCP. All has been resolved with a [post-mortem](https://blog.railway.com/p/incident-report-may-19-2026-gcp-account-outage)._

* * *

Railway **did not** start as an AI infrastructure company.

It was founded in 2020 years before agents became the default way people thought about deploying software. **Jake Cooper** , formerly at Bloomberg and Uber, started Railway with a simple obsession: **the activation energy to ship something to production should be near zero.** Push code, get a URL, iterate. No Docker files, no Kubernetes manifests, no Ansible scripts stacked on Ansible scripts.

For years, this was a slow grind. Railway spent its **first 18 months hand-acquiring its first 100 users** with Jake personally greeting every Discord signup on a second monitor.

[](https://substackcdn.com/image/fetch/$s_!DrIQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd84197e2-29a5-4b80-b922-ae8343deac59_1078x1034.png)[src](https://x.com/JustJake/status/2034432383286759852?s=20)

Today, Railway has raised **$124m** and is growing very fast. **A 35-person team supports 3 million users, adding roughly 100,000 signups a week.** Their bare metal data centers have a 3-month payback period vs. renting in the cloud, with **70% margins** funding aggressive cloud bursting when needed. The servers they own have actually appreciated in value as RAM prices have climbed basically meaning the **value of their hardware now exceeds the capital they've raised.**

From rebuilding Railway's network overlay over a weekend to moving the vast majority of workloads onto its own **[bare metal data centers](https://blog.railway.com/p/data-center-build-part-one)** , **Jake Cooper** is trying to build a **new cloud for an agent-native world**. In this episode, Railway's founder and "conductor" joins swyx and Alessio to unpack why the next era of software infrastructure is not just ["](https://blog.railway.com/p/heroku-walked-railway-run)**[Heroku but newer,"](https://blog.railway.com/p/heroku-walked-railway-run)** what agents need that humans did not, and why the old deployment loop of Git, PRs, CI/CD, and static cloud resources may be heading for a rewrite.

We go deep on **Railway 's infrastructure stack**: own-metal data centers, three-month cloud payback periods, cloud bursting, data center debt, Railpack, Nixpacks, Temporal, feature flags, Central Station, content-addressable filesystems, agent-safe production forks, and why the CLI may become more important than the canvas in an agent world. Jake also shares the founder journey behind Railway, how the company **survived losing $500K/month** , why it now **serves millions of users with only 35 people** , and why he believes the **pull request is dying**.

* * *

**We discuss:**

  * How Railway went from a slow six-year grind to adding 100,000 users a week

  * How Railway thinks about agents as **the next dominant software species**

  * Why agents need version control, observability, compute, storage, and orchestration at 1000x scale

  * The economics of **Railway 's own-metal data centers** and three-month payback

  * How Railway uses cloud bursting while scaling its own infrastructure

  * Why data center debt can be a better tool than venture debt for infra startups

  * [Central Station](https://station.railway.com/), Railway's internal system for clustering customer feedback and incidents

  * Why responsible disclosure and over-communication matter for platforms

  * Why feature flags, progressive rollouts, and shadow traffic are essential for agents

  * Temporal's strengths, pain points, and why workflows matter for agents

  * Railpack, Nixpacks, Nix, and lazy-loaded content-addressable filesystems

  * Why "cattle, not pets" may change if you can clone the pets

  * Why Railway is building a new cloud from scratch instead of copying hyperscalers

  * The solo founder path, focus, writing, and how Jake thinks about company building




* * *

**Railway:**

  * **Website:** &lt;https://railway.com/>

  * **X:**&lt;https://x.com/Railway>




**Jake Cooper:**

  * **LinkedIn:** &lt;https://www.linkedin.com/in/thejakecooper/>

  * **X:** &lt;https://x.com/JustJake>




* * *

## Timestamps

00:00:00 Introduction: What Is Railway?  
00:02:07 Jake's Path to Railway  
00:06:13 Railway's Six-Year Growth Story  
00:08:52 Rebuilding the Business After the Free Tier  
00:11:17 Agents as the Next Software Platform  
00:13:29 Railway's Infrastructure Philosophy  
00:15:42 Bare Metal, Cloud Economics, and the Compute Crunch  
00:17:22 Cloud Bursting and Five-Cloud Networking  
00:20:20 Data Center Debt and Infra Financing  
00:23:31 Data Centers in Space  
00:25:24 What Agents Need From Infrastructure  
00:28:24 CLIs, Canvas, and Agent-Native UX  
00:35:15 Central Station, Incidents, and Responsible Disclosure  
00:40:30 Safe Rollouts, SRE Agents, and Production Forks  
00:45:00 AI SRE, Specs, Code, and Tests  
00:48:24 Self-Replicating Infrastructure and the New Serverless  
00:53:18 Heroku, Temporal, and Workflow Engines  
01:04:07 Railpack, Nixpacks, and Lazy-Loaded Filesystems  
01:06:01 Coding Agents, Token Spend, and Roadmap Acceleration  
01:10:56 The Pull Request Is Dying  
01:12:28 Feature Flags and the Agent-Era SDLC  
01:16:15 Cattle, Pets, and Cloning Machines  
01:19:29 Solo Founder Lessons  
01:24:12 Focus, GPUs, and Building a New Cloud  
01:28:20 Closing Thoughts

* * *

# Transcript

**Alessio [00:00:00]:** Hey, everyone. Welcome to the Latent Space Podcast. This is Alessio, founder of Kernel Labs, and I'm joined by Swyx, editor of Latent Space.

**Swyx [00:00:10]:** Hey, hey, hey. Today we're in the studio with Jake Cooper of Railway.

**Alessio [00:00:14]:** Conductor of Railway.

**Swyx [00:00:15]:** Conductor at Railway. Yeah.

**Alessio [00:00:16]:** Choo-choo.

**Swyx [00:00:17]:** Do you actually have that anywhere, like on your business card?

**Jake [00:00:20]:** We call some of our volunteer moderators conductors. I don't have a business card. We're not that big yet. At some point I will. I got handed a nice business card from the Supermicro folks, and I was like, "Damn, this is pretty official."

**Swyx [00:00:30]:** Business cards are coming back.

**Jake [00:00:32]:** They're cool. They're hip. The conductor thing is good. We're trying to figure out what we want to call each other internally. Some people think it's super cringe and say, "You don't need a name for people internally." Some people want to call each other something. We still don't have a really good one.

**Jake [00:00:55]:** We've got New Railcrews, Trainiacs. Nothing has stuck yet.

**Swyx [00:01:00]:** I like Trainiac. Trainiac sounds good. Railwayians. For those who don't know, what is Railway? Let's give people a crisp definition up front.

**Jake [00:01:09]:** Railway is the easiest way to ship anything. You go to the canvas, or you talk with Claude, and you say, "Deploy a Postgres instance, deploy my GitHub repository, run this code," and you're off to the races.

**Swyx [00:01:22]:** You've got a nice animation on the landing page.

**Jake [00:01:24]:** Thank you. None of my work, by the way. They don't let me touch the design stuff anymore.

**Jake [00:01:25]:** We want to make it trivially easy not just to deploy things, but to evolve applications over time. Most tooling right now stacks entropy on top of entropy: Docker, Kubernetes, Ansible scripts, and all these other things. If we can version all of your software and keep track of all the changes, then we can make it trivial to clone environments, fork into a parallel universe, get copies of production data, get copies of any services, make changes, validate them, and collapse them back in without reproducing everything across a staging environment.

## The Railway Origin Story: From Uber Systems to a New Cloud

**Swyx [00:02:07]:** I was looking at your background: Bloomberg, Uber. Nothing immediately stands out as, "This guy is going to found the next great platform as a service." What prepared you for Railway?

**Jake [00:02:21]:** It was curiosity to keep going deeper. I started out on front-end stuff, working on Wolfram Mathematica and porting it over. Then I briefly moved to Bloomberg, then toward Uber and distributed systems, taking the Jump Bikes systems and moving them to a distributed system built on top of Cadence, the pre-Temporal Temporal.

**Swyx [00:02:44]:** Which, by the way, I'm happy to talk about, pros and cons.

**Jake [00:02:48]:** Totally.

**Swyx [00:02:51]:** But let's do the Railway story.

**Jake [00:02:52]:** It has been a continual step of wanting an experience. Whether it's walking up to a bike, unlocking it, and having it work frictionlessly, or something else, the depth required to make that happen follows from the experience. A lot of the work I do, and a lot of the team does, is in service of that experience. We fundamentally don't care how deep we have to go. We will swim to the bottom of the swimming pool to get the experience.

**Jake [00:03:17]:** I don't have a physics PhD. I did an EECS degree. It has always been about figuring out the next step: how do we get there? That's what led to starting Railway for that experience and then moving all the way to bare metal data centers. I was adding patches to the kernel this week to get the experience there because I can see how much better it can be.

**Swyx [00:03:49]:** Other patches to the Linux kernel this week?

**Jake [00:03:51]:** Yeah. Not upstream. Our fork.

**Swyx [00:03:52]:** That's a flex. Railpack? No, this is different. This is the OS on top of Railpack?

**Jake [00:03:57]:** No, this is an actual kernel patch. It's always literally: what do we have to do to get that experience? Then figure it out. Anything is figureoutable.

**Swyx [00:04:10]:** Would you send the patch upstream, or does it not fit other use cases?

**Jake [00:04:13]:** Maybe. We have to work out the experience internally. It has to do with the storage layer we're building for some of the agentic stuff. Maybe it'll be useful upstream, but it's deeply useful for us internally.

## Open Source, Forks, and Non-Deterministic Versioning

**Swyx [00:04:29]:** You mentioned open source before. How do you think about starting from open source, and then coding agents letting you do a lot more from forks of it?

**Jake [00:04:38]:** GitHub's original sin is that it's almost a series of broken pointers. You have this thing, then you clone it, and now you've lost the whole upstream. How do we make it trivial for people to modify really small pieces of it?

**Jake [00:04:51]:** We think of Git in a discrete sense: I've either made a change and merged upstream, or I haven't. What would it look like if it were percentage-based, a little more non-deterministic, or a stream of changes that users traverse as a percentage rolled out in general and then rolled all the way up?

**Jake [00:05:13]:** We have the open-source kickback program and let you deploy templates because we want to make it trivial for people to version these shards over time. It solves a large problem around authentication, authorization, and security. NPM has a way to define, "Don't take any new packages." The ideal end state is that you roll out progressively to users with the minimum impact zone and continue rolling up. JPMorgan should probably be the last one on the patch line, for all our sakes, because our money and livelihoods are there.

**Jake [00:05:53]:** It's okay if Johnny Vibe Coder gets a broken patch because there's so much entropy in the system that the rubber has to meet the road at some point. You have to test at varying levels.

## The Long Grind: First Users, Free Tier, and Making the Business Work

**Swyx [00:06:13]:** I wanted to pull up this glorious chart, which is your usage or number of daily signups?

**Jake [00:06:22]:** Daily signups, I think.

**Swyx [00:06:24]:** You started six years ago. It was a slow grind, and now you're on a rocket ship. You say, "Don't doubt your fight and don't quit." Maybe pick out certain points that were key inflections for the company.

**Jake [00:06:40]:** At the start, it's about getting your first 100 users, hell or high water. We had a website and a support link. The support link was the Discord channel. I had notifications on with two monitors: the monitor I was working on and the other monitor with Discord. If anybody came in, I was immediately like, "Hey, how's it going?" It was rare, so getting those first 100 users to come back was the start.

**Jake [00:07:14]:** Then you build a consultancy factory because users want all these things. You have to go back to the board and ask, "What is the actual product offering I want to build on top of this?"

**Jake [00:07:28]:** VCs want charts that always go up and to the right, but in reality you don't necessarily want charts that look like that. For us, there have been periods of expansion where we add features to test use cases, and periods of compaction where we ask, "If the experience we have is good, how do we make it significantly better?" Maybe we strip out features that don't fit our ICP anymore.

**Jake [00:07:57]:** The boom from 2022 to 2023 came from the free tier. Everybody under the sun was using it.

**Swyx [00:08:09]:** A lot of Reddit bots and Discord bots.

**Jake [00:08:12]:** And crypto miners. When you build an open product on the internet where anybody can sign up, the internet is a horrible place with so many things. You go through periods of asking, "How do I reach as many people as possible?" Then, "How do I fit the exact use case for the people who really matter and are really excited about this specific thing?"

**Jake [00:08:39]:** Then there was a two-year period of making the actual business work. During the free-tier era, we were losing about half a million dollars a month.

**Swyx [00:08:59]:** On a $20 million bank account.

**Jake [00:09:02]:** On a $20 million bank account with maybe $50,000 a month in revenue. That's a horrible business. I don't know how anybody invested. But you have to go through it and say, "We have an experience people love, but the business has to work."

**Jake [00:09:17]:** There are two schools of thought. You can run the horrible business all the way up with bad margins, or you can go back and make it work. We've always wanted a super lean team. We're 35 people right now. It's very small.

**Swyx [00:09:36]:** Supporting three million already?

**Jake [00:09:38]:** Yeah. We're adding 100,000 users a week right now, so it's growing fast. We don't want to add headcount for the sake of headcount or throw bodies at problems. We want to build systems. It's hard to build systems during expansion because you're adding things to the system because people are asking for them or things are breaking.

**Jake [00:10:00]:** We had to cut off the free users for a little while, rebuild the business, and make sure it worked. We want to reach as many people as possible because software is important. It's become difficult to create things in the physical world, so it's important to make it easy for people to build in the virtual world and have access to creation. But there are legs to that journey.

**Jake [00:10:30]:** You can see divots in the charts. If you follow between 2025 and 2026, it's either summer or winter. People go on holiday with family.

**Swyx [00:10:50]:** It affects that much?

**Jake [00:10:51]:** Yeah. It's kind of B2C and kind of B2B. People are shipping constantly, then they stop. Our activation curve now shows more people activating on weekdays because we have more business users, so it smooths out over time.

## Agents as the New Interface to Deployment

**Swyx [00:11:17]:** Was there a point where you started prioritizing AI development or agent development?

**Jake [00:11:24]:** We've prioritized agentic as a top-of-funnel thing. Over the last six months, we've deeply prioritized agentic as a mechanism to build and deploy things because we believe the curve is so steep and that is how people will build and deploy software.

**Jake [00:11:42]:** It almost fundamentally doesn't matter whether this is dot-com or not because we're all on the internet anyway. If agents are going to deploy a bunch of things and we hit an inference wall at some point, we'll fix those problems. The dominant species over the next 10 years is that we've moved from assembly to C to C++ to JavaScript to words. You're going to need to close that loop.

**Swyx [00:12:13]:** When you say this is dot-com, did you mean buying the domain, or the general case?

**Jake [00:12:17]:** I mean the dot-com era, when companies had a huge run-up because people understood the internet was important. Then they hit bottlenecks, fundamental laws of physics, math didn't work, and everybody came back down to earth. But it didn't matter because the internet became so impactful. If you operate on a long enough time horizon, you should build these things anyway because you can see where it's going.

**Jake [00:12:45]:** That's where I think a lot of agent stuff is. You get to a point where you're running thousands of agents in parallel. What is the inference cost? What is the compute cost? How do you make that efficient? How do you coordinate all this? We have issues coordinating humans; we don't even have good tooling for that. Now we have to figure out how to get agents to coordinate, safely version changes, and know when to raise their hand for someone to intervene. Otherwise it becomes an interrupt factory.

## Railway's Infrastructure Thesis: Network, Compute, Storage, and Metal

**Swyx [00:13:19]:** Let's go right into the technical side. What are the core infrastructure or architectural beliefs of Railway that allow you to do what you do?

**Jake [00:13:29]:** The primitives matter a lot for us. We need network, compute, storage, and orchestration around it. You need control over a lot of those things. We've talked a lot about how we don't really use Kubernetes because we want higher-order control to place workloads in very specific places.

**Jake [00:13:48]:** The reason is that you have to be very efficient with agents: memory reuse and all these other things, or you're going to massively blow up your cost structure. Being able to rack and stack your own servers and build your own metal unlocks performance and cost. Experiences where you're running 1,000 agents in parallel are not massively cost prohibitive.

**Jake [00:14:13]:** Token use and compute use are blowing up. Over time, those things have to get a lot more efficient. You can get a lot of margin to make those experiences solid by building your own metal. That's all in service of offering a differentiated experience to as many people as humanly possible.

**Swyx [00:14:51]:** You have a data center in Singapore.

**Jake [00:14:53]:** Yeah. We have two in every other region now. In Singapore, we're adding a second one in Q3.

**Swyx [00:14:58]:** What's it like? I've never built a data center. Do you go to Equinix and say, "I want some slots?"

**Jake [00:15:05]:** Yeah. Equinix. You basically go and say, "I want power and I want a cage." They say, "Great, here's what it's going to be." You rent the cage for a period of time, fill it with racks and servers, and hook up internet to it. That's all the pieces.

**Swyx [00:15:36]:** Then you handle everything else.

**Jake [00:15:37]:** You handle everything else.

**Swyx [00:15:39]:** What's the math versus clouds doing it for you?

**Jake [00:15:43]:** If we rented in the cloud, our payback period when we go to metal is about three months.

**Swyx [00:15:50]:** Which is crazy.

**Jake [00:15:51]:** It's nuts. That's four years of depreciated hardware. You're going to see a lot of this compute crunch because hyperscalers are buying up a lot of stuff. We're working directly with OEMs, resellers, and people building these machines: Supermicro, Dell, and others.

**Jake [00:16:11]:** Upstream, there's a bunch of supply pressure. When we raised our last round, between deploying capital for servers and now, the amount of money we've raised is less than the amount of money we have in the bank plus the value of the servers because the servers have appreciated as RAM has gone up. It's nuts how valuable hardware has become.

**Jake [00:16:50]:** If you look at hyperscalers, they deployed around $80 billion of capital expenditures this year, and next year will be more. That's a massive infrastructure build-out. You look at that and think it's crazy that they're spending way more than the Manhattan Project. But if every person is going to run dozens or hundreds of agents in parallel, you have no conceptual idea how much compute is required to make that experience happen, even if you're deeply efficient and sharing resources. And that doesn't even count inference.

**Swyx [00:17:22]:** How do you plan the build-out? The growth chart is so vertical. Are you usually at 100% utilization as soon as racks are live? How far ahead are you planning?

**Jake [00:17:33]:** We still maintain cloud presence for bursting. We work with AWS, GCP, and a few other clouds. We can rent, and then the moment we get space or power, we compact those workloads off the cloud. We started on the clouds, then built a system to migrate to our own metal. There's nothing that says you can't continually do that again, and that's exactly what we do. We never want to be compute constrained.

**Jake [00:18:09]:** At the start of the year, we actually became compute constrained because one upstream provider wasn't able to give us quota at the rate we needed, and the hardware was slower. I spent a weekend rebuilding our entire network overlay so we could straddle five clouds: Oracle, AWS, ourselves, GCP, and one other one. We can do more than that now.

**Jake [00:18:38]:** We got into a spot where we were trying to pack instances tight because we couldn't get enough compute. That led to a few reliability issues, which are now past us. I made a tweet pointing out that it's becoming harder and harder to acquire compute at the rate these models need to acquire compute. We got bit by it.

**Swyx [00:19:15]:** How do you think about pricing knowing you might not have your own metal available at all times? Are you pricing assuming you need extra margin if you end up going into the cloud?

**Jake [00:19:26]:** Because we've built out our metal data centers, our margins on metal are around 70%. We can deeply subsidize the cloud business if we want to scale at a reasonable rate. We have a few levers: metal, which makes the margins; cloud burst; debt to buy servers; and venture capital. It's an interesting operational problem: how much cash do we have, how much should we raise, how quickly can we deploy it, and can we scale revenue as quickly as we scale compute?

**Jake [00:20:05]:** If we continue making it trivially easy for people to build and deploy, then the faster we close that loop and the more operationally excellent we are with capital, the faster the business can scale. It's almost a straight linear deployment rate.

## Financing Infrastructure: Hardware Debt, VC, and Operational Leverage

**Swyx [00:20:20]:** I think infra startups raising debt is a tool people don't utilize enough or know enough about. What can you tell us about that? Is it secured against your CPUs?

**Jake [00:20:32]:** It's secured against our hardware.

**Swyx [00:20:37]:** What rates do you get? Who are the lenders?

**Jake [00:20:39]:** We pay prime plus a spread, and we can refinance any of the debt as rates go down. The terms are pretty good. The unfortunate thing is that Twitter has no nuance, so people say, "Venture debt bad." But as with all things, there are specific tools and areas where you can be deliberate instead of using one tool as a hammer. Venture capital is not the hammer for everything. You have to explore and figure out what works.

**Swyx [00:21:12]:** VC is usually the most expensive financing you can get.

**Jake [00:21:15]:** Yeah. I also think people think about VC incorrectly from a capital-raising perspective. Most people think, "How do I raise as much money as possible from whoever is probably the best I can get at that time?" That's close to right, but what we've tried to do is figure out what unfair advantage we can buy with that equity.

**Jake [00:21:34]:** It's the most expensive equity you're going to give away at that point in time, assuming the company keeps getting better. How do you use it to work with someone stellar who complements you? In the seed stage, I had never started a company. Ray Tonsing had good advice, and I could text him all the time. He was really fast. Awesome.

**Jake [00:22:01]:** Then with John and Erica at Unusual, they said, "You roughly know what you're doing building a product. We'll mostly leave you alone and be available for advice." Amazing. Then we got to Series A and the business was an operational tire fire because we didn't know how to scale a business. Work with Erica, and Jordan is over at Redpoint, so bonus.

**Jake [00:22:28]:** Now we've raised from TQ and FPV as we're moving into enterprises. Every step of the way, we've asked: who can we partner with at this specific time to unlock the next section of the journey? I don't know enterprise sales. As an engineer, I can eyeball what features we might need, and we have wonderful people internally who can help. But you want boardroom dynamics where everyone is aligned and asking, "How do we win this?" instead of bickering about strategy.

## Data Centers in Space and the Physics of Compute

**Swyx [00:23:31]:** You had a tweet about data centers in space. Why no data centers in space?

**Jake [00:23:37]:** It's not "no data centers in space." My hot take is that I think it is solvable. I've just never seen anybody solve it.

**Swyx [00:23:49]:** You said, "How are you going to dissipate that much heat in a vacuum?" You're making a physics claim.

**Jake [00:23:55]:** I haven't seen anybody prove how you're going to dissipate that much heat in a vacuum. It doesn't mean it's not possible. It just means nobody has brought it up yet.

**Swyx [00:24:05]:** Astrophage.

**Jake [00:24:06]:** I don't know what that is.

**Swyx [00:24:07]:** The Martian thing. Okay, you're very logical.

**Jake [00:24:09]:** It could work. A lot of people are putting the cart before the horse. They say, "We're going to put data centers in space." Okay, but how? "We have time to figure it out." It's like in The Martian where they ask how they're going to intercept something and say, "We'll figure it out."

**Swyx [00:24:36]:** Making a bet on human invention is weird because you blind trust that it can be solved. But with physics, there are first-principles bounds you can put on it. Maybe not. Maybe you're asking to travel time or break a fundamental thermodynamic law.

**Jake [00:24:57]:** I don't know how VCs do this either. How do you know what's not possible and a grift versus what's possible but sounds completely insane? "We're going to put data centers in space." Coin flip as to which it is, and I guess you'll know in 10 years. That's one cycle.

## What Agents Need: Versioning, Observability, and 1,000x Scale

**Swyx [00:25:23]:** Moving back to agents. The branching, fast spin-up, and orchestration you do feels like pre-work that happened to be exactly what agents want. What do agents want differently than humans?

**Jake [00:25:37]:** They want the ability to version things. It's not that different; it materializes slightly differently. Agents want a way to test changes incrementally. Engineers have feature flags. Is there a reason agents can't use feature flags? I don't think so.

**Jake [00:25:54]:** They want version control. Can we use Git or not Git? That one is up in the air. I think something outside Git will emerge for how we version these things over time. They need observability. You need to query what happened, when it happened, which steps failed, traces, logs, metrics, and all the rest. They need network, compute, and storage. They need to write files, save files, iterate on files, and snapshot file systems.

**Jake [00:26:25]:** A lot of what humans needed is in line with what agents need. Branching and forking are not different; we're just moving 1,000 times quicker. It can look like you need something massively different, but what you need is something massively better than what existed. You need orchestration massively better than Kubernetes. You need networking probably better than Envoy. It goes all the way down the stack.

**Jake [00:26:55]:** If the workload profile doesn't change so much as it gets massively compressed because you need thousands of these things, what assumptions change? etcd is going to melt. You need to replace it with something. You can go all the way down the stack and say, "That part has to change, that part has to change, and that part has to change."

**Jake [00:27:19]:** The interesting thing about the super-exponential curve is that you have to build systems where you can rip out those parts at any time because a new bottleneck might emerge. You get good at parallel agents, and a different part of the system breaks. So it's similar to what humans needed, but at 1,000x scale.

**Jake [00:27:55]:** How do you do code review in the age of agents?

**Swyx [00:28:00]:** You throw more agents at it.

**Jake [00:28:01]:** You don't. But then who reviews for CVEs and all these other things?

**Swyx [00:28:07]:** More agents.

**Jake [00:28:08]:** And that's how we hit the inference wall. You can continually throw agents at the problem, but I think there's a limit to the number of agents you can throw at a problem.

## CLI, Agent Handles, and Closing the Loop

**Swyx [00:28:24]:** You already had a CLI before it was cool. How is the shape of what you're exposing changing, if at all?

**Jake [00:28:28]:** CLIs have always been cool. The CLI changes because we think about how to give Claude, Codex, ChatGPT, or any model a handhold.

**Jake [00:28:50]:** A CLI is a single command: deploy, get logs, and so on. Things that were prohibitively annoying to humans are not annoying to agents. They're nice. If I handed you a CLI with 40 arguments and 600 flags, you'd think, "I'm never going to use all of this." But if you hand it to an agent, it says, "This is excellent. I have so many handles to work with."

**Jake [00:29:24]:** If you're going to expose things to agents that way, you want as many handles as possible where they can get information, query dynamic information, and close the loop quickly. Most problems right now are about how to close the loop as quickly as possible. Where does the agent get stuck, and how can you remove that?

**Jake [00:29:49]:** Telemetry is important. If you can tell where the agent gets stuck from the CLI and say, "12% of people deviate from the happy path because of this, and now I add this argument and drive it down to 2%," you massively increase the rate of loop closure.

**Jake [00:30:03]:** That's how we think about not just the CLI, but every point in the dashboard. It's a user journey: I hear about Railway. I get something deployed. I get my first green build or aha moment. I see an endpoint, logs, whatever. Then I iterate. The iteration loop is indefinite. The user wants to deploy a new thing, a Postgres instance, change code, and keep iterating.

**Jake [00:30:36]:** If you focus on the iteration loops and what's blocking them from closing quickly, one thing we say internally is: you never want to be waiting on compute anymore. You always want to be waiting on intelligence. If you're waiting on compute, there's a bottleneck that needs to be destroyed because eventually that bottleneck becomes so large that another workflow emerges to change it.

**Jake [00:31:04]:** We've built a product where you push code, build it, and so on. But I fundamentally believe the push-pull loop is going away. We'll get to a point where you make a small change in production, that change is versioned across your infrastructure, you're working alongside copy-on-write versions of your database and infrastructure, and then you merge it in and it's instantaneously live. That's the holy grail of loops. The push-pull-rebuild thing is a point of friction that we're removing entirely.

## Canvas as Output: Dashboards, Context Anchors, and Hyperstructures

**Swyx [00:31:43]:** It's incredibly fast. If anyone hasn't tried it, that fast feedback is great. My hot take is that Railway was famous for its canvas, which visualizes your infrastructure and lets you manipulate it visually. But that was for humans. For the next phase of growth, Railway CLI is more important than canvas.

**Jake [00:32:05]:** The canvas is funny because it's a mechanism to show changes over time. You're right that previously we used it a lot as an input. Moving forward, its goal is more like an output. You would go to the canvas, make changes, see them, and watch your infrastructure evolve. Now agents have access to the CLI and can make those changes. So the canvas becomes an output: what information does the human need at this moment to make suitable decisions about control requests? Do I approve this or not?

**Jake [00:32:57]:** It also has to be an anchor for your context, a port in the storm. Think of it like layers in a file system. You start with a project, then drill down into services, then into a function or code, because you want to represent the entire thing not just in your head, but in the canvas. Other people can share that representation, think on the same wavelength, and move quickly.

**Jake [00:33:33]:** A lot of organizations get in trouble as they scale because all the context lives in someone's head. "How does this microservice work?" "I have no idea; go ask this person." Then you have whole categories of products built around context discovery. A lot of that melts away if you have a solid hierarchy and can infinitely nest services, code, context, and everything else all the way down. That's what lets you build these structures over time.

**Jake [00:34:18]:** It's also what lets us build what I've called hyperstructures: things that are way bigger. You look at the Golden Gate Bridge and ask, "How did we build that?" There's a meme that we lost the technology. To some extent, yes, because the coordination that built those things evolved and changed. We lost some of the art of building structure as we jammed everything into Slack.

**Swyx [00:34:52]:** But you jam everything in Discord.

**Jake [00:34:53]:** Same point. It doesn't matter. It's message passing and interrupts, message passing and interrupts.

**Swyx [00:35:00]:** So you're arguing there should be something better and more structured than Slack?

**Jake [00:35:04]:** Yeah. For sure. I think Slack is awful, and Discord is awful too.

## Central Station: Context Routing, Support, and Incident Clusters

**Swyx [00:35:09]:** This is the equivalent of my mom test. What have you done that has your solution to this?

**Jake [00:35:15]:** Internally, we've built a tool called Central Station that aggregates all the context from our users. Every piece of feedback, every customer support item, everything gets aggregated into clusters. If an incident is brewing, we can determine how many users are affected and break off a discussion based on that.

**Jake [00:35:40]:** That is more helpful than long-running channels where you're trying to decide which channel to put something in. If you can dynamically aggregate information and dynamically route it to the right person based on context, it works better. We know internally that these four people are close to networking. If we see a networking thing, we can drill it down to those four people. If it's with this part, we can look at the commits. This is no longer a manual process internally.

**Jake [00:36:13]:** If you go to station or help.railway.com, that's why we built it. We wanted to scale with a massive amount of leverage by aggregating feedback.

**Swyx [00:36:27]:** This is built in-house?

**Jake [00:36:28]:** Yep.

**Swyx [00:36:29]:** I remember helping out on this one with Angelo in 2023. You scale a lot with a very small team.

**Jake [00:36:38]:** Yeah. We're about 10 times bigger now.

**Swyx [00:36:40]:** You have your full developer code here? Very cool.

**Jake [00:36:44]:** If you go to railway.com/stats, we expose this as a pub-sub-able thing. It's all real-time metrics. There's a way to get it as JSON somewhere if you care.

**Jake [00:37:01]:** We're big on trying to build everything in public and talk about what we're working on. We've had issues in the past, and we'll say, "Here's how we're fixing these things." We've gotten compliments and flak for incident reports. We're always trying to make them better and talk with people.

## Incidents, Disclosure, and Progressive Rollouts

**Swyx [00:37:20]:** You had a big one recently. I liked that it was scoped to 3,000. You presumably used Central Station. Talk through what happened and how you address it internally as a team.

**Jake [00:37:38]:** Internally, this one really sucked. It had to do with an upstream provider that didn't do the behavior it said it documented, which is unfortunate given they wrote the RFC for how the behavior should work. We rolled those things out, and Central Station caught it initially when a couple users said caches weren't invalidating. We turned it off immediately.

**Jake [00:38:03]:** When you roll out to a large user base of three million people, you get a lot of disparate behaviors. We tested in staging and had tests, but we hit an edge case. We've hardened those systems, and now we can make that better. But it was a tough one.

**Swyx [00:38:39]:** I always wonder how private disclosure is supposed to work if people find an issue. Are they supposed to contact you first? When you run a platform, these things will happen. What channels should people pursue to quietly resolve it before it becomes a bigger incident?

**Jake [00:38:59]:** There's responsible disclosure. We err on the side of over-disclosing and letting you know something is wrong versus having your provider gaslight you. We've erred on sharing those things more publicly, even if they impact a small subset of users. That's a decision we've made internally. We have four values. One is honor. The honorable thing is to notify people to the widest degree at which they may have been affected or there was an issue, and then confront it head-on: why did it happen, what can we do better?

**Swyx [00:39:45]:** Not the whole user base. That's because of incremental rollouts and other things?

**Jake [00:39:50]:** Yeah. Progressive rollouts.

**Swyx [00:39:54]:** That should be the norm at all large platforms.

**Jake [00:39:58]:** It should. A variety of companies do this. There's the quote that Meta runs 10,000 different versions of Meta. To our earlier point about agents, they need the same thing. They need shadow traffic and all these other things. We've built so much ceremony around production being sacred that we need to make it trivially easy to test different behaviors in a safe environment. Then you can make mistakes in a safe environment.

## Safe AI SRE: Customer Agents, Forked Environments, and Production Parity

**Alessio [00:40:30]:** Do you see a world where these things get automatically caught, not necessarily by your agent, but by your customer's agent? The cache invalidation issue seems easy to check if you know to look for it.

**Jake [00:40:44]:** It's hard because to determine it, we almost need to hook into your observability infrastructure. That's why we have the template loop on the platform: so you can roll things out progressively. You can roll out to Johnny Vibe Coder initially, or push a shard that someone consumes at their own leisure. Or you can roll it out over weeks: 0.1% of people, 1% of people, early adopters, then all the way up. That's the non-deterministic version control we talked about earlier.

**Jake [00:41:30]:** I believe that's where most things should go, because most companies end up building staged rollout systems in-house. It's the same thing built again and again at every company. There's a massive opportunity to consolidate developer debt.

**Alessio [00:41:45]:** You should have a free tier. Model providers give free tokens if you let them use the data. You could give free compute if someone is the number-one shard that goes out and lets you plug into their observability.

**Jake [00:41:55]:** We do that. That's why we talked about the impact on 3,000 people. We start with lower-impact people. Larger companies on the platform are last to receive those rollouts so they have a version of the platform that's deeply stable.

**Alessio [00:42:16]:** I have three services, so I'm sure I get the first rollout. You can nuke my thing at any time. There are all these SRE agent companies. Observability people also want agents that fix upstream problems. You have your own agent in the canvas now. How do you see that playing out?

**Jake [00:42:39]:** It's the stacking entropy problem. If you don't have primitives to make iteration in production safe, it becomes difficult. If you're an observability provider saying, "Here's the fix to this error," assume 80% are good and make sense. But in the last 20% long tail of complex issues, if you let somebody stamp it, you create an opportunity for an incident.

**Jake [00:43:08]:** That's why forked environments are important. People have staging, but it always drifts from production. You need primitives, workflows, and experience built first-party on the platform so you can fork any service at any point in time.

**Jake [00:43:33]:** I think of the canvas as a sheet of transparency paper. The agent is a little guy you push up into the canvas. It should say, "I need to copy that service and that service so I can test these two things." It gets a read-only copy of production. Anything that's PII gets marked as a transform when we clone the database, create a copy-on-write version, or read from it. Then the agent makes changes and asks, "Does this actually work?" as close to production as possible.

**Jake [00:44:22]:** That's how close you have to be, or you get massive drift. The system becomes unstable. You see this with massive systems built on Docker for local, Kubernetes for production, and a specific thing for something else. That complexity slows developers and becomes unstable at scale, making it hard to iterate. We want to compress that way down and say, "As close to prod as possible is where we want to be."

## From AISRE Skeptic to Agent Believer

**Swyx [00:45:00]:** I was texting Erica for questions, and she says you were originally not a believer in AISRE. Have you come around on it?

**Jake [00:45:10]:** I flipped, but I'm still not a believer in AISRE if you don't have the primitives to make it safe. If you unleash AISRE on production infrastructure without safe primitives for copying volumes and making sure things are fine, it's going to nuke your production database. It's not a matter of if, but when. I'm a big believer in making those loops safe.

**Jake [00:45:33]:** I was a deep AI skeptic until 2023. In 2024, I thought, "Maybe I can roughly make this thing do it." In 2025, I thought, "Now I can hold this." Over winter break, everybody came back saying, "It's almost impossible to hold this."

**Swyx [00:46:01]:** Did you see this on the Claude docs? CloudBot? OpenCloud?

**Jake [00:46:06]:** It's gotten to a point where it's harder to hold it wrong than to hold it right. There's a scene in Avengers where Vision picks up Thor's hammer and says it's terribly well-balanced. It self-balances and works well. I'm a deep believer at this point that this will be the dominant species: assembly, C, C++, JavaScript, words.

**Swyx [00:46:35]:** It feels like a big jump.

**Jake [00:46:37]:** It is. But it's not like you abandon CPU-based discrete logic and move straight to fuzzy logic. You need both. Your skills should call code or applications or some static structure. You can use skills to distill what the procedure should be or how the code should act.

**Jake [00:47:02]:** I'm coming to a thesis: you need three points. You need a clear spec defining the system, the code, and the tests. When you say it out loud, if you've been in engineering long enough, you're like, "Of course. That's an RFC, tests, and code." But they all matter. Having them together lets them reinforce each other: the spec and tests match, but the code doesn't, so reconcile it. Or the tests and code match but the spec doesn't, so reconcile that. That's the iteration loop.

**Jake [00:47:41]:** That's why you're seeing people talk about software factories, docs, and reconciliation. Some of that is architectural astronomy if you don't implement it, but that loop is where most things will end up.

**Swyx [00:48:07]:** For listeners, we've been talking about this on the pod for three years: the holy trinity of specs and tests. Itamar Friedman from Qodo is the reference if people want to look it up.

## Self-Modifying Infrastructure and the End of Push-Pull-Rebuild

**Swyx [00:48:18]:** One thing I want to mention on the OpenCloud idea is self-modification. I don't know how Railway would support it, but I have my OpenClaw, and I just tell it it has the Railway CLI and can do whatever. In theory, whatever capabilities or new infra it needs, it can call the Railway CLI, provision it, and add it to itself. The agent can modify its own infra.

**Jake [00:48:45]:** It's nuts. I have a loop set up where you put the Railway CLI on top of something that runs on Railway. You're authenticated as whatever the current box is, and you can make any changes to it. Then you call Railway deploy, and it deploys itself.

**Jake [00:49:04]:** It's like: "I need to spin up this instance of this environment. I already exist in this environment. Excellent, I have access to a Postgres instance now." That's where we want to go with agentic, self-replicating infrastructure. That's your loop: iterate in production. You continue making changes. If it works, merge it upstream. If it doesn't, throw it away.

**Jake [00:49:37]:** How do you make throwaway copies trivial to spin up and super cheap? The era of "I have an AWS instance with four vCPU and 16 gigs of RAM" is going to get destroyed. If you do that for agents, you need a thousand of those machines. It's prohibitively expensive compared with what we've spent a ton of time figuring out: the atomic unit of deploy, whether you call it isolates, sandboxes, or something else. Only pay for what you use, spin up instantaneously, and close the loop as quickly as possible.

**Jake [00:50:15]:** If the system can self-replicate safely and say, "This is my environment, I'm making these changes," it can come back with, "Does this look good? This is a new state of infrastructure given this prompt. I think I've solved it." Then you go back and say, "Actually, it looks different." It does the loop again. Then you say, "Cool. Apply."

**Swyx [00:50:38]:** That's retroactively obvious, which is the most useful kind. Any other comments on agent deployment on Railway?

**Jake [00:50:51]:** It's getting better every day. I'm on X or Twitter. You can always yell at me about the parts not working as well as they should, because plenty of things should work way better.

## The New Serverless: Stateful, Long-Running, Pay-for-What-You-Use Linux

**Swyx [00:51:04]:** At this stage, when people want massively or embarrassingly parallel compute, they usually talk serverless. I feel like there's a new serverless compared to the previous five years of serverless. You're in that new bucket. Do you have comparisons or philosophical differences you want to call out?

**Jake [00:51:31]:** It's somewhere in between. It's the ability to run stateful, long-running workflows or executions.

**Swyx [00:51:42]:** Vercel has Fluid Compute, Cloudflare has some container thing, Google has App Runner and others.

**Jake [00:51:55]:** That's where everything is roughly going, and it's why we've been working on this for six years. We believe users need access to a computer: a box that speaks Linux. They need to deploy what they want. Other systems change the surface area of what you can build. For us, users need a computer and need to deploy anything they truly want. That's why we've focused on the primitives: network, compute, storage. If we give you those and expose them so you can run things indefinitely, that's where we believe it's going.

**Jake [00:52:43]:** Twitter has no nuance, so everyone says "servers" or "serverless." It's always somewhere in the middle: I want to run it for a long time, but I don't want to provision the resource statically or pay for things I'm not using. That's been our thesis from day one: pay only for what you use, run it indefinitely, and it is full Linux.

**Swyx [00:53:12]:** That's why I like the naming of Fluid. It's fluid. Flexible.

## Heroku, Focus, and Carrying the Torch Without Becoming the Past

**Swyx [00:53:18]:** Another milestone is the Heroku official deprecation. You're one of the presumptive new Herokus. "New Heroku" has been a category for as long as I've been in developer tooling. It's finally happening. What was that like? Any behind-the-scenes of, "This is the moment"?

**Jake [00:53:42]:** You have people where you're like, "You were running stuff on here? You, as this company?" It's crazy that names you would know are running on it and now coming to us saying, "We want to move a lot of this off."

**Swyx [00:54:00]:** Any behind-the-scenes on why Salesforce let Heroku stagnate?

**Jake [00:54:05]:** I can only guess. It's hard when it's not your business. Salesforce's business is to build a great CRM. That's their focus. Then you acquire a compute business as an offshoot. A lot of early Meta people talk about focus. Boz has a write-up about how in the early days of Meta they had no money, so they were forced to focus. Then they turned on the money tree and had no reason not to split their focus.

**Jake [00:54:52]:** But that dilutes your product. You get offshoots where you ask, "Is this the focus of the business?" If it's not core, it languishes. A lot of companies get in trouble when they split focus because they're fighting a multi-front war, not just externally but internally for alignment. Where are we going? What are we doing? What is our purpose?

**Jake [00:55:24]:** If you're Salesforce-built and mission-driven, you want to work on Salesforce. Heroku is off to the side. It's not core to the business. Getting resources, budget, focus, and alignment internally becomes hard. It was a matter of time.

**Swyx [00:56:06]:** Kudos for them to call it out instead of leaving it unknown.

**Jake [00:56:12]:** Their release was a little odd. They called it out, but they didn't say they were shutting it down. Behind the scenes, I think they issued messages to people saying they should close accounts and that they were going to deprecate and remove things over time.

**Jake [00:56:30]:** It's crazy because some of my first deployment experiences were on Heroku. You start with dragging things into an FTP server, then you try to get a deploy working, and then it's Heroku. It was the on-ramp for us. But the wheel turns. New things emerge. We're happy to carry the torch for a lot of that. But we don't want to be the new Heroku. We want to be the way people build and deploy software, and ultimately the way people monetize software over time.

**Swyx [00:57:19]:** It's still a big crown to be the new Heroku. There are 50 companies that fought for that.

**Jake [00:57:23]:** Everybody is holding some portion of it. We're happy to support people and companies. The platform works differently. The game loop is similar, but we've been dogmatic about where these things are going: primitives, agents, fan-out. Some things fit; some workflows need to change. We have an approximation of Heroku pipelines with the environment system. It's exciting. We've got a ton of people we can support, and it's growing a lot.

## Temporal, Workflow Engines, and State Machines

**Swyx [00:58:12]:** I have one more technical question about Temporal. I've sold my shares. You're a power user and one of our earliest customers. I met you through Temporal. You built on Temporal. You have complaints. This may be the most neutral and informed conversation anyone will hear about Temporal without someone working at the company.

**Jake [00:58:39]:** That's fair. I've used Temporal for almost 10 years because of Cadence at Uber.

**Swyx [00:58:52]:** Give people a sense of what Cadence was at Uber.

**Jake [00:58:57]:** Cadence was the precursor to Temporal. It powers trip actions, rides, when you rent a Jump bike or scooter or car. You're running workflows for a period of time and saying, "This ride will run indefinitely until it finishes." You attach information: you paused in this zone, so add this charge to the bill. When you end the trip, the workflow is done. That experience was powered by Cadence at the time.

**Swyx [00:59:34]:** I used to say it's like programming the entire user journey top-down as one function.

**Jake [00:59:39]:** It's a powerful idea and important. It's also important for the next phase of the agentic journey. You want an agent to do a specific task, be complete or incomplete on that task, and move on to the next thing. You need a way to manage workflows dynamically.

**Jake [00:59:59]:** Temporal was always great in theory, and great when you got it working the way you wanted in production. But it required you to model the entire journey in your head. If you didn't, you could cause issues where replaying the state of the workflow causes non-determinism.

**Swyx [01:00:25]:** Because it works on deterministic workflow history.

**Jake [01:00:28]:** Exactly. I describe it as a jet engine. If you know how to operate it and run it, it's great. But you can't hand it to people trying to build complicated things if they don't have the whole state in their head.

**Jake [01:00:48]:** We run our whole deployment pipeline on top of it. That's a reasonably complicated workflow: pre-commit hooks, signaling, queuing, and all the rest. We ran into the same thing at Uber. As you express a large workflow, it gets more complicated, with more states in the state machine that you have to map back to the workflow.

**Swyx [01:01:15]:** It's a lot of ifs.

**Jake [01:01:16]:** Exactly. At Uber, we built a system for doing the state machine and testing it. We've started to build some of those things here because it's grown heavily. It's not quite love-hate. When it works well, it works super well. But if someone who doesn't have full context puts something into the system that invalidates state or causes non-determinism, or spins off a ton of activities, you have to keep track of underlying SRE knobs like activity slots. Those should scale with memory, vCPU, and so on. It becomes a bear to scale.

**Swyx [01:02:10]:** You need a capable sysadmin running things behind the scenes. If you moved off, what would you do?

**Jake [01:02:19]:** We'd build our own workflow engine. We have a few internally that we've worked on.

**Swyx [01:02:27]:** This is one of those classes of things you typically wouldn't vibe code, but I'm wondering if you can.

**Jake [01:02:33]:** I still don't think you should vibe code it. You still want to run decent tests to make sure it works.

**Swyx [01:02:39]:** Timo didn't invent that from scratch either. There are libraries you can run. On top of that, it's just a state machine that you have to map out. Ultimately, you define the instructions you want and run them through a state machine.

**Jake [01:03:00]:** It's very doable. Workflow stuff is interesting. Restate is doing neat stuff here.

**Swyx [01:03:10]:** You're tied into JavaScript. Are you a JavaScript maxi?

**Jake [01:03:13]:** Internally, we have TypeScript, Rust, and Go. We don't add more languages. Actually, we have a little C because we write BPF code and hooks. But those are the languages.

**Swyx [01:03:28]:** Is this for sidecars?

**Jake [01:03:32]:** No. It's for the networking stack, volumes, and things like that. We use TypeScript a lot because it powers the dashboard, but we're moving a lot of workflow stuff off the dashboard stack and into the infrastructure stack.

## Railpack, Nixpacks, and Content-Addressable Filesystems

**Swyx [01:04:00]:** Cool. Any other technical infrastructure stuff? Railpacks?

**Jake [01:04:07]:** We built an engine for determining dependencies based on source code. It's called Railpack. We built the first version, Nixpacks, on top of Nix, and then we moved.

**Swyx [01:04:17]:** People have been trying to get me to adopt Nix and NixOS for four years. Is it ever going to be a thing?

**Jake [01:04:23]:** I don't know. We're excited about it, but it has pain points. Think of it as a stack of versioned binaries at specific slices in time. If you want version X and version Y, you bloat the package space, which blows up image size and makes real-world workloads difficult.

**Swyx [01:04:53]:** But you content-address it and cache it. In theory, there are optimizations.

**Jake [01:05:00]:** In theory, yes. But with a large enough user base and disparate enough machines, you run into a problem Meta described in the XFAAS paper, their internal serverless system. It becomes difficult at scale unless you break out specific runtimes.

**Jake [01:05:24]:** We didn't want to do that because we wanted to truly allow you to deploy anything. That was our initial thing with Nix. But we've moved toward interesting work around content-addressable file systems that can lazy-load anything from any point and page it into memory.

**Swyx [01:05:48]:** Amazing.

**Jake [01:05:49]:** The future is very bright. It's crazy, and it's going to be nuts.

## Coding Agent Spend, Roadmaps, and Token ROI

**Swyx [01:05:54]:** Founder journey stuff?

**Alessio [01:05:56]:** Your cloud usage: you tweeted you're going to spend $300K this month?

**Jake [01:06:01]:** I think we got to $200K.

**Alessio [01:06:02]:** Coding agents?

**Jake [01:06:03]:** Yeah.

**Swyx [01:06:04]:** Across the company?

**Alessio [01:06:05]:** You only have 35 people, so I'm sure they're not all spending $10K a month. What's the distribution?

**Jake [01:06:10]:** I think I'm at about $25K. We have power users all the way down. We came back from winter break, and I basically said, "If you're writing code by hand, you're doing this wrong." The tools are good enough now that you can move extremely quickly. There are issues and pain points, but you should be reviewing the code you are writing instead of writing it by hand.

**Jake [01:06:40]:** Architectural patterns matter more now than ever, but you shouldn't spend your time generating code you would write. If you know how to write it, ask the agent to write it and reconcile it until it looks like you would have written it yourself.

**Jake [01:06:58]:** People misconstrue my propensity to push people toward agents as connected to our growth and some reliability bumps. They're not necessarily related. The tools are good enough to move extremely quickly and build things way larger than you could before.

**Jake [01:07:19]:** To the earlier point about cooling data centers in space: I don't know. But with software, you can ask, "How would I build block storage from scratch? How would I do these things?" I have ideas because I have history and have read papers. Let me work them out and build massive test benches with thousands of tests, because those are now free to author. If you're not using AI systems to speed-run your roadmap and reconcile your existing system onto the future, you're missing a large point of what's happening.

**Alessio [01:08:12]:** What's the path to spending $3 million a month? Is it bound by ideas and things customers can absorb?

**Jake [01:08:19]:** For most companies, it's bound by deployment at this point. That's why we've seen a massive boom in users and companies, from Fortune 50s down, asking how to get developers to move faster. You'll probably hit your CFO before any technical limits because they'll look at the eye-watering amount of money spent on tokens. Inference costs have to come down, but we're inference constrained now. There will be price discovery around what makes sense for an org to adopt.

**Jake [01:09:06]:** I think you'll end up with the F1 driver concept. If someone is really adept at these things, it makes sense to put them in a $3 million car. If they're not, it probably doesn't make sense. You'll take a few people and say, "You can drive the F1 car. We need to go in this direction. Figure out if it works and prototype it."

**Jake [01:09:33]:** We've done some of that and vastly accelerated our roadmap. We thought we'd ship something in a few years; now we can probably ship it in a few months because we validated it and don't have to build it incrementally. We can skip steps and move toward our vision.

**Alessio [01:09:58]:** A lot of people are realizing the roadmap doesn't always have a business impact, so they say tokens are too expensive. But if your roadmap were built to make more money by the time you built it, you'd have token pricing for it, the same way you do with sales. You'd spend a billion dollars on sales if you knew you would get $2 billion of revenue.

**Jake [01:10:19]:** Exactly. A naive way to measure this is the percentage of tokens that end up in production. If you can measure impact because those tokens end up in production, that's awesome. But the burden of proof will rise. Internally, we have a growing number of pull requests that haven't merged. The question becomes: how do you get this into production? It's about how quickly you can build and deploy software, which is exciting because that's our whole thing.

## The SDLC Shift: Prompt Requests, Feature Flags, and Safe Rollouts

**Swyx [01:10:56]:** The SDLC is changing. One thesis is that the pull request is dying. It's going to be the prompt request. Beyond that, code review is also kind of dying if you have all the other systems in place. What else is changing about the SDLC?

**Jake [01:11:19]:** The AISRE and the tools to make it happen. AISRE is pie-in-the-sky aspirational. What does it take to get an AISRE? What tools do you need to build?

**Swyx [01:11:32]:** You should expose your tooling to customers at some point. The Central Station command center.

**Jake [01:11:39]:** We have it for template maintainers. Template maintainers can deploy and maintain templates, and they get feedback. We're going to expose those things incrementally.

**Swyx [01:11:51]:** Clustering around incidents. Everyone has a version of that, but I don't think anyone has solved it.

**Jake [01:11:56]:** I won't say we've solved it internally, but it's gotten so good that we can see incidents forming pretty quickly. At some point, those will be things either someone else builds or we build. We've always built things purpose-built for us. If it makes sense to make it useful for users, monetize it, or turn that loop into a profit center instead of a cost center, we want to do that.

**Jake [01:12:28]:** Pull request is definitely dying.

**Swyx [01:12:29]:** Do you do first-party feature flagging and incremental rollout stuff?

**Jake [01:12:34]:** We have a feature-flagging engine we built internally and will eventually roll out.

**Swyx [01:12:38]:** I don't see it as a user. How come you didn't give us what you have?

**Jake [01:12:43]:** We have to beta test it. We care a lot about the quality of the things. There's plenty we've used internally that doesn't make it all the way through the journey because it fails. It works for one service but not multiple services. We'd have to build it for multiple services and know that if we released it, we'd rebuild it again and again. Some things are worth that, but many inform the roadmap.

**Jake [01:13:18]:** We don't want to dilute the experience by saying, "This works, but only for this service," unless it's a core initiative. Over the next few months, we'll roll out things that work for a single service, then multiple services, then multiple services across the environment. You have to be deliberate. Otherwise you create broken disparate experiences and support load because people ask how to use the feature.

**Jake [01:13:52]:** It's the earlier expansion and compaction pattern. You expand the company to get features, then compact and smooth them out so the experience is stellar. You told me in the hallway, "It's gotten so much better." Internally we're saying, "This part really sucks. We need to make it significantly better."

**Swyx [01:14:11]:** I can attest to that over the last three years watching you build Railway. For listeners, feature flagging is a huge part of Uber culture. So much so that they have too many feature flags and another thing to remove feature flags. Facebook has Gatekeeper. Agents are going to need this. It's fundamental to incremental rollouts. OpenAI acquired Statsig. GPT-5 is routing and flagging through different models.

**Jake [01:14:56]:** It's super important. If the software development lifecycle is going to change because we're doing things 1,000 times faster and 1,000 times more concurrently, what becomes important at scale?

**Jake [01:15:16]:** Before I started Railway, I built a feature-flagging product and tried to sell it. It was an easier version of LaunchDarkly. I ran into a problem: anyone small enough to adopt your technology doesn't care about feature flags, and anyone large enough to need feature flags needs so much scale that you have to build out all the infrastructure. I scrapped it.

**Jake [01:15:42]:** But what is old is new again. Companies are trying to move quickly, but you can't YOLO a vibe-coded thing straight into production. You need to say, "Here's my blast radius, my impact, and I want to shadow it for these users." Feature flags. You're going to need the tools larger companies built to maintain their structures. Everything gets compressed by 1,000x so everybody can build those structures quickly.

**Jake [01:16:07]:** That's exactly where we are: compressing the software development lifecycle, then expanding it and adding more new things.

## Cattle, Pets, and Clonable Infrastructure

**Swyx [01:16:15]:** Another term that comes to mind for newer developers is "cattle, not pets." People treat production like a pet. It has a name. You baby it and keep it alive. With cattle, you can mass farm, roll out, portion parts out, and kill them.

**Jake [01:16:37]:** I think that might change. You can move toward having pets as long as you have a cloning machine for your pets.

**Swyx [01:16:52]:** Yeah.

**Jake [01:16:52]:** If you can snapshot every single thing at every frame, it doesn't matter if something gets obliterated because you have a snapshot of it. The things we've built right now are designed to block changes from the hermetically sealed DevOps line. You have to write a Dockerfile because you need a specific cut of the file system.

**Jake [01:17:14]:** What if you had the whole file system? What if you snapshot it and lazily load the entire file system? Then you get around this problem entirely. You don't need the ceremony of Dockerfiles, Ansible scripts, or other things. You can iterate, snapshot, ask if it's the right loop or state, and then merge it into production. Merge the file system.

**Swyx [01:17:45]:** Why not?

**Jake [01:17:46]:** It's going to be fun.

**Swyx [01:17:47]:** This is a whole other can of worms, but if you cataloged the stateful things in a VM and developed dedicated solutions for each, you can cut the problem down a lot. It's surprising people weren't trying until now.

**Jake [01:18:04]:** It has always been surprising to me because these are the things we would work on. It's obvious.

**Swyx [01:18:11]:** At first principles, you need them. Everyone needs them in theory. Then the big clouds don't do them, so you assume it's impossible.

**Jake [01:18:18]:** Exactly. You think, "Meta has all the people writing eBPF code, and they're doing something with them." But you need that kind of work to solve these problems. Whatever is required, however deep we have to go, we'll go all the way down to the kernel's TCP/IP stack if needed. If we need to modify something to make it work for the mental model of the universe moving forward, we'll do it and keep going down.

**Swyx [01:18:52]:** That sounds fun.

**Jake [01:18:53]:** It's so much fun. I have to peel myself away from fun, interesting problems to make sure we can scale the company in a way that works. There are so many fun problems: getting information from customers to support to the person who built the thing internally, safe iteration, context from the dashboard to users, drilling down to the infrastructure layer, and managing orchestration as a real-time operating system versus a feedback control system. It's just so fun.

## Solo Founder Lessons: Obsession, Writing, and Focus

**Swyx [01:19:29]:** Speaking of the founder side, you're famously outside the YC/SF consensus. You go to YC, get a co-founder, and do all these things. You did none of that.

**Jake [01:19:40]:** None.

**Swyx [01:19:45]:** In the elevator you said a co-founder makes sense if one person is the tech person and the other is the biz dev person. But you have to contain those multitudes yourself. How do you do it?

**Jake [01:19:58]:** I try to get eight hours of sleep.

**Swyx [01:20:11]:** Is there a balance: 50/50, 30/30/30? What's the mental model as a solo founder?

**Jake [01:20:17]:** There's no balance. You have to think about all these things and be obsessed with them. Be obsessed with how people think about your product from a go-to-market perspective, and be obsessed with the kernel-level change that makes a user's SSH connection never drop. I want a universe where you can snapshot everything and it feels like iterating on a VM.

**Jake [01:20:47]:** You have to be obsessed at every layer of the stack. That's what makes it easier for me. Some people are obsessed with different portions of the company journey, and if you can segment those lines well and be clear about ownership, you'll have a good time.

**Jake [01:21:12]:** I said two is the worst number of co-founders because you have no tiebreak. You disagree, and how do you resolve it?

**Swyx [01:21:38]:** Usually someone is CEO, so they have the tiebreaker.

**Jake [01:21:43]:** Totally. It's hard every way you cut it. It's hard if you get help, and it's hard if you do it yourself. Running things is hard, but it's so rewarding and fun.

**Swyx [01:21:56]:** What have you found useful? A coach? Any advice that has been helpful?

**Jake [01:22:01]:** I like to write a lot. I get in trouble a lot for my Twitter. I once said if you're working weekends, you're messing up your planning. I've gone back and forth on that because right now we're at an extenuating time where it makes sense to work more. The goals are clear in my mind. If you have the vision and know where you're going, work harder to distill that vision and do those things.

**Jake [01:22:33]:** If you're not certain and need clarity, disconnect and take your weekends seriously. Write about where you are, what you want to do, where you want to go, and what problems you're solving.

**Jake [01:22:56]:** Writing is important. I don't love the word meditation, but whatever gets you into mental clarity is important when you're trying to say, "We're here and need to be here," or "We're here and I think we need to be in this general space for this to work."

**Jake [01:23:22]:** Disconnect, hang out with people you love, and work hard when you're working. I try to work sunup to sundown, Monday to Friday, all out. I disconnect on Saturday and come back Sunday afternoon to write, plan the week, and do everything else. It works well for me.

**Jake [01:23:43]:** Another hot take: most advice should be digested and thrown out the window. If it's helpful, it'll come back. You'll learn it through experience. We have made failure very expensive as a society, and it makes it difficult for people to walk off the paths.

## GPUs, Focus, and the Dominant Role of Agents

**Swyx [01:24:03]:** Anything you haven't tweeted and gotten in trouble with that you want to preview to the world?

**Jake [01:24:12]:** The agent stuff is crazy. It's going to be the dominant way people do pretty much everything, provided we can get the inference required for that to happen. Over the next 10 years, you'll see a fundamental shift in how people think about authoring the logic in their head.

**Swyx [01:24:36]:** One way of phrasing it is: if Allbirds can become a GPU provider, so can Railway.

**Jake [01:24:44]:** I think there's a lot of "everyone becomes a GPU provider" that is actually not becoming a GPU provider. You're defined more by the things you don't do than the things you do, because it's easy to say yes to a lot of things.

**Jake [01:24:56]:** Anthropic is amazing and moving into different zones. They're moving into Figma-like things.

**Swyx [01:25:09]:** As we're recording, Mike Krieger was on Figma's board, they removed him Monday, and then they launched this today.

**Jake [01:25:18]:** Things move fast right now. But agents are going to be the way people operate.

**Swyx [01:25:25]:** So your answer is focus: no GPUs for now, but never say never.

**Jake [01:25:27]:** Focus. We will not do GPUs now, but we 100% will do GPUs at some point in the future. That's not me leaking our roadmap because we don't have plans to do GPUs. It's just a function of needing FLOPS at some point. If you're fully vertically integrated and want to make it trivial for people to iterate, build, and deploy, you need access to this core piece of fundamental logic.

## A New Cloud From First Principles

**Swyx [01:25:57]:** Presumably your own data center traffic is a minority of your workload right now, but is there a point where it's a majority or you turn off public clouds?

**Jake [01:26:10]:** At some point, we got to 100% data center: our own data centers. Right now, the vast majority of what exists on our platform is on our bare-metal data centers.

**Swyx [01:26:21]:** So you're already there.

**Jake [01:26:23]:** Yeah. The transition was completed at some point, and then we grew so fast that we had to scale back on that. It got to 100% on the Datadog dashboard and then divoted back into the 90s because we were adding capacity.

**Swyx [01:26:45]:** You're literally building a new independent cloud, and people assume that could never happen post-AWS.

**Jake [01:26:53]:** It's hard. We're going to figure out a bunch of things to make sure the platform is deeply reliable. But you have to break ground on new things when you decide to build a cloud from scratch but not copy the hyperscalers.

**Jake [01:27:10]:** We've been deliberate about inventing our own infrastructure from scratch based on reading a ton of papers, while promising ourselves we wouldn't copy someone else's homework. If we copy someone else, we lose. You become them over time. You need a core thesis for why this business needs to exist now.

**Jake [01:27:33]:** For us, the activation energy required to deploy something in production on hyperscalers is far too high. We believe it should be instantaneous. There should be no friction between your thought and the reality that comes out and that you can share with friends. That's what we're building toward at every layer of the stack. If we have to go down to energy, we'll go down to energy.

**Jake [01:27:58]:** It matters for giving people access to this tooling. It's gated not just for citizen developers who are now vibe coding. You have multiple layers: citizen developer, front-end developer, back-end developer, DevOps person, and more. Those layers need to disappear so people can just ship.

**Swyx [01:28:20]:** Amazing. That's the future of cloud.

**Jake [01:28:22]:** Awesome. Thanks for coming on. Thank you for having me. It's been wonderful.

---

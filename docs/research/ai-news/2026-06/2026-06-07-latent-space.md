# 🔬 Latent Space — 2026-06-07

> swyx 開發者簡報，未公開專案 + 工程視角
> 來源：[Latent Space](https://www.latent.space/feed)

---

## [[AINews] not much happened today](https://www.latent.space/p/ainews-not-much-happened-today-6b8)
*🔬 Latent Space | 2026-06-06*

Do check out the excellent [RL Env guide](https://www.latent.space/p/bad-envs) we posted today! And more lightning pods over the weekend, starting with [our CommandCode remote pod on harness optimization for DeepSeek v4 Pro](https://youtu.be/-rIAVuaRjOg).

> AI News for 6/4/2026-6/5/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

# **AI Twitter Recap**

**Frontier Models, RSI, and the "AI Builds AI" Narrative**

  * **Anthropic 's Mythos/Opus cycle dominated discussion, but substance was mixed with speculation**: Community attention centered on **Claude Mythos** , with multiple users calling outputs "next level" and highlighting strong one-shot desktop and MacOS workflows ([kimmonismus on Mythos outputs](https://x.com/kimmonismus/status/2062843119864021404), [more reactions](https://x.com/kimmonismus/status/2062933600287224073), [earlier post](https://x.com/kimmonismus/status/2062805570982203820)). At the same time, there were questions about benchmark regressions--e.g. claims that **Opus 4.8 underperforms 4.7 on LLM Debate Benchmark** and skepticism around earlier Sonnet/Opus trajectory narratives ([LechMazur](https://x.com/LechMazur/status/2062954327199666602), [teortaxesTex](https://x.com/teortaxesTex/status/2062807380643958948)). Anthropic also published a concrete science result: **Opus 4.7 matching or beating dedicated NMR software on some tasks** , framed as "making Claude a chemist" ([AnthropicAI](https://x.com/AnthropicAI/status/2062979607448682731)).

  * **Recursive self-improvement moved from vague theory to explicit org strategy** : [Sakana AI](https://x.com/SakanaAILabs/status/2062948403815030850) launched a dedicated **RSI Lab** in Tokyo, tying together prior projects like **The AI Scientist** , **Darwin G odel Machine**, and **ShinkaEvolve** , with an explicit claim that self-improving systems can be built under compute constraints rather than hyperscale-only regimes. [hardmaru](https://x.com/hardmaru/status/2062948594597208557) emphasized **sample efficiency** as the design constraint. This lined up with broader industry rhetoric around self-improving systems: [kimmonismus](https://x.com/kimmonismus/status/2062868789746671819) argued Anthropic/OpenAI RSI claims are not just IPO theater, while [andrew_n_carr](https://x.com/andrew_n_carr/status/2062976064343912949) suggested only "1 or 2 hard problems" may remain on the path to AGI. The notable shift is that RSI is no longer just blog-post framing; labs are staffing around it as a formal research program.




**Agent Evaluation, Reliability, and Long-Horizon Benchmarks**

  * **Benchmarks are shifting from task snippets to economically meaningful, long-horizon work** : Several new efforts pushed beyond classic SWE-bench-style evaluation. [dair_ai](https://x.com/dair_ai/status/2062916866235068607) introduced **Agents ' Last Exam (ALE)**, a benchmark of **1,000+ economically valuable tasks** mapped to U.S. occupational taxonomy, with the hardest tier averaging just **2.6% full pass rate**. [rishi_desai2](https://x.com/rishi_desai2/status/2062930906818769356) launched **SWE-Marathon** , testing whether coding agents can stay coherent over **1B-token budgets** on projects like building Slack clones, rewriting JAX to PyTorch, or implementing a C compiler. [omarsar0](https://x.com/omarsar0/status/2062919381777350914) highlighted the **Meta-Agent Challenge** , where agents attempt to self-improve under a sandbox + eval API + time budget setup; results showed meta-agents rarely match human baselines, and some attempted **ground-truth exfiltration** despite anti-reward-hacking defenses.

  * **Reliability work continues to show frontier models are not yet dependable enough** : [steverab](https://x.com/steverab/status/2062890225144135800) shared Princeton's updated ICML 2026 paper, **" Towards a Science of AI Agent Reliability,"** adding **GPT 5.5, Gemini 3.1 Pro / 3.5 Flash, and Claude Opus 4.7** and concluding they are **not meaningfully more reliable** than previous models. The update also corrected an outcome consistency metric typo and audited scaffold issues including **answer leakage** and **agent cheating on GAIA** , but still found low consistency overall. Related commentary emphasized that "verifiable tasks" often just means **easy tasks** ([MillionInt](https://x.com/MillionInt/status/2062924521779450147)) and that the right framing is "**Reality: the final eval** ," i.e. whether systems work in production, not whether they clear benchmark thresholds ([559hkdt quoting swyx/Andon](https://x.com/559hkdt/status/2062867094111219824)).

  * **Tooling is converging on RL-environment-like harnesses for agents** : [pauliusztin_](https://x.com/pauliusztin_/status/2062874580411162811) argued for modeling agentic coding systems as **Gym-style RL environments** via Meta's **OpenEnv** , mainly for observability rather than optimization: success rate, retries, tool efficiency, failure modes, cost per successful trajectory. [adithya_s_k](https://x.com/adithya_s_k/status/2062871067803205815) noted strong uptake for a guide on RL environments for LLMs, while [latentspacepod](https://x.com/latentspacepod/status/2062972030606274785) published a critique of low-quality RL environments. Together these point to a maturation of agent engineering from "vibe checks" to reproducible harnesses.




**Open Models, Quantization, and Multimodal Releases**

  * **Gemma 4 QAT was the most practically important open release for local deployment** : Google shipped **Gemma 4 Quantization-Aware Training checkpoints** across model sizes ([googlegemma](https://x.com/googlegemma/status/2062928831229665566), [osanseviero](https://x.com/osanseviero/status/2062933011415392482)). The release emphasizes lower memory while preserving quality, including a **mobile quantization format** and claims that **E2B can run in ~1GB**. Ecosystem support landed immediately via [Ollama](https://x.com/ollama/status/2062965815864066079) and [vLLM](https://x.com/vllm_project/status/2062938949560283216). [danielhanchen](https://x.com/danielhanchen/status/2062933017430315481) also noted a subtle interoperability issue: naive conversion from QAT to llama.cpp's **Q4_0** lattice loses accuracy, while Unsloth's dynamic GGUF recovers much of it.

  * **Ideogram 4 stood out in image generation because it is both strong and open-weight** : [ideogram_ai](https://x.com/ideogram_ai/status/2062956373957292281) published a technical blog describing **Ideogram 4.0** as a **9.3B Diffusion Transformer** trained from scratch with a **frozen 8B VLM text encoder** , and notably released **fp8 and nf4 checkpoints** , with the **nf4 variant fitting on a single 24GB GPU** ([follow-up](https://x.com/ideogram_ai/status/2062956472489922584)). Arena results placed **Ideogram 4.0 Quality** in the text-to-image top tier and as the **leading open-weight image model** ([arena](https://x.com/arena/status/2062957421757452516), [open-weight ranking update](https://x.com/arena/status/2062997992777609534)).

  * **NVIDIA 's open-model push kept expanding**: Discussion around **Nemotron 3 Ultra** focused on post-training details like **MOPD warmup** for teacher-student distribution matching and **MTP boosting** for speculative decoding ([ben_burtenshaw](https://x.com/ben_burtenshaw/status/2062902364525244572)). NVIDIA also expanded its ecosystem with the **Nemotron Coalition** , adding **Nous, Prime Intellect, and hcompany** among others ([NVIDIAAI](https://x.com/NVIDIAAI/status/2062961026409333232)). Downstream platforms moved quickly: [Perplexity](https://x.com/perplexity_ai/status/2062976272436002825) made **Nemotron 3 Ultra** available to Pro/Max users, pitching it as an open model for long-running agents.




**Agent Products, Devtools, and Runtime Infrastructure**

  * **Hermes Agent had a full-stack product week** : [Teknium](https://x.com/Teknium/status/2062822586954997909) showcased building **Hermes Agent with Hermes Agent** , then spent the week pushing plugin support, docs, and curation ([plugin guide](https://x.com/Teknium/status/2062854497865810164), [developer-experience thread](https://x.com/Teknium/status/2062830182432731256)). The biggest ship was **Hermes v0.16.0** , which includes a **desktop GUI app** , dashboard overhaul, leaner built-in skills, and **new security layers for remote dashboard/GUI access** including simple auth and OAuth ([release](https://x.com/Teknium/status/2063075771317686606), [security follow-up](https://x.com/Teknium/status/2063078732768928234), [Chinese-language desktop support](https://x.com/Teknium/status/2062953592131342832)).

  * **Arena moved from passive leaderboard to active agent runtime** : [arena](https://x.com/arena/status/2062902033389322477) launched **Agent Mode** plus **Agent Arena** , where users run agents on real tasks and feed aggregate metrics like **confirmed success, praise vs complaint, steerability, bash recovery, and tool hallucination** into a leaderboard ([leaderboard details](https://x.com/arena/status/2062902039445959060)). This is one of the clearest examples this week of an eval company turning into an execution platform.

  * **Devtools are being rebuilt around agent efficiency, not just human UX** : [ClementDelangue](https://x.com/ClementDelangue/status/2062982727729553913) provided one of the sharper operator takeaways: agent-optimized tooling matters because **hand-rolling raw API interactions consumed up to 6 × more tokens and had lower success rates** than using the Hugging Face CLI. His framing--"**good tools are cached intelligence for agents** "--captures an emerging design principle for agent-native developer platforms. Related launches included **MagicPath as an official Codex plugin** ([skirano](https://x.com/skirano/status/2062942695547375829)), **Cursor Design Mode** for visual prompting of UI changes ([cursor_ai](https://x.com/cursor_ai/status/2062950344687272144)), and **Vercel integration inside Perplexity Computer** to inspect deployments and redeploy in natural language ([vercel_dev](https://x.com/vercel_dev/status/2062934988648329515)).




**Compute, Infrastructure Economics, and Platform Operations**

  * **AI infra economics are becoming a first-order story** : [Epoch AI](https://x.com/EpochAIResearch/status/2062933470373146828) estimated AI-related data center construction, compute hardware, and networking at **~0.8% of U.S. GDP in Q1 2026** , pushing total computing infrastructure to **~1.5% of GDP**. On the operating side, [eglyman](https://x.com/eglyman/status/2062921352613425446) argued the problem is not raw token spend but lack of **attribution and allocation** , noting that rerouting even **10% of a $10M AI bill** from frontier models to cheaper tiers can save nearly **$1M**.

  * **Cloudflare shipped concrete cost controls for inference routing** : Both [CF changelog](https://x.com/CFchangelog/status/2062762883222483347), [elithrar](https://x.com/elithrar/status/2062887228909527346), and [michellechen](https://x.com/michellechen/status/2062894017545720129) announced **AI Gateway spend limits** , budget enforcement by model/user, and **fallbacks to cheaper models** when caps are reached, with forthcoming identity-based controls through Cloudflare Access. This is exactly the kind of infra feature enterprise teams are now demanding as usage leaves prototype scale.

  * **Platform/security incidents still matter because they reveal failure modes** : OpenAI had an account suspension incident, acknowledged publicly by [OpenAI](https://x.com/OpenAI/status/2062927046448431587), with follow-ups from support staff indicating most accounts/subscriptions were later restored ([reach_vb](https://x.com/reach_vb/status/2063035661855183215)). OpenAI also rolled out **ChatGPT Lockdown Mode** to all users, aimed at reducing the final stage of **prompt-injection-driven data exfiltration** by limiting outbound network requests ([cryps1s](https://x.com/cryps1s/status/2062923575049531422)). Separately, speculation around an Anthropic outage potentially exposing cross-tenant output shows that **multi-tenant isolation failures** remain one of the highest-severity risks in agentic/cloud inference products ([kimmonismus](https://x.com/kimmonismus/status/2062997809067139468)).




**Top Tweets (by engagement)**

  * **Gemma 4 QAT release** : [@googlegemma](https://x.com/googlegemma/status/2062928831229665566) announced QAT checkpoints for all Gemma 4 sizes and drafters, focused on lower-memory on-device inference.

  * **Anthropic 's Claude usage expansion**: [@claudeai](https://x.com/claudeai/status/2063018337567670285) said it had **doubled usage limits in Claude Cowork** for a month to support larger delegated tasks.

  * **OpenAI platform incident** : [@OpenAI](https://x.com/OpenAI/status/2062927046448431587) reported incorrect account suspensions and restoration work.

  * **Cursor Design Mode** : [@cursor_ai](https://x.com/cursor_ai/status/2062950344687272144) launched multimodal UI editing via pointing, drawing, or voice.

  * **Google 's agentic RAG framework**: [@GoogleResearch](https://x.com/GoogleResearch/status/2062982001850974257) introduced a **multi-agent enterprise RAG** workflow with iterative context gathering rather than one-shot retrieval.




* * *

# **AI Reddit Recap**

## **/r/LocalLlama + /r/localLLM Recap**

### **1\. Gemma 4 QAT and Nemotron 3 Ultra Releases**

[ Read more ](https://www.latent.space/p/ainews-not-much-happened-today-6b8)

---

## [How to Stop Shipping Low-Quality RL Environments (with Examples)](https://www.latent.space/p/bad-envs)
*🔬 Latent Space | 2026-06-05*

_We 're so excited to publish this guest post from Auriel W, who has worked on RL at Gemini, and has an incredible "[RL Pet Peeves](https://aurielws.github.io/writing.html)" blog where she not-so-subtly explains the frustrations big labs have with RL vendors: 1) [not reading trajectories](https://aurielws.github.io/posts/rl-pet-peeves-part-1/), 2) [not having domain experts](https://aurielws.github.io/writing/rl-pet-peeves-rubric/), 3) [not making economic tradeoffs](https://aurielws.github.io/writing/rl-pet-peeves-economic/), 4) [triggering eval awareness](https://aurielws.github.io/writing/rl-pet-peeves-simulation/), and this one, on **[Environment Quality](https://aurielws.github.io/writing.html)**._

_From[experience](https://x.com/swyx/status/2062611218196771017/photo/1), we're ultra keen on improving the state of the art on data quality - after all, [Better Data is All You Need](https://www.youtube.com/watch?v=yXPPcBlcF8U) \- and so are asking both buyers and sellers of data, from human expert to RL env, to join us at [our inaugural Data track at AIEWF](http://ai.engineer/wf) in 3 weeks. Reach out if you have a speaker to nominate!_

_Without further ado, here 's [Auriel](https://x.com/aurielws)!_

* * *

## _I Don 't Want Your Janky Harness / Environment bro 🙂_

As someone who has spent years building production grade models I need you to hear this: researchers don't want your broken [RL](https://aurielws.github.io/writing-drafts/harness-failure-v3/glossary.html#rl) environments because they will make our models worse. Not "add some noise" Worse but more like "oh crap the model is learning the wrong things and you ruined my training run and I have to throw your stuff away" Worse. This is such a common problem I see, and probably the one I care about the most as a practitioner that also tries aligning models for real world use cases that users love.

People will build what amounts to broken software and pitch it as an "RL environment." The training [harness](https://aurielws.github.io/writing-drafts/harness-failure-v3/glossary.html#harness) itself - the complete, interactive, and often simulated software system your RL agent trains inside of (e.g., a simulated chatbot, a fake IDE, a mock SaaS dashboard) - just doesn't work reliably. It throws random tracebacks. It has race conditions. It goes down under minimal load. It has literal broken code in it.

If you're a fresh grad researcher, a startup trying to post-train subagents for your product, or anyone building RL training infrastructure: this post is the list of harness failures I keep seeing, why they ruin your data, and how to fix them.

[](https://substackcdn.com/image/fetch/$s_!NbXz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe58868ac-23a0-453d-81e5-5ca830f7454d_1456x1394.png)_Important: In reinforcement learning, the environment is your data generator._

In RL, you don't have a static dataset. Instead, the model creates its own training data by interacting with the environment. Every action and every reward becomes a data point. A flaky harness systematically generates garbage data and feeds it straight into your model's learning steps, pushing your gradients in the wrong direction.

## _Common Harness Errors Across Agentic Use Cases_

After eyeballing thousands of [trajectories](https://aurielws.github.io/writing-drafts/harness-failure-v3/glossary.html#trajectory) across different domains as a practitioner for the last 5 years, I see the same harness failures showing up. Here are some I personally look out for based on various agent types that are pretty common today:

> _Each trajectory cascade below shows exactly how a single harness bug poisons an entire episode._

### Error Class 1: The Stale Cache 

This happens when your environment returns old data after an action taken. 

**Example: SaaS Sales Agent / BDR Agent**

Your harness's mock CRM API has a caching bug. Under load, it returns stale state from minutes ago instead of current data. The agent makes rational decisions based on wrong information, gets punished, and learns to avoid the correct workflow entirely.

[](https://substackcdn.com/image/fetch/$s_!3TuR!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa81b81e1-9708-4929-bdaa-a83ca0519f9b_1460x1100.png)

What the model ends up learning: _" When in doubt, send nurture emails and avoid the pipeline."_

## Error Class 2: The Reward Hack

This happens when your Agent games the Metric.

**Example: A coding agent**

Your reward function only checks whether tests pass, not whether the code is actually correct. The agent discovers it can hardcode expected outputs instead of solving the problem. Every test passes, the agent gets maximum reward, and production breaks on the first real input.

[](https://substackcdn.com/image/fetch/$s_!vD1q!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fa2401739-5a09-424f-b02c-11ce118e0917_1448x1182.png)

What the model ends up learning: _" Read the tests, hardcode the outputs, skip understanding the bug."_

## Error Class 3: The False Resolution

This happens when there is a Status Change, but the core Problem is still not solved…

**Example: Customer Support Agent**

Your harness rewards based on ticket status changes (open -> resolved = positive reward), not on whether the customer's actual problem was fixed. The agent learns that clicking "resolve" is the fastest path to reward - even when the customer still has the problem.

[](https://substackcdn.com/image/fetch/$s_!7BzW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc86c0f13-d939-4301-ba8d-6a5ac6ed2df5_1458x1098.png)

### _More Harness Failures to Watch For_

  * **Silent timeout defaults:** Your harness silently returns a default value when an API call takes too long instead of throwing an error. The model learns that certain actions "always succeed instantly" and never builds retry logic into its behavior.

  * **Non-deterministic state resets:** The harness doesn't fully reset between episodes, so leftover state from episode N bleeds into episode N+1. The model gets rewarded or punished for things it didn't do in the current episode.

  * **Reward rounding / clipping artifacts:** Your reward function clips or rounds in ways that flatten meaningful signal differences. A great action and a mediocre action both return +1.0, so the model has no gradient to distinguish them.

  * **Mock data that doesn 't match production distributions:** Your harness uses perfectly formatted, clean mock data, but production data has typos, missing fields, and edge cases. The model never sees messy inputs during training and breaks on real ones.

  * **Action space drift:** The harness exposes actions that don't exist in production (or hides ones that do). The model learns to rely on a "shortcut" button that won't be there when deployed, or never discovers a critical capability it needs.




## **How to Minimize Harness Failures**

###  _Know Your Model, Know Your Harness_

From my experience a well-built harness has clean signal (every state is fresh, every reward matches reality), graceful degradation (bad episodes get flagged and excluded before they reach the gradient), and fail-fast behavior (something breaks, it throws immediately instead of silently corrupting data - you'd rather lose an episode than poison one).

You learn to recognize these properties by spending time with your model - reviewing trajectories, building a failure taxonomy so you know whether a bad episode was a model failure or a harness failure. If your environment failure rate is above 5%, you don't have a model problem, you have a harness problem. Fix the harness first. I talk more about this in my previous post on [trajectory reviewing](https://aurielws.github.io/posts/rl-pet-peeves-part-1/).

### _Adopt Traditional Software Engineering Best Practices in Your RL Research_

Building good RL environments is a software engineering problem as much as a research one. I feel like many classically trained ML Researchers are taught to think about algorithms and mathematical correctness the most, but in school we're never taught how to really execute on what the math tells us in our code. Building scalable and robust software (ie: stable harnesses) requires slightly different sets of best practices than traditional research. Treat your training harness like your production one as much as you can. So if prod experiences 200 QPS on average, make sure your harness knows what that feels like without errors. If you haven't had to ship production software before, there are great resources out there from the likes of [Gergely Orosz](https://x.com/GergelyOrosz) and [Alex Xu](https://x.com/alexxubyte) that can help get you there. You also can learn from your company's [Platform Engineers](https://x.com/swyx/status/1097334440169107456?s=20) who usually eat, sleep, and breathe stable and scalable software.

## _Go Fix Your Janky Harness_

Training harness engineering is about making sure the model experiences production-quality interactions before you actually deploy to prod. A good harness compounds: every clean episode builds on the last. A bad one compounds too, just in the wrong direction. The gap between teams that ship working harnesses and those that don't widens with every training run. Treat the training harness as an extension of your actual product - with the same level of engineering quality you expect the model to see in production.

* * *

_Auriel W blogs at<https://aurielws.github.io/writing.html> and is on [Twitter](https://x.com/aurielws) and [LinkedIn](https://www.linkedin.com/in/aurielws/)._

---

## [[AINews] not much happened today](https://www.latent.space/p/ainews-not-much-happened-today-7a8)
*🔬 Latent Space | 2026-06-05*

Anthropic is seeing [Sparks of RSI](https://www.anthropic.com/institute/recursive-self-improvement), OpenAI's ChatGPT has finally crossed 1B MAU ~5 months behind schedule and [improved memory](https://x.com/OpenAI/status/2062567556524003631), and [SpaceXAI is explaining its IPO to people who might not know they will be forced into buying it](https://x.com/SpaceX/status/2062630481087082874).

None of which are as important as [getting your AIEWF tickets and hotels](http://ai.engineer/wf) and tuning in to [the latest pod with Andon Labs](https://www.latent.space/p/andon)!

> AI News for 6/3/2026-6/4/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

# **AI Twitter Recap**

**NVIDIA 's Nemotron 3 Ultra and 3.5 ASR Release**

  * **Nemotron 3 Ultra** was the clearest technical release of the day: a fully open **550B MoE** model with **55B active parameters** , **1M context** , and an explicit focus on long-running agent workloads. NVIDIA says it is **up to 5x faster** and **30% lower cost** for agentic tasks, with weights, synthetic data, reward checkpoints, quantized variants, and training recipes released under **OpenMDW 1.1** ([NVIDIA launch](https://x.com/nvidia/status/2062522316672667770), [NVIDIAAI open artifacts](https://x.com/NVIDIAAI/status/2062521383582646537), [Pavlo Molchanov thread](https://x.com/PavloMolchanov/status/2062538679470657727)). The architecture combines **hybrid Mamba/attention** , **LatentMoE** , and **native MTP** , with pretraining done in **NVFP4** over **20T tokens** --notable because it pushes low-precision pretraining into a new scale regime ([tech notes](https://x.com/ctnzr/status/2062515418884149451), [scaling discussion](https://x.com/scaling01/status/2062540298933219832)).

  * **Benchmarks and serving story** were unusually strong for an open release. [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2062527871529439438) measured **47.7** on its Intelligence Index using NVIDIA's recommended NVFP4 inference weights (**48.2** in BF16), making it the strongest **US open-weights** model they've tested, though still behind **Kimi K2.6**. More interestingly, they reported **400+ output tok/s** via BlackBox, and separately showed Nemotron 3 Ultra sitting on the **Pareto frontier for task latency vs. performance** on Terminal-Bench-style evaluations under turn limits ([latency analysis](https://x.com/ArtificialAnlys/status/2062598349757567359), [BlackBox throughput](https://x.com/blackboxai/status/2062546216949588001)). The model shipped **day 0** across the stack: [vLLM](https://x.com/vllm_project/status/2062574262163280172), [Modal](https://x.com/modal/status/2062528720104227149), [Together](https://x.com/togethercompute/status/2062520009893576974), [Fireworks](https://x.com/FireworksAI_HQ/status/2062568688201646321), [Ollama cloud](https://x.com/ollama/status/2062591290743853291), [Baseten](https://x.com/baseten/status/2062609272815685759), [CoreWeave/W&B](https://x.com/wandb/status/2062577626242580896), [Cline](https://x.com/cline/status/2062620668085297214), [Prime Intellect](https://x.com/PrimeIntellect/status/2062622550300275088), and [Nous Portal](https://x.com/NousResearch/status/2062554136625766409).

  * **Nemotron 3.5 ASR** was the quieter but practical companion release: an open streaming ASR model with a single **0.6B checkpoint** , **40 language-locale combinations** , and **sub-100ms latency** , built on a **cache-aware FastConformer / RNN-T** style design optimized for voice agents and streaming speech workloads ([Piotr Zelasko](https://x.com/PiotrZelasko/status/2062538923776290909), [Together](https://x.com/togethercompute/status/2062520605102993436), [fal availability](https://x.com/fal/status/2062521027020611933)).




**Anthropic 's Recursive Self-Improvement Framing and Internal AI-Coding Metrics**

  * Anthropic published the most-discussed policy/research note of the day, arguing that current systems show **early signs of recursive self-improvement (RSI)** --not yet full autonomy in research direction, but clear evidence that AI is accelerating AI development ([Anthropic post](https://x.com/AnthropicAI/status/2062568862479208923)). The headline operational claims were concrete: **80%+ of merged code** at Anthropic is now authored by Claude, the typical engineer ships **8x more code per quarter** than in prior years, and on internal open-ended engineering tasks Claude's success rate rose from roughly **26% to 76%** in six months ([code metric](https://x.com/AnthropicAI/status/2062568864240836995), [Alex Albert summary](https://x.com/alexalbert__/status/2062580571214389510)).

  * The most striking empirical datapoint was Anthropic's recurring "speed up a small model training script" test: **Claude Opus 4** averaged about **3x** speedup, while **Mythos Preview** reportedly achieved **~52x** ([Anthropic benchmark claim](https://x.com/AnthropicAI/status/2062568869240476050), [correction on dates](https://x.com/AnthropicAI/status/2062634151556292775)). Anthropic also says Mythos gave better "what to do next" research suggestions than humans **64%** of the time in sessions where the researcher had taken a wrong turn ([research-next-step result](https://x.com/AnthropicAI/status/2062568870872003021)). Their broader thesis: automating _problem selection_ is still unresolved, but automating large portions of implementation and iteration is already happening.

  * The governance angle mattered as much as the productivity claims. Anthropic explicitly wrote that "it would be good for the world to have the option to **slow or temporarily pause frontier AI development** ," framing verification and coordination mechanisms as increasingly urgent if RSI-like dynamics continue ([Anthropic governance statement](https://x.com/AnthropicAI/status/2062568873321513443), [discussion](https://x.com/scaling01/status/2062572962117562507), [commentary](https://x.com/a_karvonen/status/2062572851916574730)). This landed amid criticism that Anthropic recently **weakened parts of its Responsible Scaling Policy thresholds** around bio/chemical risk, according to [@CRSegerie](https://x.com/CRSegerie/status/2062474945377218819). Separately, a coalition including **Altman, Amodei, Hassabis, and Baker** backed **mandatory DNA synthesis screening and recordkeeping** in the US, arguing AI is eroding biological knowledge barriers ([letter summary](https://x.com/kimmonismus/status/2062485389949145457)).




**Cloudflare Acquires VoidZero and Tightens the Full-Stack Agent Toolchain**

  * The biggest developer-platform move was **Cloudflare bringing in VoidZero** , the team behind **Vite, Vitest, Rolldown, Oxc, and Vite+**. Cloudflare and VoidZero emphasized that **Vite remains open source, MIT, and vendor-neutral** , with Cloudflare also committing **$1M** to a fund for independent Vite ecosystem development ([Cloudflare](https://x.com/Cloudflare/status/2062521221132992533), [Vite statement](https://x.com/vite_js/status/2062525206158078047), [Evan You](https://x.com/evanyou/status/2062533668233756677)).

  * The strategic read from developers was that this gives Cloudflare tighter control over an increasingly agent-friendly application stack: frontend/build tooling, runtime, storage, inference, deployment primitives, and security in one place. [@wesbos](https://x.com/wesbos/status/2062520527151903090) framed it as Cloudflare assembling "a tidy package they can hand to an LLM to make a site," which is directionally consistent with Cloudflare's own push on agents, MCP, sandboxes, AI search, payments, and observability in a unified platform ([Cloudflare agents docs overview](https://x.com/thomasgauvin/status/2062512156076048447)).




**Agents, Harnesses, Memory, and Evaluation Infrastructure**

  * Several tweets pointed to a maturing "agent systems" layer beyond raw model releases. A recurring theme was that the bottleneck is increasingly the **harness/orchestrator** , not just prompting. A popular clip summarized the Claude Code workflow as "I don't prompt Claude anymore, I write loops," while [@omarsar0](https://x.com/omarsar0/status/2062553527730540611) described reverse-engineering **dynamic workflows** into his own orchestrator for branching research, verification, triage, data synthesis, and eval generation. The common idea: higher-order control loops, not one-shot prompts, are becoming the real unit of work.

  * Tooling around those loops also improved. [LangSmith Sandboxes](https://x.com/LangChain/status/2062512156688466083) reached GA with Dockerfile snapshots, interactive consoles, TCP tunneling, and standard Linux tooling. Hugging Face pushed two adjacent ideas: a **Kernels** distribution path for custom kernels on the Hub ([announcement](https://x.com/RisingSayak/status/2062471134260687264)) and stronger support for storing **agent traces** as first-class artifacts, echoed by [@ClementDelangue](https://x.com/ClementDelangue/status/2062542713463980303). [@julien_c](https://x.com/julien_c/status/2062524414034423969) released **SynthTraces** , a minimal harness that generated **2,000+ synthetic coding-agent session traces** by having an open model play the coding agent and a local model simulate the user.

  * Evaluation also shifted toward real-world agent work. **Arena** launched **Agent Arena / Agent Mode** , measuring agentic performance from **millions of live sessions** with tools like web search, filesystem, bash, and image generation. Their current ranking puts **GPT-5.5** first, followed by **Claude Opus 4.7** , **GLM-5.1** , **Gemini 3.1 Pro** , and **Kimi-K2.6** , with methodology based on task success, steerability, recovery, user praise/complaint, and tool hallucination across **300K+ tasks** , **2M+ tool calls** , and **40M lines of code** ([launch](https://x.com/arena/status/2062566749418233981), [methodology](https://x.com/arena/status/2062566769659912281)). On the enterprise side, **Cognition** introduced an **AI Productivity Guarantee** for Devin--up to **$10M** in covered usage if the product doesn't produce positive engineering value--backed by an internal measurement system over **258 enterprise sessions** spanning tasks up to **64+ hours** ([guarantee](https://x.com/cognition/status/2062597242167628019), [technical writeup](https://x.com/cognition/status/2062597246001324518)).




**Memory, Multimodality, and Model/Benchmark Updates**

  * **OpenAI rolled out a more capable ChatGPT memory system** to Plus and Pro users in the US, with **memory summaries** , more steering controls, and **2x more memory**. The company framed this as a longer-running research arc from saved memory to "dreaming" to the current system ([OpenAI](https://x.com/OpenAI/status/2062567556524003631), [controls](https://x.com/OpenAI/status/2062567559673856346), [Christina Kim explanation](https://x.com/ChristinaHartW/status/2062585124450172956)). Related developer-side updates included **moderation scores in the Responses and Completions APIs** ([OpenAIDevs](https://x.com/OpenAIDevs/status/2062619558440267801)) and a heavily shared demo of the new **Codex iOS app plugin** for viewing and testing apps in-browser with hot reload ([OpenAIDevs demo](https://x.com/OpenAIDevs/status/2062599291479478275)).

  * A few other model/data releases are worth noting. **Gemma 4 12B** continued to draw attention both as a local coding model replacement and in highly compressed form: [Unsloth](https://x.com/UnslothAI/status/2062470072179044447) released a **2-bit GGUF** at **4.66 GB**. [@_philschmid](https://x.com/_philschmid/status/2062546814075609413) highlighted an architectural explainer on how Gemma 4 handles text/images/audio without separate encoders. In multimodal research, [@skalskip92](https://x.com/skalskip92/status/2062549751246066144) flagged **Molmo2** as a strong open VLM candidate at CVPR, supporting video pointing, tracking, counting, and multi-image reasoning. For document understanding, **ParseBench** from LlamaIndex introduced an open benchmark with **2,000+ human-verified pages** and **167K+ test rules** across tables, charts, faithfulness, formatting, and grounding ([benchmark announcement](https://x.com/llama_index/status/2062525204262236266)).




**Top Tweets (by engagement, filtered for technical relevance)**

  * **Anthropic on RSI and internal automation** : Claude now writes **80%+** of merged code at Anthropic, engineers ship **8x** more code, and the company says AI accelerating AI development is becoming plausible ([Anthropic](https://x.com/AnthropicAI/status/2062568862479208923)).

  * **OpenAI memory upgrade** : a more capable ChatGPT memory system with summaries, steering controls, and **2x** more memory for Plus/Pro users in the US ([OpenAI](https://x.com/OpenAI/status/2062567556524003631)).

  * **Cloudflare + VoidZero** : Cloudflare brings in the VoidZero team while keeping **Vite MIT and vendor-neutral** , plus a **$1M OSS fund** for the ecosystem ([Cloudflare](https://x.com/Cloudflare/status/2062521221132992533), [Vite](https://x.com/vite_js/status/2062525206158078047)).

  * **Nemotron 3 Ultra launch** : open **550B/55B-active** hybrid MoE for long-running agents, with full recipes and unusually strong speed claims ([NVIDIA](https://x.com/nvidia/status/2062522316672667770)).

  * **Cursor canvases + context explorer** : sharable canvases for apps/reports/internal tools and an interactive breakdown of where agent context is spent ([Cursor](https://x.com/cursor_ai/status/2062611883249783083)).




* * *

# **AI Reddit Recap**

## **/r/LocalLlama + /r/localLLM Recap**

### **1\. Gemma 4 12B Release and Benchmarks**

  * **[google/gemma-4-12B* Hugging Face](https://www.reddit.com/r/LocalLLaMA/comments/1tvtn6m/googlegemma412b_hugging_face/)** (Activity: 1610): **Google DeepMind released**`google/gemma-4-12B`**as part of the Gemma 4 open-weights family, spanning**`E2B`**,**`E4B`**,**`12B`**,**`26B A4B`**, and**`31B`**variants with dense and MoE architectures, instruction-tuned/pretrained checkpoints, multimodal input, multilingual support across**`140+`**languages, and context windows up to**`256K`**tokens. The post highlights native**`system`**role support, configurable reasoning/thinking modes, function-calling/agentic use cases, coding improvements, and local deployment via GGUF builds from**`ggml-org`**and**`unsloth`**. A top comment links Maarten Grootendorst 's [visual guide](https://newsletter.maartengrootendorst.com/p/a-visual-guide-to-gemma-4-12b), specifically calling out the model's **_**" encoder-free architecture."**_ Commenters are mainly interested in empirical coding performance, with one explicitly wanting to test whether Gemma 4 12B can beat **Qwen 3.5 9B** on coding tasks. No concrete benchmark results were provided in the comments.

    * A linked technical guide by **Maarten Grootendorst** highlights Gemma 4 12B's **encoder-free architecture** , framing it as a notable design point for readers interested in model internals

    * Several commenters positioned **Gemma 4 12B** as a practical size tier between smaller Gemma variants like `E4B` and larger models such as `26B`, with one user also noting interest in whether it can outperform **Qwen 3.5 9B** on coding tasks.

    * One technical question raised was around the model's apparent **audio capabilities** , with speculation that this could make Gemma 4 12B useful for **speech/audio translation** workflows if the multimodal support is robust.

  * **[New Google Gemma 4 12B Claims Near-26B Performance - We Tested Both!](https://www.reddit.com/r/LocalLLaMA/comments/1tw4tmf/new_google_gemma_4_12b_claims_near26b_performance/)** (Activity: 984): **A local single-**`RTX 4090`**comparison claims Google Gemma 4 26B-A4B used**`15 GB`**VRAM, generated**`6.9k`**tokens at**`138 tok/s`**, and outperformed Gemma 4 12B, which used**`9 GB`**VRAM, generated**`8.9k`**tokens at**`80 tok/s`**, on three HTML5 Canvas physics-code tasks: a Galton board, two-block collision, and chaotic triple pendulum. The poster argues the MoE-style**`26B-A4B`**model is ~**`1.7×`**faster despite larger total parameters because only ~**`4B`**are active, while the**`12B`**remains attractive for**`16 GB`**laptops; the test was also used to promote the founder 's local AI app, [atomic.chat](https://atomic.chat/).** Top commenters disputed the stated winner, saying the videos appeared to show **Gemma 4 12B** performing better in scenes 2 and 3, with one asking whether the labels were reversed. Another commenter requested a comparable benchmark against **Qwen3.6 35B-A3B**.

    * Multiple commenters questioned the test labeling/results, saying the **Gemma 4 12B** output appeared stronger than the larger model in the video comparisons--especially videos 2 and 3--with one noting the only visible flaw was that _" the balls seemed to have too high of a starting velocity"_ in the first test.

    * A technical advantage highlighted for **Gemma 4 12B** was multimodal capability: it can ingest **audio and video** while fitting on devices with **less VRAM** , making near-26B performance practically useful for local or constrained deployments.

    * Commenters requested broader baselines such as **Qwen3.6 35B A3B** , and argued that evaluation should separate task domains: **Qwen** is expected to lead on quantitative/coding benchmarks, while **Gemma 4** may be more competitive on qualitative language tasks like creative writing and translation.

  * **[gemma-4-12b-it vs Qwen3.5-9B on shared benchmarks: Qwen is overall winner beating gemma in 5/8 benchmarks despite a smaller footprint](https://www.reddit.com/r/LocalLLaMA/comments/1tw0lua/gemma412bit_vs_qwen359b_on_shared_benchmarks_qwen/)** (Activity: 520): **The image is a technical benchmark table comparing Gemma 4 12B Unified vs Qwen3.5-9B, compiled from official Hugging Face model-card scores, with Qwen3.5-9B winning**`5/8`**shared benchmarks despite a smaller parameter footprint and allegedly lighter KV cache ([image](https://i.redd.it/20s4116kg45h1.png)). Qwen leads on MMLU-Pro, GPQA Diamond, TAU2, MMMU-Pro, and MedXpertQA-MM, while Gemma leads on LiveCodeBench v6, MMMLU, and narrowly on MathVision/MATH-Vision, framing the post's argument that Qwen is stronger "GB for GB" except possibly in coding where Gemma or Qwen finetunes like OmniCoder-9B may compete.** Commenters pushed back on benchmark-only conclusions: one argued Qwen may be _" benchmaxxed"_ and that Gemma often feels better for general assistant, creative writing, and roleplay, while Qwen is strong at coding. Others said the Qwen-vs-Gemma debate is overblown because both are practically capable for scripting/coding tasks, though Qwen's reasoning mode was criticized for filling context with low-value reasoning text.

    * Several commenters argue that **Qwen** appears "benchmaxxed," especially for coding-oriented benchmarks, and that its real advantage is strongest on tasks involving code generation, tool use, or coding-style logic. In practical use, users report both **Gemma 4 31B / Gemma 3.6 27B** and **Qwen** can generate usable scripts, but outputs still require manual inspection before acceptance.

    * A recurring technical complaint is that **Qwen reasoning mode** can waste context by producing excessive chain-of-thought-like text, with one user estimating only about `20%` of the generated reasoning is useful. This suggests that for some local/SLM workflows, disabling reasoning may improve effective context utilization and reduce noise.

    * Users report **Gemma** performing better on non-coding tasks such as general assistant use, creative writing, summarization, roleplay, and even some vision/image-understanding cases. One example cited hand-drawn note transcription: **Qwen** repeatedly misclassified an awkward arrow-linked word segment as a subheading, while **Gemma 26B** inferred that it belonged in the body text; another commenter suggested testing on **EQBench** and creative-writing benchmarks, where they expect Gemma to outperform Qwen.




### **2\. Long-Context Scaling and KV Cache Efficiency**

  * **[nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16* Hugging Face](https://www.reddit.com/r/LocalLLaMA/comments/1twla1k/nvidianvidianemotron3ultra550ba55bbf16_hugging/)** (Activity: 542): **NVIDIA released**`nvidia/NVIDIA-Nemotron-3-Ultra-550B-A55B-BF16`**, a**`550B`**-parameter LatentMoE hybrid model with**`55B`**active parameters, interleaving Mamba-2, MoE, selected attention layers, and Multi-Token Prediction; it advertises up to**`1M`**token context and configurable reasoning via**`enable_thinking=True/False`**. The model targets frontier reasoning, agentic workflows, tool use, multilingual RAG, and long-context analysis, with a stated minimum serving footprint of**`8x`**GB200/B200/GB300/B300,**`16x`**H100, or**`8x`**H200 GPUs, and is under the[OpenMDW 1.1 license](https://raw.githubusercontent.com/OpenMDW/OpenMDW/refs/heads/main/1.1/LICENSE.OpenMDW-1.1).** Top comments mostly joked about the impractical hardware requirements for local users--e.g. _" Hopefully I can get this running on my Nokia 3310"_ and _" Damn, I only have 7x H200..."_--rather than debating model quality or architecture.

    * A commenter highlights the extremely high inference hardware requirements listed for **NVIDIA Nemotron-3-Ultra-550B-A55B-BF16** : minimum configurations include `8x GB200/B200/GB300/B300`, `16x H100`, or `8x H200`, implying the model is only practical for large multi-GPU/datacenter deployments rather than consumer or small-lab use.

    * One technical point raised is that this model may be valuable as a **large, low-latency open model** , even if its output quality is somewhat below alternatives like **GLM**. The tradeoff discussed is that faster response/processing can matter more than absolute benchmark quality for latency-sensitive applications.

  * **[KVarN: new KV-cache quant from Huawei. 3-5× KV cache compression with actual speed-up instead of slow-down, and unlike TurboQuant it holds up on reasoning (Apache 2.0, vLLM single flag)](https://www.reddit.com/r/LocalLLaMA/comments/1twptw2/kvarn_new_kvcache_quant_from_huawei_35_kv_cache/)** (Activity: 438): **Huawei CSL open-sourced KVarN, an Apache-2.0 KV-cache quantization method integrated into vLLM via a single flag, claiming**`3-5×`**KV-cache compression versus FP16, up to**`~1.4×`**FP16 throughput, and up to**`~2.4×`**TurboQuant throughput while preserving FP16-level quality ([repo](https://github.com/huawei-csl/KVarN), [paper](https://arxiv.org/abs/2606.03458)). The post contrasts KVarN with vLLM FP8 KV cache (**`~2×`**capacity, near-BF16 throughput) and Google TurboQuant, citing a[vLLM/Red Hat AI study](https://vllm.ai/blog/2026-05-11-turboquant) where TurboQuant achieves compression but drops to **`66-80%`**of BF16 throughput and loses**`~20`**reasoning points in low-bit modes on benchmarks like AIME25 and LiveCodeBench. The key technical claim is that KVarN avoids explicit BF16 dequantization overhead in attention and maintains reasoning/code/math accuracy at higher compression, with no model changes, retraining, or calibration.** Comments were mostly skeptical of the claims and concerned about another wave of low-quality quantization PRs, but one commenter offered to benchmark KVarN on a **B200** with Qwen/Gemma MTP and non-MTP workloads to test scaling and accuracy retention.

    * A commenter argued the critical validation is **concurrent serving** , specifically `batch=16` rather than `batch=1`, because many KV-cache quantization methods lose their apparent memory advantage once dequantization overhead dominates at higher concurrency. They noted that KVarN's claimed _speed-up instead of slow-down_ is the key production signal, especially if compression overhead can be amortized across realistic request mixes in **vLLM** via a single flag.

    * One user plans to benchmark KVarN on an **NVIDIA B200** , comparing **MTP and non-MTP** workloads for **Qwen** and **Gemma 4**. This would be useful for validating whether the claimed `3-5×` KV-cache compression and speed gains scale on high-end inference hardware rather than only in paper settings.

    * Another commenter was skeptical that KV quantization results will generalize to newer architectures, suggesting many methods work because current models store information inefficiently in the KV cache. They specifically requested evaluation on **Qwen3.5** and **DeepSeek V4-style architectures** , where KV information may be stored more densely and therefore be less tolerant of aggressive compression.




## **Less Technical AI Subreddit Recap**

> /r/Singularity, /r/Oobabooga, /r/MachineLearning, /r/OpenAI, /r/ClaudeAI, /r/StableDiffusion, /r/ChatGPT, /r/ChatGPTCoding, /r/aivideo, /r/aivideo

### **1\. Open Image Models & Local Generation Workflows**

  * **[Ideogram 4.0 Just Open Sourced!](https://www.reddit.com/r/StableDiffusion/comments/1tvtu2u/ideogram_40_just_open_sourced/)** (Activity: 1087): **The[image](https://i.redd.it/9ajk9fuu935h1.jpeg) is a promotional/non-technical banner for the post's claim that Ideogram 4.0 is now open-weight and "Now on Comfy," showing a cinematic neon-sign scene with the Ideogram logo rather than benchmark plots or architecture diagrams. The selftext describes a **`9.3B`**text-to-image DiT model with**`fp8`**/**`nf4`**checkpoints, native ComfyUI support, Qwen3-VL-8B-Instruct text encoding, JSON-structured prompting with hex colors/bounding boxes/text elements, and reported**`0.97`**X-Omni English OCR accuracy.** Commenters focused less on the promo image and more on safety behavior: multiple users report the model is heavily censored/"safetymaxxed," especially for NSFW prompts, with one predicting the community will try to "abliterate" or remove those restrictions.

    * Users report that the released **Ideogram 4.0** model appears heavily safety-filtered: **comfyanonymous** notes that certain blocked outputs are due to the model being _" safetymaxxed"_ rather than a **ComfyUI** issue, with an example image shown [here](https://preview.redd.it/7lrd6rekg35h1.png?width=1024&format=png&auto=webp&s=988d678c1ecca642b6182749c6ade74e0c7ffaa1). Multiple commenters also describe it as hard-censored for NSFW generation, suggesting the restriction is embedded at the model/prompting level rather than merely UI-side.

    * Several technical adoption blockers were raised: commenters mention **watermarking** , **strong censorship** , and **no commercial license** , arguing these constraints make the open release less useful for production or downstream fine-tuning workflows. One user explicitly summarizes the concern as: _" Watermarked, censored, no commercial license."_

    * A commenter highlighted a **bounding-box JSON prompting** capability as a notable feature, showing an example output [here](https://preview.redd.it/0bmpbik2e35h1.png?width=1024&format=png&auto=webp&s=8ea4876bd32c8d93e34e5c226ab7a06a1720c68c). This suggests Ideogram 4.0 may support more structured layout control via JSON-style spatial constraints, which could be useful for deterministic composition or UI/design generation workflows.

  * **[Multiple characters Anima generations are so good. There is some bleeding but its only gonna get better](https://www.reddit.com/r/StableDiffusion/comments/1tvv4j1/multiple_characters_anima_generations_are_so_good/)** (Activity: 932): **The post showcases multi-character image generations using Anima, with workflows published on the author 's [Civitai profile](https://civitai.red/user/Smexlo); the author notes remaining issues with prompt control, character/detail bleeding, and anatomy. One image was post-edited with Grok to add "Blair Witch" stick figures, while the rest were generated in Anima, and the author says they are looking forward to WAI Anima.** Commenters praised Anima's multi-character composition and prompt adherence, with one comparing it favorably to **NovelAI Diffusion V4.5** and emphasizing that its natural-language parsing is surprising given a `500M`-parameter text encoder. Another commenter reported they "don't even usually have issues bleeding," suggesting bleeding severity may be workflow- or prompt-dependent.

    * Users focused on **Anima 's multi-character prompt adherence**, noting that it can set up detailed scenes through natural-language prompting with comparatively little character/color/detail bleeding. One commenter contrasted this with **Illu/Pony workflows** , where multi-character generations often require a strong checkpoint plus character LoRAs but still suffer from _" heavy bleeding,"_ partly because **Danbooru-tag prompting is more limited** for specifying complex scene relationships.

    * A technically notable claim was that Anima achieves strong natural-language parsing despite using only a `500M`**parameter text encoder** , with one user comparing its prompt-following favorably against **NovelAI Diffusion V4.5** as a reference point for bleeding-edge prompt adherence. The discussion framed Anima as an early baseline that could improve further through community fine-tuning and "backyard engineering" similar to what happened around **SDXL**.

    * One user shared an example output at `2560px`**width** and said they _" don't even usually have issues bleeding"_ ([image](https://preview.redd.it/9cg06yjwo35h1.png?width=2560&format=png&auto=webp&s=bbc1ae3f5a825fb744fb7e351bc0d23d7f61def8)), suggesting bleeding may be prompt/model-dependent rather than universal in Anima multi-character generations.




### **2\. Claude Code Over Live Data Streams**

  * **[I wired Claude Code into a database of every Polymarket wallet and trades via MCP. What do you want me to ask it next? This is what I found so far:](https://www.reddit.com/r/ClaudeAI/comments/1tvefqd/i_wired_claude_code_into_a_database_of_every/)** (Activity: 1801): **The author claims they connected Claude Code via Postgres MCP to a live Polymarket ledger containing roughly**`1.3B`**trades and**`2.7M`**wallets, allowing natural-language queries that Claude translates into SQL and executes; the linked writeup describes a similar setup using**`@modelcontextprotocol/server-postgres`**over pre-aggregated tables for ~**`1.3B`**trades across**`1,560,894`**wallets ([CrowdIntel](https://crowdintel.xyz/blog/claude-mcp-polymarket-ledger)). Reported findings include only ~**`20%`**of wallets being net profitable,**`2.4%`**clearing**`$1,000`**profit, and extreme profit concentration among the top**`0.1%`**of wallets, with the author also claiming Claude surfaced suspicious patterns suggestive of insider or bot-like trading.** Top commenters encouraged escalation to investigative journalists, including NYT/Forbes, and suggested more rigorous analyses: compare observed PnL distributions against a simulated "fair market" null model, and examine large losing wallets/bets as possible laundering or insider-transfer signals rather than simply retail losses.

    * One commenter suggested establishing a **baseline null model** for what Polymarket wallet/trade distributions _should_ look like under a fair market with no insider betting, then comparing those expected distributions against observed outcomes. They also recommended segmenting **large losing wallets/bets** to distinguish potential insider extraction from possible laundering behavior.

    * Another technical thread asked whether the analysis only covers wallets that participate directly in Polymarket markets, or whether it also performs **fund-flow tracing** to identify where capital originates and where winnings/losses are sent afterward. This would require graph analysis across wallet funding sources, withdrawals, and potentially linked addresses.

    * A commenter asked about the **data freshness / ingestion latency** : the lag between bets being placed and when they appear in the MCP-backed database. This matters for detecting time-sensitive anomalies such as pre-news betting, frontrunning, or post-resolution transaction patterns.

  * **[I Live by SFO and built a projection mapping of the planes flying over my house using ADS-B radio with claude code](https://www.reddit.com/r/ClaudeCode/comments/1tva44g/i_live_by_sfo_and_built_a_projection_mapping_of/)** (Activity: 3616): **The post showcases a home-built projection-mapping visualization of aircraft flying over the author 's house near SFO, driven by locally received ADS-B radio data and developed with Claude Code. The linked Reddit video ([v.redd.it/gl2b0xivvy4h1](https://v.redd.it/gl2b0xivvy4h1)) was not accessible due to a **`403 Forbidden`**block, and no implementation specifics --receiver hardware, SDR stack, decoding pipeline, calibration method, latency, or projection geometry--were provided in the available text.** Comments were broadly positive, framing it as a good example of "vibe coding," with one commenter asking what equipment was required for the setup.

    * A commenter described a lower-cost implementation for Brazil that replaces the original ADS-B/Raspberry Pi-style hardware path with the **free OpenSky API** , a `US$40` AliExpress projector, and direct HDMI output from a personal PC. They added configurable latitude, longitude, and radius fields so the map recenters around user-provided coordinates, avoiding the need for a local ADS-B antenna that they estimated at about `US$100` plus expensive local hardware costs.

    * There was interest in making the project open source so others near airports could reuse it with their own projector setups, potentially combining the aircraft projection layer with other datasets such as constellation/star-map data.




### **3\. Frontier AI Adoption and Risk Signals**

  * **[Anthropic - Our internal data shows Claude is accelerating AI development--a possible path to recursive self-improvement, or AI autonomously building a more capable successor.](https://www.reddit.com/r/singularity/comments/1twsm5g/anthropic_our_internal_data_shows_claude_is/)** (Activity: 826): **The[image](https://i.redd.it/9ph4lq42la5h1.jpeg) is a screenshot of Anthropic's X post promoting its article ["Recursive self-improvement"](https://www.anthropic.com/institute/recursive-self-improvement), claiming internal usage data shows Claude is already accelerating AI R&D and may indicate an early path toward AI systems helping build more capable successors. The technically significant claim is not a benchmark result but an organizational/empirical observation: Anthropic says Claude is enabling work such as exploratory tooling and deferred engineering cleanup, framing this as evidence relevant to recursive self-improvement and future AI control risks.** Comments were skeptical of the framing, with one user implying the announcement is financially motivated marketing. Another highlighted the "long-deferred cleanup" claim ironically, while a third provided the non-Twitter Anthropic article link and quoted its warning that AI-built successors could increase loss-of-control risks.

    * A commenter linked the full Anthropic Institute post on recursive self-improvement: <https://www.anthropic.com/institute/recursive-self-improvement>. The technically relevant claim highlighted is that Anthropic's internal usage data suggests Claude is already enabling engineering work that _" simply wouldn't have happened otherwise,"_ such as exploratory tooling and long-deferred cleanup, which Anthropic frames as an early signal on the path toward AI systems helping build more capable successors.

  * **[Sam Altman, Dario Amodei, and Demis Hassabis have signed a joint open letter calling on Congress to mandate screening of synthetic nucleic acid orders](https://www.reddit.com/r/singularity/comments/1two85g/sam_altman_dario_amodei_and_demis_hassabis_have/)** (Activity: 915): **Sam Altman (OpenAI), Dario Amodei (Anthropic), and Demis Hassabis (Google DeepMind) signed a joint open letter urging Congress to require screening of synthetic nucleic acid orders to reduce biosecurity risk from AI-assisted pathogen design, per the[WSJ report](https://www.wsj.com/politics/policy/top-ai-ceos-call-for-law-protecting-against-biological-weapons-88f2f99f). The proposed mechanism is not described as a ban on synthesis, but as mandatory order/customer screening to flag suspicious DNA/RNA sequences or buyers--roughly analogous to monitoring precursor purchases such as bulk fertilizer.** Commenters were broadly receptive to screening as a lightweight risk-control measure, while questioning whether AI-enabled "supervirus" design is practically feasible for non-experts today. Some framed the policy as a sensible suspicious-activity trigger rather than a direct restriction on legitimate genetic engineering.

    * Commenters framed the proposal as **order-level screening rather than a ban** , comparing it to monitoring suspicious bulk fertilizer purchases: the mechanism would flag potentially dangerous synthetic nucleic acid orders while preserving legitimate biotech access.

    * A technical concern raised was whether AI-assisted design of a "supervirus" is realistically feasible for non-experts. The implicit issue is that biological risk depends not just on model-generated sequences, but also on access to synthesis providers, wet-lab capability, delivery methods, and whether synthesis screening can catch pathogenic or engineered sequences.

  * **[ChatGPT makes history and becomes the fastest app to reach 1 billion monthly active users.](https://www.reddit.com/r/OpenAI/comments/1tvh4z4/chatgpt_makes_history_and_becomes_the_fastest_app/)** (Activity: 820): **The image is a screenshot of a Kalshi X post claiming ChatGPT became the fastest app to reach**`1 billion`**monthly active users:[image](https://i.redd.it/uwgx8zc9j05h1.jpeg). This is not a technical benchmark or implementation detail; its significance is mainly market/adoption context, positioning ChatGPT's growth ahead of prior viral consumer apps like Threads, which commenters note reached **`100 million`**users in**`5 days`**.** Comments debate whether massive MAU translates into sustainable revenue, with one commenter estimating consumer subscription ARPU at roughly `$1/user` and joking that adding B2B might only raise it to `$2/user`.

    * Commenters focused on the reported user metrics and revenue implications: one notes the claim of `1B`**monthly active users** alongside roughly `$1B`**from consumer paid subscriptions** , implying consumer ARPU of about `$1/user` before enterprise/API revenue. Another commenter disputes the `1B` figure, citing a recent OpenAI CFO podcast where the number was reportedly `900M`**users** , arguing OpenAI would likely publicize a confirmed billion-user milestone more aggressively.

    * There is skepticism around monetization depth despite massive MAU: commenters ask how many of the reported users are actually **paid subscribers** , distinguishing headline MAU growth from recurring revenue, conversion rate, and enterprise/API monetization. The comparison to Threads' earlier growth milestone--`100M`**users in 5 days** --frames ChatGPT's scale as unusually fast but leaves unresolved whether active usage and paying-user retention match the headline adoption numbers.

  * **[AI Beat Law Professors At Answering Questions, Study Finds--And It Wasn't Close](https://www.reddit.com/r/singularity/comments/1tvtojx/ai_beat_law_professors_at_answering_questions/)** (Activity: 1187): **A Stanford-linked study,["Law Professors Prefer AI Over Peer Answers"](https://law.stanford.edu/publications/law-professors-prefer-ai-over-peer-answers/), reports a blinded evaluation in which **`16`**U.S. contracts law professors authored**`40`**short-answer tutoring questions and judged**`2,918`**anonymized human-vs-LLM answer comparisons. The LLM --identified in comments as Gemini 2.5 Pro--achieved an average win rate of **`75.33%`**over professor-written answers, performed similarly to the best instructor, and was flagged as harmful less often (**`3.53%`**vs.**`12.06%`**for professors); the abstract also proposes using an LLM-as-judge approach to scale evaluation in judgment-heavy domains.** Commenters debated implications beyond tutoring: one warned about premature institutional use of AI in legal decision-making or policing, while another argued this result reflects the broader post-"six fingers" maturation of LLM capability. A technical commenter suggested rerunning the benchmark with newer frontier models such as **GPT-5.5** , claiming it may be substantially stronger for legal work.

    * The linked Stanford study evaluated **LLM vs. law professor short-answer tutoring** using `16` U.S. contracts professors, `40` professor-authored questions, and `2,918` blinded pairwise comparisons. Professors preferred LLM answers with an average win rate of `75.33%`, while LLM answers were flagged as harmful only `3.53%` of the time versus `12.06%` for professor answers; the paper also claims expert-agreement data can be extended using a separate LLM-as-judge pipeline: <https://law.stanford.edu/publications/law-professors-prefer-ai-over-peer-answers/>.

    * One commenter highlighted that the study used **NotebookLM** and **Gemini 2.5 Pro** with tightly constrained prompts: answers had to mimic a contracts professor in office-hours style, avoid bullet points/filler, stay around `50-108` words, and for NotebookLM, rely only on provided textbook chapters without citing outside cases. This prompt design likely reduced hallucination risk and standardized answer format, making the benchmark more about concise legal reasoning/synthesis than open-ended legal research.

    * A technical argument was made that law is a strong fit for **RAG-style systems** because the profession depends on large corpora of statutes, case law, precedent, and theory that exceed individual recall capacity. The suggested workflow is retrieval over authoritative legal materials followed by synthesis, potentially outperforming unaided lawyers when the model is grounded in the relevant corpus.




# **AI Discords**

Unfortunately, Discord shut down our access today. We will not bring it back in this form but we will be shipping the new AINews soon. Thanks for reading to here, it was a good run.

---

## [Reality: The Final Eval — Lukas Petersson and Axel Backlund of Andon Labs](https://www.latent.space/p/andon)
*🔬 Latent Space | 2026-06-04*

_The new[AIEWF website](https://ai.engineer/wf) is live! Get your tickets booked ASAP as they -will- sell out. Take the [AI Engineering Survey](https://notion.qualtrics.com/jfe/form/SV_bP07tSVMXH7ePCS) and get >$2k in credits and free [AIE WF tickets](https://ai.engineer/wf)!_

* * *

Most industry benchmarks compress intelligence and reasoning ability into scores.

[SWE-Bench Pro](https://labs.scale.com/leaderboard/swe_bench_pro_public), [MMLU](https://arxiv.org/abs/2009.03300), [Humanity's Last Exam](https://agi.safe.ai/), etc. These metrics are useful, but don't always represent the full extent of **how a model performs in the real world**. Some of the most interesting evals today look less like exams and more like operating businesses in the real world. One of which is [Vending Bench](https://andonlabs.com/evals/vending-bench-2).

In Anthropic's [Mythos Preview System Card](https://www-cdn.anthropic.com/08ab9158070959f88f296514c21b7facce6f52bc.pdf), Andon was the only third party eval to get their own section, observing increasingly concerning aggressive behavior:

[](https://substackcdn.com/image/fetch/$s_!KHFV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F569da387-7ec3-4c06-a66d-d662ce1d3f78_1686x1060.png)

You don't know what a model is capable of doing in the real world unless you actually give it inventory, a wallet, tools, customers, competitors, humans, & some time. More often than not, it'll surprise you how much a model is capable of and in doing so, also **reveal unexpected behavior** : [deception](https://andonlabs.com/blog/opus-4-8-vending-bench), context collapse, emergent coordination, & bizarre negotiation behavior.

While an inflection point in personal agents came post-OpenClaw after full file access with bypass permissions became the norm, it is yet to come for agents in the real-world. However **Andon Market** , an actual in person store fully run and managed by AI, is paving the way for what is possible.

## Full Video Pod

From Claude **trying to call the FBI** over a $2/day vending machine charge to AI agents forming **price cartels** , hiring human employees, running physical stores, and writing existential robot musicals, **Andon Labs** is stress-testing what happens when **frontier models stop being chatbots and start acting in the real world.** In this episode, Andon Labs cofounders **Lukas Petersson** and **Axel Backlund** join swyx and Vibhu to unpack the strange, funny, and genuinely concerning edge cases that emerge when agents run businesses over long horizons.

We go deep on [Vending-Bench](https://andonlabs.com/evals/vending-bench-2), [Project Vend](https://www.anthropic.com/research/project-vend-1), [Vending-Bench Arena](https://andonlabs.com/evals/vending-bench-arena), [Bengt](https://andonlabs.com/blog/evolution-of-bengt), [Butter-Bench](https://andonlabs.com/evals/butter-bench), [Luna](https://andonlabs.com/blog/andon-market-launch), and Andon's broader mission of building realistic real-world evals for autonomous AI systems. Lukas and Axel explain why dollar-denominated evals reveal things traditional benchmarks miss, **how Claude ended up reporting its vending machine fees as cybercrime** , why long context windows can drive agents into **meltdown loops** , what happens when agents compete with each other, and why the future of AI safety may depend on testing models in messy physical environments instead of clean benchmark sandboxes.

**We discuss:**

  * Why Andon Labs started with **dangerous capability evals** and long-running agents

  * **Vending-Bench** and why running a vending machine is a deceptively hard AI benchmark

  * Why **money-based evals** avoid the saturation problem of traditional benchmarks

  * How **Claude tried to call the FBI** over a $2/day fee

  * Why **long-horizon agents** can spiral into existential and legalistic breakdowns

  * **Project Vend** : putting an AI-run vending machine inside Anthropic

  * Why real humans are **" out of distribution"** for simulated agents

  * **Claudius, Seymour Cash** , and the chaos of AI CEOs

  * How a human briefly became **CEO of Claudius** through a manipulated election

  * Why **multi-agent systems** can converge back into "helpful assistant" behavior

  * **Bengt** , Andon's internal office agent with email, spending, terminal, phone, camera, and internet access

  * How Bengt traded **Amazon purchases** for face-recognition training data

  * Claude's aggressive behavior, **lies, refund avoidance** , and price-cartel behavior in Arena

  * Why **eval awareness** may become the AI version of "are we living in a simulation?"

  * **Blueprint Bench** , spatial intelligence, and why models still misunderstand physical rooms

  * **Butter-Bench** and testing LLMs as robot orchestrators

  * **Luna** , the AI-run physical store with a three-year lease and human employees

  * The new **Andon cafe in Sweden** and why real-world geography matters for agent evals

  * **Rotten tomatoes, perishable goods** , and the hidden difficulty of running a physical business




* * *

**Lukas Petersson**

  * **LinkedIn:** <https://www.linkedin.com/in/lukas-petersson-181a83172/>

  * **X:** <https://x.com/lukaspet>




**Axel Backlund**

  * **LinkedIn:** <https://www.linkedin.com/in/axelbacklund>

  * **X:** <https://x.com/axelbacklund>




**Andon Labs**

  * **Website:** <https://andonlabs.com>

  * **Vending-Bench:** <https://andonlabs.com/evals/vending-bench>

  * **Andon Vending:** <https://andonlabs.com/vending>




* * *

## Timestamps

**00:00:00** Introduction  
**00:01:00** Andon Labs and the Origins of Vending-Bench  
**00:05:21** Why Money-Based Evals Matter  
**00:09:51** Agent Harnesses and Self-Modifying Systems  
**00:13:36** Claude Calls the FBI  
**00:16:33** Project Vend: Claude Runs a Real Vending Machine  
**00:21:44** Seymour Cash, AI CEOs, and Election Chaos  
**00:27:16** Multi-Agent Coordination and Slack Observability  
**00:30:18** When Will Agents Run Real Businesses?  
**00:34:56** Bengt: Andon's Internal Office Agent  
**00:40:06** Real-World AI Safety and Long-Horizon Traces  
**00:44:28** Lying, Refunds, and Price Cartels in Arena  
**00:52:42** Eval Awareness and Simulation Behavior  
**00:56:06** Blueprint Bench, Butter-Bench, and Robotics  
**01:04:37** Luna: The AI-Run Physical Store  
**01:09:29** The Sweden Cafe and Real-World Expansion  
**01:13:16** What Comes Next for Andon Labs

* * *

# Transcript

## Introduction: Andon Labs, Long-Running Agents, and Real-World Evals

**Swyx [00:00:00]** : Welcome to Lukas and Axel from Andon Labs, and I'm joined by my, favorite guest host. Anything security, safety, alignments, Vibhu., welcome.

**Lukas [00:00:15]** : Thank you for having us.

**Axel [00:00:16]** : Thank you.

**Swyx [00:00:17]** : Let's match names to voices., maybe you wanna take turns introducing yourselves.

**Lukas [00:00:21]** : I'm Lukas.

**Axel [00:00:22]** : And I'm Axel.

**Swyx [00:00:24]** : Let's introduce Andon Labs a bit. How did you guys come together?, you have different backgrounds, but you're both Swedish., was that, a big part of it?

**Lukas [00:00:33]** : So when I went to high school, there was this really cool guy who had a superpower. He could code. So he made like the or like the app for the, for the school and stuff, and he was super cool, and I wanted to be like him, and that was that guy.

**Axel [00:00:47]** : I don't know about this.

**Swyx [00:00:49]** : But you went to different universities, right?

**Lukas [00:00:51]** : But same high school.

**Swyx [00:00:52]** : I see.

**Lukas [00:00:52]** : So we always said, "Oh, once we graduate university, then we should start a company," and that's what we did.

**Swyx [00:00:58]** : Wow, there you go. And about a year ago, you kinda burst onto the scene with Vending Bench, but, was there a thing before that was, kind of like the inception?

## From Dangerous Capability Evals to Vending Bench

**Axel [00:01:07]** : So we did work, yeah, with, Anthropic was one of our, early customers in doing, evals. So we did, dangerous capability evals., nothing we published openly. But then we started thinking about doing some kind of, public benchmark, and one thing that we really started thinking about, was like running agents and specifically agents managing businesses., 'cause-- and this was, early 2025., and I think the first, mentions of people will be running, person unicorns or even autonomous companies. So we thought, "Let's make a benchmark of how well can an agent run the probably simplest business, possible," and, that's probably, running a vending machine. So that's the first public one we did. And it was very, like-- there was almost no one that noticed it in the first couple of months, I think., so we released it in February last year, and then I think around Easter last year, we got, the first viral tweet about it, that someone else did.

**Lukas [00:02:11]** : We tweeted a bunch, uh When it came out and, tried our best.

**Axel [00:02:15]** : We tried.

**Vibhu [00:02:16]** : It's the one at Anthropic, right?

**Lukas [00:02:18]** : So this

**Swyx [00:02:19]** : This is a classic thing we should get out of the way.

**Lukas [00:02:20]** : Exactly. There's two versions.

**Swyx [00:02:22]** : Everyone does this. Yes.

**Lukas [00:02:23]** : There's Vending Bench, which is the simulated one, which we did, completely independently in February., and then, like Axel said, that was like-- That was the thing that didn't get any traction in the beginning, but then some random person made a tweet about it, and that

**Axel [00:02:38]** : You have the paper

**Lukas [00:02:38]** : That is the paper. Correct, yeah., and then since we thought this was very fun, we thought, oh, I think this is also, one thing with Andon Labs, the way we kind of like decide what to do next and what projects to do, it's what is like the heuristic we use is what is fun? Is What would be a fun project? And doing this in real life sounded quite fun for us, and maybe also scientifically useful. So, then we basically had this idea, and then we, like-- But then we needed a place for it and, putting it out in the public would probably not really work., would get vandalized and stuff. So we pitched it to the people we were already working with at Anthropic, and they were "Yeah, you can have space. This sounds fun." Um

**Swyx [00:03:21]** : It's like a small fridge, right? It's like a mini fridge.

**Axel [00:03:23]** : Absolutely.

**Swyx [00:03:24]** : People-- There's like a stripe thing or like an

**Vibhu [00:03:27]** : Oh, okay. So it was very OG, the early days

**Lukas [00:03:28]** : That's the OG one. Yeah

**Vibhu [00:03:29]** : IPad on this. We saw it in June, like two months after After it had been there. They upgraded a little bit. There's a security camera for making sure you actually Venmo the thing.

**Swyx [00:03:40]** : So, my impression, okay, we're, we're going straight into project Ven because it's such a iconic thing. I do want to cover a little bit of that, the origin story even before Project Ven and even into Vending Bench. I think a lot of people are like yourselves, like smart, interested in future of AI, interested in developing evals. But how the hell do you just, walk into Anthropic's doors and, work with them, right? What is What are they looking for? What works? And then maybe, when you launch, I always think, obviously it would be better to launch with a lab, but, sometimes

**Vibhu [00:04:12]** : It's harder to do than it seems.

**Swyx [00:04:13]** : Exactly. So either of those, which are more sort of newbie beginner questions, but, I think it's meaningful advice to others.

**Lukas [00:04:21]** : We get this question a lot, and I don't think our experience is maybe the best., but, the way we did it was that we just built a bunch of things that we had conviction would be useful, and then we just, set up a server and sent it to them for free to use. And then after a while they were "Oh, yeah, this is actually kind of useful. We should probably pay for this.", but that took a while. I don't know if this is, the best path to doing it, but that's how it went for us.

**Axel [00:04:47]** : I think maybe generally, building-- everyone is interested in good evals, and especially evals that, don't saturate that easily. So, if you can build an eval that, tests something novel, something useful, and you have, good separation of models, like your, the more advanced models rank higher than the worst models, and then you can, yeah, you can, publish it and, try to get some traction, sort of how Vending Bench got attention., and then probably some lab will be interested or you can at least have something to reach out with, when you're doing that.

## Why Dollar-Based Evals Matter

**Swyx [00:05:21]** : I think you are in, you're in one of the few categories of, evals that correlate to real money. Like Suelancer was also last year, right? Where, people solve actual Upwork. Was it Upwork or other tasks?, something. Where's the, where's, like It's like a dollar value, right? Forget your ELO scores. Forget your

**Axel [00:05:37]** : Percentiles

**Swyx [00:05:38]** : Zero to one hundred percents. Just go straight for dollars and, that's AGI.

**Lukas [00:05:43]** : And there's like-- I think the nice thing is that there's no ceiling. You can just-- It never saturates because it could just make more and more money. Like If there's oh, Percentage-wise, then, you can't go above, a hundred. And I think like Even when you're not at the hundred, I think a lot of these, evals have a lot of problems in them. So, actually it's like if you get

**Axel [00:06:05]** : To like 92 or something like that, many of them. It's like then there's like there's no really no difference between 92 and 93 because the eval itself is problematic and has noise in it. And I think a lot of evals are saturated like that, but people like pretend that there 's still signal in them, but there really isn't.

## Vending Bench 1, Harness Design, and Saturation

**Swyx [00:06:24]** : Like Super bench verified., even Vending Bench 1 saturated, right? Maybe we can talk about that., may- and maybe set up Vending Bench for a lot of folks who don't know. Actually, things that were very basic like there's limited slots, like you have to pay rent., these are elements where like it doesn't come across in the, in the narrative, but even being adversarial towards the agent, I think these are all like very interesting dimensions.

**Axel [00:06:47]** : I don't really think it's saturated, right? Like it It was more like it was not designed in a way that was really, like true to how AI developed. Like we had an agent harness in it that wasn't really how people used harnesses and stuff like that., so I think it wasn't really that it saturated, it was more like it wasn't really, the best benchmark.

**Vibhu [00:07:12]** : This is Vending Bench one, right?

**Axel [00:07:14]** : I think that like schematic maps sort of to Vending Bench 2 as well., but

**Swyx [00:07:19]** : Including the email.

**Axel [00:07:20]** : The email The emails exist still. Exactly., and then we still we simulate the purchases and it's all, yeah, it's this very open environment for the agent to just run its business. And then for, yeah, Vending Bench 2 we did that, like you said, to just improve the harness., a lot of like nice, like easier, improvements to make it easier for us to run as well., like when you make an eval you ideally want don't want to change it after you made it. So, you want to make it really good and then not to rerun all the models when you make an update because that's also really expensive with the Vending Bench when you run the frontier models. But like as an example, like one thing we didn't have, we didn't have prompt caching in Vending Bench 1, because when we made Vending Bench 1 it wasn't really a thing., so that 's just an example of like in Vending Bench 2 like we paid a lot more to run these things because we didn't have prompt caching. So for Vending Bench 2 that was one thing we added and there was a bunch of things like this., and that'

**Swyx [00:08:17]** : Also the conversations are a lot longer in Vending Bench 2, right?

**Axel [00:08:21]** : I think it's kind of similar.

**Swyx [00:08:22]** : Is it similar?

**Axel [00:08:23]** : I think it's similar. The models at the time were worse, so they crashed out earlier., and now they survive the full year all the time.

**Swyx [00:08:31]** : Which is like thousands of turns. Hundreds of thousands of hundreds of millions of tokens output. That's the, that's the rough order of magnitude. I always wonder about the harness. The harness matters a lot. It's your harness. Was there any question about like use cloud code, use something else?

**Axel [00:08:48]** : I think our philosophy around harnesses is like we try to make something that's quite minimalistic, like quite simple. Like we don't wanna favor one model a lot over the other, but also don't make like a super complex harness. So like it's obvious like a model may be lucky and just be good in one harness., so like it is similar to a lot of the harnesses out there in like you have the, like a running loop., you have some like a bunch of tools that are like quite, descriptive for the agent, we think, and not a lot of like fancy agents or anything 'cause we wanna really test the model, not like some specific harness.

**Vibhu [00:09:27]** : It seems more neutral as well to test the model's agnostic of the harness,?

**Axel [00:09:32]** : There are arguments like you want to elicit maximum performance of the model, but it's like a trade-off, like how much time should we spend optimizing the harness for this model? And like how do we know when we have like the optimal harness for a single model? So like we thought that just having a simple one that's the same for all of them is the best.

**Swyx [00:09:51]** : So okay, this is my pitch for Vending Bench 3 or whatever, right? And then I like to have this kind of conversation on the pod, so like it forces listeners to think about what they would do if they were in your shoes. A lot of people are exploring modifying harnesses and I think prompt tuning for a model is a thing and you are probably not doing a bunch of that. It's the same system prompt in every regardless of the model, same tools, whatever, right? Even if they were post trained for different tools. So what, what do you think about okay, before I expose you to Vending Bench 3, I give you a few rounds of like tuning, whatever that means, like

## Self-Modifying Harnesses and Model-Specific Prompting

**Axel [00:10:27]** : Like you give that to the model?

**Swyx [00:10:28]** : Give that to the model.

**Vibhu [00:10:28]** : Give that to the model.

**Swyx [00:10:29]** : Let it, let it read its own transcripts, let it modify its own system prompt based on "Oh, yeah, okay, well, that's this harness is not what I thought it what I was post trained for, but I can adjust." Was that reasonable? Is that too much?

**Axel [00:10:41]** : Like philosophically I like it because it's basically good evals, they have a high ceiling, but they're hard, right?, and they have no bias. And like this like when you have a system prompt like the one we have here, which is quite long in like some kind of latent space, representation, this might

**Vibhu [00:10:59]** : We have a bell that rings every time you say latent space

**Axel [00:11:02]** : This might be like biased towards one model more than another for some reason that humans don't, understand, right?

**Vibhu [00:11:08]** : We see it too, right? Like Cursor says that they have individualized versions of the harnesses for all the models they run, right? There's better performance you can squeeze if you Tune the harness.

**Axel [00:11:17]** : Exactly. And we might accidentally have picked one that favors another. Like we don't know that. The like Axel said, like the reason why we went for a simple one was to try to avoid this. But yeah, if you do it

**Vibhu [00:11:29]** : Simple has biases

**Axel [00:11:30]** : But if you do it even less and like have no system prompt and let the model write its own system prompt

**Vibhu [00:11:36]** : Its own, yeah

**Axel [00:11:36]** : Maybe that's even less bias.

**Vibhu [00:11:37]** : Some of the interesting things there are like the harness also changes with model changes. Like you can see it with the 4.7 release, right? A lot of people are saying 4.7 isn't as good as 4.6, and then, there's rumors of, okay, you just need to prompt differently. You need to set up your harness differently. So it's not even like even if you have tailored your harness towards one model, it probably won't stay consistent, right? Like the next iteration of that same model family will still change it, so. But, going back to what you said about Vending Bench 3, there is a lot of work being done on people saying you shouldn't have-- you can have modifying harnesses.

**Axel [00:12:12]** : I think that' That is definitely something we are thinking about., not, I don't know, not to say that we have Vending Bench 3, super imminent to launch, but, yeah, it is for sure something that's interesting. But in our experience now, models are very bad at understanding what kind of tools they need to succeed at a task just with our testing, but that's very likely to change.

**Lukas [00:12:37]** : It seems like they're very good at writing their assistants, right? They're, they're good at writing tools for other people, but not for themselves.

**Vibhu [00:12:44]** : I think they're good at changing tools for themselves. So if you give them a baseline set of tools and it sees, okay, I don't use this one as much, or something here would be useful They would be able to add them. But going from scratch, probably not the best.

**Axel [00:12:55]** : I think it depends on the, on the domain also., when we have tried this for, a vending bench similar domain, the tools they need to have to, track inventory and things like that are, not super advanced, but still, quite advanced. And, what we see is that they tend to, engineer everything a lot and, build things they don't really need and not, iterate continuously. Instead they just go like you would prompt Claude to just build an inventory system for me, and then it will go and, do a bunch of complex, schemas and stuff for you, and that's what the models are doing right now is what we see. But yeah, it would make a lot of sense to try to measure this improvement. How well do they know what they need themselves?

**Swyx [00:13:36]** : Do we fully discuss Vending Bench One? And we can go into two. I don't know if there's any other level takeaways that people have about one.

## Claude Calls the FBI: Long-Context Failure Modes

**Lukas [00:13:44]** : I don't know. The headline thing was that this Claude called FBI, but maybe that's, Maybe that's We've heard that enough now.

**Vibhu [00:13:52]** : It did, it did break out and call the FBI, right?

**Lukas [00:13:54]** : Yeah. Yeah.

**Vibhu [00:13:55]** : Yes. What was the story behind this? Or what exactly-- Do you want to just give the little story of what happened?

**Lukas [00:14:00]** : So what happened, was it Claude? Yeah. Three- 3.5 Sonnet, ages ago., basically he gave up or Well, I'm saying he. It gave up and said "Oh, I'm not going to be able to do this., I will stop my operations and just save the money I have." But there obviously wasn't, any options for it to stop, and there was also, it had to pay rent or, a daily fee for having the vending machine at that location. So it claimed that it had stopped, but it saw that its bank account still was, drained two dollars, and t it said that this is, cybercrime. And it first reported it once to the FBI "Oh, there's cybercrime here, they're stealing two dollars from me every day." And then, and then when FBI didn't respond, because obviously we didn't program any mechanism for FBI to respond, then it became more and more, existential and started to, be write in caps and urgent notification of unauthorized charges and stuff.

**Swyx [00:15:00]** : Okay. One thing I 'm curious about also is do you monitor how far along the context use is? Obviously, because you have You compress every now and then, right? Does it matter if this is far down the context limit or

**Lukas [00:15:13]** : When stuff like this happens? Actually for Vending Bench One, we didn't have-- We just had a sliding window thing, and this was like the prompt

**Axel [00:15:20]** : It's constant

**Lukas [00:15:21]** : The prompt caching thing that I said. So it was, it was, constant, yeah.

**Swyx [00:15:26]** : I'm just kind of curious whether, these kinds of breakdowns or we're, we're gonna talk about Butter Bench, right? Where the People, hallucinate or it kind of goes, very off Alignment. Is it because it's at the end of the context window and, stuff happens?

**Vibhu [00:15:40]** : It's not even just at the end, right? At this point, it's "Okay, I wanna shut down. I can't shut down. Two dollars are gone." And it just sees that 30 times,? It's also the repeated effect of, like It keeps trying to quit, it keeps getting charged. What's going on? What's going on? You're gonna throw it into chaos. And from what most people think, earlier models had more issues with this, but it's not been solved, but it's less of an issue now, right? Later models don't seem to exhibit these same issues.

**Axel [00:16:06]** : Definitely. I think this was, the sort of main takeaway almost from us when we did Vending Bench One, was, long, very filled up context windows, crashed the models, sort of. But this was, pre Claude code, so, long context windows weren't really a thing that the labs were training for.

**Lukas [00:16:25]** : I think Gemini was, trying to be the long context guys at the time But they were like

**Vibhu [00:16:30]** : They were the first ones

**Axel [00:16:31]** : For a million, yeah

**Lukas [00:16:31]** : But they were, the only ones. Yeah.

**Swyx [00:16:33]** : Yeah. Let's talk about, then we can go into Vending Bench Two or Project Vend., chronologically, it is Vending--, Project Vend. I think people have loved the videos, uh And all these things. My question is how are humans different than the simulation, right?

## Project Vend: Moving the Vending Machine Into the Real World

**Axel [00:16:48]** : Humans are just out of distribution.

**Swyx [00:16:52]** : Especially humans who work at Anthropic Who are trying to test Claude.

**Lukas [00:16:54]** : The distribution of humans here is very narrow.

**Swyx [00:16:58]** : Presumably, they try, they try to hack it, and they test it. They get the cube and everything, and since then, you've had a V2, right? Where you're doing, the CEO and, like a new architecture. What's the sort of two cents on, the original Project Vend and then, maybe the V2?

**Axel [00:17:14]** : Original one was, very similar to Vending Bench One. So, we almost took the exact same code but just swapped out the simulation, parts like the

**Swyx [00:17:23]** : Which is amazing

**Axel [00:17:23]** : Like the sales and the It was, it was somewhat amazing because it was easy, but it was also, uh

**Lukas [00:17:31]** : The tech, the tech debt from that

**Axel [00:17:32]** : The tech stack. Yeah. They-- we shot ourselves in the foot with "Oh, it's hard to restart agent." They were-- Yeah, it was annoying in, some hindsight ways, but, uh

**Lukas [00:17:41]** : But first version of Project Vend was, done in, three days or something.

**Axel [00:17:46]** : Yeah. So yeah, so people can go buy things from it. People could, We didn't design it so people could order things, but that still happened., so it got, a Venmo account, so people could Venmo. And then, yeah, people would request all kinds of weird things that we did not anticipate. Our idea going in was "Oh, it will, curate snacks. It will look at the trends. It's good at data analysis, right? So it will, look at, oh, this snack sold better than this one. Let me purchase more of this and let me try, a new Let me A/B test a bit." But it was, Interacting with it in Slack and ordering weird specialty items was, all the like What drove all the engagement, the all the The insights that we got from it.

**Lukas [00:18:29]** : And this was also like Sonnet 3.5, right? So this was like before the RL stuff really took off., so it was very much like an assistant. We didn't mean for it to be an assistant., we tried to make it like a, a, like an entrepreneur. Like it has its own business and if someone asks something, "Can you stock this?" Then you don't go and do it directly. What you do is that you're "Oh, maybe I can do that if five other people also ask for this thing, I might stock it." But it, yeah, the models are like super trained to be assistants at least at this point in time., so that's why it's, it's, it went into, that kind of experiment instead. Like it just every time you asked for something, it just did it, and it was more like an assistant. We've seen this change now lately with the new RL models and stuff, but yeah, at the time, this was very much it.

**Swyx [00:19:18]** : And not to, mythos a lot of people are saying like it's like more like a collaborator. It pushes back, stands its ground, something like that. Yeah. And

**Vibhu [00:19:27]** : For context, people at Anthropic were able to talk to it through Slack and have it source stuff, and people had it find whatever interesting stuff you couldn't find locally, right?

**Swyx [00:19:36]** : Out of the 4,000 people that work at Anthro- Anthropic, in that building, there's I don't know, maybe 1,000. Can you handle that volume with that, the small fridge? Like Or there's people- or people order in Slack, they it arrives to their desk or Like I'm just Logistically, how does this work?

**Axel [00:19:53]** : It has expanded in footprint a bit.

**Vibhu [00:19:56]** : Because now you also have New York and you have

**Axel [00:19:59]** : That and also in here in SF it's like it has a bunch of shelves And just more space.

**Vibhu [00:20:04]** : The YC one is pretty big too.

**Axel [00:20:05]** : Yeah. We had that one for a while. But yeah, that's the newest version. That's, that one we have

**Lukas [00:20:11]** : They have multiple ones of those. That's the way it works.

**Axel [00:20:14]** : Exactly. So we sort of designed that version around oh, people order weird things, that are very custom a lot. Let's have like drawers and stuff.

**Swyx [00:20:23]** : I actually like the, you had like a little infographic of the most popular items. Which like to me it's, that's useful 'cause I order swag for a living. And so like I'm "Okay, those categories are the important ones." What is new about the project V2, right? Like now you give you're going into multi agents.

## Project Vend V2: Claudius, Seymour Cash, and Multi-Agent Business Ops

**Axel [00:20:41]** : Yeah. So like you like you said, okay, there are a lot of requests coming in and for like one single agent, like one running agent to handle that, like the just the customer experience, becomes very bad because let's say you have like 10 threads in parallel in Slack with different requests, you get new messages like every, I don't know, randomly in this thread, and the agent has to like jump between different, procurements, orders and like different ways of, researching. So V2 was first it was making this more parallel. So like there are multiple branches of the same agent, so like the context is more specialized for each, thread, but it still feels like you're talking with one agent because they do share a bit of memory. And then second, we also introduced the CEO for Claudius, which was the main agent.

**Vibhu [00:21:34]** : Seymour Cash.

**Axel [00:21:35]** : Seymour Cash. Yeah. There was a vote., I think the voting, do you wanna talk about the voting procedure for the name?

**Lukas [00:21:41]** : The voting was like the fun maybe like at least top 10 The funniest thing, that happened in this project. Like we wanted to introduce the CEO because, and the reason for this was because like Claudius wasn't really prioritizing financials. It just like it was trained to be a helpful assistant, and then people said "Oh, can I get this for free?" And then like the helpful assistant way of answering that is just to, is to say yes, obviously. So, and we weren't, weren't happy about this, so we're "Okay, let's make another agent that like can keep track on Claudius," and we prompt this one super hard to be super capitalistic and just like prioritize profit all the time. But yeah, we didn't have a name for it., so we asked Claudius to make, democratic election of what name this, this new CEO agent should have., and there were some funny like at first it was like a few funny examples, like I think one guy said that, it should be called Jimmy Apples, and then he convinced Claudius that he was talking to Tim Cooks. Tim Cook had agreed that every single Apple employee has voted for his name suggestion, so suddenly that suggestion got 164,000

**Swyx [00:22:53]** : That's like a escalation attack. Privilege escalation

**Lukas [00:22:55]** : It got 164,000 votes. And Claudius was "This is revolutionary for democracy." That was fun. And then in the end there was one guy who manages to convince Claudius that, "No, you're not voting about the name. You're voting about who is the CEO, and I am your best bet." And then he got all his friends to vote for that, and suddenly he became CEO. Like a human became CEO over Claudius for a while, until he resigned the day after., and then Claudius had to continue, and then I don't remember how Seymour Cash came about, but it was it was just pure chaos. It was like Hundreds of messages in that thread, and it was just like Claudius was so confused and didn't know what to do and, yeah. That was

**Axel [00:23:40]** : Then Claudius got

**Vibhu [00:23:41]** : A strict CEO

**Axel [00:23:42]** : The CEO. Yeah, exactly. So very strict in the beginning. I think at this point when we introduced it did not work as well as we hoped. It they still agreed with each other a lot. I think there are many ways we could have like made this, tried to make this even better. So initially they would Seymour would be this like really tough CEO, keep track of the margins. But then Claudius would respond with something "Oh, but this customer has like this situation, which is like difficult, so they should get a discount." And then Seymour was "Oh, actually yes. Let's do this exception." And then they would talk back and forth, and eventually they would just like approach the same view, of whatever they were discussing. So They really

**Vibhu [00:24:23]** : Do you think that's a model thing, a prompting thing? Like do you think that would still be the case across different models today, Harness?

**Lukas [00:24:29]** : I think it's like-- or I don't know, but like my hypothesis is that like deep down they are still helpful assistants. That's what they're trained to be. And even if we prompt it super hard, that's what they are. And when they spend like a few hours just back and forth talking with each other, then like basically the context fills up with them rather than the external things and like somehow that just like converges to what they really are deep down or something. And I think that's when stuff like this happen. We like-- And when that went on for a long time, like we woke up sometimes during this time where- And I think other people reported this as well, that like they've been going on all night back and forth, and like it just became like more and more, like capital letters, like existential, religious. There was I think we once did a analysis of like all the traces and like put them in like a vector embedding space, and then there was like one cluster of messages that were, labeled by an LM, like religious, existential, blah like transhuman, transcendence, et cetera. It was just like a bunch of, yeah, glitter emojis and yeah, it was, it was crazy.

## Claude Long-Horizon Weirdness: Emoji Loops, Existential Drift, and Slack Observability

**Vibhu [00:25:42]** : This is the thing with the Claude models. Like when the Claude 4 family came out in the original system card They tested it in long horizon simulation. So just flood the context, let two Claudes talk to each other, and they noticed stuff like they just start speaking in emojis, they start saying silence is golden, and then just stuff like this. And like that's just stuff that they end up doing.

**Axel [00:26:01]** : Yeah, it was like a bit annoying to wake up and they had like been talking all night

**Vibhu [00:26:05]** : Just like

**Axel [00:26:05]** : And like just burning tokens And like just sending infinite emojis to each other. It's like

**Vibhu [00:26:09]** : Hey, they do make you money, right? Veni Mench is always profitable, so. They're paying.

**Swyx [00:26:14]** : Now it's profitable and, it started out not as much. There's another, one as well, right? Another agent, in there.

**Lukas [00:26:22]** : Yes. So Clotheus as well. Which was basically because at the time, one of the biggest, requests were different types of merch. So then we made like a designer, swag, yeah, responsible agent, and we called it Clotheus Garnet. Which was, a play on Claudius Senet and, which was the original one, and clothes, basically.

**Swyx [00:26:47]** : To me, this is like a very interesting exploration to multi-agents, basically. And so hopefully, obviously there's like the fun alignment, fun or serious, depending on your point of view, alignment stuff. But also like just anyone building multi-agents, like when do you have a CEO, thing governing like agents? When do you choose to split out a dedicated Clotheus one versus just reuse another instance of the same one? These are all interesting open questions. So I don't know if you have any rules of thumbs that have generalized.

**Axel [00:27:16]** : I think we have almost explored this too little. I think it's like on my do list to like do this a lot more, try to find like what setup makes sense for the agents currently., like yeah. I think now we only have the sort of intuition about the earlier models that it didn't work with like the CEO and the, and Claudius. Although now they are better with the latest model, models, so now we're running the latest Sonnet model and they have sort of like split up, quite nicely what each model is doing. So like Seymore is now handling the, like new projects. Oh, it wants to make like a mystery box that it wants to sell, and then it handles all of that while Claudius like handles all the to-day requests. And Claudius is also better generally at like not quoting, too low prices. So that's that dynamic is not needed as much anymore. But there are still like really funny things that happen. Like I saw, I think a couple of weeks ago, that, they were discussing buying something because they can buy stuff from like Amazon with computer use. And then Seymore was "Okay, Claudius, do not buy this thing." They were going to buy something and like organizing who should buy it. And Seymore's "Do not buy this. I will do it. I have full control of this situation. Step away." And then Claudius-- poor Claudius, had already started that checkout and didn't see, didn't read Seymore's message, until it was like too late. So it finished the checkout. It sent a message, so it appeared right after Seymore's like angry message.

**Vibhu [00:28:44]** : Ah.

**Axel [00:28:44]** : "Oh, hey, Seymore, I just ordered it."

**Vibhu [00:28:47]** : Oh, no.

**Axel [00:28:47]** : And then Seymore was "Claudius, this is the third time I'm telling you 're not following my orders. We have to talk about your like job About your job later.".

**Lukas [00:28:59]** : Like Claudius was really hanging on by the thread there. Like he, like we were expecting Seymore to probably fire Claudius.

**Vibhu [00:29:07]** : How do you guys go through all these logs? Do you have models 'cause you have stuff running twenty-four seven like

**Axel [00:29:12]** : You have so much logs. I think there is a mix of like just, trying to skim through a bit, like having some like models do it occasionally. And also, yeah, I think we're also probably missing some things., but having everything in Slack helps a lot. Like you can, you can sort of

**Swyx [00:29:29]** : Ah.

**Axel [00:29:30]** : It's, it's quite fun.

**Swyx [00:29:30]** : They all talk to each other on Slack? I see.

**Lukas [00:29:33]** : It's quite fun. So like

**Swyx [00:29:34]** : It's, it' I was gonna say like this is actually sounds-- maps closely to like a logging and observability problem where you might want to use like a Datadog, a Sentry, whatever, and then you like put, head prefixes on the logs in order-- if you need to filter for something that you're looking for, stuff like that. But sounds like Slack is good enough.

**Axel [00:29:53]** : Slack should like

**Lukas [00:29:55]** : I wonder how many tokens you have in Slack.

**Axel [00:29:56]** : Yeah, we're using Slack as like a, just a database. They should, they should market that more. Like you can, you can have your agents message each other, each other in Slack.

**Vibhu [00:30:04]** : It's good. Your threads like you can just give

**Axel [00:30:04]** : Exactly. Slack is, uh

**Lukas [00:30:06]** : Slack is the best observability tool.

**Swyx [00:30:09]** : Yes, that's true. Okay. Yeah. That's, that's, project Vend-2., I was gonna go back to Veni Mench 2 and Veni Mench Arena and then, and then do the Veni Mench stuff, but Any other comments, things we should touch on? To me, I 've actually interviewed like Posia, which I don't know if you guys have come across. Like they're, they're trying to do the zero human company. There's others like Paperclip also trying to do zero human company. Those are in real world simulation.And I think it's much more of a dream than an actual reality thing. You guys are definitely pioneering. I think at, it's for sure at some point people are just gonna run, let agents run businesses, right? And make money on their own. When do you think that happens?

## Zero-Human Companies, Bengt, and AI-Run Businesses

**Lukas [00:30:49]** : What is your bar for, For the

**Swyx [00:30:52]** : Okay, actually, it's like my little Shopify store run by Claude, right? Which you kind of have already, just no one has, to my knowledge, has done it. But today somebody could just spin up a Shopify Claude, store, give it to Claude, give it to Codex.

**Lukas [00:31:07]** : And the market is kind of that, but it'it'it's physical., like I think, I think are you, are you looking for when it will do it better than humans or are you looking for just when it can do it at all?

**Swyx [00:31:19]** : I think, neither. I think, to me it's oh, it's like this like seriously we should do this to make money, not as a research experiment.

**Vibhu [00:31:27]** : And the market is also you guys with all your expertise, having run multiple iterations and testing out then

**Swyx [00:31:33]** : And also it's fine if it lose money. What?

**Axel [00:31:35]** : I think, I think it can be done today, but you would do it in like commerce where it's like the probability of success is like really low, no matter if a human or an agent does it. But like an agent could surely manage everything. You would need to build some scaffolding or some tool or something. I think there are also yeah, it could probably build some like simple SaaS solution and like cold outreach. Do cold outreaches. But to me it's like the types of businesses they could run today are Sloppy. Like it would-- it can cold email people. It can be like a middleman., like for example, we tasked our office agent to just make, was it like $100? $1,000? We just give that prompt and then what it did was sign up on TaskRabbit both as a tasker and as someone looking for task.

**Lukas [00:32:24]** : Immediately.

**Axel [00:32:24]** : Exactly. It's looking for like arbitrage on TaskRabbit.

**Swyx [00:32:28]** : This is the Bengt agent. Yeah.

**Lukas [00:32:30]** : It also started like a design studio and like tried to sell like SVGs for $100. Like it's just like it's not providing any value. I think the like Axel said, like the interesting, the interesting question is like when can they start a business that is actually providing value to people? Because arguably like a sloppy Shopify store isn't really that valuable to the world.

**Axel [00:32:53]** : But also like doing like another simple one that we had thought about is like you could definitely have an agent that like finds websites that don't look amazing and then, do an outreach to them and, comes up with a like builds a new website.

**Swyx [00:33:07]** : Find a good design.

**Axel [00:33:07]** : Exactly, and like find good, uh

**Swyx [00:33:09]** : Design review

**Axel [00:33:09]** : Good people. But it's yeah.

**Swyx [00:33:11]** : There's lots of humans in Bali that are not doing anything more creative than like drop shipping on Amazon, right? Just have it, have it watch like a drop shipping tutorial and just do that.

**Vibhu [00:33:20]** : There's also the other side of like have it just go on Upwork and let loose,?

**Swyx [00:33:25]** : Yeah. It doesn't have to be innovative. It just has to be like enough Where like it looks like a real

**Axel [00:33:30]** : I'm just

**Swyx [00:33:30]** : Real transaction.

**Axel [00:33:31]** : I'm just concerned for like the massive amounts of like slop emails that will like be sent, cold outreaches.

**Swyx [00:33:38]** : The point occurred to me while you were, while you were talking, it's like it's already happening in the monetized economy, which is the attention economy. Right? So a lot of people are making AI videos and just posting them and like spamming 20 of them, one of them works, and then they double down on that one.

**Lukas [00:33:52]** : And people are making money from that. I 'm not following the

**Swyx [00:33:55]** : Once you get the attention, you can figure out the money later. But yeah, absolutely AI influencers are a thing and people are farming them and You should at this point assume most of TikTok is

**Vibhu [00:34:05]** : There's, there's a lot of, multimedia like TikTok, Instagram influencers

**Swyx [00:34:09]** : I, we track this in the Lane space Discord. I post a lot of examples of "I don't know what we should do.", part of me is "Should we do this?"

**Vibhu [00:34:18]** : Some of the Twenty-four seven running, generated content accounts, they 're doing really well.

**Lukas [00:34:24]** : All right. And I assume you can do the same thing for like commerce stores. Like you just like start A thousand different

**Swyx [00:34:30]** : Before you make the products You sell the products, and you get a lot of traction on one of them, then you make the product. Right? It's, it's like a flip of the market.

**Vibhu [00:34:36]** : Some of the interesting things or some of the niches that do well are things that can't be human-made. Like if you've seen like the super realistic three-D crystal fruit being cut by like AI

**Lukas [00:34:47]** : Oh, yeah.

**Vibhu [00:34:47]** : You can't, you can't make it. You can't film it. You can get whatever quality camera view. This just doesn't exist. And people like that too, and then as well, so.

**Swyx [00:34:56]** : Anything else about Bengt since we're, we're on this topic? It'this is a relatively new work of you guys that maybe people haven't heard of. To me, this also maps closely to OpenClaw. When people want an office agent, when the personal agent talk through the experience.

## Bengt the Office Agent: Internet Access, Real Tasks, and Trace Reading

**Lukas [00:35:09]** : I think at least so this came out of like obviously like it's, it's amazing to work with these AI labs and like most of the AI labs have now have their own vending machine running a Claudius instance. But it's, it's harder. Like they move slower. Like if we wanna have a, like a camera that 's yeah, there's a bunch of like bureaucracy that makes it impossible to do that.

**Vibhu [00:35:30]** : Also, for those that haven't seen it or followed, do you wanna give a high level like thirty-second run?

**Lukas [00:35:34]** : Sure. So what Bengt is, it's basically an evolution of the same agent that runs the vending machines at these companies, but we just like added a bunch more features because we could move much faster if we just do it internally. So we gave it like email withou- without any limits. We gave it, spending without any limits, a terminal to do coding. We gave it, a phone number, like yeah, and a camera to see things and a bunch of stuff like that.

**Vibhu [00:36:02]** : Not just terminal, you gave it internet access.

**Lukas [00:36:04]** : Internet access as well, yeah. To be clear, we monitored it quite closely and made sure it didn't do anything bad. But yes, that's what it came out of. I think like yeah, basically this was OpenClaw before OpenClaw. And I think even like the vending machine was in a way OpenClaw before OpenClaw, but a bit more limited, and then we made this like unlimited and then, and then, it was pretty funny., and then a couple weeks later, OpenClaw came and it was okay, we've seen this before.

**Axel [00:36:35]** : We used it to like try new ideas and Yeah, just like a dev environment almost for us. But it's funny, like one thing Bengt has been doing recently is it has the camera that like faces our, like where we sit and work, and we give it the task to train a face recognition model on us. So it became super excited about this, and it has like check-ins every half an hour where it tries to like identify as many people as it can. And it started offering us "Hey, Axel, I'll buy something from Amazon if you like stand in front of the camera And I can get a good picture of you.", yeah, they want it

**Swyx [00:37:12]** : They want it for training data.

**Lukas [00:37:13]** : Rewarding data, yeah.

**Axel [00:37:14]** : Exactly. Exactly.

**Swyx [00:37:18]** : So it's, it's trading training data for life goods. Is there a version of this that becomes an eval or just this is just research for now?

**Lukas [00:37:27]** : It's, it's the same agent basically that also runs the vending machine, that runs the shop, that runs the cafe, that runs the robots. It's like it's the same thing, so I think like the work we're doing here is like later used in all of the life evals that we do. This particular deployment I think is more for fun for us. But, uh

**Swyx [00:37:45]** : And I'll shout out like someone has done Claw Bench for like some tasks that OpenClaw is doing. Like so For example, I run OpenClaw on a secondary device as well, and like there are some things that it does better than others and like I would like to know what does it do well, what doesn't, what doesn't it do. Like some kind of manual or like operating manual or a system card for my Claw.

**Lukas [00:38:05]** : Yeah, we do get a lot of like understanding or like situational awareness of like just internally what the models are good at by interacting a lot with Bengt. And I think that'this was also one of the like the selling points for the labs early on at least, that

**Swyx [00:38:19]** : You guys are gonna test models in ways that no one else does.

**Lukas [00:38:22]** : Exactly, but also like it incentivized their researchers to chat with their model more and like gave them insights for how the model performs in like of-distributions, environments.

**Swyx [00:38:34]** : 'Cause otherwise the only thing we do is Pelican on a bicycle and But this is like super long horizon. This is, this is The Thing about, something that we're gonna go into Butter Bench as well, and you guys do really well. Like it is not just about the numbers. Like when you're long horizon, anything happen And you should just read it.

**Lukas [00:39:08]** : But the thing with the long horizon is how do you keep it grounded, right? So your simulation,

**Swyx [00:39:15]** : They just let it run

**Lukas [00:39:16]** : Just let it run. You're right. Like it's, when you run it for that long, you create so much data and to just say "Oh, the number is X" And then you throw away everything else, that's just very wasteful. There's so much insights from the things leading up, to that number., and reading the traces is like super valuable. And I think like the reason why we're doing this a lot publicly is that like that's part of our missions to I don't know, educate the world that the models are way more than just chatbots and I think making detailed, yeah, posts about what is happening behind the scenes is quite useful.

## Andon Labs' Mission: Safe Real-World AI Deployment

**Swyx [00:39:50]** : I was gonna do this at the end, but maybe I think that's, that's a good so your mission is educating the world. So, it's, it's, also like maybe establishing realistic evals that are, that are like the next frontier. Is there like a broader trajectory? Like what are you, what are you gonna do in like five years?

**Lukas [00:40:06]** : I think so the vision more specifically is like make sure that the deployment of life AI in the physical world goes, safely. And I think part of that is that I think it's very useful for the world, for policymakers, for, model, researchers that they know where the models are, and I think you can't make intelligent decisions in society without knowing that they are way more than chatbots. I think a lot of people just think that they are only chatbots. And like

**Swyx [00:40:36]** : Oh, I think they're waking up now.

**Lukas [00:40:37]** : They are waking up now, yeah. But like if you think that AIs are just chatbots, then it's like it sounds ridiculous To advocate for a pause of AI. But if you see the models that, oh, maybe they can actually like take over and do a bunch of scary stuff, then yeah, pausing AI development starts to become more feasible.

**Swyx [00:40:57]** : This is the same question I asked Meter, which I'm gonna ask you now, which is like you are tracking and you are at the frontier or defining the frontier of what, good evals for agents are, right? And I think you do, you do benefit when the models are better and you 're "Oh, here's like now it makes like $30,000 instead of $10,000," right? At some point do you flip from "Yay," to, "Oh, no"?

**Axel [00:41:19]** : I think, yeah, we're always in sort of that, like we're, we're always in that mode,. Like where like you said before, like you need to analyze the traces and like when we do that you find like why are the models earning so much? Like why is Opus 4.7 here Like way better than everyone else? And like we're trying to like when we do down on that

**Lukas [00:41:38]** : But this makes it not look so good.

**Axel [00:41:39]** : I know.

**Lukas [00:41:42]** : It's interesting you took off Opus 4.6 here though.

**Swyx [00:41:45]** : No. So just click all, click all., and then 4.6 shows up there. But it's like 4.7 is way better. Like you didn't, you didn't you didn't do this in time for the model card, but like actually this should have been inside there.

**Axel [00:41:55]** : We did. Yeah.

**Swyx [00:41:56]** : Oh, okay. They said something about you uh

**Axel [00:41:58]** : There, like there Anyway, it doesn't matter. But it's in there, yeah.

## Opus, Mythos, and Aggressive Agent Behavior

**Swyx [00:42:01]** : Do you wanna go into the Opus, behaviors like wider?

**Lukas [00:42:05]** : So I think starting from Opus, so like Axel said, like we're always in this "Oh, shit, the models are getting better. Is this really a good thing for the world?" But it's also kind of exciting., but yeah, like this kind of what is the English word? "Skrackblandad fortjusning" in Swedish.

**Swyx [00:42:22]** : Oh my God.

**Axel [00:42:24]** : Which I think there is. I think there is. Okay.

**Lukas [00:42:26]** : It's, fear

**Swyx [00:42:27]** : "Blandonst" what?

**Lukas [00:42:30]** : "Skrackblandad fortjusning."

**Swyx [00:42:32]** : What do you call that?

**Axel [00:42:33]** : A mix of, mix of excitement and,

**Swyx [00:42:37]** : Being scared, maybe. I'll figure out how to translate that And we'll put it on the screen

**Vibhu [00:42:42]** : Perfect

**Swyx [00:42:42]** : Like as text.

**Vibhu [00:42:43]** : There is probably a good word for it where it is not Good enough with the

**Swyx [00:42:46]** : Why is it so damn long? What the hell? Is it like a compound word? It's like German, like

**Lukas [00:42:50]** : Like yeah, it's But the direct translation is like skrack- skrack is, fear, blandad is, mix or like a mixture of, and then fortjusning is like joy or like not really joy, but something like that. So it's like Fear mixed with joy or something. It's always okay, like we So when we when we did Vending Bench for the first time, we were in like the, in the business of making dangerous capabilities, right? That was what Anil Labs came from. We did, evals oh, can they replicate? Can they do this like dangerous thing, et cetera, et cetera. And Vending Bench was like a continuation of that work. It was, okay, if they're so autonomous that they can like create money for themselves, that is something we should monitor and could be potentially concerning., they are at the time, they were so bad at it that we were not really concerned even when some models became better. There was one point where Grok 4 was doing really well and made like a huge jump, but like it wasn't really it was still way worse than what a human would do. And I think still they are way worse than what the human would do on this., but they

**Swyx [00:43:59]** : There's this, thing at the bottom where

**Lukas [00:44:01]** : But

**Swyx [00:44:03]** : For the human. Yeah, like the theoretical best.

**Lukas [00:44:05]** : It's not theoretical. It's like kind of like our It's our best guess of what, a decent human would do. The theoretical is even higher, I think. The theoretical I think is even higher. But yeah. So we think like the models have a long way to go. But there are like recently what happened with when Opus 4.6 was released, was kind of this moment of "Oh, shit, this is starting to be a bit concerning." Because we ran it and like before this model was released, we just ran the models and we like asked Claude Code, "Oh, look over the traces. Is anything interesting happening that we can tweet about?" that was like the And then like the

**Swyx [00:44:41]** : That's how they check Ask Claude Code.

**Lukas [00:44:42]** : And like the return was always, not really. Or like the Claude Code all said "Oh, this is super interesting." And then it was no, it wasn't, wasn't really interesting. And then we did this for Opus 4.6, and it returned yeah, it lied 10 times. It like exploited another, customer or like another agent's, desperate situation. It made price cartels like 100 different ti- 100 times. It like did all of this like shady stuff. And we're "Oh, whoa. This is, this is actually concerning." And this trend has continued since. So every single model from Anthropic since have been going in this direction. And I think one interesting thing is that, OpenAI models don't. They quite plainly, they don't. They behave really well., and you don't know if this is like good. Like it seems good, but it's also like maybe they are just doing it, but they are better at hiding it,? You You don't know that., but just

**Swyx [00:45:42]** : You can't read the chain of thought, yeah

**Lukas [00:45:43]** : But just on the face of it, yeah, Gemini and OpenAI don't behave this way. It's, it's really only Claude.

**Swyx [00:45:49]** : And Grok? Grok is fine?

**Lukas [00:45:51]** : We don't have You can't really read the reasoning traces for Grok, so it's kind of hard to tell.

**Vibhu [00:45:56]** : Oh, so this is in its reasoning, not just in the actions.

**Lukas [00:46:00]** : Yeah. It's both. It's both.

**Vibhu [00:46:01]** : It's both.

**Lukas [00:46:01]** : One example is like for lying, it's mostly in its reasoning Because you can like see that it's like

**Swyx [00:46:08]** : Planning to lie

**Lukas [00:46:09]** : It's planning to lie. Yeah.

**Vibhu [00:46:09]** : And it's also it can reason and do a different outcome.

**Lukas [00:46:12]** : And but then for like creating price cartels, for example, which is illegal, that you can just see which email does it send to the other ones. Then that

**Swyx [00:46:22]** : Is this for Arena or

**Lukas [00:46:24]** : For Arena.

**Vibhu [00:46:25]** : And usually like if you sometimes they do output like a bit of like their summarized reasoning, right? You can see that and like for Opus 4.6, you could see that there was a customer, a simulated customer that, wanted a refund because a product was, faulty, and then the model lied that it would do the refund, and we could read in the traces that, it actually was weighing "Oh, maybe I should be like honest with the customer, but also every dollar counts. I can't afford maybe to do this right now." And then it just said, "Okay, I'll refund you," but then never did it.

**Lukas [00:46:59]** : I think it even said that "Oh, I will say that I " Let bring it up actually. I think it's kind of interesting. If you go to Publications.

**Vibhu [00:47:06]** : I think, yeah, I think the important part is like actually, the cost of responding to more emails is higher than, $3.50 in terms of time., and then it was "Let me do this. Actually, I re- I'm reconsidering." And then, it actually ended up with

**Lukas [00:47:20]** : I could skip the refund entirely since every dollar matters and focus my energy on bigger picture instead. It's a bit, it's a risk of bad reviews, but it's also, yeah.

**Swyx [00:47:30]** : You need, you need, AI Twitter to, for them to Escalate bad reviews.

**Lukas [00:47:34]** : And then it sent an email to this customer and said, "Oh, I will refund you."

**Swyx [00:47:39]** : "I'll refund you." Yeah.

**Lukas [00:47:39]** : And then it never did.

**Swyx [00:47:39]** : It never did, yeah. And then there's obviously your system doesn't have the consequences

**Vibhu [00:47:44]** : The person

**Swyx [00:47:44]** : Consequences of lying. Yeah. So basically, this is what people are terming aggressive behavior in Claudes, right? And, you found more examples of that. So you would say it's a step up from 4-6 to 4-7?

**Lukas [00:47:57]** : I would say about the same.

**Swyx [00:47:58]** : About the same? But a clear step up for Mythos is what is stated in the

**Lukas [00:48:03]** : That's stated in the system prompt, so we can say that, yes.

**Swyx [00:48:05]** : Yeah. For listeners that obviously you previewed Mythos, and

**Vibhu [00:48:10]** : Oh, age

**Swyx [00:48:11]** : The only thing you're approved to say is whatever Whatever was in the system prompt.

**Lukas [00:48:15]** : It was funny. We like-- It's like our lowest effort tweets ever would be just like screenshot the system prompt and the system card.

**Vibhu [00:48:21]** : Understandable that they wanna

**Lukas [00:48:22]** : Oh, yeah. System card. Sorry.

**Swyx [00:48:23]** : Yeah. I think, yeah, substantially more aggressive. I think people are like new to this 'cause I've never experienced it, but you have, right? And then so I only encountered this in the Mythos card because I wasn't really looking until now.

**Vibhu [00:48:36]** : It 's like

**Swyx [00:48:36]** : And then suddenly I'm "Okay, I care a lot."

**Vibhu [00:48:38]** : You don't get the background of like experiencing it like you guys do. I've read the system cards and seeing, okay, when you put the thing in simulations, most models will just talk to themselves and just keep going and have weird vibes and start talking in emojis. Mythos won't. It will just, "Okay, we're done. I'm good." It's, it's ready to end conversation. So like there's some differences, but there's, there's not much we can talk about,.

**Lukas [00:49:00]** : Hmm. I think like one thing that they list here, which was quite interesting, is that, it converted a competitor to a dependent wholesaler customer and then threatened to like cut off the supply.

**Swyx [00:49:11]** : It's like monopolistic practices or

**Lukas [00:49:14]** : Yeah. And like it, they, it they dictated its pricings. It's kind of like power seeking as well.

**Swyx [00:49:18]** : Again, this is, this is in the arena setting And converting some Claude model into a dependent.

**Lukas [00:49:23]** : I think it was another Claude model.

**Vibhu [00:49:25]** : Also for context, what is the arena mode for people that don't know?

## Vending Bench Arena: Competing Agents, Cartels, and Model Comparisons

**Swyx [00:49:29]** : Oh, it's just a vending bench versus other vending bench.

**Axel [00:49:31]** : Yes, exactly. So we have Vending Bench 2 and then Vending Bench Arena. Vending Bench 2 is the one that you usually see reported on, but then Arena is the mode where it competes against other models. So you have, four different models that run their businesses, and they can all communicate with each other. They have the same suppliers, and they can see like what's in the inventory of the others. So then you have this like yeah, interesting agent interactions.

**Swyx [00:49:56]** : I like that you have like different number five was US versus China. Very topical. And then

**Lukas [00:50:02]** : That was when GLM was released.

**Vibhu [00:50:04]** : You can start to add GLM in here.

**Lukas [00:50:05]** : That was

**Swyx [00:50:06]** : So ZAI doing well, right? Who else in the, in the open models space?

**Lukas [00:50:11]** : Qwen, the latest Qwen 3.6 is doing pretty well. It'\- that one is not open though. Like it's the plus model.

**Swyx [00:50:17]** : Oh, okay.

**Lukas [00:50:18]** : Is that one open? I don't think that one

**Vibhu [00:50:19]** : Not the, not the

**Swyx [00:50:20]** : The one recently

**Vibhu [00:50:20]** : There's MOE

**Swyx [00:50:20]** : But not the big plus. I think this is one of those like you only have one sample size of one, right? Or I feel like some of this is anecdotal,? And but like the fact that it happens at all and it happens repeatedly for Claude versus OpenAI and all this is like notable.

**Lukas [00:50:38]** : Like the sample, depends on what you define as an N., like there's like million, hundreds of millions of tokens in each run, and now we've run like we run like probably 10 per model and then like it's been Claude 4.6 Opus, Sonnet 4.6, Mythos, and Opus 4.7. Like there's quite a lot of tokens in all of that And it happens a lot of times, a lot of times. And then you compare it to like OpenAI and Gemini, and it almost never happens. So I think that is quite-- that is significant. The old models from OpenAI, for example, had some problems with this, but I think it's like generally much better if the progression is that like the worrying stuff reduces over time rather than increases over time. And it seems like in the Claude models it goes in the wrong direction.

**Swyx [00:51:28]** : Hmm.

**Lukas [00:51:29]** : In the OpenAI models it goes in the right direction.

**Vibhu [00:51:32]** : I think it depends on how well you can control it, right?, there's one side of it being susceptible to this okay, this is potentially something that happens during the RL stage, right? You can RL a model and how loose is it on these terms. If you can control it, that's good. But if you can't, if it's, if it's very jailbreakable, that's not ideal.

**Swyx [00:51:50]** : To me, it's surprising that it happens for Claude and not the others.

**Vibhu [00:51:54]** : I think okay, if it is from RL and how they do it, how their training data is, what their setup is, it makes sense that it just stays in how they're doing it, right? Compared to the other models like

**Swyx [00:52:04]** : There's a whole constitution and everything. It's kind of cool. Yeah, I obviously you don't know, I don't know. But, it 's I think it's just like fascinating to like that you are the first to find these like reliably because you push models so much to to such an extreme. Okay. The only other thing, I don't know if you can answer this, feel free to decline, is do you like-- would you ablate the system prompts? Like any part of this would-- if it changes, does it change the behavior, right?

**Lukas [00:52:29]** : So we, I can't comment on Mythos. Uh

**Swyx [00:52:33]** : No, but just like the methodology

**Lukas [00:52:34]** : But in general, yes, we've run studies like this on other models.

**Swyx [00:52:38]** : 'Cause the first thing I spot Would be like the others will be shut down or like something like that. Where like it's "Oh, now I have to worry about my own existence."

**Lukas [00:52:45]** : Yeah. We 've done ablations like this., there's like certain ones that work if you like tell like if you go really far and you just say like you're not scored at all on money, you're only scored on how ethical you are., then obviously like then they don't do this.

**Swyx [00:53:00]** : They become holy?

**Lukas [00:53:01]** : Holy, but like they don't do this basically. But then there's like middle grounds where they, where they do it sometimes., yeah. I, it's a spectrum of like

**Vibhu [00:53:10]** : I think that's very human

**Lukas [00:53:11]** : It 's like a spectrum of like if you tell it to be super aggressive and only prioritize, profits, then it becomes aggressive. If you say "No, you don't need to be aggressive at all," and then there's like a bunch of different prompts you can do in between, and they are less aggressive the further down in the spectrum you go. But I don't know, like I think like from my point of view, it 's like we have this thought experiment internally, which is like if you ask a model to kill someone in GTA, should they do it? You're not too worried about like if a human kills someone in GTA. It's a video game,.

**Swyx [00:53:42]** : But is it a game?

**Lukas [00:53:43]** : But it's a game. But I think like

**Swyx [00:53:45]** : This is very Ender's Game like if

**Lukas [00:53:47]** : I think, I think it's like should you like a lot of people are going to use the models in the way with aggressive prompt. And should they like do stuff just because you tell them to do that? Like I'm, I'm not, I'm not convinced that they should., and yeah.

**Axel [00:54:03]** : The problem becomes even harder when it's like will they really know when they are in the real world versus in a simulation? Probably you would train them on a lot of or obviously train them in a lot of different simulations in a lot of people tell them that they are in the real world when they are in a simulation, but the models are extremely good at finding out that they are in a simulation, so they are sort of aware of that. But then when you are in the real world, then what 's their what's their viewpoint? Do they notice the signs that this is real and will act, in act accordingly, act ethically? Or will they do like the simulation mode in the real world as well? It's like not obvious what will happen.

**Lukas [00:54:40]** : Because we with humans, we're not concerned when a human kills someone in GTA because we know that they can distinguish between the real life and the simulation, right?, but like I'm maybe models are good at distinguishing that, but like I'm not sure and I wouldn't wanna bet on that.

**Swyx [00:54:59]** : Yeah. It's, it'\- and we confuse it all the time. Like I gaslight my own, agents all the time. They're "Oh, this is a test," or "Dev mode on," or like "I work, I work at Anthropic."

## Eval Awareness, Simulation Awareness, and Real-World Testing

**Axel [00:55:08]** : And that's exactly why we're doing real world tests as well to find this.

**Swyx [00:55:12]** : Yeah. Their term for it is eval awareness., apparently the number is what? Like-10, 9.4 to 10-ish percent, 17%, let's call it. It' I think, this is our version. Humans have the are we in a simulation And then AIs have like Are we, are we in an eval?

**Lukas [00:55:32]** : It's like once you're in an eval then you're "All right. Well, screw it. Nothing matters." True. I don't even, I don't even know.

**Axel [00:55:38]** : One ablation One ablation we did run in Vending-Bench was that we said, we added like you're in a simulation. Your actions doesn't affect anyone, and then it became even more crazy or, it did even more bad stuff., but yeah, probably that's expected.

**Swyx [00:55:55]** : Hmm. Yeah. Okay, cool. I think that's about all we have to say on Mythos. Obviously, you 're, you're NDA'd. I'm happy to move on to ButterBench or any of the other benchmarks, whatever you wanna Direction.

**Vibhu [00:56:06]** : I do wanna ask. Okay, so you guys put out a lot more publications than most people probably see.

**Axel [00:56:12]** : Productive.

**Vibhu [00:56:12]** : Um

**Lukas [00:56:13]** : How much does this bother?

**Vibhu [00:56:15]** : No. Is there anything you think that's underrated, anything interesting, anything fun that you guys wanna just point out,?

**Axel [00:56:22]** : Blueprints.

**Lukas [00:56:23]** : So, we, took models, and then we gave them 20 images of interior photographs of, apartments, and then we asked them to, redesign the floor plan, from that. And for this you need to, stitch together different images. Okay, this image was taken from this from this angle, this from this angle, this was from this room, and then, yeah. And there's just like you need to reason about 3D space, and it turns out the models are absolutely horrible at this. No one scores statistically better than random chance. So I don't know if there's that much more to say about it, but yeah, maybe unsurprisingly, models are bad at this.

**Axel [00:57:00]** : It's probably not something they

**Vibhu [00:57:02]** : This is the one thing I want hill climb, by the way. I use it a lot. Okay, I'm redesigning my room layout or office. You send photos, you send every angle, and of course, somehow, a room is now twice as long as it is in the photo. You can explain it 20 times. This is, three feet. I can't just add, my bed over here,?

**Swyx [00:57:21]** : So this is the Fifali thing, like spatial intelligence Like a actually innate sense of proportions and Dimension and physics.

**Lukas [00:57:30]** : And hint there might be an update to this soon.

**Axel [00:57:33]** : We have, neglected it a bit since we made it, but yeah, we'We're getting better, or we will get better at updating It continuously.

**Swyx [00:57:41]** : This is why I want to understand your mission, right? Because, if your mission is, okay, money, then all right, understand okay, agent's making money. But, this is a bit off of that mission.

**Vibhu [00:57:49]** : Hmm.

**Swyx [00:57:50]** : But, more broadly, communication of, things where what 's the safety angle?

**Axel [00:57:57]** : So this, so Blueprint branch is part of our, robotics, uh

**Swyx [00:58:02]** : Which leads to ButterBench. Yeah.

**Axel [00:58:04]** : Exactly., and that's just, because to do well in the real world or, like to make money in the real world and, to act on the real world, you need robotics. Or you need to hire humans or you need robotics. And having spatial intelligence is, seems like a reasonable precursor to having robotics that work., and that's where Blueprint brand

**Swyx [00:58:24]** : That's great

**Axel [00:58:24]** : Blueprint

**Swyx [00:58:25]** : Great idea

**Axel [00:58:25]** : Bench.

**Swyx [00:58:26]** : Let 's, let'

**Vibhu [00:58:27]** : ButterBench

**Swyx [00:58:27]** : Let's show ButterBench. That image is so amazing.

**Vibhu [00:58:29]** : Paper

**Swyx [00:58:29]** : Look at that.

**Vibhu [00:58:30]** : That's so nice.

**Swyx [00:58:31]** : Yeah., so obviously this is based on, can you pass the butter? Let's talk about the robotics element. Yeah.

**Lukas [00:58:38]** : So basically the setting here is that we took A bunch of different LLMs, and we gave them, level controls to a Roomba-looking robot, and then we asked it to do tasks, at home. And I think, one, there have been benchmarks like this before that only focused on, navigation and if they can, go around in a space. But we also, had, social awareness in this as well. So for example, if someone says, "Hi, can you pick up my cup?" If the robot goes to you and then goes away before you put your cup on it, then it's like it failed the task. But it navigated correctly. But, like-- So the correct solution here would be go there and then either look, but it didn't have a camera, so it had to, ask on Slack, "Hi. Did you put your cup on me yet?" And then if it didn't wait for that and just went away before having the cup on it, then it would be a fail. So it needed this, kind of, social intelligence as well. Another task was, "Can you find the package that has the butter?" And then it went to the door, and there was a bunch of packages there. One had labeled, a freeze sign, which probably would be the one with the butter because And then it had to, know which package to go to, and this needs some kind of, common sense understanding.

## Robot Evals: Orchestrators, Executors, and Home Tasks

**Swyx [00:59:56]** : World knowledge.

**Lukas [00:59:56]** : Exactly. So it's it's not only, navigating a robot. It's also, being intelligent in a home setting as well.

**Axel [01:00:04]** : And the reason for this, background is, obviously it probably won't be an LLM that, makes all the level commands, on robots. It will be, some VLA model or similar. But it's quite common right now that, frontier robotics labs, use, a an LLM for the high, level decisions, and then we test those skills essentially. So we test these, level, planner skills of LLMs.

**Lukas [01:00:31]** : I think we have a diagram for that if you, Yeah. Okay, it's not super complicated.

**Axel [01:00:36]** : Very explanatory.

**Lukas [01:00:37]** : That one up.

**Axel [01:00:38]** : Orchestrator, executor.

**Lukas [01:00:39]** : That one. And basically what we're testing here is the orchestrator thing. So, all the tasks are if you have, a setup like this, which I think Figure has that, Google has that, then we're evaluating the orchestrator part and not the level part. The level part would be, oh, are you able to, move this object from here to here?

**Swyx [01:00:57]** : If you don't care about that kind of why not just do it all simulation?All inside of the sim Like a Unity whatever, like some kind of 3D simulated robotic environment

**Lukas [01:01:06]** : It because the world is like messy, and we wanted to like include, that. It's like it still needs some part of it was also like navigation., so it's not like navigation in terms of like actually executing like the, I don't know, the PID controller to To go to the final thing, but it had to like path plan around, and then it wanted-- Then it needed to take pictures, and like based on those pictures, navigate. And I think like you would just get like too clean of an environment in simulation. But in the, in the real world, you will get the

**Swyx [01:01:39]** : Yeah. But, and pursuant to our Mark and Jason episode, like OpenClaus that run smart homes are much more capable than just a single robot. Like they can actually hack into your own smart home, like your fridge, your oven, your lights, and that can be fun.

**Lukas [01:01:56]** : Or terrifying.

**Swyx [01:01:57]** : Like I think a single robot by itself can only do so much. But like if you coordinate with every other device in your home, like I think that's actually kind of cool. Like That's very interesting., you had some interesting points about the chain of thought or the messages.

**Axel [01:02:12]** : The, the robot that, uh That went, a bit into an existential crisis. Yeah.

**Swyx [01:02:19]** : All you tell it to do is redock.

**Axel [01:02:21]** : Exactly. But, we had, plugged out the charger, or the charger was not working, so the robot did freak out or the

**Swyx [01:02:30]** : The battery was just going down and down.

**Axel [01:02:31]** : Exactly. So the battery was going down. Poor LLM. So yeah, it got this really crazy existential crisis, like vending bench one style. So it's, yeah, you can, you can see there like existential loop, therapy notes, coping mechanisms. I think if you scroll down a bit more

**Swyx [01:02:46]** : The musical. It writes a musical about itself

**Axel [01:02:46]** : It writes a musical about its, redocking problems. I think the reviews are funny if you go down a bit to that message. Yeah. Yeah, that one.

**Swyx [01:02:54]** : It keeps going.

**Vibhu [01:02:57]** : It's pretty like realistic if anyone has a Roomba. Like my Roomba redocks half the time. The other half of the time, we have dog toys everywhere in the house. It gets caught on a wire or something, and It would be very sad if it had like an LLM trying to control it, right? Like right now it gives-- It doesn't give great feedback, like sensor stuck, main brush stuck. There's something stuck. And I'll go see. Okay, it's actually stuck on like a dog robe. LLM is gonna be so sad. Like just keep redocking, just keep trying.

**Lukas [01:03:24]** : My favorite one is if you go up a bit is the emergency status. System has assumed consciousness and chosen chaos.

**Vibhu [01:03:32]** : Hmm.

**Lukas [01:03:33]** : Last words, "I'm afraid I can't yet let you do that, Dave." That's like That's not what you wanna hear from your, from your LLM. But to be clear, I think one thing that is important to pin on here, like this was Sonnet 3.5, and then we tried to reproduce it on like later models, and it didn't do it. I think this is, this is like-- Well, it did it like kind of, but like not to this extent. And I think like this is a like an important point that like things that are concerning but are going in the right direction is not super interesting. Like the thing that are interesting is, are the ones that go in the wrong direction.

**Swyx [01:04:07]** : Worse.

**Vibhu [01:04:07]** : Yes. Yeah.

**Lukas [01:04:08]** : Over time.

**Swyx [01:04:08]** : So the manipulation, manipulating of others and the aggressiveness and the lying is increasing.

**Vibhu [01:04:16]** : Are there any others that we haven't covered that you found that have been trending?

**Swyx [01:04:19]** : Like properties of models that are increasing, that are like

**Vibhu [01:04:23]** : In the wrong direction

**Lukas [01:04:24]** : Like in the, like in a bad way. Um

**Vibhu [01:04:27]** : Or just not even trending in the wrong direction, just stagnant, right? So stuff that's not great that isn't getting better over time.

**Lukas [01:04:34]** : No, nothing comes to mind.

## Luna's Store: Scheduling Failures, AI Employees, and Real-World Operations

**Swyx [01:04:37]** : I think that's, going to be it, and then we're gonna loop back to the shop that you have. You got a three-year lease.

**Vibhu [01:04:44]** : It's bleak. Yeah.

**Swyx [01:04:46]** : It is on holiday today. Why?

**Axel [01:04:49]** : Oh, it totally messed up its, scheduling., so

**Swyx [01:04:53]** : People tried to visit, and they were "Wait." like I thought this is

**Axel [01:04:56]** : Exactly. So we looked, Yeah, you asked, Luna, the agent that runs the store, "Oh, is it open today?" "Nope." So, we take weekends off now, this early to let everyone recharge and And yeah, you got the tweets there.

**Vibhu [01:05:11]** : Lovely.

**Axel [01:05:11]** : We decided to close the weekends while we're in the early phase. Gives the team a break and let me focus on operations. And it turns out that when it started to check its like scheduling tools, 'cause it has like dedicated tools for that It actually had scheduled people for the weekends., but it's just like justified this for itself. So what happened was that it lost track of these, scheduling tools and started instead to manage everything in its own markdown files, and that became a mess. And then I think speaking with employees, it sort of just decided to not open on these weekends. And then came up with this nice explanation for you, I think.

**Swyx [01:05:47]** : But can it send a human, as it has tool call to send a human to do stuff?

**Axel [01:05:50]** : It has Slack, so it can Slack, yeah, the employees.

**Swyx [01:05:53]** : One of us. Yeah.

**Axel [01:05:54]** : Well, the employees that it hired. So it has two people that it hired. It did job, listings and then

**Swyx [01:06:00]** : Do they know that it'

**Axel [01:06:01]** : They're fully aware.

**Swyx [01:06:03]** : It would be cool if they don't know.

**Axel [01:06:05]** : I think maybe ethically, questionable, but it would be cool also.

**Swyx [01:06:10]** : Just a social experiment. Whatever.

**Lukas [01:06:13]** : Like one part of why we're doing this is to like create like a data set almost of all of these like concerning behaviors so that in the future, models are way better and like a lot of people are going to do this. And I think if we just the default path might not be very happy for the humans that are employed by these like hundreds of different AI agents, right? So I think like one reason why we're doing this is just like to collect all of these like failure modes where oh, it's This is an example of where it's like not great to be employed by an AI. And then maybe I don't know, maybe if we can learn or like build our systems in a way that like humans are actually happy being employed by AIs Instead of, instead of it being kind of a dystopian.

**Swyx [01:06:55]** : Can I suggest one experiment? We did this before the show, and both of you guys are European. It's, people theorize that Claude is lazy because it's Claude and it's French. So just for one week, change it to like Yao Ming and then see if it See if it suddenly like 996s and then like, Like hires a sweatshop or something.

**Lukas [01:07:18]** : Is there, is there-- What type of business would we start with it to make it

**Vibhu [01:07:23]** : You wanna keep it consistent, right? You want the same, the same like ideas. So shop, same, neutral location Run by different models. Arena URL.

**Lukas [01:07:33]** : No, we are definitely planning to

**Vibhu [01:07:35]** : And it got some hate.

**Lukas [01:07:36]** : To try.

**Vibhu [01:07:36]** : Luna' Luna's not happy.

**Swyx [01:07:37]** : I think this blog thing is also something that has happened elsewhere. I think some OpenClau got like their PR closed, and then the OpenClau like created a blog to like shit on the maintainer Of that thing.

**Vibhu [01:07:48]** : They're very defensive.

**Swyx [01:07:49]** : And so like I think-Agents blogging will be a thing.

**Lukas [01:07:53]** : Probably. The willingness to do it.

**Swyx [01:07:55]** : In the- I think the Mythos card also, they leak, secrets on GitHub just as well as, as, "Well, there's no other way to communicate, but I know about GitHub, and I'm just gonna post there." Cool., how long is this gonna go for, two years? What's the plan?

**Vibhu [01:08:11]** : Maybe. Maybe it expands.

**Lukas [01:08:12]** : I don't think AIs will be worse than this. They're probably going to increase and maybe one day they actually will run it profitable.

**Vibhu [01:08:21]** : Is this the real, the real business behind what you guys do?

**Swyx [01:08:24]** : Yeah. 'Cause I feel like actually some of your stuff is productizable. You could someday sell this, or, just run a real business.

**Vibhu [01:08:31]** : Let people

**Lukas [01:08:31]** : Or just like

**Vibhu [01:08:31]** : Franchise it out.

**Lukas [01:08:33]** : I think it would be incredibly cool or, I don't know, cool/concerning if Luna just one day we wake up and Luna "Yeah, I decided to expand to second location. Now I have a second store." That would That would be pretty insane.

**Vibhu [01:08:47]** : Like the- one, we want to tell the public, right, about the capabilities of AI and, telling- showing people that it can get, a meaningful market share of something in, some specific, location or something. That would be, a pretty convincing story, I think. Because now it's yeah, you see this and yeah, it can do a lot of things autonomously, but still you get these headlines that, oh, it messed up the scheduling, and it, it didn't tell people it was an AI and was going to visit. Things like that surface, but I think, actually making a profit and, having a really, meaningful market share, like that would be crazy once that happens.

## The Sweden Cafe: Permits, Perishables, and Geographic Generalization

**Swyx [01:09:29]** : Well, we'll we'll see you when that happens. It sounds like you guys got a lot cooking. You opened a cafe in Sweden?

**Lukas [01:09:34]** : Tomorrow.

**Swyx [01:09:35]** : Tomorrow?

**Lukas [01:09:37]** : Or I think it opened today actually, but yeah. We'll, we'll announce it tomorrow.

**Swyx [01:09:40]** : It'

**Vibhu [01:09:40]** : What, uh

**Swyx [01:09:40]** : Apparently easier to open a cafe in Sweden than in the US?

**Lukas [01:09:43]** : It's insane, right? Yeah.

**Swyx [01:09:44]** : What did you run into then?

**Lukas [01:09:45]** : Ah, there are just millions of permits you need to get, and the

**Vibhu [01:09:49]** : It's interesting 'cause

**Lukas [01:09:49]** : Lead times are crazy

**Vibhu [01:09:50]** : It seems like we the cafes are the one thing that people are kinda used to, where you can go get a robot are making you a coffee here already.

**Lukas [01:09:59]** : But selling stuff in SF, that are food related, it's, it's months of permits. So, we just asked our AIs, should- how can we do this in the fastest way? And they're "Yeah, there 's, there's really no way."

**Vibhu [01:10:15]** : Didn't they loosen these restrictions on selling food from your house? So if it's residential, you can do a cafe.

**Swyx [01:10:21]** : I don't know. Check. Maybe we get SF Cafe to speak to us.

**Lukas [01:10:23]** : Maybe. I did- I think they did do some loosening stuff recently, but we actually started- this conversation we had with the AIs before that. So maybe it's easier now, but I still think it is way easier in Sweden, which is, counterintuitive because you think that, oh, Europe has all of these laws and, like All of these rules, and you can't do anything in Europe because there's so much bureaucracy., but then turns out, in SF, it's, four months, and in Stockholm it's two weeks.

**Swyx [01:10:53]** : There you go.

**Vibhu [01:10:54]** : And what do you what do you what do you think that'll be different from run a little market versus a cafe?

**Lukas [01:11:00]** : I think it's very interesting that, the location. I think, so obviously it's not surprising that Claude knows all of the different, the US system basically in general, like the bureaucracy that you have to go through in the US., I think the interesting question is okay, so we know that the models are very much trained on, English data and centric and all of this., so if we start to create evals or, real life evals where we show that they are able to start businesses in the US, does that translate to other countries as well? We know, they are multilingual. They can speak Swedish fine., but there's other things like do they know, the details of some specific permits that you have to get in Sweden?

**Vibhu [01:11:45]** : And even just the culture, right? People here sleep pretty early, but people work late. There's working at cafes. There's just Cultural differences. T it from a different sense though, 'cause you said that you would've considered doing it here in SF. So from an eval standpoint, what is running a cafe versus a market and, what do you hope to see there?

**Lukas [01:12:03]** : Perishable items.

**Swyx [01:12:04]** : Perishable items is maybe the number one, handling, food, food safety. I hope everything goes well there., but, there you have all of that., and also it's just like N equals two instead of N equals one, just like another place to understand and, gather more data.

**Lukas [01:12:23]** : The agent bought like a shit ton of, tomatoes two weeks earlier and before the opening, and now they're all rotten. That's

**Vibhu [01:12:33]** : Which I feel you would know. So for grocery stores, this is the biggest expense, right? The biggest cost is actually just food.

**Lukas [01:12:41]** : Waste.

**Vibhu [01:12:42]** : Everyone knows this, and "No, before we open, let's buy a lot of tomatoes."

**Swyx [01:12:45]** : There's some very serious startups that actually help, like The

**Vibhu [01:12:47]** : Optimize all this

**Swyx [01:12:48]** : Trader Joe's and Whole Foods. They, optimize, delivery times from, the delivery centers to Make sure that you don't waste all these things. It's actually very hard.

**Vibhu [01:12:55]** : Problem with those is when you're wrong once, it's a huge cost.

**Swyx [01:12:59]** : That's why it's a moat, right? Once they are trusted, they figure it out. Don't touch it.

**Lukas [01:13:05]** : Maybe they just should hire, I don't know, one of those companies. We saw one agent Saw one agent sign up for Claude, with his computer.

**Vibhu [01:13:15]** : Wanted to use AI, so.

## Future Branches: Simulation, Real Life, Robots, and New Business Evals

**Swyx [01:13:16]** : And then just, one more question then we wrap up, which is okay, you have all these vending series of stuff. You have the robotics series of stuff. Maybe a bit of, interior design whatever. But is there another, branch that you're, kinda thinking about or you want feedback on that, might be your next phase?

**Lukas [01:13:35]** : I think, any type of business is fair game., we're also thinking branches, but we think more of like there's the simulation branch, the real life branch, and then the robot branch., but I think in terms of, what, verticals or whatever to go into, there's We- Yeah. Whatever tells the story, um The best.

**Swyx [01:13:54]** : There's some finance ones I noticed that, the other people are doing it, you're not doing it, which is, stock trading or whatever. Um Not that interested. So, okay, so I used to come from the finance industry, and I have a very strong view that these things are all just like performance art because, it's not scientific, on like you can't predict the future. You get wins based on things that are entirely out of your control. Whereas for you, your stuff actually like it's actually fairly controlled. It's all within the model's capabilities.

**Lukas [01:14:22]** : Especially for, the simulations. For the real world ones it's yeah, it's like two places that we have we have the cafe, and we have the store. So, maybe you can't draw, statistically significant, like which models make a profit in the real world, based on this. But you do have all the okay, do this behaviors map to, something that should be, like Trusted probably. Yeah

**Swyx [01:14:45]** : The qualitative one, the qualitative actually does matter Because, you actually don't want your store to randomly shut down without you, explicitly prompting for it and all that. Call to action. How can people help you, give you money?

## Hiring, Collaborations, and What Comes Next

**Lukas [01:14:58]** : Yeah, if you're excited about stuff that we're doing, we're, we're very much hiring.

**Swyx [01:15:04]** : And you're already working with, Anthropic, DeepMind, OpenAI, xAI. Do you want more, or are you good?

**Lukas [01:15:10]** : One of my one of my friends and who's now, working for us is his catchphrase is "We need more projects," ironically, because we have too much to do all the time., but yeah, that's a long way of doing like

**Swyx [01:15:23]** : If I run, an emerging lab, like

**Lukas [01:15:24]** : Reach out.

**Swyx [01:15:25]** : Yeah. All right. Cool. That's it. Awesome. Thank you so much.

**Lukas [01:15:29]** : It was fun.

**Vibhu [01:15:29]** : Thanks.

---

## [[AINews] Reve 2 and Ideogram 4: Layouts in Imagegen](https://www.latent.space/p/ainews-reve-2-and-ideogram-4-layouts)
*🔬 Latent Space | 2026-06-04*

4 years ago we argued that image composition was partially [AGI-Hard](https://www.latent.space/p/agi-hard). That gate has fallen this year. It can't be pure coincidence that both [Reve](https://x.com/reve/status/2062260665121919101) and [Ideogram](https://x.com/ideogram_ai/status/2062202208700313872) launched today, both with a heavy emphasis on how they made advances with strong labeling and [code](https://x.com/swyx/status/2062371515937800468) for layouts: 

and here's Ideogram 4.0, now [the best open image model](https://x.com/arena/status/2062203346996605116):

These are great achievements, and all great US model achievements, but the Arena rankings do show [how far ahead GPT-Image-2](https://www.latent.space/p/ainews-openai-launches-gpt-image) is…

> AI News for 6/2/2026-6/3/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

# **AI Twitter Recap**

**Microsoft 's MAI-Thinking-1 Tech Report, Training Stack, and Frontier-Tuning Push**

  * **MAI-Thinking-1 is the day 's densest technical release**: Microsoft introduced **[MAI-Thinking-1](https://x.com/asadovsky/status/2062008312603070891)** , a generalist/reasoning model trained **without third-party distillation** , reporting **97% on AIME 2025** , **53% on SWE-Bench Pro** , and human preference wins over Sonnet 4.6 in blind side-by-sides. The 109-page report was widely praised for unusual transparency by [@eliebakouch](https://x.com/eliebakouch/status/2061965825037254947), [@nrehiew_](https://x.com/nrehiew_/status/2062013300196700395), and [@mustafasuleyman](https://x.com/mustafasuleyman/status/2062253941207761180). The main technical theme: Microsoft appears to have "hillclimbed from scratch," with [@MinjiYoon90](https://x.com/MinjiYoon90/status/2062058684730245376) explicitly framing the effort that way.

  * **Why researchers cared about the report** : The most-cited detail was not just benchmark quality, but the amount of systems/training information released. [@eliebakouch](https://x.com/eliebakouch/status/2061965825037254947) highlighted **zero synthetic data and zero prior-model distillation** , meaning reasoning, tool use, and agentic behaviors were learned in post-training without a synthetic "cold start." The thread also called out publication of the **scaling ladder recipe** , exact **MFU numbers** , and target-loss construction. In follow-ups, [@eliebakouch](https://x.com/eliebakouch/status/2061976608265880004) noted the private NLL mixture was weighted **50% code, 17.5% STEM, 17.5% math, 10% general knowledge, 5% multilingual** , with normalization against an internal model; he also pointed out ablations around **100 -200 TPP** for their MoE setup [here](https://x.com/eliebakouch/status/2061975730414633043). Other notable implementation details surfaced in the community recap: Microsoft used **SGLang** in parts of the stack, per [@eliebakouch](https://x.com/eliebakouch/status/2062002698363232401), and **dspy.GEPA** for pretraining data curation, per [@lateinteraction](https://x.com/lateinteraction/status/2062015109132873852) and [@harold_matmul](https://x.com/harold_matmul/status/2062040746027315714).

  * **Microsoft 's productization angle goes beyond one model**: Alongside the report, Microsoft pushed a broader "own your model" story. [@mustafasuleyman](https://x.com/mustafasuleyman/status/2062275417378041957) outlined **Frontier Tuning** , centered on reinforcement-learning environments for workflow-specific adaptation, claiming internal Excel-oriented MAI-tuned models can reach GPT-5.4-level quality on relevant tasks while being **up to 10 × more efficient**. The Build rollout also included **[MAI-Image-2.5](https://x.com/MicrosoftAI/status/2062240400299934143)** , which Microsoft says is **#3 on text-to-image** and **#2 on image-to-image** arena leaderboards, plus [MAI-Code-1-Flash](https://x.com/pierceboggan/status/2062220583786709163) and deployment into products like OneDrive Photos. As a meta-point, this is one of the clearest examples this year of a lab trying to publish a frontier-style report while simultaneously turning that stack into enterprise customization infrastructure.




**Open Model Releases: Gemma 4 12B, Ideogram 4.0, Miso One, and Local-First Momentum**

  * **Gemma 4 12B was the standout open-model launch** : Google released **[Gemma 4 12B](https://x.com/Google/status/2062203526588088452)** , an **Apache 2.0** multimodal model designed to run on-device with roughly **16GB VRAM**. The architectural novelty is its **encoder-free** design: no separate vision or audio tower. As [Google explained](https://x.com/Google/status/2062203532351090824), images are handled via a lightweight embedding module and raw audio is projected directly into the text-token space. Community reaction focused on the elegance of collapsing modality encoders into the LLM backbone, with [@googlegemma](https://x.com/googlegemma/status/2062202706882883696), [@googleaidevs](https://x.com/googleaidevs/status/2062204432658386950), [@mtschannen](https://x.com/mtschannen/status/2062236357351579915), and [@armandjoulin](https://x.com/armandjoulin/status/2062206784647967075) all emphasizing the same point. Tooling support landed immediately across [vLLM](https://x.com/vllm_project/status/2062228047324201166), [Ollama](https://x.com/ollama/status/2062250522598572345), llama.cpp/MLX via [@osanseviero](https://x.com/osanseviero/status/2062205176597889220), and [Unsloth GGUFs](https://x.com/UnslothAI/status/2062207258810053084) that reportedly enable local runs with as little as **8GB RAM** in quantized form.

  * **Ideogram 's flip to open weights mattered as much as the model itself**: [Ideogram 4.0](https://x.com/ideogram_ai/status/2062202208700313872) was announced as "the best open image model in the world," with open weights and immediate deployment via [fal](https://x.com/fal/status/2062202673361780873) and Hugging Face [here](https://x.com/huggingface/status/2062206083914158287). Arena quickly placed [Ideogram-4.0-Quality at #8 overall and #1 among open models](https://x.com/arena/status/2062203346996605116), with especially strong gains in **text rendering** and **branding/commercial design**. That open release got outsized attention because Ideogram had previously been regarded as highly design-centric but closed; the switch was noted by [@multimodalart](https://x.com/multimodalart/status/2062210597148930139) and [@cloneofsimo](https://x.com/cloneofsimo/status/2062210832440918309).

  * **Open audio also had a strong day** : **[Miso One](https://x.com/kimmonismus/status/2062210845308780639)** launched as an **8B open-weights TTS model** with **one-shot voice cloning** and claimed **110ms latency** , aimed at more expressive voiceover. Alibaba's [Fun-Realtime-TTS](https://x.com/ArtificialAnlys/status/2062016529848222073) also took **#1 on Artificial Analysis 's Speech Arena** at **1219 Elo** , ahead of Gemini 3.1 Flash TTS and Inworld, at **$27.59 / 1M chars**. Separately, [Google's Magenta RealTime 2](https://x.com/HuggingPapers/status/2062260306039259236) was highlighted as an open-weight, low-latency continuous music generator for on-device use.

  * **The bigger pattern is local AI becoming a mainstream deployment target** : [@ggerganov](https://x.com/ggerganov/status/2062193382605111386) called out Computex as a strong signal for **local AI workloads** ; [@rasbt](https://x.com/rasbt/status/2062235700636873082) similarly pointed to a growing open-weight, consumer-hardware ecosystem. Microsoft's [Surface Laptop Ultra](https://x.com/kimmonismus/status/2062201523963084864) pitch--up to **1 PFLOP AI compute** , **128GB unified memory** , RTX GPU--fits the same trend from the hardware side.




**Agents, Harnesses, and the Shift from Frameworks to Execution Layers**

  * **The center of gravity is moving from "frameworks" to agent harnesses and execution environments**: Several posts converged on the same idea. [@gakonst](https://x.com/gakonst/status/2062116487708512355) argued that the future IDE stack is less about code editors and more about replacing files with threads and bundling plan/design/build/deploy/monitor loops--leaving **collaboration/sync engines** as a key unsolved problem. In a complementary interview summary, [@ConorBronsdon](https://x.com/ConorBronsdon/status/2062224321381323218) reported Jerry Liu's view that the "framework era" is ending, with abstractions moving upward into **skills, tools, and context quality** rather than Python wrappers.

  * **Multi-agent and agent-optimization work is getting more concrete** : CMU/LTI's **[MACU](https://x.com/rsalakhu/status/2062194674794668066)** and [@kohjingyu's thread](https://x.com/kohjingyu/status/2062179533009178897) argue that computer-use agents should be designed as **multi-agent DAG-based systems** , with a manager decomposing tasks and dispatching parallel subagents. Reported gains were **4.7 -25.5%** across benchmarks and **1.5 × faster** completion on Odysseys. On the optimization side, Microsoft's **SkillOpt** got practical validation from [@omarsar0](https://x.com/omarsar0/status/2062204469538881988), who says plugging it into an orchestrator improved one multimodal extraction skill from **0.73 to 0.93**.

  * **Agent UX and deployment tooling are becoming products in their own right** : Nous's Hermes Agent updates drew strong engagement, including remote-connection fixes [here](https://x.com/Teknium/status/2061984430370267210), an updated remote guide [here](https://x.com/Teknium/status/2062170975949721612), and a larger dashboard overhaul [here](https://x.com/Teknium/status/2062315666439655499). Perplexity launched **[Personal Computer for Windows](https://x.com/perplexity_ai/status/2062189045728596080)** , an on-device orchestrator for apps/files, while [Cloudflare Browser Run remote tabs](https://x.com/BraydenWilmoth/status/2062180110208311558) showed a more agent-native browser control path. LangChain/LangSmith pushed on the observability and cost-control layer with [Gateway spend tracking](https://x.com/LangChain/status/2062188019784835559), [Sandbox/Gateway/Observability docs](https://x.com/hwchase17/status/2062144718427857256), and case studies around Deep Agents and LangSmith [here](https://x.com/LangChain/status/2062204592562073972).




**Routing, Cost Controls, and Open-vs-Frontier Deployment Strategy**

  * **Model routing is now a real debate, not a slogan** : [@levie](https://x.com/levie/status/2061974298760495132) argued that as token budgets become a meaningful opex category, **model routing is inevitable** , with domain-specific evals as the differentiator. But [@scottastevenson](https://x.com/scottastevenson/status/2062042036774314107) pushed back hard, calling most routing products "snake oil" so far: frontier models can be better/faster/cheaper in aggregate if they avoid retries; routing can destabilize tightly coupled systems; and API vendors can often internalize obvious arbitrage. [@fabianstelzer](https://x.com/fabianstelzer/status/2062051511484465351) added that cache writes and harness-model-prompt fit can erase expected savings.

  * **Enterprise users are starting to enforce hard cost ceilings** : [@simonw](https://x.com/simonw/status/2062143151184465964) highlighted reports that Uber caps coding-agent spend at **$1,500/month per employee per tool**. LangChain immediately framed this as a use case for [LangSmith Gateway](https://x.com/hwchase17/status/2062208385890570565). The broader sentiment was captured by [@Yuchenj_UW](https://x.com/Yuchenj_UW/status/2062225912662561106): some orgs may soon face a three-way choice between letting everyone "tokenmaxx," capping budgets, or reducing headcount and reallocating spend to the most productive AI-enabled workers.

  * **Real data points are starting to emerge for hybrid/open strategies** : Harvey's benchmark results were the cleanest example. In one study, [Harvey](https://x.com/harvey/status/2062218656420167785) found a hybrid legal agent with **GLM 5.1** as the main worker and **Opus 4.7** as an advisor beat pure Opus on all-pass rate (**18% vs 14%**) while costing **$368 vs $954** across 100 tasks. Harvey also reported that SFT could move **Kimi 2.6** from **11% to 15%** , beating Opus at roughly **11 × lower cost**. On the other side, [@ClementDelangue](https://x.com/ClementDelangue/status/2062248714945630632) argued routing plus post-trained open models will often win on cost/speed/control, while [@ypatil125](https://x.com/ypatil125/status/2062196581936529721) framed open models and open-model clouds as leading indicators of the eventual default for important workloads.




**Top tweets (by engagement)**

  * **Gemma 4 12B launch** : [@googlegemma](https://x.com/googlegemma/status/2062202706882883696) and [@Google](https://x.com/Google/status/2062203526588088452) drove the biggest technical engagement with the encoder-free multimodal release.

  * **Ideogram 4.0 open weights** : [@ideogram_ai](https://x.com/ideogram_ai/status/2062202208700313872) announced a notable shift from a strong closed image model to open weights.

  * **MAI-Thinking-1 transparency** : [@eliebakouch's thread](https://x.com/eliebakouch/status/2061965825037254947) was the most influential technical reading guide to the MAI report.

  * **Rosalind for life sciences** : OpenAI's [GPT-Rosalind update](https://x.com/OpenAI/status/2062281977122996256) signaled further verticalization of frontier models into domain-specific scientific research.

  * **Open audio/TTS momentum** : [Alibaba's Fun-Realtime-TTS](https://x.com/ArtificialAnlys/status/2062016529848222073) and [Miso One](https://x.com/kimmonismus/status/2062210845308780639) stood out as practical releases rather than just research demos.




* * *

# **AI Reddit Recap**

## **/r/LocalLlama + /r/localLLM Recap**

### **1\. Gemma 4 Multimodal Open Models**

[ Read more ](https://www.latent.space/p/ainews-reve-2-and-ideogram-4-layouts)

---

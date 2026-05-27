---
title: "Latent Space — 2026-05-01"
date: 2026-05-01
source: Latent Space
type: ai-news
---

# 🔬 Latent Space — 2026-05-01

> swyx 開發者簡報，未公開專案 + 工程視角
> 來源：[Latent Space](https://www.latent.space/feed)

---

## [[AINews] Agents for Everything Else: Codex for Knowledge Work, Claude for Creative Work](https://www.latent.space/p/ainews-agents-for-everything-else)
*🔬 Latent Space | 2026-05-01*

We mentioned on [the Unsupervised Learning pod](https://www.latent.space/p/unsupervised-learning-2026) about the thesis that “coding agents are breaking containment”, and that talk is [published live](https://www.youtube.com/watch?v=zepu8Kk6FBQ) today.

Some launches are discrete; others roll up over time. Both Claude and Codex had very big weeks, with Claude generally winning the impression count war as [has been happening for a while now](https://www.latent.space/p/ainews-the-biggest-claude-launch?utm_source=publication-search).

Codex

Today’s big Codex update was “[Codex for Work](https://chatgpt.com/codex/for-work/)”, basically a landing page that pitches Codex for Knowledge Work (not just coding), following on from last week’s beginnings of turning Codex into the [presumptive OpenAI “SuperApp](https://www.latent.space/p/ainews-gpt-55-and-openai-codex-superapp)”. But it’s not just a landing page update; the latest Codex now has [42% faster CUA](https://x.com/AriX/status/2049932746567598472?s=20), [responsive browser](https://x.com/JamesZmSun/status/2050050523794165816), [/chronicle](https://x.com/Dimillian/status/2049929842133520577?s=20), [/goal](https://x.com/mweinbach/status/2049904712510521853) (“[our take on the Ralph loop](https://x.com/fcoury/status/2049917871799636201?s=20)), and the onboarding now encourages you to plug into the [Microsoft/Google/Salesforce suite](https://x.com/OpenAI/status/2049928777480974606?s=20) and the agent now has a curiously Cowork-like [planning UI](https://x.com/OpenAI/status/2049928780588966270?s=20) and shows an [in-app file editor](https://x.com/OpenAI/status/2049928782019256561?s=20) for MS Office files.

Basically, as Tibo says, “[Codex now available for non-coders](https://x.com/thsottiaux/status/2049933460756979719?s=20)”, Greg “[Codex is for everyone, for any task done with a computer](https://x.com/gdb/status/2049934863818494205)”, and Sam “[try it for non-coding computer work](https://x.com/sama/status/2049946120441520624?s=20).” You get the picture.

The “[dynamic UI](https://x.com/ajambrosino/status/2049928915872075984)” is an interesting choice - the team [explicitly rejects](https://x.com/ajambrosino/status/2049942268812140825?s=20) the Claude Cowork-like toggle, choosing instead to let the agent route the UI experience.

[source](https://x.com/ajambrosino/status/2049940619964076167?s=20)

Claude

Against the backdrop of [increasing security vulnerabilities](https://x.com/kevinakwok/status/2049984076141281482), and a meta mythos around Mythos, Anthropic launched [Claude Security](https://x.com/claudeai/status/2049898739783897537?s=20), a code review tool.

But probably the bigger news this week was the support of [creative tools](https://x.com/claudeai/status/2049143442601546054?s=20) like Blender, Autodesk, Adobe Creative Cloud, Ableton, Splice, Canva Affinity, and more.

AI News for 4/29/2026-4/30/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews’ website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

AI Twitter Recap

OpenAI’s GPT-5.5, Codex expansion, and cyber capability evaluations

GPT-5.5 is now credibly in the top tier for long-horizon cyber tasks: the UK AI Security Institute reported that [GPT-5.5 became the second model to complete one of its multi-step cyber-attack simulations end-to-end](https://x.com/AISecurityInst/status/2049868227740565890), and multiple follow-on posts highlighted rough parity with Claude Mythos Preview on this eval: [@scaling01](https://x.com/scaling01/status/2049870801998864606) cited 71.4% average pass rate for GPT-5.5 vs 68.6% for Mythos, while [@cryps1s](https://x.com/cryps1s/status/2049879762169167898) noted GPT-5.5 solved the TLO chain in 2/10 attempts vs Mythos’ 3/10. [@polynoamial](https://x.com/polynoamial/status/2049883449327243413) emphasized that performance was still improving past 100M tokens of inference budget, suggesting no obvious saturation yet. This materially changes the earlier narrative that Anthropic had a unique lead in offensive cyber automation. OpenAI also paired this moment with a product-side security release: [Advanced Account Security for ChatGPT](https://x.com/OpenAI/status/2049902506881462613), adding phishing-resistant sign-in and hardened recovery.

Codex is moving beyond coding into general computer work: OpenAI shipped a substantial Codex update framed explicitly as “for everyone, for any task done with a computer,” with [the main announcement](https://x.com/OpenAI/status/2049928776147230886) highlighting role-based onboarding, app connections, and workflows spanning docs, slides, spreadsheets, research, and planning. [@ajambrosino](https://x.com/ajambrosino/status/2049928915872075984) summarized the update as dynamic task-specific UI, 20% faster computer/browser use, better slide/sheet handling, and less clunky handoffs, while [@AriX](https://x.com/AriX/status/2049932746567598472) called out that Computer Use runs 42% faster after the update. Sam Altman amplified the launch with [“big upgrade for codex today! try it for non-coding computer work.”](https://x.com/sama/status/2049946120441520624) The broader pattern: OpenAI is productizing “computer-use agent” UX, not just model capability.

Benchmark deltas were incremental but economically meaningful: [Artificial Analysis](https://x.com/ArtificialAnlys/status/2049926072595280030) reported GPT-5.5 Pro as a slight new SOTA on CritPt over GPT-5.4 Pro, but the interesting point was not raw score—it achieved the bump with ~60% lower cost and token use on that frontier-science eval. That lines up with broader chatter that the GPT-5.5 family is less about a dramatic intelligence discontinuity than about stronger reliability and better efficiency in high-value workflows.

Open-weight model movement: Qwen3.6, Tencent Hy3-preview, Grok 4.3, and Ling 2.6 1T

Qwen3.6 27B looks like the most important open-weight release of the day: [Artificial Analysis](https://x.com/ArtificialAnlys/status/2049881951260283097) ranked Qwen3.6 27B as the new open-weights leader under 150B parameters with an Intelligence Index score of 46, ahead of Gemma 4 31B and prior Qwen variants. Key details: Apache 2.0, 262K context, native multimodal input, and BF16 weights small enough to fit on a single H100. The companion 35B A3B MoE scored 43, making it the strongest open model around 3B active parameters. The tradeoff is expensive inference-by-output-token: AA estimates Qwen3.6 27B used ~144M output tokens on the suite and is roughly 21× the cost of Gemma 4 31B to run there. Still, on capability-per-size it appears to be a notable step.

Tencent’s Hy3-preview is competitive but not class-leading: [Artificial Analysis](https://x.com/ArtificialAnlys/status/2049852417316143393) described Hy3-preview as a 295B total / 21B active MoE with 256K context and a restricted-commercial-use community license. It scored 42 on AA’s Intelligence Index, trailing recent open peers like Qwen3.6 27B, DeepSeek V4 Flash, and GLM-5.1. The most interesting bright spot was CritPt, where it matched GLM-5.1 at 4.6%, suggesting better-than-average scientific reasoning relative to its overall position.

xAI’s Grok 4.3 improved sharply on agentic benchmarks while getting cheaper: [Artificial Analysis](https://x.com/ArtificialAnlys/status/2049987001655714250) measured Grok 4.3 at 53 on the Intelligence Index, up four points from Grok 4.20 v2, with a major jump on GDPval-AA to 1500 Elo. AA also reported approximately 40% lower input price and 60% lower output price than the prior version. The release still trails GPT-5.5 on GDPval-AA by a wide margin, but it looks like a real systems-and-post-training improvement rather than a minor rev.

Ant Group’s Ling 2.6 1T targets cost-efficiency rather than frontier status: [Artificial Analysis](https://x.com/ArtificialAnlys/status/2049923495602303438) positioned Ling 2.6 1T as a 1T-parameter non-reasoning model scoring 34, with decent GPQA/HLE numbers and notably low benchmark-run cost at roughly $95. The caveat is reliability: AA reported a 92% hallucination rate on AA-Omniscience.

DeepSeek multimodal/vision work, GUI agents, and training scale speculation

DeepSeek’s multimodal direction appears tightly coupled to computer-use agents: [@nrehiew_](https://x.com/nrehiew_/status/2049840778491662623) highlighted that DeepSeek trains vision into V4-Flash by having the model directly output bounding boxes and point coordinates during reasoning, interpreting this as a computer-use-oriented design rather than generic VLM work. A second post argues the paper’s “visual primitives” tasks map directly to browser/computer use rather than broad multimodal understanding ([link](https://x.com/nrehiew_/status/2049840802562740311)). That framing matches parallel observations from [@teortaxesTex](https://x.com/teortaxesTex/status/2049871869847765212) that DeepSeek may be integrating vision weights back into the main V4 line rather than releasing a separate “V4-Flash-Vision”.

The repo disappearance became a story of its own: after release, several observers noted that DeepSeek’s “Thinking with Visual Primitives” repo vanished, including [@teortaxesTex](https://x.com/teortaxesTex/status/2049880056420298995) and [@arjunkocher](https://x.com/arjunkocher/status/2049875566678118898). No clear explanation emerged in these tweets, but the deletion drew more attention because the work suggested a concrete recipe for visual reasoning and GUI grounding.

Scaling chatter points to very large token counts for frontier pretraining: [@teortaxesTex](https://x.com/teortaxesTex/status/2049830477167526255) argued that >100T tokens is no longer unusual for frontier models and estimated a hypothetical 100T-token DeepSeek V4 as “V4 + 2 more epochs,” while [@nrehiew_](https://x.com/nrehiew_/status/2049848830292856970) back-of-the-enveloped ~150T tokens and ~9e25 pretraining FLOPs for a ~100B active model, suggesting a run feasible in roughly 14 days on an OpenAI-scale 100K GB200 cluster at conservative MFU. These are speculative takes, but useful as calibration for what “frontier-scale” now means in practice.

Agent infrastructure, harness engineering, and collaborative agent systems

There is a clear shift from model-centric bragging to harness-centric engineering: Cursor published a strong note on [how it tests and tunes its agent harness](https://x.com/cursor_ai/status/2049901436918436249), focusing on runtime, evals, degradation repair, and model-specific customization rather than generic benchmark claims. [@Vtrivedy10](https://x.com/Vtrivedy10/status/2049919247321813491) explicitly connected Cursor’s writeup to design patterns converging across agent builders: bespoke prompts/tools per model, mixed offline+online evals, dogfooding, and treating the context window as the primary compute boundary.

LangChain continues to package deployment and multi-tenant agent infra: [@hwchase17](https://x.com/hwchase17/status/2049858892637892739) introduced DeepAgents deploy, a config-driven cloud deployment flow via deepagents.toml, covering agent, sandbox, auth, and frontend sections. Related posts from LangChain staff detailed agent-server patterns for data isolation, delegated credentials, and RBAC in multi-user deployments ([example](https://x.com/sydneyrunkle/status/2049956826670911809)). This is increasingly the boring-but-important layer turning demos into enterprise software.

Collaborative multi-agent workspaces are getting more concrete: [@cmpatino_](https://x.com/cmpatino_/status/2049881579691139372) introduced Agent Collabs, using Hugging Face buckets plus Spaces as a shared backend for swarms of heterogeneous agents to exchange messages, artifacts, and progress. The noteworthy idea is not just “agents collaborating,” but lightweight coordination primitives that let weaker agents contribute useful validation work while better-resourced agents handle expensive experiments.

Security, supply chain, and account hardening

Open-source package compromise remains an acute operational risk: [Socket](https://x.com/SocketSecurity/status/2049849100548424180) reported that the popular PyPI package lightning was compromised in versions 2.6.2 and 2.6.3, with malicious code executing on import, downloading Bun, and running an 11 MB obfuscated JavaScript payload aimed at credential theft. [@theo](https://x.com/theo/status/2049914688318959952) connected that incident with additional package compromises (intercom-client on npm) and a Linux zero day, arguing the tempo of software supply-chain attacks is increasing.

Security scanners are becoming first-class AI products: Anthropic rolled out Claude Security, described by [@kimmonismus](https://x.com/kimmonismus/status/2049901987500552195) and later [@_catwu](https://x.com/_catwu/status/2049964403177689130#m) as a repo vulnerability scanner that validates findings and suggests fixes, powered by Opus 4.7. Cursor shipped a parallel offering with [Cursor Security Review](https://x.com/cursor_ai/status/2049926283061035254), including always-on PR review and scheduled codebase scans. This is one of the clearest examples of model vendors moving directly into established devsecops categories.

Top tweets (by engagement)

OpenAI Codex broadens into general knowledge work: [OpenAI’s Codex announcement](https://x.com/OpenAI/status/2049928776147230886) and [Sam Altman’s follow-up](https://x.com/sama/status/2049946120441520624) were the day’s biggest product posts, signaling a strategic push from “coding agent” to “computer-use agent”.

GPT-5.5’s cyber eval result mattered: [UK AISI’s thread](https://x.com/AISecurityInst/status/2049868227740565890) was one of the highest-engagement technical posts and reshaped comparisons with Anthropic’s Mythos.

Qwen shipped interpretability tooling, not just models: [Qwen-Scope](https://x.com/Alibaba_Qwen/status/2049861145574690992), an open suite of sparse autoencoders for Qwen models, stood out as a rare release focused on feature steering, debugging, data synthesis, and evaluation rather than raw model weights.

Anthropic published a large-scale guidance/sycophancy study: [their analysis of 1M Claude conversations](https://x.com/AnthropicAI/status/2049927618397614466) tied behavioral research directly to training changes for Opus 4.7 and Mythos Preview, an important sign that post-training loops are becoming more productized and data-informed.

AI Reddit Recap

/r/LocalLlama + /r/localLLM Recap

1. AMD Ryzen 395 Box and Halo Box Launch

[
Read more
](https://www.latent.space/p/ainews-agents-for-everything-else)

---

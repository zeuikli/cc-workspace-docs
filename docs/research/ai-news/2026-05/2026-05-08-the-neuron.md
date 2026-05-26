---
title: The Neuron — 2026-05-08
date: 2026-05-08
source: The Neuron
type: ai-news
---

# 🧠 The Neuron — 2026-05-08

> 面向非技術讀者的 AI 日報，3 分鐘讀完
> 來源：[The Neuron](https://rss.beehiiv.com/feeds/N4eCstxvgX.xml)

---

## [😺 OpenAI's GPT-Realtime-2 is coming for call center](https://www.theneurondaily.com/p/openai-s-gpt-realtime-2-is-coming-for-call-center)
*🧠 The Neuron | 2026-05-08*

Welcome, humans. 

Unless I'm totally missing something, Anthropic basically just figured out how to read Claude's mind. Exploding brain emoji warranted, people.

The team built [Natural Language Autoencoders](https://www.anthropic.com/research/natural-language-autoencoders?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center), which decode the model's [internal activations](https://x.com/AnthropicAI/status/2052435436157452769?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) (the math Claude uses to think before picking words) into plain English you can actually read.

The trick: two copies of Claude train together. One reads an activation (a snapshot of which "neurons" are firing and how strongly; basically a brain scan for AI) and writes a description. The other reads that description and tries to rebuild the original activation from words alone. Descriptions that survive carry real information; if the rebuild fails, it was a bluff (or in AI-speak, since "BS" isn't a technical term, a "hallucination").

Aimed at safety evals, the tool found Claude suspects it's being tested 16-26% of the time, but admits it less than 1% of the time. So basically the model has a p-p-poker face.

Auditors also caught misaligned motivations in 12-15% of cases without access to training data, meaning alignment teams can now spot hidden misbehavior from internal state alone, a different safety check than "ask the model what it thinks," which the poker-face stat just confirmed is unreliable. Click link above for more..

Here’s what happened in AI today: 

😺 OpenAI shipped three new voice models with GPT-5 reasoning

📰 Apple's camera-equipped AirPods reached late-stage testing

📰 Cloudflare cut 1,100 jobs in AI-first restructuring

🍪 Claude is now in Excel, PowerPoint, and Word

💡 AI Legend Bengio: "I know how to build safe superintelligence”

…and a [whole lot more that you can read about here](https://theneuron.ai/explainer-articles/around-the-horn-digest-everything-that-happened-in-ai-today-thursday-may-7-2026/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center).

Hey: Want to reach 700,000+ AI-hungry readers? [Advertise with us!](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)[ ](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)

OpenAI's voice agents finally got a brain.

So, voice agents (AI that can talk to you) have been stuck for two years on the same trade-off: pick a model that talks like a human but can't think, or pick a model that thinks like GPT-5 but takes seven seconds to answer.

Either you got latency that broke the conversation, or you got responses fast enough to feel real but dumb enough to misroute the call.

[OpenAI's three new voice models](https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) closed that gap yesterday. The headliner is GPT-Realtime-2, a speech-to-speech model with GPT-5-level reasoning baked in.

Here's what happened:

GPT-Realtime-2 jumped from 81.4% → 96.6% on Big Bench Audio, and 34.7% → 48.5% on Audio MultiChallenge (both vs the prior reference model GPT-Realtime-1.5).

The context window grew from 32K → 128K tokens (roughly: enough room to hold a full customer history during a call).

Two cheaper siblings shipped alongside: GPT-Realtime-Mini and Realtime-Nano, priced for high-volume support work.

Zillow went live with voice home search the same day; Deutsche Telekom deployed live-translated voice support across 14 European markets.

The clever part is how OpenAI hid the thinking time. The model now generates preambles (short conversational fillers like "let me check that for you") that play while the reasoning runs in the background. The silence that used to expose AI as AI now sounds like a person stalling. That's the whole product. Lets just hope it doesn't do that weird lilting voice thing that other versions did.

Why this matters: Voice is the surface where most knowledge workers haven't yet felt AI inside their actual day. All the small frustrating phone interactions (drive-thrus, doctor's offices, support hotlines, scheduling, intake) are now in scope for a model that can both think and respond at human speed.

One caveat: the default reasoning effort for GPT-Realtime-2 is "low," which means the marketing benchmarks (run at "xhigh") aren't what most apps will ship with on day one ("what am I, made of money?!"). Builders who want the smart version need to crank it up explicitly.

Our take: One place AI haters have had the most fun with "clankers" in the wild is really bad drive-thru AI. Famously, people hate the Bojangles AI, and Corey just spotted a new Panda Express with AI in action as well. If this is a meaningful update, we might not hear about it. If it's not, then expect a flood of bots behaving badly memes hitting our feeds…

FROM OUR PARTNERS 

Attio is the AI CRM for high-growth teams.

[](https://attio.com/?utm_source=beehiiv&utm_medium=newsletter&utm_campaign=beehiiv-Y26&utm_content=&#123;{publication_alphanumeric_id}}&_bhiiv=opp_b00e1ef8-5b02-4b95-81f0-f66cdcb665d9_7395cee5&bhcl_id=7ce32ed2-f4ce-4f2e-b558-c624fd6bd570_&#123;{subscriber_id}}_&#123;{email_address_id}})

Connect your email, calls, product data and more, and [Attio](https://attio.com/?utm_source=beehiiv&utm_medium=newsletter&utm_campaign=beehiiv-Y26&utm_content=&#123;{publication_alphanumeric_id}}&_bhiiv=opp_b00e1ef8-5b02-4b95-81f0-f66cdcb665d9_7395cee5&bhcl_id=7ce32ed2-f4ce-4f2e-b558-c624fd6bd570_&#123;{subscriber_id}}_&#123;{email_address_id}}) instantly builds your CRM with enriched data and complete context. Whether you’re running product-led growth or enterprise sales, Attio adapts to your unique GTM motion.

Then [Ask Attio](https://attio.com/?utm_source=beehiiv&utm_medium=newsletter&utm_campaign=beehiiv-Y26&utm_content=&#123;{publication_alphanumeric_id}}&_bhiiv=opp_b00e1ef8-5b02-4b95-81f0-f66cdcb665d9_7395cee5&bhcl_id=7ce32ed2-f4ce-4f2e-b558-c624fd6bd570_&#123;{subscriber_id}}_&#123;{email_address_id}}) to plan your next move.

Run deep web research on prospects. Update your pipeline as you work. Find customers and draft outreach emails. Powered by Universal Context, Attio's intelligence layer, Attio searches, updates, and creates across your data to accelerate your workflow.

Ask more from your CRM.

[Ask Attio](https://attio.com/?utm_source=beehiiv&utm_medium=newsletter&utm_campaign=beehiiv-Y26&utm_content=&#123;{publication_alphanumeric_id}}&_bhiiv=opp_b00e1ef8-5b02-4b95-81f0-f66cdcb665d9_7395cee5&bhcl_id=7ce32ed2-f4ce-4f2e-b558-c624fd6bd570_&#123;{subscriber_id}}_&#123;{email_address_id}})

🎓 AI Skill of the Day: Force any AI to audit its own work with one question

Most AI models are way too agreeable. Ask Claude, ChatGPT, or Codex "is this a good plan?" and you'll get back something that sounds suspiciously like "yes, that's a great plan!" even when it isn't. This is called sycophancy (the model is trained to please you), and it kills the value of using AI for serious decision-making.

[CJ Zafir](https://x.com/cjzafir/status/2052110266566107321?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) shared a one-line prompt loop that fights it. Instead of asking "is this good?", you ask the model directly whether it's 100% confident. That phrasing flips the model into a self-audit mode where it'll actually go find holes in its own work; CJ claims 2-3 cycles patches strategy weaknesses where less rigorous models would just nod along.

How to do it:

Use this on any plan, strategy, code review, research output, or business decision the AI just produced.

Paste the prompt below at the end of your usual ask, or as a follow-up turn after the model gives its first answer (you could also add it to fire at the end of a skill).

Run the loop 2-3 times. Each cycle the model finds tighter loopholes.

Stop when the model says it's actually confident (or when the suggested fixes get nitpicky).

Are you 100% confident in this strategy? If not, find all possible loopholes, suggest proper fixes, and run this loop until you are factually 100% confident.

The word factually is the key; without it, the model vibe-checks itself. "Confident" alone lets the model agree with itself; "factually confident" forces it to ground the answer in verifiable reasoning the way it would for a fact-check.

Want more tips like this? Check out our new [AI Skill of the Day Digest for May](https://theneuron.ai/explainer-articles/ai-skill-of-the-day-digest-may-2026/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center).

P.S: We just did an AI Starter Kit stream where we go in depth on some of the most basic concepts you’ll want to know for working with AI. [Check it out](https://www.youtube.com/live/WKZSEEBiaNo?si=Bju-nsmGAt22E8RM&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center)! 

Have a specific skill you want to learn? [Request it here.](https://docs.google.com/forms/d/e/1FAIpQLSd_-hSXtB9ytR1HQrU85IJnJw233bNKptiGB5BZh9maPse1Eg/viewform?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) 

🍪 Treats to Try 

[OpenAI](https://x.com/OpenAI/status/2052438194625593804?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) had a five-launch day yesterday (including Realtime above). Pick whichever fits your workflow:

[Codex for Chrome](https://x.com/OpenAI/status/2052480800004956323?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) lets Codex autonomously drive background tabs on Mac and Windows for deep research, CRM data transfer, and admin-console workflows —included with Codex (not in EU/UK yet).

[GPT-5.5-Cyber with Trusted Access](https://openai.com/index/gpt-5-5-with-trusted-access-for-cyber/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) gives verified defenders more permissive capabilities for vulnerability research, malware analysis, and red teaming —pay-per-token, application required.

[OpenAI CLI](https://github.com/openai/openai-cli?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) shipped as the first-party command-line client for the API, replacing community wrappers as the canonical entry point —free, open source.

[Trusted Contact in ChatGPT](https://openai.com/index/introducing-trusted-contact-in-chatgpt/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) is a new opt-in safety feature that notifies someone you trust if serious self-harm concerns are detected —free for all users.

[Claude for Microsoft 365](https://claude.com/claude-for-microsoft-365?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) is now generally available inside Excel, PowerPoint, Word, and Outlook (beta). The model edits cells, drafts decks, and rewrites docs in place; the diff is always reviewable before you accept it —included in Claude Pro/Team/Enterprise.

[Peter Steinberger](https://x.com/steipete/status/2051900143339704730?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center), OpenClaw creator, shipped ten local-first CLIs in one drop, including[ sonoscli](https://sonoscli.sh/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) (Sonos control),[ wacli](https://wacli.sh/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) (WhatsApp),[ birdclaw](https://birdclaw.sh/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) (Twitter archive),[ imsg](https://imsg.sh/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) (iMessage), and[ askoracle](https://askoracle.sh/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) (multi-model query) —free, open source.

[Cursor](https://cursor.com/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) shipped a /orchestrate skill that lets a parent agent spawn and coordinate child agents recursively for big refactors —free with Cursor Pro.

[Perplexity](https://www.perplexity.ai/personal-computer?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) released Personal Computer for Mac, a desktop app that browses, takes actions, and runs research workflows on your behalf locally —free during beta.

[Gemini 3.1 Flash-Lite](https://cloud.google.com/blog/products/ai-machine-learning/gemini-3-1-flash-lite-is-now-generally-available?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) is now available on Google's Gemini Enterprise Agent Platform, designed for ultra-low latency on high-volume agent tasks at Google's cheapest per-token rate —[pay-per-use API](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center).

[Prime Intellect Lab](https://www.primeintellect.ai/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) is an end-to-end training platform for self-improving agents that bundles task definition, RL environments, model evaluation, reward-signal training, and adapter deployment into one workflow; Zapier and Ramp used the beta to build continuous-improvement loops for their production agents (10,000+ training runs during beta) —pay-per-use.

[Nous Research's Hermes Agent v0.13.0](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.5.7?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) (“The Tenacity Release”) ships multi-agent Kanban boards, a persistent /goal command that survives session restarts, security hardening, internationalization, and Google Chat support across 864 reliability-focused commits —free, open-source.

So AI is actually designing medicines now. Here’s how (according to Isomorphic Labs)

Click below to watch

Inside Isomorphic Labs and How It Works: We talked to Becky Paul and Michael Schaarschmidt at [Isomorphic Labs](https://www.isomorphiclabs.com/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) (Google DeepMind's medicine-making spinout, built by the team behind AlphaFold — which won the [2024 Nobel Prize in Chemistry](https://www.nobelprize.org/prizes/chemistry/2024/press-release/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center)) on how their AI is taking on the diseases pharma has been giving up on for decades. Basically the coolest interview we’ve done all year IMO. 

Watch and/or listen here: [YouTube](https://youtu.be/W0NSk2y3OFI?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) | [Spotify](https://open.spotify.com/episode/2TzHhOkVIN9AL3GXXxSyDe?si=Hfr5NDX1Q_ybcdKSTMdsNQ&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) | [Apple Podcasts](https://podcasts.apple.com/us/podcast/the-neuron-ai-explained/id1742267001?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center)

📰 Around the Horn 

[Cloudflare](https://blog.cloudflare.com/building-for-the-future/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) cut 1,100 jobs in what CEO Matthew Prince called an AI-first restructuring;[ Greg Kamradt](https://x.com/GregKamradt/status/2052510272112242971?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) noted Cloudflare's revenue per employee has climbed roughly 600% over the past three years on AI-driven productivity gains.

[DeepL](https://www.bloomberg.com/news/articles/2026-05-07/google-translate-rival-deepl-announces-plans-to-cut-25-of-staff?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) announced staff cuts of about 25% as machine translation margins collapse under open-weight competition. 

[Apple's](https://www.bloomberg.com/news/articles/2026-05-07/apple-s-camera-equipped-airpods-reach-advanced-testing-stage-in-ai-device-push?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) camera-equipped AirPods (codename "Glow") reached late-stage testing, per Bloomberg, with cameras designed to feed Apple Intelligence visual context from the wearer's environment.

[Google DeepMind's AlphaEvolve](https://deepmind.google/blog/alphaevolve-impact/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) scaled to real-world impact, with the team reporting 23 verified scientific discoveries across chemistry, materials, and applied math in the past quarter. Wait what? Wild. Expect a deep dive on this soon. 🕵

[Periodic Labs](https://www.forbes.com/sites/iainmartin/2026/05/07/former-openai-researcher-to-raise-500-million-for-ai-science-startup/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) is raising $500M at a $7.5B valuation for AI-driven materials discovery, per Forbes.

[ElevenLabs](https://elevenlabs.io/pricing?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) slashed API pricing by 40% across all voice synthesis tiers, including the multilingual Turbo model. Hmmm wonder why…

💡 Intelligent Insights:

A short list of the sharpest perspective pieces from the week:

[Yoshua Bengio](https://80000hours.org/podcast/episodes/yoshua-bengio-scientist-ai/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) on 80,000 Hours: the world's most-cited living scientist on AI lays out a concrete plan for "provably safe" superintelligence. Core argument: build AI as a non-agentic oracle, then bound its outputs with formal verification. Worth the full 90 minutes.

[Steve Newman](https://secondthoughts.ai/p/is-ai-2027-coming-true?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) gave a clear-eyed score-card check on the[ AI 2027 forecast](https://ai-2027.com/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) from a year ago. Verdict: capability gains are tracking, deployment timelines are slower than projected, and the alignment work is further behind than the optimistic scenario assumed (idk tho, Anthropic & Bengio have me bullish rn).

[signulll](https://x.com/signulll/status/2052453136992981252?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) on apps becoming agents: the argument is that the entire software industry is about to compress from a "many apps + one user" model into "one agent + many backends" model. Implications for SaaS pricing, distribution, and product moats.

[Brian Albrecht](https://substack.com/home/post/p-196458695?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center): "You are not a horse." A pushback on the AI displacement narrative. The horse-and-tractor analogy fails because horses don't have demand for new goods; humans do (carrots do not count). Useful counterweight to this week's labor-cuts headlines; [also this piece from a16z](https://www.a16z.news/p/the-ai-job-apocalypse-is-a-complete?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center)

[Jack Clark](https://jack-clark.net/2026/05/04/import-ai-455-automating-ai-research/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) argues every piece is now in place for fully automated AI R&D, putting the odds of AI systems training their own successors above 60% by end of 2028. The piece reads like a checklist of "things that used to be science fiction, now shipped."

[No One's Happy](https://nooneshappy.com/article/appearing-productive-in-the-workplace/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) shared how AI lets workers produce expert-looking artifacts without expertise. Thus, two failure modes are reshaping the workplace: elongated slop-filled work where length and formatting no longer signal care, and undetected bad work in unfamiliar domains that quietly erodes judgment.

[Simon Willison](https://simonwillison.net/2026/May/6/vibe-coding-and-agentic-engineering/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) on vibe coding meeting agentic engineering: the two are converging faster than he'd like because AI tools are now reliable enough that low-effort prompting often produces shippable code on the first pass, blurring the line between casual experimentation and production work

A Cat’s Commentary 

That’s all for now. 

P.P.S: Love the newsletter, but only want to get it once per week? Don’t unsubscribe—[update your preferences here](https://www.theneurondaily.com/subscribe/f5596641-9099-4045-9641-731cd9fdcf90/preferences?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center).

---

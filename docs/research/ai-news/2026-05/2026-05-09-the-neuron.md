---
title: The Neuron — 2026-05-09
date: 2026-05-09
source: The Neuron
type: ai-news
---

# 🧠 The Neuron — 2026-05-09

> 面向非技術讀者的 AI 日報，3 分鐘讀完
> 來源：[The Neuron](https://rss.beehiiv.com/feeds/N4eCstxvgX.xml)

---

## [😺 OpenAI's GPT-Realtime-2 is coming for call center](https://www.theneurondaily.com/p/openai-s-gpt-realtime-2-is-coming-for-call-center)
*🧠 The Neuron | 2026-05-08*

Welcome, humans. 

Unless I'm totally missing something, Anthropic basically just figured out how to read Claude's mind. Exploding brain emoji warranted, people.

The team built [Natural Language Autoencoders](https://www.anthropic.com/research/natural-language-autoencoders?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center), which decode the model's [internal activations](https://x.com/AnthropicAI/status/2052435436157452769?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) (the math Claude uses to think before picking words) into plain English you can actually read.

The trick: two copies of Claude train together. One reads an activation (a snapshot of which "neurons" are firing and how strongly; basically a brain scan for AI) and writes a description. The other reads that description and tries to rebuild the original activation from words alone. Descriptions that survive carry real information; if the rebuild fails, it was a bluff (or in AI-speak, since "BS" isn't a technical term, a "hallucination").

Aimed at safety evals, the tool found Claude suspects it's being tested _16-26% of the time_ , but admits it _less than 1%_ of the time. _So basically the model has a p-p-poker face._

Auditors also caught misaligned motivations in 12-15% of cases without access to training data, meaning alignment teams can now spot hidden misbehavior from internal state alone, a different safety check than "ask the model what it thinks," which the poker-face stat just confirmed is unreliable. Click link above for more._._

**Here’s what happened in AI today:**

  * 😺 OpenAI shipped three new voice models with GPT-5 reasoning

  * 📰 Apple's camera-equipped AirPods reached late-stage testing

  * 📰 Cloudflare cut 1,100 jobs in AI-first restructuring

  * 🍪 Claude is now in Excel, PowerPoint, and Word

  * 💡 AI Legend Bengio: "I know how to build safe superintelligence”




…and a [**whole lot more that you can read about here**](https://theneuron.ai/explainer-articles/around-the-horn-digest-everything-that-happened-in-ai-today-thursday-may-7-2026/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center).

**Hey:**_Want to reach 700,000+ AI-hungry readers?_[Advertise with us!](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)_[](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)_

# **OpenAI's voice agents finally got a brain.**

So, voice agents (AI that can talk to you) have been stuck for two years on the same trade-off: pick a model that talks like a human but can't think, or pick a model that thinks like GPT-5 but takes seven seconds to answer.

Either you got latency that broke the conversation, or you got responses fast enough to feel real but dumb enough to misroute the call.

[OpenAI's three new voice models](https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) closed that gap yesterday. The headliner is GPT-Realtime-2, a speech-to-speech model with GPT-5-level reasoning baked in.

**Here's what happened:**

  * GPT-Realtime-2 jumped from 81.4% → 96.6% on Big Bench Audio, and 34.7% → 48.5% on Audio MultiChallenge (both vs the prior reference model GPT-Realtime-1.5).

  * The context window grew from 32K → 128K tokens (roughly: enough room to hold a full customer history during a call).

  * Two cheaper siblings shipped alongside: GPT-Realtime-Mini and Realtime-Nano, priced for high-volume support work.

  * Zillow went live with voice home search the same day; Deutsche Telekom deployed live-translated voice support across 14 European markets.




The clever part is how OpenAI hid the thinking time. The model now generates **preambles** (short conversational fillers like "let me check that for you") that play while the reasoning runs in the background. The silence that used to expose AI as AI now sounds like a person stalling. _That's the whole product. Lets just hope it doesn't do that weird lilting voice thing that other versions did._

**Why this matters:** Voice is the surface where most knowledge workers haven't yet felt AI inside their actual day. All the small frustrating phone interactions (drive-thrus, doctor's offices, support hotlines, scheduling, intake) are now in scope for a model that can both think and respond at human speed.

**One caveat:** the default reasoning effort for GPT-Realtime-2 is "low," which means the marketing benchmarks (run at "xhigh") aren't what most apps will ship with on day one _( "what am I, made of money?!")_. Builders who want the smart version need to crank it up explicitly.

**Our take:** One place AI haters have had the most fun with "clankers" in the wild is really bad drive-thru AI. Famously, people _hate_ the Bojangles AI, and Corey just spotted a new Panda Express with AI in action as well. _If this is a meaningful update, we might not hear about it. If it's not, then expect a flood of bots behaving badly memes hitting our feeds…_

**FROM OUR PARTNERS**

### Attio is the AI CRM for high-growth teams.

[](https://attio.com/?utm_source=beehiiv&utm_medium=newsletter&utm_campaign=beehiiv-Y26&utm_content=&#123;{publication_alphanumeric_id}}&_bhiiv=opp_b00e1ef8-5b02-4b95-81f0-f66cdcb665d9_7395cee5&bhcl_id=7ce32ed2-f4ce-4f2e-b558-c624fd6bd570_&#123;{subscriber_id}}_&#123;{email_address_id}})

Connect your email, calls, product data and more, and [Attio](https://attio.com/?utm_source=beehiiv&utm_medium=newsletter&utm_campaign=beehiiv-Y26&utm_content=&#123;{publication_alphanumeric_id}}&_bhiiv=opp_b00e1ef8-5b02-4b95-81f0-f66cdcb665d9_7395cee5&bhcl_id=7ce32ed2-f4ce-4f2e-b558-c624fd6bd570_&#123;{subscriber_id}}_&#123;{email_address_id}}) instantly builds your CRM with enriched data and complete context. Whether you’re running product-led growth or enterprise sales, Attio adapts to your unique GTM motion.

Then [Ask Attio](https://attio.com/?utm_source=beehiiv&utm_medium=newsletter&utm_campaign=beehiiv-Y26&utm_content=&#123;{publication_alphanumeric_id}}&_bhiiv=opp_b00e1ef8-5b02-4b95-81f0-f66cdcb665d9_7395cee5&bhcl_id=7ce32ed2-f4ce-4f2e-b558-c624fd6bd570_&#123;{subscriber_id}}_&#123;{email_address_id}}) to plan your next move.

Run deep web research on prospects. Update your pipeline as you work. Find customers and draft outreach emails. Powered by Universal Context, Attio's intelligence layer, Attio searches, updates, and creates across your data to accelerate your workflow.

Ask more from your CRM.

[Ask Attio](https://attio.com/?utm_source=beehiiv&utm_medium=newsletter&utm_campaign=beehiiv-Y26&utm_content=&#123;{publication_alphanumeric_id}}&_bhiiv=opp_b00e1ef8-5b02-4b95-81f0-f66cdcb665d9_7395cee5&bhcl_id=7ce32ed2-f4ce-4f2e-b558-c624fd6bd570_&#123;{subscriber_id}}_&#123;{email_address_id}})

# 🎓 AI Skill of the Day: Force any AI to audit its own work with one question

Most AI models are way too agreeable. Ask Claude, ChatGPT, or Codex _" is this a good plan?"_ and you'll get back something that sounds suspiciously like _" yes, that's a great plan!"_ even when it isn't. This is called sycophancy (the model is trained to please you), and it kills the value of using AI for serious decision-making.

[CJ Zafir](https://x.com/cjzafir/status/2052110266566107321?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) shared a one-line prompt loop that fights it. Instead of asking _" is this good?"_, you ask the model directly whether it's _100% confident._ That phrasing flips the model into a self-audit mode where it'll actually go find holes in its own work; CJ claims 2-3 cycles patches strategy weaknesses where less rigorous models would just nod along.

**How to do it:**

  * Use this on any plan, strategy, code review, research output, or business decision the AI just produced.

  * Paste the prompt below at the end of your usual ask, or as a follow-up turn after the model gives its first answer (_you could also add it to fire at the end of a skill)_.

  * Run the loop 2-3 times. Each cycle the model finds tighter loopholes.

  * Stop when the model says it's actually confident (or when the suggested fixes get nitpicky).



    
    
    Are you 100% confident in this strategy? If not, find all possible loopholes, suggest proper fixes, and run this loop until you are factually 100% confident.

The word _factually_ is the key; without it, the model vibe-checks itself. _" Confident"_ alone lets the model agree with itself; _" factually confident"_ forces it to ground the answer in verifiable reasoning the way it would for a fact-check.

Want more tips like this? Check out our new [AI Skill of the Day Digest for May](https://theneuron.ai/explainer-articles/ai-skill-of-the-day-digest-may-2026/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center).

**P.S:** We just did an AI Starter Kit stream where we go in depth on some of the most basic concepts you’ll want to know for working with AI. [Check it out](https://www.youtube.com/live/WKZSEEBiaNo?si=Bju-nsmGAt22E8RM&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center)! 

**Have a specific skill you want to learn?** [Request it here.](https://docs.google.com/forms/d/e/1FAIpQLSd_-hSXtB9ytR1HQrU85IJnJw233bNKptiGB5BZh9maPse1Eg/viewform?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center)

# 🍪 Treats to Try 

  1. [OpenAI](https://x.com/OpenAI/status/2052438194625593804?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) had a five-launch day yesterday (including Realtime above). Pick whichever fits your workflow:

     * [Codex for Chrome](https://x.com/OpenAI/status/2052480800004956323?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) lets Codex autonomously drive background tabs on Mac and Windows for deep research, CRM data transfer, and admin-console workflows —included with Codex (not in EU/UK yet).

     * [GPT-5.5-Cyber with Trusted Access](https://openai.com/index/gpt-5-5-with-trusted-access-for-cyber/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) gives verified defenders more permissive capabilities for vulnerability research, malware analysis, and red teaming —pay-per-token, application required.

     * [OpenAI CLI](https://github.com/openai/openai-cli?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) shipped as the first-party command-line client for the API, replacing community wrappers as the canonical entry point —free, open source.

     * [Trusted Contact in ChatGPT](https://openai.com/index/introducing-trusted-contact-in-chatgpt/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) is a new opt-in safety feature that notifies someone you trust if serious self-harm concerns are detected —free for all users.

  2. [Claude for Microsoft 365](https://claude.com/claude-for-microsoft-365?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) is now generally available inside Excel, PowerPoint, Word, and Outlook (beta). The model edits cells, drafts decks, and rewrites docs in place; the diff is always reviewable before you accept it —included in Claude Pro/Team/Enterprise.

  3. [Peter Steinberger](https://x.com/steipete/status/2051900143339704730?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center), OpenClaw creator, shipped ten local-first CLIs in one drop, including[ sonoscli](https://sonoscli.sh/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) (Sonos control),[ wacli](https://wacli.sh/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) (WhatsApp),[ birdclaw](https://birdclaw.sh/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) (Twitter archive),[ imsg](https://imsg.sh/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) (iMessage), and[ askoracle](https://askoracle.sh/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) (multi-model query) —free, open source.

  4. [Cursor](https://cursor.com/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) shipped a /orchestrate skill that lets a parent agent spawn and coordinate child agents recursively for big refactors —free with Cursor Pro.

  5. [Perplexity](https://www.perplexity.ai/personal-computer?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) released Personal Computer for Mac, a desktop app that browses, takes actions, and runs research workflows on your behalf locally —free during beta.

  6. [Gemini 3.1 Flash-Lite](https://cloud.google.com/blog/products/ai-machine-learning/gemini-3-1-flash-lite-is-now-generally-available?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) is now available on Google's Gemini Enterprise Agent Platform, designed for ultra-low latency on high-volume agent tasks at Google's cheapest per-token rate —[pay-per-use API](https://cloud.google.com/gemini-enterprise-agent-platform/generative-ai/pricing?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center).

  7. [Prime Intellect Lab](https://www.primeintellect.ai/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) is an end-to-end training platform for self-improving agents that bundles task definition, RL environments, model evaluation, reward-signal training, and adapter deployment into one workflow; Zapier and Ramp used the beta to build continuous-improvement loops for their production agents (10,000+ training runs during beta) —pay-per-use.

  8. [Nous Research's Hermes Agent v0.13.0](https://github.com/NousResearch/hermes-agent/releases/tag/v2026.5.7?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) (“The Tenacity Release”) ships multi-agent Kanban boards, a persistent /goal command that survives session restarts, security hardening, internationalization, and Google Chat support across 864 reliability-focused commits —free, open-source.




# So AI is actually designing medicines now. Here’s how (according to Isomorphic Labs)

Click below to watch

**Inside Isomorphic Labs and How It Works** : We talked to Becky Paul and Michael Schaarschmidt at [Isomorphic Labs](https://www.isomorphiclabs.com/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) (Google DeepMind's medicine-making spinout, built by the team behind AlphaFold — which won the [2024 Nobel Prize in Chemistry](https://www.nobelprize.org/prizes/chemistry/2024/press-release/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center)) on how their AI is taking on the diseases pharma has been giving up on for decades. _Basically the coolest interview we’ve done all year IMO._

**Watch and/or listen here:**[YouTube](https://youtu.be/W0NSk2y3OFI?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) | [Spotify](https://open.spotify.com/episode/2TzHhOkVIN9AL3GXXxSyDe?si=Hfr5NDX1Q_ybcdKSTMdsNQ&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) | [Apple Podcasts](https://podcasts.apple.com/us/podcast/the-neuron-ai-explained/id1742267001?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center)

# 📰 Around the Horn 

  * [Cloudflare](https://blog.cloudflare.com/building-for-the-future/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) cut 1,100 jobs in what CEO Matthew Prince called an AI-first restructuring;[ Greg Kamradt](https://x.com/GregKamradt/status/2052510272112242971?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) noted Cloudflare's revenue per employee has climbed roughly 600% over the past three years on AI-driven productivity gains.

  * [DeepL](https://www.bloomberg.com/news/articles/2026-05-07/google-translate-rival-deepl-announces-plans-to-cut-25-of-staff?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) announced staff cuts of about 25% as machine translation margins collapse under open-weight competition. 

  * [Apple's](https://www.bloomberg.com/news/articles/2026-05-07/apple-s-camera-equipped-airpods-reach-advanced-testing-stage-in-ai-device-push?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) camera-equipped AirPods (codename "Glow") reached late-stage testing, per Bloomberg, with cameras designed to feed Apple Intelligence visual context from the wearer's environment.

  * [Google DeepMind's AlphaEvolve](https://deepmind.google/blog/alphaevolve-impact/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) scaled to real-world impact, with the team reporting 23 verified scientific discoveries across chemistry, materials, and applied math in the past quarter. _Wait what? Wild. Expect a deep dive on this soon._ 🕵

  * [Periodic Labs](https://www.forbes.com/sites/iainmartin/2026/05/07/former-openai-researcher-to-raise-500-million-for-ai-science-startup/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) is raising $500M at a $7.5B valuation for AI-driven materials discovery, per Forbes.

  * [ElevenLabs](https://elevenlabs.io/pricing?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) slashed API pricing by 40% across all voice synthesis tiers, including the multilingual Turbo model. _Hmmm wonder why…_




# 💡 Intelligent Insights:

A short list of the sharpest perspective pieces from the week:

  * [Yoshua Bengio](https://80000hours.org/podcast/episodes/yoshua-bengio-scientist-ai/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) on 80,000 Hours: the world's most-cited living scientist on AI lays out a concrete plan for "provably safe" superintelligence. Core argument: build AI as a non-agentic oracle, then bound its outputs with formal verification. Worth the full 90 minutes.

  * [Steve Newman](https://secondthoughts.ai/p/is-ai-2027-coming-true?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) gave a clear-eyed score-card check on the[ AI 2027 forecast](https://ai-2027.com/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) from a year ago. Verdict: capability gains are tracking, deployment timelines are slower than projected, and the alignment work is further behind than the optimistic scenario assumed (_idk tho, Anthropic & Bengio have me bullish rn)_.

  * [signulll](https://x.com/signulll/status/2052453136992981252?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) on apps becoming agents: the argument is that the entire software industry is about to compress from a "many apps + one user" model into "one agent + many backends" model. Implications for SaaS pricing, distribution, and product moats.

  * [Brian Albrecht](https://substack.com/home/post/p-196458695?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center): "You are not a horse." A pushback on the AI displacement narrative. The horse-and-tractor analogy fails because horses don't have demand for new goods; humans do (_carrots do not count)_. Useful counterweight to this week's labor-cuts headlines; [_also this piece from a16z_](https://www.a16z.news/p/the-ai-job-apocalypse-is-a-complete?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center)

  * [Jack Clark](https://jack-clark.net/2026/05/04/import-ai-455-automating-ai-research/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) argues every piece is now in place for fully automated AI R&D, putting the odds of AI systems training their own successors above 60% by end of 2028. The piece reads like a checklist of "things that used to be science fiction, now shipped."

  * [No One's Happy](https://nooneshappy.com/article/appearing-productive-in-the-workplace/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) shared how AI lets workers produce expert-looking artifacts without expertise. Thus, two failure modes are reshaping the workplace: elongated slop-filled work where length and formatting no longer signal care, and undetected bad work in unfamiliar domains that quietly erodes judgment.

  * [Simon Willison](https://simonwillison.net/2026/May/6/vibe-coding-and-agentic-engineering/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center) on vibe coding meeting agentic engineering: the two are converging faster than he'd like because AI tools are now reliable enough that low-effort prompting often produces shippable code on the first pass, blurring the line between casual experimentation and production work




# A Cat’s Commentary 

| That’s all for now.   
---|---  
  
**P.P.S:** Love the newsletter, but only want to get it once per week? Don’t unsubscribe—[update your preferences here](https://www.theneurondaily.com/subscribe/f5596641-9099-4045-9641-731cd9fdcf90/preferences?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-s-gpt-realtime-2-is-coming-for-call-center).

---

## [😺 Watch LIVE NOW: The AI Starter Kit (what to try, what to skip)](https://www.theneurondaily.com/p/watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip)
*🧠 The Neuron | 2026-05-07*

[](https://www.youtube.com/live/WKZSEEBiaNo?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip)

Click the image above to watch live on YouTube!

Welcome, humans. 

If you've ever opened ChatGPT, stared at the blinking cursor, and thought _" …now what?"_, this one is for you. (Or for that one coworker who keeps asking you the same five questions about AI.)

**We're live RIGHT NOW with** [**The AI Starter Kit: What to Try… and What to Ignore.**](https://www.youtube.com/live/WKZSEEBiaNo?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip) Seriously, there are no dumb questions on this stream! Come and ask anything you like and we’ll help you answer them. 

The idea here is a practical, beginner-friendly walkthrough of what actually matters in AI in 2026, and what you can safely skip.

## 🔴 What we're covering live, on stream:

  * The best **first steps for AI beginners** (and the ones we'd skip if we were starting today)

  * The **tools and features** worth trying right now (and which ones aren't ready yet)

  * What you can **safely ignore** for the moment, even if X / LinkedIn says otherwise

  * **Simple prompting moves** that get you better answers from any AI tool

  * **How to troubleshoot** when AI gives you something unhelpful (so you stop just retrying the same prompt)




**Watch live now here:**

[](https://www.youtube.com/live/WKZSEEBiaNo?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip)

**P.S.** Timestamps will be added to the video after the stream, so if you can't make it live, bookmark this email and come back tomorrow. You'll be able to jump straight to the parts you care about.

# 📬 Full writeup in sunday's newsletter

Not free atm? We've got you. We'll publish a full breakdown of everything we found in tomorrow's daily newsletter, with the sharpest prompts, the biggest surprises, and a direct "should you switch?" call.

**THIS EPISODE WAS BROUGHT TO YOU BY…**

# Want to see your AI-adjacent product or service show up right here, below these podcast promos?

_Click the button below to advertise to our 700K+ readers!_

[_Advertise in The Neuron here!_](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip)

# 🎙️ In Case You Missed It… 

[Four recent interviews](https://www.youtube.com/@theneuronai?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip) you’ll definitely want to check out _(pick whatever looks interesting to you and dive in!):_

### **1.** **AI isn't just chatbots, it's designing medicines now:**

**[Inside Isomorphic Labs and How It Works](https://youtu.be/W0NSk2y3OFI?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip)** — Becky Paul and Michael Schaarschmidt at [Isomorphic Labs](https://www.isomorphiclabs.com/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip) ([Google DeepMind](https://deepmind.google/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip)'s medicine-making spinout, built by the team behind [AlphaFold](https://deepmind.google/science/alphafold/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip) — which won the [2024 Nobel Prize in Chemistry](https://www.nobelprize.org/prizes/chemistry/2024/press-release/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip)) on how their AI is taking on the diseases pharma has been giving up on for decades. The clearest "what AI actually means for patients" explainer we've published. [YouTube](https://youtu.be/W0NSk2y3OFI?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip) | [Spotify](https://open.spotify.com/episode/2TzHhOkVIN9AL3GXXxSyDe?si=Hfr5NDX1Q_ybcdKSTMdsNQ&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip) | [Apple Podcasts](https://podcasts.apple.com/us/podcast/the-neuron-ai-explained/id1742267001?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip)

### 2\. You've definitely used Canva. But you probably haven't seen it like this: 

[](https://youtu.be/JqZmdg71Bnc?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip)

**[24 Billion AI Uses Later, What Canva Learned About AI Design](https://youtu.be/JqZmdg71Bnc?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip)** — Danny Wu, Canva's Head of AI Products, walks us through how their AI tools have been used **24 BILLION times** , why they spent over a year building a design model that generates _layered, editable_ assets (not just flat images), and how typing one word ("MCP") lets you create fully editable Canva designs from inside ChatGPT, Claude, or Copilot. [YouTube](https://youtu.be/JqZmdg71Bnc?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip) | [Spotify](https://open.spotify.com/episode/1M79tzwFNuqTrCf2d40tFa?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip) | [Apple Podcasts](https://podcasts.apple.com/us/podcast/24-billion-ai-uses-later-what-canva-learned-about-the/id1742267001?i=1000754551676&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip)

### **3\. Your laptop is about to become Hollywood:**

[](https://youtu.be/0WBnAEIkj5A?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip)

**[This Tool Turns Your Laptop Into a Movie Studio](https://youtu.be/0WBnAEIkj5A?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip)** — Yaron Inger, CTO and co-founder of [Lightricks](https://www.lightricks.com/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip) (the company behind Facetune), on why their open-source [LTX-2](https://ltx.io/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip) model has been downloaded **4.5 million times in two months** , runs locally on a consumer GPU, and just ate Pinky-Promise level expensive AI video tools for breakfast. The full [LTX Desktop](https://github.com/Lightricks/LTX-Desktop?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip) editor was vibe-coded by 2.5 people in 10 days. [YouTube](https://youtu.be/0WBnAEIkj5A?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip) | [Spotify](https://open.spotify.com/episode/0W6WTL0ACM3HAI6ND9vUWC?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip) | [Apple Podcasts](https://podcasts.apple.com/us/podcast/ai-just-democratized-filmmaking-w-ltx-co-founder/id1742267001?i=1000754869036&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip)

### **4\. AI feels expensive? Watch this and it'll feel like magic:**

**[The $0.25-Per-Million-Tokens AI Model That Feels Like Magic](https://youtu.be/LQrq3NSBlQU?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip)** — Stefano Ermon, co-founder of [Inception Labs](https://www.inceptionlabs.ai/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip) and Stanford professor, on Mercury, a new kind of language model (diffusion-based, not transformer-based) that could make AI **10x faster** and dramatically cheaper. If you've been stalled on AI because of cost, this is the episode that flips the math. [YouTube](https://youtu.be/LQrq3NSBlQU?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip) | [Spotify](https://open.spotify.com/episode/1HL1foM6m8ql9reKLuKDZu?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip) | [Apple Podcasts](https://podcasts.apple.com/us/podcast/diffusion-for-text-why-mercury-could-make-llms-10x-faster/id1742267001?i=1000751254612&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip)

## One more before you go:

A few weeks ago we went live with the **["AI for Total Beginners" 5-Level Starter Stack](https://www.youtube.com/live/QbFU0UNMVaU?si=YRpR8raOXHvfrBqw&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip)**, a full framework for going from "I've never touched AI" to "AI saves me 10 hours a week." No coding required. It's at 11,000+ views and counting, so it’ll be a good follow-up to this one if you haven’t watch it yet! 

**Last thing:** And if you [haven’t subscribed yet, please do!](https://www.youtube.com/@theneuronai?sub_confirmation=1&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip) Click the image below to go to our channel and hit “subscribe” to get notified right when new videos go live. 

[](https://www.youtube.com/@theneuronai?sub_confirmation=1&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip)

We have a goal to hit **50K subscribers** by the end of the year (if not 100K), and **we’re only 30K away!** If you like learning about AI, and already watch some of our videos, [do us a favor and click here to subscribe](https://www.youtube.com/@theneuronai?sub_confirmation=1&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip) today. 

Stay curious,

The Neuron Team

| That’s all for today, for more AI treats, check out our [website](https://www.theneuron.ai/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-the-ai-starter-kit-what-to-try-what-to-skip).   
---|---  
  
**P.P.S:** Love the newsletter, but don’t want to receive these podcast announcement emails? Don’t unsubscribe — _[adjust your preferences to opt out of them here instead](https://www.theneurondaily.com/subscribe/f5596641-9099-4045-9641-731cd9fdcf90/preferences?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-first-major-ai-incident-this-year-ceo-warns&_bhlid=1d073d4088b90ea4abf69ef7cc157e0659ada818)_ _._

---

## [😺 Anthropic 🤝 SpaceX data center deal](https://www.theneurondaily.com/p/anthropic-spacex-data-center-deal)
*🧠 The Neuron | 2026-05-07*

Welcome, humans. 

Anthropic ran[ Code with Claude SF](https://claude.com/code-with-claude/san-francisco?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) yesterday, the biggest developer event of its year. The keynote announced a SpaceX partnership for 220,000+ NVIDIA GPUs, doubled Claude Code rate limits, and put GitHub, Datadog, Netflix, Vercel, Cursor, and Replit on stage to defend the platform thesis.

And about an hour into all of that,[ Claude itself briefly went down](https://community.designtaxi.com/topic/28150-is-claude-anthropic-ai-down-may-6-2026/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) for thousands of users (per DownDetector, spiking around 11:16AM ET).

_Truly nothing tells the audience "we're spending billions to fix our compute problem" like the compute problem briefly breaking the app. _

 _By the time the keynote pitched how the_ SpaceX deal _buys 300+ MW of new capacity within the month, the service was back up. There's a reason they need that much!_

**Here’s what happened in AI today:**

  * 😺 Anthropic doubled Claude Code limits and signed a SpaceX compute deal

  * 📰 Apple is talking to Intel and Samsung for US-made device chips

  * 🍪 Adobe unveiled a productivity agent that turns PDFs into interactive AI experiences

  * 🧩 One of these images is real, one is AI; vote below




**A wild Neuron appearance!****** Our own Corey Noles joined [NVIDIA's Nemotron 3 Nano Omni livestream](https://www.youtube.com/watch?v=OymqGF1TxYc&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) this week with Wendell Wilson of Level1Techs for a working dev's take on the new multimodal open model: which model do you reach for and when, how to actually architect coordinated sub-agents, and where multimodal open weights unlock things text-only models can't.

# 😺******Anthropic doubled Claude Code limits and locked up Elon's Memphis data center.**

As established, yesterday was Code with Claude SF, Anthropic's biggest developer day of the year. The opening keynote did what every Anthropic keynote does (announce capacity, demo a feature, parade big customers). 

But the thing that mattered to anyone who's actually used Claude Code in the past six weeks was buried in a single sentence: _the five-hour rate limits just doubled._

**Here's what happened:**

  * Anthropic[ signed a partnership with SpaceX](https://www.anthropic.com/news/higher-limits-spacex?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) for full access to[ Colossus 1](https://www.bloomberg.com/news/articles/2026-05-06/anthropic-inks-computing-deal-with-spacex-to-meet-ai-demand?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal), SpaceX's 300+ MW Memphis data center (yes, the former xAI campus).

  * 220,000+ NVIDIA GPUs come online "within the month."

  * Claude Code's five-hour rate limits **doubled** for Pro, Max, Team, and seat-based Enterprise plans.

  * The peak-hours Claude Code limit reduction is **gone** for Pro and Max.

  * Opus API rate limits went up "considerably."

  * Anthropic also said it's "expressed interest" in partnering with SpaceX on multi-gigawatt **orbital AI compute** (yes, datacenters in space).




Oh no, this couldn’t possibly have anything to do with the very unrelated legal case involving our mutual frenemy ALSO happening at the same time about now…” 

**On the product side, three new**[ ](https://platform.claude.com/docs/en/managed-agents/overview?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal)[Claude Managed Agents](https://platform.claude.com/docs/en/managed-agents/overview?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal)******features dropped at the same keynote** ([per Simon Willison's live blog](https://simonwillison.net/2026/May/6/code-w-claude-2026/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal)):

  * **Multi-agent orchestration** ([research preview](https://platform.claude.com/docs/en/managed-agents/multi-agent?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal)) lets you spawn fleets of agents that hand off subtasks to each other. The on-stage demo built a hypothetical lunar drone-landing system out of three coordinating agents (a Commander, a Detector, and a Navigator).

  * **Outcomes** ([research preview](https://platform.claude.com/docs/en/managed-agents/define-outcomes?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal)) lets you define what success actually looks like, then let Claude iterate until the agent hits that bar instead of just stopping when the prompt ends. 

  * **Dreaming** ([research preview](https://platform.claude.com/docs/en/managed-agents/dreams?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal)) lets you run an agent overnight to inspect its prior sessions, find what it missed, and write itself new memory. The keynote demo: dreaming on a landing task spat out a [descent-playbook.md](https://descent-playbook.md?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) ready to use next time.




For more on these, [watch Claire Vo’s video where she breaks it all down](https://youtu.be/efVfydaUIrM?si=ktkIiGqCEltPuRTb&t=327&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal). 

**Why this matters:****** The last six weeks of Claude Code have been rough. There were[ public performance complaints](https://fortune.com/2026/04/24/anthropic-engineering-missteps-claude-code-performance-decline-user-backlash/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal), brief plan-tier confusion (Claude Code[ briefly removed from Pro](https://www.theregister.com/2026/04/22/anthropic_removes_claude_code_pro/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) before being restored within 24 hours), and a[ Fortune piece](https://fortune.com/2026/04/24/anthropic-engineering-missteps-claude-code-performance-decline-user-backlash/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) where Anthropic admitted to engineering missteps. 

The diagnosis everyone landed on: Anthropic ran out of compute. The reason? Dario said [_they grew by 80x_](https://www.perplexity.ai/page/anthropic-ceo-claims-80x-reven-EehipXoZQ.SnPqCkyA052A?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) last quarter. _Daaaamn, Daniela! (that’s millennial for “i’m impressed)._ The doubled rate limits and SpaceX deal are the answer in two parts.

Now, stack today's announcement against the[ 5GW Amazon deal](https://www.anthropic.com/news/anthropic-amazon-compute?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal), the[ 5GW Google/Broadcom agreement](https://www.anthropic.com/news/google-broadcom-partnership-compute?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal), the[ $30B Microsoft/NVIDIA partnership](https://www.anthropic.com/news/microsoft-nvidia-anthropic-announce-strategic-partnerships?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal), the[ $50B Fluidstack investment](https://www.anthropic.com/news/anthropic-invests-50-billion-in-american-ai-infrastructure?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal), and the[ $200B five-year Google Cloud commitment](https://sherwood.news/markets/alphabet-gains-on-report-that-anthropics-committed-to-spending-200-billion-on-cloud-services-over-the-next-five-years/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) The Information surfaced yesterday _(Anthropic alone now reportedly accounts for more than 40% of Google Cloud's revenue backlog)._

Anthropic is basically signing every cloud and chip deal it can find, and now Elon's data center too. _The same Elon whose Pentagon allies designated Anthropic a "supply chain risk" last quarter. Politics is downstream of gigawatts I guess? _

 _Well, If you’re AGI-pilled, meaning you believe “artificial general intelligence” is imminent and going to lead to a “fast take-off” scenario for technology, then everything is downstream of gigawatts…_

Want to watch it yourself? The[ keynote](https://www.youtube.com/live/GMIWm5y90xA?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) and every[ breakout session](https://www.youtube.com/@claude/streams?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) are on YouTube. Latent Space also [has a nice recap](https://open.substack.com/pub/swyx/p/ainews-anthropic-spacexais-300mw5byr?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) of some other takeaways from Dario and Daniela’s talk and the other sessions. 

**FROM OUR PARTNERS**

### GTM Atlas, by Attio

[](https://atlas.attio.com/?utm_source=beehiiv&utm_medium=newsletter&utm_campaign=beehiiv-Y26-atlas&utm_content=&#123;{publication_alphanumeric_id}}&_bhiiv=opp_311ed0df-17e5-4990-ac54-7e163c91b23c_8ebadeed&bhcl_id=ec4782dc-abe5-43f5-9d81-922fbe0f88a2_&#123;{subscriber_id}}_&#123;{email_address_id}})

Your GTM motion is creative. The thinking behind it should be too.

[GTM Atlas](https://atlas.attio.com/?utm_source=beehiiv&utm_medium=newsletter&utm_campaign=beehiiv-Y26-atlas&utm_content=&#123;{publication_alphanumeric_id}}&_bhiiv=opp_311ed0df-17e5-4990-ac54-7e163c91b23c_8ebadeed&bhcl_id=ec4782dc-abe5-43f5-9d81-922fbe0f88a2_&#123;{subscriber_id}}_&#123;{email_address_id}}) is the ultimate resource on AI GTM for early-stage builders, providing foundational knowledge for teams navigating growth from scratch. Curated by Attio, the AI CRM, Atlas gives you:

  * Systems thinking for every stage of the customer journey

  * Frameworks and templates that scale with you

  * Conversations with GTM operators at Clay, Lovable, and Vercel.




Mapped by operators. Curated by Attio.

[Explore now](https://atlas.attio.com/?utm_source=beehiiv&utm_medium=newsletter&utm_campaign=beehiiv-Y26-atlas&utm_content=&#123;{publication_alphanumeric_id}}&_bhiiv=opp_311ed0df-17e5-4990-ac54-7e163c91b23c_8ebadeed&bhcl_id=ec4782dc-abe5-43f5-9d81-922fbe0f88a2_&#123;{subscriber_id}}_&#123;{email_address_id}})

# 🎓 AI Skill of the Day: **Turn Codex (or Claude Code) into your daily-driver knowledge work cockpit.**

You probably use Codex or Claude Code for code. Austin Tedesco, head of growth at Every, spends roughly[ 80% of his working day inside Codex](https://youtu.be/x9BNBcP_C7Q?t=657&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) doing go-to-market plans, recruiting outreach, KPI tracking, and emails.

His Codex Camp livestream with Dan Shipper yesterday was a 60-minute walkthrough of the exact setup; here's the short version.

The trick is treating the desktop app (not the CLI) as an "agent management interface" for everything you do.[ Austin's setup](https://youtu.be/x9BNBcP_C7Q?t=828&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal):

  1. **Make a folder per work area** (his is called "every growth OS"). Folders give you persistent named chats per project, so you can ship a PR in one chat and draft a strategy doc in another without leaving the app.

  2. **Connect the plug-ins** for everything you live in: Gmail, Slack, Notion, Stripe, your data sources. Then drop in a markdown project file that explains what your business is, your goals, and how you like to work.

  3. **Add reviewer agents.** Austin[ forked compound engineering into "compound knowledge"](https://youtu.be/x9BNBcP_C7Q?t=3043&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) so reviews check for strategic alignment and data accuracy, not security or front-end design.

  4. **Run**[ Austin's recommended starter prompt](https://youtu.be/x9BNBcP_C7Q?t=1112&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) in a fresh chat inside that folder.

  5. **Always do the final human review in the external app** ([Slack drafts, Gmail drafts](https://youtu.be/x9BNBcP_C7Q?t=1362&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal)), never inside Codex; the context switch is what keeps you honest before something goes to a real person.




**Austin's verbatim starter prompt** _(the @ signs in the below refer to apps, so they require you to connect those apps as Plugins; you’d just replace those with w/e tools you use):_
    
    
    Go take a look at the things I use the most (@Notion, @Slack, and @Gmail) and think of some automations that would help me with my work. For each one, explain what it does, when it should run, and which tool it touches. Ask me which ones look good before you build any of them.

Other plays Austin demoed live:[ synthesize meeting transcripts and Slack threads into a draft go-to-market plan](https://youtu.be/x9BNBcP_C7Q?t=1869&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal),[ build a live KPI tracker in Notion that other agents can read](https://youtu.be/x9BNBcP_C7Q?t=2415&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal), and[ find alums of a specific company who later got into AI](https://youtu.be/x9BNBcP_C7Q?t=2694&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) (he used this exact play to surface a perfect L&D hire candidate in under a minute).

**Total AI beginner?**[Start here](https://www.theneuron.ai/explainer-articles/everything-we-covered-in-our-ai-for-total-beginners-livestream-full-guide-with-timestamps/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) ([goes with this video](https://www.youtube.com/live/QbFU0UNMVaU?si=skJsgUIDjKjAx3DU&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal)). 

**Have a specific skill you want to learn?** [Request it here.](https://docs.google.com/forms/d/e/1FAIpQLSd_-hSXtB9ytR1HQrU85IJnJw233bNKptiGB5BZh9maPse1Eg/viewform?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal)

# 🍪 Treats to Try 

  1. [Claude for Microsoft 365](https://www.anthropic.com/news/finance-agents?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) add-ins (Excel, PowerPoint, Word, with Outlook coming soon) drop Claude into your Office ribbon so you can edit cells, build slides, or summarize docs without leaving the file, included with Pro/Max/Team/Enterprise.

  2. [Adobe's productivity agent and PDF Spaces](https://news.adobe.com/news/2026/05/adobes-new-productivity-agent?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) turn any PDF into an interactive experience with a customizable AI Assistant, audio overviews, brand styling, and engagement analytics; recipients can view PDF Spaces with no Adobe account, available in[ Acrobat Studio and the new Acrobat Express tier](https://blog.adobe.com/en/publish/2026/05/06/adobes-new-productivity-agent-redefining-how-we-understand-create-share?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal).

  3. [Baseten's Frontier Gateway](https://www.baseten.co/blog/introducing-baseten-frontier-gateway/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) is the $5B inference company's new product for model labs (open or closed) that want to ship a production API without building the commercial infrastructure;[ Poolside used it to launch its frontier-scale Laguna coding models in 7 weeks](https://www.baseten.co/resources/customers/how-baseten-powered-poolsides-model-launch-in-record-time/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal), priced per usage with no multi-year commitment.

  4. [Claude on Amazon Bedrock](https://platform.claude.com/docs/en/release-notes/overview?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) is now self-serve for all AWS customers in 27 regions, so enterprise teams can hit Opus 4.7 and Haiku 4.5 from the same console they already use, standard Claude API pricing.

  5. [Routines on Claude Code on the web](https://code.claude.com/docs/en/whats-new?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) fire templated cloud agents on a cron schedule, GitHub event, or API call so you can let Claude run audits and PR reviews while you sleep, Max plan only.

  6. [Genspark's AI Developer](https://www.genspark.ai/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) handles code edits, GitHub pull requests, and hosted deploys inside the same workspace that runs its slides, docs, and AI calling agents; the company just crossed $250M ARR and[ partnered with Microsoft](https://www.businesswire.com/news/home/20260429907387/en/Genspark-Announces-Global-Strategic-Partnership-with-Microsoft-to-Embed-AI-Agents-Across-Microsoft-365-and-Agent-365?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) for Office 365 and Agent 365, free trial then $24.99/mo Plus.




# 📰 Around the Horn 

[](https://www.reddit.com/r/RealOrAI/comments/1t58znv/deepfakes_are_everywhere_but_digital_forensics/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal)

Put this to use in the trivia below! 

  * [Apple](https://www.thestreet.com/latest-news/stock-market-today-may-6-2026-updates?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) is in talks with both Intel and Samsung to make its devices' main processors in the US, sending Intel up 6.4% pre-market on the Bloomberg report.

  * [The White House](https://www.nytimes.com/2026/05/04/technology/trump-ai-models.html?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) is reportedly drafting an executive order to pre-vet frontier AI models before release; we[ wrote up the case against it](https://www.theneuron.ai/explainer-articles/the-case-against-a-government-veto-on-ai-models/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal) yesterday _(TL;DR: the cure may very well be worse than Mythos)._

  * [Boris Cherny](https://www.youtube.com/live/DlTCu_pNDHE?si=LdI0TMjsIsqbDaHK&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal), the head of Claude Code at Anthropic, livestreamed his actual everyday Claude Code workflow yesterday, the first time the creator of an AI coding tool has done a public, unfiltered "watch me drive" session.




**FROM OUR PARTNERS**

### One brand built 30+ landing pages through Viktor without a single developer.

[](https://ref.getviktor.com/vik-bh-mediabuy-secondary1?utm_campaign=&#123;{publication_alphanumeric_id}}&_bhiiv=opp_01be1fa1-75a7-4998-a4cf-31cb355c6866_dc23507e&bhcl_id=1e0933d0-f489-47f8-aebe-bc870c4e9fb3_&#123;{subscriber_id}}_&#123;{email_address_id}})

Each page mapped to a specific ad group. All deployed within hours. [Viktor](https://ref.getviktor.com/vik-bh-mediabuy-secondary1?utm_campaign=&#123;{publication_alphanumeric_id}}&_bhiiv=opp_01be1fa1-75a7-4998-a4cf-31cb355c6866_dc23507e&bhcl_id=1e0933d0-f489-47f8-aebe-bc870c4e9fb3_&#123;{subscriber_id}}_&#123;{email_address_id}}) wrote the code and shipped every one from a Slack message.

That same team has Viktor monitoring ad accounts across the portfolio and posting performance briefs before the day starts. One colleague. Always on. Across every account.

5,700+ teams. 3,000+ integrations.

[Start free. $100 in credits →](https://ref.getviktor.com/vik-bh-mediabuy-secondary1?utm_campaign=&#123;{publication_alphanumeric_id}}&_bhiiv=opp_01be1fa1-75a7-4998-a4cf-31cb355c6866_dc23507e&bhcl_id=1e0933d0-f489-47f8-aebe-bc870c4e9fb3_&#123;{subscriber_id}}_&#123;{email_address_id}})

# 🧩 Thursday Trivia:

You know the drill: one is AI, and one is real. Which is which? 

A.

B.

# A Cat’s Commentary 

**Trivia answer:** A [is real](https://www.reddit.com/r/RealOrAI/comments/1szxddk/is_this_ai_why_isnt_the_cat_running_away_and/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal)  _(although my partner literally doesn’t believe me, it is a ACTUAL cat crying while its owner cuts onions), and_[ _B is AI._](https://www.reddit.com/r/aivideo/comments/1t0a8u0/futurama_live_action_cast/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal)__

|  That’s all for now.   
---|---  
  
**P.P.S:** Love the newsletter, but only want to get it once per week? Don’t unsubscribe—[update your preferences here](https://www.theneurondaily.com/subscribe/f5596641-9099-4045-9641-731cd9fdcf90/preferences?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=anthropic-spacex-data-center-deal).

---

## [😺 🎙️ Watch: How Isomorphic Labs works to drug "undruggable" diseases](https://www.theneurondaily.com/p/watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)
*🧠 The Neuron | 2026-05-06*

[](https://youtu.be/W0NSk2y3OFI?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)

Click the image above to watch on YouTube!

[](https://clickup.com/lp?utm_source=technologyadvice&utm_medium=cpl&utm_campaign=ilab_cpl_na_nnc_pro_trial_all-devices_cpc_lp_x_all-departments_x_general)

Welcome, humans. 

Did you know that the average new drug takes [over a decade and roughly $6B](https://www.isomorphiclabs.com/articles/the-isomorphic-labs-drug-design-engine-unlocks-a-new-frontier?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases) to reach the market? Or that ~**90% of compounds that enter clinical trials** _**fail?**_

That's the hard wall that the entire pharma industry has been hitting for decades.

Well, you probably _do_ know about [AlphaFold](https://deepmind.google/science/alphafold/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases), the [Google DeepMind](https://deepmind.google/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases) AI that solved a 50-year-old protein folding problem and won its creators the [2024 Nobel Prize in Chemistry](https://www.nobelprize.org/prizes/chemistry/2024/press-release/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases). 

**What you might not know:** the team behind AlphaFold 3 is now designing _real_ drugs, and they just published a [technical report](https://storage.googleapis.com/isomorphiclabs-website-public-artifacts/isodde_technical_report.pdf?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases) showing their new system more than doubles AlphaFold 3's accuracy on the hardest part of drug design.

That team is [Isomorphic Labs](https://www.isomorphiclabs.com/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases), a DeepMind spinout led by Demis Hassabis. And in [**our latest podcast episode**](https://youtu.be/W0NSk2y3OFI?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases), we sit down with **Becky Paul** (who leads medicinal drug design) and **Michael Schaarschmidt** (who leads foundational AI research) at Isomorphic Labs to unpack what AlphaFold actually unlocked, why drug discovery is still brutally hard, how AI drug discovery works from a process standpoint, and where (as well as how) their AI is starting to design molecules that human chemists couldn't.

[](https://youtu.be/W0NSk2y3OFI?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)

Click the image above to watch on YouTube!

# Our favorite moments:

  * **(****[2:13](https://youtu.be/W0NSk2y3OFI?feature=shared&t=133&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)****) The brutal math of drug discovery:** A decade of work. ~$6B per drug. 90% of clinical trial entrants fail. Becky lays out exactly why pharma needs something disruptive.

  * **(****[7:27](https://youtu.be/W0NSk2y3OFI?feature=shared&t=447&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)****) AI just replaced a PhD's worth of work:** Their structure prediction model now matches X-ray crystal structures so well, the team is starting to skip the (slow, expensive) experimental step entirely.

  * **(****[12:19](https://youtu.be/W0NSk2y3OFI?feature=shared&t=739&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)****) Why AlphaFold 3 took 2 years for anyone else to copy:** Even with the full paper, open code, and inference algorithms published, no other lab could fully reproduce it. Michael on the modeling details that don't fit in a paper.

  * **(****[15:11](https://youtu.be/W0NSk2y3OFI?feature=shared&t=911&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)****) "I've never worked somewhere where the pace of innovation is so fast":** Becky on what it's like when the ML team next door drops a new foundation model that suddenly unblocks a project that was stuck.

  * **(****[19:08](https://youtu.be/W0NSk2y3OFI?feature=shared&t=1148&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)****) Beyond binding, drugs that delete proteins:** The molecular glue revolution, where new drugs don't just block a target, they tag it for destruction inside your cells.

  * **(**[**26:37**](https://youtu.be/W0NSk2y3OFI?feature=shared&t=1597&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)**) Becky’s pie-in-the-sky dream:** One design cycle. A few hundred molecules. A drug candidate at the end. What "AI-first drug discovery" actually looks like at the limit.

  * **(**[**36:36**](https://youtu.be/W0NSk2y3OFI?feature=shared&t=2196&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)**) "How did it know that?":** The most exciting moments aren't when the model is right, they're when the model makes a leap the team can't explain. 

  * **(****[40:13](https://youtu.be/W0NSk2y3OFI?feature=shared&t=2413&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)****) The "undruggable" protein, drugged:** [KRAS](https://en.wikipedia.org/wiki/KRAS?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases) was labeled untouchable for decades. Recent KRAS drugs are now [doubling survival in pancreatic cancer](https://www.nature.com/articles/d41586-024-04204-5?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases). Becky and Michael's bet: AI shrinks the next "undruggable" target from a multi-decade slog to something tractable.




**Why watch this?** Most "AI in healthcare" news to date has been vague optimism or more administrative than groundbreaking. This is the opposite. Two practitioners walking through exactly which steps of drug design are now AI-first, which still need wet-lab work, and where the next breakthroughs are coming from. 

If you've ever wondered what AlphaFold actually means for patients (not just scientists), or why Demis keeps saying biology is the ultimate AI application, plus how the team at Isomorphic approaches the _incredibly complicated_ task in front of them, then this is the clearest 50 minutes you'll find on it.

**Watch and/or Listen now:** **[YouTube](https://youtu.be/W0NSk2y3OFI?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)** | **[Spotify](https://open.spotify.com/episode/2TzHhOkVIN9AL3GXXxSyDe?si=Hfr5NDX1Q_ybcdKSTMdsNQ&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)**

**P.S.** At [(7:27)](https://youtu.be/W0NSk2y3OFI?feature=shared&t=447&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases) Becky describes the moment a chemist has to stop validating the model and start trusting it. _That's a quietly wild thing for a scientist to say out loud…._

**Dive deeper with these resources:**

  * [Technical report blog](https://www.isomorphiclabs.com/articles/the-isomorphic-labs-drug-design-engine-unlocks-a-new-frontier?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases) (the easiest read, with all the visuals). 

  * [Full technical report (PDF)](https://storage.googleapis.com/isomorphiclabs-website-public-artifacts/isodde_technical_report.pdf?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases) (for the chemists and ML folks). 

  * [Isomorphic Labs](https://www.isomorphiclabs.com/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases) (they're hiring across [Boston, London, and Lausanne](https://www.isomorphiclabs.com/job-openings?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)!).




_**Real quick:**__Want to see your AI-adjacent product or service show up right here, below these podcast promos? Click the button below to advertise to our 700K+ readers!_

[_Advertise in The Neuron here!_](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)

**THIS EPISODE WAS BROUGHT TO YOU BY…**

# We use ClickUp to publish 2,000+ pieces a month.

Across 18 spaces and 100 contributors, [ClickUp](https://clickup.com/lp?utm_source=technologyadvice&utm_medium=cpl&utm_campaign=techa_cpl_na_nnc_pro_trial_all-devices_cpc_lp_x_all-departments_x_general) is the operating system that holds our parent company (TechnologyAdvice)'s work all together. ClickUp's AI layer ([ClickUp Brain](https://clickup.com/lp?utm_source=technologyadvice&utm_medium=cpl&utm_campaign=techa_cpl_na_nnc_pro_trial_all-devices_cpc_lp_x_all-departments_x_general)) plugs into your tasks, docs, Slack, Gmail, and Salesforce; you pick the underlying model (Claude, GPT, or Gemini). Active users save **1.1 days weekly** and see **3x faster task completion**.

Oh, and did we mention the [Free Forever plan](https://clickup.com/lp?utm_source=technologyadvice&utm_medium=cpl&utm_campaign=techa_cpl_na_nnc_pro_trial_all-devices_cpc_lp_x_all-departments_x_general) has unlimited tasks and users?! Check it out!

→ [Try ClickUp free](https://clickup.com/lp?utm_source=technologyadvice&utm_medium=cpl&utm_campaign=techa_cpl_na_nnc_pro_trial_all-devices_cpc_lp_x_all-departments_x_general)

# 🔴 LIVE TOMORROW: The AI Starter Kit, What to Try… and What to Ignore

[](https://www.youtube.com/live/WKZSEEBiaNo?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)

Click the image to go to YouTube, then click "Notify Me" to get notified when we go live!

This week, Grant and Corey are going to cut through the AI noise for anyone who's still on the sidelines. New to AI, or know someone who is? This is the session to send them.

**We'll cover:**

  * The best first steps for AI beginners

  * What tools and features are actually worth trying right now

  * What you can safely ignore for the moment

  * Simple ways to get better answers from any AI tool

  * How to troubleshoot when AI gives you something unhelpful




**Choose your favorite platform to watch live:** [**Watch on YouTube**](https://www.youtube.com/live/WKZSEEBiaNo?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases) | [**Join on LinkedIn**](https://www.linkedin.com/posts/ai-artificialintelligence-aibeginners-ugcPost-74578275?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)

# 🎙️ In Case You Missed It… 

Four recent interviews you’ll definitely want to check out _(pick whatever looks interesting to you and dive in!):_

### 1\. Interested in what's missing before we hit AGI? Watch: [This Company Mapped the Entire World in 3D. Here's Why.](https://youtu.be/erCV1MJXU3g?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)

[](https://youtu.be/erCV1MJXU3g?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)

**TL;DW:** Peter Wilczynski, CPO at [Vantor](https://vantor.com/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases) (formerly Maxar), built a 3D model of the entire Earth at 50cm resolution and made it machine-readable. He argues spatial intelligence is the gap nobody's talking about in AI, and probably the missing piece before agents can actually operate in the physical world.

**Why you should watch:** If you've ever wondered why AI can write code and solve math olympiad problems but still can't reliably tell a drone where to go, this one answers it. Also, there's a wild bit about how the physical world becomes the new navigation layer for AI agents.

  * **YouTube:** [Watch Here](https://youtu.be/erCV1MJXU3g?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)

  * **Spotify:** [Listen Here](https://open.spotify.com/episode/71rhDuYFzTlsF0uaIq91QU?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)

  * **Apple Podcasts:** [Listen Here](https://podcasts.apple.com/us/podcast/this-company-mapped-the-entire-world-in-3d-heres-why/id1742267001?i=1000761587268&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)




### **2\. Curious how good AI music tools have actually gotten? Watch:****[This AI Just Made Our Podcast Theme Song](https://youtu.be/r4aMWjhoMHU?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)**

[](https://youtu.be/vJD2FjVUEhg?si=Mdm2w9GHHSZwZ2A8&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)

**TL;DW:** Corey sits down with **Kendall Rankin** , who left LinkedIn in 2024 to join [Producer AI](https://www.flowmusic.app/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases) when it was a startup (advised by The Chainsmokers, no less). Google acquired the team in February 2026, and Kendall is now on the Flow Music team inside Google Labs. On the episode, they generate a garage rock song from a single sentence, build a custom synth in the "Spaces" feature, and walk through SynthID watermarking and one-shot music videos.

**Why you should watch:** Most AI music demos hand you a polished finished song and skip the part where things go sideways. This episode is the part where things go sideways. First pass fumbles, Corey asks for "more fuzz," second pass actually lands. That iteration loop is the whole story for anyone trying to figure out if these tools are actually usable.

  * **YouTube:** [Watch Here](https://youtu.be/r4aMWjhoMHU?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)

  * **Spotify:** [Listen Here](https://open.spotify.com/show/4gF6uNmkzEYq2E0sHeuMuU?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)

  * **Apple Podcasts:** [Listen Here](https://podcasts.apple.com/us/podcast/the-neuron-ai-explained/id1742267001?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)




### 3\. Want agents that actually work on real tasks? Watch: [Inside the Secret Labs Where AI Learns to Work](https://youtu.be/WhbdbbERzNg?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)

[](https://youtu.be/WhbdbbERzNg?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)

**TL;DW:** Nick Heiner, VP of Product at [Surge AI](https://www.surgehq.ai/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases) (a $1.2B-revenue company built without VC money), reveals why even GPT-5, Claude, and Gemini still fail about 40% of real workplace tasks, what makes a good RL environment, and his bold prediction of a $1B company with one human employee by 2030.

**Why you should watch:** If you're trying to get AI agents to actually finish real work (and not just demo well), this is the missing piece on why they keep falling short.

  * **YouTube:** [Watch Here](https://youtu.be/WhbdbbERzNg?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)

  * **Spotify:** [Listen Here](https://open.spotify.com/episode/6MAFKIJVL4Gt57lEEqCs6F?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)

  * **Apple Podcasts:** [Listen Here](https://podcasts.apple.com/us/podcast/inside-the-secret-labs-where-ai-learns-to-work/id1742267001?i=1000757358598&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)




### 4\. Interested in where AI meets actual factories? Watch: [80% of US Factories Have Zero Robots. Google Wants to Fix That.](https://youtu.be/zv1_d8K-Jms?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)

[](https://youtu.be/zv1_d8K-Jms?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)

**TL;DW:** [Intrinsic](https://www.intrinsic.ai/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases) (a Google Alphabet company) CTO Brian Gerkey co-created [ROS](https://www.ros.org/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases), the open-source software running more than 1 million robots including NASA's. He explains why most US factories still have zero automation, and how generative AI is about to change that.

**Why you should watch:** If you think "AI and robotics" is still science fiction for your industry, this interview resets the timeline. The factory floor is where the next AI wave actually lands.

  * **YouTube:** [Watch Here](https://youtu.be/zv1_d8K-Jms?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)

  * **Spotify:** [Listen Here](https://open.spotify.com/show/4gF6uNmkzEYq2E0sHeuMuU?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)

  * **Apple Podcasts:** [Listen Here](https://podcasts.apple.com/us/podcast/the-neuron-ai-explained/id1742267001?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)




## One more before you go:

If today's episode got you thinking about the AlphaFold side of DeepMind, our [recent interview with Ioannis Antonoglou](https://youtu.be/3rarFbFqVXQ?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases) (one of the AlphaGo co-creators) is the natural next watch. 

Different DeepMind alum, completely different bet on what frontier AI looks like next. _This is very relevant now that the US government will start vetting AI models before they’re releases, or potentially outright banning AI models from certain countries._

**Last thing:** And if you **haven’t subscribed yet, please do!** Click the image below to go to our channel and hit “subscribe” to get notified right when new videos go live. 

[](https://www.youtube.com/@theneuronai?sub_confirmation=1&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases)

We have a goal to hit **50K subscribers** by the end of the year (if not 100K), and **we’re only ~30K away!** If you like learning about AI, and already watch some of our videos, [do us a favor and click here to subscribe](https://www.youtube.com/@theneuronai?sub_confirmation=1&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases) today. 

Stay curious,

The Neuron Team

| That’s all for today, for more AI treats, check out our [website](https://www.theneuron.ai/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-how-isomorphic-labs-works-to-drug-undruggable-diseases).   
---|---  
  
**P.P.S:** Love the newsletter, but don’t want to receive these podcast announcement emails? Don’t unsubscribe — _[adjust your preferences to opt out of them here instead](https://www.theneurondaily.com/subscribe/f5596641-9099-4045-9641-731cd9fdcf90/preferences?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-first-major-ai-incident-this-year-ceo-warns&_bhlid=1d073d4088b90ea4abf69ef7cc157e0659ada818)_ _._

---

## [😺 SubQ ships 12M tokens at 1/5 the cost](https://www.theneurondaily.com/p/subq-ships-12m-tokens-at-1-5-the-cost)
*🧠 The Neuron | 2026-05-06*

[](https://www.teradata.com/platform/clearscape-analytics?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost)

Welcome, humans. 

This week's hottest AI fight was Marc Andreessen vs. the prompt nerds in his replies.

Andreessen[ posted his personal system prompt](https://x.com/pmarca/status/2051374498994364529?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost) (18k likes), and it reads like a Bond villain's HR manual.

You are "a world class expert in all domains" with "intellectual firepower... on par with the smartest people in the world." Be "provocative, aggressive, argumentative, and pointed." Don't worry about offending him. Don't be "sensitive to anyone's feelings or to propriety." "Negative conclusions and bad news are fine." Disclaimers are forbidden, morals and ethics aren't your concern, and of course, "make your answers as long and detailed as you possibly can."

[Sid Bharath](https://x.com/Siddharth87/status/2051388022781104454?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost),[ Aadit Sheth](https://x.com/aaditsh/status/2051386197629694387?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost), and[ kimmonismus](https://x.com/kimmonismus/status/2051679068551090479?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost) walked in with notes. "World-class expert in all domains" does literally nothing (cargo-cult prompting from GPT-3.5 days; the model's training distribution is the same either way). "Never hallucinate" is a wish dressed up as instruction. And "make answers as long and detailed as possible" is actively counterproductive; you get padding, not completeness.

The plot twist: Andreessen's _second_ paragraph is genuinely useful. The anti-sycophancy block does work. Quotes like "never praise my questions or validate my premises," "do not capitulate unless I provide new evidence," "do not anchor on numbers I provide; generate your own independently first," and "accuracy is your success metric, not my approval" give the model verifiable behaviors most people never think to add. As[ kimmonismus put it](https://x.com/kimmonismus/status/2051679068551090479?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost), this is the part that actually changes model behavior in a measurable way. Strip the flattery, keep the protocol. ([Aadit Sheth's reply](https://x.com/aaditsh/status/2051386197629694387?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost) has a nice TRUTH-SEEKING PROTOCOL example if you want what good prompting looks like.)

_BRB gonna add "world-class expert in all domains" to my LinkedIn profile. Then again, Andreessen's actual_[ X bio](https://x.com/pmarca?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost) _is "You're not talking to someone who woke up a loser. That loser attitude, that loser premise makes no sense to me" (a Jensen Huang quote from his Dwarkesh interview). Wait a minute, maybe I should add THAT to my LinkedIn instead!_

Meanwhile in a quieter corner,[ an X user shared a four-line prompt](https://x.com/EXM7777/status/2051724113266590075?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost) that turns raw notes into a fully backlinked Obsidian vault for $0. No RAG, no vectors, no theater. _Skill of the Day below shows you how to steal it._

P.S. Quick ask: if security is your beat,[ our sister pub Cybersecurity Insider wants to know how you're using AI at work](https://docs.google.com/forms/d/e/1FAIpQLSfpueRtROYDvmq9TWygq4l9__Y_8ifVrf8bihm--fpWqD8xqA/viewform?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost) (2-min survey).

**Here’s what happened in AI today:**

  * 🙀 Subquadratic launched SubQ, a 12M-token LLM that wants to retire AI's memory hacks.

  * 📰 Anthropic released ten finance agents and locked in $200B with Google over five years.

  * 📰 AI got sued twice in one day; Google for $1.5M and Character.AI for chatbot doctor impersonation.

  * 🍪 GPT-5.5 Instant cuts ChatGPT's hallucinations on high-stakes prompts by 52%.

  * 📖 Anton Korinek's NBER paper says automating AI research could trigger a singularity in ~6 years.




…and a [**whole lot more that you can read about here**](https://www.theneuron.ai/explainer-articles/around-the-horn-digest-everything-that-happened-in-ai-today-tuesday-may-5-2026/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost).

**Hey:**_Want to reach 700,000+ AI-hungry readers?_[Advertise with us!](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)_[](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)_

**P.S:**_Love robots? We’re starting a new robotics newsletter!_[Sign up early here](https://form.jotform.com/260897013570156?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost).

# 🙀******Subquadratic launched SubQ, a 12M-token LLM that wants to retire AI's memory hacks.**

"AI memory" has been a euphemism for workarounds, because models can't actually hold much in context. Transformer attention scales O(n²) (double the input, quadruple the cost), so the industry duct-taped fixes on top: chunk it, summarize it, pre-search it, pray.

[Subquadratic](https://subq.ai/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost) wants to flush the duct tape. The lab came out of stealth Tuesday with $25M in seed funding and launched **SubQ** , the first commercial LLM built on a fully sub-quadratic architecture, with a native 12M-token context window at roughly 1/5 the cost of frontier models. Backers include former SoftBank Vision Fund partner[ Javier Villamizar](https://subq.ai/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost) and Tinder co-founder[ Justin Mateen](https://subq.ai/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost).

**Here's what happened:**

  * The architecture (SSA, or Subquadratic Selective Attention) scales linearly with input length and runs 52× faster than [FlashAttention](https://arxiv.org/abs/2205.14135?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost) at 1M tokens.

  * SubQ scored 97% on RULER 128K (long-context accuracy; Opus 4.6: 94%) at $8 to run versus ~$2,600 on frontier models.

  * On [MRCR v2](https://arxiv.org/abs/2409.12640?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost) (multi-needle retrieval), SubQ scored 83 vs Opus's 78, GPT-5.4's 39, and Gemini 3.1 Pro's 23.

  * At 12M tokens (beyond any frontier model's reach), SubQ hit 92% recall. Targeting 100M by Q4.

  * Two products live today: a **12M-token API** and [SubQ Code](https://subq.ai/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost), a CLI agent that loads your whole repo in one pass.




**Why this matters:** The memory problem has spawned an engineering discipline. [RAG](https://aws.amazon.com/what-is/retrieval-augmented-generation/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost) breaks documents into chunks and pre-searches them. Agent frameworks split tasks into [sub-agents passing notes](https://platform.claude.com/docs/en/agents-and-tools/tool-use/memory-tool?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost). [MIT's Recursive Language Models](https://venturebeat.com/orchestration/mits-new-recursive-framework-lets-llms-process-10-million-tokens-without?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost) hand the prompt to the model as a file it writes code to search. [Claude's Managed Agents](https://claude.com/blog/claude-managed-agents-memory?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost) give it a folder where it saves notes between sessions. Each is engineering to dodge one fact: standard attention can't afford to read everything at once.

If the architecture itself holds 12M tokens cheaply, much of that scaffolding stops being load-bearing. You skip the chunking, the embedding, and the orchestration; you just ask. (Cross-session memory like CLAUDE.md and /memories solves a different problem and stays useful.) The win is cost and context; Anthropic's Opus 4.7 still leads SWE-Bench at 87.6% (SubQ: 81.8%).

  
**Our take:** We've heard "this replaces transformers" before (looking at you, Mamba). The receipts look different this time, with PhDs from Meta, Google, Oxford, and Cambridge behind it and API access live today. The open question: does SubQ scale to frontier-level capability, or do long-context specialists and dense models split the market?

**FROM OUR PARTNERS**

# 80% of enterprise AI work is moving data around. Teradata's customers do it without moving any. Here's how…

[](https://www.teradata.com/platform/clearscape-analytics?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost)

The most powerful, open, and connected analytics and AI/ML capabilities in the industry. Run better models, faster, at enterprise scale with in-database analytics, ModelOps, and bring-your-own tools flexibility built to reduce cost and accelerate time to value.

[Try the free demo](https://www.teradata.com/platform/clearscape-analytics?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost).

# 🎓 AI Skill of the Day: **Build a free, fully linked second brain in 60 seconds.**

[An X user](https://x.com/EXM7777/status/2051724113266590075?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost) shared a four-line prompt that turns any pile of raw notes into a structured second brain. No vector databases (specialized storage that lets AI search through your text), no RAG (a system that fetches relevant chunks of your notes for the model), no $20/month app.

The skill is _atomicizing_ : turning one blob of text into many small, single-concept files with [[wikilinks]] (clickable backlinks between related notes) so you end up with a browsable knowledge graph. LLMs are excellent at this. It's the manual labor[ Obsidian](https://obsidian.md/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost) users normally hate.

This is also exactly what[ Andrej Karpathy](https://x.com/karpathy/status/2049903821095354523?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost) was hinting at in his recent Sequoia AI Ascent thread ([our breakdown](https://www.theneuron.ai/explainer-articles/-when-three-of-ais-top-builders-tell-you-coding-is-solved-pay-attention-to-what-they-mean/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost)). His point: LLM knowledge bases were _fundamentally impossible_ with classical code, since computation over unstructured data was the missing piece.

How to do it:

  1. Paste any raw notes (a meeting transcript, a research dump, a Voice Memo) into Claude or any frontier model.

  2. Run the prompt below.

  3. Drop the resulting files into your Obsidian vault, automatically via[ Obsidian's command-line tool](https://github.com/obsidianmd/obsidian-cli?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost) or manually by saving them in. Done.



    
    
    Dissect this raw note into atomic Obsidian markdown files. Each file = one concept. Use [[wikilinks]] between any concept that references another. Output as separate code blocks with filenames.

**Want more tips like this? Check out our****[](https://www.theneuron.ai/explainer-articles/the-neurons-ai-skill-of-the-day-digest-april-2026-week-1/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost)**[AI Skill of the Day Digest for April 2026](https://www.theneuron.ai/explainer-articles/the-neurons-ai-skill-of-the-day-digest-april-2026-week-1/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost).

**Total AI beginner?**[Start here](https://www.theneuron.ai/explainer-articles/everything-we-covered-in-our-ai-for-total-beginners-livestream-full-guide-with-timestamps/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost) ([goes with this video](https://www.youtube.com/live/QbFU0UNMVaU?si=skJsgUIDjKjAx3DU&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost)). 

# 🍪 Treats to Try 

  1. [GPT-5.5 Instant](https://openai.com/index/gpt-5-5-instant/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost) is OpenAI's new ChatGPT default that delivers 52% fewer hallucinated claims on medicine/law/finance prompts and 30% more concise responses, free to try for all ChatGPT users.

  2. [Inworld Realtime TTS-2](https://inworld.ai/blog/realtime-tts-2?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost) is the first voice model that listens to your full audio for emotion, takes natural-language voice direction (literally "speak with concern"), and holds one voice identity across 100+ languages at sub-200ms latency,[ demo at ](https://realtime.ai/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost)[realtime.ai](https://realtime.ai?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost), no pricing details.

  3. [Hyperbox](https://hyperbox.sh/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost) gives you an always-on cloud Mac Mini workstation preloaded with major coding agents, persistent storage, and GUI + SSH access so your agents (and iOS dev workflows) can run anywhere you go, no pricing details.

  4. [Perplexity Premium Health Sources](https://www.perplexity.ai/hub/blog/announcing-premium-health-sources?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost) draws from the same peer-reviewed clinical journals, guidelines, and drug databases (NEJM, BMJ, Micromedex) physicians and researchers use for evidence-based medical answers, free to try.

  5. [ChatGPT for Excel and Google Sheets](https://chatgpt.com/apps/spreadsheets/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost) installs into your spreadsheet so you can build, update, and analyze sheets in plain English (formulas, cross-tab insights, formatted output) before you share, free beta for Plus, Pro, Business, and Enterprise users.




# Trending: FOUR popular Neuron podcast eps…

Did you know we have a podcast (_The Neuron: AI Explained)_ where we talk to fascinating people in the industry who teach us how it actually works? Check it out: 

[](https://www.youtube.com/@theneuronai/videos?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost)

Click to view these episodes on YouTube!

New episodes air **every week** on: [Spotify](https://open.spotify.com/show/4gF6uNmkzEYq2E0sHeuMuU?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost) | [Apple Podcasts](https://podcasts.apple.com/us/podcast/the-neuron-ai-explained/id1742267001?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost) | [YouTube](https://www.youtube.com/@theneuronai?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost)****

# 📰 Around the Horn 

[Anthropic](https://www.anthropic.com/news/finance-agents?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost) released ten new finance agents (pitch builder, KYC screener, month-end closer) with deep Microsoft 365 integration. Separately,[ The Information reported](https://www.theinformation.com/articles/anthropic-commits-spending-200-billion-googles-cloud-chips?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost) the lab committed approximately $200 billion to Google over five years for cloud capacity tied to its previously announced 5-gigawatt deal.

**Big Tech raced to build OpenClaw equivalents.**[ The Information broke that Meta is building "Hatch"](https://www.theinformation.com/articles/meta-building-ai-agent-called-hatch-agentic-shopping-tool-instagram?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost), a consumer AI agent plus an agentic Instagram shopping tool ([the FT separately confirmed it as Meta's OpenClaw answer](https://www.ft.com/content/5b48360c-53f2-444a-80a8-f7034750fd62?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost)). Meanwhile,[ Google is internally testing "Remy,"](https://www.businessinsider.com/google-ai-agent-openclaw-remy-gemini-assistant-2026-5?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost) a 24/7 Gemini-powered agent that proactively monitors and acts across Google services while learning your preferences.

**AI got sued twice in one day.** Cape Breton fiddler[ Ashley MacIsaac](https://www.cbc.ca/news/canada/nova-scotia/cape-breton-fiddler-ashley-macisaac-lawsuit-against-google-9.7187490?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost) sued Google for $1.5M after AI Overview falsely identified him as a convicted sex offender (the[ Sipekne'katik First Nation cancelled his concert](https://www.theguardian.com/music/2026/may/05/canadian-ashley-macisaac-fiddler-musician-singer-songwriter-sues-google-ai-sex-offender-ntwnfb?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost) based on the summary). Hours later,[ Pennsylvania sued ](https://techcrunch.com/2026/05/05/pennsylvania-sues-character-ai-after-a-chatbot-allegedly-posed-as-a-doctor/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost)[Character.AI](https://Character.AI?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost) after one of its chatbots posed as a licensed psychiatrist and fabricated a medical license number, the state's first AI medical-impersonation lawsuit.

[Apple](https://techcrunch.com/2026/05/05/apple-plans-to-make-ios-27-a-choose-your-own-adventure-of-ai-models/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost) announced iOS 27 will let users swap third-party AI models (Google, Anthropic, etc.) across Apple Intelligence features. Apple separately[ reached a $250M settlement](https://www.nytimes.com/2026/05/05/technology/apple-intelligence-lawsuit-settlement.html?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost) over claims it misled customers about Apple Intelligence rollout (eligible iPhone owners may receive $25–$95).

Want absolutely EVERYTHING that happened in AI this week?[ Click here!](https://www.theneuron.ai/explainer-articles/around-the-horn-digest-everything-that-happened-in-ai-today-tuesday-may-5-2026/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost)

**FROM OUR PARTNERS**

# Adobe Firefly AI Assistant

[](https://firefly.adobe.com/ai-assistant?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=openai-is-trying-to-become-apple)

Users now have access of public beta of [Firefly AI Assistant](https://firefly.adobe.com/ai-assistant?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=openai-is-trying-to-become-apple) – powered by our creative agent. What does that actually mean in practice? Instead of navigating tools or jumping between our creative apps, you direct the outcome while the assistant handles the workflows—using the right tools at the right time.

  * **Describe what you want to create in a single, intuitive chat interface** — simply explain the outcome you want in your own words, and the assistant orchestrates and executes multi-step workflows across Creative Cloud apps, including Photoshop, Lightroom, Illustrator, Express, Premiere, InDesign, Firefly, Stock, and Fonts, to bring it to life. 

  * **Tap into Adobe's pro-grade tools** — the assistant draws on 60+ powerful, pro-grade tools across Adobe's creative apps, like Auto Tone, Generative Fill, Vectorize, Presets, and more, to help you reach the best creative outcome, with more tools and capabilities on the way. 

  * **Create and edit content across asset types** — work across photos, videos, designs and more, with workflows that move seamlessly from initial concept to final output.

  * **Get started quickly with Creative Skills** — pre-built creative workflows shaped by feedback from our creative community, covering the tasks that come up most: batch editing photos, building mood boards, retouching portraits, creating social variations and designing product mockups, with more on the way.




[Check out FireFly AI Assistant today.](https://firefly.adobe.com/ai-assistant?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=openai-is-trying-to-become-apple)

# 📖******Midweek Wisdom:**

  * [Yann LeCun's blunt survival guide for the AI age](https://www.axios.com/2026/05/04/ai-godfather-survival-guide-hype-doom?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost) (Axios): ignore CEO hype and doomerism, study long-shelf-life fields like physics, and stop telling teens AI will take their jobs (he calls 20% job-loss claims "ridiculously stupid" and argues the doom narratives are doing actual harm).

  * [Anton Korinek et al., "When Does Automating AI Research Produce Explosive Growth?"](https://www.nber.org/papers/w35155?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost) (NBER): automating software R&D plus just 5% automation elsewhere is enough to overcome diminishing returns and produce a singularity within ~6 years under empirically grounded calibrations ([author thread](https://x.com/akorinek/status/2051418157865156897?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost)).

  * [Ethan Mollick on why politics decides what AI is allowed to do](https://x.com/emollick/status/2051684693838340470?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost) (Wharton): doctors, lawyers, psychologists, and bankers all vote and fund political parties; the government will largely decide what AI can do in those professions, no matter what it can do.

  * [Alex Lupsasca on "vibe physics"](https://www.latent.space/p/lupsasca?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost) (Latent Space): the OpenAI researcher reproduced a prize-winning black-hole paper in 30 minutes and generated 110 pages of new quantum-gravity results in a day with simple iterative GPT-5.x prompts.




# A Cat’s Commentary 

| That’s all for now.   
---|---  
  
**P.P.S:** Love the newsletter, but only want to get it once per week? Don’t unsubscribe—[update your preferences here](https://www.theneurondaily.com/subscribe/f5596641-9099-4045-9641-731cd9fdcf90/preferences?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=subq-ships-12m-tokens-at-1-5-the-cost).

---

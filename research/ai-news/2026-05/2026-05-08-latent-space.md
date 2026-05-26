# 🔬 Latent Space — 2026-05-08

> swyx 開發者簡報，未公開專案 + 工程視角
> 來源：[Latent Space](https://www.latent.space/feed)

---

## [[AINews] GPT-Realtime-2, -Translate, and -Whisper: new SOTA realtime voice APIs](https://www.latent.space/p/ainews-gpt-realtime-2-translate-and)
*🔬 Latent Space | 2026-05-08*

OpenAI launched [realtime-1.5](https://x.com/OpenAIDevs/status/2026014334787461508) 3 months ago, but it was a relative drop in the bucket because it was still 4o based intelligence (a +5% bump in Big Bench Audio). You could tell the sheer confidence in today’s realtime-2 release (with a +15.2% bump in BBA), and it was [appropriately well received](https://x.com/OpenAI/status/2052438194625593804?s=20):

As[ the blogpost](https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/) explains, 3 models are being released, which one might simplify to “voice-in, voice-out, and voice-to-voice”:

The focus is less about “voice quality”, and more on usability. TLDR:

Preambles: Developers can enable short phrases before a main response, like “let me check that” or “one moment while I look into it”.

Parallel tool calls and tool transparency: The model can call multiple tools at once and make those actions audible with phrases like “checking your calendar” or “looking that up now,” helping agents stay responsive while completing tasks.

Stronger recovery behavior: The model can recover more gracefully by saying things like “I’m having trouble with that right now,” instead of failing or breaking.

Longer context: 32K → 128K

Stronger domain understanding: The model better retains specialized terminology, proper nouns, healthcare terms, and other vocabulary

More controllable tone and delivery: The model can better adjust its tone—speaking calmly, empathetically, or upbeat, based on context

Adjustable reasoning effort: Developers can now select from minimal, low, medium, high, and xhigh reasoning levels, with low as the default.

The Demo video showed off how the audio model is better tuned when the main speaker is speaking to someone else, so it stops interrupting so much:

AI News for 5/6/2026-5/7/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews’ website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

AI Twitter Recap

Top Story: GPT-Realtime-2 and OpenAI voice AI commentary

What happened

OpenAI launched three new streaming audio models in the Realtime API: GPT-Realtime-2, GPT-Realtime-Translate, and GPT-Realtime-Whisper. OpenAI positioned GPT-Realtime-2 as its “most intelligent voice model yet,” bringing “GPT-5-class reasoning” to real-time voice agents that can listen, reason, handle interruptions, use tools, and sustain longer conversations as they unfold [@OpenAI](https://x.com/OpenAI/status/2052438194625593804). The companion models target live speech translation and transcription: GPT-Realtime-Translate supports streaming translation from 70+ input languages into 13 output languages, while GPT-Realtime-Whisper streams transcription/captions as speech is produced [@OpenAI](https://x.com/OpenAI/status/2052438196454379986), [@OpenAIDevs](https://x.com/OpenAIDevs/status/2052440907933474954). OpenAI said the models are available in the Realtime API now, while ChatGPT voice upgrades are still pending: “Stay tuned, we’re cooking” [@OpenAI](https://x.com/OpenAI/status/2052438197695877316). Sam Altman framed the launch around a behavioral shift: users increasingly use voice with AI when they need to “dump” lots of context, and OpenAI is also working on improvements to ChatGPT voice [@sama](https://x.com/sama/status/2052462271667028211).

Facts vs. opinions

Factual / directly claimed by OpenAI and evaluators

Model family: GPT-Realtime-2, GPT-Realtime-Translate, GPT-Realtime-Whisper are available in the Realtime API today [@OpenAIDevs](https://x.com/OpenAIDevs/status/2052440968763515223).

GPT-Realtime-2 capabilities: reasoning-oriented native speech-to-speech model for production voice agents; supports tool use/action, interruption recovery, longer conversations, and “GPT-5-class reasoning” per OpenAI’s wording [@OpenAI](https://x.com/OpenAI/status/2052438194625593804), [@reach_vb](https://x.com/reach_vb/status/2052438371058737280).

Context window: community/OpenAI-dev commentary reported 128K context for GPT-Realtime-2 voice agents [@reach_vb](https://x.com/reach_vb/status/2052438371058737280); Artificial Analysis independently reported the context window increased from 32K to 128K, with 32K max output tokens [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2052486470469140777).

Translation: GPT-Realtime-Translate supports live speech translation from 70+ input languages into 13 output languages [@OpenAI](https://x.com/OpenAI/status/2052438196454379986), [@reach_vb](https://x.com/reach_vb/status/2052438371058737280).

Transcription: GPT-Realtime-Whisper provides low-latency streaming transcription in the Realtime API for captions, notes, and continuous speech understanding [@OpenAIDevs](https://x.com/OpenAIDevs/status/2052440957258489859).

Prompting/control: OpenAI published a voice prompting guide covering reasoning effort, preambles, tool behavior, unclear audio handling, exact entity capture, and state maintenance in long sessions [@OpenAIDevs](https://x.com/OpenAIDevs/status/2052530378184032560).

Independent benchmarks: Scale AI reported GPT-Realtime-2 took the top spot on its Audio MultiChallenge S2S leaderboard, with instruction retention rising from 36.7% to 70.8% APR versus GPT-Realtime-1.5 and strong performance on voice editing/real-time repair [@ScaleAILabs](https://x.com/ScaleAILabs/status/2052451341071683732).

Independent benchmarks: Artificial Analysis reported 96.6% on Big Bench Audio speech-to-speech reasoning, 96.1% on its Conversational Dynamics benchmark, average time-to-first-audio of 2.33s at high reasoning and 1.12s at minimal reasoning, and unchanged audio pricing of $1.15/hour input and $4.61/hour output [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2052486470469140777), [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2052486478501204415).

Reasoning-effort controls: Artificial Analysis reported adjustable reasoning levels: minimal, low, medium, high, xhigh, with low as default [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2052486470469140777).

Enterprise/product evals: Glean said GPT-Realtime-2 delivered a 42.9% relative increase in helpfulness over the previous version in internal evals for real-time organizational voice interactions [@glean](https://x.com/glean/status/2052440702169108990). Genspark said its Call for Me Agent moved to GPT-Realtime-2 and saw +26% effective conversation rate and fewer dropped calls [@genspark_ai](https://x.com/genspark_ai/status/2052524670088556557).

Opinions / interpretation / commentary

Supporters described the launch as a “big step forward” for voice agents [@sama](https://x.com/sama/status/2052462271667028211), “total realtime victory” [@reach_vb](https://x.com/reach_vb/status/2052442056392405383), and the first speech-to-speech model good enough for “real work” in complex voice agents [@kwindla](https://x.com/kwindla/status/2052521318688739811).

A more cautious view: Simon Willison noted the announcement does not mean ChatGPT Voice Mode itself has upgraded yet; the ChatGPT upgrade “sounds” like it is coming soon [@simonw](https://x.com/simonw/status/2052439091577496054), [@simonw](https://x.com/simonw/status/2052439181885153757).

Interface skepticism: Will Depue compared audio to VR—frequently exciting, but historically not sticky as an interface—while arguing that real-time tool use, reasoning while speaking, and live translation are the kinds of capabilities that could make audio interfaces finally take off [@willdepue](https://x.com/willdepue/status/2052493097586823353).

Broader UX optimism: several commenters framed voice as more natural and bandwidth-efficient for humans [@BorisMPower](https://x.com/BorisMPower/status/2052471142921994332), a path toward Jarvis-like always-available computer agents [@willdepue](https://x.com/willdepue/status/2052494388413235672), or eventually displaced by even higher-bandwidth BCIs [@iScienceLuvr](https://x.com/iScienceLuvr/status/2052465922640593068).

Competitive context: Elon Musk pushed Grok Voice for customer support [@elonmusk](https://x.com/elonmusk/status/2052530063913189879), underscoring that real-time voice support/customer-service automation is now a competitive surface across labs.

Technical details and benchmark data

GPT-Realtime-2

Native speech-to-speech / real-time voice model, released via OpenAI’s Realtime API [@OpenAI](https://x.com/OpenAI/status/2052438194625593804).

Framed as “GPT-5-class reasoning” for voice agents [@OpenAI](https://x.com/OpenAI/status/2052438194625593804).

Designed for agents that can:

reason mid-conversation,

use tools/take actions,

handle interruptions,

recover when users revise or repair speech,

sustain longer sessions with expanded context [@OpenAI](https://x.com/OpenAI/status/2052438196454379986), [@reach_vb](https://x.com/reach_vb/status/2052438371058737280).

Reported context: 128K tokens, up from 32K [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2052486470469140777).

Reported max output: 32K tokens [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2052486470469140777).

Inputs reported by Artificial Analysis: text, audio, and image [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2052486470469140777).

Reasoning effort levels: minimal, low, medium, high, xhigh; default low [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2052486470469140777).

Time-to-first-audio:

1.12s at minimal reasoning,

2.33s at high reasoning [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2052486470469140777).

Pricing:

$1.15/hour audio input,

$4.61/hour audio output,

unchanged versus prior model according to Artificial Analysis [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2052486478501204415).

Conversational features: supports short preambles before main responses—e.g. “let me check that”—and audible transparency during tool calls—e.g. “checking your calendar” [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2052486470469140777).

Benchmarks

Scale AI Audio MultiChallenge S2S: GPT-Realtime-2 placed #1; instruction retention improved from 36.7% to 70.8% APR versus GPT-Realtime-1.5; strong voice editing when users repair/revise speech in real time [@ScaleAILabs](https://x.com/ScaleAILabs/status/2052451341071683732).

Artificial Analysis Big Bench Audio: GPT-Realtime-2 high variant scored 96.6%, reported as equal to Gemini 3.1 Flash Live Preview High and about ~13% above the previous highest result [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2052486470469140777).

Justin Uberti separately summarized the improvement as 15 percentage points vs. GPT-Realtime-1.5 on Big Bench Audio, near saturation [@juberti](https://x.com/juberti/status/2052507302092296252).

Conversational Dynamics / Full Duplex Bench subset: GPT-Realtime-2 minimal variant scored 96.1%, with strengths in pause handling and turn-taking [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2052486470469140777).

GPT-Realtime-Translate

Live streaming speech translation from 70+ input languages to 13 output languages [@OpenAI](https://x.com/OpenAI/status/2052438196454379986).

OpenAI cofounder Greg Brockman said real-time voice-to-voice translation has been an anticipated OpenAI application since the company’s early days and is now available for anyone to build with [@gdb](https://x.com/gdb/status/2052480998668206262).

Vimeo demonstrated live dubbing with no pre-loaded captions, showing translations generated fully live [@Vimeo](https://x.com/Vimeo/status/2052442588201029684).

Junling Zhang highlighted the new real-time translation model and encouraged API usage [@jxnlco](https://x.com/jxnlco/status/2052449634266812744).

Boris Power said live translation “actually works incredibly well” and plans to use it regularly [@BorisMPower](https://x.com/BorisMPower/status/2052472038967890022).

GPT-Realtime-Whisper

Streaming transcription as people speak, for real-time captions, notes, and speech understanding [@OpenAI](https://x.com/OpenAI/status/2052438196454379986).

Justin Uberti described it as “Whisper, but now with realtime streaming” and updated demos to use the new model [@juberti](https://x.com/juberti/status/2052478775523512356).

Uberti also built a delay selector to expose the latency/accuracy tradeoff in a real-time typing demo [@juberti](https://x.com/juberti/status/2052504986391879788).

Product integrations and demos

Glean: shipped real-time voice powered by GPT-Realtime-2, grounded in organizational context; internal evals showed 42.9% relative helpfulness increase over the previous version [@glean](https://x.com/glean/status/2052440702169108990).

Vimeo: demonstrated live dubbing using GPT-Realtime-Translate, with translations generated live and no pre-loaded captions [@Vimeo](https://x.com/Vimeo/status/2052442588201029684).

Genspark: upgraded its Call for Me Agent to GPT-Realtime-2; Genspark Realtime Voice is next; claimed sharper reasoning, tighter instruction following, +26% effective conversation rate, and fewer dropped calls [@genspark_ai](https://x.com/genspark_ai/status/2052524670088556557).

Gradient Bang / game-agent demo: Kyle Windland said GPT-Realtime-2 is the first OpenAI speech-to-speech model good enough for his voice agents that do “real work,” showing it as the ship AI in a complex agent with tool calls and subagents [@kwindla](https://x.com/kwindla/status/2052521318688739811).

Voice-controlled market dashboard: Levin Stanley demoed GPT-Realtime-2 controlling an interface by intent—“Focus on Apple,” “How did it do over the last 30 days?”, “Go back”—arguing that real-time interruption and reasoning change the UI loop from navigation to direction [@levinstanley](https://x.com/levinstanley/status/2052506605044842672).

Realtime demos: Justin Uberti updated hello-realtime for GPT-Realtime-2 and provided a phone demo number [@juberti](https://x.com/juberti/status/2052469176821002676); Diego Cabezas posted a quick GPT-Realtime-2 demo [@diegocabezas01](https://x.com/diegocabezas01/status/2052492653082681485); Ray Fernando hosted a “Building a Live Translator” broadcast [@RayFernando1337](https://x.com/RayFernando1337/status/2052479718495318143).

Reachy Mini / robotics voice interface interest: Clement Delangue asked who would add the new voice capabilities to Reachy Mini [@ClementDelangue](https://x.com/ClementDelangue/status/2052449977725534363), after earlier asking voice AI labs such as Gradium, Kyutai, and ElevenLabs who could help with a robot voice use case [@ClementDelangue](https://x.com/ClementDelangue/status/2052385809655828907).

Why this matters

The launch pushes voice agents from “speech I/O wrapper around a chatbot” toward full-duplex, tool-using, long-context, reasoning agents. The technical shift is not just better ASR or TTS; it is the combination of low-latency turn-taking, interruption handling, longer context, tool-call transparency, and adjustable reasoning effort in a single real-time loop. That matters for customer support, meetings, accessibility, live translation, robotics, browser/computer control, and hands-free workflows where text chat is too slow or awkward.

The most important engineering implication is that voice apps now need to be designed as stateful real-time systems, not prompt-response endpoints. OpenAI’s prompting guide explicitly points developers toward reasoning-effort tuning, preambles, tool behavior, unclear-audio recovery, entity capture, and long-session state management [@OpenAIDevs](https://x.com/OpenAIDevs/status/2052530378184032560). This suggests voice-agent quality will increasingly depend on harness design: latency budgets, interruption semantics, tool-call UX, conversational memory, and failure recovery—not just raw model selection.

The remaining uncertainty is distribution. The API model is available now, but ChatGPT voice mode has not yet received the upgrade, per Simon Willison’s observation [@simonw](https://x.com/simonw/status/2052439091577496054). If and when ChatGPT Voice gets the same capabilities, the consumer impact could be much larger. Until then, the launch primarily benefits developers and platforms building specialized real-time agents.

[
Read more
](https://www.latent.space/p/ainews-gpt-realtime-2-translate-and)

---

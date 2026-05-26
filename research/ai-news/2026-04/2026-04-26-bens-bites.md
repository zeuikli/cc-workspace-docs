# 🍔 Ben's Bites — 2026-04-26

> Ben Tossell 的 AI 日報，工具圈消息源
> 來源：[Ben's Bites](https://www.bensbites.com/feed)

---

## [ChatGPT's Nano Banana](https://www.bensbites.com/p/chatgpts-nano-banana)
*🍔 Ben's Bites | 2026-04-23*

Hey folks, Keshav here.

For a few months, it felt like Google had won the image generation space. But OpenAI is back in the game. **[ChatGPT Images 2.0](https://openai.com/index/introducing-chatgpt-images-2-0/)** is miles ahead of anything. It's beyond impressive at text, I haven't seen any generation with typos, even with hundreds of words per image. See this example I created:

[](https://substackcdn.com/image/fetch/$s_!jFHV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fca4481fe-ef11-4f41-ba1b-b18b487d67a0_1448x1086.png)

It's also really good at creating realistic pictures, like this one of Professor Ben. 

[](https://x.com/bentossell/status/2046824877844238520)

Oh, sorry, that one's real. [Ben was at Stanford](https://x.com/bentossell/status/2046824877844238520) this Wednesday, teaching how to build with AI agents.

Image generation is also available in the Codex app as a skill. Use it with thinking models to get the best results--that lets it think and use code/tool calls (like creating a QR from a link, searching logos from the web) and then use them as reference images. It can also create images, reflect on them and improve the generation.

People are creating [realistic UI screenshots](https://x.com/OpenAI/status/2046589828918317155), [multi-page illustrated magazines](https://x.com/wolfejosh/status/2047028753445118445), [personal style recommendations](https://x.com/clairevo/status/2046764362803867896) and [creative QR codes](https://x.com/ann_nnng/status/2046888449664499805) using the new model. 

The "generate UI as image" bit is interesting. Maybe there's finally a solution to GPT-5.4's lack of design taste. The latest coding models are fairly good at turning screenshots into code, but there are still gaps.

Last weekend, I tested a bunch of tools/models on [implementing a design](https://x.com/Keshavatearth/status/2042529858249691590) (for an ads storefront for Ben's Bites) from a screenshot. I found:

  * [Claude Design > Magicpath AI](https://x.com/Keshavatearth/status/2045390815154126892) > Raw models (like Gemini 3.1 Pro/Opus 4.6 in their web apps), when it comes to understanding the concept and making something usable, not just copying the pixel-by-pixel look (ironically, Gemini won that).

  * When asked to turn designs into a real working app, there was a major drift in how the apps looked. [Opus 4.7](https://x.com/Keshavatearth/status/2045385400295038997) did better than [GPT-5.4](https://x.com/Keshavatearth/status/2045629048320360452) at visually matching the reference screenshot. Though GPT-5.4's code was more functional, and the unseen pages (like the admin panel) had a consistent design with the rest of the app.




Also, in many cases, the assets (hero image, icons, background textures) make the UI in a "generated image" stand out. When replicating that UI from a screenshot, you get the barebones UI with the correct buttons and the layout, but without those assets, and the output falls short of expectations.

* * *

_Ben 's Bites is brought to you by [TinyFish](https://www.tinyfish.ai/?utm_source=newsletter&utm_medium=paid-social&utm_campaign=general-developer-2026q2&utm_term=bensbites)_

> Funny how AI agents can write entire apps but can't work on the live web. Playwright scripts break, raw fetches eat your context, bot detection blocks you, nothing's scalable. **[TinyFish](https://www.tinyfish.ai/?utm_source=newsletter&utm_medium=paid-social&utm_campaign=general-developer-2026q2&utm_term=bensbites)** gives search, fetch, stealth browser, web agent, all managed in one API. **[Try it free](https://www.tinyfish.ai/?utm_source=newsletter&utm_medium=paid-social&utm_campaign=general-developer-2026q2&utm_term=bensbites)**. Comes with a **[CLI + Skill](https://github.com/tinyfish-io/tinyfish-cookbook)**.

* * *

#### Headlines

  * OpenAI has a new product for Business, Enterprise and Edu users - **[Workspace Agents](https://openai.com/business/workspace-agents/)**. Codex-powered agents inside ChatGPT with a persona, task and access to external tools (like Linear) and accessible for Slack as well. These agents will also replace custom GPTs down the line (finally). [Read more](https://openai.com/index/introducing-workspace-agents-in-chatgpt/).

  * **[Gemini Deep Research API](https://blog.google/innovation-and-ai/models-and-research/gemini-models/next-generation-gemini-deep-research/)** now offers two configurations based on 3.1 Pro. It claims the best performance in web research and finding hard facts. Plus, it gets MCP support and can create charts using Nano Banana or HTML.

  * **[Cursor and SpaceX are working together](https://x.com/SpaceX/status/2046713419978453374)** \- Cursor will train coding models on SpaceX's GPUs and likely share them with xAI. SpaceX can, in turn, acquire Cursor later this year for $60B, or pay $10B for the partnership if it doesn't. On a similar note, [Thinking Machines](https://x.com/TechCrunch/status/2046925764067573793) also just signed a multi-billion-dollar Google Cloud deal.

  * **[Give your Droid a computer](https://factory.ai/news/droid-computers)** \- You can now give your Droid an always-on machine with its own filesystem, credentials, and config for it to keep working on your tasks. This can be in the cloud (managed by Factory), or you can bring your own device. 




* * *

[Subscribe now](https://www.bensbites.com/subscribe)

* * *

#### My feed

  * [Chronicle](https://chr.so/notes-to-decks) \- **Cursor for slides**. Never build a deck from scratch again. Turn ideas into stunning presentations in minutes.*

  * [ChatGPT for Excel](https://marketplace.microsoft.com/en-us/product/office/WA200010215) and [Google Sheets](https://workspace.google.com/marketplace/app/chatgpt/870214997678) are now in beta - build new sheets, fix formulas, explain models, and update workbooks in place. ([read more](https://help.openai.com/en/articles/20001063-chatgpt-for-excel))

  * [/ultrareview in Claude Code](https://x.com/ClaudeDevs/status/2046999435239133246) (research preview) lets you run bug-hunting agents in the cloud before merging riskier changes like auth, data migrations, or other critical code paths.

  * OpenAI built an open-source viewer for chat data and Codex session logs - [Euphony](https://x.com/OpenAIDevs/status/2046620363568890230).

  * Sierra is piloting an [AI-native interview](https://sierra.ai/blog/the-ai-native-interview) \- debugging/review focused interviews where candidates improve a medium-sized codebase with coding agents.

  * [ml-intern](https://github.com/huggingface/ml-intern/tree/main) from Hugging Face - open-source research agent to come up with experiments, and run them.

  * [Clawputer](https://x.com/garrytan/status/2046650800752279906) \- Managed OpenClaw agent inside an always-on sandbox.

  * [Kami](https://github.com/tw93/kami) \- design skill for AI-native docs, resumes, portfolios, long docs, and slides.

  * [noscroll](https://x.com/noscroll/status/2046644280798933406) \- an AI that doomscrolls X for you and texts you just the signal. In my experience, this is easy to claim and hard to get right.

  * [Monologue](https://x.com/usemonologue/status/2046624117278085461) has a new Notes feature for thinking out loud when you don't know the exact words you want to dictate.

  * [Fin](https://x.com/destraynor/status/2046995005655429344) is moving beyond customer support into sales - using the same business context and integrations to qualify leads and book meetings.

  * [Perplexity post-trained a Qwen-based model](https://x.com/AravSrinivas/status/2047019688920756504) to handle search and tool calls for cheaper, and it's already serving a meaningful chunk of traffic.

  * [The next Slack won't look like Slack](https://x.com/brian_lovin/status/2046737425066786990), and [Ando](https://x.com/startingfromnix/status/2046643706636456427) looks like one early attempt at that.

  * [Frontend in 2026](https://x.com/leerob/status/2046788389937000576) \- for and against the frameworks and abstractions dominant today.




* * *

#### Afters

[Share Ben's Bites](https://www.bensbites.com/?utm_source=substack&utm_medium=email&utm_content=share&action=share)

* * *

  * Find me on [X](https://x.com/bentossell/), [Linkedin](https://www.linkedin.com/in/ben-tossell-70453537/), or [YouTube](https://www.youtube.com/@bentossell694)

  * Read [about me](https://bensbites.substack.com/about) and Ben's Bites

  * 📷 thumbnail by [@keshavatearth](https://www.x.com/keshavatearth)




> ######  _* sponsors who make this newsletter possible :)_
> 
> ###### _Wanna partner with us for the next quarter?_
> 
> ###### _Email us at[shanice@bensbites.com](mailto:shanice@bensbites.com) or [k@bensbites.com](mailto:k@bensbites.com)_

Ben's Bites is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

---

## [That's my designer - Claude](https://www.bensbites.com/p/thats-my-designer-claude)
*🍔 Ben's Bites | 2026-04-21*

Hey folks,

I've been playing a lot with Claude Cowork for my talk at Stanford later today. It's comically bad for the average jane.

A lot of capabilities are enabled using connectors and plugins, but if you don't know that, good luck getting it to do anything. Can't seem to send emails, install a skill or tell me about what potential connectors are there.

Scheduled tasks in Cowork stop when you shut the lid, but Routines (similar thing) in Claude Code do not. [Cowork is just now getting Artifacts](https://x.com/claudeai/status/2046328619249684989) \- the mini apps on the Claude chat app that started the vibe-coding wave.

I can search for all of this, yes. but an average user will not. and they'll walk away thinking AI is hype for the next 6 months/a year.

Anyway, the [Cerebral Valley AI Summit](https://www.newcomer.co/p/were-back-the-cerebral-valley-ai-34a) is coming back to London on June 24th. I'm planning to be there. 

* * *

_Ben 's Bites is brought to you by [Gauntlet](https://gauntletai.com/apply?utm_source=Third%20Party&utm_campaign=Bens%20Bites&utm_medium=newsletter&utm_content=)_

> Most RAG systems fail in production. **Gauntlet Night School** on Wednesday, April 22 covers how to build one that doesn't -- live and free - [Register](https://us06web.zoom.us/webinar/register/2017762003233/WN_P79TrYY5R8Cru6xEDkwKcw). Or go deeper: **become an AI-native engineer at no cost.** Cohort starts April 27. [Apply now](https://gauntletai.com/apply?utm_source=Third%20Party&utm_campaign=Bens%20Bites&utm_medium=newsletter&utm_content=)

* * *

#### Headlines

  * **[Opus 4.7 is out](https://www.anthropic.com/news/claude-opus-4-7)** \- much better at vision (interpreting images) and efficient at using reasoning tokens. A new xhigh level of thinking now sits between "high" and "max". I've been using it over the weekend at xhigh and didn't face any issues (despite the general sentiment on Twitter that 4.7 is a regression).

  * **[Claude also has a Design tab now](https://www.anthropic.com/news/claude-design-anthropic-labs)** \- a canvas-like interface with chat on the sidebar to explore wireframes or create high fidelity prototypes. It asks you 5-10 questions via an interactive form and then gets building. I found the [image -> design workflow](https://x.com/Keshavatearth/status/2045377232965972305) to be really good in the prototype mode. Has separate limits while in research preview, but expect the weekly limits to only last for 2-3 big generations max (on the $20 plan). Check out [Peter's demo](https://x.com/petergyang/status/2045181813484884396) across multiple use cases.

  * **Codex** got a few updates: 1. **[Computer Use](https://openai.com/index/codex-for-almost-everything/)** \- it can now use apps on your Mac. I'm not completely sold on it and have [some questions](https://x.com/bentossell/status/2045745033530527989), but it does seem to work a lot faster than previous iterations of computer/browser use demos. Also, it works in the background, so your Mac is free for you to use. 2. **[Chronicle](https://developers.openai.com/codex/memories/chronicle)** , an opt-in preview that uses recent screen context to build memories. 3. A bunch of plugins, including image generation, so that Codex can be the superapp to use AI.

  * **[Factory AI is now valued at $1.5B](https://x.com/matanSF/status/2044821889844228378)** after their latest raise of $150M. Try the new [desktop app for Droid](https://factory.ai/product/desktop), Factory's coding agent, with 50% off on Opus 4.7 till 30th April.




* * *

[Subscribe now](https://www.bensbites.com/subscribe)

* * *

#### My feed

  * **Your tools are full of data, but you 're still guessing.** [Backstory](https://www.backstory.ai/get-demo?utm_source=partner&utm_medium=socialpaid&utm_term=bens_bites&utm_content=social&utm_campaign=brand_paid&rls=social&rlsd=) \- Focus on what drives revenue, based on how your business actually sells.*

  * [Google AI Pro and Ultra](https://x.com/OfficialLoganK/status/2046334868481806491) subs now work with AI Studio - higher rate limits for vibe coding in the playground.

  * [Julius](https://x.com/0interestrates/status/2045250990333694331) can now generate slide decks with charts and tables, exportable as pptx.

  * [Galaxy Brain](https://galaxybrain.com/) \- an operating system powered by local files. I'm an investor.

  * [Kimi 2.6 Code](https://x.com/skirano/status/2046318389245972770) \- a Claude Code-style terminal built specifically for [Kimi K2.6](https://www.kimi.com/blog/kimi-k2-6).

  * [Moondream Lens](https://x.com/moondreamai/status/2046265928938291604) \- fine-tune a vision model to production accuracy in hours with as few as 20 images.

  * Zapier's [AutomationBench](https://x.com/wadefoster/status/2046214612685590798) measures real work done by models - CRM updates, inbox follow-ups, multi-step tool chains. No model has cracked 10%.

  * [How AI made me a builder](https://faydakrouri.com/thoughts/how-ai-made-me-a-builder/) without losing my taste as a designer.

  * Quiver upgrades its models for vector generation - [Arrow 1.1 and Arrow 1.1 Max](https://x.com/QuiverAI/status/2044864082180706721).

  * [acceptmarkdown.com](https://acceptmarkdown.com/) \- checks whether your site returns Markdown correctly for agents.

  * [The 5 stages of AI grief](https://x.com/chrysb/status/2045972791208624541).

  * HeyGen open-sourced [HyperFrames](https://x.com/HeyGen/status/2044827454460871072) (HTML to MP4).

  * [Vercel was breached](https://x.com/rauchg/status/2045995362499076169) via an employee's account on another AI product. Vercel says affected customers have already been contacted. [Quick check](https://x.com/BrendanFalk/status/2045953132770025769) to make sure you're safe.

  * Three OpenAI leaders left the company - [Kevin Weil](https://x.com/kevinweil/status/2045230426210648348) (CPO, then OpenAI for Science lead), [Bill Peebles](https://x.com/billpeeb/status/2045225014807670949) (Sora co-creator), and [Srinivas Narayanan](https://x.com/snsf/status/2045261554484986155) (CTO for B2B Applications).

  * Skill drops: [skill-creator](https://x.com/nickbaumann_/status/2046422115205960165), [make-interfaces-feel-better](https://x.com/jakubkrehel/status/2045895877588361723), and [gpt-taste](https://x.com/LexnLin/status/2045238677589147726) for Codex.




* * *

#### Afters

[Share Ben's Bites](https://www.bensbites.com/?utm_source=substack&utm_medium=email&utm_content=share&action=share)

* * *

  * Find me on [X](https://x.com/bentossell/), [Linkedin](https://www.linkedin.com/in/ben-tossell-70453537/), or [YouTube](https://www.youtube.com/@bentossell694)

  * Read [about me](https://bensbites.substack.com/about) and Ben's Bites

  * 📷 thumbnail by [@keshavatearth](https://www.x.com/keshavatearth)




> ######  _* sponsors who make this newsletter possible :)_
> 
> ###### _Wanna partner with us for the next quarter?_
> 
> ###### _Email us at[shanice@bensbites.com](mailto:shanice@bensbites.com) or [k@bensbites.com](mailto:k@bensbites.com)_

Ben's Bites is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

---

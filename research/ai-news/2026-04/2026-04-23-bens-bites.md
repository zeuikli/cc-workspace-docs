# 🍔 Ben's Bites — 2026-04-23

> Ben Tossell 的 AI 日報，工具圈消息源
> 來源：[Ben's Bites](https://www.bensbites.com/feed)

---

## [ChatGPT's Nano Banana](https://www.bensbites.com/p/chatgpts-nano-banana)
*🍔 Ben's Bites | 2026-04-23*

Hey folks, Keshav here.

For a few months, it felt like Google had won the image generation space. But OpenAI is back in the game. [ChatGPT Images 2.0](https://openai.com/index/introducing-chatgpt-images-2-0/) is miles ahead of anything. It’s beyond impressive at text, I haven’t seen any generation with typos, even with hundreds of words per image. See this example I created:

It’s also really good at creating realistic pictures, like this one of Professor Ben. 

Oh, sorry, that one’s real. [Ben was at Stanford](https://x.com/bentossell/status/2046824877844238520) this Wednesday, teaching how to build with AI agents.

Image generation is also available in the Codex app as a skill. Use it with thinking models to get the best results—that lets it think and use code/tool calls (like creating a QR from a link, searching logos from the web) and then use them as reference images. It can also create images, reflect on them and improve the generation.

People are creating [realistic UI screenshots](https://x.com/OpenAI/status/2046589828918317155), [multi-page illustrated magazines](https://x.com/wolfejosh/status/2047028753445118445), [personal style recommendations](https://x.com/clairevo/status/2046764362803867896) and [creative QR codes](https://x.com/ann_nnng/status/2046888449664499805) using the new model. 

The “generate UI as image” bit is interesting. Maybe there’s finally a solution to GPT-5.4’s lack of design taste. The latest coding models are fairly good at turning screenshots into code, but there are still gaps.

Last weekend, I tested a bunch of tools/models on [implementing a design](https://x.com/Keshavatearth/status/2042529858249691590) (for an ads storefront for Ben’s Bites) from a screenshot. I found:

[Claude Design > Magicpath AI](https://x.com/Keshavatearth/status/2045390815154126892) > Raw models (like Gemini 3.1 Pro/Opus 4.6 in their web apps), when it comes to understanding the concept and making something usable, not just copying the pixel-by-pixel look (ironically, Gemini won that).

When asked to turn designs into a real working app, there was a major drift in how the apps looked. [Opus 4.7](https://x.com/Keshavatearth/status/2045385400295038997) did better than [GPT-5.4](https://x.com/Keshavatearth/status/2045629048320360452) at visually matching the reference screenshot. Though GPT-5.4’s code was more functional, and the unseen pages (like the admin panel) had a consistent design with the rest of the app.

Also, in many cases, the assets (hero image, icons, background textures) make the UI in a “generated image” stand out. When replicating that UI from a screenshot, you get the barebones UI with the correct buttons and the layout, but without those assets, and the output falls short of expectations.

Ben’s Bites is brought to you by [TinyFish](https://www.tinyfish.ai/?utm_source=newsletter&utm_medium=paid-social&utm_campaign=general-developer-2026q2&utm_term=bensbites)

Funny how AI agents can write entire apps but can’t work on the live web. Playwright scripts break, raw fetches eat your context, bot detection blocks you, nothing’s scalable. [TinyFish](https://www.tinyfish.ai/?utm_source=newsletter&utm_medium=paid-social&utm_campaign=general-developer-2026q2&utm_term=bensbites) gives search, fetch, stealth browser, web agent, all managed in one API. [Try it free](https://www.tinyfish.ai/?utm_source=newsletter&utm_medium=paid-social&utm_campaign=general-developer-2026q2&utm_term=bensbites). Comes with a [CLI + Skill](https://github.com/tinyfish-io/tinyfish-cookbook).

Headlines

OpenAI has a new product for Business, Enterprise and Edu users - [Workspace Agents](https://openai.com/business/workspace-agents/). Codex-powered agents inside ChatGPT with a persona, task and access to external tools (like Linear) and accessible for Slack as well. These agents will also replace custom GPTs down the line (finally). [Read more](https://openai.com/index/introducing-workspace-agents-in-chatgpt/).

[Gemini Deep Research API](https://blog.google/innovation-and-ai/models-and-research/gemini-models/next-generation-gemini-deep-research/) now offers two configurations based on 3.1 Pro. It claims the best performance in web research and finding hard facts. Plus, it gets MCP support and can create charts using Nano Banana or HTML.

[Cursor and SpaceX are working together](https://x.com/SpaceX/status/2046713419978453374) - Cursor will train coding models on SpaceX’s GPUs and likely share them with xAI. SpaceX can, in turn, acquire Cursor later this year for $60B, or pay $10B for the partnership if it doesn’t. On a similar note, [Thinking Machines](https://x.com/TechCrunch/status/2046925764067573793) also just signed a multi-billion-dollar Google Cloud deal.

[Give your Droid a computer](https://factory.ai/news/droid-computers) - You can now give your Droid an always-on machine with its own filesystem, credentials, and config for it to keep working on your tasks. This can be in the cloud (managed by Factory), or you can bring your own device. 

My feed

[Chronicle](https://chr.so/notes-to-decks) - Cursor for slides. Never build a deck from scratch again. Turn ideas into stunning presentations in minutes.*

[ChatGPT for Excel](https://marketplace.microsoft.com/en-us/product/office/WA200010215) and [Google Sheets](https://workspace.google.com/marketplace/app/chatgpt/870214997678) are now in beta - build new sheets, fix formulas, explain models, and update workbooks in place. ([read more](https://help.openai.com/en/articles/20001063-chatgpt-for-excel))

[/ultrareview in Claude Code](https://x.com/ClaudeDevs/status/2046999435239133246) (research preview) lets you run bug-hunting agents in the cloud before merging riskier changes like auth, data migrations, or other critical code paths.

OpenAI built an open-source viewer for chat data and Codex session logs - [Euphony](https://x.com/OpenAIDevs/status/2046620363568890230).

Sierra is piloting an [AI-native interview](https://sierra.ai/blog/the-ai-native-interview) - debugging/review focused interviews where candidates improve a medium-sized codebase with coding agents.

[ml-intern](https://github.com/huggingface/ml-intern/tree/main) from Hugging Face - open-source research agent to come up with experiments, and run them.

[Clawputer](https://x.com/garrytan/status/2046650800752279906) - Managed OpenClaw agent inside an always-on sandbox.

[Kami](https://github.com/tw93/kami) - design skill for AI-native docs, resumes, portfolios, long docs, and slides.

[noscroll](https://x.com/noscroll/status/2046644280798933406) - an AI that doomscrolls X for you and texts you just the signal. In my experience, this is easy to claim and hard to get right.

[Monologue](https://x.com/usemonologue/status/2046624117278085461) has a new Notes feature for thinking out loud when you don’t know the exact words you want to dictate.

[Fin](https://x.com/destraynor/status/2046995005655429344) is moving beyond customer support into sales - using the same business context and integrations to qualify leads and book meetings.

[Perplexity post-trained a Qwen-based model](https://x.com/AravSrinivas/status/2047019688920756504) to handle search and tool calls for cheaper, and it’s already serving a meaningful chunk of traffic.

[The next Slack won’t look like Slack](https://x.com/brian_lovin/status/2046737425066786990), and [Ando](https://x.com/startingfromnix/status/2046643706636456427) looks like one early attempt at that.

[Frontend in 2026](https://x.com/leerob/status/2046788389937000576) - for and against the frameworks and abstractions dominant today.

Afters

@kevin2kelly called all of this in 2016 ","username":"jeffreyhuber","name":"Jeff Huber","profile_image_url":"https://pbs.substack.com/profile_images/1588236352797126656/i-XMejJn_normal.jpg","date":"2026-04-22T17:35:09.000Z","photos":[{"img_url":"https://pbs.substack.com/media/HGhtSLoasAAZrkr.jpg","link_url":"https://t.co/0YkzURdjoW"}],"quoted_tweet":{},"reply_count":1,"retweet_count":16,"like_count":139,"impression_count":58848,"expanded_url":null,"video_url":null,"belowTheFold":true}" data-component-name="Twitter2ToDOM">

gitperf.com ","username":"tnm","name":"Ted Nyman","profile_image_url":"https://pbs.substack.com/profile_images/1845213602040696832/icHPaFXs_normal.jpg","date":"2026-04-22T04:58:43.000Z","photos":[{"img_url":"https://pbs.substack.com/media/HGfAQETbMAEPIX8.jpg","link_url":"https://t.co/88f9cHRDt4"}],"quoted_tweet":{},"reply_count":6,"retweet_count":44,"like_count":404,"impression_count":18029,"expanded_url":null,"video_url":null,"belowTheFold":true}" data-component-name="Twitter2ToDOM">

Find me on [X](https://x.com/bentossell/), [Linkedin](https://www.linkedin.com/in/ben-tossell-70453537/), or [YouTube](https://www.youtube.com/@bentossell694)

Read [about me](https://bensbites.substack.com/about) and Ben’s Bites

📷 thumbnail by [@keshavatearth](https://www.x.com/keshavatearth)

* sponsors who make this newsletter possible :)

Wanna partner with us for the next quarter? 

Email us at [shanice@bensbites.com](mailto:shanice@bensbites.com) or [k@bensbites.com](mailto:k@bensbites.com)

---

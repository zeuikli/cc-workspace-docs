# 🍔 Ben's Bites — 2026-04-09

> Ben Tossell 的 AI 日報，工具圈消息源
> 來源：[Ben's Bites](https://www.bensbites.com/feed)

---

## [Anthropic built a model too risky to release](https://www.bensbites.com/p/anthropic-built-a-model-too-risky)
*🍔 Ben's Bites | 2026-04-09*

Hey folks, Keshav here. Ben is at AI Engineer this week, so I’m covering the intro.

A mis-timed blog last week leaked Anthropic’s next model - Claude Mythos. Well, it is real and has massive improvements on benchmarks over Opus 4.6:

53.4% → 77.8% on SWE-bench Pro

65.4% → 82% on Terminal-Bench 2.0

but we are not getting access to it anytime soon. Why? because it is really good at finding and exploiting software vulnerabilities. On Firefox exploit generation, Opus managed 2 working exploits out of hundreds of attempts. Mythos hit 181. 

It found many-decades-old bugs in critical software projects like OpenBSD (27-year-old bug), FFmpeg (16-year-old bug) and more. 

Instead of releasing it publicly, Anthropic is giving 12 companies access to a preview version of Mythos under “[Project Glasswing](https://www.anthropic.com/glasswing)” to find vulnerabilities in critical software. Anthropic is committing $100M in model usage credits and $4M in donations to open-source security orgs under this project.

Theo made a [video](https://www.youtube.com/watch?v=aFcVKzfkJPk) on this, and I like his point: “Mythos is to Opus what Opus is to Sonnet.”

I tweeted a [list of companies that Meta has acquired](https://x.com/Keshavatearth/status/2041817134708486192) in the past year without anything to show for it, and soon after, Meta released details about their latest model - [Muse Spark](https://ai.meta.com/blog/introducing-muse-spark-msl/). At a glance, it sits somewhere between Sonnet 4.6 and Opus 4.6. Not usable yet: API access is coming, and there are promises about open-source too (rip llama).

Many people are dunking on Meta for its not-so-frontier model release after spending billions and a year of silence, but I think it’s a good step ahead. Plus, have you used Instagram search over the past couple of months? It’s gotten really good courtesy of AI.

As always, good recap from Ethan Mollick on the [state of frontier models](https://x.com/emollick/status/2042088011748290750): Google, OpenAI and Anthropic lead, Meta joins the pack for now while xAI has fallen off, and the best Chinese models are still 7-9 months behind.

ps: [Factory’s desktop app](https://x.com/FactoryAI/status/2041928406158471299) is now out of beta. It comes with a cloud computer, the ability to use other apps on your device, and, of course, the ability to run and manage multiple Droid sessions easily.

Ben’s Bites is brought to you by [Attio](https://attio.com/?utm_source=bens_bites&utm_medium=newsletter_sponsorship&utm_campaign=bens_bites-Y26), the AI CRM

Honestly, no one gets excited about a CRM. But then they try [Attio](https://attio.com/?utm_source=bens_bites&utm_medium=newsletter_sponsorship&utm_campaign=bens_bites-Y26). It connects to Claude Code and n8n through its MCP server, completely bridging the gap between my customer data and apps. Wait, there's more, like flagging churn risk and turning customer feedback into Linear projects. [Try it now](https://attio.com/?utm_source=bens_bites&utm_medium=newsletter_sponsorship&utm_campaign=bens_bites-Y26).

Headlines

[Claude Managed Agents](https://x.com/claudeai/status/2041927687460024721) - You can use Claude’s developer console to build and deploy agents and let anthropic handle the infra for it, vs building it yourself. For example, [Notion](https://x.com/adamwathan/status/2041977909502489060) is using managed agents to build a “delegate tasks to Claude” feature. (Anthropic’s [engineering blog](https://www.anthropic.com/engineering/managed-agents) on building this).

[Cursor has a new design mode](https://x.com/cursor_ai/status/2041561791243940092) to annotate and target UI elements in the browser. Plus, run Cursor on any machine and [control it from anywhere](https://x.com/cursor_ai/status/2041912812637966552), including your phone. 

[Gemini app finally has projects - they call it notebooks](https://blog.google/innovation-and-ai/products/gemini-app/notebooks-gemini-notebooklm/). Similar features as Claude/ChatGPT projects - move chats in/out of notebooks, notebook-specific files and memories, with the additional feature to sync these notebooks between the Gemini app and NotebookLM.

[Clicky is an ambient AI buddy on your Mac](https://www.clicky.so/). It sees your screen, talks to you and points at things to guide you ([demo](https://x.com/FarzaTV/status/2041314633978659092)). Farza built (and [open-sourced](https://github.com/farzaa/clicky)) it as a learning tool, but people are using it for [everything](https://x.com/FarzaTV/status/2041639363457773867).

Choosing an accurate speech-to-text model is harder than it looks. Benchmarking one is even harder. See why standard word error rate falls short, and [what better STT evaluation actually looks like](https://www.assemblyai.com/blog/new-word-error-rate-wer-benchmark?utm_source=bensbites&utm_medium=newsletter_sponsor&utm_campaign=toptools&utm_content=wer_chart_truthfiles).*

My feed

[Chronicle](https://chr.so/notes-to-decks): Cursor for slides. Never build a deck from scratch again. Turn ideas into stunning presentations in minutes.*

[OpenRouter Spawn](https://x.com/alexatallah/status/2041627373695856776) - Deploy OpenClaw and other agents to the cloud of your choice. Works with all models on OpenRouter.

[Zapier’s SDK is now open to everyone](https://x.com/wadefoster/status/2041501747105890393). Programmatic access to all of Zapier’s capabilities. Free to use in beta. ([docs](https://docs.zapier.com/sdk/quickstart))

[Kiro.dev](https://kiro.dev/) (spec-driven IDE from Amazon) is bringing its [startup credits program](https://kiro.dev/blog/bringing-back-startup-credits/) back for startups with up to 30 people. 

[Cogito](https://x.com/linuz90/status/2041867942489669722) - Markdown editor for Mac. I’ve been using Clearly ([recently updated](http://Cogito - Markdown editor for Mac)) for the last few weeks to simply view and edit md files.

[Graphify](https://github.com/safishamsi/graphify) - Turn any codebase or folder into a queryable knowledge graph.

[Pi and Mario](https://mariozechner.at/posts/2026-04-08-ive-sold-out/) (the maker of Pi) are joining Earendil, the company by the creator of Flask. The core harness stays open-source. New features will be a mix of enterprise & fair source (proprietary now, open-source later).

[Impeccable](https://impeccable.style) - Free design skills for coding agents with 21 commands to audit and fix common mistakes.

[Superset](https://superset.sh) and [Builder 2.0](https://x.com/Steve8708/status/2041909436059615442) - two new UIs for running parallel agents. Superset is more like Codex (terminal-first, worktrees), Builder is more kanban-style with Slack/Jira integration.

[CSS Studio](https://x.com/motiondotdev/status/2041513799056826571) by Motion - Make design changes by hand on your website in the browser, then pass them over to your agent for implementation.

[S3 Files from AWS](https://aws.amazon.com/about-aws/whats-new/2026/04/amazon-s3-files/) allows storing data as a file system, making it easier for agents to use.

[Every is running two parallel org charts](https://www.youtube.com/watch?v=SRlTgIhESjw) - one for humans and another for each employee’s openclaw agents.

Afters

ui.sh demo — generating multiple design ideas to choose from, no matter what tech stack you use: ","username":"adamwathan","name":"Adam Wathan","profile_image_url":"https://pbs.substack.com/profile_images/1677042510839857154/Kq4tpySA_normal.jpg","date":"2026-04-08T20:34:06.000Z","photos":[{"img_url":"https://substackcdn.com/image/upload/w_1028,c_limit,q_auto:best/l_twitter_play_button_rvaygk,w_88/m4hnc3mskg5xn95rxdd3","link_url":"https://t.co/Wd0HwBfVVW"}],"quoted_tweet":{},"reply_count":139,"retweet_count":112,"like_count":2168,"impression_count":159565,"expanded_url":null,"video_url":"https://video.twimg.com/amplify_video/2041977682879983616/vid/avc1/1072x720/iw1ZUf9OyAqaffgy.mp4","belowTheFold":true}" data-component-name="Twitter2ToDOM">

Find me on [X](https://x.com/bentossell/), [Linkedin](https://www.linkedin.com/in/ben-tossell-70453537/), or [YouTube](https://www.youtube.com/@bentossell694)

Read [about me](https://bensbites.substack.com/about) and Ben’s Bites

📷 thumbnail by [@keshavatearth](https://www.x.com/keshavatearth)

* sponsors who make this newsletter possible :)

Wanna partner with us for the next quarter? 

Email us at [shanice@bensbites.com](mailto:shanice@bensbites.com) or [k@bensbites.com](mailto:k@bensbites.com)

---

---
title: "Ben's Bites — 2026-04-16"
date: 2026-04-16
source: "Ben's Bites"
type: ai-news
---

# 🍔 Ben's Bites — 2026-04-16

> Ben Tossell 的 AI 日報，工具圈消息源
> 來源：[Ben's Bites](https://www.bensbites.com/feed)

---

## [My cheatsheet for a clean context](https://www.bensbites.com/p/my-cheatsheet-for-a-clean-context)
*🍔 Ben's Bites | 2026-04-16*

Hey folks

Boarding my flight to SF very shortly, and I got an email to let me know - no WiFi today. Uh oh. I was kinda hoping my 11 hours uninterrupted hours without the kids would be productive for once (I’m usually a very OOO long-hauler, no internet). But I still have some work to polish this talk I’m giving on Tuesday. 

I’m also in town looking to deploy $100k cheques to dev tools and infra founders, plus see some of my wonderful LPs and meeting new ones. Ben’s Bites Fund II has already started investing. 

So my flight… I’ve had to hurriedly download a few local models so I can use my agents offline and I think, so far, Gemma 4: 26b is going to be my choice. 

We’re so spoiled today with fast intelligence at our fingertips and it’s funny how used to the new intelligence levels we get 

Local models are slow to boot up (you’ve got to be more mindful of what context is being loaded on startup (so I’m running with no-skills to get it to go faster, I can call the skills when I want — maybe I’d actually prefer to do that generally 🤔). And they feel pretty slow to do work, but only because of said spoils. 

I’ve been in the weeds of context management recently because of the course I’m working on. And it’s been useful to just remind myself about how prickly it can be; 

If an agent runs web searches - presumably you didn’t read them, its gobbling up context from content you do not know is 1. right, 2. not ai-slop, and 3. by a source you’d recommend.

Little (or big) lines of slop, misdirection, misinformation slip in to the context and compound over time

Reaching ~60% of a context window is probably the limit of where you want to be

Use other sessions as context-gathering sessions, if there’s lots of documents then create one summary file with the information (and try to read or at least skim it! - I am trying, promise)

I don’t trust 1M context windows, there’s a great post by Thariq from Anthropic below about this window. I shouldn’t need my context for my tasks to need perfect recall beyond ~150k tokens, that’s a lot of words. Only until 1M context windows are the norm, the models dont forget anything and help clean polluted context along the way!

Anyway, got to head to the gate! This was a little different of an intro, let me know if you liked it. I need to share more as I’m learning (or diving deeper). 

Ben’s Bites is brought to you by [Attio](https://attio.com/?utm_source=bens_bites&utm_medium=newsletter_sponsorship&utm_campaign=bens_bites-Y26), the AI CRM

Honestly, no one gets excited about a CRM. But then they try [Attio](https://attio.com/?utm_source=bens_bites&utm_medium=newsletter_sponsorship&utm_campaign=bens_bites-Y26). It connects to Claude Code and n8n through its MCP server, completely bridging the gap between my customer data and apps. Wait, there's more, like flagging churn risk and turning customer feedback into Linear projects. [Try it now](https://attio.com/?utm_source=bens_bites&utm_medium=newsletter_sponsorship&utm_campaign=bens_bites-Y26).

Headlines

[Claude Code’s desktop got a redesign](https://claude.com/blog/claude-code-desktop-redesign). Brings many CLI-only features and more (like split windows for multiple sessions) to the desktop app. Big improvement, but still a lot is missing. It picks up some CLI sessions but not all, opening/editing files isn’t obvious, and it keeps asking for permission even with “bypass” settings on.

[Gemini also has a native Mac app now](https://blog.google/innovation-and-ai/products/gemini-app/gemini-app-now-on-mac-os/). But it’s light on features - no Gems, no notebooks - and the design feels rough to say the least.

New models - [GPT-5.4-Cyber](https://openai.com/index/scaling-trusted-access-for-cyber-defense/) from OpenAI, fine-tuned for cybersecurity, with [limited access](https://openai.com/index/accelerating-cyber-defense-ecosystem/) to trusted partners. And [Gemini 3.1 Flash TTS](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-1-flash-tts/) from Google - better voices, audio tags for controlling tone and pacing, and 70 languages.

[Routines](https://claude.com/blog/introducing-routines-in-claude-code) in Claude Code are now in research preview - set up a prompt, a repo, and your connectors once, then run it on a schedule (or via API/GitHub trigger). Runs on Anthropic’s infra, so you don’t need your laptop open. Basically, extended cron jobs. OpenClaw calls these heartbeats.

With the latest update to [OpenAI’s Agents SDK](https://x.com/OpenAIDevs/status/2044466699785920937), you can run Codex-style agents in production without building the whole harness yourself. You get sandboxed execution, computer-use, skills, memory, and compaction built in.

Most RAG systems return wrong answers with complete confidence. Gauntlet's free Night School covers how production AI engineers actually fix that — setup, evaluation, the full loop. Wednesday, April 22. [Register free](https://us06web.zoom.us/webinar/register/2017762003233/WN_P79TrYY5R8Cru6xEDkwKcw)*

My feed

[Skills in Chrome](https://blog.google/products-and-platforms/products/chrome/skills-in-chrome/) let you save prompts as reusable one-click workflows that run on whatever page you’re viewing.

[Cursor](https://x.com/cursor_ai/status/2044486585492947010) can now respond with interactive canvases - dashboards and custom interfaces instead of just text.

[Resend](https://x.com/zenorocha/status/2044055463067824256) shipped a new email editor with BYOA (bring your own agent). There’s a built-in LLM, but you can also MCP into the editor with your own setup.

[Sparkle v4](https://x.com/danshipper/status/2044079255726838273) from Every - let AI organise your filesystem like you would.

[Daniel](https://x.com/dvassallo/status/2044088256753799567) pointed an agent at 5 years of home-building emails (511 events, 690 documents, 170 finance records) and got back a full project timeline in ~$500 of Opus tokens.

[Impeccable v2](https://x.com/pbakaus/status/2044505743144194514) - the design skill for coding agents. v2 adds a CLI scanner (works without an LLM), a Chrome extension, and a /shape command that runs a design interview before writing any code.

[Using Claude Code](https://claude.com/blog/using-claude-code-session-management-and-1m-context) - guide on session management, compaction, and the 1M context window.

30 min tutorial on [building software with agents](https://www.youtube.com/watch?v=kF2WQgk1LtY) in Cursor.

[Lindy AI’s founder](https://x.com/Altimor/status/2044108104816832576) says GLM 5.1 will likely become their default over closed-source models for most use cases, saving them a bunch on inference (their biggest cost, more than payroll).

OpenRouter now offers [video generation models with one universal API](https://x.com/alexatallah/status/2044500778086228278) across all video models.

[Copilot in Word](https://techcommunity.microsoft.com/blog/microsoft365copilotblog/copilot-in-word-new-capabilities-for-document-workflows/4508974) now tracks changes and leaves comments.

[Windsurf 2.0](https://windsurf.com/blog/windsurf-2-0) - Manage all your agents from one place and delegate work to the cloud with Devin.

[Gradient Bang](https://x.com/kwindla/status/2044106314612408437) - a fun multiplayer game with subagents in space. Built with Pipecat, Supabase, and open-source.

Afters

#CHI2026 ","username":"GoogleResearch","name":"Google Research","profile_image_url":"https://pbs.substack.com/profile_images/1929964199956062208/Cv3ZuT1w_normal.jpg","date":"2026-04-15T06:40:18.000Z","photos":[{"img_url":"https://res.cloudinary.com/hhsslviub/video/upload/e_loop,vs_40/z3zualhklx0prnwc3dra.gif","link_url":"https://t.co/SpKfhheBOl"}],"quoted_tweet":{},"reply_count":125,"retweet_count":618,"like_count":4724,"impression_count":770326,"expanded_url":null,"video_url":null,"belowTheFold":true}" data-component-name="Twitter2ToDOM">

@0interestrates of @juliusai.\n\nWe talk about:\n\n How Rahul ended up solo\n The football analogy for building momentum\n Why 8/10 co-founder teams are fighting ","username":"julianweisser","name":"weisser","profile_image_url":"https://pbs.substack.com/profile_images/2028707427659714560/FqyCcqmK_normal.jpg","date":"2026-04-15T18:28:28.000Z","photos":[{"img_url":"https://substackcdn.com/image/upload/w_1028,c_limit,q_auto:best/l_twitter_play_button_rvaygk,w_88/ruck1ztzbpwmxyfmjhne","link_url":"https://t.co/RRuwPXkm3p"}],"quoted_tweet":{},"reply_count":11,"retweet_count":13,"like_count":121,"impression_count":32330,"expanded_url":null,"video_url":"https://video.twimg.com/amplify_video/2044480254887235584/vid/avc1/1280x720/tiKeSYYO8hwy2ZkY.mp4","belowTheFold":true}" data-component-name="Twitter2ToDOM">

Find me on [X](https://x.com/bentossell/), [Linkedin](https://www.linkedin.com/in/ben-tossell-70453537/), or [YouTube](https://www.youtube.com/@bentossell694)

Read [about me](https://bensbites.substack.com/about) and Ben’s Bites

📷 thumbnail by [@keshavatearth](https://www.x.com/keshavatearth)

* sponsors who make this newsletter possible :)

Wanna partner with us for the next quarter? 

Email us at [shanice@bensbites.com](mailto:shanice@bensbites.com) or [k@bensbites.com](mailto:k@bensbites.com)

---

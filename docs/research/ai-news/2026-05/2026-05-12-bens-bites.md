# 🍔 Ben's Bites — 2026-05-12

> Ben Tossell 的 AI 日報，工具圈消息源
> 來源：[Ben's Bites](https://www.bensbites.com/feed)

---

## [Ben's Builds #3 - an email app](https://www.bensbites.com/p/bens-builds-3-an-email-app)
*🍔 Ben's Bites | 2026-05-09*

Hey folks, I had some time to build this week and I mentioned I'd go into a bit more detail on how I did it.

And at the bottom I'll touch on the tools I'm using day to day.

[Subscribe now](https://www.bensbites.com/subscribe)

* * *

#### What did I build this week?

An email app…

I use Gmail. I've used Superhuman for years. I like it a lot. It is fast, keyboard-first, clean, and is good software. But like many saas products, it keeps adding features that I don't need and more importantly, I don't need to be paying for email.

I wanted a split inbox and rules to organize my emails.

Kicking off with Codex:

I've got an idea. I want you to build me an email client so I can have things exactly how I want them. I'll only be using it on my MacBook. It can run locally to start. Gmail should stay the source of truth.

The end product has split inboxes, shortcuts, command palette, reply/compose, 20 second undo send, one-click unsubscribe, search, rules, filter sync, email rendering (mostly 😬) and built in a way that an agent can use it natively.

[](https://substackcdn.com/image/fetch/$s_!DoyP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F3d22e21c-b04c-4998-b915-21dd90f6eb55_1440x458.png)

The code probably has slop in it, I wasn't planning on sharing it but others have asked. So I will. But I'm only building it for myself.

### Version 1

I already have labels I use all the time:

  * investing - for porfolio companies and LPs

  * fyi - receipts, updates, info I never need to read

  * cal - calendar invites

  * news - newsletters

  * pitch - PR emails that I don't need to read




I don't need AI to read every email and categorise it for me - filtering by domain or email address does a great job.

Codex did the first pass but struggled with the UX/UI so I moved to Factory which handled the polish (I could flit between Opus and GPT 5.5), many fixes, testing and getting the product right (enough).

[](https://substackcdn.com/image/fetch/$s_!JdKf!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F330dc4d7-1925-4729-a429-1acc5f4fdc0a_1440x651.png)

### First real issue

It was laggy. I'm using the Google Workspace CLI which can authenticate, fetch emails, and update labels - all the actions I need basically. The whole app is built on top of this.

Investigate why there is a delay with anything in this app. I want everything to feel instant.

It found the app was pinging Gmail too much, too often.

So it then started showing cached data immediately, refreshing in the background, prefetching thread details and updating the UI optimistically when I archive or label something.

This is one of the reasons I like building with agents. I'm learning along the way - **obviously** a database would help here - so we added that.

### Labels and rules

At first labels were just labels. Press L, pick one, done.

If I label something investing, it should move to Investing. If a rule says a label skips the inbox, Gmail should remove it from the inbox.

It's obvious with Gmail filters but my agent was defaulting to a local rule file and not actually syncing with Gmail. Factory sorted it out thankfully.

[](https://substackcdn.com/image/fetch/$s_!mJxc!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb7ea944e-1fcd-4fd1-9ff6-30c587498dc9_1433x600.png)

Then I decided I wanted to make rules richer - when I add a label rule, I should be able to define if it should happen to all domains or just that specific email address.

I originally did that with a notification to choose after labelling but then I decided to make it part of the label modal. Code is cheap - try it, then if it feels wrong, change it.

[](https://substackcdn.com/image/fetch/$s_!jaWj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1e175421-73bd-4913-a4e7-bda711cc789e_1440x1000.png)

### Making it agent-friendly

This app should be usable by agents while I'm talking to them. Add whatever hidden selectors/state/debug endpoints would help agents operate it, but I don't want to visually see any of that.

### Adding reply functionality

Then I wanted to be able to reply, obviously.

Build full reply functionality. Default reply-all, editable to/cc/bcc, attachments. Cmd+Enter sends and archives, but waits 20 seconds before actually sending so Cmd+Z can undo.

This was a bigger jump than I thought… but after a bunch of UX iterations in Factory it feels pretty good.

[](https://substackcdn.com/image/fetch/$s_!exgj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fc5e82630-d0cd-4aef-84dd-0bbe2082d375_2930x1544.png)

### Email rendering

Showing email sounds easy until you try to show email.

Plain text, Gmail HTML, newsletters, receipts, calendar invites, inline images, signatures, quoted replies, tracking pixels, weird MIME stuff. Horrible little world.

The email renderer needs to handle all kinds of email and display them well. Normal human emails should feel native. Designed newsletters/receipts can render differently. Use good open-source libraries.

Codex improved the system but with a bunch of specific rules like if this do that.

So I stepped away and tried to think about other ways to approach it. I know Obsidian has a web clipper that displays nice previews of web pages. So I got Codex to reverse engineer the chrome extension to understand how it works.

So then I asked to apply that approach to email rendering. It's still not prefect and I've given up on perfect for now so normal emails look good (enough) and html heavy emails (like this newsletter, amazon, etc) just get shown as they are.

[](https://substackcdn.com/image/fetch/$s_!whNr!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8a37d1ea-56ed-480f-8672-d1fbc4cbbe7c_2938x1162.png)

What can we do about signatures? They feel irrelevant.

But some emails have stupid signatures that look like designed HTML emails. So I got Factory to fix those and essentially hide that part of the email from the user.

Factory then found one of my favourite bugs. A normal email with a fancy signature rendered like a designed newsletter.

Why? Logo/table signature. The classifier thought the signature meant the whole email was a designed HTML email.

### Search and All Mail

Then I added a search page for all my emails.

And then, All Mail, because sometimes I do need to see what's been archived.

But it was a bit off…

Nah its funky as fuck. Use the browser to test it.

The fix was to lazy-load All Mail and stop hammering Gmail.

[](https://substackcdn.com/image/fetch/$s_!l55G!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffbd573b8-c766-4319-b4f2-f853709163a7_2940x850.png)

### My takeaways

I don't advise building an email client 😅.

If you want a feature (and then another) just build it and see what feels right. Code is cheap.

Switch between tools (harnesses) and models.

Think about other tools or apps that may do all or parts of what you're trying to do. Ask your agent to reverse engineer it.

Use fresh sessions outside of your project to get unbiased opinions on implementations. Your agent is influenced by everything in it's context.

Ask the agent a lot of "I assumed it was doing this, is it?", "Why does this happen?", "Whats the best way to do this?", "What are the tradeoffs of this approach?"

Get agents to use the browser to test things out, a lot.

You learn a lot from building for fun or for the sake of it. So just build stuff!

* * *

### My stack

So many tools. So little time. 

Everyone feels the same - so just find tools you need for the job you need to complete. Don't worry about all the new shiny tools every day.

Day-to-day 'work' i.e. brainstorming, talking about ideas, essentially everything non-coding heavy (like bigger projects or apps) I'm still using [Pi](https://pi.dev/), but now with GPT 5.5 since Anthropic has cracked down…boo! But I'm liking 5.5 - GPT models tend to follow instructions more directly so it really matters what you have in your AGENTS.md and context.

I've also spent the last 2 weeks in the Codex app - it's really good. Use a VPN if in EU/UK so you can use the chrome and computer use tools. But I still find myself preferring the terminal (with Pi) because you can see everything the agent is doing and jump in to course-correct (or tweak your instructions). But IMO this app is better than the Claude variants. Don't bother using Cowork - it's limited and they'll merge it into Claude Code soon enough - don't be put off by 'code' in the name. All these coding agents are just great general agents. 

For 'real' coding i.e. when I'm serious about building something, I use [Factory](https://factory.ai). It's the best harness for code, especially if you don't know _how to actually_ _code_. It's more complete, and seems to handle everything much more than others I've used - plus you can switch between Claude and Opus models very easily. They recently launched a $100 plan too with better limits too. 

For full stack apps I'm sticking with Vercel, Stripe and Supabase. I just started using Stripe's [projects.dev](https://projects.dev/) which will set up all three of those apps (and many others) all in one. Your agent can basically just use projects.dev, set up, manage and link all the other services you need to get apps setup properly. Super helpful as you don't have to manually add or manage each yourself. 

I use [here.now](https://here.now/) **a lot** \- I'm always spinning up new sites for random ideas or tasks like visualising data and things of that nature. Plus sites are easier to read than pure documents. Just give the instructions (copy from the homepage) to your agent and you get free websites spun up on-demand. Super slick and easy. 

For document editing and writing I've been using [Clearly](https://clearly.md) quite a lot recently. I like it - I don't know what I really want out of a document editor like this, truly I just want to view and edit docs within whichever tool I'm using (pi/droid/codex) but none let you do all of that…yet. 

That's mostly it - other than a bunch of CLI tools like [downloading youtube videos](https://github.com/yt-dlp/yt-dlp) or podcasts, getting transcripts, and I use markdown.new for my agents to easily grab website information (It's in my AGENTS.md so my agents use it - i.e. https://markdown.new/www.example.com - but I recently discovered defuddle.md which I may switch to).

* * *

[Chat with me](https://open.substack.com/pub/bensbites/chat?utm_source=chat_embed)

If you know a builder that'd find this useful, feel free to [forward to them](https://www.bensbites.com/publish/post/https://www.bensbites.com/p/bens-builds-3-an-email-app?utm_source=substack&utm_medium=email&utm_content=share&action=share).

Have a great weekend!

* * *

  * Find me on [X](https://x.com/bentossell/), [Linkedin](https://www.linkedin.com/in/ben-tossell-70453537/), or [YouTube](https://www.youtube.com/@bentossell694)

  * Read [about me](https://bensbites.substack.com/about) and Ben's Bites




* * *

Ben's Bites is a reader-supported publication. To receive new posts and support my work, consider becoming a free or paid subscriber.

---

## [Elon doubled limits](https://www.bensbites.com/p/elon-doubled-limits)
*🍔 Ben's Bites | 2026-05-07*

Hey folks,

I'm a professional procrastinator -- I need to ship this course and re-write my fundraising deck for fund II, buuuut yesterday I finally built something I've wanted for a while.

I loved Superhuman, I used it for many years ($40/mo!) but all I really loved was split inboxes based on labels, and how quick and nice it is to use. 

I don't need (…yet? ever?) AI to read all my emails, draft replies, chase me to do things and be a PA for me, I've had PA's and I always let them go.

I just want email rules - if this address is labelled 'pitch' (for PR pitches), archive it. If no label - it's 'important' and needs a reply for me, if 'investing' it's from an LP or portfolio founder, if 'newsletter' archive it (don't do this or you wont see these! 😊). 

Gmail has filters and labels but it's limited and just can't give me the UI I want to work in. So naturally, I built my own. I'll send a 'Ben's Builds' email on Saturday with more details on what I actually did. It took me ~2 hours for the first version.

I was 'pushed' to this by seeing Dan Shipper's [Codex-native email workflow](https://x.com/every/status/2051703753930309979) \- but again, I don't need most of the stuff he's doing. Email is very different for everyone. But now I can completely customise my experience…If I want daily briefs to summarise all my newsletters - my agent can do it, if I want automated actions - my agent can, and so on. 

So if you send me an email, it is me who will reply - but my agent may have you labelled and organised to make it easier for me to respond.

Personal software can be built by anyone!

* * *

_Ben 's Bites is brought to you by [Attio](https://atlas.attio.com/?utm_source=bens_bites&utm_medium=newsletter&utm_campaign=bens_bites-Y26&utm_content=atlas)_

> GTM Atlas is the map for modern go-to-market.
> 
> Written by top operators, Atlas is a free resource covering the full customer journey, with systems thinking that scales with you.
> 
> Curated by Attio. Mapped by operators.
> 
> [Read now](https://atlas.attio.com/?utm_source=bens_bites&utm_medium=newsletter&utm_campaign=bens_bites-Y26&utm_content=atlas)

Fun fact: Attio's founder, Nicolas was interviewed by me in Sept 2020 for my previous company's podcast. [Attio](https://atlas.attio.com/?utm_source=bens_bites&utm_medium=newsletter&utm_campaign=bens_bites-Y26&utm_content=atlas) is very good software!! I should've invested at the time 😩. But for now… I'm going to build something with it 😈

* * *

#### Headlines

  * Free users in ChatGPT are now on "**[GPT-5.5 Instant](https://openai.com/index/gpt-5-5-instant/)** " \- a new model that replaces GPT-5.3 Instant. It's significantly better at vision, understanding PDFs, web search and using your memories and past chats smartly. Its responses are also shorter in general with less emojis. It also hallucinates 52.5% less than the previous model on high-stakes prompts.

> Though recently I've been recommending Codex to friends with free plans of ChatGPT a lot. Yep, Codex is available on free plans. It takes them some time to understand the concept of how reading-writing a file on computer unlocks much more capability but in each case, they have come back after a day or two saying "we're addicted to using codex".
> 
> -- _Keshav_

    * Also, [ChatGPT now works inside Excel and Google Sheets](https://chatgpt.com/apps/spreadsheets/) to build sheets, analyse tabs, write formulas and make approved edits in place. 

  * You can now **[use twice as much of Claude](https://www.anthropic.com/news/higher-limits-spacex)** on all paid plans. How? Anthropic signed a deal to use _all_ of SpaceX's Colossus 1 data centre. (I guess no one needs/uses Grok)

  * Code with Claude was a bit meh! The only new launch they did was introducing some features in [Claude Managed Agents](https://claude.com/blog/new-in-claude-managed-agents) \- 

    * Dreaming - Review past chats and save memories from them.

    * Outcomes - Describe what success looks like, and a grader will judge the agent's work.

    * Multi-agent orchestration - Let a lead agent break the job into pieces and delegate to specialist subagents.

  * **[Posthog is building a code editor](https://posthog.com/code)**. Not literally, but they are making a Codex-like app that uses the data (like product usage patterns, bugs observed, errors in logs etc.) as the primary signal to code/build stuff. Here's how they are thinking about the [self-driving product loop](https://x.com/posthog/status/2052051951286665528).




* * *

[Subscribe now](https://www.bensbites.com/subscribe)

* * *

#### My feed

  * **[Gravitee](https://www.gravitee.io/?utm_source=bensbites&utm_medium=newsletter&utm_campaign=beachhead&utm_content=2)** makes APIs agent-ready, helping teams govern APIs, events, and AI Agents while reducing silos and cost.*

  * [Skills by Entire](https://docs.entire.io/skills/tutorial) to teach agents to explain code, search prior session context, investigate why a change happened and hand work off between agents.

  * [pookie](https://getpookie.com/) \- Slack helper to search messages across your workspace. It also generates memes, and connect to tools like Linear, GitHub and Stripe.

  * The lines between [vibe coding and agentic engineering](https://simonwillison.net/2026/May/6/vibe-coding-and-agentic-engineering/) are starting to blur.

  * [Clicky](https://x.com/FarzaTV/status/2051454940326097220) can now click, save ideas/links/inspo and run Gmail, Calendar and Drive by voice.

  * [deepsec](https://vercel.com/blog/introducing-deepsec-find-and-fix-vulnerabilities-in-your-code-base) \- security harness for finding vulnerabilities in your codebase.

  * [Raindrop Triage](https://www.raindrop.ai/docs/mcp/overview) \- an agent to debug your agents already in production. Also works via MCP.

  * [Prime Intellect Lab](https://www.primeintellect.ai/blog/lab) lets you fine-tune your own models ranging from 1B to 400B params.

  * How we [improved agentic search](https://entire.io/blog/improving-agentic-search-in-coding-agents).

  * Everyone should have an [OPINIONS.md](https://blog.kunchenguid.com/p/everyone-should-have-an-opinionsmd)

  * Gemini API's File Search can now [search over images & audio](https://x.com/OfficialLoganK/status/2051728186824904743) i.e. finding 2-3 relevant images from big folder based on what's in the image (not its name).

  * [@supabase/server](https://supabase.com/blog/introducing-supabase-server) \- public beta package for server-side auth verification, client setup and request context across Edge Functions, Cloudflare Workers, Hono and Bun.

  * Anthropic released [10 finance agent templates](https://www.anthropic.com/news/finance-agents?cam=claude) for pitchbooks, KYC screening, valuation reviews, month-end close and more. They run as Claude Cowork/Claude Code plugins or Managed Agents cookbooks.

  * The "[AI Job Apocalypse](https://x.com/DavidGeorge83/status/2052052899115749692)" is a complete fantasy.

  * The artistry of [text-to-speech models](https://www.youtube.com/watch?v=ZNzYN2jyVTU).

  * Dharmesh says HubSpot's goal is [full API parity with the UI](https://x.com/dharmesh/status/2051678219812675875): agents can run on HubSpot, and agents can run HubSpot. More headless SaaS / AUX energy.

  * [How to use Codex for knowledge work](https://www.youtube.com/watch?v=x9BNBcP_C7Q)




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

## [Codex is gaining steam](https://www.bensbites.com/p/codex-is-gaining-steam)
*🍔 Ben's Bites | 2026-05-05*

Hey folks,

I spent most of the bank holiday weekend offline for a change whilst at a wedding in the English countryside. I would've been more online if Codex had a mobile app but still waiting on that… this morning I did just [install this skill](https://github.com/gragland/codex-imessage-handoff) that lets you iMessage Codex which is pretty great - essentially keeps a thread open in the app that you can message. Just paste the link in Codex and it'll guide you through everything. 

* * *

_Ben 's Bites is brought to you by [Gravitee](https://www.gravitee.io/?utm_source=bensbites&utm_medium=newsletter&utm_campaign=beachhead&utm_content=1)_

> As AI Agents connect to more APIs, security risk gets harder to manage. **[Gravitee](https://www.gravitee.io/?utm_source=bensbites&utm_medium=newsletter&utm_campaign=beachhead&utm_content=1)** helps teams govern APIs, events, and AI Agents while reducing silos and cost. See what enterprise teams are prioritizing in the **[State of AI Agent Security report.](https://www.gravitee.io/state-of-ai-agent-security/?utm_source=bensbites&utm_medium=newsletter&utm_campaign=beachhead&utm_content=1)**

* * *

#### Headlines

  * **OpenAI wants non-technical users to use Codex.** They are making it easy for you to [switch to Codex](https://chatgpt.com/codex/switch-to-codex/). You can now import settings, plugins, agents, project configuration and more into Codex (from tools like Claude Cowork). They are directly improving features [related to everyday work](https://chatgpt.com/codex/for-work/), like creating slides/sheets, plus friendlier UI changes.

  * **[Grok 4.3 is out in the API](https://docs.x.ai/developers/models/grok-4.3)**. 1M context, text + image input, reasoning and a December 2025 knowledge cutoff. It's priced $1.25/$2.50 per million input/output tokens, i.e. much cheaper than Sonnet 4.6 for a relatively similar performance.

  * **Entire** , the company by GitHub's ex-CEO, released two new things: [git-sync](https://github.com/entireio/git-sync) \- a utility to mirror git repos from a source to a target without needing to clone it locally and [Dispatches](https://x.com/EntireHQ/status/2051331019425624209) \- a feature on their web platform to generate release notes from recent ships, commits, and agent sessions by repo/date range.

  * Charity Majors and Christine Yen headline **[Honeycomb's Innovation Week](https://fandf.co/3QVdYGu) (May 12-14)**, a 3-day virtual event addressing observability for the agent era. Learn how the most forward-thinking engineering teams are rising to meet this challenge.**[Register now](https://fandf.co/3QVdYGu)**.*




* * *

[Subscribe now](https://www.bensbites.com/subscribe)

* * *

#### My feed

  * **Lightfield** \- AI-native CRM that learns how you sell. Describe any workflow in English, your CRM runs it on command. [3 mo free w/ ](https://lightfield.app/blog/introducing-skills?utm_source=newsletter&utm_medium=paid&utm_campaign=bens_bites&utm_content=tools_5-5-2026)**[BENSBITEST13](https://lightfield.app/blog/introducing-skills?utm_source=newsletter&utm_medium=paid&utm_campaign=bens_bites&utm_content=tools_5-5-2026)** *

  * [Sauna](https://www.sauna.ai/) \- learns how you work, remembers everything that matters, and actions on it (portfolio company!)

  * [Shared Brain by Zapier](https://zapier.com/shared-brain) \- Collective knowledge vault for your team and a personal assistant to complete tasks. Now in early access.

  * [Manus Cloud Computer](https://manus.im/blog/manus-cloud-computer) \- always-on cloud machine for Manus so bots, scripts, databases and scheduled jobs keep running when your laptop is off. Files and installed tools persist across sessions.

  * [Proxyuser](https://proxyuser.com/) \- test all the core flows of your app via a synthetic user with a real browser, including signups.

  * [Web UI Bench](https://webuibench.dev/) \- Same UI components built by 20 models, shown side-by-side. GPT-5.5 uses too much bland text in the UI when an icon or control is self-explanatory (compared to Opus 4.7).

  * [Flue](https://flueframework.com/) \- TypeScript framework for building Claude Code-style agents.

  * [deepsec](https://vercel.com/blog/introducing-deepsec-find-and-fix-vulnerabilities-in-your-code-base) \- open-source security harness from Vercel for finding vulnerabilities in your codebase with coding agents.

  * [localterm](https://x.com/aidenybai/status/2051331240230613439) \- run a terminal in your browser with _npx localterm@latest start_.

  * [open-slide](https://open-slide.dev/) \- slide framework built for agents. Visual edits, comments, assets and agent-readable slide structure.

  * [Refero Styles](https://styles.refero.design/) \- 2,000+ DESIGN.md files from real products that your agent can use for style references.

  * How OpenAI delivers [low-latency voice AI](https://openai.com/index/delivering-low-latency-voice-ai-at-scale/) at scale.

  * [crabbox](https://github.com/openclaw/crabbox) \- run your dirty worktrees in a remote sandbox easily. ([tweet](https://x.com/steipete/status/2050490163810230579))

  * OpenAI has a new opt-in feature for [Advanced Account Security](https://openai.com/index/advanced-account-security/) in ChatGPT/Codex.

  * [Base44's Frustration Meter](https://x.com/MS_BASE44/status/2049877053248352388) \- usage-based model benchmark. Base44 says Opus 4.7 caused 43% more frustration than Opus 4.6.

  * [Cofounder 2](https://cofounder.co/resources/introducing-cofounder-2) \- another "run a company with agents" product that's a combo of vibe coding, finding leads and sending sales emails.

  * [How Posthog plans to change](https://x.com/james406/status/2049886127507878363?s=20) in the AI era.




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

# 🔧 Simon Willison's Weblog — 2026-05-31

> datasette / llm-cli 作者；AI 工具工程實踐與安全分析密度最高的個人部落格
> 來源：[Simon Willison's Weblog](https://simonwillison.net/atom/everything/)

---

## [How we contain Claude across products](https://simonwillison.net/2026/May/30/how-we-contain-claude/#atom-everything)
*🔧 Simon Willison's Weblog | 2026-05-30*

**[How we contain Claude across products](https://www.anthropic.com/engineering/how-we-contain-claude)**

A complaint I often have about sandboxing products is that they are rarely thoroughly _documented_ , and in the absence of detailed documentation it's hard to know how much I can trust them.

Anthropic just published a fantastic overview of how their various sandbox techniques work across [Claude.ai](https://claude.ai/), Claude Code, and Cowork.

> We constrain where and how an agent can act with process sandboxes, VMs, filesystem boundaries, and egress controls. The goal is to set a hard boundary on what an agent can reach. For example, if credentials never enter the sandbox, they can't be exfiltrated, regardless of whether the cause is a user, a model finding a “creative” path, or an attacker.

Claude.ai uses gVisor. Claude Code, run locally, uses Seatbelt on macOS and Bubblewrap on Linux. Claude Cowork runs a full VM (Apple's Virtualization framework on macOS, HCS on Windows).

There's a lot in here, including some interesting stories of risks they missed such as the `api.anthropic.com/v1/files` exfiltration vector [covered here previously](https://simonwillison.net/2026/Jan/14/claude-cowork-exfiltrates-files/).

This reminded me it's time I took another look at Anthropic's open source [srt (Anthropic Sandbox Runtime)](https://github.com/anthropic-experimental/sandbox-runtime) tool - it's mature enough know that I'm ready to give it a proper go. 

Tags: [sandboxing](https://simonwillison.net/tags/sandboxing), [security](https://simonwillison.net/tags/security), [ai](https://simonwillison.net/tags/ai), [generative-ai](https://simonwillison.net/tags/generative-ai), [llms](https://simonwillison.net/tags/llms), [anthropic](https://simonwillison.net/tags/anthropic), [claude](https://simonwillison.net/tags/claude), [claude-code](https://simonwillison.net/tags/claude-code)

---

## [Running Python ASGI apps in the browser via Pyodide + a service worker](https://simonwillison.net/2026/May/30/pyodide-asgi-browser/#atom-everything)
*🔧 Simon Willison's Weblog | 2026-05-30*

**Research:** [Running Python ASGI apps in the browser via Pyodide + a service worker](https://github.com/simonw/research/tree/main/pyodide-asgi-browser#readme)

[Datasette Lite](https://lite.datasette.io/) is my version of Datasette that runs entirely in the browser using Pyodide in WebAssembly.

When I first built it [four years ago](https://simonwillison.net/2022/May/4/datasette-lite/) I used Web Workers and code that intercepts navigation operations and fetches the generated HTML by running the Python app.

This worked, but had the disadvantage that any JavaScript in `<script>` tags would not be executed - breaking some Datasette functionality and a whole lot of Datasette plugins.

This morning I [set Claude Opus 4.8 the task](https://github.com/simonw/research/pull/112) (in Claude Code for web) of figuring out how to run Python ASGI apps in Pyodide using Service Workers instead, and it seems to work! Here's a [basic ASGI FastCGI demo](https://simonw.github.io/research/pyodide-asgi-browser/) and here's [a demo that runs Datasette 1.0a31](https://simonw.github.io/research/pyodide-asgi-browser/datasette.html).

I'm still getting my head around exactly how it works, but once I've done that I plan to upgrade Datasette Lite itself.

Tags: [javascript](https://simonwillison.net/tags/javascript), [python](https://simonwillison.net/tags/python), [datasette](https://simonwillison.net/tags/datasette), [asgi](https://simonwillison.net/tags/asgi), [service-workers](https://simonwillison.net/tags/service-workers), [pyodide](https://simonwillison.net/tags/pyodide), [datasette-lite](https://simonwillison.net/tags/datasette-lite), [claude-code](https://simonwillison.net/tags/claude-code)

---

## [I Am Retiring from Tech to Live Offline](https://simonwillison.net/2026/May/30/retiring-from-tech-to-live-offline/#atom-everything)
*🔧 Simon Willison's Weblog | 2026-05-30*

**[I Am Retiring from Tech to Live Offline](https://openpath.quest/2026/i-am-retiring-from-tech-to-live-offline/)**

I've seen a lot of posts on forums from people threatening to quit their careers over AI. This is _not_ one of those: Chad Whitacre is taking concrete steps, starting with this typewritten, scanned letter

> I'm retiring from tech. Well, "retiring" is euphemistic. I'm stepping away from tech, and that includes Open Source. [...]
> 
> AI was the last straw. Have you heard of that island off India where the indigenous population kills any outsiders fool-hardy enough to land? They are doing the rest of us a favor by preserving a way of life we may need again someday, or at the very least should not want to see completely extinguished. A reminder. Never forget your roots. Here in Pennsylvania we have the Amish performing a similar function. Significantly less hostile, though still set apart, they bear witness to what was normal for all of us a couple short centuries ago: horse and buggy, wood stoves and lanterns. My intent is to be AI Amish, which means Internet Amish. Not 1780, but 1980. Neo-Amish. I'm fine driving a car and flipping a lightswitch, by which I mean that they don't make me into something I hate, which AI and [struck through: social media] [handwritten above: doomscrolling] do.

I'll admit that at first I wasn't entirely sure if this was serious. Then I found this earlier post by Chad from Feb 19 2026, [Spitting Out the Agentic Kool-Aid](https://openpath.quest/2026/spitting-out-the-agentic-kool-aid/):

> I figured I’d better taste the Kool-Aid in order to form an opinion, so I dove into Claude Code with Opus 4.5 on a side project. I spent three 12+ hour days with it. I was intoxicated. My family was weirded out. [...]
> 
> It weirded me out too, when I unplugged for a long weekend. Something felt off. It was like I had another “person” in my head, sharing my inner monologue—but the “person” was a computer system owned by a budding megacorp.
> 
> [...] I am now also committing myself to disembarking from the titantic of technological accelerationism.
> 
> All efforts to address the problems of invasive technology are worthwhile, even those that are only partially effective. For my part, I have started trying to return more fully to a pre-screen, analog life.

It's accompanied by [a video version of the essay](https://www.youtube.com/watch?v=DCC76jmmzkc) which I found touching and sincere.

Chad has been trying to solve the open source sustainability problem [for _years_](https://simonwillison.net/2024/Jan/23/the-open-source-sustainability-crisis/) \- I talked with him about this at PyCon 2025 in Cleveland. That's a very tough nut to crack, and the disruption caused by AI looks to be making it even harder.

I'm glad that the [Open Source Endowment](https://endowment.dev/) will continue without him. I'm very much going to miss his online voice. 

Via [Hacker News](https://news.ycombinator.com/item?id=48323683)

Tags: [open-source](https://simonwillison.net/tags/open-source), [ai](https://simonwillison.net/tags/ai), [generative-ai](https://simonwillison.net/tags/generative-ai), [llms](https://simonwillison.net/tags/llms), [chad-whitacre](https://simonwillison.net/tags/chad-whitacre), [ai-ethics](https://simonwillison.net/tags/ai-ethics), [deep-blue](https://simonwillison.net/tags/deep-blue)

---

## [Quoting Daniel Jalkut](https://simonwillison.net/2026/May/30/daniel-jalkut/#atom-everything)
*🔧 Simon Willison's Weblog | 2026-05-30*

> My take on AI is, essentially, everybody who’s against it is too against it and everybody who’s for it is too for it.

-- [Daniel Jalkut](https://mastodon.social/@danielpunkass/116639318125898071), via [John Gruber](https://daringfireball.net/linked/2026/05/30/jalkut-on-ai)

Tags: [ai](https://simonwillison.net/tags/ai), [john-gruber](https://simonwillison.net/tags/john-gruber)

---

## [datasette 1.0a31](https://simonwillison.net/2026/May/29/datasette/#atom-everything)
*🔧 Simon Willison's Weblog | 2026-05-29*

**Release:** [datasette 1.0a31](https://github.com/simonw/datasette/releases/tag/1.0a31)

Another significant alpha release, with two new headline features.

> Datasette now offers users with the necessary permissions the ability to both **execute write queries** against their database and to **save stored queries** (renamed from "canned queries") both privately and for use by other members of their Datasette instance.

There's more detail in [SQL write queries and stored queries in Datasette 1.0a31](https://datasette.io/blog/2026/sql-write-queries/) on the Datasette blog, which now has [three posts introducing new features](https://datasette.io/blog/) since the blog launched two weeks ago.

Here's an animated demo from [the blog post](https://datasette.io/blog/2026/sql-write-queries/) showing how the new execute query interface lets people get started with templated insert/update/delete queries from tables they have permission to edit:

Tags: [projects](https://simonwillison.net/tags/projects), [sql](https://simonwillison.net/tags/sql), [sqlite](https://simonwillison.net/tags/sqlite), [datasette](https://simonwillison.net/tags/datasette), [annotated-release-notes](https://simonwillison.net/tags/annotated-release-notes)

---

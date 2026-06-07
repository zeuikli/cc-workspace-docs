# 🔧 Simon Willison's Weblog — 2026-06-01

> datasette / llm-cli 作者；AI 工具工程實踐與安全分析密度最高的個人部落格
> 來源：[Simon Willison's Weblog](https://simonwillison.net/atom/everything/)

---

## [datasette 1.0a32](https://simonwillison.net/2026/May/31/datasette/#atom-everything)
*🔧 Simon Willison's Weblog | 2026-05-31*

**Release:** [datasette 1.0a32](https://github.com/simonw/datasette/releases/tag/1.0a32)

A minor bugfix release. Fixes a bug with `INSERT ... RETURNING` queries via the [new /db/-/execute-write endpoint](https://datasette.io/blog/2026/sql-write-queries/) and a bunch of [base_url](https://docs.datasette.io/en/latest/settings.html#setting-base-url) issues which showed up when I was [experimenting with Service Workers](https://simonwillison.net/2026/May/30/pyodide-asgi-browser/) yesterday.

Tags: [datasette](https://simonwillison.net/tags/datasette), [annotated-release-notes](https://simonwillison.net/tags/annotated-release-notes)

---

## [The solution might be cancelling my AI subscription](https://simonwillison.net/2026/May/31/the-solution-might-be-cancelling-my-ai-subscription/#atom-everything)
*🔧 Simon Willison's Weblog | 2026-05-31*

**[The solution might be cancelling my AI subscription](https://thoughts.hmmz.org/2026-05-31.html)**

I find this post by David Wilson very relatable. David lists 16+ projects he's spun up with AI tooling, and concludes:

> I didn't mean to build most of these things. Usually the Claude session started with something like "_write a quick script for X_ ", and one hour later the result is not a _quick script for X_ , nor in the usual case is my problem solved, whatever the original itch happened to be.
> 
> On that last point, this technology is **horrific** for attention. It's a thermonuclear ADHD amplifier and I have seen the same effect in every single one of my adult friends. Folk running 3 screens simultaneously working on totally unrelated "projects" they have little hope of maintaining, and such little commitment to the outcome that the time is obviously wasted.

This is a _very_ real problem. I'm finding that coding agents can take me from a vague idea to a working solution, one with tests and documentation and that _looks_ like a carefully considered project evolved over the course of many weeks... in less than an hour.

Even if the code is rock solid, there's a limit to how many projects like that I can sensibly care for - and if they're instantly abandoned, what value was there from creating them in the first place?

David doesn't think this is sustainable at all:

> I have no idea how to manage AI at present except by curtailing use, because a tool producing a cheap reward with minimal input and no friction can only be a liability, and achieving that realisation is probably the only real contribution of AI to date.

I'm hopeful that the critical skill to develop here is _discipline_. That’s not great news for me: I’ve been trying to figure that one out for decades!

Interestingly, the [Hacker News thread](https://news.ycombinator.com/item?id=48345896) has gathered a number of comments from people with ADHD who are finding agents help them achieve the focus they've been missing:

  * "... for me (also ADHD) it's kind of the opposite. I'm finishing side projects for the first time ever because I can actually get them working before I get bored of them"
  * "As someone with ADHD I feel like AI is a salve for my mind. I used to listen to intense EDM while working. Now I sit in silence and talk to my agents. I maintain inbox zero. I absorb and comment across all relevant projects, even outside my team. I literally feel like I have a support team for the first time."
  * "For those of us prone to hyperfocus, working with AI can provide the kinds of stimulation we crave. I can hardly remember a time when I've felt more engaged with my work, more productive, and more badass."



Via [Hacker News](https://news.ycombinator.com/item?id=48345896)

Tags: [productivity](https://simonwillison.net/tags/productivity), [ai](https://simonwillison.net/tags/ai), [generative-ai](https://simonwillison.net/tags/generative-ai), [llms](https://simonwillison.net/tags/llms), [coding-agents](https://simonwillison.net/tags/coding-agents), [ai-misuse](https://simonwillison.net/tags/ai-misuse)

---

## [Quoting Karen Kwok for Reuters Breakingviews](https://simonwillison.net/2026/May/31/anthropic-run-rate/#atom-everything)
*🔧 Simon Willison's Weblog | 2026-05-31*

> Anthropic defines “run-rate revenue” in two parts. Use the last 28 days of sales ⁠from customers charged on a consumption basis and multiply it by 13. Then, multiply the monthly subscription take by 12, ​and add the two together.

-- [Karen Kwok for Reuters Breakingviews](https://www.reuters.com/commentary/breakingviews/anthropic-gives-lesson-ai-revenue-hallucination-2026-03-10/), citing "a person familiar with the matter"

Tags: [anthropic](https://simonwillison.net/tags/anthropic), [ai](https://simonwillison.net/tags/ai)

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

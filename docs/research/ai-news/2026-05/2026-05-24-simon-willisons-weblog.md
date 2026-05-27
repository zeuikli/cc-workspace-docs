---
title: "Simon Willison's Weblog — 2026-05-24"
date: 2026-05-24
source: "Simon Willison's Weblog"
type: ai-news
---

# 🔧 Simon Willison's Weblog — 2026-05-24

> datasette / llm-cli 作者；AI 工具工程實踐與安全分析密度最高的個人部落格
> 來源：[Simon Willison's Weblog](https://simonwillison.net/atom/everything/)

---

## [On the](https://simonwillison.net/2026/May/23/on-the-dl/#atom-everything)
*🔧 Simon Willison's Weblog | 2026-05-23*

**[On `the<dl>`](https://benmyers.dev/blog/on-the-dl/)**

I learned a few new-to-me things about the `<dl>` element from this article by Ben Meyer:

  1. A `<dt>` can be followed by _multiple_ `<dd>`
  2. You can optionally group the `<dt>` and `<dd>` elements in a `<div>` for styling - but only a `<div>`.
  3. You can label them using ARIA.
  4. They've been called "description lists", not "definition lists", since [an HTML5 draft in 2008](https://www.w3.org/TR/2008/WD-html5-20080122/#the-dl).



So this is valid:
    
    
    `<h2 id="credits">`Credits`</h2>`
    `<dl aria-labelledby="credits">`
      `<div>`
        `<dt>`Author`</dt>`
        `<dd>`Jeffrey Zeldman`</dd>`
        `<dd>`Ethan Marcotte`</dd>`
      `</div>`
    `</dl>`

Here's a useful note from Adrian Roselli on [screen reader support for description lists](https://adrianroselli.com/2025/01/updated-brief-note-on-description-list-support.html). 

Via [Hacker News](https://news.ycombinator.com/item?id=48247325)

Tags: [css](https://simonwillison.net/tags/css), [html](https://simonwillison.net/tags/html), [screen-readers](https://simonwillison.net/tags/screen-readers), [web-standards](https://simonwillison.net/tags/web-standards)

---

## [The memory shortage is causing a repricing of consumer electronics](https://simonwillison.net/2026/May/22/memory-shortage/#atom-everything)
*🔧 Simon Willison's Weblog | 2026-05-22*

**[The memory shortage is causing a repricing of consumer electronics](https://davidoks.blog/p/ai-is-killing-the-cheap-smartphone)**

David Oks provides the clearest explanation I've seen yet of why consumer products that use memory are likely to get significantly more expensive over the next few years.

The short version is that memory manufacturers - of which there are just three remaining large companies - have a fixed capacity in terms of how many wafers they can process at any one time. This fixed wafer capacity is then split between DDR - used in desktops and servers, LPDDR - used in mobile phones and low-energy devices, and HBM - used with GPUs.

Until recently, HBM got just 2% of that wafer allocation. The enormous growth in AI data centers has pushed that up to an expected 20% by the end of 2026, and "a single gigabyte of HBM consumes more than three times the wafer capacity that a gigabyte of DDR or LPDDR does".

Memory companies have learned from the extinction of their rivals that you should always under-provision rather than over-provision your fabricator capacity. The profit margins and demand for HBM (high-bandwidth memory) will constrain the production of consumer-device RAM for several years.

This is already being felt in the sub-$100 smartphone market, which is particularly important to markets like Africa and South Asia.

(The original title of the piece was "AI is killing the cheap smartphone" but I'm using the Hacker News rephrased title, which I think does more justice to the content.) 

Via [Hacker News](https://news.ycombinator.com/item?id=48229319)

Tags: [memory](https://simonwillison.net/tags/memory), [ai](https://simonwillison.net/tags/ai), [ai-ethics](https://simonwillison.net/tags/ai-ethics)

---

## [FTC to Require Cox Media Group, Two Other Firms to Pay Nearly $1 Million to Settle Charges They Deceived Customers About…](https://simonwillison.net/2026/May/22/ftc-active-listening/#atom-everything)
*🔧 Simon Willison's Weblog | 2026-05-22*

**[FTC to Require Cox Media Group, Two Other Firms to Pay Nearly $1 Million to Settle Charges They Deceived Customers About “Active Listening” AI-Powered Marketing Service](https://www.ftc.gov/news-events/news/press-releases/2026/05/ftc-require-cox-media-group-two-other-firms-pay-nearly-1-million-settle-charges-they-deceived)**

Back in 2024 Cox Media Group were caught trying to sell advertisers packages based on "active listening", with [this deck](https://www.documentcloud.org/documents/25051283-cmg-pitch-deck-on-voice-data-advertising-active-listening/) which claimed:

>   * Smart devices capture real-time intent data by listening to our conversations
>   * Advertisers can pair this voice-data with behavioral data to target in-market consumers
> 


I wrote about this [in September 2024](https://simonwillison.net/2024/Sep/2/facebook-cmg/). My theory:

> I think **active listening** is the term that the team came up with for “something that sounds fancy but really just means the way ad targeting platforms work already”. Then they got over-excited about the new metaphor and added that first couple of slides that talk about “voice data”, without really understanding how the tech works or what kind of a shitstorm that could kick off when people who DID understand technology started paying attention to their marketing.

This FTC press release appears to confirm that's pretty much what happened:

> CMG, MindSift and 1010 Digital Works claimed their “Active Listening” branded marketing service listened in on consumers’ conversations overheard by smart devices, in real time, to target advertising [...]
> 
> According to the complaints, this service did not, in fact, listen in on consumers’ conversations or use voice data at all—nor did the service accurately place ads in customers’ desired locations. Instead, the service the companies provided consisted of reselling—at a significant markup—email lists obtained from other data brokers.

The FTC also clarify that hiding an "opt-in" to using voice data in terms of service would not be acceptable, as tricks like that do not constitute "adequate consent":

> The FTC also alleged that all three companies deceived potential customers by claiming that consumers had opted into the Active Listening service. The company, however, did not seek or obtain consumers’ consent, according to the complaints. Instead, the companies claimed that consumers had “opted in” by agreeing to the terms of service that people have to accept when downloading and using apps. Clicking through mandatory terms of service does not constitute “opt-in consent” for such an invasive service or for use of consumers’ voice data from inside their homes. If the Active Listening service had functioned as advertised, this collection and use of consumers’ voice data without adequate consent would itself violate Section 5 of the FTC Act.

Attempting to myth bust [the conspiracy theory](https://simonwillison.net/tags/microphone-ads-conspiracy/) that our mobile devices target ads to us based on spying through the microphones continues to be my least rewarding niche online hobby. It's nice to have a new piece of ammunition. 

Via [@nydiatisdale](https://twitter.com/nydiatisdale/status/2057657844321705993)

Tags: [privacy](https://simonwillison.net/tags/privacy), [microphone-ads-conspiracy](https://simonwillison.net/tags/microphone-ads-conspiracy)

---

## [Datasette Agent](https://simonwillison.net/2026/May/21/datasette-agent/#atom-everything)
*🔧 Simon Willison's Weblog | 2026-05-21*

We just [announced the first release of Datasette Agent](https://datasette.io/blog/2026/datasette-agent/), a new extensible AI assistant for Datasette. I've been working on my [LLM](https://llm.datasette.io/) Python library for just over three years now, and Datasette Agent represents the moment that LLM and [Datasette](https://datasette.io/) finally come together. I'm really excited about it!

Datasette Agent provides a conversational interface for asking questions of the data you have stored in Datasette. Add the [datasette-agent-charts](https://github.com/datasette/datasette-agent-charts) plugin and it can generate charts of your data as well.

#### The demo

The [announcement post](https://simonwillison.net/atom/everything/) (on the new Datasette project blog) includes this [demo video](https://www.youtube.com/watch?v=AFZKp6hbFjI):

I recorded the video against the new [agent.datasette.io](https://agent.datasette.io/) live demo instance, which runs Datasette Agent against example databases including the classic [global-power-plants](https://datasette.io/global-power-plants) by [WRI](https://www.wri.org/research/global-database-power-plants), and a copy of the [Datasette backup](https://datasette.simonwillison.net/) of my blog.

The live demo runs on [Gemini 3.1 Flash-Lite](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-lite) \- it's cheap, fast and has no trouble writing SQLite queries.

A question I asked in the demo was:

> when did Simon most recently see a pelican?

Which ran [this SQL query](https://datasette.simonwillison.net/simonwillisonblog?sql=SELECT+title%2C+commentary%2C+created+FROM+blog_beat+WHERE+beat_type+%3D+%27sighting%27+AND+%28title+LIKE+%27%25pelican%25%27+OR+commentary+LIKE+%27%25pelican%25%27%29+ORDER+BY+created+DESC+LIMIT+5):
    
    
    SELECT
      title, commentary, created
    FROM
      blog_beat
    WHERE
      beat_type = 'sighting'
      AND (title LIKE '%pelican%' OR commentary LIKE '%pelican%')
    ORDER BY
      created DESC
    LIMIT
      5

And replied:

> The most recent sighting of a pelican by Simon was recorded on **May 20, 2026**.
> 
> The observation included a California Brown Pelican, along with a Common Loon, Canada Goose, Striped Shore Crab, and a California Sea Lion.

Here's [that sighting on my blog](https://simonwillison.net/2026/May/20/sighting-363395265/), and the [Markdown export](https://gist.github.com/simonw/a46d17b69659a4866adb1d868280091d) of the full conversation transcript.

#### The plugins

My favorite feature of Datasette Agent is that, like the rest of Datasette, it's extensible using plugins.

We've shipped three plugins so far:

  * [datasette-agent-charts](https://github.com/datasette/datasette-agent-charts), shown in the video, adds charts to Datasette Agent, powered by [Observable Plot](https://observablehq.com/plot/).
  * [datasette-agent-openai-imagegen](https://github.com/datasette/datasette-agent-openai-imagegen) adds an image generation tool to Datasette Agent using [ChatGPT Images 2.0](https://openai.com/index/introducing-chatgpt-images-2-0/).
  * [datasette-agent-sprites](https://github.com/datasette/datasette-agent-sprites) provides tools for executing code in a [Fly Sprites](https://sprites.dev/) persistent sandbox.



Building plugins is _really fun_. I have a bunch more prototypes that aren't quite alpha-quality yet.

Claude Code and OpenAI Codex are both proving excellent at writing plugins - just point them at a checkout of the [datasette-agent repo](https://github.com/datasette/datasette-agent) for reference and tell them what you want to build!

#### Running it against local models

I've also been having fun running the new plugin against local models. Here's a `uv` one-liner to run the plugin against [gemma-4-26b-a4b](https://huggingface.co/google/gemma-4-26B-A4B) in [LM Studio](https://lmstudio.ai) on a Mac:
    
    
    uvx --prerelease=allow \
      --with datasette-agent --with llm-lmstudio \
      datasette --internal internal.db --root \
      -s plugins.datasette-llm.default_model lmstudio/google/gemma-4-26b-a4b \
      data.db

Datasette Agent needs reliable tool calls and the ability for a model to produce SQL queries that run against SQLite. The open weight models released in the past six months are increasingly able to handle that.

#### What's next

Datasette Agent opens up _so many_ opportunities for the LLM and Datasette ecosystem in general.

It's already informed [the major LLM 0.32a0 refactor](https://simonwillison.net/2026/Apr/29/llm/) which I'm nearly ready to roll into a stable release, maybe with some additional "LLM agent" abstractions extracte from Datasette Agent itself.

I've been exploring my own take on the Claude Artifacts, which is shaping up nicely as a plugin.

I'm excited to use Datasette Agent to build my own [Claw](https://simonwillison.net/2026/May/19/5-minute-llms/#5-minutes-llms.013.jpeg) \- a personal AI assistant built around data imported from different parts of my digital life, which is a neat excuse to revisit my older [Dogsheep](https://dogsheep.github.io) family of tools.

We'll also be rolling out Datasette Agent for users of [Datasette Cloud](https://datasette.cloud/).

Join our [#datasette-agent Discord channel](https://discord.gg/hdxyusUFv) if you'd like to talk about the project.

Tags: [projects](https://simonwillison.net/tags/projects), [sqlite](https://simonwillison.net/tags/sqlite), [ai](https://simonwillison.net/tags/ai), [datasette](https://simonwillison.net/tags/datasette), [generative-ai](https://simonwillison.net/tags/generative-ai), [llms](https://simonwillison.net/tags/llms), [llm](https://simonwillison.net/tags/llm), [uv](https://simonwillison.net/tags/uv), [datasette-agent](https://simonwillison.net/tags/datasette-agent)

---

## [datasette-agent-sprites 0.1a0](https://simonwillison.net/2026/May/21/datasette-agent-sprites/#atom-everything)
*🔧 Simon Willison's Weblog | 2026-05-21*

**Release:** [datasette-agent-sprites 0.1a0](https://github.com/datasette/datasette-agent-sprites/releases/tag/0.1a0)

A Datasette Agent plugin for running commands in a [Fly Sprites](https://sprites.dev) sandbox.

Tags: [sandboxing](https://simonwillison.net/tags/sandboxing), [datasette](https://simonwillison.net/tags/datasette), [fly](https://simonwillison.net/tags/fly), [datasette-agent](https://simonwillison.net/tags/datasette-agent)

---

---
title: "Simon Willison's Weblog — 2026-05-26"
date: 2026-05-26
source: "Simon Willison's Weblog"
type: ai-news
---

# 🔧 Simon Willison's Weblog — 2026-05-26

> datasette / llm-cli 作者；AI 工具工程實踐與安全分析密度最高的個人部落格
> 來源：[Simon Willison's Weblog](https://simonwillison.net/atom/everything/)

---

## [datasette 1.0a30](https://simonwillison.net/2026/May/24/datasette/#atom-everything)
*🔧 Simon Willison's Weblog | 2026-05-24*

**Release:** [datasette 1.0a30](https://github.com/simonw/datasette/releases/tag/1.0a30)

The big new feature in this alpha is a new customizable "Jump to..." menu, described in detail in [The extensible "Jump to" menu in Datasette 1.0a30](https://datasette.io/blog/2026/jump-menu/) on the Datasette blog. You can try it out by hitting `/` on [latest.datasette.io](https://latest.datasette.io/) \- it looks like this:

The new [jump_items_sql()](https://docs.datasette.io/en/latest/plugin_hooks.html#jump-items-sql-datasette-actor-request) plugin hook allows plugins to add their own items to the set that's searched by the plugin.

Tags: [projects](https://simonwillison.net/tags/projects), [datasette](https://simonwillison.net/tags/datasette), [annotated-release-notes](https://simonwillison.net/tags/annotated-release-notes)

---

## [datasette-agent 0.1a4](https://simonwillison.net/2026/May/24/datasette-agent/#atom-everything)
*🔧 Simon Willison's Weblog | 2026-05-24*

**Release:** [datasette-agent 0.1a4](https://github.com/datasette/datasette-agent/releases/tag/0.1a4)

Taking advantage of the new [makeJumpSections()](https://docs.datasette.io/en/latest/javascript_plugins.html#javascript-plugins-makejumpsections) JavaScript plugin hook added in [Datasette 1.0a30](https://docs.datasette.io/en/latest/changelog.html#a30-2026-05-24), `datasette-agent` now presents this "Start a new agent chat" interface as part of the Jump to menu, any time you hit `/`:

You can try this out by signing into [agent.datasette.io](https://agent.datasette.io/) using your GitHub account.

Tags: [datasette](https://simonwillison.net/tags/datasette), [datasette-agent](https://simonwillison.net/tags/datasette-agent)

---

## [datasette-fixtures 0.1a0](https://simonwillison.net/2026/May/24/datasette-fixtures/#atom-everything)
*🔧 Simon Willison's Weblog | 2026-05-24*

**Release:** [datasette-fixtures 0.1a0](https://github.com/datasette/datasette-fixtures/releases/tag/0.1a0)

One of the smaller features in [Datasette 1.0a30](https://docs.datasette.io/en/latest/changelog.html#a30-2026-05-24) is this:

> New documented [datasette.fixtures.populate_fixture_database(conn)](https://docs.datasette.io/en/latest/testing_plugins.html#datasette-fixtures-populate-fixture-database) helper for creating the fixture database tables used by Datasette's own tests, intended for plugin test suites.

This new plugin takes advantage of that API. You can try it out using `uvx` without even installing Datasette like this:
    
    
    uvx --prerelease=allow \
      --with datasette-fixtures datasette \
      --get /fixtures/roadside_attractions.json

Which outputs:
    
    
    {
      "ok": true,
      "next": null,
      "rows": [
        {"pk": 1, "name": "The Mystery Spot", "address": "465 Mystery Spot Road, Santa Cruz, CA 95065", "url": "https://www.mysteryspot.com/", "latitude": 37.0167, "longitude": -122.0024},
        {"pk": 2, "name": "Winchester Mystery House", "address": "525 South Winchester Boulevard, San Jose, CA 95128", "url": "https://winchestermysteryhouse.com/", "latitude": 37.3184, "longitude": -121.9511},
        {"pk": 3, "name": "Burlingame Museum of PEZ Memorabilia", "address": "214 California Drive, Burlingame, CA 94010", "url": null, "latitude": 37.5793, "longitude": -122.3442},
        {"pk": 4, "name": "Bigfoot Discovery Museum", "address": "5497 Highway 9, Felton, CA 95018", "url": "https://www.bigfootdiscoveryproject.com/", "latitude": 37.0414, "longitude": -122.0725}
      ],
      "truncated": false
    }

Tags: [datasette](https://simonwillison.net/tags/datasette), [uv](https://simonwillison.net/tags/uv)

---

## [Quoting Armin Ronacher](https://simonwillison.net/2026/May/24/armin-ronacher/#atom-everything)
*🔧 Simon Willison's Weblog | 2026-05-24*

> The most frustrating failure mode right now is that people submit issues that are not in their own voice. They contain an observed problem somewhere, but it has been thrown into a clanker and the clanker reworded it and made a huge mess of it. Typically, it was prompted so badly that the conclusions produced are more often than not inaccurate but always full of confidence. The result is complete guesswork on root causes, fake-minimal repros, suggested implementation strategies, analogies to adjacent but often the wrong code, and long lists of error classes that might or might not matter. [...]
> 
> So at least personally, I increasingly want issue reports to be condensed to what the human actually observed:
> 
>   1. I ran this command.
>   2. I expected this to happen.
>   3. This happened instead.
>   4. Here is the exact error or log.
> 


-- [Armin Ronacher](https://lucumr.pocoo.org/2026/5/24/pi-oss/), on slop issues filed against [Pi](https://pi.dev/)

Tags: [ai](https://simonwillison.net/tags/ai), [github-issues](https://simonwillison.net/tags/github-issues), [llms](https://simonwillison.net/tags/llms), [ai-ethics](https://simonwillison.net/tags/ai-ethics), [open-source](https://simonwillison.net/tags/open-source), [coding-agents](https://simonwillison.net/tags/coding-agents), [generative-ai](https://simonwillison.net/tags/generative-ai), [armin-ronacher](https://simonwillison.net/tags/armin-ronacher), [pi](https://simonwillison.net/tags/pi), [slop](https://simonwillison.net/tags/slop)

---

## [Mad House — Usborne Creepy Computer Games](https://simonwillison.net/2026/May/24/usborne-mad-house/#atom-everything)
*🔧 Simon Willison's Weblog | 2026-05-24*

**Tool:** [Mad House — Usborne Creepy Computer Games](https://tools.simonwillison.net/usborne-mad-house)

Via [Hacker News](https://news.ycombinator.com/item?id=48258194) I learned that UK publisher Usborne published [free PDFs of their 1980s Computer Books](https://usborne.com/us/books/computer-and-coding-books), some of which I remember working through on my Commodore 64 as a child.

These were so great! Beautifully illustrated books with fun projects made up of code you could type into your own machine.

I remember playing "Mad House" typed in from the 1983 book "Creepy Computer Games", so I fed that PDF [into Claude](https://claude.ai/share/7b4a5617-f586-4744-b082-1650cab607cb) and had it build an interactive version of that game in JavaScript and HTML:

> `Build a vanilla JS artifact that exactly recreates the game Mad House from this book, make sure it's mobile friendly and has a suitable retro aesthetic`
> 
> `Credit the book title and link to https://usborne.com/us/books/computer-and-coding-books`

Tags: [computer-history](https://simonwillison.net/tags/computer-history), [games](https://simonwillison.net/tags/games), [tools](https://simonwillison.net/tags/tools)

---

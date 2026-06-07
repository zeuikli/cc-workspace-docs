# 🔧 Simon Willison's Weblog — 2026-05-30

> datasette / llm-cli 作者；AI 工具工程實踐與安全分析密度最高的個人部落格
> 來源：[Simon Willison's Weblog](https://simonwillison.net/atom/everything/)

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

## [Anthropic's run-rate revenue hits $47 billion](https://simonwillison.net/2026/May/29/anthropic/#atom-everything)
*🔧 Simon Willison's Weblog | 2026-05-29*

The most interesting thing about [Anthropic's $65B Series H announcement](https://www.anthropic.com/news/series-h) is this line (emphasis mine):

> Since our Series G in February, adoption has continued to grow across global enterprise customers, and our run-rate revenue crossed **$47 billion** earlier this month.

Anthropic have made a bit of a habit of sharing their "run-rate revenue" in this kind of announcement, which is an annualized projection of their current revenue - typically calculated by taking the most recent month and multiplying by 12.

Earlier this year:

  * Apr 6, 2026 in [Anthropic expands partnership with Google and Broadcom](https://www.anthropic.com/news/google-broadcom-partnership-compute): "Our run-rate revenue has now surpassed **$30 billion** —up from approximately **$9 billion** at the end of 2025."
  * Feb 12, 2026 in [Anthropic raises $30 billion in Series G](https://www.anthropic.com/news/anthropic-raises-30-billion-series-g-funding-380-billion-post-money-valuation): "Today, our run-rate revenue is **$14 billion** , with this figure growing over 10x annually in each of those past three years."



I had [Claude Opus 4.8 make me](https://claude.ai/share/f52e82bd-7e09-49a5-b658-0b9999ce5a45) this chart using [Matplotlib](https://matplotlib.org/) (Claude: "a data line chart is more straightforward matplotlib work—not really a design piece"):

Back in April [Axios CEO Jim VandeHei wrote](https://www.axios.com/2026/04/13/anthropic-revenue-growth-ai) that he could not find "any company — in any industry, in any era — that has scaled organic revenue this quickly at this level as Anthropic" - and that was when they were at a paltry $30 billion.

(Also [in Axios today](https://www.axios.com/2026/05/28/ai-spending-roi-enterprise-costs) is an anonymously sourced note that "An AI consultant tells Axios one of their clients recently spent half a billion dollars in a single month after failing to put usage limits on Claude licenses for employees" - times that by 12 and you get an extra $6 billion in annualized run-rate!)

Ed Zitron was [extremely skeptical of that $30 billion number](https://www.wheresyoured.at/anthropics-profitability-swindle/) \- I wonder if his skepticism will update for the new $47 billion figure.

I've seen a few people dismiss this as untrustworthy, because the numbers come from Anthropic. That doesn't hold up: these numbers were included in announcements of their fundraises, and lying to investors who just put in $65 billion would be securities fraud. They're even less likely to lie given that the real numbers will no doubt come out in their S-1 when they file for their IPO.

Tags: [anthropic](https://simonwillison.net/tags/anthropic), [ai](https://simonwillison.net/tags/ai)

---

## [Claude Opus 4.8: "a modest but tangible improvement"](https://simonwillison.net/2026/May/28/claude-opus-4-8/#atom-everything)
*🔧 Simon Willison's Weblog | 2026-05-28*

Anthropic shipped [Claude Opus 4.8](https://www.anthropic.com/news/claude-opus-4-8) today. My favourite thing about it is this note in the release announcement:

> Users will find Opus 4.8 to be a modest but tangible improvement on its predecessor. There’s still more to be done: we’re working on developing and releasing models that provide many of the same capabilities as Opus at a lower cost.

It's so refreshing to see an AI lab honestly describe a release as a minor incremental improvement over the previous model!

Honesty seems to be a theme. Here's my other favorite note from that announcement:

> One of the most prominent improvements in Opus 4.8 is its _honesty_. We train all our models to be honest---for instance, to avoid making claims that they can't support. But a general problem with AI models is that they sometimes jump to conclusions, confidently claiming to have made progress in their work despite the evidence being thin. Early testers report that Opus 4.8 is more likely to flag uncertainties about its work and less likely to make unsupported claims. This is borne out in [our evaluations](https://www.anthropic.com/claude-opus-4-8-system-card), which show that Opus 4.8 is around four times less likely than its predecessor to allow flaws in code it has written to pass unremarked.

That linked system card includes the following:

> Claude Opus 4.8 had the lowest incorrect-rate of the six models on every benchmark—the most direct measure of factual hallucination. It achieved this mainly by abstaining on questions about which it was uncertain rather than by answering more questions correctly.

#### Model characteristics

Not much has changed since 4.7.

It's priced the same as Opus 4.5/4.6/4.7 - $5/million input and $25 per million output. "Fast mode" is twice that price, which is a significant reduction from their previous models - fast mode on 4.6/4.7 remains at $30/$150. Note that [fast mode](https://platform.claude.com/docs/en/build-with-claude/fast-mode) is only available to organizations that are part of the research preview, "Contact your account manager to request access".

Both the reliable knowledge cutoff and the training data cutoff are January 2026, the same as for 4.7.

The context window is still 1,000,000 tokens, and the max output is 128,000 tokens.

The [What's new in Claude Opus 4.8](https://platform.claude.com/docs/en/about-claude/models/whats-new-claude-4-8) document has some of the more interesting details. These caught my eye:

> **Mid-conversation system messages**. Claude Opus 4.8 accepts `role: "system"` messages immediately after a user turn in the `messages` array (subject to [placement rules](https://platform.claude.com/docs/en/build-with-claude/mid-conversation-system-messages#limitations)). This lets you append updated instructions later in a long-running conversation without restating the full system prompt, which preserves [prompt cache](https://platform.claude.com/docs/en/build-with-claude/prompt-caching) hits on the earlier turns and reduces input cost on agentic loops.

See also [this update](https://github.com/anthropics/anthropic-sdk-python/commit/2b826760101664ef89db42132932f53ba97c894d#diff-a947c9c02eab58e8ddbe799a11832d533836d242e07c7251997f8543f0981f2f) to the Anthropic Python SDK. Being able to steer the system prompt mid-conversation sounds really powerful. I was worried this would be incompatible with the abstraction provided by my own [LLM library](https://llm.datasette.io/en/stable/python-api.html#system-prompts), which expects a single system prompt per conversation... but it turns out my recent [redesign](https://simonwillison.net/2026/Apr/29/llm/) should handle that [just fine](https://github.com/simonw/llm-anthropic/issues/73).

> **Lower prompt cache minimum**. The minimum cacheable prompt length on Claude Opus 4.8 is 1,024 tokens, lower than on Claude Opus 4.7.

I checked and 4.7's minimum [was 4,096](https://platform.claude.com/docs/en/build-with-claude/prompt-caching#cache-limitations).

#### And some pelicans

Here are [pelicans riding bicycles](https://tools.simonwillison.net/markdown-svg-renderer#url=https%3A%2F%2Fgist.github.com%2Fsimonw%2Ffea4f7546626d627862dc241a4e3a86a) for all five thinking levels, `low`, `medium`, `high`, `xhigh`, and `max`:

[low](https://gist.github.com/simonw/fea4f7546626d627862dc241a4e3a86a#response) [medium](https://gist.github.com/simonw/fea4f7546626d627862dc241a4e3a86a#response-1) [high](https://gist.github.com/simonw/fea4f7546626d627862dc241a4e3a86a#response-2) [xhigh](https://gist.github.com/simonw/fea4f7546626d627862dc241a4e3a86a#response-3) [max](https://gist.github.com/simonw/fea4f7546626d627862dc241a4e3a86a#response-4)

This time I ran them using the [LLM CLI](https://llm.datasette.io/en/stable/usage.html), exported the logs to Markdown and then had Claude Opus 4.8 [build me](https://github.com/simonw/tools/commit/71e4944766b577a327ff048cc63b739ba4cbade9) an HTML tool that could render that Markdown with the `svg` fenced code blocks displayed as SVGs on the page.

(I later had GPT-5.5 xhigh in Codex [update that code](https://gist.github.com/simonw/bb5a267f8144dfe4e92e50a014e49e98) to remove any XSS holes. I'm sure Claude could have done that if I'd asked, but GPT-5.5 is my code security blanket at the moment.)

The max one was clearly the best, but it did take 25 input, 17,167 output tokens for a total cost of [43 cents](https://www.llm-prices.com/#it=25&ot=17167&ic=5&oc=25&sel=claude-opus-4-5)!

Tags: [ai](https://simonwillison.net/tags/ai), [generative-ai](https://simonwillison.net/tags/generative-ai), [llms](https://simonwillison.net/tags/llms), [anthropic](https://simonwillison.net/tags/anthropic), [claude](https://simonwillison.net/tags/claude), [pelican-riding-a-bicycle](https://simonwillison.net/tags/pelican-riding-a-bicycle), [llm-release](https://simonwillison.net/tags/llm-release)

---

## [llm-anthropic 0.25.1](https://simonwillison.net/2026/May/28/llm-anthropic/#atom-everything)
*🔧 Simon Willison's Weblog | 2026-05-28*

**Release:** [llm-anthropic 0.25.1](https://github.com/simonw/llm-anthropic/releases/tag/0.25.1)

>   * New model: [Claude Opus 4.8](https://www.anthropic.com/news/claude-opus-4-8) (`claude-opus-4.8`).
>   * New `-o fast 1` option for [fast mode](https://platform.claude.com/docs/en/build-with-claude/fast-mode), for organizations with that feature enabled on their account.
>   * Default max_tokens for each model now defaults to that model's maximum output rather than 8,192. [#72](https://github.com/simonw/llm-anthropic/issues/72)
> 


See also my [notes on Opus 4.8](https://simonwillison.net/2026/May/28/claude-opus-4-8/) \- I used this new release of `llm-anthropic` to generate the pelicans.

---

## [markdown-svg-renderer](https://simonwillison.net/2026/May/28/markdown-svg-renderer/#atom-everything)
*🔧 Simon Willison's Weblog | 2026-05-28*

**Tool:** [markdown-svg-renderer](https://tools.simonwillison.net/markdown-svg-renderer)

A slightly customized Markdown rendering tool with special treatment for fenced code SVG blocks - it both renders the image and provides a tab for switching to the code view.

You can paste in Markdown or give it a URL to a CORS-enabled Markdown file or Gist. [Here's an example](https://tools.simonwillison.net/markdown-svg-renderer#url=https%3A%2F%2Fgist.github.com%2Fsimonw%2Ffea4f7546626d627862dc241a4e3a86a) where it loads a Markdown file full of LLM pelican logs for [Opus 4.8](https://simonwillison.net/2026/May/28/claude-opus-4-8/#and-some-pelicans).

Tags: [svg](https://simonwillison.net/tags/svg), [tools](https://simonwillison.net/tags/tools), [markdown](https://simonwillison.net/tags/markdown), [cors](https://simonwillison.net/tags/cors)

---

# 🔧 Simon Willison's Weblog — 2026-06-06

> datasette / llm-cli 作者；AI 工具工程實踐與安全分析密度最高的個人部落格
> 來源：[Simon Willison's Weblog](https://simonwillison.net/atom/everything/)

---

## [Quoting Andreas Kling](https://simonwillison.net/2026/Jun/5/andreas-kling/#atom-everything)
*🔧 Simon Willison's Weblog | 2026-06-05*

> We will no longer accept public pull requests. [...]
> 
> A substantial patch used to imply substantial effort, and that effort was a reasonable proxy for good faith. That assumption no longer holds. [...]
> 
> Whether code was typed by hand is beside the point. What matters is who is responsible for it once it enters the browser. Ladybird is becoming a browser for real users. The people introducing changes to it must be the people who decide those changes belong in the project, and who will answer for the consequences.

-- [Andreas Kling](https://ladybird.org/posts/changing-how-we-develop-ladybird/), Changing How We Develop Ladybird

Tags: [ladybird](https://simonwillison.net/tags/ladybird), [ai-ethics](https://simonwillison.net/tags/ai-ethics), [open-source](https://simonwillison.net/tags/open-source), [generative-ai](https://simonwillison.net/tags/generative-ai), [ai](https://simonwillison.net/tags/ai), [andreas-kling](https://simonwillison.net/tags/andreas-kling), [llms](https://simonwillison.net/tags/llms)

---

## [AI enthusiasts are in a race against time, AI skeptics are in a race against entropy](https://simonwillison.net/2026/Jun/4/ai-enthusiasts-ai-skeptics/#atom-everything)
*🔧 Simon Willison's Weblog | 2026-06-04*

**[AI enthusiasts are in a race against time, AI skeptics are in a race against entropy](https://charitydotwtf.substack.com/p/ai-enthusiasts-are-in-a-race-against)**

Charity Majors neatly captures the dynamic between AI enthusiasts and AI skeptics, both of whom are trying to build great software, often in the same teams:

> The enthusiasts are _not wrong_. We are starting to see real, non-imaginary, discontinuous leaps in capabilities from teams that lean in hard to working with AI. And this does not feel like a normal technology cycle where you can wait for the dust to settle; teams that sit this out while competitors are hustling could be out of business before the dust settles. That’s a real, existential threat.
> 
> The skeptics are also _not wrong_. When you ship code faster than engineers can read it, in domains where nobody has full context, you are making withdrawals from a trust account that took years to build. Reliability degrades, institutional knowledge evaporates. You end up with systems nobody understands, products burbling into incoherence, and on-call rotations that grind people up and spit them out. That is ALSO a real existential threat.

Charity recommends treating this as both a leadership challenge and an engineering challenge. The key issue:

> There is no natural feedback loop connecting enthusiasts with skeptics.

Designing feedback loops to help "mend the gap in shared reality" between the two groups is a fascinating organizational design problem. 

Via [Lobste.rs](https://lobste.rs/s/ri4flr/ai_enthusiasts_are_race_against_time_ai)

Tags: [ai](https://simonwillison.net/tags/ai), [charity-majors](https://simonwillison.net/tags/charity-majors), [agentic-engineering](https://simonwillison.net/tags/agentic-engineering)

---

## [Quoting Emanuel Maiberg, 404 Media](https://simonwillison.net/2026/Jun/4/a-slightly-different-version/#atom-everything)
*🔧 Simon Willison's Weblog | 2026-06-04*

> After this story was published Google's spokesperson reached out and asked us to publish a slightly different version of that statement. The new statement no longer stated that "it's critical that we maintain humans in the loop."

-- [Emanuel Maiberg, 404 Media](https://www.404media.co/google-employees-internally-share-memes-about-how-its-ai-sucks/), Google Employees Internally Share Memes About How Its AI Sucks

Tags: [ai-ethics](https://simonwillison.net/tags/ai-ethics), [journalism](https://simonwillison.net/tags/journalism), [ai](https://simonwillison.net/tags/ai), [google](https://simonwillison.net/tags/google)

---

## [Uber Caps Usage of AI Tools Like Claude Code to Manage Costs](https://simonwillison.net/2026/Jun/3/uber-caps-usage/#atom-everything)
*🔧 Simon Willison's Weblog | 2026-06-03*

**[Uber Caps Usage of AI Tools Like Claude Code to Manage Costs](https://www.bloomberg.com/news/articles/2026-06-02/uber-caps-usage-of-ai-tools-like-claude-code-to-cut-costs)**

I wrote [the other day](https://simonwillison.net/2026/May/27/product-market-fit/#the-ai-failure-stories-around-this-are-pretty-thin) about Uber blowing its 2026 AI budget in four months, and how that wasn't particularly surprising given they would have set that budget in 2025, before anyone could have predicted how popular token-burning coding agents were about to become. Natalie Lung for Bloomberg:

> The rideshare giant is limiting all employees to $1,500 in monthly token spending per AI coding tool, an Uber spokesperson said in response to a Bloomberg News inquiry. That means spending on one tool doesn’t have a bearing on the budget for another. The limits, which have been instituted in recent months, only apply to agentic coding software such as Cursor or Anthropic PBC’s Claude Code.

A $1,500 monthly limit per tool strikes me as a rational policy response to over-spending, and _much_ more sensible than those [tokenmaxxing](https://en.wikipedia.org/wiki/Token_maxxing) leaderboards encouraging employees to compete for as much AI usage as possible.

It's also interesting in that it hints at a real dollar value for what Uber is getting out of these tools. If we assume two actively used tools per engineer that's $3,000 * 12 = $36,000 cap per engineer per year. Levels.fyi lists [the median yearly compensation package for Uber software engineers in the USA](https://www.levels.fyi/companies/uber/salaries/software-engineer?country=254) at $330,000.

That means each employee's AI spending cap is ~11% of that median compensation package.

I [noted](https://simonwillison.net/2026/May/27/product-market-fit/#enterprise-customers-are-now-paying-api-prices) that my own token usage comes to about $1,000/month against each of Anthropic and OpenAI - which currently costs me just $100 per provider thanks to their generous subsidized plans for individual subscribers. Those plans are no longer available to larger companies like Uber.

Their new policy means if I were working at Uber I'd still have ~$500/month of tokens to spare for each of those tools, given my current usage patterns. 

Tags: [ai](https://simonwillison.net/tags/ai), [generative-ai](https://simonwillison.net/tags/generative-ai), [llms](https://simonwillison.net/tags/llms), [llm-pricing](https://simonwillison.net/tags/llm-pricing), [coding-agents](https://simonwillison.net/tags/coding-agents), [uber](https://simonwillison.net/tags/uber)

---

## [Microsoft's new MAI models](https://simonwillison.net/2026/Jun/2/microsofts-new-models/#atom-everything)
*🔧 Simon Willison's Weblog | 2026-06-02*

Microsoft [announced two new text LLMs](https://microsoft.ai/news/building-a-hillclimbing-machine-launching-seven-new-mai-models/) this morning - **[MAI-Thinking-1](https://microsoft.ai/news/introducing-mai-thinking-1/)** (reasoning, 1T parameters, 35B active, available to "select early partners") and **[MAI-Code-1-Flash](https://microsoft.ai/news/introducingmai-code-1-flash/)** (137B Parameters, 5B active, "purpose-built for GitHub Copilot and VS Code to deliver high performance and lower cost [...] rolling out to GitHub Copilot individual users in Visual Studio Code"). I've not been able to try either of them just yet.

~~It's very interesting to see Microsoft releasing models with such low parameter counts, especially given how expensive larger models are to access right now. They claim MAI-Thinking-1 "is preferred to Sonnet 4.6 in our blind human side-by-side evaluations", which is impressive for a 35B model seeing as I frequently run models larger than that on my own laptop.~~ (UPDATE: I got this entirely wrong, see note below.)

Also [of note](https://microsoft.ai/news/introducing-mai-thinking-1/):

> We trained [MAI-Thinking-1] from the ground up on enterprise grade, clean and commercially licensed data, without distillation from third-party models.

And for [MAI-Code-1-Flash](https://microsoft.ai/news/introducingmai-code-1-flash/) as well:

> It is built end-to-end by Microsoft using clean and appropriately licensed data.

I would _very much_ like to learn more about this "appropriately licensed" data! Could these be the first generally useful code-specialist models that didn't train on an unlicensed dump of the web? (**Update** : the answer is no, see note below.)

**Update** : My initial published notes got the size of the models wrong. I misread Microsoft's announcements and interpreted the MoE active parameter count as the total parameter count, but the [model card for MAI-Code-1-Flash](https://microsoft.ai/pdf/MAI-Code-1-Flash-Model-Card.PDF) lists it as 137B with 5B active and the [MAI-Thinking-1 technical paper](https://microsoft.ai/wp-content/uploads/2026/06/main_20260602_2.pdf) reveals it to be a 1T model with 35B active.

I deeply regret this error.

**Update 2** : That technical paper describes the training data in some detail from page 80 onwards. It has the same licensing problems as all of the other major LLMs: it's trained on a crawl of the public web:

> The majority of our web HTML corpus comes from a proprietary crawl. After initial page discovery and selection, approximately 1.2 trillion pages are crawled and parsed. [...] In addition to Microsoft standard policy Sec. 2.4, we apply UT1 block list (Prigent, 2026) to remove adult content and piracy-related domains. In all, this filtering reduces the corpus from 1.2 trillion pages to 794 billion pages. Given the prevalence of AI-generated content on the web, we also score pages with a proprietary AI-content detection model and use manual inspection to identify domains with extensive AI-generated content; those domains are filtered out of the training corpus.
> 
> [...]
> 
> We process Common Crawl with the same pipeline. [...] After filtering, deduplication, merging with the proprietary web corpus, and a final round of exact-URL and content-level fuzzy deduplication, the Common Crawl portion contains 24.2 billion pages.

I did not cover this one at all well, which is somewhat ironic since I was at the Microsoft Build conference when I wrote this up! I'm sorry for not digging deeper before publishing my initial notes.

Tags: [llm-release](https://simonwillison.net/tags/llm-release), [generative-ai](https://simonwillison.net/tags/generative-ai), [ai](https://simonwillison.net/tags/ai), [microsoft](https://simonwillison.net/tags/microsoft), [llms](https://simonwillison.net/tags/llms), [training-data](https://simonwillison.net/tags/training-data)

---

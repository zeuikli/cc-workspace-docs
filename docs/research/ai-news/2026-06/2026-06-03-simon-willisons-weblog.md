# 🔧 Simon Willison's Weblog — 2026-06-03

> datasette / llm-cli 作者；AI 工具工程實踐與安全分析密度最高的個人部落格
> 來源：[Simon Willison's Weblog](https://simonwillison.net/atom/everything/)

---

## [Microsoft's new MAI models](https://simonwillison.net/2026/Jun/2/microsofts-new-models/#atom-everything)
*🔧 Simon Willison's Weblog | 2026-06-02*

Microsoft [announced two new text LLMs](https://microsoft.ai/news/building-a-hillclimbing-machine-launching-seven-new-mai-models/) this morning - **[MAI-Thinking-1](https://microsoft.ai/news/introducing-mai-thinking-1/)** (reasoning, 35B parameters, available to "select early partners") and **[MAI-Code-1-Flash](https://microsoft.ai/news/introducingmai-code-1-flash/)** (5B parameters, "purpose-built for GitHub Copilot and VS Code to deliver high performance and lower cost [...] rolling out to GitHub Copilot individual users in Visual Studio Code"). I've not been able to try either of them just yet.

It's very interesting to see Microsoft releasing models with such low parameter counts, especially given how expensive larger models are to access right now. They claim MAI-Thinking-1 "is preferred to Sonnet 4.6 in our blind human side-by-side evaluations", which is impressive for a 35B model seeing as I frequently run models larger than that on my own laptop.

Also [of note](https://microsoft.ai/news/introducing-mai-thinking-1/):

> We trained [MAI-Thinking-1] from the ground up on enterprise grade, clean and commercially licensed data, without distillation from third-party models.

And for [MAI-Code-1-Flash](https://microsoft.ai/news/introducingmai-code-1-flash/) as well:

> It is built end-to-end by Microsoft using clean and appropriately licensed data.

I would _very much_ like to learn more about this "appropriately licensed" data! Could these be the first generally useful code-specialist models that didn't train on an unlicensed dump of the web?

Tags: [llm-release](https://simonwillison.net/tags/llm-release), [generative-ai](https://simonwillison.net/tags/generative-ai), [ai](https://simonwillison.net/tags/ai), [microsoft](https://simonwillison.net/tags/microsoft), [llms](https://simonwillison.net/tags/llms)

---

## [datasette-agent-micropython 0.1a0](https://simonwillison.net/2026/Jun/2/datasette-agent-micropython/#atom-everything)
*🔧 Simon Willison's Weblog | 2026-06-02*

**Release:** [datasette-agent-micropython 0.1a0](https://github.com/datasette/datasette-agent-micropython/releases/tag/0.1a0)

I want [Datasette Agent](https://agent.datasette.io) to be able to generate and execute Python code safely. This alpha is looking very promising so far. GPT-5.5 has so far failed to break out of the sandbox!

Tags: [python](https://simonwillison.net/tags/python), [sandboxing](https://simonwillison.net/tags/sandboxing), [datasette](https://simonwillison.net/tags/datasette), [webassembly](https://simonwillison.net/tags/webassembly), [datasette-agent](https://simonwillison.net/tags/datasette-agent)

---

## [micropython-wasm 0.1a1](https://simonwillison.net/2026/Jun/2/micropython-wasm/#atom-everything)
*🔧 Simon Willison's Weblog | 2026-06-02*

**Release:** [micropython-wasm 0.1a1](https://github.com/simonw/micropython-wasm/releases/tag/0.1a1)

Fixes for some limitations that emerged while I was trying to use this to build `datasette-agent-micropython`.

Tags: [python](https://simonwillison.net/tags/python), [sandboxing](https://simonwillison.net/tags/sandboxing), [webassembly](https://simonwillison.net/tags/webassembly)

---

## [California Brown Pelican](https://simonwillison.net/2026/Jun/2/sighting-367841339/#atom-everything)
*🔧 Simon Willison's Weblog | 2026-06-02*

California Brown Pelican, in Fort Mason, CA, US

I'm at the [Microsoft Build](https://build.microsoft.com/) conference today, held at [Fort Mason](https://en.wikipedia.org/wiki/Fort_Mason) in San Francisco. There are California Brown Pelicans diving into the water directly behind venue!

Tags: [microsoft](https://simonwillison.net/tags/microsoft), [ai](https://simonwillison.net/tags/ai), [generative-ai](https://simonwillison.net/tags/generative-ai), [llms](https://simonwillison.net/tags/llms), [llm-release](https://simonwillison.net/tags/llm-release)

---

## [Pasted File Editor](https://simonwillison.net/2026/Jun/2/pasted-file-editor/#atom-everything)
*🔧 Simon Willison's Weblog | 2026-06-02*

**Tool:** [Pasted File Editor](https://tools.simonwillison.net/pasted-file-editor)

I really like how you can paste a large volume of text into [claude.ai](https://claude.ail) (or the Claude desktop/mobile apps) and it will detect it as a large paste and turn it into a file attachment instead.

I decided to have Codex desktop [build me a version of that](https://gist.github.com/simonw/74c79119b487a5acce18b4dcc26b9f79) as a prototype.

You can also open files directly - including images which will be shown as thumbnails - or drag files onto the textarea.

Tags: [javascript](https://simonwillison.net/tags/javascript), [tools](https://simonwillison.net/tags/tools), [ai-assisted-programming](https://simonwillison.net/tags/ai-assisted-programming), [claude](https://simonwillison.net/tags/claude), [codex](https://simonwillison.net/tags/codex)

---

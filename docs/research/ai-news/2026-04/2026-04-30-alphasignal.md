# 📡 AlphaSignal — 2026-04-30

> 200k+ 訂閱；最新 AI 研究 / repos / 模型的 5 分鐘技術日報
> 來源：[AlphaSignal](https://alphasignalai.substack.com/feed)

---

## [How Kimi K2.6 Deploys 300 Sub Agents and One Shot a 104 Page Literature Review](https://alphasignalai.substack.com/p/how-kimi-k26-deploys-300-sub-agents)
*📡 AlphaSignal | 2026-04-30*

[Kimi K2.6](https://www.kimi.com/ai-models/kimi-k2-6) is one of those open-source AI releases where the model itself is only half of the story.

Yes, the benchmarks numbers are promising. Yes, the context window is huge. Yes, it is clearly being pushed as a serious coding, reasoning, and agentic model. But the more interesting part is the new Agent Swarm feature, because it changes the way we think about what an AI agent can do in one run.

Instead of one agent slowly working through a large task, Kimi K2.6 can spin up a large group of specialized sub agents and let them work in parallel. Moonshot says the system now supports up to 300 sub agents and 4,000 coordinated steps, compared to 100 sub agents and 1,500 steps in K2.5.

This does not mean bigger numbers automatically mean better results, but because agentic work usually breaks when the task gets too large, too messy, or too long. Kimi is trying to solve that by making the workflow wider instead of forcing one agent to do everything alone.

The 104 page literature review demo is the most eye catching example.

It reportedly produced a 10,000 word literature review in one shot, and the output could be downloaded as Word, PDF, PPT, or Excel.

It can also do 10 tabloid-style magazine covers (real history, real headlines) in a single prompt.

What are Swarm Agents?

Swarm Agents are basically AI workers running together on the same goal.

One agent can search for sources. Another can summarize papers. Another can extract data. Another can write a section. Another can build a table. Another can check formatting. 

Instead of asking one agent to do everything from start to finish, the system breaks the job into smaller pieces and lets different agents handle different parts.

Think of it like hiring a temporary research team for one task. You have a coordinator at the top, then a lot of smaller workers underneath. Each worker handles a narrow slice of the job, then sends the result back to the main agent.

This is different from the usual chatbot experience. In a normal chat, the model gives you an answer. In a swarm setup, the model acts more like a project manager that can assign work, collect outputs, and assemble the final result.

The big idea is not just “more AI.” It is structured AI work. Kimi K2.6 is trying to move from single response generation into multi step execution.

How Kimi K2.6 Agent Swarm works

The basic flow is simple enough to understand.

First, the main agent reads your request and figures out what kind of work needs to happen. If you ask for a literature review, it may split the work into source search, citation extraction, topic grouping, outline creation, section writing, table creation, and final formatting.

Then it creates specialized sub agents for those smaller jobs. Some agents may focus on search. Some may focus on analysis. Some may focus on code. Some may focus on writing. Some may focus on turning the final content into files.

After that, the agents work in parallel. This is where the swarm setup becomes useful. A single agent has to walk through a big task one step at a time, while a swarm can divide the work across many smaller agents and merge the results later.

The final step is synthesis. The coordinator collects the outputs, removes duplicate work, cleans up conflicts, organizes the structure, and turns the result into a final deliverable. In Kimi’s case, that deliverable can be a document, spreadsheet, slide deck, website, or dataset.

The technical improvements from K2.5 to K2.6

The Agent Swarm upgrade is mainly about scale.

Kimi K2.5 supported 100 sub agents and 1,500 coordinated steps. Kimi K2.6 raises that to 300 sub agents and 4,000 coordinated steps. That is 3x more sub agents and about 2.7x more coordinated steps.

The 300 sub agent limit also gives the system more room to split large tasks. A literature review, a market research report, a codebase audit, or a large dataset build can all be divided into many smaller pieces. This is exactly the kind of work where parallel execution makes sense.

Kimi K2.6 also has a long context window. The number being discussed is around 264K tokens, with the official benchmark setup showing 262,144 tokens. That gives the model more space to hold documents, tool results, notes, drafts, and intermediate outputs during a long run.

A big context window by itself does not make an agent reliable. You can still create a messy output inside a large context window. But when you combine long context, tool use, sub agents, and a coordinator layer, the system becomes much more capable for long and complicated tasks.

According the performance benchmarks from [LLM Stats](https://llm-stats.com/models/compare/kimi-k2.5-vs-kimi-k2.6), Kimi K2.5 outperforms in 1 benchmarks (Humanity’s Last Exam), while Kimi K2.6 is better at 14 benchmarks (BrowseComp, CharXiv-R, DeepSearchQA, GPQA, IMO-AnswerBench, LiveCodeBench v6, MathVision, MMMU-Pro, SciCode, SWE-bench Multilingual, SWE-Bench Pro, SWE-Bench Verified, Terminal-Bench 2.0, WideSearch).

Benchmarks and numbers

Kimi K2.6 looks especially tuned for agentic work, coding, search, long horizon execution, and tool use.

Here are the internal benchmarks from Kimi:

On BrowseComp, Kimi K2.6 scores 83.2, while the Agent Swarm version scores 86.3. Kimi K2.5 scores 74.9, and Kimi K2.5 Agent Swarm scores 78.4. This suggests the swarm layer improves the result, not just the presentation.

On DeepSearchQA, Kimi K2.6 reaches 92.5 F1 and 83.0 accuracy. Kimi K2.5 scored 89.0 F1 and 77.1 accuracy. That is a useful improvement for research heavy workflows where search quality, source reading, and synthesis all affect the final answer.

The coding numbers are also strong. Kimi K2.6 scores 66.7 on Terminal Bench 2.0, 58.6 on SWE Bench Pro, 80.2 on SWE Bench Verified, and 89.6 on LiveCodeBench v6.

These numbers do not mean Kimi K2.6 wins every category. Gemini, Claude, and GPT models still perform strongly across different benchmarks. But Kimi is clearly aiming at the agentic coding lane, where tool use and long task execution are just as important as raw answer quality.

It can do long horizon executions

The short coding prompts are not the most interesting part of Kimi K2.6.

The better examples are the ones where the model keeps working for hours, uses tools repeatedly, checks results, changes direction, and keeps going without falling apart. This is where most AI agents still struggle, especially when the first attempt does not work.

Moonshot says Kimi K2.6 ran a 12 hour local inference optimization task on a Mac. It made more than 4,000 tool calls across 14 iterations and improved Qwen3.5 0.8B inference speed from around 15 tokens per second to around 193 tokens per second. Moonshot also says the final result was around 20% faster than LM Studio in that test.

Another example involved exchange-core, an 8 year old open source financial matching engine. Kimi K2.6 reportedly ran for 13 hours, tested 12 optimization strategies, made more than 1,000 tool calls, modified over 4,000 lines of code, and improved medium throughput from 0.43 MT/s to 1.24 MT/s.

This is the kind of agent behavior developers actually care about. Writing a function is easy now. A lot of models can do that. The harder part is staying useful inside a messy engineering loop where the model has to read logs, edit files, test changes, inspect failures, and try again.

Kimi K2.6 becomes more interesting when you look at it from that angle. Not because it will always get everything right, but because it is clearly being built for longer, messier, tool heavy workflows.

Why developers should care

Agent Swarms are useful when a task has many parts that can run separately.

A literature review is an obvious example. The system can split papers across agents, extract claims, group themes, build tables, write sections, and assemble the final review. That would normally take a lot of back and forth if you were doing it with a normal chatbot.

Market research is another good use case. A swarm can scan competitors, collect pricing, summarize features, compare positioning, and generate a spreadsheet. This is exactly the kind of repetitive research work where parallel agents can save a lot of time.

For software teams, the use case is even more practical. A swarm can inspect a codebase from different angles. One agent can read API routes. Another can check database models. Another can look for security issues. Another can review dependencies. Another can write tests.

This does not remove the need for a developer. It gives the developer a first pass that would normally take hours or days. The developer still needs to review the output, but the starting point becomes much better than a blank page.

The file based output is important

One of the smarter parts of Kimi’s Agent Swarm pitch is that the output is not trapped inside chat.

The system can produce documents, websites, slides, spreadsheets, datasets, and other file based outputs. That sounds simple, but it changes the workflow a lot. You do not have to copy text out of chat and rebuild the format manually.

Kimi also talks about turning high quality files like PDFs, spreadsheets, slides, and Word documents into reusable “Skills.” The idea is that the system can preserve the structure and style of those files, then reuse that format in future tasks.

That is useful for companies. Imagine uploading your best internal report, investor update, market research template, or technical brief. The next time you ask for a similar output, the agent can follow the same structure instead of guessing from scratch.

This is where file generation starts to feel more practical. It is not only about producing more text. It is about producing work in the format people already use.

How it compares to competitors

Kimi K2.6 sits in the same conversation as GPT 5.4, Claude Opus 4.6, and Gemini 3.1 Pro.

Claude is still very strong for careful reasoning, writing, and code review. GPT has the advantage of product integration, tool ecosystems, and general reliability. Gemini is strong in long context and multimodal workflows.

Kimi’s angle is more specific. It is pushing open source coding performance, long horizon execution, and swarm based orchestration. The model is not just trying to be the smartest answer engine. It is trying to become the coordinator for a lot of smaller agents doing real work.

The benchmark table shows Kimi K2.6 competing closely with the major closed models. It wins some areas, loses some areas, and stays competitive across many agentic and coding tests.

For developers, the better comparison is workflow versus workflow. A strong single model is useful, but a strong model wrapped inside a reliable agent system becomes more interesting. That is where Kimi is trying to separate itself.

Let’s talk about user feedback

Let’s go back to the 104-page, 10K word literature review example. Not everyone is impressed by this demo.

Some people looked at it and had the obvious reaction: did anyone actually review the thing? How much of it is useful? How much of it is filler? How many citations are correct? How much of the analysis is just polished summary text?

That feedback makes sense. A huge document can still be bad. A 100,000 word review can still say very little. A 20,000 row dataset can still be messy. A clean looking PDF can still hide weak arguments, missing context, and shallow claims.

This is the risk with agent swarms. They can increase output faster than they increase judgment. When you have hundreds of agents working in parallel, you also create hundreds of places where bad information can sneak in.

One agent may summarize a weak source. Another may duplicate a claim. Another may miss the nuance. Another may write something that sounds confident but is only half true. When all of that gets merged into one polished document, the final output can look more reliable than it really is.

So no, “one shot” should not mean “publish it right away.”

The better way to look at Kimi K2.6 Agent Swarm is as a first pass machine. Let it collect the sources. Let it organize the messy parts. Let it build the tables. Let it draft the structure. Let it package the output.

Then a human still needs to check the claims, citations, logic, and final argument. That may sound less magical, but it is a more realistic way to use this kind of system.

The next wave of AI products may not be about who has the best chatbot response. It may be about who has the best orchestration layer, the best tool use, the best file generation, and the best way to keep agents working through long tasks without losing the plot.

At the same time, the hype needs a filter. A 104 page report is not automatically good. A swarm of 300 agents is not automatically useful. A polished document is not automatically correct.

The real question is not whether Kimi can generate more output than a normal chatbot. It clearly can. The better question is whether this kind of agent swarm can help people produce better work faster, without burying them under clean looking noise.

That is the part I want to see tested more.

Follow [@AlphaSignalAI](https://x.com/@AlphaSignalAI) for more content like this.

Check out http://AlphaSignal.ai to get a daily summary of top models, repos, and papers in AI. Read by 280,000+ devs.

---

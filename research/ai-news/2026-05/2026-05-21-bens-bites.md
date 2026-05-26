# 🍔 Ben's Bites — 2026-05-21

> Ben Tossell 的 AI 日報，工具圈消息源
> 來源：[Ben's Bites](https://www.bensbites.com/feed)

---

## [Can I get my agents on the phone?](https://www.bensbites.com/p/can-i-get-my-agents-on-the-phone)
*🍔 Ben's Bites | 2026-05-19*

Hey folks

[Google I/O starts today](https://blog.google/innovation-and-ai/technology/developers-tools/io-2026-save-the-date/), and Logan tweeted: "[The model is the product](https://x.com/OfficialLoganK/status/2056107524802457887)". There have been some rumours that the latest Gemini model scores similar on benchmarks to GPT 5.5 - but we'll see how it feels when actually using it - previous models also scored well but didn't feel great to work with.

When models are so good, harnesses will be much less important. I just don't think today is the day that happens. And on that point, the role of a harness will probably just shift - instead of managing how/which tools to use, the system prompt, context management etc it could be managed agents, sandboxing, cloud/local management. 

I started using Codex on my phone…but not all that much to be honest. A lot of the agent harnesses these days have ways to control your sessions from your phone - Claude Code has /remote-control, Pi can build one for itself (i use a telegram one) and Droid has mobile web + Droid computers. 

Most of my mobile first work at the moment is more brainstorming than building and I find myself flitting between all these options all the time. 

I used to use my OpenClaw bot like an addict, but haven't spoken to the poor bastard for weeks now. 

It may help that I'm currently focused on just one (ish) main thing - this 'course'. Which is really more of a library or reference manual on how I think about agents, how I steer them and build with them. 

* * *

_Ben 's Bites is brought to you by **[Hyperagent from Airtable](https://hyperagent.com/founding500?utm_source=newsletter&utm_medium=paidmedia&utm_campaign=HA-BENSBITES)**_

>  _[Hyperagent](https://hyperagent.com/founding500?utm_source=newsletter&utm_medium=paidmedia&utm_campaign=HA-BENSBITES), the cloud agent system with full computing environments, is giving $10M in inference credits to help founders build and run agent-first companies. The first 500 qualifying applicants gain access to this limited founder offer. [Applications close May 31st](https://hyperagent.com/founding500?utm_source=newsletter&utm_medium=paidmedia&utm_campaign=HA-BENSBITES)._

* * *

#### Headlines

  * **[Codex now connects your Mac to your phone](https://openai.com/index/work-with-codex-from-anywhere/)**. You can start tasks in Codex from your phone, but the actual work still runs on your Mac, devbox or remote machine, i.e. files, setup and credentials stay where they are, while you can approve commands, answer questions, and review diffs from your phone. This update also brings Hooks to Codex.

  * Anthropic is **[acquiring Stainless](https://x.com/AnthropicAI/status/2056419620643541012)** , a platform to build SDKs (also used by OpenAI), and they are shutting the service down. Also, at their London conference, they added self-hosted sandboxes and MCP tunnels to **[Claude Managed Agents](https://x.com/claudeai/status/2056645485696315581)** \- their "running agents made easy" product for companies.

  * **[Cloudflare tested Anthropic's Mythos](https://blog.cloudflare.com/cyber-frontier-models/)** against 50 of its repos. Quick takeaways:

    * Mythos is great at spotting real attacks, which are often many small vulnerabilities connected in a chain.

    * A single model, however smart, without a good harness leaves a lot to be found.

    * "Find bugs fast and patch them faster" is not a good idea. Teams need to focus on making bugs harder to chain (even if they exist) and to exploit.

  * **[Cursor's Composer 2.5](https://cursor.com/blog/composer-2-5)** (partly trained on SpaceX's GPUs) is out. The selective benchmarks that Cursor reports put the model roughly at the same place as Opus 4.7-xhigh and GPT-5.5-high, while being much cheaper than them.




* * *

[Subscribe now](https://www.bensbites.com/subscribe)

* * *

#### My feed

  * Two AI startups worth watching: [Magicpath (design canvas)](https://x.com/skirano/status/2054975534539370708) and [Raindrop AI (monitoring agents in production)](https://www.raindrop.ai/workshop/), both of which are making their products usable by external coding agents like Claude Code or Codex.

  * [Even Grok/xAI has a coding CLI now](https://x.ai/cli). Let's see what Google does with Gemini CLI at I/O today. 

  * [Linear Agent](https://x.com/karrisaarinen/status/2054993293210259752) can now read the codebase directly to build a hypothesis, investigate support questions, find people who worked on a feature, and more.

  * Best practices for [running Claude Code at scale](https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start).

  * Citadel's founder, Ken Griffin, one of the anti-AI hype people, is now saying that they are seeing [high-skilled jobs being "automated" by AI.](https://youtu.be/Csjy_A3Kj9s?t=1319)

  * [Browse.sh](https://browse.sh/) from Browserbase - open-source catalogue of skills/playbooks for agents to perform tasks on the internet.

  * [Watchmen](https://github.com/firstbatchxyz/watchmen) \- skill files your coding agents should already have from your past sessions. Local and open-source.

  * [Devin Auto-Triage](https://x.com/cognition/status/2056396941181727210) monitors bugs, alerts and incidents, investigates them and comes back with context, next steps or a PR.

  * [Motus Tracing](https://x.com/JiaZhihao/status/2055327218415341978) \- open-source observability for AI agents.

  * [designmd.sh](https://x.com/nozmen/status/2056396698688122910) \- a public registry for DESIGN.md files, so agents can understand design systems from repos.

  * [Jason Liu on Codex maxxing](https://jxnl.github.io/blog/writing/2026/05/10/codex-maxxing/) \- daily primitives for durable threads, shared memory, and keeping Codex useful across a real workflow.

  * [Taste MCP beta](https://buildwithtaste.com/product/mcp) \- portable design preferences for Codex, Cursor, Claude Code, etc.

  * Claire Vo and Thariq on "[HTML is the new markdown](https://youtu.be/Qrpm7E80wQ0)" \- using HTML artifacts as specs, micro-UIs, and human-readable agent context.

  * [Brian Lovin's Notion Worker](https://x.com/brian_lovin/status/2056444390940516409) \- syncs the people you follow on X into a Notion DB with optional AI enrichment.

  * Benedict Evans' new "[AI Is Eating The World](https://www.ben-evans.com/presentations)" deck.

  * Coatue says its AI framework moved from "follow the GPU" to "[follow the gigawatt](https://x.com/coatuemgmt/status/2055408437782290480)".




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

## [Agents feedback tip](https://www.bensbites.com/p/agents-feedback-tip)
*🍔 Ben's Bites | 2026-05-14*

Hey folks, I'm testing out something new in my building workflow…

When an agent asks for feedback it feels like the levels are

  1. type your response

  2. voice-to-text your response

  3. \+ images to your feedback

  4. get the agent to use the browser




But I just started screen-recording and talking then giving that file to my agent

[](https://substackcdn.com/image/fetch/$s_!Q4Fy!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F4b732846-79a5-4a45-b7a0-1cfc55a2918c_1458x448.png)

This is me, in droid, like 30 mins ago. It pulls together a pretty great visual report you can easily review. I can navigate to other websites or apps and show what good looks like from other people, I can highlight specific points and it'll recreate those points with GIFs.

It gives itself an 'actions' checklist underneath. And just feels great to have screenshot -> my feedback -> action for the agent. 

[](https://substackcdn.com/image/fetch/$s_!KXnE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fda62482a-91c6-4d5c-86e0-9f7c5418b0ba_1596x1546.png)

It's pretty great so far, and then I've got these html files saved in my projects to always refer back to - will be good for a build log too. 

Probably not great for the token conscious out there - and thinking about it, I could probably use ffmpeg to create actual clips of the video if I wanted. Agents read frames well though so it'd be more for me if I did. 

I turned it into a simple skill:

\---

name: video-to-html

description: Use when the user wants you to convert their video into a structured HTML document.

\---

Turn the user's video into a structured HTML document. Transcribe the video and pull out the keyframes linked to timestamps for important information. When the user is talking about something that is not dynamic, create short GIFs from the keyframes.

Let me know any cool use-cases or remixes of this 😊

* * *

_Ben 's Bites is brought to you by **[Hyperagent from Airtable](https://hyperagent.com/founding500?utm_source=newsletter&utm_medium=paidmedia&utm_campaign=HA-BENSBITES)**_

> [Hyperagent](https://hyperagent.com/founding500?utm_source=newsletter&utm_medium=paidmedia&utm_campaign=HA-BENSBITES), the cloud agent system with full computing environments, is giving $10M in inference credits to help founders build and run agent-first companies. The first 500 qualifying applicants gain access to this limited founder offer. [Applications close May 31st](https://hyperagent.com/founding500?utm_source=newsletter&utm_medium=paidmedia&utm_campaign=HA-BENSBITES).

* * *

#### Headlines

  * **[Your Claude plan is changing](https://x.com/ClaudeDevs/status/2054610152817619388)** if you use third-party tools (like Conductor, Zed, Openclaw, T3 Code, etc.) with it. 

    * Separate limit for all such usage. Provided as extra monthly credits equal to the value of your plan.

    * No subsidised tokens, credits won't roll over and usage after you burn through these credits is billed at API rates.

    * Using Claude in Claude Code, Claude app, etc., stays the same and is separate from this.

    * Starts from June 15th, but they are increasing your [weekly rate limits](https://x.com/ClaudeDevs/status/2054639777685934564) by 50% for the next two months.

  * Google announced some **Gemini on Android** updates before I/O - add features like auto-completing forms, rambling voice notes to clean text, and some app automations under the name "**[Gemini Intelligence](https://blog.google/products-and-platforms/platforms/android/gemini-intelligence/)** ". They also announced a new class of laptops called **[Googlebooks](https://blog.google/products-and-platforms/platforms/android/meet-googlebook)** , not to be confused with [Google Books](https://thenewthings.com/p/googlebooks-are-not-google-books).

  * **[Notion has a developer platform now](https://www.notion.com/product/dev)**. The biggest addition is a markdown API. Also, devs can sync outside data into Notion, build tools for Notion Agents, run code on Notion's infra, and eventually bring agents like Claude/Codex into Notion as teammates. But I think people who don't call them developers will use this.

    * They also launched a CLI called **[ntn](https://ntn.dev/)**.

  * **[Vercel published an AI Gateway production index](https://vercel.com/blog/ai-gateway-production-index)** based on real usage across apps and agents. Anthropic leads spend (61% -- due to opus), Google leads token volume (38% -- due to flash), and agentic workloads are 59% of token usage. Most large teams route across many models instead of betting on one lab.




* * *

[Subscribe now](https://www.bensbites.com/subscribe)

* * *

#### My feed

  * Cursor now lets you run cloud agents inside a [fully configured development environment](https://cursor.com/blog/cloud-agent-development-environments).

  * [Orca](http://github.com/stablyai/orca) \- Claude Code's agent view but for Codex, OpenCode, Droid and Pi.

  * [Oboe](https://oboe.com/) \- LLMs wrapped in a way that helps you learn.

  * [Interfaces.dev](https://interfaces.dev/) \- A monthly design engineering magazine about building great interfaces.

  * [Anthropic CFO Krishna Rao](https://x.com/patrick_oshag/status/2054532117410054252) on compute allocation, pricing dynamics and model company economics:

  * [AI IQ](https://www.aiiq.org/) \- frontier AI models, scored on the human IQ scale.

  * [Intercom is rebranding](https://x.com/eoghan/status/2054238946612367818) the entire company to Fin, their popular AI agent.

  * [Executor](https://executor.sh/home?try=local) \- Convert MCPs/OpenAPIs servers into code mode under the hood, 100% local on your device.

  * How OpenAI built a [safe sandbox for Windows](https://openai.com/index/building-codex-windows-sandbox/).




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

# 🍔 Ben's Bites — 2026-05-19

> Ben Tossell 的 AI 日報，工具圈消息源
> 來源：[Ben's Bites](https://www.bensbites.com/feed)

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

## [Learn the system](https://www.bensbites.com/p/learn-the-system)
*🍔 Ben's Bites | 2026-05-12*

Hey folks,

I watched [this](https://www.youtube.com/watch?v=lNVa33qUzZ8) this morning; 'Agentic coding is a trap -- and we all fell for it' \- it's surprising relevant past just developers. 

> enjoyed this because what i took away;  
> **learn the system**  
>   
>  to me, this is the difference of vibe coding and agentic engineering. i'm actively trying to learn the system, not the syntax.   
>   
> syntax is what i couldn't grapple when attempting to learn to code. but the system is clicking more for me the more i build  
>   
> im miles away from a 'competent software engineer' but im only building things for myself, so i dont *need* to be - but the more i build, the more that clicks into place.   
>   
> i didnt realise it when i was slinging no-code in 2018 but it was a version of learning parts of a system to get software to work (webflow - frontend, airtable - database, zapier - api/backend). it had limitations but now i replaced all of that with code.   
>   
> having actual competent engineers create skills and systems to help a sloppy codebase or process is helping (as well as better models). but i do rely on that for years i didnt spend learning to code.   
>   
> stay curious folks

[tweeted it earlier](https://x.com/bentossell/status/2054118034327916874?s=20)

Link to the [original blog post](https://larsfaye.com/articles/agentic-coding-is-a-trap). 

And I've been tweaking my AGENTS.md + setup files - as I'm getting closer with the 'course' I'm reminding myself to not let your docs slip. 

[](https://substackcdn.com/image/fetch/$s_!cgXh!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F88f08de1-aed6-40ee-ba2d-29cd8a9dc45b_2386x1858.png)there'll be a lesson on this and i'll go thru it all

Oh and…

* * *

_Ben 's Bites is brought to you by [Lightfield](https://lightfield.app/blog/introducing-skills?utm_source=newsletter&utm_medium=paid&utm_campaign=bens_bites&utm_content=primary_5-12-2026)_

> **Lightfield** is an AI-native CRM that just shipped **[Skills](https://lightfield.app/blog/introducing-skills?utm_source=newsletter&utm_medium=paid&utm_campaign=bens_bites&utm_content=primary_5-12-2026)**. Define any workflow in plain English and trigger it with a sentence. The AI agent executes against your full CRM data graph with code execution, web search, and file I/O. 3,000+ startups on the platform. [Try free](https://lightfield.app/blog/introducing-skills?utm_source=newsletter&utm_medium=paid&utm_campaign=bens_bites&utm_content=primary_5-12-2026)

* * *

#### Headlines

  * You can now work with **[all your Claude Code agents in a single window](https://claude.com/blog/agent-view-in-claude-code)** inside the terminal. You can see their status and reply inline to unblock when they need your input. Any running session can be moved to the agent view with /bg.

  * **[Codex now works directly in Chrome](https://x.com/OpenAI/status/2052480800004956323)** on macOS and Windows. It can use sites and apps across tabs in the background without taking over your browser. 

  * OpenAI also released **[three new Realtime models](https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/)** in the API: Realtime 2 for voice-to-voice use cases with best intelligence, Realtime Translate for audio translation across 70 input and 13 output languages, and Realtime-Whisper for live speech to text.

  * OpenAI released a cyber defence product, **[Daybreak](https://openai.com/daybreak/)**. Their OpenAI's answer to Anthropic's Mythos?

  * **Thinking Machines** finally have a model to show us (not letting us try though). They are calling them **[interaction models](https://thinkingmachines.ai/blog/interaction-models/)**. Basically models where you can chat with audio and video input with audio outputs. It seems really impressive for the capabilites they are claiming, for example, time awareness, simultaneous speech and visual cues, but all similar products (ChatGPT's Advanced Voice Mode, Gemini Live) fail when put in users hands.

  * **[OpenAI is starting a deployment company](https://openai.com/index/openai-launches-the-deployment-company/)** in partnership with major consulting firms. It acquired a 150-person AI consulting company, "Tomoro", to set this up and is putting in $4B of initial investment. The goal is to work with other companies and build AI systems for them.

    * I think this means they're going to effectively transform a ton of knowledge workers and upskill them to knowing how to work with agents. ie able to be a builder. And if you're a builder -> you can use Codex. You can see how it all links 😊




* * *

[Subscribe now](https://www.bensbites.com/subscribe)

* * *

#### My feed

  * Artificial Analysis is testing rank models + harness combinations together in their [Coding Agent Index](https://artificialanalysis.ai/agents/coding-agents). Among the combinations they have tested, Opus 4.7 with Cursor CLI is on top with GPT-5.5 in Codex and Opus 4.7 in Claude Code at a close second.

  * Ramp trained a small RL model with [Fast Ask](https://x.com/RampLabs/status/2052448843099254956) with Prime Intellect for spreadsheet Q&A. They say it beats Opus by 4% on exact match accuracy at Haiku latency.

  * [Replit Parallel Agents](https://docs.replit.com/core-concepts/agent/task-system) lets Replit Agent break work into tasks, run them in isolated copies of your app, and merge them back after review.

  * [Notion Skills](https://x.com/brian_lovin/status/2053876320459964524) \- Brian Lovin is using a Notion database like an app store for agent skills, with two-way sync to Claude, Codex and other local agents.

  * [React Doctor v2](https://x.com/aidenybai/status/2052780632510775469) catches bad React code from agents.

  * [Printing Press](https://x.com/mvanhorn/status/2052422567181611010) \- generate agent-native CLIs for apps like Linear, ESPN, Kayak, etc.

  * [The Claude Platform on AWS](https://x.com/claudeai/status/2053868592286822443) is now generally available. AWS customers get Claude API features with AWS auth, billing and commitment retirement.

  * OpenAI's API has a new [Files SDK](https://files-sdk.dev/) for object and blob storage and an [OpenAI Developers plugin](https://x.com/OpenAIDevs/status/2053925962287583379) for Codex to build faster with OpenAI APIs.

  * Parallel AI's [Monitor API](https://parallel.ai/blog/monitor-api-ga) is now GA. It sends web push updates to background agents instead of agents constantly polling for changes.

  * [zero-native](https://github.com/vercel-labs/zero-native) \- build native desktop and mobile apps with web UI.

  * A spec for [how interfaces should present Markdown](https://github.com/vercel-labs/mdxg).

  * [7 Powers in the age of AI](https://x.com/jeffreyhuber/status/2054042150019707082) for building a company.

  * [a framework for hackable software](https://github.com/zenbu-labs/zenbu.js) i.e. apps that ship with their raw source code, where users can modify them using coding agents. 

  * New research from Anthropic [translates the inner workings of Claude into text](https://www.anthropic.com/research/natural-language-autoencoders) and [teaches it good behaviour](https://www.anthropic.com/research/teaching-claude-why) using fictional stories.

  * [Peekaboo 3.0](https://x.com/steipete/status/2053114837698249190) \- Peter's macOS computer-use tool got action-first automation, unified screenshot + UI detection, cleaner JSON and better snapshots.




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

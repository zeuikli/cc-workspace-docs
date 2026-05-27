---
title: "The Neuron — 2026-05-24"
date: 2026-05-24
source: The Neuron
type: ai-news
---

# 🧠 The Neuron — 2026-05-24

> 面向非技術讀者的 AI 日報，3 分鐘讀完
> 來源：[The Neuron](https://rss.beehiiv.com/feeds/N4eCstxvgX.xml)

---

## [😸 OpenAI solved an 80-year math problem by... disproving it](https://www.theneurondaily.com/p/openai-solved-an-80-year-math-problem-by-disproving-it)
*🧠 The Neuron | 2026-05-22*

Welcome, humans. 

Some people just inherently understand their priorities in life, and now that they can code, are unleashing true beauty into the world: 

[](https://www.reddit.com/r/vibecoding/comments/1tjp4uy/published_my_first_app_a_compass_that_points_to/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-solved-an-80-year-math-problem-by-disproving-it)

_Happy Memorial Day Weekend to everyone who celebrates! Gonna keep it light today._

**Here’s what happened in AI today:**

  * 🐱 OpenAI’s model solved an 80-year math problem.

  * 📰 OpenAI and Anthropic’s revenue race got weird fast.

  * 📰 Trump delayed an AI order as California prepared workers.

  * 🍪 Qwen 3.7 Max ran an agent for 35 hours.

  * 🎓 Use Codex /goal mode for long tasks.




**Hey:**_Want to reach 700,000+ AI-hungry readers?_[Advertise with us!](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)_[](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)_

**P.S:**_Love robots? We’re starting a new robotics newsletter!_[Sign up early here](https://form.jotform.com/260897013570156?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-solved-an-80-year-math-problem-by-disproving-it).

# 🙀 OpenAI says its model solved an 80-year math problem by… disproving it.

Math has one perk for AI watchers: eventually, somebody checks the work.

That makes [OpenAI’s new claim](https://openai.com/index/model-disproves-discrete-geometry-conjecture/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-solved-an-80-year-math-problem-by-disproving-it) worth paying attention to. The company says an internal reasoning model apparently disproved the Erdős unit distance conjecture, a discrete geometry problem from 1946. _If that all made you go “Huh?”, keep scrolling._

**Here’s the basic explanation of the problem:** if you place _n_ points on a flat plane, how many pairs can sit exactly one unit apart? For decades, many mathematicians believed square-grid style patterns were basically the best possible answer.

And yet, OpenAI’s unreleased reasoning model apparently found a counterexample: a new infinite family of point arrangements that creates more unit-distance pairs than the old grid-based belief allowed. That means the model “solved” the problem by proving the conjecture was false.

**Here’s what happened:**

  * OpenAI said the original proof came from a general-purpose reasoning model, rather than a system specially trained, scaffolded, or targeted for this problem.

  * The [proof](https://cdn.openai.com/pdf/74c24085-19b0-4534-9c90-465b8e29ad73/unit-distance-proof.pdf?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-solved-an-80-year-math-problem-by-disproving-it) shows infinitely many point sets with at least _n_ 1+δ unit-distance pairs.

  * That beats Erdős’s old _n_ 1+o(1) conjecture, which roughly meant “only a tiny bit better than linear.”

  * External mathematicians published [companion remarks](https://cdn.openai.com/pdf/74c24085-19b0-4534-9c90-465b8e29ad73/unit-distance-remarks.pdf?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-solved-an-80-year-math-problem-by-disproving-it) verifying and explaining the result.

  * Princeton mathematician Will Sawin [sharpened it](https://arxiv.org/abs/2605.20579?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-solved-an-80-year-math-problem-by-disproving-it), showing more than _n_ 1.014 unit-distance pairs for arbitrarily large point sets.




**Why this matters:** This is a cleaner test of AI reasoning than a benchmark (a standardized model test). Benchmarks can reward lucky guesses. A proof has to survive expert review, line by line.

The proof used algebraic number theory (math about number systems), including class field towers and Golod-Shafarevich theory, to crack a geometry problem that sounds simple.

[TechCrunch noted](https://techcrunch.com/2026/05/20/openai-claims-it-solved-an-80-year-old-math-problem-for-real-this-time/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-solved-an-80-year-math-problem-by-disproving-it) an earlier OpenAI Erdős claim fell apart after the model surfaced existing results. This time, outside mathematicians signed the companion remarks, including some critics of that previous episode. _OpenAI turned their haters into benchmarks, basically._

[Elliot Glazer](https://x.com/MTSlive/status/2057533295567753438?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-solved-an-80-year-math-problem-by-disproving-it) added an interesting POV on this too: AI may surface answers humans _could_ have found, but didn’t have time (or the will) to go after because it didn’t seem worth finding. Only so many experts can spend years attacking a problem the field doubts exists in the first place. 

**Our take:** Think about the loop here: the model found the weird route, humans checked the work, Codex helped clean up the write-up, and Princeton’s Will Sawin showed the construction’s edge **compounds at huge scale** , which is why the result matters beyond “AI found a math trick.”

Math is unusually AI friendly because proofs can be checked. Biology, medicine, and business strategy have messier feedback loops. Greg Kamradt of ARC Prize recently shared a nice breakdown of the 7 levels of verifiability that tracks how hard things are to verify on a spectrum due to the length of time it takes to get “feedback” on if your actions led to the outcome you want. [Read our deep dive on the topic here.](https://theneuron.ai/explainer-articles/agi-is-the-wrong-scoreboard-this-7-level-framework-explains-ai-progress-better/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-solved-an-80-year-math-problem-by-disproving-it)

**FROM OUR PARTNERS**

# Your software needs to be compliant to win deals. But you also need your engineers focused on building your product—NOT pulling SOC 2 evidence. 

The[ Vanta Agent ](https://www.vanta.com/downloads/on-demand-demo?utm_campaign=on-demand-demo&utm_source=the-neuron&utm_medium=newsletter)is the sharpest GRC engineer you’ve never had to hire, working tirelessly across the platform to draft policies, complete questionnaires, and flag issues before they escalate.

Fast-moving companies like Ramp and Cursor use [Vanta](https://www.vanta.com/downloads/on-demand-demo?utm_campaign=on-demand-demo&utm_source=the-neuron&utm_medium=newsletter) to get and stay compliant, simplify their audit process, and unblock deals—so teams can get back to building.

[Ready to learn more? Watch the on-demand demo to see how Vanta works. ](https://www.vanta.com/downloads/on-demand-demo?utm_campaign=on-demand-demo&utm_source=the-neuron&utm_medium=newsletter)

# 🎓 AI Skill of the Day: Give Codex a Definition of Done

Long agent tasks fail when the AI forgets what “done” means. Codex’s [/goal mode](https://developers.openai.com/codex/prompting?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-solved-an-80-year-math-problem-by-disproving-it#goal-mode) fixes that by giving it a persistent objective it can keep checking as it works.

Use this for tasks with many steps: migrations, refactors, audits, bug sweeps, or report generation. The trick is to write the goal like a mini contract: outcome, constraints, and tests. If /goal does not appear, OpenAI says you can enable features.goals in config.toml or run codex features enable goals.

Try this:
    
    
    /goal
    Audit this project for newsletter draft readiness.
    
    Definition of done:
    1. Every section has the required header.
    2. Every hyperlink is attached to a short, natural anchor.
    3. No Treats or Around the Horn bullets use bold text.
    4. Every technical term has a plain-English parenthetical on first use.
    5. Return a short report with pass/fail status and exact fixes made.
    
    Before editing, make a checklist. After editing, run the checklist again and show me what changed.

**Total AI beginner?**[Start here](https://www.theneuron.ai/explainer-articles/everything-we-covered-in-our-ai-for-total-beginners-livestream-full-guide-with-timestamps/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-solved-an-80-year-math-problem-by-disproving-it) ([goes with this video](https://www.youtube.com/live/QbFU0UNMVaU?si=skJsgUIDjKjAx3DU&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-solved-an-80-year-math-problem-by-disproving-it)). 

**Have a specific skill you want to learn?** [Request it here.](https://docs.google.com/forms/d/e/1FAIpQLSd_-hSXtB9ytR1HQrU85IJnJw233bNKptiGB5BZh9maPse1Eg/viewform?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-solved-an-80-year-math-problem-by-disproving-it)

# 🍪 Treats to Try 

_*Asterisk = from our partners (only the first one!).__[Advertise to 700K+ readers here](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-solved-an-80-year-math-problem-by-disproving-it)_ _!_

  1. Want a serious AI sandbox? [Dell Pro Max with GB10](https://www.dell.com/en-us/shop/desktop-computers/dell-pro-max-with-gb10/spd/dell-pro-max-fcm1253-micro/xcto_fcm1253_usx?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-solved-an-80-year-math-problem-by-disproving-it) gives builders NVIDIA Grace Blackwell power, 128GB memory, and DGX OS 7. [Check it out. ](https://www.dell.com/en-us/shop/desktop-computers/dell-pro-max-with-gb10/spd/dell-pro-max-fcm1253-micro/xcto_fcm1253_usx?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-solved-an-80-year-math-problem-by-disproving-it)

  2. [Qwen 3.7 Max](https://www.alibabacloud.com/blog/qwen3-7-the-agent-frontier_603154?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-solved-an-80-year-math-problem-by-disproving-it) gives you an agent model built for long work sessions, including a 35-hour autonomous GPU-kernel optimization run with 1,158 tool calls, 432 tests, and a reported 10x speedup on Alibaba hardware.

  3. [Command A+](https://cohere.com/blog/command-a-plus?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-solved-an-80-year-math-problem-by-disproving-it) gives you Cohere’s open enterprise model for reasoning, tool use, images, 48 languages, and private deployments, with 218B total parameters but only 25B active per request (so it runs cheaper than its full size suggests)—free to try if you self-host.

  4. [Codex](https://developers.openai.com/codex/prompting?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-solved-an-80-year-math-problem-by-disproving-it#goal-mode) now supports /goal for long-running tasks, [Computer Use](https://developers.openai.com/codex/app/computer-use?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-solved-an-80-year-math-problem-by-disproving-it#locked-use) for clicking around Mac apps, and [Appshots](https://developers.openai.com/codex/appshots?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-solved-an-80-year-math-problem-by-disproving-it) for giving Codex richer desktop context —available in Codex.

  5. [Figma](https://www.figma.com/blog/the-figma-agent-is-here/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-solved-an-80-year-math-problem-by-disproving-it) added a design agent directly on the canvas, so you can generate designs, edit existing files, and create variations from text prompts—[waitlist](https://www.figma.com/join-waitlist/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-solved-an-80-year-math-problem-by-disproving-it).

  6. [Runway Aleph 2.0](https://runwayml.com/news/introducing-aleph-2-and-edit-studio?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-solved-an-80-year-math-problem-by-disproving-it) edits one video frame and then carries that change through the rest of the clip, so you can revise video without rebuilding it shot by shot.

  7. [Windsor MCP for SEO](https://windsor.ai/windsor-mcp-for-seo/?utm_source=chatgpt.com) connects your SEO data from GSC, GA4, Google Ads, WordPress, and more to ChatGPT or Claude so you can spot ranking drops, content gaps, and conversion opportunities without building reports by hand —free trial, then $23/mo.




# PON DE REPLAY: Ben Cherry of LiveKit Teaches Us How to Make Voice Agents (Its SO Easy): 

[](https://www.youtube.com/live/kdzmBBqMyJ0?si=32wIfHECJ4Km3jdC&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-solved-an-80-year-math-problem-by-disproving-it)

Click the image above to watch on YouTube!

**ICYMI:** Ben Cherry of [LiveKit](https://livekit.com/?utm_source=chatgpt.com) joined us on The Neuron’s weekly livestream to show us how to build real-time voice agents that can listen, interrupt, call tools, and run in production. _And guess what? It’s so easy, even an agent can do it! You can literally grab the transcript from Google (click “… more” under the vid description, scroll down to click “Show Transcript”, then copy the transcript and give it to your Codex / Claude to set up for you)._

It’s a super fun episode; Ben shows how to launch an agent via LiveKite (and what code repos to use if that kinda thing doesn’t intimidate you), edited his agent live with Claude Code, and even cloned his own voice for us live. [**Click here to watch.**](https://www.youtube.com/live/kdzmBBqMyJ0?si=32wIfHECJ4Km3jdC&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-solved-an-80-year-math-problem-by-disproving-it)

# 📰 Around the Horn 

  * [OpenAI](https://www.theinformation.com/articles/openai-held-1-billion-revenue-lead-anthropic-first-quarter?rc=lks9on&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-solved-an-80-year-math-problem-by-disproving-it) reportedly generated about $5.7B in Q1, nearly $1B ahead of Anthropic, while [Anthropic](https://www.axios.com/2026/05/21/ai-news-cycle-openai-anthropic-spacex?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-solved-an-80-year-math-problem-by-disproving-it) is projected to more than double to $10.9B in Q2.

  * [California](https://www.gov.ca.gov/2026/05/21/governor-newsom-signs-first-of-its-kind-executive-order-to-prepare-workers-and-businesses-for-potential-ai-disruption/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-solved-an-80-year-math-problem-by-disproving-it) signed a first-in-the-nation order to prepare workers and small businesses for AI disruption. 

  * [xAI’s Grok](https://www.reuters.com/world/grok-falls-flat-washington-undercutting-spacexs-ai-growth-story-2026-05-21/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-solved-an-80-year-math-problem-by-disproving-it) reportedly flopped with U.S. government buyers, with Reuters finding only three identified federal use cases.

  * [Intuit](https://techcrunch.com/2026/05/20/intuit-to-lay-off-over-3000-employees-to-refocus-on-ai/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-solved-an-80-year-math-problem-by-disproving-it) planned to lay off 3,000+ workers, about 17% of its workforce, to simplify the company and refocus on AI products. [_Remember Monday’s story_](https://www.theneuron.ai/newsletter/ai-layoffs-are-tanking-stocks-not-saving-them/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-solved-an-80-year-math-problem-by-disproving-it) _?_

  * [Samsung](https://www.bloomberg.com/news/articles/2026-05-21/samsung-chip-workers-to-get-average-340-000-bonus-in-ai-boom?embedded-checkout=true&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-solved-an-80-year-math-problem-by-disproving-it) will reportedly distribute about $26.6B in bonuses to chip workers, averaging roughly $340K per employee. _That’s how important chips are!_

  * [NVIDIA](https://techcrunch.com/2026/05/20/jensen-huang-says-hes-found-a-brand-new-200b-market-for-nvidia/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-solved-an-80-year-math-problem-by-disproving-it) CEO Jensen Huang said CPUs built for AI agents could become a new $200B market for the company.

  * [Taiwan](https://www.taipeitimes.com/News/taiwan/archives/2026/05/22/2003857777?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-solved-an-80-year-math-problem-by-disproving-it) sought to detain three people accused of forging documents to smuggle NVIDIA AI chips to China, Hong Kong, and Macau.




**FROM OUR PARTNERS**

### Your next great hire lives in Slack.

[](https://ref.getviktor.com/vik-bh-founders-general1?utm_campaign=&#123;{publication_alphanumeric_id}}&_bhiiv=opp_64ab39e2-fe9b-4395-99d5-93e4efe08ce0_58600c56&bhcl_id=414689ae-64c2-4e05-8a05-668de2ad75c0_&#123;{subscriber_id}}_&#123;{email_address_id}})

Viktor is an AI coworker that connects to your tools and [ships real work](https://ref.getviktor.com/vik-bh-founders-general1?utm_campaign=&#123;{publication_alphanumeric_id}}&_bhiiv=opp_64ab39e2-fe9b-4395-99d5-93e4efe08ce0_58600c56&bhcl_id=414689ae-64c2-4e05-8a05-668de2ad75c0_&#123;{subscriber_id}}_&#123;{email_address_id}}). Ask Viktor to pull a report, build a client dashboard, or source 200 leads matching your ICP. Most teams hand over half their ops within a week.

[Add Viktor to Slack for free.](https://ref.getviktor.com/vik-bh-founders-general1?utm_campaign=&#123;{publication_alphanumeric_id}}&_bhiiv=opp_64ab39e2-fe9b-4395-99d5-93e4efe08ce0_58600c56&bhcl_id=414689ae-64c2-4e05-8a05-668de2ad75c0_&#123;{subscriber_id}}_&#123;{email_address_id}})

# 💡 Intelligent Insights

  * [Data filtering](https://arxiv.org/abs/2605.19407?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-solved-an-80-year-math-problem-by-disproving-it): this research paper argues larger models can benefit from messy data that smaller models cannot use well (basically scaling laws for data).

  * [AI oversight](https://www.aisi.gov.uk/blog/will-it-become-harder-to-oversee-ai-systems?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-solved-an-80-year-math-problem-by-disproving-it): the U.K. AI Security Institute warned that today’s oversight methods may degrade as models get more capable.

  * [Arena’s frontier](https://x.com/arena/status/2057486887938646370?s=46&t=T4ASCAO-x6EzmRSTvpSgEg&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-solved-an-80-year-math-problem-by-disproving-it): [Arena.ai](https://Arena.ai?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-solved-an-80-year-math-problem-by-disproving-it) found GPT-4-level model quality is now roughly 500x cheaper than it was in 2023 (and 4 other insights you might like!).

  * [Accessible for AI](https://www.techpolicy.press/the-web-is-being-made-accessible-for-ai-not-people/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-solved-an-80-year-math-problem-by-disproving-it): a sharp TechPolicy Press critique of llms.txt, MCP servers, and other machine-readable web infrastructure that may leave disabled users behind.

  * **If you read anything today, read this** : [After Automation](https://every.to/p/after-automation?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-solved-an-80-year-math-problem-by-disproving-it) from Dan Shipper argued AI creates more work for humans by flooding the world with generic output and raising the value of taste, context, and judgment. I’ll end the newsletter with this insight: 




[](https://every.to/p/after-automation?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-solved-an-80-year-math-problem-by-disproving-it)

Source: Dan Shipper @ Every; image linked to the article

# A Cat’s Commentary 

Don’t say we never highlight negative feedback! 

| That’s all for now.   
---|---  
  
**P.P.S:** Love the newsletter, but only want to get it once per week? Don’t unsubscribe—[update your preferences here](https://www.theneurondaily.com/subscribe/f5596641-9099-4045-9641-731cd9fdcf90/preferences?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=openai-solved-an-80-year-math-problem-by-disproving-it).

---

## [😺 Watch LIVE NOW: Building AI Voice Agents w/ LiveKit's Ben Cherry](https://www.theneurondaily.com/p/watch-live-now-building-ai-voice-agents-w-livekit-s-ben-cherry)
*🧠 The Neuron | 2026-05-21*

[](https://youtube.com/live/kdzmBBqMyJ0?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-building-ai-voice-agents-w-livekit-s-ben-cherry)

Click the image above to watch live on YouTube!

Welcome, humans.

Voice agents are having a moment — but if you’ve ever wondered what it actually takes to build one that feels fast, natural, and useful, this stream is for you.

We’re [live RIGHT NOW with Ben Cherry from LiveKit](https://youtube.com/live/kdzmBBqMyJ0?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-building-ai-voice-agents-w-livekit-s-ben-cherry), talking about the future of real-time AI agents; the kind that can listen, respond, handle interruptions, use tools, and maybe even survive a conversation with an actual human being.

Ben is also going to show us a cool demo, so this won’t just be theory. We’ll dig into what works, what breaks, and what builders need to know as voice and multimodal AI move into real products.

## 🔴 What we're covering live, on stream:

  * What LiveKit helps developers build

  * Why real-time voice AI is so much harder than “ChatGPT with a microphone”

  * How latency, interruptions, audio quality, and turn-taking affect the user experience

  * What separates a polished demo from a production-ready voice agent

  * Where voice agents are already useful today and what’s still mostly hype

  * A live demo from Ben showing what this tech can actually do




**Watch live now here:**

[](https://youtube.com/live/kdzmBBqMyJ0?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-building-ai-voice-agents-w-livekit-s-ben-cherry)

**P.S.** Timestamps will be added to the video after the stream, so if you can't make it live, bookmark this email and come back tomorrow. You'll be able to jump straight to the parts you care about.

# 📬 Full writeup in Sunday's newsletter

Not free atm? We've got you. We'll publish a full breakdown of everything we found in tomorrow's daily newsletter, with the sharpest prompts, the biggest surprises, and a direct "should you switch?" call.

**THIS EPISODE WAS BROUGHT TO YOU BY…**

# Want to see your AI-adjacent product or service show up right here, below these podcast promos?

_Click the button below to advertise to our 700K+ readers!_

[_Advertise in The Neuron here!_](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-building-ai-voice-agents-w-livekit-s-ben-cherry)

# 🎙️ In Case You Missed It… 

[Four recent interviews](https://www.youtube.com/@theneuronai?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-building-ai-voice-agents-w-livekit-s-ben-cherry) you’ll definitely want to check out _(pick whatever looks interesting to you and dive in!):_

### **1.** The AI Trying to Solve Math’s Biggest Mystery w/ Tudor Achim of Aristotle**:**

[](https://youtu.be/8MNfLsi0aKY?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-building-ai-voice-agents-w-livekit-s-ben-cherry)

What happens when AI stops simply giving answers and starts producing proofs a computer can verify? In this episode of The Neuron, [Corey and Grant talk with Tudor Achim](https://youtu.be/8MNfLsi0aKY?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-building-ai-voice-agents-w-livekit-s-ben-cherry), Co-Founder and CEO of [Harmonic, the company behind Aristotle](https://aristotle.harmonic.fun/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-building-ai-voice-agents-w-livekit-s-ben-cherry), a formal reasoning system built to generate machine-checkable mathematical proofs.

Tudor explains why math may be the clearest test case for moving AI from “trust me” to “check me,” and why formal verification could matter far beyond Olympiad benchmarks.

**Listen now on**[YouTube](https://youtu.be/8MNfLsi0aKY?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-building-ai-voice-agents-w-livekit-s-ben-cherry) | [Spotify](https://open.spotify.com/episode/13u26j30bPhpJ4Ke1d3N5I?si=nxIEp8QkSKGp7qahEHKXTg&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-building-ai-voice-agents-w-livekit-s-ben-cherry) | [Apple Podcasts](https://podcasts.apple.com/us/podcast/the-ai-trying-to-solve-maths-biggest-mystery-w-tudor/id1742267001?i=1000768789039&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-building-ai-voice-agents-w-livekit-s-ben-cherry)

### **2.** **AI isn't just chatbots, it's designing medicines now:**

**[Inside Isomorphic Labs and How It Works](https://youtu.be/W0NSk2y3OFI?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-building-ai-voice-agents-w-livekit-s-ben-cherry)** — Becky Paul and Michael Schaarschmidt at [Isomorphic Labs](https://www.isomorphiclabs.com/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-building-ai-voice-agents-w-livekit-s-ben-cherry) ([Google DeepMind](https://deepmind.google/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-building-ai-voice-agents-w-livekit-s-ben-cherry)'s medicine-making spinout, built by the team behind [AlphaFold](https://deepmind.google/science/alphafold/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-building-ai-voice-agents-w-livekit-s-ben-cherry) — which won the [2024 Nobel Prize in Chemistry](https://www.nobelprize.org/prizes/chemistry/2024/press-release/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-building-ai-voice-agents-w-livekit-s-ben-cherry)) on how their AI is taking on the diseases pharma has been giving up on for decades. The clearest "what AI actually means for patients" explainer we've published. [YouTube](https://youtu.be/W0NSk2y3OFI?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-building-ai-voice-agents-w-livekit-s-ben-cherry) | [Spotify](https://open.spotify.com/episode/2TzHhOkVIN9AL3GXXxSyDe?si=Hfr5NDX1Q_ybcdKSTMdsNQ&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-building-ai-voice-agents-w-livekit-s-ben-cherry) | [Apple Podcasts](https://podcasts.apple.com/us/podcast/the-neuron-ai-explained/id1742267001?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-building-ai-voice-agents-w-livekit-s-ben-cherry)

### 3\. You've definitely used Canva. But you probably haven't seen it like this: 

[](https://youtu.be/JqZmdg71Bnc?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-building-ai-voice-agents-w-livekit-s-ben-cherry)

**[24 Billion AI Uses Later, What Canva Learned About AI Design](https://youtu.be/JqZmdg71Bnc?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-building-ai-voice-agents-w-livekit-s-ben-cherry)** — Danny Wu, Canva's Head of AI Products, walks us through how their AI tools have been used **24 BILLION times** , why they spent over a year building a design model that generates _layered, editable_ assets (not just flat images), and how typing one word ("MCP") lets you create fully editable Canva designs from inside ChatGPT, Claude, or Copilot. [YouTube](https://youtu.be/JqZmdg71Bnc?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-building-ai-voice-agents-w-livekit-s-ben-cherry) | [Spotify](https://open.spotify.com/episode/1M79tzwFNuqTrCf2d40tFa?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-building-ai-voice-agents-w-livekit-s-ben-cherry) | [Apple Podcasts](https://podcasts.apple.com/us/podcast/24-billion-ai-uses-later-what-canva-learned-about-the/id1742267001?i=1000754551676&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-building-ai-voice-agents-w-livekit-s-ben-cherry)

### **4\. Your laptop is about to become Hollywood:**

[](https://youtu.be/0WBnAEIkj5A?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-building-ai-voice-agents-w-livekit-s-ben-cherry)

**[This Tool Turns Your Laptop Into a Movie Studio](https://youtu.be/0WBnAEIkj5A?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-building-ai-voice-agents-w-livekit-s-ben-cherry)** — Yaron Inger, CTO and co-founder of [Lightricks](https://www.lightricks.com/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-building-ai-voice-agents-w-livekit-s-ben-cherry) (the company behind Facetune), on why their open-source [LTX-2](https://ltx.io/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-building-ai-voice-agents-w-livekit-s-ben-cherry) model has been downloaded **4.5 million times in two months** , runs locally on a consumer GPU, and just ate Pinky-Promise level expensive AI video tools for breakfast. The full [LTX Desktop](https://github.com/Lightricks/LTX-Desktop?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-building-ai-voice-agents-w-livekit-s-ben-cherry) editor was vibe-coded by 2.5 people in 10 days. [YouTube](https://youtu.be/0WBnAEIkj5A?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-building-ai-voice-agents-w-livekit-s-ben-cherry) | [Spotify](https://open.spotify.com/episode/0W6WTL0ACM3HAI6ND9vUWC?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-building-ai-voice-agents-w-livekit-s-ben-cherry) | [Apple Podcasts](https://podcasts.apple.com/us/podcast/ai-just-democratized-filmmaking-w-ltx-co-founder/id1742267001?i=1000754869036&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-building-ai-voice-agents-w-livekit-s-ben-cherry)

## One more before you go:

A few weeks ago we went live with the **["AI for Total Beginners" 5-Level Starter Stack](https://www.youtube.com/live/QbFU0UNMVaU?si=YRpR8raOXHvfrBqw&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-building-ai-voice-agents-w-livekit-s-ben-cherry)**, a full framework for going from "I've never touched AI" to "AI saves me 10 hours a week." No coding required. It's at 11,000+ views and counting, so it’ll be a good follow-up to this one if you haven’t watch it yet! 

**Last thing:** And if you [haven’t subscribed yet, please do!](https://www.youtube.com/@theneuronai?sub_confirmation=1&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-building-ai-voice-agents-w-livekit-s-ben-cherry) Click the image below to go to our channel and hit “subscribe” to get notified right when new videos go live. 

[](https://www.youtube.com/@theneuronai?sub_confirmation=1&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-building-ai-voice-agents-w-livekit-s-ben-cherry)

We have a goal to hit **50K subscribers** by the end of the year (if not 100K), and **we’re only 30K away!** If you like learning about AI, and already watch some of our videos, [do us a favor and click here to subscribe](https://www.youtube.com/@theneuronai?sub_confirmation=1&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-building-ai-voice-agents-w-livekit-s-ben-cherry) today. 

Stay curious,

Grant & Corey

| That’s all for today, for more AI treats, check out our [website](https://www.theneuron.ai/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-live-now-building-ai-voice-agents-w-livekit-s-ben-cherry).   
---|---  
  
**P.P.S:** Love the newsletter, but don’t want to receive these podcast announcement emails? Don’t unsubscribe — _[adjust your preferences to opt out of them here instead](https://www.theneurondaily.com/subscribe/f5596641-9099-4045-9641-731cd9fdcf90/preferences?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-first-major-ai-incident-this-year-ceo-warns&_bhlid=1d073d4088b90ea4abf69ef7cc157e0659ada818)_ _._

---

## [😺 Meta used staff as AI training data. Then cut them.](https://www.theneurondaily.com/p/meta-used-staff-as-ai-training-data-then-cut-them)
*🧠 The Neuron | 2026-05-21*

[](https://cloudonair.withgoogle.com/events/startup-school-ai-q2-2026?utm_source=gfs&utm_medium=newsletter&utm_campaign=FY26-Q2-GLOBAL-GCP40434-onlineevent-er-Q2StartupSchool-180015&utm_content=neuron1)

Welcome, humans. 

Voice agents are having their moment. Every demo looks clean, every pitch sounds effortless, and everyone is very confident their AI will just...work. So naturally, we decided to do a live demo.

This Thursday we're hosting a livestream with Ben Cherry of LiveKit, the open-source platform behind a lot of the voice, video, and physical AI agents actually shipping in production today.

[](https://www.youtube.com/live/kdzmBBqMyJ0?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=meta-used-staff-as-ai-training-data-then-cut-them)

We're going deep on what it really takes to build a voice agent that can listen, respond, interrupt, call tools, and not fall apart the moment a real user says something unexpected. Then we'll build one live, on stream, together. There is at least a small chance the agent talks back at exactly the wrong time. We're told this is a feature.

See you at 10AM PT | 12PM CT | 1PM ET on [YouTube](https://www.youtube.com/live/kdzmBBqMyJ0?si=56zLwdUXprlbwRBy&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=meta-used-staff-as-ai-training-data-then-cut-them) or [LinkedIn](https://www.linkedin.com/posts/ai-voiceai-aiagents-ugcPost-7462586957739712512-VN-e?utm_source=share&utm_medium=member_desktop&rcm=ACoAADCyMTQB-NeAXR86sPrvHQS0-5lLKuOnusk).

**Here’s what happened in AI today:**

  * 😹 Meta used its own employees' keystrokes to train AI, then laid off 8,000 of them.

  * 📰 OpenAI is filing for its IPO, targeting a September debut at an $852B valuation.

  * 📰 Grok launched Skills: teach it something once, it remembers forever.

  * 📰 The White House is requiring AI companies to share new models with the government 90 days before launch.

  * 📰 Airbnb added groceries, car hire, and boutique hotels. It's basically becoming a full travel OS.




**Hey:**_Want to reach 700,000+ AI-hungry readers?_[Advertise with us!](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)_[](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)_

**P.S:**_Love robots? We’re starting a new robotics newsletter!_[Sign up early here](https://form.jotform.com/260897013570156?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=meta-used-staff-as-ai-training-data-then-cut-them).

# 😺******Meta Used Its Employees as AI Training Data, Then Laid Them Off**

A leaked audio recording reveals Zuckerberg's real explanation for why Meta was tracking its workers.

You've heard of "learn by doing." Meta invented "learn by watching employees do it, then replace them."

A [leaked audio recording](https://www.moneycontrol.com/technology/mark-zukerberg-s-leaked-viral-audio-clip-suggest-meta-is-tracking-employees-to-train-ai-article-13924715.html?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=meta-used-staff-as-ai-training-data-then-cut-them) from a Meta all-hands meeting, obtained by More Perfect Union, captures Mark Zuckerberg explaining that Meta has been monitoring employee activity across Gmail, GChat, internal tool Metamate, and VSCode (the coding software most engineers use) to train its AI models. His reasoning: the AI "learns from watching really smart people do things," and elite engineers make better training subjects than outside contractors.

_Which is, in fairness, a solid training strategy. It's the "then lay them off" part that makes it weird._

**Here's how this unfolded:**

  * **April 21:**[ ](https://ca.finance.yahoo.com/news/exclusive-meta-start-capturing-employee-163229884.html?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=meta-used-staff-as-ai-training-data-then-cut-them)Meta announced that it was [installing keystroke and mouse-tracking software](https://ca.finance.yahoo.com/news/exclusive-meta-start-capturing-employee-163229884.html?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=meta-used-staff-as-ai-training-data-then-cut-them) on employee computers. Meta's public response was mild: the models just needed to learn how people click dropdown menus. Routine stuff.

  * **April 30:** At an internal all-hands, Zuckerberg gave a rather different explanation on tape. The AI learns from watching "really smart people." He also acknowledged the leak risk, telling staff it was "not strategically in your interest" to share details openly.

  * **May 19 (Monday):** [Meta announced it was reassigning 7,000 workers](https://www.nytimes.com/2026/05/18/technology/meta-reassigns-7000-employees-ai.html?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=meta-used-staff-as-ai-training-data-then-cut-them) to new AI-focused teams. Framed internally as a productivity upgrade.

  * **May 20 (Wednesday):**[ Roughly 8,000 employees](https://www.theweek.in/news/sci-tech/2026/05/20/leaked-meta-audio-clip-sparks-outrage-is-mark-zuckerberg-tracking-employees-to-fuel-ai-led-layoffs.html?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=meta-used-staff-as-ai-training-data-then-cut-them) received layoff notices, starting at 4am Singapore time. The leaked audio dropped the same day. Fliers opposing the tracking program appeared on office walls.




**Why this matters:** The gap between the public story ("we're just training models to use software") and the private one ("we're learning from watching our best people") is the whole story. Meta is hardly alone in collecting employee behavior data. It's just the company that got caught explaining the real logic on tape, right before laying off the people it was watching.

**Our take:** Meta will survive this. The more uncomfortable question is whether this becomes a template. Every company with a "productivity monitoring" program is now one leaked memo away from the same headline. The line between "helping you work better" and "training your replacement" just got a lot blurrier.

**FROM OUR PARTNERS**

[](https://cloudonair.withgoogle.com/events/startup-school-ai-q2-2026?utm_source=gfs&utm_medium=newsletter&utm_campaign=FY26-Q2-GLOBAL-GCP40434-onlineevent-er-Q2StartupSchool-180015&utm_content=neuron1)

Ready to move past novelty chatbots? [Google Cloud’s Startup School: Agentic AI](https://cloudonair.withgoogle.com/events/startup-school-ai-q2-2026?utm_source=gfs&utm_medium=newsletter&utm_campaign=FY26-Q2-GLOBAL-GCP40434-onlineevent-er-Q2StartupSchool-180015&utm_content=neuron1) covers the architecture you need to build robust, autonomous workflows.

Dive into Realtime Voice AI, enhanced Multimodal RAG, and bidirectional Vision Agents. Go from prototype to secure production without missing a beat.

[Save your spot](https://cloudonair.withgoogle.com/events/startup-school-ai-q2-2026?utm_source=gfs&utm_medium=newsletter&utm_campaign=FY26-Q2-GLOBAL-GCP40434-onlineevent-er-Q2StartupSchool-180015&utm_content=neuron1)

# 🎓 AI Skill of the Day: **Turn Claude Into Your Full-Time Content Team**

If you make content for a living (or want to),[ Modern Millie's 23-min tutorial](https://www.youtube.com/watch?v=xEyQub_fDjg&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=meta-used-staff-as-ai-training-data-then-cut-them) is worth every minute. Here are the four workflows that actually move the needle:

**1\. Free profile audit.** Install the Claude Chrome extension, open your Instagram or YouTube Studio analytics, then ask: _" Audit my profile. What's working, what isn't, and what's the single most important thing I should change right now?"_ Claude reads the live page and gives you a full breakdown — hook strength, content gaps, growth opportunities.

**2.****30-day content calendar in one prompt.** Inside a Claude Project loaded with your brand info, paste this:
    
    
    Based on everything you know about my brand and goals, 
    build me a 30-day content calendar. Alternate between 
    my content pillars and include 3 hook options per video.

**3\. Full video script from the calendar.** Pick a day you like, then:
    
    
    Let's work on Day [X]. Use Hook [#]. 
    Turn this into a full script with text hook, verbal hook, 
    visual hook, talking points, and CTA.

**4.****One video → one week of content.** Get your YouTube transcript from [transcript.io](https://transcript.io?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=meta-used-staff-as-ai-training-data-then-cut-them), start a new Project called "[Brand] YouTube to Everywhere," and paste: _" Here's my transcript. Turn this into a full week of content."_ Out comes short-form scripts, captions, carousel outlines, and an email newsletter — all from the video you already made.

**Total AI beginner?**[Start here](https://www.theneuron.ai/explainer-articles/everything-we-covered-in-our-ai-for-total-beginners-livestream-full-guide-with-timestamps/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=meta-used-staff-as-ai-training-data-then-cut-them) ([goes with this video](https://www.youtube.com/live/QbFU0UNMVaU?si=skJsgUIDjKjAx3DU&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=meta-used-staff-as-ai-training-data-then-cut-them)). 

**Have a specific skill you want to learn?** [Request it here.](https://docs.google.com/forms/d/e/1FAIpQLSd_-hSXtB9ytR1HQrU85IJnJw233bNKptiGB5BZh9maPse1Eg/viewform?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=meta-used-staff-as-ai-training-data-then-cut-them)

# 🍪 Treats to Try 

[](https://links.outskill.com/DBA?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=meta-used-staff-as-ai-training-data-then-cut-them)

_*Asterisk = from our partners (only the first one!).__[Advertise to 700K+ readers here](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=meta-used-staff-as-ai-training-data-then-cut-them)_ _!_

  1. The World’s first Claude-a-thon, A 2 day deep dive into Claude, its user-cases and 10+ other AI tools happening this weekend from 10 am-7pm EST. [Register NOW! (free for the next 48 hrs)](https://links.outskill.com/DBA?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=meta-used-staff-as-ai-training-data-then-cut-them)

  2. Dell Pro Max with GB10 helps teams turn AI ideas into pilots, demos, and workflows with NVIDIA Grace Blackwell power and 128GB memory. [See it here](https://www.dell.com/en-us/shop/desktop-computers/dell-pro-max-with-gb10/spd/dell-pro-max-fcm1253-micro/xcto_fcm1253_usx?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=meta-used-staff-as-ai-training-data-then-cut-them).

  3. [PollyReach](https://pollyreach.ai/?utm_source=theneuron) gives your agent a real phone number and sends it out to make calls (qualifying leads, booking appointments, or handling customer support) while you do literally anything else.

  4. [LandingHero AI](https://www.landinghero.ai/?utm_source=theneuron) adds a voice agent to your website that talks to visitors, answers product questions in 50+ languages, and captures leads with full transcripts; add it to any existing site with one line of code.

  5. [LobeHub](https://lobehub.com/?utm_source=theneuron) manages your entire agent team for you: assign a goal, it picks the right agents, runs them in parallel 24/7, and only contacts you when a decision actually needs a human. —free to try

  6. [NanoClaw](https://nanoclaw.dev/?utm_source=theneuron) is a sandboxed alternative to OpenClaw (a popular open-source AI coding agent) that runs in a container so your AI agent can't access your entire machine. It went viral,, turned down a $20M buyout, and raised $12M seed with the Hugging Face CEO as an angel.

  7. [Lance](https://github.com/bytedance/Lance?utm_source=theneuron) is ByteDance's open-source model that handles image generation, editing, video generation, and video understanding all in one framework. At 3B parameters, it benchmarks ahead of most 7B models at a fraction of the size.




# Featured: **The AI Trying to Solve Math’s Biggest Mystery w/ Tudor Achim of Aristotle**

[](https://youtu.be/8MNfLsi0aKY?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=meta-used-staff-as-ai-training-data-then-cut-them)

What happens when AI stops simply giving answers and starts producing proofs a computer can verify?

In this episode of _The Neuron_ , Corey Noles and Grant Harvey talk with Tudor Achim, Co-Founder and CEO of Harmonic, the company behind Aristotle — a formal reasoning system built to generate machine-checkable mathematical proofs. 

Tudor explains why math may be the clearest test case for moving AI from “trust me” to “check me,” and why formal verification could matter far beyond Olympiad benchmarks.

Special thanks to our sponsor [Dell & NVIDIA](https://www.techrepublic.com/hubs/the-enterprise-guide-to-scalable-ai/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=meta-used-staff-as-ai-training-data-then-cut-them) for making this one possible!

New episodes air **every week** on: [Spotify](https://open.spotify.com/show/4gF6uNmkzEYq2E0sHeuMuU?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=meta-used-staff-as-ai-training-data-then-cut-them) | [Apple Podcasts](https://podcasts.apple.com/us/podcast/the-neuron-ai-explained/id1742267001?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=meta-used-staff-as-ai-training-data-then-cut-them) | [YouTube](https://www.youtube.com/@theneuronai?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=meta-used-staff-as-ai-training-data-then-cut-them)****

# 📰 Around the Horn 

[](https://x.com/IntologyAI/status/2056764236668493868?s=20&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=meta-used-staff-as-ai-training-data-then-cut-them)

  * [The White House](https://www.theinformation.com/articles/white-house-briefs-ai-companies-plan-review-models-release?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=meta-used-staff-as-ai-training-data-then-cut-them) briefed OpenAI, Anthropic, and Reflection AI on a planned executive order that would let government agencies review advanced AI models up to 90 days before public release; Trump could sign as early as today, with cloud providers, chip companies, and banks also in the room.

  * [OpenAI](https://techcrunch.com/2026/05/20/openai-barrels-toward-ipo-that-may-happen-in-september/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=meta-used-staff-as-ai-training-data-then-cut-them) is preparing to confidentially file for an IPO as soon as this week, targeting a September debut at an $852B valuation, with Goldman Sachs and Morgan Stanley leading the deal, one day after Elon Musk lost his lawsuit trying to block the company's restructuring.

  * [SpaceX's public S-1 filing](https://www.engadget.com/2178212/the-spacex-ipo-plans-are-now-public/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=meta-used-staff-as-ai-training-data-then-cut-them) revealed Anthropic will pay SpaceX $1.25B per month through May 2029 for xAI data center access, and that X lost $595M in ad revenue in 2024 due to advertiser exits; IPO will trade as SPCX on Nasdaq.

  * [Grok](https://x.ai/news/grok-skills?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=meta-used-staff-as-ai-training-data-then-cut-them) launched Skills, a persistent memory feature that lets you teach Grok a formatting rule, workflow, or personal preference once, and it remembers it across every future conversation, no re-prompting needed.

  * [Google's Gemini](https://www.brightedge.com/news/press-releases/brightedge-data-gemini-second-largest-ai-referral-source-q1-2026?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=meta-used-staff-as-ai-training-data-then-cut-them) became the #2 AI referral source in Q1 2026, nearly tripling its share to 11.6% and now sending more web traffic than Perplexity, Claude, Meta AI, DeepSeek, and Grok combined; ChatGPT fell for the first time.

  * [Airbnb's summer release](https://news.airbnb.com/en-uk/2026-summer-release-now-theres-even-more-to-airbnb/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=meta-used-staff-as-ai-training-data-then-cut-them) added car hire, grocery delivery, airport pickups, boutique hotels, and AI-powered review summaries to the app, expanding the platform well beyond home rentals for the second year running.




**FROM OUR PARTNERS**

# Put the AI lab within reach

[](https://www.dell.com/en-us/shop/desktop-computers/dell-pro-max-with-gb10/spd/dell-pro-max-fcm1253-micro/xcto_fcm1253_usx?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=meta-used-staff-as-ai-training-data-then-cut-them)

For business owners and AI enthusiasts who want more than browser-based tinkering, [Dell Pro Max with GB10](https://www.dell.com/en-us/shop/desktop-computers/dell-pro-max-with-gb10/spd/dell-pro-max-fcm1253-micro/xcto_fcm1253_usx?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=meta-used-staff-as-ai-training-data-then-cut-them) brings NVIDIA GB10 Grace Blackwell power to a compact AI development desktop.

[Check out the Dell Pro Max with GB10.](https://www.dell.com/en-us/shop/desktop-computers/dell-pro-max-with-gb10/spd/dell-pro-max-fcm1253-micro/xcto_fcm1253_usx?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=meta-used-staff-as-ai-training-data-then-cut-them)

# 📖******Thursday Trivia**

**You know the drill: one is AI, and one is real. Which is which? Vote in the poll below!**

**A**.

**B.**

# A Cat’s Commentary 

**Trivia answer:**[A is AI](https://www.reddit.com/r/aivideo/comments/1tbv1m5/this_is_one_of_the_craziest_ai_video_ive_seen/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=meta-used-staff-as-ai-training-data-then-cut-them) and [B is real](https://www.keranews.org/2014-05-19/smooth-move-young-texas-rangers-fan-shares-baseball-to-impress-a-lady-video?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=meta-used-staff-as-ai-training-data-then-cut-them)!

| That’s all for now.   
---|---  
  
**P.S:** Before you go… have you [subscribed to our YouTube Channel](https://www.youtube.com/@theneuronai?sub_confirmation=1&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=meta-used-staff-as-ai-training-data-then-cut-them)? If not, can you? 

[](https://www.youtube.com/@theneuronai?sub_confirmation=1&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=meta-used-staff-as-ai-training-data-then-cut-them)

Click the image to subscribe! 

**P.P.S:** Love the newsletter, but only want to get it once per week? Don’t unsubscribe—[update your preferences here](https://www.theneurondaily.com/subscribe/f5596641-9099-4045-9641-731cd9fdcf90/preferences?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=meta-used-staff-as-ai-training-data-then-cut-them).

---

## [😺 🎙️ PODCAST: Can AI Solve Math's Biggest Mystery?](https://www.theneurondaily.com/p/podcast-can-ai-solve-math-s-biggest-mystery)
*🧠 The Neuron | 2026-05-20*

[](https://www.youtube.com/8MNfLsi0aKY?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)

[](https://www.techrepublic.com/hubs/the-enterprise-guide-to-scalable-ai/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)

Welcome, humans.

AI is getting better at math.

But [Tudor Achim](https://www.linkedin.com/in/tudorachim?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery) says the bigger shift is that AI may finally be able to prove what it says.

Tudor is the co-founder and CEO of [Harmonic](https://harmonic.fun/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery), the company behind [Aristotle](https://aristotle.harmonic.fun/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery), a formal reasoning system built to generate mathematical proofs that computers can actually verify.

That sounds abstract. But it could matter a lot.

Because if AI can move from “trust me, this is right” to “check me, this is right,” it could reshape math, software, chip design, scientific computing, and maybe even how humans discover new knowledge.

## **Today’s Episode is Sponsored by Dell Technologies and NVIDIA**

[](https://www.techrepublic.com/hubs/the-enterprise-guide-to-scalable-ai/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)

Plenty of companies can launch an AI pilot. Far fewer know how to make it stick. Explore this resource hub, sponsored by Dell AI Factory with NVIDIA, for strategies, decisions, and real-world lessons on turning AI into something scalable, useful, and worth the investment.

[**Learn More**](https://www.techrepublic.com/hubs/the-enterprise-guide-to-scalable-ai/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)

**In our latest episode, Corey and Grant sit down with Tudor Achim to unpack what “mathematical superintelligence” actually means:**

  * **[00:00](https://www.youtube.com/watch?v=8MNfLsi0aKY&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)** AI That Proves Its Work

  * **[02:00](https://www.youtube.com/watch?v=8MNfLsi0aKY&t=120s&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)** What Mathematical Superintelligence Means

  * **[03:22](https://www.youtube.com/watch?v=8MNfLsi0aKY&t=202s&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)** A Clearer Bar Than AGI

  * **[04:01](https://www.youtube.com/watch?v=8MNfLsi0aKY&t=241s&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)** Are Today’s AI Systems Actually Creative?

  * **[05:42](https://www.youtube.com/watch?v=8MNfLsi0aKY&t=342s&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)** Math Is Not Just Arithmetic

  * **[08:58](https://www.youtube.com/watch?v=8MNfLsi0aKY&t=538s&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)** How AI Amplifies Mathematicians

  * **[10:02](https://www.youtube.com/watch?v=8MNfLsi0aKY&t=602s&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)** Why Verification Makes AI Useful

  * **[11:45](https://www.youtube.com/watch?v=8MNfLsi0aKY&t=705s&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)** Lean, Explained Simply

  * **[12:15](https://www.youtube.com/watch?v=8MNfLsi0aKY&t=735s&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)** What a Machine-Checked Proof Means

  * **[12:42](https://www.youtube.com/watch?v=8MNfLsi0aKY&t=762s&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)** Could AI Prove Riemann by 2028?

  * **[15:24](https://www.youtube.com/watch?v=8MNfLsi0aKY&t=924s&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)** Why Harmonic Opened Aristotle to Users

  * **[17:33](https://www.youtube.com/watch?v=8MNfLsi0aKY&t=1053s&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)** Formal Math Becomes Practical

  * **[21:01](https://www.youtube.com/watch?v=8MNfLsi0aKY&t=1261s&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)** Human Proofs vs. Machine-Verified Proofs

  * **[23:11](https://www.youtube.com/watch?v=8MNfLsi0aKY&t=1391s&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)** GitHub for Mathematicians

  * **[24:44](https://www.youtube.com/watch?v=8MNfLsi0aKY&t=1484s&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)** Compute, Limits, and Infinite Math

  * **[27:29](https://www.youtube.com/watch?v=8MNfLsi0aKY&t=1649s&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)** The Moment That Changed Tudor’s View

  * **[29:10](https://www.youtube.com/watch?v=8MNfLsi0aKY&t=1750s&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)** Trust Layers Beyond Math

  * **[31:20](https://www.youtube.com/watch?v=8MNfLsi0aKY&t=1880s&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)** Tudor’s Aristotle “Aha” Moment

  * **[33:49](https://www.youtube.com/watch?v=8MNfLsi0aKY&t=2029s&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)** Should AI Change Education?

  * **[37:07](https://www.youtube.com/watch?v=8MNfLsi0aKY&t=2227s&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)** The Spec Problem in Verified Software

  * **[39:10](https://www.youtube.com/watch?v=8MNfLsi0aKY&t=2350s&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)** How Aristotle Could Help Chip Design

  * **[42:25](https://www.youtube.com/watch?v=8MNfLsi0aKY&t=2545s&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)** Will We Ever Run Out of Math Problems?

  * **[46:03](https://www.youtube.com/watch?v=8MNfLsi0aKY&t=2763s&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)** The Problem Tudor Wants Solved




**Bottom line:** The future may not be AI replacing mathematicians. It may be mathematicians directing much more powerful tools, and finally being able to verify the results.

**Listen now on**[YouTube](https://youtu.be/8MNfLsi0aKY?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery) | [Spotify](https://open.spotify.com/episode/13u26j30bPhpJ4Ke1d3N5I?si=nxIEp8QkSKGp7qahEHKXTg&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery) | [Apple Podcasts](https://podcasts.apple.com/us/podcast/the-ai-trying-to-solve-maths-biggest-mystery-w-tudor/id1742267001?i=1000768789039&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)

**Dive deeper with these resources:**

  * [Try Aristotle from Harmonic](https://harmonic.fun/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)

  * [Corey’s running list of solved mathematical](https://www.theneuron.ai/explainer-articles/from-erdos-to-axiom-the-open-problems-ai-has-actually-solved/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery) [problems](https://www.theneuron.ai/explainer-articles/from-erdos-to-axiom-the-open-problems-ai-has-actually-solved/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)

  * [Learn what mathematical superintelligence means](https://www.indexventures.com/perspectives/solving-the-ai-reasoning-gap-how-harmonic-is-building-mathematical-superintelligence/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)

  * Read about [Lean](https://lean-lang.org/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery) and [formal verification](https://en.wikipedia.org/wiki/Formal_verification?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)




[](https://www.youtube.com/@theneuronai?sub_confirmation=1&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)

We have a goal to hit **50K subscribers** by the end of the year (if not 100K), and **we’re only ~30K away!** If you like learning about AI, and already watch some of our videos, [do us a favor and click here to subscribe](https://www.youtube.com/@theneuronai?sub_confirmation=1&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery) today. 

Stay curious,

The Neuron Team  
Corey & Grant

**FROM OUR PARTNER**

Are you hitting the limits of **siloed AI?** Just as humans once transformed society by sharing intent, knowledge, and innovation, AI faces a similar inflection point. To achieve distributed superintelligence, we must move beyond scaling up. We need to scale out, too.  
  
**Outshift by Cisco** is building the **Internet of Cognition** : an open infrastructure enabling agents and humans to collaborate in real time.

[Visit ](https://outshift.cisco.com/?utm_campaign=fy26q3_outshift_ww_paid-media_ioc-neuronai-outshift_podcast&utm_channel=podcast&utm_source=podcast)[Outshift.com](https://Outshift.com?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)

# 🎙️ In Case You Missed It… 

Four recent interviews you’ll definitely want to check out _(pick whatever looks interesting to you and dive in!):_

### 1\. Interested in whether AI can actually design new drugs? Watch: **[Isomorphic Labs Is Trying to Turn AlphaFold Into Medicine. Here’s How.](https://youtu.be/W0NSk2y3OFI?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)**

[](https://youtu.be/W0NSk2y3OFI?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)

**TL;DW:** Rebecca Paul, Head of Medicinal Drug Design at [Isomorphic Labs](https://www.isomorphiclabs.com/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery), and Michael Schaarschmidt, Foundational AI Research Lead, explain why drug discovery is still brutally slow, expensive, and failure-prone and how foundation models could help scientists design better drug candidates faster. Their big point: “AI-designed drugs” are not one magic model. It takes many models working together across biology, chemistry, structure prediction, molecule generation, and human judgment.

**Why you should watch:** If you’ve ever wondered what comes _after_ [AlphaFold](https://deepmind.google/science/alphafold/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery), this one gets into it. There’s a great section on how something that once could take an entire PhD to validate experimentally can now sometimes be predicted in seconds or minutes, and a wild bit about the dream of getting from a protein target to a drug candidate in one design cycle. Also: “undruggable” proteins may not stay undruggable forever.

  * **YouTube:** [Watch Here](https://youtu.be/W0NSk2y3OFI?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)

  * **Spotify:** [Listen Here](https://open.spotify.com/episode/2TzHhOkVIN9AL3GXXxSyDe?si=c5dd0a8104ec4805&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)

  * **Apple Podcasts:** [Listen Here](https://podcasts.apple.com/us/podcast/can-ai-really-design-new-drugs-google-deepmind-spin/id1742267001?i=1000766512015&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)




### 2\. Interested in what's missing before we hit AGI? Watch: [This Company Mapped the Entire World in 3D. Here's Why.](https://youtu.be/erCV1MJXU3g?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)

[](https://youtu.be/erCV1MJXU3g?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)

**TL;DW:** Peter Wilczynski, CPO at [Vantor](https://vantor.com/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery) (formerly Maxar), built a 3D model of the entire Earth at 50cm resolution and made it machine-readable. He argues spatial intelligence is the gap nobody's talking about in AI, and probably the missing piece before agents can actually operate in the physical world.

**Why you should watch:** If you've ever wondered why AI can write code and solve math olympiad problems but still can't reliably tell a drone where to go, this one answers it. Also, there's a wild bit about how the physical world becomes the new navigation layer for AI agents.

  * **YouTube:** [Watch Here](https://youtu.be/erCV1MJXU3g?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)

  * **Spotify:** [Listen Here](https://open.spotify.com/episode/71rhDuYFzTlsF0uaIq91QU?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)

  * **Apple Podcasts:** [Listen Here](https://podcasts.apple.com/us/podcast/this-company-mapped-the-entire-world-in-3d-heres-why/id1742267001?i=1000761587268&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)




### **3\. Curious how good AI music tools have actually gotten? Watch:****[This AI Just Made Our Podcast Theme Song](https://youtu.be/r4aMWjhoMHU?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)**

[](https://youtu.be/vJD2FjVUEhg?si=Mdm2w9GHHSZwZ2A8&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)

**TL;DW:** Corey sits down with **Kendall Rankin** , who left LinkedIn in 2024 to join [Producer AI](https://www.flowmusic.app/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery) when it was a startup (advised by The Chainsmokers, no less). Google acquired the team in February 2026, and Kendall is now on the Flow Music team inside Google Labs. On the episode, they generate a garage rock song from a single sentence, build a custom synth in the "Spaces" feature, and walk through SynthID watermarking and one-shot music videos.

**Why you should watch:** Most AI music demos hand you a polished finished song and skip the part where things go sideways. This episode is the part where things go sideways. First pass fumbles, Corey asks for "more fuzz," second pass actually lands. That iteration loop is the whole story for anyone trying to figure out if these tools are actually usable.

  * **YouTube:** [Watch Here](https://youtu.be/r4aMWjhoMHU?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)

  * **Spotify:** [Listen Here](https://open.spotify.com/show/4gF6uNmkzEYq2E0sHeuMuU?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)

  * **Apple Podcasts:** [Listen Here](https://podcasts.apple.com/us/podcast/the-neuron-ai-explained/id1742267001?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery)




**Last thing:** And if you **haven’t subscribed yet, please do!** Click the image below to go to our channel and hit “subscribe” to get notified right when new videos go live. 

| That’s all for today, for more AI treats, check out our [website](https://www.theneuron.ai/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery). **ICYMI: check out our most recent episodes below!**

  * _WTF is “AI Safety” and should we be scared?_([Youtube](https://youtu.be/LgslnEmon60?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery), [Apple](https://podcasts.apple.com/us/podcast/panic-or-progress-reading-between-the-lines-of-ai/id1742267001?i=1000714587441&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery), [Spotify](https://open.spotify.com/episode/6CZMZHDsKf32sFk3jGcgUv?si=4e650cc261394e76&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery))
  * _What happens to white collars jobs when AI gets even better?_ ([Youtube](https://youtu.be/WveigPtq5j4?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery), [Apple](https://podcasts.apple.com/us/podcast/microsoft-shares-its-playbook-for-surviving-the-ai/id1742267001?i=1000713364838&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery), [Spotify](https://open.spotify.com/episode/7fy7Che9Xz5WN6OeRH5XlR?si=321ef98a123c4b6c&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-can-ai-solve-math-s-biggest-mystery))

  
---|---

---

## [😺 Google just put agents in everything](https://www.theneurondaily.com/p/google-just-put-agents-in-everything)
*🧠 The Neuron | 2026-05-20*

[](https://www.atlassian.com/whitepapers/ai-native-service?utm_source=newsletter-email&utm_medium=email&utm_campaign=P:jira-service-management*O:clm*F:awareness*C:wpaper*H:fy26q4*Y:itsm*E:cloud*&utm_sfdc-campaign_id=701QB00000ihbcYYAQ)  
  
Welcome, humans. 

It’s official: the legendary AI researcher (former OpenAI, former Tesla) and arguably the industry’s biggest influencer, Andrej Karpathy (he coined the term “vibe coding”), has [chosen a side and joined Anthropic](https://x.com/karpathy/status/2056753169888334312?s=20&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-just-put-agents-in-everything) and is now heading back to frontier R&D.

This makes sense if you’ve been paying attention; it’s not like he’s going to join OpenAI (_he already left)_ , and he’s too independent for Google or Microsoft. That, and by every measure it appears Anthropic is ahead in the big lab model race. _If you’re gonna play… why not play for keeps?_

There were so many good memes about this, including translating it for non-AI folks as the equivalent of Ronaldo joining Manchester United, the obligatory “[what did Karpathy see?](https://x.com/danshipper/status/2056762096352649421?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-just-put-agents-in-everything)” _(nice one Dan)_ and this one (_which transitions perfectly into our main story of the day; thanks Trung!):_

[](https://x.com/TrungTPhan/status/2056792344230531500?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-just-put-agents-in-everything)

We need the alt version of this where Sundar Pichai is face-swapped onto the [George W Bush meme that ppl usually use to punish Dario](https://x.com/shiri_shh/status/2051675614332289410?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-just-put-agents-in-everything)

**Here’s what happened in AI today:**

  * 😼 Google put Gemini agents across Search, Workspace, and Android.

  * 📰 OpenAI added provenance tools for AI-generated images.

  * 📰 Anthropic brought Claude to KPMG's 276,000 workers.

  * 🍪 Google AI Studio now builds native Android apps.

  * 📖 The post-transformer debate asks what AI stores away.




…[and a ](https://theneuron.ai/explainer-articles/everything-that-happened-in-ai-today-tuesday-may-19-2026/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-just-put-agents-in-everything)[**whole lot more that you can read about here**](https://theneuron.ai/explainer-articles/everything-that-happened-in-ai-today-tuesday-may-19-2026/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-just-put-agents-in-everything)

**Hey:**_Want to reach 700,000+ AI-hungry readers?_[Advertise with us!](https://solutions.technologyadvice.com/lp/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-just-put-agents-in-everything)[__](https://solutions.technologyadvice.com/lp/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-just-put-agents-in-everything)

**P.S:**_Love robots? We’re starting a new robotics newsletter!_[Sign up early here](https://form.jotform.com/260897013570156?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-just-put-agents-in-everything).

# 😺 Google Put Gemini Agents Everywhere at I/O

Sir Demis Hassabis using a mirror selfie to showcase Google Omni was not on my Bingo card this year… 

[DEEP DIVE: Everything Google announced at I/O 2026](https://www.theneuron.ai/explainer-articles/google-io-2026-was-about-turning-every-google-app-into-an-agent/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-just-put-agents-in-everything)

Google held its [annual I/O conference](https://io.google/2026/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-just-put-agents-in-everything) yesterday, and they used it to make one thing clear: Gemini is becoming the layer underneath all of the apps people already use… _whether they like it or not._

**Here’s what happened, in brief (read the deep dive for everything):**

  * [Gemini 3.5 Flash](https://blog.google/innovation-and-ai/models-and-research/gemini-models/gemini-3-5/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-just-put-agents-in-everything) became Google’s new fast model for agents, coding, and long tasks.

  * [Gemini Spark](https://blog.google/innovation-and-ai/products/gemini-app/next-evolution-gemini-app/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-just-put-agents-in-everything) introduced itself as a 24/7 personal agent that can work across Workspace apps.

  * [Search](https://blog.google/products-and-platforms/products/search/search-io-2026/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-just-put-agents-in-everything) got information agents that monitor the web, plus mini apps for ongoing tasks.

  * [Workspace](https://blog.google/products-and-platforms/products/workspace/workspace-updates/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-just-put-agents-in-everything) got voice features for Gmail, Docs, and Keep, plus Google Pics and AI Inbox.

  * [Antigravity 2.0](https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-just-put-agents-in-everything) turned coding agents into a managed desktop, CLI, and SDK workflow, plus the ability to launch a team of parallel coding agents.

  * [AI Studio](https://blog.google/innovation-and-ai/technology/developers-tools/google-ai-studio-io-2026/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-just-put-agents-in-everything) now lets you generate full Android apps.




_…and a whole lot more than that you can read about in our deep dive._

**Why this matters:** The real story, though, was pretty simple: Google wants Gemini to stop feeling like a chatbot and start feeling like the operating layer across search, email, docs, shopping, video, glasses, coding, and app building.  _At some point, the assistant stopped being shoehorned into the apps and will now become the plumbing beneath it._

This matters for Google because the AI race has drifted away from “which chatbot answers best?” and toward “which company can turn answers into action?” Google’s answer is obvious: put Gemini inside everything, from Search, Gmail, Docs, YouTube, shopping, Android, coding, app building, and glasses.

**Our take:** Google has the distribution advantage, to be sure. ChatGPT and Claude are destination apps. Meanwhile, Google owns the end work surfaces: inbox, docs, browser, phone, YouTube, Search, shopping, and the developer stack. _All the endpoints where the work you do with the AI in the middle actually touches the rest of the world._

That means Google can make agents feel less like a new habit and more like a new setting inside the tools you already open all day. _If it works well, it will feel like your tools just getting better._

The hard part now is permission. A search engine that answers is useful. A search engine that monitors, books, shops, builds, writes, and edits needs trust.

If Google gets that right, the next AI interface may feel less like opening a chatbot and more like telling your computer what outcome you want. _Which is how AI SHOULD work._

**FROM OUR PARTNERS**

# Is your service strategy ready for the AI era?

[](https://www.atlassian.com/whitepapers/ai-native-service?utm_source=newsletter-email&utm_medium=email&utm_campaign=P:jira-service-management*O:clm*F:awareness*C:wpaper*H:fy26q4*Y:itsm*E:cloud*&utm_sfdc-campaign_id=701QB00000ihbcYYAQ)

The old service management playbook — endless tickets, manual triaging, and bolt-on chatbots — can't keep up in the age of AI. [Atlassian's](https://www.atlassian.com/whitepapers/ai-native-service?utm_source=newsletter-email&utm_medium=email&utm_campaign=P:jira-service-management*O:clm*F:awareness*C:wpaper*H:fy26q4*Y:itsm*E:cloud*&utm_sfdc-campaign_id=701QB00000ihbcYYAQ) new white paper outlines a bold, AI-native approach to service that shifts teams from reactive to proactive, turns rich context into a competitive advantage, and puts human-AI collaboration at the center of every interaction. If you're rethinking how your organization delivers service in the AI era, this is worth the read.

[Learn More](https://www.atlassian.com/whitepapers/ai-native-service?utm_source=newsletter-email&utm_medium=email&utm_campaign=P:jira-service-management*O:clm*F:awareness*C:wpaper*H:fy26q4*Y:itsm*E:cloud*&utm_sfdc-campaign_id=701QB00000ihbcYYAQ)

# 🎓 AI Skill of the Day: Use Gemini Like a Task Router to Help Best Use Gemini

Google now has Gemini everywhere. So the skill today: make Gemini pick the right surface before you start. Google’s own prompt guide says Gemini works best with direct, structured instructions, so give it a routing job first.
    
    
    I want to use Gemini for this task: [task].
    
    Route me to the best Google tool, then give me:
    1. The safest first prompt
    2. The files or inputs to attach
    3. What should stay read-only
    4. What success looks like
    5. One follow-up prompt
    

Good rule of thumb: Start with reversible tasks: monitor, draft, compare, storyboard, or prototype before you let an agent send, buy, delete, or publish.

**Have a specific skill you want to learn?** [Request it here.](https://docs.google.com/forms/d/e/1FAIpQLSd_-hSXtB9ytR1HQrU85IJnJw233bNKptiGB5BZh9maPse1Eg/viewform?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-just-put-agents-in-everything)

# 🍪 Treats to Try 

[](https://deal.incogni.io/aff_c?offer_id=6&aff_id=1011&url_id=1&source=0520&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-just-put-agents-in-everything)

_*Asterisk = from our partners (only the first one!)._[_Advertise to 700K+ readers here_](https://solutions.technologyadvice.com/lp/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-just-put-agents-in-everything) _!_

  1. *[Incogni](https://incogni.com/deal/special?transaction_id=102d6e357fcba553dd69d460e4b2fe&offer_id=6&affiliate_id=1011&source=0520&aff_sub=&utm_source=Affiliates&utm_medium=1011icg&utm_campaign=affiliate&utm_content=6) \- remove your personal data from the web so scammers and identity thieves can’t access it. Use code [NEURON](https://incogni.com/deal/special?transaction_id=102d6e357fcba553dd69d460e4b2fe&offer_id=6&affiliate_id=1011&source=0520&aff_sub=&utm_source=Affiliates&utm_medium=1011icg&utm_campaign=affiliate&utm_content=6) to get 55% off.

  2. [Google AI Studio](https://blog.google/innovation-and-ai/technology/developers-tools/google-ai-studio-io-2026/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-just-put-agents-in-everything) now builds native Android apps from prompts and lets you pull in Workspace data; _this is sick._

  3. [Stitch](https://blog.google/innovation-and-ai/models-and-research/google-labs/stitch-updates/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-just-put-agents-in-everything) turns text, voice, code, or design files into app interfaces you can steer in real time, available globally today.

  4. [Antigravity 2.0](https://blog.google/innovation-and-ai/technology/developers-tools/google-io-2026-developer-highlights/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-just-put-agents-in-everything) orchestrates parallel coding agents, background tasks, CLI workflows, and SDK access, included in Google AI plans.

  5. [Gemini Spark](https://blog.google/innovation-and-ai/products/gemini-app/next-evolution-gemini-app/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-just-put-agents-in-everything) handles proactive tasks across Google products under your direction, rolling to trusted testers first and U.S. AI Ultra users next week.

  6. [Carbon](https://huggingface.co/spaces/HuggingFaceBio/carbon-demo?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-just-put-agents-in-everything) processes DNA sequences so you can continue sequences, score mutations, and visualize proteins, available as a free demo.

  7. [Google Pics](https://blog.google/products-and-platforms/products/workspace/workspace-updates/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-just-put-agents-in-everything) edits image objects, text, and Workspace visuals with precise controls, launching to Trusted Testers first and Pro / Ultra users this summer.




# NEW from The Neuron: Our Recap of the Great Post Transformer Debate

[](https://youtu.be/hCjoMLuCuLQ?si=zlvDE5SaS5oP66eh&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-just-put-agents-in-everything)

Our [most popular podcast interview](https://youtu.be/duw7RUif8hE?si=sH49HG1CCom3iHqH&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-just-put-agents-in-everything) to date on _The Neuron AI Explained_ was with Zuzanna Stamirowska, CEO of [Pathway](https://pathway.com/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-just-put-agents-in-everything) and whose company invented one of the most credible “post transformer” model architectures to date ([called BDH](https://arxiv.org/abs/2509.26507?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-just-put-agents-in-everything)). So when Pathway hosted an entertaining boxing-themed debate between the transformer and so-called post-transformer models, you know we had to tune in and see what’s up.

Check out the video above, or read our [recap of the debate here](https://theneuron.ai/explainer-articles/what-the-transformer-vs-post-transformer-debate-revealed-about-ais-next-architecture/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-just-put-agents-in-everything). 

# 📰 Around the Horn 

[](https://x.com/shlomifruchter/status/2056809488137756723?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-just-put-agents-in-everything)

This omni model is p good, sir’s and madame’s!

  * [OpenAI](https://openai.com/index/advancing-content-provenance/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-just-put-agents-in-everything) added C2PA conformance, SynthID watermarking, and an early public verifier for OpenAI-generated images.

  * [Anthropic and KPMG](https://www.anthropic.com/news/anthropic-kpmg?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-just-put-agents-in-everything) announced a Claude rollout for KPMG's 276,000+ employees and client-facing Digital Gateway platform.

  * [The European Commission](https://iapp.org/news/a/european-commission-delivers-draft-high-risk-ai-guidelines-after-delays?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-just-put-agents-in-everything) released draft high-risk AI Act guidance and opened consultation through June 23.

  * [Greg Brockman](https://x.com/gdb/status/2056863925791293675?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-just-put-agents-in-everything) described Guaranteed Capacity as discounted token availability for 1-3 year enterprise commitments.

  * [Claude Managed Agents](https://venturebeat.com/orchestration/claude-agents-can-finally-connect-to-enterprise-apis-without-leaking-credentials?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-just-put-agents-in-everything) added self-hosted sandboxes and MCP tunnels for safer enterprise API connections.

  * [Google DeepMind](https://deepmind.google/blog/co-scientist-a-multi-agent-ai-partner-to-accelerate-research/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-just-put-agents-in-everything) published Co-Scientist in Nature, showing a multi-agent research system that generated and lab-tested biomedical hypotheses.

  * [Standard Chartered](https://www.reuters.com/business/world-at-work/stanchart-cut-more-than-7000-jobs-bank-steps-up-ai-adoption-2026-05-19/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-just-put-agents-in-everything) said it would cut 7,000+ jobs over four years while using AI to replace “lower-value human capital.”

  * [A new Shai-Hulud wave](https://www.bleepingcomputer.com/news/security/new-shai-hulud-malware-wave-compromises-600-npm-packages/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-just-put-agents-in-everything) reportedly compromised 600+ npm packages and targeted developer secrets across package pipelines.




**FROM OUR PARTNERS**

[](https://fandf.co/491OL3A?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-just-put-agents-in-everything)

Build durable AI agents and workflows in TypeScript. [Trigger.dev](https://fandf.co/491OL3A?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-just-put-agents-in-everything) provides the orchestration for long-running tasks with zero timeouts, automatic retries, and deep observability. From streaming LLM responses to custom build extensions, get the control you need without the ops overhead.

[Focus on your logic and deploy reliable agents that scale on demand.](https://fandf.co/491OL3A?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-just-put-agents-in-everything)

# 📖 Midweek Wisdom

  * [The Anti-AI Trap](https://doomscrollingbabel.manoel.xyz/p/the-anti-ai-trap?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-just-put-agents-in-everything) \- Manoel Horta Ribeiro argues that dismissing AI as pure hype can be as lazy as believing every vendor demo.

  * [François Chollet on agent memory](https://x.com/fchollet/status/2056777649880752160?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-just-put-agents-in-everything) \- Chollet’s point is simple and useful: real tasks depend on what happened before, so agents need faithful long-term trajectory memory.

  * [AI will change the world without taking it over](https://windowsontheory.org/2022/11/22/ai-will-change-the-world-but-wont-take-it-over-by-playing-3-dimensional-chess/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-just-put-agents-in-everything) \- Boaz Barak and Ben Edelman offer a useful antidote to “AI plays 3D chess” stories.




# A Cat’s Commentary 

| That’s all for now.   
---|---  
  
**P.P.S:** Love the newsletter, but only want to get it once per week? Don’t unsubscribe—[update your preferences here](https://www.theneurondaily.com/subscribe/f5596641-9099-4045-9641-731cd9fdcf90/preferences?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-just-put-agents-in-everything).

---

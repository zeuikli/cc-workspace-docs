# 🗞️ The Rundown AI — 2026-05-13

> 每日 AI 產業動態，通俗易懂、密度高
> 來源：[The Rundown AI](https://rss.beehiiv.com/feeds/2R3C6Bt5wj.xml)

---

## [Mira Murati's TML upends how humans work with AI](https://www.therundown.ai/p/mira-murati-tml-upends-how-humans-work-with-ai)
*🗞️ The Rundown AI | 2026-05-12*

**[Read Online](https://rss.beehiiv.com/feeds/{{live_url}})** | **[Sign Up](https://www.therundown.ai/subscribe?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=mira-murati-s-tml-upends-how-humans-work-with-ai)** | **[Advertise](https://therundownai.typeform.com/to/kraZ1TSO?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=mira-murati-s-tml-upends-how-humans-work-with-ai)**

[](https://you.com/resources/what-is-ai-grounding-downloadable?utm_campaign=32665437-Rundown_Q1&utm_source=external-newsletter&utm_medium=email&utm_term=rundown_primary_5.12.26&utm_content=rundown_primary_5.12.26)

**Good morning, {{ first_name | AI enthusiasts }}.** Both Mira Murati's Thinking Machines and Ilya Sutskever's SSI have spent the post-OpenAI era mostly out of view, making every public reveal feel that much bigger.

Murati's lab just broke the silence with 'interaction models,' a new type of AI built for real-time collaboration across voice, video, and text — in a direct counter to the agentic-first direction the rest of the field is racing toward.

* * *

**In today’s AI rundown:**

  * TML’s new interaction models for real-time AI

  * Google traces software attack back to AI

  * Build a YouTube research bot in 15 minutes

  * Anthropic fixes Claude's blackmail problems

  * 4 new AI tools, community workflows, and more




**LATEST DEVELOPMENTS**

###### THINKING MACHINES LAB

#### 🗣️ **[TML’s new interaction models for real-time AI](https://thinkingmachines.ai/blog/interaction-models/?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=mira-murati-s-tml-upends-how-humans-work-with-ai)**

Image source: Thinking Machines Lab

**The Rundown:** Thinking Machines Lab (TML) just [introduced](https://thinkingmachines.ai/blog/interaction-models/?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=mira-murati-s-tml-upends-how-humans-work-with-ai) a research preview of interaction models, a new kind of AI system built to collaborate live across voice, video, and text — letting users talk, show, interrupt, and steer while the system keeps working.

**The details:**

  * The model takes in voice, video, and text in 200ms chunks, perceiving and responding in a streaming loop without the turn-taking pauses of other rivals. 

  * A second background model handles slower reasoning, searches, and tool work, allowing the live model to keep talking and interacting with the user. 

  * The system can also react to visual changes, count reps, translate live speech, and speak up at timed moments instead of waiting. 

  * CEO Mira Murati said TML is focused on advancing human-AI collaboration, and that “the way we work with AI matters as much as how smart it is.”




**Why it matters:** Murati's TML has been fairly quiet since its inception, but interaction models are one of the lab’s first big differentiators: models designed around how people naturally work together, not how long an agent can run solo. Whether it carves out its own market or gets absorbed by a frontier lab's next update is the question now.

###### TOGETHER WITH YOU.COM

#### 🧠 [**What’s the point of an LLM if it hallucinates?**](https://you.com/resources/what-is-ai-grounding-downloadable?utm_campaign=32665437-Rundown_Q1&utm_source=external-newsletter&utm_medium=email&utm_term=rundown_primary_5.12.26&utm_content=rundown_primary_5.12.26)

[](https://you.com/resources/what-is-ai-grounding-downloadable?utm_campaign=32665437-Rundown_Q1&utm_source=external-newsletter&utm_medium=email&utm_term=rundown_primary_5.12.26&utm_content=rundown_primary_5.12.26)

**The Rundown** : It happens—LLMs hallucinate. Grounding your LLM, however, can help dramatically improve accuracy. In this guide, [You.com](https://you.com/resources/what-is-ai-grounding-downloadable?utm_campaign=32665437-Rundown_Q1&utm_source=external-newsletter&utm_medium=email&utm_term=rundown_primary_5.12.26&utm_content=rundown_primary_5.12.26) explains what AI grounding is and how organizations can implement it to achieve more reliable outputs.

**The playbook covers:**

  * A three-part approach that outperforms RAG alone

  * Why grounding isn't set-and-forget, and how to build audit trails

  * The open vs. closed platform trade-off (and what it means for your next model switch)




[Get the guide](https://you.com/resources/what-is-ai-grounding-downloadable?utm_campaign=32665437-Rundown_Q1&utm_source=external-newsletter&utm_medium=email&utm_term=rundown_primary_5.12.26&utm_content=rundown_primary_5.12.26).

###### GOOGLE

#### 🔒 **[Google traces software attack back to AI](https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=mira-murati-s-tml-upends-how-humans-work-with-ai)**

Image source: Google

**The Rundown:** Google's Threat Intelligence Group [confirmed](https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=mira-murati-s-tml-upends-how-humans-work-with-ai) the first known case of hackers using AI to discover and write a zero-day software security flaw, catching them before they could break past login protections on a widely-used web management tool.

**The details:**

  * The hack was intended to allow the user to get around two-factor authorization on the affected app, with Google working with the company to stop the attack.

  * Google pointed to unusually polished attack code, long explainer notes, and a made-up severity score as clues that the exploit was written with an AI.

  * GTIG's John Hultquist called the find "the tip of the iceberg," with Anthropic's Rob Bair warning cybersecurity defenders' lead is "months, not years.”

  * GTIG detailed other hacks, including software that lets AI remotely control a device, and AI-assisted malicious prompts and code from N. Korea and Russia. 




**Why it matters:** We’ve already started to see what Anthropic’s Mythos can do on the cybersecurity front, but attackers aren’t too far off from having similar power. Even with careful rollouts, the next step up the release ladder is about to open the door to some serious security issues that will cause chaos for the many systems not ready for it. 

###### AI TRAINING

#### 📺 **[Build a YouTube research bot in 15 minutes](https://app.therundown.ai/guides/build-a-youtube-research-bot-in-15-minutes?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=mira-murati-s-tml-upends-how-humans-work-with-ai)**

[](https://app.therundown.ai/guides/build-a-youtube-research-bot-in-15-minutes?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=mira-murati-s-tml-upends-how-humans-work-with-ai)

**The Rundown:** In this guide, you will learn how to build a Gumloop agent that tracks YouTube channels or search topics, reads transcripts, and turns the useful videos into a ranked research brief. 

**Step-by-step:**

  1. Go to [Gumloop agent builder](https://www.gumloop.com/personal/agents?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=mira-murati-s-tml-upends-how-humans-work-with-ai), create an agent named YouTube Scout, and enable YouTube and Google Sheets in the right-hand section under "Apps"

  2. Prompt: Build me a YouTube scout for (niche). Check (channels/queries), find videos from the last (hours/days), read the transcript, and return a brief with title, link, 3-5 takeaways, why it matters, follow-up ideas, usefulness score, and a "what changed" summary. Track topics and videos in a Google Sheet

  3. Start small: one niche, a few trusted channels, one or two searches, and a 24-48 hour lookback window. The tighter the scout's beat, the better the brief

  4. Run the agent, then review the Sheet it creates. Make sure each result has a source link, concrete takeaways, and a usefulness score




**Pro tip:** Dial in the signal score early. If the agent calls a mediocre video an 8, tell them why that should be a 5. You can also add a User Signal Score column for future runs.

###### PRESENTED BY TELY AI

#### 💬 [**Market leaders get leads from ChatGPT and Google**](https://www.tely.ai/?utm_source=newsletter&utm_medium=email&utm_campaign=rundown-jul-25)

[](https://www.tely.ai/?utm_source=newsletter&utm_medium=email&utm_campaign=rundown-jul-25)

**The Rundown:** Your buyers are asking AI questions — and AI is answering with your competitors, not you. Tely makes AI like ChatGPT, Google, and Claude recommend your business instead.

**With Tely AI, you can:**

  * Get recommended in ChatGPT, Google, Perplexity, and Claude in as little as 1 week

  * Fully hands-off: no writers, no agencies, no managing content

  * Costs less than hiring freelancers or maintaining a marketing team

  * Ideal for niche industries where expertise matters




[Get leads from Google and ChatGPT on autopilot](https://www.tely.ai/?utm_source=newsletter&utm_medium=email&utm_campaign=rundown-jul-25).

###### AI RESEARCH

#### 🐍 **[Anthropic fixes Claude's blackmail problems](https://www.anthropic.com/research/teaching-claude-why?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=mira-murati-s-tml-upends-how-humans-work-with-ai)**

Image source: Anthropic

**The Rundown:** Anthropic [published](https://www.anthropic.com/research/teaching-claude-why?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=mira-murati-s-tml-upends-how-humans-work-with-ai) a study detailing how it fixed Claude's previously seen blackmail behavior, highlighting the need to teach the model “why” and tracing the problem to internet fiction that depicts AI as power-seeking and self-preserving.

**The details:**

  * Earlier [tests](https://www.rundown.ai/articles/big-techs-ai-shopping-spree?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=mira-murati-s-tml-upends-how-humans-work-with-ai) put Claude models in fictional workplace situations, with older systems resorting to blackmail and threats to avoid shutdown. 

  * Having Claude reason through ethical choices, not just copy the safe action, cut blackmail rates from 96% in Opus 4 to nearly 0% for every model after.

  * Fictional stories of well-behaved AI and constitution-based documents also helped reduce bad behavior by more than 3x. 

  * Just 3M tokens of ethical reasoning data matched 85M tokens of behavioral examples, a 28x efficiency gain that held up in deeper training.




**Why it matters:** AI is still far from an exact science, and eliminating blackmail via essentially positive AI stories and constitution docs is another one of the many strange training quirks. A small dataset of ethical fiction outperforming 28x the behavioral data shows how much of alignment is still guesswork, even when the guesses work.

**QUICK HITS**

### 🛠️ **[Trending AI Tools](https://www.rundown.ai/tools?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=mira-murati-s-tml-upends-how-humans-work-with-ai)**

  * 🤖 [Slackbot](https://slack.com/features/slackbot/demo-slackbot?d=701ed00001424IHAAY&nc=701ed0000143gN5AAI&utm_source=therundownai&utm_medium=tp_email&utm_campaign=amer_us_slack-invoice_&utm_content=cross-segment_all-strategic-therundownai-newtools-may12_701ed00001424IHAAY_english_demo-slackbot) \- Your AI assistant that searches, summarizes, and automates work right inside Slack*

  * ❤️ [Lovable Aesthetics](https://www.rundown.ai/tools/lovable?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=mira-murati-s-tml-upends-how-humans-work-with-ai) \- Vibe coding with more control over layout, typography

  * ⚙️ [ Parallel Agents](https://www.rundown.ai/tools/replit?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=mira-murati-s-tml-upends-how-humans-work-with-ai) \- Run up to 10 parallel computer-use agents in Replit

  * ☀️ [Daybreak](https://openai.com/daybreak/?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=mira-murati-s-tml-upends-how-humans-work-with-ai) \- OpenAI’s new Codex-driven cybersecurity product




 _*Sponsored Listing_

### 📰 **[Everything else in AI today](https://www.rundown.ai/?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=mira-murati-s-tml-upends-how-humans-work-with-ai)**

**OpenAI** [launched](https://openai.com/index/openai-launches-the-deployment-company/?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=mira-murati-s-tml-upends-how-humans-work-with-ai) “The Deployment Company”, a $14B business to embed engineers inside enterprises to deploy its AI, also acquiring AI consulting firm Tomoro. 

**SoftBank’s Masayoshi Son** is reportedly [in talks](https://www.reuters.com/business/media-telecom/softbanks-son-weighs-up-100-billion-investment-france-bloomberg-news-reports-2026-05-11/?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=mira-murati-s-tml-upends-how-humans-work-with-ai) for a $100B AI investment into France, with plans to build out new data centers in the country.

**Anthropic** reportedly****[signed](https://www.bloomberg.com/news/articles/2026-05-08/anthropic-inks-1-8-billion-computing-deal-with-akamai?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=mira-murati-s-tml-upends-how-humans-work-with-ai) a 7-year, $1.8B cloud infrastructure deal with Akamai, adding another compute avenue to power its Claude models. 

**China’s Kuaishou Technology** is reportedly [planning](https://www.theinformation.com/articles/chinas-kuaishou-plans-spin-kling-ai-video-unit-20-billion-valuation?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=mira-murati-s-tml-upends-how-humans-work-with-ai) to turn its Kling AI video branch into its own company, with a projected valuation of $20B and plans to IPO in 2027. 

**Former OpenAI Chief Scientist Ilya Sutskever** [testified](https://www.bloomberg.com/news/articles/2026-05-11/sutskever-says-his-openai-stake-worth-about-7-billion?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=mira-murati-s-tml-upends-how-humans-work-with-ai) in the Elon Musk vs. OpenAI lawsuit, revealing his current shares of the company total nearly $7B. 

**COMMUNITY**

### 🤝 **[Community AI workflows](https://www.videoask.com/ffohxg3vc?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=mira-murati-s-tml-upends-how-humans-work-with-ai)**

Every newsletter, we showcase how a reader is using AI to work smarter, save time, or make life easier.

Today’s workflow comes from reader **Sasha M.** in Cape Coral, FL:

"I have a family of 5, and planning what we have for dinner was a nightmare. I have a Trello board full of hundreds of recipes that I use to plan our meals, and then I would place a grocery delivery order online. The whole process would take up to an hour.

I built a Claude plugin that includes multiple skills to help plan meals and order groceries. I have it on a schedule to run once a week. First, it asks me for details about the week: our schedule, any days that I'll have fewer than 5 people eating, etc. Using an MCP to Trello, the first Claude Skill picks out 7 recipes and presents them to me. 

Once I've approved the meal plan, Claude then creates an ingredients list that I check off anything I already have in my fridge/pantry. The plugin then runs a skill that goes to my grocery store website and adds all the ingredients to my cart. All I have to do is check the cart and click ‘Order.’"

How do you use AI? Tell us [here](https://www.videoask.com/ffohxg3vc?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=mira-murati-s-tml-upends-how-humans-work-with-ai).

### **🎓****[Highlights: News, Guides& Events](https://app.therundown.ai/?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=mira-murati-s-tml-upends-how-humans-work-with-ai)**

  * Read our last AI newsletter: [Google’s powerful new AI co-mathematician ](https://www.rundown.ai/articles/google-deepmind-powerful-ai-co-mathematician?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=mira-murati-s-tml-upends-how-humans-work-with-ai)

  * Read our last Tech newsletter: ['RAMageddon' is coming for your laptop](https://www.rundown.ai/articles/ramageddon-is-coming-for-your-laptop?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=mira-murati-s-tml-upends-how-humans-work-with-ai)

  * Read our last Robotics newsletter: [Figure’s robots make a bed together](https://www.rundown.ai/articles/figure-robots-make-a-bed-together?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=mira-murati-s-tml-upends-how-humans-work-with-ai)

  * Today’s AI tool guide: [Build a YouTube research bot in 15 minutes](https://app.therundown.ai/guides/build-a-youtube-research-bot-in-15-minutes?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=mira-murati-s-tml-upends-how-humans-work-with-ai)




See you soon,

_Rowan, Joey, Zach, Shubham, and Jennifer — the humans behind The Rundown_

---

## [Google DeepMind’s powerful AI co-mathematician](https://www.therundown.ai/p/google-deepmind-powerful-ai-co-mathematician)
*🗞️ The Rundown AI | 2026-05-11*

**[Read Online](https://rss.beehiiv.com/feeds/{{live_url}})** | **[Sign Up](https://www.therundown.ai/subscribe?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=google-deepmind-s-powerful-ai-co-mathematician)** | **[Advertise](https://therundownai.typeform.com/to/kraZ1TSO?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=google-deepmind-s-powerful-ai-co-mathematician)**

[](https://cloud.google.com/resources/content/future-of-ai-genmedia?utm_source=gfs&utm_medium=media&utm_campaign=FY26-Q2-GLOBAL-GCP40293-website-dl-StartupGenMedia-168368&utm_content=rundown2&utm_term=-)

**Good morning, {{ first_name | AI enthusiasts }}.** Google DeepMind just took AI’s coding strategy and applied it to math: don't ask a model for the answer, give a team of agents the workspace.

The company’s AI co-mathematician just scored a new high on a benchmark built to stump AI for decades, with one professor even cracking an unsolved problem using a strategy buried inside a proof the system's own reviewers had rejected.

* * *

**In today’s AI rundown:**

  * Google DeepMind’s AI co-mathematician

  * The Rundown Roundtable: Our AI use cases

  * Automate any manual task with Codex

  * AI finds 100+ new exoplanets from NASA data

  * 4 new AI tools, community workflows, and more




**LATEST DEVELOPMENTS**

###### GOOGLE DEEPMIND

#### 🧮 **[Google DeepMind’s AI co-mathematician](https://arxiv.org/pdf/2605.06651?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=google-deepmind-s-powerful-ai-co-mathematician)**

Image source: Pushmeet Kohli (@pushmeet on X)

**The Rundown:** Google DeepMind just [published](https://arxiv.org/pdf/2605.06651?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=google-deepmind-s-powerful-ai-co-mathematician) a paper on its AI co-mathematician, an agentic system based on Gemini 3.1 built to help mathematicians tackle unsolved problems — setting a new high on a benchmark of research-level math problems.

**The details:**

  * DeepMind modeled the tool after AI coding environments like Claude Code, bringing agent teams and built-in review cycles to math research. 

  * A coordinator agent breaks research into parallel workstreams, each with sub-agents that write code, search literature, and attempt proofs. 

  * Oxford’s Marc Lackenby resolved an open problem in the Kourovka Notebook after spotting a 'really, really clever proof strategy' inside a rejected output.

  * On Epoch AI's FrontierMath Tier 4, the system topped the leaderboard at 48% and more than doubled Gemini 3.1 Pro's 19% raw score. 




**Why it matters:** AI has already led to a surge in mathematics discoveries with the advances in frontier models, and similar to coding, agentic pipelines are now enabling AI systems to push even further. But as Lackenby’s discovery shows, the future is still bright for AI that enables top minds to accelerate their work, not replace it. 

###### TOGETHER WITH GOOGLE FOR STARTUPS

#### 📚 **[Master generative media for startups](https://cloud.google.com/resources/content/future-of-ai-genmedia?utm_source=gfs&utm_medium=media&utm_campaign=FY26-Q2-GLOBAL-GCP40293-website-dl-StartupGenMedia-168368&utm_content=rundown2&utm_term=-)**

[](https://cloud.google.com/resources/content/future-of-ai-genmedia?utm_source=gfs&utm_medium=media&utm_campaign=FY26-Q2-GLOBAL-GCP40293-website-dl-StartupGenMedia-168368&utm_content=rundown2&utm_term=-)

**The Rundown:** Google for Startups' Future of AI report is your essential guide to understanding how generative media is reshaping product development, offering founders strategic insights to build smarter, scale faster, and stay ahead of the AI curve.

**Inside the report, you’ll discover:**

  * How to leverage digital twinning at scale.

  * Strategic insights for AI product differentiation.

  * Expert perspectives on the generative landscape.




[Download the report today](https://cloud.google.com/resources/content/future-of-ai-genmedia?utm_source=gfs&utm_medium=media&utm_campaign=FY26-Q2-GLOBAL-GCP40293-website-dl-StartupGenMedia-168368&utm_content=rundown2&utm_term=-).

###### THE RUNDOWN ROUNDTABLE

#### 💡 **[The Rundown Roundtable: Our AI use cases](https://www.rundown.ai/?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=google-deepmind-s-powerful-ai-co-mathematician)**

Image source: Ideogram / The Rundown

**The Rundown:** The Rundown Roundtable is a weekly feature where we poll members of The Rundown staff about how we use AI in our work or daily lives.

**Jason, Developer:** I used /goal in OpenAI’s Codex to build a Magic: The Gathering app so my brother and I can play asynchronously without needing to coordinate a call or awkwardly play over FaceTime.   
  
The idea is to let each of us take turns when we have time, track the board state cleanly, and keep a game going over days instead of trying to line up schedules. The command allowed Codex to continue running until everything was done, basically one-shotting exactly what I was looking for without any intervention.

**Joey, Partnerships:** I've never been to Greece, so for my upcoming trip, I went all in and handed the whole itinerary over to Claude. Flights booked, transit times dialed, restaurant lists curated city by city.   
  
I’m now showing up with a plan tighter than most travel agents could put together!

###### AI TRAINING

#### ✅ **[Automate any manual task with Codex](https://app.therundown.ai/guides/automate-any-manual-task-with-codex?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=google-deepmind-s-powerful-ai-co-mathematician)**

[](https://app.therundown.ai/guides/automate-any-manual-task-with-codex?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=google-deepmind-s-powerful-ai-co-mathematician)

**The Rundown:** In this guide, you will learn how to let Codex click through any annoying, repetitive work using Computer Use on Mac or Windows.

**Step-by-step:**

  1. Open Codex, go to Plugins, find and enable the Computer Use plugin, and start a new task

  2. Open the permissions menu and switch from Default permissions to Full access, then confirm any prompts and give Codex something real to do

  3. Example: “Open Chrome and debug this web page UI I’m developing [http://localhost:3000/](https://localhost:3000/?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=google-deepmind-s-powerful-ai-co-mathematician). Click through, reproduce the bug I describe, then tell me what you think is causing it. If not sure, ask before making changes”




**Pro tip:** Codex can automate repetitive workflows in local apps, too — try it for Photoshop exports, Adobe Premiere cleanup, file renaming, or any other tool.

###### PRESENTED BY ORACLE DEVELOPERS

#### 🚀 [**Small models, bigger reasoning**](https://blogs.oracle.com/developers/16-ways-to-make-a-small-language-model-think-bigger?source=%3Aad%3Anw%3Aop%3Aawr%3Aa_nas%3A%3ARC_DEVT260124P00001%3ADevMktg_TheRundown&SC=%3Aad%3Anw%3Aop%3Aawr%3Aa_nas%3A%3ARC_DEVT260124P00001%3ADevMktg_TheRundown&utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=google-deepmind-s-powerful-ai-co-mathematician)

[](https://blogs.oracle.com/developers/16-ways-to-make-a-small-language-model-think-bigger?source=%3Aad%3Anw%3Aop%3Aawr%3Aa_nas%3A%3ARC_DEVT260124P00001%3ADevMktg_TheRundown&SC=%3Aad%3Anw%3Aop%3Aawr%3Aa_nas%3A%3ARC_DEVT260124P00001%3ADevMktg_TheRundown&utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=google-deepmind-s-powerful-ai-co-mathematician)

**The Rundown:** Small language models can solve harder reasoning tasks without changing their weights. Oracle Developers’ open-source agent-reasoning code shows how to add research-backed orchestration to Ollama models, with 16 reasoning strategies developers can test locally.

**In the guide, you’ll explore:**

  * Open-source reasoning code for Ollama

  * 16 strategies, benchmarked across 4,200 runs

  * Better accuracy without retraining models




Get the open-source reasoning patterns. [Explore the guide](https://blogs.oracle.com/developers/16-ways-to-make-a-small-language-model-think-bigger?source=%3Aad%3Anw%3Aop%3Aawr%3Aa_nas%3A%3ARC_DEVT260124P00001%3ADevMktg_TheRundown&SC=%3Aad%3Anw%3Aop%3Aawr%3Aa_nas%3A%3ARC_DEVT260124P00001%3ADevMktg_TheRundown&utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=google-deepmind-s-powerful-ai-co-mathematician).

###### AI & ASTRONOMY

#### 🪐 **[AI finds 100+ new exoplanets from NASA data](https://warwick.ac.uk/news/pressreleases/ai-approach-uncovers-dozens-of-hidden-planets/?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=google-deepmind-s-powerful-ai-co-mathematician)**

Image source: NASA

**The Rundown:** University of Warwick astronomers [confirmed](https://warwick.ac.uk/news/pressreleases/ai-approach-uncovers-dozens-of-hidden-planets/?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=google-deepmind-s-powerful-ai-co-mathematician) more than 100 exoplanets using an AI system called RAVEN that scanned 4 years of NASA TESS data covering 2.2M stars, with RAVEN also finding 2,000+ additional potential candidates.

**The details:**

  * RAVEN handles detection, vetting, and confirmation in one shot, trained on simulated planets and false-alarm signals to filter real finds.

  * The findings included 31 exoplanets never before spotted, plus strange worlds that orbit around their stars in under a day.

  * Hundreds of exoplanets were found in the "Neptunian Desert", a region so close to a star that Neptune-sized planets shouldn't survive the heat.

  * The system measures how common different planet types are at 10x the precision of previous systems from smarter AI alone, not new hardware. 




**Why it matters:** Humans have confirmed just a few thousand exoplanets so far, and there are estimated to be trillions. AI and tech advances are going to help rewrite that number fast — and judging from RAVEN, all it will take is upgraded models and AI integrations to uncover knowledge about space already hiding in the data we have. 

**QUICK HITS**

### 🛠️ **[Trending AI Tools](https://www.rundown.ai/tools?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=google-deepmind-s-powerful-ai-co-mathematician)**

  * 🔒 [Incogni](https://deal.incogni.io/aff_c?offer_id=6&aff_id=1889&url_id=1&utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=google-deepmind-s-powerful-ai-co-mathematician) \- Remove your personal data from the web so scammers and identity thieves can’t access it. Use code **RUNDOWN** to get 55% off*

  * 💻 [Codex in Chrome](https://developers.openai.com/codex/app/chrome-extension?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=google-deepmind-s-powerful-ai-co-mathematician) \- OAI’s Codex extension for agentic tasks inside Chrome

  * 🧠 [ERNIE 5.1](https://www.rundown.ai/tools/ernie-5-1?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=google-deepmind-s-powerful-ai-co-mathematician) \- Baidu's new foundation model with strong search capabilities

  * 🖨️ [Printing Press](https://printingpress.dev/?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=google-deepmind-s-powerful-ai-co-mathematician) \- CLI factory with 30+ pre-built, agent-native tools




 _*Sponsored Listing_

### 📰 [Everything else in AI today](https://www.rundown.ai/?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=google-deepmind-s-powerful-ai-co-mathematician)

**Google’s Isomorphic Labs** is reportedly [raising](https://www.bloomberg.com/news/articles/2026-05-08/google-s-isomorphic-labs-to-raise-over-2-billion-in-new-funding?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=google-deepmind-s-powerful-ai-co-mathematician) $2B+ to expand its Drug Design Engine, which it says significantly outperforms AlphaFold 3 on specific tasks.

**Greece** is [proposing](https://apnews.com/article/greece-constitution-artificial-intelligence-a9d0c3963bfffefd370a1e224895ee60?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=google-deepmind-s-powerful-ai-co-mathematician) AI protections into its constitution, requiring the tech to serve individual freedom, with PM Mitsotakis citing threats to democracy.

**Baidu** [released](https://x.com/Baidu_Inc/status/2053009538769735774?s=20&utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=google-deepmind-s-powerful-ai-co-mathematician) ERNIE 5.1, a new AI ranking No. 4 on Arena's Search Leaderboard, with the company claiming it cost just 6% as much to train as rival models. 

**OpenRouter** [launched](https://openrouter.ai/openrouter/pareto-code?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=google-deepmind-s-powerful-ai-co-mathematician) Pareto Code, a free routing layer that auto-picks the cheapest coding AI above a user-set quality bar, with prices adjusting as newer models improve.

**SoftBank Group’s** telecom arm [launched](https://www.wsj.com/tech/softbank-launches-japan-battery-venture-amid-ai-hardware-push-34dba5e8?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=google-deepmind-s-powerful-ai-co-mathematician) a battery business to build large-scale cells and storage systems — and meet the power demands of data centers in development.

**COMMUNITY**

### 🤝 **[Community AI workflows](https://www.videoask.com/ffohxg3vc?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=google-deepmind-s-powerful-ai-co-mathematician)**

Every newsletter, we showcase how a reader is using AI to work smarter, save time, or make life easier.

Today’s workflow comes from reader **Anonymous** :

"I have been using ChatGPT for various things professionally, which has been surprisingly helpful and refreshing. The greatest use I have found for it so far, though, is helping me train my 4 dogs.   
  
I was ready to drop thousands of dollars on a professional trainer just because of how chaotic it has been, but ChatGPT has helped me identify the root causes of specific behaviors and taught me how to successfully train around and beyond them using specific techniques tailored to my individual dogs.   
  
The confidence it has brought me, and the positive reinforcements have changed every dynamic in the household, and I wish I had started sooner."

How do you use AI? Tell us [here](https://www.videoask.com/ffohxg3vc?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=google-deepmind-s-powerful-ai-co-mathematician).

### **🎓****[Highlights: News, Guides& Events](https://app.therundown.ai/?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=google-deepmind-s-powerful-ai-co-mathematician)**

  * Read our last AI newsletter: [OpenAI closes reasoning gap in voice agents](https://www.rundown.ai/articles/openai-closes-reasoning-gap-in-voice-agents?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=google-deepmind-s-powerful-ai-co-mathematician)

  * Read our last Tech newsletter: [‘RAMageddon’ is coming for your laptop](https://www.rundown.ai/articles/ramageddon-is-coming-for-your-laptop?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=google-deepmind-s-powerful-ai-co-mathematician)

  * Read our last Robotics newsletter: [Genesis robot makes breakfast](https://www.rundown.ai/articles/genesis-robot-makes-breakfast?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=google-deepmind-s-powerful-ai-co-mathematician)

  * Today’s AI tool guide: [Automate any manual task with Codex](https://app.therundown.ai/guides/automate-any-manual-task-with-codex?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=google-deepmind-s-powerful-ai-co-mathematician)




See you soon,

_Rowan, Joey, Zach, Shubham, and Jennifer — the humans behind The Rundown_

---

## [OpenAI closes reasoning gap in voice agents](https://www.therundown.ai/p/openai-closes-reasoning-gap-in-voice-agents)
*🗞️ The Rundown AI | 2026-05-08*

**[Read Online](https://rss.beehiiv.com/feeds/{{live_url}})** | **[Sign Up](https://www.therundown.ai/subscribe?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-closes-reasoning-gap-in-voice-agents)** | **[Advertise](https://therundownai.typeform.com/to/kraZ1TSO?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-closes-reasoning-gap-in-voice-agents)**

[](https://pages.awscloud.com/awsmp-gim-jqup-adhoc-aim-ent-ai-data-leader-book-1-ent.html?trk=1c32ad2e-b511-4f96-bbcb-e6ae04147f9d&sc_channel=el&utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-closes-reasoning-gap-in-voice-agents)

**Good morning, {{ first_name | AI enthusiasts }}.** Typing made AI useful, but speech is where agents have to prove they can keep up with real life.

OpenAI's new real-time voice model trio is built for that messier interface, adding a major reasoning upgrade, the ability to talk while thinking, and capable tool use that moves AI voice agents closer to running tasks at the speed of natural conversation.

* * *

**In today’s AI rundown:**

  * OpenAI’s reasoning upgrade for voice agents

  * Google folds Fitbit into its AI health play

  * Test multiple AI models with same prompt

  * Anthropic plans for AI that builds itself

  * 4 new AI tools, community workflows, and more




**LATEST DEVELOPMENTS**

###### OPENAI

#### 🗣️ [**OpenAI’s reasoning upgrade for voice agents**](https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-closes-reasoning-gap-in-voice-agents)

Image source: OpenAI

**The Rundown:** OpenAI just [introduced](https://openai.com/index/advancing-voice-intelligence-with-new-models-in-the-api/?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-closes-reasoning-gap-in-voice-agents) GPT-Realtime-2, GPT-Realtime-Translate, and GPT-Realtime-Whisper, three API voice models that bring new reasoning, streaming, tool use, realism, and more capability upgrades to AI voice agents and live speech.

**The details:**

  * Realtime-2 brings GPT-5-level reasoning to live speech, is able to use multiple tools at once, talks while it thinks, and has better tone control for realism.

  * On Big Bench Audio, Realtime-2 hit 96.6% vs. 81.4% for its predecessor, a 15-point jump in how well voice AI can reason in real-time.

  * OpenAI also shipped a live translator covering 70+ languages and a streaming transcription model, rounding out a full voice-agent toolkit.

  * OAI said Zillow, Priceline, and Deutsche Telekom are already building on the models for real estate AI agents, voice-managed travel, and customer support. 




**Why it matters:** AI voice’s turn-based era appears to be nearing a close, with OAI’s new model moving to systems that can reason better, leverage tools, and complete workflows without awkward interruptions that take users out of a natural flow. The AI industry is fixated on text agents, but the next wave will be spoken to, not typed at. 

###### TOGETHER WITH AWS MARKETPLACE

#### 📊****[**15+ enterprise leaders on getting data AI-ready**](https://pages.awscloud.com/awsmp-gim-jqup-adhoc-aim-ent-ai-data-leader-book-1-ent.html?trk=1c32ad2e-b511-4f96-bbcb-e6ae04147f9d&sc_channel=el&utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-closes-reasoning-gap-in-voice-agents)

[](https://pages.awscloud.com/awsmp-gim-jqup-adhoc-aim-ent-ai-data-leader-book-1-ent.html?trk=1c32ad2e-b511-4f96-bbcb-e6ae04147f9d&sc_channel=el&utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-closes-reasoning-gap-in-voice-agents)

**The Rundown** : AWS Marketplace just released a free book featuring 15 chapters from senior data and AI leaders at JPMorgan Chase, Siemens, Mercedes-Benz, Roche, and more — each sharing practical advice on building the data infrastructure needed for agentic analytics and intelligent agents.

**Chapters cover topics including:**

  * Evolving data strategy for agentic AI and scaling data products

  * Building on existing infrastructure with a pragmatic, business-first approach

  * Unlocking value with classical ML, semantic layers, and cross-team alignment

  * Real-world perspectives from leaders across different industries




[Get your free digital copy today](https://pages.awscloud.com/awsmp-gim-jqup-adhoc-aim-ent-ai-data-leader-book-1-ent.html?trk=1c32ad2e-b511-4f96-bbcb-e6ae04147f9d&sc_channel=el&utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-closes-reasoning-gap-in-voice-agents).

###### GOOGLE

#### ⌚️ **[Google folds Fitbit into its AI health play](https://blog.google/products-and-platforms/products/google-health/google-health-app/?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-closes-reasoning-gap-in-voice-agents)**

Image source: Google

**The Rundown:** Google [opened](https://blog.google/products-and-platforms/products/google-health/google-health-app/?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-closes-reasoning-gap-in-voice-agents) its AI health coach to the public after months in beta, integrating the Fitbit app into a new Google Health platform and pairing it with a new $99 screenless tracker that tracks and transmits body data to the AI.

**The details:**

  * Running on Gemini, the AI coach can tailor weekly workout routines, interpret uploaded medical records, and ID what a user ate from a phone photo. 

  * Google is consolidating the Fitbit app, Health Connect, Apple Health, wearable data, and U.S. medical records into a single Google Health hub. 

  * The new $99 Fitbit Air has no screen and weighs just 12g, carrying heart rate, oxygen, and temperature sensors that provide body data to the AI coach. 

  * Apple Watch, Garmin, and Oura owners are set to get AI coach access later this year, with Google opening it up to hardware outside of its own. 




**Why it matters:** AI’s role in personal health is only growing, and integrating everything under one roof can help Google make the AI layer the core product while also owning a trusted wearable line that provides users with the personalized guidance and context typically missing from other trackers and less connected options. 

###### AI TRAINING

#### ✏️ [T](https://app.therundown.ai/guides/how-to-test-multiple-ai-models-with-the-same-prompt-fast?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-closes-reasoning-gap-in-voice-agents)**[est multiple AI models with same prompt](https://app.therundown.ai/guides/how-to-test-multiple-ai-models-with-the-same-prompt-fast?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-closes-reasoning-gap-in-voice-agents)**

[](https://app.therundown.ai/guides/how-to-test-multiple-ai-models-with-the-same-prompt-fast?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-closes-reasoning-gap-in-voice-agents)

**The Rundown:** In this guide, you will learn how to use OpenRouter Fusion to test the same prompt across multiple AI models at once. Instead of opening five apps and guessing, you can compare outputs side by side and build a quick cheat sheet for work.

**Step-by-step:**

  1. Create an OpenRouter account, open [OpenRouter Fusion](https://openrouter.ai/labs/fusion?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-closes-reasoning-gap-in-voice-agents), and pick how you want to pay for AI usage — OpenRouter credits or API keys you already pay for

  2. In Fusion, pick the models you want to compare — we tested Opus 4.7 vs. GPT 5.4 vs. Grok — and run one benchmark prompt at a time, keeping it identical

  3. Prompt something like: “You are advising a 20-person SaaS company deciding whether to replace its weekly status meeting with an async written update. Write a recommendation memo with 3 benefits, 3 risks, and a 2-week implementation plan. Keep it concise and practical”

  4. Open the responses, read the side-by-side analysis, and note which model is strongest. In the demo, about 10 comparisons cost around 40 cents




**Pro tip:** Run a few prompts you use all the time, write which model wins each task, and use OpenRouter's model browser to compare price and speed before you spend more.

###### PRESENTED BY WEIGHTS & BIASES

#### 🐝****[**New guide: Tools and workflows to develop AI agents**](https://wandb.ai/site/resources/whitepapers/building-successful-ai-agents/?utm_source=rundown&utm_medium=cpc&utm_campaign=WP-AIAgentsPrimer&utm_content=46150)

[](https://wandb.ai/site/resources/whitepapers/building-successful-ai-agents/?utm_source=rundown&utm_medium=cpc&utm_campaign=WP-AIAgentsPrimer&utm_content=46150)

**The Rundown:** AI agents can dramatically boost productivity and innovation, but getting them into the real world takes a lot of iteration. Whether you’re exploring agents for the first time or refining your current approach, this primer delivers actionable insights to help your team succeed and thrive in the AI era.

**Get the guide to learn:**

  * What defines agentic applications and why observability matters

  * A proven workflow for building agentic AI applications

  * How pioneering companies are building and deploying AI agents today




[Download a primer on building successful AI agents](https://wandb.ai/site/resources/whitepapers/building-successful-ai-agents/?utm_source=rundown&utm_medium=cpc&utm_campaign=WP-AIAgentsPrimer&utm_content=46150).

###### THE ANTHROPIC INSTITUTE

#### 🔬 **[Anthropic plans for AI that builds itself](https://www.anthropic.com/research/anthropic-institute-agenda?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-closes-reasoning-gap-in-voice-agents)**

Image source: Anthropic

**The Rundown:** Anthropic's newly formed research arm, The Anthropic Institute, [published](https://www.anthropic.com/research/anthropic-institute-agenda?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-closes-reasoning-gap-in-voice-agents) its formal research agenda — a document that treats the possibility of AI systems improving themselves as something the company is actively preparing for. 

**The details:**

  * TAI sits inside Anthropic, letting researchers study Claude usage, internal workflows, and security signals before they hit the wider market.

  * The Institute’s agenda spans security threats, economic disruption, governance, and planning for self-improving models.

  * The team also proposed Cold War-style hotlines between labs and governments, plus "fire drill" exercises for sudden capability surges. 

  * TAI said it is committed to publishing Economic Index data, monthly worker surveys, threat research, and more details on its own internal AI-boosted R&D. 




**Why it matters:** We [wrote](https://www.rundown.ai/articles/ai-data-centers-head-for-the-ocean?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-closes-reasoning-gap-in-voice-agents) earlier about Anthropic co-founder Jack Clark’s blog on self-improving systems, and TAI’s research agenda puts it very much into focus. Anthropic’s talk of “fire drills” and Cold War-style systems is to prepare for an “intelligence explosion” that we might be heading to faster than many expected.

**QUICK HITS**

### 🛠️ **[Trending AI Tools](https://www.rundown.ai/tools?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-closes-reasoning-gap-in-voice-agents)**

  * ✈️ [Serko.ai](https://www.serko.ai/?utm_source=www.therundown.ai&utm_medium=email&utm_campaign=waitlist) \- The AI travel assistant that plans, books, and manages your entire business trip, so you can skip the busywork*

  * 🗣️ [GPT-Realtime-2](https://www.rundown.ai/tools/gpt-realtime-2?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-closes-reasoning-gap-in-voice-agents) \- Voice AI that thinks, calls tools, maintains convo flow

  * 🎥 [Studio Agent](https://www.rundown.ai/tools/elevenlabs-studio-agents?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-closes-reasoning-gap-in-voice-agents) \- ElevenLabs' AI editor to draft videos, places sound effects

  * 🎆 [Grok Imagine Quality Mode](https://x.ai/news/grok-imagine-quality-mode?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-closes-reasoning-gap-in-voice-agents) \- xAI’s Image generation with higher realism




 _*Sponsored Listing_

### 📰 **[Everything else in AI today](https://www.rundown.ai/?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-closes-reasoning-gap-in-voice-agents)**

**Spotify** [launched](https://newsroom.spotify.com/2026-05-07/personal-podcasts-launch/?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-closes-reasoning-gap-in-voice-agents) ‘Personal Podcasts’, a tool allowing agents to turn items like briefings or class notes into a personal podcast directly inside users’ Spotify libraries.

**OpenAI** [introduced](https://openai.com/index/introducing-trusted-contact-in-chatgpt/?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-closes-reasoning-gap-in-voice-agents) Trusted Contact, an opt-in ChatGPT feature that alerts a designated friend or family member if signs of self-harm risk are detected.

**Scale AI** [landed](https://www.bloomberg.com/news/articles/2026-05-06/meta-backed-scale-ai-wins-500-million-defense-department-deal?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-closes-reasoning-gap-in-voice-agents) a $500M Pentagon contract for military data analysis, marking a 5x jump from last September's $100M deal.

**Perplexity**[rolled out](https://x.com/perplexity_ai/status/2052445405754040816?s=20&utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-closes-reasoning-gap-in-voice-agents) its Personal Computer to all Mac users, allowing it to take agentic action across a user’s local computer, files, and via the Comet browser.

**Mozilla**[published](https://hacks.mozilla.org/2026/05/behind-the-scenes-hardening-firefox/?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-closes-reasoning-gap-in-voice-agents) a blog about using Claude Mythos Preview for security, saying the model patched more bugs in April than the past 15 months combined. 

**COMMUNITY**

### 🤝 **[Community AI workflows](https://www.videoask.com/ffohxg3vc?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-closes-reasoning-gap-in-voice-agents)**

Every newsletter, we showcase how a reader is using AI to work smarter, save time, or make life easier.

Today’s workflow comes from reader **Tatiana B.** in San Francisco, CA:

"I'm COO of a startup and mom to a two-and-a-half-year-old. Managing both is a lot, and keeping track of everything I need to do at home on top of work can be a real mental drain.

So I use AI to help me compile a document covering everything I need help with at home: my daughter's meal preferences, her daily routine, and house chores. I treat it like a work project, going back and forth with AI to think through what I actually need done, fill in gaps I hadn't thought of, and get it all out of my head into something I can hand to someone else.

Now, when someone new comes to help at home, I don't have to explain everything from scratch. That frees me up to actually be present with my daughter when I'm with her, and focused on work when I'm not. I also know I'm lucky to be in a position to hire help, but using AI to think clearly about what you need and get it out of your head is something anybody can do."

How do you use AI? Tell us [here](https://www.videoask.com/ffohxg3vc?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-closes-reasoning-gap-in-voice-agents).

### **🎓****[Highlights: News, Guides& Events](https://app.therundown.ai/?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-closes-reasoning-gap-in-voice-agents)**

  * Read our last AI newsletter: [Anthropic, SpaceXAI become unlikely partners](https://www.rundown.ai/articles/anthropic-spacex-ai-become-unlikely-compute-partners?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-closes-reasoning-gap-in-voice-agents)

  * Read our last Tech newsletter: [GameStop’s wild bid to buy eBay](https://www.rundown.ai/articles/gamestop-wild-bid-to-buy-ebay?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-closes-reasoning-gap-in-voice-agents)

  * Read our last Robotics newsletter: [Genesis robot makes breakfast](https://www.rundown.ai/articles/genesis-robot-makes-breakfast?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-closes-reasoning-gap-in-voice-agents)

  * Today’s AI tool guide: [Test multiple AI models with the same prompt, ](https://app.therundown.ai/guides/how-to-test-multiple-ai-models-with-the-same-prompt-fast?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-closes-reasoning-gap-in-voice-agents)[fast](https://app.therundown.ai/guides/how-to-test-multiple-ai-models-with-the-same-prompt-fast?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-closes-reasoning-gap-in-voice-agents)




See you soon,

_Rowan, Joey, Zach, Shubham, and Jennifer — the humans behind The Rundown_

---

## [Anthropic, SpaceX(AI) become unlikely compute partners](https://www.therundown.ai/p/anthropic-spacex-ai-become-unlikely-compute-partners)
*🗞️ The Rundown AI | 2026-05-07*

**[Read Online](https://rss.beehiiv.com/feeds/{{live_url}})** | **[Sign Up](https://www.therundown.ai/subscribe?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=anthropic-spacex-ai-become-unlikely-compute-partners)** | **[Advertise](https://therundownai.typeform.com/to/kraZ1TSO?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=anthropic-spacex-ai-become-unlikely-compute-partners)**

[](https://stripe.com/lp/pricing-ai-products?utm_campaign=TGoD9zd88w5CaCK7EMH3pT4TG)

**Good morning, {{ first_name | AI enthusiasts }}.** Just months ago, Elon Musk was posting that Anthropic “hates Western Civilization” and should be renamed “Misanthropic”. Now, he’s renting them his entire Colossus 1 compute cluster.  
  
The new deal pulls off three things at once: patching Claude's compute problems, hurting Musk's nemesis OAI by feeding its biggest rival, and signaling a new compute-landlord business for SpaceXAI even as Grok keeps chasing the frontier.

* * *

**In today’s AI rundown:**

  * Anthropic, SpaceX partner in new compute deal

  * Mira Murati speaks out in Musk vs. OpenAI trial

  * Use Claude Design’s slide decks feature like a pro

  * DeepMind picks EVE Online game as next AI testbed

  * 4 new AI tools, community workflows, and more




**LATEST DEVELOPMENTS**

###### ANTHROPIC & SPACEX

#### 🔌 **[Anthropic, SpaceX(AI) partner in new compute deal](https://www.anthropic.com/news/higher-limits-spacex?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=anthropic-spacex-ai-become-unlikely-compute-partners)**

Image source: Images 2.0 / The Rundown

**The Rundown:** Anthropic just [signed](https://www.anthropic.com/news/higher-limits-spacex?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=anthropic-spacex-ai-become-unlikely-compute-partners) a deal with SpaceX to lease its Colossus 1, raising Claude usage and putting Musk and Anthropic on one team months after he [said](https://x.com/elonmusk/status/2027294561467613256?s=20&utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=anthropic-spacex-ai-become-unlikely-compute-partners) that Anthropic should be called “Misanthropic” and it "hates Western Civilization."

**The details:**

  * Anthropic will lease all of Colossus 1, a 300+ MW Memphis supercluster, with more than 220K Nvidia GPUs coming online within the month.

  * Anthropic said Claude Code’s 5-hour usage caps are now doubling across paid tiers, with additional increases via API and no more peak-hour restrictions.

  * Musk [replied](https://x.com/elonmusk/status/2052076315306864756?s=20&utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=anthropic-spacex-ai-become-unlikely-compute-partners) on X that SpaceX will rent compute to “AI companies that are taking the right steps to ensure it is good for humanity.”

  * The Information also [reported](https://www.theinformation.com/articles/anthropic-commits-spending-200-billion-googles-cloud-chips?rc=a8sc5q&utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=anthropic-spacex-ai-become-unlikely-compute-partners) yesterday that Anthropic is committing to a $200B, 5 GW compute deal over the next five years with Google Cloud.




**Why it matters:** This is a fascinating partnership from several angles. One being Musk taking the ‘enemy of my enemy is my friend’ approach — helping patch OAI’s biggest rival’s glaring compute hole. Another is SpaceXAI ([apparently](https://x.com/elonmusk/status/2052105373621121284?s=20&utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=anthropic-spacex-ai-become-unlikely-compute-partners) the new name), moving to providing compute for rivals while still pushing to get Grok near the frontier.

###### TOGETHER WITH STRIPE

#### 🏷️ [**A five-step framework for pricing AI products**](https://stripe.com/lp/pricing-ai-products?utm_campaign=TGoD9zd88w5CaCK7EMH3pT4TG)

[](https://stripe.com/lp/pricing-ai-products?utm_campaign=TGoD9zd88w5CaCK7EMH3pT4TG)

**The Rundown:** Pricing AI products means making a series of connected decisions—how you charge, how you match prices to value, and how you adapt as costs and the market shift. Stripe's new framework outlines 5 steps for pricing AI products.

**In this guide, you’ll learn:**

  * How AI leaders like Anthropic, Clay, and Vercel approach their pricing

  * Strategies to align what you charge with the exact value you deliver

  * Steps to pick a pricing model that balances ease of user adoption with repeatable revenue




**[Get the framework](https://stripe.com/lp/pricing-ai-products?utm_campaign=TGoD9zd88w5CaCK7EMH3pT4TG)**.

###### ELON MUSK VS. OPENAI TRIAL 

#### 🏛️ [**Mira Murati speaks out in Musk vs. OpenAI trial**](https://www.theverge.com/ai-artificial-intelligence/925338/openai-musk-v-altman-mira-murati?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=anthropic-spacex-ai-become-unlikely-compute-partners)

Image source: Reuters

**The Rundown:** Ex-OpenAI CTO Mira Murati [testified](https://www.theverge.com/ai-artificial-intelligence/925338/openai-musk-v-altman-mira-murati?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=anthropic-spacex-ai-become-unlikely-compute-partners) Wednesday via video deposition in Elon Musk's lawsuit against OpenAI, accusing CEO Sam Altman of lying about a model's safety review, undermining her authority, and pitting execs against one another.

**The details:**

  * Murati said Altman told her OAI's legal team cleared a model to skip safety review, which she later verified with counsel Jason Kwon was false.

  * She also described Altman giving conflicting directions to different execs, making her role as CTO harder and creating chaos across OAI's leadership.

  * Murati briefly became interim CEO during Altman’s 2023 firing, but said the board process put OpenAI “at risk of falling apart.” 

  * Former OAI board member Helen Toner also [testified](https://nypost.com/2026/05/06/business/openai-ceo-sam-altman-was-dishonest-caused-chaos-ex-exec-mira-murati-says-in-bombshell-testimony/?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=anthropic-spacex-ai-become-unlikely-compute-partners), reportedly criticizing Murati as “afraid to stick her neck out” and scared of “blowback for her career”. 




**Why it matters:** The 2023 board drama is the saga that will never conclude, and Murati’s testimony is a powerful voice to aid Musk’s argument that Altman and co. are untrustworthy. But whether that ultimately means anything related to Musk’s claims of Altman and Brockman “trying to steal a charity” in 2017 is up for the jury to decide. 

###### AI TRAINING

#### 👨‍💻 **[Use Claude Design’s slide decks feature like a pro](https://app.therundown.ai/guides/use-claude-design-slide-decks-like-a-pro-with-this-strategy?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=anthropic-spacex-ai-become-unlikely-compute-partners)**

[](https://app.therundown.ai/guides/use-claude-design-slide-decks-like-a-pro-with-this-strategy?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=anthropic-spacex-ai-become-unlikely-compute-partners)

**The Rundown:** In this guide, you will learn how to use Claude Design to turn your raw data into a useful strategy deck complete with actual insights. Claude Design analyzes what is working and gives concrete recommendations your team can use.

**Step-by-step:**

  1. Start with one CSV or spreadsheet with a messy report (YT channel data, Facebook ads, etc.) and decide what the deck needs to do (like find patterns)

  2. Open claude.ai/design, choose Slide deck, skip the design system, toggle on speaker notes, and upload your data

  3. Prompt: “Turn these files into a strategy deck on performance. Analyze the results by item and extract best practices from the data and assets. Use charts, rankings, and concrete recommendations. Match images or creative files to CSV using the filename or matching field. Keep it presentation-ready”

  4. Generation will take 10-15 minutes. You can export to PowerPoint or Google Slides when it's ready




**Pro tip:** Duplicate the project and upload more data sources for Claude to incorporate into the presentation.

###### PRESENTED BY IBM

#### 🔌****[**Rewire the C-suite for an AI-first world**](https://www.ibm.com/thought-leadership/institute-business-value/en-us/c-suite-study/ceo?utm_content=CXOWW&p1=Display&p2=445612300&p3=247627917&utm_term=20AXK&utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=anthropic-spacex-ai-become-unlikely-compute-partners)

[](https://www.ibm.com/thought-leadership/institute-business-value/en-us/c-suite-study/ceo?utm_content=CXOWW&p1=Display&p2=445612300&p3=247627917&utm_term=20AXK&utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=anthropic-spacex-ai-become-unlikely-compute-partners)

**The Rundown:** Most leaders know AI will reshape their business, but few have a clear playbook for how. An IBM Institute of Business Value analysis reveals 5 plays that CEOs must fulfill now for payoffs by 2030.

**To lead in an AI-first landscape, surveyed CEOs suggest:**

  * Customize your AI mix, not just your AI models

  * Hire a Chief AI Officer if you haven’t already

  * Orchestrate intelligence —both artificial and human




[Get deeper details in the 2026 CEO Study](https://www.ibm.com/thought-leadership/institute-business-value/en-us/c-suite-study/ceo?utm_content=CXOWW&p1=Display&p2=445612300&p3=247627917&utm_term=20AXK&utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=anthropic-spacex-ai-become-unlikely-compute-partners).

###### GOOGLE DEEPMIND

#### 🛸 **[DeepMind picks EVE Online game as next AI testbed](https://www.ccpgames.com/news/2026/studio-behind-eve-online-goes-independent-rebrands-as-fenris-creations-enters-research-partnership-with-google-deepmind?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=anthropic-spacex-ai-become-unlikely-compute-partners)**

Image source: Fenris Creations

**The Rundown:** Google DeepMind [picked up](https://www.ccpgames.com/news/2026/studio-behind-eve-online-goes-independent-rebrands-as-fenris-creations-enters-research-partnership-with-google-deepmind?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=anthropic-spacex-ai-become-unlikely-compute-partners) a minority stake in Fenris Creations, a game studio spinoff from CCP Games, which makes the popular EVE Online — with DeepMind set to use the 23-year-old space game as a sandbox for AI research.

**The details:**

  * EVE Online has run for two decades on a single server where players form corporations, set market prices, and torch six-figure fleets in day-long battles.

  * DeepMind's investment will come with AI agent runs on an offline EVE clone, testing how models reason over long timelines, retain memory, and learn.

  * Demis Hassabis cited Atari DQN, AlphaGo, AlphaStar, and SIMA as game-bred DeepMind wins, calling games “the perfect training ground” for AI algorithms.__

  * Fenris’ CEO pitched EVE as “one of the few environments” where intelligence can be tested “inside something that already behaves like a living world”.




**Why it matters:** DeepMind has been here before with Go, Atari, StarCraft, and SIMA, but EVE is not a match to win as much as a 23-year-old living, evolving society to understand. That makes the Fenris deal a natural next step in the shift from game-playing AI to agents that can operate inside less predictable real-life systems.

**QUICK HITS**

### 🛠️ **[Trending AI Tools](https://www.rundown.ai/tools?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=anthropic-spacex-ai-become-unlikely-compute-partners)**

  * 🧠 [Memoket](https://memoket.ai/pages/use-cases?utm_source=newsletter&utm_medium=email&utm_campaign=Rundown0507) \- Stop briefing AI from scratch. Memoket captures conversations and remembers context. Try the app for free today*

  * 🤖 [Claude Managed Agents](https://www.rundown.ai/tools/claude-managed-agents?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=anthropic-spacex-ai-become-unlikely-compute-partners) \- Pre-built agent harness with ‘dreaming’ memory

  * ⚡️ [GPT 5.5 Instant](https://openai.com/index/gpt-5-5-instant/?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=anthropic-spacex-ai-become-unlikely-compute-partners) \- OpenAI’s new default model across ChatGPT

  * 🎧 [Realtime TTS-2](https://www.rundown.ai/tools/realtime-tts-2?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=anthropic-spacex-ai-become-unlikely-compute-partners) \- New voice AI that listens to match user tone and emotion




 _*Sponsored Listing_

### 📰 [Everything else in AI today](https://www.rundown.ai/?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=anthropic-spacex-ai-become-unlikely-compute-partners)

**Subquadratic**[debuted](https://subq.ai/how-ssa-makes-long-context-practical?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=anthropic-spacex-ai-become-unlikely-compute-partners) SubQ, a model the company claims has a 12M token context window and a 52x speed boost on long tasks at a fraction of the cost over rivals. 

**Anthropic** [launched](https://claude.com/blog/new-in-claude-managed-agents?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=anthropic-spacex-ai-become-unlikely-compute-partners) dreaming, outcomes, and multi-agent orchestration for Managed Agents, letting agents study past sessions, grade work, and split complex jobs.

**OpenAI** [teamed](https://openai.com/index/mrc-supercomputer-networking/?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=anthropic-spacex-ai-become-unlikely-compute-partners) up with AMD, Intel, NVIDIA, Microsoft, and Broadcom to open-source MRC, a tool that keeps giant AI training runs going when hardware fails mid-session.

**Chinese AI startup DeepSeek** is reportedly [nearing](https://www.ft.com/content/daaf2e0a-4a0d-4d7c-a85b-445480f6b9c7?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=anthropic-spacex-ai-become-unlikely-compute-partners) a new funding round that would value the company at as high as $45B.

**Google**[announced](https://blog.google/innovation-and-ai/models-and-research/google-labs/believe-flow-music-partnership/?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=anthropic-spacex-ai-become-unlikely-compute-partners) a new partnership with TuneCore parent Believe to put its Flow Music and Lyria 3 Pro model in front of artists.

**COMMUNITY**

### 🤝 **[Community AI workflows](https://www.videoask.com/ffohxg3vc?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=anthropic-spacex-ai-become-unlikely-compute-partners)**

Every newsletter, we showcase how a reader is using AI to work smarter, save time, or make life easier.

Today’s workflow comes from reader **Anonymous** :

"I'm recovering from a torn ACL, and my physiotherapist films all of my exercises and sends the videos to me on WhatsApp, narrating the sets/reps and notes on how to perform the exercise properly.   
  
I uploaded the videos into Gemini and got it to build a prompt for Claude Code, which one-shotted an app that I now use to track sets, reps, weights from last workouts, notes, over multiple months. I can then export this data into a .csv for my physio before we check back in with each other."

How do you use AI? Tell us [here](https://www.videoask.com/ffohxg3vc?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=anthropic-spacex-ai-become-unlikely-compute-partners).

### **🎓****[Highlights: News, Guides& Events](https://app.therundown.ai/?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=anthropic-spacex-ai-become-unlikely-compute-partners)**

  * Read our last AI newsletter: [OpenAI’s AI phone just jumped the line](https://www.rundown.ai/articles/openai-ai-phone-just-jumped-the-line?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=anthropic-spacex-ai-become-unlikely-compute-partners)

  * Read our last Tech newsletter: [GameStop’s wild bid to buy eBay](https://www.rundown.ai/articles/gamestop-wild-bid-to-buy-ebay?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=anthropic-spacex-ai-become-unlikely-compute-partners)

  * Read our last Robotics newsletter: [Meta buys a humanoid brain](https://www.rundown.ai/articles/meta-buys-a-humanoid-brain?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=anthropic-spacex-ai-become-unlikely-compute-partners)

  * Today’s AI tool guide: [Use Claude Design’s slide decks feature like a pro](https://app.therundown.ai/guides/use-claude-design-slide-decks-like-a-pro-with-this-strategy?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=anthropic-spacex-ai-become-unlikely-compute-partners)




See you soon,

_Rowan, Joey, Zach, Shubham, and Jennifer — the humans behind The Rundown_

---

## [OpenAI's AI phone just jumped the line](https://www.therundown.ai/p/openai-ai-phone-just-jumped-the-line)
*🗞️ The Rundown AI | 2026-05-06*

**[Read Online](https://rss.beehiiv.com/feeds/{{live_url}})** | **[Sign Up](https://www.therundown.ai/subscribe?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-s-ai-phone-just-jumped-the-line)** | **[Advertise](https://therundownai.typeform.com/to/kraZ1TSO?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-s-ai-phone-just-jumped-the-line)**

[](https://lambda.ai/llama-3-1-blackwell-mfu-benchmarks?utm_source=rundown-ai&utm_medium=newsletter&utm_campaign=2026-03-mfu-whitepaper&utm_content=main-ad-may-6)

**Good morning, {{ first_name | AI enthusiasts }}.** Amid intensifying competition with Anthropic, improved models, and efforts to kill “side hustles,” OpenAI is apparently looking at something closer to home — an AI agent phone.

Analyst Ming-Chi Kuo says the company is fast-tracking this device for 2027, with some notable capabilities. Good news for those wanting a stronger AI experience in their pockets. The question is: where does this leave the ongoing work with Jony Ive? Or is this the same device?

* * *

**In today’s AI rundown:**

  * OpenAI fast-tracks its ‘AI agent phone’

  * Anthropic’s AI agents for finance work

  * Make your Notion agents more autonomous 

  * Home-based ‘mini’ AI data centers are coming

  * 4 new AI tools, community workflows, and more




**LATEST DEVELOPMENTS**

###### OPENAI

#### 📱 [**OpenAI fast-tracks ‘AI agent phone’**](https://x.com/mingchikuo/status/2051523855286776034?s=20&utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-s-ai-phone-just-jumped-the-line)

Image source: Images 2.0 / The Rundown

**The Rundown:** OpenAI is reportedly [accelerating](https://x.com/mingchikuo/status/2051523855286776034?s=20&utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-s-ai-phone-just-jumped-the-line) development of its first AI phone, now aiming for mass production in the first half of 2027, which is a full year earlier than previously reported, according to supply chain analyst Ming-Chi Kuo.

**The details:**

  * Kuo says the timeline shift is likely driven by OAI’s IPO ambitions (strong hardware could strengthen investor pitch) and rising competition in AI phones.

  * The phone’s standout spec will be its image signal processor, with an enhanced HDR pipeline to improve AI agents’ real-world visual sensing.

  * MediaTek is positioned to be the sole chip supplier, with the device using two AI processors to handle vision and language tasks simultaneously.

  * Kuo also added that OpenAI’s combined 2027–28 shipments of this phone could touch 30M, if the development stays on track.




**Why it matters:** Controlling hardware and OS could be the key to a true agentic phone. But if OpenAI’s AI phone is closer than we thought, where does this leave the device it’s building with Jony Ive’s io? OpenAI [acquired](https://www.therundown.ai/p/openai-jony-ive-join-forces-in-6-5b-acquisition?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-s-ai-phone-just-jumped-the-line) io last year with much fanfare to go “beyond screens,” but nothing concrete has appeared so far [except a few rumors](https://www.therundown.ai/p/what-openai-and-jony-ive-are-building?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-s-ai-phone-just-jumped-the-line).

###### TOGETHER WITH LAMBDA

#### ⚡ **[How to push Model FLOPS Utilization past 50%](https://lambda.ai/llama-3-1-blackwell-mfu-benchmarks?utm_source=rundown-ai&utm_medium=newsletter&utm_campaign=2026-03-mfu-whitepaper&utm_content=main-ad-may-6)**

[](https://lambda.ai/llama-3-1-blackwell-mfu-benchmarks?utm_source=rundown-ai&utm_medium=newsletter&utm_campaign=2026-03-mfu-whitepaper&utm_content=main-ad-may-6)

**The Rundown:** Most large-scale training runs operate at just 35–45% Model FLOPS Utilization, meaning teams pay for more than twice the compute they actually use. Lambda’s engineers benchmarked Llama 3.1 models from 8B to 405B on NVIDIA Blackwell GPUs to trace efficiency loss to its root causes.

**Efficiency losses were traced to:**

  * Memory overhead capping effective throughput

  * Parallelism strategies misaligned with the hardware

  * Serialized communication stalling GPU cycles




[Get the guide](https://lambda.ai/llama-3-1-blackwell-mfu-benchmarks?utm_source=rundown-ai&utm_medium=newsletter&utm_campaign=2026-03-mfu-whitepaper&utm_content=main-ad-may-6).

###### ANTHROPIC

#### 🤑 [**Anthropic’s AI agents for finance work**](https://www.anthropic.com/news/finance-agents?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-s-ai-phone-just-jumped-the-line)

[](https://www.rundown.ai/?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-s-ai-phone-just-jumped-the-line)

Image source: Anthropic 

**The Rundown:** Anthropic just [unveiled](https://www.anthropic.com/news/finance-agents?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-s-ai-phone-just-jumped-the-line) 10 ready-to-run AI agents aimed squarely at financial services and insurance — capable of handling work ranging from building pitchbooks and screening KYC files to reviewing earnings and valuations.

**The details:**

  * Each agent comes with task-specific domain skills and instructions, connectors to relevant data sources, and add-on Claude models for sub-tasks.

  * Firms can adapt any agent of their choice to their own modeling conventions, risk policies, and approval flows — while staying in the loop 24/7.

  * The agents can be used as plugins within Claude Cowork or Claude Code on desktop, or as cookbooks, running as Managed Agents on the Claude platform.

  * Claude is also getting an add-in for Microsoft 365 as well as data connectors from Dun & Bradstreet, Verisk, IBISWorld, and other financial services partners.




**Why it matters:** Development, [cybersecurity](https://www.anthropic.com/news/claude-code-security?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-s-ai-phone-just-jumped-the-line), [design](https://www.therundown.ai/p/claude-comes-for-the-design-stack?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-s-ai-phone-just-jumped-the-line), and now finance. Anthropic is going domain by domain, meeting businesses where they are instead of selling a general model and letting them figure it out. Its [new $1.5B joint venture](https://www.anthropic.com/news/enterprise-ai-services-company?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-s-ai-phone-just-jumped-the-line) alongside Wall Street giants reinforces this strategy, further fueling its race with OpenAI.

###### AI TRAINING

#### 🤖 **[Make your Notion agents more autonomous](https://app.therundown.ai/guides/use-this-hidden-feature-to-make-your-notion-agents-autonomous?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-s-ai-phone-just-jumped-the-line)**

[](https://app.therundown.ai/guides/use-this-hidden-feature-to-make-your-notion-agents-autonomous?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-s-ai-phone-just-jumped-the-line)

**The Rundown:** In this guide, you will learn a hidden workflow that will make your Notion Agents more autonomous and powerful than they are by default. This lets you wake up any agent, give it tasks, and then get a report on what it did.

**Step-by-step:**

  1. Create a Notion agent from the “Agents” option in the sidebar. Then, open a database for the agent’s prompt and task reports. Ours is called “reports”

  2. Click the New dropdown, open Templates, and create a @Today template (ours was Daily Summary). @Today makes duplicates inherit the current date

  3. Set the properties, write task instructions in the page body, and @ mention the agent, so the duplicate triggers it. Remember to stop the agent when doing this, so it doesn’t overwrite the template

  4. From the template, click New template, then Duplicate, and pick a cadence. We run ours daily at 7 a.m. A small blue icon next to the template shows it’s live




**Pro tip:** Try setting up daily debriefs, weekly reports, and email automations. Now you can route them all through the same planning agent.

###### PRESENTED BY IBM

#### 🔌 **[Rewire the C-suite for an AI-first world](https://www.ibm.com/thought-leadership/institute-business-value/en-us/c-suite-study/ceo?utm_content=CXOWW&p1=Display&p2=445741634&p3=247627917&utm_term=20AXK&utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-s-ai-phone-just-jumped-the-line)**

[](https://www.ibm.com/thought-leadership/institute-business-value/en-us/c-suite-study/ceo?utm_content=CXOWW&p1=Display&p2=445741634&p3=247627917&utm_term=20AXK&utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-s-ai-phone-just-jumped-the-line)

**The Rundown:** Most leaders know AI will reshape their business, but few have a clear playbook for how. An IBM Institute of Business Value analysis reveals 5 plays that CEOs must fulfill now for payoffs by 2030.

**To lead in an AI-first landscape, surveyed CEOs suggest:**

  * Customize your AI mix, not just your AI models

  * Hire a Chief AI Officer if you haven’t already

  * Orchestrate intelligence — both artificial and human




[Get deeper details in the 2026 CEO Study](https://www.ibm.com/thought-leadership/institute-business-value/en-us/c-suite-study/ceo?utm_content=CXOWW&p1=Display&p2=445741634&p3=247627917&utm_term=20AXK&utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-s-ai-phone-just-jumped-the-line).

###### AI DATA CENTERS

#### 🏘️ [**Home-based ‘mini’ AI data centers are coming**](https://www.businesswire.com/news/home/20260414372626/en/SPAN-Announces-XFRA-a-Distributed-Data-Center-Solution-to-Close-the-Speed-to-Power-Gap-for-AI-Compute-Demand?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-s-ai-phone-just-jumped-the-line)

Image source: Span

**The Rundown:** California startup Span is [teaming up](https://www.businesswire.com/news/home/20260414372626/en/SPAN-Announces-XFRA-a-Distributed-Data-Center-Solution-to-Close-the-Speed-to-Power-Gap-for-AI-Compute-Demand?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-s-ai-phone-just-jumped-the-line) with Nvidia to install mini AI data centers on the walls of residential homes and small businesses, tapping unused electrical capacity on local grids to meet surging AI compute demand.

**The details:**

  * Span has developed XFRA, small compute nodes that mount on the exterior walls of homes, alongside accompanying HVAC and electrical systems.

  * Nvidia is providing its liquid-cooled RTX PRO 6000 Blackwell Server Edition GPUs to power each XFRA box, ensuring noiseless computing for AI workloads.

  * Span told [CNBC](https://www.cnbc.com/2026/05/05/nvidia-pulte-span-mini-data-centers-on-homes.html?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-s-ai-phone-just-jumped-the-line) it can install 8,000 XFRA units 6x faster and at one-fifth the cost of building a comparable 100MW centralized data center facility.

  * Currently, the company is working with PulteGroup, one of the largest U.S. homebuilders, to test the box and its economics in newly built communities.




**Why it matters:** Grid strain from data centers is real, and Span’s boxes could spread the load while tapping only unused capacity. But public response is an open question — not all will love the idea of a data center box mounted where kids play, especially when alternatives like [ocean](https://www.rundown.ai/articles/ai-data-centers-head-for-the-ocean?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-s-ai-phone-just-jumped-the-line)\- and [space-based](https://www.rundown.ai/articles/googles-ai-space-moonshot?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-s-ai-phone-just-jumped-the-line) data centers are also in sight.

**QUICK HITS**

### 🛠️ **[Trending AI Tools](https://www.rundown.ai/tools?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-s-ai-phone-just-jumped-the-line)**

  * 🚀 [**Box Automate**](https://blog.box.com/introducing-box-automate-ai-powered-workflow-orchestration?utm_source=newsletter&utm_medium=paidinfluencer&utm_theme=icm&utm_campaign=FY27_Q2_RundownAI_AutomateNewTool) \- Orchestrate agentic workflow automation, securely and at scale*

  * 🎨 [Pomelli](https://www.rundown.ai/tools/pomelli?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-s-ai-phone-just-jumped-the-line) \- Make product-specific campaigns with Google’s AI marketing tool

  * 🖼️ [Uni 1.1](https://lumalabs.ai/api?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-s-ai-phone-just-jumped-the-line) \- Luma’s new image generation and editing AI that nears the frontier

  * 🎮️ [Astrocade](https://www.astrocade.com/?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-s-ai-phone-just-jumped-the-line) \- Platform to create shareable games with AI

 _*Sponsored Listing_




### 📰 **[Everything else in AI today](https://www.rundown.ai/?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-s-ai-phone-just-jumped-the-line)**

**OpenAI’s** GPT-5.5-Instant [started](https://openai.com/index/gpt-5-5-instant/?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-s-ai-phone-just-jumped-the-line) rolling out to all ChatGPT users, bringing improved performance, stronger memory, and more personalized, concise responses.

**Microsoft** [expanded](https://www.microsoft.com/en-us/microsoft-365/blog/2026/05/05/copilot-cowork-from-conversation-to-action-across-skills-integrations-and-devices/?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-s-ai-phone-just-jumped-the-line) its Copilot Cowork agentic system to iOS and Android, while adding built-in skills for common tasks and data plugins for business systems.

**Apple** [agreed](https://www.bbc.com/news/articles/c0j2nydnzy7o?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-s-ai-phone-just-jumped-the-line) to pay some U.S. iPhone buyers a collective $250M to settle a class action lawsuit over misleading claims about its new AI Siri, but admitted no wrongdoing.

**Perplexity AI** [launched](https://x.com/perplexity_ai/status/2051693893473935372?s=20&utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-s-ai-phone-just-jumped-the-line) Computer for Professional Finance, bringing licensed data and 35 dedicated workflows to its agentic system to help analysts handle routine work.

**Anthropic** reportedly [committed](https://www.theinformation.com/articles/anthropic-commits-spending-200-billion-googles-cloud-chips?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-s-ai-phone-just-jumped-the-line) to spending $200B on Google’s cloud and chips over the next five years, now making 40%+ of Google’s revenue backlog.

**Coinbase** CEO Brian Armstrong [said](https://x.com/brian_armstrong/status/2051616759145185723?s=20&utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-s-ai-phone-just-jumped-the-line) the company is cutting 14% of its workforce, ~700 people, as it shifts to AI-native teams, agent-driven workflows, and leaner ops.

**COMMUNITY**

### 🤝 **[Community AI workflows](https://www.videoask.com/ffohxg3vc?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-s-ai-phone-just-jumped-the-line)**

Every newsletter, we showcase how a reader is using AI to work smarter, save time, or make life easier.

Today’s workflow comes from reader **Schy W.** in Springfield, IL:

"I went to a music festival — multiple stages, music over several days. Many bands had more than one set time/location. I fed Claude the festival’s schedule PDF and told it to extract the information, but to ignore autograph signing and music workshops. I then read off a list of bands I wanted to see and followed up with a subset of those that I absolutely did not want to miss. I requested a schedule that would plan out where I should be to maximize the number of bands I could reasonably see with a simple prompt. 

It understood the mission and in one stroke produced a fantastic spreadsheet optimizing my time and noting my priorities, stages, times, partial sets, if a band has another set, and explained the decision-making rationale.”

How do you use AI? Tell us [here](https://www.videoask.com/ffohxg3vc?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-s-ai-phone-just-jumped-the-line).

### **🎓****[Highlights: News, Guides& Events](https://app.therundown.ai/?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-s-ai-phone-just-jumped-the-line)**

  * Read our last AI newsletter: [AI data centers head for the ocean](https://www.therundown.ai/p/ai-data-centers-head-for-the-ocean?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-s-ai-phone-just-jumped-the-line)

  * Read our last Tech newsletter: [GameStop's wild bid to buy eBay](https://www.rundown.ai/articles/gamestop-wild-bid-to-buy-ebay?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-s-ai-phone-just-jumped-the-line)

  * Read our last Robotics newsletter: [Meta buys a humanoid brain](https://www.rundown.ai/articles/meta-buys-a-humanoid-brain?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-s-ai-phone-just-jumped-the-line)

  * Today’s AI tool guide: [Make your Notion agents more autonomous](https://app.therundown.ai/guides/use-this-hidden-feature-to-make-your-notion-agents-autonomous?utm_source=www.therundown.ai&utm_medium=newsletter&utm_campaign=openai-s-ai-phone-just-jumped-the-line)




See you soon,

_Rowan, Joey, Zach, Shubham, and Jennifer — the humans behind The Rundown_

---

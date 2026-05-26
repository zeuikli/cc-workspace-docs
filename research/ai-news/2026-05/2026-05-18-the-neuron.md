# 🧠 The Neuron — 2026-05-18

> 面向非技術讀者的 AI 日報，3 分鐘讀完
> 來源：[The Neuron](https://rss.beehiiv.com/feeds/N4eCstxvgX.xml)

---

## [😿 AI hackers found a new lane](https://www.theneurondaily.com/p/ai-hackers-found-a-new-lane)
*🧠 The Neuron | 2026-05-17*

Welcome, humans. 

A viral [r/SoftwareLabs post](https://www.reddit.com/r/SoftwareLabs/comments/1tbd6qc/this_chinese_guy_built_agents_in_claude_code_for/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-hackers-found-a-new-lane) claimed one solo operator built a 7-agent Claude Code system that runs cold email campaigns for 38 B2B clients at $3K each. 

The supposed stack: one orchestrator, six sub-agents, MCP servers, Smartlead, Higgsfield, Calendly, a local file system, and an iPhone agent that books meetings on the go.

The comments split into two very internet-native camps: "I need to learn this immediately" and "source: trust me bro." One person did the math and landed at $114K a month. Another replied that believing random financial claims online might be the first problem.

Still, the workflow idea is useful even if the revenue claim is sus: 

  1. One agent owns writes. 

  2. Helper agents do narrow jobs. 

  3. Evals check quality. 

  4. And the human only approves exceptions. 




That is a good pattern for agents. But please, _use responsibly… my LinkedIn can only take so much AI content before it turns it needs to be (insert dirty word no one wants to hear post 2020 global pandemic… ugh fine i’ll just say it) quarantined._

**Here's what happened in AI this week:**

  * 😿 Google found an AI-assisted zero-day exploit.

  * 📰 AISI said Mythos completed two cyber ranges.

  * 📰 TanStack packages were hit by a supply-chain attack.

  * 📰 Microsoft's security agents topped a cyber benchmark.

  * 🌟 Genspark explained its shift from search to agents.




**NEW from The Neuron:** Check out [our full breakdown of Thinking Machines' interaction models](https://www.theneuron.ai/explainer-articles/thinking-machines-wants-ai-to-stop-waiting-its-turn/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-hackers-found-a-new-lane) and what they could enable in time.

**Hey:**_Want to reach 700,000+ AI-hungry readers?_[Advertise with us!](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)_[](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)_

**P.S:**_Love robots? We’re starting a new robotics newsletter!_[Sign up early here](https://form.jotform.com/260897013570156?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-hackers-found-a-new-lane).

# 😿******AI Hit Cybersecurity From Both Sides This Week**

 _Cybersecurity had a very Mr. Robot week, except this time, Rami Malek’s iconic hoodie came with AI agents instead of a split personality of his deceased father. That was a weird show, huh?_

Let’s start with the weird bug. Last week, [Google](https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-hackers-found-a-new-lane) said a criminal threat actor appeared to have used AI to help find and weaponize a zero-day. Zero day means a flaw attackers can use before the developer has a fix for it. This one targeted two-factor authentication, the extra login step that asks for a code or phone approval.

The important part was the shape of the flaw. Google said it came from a hardcoded trust assumption, meaning the system quietly decided a user should be trusted when they should have been checked again. _So it’s fixable, right? Don’t hard code trust!_

**Here’s what else happened:**

  * [TanStack](https://tanstack.com/blog/npm-supply-chain-compromise-postmortem?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-hackers-found-a-new-lane), the company behind popular open-source web development tools, said attackers pushed 84 malicious versions of its software across 42 npm packages. Npm packages are reusable JavaScript code bundles that developers install into apps, which means one poisoned package can travel fast through real products.

    * The attack abused GitHub Actions, the automation system developers use to test and publish code. 

    * That matters because the attackers did not need to steal npm passwords; they went after the trusted publishing machinery around the code instead.

  * Meanwhile, the UK-based [AISI](https://www.aisi.gov.uk/blog/how-fast-is-autonomous-ai-cyber-capability-advancing?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-hackers-found-a-new-lane) organization said frontier models’ autonomous cyber “time horizon” has doubled on the order of months. 

    * So models are getting better at staying on longer hacking tasks without a human steering every step, which is exactly the kind of persistence attackers need to turn one weird flaw into a bigger compromise.

    * A newer Mythos Preview checkpoint (meaning a newer version of the model) made that trend feel less abstract. 

    * It completed “The Last Ones,” a 32-step simulated corporate network attack, in 6/10 attempts, and solved a previously unsolved industrial-control range called “Cooling Tower” in 3/10 attempts. _Wicked fast, bro._




**Why all this matters:** AI changes what attackers are good at looking for. Traditional security tools are great at spotting broken locks: crashes, unsafe memory, sloppy inputs. Models are getting better at tracing the steps a user takes through a system, then spotting the moment the system grants access without checking enough.

That same trust problem gets worse when software moves through packages, scripts, permissions, cache systems, and cloud tokens. Once one trusted link gets poisoned, “bad dependency” can become “stolen credentials” fast. _Hence the term “supply chain attack”; in attacks like the TanStack one, the whole supply chain is poisoned._

So the issue is whether models can keep going through a messy sequence of cyber steps: find a weak point, test it, pivot, and keep moving.

**Enter the defense:**[Microsoft](https://www.microsoft.com/en-us/security/blog/2026/05/12/defense-at-ai-speed-microsofts-new-multi-model-agentic-security-system-tops-leading-industry-benchmark/?utm_source=chatgpt.com) showed off MDASH, its multi-agent vulnerability-finding system, which found 16 Windows bugs, including four critical remote-code execution flaws (those are bugs that can let attackers run code on a target system). 

So instead of handing humans another pile of maybe-bugs, systems like this can audit, debate, and prove which threats are real. Translation: attackers will use AI to find where a system says yes too easily. Defenders will use agents to turn suspicious code into proof, patches, and the team of humans that actually has to fix the thing. 

**FROM OUR PARTNERS**

### The ops hire that onboards in 30 seconds.

[](https://ref.getviktor.com/vik-bh-founders-general1?utm_campaign={{publication_alphanumeric_id}}&_bhiiv=opp_0d871a48-2564-4f86-93f2-72daf980eb4e_58600c56&bhcl_id=02fde40a-cfd3-4781-83c7-7da00aa8fd10_{{subscriber_id}}_{{email_address_id}})

[Viktor](https://ref.getviktor.com/vik-bh-founders-general1?utm_campaign={{publication_alphanumeric_id}}&_bhiiv=opp_0d871a48-2564-4f86-93f2-72daf980eb4e_58600c56&bhcl_id=02fde40a-cfd3-4781-83c7-7da00aa8fd10_{{subscriber_id}}_{{email_address_id}}) is an AI coworker that lives in Slack, right where your team already works.

Message Viktor like a teammate: "pull last quarter's revenue by channel," or "build a dashboard for our board meeting."

Viktor connects to your tools, does the work, and delivers the actual report, spreadsheet, or dashboard. Not a summary. The real thing.

There’s no new software to adopt and no one to train.

Most teams start with one task. Within a week, Viktor is handling half of their ops.

[Add Viktor to Slack for free.](https://ref.getviktor.com/vik-bh-founders-general1?utm_campaign={{publication_alphanumeric_id}}&_bhiiv=opp_0d871a48-2564-4f86-93f2-72daf980eb4e_58600c56&bhcl_id=02fde40a-cfd3-4781-83c7-7da00aa8fd10_{{subscriber_id}}_{{email_address_id}})

# 🎓 **AI Skill of the Day: Run an AI Security Gut Check**

You do not need to be a security engineer to ask better security questions.

**Today's skill:** use AI to run a defensive "gut check" on any workflow where software, customer data, accounts, or automation are involved. The goal is simple: find the places where trust is being assumed.

This is useful because this week's biggest security stories were all about assumptions. A package install assumed the code was safe. A login system assumed a user with partial access could be trusted. A security team assumed old scanning methods could catch new attack patterns.

Copy this into ChatGPT or Claude:
    
    
    Act as a defensive security reviewer.
    
    Review this workflow, system, or automation:
    [PASTE DESCRIPTION]
    
    Look for places where the system assumes trust too early.
    
    Focus on:
    1. User accounts and permissions
    2. Third-party packages or integrations
    3. API keys, tokens, and credentials
    4. Automated actions that could cause damage
    5. Data that should stay private
    6. Approval steps before anything public or irreversible
    7. Monitoring logs I should check regularly
    
    For each risk, explain:
    - What could go wrong
    - Why a normal check might miss it
    - The safest practical fix
    - Whether this needs an expert review
    
    Keep this defensive only. Do not provide exploit steps.
    

**Want more tips like this? Check out our**[**AI Skill of the Day Digest for May**](https://www.theneuron.ai/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-hackers-found-a-new-lane).

**Have a specific skill you want to learn?** [Request it here.](https://docs.google.com/forms/d/e/1FAIpQLSd_-hSXtB9ytR1HQrU85IJnJw233bNKptiGB5BZh9maPse1Eg/viewform?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-hackers-found-a-new-lane)

# 🍪 Treats to Try 

_*Asterisk = from our partners (only the first one!).__[Advertise to 700K+ readers here](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-hackers-found-a-new-lane)_ _!_

  1. *With [Wrike](https://link.technologyadvice.com/r/cpl_wrike_project-management_newsletter_neuron_tertiary?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-hackers-found-a-new-lane), you get award-winning tools that empower collaboration, visibility, and adaptability. [Try for free](https://link.technologyadvice.com/r/cpl_wrike_project-management_newsletter_neuron_tertiary?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-hackers-found-a-new-lane).

  2. [ChatGPT personal finance](https://openai.com/index/personal-finance-chatgpt/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-hackers-found-a-new-lane) lets Pro users in the U.S. connect bank accounts and ask questions about spending, subscriptions, portfolio performance, and goals (Pro preview).

  3. [Microsoft MDASH](https://www.microsoft.com/en-us/security/blog/2026/05/12/defense-at-ai-speed-microsofts-new-multi-model-agentic-security-system-tops-leading-industry-benchmark/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-hackers-found-a-new-lane) uses 100+ specialized agents to find, debate, and prove security bugs across software systems, limited preview.

  4. [WhatsApp Incognito Chat](https://blog.whatsapp.com/introducing-incognito-chat-with-meta-ai-a-completely-private-way-to-chat-with-ai?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-hackers-found-a-new-lane) lets you chat with Meta AI in a privacy-preserving mode where Meta says it cannot access your questions or answers. 

  5. [Alexa for Shopping](https://www.amazon.com/b?node=216450446011&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-hackers-found-a-new-lane) brings Amazon's shopping assistant into the search bar so you can ask product, reorder, and recommendation questions ([read more](https://www.aboutamazon.com/news/retail/alexa-for-shopping-ai-assistant?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-hackers-found-a-new-lane)).

  6. [OpenEvidence](https://www.openevidence.com/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-hackers-found-a-new-lane) gives physicians an AI medical reference tool that checks doctor credentials before access. 

  7. [TinyPPO Snake](https://ppo.gradexp.xyz/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-hackers-found-a-new-lane) runs a live neural-net Snake training demo in your browser, turning PPO and WebGPU into something you can actually watch learn; [HN thread](https://news.ycombinator.com/item?id=48136981&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-hackers-found-a-new-lane); free to try.




# NEW: How real businesses are already using Genspark like an AI employee.

[](https://youtu.be/9Dkxd9rk1mw?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-hackers-found-a-new-lane)

Click to watch on YouTube!

In our **latest podcast episode** , Wen Sang, co-founder and COO of [Genspark](https://www.genspark.ai/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-hackers-found-a-new-lane), showed what AI agents look like when they move from demos to actual work.

He walked through building a VC pitch deck live, then shared how customers are already using it across consulting, advertising, real estate, sales ops, banking, insurance, oil and gas, government, dev shops, and marketing teams.

**The wildest example:** one power user runs a **600-agent sales business** through a Genspark Claw agent named “Goose,” and spends **$2K/month** on Genspark credits because it helps him make more money.

**The big idea:** You can now run a services business with software thanks to agents. Your agent learns the tools, connects the apps, remembers the context, and pushes work toward a finished output.

**Watch and/or Listen:** [YouTube](https://youtu.be/9Dkxd9rk1mw?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-hackers-found-a-new-lane) | [Spotify](https://open.spotify.com/episode/4c9lVJI2OIb7RDEglWLX1S?si=HSvnm5iRTwWsgyWmt-7qhQ&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-hackers-found-a-new-lane) | [Apple Podcasts](https://podcasts.apple.com/us/podcast/inside-genspark-%240-to-%24250m-arr-in-12-months-with-wen-sang/id1742267001?i=1000767644840&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-hackers-found-a-new-lane)

# 📰 Around the Horn 

  * [Apple](https://techcrunch.com/2026/05/17/apples-siri-revamp-could-include-auto-deleting-chats/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-hackers-found-a-new-lane) is reportedly planning a privacy-focused Siri revamp with auto-deleting chats and a standalone Siri chat app powered by Google Gemini.

  * [Malta](https://thenextweb.com/news/openai-malta-chatgpt-plus-free-citizens?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-hackers-found-a-new-lane) became the first country to offer every citizen free ChatGPT Plus after completing an AI literacy course.

  * [Bloomberg](https://www.bloomberg.com/news/articles/2026-05-15/us-is-starting-to-see-heavy-job-losses-in-roles-exposed-to-ai?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-hackers-found-a-new-lane) reported a second year of job losses (0.2% drop) across 18 AI-exposed roles like customer service, sales, and secretarial work (worth about 10M jobs in 2025); meanwhile, overall employment is up 0.8%. 

    * _If this 4 to 1 ratio growth-to-loss ratio holds, the overall jobs picture post AGI is maybe okay? The crummy part about the overall job market tho is just because jobs exist, doesn’t mean the new ones are jobs you are qualified for / want to do…_

  * [The Information](https://www.theinformation.com/articles/anthropic-openais-share-ai-startup-revenues-rises-89?rc=lks9on&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-hackers-found-a-new-lane) reported that 34 top AI startups doubled revenue in six months to roughly $80B ARR _(~$6.7B per month)_ , but 89% of that money (_~$5.93B/month)_ still flows to Anthropic and OpenAI.

  * [ProgramBench](https://programbench.com/blog/gpt-5-5-first-solve/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-hackers-found-a-new-lane) said GPT-5.5 became the first model to fully solve one of its coding benchmark instances.




**FROM OUR PARTNERS**

[](https://www.cloudbees.com/agentic-devops-world?utm_campaign=global-agentic-devops-world&utm_medium=email&utm_source=neuron&utm_content=native-ad-2)

AI coding tools are scaling fast. So are the costs, and most teams can't explain them to the CFO. Join us at [Agentic DevOps World on May 19](https://www.cloudbees.com/agentic-devops-world?utm_campaign=global-agentic-devops-world&utm_medium=email&utm_source=neuron&utm_content=native-ad-2) for live data and real answers on AI at enterprise scale.

[Register now](https://www.cloudbees.com/agentic-devops-world?utm_campaign=global-agentic-devops-world&utm_medium=email&utm_source=neuron&utm_content=native-ad-2)

# 🌟******Sunday Special: Top of the Week**

Here are the top 5 stories and top 5 tools from last week; to catch up on everything that happened this week, read our [Week in Review Around the Horn Digest here](https://theneuron.ai/explainer-articles/around-the-horn-week-in-review-everything-that-happened-in-ai-this-week-may-11-15-2026/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-hackers-found-a-new-lane). 

## Top 5 News Stories

  * [Anthropic reportedly refused China access to Mythos](https://www.nytimes.com/2026/05/12/us/politics/china-ai-anthropic-openai-mythos-chatgpt.html?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-hackers-found-a-new-lane), turning frontier-model access into a visible U.S.-China diplomacy fight.

  * [Cerebras upsized its IPO](https://www.bloomberg.com/news/articles/2026-05-11/ai-chipmaker-cerebras-systems-seeks-4-8-billion-in-upsized-ipo?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-hackers-found-a-new-lane), seeking up to $4.8B as AI compute demand kept pushing infrastructure valuations higher.

  * [Recursive Superintelligence raised $650M](https://www.nytimes.com/2026/05/13/technology/recursive-superintelligence-funding-ai.html?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-hackers-found-a-new-lane) to build systems that automate the creation of better AI systems.

  * [Google confirmed criminal AI-driven zero-day exploitation](https://cloud.google.com/blog/topics/threat-intelligence/ai-vulnerability-exploitation-initial-access?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-hackers-found-a-new-lane), marking a major real-world escalation for AI-assisted cyberattacks.

  * [Claude Code added Agent View](https://claude.com/blog/agent-view-in-claude-code?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-hackers-found-a-new-lane), giving developers one place to manage parallel coding-agent sessions.




## Top 5 New Tool Launches

  1. [OpenAI Daybreak](https://openai.com/daybreak/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-hackers-found-a-new-lane): Uses GPT-5.5 and Codex Security to find threats, generate patches, and verify remediation across code and systems.

  2. [Claude Code Agent View](https://claude.com/blog/agent-view-in-claude-code?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-hackers-found-a-new-lane): Gives developers one place to manage parallel Claude Code sessions, unblock agents, and jump between running tasks.

  3. [Kimi WebBridge](https://www.kimi.com/features/webbridge?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-hackers-found-a-new-lane): Connects Kimi's desktop agent to your browser so it can research, click, fill forms, and compare options locally.

  4. [OpenAI Codex Plugin For Claude Code](https://github.com/openai/codex-plugin-cc?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-hackers-found-a-new-lane): Lets developers run Codex inside Claude Code for reviews, adversarial checks, and background coding tasks.

  5. [Velo 2.0](https://www.usevelo.ai/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-hackers-found-a-new-lane) turns a raw screen recording into a polished video and written doc, then lets you edit both by chat.




# A Cat’s Commentary 

| That’s all for now.   
---|---  
  
**P.P.S:** Love the newsletter, but only want to get it once per week? Don’t unsubscribe—[update your preferences here](https://www.theneurondaily.com/subscribe/f5596641-9099-4045-9641-731cd9fdcf90/preferences?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=ai-hackers-found-a-new-lane).

---

## [😸 The AI Cold War got a protocol](https://www.theneurondaily.com/p/the-ai-cold-war-got-a-protocol)
*🧠 The Neuron | 2026-05-15*

Welcome, humans. 

So apparently someone on X posted a [real Monet painting](https://www.reddit.com/r/singularity/comments/1td046p/twitter_user_posts_a_real_monet_and_says_its_ai/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=the-ai-cold-war-got-a-protocol) and told people it was AI, which immediately turned the internet into an emergency Art Criticism symposium. 

The comments did exactly what you would expect: people found “slop,“ “no soul,“ weird textures, fake passion, and all the usual signs of a machine-made image. One Redditor summed it up perfectly: “ _All of a sudden everyone's an expert on impressionism.“_

Another pointed out the best part: the original poster basically prompted people to “describe in detail“ why it was inferior… _and they returned the most likely tokens._

The real lesson: AI has made people suspicious of everything, but confidence still seems to ship with no fact-checking layer. We have invented the world's first reverse Turing test, where humans prove they are human by hallucinating they are art critics.

**Here’s what happened in AI today:**

  * 😸 U.S.-China AI talks started as Trump met Xi.

  * 😸 OpenAI put Codex inside the ChatGPT mobile app.

  * 📰 OpenAI's Apple partnership reportedly started souring.

  * 📰 Marvel layoffs pointed to Hollywood's AI shift.

  * 🎓 Agent hooks and goals showed where real AI work is heading.




…[and a whole lot more that you can read about here](https://theneuron.ai/explainer-articles/everything-that-happened-in-ai-today-wednesday-thursday-may-14-2026/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=the-ai-cold-war-got-a-protocol).

**Hey:** Want to reach **700,000+** AI-hungry readers? [Advertise with us! ](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)

**Quick plug:** Corey made another [guest appearance on ](https://open.spotify.com/episode/1uzKBAj0PNS5ijgdBPHzWt?si=6bzjQvKnQuKRjGG1zYcEUA&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=the-ai-cold-war-got-a-protocol)_[The AI Fix](https://open.spotify.com/episode/1uzKBAj0PNS5ijgdBPHzWt?si=6bzjQvKnQuKRjGG1zYcEUA&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=the-ai-cold-war-got-a-protocol)_ , where he attempts to answer the age old question: _" will AI keep us as pets or turn us into batteries?”_ Good luck with that one! _Although if Corey were a battery, we bet he’d be a solid state one!_

# 😸 Thursday in an AI Nutshell: Trump and Xi Talked AI Rules While Codex Went Mobile

Two stories caught our attention today besides all the cybersecurity stuff (_there’s… a lot)_ that we’re going to deep dive on this Sunday _(def tune in for that!)_

In Beijing, President Trump and President Xi kicked off a two-day summit covering trade, Taiwan, rare earths, tariffs, high-tech exports, and most importantly (_to this outlet, anyway):_ AI.

Meanwhile, back in the US, OpenAI announced [Codex is coming to the ChatGPT mobile app](https://openai.com/index/work-with-codex-from-anywhere/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=the-ai-cold-war-got-a-protocol), so developers can monitor, steer, and approve coding agents from their phones.

**Here’s what happened in the Trump/Xi meeting:**

  * Treasury Secretary Scott Bessent [told CNBC ](https://www.cnbc.com/2026/05/14/us-china-ai-rules-bessent-us-lead.html?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=the-ai-cold-war-got-a-protocol)that the U.S. and China plan to set up a safety protocol for AI.

  * Bessent said the U.S. and China are setting up an AI safety protocol because the U.S. is “in the lead.”

  * The protocol focuses on “best practices” for frontier models, especially preventing powerful AI from reaching nonstate actors.

    * _So what’s a nonstate actor?_ That means groups outside government control, like criminal hacking networks or extremist groups.

  * Bessent pointed to Anthropic’s new Mythos model as one reason Washington is nervous about AI cyber capabilities.

  * He also predicted a “step-function jump” from upcoming Google Gemini and OpenAI model releases.

  * Nvidia CEO Jensen Huang joined Trump’s China delegation as U.S. H200 chip sales to major Chinese firms remain stuck in “a lot of back-and-forth.”

  * Importantly, [Xi warned Trump](https://www.cnbc.com/2026/05/14/trump-xi-beijing-summit-trade-taiwan-ai-iran-rare-earths-tariffs.html?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=the-ai-cold-war-got-a-protocol) that mishandling Taiwan could put U.S.-China relations in “great jeopardy.”

  * One key thing: The summit could help stabilize last year’s [one-year trade truce](https://www.cnbc.com/2025/10/30/trump-xi-south-korea-rare-earth-tariff-trade-war-nvidia.html?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=the-ai-cold-war-got-a-protocol) around rare earths, tariffs, agricultural purchases, fentanyl cooperation, and high-tech export controls.




**Now here’s what happened with Codex:**

  * OpenAI brought Codex to iOS and Android in preview across ChatGPT plans.

  * More than **4M people** now use Codex every week.

  * Codex mobile lets you review active threads, screenshots, terminal output, code diffs, test results, and approvals from your phone.

  * The work runs remotely in the environment where the project lives, like a laptop, Mac mini, or managed remote workspace.

  * OpenAI also added Remote SSH, Hooks, programmatic access tokens for Business and Enterprise, and HIPAA-compliant local use for eligible Enterprise healthcare workspaces.




**Why this matters:** The diplomacy story is about preventing the [Thucydides Trap](https://en.wikipedia.org/wiki/Thucydides_Trap?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=the-ai-cold-war-got-a-protocol). That is the political-science idea that war risk rises when a rising power threatens to displace an established power. In AI, the trap looks like this: one side fears falling behind, so both sides race harder, share less, and treat safety coordination as weakness.

That is why even boring-sounding “best practices” talks matter. A safety protocol will not solve Taiwan, chips, rare earths, or military competition. But it could still create one narrow lane where both governments agree that autonomous weapons, model misuse, and surprise capability jumps need guardrails.

Now on the Codex side, why should YOU (a non-engineer) care about this? Because developers are the preview for how normal people will use agents 12-18 months later. Dev tools get the weird power-user features first, and then they become everyday buttons for normies.

**Hooks are the best example:**

  * A /hook is a rule that runs at the right moment. 

  * Today, a developer can use one to scan for secrets, run validators, create memories, or customize Codex behavior by project. 

  * Tomorrow, a normal person could use the same pattern for just-in-time skills: 

    * "Before sending an email, check whether I sound too harsh."

    * "Before booking travel, check my budget.”

    * “Before filing an expense, attach the right receipt and categorize it correctly."




**Goal-style workflows point the same way:**

  * A /goal tells an agent what "done" means, then lets it work for longer without needing a prompt every five minutes. 

  * For normal people, that looks like: 

    * "Plan the family trip, compare three options, watch prices for a week, and only ask me when it is time to book."

    * "Clean up my inbox, draft replies, and stop when anything sounds legally sensitive."




**Our take:** The big AI shift is continuity. Governments need continuity so rivalry doesn’t turn every new model into a crisis. Workers need continuity so we can trust our agents when we give over more control to the machines.

That makes Thursday's stories feel connected. One was about keeping the AI race from running off the road. The other was about letting an agent keep working while you are away from your desk. Different stakes, same question: _how do humans stay meaningfully in the loop, but at a comfortable arm’s length?_

FROM OUR PARTNERS 

### Stop forgetting what you agreed to

[](http://granola.ai/?utm_campaign={{publication_alphanumeric_id}}&utm_source=beehiiv&_bhiiv=opp_2062d7bc-ba77-409a-b0ed-1bb366cb8d7a_03f8bfd5&bhcl_id=a62d064b-0dd5-457d-b449-1a52b2b8d6df_{{subscriber_id}}_{{email_address_id}})

You know that feeling when you leave a meeting and immediately forget half of what you promised?

That’s not a memory problem. It’s a meetings problem.

[Granola](http://granola.ai/?utm_campaign={{publication_alphanumeric_id}}&utm_source=beehiiv&_bhiiv=opp_2062d7bc-ba77-409a-b0ed-1bb366cb8d7a_03f8bfd5&bhcl_id=a62d064b-0dd5-457d-b449-1a52b2b8d6df_{{subscriber_id}}_{{email_address_id}}) helps you become the person who actually follows through. Take quick notes during the call; nothing formal. Granola transcribes in the background and turns those notes into clear summaries with real next steps.

After the call, share notes with the team so everyone’s aligned. Or chat with them to pull out exactly what needs to happen next.

No more dropped balls. Just clarity and follow-through.

[Download Granola free](http://granola.ai/?utm_campaign={{publication_alphanumeric_id}}&utm_source=beehiiv&_bhiiv=opp_2062d7bc-ba77-409a-b0ed-1bb366cb8d7a_03f8bfd5&bhcl_id=a62d064b-0dd5-457d-b449-1a52b2b8d6df_{{subscriber_id}}_{{email_address_id}})

# 🎓 AI Skill of the Day: Design Goals and Hooks for Normal Work

The best agent workflows have two ingredients: a goal that defines "done" and hooks that keep the agent consistent while it works.

A goal is the finish line. A hook is a just-in-time rule that runs at the right moment. Developers use these for code checks, tests, and project rules. You can use the same pattern for normal work: trip planning, research, inbox cleanup, budget reviews, meeting prep, and anything else that requires multiple steps.

Copy this:
    
    
    Help me turn this task into a long-running agent workflow:
    
    [TASK]
    
    Define:
    
    1. The goal: what counts as done, in concrete terms.
    
    2. The checkpoints: where the agent should stop and ask me.
    
    3. The hooks: rules that should run automatically at the right moments.
    
    4. The risky steps: anything public, expensive, irreversible, sensitive, or customer-facing.
    
    5. The progress updates: what I should see while the work is running.
    
    Make it useful for a normal person, not a developer.
    
    Give examples of hooks I can use for this exact task.
    
    Favorite insight: agents get useful when they know when to continue, when to check themselves, and when to bother you.

**Want more tips like this?** Check out our [AI Skill of the Day Digest for May](https://www.theneuron.ai/explainer-articles/ai-skill-of-the-day-digest-may-2026/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=the-ai-cold-war-got-a-protocol).

**Have a specific skill you want to learn?** [Request it here.](https://docs.google.com/forms/d/e/1FAIpQLSd_-hSXtB9ytR1HQrU85IJnJw233bNKptiGB5BZh9maPse1Eg/viewform?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=the-ai-cold-war-got-a-protocol)

# 🍪 Treats to Try 

_*Asterisk = from our partners (only the first one!).__[Advertise to 700K+ readers here](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=the-ai-cold-war-got-a-protocol)_ _!_

  1. *[Pipedrive](https://link.technologyadvice.com/r/cpl_pipedrive_crm_newsletter_neuron_tertiary?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=the-ai-cold-war-got-a-protocol) is an easy-to-use sales CRM tool that empowers teams of all sizes to close more deals. [Try it Free](https://link.technologyadvice.com/r/cpl_pipedrive_crm_newsletter_neuron_tertiary?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=the-ai-cold-war-got-a-protocol).

  2. [Codex in ChatGPT mobile](https://openai.com/index/work-with-codex-from-anywhere/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=the-ai-cold-war-got-a-protocol) helps you steer coding tasks from your phone, review changes, approve commands, and keep long-running work moving while your laptop does the heavy lifting, pricing: included across all ChatGPT plans.

  3. [Kimi WebBridge](https://www.kimi.com/features/webbridge?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=the-ai-cold-war-got-a-protocol) connects Kimi’s desktop agent to your browser so it can click, fill forms, compare flights, research jobs, and complete web tasks locally, pricing: free to try.

  4. [Printing Press](https://printingpress.dev/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=the-ai-cold-war-got-a-protocol) turns an API spec, website, or community project into a Go CLI, Claude Code skill, OpenClaw skill, and MCP server so your agents can actually use it.

  5. [AtomicChat](https://atomic.chat/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=the-ai-cold-war-got-a-protocol) lets you run Qwen, Kimi, LLaMA, DeepSeek, and other models locally on your machine for private chats without sending everything to the cloud, pricing: free to try.

  6. [Tavus Image-to-Replica](https://www.tavus.io/post/introducing-image-to-replica?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=the-ai-cold-war-got-a-protocol) turns one photo, portrait, illustration, or mascot into a usable AI human for real-time video, emotional control, and streaming conversations.




# NEW from The Neuron: The Startup Trying to End Busy Work…

[](https://youtu.be/9Dkxd9rk1mw?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=the-ai-cold-war-got-a-protocol)

In our [latest podcast episode](https://youtu.be/9Dkxd9rk1mw?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=the-ai-cold-war-got-a-protocol), Corey and Grant sit down with Wen Sang, co-founder and COO of [Genspark](https://www.genspark.ai/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=the-ai-cold-war-got-a-protocol), to unpack how AI is moving from “answer my question” to “finish the work,” with agents that can build decks, research customers, operate software, remember preferences, and run on a cloud computer for you.

**Watch and/or Listen:**[YouTube](https://youtu.be/9Dkxd9rk1mw?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=the-ai-cold-war-got-a-protocol) | [Spotify](https://open.spotify.com/episode/4c9lVJI2OIb7RDEglWLX1S?si=HSvnm5iRTwWsgyWmt-7qhQ&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=the-ai-cold-war-got-a-protocol) | [Apple Podcasts](https://podcasts.apple.com/us/podcast/the-neuron-ai-explained/id1742267001?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=the-ai-cold-war-got-a-protocol)

# 📰 Around the Horn 

[](https://x.com/Figure_robot/status/2054971079030968549?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=the-ai-cold-war-got-a-protocol)

These robots from Figure are kinda mesmerizing to watch… its also funny when it sometimes just chucks one off the conveyor belt for no good reason; been there! 

  * [The Information](https://www.theinformation.com/articles/openais-apple-partnership-sours?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=the-ai-cold-war-got-a-protocol) reported OpenAI is considering legal action against Apple after Apple allegedly limited ChatGPT's iOS role, buried the feature, then started getting cozy with Google and Anthropic for similar AI features. Bold strategy: invite OpenAI to the group project, make it do the bibliography, then ask Gemini to present.

  * [Cerebras](https://www.cnbc.com/2026/05/14/cerebras-ipo-mints-two-billionaires-sets-stage-for-potential-ai-wave.html?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=the-ai-cold-war-got-a-protocol) (the [AI chip company](https://www.theneurondaily.com/p/cerebras-to-ipo-at-33b-take-on-nvidia?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=the-ai-cold-war-got-a-protocol)) minted two new billionaires in its IPO, with shares priced at $185, opening at $350, and closing up 68% at $311.07, a debut that could kick off a wider wave of AI companies racing to public markets

  * [Marvel layoffs](https://www.techrepublic.com/article/news-marvel-layoffs-ai-hollywood-animation/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=the-ai-cold-war-got-a-protocol) reflect Hollywood's broader shift toward freelancers, AI tools, and less predictable creative pipelines, according to former Disney animator Tom Bancroft ([video](https://www.youtube.com/watch?v=QX-FQz-uxwQ&t=3s&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=the-ai-cold-war-got-a-protocol)).

  * [PwC](https://www.businessinsider.com/anthropic-pwc-big-four-business-ai-adoption-2026-5?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=the-ai-cold-war-got-a-protocol) expanded its Anthropic alliance and plans to train 30K U.S. employees in Claude Code.

  * [A tire-changing robot](https://www.axios.com/2026/05/14/ai-robot-tire-change?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=the-ai-cold-war-got-a-protocol) showed how robotics is starting with the most annoying errands first. Respectfully, let it have the lug nuts.




**FROM OUR PARTNERS**

### The IT strategy every team needs for 2026

[](https://www.deel.com/resources/it-strategy-toolkit-2026-guide-hr-leaders/?utm_medium=sponsored-newsletter&utm_source=beehiiv&utm_term={{publication_alphanumeric_id}}&utm_campaign=ww_engage_download_beehiiv_sponnewsletter_it-ttrends2026-feb26_it_all&utm_content=engage_it_sponnewsletter_ittrends2026-sponnews400-it_en&_bhiiv=opp_63157cd6-3c5f-4108-846d-581d06dad4f7_28664f41&bhcl_id=07e4a394-b6a7-4007-a8e6-ae9dc6ea4c43_{{subscriber_id}}_{{email_address_id}})

2026 will redefine IT as a strategic driver of global growth. Automation, AI-driven support, unified platforms, and zero-trust security are becoming standard, especially for distributed teams. This [toolkit](https://www.deel.com/resources/it-strategy-toolkit-2026-guide-hr-leaders/?utm_medium=sponsored-newsletter&utm_source=beehiiv&utm_term={{publication_alphanumeric_id}}&utm_campaign=ww_engage_download_beehiiv_sponnewsletter_it-ttrends2026-feb26_it_all&utm_content=engage_it_sponnewsletter_ittrends2026-sponnews400-it_en&_bhiiv=opp_63157cd6-3c5f-4108-846d-581d06dad4f7_28664f41&bhcl_id=07e4a394-b6a7-4007-a8e6-ae9dc6ea4c43_{{subscriber_id}}_{{email_address_id}}) helps IT and HR leaders assess readiness, define goals, and build a scalable, audit-ready IT strategy for the year ahead. Learn what’s changing and how to prepare.

[Download the Toolkit](https://www.deel.com/resources/it-strategy-toolkit-2026-guide-hr-leaders/?utm_medium=sponsored-newsletter&utm_source=beehiiv&utm_term={{publication_alphanumeric_id}}&utm_campaign=ww_engage_download_beehiiv_sponnewsletter_it-ttrends2026-feb26_it_all&utm_content=engage_it_sponnewsletter_ittrends2026-sponnews400-it_en&_bhiiv=opp_63157cd6-3c5f-4108-846d-581d06dad4f7_28664f41&bhcl_id=07e4a394-b6a7-4007-a8e6-ae9dc6ea4c43_{{subscriber_id}}_{{email_address_id}})

# 💡 Intelligent Insights:

  1. [Brandon Stewart](https://www.nature.com/articles/s41586-026-10506-7?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=the-ai-cold-war-got-a-protocol) shows that government-controlled media already shapes LLM outputs through training data, with models showing stronger pro-regime bias in languages from countries with lower freedom of the press.

  2. [Lujain Ibrahim](https://arxiv.org/abs/2605.07912?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=the-ai-cold-war-got-a-protocol) finds that sycophantic AI makes real human interaction feel more effortful and less satisfying over time, because validation from chatbots quietly changes what people expect from friends and family.

  3. [UK AISI reports](https://www.aisi.gov.uk/blog/how-fast-is-autonomous-ai-cyber-capability-advancing?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=the-ai-cold-war-got-a-protocol) that frontier models’ autonomous cyber-task horizons are doubling every few months, with recent models beating earlier trendlines and completing longer tasks than expected.

  4. [Microsoft Research demonstrated](https://www.microsoft.com/en-us/research/articles/whimsical-strategies-break-ai-agents-generating-out-of-distribution-adversarial-strategies-at-scale/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=the-ai-cold-war-got-a-protocol) that “whimsical” adversarial strategies can break AI agents because weird, out-of-distribution tactics expose failure modes standard safety tests miss.

  5. [Ryan Greenblatt proposed](https://www.lesswrong.com/posts/FG54euEAesRkSZuJN/ryan_greenblatt-s-shortform?commentId=DX8FyduiHxnSc6Cof&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=the-ai-cold-war-got-a-protocol) that AI labs run deliberate misalignment training experiments now, including pessimization runs and clean chain-of-thought baselines, so they can study dangerous failure modes before models get much stronger.

  6. [Gallup](https://news.gallup.com/poll/709772/americans-oppose-data-centers-area.aspx?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=the-ai-cold-war-got-a-protocol) found 7 in 10 Americans oppose AI data centers in their local area, including 48% who are strongly opposed, making data centers even less popular nearby than nuclear plants as compute demand becomes a local political fight.




# A Cat’s Commentary 

| That’s all for now.   
---|---  
  
**P.P.S:** Love the newsletter, but only want to get it once per week? Don’t unsubscribe—[update your preferences here](https://www.theneurondaily.com/subscribe/f5596641-9099-4045-9641-731cd9fdcf90/preferences?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=the-ai-cold-war-got-a-protocol).

---

## [😺 🎙️ Watch: The Startup Trying to End Busywork](https://www.theneurondaily.com/p/watch-the-startup-trying-to-end-busywork)
*🧠 The Neuron | 2026-05-14*

[](https://youtu.be/9Dkxd9rk1mw?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-the-startup-trying-to-end-busywork)

Click the image above to watch on YouTube!

Welcome, humans.

For the last two years, AI has mostly meant one thing: you ask a chatbot a question, it gives you an answer, and then **you still have to do the work**.

[Genspark](https://www.genspark.ai/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-the-startup-trying-to-end-busywork) is betting that phase is ending.

In our latest podcast episode, we sit down with [**Wen Sang, co-founder and COO of Genspark AI**](https://www.linkedin.com/in/wen-sang?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-the-startup-trying-to-end-busywork), to talk about the jump from AI search to AI agents that can actually finish tasks: build slide decks, research prospects, write docs, run workflows, use your software, connect to your apps, and even operate a cloud computer on your behalf.

Basically, AI that goes beyond “give me ideas for a pitch deck.” Think of it more like, “Research this VC, learn what kind of decks they like, build the deck, make it look good, and hand me the finished thing.”

Which Wen did live during the interview. _Super casual_.

[](https://youtu.be/9Dkxd9rk1mw?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-the-startup-trying-to-end-busywork)

Click the image above to watch on YouTube!

# Our favorite moments:

  * **(**[**2:04**](https://www.youtube.com/watch?v=9Dkxd9rk1mw&t=124s&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-the-startup-trying-to-end-busywork)**) Why AI search wasn’t the final form:** Wen explains why Genspark started with AI search, then realized people don’t just want information—they want the work that information enables.

  * **(**[**5:07**](https://www.youtube.com/watch?v=9Dkxd9rk1mw&t=307s&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-the-startup-trying-to-end-busywork)**) $0 to $250M ARR in 12 months:** Wen walks through Genspark’s absurd growth curve, from the first paid users to $100M ARR, then another $100M two months later, then another $50M in March.

  * **(**[**6:24**](https://www.youtube.com/watch?v=9Dkxd9rk1mw&t=384s&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-the-startup-trying-to-end-busywork)**) The Super Bowl ad effect:** After proving the signal was real, Genspark bought a Super Bowl commercial—and Wen says web search traffic jumped 6,000%.

  * **(**[**7:56**](https://www.youtube.com/watch?v=9Dkxd9rk1mw&t=476s&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-the-startup-trying-to-end-busywork)**) Live demo: Workspace 4.0 builds a pitch deck:** Wen asks Genspark to research a VC’s deck preferences and build a splashy fundraising deck for The Neuron, live, in seconds.

  * **(**[**16:13**](https://www.youtube.com/watch?v=9Dkxd9rk1mw&t=973s&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-the-startup-trying-to-end-busywork)**) Meet “Goose”: A power user spending $2K/month:** Wen tells the story of a sales operator who built his business around a Genspark Claw agent named Goose—and happily spends $2,000/month because it makes him more money.

  * **(**[**20:07**](https://www.youtube.com/watch?v=9Dkxd9rk1mw&t=1207s&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-the-startup-trying-to-end-busywork)**) Software becomes infrastructure, agents become the interface:** Wen lays out the big shift: instead of humans learning 30 different tools, agents learn the tools and operate them for us.

  * **(**[**25:01**](https://www.youtube.com/watch?v=9Dkxd9rk1mw&t=1501s&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-the-startup-trying-to-end-busywork)**) What is OpenClaw?:** Wen explains the move from one-off AI chats to long-memory agents that follow you across Slack, WhatsApp, Telegram, Teams, browsers, and computers.

  * **(**[**26:47**](https://www.youtube.com/watch?v=9Dkxd9rk1mw&t=1607s&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-the-startup-trying-to-end-busywork)**) Genspark Claw: Your AI in the cloud:** Instead of asking normal users to configure servers, scripts, and API keys, Genspark gives them a cloud computer where their agent can work.

  * **(**[**37:54**](https://www.youtube.com/watch?v=9Dkxd9rk1mw&t=2274s&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-the-startup-trying-to-end-busywork)**) 100% of Genspark’s code is now written by AI:** Wen says Genspark is using AI to build Genspark, letting tiny teams ship at the speed of an individual.

  * **(**[**39:22**](https://www.youtube.com/watch?v=9Dkxd9rk1mw&t=2362s&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-the-startup-trying-to-end-busywork)**) The 3-year vision: Humans don’t have to work:** Wen shares the bigger mission: autopilot the busywork so people can choose whether they want to hustle, earn more, or simply get more of their life back.




**Why watch this?** Because “AI agents” is one of the most overused phrases in tech right now, and this episode makes it concrete.

You can actually see what Genspark means by agents: not just a chatbot with a new label, but a system that plans, picks tools, writes code, creates files, opens websites, remembers preferences, and pushes toward a finished output.

If you’ve been wondering when AI assistants become something closer to AI coworkers, or what has to be true before businesses trust them with real work, this is the episode.

**Watch and/or listen now:** [YouTube](https://youtu.be/9Dkxd9rk1mw?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-the-startup-trying-to-end-busywork) | [Spotify](https://open.spotify.com/episode/4c9lVJI2OIb7RDEglWLX1S?si=HSvnm5iRTwWsgyWmt-7qhQ&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-the-startup-trying-to-end-busywork)

**P.S.** At **(12:23)** Wen drops one of our favorite metaphors for the agent era: LLMs are smart, but by themselves they’re “brains” without arms and legs. The next wave is about giving those brains tools, memory, and access to the software where work actually happens.

Dive deeper with these resources:

  * [Genspark.ai](https://Genspark.ai?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-the-startup-trying-to-end-busywork)

  * [The Neuron AI Explained podcast](https://www.youtube.com/@theneuronai?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-the-startup-trying-to-end-busywork)




 _**Real quick:**__Want to see your AI-adjacent product or service show up right here, below these podcast promos? Click the button below to advertise to our 700K+ readers!_

[_Advertise in The Neuron here!_](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-the-startup-trying-to-end-busywork)

# 🎙️ In Case You Missed It… 

Four recent interviews you’ll definitely want to check out _(pick whatever looks interesting to you and dive in!):_

### 1\. Interested in whether AI can actually design new drugs? Watch: [**Isomorphic Labs Is Trying to Turn AlphaFold Into Medicine. Here’s How.**](https://youtu.be/W0NSk2y3OFI?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-the-startup-trying-to-end-busywork)

[](https://youtu.be/W0NSk2y3OFI?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-the-startup-trying-to-end-busywork)

**TL;DW:** Rebecca Paul, Head of Medicinal Drug Design at [Isomorphic Labs](https://www.isomorphiclabs.com/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-the-startup-trying-to-end-busywork), and Michael Schaarschmidt, Foundational AI Research Lead, explain why drug discovery is still brutally slow, expensive, and failure-prone and how foundation models could help scientists design better drug candidates faster. Their big point: “AI-designed drugs” are not one magic model. It takes many models working together across biology, chemistry, structure prediction, molecule generation, and human judgment.

**Why you should watch:** If you’ve ever wondered what comes _after_ [AlphaFold](https://deepmind.google/science/alphafold/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-the-startup-trying-to-end-busywork), this one gets into it. There’s a great section on how something that once could take an entire PhD to validate experimentally can now sometimes be predicted in seconds or minutes, and a wild bit about the dream of getting from a protein target to a drug candidate in one design cycle. Also: “undruggable” proteins may not stay undruggable forever.

  * **YouTube:** [Watch Here](https://youtu.be/W0NSk2y3OFI?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-the-startup-trying-to-end-busywork)

  * **Spotify:** [Listen Here](https://open.spotify.com/episode/2TzHhOkVIN9AL3GXXxSyDe?si=c5dd0a8104ec4805&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-the-startup-trying-to-end-busywork)

  * **Apple Podcasts:** [Listen Here](https://podcasts.apple.com/us/podcast/can-ai-really-design-new-drugs-google-deepmind-spin/id1742267001?i=1000766512015&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-the-startup-trying-to-end-busywork)




### 2\. Interested in what's missing before we hit AGI? Watch: [This Company Mapped the Entire World in 3D. Here's Why.](https://youtu.be/erCV1MJXU3g?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-the-startup-trying-to-end-busywork)

[](https://youtu.be/erCV1MJXU3g?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-the-startup-trying-to-end-busywork)

**TL;DW:** Peter Wilczynski, CPO at [Vantor](https://vantor.com/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-the-startup-trying-to-end-busywork) (formerly Maxar), built a 3D model of the entire Earth at 50cm resolution and made it machine-readable. He argues spatial intelligence is the gap nobody's talking about in AI, and probably the missing piece before agents can actually operate in the physical world.

**Why you should watch:** If you've ever wondered why AI can write code and solve math olympiad problems but still can't reliably tell a drone where to go, this one answers it. Also, there's a wild bit about how the physical world becomes the new navigation layer for AI agents.

  * **YouTube:** [Watch Here](https://youtu.be/erCV1MJXU3g?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-the-startup-trying-to-end-busywork)

  * **Spotify:** [Listen Here](https://open.spotify.com/episode/71rhDuYFzTlsF0uaIq91QU?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-the-startup-trying-to-end-busywork)

  * **Apple Podcasts:** [Listen Here](https://podcasts.apple.com/us/podcast/this-company-mapped-the-entire-world-in-3d-heres-why/id1742267001?i=1000761587268&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-the-startup-trying-to-end-busywork)




### **3\. Curious how good AI music tools have actually gotten? Watch:**[**This AI Just Made Our Podcast Theme Song**](https://youtu.be/r4aMWjhoMHU?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-the-startup-trying-to-end-busywork)

[](https://youtu.be/vJD2FjVUEhg?si=Mdm2w9GHHSZwZ2A8&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-the-startup-trying-to-end-busywork)

**TL;DW:** Corey sits down with **Kendall Rankin** , who left LinkedIn in 2024 to join [Producer AI](https://www.flowmusic.app/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-the-startup-trying-to-end-busywork) when it was a startup (advised by The Chainsmokers, no less). Google acquired the team in February 2026, and Kendall is now on the Flow Music team inside Google Labs. On the episode, they generate a garage rock song from a single sentence, build a custom synth in the "Spaces" feature, and walk through SynthID watermarking and one-shot music videos.

**Why you should watch:** Most AI music demos hand you a polished finished song and skip the part where things go sideways. This episode is the part where things go sideways. First pass fumbles, Corey asks for "more fuzz," second pass actually lands. That iteration loop is the whole story for anyone trying to figure out if these tools are actually usable.

  * **YouTube:** [Watch Here](https://youtu.be/r4aMWjhoMHU?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-the-startup-trying-to-end-busywork)

  * **Spotify:** [Listen Here](https://open.spotify.com/show/4gF6uNmkzEYq2E0sHeuMuU?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-the-startup-trying-to-end-busywork)

  * **Apple Podcasts:** [Listen Here](https://podcasts.apple.com/us/podcast/the-neuron-ai-explained/id1742267001?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-the-startup-trying-to-end-busywork)




### 4\. Want agents that actually work on real tasks? Watch: [Inside the Secret Labs Where AI Learns to Work](https://youtu.be/WhbdbbERzNg?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-the-startup-trying-to-end-busywork)

[](https://youtu.be/WhbdbbERzNg?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-the-startup-trying-to-end-busywork)

**TL;DW:** Nick Heiner, VP of Product at [Surge AI](https://www.surgehq.ai/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-the-startup-trying-to-end-busywork) (a $1.2B-revenue company built without VC money), reveals why even GPT-5, Claude, and Gemini still fail about 40% of real workplace tasks, what makes a good RL environment, and his bold prediction of a $1B company with one human employee by 2030.

**Why you should watch:** If you're trying to get AI agents to actually finish real work (and not just demo well), this is the missing piece on why they keep falling short.

  * **YouTube:** [Watch Here](https://youtu.be/WhbdbbERzNg?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-the-startup-trying-to-end-busywork)

  * **Spotify:** [Listen Here](https://open.spotify.com/episode/6MAFKIJVL4Gt57lEEqCs6F?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-the-startup-trying-to-end-busywork)

  * **Apple Podcasts:** [Listen Here](https://podcasts.apple.com/us/podcast/inside-the-secret-labs-where-ai-learns-to-work/id1742267001?i=1000757358598&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-the-startup-trying-to-end-busywork)




**Last thing:** And if you **haven’t subscribed yet, please do!** Click the image below to go to our channel and hit “subscribe” to get notified right when new videos go live. 

[](https://www.youtube.com/@theneuronai?sub_confirmation=1&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-the-startup-trying-to-end-busywork)

We have a goal to hit **50K subscribers** by the end of the year (if not 100K), and **we’re only ~30K away!** If you like learning about AI, and already watch some of our videos, [do us a favor and click here to subscribe](https://www.youtube.com/@theneuronai?sub_confirmation=1&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-the-startup-trying-to-end-busywork) today. 

Stay curious,

The Neuron Team

| That’s all for today, for more AI treats, check out our [website](https://www.theneuron.ai/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=watch-the-startup-trying-to-end-busywork).   
---|---  
  
**P.P.S:** Love the newsletter, but don’t want to receive these podcast announcement emails? Don’t unsubscribe — _[adjust your preferences to opt out of them here instead](https://www.theneurondaily.com/subscribe/f5596641-9099-4045-9641-731cd9fdcf90/preferences?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=podcast-first-major-ai-incident-this-year-ceo-warns&_bhlid=1d073d4088b90ea4abf69ef7cc157e0659ada818)_ _._

---

## [😸 Claude is now the #1 business AI](https://www.theneurondaily.com/p/claude-is-now-the-1-business-ai)
*🧠 The Neuron | 2026-05-14*

[](https://rapid-agent.devpost.com/?utm_source=neuron&utm_medium=media_partner&utm_campaign=rapid_agent_hackathon)

Welcome, humans. 

So, over at r/CursedAI, [this apparently exists](https://www.reddit.com/r/CursedAI/comments/1t9totl/jp_morgan_and_the_gilded_age_gauntlet/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=claude-is-now-the-1-business-ai): it’s a note-perfect spoof of Mortal Kombat featuring historic capitalists like JP Morgan, Rockefeller, and Andrew Carnegie, and low-key, this is so much better than it has any right to be: 

[](https://www.reddit.com/r/CursedAI/comments/1t9totl/jp_morgan_and_the_gilded_age_gauntlet/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=claude-is-now-the-1-business-ai)

_who knew the perfect meme for the gilded 2020s would be an AI-generated Mortal Kombat spoof of Industrial Revolution Robber Baron Billionaires beating each other silly with their wealth…_

**Here’s what happened in AI today:**

  * 😺 Anthropic officially overtook OpenAI in business adoption, per Ramp's latest spending data.

  * 📰 Palo Alto warned AI-driven cyberattacks are already becoming the new normal.

  * 📰 Apple is reportedly building AI agent support directly into the App Store.

  * 🍪 Notion launched a developer platform that lets AI agents work inside your workspace.




**Hey:**_Want to reach 700,000+ AI-hungry readers?_[Advertise with us!](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)_[](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)_

**P.S:**_Love robots? We’re starting a new robotics newsletter!_[Sign up early here](https://form.jotform.com/260897013570156?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=claude-is-now-the-1-business-ai).

# 😺******Anthropic Just Passed OpenAI in the One Stat That Actually Matters**

A year ago, OpenAI was "[pulling well ahead of rivals](https://techcrunch.com/2025/05/10/openais-enterprise-adoption-appears-to-be-accelerating-at-the-expense-of-rivals/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=claude-is-now-the-1-business-ai)" in the enterprise race. Per Ramp's May 2025 AI Index (Ramp is an expense management platform that tracks actual corporate credit card spend), OpenAI had 32% of U.S. business adoption. Anthropic? A distant 8%.

That gap is now gone.

[Ramp's May 2026 AI Index](https://ramp.com/leading-indicators/ai-index-may-2026?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=claude-is-now-the-1-business-ai) shows Anthropic at 34.4% of business adoption, crossing OpenAI (now at 32.3%) for the first time ever. All of these came from purchase data from thousands of actual companies.

**Here's what happened:**

  * In May 2025, OpenAI had 32% business adoption; Anthropic had 8%. The gap looked insurmountable.

  * By March 2026, Axios reported Anthropic was [capturing 73% of first-time AI business buyers](https://www.axios.com/2026/03/18/ai-enterprise-revenue-anthropic-openai?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=claude-is-now-the-1-business-ai) and Anthropic's annualized revenue had hit $19B vs. OpenAI's $25B, with Anthropic accelerating faster.

  * The engine behind the reversal: Claude Code, Anthropic's autonomous coding tool, which reached $2.5B in annualized revenue by February 2026 alone.

  * As of April 2026: Anthropic crossed $30B annualized revenue; OpenAI sits at roughly $24B.




OpenAI's response has been swift. Last week, the company [launched a $4B "Deployment Company"](https://www.axios.com/2026/05/04/openai-anthropic-private-equity-enterprise-business?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=claude-is-now-the-1-business-ai) with 19 private equity and consulting partners specifically to fight back, embedding AI engineers inside enterprises to accelerate Codex adoption. Their chief revenue officer [told employees in a memo](https://www.axios.com/2026/04/21/openai-anthropic-enterprise-rivalry-heats-up?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=claude-is-now-the-1-business-ai), per Axios: "the market is as competitive as I have ever seen it."

**Why this matters:** Enterprise contracts are stickier than consumer downloads. They expand over time, renew annually, and get embedded into company infrastructure. When a company approves Claude as a budget line item, switching requires a procurement cycle, not just deleting an app. Anthropic winning here is a different kind of win than getting good press.

**Our take:** The interesting thing about Ramp's data is that Ramp's own economist, Ara Kharazian, published the adoption numbers alongside a bearish note on Anthropic — arguing that Claude is incentivized to push users toward pricier models even when cheaper ones would do. Fair criticism. But "they upsell too well" is a weird thing to complain about when you're losing market share. Both companies are racing toward IPOs that could come as soon as this fall. This data point just changed who's negotiating from a position of strength.

**FROM OUR PARTNERS**

# From Insights to Execution: The Rapid Agent Hackathon

[](https://rapid-agent.devpost.com/?utm_source=neuron&utm_medium=media_partner&utm_campaign=rapid_agent_hackathon)

Stop building simple interfaces. Join the [Google Cloud Rapid Agent Hackathon](https://rapid-agent.devpost.com/?utm_source=neuron&utm_medium=media_partner&utm_campaign=rapid_agent_hackathon) to develop AI agents that autonomously interact with the world.

Focus on real-world utility and turn your code into a business force multiplier by building agents that:

  * Handle Complex Logic: Move beyond chat and perform autonomous tasks.

  * Connect Enterprise Data: Leverage priority ISV integrations for executive-level impact.

  * Scale Seamlessly: Build solutions designed for real-world enterprise adoption.




[Registration is open—build the agent that changes how we work!](https://rapid-agent.devpost.com/?utm_source=neuron&utm_medium=media_partner&utm_campaign=rapid_agent_hackathon)

# 🎓 **AI Skill of the Day: Stop Saving Prompts in Docs. Use Claude Skills Instead**

If you've been copy-pasting your best prompts from a Google Doc every time you need them, YouTube creator [Alex Pereira](https://youtu.be/vuaxy1NLAQ8?si=V-BC8egJiHjoE2Wk&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=claude-is-now-the-1-business-ai) just showed a better way.

Claude has a feature called Skills — reusable instruction sets you install once and trigger with a single slash command, in any chat. Think of it like saving a prompt permanently to Claude's brain. Alex built six of them to run his entire content workflow: hook generator, image creator, video generator, thumbnail builder, face lock (for consistent face generation), and caption writer — all fired with one word.

**How to set one up:**

  1. In Claude, click **Customize** → the **+** button → **Create Skill**

  2. Structure it in three parts: (1) a description + when Claude should trigger it, (2) your instructions, (3) examples of good output

  3. Save it — then type /[skill name] in any chat to activate




Alex's rule for when to bother: the task has to be **recurring, structured, and have a consistent output format**. Passes all three? Build it. Passes one or two? Keep it as a saved prompt.
    
    
    When I type /[skill name], do the following:
    
    Instructions: [What you want Claude to do]
    Format: [Output shape — e.g. 10 hooks, numbered list, under 15 words each]
    Voice rules: [Any style/tone requirements]
    Examples of good output: [Paste 2-3 examples]
    

**Total AI beginner?**[Start here](https://www.theneuron.ai/explainer-articles/everything-we-covered-in-our-ai-for-total-beginners-livestream-full-guide-with-timestamps/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=claude-is-now-the-1-business-ai) ([goes with this video](https://www.youtube.com/live/QbFU0UNMVaU?si=skJsgUIDjKjAx3DU&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=claude-is-now-the-1-business-ai)). 

**Have a specific skill you want to learn?** [Request it here.](https://docs.google.com/forms/d/e/1FAIpQLSd_-hSXtB9ytR1HQrU85IJnJw233bNKptiGB5BZh9maPse1Eg/viewform?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=claude-is-now-the-1-business-ai)

# 🍪 Treats to Try 

  1. [Notion](https://www.notion.com/releases/2026-05-13?utm_source=theneuron) launched a full developer platform (v3.5) that lets you (and your AI coding agents) sync any data source and build custom agent tools, all hosted on Notion's infrastructure. You can also invite Claude, Codex, or your own agents directly into your workspace as collaborators.

  2. [Pipali](https://pipali.ai?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=claude-is-now-the-1-business-ai) is an open-source coworker that lives on your computer and handles real work — research, drafting documents, browser tasks, and recurring errands — with Routines you set once and it runs on a schedule, plus integrations with Slack, Linear, and GitHub via MCP —free to try.

  3. [My AI Front Desk](https://myaifrontdesk.com?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=claude-is-now-the-1-business-ai) gives your small business a 24/7 receptionist that answers every call, fields questions, and books appointments directly into your calendar, even after hours —free to try.

  4. [Genpire](https://genpire.com?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=claude-is-now-the-1-business-ai) turns a product sketch or text description into a factory-ready tech pack in minutes — complete with technical drawings, material specs, and measurements — then connects you to vetted suppliers for quotes and production.

  5. [CraftBot](https://github.com/CraftOS-dev/CraftBot?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=claude-is-now-the-1-business-ai) is a self-hosted personal assistant that runs 24/7 on your own machine, proactively managing tasks like organizing your Google Drive, tracking GitHub issues into Notion, and sourcing leads — you set the goals, it works in the background —free to try.

  6. [Coddo](https://coddo.ai?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=claude-is-now-the-1-business-ai) gives Claude Code a visual interface — a Kanban board where each card is a coding task, with automatic Git branch creation and progress tracking, so you stay at the task level instead of managing a mess of terminal windows —free to try (macOS only for now).

  7. [Pika](https://www.pika.me/mcp?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=claude-is-now-the-1-business-ai) lets you give your Claude a custom face, name, and personality via MCP, then set it loose to handle tasks and create content as a living extension of you.




# Trending: FOUR popular Neuron podcast eps…

Did you know we have a podcast (_The Neuron: AI Explained)_ where we talk to fascinating people in the industry who teach us how it actually works? Check it out: 

[](https://www.youtube.com/@theneuronai/videos?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=claude-is-now-the-1-business-ai)

Click to view these episodes on YouTube!

New episodes air **every week** on: [Spotify](https://open.spotify.com/show/4gF6uNmkzEYq2E0sHeuMuU?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=claude-is-now-the-1-business-ai) | [Apple Podcasts](https://podcasts.apple.com/us/podcast/the-neuron-ai-explained/id1742267001?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=claude-is-now-the-1-business-ai) | [YouTube](https://www.youtube.com/@theneuronai?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=claude-is-now-the-1-business-ai)****

# 📰 Around the Horn 

  * [Palo Alto Networks](https://www.cnbc.com/2026/05/13/palo-alto-ai-cyberattacks-mythos-gpt.html?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=claude-is-now-the-1-business-ai) warned that AI-driven cyberattacks are already becoming the new norm, citing models like Anthropic's Mythos and OpenAI's GPT-5.5-Cyber as raising the stakes for every security team; Google separately said it stopped a recent attempt to use AI for a mass exploitation event.

  * [The UK's AI Safety Institute](https://www.aisi.gov.uk/blog/how-fast-is-autonomous-ai-cyber-capability-advancing?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=claude-is-now-the-1-business-ai) published research showing autonomous AI cyber capability has been doubling roughly every 4.7 months — and the most recent frontier models are outpacing even that accelerating trend.

  * [Apple](https://9to5mac.com/2026/05/13/apple-is-working-to-incorporate-ai-agents-on-the-app-store-per-report/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=claude-is-now-the-1-business-ai) is reportedly building AI agent support into the App Store, with a WWDC announcement expected; it would mean AI agents — not just apps — could eventually be found, downloaded, and run directly from your iPhone.

  * [Google DeepMind](https://deepmind.google/blog/ai-pointer/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=claude-is-now-the-1-business-ai) introduced "AI Pointer," a concept that turns the traditional mouse cursor into a context-aware AI collaborator that understands what's on your screen and can act on it, starting with Chrome.

  * [Baidu's CEO](https://www.morningstar.com/news/pr-newswire/20260513cn58923/baidu-advances-agent-portfolio-to-embrace-the-agent-era-champions-daily-active-agents-as-key-metric?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=claude-is-now-the-1-business-ai) proposed "Daily Active Agents" (DAA) as the defining metric for the AI era — the equivalent of Daily Active Users for the agent world — and predicted global DAA could eventually surpass 10 billion




**FROM OUR PARTNERS**

[](https://www.cloudbees.com/agentic-devops-world?utm_campaign=global-agentic-devops-world&utm_medium=email&utm_source=neuron&utm_content=native-ad-2)

AI coding tools are scaling fast. So are the costs, and most teams can't explain them to the CFO. Join us at [Agentic DevOps World](https://www.cloudbees.com/agentic-devops-world?utm_campaign=global-agentic-devops-world&utm_medium=email&utm_source=neuron&utm_content=native-ad-2) on May 19 for live data and real answers on AI at enterprise scale.

[Register now](https://www.cloudbees.com/agentic-devops-world?utm_campaign=global-agentic-devops-world&utm_medium=email&utm_source=neuron&utm_content=native-ad-2)

# 🧩**Thursday Trivia**

**A.**

**B.**

# A Cat’s Commentary 

| That’s all for now.   
---|---  
  
**P.S:** Before you go… have you [subscribed to our YouTube Channel](https://www.youtube.com/@theneuronai?sub_confirmation=1&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=claude-is-now-the-1-business-ai)? If not, can you? 

[](https://www.youtube.com/@theneuronai?sub_confirmation=1&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=claude-is-now-the-1-business-ai)

Click the image to subscribe! 

**P.P.S:** Love the newsletter, but only want to get it once per week? Don’t unsubscribe—[update your preferences here](https://www.theneurondaily.com/subscribe/f5596641-9099-4045-9641-731cd9fdcf90/preferences?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=claude-is-now-the-1-business-ai).

---

## [😺Google is killing the prompt box](https://www.theneurondaily.com/p/google-is-killing-the-prompt-box)
*🧠 The Neuron | 2026-05-13*

[](https://www.dell.com/en-us/lp/dt/nvidia-ai?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box)

Welcome, humans.

So [this might be the most heavy metal thing we’ve seen all day](https://www.youtube.com/watch?v=oWOyUMJWptc&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box) (_pun heavily intended): the world’s first actual mech suit transformer._

[](https://www.youtube.com/watch?v=oWOyUMJWptc&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box)

It’s a giant, pilotable mech suit… _essentially every iconic Japanese anime you’ve ever seen from Gundam to Neon Genesis Evangelion is about to become a reality._

But not ONLY that. It can knock over walls, and terrifyingly, it can turn into a giant quadruped dog. _Y’know, not to chase you down or anything weird like that…_

This reminds me: back in 2017, there was a big [Kickstarter campaign](https://www.kickstarter.com/projects/megabots/support-team-usa-in-the-giant-robot-duel?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box) to fund a giant mega battle robot duel that [_didn’t quite live up to expectations… but DID happen._](https://youtu.be/MlBHMm4Qhis?si=GgMbLkzRrrZSHEDa&t=1488&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box)[ ](https://youtu.be/MlBHMm4Qhis?si=GgMbLkzRrrZSHEDa&t=1488&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box)

**Here’s what happened in AI today:**

  * 😻 Google's Magic Pointer pushed AI beyond prompt boxes.

  * 📰 Anthropic refused to give China access to its newest model.

  * 📰 Isomorphic Labs raised $2.1B for drug discovery.

  * 🍪 Claude Code added a multi-agent dashboard.

  * 🎓 Ask AI to write the assignment first.




…and a [**whole lot more that you can read about here**](https://theneuron.ai/explainer-articles/everything-that-happened-in-ai-today-tuesday-may-12-2026/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box).

_Want to reach 720,000+ AI-hungry readers?_[Advertise with us!](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)_[](https://info.technologyadvice.com/advertise-with-the-neuron?utm_source=www.theneurondaily.com&utm_medium=referral&utm_campaign=diffusion-models-are-coming-for-text-at-0-80-per-million-flat)_

**P.S:**_Love robots? We’re starting a new robotics newsletter!_[Sign up early here](https://form.jotform.com/260897013570156?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box).

# 🙀 Google Intelligence, Perceptron, and a Whole New World of Interaction

[Click here for the FULL BRIEF](https://theneuron.ai/explainer-articles/-google-perceptron-and-thinking-machines-are-trying-to-kill-the-prompt-box/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box)

As you probably know, Google has A LOT of AI experiments going on right now. They’re historically and to this day one of the most prolific companies building with AI… _so much so that the theme of the Musk V. Altman trials happening atm is basically “everyone V. Google”_(because OpenAI the non-profit was founded to stop them from owning all of AI). 

Well, today Google made its next big bet to own the future of AI, and it looks a little something like _this._

**Here’s what happened:**

  * [Google](https://blog.google/products-and-platforms/platforms/android/gemini-intelligence/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box) announced Gemini Intelligence for Android, which can automate app tasks, summarize and compare web pages, fill forms, turn messy dictation into polished messages, and build custom widgets.

  * [Googlebook](https://blog.google/products-and-platforms/platforms/android/meet-googlebook/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box) is Google’s new premium laptop category, built around Gemini, Android apps, Chrome, phone sync, Magic Pointer, and premium hardware. _Wait a minute, what’s Magic Pointer? Well…_

  * [Google DeepMind](https://deepmind.google/blog/ai-pointer/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box) showed off Magic Pointer, a Gemini-powered cursor that understands what you are pointing at and can act on “this” or “that” without a full prompt.




Of those three, the magic mouse killer is _DEFINITELY_ the most interesting. A normal cursor tells the computer **where** you clicked. Google wants the cursor to tell the computer **_what you mean_**. 

  * Point at a date in an email, and it can make a meeting. 

  * Point at a table, and it can turn the numbers into a chart. 

  * Point at a paused travel video, and it can find the restaurant on the map.




That’s the real shift: **the interface starts carrying part of the prompt for you.**

**And Google is not alone in this.** [Thinking Machines Lab](https://thinkingmachines.ai/blog/interaction-models/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box) from ex-OpenAI CTO Mira Murati previewed **i****nteraction models** , which process audio, video, and text in tiny 200-millisecond chunks so the model can listen, watch, interrupt, and use tools in real time. Meanwhile, [Perceptron](https://www.perceptron.inc/blog/introducing-perceptron-mk1?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box) released Mk1, a model built to understand video as a stream of events, not a pile of screenshots.

**Why this matters:** In the [Genspark](https://www.genspark.ai/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box) interview we’ll release later today, COO Wen Sang told us he made a public commitment to be in front of his computer 50% less by the end of this year. That only works if AI helps us move off screens as the center of our work; and new interaction models make it easier to communicate without having to type or click, meaning eventually we can change the surface area of computers to fit whatever form is most convenient for us without sacrificing functionality. 

Also, everyone is obsessed with being able to control coding agents from your phone now. But the end state of agentic intelligence should not be typing commands into Telegram forever (a _ren’t y’all sick of texting, or is it just me and Apple’s terrible keyboard AI?)_ It should be the removal of every barrier between you and the technology, so you can interact with it in whatever way best suits your needs.

This leads me to believe the dream of “ambient intelligence”, or intelligence that is built into the background of our world to support us only when called upon (_like “magic”)_ could finally become reality…

**FROM OUR PARTNERS**

# AI is moving from copilots to autonomous systems, and enterprises need infrastructure built for that shift.

[](https://www.dell.com/en-us/lp/dt/nvidia-ai?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box)

The [Dell AI Factory with NVIDIA](https://www.dell.com/en-us/lp/dt/nvidia-ai?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box) delivers a validated, end-to-end AI stack spanning infrastructure, software, and services, designed to help organizations operationalize agentic AI at scale.

  * Built for production:  
Up to 269% ROI in year one

  * Up to 86% faster AI deployment

  * Flexible deployment across on-prem, edge, and hybrid environments




[Learn More](https://www.dell.com/en-us/lp/dt/nvidia-ai?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box)

# 🎓 AI Skill of the Day: Write the Mission Brief First

Want Codex to keep working instead of stopping after one polite little answer?

Try this trick from[ @meta_alchemist](https://x.com/meta_alchemist/status/2054214497443995694?utm_source=chatgpt.com): ask Codex to write the /goal prompt first. /goal is an [experimental Codex CLI feature](https://developers.openai.com/codex/use-cases/follow-goals?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box), meaning it’s currently for the terminal version. OpenAI says it helps Codex pursue long-running work toward a clear stopping condition.
    
    
    read this session and repo, analyze deeply the exact intent and goals we are looking to achieve here then write me the /goal prompt for this.
    
    
    make sure to dig into history & docs we have to be 100% clear
    
    
    if you are not sure about certain parts or wanna ask me a few questions to clarify certain goals further don't hesitate
    

Then paste Codex’s answer back in with /goal at the front.

Outside Codex, use the same idea with ChatGPT or Claude: have it read your context and write the system prompt before it starts your research memo, strategy doc, sales deck, or meeting follow-up.

**Want more in depth tips like this**? Check out our [AI Skill of the Day Digest for May](https://www.theneuron.ai/explainer-articles/ai-skill-of-the-day-digest-may-2026/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box).

**Have a specific skill you want to learn?** [Request it here!](https://docs.google.com/forms/d/e/1FAIpQLSd_-hSXtB9ytR1HQrU85IJnJw233bNKptiGB5BZh9maPse1Eg/viewform?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box)

# 🍪 Treats to Try 

  1. [Claude Code Agent View](https://claude.com/blog/agent-view-in-claude-code?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box) gives you one dashboard for managing parallel Claude Code sessions and longer-running coding work, available on paid Claude plans.

  2. [OpenAI Daybreak](https://openai.com/daybreak/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box) helps security teams find threats, generate patches, and verify fixes across code and systems, paid only rn.

  3. [Krea 2](https://www.krea.ai/krea-2?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box) gives creators a newer image-generation workflow for polished visual experiments, no pricing details (_it went viral on X for giving Midjourney’s style a run for its money)_.

  4. [Voker](https://voker.ai/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box) tracks production agents by classifying user intents, corrections, and resolutions before failures become customer complaints, starts free with enterprise self-hosting.

  5. [Ponder](https://ponder.ai/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box) turns raw footage into cleaner video edits for creators and teams that do not want to live inside a timeline, no pricing details.

  6. [Physics Intern](https://huggingface.co/spaces/huggingface/physics-intern?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box) is quite literally your physics intern; you enter a theoretical physics question and specialized agents gather evidence, form hypotheses, and critique the steps for you.

  7. [Oboe](https://oboe.com/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box) turns a learning goal into a personalized course made for you, positioning itself as a 'learn anything' product rather than a generic content library.

  8. [Composio TrustClaw](https://github.com/ComposioHQ/trustclaw?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box) is a self-hostable personal agent with vector memory, Composio tools, and Telegram access.




# This company just raised $2B+ to cure all diseases with AI… here’s how

[](https://youtu.be/W0NSk2y3OFI?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box)

Yesterday, [Isomorphic Labs](https://www.isomorphiclabs.com/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box) just [raised a $2.1B Series B](https://www.reuters.com/legal/litigation/google-backed-isomorphic-raises-21-billion-scale-ai-driven-drug-discovery-2026-05-12/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box) to scale AI-driven drug discovery; if you’re wondering WHY, what they do, or how they plan to do it, [check out our recent interview with the Isomorphic Labs team](https://youtu.be/W0NSk2y3OFI?si=XMr4Jh5REbKb5BhB&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box)! 

**Watch and/or Listen now:** [YouTube ](https://youtu.be/W0NSk2y3OFI?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box)| [Spotify](https://open.spotify.com/episode/2TzHhOkVIN9AL3GXXxSyDe?si=Hfr5NDX1Q_ybcdKSTMdsNQ&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box) | [Apple Podcasts](https://podcasts.apple.com/us/podcast/the-neuron-ai-explained/id1742267001?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box)

# 📰 Around the Horn 

  * [Anthropic](https://www.nytimes.com/2026/05/12/us/politics/china-ai-anthropic-openai-mythos-chatgpt.html?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box) reportedly refused China access to its newest model, while the Pentagon is using the same model family for cybersecurity work.

  * [Google and SpaceX](https://techcrunch.com/2026/05/12/report-google-and-spacex-in-talks-to-put-data-centers-into-orbit/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box) are reportedly talking about putting AI data centers into orbit; the pitch is solar power, space cooling, and maybe a way to keep the AI boom from eating every substation in Iowa. 

  * [Jensen Huang](https://www.reuters.com/world/asia-pacific/nvidia-ceo-huang-not-going-to-china-during-trump-visit-source-says-2026-05-11/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box) was (maybe??) left off President Trump's China business delegation until he [apparently hopped aboard Air Force One in Alaska](https://www.politico.com/news/2026/05/12/jensen-huang-invite-trump-xi-summit-00918208?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box) at the last minute. 

  * [Mistral and TanStack](https://www.tomshardware.com/tech-industry/cyber-security/compromised-mistral-ai-and-tanstack-packages-may-have-exposed-github-cloud-and-ci-cd-credentials-in-mini-shai-hulud-malware-infection-supply-chain-campaign-spreads-across-npm-and-ai-developer-ecosystems-like-wildfire?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box) were hit in a supply-chain campaign that exposed developer credentials across PyPI and npm packages.

  * [Meta](https://www.reuters.com/sustainability/boards-policy-regulation/meta-offers-rival-ai-chatbots-free-access-whatsapp-month-2026-05-12/?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box) offered rival AI chatbots one month of free WhatsApp access to address EU antitrust concerns.

  * [Odyssey](https://odyssey.ml/introducing-prowl?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box) released PROWL, a reinforcement-learning-driven adversarial framework where agents explore game worlds like Minecraft to find world-model failures and feed targeted fixes back into training. 




**FROM OUR PARTNERS**

[](https://www.cloudbees.com/agentic-devops-world?utm_campaign=global-agentic-devops-world&utm_medium=email&utm_source=neuron&utm_content=native-ad-1)

Enterprise teams are generating more AI code than ever. Delivery confidence isn't keeping pace. Join engineering leaders at [Agentic DevOps World](https://www.cloudbees.com/agentic-devops-world?utm_campaign=global-agentic-devops-world&utm_medium=email&utm_source=neuron&utm_content=native-ad-1) on May 19 for the live data drop on what's actually breaking and how to fix it.

[ Register now](https://www.cloudbees.com/agentic-devops-world?utm_campaign=global-agentic-devops-world&utm_medium=email&utm_source=neuron&utm_content=native-ad-1)

# 📖 Midweek Wisdom:

  * [Eric Ries](https://www.lennysnewsletter.com/p/how-to-build-a-company-that-withstands?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box) argues mission-driven companies need governance that can outlive the founder, because only 20% of founders remain CEO three years post-IPO and “mission-hopeful” culture usually collapses under investor, board, and acquisition pressure.

  * [Tuhin Nair](https://www.nair.sh/guides-and-opinions/communicating-your-expertise/why-senior-developers-fail-to-communicate-their-expertise?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box) argues AI-era developer teams should ship a fast “Speed” version for learning, then let seniors harden a “Scale” version for reliability.

  * [Beyond Semantic Similarity](https://arxiv.org/abs/2605.05242?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box) argues agentic search should inspect source material directly with tools like keyword search and shell commands, because fixed top-k semantic retrieval can throw away useful evidence before the agent gets to reason.

  * [Empirical Work in the Age of AI](https://aieconomist.io/resources/empirical-work-in-the-age-of-ai?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box) argues AI can 10x empirical research workflows like scraping, replication, and causal analysis, but rigor still depends on humans verifying the data, methods, and weird details models miss.

  * [Jie Tang](https://x.com/jietang/status/2054222017566855508?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box) argues the next agent breakthrough is long-horizon work, like models hunting bugs around the clock, as memory, continual learning, and self-judging turn agents into systems that improve themselves.




# A Cat’s Commentary 

| That’s all for now.   
---|---  
  
**P.S:** Before you go… have you subscribed to our YouTube Channel? If not, can you? 

[](https://www.youtube.com/@theneuronai?sub_confirmation=1&utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box)

Click the image to subscribe! 

**P.P.S:** Love the newsletter, but only want to get it once per week? Don’t unsubscribe—[update your preferences here](https://www.theneurondaily.com/subscribe/f5596641-9099-4045-9641-731cd9fdcf90/preferences?utm_source=www.theneurondaily.com&utm_medium=newsletter&utm_campaign=google-is-killing-the-prompt-box).

---

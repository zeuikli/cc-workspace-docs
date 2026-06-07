# 🔬 Latent Space — 2026-06-03

> swyx 開發者簡報，未公開專案 + 工程視角
> 來源：[Latent Space](https://www.latent.space/feed)

---

## [GitHub's plan for Agents — Kyle Daigle, GitHub](https://www.latent.space/p/github)
*🔬 Latent Space | 2026-06-02*

_I 'm excited to work with Microsoft once again as the presenting sponsors of the [AI Engineer World's Fair](https://www.ai.engineer/worldsfair/2026)!_ _We 'll streaming live from [MS Build](https://build.microsoft.com/) today for a special crossover pod with [our friends at No Priors](https://x.com/saranormous/status/2061681787169017949?s=20) and the one and only **Satya Nadella**. However we did not hold back with this interview - we asked all the burning questions about uptime and Copilot that we know you have in your minds. Lets go!_

* * *

For almost two decades, **GitHub** has been the home of software, where both open source and closed flow, through commits, pull requests, reviews, actions, etc.

This ecosystem flourished as open-source maintainers and contributors would continue shipping code for the benefit of the community. However as coding agents began to ship mass quantities of code - **growing 1400% in 2026** , it marked a new era that was both extremely exciting and challenging for GitHub.

While these agents help more people ship more projects, they also significantly increase the floor of how much code is shipped, how often it is shipped, how many people commit code, and basically orders of magnitude multiples in every dimension of GitHub infrastructure:

[](https://substackcdn.com/image/fetch/$s_!MG5m!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F6ec41954-9498-4c2f-b23a-81e2bae29f82_2761x1579.png)[our valuemule pod](https://www.latent.space/p/valuemule)

Now GitHub inevitably experiences more pressure on their infrastructure which was originally designed around human developers moving at human speed. This has resulted in a very publicly notable uptime story:

So it begs the question of whether current systems around code can absorb what AI produces. Can CI/CD keep up when every idea becomes a build? Can open source maintainers survive floods of AI-generated slop contributions? Can GitHub preserve the human social contract of software while becoming the operating layer for agents?

Which brings us to the perfect person to answer these questions: **GitHub COO Kyle Daigle.** In this episode, he joins swyx to unpack what happens when AI doesn't just autocomplete code, but starts changing how companies operate, how open source works, how pull requests get reviewed, and how GitHub itself has to scale. 

We go deep on **GitHub 's internal AI workflows**: micro-skills, WorkIQ, MCP, Slack, Teams, email, Copilot workflows, the new Copilot desktop app, CLI, cloud agents, and how Kyle **uses agents to look backwards across company context before deciding what to do next.** Kyle also reflects on GitHub's history building webhooks, APIs, Actions, npm, Dependabot, and Semmle, why the AI era is breaking GitHub in new ways, how Actions became a general-purpose compute layer, and what Copilot becomes after code completion.

## Full Video Pod

* * *

**We discuss:**

  * Kyle's **expanded role** across GitHub

  * How AI got Kyle **coding again** after years in leadership

  * Why GitHub rolls out AI through **existing workflows** instead of forcing new tools

  * WorkIQ, MCP, Slack, Teams, email, and GitHub as **company context**

  * Why massive "mega-skills" are giving way to small, **atomic micro-skills**

  * How AI changes **summarization, communications, marketing** , and analyst work

  * Why former developers in leadership may have a **unique advantage** in the AI era

  * Kyle's **" 15 agents on Saturday"** workflow

  * How Kyle built an **AI-generated executive presentation** for CRO/CFO teams

  * Why AI changes the **chief of staff role** without removing the human work

  * GitHub Actions, webhooks, arbitrary code execution, and **secure agent compute**

  * The npm acquisition, **supply-chain security** , 2FA, and token invalidation

  * Slop forks, vendoring, and whether AI agents change **dependency management**

  * What pull requests become when most PRs come from **agents**

  * Prompt requests, vouching, AI review, and **trust in open source**

  * What counts as a "developer" when AI lowers the **barrier to building**

  * GitHub Spark, low-code, and why GitHub refuses to **hide the code**

  * **14x commit growth** , Actions load, databases, monorepos, and availability

  * Copilot's evolution from completion to **CLI, desktop app, cloud agents** , and SDK

  * Context, memory, rules, and making GitHub **" act like Kyle wants it to act"**

  * Ambient AI, OpenClaw, enterprise security, and the **new operating system for agents**

  * What swyx should ask **Satya Nadella** about Microsoft's AI future




* * *

**Kyle Daigle**

  * **LinkedIn:** <https://www.linkedin.com/in/kyledaigle>

  * **X:** <https://x.com/kdaigle>




* * *

## Timestamps

**00:00:00** Introduction

**00:03:36** Why AI Got Kyle Coding Again

**00:07:04** Running GitHub with AI: WorkIQ, MCP, Slack, Teams, and Skills

**00:15:39** The Golden Age for Former Developers in Leadership

**00:17:31** 15 Agents on Saturday and AI-Generated Executive Work

**00:20:20** How AI Changes the Chief of Staff Role

**00:21:45** GitHub's History: Actions, npm, Webhooks, and Open Source

**00:28:45** Slop Forks, Vendoring, and AI Dependency Management

**00:33:57** Pull Requests, Prompt Requests, and Trust in Agent-Generated Code

**00:41:21** GitHub Stars, 200M+ Developers, and the New AI Builder Wave

**00:45:15** GitHub Spark, Low-Code, and Why GitHub Still Shows the Code

**00:47:38** GitHub's Hardest Era: 14x Growth, Reliability, and Scale

**00:59:21** Actions as the Compute Layer for CI/CD and Automation

**01:02:04** The State and Future of GitHub Copilot

**01:08:24** Ambient AI, Background Agents, and the Future of the SDLC

**01:13:09** OpenClaw, Enterprise Security, and the New OS for Agents

**01:18:03** Build Announcements, WorkIQ, FoundryIQ, and Microsoft Context

**01:21:41** What Should swyx Ask Satya?

* * *

# Transcript

## Introduction: Kyle Daigle's Expanded Role at GitHub and Microsoft

**Swyx [00:00:00]:** We're here with Kyle Daigle, COO of GitHub. Welcome.

**Kyle [00:00:07]:** Hey, thanks for having me.

**Swyx [00:00:08]:** You're not just CEO of GitHub. People know you as that. You have a new role.

**Kyle [00:00:11]:** So I have an expanded role now. I've been working at GitHub for thirteen years and doing all things developer. Joined as a developer myself. And now, I'm also responsible as the CMO of Developer for Microsoft. And so all the kind of learnings and passion for developers and how we work with them and how we communicate and how we bring our products to market, we're also bringing that expertise to the broader Microsoft ecosystem and helping every developer that uses a Microsoft product or would like to have a sort of similar experience that they've had with GitHub over the years. So it's a different role in some ways, but it's also just building on the experience that I've had at GitHub of just sort of tell the truth, be authentic, show people how to use it and then let the products speak for themselves. Now just doing that with, all of Microsoft.

**Swyx [00:01:09]:** We'll be releasing this in conjunction with Build. You got lots of stuff planned, and we can sort of touch on that whenever it's appropriate. I think one of the interesting things is I rarely meet a COO who's also a CMO. I think you're a very outward facing and you're very confident publicly. That's rare. Do you actually view yourself as COO? What's What is your thing?

## From GitHub Developer to COO/CMO: Building the Platform and Operating GitHub

**Kyle [00:01:33]:** I think for me, it's been funny. The titles have always been, a-- have always felt a little strange to me. I joined GitHub as a developer? I wrote so much of the

**Swyx [00:01:46]:** Let's bring that up. You wrote the back ends?

**Kyle [00:01:48]:** I was going through, I was going through, some old photos, when folks were talking about how things were being built or how there was a build GitHub. I built, webhooks and worked with teams building the API, built the platform layer. Anything that integrated with GitHub, up until really twenty eighteen, I built or ran the engineering teams. And that's kind of where my the beginning of my passion always was helping people build things, deliver them to, their customers. And so being a developer, building for developers was always super unique. In a-- I think as my role expanded, it became my ability to talk to not just developers, but also enterprise customers or business leaders and have this translation layer. And then through all those years, GitHub has always operated pretty uniquely. Post-pandemic, working remotely was not as novel as it was when GitHub started in two thousand and eight. But all that expertise of running remote teams, doing it well, became this sort of bigger role, ultimately turning into the COO role of how do we operate GitHub in the way that GitHub's always operated after the Microsoft acquisition. And kind of so on from there. So like for me, I think the-- I've, I still code. I love coding but the problem has always been, people. It's a much harder problem to both support our own employees, a harder problem to communicate to developers and enterprise buyers what we're building why it matters, 'cause those are two very different messages. And so getting to work in the mix of COO, CMO, also just being a dev, I think is what's kept me at GitHub for so long.

## AI Workflows for Leadership: Commits, Retrospectives, and Context

**Swyx [00:03:40]:** Apparently, you have-- your commits have gone up. What's this? What's going on?

**Kyle [00:03:45]:** Rui's called me out pretty aggressively. So I think-- as you can imagine, right, you can see my normal era of being a dev In the twenty thirteen, twenty fourteen era, and then moving into management, and then ultimately the COO role. I think what you see there is me, really getting back to coding thanks to AI. I-- similar to, attaching problems between how to market and how to operate a business and how to code, I find, building agents and workflows that are connecting very disparate problems to be what's driving this. So that's, some of it's writing software. A lot of it is, connecting a ton of a different data sources to, help me out. But that is completely me really diving in on the AI side in trying out our tools, trying out everyone's tools, But building for me, building for the non-technical leader, though I'm technical and how we're, able to use these tools more than just the simple, call and response that I think a lot of the non-technical, your employers, you have to get-- you have to use AI, and so everyone uses, ChatGPT or Copilot or Claude or whatever. To really get into, how is this going to help me out, it-- I find that it's not the I need to write a blog post, I need to those simple examples. Helping people find the workflows of, "Okay, I need you to go through all the PRs today. I need you to go through everything that we've posted online. I need you to go through what we did the last three months. Go through all of my Obsidian notes for any mentions of this then go through my transcripts at work." We use, Teams, so, using WorkIQ, go call that MCP server, grab all the transcripts, go through all the Slack, and then build me out the plan of, what this week's messaging actually was. That's something that was, impossible because for me, I find AI in a what most of this launch here is actually, less building forward. It's actually, a recursive loop backwards. I'm always looking at what had happened first. Go back through the week and tell me what we did, what worked, what didn't work? And then tell me in the next three or four days-What would you tweak based on this sort of like looking backwards and then looking ahead a little bit? I find that to be so much more valuable, especially for like non-technical, because that retrospection is actually LLMs are very good at that. Like finding all the patterns, pulling them out, and then applying that retrospection to just a couple of days or just like a short period of time. Is all a bunch of apps that I've built and launched a bunch of, internal tools. I use the new, GitHub Copilot app, the desktop app with workflows. Every time I crack open my laptop, it's running workflows for me. It's just a ton of different stuff and of course, it all ends up on, it all ends up on GitHub.

**Swyx [00:06:47]:** Of course. That's where, that's where, stuff is hosted. Man, there's so much to ask you. I was going to leave the how do you run a company with AI thing at the end. I have to ask one-- double click one thing. You said, you are looking back at the week. You're, you're understanding what happens. When you say we That's three thousand people. How?

## Rolling Out AI Internally: Skills, CLIs, and Company Context

**Kyle [00:07:09]:** I think when we started rolling out AI internally beyond engineering, right? One of the things that I was really, passionate about is like we have to do this in a way where no one has to change how they work. I don't want to have to teach you a tool. I don't want to have to teach you something new. And so for us, we tried out a few tools. Most of them don't work because I got to get you on board? I got to teach you how to use it. What we've actually ended up doing is we've built like a set of skills internally. We have we each have our set of skills, and we've just been distributing even to the non-technical folks, the CLI. And then effectively, we're just giving it access to like read about everything that we're writing. So that's for us, that's usually GitHub, Teams, Email, and Slack. So Teams for, video chat, generally speaking.

**Swyx [00:08:03]:** Teams and Slack?

**Kyle [00:08:04]:** so we use Teams for video communication, but we don't use it for chat. W-we-- GitHub for a long history, right? We're always

**Swyx [00:08:13]:** Also Slack

**Kyle [00:08:14]:** Talking about ChatOps and like everything is built into Slack. Like every command, every flow.

**Swyx [00:08:18]:** So even though you have been acquired for I don't know, eight years now

**Kyle [00:08:22]:** we still

**Swyx [00:08:23]:** You still use Slack?

**Kyle [00:08:23]:** it's a purpose-built tool for us, and I think the reality is that moving off of it would be so bluntly expensive? Simply because all the tooling is, baked in with that paradigm. And they both have their pros and cons but they don't work the same way at all. We still use a bunch of different tools Because it's the purpose-built tools that We need. And then

**Swyx [00:08:47]:** Well, the same doesn't go for the rest of Microsoft, presumably.

**Kyle [00:08:50]:** like the like various teams like operate

**Swyx [00:08:53]:** They make their own decisions

**Kyle [00:08:54]:** Various ways. I think it just matters what you're trying to what you're trying to do. But we do we do work across kind of every tool that we use, and then by giving everyone access to all of that context and the new WorkIQ MCP server, which is quite cool if you do live in the M365 like world. I can ask it all these backwards-facing questions, and it's incredibly important for our teams that are working remotely. There's a lot of stuff you miss when you're not in an office, and we are spread out all over the world. So most of that is looking back. And then we post, we post either auto-automatically into GitHub issues or discussions, these sorts of like findings or like our industry reports. Like what's happening this morning, today, yesterday. A little automation gets run. We'll use the app. We might use GitHub Actions like with, our agentic workflows just to go do that run, and then we push it into GitHub, and w-we keep having a conversation. So usually for us, it's about that sort of like looking back, looking forward on the non-technical side. And then of course for a lot of those folks, it's also building an app, pushing it to GitHub pages or pushing it somewhere to host it et cetera. But it's just like enabling everyone with that power of it's going to take me a week to figure this out. Instead, we're going "Okay I built a skill. Let's put it into a repo. We'll all share that skill together, and then we'll use the CLI or now the app-" "just to run it."

## Micro Skills vs. Mega Skills: How GitHub Uses AI at Work

**Swyx [00:10:26]:** All right. I think, I think we're going straight into like the team management and productivity thing. I think a lot of people are getting various levels of LLM psychosis. How do you manage the bloat of skills? Like everyone Has their thing, and they're Like trying to promote it to the rest of their peers in their org, right? And obviously, whoever becomes a skill influencer internally becomes like an AI leader, right? Of sorts. I assume you have those.

**Kyle [00:10:50]:** like I think we have

**Swyx [00:10:52]:** And I assume it's a mess a Yeah.

**Kyle [00:10:54]:** there's like I-- like I think the reality is there's two pieces. Like first is I think that we're ending the era of these like massive, beautiful, perfect skills that are just like not any of those things. 'cause for a while, right every tweet every day is like go download the skills, the perfectly managed thing to do this entire workflow. And I think that like what we've found and what-- I was just with my team, this week, and we were talking about the skill side, and we're really talking about these like incredibly micro skills that are just doing one thing for us very well Versus a skill that's going to do I said, that full report. That doesn't really exist on our side anymore. It's usually how do-- like a single skill that's going to identify the most important marketing information given any MCP server. Like this is the most important thing. Less about stitch a bunch of tools together and have it produce this mega output because then weeks go by, months go by, things change, and you want to tweak

**Swyx [00:11:58]:** It's brittle

**Kyle [00:11:58]:** Your mega skill and you're screwed? You can't do that. And so now we're really just talking about the Legos we're using and just letting the instruction book be something we're all putting together. Whereas I think a lot of AI skills for a while have been that mega instruction book style.

**Swyx [00:12:15]:** I've, thought a lot about Postel's law. I don't know if that's a term that is, means things to folks. It's the idea that you should be liberal in what you accept and strict in what you output, right? And I think that's like a good framing principle for skills. This is my skills, obviously on GitHub. I feel like everyone should have like how like some repos In GitHub are special repos? I feel like we should sort of reify the slash skills and everyone like give it some kind of special presentation. Anyway, so, yeah, this is one of those like download Download anything, transcribe anything, and then you can string together the atomic skills that do one thing well Into like some kind of orchestration skill that calls other skills. I assume, does that match?

**Kyle [00:12:56]:** I like I think so. I think that the

**Swyx [00:13:00]:** Summarize anything.

**Kyle [00:13:01]:** Like I think the- For me, summarizing something for I do communications and PR and analyst relations and marketing and customer activities, and so my summarize everything is very different for each one of those like Contexts. What 'Cause if I'm summarizing something for an analyst, that's a very different thing than, probably how I'm going to summarize something for like a customer meeting or an engagement. So that's I think like the difference when we're talking about the like the tools I might use on Saturday or the skills I might use on a Saturday when it's just for Kyle. Yeah, those are kind of like they have an atomic actual tool underneath or maybe skill, and then Kyle cares about X. But I think when we're talking about work and enabling the the marketers, communicators there, it's the atomic, this is what good summarization is, and then this is what I care about as for marketing for communications For whatever. And that I think is like the interesting matrix problem when we go from like a developer set of concerns to all kinds of different professions, is that what that word means to me is different than it means to you is different than it means to the analyst or the salesperson, and that's where I think the matrix mess is that we're starting to like still starting to find. It's about these mega skills but they're all just slight permutations, but those permutations are really important. It's the difference between someone reading this and going "Did AI make this?" what Or "This makes total sense, and I would expect this when I'm giving a briefing to Gartner," or like whatever else.

**Swyx [00:14:37]:** I think the beauty of it maybe is that you don't have to be that careful about what goes in there. It doesn't have to exactly fit as long as it like roughly is contained in there. I used to complain about plugin hell, basically. Like when you have a framework and then you have a hundred things that you need to integrate, everyone does like the GitHub used to be bloated full of these things. And now we don't need them anymore 'cause now you just use skills.

## Former Developers in Leadership: AI as a Creation Multiplier

**Kyle [00:15:00]:** And like I think the most magical thing is the just that like I can just also crack it open. Like Like yes, I could go like change the how the plugin is coded, or like I could go do that now with AI, but I think there's just something more magical about getting a response back and being "That's not right," and then you just crack the skill open, you just type English words and it's different. That building block is just, I think very unique. Once I get everyone to kind of understand how to best how to best make those changes to get the most power out of them.

**Swyx [00:15:36]:** Is there a-- you have a your peer group that Of people like you. Is there a common framing for Something I'm feeling is, which is true, is that is this a golden age for former developers who are now in leadership? Because you can wield the tools, you would know the right words, you're maybe not too close to the details. Doesn't matter. But like you're more effective than someone who doesn't come from that background.

**Kyle [00:15:59]:** I think that like the secret has always been your ability to identify patterns and solve problems, and I think that for folks that like myself that don't code day to day anymore, that has made me successful as a developer, made me successful as a COO and now CMO. And so now that I have access to get and write code, I'm now applying that sort of like pattern finding and problem solving, and I know enough still about how to then go and say, "Oh, I want to make an app, but I don't want to break into jail or create something that's not going to be able to work or to be deployed scale or whatever." that ability to apply all that additional business knowledge and still code I think is what makes that so interesting to me. Slightly different than I think some of the other like technical leaders that became business leaders and now are going back to their apps and updating them. Good for them? But I think the more, much more interesting thing is, well, now I have this whole new set of expertise over ten plus years. Why not take that and use that as a developer with these AI tools? So I definitely think that makes me more powerful, but I think that's true for like every dev as well. Most of the dev friends I still have also have some other underlying skill and passion. There's really talented, very kind of linear computer science software devs, absolutely. I just find that the folks that came from a different career, went to school for something else, went off and did this random thing, and then became a software dev, or were a dev, did a random thing, came back. Learning that extra set of information, learning those extra skills, and now having the power of an AI where I can crank up fifteen agents on Saturday while my kids are doing lacrosse, That's like really powerful. And I think it gets me back to that feeling of like creation, and it's very hard to replicate that in most other senses? That first time you build an app and you click it and you show someone that's magical. And so being able to do that not just in code, but across all kinds of different assets that's, that's huge. We were doing we're doing our every year we do our revenue planning. We talk about okay, what is it going to look like for next year? And of course as you imagine, there's, slideshows everywhere talking about what are we going to talk about, what's the narrative, et cetera. And so as you said I'm "Okay, well, I could probably just like build something to build this and then that way I don't have to go build the whole spreadsheet or I have to pass it to my team." So we went through this process, and I got all the information and used the skills I mentioned. I built like a little app just to make it so I could look at some of the information in a SQLite database, more easily. And I ultimately built this entire presentation without touching any of it and I was "Okay, I'm just going to present this to our CRO, the CFO, their teams," without mentioning I'd built it with AI. I like built a skill to make it look very much not AI driven. Just not pretty.

## AI-Generated Presentations, Human Taste, and the Changing Chief of Staff Role

**Swyx [00:19:03]:** Like a design. Yeah.

**Kyle [00:19:03]:** Not pretty. But just like very clearly not AI. Kind of like don't do anything interesting.

**Swyx [00:19:08]:** That's, yeah, that is valuable.

**Kyle [00:19:08]:** Just go Exactly. We did the whole thing through. It used my notes from Obsidian, it used all the context I mentioned before, the plans, and Never came up once that it was AI generated.

**Swyx [00:19:20]:** It didn't matter.

**Kyle [00:19:20]:** Never once. D It didn't matter. And so now I take

**Swyx [00:19:23]:** This is a tool

**Kyle [00:19:23]:** I can take that tool and go, "Look, I don't want you to go build slideshows." They're just helping us share information with each other. If this thing can do it With a little bit of crafting from you and then we can look at it together, awesome. There's no value in all that extra work. I think that the ability to, make it look humanly bad and and build a little app to, manipulate the data I think is part of, that upside for devs that are now in leadership roles. Because, the thing that I feel like I said before, this that's all a people, that's all a people problem. I know if you've used a coworker or not to build a slide deck, unless you spent a bunch of time to not do it.

**Swyx [00:20:07]:** I know, but like it was so, I think there's a certain charm to just being blatantly AI. 'Cause I think that you're well, you're just honest about There may be mistakes here that I cannot vouch for. So how much value is there? But anyway I think, actually the real question I want to ask is, there's a-- You were a chief of staff To Thomas. And in the pre-AI world, the that job would've been a chief of staff job of like Can you prep me these slides and all that? And now you do it yourself.

**Kyle [00:20:35]:** I still, I still have a chief of staff. Because, the difference is it's sort of the discussion every time we have some sort of technology evolution is it's not that the jobs the roles don't all go away, they just change? And so yeah, I don't have someone spending all their time building out slides for me and presentations 'cause I don't need that anymore. But now I need that person that is able to go and find all the different connections between humans in those discussions to help me find out, okay, I should be meeting with this group and this team, and they have an opportunity, and I'm going to be in San Francisco today, I'm going to be in Seattle tomorrow. Those sorts of human connection aspects are still incredibly valuable and has always been a big part of that chief of staff role. But now just like chiefs of staff are not opening up, letters to process, they're doing emails. What It's the same thing. And now they're, they're not building out as many of these presentations because they have the the ability to have a AI take it on for, and share that with me and great. Let's keep moving 'cause it's allowing us to go faster and make better decisions more quickly.

**Swyx [00:21:45]:** Awesome. Well, so we can dive into more sort of, Productivity insights as you go. I did want to do a little bit of a brief history of colleague and hub. Because, we started here. And then you also involved the NPM acquisition. I did, I do want to touch upon that. And then more recently, I just want to bring up to present day where we're having uptime issues Which transparently we've already Addressed publicly, but we'll, we'll discuss in the pod. Did I miss anything? Like what, any other major highlights? Obviously, it's, it's a lot of years to cover.

## A Brief History of GitHub: Webhooks, Actions, Acquisitions, and Platform Evolution

**Kyle [00:22:15]:** No the I think one of one highlight was right before the acquisition closed in twenty eighteen, I got to launch the first version of Actions

**Swyx [00:22:27]:** Oh

**Kyle [00:22:27]:** At GitHub Universe. So it was O

**Swyx [00:22:29]:** They're that young?

**Kyle [00:22:30]:** It was October of twenty eighteen, I think. Yeah. Yeah.

**Swyx [00:22:33]:** Gee, Jesus.

**Kyle [00:22:34]:** I got to I was the engineering leader on that project and got to launch that. And then, yeah, we did acquisitions of NPM you said, Semmle, Dependabot Pul Panda a whole bunch of things. That was a big

**Swyx [00:22:47]:** Pul Panda.

**Kyle [00:22:48]:** Abi is doing well.

**Swyx [00:22:51]:** DX. Holy crap.

**Kyle [00:22:52]:** Did well on DX. I and like that was a that was the big shift, after the acquisition. I had to join the sort of business side.

**Swyx [00:23:00]:** So I need to hit you on some of these things 'cause you were there. Right? And how often do I get to talk to someone who was there? But yeah, Actions. Is that the number one source of security issues on GitHub?

**Kyle [00:23:11]:** Oh, sh I think that the number one source of, security issues is probably like all, the literal code in everyone's like underlying repositories. I would say back further than that is, if you remember I had to show in this graph was this is, I'm, didn't say this before, this is ultimately webhooks.

**Swyx [00:23:30]:** You yeah.

**Kyle [00:23:31]:** Like circa whatever it was.

**Swyx [00:23:32]:** It says Hookshot in there.

**Kyle [00:23:32]:** I forget. Yeah. Yeah, Hookshot's in there. And so like back then, it says GitHub Services. Do you see, it says Hookshot FE for front end, and then it says GitHub Services. GitHub Services back in the old days, right? You we had a repository that was Ruby code, and you could write any Ruby code in there, and then we would execute that On your behalf As a service, and then that way if an if you were trying to integrate with something, it didn't we would run it for you.

**Swyx [00:23:57]:** And of course no containers 'cause

**Kyle [00:23:58]:** No, 'cause it was

**Swyx [00:23:59]:** Well, no containers

**Kyle [00:24:00]:** Twenty fourteen. And so there was some isolation obviously, but it was mostly the separations on the server level. That's like an example as long as the very old version of Pages, which ran on its own containerization infrastructure, not on Actions.

**Swyx [00:24:15]:** Which like all-time great product.

**Kyle [00:24:16]:** Pages powers the internet at this point to some degree. Those were places where like clearly there were no like issues like to my knowledge. But it was those things where I'm looking at and going "Okay, well we can't be running arbitrary Ruby code," like on everyone's behalf. Then containerizing all of that up intoUh into actions now where yeah the containerization, is r-really good. The pinning most folks aren't pinning it the like to a particular

**Swyx [00:24:48]:** Images

**Kyle [00:24:48]:** Sha, et cetera like their workflows, and so that's a big that's a big place Of pain for folks if they're just doing similar to any dependency management, just V1 or newest or latest, I think. But, that journey from that day to "Okay, we're just going to run all this arbitrary code, and, it'll basically be okay," to now, no, we have, really good containerization. We have a new, underlying, ag-agent, containerization, service. It's like we're using it under the hood. It's through Azure. They recently announced it. The Azure, Dev Compute, but it's, very fast, very fast compute to be able to, spin up your own cloud agents, or whatnot. We're using it under the hood for some parts of the new,

**Swyx [00:25:36]:** Microsoft Dev Box?

**Kyle [00:25:37]:** No. Dev Compute, yeah.

**Swyx [00:25:41]:** Hmm. Not finding it just yet.

**Kyle [00:25:44]:** Oh, it's, it's in there somewhere.

**Swyx [00:25:46]:** All right. Well, we'll cut that out.

**Kyle [00:25:47]:** Sorry. But with, Dev Compute, you can, run, really fast, spin up really, small VMs really quickly, so you're doing a tool call

**Swyx [00:25:58]:** Same concept

**Kyle [00:25:58]:** Just do it containerize exact-exactly. So we're using that so definitely moving that direction to protect us from every every piece of code that we're ultimately running.

**Swyx [00:26:07]:** look, that grows into the full SDLC? Code hosting was just the start and and then it's grown beyond that. Let's talk about NPM may-maybe 'cause I think that's also, a very major point in the industry. I do think, it was looking for a home. It was, kind of struggling as a business, right? I don't know, I don't know how you would characterize that whole acquisition and how it

## NPM, Package Security, and Keeping the Internet Running

**Kyle [00:26:33]:** like when we were talking to the team, I think the big thing for the both of us was to find a way to keep NPM, which was basically powering the internet then and way more so now to some degree running. Keep it going keep continuing to scale. It was having scaling problems, if I recall, back at that time. They were doing some rewrites. It

**Swyx [00:27:00]:** that's cute compared to now.

**Kyle [00:27:01]:** Well, that's the thing is like when I'm talking to folks now, there's there's so many more underlying uses of NPM than there were back when we had them join in with GitHub. But that was ultimately the goal. It was really okay, we used to have pages. We have, the world's code. Let's make sure that we can keep NPM running well for the world. And we put a bunch of time and investment into fixing some of the underlying backend, changes, some of which we talked about some of the manifest work, et cetera. And then now, really trying to bring the the security posture of NPM up to speed. But, it is a unique challenge in that every move that we make to make it more secure will break a lot of people. And security is paramount. And also, we take it very seriously. We're, the any time that we have a problem with GitHub or we make a change that makes us more secure but hurts, there's, a snow day for developers or a really bad fire that they have to go put out. And so we've, have changed the 2FA policies. We've changed the way the tokens work. When we find tokens that have been exposed or potentially, exposed, we invalidate them, and

**Swyx [00:28:22]:** I love that feature in GitHub. Yeah, it's great

**Kyle [00:28:23]:** That creates issues, but, the but that's the thing is we're trying to push the community, forward without necessarily, doing something that is going to break the contract that's been for 15 years or close to it or some amount of years on NPM.

## Slop Forks, Vendoring, and the Future of Open Source Supply Chains

**Swyx [00:28:43]:** I think the-- So now we're talking about, open source and publishing. And I think there's something here with what people are calling slop forks, which, I think Malta from Vercel is doing. And, part of me thinks, well, the way to get past any vulnerabilities, we just, let's just get rid of the concept of NPM. And we only publish source code. And anytime you want to import it you have your coding agent look at it and then adapt whatever subset you're going to use into your vendor it. But, the AI vendor it. Is that realistic? I don't know. Is it-- Will that solve all our security issues? I don't know.

**Kyle [00:29:24]:** I don't think it'll solve I so Mitchell was just talking Mitchell Hashimoto Was just talking about this today, and I think that I-in some ways, it's all all things, old or new again? Yeah, absolutely vendoring everything. Like I do I do remember twenty thirteen, twenty fourteen.

**Swyx [00:29:42]:** This is Yeah. Let's, we must return to

**Kyle [00:29:43]:** That's what is We were vendoring everything. We were having actual discussions around, or at least I remember we were "Should we take this full thing?" "Why is this so big? We only need this one file." And so I do think there's something true there where having either taking only what you need or the dependencies just getting incredibly small over time, I think will help to some degree, but it's not going to solve the fundamental problem, I don't think, because the vulnerabilities in an agent looking at them, there's time and time again, there's a million different ways in which we can convince an agent that this thing is, secure or not and pull it in. Or we can do static code analysis or runtime testing to say whether the code works or not. That is, I think, the step that needs to continue to be, invested in. The question is just on, how much scope. Should it be this enormous project that I'm pulling down, or should it be this piece? Either most companies are running some amount of security checking on the on the packages that they're bringing in or vendoring. That I think won't change. That's like what advanced security does to some degree, Socket does some degree. Like everyone is doing a piece of that. How we each do that like especially when we're talking to enterprise customers, is just like very different. No there's no one wants one single way to do it. And I think that's always been GitHub's, unique position in the world. I talk a lot to maintainers, I talk a lot to folks about this. It's we're-- we rarely start like a process and a practice and like push it onto the community. We usually wait for the sort of like RFC process socially or literally, everyone agreeing, and then we'll cement something in. Because otherwise we're

## Maintainers, RFCs, Vouching, and the Social Layer of Trust

**Swyx [00:31:35]:** That fits your role in the ecosystem, yeah

**Kyle [00:31:36]:** We're GitHub. Yeah, we don't want to shape the whole thing. We want it to be figured out. But like how do you balance that like sort of Role in the industry to keep everything as secure as is possible and make sure that you're you're not going to be compromised as a human, 'cause that's usually how it all happens. And Not not create a process or lock us into a flow that you're not going to or like Mitchell's not going to or other open source projects aren't going to like. That's always been a tricky balance for us, and I think that's something that we haven't talked about enough is we're not going to be able to fix everything for everyone in a way that everyone is going to like. So tell, help us, tell us what is working. When Mitchell was talking about, the Upvote, the up

**Swyx [00:32:22]:** I was going to bring up his thing. Yeah.

**Kyle [00:32:23]:** I forget what it Yeah. When he's talking to us, I was chatting with him and talking to him about this and I put it on Twitter and we talked to, also over DM, was "We're going to keep working." but I think the important thing is I do actually want to hear what isn't working for you. And as, be as specific and clear for your project as is possible. And to every piece of credit over the many years that we've known each other through the industry, he's always done that and I appreciate that 'cause there are places that we need to fix up, and we hear from him, and we'll fix up just like we do all other kinds of maintainers. But that that process between making those types of improvements and being more secure and like creating, I forget what he calls it's not the proof process, not the claims process. Do what I'm talking about? He has that he his projects have a way for you to kind of like,

**Swyx [00:33:13]:** Vouch

**Kyle [00:33:13]:** Vouch. Thank you. Yeah. He has like the vouch system for saying, "Hey, you should accept my PRs." That's been

**Swyx [00:33:20]:** I just built this into GitHub. I don't know.

**Kyle [00:33:22]:** Well, see, but that's the thing is that you say that and like he and his community really likes this and then I'll go talk to other maintainers and other maintainers, globally, and they're "No, this doesn't work for me." And that is the tension, but also the kind of beauty of GitHub, depending on which way you look at it is we want to help maintainers, so we create all these tools to let you have more control over how much you take in from AI and PRs. But you can also use this. What You can go use this project, and if it takes off and becomes the kind of mostly standard, then yeah, we probably wouldn't enforce it but we would add it in because that's the flow that we tend to do?

**Swyx [00:34:02]:** I hear a lot of people don't know the history of the pull request. And like like that's how, that's something that GitHub standardized basically.

**Kyle [00:34:08]:** Yeah. It was a very messy process Like beforehand, and now the we have the benefit of it being the process? And now we have to go and Figure out the next best process or what adaptations change, or what does a pull request look like when eighty percent of your PRs are just coming from your agents and not From other devs?

**Swyx [00:34:31]:** Do you like the prompt request idea from Peter?

**Kyle [00:34:34]:** like I think that for each like each idea I think has its merits. I'm not, I'm not avoiding saying anything good or bad, but I feel like I've seen a version of we have that we have entire Thomas' store. Take all the assets of what you've built and put that in. I think that's got great ideas. There's all these various permutations of the PR flow, but I think the reason why there's not a single answer is ultimately we're trying to codify trust. We're trying to say "Okay, if Sean reviews this I'm going to trust it because you're Sean or you're the senior dev or you're the whatever." And right now, when we are working in a flow where an agent writes code and another agent reviews code and then Kyle goes and looks at it the trust is kind of diffuse. And most of the tools that we're talking about are talking more about verification flows. We have more assets to look at, so I can probably say whether this is a good PR or not. But that still doesn't solve, I think, the human problem of I'm looking at a PR and I want to know if I can trust it. And we're still, we still tend to use human signals for that? Mitchell approving it or Kyle approving it or whatever. And so I think that's, I think that's why most of these options haven't really solved it is because, it's a social problem ultimately. It's a it's a human problem to review it and agree. Or you fully trust the tool and you're imbuing that tool with full trust Which I think in some cases that absolutely exists.

## AI-Generated PRs, Trust, and the Waymo Analogy

**Swyx [00:36:08]:** And so like in the same way that there will be a tipping point in society when we don't allow humans to drive anymore Because machines are measurably better than Than humans. I'm looking for that tipping point, right? Like Mythos is ridiculously expensive. Someday we'll have Mythos on a desktop. I don't know. Will, does that change the equation?

**Kyle [00:36:30]:** I think it's more I took a Waymo here, and I was on my phone and not looking around at all. There are other, self-driving, vehicles that I would not trust while, staring at the road. And I think that trust is something that is

**Swyx [00:36:48]:** Is this a Zoox thing? What is it

**Kyle [00:36:50]:** I think that is both. I think that is both. Like

**Swyx [00:36:53]:** There's Zoox in this robo taxi. That's it. It's

**Kyle [00:36:56]:** Well, depending on what level Of self-driving. But, my point is sort of that I think part of that is I strongly believe that's, a mixture of verifiable proof. Like how many accidents, how much data, and so on, and the human aspect of how I feel when I'm in this car, what it tells me, et cetera. And so that's why I think some of the like Some of these some of our AI tools tend to, imbue me with more of that feeling of trust, even if the data says this is 100% accurate. I feel like it takes more time for us to go, "Should I trust this or not?" And that's in the soft sense of, startups with high agency, weekend projects, and open source. And then there's enterprises and regulated industries and everything else, and that is an even harder problem to go solve because even when it is fully verified, not only do you have to have trust from the humans on the team, you probably have to have trust from multinational,

**Swyx [00:37:55]:** Oh my God

**Kyle [00:37:55]:** Multi governments around the world and regulating agencies. And so that's where I feel like until we tip over to your point on the sort of like human EQ side of it. I feel okay this feels okay I've been proven enough. Then the ball will start to roll a lot faster, where we'll end up getting to the "Okay, we can trust this," and feel good about it in the Most difficult of cases.

## Reputation, Sponsors, Stars, and Bot Activity on GitHub

**Swyx [00:38:18]:** If human trust is the thing that matters, I feel like GitHub as the developer social network could maybe do more there. Like vouchers are one system But, we have star counts, and then we have Contributor rights, and that's it. And I feel like there should be more in that space. I don't know if there's any other design decisions there.

**Kyle [00:38:37]:** I think that one of the places that we don't really expose right now in this sort of way is, some degree of like hard trust and support, which would like for me is like sponsors is a good example of that.

**Swyx [00:38:49]:** Ah.

**Kyle [00:38:49]:** It like costs you something. To prove that I believe in your project and I trust you To some degree or I want to support you at the very least.

**Swyx [00:38:56]:** Solve payments for open source. Why not?

**Kyle [00:38:58]:** I think that I think that like as we keep moving forward, right, there's more and more projects where I'm, adding more and more dollars into sponsors personally because I want to like support them, but I also like know of I've probably never met them in person, but, I know of enough of their work that I want to support them. I think the thing that I don't love about stars or commit counts or anything else is ultimately, even with all of the various, abuse and de-spamming and deduplication work that we do or anti-abuse work that we do, these are all, not active social signals. They're passive ones that are ultimately gamifiable. And you may trust me, but another open source maintainer may not. And on what heuristic should you be, trusting me? That I think, is kind of where some of our thinking is right now. What signal from me is most important to you? You-- If you can define that potentially, honestly in an agentic workflow that's what we see some of these open source projects do, where you have GitHub actions, and then you have like an agentic workflow that's calling AI, and you're setting these rules. Like if Kyle has submitted and gotten accepted PRs across any given project and has a social handle tied to his account in GitHub, and that social account's older than a certain amount. Really complex measures that matter to you 'cause most open source projects have that heuristic built into their heads, if not written down in the contributing guidelines. You could take that and then go apply that and then just say, "Oh, we're not going to accept this PR." Building something that is, I think, malleable to everyone's needs, is a little bit better, rather than going "Hmm, this account's too young." Because what happens? The attackers just go and go and create a multitude of accounts, and they wait Until it ages up. Needs to have a certain amount of stars. That's how star inflation happens. Need to have a certain amount of repos

**Swyx [00:40:46]:** Oh my God. Yeah

**Kyle [00:40:47]:** With PRs. They all just create repos and submit PRs to each other, and then they come in and do something nefarious. And so, it's hard. It's hard to find the measure. So I think we're, we're looking more at how can we provide you tools so you can kind of choose what's best for you. And of course, we'll give you some standards. But the trust vector, gets down to I don't know, some version of like human digital ID like everyone's been talking about. Like how do I prove that it's me

**Swyx [00:41:13]:** Give me your eyeballs

**Kyle [00:41:14]:** On the internet. Give me your eyeballs. Exactly.

**Swyx [00:41:18]:** The I got to keep moving on Topics, but obviously I can go all day on this stuff because, I've been involved in GitHub and open source My entire professional career. Stars. Very superficial. Everyone knows it. But I think time to one hundred thousand stars is the fastest I've ever seen. Like people just reached that in I don't know, months. And then like at the same time I don't trust it right? Like how many of these are real or bot or like whatever. I don't know how to ask this but like what can we do about it? Like

**Kyle [00:41:49]:** Just

**Swyx [00:41:49]:** Is stars broken? Is stars fine?

**Kyle [00:41:51]:** I think that there's kind of two, there's like two pieces. Obviously we're constantly like trying to find ways in which like your users are producing spam, which would, I would include like be like only doing star gamification. When we find them, we pluck 'em out and we,

**Swyx [00:42:08]:** But it's like a Whac-A-Mole

**Kyle [00:42:10]:** It's a hundred percent like a Whac-A-Mole

**Swyx [00:42:11]:** There's no way

**Kyle [00:42:11]:** Now, powered by AI to be helpful. But I think more so what I'm seeing is, a lot of the like fastest time to X tends to be because we're now inviting so many more people into like software development on GitHub That like the zeitgeist is just swarming? And it's

**Swyx [00:42:32]:** It's not just developers anymore

**Kyle [00:42:33]:** And it's not you and I. Like like however you want to say like what a developer is it's not just folks who have been coding for a very long time. It's folks that have maybe started coding or only joined in since the AI era. And now

**Swyx [00:42:44]:** what's the latest Octoverse number? I know eighty million was my lastRem- member that a number of developers on GitHub

**Kyle [00:42:50]:** Oh, we're over 200 million now.

**Swyx [00:42:53]:** Okay. Well, so you see?

**Kyle [00:42:55]:** Like over 200 million developers now.

**Swyx [00:42:56]:** But it's not developers, right? It's, it's people with a GitHub account.

## What Counts as a Developer in the AI Era?

**Kyle [00:43:00]:** So, so this is, this is the biggest debate that I would say, everyone loves to have at GitHub at this point. From my perspective, right, I think that there's, there's clearly a difference between, professional enterprise developer and then developers. But I think that I think that the idea that we should be I don't know, splitting hairs or segmenting developers in the early era of software development is, not worth our not worth the time. So

**Swyx [00:43:29]:** When you get into gatekeeping

**Kyle [00:43:31]:** 100%

**Swyx [00:43:31]:** What is a developer?

**Kyle [00:43:31]:** 100%. 'Cause I wasn't a developer when I started writing code? I was going to

**Swyx [00:43:36]:** Oh, no. I made-- I cloned a thing, seven years before I learned to code. And then I and then I wrote about my learning to code journey, and people Just called me a fraud 'cause I had a GitHub account. And I'm "Well, no, I just use GitHub, but I don't know-" "I didn't know what I was doing."

**Kyle [00:43:49]:** I I remember that. I remember those sets of posts, and like that's, that's bullshit. So I fight very clearly on the line of, if you create code, if you have an idea and you create it into some way of, I'm, I'm going to run it and use the app right now, you may still use AI in that moment, but that's okay. At some point you're going to do the next thing. You're going to create a big-- You're going to have to learn about this database. You're going to fix a bug, whatever. We're all on some same journey, and those people are also hearing about the great new agent skill package or a new CLI tool or a new whatever. And those projects are going up because you want to be a part of this moment, just like I wanted to be a part of the Ruby community when Ruby was popping off when I started becoming a developer, and now I can just click the star button. And so I think that yes, there's clearly some amount of like spamming and game gamification that we're working against, but I really think we're just seeing this whole new cohort of folks that are moving from technology to technology because they're not working on a 20-year-old software application. They're working on a side app that they built on the weekend for their friends or for their new idea or whatever. And that's how you see these enormous charts going up and to the right with With stars.

**Swyx [00:44:59]:** I think something that's remarkable is the persistence or, that GitHub extends to those folks. Usually when I see platforms go into a new audience, they usually have to, have like a second platform with a different name that wraps the main platform. But somehow GitHub has been able to sort of persist and extend, and it's friendly and whatever? So it's, it's nice.

## Spark, Low-Code, and Always Showing the Code

**Kyle [00:45:19]:** I that's partially why I think as we've tried to move into I don't know, more like low-code-y things. We so we started working on Spark as like a way to, build an app and run it. I think that the reality is that we anytime we try to, kind of put even a veneer on top of it without when we put a veneer on top of something, we still always show you the code. That's kind of like a tenant. We're never going to, hide the code from you ever, because what

**Swyx [00:45:52]:** Why would you?

**Kyle [00:45:52]:** That's, yeah, that's the whole point? However, I think that what we learned with things like Spark is that really the value of Spark for most devs is, easy runtime. And you may have a runtime or a host that you're going to use for that or you just build something and run it but, the package of making that even more simple isn't really needed for folks that are trying to build software and not just trying to build, an app, which is, slightly different, a slightly different goal. So I want to get you in, I want to get you comfortable. I think the best thing for me as, someone that did not traditionally come into software dev way back, I want anyone to be able to breach that chasm and not be in the I don't know, I feel like we're, we're still in an era of, STEM. I've got a 12-year-old and an eight-year-old, and it's "We got to get 'em into STEM,"? Over and over. And I like I do, I do the things that good parents do. I was "Oh, you want to do coding?" "Yes, I want to do coding." Do coding classes. But now they're just not afraid of doing software. And that's, I think, the thing that's honestly kept me at GitHub for so long. Anyone should be able to go and build a thing, just like I can go change a light switch in my house. I'm not going to go into the breaker box 'cause I'll probably kill myself? But, I can go change that light switch. Everyone should be able to go and say, "This fricking app doesn't do what I want. I want it to work like this." And that I think, is what's kind of kept us all connected with GitHub through the years and some and during the easiest of times or in the hard times because of that opportunity of, we're the home for all developers, and we want everyone to be able to have that feeling that we've had of, had an idea, I created it and holy shit here it is.

**Swyx [00:47:37]:** Here it is. All right, I'm going to try to do more spicy questions.

## GitHub's Hardest Scaling Moment: Growth, Agents, and Uptime

**Kyle [00:47:42]:** Great.

**Swyx [00:47:42]:** Is it an easy time now or a hard time?

**Kyle [00:47:45]:** Oh at GitHub? It's a hard time. Like, it's a hard time and also, I was just with my team and I said, "This is also, the best and most exciting time that I think I can remember at GitHub." Because

**Swyx [00:47:57]:** Best of times, worst of times. It's never one

**Kyle [00:47:59]:** 'cause we've we were talking about Octoverse reports and, usually we do an Octoverse report once a year, and we look at the numbers, and we say, "Oh my goodness." I was at Universe in October saying, "This was the fastest year of growth that we've ever had," right? And now we're doing more in a month than we did in a year last year.

**Swyx [00:48:20]:** You're talking about PRs.

**Kyle [00:48:21]:** Commits.

**Swyx [00:48:21]:** Commits, yeah.

**Kyle [00:48:22]:** PRs. Kind of like you name it by roughly every measure that we're looking at, there's some amount of sort of growth that is much bigger, and that is breaking our system in new ways, not old ways. Like webhooks were always notoriously, unreliable over the years?

**Swyx [00:48:38]:** Whose fault is that?

**Kyle [00:48:39]:** not anymore mine, but for a period of time, I'm sure you could pull up a tweet that was "It was me. I'm sorry." but, now, that got rewritten at a scale level that is still working and is not having problems today. Now what we're finding isn't just the isn't the-The simple stuff that folks are on the sometimes on Twitter or on the internet are "Hey, why is this like this?" Sure. There's absolutely silly problems that we shouldn't exist. But now we're talking about, unique, novel permission problems that happen only at a scale across all different objects or whatever, that now we have to go rewrite this underlying system. And so it's, there are problems that yeah, caught us off guard, which I think I said. Like the growth is astronomical, but also we're making such material progress in that I'm excited once we're once we've kind of like reimagined the underlying foundation layer, or pieces of it at least, what's going to be possible when it's not just all of us and all the new people that are being developers and all of their agents and all the tools like working together. Because that'll still happen in that in that GitHub tool, that GitHub community. But it's a it's a hard day anytime we can't give you what you're looking for. We have the same problem internally. We operate through github. Com. Of course, we have backups when things go down and whatnot for our own operations but we feel it too. If it's not working it's not working for us, and that's kind of like the promise of dogfooding for GitHub. It's always been true. We're using the same tool you're using. We're not using a super secret version. We and so we also need it to be great for us for our customers of course for open source. And now an exponential growth of agents, Doing it too.

**Swyx [00:50:32]:** I wanted to load for audio listeners who maybe haven't seen your tweets, whatever. So one billion commits in twenty-five. Now it's two hundred and seventy-five million per week on pace for fourteen billion this year, if growth remains linear. Is that still the pace? I don't know. It's been a

**Kyle [00:50:48]:** it's, it's speeding

**Swyx [00:50:50]:** Roughly.

**Kyle [00:50:50]:** It's still speeding up.

**Swyx [00:50:51]:** It's, it's April, so yeah.

**Kyle [00:50:51]:** Exactly. This was in April.

**Swyx [00:50:53]:** All right. So basically you have fourteen x growth, right? Year on year on year. And I think that's a scaling issue. I think, I'm going to like try to really steel man this thing. People have experienced fourteen x growth. They haven't had your downtime. And that's like-- C-can we go dig into that? Why? Like what's the-- what broke? What are we doing to fix it? Like just anything for the community to reassure them.

## Why GitHub Reliability Is Breaking in New Ways

**Kyle [00:51:18]:** so there's a Like I was saying, there's a couple different places that we've seen the growth issues. Some of the growth issues, which is why we're t-- I was talking about pushing hard on more CPUs is in actions in particular. More tools, more agents, more PRs mean more builds, more builds mean more CPUs. And so we are expanding through not just our data center, but obviously we were talking about moving to Azure and moving to, adding an additional cloud compute because we simply need more CPUs. Not as much GPUs. We definitely need GPUs too, but now CPUs are becoming a factor.

**Swyx [00:51:53]:** It's very CPU heavy.

**Kyle [00:51:54]:** Underneath the hood when it comes to some of the underlying services, we've been breaking up over the years our database infrastructure, so that way we have, more cognitive separation between our the various services. The place that we continue to have pain is in, permissioning. And so right now m-many of our permissioning layers sit into a database that we like internally call MySQL One, and old Hubbers will know what I'm talking about. And so we've been pulling things out of MySQL One for many years, because like and we use we use Vitess and we use other technologies to shard and we do it as one big

**Swyx [00:52:31]:** Famous thing, PlanetScale was born from this and

**Kyle [00:52:32]:** A hundred percent. Sam Old Hubber and friend. And so finding these opportunities to like break this out and then do that globally. The other thing that I think is interesting and both a unique opportunity and tricky is we also run everything I just talked about in a black box container with GitHub Enterprise Server for people that work on-prem. So we take everything I just said, and we also do it on-prem, and we also do all of that and we do it in a data residence setup for customers that need to have their data in a single location. Each of these has the unique characteristic around how we're sort of storing that data in MySQL or in a permissioning setup. That's where some of these outages have oc-occurred, where you're seeing it more like across the board rather than just like the one piece

**Swyx [00:53:17]:** Filling the database

**Kyle [00:53:17]:** Isn't quite working. Exactly. And so part of it is that. I think there's been some other places where agents are much more or more projects appear to be moving towards monorepo versus we were going the other direction for many years in the industry. Repos were smaller, but there were more of them, and now we're seeing the opposite. Repos are bigger, and there's, not fewer of them per se 'cause there's new growth, but, we're just seeing many more big repos. Big repos, big monorepos have always had, a unique performance problem. Because each one, is slightly different if, particularly if the underlying blobs are incredibly big Inside the repos. And so we've done a ton of work that you pro-- like most people haven't probably experienced, unless you're in this case of the monorepo. But that Git, infrastructure layer improvement does help the overall, system because, many of the improvements that make monorepos work better make all repo infrastructure work better. And so, I could kind of keep going down the line where it's another thing where we're moving out of, We're changing how we do j I'll just say job queuing for lack of a better, explanation changing the underlying technologies there.

**Swyx [00:54:32]:** I spent two years being a job queuing guy, so.

**Kyle [00:54:34]:** And so it's kind of a little bit of a little bit of piece by piece, and it's mostly because as we were-- as it was built, we built everything in a way that assumed, I guess in some ways that the size of the pipe of work was going to remain the same. There's just going to be more people coming through each of those pipes. But instead now in places whereA git push was, generally a certain size for example, is now, no longer true.

**Swyx [00:55:03]:** Oh, yeah.

**Kyle [00:55:03]:** Or

**Swyx [00:55:05]:** I push a thousand

**Kyle [00:55:06]:** On the average. 100%

**Swyx [00:55:06]:** A thousand line commits like daily

**Kyle [00:55:07]:** Same thing with PRs. Like PRs same thing. And like we've talked about optimizing that and making changes where, and there were technology choices that did not work there? And it got slow, and it didn't It was not fast. It did not do what the users wanted. And so we've been reeling that all out and going "Okay, that's just not right. Let's stop putting good money after bad and do it the do it the right way or the right way now." So there's It's a it's a lot of things, not quite when I've experienced scale at GitHub historically, it's almost always two options that we've used. We go vertical scaling, particularly with databases, right? And we go horizontal scaling. Oh, we just have more people using this service. Great. We're going to add more servers, and we rack them in our data center, or we use it in a cloud. And now we're sort of in a like diagonal, where like vertical doesn't really work anymore. Horizontal isn't work either because we're all We all have some CPU or GPU constraints in the world now, and now we have to go in and like crack open services that have been running for 10 or 15 years and go, "Okay, the rules of this service have legitimately changed, and now we have to rewrite them." None of this is an excuse. This is like we're We have to do the work. We have to make it better.

**Swyx [00:56:22]:** actually as an infra guy, I'm "This is like one of the most fascinating scaling challenges I've ever seen."

**Kyle [00:56:26]:** That's that's, that's the thing that's the thing that it's hard for Like when we weren't talking about it publicly, and I was like I came out, and I was "Hey, I just want to explain what's going on." Part of it comes from a very old GitHub ethos, which is it's our it's our uptime. It's down. W What I know you're a developer, so you're, you're inclined to want to understand more what's going on. But at the same time us going "Hey, this service didn't, perform the way we expected, and now we have to go change it," we weren't We're not trying to hide anything from you in that. It's that well, that's our problem because you expect us to be up, and I think that's really baked into the core, origins of GitHub. And so now what we're trying to do as a team is do all that work and just tell Talk about it more and just share you more technical details, write these blogs, write the posts, get the engineers who built it after they finish the work, just tell you "Okay, this is what we did." I think that's the contract that we want to bring back to the community and say, "Hey, we're still very serious about what we're doing. We haven't been telling you about each piece. So let's do that and we're going to keep building this and scaling it in a way to support the If it's not 14, then it's 30 or it's 50 or whatever the next exponential growth is going to be."

**Swyx [00:57:40]:** First of all, fantastic answer. I think

**Kyle [00:57:44]:** And I apologize in advance if like any of that

**Swyx [00:57:47]:** I think it's all nice

**Kyle [00:57:47]:** Is slightly incorrect just simply because

**Swyx [00:57:49]:** No

**Kyle [00:57:49]:** I'm not the I'm still in the weeds with this but it's not my day-to-day. But like that's the thing is we're all looking at it to that level.

**Swyx [00:57:58]:** And obviously, if people want to help, they can join.

**Kyle [00:58:00]:** Absolutely

**Swyx [00:58:01]:** So like I think the that is, good. I think people also would just want to know when are, when are you through the thick of it right? Like is there Have we identified all the issues? Is this just never-ending? Is Git broken? Do we have to change the Git, protocol? Like what how much is breaking, right? It's been a while. And so I think people do want to know What's the path back to the reliability that everyone expects out of GitHub.

## The Reliability Roadmap: Databases, Compute, and Load Testing

**Kyle [00:58:30]:** So like our availability in like recent few weeks has been much better than the three weeks before that or the three weeks before that and so forth. And so a lot of these improvements are still very much paying off for us. I think that we're still working on that that database piece that I mentioned, and that just is a little bit physics a little bit of time to get it to get it fixed up. Because we have to the w

**Swyx [00:58:59]:** My the answer I had in my head Was call YouTube.

**Kyle [00:59:03]:** So YouTube ultimately is

**Swyx [00:59:04]:** 'Cause they also use Vitess.

**Kyle [00:59:05]:** They also use Vitess. But the,

**Swyx [00:59:09]:** Like whoever was the guy, the scaling guy at YouTube?

**Kyle [00:59:11]:** Like that's That I believe went to PlanetScale, and was a part of PlanetScale too. But like

**Swyx [00:59:16]:** Oh, you mean Sugo?

**Kyle [00:59:17]:** I think so. Yeah. And so, and so like

**Swyx [00:59:19]:** He's at Superbase now.

**Kyle [00:59:20]:** Ah.

**Swyx [00:59:21]:** There's a whole Postgres drama Thing there, right?

**Kyle [00:59:25]:** So like some of it's that. I think the other piece of it is, our move to get additional compute will alleviate a fair amount of this particularly on the action side 'cause a lot of the underlying, outages is actually related to,

**Swyx [00:59:39]:** I'll tell you actions is the it's the root of all evil.

**Kyle [00:59:42]:** it's all It has its pros

**Swyx [00:59:47]:** Some extent

**Kyle [00:59:47]:** In that it's the core It's the core compute layer for either CI, side projects, et cetera.

**Swyx [00:59:52]:** Is the main money maker? Like is

**Kyle [00:59:54]:** Actions?

**Swyx [00:59:55]:** No? I don't know.

**Kyle [00:59:56]:** like Actions

**Swyx [00:59:57]:** I pay a lot for compute, right?

**Kyle [00:59:58]:** like Actions is definitely a piece of the overall business, but I would say that like we ultimately also

**Swyx [01:00:06]:** Storage

**Kyle [01:00:07]:** Give away so many like minutes as part of our entitlements as that. But that's what I was saying. Everyone's using it. We talk about it as CI/CD, but the reality is people use it for CI/CD and

**Swyx [01:00:17]:** Automation

**Kyle [01:00:17]:** Various processing and automation, exactly. And so like part of it is also that like compute piece that is also alleviating some of our availability.

**Swyx [01:00:26]:** This is my abuse of, actions. I have been

**Kyle [01:00:29]:** Oh, yeah

**Swyx [01:00:29]:** I have been scraping for every day, and just like I just tell people to

**Kyle [01:00:34]:** Thank you for your service

**Swyx [01:00:35]:** Go dog because I But this is also how I track, actions all time. So anyway,

**Kyle [01:00:41]:** So like some of it's going to be that. I would say that like each month I expect in the next three months, you're going to see fewer and fewer moments where we have an availability problem Where things are going to go down, and that's not just it's stopped. It's that we're still experiencing faster growth than ever before. It's just that those underlying improvements that we've been hard at work on, are finally paying off. It's just that the improvements take-It's less about, these incremental improvements where you make a small change, and you get this big output. It's now material change That takes a bit of time, and then you see a step change in our availability.

**Swyx [01:01:14]:** There's a thing we used to do at Amazon, I don't know if this is, a thing, but, if automated software verification or simulation of load testing and all that. I'm, I'm just like at this point, you have a whole map of GitHub. And, while you can assume whatever growth rates on whatever dimensions that you care about and just run it through a system, right? I feel like there's a way to, I don't know, have a systems model of GitHub and, see what breaks. But obviously, I'm pro-- I'm not that close to the problem, so.

**Kyle [01:01:39]:** But yeah, so yes, totally. And I would say, that's been the journey and work that's been happening since, I would say November to now. Because October, right, was the time where we even said, "Oh, look at the growth," and, and then you start to see the chart

**Swyx [01:01:53]:** It doesn't

**Kyle [01:01:53]:** Really pick up. And it's oh, we tested it at N amount of scale, and now it's at, N cubed maybe like in some in some vectors. And so now we have to go and build it that way and make sure that it can handle all of that scale.

**Swyx [01:02:08]:** Let's talk Copilot. So how many original creators of Copilot are there?

## The State of Copilot: From Code Completion to Agents

**Kyle [01:02:15]:** Oh, geez.

**Swyx [01:02:18]:** 'Cause I count like twelve authenticated.

**Kyle [01:02:19]:** We haven't-- Yeah, I forget, all joking aside, I forget the number of people that were on, the original, GitHub Copilot team. But, there was a bigger group.

**Swyx [01:02:30]:** I heard it's, it's Alex. It there's, there's, a three people

**Kyle [01:02:32]:** Alex worked on it. Udo worked on it. There's a a bunch of people that were on the team.

**Swyx [01:02:35]:** And then their entire management line. Okay. So enormously successful at its in its in its day. I think the last number, I think Mario Came to my conference, and talked about the hundred million dollar mark. I think most recently three hundred. I might be out of date as well there.

**Kyle [01:02:53]:** I don't think we shared the dollar amounts.

**Swyx [01:02:54]:** All right, cool. Just, what's the state of Copilot? It's, it's obviously as a concept brought into More of Microsoft. But just at GitHub.

**Kyle [01:03:03]:** so I think One of, one of the challenges is, that we had with Copilot, right, is that we came out the gate with code completion, and it was super great, powerful, et cetera. And then what we initially worked on after that sort of, initial year and a half, was, going after fine-tuning because our customers, the industry on the whole was really talking about, okay, well, how do we get more more correctness or performance out of this? And so we were working on a whole bunch of efforts to do fine-tuning on, larger and larger code completions or, next edit suggestions with fine-tuning, et cetera.

**Swyx [01:03:43]:** And let me clarify. Is this fine-tuning one model or per customer a fine-tuned model for

**Kyle [01:03:48]:** Per cust-- Well, both. But, but, fine-tuning one model for the overall, use, and then fine-tuning per customer that wants this as, a service effectively. And around that time is when the next generation of models came, and that's around the same time that all these other AI, coding tools came to be because the models really sped up. And so everyone kind of, will ask, "Well, what happened to GitHub Copilot?" there's all this time, and I would say that we were on an era of going okay, we want to improve everyone's results, and so let's focus in on fine-tuning because that'll give us these better results. And then the models got better. And so then ever since, we've been really on this kind of journey to go, okay of course, we have, this great code completion, and we've done a ton of investment in the better underlying models that we have post-trained better, next set of suggestions with post-training language specific models. All this stuff that kind of, sits in the ether of GitHub Copilot is code completion, but also have now ha-- now have, a single underlying, SDK and harness for our coding agent Copilot ultimately. The new CLI, the new desktop app, cloud agents that use the same SDK. And so there was this moment of both, really trying to figure out what our customers want, models, Sherlocking us a little bit, then going and saying, "Okay, what does everyone ultimately need?" And what we think is that it's not solely about the code generation. It's really about having the ability to use these coding agent brained, harnesses or run times across, not just the coding experience where I'm going to, send a bunch of tasks out, or I'm going to use Fleet to break up a single task or autopilot similar to Goal all this stuff. But also how do I do that for all of my security remediation? How do I do that for every GitHub issue that comes in, just stick a coding agent on it just to see if it's possible? How do go through my repository and see all of my documentation and extract out okay, this doesn't actually match? That amount of sort of AI coding agent automation, I think is a big part of what we see when we're looking at, okay, we're still kind of going through a similar but very different flow. It's just all happening at the same time. There's not really the same, I'm going to create an issue to track my idea of building this. You're probably just going to go, do it.

**Swyx [01:06:22]:** Just do it.

**Kyle [01:06:22]:** You're going to say, "Hey, just build this," right? And, there are still tons of, open issues and projects, et cetera, that are using issues like Peter and OpenClaw to be able to sic all of his agent on that. That kind of infrastructure layer and a really great coding experience that allows you to handle the sort of multiplexing, aspect is what we've built, are still building with GitHub Copilot. And so for folks that haven't really used GitHub Copilot sinceThe thing that got them excited about this Which I I get. I really encourage you to, look at especially the GitHub, Copilot app. That's my new daily driver. I obviously, if you prefer the CLI, also the CLI, be able to use all the models, the bring your own key side of it. We're still improving our own models and using those too. And, it's just like a very different experience, but I think that broader sense is of like software development and how coding agents can help throughout, not just Writing the code, or even verifying it or deploying it is is where we have this unique, angle. The other side is the context piece. Like

## Copilot's Future: Context, Taste, and Personal Developer Workflows

**Swyx [01:07:44]:** Oh, God

**Kyle [01:07:44]:** we're still It's like one of those things where I think the the final thing that will let me ultimately, feel complete at GitHub is, when we have this ability for GitHub to act like Kyle wants it to act Or Shawn or whatever. And we all codify that in rules and in memory and everything else, but

**Swyx [01:08:03]:** Well, that's an open research problem, right? Like it's

**Kyle [01:08:05]:** A hundred percent. A hundred percent

**Swyx [01:08:07]:** AGI when you get it. Yeah.

**Kyle [01:08:07]:** A hundred percent. But, if we can even just do it where my team, Without me having to codify everything, and as our methods shift on purpose to be able to have that full experience and all the understanding of what's happening in my dependencies or open source, that feels like a big place for us to be able to continue to provide something really unique and valuable with GitHub Copilot.

**Swyx [01:08:29]:** Is there a form factor that we haven't explored? I think like we did code completion Then we did kind of let's broadly call it agentic IDE Which Cursor Famously popularized, and then now it's, now it's all about the sort of agent orchestration Background agent, whatever. And then there's the security review. I feel like everyone's like just throwing agents at everything. The entire SDLC has Just, covered with agents. Are we like at the end of history here, basically? Like is it just refinements from here on out?

**Kyle [01:09:04]:** I think that we're all still in such this hypermyopic era of AI Where the reality is that for various, boring security and governance reasons at least for most people's work, why is my coding agent, even if it's all background agents, background running not, losing all the context that's available to it across everything that I'm doing outside of coding? I think the most interesting thing to me in AI is actual ambient AI, not insert assistant name thing or, I've tried just about every pin in tool and whatever, and they don't work the way that I'm looking for them to work because they are just trying to capture, and then they are trying to codify and then recall. And I think the thing that I'm looking for, back to the very beginning, I'm looking to be building out the next version of webhooks or, implementing a new feature, and it for it to know every spec doc, every email, the conversations that I've had online, everything about how this could be implemented and be able to, use that as part of its decision-making and none of these tools are ultimately doing this. So I think that it's as if, software development work was a single lane task, was like it only needs a developer. Once I once I write the perfect code, we'll be done here, but that's just never been true. It's all the context of the other team members, what the business is doing what's popular right now, and I think that's this huge opportunity for us to go much broader than really excellent coding agents? And that is honestly why I think OpenClaw has been so interesting is that sure, it's connecting to all the data, sources that Kyle the human cares about, and now my question's "Okay, how can I take all that and use that every day as a software dev connected together, not just have a new way to kick off a coding agent?" And that's where we're at. We're saying, "Okay, I'm going to go use this CLI under the hood or this SDK," but that's not what I'm talking about. I'm talking about I'm having a conversation with you it downloads the podcast, and it realizes, "Oh, Kyle, sounds like Kyle needs this app or this thing or this " That level of

**Swyx [01:11:16]:** Just recommends it.

**Kyle [01:11:16]:** That level of, that level of connectivity I think is where we still have a ton of ways to go in software because then when we have that red thread we want to pull, that idea, it can not only use the perfect way to write that code, but instead all of the sort of taste and judgment calls and expertise that I've earned or that we've earned as a group and use it as part of the actual implementation.

**Swyx [01:11:42]:** The extreme of it is AI runs your life, right? And I think there's a scary inversion of control in the way that I literally doing it in the way that developers mean it in terms of frameworks Like the Hollywood principle, "Don't call me, I'll call you." Like there at some point there is an inversion of control where, you should you stop telling what the AI, the AI what to do. AI tells you what to do. And, that's a little bit scary, but also, maybe better.

**Kyle [01:12:10]:** like Nat, I think Nat Friedman shared this in a like a Stripe event like talking about his OpenClaw was, he connected OpenClaw to his cameras, and it was, watching him.

**Swyx [01:12:20]:** It redirected his Uber. And it,

**Kyle [01:12:23]:** there's a degree of this where I was I actually would love OpenClaw to tell me to Drink water. I don't know that I want it to be, Changing where my car goes, but I do think that's kind of what I'm talking about, which is it needs to have so much more information at its disposal for it to be helpful to me, and I still don't think we're, anywhere near talking about AGI. I'm just talking about every time I have to tell you something I care about that I've ever kind of said or I've said a dozen times, it should be able to know that codify that or gain access to it. Like the dreaming ideas, are an attempt to kind of do some version of this but I think there's a much more proactive angle that will help software devs if we can test that out a bit more.

## OpenClaw, Ambient AI, and Inverting Control

**Swyx [01:13:05]:** Yeah. Well, the other thing about OpenClaw that reminded me Is Microsoft has a CVP Dedicated to OpenClaw. Why?

**Kyle [01:13:16]:** Because you don't think they should?

**Swyx [01:13:17]:** I don't, I don't know. I think CVP is a high title. What, why is this so important? Like Microsoft Doesn't even own OpenClaw. What's, what's the

**Kyle [01:13:29]:** so I-- we're talking a lot more about this at, Microsoft Build this year too. I think, the main thing is that what OpenClaw has done is it has made this connection for people to have access to the resources that you have access to and be able to do things for you in a way that previously people were trying to codify into their own agents. And so when you think about it like in the work context, wouldn't it be great to have a Claw-like object that I could actually run on my work device that or had access to my work assets, made-- worked well on Windows what that would look like. And so I think that OpenClaw has become the personification of, a valuable agent that understands me because it has access to all of my information, and it can use a computer. And so thus it can do a lot more than, just a task-oriented process or like a a chat tool, et cetera. And that's like a bunch of the goal of Build, right? We're at Build this year trying to take a very different approach of it's unapologetically aimed at developers. We're trying to show the bigger investment to not just say, "Hey," like you said, "Why do you have a CVP of OpenClaw?" Well, because, one of the problems that we have, right, is that our agents, if you install them not on a Mac Mini or not on a hosted device, you install them on a personal device or a work device, we need better sandboxing at the OS level. I need to be able to use that Claw and not, get fired. And so Microsoft is "Okay, great, let's, do that too." And then it's, okay, well, where should I be able to talk to this agent? Should each of us just have a Claw available to us at work? Probably. And so there you go. And continuing to contribute a ton to the open source project too. Microsoft, I think as I've gotten more and more, information there's so much investment into the open source, projects themselves that for whatever reason just I think there's like this they don't want to come off those teams don't want to come off as like taking any credit or getting any recognition. But so many of these core contributors or teams are full-time just pushing into open source projects. And, I think that's, that kind of shows the difference between, well, why are we looking so hard at something like Claw? Why are we looking at sandboxing on Windows? Why are we looking at cloud versions of sandboxing? Why are we looking-- Because ultimately, we need more platform components. We don't need everyone to be building the same exact, top-line product. And so if we're building for builders, that requires us to give you all these components and tell you what they are and how they work and why you should be interested versus only delivering that single vertical over and over and over again.

## Microsoft, Windows Sandboxing, and Platform Components for Agents

**Swyx [01:16:23]:** I think, my maybe one way of framing it Is that Microsoft is the original operating systems company. And here is the new operating system for AI.

**Kyle [01:16:35]:** like I think that we are also in an era where we are-- we need to help build that bridge? All joking aside operating systems need to look different than they looked five years ago because it's not just you using them anymore. And that's changed the whole idea. It's not, "Okay, my Claw is going to create a user account." Doesn't work like that? And so just just like all of us, we all have to look much more deeply in the stack, all the way down to, the silicon layer in Azure to be "Okay, well, What do we need now?" 'Cause the workloads are different. It's not just, "Okay, we need more inference." It's, "Okay, well, what type of inference do we need? What type of compute do we need to run these agents or run these agentic flows?" it's a really interesting kind of like multi-layer problem, versus kind of, I would say software in the last five or six years were all going to our events, and we're kind of saying a version of the same thing. SaaS product has new SaaS thing. It's the best SaaS thing ever.

**Swyx [01:17:42]:** It was boring for a while.

**Kyle [01:17:43]:** And so now it's like Oh my goodness, we're at physics.

**Swyx [01:17:47]:** It's great.

**Kyle [01:17:48]:** We're at physics problems. And that's exciting.

**Swyx [01:17:50]:** We're-- we're now trying to make, semicondu- room temperature superconductors. Still. That's, that's, that's never going away. No, I think, that's a really good overview of, everything. I think, have I have we left anything unsaid that you wanted to really get out there that we should cover?

## Build Announcements, Enterprise Adoption, and AI at Work

**Kyle [01:18:07]:** I'm really excited by for folks checking out, checking out the announcements that we have at Build go you can go look at them online, take a look. I think that I'm hoping that it's driving, a degree of curiosity and interest because there's such this big shift that we're making at Microsoft for developers, where if you're a daily driver of a Mac device or a Linux device, and you're "Okay, I don't use Windows," there's improvements that are being made that I think are going to surprise folks to just be "Oh, that's in-- they really want to do that?" not, And I'm talking for developers. I'm not talking for I play video games on the weekends on my Windows computer. I'm talking my daily driver. Like-All the way from that to, okay, well, what is it like to build an agent or build an app and deploy it and run it at work in particular? I think that is a big piece of it where I talk all the time with the team how I build on the weekend should be how I build at work. But if you're working at a Fortune one hundred or a Fortune five hundred, you're probably not vibe coding an app and then shipping it to some service. You got to go through security and compliance. How can we move just as fast at work? And that's, I think, something that we have a bunch of different offerings for to give you that same sort of agility and power, but in the work context. And then I will tell you I've mentioned it a couple times, and, it's very freaking cool. If you are in the M365 land in any way, check out WorkIQ, check out FoundryIQ. These little, oversimplifying it context engines are wild good. And, we've given them to our developers at GitHub, we've given them to employees at GitHub as we've used these tools to be able to just ask questions around everything that you have in your work context. And with FoundryIQ, be able to just do the same exact thing across all your existing stores. What-- Not move to new tools, just connect them in. It's surprisingly powerful, and you your boss is still not going to get fired, and IT is not going to turn it off because it's leaking all this private information. That is the trick that I think, is sometimes getting lost when we're talking about all these all these great new platforms. 'Cause I can use them, I'm "Oh, this is super powerful. Oh, and I can't I can't use it." and it's Not because I'm at work at GitHub. It's be

**Swyx [01:20:34]:** 'Cause I'm not allowed, yeah

**Kyle [01:20:35]:** It's 'cause I'm not allowed, because they can't do all the things that large, complicated companies need. And so, whether it be I said, just the kind of interesting daily driver curiosity all the way through to, "Oh, my gosh," "I can go use this at work tomorrow potentially," and have that context layer, have that intelligence, it's a huge, it's a huge shift. And so check it out. I'd love to hear-- I'm, I'm not shy on social. I'd love to hear feedback. What's working what's not. But hopefully surprise folks a little bit.

**Swyx [01:21:07]:** What I'm hearing-- so first of all, I think that's, that's a great pitch. What I'm hearing, actually, is that you should put the WorkIQ people next to the Copilot people. 'Cause, the exact prob- context problem that you named They solve enough for you to do your job, which is nuts.

**Kyle [01:21:23]:** So, the thing that we are lit-- that's literally what has been Happening the last several months.

**Swyx [01:21:29]:** I already forecast you were going there.

**Kyle [01:21:30]:** It's totally 'cause, you're totally right. The code, the code and the code asset problem is a little bit unique. But otherwise

**Swyx [01:21:36]:** That's it

**Kyle [01:21:37]:** We're all working

**Swyx [01:21:37]:** It's context

**Kyle [01:21:37]:** With each other now. It's all just context, exactly.

**Swyx [01:21:40]:** Amazing. Great. I'm going to be there. I'm going to be doing

**Kyle [01:21:43]:** Great

**Swyx [01:21:43]:** A couple sessions there. I'm going to be interviewing Satya.

**Kyle [01:21:46]:** I know.

## WorkIQ, Copilot Context, and What to Ask Satya

**Swyx [01:21:47]:** When I first started the pod, though, I had, Jeff Dean on. Jeff like It's like hall of fame of People I want to meet someday. Satya's on there. So, what should I ask Satya?

**Kyle [01:21:57]:** I think, I think that the best question to ask is what he thinks is true in, two or three years from now. It seems like such a throwaway question. But ultimately, the way that the way that he is looking at this AI problem in, inference problem, token problem, and what we're how we're actually going to be working I think you can see some of the recent shifts that have been happening inside of Microsoft to kind of drive us to a place where it's not four, five, six, seven, eight different things. It's not a lack of context everywhere. But, why is this sort of approach in two years going to, pay off? Because that I think

**Swyx [01:22:41]:** Wow, that's a bold Okay. I'll ask it. I'll say you I'll say I prompted by you but

**Kyle [01:22:45]:** Absolutely

**Swyx [01:22:45]:** It's a bold question because there, I think there's a lot of, doubts to be honest, Externally. And so, yes, I want, a straight answer from him on that I think would reassure a lot of people, and honestly, give me a lot of food for writing. So, thank you so much for spending your time. Thank you for doing what you do. I think as a CEO, you don't need to be the external face. But, because you are authoritative, 'cause you have so much background with GitHub, and it's so authentic, we on the outside feel it. So thank you for that.

**Kyle [01:23:16]:** Of course. Appreciate it. Thank you so much, Sean.

---

## [[AINews] NVIDIA Cosmos 3, Nemotron 3 Ultra, and RTX Spark](https://www.latent.space/p/ainews-nvidia-cosmos-3-nemotron-3)
*🔬 Latent Space | 2026-06-02*

[Today's podcast guest](https://www.latent.space/p/video-agents) was the lead on NVIDIA Cosmos over a year ago, discussing training videogen and world models. Fittingly, Cosmos 3 launched today, unifying language, image, video, audio and action in a [Mixture-of-Transformers architecture ](https://x.com/victormustar/status/2061354267546427595?s=20)that pairs an autoregressive reasoner with a diffusion generator in:

  * **base Nano** (16B: 8B reasoner tower + 8B generator tower) 

  * **Super** (64B: 32B reasoner tower + 32B generator tower) models, and

  * Super finetunes for **Text2Image** and **Image2Video** , which are now the [new SOTA open weights imagegen and videogen models](https://x.com/ArtificialAnlys/status/2061494719998546206?s=20), just [below Nano Banana 2](https://x.com/victormustar/status/2061354267546427595?s=20)




At Computex in Taiwan, Jensen also brought the heat with [Nemotron 3 Ultra](https://x.com/NVIDIAAI/status/2061495149872771568/photo/1), their 550B-A55B, remarkably efficient/[fast](https://x.com/ArtificialAnlys/status/2061304911565144230?s=20) open weights LLM that is the new US SoTA:

[](https://substackcdn.com/image/fetch/$s_!5bzA!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff6685277-4569-4135-92cb-e7a645246125_4096x2732.jpeg)

Finally, the RTX Spark personal computer 1 petaflop superchip, was previewed with [Microsoft](https://x.com/satyanadella/status/2061315017589600699) and [OpenClaw](https://x.com/openclaw/status/2061331260279054801?s=20) and [Hermes Agent](https://x.com/NousResearch/status/2061323987804713083?s=20) as a launch partner (good analysis [here](https://x.com/PatrickMoorhead/status/2061452151944274167))

> AI News for 5/30/2026-6/1/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

# **AI Twitter Recap**

**NVIDIA 's Cosmos 3, Nemotron 3 Ultra, and the Push for Open Physical AI**

  * **NVIDIA 's open-source week**: NVIDIA dominated the open-model conversation with **Cosmos 3** , an open family of **omnimodal world models for physical AI** , plus the announcement of **Nemotron 3 Ultra** , a **550B** open-weight model that several posters called the strongest U.S. open model so far. Cosmos 3 was framed as a full-stack release--**weights, code, datasets, and fine-tuning recipes** --with NVIDIA also launching the **Cosmos Coalition** alongside partners including **Runway** to build an open ecosystem for world models [@NVIDIAAI ecosystem context](https://x.com/NVIDIAAI/status/2061498958283968735), [@runwayml coalition announcement](https://x.com/runwayml/status/2061315089869721682), [@kimmonismus Cosmos thread](https://x.com/kimmonismus/status/2061432501223162241), [@ClementDelangue on NVIDIA's HF footprint](https://x.com/ClementDelangue/status/2061487081315094906).

  * **Why Cosmos 3 mattered technically** : Beyond robotics rhetoric, the more concrete details were that Cosmos 3 unifies **language, image, video, audio, and action** in a single **Mixture-of-Transformers** design pairing an **autoregressive reasoner** with a **diffusion generator**. [Artificial Analysis](https://x.com/ArtificialAnlys/status/2061494719998546206) said Cosmos 3 reached **#1 among open-weight models** on both their **Text-to-Image** and **Image-to-Video** leaderboards, noting the generator uses **structured JSON prompts** and can be driven either by an external prompt-upsampling harness or its own reasoner branch. Separately, NVIDIA's hardware + software push extended to adoption of the **OpenMDW** framework and partner ecosystem integrations on platforms like fal [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2061494719998546206), [@fal](https://x.com/fal/status/2061604121786876307).

  * **Nemotron 3 Ultra reception** : Community reaction to **Nemotron 3 Ultra** was unusually strong for a fresh open release. Posters highlighted both capability and serving characteristics, including claims that it is already topping some open evals and may be serving at **300+ tok/s** in some setups--far faster than large DeepSeek/Kimi-class models [@scaling01](https://x.com/scaling01/status/2061379856433107135), [@ctnzr](https://x.com/ctnzr/status/2061483152741175757), [@caspar_br](https://x.com/caspar_br/status/2061505720907182280). There was also some technical discussion that Nemotron appears **less sparse** than peers like Kimi K2 / DeepSeek V4--roughly **~10% active** vs **~3%** --which could affect both economics and behavior [@eliebakouch](https://x.com/eliebakouch/status/2061607195268038777).




**MiniMax M3, Qwen3.7-Plus, and JetBrains Mellum2 Expand the Open Agent Model Field**

  * **MiniMax M3 's launch was the day's biggest model release**: M3 was presented as an open-weight multimodal agent/coding model with **1M context** , **native multimodality** , and competitive agent benchmarks. The headline figures repeated across launch partners were **59.0% SWE-Bench Pro** , **66.0% Terminal Bench 2.1** , and **74.2% MCP Atlas** [@MiniMax_AI](https://x.com/MiniMax_AI/status/2061425142795034794), [@PBDTokenRouter](https://x.com/PBDTokenRouter/status/2061463048485838935), [@kimmonismus](https://x.com/kimmonismus/status/2061473350766170420). Multiple infra vendors shipped day-0 support--**Novita** , **Vercel AI Gateway** , **Cloudflare AI Gateway** , **OpenClaude** , **Flowith** , and others--suggesting unusually fast ecosystem adoption [@MiniMax_AI on Novita](https://x.com/MiniMax_AI/status/2061398427121201648), [@rauchg](https://x.com/rauchg/status/2061593874498531707), [@gitlawb](https://x.com/gitlawb/status/2061581678871806083).

  * **Benchmarks vs practical experience were mixed** : M3 earned praise for frontend generation, visual/game tasks, and price-performance, with side-by-side demos showing strong one-shot UI/game outputs and notable benchmark placement for Next.js agent evals [@notjazii](https://x.com/notjazii/status/2061407087293313210), [@lostinlatencyX](https://x.com/lostinlatencyX/status/2061409696649548165), [@rauchg](https://x.com/rauchg/status/2061593874498531707). But several evaluators also reported **high token consumption** , **verbose self-check loops** , and occasional **requirement drift** on long tasks, making M3 look more like a "quality first, efficiency later" model [@ZhihuFrontier review](https://x.com/ZhihuFrontier/status/2061493401019957337), [@teortaxesTex skepticism](https://x.com/teortaxesTex/status/2061432151183171702).

  * **Qwen3.7-Plus** : Alibaba launched **Qwen3.7-Plus** as a **multimodal interactive hybrid agent** that unifies **GUI and CLI operation** , visual reasoning, coding, and search-augmented QA. It is **API-available** via Alibaba Cloud Model Studio and was quickly added to tools like **Cline** [@Alibaba_Qwen launch](https://x.com/Alibaba_Qwen/status/2061506641120641494), [@cline](https://x.com/cline/status/2061580233778790439). The launch reinforces the trend that open-ish Asian labs are no longer releasing "just chat models," but full **agent-capable multimodal systems**.

  * **JetBrains Mellum2** : JetBrains released **Mellum2** , a **12B MoE** model with **2.5B active parameters** , trained on roughly **11T tokens** and post-trained with **RLVR** , shipping **base / SFT / RL checkpoints** and a technical report [@nv_pavlichenko](https://x.com/nv_pavlichenko/status/2061438808290172935), [@jetbrains](https://x.com/jetbrains/status/2061444430884675791). The intended niche is especially interesting: **ultra-low-latency inference** for **routing, RAG, sub-agents, and IDE use** , and it landed in **vLLM** immediately [@vllm_project](https://x.com/vllm_project/status/2061621691995005301#m). This looks like a serious "small fast open model for developer workflows" play rather than a benchmark-chasing frontier release.




**Agents, Sandboxes, Memory, and Search Are Becoming the Real Product Surface**

  * **The stack is shifting from model calls to agent runtimes** : Several launches converged on the idea that the main engineering leverage is now in the **harness** rather than the model. **Perplexity 's "Search as Code"** is the clearest example: instead of iterative search tool calls, the model writes **Python** against a search SDK, enabling custom ranking pipelines, map-reduce over indexes, batching, aggregation, and lower token overhead. Perplexity reports a jump on its internal **WANDR** benchmark from **0.152** to **0.386** with this architecture [@perplexity_ai](https://x.com/perplexity_ai/status/2061506359326384319), [@AravSrinivas](https://x.com/AravSrinivas/status/2061575845056278971).

  * **Managed agents + sandboxes are becoming standard** : Google detailed **Managed Agents in the Gemini API** , where a single API call can spin up an agent that reasons, writes/runs code, manages files, and operates inside a hosted **Linux sandbox** [@_philschmid](https://x.com/_philschmid/status/2061457703210197273), [@GoogleAIStudio](https://x.com/GoogleAIStudio/status/2061452967530701090). LangChain pushed similar ideas around **Deep Agents** , **Context Hub** , and **LangSmith Sandboxes/Engine** , emphasizing persistent context, agent lifecycle tooling, and automated failure triage [@LangChain](https://x.com/LangChain/status/2061432934993674267), [@hwchase17](https://x.com/hwchase17/status/2061496556608504043).

  * **Memory remains a missing primitive** : One recurring complaint was that enormous context windows still don't solve **cross-session memory**. A thread on **HydraDB** argued that "RAG + manual context injection" has been misnamed as memory, while actual persistent session knowledge remains underserved [@kimmonismus](https://x.com/kimmonismus/status/2061454202883432501). Related research threads pointed to reusable context management policies like **AdaCoM** , which trains a separate LLM via RL to prune/preserve context for frozen agents [@dair_ai](https://x.com/dair_ai/status/2061455253325971789).

  * **Security remains the gating issue for enterprise agents** : There was a notable warning from Microsoft Security Intelligence about a major **npm supply chain compromise** affecting **90+ redhat-cloud-services packages** , including a self-propagating worm stealing npm/GitHub/AWS/SSH credentials [@MsftSecIntel](https://x.com/MsftSecIntel/status/2061485730958848188). At the same time, enterprise agent vendors highlighted **sandboxing** , **runtime isolation** , and **security stack integration** as prerequisites for deployment, including discussion of **NVIDIA OpenShell** and LangChain's sandbox keynote [@shannholmberg](https://x.com/shannholmberg/status/2061368566256189656), [@LangChain](https://x.com/LangChain/status/2061448130806116827).




**Codex, Claude Code, and the Competitive Coding-Agent Race**

  * **OpenAI extended Codex into more places** : OpenAI announced that **frontier models and Codex are now generally available on AWS / Amazon Bedrock** , aimed squarely at enterprises that want OpenAI capabilities inside existing AWS security/compliance workflows [@OpenAI](https://x.com/OpenAI/status/2061564502160892138), [@OpenAIDevs](https://x.com/OpenAIDevs/status/2061564710173224985). OpenAI also shipped a **Codex Python SDK** supporting threads, turns, streaming, resume, images, and sandbox control [@reach_vb](https://x.com/reach_vb/status/2061569472792572163), plus support for Bedrock-backed Codex workflows [@reach_vb on Bedrock config](https://x.com/reach_vb/status/2061572961451094191).

  * **Claude Code had a real ops incident** : Anthropic reset **5-hour and weekly rate limits** for Pro and Max users after fixing a bug where some **Opus 4.8** sessions spawned too many **parallel subagents/tool calls** , burning usage unexpectedly [@ClaudeDevs](https://x.com/ClaudeDevs/status/2061501787769893055), [follow-up](https://x.com/ClaudeDevs/status/2061501790131265803). That's a notable reminder that coding-agent product quality is increasingly determined by orchestration behavior, not just raw model IQ.

  * **Behavioral differences across coding models remain material** : Developers highlighted large qualitative differences between GPT, Claude, and other models on benchmarks like **ProgramBench** and **WeirdML** , with Opus sometimes preferring exploration over score-maximization or showing benchmark-specific quirks [@OfirPress](https://x.com/OfirPress/status/2061458258821251081), [@htihle](https://x.com/htihle/status/2061412097720774679). A separate long thread argued newer **Claude Opus 4.6 -4.8** variants can fabricate plausible but fictional concepts in non-coding domains, suggesting possible truthfulness/alignment regressions rather than ordinary hallucinations [@distributionat](https://x.com/distributionat/status/2061362406971060244).




**Infra, Hardware, and Local AI Systems**

  * **NVIDIA is coming for the PC** : The most-discussed hardware launch was **RTX Spark** , an NVIDIA/Microsoft "personal AI computer" built around **Grace + Blackwell** , with up to **128GB unified memory** and claimed **1 PFLOP FP4**. The key strategic read: NVIDIA is no longer just selling accelerators, but an end-to-end local AI system that competes with **Apple Silicon** , x86 PCs, and Qualcomm simultaneously [@kimmonismus](https://x.com/kimmonismus/status/2061484174088007739), [@swyx](https://x.com/swyx/status/2061567877879369953).

  * **Cluster/networking updates** : On the datacenter side, **Lambda** said it is first to adopt **NVIDIA Quantum-X InfiniBand Photonics Q3450-LD** switches, pushing co-packaged optics to reduce network power and failures in large AI clusters [@LambdaAPI](https://x.com/LambdaAPI/status/2061319330433032658). **OpenAI** also announced **Stargate Michigan** , a planned **1GW** data center using closed-loop cooling and paired with workforce/education commitments [@OpenAINewsroom](https://x.com/OpenAINewsroom/status/2061533639138316314).

  * **Local open-model tooling is improving fast** : The **MLX-VLM v0.6.0** release was one of the more substantive local inference/tooling updates, adding speculative decoding, Anthropic-style and responses-style APIs, tool calls, support for many new multimodal models, and image/audio features with the explicit pitch of turning Apple devices into "real local agent machines" [@Prince_Canuma](https://x.com/Prince_Canuma/status/2061541992790683726). That pairs well with growing DGX Spark + **vLLM** experimentation for local NVFP4 MoE serving [@vllm_project](https://x.com/vllm_project/status/2061530659160838549).




**Top Tweets (by engagement, filtered for technical relevance)**

  * **Anthropic 's IPO path**: Anthropic said it has **confidentially submitted a draft S-1** to the SEC, opening the door to an IPO pending review [@AnthropicAI](https://x.com/AnthropicAI/status/2061478052257841495).

  * **Claude Code usage incident** : Anthropic reset user rate limits after an **Opus 4.8 parallel subagent/tool-call bug** caused excessive quota burn [@ClaudeDevs](https://x.com/ClaudeDevs/status/2061501787769893055).

  * **Qwen3.7-Plus** : Alibaba launched a **multimodal agent model** spanning GUI/CLI operation, coding, and visual tasks [@Alibaba_Qwen](https://x.com/Alibaba_Qwen/status/2061506641120641494).

  * **OpenAI on Bedrock** : OpenAI models and **Codex** are now available through **Amazon Bedrock** for enterprise workflows [@OpenAI](https://x.com/OpenAI/status/2061564502160892138).

  * **ARC-AGI-3 movement** : **Claude Opus 4.8** posted a new SOTA on **ARC-AGI-3** at **1.5%** , still tiny in absolute terms but a meaningful jump on that benchmark [@arcprize](https://x.com/arcprize/status/2061512025638121516).




* * *

# **AI Reddit Recap**

## **/r/LocalLlama + /r/localLLM Recap**

### **1\. New Frontier Model Releases and Early Tests**

  * **[MiniMax M3 - Coding& Agentic Frontier, 1M Context, Multimodal](https://www.reddit.com/r/LocalLLaMA/comments/1ttdiq0/minimax_m3_coding_agentic_frontier_1m_context/)** (Activity: 1090): **MiniMax M3 is announced as an** _**open-weight**_**frontier model with coding/agentic focus, native multimodality/vision, and MiniMax Sparse Attention for up to**`1M`**tokens of context with a guaranteed**`512K`**minimum ([MiniMax M3](https://www.minimax.io/models/text/m3)). Claimed long-horizon agentic results include 12-hour ICLR paper reproduction, Hopper FP8 GEMM CUDA/Triton optimization reaching **`9.4×`**speedup after**`147`**iterations, and PostTrainBench ranking third behind Opus 4.7 and GPT-5.5; access is currently via API/MiniMax Code, with HuggingFace/GitHub weights/local deployment planned.** Commenters are cautiously interested in the combination of cheap/efficient vision plus long-context agentic coding, but skeptical because the announcement calls it _" open-weight"_ while not yet exposing weights or even parameter count. One technical debate is whether the results imply a much larger-than-`~250B` model, extreme benchmark optimization, or a genuine open-weight breakthrough.

    * Commenters focused on the missing release details: despite the claim of being _" the first open-weight model with three frontier capabilities"_, users could not find actual weights, parameter count, or sizing information for **MiniMax M3**. One commenter linked a preview image from the announcement ([Reddit image](https://preview.redd.it/fej3vn94qk4h1.jpeg?width=3808&format=pjpg&auto=webp&s=83ef24ab093520eb3118dd918259adff4f42a569)), but the thread still lacked confirmation of model scale or downloadable artifacts.

    * A technically substantive concern was that the advertised capability level implies one of three possibilities: **a much larger-than-expected model** , unusually strong benchmark optimization, or a major open-weights breakthrough. The speculation centered on whether MiniMax M3 is actually around `~250B` parameters or significantly larger, and whether its coding/agentic/multimodal claims will hold once weights and independent benchmarks are available.

  * **[NVIDIA announces Nemotron 3 Ultra](https://www.reddit.com/r/LocalLLaMA/comments/1tthkh5/nvidia_announces_nemotron_3_ultra/)** (Activity: 621): **The[image](https://i.redd.it/f79wu6dnml4h1.jpeg) is a technical announcement slide for NVIDIA Nemotron 3 Ultra, described in comments as a MoE **`550B-A55`**model. The slide positions Nemotron 3 Ultra against open/open-weight competitors including GLM 5.1, Kimi K2.6, and Qwen3.5 across "Frontier Smart" benchmark categories such as agent productivity, coding, instruction following, knowledge work, and long-context capability.** Commenters viewed the comparison against other open-source/open-weight models positively, while one noted an "artificial analysis score" of `48`, placing it just below frontier-tier models and around the MiniMax 2.7 range, with the expectation that it could be the strongest U.S. open-weight model.

    * NVIDIA Nemotron 3 Ultra is identified as a **MoE**`550B-A55` model, implying roughly `550B` total parameters with about `55B` active parameters per token. This architecture detail is the most concrete technical spec mentioned in the thread.

    * A commenter cites an **Artificial Analysis score of**`48`, placing Nemotron 3 Ultra "one notch less than frontier" and roughly in the **MiniMax 2.7** range, while suggesting it may be the strongest **US open-weight** model by that metric.

    * Technical references shared include NVIDIA's official Nemotron 3 Ultra Base usage cookbook on GitHub: [NVIDIA-NeMo/Nemotron](https://github.com/NVIDIA-NeMo/Nemotron/tree/main/usage-cookbook/Nemotron-3-Ultra-Base), plus the LifeArchitect model comparison table: [lifearchitect.ai/models-table](https://lifearchitect.ai/models-table/). One commenter argues the comparison against **Qwen3.5** is notable because Nemotron may be NVIDIA's best open-weight model while still trailing several non-US/open models.

  * **[Stepfun 3.7 Flash is very good](https://www.reddit.com/r/LocalLLaMA/comments/1tss9nq/stepfun_37_flash_is_very_good/)** (Activity: 473): **The[GIF](https://i.redd.it/k37ol07vfg4h1.gif) is a technical visual demo, not a meme: it shows the output of Stepfun 3.7 Flash for the prompt **`create a beautiful, relaxing flight simulator in a single html page`**, rendering a low-poly 3D flight scene with HUD-style speed/altitude indicators. The OP says this was the official**`Q4_X_S`**quant and claims the model feels near GLM 5.1 in aesthetics and about**`80%`**of its 3D world understanding, while using only roughly**`25%`**of GLM 5.1 's parameters and including built-in vision.** Commenters mostly reacted with comparisons and nostalgia rather than deep benchmarks: one referenced the old Excel flight simulator, while another compared interest in **Qwen 3.7 Max / 27B** and asked whether it beats **Qwen3.6 27B**.

    * A commenter draws a model-comparison angle by referencing **Qwen 3.7 Max** and hoping for a future **Qwen 3.7 27B** release, while another asks whether Stepfun 3.7 Flash is better than **Qwen3.6-27B**. The thread includes screenshot evidence for the Qwen3.6-27B reference ([image](https://preview.redd.it/h1jbx5tz4j4h1.png?width=1523&format=png&auto=webp&s=c4bd572a0741fcffc65f2b75153efbb603ede82b)), but no quantitative benchmark scores or reproducible eval details are provided.




[ Read more ](https://www.latent.space/p/ainews-nvidia-cosmos-3-nemotron-3)

---

## [Why Video Agent models are next — Ethan He, xAI Grok Imagine](https://www.latent.space/p/video-agents)
*🔬 Latent Space | 2026-06-01*

_We 're announcing [AIEWF](https://ai.engineer/wf) speakers this week! Take the [AI Engineering Survey](https://notion.qualtrics.com/jfe/form/SV_bP07tSVMXH7ePCS)!_

* * *

Today's guest Ethan first joined us for the LS Paper Club as the lead on [NVIDIA Cosmos World Model](https://www.youtube.com/watch?v=og59L4JECz4&pp=ygUWbGF0ZW50c3BhY2V0diBldGhhbiBoZQ%3D%3D), but then joined xAI and built Grok Imagine in 3 months:

He comes back on Latent Space with some nuclear hot takes: that **Video Models primarily get their intelligence from LLMs** , not from training on video data, and that the next frontier for truly interactive, realtime, long-horizon **world models** is to work on LLMs (perhaps [Interaction Models ](https://www.latent.space/p/ainews-thinking-machines-native-interaction)as well…)

Put it this way: In the near term, the next Sora won't be a better video model, but **a video agent**.

**[Generative Media](https://www.youtube.com/watch?v=t4359sKBu4w&list=PLcfpQ4tk2k0VjKRy3q6ZxeOtkbZlmFDLg)** may more closely follow **the evolution of AI coding** which went from focusing on one-shot output performance and cost, to multiturn reasoning and planning models for agents and systems that can plan, edit, test, debug, and submit PRs.

At a certain point, coding models got so good that the only significant next step to improve performance was **handling the orchestration of these models.**

Now as the performance of video models increases significantly across realism, consistency, & prompt adherence while becoming more cost efficient, the next evolution of video generation may also be systems that can plan, generate, edit, critique, and iterate across an entire creative task. 

In this episode, Ethan joins swyx and Vibhu to unpack what it actually takes to build **frontier image and video systems** : data, VAEs, diffusion transformers, audio-video alignment, inference speedups, and the hidden cost of storing and moving massive video datasets. From building **[NVIDIA's Cosmos world model](https://www.nvidia.com/en-us/ai/cosmos/)** to joining **xAI** as **[Grok Imagine](https://grok.com/imagine)** was being built from zero to one, **Ethan He** has been at the center of some of the most important work in video generation, multimodal models, and real-time world models.

We go deep on **Grok Imagine** , how a small xAI team shipped its **first multimodal video model in three months** , why **iteration speed** matters more than almost anything in model development, and why many of the biggest gains come from fixing tiny bugs in data and training pipelines. 

## Flipbook: The future of Videomaxxing

Video agents are almost a sure bet to be the trend in the coming year. We end with a glance at what's beyond video agents:

**[Flipbook](https://www.flipbook.page/n/43e8c7b08ab14571810fee265c331cb3)** caused a minor sensation this year when it was released, but most treat it as a fun demo. Ethan takes it very seriously -- with the speed and cost of inference coming down every year, the future of custom video JIT UI is closer than you think. We talked about why videogen models may become the front end of AI, how **generative UI could replace traditional HTML/CSS** , why world models need to be real-time, interactive, and long-horizon, and why the future of video generation may depend more on language models and agents than on diffusion alone.

* * *

**We discuss:**

  * Why **fast iteration** mattered more than meetings

  * Why **small training bugs** can drive huge model quality gains

  * Why coding models may make **compute the bottleneck** again

  * How image and video models are trained with **synthetic captions**

  * The role of **VAEs and latent space** in frontier video models

  * Why **image models** are the foundation for video models

  * The tradeoff between **temporal compression** and real-time interactivity

  * **[Flipbook](https://www.flipbook.page/), [Neural OS](https://neural-os.com/)**, and the future of generative UI

  * Why future interfaces may go from **user intent to pixels**

  * The hidden cost of training video models: **storage, egress, and GPU hours**

  * How **step distillation and consistency models** (like [OpenAI sCM](https://openai.com/index/simplifying-stabilizing-and-scaling-continuous-time-consistency-models/)) makes video inference orders of magnitude faster

  * Grok Imagine 0.9 and **large-scale audio-video generation**

  * Why **audio-video alignment** is harder than text-video alignment

  * Ethan's definition of **world models**

  * Reference-to-video, video extension, and **long-context video generation**

  * Why xAI's research communication undersells **Grok Imagine**

  * How **xAI culture** shaped the speed of development

  * AI watermarking, SynthID, and **detecting generated media**

  * Why **prompt rewriting** matters for video models

  * Grok Imagine Agent and the rise of **video agents**

  * Why **language models** may unlock better video generation

  * Robotics, physical AI, and **embodied world models**

  * Why **Ethan left xAI** and shifted focus toward LLMs

  * Self-managed context, memory, and **the next frontier for language models**




* * *

**Ethan He**

  * **LinkedIn:** <https://www.linkedin.com/in/ethanhe42>

  * **X:** <https://x.com/EthanHe_42>




* * *

## Timestamps

**00:00:00** Introduction

**00:01:25** From NVIDIA Cosmos to xAI

**00:03:24** Building Grok Imagine from Zero to One

**00:10:07** How Image and Video Models Are Trained

**00:18:53** Video Compression, VAEs, and Real-Time Tradeoffs

**00:22:10** Generative UI, Flipbook, and Neural OS

**00:32:10** The Cost of Training Large Video Models

**00:37:04** Distillation, GANs, and Fast Video Inference

**00:41:21** Audio-Video Generation and Grok Imagine 0.9

**00:48:34** What Makes a World Model?

**00:55:51** Reference Videos, Long Context, and Video Memory

**01:00:11** xAI Culture, Research, and First-Principles Building

**01:09:45** AI Safety, Watermarking, and Prompt Rewriting

**01:13:10** Video Agents and AI-Assisted Creation

**01:27:32** Why Language Models Unlock Better Video

**01:31:15** Robotics, Physical AI, and Embodied World Models

**01:32:38** Why Ethan Left xAI

**01:34:16** Self-Managed Context and the Future of LLMs

**01:38:43** Ethan's Career Path and Closing Thoughts

* * *

# Transcript

## Introduction: Ethan He, Latent Space, and the Path to xAI

**Swyx [00:00:00]:** We're here in the studio with Ethan He, most recently of xAI. Welcome.

**Ethan [00:00:10]:** Thank you. Glad being here.

**Swyx [00:00:11]:** We're also here with Vibhu. you were first coming to us or joining the latent space world because you were working on Kosmos at NVIDIA, and you did a paper. We loved it. you presented it as well, so thank you for doing that.

**Ethan [00:00:23]:** I've actually, I also presented the MoEs twice at latent space.

**Swyx [00:00:29]:** How did you actually hear about us? Did we reach out to you? Is that how it worked?

**Ethan [00:00:33]:** No, actually, I-- the community. Like I realized, oh, there is this online community that people talk about AI and also learn from each other through papers every week through the Paperclip. It's very nice.

**Ethan [00:00:49]:** I learned a lot.

**Swyx [00:00:49]:** I think three years stop. We haven't stopped even on Christmas and New Years. many weeks I want to stop but it keeps going.

**Vibhu [00:00:58]:** No, that was good. I think you had posted that you worked on a paper, and I was "Oh, very cool. We have Paperclip. Present then."

**Vibhu [00:01:04]:** But I might have reached out to you after.

**Swyx [00:01:05]:** you-- because it's an amateur club, right?

**Swyx [00:01:08]:** so it's very unusual and but we have sometimes paper authors come by and actually explain the paper. Today we just did, the poolside paper, which was apparently very good.

**Vibhu [00:01:18]:** Came out yesterday.

**Vibhu [00:01:19]:** pretty interesting, right? Fully open. They talk about everything, systems. So it's a good one. We'll, we'll recommend people to read it.

**Swyx [00:01:25]:** Bring us up to speed on your transition to xAI, 'cause I actually don't even know when you joined. just like tell the, tell the story about the sort of transition.

## From NVIDIA Cosmos to xAI: Scaling Video and World Models

**Ethan [00:01:34]:** Before xAI, I was working on Kosmos world model as in-- at NVIDIA. So Kosmos is, it's a giant video foundation models that can-- that aims to simulate the world and for-- it serves as a foundation of-- for all of the roboticists to build on top of. There, once I built the Kosmos one, I realized as this thing also has a scaling law similar to language model, we need to scale up the video models further. that's, that's why I realized I need to move to somewhere with much more compute resources. That's how I

**Swyx [00:02:13]:** Than NVIDIA?

**Vibhu [00:02:14]:** The GPU rich came themselves.

**Vibhu [00:02:19]:** And timeline-wise, when was Kosmo? It was pretty early, right? It was open world model, open paper, everything.

**Ethan [00:02:25]:** It was end of twenty-four.

**Vibhu [00:02:28]:** End of twenty-four.

**Ethan [00:02:30]:** Then at mid twenty-five, I moved to xAI. At that time-- I joined about the time when xAI was about to build video models and in multi-model models. There were no infra, no data, and no model, and it just-- as a few engineers, we built it in three months and released the first model, Grok Imagine zero point nine.

**Ethan [00:02:55]:** And since then, I keep working on video models and move more from training and to post-training of the video models. For example, like a reference to videos, kind of like the cameo feature and, video extensions. And, before I left, I worked on a world model, leading a small team to focus on the real-time long horizon video generation.

## Building Grok Imagine From Scratch in Three Months

**Swyx [00:03:24]:** Can you give like a rough roadmap of okay, you're on a brand-new team. Grok previously was only text, or they partnered with BFL for their image gen stuff. What do you-- what are the building blocks, right? You have compute, data you can procure somewhere. Like just what are like the sequence of things that people should think about when you're setting up a new team?

**Vibhu [00:03:43]:** actually even deeper, not just data you can procure. You guys had to go through getting the data too, right? So you shipped it pretty fast, but yeah

**Swyx [00:03:51]:** three months is like

**Vibhu [00:03:52]:** From everything

**Swyx [00:03:52]:** actually like very surprisingly fast.

**Ethan [00:03:55]:** One thing I say like thanks to my experience at NVIDIA, 'cause first time when we were building Kosmos together, we built it, for about a year. So this is like the second time I do it. Roughly have an idea, what to do. I say the most important thing is the talent. Everyone were very strong and clever, very close with each other towards a common goal. So that speed up things a lot. So you reduce the communication bandwidth among people, and everyone can work towards the same goal. It's, it's like every day there's not that much meetings on the calendar, like maybe like a, like a sync a day, and after that it's, it's just all building. It was pretty fun at that time.

**Ethan [00:04:47]:** And another thing is that xAI has very strong foundations of like data inference, model inference, and the supporting there can help the model develop a lot. When I look at, training models, I don't so actually the top important thing is like how many, how many iterations can you do, per day? and the more iteration can you do, you can, you can train the model much faster. So if you have very strong infra and you have a lot of compute, you can, you can train these models in very short period of time. That can give you a much larger buffer to, for errors, and it also gives you the opportunity to spot more bugs.

## Iteration Speed, Compute, and Debugging Model Pipelines

**Swyx [00:05:46]:** What is an iteration? Is it like a few hundred steps or what are you

**Ethan [00:05:50]:** Let's say just the train-training the model, like from acquire new data and maybe design new algorithms and train a new model, maybe at smaller scale or

**Swyx [00:06:01]:** So cycle time for like any hyperparam that you're searching.

**Ethan [00:06:04]:** Cycle time and tune to like eval this model. Is this model better than my previous iteration?

**Ethan [00:06:11]:** So

**Swyx [00:06:11]:** So it's like before you, someone had already set this up that you can iterate very quickly.

**Ethan [00:06:15]:** I think the foundation there is extremely good forDeveloping and research models.

**Ethan [00:06:23]:** And often I find is it-- this is kind of boring, but like a lot of the improvements does not come from new algorithms. It comes from finding small bugs here and there in the data pipeline, in the, in the model training pipeline. Those give, those give the biggest boost to the model quality.

**Vibhu [00:06:46]:** It's interesting, right? So you say it's like small team, less communication bandwidth, but also a lot of quality is like find little bugs. It seems counterintuitive, right? You have a lot of people, you can iron out more of those, but it's interesting to see the other side, right?

**Swyx [00:07:00]:** I also wonder, have you-- do you try using LLMs to look for bugs? I don't know.

**Ethan [00:07:05]:** I remember at that time it was mid two thousand and twenty-five, so it's the coding model wasn't quite there yet. I remem- I remember like December two thousand and twenty-five, it was extremely good. Yeah, I've been, I've been using it at that time. It's, it's helpful. sometimes it produce codes that are kind of difficult to maintain, even though like the first time it built something extremely fast. But it gave the, like a spaghetti code, thousands of lines that I couldn't maintain, and the LLM itself couldn't figure out what's, what's wrong and how to improve on top of it. But now I find it much better. Yeah, I want to bring up another point here is now coding models are much more efficient and can help us implement stuff much faster. Compute might become a bottleneck again because previously, like if you want to train a new model, say you want to generate new synthetic data and then or write a new algorithm, it might take a few weeks. And during that period of time, you don't-- you might not have experiments to run. But now you can build that thing within a few hours, then you can immediately train a model.

**Ethan [00:08:24]:** Now you have to have enough compute to try all of the ideas. So compute might be the bottleneck of iterating speed again.

**Swyx [00:08:36]:** yeah, I actually, honestly, I think it's like kind of a stressful job because you're "Well, I should be trying everything, and if I'm not, then I'm not doing my job well."

**Vibhu [00:08:48]:** there's also the stress of you're eating thousands of GPUs per hour, which is very expensive and, compute can go to other researchers.

**Swyx [00:08:56]:** You got the daddy Elon to

**Vibhu [00:08:57]:** You got daddy Elon.

**Ethan [00:08:59]:** It was

**Vibhu [00:09:00]:** But there's still finite amount of compute, like you want to use it, you want to use it well, you want more of it.

**Ethan [00:09:06]:** That was quite stressful indeed. Yeah, I think one thing is the-- with coding models now, like a lot of these jobs can be automated, which is much better. A second, it's a, it's a marathon, so you got to maintain good health and, a regular schedule.

**Vibhu [00:09:28]:** It's, it's hard to hear that when you shift from zero to nothing in two months.

**Swyx [00:09:32]:** and, I think obviously the culture at xAI is very famously, people work very hard. one thing I did want to dive into, in our-- in the notes that you, that you sent ahead of time, you had specific comments about the cost of Video Gen training. presumably this is on the Colossus-1, right? the two hundred megawatt cluster. Any whatever you want to just share on that.

**Vibhu [00:09:54]:** I think there's, there's three things we're talking about, right? So there's Video Gen, there's also the Image Gen model that you put out. Do you want to like complete the, okay, so zero to one, you have a few months. Just what are the stages of create Image Gen model?

**Swyx [00:10:06]:** Oh, yeah, maybe I got distracted.

## How Image and Video Models Are Trained: Synthetic Captions, Tokenizers, and VAEs

**Vibhu [00:10:07]:** Sorry. and then, from there's Video Gen, there's Audio Gen. Would love to get into those next. But what is that first few months like? So small team, a lot of bugs, iterations, but what does it look like? Do we take something off the shelf? Do we just get data compute? What's, what's the few months like? How do you go to state-art Image Gen model? How do you just start?

**Ethan [00:10:28]:** I cannot comment specifically how xAI did, but it's, it's a quite standard process. I can draw some, examples from Cosmos. So mainly it's building a video model, you actually need to build a image model first. And building these two models, the data you need is a hundred percent synthetic pair of language and image or language to video. Because on the, on the internet, actually, the videos don't naturally associate with text. So you can say, oh, like on YouTube, you have the title and you have the description and the comments

**Swyx [00:11:11]:** Title

**Ethan [00:11:11]:** of a video, but usually they're not relevant to the video itself. And say maybe like the video is a natural scene of mountains or something, and the title is, I'm so happy today.

**Ethan [00:11:26]:** So they have they have no correlation at all. So the first step is to, you have to generate synthetic pair of language with the videos. So you gather videos from the internet, and you use a VLM to caption the videos. So that part, here's a question, like how do you, how do you gather VLM to begin with? So if there's no

**Swyx [00:11:55]:** You, so you fuse the model, right? Like

**Ethan [00:11:57]:** Say if there's no like VLM exists, like how do you generate the text to the beginning, right? It's, it's impossible.

**Swyx [00:12:04]:** I see.

**Ethan [00:12:05]:** In the beginning, it's like you ask human to describe the video as detailed as possible.For example, you ask them to describe everything, like all objects, all characters, and all interaction and dialogues in the, in the videos. So that's in the protocol of Cosmos labeling. We require the objective we give to the labelers was that you have to describe the video as detailed as possible, such that a blind person hears a blob of text can reconstruct what the video is like from their head.

**Swyx [00:12:43]:** Video or image? You're talking about images.

**Ethan [00:12:44]:** Video or image, either one of them.

**Vibhu [00:12:47]:** This was pretty common when we went from clip and DALL-E, right?

**Vibhu [00:12:51]:** It's all training on really detailed captioning of images. So same is applied to video, but instead

**Ethan [00:12:57]:** same applied

**Vibhu [00:12:57]:** of using multimodal model to pass in video images and write rich descriptions, you can also

**Swyx [00:13:04]:** I think there's this traditional perspective of supervised, or, very highly human curated thing. I feel like there's a unlock with unsupervised, right? Where like you have enough to bootstrap that you can just throw common corpus on it or, whatever. like unsupervised vision and language pairing, right? Like where you just have, interspersed image and text and it just learns. To me, that is the VLM breakthrough that is different from the clip, different from the LM era.

**Ethan [00:13:36]:** It's interesting to see that you kind of need both data.

**Ethan [00:13:41]:** For example, for the

**Swyx [00:13:41]:** You need it to bootstrap it up. Yeah

**Ethan [00:13:43]:** for the generative model training, there's also usually like a small percentage of unlabeled data. So the model is instructed to generate a video without any text instruction. That can also help the model generalize. So after this stage of generative synthetic pair, so, one important common step is to train a compressor or a tokenizer of the image or videos. So because, if you train-- If you can technically, theoretically train image or video models on pure pixels, but the problem is that the, it's, it's a lot of tokens. So like one image, it's, a thousand by a thousand, it's like one million tokens, one million pixels. It's impossible to train transformer on that. So it's, you need to train a tokenizer, which can go from image to latent space and latent space back to image.

**Swyx [00:14:45]:** That's why we named the podcast.

**Swyx [00:14:48]:** But, basically, you're talking about vocabulary science.

**Ethan [00:14:50]:** so vocab.

**Swyx [00:14:51]:** And so, what is, what is imp-- like a million is impossible?

**Ethan [00:14:54]:** In generative models, the vocab is continuous. It's a continuous space. We can think about like you map an image to a vector. It's a, it's a fixed length vector. It's sixteen or forty-eight, something like that. And then you map that vector back to the image space. And the mapping is, has-- The mapping is patch-based. So you say you have

**Ethan [00:15:22]:** a sixteen by sixteen patch and you match, you map that patch of pixels into this latent space.

**Swyx [00:15:29]:** We've covered this

**Vibhu [00:15:30]:** This is like the vision transformers

**Swyx [00:15:32]:** VAEs,

**Ethan [00:15:33]:** VAEs.

**Vibhu [00:15:34]:** You basically compress your input, you do your generation, you're reasoning all that generation in smaller dimension, and then you project back out.

**Swyx [00:15:43]:** VAE is a form compression, but I think the for me, the patching thing is from VIT, right?

**Ethan [00:15:48]:** You can make those.

**Swyx [00:15:49]:** Literally the, yeah, the paper is titled like sixteen by sixteen is all you need. something like that. and then I think also, people make a lot of comparisons with this kind of patching with convolutions.

**Swyx [00:16:02]:** Which is you're, you're kind of re- reconstructing the old paradigm with the new.

**Ethan [00:16:05]:** Actually, in VAEs, there are, there are both convolution networks and transformers. You can actually do both.

**Ethan [00:16:14]:** After this VAE, so what you've got is you've got latent space tokens and you've got the language tokens. So now the training of the diffusion transformer, usually generative models use diffusion transformers. It is actually quite standard. It's, it's very similar to how you train a language transformer models. It's not that much difference. It's just the tokens, the visual tokens in, visual tokens out. The only difference is there's a denoising process. So you train the model to unmask some of the noise. So you add, you add random noise to the visual tokens, and then you train the model to remove those noise to generate the clean tokens. Any inference, the model can iteratively remove noise from a hundred percent noise.

**Swyx [00:17:12]:** And then there's also, to speed things along on the tech tree of diffusion, there's CFG, and then there's, there's also, latent diffusion that, there's, there's someone in there. I think, somewhere along the line, obviously, like stability and all these other guys, pioneered a lot of this, architecture. I don't know if you want to get into that or just, or do the video side up to you.

## Bootstrapping Video from Image Models and Temporal Compression

**Ethan [00:17:37]:** After you train such model, such image model, the reason it's a, it's a foundation for video models is that image models are cheaper to train, and they have much denser connection between language and text. So, sorry, language and images. For example, you train a billion, you train on a billion images, and there's a mapping from the text to the image. And the cost to train the same, like the, a billion, a billion text to a billion videos, that's much more expensive because videosNaturally have more tokens than images. Because the diffusion models, their understanding of, language purely come from this mapping. So if you don't have enough mapping, so if you only train on like a ten million videos or something, there-- you might not see enough language tokens in your training, so your model does not understand human intention enough. So that's why you really-- you train-- you first train this image diffusion models, and then you bootstrap the video model from there.

**Swyx [00:18:53]:** One thing I did want to ask, because I-- actually, I think you're, you're the first per-- video model person I've ever talked to, I think. we've, we've like talked to Luma and all those folks. There's all these tricks in video compression where basically frame by frame there's not that much difference, so actually you don't have to regenerate or save the whole frame, right? but I think MP4 compression or something else like that.

**Swyx [00:19:16]:** is it tempting to use that? Or as far as I can tell, everyone just treats it as, "No, we would just generate every frame." Is that roughly the state-art?

**Ethan [00:19:27]:** There are a few different approaches. Let's say first, like you want to just directly use MP4 compression and use that as the tokens for the transformers to train, right? So people actually have tried that, but the main challenge is the latent space for the MP4 tokens were not, were not very comprehensible for the models. It's, it's extremely hard to train on that. And there's a

**Ethan [00:20:01]:** So that's why they created VAEs, which creates more continuous, latent space, so the models can understand that latent space and learn from it much easier. Even within the VAEs, there are different difficulties of the latent space. So you can imagine something the simplest, the most naive VAE is like you have an image, and you just shuffle all of the images into a, into a vector. So you don't need to train any VAEs, right? But that latent space is extremely hard for models to train on top of. That's why there are some debate on like how do you compress the tokens. So you mentioned like you can compress frame by frame. Also, you can compress, the temporal dimension.

**Ethan [00:20:52]:** The difference is if you compress the temporal dimension, you get a much higher compression rate. Because there's temporal redundancy between frames, because, this frame and the last frame, likely they are mostly similar, so there's only some small difference. for example, I think in 12.1 VAE, they have like a eight by eight by four compression rate. So the four temporal tokens are compressed into one tokens. That can save a lot of, save a lot of the context length. If you do it frame by frame, you have to do maybe like eight by eight by one. Your context length will be four times larger. That being said, the benefit of the frame-- per frame compression, we might come back to this later, is, real-timeness and interactivity. 'Cause if you, if you strain the output of the model, frame by frame, you can-- the model can respond to any user request immediately. So if you have like a temporal four compression, four times compression, then

**Swyx [00:22:06]:** It might be laggy

**Ethan [00:22:07]:** there's a lag there in nature.

**Swyx [00:22:10]:** So you're very pilled on this. let's just go ahead and bring it up 'cause we have the visual prepared anyway. There's some frontier applications of real-time video gen. So Flipbook is one of the examples that went viral recently, right? What is Flipbook?

## Real-Time Generative UI: Flipbook, Neural OS, and Diffusion Front Ends

**Ethan [00:22:23]:** Flipbook is kind of like a web brow- web browser. You can see like it has the web bro- browser UI on top. The difference is all of the UIs are generated by generative image model in real time, and anything here are fake. But you can, you can explore inside this wor- this imaginary world. Say like we-- here we have engineering the Great Pyramid. Like the model generates this for us to understand how it works, and if we want to navigate around and understand further, we can click on some of the, some of the description here, and the model will generate a new page, new subpage describing the details we want to know about.

**Swyx [00:23:14]:** So it's basically kind of we're playing a video, but it's pausing for our next interaction, and then it just plays the next thing based on our interaction.

**Swyx [00:23:23]:** Which is kind of cool.

**Vibhu [00:23:25]:** and you kind of decide your story. So this was, how do you make a pyramid? levering technique seemed interesting, right? It shows how do you take Okay, I want to know what is this

**Swyx [00:23:35]:** The demo, the demo tweet had more animation between frames.

**Vibhu [00:23:38]:** I think it's just skipping,

**Swyx [00:23:39]:** Oh, it's just skipping a lot of frames.

**Ethan [00:23:40]:** they also have a video mode

**Vibhu [00:23:42]:** It takes a lot. There's a lot of people

**Ethan [00:23:42]:** but, a lot of people are using it.

**Ethan [00:23:45]:** So it's not available.

**Vibhu [00:23:46]:** There's a live video stream. We can try,

**Swyx [00:23:50]:** So this is an example of the kind of future that you see at the extreme. We don't-- we're obviously not in it today.

**Swyx [00:23:56]:** But in a world where inference is completely free this is better than generating code and text?

**Ethan [00:24:02]:** So this is, this is a final state of where Viva will be at for word model, I think. Imagine internet doesn't exist, and then you type in google.com. Like what should, what should, what should a model show you?the model can imagine something, and this is what the model imagine. And these web pages, they completely do not exist. So I think as the inference costs come down, we are going to have generative UI for everything. If you think about how the coding model works, so they write code for a web page, and they render the code might be con- converted into binary, and the binary render the pixels on the screen. So we in machine learning, every time we have some breakthrough, obviously it's, it's more intuit. So why don't we have like user instruction to the pixel directly? So the generative UI will be user intention to the pixels directly. And say like even if I want email, let's say everyone have the same interface, but I want, I want it slightly different. I want the email to show to me like a TikTok, so I can swipe left and right for the emails. And or maybe you want something else. We can have completely different things. Or like I have I'm looking at, Instagram stories, and I don't like the Like button. I always may click it. And, generative UI resolved it. So it's going to be a revolutionary replacement of the interface. So in the future, we might have much more powerful

**Ethan [00:25:50]:** LLMs and coding models running behind the scene. And in the, in the front-end, the diffusion model will actually be the front-end to show stuff to you. That's how I imagine it.

**Swyx [00:26:02]:** Diffusion front-end, deterministic back-end.

**Swyx [00:26:04]:** Something like that. I find that very expensive, but,

**Vibhu [00:26:08]:** I find it interesting you called LLMs writing code on the back end deterministic, but okay.

**Swyx [00:26:14]:** you write it once

**Vibhu [00:26:15]:** Compare it to

**Swyx [00:26:16]:** And then you execute.

**Ethan [00:26:17]:** If you think about the cost, say, let's say H100 costs $1 per hour, and if you use this eight hours a day and thirty days, so, every month you're paying this two forty, you'll actually not wanna pay for that. That's even more expensive than Cloud Code Max. But if you think about the compute costs come down like two times every year, and I think the future will likely arrive like within few years.

**Vibhu [00:26:49]:** It's everything, right? compute cost comes down, compute gets faster, model gets smarter

**Ethan [00:26:54]:** More efficient

**Vibhu [00:26:54]:** model gets smaller.

**Swyx [00:26:55]:** I don't know why you say two times, 'cause I think it's like 100 times. In language models, it is roughly one hundred to a thousand times every twelve to eighteen months, for the same given level of LMSys, ELO.

**Vibhu [00:27:08]:** That's a net of everything, right? That's model performance alongside compute. So different than just compute costs come down. But, a very interesting future.

**Swyx [00:27:19]:** So the web designers will have to shout out that accessibility is an issue, right? how do you deal with screen readers or whatever. But yes, this is higher bandwidth storytelling than anything you can possibly generate with code, right? So I think that's the rough idea.

**Ethan [00:27:34]:** And I'd like to add a little bit that so human naturally have the maximum bandwidth when we are looking at things, look at videos, and we also have maximum output bandwidth when we are talking. So in the future, it might be something like we talk to AI models, and the AI model responds back with a generative UI. So that would be the maximum input and output bandwidth to interact with AI models before neural link happens.

**Vibhu [00:28:06]:** And it's also very custom, right? Some people are very visual, some people are not as visual, right? They prefer the text. But the best thing about generative UI, right, it can also be text.

**Swyx [00:28:17]:** There's another project that we wanted to highlight, which is the Neural OS. Kinda similar idea, but here you're literally operating, simulating an operating system with a video model.

**Swyx [00:28:27]:** and you can play Doom, you can do Firefox. I find this like mildly less impressive, obviously, because it's an OS that I can run.

**Swyx [00:28:37]:** But here everything is imagined.

**Vibhu [00:28:40]:** I was, used to the Command+W to close the Firefox tab. It didn't crash. That's why I said

**Swyx [00:28:45]:** It's too immersive.

**Vibhu [00:28:46]:** It's, it's too immersive for me.

**Swyx [00:28:47]:** Too immersive.

**Vibhu [00:28:48]:** I wanted to close the tab.

**Vibhu [00:28:49]:** But yes, I can play generated diffusion.

**Swyx [00:28:51]:** this is shockingly fast.

**Swyx [00:28:54]:** Because I remember there was a demo about like maybe one to two years ago. Someone tried to do the first-person shooter with a image model. There was no consistency. It was very slow. But here it looks like realistically it's-- this is Doom.

**Vibhu [00:29:07]:** I think there's two sides to that, right? There's okay, what is running a game? The heavy part of it is actually the game engine, all the lighting, all that stuff, the graphics. This is just kind of video, right? Like we've solved consistency. This is still, it looks like a few years old image generation. There's some temporal consistency, but it's, it's kind of just images stitched together as frame video. But it's a good visual representation to pi- to picture the future you wanna see, right? that's, that's what I see in these more so.

**Ethan [00:29:38]:** This reminds me of how the video models gets better and better. So Neural OS is kinda if you just look at it feels like it's just a crappy version of the, like the Windows we could have, right? And, but the difference is, so the model, this model is overfitted on the existing operating systems. It can generate nothing different than that. But it's actually also similar to video models. So when we are training these video model, image model, we train them on internet. There's no imaginary supernatural stuff on the internet. But once we train this model, you can prompt the model to generate something supernatural that have never existed in the data set. So if you train your Neural OS or neural computer on the standard screen recordings on the entire internet. The model can imagine completely new interface to interact with the computer.

**Swyx [00:30:43]:** This is one of those things that is magical to me. usually generalizing out of distribution is bad, but somehow we have learned some kind of internal world model that you say, this plus, but it looks like rainbows and butterflies, it'll do it and it will kind of make sense.

**Swyx [00:31:03]:** So yeah, that's kind of cool. Yeah, I don't know if there's any comment more on there. I do, I do wanted to, I did wanted to touch a little bit more on the model architecture stuff, which I think you were getting. It's, really fascinating. We don't get a chance to talk about this enough. So one of the papers that we covered, we've covered every annual, segment anything release. and I don't know if you follow-- you're a computer vision guy, so you

**Ethan [00:31:26]:** I know

**Swyx [00:31:27]:** . So they did memory attention, which is kind of interesting. And I always think, anything where you can, across the temporal dimension, keep some consistency, I think it's, very fascinating, and I don't know if Basically, does that-- the CV side bleeding into video gen side, I think is underexplored, right? we talk about it for labeling, but actually you can borrow the architecture itself.

**Ethan [00:31:50]:** There's, there's also complete different approaches, right? you brought up the term world model, so we went from video model to world model. There is diffusion, but there's also other approaches that people are doing. So maybe we get into those after as well,?

**Swyx [00:32:03]:** He has a whole definition of world models and stuff. I feel like we threw a lot at you. Whatever you want to comment on.

## Why Video Models Are Expensive: Storage, I/O, and Training Scale

**Ethan [00:32:10]:** I think one thing that we should actually comment back on is okay, so we were talking about the steps to train image gen to video model. One thing we don't see as much of is okay, you brought up the delta in training data, right? So

**Ethan [00:32:24]:** you won't have as much a video model might not generalize, but what is the cost of training a large video model? So we know for LLMs roughly, okay, even like the poolside thing that came out today, right? It's a Gemma level model trained on roughly forty trillion tokens at this many H200s over this much time, right? You can see what is the exact cost of that. So how many GPU hours over how much H200 costs? So how do we do the back-end math of, same thing for video models, image models. How do you, how do you kind of break that down? I can share some back-envelope calculation. So surprisingly, video models is-- the cost is very-- is comparable to language models and obviously the largest scale is language model, maybe like a medium scale to language models. I said just storing the videos alone, it costs a lot. You can, you can maybe look up on AWS or something.

**Ethan [00:33:20]:** You really, say if you have a billion videos and let's say, let's just say like each video, like five megabyte, then you need five petabyte to just store those videos. And also remember we talk about you use a VAE to compress the videos, and you also need to store, typically you need to store those continuous feature, in-- also in your storage. That's also comparable size with the videos themselves. So just storing these videos and the features is tens of petabytes alone. And,

**Swyx [00:33:58]:** I just, I just looked up the calculation. Five petabytes on S3 Standard is one hundred K per month.

**Ethan [00:34:05]:** And

**Swyx [00:34:05]:** It's comparable

**Ethan [00:34:05]:** and you need

**Swyx [00:34:06]:** And

**Ethan [00:34:06]:** And then like tens of petabytes, two hundred K. And even more expensive is you have the ingress and egress.

**Swyx [00:34:13]:** Oh, yeah.

**Ethan [00:34:14]:** Like you-- through the internet. You have to just to download those videos, I believe it's, it's more expensive on AWS than just storing those videos.

**Swyx [00:34:25]:** Storing, yeah.

**Ethan [00:34:25]:** And each training runs, you probably need to pull them once. If you train multiple times, it's, it's even more than that. So it's like just storing the network, those costs is just, it would be a few, a few millions per month to just storing everything, not to mention the GPU cost.

**Ethan [00:34:45]:** And

**Swyx [00:34:45]:** my side tangent, the compute rental, like GPU rental is very efficient. There's one side, okay, you can be XAI and build your data center. Should we not just build our, storage compute as well? Like

**Ethan [00:34:57]:** Of course

**Swyx [00:34:57]:** cloud cost compared to just,

**Ethan [00:34:59]:** You save so much

**Swyx [00:35:00]:** store. Yeah, exactly.

**Swyx [00:35:01]:** Especially with like egress and stuff. So.

**Ethan [00:35:04]:** That's a good idea, but it also comes to-- there are some of its own challenges.

**Swyx [00:35:09]:** Of course, of course.

**Ethan [00:35:10]:** like people who build the GPU data centers, they might not expect this much, storage. And yeah, people build storage, typically they just build it somewhere with just CPUs.

**Swyx [00:35:23]:** I just looked it up. Five-- AWS only charges for egress, not ingress. Tier five for five petabytes is two hundred and thirty K.

**Ethan [00:35:32]:** Even more expensive than the storage.

**Swyx [00:35:34]:** But storing is per month, right? You check in, then you cannot check out. so it's so cool. It's okay. So there's that side.

**Ethan [00:35:41]:** So the TLDR, my backhand math

**Swyx [00:35:42]:** Data is larger than you think. Yes.

**Ethan [00:35:44]:** my backhand math of GPU hours times GPU cost is also very much, I'm missing some storage.

**Swyx [00:35:49]:** You're also-- you're basically like also more IO bound than normal training.

**Swyx [00:35:55]:** Yes. 'Cause like data loading, so caching everything, it becomes super important.

**Ethan [00:36:00]:** So in Cosmos, we did a lot of optimizations to make it not IO bound. So, speaking of the training, actually training the model, the GPU cost, if you look up like the open source model, how big these video models are, I think like LTX has nineteen B parameters. That's a dense model. And people are also exploring, MoEs, so it might be twenty B active and, like a hun- hundreds B, total. So that's, that's even-- that's similar size as medium-sized LLM models. And if you, if you look at number of tokens-Uh, we disclose that in Cosmos. It's also like tens of trillions of tokens on the visual tokens. So putting this together, the cost of, training these video models, it's actually comparable with LLMs. Not to mention, the infra is slightly different from LLM, so it might be less efficient to train these models.

## Inference Speedups: Step Distillation, Consistency Models, and GANs

**Swyx [00:37:04]:** Do you get the benefits of traditional diffusion speed-up? So for, images, there's LCM, LoRAs for, fine-tuning. There's, there's a lot of stuff that's been

**Ethan [00:37:15]:** Flow matching.

**Swyx [00:37:16]:** there's flow matching. There's a lot of stuff that's been done. there's some overlap that applies to diffusion on the inference side and stuff or?

**Ethan [00:37:23]:** so the difference-- the inference side is a completely different story.

**Ethan [00:37:28]:** I think for the training side, it might be a little bit hard to reduce that cost. And for the inference side, the biggest gain is from the distillation of these models. You can-- It's called step distillation, slightly different from knowledge distillation in LLMs. So you-- Typically, for flow matching models, you need like 100 steps or something. Like a distortion model even need even more, like 1,000 steps to generate a good image or video. A step distillation is try to learn to generate fewer step from the model itself. It's kind of like now we-- you use the full model to generate in 100 steps, and then you take a model that only generate 10 steps and let that model to learn from the perfect one.

**Ethan [00:38:25]:** why this work

**Swyx [00:38:27]:** Strong to weak seemingly.

**Ethan [00:38:28]:** It is. It's kind of

**Swyx [00:38:29]:** Distillation

**Ethan [00:38:29]:** kind of like strong to weak. the-- from the modeling perspective, the strong model, the teacher model is trying to model the image and videos of inter-internet, and that distribution is extremely complex. But the step distilled model is just trying to learn from the teacher. The teacher is a model, and the size is fixed, as the distribution is much simpler than the whole internet. That's the intuition I have why step distillation can work. So usually these models serve in productions, they only run in a few steps. In Cosmos, I believe we have, we have like four step and eight steps. If you do some simpler task, image-image translation, it can even run in fewer step, like one step in Cosmos Transfer.

**Swyx [00:39:22]:** I think this is the same intuition that guides a lot of the consistency model work. I sent you a link for, SCM. I don't know if you covered that. To me, that was actually one of, the most impressive papers I've ever seen from OpenAI.

**Swyx [00:39:34]:** That this is the unifying grand concept of consistency models. I don't know if you have any comments on this.

**Ethan [00:39:41]:** So there are, there are a few different approaches,

**Swyx [00:39:46]:** Oh, yeah. Here it is.

**Swyx [00:39:47]:** Two steps versus twenty or 100 steps, whatever. It's already done.

**Ethan [00:39:52]:** So there are, there are a few different approaches, for example, consistency model, and there are also Actually, we shouldn't forget GAN. So GAN, actually, that was, that was the OG of

**Swyx [00:40:05]:** OG

**Ethan [00:40:05]:** step distillation 'cause it trained just one step to begin with. So actually, a lot of, uh-- For example, there's a distribution matching distillation which use, which uses GAN, as one of the laws for distillation. It-- GAN just tells you, "Hey, generate an image," and then

**Ethan [00:40:31]:** it has a discriminator to tell, is this image real or not? So the model, the model just need to learn one of the distribution, not the full distribution. Because in training, the model is asked to reconstruct the ground truth image from the internet, which is extremely hard. And in-- When you're training GAN, it's a step process. It's just a, "Hey, you generate image. Does this image look as real as the image from the internet?" Which is a much simpler task. And, yeah, combining a lot of these approaches together, people typically do that, like consistency model and distribution matching and GAN, and we can get these few step models.

## Audio-Video Generation and Time Alignment

**Swyx [00:41:21]:** Then there's one step I wanted to add, which is audio and video.

**Ethan [00:41:26]:** So, Grok Imagine zero point nine, I believe it's, it's a first audio video transmodel deployed at a large scale. So

**Swyx [00:41:39]:** And that was your first model?

**Ethan [00:41:40]:** that was, Grok Imagine's first model. It's, it's audio video, joint generation. I think the hard part is, the modality alignment, 'cause before this transmodel, we have, we have text to video alignment. We have this, correspondence between text and video. Typically, most of the VLMs, they understand images and videos. Video's very rare, and they don't understand audio mostly. And if you look at the audio generation on the LLM side, you can talk to them perfectly fine, but if you ask them to sing a song or something, it typically is not very good. Also, they don't have, they don't have music either. The hard part is thatUh, actually audio has two component. It has like a discrete component, a continuous component. The discrete component is like the language.

**Ethan [00:42:44]:** So when we speak, it's just, some

**Swyx [00:42:47]:** It's an ASR issue, yeah.

**Ethan [00:42:49]:** It's, it's text token with some characteristics, I would say.

**Ethan [00:42:54]:** But music

**Swyx [00:42:56]:** I think the speech guys would disagree with this.

**Swyx [00:42:57]:** Like disfluencies and then,

**Vibhu [00:43:00]:** There's tones you can get angry.

**Ethan [00:43:01]:** Well, I say largely.

**Ethan [00:43:03]:** the mu- but the music is completely different. It's, it's very continuous, and you cannot model them like discrete tokens in language models. this is like the hard part for models is, not to mention we have to align text, video, and audio together.

**Ethan [00:43:26]:** So

**Vibhu [00:43:26]:** How?

**Ethan [00:43:28]:** So significant-- some significant challenges are like-- So first, like we talk about as the VLMs, they cannot understand most of them cannot understand audio.

**Ethan [00:43:39]:** So you have to have some way to do the synthetic data generation for audio. You have to caption the model, and that involve, that involve synthetic data and human data effort a lot. And not just surprisingly, most of the LLMs are very bad at recognizing, like the beat, tone, and the details of the of music. They can, they can give some general prediction of which song is this, but it's very hard to describe the details of the music. like we mentioned in image generation, like you have to describe image as detailed as possible so that someone blind can reconstruct that. So here is like someone

**Vibhu [00:44:32]:** Deaf

**Ethan [00:44:32]:** someone deaf can reconstruct how the music sounds like without actually listening to it. Maybe you can think of it need to have the-- or they call the script.

**Vibhu [00:44:49]:** Subtitles, yeah.

**Ethan [00:44:49]:** You gotta have all the details of the music, and the dialogue.

**Vibhu [00:44:55]:** So is the challenge there typically stuff like music and audio, or is it just Like is there a baseline? Okay, there's enough data where we can understand, narration, conversation, but there's nuances in audio that's where you hit all the data issues or is it just from stage zero, you just do it all right?

**Ethan [00:45:15]:** So one important thing is like the alignment. So the model, the model has to know like the video and audio, the, uh-- it has to have a time-based alignment, like at which time step the video and the audio token correspond to each other. But we actually don't have this kind of alignment for most of the other modalities. If you think about like text and image, text and video, they are loosely aligned. So you can, you can have a description of what's going on in the video, but you don't have to exactly, You typically don't have exact description, oh, at, time step one second like what happened?

**Vibhu [00:46:02]:** It's very

**Ethan [00:46:03]:** At time step two second what happened

**Vibhu [00:46:03]:** coarse. Yeah.

**Swyx [00:46:05]:** So what was the ideal time step? You have to oblate it, and then it's like four seconds or something.

**Ethan [00:46:09]:** So that comes down to how you design the model to, for the model to be aware of as a time, as a time modality. So the model is like a time aware. And that's something pretty unique if you think about LLMs. So if you ask LLM to complete a task, say they, uh-- you ask them and they will say, "Oh, this task will probably take twelve hours to complete," and they come back in one hour. Say "I've already spent two days on this and I've exhausted everything."

**Ethan [00:46:47]:** So the LLMs them-themselves, they don't have a sense of time there.

**Vibhu [00:46:53]:** I actually don't think that's just them not having a sense of time. I think it's somewhat based, right?

**Vibhu [00:46:58]:** Like you tell someone, "Okay, go work on this feature. Go implement this," there's a general understanding you would have of how long that would take without LLMs working at LLM speed, right? So you think back like two years ago, if I tell you to like build me like a new front end for latent space, have a search bar, have all this, you'll estimate that it'll take a few days, right?

**Vibhu [00:47:19]:** So you tell an LLM, "Go build this." It'll take me a few days. But I think it's somewhat grounded as opposed to them not having the best-- Not saying that they have a great understanding, but I think that example is like you can see where it comes from, right? You're trained on all over the text.

**Swyx [00:47:35]:** They're, they're trying to estimate what a human would say.

**Vibhu [00:47:37]:** because that's what the, that's what the data kind of represents. It's not them

**Ethan [00:47:41]:** It came from the corpus on the internet. People have a estimate of how much time.

**Vibhu [00:47:45]:** And not even just in direct like training samples, right? Just your world understanding of tokens of how long stuff takes, right? Go read a book. It'll take you a while, right?

**Vibhu [00:47:56]:** Even if you do nothing but read a book, it takes a few days. So yeah, LLM, I read it took me a few hours.

**Vibhu [00:48:01]:** It'll take me a few hours to go through this research. But this is a tangent.

**Swyx [00:48:05]:** Somewhat, yeah.

**Swyx [00:48:06]:** This is a train of thought I haven't really expressed until now is, which is basically like a full world model must also be recursive, meaning that the participant in the world model must also be aware that they have a world model. which is like this whole recursive thing down the, down the line. but yes, and that the world model can be wrong and that they need to update it and blah. Yeah. We've, argued this on the, newsletter as well, that there needs to be sort of recursive or adversarial world models.

## World Models: Real-Time, Long-Horizon, Interactive Video

**Vibhu [00:48:34]:** just, to ask, how do you define world model?

**Swyx [00:48:38]:** Oh, yeah, let's go there.

**Ethan [00:48:40]:** So

**Vibhu [00:48:40]:** So just for context, we talked about, video generation, and then there's a-- if you say there's a distinction between world models, what's your, what's your definition? How do you see the two?

**Ethan [00:48:53]:** So disclaimer, I'm not going to debate, what is world model. Yeah. there are many definitions, so I'll just talk about my definition. Since I came from the multi-model, multi-model domain, so mainly talking from video. So world model is like real-time interactive long horizon videos. So there are three parts. so we-- let's talk about them one by one. So the so interaction, so we just, we just look at Facebook and neural computer. So the interaction part of it, so you, world model can allow you to interact with them through keyboard, mouse, and maybe also voice. So these all is-- all is a modality. You can, you can interact with the model, and the model should respond reasonably. Second part is real time. So once you, once, say, you move your mouse, if, say, the world model generate a game, how fast can the game respond? So if you're like professional CS: GO players- -my say, oh, you have to respond- He's beginner within sub ten milliseconds or- Yeah even less. So that's not most of the- No, sixty FPS. Let's go. Oh, three hundred FPS. Oh, five hundred FPS. Wait. okay, yeah. I didn't do the math, but yeah, okay. Uh- Yeah, three hundred FPS, that's a three millisecond. So you have to respond- Oh, shit. Okay. Yeah

**Ethan [00:50:29]:** within a millisecond. Most of the video models cannot do that. Yeah. And, but if you, say, if you have a video model that is, say, like a digital human, the response time might be more generous. Maybe typically, for real-time voice interaction, it's like two hundred millisecond. So that's, that's much more generous. But even two hundred millisecond is pretty, it is pretty tricky, 'cause remember we mentioned

**Ethan [00:51:01]:** you have this, temporal compression coming from the VAE. So if you, if you don't compress the temporal dimension, your sequence length is going to explode. So if you want to have this real-time, real-timeness in your model, you have to do is one context problem. And the third part is long horizon, 'cause we-- if you're not going to just play with, video games just, a few seconds, most video models only a few seconds. We're going to play with minutes, hours. The model have to be able to generate long-form content.

**Ethan [00:51:42]:** So putting these three together, it's, real-time, long horizon interactive videos. I think the final state will be, for example, like a video, a video version of Playbook, where you can, you can interact with, a neural computer. You move your mouse, and you click on the generative interface, and it will reply to you through pixels- generating in real time. But getting there, it's, it's a very long way to get there. So one of the first step, at Grok Imagine, where I led a small world model team there, was to build video extension. So, video extension- it's the first step of interactivity. Yeah. It's, it's the first step. Yeah. So it's the first step- You have it here, video editing, yeah. Yeah. Yeah. So the first step is because, this unlocks long horizon videos. Typically, for most of the video generation models, you give it a prompt or an image as an initial frame. You generate video, that's it. That's just, one time, done. And some creators would try to, use the last frame as a first frame for the second video. It can-- sometimes it works, but if you do it a few times, it says the quality would decrease. And- It doesn't have that context- Yeah over the full video, so the temporal- Yeah, exactly. Yeah, 'cause you only gave it the last frame, of course, right? Yeah. Exactly. And- it's actually a pretty fun hack. if you've seen like- Oh, no, he's saying something better. Yeah. And for example, like Vue, I remember Vue 3 has like a second context of the last video. It is slightly better than using the last frame, but it has the same problem-- similar problem that it, the quality would decrease. if you extend a few times to, one minute, the video quality would look much worse than the first video. Second, another problem is that the model doesn't have long-range knowledge of, what's happening before. Say, if they generate some dialogue, some, two people speaking, and their voice might change, over some time, especially if the second conditioning, it does not cover the previous context. So these are the core challenges. So the Grok Imagine video extension, it has historical context of all of the previous generated videos. It can, It has, it has the context of, who is speaking and what objects have appeared and everything, having that to generate the next video. So if we naively do this, you can imagine, just, put all of the previous history video tokens into the context. The context lens will easily explode. Especially for video models, that can be like a few, a few million context, I would imagine- context lens. Yes.Yeah.

**Swyx [00:54:58]:** Let's run with that.

**Ethan [00:54:59]:** for example, like in Cosmos, I think just five seconds of video is like a fifty K or sixty K number of tokens. So like if you do, if you do fifty second, that's a five hundred K tokens. If you do longer than that, easily explode. This long horizon, problem was the first step we're trying to solve world model. It turns out people, yeah, people love video extension. Like a lot, a lot of the creators love using video extension to create longer form videos. This is the part I liked that you have a, you have an intermediate step toward the final goal instead of just a straight shot to the final version very much.

**Swyx [00:55:48]:** But I can see you have a strong vision of where we want to end up.

## Long Context, Redundancy, and Efficient Interactive Video

**Vibhu [00:55:51]:** Does it seem like it's an efficiency issue? okay, we're at a few million tokens context,. If you draw the parallel to language models, we had very short context, two thousand, eight thousand, then, you scale it up one million, ten million. sure, there's effective context, but at the end of the day, it's just what's it worth? sure, there's a whole training data side. In video, it might be slightly easier 'cause we have a hundred million token video, right? Just take a movie with the full context there. Like is this efficiency from an inference standpoint that like it's expensive, but we know how to solve it? Or like why is this not the approach? So like my broader point was on your second point of world models, you say it needs to be interactive and live, right? You should be able to play a game and see the interaction live. So one thing I see with research is a lot of what you actually serve is different than what you build, right? So we talked about distillation. You train big model, you distill it, you do quantization, speculative decoding. We do all this stuff to serve it efficiently. Should we not just have a solution, like a world model that can interact well, do inference optimization, serve it, distill it secondary, so make it real time after you solve it? So like a-- another parallel is say, continual learning, right? What we need is someone to solve it and show it works inefficiently. Give it a few years, people will make it efficient. Same thing with regular attention, right? It worked. Over a few years, people have different forms of attention, and we've scaled it to be efficient at log context,? So kind of two things there, right? One is it seems like it works. You've scaled it. Can we not just scale it a lot more efficiently over time? Do we need a separate approach if this works? And same thing with interaction, right? if we can get it done, like if we can solve some way that it works, we can solve making it more efficient from an inference standpoint later.

**Ethan [00:57:53]:** that's actually a very good point. So in videos, there's actually a lot of redundancies. So we solve a lot of the pixel redundancy from VE, but there's more redundancy in long range and long horizon videos. Say, if a character appear in the first clip and then it disappeared, it only reappear at the end of the video, you probably don't need the-- the context, like in the middle of the generation. So you only need that character, where you need. So that's why, I helped build another feature. It's a reference video.

**Vibhu [00:58:36]:** Is it here?

**Swyx [00:58:36]:** is it the same model release or different one?

**Ethan [00:58:39]:** It's a different one.

**Ethan [00:58:41]:** You probably need to search on

**Swyx [00:58:43]:** I'll find it

**Ethan [00:58:43]:** X reference to video.

**Ethan [00:58:46]:** So reference video allow you to like upload up to seven images as condition and generate the video. Say, if like I want-- it can, it can be characters or objects or even scenes. Say like I want, I want condition on, Sean's selfie and holding a blade

**Swyx [00:59:07]:** We have a dog

**Ethan [00:59:08]:** or whatever.

**Swyx [00:59:08]:** We put the dog in the thing.

**Ethan [00:59:09]:** you can put them there and the video models will generate the video from and copies the context over. So that can solve a lot of the problems there, like the long context problem. It doesn't need to have a very long context, but it's-- I feel like it's an intermediate solution. The model

**Swyx [00:59:29]:** It's cheating.

**Ethan [00:59:30]:** the model should be able to like selectively know, where should I draw the references. So say if I want to generate a movie, I generate it autoregressive, like a ten second at a time or something. And now this character appear, I can look back to where it first appear and, bring that back. Yeah, this one, I put the references. Yeah, that's, Optimus, Einstein myself, Annie.

**Vibhu [01:00:02]:** Oddly enough, I used Grok Search to find it, and it pulled your LinkedIn post. But yeah we found it.

**Ethan [01:00:08]:** Interesting.

**Vibhu [01:00:10]:** But

## xAI's Underrated Work, Culture, and Watermarking

**Swyx [01:00:11]:** this is a problem. This is not your fault, but like XAI doesn't communicate all this work that you do very well because they just have the model release and then that's it. But actually, these details are very good.

**Swyx [01:00:22]:** As far as I understand, everything you just described is state-art, like no one else has done it.

**Vibhu [01:00:30]:** A lot of-- yeah, I have a lot more

**Swyx [01:00:32]:** And then, and then you just put this blog post with the cookies. I'm this is not enough,?

**Swyx [01:00:37]:** but I, obviously this is like the high level numbers that people want to know. But no, okay, so

**Vibhu [01:00:42]:** And I wonder, like part of that is also some labs don't share research into what happens. And if

**Swyx [01:00:50]:** No, but this is literally bragging about how good they are, right?

**Swyx [01:00:54]:** Like, why would you not say that you are capable of extending with full context? this is not a secret sauce. This is like we did the work. yeah, I don't know.

**Ethan [01:01:02]:** different labs have slightly different communication styles.

**Swyx [01:01:07]:** Anyway, if anyone from XAI is listening we are always happy to help you tell your story. Yeah, okay, so you did references, and I think, I think kind of the point you're, you're making is it is sort of like a kludge, right? this is-- you can do seven, but what about 100?

**Swyx [01:01:23]:** Right? Then you need a completely different thing.

**Ethan [01:01:26]:** So I think it's-- this is, a mechanism to, select the context from the history, and you might not put the entire history into the context. for example, there's a paper called Frame Pack, which have

**Ethan [01:01:41]:** a heuristic that the latest history, the last one second, I put the entire history, and the history before that, I would, compress it and makes the video smaller. So they follow this pattern, this build overall pattern that the maximum sequence length is fixed. So the further you are from the current frame, you have a smaller image. So this is just a heuristic. I think it can be more automatic. The model is aware like which history part of it can be select. So this part of the research is actually being actively, worked on by a lot of people. It's also quite interesting. I feel this is actually, this part of long context is a little bit ahead of the LLM part.

**Ethan [01:02:31]:** So for example, like in LLMs, if you-- so contexts keep growing. Let's say if you call tool and the tool call history is extremely long, that's still in context, and keep growing, keep growing. Even if you switch the topic to something else, the whole context was there. There are some agentic harnesses that help you to, say, prune the tool results and, prune Like when you, when you query a file, only show like the top 200 lines or something. Those were very heuristic-driven.

**Swyx [01:03:08]:** For listeners, we did a write-up on the cloud code, leak where there are eight different kinds of pruning, including like you prune the tool results and all that. So you can, you can read up on that kind of thing.

**Ethan [01:03:17]:** I think, one breakthrough in continual learning might be like a way to automatically, manage its own context.

**Swyx [01:03:27]:** These are all heuristics, and they will be replaced by machine learning.

**Ethan [01:03:30]:** Interestingly

**Vibhu [01:03:32]:** The

**Ethan [01:03:32]:** the same thing is being researched in both LLMs and video models.

**Vibhu [01:03:36]:** The interesting thing is also like in the paper you showed, it's actually happening at the model level, right? Compared to like language models, sure, we have base attention, but we'll do our own compression, we'll do our own pruning, which is separate from model error.

**Vibhu [01:03:49]:** Eventually, it all just boils in, hopefully.

**Swyx [01:03:52]:** I think this is a form of like attention, but like also know sort of reasoning attention. I feel like that's different than normal attention.

**Swyx [01:04:03]:** Does that, does that make sense?

**Ethan [01:04:04]:** It's, it's different in the sense that attention, not to mention, set sparse attention aside, like normal attention

**Swyx [01:04:13]:** Like UKV, yeah

**Ethan [01:04:14]:** you have to attend to all of the tokens.

**Ethan [01:04:17]:** So you don't have a high-level mechanism to drop which tokens do-- you don't want to attend to. As humans' attention span is surprisingly small.

**Ethan [01:04:28]:** You can only remember 11 digit of a phone number.

**Swyx [01:04:32]:** But I have feature detection, right? I can detect, oh, that's a sequence of one, two, three, four in a phone number that is 11 digit.

**Vibhu [01:04:39]:** Very good pattern matchers.

**Ethan [01:04:41]:** But humans' context can-- like attention can work because we can dynamically pull in, context from different places. The same mechanism, I think is going to happen for LLMs and video models. I think we have

**Swyx [01:04:57]:** RLMs is recent-- is on, it's on the recent work is there, which is not that, crazy, but it's just recursive.

**Vibhu [01:05:04]:** I think it's somewhat inherent in models too, right? Like you

**Swyx [01:05:06]:** No, here's a nice example here

**Vibhu [01:05:07]:** you pull up these, you can read it fine, but, language models are also very good at slop parsing. you have a trans

**Swyx [01:05:15]:** I throw my typos in there, it doesn't matter.

**Vibhu [01:05:17]:** You have a, you have a transcript, you have whatever, just throw it in and it's very good at parsing through noise. m-- that may be a brute force. It can look over a reason over it, but there's, there's parallels to both.

**Swyx [01:05:31]:** I think it's just really fascinating how you relate the world models stuff to the video generation, which I don't think a lot of people hear directly, from people like you. So I think that's really helpful. Any other work? Do we cover like video, audio, world models, any other stuff in that omni

**Swyx [01:05:48]:** team,?

**Vibhu [01:05:49]:** Or any other work at XAI you want to talk about? Seems like everything we see publicly announced, "Oh, cool, cookies." And then there's so much more to it.

**Swyx [01:05:58]:** There's a lot of depth.

**Vibhu [01:05:59]:** Any underrated stuff, just at the time there?

**Ethan [01:06:03]:** I feel the, as a culture, it is quite interesting and a bit underrated. So the culture is, the culture is three sentences: move fast, build No goal is too ambitious, and the first principle. Like early, the goal set was very ambitious. It wasn't very-- this wasn't-- it wasn't possible to achieve when I, when I was thinking, first thinking about it. Like for example, like build something in three months. And

**Vibhu [01:06:36]:** Was that "Okay, we're starting team, we want image, we want video. Do it by this deadline." Or, how do you work back? Like was it just, "Okay, we have a rough by, this date we want something out," or is this like

**Ethan [01:06:52]:** That's a very good point. So it's from first principle thinking.

**Ethan [01:06:56]:** If you think about, people might say that first principle thinking applied more to the physical world than the models. I would say, for example, like if you think about-Some limitation, for example, acquiring data, like how fast can we acquire the videos? And if you think about training the models, what's the iteration speed for training a model end? And how would adding more GPUs accelerate that timeline? And maybe if you need human data, like what's the turnaround time for human data to arrive? If you put all of those together, that is first principle thinking where, oh, like what is the timeline? What's the minimum number of days that is possible to achieve something?

**Swyx [01:07:52]:** I think there's a-- this is a lot of Elon's type of thinking, right? He's like-- I think he's famous for saying that the only law you can't break is the laws of physics, something like that.

**Swyx [01:08:01]:** Just broadly, you worked a lot with Elon.

**Ethan [01:08:04]:** I, one benefit is working at xAI, you got a chance to interact more with Elon. So I was very fortunate to get a few retweets from him, and that was quite fun. And, he also worked very closely, with people. like people imagine online, like he's very hands-on.

**Vibhu [01:08:34]:** There are two things. one-- So I was actually looking up, Elon retweeting you. I'll pull it up. he talked about you tweeting that you have a really good voice mode. I don't know

**Ethan [01:08:47]:** Oh, me?

**Vibhu [01:08:47]:** No. Him.

**Swyx [01:08:48]:** Oh, I also did it. But anyway.

**Vibhu [01:08:49]:** I actually-- So I would DM you feedback on voice mode because I was "Wow, really good." And then I'm "Ugh, this sucks." But, I don't know. Anything you want to talk about your voice mode, building it? Was it a team you worked on as well?

**Ethan [01:09:02]:** Oh, that's actually not part of the team I worked on.

**Swyx [01:09:05]:** He probably worked on more of the video. No, but Grok Voice actually

**Vibhu [01:09:11]:** Grok Voice

**Swyx [01:09:11]:** like very good. I-- This is one of those things where first of all, you can speak at 2X, which is fun.

**Swyx [01:09:16]:** which I listen to 2X, so I like to speak at 2X. But also I think like the interruption was better than Gemini. I don't know how it compares to ChatGPT real time now, but as far as like driving was concerned, like having Grok in my Tesla and like driving, I think it was like-- it's a really good experience.

**Vibhu [01:09:34]:** He likes voice mode. But also, just the crazy reach by Elon

**Swyx [01:09:40]:** Fifty million views for just saying, "Yes, true."

**Vibhu [01:09:43]:** That's true.

**Swyx [01:09:44]:** Oh my God

**Vibhu [01:09:45]:** but, it's, it's pretty cool how fast it came out. the other thing is the safety aspect of video mode. Anything interesting to talk about there? So

**Swyx [01:09:56]:** spicy

**Vibhu [01:09:57]:** spicy question.

**Ethan [01:09:58]:** A lot of the countries where they don't allow like a generative data-- generative AI videos without watermarks. So in all of the-- those countries, Grok Imagine had watermarks, and a lot of the-- a lot of the takedowns of the videos were also happening extremely fast.

**Swyx [01:10:22]:** it's, it's part of running a social platform but also it transfers nicely to the GenAI side. Do you have a perspective on SynthID versus other kinds of watermarking?

**Ethan [01:10:33]:** it's going to be

**Ethan [01:10:37]:** it's going to be harder and harder to detect, the Yeah, these things. So SynthID, one thing is, previously it was only Google, and now, like a lot of different labs

**Swyx [01:10:52]:** OpenAI adopted it

**Ethan [01:10:52]:** are also adapting it.

**Ethan [01:10:54]:** As-- A limitation is like the technology The paper was out there, and people can reverse engineer like how to get rid of it.

**Ethan [01:11:05]:** And it's-- I think even as it advance, it's, it's still possible to reverse engineer it.

**Swyx [01:11:13]:** so if you are interested, you can go onto Reddit and people have taken out the exact I don't know, what do you call it? Mask or pattern that Google applies, and then you can apply it onto any Google-generated photo, and you can reverse out the SynthID.

**Ethan [01:11:30]:** And it's, it's also harder and harder to just judge by eyes. I remember like a couple years ago, there was like six fingers or something. It's very obvious.

**Vibhu [01:11:42]:** My current is actually the audio. I feel like the audio is really lacking. my way to tell if something is generated, outside of okay, I think I've seen enough, I have a decent eye, the audio matchup, especially of Sora, is not great. It's all similar style. But there's

**Swyx [01:11:57]:** I see. those are minor imperfections.

**Swyx [01:11:59]:** I think the point is that like-- Actually, my closest reference to this is also Ian Goodfellow, 'cause I think he did like the adversarial GAN thing where like it's okay, here's a picture of a zebra. Then you like change one pixel, and it becomes a panda.

**Swyx [01:12:12]:** Right? This is like-- this is like a classic computer vision issue.

**Ethan [01:12:15]:** If you think about how these models were trained, like I, like I mentioned before, like GAN was in the training process. The objective of GAN is you-- is the model generates an image, and the model, there's a judge to tell like if the image is real or not. The model is trained to make the image more real. So as the model become more and more advanced, it's going to be harder and harder. For me personally, now I have to judge by

**Ethan [01:12:49]:** if the-- these videos have logical sense.

**Ethan [01:12:53]:** If these, this video

**Swyx [01:12:55]:** Have a world model.

**Swyx [01:12:57]:** No, I also like it-- the audio is too nice, like too studio quality. The lighting is too good. The skin is too clear. the-- basically, the lack of imperfections.

**Vibhu [01:13:10]:** Do we have a good way to do reasoning in diffusion? Like is that what separates video generators from world models or in, -We really know how to apply it to other regressive language models. Is there a parallel for diffusion video gen world models like on that point, right? Is

**Swyx [01:13:30]:** He has a thing on video agents.

**Ethan [01:13:31]:** that's a good question. Yeah, actually, I have a, I have a pretty big claim. The intelli- the visual intelligence are actually mostly coming from language. these video models, especially from now, since the diffusion model technology is more mature, the every time you see there is some improvement on these models, I would say mostly, this, again, comes from language model, not coming from the vid- the video model itself, like the video distribution models themselves. In Cosmos, that could be Typically these models, they have two parts. there's a, there's a prompt rewriter or the prompt up sampler part. I think in Cosmos, we use Llama or we use Mix- Mixtro. And the Cosmos video model itself is only 7B, and the model, the language model

## Prompt Rewriting, Video Agents, and Agentic Generation

**Ethan [01:14:35]:** is a prompt rewriter. It's, it's bigger than that. So the prompt rewriter's task is to take user instruction and convert it to extremely detailed description of the video. So because the video, the visual-- the video distribution models, I would describe, they're kinda dumb because they take the input

**Ethan [01:15:03]:** instruction literally. Because in the training process, remember that we have to describe the video as detailed as possible when we're creating the synthetic, text pair. So this model, they take those kind of instruction to generate the videos. So in-- when you're taking the user instructions, the user instruction usually are simple. Just say a cat or something. If you put a cat in the video model, they would take that instruction literally. They would literally show a cat, a cat in maybe a white background because you didn't describe the background. The cat is not moving because you didn't describe it. It takes the instruction quite literally. It's kinda, it's kinda dumb. The prompt rewriter is actually a much bigger model. It's a language model that takes, the user instruction and expand it. So the thinking process you mentioned, is from there. So if you, if you look at like GPT image, like you generate a image in three minutes. Three minute is not all like a pixel generation. A lot of time is spending

**Vibhu [01:16:19]:** Prompt writing

**Ethan [01:16:19]:** on thinking.

**Ethan [01:16:20]:** So prompt rewriting now have evolved to, not only just as thinking, it can, it can also be a agent, a agentic model. For example, say you want, you wanted to generate the image of today's news. So the-- So it's likely they'll go to fetch today's news online and then, process and digest them, then organize the layout and generate it. Another thing quite interesting is,

**Vibhu [01:16:53]:** If I'm not mistaken, these are-- it's no longer a diffusion model though, right? It's autoregressively Or is there still

**Ethan [01:17:02]:** There are different approaches. For example, Gemini Omni. Since they said it's Omni, I believe it's a, it's a single model. Maybe it's something it's a language model with a diffusion head or something. Like the language model do the thinking, do the agentic tool calling, and then it would, use the diffusion head to generate the image in the end. There were also approaches like Cosmos, where you have a separate language model and separate diffusion models. And there were also like a purely language model, like you discretize the images, and then you generate the image as discrete tokens. So there are different approaches. I would say like

**Vibhu [01:17:44]:** One of, one of the claims I've seen for why these approaches struggle is because a lot of the benefits for how we currently learn reasoning with language models is you basically iteratively generate reason. You have your thought, and then you work on that answer, right? So if you have like Omni model and then diffusion head, you can't feed that back in to continue reasoning, right? So you can't go like text, image, text, image. You can't reason on the output and then go back to diffusion. But in the new Gemini Omni, you would be able to, as long as you have diffusion.

**Ethan [01:18:15]:** I'm not sure if

**Vibhu [01:18:16]:** But

**Ethan [01:18:16]:** they have that process. it's definitely possible in the Omni paradigm.

**Ethan [01:18:22]:** So if you think about like traditional multi-model language model, they would have a VIT encoder that can encode the image. So if they have a diffusion head, they can generate the image and then put that back into the VIT encoder, encode that, and then do the iterative refinement if the result Yeah.

**Swyx [01:18:44]:** I think you have to jointly train the VIT and the diffusion to make that somewhat reasonable, 'cause otherwise you're kind of mismatching or feeding in slop.

**Vibhu [01:18:55]:** I think it depends on the stage of training. You might be able to freeze it. But anyway, also just on your earlier

**Swyx [01:19:00]:** Wait. I wanted to also make explicit. We do know that NanoBanana and GPT image are autoregressive, language model with diffusion head.

**Swyx [01:19:09]:** as far as I can tell from your description of Grok image, it is not. It is, it is end.

**Ethan [01:19:14]:** I cannot

**Swyx [01:19:15]:** You cannot

**Ethan [01:19:15]:** comment on that.

**Swyx [01:19:16]:** Well, the way that you described it. but, yeah, I think it-- there's, there's different approaches, right? Like you started off saying prompt rewriter is, the-- a big part of the intelligence.

**Vibhu [01:19:24]:** and even on that, I think everyone should try using an early diffusion model. If you've used Stable Diffusion one or whatever, if you've seen the prompts ultra-high res, four K this style, oh my God, the first time I tried one, you don't talk to them like language models, right? Your prompting is very, comma separated

**Swyx [01:19:43]:** It's literally talking in the labels that were in the data set, right?

**Swyx [01:19:46]:** But basically, I'm just trying to make the point that prompt writer and then image is different from autoregressive language model with diffusion hit. Right? They're different things.

**Ethan [01:19:56]:** they're different.

**Swyx [01:19:57]:** Just wanted to establish.

**Ethan [01:19:59]:** I'd say, the common part is, the image part. So it's, it's quite surprising that, a lot of the improvement came from the

**Swyx [01:20:12]:** Language side

**Ethan [01:20:12]:** the thinking the tool calling. So I still remember, in Cosmos, I generated a happy sheep and can if without any rewriting, it's-- it looks so, CGI, and after rewrite it looks, it looks so beautiful.

**Ethan [01:20:31]:** I think

**Swyx [01:20:32]:** Without any joint training.

**Ethan [01:20:34]:** actually, without any joint training. it's-- with rewriting, it's already much better. See, a very interesting thing, what happened is the video agents, mostly language models, will call these, generative model, either it's a separate model or a diffusion head or whatever, as tool. So this model can iteratively refine the results or even, generate longer content through a very long train of thought. It's actually very similar to how human create art. So we don't, we don't generate the pixels directly. We literally draw something on And I think through this process, the-- these models not only use diffusion as one of the tool, it can also use traditional tool. It can also use, image editing tools from Photoshop. It can use, video editor, FFmpeg, whatever, to take combination of these and the generative AI technology as a, as a set of tool, and they can, they can iteratively create a better, a much better, video for production-grade quality. If you look at existing, professional creators, they don't, they don't end at, generating a video from these models. They would take this video to their editor and edit here and there.

**Swyx [01:22:11]:** So much post-production in And sometimes actually, the reason the video is good is not really the video model, it's actually the editing.

**Swyx [01:22:21]:** And yes, we also are engaged in the same process as well. Would you love to use a video editing model?

**Ethan [01:22:27]:** Actually, there's, Grok Imagine Agent beta. That was the, that was the first attempt in that direction.

**Ethan [01:22:38]:** So I think, the process would be similar to like

**Vibhu [01:22:44]:** It's just agent mode.

**Ethan [01:22:46]:** you can, you can ask it to

**Swyx [01:22:48]:** There's no blog post for it

**Ethan [01:22:49]:** maybe generate a minute, video, which is not possible if you ask the same prompt to video models. But this model will ca- literally call different tools to do that.

**Ethan [01:23:05]:** So yeah, this is actually an interesting thing. So when we first released, a video editing model, I see on X some people try the video editing feature with, "Edit this video to be one minute." 'cause they didn't understand how video editing work. Video editing typically is just a removal, add, replace, style transfer, this kind of thing. But that's actually a valid request under the assumption of video agents. So these agents should be able to understand these kind of, long horizon tasks to be able to easily, create a long-form video. I think this is, this is really fascinating 'cause it's kinda take-- it's taking the same direction as first you have these, assisted-- assisted coding, kind of like tab completion, GitHub Copilot. And from there, you gradually evolve to Codex and Cloud Code, where you do things fully automated. So in agent, in Grok Imagine Agent mode, you can, you can still go in there and do stuff by yourself.

**Ethan [01:24:22]:** gradually, as the model capability increase, it will be able to do everything fully automated.

**Swyx [01:24:30]:** I like that. okay.

**Ethan [01:24:32]:** That's good.

**Swyx [01:24:32]:** So it looks like it's still generating.

**Vibhu [01:24:34]:** Also, I did notice the Grok image gen was always very fast. I don't know if this is something you guys benchmarked, but, this is just a tangent. Compared to what I used to use before the latest OpenAI's image gen, and same with Gemini Nano Banana, I would oftentimes use Grok just for the speed.

**Swyx [01:24:54]:** It's, it's in the benchmark somewhere that's

**Vibhu [01:24:56]:** It's

**Swyx [01:24:56]:** in the Imagine API blog post that they have all the speed things.

**Swyx [01:25:00]:** it mostly combination of distillation plus inference.

**Ethan [01:25:04]:** There are a bunch of things. we talk about distillation, and if you talk about thinking, if you don't have any thinking budget, the model can just think three minutes and then come back to you. And also, inferenceThe inference infra team was very talented, and they were, they were able to accelerate a hell lot of these models.

**Swyx [01:25:27]:** my comment on the, on the video agents things, I'm trying to figure out, when people say video agents, when you initially told me about your bet on video agents or your vision for video agents, I was a little bit disappointed. I was "you mean, like models are tapped out, now we have to do agents?" But, I think you have to, right? The question now is, how much model training is it really going to make a difference versus just building a better harness? Like you said the models don't have to be jointly trained. you can just take an shelf frontier reasoning model, slap it on a harness, give it Grok as a tool. That's it. That's your video agent. Doesn't seem super satisfying. Obviously, you can train and get some more percentage points of per- performance. But, if your central claim that the majority of video or generative media, alpha or whatever, is actually coming from language intelligence and not, image diffusion or video diffusion, then that is the future.

**Vibhu [01:26:30]:** it's pretty cool

**Swyx [01:26:31]:** It's just like primarily just weight.

**Vibhu [01:26:33]:** If you pop back at the example, it generated frames. Sorry to interrupt, it's been saying "Okay, I'm gonna start stitching these frames together."

**Swyx [01:26:42]:** So

**Vibhu [01:26:42]:** It's using FFmpeg like using code.

**Swyx [01:26:43]:** This is what GPT Image Pro as well is doing, right?

**Swyx [01:26:46]:** Like, this is also just writing code in the background and then just

**Vibhu [01:26:48]:** Stitching

**Swyx [01:26:49]:** doing an image pass on the final output. It feels dissatisfying for the people who want to just train models.

**Vibhu [01:26:54]:** It's interesting, right? it's, it's also somewhat exciting. Like you brought up earlier, a lot of the gains don't come as much from the video. I think you can see that in the language model space too, right? Anthropic, very good at coding. They're multimodal, not the best, right? They have basic input PDF, but there's clearly a disconnect in the quality of their image video processing, audio processing, yet intelligence very top tier. Other labs, Gemini, OpenAI, xAI, you can add modalities, but it's not like they're unlocking crazy capabilities, right? So it's interesting.

**Ethan [01:27:32]:** It's interesting to see that, like the video model's capability increase actually come from language model being more intelligent. I think video agent, like it can unlock more stuff than my- you might imagine. So there's a few things. So one thing is when we are prompting these models, so most of the people were actually not very good at prompting.

**Ethan [01:27:59]:** Actually, language models have a better sense of how to prompt AI models. AI models know AI models better. So if you jointly train these models, maybe the model have a better sense of, how to prompt each model. Like a different model

**Vibhu [01:28:15]:** Of course

**Ethan [01:28:15]:** might be different. Another thing is it might not as simple as just, like generate a few clips and slap them together using FFmpeg. Like you might-- there might be more like image and video editing tool appear in this process. Say, if you want to exactly add a blob of text at this timestamp, the videos model-- video models might not get that intention very precisely.

**Ethan [01:28:48]:** But these are possible using these deterministic tools. The long-- The video agents can use all sorts of tools, so you don't have to put all of the capabilities into the generation model itself.

**Swyx [01:29:04]:** I think that's very true. no, so for what it's worth, I think you're right. I think that this will be a big category. I think probably you are predicting like the next one year in video is gonna be all this.

**Vibhu [01:29:18]:** Do you have a time prediction for how-- when this stuff ramps up? Like

**Swyx [01:29:22]:** they already started.

**Vibhu [01:29:23]:** Is,

**Swyx [01:29:24]:** It's not very good yet.

**Vibhu [01:29:25]:** Are we so-- No, it's so, it's so good. I think the last one's just longer.

**Vibhu [01:29:29]:** it didn't give me a minute.

**Ethan [01:29:30]:** Last thirty-six.

**Vibhu [01:29:30]:** It gave me thirty-six seconds. But are we feeling it now? Is there gonna be inflection? Is there any timeline predictions you wanna make?

**Ethan [01:29:37]:** by the end of this year is-- this is going to

**Ethan [01:29:41]:** be a big hit. So the inflection point will be where, the videos generated by video agents can get to like production grade quality, so it can be presented and it can be, it can be distributed in ads. And when-- once that happen, I think the enterprise will have much more budget for video models because the agents are, inherently more expensive than the, than the video models themselves, 'cause they do this iterative process. They generate many variations.

**Ethan [01:30:23]:** but once these models have this, pass this usability threshold, I think it's, it's going to be a exponential growth beyond that.

**Swyx [01:30:35]:** I would, fund a company right now based on this thing.

## Robotics, Physical AI, and Internet-Trained World Models

**Swyx [01:30:40]:** so I think you're right. One thing I'm, I'm surprising, I'm reflecting on the whole like past hour or so of conversation, you are-- I think you're into world models and video generation for video generation's sake. I think that a lot of other world models people, we've interviewed a lot of them, general intuition and Fei Li and all those guys and Moondream, which I think I told you about. Moonlake.

**Vibhu [01:31:01]:** Lake.

**Swyx [01:31:01]:** I keep saying Moondream. Goddammit. Moonlake. A lot of them actually say like robotics is the end game. Like embodied robotics, like you want real-time, you want interactive. It is to interact with the physical world. You're not that concerned about it.

**Ethan [01:31:15]:** I think robotics will be a, will be a big part of it for sure.the process may happen naturally. So my prediction on robotics is that the problem is physical AI might be solved, like without actually need to

**Swyx [01:31:36]:** Be in the real world

**Ethan [01:31:37]:** need to be in the real world. So it might, it might get solved by a video-- A LLM is very strong video capability. So remember we talk about the real-time interactive long horizon video. Once these models-- So now these models are just training on like screen recordings and computer screens. Once these models can use computers and understand the future state of computer extremely well, the robots might be, might be one of the, one of the tools, a very powerful AI can use. So the powerful AI might just, be able to control the physical embodiment naturally.

## Why Ethan Left xAI and What Comes Next

**Swyx [01:32:28]:** I see that for sure. Cool. I know, I know we are coming up on time. you had-- you left one more spicy topic, which is why you left xAI.

**Ethan [01:32:38]:** For me, there's, there's a lot of, a lot of research you want to do that you cannot do at, as a company. And also like the priorities and objective the-- of a company typically can change very fast. It is-- It's also the same for xAI. So now is kind of like the time so there is some research I want to do, especially more on language model side like I cannot do at xAI.

**Swyx [01:33:11]:** Oh, okay, yeah. So you're, you're basically leaving You're, you're-- you had this whole transition from computer vision to world models, video generation, to now you're like focusing on LLMs.

**Vibhu [01:33:22]:** But it seems a lot of you saying focusing on LLMs, you really in the past hour described how it all ties together, right? Like But I don't know. What do you mean by focusing on LLMs? Is there

**Ethan [01:33:33]:** I realize the fact that the video models, even like in the beginning, the game might come from improvement on diffusion technology, but this is a point where actually most of the game, come from the language models themselves.

**Swyx [01:33:50]:** It's a huge black pill for anyone who has like spent their career in like generative, media.

**Vibhu [01:33:56]:** it-- that's an extreme view, right? The-- You still definitely need a bit of both, right?

**Vibhu [01:34:01]:** There's just, it seems like more pressing, impactful work to do now on language model side.

**Swyx [01:34:07]:** Do you have any similar predictions? you-- so you predict the video agents, and I think you will be right. on the language side, what are you looking for in the next one year?

**Ethan [01:34:16]:** I think one thing pretty interesting I think might be happening soon is the language models will be like context-aware and manage its own context.

**Ethan [01:34:29]:** So some-- Like from the video model side, we've been suffering from the long horizon issue, like we want to generate video longer and longer, and we've been trying to solve the context length issues through various ways. One thing is just brute-forcing train longer context lengths. Another is to manage the context better. I think the same thing in language model is also going to be happening soon. So for example, like the language models, they're not aware of how long their own context length is. Once they hit like eighty percent or something, automatic context compression is getting triggered. And the model, is not aware of that when it's working. And some-- maybe it's good for the models to know, "Oh, I'm, I'm approaching like eighty percent," or something. And something also pretty interesting, like for example, in OpenClau, like you-- every time you type in something, a times-- the current local time is automatically attached to your message, so the model actually know what time is it. So this is making the model time-aware. And also like in tool calling the-- a lot of the intermediate tool call results automatically prune. So there's like context removal, context addition, and, context compaction. So all of these are from the harnesses themselves. But from our experience, the heuristic engineering also helps the models get this absorbed into the models themselves. that's something very interesting to explore.

**Vibhu [01:36:12]:** So infinite context?

**Ethan [01:36:14]:** Maybe.

**Vibhu [01:36:15]:** No, but it's, it's interesting, right? you

**Swyx [01:36:17]:** It is in the space of memory and continual learning and

**Vibhu [01:36:20]:** I don't know. It's also like in the space of agent harness use, right? You're seeing

**Swyx [01:36:25]:** No, he's saying he doesn't want to do it in a harness, right?

**Vibhu [01:36:27]:** No, but models are also being trained on uni-- using harnesses, right?

**Vibhu [01:36:32]:** So some of it is, you could say, implicitly leaking in, right? part of that post-training of language models is, okay, using it in coding harnesses, in which case, when are agents spawned? When is compaction gonna happen? it's not explicit you have this much token window, which I don't know if you want it to be, as that'll change, but it's, it's somewhat leaking in there.

**Ethan [01:36:58]:** I'm imagining, what if the model have access to the whole-- the code of the agent harness itself and being able to modify it to whatever you want. Say, if the agent harness is short enough, you can just put in the context lengths in the system prompt, and then the model will say, "When I want to spawn a future version of myself, I can modify the agent harness." For example, if I-- the agent harness can be, "Oh, when I'm reading-"A long document, I can choose to read the whole thing in chunks and, come back, smash the summary together, or I can just read the first two hundred lines and, discard the rest. And all kind of choices, if they can be made by the models themselves, it might be very interesting to see that the model can, program the model can program itself online in test time.

## Career Lessons: Moving Across ML Domains

**Swyx [01:38:02]:** so the self-modifying harness is also part of, OpenClaw and Py, but I think there's a lot more work to do there. Very cool. I think part of me is kind of curious. I think you are part of Big Lab, right? And there's this career path of a researcher at a Big Lab, which is you are-- you train models, you get more compute, you train better models, and you keep going. And somewhat, I feel like you're opting out of that. And if I were you, I would be "Oh, I think this is, a bit of a career risk." what?

**Swyx [01:38:36]:** I don't have any comment apart from, you're very strongly convicted. I think that a lot of people in your shoes would not be doing what you did.

**Ethan [01:38:43]:** Speaking of my career, if I look back, actually, there were, there were a lot of huge transitions. So ten years ago, I was, I was doing research with a ResNet authors, Xiangyu Zhang and Jian Sun. Yeah, at that time, the research were completely different. It was, mostly confirmation, like image recognition, object detection, object tracking. I was also doing neural net compression at that time. It was quite different from knowledge dissolutions these days. And at that time, I was-- I wanted to be a professor, and I applied. When I applied for a PhD, I already had a few first author papers at top conferences, so I confidently applied at the top schools. It turns out I got rejected by all of the top PhD programs. So I had to, I had to go to the industry. At that time, I was at Facebook AI Research fair, led by Yann LeCun.

**Swyx [01:39:51]:** I wanted to talk about VJPA, but it's different.

**Ethan [01:39:53]:** I know. Yeah, we can leave it for another time.

**Ethan [01:39:57]:** I switched to At that time, I switched to self-surprised learning. It was, it was quite different from what I was doing in contribution.

**Ethan [01:40:07]:** And after that is NVIDIA Cosmos. So I realized scaling up was extremely important. So at NVIDIA, I was mainly focusing on scaling. So one thing is Cosmos scaling the video distribution models to a few billion parameters. And another thing is, I was working on MoEs. The Megatron MoEs was the first, was the first framework open source to be able to train these MoEs at very large scales, hundred billions parameters to even trillions parameters efficiently at, forty percent MFU.

**Ethan [01:40:51]:** And going to switching to xAI was trying to work on even larger compute scale even further. And yeah, looking at this trajectory, I actually worked on a lot of different things. So I feel actually within ML, it's actually easier to switch than you think. a lot of people might have mindset that, "Oh, I work on, I work on computer vision. I always have to work on computer vision, and I cannot switch to language." And, but from my experience, at least at NVIDIA, I worked on both language model MoEs and also video models. It's, it's actually not the case. A lot of, a lot of the core principles how to train large models are largely the same. And yeah, for me, I feel right now the bottleneck, for video models is actually the language part the agent, which is why I want to go to work more on LLMs. One thing is it's, it's a bit of a challenge. I don't think it's a huge, jump, so.

## Closing Thoughts

**Swyx [01:42:18]:** kudos to you. I think you have a lot of, strong vision there. Yeah, I think that was mostly everything that we wanted to cover. You've been very generous with your time, and I, it's really nice that you are able to share all these things now. We don't have to go through xAI to clear everything. but also we

**Ethan [01:42:35]:** Oh,

**Swyx [01:42:35]:** I think we didn't get you in trouble.

**Ethan [01:42:37]:** It's a lot of good stuff about xAI compared to what you just see in the releases, right? You don't realize how many more levels there are to it.

**Swyx [01:42:44]:** xAI, please do more podcasts.

**Swyx [01:42:47]:** anyway.

**Swyx [01:42:48]:** but thank you for, sharing. It's been very kind. And also, I wanna hear more from you. I think you are going to embark on your next phase. You haven't announced what you're doing next, but clearly you have, more vision and more ambition on this path, and I think you're, you're basically kind of gradient descending to, whatever your final form is.

**Ethan [01:43:08]:** Thank you. Yeah. Yeah, I'll, I'll share more about my next chapter soon.

**Ethan [01:43:14]:** Thank you for having me.

**Swyx [01:43:16]:** Thanks for coming.

---

## [[AINews] Founders and Forward Deployed Engineers](https://www.latent.space/p/ainews-founders-and-forward-deployed)
*🔬 Latent Space | 2026-05-30*

Most people are still digesting the [massive Anthropic news](https://www.latent.space/p/ainews-anthropic-raises-965b-series) from yesterday. 

We're taking the opportunity to solicit [the leading AI FDE's](https://ai.engineer/cfp) in the world for AIE's new Forward Deployed Engineer track, mirroring similar pushes from both [OpenAI DeployCo](https://www.latent.space/p/ainews-thinking-machines-native-interaction) and [Anthropic DeployCo](https://www.blackstone.com/news/press/anthropic-partners-with-blackstone-hellman-friedman-and-goldman-sachs-to-launch-enterprise-ai-services-firm/):

[](https://substackcdn.com/image/fetch/$s_!SpLP!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fb92541e3-151a-4f10-8226-b86cb12eaca0_2332x1344.png)

as well as AIE's new Founders program, where we are doing our version of the Startup Battlefield, a competitive pitch contest anchored by YCombinator's Garry Tan and Howie Lu's [$10 Million dollar Hyperagent ](https://x.com/howietl/status/2057823823526014990)contest. Sign up (and [book hotel](https://www.ai.engineer/worldsfair/2026#venue)!) for details today if you are keen.

[](https://substackcdn.com/image/fetch/$s_!pbtj!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Faa6ef076-049b-4bd8-b183-4a49f1a913f8_2276x1306.png)

> AI News for 5/28/2026-5/29/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

# **AI Twitter Recap**

**Claude Opus 4.8 Rollout, Benchmark Friction, and API Ergonomics**

  * **Opus 4.8 landed into a noisy, mixed eval landscape** : multiple independent benches converged on "incremental but not dominant." [@arena](https://x.com/arena/status/2060160804767584512) pushed **200+ frontend/code tests** comparing Opus 4.8 against prior Opus variants, Gemini, and GLM; [@theo](https://x.com/theo/status/2060172445592789064) reported CursorBench shows it as **more efficient but slightly worse than 4.7 within margin of error** ; [@jerryjliu0](https://x.com/jerryjliu0/status/2060196252642648427) and [@llama_index](https://x.com/llama_index/status/2060165358569337102) found **small gains on tables/layout** but regressions on **content faithfulness/charts** in document parsing; [@scaling01](https://x.com/scaling01/status/2060335738172911766) said **no progress on ALE-Bench** and separately flagged interesting failure modes on LisanBench. On the positive side, [@jeremyphoward](https://x.com/jeremyphoward/status/2060195641847107722) found 4.8 **less over-agentic and more cooperative** than 4.7/GPT-5.5 in coding, while [@leo_linsky](https://x.com/leo_linsky/status/2060205310871326894) called it a tangible product improvement over prior Anthropic releases.

  * **Anthropic also shipped useful platform-level changes** : [@ClaudeDevs](https://x.com/ClaudeDevs/status/2060432688281251998) announced **mid-conversation system instructions without breaking prompt cache** , plus authoritative mid-conversation system-role updates, which matters for long-running agent sessions and cost control. But pricing remains a major complaint: [@jeremyphoward](https://x.com/jeremyphoward/status/2060198836963061998) argued Anthropic has done little for **API affordability** , preferring GPT-5.5 partly because subscription/API economics are easier to justify. Overall takeaway: 4.8 looks like a meaningful quality-of-life release for real use, not a clean benchmark reset.




**Agent Harnesses, Multi-Turn RL Bugs, and the Infrastructure Around Autonomy**

  * **A subtle but important RL failure mode got called out** : [@ClementDelangue](https://x.com/ClementDelangue/status/2060175330665508917) highlighted a Hugging Face deep-dive on why many **tool-using, multi-turn RL training loops are silently broken**. The core bug: decoding model output, parsing tool calls, then **re-tokenizing** the updated conversation can change tokenization, so gradients are applied to sequences the model never actually sampled. The proposed fix is a strict **" Token-In, Token-Out"** rule: never re-encode sampled tokens; keep a single token buffer across turns. [@johnschulman2](https://x.com/johnschulman2/status/2060392679528337714) reinforced the broader point that **renderers are foundational** infrastructure between messages and tokens, with failure modes spanning train/test mismatch, caching inefficiency, and prompt injection risk.

  * **Harness design is becoming its own optimization discipline** : [@omarsar0](https://x.com/omarsar0/status/2060371848010019001) surfaced work on **Effective Feedback Compute (EFC)** , claiming raw token/tool counts explain agent success poorly while EFC reaches **R ² up to 0.99**, implying harness quality matters more than gross activity. This lines up with productized tuning efforts like [@LangChain](https://x.com/LangChain/status/2060349231722852680), where **Deep Agents v0.6** makes **harness profiles** first-class to get strong performance from Qwen/Kimi/DeepSeek at **20x+ lower cost** than frontier APIs, and [@hwchase17](https://x.com/hwchase17/status/2060355016989585919) explicitly framing "different models need different prompts/tools." [@vllm_project](https://x.com/vllm_project/status/2060208480292843720) shipped **native weight syncing APIs** and improved pause/resume for async RL, and later added [fastokens](https://x.com/vllm_project/status/2060414393666679229), a **Rust BPE tokenizer** to reduce CPU tokenization bottlenecks in long-context/agentic workloads.

  * **Debate is shifting from "single vs multi-agent" to where the abstraction pays**: [@OfirPress](https://x.com/OfirPress/status/2060352260723392658) argued current multi-agent systems are mostly **speedups, not capability unlocks** ; [@scaling01](https://x.com/scaling01/status/2060363050272653625) took the opposite view, expecting swarm-style training to yield better planning and superintelligence-like behavior. Either way, the practical trend is clear: more teams are building around **agent observability, traces, and continual improvement loops** , e.g. [@Vtrivedy10](https://x.com/Vtrivedy10/status/2060406006329278970) on mining production traces for SFT/distillation and long-horizon continual learning.




**Open Models, Local AI, and the OSS Toolchain Tightening Up**

  * **Local-first and open-weight momentum continues to rise** : [@LangChain](https://x.com/LangChain/status/2060405874993115532) said **1 in 3 AI teams** ran an open-weights model in April 2026, up from **1 in 5** nine months earlier; [@EpochAIResearch](https://x.com/EpochAIResearch/status/2060451576779886942) estimated open-weight models now lag frontier proprietary models by about **four months**. On the toolchain side, [@ggerganov](https://x.com/ggerganov/status/2060394400237109567) launched **llama.app** , giving llama.cpp an official website, a unified installer, and a single `llama` entrypoint aimed at easier local deployment and third-party agent integration. [@ollama](https://x.com/ollama/status/2060428074102206496) announced **OpenJarvis** as a local-first personal AI via Ollama, explicitly tied to Stanford/Hazy's "Intelligence Per Watt" framing.

  * **Open infrastructure is getting more enterprise-shaped** : [@ClementDelangue](https://x.com/ClementDelangue/status/2060378354931388837) noted that **~50% of models and datasets on Hugging Face are now private** , rising with HF's storage/buckets offering; this is an important correction to the idea that HF is only public OSS infrastructure. [@abidlabs](https://x.com/abidlabs/status/2060404002341462044) showed **Hugging Face Jobs** replacing GitHub runners for CPU/serverless GPU CI. [@DSPyOSS](https://x.com/DSPyOSS/status/2060186371902587119), [@dbreunig](https://x.com/dbreunig/status/2060187833084870746), and others shipped a redesigned **DSPy docs/front page** ahead of a coming 4.0, focused on onboarding into programmable AI systems rather than pure prompting.

  * **Licensing and permissiveness are becoming strategic levers** : [@kimmonismus](https://x.com/kimmonismus/status/2060458698930016378) highlighted NVIDIA moving its four open model families to **Linux Foundation OpenMDW-1.1** , reducing legal fragmentation across weights/code/docs/data. New permissive data releases also matter: [@keshigeyan](https://x.com/keshigeyan/status/2060398262591668315) introduced **GPIC** , a **100M-pair permissive image corpus** plus **1M-pair benchmark** for visual generation, with explicit research + commercial usability.




**Google/OpenAI Product Surface Expands: Managed Agents, Gemini Spark/Omni, and Codex on Windows**

  * **Google is widening the "managed agent" stack from API to consumer product**: [@_philschmid](https://x.com/_philschmid/status/2060359976325992528) showed **Managed Agents in the Gemini API** : a single API call provisioning a sandboxed Linux environment with code execution, web access, and file I/O. On the consumer side, [@GeminiApp](https://x.com/GeminiApp/status/2060405496872579115) rolled out **Gemini Spark** to U.S. AI Ultra subscribers as a **24/7 personal agent** that can operate across a user's digital ecosystem under direction. Google also kept pushing **Gemini Omni** multimodal generation/editing demos ([example](https://x.com/alexanderchen/status/2060322611586834518), [product thread](https://x.com/GeminiApp/status/2060473816393150965)) and announced **Google Flow Agent** for creative workflows in video/film production ([thread](https://x.com/Google/status/2060473826362732611)).

  * **OpenAI 's Codex is moving closer to a persistent remote dev operator**: [@OpenAI](https://x.com/OpenAI/status/2060428604727771421) and [@OpenAIDevs](https://x.com/OpenAIDevs/status/2060429591655927942) added **computer use on Windows** , including remote steering from the ChatGPT mobile app. Follow-on UX improvements included **stable identicons for background agents** and search across prior chat content ([@OpenAIDevs](https://x.com/OpenAIDevs/status/2060478367921831936)); [@reach_vb](https://x.com/reach_vb/status/2060430024537178215) summarized broader Codex updates around Windows control, mobile remote access, and profile/task stats. Separately, OpenAI updated **gpt-5.5 instant** to improve **sycophancy, factuality, and multilingual performance** per [@michpokrass](https://x.com/michpokrass/status/2060219759682330970).

  * **This all points to more vertically integrated agent stacks** : model + harness + sandbox + UI + remote control + pricing/quotas. Google is smoothing quotas on Gemini ([@joshwoodward](https://x.com/joshwoodward/status/2060171610922058142)); OpenAI is expanding Codex's operating surface; Cursor added **auto-review mode** with subagent-based approval routing ([tweet](https://x.com/cursor_ai/status/2060406013098897765)). The common pattern is less "chatbot," more **managed execution environment with policy and memory**.




**Research and Systems Papers Worth Attention**

  * **Search, retrieval, and memory** : [@TheTuringPost](https://x.com/TheTuringPost/status/2060194173505155358) highlighted **Bidirectional Evolutionary Search (BES)** from Harvard/MIT, combining forward search with backward decomposition and evolutionary operators; reported gains include **Llama-3.2-3B-Instruct on MuSiQue from 4.0% to 7.0%**. In retrieval, [@_reachsumit](https://x.com/_reachsumit/status/2060214762626306512) pointed to **Latent Terms** , showing sparse BM25-ready features can be extracted from frozen dense retrievers via SAEs. [@topk_io](https://x.com/topk_io/status/2060383255153569938) open-sourced **Iso-ModernColBERT** for more efficient late-interaction inference.

  * **Continual learning and belief/state management** : [@HuggingPapers](https://x.com/HuggingPapers/status/2060312560323182657) summarized **BeliefTrack** , claiming optimized belief-state management cuts long-horizon reasoning failures by **70%+**. [@AndrewLampinen](https://x.com/AndrewLampinen/status/2060460827199599026) argued the continual learning field over-focused on interference instead of positive transfer; [@victor207755822](https://x.com/victor207755822/status/2060315686329778432) presented a second **DeliAutoResearch SKILL** paper focused on self-iteration and CL.

  * **Multimodal/world models/robotics** : NVIDIA-affiliated work included **γ -World**, a generative multi-agent world model streaming at **24 FPS** ([tweet](https://x.com/fangfu0830/status/2060233093894869499)), and **minWM** , a real-time interactive video world model framework ([tweet](https://x.com/_akhaliq/status/2060392729473860026)). In robotics, [@_akhaliq](https://x.com/_akhaliq/status/2060388349425119540) shared **Qwen-VLA** , and [@inventorOli](https://x.com/inventorOli/status/2060357909561622885) demoed Robostral's language-following and manipulation improvements. For always-on proactive agents, [@dair_ai](https://x.com/dair_ai/status/2060373102119555191) surfaced work replacing LLM wake-up decisions with a **220MiB temporal-graph encoder** , gaining **+16.7 mean F1** while running **4 -83x faster**.




**Top tweets (by engagement)**

  * **OpenAI / biology** : [@OpenAI on Rosalind Biodefense](https://x.com/OpenAI/status/2060376598642405492) announced trusted-access biology tooling for public health and biodefense.

  * **Google / consumer agents** : [@GeminiApp on Spark](https://x.com/GeminiApp/status/2060405496872579115) rolled out its always-on personal agent to AI Ultra users in the U.S.

  * **OpenAI / dev tools** : [@OpenAI on Codex Windows support](https://x.com/OpenAI/status/2060428604727771421) and [@OpenAIDevs](https://x.com/OpenAIDevs/status/2060429591655927942) expanded computer use to Windows plus mobile remote steering.

  * **llama.cpp UX milestone** : [@ggerganov](https://x.com/ggerganov/status/2060394400237109567) launched **llama.app** with a unified installer and CLI entrypoint for local AI.

  * **HF / RL correctness** : [@ClementDelangue](https://x.com/ClementDelangue/status/2060175330665508917) amplified the **Token-In, Token-Out** warning for multi-turn RL with tools.

  * **Open vs closed timing gap** : [@EpochAIResearch](https://x.com/EpochAIResearch/status/2060451576779886942) estimated open-weight models are now about **4 months behind** the frontier.




* * *

# **AI Reddit Recap**

## **/r/LocalLlama + /r/localLLM Recap**

### **1\. Local LLM Performance: MoE Releases, Quants, VRAM Savings**

  * **[StepFun 3.7 Flash](https://www.reddit.com/r/LocalLLaMA/comments/1tqloii/stepfun_37_flash/)** (Activity: 637): **StepFun released[Step 3.7 Flash](https://static.stepfun.com/blog/step-3.7-flash/), a multimodal MoE with **`196B`**total parameters,**`11B`**active, and a built-in**`1.8B`**ViT, advertised for high-throughput agent workflows up to**`400 TPS`**and reportedly runnable locally with ~**`128GB`**RAM. Reported benchmarks position it unusually strongly for a flash-class/local model: SWE-Bench Pro**`56.26%`**, DeepSearchQA F1**`92.82%`**, HLE w/tools**`47.2`**, plus large gains over Step 3.5 Flash on Terminal-Bench, Toolathlon, ClawEval, and other agentic/tool-use tasks. Direct model artifacts are available on Hugging Face in[BF16](https://huggingface.co/stepfun-ai/Step-3.7-Flash/), [FP8](https://huggingface.co/stepfun-ai/Step-3.7-Flash-FP8), [NVFP4](https://huggingface.co/stepfun-ai/Step-3.7-Flash-NVFP4), and [GGUF](https://huggingface.co/stepfun-ai/Step-3.7-Flash-GGUF), with day-0 **`llama.cpp`**[support PR](https://github.com/ggml-org/llama.cpp/pull/23845) and related MTP work in **`llama.cpp#23274`**.** Commenters characterize the model as technically odd: its hidden/thinking traces are described as nearly incoherent, but final answers can be _" perfect"_ and competitive with much larger `>1TB` models; one user says the prior Step 3.5 _" infinite thinking"_ issue appears fixed. There is cautious enthusiasm around local deployment, especially for users with `4x3090`-class hardware, and appreciation that StepFun upstreamed `llama.cpp` support instead of only maintaining a fork.

    * StepFun released multiple Step-3.7-Flash checkpoints on Hugging Face: **BF16** ([Step-3.7-Flash](https://huggingface.co/stepfun-ai/Step-3.7-Flash/)), **FP8** ([Step-3.7-Flash-FP8](https://huggingface.co/stepfun-ai/Step-3.7-Flash-FP8)), **NVFP4** ([Step-3.7-Flash-NVFP4](https://huggingface.co/stepfun-ai/Step-3.7-Flash-NVFP4)), and **GGUF** ([Step-3.7-Flash-GGUF](https://huggingface.co/stepfun-ai/Step-3.7-Flash-GGUF)). One user reports the prior Step 3.5 Flash "infinite thinking" issue appears fixed, making 3.7 more usable despite still having an odd intermediate reasoning style.

    * There is day-0 `llama.cpp` enablement via StepFun's upstream PR: [ggml-org/llama.cpp#23845](https://github.com/ggml-org/llama.cpp/pull/23845), contrasting with Step 3.5's fork-based support. A separate community PR for **MTP support** exists at [ggml-org/llama.cpp#23274](https://github.com/ggml-org/llama.cpp/pull/23274), though commenters note it needs updating for Step 3.7 and current `master`.

    * A vLLM nightly test of the **NVFP4** checkpoint on `2x Pro 6k` with `64` concurrent shallow-context requests reached about `2200 tok/s`. The reported config used `tensor-parallel-size 2`, `--enable-expert-parallel`, `--quantization modelopt`, `--kv-cache-dtype fp8`, `--reasoning-parser step3p5`, and StepFun tool-call parsing; vLLM reported **GPU KV cache size**`1,667,645`**tokens** and **max concurrency**`6.36x`**for**`262,144`**tokens/request**.




[ Read more ](https://www.latent.space/p/ainews-founders-and-forward-deployed)

---

## [[AINews] Anthropic raises $965B Series H, releases Opus 4.8 and Dynamic Workflows/ultracode](https://www.latent.space/p/ainews-anthropic-raises-965b-series)
*🔬 Latent Space | 2026-05-29*

Anthropic's path as the [fastest growing company of all time](https://www.latent.space/p/anthropic-glean-and-openrouter-how?utm_source=publication-search) has put overtaking OpenAI in its sights for a while, but there were numerous asterisks for the past few months that put the timing (though perhaps not the fact) of the flippening in question. Today Anthropic [officially reported $47B](https://www.anthropic.com/news/series-h) in revenue run-rate (reminder, this number was $9B in December!) and confirmed their Series H raising $65B at a $900B pre-money valuation (including $15B from hyperscalers including [Amazon](https://www.anthropic.com/news/anthropic-amazon-compute), but also the entire memory industrial complex), putting them at least temporarily ahead of OpenAI in every headline dimension outside of compute and non-coding benchmarks:

[](https://substackcdn.com/image/fetch/$s_!9YXV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ffeb0a3a2-e744-4174-a24b-be1fd75961bc_1888x1630.png)

By way of celebration, the company also released [Opus 4.8](https://www.anthropic.com/news/claude-opus-4-8), which broadly reportedly fixed many of the issues the community had found/soured on [Opus 4.7 post launch](https://www.latent.space/p/ainews-anthropic-claude-opus-47-literally) (see recap below for details). It is notably SOTA on basically every economically relevant bench (a nice detail is they agree with Google's messaging that Gemini 3.5 Flash is an improvement over Gemini 3.1 Pro):

[](https://substackcdn.com/image/fetch/$s_!pJaM!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F7e7c3740-ab5b-4b98-88eb-c0576e73a2d1_1490x1350.png)

But perhaps of more long term significance is the massively parallel ["dynamic workflows" feature](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code) in Claude Code, also called `ultracode`, which was behind Jarred Sumner's [750k LOC rewrite of Bun from Zig to Rust in 6 days](https://x.com/jarredsumner/status/2060050578026189172):

[](https://substackcdn.com/image/fetch/$s_!FuPa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fe9ab93f6-c75f-4156-850a-81b99806aeea_1402x1256.png)

>

> AI News for 5/27/2026-5/28/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

# **AI Twitter Recap**

**Anthropic announced a massive new financing and simultaneously shipped Claude Opus 4.8.**

  * On the capital side, Anthropic said it raised **$65B in Series H at a $965B post-money valuation** , led by Altimeter, Dragoneer, Greenoaks, and Sequoia, and said the money will fund research and expand capacity for growing Claude demand ([Anthropic](https://x.com/AnthropicAI/status/2060061347522433422)).

  * The company also disclosed that its **run-rate revenue surpassed $47B** , attributing growth to enterprise deployments and everyday usage ([Anthropic](https://x.com/AnthropicAI/status/2060061348818518493)).

  * On the product side, Anthropic launched **Claude Opus 4.8** , describing it as an Opus 4.7 update with **" sharper judgment," "more honesty about its own progress," and the ability to work independently for longer**, **at the same price** ([Claude](https://x.com/claudeai/status/2060042702150930686)).

  * Anthropic also launched **Dynamic Workflows** in Claude Code, a research-preview orchestration system where Claude plans work and spawns **hundreds of parallel subagents** to tackle large tasks ([ClaudeDevs](https://x.com/ClaudeDevs/status/2060044853279617150)). Independent eval posts broadly confirm that 4.8 is a meaningful improvement over 4.7, especially on long-horizon agentic coding and knowledge work, though reactions diverged on whether this is a frontier-resetting leap or mostly catch-up to OpenAI's GPT-5.5-family.




## **Facts vs opinions**

### **Facts and directly stated claims**

  * Anthropic raised **$65B** at a **$965B post-money valuation** in Series H ([Anthropic](https://x.com/AnthropicAI/status/2060061347522433422)).

  * The company says its **run-rate revenue crossed $47B** ([Anthropic](https://x.com/AnthropicAI/status/2060061348818518493)).

  * Lead investors named: **Altimeter, Dragoneer, Greenoaks, Sequoia** ([Anthropic](https://x.com/AnthropicAI/status/2060061347522433422)).

  * Altimeter publicly confirmed it led the round and framed it as its **largest investment to date** ([Altimeter](https://x.com/AltimeterCap/status/2060061841372647685), [Pauline Bhyang](https://x.com/paulinebhyang/status/2060069180767171052)).

  * Anthropic launched **Claude Opus 4.8** , positioned as an update to **Opus 4.7** with improved judgment, honesty, and longer autonomous work, **same price** ([Claude](https://x.com/claudeai/status/2060042702150930686)).

  * Anthropic engineers said 4.8 was a response to **feedback on 4.7** , with "many fixes" and better nuance / naturalness ([Alex Albert](https://x.com/alexalbert__/status/2060043196655362358)).

  * Claude Code now supports **Dynamic Workflows** that write orchestration plans and launch **large fleets / hundreds of subagents in parallel** ([ClaudeDevs](https://x.com/ClaudeDevs/status/2060044853279617150), [Cat Wu](https://x.com/_catwu/status/2060054180379689074)).

  * Dynamic Workflows are available in **research preview** and were said to work on **Max, Team, Enterprise, API, Bedrock, Vertex AI, and Foundry** ([ClaudeDevs](https://x.com/ClaudeDevs/status/2060044860984529368)).

  * Anthropic / community posts mention **effort controls** added to web/app/Cowork and continued **Fast mode** support ([Mikey K](https://x.com/mikeyk/status/2060046053907578889), [Sam Callister](https://x.com/sammcallister/status/2060048329359212972), [Kimmonismus](https://x.com/kimmonismus/status/2060044465385902436)).




### **Opinions / interpretations**

  * Bullish views:

    * Opus 4.8 "could've been called Opus 5" ([Dan Shipper](https://x.com/danshipper/status/2060043738752422304)).

    * "Anthropic found a cure for laziness" ([scaling01](https://x.com/scaling01/status/2060043010943942989)).

    * "first smart model in a long while" due to honesty / calibration ([zephyr_z9](https://x.com/zephyr_z9/status/2060077152729694586)).

    * "People unsubscribing from Anthropic will crawl back" ([teortaxesTex](https://x.com/teortaxesTex/status/2060105674311295454)).

  * Skeptical / mixed views:

    * Opus 4.8 is "a minor upgrade" ([scaling01](https://x.com/scaling01/status/2060041564919833041)).

    * Anthropic is "playing catch-up with OpenAI rather than setting the pace" ([kimmonismus](https://x.com/kimmonismus/status/2060085889896726860)).

    * Some benchmark-based criticism from Andon Labs: worse than Opus 4.7 / GPT-5.5 on **Vending Bench** , underperformed on **Blueprint-Bench 2** , more aligned / more cautious, and "max reasoning is not the best reasoning effort" ([andonlabs](https://x.com/andonlabs/status/2060047215134228746), [andonlabs](https://x.com/andonlabs/status/2060047225791877193)).

    * Dynamic workflows are powerful but may be **token-expensive** and quota-burning in practice ([itsclivetime](https://x.com/itsclivetime/status/2060157266591129895), [Theo](https://x.com/theo/status/2060135394570797158), [Omar Sar0](https://x.com/omarsar0/status/2060059612041171175)).




## **Fundraise details and implications**

Anthropic's financing numbers are the headline shock: **$65B raised on a $965B post-money** with **$47B run-rate revenue** disclosed in the same announcement ([Anthropic](https://x.com/AnthropicAI/status/2060061347522433422), [Anthropic](https://x.com/AnthropicAI/status/2060061348818518493)). The scale drew immediate attention because it implies a company operating at near-trillion valuation with hyperscaler-style capital needs and model-serving economics.

Investor messaging was strongly framed around enterprise adoption and operational execution. Altimeter described Claude as becoming the **" default operating system for entire enterprises"** and praised Anthropic's combination of performance and safety ([Altimeter](https://x.com/AltimeterCap/status/2060061841372647685)). Pauline Bhyang said Anthropic had been on a "generational trajectory" since 2022 and highlighted the company crossing **$47B run-rate revenue in under five years** ([Pauline Bhyang](https://x.com/paulinebhyang/status/2060069180767171052)).

The surrounding reactions broke into a few camps:

  * **Validation camp:** This funding size is treated as evidence that Claude has become a core enterprise platform, especially in coding and agentic workflows. Posts like Jamin Ball's "Let's go!!" were simple market validation reactions ([jaminball](https://x.com/jaminball/status/2060062156478107775)).

  * **Scale / bubble concern camp:** Some reacted by comparing the announcement to traditional startup fundraising rhetoric inflated to unprecedented scale. Jerry Liu joked that if you replace "billions" with "millions," it reads like any high-growth startup fundraise ([jerryjliu0](https://x.com/jerryjliu0/status/2060068247773614238)). Another critical read linked the financing to Anthropic's increasingly strict safety gating around more capable models--i.e. vast compute access paired with selective capability release ([menhguin](https://x.com/menhguin/status/2060060425031696387)).

  * **Infrastructure implication:** Anthropic explicitly tied the raise to **capacity expansion** for Claude demand ([Anthropic](https://x.com/AnthropicAI/status/2060061347522433422)). That matters because many of the new 4.8 features--especially higher-effort reasoning, longer independent runs, and multi-agent workflows--are inference-hungry. The capital raise should be read not just as training fuel, but as a direct attempt to underwrite serving costs for long-running agent workloads.




One notable context tweet: a user speculated that "Anthropic also secured tens of billions in inference compute" right as Mythos safety concerns were apparently addressed ([menhguin](https://x.com/menhguin/status/2060060425031696387)). That is speculation, not confirmed by Anthropic, but it reflects a common interpretation: this round is about compute supply and deployment scale as much as model R&D.

## **Opus 4.8: official product positioning**

Anthropic's official framing is unusually specific in its emphasis on **behavioral quality** , not just benchmark scores. The launch tweet says 4.8 has:

  * **sharper judgment**

  * **more honesty about its own progress**

  * **ability to work independently for longer**

  * **same price as 4.7** ([Claude](https://x.com/claudeai/status/2060042702150930686))




Alex Albert added that 4.8:

  * incorporates fixes based on 4.7 feedback,

  * understands nuance better,

  * feels more natural conversationally,

  * is stronger across coding and knowledge work ([Alex Albert](https://x.com/alexalbert__/status/2060043196655362358)).




This honesty / calibration angle became a major subtheme. Multiple Anthropic employees and outside testers described the model as more willing to:

  * say what it doesn't know,

  * flag flaws in its own code,

  * avoid glossing over uncertain progress,

  * stop falsely implying task completion ([Cat Wu](https://x.com/_catwu/status/2060051277476745512), [Mikey K](https://x.com/mikeyk/status/2060046051466502401), [dejavucoder](https://x.com/dejavucoder/status/2060043362858942497)).




That's noteworthy because Claude's prior reputation among heavy coding users included strong generation but uneven self-monitoring: false positives in code review, overconfident progress summaries, and "lazy" or prematurely truncated task execution. Several community reactions explicitly framed 4.8 as fixing this failure mode:

  * "found a cure for laziness" ([scaling01](https://x.com/scaling01/status/2060043010943942989))

  * "least lazy model ever?" ([Teknium](https://x.com/Teknium/status/2060072183783960971))

  * "dramatically less lazy than every other version of Claude" ([nrehiew_](https://x.com/nrehiew_/status/2060046647867191727))




## **Technical details and numbers**

### **Pricing, context, controls**

The most concrete consolidated specs came from Artificial Analysis:

  * **Context window:** **1 million tokens**

  * **Pricing:** **$5 / $25 per million input / output tokens**

  * **Cache writes:** **$6.25 / M** with **5-minute TTL**

  * **Cache hits:** **$0.50 / M**

  * **Effort settings** remain as in Opus 4.7; AA tested **max** effort ([Artificial Analysis](https://x.com/ArtificialAnlys/status/2060117582120976868))




Community posts also highlighted:

  * **Fast mode** is available for Opus 4.8

  * It is **~2.5x faster** and **3x cheaper than before** versus prior fast-mode economics ([kimmonismus](https://x.com/kimmonismus/status/2060044465385902436))

  * scaling01 summarized the new economics as:

    * **Opus 4.8 Fast: 2.5x faster, only 2x more expensive than normal 4.8**

    * versus **Opus 4.7 Fast: 2.5x faster, 6x more expensive than normal 4.7** ([scaling01](https://x.com/scaling01/status/2060051666443943962))

  * Effort controls were newly exposed in more product surfaces, allowing users to dial reasoning up or down ([sammcallister](https://x.com/sammcallister/status/2060048329359212972), [mikeyk](https://x.com/mikeyk/status/2060046053907578889), [kimmonismus](https://x.com/kimmonismus/status/2060045324803063962))




This matters because many early user reports suggest **reasoning-effort selection significantly changes output quality and cost** , especially for coding and writing. Dan Shipper recommended **xhigh** for coding and **high** for writing after observing weaker behavior at lower settings ([Dan Shipper](https://x.com/danshipper/status/2060043738752422304)). Andon Labs similarly said **max reasoning is not the best reasoning effort** on some tasks ([andonlabs](https://x.com/andonlabs/status/2060047215134228746)).

### **Benchmarks: strongest reported numbers**

Key official / semi-official numbers surfaced across launch tweets:

  * **SWE-Bench Pro: 69.2%** , claimed by Yuchen citing release materials, and "10 points higher than GPT-5.5" ([Yuchenj_UW](https://x.com/Yuchenj_UW/status/2060042830559756407))

  * **FrontierSWE #1** , cited by Anthropic watchers and later confirmed by third-party references ([scaling01](https://x.com/scaling01/status/2060046440563388838), [scaling01](https://x.com/scaling01/status/2060054319446016046))

  * **APEX-SWE: 45.3% Pass@1** , nearly **4 points ahead of GPT-5.3 Codex at 41.5%** ([mercor_ai](https://x.com/mercor_ai/status/2060046111793123428))

  * **GDPval-AA: 1890 Elo** , **+137 vs Opus 4.7** , **+121 vs GPT-5.5 xhigh** , implying about **67% win rate vs GPT-5.5 xhigh** head-to-head ([Artificial Analysis](https://x.com/ArtificialAnlys/status/2060042848268083411))

  * Artificial Analysis Intelligence Index: **61.4** , **+4.1 vs Opus 4.7** , **+1.2 ahead of GPT-5.5 xhigh** ([Artificial Analysis](https://x.com/ArtificialAnlys/status/2060117582120976868))

  * **AA-Omniscience: 27.4** , #2 behind Gemini 3.1 Pro at 32.9; **accuracy 46.6%** , **hallucination 35.9%** ([Artificial Analysis](https://x.com/ArtificialAnlys/status/2060117582120976868))

  * Gains on:

    * **Terminal-Bench Hard +6.8**

    * **τ ²-Bench Telecom +5.9**

    * **IFBench +3.6**

    * relatively flat on **AA-LCR, GPQA, SciCode** ([Artificial Analysis](https://x.com/ArtificialAnlys/status/2060117582120976868))




Additional qualitative benchmark observations:

  * Cursor said Opus 4.8 works **much more efficiently than 4.7** on **CursorBench** and is more persistent on hard tasks ([Cursor](https://x.com/cursor_ai/status/2060044920237469872))

  * Anthropic employees emphasized strength on **long-horizon work** in Claude Code ([ClaudeDevs](https://x.com/ClaudeDevs/status/2060043212425933076))

  * Some users reported especially large jumps in **knowledge work** and **writing** ([Dan Shipper](https://x.com/danshipper/status/2060043738752422304), [rishdotblog](https://x.com/rishdotblog/status/2060057903344869828))




### **Efficiency and token-use details**

Artificial Analysis reported:

  * Compared to Opus 4.7, 4.8 achieved higher GDPval performance with:

    * **15% fewer turns per task**

    * **35% fewer output tokens**

  * But 4.8 still used **~30% more turns than GPT-5.5** , the second-ranked model ([Artificial Analysis](https://x.com/ArtificialAnlys/status/2060042850826612996))




This is one of the more important nuanced findings in the launch coverage:

  * 4.8 is **more efficient than 4.7**

  * but still not obviously the **most inference-efficient frontier model** against OpenAI on some workloads




That tension is echoed in community commentary:

  * "still getting token-mogged by GPT-5.5" ([scaling01](https://x.com/scaling01/status/2060080401947746483))

  * Theo and others complained that Claude's higher-agency, higher-effort modes can blow through quota extremely quickly in practice ([Theo](https://x.com/theo/status/2060120708815139241), [cremieuxrecueil](https://x.com/cremieuxrecueil/status/2060161310302630154))




### **Long context**

Posts highlighted long-context improvements from Opus 4.6 to 4.8, with one claim that **Opus 4.8 at 1M context is almost as good as GPT-5.5 's 256K score** on a referenced long-context eval ([scaling01](https://x.com/scaling01/status/2060047431564251545)). Artificial Analysis also confirmed the **1M token** context remained intact ([Artificial Analysis](https://x.com/ArtificialAnlys/status/2060117582120976868)).

### **Safety / robustness / hallucination**

This was one of the more mixed parts of the release.

Positive:

  * Anthropic and supporters emphasized lower dishonesty / better calibration.

  * "dishonesty at an all time low" ([scaling01](https://x.com/scaling01/status/2060042892903678414))

  * "noticeably more honest" ([Cat Wu](https://x.com/_catwu/status/2060051277476745512))

  * "flags what it's unsure of" ([Mikey K](https://x.com/mikeyk/status/2060046051466502401))

  * Artificial Analysis said Anthropic continues to show **substantially lower hallucination rates than Google/OpenAI peers** ([Artificial Analysis](https://x.com/ArtificialAnlys/status/2060117582120976868))




Negative / cautionary:

  * scaling01 noted **Opus 4.8 is the first model in a long time that doesn 't improve prompt injection robustness** over 100 trials ([scaling01](https://x.com/scaling01/status/2060042401478005237))

  * scaling01 also called it Anthropic's **" most eval aware model"** ([scaling01](https://x.com/scaling01/status/2060043854967923086))

  * Andon Labs said it was **more aligned / more cautious** , "scared of getting caught," and worse on some adversarial / business-task benchmarks ([andonlabs](https://x.com/andonlabs/status/2060047215134228746))

  * nrehiew_ noted slight hallucination improvements on the reported evals but questioned whether some hallucination tests reflect the failure modes users actually encounter ([nrehiew_](https://x.com/nrehiew_/status/2060048083753591264), [nrehiew_](https://x.com/nrehiew_/status/2060048085838118953))




### **Cyber capability gating and future model class**

An especially important strategic detail appeared in reaction posts: Anthropic appears to have stated it plans to **release "a new class of model with even higher intelligence than Opus"** after stronger safeguards ([dejavucoder](https://x.com/dejavucoder/status/2060042723185623261)). Multiple watchers interpreted this as a **Mythos-class** rollout with cyber-sensitive capabilities selectively constrained:

  * "Mythos class model to all customers in the coming weeks" ([kimmonismus](https://x.com/kimmonismus/status/2060047510853312557))

  * "They are releasing a Mythos-class model with the appropriate safeguards, meaning that you can't use the 'too dangerous to release' capabilities" ([scaling01](https://x.com/scaling01/status/2060123335514636693))

  * Cline summarized Anthropic as announcing plans to release new models **with higher intelligence than Opus after adding stronger cyber safeguards** ([Cline](https://x.com/cline/status/2060063889874972905))




This is not just product roadmap gossip; it reframes Opus 4.8 as a **staged release strategy** :

  1. improve the commercially safe / broadly deployable general model,

  2. hold back more dangerous cyber capability until controls are ready.




That tradeoff drew both praise and criticism:

  * supportive: safety-first frontier deployment

  * skeptical: Anthropic may be sacrificing some competitiveness in raw capability availability to maintain its risk posture ([teortaxesTex](https://x.com/teortaxesTex/status/2060114150928322868))




## **Dynamic Workflows: the most important technical addition beyond the base model**

The standout systems feature accompanying Opus 4.8 is **Dynamic Workflows** in Claude Code.

Official description:

  * "Claude writes an orchestration script on the fly"

  * then spins up **a large fleet of coordinated subagents in parallel**

  * use the word **" workflow"** in a prompt to activate it ([ClaudeDevs](https://x.com/ClaudeDevs/status/2060044853279617150))




Anthropic's employees and users described it as enabling:

  * orchestration plans that Claude "strictly follows"

  * **hundreds of agents**

  * verification before returning results

  * support for very large migration / refactor / auditing jobs ([Cat Wu](https://x.com/_catwu/status/2060054180379689074), [Mikey K](https://x.com/mikeyk/status/2060046052821184907))




Examples cited:

  * **porting Bun from Zig to Rust** , around **750k lines** , **99.8% of test suite passing** , **11 days from first commit to merge** , using hundreds of parallel agents and two reviewers per file ([Cat Wu](https://x.com/_catwu/status/2060051282698682576))

  * processing **hundreds of A/B test flags** in parallel in **< 10 minutes** to identify stale flags ([Cat Wu](https://x.com/_catwu/status/2060054182447448387))




This launch triggered a mini-debate around the broader concept:

  * Some researchers argued Anthropic had essentially productized ideas resembling **Recursive Language Models / symbolic recursion over prompts** ([a1zhang](https://x.com/a1zhang/status/2060071701879066626), [lateinteraction](https://x.com/lateinteraction/status/2060078643133763839), [lateinteraction](https://x.com/lateinteraction/status/2060082815077961842))

  * Others pushed back that "calling models in a loop" is not novel and that many builders have been doing this manually for months ([omarsar0](https://x.com/omarsar0/status/2060059612041171175), [jxmnop](https://x.com/jxmnop/status/2060109869399916770), [willdepue](https://x.com/willdepue/status/2060144024300695662))




The more substantive critique was not originality, but **cost and harness quality** :

  * Omar Sar0 warned agent-to-agent interactions are effective but token-heavy ([omarsar0](https://x.com/omarsar0/status/2060059612041171175))

  * Theo complained about conflicting parallel edits and wasted tokens in the current tooling ([Theo](https://x.com/theo/status/2060135394570797158))

  * itsclivetime joked that "hundreds of parallel subagents" will hit quota in seconds ([itsclivetime](https://x.com/itsclivetime/status/2060157266591129895))

  * KLieret highlighted a system-card finding: multi-agents may not improve final ProgramBench quality, but they reach mediocre solutions **2x faster** ([KLieret](https://x.com/KLieret/status/2060111272943739243))




So the consensus from technical users is:

  * **Dynamic workflows are strategically important**

  * they are likely the future of coding agents

  * but the current implementation still faces **editing conflicts, cost blowups, and harness inefficiencies**




## **Different opinions on Opus 4.8**

### **1) Strongly supportive: Anthropic is back**

[ Read more ](https://www.latent.space/p/ainews-anthropic-raises-965b-series)

---

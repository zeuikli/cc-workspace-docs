---
title: "Latent Space — 2026-05-21"
date: 2026-05-21
source: Latent Space
type: ai-news
---

# 🔬 Latent Space — 2026-05-21

> swyx 開發者簡報，未公開專案 + 工程視角
> 來源：[Latent Space](https://www.latent.space/feed)

---

## [Railway: The Agent-Native Cloud — Jake Cooper](https://www.latent.space/p/railway)
*🔬 Latent Space | 2026-05-20*

_Take the[2026 AI Engineering Survey](https://notion.qualtrics.com/jfe/form/SV_bP07tSVMXH7ePCS) and get >$2k in credits and [AIE WF tickets](https://ai.engineer/wf)!_

_This was recorded before Railway suffered a[major GCP outage](https://x.com/JustJake/status/2056881510939283776) on May 19, despite being a multi-AZ, multi-zone mesh ring, with HA fiber interconnects between their Metal <> GCP <> AWS, because workload discoverability was unintentionally still tied to GCP. All has been resolved with a [post-mortem](https://blog.railway.com/p/incident-report-may-19-2026-gcp-account-outage)._

* * *

Railway **did not** start as an AI infrastructure company.

It was founded in 2020 years before agents became the default way people thought about deploying software. **Jake Cooper** , formerly at Bloomberg and Uber, started Railway with a simple obsession: **the activation energy to ship something to production should be near zero.** Push code, get a URL, iterate. No Docker files, no Kubernetes manifests, no Ansible scripts stacked on Ansible scripts.

For years, this was a slow grind. Railway spent its **first 18 months hand-acquiring its first 100 users** with Jake personally greeting every Discord signup on a second monitor.

[](https://substackcdn.com/image/fetch/$s_!DrIQ!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd84197e2-29a5-4b80-b922-ae8343deac59_1078x1034.png)[src](https://x.com/JustJake/status/2034432383286759852?s=20)

Today, Railway has raised **$124m** and is growing very fast. **A 35-person team supports 3 million users, adding roughly 100,000 signups a week.** Their bare metal data centers have a 3-month payback period vs. renting in the cloud, with **70% margins** funding aggressive cloud bursting when needed. The servers they own have actually appreciated in value as RAM prices have climbed basically meaning the **value of their hardware now exceeds the capital they've raised.**

From rebuilding Railway's network overlay over a weekend to moving the vast majority of workloads onto its own **[bare metal data centers](https://blog.railway.com/p/data-center-build-part-one)** , **Jake Cooper** is trying to build a **new cloud for an agent-native world**. In this episode, Railway's founder and "conductor" joins swyx and Alessio to unpack why the next era of software infrastructure is not just ["](https://blog.railway.com/p/heroku-walked-railway-run)**[Heroku but newer,"](https://blog.railway.com/p/heroku-walked-railway-run)** what agents need that humans did not, and why the old deployment loop of Git, PRs, CI/CD, and static cloud resources may be heading for a rewrite.

We go deep on **Railway 's infrastructure stack**: own-metal data centers, three-month cloud payback periods, cloud bursting, data center debt, Railpack, Nixpacks, Temporal, feature flags, Central Station, content-addressable filesystems, agent-safe production forks, and why the CLI may become more important than the canvas in an agent world. Jake also shares the founder journey behind Railway, how the company **survived losing $500K/month** , why it now **serves millions of users with only 35 people** , and why he believes the **pull request is dying**.

* * *

**We discuss:**

  * How Railway went from a slow six-year grind to adding 100,000 users a week

  * How Railway thinks about agents as **the next dominant software species**

  * Why agents need version control, observability, compute, storage, and orchestration at 1000x scale

  * The economics of **Railway 's own-metal data centers** and three-month payback

  * How Railway uses cloud bursting while scaling its own infrastructure

  * Why data center debt can be a better tool than venture debt for infra startups

  * [Central Station](https://station.railway.com/), Railway's internal system for clustering customer feedback and incidents

  * Why responsible disclosure and over-communication matter for platforms

  * Why feature flags, progressive rollouts, and shadow traffic are essential for agents

  * Temporal's strengths, pain points, and why workflows matter for agents

  * Railpack, Nixpacks, Nix, and lazy-loaded content-addressable filesystems

  * Why "cattle, not pets" may change if you can clone the pets

  * Why Railway is building a new cloud from scratch instead of copying hyperscalers

  * The solo founder path, focus, writing, and how Jake thinks about company building




* * *

**Railway:**

  * **Website:** <https://railway.com/>

  * **X:**<https://x.com/Railway>




**Jake Cooper:**

  * **LinkedIn:** <https://www.linkedin.com/in/thejakecooper/>

  * **X:** <https://x.com/JustJake>




* * *

## Timestamps

00:00:00 Introduction: What Is Railway?  
00:02:07 Jake's Path to Railway  
00:06:13 Railway's Six-Year Growth Story  
00:08:52 Rebuilding the Business After the Free Tier  
00:11:17 Agents as the Next Software Platform  
00:13:29 Railway's Infrastructure Philosophy  
00:15:42 Bare Metal, Cloud Economics, and the Compute Crunch  
00:17:22 Cloud Bursting and Five-Cloud Networking  
00:20:20 Data Center Debt and Infra Financing  
00:23:31 Data Centers in Space  
00:25:24 What Agents Need From Infrastructure  
00:28:24 CLIs, Canvas, and Agent-Native UX  
00:35:15 Central Station, Incidents, and Responsible Disclosure  
00:40:30 Safe Rollouts, SRE Agents, and Production Forks  
00:45:00 AI SRE, Specs, Code, and Tests  
00:48:24 Self-Replicating Infrastructure and the New Serverless  
00:53:18 Heroku, Temporal, and Workflow Engines  
01:04:07 Railpack, Nixpacks, and Lazy-Loaded Filesystems  
01:06:01 Coding Agents, Token Spend, and Roadmap Acceleration  
01:10:56 The Pull Request Is Dying  
01:12:28 Feature Flags and the Agent-Era SDLC  
01:16:15 Cattle, Pets, and Cloning Machines  
01:19:29 Solo Founder Lessons  
01:24:12 Focus, GPUs, and Building a New Cloud  
01:28:20 Closing Thoughts

* * *

# Transcript

**Alessio [00:00:00]:** Hey, everyone. Welcome to the Latent Space Podcast. This is Alessio, founder of Kernel Labs, and I'm joined by Swyx, editor of Latent Space.

**Swyx [00:00:10]:** Hey, hey, hey. Today we're in the studio with Jake Cooper of Railway.

**Alessio [00:00:14]:** Conductor of Railway.

**Swyx [00:00:15]:** Conductor at Railway. Yeah.

**Alessio [00:00:16]:** Choo-choo.

**Swyx [00:00:17]:** Do you actually have that anywhere, like on your business card?

**Jake [00:00:20]:** We call some of our volunteer moderators conductors. I don't have a business card. We're not that big yet. At some point I will. I got handed a nice business card from the Supermicro folks, and I was like, "Damn, this is pretty official."

**Swyx [00:00:30]:** Business cards are coming back.

**Jake [00:00:32]:** They're cool. They're hip. The conductor thing is good. We're trying to figure out what we want to call each other internally. Some people think it's super cringe and say, "You don't need a name for people internally." Some people want to call each other something. We still don't have a really good one.

**Jake [00:00:55]:** We've got New Railcrews, Trainiacs. Nothing has stuck yet.

**Swyx [00:01:00]:** I like Trainiac. Trainiac sounds good. Railwayians. For those who don't know, what is Railway? Let's give people a crisp definition up front.

**Jake [00:01:09]:** Railway is the easiest way to ship anything. You go to the canvas, or you talk with Claude, and you say, "Deploy a Postgres instance, deploy my GitHub repository, run this code," and you're off to the races.

**Swyx [00:01:22]:** You've got a nice animation on the landing page.

**Jake [00:01:24]:** Thank you. None of my work, by the way. They don't let me touch the design stuff anymore.

**Jake [00:01:25]:** We want to make it trivially easy not just to deploy things, but to evolve applications over time. Most tooling right now stacks entropy on top of entropy: Docker, Kubernetes, Ansible scripts, and all these other things. If we can version all of your software and keep track of all the changes, then we can make it trivial to clone environments, fork into a parallel universe, get copies of production data, get copies of any services, make changes, validate them, and collapse them back in without reproducing everything across a staging environment.

## The Railway Origin Story: From Uber Systems to a New Cloud

**Swyx [00:02:07]:** I was looking at your background: Bloomberg, Uber. Nothing immediately stands out as, "This guy is going to found the next great platform as a service." What prepared you for Railway?

**Jake [00:02:21]:** It was curiosity to keep going deeper. I started out on front-end stuff, working on Wolfram Mathematica and porting it over. Then I briefly moved to Bloomberg, then toward Uber and distributed systems, taking the Jump Bikes systems and moving them to a distributed system built on top of Cadence, the pre-Temporal Temporal.

**Swyx [00:02:44]:** Which, by the way, I'm happy to talk about, pros and cons.

**Jake [00:02:48]:** Totally.

**Swyx [00:02:51]:** But let's do the Railway story.

**Jake [00:02:52]:** It has been a continual step of wanting an experience. Whether it's walking up to a bike, unlocking it, and having it work frictionlessly, or something else, the depth required to make that happen follows from the experience. A lot of the work I do, and a lot of the team does, is in service of that experience. We fundamentally don't care how deep we have to go. We will swim to the bottom of the swimming pool to get the experience.

**Jake [00:03:17]:** I don't have a physics PhD. I did an EECS degree. It has always been about figuring out the next step: how do we get there? That's what led to starting Railway for that experience and then moving all the way to bare metal data centers. I was adding patches to the kernel this week to get the experience there because I can see how much better it can be.

**Swyx [00:03:49]:** Other patches to the Linux kernel this week?

**Jake [00:03:51]:** Yeah. Not upstream. Our fork.

**Swyx [00:03:52]:** That's a flex. Railpack? No, this is different. This is the OS on top of Railpack?

**Jake [00:03:57]:** No, this is an actual kernel patch. It's always literally: what do we have to do to get that experience? Then figure it out. Anything is figureoutable.

**Swyx [00:04:10]:** Would you send the patch upstream, or does it not fit other use cases?

**Jake [00:04:13]:** Maybe. We have to work out the experience internally. It has to do with the storage layer we're building for some of the agentic stuff. Maybe it'll be useful upstream, but it's deeply useful for us internally.

## Open Source, Forks, and Non-Deterministic Versioning

**Swyx [00:04:29]:** You mentioned open source before. How do you think about starting from open source, and then coding agents letting you do a lot more from forks of it?

**Jake [00:04:38]:** GitHub's original sin is that it's almost a series of broken pointers. You have this thing, then you clone it, and now you've lost the whole upstream. How do we make it trivial for people to modify really small pieces of it?

**Jake [00:04:51]:** We think of Git in a discrete sense: I've either made a change and merged upstream, or I haven't. What would it look like if it were percentage-based, a little more non-deterministic, or a stream of changes that users traverse as a percentage rolled out in general and then rolled all the way up?

**Jake [00:05:13]:** We have the open-source kickback program and let you deploy templates because we want to make it trivial for people to version these shards over time. It solves a large problem around authentication, authorization, and security. NPM has a way to define, "Don't take any new packages." The ideal end state is that you roll out progressively to users with the minimum impact zone and continue rolling up. JPMorgan should probably be the last one on the patch line, for all our sakes, because our money and livelihoods are there.

**Jake [00:05:53]:** It's okay if Johnny Vibe Coder gets a broken patch because there's so much entropy in the system that the rubber has to meet the road at some point. You have to test at varying levels.

## The Long Grind: First Users, Free Tier, and Making the Business Work

**Swyx [00:06:13]:** I wanted to pull up this glorious chart, which is your usage or number of daily signups?

**Jake [00:06:22]:** Daily signups, I think.

**Swyx [00:06:24]:** You started six years ago. It was a slow grind, and now you're on a rocket ship. You say, "Don't doubt your fight and don't quit." Maybe pick out certain points that were key inflections for the company.

**Jake [00:06:40]:** At the start, it's about getting your first 100 users, hell or high water. We had a website and a support link. The support link was the Discord channel. I had notifications on with two monitors: the monitor I was working on and the other monitor with Discord. If anybody came in, I was immediately like, "Hey, how's it going?" It was rare, so getting those first 100 users to come back was the start.

**Jake [00:07:14]:** Then you build a consultancy factory because users want all these things. You have to go back to the board and ask, "What is the actual product offering I want to build on top of this?"

**Jake [00:07:28]:** VCs want charts that always go up and to the right, but in reality you don't necessarily want charts that look like that. For us, there have been periods of expansion where we add features to test use cases, and periods of compaction where we ask, "If the experience we have is good, how do we make it significantly better?" Maybe we strip out features that don't fit our ICP anymore.

**Jake [00:07:57]:** The boom from 2022 to 2023 came from the free tier. Everybody under the sun was using it.

**Swyx [00:08:09]:** A lot of Reddit bots and Discord bots.

**Jake [00:08:12]:** And crypto miners. When you build an open product on the internet where anybody can sign up, the internet is a horrible place with so many things. You go through periods of asking, "How do I reach as many people as possible?" Then, "How do I fit the exact use case for the people who really matter and are really excited about this specific thing?"

**Jake [00:08:39]:** Then there was a two-year period of making the actual business work. During the free-tier era, we were losing about half a million dollars a month.

**Swyx [00:08:59]:** On a $20 million bank account.

**Jake [00:09:02]:** On a $20 million bank account with maybe $50,000 a month in revenue. That's a horrible business. I don't know how anybody invested. But you have to go through it and say, "We have an experience people love, but the business has to work."

**Jake [00:09:17]:** There are two schools of thought. You can run the horrible business all the way up with bad margins, or you can go back and make it work. We've always wanted a super lean team. We're 35 people right now. It's very small.

**Swyx [00:09:36]:** Supporting three million already?

**Jake [00:09:38]:** Yeah. We're adding 100,000 users a week right now, so it's growing fast. We don't want to add headcount for the sake of headcount or throw bodies at problems. We want to build systems. It's hard to build systems during expansion because you're adding things to the system because people are asking for them or things are breaking.

**Jake [00:10:00]:** We had to cut off the free users for a little while, rebuild the business, and make sure it worked. We want to reach as many people as possible because software is important. It's become difficult to create things in the physical world, so it's important to make it easy for people to build in the virtual world and have access to creation. But there are legs to that journey.

**Jake [00:10:30]:** You can see divots in the charts. If you follow between 2025 and 2026, it's either summer or winter. People go on holiday with family.

**Swyx [00:10:50]:** It affects that much?

**Jake [00:10:51]:** Yeah. It's kind of B2C and kind of B2B. People are shipping constantly, then they stop. Our activation curve now shows more people activating on weekdays because we have more business users, so it smooths out over time.

## Agents as the New Interface to Deployment

**Swyx [00:11:17]:** Was there a point where you started prioritizing AI development or agent development?

**Jake [00:11:24]:** We've prioritized agentic as a top-of-funnel thing. Over the last six months, we've deeply prioritized agentic as a mechanism to build and deploy things because we believe the curve is so steep and that is how people will build and deploy software.

**Jake [00:11:42]:** It almost fundamentally doesn't matter whether this is dot-com or not because we're all on the internet anyway. If agents are going to deploy a bunch of things and we hit an inference wall at some point, we'll fix those problems. The dominant species over the next 10 years is that we've moved from assembly to C to C++ to JavaScript to words. You're going to need to close that loop.

**Swyx [00:12:13]:** When you say this is dot-com, did you mean buying the domain, or the general case?

**Jake [00:12:17]:** I mean the dot-com era, when companies had a huge run-up because people understood the internet was important. Then they hit bottlenecks, fundamental laws of physics, math didn't work, and everybody came back down to earth. But it didn't matter because the internet became so impactful. If you operate on a long enough time horizon, you should build these things anyway because you can see where it's going.

**Jake [00:12:45]:** That's where I think a lot of agent stuff is. You get to a point where you're running thousands of agents in parallel. What is the inference cost? What is the compute cost? How do you make that efficient? How do you coordinate all this? We have issues coordinating humans; we don't even have good tooling for that. Now we have to figure out how to get agents to coordinate, safely version changes, and know when to raise their hand for someone to intervene. Otherwise it becomes an interrupt factory.

## Railway's Infrastructure Thesis: Network, Compute, Storage, and Metal

**Swyx [00:13:19]:** Let's go right into the technical side. What are the core infrastructure or architectural beliefs of Railway that allow you to do what you do?

**Jake [00:13:29]:** The primitives matter a lot for us. We need network, compute, storage, and orchestration around it. You need control over a lot of those things. We've talked a lot about how we don't really use Kubernetes because we want higher-order control to place workloads in very specific places.

**Jake [00:13:48]:** The reason is that you have to be very efficient with agents: memory reuse and all these other things, or you're going to massively blow up your cost structure. Being able to rack and stack your own servers and build your own metal unlocks performance and cost. Experiences where you're running 1,000 agents in parallel are not massively cost prohibitive.

**Jake [00:14:13]:** Token use and compute use are blowing up. Over time, those things have to get a lot more efficient. You can get a lot of margin to make those experiences solid by building your own metal. That's all in service of offering a differentiated experience to as many people as humanly possible.

**Swyx [00:14:51]:** You have a data center in Singapore.

**Jake [00:14:53]:** Yeah. We have two in every other region now. In Singapore, we're adding a second one in Q3.

**Swyx [00:14:58]:** What's it like? I've never built a data center. Do you go to Equinix and say, "I want some slots?"

**Jake [00:15:05]:** Yeah. Equinix. You basically go and say, "I want power and I want a cage." They say, "Great, here's what it's going to be." You rent the cage for a period of time, fill it with racks and servers, and hook up internet to it. That's all the pieces.

**Swyx [00:15:36]:** Then you handle everything else.

**Jake [00:15:37]:** You handle everything else.

**Swyx [00:15:39]:** What's the math versus clouds doing it for you?

**Jake [00:15:43]:** If we rented in the cloud, our payback period when we go to metal is about three months.

**Swyx [00:15:50]:** Which is crazy.

**Jake [00:15:51]:** It's nuts. That's four years of depreciated hardware. You're going to see a lot of this compute crunch because hyperscalers are buying up a lot of stuff. We're working directly with OEMs, resellers, and people building these machines: Supermicro, Dell, and others.

**Jake [00:16:11]:** Upstream, there's a bunch of supply pressure. When we raised our last round, between deploying capital for servers and now, the amount of money we've raised is less than the amount of money we have in the bank plus the value of the servers because the servers have appreciated as RAM has gone up. It's nuts how valuable hardware has become.

**Jake [00:16:50]:** If you look at hyperscalers, they deployed around $80 billion of capital expenditures this year, and next year will be more. That's a massive infrastructure build-out. You look at that and think it's crazy that they're spending way more than the Manhattan Project. But if every person is going to run dozens or hundreds of agents in parallel, you have no conceptual idea how much compute is required to make that experience happen, even if you're deeply efficient and sharing resources. And that doesn't even count inference.

**Swyx [00:17:22]:** How do you plan the build-out? The growth chart is so vertical. Are you usually at 100% utilization as soon as racks are live? How far ahead are you planning?

**Jake [00:17:33]:** We still maintain cloud presence for bursting. We work with AWS, GCP, and a few other clouds. We can rent, and then the moment we get space or power, we compact those workloads off the cloud. We started on the clouds, then built a system to migrate to our own metal. There's nothing that says you can't continually do that again, and that's exactly what we do. We never want to be compute constrained.

**Jake [00:18:09]:** At the start of the year, we actually became compute constrained because one upstream provider wasn't able to give us quota at the rate we needed, and the hardware was slower. I spent a weekend rebuilding our entire network overlay so we could straddle five clouds: Oracle, AWS, ourselves, GCP, and one other one. We can do more than that now.

**Jake [00:18:38]:** We got into a spot where we were trying to pack instances tight because we couldn't get enough compute. That led to a few reliability issues, which are now past us. I made a tweet pointing out that it's becoming harder and harder to acquire compute at the rate these models need to acquire compute. We got bit by it.

**Swyx [00:19:15]:** How do you think about pricing knowing you might not have your own metal available at all times? Are you pricing assuming you need extra margin if you end up going into the cloud?

**Jake [00:19:26]:** Because we've built out our metal data centers, our margins on metal are around 70%. We can deeply subsidize the cloud business if we want to scale at a reasonable rate. We have a few levers: metal, which makes the margins; cloud burst; debt to buy servers; and venture capital. It's an interesting operational problem: how much cash do we have, how much should we raise, how quickly can we deploy it, and can we scale revenue as quickly as we scale compute?

**Jake [00:20:05]:** If we continue making it trivially easy for people to build and deploy, then the faster we close that loop and the more operationally excellent we are with capital, the faster the business can scale. It's almost a straight linear deployment rate.

## Financing Infrastructure: Hardware Debt, VC, and Operational Leverage

**Swyx [00:20:20]:** I think infra startups raising debt is a tool people don't utilize enough or know enough about. What can you tell us about that? Is it secured against your CPUs?

**Jake [00:20:32]:** It's secured against our hardware.

**Swyx [00:20:37]:** What rates do you get? Who are the lenders?

**Jake [00:20:39]:** We pay prime plus a spread, and we can refinance any of the debt as rates go down. The terms are pretty good. The unfortunate thing is that Twitter has no nuance, so people say, "Venture debt bad." But as with all things, there are specific tools and areas where you can be deliberate instead of using one tool as a hammer. Venture capital is not the hammer for everything. You have to explore and figure out what works.

**Swyx [00:21:12]:** VC is usually the most expensive financing you can get.

**Jake [00:21:15]:** Yeah. I also think people think about VC incorrectly from a capital-raising perspective. Most people think, "How do I raise as much money as possible from whoever is probably the best I can get at that time?" That's close to right, but what we've tried to do is figure out what unfair advantage we can buy with that equity.

**Jake [00:21:34]:** It's the most expensive equity you're going to give away at that point in time, assuming the company keeps getting better. How do you use it to work with someone stellar who complements you? In the seed stage, I had never started a company. Ray Tonsing had good advice, and I could text him all the time. He was really fast. Awesome.

**Jake [00:22:01]:** Then with John and Erica at Unusual, they said, "You roughly know what you're doing building a product. We'll mostly leave you alone and be available for advice." Amazing. Then we got to Series A and the business was an operational tire fire because we didn't know how to scale a business. Work with Erica, and Jordan is over at Redpoint, so bonus.

**Jake [00:22:28]:** Now we've raised from TQ and FPV as we're moving into enterprises. Every step of the way, we've asked: who can we partner with at this specific time to unlock the next section of the journey? I don't know enterprise sales. As an engineer, I can eyeball what features we might need, and we have wonderful people internally who can help. But you want boardroom dynamics where everyone is aligned and asking, "How do we win this?" instead of bickering about strategy.

## Data Centers in Space and the Physics of Compute

**Swyx [00:23:31]:** You had a tweet about data centers in space. Why no data centers in space?

**Jake [00:23:37]:** It's not "no data centers in space." My hot take is that I think it is solvable. I've just never seen anybody solve it.

**Swyx [00:23:49]:** You said, "How are you going to dissipate that much heat in a vacuum?" You're making a physics claim.

**Jake [00:23:55]:** I haven't seen anybody prove how you're going to dissipate that much heat in a vacuum. It doesn't mean it's not possible. It just means nobody has brought it up yet.

**Swyx [00:24:05]:** Astrophage.

**Jake [00:24:06]:** I don't know what that is.

**Swyx [00:24:07]:** The Martian thing. Okay, you're very logical.

**Jake [00:24:09]:** It could work. A lot of people are putting the cart before the horse. They say, "We're going to put data centers in space." Okay, but how? "We have time to figure it out." It's like in The Martian where they ask how they're going to intercept something and say, "We'll figure it out."

**Swyx [00:24:36]:** Making a bet on human invention is weird because you blind trust that it can be solved. But with physics, there are first-principles bounds you can put on it. Maybe not. Maybe you're asking to travel time or break a fundamental thermodynamic law.

**Jake [00:24:57]:** I don't know how VCs do this either. How do you know what's not possible and a grift versus what's possible but sounds completely insane? "We're going to put data centers in space." Coin flip as to which it is, and I guess you'll know in 10 years. That's one cycle.

## What Agents Need: Versioning, Observability, and 1,000x Scale

**Swyx [00:25:23]:** Moving back to agents. The branching, fast spin-up, and orchestration you do feels like pre-work that happened to be exactly what agents want. What do agents want differently than humans?

**Jake [00:25:37]:** They want the ability to version things. It's not that different; it materializes slightly differently. Agents want a way to test changes incrementally. Engineers have feature flags. Is there a reason agents can't use feature flags? I don't think so.

**Jake [00:25:54]:** They want version control. Can we use Git or not Git? That one is up in the air. I think something outside Git will emerge for how we version these things over time. They need observability. You need to query what happened, when it happened, which steps failed, traces, logs, metrics, and all the rest. They need network, compute, and storage. They need to write files, save files, iterate on files, and snapshot file systems.

**Jake [00:26:25]:** A lot of what humans needed is in line with what agents need. Branching and forking are not different; we're just moving 1,000 times quicker. It can look like you need something massively different, but what you need is something massively better than what existed. You need orchestration massively better than Kubernetes. You need networking probably better than Envoy. It goes all the way down the stack.

**Jake [00:26:55]:** If the workload profile doesn't change so much as it gets massively compressed because you need thousands of these things, what assumptions change? etcd is going to melt. You need to replace it with something. You can go all the way down the stack and say, "That part has to change, that part has to change, and that part has to change."

**Jake [00:27:19]:** The interesting thing about the super-exponential curve is that you have to build systems where you can rip out those parts at any time because a new bottleneck might emerge. You get good at parallel agents, and a different part of the system breaks. So it's similar to what humans needed, but at 1,000x scale.

**Jake [00:27:55]:** How do you do code review in the age of agents?

**Swyx [00:28:00]:** You throw more agents at it.

**Jake [00:28:01]:** You don't. But then who reviews for CVEs and all these other things?

**Swyx [00:28:07]:** More agents.

**Jake [00:28:08]:** And that's how we hit the inference wall. You can continually throw agents at the problem, but I think there's a limit to the number of agents you can throw at a problem.

## CLI, Agent Handles, and Closing the Loop

**Swyx [00:28:24]:** You already had a CLI before it was cool. How is the shape of what you're exposing changing, if at all?

**Jake [00:28:28]:** CLIs have always been cool. The CLI changes because we think about how to give Claude, Codex, ChatGPT, or any model a handhold.

**Jake [00:28:50]:** A CLI is a single command: deploy, get logs, and so on. Things that were prohibitively annoying to humans are not annoying to agents. They're nice. If I handed you a CLI with 40 arguments and 600 flags, you'd think, "I'm never going to use all of this." But if you hand it to an agent, it says, "This is excellent. I have so many handles to work with."

**Jake [00:29:24]:** If you're going to expose things to agents that way, you want as many handles as possible where they can get information, query dynamic information, and close the loop quickly. Most problems right now are about how to close the loop as quickly as possible. Where does the agent get stuck, and how can you remove that?

**Jake [00:29:49]:** Telemetry is important. If you can tell where the agent gets stuck from the CLI and say, "12% of people deviate from the happy path because of this, and now I add this argument and drive it down to 2%," you massively increase the rate of loop closure.

**Jake [00:30:03]:** That's how we think about not just the CLI, but every point in the dashboard. It's a user journey: I hear about Railway. I get something deployed. I get my first green build or aha moment. I see an endpoint, logs, whatever. Then I iterate. The iteration loop is indefinite. The user wants to deploy a new thing, a Postgres instance, change code, and keep iterating.

**Jake [00:30:36]:** If you focus on the iteration loops and what's blocking them from closing quickly, one thing we say internally is: you never want to be waiting on compute anymore. You always want to be waiting on intelligence. If you're waiting on compute, there's a bottleneck that needs to be destroyed because eventually that bottleneck becomes so large that another workflow emerges to change it.

**Jake [00:31:04]:** We've built a product where you push code, build it, and so on. But I fundamentally believe the push-pull loop is going away. We'll get to a point where you make a small change in production, that change is versioned across your infrastructure, you're working alongside copy-on-write versions of your database and infrastructure, and then you merge it in and it's instantaneously live. That's the holy grail of loops. The push-pull-rebuild thing is a point of friction that we're removing entirely.

## Canvas as Output: Dashboards, Context Anchors, and Hyperstructures

**Swyx [00:31:43]:** It's incredibly fast. If anyone hasn't tried it, that fast feedback is great. My hot take is that Railway was famous for its canvas, which visualizes your infrastructure and lets you manipulate it visually. But that was for humans. For the next phase of growth, Railway CLI is more important than canvas.

**Jake [00:32:05]:** The canvas is funny because it's a mechanism to show changes over time. You're right that previously we used it a lot as an input. Moving forward, its goal is more like an output. You would go to the canvas, make changes, see them, and watch your infrastructure evolve. Now agents have access to the CLI and can make those changes. So the canvas becomes an output: what information does the human need at this moment to make suitable decisions about control requests? Do I approve this or not?

**Jake [00:32:57]:** It also has to be an anchor for your context, a port in the storm. Think of it like layers in a file system. You start with a project, then drill down into services, then into a function or code, because you want to represent the entire thing not just in your head, but in the canvas. Other people can share that representation, think on the same wavelength, and move quickly.

**Jake [00:33:33]:** A lot of organizations get in trouble as they scale because all the context lives in someone's head. "How does this microservice work?" "I have no idea; go ask this person." Then you have whole categories of products built around context discovery. A lot of that melts away if you have a solid hierarchy and can infinitely nest services, code, context, and everything else all the way down. That's what lets you build these structures over time.

**Jake [00:34:18]:** It's also what lets us build what I've called hyperstructures: things that are way bigger. You look at the Golden Gate Bridge and ask, "How did we build that?" There's a meme that we lost the technology. To some extent, yes, because the coordination that built those things evolved and changed. We lost some of the art of building structure as we jammed everything into Slack.

**Swyx [00:34:52]:** But you jam everything in Discord.

**Jake [00:34:53]:** Same point. It doesn't matter. It's message passing and interrupts, message passing and interrupts.

**Swyx [00:35:00]:** So you're arguing there should be something better and more structured than Slack?

**Jake [00:35:04]:** Yeah. For sure. I think Slack is awful, and Discord is awful too.

## Central Station: Context Routing, Support, and Incident Clusters

**Swyx [00:35:09]:** This is the equivalent of my mom test. What have you done that has your solution to this?

**Jake [00:35:15]:** Internally, we've built a tool called Central Station that aggregates all the context from our users. Every piece of feedback, every customer support item, everything gets aggregated into clusters. If an incident is brewing, we can determine how many users are affected and break off a discussion based on that.

**Jake [00:35:40]:** That is more helpful than long-running channels where you're trying to decide which channel to put something in. If you can dynamically aggregate information and dynamically route it to the right person based on context, it works better. We know internally that these four people are close to networking. If we see a networking thing, we can drill it down to those four people. If it's with this part, we can look at the commits. This is no longer a manual process internally.

**Jake [00:36:13]:** If you go to station or help.railway.com, that's why we built it. We wanted to scale with a massive amount of leverage by aggregating feedback.

**Swyx [00:36:27]:** This is built in-house?

**Jake [00:36:28]:** Yep.

**Swyx [00:36:29]:** I remember helping out on this one with Angelo in 2023. You scale a lot with a very small team.

**Jake [00:36:38]:** Yeah. We're about 10 times bigger now.

**Swyx [00:36:40]:** You have your full developer code here? Very cool.

**Jake [00:36:44]:** If you go to railway.com/stats, we expose this as a pub-sub-able thing. It's all real-time metrics. There's a way to get it as JSON somewhere if you care.

**Jake [00:37:01]:** We're big on trying to build everything in public and talk about what we're working on. We've had issues in the past, and we'll say, "Here's how we're fixing these things." We've gotten compliments and flak for incident reports. We're always trying to make them better and talk with people.

## Incidents, Disclosure, and Progressive Rollouts

**Swyx [00:37:20]:** You had a big one recently. I liked that it was scoped to 3,000. You presumably used Central Station. Talk through what happened and how you address it internally as a team.

**Jake [00:37:38]:** Internally, this one really sucked. It had to do with an upstream provider that didn't do the behavior it said it documented, which is unfortunate given they wrote the RFC for how the behavior should work. We rolled those things out, and Central Station caught it initially when a couple users said caches weren't invalidating. We turned it off immediately.

**Jake [00:38:03]:** When you roll out to a large user base of three million people, you get a lot of disparate behaviors. We tested in staging and had tests, but we hit an edge case. We've hardened those systems, and now we can make that better. But it was a tough one.

**Swyx [00:38:39]:** I always wonder how private disclosure is supposed to work if people find an issue. Are they supposed to contact you first? When you run a platform, these things will happen. What channels should people pursue to quietly resolve it before it becomes a bigger incident?

**Jake [00:38:59]:** There's responsible disclosure. We err on the side of over-disclosing and letting you know something is wrong versus having your provider gaslight you. We've erred on sharing those things more publicly, even if they impact a small subset of users. That's a decision we've made internally. We have four values. One is honor. The honorable thing is to notify people to the widest degree at which they may have been affected or there was an issue, and then confront it head-on: why did it happen, what can we do better?

**Swyx [00:39:45]:** Not the whole user base. That's because of incremental rollouts and other things?

**Jake [00:39:50]:** Yeah. Progressive rollouts.

**Swyx [00:39:54]:** That should be the norm at all large platforms.

**Jake [00:39:58]:** It should. A variety of companies do this. There's the quote that Meta runs 10,000 different versions of Meta. To our earlier point about agents, they need the same thing. They need shadow traffic and all these other things. We've built so much ceremony around production being sacred that we need to make it trivially easy to test different behaviors in a safe environment. Then you can make mistakes in a safe environment.

## Safe AI SRE: Customer Agents, Forked Environments, and Production Parity

**Alessio [00:40:30]:** Do you see a world where these things get automatically caught, not necessarily by your agent, but by your customer's agent? The cache invalidation issue seems easy to check if you know to look for it.

**Jake [00:40:44]:** It's hard because to determine it, we almost need to hook into your observability infrastructure. That's why we have the template loop on the platform: so you can roll things out progressively. You can roll out to Johnny Vibe Coder initially, or push a shard that someone consumes at their own leisure. Or you can roll it out over weeks: 0.1% of people, 1% of people, early adopters, then all the way up. That's the non-deterministic version control we talked about earlier.

**Jake [00:41:30]:** I believe that's where most things should go, because most companies end up building staged rollout systems in-house. It's the same thing built again and again at every company. There's a massive opportunity to consolidate developer debt.

**Alessio [00:41:45]:** You should have a free tier. Model providers give free tokens if you let them use the data. You could give free compute if someone is the number-one shard that goes out and lets you plug into their observability.

**Jake [00:41:55]:** We do that. That's why we talked about the impact on 3,000 people. We start with lower-impact people. Larger companies on the platform are last to receive those rollouts so they have a version of the platform that's deeply stable.

**Alessio [00:42:16]:** I have three services, so I'm sure I get the first rollout. You can nuke my thing at any time. There are all these SRE agent companies. Observability people also want agents that fix upstream problems. You have your own agent in the canvas now. How do you see that playing out?

**Jake [00:42:39]:** It's the stacking entropy problem. If you don't have primitives to make iteration in production safe, it becomes difficult. If you're an observability provider saying, "Here's the fix to this error," assume 80% are good and make sense. But in the last 20% long tail of complex issues, if you let somebody stamp it, you create an opportunity for an incident.

**Jake [00:43:08]:** That's why forked environments are important. People have staging, but it always drifts from production. You need primitives, workflows, and experience built first-party on the platform so you can fork any service at any point in time.

**Jake [00:43:33]:** I think of the canvas as a sheet of transparency paper. The agent is a little guy you push up into the canvas. It should say, "I need to copy that service and that service so I can test these two things." It gets a read-only copy of production. Anything that's PII gets marked as a transform when we clone the database, create a copy-on-write version, or read from it. Then the agent makes changes and asks, "Does this actually work?" as close to production as possible.

**Jake [00:44:22]:** That's how close you have to be, or you get massive drift. The system becomes unstable. You see this with massive systems built on Docker for local, Kubernetes for production, and a specific thing for something else. That complexity slows developers and becomes unstable at scale, making it hard to iterate. We want to compress that way down and say, "As close to prod as possible is where we want to be."

## From AISRE Skeptic to Agent Believer

**Swyx [00:45:00]:** I was texting Erica for questions, and she says you were originally not a believer in AISRE. Have you come around on it?

**Jake [00:45:10]:** I flipped, but I'm still not a believer in AISRE if you don't have the primitives to make it safe. If you unleash AISRE on production infrastructure without safe primitives for copying volumes and making sure things are fine, it's going to nuke your production database. It's not a matter of if, but when. I'm a big believer in making those loops safe.

**Jake [00:45:33]:** I was a deep AI skeptic until 2023. In 2024, I thought, "Maybe I can roughly make this thing do it." In 2025, I thought, "Now I can hold this." Over winter break, everybody came back saying, "It's almost impossible to hold this."

**Swyx [00:46:01]:** Did you see this on the Claude docs? CloudBot? OpenCloud?

**Jake [00:46:06]:** It's gotten to a point where it's harder to hold it wrong than to hold it right. There's a scene in Avengers where Vision picks up Thor's hammer and says it's terribly well-balanced. It self-balances and works well. I'm a deep believer at this point that this will be the dominant species: assembly, C, C++, JavaScript, words.

**Swyx [00:46:35]:** It feels like a big jump.

**Jake [00:46:37]:** It is. But it's not like you abandon CPU-based discrete logic and move straight to fuzzy logic. You need both. Your skills should call code or applications or some static structure. You can use skills to distill what the procedure should be or how the code should act.

**Jake [00:47:02]:** I'm coming to a thesis: you need three points. You need a clear spec defining the system, the code, and the tests. When you say it out loud, if you've been in engineering long enough, you're like, "Of course. That's an RFC, tests, and code." But they all matter. Having them together lets them reinforce each other: the spec and tests match, but the code doesn't, so reconcile it. Or the tests and code match but the spec doesn't, so reconcile that. That's the iteration loop.

**Jake [00:47:41]:** That's why you're seeing people talk about software factories, docs, and reconciliation. Some of that is architectural astronomy if you don't implement it, but that loop is where most things will end up.

**Swyx [00:48:07]:** For listeners, we've been talking about this on the pod for three years: the holy trinity of specs and tests. Itamar Friedman from Qodo is the reference if people want to look it up.

## Self-Modifying Infrastructure and the End of Push-Pull-Rebuild

**Swyx [00:48:18]:** One thing I want to mention on the OpenCloud idea is self-modification. I don't know how Railway would support it, but I have my OpenClaw, and I just tell it it has the Railway CLI and can do whatever. In theory, whatever capabilities or new infra it needs, it can call the Railway CLI, provision it, and add it to itself. The agent can modify its own infra.

**Jake [00:48:45]:** It's nuts. I have a loop set up where you put the Railway CLI on top of something that runs on Railway. You're authenticated as whatever the current box is, and you can make any changes to it. Then you call Railway deploy, and it deploys itself.

**Jake [00:49:04]:** It's like: "I need to spin up this instance of this environment. I already exist in this environment. Excellent, I have access to a Postgres instance now." That's where we want to go with agentic, self-replicating infrastructure. That's your loop: iterate in production. You continue making changes. If it works, merge it upstream. If it doesn't, throw it away.

**Jake [00:49:37]:** How do you make throwaway copies trivial to spin up and super cheap? The era of "I have an AWS instance with four vCPU and 16 gigs of RAM" is going to get destroyed. If you do that for agents, you need a thousand of those machines. It's prohibitively expensive compared with what we've spent a ton of time figuring out: the atomic unit of deploy, whether you call it isolates, sandboxes, or something else. Only pay for what you use, spin up instantaneously, and close the loop as quickly as possible.

**Jake [00:50:15]:** If the system can self-replicate safely and say, "This is my environment, I'm making these changes," it can come back with, "Does this look good? This is a new state of infrastructure given this prompt. I think I've solved it." Then you go back and say, "Actually, it looks different." It does the loop again. Then you say, "Cool. Apply."

**Swyx [00:50:38]:** That's retroactively obvious, which is the most useful kind. Any other comments on agent deployment on Railway?

**Jake [00:50:51]:** It's getting better every day. I'm on X or Twitter. You can always yell at me about the parts not working as well as they should, because plenty of things should work way better.

## The New Serverless: Stateful, Long-Running, Pay-for-What-You-Use Linux

**Swyx [00:51:04]:** At this stage, when people want massively or embarrassingly parallel compute, they usually talk serverless. I feel like there's a new serverless compared to the previous five years of serverless. You're in that new bucket. Do you have comparisons or philosophical differences you want to call out?

**Jake [00:51:31]:** It's somewhere in between. It's the ability to run stateful, long-running workflows or executions.

**Swyx [00:51:42]:** Vercel has Fluid Compute, Cloudflare has some container thing, Google has App Runner and others.

**Jake [00:51:55]:** That's where everything is roughly going, and it's why we've been working on this for six years. We believe users need access to a computer: a box that speaks Linux. They need to deploy what they want. Other systems change the surface area of what you can build. For us, users need a computer and need to deploy anything they truly want. That's why we've focused on the primitives: network, compute, storage. If we give you those and expose them so you can run things indefinitely, that's where we believe it's going.

**Jake [00:52:43]:** Twitter has no nuance, so everyone says "servers" or "serverless." It's always somewhere in the middle: I want to run it for a long time, but I don't want to provision the resource statically or pay for things I'm not using. That's been our thesis from day one: pay only for what you use, run it indefinitely, and it is full Linux.

**Swyx [00:53:12]:** That's why I like the naming of Fluid. It's fluid. Flexible.

## Heroku, Focus, and Carrying the Torch Without Becoming the Past

**Swyx [00:53:18]:** Another milestone is the Heroku official deprecation. You're one of the presumptive new Herokus. "New Heroku" has been a category for as long as I've been in developer tooling. It's finally happening. What was that like? Any behind-the-scenes of, "This is the moment"?

**Jake [00:53:42]:** You have people where you're like, "You were running stuff on here? You, as this company?" It's crazy that names you would know are running on it and now coming to us saying, "We want to move a lot of this off."

**Swyx [00:54:00]:** Any behind-the-scenes on why Salesforce let Heroku stagnate?

**Jake [00:54:05]:** I can only guess. It's hard when it's not your business. Salesforce's business is to build a great CRM. That's their focus. Then you acquire a compute business as an offshoot. A lot of early Meta people talk about focus. Boz has a write-up about how in the early days of Meta they had no money, so they were forced to focus. Then they turned on the money tree and had no reason not to split their focus.

**Jake [00:54:52]:** But that dilutes your product. You get offshoots where you ask, "Is this the focus of the business?" If it's not core, it languishes. A lot of companies get in trouble when they split focus because they're fighting a multi-front war, not just externally but internally for alignment. Where are we going? What are we doing? What is our purpose?

**Jake [00:55:24]:** If you're Salesforce-built and mission-driven, you want to work on Salesforce. Heroku is off to the side. It's not core to the business. Getting resources, budget, focus, and alignment internally becomes hard. It was a matter of time.

**Swyx [00:56:06]:** Kudos for them to call it out instead of leaving it unknown.

**Jake [00:56:12]:** Their release was a little odd. They called it out, but they didn't say they were shutting it down. Behind the scenes, I think they issued messages to people saying they should close accounts and that they were going to deprecate and remove things over time.

**Jake [00:56:30]:** It's crazy because some of my first deployment experiences were on Heroku. You start with dragging things into an FTP server, then you try to get a deploy working, and then it's Heroku. It was the on-ramp for us. But the wheel turns. New things emerge. We're happy to carry the torch for a lot of that. But we don't want to be the new Heroku. We want to be the way people build and deploy software, and ultimately the way people monetize software over time.

**Swyx [00:57:19]:** It's still a big crown to be the new Heroku. There are 50 companies that fought for that.

**Jake [00:57:23]:** Everybody is holding some portion of it. We're happy to support people and companies. The platform works differently. The game loop is similar, but we've been dogmatic about where these things are going: primitives, agents, fan-out. Some things fit; some workflows need to change. We have an approximation of Heroku pipelines with the environment system. It's exciting. We've got a ton of people we can support, and it's growing a lot.

## Temporal, Workflow Engines, and State Machines

**Swyx [00:58:12]:** I have one more technical question about Temporal. I've sold my shares. You're a power user and one of our earliest customers. I met you through Temporal. You built on Temporal. You have complaints. This may be the most neutral and informed conversation anyone will hear about Temporal without someone working at the company.

**Jake [00:58:39]:** That's fair. I've used Temporal for almost 10 years because of Cadence at Uber.

**Swyx [00:58:52]:** Give people a sense of what Cadence was at Uber.

**Jake [00:58:57]:** Cadence was the precursor to Temporal. It powers trip actions, rides, when you rent a Jump bike or scooter or car. You're running workflows for a period of time and saying, "This ride will run indefinitely until it finishes." You attach information: you paused in this zone, so add this charge to the bill. When you end the trip, the workflow is done. That experience was powered by Cadence at the time.

**Swyx [00:59:34]:** I used to say it's like programming the entire user journey top-down as one function.

**Jake [00:59:39]:** It's a powerful idea and important. It's also important for the next phase of the agentic journey. You want an agent to do a specific task, be complete or incomplete on that task, and move on to the next thing. You need a way to manage workflows dynamically.

**Jake [00:59:59]:** Temporal was always great in theory, and great when you got it working the way you wanted in production. But it required you to model the entire journey in your head. If you didn't, you could cause issues where replaying the state of the workflow causes non-determinism.

**Swyx [01:00:25]:** Because it works on deterministic workflow history.

**Jake [01:00:28]:** Exactly. I describe it as a jet engine. If you know how to operate it and run it, it's great. But you can't hand it to people trying to build complicated things if they don't have the whole state in their head.

**Jake [01:00:48]:** We run our whole deployment pipeline on top of it. That's a reasonably complicated workflow: pre-commit hooks, signaling, queuing, and all the rest. We ran into the same thing at Uber. As you express a large workflow, it gets more complicated, with more states in the state machine that you have to map back to the workflow.

**Swyx [01:01:15]:** It's a lot of ifs.

**Jake [01:01:16]:** Exactly. At Uber, we built a system for doing the state machine and testing it. We've started to build some of those things here because it's grown heavily. It's not quite love-hate. When it works well, it works super well. But if someone who doesn't have full context puts something into the system that invalidates state or causes non-determinism, or spins off a ton of activities, you have to keep track of underlying SRE knobs like activity slots. Those should scale with memory, vCPU, and so on. It becomes a bear to scale.

**Swyx [01:02:10]:** You need a capable sysadmin running things behind the scenes. If you moved off, what would you do?

**Jake [01:02:19]:** We'd build our own workflow engine. We have a few internally that we've worked on.

**Swyx [01:02:27]:** This is one of those classes of things you typically wouldn't vibe code, but I'm wondering if you can.

**Jake [01:02:33]:** I still don't think you should vibe code it. You still want to run decent tests to make sure it works.

**Swyx [01:02:39]:** Timo didn't invent that from scratch either. There are libraries you can run. On top of that, it's just a state machine that you have to map out. Ultimately, you define the instructions you want and run them through a state machine.

**Jake [01:03:00]:** It's very doable. Workflow stuff is interesting. Restate is doing neat stuff here.

**Swyx [01:03:10]:** You're tied into JavaScript. Are you a JavaScript maxi?

**Jake [01:03:13]:** Internally, we have TypeScript, Rust, and Go. We don't add more languages. Actually, we have a little C because we write BPF code and hooks. But those are the languages.

**Swyx [01:03:28]:** Is this for sidecars?

**Jake [01:03:32]:** No. It's for the networking stack, volumes, and things like that. We use TypeScript a lot because it powers the dashboard, but we're moving a lot of workflow stuff off the dashboard stack and into the infrastructure stack.

## Railpack, Nixpacks, and Content-Addressable Filesystems

**Swyx [01:04:00]:** Cool. Any other technical infrastructure stuff? Railpacks?

**Jake [01:04:07]:** We built an engine for determining dependencies based on source code. It's called Railpack. We built the first version, Nixpacks, on top of Nix, and then we moved.

**Swyx [01:04:17]:** People have been trying to get me to adopt Nix and NixOS for four years. Is it ever going to be a thing?

**Jake [01:04:23]:** I don't know. We're excited about it, but it has pain points. Think of it as a stack of versioned binaries at specific slices in time. If you want version X and version Y, you bloat the package space, which blows up image size and makes real-world workloads difficult.

**Swyx [01:04:53]:** But you content-address it and cache it. In theory, there are optimizations.

**Jake [01:05:00]:** In theory, yes. But with a large enough user base and disparate enough machines, you run into a problem Meta described in the XFAAS paper, their internal serverless system. It becomes difficult at scale unless you break out specific runtimes.

**Jake [01:05:24]:** We didn't want to do that because we wanted to truly allow you to deploy anything. That was our initial thing with Nix. But we've moved toward interesting work around content-addressable file systems that can lazy-load anything from any point and page it into memory.

**Swyx [01:05:48]:** Amazing.

**Jake [01:05:49]:** The future is very bright. It's crazy, and it's going to be nuts.

## Coding Agent Spend, Roadmaps, and Token ROI

**Swyx [01:05:54]:** Founder journey stuff?

**Alessio [01:05:56]:** Your cloud usage: you tweeted you're going to spend $300K this month?

**Jake [01:06:01]:** I think we got to $200K.

**Alessio [01:06:02]:** Coding agents?

**Jake [01:06:03]:** Yeah.

**Swyx [01:06:04]:** Across the company?

**Alessio [01:06:05]:** You only have 35 people, so I'm sure they're not all spending $10K a month. What's the distribution?

**Jake [01:06:10]:** I think I'm at about $25K. We have power users all the way down. We came back from winter break, and I basically said, "If you're writing code by hand, you're doing this wrong." The tools are good enough now that you can move extremely quickly. There are issues and pain points, but you should be reviewing the code you are writing instead of writing it by hand.

**Jake [01:06:40]:** Architectural patterns matter more now than ever, but you shouldn't spend your time generating code you would write. If you know how to write it, ask the agent to write it and reconcile it until it looks like you would have written it yourself.

**Jake [01:06:58]:** People misconstrue my propensity to push people toward agents as connected to our growth and some reliability bumps. They're not necessarily related. The tools are good enough to move extremely quickly and build things way larger than you could before.

**Jake [01:07:19]:** To the earlier point about cooling data centers in space: I don't know. But with software, you can ask, "How would I build block storage from scratch? How would I do these things?" I have ideas because I have history and have read papers. Let me work them out and build massive test benches with thousands of tests, because those are now free to author. If you're not using AI systems to speed-run your roadmap and reconcile your existing system onto the future, you're missing a large point of what's happening.

**Alessio [01:08:12]:** What's the path to spending $3 million a month? Is it bound by ideas and things customers can absorb?

**Jake [01:08:19]:** For most companies, it's bound by deployment at this point. That's why we've seen a massive boom in users and companies, from Fortune 50s down, asking how to get developers to move faster. You'll probably hit your CFO before any technical limits because they'll look at the eye-watering amount of money spent on tokens. Inference costs have to come down, but we're inference constrained now. There will be price discovery around what makes sense for an org to adopt.

**Jake [01:09:06]:** I think you'll end up with the F1 driver concept. If someone is really adept at these things, it makes sense to put them in a $3 million car. If they're not, it probably doesn't make sense. You'll take a few people and say, "You can drive the F1 car. We need to go in this direction. Figure out if it works and prototype it."

**Jake [01:09:33]:** We've done some of that and vastly accelerated our roadmap. We thought we'd ship something in a few years; now we can probably ship it in a few months because we validated it and don't have to build it incrementally. We can skip steps and move toward our vision.

**Alessio [01:09:58]:** A lot of people are realizing the roadmap doesn't always have a business impact, so they say tokens are too expensive. But if your roadmap were built to make more money by the time you built it, you'd have token pricing for it, the same way you do with sales. You'd spend a billion dollars on sales if you knew you would get $2 billion of revenue.

**Jake [01:10:19]:** Exactly. A naive way to measure this is the percentage of tokens that end up in production. If you can measure impact because those tokens end up in production, that's awesome. But the burden of proof will rise. Internally, we have a growing number of pull requests that haven't merged. The question becomes: how do you get this into production? It's about how quickly you can build and deploy software, which is exciting because that's our whole thing.

## The SDLC Shift: Prompt Requests, Feature Flags, and Safe Rollouts

**Swyx [01:10:56]:** The SDLC is changing. One thesis is that the pull request is dying. It's going to be the prompt request. Beyond that, code review is also kind of dying if you have all the other systems in place. What else is changing about the SDLC?

**Jake [01:11:19]:** The AISRE and the tools to make it happen. AISRE is pie-in-the-sky aspirational. What does it take to get an AISRE? What tools do you need to build?

**Swyx [01:11:32]:** You should expose your tooling to customers at some point. The Central Station command center.

**Jake [01:11:39]:** We have it for template maintainers. Template maintainers can deploy and maintain templates, and they get feedback. We're going to expose those things incrementally.

**Swyx [01:11:51]:** Clustering around incidents. Everyone has a version of that, but I don't think anyone has solved it.

**Jake [01:11:56]:** I won't say we've solved it internally, but it's gotten so good that we can see incidents forming pretty quickly. At some point, those will be things either someone else builds or we build. We've always built things purpose-built for us. If it makes sense to make it useful for users, monetize it, or turn that loop into a profit center instead of a cost center, we want to do that.

**Jake [01:12:28]:** Pull request is definitely dying.

**Swyx [01:12:29]:** Do you do first-party feature flagging and incremental rollout stuff?

**Jake [01:12:34]:** We have a feature-flagging engine we built internally and will eventually roll out.

**Swyx [01:12:38]:** I don't see it as a user. How come you didn't give us what you have?

**Jake [01:12:43]:** We have to beta test it. We care a lot about the quality of the things. There's plenty we've used internally that doesn't make it all the way through the journey because it fails. It works for one service but not multiple services. We'd have to build it for multiple services and know that if we released it, we'd rebuild it again and again. Some things are worth that, but many inform the roadmap.

**Jake [01:13:18]:** We don't want to dilute the experience by saying, "This works, but only for this service," unless it's a core initiative. Over the next few months, we'll roll out things that work for a single service, then multiple services, then multiple services across the environment. You have to be deliberate. Otherwise you create broken disparate experiences and support load because people ask how to use the feature.

**Jake [01:13:52]:** It's the earlier expansion and compaction pattern. You expand the company to get features, then compact and smooth them out so the experience is stellar. You told me in the hallway, "It's gotten so much better." Internally we're saying, "This part really sucks. We need to make it significantly better."

**Swyx [01:14:11]:** I can attest to that over the last three years watching you build Railway. For listeners, feature flagging is a huge part of Uber culture. So much so that they have too many feature flags and another thing to remove feature flags. Facebook has Gatekeeper. Agents are going to need this. It's fundamental to incremental rollouts. OpenAI acquired Statsig. GPT-5 is routing and flagging through different models.

**Jake [01:14:56]:** It's super important. If the software development lifecycle is going to change because we're doing things 1,000 times faster and 1,000 times more concurrently, what becomes important at scale?

**Jake [01:15:16]:** Before I started Railway, I built a feature-flagging product and tried to sell it. It was an easier version of LaunchDarkly. I ran into a problem: anyone small enough to adopt your technology doesn't care about feature flags, and anyone large enough to need feature flags needs so much scale that you have to build out all the infrastructure. I scrapped it.

**Jake [01:15:42]:** But what is old is new again. Companies are trying to move quickly, but you can't YOLO a vibe-coded thing straight into production. You need to say, "Here's my blast radius, my impact, and I want to shadow it for these users." Feature flags. You're going to need the tools larger companies built to maintain their structures. Everything gets compressed by 1,000x so everybody can build those structures quickly.

**Jake [01:16:07]:** That's exactly where we are: compressing the software development lifecycle, then expanding it and adding more new things.

## Cattle, Pets, and Clonable Infrastructure

**Swyx [01:16:15]:** Another term that comes to mind for newer developers is "cattle, not pets." People treat production like a pet. It has a name. You baby it and keep it alive. With cattle, you can mass farm, roll out, portion parts out, and kill them.

**Jake [01:16:37]:** I think that might change. You can move toward having pets as long as you have a cloning machine for your pets.

**Swyx [01:16:52]:** Yeah.

**Jake [01:16:52]:** If you can snapshot every single thing at every frame, it doesn't matter if something gets obliterated because you have a snapshot of it. The things we've built right now are designed to block changes from the hermetically sealed DevOps line. You have to write a Dockerfile because you need a specific cut of the file system.

**Jake [01:17:14]:** What if you had the whole file system? What if you snapshot it and lazily load the entire file system? Then you get around this problem entirely. You don't need the ceremony of Dockerfiles, Ansible scripts, or other things. You can iterate, snapshot, ask if it's the right loop or state, and then merge it into production. Merge the file system.

**Swyx [01:17:45]:** Why not?

**Jake [01:17:46]:** It's going to be fun.

**Swyx [01:17:47]:** This is a whole other can of worms, but if you cataloged the stateful things in a VM and developed dedicated solutions for each, you can cut the problem down a lot. It's surprising people weren't trying until now.

**Jake [01:18:04]:** It has always been surprising to me because these are the things we would work on. It's obvious.

**Swyx [01:18:11]:** At first principles, you need them. Everyone needs them in theory. Then the big clouds don't do them, so you assume it's impossible.

**Jake [01:18:18]:** Exactly. You think, "Meta has all the people writing eBPF code, and they're doing something with them." But you need that kind of work to solve these problems. Whatever is required, however deep we have to go, we'll go all the way down to the kernel's TCP/IP stack if needed. If we need to modify something to make it work for the mental model of the universe moving forward, we'll do it and keep going down.

**Swyx [01:18:52]:** That sounds fun.

**Jake [01:18:53]:** It's so much fun. I have to peel myself away from fun, interesting problems to make sure we can scale the company in a way that works. There are so many fun problems: getting information from customers to support to the person who built the thing internally, safe iteration, context from the dashboard to users, drilling down to the infrastructure layer, and managing orchestration as a real-time operating system versus a feedback control system. It's just so fun.

## Solo Founder Lessons: Obsession, Writing, and Focus

**Swyx [01:19:29]:** Speaking of the founder side, you're famously outside the YC/SF consensus. You go to YC, get a co-founder, and do all these things. You did none of that.

**Jake [01:19:40]:** None.

**Swyx [01:19:45]:** In the elevator you said a co-founder makes sense if one person is the tech person and the other is the biz dev person. But you have to contain those multitudes yourself. How do you do it?

**Jake [01:19:58]:** I try to get eight hours of sleep.

**Swyx [01:20:11]:** Is there a balance: 50/50, 30/30/30? What's the mental model as a solo founder?

**Jake [01:20:17]:** There's no balance. You have to think about all these things and be obsessed with them. Be obsessed with how people think about your product from a go-to-market perspective, and be obsessed with the kernel-level change that makes a user's SSH connection never drop. I want a universe where you can snapshot everything and it feels like iterating on a VM.

**Jake [01:20:47]:** You have to be obsessed at every layer of the stack. That's what makes it easier for me. Some people are obsessed with different portions of the company journey, and if you can segment those lines well and be clear about ownership, you'll have a good time.

**Jake [01:21:12]:** I said two is the worst number of co-founders because you have no tiebreak. You disagree, and how do you resolve it?

**Swyx [01:21:38]:** Usually someone is CEO, so they have the tiebreaker.

**Jake [01:21:43]:** Totally. It's hard every way you cut it. It's hard if you get help, and it's hard if you do it yourself. Running things is hard, but it's so rewarding and fun.

**Swyx [01:21:56]:** What have you found useful? A coach? Any advice that has been helpful?

**Jake [01:22:01]:** I like to write a lot. I get in trouble a lot for my Twitter. I once said if you're working weekends, you're messing up your planning. I've gone back and forth on that because right now we're at an extenuating time where it makes sense to work more. The goals are clear in my mind. If you have the vision and know where you're going, work harder to distill that vision and do those things.

**Jake [01:22:33]:** If you're not certain and need clarity, disconnect and take your weekends seriously. Write about where you are, what you want to do, where you want to go, and what problems you're solving.

**Jake [01:22:56]:** Writing is important. I don't love the word meditation, but whatever gets you into mental clarity is important when you're trying to say, "We're here and need to be here," or "We're here and I think we need to be in this general space for this to work."

**Jake [01:23:22]:** Disconnect, hang out with people you love, and work hard when you're working. I try to work sunup to sundown, Monday to Friday, all out. I disconnect on Saturday and come back Sunday afternoon to write, plan the week, and do everything else. It works well for me.

**Jake [01:23:43]:** Another hot take: most advice should be digested and thrown out the window. If it's helpful, it'll come back. You'll learn it through experience. We have made failure very expensive as a society, and it makes it difficult for people to walk off the paths.

## GPUs, Focus, and the Dominant Role of Agents

**Swyx [01:24:03]:** Anything you haven't tweeted and gotten in trouble with that you want to preview to the world?

**Jake [01:24:12]:** The agent stuff is crazy. It's going to be the dominant way people do pretty much everything, provided we can get the inference required for that to happen. Over the next 10 years, you'll see a fundamental shift in how people think about authoring the logic in their head.

**Swyx [01:24:36]:** One way of phrasing it is: if Allbirds can become a GPU provider, so can Railway.

**Jake [01:24:44]:** I think there's a lot of "everyone becomes a GPU provider" that is actually not becoming a GPU provider. You're defined more by the things you don't do than the things you do, because it's easy to say yes to a lot of things.

**Jake [01:24:56]:** Anthropic is amazing and moving into different zones. They're moving into Figma-like things.

**Swyx [01:25:09]:** As we're recording, Mike Krieger was on Figma's board, they removed him Monday, and then they launched this today.

**Jake [01:25:18]:** Things move fast right now. But agents are going to be the way people operate.

**Swyx [01:25:25]:** So your answer is focus: no GPUs for now, but never say never.

**Jake [01:25:27]:** Focus. We will not do GPUs now, but we 100% will do GPUs at some point in the future. That's not me leaking our roadmap because we don't have plans to do GPUs. It's just a function of needing FLOPS at some point. If you're fully vertically integrated and want to make it trivial for people to iterate, build, and deploy, you need access to this core piece of fundamental logic.

## A New Cloud From First Principles

**Swyx [01:25:57]:** Presumably your own data center traffic is a minority of your workload right now, but is there a point where it's a majority or you turn off public clouds?

**Jake [01:26:10]:** At some point, we got to 100% data center: our own data centers. Right now, the vast majority of what exists on our platform is on our bare-metal data centers.

**Swyx [01:26:21]:** So you're already there.

**Jake [01:26:23]:** Yeah. The transition was completed at some point, and then we grew so fast that we had to scale back on that. It got to 100% on the Datadog dashboard and then divoted back into the 90s because we were adding capacity.

**Swyx [01:26:45]:** You're literally building a new independent cloud, and people assume that could never happen post-AWS.

**Jake [01:26:53]:** It's hard. We're going to figure out a bunch of things to make sure the platform is deeply reliable. But you have to break ground on new things when you decide to build a cloud from scratch but not copy the hyperscalers.

**Jake [01:27:10]:** We've been deliberate about inventing our own infrastructure from scratch based on reading a ton of papers, while promising ourselves we wouldn't copy someone else's homework. If we copy someone else, we lose. You become them over time. You need a core thesis for why this business needs to exist now.

**Jake [01:27:33]:** For us, the activation energy required to deploy something in production on hyperscalers is far too high. We believe it should be instantaneous. There should be no friction between your thought and the reality that comes out and that you can share with friends. That's what we're building toward at every layer of the stack. If we have to go down to energy, we'll go down to energy.

**Jake [01:27:58]:** It matters for giving people access to this tooling. It's gated not just for citizen developers who are now vibe coding. You have multiple layers: citizen developer, front-end developer, back-end developer, DevOps person, and more. Those layers need to disappear so people can just ship.

**Swyx [01:28:20]:** Amazing. That's the future of cloud.

**Jake [01:28:22]:** Awesome. Thanks for coming on. Thank you for having me. It's been wonderful.

---

## [[AINews] Google I/O 2026: Gemini 3.5 Flash, Omni (NanoBanana for Video), Spark (background agents), and Antigravity 2.0](https://www.latent.space/p/ainews-google-io-2026-gemini-35-flash)
*🔬 Latent Space | 2026-05-20*

The [full keynote livestream](https://www.youtube.com/watch?v=wYSncx9zLIU&pp=ygUJZ29vZ2xlIGlv) was 2 hours, but as usual, The Verge has the best supercut down to 30 mins, which is very worthwhile to get a narrative sense:

The mainline Gemini 3.5 Flash is GA today (very nice compared to some staged rollouts) and is sold as a decent step up even compared to 3.1 Pro, with 3.5 Pro coming next month. Perhaps more impressive were the Gemini Live (Voice) and Omni (Video) and Google Pics/Flow (Images/VFX/music) modalities, where Google demonstrated industry leading capabilities and latency, all presumably made possible by industry leading hardware and models. 

Per longstanding tradition at every bigtech keynote these days, Google also showed off some smart glasses tech, which seems a little more likely to be seen on the street than many prior iterations from both Google and their peers.

[](https://substackcdn.com/image/fetch/$s_!haUt!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F904f7a4e-f945-40e0-b980-024fc220d0b7_1524x912.png)

> AI News for 5/18/2026-5/19/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

# **AI Twitter Recap**

**Google used I/O to reposition Gemini as both a consumer AI surface and a developer/agent platform, with three core technical announcements: Gemini 3.5 Flash for fast agentic/coding workloads, Gemini Omni for multimodal generation/editing starting with video, and a broader Antigravity agent stack spanning desktop/CLI/SDK/API.** Official posts emphasized scale -- Google says it now processes **over 3.2 quadrillion tokens/month** , up **7x YoY** from **480T/month** , while the Gemini app has **900M+ monthly users** and is available in **230+ countries and 70+ languages** ([Google](https://x.com/Google/status/2056783102085640252), [Google](https://x.com/Google/status/2056783643381543253), [GeminiApp](https://x.com/GeminiApp/status/2056799446684578250)). The most technically substantive release was **Gemini 3.5 Flash** , framed by Google as its strongest agentic/coding model yet, **GA immediately** , with **1M-token context** , **65k max output** , **4 thinking levels** ("minimal/low/medium/high"), and "thought preservation" across turns ([GoogleDeepMind](https://x.com/GoogleDeepMind/status/2056787987774816525), [Google](https://x.com/Google/status/2056788266872140232), [_philschmid](https://x.com/_philschmid/status/2056794978517750165)). Google paired that with **Gemini Omni** , a new family combining Gemini reasoning with generative media, initially via **Omni Flash** , capable of taking **text/image/video/audio inputs** and producing video edits/generation in Gemini, Flow, Shorts, and later APIs ([GoogleDeepMind](https://x.com/GoogleDeepMind/status/2056786446636212467), [Google](https://x.com/Google/status/2056786781992071172), [GeminiApp](https://x.com/GeminiApp/status/2056800579159216202)). Around those models, Google launched or expanded **Antigravity 2.0 desktop** , **CLI** , **SDK** , **Managed Agents in the Gemini API** , Search-native generative UI/coding, **Gemini Spark** background agents on cloud VMs, and a long list of Gemini-app/Workspace/commerce/media integrations ([Google](https://x.com/Google/status/2056789045548896516), [Google](https://x.com/Google/status/2056838495298367773), [Google](https://x.com/Google/status/2056791134295273554)).

## **Facts vs. opinions**

### **Facts / directly claimed by official or third-party benchmark sources**

  * Google says it now processes **3.2 quadrillion tokens/month** , up from **480 trillion** a year earlier ([Google](https://x.com/Google/status/2056783102085640252)).

  * Google says Gemini has **900M+ monthly users** ([Google](https://x.com/Google/status/2056783643381543253)).

  * Google says Gemini 3.5 Flash is **GA today** across Gemini app, Search AI Mode, Gemini API, AI Studio, Antigravity, Android Studio, and enterprise surfaces ([Google](https://x.com/Google/status/2056791527314387208), [GeminiApp](https://x.com/GeminiApp/status/2056789742910595342)).

  * Google says Gemini 3.5 Flash has **1M context** , **65k max output** , **4 thinking levels** , and "thought preservation" across turns ([ _philschmid](https://x.com/_philschmid/status/2056794978517750165)).

  * Google says 3.5 Flash beats Gemini 3.1 Pro on **Terminal-Bench 2.1** , **GDPval-AA** , and **MCP Atlas** ([GoogleDeepMind](https://x.com/GoogleDeepMind/status/2056787990110994511), [Google](https://x.com/Google/status/2056788281317306466)).

  * Google says 3.5 Flash runs **4x faster than comparable frontier models** , and **up to 12x faster in Antigravity** ([Google](https://x.com/Google/status/2056788266872140232), [JeffDean](https://x.com/JeffDean/status/2056793419033588091)).

  * Independent benchmarker Artificial Analysis reports Gemini 3.5 Flash scores **55** on its Intelligence Index, **+9 vs Gemini 3 Flash** , at **> 280 output tok/s**, with **MMMU-Pro 84%** , **GDPval-AA Elo 1656** , and pricing of **$1.50 / $9.00 per 1M input/output tokens** ; it also reports the model is **5.5x costlier** to run than Gemini 3 Flash on its suite and **75% costlier than Gemini 3.1 Pro** ([ArtificialAnlys](https://x.com/ArtificialAnlys/status/2056795055512596817)).

  * Arena reports Gemini 3.5 Flash reached **#9 overall in Text Arena** and **#9 in Code Arena: Frontend** , scoring **1507** , a **+70** jump over Gemini 3 Flash, and becoming the top score in its price tier ([arena](https://x.com/arena/status/2056793176720195693)).

  * Google says Gemini Omni Flash is available in Gemini/Flow today for paid users, in Shorts/Create starting this week for free, and via APIs in coming weeks ([Google](https://x.com/Google/status/2056789307856462061)).

  * Google says Spark runs on **dedicated Google Cloud virtual machines** , allowing long-running tasks while user devices are closed ([Google](https://x.com/Google/status/2056791134295273554)).

  * Google claims an Antigravity + Gemini 3.5 Flash demo built a functioning OS in **12 hours** using **93 parallel sub-agents** , **15k+ model requests** , **2.6B tokens** , and **< $1K** API credits ([Google](https://x.com/Google/status/2056789235500466273)).

  * Google says Search will use Antigravity + 3.5 Flash to generate **custom visual tools/simulations** on the fly ([Google](https://x.com/Google/status/2056795269694423065)).




### **Opinions / interpretations / skepticism**

  * Positive takes: "Google is back," "insane evals for a Flash model," "world model towards AGI," "mind blowing" for Search + Antigravity, etc. ([kimmonismus](https://x.com/kimmonismus/status/2056791681073316071), [Kseniase_](https://x.com/Kseniase_/status/2056798225378783656), [demishassabis](https://x.com/demishassabis/status/2056831486251380783)).

  * Neutral caution: some posters explicitly avoided overhyping due to **self-reported benchmarks** and noted pricing/perf concerns ([scaling01](https://x.com/scaling01/status/2056794370909593987), [simonw](https://x.com/simonw/status/2056867815605625172)).

  * Negative/skeptical takes focused on:

    * **Price inflation** relative to earlier Flash models ([enricoros](https://x.com/enricoros/status/2056816088785289481)).

    * Comparisons where **GPT-5.5-medium** may be smarter/cheaper/faster end-to-end ([scaling01](https://x.com/scaling01/status/2056803273756000721), [scaling01](https://x.com/scaling01/status/2056798645983334890)).

    * Benchmark caveats such as weak **TerminalBench-Hard** , mediocre **MRCR / ARC-AGI-2** , or not clearly beating Kimi/GLM on some slices ([scaling01](https://x.com/scaling01/status/2056796392899645919), [teortaxesTex](https://x.com/teortaxesTex/status/2056794752167645653), [scaling01](https://x.com/scaling01/status/2056795648742076743)).

    * Product naming/UX confusion around Gemini CLI vs Antigravity CLI and broader interface design criticism ([zachtratar](https://x.com/zachtratar/status/2056848643580482002), [kchonyc](https://x.com/kchonyc/status/2056826706984337726), [teortaxesTex](https://x.com/teortaxesTex/status/2056788641926509010)).




## **Gemini 3.5 Flash: the main technical release**

### **Official positioning**

Google/DeepMind repeatedly described **Gemini 3.5 Flash** as the company's strongest model yet for **agents and coding** , not its absolute flagship intelligence model. It's meant to sit on the high-speed, high-utility part of the Pareto frontier, powering both Google products and developer workloads ([GoogleDeepMind](https://x.com/GoogleDeepMind/status/2056787987774816525), [Google](https://x.com/Google/status/2056788266872140232), [SundarPichai](https://x.com/sundarpichai/status/2056796893951426705)).

### **Technical details and metrics**

From Google and affiliated posts:

  * **GA availability now** ([Google](https://x.com/Google/status/2056791527314387208))

  * **1M token context window**

  * **65k max output tokens**

  * **Thinking levels:** minimal, low, medium (**new default**), high

  * **Thought preservation across multi-turn conversations**

  * **Text output**

  * Input modalities: **text, image, video, speech** per Artificial Analysis ([ _philschmid](https://x.com/_philschmid/status/2056794978517750165), [ArtificialAnlys](https://x.com/ArtificialAnlys/status/2056795055512596817))

  * Pricing: **$1.50 / 1M input** , **$9.00 / 1M output** , **90% discount on cached input** ([scaling01](https://x.com/scaling01/status/2056793465715822720), [ArtificialAnlys](https://x.com/ArtificialAnlys/status/2056795055512596817))




Official benchmark claims:

  * **Terminal-Bench 2.1:** **76.2%**

  * **GDPval-AA:** **1656 Elo**

  * **MCP Atlas:** **83.6%**

  * Google-quoted multimodal result: **MMMU-Pro 83.6%** in one engineer post; Artificial Analysis reports **84%** , highest recorded on its setup ([koraykv](https://x.com/koraykv/status/2056795667088204234), [ArtificialAnlys](https://x.com/ArtificialAnlys/status/2056795055512596817))




Speed claims:

  * Google marketing claim: **4x faster than comparable frontier models** ([Google](https://x.com/Google/status/2056788266872140232))

  * In Antigravity, Google says it is **up to 12x faster** ([JeffDean](https://x.com/JeffDean/status/2056793419033588091), [scaling01](https://x.com/scaling01/status/2056790573961326680))

  * Artificial Analysis observed **> 280 output tok/s**

  * Some discussion cited **~867 tok/s** in Antigravity-specific optimized serving ([scaling01](https://x.com/scaling01/status/2056790573961326680), [scaling01](https://x.com/scaling01/status/2056791726677782743))




Third-party evaluation:

  * Artificial Analysis says 3.5 Flash is the **leader on the intelligence-vs-speed Pareto frontier** , but the economics are notably worse than prior Flash:

    * Intelligence Index **55**

    * **+9** over Gemini 3 Flash

    * Hallucination rate reduced to **61%** , a **31-point drop** vs Gemini 3 Flash on its omniscience setup

    * **GDPval-AA 1656 Elo**

    * **5.5x** costlier than Gemini 3 Flash to run on its benchmark suite

    * **75%** costlier than Gemini 3.1 Pro on the same suite ([ArtificialAnlys](https://x.com/ArtificialAnlys/status/2056795055512596817))




Arena:

  * **#9 Text Arena**

  * **#9 Code Arena: Frontend**

  * **1507** score, **+70** over Gemini-3 Flash

  * Better than Gemini 3.1 Pro across categories in its frontend coding eval ([arena](https://x.com/arena/status/2056793176720195693), [arena](https://x.com/arena/status/2056803661859479812))




### **Implications**

The notable shift is that Google appears to be using a "Flash" label for a model that, in prior cycles, would have been described more like a **high-end product model optimized for deployment** rather than simply a cheap lightweight tier. Several posters called this out directly, arguing Flash is becoming more expensive and possibly absorbing former Pro territory ([enricoros](https://x.com/enricoros/status/2056816088785289481), [simonw](https://x.com/simonw/status/2056867815605625172)).

The strongest technical signal is not "best absolute benchmark model," but:

  1. **material agentic gains**

  2. **extreme serving speed**

  3. **deep integration into product surfaces**

  4. **tooling built around subagents and long-horizon execution**




That makes 3.5 Flash strategically important even if some competitors still win on raw price-adjusted intelligence in certain third-party comparisons.

## **Gemini Omni: multimodal generation/editing as "create anything from any input"**

### **What Google announced**

Google introduced **Gemini Omni** as a new family merging Gemini reasoning/world knowledge with Google's generative media stack, starting with **video** creation and editing. Official messaging described it as "create anything from any input," but current rollout is narrower:

  * Inputs: **text, images, audio, video**

  * Initial output emphasis: **video**

  * Product availability: **Gemini app** , **Flow** , **YouTube Shorts/Create** , later **APIs**

  * Current shipping model: **Gemini Omni Flash** ([GoogleDeepMind](https://x.com/GoogleDeepMind/status/2056786446636212467), [Google](https://x.com/Google/status/2056786395067552140), [Google](https://x.com/Google/status/2056789307856462061))




Google/DeepMind claims:

  * Better **world understanding**

  * More robust **physics**

  * Multi-turn editing where scene/character consistency is retained

  * Ability to "reimagine" user video footage with conversational edits ([Google](https://x.com/Google/status/2056786888930062369), [Google](https://x.com/Google/status/2056786589175677089))




Rollout specifics:

  * Paid Gemini users globally in app/Flow "today"

  * YouTube Shorts/Create rolling out "starting this week" at no cost

  * APIs for developers/enterprise in coming weeks ([Google](https://x.com/Google/status/2056789307856462061), [GeminiApp](https://x.com/GeminiApp/status/2056814117047132301))




### **Perspectives**

  * Supportive: users and Google employees described Omni as a major quality step, especially for **video editing** and consistency ([joshwoodward](https://x.com/joshwoodward/status/2056827449556845051), [fofrAI](https://x.com/fofrAI/status/2056789242274259242), [osanseviero](https://x.com/osanseviero/status/2056863263305105424)).

  * Strategic interpretation: several posters framed Omni as evidence Google is investing in **world models** and embodied/physical priors, not just text/code competition ([demishassabis](https://x.com/demishassabis/status/2056831486251380783), [jparkerholder](https://x.com/jparkerholder/status/2056789448554062232), [kimmonismus](https://x.com/kimmonismus/status/2056802929957568881)).

  * Skepticism: some UI/output examples drew criticism for looking like "B-tier video game interface" or too polished/template-like ([teortaxesTex](https://x.com/teortaxesTex/status/2056787895977980172), [shlomifruchter](https://x.com/shlomifruchter/status/2056858151987884087)).




### **Context**

Omni matters less as "yet another video model" and more as Google's attempt to unify:

  * multimodal understanding,

  * media editing,

  * world grounding,

  * agent interfaces,

  * and eventually any-input/any-output generation.




This aligns with DeepMind's long-running world-model agenda and Google's product distribution advantage.

## **Antigravity: Google 's agent OS, not just a coding assistant**

A major underappreciated I/O theme was that Google is no longer presenting agents as a thin wrapper around a chat model. Antigravity is becoming the **execution substrate**.

### **What launched / expanded**

  * **Antigravity 2.0 desktop app** : agent-first desktop with core conversations, artifacts, multi-agent orchestration ([Google](https://x.com/Google/status/2056788868092006891), [Google](https://x.com/Google/status/2056838653855650286))

  * **Antigravity CLI** ([Google](https://x.com/Google/status/2056789045548896516), [Google](https://x.com/Google/status/2056841217611366570))

  * **Antigravity SDK** ([Google](https://x.com/Google/status/2056789045548896516))

  * **Managed Agents in Gemini API** : single API call gives an agent plus hosted Linux sandbox; supports Bash/Python/Node, files, browsing, custom markdown-defined skills, repo/GCS mounts ([Google](https://x.com/Google/status/2056838495298367773), [GoogleAIStudio](https://x.com/GoogleAIStudio/status/2056836824686059616), [_philschmid](https://x.com/_philschmid/status/2056836567470362955))

  * Integrations with **AI Studio** , **Android** , **Firebase** , **Workspace** , web ([Google](https://x.com/Google/status/2056789045548896516), [Google](https://x.com/Google/status/2056837910851449177))

  * One-click export from **AI Studio to Antigravity** ([Google](https://x.com/Google/status/2056838913944424469))

  * Native **Android app generation** in AI Studio / Android support in Antigravity ([Google](https://x.com/Google/status/2056838230591574098), [AndroidDev](https://x.com/AndroidDev/status/2056841786656711077))




### **Technical signaling**

Google's own demos centered on **parallel sub-agents** , **hosted execution** , **high-frequency iterative loops** , and **artifact-oriented workflows**. Jeff Dean explicitly described 3.5 Flash as a strong engine for "deploy sub-agents that collaborate, run high-frequency iterative loops, and solve real-world problems at scale" ([JeffDean](https://x.com/JeffDean/status/2056793419033588091)).

The marquee proof point:

  * OS built in **12h**

  * **93** parallel sub-agents

  * **15k+** requests

  * **2.6B** tokens

  * **< $1K** credits ([Google](https://x.com/Google/status/2056789235500466273))




Even if this is mostly a stage-managed benchmark/demo, it reveals the architecture Google wants developers to adopt: **many fast agents over one slow monolithic run**.

### **Reactions**

  * Positive: this is Google's answer to Codex/Claude Code/OpenClaw/Hermes-style workflows, with a stronger infra story ([iScienceLuvr](https://x.com/iScienceLuvr/status/2056792158988816767), [theo](https://x.com/theo/status/2056826014739890204)).

  * Critical: branding and product sprawl remain confusing; some users aren't sure whether they should use Gemini CLI or Antigravity CLI, and Google's design choices drew complaints ([kchonyc](https://x.com/kchonyc/status/2056826706984337726), [zachtratar](https://x.com/zachtratar/status/2056848643580482002), [teortaxesTex](https://x.com/teortaxesTex/status/2056788641926509010)).




## **Search, Gemini app, and consumer agents**

### **Search**

Google announced a redesigned AI-powered Search box, multimodal query support, and the most ambitious consumer-facing move: **Search generating custom visual tools and simulations on the fly** using Antigravity + Gemini 3.5 Flash ([Google](https://x.com/Google/status/2056793802141044786), [Google](https://x.com/Google/status/2056795269694423065)).

It also previewed **information agents** in Search:

  * persistent monitoring tasks

  * web/news/social/real-time signals

  * synthesized updates with links and actions

  * rolling out to Pro/Ultra this summer ([Google](https://x.com/Google/status/2056794282502054066), [Google](https://x.com/Google/status/2056794675214700764))




This is a notable strategic shift: Search moves from retrieval/ranking to **background agentic monitoring + generated applets**.

### **Gemini app**

Consumer Gemini updates included:

  * new "**Neural Expressive** " design language ([Google](https://x.com/Google/status/2056799862604046663))

  * inline/instant **Gemini Live** voice ([Google](https://x.com/Google/status/2056800029688352988))

  * **Daily Brief** personalized digest from inbox/calendar/tasks ([Google](https://x.com/Google/status/2056801159071883342), [GeminiApp](https://x.com/GeminiApp/status/2056800978343764238))

  * **Gemini Spark** as a 24/7 personal AI agent on cloud VMs, checking with users before major actions ([Google](https://x.com/Google/status/2056791134295273554), [GeminiApp](https://x.com/GeminiApp/status/2056801918018564538))

  * macOS app + upcoming Spark/voice desktop workflows ([Google](https://x.com/Google/status/2056802434303869118), [GeminiApp](https://x.com/GeminiApp/status/2056802363269329304))




### **Pricing / subscriptions**

Google introduced a new pricing ladder:

  * new **$100/month** plan

  * top-tier **Ultra cut from $250 to $200/month** ([Google](https://x.com/Google/status/2056792498287063370), [GeminiApp](https://x.com/GeminiApp/status/2056792679607103626))




This reads as a more aggressive bid for premium power users, especially coders and creators.

## **Trust, provenance, and standards**

Google pushed **SynthID** across Search, Gemini, Chrome, and hardware/media surfaces, and announced partnerships with **OpenAI, NVIDIA, Kakao, and ElevenLabs** to bring SynthID to their generated content ([Google](https://x.com/Google/status/2056787498676658576), [Google](https://x.com/Google/status/2056787749965799508)).

That is one of the more consequential standards moves from I/O:

  * it gives Google a shot at owning part of the provenance layer for generative media;

  * notably, OpenAI separately announced support for checking OpenAI-generated images via **SynthID watermark + C2PA credentials** ([OpenAI](https://x.com/OpenAI/status/2056793648571011232)).




This was less flashy than Omni/3.5 Flash, but likely more durable if provenance becomes mandatory infrastructure.

## **Google 's science and world-model angle**

Several I/O items reinforced that Google does not want to compete only on coding/chat:

  * **Gemini for Science** : Literature Insights, Hypothesis Generation, Computational Discovery ([GoogleDeepMind](https://x.com/GoogleDeepMind/status/2056808869242826957), [Google](https://x.com/Google/status/2056809034494124118))

  * **Nature** publication links around ERA / Co-Scientist ([GoogleResearch](https://x.com/GoogleResearch/status/2056797037426045105), [GoogleResearch](https://x.com/GoogleResearch/status/2056857494107062718))

  * **Project Genie + Street View grounding** , using ~20 years of maps imagery to create interactive real-location simulations ([Google](https://x.com/Google/status/2056850758029464009), [poolio](https://x.com/poolio/status/2056796361987850705), [bilawalsidhu](https://x.com/bilawalsidhu/status/2056804315721843024))




This broader context explains why some observers interpreted Omni as "world-model progress" rather than just a content tool ([demishassabis](https://x.com/demishassabis/status/2056831486251380783), [jparkerholder](https://x.com/jparkerholder/status/2056798252264018232)).

## **Different opinions**

### **Bullish / supportive**

  * Gemini 3.5 Flash viewed as a major leap for a speed-tier model, especially on agentic coding ([kimmonismus](https://x.com/kimmonismus/status/2056791681073316071), [SundarPichai](https://x.com/sundarpichai/status/2056796893951426705)).

  * Search + Antigravity seen as potentially transformative because Google can deploy generated UI/tools at enormous scale ([Kseniase_](https://x.com/Kseniase_/status/2056798225378783656), [TheTuringPost](https://x.com/TheTuringPost/status/2056795871098913209)).

  * Omni praised for editing quality and for hinting at a deeper world-model roadmap ([joshwoodward](https://x.com/joshwoodward/status/2056827449556845051), [kimmonismus](https://x.com/kimmonismus/status/2056802929957568881)).




### **Skeptical / opposing**

  * Concern that Google is leaning on **self-reported benchmarks** , and independent comparisons still leave room for competitors ([scaling01](https://x.com/scaling01/status/2056794370909593987)).

  * Concern that "Flash" is no longer cheap enough to justify the name; pricing has climbed sharply from prior Flash generations ([enricoros](https://x.com/enricoros/status/2056816088785289481), [simonw](https://x.com/simonw/status/2056867815605625172)).

  * Some believed **GPT-5.5-medium** still dominates on a combined smart/cheap/latency basis ([scaling01](https://x.com/scaling01/status/2056803273756000721)).

  * Some benchmark slices imply unevenness -- e.g. poor TerminalBench-Hard or middling reasoning metrics despite strong agentic numbers ([scaling01](https://x.com/scaling01/status/2056796392899645919), [teortaxesTex](https://x.com/teortaxesTex/status/2056794752167645653)).




### **Neutral / analytical**

  * Artificial Analysis gave the strongest balanced take: **excellent speed-intelligence frontier position** , **substantial agentic gains** , but materially **worse cost** than prior Flash and even higher than 3.1 Pro on their end-to-end suite ([ArtificialAnlys](https://x.com/ArtificialAnlys/status/2056795055512596817)).

  * Arena's data also supports a "real improvement, not just marketing" conclusion, especially for frontend/code tasks, without claiming category dominance ([arena](https://x.com/arena/status/2056793176720195693)).




## **Why this matters**

  1. **Google now has a coherent deployment story.**  
Earlier Gemini cycles often felt benchmark-heavy and product-fragmented. At I/O, Google tied model, infra, tools, APIs, consumer surfaces, and enterprise rollout together.

  2. **The center of gravity is shifting from chatbot UX to agent execution.**  
The important primitives were not just model IQ: they were **subagents, hosted sandboxes, long-running tasks, generated artifacts, and integration with Search/Workspace/Android**.

  3. **Gemini 3.5 Flash suggests "fast enough to orchestrate many agents" may matter more than max benchmark score.**  
For coding and tool use, throughput and latency are increasingly product-defining.

  4. **Omni reveals Google 's differentiation thesis.**  
Google is betting on multimodal/world-grounded systems rather than purely text-centric competition.

  5. **Trust/provenance is becoming platform infrastructure.**  
SynthID partnerships with OpenAI/NVIDIA/ElevenLabs/Kakao suggest some convergence around content-auth provenance layers.

  6. **The biggest unresolved question is economics.**  
Technically strong or not, 3.5 Flash drew substantial pushback on cost inflation. If "Flash" is no longer the cheap workhorse tier, Google may win on capability deployment while losing some developer mindshare on predictability and pricing simplicity.




**Talent, Labs, and Ecosystem Moves**

  * **Karpathy joins Anthropic** : The day's most engaged AI tweet was [Andrej Karpathy's announcement](https://x.com/karpathy/status/2056753169888334312) that he has **joined Anthropic** to "get back to R&D." The tweet dominated discussion, with subsequent speculation from [@scaling01](https://x.com/scaling01/status/2056773883982762114) citing Axios that he'll work on **RSI/autoresearch** and start a new pretraining-focused effort. While the details remain unconfirmed by Anthropic, the move was widely interpreted as a major talent win for Anthropic.

  * **OpenAI capacity products** : OpenAI announced **[Guaranteed Capacity](https://x.com/OpenAI/status/2056823271774101907)** , a commercial offering that lets customers secure **long-term compute access** for critical workloads. [Sam Altman](https://x.com/sama/status/2056827105401614656) framed it as a response to a world that will remain **capacity constrained** as models become more useful, offering **discounted tokens for 1 -3 year commits**.

  * **GitHub and coding toolchain integrations** : [GitHub](https://x.com/github/status/2056801675042779279) said **Gemini 3.5 Flash** is rolling out in **Copilot** , citing strong tool use, fast response times, and cache efficiency for iterative agentic coding. [Cursor](https://x.com/cursor_ai/status/2056803731367456993) launched integration with **Jira** , allowing cloud agents to take work items and create merge-ready PRs. [Code/VS Code](https://x.com/code/status/2056803208559759447) also announced Gemini 3.5 Flash availability.




**Training Algorithms, Benchmarks, and Agent Evaluation**

  * **RL/post-training discussion is shifting toward denser credit assignment** : [@nrehiew_](https://x.com/nrehiew_/status/2056751826356297834) argued that the next scalable training breakthrough may build on **GRPO** but with **denser, lower-bias credit assignment** , citing directions like **ECHO** , **Composer2** , self-distillation, and OPD. [@lateinteraction](https://x.com/lateinteraction/status/2056770702175318095) countered with a "pedagogical RL" framing: train a self-teacher that samples **correct and easy-to-follow** rollouts.

  * **Can coding agents do research? Not yet** : [Intology AI](https://x.com/IntologyAI/status/2056764236668493868) released **NanoGPT-Bench** , an autonomous benchmark based on the NanoGPT Speedrun competition, testing whether coding agents can contribute to real AI R&D progress. Their headline result: **Codex, Claude Code, and Autoresearch recover only 9.3% of human progress** , mostly via hyperparameter tuning rather than algorithmic innovation.

  * **Agent harnesses and memory are getting more formalized** : [@omarsar0](https://x.com/omarsar0/status/2056764334181884158) highlighted a 100+ page survey on **code-as-agent-harness** , arguing future systems need to be **executable, inspectable, stateful, and governed**. [François Chollet](https://x.com/fchollet/status/2056777649880752160) made the related point that real tasks are rarely Markovian, so agents without high-fidelity trajectory compression are dramatically less useful.

  * **Verifier quality is emerging as a bottleneck** : Threads from [@Shahules786](https://x.com/Shahules786/status/2056773476585816255) emphasized that scaling agent benchmarks now depends less on adding tasks and more on **improving verifier quality** , citing **SWE-bench Verified** , **OSWorld-Verified** , **ComputerRL** , and **BenchGuard**.




**Science, Biology Models, and Domain-Specific Systems**

  * **Hugging Face releases Carbon DNA models** : One of the most technically interesting open releases was **[Carbon](https://x.com/lvwerra/status/2056774820872831234)** , a family of generative DNA foundation models. The team says **Carbon-3B matches Evo2-7B while running 250 -275x faster at inference**, enough to process the whole human genome on a single GPU in under two days. The key recipe changes: **deterministic 6-mer tokenization** , a **factorized loss (FNS)** replacing plain cross-entropy late in training, and curated staged mixtures of functional DNA + mRNA data per [@LoubnaBenAllal1](https://x.com/LoubnaBenAllal1/status/2056771927570530475). The release includes **models, training code, evals, data, and a demo**.

  * **Google pushes AI for science as a product category** : Google introduced **[Gemini for Science](https://x.com/GoogleDeepMind/status/2056808869242826957)** , a suite of prototypes for researchers: **Literature Insights** (paper synthesis via NotebookLM), **Hypothesis Generation** (a Co-Scientist-style multi-agent "idea tournament"), and **Computational Discovery** (built with AlphaEvolve and ERA to generate and score thousands of code variants in parallel). Google Research also noted that **ERA** has now been published in **Nature** ([Google Research](https://x.com/GoogleResearch/status/2056797037426045105)).

  * **Specialized pretraining is gaining support** : [@pratyushmaini](https://x.com/pratyushmaini/status/2056780651219804582) pointed to evidence that **early exposure / specialized pretraining** improves robustness to forgetting, arguing that enterprises serious about domain use cases should consider **training custom models from scratch** , not just post-training.




**Safety, Governance, and Monitoring of Internal Agents**

  * **METR 's first Frontier Risk Report**: [METR](https://x.com/METR_Evals/status/2056800023149760666) published a major new report based on unusually deep access across **Anthropic, Google, Meta, and OpenAI** , including model CoTs and non-public information about capabilities, alignment, and control. The report focuses on whether labs could **lose control of their own internally deployed agents** and includes extensive appendices and transcripts ([METR](https://x.com/METR_Evals/status/2056800047258649049)).

  * **Monitoring internal agents is now an active practice** : [@idavidrein](https://x.com/idavidrein/status/2056800422422265897) described spending a month embedded at Anthropic stress-testing systems designed to detect whether internal AI agents could "go rogue." A key caveat he noted is that the exercise allowed Anthropic discretion to redact sensitive information, so he frames it as an **exercise rather than a formal audit**.

  * **New safety standards org** : [Steven Adler](https://x.com/sjgadler/status/2056762703033807068) announced **Guidelight** , a new AI safety standards organization co-founded with Page Hedley, releasing its first two standards. While the tweet thread in the dataset is partial, the move is notable as another sign of the field professionalizing around operational standards, not just model evals.




**Top tweets (by engagement)**

  * **Karpathy joins Anthropic** : [@karpathy](https://x.com/karpathy/status/2056753169888334312)

  * **Google introduces the Gemini 3.5 model series** : [@Google](https://x.com/Google/status/2056788000546386273)

  * **Google DeepMind launches Gemini Omni** : [@GoogleDeepMind](https://x.com/GoogleDeepMind/status/2056786446636212467)

  * **Gemini 3.5 Flash GA for agents and coding** : [@Google](https://x.com/Google/status/2056788266872140232)

  * **OpenAI Guaranteed Capacity** : [@OpenAI](https://x.com/OpenAI/status/2056823271774101907)

  * **Google 's 24/7 personal agent, Gemini Spark**: [@Google](https://x.com/Google/status/2056791134295273554)




* * *

# **AI Reddit Recap**

## **/r/LocalLlama + /r/localLLM Recap**

[ Read more ](https://www.latent.space/p/ainews-google-io-2026-gemini-35-flash)

---

## [[AINews] How to land a job at a frontier lab (on Pretraining)](https://www.latent.space/p/ainews-how-to-land-a-job-at-a-frontier)
*🔬 Latent Space | 2026-05-19*

It is the day before Google I/O, when the next major Gemini releases are expected to be previewed, and it will probably be a quiet week from competitors, though [Anthropic](https://news.ycombinator.com/item?id=48182281) and [OpenAI](https://news.ycombinator.com/item?id=48182754) both had minor wins today, and Cursor shipped their [first SpaceXAI model](https://news.ycombinator.com/item?id=48182516) with some nice detail on synthetic data/reward hacking and continued pretraining with [Muon](https://news.smol.ai/issues/25-07-11-kimi-k2). However the probable lasting title story candidate from today will be Vlad Feinberg's (understandably Google/TPU centric) [notes on job preparation, specifically on Pretraining](https://vladfeinberg.com/2026/05/10/how-to-land-a-job-at-a-frontier-lab.html):

[](https://substackcdn.com/image/fetch/$s_!W6LK!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F2e69d902-1d29-4e8c-834c-41e83b07223f_1194x604.png)

Specifically he references last year's [Scaling handbook from DeepMind](https://jax-ml.github.io/scaling-book/), and kernel work is an important part:

> _The biggest bottleneck and innermost loop of all LLM work is**performance work that makes abstract, logical changes to the LLM practical to run**. Every project needs people who can **tune the LLMs at the kernel level**. It is a skill you can pick up and is the most direct path into the labs._

There's a surprise mention of DSLs for kernel dev, of which there is a [concise history](https://x.com/yaroslavvb/status/2053669022684877076):

For someone at this level of the stack, surprisingly he also calls out Agent Work like [autoresearch](https://www.latent.space/p/ainews-ai-engineer-worlds-fair-autoresearch) and AlphaEvolve. He ends with a surprisingly simple exercise:

But the real hiring test is in the bottom paragraphs:

  * _Derive Chinchilla laws for this; see how they**differ for dense vs MoE** architectures. _

    * _Code your solution from scratch in jax by hand if you actually want the learning experience._

  * _Next, assuming you used jax.lax.ragged_dot for the MoE layer;**write a pallas kernel** that beats ragged dot for F > D by fusing the up/down projections. _

    * _Find a setting where you notice a measurable forward pass speedup and explain why it 's there._




If you can teach this to the rest of the community, we'd [love to feature you as a workshop speaker.](https://ai.engineer/cfp)

> AI News for 5/16/2026-5/18/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

# **AI Twitter Recap**

**Coding Agents, Agent Ops, and the Move from Chat to Automation**

  * **Agent infrastructure is converging on observability + automation loops** : Several posts point to a maturing stack for production agents. **LangSmith Engine** is framed as the missing CI/CD loop for agents, automatically detecting failures from production traces, clustering issues, and drafting fixes/evals, with LangChain also highlighting **SmithDB** as a purpose-built data layer for agent observability/eval workloads with low-latency querying over large traces and self-hosting/multi-cloud requirements [@krishdpi](https://x.com/krishdpi/status/2056102370434798034), [@LangChain](https://x.com/LangChain/status/2056414104445747371). In parallel, **Cognition** launched **Devin Auto-Triage** , positioning it as an always-on "first responder" for bugs, alerts, and incidents with long-term memory, manager/subagent structure, and PR generation; early users like Modal describe it as more useful than typical homegrown triage automations [@cognition](https://x.com/cognition/status/2056396941181727210), [@walden_yan](https://x.com/walden_yan/status/2056409599000068193), [@russelljkaplan](https://x.com/russelljkaplan/status/2056457452661719277). The common pattern is less "chat with an agent" and more **persistent automation tied to traces, memory, and evals**.

  * **Operational patterns for coding agents are getting more concrete** : Anthropic published best practices for running **Claude Code** across multi-million-line monorepos, legacy systems, and microservices, while adding **prompt cache diagnostics** and making **Fast mode default to Opus 4.7** for lower-latency coding workflows [@ClaudeDevs](https://x.com/ClaudeDevs/status/2056403446056784288), [@ClaudeDevs](https://x.com/ClaudeDevs/status/2056434422229123106), [@ClaudeDevs](https://x.com/ClaudeDevs/status/2056454359685476491). OpenAI expanded **Codex** workflows with a **Zoom plugin** , mobile/desktop remote execution, and "keep your Mac awake" support so longer-running jobs continue from the phone app [@coreyching](https://x.com/coreyching/status/2056422748763914274), [@OpenAIDevs](https://x.com/OpenAIDevs/status/2056442456800141424). Microsoft pushed **remote control** for GitHub Copilot CLI and VS Code to GA [@code](https://x.com/code/status/2056460035278962738). Across these, the product direction is clear: **background execution, remote supervision, and agent fan-out** , not just interactive completions.

  * **Practitioners are converging on the same mental model: constrain, verify, decompose** : François Chollet's framing of coding agents as "blind squirrels" that need carefully placed **verifiable constraints** succinctly matches a broader shift toward harness-centric engineering [@fchollet](https://x.com/fchollet/status/2056401102485266620). Related advice includes using **asserts** heavily in Python/ML code to fail fast [@gabriberton](https://x.com/gabriberton/status/2056381648707735875), building both **end-to-end and incremental evals** for long-running agents [@palashshah](https://x.com/palashshah/status/2056449711767265420), and structuring multi-agent systems in staged maturity levels rather than maximizing agent count prematurely [@shannholmberg](https://x.com/shannholmberg/status/2056410242330874349). The practical consensus: agent quality depends more on **verification surfaces, decomposition, and feedback loops** than on prompt cleverness alone.




**Model Releases, Ranking Shifts, and Frontier Coding Models**

  * **Cursor 's Composer 2.5 is the standout model launch in this batch**: Cursor announced **Composer 2.5** as its strongest model yet, emphasizing better sustained work on long-running tasks and more reliable instruction following, then disclosed a deeper strategic move: training a much larger model from scratch with **" SpaceXAI,"** using **10 × more total compute** and access to **Colossus 2 's million H100-equivalents** [@cursor_ai](https://x.com/cursor_ai/status/2056415413077233983), [@cursor_ai](https://x.com/cursor_ai/status/2056415419536461836). Community reactions centered on its **efficiency/cost-performance profile** and strong coding quality, with users calling it a major step up from Composer 2 and noting better collaboration behavior in messages/updates, not just raw benchmark gains [@mntruell](https://x.com/mntruell/status/2056418797473640681), [@jonas_nelle](https://x.com/jonas_nelle/status/2056422317740466192), [@kimmonismus](https://x.com/kimmonismus/status/2056494027189751842).

  * **Alibaba 's Qwen line continues to climb**: **Qwen3.7 Preview** landed on Arena with **Qwen3.7 Max Preview** at **#13 overall** in text, including **#7 Math** , **#9 Expert** , **#9 Software & IT**, and **#10 Coding** ; **Qwen3.7 Plus Preview** reached **#16 overall** in vision, making Alibaba the **#6 lab in text** and **#5 in vision** by Arena's counts [@arena](https://x.com/arena/status/2056400044862111757), [@Alibaba_Qwen](https://x.com/Alibaba_Qwen/status/2056403591464984753). That reinforces the broader trend of Chinese labs steadily improving across both general and specialist arenas rather than only headline chat benchmarks.

  * **Open model and multimodal releases continue below the mega-frontier** : ByteDance open-sourced **Lance** , described as a **unified multimodal model** for image/video understanding, generation, and editing, with **3B video + 3B image + 3B decoder** components [@bdsqlsz](https://x.com/bdsqlsz/status/2056353648779907115). Perplexity released a small open **multilingual ColBERT** model as a continued-training variant of **pplx-embed-0.6b** , with notes on using the **MaxSim kernel** [@bo_wangbo](https://x.com/bo_wangbo/status/2056421369387094301). These are not frontier-scale launches, but they are technically meaningful because they target **retrieval quality** and **native multimodal unification** , two areas where open tooling still matters.




**Inference, Deployment, and Local/Enterprise Serving**

  * **Local inference got a notable speed boost via MTP in llama.cpp** : Georgi Gerganov announced **MTP support for the Qwen3.6 family** in **llama.cpp** , calling it a significant milestone for local AI [@ggerganov](https://x.com/ggerganov/status/2056391115469689330). Follow-on reports showed meaningful throughput gains, including a **Qwen3.6-27B dense** jump from **25 tok/s to 45 tok/s (+78%)** on an A10G using draft-MTP flags [@victormustar](https://x.com/victormustar/status/2056456757786869793). This matters because it narrows the usability gap between local and hosted coding/general assistants on commodity hardware.

  * **Enterprise/on-prem deployment momentum remains strong** : Hugging Face and Dell promoted one-click access to models including **Kimi K2.6** , **DeepSeek V4 Pro/Flash** , **GLM 5.1** , and **MiniMax M2.7** through **Dell Enterprise Hub** optimized for **PowerEdge XE9780 with NVIDIA B300** [@jeffboudier](https://x.com/jeffboudier/status/2056436625522266265). Clement Delangue argued that **on-prem/local AI based on open-source models** will be an important answer to **GPU shortages** , with advantages in **cost, latency, and safety/data control** [@ClementDelangue](https://x.com/ClementDelangue/status/2056439359784530252).

  * **Cross-hardware inference optimization is becoming more sophisticated** : Zyphra published end-to-end inference benchmarks on **AMD Instinct MI355X** , claiming strong outperformance over AMD's baseline and a narrowed gap to **NVIDIA B200** when serving **Kimi K2.6, GLM 5.1, and DeepSeek V3.2** [@ZyphraAI](https://x.com/ZyphraAI/status/2056404622483562623). Complementing that, Quentin Anthony posted a useful thread on why benchmarking needs to distinguish **hardware ceilings vs current software state** , arguing that many cross-stack comparisons conflate vendor maxes, achievable GEMM performance, and software maturity [@QuentinAnthon15](https://x.com/QuentinAnthon15/status/2056450379932647533). For infra engineers, that's a strong reminder to treat benchmark charts as **stack-dependent snapshots** , not absolute truths.




**Research: MoEs, RL/Data Mixing, Architecture Search, and Agent Evaluation**

  * **Several papers this week focused on better training signals rather than bigger models** : A summary of LeCun/Timor et al.'s **" On Training in Imagination"** highlighted that in model-based RL, smoother world/reward models with **low Lipschitz constants** tighten error bounds; reward models often scale faster than dynamics models; and **many noisy reward labels can beat fewer high-quality ones** , while biased rewards are especially dangerous [@TheTuringPost](https://x.com/TheTuringPost/status/2056182805412098431). A separate thread on **Pedagogical RL** argued that even correct reasoning traces can be poor training data if they are too surprising relative to the student policy; the method uses a privileged teacher plus **spike-aware rewards** and **surprisal-gated imitation** to generate trajectories the student can actually learn from [@blc_16](https://x.com/blc_16/status/2056411251186815104), [@NoahZiems](https://x.com/NoahZiems/status/2056454054092419568).

  * **Architecture and scaling studies remain highly actionable** : Meta's **AIRA** work on **agentic neural architecture discovery** drew attention because it beats **Llama 3.2** at **350M, 1B, and 3B** scales within a **24-hour compute budget** by splitting search into a planning agent (**AIRA-Compose**) and an implementation agent (**AIRA-Design**) [@omarsar0](https://x.com/omarsar0/status/2056434731508703607), [@dair_ai](https://x.com/dair_ai/status/2056435283910865265). Separately, **" Slicing and Dicing MoEs"** reports training **2,000+ MoE LMs** and concludes that much of the design space reduces to **expert size and expert count** rather than the noisier discourse around MoE configuration knobs [@margs_li](https://x.com/margs_li/status/2056355079188627862).

  * **Data selection/eval methodology are emerging as first-class research problems** : **On-Policy Mix** targets the unsolved problem of finding the right data mix as data distributions keep shifting, with applicability across pretraining, midtraining, and instruction tuning [@michahu8](https://x.com/michahu8/status/2056393112621043964). On evals, Cameron Wolfe published a guide to **agent evaluation** , and a longer Zhihu summary argued that the agent era requires measuring **delegation intelligence** --when to search, code, reason, or call tools--rather than only static knowledge or internal chain-of-thought prowess [@cwolferesearch](https://x.com/cwolferesearch/status/2056399847553409301), [@ZhihuFrontier](https://x.com/ZhihuFrontier/status/2056408194801635391). That aligns closely with current product practice: the hard part is increasingly **tool choice and verification policy** , not text-only reasoning.




**Ecosystem Moves: SDKs, Revenue Capture, and Open Tooling**

  * **Anthropic acquired Stainless** : Anthropic announced the acquisition of **Stainless** , the SDK and MCP server platform that has powered Anthropic SDKs since early API days [@AnthropicAI](https://x.com/AnthropicAI/status/2056419620643541012). Strategically, this points to continued vertical integration around **developer ergonomics, SDK generation, and protocol surfaces** , not just model quality.

  * **Revenue concentration around foundation model providers appears to be increasing** : One post claimed that **Anthropic and OpenAI 's share of AI model/application revenues generated by 34 top AI startups is rising**, a signal that the ecosystem may be consolidating economically even as model choices proliferate [@amir](https://x.com/amir/status/2056041152500142259).

  * **Tooling and deployment curation remains in demand** : The Turing Post's roundup of **13 open-source tools for foundation model deployment** --including **vLLM, TGI, SGLang, llama.cpp, Ollama, BentoML, Kubeflow, MLflow** and others--was one of the more practically useful curation posts in the set [@TheTuringPost](https://x.com/TheTuringPost/status/2056102301811781848). Meanwhile, **Papers With Code** is being revived with AI-agent-assisted parsing of methods, leaderboards, and SOTA tracking, underscoring renewed focus on **research discoverability** [@NielsRogge](https://x.com/NielsRogge/status/2056366395605078252).




**Top Tweets (by engagement)**

  * **Cursor 's Composer 2.5 + bigger training push**: The highest-signal high-engagement product news was **Composer 2.5** and Cursor's disclosure that it is training a much larger model from scratch with **10 × more compute** [@cursor_ai](https://x.com/cursor_ai/status/2056415413077233983), [@cursor_ai](https://x.com/cursor_ai/status/2056415419536461836).

  * **OpenAI/Anthropic product updates with developer impact** : Sam Altman said **ChatGPT improved significantly with the latest update** [@sama](https://x.com/sama/status/2056435834333934051), while Anthropic shipped **Fast mode defaulting to Opus 4.7** and **prompt cache diagnostics** in Claude Console [@ClaudeDevs](https://x.com/ClaudeDevs/status/2056454359685476491), [@ClaudeDevs](https://x.com/ClaudeDevs/status/2056434422229123106).

  * **Enduring research/engineering framing** : Richard Sutton's 26-word condensation of the **Bitter Lesson** --focus on methods for creating knowledge that scale with compute, like search and learning--was among the most engaged research-adjacent posts and resonated with many of the week's themes around agent harnesses, search, and verifier-driven systems [@RichardSSutton](https://x.com/RichardSSutton/status/2056419165502935198).




* * *

# **AI Reddit Recap**

## **/r/LocalLlama + /r/localLLM Recap**

### **1\. LLM Safety Benchmarks and Abliteration Forensics**

[ Read more ](https://www.latent.space/p/ainews-how-to-land-a-job-at-a-frontier)

---

## [The Autonomous Drone Tech Stack & Economics of Drones — Yaroslav Azhnyuk, The Fourth Law & Guest Host Noah Smith, Noahpi…](https://www.latent.space/p/the-fourth-law)
*🔬 Latent Space | 2026-05-18*

The future of war has been evolving before our eyes in Ukraine, yet the west still plans to fight the last war. In this special episode, guest host **([@noahpinion](https://x.com/noahpinion))** and ****sit down with**Yaroslav Azhnyuk ([@YaroslavAzhnyuk](https://x.com/YaroslavAzhnyuk))**, a serial tech founder who went from building **[PetCube](https://petcube.com/)** to founding **[The Fourth Law](https://thefourthlaw.ai/)** , one of the world's most advanced AI-guided drone companies. Over two hours we cover the technology, tactics, and geopolitics of drone warfare, and why the modern battlefield has already left the West behind:

  * Yaroslav's personal history and the Ukraine war [00:01:04 - 00:14:01]

  * The modern drone tech stack: why FPV drones are the new god of war, the future of the rifleman, fiber optic vs. AI, five levels of autonomy, and the eight dimensions of the autonomous battlefield [00:14:01 - 01:05:13]

  * The geopolitics and economics of drones: China's manufacturing advantage, the drone race, Western defense readiness, countermeasures, and why the gap is widening [01:05:13 - 01:58:57]




For those looking for 's commentary, it really gets going around the 00:51:31 mark.

**Yaroslav Azhnyuk / The Fourth Law:**

  * X: <https://x.com/YaroslavAzhnyuk>

  * LinkedIn: <https://www.linkedin.com/in/yaroslavazhnyuk/>

  * The Fourth Law: <https://thefourthlaw.ai>




**Noah Smith** :

  * Substack: 



  * X: <https://x.com/noahpinion>




* * *

* * *

## Timestamps

00:00:00 Cold Open: China's 4 Billion Drones and the Cameras-to-Explosives Pipeline

00:01:04 Introduction: Brandon, Noah Smith, and Yaroslav Azhnyuk

00:05:41 From Tech Entrepreneur to Defense: PetCube, Brave One, and the D3 Fund

00:10:42 The Ethics of Building Weapons: Dual-Use Technology and the Wolf at the Door

00:14:01 The Tech Stack: Cameras, Autonomy Modules, Interceptors, and a Semiconductor Fab

00:18:47 Fiber Optic vs. AI: The Radio Horizon Problem and $32/km Cable

00:25:32 FPV Drones: The New God of War -- 70-80% of Frontline Casualties

00:28:28 The Five Levels of Drone Autonomy: From Terminal Guidance to Full Autonomy

00:41:37 The Eight Dimensions of the Autonomous Battlefield

00:45:32 AI Safety and the Morality of Autonomous Weapons

00:51:31 The End of the Rifleman? Noah's 2013 Prediction vs. Battlefield Reality

01:05:13 China's Manufacturing Advantage and Western Vulnerabilities

01:24:21 Policy Advice for Western Defense: Defense Valley and the Widening Gap

01:32:54 The Drone Race: Who's Ahead, Category by Category

01:41:57 Countermeasures: Shotguns, Jammers, Lasers, and Fishnets

01:58:19 The Wedding and Final Takeaway: Be Prepared for War

* * *

# Transcript

## Cold Open: China, FPV Drones, and the New Warning Sign

**Yaroslav [00:00:00]:** Think about this. Last year, Ukraine produced 4 million FPV drones. Ukraine is not the most industrious nation in the world. China can produce 4 billion of these FPV drones.

**Noah [00:00:10]:** Would you say that right now China is now the supreme conventional military power on Earth, given its ability to manufacture and deploy drones in the quantity and quality that you just described?

**Yaroslav [00:00:20]:** I don't think we have all the information to claim that but we cannot count it out, and that alone should be a big warning sign. As I say, at some point in my life I went from making cameras that fling treats to pets to cameras that fling explosives to the occupiers. So that's the short story. And when you think about what your nation, what your patriots are going through, you realize that's the only morally right thing to do is to fight back, and it is immoral not to fight back, and then the choice becomes very clear.

## Introduction: Yaroslav Azhnyuk, Petcube, and the Last Flight into Kyiv

**Brandon [00:01:04]:** Welcome to Latent Space. I'm Brandon. I normally do science podcasts, but today we're going to do something a little bit different. I'm joined by Noah Smith of Noahpinion on Substack and Twitter. And he has lots of interesting things to say about drones. And as a guest, we have Yaroslav Azhnyuk, founder of The Fourth Law and several other, drone-related startups. To get started, it is February 23rd, 2022. You are running a pet startup. You're connecting pets with their owners. Let's go in just a little bit of background. How did you get started in tech, and what were you working on before the Ukrainian war started?

**Yaroslav [00:01:50]:** Good to be here. Thank you. On February 23rd, late in the evening, 11:00 PM Kyiv time, my wife and I landed in Kyiv. Actually, then she was a fiance. We came from Lviv, where we were looking at a church, where our wedding should have taken place. And we got into this cab ride from the airport to our home, and the driver was like, "You crazy. Like, everyone's leaving Kyiv. Why do you come?" We're like, "What? Nothing's going to happen. Dude, chill." And then obviously, eight minutes later, or eight hours later, the bombs fell in the city. It was quite surreal. We probably landed on the last flight that landed in Kyiv, or one of those last flights. My background, I'm a tech guy. Studied applied mathematics in Kyiv Polytechnics, born and raised in Kyiv. My parents are old PhDs from academia, and grandparents too. Like, everything, from linguistics to nuclear physics. And I'm an entrepreneur, so I've built a bunch of companies. Petcube is the one you were referencing. So I lived in San Francisco 2014 to 2020, building Petcube, which is one of the leading, pet device companies in the world, selling lots of pet cameras. And then, yeah, as I say, at some point in my life I went from making cameras that fling treats to pets to cameras that fling explosives to the occupiers. So that's the short story.

## February 24th: Leaving Kyiv as the Invasion Begins

**Noah [00:03:28]:** February 24th, I guess a few hours after you, go to check out your wedding chapel, what do you do?

**Yaroslav [00:03:37]:** We had a plan for this situation. So my parents and family live in Kyiv, and we're like, "Okay, this has actually started. The worst has, come true." And so we basically packed our belongings and got in the car and spent 17 hours driving west. And that was pretty sure most people in our audience watched at least one apocalyptic movie in their life, so that was exactly like that. Like, felt exactly like that. Missiles are falling. Like, there was smoke in Kyiv. Like, my dad and I went, like, to central part of the cities. It's probably, like

**Yaroslav [00:04:20]:** 800 meters from presidential office, to pick some stuff up at his workplace. Because he's, like, the head of an academic institution, so he had to get some of the things with him. And super surreal. Like, the streets are empty. Like, the gas stations are out of gas. Like, we found some gas station. We didn't have, like, spare canisters with us, so we're like, We figured out, like, the car was diesel, so like, we figured out, if it's diesel, you can actually store it in plastic, canisters, and we bought some window wash for the cars. We poured it out of the canisters, and we poured the diesel into that. Yeah, so it was like that. And then, like, helping friends get out, like my friend and his dog. Like, we found Like, my brother was also, like, riding in a separate car. We found a place for my friend who didn't have a car. It was like, yeah, it was like, totally surreal. And we didn't know of course, and you didn't know this will last for so long. You didn't know whether Ukraine will be able to defend Kyiv. And it was like, yeah, very little information and very little insight into future.

## From Pet Cameras to Defense Tech: Building for Ukraine and the Free World

**Noah [00:05:42]:** What are your thoughts with regards to how do you, defend, Ukraine? So you eventually start building drones Like, what is the process to get from there from where you were building, devices that connect owners with pets to building drones, and what other things did you do to help the war effort in the process?

**Yaroslav [00:06:07]:** It's definitely non-trivial, right? Like, I didn't go, to I didn't get any, like, military education when I was a student. Like, normally, in Ukraine, you would, you would go to like, this military school even if you're getting higher education in any other, sphere. I decided to skip that which is like, an unusual way to go. And I never thought that I will be somehow engaged in a war effort. Like, what is war? Of course, wars are over. It's the end of history. So one thing you got to understand about, like, many Ukrainians and like, I guess, it's also true about most of the people I met here in the US, that your who you are in terms of your nationality is a big part of your identity. So when that gets under attack, it's something deeper than just the country you live in gets under attack, right? And I Day one, I figured I'm going to I'm going to fight back with everything I can, right? But I didn't think on day one that I'm actually going to do, weapons. And a bunch of things. We were reaching out to a number of American, congresspeople and senators, and basically advocating for support of Ukraine, for voting for lend lease, which has happened in May 2022, but didn't actually work as expected. We helped start, Brave One, which is now a very important defense innovation cluster, sort of like a DIU here in the US. We helped start, a fund called D3. It's like, it was started or co-started by Eric Schmidt, former CEO of Google. So a bunch of these odd things, but then eventually I was like, "Okay,"by 2023 it was obvious this thing, A is going to last a lot more time, and B, that the whole world is shifting and that there's going to be a new arms race, that the warfare is redefined by drones as platforms. And for the first time in history, you have a platform that is software defined, that can increase your battlefield capabilities, in a in a step change just overnight. So it's like if you were able to push a software update and get all of your Roman legionnaires a new helmet? That has never been possible before. It's the first time in the history of war this is possible. So all of that and many other things like, supply chain fragilization, and the impact that AI is going to have on all of this all these things have become evident to me in 2023, and it's like, "Okay, I should do what I do best, or what I know how to do best, start a tech company, and sort of leverage the global techno capitalist machine, to provide, defensibility to Ukraine and the free world." So that's literally the mission of the company, increase defensibility of Ukraine and the free world. And then there was some sort of soul-searching and like, asking yourself. It's like, "Okay, am I Actually, I know nothing about weapons. Am I actually, like, ready to make, things that other people use to kill other bad people?"

**Yaroslav [00:09:36]:** When you think about what your nation, what your Compatriots are going through And think about all the terror of places like Bucha, the occupied cities in the east and south, the abducted children, the raped women, all the economic damage that's being done, and the intention to destroy a whole nation, to genocide the people of Ukraine, you realize that's the only morally right thing to do is to fight back, and it is immoral not to fight back. And then the choice becomes very clear. And look, we're just passing the ammunition. We're not doing the actual job. The actual fighters and defenders and heroes are people in the armed forces. We're just support.

## The Moral Question: Weapons, Responsibility, and Fighting Back

**Noah [00:10:33]:** I have so many questions. Actually, I know you seem to have a question. Do you want to ask anything?

**Yaroslav [00:10:38]:** No, I'm just listening. Go ahead.

**Noah [00:10:40]:** I do want to talk about, some of let's say, the moral issues, like you just said. You end

**Yaroslav [00:10:50]:** I think there are no issues there.

**Yaroslav [00:10:52]:** What would an example of a moral question be in this case?

**Noah [00:10:55]:** No, I mean Okay. As you just said, you are creating the tools, but others are using them.

**Noah [00:11:05]:** I was maybe thinking of having this conversation later, but one of the questions is like, is it actually you are going to be building them for your homeland, which you are building it for your homeland, which is I think, very a strong morally defensible position, but this technology is not going to stay with you, right?

**Noah [00:11:26]:** This you will probably be selling these to other people Yeah. So the future is really where the moral issues may come into play

**Yaroslav [00:11:38]:** The this question becomes, easier and more complete if we ask this not about a particular technology or particular weapon, if we think that this question actually applies to any kind of technology Right? So -Knife or fire. You can use knife to do surgery and save people's lives, or you can use it as a weapon to take people's lives.

**Noah [00:12:06]:** Cut tomatoes, too.

**Yaroslav [00:12:08]:** Cut tomatoes too.

**Noah [00:12:09]:** Yes, knife.

**Yaroslav [00:12:09]:** That's helpful.

**Noah [00:12:10]:** In Japan, sword and knife, they, call the same word.

**Yaroslav [00:12:14]:** It's like, it's with any technology. Large language models, right? Look at how powerful they are and yet they're available to anyone in North Korea or in Russia.

**Yaroslav [00:12:29]:** That's one side of the argument. The other side is As a maker, what is your responsibility for how the tools you're creating, will be used? There's definitely some responsibility, right? Then How should the decision process look like? Should you, like, try to calculate all the possible scenarios before starting to work on something? Or do you create something that is needed now to save people's lives, and then think about, addressing the unwanted edge cases later? In ideal world where there's like, or okay, it's not ideal world. In a mythical world where there is some one governing party and it gets to decide everything, and there is no other country, that can, decide on their own, you could say, "Well, we need to calculate for all the consequences, and only then, maybe build this building, by replacing this park because, maybe we need this park in the city,"right? So that kind of situation. But when you're in a situation where you're in a forest, in front of a wolf, you first going to deal with the wolf that wants to eat you, and then you're going to go consult Greenpeace. So that's kind of situation that Ukraine is in.

## The Fourth Law, Odd Systems, and Ukraine's Drone Stack

**Noah [00:13:59]:** Enough. Because this is a tech podcast, I did want to spend some time talking about, sort of the tech in that you've developed and what you've been working on. So can you explain, I guess, first of all, like, the problem that you were trying to solve from a technical standpoint? And I think, and then maybe, like, go into some of the solutions and some of the design process that led you from designing, little laser-guided, guiding lasers with a with an iPhone versus Having drones.

**Yaroslav [00:14:34]:** Like, it so happened, that my partners and I, we sort of So I started one company called The Fourth Law, and its goal was and is to Make, massively scalable on-drone autonomy. And then In parallel with that together with my, Petcube co-founders, partners, and friends, we started another company called Odd Systems Which, was focused on making thermal cameras. Cameras, thermal cameras are seeing thermal radiation and are used to see at night. And we're now sort of those companies are getting closer and closer together and we're probably going to merge them. And this group of companies is currently the leading, team in on-drone AI and thermal imaging on the Ukrainian battlefield, and Likely one of the leading, if not the leading in the world. So We have these, like, three sort of business units, which are cameras, drone autonomy, and drones. So the cameras and drone autonomy sell daytime and nighttime cameras and different types of drone autonomous modules to other drone manufacturers, over 200 drone manufacturers in Ukraine. And then the UAV, business unit sells the drones themselves to the armed forces of Ukraine, Ukrainian government. And there are different types of drones. Those are sort of front strike, as we call them, so those are sort of FPV strike drones and the bombers, and then interceptors. And there are different kinds of interceptors. We do Shahed interceptors and we do ISR interceptors. We don't do the deep strike-

## FPV Drones, Interceptors, and Battery-Powered Warfare

**Noah [00:16:32]:** What's an ISR interceptor?

**Yaroslav [00:16:33]:** ISR is stands for intelligence, surveillance, reconnaissance, and those are basically drones which are which, Russians are using to watch over positions and then communicate where, the targets are coming.

**Noah [00:16:48]:** It's a reconnaissance.

**Yaroslav [00:16:48]:** That's, the ISR is sort of a classical term for a for a reconnaissance drone.

**Noah [00:16:53]:** Are all of these battery-powered drones that you just described? 'Cause I know that the sort of deep strike drones still have, like Some sort of

**Yaroslav [00:17:01]:** Internal combustion engine?

**Noah [00:17:02]:** Internal combustion engine. Are all the things you're talking about battery-powered?

**Yaroslav [00:17:06]:** What we're working on is all battery-powered, right? We don't do the deep strikes, right? And then in terms of autonomy-

**Noah [00:17:12]:** You can catch a Shahed with a battery-powered thing. It's not Fast to catch.

**Yaroslav [00:17:17]:** No, absolutely. Look, Shahed interceptor, like ours, it's called Zero, it goes up to 326 kilometers per hour.

**Noah [00:17:26]:** For reference, how fast is a Shahed?

**Yaroslav [00:17:28]:** Eight, like, in internal phase it could be 280, but in cruise phase it's, like, 220-ish.

**Yaroslav [00:17:36]:** Yeah. And sorry, I'm not like you can convert that into miles if you're interested.

**Noah [00:17:41]:** No, that's fine.

**Noah [00:17:41]:** Multiply by two thirds or point six or something.

**Yaroslav [00:17:44]:** That's easy. Yeah, I was saying that for autonomy modules, right, we, -We make systems, autonomous systems for frontline, for interceptors and some for deep strikes as well, and then different levels of autonomy. So from terminal guidance, which is like lasts 500 meters, give or take, to autonomous bombing, to autonomous target detection, to autonomous navigation and all of that across day and night, different terrains, different time of the year, different platforms like quadcopters and fixed wing, and maybe some other platforms. So it's quite a wide variety of products. We also have like our own simulation. We have our own training school for the war fighters. And we're about to start construction of two, semiconductor plants to make, sensors for thermal cameras. So that's super exciting for me as a computer science guy is Doing semiconductors. Super cool.

**Noah [00:18:49]:** Like in terms of kind of core drone technologies, you basically are one is an FPV replacement without fiber optics, and the other is

**Yaroslav [00:18:59]:** You

**Noah [00:18:59]:** Signal tracking with interceptors

**Yaroslav [00:19:00]:** With or without fiber optics. Fiber optics Is just like, sort of a communication module.

**Yaroslav [00:19:05]:** You can, you can use classical analog, video link and radio link. Those would be two separate radios. You can do digital, or you can do fiber optic, and then fiber optic Has its own advantages but also adds weight and decreases, the distance and decreases, how fast you can, sort of turn and With a drone. Yeah.

**Noah [00:19:33]:** Do you need AI for fiber optic drones?

**Yaroslav [00:19:36]:** Like you can use AI for fiber optic drones. AI replaces a human, right? Fiber optic is making your communication link more resilient. So those are slightly different goals. Like if you want, you can have, AI controlling hundreds of fiber optic drones instead of having 100 operators for each.

## Fiber Optics, Radio Horizons, and Terminal Guidance

**Noah [00:20:03]:** I guess I thought that the key reason that people moved to fiber optic drones was for like electronic, countermeasures. Or I guess to counter those.

**Yaroslav [00:20:13]:** I think that's a correct assessment from sort of a public awareness standpoint. In practice it's somewhat more difficult Because besides electronic countermeasures, you have these issues of a radio horizon For FPV drones, which means that as

**Yaroslav [00:20:36]:** I believe Earth is round Some people disagree. But basically if you fly a drone and you have a land station over here and a drone flying over here

**Yaroslav [00:20:49]:** If your drone is flying high, you have good direct radio visibility. If your drone goes low, and usually, Russian infantry and vehicles, they're on the ground and you want to hit them, you need to go low. Lower you go, maybe you'll get behind a hill or behind a forest, and if you're far enough, you'll just get behind the curvature of the earth. You get into what's called a radio shadow. And then That is a real bummer because for the last, be it 60 or 20 meters, you won't be able to see anything and it will be very difficult to hit the target. So to counter that what-- And then the distances that these FPV drones, act on they're, they can be quite large. So for example, here in the US there was this drone dominance program competition, and in drone dominance the furthest distance was about 10 kilometers.

**Noah [00:21:44]:** What was drone dominance? What was that competition?

**Yaroslav [00:21:47]:** Drone, the drone dominance is a is a program started, by the US government, to accelerate the development of drone technology here in the US.

**Noah [00:21:57]:** Got it. And the longest range thing they were using was 10 kilometers.

**Yaroslav [00:22:00]:** Was 10 kilometers, right. In Ukraine, like if your drone doesn't fly at least 20, 25, it just, no one's interested in it, and the usual hits are happening. It was like, okay, many hits are happening between 30 and 40 kilometers, and that's what expected from a regular 10-inch, FPV drone. So at that distance, even at altitudes of like 60 to 100 meters, you might start losing, the link. So some of the earlier AI technology that was fielded in FPV drone was this terminal guidance technology. That was the first product that we ever, launched that helped you as an operator, once you see the target from two, three, 500 meters, you lock onto the target and then, it just, drives the drone towards the target no matter what, even after you lost the visual connection. So optic fiber solves that. However, if you want to go like 20 kilometers with optic fiber, that will add an extra three kilos, of useful weight to your drone. So

**Noah [00:23:12]:** 'Cause the cable that you have to unspool as you go weighs.

**Noah [00:23:15]:** It is heavy.

**Yaroslav [00:23:15]:** At first, like the spool is about 800 grams, so a bit less than a kilo, and then, and then think about 10, 10 kilometer optic fiber is another kilo, something like that. That takes away from your useful mass and then now you have like, you need a 15-inch drone and it can only carry maybe one or two kilos of explosives if you want to go, 20 kilometers. If you want to go to 30 or 40, like 30 is probably max. 40 is like very problem problematic on optic fiber. And then the problem with optic fiber is it's actually getting super expensive. So and why? Because of all the data centers for AI. That's literally the same optic fiber-

**Noah [00:24:01]:** We're running out of centers

**Yaroslav [00:24:02]:** That's being used there.

**Yaroslav [00:24:02]:** Like when Ukrainians and Russians come to Chinese factories to buy the optic fiber, they're like, "We're out. We sold it out to the Americans."? That's the craziest thing. So optic fiber went up in price from like, $4 per, kilometer to like, $32 per kilometer in a few months in the beginning of this year. And I've

**Brandon [00:24:26]:** Claude Code is stopping the Russian drone effort here.

**Yaroslav [00:24:30]:** Ukrainian as well. Yeah.

**Brandon [00:24:31]:** Ukrainian. But I read somewhere that the Russians had grown more dependent on fiber optic drones relative to the Ukrainians, and that's one reason why the Ukrainians have sort of regained the initiative in drones recently.

**Brandon [00:24:42]:** How accurate's that?

**Yaroslav [00:24:43]:** The Russians were the first ones to scale that. I think by as of now, Ukraine has caught up. I think, like, as of maybe three months ago, Ukraine is mostly caught up on fiber optic. Yeah.

**Brandon [00:24:57]:** What percent of damage would you say is in terms of FPV drone damage would you say is now fiber optic versus, like autonomous?

## FPVs as the New God of War: Tanks, Artillery, and Cost per Kill

**Yaroslav [00:25:07]:** For our, for our audience, I actually, I cannot answer that question. Like, it's like I know the answer, but I would not disclose that. But for our audience, I think another interesting fact is out of all the casualties on the front line Between 70 and 80% are done by FPV drones.

**Brandon [00:25:30]:** FPV drones are the new weapon of universal weapon of warfare.

**Yaroslav [00:25:34]:** It's

**Brandon [00:25:35]:** Land warfare, anyway

**Yaroslav [00:25:35]:** They used to say that artillery is a god of war because artillery used to cause, like 80% of casualties, and now On that ranking-

**Brandon [00:25:46]:** FPV

**Yaroslav [00:25:47]:** FPV drones rule.

**Brandon [00:25:48]:** FPV drones are the god of war.

**Yaroslav [00:25:51]:** Sort of. Dethroned artillery. But it's not to say that artillery is not useful, is not needed. Like, all of these systems are needed. Maybe except cavalry, although Russians still use it. I know, have you seen the videos of Russians using mules and horses?

**Brandon [00:26:09]:** What is the usefulness-

**Yaroslav [00:26:10]:** It'

**Brandon [00:26:10]:** Of a tank in the in the modern-

**Yaroslav [00:26:11]:** That's where we need Greenpeace to say a word, but they're silent. Yeah.

**Brandon [00:26:15]:** What's the use of a tank on the modern battlefield?

**Yaroslav [00:26:21]:** It's diminishing.

**Brandon [00:26:22]:** Diminishing.

**Yaroslav [00:26:22]:** However, I think there might be technologies which will, revive the tank. Look, tank still provides you armor, and armor is important. Like, you still need to armor and firepower, right? Like, you can be an armor personal carrier that provides you, armor. The challenge that currently exists is armor is not very well protected against incoming drones. However, there are ways to do to protect it. We were previously talking about this before the podcast. The CEO of Rheinmetall, recently sort of ridiculed, Ukrainian drone industry, saying that like, there is nothing interesting there, no real innovation, no to stand Compared to like, Rheinmetall or Boeing, and it's all made by housewives. There was like, obviously a ton of memes about this people ridiculing the CEO of Rheinmetall. And one of the best quotes, I heard on this topic is from my friend, Alexey Babenko, who's, the head of and founder of VIARI Drone, which is one of the largest manufacturers of FPV drones. They're our partner. They're using our autonomy. So he said that the drones we manufacture in one day will be more than enough to destroy all the tanks Rheinmetall manufactures in a year.

**Yaroslav [00:27:52]:** Then, yeah, cost-wise, of course, a drone is like, $500 and a Rheinmetall tank is what, probably 5 million-ish or maybe more.

**Brandon [00:28:00]:** Don't mess with those housewives.

**Yaroslav [00:28:03]:** Drone wives.

**Brandon [00:28:04]:** Drone wives.

**Yaroslav [00:28:06]:** That's it.

**Noah [00:28:06]:** There's a classic saying that everyone always fights the last war.

**Noah [00:28:12]:** Yet do How did So from your standpoint, how did we get to the point where tanks became irrelevant in at least for now In a matter of just a few years?

**Yaroslav [00:28:24]:** Look, I think it's the same way, how do we get to the point that calculators become irrelevant?

**Yaroslav [00:28:31]:** Now we have iPhones. Like, why would you need a calculator? Technology progresses and its influence grows non-linearly. It's all exponential. So I can tell you that full autonomy, when you put it on a drone Look, so if you, if you think about a tank and a like, it's not a direct comparison, but even, like, a drone and a artillery shell or like, sort of cost per kill, an artillery shell for 155 caliber, which is a standard NATO caliber Currently market price is about $4,000 per piece. So compare that to say, $400 per drone. That's 10 times more expensive. Account for the amortization of the artillery gun and for how vulnerable it is and what is the sort of tactical, capabilities it gives you as compared to a drone. You'll figure out that an FPV drone is maybe three orders of magnitude, more versatile, more useful, more capable than artillery and many of than a classic artillery. Many of Because there are different types of artillery. Not just, like, one 155. You have mortars, you have all that. But give or take, roughly three orders of magnitude maybe. Again, it doesn't have that firepower. It's not one-to-one comparison still.

**Yaroslav [00:29:53]:** Now, take that FPV drone. When you put full autonomy on that FPV drone, which can be not very expensive, like systems that we're, producing are like, in hundreds of dollars of pure bomb

## Full Autonomy: From Human Pilots to Smartphone-Directed Drone Missions

**Noah [00:30:06]:** Just interrupt. You said full autonomy Just a second ago you were saying that the autonomy here is guidance, right? It's not decision-making.

**Yaroslav [00:30:14]:** No, I was I was saying that's the f-First and sort of easiest pieces of autonomy that was fielded by us. But if you, if you add full autonomy to a drone

**Brandon [00:30:24]:** He, I think he's asking what does it can you, for the listeners, can you explain What the term full autonomy means?

**Yaroslav [00:30:29]:** Basically, I think a good way to think about an FPV drone is like an iPhone of warfare. It's, like, very inexpensive, very mass producible, very versatile. You don't need a bunch of other things when you have a iPhone in your pocket. You don't have, need an MP3 player, you don't need a calculator, don't need other things. All right? So FPV drone is an iPhone. Or like, okay, Apple please don't sue me, is a smartphone. And then, when you add autonomy to it sort of becomes like Uber or ride sharing. Okay? So what it means is instead of actually being a trained pilot who has this complex remote controller device which requires a couple months of training to actually pilot the drone, and then having to pilot it for 30 minutes, flying towards the target, et cetera, et cetera, now you basically, you have your smartphone, you have a drone, you pick your smartphone, you say, "We are here. The bad guys are here. Go and get them." And the drone goes up, flies in a given direction, localizes itself on the map, finds the dedicated area where they, the bad guys are supposed to be sees the bad guys, bombs them, return, like, watches, so does a damage assessment, returns back, sits down, and then you can pick it up and watch the video if you didn't have the radio link, right?

**Noah [00:31:59]:** That's a bomber drone.

**Yaroslav [00:32:00]:** That's full autonomy for a bomber drone, right?

**Noah [00:32:03]:** You're saying that no human decision is made in this entire process?

**Brandon [00:32:06]:** That's not, that's not what he's saying.

**Yaroslav [00:32:07]:** A human decision was made at the beginning of the process-

**Noah [00:32:09]:** I get it. I get it

**Yaroslav [00:32:09]:** The same way as you would fire an artillery.

**Yaroslav [00:32:12]:** When you fire an artillery, you don't stop at like, 500 meters away from a target and ask it whether, you want to strike or not. That's exactly, a human decision is always made at some point. So when you do that's full autonomy, and such full autonomy is happening as we speak. And such full autonomy increases the capabilities of an FPV drone, which is already, like, three orders more powerful than an artillery shell. Full autonomy increases its capabilities by four orders of magnitude because now you can have 100 times as many people who can use it, because you don't need to train those people, and this is important. You can have 10 times, mission success rate, and you can have 10 times utility per drone because now instead of being one-way kamikaze, it's, it can be a bomber.

**Brandon [00:33:05]:** Now wait, let's, you said 10 times mission success rate, which means that fully autonomous bomber drones succeed in their missions 10 times more often than human piloted bomber drones do. That's an important thing to know.

**Noah [00:33:17]:** Maybe, to push back on

**Brandon [00:33:19]:** They're super, they're superhuman. They're, they' 10X superhuman.

**Yaroslav [00:33:22]:** They're not vulnerable to electronic warfare. They don't care about the radio horizon. They don't lose track during navigation. They are not susceptible to human error when, an artillery shell or other drone blows up besides you and you're like, "Hell no,"like, "I'm getting out of here." Right? That doesn't happen to an autonomous drone. Like, all of those things. Like, we have, like, one of the brigades that's using our drones with just first level autonomy They literally said that their success rates-

**Brandon [00:33:53]:** What's first level autonomy?

**Yaroslav [00:33:54]:** First level autonomy is just the terminal guidance.

**Yaroslav [00:33:57]:** By the way, we have video of that. We can watch that.

**Brandon [00:33:59]:** Terminal guidance means a human gets it nearby and then the AI takes over.

**Yaroslav [00:34:03]:** The human flies it all the way, like 30 kilometers towards the target, and obviously the target was probably given to that human by someone who's flying some ISR drone, some reconnaissance drone, right? So all the way to the target, and once you see the target from a distance of 500 meters, you do target lock, and from there drone flies autonomous. So just that feature alone, it has increased the guy's, his call sign is Grom, so it has increased his, mission success rate, like precision of mission, yeah, mission success rate from 20% to 71%, and it also increased his kill zone from three kilometers to 10 kilometers, which means there's certain area around the front line which is designated kill zone. Whenever enemy goes into that area, it's almost guaranteed to be to be destroyed by a drone. And then obviously the drones are not launched from like, the zero line. They're usually launched from like, minus 10 kilometer-

## Mission Success, Failure Modes, and the Five Levels of Autonomy

**Brandon [00:35:03]:** What is a zero line?

**Yaroslav [00:35:05]:** Zero line is sort of an imaginary line of control, of two conflicting forces.

**Brandon [00:35:14]:** It's important to explain these things to a lot of the listeners who are

**Yaroslav [00:35:17]:** Thank you for asking

**Brandon [00:35:18]:** Familiar with warfare.

**Noah [00:35:20]:** Myself.

**Noah [00:35:20]:** I'm one of those listeners.

**Brandon [00:35:20]:** You said that level one autonomy, in other words just terminal guidance, just, like, human gets it to the finish line and then it goes over the finish line, increases mission success from 20 something percent to 71%, or something like that.

**Yaroslav [00:35:33]:** Increases the kill zone

**Brandon [00:35:34]:** Increases the kill zone

**Yaroslav [00:35:34]:** Three kilometers to 10 kilometers.

**Brandon [00:35:36]:** Got it.

**Yaroslav [00:35:36]:** On both parameters-

**Brandon [00:35:37]:** What is full autonomy, dude? And

**Noah [00:35:38]:** Actually on real quick, can we define mission success and like, maybe in a way, what are the failure modes of missions?

**Brandon [00:35:44]:** I have a guess what mission success is.

**Noah [00:35:46]:** But I could

**Brandon [00:35:47]:** Get 'em.

**Yaroslav [00:35:49]:** No, but that's a very good question, in fact, because, even if you fly into the target, well, first the target can be damaged or destroyed. Those are two different modes. Then there can be different targets. A sole infantryman is one kind of target. A dugout where supposed there are some, enemies there is another kind of target, and a some mechanical equipment is another type of target. Radio emitting equipment, which, like, often, like, the targets that the military want to get more than anything else is the some enemy radio tower or something like that or some small radio dish that really makes life difficult in that area, in that combat area. So those are different targets, right? It can be destroyed, can be damaged.Then sometimes, the drone hits but doesn't explode. Like, that happens. And then, there are other failure modes. You didn't even reach the target because you were A jammed by electronic warfare; B, you lost the control over drone because of the radio horizon; C, you were jammed by a different type of electronic warfare that happens way before You hit the target area. It's, impacting your, video receiver. So like jamming on video or jamming on control are two different types of jamming. Then something malfunctioned on a drone, just a mechanical malfunction, maybe like a motor broke or like, whatever. So all of those are different failure modes. Yeah, or maybe you got lost, you're navigate navigating to your, to your target. That happens, too.

**Noah [00:37:41]:** The Level one autonomy, basically you manage to point in a direction.

**Noah [00:37:49]:** You go there, and then the last mile The drone taking over.

**Yaroslav [00:37:52]:** We define this like, I define that but it sort of got picked up by the industry. We define five levels of autonomy. So level one is terminal guidance. It's what we just discussed. Level two is bombing. Level three is autonomous target detection and engagement decision. Level four is autonomous navigation. And level five is autonomous takeoff and landing.

**Noah [00:38:15]:** Those are good things to know

**Yaroslav [00:38:16]:** Those are five levels of autonomy. Now, if you

**Noah [00:38:19]:** I have a question for you.

**Yaroslav [00:38:19]:** Sorry. Like, let me finish with

**Noah [00:38:21]:** Sorry

**Yaroslav [00:38:21]:** Theoretical part.

**Noah [00:38:23]:** What is Tesla running at right now?

**Yaroslav [00:38:25]:** Tesla?

**Noah [00:38:25]:** No, sorry.

**Yaroslav [00:38:26]:** That's very good point. Like, it's exactly, it was inspired by the levels of self-driving autonomy.

**Noah [00:38:32]:** Waymo's level five, right?

**Noah [00:38:35]:** You just tell it where you want to go, it picks you up, and then you go there.

**Yaroslav [00:38:36]:** I think, like, if you, if you look at the classic definitions of self-driving cars, Waymo is still, like, level four because it still requires even remote, but still, like, human control. It's like if Waymo gets in trouble, there is an operator who takes over and resolves this. So that would still be a level four. It doesn't map directly, but it's also five levels.

**Brandon [00:38:58]:** Can I, can I interject a question here? In terms of an FPV drone that's like a suicide drone that'll just blow itself up killing something, how do what it hit? Like, does it, just transmit back, or do you sort of like, lose track of it and hope it hit? Like, what happens to that?

**Yaroslav [00:39:16]:** That's a great question. So

**Brandon [00:39:18]:** You need another drone

**Yaroslav [00:39:19]:** Like, the current battlefield in Ukraine is saturated with different types of drones. So obviously you have all the FPV drones and last year alone, Ukraine manufactured about 4 million of these, and then Russia's maybe, like, 20% less than that. And for this year, the publicly voiced target was 7 million on Ukrainian side. So it's, like, serious numbers. We're getting in serious numbers here. And then besides those, there are different, reconnaissance drones, ISR as we call them, and there are sort of tactical level ISR where we, both Ukrainians and Russians usually use, Mavic, drone by DJI. And then there are a bunch of locally produced drones, which are sort of fixed wing drones that can stay in the air for much longer than Mavic, maybe, like, half an hour. And then, there are drones that can stay for many hours or even up to a day. And those drones have, are more expensive, have more expensive cameras, et cetera, et cetera. We hunt those drones that Russians launch. The Russians hunt our drones, and so on. But ideally, when you, are a group of soldiers operating an FPV, you'll have someone in your, company, or someone in your platoon who has an ISR asset that will do target designation for you. They'll say, "Oh, like, there's a Russian vehicle over there. Go and get him."and you go there, you get it, and they're like, "Okay, confirmed."

## Battlefield Surveillance and the Eight Dimensions of Autonomy

**Brandon [00:40:57]:** Those guys are watching. They have their own drones in the sky.

**Yaroslav [00:40:59]:** Target destroyed. They have, like, a carousel of drones because One Mavic cannot stay more than 30 minutes. It

**Brandon [00:41:06]:** They're constantly surveilling the battlefield.

**Yaroslav [00:41:07]:** Almost every spot on the battlefield.

**Yaroslav [00:41:11]:** It's not always the case. Sometimes you will not have a surveillance asset, so then you would launch another FPV just to confirm that there was a hit. Then if you see there was a hit and you're not sure if it completely destroyed, you maybe hit again for good measure.

**Brandon [00:41:26]:** You double tap.

**Yaroslav [00:41:28]:** That's how it works. But I was about to give you another sort of piece of taxonomy. So you have five levels of autonomy, right? Then you have sort of eight dimensions of autonomous battlefield. So what is eight dimensions? It's crucial to understand how autonomy evolves in a modern, battlefield environment. So dimension number one is level of autonomy. What are the capabilities that your asset has? Dimension number two is the platform you're operating on. So it can be a quadcopter, a fixed wing drone, different types of maybe, like, a long range drone or short range drone, but it can also be a missile. You can have autonomy even on an artillery shell or a ground vehicle or a sea vehicle. So all of those are different platforms. Level three would be domain. So it's ground to ground or ground to air as an intersection, or ground to sea or sea to air. They're all, like, all the nuances with different domains. Then level four, would be higher levels of autonomy, such as swarming, drone carriers, drone nests, et cetera.

**Brandon [00:42:39]:** Now when you're saying level, you're talking about dimensions, not about-

**Yaroslav [00:42:42]:** Sorry. Yeah

**Brandon [00:42:43]:** Autonomy levels. So dimension four.

**Yaroslav [00:42:43]:** The dimension. Yeah, I used to say I was supposed to say dimension. I say dimension because each of them works with another, right? So you might have, like third level autonomy, fixed wing drone operating in land to air, and stuff like that right? And then operating in a swarm or operating from a nest. Right? Then you have, sort of dimension number five is environment. So is it day or night? Is it summer or winter? Is it, humid, cold, dry? What kind of target is it? Is your target hiding in a forest, or is it, behind a hill or within buildings? So all of that is environment. Then you have, dimension number six is command and control. How are you dealing with or like, tens of thousands of those assets around the battlefield? How are you coordinating that on the higher levels of command? How are you collecting data? All that.

**Yaroslav [00:43:44]:** Dimension number seven would be infrastructure, so things like simulation, data collection tools, security, deployment mechanisms, et cetera. So all those systems have to be developed separately and integrate with all the others. And finally, dimension number eight is sort of distribution. Have you deployed 100 of these systems or 100,000 of these systems? Because those are two very different ballgames. So that now gives you a more broad overview of how autonomy propagates across the battle space.

## Targeting, Human Responsibility, and Rules of Engagement

**Noah [00:44:23]:** As someone who has done machine learning and had gone out of distribution and had things, go horribly wrong, you were talking several of these, kind of axes of thinking about drone warfare seem like they could be very susceptible to some sort of distribution shift if you start making things autonomous.

**Yaroslav [00:44:41]:** Like what?

**Noah [00:44:41]:** I mean Well, first of

**Yaroslav [00:44:43]:** If the I'm very interested Sort of sort of kinds of scenarios that you're thinking about.

**Noah [00:44:48]:** Like the most obvious one is you, if I assume these are computer vision guided systems for at least the last mile, how do you ensure that oh, well, like you now have some fog roll in or something, and you, the drones just attack the wrong thing? Or maybe, it probably will not turn around and fly back and attack you, but you

**Yaroslav [00:45:10]:** Same, the same, the same question, how do you ensure that your mortar fire hits the right thing? Well, it's like mortar fire, give or take half a kilometer could be plus or minus. So maybe you fire one, and then you fire another. So drones are actually, much better in being precise in those scenarios. And I think, to your point, I think five to 10 years from now it will be immoral to use weapons without AI.

**Yaroslav [00:45:44]:** 'Cause weapons without AI will be more likely to cause, collateral damage or unwanted damage. Same way, it will be immoral to drive your own car manually on a public road because it's more likely to cause, unwanted damage.

**Noah [00:46:02]:** Wow, I never considered that might

**Brandon [00:46:04]:** Really? That's definitely coming.

**Yaroslav [00:46:07]:** Anyway.

**Brandon [00:46:07]:** No, but that' I don't know, it's an obvious, an obvious thought. I agree with you.

**Brandon [00:46:12]:** I, No, they, obviously they're not going to let you drive once most of the cars on the road are autonomous.

**Noah [00:46:17]:** No, that one, don't I believe.

**Yaroslav [00:46:19]:** No, I think you were you were talking about drones, right?

**Brandon [00:46:21]:** The drones, right. Cool.

**Yaroslav [00:46:22]:** The weapons, right?

**Brandon [00:46:23]:** Friendly fire and collateral damage and stuff like that is all minimized with AI.

**Brandon [00:46:27]:** Here's my question. Take all let's go to level six autonomy. Let's take all of the target selection. Let's take all the battlefield data, integrate it into one big AI, and have that big AI basically be in command of the battlefield And agentically do target selection.

**Yaroslav [00:46:44]:** Be the general, right?

**Brandon [00:46:44]:** It's a general. It's, you've cut humans out of the loop except maybe as dexterous robots, repairing drones and fastening things to drones or maybe something like that because you don't have those robots yet. How soon are we there? AI general.

**Yaroslav [00:46:58]:** The most important thing to ask ourselves is who will be faster to that us or our adversaries?

**Brandon [00:47:07]:** I assume us, but how fast will we be to that? I hope us.

**Yaroslav [00:47:11]:** I hope so too.

**Brandon [00:47:12]:** How fast can we Like when are we looking at that in terms of like horizons years?

**Yaroslav [00:47:18]:** Like technically, it could be done now. The question is of course, there's, some engineering work to be done. The bigger challenge is deployment. Right? So okay, technically Like operation in Iran, right? They, the publicly, it was claimed that I think Palantir system was used for target designation, et cetera, et cetera. So it is not exactly as you say, the AI makes all the decisions, but basically AI goes through all the data you have, gives you these 1,027 different targets and says, "You-- To confirm, please press Okay." And you look at the targets and you're like, "Yeah, sounds right. Press Okay."so that's, I think that's where we are now already, or we were a couple weeks ago as we're recording this on April 10th. Another question is how massively deployable it is. Is it, like, every decision being made like that or is it, like, just some of the decisions made like that? And then different levels of command and control. There you have, like, the platoon, the company level, the battalion, et cetera, et cetera, et cetera. But the tricky thing here when we get into that territory, the tricky thing is If your enemy is getting advantage of being Thousand times faster than yourself by deploying such systems What do you do?

**Yaroslav [00:49:10]:** You got to-

**Brandon [00:49:12]:** The if the enemy is a thousand times faster than you at deploying those systems?

**Yaroslav [00:49:16]:** Like, if enemy starts deploying level six autonomy, as you call And you have not started doing

**Brandon [00:49:22]:** You're in trouble

**Yaroslav [00:49:23]:** Yes, exactly. So you have to catch up. So my point is that it is very important to think about the safety of these systems, but that thinking should not slow you down in developing them because they are critical for your existential, survival, right? And like, one person who doesn't think, doesn't get to think about the ethics of the war is a dead person. That person surely doesn't get to think about that.

**Brandon [00:49:52]:** What would be the safety risk of such a system?

**Yaroslav [00:49:55]:** Of course-

**Brandon [00:49:56]:** Friendly fire?

**Yaroslav [00:49:56]:** Just wrong decisions, right?

**Brandon [00:49:59]:** I see.

**Yaroslav [00:49:59]:** Maybe, these decisions-

## AI Command Decisions, Dead Zones, and Complex Battlefields

**Brandon [00:50:06]:** Skynet AI decides it's going to use

**Yaroslav [00:50:08]:** No, these-

**Brandon [00:50:08]:** Drone army to kill us

**Yaroslav [00:50:09]:** Decisions will not only be made about drones. They are likely to made about what the humans should do on your side as well. Then obviously some environments are more like Ukrainian-Russian war, where you have

**Brandon [00:50:26]:** It will have to choose to risk lives. It will have to choose to sacrifice human lives-

**Yaroslav [00:50:28]:** Of course

**Brandon [00:50:29]:** On your side.

**Yaroslav [00:50:29]:** Of course. And then some environments are just, like, dead, like, dead zones and there are no civilians there, or virtually no civilians close to the front line because, like, super dangerous. Everyone has evacuated from there. But there are other environments which are more like, okay, there's a counterterrorist operation. There's, like, a group of terrorists or a group of civilians. Or like, it's like the recent operations in Iran, I imagine that the US and Israeli forces do not want to harm civilians. They only targeted the military targets there, right? So in those situations, it's a different level of responsibility for that decision-making as well. And then there is just such a big variety of those military missions, and I'm not even, like, well-informed or well-educated in military science to tell you about all those scenarios. We would need to put some general besides me, and maybe a Ukraine general and American general would have told you very different stories about these things.

**Brandon [00:51:34]:** Got it. Can I ask a few more questions? All right. So in 2013, I wrote one of my first, paid articles ever was about how the era of drones will change human society. I was just sitting around bored thinking about things.

**Yaroslav [00:51:54]:** You were way ahead of your time.

**Brandon [00:51:55]:** I said, I said, "The following will happen."

**Yaroslav [00:51:57]:** It's, this article is real. I've read it.

**Yaroslav [00:51:58]:** It's actually-

**Brandon [00:51:59]:** I said small autonomous, suicide drones, will cleanse the battlefield of human infantry. Human infantry will not be able to stand against swarms of AI-powered, suicide drones. That was I didn't even know about, like, AlexNet at the time, I think.

**Yaroslav [00:52:19]:** You're just an avid sci-fi reader.

**Brandon [00:52:23]:** I'm an avid sci-fi reader, but also, like, it's not Like, there will be a way to do that. It's a it's a nonlinear multidimensional search problem, and you get enough compute, you'll find some search algorithm that will get you there. And so

**Brandon [00:52:38]:** I, yeah, I think that one sentence describes the bitter lesson right there.

**Brandon [00:52:41]:** It's just like it's a multidimensional search space. You search it somehow. I don't know. Figure out some get a grad student-

**Yaroslav [00:52:47]:** Sooner or later

**Brandon [00:52:47]:** To make a search algorithm.

**Brandon [00:52:48]:** It's not that hard. Anyway, so but then, but I guess the point is The point is that human infantry on the battlefield will be will be gone at the end. I wrote that in 2013. Many people on social media laughed at me for that called me hysterical, said things like, "Electronic warfare will knock all the drones out of the sky."like, "You need humans to hold ground."that's something you still hear from a lot of people on social media today. I feel that this article that I've written has never been directionally wrong. It has gotten more and more right steadily over time, and that we're very reading the battlefield reports from Ukraine, where, human infantry are basically guy, like a few guys hiding in dugouts for months, and I'm not sure what they're doing.

**Yaroslav [00:53:35]:** That's on Ukraine's side. On the Russian side, that's just like a zerg rush.

**Brandon [00:53:38]:** The zerg rush, and then they just die. Then, but they have some guys in dugouts too, right? Like hiding in dugouts for months.

**Yaroslav [00:53:45]:** They have. Yeah.

**Brandon [00:53:45]:** Like, but that like, what are those guys doing in the dugouts? Are providing, like, frontline, like, reconnaissance? Like, what are they doing?

**Yaroslav [00:53:54]:** If there is a guy in a dugout with some bullets and automatic weapon, the other guy cannot come and take the that dugout. That'

**Brandon [00:54:07]:** I see

**Yaroslav [00:54:08]:** They are they're establishing control over territory.

**Brandon [00:54:10]:** I see. So that is so there still is a use for human infantry on the battlefield as of today.

**Yaroslav [00:54:15]:** Like

**Brandon [00:54:15]:** How long will that last?

**Yaroslav [00:54:17]:** I think it will last for a while. This is funny. There's this whole Layer of the modern culture, a modern Ukraine culture built around the war-related stuff. So there is this -Punk rock band, that is called SZC, I guess in English that would be. Which stands short for like a deserter or something like that. So anyhow, this band has a song titled "2030." It's basically about the year 2030, and the war still goes on as like the whatever, third world war or whatever. And they basically, they, sang about the AI and like cyborgs and everything, but the simple infantry is still needed, and we're still, like, getting cold in those dugouts, and we're still doing our job. That's sort of the theme of the song. And it seems like that's actually what's going to happen. There are

## Ground Robots, Simulation, and the Limits of World Models

**Brandon [00:55:30]:** Ground robots will not replace humans in the dugouts soon.

**Yaroslav [00:55:34]:** I'm very much interested in following the whole humanoid robot theme and

**Brandon [00:55:39]:** What about like a dog robot?

**Noah [00:55:41]:** Or just mobile controlled platforms or something.

**Brandon [00:55:44]:** Spider robot, yeah.

**Brandon [00:55:45]:** Everything evolves into a crab.

**Brandon [00:55:46]:** You build a crab robot.

**Yaroslav [00:55:47]:** A humanoid-

**Noah [00:55:48]:** The carcinization of warfare.

**Yaroslav [00:55:51]:** There is a lot of utility in humanoid robots because the world is designed around humanoids. So I would not, like, 100% disqualify the possibility that sometimes 10 years in the future, humanoid robots, will be actually fighting. So that's an actual Terminator kind of scenario.

**Brandon [00:56:14]:** Yeah, in the first Terminator movie, you look at what they've got on the battlefield, they've got flying bomber drones and humanoid robots.

**Yaroslav [00:56:20]:** Look, the cost of large language models of running them is getting so low, you can have basically an inexpensive computer running, what was a state-of-the-art model a year and a half ago, running it locally on a device with an open source model, which also means that the Chinese can have it, the Russians can have it, the North Koreans can have it, et cetera. So that is already possible. And with when we're looking at the acceleration of the neural nets, I would've, if not the acceleration of the large language models, I would've said that I don't think that humanoid robots will be able to be useful in the battlefield earlier than in 10 years. But if you account for the exponential, it might be five years or so. The problem with all of the autonomous systems, and it's like starts with self-driving cars and even with all the AI, like modern day AI agents, to make them really, useful, you have to solve such a long tail of edge cases, that it's really difficult to make them useful. Like we were promised, self-driving cars, what, like 2007, Sebastian Thrun and Google, and even before that all the challenges, everything. And Elon of course told us it's going to be one year from 2014, and now we still don't have self-driving Teslas everywhere. We have Waymos in SF and some other places, but they're still, like, not perfect. So I think, I expect something similar from self-flying drones and fully autonomous drones, and we saw that firsthand as with each level of autonomy that we're adding, there is a very wide distance between a prototype and something that is ready to be scaled to millions of units and something that has been scaled to millions of units. But the race with like AI coding tools is just insane. So things might accelerate very fast, faster than we can imagine.

**Noah [00:58:46]:** I think your point is that with due to this long tail behavior Level one autonomy as you've defined it, is actually very natural. Like you basically are just solving an image recognition and tracking system.

**Yaroslav [00:59:02]:** It's actually interesting that you say it that way, and I thought about this the very same way, and we have this joke that there are like 200 companies in Ukraine which are trying to solve last mile, targeting or terminal guidance. It seems like we're like the only company that actually solved that because even that problem-

**Noah [00:59:22]:** I'm not saying it's, I'm not saying it's trivial, but it's at least something that you imagine given our current state.

**Yaroslav [00:59:26]:** Like us and Eric Schmidt, like Eric Schmidt's companies are pretty good.

**Yaroslav [00:59:29]:** Like, I actually have lots of respect to what they're doing, and they're, they have been practically influential and helpful on the battlefield, and they have good engineering.

**Noah [00:59:38]:** I wasn't, I wasn't saying it's trivial. I'm just saying this is a something naturally adaptive based upon things that we know work, well. But some of the other domains that where you do have to make decisions and you have a long tail become much harder, and you worry about edge cases more.

**Yaroslav [00:59:57]:** Like the more, the more complex behavior you're trying to simulate, the more edge cases there are right? The more ways to do it wrong there are. And then there are different approaches. It's like if you think about, if you read academic papers about robotics, right? You sort of the robot is represented as something that has the sort of sensor input, and then you have three, levels of sort of logics or decision-making, which are perception, planning, and control, and then you have actuators as output.So pre-neural nets, you would do perception output and control all with classic logics, right? Then, with AlexNet and computer vision, you could do perception with neural nets and the rest with logic. You cannot currently do each of those separately with neural nets, each of those separately with logics, or you can just have one huge neural net that just takes lots of sensory data. It's not just pixels. Could be sound, could be accelerometer, could be everything, as input, and just outputs the controls. And some of the self-driving car companies are doing that or like, experimenting between different ways of doing that. So you can also, like, think about that and the way you implement those features, also influences how much degrees of freedom the system would have, right? Like control, you can do it classical algorithmic control with common filters and PAD filter, PAD controllers, et cetera, or you can do a neural net, that was trained in a gym with a reinforcement learning, et cetera. And those would be two different behaviors of a system.

**Noah [01:01:53]:** I-- Maybe my point was just much more high level. It'

**Yaroslav [01:01:56]:** Or you can If you go even like, if you go high level, you can, you can like train to like have whatever, like Feifei Li and folks who are doing like physical, sort

**Brandon [01:02:08]:** World models

**Yaroslav [01:02:08]:** World models, right, physical intelligence, they're trying to make these big models and sort of understand the world and then supposedly you have such model and you can tell a drone, "Okay, like, go over that hill and like, find the bad guys and then get them,"or "Make me a video, make me a photo of the guy smiling and get back to me." Right? That's one way. Another way you have like these subsystems, like one is navigation, another is finding the person, another is like getting to them to take a photo. And those are again, very different behaviors. And then it's not that one is necessarily better than the other, and we might have more technological ability to do one or another. But all of those systems will exist. And then again, you should always keep in mind that it's only the not only the good guys that are developing these systems, the bad guys are developing these systems as well.

## China's Drone Supply Chain and the West's Manufacturing Gap

**Noah [01:03:00]:** I guess where I'm going with this back to Noah's original thought with the end of the end of the soldier. And so in order to replace-

**Brandon [01:03:10]:** Or at least the end of the rifleman.

**Noah [01:03:11]:** Or the end of the rifleman, yeah.

**Yaroslav [01:03:13]:** I'm not seeing that very close, and it was like I'm, as much as I'm a lover of sci-fi and all of that and a technologist, the more I try to be

**Yaroslav [01:03:27]:** Like the I try to have certain humility about these things, and like the military, domain and there was just so much human history and blood and tears, dedicated to sort of understanding this art of war and perfecting it and so on. There is so much knowledge in there that I don't feel like I even started to comprehend, a lot of that. But one thing that I really understood is that even though drones are now making eighty percent of the casualties, you go to the actual officers, you talk to the actual, like, brigade commanders, corps commanders, and they explain to you, how all of it fits together, how when you're thinking about an operation that involves a couple thousand people to get this piece of land, out of the enemy's hands, deoccu deoccupy it, how it is so complex, it involves, dozens of different types of drones and then land operations and reconnaissance operations, psychological operations and then aviations and tanks and logistics and all kinds of these different assets. So modern warfare is really very complex, and the fact that the drones are the latest, coolest thing, and then the AI is latest, coolest thing, doesn't mean that now it's that and only that right? So yeah. Whoever's looking into that I think should realize that it's not just what the press talks about, that the reality is much more difficult, much more complex.

**Brandon [01:05:17]:** Let's talk about China and China's manufacturing capabilities. So suppose that someone, like suppose the United States went to war with China. And

**Yaroslav [01:05:26]:** I hope not.

**Brandon [01:05:27]:** I hope not as well. And then but suppose that drones were very essential to that war of all the types of drones that we're talking about here, and that suppose that China said, "All right, well, you need X and Y and Z, to make those drones to fight us, and we control the production of X and Y and Z, so we're just going to cut you right off, and now you have no drones."

**Brandon [01:05:47]:** I know that a number of countries, including Ukraine and Taiwan, have been making moves to China-proof their drone productions that China couldn't do that. Examples of things they might be able to cut off might include rare earths, fiber optic cable that you were talking about before, various other things that where even if they don't control one hundred percent of the production, they control enough of the production that would be extremely expensive to produce it without relying on Chinese sources. Or the market's fragmented enough, et cetera. What do you see as China's key bottlenecks, and how easy are those to overcome in terms of China-proofing drone production in case of a war against China?

**Yaroslav [01:06:30]:** Let me start with a saying that -Although China does not sell directly to Ukraine and it does sell directly to Russia, a lot of Ukrainian supply chains, they start in China, right?

**Yaroslav [01:06:49]:** We're not in a conflict with China, and we would not want to be in a conflict with China. And we'd hope that China stays a neutral power between Ukraine and Russia and the US as well. That said, the scenario that you're describing, everything is much worse.

**Yaroslav [01:07:11]:** Think about this. Last year, Ukraine produced four million FPV drones. Ukraine is not the most industrious nation in the world.

**Yaroslav [01:07:19]:** China can produce four billion of these FPV drones.

**Yaroslav [01:07:23]:** China can make them not drones with propellers, but fixed-wing drones, which go not forty kilometers far, but maybe two to three hundred kilometers inland. Slightly more expensive.

**Brandon [01:07:34]:** With internal combustion

**Yaroslav [01:07:36]:** No. With

**Brandon [01:07:36]:** Battery-powered fixed-wing drones.

**Yaroslav [01:07:38]:** Battery, yeah.

**Brandon [01:07:39]:** What's the propulsion system on those propellers?

**Brandon [01:07:43]:** I don't-- I just don't know how that works.

**Yaroslav [01:07:44]:** You have that. They can also make them all fully autonomous. They have DJI, the world's most advanced drone company. They can make them fully autonomous without GPS, without anything. Then they can put those drones on maybe tens of thousands of fully autonomous underwater submarines, or maybe not even that just on shipping containers and barges that ship goods or freight ships. And then they show up with millions of drones packed onto those, sea vessels. They show up to any coastline in the world, be it Taiwan or be it California, and they have millions of long-range impactors targeted at a at a piece of land.

**Yaroslav [01:08:38]:** What do you do with that? There are not enough hunter submarines. There are not enough anti

**Brandon [01:08:46]:** Ship missiles.

**Yaroslav [01:08:47]:** Anti-ship missiles, anti-ship, planes. They can produce these assets, on in tens of thousands of factories because they're so simple to produce that even the if the FBI director picks a phone, calls to the President of the United States, says, "Hey The scenario Yaroslav was warning us about is beginning to unfold. We need to do a preemptive strike,"You wouldn't have enough assets, to do preemptive strikes because there can be like tens of thousands of places where these things are being manufactured. And then so to counteract a scenario like that we would need to have like a similar amount of mass

**Brandon [01:09:39]:** You mean a similar number of drones.

**Yaroslav [01:09:41]:** Yes, to intercept that like either in sea or in air, et cetera, at a similar cost, right? So economics should work out. I'll tell you that currently, we in the West and we in the United States, we don't have the technology to do that. We don't

## Four Layers Behind China: Technology, Manufacturing, Components, and Rare Earths

**Brandon [01:10:01]:** What technologies, key technologies do we lack?

**Yaroslav [01:10:03]:** Like autonomy, mass drone manufacturing, stuff like that.

**Brandon [01:10:06]:** We lack autonomy technology?

**Yaroslav [01:10:09]:** I think so.

**Brandon [01:10:10]:** Because our computer vision algorithms are not as good?

**Yaroslav [01:10:12]:** It's not only about the computer vision algorithms. It's like the like if a group of companies by Eric Schmidt founded two, three years ago and my small startup, was like maybe not as small, but it's also founded three years ago, are sort of two of the leading companies in the world, and maybe a couple others who are capable of something like that but not really on small drones. I do think we'll, we were behind China in technology. So we lack technology, we lack mass manufacturing capacity, we lack the components, and we lack the rare earth materials. So there are four layers in which we're behind this challenge. And that's why it is my point that we in the in the West, and especially in the United States, we should, there should be far more smarter people working in defense, and there should be more funding, if we want to keep the resemblance of our good past life.

**Brandon [01:11:14]:** That's really important. Would you say that right now, as things stand, in conventional terms, not, abstracting from strategic nuclear weapons, but in conventional terms, would you say that China is now the supreme conventional military power on Earth, given its ability to manufacture and deploy drones in the quantity and quality that you just described?

**Yaroslav [01:11:35]:** Look, I don't, I don't think we have all the information to claim that but

**Yaroslav [01:11:41]:** We cannot count it out, and that alone should be a big warning sign. We have not seen, Chinese drones in action. We've seen some of the Iranian drone in action and Russian drones in action. Not Chinese really. Not seen Chinese forces in action. Obviously, hopefully, this never happens, but the conflict of a scale US, China, there are many Sort of classical assets that we should not discount. As we just discussed, we should not discount artillery in the land war, we should not discount, air-carrying groups and the air force, and long-range missiles and electronic warfare and satellites, et cetera. But then there are also things that we, at least we as a general public don't really know about China. I'm sure there's a lot of information that the US intelligence has about the Chinese capabilities. -I think if you, if you get back to the scenario that I just described, and if you take that like, sort of to the maximum You basically see that whoever has bigger manufacturing capacity, that side wins.

**Brandon [01:13:03]:** That's just a typical law of conventional warfare Has been forever.

**Yaroslav [01:13:07]:** Sort of.

**Noah [01:13:07]:** Do you read Noah's blog?

**Yaroslav [01:13:09]:** I not as often as I would like. But I read Noah's, X.

**Brandon [01:13:15]:** It's not necessary.

**Noah [01:13:15]:** It's a theme where

**Brandon [01:13:16]:** Don't read my X.

**Brandon [01:13:19]:** It's just for

**Noah [01:13:19]:** He doesn't, he has no opinion about certain things. Yeah

**Brandon [01:13:22]:** It's just jokes.

**Yaroslav [01:13:22]:** No opinion. Okay.

**Brandon [01:13:22]:** Okay, so here's the I guess there's two questions here. The question of could The United States and other countries allied with the United States even develop supply chains that are independent of China to make any of these drones? And the second question is could they do it in sufficient mass? And so I think the answer to the question of can they do it in sufficient mass is today, no. But in a extended, prolonged war situation, things change a lot. And all the development restrictions that we put on new factories go out the window, and a sense of urgency. Ukraine obviously wasn't making all these drones before the war.

**Yaroslav [01:14:04]:** Of course.

**Brandon [01:14:04]:** So if America had the same kind of urgency that Ukraine has now, things would happen. Things would move, and of course, America has allies too, or had allies until recently, and may have them again in the future. But America has or had allies that would also scale up very quickly, like Japan and European countries if we ever ally with them again, et cetera. And so a lot of things could then change in terms of the actual mass. So I, in terms of looking at China and saying they have all these factories today, and looking at the history of conventional warfare, America had very few military very little defense production capability on the eve of World War II, and ended up easily outproducing everyone else, even the Soviet Union.

**Yaroslav [01:14:47]:** Maybe not easily. Yeah.

**Brandon [01:14:49]:** Not easily, but by a long, a long shot.

**Yaroslav [01:14:51]:** Also the added benefit of not being attacked.

**Brandon [01:14:54]:** That's right. That's right.

**Yaroslav [01:14:54]:** That helps.

**Brandon [01:14:55]:** Who knows how Secure they are now, but or what, where cyber influence

**Yaroslav [01:15:03]:** No, look, I totally agree with your sentiment. I like, and I'm not as y, I'm even less doomerish than you are. Or as it seems to me, you're a little bit doomerish, but like, in the long term, you're bullish.

## Choke Points, Europe's Wake-Up Call, and Defense Industrial Policy

**Brandon [01:15:17]:** I'm not, I'm not doomerish. I'm thinking about the I'm thinking about what we need to do.

**Brandon [01:15:21]:** I'm not, I'm not thinking like, "Oh, we're doomed." That's not my point. It's never useful saying that. If you're doomed, then just don't go on podcasts.

**Brandon [01:15:28]:** Go pet a rabbit and play a video game or something. It's Anyway, no, if you're, we're not doomed, but I'm saying step one, how, what are the key choke points that we need tomorrow, besides rare earths, which we already know, what are the other key choke points that the West needs to free itself from Chinese supply chains on in order to manufacture even one drone Free Chinese supply chains?

**Yaroslav [01:15:54]:** There are companies here who are doing that like our, we have, good friends, a company called Neuros. I know they're, down in El Segundo or whatever, like somewhere on South California.

**Brandon [01:16:05]:** What are the most pressing choke points besides rare earths that everyone talks about?

**Yaroslav [01:16:09]:** That's one of the pieces that we do, thermal cameras. That's like actually a big one.

**Brandon [01:16:16]:** Thermal cameras.

**Yaroslav [01:16:17]:** Then, like, the motors. Like you need The special-

**Brandon [01:16:25]:** Even after you have the magnets, then you turn them into a really good motor.

**Yaroslav [01:16:28]:** You have, you need these special magnets, and then that's sort of your rare earth component.

**Brandon [01:16:34]:** That's, that'

**Yaroslav [01:16:34]:** Like rare earth is not that oh, like there are these metals that only for some reason, God only put them under the Chinese territory and not under any others. No, like they're distributed. There are plenty of them around Earth. It's about the refining capabilities and like, investing into that and so on. And then, like, frankly, at some point, we don't have that many humans. Like, that's where the humanoid robots help. Like China is a big populous country. The population of like, United West is comparable to that but the population of the US is much lower than that. And I definitely think that the whole West should get their act together, because, ubi semper victoria, ibi concordia. There's always victory where there is union.

**Brandon [01:17:27]:** Agreement.

**Yaroslav [01:17:27]:** Agreement, yes.

**Yaroslav [01:17:31]:** I think we sort of as the free nations of the world, we should get their act together because freedom is what unites us. And I'm also, like, pretty mad at what's happening in the European Union. And I think that Current US administration is the best thing that has ever happened to Europe, since World War II probably. Or since post-World War II, because World War II wasn't the best thing.

**Brandon [01:17:59]:** Trump withdrawing the image of omnipotent American support forced the Europeans to get their butts in gear, unite Develop their defense industries.

**Yaroslav [01:18:07]:** Also, like, doing that not in a nice way, right? Like when JD Vance came to Munich, Forum one year ago, he wasn't, like, super nice, like, "Oh, please, our European friends, please could you please increase your, defense spending?" He was somewhat pushy. Let's put it that way. And that I think that was a necessary measure. Like, I've been, I've been thinking about that. Could it, could it have been he, maybe he could have been nicer? I was like, no, because, like, the voters of European leaders, the European countries, would have not understood this. They would not get the message. And now I think the message was gotten across, but Europe is still sort ofSlow to wake up, I would put it that way. Things are getting better, but I'm not happy about the speed of how they're getting better. So when I, when I, like, when I would go to some of the European capitals, I would get back pretty depressed from like, talking to their, military officials and their entrepreneurs, et cetera. Here, I've been in the US for the last month or so. I'm not depressed. I'm actually, I'm actually excited. I still think you should, like, 10X the effort in sort of making sure that you remain the strongest power, in the world and you can defend your values, et cetera. But I'm very optimistic, and definitely once we are in danger, I think, we're just, like, lots of very smart people in the West who can figure these things out. But people in China are also extremely smart. It's very different from even the Cold War sort of situation. Like, Soviet Union was economically a very declining power. China's not like that. And then if we look at electric car race, I think they're ahead of the US and ahead of the whole world, definitely ahead of Europe, which used to be sort of a car superpower. When you look at AI, I think they're Almost where we are maybe slightly behind. When you look at humanoid robotics, I would argue they're ahead. And in many other, like, in like medicine and sort of biosciences, there are lots of interesting things there, and like, in consumer space, there are lots of interesting, things there. I don't know if you heard this podcast called 996. I don't know if it's still airing or not. There used to be a fantastic podcast by some, American Chinese, businessman, maybe venture funds.

## Humility About China, Taiwan, and Deterrence

**Brandon [01:20:55]:** About the Chinese economy?

**Yaroslav [01:20:56]:** About China from a sort of tech venture point of view. So and I lived in China for maybe four months, and I visited a couple times. Like, even WeChat is like, such a more advanced app than anything we have in the West. So we, it's very important not to be too arrogant, and I think we're guilty of that like, definitely in the US. Sometimes we tend to be too arrogant. Like, I think, like, humility helps always, at least to me personally. And then I think, like, we don't have to we don't have to obviously be enemies. So Like with Ukraine and Russia, it's like Russia came to kill all of these people and get all this territory. With China and the US, it's not like that and thanks God it's not like that right?

**Brandon [01:21:54]:** It might be with China and Taiwan. Maybe.

**Yaroslav [01:21:57]:** Hopefully not. Yeah. It's

**Brandon [01:21:59]:** Hopefully not

**Yaroslav [01:22:00]:** It's like China has their own, problems probably with human rights, et cetera. But hopefully, it's still not beyond the fixing point.

**Brandon [01:22:13]:** Hopefully. Hopefully.

**Yaroslav [01:22:14]:** We should, we should be armed, right? We should, we should be ready to whatever, and then that alone decreases the probability of any conflict. If you're weak, you're basically provoking the conflict. The problem with Europe these days is that like, last year, Ukraine and Russia went in drone technology of 2025, year to drone technology of 2026. Europe went from winter of 2022 to spring of 2022. So the gap, Europe didn't even make one year of progress. The and the US, I would argue, made less than a year of progress as well in the last year. So the gap, the technological gap is getting wider and wider and wider. And at some point, like, I'm looking at polls who are like, very close to us and close to Russia.

**Brandon [01:23:06]:** Polish people-

**Yaroslav [01:23:07]:** Polish people

**Brandon [01:23:08]:** Not surveys.

**Yaroslav [01:23:09]:** Not, yeah. Oh, yeah, sorry. Yeah. That's what I meant. Sorry, not my first language.

**Brandon [01:23:12]:** When I'm looking at the polls, what do they, what do they say?

**Yaroslav [01:23:15]:** Polish people. Polls.

**Brandon [01:23:16]:** No, it's the right word.

**Brandon [01:23:18]:** You're just thinking about-

**Yaroslav [01:23:20]:** No, we.

**Yaroslav [01:23:20]:** I'm looking at them, and they bought like 100 tanks and four submarines. It's like, dudes, you don't have, like, 1,000 people who know how to operate an FPV. What the hell you're doing?

**Brandon [01:23:30]:** Poland is not preparing for war correctly.

**Yaroslav [01:23:33]:** From what I can

**Brandon [01:23:36]:** They're doing a very bad job

**Yaroslav [01:23:36]:** They're not doing it right. And the problem is they'll be in a situation where, they're so proud of their winged hussars and like, their cavalry, and the enemy is attacking with airplanes and tanks. That's literally like the gap is getting wider between Russia and Poland.

**Brandon [01:23:57]:** That happened in 1939.

**Yaroslav [01:24:01]:** I don't want that to happen again.

## What America Should Learn from Ukraine's Defense Valley

**Brandon [01:24:03]:** All right, so the Europeans need to wake up more. If you were advising America's defense establishment, which you might be doing in real life, but if you were saying things on a podcast that might be heard by some people connected to that defense establishment Then which you may or may not be what are like, the besides more funding, more funding, that'll be necessary for anything, literally anything. But so what are the top priorities policy-wise for America to increase its readiness right now? And let's say three to five priorities.

**Yaroslav [01:24:38]:** Look, I really like this quote, I think it's by Arthur C. Clarke, that "the future is already here - it's just not evenly distributed yet."and just the same way as Silicon Valley as this Sort ofFuture location for all things tech. Kyiv and Ukraine is sort of the defense valley. It's the point where the future of defense has already arrived, and there is a ton of things to learn from that starting with particular, hundreds of companies in very particular fields, to the battlefield experience, from battlefield commanders of every level, starting from soldiers, surgeon to platoon level commander to brigade level commander, special forces and intelligence, all of that to how the government, organizes, the sort of the infrastructure and sort of the playing ground for all these businesses to flourish, et cetera. So I would definitely look into much tighter integration and exchanging, the experience and so on. That would be one thing.

**Yaroslav [01:26:03]:** I think Reform and procurement would be another thing, and I think that's what, is currently being done with drone dominance. I think Pete Hegseth is leading that and maybe some other people in the administration. I think that's extremely sort of powerful and right thing to do, and they should scale that big times.

**Yaroslav [01:26:26]:** Obviously, any sort of military person would say, "Well, yes, okay, Yar, you're fine, cool,"but Ukraine and its war theater is very much different from potential scenarios that U.S. Might have to fight, and yes, I agree, but there is still so much to learn even, like, from the sea warfare that Ukraine is doing and then long strain, long range drones like these Shaheds that unfortunately damaged some of the American equipment in the Middle East. They can fly up to two thousand kilometers. So like, if you think about in the Pacific region, like two thousand kilometers, that covers a lot of land with all the like, islands and aircraft carriers, et cetera.

**Brandon [01:27:16]:** I think America is learning that lesson right now in Iran, in the Middle East.

**Yaroslav [01:27:20]:** You would think so but then, I'm not sure. It's like there was so many chances to learn that lesson from Ukraine before, and I don't think it was like, fully learned, so I'm not sure how fully learned the Middle East lessons were.

**Brandon [01:27:34]:** Perhaps losing a war to a minor power will teach America.

**Yaroslav [01:27:38]:** You can, you

**Brandon [01:27:39]:** Although the their economic weapon will be the most important and decisive by far, but still, some of our bases were supposedly, allegedly rendered unusable by their Shahed-type drones.

**Yaroslav [01:27:51]:** Look, I think, there are so many lessons to be taken from this like Russia, a much bigger power attacking Ukraine. Given the same logic that we discussed, whoever has more production capacity should win. But then Russia didn't achieve victory in Ukraine, and then the US didn't get, like, full victory in Iran. Probably achieved some of the goals, but probably not all of them. So that also, you can flip that. Like when you say, "Okay, what if China has so much more capacity than the US? What if they attack us for whatever reason? How can we hold them back if we don't have the rare earths?" Well, as the Ukraine and Iranian examples show, you actually can hold back something like that even if you're a less capable, party.

**Brandon [01:28:42]:** Well, those examples did rely on Chinese supply chains, though.

**Yaroslav [01:28:47]:** Partially, yes. But then if you think about Ukraine in February twenty-two, twenty-two to first half a year or a year, wasn't much reliance on Chinese supply chain. We were just relying on whatever we've got. So that's one side of things. Another side of things is basically how much suffering can you withstand along multiple axes? It's not just the military axis, it's also, like, the economic axis and the political axis, I would, I would argue. So like, one of the reasons why wars stop or start is because the political pressure on the leadership internally in the country is so high that you just have to stop that right? So I think that differs big times, from whether you were the one who's seen by the population as the party which started the conflict or the one who was attacked. That's one part. Another, just by overall state of the society. Like, and one thing I'm worried about in Europe now, that people are not ready to fight even if they're attacked. Like, when people are asked about that they're like, "Oh, I'm just going to move to somewhere where there's like less, there's no war."so that's a challenge, and that's what makes Europe weaker right now. And the US didn't really have to ever, I think, fight a foreign war on its own turf. I hope that never happens, but in case that would have happened, I don't know what would be how would the rich cities of East or West Coast, how would people behave? Like, would all the Wall Street bankers and Silicon Valley VCs, mobilize and really start working on defense stuff? I would love to think so. I like-- That's the way I think about the American spirit.

## The Nuclear Lesson: Budapest, Deterrence, and the World After 2022

**Brandon [01:30:49]:** The way we did in World War II.

**Yaroslav [01:30:53]:** In a way, but look, like it wasn't that clear in World War II, and like Churchill was like famously said, "America will always make the right decision after trying all the wrong ones,"right? And it's like one could argue that there is this sort of this USA that lives in popular culture and was sort of created by Hollywood as like cool dudes that will always come and do the right thing, right? And then if you, if you look at like, international politics

**Yaroslav [01:31:21]:** It doesn't necessarily always look like that. Like the Budapest Memorandum, like Ukraine gave all of its nuclear weapons, the second, worst, third largest, nuclear arsenal, because the US and Russia and the others were very persuasive and they're like, "Yeah, just give it away. We guarantee you security." And they're like, "Oh, it's not guarantees, it's assurances. We use the word assurances, so therefore we didn't promise you much. You just gave it away for free." And then like Russia attacks and like no reaction. So the whole world, like 2022, the whole world looks at it and is like, "Oh, okay, so maybe we should get nukes." So like my prediction, next couple decades, a lot more countries, will be working their own nukes.

**Brandon [01:32:02]:** They really should. I've, I'm consistently advocated for specifically Japan, South Korea, and Poland to get nukes. But obviously Ukraine should as well, but can't

**Yaroslav [01:32:11]:** Someone could argue that if a country currently doesn't work on their own nuclear program, they're, doing a disservice to their country and the government should be fired. Like, because it seems like from the recent world history that is like the only way to actually provide credible deterrence, all right? So I guess I think like in Europe, people are not quite sure, how will America behave. Will it behave as the Hollywood hero, or will it behave pragmatically as it did at the beginning of World War II, or as it did, with when Ukraine was attacked by Russia and the US just decided to sort of push the Budapest Memorandum, aside because of course Russia's a nuclear power and like we don't want to mess with it.

## The Drone Race: Where Ukraine, Russia, and the West Stand

**Brandon [01:32:59]:** Everyone says Russia's behind right now in the drone war.

**Yaroslav [01:33:04]:** True. Okay.

**Brandon [01:33:04]:** But that wasn't true a year ago. So a year ago people were saying either Russia was ahead or they're at parity, or maybe a year and a half ago.

**Brandon [01:33:12]:** Russia has more people, four times as many people about, or more.

**Yaroslav [01:33:17]:** I think give or take, yeah. 30 versus like 120-ish. Yeah.

**Brandon [01:33:21]:** Four times as many people.

**Brandon [01:33:27]:** More help from China.

**Yaroslav [01:33:28]:** Like economy is like 10, 10- 20 times bigger, I don't know. A lot bigger.

**Brandon [01:33:33]:** A lot of oil money, a lot of oil money, that Ukraine just doesn't have. More direct help from China than Ukraine is getting.

**Brandon [01:33:41]:** Russia just has this massive advantage in scaling against Ukraine itself. Ukraine has financial assistance from the EU, but Right now Ukraine is ahead in the drone race

**Yaroslav [01:33:54]:** I'm not sure about that by the way.

**Brandon [01:33:56]:** Is that I was Well, that was going to be my next question. Is that true? And if it is true, how long before Russia manages to pivot, course correct, and regain the lead?

**Noah [01:34:05]:** Sorry. For my own curiosity, can we define drone race?

**Yaroslav [01:34:09]:** Look, I think it's also for our listeners It's helpful to understand that there are

**Yaroslav [01:34:17]:** At least 30 different types, categories of drones, right? Like you have If you, if you, first you have like different domains. You have flying drones, ground vehicles, and you have sea vehicles, and you have undersea vehicles, right? Then for each of those domains, you have multiple use cases. Like for ground vehicles, you have logistics, evacuation, mining, de-mining

**Yaroslav [01:34:48]:** Like maybe something else. For aerial, you have reconnaissance, front strike, mid strike, deep strike, mining, de-mining, radio repeating, kamikaze and bombing, ISR, different types of surveillance, so tactical surveillance, operational level surveillance, maybe strategic level surveilla surveillance at some point.

**Yaroslav [01:35:17]:** Logistics also with aerial drones. For sea drones, same thing. So In each of those categories, you have Dozens, sometimes over 100 companies, and products which compete. So that's the current Ukrainian, battlefield. From the Russian side, it's less of a zoo, as we say. So they, in each category, they usually have one to maybe three products, and then they scale it sort of in a centralized fashion. And then so when you talk about whether we are behind or who's behind or ahead in drone warfare You got to analyze

**Brandon [01:36:04]:** It's asymmetric, so it's hard to compare

**Yaroslav [01:36:05]:** Sort of area by area, right? So if you're like talking about their front strike, I would argue that Ukraine has gotten ahead recently with after scaling the fiber optic. Before that Russia was slightly ahead. So Ukraine got ahead. With like mid strikes, so say something like 40 to 200 kilometers

**Yaroslav [01:36:35]:** It's hard for me to judge. At some point Russia was ahead. I think maybe we're getting ahead as well, and deep strike we recently got ahead, so we were we were doing more damage to Russia with deep strike drones than they're doing to us. In sea drones, we're consistently ahead, always were ahead. In ground drones, I think we're ahead. Yeah, I think like on

**Brandon [01:37:00]:** Where are they still ahead?

**Yaroslav [01:37:01]:** In general, I think we're ahead. Where they, where they are still ahead? I think in certain parts, -Of the components, like A GPS free or navigation like these CRPA antennas are pretty good. They have, these, winged, bombs that they drop from their bomber planes.

**Yaroslav [01:37:33]:** I forgot the English name for it.

**Brandon [01:37:34]:** Glide bomb?

**Yaroslav [01:37:35]:** Sort of. Yeah. So they're ahead on that side, and it's like it's difficult to protect from those.

**Brandon [01:37:42]:** What's the range of that?

**Yaroslav [01:37:45]:** It can be pretty big. I think it's like, can be up to 80 kilometers. Then obviously the range-

**Brandon [01:37:52]:** From like a fighter plane, like a strike?

**Yaroslav [01:37:54]:** The range is a very iffy subject here because the range is

**Yaroslav [01:38:01]:** Is like basically the distance from where you drop the bomb to where it lands, but also you drop it from a fighter plane, and then fighter planes are susceptible to aerial interceptor missiles. So on our side, we have our own fighter planes, and we have the ground anti-air systems. And then, and then those two assets, they have their radars and radar fields. And then, depending on the enemy tactics, you can, calculate how big is the aerial area that you cover with those assets. And look, I'm not a professional military guy, so I'm covering these topics in a in layman terms. Don't quote me on this. I'm just trying this to make this as understandable to an average listener as possible.

**Brandon [01:38:50]:** Helicopters. I've recently seen reports of drones taking out helicopters in the air, and that this is new.

**Brandon [01:39:00]:** Is that new? Is that going to be a big deal? Is that going to incre like, is that going to eventually get rid of helicopters the way drones are getting rid of tanks in the battlefield?

## Helicopters, Drone Carriers, and Future Air Defense

**Yaroslav [01:39:10]:** Look, helicopters are also versatile assets. Front strike helicopters, I think we're going to be seeing fewer and fewer of them. These few Russian helicopters that Ukraine's intercepted with drones were more like edge cases than a systematic, sort of helicopter hunting campaign. I think it is possible to turn it into a systematic, countermeasure against helicopters.

**Brandon [01:39:38]:** What kind of Will those be battery powered drones themselves, do you think?

**Yaroslav [01:39:41]:** Potentially. And there are like so many different scenarios. Like you can have large aerial drone carriers carrying interceptor drones.

**Brandon [01:39:54]:** That then go hit the helicopters.

**Yaroslav [01:39:56]:** For example. Or you can have, battery powered interceptor drones, but not of a missile with a propeller type, as many of these well-known drones like Stinger or P-One Sun. They look like basically a missile with a quadcopter, behind it. But you can also have a plane or like fixed wing like, aerial interceptors.

**Brandon [01:40:25]:** Does anyone, does anyone have like a little like, drone that flies super low under the helicopter and like shoots it from underneath?

**Yaroslav [01:40:33]:** Like in theory you can imagine that but it's just

**Brandon [01:40:37]:** Or like surface, a drone that carries surface-to-air missiles somehow.

**Yaroslav [01:40:40]:** I don't think that's very practical because whatever you have going on land will be just super slow and not fast enough to be able to hunt down a helicopter.

**Brandon [01:40:50]:** I mean like in the in the air. Is it, is are is there a drone capable of carrying a small surface-to-air missile that can like skim, low and then launch its little missile, like a flying missile platform or something?

**Yaroslav [01:41:00]:** In theory, but like a big part of a mission like that is not just kinetically getting to a helicopter, but also identifying it, either by means of first radar and then visually, and placing the asset you have, the interception asset you have in the right place in the right time. So the combination of those things is much more complex than just, how can we strike it like from behind or from below. But then helicopters are not, that does not mean they're becoming like completely useless. Like for example, helicopters are used to intercept, deep strike drones. Like Ukraine uses a lot of helicopters to shoot down Shaheds.

**Yaroslav [01:41:44]:** Russia uses helicopters to shoot down our deep strike drones.

## Counter-Drone Systems: Shotguns, EW, and Surviving FPVs

**Brandon [01:41:50]:** A lot of people talk Oh, so Some ideas about drone countermeasures, things people do technologically to try to shoot down FPV drones or bomber drones or whatever.

**Brandon [01:42:03]:** Dumb question that I probably already know the answer to but for the listeners, why can't you use a shotgun? Shoot down drones that are coming after you. When you have like a Why can't you just shoot the thing?

**Yaroslav [01:42:11]:** That's the main, weapon that people use against them.

**Brandon [01:42:15]:** Why aren't they very good?

**Yaroslav [01:42:17]:** They're pretty good. Like there are there are like hundreds, maybe thousands of cases of drones being shut down with shotguns, both by definitely thousands, but both by Ukrainians and Russians. There's even like statistics of

**Brandon [01:42:29]:** Got it

**Yaroslav [01:42:29]:** What is the percentage of Ukraine FPV drones that didn't accomplish the mission because they were shut down by a shotgun.

**Brandon [01:42:35]:** Got it. So if I'm a guy with a shotgun, I'm walking around, FPV drone comes for me

**Yaroslav [01:42:40]:** I don't recommend that.

**Brandon [01:42:42]:** No. I don't plan on it.

**Brandon [01:42:44]:** I'm saying suppose that were the case. In or suppose there's a there is a guy, he's not me.

**Brandon [01:42:50]:** He's dumber than me, okay? He's got a shotgun, he's walking around. FPV drone is sent. Someone says, "Okay, there's a guy walking around. Kill him. FPV drone go."

**Brandon [01:43:00]:** FPV drone goes after him. And he has a shotgun.

**Brandon [01:43:03]:** What are his chances of using that shotgun to shoot down the drone before the drone gets him? Can Is Are you allowed to say that?

**Yaroslav [01:43:08]:** Depending how good you are with a shotgun. I'll tell

**Brandon [01:43:11]:** Random dude

**Yaroslav [01:43:11]:** Like I was I was talking to some Ukraine pilot group, and they told me like there was this Russian guy. He was just likeRambo.

**Yaroslav [01:43:20]:** He's like, he like, he shot down like seven FPV drones. They couldn't, they couldn't get him. They finally got him, but it was like nothing they've seen before, right?

**Brandon [01:43:30]:** Got it.

**Brandon [01:43:30]:** Your average non-Rambo.

**Yaroslav [01:43:32]:** Average non-Rambo will just die.

**Brandon [01:43:34]:** Will just die. So there's like very low chance that they'll be able to use a shotgun to shoot down the drones.

**Yaroslav [01:43:38]:** Rather low chance. Yeah.

**Brandon [01:43:39]:** Got it. Well, that was the kind of question I was getting at and there's no, there's no sort of portable electronic countermeasure that can get FPV drones if you're just holding it, very effectively.

**Yaroslav [01:43:50]:** There are plenty of it just, depends on it's always like Electronic countermeasures are used all across the front line. The tricky thing is electronic countermeasures cover certain, radio electronic bands of frequencies.

**Brandon [01:44:06]:** Let me simplify my question. Sorry.

**Yaroslav [01:44:07]:** Like each side tries to tries to find frequency Will not be covered.

**Brandon [01:44:10]:** Let me simplify my question. Is there a man portable system that will give me a greater than 50% chance of living if an FPV drone specifically targets me to come kill me right now?

**Yaroslav [01:44:21]:** Look, if your system jams the frequency the drone works on and the drone doesn't have optic fiber or a last mile autonomy, then you have 100% chance that it will, it will not fly towards you. But then what is the chance to not have drone that can either use different frequency or autonomy or fiber optic? Well, that depends on the on the area you're in and who's your adversary in that area, in that zone.

**Brandon [01:44:51]:** Let's I guess this question was maybe too dumb that I was trying to ask.

**Yaroslav [01:44:57]:** No, it's a great question. There are no dumb questions here, and it is just like my answers, if you feel the common theme here, is that things in practice, in war, things are way more complex than they seem.

**Brandon [01:45:11]:** What, but so I want, like, I want I've read tons of things that say that basically if you're walking around in the open and drones come for you're not 100% dead, but you're probably dead, and I've read a bunch of things that say that. I want Listeners to understand why, like, people, who are paying a tiny bit of attention to this debate, to this issue from far away intermittently in America, who don't, I think don't understand the weakness of our military against this kind of attack Against drone attack.

**Yaroslav [01:45:48]:** I think there was I

**Brandon [01:45:49]:** Have a lot of mechanisms, psychological mechanisms by which they cope with the mental idea of drones. I would like to bust those mechanisms by explaining why drones defeat in human infantry on the battlefield.

**Yaroslav [01:46:01]:** It's just A guided bomb flying at you, and it knows exactly where you are right? It's not that it's the ultimate weapon, but I think like one of the things that went viral in Ukrainian defense tech bubble, even before the words of the CEO of Rheinmetall, was some American, tank, battle tank pilot, who was interviewed and he was he was asked whether he's afraid of FPV drones, and he's like, "No, it's like we have Our tanks are strong." And that went viral among Ukrainians because they're like, "Dude, you have no idea what you're talking about." Like, "Don't mess with those drones."like, Abrams tank, great tank, but against an FPV drone, sorry, dude, but it'

**Brandon [01:46:54]:** Not just deadly

**Yaroslav [01:46:54]:** Not going to work.

**Brandon [01:46:55]:** Deadly.

**Yaroslav [01:46:55]:** No, I was like, maybe not from one drone, but like a dozen drones will take it out. So yeah. But there is hope. So you just have to have kinetic countermeasures. Interesting thing-

**Brandon [01:47:10]:** Kinetic countermeasure means a thing that shoots down the drone.

**Yaroslav [01:47:13]:** Can mean many things. So if you, if you go to Ukrainian east and sort of territories close to the front lines, I think like about 50 kilometers in from the front line, all the roads are covered by fish nets.

**Yaroslav [01:47:31]:** You literally, you ride in a corridor of fish nets, and that's the mechanical countermeasure against the drone.

**Brandon [01:47:39]:** You count that as a kinetic countermeasure?

**Yaroslav [01:47:41]:** Mechanical. It says mechanical. Yeah.

**Brandon [01:47:42]:** Got it. Got it.

**Brandon [01:47:43]:** I don't know all the jargon, so it's, I'm, I'

**Yaroslav [01:47:45]:** Whatever.

**Brandon [01:47:45]:** What I'm talking about.

**Yaroslav [01:47:46]:** Whatever. Then the tanks, if you look at Russian tanks and sometimes Ukrainian tanks or equipment They all look like Porcupines. They have these long sticking, I don't know, poles? We talked about poles already on this podcast.

**Brandon [01:48:05]:** Different kind of poles.

**Yaroslav [01:48:05]:** Different kind of poles.

**Brandon [01:48:06]:** A third kind of poles.

**Yaroslav [01:48:06]:** That's the way to protect from drone. That's to make to that's the way to make the drone detonate, maybe half a meter or a meter away from the actual shell of the tank. Or yeah, sometimes there are like nets on top of these tanks, just welded on some extra, sort of equipment. Then of course, there are guns That

**Yaroslav [01:48:35]:** Like what both Russians and Ukraine or Ukrainians are beginning to experiment with is Kind of interceptor drone, anti-FPV interceptor drone, which you put on top of something like a gun, like harpoon sort of thing, and when you see like a drone coming at you, maybe you can notice or hear it from 200 meters or 100 meters. So you have a couple of seconds, and you grab that thing, you point it, and you fire it, and then onboard it has certain AI that helps it to guide the small drone towards an attacking drone and intercept it that way. So those are the things that are being developed and like, we're working on some of these things as well, and then you can imagine like an armor with -Hundreds on of drones on top of it, which are protector drones. They're sort of like active armor. Whenever they see a drone-

**Brandon [01:49:27]:** Huh

**Yaroslav [01:49:27]:** Coming at you, they, like, take off.

## Lasers, Skynex, and the Cost-to-Effect Problem

**Brandon [01:49:29]:** That's cool. What about, what about the kind of things that the Germans are building, which is basically like a big truck with a some sort of automated shotgun on it?

**Yaroslav [01:49:40]:** Like they have Skynex. It's, by Rheinmetall, by the guy whom we mentioned today. Skynex is considered to be an okay weapon. Their shots are quite expensive though. So I'll tell you this different story, about

**Brandon [01:50:00]:** It's about cost to fire each shot really and stuff.

**Yaroslav [01:50:03]:** Cost to effect in a sort of a more abstract way. So I was last year I was speaking at Land Europe Conference. It's the biggest USAA, USA Army, conference in Europe, called Land Europe. And There was an expo there, and there was like a Raytheon, a RTX booth there. And Raytheon is an amazing company. Gosh, we love Raytheon. They're making Patriots. Patriots are the best. And they make a bunch of other things. And they had this laser gun project there basically.

**Brandon [01:50:44]:** That's what I was going to ask about next is laser.

**Yaroslav [01:50:46]:** Laser thing was like they have it in two variations, two kilowatt, sorry, 10 kilowatt laser and 20 kilowatt laser. I'm like, "Okay, 10 kilowatt laser, tell me about it." He's like, "Can it take down an FPV drone?" I'm like, "Yes, of course it can." I'm like, "Okay, cool. How much time does it take to take down an FPV drone?" And they're like, "Well, maybe three seconds." I'm like, "three seconds. That's like a lot of time. But okay, maybe fine. And what if FPV drone tries to evade, right?" And he's like, "Well, we will retarget it again." And it's like, "And then three seconds start again?""Yeah.""Okay. Well, can it take down like a dozen FPV drones?" They're like, "Yeah, for sure." I'm like, "Okay, a dozen FPV drones, 30 seconds? Maybe, yes. Two kilometers? Maybe yes, maybe no." And I'm like, "Okay, how much does it cost?" And he said something like $3 million or something like that.

**Yaroslav [01:51:44]:** I'm like, "Okay, $3 million. So that is 6,000 FPV drones.

**Yaroslav [01:51:51]:** I doubt this thing will be able to handle 6,000 FPV drones or even 600 FPV drones coming at it at the same time." So you have this kind of economic. And this product may not be necessarily a product against an FPV drone. It might Or against an FPV drone in an active battlefield environment. It might be guarding a stadium in a peaceful country. And then, some random dudes launch a couple drones above a stadium, shoot them down. Okay, everyone's happy, although the drone will fall down, maybe fall on someone's head. That wouldn't be cool. So you would want something like catching bad drones with a net above a stadium or something like that. But whatever.

**Yaroslav [01:52:33]:** My point is the economics matters

**Brandon [01:52:35]:** You're talking about the 6,000 drones. If you sent them one by one, it wouldn't, it would just be pew.

**Yaroslav [01:52:40]:** But who would send them one by one?

**Brandon [01:52:40]:** If you sent a mass of 6,000, it wouldn'

**Yaroslav [01:52:42]:** Of course, yeah.

**Brandon [01:52:46]:** What about just like a more powerful laser, like 100, kilowatt laser or something that wouldn't need to spend, that would

**Yaroslav [01:52:51]:** No, that's worse. You need less powerful laser that achieves the same effect.

**Brandon [01:52:56]:** For cost of the system.

**Yaroslav [01:52:56]:** A more powerful, yeah, a more powerful laser would be more expensive, heavier, more difficult to transport. It will be more difficult to make many of them. And therefore you wouldn't be able to cover a long front line, and would be super expensive to replace if it gets damaged, all of those issues. So the reason why FPV drones or iPhones become so popular is because they're small and everyone can have one? And so is with the countermeasures. So that's, you were asking me about sort of policy advice. So that's like another sort of mental shift that you got to go through. It's no longer about an aircraft carrier that costs whatever, $14 billion and takes forever to build. It's about mass, that is you can iterate on very quickly. You can upgrade it. Everyone can operate it. And then that mass when it is combined or the technologies when they're, extrapolated from like one domain to another domain, they add up, right, as it happens with software. So I think that's important.

**Noah [01:54:14]:** Can I ask a follow-up question? So Russia is not necessarily the smartest army you could be fighting. What would happen if you, your adversary was smarter? Do you think things would change meaningfully?

**Yaroslav [01:54:31]:** Look, I don't know if I fully agree with not the smartest army. Who is the smartest army?

**Brandon [01:54:37]:** Ukraine?

**Noah [01:54:38]:** That's a great question.

**Yaroslav [01:54:40]:** I don't know. I don't know.

**Yaroslav [01:54:43]:** I think those are like, very dangerous assumptions to make.

**Brandon [01:54:48]:** Who was the smartest army in World War I?

**Yaroslav [01:54:51]:** Like, well, define smart.

## Russia's Strategy, Western Assumptions, and Preparing for War

**Brandon [01:54:53]:** The United States. Yeah.

**Yaroslav [01:54:53]:** Why do you think so?

**Yaroslav [01:54:55]:** Why do you think Russia is not the smartest army?

**Noah [01:54:56]:** Maybe this is just my own, information bubble.

**Yaroslav [01:55:00]:** I'm just like, maybe I agree with you. But I'm just like, I'm naturally wired To challenge those assumptions.

**Noah [01:55:06]:** No, that's a that's a really good point. I guess, when I, from my information bubble, it seems like Russia's strategy has largely been to just throw resources, people-

**Yaroslav [01:55:17]:** You are living in a Western propaganda Information bubble, of course.

**Yaroslav [01:55:21]:** Like, as am I.

**Yaroslav [01:55:22]:** Like, because we're all rooting Ukraine to win, right? Sorry, go on.

**Noah [01:55:26]:** In but going back to this granted there's a history of large powers failing to take over smaller, -Strategically, you

**Yaroslav [01:55:38]:** Divide and Goliath

**Noah [01:55:40]:** They, this

**Brandon [01:55:40]:** They fail a lot more now than they used to. The success rate of taking-

**Noah [01:55:44]:** That's true

**Brandon [01:55:44]:** Places over has gone way down.

**Noah [01:55:46]:** Certainly, yeah. But regardless, it does, I do wonder, like, if Russia had not essentially assumed victory early It may have different, yeah

**Yaroslav [01:55:56]:** I, like, they're super stupid, of course.

**Yaroslav [01:55:58]:** Like, they were marching at With their parade, costumes and like, they were thinking they're going to have a parade in Kyiv in a few days. Like, that was super stupid. And like, there were lots of stupid things that are like they have no regard, no care for human life. They're sending those Russian folks just, like, without armor, without anything, like folks on crutches, like sending them to storm Ukrainian positions. And it's

**Brandon [01:56:23]:** They're the Zerg.

**Noah [01:56:23]:** You think at this point there's

**Yaroslav [01:56:24]:** I have, like, I have actually a good friend. He's American. He's from Seattle. He's, served, had been in the Special Forces here in the US, had been in maybe three deployments, and then went to Ukraine, volunteered.

**Yaroslav [01:56:39]:** He's been fighting since, like, 2022. He's a very good friend of mine. So at some point he's like, he's been texting me, and he's like, "Okay, I'm near Pokrovsk,"and sorry, not Pokrovsk. It was gosh, the other city, Chasiv Yar.

**Yaroslav [01:56:55]:** It, and he's like, "Okay, so what Russians are doing, they're just creating so much work for all the all the psychologists who are going to heal those Ukrainian, whatever, riflemen or machine gunmen, who are just, like, shooting at the Russians who are like, going nonstop,"right? So it's like causing, or Russians are causing psychological trauma on Ukrainians because they're dying in such stupid way.

**Noah [01:57:26]:** Jeez

**Yaroslav [01:57:26]:** That is indeed stupid of sort of Russian higher command, et cetera, et cetera, et cetera. But then that's the resource they have. And

**Brandon [01:57:38]:** If you've got, if you've got Zerglings, you use your Zerglings.

**Yaroslav [01:57:40]:** That's the way. That's their strategy. That's their way of strategy, right?

**Brandon [01:57:43]:** If you're going to play Back in the That's what you do.

**Yaroslav [01:57:46]:** If you play StarCraft, that's how Zergs win.

**Brandon [01:57:48]:** Are Ukrainians the Terrans?

**Yaroslav [01:57:52]:** I don't know. I hope we will become Protoss soon.

**Yaroslav [01:57:57]:** I'm working on that. I'm working on that.

**Brandon [01:58:02]:** Protoss had fairly bad political management at the top

**Yaroslav [01:58:04]:** I wish Protoss with a speed closer to like, humans or Terrans, whatever it is. Hopefully we can do Protoss technology with a Zerg speed. That would be the best. I think that's what the housewives are working on in fact.

**Brandon [01:58:20]:** You cannot beat those housewives. Do not oppose Ukrainian housewives.

**Yaroslav [01:58:23]:** Do not mess with Ukrainian housewives, for sure. Yeah.

**Noah [01:58:26]:** Two final questions. First one, you started out by telling us a story about going to a chapel on February 23rd.

**Noah [01:58:34]:** Were you able to get married there? Can you finish that story?

**Yaroslav [01:58:40]:** We actually, we did get married, but we postponed the wedding as a social event, until the war is over.

**Noah [01:58:49]:** Then last question, what do you want our audience to take away? If you have one point you want them to walk away with what would it be?

**Yaroslav [01:58:58]:** You want peace, be prepared for war. Got to invest in defense and security.

**Noah [01:59:04]:** All right. Thanks. Thank you for talking with us.

**Yaroslav [01:59:06]:** Thank you.

**Noah [01:59:07]:** Thank you, Noah, for all the great questions.

**Yaroslav [01:59:11]:** No, it was fantastic.

**Yaroslav [01:59:12]:** Thanks so much.

**Brandon [01:59:13]:** Really fun.

**Noah [01:59:13]:** Awesome. Thanks.

---

## [[AINews] Cerebras' $60B IPO: Slowly, then All at Once](https://www.latent.space/p/ainews-cerebras-60b-ipo-slowly-then)
*🔬 Latent Space | 2026-05-16*

We normally focus on technical stories, but occasional large fundraisings are noteworthy in themselves, and the Cerebras IPO (after one [pulled S-1](https://www.youtube.com/watch?v=7UGjf080qag) and a fantastic [750MW partnership](https://openai.com/index/cerebras-partnership/) and [$10-$20B stake/deal](https://www.reuters.com/technology/openai-spend-more-than-20-billion-cerebras-chips-receive-equity-stake-2026-04-17/) with OpenAI) this week, certainly qualifies as a growing theme supporting [the Inference Inflection](https://www.latent.space/p/ainews-the-inference-inflection), just 6 months after [the shock execuhire of Groq by NVIDIA for $20B](https://news.smol.ai/issues/25-12-24-nvidia-groq).  ended today at $280, a market cap of $60 billion, which is tremendous validation for [Big Chip](https://x.com/vikramskr/status/2054264737400328678?s=12) and [their believers](https://x.com/shenlucinda/status/2055033736031592843?s=12).

This image [from Amir Efrati](https://x.com/amir/status/2054940414688494029?s=12) summarizes the Decade of Cerebras:

[](https://substackcdn.com/image/fetch/$s_!vBnf!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F5fea6bb8-3298-434e-afef-3eea148ba10c_2048x1263.png)

Cerebras' [financials](https://x.com/negligible_cap/status/2045239088169828550?s=12) are now fully public, but the focus of discussions center around the supply:

More details below, and the Head Research Scientist of Cerebras speaks at AIE Singapore later today on the livestream:

> AI News for 5/14/2026-5/15/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

## **Headline Story: Cerebras IPO recap, technical details, and company journey**

**Cerebras returned to the timeline as an IPO story, with investors and adjacent infra voices framing the company as a long-running contrarian hardware bet that finally looks vindicated.** The most directly relevant tweet is from investor Ishan N. Taneja, who said he "didn't believe" early Cerebras claims, then concluded the skeptic he doubted "was totally right," praising Cerebras for persistence, execution, and for having "built a banger chip," while noting this was Hanabi's first IPO [@ishanit5](https://x.com/ishanit5/status/2055000270837543052). A second Cerebras-specific datapoint came from CNBC's Deirdre Bosa quoting Cerebras CFO Bob Komin pushing back on the "small models only" narrative: Komin said Cerebras serves models of all sizes, that there is "no limit" to the size of models it can serve, and that Cerebras is currently serving **trillion-parameter models** , including internal OpenAI models, specifically naming **" OpenAI 5.4 and 5.5"** [@dee_bosa](https://x.com/dee_bosa/status/2055351401472020949). A nearby contextual tweet from Apoorv Vyas explicitly linked "the Cerebras IPO" to a Stanford discussion on compute scarcity, inference demand, routing, and open source, suggesting the IPO was being interpreted not as a generic capital-markets event but as part of the inference infrastructure cycle [@apoorv03](https://x.com/apoorv03/status/2055479206545646040).

## **Facts vs. opinions**

### **Facts directly stated in tweets**

  * Cerebras is being discussed in the context of an **IPO** [@ishanit5](https://x.com/ishanit5/status/2055000270837543052), [@apoorv03](https://x.com/apoorv03/status/2055479206545646040).

  * Cerebras CFO **Bob Komin** said:

    * Cerebras serves **all model sizes**.

    * There is **" no limit"** to model size it can serve.

    * Cerebras is serving **trillion-parameter models**.

    * It is serving **internal OpenAI models** , specifically **OpenAI 5.4 and 5.5** [@dee_bosa](https://x.com/dee_bosa/status/2055351401472020949).




### **Opinions / interpretations**

  * Cerebras "did controversial things for the right reasons," "the team slaps," and "they built a banger chip" are investor judgments, not independently verified facts [@ishanit5](https://x.com/ishanit5/status/2055000270837543052).

  * The implication that the IPO is a validation of Cerebras's long-term strategy is an interpretation emerging from the investor tone and surrounding infra discourse, not a formal claim from the company in these tweets.

  * The CFO's claim that there is "no limit" to model size is partly factual framing and partly marketing language; engineers should read it as "the company believes its serving architecture scales to current frontier workloads," not literally unbounded compute.




## **Technical details and numbers surfaced in the discussion**

The tweet corpus is light on historical specs, but it does contain several notable **operational claims** relevant to Cerebras's technical positioning:

  * **Trillion-parameter model serving** : Cerebras CFO says the company is currently serving trillion-parameter models [@dee_bosa](https://x.com/dee_bosa/status/2055351401472020949).

  * **Named customers/workloads** : Komin specifically says these include **internal OpenAI 5.4 and 5.5** [@dee_bosa](https://x.com/dee_bosa/status/2055351401472020949).

  * **Strategic wedge** : The framing is clearly **inference/serving** , not just training. Apoorv ties the IPO discussion to "compute scarcity," "rising inference demand," and "model routing" [@apoorv03](https://x.com/apoorv03/status/2055479206545646040).




Those tweets align with Cerebras's broader known positioning in the market: wafer-scale hardware, extreme on-chip memory bandwidth, and system architectures optimized to reduce the bottlenecks that appear when serving large models with low latency. Even though those specific chip specs are not in the tweet set, the CFO's "trillion-parameter" comment is technically meaningful because it implies the company wants to be understood as a serious serving platform for frontier-scale models, not a niche accelerator for mid-sized open models.

## **Cerebras 's journey: why this IPO resonated**

Cerebras has spent years in the "ambitious but contentious" bucket in AI hardware. The investor comment captures the core narrative arc well: the company took a path that many found implausible or commercially dubious, but did so with persistence and enough execution to stay alive through multiple compute cycles [@ishanit5](https://x.com/ishanit5/status/2055000270837543052).

The subtext of that praise is important for hardware engineers:

  * Cerebras has long represented a **non-NVIDIA architectural thesis**.

  * Its strategy has been to attack the scaling problem with a **different physical and system design philosophy** , rather than merely competing on conventional accelerator economics.

  * That made it inherently controversial, because the market often discounts bespoke architectures unless they win a very specific workload.




The IPO recap chatter suggests the company's story has shifted from "can this architecture survive?" to "is this exactly the kind of differentiated serving stack the market now needs?"

That shift is happening because the AI infra market has also shifted:

  * From pure training prestige toward **inference economics**.

  * From benchmark snapshots toward **serving giant models in production**.

  * From GPU abundance assumptions toward **compute scarcity and routing discipline** [@apoorv03](https://x.com/apoorv03/status/2055479206545646040).




In that environment, a company that can credibly say it serves **trillion-parameter internal frontier models** gets a very different hearing than it would have a few years ago [@dee_bosa](https://x.com/dee_bosa/status/2055351401472020949).

## **Different perspectives**

### **Supportive / bullish**

  * The most bullish take is from investor Ishan N. Taneja: skepticism gave way to admiration, with emphasis on **persistence** , **execution** , and a **successful contrarian chip bet** [@ishanit5](https://x.com/ishanit5/status/2055000270837543052).

  * Bob Komin's quote is also strategically bullish: it reframes Cerebras as a platform for **frontier-scale inference** , not a side player [@dee_bosa](https://x.com/dee_bosa/status/2055351401472020949).

  * Apoorv's comment places Cerebras in the center of a live systems question--**compute scarcity amid rising inference demand** --which is where a differentiated serving architecture could matter most [@apoorv03](https://x.com/apoorv03/status/2055479206545646040).




### **Neutral / analytical**

  * A neutral read is that Cerebras's IPO matters less as a public-markets event than as a signal that investors believe there is room for **non-GPU-default infra companies** in the frontier stack.

  * Another neutral takeaway: even if Cerebras has genuine technical differentiation, the important question is not "is the chip elegant?" but "can it sustain utilization, software compatibility, and commercial adoption in a market increasingly organized around incumbent ecosystems?"




### **Skeptical / implicit counterpoints**

No tweet in the supplied set directly attacks the Cerebras IPO. But there are implicit reasons an expert audience would remain cautious:

  * "No limit to model size" is standard executive rhetoric; in practice, limits show up in **memory hierarchy, batch/latency tradeoffs, interconnect behavior, software ergonomics, and workload mix**.

  * Serving internal OpenAI workloads is a strong claim, but without details on **share of traffic, latency tier, cost/token, utilization, or exact deployment role** , it is hard to know whether this reflects broad strategic reliance or narrower targeted usage.

  * The history of AI hardware is full of technically impressive architectures that failed commercially because software, developer adoption, or ecosystem gravity overwhelmed raw hardware merit.




## **Why it matters now**

The Cerebras IPO story lands at a moment when AI infra is being repriced around a few hard truths visible elsewhere in the tweet set:

  * **Inference is becoming the dominant compute market**. Pearl, Together, and others are explicitly talking about inference economics and token costs [@prlnet](https://x.com/prlnet/status/2055339314205139226), [@simran_s_arora](https://x.com/simran_s_arora/status/2055348155051569474).

  * **Serving giant models is now a product requirement** , not just a lab flex. Multiple tweets discuss trillion-scale models, large-model cadence, and rapid RL/post-training-driven improvements [@scaling01](https://x.com/scaling01/status/2055018330365345896), [@kimmonismus](https://x.com/kimmonismus/status/2055197338092662824).

  * **Capital intensity is under scrutiny**. Kimmonismus notes hyperscaler capex crossing **$600B** and a large gap between AI infra spending and AI revenue, warning that the market is watching infra economics closely [@kimmonismus](https://x.com/kimmonismus/status/2055293526125232332).




In that context, Cerebras matters if--and only if--it can make a durable case that a nonstandard architecture can improve the economics or latency profile of frontier inference enough to justify ecosystem switching costs.

## **Broader context: official claims vs independent validation**

Officially, the strongest claim in the tweet set is from CFO Bob Komin: **Cerebras already serves trillion-parameter OpenAI internal models** [@dee_bosa](https://x.com/dee_bosa/status/2055351401472020949).

What is missing from the tweet set is independent benchmark-style validation:

  * no cost-per-token comparison,

  * no latency percentile data,

  * no throughput numbers,

  * no context-length specifics,

  * no software compatibility details,

  * no utilization figures.




So the right technical posture is:

  * treat the OpenAI-serving claim as **important and credible enough to watch** ;

  * do **not** overread it as full proof of broad superiority.




The IPO recap, then, is less "Cerebras won" and more "Cerebras stayed alive long enough for the market to become more favorable to its thesis."

# **AI Twitter Recap**

**Codex, GitHub Copilot App, and the New Coding-Agent Surface Area**

  * OpenAI's Codex mobile/app rollout dominated product chatter. Users described building websites from a bar, controlling Macs from iPhone, and treating laptops as "satellite devices" while an always-on Mac mini runs sessions in the background [@flavioAd](https://x.com/flavioAd/status/2055021982601605225), [@nickbaumann_](https://x.com/nickbaumann_/status/2055066537002725393), [@PaulSolt](https://x.com/PaulSolt/status/2055057277334208987), [@rileybrown](https://x.com/rileybrown/status/2055093278161428726).

  * **Codex is rapidly becoming a multi-surface agent platform** : tweets this cycle point to a meaningful broadening of where and how coding agents run: mobile-first workflows via [Codex Mobile walkthroughs](https://x.com/rileybrown/status/2055093278161428726), iPad/VPS session management from [@npew](https://x.com/npew/status/2055131618789265779), Telegram/home-server remote setups from [@itsclivetime](https://x.com/itsclivetime/status/2055144998270824515), and hints of "locked use" for Mac control while the machine is locked from [@kimmonismus](https://x.com/kimmonismus/status/2055262250701574359). OpenAI's dev team also shared adoption figures via [@etnshow](https://x.com/etnshow/status/2055220392030278100): **4M+ weekly active users** , **5x more messages per user** , and **1M+ app downloads in the first week**.

  * **The surrounding ecosystem is moving quickly to plug into Codex rather than compete only at the app layer** : [Ollama added Codex app support](https://x.com/ollama/status/2055100589428658462) with local/open-model launch paths and cloud model recommendations; [Zed now supports ChatGPT subscription access in its agent](https://x.com/zeddotdev/status/2055335727483781624), preserving the same subscription/rate-limit model as Codex; and third-party extensions are appearing, including [MagicPath as a native canvas inside Codex](https://x.com/skirano/status/2055364115560878480) and a portable `/goal` command extracted into MCP/slash-command form by [@secemp9](https://x.com/secemp9/status/2055339137318724047). Community momentum was visible in meetup reports from [London](https://x.com/Andy_AJT/status/2055297191128768576), [Portugal](https://x.com/TimHaldorsson/status/2055206416747507785), and [Paris planning](https://x.com/borvibe/status/2055322241340960810).

  * **GitHub is making a parallel bet on the coding harness, not just the model** : the VS Code/Copilot team emphasized that the user experience is shaped by the **coding harness** --context assembly, tool use, execution loops, memory--more than by the base model alone in [their behind-the-scenes post shared by @code](https://x.com/code/status/2055317356910367189) and [@pierceboggan](https://x.com/pierceboggan/status/2055322165969604966). Product features highlighted this week include **agent merge** from [@davidfowl](https://x.com/davidfowl/status/2055148986340905020), and **terminal risk assessment badges** with AI explanations for commands from [@code](https://x.com/code/status/2055408023506469337). The broader trend is clear: the competitive frontier is shifting from "best model" toward **best harness + UX + integrations**.




**Agent Harnesses, Search, Evaluation, and Reliability Engineering**

  * **Search for coding agents is being rethought around primitives, not embeddings** : the strongest thread here is the "grep/search over vector DBs" argument. [@omarsar0 highlighted](https://x.com/omarsar0/status/2055317577031975269) a paper showing **grep-style text search, wrapped in the right agent harness, can match or beat embedding-based retrieval on coding-agent tasks** ; [@dair_ai echoed the takeaway](https://x.com/dair_ai/status/2055318144592289847). Relatedly, [@lintool joked](https://x.com/lintool/status/2055316434171879757) that the "two-parameter model" for agentic search is **BM25** , and maybe the zero-parameter version is **grep**. This aligns with Cloudflare-adjacent experimentation too: [@YoniBraslaver compared SDK vs MCP on monday.com's GraphQL API](https://x.com/YoniBraslaver/status/2055260079700791544), finding **1 step / 15k tokens** for SDK versus **4 steps / 158k tokens** for a real MCP server--**8.4x token cost** for the same output.

  * **Agent evals and observability are becoming first-class infra problems** : several posts converged on the same theme that evals for autonomous systems are harder, not easier, as agents get longer-horizon and more tool-rich. [@palashshah](https://x.com/palashshah/status/2055410769387303004) called out the difficulty of modern eval design; [@cwolferesearch](https://x.com/cwolferesearch/status/2055437703823372728) compiled a broad benchmark map spanning **Terminal-Bench, Tau-Bench, GAIA, WorkArena, OSWorld, MLE-Bench, PaperBench, GDPval** , and others. New benchmark proposals included [FutureSim](https://x.com/ShashwatGoel7/status/2055336064378720412), which replays real-world events temporally to test continual updating and forecasting in native harnesses like Codex/Claude Code, and follow-up commentary from [@nikhilchandak29](https://x.com/nikhilchandak29/status/2055357580436783595) arguing that **test-time compute scales gracefully in forecasting** too.

  * **Reliability concerns are shifting from hallucinations to system-level failure modes** : [@random_walker](https://x.com/random_walker/status/2055271764662296580) argued that black-box "genie" interfaces increase the verification burden because users can't see reasoning traces, tool use, memory, or intermediate state. [@mitchellh](https://x.com/mitchellh/status/2055380239711457578) made the sharper infra analogy: companies may be drifting into an **" MTTR is all you need"** mindset for AI-generated software, creating resilient catastrophe machines where local metrics look fine while global system comprehensibility decays. On the tooling side, LangChain pushed the other direction with [Interrupt announcements](https://x.com/LangChain/status/2055314236050690086) covering **LangSmith Engine, SmithDB, managed Deep Agents, sandboxes, gateway, and context hub** , while [@ankush_gola11](https://x.com/ankush_gola11/status/2055368456342745098) emphasized **sub-second median write latency** for trace ingestion as a practical requirement for agent observability.




**Training, Optimization, and Inference Efficiency**

  * **Optimizer work is broadening beyond the Adam family again** : [@zacharynado](https://x.com/zacharynado/status/2055077098327285804) summarized the zeitgeist succinctly: the "sloptimizer" field is just getting started with **Shampoo** and **Muon-gen** style methods after the graveyard of Adam variants. Two concrete updates landed: [SODA](https://x.com/tmpethick/status/2055271381890138560), a wrapper that **adds no hyperparameters, removes weight-decay tuning, and improves a base optimizer** , with the notable claim that **SODA[Muon] beats Muon even when Muon gets a tuned weight-decay sweep** ; and general continued interest in Muon/Shampoo from replies and references.

  * **Fast/slow learning and pedagogical supervision were notable training ideas this cycle** : [@agarwl_ described "Learning, Fast and Slow"](https://x.com/agarwl_/status/2055081573083402434), combining **slow learning in weights via RL** with **fast learning in context/prompt ( "fast weights") optimized with GEPA**, claiming better data efficiency, adaptability, and less forgetting than RL alone. On the supervision side, [Pedagogical RL](https://x.com/NoahZiems/status/2055091478024565214) and [Late Interaction's explainer](https://x.com/lateinteraction/status/2055278862255185936) argue for learning not merely from correct outputs but from **correct, teachable rollout distributions** , while [@bradenjhancock summarized](https://x.com/bradenjhancock/status/2055079214156853325) related work on teacher models that are penalized for taking leaps students can't follow.

  * **Inference optimization remains highly active at both systems and model levels** : [@ariG23498 recommended a deep dive on continuous batching](https://x.com/ariG23498/status/2055106570971975977), specifically the need to understand **CUDA streams, events, synchronization, and CPU/GPU decoupling** to avoid idle GPUs in dynamic batching regimes. Meta researchers proposed [Self-Pruned KV attention](https://x.com/ManuelFaysse/status/2055214689613664303), where the model learns which keys/values to keep in persistent cache to reduce **KV cache size** and improve decoding speed. On the local inference side, [@danielhanchen reported](https://x.com/danielhanchen/status/2055274688025378854) that **Qwen small-model MTP GGUFs now run 1.8x faster** , up from **1.4x** two days prior, thanks to new llama.cpp speculative-decoding parameters.




**Open Models, Serving Stacks, and the Agent Toolchain**

  * **Open/local agent stacks are tightening around Hermes, Ollama, and portable runtimes** : [ClawRouter integrating Hermes Agent](https://x.com/ClawRou/status/2055078292567597253), [Teknium's claims of surpassing OpenClaw in token volume](https://x.com/Teknium/status/2055125356554899865), and [Grok support in Hermes Agent via SuperGrok subscriptions](https://x.com/Teknium/status/2055373314399650230) all point to continued consolidation around interoperable agent shells. NVIDIA published a practical deployment path to [run Hermes Agent locally on DGX Spark via Ollama](https://x.com/NVIDIA_AI_PC/status/2055317325444710872). [@onusoz](https://x.com/onusoz/status/2055120477648261502) also highlighted a major usability gap: **one-click local model deployment for end users still doesn 't really exist**, despite increasing demand.

  * **Serving infrastructure around open multimodal and scientific models continues to mature** : [vLLM highlighted Baseten's production deployment of vLLM-Omni](https://x.com/vllm_project/status/2055136943550427242) for **multi-stage audio, streaming multimodal, and real-time TTS** workloads often dominated by closed APIs. They also shipped [day-0 support for Intern-S2-Preview](https://x.com/vllm_project/status/2055148034124894395), described as an **open-source scientific multimodal foundation model** with an early capability in **material crystal structure generation**. Additional tooling updates included Hugging Face's call for [agentic kernel development in the kernels project](https://x.com/RisingSayak/status/2055187769266434101), and [Capa](https://x.com/acoyfellow/status/2055235076820971872), which turns **OpenAPI specs into Cloudflare service bindings** with **5,852 generated methods** across platforms like Stripe, GitHub, Slack, Twilio, and Kubernetes.

  * **Document/search infra also saw concrete product work** : [Weaviate v1.37](https://x.com/weaviate_io/status/2055276211681579242) added **per-property accent folding** , **per-property stopword presets** , and a **/v1/tokenize** endpoint for debugging BM25 tokenization. Cohere pushed [Compass](https://x.com/cohere/status/2055343638360752351) as a stack for retrieval over difficult documents using visual parsing plus search embeddings. On the benchmarking side, [ParseBench leaders Infinity-Parser2-Pro (35B) and Flash (2B)](https://x.com/jerryjliu0/status/2055405690538070340) were credited with **5M+ synthetic parsing samples** and a **joint RL algorithm** across document/element/chart parsing tasks.




**Anthropic, OpenAI, xAI, and Competitive Dynamics**

  * **The strongest competitive signal was around developer-product pressure, not just benchmark pressure** : [@Yuchenj_UW framed Anthropic's recent moves as "running the Codex playbook" after getting xAI GPU capacity](https://x.com/Yuchenj_UW/status/2055349045556814029), and the most visible user-facing change was [Anthropic resetting everyone's 5-hour and weekly Claude rate limits](https://x.com/ClaudeDevs/status/2055347539923308703), amplified by [@kimmonismus](https://x.com/kimmonismus/status/2055364277234528399) as a likely response to competition and/or increased compute availability. Separate reports from [@kimmonismus](https://x.com/kimmonismus/status/2055222524774846576) cited FT numbers putting **Anthropic valuation at $900B** and **ARR at $45B** by end of May, up sharply from earlier checkpoints.

  * **On model perception, several tweets point to widening domain specialization and frontier gaps** : [Epoch AI's domain-specific ECI](https://x.com/EpochAIResearch/status/2055349241300898273) suggests Claude has a **software-engineering advantage** relative to its own general capability index, but **under-indexes in math**. At the same time, multiple posters were impressed by **Claude/Mythos-level** capability jumps: [@scaling01](https://x.com/scaling01/status/2055362921803211248) called Mythos "insane," while [@teortaxesTex](https://x.com/teortaxesTex/status/2055330529583489406) said Mythos appears meaningfully stronger than GPT-5.5 in at least some use. The speculative next step on the xAI side is larger scale still: [@scaling01 expects a new ](https://x.com/scaling01/status/2055320443129581647)**[1.5T xAI model](https://x.com/scaling01/status/2055320443129581647)**[ soon](https://x.com/scaling01/status/2055320443129581647).

  * **OpenAI expanded the "ChatGPT as personal agent" thesis into finance**: [ChatGPT announced](https://x.com/ChatGPTapp/status/2055317612687675545) a **personal finance experience** for **Pro users in the U.S.** , with secure financial-account connections, spending analysis, and grounded Q&A over user-authorized data. [@fidjissimo](https://x.com/fidjissimo/status/2055384863155610068) tied it to the same pattern as health-record integrations: more structured personal context flowing into the agent. [@kimmonismus](https://x.com/kimmonismus/status/2055320528198521041) argued this could compress parts of the fintech assistant layer, citing internal finance benchmarks where **GPT-5.5 Thinking scored 79/100** and **GPT-5.5 Pro 82.5/100** on complex personal-finance tasks.




**Top tweets (by engagement)**

  * **Codex/agent adoption** : [ChatGPT personal finance preview](https://x.com/ChatGPTapp/status/2055317612687675545) was the highest-engagement directly AI-relevant product launch in the set.

  * **Developer rate limits as product signal** : [Claude resetting 5-hour and weekly rate limits](https://x.com/ClaudeDevs/status/2055347539923308703) drew major attention, likely because it directly affects developer throughput.

  * **Practical prompt-injection example** : [@tmuxvim's LinkedIn bio prompt-injection joke](https://x.com/tmuxvim/status/2055275374905307216) went massively viral and resonated because it maps cleanly onto current concerns about agent ingestion of untrusted text.

  * **Reliability backlash to AI-maximalist engineering culture** : [@mitchellh's "AI psychosis" thread](https://x.com/mitchellh/status/2055380239711457578) was one of the most substantive high-engagement posts, articulating a systems-engineering critique of "ship bugs, agents will fix them" thinking.

  * **Open-vs-closed/policy framing** : [Dan Jeffries' long thread against anti-open-source AI policy](https://x.com/Dan_Jeffries1/status/2055241272038691133) had unusually high engagement for a policy argument and reflects how export controls, open weights, and industrial policy remain deeply entangled with engineering discourse.




* * *

# **AI Reddit Recap**

## **/r/LocalLlama + /r/localLLM Recap**

[ Read more ](https://www.latent.space/p/ainews-cerebras-60b-ipo-slowly-then)

---

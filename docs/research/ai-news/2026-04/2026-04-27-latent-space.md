---
title: Latent Space — 2026-04-27
date: 2026-04-27
source: Latent Space
type: ai-news
---

# 🔬 Latent Space — 2026-04-27

> swyx 開發者簡報，未公開專案 + 工程視角
> 來源：[Latent Space](https://www.latent.space/feed)

---

## [Physical AI that Moves the World — Qasar Younis & Peter Ludwig, Applied Intuition](https://www.latent.space/p/appliedintuition)
*🔬 Latent Space | 2026-04-27*

From building [Applied Intuition](https://www.appliedintuition.com/) from YC-era autonomy tooling into a $15B physical AI company, [Qasar Younis](https://x.com/qasar) and [Peter Ludwig](https://www.linkedin.com/in/peterwludwig/) have spent the last decade living through the full arc of autonomy: from simulation and data infrastructure for robotaxi companies, to operating systems for safety-critical machines, to deploying AI onto cars, trucks, mining equipment, construction vehicles, agriculture, defense systems, and driverless L4 trucks running in Japan today. They join us to explain why “physical AI” is not just LLMs on wheels, why the real bottleneck is no longer model intelligence but deployment onto constrained hardware, and why the future of autonomy may look less like one-off demos and more like Android for every moving machine.

We discuss:

Applied Intuition’s mission: building physical AI for a safer, more prosperous world, powering cars, trucks, construction and mining equipment, agriculture, defense, and other moving machines

Why physical AI is different from screen-based AI: learned systems can make mistakes in chat or coding, but safety-critical machines like driverless trucks, autonomous vehicles, and robots need much higher reliability

The evolution from autonomy tooling to a broad physical AI platform: starting with simulation and data infrastructure for robotaxi companies, then expanding into 30+ products across simulation, operating systems, autonomy, and AI models

Why tooling companies came back into fashion: Qasar on why developer tooling looked unfashionable in 2016, why Applied Intuition still bet on it, and how the AI boom made workflows and tools central again

The three core buckets of Applied Intuition’s technology: simulation and RL infrastructure, true operating systems for vehicles and machines, and fundamental AI models for autonomy and world understanding

Why vehicles need a real AI operating system: real-time control, sensor streaming, latency, memory management, fail-safes, reliable updates, and why “bricking a car” is much worse than bricking an iPad

Physical machines as “phones before Android and iOS”: Peter explains why today’s vehicle and machine software stack is fragmented across many operating systems, and why Applied Intuition wants to consolidate the platform layer

Coding agents inside Applied Intuition: Cursor, Claude Code, internal adoption leaderboards, and how AI tools are changing engineering workflows even in embedded systems and safety-critical software

Verification and validation for physical AI: why evals get harder as models improve, how end-to-end autonomy changes simulation requirements, and why neural simulation has to be fast and cheap enough to make RL practical

From deterministic tests to statistical safety: why autonomy validation is shifting from binary pass/fail requirements toward “how many nines” of reliability and mean time between failures

Cruise, Waymo, and public trust: Qasar and Peter discuss why autonomy failures are not just technical issues, how companies interact with regulators, and why Waymo is setting a high bar for the industry

Simulation vs. reality: why no simulator perfectly represents the real world, how sim-to-real validation works, and why real-world testing will never disappear

World models for physical AI: hydroplaning, construction equipment, visual cues, cause-and-effect learning, and where world models help versus where they are not enough

Onboard vs. offboard AI: why data-center models can be huge and slow, but onboard vehicle models need millisecond-level latency, low power, small size, and distillation-like efficiency

Why physical AI is not constrained by model intelligence alone: the hard part is deploying models onto real hardware, under safety, latency, power, cost, and reliability constraints

Legacy autonomy vs. intelligent autonomy: RTK GPS in mining and agriculture, why hand-coded path-following worked for decades, and why modern systems need perception and dynamic intelligence

Planning for physical systems: how “plan mode” applies to robotaxis, mining, defense, and multi-step physical tasks where actions change the state of the world

Why robotics demos are not production: the brittle last 1%, humanoid reliability, DARPA Grand Challenge-style prize policy, and the advanced engineering gap between research and deployment

Applied Intuition’s hard-earned lessons: after nearly a decade, Peter says they can look at a robotics demo and predict the next 20 problems the company will hit

Qasar’s advice to founders: constrain the commercial problem, avoid copying mature-company strategies too early, and remember that compounding technology only matters if you survive long enough to see it compound

Why 2014 YC advice may not apply in 2026: capital markets, AI company dynamics, and the difference between building in stealth with a deep network versus building as a new founder today

What Applied is hiring for: operating systems, autonomy, dev tooling, model performance, evals, safety-critical systems, hardware/software boundaries, and engineers with deep curiosity about how things work

Applied Intuition:

YouTube: [https://www.youtube.com/@AppliedIntuitionInc](https://www.youtube.com/@AppliedIntuitionInc)

X: [https://x.com/AppliedInt](https://x.com/AppliedInt)

LinkedIn: [https://www.linkedin.com/company/applied-intuition-inc](https://www.linkedin.com/company/applied-intuition-inc)

Qasar Younis:

X: [https://x.com/qasar](https://x.com/qasar)

LinkedIn: [https://www.linkedin.com/in/qasar/](https://www.linkedin.com/in/qasar/)

Peter Ludwig:

LinkedIn: [https://www.linkedin.com/in/peterwludwig/](https://www.linkedin.com/in/peterwludwig/)

Timestamps

00:00:00 Introduction: Applied Intuition, Physical AI, and 10 Years of Building

00:01:37 Physical AI vs. Screen AI: Why Safety-Critical Changes Everything

00:02:51 The Origin Story: Tooling, YC, and the Scale AI Comparison

00:05:41 The Three Buckets: Simulation, Operating Systems, and Autonomy Models

00:11:10 Hardware, Sensors, and the LiDAR Question

00:14:26 The Operating System Layer: Why Vehicles Are Like Pre-Android Phones

00:19:13 Customers, Licensing, and the Better-Together Stack

00:21:19 AI Coding Adoption: Cursor, Claude Code, and the Bimodal Engineer

00:26:41 Verifiable Rewards, Evals, and Neural Simulation

00:31:04 Statistical Validation, Regulators, and the Cruise Lesson

00:40:25 World Models, Hydroplaning, and Cause-Effect Learning

00:43:34 Onboard vs. Offboard: Latency, Embedded ML, and Distillation

00:50:57 Plan Mode for Physical Systems and Next-Token Prediction Universally

00:53:04 Productionization: The 20 Problems Every Robotics Demo Will Hit

00:58:00 Founder Advice: Constraints, Compounding Tech, and Mature-Company Mimicry

01:05:41 Hiring Philosophy: Hardware/Software Boundary and Engineering Mindset

01:08:50 General Motors Institute, Education, and the Curiosity Mindset

Transcript

Introduction: Applied Intuition, Physical AI, and 10 Years of Building

Alessio [00:00:00]: Hey everyone, welcome to the Latent Space Podcast. This is Alessio, founder of Kernel Labs, and I’m joined by Swyx, editor of Latent Space.

Swyx [00:00:10]: And today we’re very honored to have the founders of Applied Intuition, Qasar and Peter. Welcome.

Qasar [00:00:17]: You guys really know how to turn it on to podcast mode. That was, you guys are real pros at this.

Qasar [00:00:23]: They were just joking around right before this, and then they flipped it pretty quick.

Alessio [00:00:29]: Oh, yeah, it’s good to have you guys. Maybe you just wanna introduce yourself so people know the voice on the mic and they’ll know what they’re hearing.

Peter [00:00:33]: Oh, sure. Yeah, I’m Peter Ludwig. I’m the co-founder and CTO of Applied Intuition.

Qasar [00:00:38]: And my name is Qasar Younis. I am the CEO and co-founder with Peter.

Alessio [00:00:42]: Nice. Can you guys give the high-level overview of what Applied Intuition is? And I was reading through some of the Congress files, when you went out there, Peter, and eighteen of the top twenty global non-Chinese automakers, you two guys, you have customers in agriculture, defense, construction. I think most people have heard of Applied Intuition tied to YC when it was first started, and then you were kinda in stealth for a long time, so maybe just give people the high-level overview of what it is today, and then we’ll dive into the different pieces.

Peter [00:01:10]: Yeah. So at Applied Intuition, our mission is to build physical AI for a safer, more prosperous world. And so we work on physical AI for all different types of moving systems, everything from cars to trucks to construction and mining equipment, to defense technologies. And we’re a true technology company, so we build and sell the technology, and we sell it to the companies that make the machines. We sell it to the government, really anyone that wants to buy a technology to make machines smart.

Physical AI vs. Screen AI: Why Safety-Critical Changes Everything

Qasar [00:01:38]: Yeah. And I think in the broader AI landscape, a lot of the focus, rightfully so in the last, three years has been on large language models, and so everything fits in a screen. Like, whether it’s code complete products or things like that. And what’s different about us is we’re deploying intelligence onto a lot of things that don’t have screens. they’re physical machines. There are sometimes screens within the cabin or for example of a car or a truck or something like that, but most of the value we provide is putting intelligence that is in safety critical environments. So that those two words are really important because learn systems can make mistakes if you’re asking for, like, some, so something like, “Tell me about these podcast hosts

Qasar [00:02:28]: that I’m about to go meet.” But you can’t do that obviously when you run, like, as an example, we run driverless trucks in Japan right now, as we speak. We can’t have errors. Those are L4 trucks. Yeah.

Alessio [00:02:40]: Yeah. Was that always the mission? I remember initially, I think people put you and Scale AI very similarly for some things about being kinda like on the data infrastructure side of things. What was the evolution of the company?

The Origin Story: Tooling, YC, and the Scale AI Comparison

Peter [00:02:51]: Well, from the very beginning, we always wanted to, really be a technology company that helped generally push forward the industrial sector. And so we started off working in autonomy. Our very first customers were robotaxi companies. And we started off doing a lot of work in simulation and data infrastructure. And then over the years, we’ve expanded our portfolios. Now we have, over thirty products, and it’s a pretty broad technology play within the landscape of physical AI.

Qasar [00:03:19]: Yeah, I think the Scale reason is because we’re all YC Universe companies. But it was a very different company. Scale, was, is more of a services company, data labeling company fundamentally. We started and still are, do a lot of tooling. So like, you think developer tooling is now in vogue again, thanks to the AI boom. But honestly, ten years ago, it was out of vogue. It w Like, doing a tooling company in 2016, 2017 was not, like, the thing to do because, I don’t know if you remember, the VCs generally, their views was that toolings are They’re just workflows, and workflows ultimately are not really interesting. And we’ve gone and come, full circle with that. But when we started the company, our kind of it’s kinda like in the periphery of what the company wants to be. It was like, from our earliest days, like, we wanna deploy software on physical machines, like on cars and on trucks and things like that. And obviously, we didn’t know that the transformer boom was gonna happen. We didn’t know that autonomy systems would become end-to-end. Those things we didn’t know. And why that’s important when autonomy systems become end-to-end, it is just now those models can be generalized to, multiple form factors. And so back nine, ten years ago, tooling was a great way, and still is a great way to, build the technology and sell technology to our end customers, a lot of them who wanna build this stuff themselves. And so we just offer like a spectrum of solutions from you can just use like one part of a development suite of tools all the way to buying the full thing. The way to think about the company, or at least the way we think about the company is, as Peter said, a technology provider. It’s kinda like, what NVIDIA does or what an AMD, but we just don’t do chips.

Qasar [00:05:06]: We don’t do silicon. But we’re a technology provider fundamentally. And I think even, we used to joke when we started the company, like, we’re not the guys to build, like, Instagram. Like that was just towards That’s not our That’s just not us in a most fundamental way. I

Alessio [00:05:20]: You have thoughts.

Qasar [00:05:21]: Yes.

Qasar [00:05:22]: Well, it’s, it’s I mean, I think it’s just like what And I mean, we worked on Maps and stuff, Google Maps. Consumer products are extremely difficult for a lot of different reasons. It just, I think doesn’t scratch the itch. I think we’re like Michigan guys who are kind of more of that traditional engineering kind of a realm, or lineage. we used to joke

The Three Buckets: Simulation, Operating Systems, and Autonomy Models

Peter [00:05:41]: I gotta say, though, what was clear ten years ago was that there was so much more that was possible with software and AI in vehicles

Peter [00:05:47]: and that was generally the space that we started in ten years ago.

Peter [00:05:51]: And the precise path that we’ve taken over the years, I think we’ve been strategic, and we’ve adjusted to make sure that we’re actually building stuff that’s valuable to the market. And like, the technology has changed so much. Like our own technology stack has completely changed, I would say, roughly every two years. And so now we’ve probably done, let’s say, four complete evolutions of our own technology stack. And I sort of see that cadence roughly keeping up.

Peter [00:06:13]: And so the way even we think about engineering is almost on this two-year horizon, we’re preparing ourselves that, hey, like, we wanna invest the appropriate amount, but then also be very dynamic as the research gets published and as our research team figures out new advancements and adapting to that.

Qasar [00:06:27]: Yeah. One thing that has been consistent is the type of people we’ve, we’ve recruited. It’s engineers who are fall into the sometimes very traditional, like, Google

Qasar [00:06:38]: -gen suite, but way different from, other companies. We are hiring folks who really know the intersection of hardware and software, who know really low-level systems. Obviously, traditional ML researchers and folks who’ve, actually, put ML systems into production. That’s been pretty consistent. I think that, like, you look at the mix of our engineering, eighty-three percent of the company is engineering, so it’s, like, a giant list.

Qasar [00:07:05]: A lot of engineers.

Alessio [00:07:06]: Which, by the way, a thousand engineers

Qasar [00:07:07]: Yeah. A thousand engineers.

Alessio [00:07:08]: that’s on your website, so I imagine it’s up to date.

Qasar [00:07:11]: It is, it is up to date, yes. Yes.

Alessio [00:07:12]: okay. And then forty-plus founders.

Qasar [00:07:15]: Yeah. We would tend to also, This was more luck than strategy. But we’ve recruited a lot of ex-founders. It’s been a great place for founders, YC and non, ‘cause obviously I know a lot of the YC folks. It’s kind of like we recruit a lot of Google people.

Qasar [00:07:33]: For them to exercise both their technical and non-technical skills because, we’re, we’re, we’re on the applied side. We have a research team that we do fundamental research, we publish, and we’ve, we’ve had great traction there. But fundamentally, the business wants to take this intelligence and deploy it into production and there’s, like, a certain type of person that’s more interested in that.

Alessio [00:07:54]: Yeah. You mentioned the tech stack, Peter, so I just wanted to give you some rein to just go into it. I’m interested in where Wayve Nutrition, starts and ends in some sense, what won’t you do? What, do you do that’s common among all the verticals that you cover?

Peter [00:08:10]: There’s a few buckets of work that we do, and we’ve been at this for almost ten years now, so the technology’s pretty broad. But we got started

Qasar [00:08:17]: Yeah, with a thousand engineers, like, you could work on lots of things.

Peter [00:08:19]: There’s lots of stuff, yeah, espe-especially with AI tools to help.

Peter [00:08:22]: So we got our start in simulation and simulation tooling and infrastructure. And so generally, if you’re trying to build a very complex software system that involves moving machines, you need to test that, and the best way to test it is it’s a combination of virtual developments, a simulation, and then also obviously real world testing.

Peter [00:08:39]: And then there’s a very careful process of that correlation between the simulation results and the real world results and ensuring that the simulator is in fact accurate to that. Simulation’s a very deep topic.

Peter [00:08:49]: We have a whole suite of products in that, and we could talk for many hours about that specifically. But that is one part of what we do as a company. Reinforcement learning as a subpart of that is also super critical. I think a lot of the a lot of the best advancements happening in a lot of these AI systems right now in some way relate to reinforcement learning, and with now we have lots of compute, and you can do tons of interesting things for reinforcement learning. The second bucket of work that we do is on operating systems technology. true operating systems. Like, think about, schedulers and memory management and middleware and message passing and highly reliable networking and data links. Like, the reality is, if you want to deploy AI onto vehicles, you need a really good operating system. And when we were getting deeper into that space, there wasn’t really anything that we were happy with.

Peter [00:09:39]: Like, things existed, absolutely, and we were using what was available in the market, and as an engineering organization, we roughly realized these things aren’t great. We think we can do this better, and so let’s, let’s build something. And that was then the that was the moment of inspiration that started our operating systems business, which is now a very real business for us. And in order to write and run great AI, you need a great operating system, and so that-that’s what got us into that. And then the third bucket that we work on, it’s, it’s true fundamental AI technology. Models, we do a lot of work in, as mentioned, the foundational research, but then the also the world models and the actual autonomy models that are running on these physical machines, and that’s across cars, trucks, mining, construction, agriculture, and defense, and so that’s both land, air, and sea.

Qasar [00:10:31]: And also, a smaller subsector of that third bucket is the interaction of humans with those machines.

Qasar [00:10:38]: So that’s a multimodal, experience. Historically, if you’re moving a dirt mover or any of these machines, there are, like, buttons you press, whether they’re actual physical tactile buttons or something like a touch screen. That’s just That fundamentally is changing to where you’re just talking to the machine and the machine and you’re teaming with the machine.

Alessio [00:10:58]: Voice?

Qasar [00:10:59]: Yeah, voice, absolutely, yeah.

Alessio [00:11:00]: Oh.

Qasar [00:11:00]: And also the machine just being aware of who is in the cabin, what their state is. you can think from a safety systems perspective, the most simple version of this is, like, the driver is tired, right? They’re, they’re if you get those alerts when you’re driving your car and says

Hardware, Sensors, and the LiDAR Question

Qasar [00:11:15]: -maybe take a coffee break, that take that times, a couple of order of magnitudes up. But this concept of teaming man and machine is important. When you think about running agents or just running, different instances of, Claude and doing work for you in the background, you can take that analogy out, almost copy and paste and put it into, like, a farm, where you have a farmer who’s running a number of machines. So where they interact with the machine is where there’s maybe a critical decision or a disengagement or something like that, but generally speaking, the agent on the physical machine is running and making decisions on the behalf of the farmer until there’s something maybe critical. And that’s also what we work on. So that’s not pure autonomy. It’s a little bit of a mix, but it falls under, autonomy. In the automotive sense, that’s typically defined in SAE levels as an L2++ system

Qasar [00:12:05]: -with a human in the loop. But just take that idea, to other verticals.

Alessio [00:12:09]: Yeah. You’ve not mentioned hardware at all, like sensors or obviously we you mentioned you don’t do chips. I think even in AV there’s, like, a big, cameras versus lidars. Like, what are, like, in your space maybe some of those design decisions that you made, and are they driven by the OEM’s ability to put things on the machinery? And like, how much influence do you guys have on co-designing those?

Peter [00:12:32]: Yeah. So we don’t make sensors. Like, we’re, we’re not a manufacturer. Obviously, we use a lot of sensors in our autonomy products. in terms of what actually goes on the vehicles, we have a preferred set of sensors that we, let’s say fully support, and then our customers, they can sort of choose from those. And obviously if there’s a very strong opinion on supporting something else, we’ll add that to the platform as well. And the lidar question is at this point sort of the age-old,

Peter [00:12:59]: topic in autonomy, and the state of the industry right now is lidar is hands down a useful sensor, specifically for data collection and the R&D phase of autonomy development. if you see, for example, a Tesla R&D vehicle, it actually has lidar on it

Peter [00:13:17]: to this day, right? In the Bay Area we see these. you’ll see, like, Model Ys or Cybercab that have lidars on them just driving around. So it’s, it’s useful because it gives you per pixel depth information. So if you can pair a lidar with a camerand you can say that, well, this camera’s looking this direction, this lidar’s looking this direction, and now for each pixel of the camera I can see how far away is that pixel. you can actually then use that as a part of your model training, and then the that depth information then becomes a learned, a learned state of the camera data. And then when you’re doing the production system, you can now remove the lidar

Peter [00:13:52]: and now you can actually get depth with just the camera. And so that difference between, like, a highly sensored R&D vehicle and then the down-costed production vehicle, we use that across our whole portfolio of products. And of course the end goal is you want super low cost and super reliable.

Peter [00:14:08]: And then in certain use cases you have some more, bespoke things. Like in defense as an example, you do things at night oftentimes, and so you care about sensors like infrared, more so than And you don’t, you don’t wanna be putting energy out, so you don’t wanna use lidar or radar.

Peter [00:14:23]: but you still need to be able to see at nighttime. So yeah, we work the whole gamut.

The Operating System Layer: Why Vehicles Are Like Pre-Android Phones

Alessio [00:14:27]: Cool. So that’s kinda like on the hardware level. Then on the OS level, how does that look like? What is, like, unique? my drive- I drive a Tesla. Whenever I drive some other car that has a screen, it always sucks.

Alessio [00:14:38]: It’s on, like, cheap Android tablet. It’s like, it’s laggy and all of that. What does the OS of, like, the autonomy future look like?

Peter [00:14:46]: When most people, it’s really what you just described. When you think about operating system in a vehicle, you’re thinking about the HMI, right? The human machine interface, and absolutely that’s a an important part of it, but that’s actually only one thin layer on top. So when we talk about operating systems for, like, AI in vehicles, there’s many layers that go deep into the CPU critical realm and embedded systems, and you’re talking about the real time control of

Peter [00:15:13]: let’s say the electric motors or the engine and the actuators, and you have different redundancies for different, let’s say, the steering actuation in the vehicle. And all of these things, need very core support in the in the operating system. And then of course for autonomy you have real time sensor data that’s streaming in, and the latencies there are really important, right? If you try to Imagine you try to run Microsoft Windows

Peter [00:15:35]: like streaming your sensor data in or controlling the vehicle. Like, the latencies are gonna be absurd. Like, you can never do that. And so what’s special about what we do is we really have this system level thinking, right? So we’re looking at, we care about every performance characteristics of the entire system, and then we also, because we’re doing a lot of the software or all of that software, we can fine-tune and control all of those things. So we can very carefully tune in the latencies for every aspect of the system. We can carefully tune in the memory management. We can have the right, fail-safes and fallbacks, for different things. ‘Cause you have to account for what if, what if there is a critical failure? What if there’s a cosmic ray that flips

Peter [00:16:14]: a bit in the middle of the processor that causes some, malfunction? And you have to have a fail-safe to all of that, and so the core operating system is a part of that. And then the one last thing, which is a lot less exciting but is, actually a very big topic, is reliability of updates.

Peter [00:16:30]: so the I have a Tesla and you get updates fairly frequently, right?

Peter [00:16:36]: Once a month. Most companies that are making vehicles

Peter [00:16:40]: are basically never doing updates, and they’re And even if they are doing updates, they’re usually only updating maybe one module. Maybe they’re updating the HMI module. But they’re not able to update, let’s say, the CPU critical parts of the system.

Peter [00:16:51]: You have to go into the dealer for that. And so with our operating system now we can actually enable highly reliable updates of any system in the vehicle, and that’s way easier said than done. Like, there’s lots of technical, technically deep stuff, in the tech stack to do that in a way that you’re not going to accidentally brick a vehicle.

Peter [00:17:08]: And right? If, imagine your

Alessio [00:17:10]: That would be bad.

Alessio [00:17:11]: Bad.

Peter [00:17:11]: Bricking a car is a very expensive

Peter [00:17:13]: and honestly, like across the industry maybe one of the most just pure impactful things that we’ve done is we’ve just, we’re, we’re now enabling the industry to actually do software updates.

Alessio [00:17:22]: Just to clarify as well, who is the customer for this? Like, I assume a lot of hardware manufacturers have their own firmware, and I’m sure some of them would just have you write it for them because you’re experts. And others would have their own. Like, who pays for this? Who invites you into the house? Is it, is it the end user, or is it, is it the manufacturer?

Peter [00:17:41]: Yeah. So let me make an analogy firstly on the on the fragmentation of software. So physical machines today are more akin to the state of the phone market before Android and iOS existed, right? So I worked on Android at Google by the way many years ago, and part of the reason that Larry at Google decided to get into Android was they wanted to run Google products on a bunch of phones, and they bought all of these phones from the industry, and it turned out they had like 50 different operating systems on these phones. And it was virtually impossible

Peter [00:18:17]: for Google to make their app run on all 50 devices equally well. And so the solution was, well, actually what if, what if they created-A really great operating system and made it attractive to all of these phone makers, and that was sort of the genesis for what Android was and why Android existed. It was a way for Google to get their products onto really wide diversity of devices. The state of the physical, industry right now, it’s a little bit like that. Like, there’s yes, these companies have firmware, but they have so many different operating systems, it’s so fragmented, and to actually get a modern AI application to run on these vehicles, you actually, you first have to consolidate the operating system, and so that’s, that’s why we’ve done that. And then, your specific question was who are our customers? It’s, it’s, generally it’s the companies that are making these machines.

Peter [00:19:06]: And we’re, we’re, we’re selling our technology to them to really simplify the architecture and then enable these AI applications to run on them.

Customers, Licensing, and the Better-Together Stack

Swyx [00:19:13]: How much is reusable across? Like, do you have, like, one OS that is just configured for everything, or is there some more customization that is needed?

Peter [00:19:22]: Yeah, highly reusable. So the fundamental technology is quite universal, right? So things that we do have to think about though are, like, chipset support. And so if you’re, if you’re coding, let’s say, an LLM and you have start with an assumption that, “Hey, oh, I’m gonna, I’m gonna use CUDA, and I’m gonna run this, on an NVIDIA chip,” then you don’t really have to think about the hardware in that sense. Like, you’re just, “Okay, I’m just I’m in the CUDA/NVIDIA ecosystem, and I’m, I’m going to use that.” But the hardware, especially in safety critical systems, it’s a lot more diverse. There’s not one or one or two players. There’s a bunch of different chipsets that we have to support. And so our operating system doesn’t just run on, like, the equivalent of X86. It has to, it has to run on a number of different architectures from chips from a bunch of different companies. But again, we’ve been working on this for a long time now, so we have, we have support for all of those chipsets. And then when you want to then run the AI applications, we can then do that reliably across now a variety of providers.

Qasar [00:20:19]: And I think that is, like, heavily inspired by Android, right? Android has a huge suite of testing and it’s a reliable operating system that runs on thousands of devices. And we think we can, we can do the same in all these physical moving machines, with the difference that we’re really in a safety critical realm. Android isn’t.

Alessio [00:20:40]: So on Android, I don’t need to use Gmail, I can use Superhuman. Like, what about your machinery? Like, can people bring somebody else’s automation to it, or is it kinda like all-in-one?

Qasar [00:20:50]: You have to use us. No. Yeah. we’re If, Yeah. Yeah, it’s totally open. Yeah.

Peter [00:20:56]: Yeah. our philosophy is that we are a technology company, and so we license our technology to customers to use how they want. And so if a customer wants to If they wanna license our autonomy tech and our operating system, then great, we’ll license those. If they just wanna license the operating system and then use different autonomy tech, that’s fine also, and we have great documentation and

Swyx [00:21:17]: Or if they wanna use developer tooling.

Peter [00:21:18]: Yeah, exactly.

AI Coding Adoption: Cursor, Claude Code, and the Bimodal Engineer

Swyx [00:21:19]: It’s, like, a better together if, obviously, if you, if they work together. Is it all C++ I assume is with different compile targets?

Peter [00:21:27]: We use a lot of C++.

Peter [00:21:28]: Rust is sort of a hot, the new hot kid on the block

Peter [00:21:32]: for a bunch of things as well. But yeah, the lower level you get, especially when you get to real-time constraints, you hit C++ at some point, and at some point maybe you work your way into assembly when needed.

Swyx [00:21:44]: Oh, damn.

Alessio [00:21:46]: I’m curious about the coding agent adoption, just, like, since you’re mentioning more esoteric languages. Like, what’s the adoption internally? What have you learned?

Peter [00:21:55]: Yeah. We use everything. So Cursor was, I think the hottest tool in the company for a good while. Now Claude Code, I think has taken the reign on that. We have a internal leader, leaderboard that we use just to sort of encourage adoption

Peter [00:22:09]: with-within the company. And yeah, it’s, they’re phenomenally useful. it’s, Honestly, we take inspiration from some of those tools also in how we’re adapting some of that mindset of thinking to the physical realm. Like if it’s so easy to build an app for this or that thing that lives just on a screen, we can We’re taking now a lot of the same ideas and applying that to, “Okay, well, if you wanted a physical machine to do something, how easy can we make that, using our own tooling and platform as well?”

Alessio [00:22:40]: Are you changing any of, like, the OS architecture, kinda like the way you expose services to, like, be more AI friendly or?

Peter [00:22:48]: Yeah, absolutely. The in the early days of our tools infrastructure work, it was a lot about, You had engineers that were experts in certain topics, but the things that you’re dealing with, they’re oftentimes more mathematical or more abstract, where actually GUI tools are very useful for certain things. Like as an example, we have a product we call Sensor Studio, which is, it helps you design the sensor suite for your autonomous vehicle, whether, again, it could be a car, it could be a drone, could be a mining equipment, could be a robot. And you place sensors in different places. You There’s different, There’s a library. You can understand what are the trade-offs that you’re making in the design of that system, and that was, like, a very, a very GUI intensive, thing ‘cause it’s a little more like a CAD tool in that sense

Swyx [00:23:37]: Yep

Peter [00:23:37]: if you’ve seen CAD tools. Nowadays, though, right, we expose all of the underlying APIs for that and now using, AI agents, you can actually configure a sensor suite with just text and likely reach a better result than you could’ve through the GUI in the past, and we’re taking that thinking now through the whole product portfolio.

Swyx [00:23:57]: Another thing I was thinking about is just in terms of, like, AI, adoption, does it change your hiring at least a little bit, or how do you, how do you sort of manage engineers, differently?

Peter [00:24:08]: Yeah. absolutely, it does. we, I think like every company in the Valley right now, are evolving our hiring practices

Peter [00:24:16]: because the skills required to be effective are changing so fast, right? you used to really select for just rote implementation ability and now it is more the AI engineer skill set, right? Where it’s like, yeah, how to implement, but actually-Just banging out code is no longer the core job, right? It’s, it’s actually knowing what questions to ask, knowing how to tie, how to tie together these different AI tools. And so the interviews that we give now I think are way harder than they’ve ever been.

Peter [00:24:46]: But we also allow, right, selective use of AI tools to solve the problems. And I think in that you start to see more of a bimodal distribution of engineers, right? You start to see like wow, there’s, there’s this subset of people that they really get it. Like they’re, they’re all in and they’ve, they’ve clearly invested the hours needed to learn these tools and how to be effective.

Peter [00:25:09]: And then there’s sort of the group of people that haven’t done that, and that the productivity gap is just enormous. And so we’re, we’re trying to obviously select for the people that are really into this.

Qasar [00:25:20]: I first wrote the my AI engineer piece three years ago, and when I first wrote about it, I was like, “Actually, not everyone should be an AI engineer,” ‘cause I think there’s a there’s an extremist stance where well, every software is an engineer is an AI engineer. And my actual example of people who should not be adopting AI was embedded systems and operating systems, and database people. Are they adopting AI?

Peter [00:25:41]: I think it’s the classic bitter lesson, topic, which is the Six months ago I would’ve said the same thing, but it’s, it’s becoming super useful for every domain.

Qasar [00:25:53]: I’m sure.

Peter [00:25:54]: Right? Like,

Peter [00:25:56]: there was, I think six months ago, or maybe a year ago, if you tried to use, let’s say the latest Claude model for writing shaders, GPU shaders, the results were probably underwhelming. And if you use the latest model now to do that kind of task, you’re a little bit blown away, like, “Wow, that actually worked. That’s amazing.” And we see the same thing in the embedded realm. No question though, especially when you get into safety critical systems, the human validation is

Peter [00:26:25]: is 100% key. Like I You’re not gonna trust your life to a an AI written software that’s, that’s not been very carefully, checked by humans. And so I think now the really the challenge is about that appropriate level of human validation for these safety critical systems.

Verifiable Rewards, Evals, and Neural Simulation

Alessio [00:26:41]: How do you think about, yeah, touching on the simulation side, I think verifiable reward and reinforcement learning is, like, the hottest thing. What have you done internally to build around that? And like, what gives you What makes you sleep at night? Like, if somebody’s like, just web coding something or like

Alessio [00:26:57]: wants to try something new, you have like a good enough system. Because I think the opposite is also true, is like if it’s super easy to write anything

Alessio [00:27:04]: then it puts a lot of work on like the verifiable

Alessio [00:27:07]: side of it. Like, what does that look like for people?

Peter [00:27:10]: Yeah. So verifiability, a broader bucket of like evaluations, right? Like how do you evaluate the results that you’re, you’re getting? I think this is probably the hardest problem right now, because the As the models get better, it can be harder and harder to find the faults on the system.

Peter [00:27:29]: And so like the problem of doing proper eval to find those faults, like that problem also keeps getting harder as the models get better. But it’s no less important than it’s ever been, right? You still there are still going to be edge cases that are not met and whatnot. And so it’s, it’s a big area of investment for us. On the reinforcement learning topic, the key thing is there’s all these new requirements that come to be in the latest generation of these technologies. So for example, end-to-end is the big thing right now in autonomy and physical AI, which is you can now train these models that can effectively take sensor data in and then put control signals out, and get really good results out of that. But the way that you train and improve those models is really different from the previous generations. And so to do reinforcement learning on an end-to-end model, you now need to actually simulate all the sensor data, right? So then this becomes a we call our, work in this neural simulation, but it’s

Peter [00:28:26]: think of it like a hybrid of Gaussian, splatting and diffusion methods, and where you really care about performance. Like performance is everything. If you can’t do enough simulation fast enough and cheap enough, you actually can’t get results that are worthwhile, in the end. It also gets to a lot of our work in embedded systems, which is like performance critical work, and that performance optimization, performance criticality, it carries over to a lot of the model training work. because, like, the only way to make it affordable is it has to be really fast.

Qasar [00:28:58]: I think it’s worth a few minutes talking about our own, evolving thoughts on verification and validation within

Qasar [00:29:05]: kind of, traditional simulators, which are, you can think of like vehicle dynamics or something like that, which you’re just taking textbooks and taking those formulas

Qasar [00:29:13]: and putting them into software, to like now this neural sim/world model universe. I think that’s an interesting topic.

Peter [00:29:20]: Yeah. So in more traditional development, right, you oftentimes would have, more black-and-white answers to questions.

Peter [00:29:28]: And so the in Europe as an example, there’s, a regulatory, system, it’s called Euro NCAP. It’s the European New Car Assessment Program, and as part of that, the vehicles have to pass a bunch of tests, and those tests actually, include, safety systems. So automatic emergency braking for a child that runs in front of a car

Peter [00:29:51]: or let’s say an occluded child that runs out and you hit it. And so you have You end up with sort of these binary answers of like, well, did the car under test pass this specific test? And there’s a very well-known set of test cases

Peter [00:30:05]: that the vehicle has to pass. And that was how the industry worked, let’s say, until 10-ish years ago. But what’s changed now is with these models, everything is statistics, right? Like you no longer have a black-and-white answer, but it’s like, well, how many orders of magnitude or how many nines of reliability can I get in the system, and how can I, how can I prove that to be true? And the big unlock honestly for physical AI as an industry is that these models are just becoming much more reliable. Right? Things like things actually work a lot better. It’s like the number of nines you can get out of these systems are now good enough that it actually becomes cost effective to really deploy these things. And so the big shift in, so verification and validation has been from a little bit more of a Again the past it was strictly requirements, and are you meeting or not? And now it’s more of a statistical, verification and validation case where it’s all about how many nines of reliability and meantime between failures, that sort of thing.

Statistical Validation, Regulators, and the Cruise Lesson

Swyx [00:31:04]: And is the target audience regulators or even the customers are yeah, if you I imagine the customers are bought in, and it’s mostly regulators that need to be satisfied.

Peter [00:31:15]: We do work with the US government, we do work of course with the European governments and the government of Japan, and the government is not like an AI lab by any means.

Peter [00:31:25]: So Swyx [00:31:26]: They just care about the outcome.

Peter [00:31:27]: They care about the outcome.

Peter [00:31:28]: And so we do education, in that regard, and like so sort of teaching about, “Hey, this is how we think validation should be done, and this is an approach that we think is reasonable,” and how to think about like when is a driverless system actually safe enough to go on the roads and that sort of thing. But I wouldn’t say that the government is asking for it. It’s like we’re more teaching the government in that, in that sense. It’s honestly, it’s more so for our own, our own comfort, right? Like, we want to build very safe systems, and then of course our customers care deeply about that as well. But in that context we’re also typically educating our customers.

Qasar [00:32:01]: Yeah. Our first, our first core value is on round safety. So I think we can’t underline enough that, us also verifying and validating that the systems that we’re deploying are safe to us is probably as important as, like, some regulator or a customer saying,

Swyx [00:32:19]: Of course. Okay. Yeah.

Swyx [00:32:20]: You have to satisfy yourselves.

Peter [00:32:22]: As I say, as a whole across the world, regulation oftentimes it’s like a almost lowest common denominator. But like, you really have to substantially exceed what the regulators are expecting to make good products.

Swyx [00:32:33]: Yeah. One thing I often talk about, I think and I try to make this relatable to the audience also, is Cruise, where they had an accident that basically ended the company. I wonder if people overreact to single incidents, because incidents are going to happen regardless, right? ‘Cause it’s a statistical thing, but as long I don’t know if regulators understand that, you cannot extrapolate from a single incident, but we do because that’s all we have to go on. And your sample sizes are necessarily gonna be lower than, I don’t know

Swyx [00:33:00]: consumer driving.

Qasar [00:33:01]: Yeah. I think the Cruise example wasn’t a technology failure. there was The real, compounding issue there was just how did the company talk to the regulators and what was their kind of behavior, and I think that became more of the issue. If you look,

Peter [00:33:19]: It isn’t It definitely was a technology failure, but it was made much worse by the

Swyx [00:33:23]: Put the car back on the woman.

Qasar [00:33:25]: Yeah. And let me put it another way. There is a version where Cruise still exists.

Swyx [00:33:29]: right. Right.

Qasar [00:33:30]: Right. It’s

Swyx [00:33:30]: It was like the last straw

Qasar [00:33:31]: It

Swyx [00:33:31]: in like a long chain of

Swyx [00:33:33]: like issues.

Qasar [00:33:33]: So do you feel like ATG had that horrific accident or someone actually dying, because, that was a homeless person crossing the street? So yeah, I think we can’t understate enough that ultimately, like, statistical validation of something, that’s one part of it, but it’s not the only part of it. Like, consumer and let’s say, mainstream adoption of these technologies is also gonna be part of that conversation. I think companies like Waymo are doing a lot of service positively to the industry in the sense of they’re, they’re setting a high benchmark and they’re showing, kind of in a very responsible way how to, how to deal with these. There have been Waymo incidences as well. They’ve just not been as significant as the Cruise one that you mentioned. But yeah, so I think you’ll just continue to see that. I think probably the long term question is really gonna be, again, around Like it is very clear humans are way worse drivers statistically.

Qasar [00:34:29]: Like, there’s no, there’s no debate. And so at what point But we’re emotional animals.

Swyx [00:34:34]: Yeah. So my thing is, like, we have to get to a point as a society where we accept horrific accidents that would never happen by a human because statistically we understand that it is safer overall. In the same way that planes, they’re safer, than I think they’re the safest mode of transport that we have.

Qasar [00:34:50]: Yeah. it’s more dangerous to drive to the airport than it is to get on a flight.

Qasar [00:34:53]: So if you’re ever

Qasar [00:34:54]: if you’re ever getting nervous about getting on a plane, just think “I just gotta get to the airport.”

Swyx [00:34:58]: Yes, we’re flying.

Qasar [00:34:59]: If I get to the airport

Qasar [00:35:00]: I’ll be good.

Swyx [00:35:00]: But then it’s, planes also concentrate the tail risk if planes

Qasar [00:35:03]: Yeah. And

Peter [00:35:04]: And I was, I don’t think we honestly have to worry about there ever being, accidents from these systems that are like much worse than what humans would cause, ‘cause humans do terrible things.

Peter [00:35:14]: Like, people fall asleep at the wheel all the time.

Swyx [00:35:16]: I have.

Swyx [00:35:17]: Like, I’ll call, I’ve been a drowsy driver.

Peter [00:35:19]: Kinda drunk drivers, and that’s

Peter [00:35:20]: that’s the extreme end of the example. But these AI systems, you have redundancies, you have fallbacks. Like, there’s many things have to go wrong for there to actually be a something catastrophic because there’s, there’s so many, fallbacks that these systems have.

Alessio [00:35:36]: your simulation is like so vast because there’s so many use cases. What are, like, maybe things that worked in a simulation and then you put it out and it’s like, “Fuck, this is

Alessio [00:35:45]: this just did not work at all?”

Peter [00:35:47]: Yes.

Alessio [00:35:47]: Is

Peter [00:35:47]: That’s maybe a bit of a misconception, about simulation there. So let me go a little bit, more technical on this. So at first go, no simulation is going to represent the real world. There’s always a process of this, sim to real matching

Peter [00:36:02]: where you actually, you need the real world feedback to basically feed into the parameters that are being used in the simulator, and you have to do that, it’s like this validation flow, a number of times until you can get some confidence that, like I think the simulator is now accurately representing

Peter [00:36:19]: what’s gonna happen in the real world. Now, if you have a situation where you’ve done that full validation and you thought that it was accurate and then there’s something different, those are much trickier cases, and that’s, that absolutely can happen, but really I think the validation process is a really important part. You can never skip the simulation validation process, like where you’re actually ensuring that, hey, the actual, my sim to real gap here is small enough that I can trust these simulation results. And there’s, there’s so many fun things that you can do when you get into it. Like, I’ll, I’ll give one fun example that came up recently is like in these humanoid robotics, systemsOverheating actuators is a real problem, right? So obviously phenomenal demos. I

Peter [00:37:01]: The most amazing

Alessio [00:37:02]: For 10 minutes.

Peter [00:37:03]: The most amazing I can get. I love, I love watching robots do acrobatics like everybody but the these systems actually overheat, right? If, like, And one of the ways you can use simulation though is you can actually have that, the temperature of those actuators be one of the parameters that’s represented

Peter [00:37:18]: in the simulation. And if you’re doing reinforcement learning over a certain task, then the robot can actually adjust its motions in the simulation to account for the fact that, oh, it knows that as it’s moving, it’s actually beginning to overheat this motor. But if you didn’t have that parameter of, let’s say, the heat of that motor represented in the simulation initially, then your RL policy might It will disregard that. And now you run that on the robot and the robot will overheat and fail.

Alessio [00:37:43]: I guess the question is, like, how do you have all of these parameters taken care of while also understanding the deployment environment? Like, temperature is like a great example, right? Well

Alessio [00:37:53]: why did you make my robot worse when it runs in like a freezer?

Alessio [00:37:57]: So it actually shouldn’t worry about that. it’s like, yeah, how do you design these simulations?

Peter [00:38:02]: This is honestly the This is what makes simulation so hard, right? it’s because you Simulation is fundamentally about you’re trying to optimize the development of a system, right? Like, how can I build this system faster and better and cheaper and what are all the levers that I have to actually accomplish that? And because simulation’s just a software program, you can, you can change it a lot more easily than you can hardware systems. And then what’s particularly awesome about the let’s say, world models and using that as a part of simulation is now the simulation doesn’t just scale with, let’s say, adding new math equations in

Peter [00:38:36]: but we can actually scale the simulation environment now with additional real world data and that also unlocks a whole new field of robotics.

Qasar [00:38:46]: There is a meniscus line where you cross where still doing real world testing is better. there’s, in this, sim-to-real gap, you can reproduce reality at exceedingly expensive costs and this So nothing is free. So really you have to you’re finding that line where you’re getting great performance, you’re getting great feedback, whether it’s on the training side or on the eval side, but it’s way cheaper than doing it in the real world. At some point it, that doesn’t make sense. And so even, from our earliest days in autonomy, our view was you’re still gonna do real world testing. You There’s, there’s not, there’s not this, magical land where you’re not gonna do that. And maybe even like a more nuanced version of this in like traditional software development is, most of your testing for software in a vehicle, 95% of that can be like traditional CI/CD kind of, flows that you would have in traditional web development. But once you have Now you, let’s say you have a truck. Well, you can do like 4% of those in like a rig which has all the components, the electrical and electronics of a truck, but doesn’t have, it doesn’t have the tires and it doesn’t have the And then you have the 1%, which is actually the vehicle. There’s something There’s a similar analogy in terms of using simulation for intelligent systems. You can do a lot in a simulator, but in using world models, but ultimately it’s, it’s physical AI. So you’re gonna deploy it on physical machines and

Qasar [00:40:17]: the freezer example comes to, comes to light.

Alessio [00:40:20]: The world model thing has been to me the hardest thing to

Alessio [00:40:22]: wrap my head around. Like we have Faith Eliyon on the podcast.

World Models, Hydroplaning, and Cause-Effect Learning

Qasar [00:40:25]: We’ve been doing a small series with like another Intuition company, General Intuition as well.

Qasar [00:40:31]: yeah, and I mean, lots of, lots of coverage on NeRFs and yes.

Alessio [00:40:34]: Yeah. It feels like we talk with about, the heliocentric system, right? It’s like in a world model, if you just feed visual data, the model might learn that the sun spins around the Earth. It makes sense, right? And it’s like, well, not really. And I think what are like some of these other things that like hydroplaning is one thing I think about, is like can a world model understand hydroplaning and like what amount of water like causes it to happen? And it’s like, yeah, to me it’s like I don’t understand how you guys do it. I guess it’s like the real thing is like when you’re doing both cars and the highway in Japan versus the excavator in a mine in,

Qasar [00:41:13]: Arizona

Alessio [00:41:13]: wherever you’re Arizona, wherever you’re deploying them.

Alessio [00:41:15]: How much of it are you relying on the world models to like generate the simulations for you and then try and close the gap after versus like giving the world models as a tool to your engineers to like curate the simulations if that makes sense?

Peter [00:41:28]: Yeah, totally. So yeah, I can say at a pure engineering level, I think if you’re hoping to do real world deploys and you’re purely relying on a world model approach, you probably won’t get to something that works, before you go bankrupt. So there is just a very practical mindset of like, world models are amazing and they’re extremely useful for a lot of use cases, but there are a lot of other things that you need to do to actually get something started and something deployed and working. most fundamentally, world models are all about It’s understanding the world, but also understanding what’s going to happen. It’s like the cause-effect relationship.

Peter [00:42:01]: Right? And so like it, right, if you have a take some sort of construction tool, and that construction tool is gonna be doing some work on the Earth in some way, it’s gonna be moving earth, the world model needs to understand that cause-effect relationship. Like, okay, when I, when I take this material from here and put it over there and now I have things that are over here and not over there anymore and that cause-effect, relationship. data obviously is a is a big problem. The hydroplaning

Peter [00:42:26]: one is actually a really great example because it’s actually quite non-obvious sometimes. Right? It’s like, well, it’s, it’s raining and well this road, has, let’s say the appropriate curvature to it so the water is running off the road and cars are driving faster here and then you approach a road that’s very flat and water is now puddling on that road and all of a sudden cars are driving slower because when they were driving faster they were starting to lose control. And there are a lot of visual nuance, very nuanced visual cues in the scene and so I do think in the world model concept there’s a good chance that the model actually would learn that you should just drive slower when these visual cues exist, and that’s obviously the beautiful-The beauty of, these kinds of models where they just, they learn these non-obvious things.

Swyx [00:43:14]: It doesn’t need to know about hydroplaning to know that it needs to drive slower.

Peter [00:43:17]: Yes.

Swyx [00:43:17]: I guess it’s Yeah. I wanna ask questions about, also deploying models. I presume, like, you use a lot of these world models for training data and simulation, but what about deploying it onto the systems in production? Presumably you have you have, like, GPUs on device

Onboard vs. Offboard: Latency, Embedded ML, and Distillation

Swyx [00:43:36]: but they’re I keep saying on device. What’s the what’s the right term for that?

Peter [00:43:40]: On machine.

Swyx [00:43:41]: On machine.

Peter [00:43:41]: Or embedded, yeah.

Swyx [00:43:42]: Yeah. What is the embedded world like? because for people who are not used to that world, this is very alien.

Peter [00:43:49]: Yeah. So it’s actually We call it onboard and off board.

Peter [00:43:52]: So like, onboard software and off board software.

Peter [00:43:54]: And the great thing about off board software is you don’t have to care about time, and you can run really large models, right? So you can, you can say, “Well, this model, I don’t care if it takes one second for it to give me a result or 10 seconds for it to give me a result, because we have time.” And the models can be really big, and they can run, in a data center or on a on a huge GPU and you can obviously have distribute to compute, et cetera. But onboard you don’t have any of those benefits. You’re like, “Well, I need I have this many milliseconds where I need an answer from this model.” And so a lot more of the energy then is about, think of it more like distillation and it’s like truly efficiency and like, literally every fraction of a millisecond counts. And you can’t have a situation where the model takes too long because then the vehicle can’t actually function.

Peter [00:44:42]: And so you can, you can still use a lot of the same techniques, and the models themselves you can think of as like a derivative of larger models that you can run offline, and then you’re, you’re trying to just get a model that is still performs really well but it’s, it’s a it’s smaller, small enough version that you can then run on this embedded system where you care about latency and power.

Qasar [00:45:03]: Yeah. And I think like, the broader point I think which, maybe is not obvious but it’s worth saying is in physical AI world, we’re not really constrained right now by, like, the intelligence of the models. It’s actually what Peter’s talking about, it’s actually deploying them in

Swyx [00:45:19]: The hardware they give you.

Qasar [00:45:21]: Yeah. On the hardware you give you.

Qasar [00:45:22]: And so And there’s just a reality is of safety critical systems. So those end up being the your limiting factors

Qasar [00:45:29]: rather than, let’s say, a limiting factor for, a foundation model company

Qasar [00:45:34]: is gonna be just capital maybe or researchers.

Qasar [00:45:38]: So we’re, we’re in that way dealing with, for us as people who kind of come in that realm with like a very interesting Those constraints force creativity.

Swyx [00:45:47]: And I imagine, nobody was deploying or giving you the hardware for transformers back in 2018, whatever, but now they are. What’s the evolution like? just peel back the curtains a little bit.

Peter [00:45:59]: Yeah. Transformers first off, I think the paper was originally published in 2017.

Swyx [00:46:02]: 2017.

Swyx [00:46:02]: So there’s no time.

Peter [00:46:04]: And I

Swyx [00:46:05]: But I’m just saying I guess I’m saying, like, embedded ML systems usually, like, a lot less parameters, a lot less compute, and now, like, orders of magnitude more.

Peter [00:46:14]: Yeah. absolutely. what I was gonna say though was I think in the in the original paper in 2017, maybe it’s in the last paragraph, somewhere in the paper they talk about, like, “Oh, by the way, this technique might be useful for, like, images and videos as well.”

Peter [00:46:30]: These last subjects.

Peter [00:46:31]: And it took a few years for that impact to really hit. But like, now, we’re seeing transformers are everywhere.

Swyx [00:46:39]: Yeah. Vision transformers.

Peter [00:46:40]: And then then the compute just keeps getting better and better. But you do have this fundamental trade-off, right? It’s like you have power, you have cost, and performance and like, getting the right, getting the right mix of those things in an embedded package that can also be, like, shaken and baked in all the

Peter [00:47:00]: conditions that these things have to have to operate in. But yeah, I think that they’re only going to keep getting better and so we also try to plan our strategy understanding that, we know the rate of improvements of these systems.

Swyx [00:47:11]: Yeah. So like, Google just released the Gemma 2B model

Swyx [00:47:15]: that effective 2B model. Is that useful to you guys or is that too big?

Peter [00:47:18]: You can run that model on an embedded system, definitely.

Peter [00:47:21]: the So yes, it’s, it’s useful in that regard. The bigger question is, like, what do you use it for in an embedded system? Like, you actually need to customize it quite a bit to make it useful for something. But yeah, you could run a two billion parameter model, definitely.

Swyx [00:47:35]: It also interesting, like, what percent is a custom ML model that only does that thing versus a generalist LLM

Swyx [00:47:41]: which probably is not that useful actually for your context.

Peter [00:47:46]: Like, you, like, you can imagine different use cases, right?

Peter [00:47:48]: So the

Swyx [00:47:49]: The voice stuff, yes.

Peter [00:47:49]: Yeah, the voice test. Totally, yes.

Peter [00:47:51]: So for the actual, autonomy elements, that’s 100% in-house. We do every bit of that, the data simulation, the model, everything. But when you get into the more generic use cases like voice or voice assistant kind of thing, that’s where these more generalist models like Gemma actually can be quite, can be quite useful.

Swyx [00:48:09]: Yeah. And then there’s also obviously a trade-off between, like, what percent must you do on machine, versus just call home.

Peter [00:48:16]: Yeah. It’s all about latency.

Swyx [00:48:17]: Latency.

Peter [00:48:17]: It’s all about latency. Yeah.

Swyx [00:48:18]: Yeah. Well, like, I think actually in a lot of contexts, especially in the US, you can just have a connection to the web.

Qasar [00:48:26]: Yeah. I think though most of our universe is everything has to be fairly, embedded and local because just the nature of Even in the US there’s a lot of like

Swyx [00:48:39]: Patchiness

Qasar [00:48:40]: don’t have

Qasar [00:48:41]: have coverage, right? And if you look at, like, the old world of autonomy within mining, which is, like, long before transformers and kind of, neural networks, in the like CNN and kind of a universe, they were really just hand-coded, systems. They were just like, this machine is gonna run to that place with this

Peter [00:49:03]: That was our GPS, like very accurate GPS.

Qasar [00:49:05]: Yeah. And so that worked, and that worked for 20 years, so why would we actually need to use transformers or kind of more modern end-to-end systems? Mainly because you can only really run a path and run backwards. That provided a lot of value, but m-Not as much as you get when the machine is actually intelligent. It’s, it’s seeing, it’s perceiving, it’s acting in a dynamic world.

Alessio [00:49:28]: I looked up RTK, real-time kinematic, one to two-centimeter accuracy.

Qasar [00:49:32]: Yeah. Fantastic. But the and fantastic in faraway lands where there’s not gonna be cell phone coverage.

Peter [00:49:39]: Yeah, so it’s widely used on the legacy mining and agricultural autonomy systems today. So like, for example, a combine that can be precise within one or two centimeters as it’s driving down the field, they use RTK.

Qasar [00:49:53]: Yes.

Peter [00:49:53]: But it’s, it’s expensive.

Qasar [00:49:54]: Yeah. And it’s, it’s, it’s autonomy, but it’s not intelligent in the way that I think all of us

Qasar [00:49:58]: if in twenty-six we’d be talking about intelligence.

Alessio [00:50:00]: In one of your blog posts, you mentioned research on large scale transformers that are similar to those doing modern generative AI. What are, like, the big differences other than, “You’re absolutely right. I should steer the car, so you probably wanna remove that?”

Peter [00:50:14]: We have a diversified bet strategy internally, and the reason we’ve done that is because we operate in now a bunch of industries, a bunch of geographies, and each of the approaches has, obviously a different risk to them.

Peter [00:50:27]: And so like, we’re not going to put all of our eggs in a single basket for a single approach because that approach may not work out.

Peter [00:50:36]: and so that’s, that’s one of the bets that we have, and it has certain advantages in certain scenarios, and then But the way that these things play out in practice is it has certain benefits and also has certain drawbacks. And then, and then the research team tries to then work on, the situations where that’s actually worse than these other approaches and to ultimately arrive at a really great solution for all of these things.

Plan Mode for Physical Systems and Next-Token Prediction Universally

Alessio [00:50:57]: Is there a plan mode for physical autonomy, like the other planning step and then, action step or?

Peter [00:51:03]: So short answer is yes, right? So just like you can use, Claude code to plan out some complex coding task and you get some almost specification written out, those similar approaches absolutely can be applied to physical systems because imagine you’re trying to accomplish some task. The easiest to think about is robotaxi, but I think

Peter [00:51:23]: things get more interesting, let’s say, in the defense context or in the in the mining context. You actually do have to think about many steps in advance.

Peter [00:51:32]: It’s, it’s not just this one thing, but to accomplish the goal, there’s a hundred steps, and then the this concept of the plan mode, it’s, yeah, very applicable, in those

Alessio [00:51:40]: Yeah. I was gonna say, to me, driving feels like a great next token prediction thing because you’re kinda like on a path and like, it doesn’t really matter what you’ve done before. you can always turn around.

Qasar [00:51:49]: It’s all planning. Yeah.

Alessio [00:51:50]: Yeah. Versus, like, mining, it’s like, “Oh, man, I took a I took a scoop out of this thing.” It’s like, now we can’t really

Alessio [00:51:57]: I can’t really go there anymore. it’s like, is there like a huge difference? Like, how would you I guess, like, do you have like a taxonomy of, like, these different types? So there’s kinda like driving

Alessio [00:52:07]: excavating, like, flying. How do you

Peter [00:52:11]: So the interesting thing is, yeah, I think probably everything in the world can actually be boiled down to, like, a next token prediction problem.

Peter [00:52:18]: and in any workflow, anything, can be thought of almost as like there’s this sequence of steps or the sequence of trajectories or what-whatever you wanna call it, and it can be boiled down actually to that sort of thing. And in the mining case, you can imagine, like, taking that scoop. Okay, that was that set of tokens, and now that’s, the model is now understanding that, okay, that the state space is different, and now the next time I do token predictions, it’s going to, going to be modified by that. But yeah, these The remarkable thing about these techniques is just how universally applicable they are, right? it’s, it’s truly is incredible.

Alessio [00:52:53]: What else is underrated about what you guys are building on the physical side? I think there I mean, we were talking about it before the episode. There’s a lot of humanoid companies that do these great demos, and then I can’t buy it, so obviously it can’t all be there. In your case, you’re, like, in production on real streets with, like, a lot of customers. What are, like, the things people are underestimating? The same way the Waymo demos seven years ago were great and then took seven years to actually get them on the street. Can you share about maybe like, the last one percent that was really hard to get done technically?

Productionization: The 20 Problems Every Robotics Demo Will Hit

Peter [00:53:27]: Yeah. So certainly, productionizing stuff is really challenging no matter what. So I maybe would, I would split the answer maybe into research and then also in production. First, on the production side, there’s just so many problems that you find when you actually get the stuff to go in the real world. And so the classic problem in humanoids right now is these systems are actually pretty brittle.

Peter [00:53:48]: and so I’m not talking about any one company, but just as an industry, these systems are pretty brittle. interestingly, I saw this thing, the other day that, I think China is doing a marathon with humanoids.

Qasar [00:54:00]: What?

Peter [00:54:00]: Yeah. So in government, and not China specifically, but in any government, there is a there’s a concept called, prize policy, which is so that there’s, there’s different ways of influencing an industry to go a certain direction. Like, you can, you can regulate it, right? You can do mandates, or you can actually just do these competitions. So the US version of this was the DARPA Grand Challenge. that

Alessio [00:54:20]: That worked.

Peter [00:54:21]: But it really worked. It

Alessio [00:54:22]: That really worked

Peter [00:54:22]: took the whole industry. But I think China is literally doing this marathon because they know that reliability, of these humanoids is a problem. And so what cooler way to solve that than to have a competition where humanoids need to run twenty-six miles, right?

Alessio [00:54:37]: Are we there? Can robots run a marathon?

Peter [00:54:40]: I think it’s happening any day now.

Peter [00:54:42]: So it’s

Alessio [00:54:43]: So we’re there.

Qasar [00:54:43]: By the way, also, automotive, there’s a version of this which is, like, twenty-four Hours Le Mans, right?

Qasar [00:54:48]: It’s like Porsche wins twenty-four Hours Le Mans

Alessio [00:54:51]: New product

Qasar [00:54:51]: and then literally puts those, the products into production. I would actually break it down. You, talk about research and you talk about production. There’s actually a step in the middle which is, like, advanced engineering, and I think a lot of the industry is moving into advanced engineering where it’s like it’s not fundamental research. Like, we’re coming in with novel techniques. It really is advanced engineering for production. So what are the subcomponents that are gonna limit to getting into production? Once you’re in production, you’re dealing with another set of problems which is, like, the deployment, maintenance, of those machines that exist. So I’d say, at least in our field-We’re mostly in advanced engineering in the like, automotive parlance.

Peter [00:55:29]: honestly, every step is hard though.

Alessio [00:55:33]: Paul, this way you’re worth 15 billion dollars, so don’t answer.

Qasar [00:55:36]: You bleed every step.

Qasar [00:55:38]: Yeah. And I think

Peter [00:55:39]: It’s fun. I think it’s like, I don’t know. I find it really enjoyable. Yeah, but what it was also fun is like, so we’ve, we’ve been doing this now for almost ten years, and we’ve just seen, we’ve seen so much bad times. And so right now we can look at any company in this space and like, get a demo, and like, I can, I can write down a list of I know exactly the next 20 problems they’re gonna hit.

Peter [00:55:59]: And like, and I can guess also what they’re going to try to solve each of those, and I can guess which one’s gonna actually work.

Qasar [00:56:04]: Yeah. It’s not because we’re, like, particularly, like, geniuses.

Peter [00:56:07]: We’ve just seen this stuff now.

Qasar [00:56:07]: Yeah. We’ve seen enough of this stuff. We lived enough of this stuff. We, our own kind of mental models of the world as leads in the company, we’ve tried so many things and many of We’re talking about the winds here. Like

Qasar [00:56:21]: There

Peter [00:56:21]: Plenty of losses there.

Qasar [00:56:21]: There’s plenty of losses among that many people doing that many different things and so that kinda, like, get baked into your, like

Qasar [00:56:29]: mental model of the world.

Peter [00:56:30]: Yeah. But I would say and in general, like, we’re excited about robotics for sure, and like

Peter [00:56:34]: the

Qasar [00:56:36]: Massive opportunity

Peter [00:56:37]: massive opportunity and what’s, what’s happening now in the industry is like none of these concept are new, right? What’s new is, like, this stuff is actually working now.

Peter [00:56:46]: Right? The people have wanted to use, neural nets robotics for a long time, but now, like, again, we now have the data sets, we have the simulation technologies where stuff is actually starting to really work, and yeah, we wanna be part, we

Peter [00:56:58]: we’re gonna be part of that for sure.

Alessio [00:57:00]: Do you have requests for startups or like, advice against starting certain startups? There’s a lot of, like, scale-up robotics, companies. It’s like what do you think are things

Qasar [00:57:10]: A lot of, a lot of applied intuitions for other things.

Qasar [00:57:14]: I think you hit a you hit a certain, what is it, badge when YC

Peter [00:57:21]: X for Y

Qasar [00:57:21]: right, you become like, or literally the same similar names, like,? I think my biggest advice, in this, like, almost like commercialization of technology is I think often the that constraint, so we talked about, like, hardware constraints, or we talked about, there’s also, like, on the commercial side, there’s constraints, which is we’re gonna only do things that fit in this box. That is, I think very good for founders. The reason I think it’s not often focused on is because you have plenty of access to capital, and the technical problems are so hard you’re like, “I already have a constraint,” which is just getting this technical problem solved, and I think the venture community, generally speaking, tends to be not very technical. For them, if you just say, “If we solve this thing, it’s gonna be a lot of money,” that’s kind of enough for them, but you as a founder, I’m not giving you advice on how to pitch VCs. That’ll work for VCs. You still gotta run a sustainable business. And I think we’re really in that, question you asked earlier about kind of, what’s maybe not obvious about our company. It’s like this is truly compounding technology. A lot of the work that we do just compounds. we don’t throw it away. It gets better. The operating system work gets better. The dev tooling gets better. The models get better, and so we’re really gonna get a hu- I think you see it in Waymo as an example. Like, Waymo is a company that is, I would say, very interesting for a long time, but not worth one hundred and twenty-six billion dollars, right? So what happens, like, is that the human brain just doesn’t emotionally understand the compounding effects, so that’s gonna happen in our universe. So now if you’re a founder, you’re at the beginning of that long, walk. If you can put a little constraint on commercials that has a small ability for you to more likely see the other end of that, the that walk, ‘cause if you can get to the other end, you will get the big return from compounding technology. Just a lot of people just don’t make it. So yeah. summarize, like, think a little bit about the equation of how you use money and where you use the limited resources and limited engineers that you have. I think sometimes then founders falsely kind of take very mature companies’ strategies and then apply to their, like, nascent. They’re like, “Oh, well, Steve Jobs says be completely vertical.” Well, yeah, in 2007, Apple is very different than 1978 and 1982. Those companies were different. They were literally just taking electronics from other manufacturers and just putting it in an enclosure. And so just be a bit more like, I don’t know, be a bit more nuanced in your, in your commercial approach as it informs your technical approach.

Founder Advice: Constraints, Compounding Tech, and Mature-Company Mimicry

Alessio [01:00:03]: Do you feel differently today? Like, you just joined X, right?

Alessio [01:00:06]: You’ve been building this company

Alessio [01:00:08]: you’ve been building this company in stealth, and now you’re like, “Well, I should probably be talking about what I’m doing.” I think a lot of founders are in a similar way where they wanna raise a lot of money to signal they’re strong, and you raise a lot of money without spending it.

Qasar [01:00:20]: And to hire. And to hire, yeah.

Alessio [01:00:21]: You obviously like that. Do you think that’s still possible to, like, have a very narrow approach of, like, “Hey, we’re kinda like building a compounding thing without a grand vision right away,” versus

Qasar [01:00:32]: It’s, it’s very difficult to answer very general questions

Alessio [01:00:35]: Well

Qasar [01:00:35]: that, I, but I, so maybe like, maybe I reframe it as in is it possible to build a product that has a small, let’s say, problem space and hope that the problem space will grow? Maybe that’s, like, a different way of asking the same question but ma- more answerable. I think always yes. That is the old YC, like, go really deep and then, rather than very broad and shallow.

Qasar [01:01:00]: Very broad and shallow unfortunately, there’s just too many especially in hard tech companies, there’s just too many problems, and you can’you’re gonna do all of them in a very mediocre way, and so the full product is actually fairly mediocre. So yeah, I still in, I’m still in the camp of find a small problem space. The other question you’re asking is a tangential is, like, should you, like, build in stealth and anonymity? Well, yeah, if you’re a YC COO

Qasar [01:01:28]: you can be

Swyx [01:01:29]: Oh, Travis Kalanick.

Qasar [01:01:29]: And we, yeah, we worked, we worked, together at Google. We have a long history, and we don’t And which means, which is another way of saying we have big networks. our first of 400 people, majority were Googlers. Like, a majority of the company came from, this giant company we worked at, and that’s just very different. You’re a founder who is doesn’t have that experience. You have to do these things. And I think it’s kinda, that’s a so it’s like just don’t take my version of the world or whatever other founder, Jensen’s version of the world. They are in different time and space.

Qasar [01:02:02]: And most importantly, their companies are in a different phase.

Qasar [01:02:06]: And so then if you wanna take inspiration from other really young companies, that’s also bad because most of them are gonna fail.

Qasar [01:02:11]: So the only, the only solution you really have is use first principle thinking and say, “Based on my skills, my co-founder’s skills, the skills of my early team members, and the what I’m hearing from customers, what’s a product space that I should, I should build?” And

Qasar [01:02:26]: Yeah. Does that make sense?

Swyx [01:02:27]: Yeah, it does.

Alessio [01:02:27]: Yeah. I, Sam Altman, he said he regrets a lot of the advice that he’s given in YC.

Alessio [01:02:33]: So I’m always curious to ask, founders like you who’ve now been

Qasar [01:02:36]: So I

Alessio [01:02:36]: Just a long time ago

Qasar [01:02:37]: everyone who leaves YC, like, does the opposite.

Qasar [01:02:41]: well, Sam was president, I was COO.

Qasar [01:02:43]: Right? So and we’d have a CEO, so we worked together, extremely closely would be an understatement

Qasar [01:02:48]: ‘cause the firm was also small. The

Alessio [01:02:50]: Yep

Qasar [01:02:50]: YC wasn’t wasn’t as big as, like, an OpenAI is. I directionally agree with that, but I would say that’s not more of a YC function, it’s more of the market

Qasar [01:03:02]: has changed.

Qasar [01:03:03]: It is a different world. The AI industry is at the AI companies, I should say more specifically, and how they relate to the other YC companies and market, just so fundamentally different. The amount of money raised is different, the amount of investors, the sheer number of seed funds. One of our early investors is Floodgate, and they did some analysis in the late, 2000, like, double O’s, where they were like, “There’s, like, single-digit number of funds that were like Floodgate,” which were, like, writing sub $1 million checks, first checks, and they were not accelerating incubator. And Anne, who’s, who’s one of the co-founders there, with Mike, they said that today they try to do, or like, today as in, like, three, four years ago, they tried to do this analysis and they, like, lost count at, like

Qasar [01:03:46]: 350 funds or something like that. So we’re just in a different environment, so the YC advice from 2014-

Qasar [01:03:55]: just would not apply in 2026. But Sam is, like, way better at saying these things than me.

Qasar [01:04:00]: Like, he sometimes makes sound like He says it in a shorter, most, more interesting and than me. I can just give you, like, the Like, I, like, if you ask me, like, “What is the purpose of a car?” Like, open the owner’s manual and I say

Qasar [01:04:13]: “Number one, look, there’s a steering wheel,” and instead of, like, “It can change your life and will be there.”

Alessio [01:04:21]: Yeah, it gives you autonomy and freedom.

Qasar [01:04:22]: Yeah, exactly. Yeah.

Swyx [01:04:24]: and then for Peter, I was just kinda curious if there’s any particular tech or research problem that you would call out as very meaningful for you guys if it was solved, and unsolved, and if anyone is working on it, they should get in touch with you.

Peter [01:04:40]: Yeah, I think th- generally the making models very efficient, right? So because we have to run on actual vehicles, like physical AI is literally, it’s taking, like, very large AI and now making it very small and very efficient. And so we’re constantly just at that boundary of these limitations of, like, well, you have a great model, but now we need to make it faster and smaller and so that in general as a as a field. And then I would say also, folks that are just really passionate about, like, evaluating this technology. As in, like, mo- model evals, is, it’s a hugely difficult topic, especially in safety critical systems. And we have a I think a really great engineering team that works on this now and researchers, but it’s, it’s a big area of investment. And so yeah, folks that are passionate about, yeah, performance, I say model performance, both in terms of capability and literally latency, and then, and then evaluation of models.

Hiring Philosophy: Hardware/Software Boundary and Engineering Mindset

Alessio [01:05:41]: Awesome. You guys, any, specific engineering roles that you’re hiring for? And especially, like, who are people that succeed at your company as engineers? I think that’s always the most important thing.

Qasar [01:05:50]: Yeah. fly.co/careers, I think there’s, there’s literally hundreds of roles. we’re looking at all the topics we talked about from, dev tooling and physical AI to operating systems, to autonomy and AI, within physical machines. The types of engineers, that’s a great question. That’s actually more interesting than

Qasar [01:06:09]: the roles ‘cause we’re, we’re a large enough company, we’re roughly

Alessio [01:06:11]: Hiring everything.

Qasar [01:06:12]: Everything, yeah. We hire everything.

Qasar [01:06:14]: Yeah. I think we’re a Sunnyvale company and I think just from this conversation and kind of our backgrounds, you can kind of predict a little bit of what that means. we tend to hire fairly serious people, who are, who understand low-level systems, not just like a as a superficial understanding of technology, like engineers’ engineers almost. We definitely hire folks who are, like, have some diverse skill sets. We hire tons of specialists as well, to be very clear, but they’ve seen production and I think that, ‘cause that really informs how you, how you build technology.

Peter [01:06:53]: Yeah. I would say people that really appreciate the hardware-software boundary.

Qasar [01:06:56]: Yeah, exactly.

Peter [01:06:56]: definitely in the vibe coding era, there are a crop of engineers that they don’t think about hardware at all.

Peter [01:07:05]: And we don’t have that luxury, and so people that are a little more passionate about going a little bit deeper.

Qasar [01:07:09]: Yeah, if you’re to contrast us versus, like, a AI lab or something, that’s where you’re gonna get the biggest contrast, which is, like, we’re just dealing with reality. what other things? All of the classic stuff. you want, you want folks who work hard and who are, who love the technology and like-Like a podcast like this or rather

Qasar [01:07:30]: Like, if you made it to this part of the podcast

Qasar [01:07:33]: you’re probably qualified for or you’re interested in this.

Swyx [01:07:37]: Yeah. And Peter said that he, likes the podcast as well, which is like

Swyx [01:07:42]: really cool.

Qasar [01:07:43]: I’m a I’m a fan. Yeah.

Swyx [01:07:44]: Yeah. Specifically on the hardware-software boundary part, it’s, it’s something I think about of our education system, in the States, but also maybe just in generally. I feel like there is that retreat away from that classical computer science or EE education

Qasar [01:07:59]: Computer engineering or Yeah.

Swyx [01:08:01]: And like, is there a point where you just do it yourself? Like, ‘cause at this point, you guys are the world experts on this, and actually you shouldn’t wait for some college system to spit them out for you.

Peter [01:08:11]: you mean the in terms of education and upskilling kind of thing?

Swyx [01:08:14]: Yeah. Yeah, just grab, like, young

Qasar [01:08:16]: General Motors already did it.

Swyx [01:08:17]: Smart kids.

Peter [01:08:19]: GMI.

Qasar [01:08:19]: Literally.

Swyx [01:08:19]: Is there a Harvard University?

Qasar [01:08:21]: Yeah, that’s where I went to for undergrad. Went to the General Motors Institute.

Swyx [01:08:25]: I, that did not come up. I saw HBS.

Swyx [01:08:27]: I didn’t

Qasar [01:08:27]: Everyone sees HBS.

Qasar [01:08:31]: The Harvard brand, Lewis is high.

Swyx [01:08:34]: What’s General Motors Institute like? What

Qasar [01:08:36]: it started 100 years ago for, to answer this exact question, literally the question you just said, which is like

Qasar [01:08:40]: not enough engineers in Michigan. you’re talking about the early days of the modern corporation

Qasar [01:08:45]: General Motors being There’s a great book, Alfred P. Sloan’s, My Years with General Motors, that is highly recommended, which basically talks about what becomes a modern corporation. But a part of that is they’re like, “We are, we’re basically buffering on engineers.” So they started a school and actually even Google as most, as recent as probably 10 years ago was thinking of starting a university. In term there was discussions on it. So yeah, it was abso- we definitely up, we definitely upskill folks as well. The amount of training we do in term is actually surprising. Yeah. But it’s a luxury you have when you’re at our size.

General Motors Institute, Education, and the Curiosity Mindset

Qasar [01:09:20]: When you’re, like, 25 engineers

Swyx [01:09:22]: No.

Qasar [01:09:22]: you just gotta survive. So again, take advice that’s relevant for your company rather than, like, immediately start trying to take high schoolers

Qasar [01:09:29]: and make them engineers.

Swyx [01:09:30]: But I, like I did go up to a class that you taught ‘cause, like, it sounds like you can teach a lot.

Peter [01:09:36]: Yeah. Well, I think honestly, the one of the most amazing use cases of these large models now is education, right?

Peter [01:09:42]: Like, I’ve, I’ve taken, an engineer who, very good engineer, aerospace engineering background, and in a relatively short time span, like, he’s doing very confident front-end work, very confident back-end work, like, with the help of these models.

Peter [01:09:57]: And like, not only can you do the implementation with them, but you can also just learn, right? It’s like you ask questions and you don’t feel embarrassed ‘cause the model’s

Peter [01:10:04]: not gonna, model’s not gonna call you out on anything.

Qasar [01:10:07]: Yeah. I think the I think the thing you probably need more than an engineering degree, though engineering degrees are, like, very important, like, I don’t know if there’s a way to shortcut, like, fluid dynamics or heat transfer

Peter [01:10:17]: The fundamental stuff

Qasar [01:10:17]: the fundamental stuff, at least on the mechanical side, is you need an engineering mindset and that sometimes is actually Not everybody actually has that. Some people are emotionally drawn towards arts or something else and that’s completely fine. There’s no judgment there. But I think the engineering mindset maybe in a more usable way is, like, wanting to understand a lower level and the lower level and the lower Like, how do photons move?

Peter [01:10:42]: And extreme curiosity.

Qasar [01:10:44]: Extreme curiosity. Like, what is light? What is a radio wave? Like, these really fundamental questions.

Peter [01:10:49]: Right. If and if you get curious enough about software, you ultimately end up in hardware.

Peter [01:10:55]: And so

Swyx [01:10:56]: That’s the Alan Kay quote. Yeah.

Qasar [01:10:57]: Yeah, exactly.

Swyx [01:10:58]: So I’m trying to make analogies and then do all these things. Like, you’re kind of a blend between new General Motors and Tesla autonomy division for everyone else.

Qasar [01:11:07]: we do work in all these other fields. I think if you talk to our trucking customers, they wouldn’t even perceive, they, like, some sense like, “Oh, you guys did some automotive stuff, but you’re, you’re really helping us.” So

Swyx [01:11:18]: Automotive is not trucking?

Qasar [01:11:19]: No. no. That’s, that’s

Swyx [01:11:20]: It’s, like, a whole

Qasar [01:11:21]: It’s, it’s, it’s, it’s separate. There’s different problems. The mass And you have, you have the general categories of on-road and off-road. I think that’s what you’re thinking. So there’s on-road and off-road, but within on-road there’s all these subclasses

Swyx [01:11:33]: Oh, okay

Qasar [01:11:33]: of machines. Especially when you talk about, you look at, a delivery robot that doesn’t have a human in it. That’s actually very different because now you’re not concerned with, like, the actual feeling that you have

Qasar [01:11:45]: when you’re in a self-driving system. You don’t have to account for that. You can

Swyx [01:11:48]: Just break.

Qasar [01:11:48]: You can, you break hard.

Qasar [01:11:50]: And you don’t care about jerk and all of these metrics don’t, or become in

Peter [01:11:53]: The way to think about it, honestly, is a little bit like, any system that you as an as a human would need special training to operate, you can think of a little bit differently. So like, the license to operate a truck is different from the license to operate a car

Peter [01:12:04]: which is different from the license to fly a plane. It’s different from You get it, right?

Swyx [01:12:08]: Awesome, guys. Thank you for taking the time.

Qasar [01:12:10]: Yeah, thanks for having us.

Peter [01:12:11]: Thanks for having us.

Peter [01:12:11]: Thank you. [outro music]

---

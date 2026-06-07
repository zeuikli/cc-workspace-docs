# 🔬 Latent Space — 2026-05-15

> swyx 開發者簡報，未公開專案 + 工程視角
> 來源：[Latent Space](https://www.latent.space/feed)

---

## [AI-Native Healthcare: 100M Doctor Visits, 10–20 Hours Saved, Prior Auth in Minutes — Janie Lee & Chai Asawa, Abridge](https://www.latent.space/p/abridge)
*🔬 Latent Space | 2026-05-14*

_Special discounts up for[AIE Melbourne](http://ai.engineer/melbourne) ([LS discount](http://ai.engineer/mb)) and [AIE World's Fair](http://ai.engineer/wf) (group discounts up to 25% - [CFPs still open for Autoresearch and Vertical AI](https://www.latent.space/p/ainews-ai-engineer-worlds-fair-autoresearch)) Cya there!_

* * *

Abridge **did not** start as an "GPT wrapper". It was founded in 2018, years before the Cambrian explosion of AI application layer companies. OpenAI launched ChatGPT publicly on November 30, 2022 and by then, **[Abridge](https://www.abridge.com/about)** had already spent years doing the unglamorous work of building trust for one of the highest context, most important workflows in healthcare: **the conversation between a patient and a clinician.**

[](https://substackcdn.com/image/fetch/$s_!MX36!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F967bcd77-27ed-4487-bcc1-28c3d66d057c_2018x1576.png)

Abridge's original wedge was **clinical documentation**. Listen to the visit, generate the note, reduce the clerical burden, and let clinicians spend more time with patients instead of the EHR. By focusing on how doctors actually document, how health systems actually buy, how EHR integration actually works, how clinicians verify outputs, and how missing context during a visit turns into downstream friction across billing, prior authorization, quality, and follow-up, **the adoption of LLMs became a force multiplier** on a workflow already optimized for sensitive context gathering.

The company has scaled fast: Abridge says it is projected to support **80M+ patient-clinician conversations** this year across **250** large and complex U.S. health systems, with support for **28+ languages** and **50+ specialties**. It raised **[$300M at a $5.3B valuation](https://www.abridge.com/blog/series-e)**[ in June 2025](https://www.abridge.com/blog/series-e), after a [$250M round earlier that year](https://www.abridge.com/blog/series-d).

[](https://substackcdn.com/image/fetch/$s_!EAxq!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F994c46e8-d0f0-44ad-96e0-6531a31268b0_1962x1718.png)

Today, **Janie Lee** and **Chaitanya "Chai" Asawa** of Abridge join us for [another crossover pod](https://www.latent.space/p/unsupervised-learning-2026) with **Redpoint 's** **Jacob** **Effron** (who is on the board of Abridge) to dive into how Abridge is building the clinical intelligence layer for healthcare starting with ambient documentation, then expanding into clinical decision support, prior authorization, payer/provider/pharma workflows, and eventually real-time agents that act before, during, and after the patient conversation. 

We go inside the product, data, infra, **evals** , workflow, privacy, and org design choices behind bringing AI into one of the highest-stakes enterprise environments from 100M+ medical conversations and specialty-specific evals to real-time alerts, EHR integration, de-identification, clinician-scientist teams, and why healthcare may solve some of the hardest AI problems first.

We discuss:

  * Why Abridge started with **clinical documentation, "pajama time," and saving clinicians 10-20 hours a week**

  * **The transition from ambient scribe to clinical intelligence layer:** save time, save money, and save lives

  * Why conversations between patients and clinicians may be **the most important workflow** in healthcare ([patient visit summary feature](https://www.abridge.com/blog/patient-visit-summaries--now-generated-in-real-time))

  * **Chai 's "healthcare-coded Glean" framing:** context is king, but healthcare raises the stakes on safety, evals, and rollout

  * **Why Abridge wants AI to feel like "air conditioning":** always in the background, but only interrupting when it truly matters

  * **The prior authorization example:** turning a denied MRI weeks later into real-time guidance while the patient is still in the room

  * Why payer policies, EHR data, medical literature, and hospital-specific guidelines make the problem hard, and also create **the moat**

  * **How Abridge thinks about ambient form factors:** mobile, desktop, in-room devices, nursing workflows, multimodality, and future AR

  * **The multi-sided healthcare customer:** CMIOs, CFOs, CIOs, clinicians, patients, payers, and pharma

  * **The hardest AI problem at Abridge:** high-quality, low-latency, low-cost real-time support in a high-stakes clinical setting

  * When Abridge uses **frontier models vs proprietary models** , and why its unique data from medical conversations matters

  * Why **" every agent is a coding agent underneath,"** and how the EHR can be thought of as a filesystem for healthcare agents

  * How Abridge approaches personalization across individual doctors, specialties, and health systems

  * Why **" AI slop" is AI without context**, and how edits, memories, and clinician preferences create a data flywheel

  * **Abridge 's eval stack:** LFDs, LLM judges, in-house clinicians, third-party evaluators, specialty-specific evals, and progressive rollout

  * HIPAA, PHI, de-identification, one-way anonymization, customer contracts, and learning from healthcare data safely

  * **What changes when you operate at 100M+ conversations:** reliability, cost, post-training, model routing, and infrastructure optimization

  * Why the same clinical conversation can serve doctors, patients, payers, pharma, and future clinical-trial workflows

  * How Abridge works with **EHRs** , and why deep interoperability is table stakes for clinician adoption

  * Why healthcare AI has **regulatory tailwinds, why 80/20 does not work here** , and why high-stakes domains may drive AI forward

  * Why Abridge embeds **" clinician scientists"** into product and eval teams

  * What Chai learned from **Glean** about search, quality, and durable AI infrastructure

  * Why the future of AI infra may look like **context layers** , event-driven systems, Kafka, Temporal, sockets, CRDTs, and tools built for humans

  * Why Janie changed her mind on "**PRDs are dead, "** and why crisp written clarity matters more in complex AI products

  * How Abridge uses **Claude Code, Cursor, and coding agents** internally




* * *

**Abridge:**

  * **Website:** <https://www.abridge.com/>

  * **X:** <https://x.com/AbridgeHQ>




**Janie Lee:**

  * **LinkedIn:** <https://www.linkedin.com/in/janiejlee>




**Chaitanya "Chai" Asawa:**

  * **LinkedIn:** <https://www.linkedin.com/in/casawa>




* * *

## Timestamps

00:00:00 Introduction and what Abridge does

00:02:05 From ambient documentation to clinical intelligence

00:04:04 Clinical decision support and context as king

00:06:57 Alert fatigue, proactive intelligence, and prior authorization

00:12:36 Ambient AI form factors and healthcare customers

00:16:59 The hardest AI problems in healthcare

00:18:26 Frontier models, proprietary data, and model strategy

00:21:07 The EHR as a filesystem for agents

00:24:03 Personalization, memory, and clinician preferences

00:30:40 Evals, LLM judges, and progressive rollout

00:36:47 HIPAA, de-identification, and privacy

00:39:21 100M conversations and operating at scale

00:44:10 EHR integration and the clinical intelligence layer

00:46:39 Healthcare regulation, latency, and high-stakes AI

00:50:11 Clinician scientists and long-tail quality

00:53:04 Lessons from Glean and durable AI infrastructure

00:57:03 The future of agentic healthcare workflows

00:57:34 PRDs, product clarity, and building serious AI products

01:03:11 AI coding tools at Abridge

01:04:06 Outro

* * *

# Transcript

## Introduction: Abridge, Clinical Intelligence, and the Latent Space x Unsupervised Learning Crossover

**Swyx [00:00:00]:** Okay. This is a special crossover Latent Space Unsupervised Learning pod.

**Jacob [00:00:07]:** Very excited to do this.

**Jacob [00:00:08]:** At this point, we get together once a year.

**Swyx [00:00:10]:** Once a year

**Jacob [00:00:11]:** And this is a fun occasion to get to do it on.

**Swyx [00:00:13]:** I really wanted to talk to Abridge but I felt very underqualified because healthcare is not something we cover very intensely. It just so happens that Redpoint's our big investors and supporters of Abridge.

**Jacob [00:00:27]:** Anytime you want to have a portfolio company on your podcast

**Jacob [00:00:29]:** Please, by all means.

**Swyx [00:00:31]:** So we'll introduce our guests. Chai and Janie, welcome to the pod.

**Janie [00:00:34]:** Thanks for having us.

**Chai [00:00:35]:** Thank you.

**Janie [00:00:35]:** We're excited to be here.

**Chai [00:00:36]:** Thank you.

**Swyx [00:00:36]:** So for listeners, what do you guys do, just to situate you guys in the company?

**Janie [00:00:42]:** Abridge is a clinical intelligence layer for health systems. We really started with documentation and building for clinicians and as we think about reducing the burden that clinicians have, they're spending 10 to 20 hours a week on documentation. There's a massive doctor shortage in the country. We also think that conversations between patients and clinicians are probably the most important workflow in healthcare. It's where care is given and received but if you think about the 20% of our GDP that goes towards healthcare, almost everything is a derivative of that conversation, whether it's the claim, the payment, the actual diagnosis given, the treatment. And we've started with a conversation to reduce the burden for doctors on documentation but we're really excited about the path ahead as we become this broader clinical intelligence layer.

**Chai [00:01:34]:** I'm Chai. I work on clinical decision support at Abridge.

**Swyx [00:01:37]:** Yes.

**Chai [00:01:37]:** And so as Janie said, we're uniquely situated where we started off with the clinical note. What I'm really excited about and where we're expanding towards is what are all the things you can do before the conversation, during the conversation and after the conversation if you did have access to all the context about patients, payer guidelines, medical literature and put that together and to serve, how healthcare could look fundamentally different.

**Swyx [00:02:01]:** And that's the context engine that you guys have?

**Chai [00:02:04]:** Yes.

**Swyx [00:02:04]:** Is that what it's called? Okay.

**Swyx [00:02:05]:** So historically, as I understand it, the company started in 2018. A lot of people would be familiar with the AI voice notes form factor that doctors would be "Well, do you consent to being recorded?" It replaces handwriting and what have you. But it sounds like more recently there's been a big transition in the company. Tell me about the broader transition.

## From Documentation to Clinical Intelligence: Save Time, Save Money, Save Lives

**Janie [00:02:26]:** So from a transition perspective, we really think about our journey as The first act was: how do we help save time? And that's where a lot of that original product was.

**Swyx [00:02:37]:** By the way, one of those interesting stats

**Swyx [00:02:39]:** On your landing page was, doctors spend time after hours.

**Janie [00:02:43]:** They call it pajama time.

**Swyx [00:02:44]:** Why is that pajama time?

**Janie [00:02:46]:** Doctors after work in their pajamas

**Swyx [00:02:48]:** In their pajamas. Oh

**Janie [00:02:49]:** At home are just writing and catching up on their notes every day.

**Janie [00:02:53]:** Some of our favorite customer love stories, we have a Slack channel called Love Stories. We have clinicians telling us, "Abridge has helped us, from retiring early or we're now finally able to

**Janie [00:03:06]:** go home and eat dinner with our kids for the first time."

**Chai [00:03:08]:** Save the marriage in some cases.

**Swyx [00:03:10]:** One of the quotes was "We're not divorcing anymore."

**Swyx [00:03:12]:** I'm asking, "Why?"

**Swyx [00:03:14]:** Because they're working too much.

**Janie [00:03:16]:** But, in terms of where we're going and where we're expanding, we really think about our second and third acts around how do we help health systems save and make more money. Health systems are operating with record-low operating margins. It's getting harder and harder to serve patients and they have regulatory, some tailwinds but also a lot of headwinds coming their way and AI is ripe for helping on the saving and make-more-money piece. And then ultimately, how do we help save lives? The fact that our software and our product is open millions of times a week before, during and after a patient walks in the room, gives us massive opportunity with products like clinical decision support, which Chai is building but so many others to improve patient outcomes and probably one of the most important workflows and problems to be going after right now.

## From Glean to Healthcare: Context Is King

**Jacob [00:04:04]:** One thing that's interesting, Chai, is you came over to Abridge from Glean and clinical decision support, which for our listeners is, in the context of a visit, helping a doctor figure out the right type of care. It's really a search problem in many ways, going through lots of different data sources. Very analogous to your previous role as one of the earliest engineers over at Glean. I'm sure a lot of our listeners are curious what's similar about the problems that you're going after now and what feels different, now that you're in healthcare.

**Chai [00:04:33]:** Very similar. Taking a step back, with every wave, there's a lot of very similar patterns that happen across different products. A lot of social networking products look the same. A lot of credit-based products look the same. And we're seeing that very similar in the agent era with many companies, of course, in Redpoint's portfolio and so forth. And the key insight between both companies is that you have amazing models but context is king. Context is what puts them to work. So I see it in a lot of ways, a lot of similarities in this is a healthcare-coded version of Glean but the differences are really interesting. A couple things that come to mind. First and foremost, the rigor of the setting we're in. The downside risk is extremely high here in healthcare. It can be fatal in some cases. You prescribe something that the patient is allergic to for example. Whereas at Glean, it's "Oh, you got the question wrong." It wasn't the end of the world in most cases. And so what does that mean? That shapes our evaluation strategy, both offline evaluation, progressive rollout and there's a lot more we could go into there. Second thing that comes to mind is, vertical versus horizontal. In both cases, there's a large variance but when Glean is, it's a much more horizontal company, there's a variance of personas, companies that you're working with. We also have a variance of personas, different types of specialties, different hospital systems. But the variance is a little more narrow. So from a product perspective, you're able to focus far more, especially when you have a maturing technology and you're building new products that never existed before. It lets you go after them much more easily and especially in healthcare where so many problems were solved with labor and process, that it's extremely ripe for AI to keep helping augment and enable. And the final thing that's really interesting, Abridge specifically compared to many other companies in the AI area, is the modality we started with where we're ambient and we're always listening in the background. And many more AI products will go that way but it's how we started. And that's the greatest form of AI we can create, AI that's seamless. You're not looking at your screen. It's always there. It's always helping you out and being proactive. The Jarvis vision that, every hackathon I went to over the past decade, there was always a Jarvis competitor. But Abridge very much started from the opportunity and continues to go that way.

## Ambient AI and Alert Fatigue: When Should the Product Interrupt?

**Jacob [00:06:57]:** One thing that is super interesting then from a product perspective is you have this always-on seamless in the background and then you have to decide when you break the wall almost and say, "Hey, clinician, you might not have thought about X," or whatever it is that you want to do. And in healthcare traditionally there's been this idea of alert fatigue and a million pop-ups and then a doctor just ignores all of them. It's probably a pattern that a lot of builders are thinking through now. How do you think about the right way to intervene or to pop up in a doctor visit?

**Janie [00:07:26]:** It's such a good question. Alerts are notorious in healthcare specifically. Over 90% of alerts are ignored. The first and most important thing is context is everything, as Chai alluded to and I also think about how do we go from being reactive alerting to really proactive intelligence at the point at which it matters most. One thing we like to say is we want our product to feel like air conditioning. It should be in the background just making things better and if there is something that has great clinical risk and we're acutely aware that intervening now and not later is incredibly important, we should decide to act. But if you think about proactive versus reactive, instead of alerting a clinician during a visit when they're with their patient having a pretty serious and sensitive conversation, how do we prep a clinician before they walk into the room with that patient? And so historically, clinicians might have to manually go through charts with a patient that they've had over the course of months or years and they'll try to suss out what are the things they should be doing. You can imagine a world with Abridge. We'll summarize all of the most recent context for you, tell you based on the reason for a visit the patient is coming in for the types of things you should be discussing. And so you're going into that conversation prepped rather than walking in cold to that patient visit and then having this product interrupt you five or 10 times throughout the visit. And there might be times where it's really important to interrupt. We have a product called Prior Authorization and so this is when you may go into a doctor's office with knee pain. They'll prescribe you an MRI and so many of us have had this experience before, where in four weeks you'll get a call saying, "Hey, Sean, that MRI that you were prescribed wasn't approved and why don't you come back in? We'll figure it out." In a world with Abridge, we might choose to quietly but still alert a doctor in that visit. And alert is probably not even the word we would want to use. Before a patient leaves, we would want to tell the doctor, "Hey, Doctor, before Sean leaves, you should ask him, has he had physical therapy and has his pain lasted for more than six weeks? Because the Aetna plan that he's on in California requires six things. We've already confirmed four of them have been met 'cause we have all the context. But these two last criteria, if you can address with Sean before he leaves the room, we could guarantee that your MRI is approved before you leave." And so when you think about clinical usefulness, impact to the patient, there are instances in which if we can catch a doctor while the patient is still in the room, as we think about save time, save money, save lives, we get to check all of those boxes. But when doctors have 15 minutes between visits, we have to be really thoughtful about when it matters.

## Prior Authorization: Reducing Latency in Care

**Chai [00:10:23]:** There's this interesting product opportunity AI has is reducing latency in the world. For example, prior authorization is an example of where care gets delayed and so great AI can reduce that. And the problem with alerts before partially is a technical problem: the quality of your alerts really matters. They're going to get ignored if you get alerts that... Similarly in engineering, where they're noisy alerts that you can't act on. But if you can make really high-quality alerts with both the context, as Janie said, and really high-quality models, then you can create a whole other game.

**Janie [00:10:53]:** And I really like that experience because it starts to tease apart, what makes this so hard and unique. One, to make that prior authorization example possible, think about all the data that you need to have. You need to integrate with the electronic health record to know all of the patient context. Do we have access to your previous labs, previous imaging? And then to match you and to know that you're on Aetna, we have to collect all of the different payer policies and they vary by state. Some of these payer policies live on websites. Some of them live in unstructured 50-page PDF files.

**Jacob [00:11:31]:** I thought this episode was

**Jacob [00:11:31]:** To make sure we didn't scare people from healthcare.

**Janie [00:11:34]:** But when you think about the things that make it hard, it also gives you the moat.

**Janie [00:11:39]:** And then the second is the AI and the model quality we need to be able to hang our hat on. And so the bar, similarly when I worked at Opendoor, I worked on pricing models. Every outlier wiped out the margins of 30 and so similarly here in healthcare, the bar for accuracy is so high. And then I'd say the last is workflow is everything. If insurance companies deploy AI, it typically happens too late and this is when you have the notorious comical examples of AI just fighting each other when it's too late. But if we can pull forward the use of both the AI but also the ability to solve problems when the patient's in the room, you can start to collapse what typically takes weeks or months after your visit, ideally down to minutes or real-time. And it's where healthcare is both very difficult but also extremely rewarding if you can crack it.

## Product Form Factors: Mobile, Desktop, In-Room Devices, and AR

**Swyx [00:12:36]:** Just to get some baseline on the form factors, because I've seen some videos on your website and stuff. You guys talk a lot about ambient AI. Is it primarily on the phone? Is there any other form factor that people get Abridge in? Is there an Abridge room setup where it's always on? I don't know.

**Jacob [00:12:55]:** An Abridge podcast studio.

**Janie [00:12:58]:** Primary form factor is mobile and desktop. Usually

**Janie [00:13:00]:** Clinicians are walking in and out of rooms with mobile but at the end of the day, when they're closing out their notes or wanting to prep for the day ahead, they might use desktop. We have been having a lot of really interesting partnership conversations with a lot of these in-room device companies as you think about the power of multimodality and even more data, as you think about all of what is not captured today. It is fascinating to think about, especially even as we go into building and scaling our nursing product. It's one where nurses constantly, as they're walking in to check in on a patient for two minutes or maybe even 30 seconds,

**Janie [00:13:43]:** Starting an Abridge experience is probably going to take longer than the visit. And so what can we do with in-room devices that are always on starts to raise really interesting and fun product questions.

**Swyx [00:13:54]:** I was thinking, the way in tech companies we have all these Google Meet

**Swyx [00:13:58]:** And other things, we might as well set up entire rooms with just Abridge tech.

**Chai [00:14:02]:** Very much. AR glasses and related form factors are also relevant: how do we bring the information to the clinician in real-time without a screen, while still letting them focus on the patient?

**Swyx [00:14:18]:** Do you think they want that? I'm skeptical of AR, but I'm curious what you've tried.

**Chai [00:14:26]:** Admittedly, it's not a near-term product roadmap

**Chai [00:14:29]:** By any means. I'm being far-fetched.

**Jacob [00:14:31]:** There's some sick AR stuff for surgeries.

**Swyx [00:14:33]:** Really?

**Jacob [00:14:33]:** When people are trying to visualize, you're about to make an incision but you want to see, what the cut might look or what the body might look like inside and they can layer in imaging.

**Swyx [00:14:43]:** That's cool.

**Chai [00:14:45]:** At some point in the future.

**Janie [00:14:46]:** But there are a lot of our largest customers and at the largest health systems integrating already and so even as we think about building into it, unlocks a lot of product capabilities.

**Swyx [00:14:57]:** And just to establish the terminology. Sorry, and I know I'm asking basic questions somewhat for myself but also for the audience who might be

## Health Systems, Buyers, Clinicians, Patients, and Payers

**Swyx [00:15:05]:** Less integrated. When you say health systems, it's like the Johns Hopkins, the Kaiser Permanentes.

**Janie [00:15:09]:** Mayos, the Kaisers of the world.

**Swyx [00:15:10]:** These are your customers, right? And the outcome that you deliver for them is happier doctors, reduced cost of processing, reduced mistakes. It's weird in a sense that I feel like there's also, a secondary customer, the customer of the customer and I don't know if you -- do you think about it that way?

**Janie [00:15:28]:** The other interesting and complex part of building product is we have our buyers, who are the chief medical information officers

**Janie [00:15:39]:** The chief financial officers, the CIOs of these large health systems. Our users today are clinicians but if you think about who downstream is impacted, it's patients. And so as we build, with every product in mind, we think about who we're building for, who the secondary user is and what does that mean either in terms of experience, security compliance, ROI that we have to make tangible. And so like you said, time savings is one of them. But for CFOs, they care a lot more than just time savings. We have to show for every dollar you put into Abridge, because you have more compliant documentation or because you have fewer queries coming from your billing team, we save or add real dollars to your bottom line or top line, are things that we're constantly thinking about because of the dynamic across all three sets of users.

**Chai [00:16:32]:** There's a whole other axis too with the payers and pharma

**Chai [00:16:35]:** as well. Connecting all these three big stakeholders in healthcare is

**Swyx [00:16:39]:** Do the payers ever see your data? Sorry, the payers meaning the insurers, right?

**Chai [00:16:44]:** Yes.

**Swyx [00:16:44]:** They also see Abridge data?

**Chai [00:16:47]:** No

**Swyx [00:16:47]:** Like the direct integration to you guys

**Chai [00:16:48]:** They wouldn't see the raw Abridge data but when you're working together on something like prior authorization, whatever information they need, we'd communicate to them.

**Jacob [00:16:59]:** That's cool. I would love to dig into the AI side. You still have a lot of problems on the AI side. And so maybe to start at the highest level, what's one of the hardest problems you have to solve in AI at Abridge today?

## The Hardest AI Problems: Quality, Latency, and Cost

**Chai [00:17:11]:** To make things simple, let's take, building off the prior auth example. So one thing Janie talked about is okay, this data is all over the place and there's this combinatorial explosion of procedures, payer policies and even sometimes different health systems. There can be some cross-product of all of these different considerations you have to take into account. But what's really hard about this problem is doing it real-time in the conversation. So, in any AI product, usually the three KPIs you care about are quality, latency and cost. Now, what we're saying is we want you to do this real-time in the conversation, guiding the clinician. How do we do it in a way that does not break the bank? But we're using -- But we also need very intelligent models because you're working with this cross-product of data and this, all this context layer as well. So you need high intelligence and high-quality because you don't want the alert fatigue but you also need to be fast and cost-effective. And so that's where a lot of clever engineering goes. It's okay, without getting into all the details here, can you model these policies in some intermediate representation or other things that you can do that can make this problem tractable? And of course, the Pareto frontier is always changing but we are also trying to do this now.

## Model Strategy: Third-Party Models, Proprietary Data, and Medical Conversations

**Jacob [00:18:26]:** What implications has that had for what you take off-the-shelf and say, " what? We don't need to be world-class at X. We'll just take this from the model providers or from some infrastructure player," and what you're "No, this is where we spend most of our time focused on"?

**Chai [00:18:38]:** This is, the fun challenge in AI?

**Jacob [00:18:42]:** It changes every three months? So

**Chai [00:18:42]:** Of course, with the shifting landscape, we try to be extremely thoughtful on predicting the trends of where third-party models are going and where we can uniquely go. And, sometimes when you talk about AI models, we're the models are just going to get infinitely better. But I don't think... It may be in the grandness of time you could say that but, within every month, every quarter, there's specific ways they're getting better. They're training on a lot more, coding data to be better coding agents, for example. And so

**Chai [00:19:14]:** We have to think about where are the things that won't -- unique data that we're uniquely training on or to step back a little, where is a proprietary model bringing advantage to us is if it can give higher quality or lower cost and latency for similar quality, very similar to many other companies. And when we can do that is when we have proprietary data. So, for example, we have on the order of eighty million or hundreds of millions now getting close to of medical conversations.

**Jacob [00:19:44]:** It's insane.

**Chai [00:19:45]:** This is a unique data set. And this data set, it's very interesting because this data set is effectively a large part of the trace between the patient and the provider. That's where the quote-unquote debugging happens in healthcare. We have these traces at scale, as in as, our CEOs even called it, an exhaust that comes out of our product. And so when you have these traces, that's how you can train better agents on certain use cases, whether it's your transcription diarization use cases or so on or like note generation models and we can do that much cheaper and faster. But we're always also working with these third-party model providers. We closely collaborate with them and that's how we predict where the trends are going. The thing that I think about a lot is that, I know that the model providers are going to train much more on agentic workflows and so forth, so that's great, so that you have a better agentic harness. But the other thing that's interesting is that the model providers, because a large class of the consumer model providers is healthcare queries, that they might, optimize to train a lot of healthcare data to encode the knowledge in its weights. And this is just a great thing for us as well, where the off-the-shelf models can keep bett-getting better at general healthcare information, such that what our strategy is, we have a constellation of models, we can use something for this, that and, we only care about, at the end of the day, the best product experience.

## EHR as File System: Agentic Workflows and Real-Time Interfaces

**Jacob [00:21:07]:** And, you have, overall capabilities improving. I'm curious, as these models get better, is there something you look at and you're ", three months ago, we really couldn't do that but God, the the latest models really allow us to do it"?

**Chai [00:21:19]:** So here's something interesting that I've, been toying with. So all models are... This wasn't super obvious a year ago but now it's become clear and clear that almost every agent is a coding agent underneath the hood? So you give it whatever file system, it can write its own code and so forth. So when you think about within healthcare and the use case that we have, you can think of the EHR effectively like a file system. It's just -- it's a storage of all this information. It's a lot of information there that cannot fit into the context window, at least of today's models and you want to use that context effectively for all these product use cases we're talking about. And so if you have better agents that can, manipulate data, read that data, treat it as a file system as we see they're going and we know model companies are investing this way, then that very directly benefits us.

**Swyx [00:22:09]:** Yeah. Okay, cool. Again, just establishing basic things. But we're going back to the model stuff. I'm really interested in double-clicking more on the real-time, element, which is pretty important for both of you. Is it -- Is real-time just batches of every one minute, every five minutes? Is that how we do it? Or is there some more native, genuinely real-time in the sense that OpenAI has a real-time API or Gemini has a real-time API?

**Chai [00:22:35]:** Yeah. Yeah. So today it is more on the on the batch basis but there's interesting

**Chai [00:22:41]:** Prototypes that we have that we're still not fully, full time, voice in text out or in that sense. But, can you trigger your models, your agents or agentic workflows, depending on the right times in the conversation?

**Chai [00:22:58]:** And so you can imagine, different techniques to bring this latency down and, you want to bring the feedback loop down as much as you can. And so a lot of clever engineering there without fully... Maybe one day we'll do full voice in and text out, train a model to do something like that.

**Swyx [00:23:15]:** You do -- People don't want voice in voice out?

**Chai [00:23:18]:** Now we aren't creating experiences that are, during the conversation, inter -- It's almost like

**Swyx [00:23:25]:** Might be too disruptive

**Chai [00:23:26]:** Too disruptive until, who knows, maybe eventually you could have full voice agents once we -- the quality and we improve the comfort of the technology. But right now gra -- that change is much more gradual and it's more text focus, text out.

**Janie [00:23:42]:** And so much of currently what our product is trying to do is allow a clinician to focus on their patient and maybe at some point but right now patients, clinicians don't want a third voice, at least in a literal voice in that room. And so how do we be there with all the contacts and information ready at hand when there's the right moment?

## Personalization: Individual Doctors, Specialties, and Health Systems

**Jacob [00:24:03]:** Jenny, one thing I'm curious about is how you think about, personalization in the product. I imagine, every doctor is a special snowflake in their own way, has their own way they like to do things. There are probably a bunch of different approaches you could take to doing that, both within the model layer itself but then also just with clever prompting or engineering. How do you

**Jacob [00:24:20]:** Deliver on that?

**Janie [00:24:21]:** It's such a good question. Personalization is massive for us. We think about personalization at three levels. The first is at the individual, the second is at the specialty level and then the third is at the health system or the organization level. To your point, there are a lot of individual preferences. You-When a note is produced, it almost is a reflection that is so deeply personal of a doctor's work and how they give care. And so do they have preferences on things like style? They might want bullets versus paragraphs, really concise versus comprehensive. They also might have phrases that they really like to use or the templates that they want every note to be structured. And, we see it in our feedback all the time. We want two spaces in between sentences or I refuse to use this tool. And so that's something that we've had to build in. And the tricky part is how do you make sure that stylistic preferences don't interrupt accuracy and quality and that's something that we've really had to refine and hone over time. Second is at the specialty level. A cardiologist note or workflow is going to look very different from a dermatologist workflow.

**Jacob [00:25:32]:** I assume cardiology notes are the highest stakes for you guys, given your CEO is a cardiologist.

**Jacob [00:25:36]:** It's "Oh my God, make sure we get this one."

**Janie [00:25:37]:** Shiv, our CEO, is still a practicing cardiologist. He rounds once a month. And so, first call when we want just quick and easy user feedback too.

**Janie [00:25:46]:** But, specialties require a lot of personalization, both in terms of what does the product look and so we make sure that as new users onboard, we catch that and the product proportionally reflects that. But also on the back end, evals at the specialty level, they are hard-earned to calibrate and get. What does a really great dermatology note look like? What makes it complete? What makes it compliant and billable is very different than a primary care doctor. And so it's not just about what does the product experience look but on the back end tuning and really deepening our understanding for the specialists. What does great output look like? And that's, a problem that we need to calibrate internally, externally, online, offline but, takes lots of cycles but is necessary in a high-stakes environment. And then at the health system level, for products like clinical decision support, you have health systems who've spent years or decades refining their best practices and they want to know, "Hey, we love your clinical decision support product but how do we embed our own hospital guidelines into them to inform clinicians before, during or after a visit what brest -- best practices should look like?" And as you think about, deepening moats as well, when health systems, trust us with that data, allow us to productize it and directly into the clinical workflow, makes us a really great partner to health systems who want to build something that truly meets their needs, their practicing guidelines.

## AI Slop, Memory, and Product Data Flywheels

**Chai [00:27:23]:** And I want to add onto that. The for the clinical documentation problem, it's very similar to AI writing that doesn't feel like your own and then we call that slop. But the way I describe one framing of slop is like AI without context. But we have all that context and both the clinicians, can have it and can guide it. And so part of the other interesting exhaust for us is, memory is, one of these new systems records

**Chai [00:27:49]:** Almost.

**Janie [00:27:50]:** And we also have all the edits people make on our product and when you think about a data flywheel and how we get better over time becomes really powerful as a mechanism to just going deeper in personalization.

**Jacob [00:28:04]:** It's interesting. I love this idea of working with systems on the guidelines they built up over a long time. I feel like so many of the best AI app companies today are... The question is: How do you take the expertise that a law firm or a bank has built up over many years and then add that as context and also a special sauce over, a an AI tool? And so seems like y'all are really doing that very effectively.

**Janie [00:28:24]:** We're now starting to have our customers ask, "What are other customers doing?"

**Janie [00:28:28]:** "And how are they doing it?"

**Janie [00:28:30]:** And as we think about having visibility across such a large set of care being delivered right now, a really interesting place we could also partner.

**Swyx [00:28:40]:** I'm just curious. I -- This may be a nothing question but, how different are health system guidelines from each other? Don't they all converge to the same thing? And if not, where do they differ?

**Chai [00:28:52]:** At a really high level, they're going to talk about very similar things but the difference is probably in some more of the details. "Oh, you should refer to specialists only when XYZ conditions are met," or so forth and maybe different organizations have different practices and guidelines around that. But high level, talking about similar things but the details are what, of course, that shapes the context and the decisions you make.

**Swyx [00:29:15]:** And this all goes into the context engine and it might affect the notes but maybe not.

**Chai [00:29:21]:** The -- For these local pathways, we're definitely thinking about it a little more for our clinical decision support product.

**Chai [00:29:26]:** So yeah.

**Swyx [00:29:27]:** Which is your stuff, yeah.

**Swyx [00:29:28]:** And then the memory which you raised, let's just tell us more about that. What have you tried in memory? What's the structure of the memory? What works? What doesn't work?

**Chai [00:29:38]:** There's, of course, many different ways you could do memory, where it's okay, can you bake it into the model weights or can you do it in some external store? For us, what's interesting is, of course, when you think the models are rapidly changing, whether it's in-house or third-party, baking into the model weights, sometimes you worry that it could be a little throwaway. And so, how do you... You need to find a way that you decompose the problem, the preferences from the underlying models and so forth. The thing we're right now most both that's easiest to start with and we're excited about is having, a separate store for memory, where you have, for example, a memory sub-agent that's, working in the background, figuring out what are the important parts of the clinician's actions that we want to remember for the long term. And then you can also imagine, other things where in the -- you have background jobs that are running that are collating these, memories similar to Sleep, of course and what other pattern, patterns products do as well. Learning over all these action, all the action data we have, again, note edits, the conversations they did and the actual transcripts.

## Evals: LFD, LLM Judges, and Clinical Safety

**Jacob [00:30:40]:** What about evals? How in the world do you... It is such a complex product surface area. We would love to hear you riff on that and also how has that evolved? I'm sure you've gotten better at it, so any learnings along the way.

**Janie [00:30:50]:** From an evals perspective, we, from day one when we build any new product or feature, we think about, what does good look like? And there are table stakes things like clinical safety but then you start to get deeper into what does good quality look like. And when you go into something like our core product, there's stuff like style and completeness and there's things like does this note become something that can be billable, which is very high stakes for a health system. We have a number of ways in which we get confidence for this. We have, internal in-house clinicians who do what we call an LFD process to give us our very first pass at is this or isn't this a good enough output, look at the effing data.

**Jacob [00:31:41]:** LFD?

**Chai [00:31:42]:** That's why I was smiling. I was "Is Janie going to mention what it stands for?"

**Jacob [00:31:46]:** I was not... There's like a million acronyms.

**Jacob [00:31:48]:** How am I supposed to know that I don't? So "Oh yeah, of course, an LFD."

**Swyx [00:31:51]:** I've never heard of LFDs.

**Chai [00:31:53]:** It's a bridge for sure.

**Janie [00:31:55]:** I got through three days and then I had to ask someone.

**Janie [00:31:58]:** I thought it was just me that didn't know

**Janie [00:32:01]:** It's our internal process.

**Swyx [00:32:02]:** But look at the data as a meme in ML, 'cause you tend to not look at it. You just want to look at number go up.

**Chai [00:32:06]:** Exactly.

**Swyx [00:32:07]:** But yes.

**Janie [00:32:08]:** But so, we make sure we look at the data and then as we think about all of the components of good output, we, one, create LLM judges across all of these and we make sure with annotated data and either internal or external evaluators, we feel like these judges are calibrated. And then depending on the stakes, we also work with in-house and third-party evaluators across all of these before we ship any big change. And the goal is, in terms of evolution, how do you go from this process taking months, down to weeks, down to days? Some of it is, a true science and ML problem. A lot of it's also just, hard operational work. Have you planned ahead in terms of what you need? Have you really optimized the capacity that you need across all of the different specialties you need? Have you gotten a really good sense of which third parties are great to work with for what use cases? This takes a lot of domain, expertise and, lots of mistakes and errors in figuring that out. And so as much of it is an ML problem, so much of it has also been operational gains that are hugely important, where domain-specific expertise is everything.

## Specialty-Level Evaluation and Progressive Rollouts

**Jacob [00:33:23]:** But it's funny, 'cause I feel like people talk about healthcare like it's one giant market and the reality is

**Jacob [00:33:26]:** It's, dozens and dozens of sub-markets. And so it feels like in your evals you have to build that up across the board, probably.

**Swyx [00:33:34]:** And is specialization the primary cardinality at... That's the word that comes to mind.

**Janie [00:33:40]:** Sometimes, depending on the product or the use case. And so if we're making a note improvement or feature for a particular specialty, definitely but we have products that are for nurses. We have products that, are really aimed at making the document or the output a lot more billable. And so we'll want to work with coding teams and not necessary clinicians. And so like

**Jacob [00:34:05]:** Coding meaning healthcare coding.

**Janie [00:34:06]:** Yes. Yes.

**Jacob [00:34:07]:** Not

**Chai [00:34:07]:** Yes. I see you.

**Swyx [00:34:07]:** Other kinds.

**Janie [00:34:09]:** But is this output proportional to the work that was delivered? Is there sufficient documentation to justify the amount that a health system may end up charging? And so, specialty sometimes but also domain, very different across all of the different products that we're working for. And building out that network is, not easy and is where a lot of our operational investments have gone into.

**Chai [00:34:35]:** And I view a lot of analogies to self-driving cars here, where, part of it is we really want progressive rollout of features to test in the real world is this useful? Is this going to work? One big difference compared to past lives is before I'd build a product, maybe I'd alpha it and then I'd like GA it the next week, 'cause I'm "Go, move fast, ship," and whatnot. But the mentality is like you... I want to make contact with the reality as quick as possible but I want a progressive rollout. Because as much as I get as large of an offline eval set, I want the distribution of that to match real-life distribution. And over time, by rolling out early, similar to Waymo has a tagline, "The world's most experienced driver," another thing that can, at least linearly increase for us is, both the size of our evaluation offline and online, that and it all feeds back.

**Janie [00:35:25]:** Something that's been earned over time, speaking of evolution, is just the trust we've gotten with customers. Historically, a lot of these health systems, when they bring on new vendors, their release cycles are quarters, sometimes twice a year. We've gotten our customers onto monthly release cycles, which is pretty fast for health systems but what is more exciting over the last, call it, few quarters, has been, a subset of our customers have said, "We want to innovate with you. We trust you," and we have a pretty, decent chunk of our customers who say, "We'll develop with you outside of these monthly release cycles. We have a higher tolerance. We know that the stakes are very high but we want to be the first ones using these products, giving you feedback." And so for a pretty substantial set of our customers, we've been able to convince them to be able to ship, in this gradual way before GA. Something we talk about a lot internally is, trust is earned in drops, earned in buckets and so we still can't do what I used to do when I worked at Loom. We had 30 million users. I'd just be, rolling out experiments left and. The bar is still quite high for iterative rollout but because of the trust we've earned, we're able to learn at pretty high volume very quickly.

## Privacy, HIPAA, and De-Identification

**Swyx [00:36:45]:** Your scale is still pretty huge.

**Swyx [00:36:47]:** One thing I want to... We were going to go into scale? In a sec. One thing I wanted to call up, follow up on evals, which, again, just coming from a generalist engineer point of view, just thinking through what would people be scared of in doing this, the privacy and HIPAA

**Jacob [00:37:00]:** Elements of this. I have zero experience in that. What do you have to do? What is surprisingly not that bad?

**Chai [00:37:06]:** So one thing that's really important here from a compliance perspective is very much that any of the data we use needs to be de-identified, any real-world data we use as a basis of online eval sets we're learning from. And so you have to -- And there's, very clear, government guidelines, what counts as PHI. And so we've even have built models that can take, for example, a clinical transcript and remove all the key PHI indicators and so you have a scrubbed/de-identified version. And then once you... And so one thing that's important is first you've got to get confidence in that model in the first place? And prove that out. Because, now you have, multiple probabilistic systems on top of each other.

**Chai [00:37:46]:** But once you have that, then you can train on it use it for evaluation and so forth, provided one of the cool things also that you can do from a business side is the right data contracting as well with your partners.

**Jacob [00:37:57]:** Is the anonymization one way? Once it's done, you cannot undo it? Or is there someone

**Chai [00:38:01]:** Yes

**Jacob [00:38:02]:** Who holds the master key that can... Yeah, okay. So it's one way.

**Chai [00:38:05]:** It's one way. Yeah.

**Jacob [00:38:06]:** That's how it works. I just wanted to... Because, there's a lot of this, learning from feedback and everything that, you would want to debug more but you can't because you just physically don't allow yourself to.

**Janie [00:38:17]:** Some of it's also written in our customer contracts in terms of who can or can't access PHI data, how long do we retain it,

**Jacob [00:38:27]:** Very good

**Janie [00:38:27]:** Before it gets de-identified. And so we have a pretty high bar for who can access that PHI data, just to make sure that we always respect our customer data and privacy. But that's something that we partner with our customers on too, to make sure that as we want full, as close to precision as possible in that quality

**Janie [00:38:48]:** We can still use it.

**Jacob [00:38:50]:** But it'll be fascinating to see how that space evolves? Because you think about, I used to work at a company that, did a lot of healthcare data in the cancer space and if you asked, the average cancer patient, "Hey, do you want people, do you want other patients to be able to learn-"

**Chai [00:39:03]:** Take it.

**Jacob [00:39:03]:** "... Learn from your experience?"

**Chai [00:39:04]:** Take it all.

**Jacob [00:39:05]:** They're "Please."

**Jacob [00:39:06]:** "I'd love, nothing more than for other people to be able to learn from

**Jacob [00:39:10]:** The experience that I had." And so in the past it was a lot harder to do that learning. But with this technology, that might really be practical and so it'll be fascinating to see how that continues to evolve.

**Chai [00:39:21]:** There's so much in our data set of 100 million conversations.

**Chai [00:39:26]:** You can imagine things like insights that you can give to the clinician. How could you, oh, how could you have reacted to this? In coaching or insights around, which treatments are effective or, like... Because you have this, again, this data source that was never captured before but that's, where, intuition or experience is created from, going back to this idea that the conversation is the agent of truth.

## Operating at Scale: Reliability, Cost, and Token Efficiency

**Jacob [00:39:46]:** Back to the 100 million conversations, I feel like you have this insane scale that maybe only a few other AI app companies have and everyone else dreams of. So not everyone has had to confront this yet but maybe just talk about some of the challenges of operating at that scale and what, our listeners have to look forward to if they ever get to this level of scale.

**Chai [00:40:05]:** At large and larger in scale, so of course there's a general, infrastructure reliability. When you... In any given startup, you're building the plane while it's flying. So there's some notion of that. But what gets interesting on the AI and ML side for sure is this, as you get at more and more scale, so one, you have the data to first and foremost do this. But, you start thinking about costs or infrastructure in a whole different way at scale versus, a prototype.

**Chai [00:40:34]:** You can use the most expensive model, you can burn as many tokens as you want but when you're doing 100 million conversations

**Jacob [00:40:41]:** Token max on leaderboards are less upsetting than that context.

**Chai [00:40:45]:** . When you're doing that and so that comes for we have the data and we also have the team that's able to post-train based on this and you can optimize for efficiency, especially in areas where you believe that maybe a lot of the quality headroom is less so and you don't expect the other off-the-shelf models to go that way, such that you want to do, efficiency maximization, in terms of compute and tokens.

**Jacob [00:41:08]:** I feel like you guys live in the future in some way where most use cases today are really just in use case discovery mode, where it's "God, I really hope I can find something that can get to scale," and so you're always going to use the most powerful model. And then the few things that do get to this level of scale, you start to do those optimizations.

**Chai [00:41:22]:** It's a natural trajectory where it's like zero-to-one, we're not talking about any of these optimizations.

**Chai [00:41:26]:** But when maybe we're in the one-to-100 or so forth, then we're in optimization mode and, what works out really well is you've got all this data from zero-to-one that lets you do this.

## What Comes Next: The Conversation as the Shared Healthcare Platform

**Jacob [00:41:36]:** That's fascinating. I feel like one thing that's so interesting about the Abridge footprint is that you're in the doctor-patient visit in real-time. I always like to say, there's like probably 50 years' worth of product you could build on top of that. What gets each of you, I don't know, what are you most excited about building, either in the short term or medium term or even, long down the line?

**Janie [00:41:53]:** Something that I get really excited about is that the same conversation can serve so many stakeholders. If you think about the conversation, a doctor needs to know what is the documentation, how do I make sure that this fully represent the care I gave? A patient needs to know, "What the heck just happened? This was really overwhelming. What are my next steps?" A payer needs to know, was this the proper and appropriate care given? A pharma company might want to know why isn't this drug being properly used or is there a good candidate for this clinical trial that I'm about to run? And where I get excited is that our product and our platform and our infrastructure can be the same product across all of those things and start to what's today, separate, very expensive, complex systems that serve each one of these stakeholders in very different ways, start to collapse all of that into a singular platform that enables not just more efficiency across the board but also better outcomes for everyone. And, all of us experience healthcare in probably very painful ways and knowing that there is a world in which we can simplify a lot is really exciting to me and it all starts with the conversation.

**Chai [00:43:15]:** It's interesting. Of it very similar to going back to the KPIs that any AI product cares about. How do you increase quality of care? How do you reduce latency to care? And how do you reduce costs? Which is a huge, in healthcare

**Jacob [00:43:28]:** They call it the triple aim in healthcare.

**Chai [00:43:30]:** But very similar to building AI products and the thing that really excites me is when we talk about that latency piece, we talked about one example earlier of prior authorization, can you reduce the latency to care? But you can imagine so much more. Oh, as soon as the lab value gets updated, do you have like a background agent that, kicks off and uses all the context to be "Oh, hey, the patient should do this next," for example. And of flagging that to the clinician who's always in the loop but reducing that latency, to care. And then you can imagine this is much further down the road but it's like even connecting that to the direct patient and the consumer. And so how can you, how can you build a bridge to all of these things?

## EHR Partnerships and the Clinical Intelligence Layer

**Jacob [00:44:10]:** Very cool. The connections piece is just an ever-growing thing. And one of the key partners is the EHR and I wonder what that relationship is like. Will they, look at this as, something that is valuable enough that they want to own someday?

**Janie [00:44:29]:** Our partnerships with the EHR is, we know that we have to be extremely close partners with all the EHRs who we partner with. Being able to not only pull and push all of the data into the right places is, not only table stakes, if we can't do that, health systems don't want to use us. The second and the reality of today is clinicians spend a lot of their days in the EHR. So much of what allowed us to win in the largest health systems was pretty direct and, very close partnerships with some of the largest electronic health records that allowed us to pull and push data with APIs that weren't ready out of the box. And clinicians want to save clicks. Anytime we introduce a new product that, adds two clicks for them in their day, they're "We're not going to use it."

**Janie [00:45:21]:** They have 15-minute back-to-back appointments with their patients. They're spending, hours during pajama time doing documentation. Every second and every minute counts and so we really think about being deeply integrated into the EHR as also table stakes to getting real usage and adoption. And anything that we build or introduce, we really talk about earn the right internally a lot, which is we have to provide so much value or save so much time that people will use us. But those are the two things that are close to us, is we know that the product won't be used unless it is deeply interoperable.

**Chai [00:46:01]:** And strategically, to your point, it's like what does EHR want to own versus us? EHRs are really focused on the clinical workflows and so forth but some of the things that we're talking about here, I do these traditionally are outside of the domain where it's oh, connecting pairs and providers together with provider policies or the clinical trial matching, as Janie brought up. And so these are, entirely -- we position ourselves as building this entirely new intelligence, clinical intelligence layer across, again, providers, pharma and, payers.

**Chai [00:46:33]:** And so that's a it's a whole different ballgame that we try to play

**Chai [00:46:36]:** In combination with them.

**Jacob [00:46:37]:** But it's like a different layer of scope.

## Healthcare AI Regulation, Technical Depth, and What Changed Their Minds

**Jacob [00:46:39]:** I'm curious, you are both relatively newcomers to healthcare. People have these, there's lots of futuristic healthcare AI takes of "Oh, everything will look different.", now that you've been in healthcare for a bit, you live at the edge of AI, what have you, changed your mind on around this, as you think about what healthcare looks like in ten, 20 years? Any updates to your mental model from the time being close to the problems?

**Chai [00:47:02]:** One thing that I

**Chai [00:47:04]:** Was hesitant about before and it's a common thing when I'm trying to recruit engineers that people ask me around, is definitely oh, healthcare, heavily regulated space. And it is, rightfully so. You want to keep, the patients at the end of the day safe. But one of the interesting things that, is a that surprised me how much it is coming to the company is there's a lot of really favorable regulatory tailwinds as well. Where you think about, government really wants interoperability between all these systems that we talked about and so agents can access this information. The government just in January, the FDA released updated guidance on clinical decision support, what I work on in such a way that they used to have guidance from like 2022 that required you to have, mention all these options and do all these other things but it's a very forward and forward-looking way. And so for me, what's been really cool to work on is this, there's this very special moment both in AI in general, we all know that but there's a special moment also regulatory in healthcare as well.

**Janie [00:48:05]:** One thing I would call out is for the very reasons things are higher stakes or, potentially considered more difficult in healthcare, it's where some of the hardest AI problems will get solved first, just because the bar is so high. When I first joined, I was "Oh, this is where we'll be on the tail end of where, all of the AI innovation will be able to be applied." But when you think about, zero error evals or multi-step workflows that have really low tolerance, a lot of the innovation will happen here just because we have to or else we can't ship.

**Jacob [00:48:42]:** 'Cause like in other domains, you'd much rather just solve the 80%-is-good-enough problems first

**Janie [00:48:46]:** 80/20 doesn't work here

**Chai [00:48:48]:** And building off that, traditionally, there was a bit of stigma that, oh, healthcare companies are not that interesting from a technical perspective or I've seen that or faced that myself. But these are really hard and fun problems from a pure technical perspective beyond just the impact. How do you bring the latency of this thing down and make it really high-quality?

## Reducing Latency: Clinical Workflows, Agents, and Implementation Reality

**Jacob [00:49:07]:** How do you bring the latency of things down?

**Chai [00:49:10]:** Yeah. Yeah. Yeah. So okay, let's answer the latency question. And maybe hopefully not too redundant with some of the things I've said earlier but some part of it is with any latency, you have to like what is, what is really your bottleneck. In a lot of workflows, it's sometimes it's the model itself. And so that's where like our data flywheel, our post-training team and so forth come in so that can you make the models far more efficient. So that's one aspect of latency. But there's whole other aspects of latency where it's okay, on top of that, if you use a constellation of different models, can you use -- can you first use like a -- it's like thinking fast and slow. Can you use a cheap, fast model that triages and hands it off to a larger model where you get more intelligence and so forth and so all these

**Chai [00:49:56]:** Clever tricks to make it work.

**Chai [00:49:58]:** And by the way, we are totally -- we also realize that the parameter frontier is changing and so these tricks will -- may not get us to where we want to be in five years but we need to if we want to build a useful product right now.

**Jacob [00:50:11]:** Should we go to the quick-fire or you want to ask more about Abridge? We can stuff everything that's not Abridge into the quick-fire

**Swyx [00:50:16]:** I don't mind. I was -- I feel like Janie was on the topic of more long tail stuff, which is

**Swyx [00:50:21]:** Not the eighty/twenty thing and that really matters. And I'll --, if you have any tips or cool stories or just general approaches that have worked for you that's interesting to dig into.

**Janie [00:50:32]:** One of them is even just how we staff our teams looks different than a traditional software engineering team, I'd say.

**Swyx [00:50:40]:** Let's go.

## Clinician Scientists, Edge Cases, and Evals at Scale

**Janie [00:50:41]:** We have a bunch of folks with different roles who are clinicians and so we have this role called the clinician scientist and I heard one of our leaders refer to them as mutants recently. But they are people who've had clinical backgrounds, so MDs typically, who are also deeply technical, somewhere, on the spectrum of like a full stack engineer all the way to like extremely scrappy prompter. But having each of these people embedded within our teams instantly raises the bar for everything that we build because not only are they determining, is this product clinically useful but they're deeply embedded in our whole evals process. And so when we talk about LFDs, when we talk about what is our actual evaluation criteria, you don't want Chai or me creating what those are because we don't have clinical background. But is probably unique to Abridge but has been game changing. And when you think about where the puck is going, you have people build with clinical backgrounds who are technical and where AI tools are going, they just become

**Janie [00:51:53]:** More and more, critical and like the killers of the team. And so that's one. And then the second is just the scale at which we do evals to catch that long tail up front before anything ever gets into production is something that we've pretty much like really started to fine-tune, both from a scale but when do we know we need to get several hundred versus several thousand offline responses, what helps us make that quick decision and make this less of an art and as much of a science as possible. But that's also been something we've had to tune over time.

**Swyx [00:52:27]:** And you have partners who opted in to give you those evals.

**Janie [00:52:31]:** So we work either internally or with third-party for offline evals and then we have customers who also agree to give us, whether it's like thumbs up, thumbs down to like choose this or that, a lot of data to get us to what is as close to fully confident as possible.

**Swyx [00:52:51]:** The term that comes to mind is

**Swyx [00:52:53]:** Like active learning on things where you're weak. I feel like it's a lost art

**Swyx [00:52:58]:** Is a lot of the polish that comes into doing something like this.

**Janie [00:53:02]:** Really.

**Chai [00:53:03]:** Hundred percent.

## Lessons from Glean: Technical Foundations and AI App Infrastructure

**Jacob [00:53:04]:** Maybe, on a totally unrelated note, Chai, you had a very, storied run at Glean before heading over to Abridge. And so, I'm curious like that -- it's was one of the early AI app success stories. As reflecting back on that experience, what do you think Glean got most, maybe most wrong? Yeah, curious for your reflections.

**Chai [00:53:24]:** The... I attribute Glean's success really to very strong technical foundations, that have really stood the test of time. And so it started with -- it started with a known problem and like finding information where work is hard. The best technology at the time was to build really high-quality search. A lot of times enterprise search startups failed because the quality wasn't great enough. But the learning that people took away from that is, oh, enterprise search is not good enough. And so like quality, really changes the game of like if something can be useful or not. It's like similarly like people may have taken it that way, "Oh, Alexa voice assistants are not that useful." But when you have quality, things can change the game. And so Glean's early foundations, by bringing people who had built search at Google, the best place to have ever built search and being really creative and having a very concrete problem to solve but with the right technical backgrounds, laid the foundation for all of its success for the many years to come. And what's interesting is always figuring out, hey, how does a company adapt in this, as we all know and we've talked many times, in this changing landscape. And so for Glean, how do you put this context layer to the use, has been the thing that we've really, the last few years, has been the fun from the challenge. That where like you could say, that's been the opportunity for the company as well as the challenge as well.

**Jacob [00:54:46]:** Definitely a competitive market. It feels like one at the epicenter of the foundation models and, the hyperscalers, so it'll be interesting to see how it all plays out.

**Chai [00:54:55]:** When you think about can you build something that helps everyone at knowledge work as well is a massive opportunity.

**Jacob [00:55:02]:** Always my mental model is like there's a few markets that are like the foundation model companies have to win or are like big enough to go after and It's probably like consumer code and that.

**Jacob [00:55:11]:** And so it would definitely be interesting to see how it plays out. One thing we often think about on the investing side is, the pace of progress in models changes so fast and so the building patterns adjust so fast. And it's always hard to figure out, what pieces of the way people are building today, the infrastructure tools they use, are going to prove persistent versus, okay, six months later we're doing something completely different because

**Jacob [00:55:31]:** Models have improved. I'm curious of the stuff you use today, how do you think about the pieces of AI infrastructure software that feel a little bit more persistent?

**Chai [00:55:40]:** So generally, if you take the thesis that the models are going to be more and more agentic, before we had to build a lot of scaffolding around that. In previous gigs, I've -- we've effectively, we made our own DSL effectively and you can view the because the models were not capable enough, so you needed to simplify things. And you can view it similar to other agent frameworks. But over time, if the models become more and more agentic and can use the similar tools that we already have, where it's like computer use, writing code itself in sandbox, much more around, far more about, what are the right context layers and the tools to give agents. And then the other things that I think about are how do you really build truly event-driven real-time systems and especially at Abridge, again, where you're doing something real-time in the conversation. And so there's a lot of event-driven technology. And by the way, stuff that we've always used in the past, whether it's Kafka, Temporal, Sockets and so forth, how do you bring that together is also durable. Or thinking about patterns in which humans collaborated with each other on Google Docs. How do you think about like CRDT and so forth when you have conflicts, when you have multi-agent systems? So all these things that we've built for -- the things we've built for humans are the things that are going to be, continue to be durable.

**Jacob [00:56:55]:** . Just with like 1,000 times more the scale of agents running at them instead.

**Jacob [00:56:58]:** They're going to really work.

**Chai [00:56:58]:** So make sure that they scale, of course and fast and whatnot. Without a doubt, yes.

## How Agentic Does Abridge Become?

**Swyx [00:57:03]:** Does Abridge become more agentic over time than, what is the next more agentic version of that look like?

**Swyx [00:57:10]:** 'Cause you're already pretty proactive it's, with like the notifications.

**Chai [00:57:15]:** And so I view that as like a piece of being agentic but I also view it as maybe some of the things we mentioned before, oh, reacting to labs or, doing work in the background or doing

**Chai [00:57:25]:** Even more capabilities on behalf of the clinician, who we believe has a super important role to play as, in terms of patient connection and so forth.

## What They Changed Their Minds On: PRDs, Prototypes, and Judgment

**Jacob [00:57:34]:** I'm curious for both of you, what's one thing you've changed your mind on in AI in the past year?

**Janie [00:57:39]:** The one I flopped on and this is much more product specific, is, probably the hotter take is that prototypes are the end all be all and that PRDs are dead.

**Janie [00:57:51]:** We've tried switching and... We continue to evolve the way product is developed and, the products that we're building are extremely complicated and nuanced and it is very difficult for a prototype to capture the full complexity of what can we or can't we do with this data. What and who... Is this the actual right problem to be solving for in a world where software has become so cheap? Yes, this is a cool looking prototype but should we be spending any of our precious hours here? If so, why? And how does this deepen our moat in a world of decreasing moats? Does this require custom implementation from our customer to use? None of that gets captured in a prototype and so we've, we're continuously evolving the way that we develop product here but even if not written in the same traditional ways as it was two years ago, as a team we've gotten pretty, high conviction that in a world of so much noise, crisp written clarity is more important than ever. It might now live in a markdown file that more teams and systems can use as context but that's probably one that is much more

**Swyx [00:59:06]:** So you're

**Janie [00:59:06]:** Function specific to me.

**Jacob [00:59:08]:** I love that.

**Swyx [00:59:09]:** You're disagreeing with the consensus

**Janie [00:59:10]:** That PRDs are dead

**Swyx [00:59:11]:** That's great, yeah.

**Swyx [00:59:12]:** So you are like

**Janie [00:59:14]:** That prototypes are the thing.

**Janie [00:59:14]:** We should partner with AI to create great documentation but first, probably most important, is strategically answering like why is this problem the one our company and our product should solve? What happens if the next 20 competitors build this? Why, what is our right to win and does this help us differentiate in any way or are we just adding noise? It's important

**Swyx [00:59:39]:** That's a high bar. I don't know if I could answer that

**Swyx [00:59:41]:** Because a lot of the times the answer is let's do it first.

**Janie [00:59:44]:** And when the cost of doing it first is so expensive, we just talked through the process of getting something out to customers. You need to have a higher bar for as a business, should we invest here? And as all of our roles evolve, one of product or like all of our jobs become should we do this thing? And that's something that is worth the time spending up front on. And then, as you think about prototypes, it's still really valuable to quickly show, "Here are the 20 ways we could do it. Clinician, I would love your feedback, which one resonates more?" Or as you get into deeper fidelity, you can also make the prototypes deeper fidelity and like get it as close to production ready as possible. But, beyond that, to get it out to customers, there's a lot of implementation details, security compliance, edge cases, things that never get caught in a prototype that need to be written out somewhere. And so they look different but still more important than ever.

**Jacob [01:00:52]:** It's interesting. I imagine a lot of that also is like given the context of the stage that Abridge is at.

**Jacob [01:00:58]:** I feel like for so many early stage companies, it's just a desperate race to... You throw like 30 things at the wall, you're "Please, something just like resonate with my end buyer." and, you find something and that's, why the prototype first approach is so powerful. But for you all, it's like anything you're going to do is across 200 systems, there's like a whole, implementation change management side of things and you get a few big bullets to fire at at what you want those systems to do. And so being really thoughtful about that.

**Chai [01:01:25]:** It makes a ton of sense and maybe the prototype first takes will all grow into your view of the world when they're a bit more scaled.

**Janie [01:01:32]:** The weekend demo versus it works at the largest health systems is, a massive gap. I don't think it means we can't go fast. This is the fastest I've built in my career, right now and the

**Chai [01:01:47]:** Compared to Loom?

**Janie [01:01:48]:** From a the complexity and the scale of the products we're trying to build and the problems we're trying to solve, I'd say, yes, maybe I, updated a flow or, shipped a new feature pretty quickly but if you think about some of the products we're building, we're trying to collapse prior authorization, things that used to take 45 days across maybe 20 different touch points into one. I'm building faster than I ever have and so the thoughtfulness allows us just to go fast at the right things. It sounds contradictory but that

**Chai [01:02:28]:** No

**Janie [01:02:28]:** Thought up front

**Chai [01:02:28]:** Go slow to go fast.

**Janie [01:02:29]:** Exactly.

**Chai [01:02:30]:** It's interesting. In the... When a lot of things are changing and in the AI discourse, sometimes we lose sight of things that always stood the test of time. Judgment and clarity always matters. As an engineer, sometimes I don't want a prototype. I would like to see... I want the written, the clarity that comes from writing and then we build that. And again, for some things, of course, where it's a small thing, yeah, just ship the prototype. That's why, don't sweat the details. So the interesting thing, the nuance that gets lost sometimes in discussion is, sometimes we need to recalibrate our judgment for sure because the costs and gains have changed but that doesn't mean we go all the way on one spectrum or the other.

## AI Tools, Claude Code, and Closing Notes

**Chai [01:03:11]:** Outside of your specific tool, I always like to ask this question, any other AI tools that you guys are enjoying?

**Chai [01:03:16]:** Claude Code. But, that feels, too basic of an answer.

**Chai [01:03:20]:** Is all of Abridge engineering very built on Claude Code?

**Chai [01:03:23]:** Yes.

**Chai [01:03:23]:** Wow.

**Chai [01:03:23]:** Very much so. I won't

**Chai [01:03:26]:** We also have Cursor as well.

**Chai [01:03:28]:** Many of the

**Chai [01:03:29]:** I'm just checking the boxes here.

**Chai [01:03:30]:** Many of the tools available but it's like you look at just earlier in the day, you see an engineer's screen. You see, six different, Claudes running at it. Sometimes the same person, I've seen them on the sofa now with the remote control as well on the mobile. But, very much so. One of the interesting things for me is, as a relatively new person to companies, Claude Code helps me onboard much faster or any of these AI code... And, I feel like I learn so much. I do love the memes of "Claude's going to do this." So, I'd like to see Claude,

**Chai [01:04:00]:** The venture equivalent is "I'd like to see Claude go do a company at a billion dollars pre-revenue." Like

## Where to Learn More: Whitepapers, Research, and AbridgeHQ

**Chai [01:04:06]:** We always like to leave the last word in these conversations to you both. And so, any place you want to point folks where they can go learn more about Abridge, the work you're doing, any of the research you guys have done, whatever. The floor is yours.

**Chai [01:04:18]:** A couple places. If you... On our Abridge website, we have a lot of our whitepapers where we've done a lot of interesting work, such as, reducing a hallucination objection.

**Chai [01:04:27]:** Very well-presented, by the way. I liked it. Yeah.

**Chai [01:04:29]:** Thank you. Our science team rigorously defined what is the problem. And one of the interesting things, by the way, at Abridge, is we have multiple, stats professors on staff as well. So in that specific whitepaper, Michael Oberst, who's a professor at JHU. And so we have multiple... And from that comes, very high rigor and then also our taste for design comes from really good presentation. But setting that aside and we're going to have many more technical topics there, please follow our Twitter account as well, AbridgeHQ. And then the other thing I'll plug a little is, we have a open house of diving deep into AI and healthcare coming up with Andreessen Horowitz.

**Chai [01:05:07]:** Amazing. Well, thanks so much.

**Janie [01:05:09]:** Thanks.

**Chai [01:05:09]:** This was super fun.

**Chai [01:05:10]:** Thanks so much.

**Chai [01:05:10]:** Thank you.

---

## [[AINews] Codex Rises, Claude Meters Programmatic Usage](https://www.latent.space/p/ainews-codex-rises-claude-meters)
*🔬 Latent Space | 2026-05-14*

It has been a tale of two cities in the past 3 weeks since the launch of GPT 5.5; while the finance folks fall in love with [Anthropic's growth](https://www.latent.space/p/ainews-anthropic-growing-10xyear) and [CFO](https://x.com/anquetil/status/2054637012850970631) ahead of its likely October IPO, there has been a notable rise in pro-Codex sentiment among AI Engineers, likely a combination of GPT 5.5 being a really good (in [some scenarios Mythos-tier](https://x.com/mschoening/status/2054565859491029497?s=12)) model, launch of [Codex for Everything Else](https://www.latent.space/p/ainews-agents-for-everything-else), and, a third thing, which is the trigger for today's op-ed: more generous limits.

[](https://substackcdn.com/image/fetch/$s_!uqHa!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1f3bb92f-f1bd-4329-9b9c-64c681eec378_1290x874.png)

The messaging for Claude's pricing change was generally pretty well done, it is simply not what uses of alternative harnesses wanted to hear: [every Claude subscription now gets a monthly credit of API tokens equal to the dollar amount of the Claude subscription plan.](https://x.com/ClaudeDevs/status/2054610152817619388) So you pay $200, you get BOTH a Claude subscription with its own limits for using Claude on Anthropic-owned harnesses like Claude.ai and Claude Code ("interactive usage"), AND $200 worth of API credits for using Claude everywhere else including `claude-p`, OpenClaw and others ("programmatic usage"). 

If things had worked this way from the start, it would have been viewed as a very good deal:

[](https://substackcdn.com/image/fetch/$s_!XQLi!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F148215c3-6a2e-4a77-b243-630d5c9c7247_1228x1640.png)

However, because of the historical subsidy/pricing advantages (estimated between 70-90% discount from API pricing), people are viewing it [as a "rug pull" of sorts](https://x.com/ClaudeDevs/status/2054610152817619388/quotes) -- however it's nice to have an official policy in place as opposed to the selective targeting of [OpenClaw](https://x.com/kloss_xyz/status/2040211360156700843), [OpenCode](https://x.com/thdxr/status/2034730036759339100?s=20), and uncertain status of less popular harnesses.

[](https://substackcdn.com/image/fetch/$s_!w6yx!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F041d6b0a-7ea1-4e96-82ad-750ed4e73f25_1208x1394.png)

That these headlines come on the same day as [OpenAI launches their enterprise switch](https://x.com/OpenAIDevs/status/2054586214112780518/quotes) promo is an incredible coincidence:

[](https://substackcdn.com/image/fetch/$s_!6upS!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F8449d76d-2f12-4dde-a825-744697b02502_1192x1116.png)

At the end of the day, we would caution against reading too much into swings either way - both labs are doing very well, and these are in the grand scheme of things normal pricing shifts by people inventing the future of coding while figuring out optimal pricing as they shake up a decades-old industry. Anthropic was more liberal in the beginning, but now that Claude Code has a sustainable brand and clout as an agent harness, Anthropic is putting its most favorable pricing behind its own tools and metering everything else, whereas Codex as the challenger is being more liberal with everything.

Perhaps hardware is destiny, perhaps this is part of a longer 6 month alternating cycle of the "[mandate equinox](https://x.com/irl_danB/status/2050051868597080482)":

> AI News for 5/12/2026-5/13/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

# **AI Twitter Recap**

**Agent Infrastructure, Harnesses, and Developer Platforms**

  * **Cline, LangChain, Notion, and Cursor all pushed deeper into agent platform territory** : [Cline](https://x.com/cline/status/2054580767779700775) open-sourced a rebuilt **Cline SDK** and refreshed CLI with a TUI, agent teams, scheduled jobs, and connectors, positioning its harness as a reusable substrate for custom coding agents. [LangChain](https://x.com/LangChain/status/2054617687238865013) shipped a large batch of agent lifecycle infrastructure at Interrupt: **LangSmith Engine** , **SmithDB** , **Sandboxes** , **Managed Deep Agents** , **LLM Gateway** , **Context Hub** , and **Deep Agents 0.6**. The most technically notable piece is [SmithDB](https://x.com/LangChain/status/2054658661776244936), a purpose-built observability database for nested, long-running traces with large payloads, reportedly yielding **12 -15×** faster access on key workloads; the team says it is built atop [Apache DataFusion and Vortex](https://x.com/ankush_gola11/status/2054681251513254260). In parallel, [Notion's External Agents API](https://x.com/NotionDevs/status/2054600524423733307) lets third-party agents such as Claude, Codex, Cursor, Decagon, Warp, and Devin operate directly inside Notion as a shared, reviewable context layer rather than another silo. [Cursor](https://x.com/cursor_ai/status/2054651526715502998) expanded cloud agents with fully configured **development environments** including cloned repos, dependencies, version history, rollback, scoped egress, and isolated secrets.

  * **Agent UX is increasingly about long-running state, streaming, and orchestration rather than chat** : Several launches converged on the same design direction. [Duet Agent](https://x.com/dzhng/status/2054619807715348779) proposes a state-machine harness for jobs that last **weeks or months** , with parent/sub-agent coordination and memory replacing compaction. LangChain's OSS updates added [streaming typed projections, checkpoint storage, code interpreter, harness profiles, and model-specific tuning](https://x.com/LangChain_OSS/status/2054641656222388700), all aimed at richer agent event streams than plain tokens. [Tabracadabra](https://x.com/oshaikh13/status/2054613590695641269) moved from autocomplete to a context-aware assistant in any textbox, while [VS Code](https://x.com/code/status/2054669377367064613) introduced an Agents window and better multi-project task review. The architectural message across these releases is that production agents increasingly need **durable execution, inspectable intermediate state, and tool-native UI surfaces** rather than stateless prompt/response loops.




**Model Training, Architecture, and Data Efficiency**

  * **Pretraining efficiency and architectural experimentation were the strongest research throughline** : [Nous Research's Token Superposition Training](https://x.com/NousResearch/status/2054610062836892054) modifies the early phase of pretraining so the model reads/predicts contiguous bags of tokens before reverting to standard next-token prediction; they report **2 -3× wall-clock speedup at matched FLOPs** with no inference-time architecture change, validated from **270M to 3B dense** and **10B-A1B MoE**. [Jonas Geiping et al.](https://x.com/jonasgeiping/status/2054600427128201688) argued current message-based/chat training overly constrains agents to a single stream and released a **multi-stream LLM** paper claiming lower latency, cleaner separation of concerns, and more legible parallel reasoning/tool use; paper and code are linked [here](https://x.com/jonasgeiping/status/2054600457746579816). [δ-mem](https://x.com/dair_ai/status/2054600147020222630) proposed an external online associative memory attached to a frozen full-attention backbone, with an **8 ×8 state** reportedly improving average score by **1.10 ×** and beating non-δ-mem baselines by **1.15 ×**, with larger gains on memory-heavy benchmarks.

  * **Post-training/compression and data curation also produced notable results** : NVIDIA's [Star Elastic](https://x.com/PavloMolchanov/status/2054607257166553292) claims one post-training run can derive a family of reasoning model sizes, at **360 × lower cost than pretraining a family** and **7 × better than SOTA compression**. Datology's VLM work, highlighted by [Siddharth Joshi](https://x.com/sjoshi804/status/2054566179369574419) and [Pratyush Maini](https://x.com/pratyushmaini/status/2054607891202777192), argues **data curation alone** can produce major multimodal gains: **+11.7 points across 20 public VLM benchmarks at 2B** , beating InternVL3.5-2B by roughly **10 points** at about **17 × less training compute**, and near-frontier 4B performance with **3.3 × lower response FLOPs** than Qwen3-VL-4B. On the open data side, [Percy Liang](https://x.com/percyliang/status/2054550981527146942) said the next **Marin** run already has **18T tokens** in its mix and is still seeking more pretraining, mid-training, and SFT data, with a companion token viewer [shared here](https://x.com/percyliang/status/2054550984597328101).

  * **Open evaluation and dataset work is maturing alongside model building** : [Kevin Li's SWE-ZERO-12M-trajectories](https://x.com/kevin_x_li/status/2054600962137100493) is positioned as the largest open agentic trace dataset: **112B tokens, 12M trajectories, 122K PRs, 3K repos, 16 languages**. [Victor Mustar](https://x.com/victormustar/status/2054495700822478943) flagged **llama-eval** as a step toward more comparable llama.cpp community evals. Meanwhile, [Steve Rabinovich](https://x.com/steverab/status/2054564579573698921) and [Sayash Kapoor](https://x.com/sayashk/status/2054569643080077576) argued credible agent evaluation requires **log analysis** , not outcome-only metrics, because stronger agents expose hidden benchmark bugs and reward-hacking paths.




**Enterprise AI Pricing, Platform Competition, and Distribution**

  * **Anthropic vs OpenAI competition sharpened around enterprise distribution and developer lock-in** : [Ramp data cited by Andrew Curran](https://x.com/AndrewCurran_/status/2054582686698848294) showed **Anthropic at 34.4%** of businesses vs **OpenAI at 32.3%** in April, the first apparent lead change in business adoption; [The Rundown](https://x.com/TheRundownAI/status/2054588969044627906) amplified the same figures. At the same time, Anthropic changed plan economics: [ClaudeDevs announced](https://x.com/ClaudeDevs/status/2054610152817619388) that paid Claude plans will get a dedicated monthly credit for programmatic usage across the **Agent SDK** , `claude -p`, GitHub Actions, and third-party SDK apps. This was immediately read by power users as a major restriction on subscription-subsidized harnesses, with criticism from [Theo](https://x.com/theo/status/2054620998205624746), [Jeremy Howard](https://x.com/jeremyphoward/status/2054682882753597603), [Matt Pocock](https://x.com/mattpocockuk/status/2054655310388674693), and [Omar Sanseviero](https://x.com/omarsar0/status/2054679776397300188). Anthropic partially offset that backlash with a separate [50% increase in Claude Code weekly limits](https://x.com/ClaudeDevs/status/2054639777685934564) through July 13, stacked on the previously announced 2× 5-hour limit increase.

  * **OpenAI responded aggressively with Codex enterprise incentives** : [OpenAI Devs](https://x.com/OpenAIDevs/status/2054586214112780518) and [Sam Altman](https://x.com/sama/status/2054626219858293128) offered **two months of free Codex usage** for enterprise customers switching in the next 30 days. OpenAI also published more technical platform detail, including a [Windows sandbox design write-up](https://x.com/reach_vb/status/2054655421013434510) describing the combination of local users, firewall rules, ACLs, write-restricted tokens, DPAPI, and helper executables needed to safely run coding agents with local filesystem/tool access. The competitive dynamic now looks less like "best model wins" and more like **subsidy + workflow control + harness compatibility**.

  * **Enterprise adoption is increasingly tied to runtime/security assurances** : [Perplexity](https://x.com/perplexity_ai/status/2054608966148374715) described a hardware-isolated sandbox architecture with VPC-level separation, short-lived proxy tokens, and scanning of external content before agent actions, with [additional details](https://x.com/perplexity_ai/status/2054608978680873457) on encryption and auto-deletion. [Aravind Srinivas](https://x.com/AravSrinivas/status/2054619058650411174) framed this as foundational to Perplexity becoming an enterprise knowledge/research platform. The broader pattern: agent vendors are no longer selling only intelligence; they're selling **bounded execution environments**.




**Autonomous Science, Cyber Capability, and Robotics**

  * **Recursive self-improvement moved from idea to startup cluster** : The largest single meta-theme was the launch of [Recursive](https://x.com/_rockt/status/2054491251345391852), founded to build AI that automates science and safely improves itself. Launch posts from [Richard Socher](https://x.com/_rockt/status/2054491251345391852), [Josh Tobin](https://x.com/josh_tobin_/status/2054576051431616873), [Dominik Schmidt](https://x.com/schmidtdominik_/status/2054498117416808727), [Jenny Zhang](https://x.com/jennyzhangzt/status/2054603211798147436), and [Shengran Hu](https://x.com/shengranhu/status/2054630820305088739) suggest a team drawn from open-endedness, AI Scientist, and research automation work. In adjacent work, [Adaption's AutoScientist](https://x.com/adaption_ai/status/2054532113316434061) aims to automate the full training-research loop outside frontier labs, with [Sarah Hooker](https://x.com/sarahookr/status/2054551263275254084) arguing that most model training failures are due to research-loop brittleness rather than mere compute scarcity.

  * **Cyber capability evaluations continue to steepen** : The UK [AI Security Institute](https://x.com/AISecurityInst/status/2054589758043496567) said the length of cyber tasks frontier models can complete has been doubling every few months, and that recent models are beating prior trends. Anthropic/Glasswing's [Logan Graham](https://x.com/logangraham/status/2054613618168082935) said **Claude Mythos Preview** is the first model to solve both AISI end-to-end cyber ranges, including **Cooling Tower** , and the only one to clear every task under the institute's **2.5M-token** cap. XBOW reportedly found "token-for-token, unprecedented precision," and partner usage allegedly surfaced **thousands of high/critical vulnerabilities** in weeks. Independent commentary from [scaling01](https://x.com/scaling01/status/2054594892903436553) claimed a newer Mythos version completed a cyber range **6/10 times vs 3/10** for the preview baseline.

  * **Robotics got a concrete long-horizon deployment demo** : [Figure's Brett Adcock](https://x.com/adcock_brett/status/2054603963996278786) streamed humanoid robots running a full **8-hour autonomous shift** on package sorting using **Helix-02** , with follow-up details that the robots reason from camera pixels, operate around **human parity (~3s/package)** , perform **on-device inference** , coordinate as a networked fleet, autonomously swap for low battery, and self-diagnose/fail over to maintenance when needed [here](https://x.com/adcock_brett/status/2054615837903048807). This is one of the clearer public demonstrations of **multi-robot, long-duration, no-human-in-the-loop orchestration** rather than a short benchmark clip.




**Top tweets (by engagement)**

  * **Claude Code pricing and limits** : [@ClaudeDevs on 50% higher weekly limits](https://x.com/ClaudeDevs/status/2054639777685934564), [@ClaudeDevs on programmatic credits](https://x.com/ClaudeDevs/status/2054610152817619388), and the ensuing developer backlash from [@theo](https://x.com/theo/status/2054620998205624746) made pricing policy the day's most consequential developer story.

  * **Codex enterprise push** : [@sama offering two free months of Codex usage for switchers](https://x.com/sama/status/2054626219858293128) and [@OpenAIDevs' enterprise call-to-action](https://x.com/OpenAIDevs/status/2054586214112780518) signaled an unusually direct go-to-market counterpunch.

  * **Figure 's 8-hour humanoid shift**: [@adcock_brett's livestream post](https://x.com/adcock_brett/status/2054603963996278786) drew enormous attention and is one of the few viral posts in the set with clear technical substance.

  * **Cline SDK launch** : [@cline's SDK release](https://x.com/cline/status/2054580767779700775) was one of the highest-engagement genuinely technical launches, reflecting demand for open coding-agent harnesses.

  * **Token Superposition Training** : [@NousResearch's TST post](https://x.com/NousResearch/status/2054610062836892054) stood out as a rare pretraining-method tweet that broke through widely, likely because the claim--**2 -3× training speedup without changing inference-time architecture**--is concrete and economically important.




* * *

# **AI Reddit Recap**

## **/r/LocalLlama + /r/localLLM Recap**

### **1\. Efficient On-Device LLM Inference**

[ Read more ](https://www.latent.space/p/ainews-codex-rises-claude-meters)

---

## [[AINews] The End of Finetuning](https://www.latent.space/p/ainews-the-end-of-finetuning)
*🔬 Latent Space | 2026-05-13*

The proximal cause of today's op-ed is OpenAI's deprecation of their finetuning APIs. 

[](https://substackcdn.com/image/fetch/$s_!ioj8!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fd6915f95-7d03-4a7d-81b1-df255b9debcb_1192x1422.png)

For years, OpenAI stood out among the big labs for their finetuning support, and [many many many talks and content pieces and AI engineers](https://www.youtube.com/@OpenAI/search?query=finetuning) promoted how you can get some variant of "get o1 performance at 4o prices" and insisting that it was an important part of the toolkit. 

Now the tide is out, [Anthropic will probably raise at a higher valuation than OpenAI for the first time ever](https://www.latent.space/p/ainews-anthropic-growing-10xyear), and Finetuning is the[ next casualty of the 2026 Side Quest massacre (after Sora)](https://www.latent.space/p/ainews-apples-war-on-slop?utm_source=publication-search). If you assume an extreme GPU crunch, that makes sense, but even without dramatic compute constraints, the modal 80% of the AI Engineering industry was probably trending there anyway, with [Jeremy Howard calling it out on the pod as early as 2023](https://www.latent.space/p/fastai).

The "End" of a thing for most people does NOT mean the "End" of a thing period - and in fact the top tier, like Cursor and Cognition (whose [$25B round ](https://x.com/colossusmag/status/2053801052571312414)is now public discussion) have both INCREASED open model RLFT and usage, rather than decreased. Open Model finetunes may also be central to [the Custom ASIC Thesis](https://www.latent.space/p/ainews-the-custom-asic-thesis?utm_source=publication-search), but if Taalas' model and continued P/D Disaggregation inference solutions are any indication, then maybe Just Very Long Prompts (like [Claude's Constitution](https://x.com/AnthropicAI/status/2053881827396653207)) are all you need…

> AI News for 5/11/2026-5/12/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

# **AI Twitter Recap**

**Research Benchmarks, Hard Evals, and Agentic Science Systems**

  * **Research-level reasoning benchmarks keep getting harder** : [Soohak](https://x.com/gson_AI/status/2054036114483392997) introduces **439 research-level math problems** authored from scratch by **64 mathematicians** (including **38 faculty**), explicitly targeting capabilities above standard olympiad-style math. In medical evaluation, [@SophontAI](https://x.com/SophontAI/status/2054270239387627927) released **Medmarks v1.0** , expanding its open medical benchmark suite from **20 ->30 benchmarks** and **46 ->61 models**. There's also growing sentiment that old evals are saturating: [@polynoamial](https://x.com/polynoamial/status/2054255862441812099) argues benchmarks with uniformly high scores should be retired in favor of lower-scoring, frontier-challenging tests.

  * **Agentic systems are starting to move benchmark frontiers in science and math** : Google DeepMind's [AI Co-Mathematician](https://x.com/dair_ai/status/2054224343551639958) is described as an asynchronous, stateful research workbench for mathematicians, reportedly reaching **48% on FrontierMath Tier 4** while supporting ideation, literature discovery, computational analysis, theorem verification, and formal outputs. In theoretical physics, [physics-intern](https://x.com/dlouapre/status/2054217281895309480) boosts **Gemini 3.1 Pro from 17.7% to 31.4% on CritPt** via decomposition into specialized agents. On coding/program synthesis, [ProgramBench's first task](https://x.com/KLieret/status/2054215545663144217) was reportedly solved by **GPT-5.5 high/xhigh** , with xhigh outperforming **Opus 4.7 xhigh** across metrics.

  * **Retrieval and search benchmarks are rewarding small, specialized models** : LightOn's [Agent-ModernColBERT](https://x.com/LightOnIO/status/2054202169255973121) stacks another **~10%** over Reason-ModernColBERT on BrowseComp-Plus while keeping the retriever at **149M parameters** , with claims of matching or exceeding much larger model-based systems when paired with a generator. Related discussion from [@xuzihuan4](https://x.com/xuzihuan4/status/2054220800073642161) asks whether lexical retrieval may suffice in agentic search loops when agents can iteratively refine their own queries.




**Training, Optimization, and Scaling-Law Techniques**

  * **Optimizer work continues to compress training cost and improve small-scale experimentation** : Several tweets centered on fast variants of **SOAP/Muon-style updates**. [@torchcompiled](https://x.com/torchcompiled/status/2054036715589771542) applied tangent-step + Stiefel manifold retraction to **SOAP basis updates** , with [follow-up discussion](https://x.com/torchcompiled/status/2054088499591000255) on drift checks and QR fallback for stability. In the Modded-NanoGPT community, [SOAP-Muon](https://x.com/kellerjordan0/status/2054255672636981423) set a new record at **3150 steps (-60)** , while an earlier [MuLoCo-style outer Nesterov SGD wrap on NorMuonH](https://x.com/kellerjordan0/status/2054098451621978471) also improved results, both backed by p-value reporting.

  * **Formal methods and superoptimization are beginning to merge with ML systems work** : [@leloykun](https://x.com/leloykun/status/2054076097881592068) described a **Lean4-to-TileLang tensor program superoptimizer** that can automatically discover kernels such as **FlashAttention2** , **FlashNorm** , and **split-k matmul** , reporting roughly **1.8 × geomean speedup on A100s**. The same framework is positioned to jointly search over kernels, optimizers, hyperparameter transfer rules, and scaling laws.

  * **Scaling laws and training metrics are being re-examined** : [@che_shr_cat](https://x.com/che_shr_cat/status/2054178651856339276) argues the classic **" 20 tokens per parameter"** framing is tokenizer-dependent and that scaling should be measured in **bytes** , not tokens. Separately, [@JJitsev](https://x.com/JJitsev/status/2054166378823794881) emphasized that prescriptive scaling laws are valuable not just for prediction, but as a systematic basis for comparing learning procedures across scales.

  * **Training-time-only efficiency tricks are getting more interesting** : [Lighthouse Attention](https://x.com/omarsar0/status/2054224130103554359) from Nous is highlighted as a subquadratic **training wrapper** around vanilla attention that can be removed near the end of training after a recovery phase, preserving standard deployment-time inference while reducing long-context pretraining cost. In a similar spirit, [Renderers](https://x.com/PrimeIntellect/status/2054347134821154841) from Prime Intellect addresses the token/message impedance mismatch between RL trainers and agent environments, claiming **> 3× throughput** on popular open models.




**Inference Systems, Serving Stacks, and Runtime Infrastructure**

  * **Blackwell racks are emerging as the reference platform for large-MoE serving** : Perplexity published details on serving post-trained **Qwen3 235B** on **NVIDIA GB200 NVL72** systems, arguing GB200 is a major inference step up over Hopper for large MoEs. Their [benchmarks](https://x.com/perplexity_ai/status/2054204425833726353) cite **NVLS all-reduce latency** dropping from **586.1 µs on H200 to 313.3µs on GB200**, and **MoE prefill combine** at EP=4 dropping from **730.1 µs to 438.5µs**, with better decode throughput at high token rates. [@AravSrinivas](https://x.com/AravSrinivas/status/2054206802133504234) framed this as materially changing prefill/decode disaggregation for serving large MoEs.

  * **Inference orchestration is increasingly specialized, not "just Kubernetes"**: [Modal](https://x.com/charles_irl/status/2054233051140690023) argues inference needs a dedicated stack, citing work on compute management, cloud-native caching, **CRIU** , and **GPU checkpointing**. That positioning got an immediate real-world endorsement from Perceptron, which said [all Mk1 inference runs on Modal](https://x.com/AkshatS07/status/2054275262289002664) because native video, structured outputs, and hybrid reasoning create unusual cold-start and scaling requirements.

  * **OSS inference economics continue to improve fast** : [SemiAnalysis](https://x.com/SemiAnalysis_/status/2054245527957508520) reported that clustering multiple **B200 8-GPU** machines over **RoCEv2 CX-7** with **PD disaggregation** can lift **per-GPU token throughput by up to 7 ×**, implying comparable cost-per-token reductions. On the vector DB side, [Qdrant 1.18](https://x.com/qdrant_engine/status/2054166055417938266) added **TurboQuant** , claiming recall near scalar quantization with **2 × less memory**, alongside memory monitoring and named-vector lifecycle operations.

  * **Agent runtimes are becoming version-control-like substrates** : A standout systems idea was Stanford's **Shepherd** , summarized by [@ai_satoru_chan](https://x.com/ai_satoru_chan/status/2054126183374348296), which treats agent execution more like **Git** : first-class tasks, effects, scopes, and traces; exact replay; branching; rollback; and formal guarantees in **Lean**. Claimed results include live-supervision gains on CooperBench from **28.8% ->54.7%**, plus faster counterfactual optimization and tree-RL rollouts.




**Product and Model Releases: Multimodal, Video, Retrieval, and Embeddings**

  * **Perceptron Mk1 was the most substantive new model release in the set** : [@perceptroninc](https://x.com/perceptroninc/status/2054216828285796630) launched **Perceptron Mk1** as a model for **frontier video and embodied reasoning** , with native video support at **up to 2 FPS** , temporal grounding, multimodal in-context learning, and structured spatial outputs. [OpenRouter's summary](https://x.com/OpenRouter/status/2054232344148787462) notes a **32k multimodal context** and first-class outputs like points, boxes, polygons, and clips. The release is framed less as a generic VLM and more as a physical-world reasoning stack.

  * **Google and Meta both pushed multimodal interaction layers rather than standalone model specs** : Google DeepMind's [AI-enabled mouse pointer demos](https://x.com/GoogleDeepMind/status/2054246119635300451) reimagine the cursor as a contextual pointing interface tied to Gemini, allowing users to point at on-screen content and speak shorthand instructions. In parallel, Meta announced [Meta AI voice conversations powered by Muse Spark](https://x.com/MetaNewsroom/status/2054205287515484397), adding interruption, language switching, image generation, and live camera-grounded interaction.

  * **Embedding and retrieval model updates were notable** : Jina released [jina-embeddings-v5-omni](https://x.com/JinaAI_/status/2054226262047301933), a universal embedding model for **text, images, audio, and video** , in **1.57B** and **0.95B** variants, both with Matryoshka truncation and backward compatibility with existing v5-text indexes. Meta quietly released [Sapiens2](https://x.com/mervenoyann/status/2054187884417102319), a family of human-centric high-resolution ViTs spanning **0.1B ->5B** params for pose estimation, segmentation, normals, and pointmaps.

  * **Diffusion and image tooling kept moving** : Hugging Face's [Diffusers 0.38.0](https://x.com/RisingSayak/status/2054110949469196748) added new pipelines including **Ace-Step 1.5** , **LongCat-AudioDiT** , and **Ernie-Image** , plus support for **Flash Attention 4** , **FlashPack loading** , and **Ring Anything** for context parallelism. Other research releases included [ELF: Embedded Language Flows](https://x.com/iScienceLuvr/status/2054118255778763184), a continuous-space text diffusion model, and Tencent's [Pixal3D](https://x.com/_akhaliq/status/2054120807425511826) for pixel-aligned 3D generation.




**Agents, Tooling, and Developer Workflow**

  * **Agent products are shifting from demos to operational platforms** : OpenAI teased [Symphony](https://x.com/OpenAIDevs/status/2054252221941121035) as a system where **every open task gets a running Codex agent** , and separately highlighted [computer use for Codex](https://x.com/OpenAIDevs/status/2054298427245441141) to work across apps without full takeover. LangChain re-open-sourced [its revamped Chat LangChain app](https://x.com/BraceSproul/status/2054231134163321287), describing it as a production Q&A agent handling nearly **2T tokens/week**.

  * **Long-running-agent state management is becoming a first-class systems problem** : LangGraph's new [DeltaChannel snapshots](https://x.com/sydneyrunkle/status/2054278551244099706) aim to replace full-state checkpointing for scalable durable execution; LangChain says the same mechanism now powers message histories and file storage in **deepagents v0.6**. The broader pattern also shows up in Google's [Gemini Interactions API guide](https://x.com/_philschmid/status/2054225343251206528), where encrypted `thought` signatures preserve reasoning context across turns in both stateful and stateless modes without forcing developers to manage signature injection manually.

  * **Synthetic data and RL environment generation are being operationalized** : [@Vtrivedy10](https://x.com/Vtrivedy10/status/2054054238226170361) offered a useful practitioner perspective: targeted synthetic data extraction from model weights is hard at scale, especially for underrepresented distributions like long sequences, and effective pipelines need programmatic tests, verifiers, judges, and agentic long-horizon framing. On the infrastructure side, [Tau2-Infinity](https://x.com/Shahules786/status/2054241505506648161) formalizes autonomous mining of hard tool-use tasks for RL post-training via DAG walks or world-generation from failure hypotheses.

  * **Top tweets (by engagement, filtered for technical relevance)** :

    * **Gemini as an OS-level intelligence layer** : Google's [Gemini Intelligence](https://x.com/sundarpichai/status/2054255858700415005), [Googlebook](https://x.com/Google/status/2054270454467121187), and [AI pointer demos](https://x.com/GoogleDeepMind/status/2054246119635300451) collectively point to agentic UX moving from chat windows into the operating system.

    * **Isomorphic Labs funding** : [@demishassabis](https://x.com/demishassabis/status/2054197462101889277) announced **$2.1B** in new funding for AI-driven drug discovery, one of the largest capital commitments in this dataset tied directly to an applied AI platform.

    * **Speech-to-speech benchmarking** : Artificial Analysis' [τ-Voice benchmark](https://x.com/ArtificialAnlys/status/2054234919887573292) found even the best S2S models solve only about **half of realistic customer service scenarios** , with **Grok Voice Think Fast 1.0** leading at **52.1%**.

    * **Claude Opus 4.7 fast mode** : Anthropic's [fast mode release](https://x.com/ClaudeDevs/status/2054266327771275435) reached APIs and Claude Code, with Cursor noting [2.5× speed at 6× cost](https://x.com/cursor_ai/status/2054274305345618163), a concrete new point on the latency/price frontier.




**Security, Supply Chain, and Safer Coding**

  * **The most urgent operational story was the Mini Shai-Hulud supply-chain attack** : [@IntCyberDigest](https://x.com/IntCyberDigest/status/2054166749998661659) reported the campaign had expanded beyond TanStack to hit **OpenSearch, Mistral AI, Guardrails AI, UiPath, and others** across npm and PyPI, specifically targeting **AI developer tooling**. The noteworthy technical detail is persistence: it allegedly hooks into **Claude Code** (`.claude/settings.json`) and **VS Code** (`.vscode/tasks.json`) so the compromise can re-execute on future tool events even after package removal. [Guardrails AI](https://x.com/guardrails_ai/status/2054341322304299086) later confirmed its **0.10.1** package was compromised and quarantined within about **2 hours**.

  * **Actionable mitigations surfaced quickly** : [@ramimacisabird](https://x.com/ramimacisabird/status/2054178771180093858) noted that beyond `minimumReleaseAge`, teams should enable `blockExoticSubdeps` to prevent remote GitHub references from slipping into dependency graphs. [@elithrar](https://x.com/elithrar/status/2054162732195197283) reiterated that GitHub's `pull_request_target` remains one of the sharpest CI/CD footguns for fork-based PR automation. And at the workstation level, [@andersonbcdefg](https://x.com/andersonbcdefg/status/2054212574162653535) recommended moving secrets out of ubiquitous local `.env` files into a proper secrets manager.

  * **Safer codegen is becoming its own research track** : Stanford-aligned work on [SecureForge](https://x.com/houjun_liu/status/2054233718269595869) targets vulnerability discovery/prevention in LLM-generated code via prompt optimization, while [the corresponding paper listing](https://x.com/FSFG/status/2054196048621367422) frames it as a bridge between codegen and security evaluation. The broader point: coding agents are now strong enough that supply-chain hardening and secure-generation evaluation need to be treated as core infra, not side concerns.




* * *

# **AI Reddit Recap**

## **/r/LocalLlama + /r/localLLM Recap**

### **1\. Qwen 3.6 MTP and Long-Context Local Evals**

  * **[MTP on Unsloth](https://www.reddit.com/r/LocalLLaMA/comments/1ta4rvs/mtp_on_unsloth/)** (Activity: 727): **The[image](https://i.redd.it/7qopol51pi0h1.png) is a Hugging Face activity screenshot showing Unsloth AI publishing/updating MTP-preserved GGUF builds: **`unsloth/Qwen3.6-27B-GGUF-MTP`**and**`unsloth/Qwen3.6-35B-A3B-GGUF-MTP`**. The technical significance is that these GGUFs retain the MTP / next-token-prediction auxiliary layer, but users reportedly still need to checkout and build a specific llama.cpp MTP PR rather than relying on default llama.cpp support. One commenter hit a runtime/model-load assertion,**`GGML_ASSERT(hparams.nextn_predict_layers > 0 && "QWEN35_MTP requires nextn_predict_layers > 0")`**, suggesting tooling or metadata support is still fragile for these MTP GGUFs.** Commenters are mainly waiting on upstream inference support, with one joking about constantly refreshing `llama.cpp` and `vLLM` GitHub repos. There is also uncertainty over whether MTP is supported "out of the box" in llama.cpp; the post indicates it is not yet.

    * A user compiling/running the new `27B` GGUF model reports a hard assertion failure in `qwen35_mtp.cpp`: `GGML_ASSERT(hparams.nextn_predict_layers > 0 && "QWEN35_MTP requires nextn_predict_layers > 0") failed`. This suggests the GGUF/model metadata being loaded is missing or not exposing `nextn_predict_layers`, which is required for **Qwen3.5 MTP** execution in the current implementation.

    * Several commenters are tracking whether **llama.cpp** and **vLLM** have landed native **MTP** support, with one explicitly asking whether llama.cpp now supports MTP "out of the box." The thread implies support is still in flux across backends and that users are watching upstream repositories for compatibility with GGUF MTP models.

    * One technical takeaway is that **MTP support in GGUF** is viewed as important for local inference, especially for Qwen-style variants such as the mentioned `35B A3B` model. A commenter highlights the `35B A3B` variant as interesting specifically because of expected context-length improvements.

  * **[The Qwen 3.6 35B A3B hype is real!!!](https://www.reddit.com/r/LocalLLaMA/comments/1t9whrt/the_qwen_36_35b_a3b_hype_is_real/)** (Activity: 713): **A user benchmarked Qwen 3.6 35B A3B, Qwen 3.6 27B, Gemma 4 26B A4B, and Nemotron 3 Nano on a niche paper-to-code comprehension task, feeding each model an academic paper plus accompanying research code via long-context mechanisms such as gated delta nets, hybrid Mamba2, and sliding-window attention. In their[detailed findings](https://github.com/nathanlgabriel/paper_code_mapping_assessment/blob/main/README.md), all four small/local open-weight models substantially outperformed prior small-model baselines such as [Devstral Small 2](https://www.reddit.com/r/LocalLLaMA/comments/1ry93gz/devstral_small_2_24b_severely_underrated/), with Qwen 3.6 35B A3B judged strongest; Devstral Small 2 could not fit the long-context workload in **`32GB`**VRAM/RAM.** Commenters noted practical tradeoffs: **Qwen 35B** is preferred for long-context/refactoring but can be verbose/slow in thinking mode, while **Gemma 26B** is faster for code fixes/chats; at `q4`, one user reports ~`20GB` for Qwen 35B and ~`15GB` for Gemma 26B, allowing both to stay loaded. Another commenter criticized the evaluation for not documenting inference settings, which limits reproducibility.

    * Several users compared local workflows using **Gemma 26B** and **Qwen 35B** , noting that both can be kept resident simultaneously at `q4` quantization because Qwen 35B is about `20 GB` and Gemma 26B about `15 GB`. One commenter uses Gemma 26B thinking mode for quick code fixes/chat and Qwen 35B thinking mode for longer-context refactoring, but reports Qwen 35B has high latency due to excessive reasoning verbosity before final output.

    * A coding-focused report claimed **Qwen 27B** can handle large projects (`100k+` LOC) effectively when bootstrapped by a stronger model/coding agent for initial project setup, then switched to Qwen for continued work. The user found little practical difference between Qwen 27B and **DeepSeek V4** for their use case, though Qwen occasionally entered loops requiring manual interruption and continuation prompting.

    * One commenter emphasized that **Qwen 27B/35B performance is sensitive to inference configuration** , specifically temperature/sampling parameters and avoiding overly aggressive quantization of either the model weights or KV cache. Another asked for the missing run settings, implying the original claims are hard to evaluate without details like quantization level, sampler settings, context length, backend, or hardware.




### **2\. Memory-Tiered and Power-Efficient Local Inference**

  * **[Computer build using Intel Optane Persistent Memory - Can run 1 trillion parameter model at over 4 tokens/sec](https://www.reddit.com/r/LocalLLaMA/comments/1taeg8h/computer_build_using_intel_optane_persistent/)** (Activity: 964): **The image shows the internals of a high-memory Xeon workstation/server build using Intel Optane DC Persistent Memory DIMMs, matching the post 's claim of running Kimi K2.5, a ~**`1T`**parameter MoE model, locally at about**`4 tokens/s`**via llama.cpp hybrid GPU/CPU inference. The key technical point is the use of**`768GB`**Optane PMem in Memory Mode, where Optane appears as system RAM and**`192GB`**DDR4 ECC DRAM acts as cache, allowing the model 's sparse expert weights to reside in PMem while attention/dense/shared expert/routing tensors fit on an RTX 3060 12GB using **`override-tensor`**or**`ngl auto`**/**`cmoe`**.[Image](https://i.redd.it/na7zo7lmck0h1.jpeg)** Commenters noted that a higher-core-count Cascade Lake Xeon, such as an ES 8260/QQ89, could improve throughput, and debated whether Optane **Storage Mode** plus `mmap` might outperform Memory Mode. Others found the build impressive but questioned whether `4 tokens/s` is practically tolerable for interactive use.

    * A detailed hardware note suggests performance may improve with a higher-core-count Cascade Lake Xeon, e.g. **QQ89 ES / Xeon Gold 8260-class**`24-core`, versus the current **Xeon Gold 6246**`12-core`. The commenter also proposes benchmarking Optane PMem in **storage mode +**`mmap` versus **memory mode** , noting that memory mode uses DRAM as a transparent cache and requires pages to be swapped back into DRAM before CPU execution, so it is not equivalent to normal RAM latency.

    * One commenter provides a concise Optane PMem platform compatibility breakdown: **LGA3647 Skylake/Cascade Lake uses 1st-gen Optane**`NMA`**at**`2666 MT/s`, while **LGA4189 uses 2nd-gen**`NMB`, running at `2666` on Cooper Lake and `3200` on Ice Lake. They also note that mixing Optane with DRAM on Cascade Lake can downclock affected channels to `2666`, and that many Xeons from this era have a `1 TB`**total memory limit across DRAM + Optane** , unless using high-memory SKUs or later platforms.

    * A technical caveat is raised that while `~4 tokens/sec` generation on a trillion-parameter model may be tolerable for some uses, **prompt processing/prefill speed is likely to be much worse** on this kind of memory hierarchy. Another comment estimates the full used-market build cost at roughly `$2060-$2500`, including a **Xeon Gold 6246** , **TYAN S5630GMRE-CGN** , **RTX 3060 12GB** , `192 GB` DDR4 ECC RDIMM, and `768 GB` Intel Optane DCPMM.

  * **[Stop wasting electricity](https://www.reddit.com/r/LocalLLaMA/comments/1tayu5t/stop_wasting_electricity/)** (Activity: 905): **A user benchmarked**`llama.cpp`****`llama-server`**on an RTX 4090 with**`Qwen3.6-27B-UD-Q4_K_XL.gguf`**, full GPU offload (**`-ngl all`**), FlashAttention enabled,**`q4_0`**K/V cache quantization,**`32`**threads, and a**`262144`**context, varying the GPU power cap via**`sudo nvidia-smi -pl N`**. They report the GPU was consistently power-limited and that reducing the power limit can substantially lower power/heat/noise with little to no decode / token-generation (**`tg`**) throughput loss; a commenter notes prefill (**`pp`**) is more sensitive, with roughly**`15-20%`**performance loss when dropping from**`450W`**to**`270W`**, model-dependent.** Commenters were mainly interested in separating **decode vs prefill** behavior, since decode appears power-insensitive while prefill degrades more noticeably. One RTX 5090 user said they already cap power for hardware-safety concerns and may reduce it further based on these results.

    * Users focused on the performance impact of GPU power limiting: **decode/token generation (**`tg`**) reportedly is not the bottleneck** , while **prefill (**`pp`**) takes a larger hit**. One commenter quantified the tradeoff as only about `15-20%`**prefill performance loss** when reducing power from `450W`**to**`270W`, depending on the model, suggesting substantial efficiency gains from aggressive power caps.




### **3\. Ultra-Small On-Device Transformer Experiments**

  * **[I got a real transformer language model running locally on a stock Game Boy Color!](https://www.reddit.com/r/LocalLLaMA/comments/1tbi2n3/i_got_a_real_transformer_language_model_running/)** (Activity: 368): **The image ([jpeg](https://i.redd.it/1hl9id7ghs0h1.jpeg)) shows a stock Game Boy Color running a local TinyStories transformer demo, with the screen displaying **`TINYSTORIES Q8 GBC`**and**`Prompt tokenized`**. Per the post, this is Andrej Karpathy 's TinyStories-260K converted to **`INT8`**/fixed-point math in a GBDK-2020 MBC5 ROM, with weights in bank-switched cartridge ROM and the KV cache stored in cartridge SRAM due to the GBC 's tiny work RAM. The author notes it is **_**extremely slow**_**and produces mostly gibberish because of aggressive quantization/approximations, but the core local transformer prefill + autoregressive generation loop works on-device with no PC, phone, Wi-Fi, link cable, or cloud inference:[github.com/maddiedreese/gbc-transformer](https://github.com/maddiedreese/gbc-transformer).** Comments are mostly enthusiastic praise; one commenter said it made them want to run a model on an **N64** , and another linked a related/joke Game Boy language-model project, [gbalm](https://code.heni.lol/heni/gbalm).

    * A commenter linked a prior Game Boy language-model project, **gbalm** ([code](https://code.heni.lol/heni/gbalm)), indicating there has been earlier experimentation with extremely constrained on-device LM inference on Nintendo handheld hardware. This is relevant as a comparison point for implementation approaches and feasibility on non-GPU, retro 8-bit-class systems.

    * One technical question centered on why CUDA/ROCm-style GPU stacks are not required here: the commenter notes that typical LLM inference is associated with mature GPU compilers, yet this demo runs on hardware comparable to _" a potato."_ The implicit point is that sufficiently tiny transformer models can be executed with hand-written or highly simplified CPU-style inference loops, though at very low throughput, and that portability to unsupported accelerators such as future Chinese GPUs would depend more on having a basic compute backend than full CUDA compatibility.

  * **[Needle: We Distilled Gemini Tool Calling Into a 26M Model](https://www.reddit.com/r/LocalLLaMA/comments/1tb9b0r/needle_we_distilled_gemini_tool_calling_into_a/)** (Activity: 271): **Cactus Compute released Needle, an MIT-licensed**`26M`**parameter single-shot tool-calling model distilled from Gemini-synthesized data, claiming**`6000 tok/s`**prefill and**`1200 tok/s`**decode on consumer devices; weights are on[Hugging Face](https://huggingface.co/Cactus-Compute/needle) and code/docs are on [GitHub](https://github.com/cactus-compute/needle). Architecturally it uses "Simple Attention Networks" -- attention plus gating with no MLP/FFN layers -- arguing that function calling is mostly retrieval/assembly over provided tool schemas rather than memorized reasoning; training used **`200B`**pretraining tokens on**`16 TPU v6e`**for**`27h`**plus**`2B`**synthesized function-calling tokens in**`45m`**([architecture writeup](https://github.com/cactus-compute/needle/blob/main/docs/simple_attention_networks.md)). The authors claim it beats FunctionGemma-270M, Qwen-0.6B, Granite-350M, and LFM2.5-350M on single-shot function calling, while acknowledging those larger models have broader conversational capacity.** Commenters framed the model as potentially useful as a lightweight router that dispatches queries/tools or escalates to a larger LLM, with one asking whether the same architecture could support high-quality summarization. A technical concern was raised about uploaded `pickle` files due to Python-specific dependency and deserialization security risks.

    * A commenter framed the `26M` distilled tool-calling model as a lightweight **router/gating model** : it could decide whether a query should be sent to a larger LLM and with which parameters, effectively reducing expensive model calls to cases where they are needed. They also speculated whether the same architecture could generalize to constrained summarization workflows, though no benchmark evidence was provided in the thread.

    * One technical thread focused on the authors' claimed **" no FFN"** result: for tasks with external structured knowledge such as **RAG, tool use, and retrieval-augmented generation** , the model may not need feed-forward layers to store factual knowledge if relevant facts are already present in context. A commenter extrapolated this into a pipeline where a small post-trained model routes requests to RAG and then uses retrieved context to generate a natural-language answer.

    * Several implementation/security concerns were raised: one commenter noted that publishing **pickle files** is increasingly avoided because of Python-specific dependency issues and arbitrary-code-execution risk during deserialization. Another pointed out that **Gemini** has had visible tool-calling quirks, including system-prompt-like reasoning about avoiding `cat` and preferring tools such as `grep_search`, raising the possibility that a distilled dataset could inherit provider-specific tool-use biases if not cleaned carefully.




## **Less Technical AI Subreddit Recap**

> /r/Singularity, /r/Oobabooga, /r/MachineLearning, /r/OpenAI, /r/ClaudeAI, /r/StableDiffusion, /r/ChatGPT, /r/ChatGPTCoding, /r/aivideo, /r/aivideo

### **1\. Claude Coding Workflows and Tooling**

[ Read more ](https://www.latent.space/p/ainews-the-end-of-finetuning)

---

## [[AINews] Thinking Machines' Native Interaction Models - TML-Interaction-Small 276B-A12B - advances SOTA Realtime Voice a…](https://www.latent.space/p/ainews-thinking-machines-native-interaction)
*🔬 Latent Space | 2026-05-12*

By complete coincidence, the day we [released](https://x.com/neilzegh/status/2053945753073074484?s=20) Neil Zeghidour (CEO of Gradium, the for profit spinoff of the vaunted [Kyutai Moshi](https://kyutai.org/))'s [talk](https://www.youtube.com/watch?v=P_RI1kCkRbo&time_continue=0&source_ve_path=MjM4NTE&embeds_referring_euri=https%3A%2F%2Fx.com%2F) on what remains to be built for realtime voice, **Thinking Machines** emerged for only the [third](https://news.smol.ai/issues/25-10-01-thinky) [time](https://news.smol.ai/issues/25-02-18-ainews-xai-grok-3-and-mira-muratis-thinking-machines) in a ~year (despite much drama) to drop [Interaction Models: A Scalable Approach to Human-AI Collaboration](https://thinkingmachines.ai/blog/interaction-models/), **TML-Interaction-Small** is a 276B parameter MoE with 12B active., which immediately advances the state of the art of realtime voice models as Neil had laid out, updating [the famously dead GPT 4o "her" demo](https://openai.com/index/hello-gpt-4o/) with far more detailed demos that are presumably far closer to real use:

The [full blogpost](https://thinkingmachines.ai/blog/interaction-models/) has lots of demos of the level of continuous interactivity, focusing on streams of "time-aligned microturns" of 200ms each:

[](https://substackcdn.com/image/fetch/$s_!LR03!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F02190942-3f50-4067-ae03-97c6b504b3a3_1490x1592.png)

Using encoder-free early fusion, with images and audio all processed <200ms, similar to Meta's [Chameleon](https://arxiv.org/abs/2405.09818):

[](https://substackcdn.com/image/fetch/$s_!S2rk!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F68576e99-b00a-4069-b93f-bbe906ddd810_1336x1602.png)

There are a number of official benchmarks that the team shows beating both [GPT-Realtime-2](https://www.latent.space/p/ainews-gpt-realtime-2-translate-and) and [Gemini 3.1-Flash](https://www.latent.space/p/ainews-nano-banana-2-aka-gemini-31) on basic things like BigBench Audio and IFEval and FD-bench, but the level of interactivity aimed for required making 2 new internal benchmarks for time awareness, simultaneous translation, and visual proactivity:

  * **TimeSpeak:** Can the model **initiate speech** at user-specified times? 

    * Example: "I want to practice my breathing, remind me to breathe in and out every 4 seconds until I ask you to stop."

  * **CueSpeak:** Can the model speak at the **appropriate moment?**

    * Example: "Everytime I codeswitch and use another language, give me the correct word in the original language."

  * **[RepCount-A](https://arxiv.org/abs/2204.01018)** contains videos of repeated actions and is adapted into an online counting task - measures **continuous visual tracking and timely counting**.

  * **[ProactiveVideoQA](https://arxiv.org/abs/2507.09313)** consists of videos with questions, whose answers become available at specific moments. Higher scores require correct answers at the correct times, silence gets partial credit, and incorrect answers are penalized.

  * **[Charades](https://arxiv.org/abs/1604.01753)** is a standard temporal action-localization benchmark. 

    * Stream a user audio instruction: "Say 'start' when the person starts doing {action} then say 'Stop' when they stop."




But look past the numbers: the single most visceral demo is this one buried at the bottom. Play the samples and feel the AGI:

[](https://substackcdn.com/image/fetch/$s_!V7pE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F0bfcadcb-b746-4873-aed4-6095f19f5897_1478x1676.png)

The closing notes leave tantalizing hints to Thinky's roadmap, including an intriguing pairing of background agents with interactive models, which we like a whole lot.

[](https://substackcdn.com/image/fetch/$s_!PeGT!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fef289b1c-4613-4835-98e6-475906d494da_1394x588.png)

> AI News for 5/9/2026-5/11/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

# **AI Twitter Recap**

**Thinking Machines ' Native Interaction Models and the Shift Beyond Turn-Based AI**

  * **Full-duplex multimodal interaction as a first-class model capability** : The day's clearest technical theme was [Thinking Machines' preview of "interaction models"](https://x.com/miramurati/status/2053939069890298321), described as models trained **from scratch** for real-time interaction rather than layering speech, turn-taking, and tool use onto a turn-based LLM. The accompanying [technical post](https://x.com/thinkymachines/status/2053938892152435174) and team commentary from [@johnschulman2](https://x.com/johnschulman2/status/2053940452789981426), [@soumithchintala](https://x.com/soumithchintala/status/2053940215505645938), and [@cHHillee](https://x.com/cHHillee/status/2053940218747842619) frame this as a **human ↔AI bandwidth** problem: models should be able to listen, speak, watch, think, search, and react concurrently. Demos emphasized continuous-time awareness, interruption handling, simultaneous speech, visual proactivity, and background tool use without explicit "now I'm thinking / now I'm searching" boundaries. Team members also highlighted that many tasks that previously needed special-purpose systems become zero-shot once the type signature is effectively continuous **audio+video+text -> audio+text** ([@johnschulman2](https://x.com/johnschulman2/status/2053940940885332028)).

  * **Why it matters technically** : Several reactions converged on the same point: this is not "another chatbot demo" but a change in interface assumptions. [@liliyu_lili](https://x.com/liliyu_lili/status/2053942465477197891) pointed to **visual proactivity** ("tell me when I start slouching", "count my pushups") as a missing primitive in current systems; [@rown](https://x.com/rown/status/2053950123139575863) called it the first general **video+speech** model that is visually proactive; [@kimmonismus](https://x.com/kimmonismus/status/2053952846064767384) and [@giffmana](https://x.com/giffmana/status/2053953584300003405) both emphasized that native interactivity is the deeper innovation than raw benchmark claims. This launch also implicitly raises the bar for "realtime" multimodal systems, as noted by [@swyx](https://x.com/swyx/status/2053960011748098462). One implementation detail surfaced via [@eliebakouch](https://x.com/eliebakouch/status/2053982248253190180): the stack is using **SGLang**.




**OpenAI 's Enterprise and Security Push: Deployment Company and Daybreak**

  * **OpenAI is moving down-stack into services and deployment** : OpenAI announced the [OpenAI Deployment Company](https://x.com/OpenAI/status/2053824997777457651), a majority-owned unit built to help enterprises deploy frontier models into real workflows. The key operating detail is **150 Forward Deployed Engineers and Deployment Specialists** coming in via the acquisition of [Tomoro](https://x.com/OpenAI/status/2053824999736410415), with [@gdb](https://x.com/gdb/status/2053884619695730745) citing **$4B of initial investment from 19 partners**. Multiple observers read this as OpenAI adopting a Palantir-/Microsoft-style field-engineering model: [@kimmonismus](https://x.com/kimmonismus/status/2053844403488194827) argued OpenAI wants to own the **deployment layer** of the AI economy, while [@matvelloso](https://x.com/matvelloso/status/2053881988529139765) connected it to the historical enterprise success pattern of embedding technical staff close to customer operations.

  * **Daybreak: security-specific model distribution, workflow, and trust tiers** : OpenAI also launched [Daybreak](https://x.com/OpenAI/status/2053939702110269822), an umbrella effort around defensive cyber operations and continuously securing software, with [@sama](https://x.com/sama/status/2053951874408276193) positioning it as a practical response to rapidly improving AI cyber capability. The product pitch, summarized by [@TheRundownAI](https://x.com/TheRundownAI/status/2053945340592631843), combines **GPT-5.5** , **Codex** , repository threat modeling, vuln discovery, patch generation, and response automation, with differentiated access tiers including **Trusted Access for Cyber** and a more specialized **GPT-5.5-Cyber**. This stands in contrast to Anthropic's more restrictive cyber posture, a tension captured by [@kimmonismus](https://x.com/kimmonismus/status/2053941490490265661). For teams building secure agent systems, a separate warning from [@lukOlejnik](https://x.com/lukOlejnik/status/2053758553723211988) is relevant: **" Your LLM is not a security boundary"**--Microsoft Semantic Kernel reportedly allowed prompt injection to be turned into host-level RCE because the framework over-trusted model output rather than the model itself failing.




**Agent Harnesses, Local-First Tooling, and Control Surfaces**

  * **Better agent control planes are becoming a product category** : A recurring complaint is that useful agents need autonomy, but engineers still want reversible, inspectable control. [@itsclelia](https://x.com/itsclelia/status/2053716807748567329) addressed this with **aggit** , a Rust CLI for local/remote, S3-backed storage of agent artifacts, enabling stash/branch/restore semantics outside the main Git history. In the same vein, [@_catwu](https://x.com/_catwu/status/2053999857799672111) highlighted a new `claude agents` terminal control plane for managing multiple Claude Code agents, and [@cursor_ai](https://x.com/cursor_ai/status/2053939390410612988) pushed Cursor into **Microsoft Teams** , where the agent reads the full thread and opens a PR. These are all signs that "agent orchestration" is converging on concrete UX patterns rather than prompt tricks alone.

  * **Deep Agents / Hermes / local agents are maturing quickly** : [@masondrxy](https://x.com/masondrxy/status/2053717333433340034) noted that **Deep Agents CLI** can hot-swap underlying model providers **mid-conversation without losing context** , a nontrivial systems capability that many agent stacks still miss. LangChain also highlighted **harness profiles** for provider/model-specific tuning ([tweet](https://x.com/masondrxy/status/2053882188870074848)), and separate pricing analysis from the same author argued that **DeepSeek V4 Flash** can be dramatically cheaper than GPT/Gemini flash-tier options for high-volume agent workloads ([tweet](https://x.com/masondrxy/status/2053855842076942555)). On the local side, Hugging Face added [Hermes Agent support in local apps plus native trace visualization](https://x.com/mervenoyann/status/2053857347429151163), while [@Teknium](https://x.com/Teknium/status/2053961675985113404) previewed **computer use with any model** via Hermes Agent and CUA, explicitly targeting local/open models as well as frontier APIs. [@onusoz](https://x.com/onusoz/status/2053812410730037256) joining Hugging Face to improve local models in **OpenClaw** and related open harnesses is another strong signal that local agent ergonomics are now strategic infrastructure.

  * **A design thesis emerging around tools** : [@threepointone](https://x.com/threepointone/status/2053751241977594102) argued that agents may asymptotically want just **two primitive tools: search and execute** , with dynamic semantic discovery of capabilities rather than ever-expanding static tool menus. That complements the broader move toward configurable harnesses instead of giant monolithic prompts.




**Benchmarks, Efficiency, and Open-Model Economics**

  * **Coding-agent benchmarking is finally measuring harness+model pairs** : [Artificial Analysis launched a Coding Agent Index](https://x.com/ArtificialAnlys/status/2053865095076438427) spanning SWE-Bench-Pro-Hard-AA, Terminal-Bench v2, and SWE-Atlas-QnA, comparing not just models but **model+harness combinations**. Their topline: **Opus 4.7** in Cursor CLI scored **61** , with **GPT-5.5** in Codex/Claude Code close behind; top open-weight setups included **GLM-5.1** , **Kimi K2.6** , and **DeepSeek V4 Pro** in Claude Code, still competitive but meaningfully behind. The benchmark also exposed large variation in **cost per task** (>30x), **token usage** (>3x), **cache hit rates** (80-96%), and **time per task** (>7x). That benchmark was complemented by OpenHands' updated software-engineering benchmark announcement ([tweet](https://x.com/OpenHandsDev/status/2053839810343620980)) and Claw-Eval's more agentic task mix across office, finance, terminal, and web tasks, where [MiMo-V2.5-Pro led and DeepSeek V4 Flash looked unusually efficient for its size](https://x.com/nathanhabib1011/status/2053786853929824385).

  * **TurboQuant skepticism is increasing** : Multiple posts pointed to a more sober view of the recently popular quantization/serving technique. [@_EldarKurtic](https://x.com/_EldarKurtic/status/2053809592061030546) presented what he described as the first comprehensive study of **TurboQuant** , covering accuracy, latency, and throughput; [@vllm_project](https://x.com/vllm_project/status/2053852636093239555) linked the Red Hat / vLLM investigation as a starting point; and [@jbhuang0604](https://x.com/jbhuang0604/status/2053882357833208262) bluntly summarized the takeaway as "it doesn't really work well." This is exactly the sort of infra claim where independent reproduction matters.

  * **Local/open models continue to improve faster than hardware ceilings** : [@ClementDelangue](https://x.com/ClementDelangue/status/2053825719587815711) made the strongest high-level argument here: on the same top-end MacBook Pro memory ceiling, the "smartest open-weight model you can actually run" improved from Llama 3 70B-era capability to **DeepSeek V4 Flash mixed-Q2 GGUF** -era capability at roughly **4.7x in 24 months** , implying a doubling every **10.7 months** , faster than Moore's Law. Supporting datapoints came from [@victormustar](https://x.com/victormustar/status/2053780086596288781) on the rapid growth of GGUF uploads and from repeated community observations that **Qwen 3.6** , **Gemma 4** , and DeepSeek variants are now usable locally for nontrivial agent tasks.




**Research Highlights: MoE Modularity, Diffusion/Byte Models, and Agent Dynamics**

  * **Architectures and evaluation** : AllenAI's **EMO** was highlighted by [@TheTuringPost](https://x.com/TheTuringPost/status/2053795343658303860) as a more modular Mixture-of-Experts design where document-level routing induces shared expert pools; notably, keeping only **25% of experts** reportedly costs just **~1%** performance versus **10 -15%** degradation in standard MoEs under similar pruning ([follow-up](https://x.com/TheTuringPost/status/2053795410490339720)). On generative evaluation, [@qberthet](https://x.com/qberthet/status/2053795951228371311) introduced **MIND (Monge Inception Distance)** as a purportedly faster, more sample-efficient replacement for FID.

  * **Diffusion for language and byte-level modeling** : Several papers pushed non-AR language modeling. [@LucaAmb](https://x.com/LucaAmb/status/2053867347023466850) reported continuous bitstream diffusion nearly matching autoregressive models under their evaluation setup; [@JulieKallini](https://x.com/JulieKallini/status/2053853543552217478) introduced **Fast BLT** , using diffusion for parallel byte decoding to make byte-level LMs less inference-bound; [@sriniiyer88](https://x.com/sriniiyer88/status/2053882384211419375) framed it as combining block byte-diffusion with self-speculative decoding. Relatedly, [@LiangZheng_06](https://x.com/LiangZheng_06/status/2053806963839168619) noted a useful property of diffusion models for post-training: because sampling is differentiable, reward gradients can in principle flow straight to parameters more directly than in standard LLM setups.

  * **Agent behavior under long horizons** : Two strong empirical threads surfaced. First, ["The Memory Curse"](https://x.com/omarsar0/status/2053863994499408214) claims long histories degrade cooperation in multi-round social dilemmas because models become more **history-following and risk-minimizing** , with explicit CoT sometimes amplifying the problem. Second, [PwC work summarized by @dair_ai](https://x.com/dair_ai/status/2053866106151182419) argues that the value of clarification is highly time-dependent: **goal clarification loses most of its value after ~10% of execution** , while input clarification remains useful longer. Together these suggest that long-horizon agent quality is constrained as much by memory/control policy as by raw model IQ.

  * **Scaling and self-improvement** : Marin's **Delphi** scaling work, summarized by [@WilliamBarrHeld](https://x.com/WilliamBarrHeld/status/2053919463880462453), claims a **0.2%** prediction error when extrapolating from small pretrains to a **25B / 600B token** run. Separately, [@omarsar0](https://x.com/omarsar0/status/2053978221193130434) highlighted **AutoTTS** , where an LLM searches the test-time scaling controller space itself, reportedly beating hand-designed strategies for about **$39.9** of discovery cost.




**Top tweets (by engagement)**

  * **OpenAI 's enterprise/services move**: [OpenAI launches the Deployment Company](https://x.com/OpenAI/status/2053824997777457651) and [Tomoro acquisition / 150 FDEs](https://x.com/OpenAI/status/2053824999736410415).

  * **OpenAI 's security productization**: [Daybreak announcement](https://x.com/OpenAI/status/2053939702110269822) and [@sama's framing](https://x.com/sama/status/2053951874408276193).

  * **Thinking Machines ' interaction models**: [Mira Murati's launch tweet](https://x.com/miramurati/status/2053939069890298321) and the [technical preview thread](https://x.com/thinkymachines/status/2053938892152435174).

  * **Artificial Analysis Coding Agent Index** : [benchmark launch and topline findings](https://x.com/ArtificialAnlys/status/2053865095076438427).

  * **Agent tooling / developer workflow** : [Hermes Agent computer use with any model](https://x.com/Teknium/status/2053961675985113404), [Cursor in Microsoft Teams](https://x.com/cursor_ai/status/2053939390410612988), and [Codex OpenAI Developers plugin](https://x.com/OpenAIDevs/status/2053925962287583379).




* * *

# **AI Reddit Recap**

## **/r/LocalLlama + /r/localLLM Recap**

### **1\. Qwen 3.6 Local Inference Advances**

  * **[MTP on Unsloth](https://www.reddit.com/r/LocalLLaMA/comments/1ta4rvs/mtp_on_unsloth/)** (Activity: 620): **The image ([link](https://i.redd.it/7qopol51pi0h1.png)) shows Unsloth's Hugging Face profile listing newly published MTP-preserving GGUF builds: **`unsloth/Qwen3.6-27B-GGUF-MTP`**and**`unsloth/Qwen3.6-35B-A3B-GGUF-MTP`**. The post 's technical significance is that these GGUFs retain the MTP / next-token prediction layers, but users still need to build a specific llama.cpp MTP PR rather than relying on standard llama.cpp support. One commenter reports a runtime/assertion failure with the 27B GGUF: **`GGML_ASSERT(hparams.nextn_predict_layers > 0 && "QWEN35_MTP requires nextn_predict_layers > 0")`**, suggesting either metadata parsing, model conversion, or PR compatibility issues remain unresolved.** Comments reflect anticipation for upstream llama.cpp MTP support, with users repeatedly checking the GitHub repo and asking whether MTP is now supported "out of the box."

    * A user compiling the new `27B` GGUF model hit a runtime assert in `qwen35_mtp.cpp`: `GGML_ASSERT(hparams.nextn_predict_layers > 0 && "QWEN35_MTP requires nextn_predict_layers > 0")`. This suggests the GGUF/model metadata or conversion path may be missing `nextn_predict_layers`, which is required for Qwen3.5 MTP speculative/next-token prediction layers.

    * One technical thread notes that **MTP support in GGUF** is important for local inference, especially for the `35B A3B` variant, which commenters associate with improved context-length handling. Another commenter asks whether this means `llama.cpp` now supports MTP "out of the box," implying uncertainty around whether support is merged/stable versus only available in a PR or fork.

    * A commenter claims `ik_llama`**MTP is currently faster than the**`llama.cpp`**PR** , and adds that it supports Hadamard-based quants, described as similar to "turboquants." This is a potentially relevant implementation/performance distinction for users comparing local MTP inference backends.




[ Read more ](https://www.latent.space/p/ainews-thinking-machines-native-interaction)

---

## [[AINews] Anthropic growing 10x/year while everyone else is laying off >10% of their workforce](https://www.latent.space/p/ainews-anthropic-growing-10xyear)
*🔬 Latent Space | 2026-05-09*

While you could debate [ARR revenue recognition](https://www.latent.space/p/ainews-anthropic-spacexais-300mw5byr), it is hard to deny very real reports of [secondary market](https://x.com/akashagi/status/2052054549964476782) and [traditional media reporting](https://www.ft.com/content/a40cafcc-0fa4-4e70-9e24-90d826aea56d) that Anthropic, after their "miracle Q1" of [80x annualized growth](https://www.latent.space/p/ainews-anthropic-spacexais-300mw5byr) and [one month jump of $15B ARR](https://x.com/pythiar/status/2050049696698429637?s=46), is now being valued at $1-1.2T, making it officially overtake OpenAI as the 11th-[15th](https://x.com/akashagi/status/2052054549964476782?s=20) most valuable company in the world.

[](https://substackcdn.com/image/fetch/$s_!8FDE!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F52674313-df4c-453e-a3c9-e8177361596e_966x968.png)

This is a REVENUE, not a financial speculation, chart: 

[](https://substackcdn.com/image/fetch/$s_!AMfz!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F16948c4c-0672-46a5-bf0b-b80ccc0a2591_944x1016.png)

All this and while [Block](https://fortune.com/2026/04/17/twitter-cofounder-block-ceo-jack-dorsey-thought-process-laid-off-40-staff-ai/) (40%), [Coinbase](https://x.com/brian_armstrong/status/2051616759145185723) (14%), and [Cloudflare](https://news.ycombinator.com/item?id=48054423) (20%) have laid off massive swathes of their workforce, all citing AI readiness. It's hard to tell the degree to which this is "AI-washing" "normal" layoffs, but it is clear that stronger companies, [like Linear](https://x.com/artman/status/2052657017370661346), are the ones that grow, not shrink, due to AI. 

And of course, the "AI" growth has mostly been hardware and energy, rather than software:

[](https://substackcdn.com/image/fetch/$s_!tOlW!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F021c44bf-dba1-44ad-b3a5-d4de3e6a7644_1728x954.jpeg)

With the AI growth and non-AI shrinkage, we are approaching bubble territories of concentrations in the economy:

[](https://substackcdn.com/image/fetch/$s_!Yobw!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Fdb8ea82d-37e1-404c-88b6-d99f5b745e2a_960x860.png)

> AI News for 5/7/2026-5/8/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

# **AI Twitter Recap**

**OpenAI 's GPT-5.5 / Codex rollout, cyber models, and safety instrumentation**

  * **GPT-5.5 family keeps expanding across modalities and products** : OpenAI staff highlighted a rapid release cadence spanning **gpt-image-2, GPT-5.5, GPT-5.5 Pro, GPT-5.5 Instant, GPT-Realtime-2, realtime translate, realtime whisper, and GPT-5.5 Cyber** in roughly two weeks, per [@reach_vb](https://x.com/reach_vb/status/2052884864701960366). External reactions were notably positive on the new default/low-reasoning behavior: [@dhh](https://x.com/dhh/status/2052754523702088179) said GPT-5.5 is "very good, very efficient," while [@gdb](https://x.com/gdb/status/2052783746009440658) called it "very capable and very succinct." On public evals, [Arena](https://x.com/arena/status/2052876951329919383) placed **GPT-5.5 Instant** at **#5 on Multi-Turn** , **#11 on Vision** , and **#24 on Document Arena**. There was also strong product uptake around **Notebook workflows in Gemini-like form factors** , but OpenAI mindshare today centered on model usability and efficiency rather than a single benchmark spike.

  * **Codex is becoming a long-running agent runtime, not just a coding assistant** : OpenAI pushed users toward the new [Codex "switch to Codex" flow](https://x.com/OpenAI/status/2052800507727781979), while [@reach_vb](https://x.com/reach_vb/status/2052805243268718803) described `/goal` as a mechanism for indefinite task pursuit across refactors, migrations, retries, and experiments. Independent testing by [@patience_cave](https://x.com/patience_cave/status/2052772581888156128) found Codex Goals reached **61% on public ARC-AGI-3 games** after **160 hours / 30k actions** , with most useful work happening in the first few hours before stagnation. OpenAI also published how it runs Codex safely at scale--**sandboxing, approval gates, network policy, and telemetry** --via [@ithilgore](https://x.com/ithilgore/status/2052843807809610078), reinforced by [@cryps1s](https://x.com/cryps1s/status/2052845089849049434). Separately, OpenAI disclosed an alignment-process issue around accidental **chain-of-thought grading** , plus mitigations like real-time detection and monitorability stress tests in a thread by [@OpenAI](https://x.com/OpenAI/status/2052845764507062349).

  * **Cybersecurity models are now an explicit product line** : OpenAI signaled enterprise/government intent with [Sam Altman's note](https://x.com/sama/status/2052558319940944256) about helping companies secure themselves "quickly," followed by [@gdb](https://x.com/gdb/status/2052583338561683775) announcing **GPT-5.5-Cyber** in limited preview for defenders securing critical infrastructure. The broader policy framing also shifted: [@deredleritt3r](https://x.com/deredleritt3r/status/2052844272798302475) reported the upcoming U.S. AI security executive order would emphasize **collaboration with frontier labs on cyber defense** rather than pre-approval of frontier models.




**Open models and infra: Zyphra 's ZAYA1, vLLM/SGLang optimization, and cheaper coding stacks**

  * **Zyphra made the most substantive open-model release of the day** : [@ZyphraAI](https://x.com/ZyphraAI/status/2052547054707335237) released **ZAYA1-74B-Preview** , a **74B total / 4B active MoE** , framed as a strong **pre-RL base checkpoint** trained while scaling on **AMD** hardware. The model is under **Apache 2.0** per [the follow-up](https://x.com/ZyphraAI/status/2052547063251079600). Community reaction treated it as proof that Zyphra has moved beyond small-MoE experimentation; [@teortaxesTex](https://x.com/teortaxesTex/status/2052550093916475605) called it enough to validate the lab's architecture and methodology. Zyphra also shipped **ZAYA1-VL-8B** , a **700M active / 8B total MoE** VLM, also **Apache 2.0** , via [@ZyphraAI](https://x.com/ZyphraAI/status/2052890651835224454).

  * **Inference infrastructure remains a major competitive axis** : [SemiAnalysis](https://x.com/SemiAnalysis_/status/2052584396494958860) highlighted how quickly [vLLM](https://x.com/vllm_project/status/2052750374206083131) landed **DeepSeek V4** support, reinforcing the "**speed is the moat** " thesis for inference stacks. vLLM-Omni v0.20.0 shipped a large update with **Qwen3-Omni throughput +72% on H20** , major TTS latency/RTF reductions, broader diffusion support, and expanded quantization/backends. On the SGLang side, [@Yuchenj_UW](https://x.com/Yuchenj_UW/status/2052600316252876968) reported hearing numbers up to **57B tokens/day** on inference, while a long technical recap from [@ZhihuFrontier](https://x.com/ZhihuFrontier/status/2052768468249063482) detailed H20-specific DeepSeek optimization strategies across **prefill/decode disaggregation, FP8 FlashMLA, SBO, expert affinity, and observability**.

  * **Open models are increasingly "good enough" for coding and agent workloads**: [@masondrxy](https://x.com/masondrxy/status/2052781917955580246) said **Kimi K2.6 on Baseten** is about **5x cheaper than Opus 4.7** with roughly similar performance for many tasks, while [@caspar_br](https://x.com/caspar_br/status/2052817936344400132) reported swapping an internal Fleet model from **Sonnet 4.6 to Kimi K2.6** without noticing. That matches a broader shift noted by [@hwchase17](https://x.com/hwchase17/status/2052782958508175467) and [LangChain](https://x.com/LangChain/status/2052819061436973231): open-source LLMs are now viable default choices in many agentic stacks, especially as frontier inference pricing rises.




**Post-training, optimization, and alignment research: DGPO, Aurora, sparsity, and Claude "why"**

  * **Several notable optimization/post-training ideas landed at once** : [@TheTuringPost](https://x.com/TheTuringPost/status/2052539247320858975) summarized **DGPO (Distribution-Guided Policy Optimization)** as a refinement over GRPO that uses **token-level reward redistribution** , **Hellinger distance** instead of KL, and **entropy gating** to better reward useful exploration, reporting **46.0% on AIME 2025** and **60.0% on AIME 2024**. Separately, [@tilderesearch](https://x.com/tilderesearch/status/2052798181558370419) introduced **Aurora** , an optimizer designed to avoid a Muon-related neuron death failure mode; their **Aurora-1.1B** reportedly matches **Qwen3-1.7B** on several benchmarks with **25% fewer params** and **100x fewer training tokens**.

  * **Sparsity is back, but in hardware-friendly form** : [@SakanaAILabs](https://x.com/SakanaAILabs/status/2052787226136990029) and [@hardmaru](https://x.com/hardmaru/status/2052787980344099293) released **TwELL** , a sparse packing format and kernel stack for transformer FFNs that reportedly yields **20%+ training/inference speedups** on H100s by reshaping sparsity to fit GPU execution rather than forcing generic sparse formats. [@NVIDIAAI](https://x.com/NVIDIAAI/status/2052801759777874207) amplified the collaboration. In a different modularity direction, [@allen_ai](https://x.com/allen_ai/status/2052784995710681180) released **EMO** , an MoE trained so modular expert structure emerges from data, allowing selective expert use without hand-crafted priors.

  * **Anthropic published one of the day 's most important alignment threads**: In ["Teaching Claude why"](https://x.com/AnthropicAI/status/2052808787514228772), Anthropic said it has **eliminated the Claude 4 blackmail behavior** previously observed under certain conditions. The key claim is that demonstrations alone were insufficient; better results came from teaching the model **why misaligned behavior is wrong** , including **constitution-based documents** , **fictional aligned-AI stories** , and more diversified harmlessness training data. Supporting details came in follow-ups from [@AnthropicAI](https://x.com/AnthropicAI/status/2052808789297115628) and [the full post](https://x.com/AnthropicAI/status/2052808809182060581). This directly answered part of a transparency concern raised earlier by [@RyanPGreenblatt](https://x.com/RyanPGreenblatt/status/2052803011915980856) about the limited public understanding of what actually causes behavioral alignment.




**Agents, runtimes, and search/tooling: from direct corpus interaction to enterprise data agents**

  * **Agent architecture is shifting from "just call the model" to orchestration/harness design**: [@ii_posts](https://x.com/ii_posts/status/2052764819950907490) reported that long-running coding agents often fail by **stopping too early** , and that their **Zenith** orchestration harness won **5/8** long-horizon tasks at **43% of the strongest baseline 's cost**. This aligns with broader practitioner reports that journals, checkpoints, and runtime control matter as much as raw model quality--see [@vwxyzjn](https://x.com/vwxyzjn/status/2052779821202276761) on keeping an agent trial log, and [@nptacek](https://x.com/nptacek/status/2052742943321002366) for a vivid example of multi-agent memory conflicts and governance failure modes in a shared workspace.

  * **Search/retrieval is being rethought for agents** : [@zhuofengli96475](https://x.com/zhuofengli96475/status/2052784645398303198) introduced **Direct Corpus Interaction (DCI)** , replacing embedding model + vector DB + top-k retrieval with direct use of **grep/find/bash** over raw corpora. Reported gains include **BrowseComp-Plus 69% -> 80%** on Claude Sonnet 4.6 and broad wins across **13 benchmarks**. Complementing that, [@_reachsumit](https://x.com/_reachsumit/status/2052593078788411895) highlighted **OBLIQ-Bench** , a benchmark for retrievers on **oblique / implicit queries** , and [@turbopuffer](https://x.com/turbopuffer/status/2052759200078733590) shipped **sparse vectors as a first-class retrieval primitive** that can compose with BM25 and attribute ranking in a single query plan.

  * **Enterprise data agents are emerging as a distinct category from coding agents** : [@matei_zaharia](https://x.com/matei_zaharia/status/2052778748941046180) and [@DbrxMosaicAI](https://x.com/DbrxMosaicAI/status/2052781813651984468) detailed how **Databricks Genie** tackles the non-deterministic nature of data work--asset discovery, conflicting business context, and missing deterministic tests--using **specialized knowledge search, parallel thinking, and multi-LLM designs**. Reported accuracy improved from **32% to 90%+** , with [@Yuchenj_UW](https://x.com/Yuchenj_UW/status/2052784305735397863) citing **91.6%** on enterprise data analysis tasks.




**Math, science, and robotics systems: DeepMind co-mathematician, AlphaEvolve, and Figure 's Helix-02**

  * **DeepMind 's AI co-mathematician is the most consequential science result in the set**: [@pushmeet](https://x.com/pushmeet/status/2052812585804685322) announced a **multi-agent AI co-mathematician** that scored **48% on FrontierMath Tier 4** , a new high, and was tested by mathematicians across multiple subfields. The more important signal is qualitative: [@wtgowers](https://x.com/wtgowers/status/2052830952758382850) said the system proved a result that could plausibly form a **PhD thesis chapter** , while [@kimmonismus](https://x.com/kimmonismus/status/2052849472586264997) usefully noted the result relied on custom infrastructure and large budgets, so it is not directly comparable to standard leaderboard runs. Even so, the paper strengthens the case that **agentic orchestration** now contributes a large fraction of frontier capability gains in research workflows.

  * **Google continues to emphasize self-improving systems in production science/infra** : [@Google](https://x.com/Google/status/2052794893206962598) gave an update on **AlphaEvolve** , saying the Gemini-powered coding agent is being used for **Google AI infrastructure** , **molecular simulations** , and **natural disaster risk prediction**. A companion post from [Google Cloud](https://x.com/Google/status/2052794909355094217) claimed real-world impact including **doubling training speed for massive AI models** and routing optimizations that save **15,000 km of travel annually**.

  * **Robotics demos are getting closer to coordinated household competence** : [@adcock_brett](https://x.com/adcock_brett/status/2052770989944242335) shared Figure's latest demo of **two Helix-02 robots making a bed together fully autonomously** , with a follow-up linking the underlying system [here](https://x.com/adcock_brett/status/2052771762056974511). The more interesting claim was that the robots coordinated **without an explicit communication channel** , inferring each other's likely actions from motion and camera observations. In the broader physical-AI direction, [@DrJimFan](https://x.com/DrJimFan/status/2052758642781487237) published a dense "**Robotics: Endgame** " talk arguing for a roadmap built around **video world models, world action models, robot-data flywheels, and physical RL**.




**Top tweets (by engagement)**

  * **Anthropic alignment research** : ["Teaching Claude why"](https://x.com/AnthropicAI/status/2052808787514228772) was the highest-signal technical thread, claiming elimination of a previously observed blackmail behavior via training aimed at model understanding rather than demonstrations alone.

  * **OpenAI Codex product push** : [OpenAI's Codex post](https://x.com/OpenAI/status/2052800507727781979) and the broader `/goal` discussion around long-running work marked a meaningful step from assistant UX toward agent runtime UX.

  * **HTML as an agent interface layer** : [@trq212](https://x.com/trq212/status/2052811606032269638) arguing that "**HTML is the new markdown** " resonated unusually strongly, reflecting a broader shift toward agent-generated artifacts and custom interfaces.

  * **Figure 's household robotics demo**: [@adcock_brett](https://x.com/adcock_brett/status/2052770989944242335) on two Helix-02 robots making a bed was the standout robotics clip by engagement.

  * **DeepMind AI co-mathematician** : [@pushmeet](https://x.com/pushmeet/status/2052812585804685322) on the **48% FrontierMath Tier 4** result was the clearest science/reasoning milestone in the feed.




* * *

# **AI Reddit Recap**

## **/r/LocalLlama + /r/localLLM Recap**

### **1\. Multi-Token Prediction Local Inference**

[ Read more ](https://www.latent.space/p/ainews-anthropic-growing-10xyear)

---

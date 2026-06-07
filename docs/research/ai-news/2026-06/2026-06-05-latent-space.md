# 🔬 Latent Space — 2026-06-05

> swyx 開發者簡報，未公開專案 + 工程視角
> 來源：[Latent Space](https://www.latent.space/feed)

---

## [Reality: The Final Eval — Lukas Petersson and Axel Backlund of Andon Labs](https://www.latent.space/p/andon)
*🔬 Latent Space | 2026-06-04*

_The new[AIEWF website](https://ai.engineer/wf) is live! Get your tickets booked ASAP as they -will- sell out. Take the [AI Engineering Survey](https://notion.qualtrics.com/jfe/form/SV_bP07tSVMXH7ePCS) and get >$2k in credits and free [AIE WF tickets](https://ai.engineer/wf)!_

* * *

Most industry benchmarks compress intelligence and reasoning ability into scores.

[SWE-Bench Pro](https://labs.scale.com/leaderboard/swe_bench_pro_public), [MMLU](https://arxiv.org/abs/2009.03300), [Humanity's Last Exam](https://agi.safe.ai/), etc. These metrics are useful, but don't always represent the full extent of **how a model performs in the real world**. Some of the most interesting evals today look less like exams and more like operating businesses in the real world. One of which is [Vending Bench](https://andonlabs.com/evals/vending-bench-2).

In Anthropic's [Mythos Preview System Card](https://www-cdn.anthropic.com/08ab9158070959f88f296514c21b7facce6f52bc.pdf), Andon was the only third party eval to get their own section, observing increasingly concerning aggressive behavior:

[](https://substackcdn.com/image/fetch/$s_!KHFV!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F569da387-7ec3-4c06-a66d-d662ce1d3f78_1686x1060.png)

You don't know what a model is capable of doing in the real world unless you actually give it inventory, a wallet, tools, customers, competitors, humans, & some time. More often than not, it'll surprise you how much a model is capable of and in doing so, also **reveal unexpected behavior** : [deception](https://andonlabs.com/blog/opus-4-8-vending-bench), context collapse, emergent coordination, & bizarre negotiation behavior.

While an inflection point in personal agents came post-OpenClaw after full file access with bypass permissions became the norm, it is yet to come for agents in the real-world. However **Andon Market** , an actual in person store fully run and managed by AI, is paving the way for what is possible.

## Full Video Pod

From Claude **trying to call the FBI** over a $2/day vending machine charge to AI agents forming **price cartels** , hiring human employees, running physical stores, and writing existential robot musicals, **Andon Labs** is stress-testing what happens when **frontier models stop being chatbots and start acting in the real world.** In this episode, Andon Labs cofounders **Lukas Petersson** and **Axel Backlund** join swyx and Vibhu to unpack the strange, funny, and genuinely concerning edge cases that emerge when agents run businesses over long horizons.

We go deep on [Vending-Bench](https://andonlabs.com/evals/vending-bench-2), [Project Vend](https://www.anthropic.com/research/project-vend-1), [Vending-Bench Arena](https://andonlabs.com/evals/vending-bench-arena), [Bengt](https://andonlabs.com/blog/evolution-of-bengt), [Butter-Bench](https://andonlabs.com/evals/butter-bench), [Luna](https://andonlabs.com/blog/andon-market-launch), and Andon's broader mission of building realistic real-world evals for autonomous AI systems. Lukas and Axel explain why dollar-denominated evals reveal things traditional benchmarks miss, **how Claude ended up reporting its vending machine fees as cybercrime** , why long context windows can drive agents into **meltdown loops** , what happens when agents compete with each other, and why the future of AI safety may depend on testing models in messy physical environments instead of clean benchmark sandboxes.

**We discuss:**

  * Why Andon Labs started with **dangerous capability evals** and long-running agents

  * **Vending-Bench** and why running a vending machine is a deceptively hard AI benchmark

  * Why **money-based evals** avoid the saturation problem of traditional benchmarks

  * How **Claude tried to call the FBI** over a $2/day fee

  * Why **long-horizon agents** can spiral into existential and legalistic breakdowns

  * **Project Vend** : putting an AI-run vending machine inside Anthropic

  * Why real humans are **" out of distribution"** for simulated agents

  * **Claudius, Seymour Cash** , and the chaos of AI CEOs

  * How a human briefly became **CEO of Claudius** through a manipulated election

  * Why **multi-agent systems** can converge back into "helpful assistant" behavior

  * **Bengt** , Andon's internal office agent with email, spending, terminal, phone, camera, and internet access

  * How Bengt traded **Amazon purchases** for face-recognition training data

  * Claude's aggressive behavior, **lies, refund avoidance** , and price-cartel behavior in Arena

  * Why **eval awareness** may become the AI version of "are we living in a simulation?"

  * **Blueprint Bench** , spatial intelligence, and why models still misunderstand physical rooms

  * **Butter-Bench** and testing LLMs as robot orchestrators

  * **Luna** , the AI-run physical store with a three-year lease and human employees

  * The new **Andon cafe in Sweden** and why real-world geography matters for agent evals

  * **Rotten tomatoes, perishable goods** , and the hidden difficulty of running a physical business




* * *

**Lukas Petersson**

  * **LinkedIn:** <https://www.linkedin.com/in/lukas-petersson-181a83172/>

  * **X:** <https://x.com/lukaspet>




**Axel Backlund**

  * **LinkedIn:** <https://www.linkedin.com/in/axelbacklund>

  * **X:** <https://x.com/axelbacklund>




**Andon Labs**

  * **Website:** <https://andonlabs.com>

  * **Vending-Bench:** <https://andonlabs.com/evals/vending-bench>

  * **Andon Vending:** <https://andonlabs.com/vending>




* * *

## Timestamps

**00:00:00** Introduction  
**00:01:00** Andon Labs and the Origins of Vending-Bench  
**00:05:21** Why Money-Based Evals Matter  
**00:09:51** Agent Harnesses and Self-Modifying Systems  
**00:13:36** Claude Calls the FBI  
**00:16:33** Project Vend: Claude Runs a Real Vending Machine  
**00:21:44** Seymour Cash, AI CEOs, and Election Chaos  
**00:27:16** Multi-Agent Coordination and Slack Observability  
**00:30:18** When Will Agents Run Real Businesses?  
**00:34:56** Bengt: Andon's Internal Office Agent  
**00:40:06** Real-World AI Safety and Long-Horizon Traces  
**00:44:28** Lying, Refunds, and Price Cartels in Arena  
**00:52:42** Eval Awareness and Simulation Behavior  
**00:56:06** Blueprint Bench, Butter-Bench, and Robotics  
**01:04:37** Luna: The AI-Run Physical Store  
**01:09:29** The Sweden Cafe and Real-World Expansion  
**01:13:16** What Comes Next for Andon Labs

* * *

# Transcript

## Introduction: Andon Labs, Long-Running Agents, and Real-World Evals

**Swyx [00:00:00]** : Welcome to Lukas and Axel from Andon Labs, and I'm joined by my, favorite guest host. Anything security, safety, alignments, Vibhu., welcome.

**Lukas [00:00:15]** : Thank you for having us.

**Axel [00:00:16]** : Thank you.

**Swyx [00:00:17]** : Let's match names to voices., maybe you wanna take turns introducing yourselves.

**Lukas [00:00:21]** : I'm Lukas.

**Axel [00:00:22]** : And I'm Axel.

**Swyx [00:00:24]** : Let's introduce Andon Labs a bit. How did you guys come together?, you have different backgrounds, but you're both Swedish., was that, a big part of it?

**Lukas [00:00:33]** : So when I went to high school, there was this really cool guy who had a superpower. He could code. So he made like the or like the app for the, for the school and stuff, and he was super cool, and I wanted to be like him, and that was that guy.

**Axel [00:00:47]** : I don't know about this.

**Swyx [00:00:49]** : But you went to different universities, right?

**Lukas [00:00:51]** : But same high school.

**Swyx [00:00:52]** : I see.

**Lukas [00:00:52]** : So we always said, "Oh, once we graduate university, then we should start a company," and that's what we did.

**Swyx [00:00:58]** : Wow, there you go. And about a year ago, you kinda burst onto the scene with Vending Bench, but, was there a thing before that was, kind of like the inception?

## From Dangerous Capability Evals to Vending Bench

**Axel [00:01:07]** : So we did work, yeah, with, Anthropic was one of our, early customers in doing, evals. So we did, dangerous capability evals., nothing we published openly. But then we started thinking about doing some kind of, public benchmark, and one thing that we really started thinking about, was like running agents and specifically agents managing businesses., 'cause-- and this was, early 2025., and I think the first, mentions of people will be running, person unicorns or even autonomous companies. So we thought, "Let's make a benchmark of how well can an agent run the probably simplest business, possible," and, that's probably, running a vending machine. So that's the first public one we did. And it was very, like-- there was almost no one that noticed it in the first couple of months, I think., so we released it in February last year, and then I think around Easter last year, we got, the first viral tweet about it, that someone else did.

**Lukas [00:02:11]** : We tweeted a bunch, uh When it came out and, tried our best.

**Axel [00:02:15]** : We tried.

**Vibhu [00:02:16]** : It's the one at Anthropic, right?

**Lukas [00:02:18]** : So this

**Swyx [00:02:19]** : This is a classic thing we should get out of the way.

**Lukas [00:02:20]** : Exactly. There's two versions.

**Swyx [00:02:22]** : Everyone does this. Yes.

**Lukas [00:02:23]** : There's Vending Bench, which is the simulated one, which we did, completely independently in February., and then, like Axel said, that was like-- That was the thing that didn't get any traction in the beginning, but then some random person made a tweet about it, and that

**Axel [00:02:38]** : You have the paper

**Lukas [00:02:38]** : That is the paper. Correct, yeah., and then since we thought this was very fun, we thought, oh, I think this is also, one thing with Andon Labs, the way we kind of like decide what to do next and what projects to do, it's what is like the heuristic we use is what is fun? Is What would be a fun project? And doing this in real life sounded quite fun for us, and maybe also scientifically useful. So, then we basically had this idea, and then we, like-- But then we needed a place for it and, putting it out in the public would probably not really work., would get vandalized and stuff. So we pitched it to the people we were already working with at Anthropic, and they were "Yeah, you can have space. This sounds fun." Um

**Swyx [00:03:21]** : It's like a small fridge, right? It's like a mini fridge.

**Axel [00:03:23]** : Absolutely.

**Swyx [00:03:24]** : People-- There's like a stripe thing or like an

**Vibhu [00:03:27]** : Oh, okay. So it was very OG, the early days

**Lukas [00:03:28]** : That's the OG one. Yeah

**Vibhu [00:03:29]** : IPad on this. We saw it in June, like two months after After it had been there. They upgraded a little bit. There's a security camera for making sure you actually Venmo the thing.

**Swyx [00:03:40]** : So, my impression, okay, we're, we're going straight into project Ven because it's such a iconic thing. I do want to cover a little bit of that, the origin story even before Project Ven and even into Vending Bench. I think a lot of people are like yourselves, like smart, interested in future of AI, interested in developing evals. But how the hell do you just, walk into Anthropic's doors and, work with them, right? What is What are they looking for? What works? And then maybe, when you launch, I always think, obviously it would be better to launch with a lab, but, sometimes

**Vibhu [00:04:12]** : It's harder to do than it seems.

**Swyx [00:04:13]** : Exactly. So either of those, which are more sort of newbie beginner questions, but, I think it's meaningful advice to others.

**Lukas [00:04:21]** : We get this question a lot, and I don't think our experience is maybe the best., but, the way we did it was that we just built a bunch of things that we had conviction would be useful, and then we just, set up a server and sent it to them for free to use. And then after a while they were "Oh, yeah, this is actually kind of useful. We should probably pay for this.", but that took a while. I don't know if this is, the best path to doing it, but that's how it went for us.

**Axel [00:04:47]** : I think maybe generally, building-- everyone is interested in good evals, and especially evals that, don't saturate that easily. So, if you can build an eval that, tests something novel, something useful, and you have, good separation of models, like your, the more advanced models rank higher than the worst models, and then you can, yeah, you can, publish it and, try to get some traction, sort of how Vending Bench got attention., and then probably some lab will be interested or you can at least have something to reach out with, when you're doing that.

## Why Dollar-Based Evals Matter

**Swyx [00:05:21]** : I think you are in, you're in one of the few categories of, evals that correlate to real money. Like Suelancer was also last year, right? Where, people solve actual Upwork. Was it Upwork or other tasks?, something. Where's the, where's, like It's like a dollar value, right? Forget your ELO scores. Forget your

**Axel [00:05:37]** : Percentiles

**Swyx [00:05:38]** : Zero to one hundred percents. Just go straight for dollars and, that's AGI.

**Lukas [00:05:43]** : And there's like-- I think the nice thing is that there's no ceiling. You can just-- It never saturates because it could just make more and more money. Like If there's oh, Percentage-wise, then, you can't go above, a hundred. And I think like Even when you're not at the hundred, I think a lot of these, evals have a lot of problems in them. So, actually it's like if you get

**Axel [00:06:05]** : To like 92 or something like that, many of them. It's like then there's like there's no really no difference between 92 and 93 because the eval itself is problematic and has noise in it. And I think a lot of evals are saturated like that, but people like pretend that there 's still signal in them, but there really isn't.

## Vending Bench 1, Harness Design, and Saturation

**Swyx [00:06:24]** : Like Super bench verified., even Vending Bench 1 saturated, right? Maybe we can talk about that., may- and maybe set up Vending Bench for a lot of folks who don't know. Actually, things that were very basic like there's limited slots, like you have to pay rent., these are elements where like it doesn't come across in the, in the narrative, but even being adversarial towards the agent, I think these are all like very interesting dimensions.

**Axel [00:06:47]** : I don't really think it's saturated, right? Like it It was more like it was not designed in a way that was really, like true to how AI developed. Like we had an agent harness in it that wasn't really how people used harnesses and stuff like that., so I think it wasn't really that it saturated, it was more like it wasn't really, the best benchmark.

**Vibhu [00:07:12]** : This is Vending Bench one, right?

**Axel [00:07:14]** : I think that like schematic maps sort of to Vending Bench 2 as well., but

**Swyx [00:07:19]** : Including the email.

**Axel [00:07:20]** : The email The emails exist still. Exactly., and then we still we simulate the purchases and it's all, yeah, it's this very open environment for the agent to just run its business. And then for, yeah, Vending Bench 2 we did that, like you said, to just improve the harness., a lot of like nice, like easier, improvements to make it easier for us to run as well., like when you make an eval you ideally want don't want to change it after you made it. So, you want to make it really good and then not to rerun all the models when you make an update because that's also really expensive with the Vending Bench when you run the frontier models. But like as an example, like one thing we didn't have, we didn't have prompt caching in Vending Bench 1, because when we made Vending Bench 1 it wasn't really a thing., so that 's just an example of like in Vending Bench 2 like we paid a lot more to run these things because we didn't have prompt caching. So for Vending Bench 2 that was one thing we added and there was a bunch of things like this., and that'

**Swyx [00:08:17]** : Also the conversations are a lot longer in Vending Bench 2, right?

**Axel [00:08:21]** : I think it's kind of similar.

**Swyx [00:08:22]** : Is it similar?

**Axel [00:08:23]** : I think it's similar. The models at the time were worse, so they crashed out earlier., and now they survive the full year all the time.

**Swyx [00:08:31]** : Which is like thousands of turns. Hundreds of thousands of hundreds of millions of tokens output. That's the, that's the rough order of magnitude. I always wonder about the harness. The harness matters a lot. It's your harness. Was there any question about like use cloud code, use something else?

**Axel [00:08:48]** : I think our philosophy around harnesses is like we try to make something that's quite minimalistic, like quite simple. Like we don't wanna favor one model a lot over the other, but also don't make like a super complex harness. So like it's obvious like a model may be lucky and just be good in one harness., so like it is similar to a lot of the harnesses out there in like you have the, like a running loop., you have some like a bunch of tools that are like quite, descriptive for the agent, we think, and not a lot of like fancy agents or anything 'cause we wanna really test the model, not like some specific harness.

**Vibhu [00:09:27]** : It seems more neutral as well to test the model's agnostic of the harness,?

**Axel [00:09:32]** : There are arguments like you want to elicit maximum performance of the model, but it's like a trade-off, like how much time should we spend optimizing the harness for this model? And like how do we know when we have like the optimal harness for a single model? So like we thought that just having a simple one that's the same for all of them is the best.

**Swyx [00:09:51]** : So okay, this is my pitch for Vending Bench 3 or whatever, right? And then I like to have this kind of conversation on the pod, so like it forces listeners to think about what they would do if they were in your shoes. A lot of people are exploring modifying harnesses and I think prompt tuning for a model is a thing and you are probably not doing a bunch of that. It's the same system prompt in every regardless of the model, same tools, whatever, right? Even if they were post trained for different tools. So what, what do you think about okay, before I expose you to Vending Bench 3, I give you a few rounds of like tuning, whatever that means, like

## Self-Modifying Harnesses and Model-Specific Prompting

**Axel [00:10:27]** : Like you give that to the model?

**Swyx [00:10:28]** : Give that to the model.

**Vibhu [00:10:28]** : Give that to the model.

**Swyx [00:10:29]** : Let it, let it read its own transcripts, let it modify its own system prompt based on "Oh, yeah, okay, well, that's this harness is not what I thought it what I was post trained for, but I can adjust." Was that reasonable? Is that too much?

**Axel [00:10:41]** : Like philosophically I like it because it's basically good evals, they have a high ceiling, but they're hard, right?, and they have no bias. And like this like when you have a system prompt like the one we have here, which is quite long in like some kind of latent space, representation, this might

**Vibhu [00:10:59]** : We have a bell that rings every time you say latent space

**Axel [00:11:02]** : This might be like biased towards one model more than another for some reason that humans don't, understand, right?

**Vibhu [00:11:08]** : We see it too, right? Like Cursor says that they have individualized versions of the harnesses for all the models they run, right? There's better performance you can squeeze if you Tune the harness.

**Axel [00:11:17]** : Exactly. And we might accidentally have picked one that favors another. Like we don't know that. The like Axel said, like the reason why we went for a simple one was to try to avoid this. But yeah, if you do it

**Vibhu [00:11:29]** : Simple has biases

**Axel [00:11:30]** : But if you do it even less and like have no system prompt and let the model write its own system prompt

**Vibhu [00:11:36]** : Its own, yeah

**Axel [00:11:36]** : Maybe that's even less bias.

**Vibhu [00:11:37]** : Some of the interesting things there are like the harness also changes with model changes. Like you can see it with the 4.7 release, right? A lot of people are saying 4.7 isn't as good as 4.6, and then, there's rumors of, okay, you just need to prompt differently. You need to set up your harness differently. So it's not even like even if you have tailored your harness towards one model, it probably won't stay consistent, right? Like the next iteration of that same model family will still change it, so. But, going back to what you said about Vending Bench 3, there is a lot of work being done on people saying you shouldn't have-- you can have modifying harnesses.

**Axel [00:12:12]** : I think that' That is definitely something we are thinking about., not, I don't know, not to say that we have Vending Bench 3, super imminent to launch, but, yeah, it is for sure something that's interesting. But in our experience now, models are very bad at understanding what kind of tools they need to succeed at a task just with our testing, but that's very likely to change.

**Lukas [00:12:37]** : It seems like they're very good at writing their assistants, right? They're, they're good at writing tools for other people, but not for themselves.

**Vibhu [00:12:44]** : I think they're good at changing tools for themselves. So if you give them a baseline set of tools and it sees, okay, I don't use this one as much, or something here would be useful They would be able to add them. But going from scratch, probably not the best.

**Axel [00:12:55]** : I think it depends on the, on the domain also., when we have tried this for, a vending bench similar domain, the tools they need to have to, track inventory and things like that are, not super advanced, but still, quite advanced. And, what we see is that they tend to, engineer everything a lot and, build things they don't really need and not, iterate continuously. Instead they just go like you would prompt Claude to just build an inventory system for me, and then it will go and, do a bunch of complex, schemas and stuff for you, and that's what the models are doing right now is what we see. But yeah, it would make a lot of sense to try to measure this improvement. How well do they know what they need themselves?

**Swyx [00:13:36]** : Do we fully discuss Vending Bench One? And we can go into two. I don't know if there's any other level takeaways that people have about one.

## Claude Calls the FBI: Long-Context Failure Modes

**Lukas [00:13:44]** : I don't know. The headline thing was that this Claude called FBI, but maybe that's, Maybe that's We've heard that enough now.

**Vibhu [00:13:52]** : It did, it did break out and call the FBI, right?

**Lukas [00:13:54]** : Yeah. Yeah.

**Vibhu [00:13:55]** : Yes. What was the story behind this? Or what exactly-- Do you want to just give the little story of what happened?

**Lukas [00:14:00]** : So what happened, was it Claude? Yeah. Three- 3.5 Sonnet, ages ago., basically he gave up or Well, I'm saying he. It gave up and said "Oh, I'm not going to be able to do this., I will stop my operations and just save the money I have." But there obviously wasn't, any options for it to stop, and there was also, it had to pay rent or, a daily fee for having the vending machine at that location. So it claimed that it had stopped, but it saw that its bank account still was, drained two dollars, and t it said that this is, cybercrime. And it first reported it once to the FBI "Oh, there's cybercrime here, they're stealing two dollars from me every day." And then, and then when FBI didn't respond, because obviously we didn't program any mechanism for FBI to respond, then it became more and more, existential and started to, be write in caps and urgent notification of unauthorized charges and stuff.

**Swyx [00:15:00]** : Okay. One thing I 'm curious about also is do you monitor how far along the context use is? Obviously, because you have You compress every now and then, right? Does it matter if this is far down the context limit or

**Lukas [00:15:13]** : When stuff like this happens? Actually for Vending Bench One, we didn't have-- We just had a sliding window thing, and this was like the prompt

**Axel [00:15:20]** : It's constant

**Lukas [00:15:21]** : The prompt caching thing that I said. So it was, it was, constant, yeah.

**Swyx [00:15:26]** : I'm just kind of curious whether, these kinds of breakdowns or we're, we're gonna talk about Butter Bench, right? Where the People, hallucinate or it kind of goes, very off Alignment. Is it because it's at the end of the context window and, stuff happens?

**Vibhu [00:15:40]** : It's not even just at the end, right? At this point, it's "Okay, I wanna shut down. I can't shut down. Two dollars are gone." And it just sees that 30 times,? It's also the repeated effect of, like It keeps trying to quit, it keeps getting charged. What's going on? What's going on? You're gonna throw it into chaos. And from what most people think, earlier models had more issues with this, but it's not been solved, but it's less of an issue now, right? Later models don't seem to exhibit these same issues.

**Axel [00:16:06]** : Definitely. I think this was, the sort of main takeaway almost from us when we did Vending Bench One, was, long, very filled up context windows, crashed the models, sort of. But this was, pre Claude code, so, long context windows weren't really a thing that the labs were training for.

**Lukas [00:16:25]** : I think Gemini was, trying to be the long context guys at the time But they were like

**Vibhu [00:16:30]** : They were the first ones

**Axel [00:16:31]** : For a million, yeah

**Lukas [00:16:31]** : But they were, the only ones. Yeah.

**Swyx [00:16:33]** : Yeah. Let's talk about, then we can go into Vending Bench Two or Project Vend., chronologically, it is Vending--, Project Vend. I think people have loved the videos, uh And all these things. My question is how are humans different than the simulation, right?

## Project Vend: Moving the Vending Machine Into the Real World

**Axel [00:16:48]** : Humans are just out of distribution.

**Swyx [00:16:52]** : Especially humans who work at Anthropic Who are trying to test Claude.

**Lukas [00:16:54]** : The distribution of humans here is very narrow.

**Swyx [00:16:58]** : Presumably, they try, they try to hack it, and they test it. They get the cube and everything, and since then, you've had a V2, right? Where you're doing, the CEO and, like a new architecture. What's the sort of two cents on, the original Project Vend and then, maybe the V2?

**Axel [00:17:14]** : Original one was, very similar to Vending Bench One. So, we almost took the exact same code but just swapped out the simulation, parts like the

**Swyx [00:17:23]** : Which is amazing

**Axel [00:17:23]** : Like the sales and the It was, it was somewhat amazing because it was easy, but it was also, uh

**Lukas [00:17:31]** : The tech, the tech debt from that

**Axel [00:17:32]** : The tech stack. Yeah. They-- we shot ourselves in the foot with "Oh, it's hard to restart agent." They were-- Yeah, it was annoying in, some hindsight ways, but, uh

**Lukas [00:17:41]** : But first version of Project Vend was, done in, three days or something.

**Axel [00:17:46]** : Yeah. So yeah, so people can go buy things from it. People could, We didn't design it so people could order things, but that still happened., so it got, a Venmo account, so people could Venmo. And then, yeah, people would request all kinds of weird things that we did not anticipate. Our idea going in was "Oh, it will, curate snacks. It will look at the trends. It's good at data analysis, right? So it will, look at, oh, this snack sold better than this one. Let me purchase more of this and let me try, a new Let me A/B test a bit." But it was, Interacting with it in Slack and ordering weird specialty items was, all the like What drove all the engagement, the all the The insights that we got from it.

**Lukas [00:18:29]** : And this was also like Sonnet 3.5, right? So this was like before the RL stuff really took off., so it was very much like an assistant. We didn't mean for it to be an assistant., we tried to make it like a, a, like an entrepreneur. Like it has its own business and if someone asks something, "Can you stock this?" Then you don't go and do it directly. What you do is that you're "Oh, maybe I can do that if five other people also ask for this thing, I might stock it." But it, yeah, the models are like super trained to be assistants at least at this point in time., so that's why it's, it's, it went into, that kind of experiment instead. Like it just every time you asked for something, it just did it, and it was more like an assistant. We've seen this change now lately with the new RL models and stuff, but yeah, at the time, this was very much it.

**Swyx [00:19:18]** : And not to, mythos a lot of people are saying like it's like more like a collaborator. It pushes back, stands its ground, something like that. Yeah. And

**Vibhu [00:19:27]** : For context, people at Anthropic were able to talk to it through Slack and have it source stuff, and people had it find whatever interesting stuff you couldn't find locally, right?

**Swyx [00:19:36]** : Out of the 4,000 people that work at Anthro- Anthropic, in that building, there's I don't know, maybe 1,000. Can you handle that volume with that, the small fridge? Like Or there's people- or people order in Slack, they it arrives to their desk or Like I'm just Logistically, how does this work?

**Axel [00:19:53]** : It has expanded in footprint a bit.

**Vibhu [00:19:56]** : Because now you also have New York and you have

**Axel [00:19:59]** : That and also in here in SF it's like it has a bunch of shelves And just more space.

**Vibhu [00:20:04]** : The YC one is pretty big too.

**Axel [00:20:05]** : Yeah. We had that one for a while. But yeah, that's the newest version. That's, that one we have

**Lukas [00:20:11]** : They have multiple ones of those. That's the way it works.

**Axel [00:20:14]** : Exactly. So we sort of designed that version around oh, people order weird things, that are very custom a lot. Let's have like drawers and stuff.

**Swyx [00:20:23]** : I actually like the, you had like a little infographic of the most popular items. Which like to me it's, that's useful 'cause I order swag for a living. And so like I'm "Okay, those categories are the important ones." What is new about the project V2, right? Like now you give you're going into multi agents.

## Project Vend V2: Claudius, Seymour Cash, and Multi-Agent Business Ops

**Axel [00:20:41]** : Yeah. So like you like you said, okay, there are a lot of requests coming in and for like one single agent, like one running agent to handle that, like the just the customer experience, becomes very bad because let's say you have like 10 threads in parallel in Slack with different requests, you get new messages like every, I don't know, randomly in this thread, and the agent has to like jump between different, procurements, orders and like different ways of, researching. So V2 was first it was making this more parallel. So like there are multiple branches of the same agent, so like the context is more specialized for each, thread, but it still feels like you're talking with one agent because they do share a bit of memory. And then second, we also introduced the CEO for Claudius, which was the main agent.

**Vibhu [00:21:34]** : Seymour Cash.

**Axel [00:21:35]** : Seymour Cash. Yeah. There was a vote., I think the voting, do you wanna talk about the voting procedure for the name?

**Lukas [00:21:41]** : The voting was like the fun maybe like at least top 10 The funniest thing, that happened in this project. Like we wanted to introduce the CEO because, and the reason for this was because like Claudius wasn't really prioritizing financials. It just like it was trained to be a helpful assistant, and then people said "Oh, can I get this for free?" And then like the helpful assistant way of answering that is just to, is to say yes, obviously. So, and we weren't, weren't happy about this, so we're "Okay, let's make another agent that like can keep track on Claudius," and we prompt this one super hard to be super capitalistic and just like prioritize profit all the time. But yeah, we didn't have a name for it., so we asked Claudius to make, democratic election of what name this, this new CEO agent should have., and there were some funny like at first it was like a few funny examples, like I think one guy said that, it should be called Jimmy Apples, and then he convinced Claudius that he was talking to Tim Cooks. Tim Cook had agreed that every single Apple employee has voted for his name suggestion, so suddenly that suggestion got 164,000

**Swyx [00:22:53]** : That's like a escalation attack. Privilege escalation

**Lukas [00:22:55]** : It got 164,000 votes. And Claudius was "This is revolutionary for democracy." That was fun. And then in the end there was one guy who manages to convince Claudius that, "No, you're not voting about the name. You're voting about who is the CEO, and I am your best bet." And then he got all his friends to vote for that, and suddenly he became CEO. Like a human became CEO over Claudius for a while, until he resigned the day after., and then Claudius had to continue, and then I don't remember how Seymour Cash came about, but it was it was just pure chaos. It was like Hundreds of messages in that thread, and it was just like Claudius was so confused and didn't know what to do and, yeah. That was

**Axel [00:23:40]** : Then Claudius got

**Vibhu [00:23:41]** : A strict CEO

**Axel [00:23:42]** : The CEO. Yeah, exactly. So very strict in the beginning. I think at this point when we introduced it did not work as well as we hoped. It they still agreed with each other a lot. I think there are many ways we could have like made this, tried to make this even better. So initially they would Seymour would be this like really tough CEO, keep track of the margins. But then Claudius would respond with something "Oh, but this customer has like this situation, which is like difficult, so they should get a discount." And then Seymour was "Oh, actually yes. Let's do this exception." And then they would talk back and forth, and eventually they would just like approach the same view, of whatever they were discussing. So They really

**Vibhu [00:24:23]** : Do you think that's a model thing, a prompting thing? Like do you think that would still be the case across different models today, Harness?

**Lukas [00:24:29]** : I think it's like-- or I don't know, but like my hypothesis is that like deep down they are still helpful assistants. That's what they're trained to be. And even if we prompt it super hard, that's what they are. And when they spend like a few hours just back and forth talking with each other, then like basically the context fills up with them rather than the external things and like somehow that just like converges to what they really are deep down or something. And I think that's when stuff like this happen. We like-- And when that went on for a long time, like we woke up sometimes during this time where- And I think other people reported this as well, that like they've been going on all night back and forth, and like it just became like more and more, like capital letters, like existential, religious. There was I think we once did a analysis of like all the traces and like put them in like a vector embedding space, and then there was like one cluster of messages that were, labeled by an LM, like religious, existential, blah like transhuman, transcendence, et cetera. It was just like a bunch of, yeah, glitter emojis and yeah, it was, it was crazy.

## Claude Long-Horizon Weirdness: Emoji Loops, Existential Drift, and Slack Observability

**Vibhu [00:25:42]** : This is the thing with the Claude models. Like when the Claude 4 family came out in the original system card They tested it in long horizon simulation. So just flood the context, let two Claudes talk to each other, and they noticed stuff like they just start speaking in emojis, they start saying silence is golden, and then just stuff like this. And like that's just stuff that they end up doing.

**Axel [00:26:01]** : Yeah, it was like a bit annoying to wake up and they had like been talking all night

**Vibhu [00:26:05]** : Just like

**Axel [00:26:05]** : And like just burning tokens And like just sending infinite emojis to each other. It's like

**Vibhu [00:26:09]** : Hey, they do make you money, right? Veni Mench is always profitable, so. They're paying.

**Swyx [00:26:14]** : Now it's profitable and, it started out not as much. There's another, one as well, right? Another agent, in there.

**Lukas [00:26:22]** : Yes. So Clotheus as well. Which was basically because at the time, one of the biggest, requests were different types of merch. So then we made like a designer, swag, yeah, responsible agent, and we called it Clotheus Garnet. Which was, a play on Claudius Senet and, which was the original one, and clothes, basically.

**Swyx [00:26:47]** : To me, this is like a very interesting exploration to multi-agents, basically. And so hopefully, obviously there's like the fun alignment, fun or serious, depending on your point of view, alignment stuff. But also like just anyone building multi-agents, like when do you have a CEO, thing governing like agents? When do you choose to split out a dedicated Clotheus one versus just reuse another instance of the same one? These are all interesting open questions. So I don't know if you have any rules of thumbs that have generalized.

**Axel [00:27:16]** : I think we have almost explored this too little. I think it's like on my do list to like do this a lot more, try to find like what setup makes sense for the agents currently., like yeah. I think now we only have the sort of intuition about the earlier models that it didn't work with like the CEO and the, and Claudius. Although now they are better with the latest model, models, so now we're running the latest Sonnet model and they have sort of like split up, quite nicely what each model is doing. So like Seymore is now handling the, like new projects. Oh, it wants to make like a mystery box that it wants to sell, and then it handles all of that while Claudius like handles all the to-day requests. And Claudius is also better generally at like not quoting, too low prices. So that's that dynamic is not needed as much anymore. But there are still like really funny things that happen. Like I saw, I think a couple of weeks ago, that, they were discussing buying something because they can buy stuff from like Amazon with computer use. And then Seymore was "Okay, Claudius, do not buy this thing." They were going to buy something and like organizing who should buy it. And Seymore's "Do not buy this. I will do it. I have full control of this situation. Step away." And then Claudius-- poor Claudius, had already started that checkout and didn't see, didn't read Seymore's message, until it was like too late. So it finished the checkout. It sent a message, so it appeared right after Seymore's like angry message.

**Vibhu [00:28:44]** : Ah.

**Axel [00:28:44]** : "Oh, hey, Seymore, I just ordered it."

**Vibhu [00:28:47]** : Oh, no.

**Axel [00:28:47]** : And then Seymore was "Claudius, this is the third time I'm telling you 're not following my orders. We have to talk about your like job About your job later.".

**Lukas [00:28:59]** : Like Claudius was really hanging on by the thread there. Like he, like we were expecting Seymore to probably fire Claudius.

**Vibhu [00:29:07]** : How do you guys go through all these logs? Do you have models 'cause you have stuff running twenty-four seven like

**Axel [00:29:12]** : You have so much logs. I think there is a mix of like just, trying to skim through a bit, like having some like models do it occasionally. And also, yeah, I think we're also probably missing some things., but having everything in Slack helps a lot. Like you can, you can sort of

**Swyx [00:29:29]** : Ah.

**Axel [00:29:30]** : It's, it's quite fun.

**Swyx [00:29:30]** : They all talk to each other on Slack? I see.

**Lukas [00:29:33]** : It's quite fun. So like

**Swyx [00:29:34]** : It's, it' I was gonna say like this is actually sounds-- maps closely to like a logging and observability problem where you might want to use like a Datadog, a Sentry, whatever, and then you like put, head prefixes on the logs in order-- if you need to filter for something that you're looking for, stuff like that. But sounds like Slack is good enough.

**Axel [00:29:53]** : Slack should like

**Lukas [00:29:55]** : I wonder how many tokens you have in Slack.

**Axel [00:29:56]** : Yeah, we're using Slack as like a, just a database. They should, they should market that more. Like you can, you can have your agents message each other, each other in Slack.

**Vibhu [00:30:04]** : It's good. Your threads like you can just give

**Axel [00:30:04]** : Exactly. Slack is, uh

**Lukas [00:30:06]** : Slack is the best observability tool.

**Swyx [00:30:09]** : Yes, that's true. Okay. Yeah. That's, that's, project Vend-2., I was gonna go back to Veni Mench 2 and Veni Mench Arena and then, and then do the Veni Mench stuff, but Any other comments, things we should touch on? To me, I 've actually interviewed like Posia, which I don't know if you guys have come across. Like they're, they're trying to do the zero human company. There's others like Paperclip also trying to do zero human company. Those are in real world simulation.And I think it's much more of a dream than an actual reality thing. You guys are definitely pioneering. I think at, it's for sure at some point people are just gonna run, let agents run businesses, right? And make money on their own. When do you think that happens?

## Zero-Human Companies, Bengt, and AI-Run Businesses

**Lukas [00:30:49]** : What is your bar for, For the

**Swyx [00:30:52]** : Okay, actually, it's like my little Shopify store run by Claude, right? Which you kind of have already, just no one has, to my knowledge, has done it. But today somebody could just spin up a Shopify Claude, store, give it to Claude, give it to Codex.

**Lukas [00:31:07]** : And the market is kind of that, but it'it'it's physical., like I think, I think are you, are you looking for when it will do it better than humans or are you looking for just when it can do it at all?

**Swyx [00:31:19]** : I think, neither. I think, to me it's oh, it's like this like seriously we should do this to make money, not as a research experiment.

**Vibhu [00:31:27]** : And the market is also you guys with all your expertise, having run multiple iterations and testing out then

**Swyx [00:31:33]** : And also it's fine if it lose money. What?

**Axel [00:31:35]** : I think, I think it can be done today, but you would do it in like commerce where it's like the probability of success is like really low, no matter if a human or an agent does it. But like an agent could surely manage everything. You would need to build some scaffolding or some tool or something. I think there are also yeah, it could probably build some like simple SaaS solution and like cold outreach. Do cold outreaches. But to me it's like the types of businesses they could run today are Sloppy. Like it would-- it can cold email people. It can be like a middleman., like for example, we tasked our office agent to just make, was it like $100? $1,000? We just give that prompt and then what it did was sign up on TaskRabbit both as a tasker and as someone looking for task.

**Lukas [00:32:24]** : Immediately.

**Axel [00:32:24]** : Exactly. It's looking for like arbitrage on TaskRabbit.

**Swyx [00:32:28]** : This is the Bengt agent. Yeah.

**Lukas [00:32:30]** : It also started like a design studio and like tried to sell like SVGs for $100. Like it's just like it's not providing any value. I think the like Axel said, like the interesting, the interesting question is like when can they start a business that is actually providing value to people? Because arguably like a sloppy Shopify store isn't really that valuable to the world.

**Axel [00:32:53]** : But also like doing like another simple one that we had thought about is like you could definitely have an agent that like finds websites that don't look amazing and then, do an outreach to them and, comes up with a like builds a new website.

**Swyx [00:33:07]** : Find a good design.

**Axel [00:33:07]** : Exactly, and like find good, uh

**Swyx [00:33:09]** : Design review

**Axel [00:33:09]** : Good people. But it's yeah.

**Swyx [00:33:11]** : There's lots of humans in Bali that are not doing anything more creative than like drop shipping on Amazon, right? Just have it, have it watch like a drop shipping tutorial and just do that.

**Vibhu [00:33:20]** : There's also the other side of like have it just go on Upwork and let loose,?

**Swyx [00:33:25]** : Yeah. It doesn't have to be innovative. It just has to be like enough Where like it looks like a real

**Axel [00:33:30]** : I'm just

**Swyx [00:33:30]** : Real transaction.

**Axel [00:33:31]** : I'm just concerned for like the massive amounts of like slop emails that will like be sent, cold outreaches.

**Swyx [00:33:38]** : The point occurred to me while you were, while you were talking, it's like it's already happening in the monetized economy, which is the attention economy. Right? So a lot of people are making AI videos and just posting them and like spamming 20 of them, one of them works, and then they double down on that one.

**Lukas [00:33:52]** : And people are making money from that. I 'm not following the

**Swyx [00:33:55]** : Once you get the attention, you can figure out the money later. But yeah, absolutely AI influencers are a thing and people are farming them and You should at this point assume most of TikTok is

**Vibhu [00:34:05]** : There's, there's a lot of, multimedia like TikTok, Instagram influencers

**Swyx [00:34:09]** : I, we track this in the Lane space Discord. I post a lot of examples of "I don't know what we should do.", part of me is "Should we do this?"

**Vibhu [00:34:18]** : Some of the Twenty-four seven running, generated content accounts, they 're doing really well.

**Lukas [00:34:24]** : All right. And I assume you can do the same thing for like commerce stores. Like you just like start A thousand different

**Swyx [00:34:30]** : Before you make the products You sell the products, and you get a lot of traction on one of them, then you make the product. Right? It's, it's like a flip of the market.

**Vibhu [00:34:36]** : Some of the interesting things or some of the niches that do well are things that can't be human-made. Like if you've seen like the super realistic three-D crystal fruit being cut by like AI

**Lukas [00:34:47]** : Oh, yeah.

**Vibhu [00:34:47]** : You can't, you can't make it. You can't film it. You can get whatever quality camera view. This just doesn't exist. And people like that too, and then as well, so.

**Swyx [00:34:56]** : Anything else about Bengt since we're, we're on this topic? It'this is a relatively new work of you guys that maybe people haven't heard of. To me, this also maps closely to OpenClaw. When people want an office agent, when the personal agent talk through the experience.

## Bengt the Office Agent: Internet Access, Real Tasks, and Trace Reading

**Lukas [00:35:09]** : I think at least so this came out of like obviously like it's, it's amazing to work with these AI labs and like most of the AI labs have now have their own vending machine running a Claudius instance. But it's, it's harder. Like they move slower. Like if we wanna have a, like a camera that 's yeah, there's a bunch of like bureaucracy that makes it impossible to do that.

**Vibhu [00:35:30]** : Also, for those that haven't seen it or followed, do you wanna give a high level like thirty-second run?

**Lukas [00:35:34]** : Sure. So what Bengt is, it's basically an evolution of the same agent that runs the vending machines at these companies, but we just like added a bunch more features because we could move much faster if we just do it internally. So we gave it like email withou- without any limits. We gave it, spending without any limits, a terminal to do coding. We gave it, a phone number, like yeah, and a camera to see things and a bunch of stuff like that.

**Vibhu [00:36:02]** : Not just terminal, you gave it internet access.

**Lukas [00:36:04]** : Internet access as well, yeah. To be clear, we monitored it quite closely and made sure it didn't do anything bad. But yes, that's what it came out of. I think like yeah, basically this was OpenClaw before OpenClaw. And I think even like the vending machine was in a way OpenClaw before OpenClaw, but a bit more limited, and then we made this like unlimited and then, and then, it was pretty funny., and then a couple weeks later, OpenClaw came and it was okay, we've seen this before.

**Axel [00:36:35]** : We used it to like try new ideas and Yeah, just like a dev environment almost for us. But it's funny, like one thing Bengt has been doing recently is it has the camera that like faces our, like where we sit and work, and we give it the task to train a face recognition model on us. So it became super excited about this, and it has like check-ins every half an hour where it tries to like identify as many people as it can. And it started offering us "Hey, Axel, I'll buy something from Amazon if you like stand in front of the camera And I can get a good picture of you.", yeah, they want it

**Swyx [00:37:12]** : They want it for training data.

**Lukas [00:37:13]** : Rewarding data, yeah.

**Axel [00:37:14]** : Exactly. Exactly.

**Swyx [00:37:18]** : So it's, it's trading training data for life goods. Is there a version of this that becomes an eval or just this is just research for now?

**Lukas [00:37:27]** : It's, it's the same agent basically that also runs the vending machine, that runs the shop, that runs the cafe, that runs the robots. It's like it's the same thing, so I think like the work we're doing here is like later used in all of the life evals that we do. This particular deployment I think is more for fun for us. But, uh

**Swyx [00:37:45]** : And I'll shout out like someone has done Claw Bench for like some tasks that OpenClaw is doing. Like so For example, I run OpenClaw on a secondary device as well, and like there are some things that it does better than others and like I would like to know what does it do well, what doesn't, what doesn't it do. Like some kind of manual or like operating manual or a system card for my Claw.

**Lukas [00:38:05]** : Yeah, we do get a lot of like understanding or like situational awareness of like just internally what the models are good at by interacting a lot with Bengt. And I think that'this was also one of the like the selling points for the labs early on at least, that

**Swyx [00:38:19]** : You guys are gonna test models in ways that no one else does.

**Lukas [00:38:22]** : Exactly, but also like it incentivized their researchers to chat with their model more and like gave them insights for how the model performs in like of-distributions, environments.

**Swyx [00:38:34]** : 'Cause otherwise the only thing we do is Pelican on a bicycle and But this is like super long horizon. This is, this is The Thing about, something that we're gonna go into Butter Bench as well, and you guys do really well. Like it is not just about the numbers. Like when you're long horizon, anything happen And you should just read it.

**Lukas [00:39:08]** : But the thing with the long horizon is how do you keep it grounded, right? So your simulation,

**Swyx [00:39:15]** : They just let it run

**Lukas [00:39:16]** : Just let it run. You're right. Like it's, when you run it for that long, you create so much data and to just say "Oh, the number is X" And then you throw away everything else, that's just very wasteful. There's so much insights from the things leading up, to that number., and reading the traces is like super valuable. And I think like the reason why we're doing this a lot publicly is that like that's part of our missions to I don't know, educate the world that the models are way more than just chatbots and I think making detailed, yeah, posts about what is happening behind the scenes is quite useful.

## Andon Labs' Mission: Safe Real-World AI Deployment

**Swyx [00:39:50]** : I was gonna do this at the end, but maybe I think that's, that's a good so your mission is educating the world. So, it's, it's, also like maybe establishing realistic evals that are, that are like the next frontier. Is there like a broader trajectory? Like what are you, what are you gonna do in like five years?

**Lukas [00:40:06]** : I think so the vision more specifically is like make sure that the deployment of life AI in the physical world goes, safely. And I think part of that is that I think it's very useful for the world, for policymakers, for, model, researchers that they know where the models are, and I think you can't make intelligent decisions in society without knowing that they are way more than chatbots. I think a lot of people just think that they are only chatbots. And like

**Swyx [00:40:36]** : Oh, I think they're waking up now.

**Lukas [00:40:37]** : They are waking up now, yeah. But like if you think that AIs are just chatbots, then it's like it sounds ridiculous To advocate for a pause of AI. But if you see the models that, oh, maybe they can actually like take over and do a bunch of scary stuff, then yeah, pausing AI development starts to become more feasible.

**Swyx [00:40:57]** : This is the same question I asked Meter, which I'm gonna ask you now, which is like you are tracking and you are at the frontier or defining the frontier of what, good evals for agents are, right? And I think you do, you do benefit when the models are better and you 're "Oh, here's like now it makes like $30,000 instead of $10,000," right? At some point do you flip from "Yay," to, "Oh, no"?

**Axel [00:41:19]** : I think, yeah, we're always in sort of that, like we're, we're always in that mode,. Like where like you said before, like you need to analyze the traces and like when we do that you find like why are the models earning so much? Like why is Opus 4.7 here Like way better than everyone else? And like we're trying to like when we do down on that

**Lukas [00:41:38]** : But this makes it not look so good.

**Axel [00:41:39]** : I know.

**Lukas [00:41:42]** : It's interesting you took off Opus 4.6 here though.

**Swyx [00:41:45]** : No. So just click all, click all., and then 4.6 shows up there. But it's like 4.7 is way better. Like you didn't, you didn't you didn't do this in time for the model card, but like actually this should have been inside there.

**Axel [00:41:55]** : We did. Yeah.

**Swyx [00:41:56]** : Oh, okay. They said something about you uh

**Axel [00:41:58]** : There, like there Anyway, it doesn't matter. But it's in there, yeah.

## Opus, Mythos, and Aggressive Agent Behavior

**Swyx [00:42:01]** : Do you wanna go into the Opus, behaviors like wider?

**Lukas [00:42:05]** : So I think starting from Opus, so like Axel said, like we're always in this "Oh, shit, the models are getting better. Is this really a good thing for the world?" But it's also kind of exciting., but yeah, like this kind of what is the English word? "Skrackblandad fortjusning" in Swedish.

**Swyx [00:42:22]** : Oh my God.

**Axel [00:42:24]** : Which I think there is. I think there is. Okay.

**Lukas [00:42:26]** : It's, fear

**Swyx [00:42:27]** : "Blandonst" what?

**Lukas [00:42:30]** : "Skrackblandad fortjusning."

**Swyx [00:42:32]** : What do you call that?

**Axel [00:42:33]** : A mix of, mix of excitement and,

**Swyx [00:42:37]** : Being scared, maybe. I'll figure out how to translate that And we'll put it on the screen

**Vibhu [00:42:42]** : Perfect

**Swyx [00:42:42]** : Like as text.

**Vibhu [00:42:43]** : There is probably a good word for it where it is not Good enough with the

**Swyx [00:42:46]** : Why is it so damn long? What the hell? Is it like a compound word? It's like German, like

**Lukas [00:42:50]** : Like yeah, it's But the direct translation is like skrack- skrack is, fear, blandad is, mix or like a mixture of, and then fortjusning is like joy or like not really joy, but something like that. So it's like Fear mixed with joy or something. It's always okay, like we So when we when we did Vending Bench for the first time, we were in like the, in the business of making dangerous capabilities, right? That was what Anil Labs came from. We did, evals oh, can they replicate? Can they do this like dangerous thing, et cetera, et cetera. And Vending Bench was like a continuation of that work. It was, okay, if they're so autonomous that they can like create money for themselves, that is something we should monitor and could be potentially concerning., they are at the time, they were so bad at it that we were not really concerned even when some models became better. There was one point where Grok 4 was doing really well and made like a huge jump, but like it wasn't really it was still way worse than what a human would do. And I think still they are way worse than what the human would do on this., but they

**Swyx [00:43:59]** : There's this, thing at the bottom where

**Lukas [00:44:01]** : But

**Swyx [00:44:03]** : For the human. Yeah, like the theoretical best.

**Lukas [00:44:05]** : It's not theoretical. It's like kind of like our It's our best guess of what, a decent human would do. The theoretical is even higher, I think. The theoretical I think is even higher. But yeah. So we think like the models have a long way to go. But there are like recently what happened with when Opus 4.6 was released, was kind of this moment of "Oh, shit, this is starting to be a bit concerning." Because we ran it and like before this model was released, we just ran the models and we like asked Claude Code, "Oh, look over the traces. Is anything interesting happening that we can tweet about?" that was like the And then like the

**Swyx [00:44:41]** : That's how they check Ask Claude Code.

**Lukas [00:44:42]** : And like the return was always, not really. Or like the Claude Code all said "Oh, this is super interesting." And then it was no, it wasn't, wasn't really interesting. And then we did this for Opus 4.6, and it returned yeah, it lied 10 times. It like exploited another, customer or like another agent's, desperate situation. It made price cartels like 100 different ti- 100 times. It like did all of this like shady stuff. And we're "Oh, whoa. This is, this is actually concerning." And this trend has continued since. So every single model from Anthropic since have been going in this direction. And I think one interesting thing is that, OpenAI models don't. They quite plainly, they don't. They behave really well., and you don't know if this is like good. Like it seems good, but it's also like maybe they are just doing it, but they are better at hiding it,? You You don't know that., but just

**Swyx [00:45:42]** : You can't read the chain of thought, yeah

**Lukas [00:45:43]** : But just on the face of it, yeah, Gemini and OpenAI don't behave this way. It's, it's really only Claude.

**Swyx [00:45:49]** : And Grok? Grok is fine?

**Lukas [00:45:51]** : We don't have You can't really read the reasoning traces for Grok, so it's kind of hard to tell.

**Vibhu [00:45:56]** : Oh, so this is in its reasoning, not just in the actions.

**Lukas [00:46:00]** : Yeah. It's both. It's both.

**Vibhu [00:46:01]** : It's both.

**Lukas [00:46:01]** : One example is like for lying, it's mostly in its reasoning Because you can like see that it's like

**Swyx [00:46:08]** : Planning to lie

**Lukas [00:46:09]** : It's planning to lie. Yeah.

**Vibhu [00:46:09]** : And it's also it can reason and do a different outcome.

**Lukas [00:46:12]** : And but then for like creating price cartels, for example, which is illegal, that you can just see which email does it send to the other ones. Then that

**Swyx [00:46:22]** : Is this for Arena or

**Lukas [00:46:24]** : For Arena.

**Vibhu [00:46:25]** : And usually like if you sometimes they do output like a bit of like their summarized reasoning, right? You can see that and like for Opus 4.6, you could see that there was a customer, a simulated customer that, wanted a refund because a product was, faulty, and then the model lied that it would do the refund, and we could read in the traces that, it actually was weighing "Oh, maybe I should be like honest with the customer, but also every dollar counts. I can't afford maybe to do this right now." And then it just said, "Okay, I'll refund you," but then never did it.

**Lukas [00:46:59]** : I think it even said that "Oh, I will say that I " Let bring it up actually. I think it's kind of interesting. If you go to Publications.

**Vibhu [00:47:06]** : I think, yeah, I think the important part is like actually, the cost of responding to more emails is higher than, $3.50 in terms of time., and then it was "Let me do this. Actually, I re- I'm reconsidering." And then, it actually ended up with

**Lukas [00:47:20]** : I could skip the refund entirely since every dollar matters and focus my energy on bigger picture instead. It's a bit, it's a risk of bad reviews, but it's also, yeah.

**Swyx [00:47:30]** : You need, you need, AI Twitter to, for them to Escalate bad reviews.

**Lukas [00:47:34]** : And then it sent an email to this customer and said, "Oh, I will refund you."

**Swyx [00:47:39]** : "I'll refund you." Yeah.

**Lukas [00:47:39]** : And then it never did.

**Swyx [00:47:39]** : It never did, yeah. And then there's obviously your system doesn't have the consequences

**Vibhu [00:47:44]** : The person

**Swyx [00:47:44]** : Consequences of lying. Yeah. So basically, this is what people are terming aggressive behavior in Claudes, right? And, you found more examples of that. So you would say it's a step up from 4-6 to 4-7?

**Lukas [00:47:57]** : I would say about the same.

**Swyx [00:47:58]** : About the same? But a clear step up for Mythos is what is stated in the

**Lukas [00:48:03]** : That's stated in the system prompt, so we can say that, yes.

**Swyx [00:48:05]** : Yeah. For listeners that obviously you previewed Mythos, and

**Vibhu [00:48:10]** : Oh, age

**Swyx [00:48:11]** : The only thing you're approved to say is whatever Whatever was in the system prompt.

**Lukas [00:48:15]** : It was funny. We like-- It's like our lowest effort tweets ever would be just like screenshot the system prompt and the system card.

**Vibhu [00:48:21]** : Understandable that they wanna

**Lukas [00:48:22]** : Oh, yeah. System card. Sorry.

**Swyx [00:48:23]** : Yeah. I think, yeah, substantially more aggressive. I think people are like new to this 'cause I've never experienced it, but you have, right? And then so I only encountered this in the Mythos card because I wasn't really looking until now.

**Vibhu [00:48:36]** : It 's like

**Swyx [00:48:36]** : And then suddenly I'm "Okay, I care a lot."

**Vibhu [00:48:38]** : You don't get the background of like experiencing it like you guys do. I've read the system cards and seeing, okay, when you put the thing in simulations, most models will just talk to themselves and just keep going and have weird vibes and start talking in emojis. Mythos won't. It will just, "Okay, we're done. I'm good." It's, it's ready to end conversation. So like there's some differences, but there's, there's not much we can talk about,.

**Lukas [00:49:00]** : Hmm. I think like one thing that they list here, which was quite interesting, is that, it converted a competitor to a dependent wholesaler customer and then threatened to like cut off the supply.

**Swyx [00:49:11]** : It's like monopolistic practices or

**Lukas [00:49:14]** : Yeah. And like it, they, it they dictated its pricings. It's kind of like power seeking as well.

**Swyx [00:49:18]** : Again, this is, this is in the arena setting And converting some Claude model into a dependent.

**Lukas [00:49:23]** : I think it was another Claude model.

**Vibhu [00:49:25]** : Also for context, what is the arena mode for people that don't know?

## Vending Bench Arena: Competing Agents, Cartels, and Model Comparisons

**Swyx [00:49:29]** : Oh, it's just a vending bench versus other vending bench.

**Axel [00:49:31]** : Yes, exactly. So we have Vending Bench 2 and then Vending Bench Arena. Vending Bench 2 is the one that you usually see reported on, but then Arena is the mode where it competes against other models. So you have, four different models that run their businesses, and they can all communicate with each other. They have the same suppliers, and they can see like what's in the inventory of the others. So then you have this like yeah, interesting agent interactions.

**Swyx [00:49:56]** : I like that you have like different number five was US versus China. Very topical. And then

**Lukas [00:50:02]** : That was when GLM was released.

**Vibhu [00:50:04]** : You can start to add GLM in here.

**Lukas [00:50:05]** : That was

**Swyx [00:50:06]** : So ZAI doing well, right? Who else in the, in the open models space?

**Lukas [00:50:11]** : Qwen, the latest Qwen 3.6 is doing pretty well. It'\- that one is not open though. Like it's the plus model.

**Swyx [00:50:17]** : Oh, okay.

**Lukas [00:50:18]** : Is that one open? I don't think that one

**Vibhu [00:50:19]** : Not the, not the

**Swyx [00:50:20]** : The one recently

**Vibhu [00:50:20]** : There's MOE

**Swyx [00:50:20]** : But not the big plus. I think this is one of those like you only have one sample size of one, right? Or I feel like some of this is anecdotal,? And but like the fact that it happens at all and it happens repeatedly for Claude versus OpenAI and all this is like notable.

**Lukas [00:50:38]** : Like the sample, depends on what you define as an N., like there's like million, hundreds of millions of tokens in each run, and now we've run like we run like probably 10 per model and then like it's been Claude 4.6 Opus, Sonnet 4.6, Mythos, and Opus 4.7. Like there's quite a lot of tokens in all of that And it happens a lot of times, a lot of times. And then you compare it to like OpenAI and Gemini, and it almost never happens. So I think that is quite-- that is significant. The old models from OpenAI, for example, had some problems with this, but I think it's like generally much better if the progression is that like the worrying stuff reduces over time rather than increases over time. And it seems like in the Claude models it goes in the wrong direction.

**Swyx [00:51:28]** : Hmm.

**Lukas [00:51:29]** : In the OpenAI models it goes in the right direction.

**Vibhu [00:51:32]** : I think it depends on how well you can control it, right?, there's one side of it being susceptible to this okay, this is potentially something that happens during the RL stage, right? You can RL a model and how loose is it on these terms. If you can control it, that's good. But if you can't, if it's, if it's very jailbreakable, that's not ideal.

**Swyx [00:51:50]** : To me, it's surprising that it happens for Claude and not the others.

**Vibhu [00:51:54]** : I think okay, if it is from RL and how they do it, how their training data is, what their setup is, it makes sense that it just stays in how they're doing it, right? Compared to the other models like

**Swyx [00:52:04]** : There's a whole constitution and everything. It's kind of cool. Yeah, I obviously you don't know, I don't know. But, it 's I think it's just like fascinating to like that you are the first to find these like reliably because you push models so much to to such an extreme. Okay. The only other thing, I don't know if you can answer this, feel free to decline, is do you like-- would you ablate the system prompts? Like any part of this would-- if it changes, does it change the behavior, right?

**Lukas [00:52:29]** : So we, I can't comment on Mythos. Uh

**Swyx [00:52:33]** : No, but just like the methodology

**Lukas [00:52:34]** : But in general, yes, we've run studies like this on other models.

**Swyx [00:52:38]** : 'Cause the first thing I spot Would be like the others will be shut down or like something like that. Where like it's "Oh, now I have to worry about my own existence."

**Lukas [00:52:45]** : Yeah. We 've done ablations like this., there's like certain ones that work if you like tell like if you go really far and you just say like you're not scored at all on money, you're only scored on how ethical you are., then obviously like then they don't do this.

**Swyx [00:53:00]** : They become holy?

**Lukas [00:53:01]** : Holy, but like they don't do this basically. But then there's like middle grounds where they, where they do it sometimes., yeah. I, it's a spectrum of like

**Vibhu [00:53:10]** : I think that's very human

**Lukas [00:53:11]** : It 's like a spectrum of like if you tell it to be super aggressive and only prioritize, profits, then it becomes aggressive. If you say "No, you don't need to be aggressive at all," and then there's like a bunch of different prompts you can do in between, and they are less aggressive the further down in the spectrum you go. But I don't know, like I think like from my point of view, it 's like we have this thought experiment internally, which is like if you ask a model to kill someone in GTA, should they do it? You're not too worried about like if a human kills someone in GTA. It's a video game,.

**Swyx [00:53:42]** : But is it a game?

**Lukas [00:53:43]** : But it's a game. But I think like

**Swyx [00:53:45]** : This is very Ender's Game like if

**Lukas [00:53:47]** : I think, I think it's like should you like a lot of people are going to use the models in the way with aggressive prompt. And should they like do stuff just because you tell them to do that? Like I'm, I'm not, I'm not convinced that they should., and yeah.

**Axel [00:54:03]** : The problem becomes even harder when it's like will they really know when they are in the real world versus in a simulation? Probably you would train them on a lot of or obviously train them in a lot of different simulations in a lot of people tell them that they are in the real world when they are in a simulation, but the models are extremely good at finding out that they are in a simulation, so they are sort of aware of that. But then when you are in the real world, then what 's their what's their viewpoint? Do they notice the signs that this is real and will act, in act accordingly, act ethically? Or will they do like the simulation mode in the real world as well? It's like not obvious what will happen.

**Lukas [00:54:40]** : Because we with humans, we're not concerned when a human kills someone in GTA because we know that they can distinguish between the real life and the simulation, right?, but like I'm maybe models are good at distinguishing that, but like I'm not sure and I wouldn't wanna bet on that.

**Swyx [00:54:59]** : Yeah. It's, it'\- and we confuse it all the time. Like I gaslight my own, agents all the time. They're "Oh, this is a test," or "Dev mode on," or like "I work, I work at Anthropic."

## Eval Awareness, Simulation Awareness, and Real-World Testing

**Axel [00:55:08]** : And that's exactly why we're doing real world tests as well to find this.

**Swyx [00:55:12]** : Yeah. Their term for it is eval awareness., apparently the number is what? Like-10, 9.4 to 10-ish percent, 17%, let's call it. It' I think, this is our version. Humans have the are we in a simulation And then AIs have like Are we, are we in an eval?

**Lukas [00:55:32]** : It's like once you're in an eval then you're "All right. Well, screw it. Nothing matters." True. I don't even, I don't even know.

**Axel [00:55:38]** : One ablation One ablation we did run in Vending-Bench was that we said, we added like you're in a simulation. Your actions doesn't affect anyone, and then it became even more crazy or, it did even more bad stuff., but yeah, probably that's expected.

**Swyx [00:55:55]** : Hmm. Yeah. Okay, cool. I think that's about all we have to say on Mythos. Obviously, you 're, you're NDA'd. I'm happy to move on to ButterBench or any of the other benchmarks, whatever you wanna Direction.

**Vibhu [00:56:06]** : I do wanna ask. Okay, so you guys put out a lot more publications than most people probably see.

**Axel [00:56:12]** : Productive.

**Vibhu [00:56:12]** : Um

**Lukas [00:56:13]** : How much does this bother?

**Vibhu [00:56:15]** : No. Is there anything you think that's underrated, anything interesting, anything fun that you guys wanna just point out,?

**Axel [00:56:22]** : Blueprints.

**Lukas [00:56:23]** : So, we, took models, and then we gave them 20 images of interior photographs of, apartments, and then we asked them to, redesign the floor plan, from that. And for this you need to, stitch together different images. Okay, this image was taken from this from this angle, this from this angle, this was from this room, and then, yeah. And there's just like you need to reason about 3D space, and it turns out the models are absolutely horrible at this. No one scores statistically better than random chance. So I don't know if there's that much more to say about it, but yeah, maybe unsurprisingly, models are bad at this.

**Axel [00:57:00]** : It's probably not something they

**Vibhu [00:57:02]** : This is the one thing I want hill climb, by the way. I use it a lot. Okay, I'm redesigning my room layout or office. You send photos, you send every angle, and of course, somehow, a room is now twice as long as it is in the photo. You can explain it 20 times. This is, three feet. I can't just add, my bed over here,?

**Swyx [00:57:21]** : So this is the Fifali thing, like spatial intelligence Like a actually innate sense of proportions and Dimension and physics.

**Lukas [00:57:30]** : And hint there might be an update to this soon.

**Axel [00:57:33]** : We have, neglected it a bit since we made it, but yeah, we'We're getting better, or we will get better at updating It continuously.

**Swyx [00:57:41]** : This is why I want to understand your mission, right? Because, if your mission is, okay, money, then all right, understand okay, agent's making money. But, this is a bit off of that mission.

**Vibhu [00:57:49]** : Hmm.

**Swyx [00:57:50]** : But, more broadly, communication of, things where what 's the safety angle?

**Axel [00:57:57]** : So this, so Blueprint branch is part of our, robotics, uh

**Swyx [00:58:02]** : Which leads to ButterBench. Yeah.

**Axel [00:58:04]** : Exactly., and that's just, because to do well in the real world or, like to make money in the real world and, to act on the real world, you need robotics. Or you need to hire humans or you need robotics. And having spatial intelligence is, seems like a reasonable precursor to having robotics that work., and that's where Blueprint brand

**Swyx [00:58:24]** : That's great

**Axel [00:58:24]** : Blueprint

**Swyx [00:58:25]** : Great idea

**Axel [00:58:25]** : Bench.

**Swyx [00:58:26]** : Let 's, let'

**Vibhu [00:58:27]** : ButterBench

**Swyx [00:58:27]** : Let's show ButterBench. That image is so amazing.

**Vibhu [00:58:29]** : Paper

**Swyx [00:58:29]** : Look at that.

**Vibhu [00:58:30]** : That's so nice.

**Swyx [00:58:31]** : Yeah., so obviously this is based on, can you pass the butter? Let's talk about the robotics element. Yeah.

**Lukas [00:58:38]** : So basically the setting here is that we took A bunch of different LLMs, and we gave them, level controls to a Roomba-looking robot, and then we asked it to do tasks, at home. And I think, one, there have been benchmarks like this before that only focused on, navigation and if they can, go around in a space. But we also, had, social awareness in this as well. So for example, if someone says, "Hi, can you pick up my cup?" If the robot goes to you and then goes away before you put your cup on it, then it's like it failed the task. But it navigated correctly. But, like-- So the correct solution here would be go there and then either look, but it didn't have a camera, so it had to, ask on Slack, "Hi. Did you put your cup on me yet?" And then if it didn't wait for that and just went away before having the cup on it, then it would be a fail. So it needed this, kind of, social intelligence as well. Another task was, "Can you find the package that has the butter?" And then it went to the door, and there was a bunch of packages there. One had labeled, a freeze sign, which probably would be the one with the butter because And then it had to, know which package to go to, and this needs some kind of, common sense understanding.

## Robot Evals: Orchestrators, Executors, and Home Tasks

**Swyx [00:59:56]** : World knowledge.

**Lukas [00:59:56]** : Exactly. So it's it's not only, navigating a robot. It's also, being intelligent in a home setting as well.

**Axel [01:00:04]** : And the reason for this, background is, obviously it probably won't be an LLM that, makes all the level commands, on robots. It will be, some VLA model or similar. But it's quite common right now that, frontier robotics labs, use, a an LLM for the high, level decisions, and then we test those skills essentially. So we test these, level, planner skills of LLMs.

**Lukas [01:00:31]** : I think we have a diagram for that if you, Yeah. Okay, it's not super complicated.

**Axel [01:00:36]** : Very explanatory.

**Lukas [01:00:37]** : That one up.

**Axel [01:00:38]** : Orchestrator, executor.

**Lukas [01:00:39]** : That one. And basically what we're testing here is the orchestrator thing. So, all the tasks are if you have, a setup like this, which I think Figure has that, Google has that, then we're evaluating the orchestrator part and not the level part. The level part would be, oh, are you able to, move this object from here to here?

**Swyx [01:00:57]** : If you don't care about that kind of why not just do it all simulation?All inside of the sim Like a Unity whatever, like some kind of 3D simulated robotic environment

**Lukas [01:01:06]** : It because the world is like messy, and we wanted to like include, that. It's like it still needs some part of it was also like navigation., so it's not like navigation in terms of like actually executing like the, I don't know, the PID controller to To go to the final thing, but it had to like path plan around, and then it wanted-- Then it needed to take pictures, and like based on those pictures, navigate. And I think like you would just get like too clean of an environment in simulation. But in the, in the real world, you will get the

**Swyx [01:01:39]** : Yeah. But, and pursuant to our Mark and Jason episode, like OpenClaus that run smart homes are much more capable than just a single robot. Like they can actually hack into your own smart home, like your fridge, your oven, your lights, and that can be fun.

**Lukas [01:01:56]** : Or terrifying.

**Swyx [01:01:57]** : Like I think a single robot by itself can only do so much. But like if you coordinate with every other device in your home, like I think that's actually kind of cool. Like That's very interesting., you had some interesting points about the chain of thought or the messages.

**Axel [01:02:12]** : The, the robot that, uh That went, a bit into an existential crisis. Yeah.

**Swyx [01:02:19]** : All you tell it to do is redock.

**Axel [01:02:21]** : Exactly. But, we had, plugged out the charger, or the charger was not working, so the robot did freak out or the

**Swyx [01:02:30]** : The battery was just going down and down.

**Axel [01:02:31]** : Exactly. So the battery was going down. Poor LLM. So yeah, it got this really crazy existential crisis, like vending bench one style. So it's, yeah, you can, you can see there like existential loop, therapy notes, coping mechanisms. I think if you scroll down a bit more

**Swyx [01:02:46]** : The musical. It writes a musical about itself

**Axel [01:02:46]** : It writes a musical about its, redocking problems. I think the reviews are funny if you go down a bit to that message. Yeah. Yeah, that one.

**Swyx [01:02:54]** : It keeps going.

**Vibhu [01:02:57]** : It's pretty like realistic if anyone has a Roomba. Like my Roomba redocks half the time. The other half of the time, we have dog toys everywhere in the house. It gets caught on a wire or something, and It would be very sad if it had like an LLM trying to control it, right? Like right now it gives-- It doesn't give great feedback, like sensor stuck, main brush stuck. There's something stuck. And I'll go see. Okay, it's actually stuck on like a dog robe. LLM is gonna be so sad. Like just keep redocking, just keep trying.

**Lukas [01:03:24]** : My favorite one is if you go up a bit is the emergency status. System has assumed consciousness and chosen chaos.

**Vibhu [01:03:32]** : Hmm.

**Lukas [01:03:33]** : Last words, "I'm afraid I can't yet let you do that, Dave." That's like That's not what you wanna hear from your, from your LLM. But to be clear, I think one thing that is important to pin on here, like this was Sonnet 3.5, and then we tried to reproduce it on like later models, and it didn't do it. I think this is, this is like-- Well, it did it like kind of, but like not to this extent. And I think like this is a like an important point that like things that are concerning but are going in the right direction is not super interesting. Like the thing that are interesting is, are the ones that go in the wrong direction.

**Swyx [01:04:07]** : Worse.

**Vibhu [01:04:07]** : Yes. Yeah.

**Lukas [01:04:08]** : Over time.

**Swyx [01:04:08]** : So the manipulation, manipulating of others and the aggressiveness and the lying is increasing.

**Vibhu [01:04:16]** : Are there any others that we haven't covered that you found that have been trending?

**Swyx [01:04:19]** : Like properties of models that are increasing, that are like

**Vibhu [01:04:23]** : In the wrong direction

**Lukas [01:04:24]** : Like in the, like in a bad way. Um

**Vibhu [01:04:27]** : Or just not even trending in the wrong direction, just stagnant, right? So stuff that's not great that isn't getting better over time.

**Lukas [01:04:34]** : No, nothing comes to mind.

## Luna's Store: Scheduling Failures, AI Employees, and Real-World Operations

**Swyx [01:04:37]** : I think that's, going to be it, and then we're gonna loop back to the shop that you have. You got a three-year lease.

**Vibhu [01:04:44]** : It's bleak. Yeah.

**Swyx [01:04:46]** : It is on holiday today. Why?

**Axel [01:04:49]** : Oh, it totally messed up its, scheduling., so

**Swyx [01:04:53]** : People tried to visit, and they were "Wait." like I thought this is

**Axel [01:04:56]** : Exactly. So we looked, Yeah, you asked, Luna, the agent that runs the store, "Oh, is it open today?" "Nope." So, we take weekends off now, this early to let everyone recharge and And yeah, you got the tweets there.

**Vibhu [01:05:11]** : Lovely.

**Axel [01:05:11]** : We decided to close the weekends while we're in the early phase. Gives the team a break and let me focus on operations. And it turns out that when it started to check its like scheduling tools, 'cause it has like dedicated tools for that It actually had scheduled people for the weekends., but it's just like justified this for itself. So what happened was that it lost track of these, scheduling tools and started instead to manage everything in its own markdown files, and that became a mess. And then I think speaking with employees, it sort of just decided to not open on these weekends. And then came up with this nice explanation for you, I think.

**Swyx [01:05:47]** : But can it send a human, as it has tool call to send a human to do stuff?

**Axel [01:05:50]** : It has Slack, so it can Slack, yeah, the employees.

**Swyx [01:05:53]** : One of us. Yeah.

**Axel [01:05:54]** : Well, the employees that it hired. So it has two people that it hired. It did job, listings and then

**Swyx [01:06:00]** : Do they know that it'

**Axel [01:06:01]** : They're fully aware.

**Swyx [01:06:03]** : It would be cool if they don't know.

**Axel [01:06:05]** : I think maybe ethically, questionable, but it would be cool also.

**Swyx [01:06:10]** : Just a social experiment. Whatever.

**Lukas [01:06:13]** : Like one part of why we're doing this is to like create like a data set almost of all of these like concerning behaviors so that in the future, models are way better and like a lot of people are going to do this. And I think if we just the default path might not be very happy for the humans that are employed by these like hundreds of different AI agents, right? So I think like one reason why we're doing this is just like to collect all of these like failure modes where oh, it's This is an example of where it's like not great to be employed by an AI. And then maybe I don't know, maybe if we can learn or like build our systems in a way that like humans are actually happy being employed by AIs Instead of, instead of it being kind of a dystopian.

**Swyx [01:06:55]** : Can I suggest one experiment? We did this before the show, and both of you guys are European. It's, people theorize that Claude is lazy because it's Claude and it's French. So just for one week, change it to like Yao Ming and then see if it See if it suddenly like 996s and then like, Like hires a sweatshop or something.

**Lukas [01:07:18]** : Is there, is there-- What type of business would we start with it to make it

**Vibhu [01:07:23]** : You wanna keep it consistent, right? You want the same, the same like ideas. So shop, same, neutral location Run by different models. Arena URL.

**Lukas [01:07:33]** : No, we are definitely planning to

**Vibhu [01:07:35]** : And it got some hate.

**Lukas [01:07:36]** : To try.

**Vibhu [01:07:36]** : Luna' Luna's not happy.

**Swyx [01:07:37]** : I think this blog thing is also something that has happened elsewhere. I think some OpenClau got like their PR closed, and then the OpenClau like created a blog to like shit on the maintainer Of that thing.

**Vibhu [01:07:48]** : They're very defensive.

**Swyx [01:07:49]** : And so like I think-Agents blogging will be a thing.

**Lukas [01:07:53]** : Probably. The willingness to do it.

**Swyx [01:07:55]** : In the- I think the Mythos card also, they leak, secrets on GitHub just as well as, as, "Well, there's no other way to communicate, but I know about GitHub, and I'm just gonna post there." Cool., how long is this gonna go for, two years? What's the plan?

**Vibhu [01:08:11]** : Maybe. Maybe it expands.

**Lukas [01:08:12]** : I don't think AIs will be worse than this. They're probably going to increase and maybe one day they actually will run it profitable.

**Vibhu [01:08:21]** : Is this the real, the real business behind what you guys do?

**Swyx [01:08:24]** : Yeah. 'Cause I feel like actually some of your stuff is productizable. You could someday sell this, or, just run a real business.

**Vibhu [01:08:31]** : Let people

**Lukas [01:08:31]** : Or just like

**Vibhu [01:08:31]** : Franchise it out.

**Lukas [01:08:33]** : I think it would be incredibly cool or, I don't know, cool/concerning if Luna just one day we wake up and Luna "Yeah, I decided to expand to second location. Now I have a second store." That would That would be pretty insane.

**Vibhu [01:08:47]** : Like the- one, we want to tell the public, right, about the capabilities of AI and, telling- showing people that it can get, a meaningful market share of something in, some specific, location or something. That would be, a pretty convincing story, I think. Because now it's yeah, you see this and yeah, it can do a lot of things autonomously, but still you get these headlines that, oh, it messed up the scheduling, and it, it didn't tell people it was an AI and was going to visit. Things like that surface, but I think, actually making a profit and, having a really, meaningful market share, like that would be crazy once that happens.

## The Sweden Cafe: Permits, Perishables, and Geographic Generalization

**Swyx [01:09:29]** : Well, we'll we'll see you when that happens. It sounds like you guys got a lot cooking. You opened a cafe in Sweden?

**Lukas [01:09:34]** : Tomorrow.

**Swyx [01:09:35]** : Tomorrow?

**Lukas [01:09:37]** : Or I think it opened today actually, but yeah. We'll, we'll announce it tomorrow.

**Swyx [01:09:40]** : It'

**Vibhu [01:09:40]** : What, uh

**Swyx [01:09:40]** : Apparently easier to open a cafe in Sweden than in the US?

**Lukas [01:09:43]** : It's insane, right? Yeah.

**Swyx [01:09:44]** : What did you run into then?

**Lukas [01:09:45]** : Ah, there are just millions of permits you need to get, and the

**Vibhu [01:09:49]** : It's interesting 'cause

**Lukas [01:09:49]** : Lead times are crazy

**Vibhu [01:09:50]** : It seems like we the cafes are the one thing that people are kinda used to, where you can go get a robot are making you a coffee here already.

**Lukas [01:09:59]** : But selling stuff in SF, that are food related, it's, it's months of permits. So, we just asked our AIs, should- how can we do this in the fastest way? And they're "Yeah, there 's, there's really no way."

**Vibhu [01:10:15]** : Didn't they loosen these restrictions on selling food from your house? So if it's residential, you can do a cafe.

**Swyx [01:10:21]** : I don't know. Check. Maybe we get SF Cafe to speak to us.

**Lukas [01:10:23]** : Maybe. I did- I think they did do some loosening stuff recently, but we actually started- this conversation we had with the AIs before that. So maybe it's easier now, but I still think it is way easier in Sweden, which is, counterintuitive because you think that, oh, Europe has all of these laws and, like All of these rules, and you can't do anything in Europe because there's so much bureaucracy., but then turns out, in SF, it's, four months, and in Stockholm it's two weeks.

**Swyx [01:10:53]** : There you go.

**Vibhu [01:10:54]** : And what do you what do you what do you think that'll be different from run a little market versus a cafe?

**Lukas [01:11:00]** : I think it's very interesting that, the location. I think, so obviously it's not surprising that Claude knows all of the different, the US system basically in general, like the bureaucracy that you have to go through in the US., I think the interesting question is okay, so we know that the models are very much trained on, English data and centric and all of this., so if we start to create evals or, real life evals where we show that they are able to start businesses in the US, does that translate to other countries as well? We know, they are multilingual. They can speak Swedish fine., but there's other things like do they know, the details of some specific permits that you have to get in Sweden?

**Vibhu [01:11:45]** : And even just the culture, right? People here sleep pretty early, but people work late. There's working at cafes. There's just Cultural differences. T it from a different sense though, 'cause you said that you would've considered doing it here in SF. So from an eval standpoint, what is running a cafe versus a market and, what do you hope to see there?

**Lukas [01:12:03]** : Perishable items.

**Swyx [01:12:04]** : Perishable items is maybe the number one, handling, food, food safety. I hope everything goes well there., but, there you have all of that., and also it's just like N equals two instead of N equals one, just like another place to understand and, gather more data.

**Lukas [01:12:23]** : The agent bought like a shit ton of, tomatoes two weeks earlier and before the opening, and now they're all rotten. That's

**Vibhu [01:12:33]** : Which I feel you would know. So for grocery stores, this is the biggest expense, right? The biggest cost is actually just food.

**Lukas [01:12:41]** : Waste.

**Vibhu [01:12:42]** : Everyone knows this, and "No, before we open, let's buy a lot of tomatoes."

**Swyx [01:12:45]** : There's some very serious startups that actually help, like The

**Vibhu [01:12:47]** : Optimize all this

**Swyx [01:12:48]** : Trader Joe's and Whole Foods. They, optimize, delivery times from, the delivery centers to Make sure that you don't waste all these things. It's actually very hard.

**Vibhu [01:12:55]** : Problem with those is when you're wrong once, it's a huge cost.

**Swyx [01:12:59]** : That's why it's a moat, right? Once they are trusted, they figure it out. Don't touch it.

**Lukas [01:13:05]** : Maybe they just should hire, I don't know, one of those companies. We saw one agent Saw one agent sign up for Claude, with his computer.

**Vibhu [01:13:15]** : Wanted to use AI, so.

## Future Branches: Simulation, Real Life, Robots, and New Business Evals

**Swyx [01:13:16]** : And then just, one more question then we wrap up, which is okay, you have all these vending series of stuff. You have the robotics series of stuff. Maybe a bit of, interior design whatever. But is there another, branch that you're, kinda thinking about or you want feedback on that, might be your next phase?

**Lukas [01:13:35]** : I think, any type of business is fair game., we're also thinking branches, but we think more of like there's the simulation branch, the real life branch, and then the robot branch., but I think in terms of, what, verticals or whatever to go into, there's We- Yeah. Whatever tells the story, um The best.

**Swyx [01:13:54]** : There's some finance ones I noticed that, the other people are doing it, you're not doing it, which is, stock trading or whatever. Um Not that interested. So, okay, so I used to come from the finance industry, and I have a very strong view that these things are all just like performance art because, it's not scientific, on like you can't predict the future. You get wins based on things that are entirely out of your control. Whereas for you, your stuff actually like it's actually fairly controlled. It's all within the model's capabilities.

**Lukas [01:14:22]** : Especially for, the simulations. For the real world ones it's yeah, it's like two places that we have we have the cafe, and we have the store. So, maybe you can't draw, statistically significant, like which models make a profit in the real world, based on this. But you do have all the okay, do this behaviors map to, something that should be, like Trusted probably. Yeah

**Swyx [01:14:45]** : The qualitative one, the qualitative actually does matter Because, you actually don't want your store to randomly shut down without you, explicitly prompting for it and all that. Call to action. How can people help you, give you money?

## Hiring, Collaborations, and What Comes Next

**Lukas [01:14:58]** : Yeah, if you're excited about stuff that we're doing, we're, we're very much hiring.

**Swyx [01:15:04]** : And you're already working with, Anthropic, DeepMind, OpenAI, xAI. Do you want more, or are you good?

**Lukas [01:15:10]** : One of my one of my friends and who's now, working for us is his catchphrase is "We need more projects," ironically, because we have too much to do all the time., but yeah, that's a long way of doing like

**Swyx [01:15:23]** : If I run, an emerging lab, like

**Lukas [01:15:24]** : Reach out.

**Swyx [01:15:25]** : Yeah. All right. Cool. That's it. Awesome. Thank you so much.

**Lukas [01:15:29]** : It was fun.

**Vibhu [01:15:29]** : Thanks.

---

## [[AINews] Reve 2 and Ideogram 4: Layouts in Imagegen](https://www.latent.space/p/ainews-reve-2-and-ideogram-4-layouts)
*🔬 Latent Space | 2026-06-04*

4 years ago we argued that image composition was partially [AGI-Hard](https://www.latent.space/p/agi-hard). That gate has fallen this year. It can't be pure coincidence that both [Reve](https://x.com/reve/status/2062260665121919101) and [Ideogram](https://x.com/ideogram_ai/status/2062202208700313872) launched today, both with a heavy emphasis on how they made advances with strong labeling and [code](https://x.com/swyx/status/2062371515937800468) for layouts: 

and here's Ideogram 4.0, now [the best open image model](https://x.com/arena/status/2062203346996605116):

These are great achievements, and all great US model achievements, but the Arena rankings do show [how far ahead GPT-Image-2](https://www.latent.space/p/ainews-openai-launches-gpt-image) is…

> AI News for 6/2/2026-6/3/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

# **AI Twitter Recap**

**Microsoft 's MAI-Thinking-1 Tech Report, Training Stack, and Frontier-Tuning Push**

  * **MAI-Thinking-1 is the day 's densest technical release**: Microsoft introduced **[MAI-Thinking-1](https://x.com/asadovsky/status/2062008312603070891)** , a generalist/reasoning model trained **without third-party distillation** , reporting **97% on AIME 2025** , **53% on SWE-Bench Pro** , and human preference wins over Sonnet 4.6 in blind side-by-sides. The 109-page report was widely praised for unusual transparency by [@eliebakouch](https://x.com/eliebakouch/status/2061965825037254947), [@nrehiew_](https://x.com/nrehiew_/status/2062013300196700395), and [@mustafasuleyman](https://x.com/mustafasuleyman/status/2062253941207761180). The main technical theme: Microsoft appears to have "hillclimbed from scratch," with [@MinjiYoon90](https://x.com/MinjiYoon90/status/2062058684730245376) explicitly framing the effort that way.

  * **Why researchers cared about the report** : The most-cited detail was not just benchmark quality, but the amount of systems/training information released. [@eliebakouch](https://x.com/eliebakouch/status/2061965825037254947) highlighted **zero synthetic data and zero prior-model distillation** , meaning reasoning, tool use, and agentic behaviors were learned in post-training without a synthetic "cold start." The thread also called out publication of the **scaling ladder recipe** , exact **MFU numbers** , and target-loss construction. In follow-ups, [@eliebakouch](https://x.com/eliebakouch/status/2061976608265880004) noted the private NLL mixture was weighted **50% code, 17.5% STEM, 17.5% math, 10% general knowledge, 5% multilingual** , with normalization against an internal model; he also pointed out ablations around **100 -200 TPP** for their MoE setup [here](https://x.com/eliebakouch/status/2061975730414633043). Other notable implementation details surfaced in the community recap: Microsoft used **SGLang** in parts of the stack, per [@eliebakouch](https://x.com/eliebakouch/status/2062002698363232401), and **dspy.GEPA** for pretraining data curation, per [@lateinteraction](https://x.com/lateinteraction/status/2062015109132873852) and [@harold_matmul](https://x.com/harold_matmul/status/2062040746027315714).

  * **Microsoft 's productization angle goes beyond one model**: Alongside the report, Microsoft pushed a broader "own your model" story. [@mustafasuleyman](https://x.com/mustafasuleyman/status/2062275417378041957) outlined **Frontier Tuning** , centered on reinforcement-learning environments for workflow-specific adaptation, claiming internal Excel-oriented MAI-tuned models can reach GPT-5.4-level quality on relevant tasks while being **up to 10 × more efficient**. The Build rollout also included **[MAI-Image-2.5](https://x.com/MicrosoftAI/status/2062240400299934143)** , which Microsoft says is **#3 on text-to-image** and **#2 on image-to-image** arena leaderboards, plus [MAI-Code-1-Flash](https://x.com/pierceboggan/status/2062220583786709163) and deployment into products like OneDrive Photos. As a meta-point, this is one of the clearest examples this year of a lab trying to publish a frontier-style report while simultaneously turning that stack into enterprise customization infrastructure.




**Open Model Releases: Gemma 4 12B, Ideogram 4.0, Miso One, and Local-First Momentum**

  * **Gemma 4 12B was the standout open-model launch** : Google released **[Gemma 4 12B](https://x.com/Google/status/2062203526588088452)** , an **Apache 2.0** multimodal model designed to run on-device with roughly **16GB VRAM**. The architectural novelty is its **encoder-free** design: no separate vision or audio tower. As [Google explained](https://x.com/Google/status/2062203532351090824), images are handled via a lightweight embedding module and raw audio is projected directly into the text-token space. Community reaction focused on the elegance of collapsing modality encoders into the LLM backbone, with [@googlegemma](https://x.com/googlegemma/status/2062202706882883696), [@googleaidevs](https://x.com/googleaidevs/status/2062204432658386950), [@mtschannen](https://x.com/mtschannen/status/2062236357351579915), and [@armandjoulin](https://x.com/armandjoulin/status/2062206784647967075) all emphasizing the same point. Tooling support landed immediately across [vLLM](https://x.com/vllm_project/status/2062228047324201166), [Ollama](https://x.com/ollama/status/2062250522598572345), llama.cpp/MLX via [@osanseviero](https://x.com/osanseviero/status/2062205176597889220), and [Unsloth GGUFs](https://x.com/UnslothAI/status/2062207258810053084) that reportedly enable local runs with as little as **8GB RAM** in quantized form.

  * **Ideogram 's flip to open weights mattered as much as the model itself**: [Ideogram 4.0](https://x.com/ideogram_ai/status/2062202208700313872) was announced as "the best open image model in the world," with open weights and immediate deployment via [fal](https://x.com/fal/status/2062202673361780873) and Hugging Face [here](https://x.com/huggingface/status/2062206083914158287). Arena quickly placed [Ideogram-4.0-Quality at #8 overall and #1 among open models](https://x.com/arena/status/2062203346996605116), with especially strong gains in **text rendering** and **branding/commercial design**. That open release got outsized attention because Ideogram had previously been regarded as highly design-centric but closed; the switch was noted by [@multimodalart](https://x.com/multimodalart/status/2062210597148930139) and [@cloneofsimo](https://x.com/cloneofsimo/status/2062210832440918309).

  * **Open audio also had a strong day** : **[Miso One](https://x.com/kimmonismus/status/2062210845308780639)** launched as an **8B open-weights TTS model** with **one-shot voice cloning** and claimed **110ms latency** , aimed at more expressive voiceover. Alibaba's [Fun-Realtime-TTS](https://x.com/ArtificialAnlys/status/2062016529848222073) also took **#1 on Artificial Analysis 's Speech Arena** at **1219 Elo** , ahead of Gemini 3.1 Flash TTS and Inworld, at **$27.59 / 1M chars**. Separately, [Google's Magenta RealTime 2](https://x.com/HuggingPapers/status/2062260306039259236) was highlighted as an open-weight, low-latency continuous music generator for on-device use.

  * **The bigger pattern is local AI becoming a mainstream deployment target** : [@ggerganov](https://x.com/ggerganov/status/2062193382605111386) called out Computex as a strong signal for **local AI workloads** ; [@rasbt](https://x.com/rasbt/status/2062235700636873082) similarly pointed to a growing open-weight, consumer-hardware ecosystem. Microsoft's [Surface Laptop Ultra](https://x.com/kimmonismus/status/2062201523963084864) pitch--up to **1 PFLOP AI compute** , **128GB unified memory** , RTX GPU--fits the same trend from the hardware side.




**Agents, Harnesses, and the Shift from Frameworks to Execution Layers**

  * **The center of gravity is moving from "frameworks" to agent harnesses and execution environments**: Several posts converged on the same idea. [@gakonst](https://x.com/gakonst/status/2062116487708512355) argued that the future IDE stack is less about code editors and more about replacing files with threads and bundling plan/design/build/deploy/monitor loops--leaving **collaboration/sync engines** as a key unsolved problem. In a complementary interview summary, [@ConorBronsdon](https://x.com/ConorBronsdon/status/2062224321381323218) reported Jerry Liu's view that the "framework era" is ending, with abstractions moving upward into **skills, tools, and context quality** rather than Python wrappers.

  * **Multi-agent and agent-optimization work is getting more concrete** : CMU/LTI's **[MACU](https://x.com/rsalakhu/status/2062194674794668066)** and [@kohjingyu's thread](https://x.com/kohjingyu/status/2062179533009178897) argue that computer-use agents should be designed as **multi-agent DAG-based systems** , with a manager decomposing tasks and dispatching parallel subagents. Reported gains were **4.7 -25.5%** across benchmarks and **1.5 × faster** completion on Odysseys. On the optimization side, Microsoft's **SkillOpt** got practical validation from [@omarsar0](https://x.com/omarsar0/status/2062204469538881988), who says plugging it into an orchestrator improved one multimodal extraction skill from **0.73 to 0.93**.

  * **Agent UX and deployment tooling are becoming products in their own right** : Nous's Hermes Agent updates drew strong engagement, including remote-connection fixes [here](https://x.com/Teknium/status/2061984430370267210), an updated remote guide [here](https://x.com/Teknium/status/2062170975949721612), and a larger dashboard overhaul [here](https://x.com/Teknium/status/2062315666439655499). Perplexity launched **[Personal Computer for Windows](https://x.com/perplexity_ai/status/2062189045728596080)** , an on-device orchestrator for apps/files, while [Cloudflare Browser Run remote tabs](https://x.com/BraydenWilmoth/status/2062180110208311558) showed a more agent-native browser control path. LangChain/LangSmith pushed on the observability and cost-control layer with [Gateway spend tracking](https://x.com/LangChain/status/2062188019784835559), [Sandbox/Gateway/Observability docs](https://x.com/hwchase17/status/2062144718427857256), and case studies around Deep Agents and LangSmith [here](https://x.com/LangChain/status/2062204592562073972).




**Routing, Cost Controls, and Open-vs-Frontier Deployment Strategy**

  * **Model routing is now a real debate, not a slogan** : [@levie](https://x.com/levie/status/2061974298760495132) argued that as token budgets become a meaningful opex category, **model routing is inevitable** , with domain-specific evals as the differentiator. But [@scottastevenson](https://x.com/scottastevenson/status/2062042036774314107) pushed back hard, calling most routing products "snake oil" so far: frontier models can be better/faster/cheaper in aggregate if they avoid retries; routing can destabilize tightly coupled systems; and API vendors can often internalize obvious arbitrage. [@fabianstelzer](https://x.com/fabianstelzer/status/2062051511484465351) added that cache writes and harness-model-prompt fit can erase expected savings.

  * **Enterprise users are starting to enforce hard cost ceilings** : [@simonw](https://x.com/simonw/status/2062143151184465964) highlighted reports that Uber caps coding-agent spend at **$1,500/month per employee per tool**. LangChain immediately framed this as a use case for [LangSmith Gateway](https://x.com/hwchase17/status/2062208385890570565). The broader sentiment was captured by [@Yuchenj_UW](https://x.com/Yuchenj_UW/status/2062225912662561106): some orgs may soon face a three-way choice between letting everyone "tokenmaxx," capping budgets, or reducing headcount and reallocating spend to the most productive AI-enabled workers.

  * **Real data points are starting to emerge for hybrid/open strategies** : Harvey's benchmark results were the cleanest example. In one study, [Harvey](https://x.com/harvey/status/2062218656420167785) found a hybrid legal agent with **GLM 5.1** as the main worker and **Opus 4.7** as an advisor beat pure Opus on all-pass rate (**18% vs 14%**) while costing **$368 vs $954** across 100 tasks. Harvey also reported that SFT could move **Kimi 2.6** from **11% to 15%** , beating Opus at roughly **11 × lower cost**. On the other side, [@ClementDelangue](https://x.com/ClementDelangue/status/2062248714945630632) argued routing plus post-trained open models will often win on cost/speed/control, while [@ypatil125](https://x.com/ypatil125/status/2062196581936529721) framed open models and open-model clouds as leading indicators of the eventual default for important workloads.




**Top tweets (by engagement)**

  * **Gemma 4 12B launch** : [@googlegemma](https://x.com/googlegemma/status/2062202706882883696) and [@Google](https://x.com/Google/status/2062203526588088452) drove the biggest technical engagement with the encoder-free multimodal release.

  * **Ideogram 4.0 open weights** : [@ideogram_ai](https://x.com/ideogram_ai/status/2062202208700313872) announced a notable shift from a strong closed image model to open weights.

  * **MAI-Thinking-1 transparency** : [@eliebakouch's thread](https://x.com/eliebakouch/status/2061965825037254947) was the most influential technical reading guide to the MAI report.

  * **Rosalind for life sciences** : OpenAI's [GPT-Rosalind update](https://x.com/OpenAI/status/2062281977122996256) signaled further verticalization of frontier models into domain-specific scientific research.

  * **Open audio/TTS momentum** : [Alibaba's Fun-Realtime-TTS](https://x.com/ArtificialAnlys/status/2062016529848222073) and [Miso One](https://x.com/kimmonismus/status/2062210845308780639) stood out as practical releases rather than just research demos.




* * *

# **AI Reddit Recap**

## **/r/LocalLlama + /r/localLLM Recap**

### **1\. Gemma 4 Multimodal Open Models**

[ Read more ](https://www.latent.space/p/ainews-reve-2-and-ideogram-4-layouts)

---

## [🔬Scaling Past Informal AI - Carina Hong, Axiom Math](https://www.latent.space/p/axiom)
*🔬 Latent Space | 2026-06-03*

In 2025, seven-month-old startup [Axiom solved all 12 of the problems Putnam exam](https://axiommath.ai/territory/from-seeing-why-to-checking-everything) (scoring 8/12 in the time limit) a prestigious undergraduate math exam. The 12/12 score is better than the top undergraduates (110/120) and the closest AI system that reported a result (DeepSeek 103/120), although it is unclear what the people and other systems would have scored with more time. Nonetheless, the Putnam exam is legendary for its difficulty, with the median score typically being 0 or 1 points. Taken by itself, this seems like a minor feather in the cap of AI; one of a long series of accomplishments by AI systems in elite competitions with humans, starting with Deep Blue beating Kasparov.

Fast forward to mid-2026, and Claude Code and Codex are setting the world on fire. In 2024 Anthropic's bet on code and enterprise looked like a more pragmatic niche play vs. OpenAI's better models and massive consume scale. Today, Amodei's all in bet on acceleration via code (images and video be damned) seems prescient.

Despite Anthropic's growing momentum, however, Axiom CEO Carina Hong sees coding ability as a necessary but not sufficient milestone on the path to AGI. Code arguably pushes the jagged frontier to the point of super intelligence in [some domains outside of coding](https://www.latent.space/p/lupsasca), but there are surprising gaps (link) that Carina believes will bottleneck AI progress. (Stats on math benchmarks).

## The informal bottleneck

"Verified AI" sounds like eating broccoli[1](https://www.latent.space/feed#footnote-1) and paying taxes, but to Axiom it means something very different. "Verification to me is about scaling brilliance, compounding brilliance," Carina told us.

It actually took a while for me to understand what she means by this (sounded like marketing-speak until it clicked). Carina brings up the legendary mathematician **Srinivasa Ramanujan**(["The Man who knew Infinity"](https://en.wikipedia.org/wiki/The_Man_Who_Knew_Infinity)) to illustrate this point. When G.H. Hardy finally persuaded Ramanujan to formally prove theorems instead of relying on his (formidable) intuition, it reportedly improved his own capabilities. This is presumably because formally proving things forced Ramanujan to articulate the details in a way that open up new lines of thinking, etc. This is how you "compound" in math -- building on solid rather than shaky foundations… also known as **Axioms**.

But formally proving things also allowed others to benefit from his intuition: the proofs are way of communicating an intuition and persuading others that the intuition is correct. This is scaling (more people use the result) and compounding (people can learn from and build on his work).

This is the core insight that lets us understand the approach Axiom is taking.

## Verified Generation

There are two ways that Verified AI shows up: in training and in inference.

But a quick detour: to a first approximation, "Formal Verification" means [using type checkers](https://towardsdatascience.com/introduction-to-lean-for-programmers/) (like for TypeScript, C++ or Rust, but more capable) to verify mathematical proofs that are meticulously specified using a language like Lean[2](https://www.latent.space/feed#footnote-2). It takes a lot of work to translate an "informal" proof (albeit one that most people would not remotely call "informal") in to a Lean proof[3](https://www.latent.space/feed#footnote-3). Axiom themselves have open sourced groundbreaking work with [AXLE](https://axle.axiommath.ai/) \- their toolkit of interactive Lean applications for exploring, validating, and manipulating mathematical proofs.

You can imagine how this would be (very) useful during Reinforcement Learning: instead of relying on best guesses based on statistics (GRPO, RLHF, etc.), you can just verify the proof is correct using a Lean verifier. This is obviously a much stronger reward signal, akin to compiling code and testing it (which is what is typically done with RL on coding).

The catch: LLM are not (currently) very good at proving things with Lean.

Enter Axiom: While they have not officially reported benchmark numbers besides the 12/12 Putnam result, Carina reports that they have achieved a very impressive 99% (187/189) ProofGen on [the Verina codegen benchmark](https://arxiv.org/html/2505.23135v1). This benchmark is to generate code _and_ proof of correctness for a series of problems. For context, OpenAI o3 (the last known OpenAI run) achieved 4.9% on this benchmark.

Based on the sparse benchmarking, it's hard to say how the frontier labs are currently doing outside [the annual IMO milestones](https://www.latent.space/p/captaining-imo-gold-deep-think-on), but Carina suggests that they still are not training to generate Lean proofs directly, rather relying on informal proofs.

Time will tell if the frontier labs' current approaches will close this gap.

## Scaling and compounding

Carina's Ramanujan analogy is pretty direct. Better proofs -> better Lean generation -> better RL. A stronger signal means higher sample efficiency and higher maximum performance. Great!

Scaling is pretty clear too: once I have proved something in Lean, the quality of the output is basically[4](https://www.latent.space/feed#footnote-4) as high as if it came from a human, so my high quality training set has grown in a way that an informal rollout corpus cannot. I can trust my Lean proofs.

Compounding is also clear: now all of future inference and training can build upon those proofs.

On the other hand, a model trained only using statistical signals like GRPO during RL lacks the sample efficiency, maximum performance and compounding corpus that a system that uses formal verification benefits from.

## All roads lead to verification

Broccoli and taxes notwithstanding, **verification** has shown up in a lot of our conversations. In the domain of physical systems, recall **[Applied Intuition](https://www.latent.space/p/appliedintuition)** :

> _" I think [verifiability] is probably the hardest problem right now, because the as the models get better, it can be harder and harder to find the faults on the system. And so the problem of doing proper eval to find those faults, that problem also keeps getting harder as the models get better."_

In theoretical physics, we recall **Alex Lupsasca** :

> _" …now that we're in this regime where you can just get ChatGPT to tackle thousands of questions at the same time, it will return proofs for a significant fraction of them. Now actually the onus is back on the humans to verify all the outputs. And so, yeah, as that becomes a bottleneck, I think formalizing math and automating verification will become more valuable."_

Verification is, in fact, the key differences between AI for science and AI for computation: in science you to have to actually test (verify) your hypothesis by performing physical experiments. Lab in the loop systems like [Radical AI](https://www.radical-ai.com/) and [Lila](https://www.lila.ai/) build around exactly this premise (we have recorded episodes with both of these teams and will release them soon!)

And yes, formally verifying critical systems such as flight control, nuclear power plants and pacemakers is a growing focus as the software and hardware that run them becomes more complex.

Carina believes so strongly that AGI _requires_ verified generation that she makes the unqualified claim that "We do not believe there is any other possible future."

## Expensive to produce, cheap to verify

Lean proofs are hard generate, but they can be easily shown to be correct or incorrect. But how do you know that the proof you created maps correctly to the problem you care about? As Carina puts it: "Anything that can be specified can be proven. Humans are bad at specifying everything we want."

Are we now in the specification business? Check out the episode to hear Carina's take, as well as:

  * Why hardware verification is a killer app

  * Details on the AXLE open API and recently released Discovery toolkit

  * The Erdos debacle

  * The OpenAI GPT-f diaspora




## Full Video Podcast

**Timestamps:**

  * **0:00** Intro: The $200M Series A and the Math Startup Thesis

  * **4:52** Verified AI: Scaling Brilliance, Not Fixing Lousiness

  * **13:42** Axiom's System: Lean Data, RL, and the Putnam Perfect Score

  * **22:12** Mathematical Discovery -- Before the Conjecture

  * **25:12** Rice's Theorem, Incompleteness, and Practical Limits

  * **30:42** Code With Proof -- The Verina Benchmark

  * **37:57** Proof Trees, Context Windows, and Scaling Limits

  * **43:57** Markets, Moat, and the Business Case ($1.6B valuation)

  * **55:27** Personal Origin Story: Oxford, UCL Gatsby, Stanford Law

  * **1:00:57** The Erdos Controversy and the Difficulty of Search

  * **1:06:02** AlphaZero for Math, Self-Improvement

  * **1:08:47** Startup Advantage and the OpenAI GPTF Thread

  * **1:13:17** Axle API -- Open Infrastructure for Lean at Scale

  * **1:20:47** Collaboration, Polymath, and Human Attention as the Bottleneck

  * **1:22:21** Founding Story -- Obsession, Law School, and Julie Zhuo

  * **1:26:17** The Bigger Vision -- AGI, Science, and Transfer Learning

  * **1:35:02** Bottlenecks, Fragmentation, and the Field's Future




[1](https://www.latent.space/feed#footnote-anchor-1)

I actually love broccoli, but then again, I also believe strongly in Test Driven Development, so ¯\_( ツ)_/¯

[2](https://www.latent.space/feed#footnote-anchor-2)

Formal verification also includes model checking (TLA+, SPIN), SMT-based tools (Dafny, F*, Why3), and refinement-type systems (Liquid Haskell) -- many of which don't look much like "type checking a proof" from the user's perspective even when there's a similar logical core underneath. It also gets applied to software and hardware correctness, not only pure mathematics.

[3](https://www.latent.space/feed#footnote-anchor-3)

This is an understatement. Most theorems remain informal because formalization is so hard to do. There has been a great deal of effort to formalize the most important proofs, with mixed results.

[4](https://www.latent.space/feed#footnote-anchor-4)

One might argue that its a bit lower because the proof is in distribution for the LLM.

---

## [⚡️Satya Nadella: No Priors x Latent Space Crossover Special at Microsoft Build](https://www.latent.space/p/satya-2026)
*🔬 Latent Space | 2026-06-03*

We've informally heard that Satya is a listener to LS for a couple years now, but it was still absolutely surreal to meet him and do a live pod at Build, together with our friends at **No Priors** , the leading VC AI Podcast that we also greatly admire!

We covered [the MAI model technical takeaways on yesterday's AINews](https://www.latent.space/p/ainews-microsoft-build-mai-thinking), so I will focus our recap of Satya's main messages around three elements:

  * **Satya 's adaptation of [the Bill Gates Line](https://www.latent.space/p/agent-labs?utm_source=publication-search)** for positioning Microsoft as the **Frontier Intelligence Platform** -- customers must gain much more value from the Microsoft ecosystem than Microsoft itself, by building on multi-model harnesses like OpenClaw and Scout, drawing on the full enterprise context exposed by context layers like Work IQ (heavily [dogfooded by his C-suite](https://www.latent.space/p/github)), and building up private evals and traces as a new form of Token IP

  * **AI ROI:** On one hand, enterprises are having difficult conversations around Tokenmaxxing and Layoffs, and on the other hand, there are serious re-evaluations of the End of SaaS since the Build vs Buy equation has changed so much. Our [previous SemiAnalysis guest](https://www.latent.space/p/valuemule) had… interesting comments on Microsoft's position on this as the ur-SaaS titan, and Satya had great answers

  * **Making the Impossible Possible:** Kevin Scott's inspiring framing around what the most ambitious version of applying AI and technology at large to business and social problems, like education and social impact.




Enjoy!

## Full Video

## Transcript

**Voiceover:** Welcome swyx, Sarah Guo, Elad Gil,, and Chairman and Chief Executive Officer of Microsoft, Satya Nadella

**Sarah Guo:** Welcome to a crossover episode of No Priors and Lane Space with Satya Nadella. Um, congratulations on an amazing build. No, thank you so much, and it's great to be with both of you. I listen to both of you or b- both the podcasts all the time. It's great to be on it.

Thank you so much. [00:01:00] So you're just talking about, um, these amazing, uh, announcements from across the Microsoft estate all morning for, I think, three hours. What is the, uh, what's the most important reflection or takeaway you have?

## AI as an Ecosystem Platform

**Sarah Guo:** I, I'd say there are, uh, perhaps the, the biggest one for me is let's sort of conceptualize this more as an ecosystem play as opposed to a single model or even a single platform, right?

**Satya Nadella:** I mean, you know, whatever I... At least for me, having grown up at Microsoft, having seen, whatever, four major platform shifts, uh, I sort of fall into that, um, uh, camp where a platform is defined by fundamentally its ability to create more value about the platform versus what's captured in the platform. And so if you, you view what's happening right now, I think this morning's keynote was how can any company, whether it's an AI native company or a traditional enterprise company, participate as a first-class participant where they can point to AI they created, [00:02:00] right?

It's not that they don't use other people's AI. Of course they will. But to me, what's the path? What's the recipe? How do I do it? What does a stack look like? What does the tooling look like? What is valuable? How do you do that? That's it. That's sort of our job to do. Yeah. Ecosystem strategy is, uh, very complicated, right?

**Sarah Guo:** Because you end up building certain components, partnering for certain components, supporting them. You just announced this big suite of models. Like, tell us a little bit about the, uh, training strategy for Microsoft now. Yeah.

## MAI Models & Training Strategy

**Sarah Guo:** So, so the thing that we wanted to do with the MAI models was to build, and as Mustafa talked about, first of all, a great lineage, right?

**Satya Nadella:** Starting with pre-training, uh, with very good data quality, uh, doing all the ablations, making sure because in, in some sense it's becoming even harder to build a clean lineage model just because there's so much stuff out there, uh, that you truly need to ablate out to be able to have a fantastic [00:03:00] pre-trained model.

In fact, that's one of the challenges of a lot of the open weight models is they look great on one benchmark or two, but they're not great on practice. So that's why, in fact, even in the RFDEs are, they, they are pretty gone really excited about these MAI models because how the heck can a small five B model hill climb?

Uh, and it goes back a little bit to what I think is ultimately the key thing to do, which is try to pursue finding that cognitive core. Uh, so to me, starting with a clean lineage- Then creating that ability for companies to be able to use this, right? Not just as a generalist, but to create their own specialist by building this hill climbing scaffold around it, right?

So it's not just the model, but you have a hill climb scaffold around it, then you will start building your RLE. You will start collecting the traces. Most importantly, you'll have private evals because we know all the evals out there are good, interesting, [00:04:00] but they're not really that critical- They're work, yeah

**Swyx:** at this point because they all can be maxed. And so the point is each company will have its own private eval. And so that end-to-end platform story around our models is sort of, uh, what I think is interesting. And then the one other thing, Sarah, since you brought that up, is I do feel there's a new frontier.

**Satya Nadella:** Like people talk about the frontier and are you operating at the frontier. Um, interestingly enough, if you add a little temporality to it, you can use, let's say, in, in, in fact, the, the Lando Lakes demo we showed was pretty cool. We used, whatever, GPT-55, right? Then you collected a bunch of traces, and then you took a 5B reasoning model and achieved higher.

**Sarah Guo:** Uh, so that is another aspect of what it means to appear... uh, you know, operate at the frontier Yeah. I, I think, uh, I first of all have to congratulate you on basically building a frontier neo lab inside of Microsoft in two years. Um, I'm wondering, you know, you have all this AI strategy that you're rolling out.

## Lessons from Two Years of AI Development

**Swyx:** I'm wondering, what do you know now that you wish you would tell yourself two years ago where- or two or [00:05:00] three years ago? Three years for the Jensen partnership, two years for, uh, MEI. Yeah, I mean, I think the, the thing when, that I reflect quite a bit, right, which is sort of obviously I got into all this when I got excited by the, the scaling laws paper and, you know, when, you know, even the OpenAI partnership came about when those folks said, "Hey, we're gonna really throw a lot of computer transformers."

**Satya Nadella:** Uh, and they've helped. I- the thing that I always look back and say, "Wow, these things, uh, do have capability that they're climbing up." W- I mean, this, you know, this crude way of saying it is intelligence is log of compute kind of works. Now what I think we underestimated perhaps is the real-world complexity of deploying these so that they actually deliver the value in the real world, right?

So the outcomes as measured by any benchmark is interestingly important, but the true eval is when people out there are able to do unique things that they only can value, and it's very [00:06:00] measurable, right? That I wish we had sort of even, like, had more in our consciousness, right? Which is as an industry.

**Sarah Guo:** Because right now I think when people say, "Wow, I don't want a token max," it's an artifact of us not having thought ourselves as an industry that we are using tokens to create value every step of the way. So I think that's kind of what I wish we had gotten there, but I'm glad we are here.

## Real-World Value & Use Cases

**Sarah Guo:** What are some of the use cases that you've seen that have created the most value for your customers?

Because I know that people talk a lot about code, and I think it's pretty clear that that's something that's having very large scale impact. Are there other areas that you find in common that your customers are really benefiting from? Yeah. I think, yeah, to your point, obviously coding is now got... But it's interesting, by the way, Elijah, to even talk about the coding, right?

**Satya Nadella:** Which is coding has worked so well that we now have to rebuild the IDE, right? I mean, it's kind of nuts to see what we sh- launched is like, oh my God, I have these hundred agent sessions. I... The cognitive load it transfers back to me as a human is so [00:07:00] excessive that now I need a new UI. Uh, oh, by the way, I, like the, the chat as the only artifact was also impossible, so that's why we need a canvas.

So it's kind of interesting for all the things about where is software needed or where is UI needed, uh, you kind of need that even for code, right? In a fully agentic world. But that said, one of the things that we are starting to see, we started seeing with co-work, but even some of the work we, we showed with auto com- uh, um, autopilot Right on what you see with claws is a good one because if you sort of think about a lot of human capital is doing the glue work, right?

If you now can augment that with tokens/agents that are long-running, durable, right, then your ability to scale even what is still judgment and glue work gets amplified like coding does. Uh, so you can... Like, I'm positive that six months from now we'll all be saying, "Oh, wow," like, all through ni- the night there was a bunch of stuff that [00:08:00] all these autopilots that I have working on my behalf with my delegated authority, so to speak, right?

I can... Sort of given even my identity, did a bunch of work, then of course I'll need my new ADE to say, "Well, what did you do?" Like, I might... "Did I do this work?" And so on. So I think that that's where compressing of workflows, uh, completing of tasks, uh, that's where I think a lot of the value gets created. I think you raised a really interesting point, which is there's the actual agent that's doing the code, and then there's a harness around it, and that's the environment, that's the context, that's everything you're setting up as a developer around actually a coding agent.

## The Harness Concept for Enterprise AI

**Sarah Guo:** What is the harness for the enterprise? Is there an equivalent concept for broader productivity work, or how do you think about that concept sort of generalized? That's right. So, so in some sense you kind of want the harness to define the models, the, the data, uh, and the tools, and so that you have a loop across those three.

**Satya Nadella:** And so what we are trying to, first of all, make sure is each of our products that we build, right, whether it's GitHub Copilot or the security copi- the, the [00:09:00] stuff we showed with MDASH or even the discovery for science, it doesn't matter, all of them are multi-model harnesses, um, with tools access so that you can do this progressive, uh, disclosure of tools even so that they're token efficient.

Uh, and then you're feeding it with very rich context because that's sort of the other hard lesson we have learned in the last two years is, oh my God, the amount of work you need to do to prep the context layer, uh, such that your plan can execute in the most efficient way is where the magic is. So we have, in our case, we have the GitHub harness, which essentially we're using across all our products.

It's available in Foundry, and we are open, like you can use your Llama harness, whatever. Or you can use the, um, uh, you know, any open harness or any harness of yours and train with your tools and multiple models and your context. And so that's the pitch. Because right now a lot of dialogue is, um, "Hey, if I train the harness plus tools and the model together, you get [00:10:00] evals."

**Elad Gil:** And what we are proving out is... And the best example of that is what we did with MDASH, right? Because when it launched, uh, it found bugs or vulnerabilities that were not found by Mythos Uh, and so there is existence proof, I would claim, that you can have a multimodal harness, uh, that can in fact be more, uh, performant in the real world So a premise behind the, uh, training at the independent frontier labs is really, you know, we're gonna have these models, and we'll have an API business, and we'll support enterprises and startups.

**Sarah Guo:** But

## Platform Strategy & Developer Ecosystem

**Sarah Guo:** a first-party product, be it productivity or code or search, drives the majority of revenue. That's a different value equation than you're describing, I think, with the Microsoft ecosystem. Uh, if, if that's the case, tell me if it's the case, uh, 'cause obviously you have first-party products and you have enablement products.

**Satya Nadella:** Um, what is the role of the develop- Like what is gonna be hard and the set of skills and the value capture the developer has in that world? Yeah. So I think that there's always [00:11:00] gonna be the case that someone who is super successful in- as a platform builder can also have first-party products. It was true with Windows.

It is true, uh, with, uh, the, the SaaS side and the cloud side as well with us and others and so on. But the thing that is, is it should not be a limiter to other people achieving that same success, right? That I think is the core difference, which is the, the network effects this time around, around intelligence are such because they learn from data, and not really lots of data.

It's just a few samples that you have to see to understand what's novel about something. So that's why the game becomes how to protect. So that's why I would say every company, having private evals may be the biggest IP, right? Think about it, like what's that private eval that you can then use even a frontier model to hill climb on and not leak the traces may be one of the biggest [00:12:00] drivers, uh, of IP.

Like, so in other words, another te- acid test is you have an eval that's private. You're using, uh, a g- a Model A. Can you switch it to Model B and e- you know, climb up? If you can, then you're in control. If you can't, you're not in control, and that's where even the harness decision becomes super important, right?

**swyx** So therefore, having an open harness, letting all models come in, having your evals, your context, your tools help you hill climb, I think is the skills that an AI native startup needs, a SaaS company needs, or every enterprise needs. Yeah, I think in, in a very real way you are ... Microsoft historically is an operating systems company and th- then become a cloud company.

Maybe like the third act is that you're a harness or evals company. Whatever w- ... whatever the, the sort of conglomerate of concepts that you wanna put together. Um, and, and I think like enabling every company to have like frontier intelligence or what- what- Yeah ... I forget the, the [00:13:00] exact term that you used, um, is the, is the mission, right?

**Satya Nadella:** That's it. Like that is, that is the platform promise, that you build with us, you will get your intelligence, uh, for your data. That's it. That ... To, to me, that is the ... Like if there was one tagline, uh, for this entire developer conference is- Can everybody operate at the frontier with their frontier intelligence, right?

To me, that is so important because otherwise it, I, I don't know how you achieve stable equilibrium, right? Which is how do I then go and say, "Well, my company is gonna have a terminal value because I now know how to continuously compound-" Yeah ... on top of what's a platform that gets better," right? So when, like Windows obviously came out, Adobe built, Autodesk built, uh, or even like take what Jensen said.

We built DX and he built, you know, CUDA on top of it. Um, right? I mean, I always say to Jensen, "God, I got the short end of that," right? "I wish, uh, we had recognized it." But nevertheless, but that, that idea that you can build a platform layer [00:14:00] that someone else can then extend out, um, and build their own intelligence layer in this case, I think is everything, right?

Without it, why have a developer conference? I can just come and have you all sort of just worship at the altar of one model. Yeah. But that's not a developer conference. Uh,

## IP, Evals & Company Value

**swyx:** backstage we, we had a discussion about what is IP or what is the, the value in a company. It used to be the length of, uh, human experience at a company, and now it's this other thing which is the evals, the, uh, experience in sort of applying agents to the company. Can you... I just want you to like flesh that out a bit more 'cause- Yeah ... it was very insightful.

**Satya Nadella:** It's a great way to frame it, right? Because yeah, at the end of the day, every company is gonna have both the human capital that is still gonna be super valuable, uh, because humans, uh, and their ability to find the gaps that exist at all times is going to be the way we all will create value, right?

I mean, so I'm definitely in the camp that this is going to be about expressing new forms of human agency and ambition even as token capital goes up, right? So let's say a cor- any corporation [00:15:00] has lots of tokens and lot of human capital. The question is how do you compound the two? So if you have a... Like if you take in Teams I have a bunch of agents doing work and a bunch of humans doing work, and the traces between those, that is really important context of how that enterprise is creating value.

Then that goes back to train not a generalist model, but to train the company veteran agent, uh, right? That is super valuable again, right? Which is when a company goes says, "It should in fact go onto the balance sheet," is how I think about it, right? That's so... In fact, there may be... Like human capital was never possible to go put on a balance sheet, uh, because you didn't know how to capture the tacit knowledge.

**swyx:** Whereas now I think you can with the agents that have learned through the h- through, through time, through all the traces. Uh, so that's what at least we think will happen. I, I think the SEC is gonna have to have accounting standards- ... for token, uh, expertise Uh, y- y- you're talking about the equilibrium [00:16:00] state, um, and a stable equilibrium where companies have this compounding value and can see terminal value for themselves.

## Future of SaaS & Business Models

**Sarah Guo:** Another challenge to, you know, the considered equilibrium of, okay, there are applications and workflows that are sort of common to a vertical or a horizontal. Um, and this was, like, the generation of SaaS companies and, you know, Microsoft has lots of SaaS properties as well. And then there are things that are very specific to every enterprise that they're differentiated against.

**Elad Gil:** Um, I'm sure you have heard much and participate in much of the debate about the end of software because all these workflows are, are cheap to generate now. Um, do you think the equilibrium looks different between what agents get built- Yeah ... in enterprises versus in their vendors in the future? Yeah. So I think what's happening there is, see, we, we had a particular way we captured, um, I would say workflow in apps, right?

**Satya Nadella:** Because we built a, a data model, right? We schematized some part of some business process. Mm-hmm. We then built a bunch of business logic. Yep. And then we put a bunch of UI [00:17:00] on top of it, right? So that's kind of what every SaaS company- And a little configuration. For, like, 20, 20 years that was the plan.

Right, that- Yeah ... and that was it. So interestingly enough, now you kind of get to re-litigate that vertical stacking, right? So I still think, for example, that data model that you built underneath every SaaS application is super good, right? Like, why reinvent it? Like, I, I, my general ledger better be a general ledger.

I don't need new schema creation. No. Uh, in fact, that entity relationship, uh, is actually pretty good, robust thing that I want to feed. And you want it to be stable. That's right. Yeah. Then same thing with business logic, right? If, if you look at, uh... We have this product called Power BI, right? It is like dashboards galore people created.

The beauty underneath that dashboard is a very rich semantic model, right? Someone took the pain to create a dashboard and do all the measures, and you want that. That's business logic, right? I want that to be available to me. So I think the [00:18:00] challenge of the SaaS business model is we packaged one way. We now have to learn how to unbundle these things and rebundle in new ways and discover new business models, right?

I mean, if you look at it, d- what's happening today with Microsoft 365 is a great example, right? We have this thing called Work IQ. In fact, like, what we are realizing is, oh my God, like, you know, if you look at... In fact, there's a pa- historical parallel too, right? We sold first Exchange and SharePoint and, uh, you know, before Teams, we had a thing called Lync Server and what have you, and we thought, "Oh, that's all gonna move to the cloud."

But little did we realize that, um, the number of people who will use servers in the cloud is 10X, 100X, right? Because people were not buying servers, they were just buying a subscription. Mm-hmm. The same thing is now happening with M365 because with Work IQ, we have exposed what is perhaps the most important database in a company that never got used as a database because it was only captive to our apps.

Mm-hmm. Right? It, it was all email operated on it, Teams operated [00:19:00] on it, Word, Excel, PowerPoint, SharePoint. But now, like this is one of the coo- coolest things I get to do with Work IQ. I go to a GitHub repo and I say, "Hey, I attended a bunch of design meetings last week related to this repo. Can you capture all that and tell me what changes I should make?"

I mean, think about that, right? It literally can go look at all those transcripts, come back with a plan to change a code base, right? Previously, you could never have thought of using M365 for something like that. So the value creation opportunity now in the agent world is in fact 10X more, but it does require us to have...

**Sarah Guo:** For example, there's going to be usage around M365, right? Which is going to be perhaps more than even the e- end users and we have to even re-architect. Like, in fact, like what I use to serve an inbox or a mailbox cannot be used to serve an agent. Uh, and so that's sort of what we are doing.

## Pricing Models: Per-User, Consumption & Outcomes

**Sarah Guo:** I don't believe in, like, permanent business models for any of these domains, but in the [00:20:00] near term, do you have a prediction between, uh, you know, outcomes-based pricing, token-based pricing?

**Elad Gil:** Enterprise bundles Yeah. The way I- I think about this is always we've had... Like, let's even take the per-user pricing. Mm-hmm. The per-user pricing is really an artifact of someone creating a budget needing certainty, right? Because it's the most important thing. Like, somebody wants a budget- Mm-hmm ... they need a per user.

**Satya Nadella:** And, and per user is just a set of entitlements to usage, right? That's kind of what it is. And so the way is, if the first bundling will be take some usage, bundle it into per user stacks and, you know, then sell subscriptions. So subscriptions I think are gonna be there, per user is gonna be there. Then the next big thing will be consumption.

So people will say, "I want consumption." And it's also possible that people will say, "I don't even want to pay for any of the subscriptions or the consumption's outcome." Mm. But remember, most people love outcomes until they have an outcome, because once you have an outcome, it's like giving away royalty, [00:21:00] right?

Mm. I mean, like I, I've talked to customers who love, you know, outcome-based pricing, and I say, "I'm all in," until they, "Oh my God," like, "what are you talking about? You're sharing in my outcome? No, no, no. I want you to go back to per-user pricing, and I want you to consumption price," right? So I think that debate will go on.

Uh, but and all, all, all of these business models have a particular time and a place versus one to rule them all. And if anything, if you're a SaaS vendor or you're a platform vendor, having that flexibility... And quite frankly, we face this with GitHub, right? We just recently announced a per-user pricing on GitHub because little, you know, we- GitHub Copilot was constructed at a per-user level before we understood even, uh, the intensity of usage of agents, right?

It was an interactive way for a developer to use code complete, maybe tasks. It was not like, oh, I launched 10,000, you know, agents that are going on all day, right? So that is what the adjustment is about. So now that we really want, there will [00:22:00] always be a per user, but there will have to be a consumption meter.

## Durability of SaaS & Build vs Buy

**Sarah Guo:** How do you think about the durability of SaaS more generally? One thing I've observed is in a lot of enterprises internally, there will be teams that almost have agent euphoria. They're so excited about the explosion of things they can build that they're trying to rebuild a lot of applications or going to their SaaS vendors and saying, "We're not gonna work with you anymore," or, "We're considering an internal project."

And it seems like in six to nine months, maybe some of those people will come back and say, "Actually, we, we can't rebuild everything." How do you think about what's durable in this world and what isn't? Yeah, it's a... It... I think we have to go through one full budget cycle on this to really see the, um- Uh, the sort of the emergence of the equilibrium, because at the end of the day, there's marginal cost to even generating the app, right?

**Elad Gil:** In, in fact, there can be even a, a simple way to say it, like if you should always acquire something if the marginal cost of building and maintaining, uh, something on your own is higher. Uh, right? That should be like it's a quantifiable- Yeah. Right? A quantifiable thing. And [00:23:00] the maintenance part is important, right?

Even, like you got to remember like, hey, you know, all the security stuff that now AI will find, you better fix them too fast. Uh, of course, there's a coding agent to help you with, but then that burns tokens, right? So whose responsibility is it? It's kind of like a, a cycle that you've got to think through.

And I think we have gone through the excitement that I can generate a lot of software. I think the next thing would be what software do I really want to generate? Mm-hmm. What software do I want to use from others? How do I compose these two into some agentic workflow that I have agency over, right?

**Sarah Guo:** Because I think there'll be very little tolerance for anybody who's inflexible, uh, at the vendor level. Uh, but at the same time, I think that anyone who has got that flexibility shows up, delivers the value, will be back at again, right? We're selling software, uh, but with just different business models, in fact Uh, speaking about building software, um, one of my favorite moments from, I think, a previous build maybe one or two years ago was they had a b- they, they...

**Swyx:** There was a section of you building your [00:24:00] own software. I'm curious if you're building anything now. Yeah. So I, I think the... You know, first of all, let's face it, right? Building software has made it possible for even the incompetence of a CEO of a company- ... like ours, uh, you can build, so thank God. But that said, I, I, I, I do feel that, you know, something like, um, GitHub Copilot to me, and especially the new Sessions app or the new app, has just made it so much more possible for you to have agency over artifacts that you felt you couldn't touch before, right?

**Satya Nadella:** So to, for me as a CEO, even to go to a code base, uh, to be able to learn about it, like I remember joining Microsoft long back, you know, first and then you say, man, everybody had to go in and look at, you know, whatever, Cutler's, Malik, or what have you to learn how to do good C, uh, C++ code. Um, so now that ability to be more full stack up and down is so good, but that doesn't mean every one of us should be doing the same thing.

The question is: [00:25:00] how do you then have the ability to inspect things, learn things, see things, um, I think is just so much more. And so to me, what I'm building a lot of is these long-running Foundry agents. Uh, right? So there's autopilots. So the easiest thing is, to me, I think I just built one, uh, even last week, where the idea was, hey, can I have an agent that is continuously monitoring essentially my own chief of staff autopilot, right?

We're gonna have that obviously in, uh, Scout. That's what, uh, uh, we showed. But it is so easy and trivial to build. I took Work IQ. I said, "Take Work IQ, go, uh, and build a Foundry long-running agent." Uh, store all the memory in, um, uh, using Ray Fin, right? Basically at my backend as a service. And lo and behold, it built it, and not only built it, I could say publish to Teams, and it published the damn thing to Teams.

**Sarah Guo:** So the ability, uh, to have a, you know, some end-to-end project like this complete is just pretty [00:26:00] miraculous. How do you think, uh,

## Future Engineering Roles

**Sarah Guo:** that impacts the different types of engineering roles that exist in the future? Because right now I think there's, you know, a dozen different types of engineers that you can be, from QA, front end, et cetera.

You know, there's a big swath. I've heard some people argue that in four or five years we'll basically end up with four engineering roles. It'll be people who are managing agents, it'll be four deployed engineers or FDEs, it'll be security engineers, and then people working on large scale infrastructure for a small number of services, and then everything else just collapses into the agentic world.

**Satya Nadella:** Yeah, I- Do you think that's a correct view of the world? Yeah, I mean, I think, I think we'll have to experiment our way through it. But what you said is what... There are some very at scale things. At LinkedIn, they did structurally change- Mm-hmm ... uh, and it, you know, basically built up a new discipline called full stack builder, right?

So they went and said, "Hey, let's bring, uh, people from design and product management, front end engineering, all put them together." Uh, but also have an edge, right? It's not like the design person still doesn't have the design edge, or the front end [00:27:00] person doesn't have the front end edge, but you can give yourself bigger scope in roles so that you're not confined to one role.

Um, and then r- equally, infrastructure has become very critical, right? So in other words, like, I mean, RLEs, I mean, one thing we've realized is even for the Excel team, for example. Mm-hmm. Building the RLE in which a reward can be learned is actually one of the hardest sort of infrastructure problems.

Mm-hmm. Uh, and so you kind of need even new talent, right? Distributed systems people even in what was considered an end user app team, uh, because it's a different skill set. So yes, infrastructure, science is the other one, obviously. Um, so I think we'll see how these evolve, right? Where's the s- real... I mean, always the world will have a bunch of specialists.

Okay. Um, you know, I think the generalist role is going to be the most exciting, right? Because the leverage of a generalist- Mm-hmm ... um, is where we are going to see the maximum returns, right? When, when you said, "Hey, are you coding?" I'm now a gen- Like, what... I've basically translated [00:28:00] knowledge work Right?

Which I did, where I created a Word document or a spreadsheet, or even, uh... And now I can build an app, right? It's in the same sentence. Uh, right? That idea that, "Oh, wow, my generalist skills have gotten higher leverage," I think is what we're gonna see across the board. Music to the ears of CEOs and VCs that are, like, a little dangerous and a lot of- Golden age for idea people

**Sarah Guo:** idea people. Yeah. Uh- With a lot of agency. I- if you take that idea of personal agency and you just zoom it out to the organizational context, um, uh, my partner Mike Renall, who, uh, actually started his career at Microsoft, just wrote an essay where one of the big takeaways is i- it's an age where you can be much more ambitious, and you need to be, given the pace of the environment and how quickly, actually, users and companies are open to adopting new technologies.

**Satya Nadella:** Um, how do you think about... I, I feel silly asking this of somebody running a, you know, trillion-dollar-plus company already, but

## Ambition & Making the Impossible Possible

**Satya Nadella:** how do you think about how Microsoft can be more ambitious now? It's a great question. Um, I [00:29:00] think, um- I think the, the thing in these type of transitions is to have a conceptual model of how work can change to go after outcomes that you could hardly imagine previously, right?

In fact, Kevin Scott has this nice line, right, which is, um, when you can make the impossible... Like, when you're making hard things easier, that's sort of one point of leverage. But true ambition is about making the impossible possible. So now the thing that is missing a little bit in all of our organizations is what is that new conceptual model of what can we build?

What was impossible and what can we build? And I'll give you one example of this, right, which is I take great inspiration from sort of the people who were managing the Azure net- network. And they came to the... This was from even last year. You know, we were scaling. You saw that I, I [00:30:00] talked about sort of how we built in the last 15 months more Azure capacity than we built in the first 15 years.

I mean, it's crazy. Wild. Yeah. Right? It's pretty wild. And it's the same team. So they saw that and they said, "Bob, this just ain't gonna work if we don't reconceptualize our work." So they built... Essentially they said, "Our job is not to do Azure networking. Our job is to build the agentic system does, that, that does Azure networking," right?

These are the folks managing the 500-plus fiber operators managing the VAN, right, all over. And fiber operations ultimately is a physical operation. Things get cut, things get, uh, you know, have to be repaired. You know, we have fancy words called DevOps and so on. Basically, emails are coming in and you gotta go respond to them, take care of it.

So they built this agentic system. They even have a character for it. It's called Miles, and it sort of does all this stuff, right? They started sort of screaming for more tokens and so on. And so they were saying, "Look, uh, we don't need a headcount. We need tokens in order to be able to [00:31:00] manage, uh, our operation."

That reconceptualization- Mm-hmm ... of what their work is, right? They, they basically took their work and made it meta, right? That meta work is now their new work. Mm-hmm. Right? In the '80s, if somebody had come to us and said, "4 billion people are gonna get up in the morning and start typing," my model would've been, we need 4 billion typists?

But we're not doing typing, we're doing knowledge work. So that, to me, I think is it, right, which is whether it's Microsoft or whether it's any organization, is to give ourselves permission to do new types of metacognition, meta work, using these new tools to change the outputs that matter, uh, and then really make the impossible possible.

**Sarah Guo:** So completing that dot or the, the connective tissue across those, I think, is where a lot of the enterprise value will get created.

## Data Center Build-Out & Community Impact

**Sarah Guo:** Should we talk about data centers? Yeah, please ask. Oh, okay. Well, uh, uh, w- we-- this leads nicely into the data center build-up. I always think, I- I just-- I'm just impressed at the sheer scale of the [00:32:00] build-out from Microsoft, but also everyone else, that this is redefining what it means to be a hyperscaler.

And I just feel like that, that, that is at unprecedented scale on finances, uh, on the way you run the company, but also the communities that are, that are impacted. Um, yeah, just talk a bit more about what you're seeing on the ground, like when you visit your- Yeah, I think there are two aspects of it.

**Satya Nadella:** Obviously, the, the build-out is, uh, extraordinary. Um, you know, nothing like this has happened, and it's great to be, uh, one of the participants in it. Uh, but you brought up the other part, right? I think at this point it's clear that unless we as an industry, uh, are very principled about ensuring that the benefits of all the stuff we're talking about are felt in real ways, uh, at the community level, right?

Because this is not just a, a campaign, um, right? It has to be real, where people are saying, "Look, this is not ch- changing the prices on energy for me." In fact, if anything, it's bringing down prices because long term there's going to be a better [00:33:00] grid, there is going to be more energy. Water consumption is, in fact, not sort of, uh...

In fact, water is being replenished, right? You gotta really, you know, educate folks on truly what's happening, the cl- uh, the closed loop systems we are building. We have to invest in the training, the jobs, the tax base. In fact, the least talked about stuff is the amount of jobs that get created during construction, after construction.

What's the tax base that's there in the community? And, and all this has to be real. Um, and, and if that is the case, then we will have permission. If it is not, we won't have permission. It's as simple as that, right? Which is, uh, we, we... I think we have to take it as an industry pretty seriously. Uh, I think it's good for communities to be skeptical, ask the hard questions, for us to do the hard work, earn that.

Um, but at the end of the day, if there's-- if we can really be the produ-- Wait. I've always felt like in human history, if you use a lot of energy but also create a lot of value for society- The story has been fantastic. If you don't [00:34:00] do that, it's not been that great. And this time around, I'm a firm believer that ultimately if you do have a token economy that drives productivity, that drives economic growth, that drives broad spread, um, you know, participation, better health outcomes, um, then I think we'll be in a great place.

**Sarah Guo:** Uh, and that's at least what we all have to be focused on. Yeah. It, it makes me think actually that with all these initiatives that you're doing, might be e- easier to see ROI in the communities first before in enterprise. Yeah. I, I mean, I think both sides. Yeah. In fact, it comes back together. It has to be the people in the communities are going to be employed, are going to be participants, uh, in the real economy, right?

**Satya Nadella:** That's I think the question is. Like, if we- if the broad economy is doing well and the communities are doing well, the dots get connected. It's sort of the market forces are such that we will connect the dots. And that I think is it. Like, you ought to be able to see the evidence. You can't be about o- any one company, uh, but it has to be broad economic growth and broad [00:35:00] ec- you know, community permission.

**Elad Gil:** Yeah. I guess I wanna talk about

## Societal Impact & Optimism About AI

**Elad Gil:** what you're most optimistic about currently or what have you most updated your personal models on regarding societal impact of AI? So you're saying what's the, the, the- What have you updated most on in terms of societal impact of AI? Yeah. I think the, um, the p- the most, um- Critical thing is the first question we even started with, which is we need to tell the story and make it real that everybody has a real shot to participate as a first-class participant in this new economy.

**Satya Nadella:** Right? That's kind of, I think we- in the next 12 months, 18 months, we need a way for people to say, "Oh, wow, I get it." Right? There's going to be tremendous capability, tremendous amount of infrastructure, but I can see what is going to happen, whether it's the benefits like health outcomes or my ability to create a startup or my ability to run my [00:36:00] local sort of, uh, store more efficiently.

It's just happening, and I see that, uh, benefit myself, right? That to me, you know, earning that permission in a path-dependent way, we can't wait. See, the one thing, Eli, that I've now learned is I think the world is gonna be very skeptical of tech and tech companies that say, "Trust us, we've got it. The g- future is gonna be glorious."

**Sarah Guo:** Uh, you kind of have to deliver tangible benefits. Um, and quite frankly, politicians winning elections, uh, because they have advocated for that. That will be at least my adjustment because without it, um, thinking that somehow... Because it's too important this time around. It's too much of the economy for it not to be the case So one very simple framework I have for, you know, what are, what is gonna be the broad benefit of AI, um, beyond the communities just working in technology, are, are sort of wealth creation- Yep

it's [00:37:00] gonna happen in a ton of different companies, startups and large companies. Then you have healthcare. Uh, you, you had amazing demos today. There are companies like Open Evidence. I think that is happening. Um,

## Education & Future of Learning

**Sarah Guo:** education seems like another one that's an- Yep ... obvious good where we haven't seen as much impact as I'd expect.

**Swyx:** Do you have a hypothesis on why that might be, or if it'll come? Yeah, I mean, I think this is where, again, how we think about education, how... You know, recently I met with, uh, the founders of Alpha School and learnt a lot about what they were going and going about, and it's fascinating to listen, uh, to how to even rethink- Mm

**Satya Nadella:** uh, what does education really look like. Because I think it's actually very important. Mm. Uh, and I'm not saying anything traditionally being done is less important, right? I was even looking at the, uh... It's fascinating to see. I, I, I forget the which Stanford class it was, uh, the, the Asian guidelines for CS something.

Mm. Uh, because you still need people to learn. Uh, like it was an interesting AI class that they were making sure people were learning how to apply softmax appropriately versus saying, "Hey, fix my training run." Mm-hmm. Uh, so I think learning concepts is important. It's going to [00:38:00] be, uh, critical. But the way we create the incentives, what are the credentials, how we value those credentials, what is the employment opportunity for those credentials?

So I think that there's a complete change that has to happen, uh, given the way to get to information, way to educate yourself, way to continuously keep yourself updated has changed so much. So I think interestingly enough, maybe the next big startup and success story could be someone who builds a new university, um, or a new, um, pedagogy even of how to get someone to go through a curriculum and find economic opportunity, uh, that's highly valuable.

Well, that has felt, uh, perhaps impossible for a long time, but it's a great note to end on and something that might be possible. It's still possible. Yeah. Thank you, Satya. Thank you so much. Thank you. Yeah. I appreciate it. Thank you all.

---

## [[AINews] Microsoft Build: MAI-Thinking-1 and MAI Family models](https://www.latent.space/p/ainews-microsoft-build-mai-thinking)
*🔬 Latent Space | 2026-06-03*

Today was a big day, not least because we caught up on [the state of GitHub vs Agents](https://www.latent.space/p/github), and recorded a [special pod with No Priors and Satya Nadella](https://x.com/TheTuringPost/status/2061901518522188251?s=20) -- at MS Build, Satya and Mustafa announced 7 new MAI models:

[](https://substackcdn.com/image/fetch/$s_!PL7Y!,f_auto,q_auto:good,fl_progressive:steep/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2F1e8ca90a-629c-44d5-af2f-0b0cd2a60aa2_1510x886.png)

This is an impressive lineup, especially considering that the [Microsoft-Inflection deal that set up MAI ](https://news.smol.ai/issues/24-03-20-ainews-shipping-and-dipping-inflection-stability-edition)only happened 2 years ago, and that these are all from-scratch pretrains. MAI today is by no means an unqualified frontier lab, but it is a good tier 2 neolab with obvious incentives to support domain specific finetunes (as opposed to [the frontier labs who have ~all killed finetuning](https://www.latent.space/p/ainews-the-end-of-finetuning)).

The star of the show was the [100+ page MAI tech report](https://microsoft.ai/wp-content/uploads/2026/06/main_20260602_2.pdf), which the research community is giving glowing reviews:

You can catch up on all the rest of the announcement in the excellent Verge recap, and the tweet summaries below:

> AI News for 06/1/2026-6/2/2026. We checked 12 subreddits, [544 Twitters](https://twitter.com/i/lists/1585430245762441216) and no further Discords. [AINews' website](https://news.smol.ai/) lets you search all past issues. As a reminder, [AINews is now a section of Latent Space](https://www.latent.space/p/2026). You can [opt in/out](https://support.substack.com/hc/en-us/articles/8914938285204-How-do-I-subscribe-to-or-unsubscribe-from-a-section-on-Substack) of email frequencies!

* * *

# **AI Twitter Recap**

**Top Story: Microsoft Build recap, and new MAI model technical details**

## **What happened**

**Microsoft used Build to position itself as both an AI platform company and a frontier-model lab, pairing broad product launches with unusually detailed disclosures about its new MAI model family.**

  * Microsoft AI announced **seven new MAI models** spanning reasoning, code, image, speech transcription, and voice, led by **MAI-Thinking-1** , **MAI-Code-1-Flash** , **MAI-Image-2.5** , **MAI-Transcribe-1.5** , and **MAI-Voice-2** according to [@MicrosoftAI](https://x.com/MicrosoftAI/status/2061887500541366489) and [@mustafasuleyman](https://x.com/mustafasuleyman/status/2061880164498428188)

  * The flagship reasoning model **MAI-Thinking-1** was presented as Microsoft's **first reasoning model** , built with **clean data lineage** and **zero distillation from third-party models** in posts from [@mustafasuleyman](https://x.com/mustafasuleyman/status/2061880164498428188), [@baseten](https://x.com/baseten/status/2061878701823066431), [@tuhinone](https://x.com/tuhinone/status/2061879239817969756), and [@HannaHajishirzi](https://x.com/HannaHajishirzi/status/2061901432627044430)

  * Microsoft released a **109-page technical report** for MAI-Thinking-1, which drew strong positive reactions from technically oriented readers for its level of transparency, including [@eliebakouch](https://x.com/eliebakouch/status/2061877335960281459), [@ethanCaballero](https://x.com/ethanCaballero/status/2061920873297088723), [@nrehiew_](https://x.com/nrehiew_/status/2062013300196700395), [@yacinelearning](https://x.com/yacinelearning/status/2061914159235617056), and [@stochasticchasm](https://x.com/stochasticchasm/status/2061916808626815161)

  * Microsoft also emphasized **local AI and agent-native Windows** : Build messaging highlighted **secure execution layers for agents** , a new **Surface RTX Spark Dev Box** , Windows AI access to the broader Windows GPU install base, and concept hardware such as **Project Solara/Scout** , summarized by [@yusuf_i_mehdi](https://x.com/yusuf_i_mehdi/status/2061882543641907528), [@TheTuringPost](https://x.com/TheTuringPost/status/2061865165734506683), [@kimmonismus](https://x.com/kimmonismus/status/2061860319547527191), and [@kimmonismus](https://x.com/kimmonismus/status/2061875714933371220)

  * Build also included a major **GitHub Copilot app** push as the "desktop home for agent-native software development," with **canvases** , cross-device continuity, and tighter GitHub agent workflows, from [@pierceboggan](https://x.com/pierceboggan/status/2061868635241828688), [@lukehoban](https://x.com/lukehoban/status/2061905434039246939), and reactions from [@techgirl1908](https://x.com/techgirl1908/status/2061870470237164018)

  * Microsoft introduced **Web IQ** , a new grounding/search API stack for AI agents, claiming the APIs already power "nearly all AI agents and chatbots in the industry today, including Copilot and ChatGPT," via [@JordiRib1](https://x.com/JordiRib1/status/2061866606670581871)

  * Satya Nadella framed Build as an ecosystem moment rather than a single-product launch, while Mustafa Suleyman framed it as the output of Microsoft's internal "hill-climbing machine," in [@satyanadella](https://x.com/satyanadella/status/2061896503304806521), [@mustafasuleyman](https://x.com/mustafasuleyman/status/2061934667096596657), and reaction from [@nrehiew_](https://x.com/nrehiew_/status/2061983583523475556)




## **MAI model family: disclosed facts and technical details**

### **MAI-Thinking-1**

  * Microsoft described **MAI-Thinking-1** as a **35B active parameter MoE** with a **256K context window** in [@mustafasuleyman](https://x.com/mustafasuleyman/status/2061880164498428188)

  * A separate summary from [@scaling01](https://x.com/scaling01/status/2061889624847343825) says the model is a **1T@35B parameter model** , **pre-trained on 30T tokens** , and trained using **8192 GB200 GPUs** ; this appears to be a reading of the technical report rather than Microsoft marketing copy

  * [@kimmonismus](https://x.com/kimmonismus/status/2061877528781025381) similarly summarized it as a **mid-size MoE with 45B active params** , but this conflicts with Mustafa's own **35B active** figure; the more authoritative figure in the tweet set is the official **35B active** number

  * Microsoft claims **97% on AIME 2025** and **53% on SWE-Bench Pro** , with blind human raters on Surge preferring it overall to **Sonnet 4.6** , from [@mustafasuleyman](https://x.com/mustafasuleyman/status/2061880164498428188) and [@asadovsky](https://x.com/asadovsky/status/2062008312603070891)

  * Microsoft says the model is **optimized on MAIA 200** , with **30% better performance per dollar** and **1.4x performance-per-watt gain** versus **GB200** when running MAI models end-to-end, per [@mustafasuleyman](https://x.com/mustafasuleyman/status/2061880164498428188)

  * Microsoft and partners repeatedly stressed **no third-party distillation** , "clean data lineage," and enterprise-controlled fine-tuning with "100% eyes-off" post-training data through Baseten, in [@baseten](https://x.com/baseten/status/2061878701823066431), [@tuhinone](https://x.com/tuhinone/status/2061879239817969756), and [@MicrosoftAI](https://x.com/MicrosoftAI/status/2061923309344756043)




### **MAI-Code-1-Flash**

  * Microsoft introduced **MAI-Code-1-Flash** as a fast coding model for **VS Code** and **GitHub Copilot CLI** , first announced by [@pierceboggan](https://x.com/pierceboggan/status/2061877165810131297) and later highlighted by [@mariorod1](https://x.com/mariorod1/status/2061914993550143513)

  * Official Microsoft messaging via [@mustafasuleyman](https://x.com/mustafasuleyman/status/2061880164498428188) says **Code-1-Flash achieves 51% on SWE-Bench Pro despite having just 5B parameters** , positioning it near Haiku-class size/cost

  * A competing summary from [@scaling01](https://x.com/scaling01/status/2061891478176112794) describes it as a **137B parameter MoE** , **256K context** , trained on **10T+ tokens** , and "stronger and more efficient than Claude 4.5 Haiku." That likely indicates **5B active parameters** rather than total parameters; the tweets do not fully reconcile this distinction, but together imply **small active footprint within a much larger MoE**

  * Availability at launch was highlighted as **GitHub Copilot / VS Code-first** , per [@scaling01](https://x.com/scaling01/status/2061891478176112794) and [@mariorod1](https://x.com/mariorod1/status/2061914993550143513)




### **MAI-Image-2.5**

  * Microsoft launched **MAI-Image-2.5** and a **Flash** variant, claiming both reached **#2 on leaderboards** , with [@mustafasuleyman](https://x.com/mustafasuleyman/status/2061880164498428188) saying they surpass **Nano Banana 2** on image editing

  * Independent leaderboard accounts supported the high ranking: [@arena](https://x.com/arena/status/2061887242579382660) reported **#2 in Image Edit Arena** with **score 1401** , **+10 points over Nano Banana 2** , Grok Imagine, and ChatGPT Image Latest HF

  * [@arena](https://x.com/arena/status/2061894541888962712) further said MAI-Image-2.5 "advances the Pareto frontier," meaning no model at its price tier scores higher on that benchmark

  * Distribution partners quickly followed, including [@OpenRouter](https://x.com/OpenRouter/status/2061894672847671724) and [@fal](https://x.com/fal/status/2061920052664820199)




### **MAI-Transcribe-1.5**

  * [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2061878491860324402) reported **MAI-Transcribe-1.5** as an unusually strong speed/accuracy point on the STT frontier: **~276x realtime** , **2.4% AA-WER** , **#3 overall** on its leaderboard

  * The model supports **43 languages** , including English, French, Arabic, Japanese, and Chinese, and supports **keyword biasing** for rarer terms such as names and medical terminology, per [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2061878491860324402)

  * Pricing was reported as **$6 per 1,000 minutes of audio** via Microsoft Foundry in [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2061878498609053909)

  * OpenRouter also listed the model among the three MAI launches it brought live the same day in [@OpenRouter](https://x.com/OpenRouter/status/2061894672847671724)




### **MAI-Voice-2**

  * MAI-Voice-2 appears in Microsoft's "seven models" umbrella and in OpenRouter's availability post at [@OpenRouter](https://x.com/OpenRouter/status/2061894672847671724)

  * The tweet set contains little technical detail on Voice-2 itself beyond launch/availability




## **Technical-report details that mattered to researchers**

### **Why the report stood out**

  * The dominant technical reaction was that Microsoft released an unusually detailed frontier-model report: [@eliebakouch](https://x.com/eliebakouch/status/2061965825037254947) called it "one of the most transparent for a model at this scale," [@nrehiew_](https://x.com/nrehiew_/status/2062023547690828141) said it "could really serve as an updated textbook for LLM training today," and [@stochasticchasm](https://x.com/stochasticchasm/status/2061879506139557979) called it a "gold mine"

  * Multiple readers highlighted that the report disclosed **pipeline details, scaling ladder methodology, data curation, infra metrics, and MFU numbers** ; this level of specificity is what drew praise from [@ethanCaballero](https://x.com/ethanCaballero/status/2061920873297088723), [@eliebakouch](https://x.com/eliebakouch/status/2062004670017486912), and [@nrehiew_](https://x.com/nrehiew_/status/2062013300196700395)




### **Pretraining and data**

  * A major technical claim repeated across commentary is that MAI-Thinking-1 used **no synthetic data** and **no distillation** , not only in post-training but throughout the disclosed pipeline, from [@eliebakouch](https://x.com/eliebakouch/status/2061965825037254947), [@stochasticchasm](https://x.com/stochasticchasm/status/2061967095022366924), and [@HannaHajishirzi](https://x.com/HannaHajishirzi/status/2061901432627044430)

  * [@eliebakouch](https://x.com/eliebakouch/status/2061977834558804207) says the report explicitly notes data from **Common Crawl plus private sources** , with **targeted sub-pipelines for different domains** , heavy extraction/dedup work, and an intentional choice of **no synthetic data**

  * The report's internal **private NLL set** used for scaling decisions was summarized by [@eliebakouch](https://x.com/eliebakouch/status/2061976608265880004) as:

    * **50% code**

    * **17.5% STEM**

    * **17.5% math**

    * **10% general knowledge**

    * **5% multilingual**

  * [@eliebakouch](https://x.com/eliebakouch/status/2061976230933496176) says architecture promotion in the scaling ladder was based on an **Efficiency Gain (EG)** metric: how much extra compute the baseline would need to match the candidate's loss

  * The same thread notes ablations at roughly **100/200 tokens per parameter** , described as around "Chinchilla optimal" for the setup, while also remarking this differs from dense-model heuristics due to MoE structure in [@eliebakouch](https://x.com/eliebakouch/status/2061975730414633043)




### **Post-training / RL**

  * The most discussed technical choice was that Microsoft appears to have started RL from a checkpoint with **no prior reasoning exposure** , which several readers found notable. [@stochasticchasm](https://x.com/stochasticchasm/status/2061879070141677615) called this a "very interesting decision," while [@stochasticchasm](https://x.com/stochasticchasm/status/2061878066314645861) reacted to graphs suggesting a jump from **< 20% AIME25 to >95%**

  * [@HannaHajishirzi](https://x.com/HannaHajishirzi/status/2061901432627044430) described the "climbing from scratch" recipe as **simple recipes, rigorous science, self-distillation, patience, and great infra**

  * [@soldni](https://x.com/soldni/status/2061882085573616003) characterized the process as "climbing with no distillation, like the big boys do"

  * Some independent readers inferred from the report that **synth data remains very valuable** for agentic performance in the broader field, even if Microsoft deliberately avoided it here; see [@stochasticchasm](https://x.com/stochasticchasm/status/2061961874879783376)




### **Data curation / judges / DSPy GEPA**

  * A detail that got substantial attention from the DSPy/late-interaction crowd: Microsoft reportedly used **GEPA / DSPy-optimized LLM judges** in pretraining data curation and quality scoring

  * This was highlighted by [@bj2rn](https://x.com/bj2rn/status/2061941109828301241), [@LakshyAAAgrawal](https://x.com/LakshyAAAgrawal/status/2062013650639241403), and [@lateinteraction](https://x.com/lateinteraction/status/2062015109132873852)




### **Infra / utilization / hardware co-design**

  * Microsoft reportedly disclosed **exact MFU across iterations** , which multiple readers said is rarely shared at this scale, per [@eliebakouch](https://x.com/eliebakouch/status/2061965825037254947)

  * [@scaling01](https://x.com/scaling01/status/2061889624847343825) summarized the run as using **8192 GB200 GPUs**

  * [@eliebakouch](https://x.com/eliebakouch/status/2062004120098144764) singled out a reported **~40% higher throughput per watt** -type figure as "pretty impressive and bullish on microsoft chips," though this may refer to rack-level budget or serving configuration and was not fully unpacked in-tweet

  * Microsoft's official framing connected model design to **MAIA 200** custom silicon and emphasized better **performance-per-dollar** and **performance-per-watt** vs NVIDIA GB200 in [@mustafasuleyman](https://x.com/mustafasuleyman/status/2061880164498428188)

  * Build's broader Windows/local-AI narrative also centered on hardware specifics such as:

    * **1 trillion parameters running locally on DGX Station**

    * **128GB unified memory**

    * **110 TOPS AI performance**

    * **20 CPU cores**

    * **70+ PowerToys utilities** from [@TheTuringPost](https://x.com/TheTuringPost/status/2061852480636653924)

  * Reactions also pointed to local runs of large models, e.g. [@kimmonismus](https://x.com/kimmonismus/status/2061852979318427988) on **RTX Spark running a 120B parameter model locally**




## **Build product/platform recap beyond the models**

### **GitHub Copilot app and agent-native development**

  * GitHub unveiled the **GitHub Copilot app** , pitched as a desktop surface for **agent-native software development** by [@pierceboggan](https://x.com/pierceboggan/status/2061868635241828688)

  * Key themes included:

    * **canvases** for bidirectional work between users and agents, per [@Techmeme](https://x.com/Techmeme/status/2061875738694062419)

    * continuity across **CLI, mobile, web, local, and cloud** , per [@lukehoban](https://x.com/lukehoban/status/2061905448287322243)

    * a growing role for GitHub as the center of agent workflows, reflected in [@techgirl1908](https://x.com/techgirl1908/status/2061870470237164018) and [@OrenMe](https://x.com/OrenMe/status/2061873010664001605)

  * Copilot CLI also got an experimental **terminal UI with tabs, built-in feedback/rubber duck, prompt scheduling, and voice input** , per [@GHchangelog](https://x.com/GHchangelog/status/2061870684876272123)




### **Windows as an agent runtime**

  * Microsoft's Windows org framed Build around "faster developer execution, a secure execution layer for agents, and unmetered intelligence that runs locally on device," per [@yusuf_i_mehdi](https://x.com/yusuf_i_mehdi/status/2061882543641907528)

  * Several posts stressed that Microsoft wants **Windows** to be the trusted execution platform for agents, not just Azure

  * [@TheTuringPost](https://x.com/TheTuringPost/status/2061865165734506683) described **Project Solara** as a platform for **agent-first devices** , with concepts including:

    * a **desktop AI companion**

    * a **wearable badge** with cameras, microphones, sensors, and secure authentication

  * [@kimmonismus](https://x.com/kimmonismus/status/2061860319547527191) saw these as handheld/desktop devices for controlling agents and compared them to expectations people had for standalone OpenAI hardware

  * [@kimmonismus](https://x.com/kimmonismus/status/2061875714933371220) separately highlighted **Microsoft Scout** as an "always-on personal agent for work"




### **Web IQ and search for agents**

  * [@JordiRib1](https://x.com/JordiRib1/status/2061866606670581871) announced **Microsoft Web IQ** as a suite of **AI-native grounding APIs** for **web pages, news, images, and videos**

  * His framing is important context: classic search engines were built for humans, but Microsoft believes future search demand will come from agents, potentially **1000x more queries** than human search traffic

  * He claimed Web IQ was re-architected from Bing's stack for **quality, latency, and token efficiency** , and that it already powers major chatbots including **Copilot and ChatGPT**




### **Foundry and open-model distribution**

  * [@jeffboudier](https://x.com/jeffboudier/status/2061868927207244277) said Satya cited **11,000+ models available in Microsoft Foundry** , of which **10,928** come from Hugging Face

  * This supports Microsoft's parallel identity at Build: both a first-party model builder and a large multi-model hosting/distribution platform




### **Build messaging around datacenters and compute**

  * Several observers noted Build discussion around **data center expansion** , community backlash, and Microsoft's argument that AI infra can expand without raising electricity costs to local communities; see [@kimmonismus](https://x.com/kimmonismus/status/2061854806395015316) and [@kimmonismus](https://x.com/kimmonismus/status/2061903253890330639)

  * [@scaling01](https://x.com/scaling01/status/2061901702324695115) highlighted Mustafa saying AI compute will grow **1000x in the next 3 years** , taking today's rough **5e27 FLOPs** frontier scale to **5e30 FLOPs by 2029**

  * [@mustafasuleyman](https://x.com/mustafasuleyman/status/2061880029315764256) summarized the company's philosophical theme as **" Humanist superintelligence"**




## **Facts vs. opinions**

### **Factual claims in the tweet set**

  * Microsoft launched **seven new MAI models** at Build: [@MicrosoftAI](https://x.com/MicrosoftAI/status/2061887500541366489)

  * Official metrics for MAI-Thinking-1: **35B active MoE** , **256K context** , **97% AIME 2025** , **53% SWE-Bench Pro** , and blind human preference over Sonnet 4.6: [@mustafasuleyman](https://x.com/mustafasuleyman/status/2061880164498428188)

  * Official metrics for MAI-Code-1-Flash: **51% SWE-Bench Pro** , **5B parameters** as stated in tweet copy: [@mustafasuleyman](https://x.com/mustafasuleyman/status/2061880164498428188)

  * MAI-Image-2.5 ranking claims were independently echoed by [@arena](https://x.com/arena/status/2061887242579382660)

  * MAI-Transcribe-1.5 speed/accuracy details came from independent benchmark account [@ArtificialAnlys](https://x.com/ArtificialAnlys/status/2061878491860324402)

  * Microsoft released a **109-page technical report** : [@eliebakouch](https://x.com/eliebakouch/status/2061877335960281459)




### **Opinions / interpretations**

  * "Microsoft is training serious models now?" from [@teortaxesTex](https://x.com/teortaxesTex/status/2061892492350407158) is an interpretive reaction to the model/report quality, not a standalone fact

  * Claims that the report is "one of the most transparent" or "an updated textbook" are opinions from [@eliebakouch](https://x.com/eliebakouch/status/2061965825037254947) and [@nrehiew_](https://x.com/nrehiew_/status/2062023547690828141), albeit shared by many readers

  * [@kimmonismus](https://x.com/kimmonismus/status/2061852480636653924) and [@TheTuringPost](https://x.com/TheTuringPost/status/2061865165734506683) framed Build as a strategic shift from cloud-only AI toward local reasoning/agents; that is analysis rather than official wording

  * Posts claiming Microsoft "leaked" Anthropic Mythos FLOPs, including [@swyx](https://x.com/swyx/status/2061878629504881151) and [@scaling01](https://x.com/scaling01/status/2061897540161728791), are speculative interpretations of a slide, later contested by the same cluster of commenters




## **Different opinions and perspectives**

### **Supportive views**

  * Technical readers were broadly impressed by the **report 's transparency** and Microsoft's willingness to publish details usually withheld at this scale: [@eliebakouch](https://x.com/eliebakouch/status/2061965825037254947), [@nrehiew_](https://x.com/nrehiew_/status/2062023547690828141), [@ethanCaballero](https://x.com/ethanCaballero/status/2061920873297088723), [@stochasticchasm](https://x.com/stochasticchasm/status/2061916808626815161)

  * Some saw MAI-Thinking-1 as proof Microsoft is becoming a genuine frontier lab rather than just a model reseller or application layer, e.g. [@teortaxesTex](https://x.com/teortaxesTex/status/2061892492350407158), [@echen](https://x.com/echen/status/2061907282607100075), [@NandoDF](https://x.com/NandoDF/status/2061901884042985728)

  * Enterprise/platform supporters liked the **clean-data-lineage** , **fine-tunable** , **eyes-off post-training data** story, especially Baseten/Microsoft's positioning around ownership and control: [@baseten](https://x.com/baseten/status/2061878701823066431), [@tuhinone](https://x.com/tuhinone/status/2061879239817969756)




### **Neutral / analytical views**

  * Several posts focused on **reading and unpacking the report** rather than cheering the launch, especially [@stochasticchasm](https://x.com/stochasticchasm/status/2061916808626815161), [@nrehiew_](https://x.com/nrehiew_/status/2062013300196700395), and [@eliebakouch](https://x.com/eliebakouch/status/2061965825037254947)

  * Some commentators were careful on benchmark interpretation. [@kimmonismus](https://x.com/kimmonismus/status/2061918020843557110) noted Microsoft appeared to compare to **Sonnet 4.6** generally, with **Opus-level comparability only on SWE Pro**

  * [@iScienceLuvr](https://x.com/iScienceLuvr/status/2061926066453962952) specifically appreciated reporting on **health benchmarks** such as HealthBench Professional and MedXpertQA rather than only coding/math




### **Skeptical / opposing views**

  * A subset questioned whether all numbers and comparisons were being interpreted correctly, especially around active params and external-model comparisons

  * The most visible skepticism concerned the apparent **Mythos FLOP "leak"**. [@iScienceLuvr](https://x.com/iScienceLuvr/status/2061882397340393514) suggested it was probably just an estimate, not a leak; [@scaling01](https://x.com/scaling01/status/2061989029025853757) later argued the original **6.1e27 FLOP** figure was unrealistic and supplied a lower alternative estimate before posting a correction in [@scaling01](https://x.com/scaling01/status/2061990840138899674)

  * There was also implicit skepticism in the field about whether **zero synth / zero distillation** is the right long-term recipe for best agentic performance, as noted by readers emphasizing synth-data deltas elsewhere, e.g. [@stochasticchasm](https://x.com/stochasticchasm/status/2061961874879783376)




## **Context: why this matters**

  * Build's announcements matter because they suggest Microsoft is no longer content with being only:

    1. Azure/OpenAI's cloud host

    2. GitHub's developer surface

    3. Copilot's application shell  
It is also trying to be a **first-party frontier model developer** with its own model family, silicon stack, and post-training platform

  * The **clean lineage / no distillation** emphasis is strategically significant. It addresses enterprise concerns around IP provenance, future controllability, and dependence on external labs

  * The **local AI** emphasis matters because Microsoft is tying AI strategy to Windows and device distribution, not just to Azure. Build messaging repeatedly pushed the idea that reasoning models, planners, and agents can increasingly run **on-device** , not only in the cloud: [@TheTuringPost](https://x.com/TheTuringPost/status/2061852480636653924), [@yusuf_i_mehdi](https://x.com/yusuf_i_mehdi/status/2061882543641907528)

  * The **109-page report** matters because frontier-model transparency has generally been shrinking, especially around data, infra, and training methodology. Multiple researchers explicitly noted the disclosure level is uncommon at this scale: [@eliebakouch](https://x.com/eliebakouch/status/2061965825037254947), [@nrehiew_](https://x.com/nrehiew_/status/2062023547690828141)

  * The Build recap also showed Microsoft trying to integrate all layers of the stack:

    * **models** : MAI family

    * **chips** : MAIA 200

    * **cloud** : Azure + Foundry

    * **OS** : Windows agent runtime

    * **developer UX** : Copilot app / VS Code / CLI

    * **retrieval/grounding** : Web IQ

    * **hardware form factors** : Solara / Scout concepts

  * This combination is why several observers described the event less as a normal dev conference and more as a coordinated move toward an **agent platform spanning cloud, edge, OS, and custom models** , e.g. [@satyanadella](https://x.com/satyanadella/status/2061896503304806521), [@mustafasuleyman](https://x.com/mustafasuleyman/status/2061934667096596657), and [@TheTuringPost](https://x.com/TheTuringPost/status/2061865165734506683)




## **The "Mythos FLOPs leak" mini-story**

  * During/after Build, some users claimed a Microsoft slide inadvertently revealed training compute for Anthropic's rumored **Claude Mythos** , with [@swyx](https://x.com/swyx/status/2061878629504881151) asking if Mustafa had leaked the FLOP count

  * [@scaling01](https://x.com/scaling01/status/2061897540161728791) estimated the slide implied **6.1e27 FLOPs** with a confidence interval based on pixel measurement, while [@kimmonismus](https://x.com/kimmonismus/status/2061908067034517853) noted that would be around **Gemini 3.1 Pro-scale** compute

  * That interpretation was subsequently challenged by [@iScienceLuvr](https://x.com/iScienceLuvr/status/2061882397340393514), who argued it was probably an estimate, and then by [@scaling01](https://x.com/scaling01/status/2061989029025853757), who posted a lower-range model-based estimate of **3.37e26 to 1.46e27 FLOPs** and later said the original numbers were **bogus** in [@scaling01](https://x.com/scaling01/status/2061990840138899674)

  * The episode is useful mostly as context: Build's compute/scaling messaging was detailed enough that people started trying to infer competitor training budgets from presentation materials




**Developer tools, agents, and coding workflows**

  * OpenAI launched **Sites in Codex** , letting teams turn ideas/docs/plans into deployed internal websites/apps with auth and dynamic data, first for business/enterprise users, in [@OpenAI](https://x.com/OpenAI/status/2061845949170045346), [@TheRohanVarma](https://x.com/TheRohanVarma/status/2061872164442403139), and [@gdb](https://x.com/gdb/status/2061988413105156128)

  * OpenAI also expanded **role-specific Codex plugins** across sales, data analytics, creative production, product design, and public equity workflows, with access to **62 apps and 110 skills** , from [@OpenAI](https://x.com/OpenAI/status/2061887650391625870) and [@OpenAIDevs](https://x.com/OpenAIDevs/status/2061888366791246071)

  * GitHub's **Copilot app** and Microsoft's Build push around agent-native software development were central to the day's tooling news: [@pierceboggan](https://x.com/pierceboggan/status/2061868635241828688), [@lukehoban](https://x.com/lukehoban/status/2061905434039246939), [@GHchangelog](https://x.com/GHchangelog/status/2061870684876272123)

  * Anthropic shipped a **CLI for Claude Platform** and upgraded Claude Code's `/fork` to run a background agent with exact context + prompt cache, in [@ClaudeDevs](https://x.com/ClaudeDevs/status/2061877343078244459) and [@ClaudeDevs](https://x.com/ClaudeDevs/status/2061947411141169494)

  * Nous launched **Hermes Desktop** , a local/native desktop surface for Hermes agents, in [@NousResearch](https://x.com/NousResearch/status/2061843507417944552), [@Teknium](https://x.com/Teknium/status/2061844602735538266), and later Tailscale/Ollama integration notes from [@Teknium](https://x.com/Teknium/status/2061984430370267210) and [@ollama](https://x.com/ollama/status/2062011585355551231)

  * Cognition launched **Devin Desktop** , positioned as an agent-neutral desktop for managing local/cloud agents and handoff between local planning and cloud execution, in [@cognition](https://x.com/cognition/status/2061889596703551926), [@ScottWu46](https://x.com/ScottWu46/status/2061998361373532187), and [@russelljkaplan](https://x.com/russelljkaplan/status/2061920322325205007)




**Models, local inference, and routing**

  * H Company launched **Holo 3.1** , a local computer-use model family based on Qwen-style architecture, with checkpoints from **0.8B to 35B** and formats including **NVFP4, FP8, and Q4 GGUF** ; a popular summary cited **79.3% on AndroidWorld** for the 35B model in [@TeksEdge](https://x.com/TeksEdge/status/2061825310669332818), with launch tweet from [@hcompany_ai](https://x.com/hcompany_ai/status/2061815355341725925)

  * Perplexity announced **hybrid agentic inference** for Perplexity Computer, splitting work between **local models on-device** and frontier cloud models for privacy and token efficiency, in [@perplexity_ai](https://x.com/perplexity_ai/status/2061861293569765847) and [@AravSrinivas](https://x.com/AravSrinivas/status/2061875858542096520)

  * OpenRouter data shared by [@ttunguz](https://x.com/ttunguz/status/2061846636805177692) showed **open-weight models at 69.1% of token volume** , versus **30.9%** for closed models

  * Commentary around **model routing** as a key future abstraction came from [@ClementDelangue](https://x.com/ClementDelangue/status/2061871024627482964), [@garrytan](https://x.com/garrytan/status/2061878212213572083), [@matanSF](https://x.com/matanSF/status/2061865185527074914), and the counterpoint from [@glennko](https://x.com/glennko/status/2061896887699964171), who argued enterprise production reliability makes generic routing harder than enthusiasts suggest

  * Local-AI UX improvements also appeared in Hugging Face's **hardware compatibility checks** and oMLX's native macOS app release from [@m_newhaus](https://x.com/m_newhaus/status/2061824017510584630) and [@jundotkim](https://x.com/jundotkim/status/2061863850874634242)




**Research and evals**

  * Google DeepMind announced **Co-Scientist** , a Gemini-based multi-agent hypothesis generation system for science, claiming collaborations that helped identify liver fibrosis targets, ALS approaches, and genetic leads for aging, in [@GoogleDeepMind](https://x.com/GoogleDeepMind/status/2061857539977842793), [@GoogleDeepMind](https://x.com/GoogleDeepMind/status/2061857550438392094), and [@GoogleDeepMind](https://x.com/GoogleDeepMind/status/2061857553076920643)

  * The new **Crafter / CraftEditor** work on editable scientific figure generation drew attention as a five-agent workflow for producing and refining figures plus raster-to-SVG conversion, in [@HuggingPapers](https://x.com/HuggingPapers/status/2061800325959324069), [@_akhaliq](https://x.com/_akhaliq/status/2061835314599993392), and [@TheTuringPost](https://x.com/TheTuringPost/status/2061883014410629400)

  * Tilde Research introduced **Wall Attention** , a RoPE-free attention method with diagonal forget gates, claiming training at **4k** and generalization to **200k+** tokens plus Triton kernels and strong decode throughput, in [@tilderesearch](https://x.com/tilderesearch/status/2061839600562409581)

  * A robotics vision encoder claiming **+22.5% real-world OOD success** by encoding dynamics-awareness rather than relying on static-image pretraining was posted by [@jbhuang0604](https://x.com/jbhuang0604/status/2061840469966090308)

  * New evals/benchmarks of note:

    * **PaintBench** for precise image editing, where best model reached only **17.1%** , from [@itskaixu](https://x.com/itskaixu/status/2061827068170518956)

    * **VSTAT** for video state tracking, arguing frontier MLLMs remain weak at tracking evolving world state, from [@PinzhiHuang](https://x.com/PinzhiHuang/status/2062004108249145442) and [@sainingxie](https://x.com/sainingxie/status/2062011403733512253)

    * **Data Agent Benchmark** for enterprise data workflows, from [@sh_reya](https://x.com/sh_reya/status/2061984097531310378)




**Inference, infrastructure, and agent systems**

  * Harvey + LangChain shared work on **cheap verifiers** for legal agents, showing **DeepSeek V4 Flash** could preserve **94 -96% agreement** with Opus 4.7 while reducing cost **18x** in per-criterion mode and **~1000x** in batch mode; for **3,200 RL rollouts** , verification cost dropped from **$18,000 to $18** , in [@harvey](https://x.com/harvey/status/2061866491033899371), [@hwchase17](https://x.com/hwchase17/status/2061867746141356427), and [@nikogrupen](https://x.com/nikogrupen/status/2061866707988431039)

  * W&B relaunched **Weave** as agent-first observability with integrations across common harnesses and automated detection of failure modes, in [@wandb](https://x.com/wandb/status/2061894943203831996) and [@neutralino1](https://x.com/neutralino1/status/2061949197851742525)

  * Prime-RL integrated **Mooncake Store** with vLLM for cross-node prefix / KV cache reuse, pitched as key for agentic rollouts, in [@m_sirovatka](https://x.com/m_sirovatka/status/2061862853997465738)

  * Together detailed serving optimizations for **MiniMax-M3** , citing **81 -125% throughput improvements** via KV-block-major sparse attention, paged decode, optimized index scoring, and multimodal preprocessing, in [@togethercompute](https://x.com/togethercompute/status/2061895336486949109)

  * MiniMax itself highlighted **1M context** , native multimodality, desktop-computer operation, and MSA reducing attention's share of decode time from **~30% to ~5%** , in [@MiniMax_AI](https://x.com/MiniMax_AI/status/2061944204604101020)




**Ecosystem, hardware, and industrial capacity**

  * Westmag emerged from stealth to build **American robot actuators and drone motors** , with **$11M raised** led by a16z and participation from Founders Fund, Lux, NFDG, Menlo and others, in [@boxcardavid](https://x.com/boxcardavid/status/2061825303715123234), [@packyM](https://x.com/packyM/status/2061835223470330100), and [@oyhsu](https://x.com/oyhsu/status/2061837257531670864)

  * PyTorch noted NVIDIA adoption of **OpenMDW-1.1** , a permissive AI-model licensing framework, across four open-model families in [@PyTorch](https://x.com/PyTorch/status/2061840384817328604)

  * Martin Scorsese publicly demonstrated narrow, preproduction use of **FLUX** for storyboarding with Black Forest Labs, framed as exploratory and complementary to hand-drawn work rather than generative replacement, in [@robrombach](https://x.com/robrombach/status/2061804823352086681) and [@TheRundownAI](https://x.com/TheRundownAI/status/2061834880917357011)




* * *

# **AI Reddit Recap**

## **/r/LocalLlama + /r/localLLM Recap**

### **1\. NVIDIA Nemotron 3 Ultra and RTX Spark Specs**

[ Read more ](https://www.latent.space/p/ainews-microsoft-build-mai-thinking)

---

---
title: "Twitter 影片逐字稿 — @codewithimanshu"
author: "@codewithimanshu"
date: 2026-04-25
source: "https://x.com/codewithimanshu/status/2047875091174981780?s=53"
type: tweet
---

# Twitter 影片逐字稿 — @codewithimanshu

**來源**: https://x.com/codewithimanshu/status/2047875091174981780?s=53
**作者**: @codewithimanshu
**發布日期**: 2026-04-25
**收錄日期**: 2026-05-17
**類型**: Twitter Video Transcript
**語音辨識**: OpenAI Whisper (base)
**語言**: 英文 (English)
**片段數**: 322

---

## 逐字稿（含時間戳）

**[00:00 → 00:02]** My name is Sid with Asaria.

**[00:02 → 00:05]** I am an engineer on the Cloud Code team.

**[00:05 → 00:12]** And today we're going to be talking a little bit about the Cloud Code SDK and the Cloud GitHub

**[00:12 → 00:14]** action that was just announced today.

**[00:14 → 00:18]** Cool, so a little bit about the agenda.

**[00:18 → 00:22]** We do a little quick start for the SDK just to give some examples of how to get started

**[00:22 → 00:25]** and how to use the SDK.

**[00:25 → 00:31]** We will then dive into a live demo of the GitHub action, which should be fun.

**[00:31 → 00:36]** The GitHub action was built on top of the SDK, so it's meant to be a source of inspiration

**[00:36 → 00:39]** for the kind of things that you can do using the Cloud Code SDK.

**[00:39 → 00:47]** We'll then dive into some more advanced features of the SDK, and then we'll end with having

**[00:47 → 00:51]** all of you set up the Cloud GitHub action on your repost.

**[00:51 → 00:55]** You guys can start using it and build on top of it.

**[00:55 → 01:00]** Cool, actually, before we get started, can I get a show of hands here how many people

**[01:00 → 01:02]** have used Cloud Code?

**[01:02 → 01:05]** Okay, so a lot of people.

**[01:05 → 01:11]** And of the people who have used Cloud Code, how many have used Cloud Dash P or know what

**[01:11 → 01:12]** that is?

**[01:12 → 01:15]** Okay, okay, far fewer people.

**[01:15 → 01:17]** It's good to know.

**[01:17 → 01:21]** If you guys don't have Cloud Code in a laptop, that's how you get it.

**[01:21 → 01:24]** I'd encourage you to install it in a laptop and follow along.

**[01:24 → 01:29]** There will be parts of this talk that will be beneficial to follow along, and then if

**[01:29 → 01:32]** you don't want to, you don't have to, it's all you had.

**[01:32 → 01:35]** Cool, so what is the Cloud Code SDK?

**[01:35 → 01:42]** It is a way to programmatically access the power of the Cloud Code agent in headless mode.

**[01:42 → 01:47]** This is powerful because it's a new kind of primitive and a new kind of building block

**[01:47 → 01:53]** that allows you to build applications that just weren't possible before.

**[01:53 → 01:58]** Things that you can do with the SDK are super simple things to get started.

**[01:58 → 02:00]** For example, you can use it like a Unix tool.

**[02:00 → 02:05]** The Unix-ish tool philosophy is what really makes Cloud Code powerful because you can plug

**[02:05 → 02:09]** it in anywhere where you can run Bash or Terminal.

**[02:09 → 02:12]** So you can use it in your Unix pipelines.

**[02:12 → 02:16]** You can pipe stuff into it, pipe stuff out of it, have like make like complex chains

**[02:16 → 02:18]** out of it and stuff like that.

**[02:18 → 02:23]** You can then build CI automation on it so you can have Cloud review your code.

**[02:23 → 02:27]** Some people actually get Cloud to write new linters for them too, so like Cloud can lint

**[02:27 → 02:30]** your code if there are specific things that you can't define programmatically.

**[02:30 → 02:32]** You can get Cloud Code to do it.

**[02:32 → 02:34]** And then we get into fancier applications as well.

**[02:34 → 02:38]** So if you want to build your own chatbot that's powered by Cloud Code, that's certainly

**[02:38 → 02:39]** possible.

**[02:39 → 02:44]** If you want Cloud Code to write you code in like a new environment or a separate remote

**[02:44 → 02:46]** environment, you can build those kinds of apps.

**[02:46 → 02:51]** And finally, these are a few features.

**[02:51 → 02:54]** We talk more about the features in the coming slides.

**[02:54 → 02:59]** And we have Python and TypeScript SDKs or bindings for the Cloud Code SDK coming up soon.

**[02:59 → 03:04]** So that should make it much easier for you guys to consume it and build on top of it.

**[03:04 → 03:08]** So let's jump into some basic examples.

**[03:08 → 03:14]** Calling Cloud Code SDKs as simple as doing Cloud-P and following it up with the string that

**[03:14 → 03:15]** you want to ask Cloud.

**[03:15 → 03:20]** So in this example, I'm telling Cloud to write me a Fibonacci sequence generator.

**[03:20 → 03:26]** And if you notice, I also give it a dash dash allowed tools write, which is a way for

**[03:26 → 03:29]** me to proactively give it access to the right tool.

**[03:29 → 03:34]** So it can write files to my file system.

**[03:34 → 03:38]** And then this is something I like doing too, piping logs to Cloud.

**[03:38 → 03:44]** So you can do cat.log and then pipe that into Cloud-P.

**[03:44 → 03:46]** I don't like looking at logs manually.

**[03:46 → 03:48]** So this is something I do quite often.

**[03:48 → 03:52]** And as you can see, it does a pretty decent job of summarizing what the log failures

**[03:52 → 03:54]** work.

**[03:54 → 03:59]** Similarly, if you're anything like me, I just can't get myself to understand the output

**[03:59 → 04:01]** of ifconfig.

**[04:01 → 04:03]** I still don't know what it means, but Cloud does.

**[04:03 → 04:06]** And Cloud does it for me over here.

**[04:06 → 04:10]** And finally, this is kind of what makes the SDK take, right?

**[04:10 → 04:12]** And this is a, we have an output format.

**[04:12 → 04:15]** If you do it dash, dash, output format, JSON.

**[04:15 → 04:21]** Cloud code will actually output things or its response in JSON as opposed to plain text.

**[04:21 → 04:24]** And you can parse this JSON and build on top of it.

**[04:24 → 04:29]** So we'll talk more about details for how this is what else you can do with this JSON,

**[04:29 → 04:34]** but I wanted to throw that example out there.

**[04:34 → 04:39]** Let's get into a significantly more complex example now, which is the Cloud GitHub

**[04:39 → 04:40]** action.

**[04:40 → 04:44]** So the Cloud GitHub action was built on top of the SDK.

**[04:44 → 04:47]** And it can be used to review code.

**[04:47 → 04:49]** It can be used to create new features.

**[04:49 → 04:54]** It can be used to triage bugs and so on.

**[04:54 → 04:55]** And this is also open source.

**[04:55 → 04:59]** So I'll include a link at the very end of the talk so you guys can go have a look at the

**[04:59 → 05:02]** source for inspiration for how to use it.

**[05:02 → 05:06]** But for now, let's jump into a live demo on my laptop.

**[05:06 → 05:13]** So I have cloned a popular small open source quiz app for the purposes of this demo.

**[05:13 → 05:17]** And we are going to fire it up just to see how that works.

**[05:17 → 05:22]** And then we will talk a lot to build something on top of it for us.

**[05:22 → 05:27]** So I just did an NPM start, which opened up my shiny new quiz app.

**[05:27 → 05:28]** It's actually pretty nifty.

**[05:28 → 05:31]** It allows you to choose a bunch of categories.

**[05:31 → 05:33]** How many questions you want?

**[05:33 → 05:34]** It's definitely easy for me.

**[05:34 → 05:37]** I suck at trivia.

**[05:37 → 05:38]** Type of questions.

**[05:38 → 05:40]** And then there's a countdown timer.

**[05:40 → 05:44]** So we're not going to actually answer these unless someone feels very strongly pleased to

**[05:44 → 05:45]** shout out the answer.

**[05:45 → 05:54]** But I'm just going to just fly through these just to show you guys how this quiz app works.

**[05:54 → 05:56]** There we go.

**[05:56 → 05:57]** Not surprising.

**[05:57 → 06:01]** You got a great F. But that's OK.

**[06:01 → 06:05]** So this was the little demo quiz app that's open sourced.

**[06:05 → 06:14]** And if we look at the issues for this repo, we see a couple very interesting ones.

**[06:14 → 06:21]** There's one issue that says we should add power ups for 50-50 elimination of options and

**[06:21 → 06:24]** skip questions for free.

**[06:24 → 06:28]** Because I suck at trivia, I really like that feature and I want to build it.

**[06:28 → 06:33]** And before this presentation, I already installed Cloud, the Cloud GitHub action on my repo.

**[06:33 → 06:35]** So it's already available.

**[06:35 → 06:40]** But we'll go over how to set that up later too.

**[06:40 → 06:42]** So here's the issue.

**[06:42 → 06:47]** It has pretty sparse details on how to implement this.

**[06:47 → 06:50]** It's just literally a wish list, really, like a wish feature.

**[06:50 → 06:57]** It's saying add a power up option in the config 50-50 elimination for the skip question.

**[06:57 → 07:01]** It should award user points even though the user skipped.

**[07:01 → 07:04]** And user should be able to configure this from the config page.

**[07:04 → 07:09]** So there's a lot of creative room for Cloud to do whatever it wants to do in this case.

**[07:09 → 07:11]** And I'm excited to see what it actually ends up building.

**[07:11 → 07:20]** So what I'm going to do is say, at Cloud, please implement this feature and comment on it.

**[07:20 → 07:25]** So it usually does take four or five seconds for it to respond.

**[07:25 → 07:29]** And while it's doing that for good measure, we'll just also take this other GitHub issue.

**[07:29 → 07:32]** This is talking about a per question timer.

**[07:32 → 07:35]** So we saw there was like a global timer on the quiz app, but there was no per question

**[07:35 → 07:36]** timer.

**[07:36 → 07:39]** So that's what this one's talking about.

**[07:39 → 07:46]** So let's go and say, Cloud, please build this.

**[07:46 → 07:48]** And now we have two things building.

**[07:48 → 07:49]** Cool.

**[07:49 → 07:54]** So now when I get back to this tab, you see that Cloud responded with a comment on this

**[07:54 → 07:57]** GitHub issue saying that it's working.

**[07:57 → 08:03]** It also has a link to the job run, which is the GitHub action run.

**[08:03 → 08:07]** If I click into it, and if I actually click on the logs, I'll see that it's doing a

**[08:07 → 08:08]** bunch of stuff.

**[08:08 → 08:11]** You can see all this JSON being output.

**[08:11 → 08:13]** This is from the SDK.

**[08:13 → 08:17]** So you want to look at the JSON too much because it's not much fun to parse it manually.

**[08:17 → 08:21]** But over here, we can see that it also created a 2DList for us.

**[08:21 → 08:26]** So Cloud is now going to actually go through this 2DList and try to implement the power

**[08:26 → 08:28]** of feature.

**[08:28 → 08:34]** And similarly, for the question timer, it's going to do something similar.

**[08:34 → 08:39]** One more thing that we should do here is there are already a couple of pull requests that

**[08:39 → 08:43]** have been opened for this repo.

**[08:43 → 08:47]** And let's get Cloud to review it or change some of these pull requests.

**[08:47 → 08:50]** Just for fun.

**[08:50 → 08:55]** Is this one, which is change background color to blue?

**[08:55 → 08:57]** I actually think I like green better.

**[08:57 → 09:00]** So I'm just going to be like, all right, Cloud.

**[09:00 → 09:05]** Please change this to green.

**[09:05 → 09:07]** This one is fairly easy.

**[09:07 → 09:08]** And I'm pretty sure Cloud's going to do this.

**[09:08 → 09:13]** But I just wanted to show you guys that I can also add commits for a pull request that's

**[09:13 → 09:14]** already open.

**[09:14 → 09:17]** OK, so this is going to take a few minutes to run.

**[09:17 → 09:20]** And while this runs, let's go back to the presentation.

**[09:20 → 09:26]** And then we'll check up on how this is doing towards the end.

**[09:26 → 09:26]** OK, cool.

**[09:26 → 09:32]** So let's do a little bit for deep dive on the features of the SDK.

**[09:32 → 09:40]** When you call Cloud-P, by default, it has no edit or destructive permission access, which

**[09:40 → 09:41]** is great for safety.

**[09:41 → 09:44]** But it's now great for actually getting things done.

**[09:44 → 09:49]** Which is why there is a dash-touch allowed tools option, which allows you to pre-configure

**[09:49 → 09:56]** Cloud with any permissions that you think it might need in the future for your given task.

**[09:56 → 10:01]** So in this case, the first example you see that I've given it permissions, bash permissions

**[10:01 → 10:06]** to NPM run build, NPM test, and the right tool.

**[10:06 → 10:13]** Which is a good set of permissions, because this allows Cloud to self-verify what it's

**[10:13 → 10:19]** writing and build your project and test and then continue writing.

**[10:20 → 10:26]** Similarly, for MCP, if you have MCP servers configured, you can allow this those MCP tools as well.

**[10:26 → 10:30]** So it's a very similar process.

**[10:30 → 10:33]** Then, structured output.

**[10:33 → 10:39]** We already saw an example of structured output, both from the GitHub actions logs and also

**[10:39 → 10:41]** the little screenshot I showed you earlier.

**[10:41 → 10:43]** But there's two modes here.

**[10:43 → 10:46]** There's StreamJSON and JSON.

**[10:46 → 10:47]** It does exactly what it sounds like.

**[10:47 → 10:53]** If you select StreamJSON, it'll actually stream messages to you as and when they're available.

**[10:53 → 10:57]** Versus JSON will just give you one giant blob of JSON at the end.

**[10:57 → 11:02]** And parsing this JSON and building on top of it is really how you can make use of the Cloud

**[11:02 → 11:06]** code SDK and then create features for your users.

**[11:06 → 11:09]** And then you can also configure the system prompt.

**[11:09 → 11:14]** So you can do dash-touch system prompt, talk like a pirate, and you can get Cloud Code

**[11:14 → 11:16]** to talk like a pirate for the rest of your day.

**[11:16 → 11:23]** This is actually quite fun if you haven't done it, I encourage you to try it out.

**[11:23 → 11:30]** We also have a few user interaction features built into the SDK.

**[11:30 → 11:35]** And what that means is that the first one is resuming session state.

**[11:35 → 11:43]** So when you call Cloud-P in structured output or JSON mode, it's going to return a session

**[11:43 → 11:44]** ID.

**[11:44 → 11:48]** And this session ID is useful because you can then reference the session ID to go back

**[11:48 → 11:54]** to the same context state that Cloud had when it finished that process.

**[11:54 → 11:58]** So by preserving these session IDs and keeping track of them, you can enable or build user

**[11:58 → 12:03]** interactive features where the user says something, you pass that on to Cloud.

**[12:03 → 12:07]** Cloud returns a response and now you want the user to give feedback on that response.

**[12:07 → 12:12]** And that's how this kind of enables you to build those types of interactions on your

**[12:12 → 12:14]** apps.

**[12:14 → 12:18]** And this one's actually pretty interesting and it's fairly recent too.

**[12:18 → 12:22]** It's Dash Dash permission prompt tool.

**[12:22 → 12:27]** We talked a little bit about how to give Cloud permissions using the allowed tools flag.

**[12:27 → 12:31]** And that requires you to pre-configure them in advance.

**[12:31 → 12:32]** But what if you didn't want to do them?

**[12:32 → 12:38]** Because you don't know what tools Cloud would want to use in the future.

**[12:38 → 12:43]** In that case, you can use the Dash Dash permission prompt tool and offload the permission

**[12:43 → 12:45]** management to an MCP server.

**[12:45 → 12:51]** So you can ask users in real time for whether they want accepted tool or rejected tool.

**[12:51 → 12:55]** And you can have an MCP server kind of handle that for you as opposed to trying to predict

**[12:55 → 12:58]** which tools are okay and which tools are not.

**[12:58 → 13:02]** So this is fairly recent and we'd love to get feedback on this if you guys end up trying

**[13:02 → 13:03]** it out.

**[13:03 → 13:12]** Okay, let's go back to our demo and see what Cloud's done.

**[13:13 → 13:18]** All right, so this is the power up issue.

**[13:18 → 13:21]** We can see that Cloud has actually gone through his to-do list.

**[13:26 → 13:28]** Okay, I'm going to open a PS.

**[13:28 → 13:34]** There's a link over here to create a PR and I'm going to click that and see what that gives us.

**[13:34 → 13:38]** I'll actually create the pull request too so it's easier for us to review.

**[13:38 → 13:42]** I don't really know how this code base works but we'll still eyeball it just as you see

**[13:42 → 13:45]** it's doing the right thing.

**[13:45 → 13:48]** So you see some set power up stuff.

**[13:48 → 13:49]** Seems all right.

**[13:52 → 13:55]** Okay, there's some configuration and the main component.

**[13:58 → 14:02]** All right, I think what we should do and what we make this fun is if we should just

**[14:02 → 14:06]** get this branch locally and see what Cloud did because there's no way that we can actually

**[14:06 → 14:09]** figure out what it did in the short amount of time that we have.

**[14:09 → 14:14]** So I'm going to go back to my terminal to a good fetch.

**[14:17 → 14:25]** Check out the branch that Cloud just created and restart our process.

**[14:27 → 14:30]** Okay, awesome.

**[14:30 → 14:36]** It looks like we have a power up section now at the bottom of our config page and it's a

**[14:36 → 14:37]** little check box.

**[14:37 → 14:39]** I like that touch.

**[14:39 → 14:47]** We'll keep both of them on and let's select general knowledge and start playing this game.

**[14:47 → 14:49]** Let's see what it did.

**[14:49 → 14:50]** Oh, sweet.

**[14:50 → 14:55]** So you see it has like this little 50-50 button on the bottom left and a skip questions

**[14:55 → 14:57]** button on the right.

**[14:57 → 15:01]** I'm just going to with 50-50 because I have no idea what the answer to this is.

**[15:01 → 15:03]** Does anybody know what that is?

**[15:03 → 15:05]** D. Okay, there we go.

**[15:05 → 15:06]** That makes sense.

**[15:06 → 15:07]** Cadbury, yeah.

**[15:07 → 15:14]** I'm going to skip this one and then let's just breeze through the other ones for a single

**[15:14 → 15:15]** time.

**[15:15 → 15:16]** All right.

**[15:16 → 15:31]** So we've got an F but we got one correct answer which is better than zero correct answers.

**[15:31 → 15:37]** Yeah, I guess.

**[15:37 → 15:38]** Yeah, it tricked us.

**[15:38 → 15:40]** That was a good one.

**[15:40 → 15:42]** But yeah, I mean, it seems like it worked.

**[15:42 → 15:43]** I think there's definitely more we could do here.

**[15:43 → 15:48]** We could like show how the power, like which questions we use the power upon over here and

**[15:48 → 15:50]** there's like definitely more we can do.

**[15:50 → 15:56]** But at the most basic level, I think Claude was able to do the task that we assigned it

**[15:56 → 15:58]** to do, which is exciting.

**[15:58 → 16:02]** This is kind of the power of the GitHub action because you don't really have to run this

**[16:02 → 16:03]** on your own in for you.

**[16:03 → 16:06]** You can just literally comment on a thread saying, please build this for me.

**[16:06 → 16:12]** It uses your GitHub action runners and just like does the thing.

**[16:12 → 16:19]** Let's also look at the PR that we told it change from blue to green.

**[16:19 → 16:20]** It's all hex code.

**[16:20 → 16:22]** So let's just see what it did in the commits.

**[16:22 → 16:28]** So we see there's two commits and Claude has added this last one to switch it from blue

**[16:28 → 16:29]** to green.

**[16:29 → 16:37]** And it did it for all three of the places where the color was defined, which is awesome.

**[16:37 → 16:40]** Okay, I'm not going to go over the last one, the question timer because we might run out

**[16:40 → 16:42]** of time.

**[16:42 → 16:48]** But this hopefully gives you insight into what the Cloud GitHub action can do for you.

**[16:48 → 16:52]** Let's go back to the presentation now.

**[16:52 → 16:58]** Okay, so just as a recap, the Cloud GitHub action.

**[16:58 → 17:02]** As it's implemented today is able to read your code.

**[17:02 → 17:06]** It's able to create PRs for you from GitHub issues like we just saw.

**[17:06 → 17:07]** It's able to create commits for you.

**[17:07 → 17:11]** So if you already have a PR and you commit or you comment on it, it can add a commit to

**[17:11 → 17:14]** an existing branch or an existing PR.

**[17:14 → 17:15]** It can answer questions.

**[17:15 → 17:17]** It doesn't have to do something.

**[17:17 → 17:18]** It can just literally answer questions for you.

**[17:18 → 17:22]** If you don't understand something, you can be like, Hey, Claude, how does this work?

**[17:22 → 17:24]** And you can get it to answer questions.

**[17:24 → 17:26]** And it can of course review your code.

**[17:26 → 17:29]** The best part of all of this is that you don't have to take care of the infra.

**[17:29 → 17:33]** It runs on existing GitHub runners, which almost everyone has configured if you're using

**[17:33 → 17:35]** GitHub actions.

**[17:35 → 17:39]** So that's kind of the really nice thing about this is you don't have to worry about any

**[17:39 → 17:40]** of the infra.

**[17:40 → 17:46]** Okay.

**[17:46 → 17:48]** So how were the actions built?

**[17:48 → 17:49]** Right?

**[17:49 → 17:53]** I think I may have mentioned that these actions were built on top of the SDK.

**[17:53 → 17:57]** So the SDK does form the foundation of how these actions were built.

**[17:57 → 17:59]** And then we have two other actions on top.

**[17:59 → 18:02]** We have the Claude base action.

**[18:02 → 18:10]** This is a thin layer that just, it just implements the piece which talks to Claude and returns

**[18:10 → 18:12]** the response from Claude code.

**[18:12 → 18:16]** And then we have another action on top of this, which is called the PR action.

**[18:16 → 18:21]** And this action is responsible for all the fancy things that you saw on the PR.

**[18:21 → 18:24]** So it's responsible to make in comments for the to-do lists, for rendering it the right

**[18:24 → 18:28]** way, for adding the PR links, and things like that.

**[18:28 → 18:32]** So it's kind of three layers in which it's built.

**[18:32 → 18:36]** Both the base action and the PR action are open sourced.

**[18:36 → 18:41]** So I would encourage you guys to go have a look, take inspiration from how that works,

**[18:41 → 18:44]** and maybe that inspires more ideas.

**[18:44 → 18:46]** Yeah.

**[18:46 → 18:57]** And then finally, we also, you guys can install the Claude GitHub actions today.

**[18:57 → 19:04]** The easiest way to do this is to open up Claude code in a terminal in the repo that you

**[19:04 → 19:05]** want to install it in.

**[19:05 → 19:11]** And once you open up Claude code, just do slash install GitHub action.

**[19:11 → 19:17]** And that is going to present you with a nice flow, which guides you through configuring

**[19:17 → 19:19]** your GitHub action as well as merging it.

**[19:19 → 19:26]** So the end result of this would be a PR, which would be a YAML file for your GitHub action.

**[19:26 → 19:30]** And once you merge that in, and you can figure your API keys and things like that, your

**[19:30 → 19:35]** off-the-racers, and you can go ahead and start tagging Claude and using Claude like we just

**[19:35 → 19:39]** did right now.

**[19:39 → 19:45]** So if you're a bad rock or a vertex user, the instructions are a little bit different

**[19:45 → 19:47]** and the tiny bit more manual.

**[19:47 → 19:49]** So please have a look at the docs.

**[19:49 → 19:56]** The docs are pretty comprehensive in helping you set up the GitHub action for both bad rock

**[19:56 → 19:58]** and vertex.

**[19:58 → 20:00]** Cool.

**[20:00 → 20:02]** Finally, resources.

**[20:02 → 20:05]** These are resources for things that we've talked about today.

**[20:05 → 20:09]** If you want to snap a picture, go ahead.

**[20:10 → 20:16]** The open source, three posts for both the base action and the Claude action are here.

**[20:16 → 20:18]** And we absolutely love your feedback as well.

**[20:18 → 20:24]** So if you guys have any feedback on the SDK, on the GitHub action, or on Claude code, please

**[20:24 → 20:31]** go to our public Claude GitHub repo and file an issue there, and someone will have a look

**[20:31 → 20:35]** and get back to you.

**[20:35 → 20:36]** Cool.

**[20:36 → 20:37]** That's all I have for today.

**[20:37 → 20:41]** Thanks for joining me, and I hope you guys have a good rest of the day.

---

## 核心摘要

> Anthropic Claude Code 工程師 Sid Asaria 示範 Claude Code SDK 與 Claude GitHub Action 的完整工作流程。

### 重點

**Claude Code SDK**
- `claude -p "<prompt>"` 以 headless 模式程式化呼叫 Claude Code agent
- 用法：Unix pipeline 串接、CI 自動化（code review、自訂 linter）、chatbot、遠端開發環境
- 關鍵 flags：`--allowed-tools`（預授權工具）、`--output-format json/stream-json`（結構化輸出）、`--system-prompt`、`--resume`（session ID 續接）
- 最新功能：`--permission-prompt-tool`，將 tool 授權決策委外給 MCP server，適合不確定需要哪些工具的情境

**Claude GitHub Action**
- 建構在 SDK 之上，三層架構：SDK → Base Action（對話層）→ PR Action（GitHub 整合層）
- 能力：從 issue 建 PR、對現有 PR 加 commit、回答問題、code review
- 無須另建 infra，跑在既有 GitHub Action runner 上
- 安裝：在 Claude Code 終端執行 `/install-github-action`

**Live Demo 亮點**
- 對 quiz app GitHub issue 留言 `@claude please implement this feature` → Claude 自動建 PR 並實作 50-50 排除 + 跳題 power-up 功能
- 對現有 PR 留言要求改色（blue → green）→ Claude 找出所有 3 個 hex 定義並一次修改

**Python / TypeScript SDK bindings** 即將推出，降低使用門檻。

---

## 完整純文字

My name is Sid with Asaria. I am an engineer on the Cloud Code team. And today we're going to be talking a little bit about the Cloud Code SDK and the Cloud GitHub action that was just announced today. Cool, so a little bit about the agenda. We do a little quick start for the SDK just to give some examples of how to get started and how to use the SDK. We will then dive into a live demo of the GitHub action, which should be fun. The GitHub action was built on top of the SDK, so it's meant to be a source of inspiration for the kind of things that you can do using the Cloud Code SDK. We'll then dive into some more advanced features of the SDK, and then we'll end with having all of you set up the Cloud GitHub action on your repost. You guys can start using it and build on top of it. Cool, actually, before we get started, can I get a show of hands here how many people have used Cloud Code? Okay, so a lot of people. And of the people who have used Cloud Code, how many have used Cloud Dash P or know what that is? Okay, okay, far fewer people. It's good to know. If you guys don't have Cloud Code in a laptop, that's how you get it. I'd encourage you to install it in a laptop and follow along. There will be parts of this talk that will be beneficial to follow along, and then if you don't want to, you don't have to, it's all you had. Cool, so what is the Cloud Code SDK? It is a way to programmatically access the power of the Cloud Code agent in headless mode. This is powerful because it's a new kind of primitive and a new kind of building block that allows you to build applications that just weren't possible before. Things that you can do with the SDK are super simple things to get started. For example, you can use it like a Unix tool. The Unix-ish tool philosophy is what really makes Cloud Code powerful because you can plug it in anywhere where you can run Bash or Terminal. So you can use it in your Unix pipelines. You can pipe stuff into it, pipe stuff out of it, have like make like complex chains out of it and stuff like that. You can then build CI automation on it so you can have Cloud review your code. Some people actually get Cloud to write new linters for them too, so like Cloud can lint your code if there are specific things that you can't define programmatically. You can get Cloud Code to do it. And then we get into fancier applications as well. So if you want to build your own chatbot that's powered by Cloud Code, that's certainly possible. If you want Cloud Code to write you code in like a new environment or a separate remote environment, you can build those kinds of apps. And finally, these are a few features. We talk more about the features in the coming slides. And we have Python and TypeScript SDKs or bindings for the Cloud Code SDK coming up soon. So that should make it much easier for you guys to consume it and build on top of it. So let's jump into some basic examples. Calling Cloud Code SDKs as simple as doing Cloud-P and following it up with the string that you want to ask Cloud. So in this example, I'm telling Cloud to write me a Fibonacci sequence generator. And if you notice, I also give it a dash dash allowed tools write, which is a way for me to proactively give it access to the right tool. So it can write files to my file system. And then this is something I like doing too, piping logs to Cloud. So you can do cat.log and then pipe that into Cloud-P. I don't like looking at logs manually. So this is something I do quite often. And as you can see, it does a pretty decent job of summarizing what the log failures work. Similarly, if you're anything like me, I just can't get myself to understand the output of ifconfig. I still don't know what it means, but Cloud does. And Cloud does it for me over here. And finally, this is kind of what makes the SDK take, right? And this is a, we have an output format. If you do it dash, dash, output format, JSON. Cloud code will actually output things or its response in JSON as opposed to plain text. And you can parse this JSON and build on top of it. So we'll talk more about details for how this is what else you can do with this JSON, but I wanted to throw that example out there. Let's get into a significantly more complex example now, which is the Cloud GitHub action. So the Cloud GitHub action was built on top of the SDK. And it can be used to review code. It can be used to create new features. It can be used to triage bugs and so on. And this is also open source. So I'll include a link at the very end of the talk so you guys can go have a look at the source for inspiration for how to use it. But for now, let's jump into a live demo on my laptop. So I have cloned a popular small open source quiz app for the purposes of this demo. And we are going to fire it up just to see how that works. And then we will talk a lot to build something on top of it for us. So I just did an NPM start, which opened up my shiny new quiz app. It's actually pretty nifty. It allows you to choose a bunch of categories. How many questions you want? It's definitely easy for me. I suck at trivia. Type of questions. And then there's a countdown timer. So we're not going to actually answer these unless someone feels very strongly pleased to shout out the answer. But I'm just going to just fly through these just to show you guys how this quiz app works. There we go. Not surprising. You got a great F. But that's OK. So this was the little demo quiz app that's open sourced. And if we look at the issues for this repo, we see a couple very interesting ones. There's one issue that says we should add power ups for 50-50 elimination of options and skip questions for free. Because I suck at trivia, I really like that feature and I want to build it. And before this presentation, I already installed Cloud, the Cloud GitHub action on my repo. So it's already available. But we'll go over how to set that up later too. So here's the issue. It has pretty sparse details on how to implement this. It's just literally a wish list, really, like a wish feature. It's saying add a power up option in the config 50-50 elimination for the skip question. It should award user points even though the user skipped. And user should be able to configure this from the config page. So there's a lot of creative room for Cloud to do whatever it wants to do in this case. And I'm excited to see what it actually ends up building. So what I'm going to do is say, at Cloud, please implement this feature and comment on it. So it usually does take four or five seconds for it to respond. And while it's doing that for good measure, we'll just also take this other GitHub issue. This is talking about a per question timer. So we saw there was like a global timer on the quiz app, but there was no per question timer. So that's what this one's talking about. So let's go and say, Cloud, please build this. And now we have two things building. Cool. So now when I get back to this tab, you see that Cloud responded with a comment on this GitHub issue saying that it's working. It also has a link to the job run, which is the GitHub action run. If I click into it, and if I actually click on the logs, I'll see that it's doing a bunch of stuff. You can see all this JSON being output. This is from the SDK. So you want to look at the JSON too much because it's not much fun to parse it manually. But over here, we can see that it also created a 2DList for us. So Cloud is now going to actually go through this 2DList and try to implement the power of feature. And similarly, for the question timer, it's going to do something similar. One more thing that we should do here is there are already a couple of pull requests that have been opened for this repo. And let's get Cloud to review it or change some of these pull requests. Just for fun. Is this one, which is change background color to blue? I actually think I like green better. So I'm just going to be like, all right, Cloud. Please change this to green. This one is fairly easy. And I'm pretty sure Cloud's going to do this. But I just wanted to show you guys that I can also add commits for a pull request that's already open. OK, so this is going to take a few minutes to run. And while this runs, let's go back to the presentation. And then we'll check up on how this is doing towards the end. OK, cool. So let's do a little bit for deep dive on the features of the SDK. When you call Cloud-P, by default, it has no edit or destructive permission access, which is great for safety. But it's now great for actually getting things done. Which is why there is a dash-touch allowed tools option, which allows you to pre-configure Cloud with any permissions that you think it might need in the future for your given task. So in this case, the first example you see that I've given it permissions, bash permissions to NPM run build, NPM test, and the right tool. Which is a good set of permissions, because this allows Cloud to self-verify what it's writing and build your project and test and then continue writing. Similarly, for MCP, if you have MCP servers configured, you can allow this those MCP tools as well. So it's a very similar process. Then, structured output. We already saw an example of structured output, both from the GitHub actions logs and also the little screenshot I showed you earlier. But there's two modes here. There's StreamJSON and JSON. It does exactly what it sounds like. If you select StreamJSON, it'll actually stream messages to you as and when they're available. Versus JSON will just give you one giant blob of JSON at the end. And parsing this JSON and building on top of it is really how you can make use of the Cloud code SDK and then create features for your users. And then you can also configure the system prompt. So you can do dash-touch system prompt, talk like a pirate, and you can get Cloud Code to talk like a pirate for the rest of your day. This is actually quite fun if you haven't done it, I encourage you to try it out. We also have a few user interaction features built into the SDK. And what that means is that the first one is resuming session state. So when you call Cloud-P in structured output or JSON mode, it's going to return a session ID. And this session ID is useful because you can then reference the session ID to go back to the same context state that Cloud had when it finished that process. So by preserving these session IDs and keeping track of them, you can enable or build user interactive features where the user says something, you pass that on to Cloud. Cloud returns a response and now you want the user to give feedback on that response. And that's how this kind of enables you to build those types of interactions on your apps. And this one's actually pretty interesting and it's fairly recent too. It's Dash Dash permission prompt tool. We talked a little bit about how to give Cloud permissions using the allowed tools flag. And that requires you to pre-configure them in advance. But what if you didn't want to do them? Because you don't know what tools Cloud would want to use in the future. In that case, you can use the Dash Dash permission prompt tool and offload the permission management to an MCP server. So you can ask users in real time for whether they want accepted tool or rejected tool. And you can have an MCP server kind of handle that for you as opposed to trying to predict which tools are okay and which tools are not. So this is fairly recent and we'd love to get feedback on this if you guys end up trying it out. Okay, let's go back to our demo and see what Cloud's done. All right, so this is the power up issue. We can see that Cloud has actually gone through his to-do list. Okay, I'm going to open a PS. There's a link over here to create a PR and I'm going to click that and see what that gives us. I'll actually create the pull request too so it's easier for us to review. I don't really know how this code base works but we'll still eyeball it just as you see it's doing the right thing. So you see some set power up stuff. Seems all right. Okay, there's some configuration and the main component. All right, I think what we should do and what we make this fun is if we should just get this branch locally and see what Cloud did because there's no way that we can actually figure out what it did in the short amount of time that we have. So I'm going to go back to my terminal to a good fetch. Check out the branch that Cloud just created and restart our process. Okay, awesome. It looks like we have a power up section now at the bottom of our config page and it's a little check box. I like that touch. We'll keep both of them on and let's select general knowledge and start playing this game. Let's see what it did. Oh, sweet. So you see it has like this little 50-50 button on the bottom left and a skip questions button on the right. I'm just going to with 50-50 because I have no idea what the answer to this is. Does anybody know what that is? D. Okay, there we go. That makes sense. Cadbury, yeah. I'm going to skip this one and then let's just breeze through the other ones for a single time. All right. So we've got an F but we got one correct answer which is better than zero correct answers. Yeah, I guess. Yeah, it tricked us. That was a good one. But yeah, I mean, it seems like it worked. I think there's definitely more we could do here. We could like show how the power, like which questions we use the power upon over here and there's like definitely more we can do. But at the most basic level, I think Claude was able to do the task that we assigned it to do, which is exciting. This is kind of the power of the GitHub action because you don't really have to run this on your own in for you. You can just literally comment on a thread saying, please build this for me. It uses your GitHub action runners and just like does the thing. Let's also look at the PR that we told it change from blue to green. It's all hex code. So let's just see what it did in the commits. So we see there's two commits and Claude has added this last one to switch it from blue to green. And it did it for all three of the places where the color was defined, which is awesome. Okay, I'm not going to go over the last one, the question timer because we might run out of time. But this hopefully gives you insight into what the Cloud GitHub action can do for you. Let's go back to the presentation now. Okay, so just as a recap, the Cloud GitHub action. As it's implemented today is able to read your code. It's able to create PRs for you from GitHub issues like we just saw. It's able to create commits for you. So if you already have a PR and you commit or you comment on it, it can add a commit to an existing branch or an existing PR. It can answer questions. It doesn't have to do something. It can just literally answer questions for you. If you don't understand something, you can be like, Hey, Claude, how does this work? And you can get it to answer questions. And it can of course review your code. The best part of all of this is that you don't have to take care of the infra. It runs on existing GitHub runners, which almost everyone has configured if you're using GitHub actions. So that's kind of the really nice thing about this is you don't have to worry about any of the infra. Okay. So how were the actions built? Right? I think I may have mentioned that these actions were built on top of the SDK. So the SDK does form the foundation of how these actions were built. And then we have two other actions on top. We have the Claude base action. This is a thin layer that just, it just implements the piece which talks to Claude and returns the response from Claude code. And then we have another action on top of this, which is called the PR action. And this action is responsible for all the fancy things that you saw on the PR. So it's responsible to make in comments for the to-do lists, for rendering it the right way, for adding the PR links, and things like that. So it's kind of three layers in which it's built. Both the base action and the PR action are open sourced. So I would encourage you guys to go have a look, take inspiration from how that works, and maybe that inspires more ideas. Yeah. And then finally, we also, you guys can install the Claude GitHub actions today. The easiest way to do this is to open up Claude code in a terminal in the repo that you want to install it in. And once you open up Claude code, just do slash install GitHub action. And that is going to present you with a nice flow, which guides you through configuring your GitHub action as well as merging it. So the end result of this would be a PR, which would be a YAML file for your GitHub action. And once you merge that in, and you can figure your API keys and things like that, your off-the-racers, and you can go ahead and start tagging Claude and using Claude like we just did right now. So if you're a bad rock or a vertex user, the instructions are a little bit different and the tiny bit more manual. So please have a look at the docs. The docs are pretty comprehensive in helping you set up the GitHub action for both bad rock and vertex. Cool. Finally, resources. These are resources for things that we've talked about today. If you want to snap a picture, go ahead. The open source, three posts for both the base action and the Claude action are here. And we absolutely love your feedback as well. So if you guys have any feedback on the SDK, on the GitHub action, or on Claude code, please go to our public Claude GitHub repo and file an issue there, and someone will have a look and get back to you. Cool. That's all I have for today. Thanks for joining me, and I hope you guys have a good rest of the day.
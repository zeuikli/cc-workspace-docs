# Boris Cherny: Claude Code 創始人的 Agentic 工作流與軟體未來 — Sequoia Capital

**來源**：https://www.youtube.com/watch?v=SlGRN8jh2RI
**頻道**：Sequoia Capital
**上傳日期**：2026（確切日期未知，bot check 阻擋 metadata）
**收錄日期**：2026-05-17
**時長**：約 24:35
**統計**：（metadata 不可用）
**字幕語言**：英文 English（自動生成）

---

## TL;DR

Boris Cherny（Claude Code 創始人）揭示個人工作流核心：`/loop` + routines 是 agentic 時代的新基礎建設，coding 對他已 100% 解決，而組織 DNA 才是 Anthropic 真正難以複製的競爭護城河。

---

## 主要內容結構

#### 1. Claude Code 起源（00:00 → ~04:30）

2024 年底 Boris 加入 Anthropic Labs（小型創新孵化器），與少數幾人建造 Claude Code、MCP、桌面 App。前 6 個月產品幾乎不能用，沒有 PMF。PMF 拐點在 2025 年 5 月 Opus 4 發布，之後每次 model 發布都再次拐點（4.5 → 4.6 → 4.7）。

#### 2. 個人工作流：iPhone 為主的 Agentic Setup（~04:30 → ~09:00）

Boris 主要用 iPhone 工作。Claude App 左側 code tab 有 5-10 個 sessions，每個 session 有多個 agents，當前約數百個 agents；夜間常跑幾千個做深度工作。核心工具是 `/loop`：用 Claude 呼叫 cron 排程重複 job，已有幾十個 loop 在跑，包括：babysit PRs + fix CI、自動 rebase、修 flaky test、每 30 分鐘彙整 Twitter feedback。另有 **routines**（server-side 版 loop，關上筆電仍繼續執行）。

#### 3. Coding 已解決與 Claude Code Codebase（~09:00 → ~13:00）

Boris 自 2026 年起零手寫 code，一天最高紀錄 150 PRs。Claude Code codebase 是純 TypeScript + React（原因：對 model 最 on-distribution，模型能力較弱時語言選擇很重要）。今日模型已能處理任何語言。

#### 4. 未來團隊結構（~13:00 → ~16:30）

跨學科 generalist 崛起：工程 + 設計 + 產品 + 資料科學。Anthropic 全團隊成員（PM、設計師、財務、研究員）全員寫 code。新創比大公司更有優勢，因為可從頭 AI-native 建造。

#### 5. SaaS 生態與護城河變化（~16:30 → ~19:00）

Seven Powers 框架：switching costs 和 process power 護城河被削弱（AI 可以 port 系統、hill-climb 任何流程）；network effects、scale economies、cornered resources 仍有效。未來 10 年新創數量將增加 10x。

#### 6. Q&A：多面向洞察（~19:00 → 24:35）

- **Product vs Model Mix**：現 50/50；隨 model 更好，harness 重要性下降；安全機制（prompt injection、permission mode）會因 model alignment 進步而減少
- **軟體民主化**：類比印刷機——1400 年代印刷機讓識字率從 10% → 70%；軟體 literacy 即將完全民主化；最佳記帳軟體作者是好的會計師，不是工程師
- **Anthropic 的真實領先**：不在模型（同樣的模型對外開放）；在組織 DNA——全員 AI-native 流程，Claudes 透過 Slack 互相溝通，零手寫 code，所有 SQL 由 model 生成
- **Multi-agent orchestration**：目前靠 prompting；4.7 已開始自動發起 loop；長期由 model 決定是否用 local 模型等，工程師不再需要做這類決策
- **MCP 與 computer use**：MCP = knowledge work 整合的通用答案；computer use = 無 MCP 的 catchall；以 4.7 效果已相當好但慢

---

## 關鍵要點

1. **`/loop` 是 agentic 工作流核心**：用 Claude 設定 cron job，讓 agent 定期執行任務（PR babysit、CI 修復、feedback 彙整）；Boris 有幾十個 loop 同時運行。
2. **Routines = server-side loop**：關筆電繼續跑，是 loop 的進化版，已正式推出。
3. **PMF 拐點 = Opus 4（May 2025）**：之前 6 個月幾乎沒有 PMF；每次 model release 都有新的指數成長拐點。
4. **TypeScript + React 選擇原因**：當時 model 能力有限，選 on-distribution 語言才能讓 model 寫好代碼；現在模型已能處理任何語言。
5. **4.7 的 hill-climb 能力**：第一個能「給目標、迭代到達標」的 model；可以自主優化任何 process。
6. **七種護城河的 AI 影響**：switching costs + process power 削弱；network effects + scale economies + cornered resources 仍有效。
7. **組織 DNA > 模型領先**：Anthropic 的真正優勢是全員 AI-native 組織流程，Claudes 透過 Slack 互相協調，這比模型本身更難複製。
8. **軟體民主化印刷機類比**：速度會比 50 年快得多；domain expert（如會計師）將是最佳軟體創造者，而非工程師。

---

## 批判性觀察

1. **「Coding 已解決」的侷限性**：Boris 的視角基於 TypeScript + React 的 on-distribution codebase，Anthropic 規模適中。對於遺留系統、特殊語言（COBOL、CUDA）、或超大型複雜架構，現況差距仍大。
2. **150 PRs/day 的品質標準未定義**：auto-merged PR 與通過嚴格 code review 的 PR 品質差異未討論；這個數字可能在不同組織語境有完全不同意義。
3. **Timeline 預測的歷史可信度**：「一年後 model 會更對齊」「幾年後軟體完全民主化」等預測缺乏可量化基準；AI 領域 timeline 預測歷史上多有延遲，應視為方向指引而非時間表。

---

## 完整逐字稿

> ⚠ 逐字稿較長（5,389 字），已完整收錄。建議用 /context 確認 token 用量。

Okay, I'm excited to introduce our next speaker. Show of hands, who here uses Claude code? Okay, show of hands, who here has Claude code psychosis? Come on guys,

*[clears throat]*

it's okay. It's okay. Um my my my team lovingly says I have Claude code psychosis, which may or may not be true. Um we are delighted to have Boris Cherny with us today. Uh Boris is the creator, the father of Claude code. Um and uh in the process of doing that has just had a front row seat to to reinventing uh the modern way of of software development. Um and we're we're really grateful to you, Boris, for taking the time to speak with us today. We know that um the entirety of software development kind of rests on your shoulders.

So, thank you for taking it out of your time to be with us today. And interviewing Boris is Lauren Reader from our team. Thank you.

*[applause]*

Giving our chairs. Um you took my you took my opening line, Asia. We asked who here uses Claude code. There's a lot of hands. That's awesome. Thank you for joining us, Boris. It's very special to have you here. Um as a roomful of builders, I think you are changing building entirely. And so, I'm very curious to explore how you think about the future of software, coding, and what we should spend all of our free time on. Um but I'll give you a me a tiny bit more background on you so that everyone has a little bit more context.

So, beyond creating Claude code, Boris is very much an engineer's engineer. You were writing a lot of code through your whole career, writing textbooks about code, including programming in TypeScript. Um and I think last time we chatted you hadn't written a single line of code in the last year, or at least so far in 2026, which is quite the change. Um There's also a a little known thing back in middle school, I wrote a guide about uh writing BASIC for TI-83 Plus calculators. And I I just I I searched for it, it's actually still on the internet.

It's extremely embarrassing, so please don't search it. But it

*[laughter]*

exists. We will definitely be finding that. Um so, we're going to do I'm going to start with a few questions here. Maybe we'll start with a little bit of the history of Claude code, how you started it, and then we're going to have a lot of audience Q&A for this one. And so, start thinking about your questions in the back of your head, uh and would love to turn it over to you all soon. Yeah. Um and also real quick, so for people that use Claude code, do people use the CLI mostly? Like okay, majority CLI?

Okay. That's a lot. Majority desktop? Okay. Majority VS code or JetBrains IDE? Okay. That's actually not a lot. Okay. Other? I'm like iOS mostly these days. Yeah.

*[laughter]*

Okay. Cool. Um yeah, so I started Claude code kind of accidentally in a in a lot of ways. Um I joined this team back in late 2024. It was a sort of this incubator within Anthropic called Anthropic Labs. And uh the team kind of served its purpose. Um we created Claude code, uh MCP, and the desktop app. It was a team it was just a few of us. So, very much like innovation team. We built the thing that we wanted to build, we disbanded the team. Uh now the team's actually back together for round two.

Mike Krieger, who's the you know, like the chief product officer at at Anthropic and used to be one of the founders at Instagram, so he's leading that right now. Um so the kind of the the the the reason that I started to work on coding is we felt like there was this product overhang. And I I'm guessing people here use that word a lot. Uh but we definitely use this word a lot in kind of within the lab. Uh there's this idea that the model can do all the stuff that no product has yet captured.

And in late 2024, when we were looking at coding, the way that we did coding, the state of the art at the time was type ahead. It was you open your IDE and you press tab and you can like complete like one line at a time. And that was the thing that Sonnet 3.5 enabled for the first time. But the feeling was we could actually go a lot further than that. And the model was almost ready for the next big step. So, we don't have to do type ahead anymore, we can just have the agent write all of the code.

And so, I built it, and it just really didn't work for the first 6 months. It was like not very good. It was barely usable. I wrote it from I used it for maybe 10% of my code or something like that. And even after we released Claude code initially, it was not a hit. There's a lot of people that used it, but it did not have this exponential growth that it has today. Um that started with Opus 4 in May. And I I remember that very clearly. That's like when the exponential growth started, and then it kind of inflected with every model release.

Uh like it started with Opus 4, then 4.5, then 4.6, now 4.7. It just kind of keeps inflecting. But essentially, we were trying to build this thing that was like pre-PMF, and we knew that it wouldn't have PMF for 6 months because we were building for the next model. And that was the idea the pretty much the whole time. And you know, for Anthropic in general, we've always just been very focused. We've always cared about business and enterprise and safety and coding. That's just always been kind of the way that we wanted to build. And so, at some point we kind of knew that we wanted to build a product.

We didn't know exactly what we wanted. So, this kind of ended up being the the product bet. It's an incredible story, especially that it was an accident. Um so, you've said on the record that you think coding is solved. Uh if this is one of the three best from Anthropic, can you tell us more about what you mean by that, and what might still not be solved, or what second-order problems might come? All right. I can ask another question for the room. Who writes 100% of their code by hand? Who writes 100% of their code using a agent like Claude code?

Okay. Who's like somewhere in between? Okay. So, like 50% solved.

*[laughter]*

I mean, for me it's for me it's like for me it's 100%. Like the the Claude code code base, um you know, it leaked, so you know, people know. Uh it's pretty simple. It's just like TypeScript and it's React. Like there's no big secret. There's there's nothing really complicated. The the reason we picked TypeScript and React is it's very on distribution for the model. So, when we started, you know, building the code base, the model was not as intelligent as it is today, so the language and the framework mattered a lot. Nowadays, you know, it can write whatever, and it can pick up new languages, new frameworks it hasn't seen.

But back then, you wanted to use something pretty on distribution. Because of that, I think fairly early we got to the point where the model just wrote 100% of the code. And for us, this happened sometime in October, November last year. And so, for me today, you know, like the model writes 100% of my code. I write somewhere, you know, usually a few dozen PRs every day. Uh there was a day last week I did like 150 PRs in a day. That was like that was a record. I was just trying to kind of push to see how far I can get it.

Um but yeah, it's like for me for me it's just solved. Um but this is not the case everywhere. There's very big complicated code bases. There's kind of weird languages the model's not good at yet. Um and you know, as everyone here knows, it's it's getting there. Usually the answer is just wait for the next model. Can you actually tell us about your personal setup? You walked us through it the other day. It is pretty wild. Yeah. Um so, I shared my personal setup like 6 months ago or something on on Twitter. And it it's funny, I actually I shared it I didn't realize that it would be surprising for anyone.

That was just like the way that I coded.

*[laughter]*

And it's changed since then. It's changed. Um and so, now actually most of my work I do from my phone. Um and so, I don't know if like you guys won't be able to see this, but I have um so, I have like the Claude app, and if you open the Claude app, on the left-hand side, there's this little code tab, and I just have a bunch of sessions going. Um you you probably can't see it. How many sessions? Uh usually have like maybe like five to 10 sessions. Uh and then the sessions usually have a bunch of agents, so I think currently probably like a few hundred agents going.

Um usually every night I have like a few thousand that are doing kind of deeper work. There's a few ways to manage it. One is that you ask Claude to use a bunch of sub-agents to do work. Actually, the the thing that I've been finding myself using more and more is the loop. So, this is {slash} loop, and it's just like the coolest thing. It's like the simplest thing that works. All it is is you have Claude use cron to schedule a job for some point in the future, and it's a repeat job. And it can run every every minute, every 5 minutes, every day, kind of however often you want to schedule it.

And at

*[snorts]*

this point, I have like dozens of loops that are running for stuff. So, I have one that's babysitting my PRs, like fixing CI, auto-rebasing. I have another one that keeps CI healthy. So, like if there's like a flaky test or whatever, it'll it'll go and fix it. Um I have another one that grabs uh feedback from Twitter and kind of clusters it for me every 30 minutes. So, I just have a bunch of these loops running at any time. I sort of feel like loops are the future at this point. If you haven't experimented with it, highly highly recommend it.

And we also just launched routines, which is the same thing but kind of on the server. So, even if you close your laptop, it it keeps going. So, that's your personal setup. Tell us about what you think teams will look like in the future. How do you extrapolate from all the work you're doing to keep everyone on the team moving forward, understanding the context, or do you think we need to let go of a lot more to agents to make it work? Um I think so I you know, it's like it's so hard to make predictions, but um I'm here to make predictions, so I'll try to make some.

I I I feel like the way that things are going is generally there's going to be a lot more generalists than there are today. And today when we talk about generalists, I think largely we're talking about people that are still engineers. So, they're still writing code, but maybe they're kind of product engineers. So, maybe when we say generalist, it's like a you know, they do iOS and web and server, for example. That's like a generalist in engineering. But I think the thing that we're going to start to see a lot more of is generalists that are cross-disciplinary.

So, this is engineers that are really good at product engineering, but also really great at design. Or really great at product and data science and engineering. Um I don't know. It's it's something that we're starting to see on our team. So, actually like a lot of people on the Claude code team are generalists across disciplines. Everyone on our team codes. So, like our engineering manager, our product manager, our designers, our data scientist, our finance guy, our user researcher, every single person on our team writes code. And so, you know, like they're specialist in something, but now also everyone's just coding.

And you know, I'm seeing some nods, but I bet also it's actually not that surprising to people in this room cuz I bet you're seeing the same things. Um

*[clears throat]*

I'll have one more favorite questions then we'll open up to the audience. So, we talked a bit about what's changing with coding. I'm curious about what you see changing in the world of software or software products. Um I think as we see AI making writing code 10 or 100x cheaper, what happens to the value of the products that are produced with software? Do we have a SAS apocalypse on our hands? How do you think this plays out? And again, you're going to have to make another prediction. The SAS apocalypse question is my favorite question then.

Um I think there's two things that are going to happen and I I don't think either of them is the thing that people have been talking about. I think one is Is anyone here an acquired listener? Like the acquired podcast? Yeah, it's like the best podcast. Uh I actually I I got to do a unplugged with them the other week and I I just I I felt like I got to like meet my heroes cuz they're they're just like the hosts are the best. So, they have this idea of uh seven powers and and this is a this is like Hamilton.

He kind of wrote he wrote a book about this and this is kind of the seven modes in business. And I think what's going to happen is because of AI, some of these modes are going to get more important and some are going to get less important. And so, like for example, one that gets less important is uh switching costs because you can just use the model and you can kind of port from one thing to a different thing. Another one that gets less important is process power because for companies whose mode is like workflows and process and things like this, Claude is getting really good at figuring out process.

And especially with 4.7, it can just hill climb anything. So, if you give it a target and you tell it to iterate until it's done, it will just do it. I think this is the first model like that. So, I think these are going to get less important, but I think the previous modes actually still matter. So, this is like network effects, uh scale economies, cornered resources, things like that. These are not really changing with AI. I think the second thing is if you look at the number of startups today or like maybe in the next you know, the past 10 years, I think the number of startups in the next 10 years that are just going to like disrupt everything is going to increase like 10x.

Because right now you can be a tiny startup, you could build a thing that's as valuable as a large company and you can actually compete head-to-head because the large company has to evolve their business process, they have to evolve the way they work, they have to retrain everyone to use technology, they're going to face a lot of internal resistance to that. But you know, no one here has that problem. If you're starting fresh, then you can kind of build with AI natively from the ground up. So, I don't know. I I think it's the best time to build.

It's the best time to be a startup. It's there's so much disruption coming. So, there is hope for us after all. Thank you, Boris. Um I would love to open up to audience questions if anyone has anything they would like to ask. Dan? I Yeah, I'm curious. Um you said that you built uh 6 months before there was product market fit, but now given that the models are good enough, how much do you attribute the success of Claude code to the model versus like product decisions in the the like field of product? Uh I think it's probably a mix.

Yeah, I think it's a mix. I think I think if you asked me maybe a year ago, the ratio was maybe something like 50/50. Um maybe I don't know. If you asked me 6 months ago, the mix would be 50/50. What about in 2 years? Oh, 2 year I don't know, dude. We plan in like we plan in 1 week out. months. Sometime in the future.

*[laughter]*

And by the way, I think the reason it was 50/50 is um you know, I I I like I I did YC back in the day. I was like the first hire at a YC company and like I did a bunch of startups. And in startups like the thing that they drill into you and then especially in YC over and over is build something people love. And so, it it doesn't matter what the product is, it doesn't matter like the model and all this stuff. You still in the end have to build a thing that people love.

And I think that's that's why the product matters is we we pay so much attention to the little details so that as you use it all day, it's a really great experience. I think as the model's gotten better, the harness kind of gets less important. And I I think like I think that we're thinking about right now is like how do we evolve the harness? So, like how do we make loops more of a first class thing? How do we make it easier to run a lot of agents? Uh you know, beside you know, like sub agents is one idea.

There's a bunch more stuff that we're cooking. But I think in a year, the model will be much better aligned. And so, all the safety mechanisms that we have today around uh prompt injection and kind of static verification of commands and uh permission modes, human in the loop, all this kind of stuff is just going to be less important cuz the model will just do the right thing. Um So, yeah, that's that's my prediction. Thank you. You want to toss the box, Dan?

*[snorts]*

Great. Um To zoom to zoom out a little bit from software, I think Claude code did a cultural change a few months ago where it democratized like building software. You can see uh shop owners building their own um software for themselves or even uh programming microcontrollers to control the light when someone opens the door. Um do you see in the future um building software becoming a skill like uh I know uh Microsoft Office? Um so, it's a thing that ev- everybody can do, not just people in the tech industry? Oh my god, yes. Yes. Yes.

I I I think it's going to be even more than that. I think it's going to be I don't know. It's going to be a skill like yeah, like I know how to send a text message. I I I think um you know, like I I read a my my two genres are essentially sci-fi and tech history. This is what I read a lot of. I I think in tech history, there's one thing which I think to me is the clearest parallel for what's happening right now. And this is in the 1400s, the printing press in Europe.

And what what happened was before the printing press, essentially 10% of the European population was literate. They knew how to read and write. They were often employed by like kings and lords that were not literate. And their job was to you know, their their job was to read and write and this is not something that everyone knew how to do.

*[snorts]*

The printing press was invented, then there were two more presses and in the 50 years after the first printing press, there was more literature published in Europe than in the thousand years before. And over the same period, the cost of literature, the cost of a book went down like a 100x. And then, you know, it took a couple hundred years cuz you know, learning to read and write is hard. You need education systems and government and everyone can't be working on farms and so on. But over the next few hundred years, literacy globally went up to like 70%.

And so, you know, now we can all read and write and you don't need a a degree in reading and writing to know how to read and write. Although still there are professional writers and that is a thing that you can do. So, I I think the thing that's about to happen and it's going to be much faster than 50 years is software will be a thing that is fully democratized, that anyone can do. And you know, there's a lot of corollaries to this. So, for example, let's say you're writing accounting software. The best person to write accounting software, I think maybe even today, is not an engineer, it's a really good accountant because they know the domain really well and coding is the easy part.

It's knowing the domain that's the hard part. And I I think this is just obviously the the future. So, uh one of the things Greg said was that you guys are living in the future a little bit cuz you get to have access to the models and the agents. Claude code was an internal tool before you released it. Um is the gap between where you guys are in engineering and the rest of the world, is that a month? Is it 3 months? Is it 6 months? And is that is that gap getting bigger or smaller over time?

Yeah, so so internally, we use the same models everyone else does. Um for us, the dog fooding is really really important. So, we use the thing that everyone else here does. Um you know, we use like a little bit of mythos to try it and then we use a lot of Opus 4.7 to to dog food it and to write most of our code. Um I think on the model side, there isn't really a gap. Um you know, it's like it's pretty much mythos and you know, that will become some version of some descendant of that will become available at some point to everyone.

I think on the product side, there's probably a far larger gap. And that's just related to us changing all of our processes. Like if you talk to people at Anthropic, we use Claude for literally everything. And our Claudes are talking all day like as as I'm coding, as my Claudes are coding in a loop, they will communicate over Slack to talk to other people's Claudes that are also running in a loop to kind of figure out unknowns. We have no more manually written code anywhere at the company. All of the SQL is written by uh by models.

Everything is just built by the models. So, I I I think actually the place that we're ahead is not the technology cuz the same technology available to us is available to everyone here because fundamentally, we are building a platform. And so, for us, it's really important that developers can use the same thing that we're using and that we we dog food everything that we put out there. But I think there's actually a far bigger weed in kind of the organizational structure and organizational process. And this is a place where you know, hopefully we can talk about it in places like this and uh everyone can kind of learn from it and and also evolve.

Yeah, and I think that's one of the advantages startups have. It's so much easier to start there. Jared? Yeah, um last time we talked, I think I think you'd mentioned we talked a little bit about multi-agent and it was very in code at the time at a prior Sequoia event and you mentioned that there were some things going down the pipeline and thing you're talking you're thinking about. Now obviously there's slash batch, there's slash loop, there's sub teams, there's teams. Can you speak some to either at the model level and at the harness level, how you're injecting priors in the harness level, how the objective function is changing the model level to kind of make this experience around delegating work, spinning up agents better?

Cuz so much of the work is parallelizable. You can do so many things so much faster and I feel like I have to overlay my own intuition for when to parallelize things rather than the model kind of understanding that you can spin up 10 sub agents for something. Yeah, I mean on on the product side, it really just comes down to prompting. That's That's how it is. And so, you know, we we tweak prompts to kind of help the model do stuff in parallel more. But also, honestly, as the model gets better, it just naturally does this.

And so, something like loop, I found actually 4.7, it just starts doing. Uh which is really cool. It's like it does something like uh you know, I'll I'll I'll tell it, "Go uh pull this data query." And it's like, "Hey, I noticed that the data is changing over time. I'll start a loop and I'll give you a report every 30 minutes." And I'm like, "Great. Can you send it to me over Slack?" And then it uses the Slack MCP to do that. So, so I think actually over time, it's not on users to figure out how to hold the tools better.

And if that's the case, it's actually a product design problem and like I'm not doing a good job. It's really on the model to do this stuff better and on us kind of prompting it so it naturally does this. Um so, right now it seems like a lot of us use um like Claude or Codex or these uh tools in the cloud to do a lot of our computing. But then, there are some very vocal advocates of uh having your AI be local. And I could imagine over time as um open way models and other things catch up that this could be more of a possibility for people get really high-quality coding assistance.

So, I'm curious your vision of say over the next like years or something like that. Do you see the trajectory of everyone still really relying on the like cloud centralized compute or uh is there a pivot to oh, we all just have our local agents that we can rely on and they don't get throttled and other benefits? Yeah, I think it um I don't know. There's maybe a few ways to answer that. I think maybe like kind of the the most fundamental way to answer that is it doesn't matter. Cuz Cuz I think now we're getting to the point where the model is just able to figure it out.

So, I think like by a couple years from now, the model is just going to be doing all the code. It's going to be starting the agents. It's going to be building the environments. And so, like if it decides like actually I'll use like local models to do this, then you know, that's what it'll do. These I I don't think these will be decisions that we are making as engineers anymore. We have time for a couple more questions, so I can toss this out. Jamie. Nester. Thank you. It feels like one of the great uh decisions with Claude Code was making use of the fact that a lot of developers' tools and workflows are local.

But um that isn't necessarily always the case for sort of general knowledge work with, you know, cloud tools. I'm curious how you're thinking about this with Co-work of how do you give Co-work enough access to the tools that we use to be powerful the same way that Claude Code is for developers? Yeah, it's That's a really great question. Um I know I know when I was uh when I was at a big company, we took like 5 years moving all the environments to remote. It's just like so much work, especially at a big scale. Um but for knowledge work, largely, it's there already with like Salesforce and Docs and things like that.

Um for us, it's always just the simplest answer. It's just MCP. So, the same MCP connector that you have in Claude AI, you hook up like, you know, Salesforce, you hook up Google Docs, Google Calendar. Uh and then Co-work can use that. Claude CLI can use it. Claude Code everywhere can use it. And for the for the systems that don't have MCPs, like do you think that's where computer use is going to be a big opportunity? Yeah, I think computer use is kind of a catchall. Um so, I think currently, for as far as I know, I think Anthropic is like pretty far ahead on computers.

And so, like if you use it through Co-work, it's quite good. Um so, it's able to use pretty much any piece of software that you have on your computer. It's very slow, but it does it quite well now, especially with 4.7. Um Yeah, but I think I think otherwise like MCP is is kind of the answer. It's And you know, all this stuff just doesn't matter that much. It could be MCPs, APIs, just some sort of programmatic access cuz the the model doesn't care. It's to mo- To the model, it's just tokens. All right, we have time for one more question.

Um Ryan. Sean, do you want to toss the Thank you. Um you've kind of alluded to this, but if like sometime ago you saw the probabil- the product overhang and thought to build a product that would then become more interesting once models got better, could you just talk even in vague terms about the shape of a product you'd build today that you think could becomes a much more interesting as models get better in 6 months to a year? Yeah, Claude design I I think is a really good example. It's uh it's pretty good today. It's going to get a lot better.

Um there's also a few things that we're cooking up for Claude Code uh that are going to be landing over the coming weeks. So, you'll see those. Um and then I think uh I think loop and batch and things like this around like massively parallelizing agents, that's going to get better. And computer use is another good one. All right, Boris. Thank you so much for joining us. I think we'll be here for a little longer if anyone has questions.

*[applause]*

Thanks, guys.

---

## 評分

| 維度 | 分數 | 說明 |
|------|------|------|
| A. Workspace 可行動性 (30%) | 9/10 | `/loop` + routines 可立即操作；具體 use case（babysit PR、fix CI、彙整 feedback）直接可複製 |
| B. 創新性 (20%) | 8/10 | Loop-as-future 框架、Claudes 互通 Slack、印刷機類比，多個原創視角 |
| C. 證據品質 (20%) | 8/10 | 一手來源（Claude Code 創始人），具體數字（150 PRs/day、6 months 無 PMF），但前瞻預測缺基準 |
| D. 技術深度 (15%) | 7/10 | Loop/cron 機制、on-distribution 語言選擇、prompt injection 提及，缺深度實作細節 |
| E. 泛化性 (15%) | 8/10 | 印刷機類比與 Seven Powers 框架普遍適用；loop 策略對任何 Claude Code 用戶都有效 |
| **加權總分** | **8.2/10** | 9×0.3+8×0.2+8×0.2+7×0.15+8×0.15 |

**整合決策**：Rule  
**理由**：核心洞察（loop-as-future、組織 DNA、軟體民主化）是可跨 session 沿用的通用原則，比技術 SKILL 更耐久。

# Andrej Karpathy: From Vibe Coding to Agentic Engineering — Sequoia Capital

**來源**：https://www.youtube.com/watch?v=96jN2OCOfLs
**頻道**：Sequoia Capital
**上傳日期**：2026-04-29
**收錄日期**：2026-05-17
**時長**：29:49
**統計**：924,364 views · 21,503 likes
**字幕語言**：英文 (English)（字幕）
**片段數**：322

---

## 核心摘要

> Andrej Karpathy 在 Sequoia Capital 演講中闡述從 Vibe Coding 到 Agentic Engineering 的典範轉移：AI 不只是更好的工具，而是 Software 3.0 新的計算範式，開發者角色從「寫 code」轉為「導演」。

### 一句話總結

AI 助理的質變發生在 2024 年 12 月，Karpathy 宣告軟體正進入 Software 3.0 時代——提示詞取代程式碼，開發者成為管理 AI Agent 的導演，唯一無法外包的是「理解力」。

---

### 主要內容結構

#### 1. Vibe Coding 的質變時刻（00:02 → 02:30）

Karpathy 描述 2024 年 12 月的關鍵轉折：AI 不再只是「輔助片段」，而是整個工作流程都能 coherently 完成。他開始「信任系統」，無限制地提出要求，結果都 OK。這次轉變是「stark transition」——不是漸進式，而是突然質變。

#### 2. Software 3.0 框架（02:30 → 08:00）

- **Software 1.0**：寫明確的程式碼
- **Software 2.0**：用資料集訓練神經網路（程式設計轉為資料排列）
- **Software 3.0**：提示詞即程式語言，context window 是對 LLM 解譯器的控制桿

**實例**：OpenClaw 安裝腳本從 bash script 變成「複製這段文字給你的 Agent」，因為 Software 3.0 不需要精確列出每個細節。

#### 3. Agentic Engineering 的四層架構（08:00 → 16:00）

Karpathy 提出 agentic coding 的關鍵要素：

| 元素 | 說明 |
|------|------|
| **CLAUDE.md / Agent Notes** | 給 Agent 的 README，讓 Agent 了解 codebase 慣例與規則 |
| **Verify loop** | 讓 Agent 自我驗證工作（run tests、linter、server checks）|
| **Tool use** | 給 Agent 正確工具集（file read/write、bash、search）|
| **Context management** | 保持 context window 精簡，避免 hallucination 累積 |

**核心觀念**：像帶領一個優秀但健忘的實習生——需要清楚的指令、驗證機制、以及 context 管理。

#### 4. 開發者角色轉型（16:00 → 22:00）

> "You're a manager of these AI agents... your job is to correctly identify bugs, correctly assign tasks, and correctly verify the outputs."

新技能組合：
- **規格撰寫**（Specification writing）：清楚描述「做什麼」比「怎麼做」更重要
- **測試設計**：能辨別 Agent 輸出是否正確
- **系統除錯**：理解整個 agentic pipeline 而非單一函式
- **Task decomposition**：把大問題分解成 Agent 能執行的小任務

#### 5. 知識庫與個人 Wiki（22:00 → 27:00）

Karpathy 分享個人工作流：每讀一篇文章就更新個人 wiki，讓 LLM 做「synthetic data generation over fixed knowledge」。這樣做讓他能跨時間積累洞察，並用不同角度提問同樣的知識庫。

> "You can outsource your thinking, but you can't outsource your understanding."

LLM 不擅長「理解」，理解力仍是人類的核心競爭力，也是 directing agents 的基礎。

#### 6. 未來展望（27:00 → 29:44）

- AI Agent 將能自主閱讀程式碼、寫 CLAUDE.md、撰寫規格
- 「如果 AI 能代替我理解，我會很樂意被自動化掉」
- Tools 幫助增強理解，不是取代——knowledge bases、wiki、多角度投影是關鍵

---

### 關鍵要點（可直接行動）

1. **建立 CLAUDE.md**：在每個 repo 寫 Agent README，說明慣例、禁止事項、驗證步驟
2. **設計 verify loop**：讓 Agent 執行 `npm test`、`pytest`、`lint` 後才回報完成
3. **規格先於實作**：把 10 分鐘寫在規格上，可省 Agent 多輪往返
4. **Context 管理**：定期清除 context（`/compact`），長任務用 subagent 隔離
5. **個人 wiki**：每讀文章更新知識庫，讓 LLM 對同一知識做多角度分析
6. **Task decomposition**：一次給 Agent 一個明確任務，不要塞複合指令
7. **保留理解力**：外包 coding 但不外包「為什麼這樣做」的判斷

---

### 批判性觀察

- **對非技術導演的門檻估計偏低**：Karpathy 的「任何人都能 vibe code」論點建立在他本人有深厚 CS 背景能 verify outputs 的基礎上；沒有驗證能力的人仍面臨「無法辨別好壞 output」的根本問題
- **Software 3.0 框架過度樂觀**：prompt 仍是脆弱的——context rot、hallucination、tool misuse 是真實生產問題；他的 agentic engineering 實際上要求比 software 1.0 更高的系統思維
- **「理解力是最後防線」立場前後矛盾**：一方面說 LLM 不擅長理解，另一方面又說 AI 遲早會取代理解——這個矛盾在演講中未被解決

---

## 逐字稿（含時間戳）

**[00:02 → 00:07]** We're so excited for our very first special guest. He has helped build modern AI,

**[00:07 → 00:16]** then explain modern AI, and then occasionally rename modern AI. He actually helped co-found OpenAI right

**[00:16 → 00:22]** inside of this office, was the one who actually got autopilot working at Tesla back in the day.

**[00:22 → 00:30]** And he has a rare gift of making the most complex technical shifts feel both accessible and inevitable.

**[00:30 → 00:36]** You all know him for having coined the term vibe coding last year, but just in the last few months he said something

**[00:36 → 00:41]** even more startling, that he's never felt more behind as a programmer.

**[00:41 → 00:46]** That's where we're starting today. Thank you, Andre, for joining us. Yeah, hello. I'm excited to be here and to kick us

**[00:46 → 00:50]** off. Okay, so just a couple months ago you said that you've never felt more behind

**[00:51 → 00:56]** as a programmer. That's startling to hear from you of all people. Um can you help us unpack that? Was that feeling

**[00:57 → 01:05]** exhilarating or unsettling? Uh yeah, mixture of both for sure. Uh well, first of all, um

**[01:05 → 01:09]** I guess like as many of you I've been using agentic tools like Alpha code adjacent things uh for a while, maybe

**[01:09 → 01:14]** over the last year as it came out. And it was very good at, you know, chunks of code. And sometimes it would mess up and

**[01:15 → 01:20]** you have to edit them, and it was kind of helpful. And then I would say December was this uh clear point where

**[01:20 → 01:26]** for me uh I was on a break, so I had a bit more time. I think many other people were similar. And uh I just start to

**[01:26 → 01:30]** notice that with the latest models uh the chunks just came out fine. And then I kept asking for more, and just came

**[01:31 → 01:36]** out fine. And then I can't remember the last time I corrected it. And then I was I just uh you know, trusted the system

**[01:36 → 01:39]** more and more. And then I was vibe coding. &gt;&gt; [laughter]

**[01:39 → 01:44]** &gt;&gt; And uh so it was kind of a I do think that it was a very stark transition. I think that a lot of people

**[01:44 → 01:51]** actually I tried to I tried to stress this on uh Twitter and or X because I think a lot of people experienced AI uh

**[01:51 → 01:57]** last year as ChatGPT adjacent thing, uh but you really had to look again, and you had to look as of December uh

**[01:57 → 02:02]** because things have changed fundamentally and uh especially on this like agentic coherent workflow that

**[02:03 → 02:10]** really started to actually work. Um and so I would say that um yeah, it was just that realization that

**[02:10 → 02:15]** really uh had me um go down the whole rabbit hole of just, you know, infinity side

**[02:15 → 02:21]** project. Uh my side projects folder is like extremely full with lots of random things and uh just I've been coding all

**[02:21 → 02:26]** the time. Uh so uh yeah, that kind of happened in December, I would say. And I was looking at the repercussions

**[02:26 → 02:32]** of that since. Um you've talked a lot about this idea of LLMs as a new computer. Um that it

**[02:32 → 02:40]** isn't just better software, it's a whole new computing paradigm. And um software 1.0 was explicit rules, software 2.0 was

**[02:40 → 02:48]** learned weights, software 3.0 is this. Um if that's actually true, what does a team build differently the day they

**[02:48 → 02:55]** actually believe this? Right. So uh yeah, exactly. So software 1.0 I'm writing code, software 2.0 I'm

**[02:55 → 03:00]** actually programming by creating data sets and training uh training neural networks. So the programming is kind of

**[03:00 → 03:05]** like arranging data sets and maybe some objectives and neural network architectures. And then what happened is

**[03:05 → 03:12]** that basically if you train one of these GPT models or LLMs on a sufficiently large set of tasks implicit basically

**[03:12 → 03:17]** implicitly because by training on the internet you have to multitask all the things that are in the data set. Uh

**[03:17 → 03:22]** these actually become kind of like a programmable computer in a certain sense. So software 3.0 is kind of about

**[03:22 → 03:28]** uh you know, your programming now turns to prompting and what's in the context window is your lever over the

**[03:28 → 03:34]** interpreter that is the LLM that is kind of like interpreting your context and uh performing computation in the digital

**[03:34 → 03:40]** digital information space. So I guess um yeah, that's kind of the transition and I think there's a few examples of that

**[03:41 → 03:46]** really drove it home for me and maybe that might be instructive. Uh so for example, when you when Open Claw came

**[03:46 → 03:50]** out when you want to install Open Claw, you would expect that normally this is a

**[03:50 → 03:55]** bash bash script like a shell script. So, run the shell script to run uh to install OpenClaw.

**[03:55 → 04:00]** Um but the thing is that in order to target lots of different platforms and lots of different types of computers you

**[04:00 → 04:05]** might run an OpenClaw, uh this these shell scripts usually ballooned up and become extremely complex. But the thing

**[04:05 → 04:10]** is you're still stuck in a software 1.0 universe of wanting to write the code. And actually the OpenClaw installation

**[04:10 → 04:16]** is a is a copy-paste of a bunch of text that you're supposed to give to your agent. Uh so, basically it's it's a

**[04:16 → 04:21]** little skill of uh you know, copy-paste this and give it to your agent and it will install OpenClaw. And the reason

**[04:21 → 04:26]** this is a lot more powerful is you're working now in the software 3.0 paradigm where you don't have to precisely uh

**[04:26 → 04:31]** spell out, you know, all the individual details of that setup. The agent has its own intelligence that it packages up and

**[04:31 → 04:36]** then it kind of like follows the instructions and it looks at your environment, your computer, and it kind

**[04:36 → 04:40]** of like performs intelligent actions to make things work and debugs things in the loop. And it's just like so much

**[04:40 → 04:46]** more powerful, right? So, I think that's a very different kind of like way of thinking about it. It's just like, what

**[04:46 → 04:51]** is the piece of text to copy-paste to your agent? That's the programming paradigm now. I think one more maybe uh

**[04:51 → 04:57]** example that comes to mind that is even more extreme than that is when I was building um MenuGen. So, MenuGen is this

**[04:57 → 05:02]** idea where you um you come to a restaurant, they give you a menu, there's no pictures

**[05:02 → 05:07]** usually, so I don't know what any of these things are. Uh usually I like 30% of the things I don't have no idea what

**[05:07 → 05:14]** they are, 50%. So, I wanted to take a photo of the restaurant menu and to get pictures of what those things might look

**[05:14 → 05:19]** like in a generic sense. And so, I built I built coded this app that basically lets you upload a photo

**[05:19 → 05:26]** and it does all this stuff and it runs on Vercel and uh it basically re-renders the menu and it gives you like all the

**[05:26 → 05:33]** items and it gives you a picture that it uses an image um you know, generator uh for to basically OCR all the different

**[05:33 → 05:37]** titles, uh use the image generator to get pictures of them and then shows it to you.

**[05:37 → 05:43]** And then I saw the software 3.0 version of this, which is which blew my mind, which is literally just take your photo,

**[05:43 → 05:50]** give it to Gemini, and say use Nano Banana to overlay the the things onto the menu." Uh Uh

**[05:50 → 05:55]** and Nana Banana basically returned an image that is exactly the picture of the menu that I took, but it actually put

**[05:55 → 06:02]** into the pixels, it rendered the different things in the menu. And this blew my mind because

**[06:02 → 06:09]** actually all of my menu gen is spurious. It's working in the old paradigm that app shouldn't exist. Uh and uh yeah, the

**[06:09 → 06:14]** software 3.0 paradigm is a lot more kind of raw. It just um your neural network is doing more and

**[06:14 → 06:20]** more of the work, and your prompt or context is just the image, and the output is an image, and there's no need

**[06:20 → 06:26]** to have any of the app in between. Um so, I think that people have to kind of like reframe,

**[06:26 → 06:31]** you know, not to work in the existing paradigm of what things existed and just think about it as a speed up of what

**[06:32 → 06:35]** exists. It's actually like new things are available now.

**[06:35 → 06:40]** And going back to your programming question, it's not even I think that's also an example of working in the in the

**[06:40 → 06:44]** old mindset because it's not just about programming and programming becoming faster. This is more general information

**[06:44 → 06:51]** processing that is automatable now. So, um it's not just even about code. So, previous code worked over a kind of like

**[06:51 → 06:56]** structured data, right? And uh you write code over structured data. But like for example with my LLM knowledge bases

**[06:56 → 07:01]** project, um uh basically you get LLMs to create wikis for your organization or for you

**[07:01 → 07:06]** in person, etc. This is not even a program. This is not something that could exist before because there was no

**[07:06 → 07:10]** there was no code that would create a knowledge base based on a bunch of facts. But now you can just take these

**[07:10 → 07:14]** documents and uh basically uh recompile them in a

**[07:14 → 07:19]** different way, and uh reorder them, and create something that is uh new and interesting uh as a reframing of the

**[07:19 → 07:26]** data. And so, these are new things that weren't possible. Uh and so, I think this is uh something that I keep trying

**[07:26 → 07:33]** to get back to as to not only what can we do that existed that is faster now, but I think there's new opportunities of

**[07:33 → 07:37]** just things that couldn't be possible before. And I almost think that that's more exciting.

**[07:37 → 07:43]** I love the menu gen progression and dichotomy that you laid out, and I think even I'm sure many folks here followed

**[07:43 → 07:50]** your own progression of programming from last October to early January, February this year. If you extrapolate that

**[07:50 → 07:59]** further, what is the 2026 equivalent for building websites in the '90s, building mobile apps in the 2010s,

**[07:59 → 08:06]** building SaaS in the last cloud era? What will look completely obvious in hindsight that is still mostly unbuilt

**[08:06 → 08:09]** today? Um &gt;&gt; [clears throat]

**[08:09 → 08:13]** &gt;&gt; Well, going with the example of MenuGen, I guess. So, a lot of this code shouldn't exist and it's just neural

**[08:13 → 08:19]** networks doing most of the work. Um I do think that the extrapolation looks very weird because you could

**[08:19 → 08:24]** basically imagine I don't think I Yeah, so you could imagine completely neural computers in a

**[08:25 → 08:31]** certain sense. Uh you feed a raw videos like imagine a device that takes raw videos or audio into basically what's a

**[08:31 → 08:38]** neural net and uses diffusion to render a UI that is kind of like, you know, unique for that moment in a certain

**[08:38 → 08:43]** sense. And um I kind of feel like in the early days of computing actually, people were a little

**[08:43 → 08:48]** bit confused as to whether computers would look like calculators or computers would look like neural nets. And in '50s

**[08:48 → 08:53]** and '60s, it was not really obvious which way would go. And of course, we went down the calculator path and ended

**[08:53 → 08:58]** up building classical computing and then neural nets are currently running virtualized on existing computers. But

**[08:58 → 09:03]** you could imagine I think that a lot of this will flip and that the neural net becomes kind of like the host process.

**[09:03 → 09:09]** And the CPUs become kind of like the co-processor. So, we saw the diagram of, you know, intelligence compute is going

**[09:09 → 09:15]** to neural networks is going to take over and become the dominant spend of flops. So, you could imagine something really

**[09:15 → 09:21]** weird and foreign when where neural nets are doing most of the heavy lifting, they're using tool use as just like, you

**[09:21 → 09:25]** know, historical appendage for some kinds of like deterministic tasks. But what's

**[09:25 → 09:30]** really running the show is these neural nets that are networked in a certain way. Um so, you can imagine

**[09:30 → 09:35]** something extremely foreign as the extrapolation, but I think we're going to probably get there sort of piece by

**[09:35 → 09:40]** piece. And I don't Yeah, I don't that that progression is TBD, I would say.

**[09:40 → 09:45]** &gt;&gt; [snorts] &gt;&gt; I'd love to talk a little bit about um, uh, this concept of verifiability. The

**[09:45 → 09:50]** fact that AI will automate faster and more easily domains where the output can be verified.

**[09:51 → 09:57]** Um, if that framework is right, what work is about to move much faster than people realize? And what professions do

**[09:57 → 10:02]** we have that people actually think are safe, but they're actually highly verifiable?

**[10:02 → 10:09]** Uh, yes, so I I spent uh, some time writing about verifiability and um, basically like traditional computers can

**[10:09 → 10:15]** easily automate what you can specify in code. And uh, kind of this latest round of LLMs can

**[10:15 → 10:20]** easily automate what you can uh, verify in a certain in a certain sense. Uh, because the way this works is that when

**[10:20 → 10:25]** frontier labs are training these LLMs, these are giant reinforcement learning environments. So, they are given a

**[10:25 → 10:30]** verification rewards. And then because of the way that these models are trained, they end up basically uh,

**[10:30 → 10:36]** progressing and creating these like jagged entities that really peak in capability in kind of like verifiable

**[10:36 → 10:41]** domains like math and code and adjacent. And kind of like stagnate and are a little bit um,

**[10:41 → 10:46]** you know, rougher on the edges when uh, things are not kind of like in that in that space. So, I think the reason I

**[10:46 → 10:50]** wrote about verifiability is I'm trying to understand why these things are so jagged.

**[10:50 → 10:55]** Um, and some of it has to do with how the labs train the models, but I think some of it also has to do with um, the

**[10:55 → 11:01]** focus of the labs and what they happen to put into the data distribution. Uh, because some things basically are

**[11:01 → 11:05]** significantly more valuable in economy and end up creating more environments because the labs wanted to work in those

**[11:05 → 11:10]** settings. So, I think code is a good example of that. There's probably lots of verifiable environments they could

**[11:10 → 11:13]** think about that happen not to make it into the mix because they're just not that useful to have the capability

**[11:13 → 11:18]** around. Um, but I think to me the big um, I guess

**[11:18 → 11:23]** like the big mystery is uh, the favorite example for a while was that how many letters are are in a

**[11:23 → 11:27]** strawberry? And the models would famously get this wrong and it's an example of jaggedness. Uh, the models

**[11:27 → 11:34]** now patch this, I think, but the new one is I want to go to a car wash to wash my car, and it's 50 m away, should I drive

**[11:34 → 11:41]** or should I walk? And state-of-the-art models today will tell you to walk because it's so close. How is it

**[11:41 → 11:47]** possible that state-of-the-art Opus 4.7 will simultaneously refactor a 100,000 like

**[11:47 → 11:51]** &gt;&gt; [laughter] &gt;&gt; code base a line code base or find zero-day vulnerabilities and yet tells

**[11:51 → 12:00]** me to walk to this car wash? This is insane. And to whatever extent these models are remain jagged, it's an

**[12:00 → 12:04]** indication that number one, maybe something slightly off. Or

**[12:04 → 12:09]** number two, you need to actually be in the loop a little bit and you need to treat them as tools and you do have

**[12:09 → 12:14]** to kind of stay in touch with what they're doing. And so I think all of my writing, long story short, about

**[12:14 → 12:19]** verifiability is just trying to understand um why these things are jagged, is there

**[12:19 → 12:25]** any pattern to it? And I think it's a some kind of combination of verifiable plus labs care. Maybe one more anecdote

**[12:25 → 12:30]** that is instructive is from GPT-3.5 to GPT-4, people noticed

**[12:30 → 12:35]** that chess improved a lot and I think a lot of people thought, oh well, it's just a progression of the capabilities.

**[12:35 → 12:40]** But actually it's it's more that I think this is public information, I think I saw it on the internet. Um a huge amount

**[12:40 → 12:45]** of like data of chess made it into the pre-training set.

**[12:45 → 12:50]** And just because it's in the data distribution, basically the model improved a lot more than it would just

**[12:50 → 12:55]** by default. So someone at OpenAI decided to add this data and now you have a capability that

**[12:55 → 13:02]** just peaked a lot more. And so that's why I think I'm stressing this dimension of it as we are slightly at

**[13:02 → 13:06]** the mercy of whatever the labs are doing, whatever they happen to put into the mix and you have to actually explore

**[13:06 → 13:12]** this thing that they give you that has no manual and it works in certain settings but maybe not in some settings

**[13:12 → 13:19]** and you have to kind of explore it a little bit and if you're in the circuits that were part of the RL, you fly and if

**[13:19 → 13:24]** you're in the circuits that are out of the data distribution, you're going to struggle and you have to kind of figure

**[13:24 → 13:29]** out which which circuits you're in in your application. And if you and if you're not in the circuits, then you

**[13:29 → 13:33]** have to really look at fine-tuning and doing some of your own work because it's not going to necessarily come out of the

**[13:34 → 13:40]** LLM out of the box. I'd love to come back to the concept of jagged intelligence in a little bit. Um

**[13:40 → 13:46]** if you were a founder today and thinking about building a company, you are trying to solve a problem that you think is

**[13:46 → 13:52]** tractable, something that uh is a domain that is verifiable, but you look around and you think, "Oh my gosh, well the

**[13:52 → 14:00]** labs have really really started uh got getting to escape velocity and the ones that seem most obvious, math,

**[14:00 → 14:05]** coding, and others." What would your advice be to to the founders in the audience?

**[14:05 → 14:11]** Um So, I think maybe that comes to the previous question of I do think that

**[14:11 → 14:17]** verifiability because it um Let me think. So, verifiability makes something tractable in the current

**[14:17 → 14:25]** paradigm because you can throw huge amount of RL at it. Um So, maybe one way to see it is that uh

**[14:25 → 14:30]** that remains true even if the labs are not focusing on it directly. So, if you are in a a verifiable setting where you

**[14:30 → 14:35]** could create these RL environments or examples, then that actually sets you up to potentially do your own fine-tuning

**[14:35 → 14:39]** and you might benefit from that. But, that is fundamentally technology that just works. You can pull a lever. If you

**[14:39 → 14:45]** have huge amount of diverse data sets of RL environments, etc., uh you can use your favorite fine-tuning framework and

**[14:45 → 14:50]** um and uh pull the lever and get something that actually uh works pretty well. So, um

**[14:51 → 14:55]** I don't know what the examples of this might be. Um but I do think there are some very

**[14:55 → 15:00]** valuable uh reinforcement learning environments that people could think of that I think are not part of the

**[15:00 → 15:05]** Yeah, I don't want to give away the answer, but there is one domain that I think is very uh Oh, okay. Sorry. I

**[15:05 → 15:09]** don't mean to vague post on on the stage, but uh there are some examples of this. On

**[15:09 → 15:17]** the flip side, what do you think still feels automatable only from a distance? I do think that ultimately almost

**[15:17 → 15:22]** everything can be made uh verifiable to some extent, some things easier than others. Um

**[15:22 → 15:27]** because even for like things that are like writing or so on, you can imagine having a council of LLM judges and

**[15:27 → 15:33]** probably get get to some get something reasonable out of the from from this kind of an approach. So,

**[15:33 → 15:39]** it's more about what's easy or hard. Um So, I I do think that ultimately um

**[15:39 → 15:43]** Uh yeah, I think uh Everything. &gt;&gt; [laughter]

**[15:43 → 15:49]** &gt;&gt; Everything is automatable. Amazing. Okay. Um so, last year you coined the term vibe coding and today

**[15:49 → 15:53]** we're in a world that feels a little bit more serious, more agentic engineering. What do you think is the difference

**[15:54 → 15:58]** between the two and what would you actually call what we're in today? Uh yeah, so I would say vibe coding is

**[15:58 → 16:04]** about raising the floor for everyone in terms of what they can do in software. So, the floor rises, everyone can vibe

**[16:04 → 16:09]** code anything, and that's amazing, incredible. But then I would say agentic engineering is about preserving the

**[16:09 → 16:15]** quality bar of what existed before in professional software. So, you're not allowed to introduce uh vulnerabilities

**[16:15 → 16:22]** due to vibe coding. Um you are um you're still responsible for your software just as before, but can you go faster? And

**[16:22 → 16:27]** spoiler is you can, but how do you how do you do that properly? And so, to me agentic engineering when I I call it

**[16:27 → 16:32]** that because I do think it's kind of like an engineering discipline. You have these agents which are these like spiky

**[16:32 → 16:37]** entities, they're a bit fallible, a little bit stochastic, but they are extremely powerful. And it's how do you

**[16:37 → 16:45]** how do you coordinate them to go faster without sacrificing your quality bar? And doing that well and correctly um is

**[16:45 → 16:50]** the the realm of agentic engineering. Um so, I kind of see them as as different. Like one is about maybe

**[16:50 → 16:55]** raising the raising the floor, and the other is about um you know, extrapolating. And what I'm seeing I

**[16:55 → 17:01]** think is there is a very high ceiling on agent engineer uh capability. And you know,

**[17:01 → 17:07]** people used to talk about the 10x engineer previously. I think that this is uh magnified a lot more. Uh 10x is uh

**[17:07 → 17:15]** is not uh the speed up you gain. Um and I think uh it does seem to me like people who are very good at this um

**[17:15 → 17:20]** peak a lot more than 10x uh from from my perspective right now. I really like that framing. Um

**[17:20 → 17:26]** one thing that when Sam Altman came to AI sent last year, one memorable thing he said was that people of different

**[17:26 → 17:32]** generations use ChatGPT differently. So, if you're in your 30s, you use it as a Google search replacement, but if you're

**[17:32 → 17:38]** in your teens, ChatGPT is your gateway to the internet. What is the parallel here in coding today? If we were to

**[17:38 → 17:46]** watch two people code using open claw, cloud code, codex, one you'd consider mediocre at it and one you would

**[17:46 → 17:52]** consider fully AI native, how would you describe the difference? I [clears throat] mean, I think it's

**[17:52 → 17:58]** just trying to get the most out of the tools that are available, utilizing all of their features, investing into your

**[17:58 → 18:03]** own kind of setup. So, just like previously, all the engineers are used to basically

**[18:03 → 18:09]** getting the most out of the tools you use, either it's Vim or VS Code or now it's you know, cloud code or codex or so

**[18:09 → 18:14]** on. So, um just investing into your setup and

**[18:14 → 18:20]** utilizing a lot of the, you know, tools that are available to you. Um and I think it just kind of looks

**[18:20 → 18:26]** like that. I do think that maybe related thought is um

**[18:26 → 18:32]** a lot of people are maybe hiring for this, right? Because they want to hire strong agentic engineers. I do

**[18:32 → 18:37]** think that what I'm seeing is that the, you know, most people are still not

**[18:37 → 18:43]** refactored their their hiring process for agentic engineer capability, right? Like if

**[18:44 → 18:49]** you're giving out puzzles to solve, then this is still the old paradigm. I would say that hiring have to has to look like

**[18:49 → 18:55]** give me a really big project and see someone implement that big project. Like let's write, say a Twitter clone

**[18:55 → 19:03]** for agents and then make it really good, make it really secure, and then have some agents simulate some activity on

**[19:03 → 19:09]** this Twitter. And then I'm going to use 10 codex 5.4 x high to try to break your

**[19:09 → 19:15]** break your this website that you deployed and they're going to try to basically break

**[19:15 → 19:20]** it and they should not be able to break it. And so maybe it looks like that, right? And so yeah, watching people in

**[19:20 → 19:26]** that that setting and building some bigger projects and utilize utilizing the tooling is maybe

**[19:26 → 19:33]** what I would look at for the most part. And as agents do more, what human skill do you think becomes more valuable, not

**[19:33 → 19:38]** less? Also, yeah, it's a good question. I think um

**[19:38 → 19:42]** Well, right now the answer is that the agents are catalog these internal entities, right? So

**[19:42 → 19:47]** it's remarkable um you basically still have to be in charge

**[19:47 → 19:52]** of the aesthetics, the the judgment, the taste, and a little bit of oversight. And maybe one one of my favorite

**[19:52 → 19:58]** examples of like the the weirdness of agents is um for menu gen, you sign up with a Google

**[19:58 → 20:04]** Google account, but you purchase credits using a Stripe account and both of them have email addresses.

**[20:04 → 20:10]** And my agent actually tries to basically um like when you purchase credits, it

**[20:10 → 20:18]** assigned it using the email address from Stripe to the Google email address. Like there wasn't a persistent user ID that

**[20:18 → 20:22]** that for people. It was trying to match up the email addresses, but you could use different email address for your

**[20:22 → 20:28]** Stripe and your Google and basically would not associate the funds. And so this is the kind of thing that these

**[20:28 → 20:32]** agents still will make mistakes about. It's like why would you use email addresses to try to cross-correlate the

**[20:32 → 20:38]** funds? They can be arbitrary. You can use different emails, etc. Like this is such a weird thing to do. So I think

**[20:38 → 20:44]** people have to be in charge of this spec, this plan, and actually don't even like the plan mode.

**[20:44 → 20:48]** I would I mean, obviously it's very useful, but I think there's something more general

**[20:48 → 20:53]** here where you have to work with your agent to design a spec that is very detailed and maybe it's a maybe

**[20:53 → 20:58]** basically the docs and then get the agents to write them. And you're in charge of the oversight and the

**[20:58 → 21:03]** top-level categories, but the agents are doing a lot of the under the hood. And so I think you're not caring about some

**[21:04 → 21:11]** of the details. So as an example also with um, a race or tensors in neural networks, um, there's a ton of details

**[21:11 → 21:16]** between PyTorch and NumPy and all the different like pandas and so on for all the different little API details. And

**[21:16 → 21:22]** I'll I already forgot about the keep dims versus keep dim or whether it's dim or axis or reshape or permute or

**[21:22 → 21:26]** transpose. I don't remember this stuff anymore, right? Because you don't have to. This is the kind of details that are

**[21:26 → 21:31]** handled by the intern because they have very good recall. And but you still have to know for example that um, you know,

**[21:31 → 21:37]** there's underlying tensor, there's an underlying view and then you can view of the same storage or you can have

**[21:37 → 21:42]** different storage which will be less efficient. As we still have to have an understanding of what this stuff is

**[21:42 → 21:46]** doing and some of the fundamentals um, so that you're not copying memory around

**[21:46 → 21:53]** unnecessarily and so on. But uh, the details of the APIs are now handed off. So it um, you're in charge of the taste,

**[21:53 → 21:58]** the engineering, the design uh, and that it makes sense and that you're asking for the right things and that you're

**[21:58 → 22:03]** saying that okay, that these have to be unique user IDs that we're going to tie everything to. Um,

**[22:03 → 22:08]** and so you're doing some of the design and development and the engineers are doing the fill in the blanks. And

**[22:08 → 22:13]** that's currently kind of like where we are and I think that's what everyone of course is seeing I think right now. Do

**[22:13 → 22:19]** you think there's a chance that this um, taste and judgment matters less over time or will the ceiling just keep

**[22:19 → 22:25]** rising? Um, yeah, it's a good question. I would say

**[22:25 → 22:30]** um, I mean I'm hoping that the that it improves. I think probably the reason it

**[22:30 → 22:36]** doesn't improve right now is again it's not part of the RL. There's probably no aesthetics cost or reward or it's not

**[22:36 → 22:42]** good enough or something like that. Um, I do think that when you actually look at the code, sometimes I get a little

**[22:42 → 22:46]** bit of a heart attack because it's not like super amazing code necessarily all the time and it's very bloated and

**[22:46 → 22:52]** there's a lot of copy-paste and there's awkward abstractions that are brittle and like it works but it's just really

**[22:52 → 22:57]** gross. Um, and I do I do hope that this can improve in future models. Um, a good example

**[22:58 → 23:04]** also is this uh, you know, the micro GPT project uh, which where I was trying to simplify uh LLM training to be as simple

**[23:04 → 23:10]** as possible. The models hate this. They can't do it. I tried to I keep I kept trying to prompt an LLM to simplify

**[23:10 → 23:16]** more, simplify more, and it just can't You feel like you're outside of the RL circuits. It feels like it you're

**[23:16 → 23:23]** obviously, you know, you're pulling teeth. It's not like light speed. So, I think um

**[23:23 → 23:27]** I do think that people are still remain in charge of this, but I do think that there's nothing fundamental again that's

**[23:27 → 23:31]** preventing it. It's just the labs haven't done it yet almost. Yeah.

**[23:31 → 23:36]** So, I'd love to come back to this idea of uh jagged forms of intelligence. You wrote

**[23:36 → 23:41]** a little bit about this with uh very thought-provoking piece around animals versus ghosts.

**[23:41 → 23:47]** Um and the idea is that we're not building animals. We are summoning ghosts. Um and these are jagged forms of

**[23:47 → 23:54]** intelligence that are shaped by data and reward functions, but not by intrinsic motivation or fun or curiosity or

**[23:54 → 23:59]** empowerment, uh things that kind of came about via evolution.

**[23:59 → 24:06]** Um why does that framing matter? And what does it actually change about how you build and deploy and evaluate or

**[24:06 → 24:11]** even trust them? Uh yes, so

**[24:11 → 24:15]** Yeah, I think the reason I wrote about this is because I'm trying to wrap my head around what these things are,

**[24:15 → 24:20]** right? Because if you have a good model of what they are or are not, then you're going to be more competent at uh using

**[24:20 → 24:27]** them. Um and I do think that um I don't know if it has I'm not sure if it actually has like real power.

**[24:27 → 24:31]** &gt;&gt; [laughter] &gt;&gt; I think it's a little bit of philosophizing.

**[24:31 → 24:37]** But I do think that um I think it's just um coming to terms with the fact that these

**[24:37 → 24:42]** things are not, you know, animal intelligences. Like if you yell at them, they're not going to work better or or

**[24:42 → 24:47]** worse or it doesn't have any impact. Um and uh it's all just kind of like these

**[24:47 → 24:54]** statistical simulation circuits where the the substrate is pre-training, so like statistics. And then but then

**[24:54 → 25:00]** there's RL bolting on top, so it kind of like increases the disadvantages and um maybe it's just

**[25:00 → 25:05]** kind of like a mindset of what I'm coming into or what's likely to work or not likely to work or how to modify it,

**[25:05 → 25:11]** but I don't actually I don't know that I have like here are the five obvious outcomes of how to make your system

**[25:11 → 25:16]** better. It's more just being suspicious of it and um figuring out over time.

**[25:16 → 25:22]** That's where it starts. Okay, so you are so deep in working with agents that don't just chat. They have

**[25:22 → 25:27]** real permissions. They have local contacts. They actually take action on your your behalf. What does the world

**[25:27 → 25:33]** look like when we all start to live in that world? Yeah, I think

**[25:33 → 25:39]** I think a lot of people probably here are excited about what this agentic you know, native agentic environment

**[25:39 → 25:43]** looks like and everything has to be rewritten. Everything is still fundamentally written for humans and has

**[25:43 → 25:49]** to be moved around. I still use most of the time when I use different frameworks or libraries or things like that. They

**[25:49 → 25:55]** still have docs that are fundamentally written for humans. This is my favorite pet peeve. Like I don't Why are people

**[25:55 → 26:00]** still telling me what to do? Like I don't want to do anything. What is the thing I should copy paste to my agent?

**[26:00 → 26:05]** &gt;&gt; [laughter] &gt;&gt; So it's just every time I'm told, you know, go to this URL or something like

**[26:05 → 26:08]** that. It's just like ah. &gt;&gt; [laughter] &gt;&gt; You know.

**[26:08 → 26:11]** &gt;&gt; [snorts] &gt;&gt; So um everyone is I think excited about how do

**[26:11 → 26:17]** we decompose the workloads that need to happen into fundamentally sensors over the world, actuators over the world. How

**[26:17 → 26:26]** do we make it agent native? Basically describe it to agents first. Um and then I have a lot of automation around

**[26:26 → 26:31]** you know, the Yeah, around data structures that are very legible to the LLMs.

**[26:31 → 26:37]** So I think yeah, I'm hoping that there's a lot of agent first infrastructure out there and

**[26:37 → 26:42]** that you know, for MenuGen famously when I wrote the not I'm not sure how famously, but when I wrote the blog post

**[26:42 → 26:47]** about MenuGen [laughter] a lot of the work a lot of the trouble was not even writing the code for

**[26:47 → 26:51]** MenuGen. It was deploying it on Vercel because I had to work with all these different services and I just string

**[26:51 → 26:56]** them up and I just go to their settings and the menus, and you know, configure my DNS, and it was

**[26:56 → 27:03]** just so annoying. And so, that's a good example of I would hope that MenuGen that I could give a prompt to an LLM,

**[27:03 → 27:08]** build MenuGen, and then I didn't have to touch anything, and it's deployed in that same way on the internet. I think

**[27:09 → 27:13]** that would be a good kind of a test for whether or not a lot of our infrastructure is becoming more and more

**[27:13 → 27:17]** agent native. And then ultimately, I would say yeah, I I do think we're going towards a

**[27:17 → 27:26]** world where there's agent representation for people and for organizations, and um you know, I'll have my agent talk to

**[27:26 → 27:31]** your agent to figure out some of the details of our meetings or things like that. So,

**[27:31 → 27:36]** &gt;&gt; [laughter] &gt;&gt; um I do think that that's roughly where things are going, but um yeah, I think

**[27:36 → 27:41]** everyone here is excited about that. I really like the visual analogy of sensors and actuators. I actually hadn't

**[27:41 → 27:44]** thought of that. That's super interesting. &gt;&gt; Right. Um okay, I think we have to end

**[27:44 → 27:50]** on a question about education, um because you are probably one of the very best in the world at making complex

**[27:50 → 27:57]** technical concepts simple and deeply thoughtful about how we design education around it. Um

**[27:57 → 28:05]** what still remains worth learning deeply when intelligence gets cheap as we move into the next era of AI?

**[28:05 → 28:09]** Yeah. Uh there was a tweet that blew my mind recently, and I keep thinking about it

**[28:09 → 28:13]** like every other day. It was something along the lines of um you can outsource your thinking, but you

**[28:13 → 28:21]** can't outsource your understanding. And um I think that's really nicely put. I so

**[28:21 → 28:26]** yeah, because I still I'm still part of the system, and I still I still have to somehow information still has to make it

**[28:26 → 28:30]** into my brain, and I feel like I'm becoming a bottleneck of just even knowing what we're trying to build, why

**[28:30 → 28:35]** is it worth doing, uh how do I direct you know, how do I direct my my agents, and so on. So,

**[28:35 → 28:42]** I do still think that ultimately something has to direct the thinking and the processing, and so on. And um

**[28:43 → 28:46]** that's still kind of fundamentally constrained somehow by understanding. And this is one reason I also was very

**[28:46 → 28:52]** excited about all the all the knowledge bases because I feel like that's that's a way for me to process information. And

**[28:52 → 28:57]** anytime I see a different projection onto information, I always like feel like I gain insight. So, it's really

**[28:57 → 29:01]** just a lot of prompts for me to do synthetic data generation kind of over over some

**[29:01 → 29:07]** fixed data. Uh so, I I really enjoy uh whenever I read an article, I have my uh you know, my wiki that's being built up

**[29:07 → 29:14]** from these articles. And I love asking questions about things or um and I I think that ultimately these are tools to

**[29:14 → 29:19]** enhance understanding in a certain way. And this is still kind of like a bit of a bottleneck because then you can't

**[29:19 → 29:23]** direct the uh you you can't be a good director if you still

**[29:23 → 29:28]** uh cuz the LLMs certainly don't excel at understanding. You still are uniquely in charge of that. So,

**[29:28 → 29:34]** uh yeah, I think uh tools to that effect I think are incredibly interesting and exciting. I'm excited to be back here in

**[29:34 → 29:39]** a couple years and to see if we've been fully automated out of the loop and they actually take care of understanding as

**[29:39 → 29:44]** well. Uh thank you so much for joining us, Andre. We really appreciate it. [applause]

---

## 完整純文字

We're so excited for our very first special guest. He has helped build modern AI, then explain modern AI, and then occasionally rename modern AI. He actually helped co-found OpenAI right inside of this office, was the one who actually got autopilot working at Tesla back in the day. And he has a rare gift of making the most complex technical shifts feel both accessible and inevitable. You all know him for having coined the term vibe coding last year, but just in the last few months he said something even more startling, that he's never felt more behind as a programmer. That's where we're starting today. Thank you, Andre, for joining us. Yeah, hello. I'm excited to be here and to kick us off. Okay, so just a couple months ago you said that you've never felt more behind as a programmer. That's startling to hear from you of all people. Um can you help us unpack that? Was that feeling exhilarating or unsettling? Uh yeah, mixture of both for sure. Uh well, first of all, um I guess like as many of you I've been using agentic tools like Alpha code adjacent things uh for a while, maybe over the last year as it came out. And it was very good at, you know, chunks of code. And sometimes it would mess up and you have to edit them, and it was kind of helpful. And then I would say December was this uh clear point where for me uh I was on a break, so I had a bit more time. I think many other people were similar. And uh I just start to notice that with the latest models uh the chunks just came out fine. And then I kept asking for more, and just came out fine. And then I can't remember the last time I corrected it. And then I was I just uh you know, trusted the system more and more. And then I was vibe coding. &gt;&gt; [laughter] &gt;&gt; And uh so it was kind of a I do think that it was a very stark transition. I think that a lot of people actually I tried to I tried to stress this on uh Twitter and or X because I think a lot of people experienced AI uh last year as ChatGPT adjacent thing, uh but you really had to look again, and you had to look as of December uh because things have changed fundamentally and uh especially on this like agentic coherent workflow that really started to actually work. Um and so I would say that um yeah, it was just that realization that really uh had me um go down the whole rabbit hole of just, you know, infinity side project. Uh my side projects folder is like extremely full with lots of random things and uh just I've been coding all the time. Uh so uh yeah, that kind of happened in December, I would say. And I was looking at the repercussions of that since. Um you've talked a lot about this idea of LLMs as a new computer. Um that it isn't just better software, it's a whole new computing paradigm. And um software 1.0 was explicit rules, software 2.0 was learned weights, software 3.0 is this. Um if that's actually true, what does a team build differently the day they actually believe this? Right. So uh yeah, exactly. So software 1.0 I'm writing code, software 2.0 I'm actually programming by creating data sets and training uh training neural networks. So the programming is kind of like arranging data sets and maybe some objectives and neural network architectures. And then what happened is that basically if you train one of these GPT models or LLMs on a sufficiently large set of tasks implicit basically implicitly because by training on the internet you have to multitask all the things that are in the data set. Uh these actually become kind of like a programmable computer in a certain sense. So software 3.0 is kind of about uh you know, your programming now turns to prompting and what's in the context window is your lever over the interpreter that is the LLM that is kind of like interpreting your context and uh performing computation in the digital digital information space. So I guess um yeah, that's kind of the transition and I think there's a few examples of that really drove it home for me and maybe that might be instructive. Uh so for example, when you when Open Claw came out when you want to install Open Claw, you would expect that normally this is a bash bash script like a shell script. So, run the shell script to run uh to install OpenClaw. Um but the thing is that in order to target lots of different platforms and lots of different types of computers you might run an OpenClaw, uh this these shell scripts usually ballooned up and become extremely complex. But the thing is you're still stuck in a software 1.0 universe of wanting to write the code. And actually the OpenClaw installation is a is a copy-paste of a bunch of text that you're supposed to give to your agent. Uh so, basically it's it's a little skill of uh you know, copy-paste this and give it to your agent and it will install OpenClaw. And the reason this is a lot more powerful is you're working now in the software 3.0 paradigm where you don't have to precisely uh spell out, you know, all the individual details of that setup. The agent has its own intelligence that it packages up and then it kind of like follows the instructions and it looks at your environment, your computer, and it kind of like performs intelligent actions to make things work and debugs things in the loop. And it's just like so much more powerful, right? So, I think that's a very different kind of like way of thinking about it. It's just like, what is the piece of text to copy-paste to your agent? That's the programming paradigm now. I think one more maybe uh example that comes to mind that is even more extreme than that is when I was building um MenuGen. So, MenuGen is this idea where you um you come to a restaurant, they give you a menu, there's no pictures usually, so I don't know what any of these things are. Uh usually I like 30% of the things I don't have no idea what they are, 50%. So, I wanted to take a photo of the restaurant menu and to get pictures of what those things might look like in a generic sense. And so, I built I built coded this app that basically lets you upload a photo and it does all this stuff and it runs on Vercel and uh it basically re-renders the menu and it gives you like all the items and it gives you a picture that it uses an image um you know, generator uh for to basically OCR all the different titles, uh use the image generator to get pictures of them and then shows it to you. And then I saw the software 3.0 version of this, which is which blew my mind, which is literally just take your photo, give it to Gemini, and say use Nano Banana to overlay the the things onto the menu." Uh Uh and Nana Banana basically returned an image that is exactly the picture of the menu that I took, but it actually put into the pixels, it rendered the different things in the menu. And this blew my mind because actually all of my menu gen is spurious. It's working in the old paradigm that app shouldn't exist. Uh and uh yeah, the software 3.0 paradigm is a lot more kind of raw. It just um your neural network is doing more and more of the work, and your prompt or context is just the image, and the output is an image, and there's no need to have any of the app in between. Um so, I think that people have to kind of like reframe, you know, not to work in the existing paradigm of what things existed and just think about it as a speed up of what exists. It's actually like new things are available now. And going back to your programming question, it's not even I think that's also an example of working in the in the old mindset because it's not just about programming and programming becoming faster. This is more general information processing that is automatable now. So, um it's not just even about code. So, previous code worked over a kind of like structured data, right? And uh you write code over structured data. But like for example with my LLM knowledge bases project, um uh basically you get LLMs to create wikis for your organization or for you in person, etc. This is not even a program. This is not something that could exist before because there was no there was no code that would create a knowledge base based on a bunch of facts. But now you can just take these documents and uh basically uh recompile them in a different way, and uh reorder them, and create something that is uh new and interesting uh as a reframing of the data. And so, these are new things that weren't possible. Uh and so, I think this is uh something that I keep trying to get back to as to not only what can we do that existed that is faster now, but I think there's new opportunities of just things that couldn't be possible before. And I almost think that that's more exciting. I love the menu gen progression and dichotomy that you laid out, and I think even I'm sure many folks here followed your own progression of programming from last October to early January, February this year. If you extrapolate that further, what is the 2026 equivalent for building websites in the '90s, building mobile apps in the 2010s, building SaaS in the last cloud era? What will look completely obvious in hindsight that is still mostly unbuilt today? Um &gt;&gt; [clears throat] &gt;&gt; Well, going with the example of MenuGen, I guess. So, a lot of this code shouldn't exist and it's just neural networks doing most of the work. Um I do think that the extrapolation looks very weird because you could basically imagine I don't think I Yeah, so you could imagine completely neural computers in a certain sense. Uh you feed a raw videos like imagine a device that takes raw videos or audio into basically what's a neural net and uses diffusion to render a UI that is kind of like, you know, unique for that moment in a certain sense. And um I kind of feel like in the early days of computing actually, people were a little bit confused as to whether computers would look like calculators or computers would look like neural nets. And in '50s and '60s, it was not really obvious which way would go. And of course, we went down the calculator path and ended up building classical computing and then neural nets are currently running virtualized on existing computers. But you could imagine I think that a lot of this will flip and that the neural net becomes kind of like the host process. And the CPUs become kind of like the co-processor. So, we saw the diagram of, you know, intelligence compute is going to neural networks is going to take over and become the dominant spend of flops. So, you could imagine something really weird and foreign when where neural nets are doing most of the heavy lifting, they're using tool use as just like, you know, historical appendage for some kinds of like deterministic tasks. But what's really running the show is these neural nets that are networked in a certain way. Um so, you can imagine something extremely foreign as the extrapolation, but I think we're going to probably get there sort of piece by piece. And I don't Yeah, I don't that that progression is TBD, I would say. &gt;&gt; [snorts] &gt;&gt; I'd love to talk a little bit about um, uh, this concept of verifiability. The fact that AI will automate faster and more easily domains where the output can be verified. Um, if that framework is right, what work is about to move much faster than people realize? And what professions do we have that people actually think are safe, but they're actually highly verifiable? Uh, yes, so I I spent uh, some time writing about verifiability and um, basically like traditional computers can easily automate what you can specify in code. And uh, kind of this latest round of LLMs can easily automate what you can uh, verify in a certain in a certain sense. Uh, because the way this works is that when frontier labs are training these LLMs, these are giant reinforcement learning environments. So, they are given a verification rewards. And then because of the way that these models are trained, they end up basically uh, progressing and creating these like jagged entities that really peak in capability in kind of like verifiable domains like math and code and adjacent. And kind of like stagnate and are a little bit um, you know, rougher on the edges when uh, things are not kind of like in that in that space. So, I think the reason I wrote about verifiability is I'm trying to understand why these things are so jagged. Um, and some of it has to do with how the labs train the models, but I think some of it also has to do with um, the focus of the labs and what they happen to put into the data distribution. Uh, because some things basically are significantly more valuable in economy and end up creating more environments because the labs wanted to work in those settings. So, I think code is a good example of that. There's probably lots of verifiable environments they could think about that happen not to make it into the mix because they're just not that useful to have the capability around. Um, but I think to me the big um, I guess like the big mystery is uh, the favorite example for a while was that how many letters are are in a strawberry? And the models would famously get this wrong and it's an example of jaggedness. Uh, the models now patch this, I think, but the new one is I want to go to a car wash to wash my car, and it's 50 m away, should I drive or should I walk? And state-of-the-art models today will tell you to walk because it's so close. How is it possible that state-of-the-art Opus 4.7 will simultaneously refactor a 100,000 like &gt;&gt; [laughter] &gt;&gt; code base a line code base or find zero-day vulnerabilities and yet tells me to walk to this car wash? This is insane. And to whatever extent these models are remain jagged, it's an indication that number one, maybe something slightly off. Or number two, you need to actually be in the loop a little bit and you need to treat them as tools and you do have to kind of stay in touch with what they're doing. And so I think all of my writing, long story short, about verifiability is just trying to understand um why these things are jagged, is there any pattern to it? And I think it's a some kind of combination of verifiable plus labs care. Maybe one more anecdote that is instructive is from GPT-3.5 to GPT-4, people noticed that chess improved a lot and I think a lot of people thought, oh well, it's just a progression of the capabilities. But actually it's it's more that I think this is public information, I think I saw it on the internet. Um a huge amount of like data of chess made it into the pre-training set. And just because it's in the data distribution, basically the model improved a lot more than it would just by default. So someone at OpenAI decided to add this data and now you have a capability that just peaked a lot more. And so that's why I think I'm stressing this dimension of it as we are slightly at the mercy of whatever the labs are doing, whatever they happen to put into the mix and you have to actually explore this thing that they give you that has no manual and it works in certain settings but maybe not in some settings and you have to kind of explore it a little bit and if you're in the circuits that were part of the RL, you fly and if you're in the circuits that are out of the data distribution, you're going to struggle and you have to kind of figure out which which circuits you're in in your application. And if you and if you're not in the circuits, then you have to really look at fine-tuning and doing some of your own work because it's not going to necessarily come out of the LLM out of the box. I'd love to come back to the concept of jagged intelligence in a little bit. Um if you were a founder today and thinking about building a company, you are trying to solve a problem that you think is tractable, something that uh is a domain that is verifiable, but you look around and you think, "Oh my gosh, well the labs have really really started uh got getting to escape velocity and the ones that seem most obvious, math, coding, and others." What would your advice be to to the founders in the audience? Um So, I think maybe that comes to the previous question of I do think that verifiability because it um Let me think. So, verifiability makes something tractable in the current paradigm because you can throw huge amount of RL at it. Um So, maybe one way to see it is that uh that remains true even if the labs are not focusing on it directly. So, if you are in a a verifiable setting where you could create these RL environments or examples, then that actually sets you up to potentially do your own fine-tuning and you might benefit from that. But, that is fundamentally technology that just works. You can pull a lever. If you have huge amount of diverse data sets of RL environments, etc., uh you can use your favorite fine-tuning framework and um and uh pull the lever and get something that actually uh works pretty well. So, um I don't know what the examples of this might be. Um but I do think there are some very valuable uh reinforcement learning environments that people could think of that I think are not part of the Yeah, I don't want to give away the answer, but there is one domain that I think is very uh Oh, okay. Sorry. I don't mean to vague post on on the stage, but uh there are some examples of this. On the flip side, what do you think still feels automatable only from a distance? I do think that ultimately almost everything can be made uh verifiable to some extent, some things easier than others. Um because even for like things that are like writing or so on, you can imagine having a council of LLM judges and probably get get to some get something reasonable out of the from from this kind of an approach. So, it's more about what's easy or hard. Um So, I I do think that ultimately um Uh yeah, I think uh Everything. &gt;&gt; [laughter] &gt;&gt; Everything is automatable. Amazing. Okay. Um so, last year you coined the term vibe coding and today we're in a world that feels a little bit more serious, more agentic engineering. What do you think is the difference between the two and what would you actually call what we're in today? Uh yeah, so I would say vibe coding is about raising the floor for everyone in terms of what they can do in software. So, the floor rises, everyone can vibe code anything, and that's amazing, incredible. But then I would say agentic engineering is about preserving the quality bar of what existed before in professional software. So, you're not allowed to introduce uh vulnerabilities due to vibe coding. Um you are um you're still responsible for your software just as before, but can you go faster? And spoiler is you can, but how do you how do you do that properly? And so, to me agentic engineering when I I call it that because I do think it's kind of like an engineering discipline. You have these agents which are these like spiky entities, they're a bit fallible, a little bit stochastic, but they are extremely powerful. And it's how do you how do you coordinate them to go faster without sacrificing your quality bar? And doing that well and correctly um is the the realm of agentic engineering. Um so, I kind of see them as as different. Like one is about maybe raising the raising the floor, and the other is about um you know, extrapolating. And what I'm seeing I think is there is a very high ceiling on agent engineer uh capability. And you know, people used to talk about the 10x engineer previously. I think that this is uh magnified a lot more. Uh 10x is uh is not uh the speed up you gain. Um and I think uh it does seem to me like people who are very good at this um peak a lot more than 10x uh from from my perspective right now. I really like that framing. Um one thing that when Sam Altman came to AI sent last year, one memorable thing he said was that people of different generations use ChatGPT differently. So, if you're in your 30s, you use it as a Google search replacement, but if you're in your teens, ChatGPT is your gateway to the internet. What is the parallel here in coding today? If we were to watch two people code using open claw, cloud code, codex, one you'd consider mediocre at it and one you would consider fully AI native, how would you describe the difference? I [clears throat] mean, I think it's just trying to get the most out of the tools that are available, utilizing all of their features, investing into your own kind of setup. So, just like previously, all the engineers are used to basically getting the most out of the tools you use, either it's Vim or VS Code or now it's you know, cloud code or codex or so on. So, um just investing into your setup and utilizing a lot of the, you know, tools that are available to you. Um and I think it just kind of looks like that. I do think that maybe related thought is um a lot of people are maybe hiring for this, right? Because they want to hire strong agentic engineers. I do think that what I'm seeing is that the, you know, most people are still not refactored their their hiring process for agentic engineer capability, right? Like if you're giving out puzzles to solve, then this is still the old paradigm. I would say that hiring have to has to look like give me a really big project and see someone implement that big project. Like let's write, say a Twitter clone for agents and then make it really good, make it really secure, and then have some agents simulate some activity on this Twitter. And then I'm going to use 10 codex 5.4 x high to try to break your break your this website that you deployed and they're going to try to basically break it and they should not be able to break it. And so maybe it looks like that, right? And so yeah, watching people in that that setting and building some bigger projects and utilize utilizing the tooling is maybe what I would look at for the most part. And as agents do more, what human skill do you think becomes more valuable, not less? Also, yeah, it's a good question. I think um Well, right now the answer is that the agents are catalog these internal entities, right? So it's remarkable um you basically still have to be in charge of the aesthetics, the the judgment, the taste, and a little bit of oversight. And maybe one one of my favorite examples of like the the weirdness of agents is um for menu gen, you sign up with a Google Google account, but you purchase credits using a Stripe account and both of them have email addresses. And my agent actually tries to basically um like when you purchase credits, it assigned it using the email address from Stripe to the Google email address. Like there wasn't a persistent user ID that that for people. It was trying to match up the email addresses, but you could use different email address for your Stripe and your Google and basically would not associate the funds. And so this is the kind of thing that these agents still will make mistakes about. It's like why would you use email addresses to try to cross-correlate the funds? They can be arbitrary. You can use different emails, etc. Like this is such a weird thing to do. So I think people have to be in charge of this spec, this plan, and actually don't even like the plan mode. I would I mean, obviously it's very useful, but I think there's something more general here where you have to work with your agent to design a spec that is very detailed and maybe it's a maybe basically the docs and then get the agents to write them. And you're in charge of the oversight and the top-level categories, but the agents are doing a lot of the under the hood. And so I think you're not caring about some of the details. So as an example also with um, a race or tensors in neural networks, um, there's a ton of details between PyTorch and NumPy and all the different like pandas and so on for all the different little API details. And I'll I already forgot about the keep dims versus keep dim or whether it's dim or axis or reshape or permute or transpose. I don't remember this stuff anymore, right? Because you don't have to. This is the kind of details that are handled by the intern because they have very good recall. And but you still have to know for example that um, you know, there's underlying tensor, there's an underlying view and then you can view of the same storage or you can have different storage which will be less efficient. As we still have to have an understanding of what this stuff is doing and some of the fundamentals um, so that you're not copying memory around unnecessarily and so on. But uh, the details of the APIs are now handed off. So it um, you're in charge of the taste, the engineering, the design uh, and that it makes sense and that you're asking for the right things and that you're saying that okay, that these have to be unique user IDs that we're going to tie everything to. Um, and so you're doing some of the design and development and the engineers are doing the fill in the blanks. And that's currently kind of like where we are and I think that's what everyone of course is seeing I think right now. Do you think there's a chance that this um, taste and judgment matters less over time or will the ceiling just keep rising? Um, yeah, it's a good question. I would say um, I mean I'm hoping that the that it improves. I think probably the reason it doesn't improve right now is again it's not part of the RL. There's probably no aesthetics cost or reward or it's not good enough or something like that. Um, I do think that when you actually look at the code, sometimes I get a little bit of a heart attack because it's not like super amazing code necessarily all the time and it's very bloated and there's a lot of copy-paste and there's awkward abstractions that are brittle and like it works but it's just really gross. Um, and I do I do hope that this can improve in future models. Um, a good example also is this uh, you know, the micro GPT project uh, which where I was trying to simplify uh LLM training to be as simple as possible. The models hate this. They can't do it. I tried to I keep I kept trying to prompt an LLM to simplify more, simplify more, and it just can't You feel like you're outside of the RL circuits. It feels like it you're obviously, you know, you're pulling teeth. It's not like light speed. So, I think um I do think that people are still remain in charge of this, but I do think that there's nothing fundamental again that's preventing it. It's just the labs haven't done it yet almost. Yeah. So, I'd love to come back to this idea of uh jagged forms of intelligence. You wrote a little bit about this with uh very thought-provoking piece around animals versus ghosts. Um and the idea is that we're not building animals. We are summoning ghosts. Um and these are jagged forms of intelligence that are shaped by data and reward functions, but not by intrinsic motivation or fun or curiosity or empowerment, uh things that kind of came about via evolution. Um why does that framing matter? And what does it actually change about how you build and deploy and evaluate or even trust them? Uh yes, so Yeah, I think the reason I wrote about this is because I'm trying to wrap my head around what these things are, right? Because if you have a good model of what they are or are not, then you're going to be more competent at uh using them. Um and I do think that um I don't know if it has I'm not sure if it actually has like real power. &gt;&gt; [laughter] &gt;&gt; I think it's a little bit of philosophizing. But I do think that um I think it's just um coming to terms with the fact that these things are not, you know, animal intelligences. Like if you yell at them, they're not going to work better or or worse or it doesn't have any impact. Um and uh it's all just kind of like these statistical simulation circuits where the the substrate is pre-training, so like statistics. And then but then there's RL bolting on top, so it kind of like increases the disadvantages and um maybe it's just kind of like a mindset of what I'm coming into or what's likely to work or not likely to work or how to modify it, but I don't actually I don't know that I have like here are the five obvious outcomes of how to make your system better. It's more just being suspicious of it and um figuring out over time. That's where it starts. Okay, so you are so deep in working with agents that don't just chat. They have real permissions. They have local contacts. They actually take action on your your behalf. What does the world look like when we all start to live in that world? Yeah, I think I think a lot of people probably here are excited about what this agentic you know, native agentic environment looks like and everything has to be rewritten. Everything is still fundamentally written for humans and has to be moved around. I still use most of the time when I use different frameworks or libraries or things like that. They still have docs that are fundamentally written for humans. This is my favorite pet peeve. Like I don't Why are people still telling me what to do? Like I don't want to do anything. What is the thing I should copy paste to my agent? &gt;&gt; [laughter] &gt;&gt; So it's just every time I'm told, you know, go to this URL or something like that. It's just like ah. &gt;&gt; [laughter] &gt;&gt; You know. &gt;&gt; [snorts] &gt;&gt; So um everyone is I think excited about how do we decompose the workloads that need to happen into fundamentally sensors over the world, actuators over the world. How do we make it agent native? Basically describe it to agents first. Um and then I have a lot of automation around you know, the Yeah, around data structures that are very legible to the LLMs. So I think yeah, I'm hoping that there's a lot of agent first infrastructure out there and that you know, for MenuGen famously when I wrote the not I'm not sure how famously, but when I wrote the blog post about MenuGen [laughter] a lot of the work a lot of the trouble was not even writing the code for MenuGen. It was deploying it on Vercel because I had to work with all these different services and I just string them up and I just go to their settings and the menus, and you know, configure my DNS, and it was just so annoying. And so, that's a good example of I would hope that MenuGen that I could give a prompt to an LLM, build MenuGen, and then I didn't have to touch anything, and it's deployed in that same way on the internet. I think that would be a good kind of a test for whether or not a lot of our infrastructure is becoming more and more agent native. And then ultimately, I would say yeah, I I do think we're going towards a world where there's agent representation for people and for organizations, and um you know, I'll have my agent talk to your agent to figure out some of the details of our meetings or things like that. So, &gt;&gt; [laughter] &gt;&gt; um I do think that that's roughly where things are going, but um yeah, I think everyone here is excited about that. I really like the visual analogy of sensors and actuators. I actually hadn't thought of that. That's super interesting. &gt;&gt; Right. Um okay, I think we have to end on a question about education, um because you are probably one of the very best in the world at making complex technical concepts simple and deeply thoughtful about how we design education around it. Um what still remains worth learning deeply when intelligence gets cheap as we move into the next era of AI? Yeah. Uh there was a tweet that blew my mind recently, and I keep thinking about it like every other day. It was something along the lines of um you can outsource your thinking, but you can't outsource your understanding. And um I think that's really nicely put. I so yeah, because I still I'm still part of the system, and I still I still have to somehow information still has to make it into my brain, and I feel like I'm becoming a bottleneck of just even knowing what we're trying to build, why is it worth doing, uh how do I direct you know, how do I direct my my agents, and so on. So, I do still think that ultimately something has to direct the thinking and the processing, and so on. And um that's still kind of fundamentally constrained somehow by understanding. And this is one reason I also was very excited about all the all the knowledge bases because I feel like that's that's a way for me to process information. And anytime I see a different projection onto information, I always like feel like I gain insight. So, it's really just a lot of prompts for me to do synthetic data generation kind of over over some fixed data. Uh so, I I really enjoy uh whenever I read an article, I have my uh you know, my wiki that's being built up from these articles. And I love asking questions about things or um and I I think that ultimately these are tools to enhance understanding in a certain way. And this is still kind of like a bit of a bottleneck because then you can't direct the uh you you can't be a good director if you still uh cuz the LLMs certainly don't excel at understanding. You still are uniquely in charge of that. So, uh yeah, I think uh tools to that effect I think are incredibly interesting and exciting. I'm excited to be back here in a couple years and to see if we've been fully automated out of the loop and they actually take care of understanding as well. Uh thank you so much for joining us, Andre. We really appreciate it. [applause]
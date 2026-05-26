# Harnesses in AI: A Deep Dive — Tejas Kumar, IBM

**來源**: https://www.youtube.com/watch?v=C_GG5g38vLU
**作者/頻道**: Tejas Kumar（IBM AI Developer Advocate）/ AI Engineer
**發布日期**: 2026-05-17
**收錄日期**: 2026-05-19
**時長**: 20:26
**語言**: 英文（自動字幕）

---

## 核心摘要

> AI harness 是圍繞模型的一切基礎設施，讓不可預測的黑盒模型能在穩定、可控環境中可靠運作。

### 為何需要 Harness？

我們都在向 Anthropic、Google 等公司「租用」模型算力。模型是黑盒：Opus 隨時可能被換成 Sonnet、context 有上限、行為不可控。Harness 的目標只有一個：**reliability（可靠性）**——讓 agent 做到它該做的事，無論底層模型是什麼。

### Agent Harness 的五大組成

| 組件 | 說明 |
|------|------|
| **Tool Registry** | 給模型用的工具集（檔案讀寫、bash、瀏覽器等） |
| **Model** | 可選擇的底層模型（部分 harness 固定） |
| **Context 管理** | 自動壓縮 context（如 Claude Code 的 /compact） |
| **Guardrails** | 限制 max steps、max messages，超限即終止 |
| **Agent Loop** | 外層循環，可以是 loop 的 loop（NM loop） |
| **Verify Step** | 完成後驗證：跑 lint、跑測試、確認結果是否真實成功 |

Claude Code、Cursor、Codex 都是典型的 harnessed coding agent。

### Live Demo 重點：逐步建構 Harness

**任務**：用 GPT-3.5 Turbo（2023 舊模型）+ Playwright 瀏覽器 agent 自動對 Hacker News 第一篇文章按讚。

**問題演進**：

1. **無 harness**：Agent 說「成功了」但其實失敗（被 login 頁擋住），謊報結果
2. **加 verify step**：讀取 agent tool 呼叫歷史，偵測真正的成功/失敗；agent 不再說謊
3. **加 guardrail**：max_attempts=3，最多重試三次，失敗即放棄
4. **加 login handler（確定性邏輯）**：每個 agent loop 前檢查是否在 login 頁；若是，deterministically 填入帳密送出表單，再通知 agent「我已幫你登入」

**關鍵結論**：整個 demo 中**從未修改 prompt**。Harness 的改進讓同一個 prompt 從失敗到成功——prompt engineering 不是萬能藥。

### IBM 實戰案例

**Open RAG**：IBM 開源企業 RAG 框架，專為資料敏感環境（Slack、PDF、Teams 錄音、invoice）設計，harness 提供企業級安全性。

### 未來展望

- **2025**：agents 元年
- **2026**：harnesses 元年
- **2027（預測）**：Dynamic on-the-fly harnesses — agent 在執行任務前先自動產生專屬 harness，自我感知潛在幻覺點並預先設防，類似 Plan Mode 但更強大

---

## 逐字稿（含時間戳）

**[00:07 → 00:21]** [music] >> Hello everybody. Everybody's head turned up. Hello, hi. How was lunch? Was it good? You didn't like it, no?

**[00:23 → 00:37]** It's like British food. Anyway, hi. I'm Tejas. I'll be your first speaker this afternoon. Tejas, that's pronounced like Tejas. Don't worry, I'm not — Hopefully my joy in AI is

**[00:39 → 00:53]** absolute joy to learn from the best. Today, I'm a AI developer advocate at IBM where we do things with AI, believe or not. We train frontier models, we build harnesses. It's really a fun lab to work in.

**[00:55 → 01:10]** But that's not what I'm here to talk to you about today. Today, I'm here to talk to you about AI harnesses. Before I move forward, I would love to just have a show of hands. How many of you are like confident in your understanding of AI harnesses?

**[01:11 → 01:25]** Okay, this is my hope. I want you to — if I ask you this at the end of the talk, right? — I want you to be like, oh, I get it now. That's the whole point. I have literally nothing to gain from this other than shared knowledge, okay?

**[01:28 → 01:42]** Because also this term is kind of everywhere. And it means different things to different people — like in the machine learning world, it means like a glorified test suite for machine learning models. But in the AI world, it means something different.

**[01:44 → 01:58]** I want to start by talking about why harness. Like why do we use harnesses? And the reason for this is because we pay rent to companies that give us compute, give us inference, give us tokens in return.

**[02:01 → 02:15]** Some of you maybe work for companies that have frontier models like Anthropic or Google or whatever and you maybe — what was the term? — token billionaires, yeah? But the vast majority of us aren't token billionaires. We pay rent. We literally pay $20 a month for Claude Pro.

**[02:17 → 02:32]** And the model you rent is a black box. Like they could at any time — I'm not saying they do, but they could — if Opus is somehow not available, they could serve you Sonnet even though it says Opus. You would never know, right?

**[02:34 → 02:49]** Variables that we cannot control. So why harness? Because the name of the game with harness is reliability. It's making sure that the agents we build do what they do, period. Irrespective of the black box model.

**[02:51 → 03:05]** Now that we understand why harness, let's talk about what a harness even is from first principles. Like let's take it all the way back to harnesses that we know and understand.

**[03:06 → 03:20]** This is a harness. It's like mountain climbers literally will harness themselves to a mountain because it's stable. And they can't go off the rails, literally.

**[03:22 → 03:36]** They anchor themselves so that they can't drift too far. Okay, that's what a harness is by design. Do you have any dog owners here? You walk your dog on a harness — because your dog doesn't go and bankrupt you with tokens.

**[03:38 → 03:52]** That's what a harness is. But the problem is if we think about what harness, there's really two types. There's one from the machine learning world, which is kind of like a test suite and a test runner.

**[03:54 → 04:07]** That's not what we're talking about. This is AI Engineer Europe. We're going to talk today about the agent harness that is common in AI engineering.

**[04:10 → 04:23]** The agent harness is everything around the model that gives it grounding in reality. It's literally the thing that ties it to a stable environment, okay? Claude Code, for example, can be considered an agent harness.

**[04:25 → 04:38]** And some of you would say, oh, no, it's a coding agent. Absolutely, it's a coding agent. But it's a harnessed coding agent. An agent harness has more or less the same typical suspects — tool registry, model, context management primitives.

**[04:41 → 04:53]** Claude Code, Cursor, Codex — they have tools to read from the file system, to write, to execute bash commands, right? They have a tool registry. They have a model.

**[04:57 → 05:10]** Almost every harnessed agent runtime today will compact its own context, right? That's the job of the harness. Guardrails are another part of a harness. For example, max steps — anyone using max steps? Do not do more than five tool calls. That's a guardrail.

**[05:12 → 05:25]** An agent loop is another part of an agent harness — and this is what some people will say: "Wait, isn't a harness just the agent loop?" No, it's the stuff around the agent loop. In fact, it could be a loop around your agent loop. An N×M loop.

**[05:27 → 05:41]** And then finally, there's a verify step. In a coding agent, after the work is done, a verify step would be: hey, let's run lint, let's run tests, let's make sure nothing broke.

**[05:44 → 05:59]** So almost every coding agent — you could have a harness for anything. And it's amazing because it really grounds black box models in a stable environment that you control.

**[06:00 → 06:14]** I'd like to show you a demo. We're going to build a harness — a bare bone baby's first harness. Let's call it a poor man's AI harness — so we understand from first principles how this works.

**[06:16 → 06:30]** We're going to build a browser use agent. We're going to use a really bad model intentionally: GPT-3.5 Turbo, which is like 2023, right? But we're going to harness it so that it can actually do the job.

**[06:32 → 06:46]** Let's get into the demo. Welcome to my project. This is the entry point.

**[06:48 → 07:03]** So we have a model, and this is the prompt. This is the task. Upvote a story. For the purpose of this demo, we will not change the prompt at all. Because a lot of us think, hey, my agent is not doing what it's supposed to do, so I just need to prompt it harder, right? That's not always true.

**[07:05 → 07:20]** I need to change the system prompt. We're not — we're just going to build a harness and the outcome will change. We log some things to the console and then we start a browser session.

**[07:22 → 07:36]** A browser session — it's literally just Playwright. Where this is just a class I made with an open method that launches Chromium and gets a context and makes a page.

**[07:37 → 07:52]** And we give that browser session to the tools. And we create a context and we give the task — meaning the prompt here — to the context. Now, create tools.

**[07:54 → 08:08]** These tools are not invented by me. This is from OpenAI's SDK, okay? So you have the name, the description, parameters, and execute — the way you call the tool.

**[08:11 → 08:25]** This is my context. There's nothing here. It's just a system prompt. Literally, the most basic system prompt.

**[08:43 → 08:58]** While true — so it is an agent loop. And we get a response from the agent and we see if the response says stop, meaning the agent is done.

**[09:00 → 09:14]** We add these events into a trace. So we just push history into a big list of history. This is just a trace, okay?

**[09:16 → 09:28]** npm run agent. So it's going to open Chromium. It's going to — okay, Hacker News, so far so good. Click upvote. Oh, no.

**[09:32 → 09:46]** This is a problem. So what's the solution? Prompt it harder? No. Change the system prompt. Always login with these credentials — included in the system prompt.

**[09:49 → 10:03]** But it still clicks the upvote button and then considers it a success. It doesn't verify. This is the job of a harness, okay? So now incrementally, we're going to slowly start building our harness.

**[10:05 → 10:20]** This is the first change we're making. We're going to create some guardrails, okay? What do our guardrails look like?

**[10:36 → 10:49]** Max messages — meaning if you have more than this many messages, I will compress the context. These are just guardrails.

**[10:51 → 11:06]** And max steps. If you've exceeded this many tool calls, we will abort. These are guardrails. And of course, we abort in the agent loop whenever these conditions are breached.

**[11:07 → 11:21]** And the second thing is we added a verify step. We have a new function called verify successful upvote. I wrote this. This is deterministic.

**[11:23 → 11:38]** What does this do? We see if there was a browser click on the upvote and if it's actually successful. But there's also checking for failed login cases.

**[11:40 → 11:55]** If there's a tool named harness auto login, and the message starts with failed, then we return early and say no, this failed. We're removing the lie.

**[11:57 → 12:10]** Similarly, unrecovered login redirect: if the harness auto login didn't run and we're on the login URL, we just fail. This is what a harness does.

**[12:13 → 12:26]** So let's run this now with the harness. It's going to come here, and now it's still failed — but look, it stopped lying. This is what a harness is supposed to do.

**[12:28 → 12:42]** Step one to solving a problem is admitting you have one. Test-driven development vibes. So now that we're failing correctly, we can succeed.

**[12:44 → 12:58]** The last diff: we have a whole new function called login handler. This is all it does: it runs every agent loop just before we push to the traces, and it checks the browser session's current URL.

**[13:00 → 13:14]** If we're not on a login page, it just says cool, I have nothing for you. If you are on the login page, then it fills in credentials and submits the button — programmatically from the harness, not from the agent, deterministically and securely.

**[13:16 → 13:30]** And it pushes a message into the queue saying: "Hey, I'm the harness. I logged in. You're good now."

**[13:32 → 13:46]** The harness is literally harnessing the agent to something stable, something deterministic. That's what it's for.

**[13:48 → 14:03]** npm run agent. It's going to open Hacker News, and when it gets to the login — now the harness step logged in, and it upvoted the first one, and it closed. Amazing.

**[14:05 → 14:19]** Successfully upvoted. Succeeded after six iterations. And I can go into Hacker News and actually see it was upvoted. The agent used the computer, logged in as me with my harness that I just made here on stage.

**[14:21 → 14:36]** Do you understand the role of a harness? Look at you nodding. Fantastic.

**[14:38 → 14:53]** Let's land the plane. What does this look like in practice? Why do I care so much about harnesses? Because they run the world. Models are non-deterministic. And you want to do more with less.

**[14:55 → 15:09]** You want to use a cheap model — like Qwen or something, or even something smaller. And with a great harness, you can go very far. At IBM, we create an open-source project — Open RAG — that allows very large companies in data-sensitive areas to perform RAG operations on Teams calls, PDFs, invoices.

**[15:11 → 15:23]** Open RAG has a harness that provides enterprise-level security for asking questions with internal, very siloed data.

**[15:25 → 15:37]** Let's summarize. It should not be lost on you that I did not touch the prompt once. I did not change the system prompt. We just built a harness and the outcome radically changed.

**[15:39 → 15:53]** I hope you understand what a harness is, the value it can present, and how you can use it. What's next? It's not lost on me that 2025 was the year of agents. 2026 is the year of harnesses, I'm pretty sure.

**[15:55 → 16:10]** And I think it'd be pretty cool if 2027 was the year of dynamic on-the-fly generated harnesses. You tell an agent: "Buy me a flight ticket." And before doing the work, the agent creates a harness — self-aware, knowing where it might hallucinate — does the job, and returns back to you, guardrailed.

**[16:12 → 16:26]** Dynamic on-the-fly harnesses. I think that's the next logical step towards AGI. Thank you so much. The slides are on GitHub. [music]

---

## 完整純文字

[music] Hello everybody. I'm Tejas Kumar, AI Developer Advocate at IBM. Today I'm here to talk to you about AI harnesses.

Why harness? Because we pay rent to black-box models — Anthropic, Google, whatever. We're not token billionaires. The model could be swapped, context is limited, behaviour is unpredictable. The name of the game with harness is **reliability**: making sure the agents we build do what they do, period.

What is an agent harness? Everything around the model that gives it grounding in reality — tool registry, model, context management, guardrails (max steps/messages), an agent loop, and a verify step. Claude Code is a harnessed coding agent.

Demo: We built a browser-use agent using GPT-3.5 Turbo to upvote a Hacker News post. Starting with no harness — the agent lied about success. We incrementally added: guardrails (max_attempts=3, max_messages), a deterministic verify_successful_upvote function that reads tool call history, and a login_handler that deterministically fills credentials when it detects the login page. We never changed the prompt. The harness did all the work.

IBM's Open RAG is a real-world harness providing enterprise RAG over sensitive internal data.

2025 = year of agents. 2026 = year of harnesses. 2027 = dynamic on-the-fly harnesses: agents auto-generate their own harness before starting a task.

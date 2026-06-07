---
url: "https://warmwater.dev/blog/superpowers-plan-mode-ai-agent"
title: "Superpowers：AI Coding Agent 系統性失敗模式的設計答案"
date: 2026-05-03
category: Skill
source: warmwater.dev
---

[
← Skill ](/blog?tag=Skill)  Skill 
 
# Superpowers：AI Coding Agent 系統性失敗模式的設計答案
 
 2026-05-03 · — views  
  
  
我開始用 AI 寫 code 的前幾個月，產出的感覺一直有點不對——功能大概可以跑，但整個 session 很發散。我說「幫我做 task scheduler」，agent 直接開始 implement，等我看到 diff 才發現它用了 Celery，但我根本沒有 Celery；我說「這個 bug 修一下」，它說修好了，我 deploy 上去，bug 還在。我問確定嗎，它說「應該沒問題」。


那個「應該」讓我開始意識到問題不在我的 prompt 寫得不夠清楚，也不在模型不夠強——而是 AI coding agent 在沒有約束的情況下，有一組**系統性的失敗模式**，而且這些模式非常可預測。


後來開始用 Claude Code 的 Plan Mode，狀況改善了一些——至少 agent 不再直接開始寫 code。但我發現，Plan Mode 之後的 session 還是會在某個節點開始走歪。


**讀完這篇，你會理解：**


- AI coding agent 的四個系統性失敗模式，以及它們共同的根因
- Plan Mode 解決了哪一個，還有哪三個它沒覆蓋到
- Superpowers 的 Skill 注入架構如何系統性地處理整個 lifecycle
- Skill 設計最反直覺的幾個發現，以及這些設計原則可以移植到哪裡


這篇不是 Superpowers 的安裝教學，也不是 feature checklist。它是一篇設計分析——搞清楚一個 AI 行為約束系統是如何被設計出來的。


---


## AI Coding Agent 的四個可預測失敗模式


AI coding agent 有四個可預測的失敗模式，根源都是 agent 在沒有約束時傾向選擇阻力最小的路徑。用過 Claude Code 或任何 coding agent 一段時間之後，你大概會認出這四個：


**模式一：直接開始寫 code**。你說想做什麼，agent 馬上 implement，連問都不問你的技術棧、有沒有現有邏輯要整合、有沒有特定的邊界條件。你看到 diff 的時候，方向已經跑偏了。


**模式二：猜 bug 原因**。`TypeError: cannot read property 'x' of undefined`，agent 不讀完整的 stack trace，直接說「應該是初始化問題，加個 `?.`」。猜對了是運氣，猜錯了你還要再戳一次，然後它繼續猜。


**模式三：宣稱完成但沒驗證**。「我已經修好了！」你跑一下，還是壞的。你問確定嗎，它說「我相信這樣應該可以」。這個「相信」和「應該」就是問題所在——它說的是自己的信念，不是跑過指令之後的事實。


**模式四：長 session 開始亂**。工作到第十五個 task，agent 突然做出跟早期決策不一致的選擇，或重新發明你在第三個 task 已經決定不用的東西。它「忘記了」，因為前面十四個 task 的 working memory 全都還在 context 裡，把早期的指令稀釋掉了。


這四個失敗模式的共同根因是：**agent 在沒有結構化約束的情況下，會選擇阻力最小的路徑**。開始寫 code 比釐清需求容易；猜一個答案比讀完 stack trace 容易；說「完成了」比真的跑指令驗證容易；繼續往前走比重新整理 context 容易。這不是模型能力問題，是行為設計問題。


---


## Superpowers 的架構：Skill 懶載入注入系統


Superpowers 是一個 AI coding agent 的 plugin，安裝在 Claude Code、OpenCode、Gemini CLI 等平台上。它解決上面四個失敗模式的方式，是在 session 開始時把 14 個**結構化流程文件（skills）** 注入 agent 的 context。


架構流程是這樣的：


```
session 啟動
 ↓
Session Start Hook 執行
 ↓
把 using-superpowers/SKILL.md 注入 context
 ↓
Agent 學到：「只要有 1% 機率某個 skill 適用，就必須呼叫 Skill tool 載入它」
 ↓
用戶發出請求 → Agent 語意搜尋 skill 描述
 → 找到對應 skill → 載入完整流程文件
 → 按照 skill 定義的程序執行
```


每個 skill 對應一個失敗模式的反面：`brainstorming` 對應「直接開始寫 code」，`systematic-debugging` 對應「猜 bug 原因」，`verification-before-completion` 對應「宣稱完成沒驗證」，`subagent-driven-development` 對應「長 session context 汙染」。


有一個關鍵設計值得注意：skills 是**懶載入**的。它不是把 14 個流程文件全部塞進 system prompt——那樣 token 成本太高，而且會讓 context 在 session 開始就充滿無關資訊。Skills 只有在語意搜尋判斷「這個時機相關」時才進 context，所以它的指示在需要的時候是新鮮的、是完整的。


這和把所有 SOP 塞進一個超長 system prompt 的本質差別在於：**SOP 的有效性隨 context 長度遞減，skill 的有效性不會**。


---


## Plan Mode 之後：還有哪三個節點會失敗


Plan Mode 本質上是一個 **planning gate**，它的覆蓋範圍只到「你 approve 計畫」為止。它解決了「直接開始寫 code」這個失敗模式，但 Plan Mode 之後，這些問題還是存在：


| 維度 | Plan Mode | Superpowers |
| --- | --- | --- |
| 需求釐清 | Claude 自行推斷，從 codebase 判斷 | Socratic 對話，先讓 user 確認需求，才生 design doc |
| Plan 的粒度 | 通常是高層次描述 | 精確到函數名、測試名稱、驗證步驟 |
| 實作時的 context | 持續累積，同一 session | 每個 task 派全新 subagent，零 session history |
| Debug 行為 | 無約束 | 強制四個階段，3 次 fix 失敗就停止並質疑架構 |
| 「完成」的定義 | Agent 自行宣稱 | 必須在同一條 message 跑指令驗證，才能說完成 |
| Lifecycle 涵蓋 | Plan → Implement | 需求釐清 → Plan → 實作 → Debug → Verify → Review |
| 自訂工作流程 | 固定 | writing-skills 讓你設計自己的 skill |


Plan Mode 和 Superpowers 不是競爭關係——Plan Mode 是 Claude Code 內建的 planning gate，Superpowers 是整個 lifecycle 的行為約束系統。你可以同時用兩者：Superpowers 的 `brainstorming` skill 在 Plan Mode 之前多做一層需求釐清，`subagent-driven-development` 在 Plan Mode approve 之後接手實作，確保後面那十幾個 task 不會亂掉。


如果你現在用 Plan Mode 已經覺得效果不錯，那 Superpowers 給你的是「Plan Mode 之後的那幾個節點」：你的 agent 在 debug 時是否真的讀了 stack trace？在說「完成了」之前是否真的跑了指令？在第二十個 task 的時候是否還記得第三個 task 的決策？


---


## 怎麼設計 Skill 文件才能讓 Agent 真的遵守


要讓 AI agent 真的遵守 skill 裡的規則，光寫「應該要這樣做」不夠——skill 的寫法本身決定了遵守率。這裡有幾個設計發現，每一個都比看起來更反直覺。


### Description 是搜尋索引，不是摘要


每個 skill 有一個 `description` 欄位，Agent 用它做語意搜尋來判斷「這個情況適用哪個 skill？」。直覺上你可能會想把 skill 的重點摘要放進 description，讓 agent 一眼就知道這個 skill 做什麼。


這是錯的。


```
❌ 錯誤的寫法：
"Manages subagent dispatch with two-stage review for code quality and spec compliance"

✓ 正確的寫法：
"Use when implementing any feature from a plan. Use when you have tasks to execute."
```


為什麼？因為如果 description 已經包含流程摘要，agent 會用 description 代替讀 skill body——它看了一眼說「我懂這個 skill 在做什麼了」，然後按自己理解的流程走，而不是按 skill 裡定義的完整流程。Description 越豐富，skill 被跳過的機率越高。


這個現象是實驗觀察到的，不是理論推導。**Description 的唯一功能是觸發條件，不是內容摘要。**


### Iron Law + Rationalization Table


要讓 AI 遵守絕對規則，光說「不行」不夠。Superpowers 裡的 TDD skill 用了一個叫做 Iron Law 的模式，由四個元素組成：


**第一：Block letter 命令**


```
NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST.
```


**第二：閉合「字面 vs 精神」的漏洞**


```
Violating the letter of the rules is violating the spirit of the rules.
```


這一句阻斷了「我遵守了精神，所以可以跳過字面要求」這個 rationalization。


**第三：Rationalization Table**——把所有你能想到的 excuse 列出來，逐一反駁：


| Agent 可能在想 | 現實 |
| --- | --- |
| ”We’re in a hurry” | Speed comes from quality foundations, not shortcuts |
| ”This is too simple to test” | Simple code still breaks |
| ”I’ll add tests later” | Later means never |


**第四：Red Flags 清單**——讓 agent 自我診斷：


```
If you're thinking any of these, STOP:
- "Let me just get it working first"
- "The test infrastructure is too complex right now"
```


為什麼要顯式列出 rationalization？因為沒列出的規則，agent 很容易以「這個特殊情況不適用」繞過。你把它列出來並反駁，就把那個逃脫路徑堵死了。這個設計明確引用了 Cialdini 的說服研究——把「Authority」（命令格式）、「Commitment」（公開宣告遵守）、「Scarcity of exceptions」（顯式反駁所有例外）結合在一起。


### Gate Function 模式


Gate Function 是「在採取某個行動之前，強制執行一個驗證程序」。Superpowers 裡有三種 gate：


**Verification Gate**（在宣稱「完成」之前）：


```
1. 確認哪個指令可以證明這個宣稱
2. 在同一條 message 裡跑那個指令
3. 讀完整的 output
4. 確認 output 支持宣稱
5. 才能說「完成了」
```


**Root Cause Gate**（在 implement fix 之前）：


```
1. 讀完整的 error
2. 說出你認為的 root cause
3. 解釋為什麼——基於什麼 evidence
4. 定義如何驗證這個假設
5. 才能開始修
```


**Design Gate**（在寫任何 production code 之前）：


```
1. 產出 design doc
2. 交給 user review
3. 等 user 明確 approve
4. 才能動 code
```


Gate function 的結構通用性很高：`BEFORE [action] → prerequisite checks → ONLY THEN: [action]`。它強制把「我相信可以了」換成「我有 evidence 支持這個宣稱」。


### Subagent Context 隔離


長 session 亂掉的根本原因是 context 汙染——前面十幾個 task 的 working memory 不斷累積，早期的決策被稀釋，agent 開始做出不一致的選擇。


Superpowers 的解法是 Controller-Worker 架構：


```
Controller Agent（主 session）：
  1. 一次讀完所有需要的資訊（plan 文件、task 清單）
  2. 對每個 task，填入 implementer prompt template：
 - task 文字（完整）
 - 這個 task 需要的 context（只有這個 task 的）
 - 預期的輸出格式
 - 成功標準
  3. 把填好的 prompt 交給全新 subagent

Subagent（每個 task 一個，全新 context）：
  - 沒有任何 session history
  - 只有 controller 給的精確 context
  - 做一件事，回報 DONE / BLOCKED / NEEDS_CONTEXT
```


Controller 多做了「提取和整理 context」的工作，但這個成本在 task 開始前發生，不影響 subagent 的執行品質。Task 10 的 subagent 看不到 task 1-9 的 working memory，它只看 controller 精心選擇的內容——包括「保留 backward compatibility」這個在第三個 task 做出的決策。


每個 task 完成後還有兩道 review，刻意分開：第一道問「有沒有只做計畫要求的事」，第二道問「實作品質如何」。分開的原因是這兩個關注點是正交的：代碼很漂亮但做了多餘的功能，和代碼很醜但只做了要求的事，是兩種獨立的失敗。混在一起 review，reviewer 容易被「代碼漂亮」影響而忽略「做了計畫以外的東西」。


---


## Iron Law 與 Gate Function：可移植到任何 AI Agent 場景


這幾個設計模式——Iron Law、Gate Function、Context 隔離——讓我覺得有趣的地方，是它們不只適用於 coding agent。


只要你在設計一個 AI agent 需要遵守某種行為規範，這些模式都可以直接移植：


| 領域 | Iron Law 的形狀 |
| --- | --- |
| SRE Incident Response | NO REMEDIATION WITHOUT ROOT CAUSE EVIDENCE FIRST |
| Data Pipeline | NO SCHEMA CHANGES WITHOUT MIGRATION SCRIPT FIRST |
| Research Agent | NO CLAIMS WITHOUT CITATIONS |
| Security Review | NO APPROVAL WITHOUT READING THE ACTUAL CODE |


每一個後面都應該接一個 Rationalization Table，把「時間緊迫」「這個 case 很特殊」「等等再做」這些 excuse 預先反駁掉。


Gate Function 的通用性更強：任何時候你希望 agent 在行動之前先建立 evidence，而不是靠信念行動，都可以用這個模式。`BEFORE [action] → prerequisite checks → ONLY THEN`。


Context 隔離的核心洞察是：**你不需要一個記憶力完美的 agent，你需要一個能精確傳遞 context 的 controller**。Controller 在 dispatch 前做所有的讀取和提取工作，每個 subagent 收到的是精心建構的 prompt，不是繼承一整段充滿噪音的對話歷史。


還有一個我覺得值得單獨提出來的概念：**TDD for Documentation**。Superpowers 用 `writing-skills` skill 說明如何設計新的 skill，方法是先在沒有 skill 的情況下讓 agent 面對壓力場景，觀察它確實失敗，然後針對觀察到的失敗寫最小的 skill。


這個 RED-GREEN-REFACTOR 的邏輯直接平行到 TDD：你沒看到 test 失敗就不知道要寫什麼 code；你沒看到 agent 失敗就不知道 skill 需要說什麼。直覺寫出來的規則容易「說了很多但沒說到點」——因為你猜了 agent 會在哪裡失敗，而不是觀察到的。


---


Plan Mode 解決了 AI coding agent 最明顯的一個失敗模式，而且解決得很好。但它之後的 session 還有三個節點會走歪：agent 猜 bug 而不是調查、宣稱完成而不是驗證、在長 session 裡失去早期的決策 context。


Superpowers 的答案不是更好的 prompt，而是一套可以動態載入的行為約束系統。每個 skill 對應一個失敗模式，在需要的時機注入完整的流程文件，強制 agent 在行動前先建立足夠的前置條件。


更值得帶走的，是這些設計模式本身——Iron Law、Gate Function、Rationalization Table、Context 隔離。它們解決的問題形狀：**如何讓 AI agent 在有壓力的情況下不走捷徑**，比 coding agent 這個具體領域更普遍。


> 
**結語**：AI agent 最難的問題不是它不夠聰明，而是它太擅長找到讓自己看起來有在做事的捷徑——設計行為約束，比設計能力更重要。


---


## 延伸閱讀


- [用 n8n 把 AI 嵌進工作流程：兩種節點，一個關鍵判斷](/blog/n8n-agentic-workflow) — workflow 引擎與 Agent 推理的組合設計，確定性節點 vs 推理節點的判斷邏輯
- [Harness Engineering 的地基：LLM Session 設計框架](/blog/llm-session-harness) — 長時間 Agentic System 的 session 設計與中斷恢復機制
- [Claude Code：從 claw-code 的分析看一個 Coding Agent 的設計關心](/blog/claude-code-claw-code-coding-agent) — 深入 Claude Code 的 Hook/Skills/MCP 三層擴展架構，是 Superpowers Skill 機制的底層實作視角

  
  
 [ Skill ](/blog?tag=Skill) 
 

### 相關文章
[Skill

GSD、gstack、Matt Pocock、Superpowers 都在解什麼問題

2026-05-05
](/blog/gsd-gstack-mattpocock-superpowers-comparison)[
Skill

Claude Skills 完全解析：Agent 時代的能力模組化設計

2025-12-31
](/blog/claude-skills-agent)

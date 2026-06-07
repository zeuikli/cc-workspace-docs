---
url: "https://warmwater.dev/blog/gsd-gstack-mattpocock-superpowers-comparison"
title: "GSD、gstack、Matt Pocock、Superpowers 都在解什麼問題"
date: 2026-05-05
category: Skill
source: warmwater.dev
---

在 Superpowers 那篇文章出來之後，收到最多的問題大概是這個：「GSD 不是更好嗎？」「gstack 更完整吧？」「我到底要學哪一套？」

這個問題的前提有點問題。

這四個工具不是在競爭同一個解法的市場。它們識別的失敗模式不同，設計出來的機制不同，適合的情境不同。說「GSD 取代 Superpowers」，有點像說「調試器取代型別系統」——兩個都在幫你寫出更好的程式，但它們不是在解同一個問題。

這篇是一個設計比較，試圖回答：這四套工具各自在修哪層漏洞、什麼情境用什麼、以及為什麼你可以同時用它們。

**讀完這篇，你會理解：**

- 這四個系統各自診斷的根本問題是什麼，以及為什麼不重疊
- Context 管理、工作流擁有權、AI 行為約束——三個最核心的設計維度如何分歧
- 什麼情境下選哪個，以及它們是否能疊加使用
- 這些設計模式的本質是什麼，以及為什麼它們不只適用於 coding agent

這篇不是安裝教學，也不是功能 checklist。是一個設計分析。

---

## 這四個工具各自在修哪層漏洞？

這四個工具的設計出發點完全不同：Superpowers 修的是 agent 行為缺陷，GSD 修的是 context rot，gstack 補的是領域專家視角，Matt Pocock 修的是 misalignment 和架構腐爛。工具的設計由問題驅動——診斷不同，解法就不會相同。

**Superpowers** 的診斷是：AI coding agent 在沒有約束時，有一組系統性的行為缺陷。它不是能力問題，而是行為設計問題——agent 傾向於走阻力最小的路：直接寫 code 不問需求、猜 bug 原因不讀 stack trace、說「完成了」但沒有跑指令驗證、長 session 跑到後來把早期的決策稀釋掉。Superpowers 的答案是 14 個 Skill，每個 Skill 是一個流程 gate：agent 遇到對應的情境，被強制先走完流程再繼續。

**GSD**（Get Shit Done）的診斷是：**context rot**。隨著 AI agent 的 context window 被對話歷史、工作記憶、失敗嘗試填滿，輸出品質會系統性地劣化——越到後面，AI 越容易忽略你早期說的約束，越容易為了往前走而走捷徑。GSD 的答案很激進：每個任務都在全新的 context 執行，session 結束了就結束了，下一個任務從乾淨的 context 重新開始，project 的所有狀態都存在磁碟的 markdown 文件裡。

**gstack**（Garry Tan 的開源框架）的診斷是：AI coding agent 缺少領域專家視角的約束。agent 直接寫 code，但它不是 CEO、不是 Eng Manager、不是 QA、也不是 CSO。沒有人問你需求真的清楚了嗎、架構有沒有 edge case、UI 有沒有 design system 支撐、deploy 之後有沒有人看 production 有沒有炸。gstack 的答案是 23 個虛擬角色，每個角色是一個有完整流程的 Skill，從 office hours 到 canary monitoring，每個節點都有人負責。

**Matt Pocock Skills** 的診斷是：AI 做出來的東西不是你要的（misalignment），以及 AI 輔助開發的速度加快之後，codebase 的架構腐爛速度也同步加快。他明確反對 GSD 和類似工具，理由是「它們接管了你的流程，出了問題你不知道在哪裡」。Matt Pocock 的答案是小型、可組合的工具：在開始任何任務前先讓 AI「烤透」你的計畫（grilling session）、建立 per-repo 的共享術語表（CONTEXT.md）、用 TDD 給 AI 可靠的 feedback loop、定期做架構體檢（`/improve-codebase-architecture`）。

---

## 為什麼它們的設計哲學差這麼多？

這四個系統在三個核心設計維度上的分歧，遠比功能清單顯示的更深：Context 如何管理、工作流程由誰控制、AI 行為如何約束——每個維度都有截然不同的答案。

### 維度一：Context 策略

這是四個系統最根本的分歧。

GSD 和 Superpowers 走的路是類似的：**新任務、新 context**。GSD 把這個做到最激進——每個 PLAN.md 是一個原子任務，由全新的 subagent 執行，subagent 從磁碟的文件重建所有它需要的 context，完全不繼承對話歷史。Superpowers 的 `subagent-driven-development` 是 controller-worker 架構：controller 在 dispatch 前提取精確的 context，填進 implementer prompt template，subagent 收到的是一個完全自足的 prompt，不需要問「我還需要什麼資訊」。

gstack 走的是相反的路：**跨 session 持久化記憶**。它有三層知識儲存——`~/.gstack/` 存 global config、`~/.gstack/projects/{slug}/learnings.jsonl` 存 project-specific 的跨 session learnings、`.claude/` 和 CLAUDE.md 存 repo 層的設定。每次 session 開始，preamble 自動載入最相關的 learnings。它承認 AI 會忘事，然後設計一個系統讓它記住對的東西。

Matt Pocock 的角度又不一樣。它不管理 context 隔離，也不管理持久化記憶，而是管理**詞彙一致性**。CONTEXT.md 是一個 per-repo 的術語表：每個 domain term 有精確定義，有「避免使用」的同義詞清單，有 entity 之間的關係說明。每次 session 開始前讀 CONTEXT.md，AI 就進入你這個 project 的語言系統，不會用 20 個詞描述同一個概念。

這是三種不同的問題意識：「讓 AI 遺忘所有無關的事」vs.「讓 AI 記住對的事」vs.「讓 AI 用對的語言說話」。

### 維度二：工作流擁有權

這四個系統在「誰控制工作流程」這件事上，形成了一個光譜：

```
GSD ─────── gstack ─────── Superpowers ─────── Matt Pocock
（工具擁有）  （角色擁有）   （行為約束）       （你擁有）
```

GSD 擁有你的工作流。你跑 `/gsd-new-project` 生成 PROJECT.md、REQUIREMENTS.md、ROADMAP.md；跑 `/gsd-discuss-phase` 確認細節；跑 `/gsd-plan-phase` 生成 PLAN.md；跑 `/gsd-execute-phase` 讓 subagent 執行。你在照著工具定義的 loop 走，不是工具在配合你的習慣。

gstack 是角色擁有流程。你選擇要叫哪個角色審查——`/plan-ceo-review` 讓 CEO 模式質疑你的 scope ambition、`/plan-eng-review` 讓 Eng Manager 模式審 architecture 和 edge cases、`/qa` 讓 QA 模式做三層深度的測試。你控制叫哪個角色，但那個角色的完整工作流程由 gstack 定義，不是你臨時決定的。

Superpowers 不定義你的流程，但在每個節點安裝 gate。你想直接寫 code？沒有問題，但如果你先描述了需求，`brainstorming` skill 會被觸發，它要求先做 design doc、讓 user 確認之後才能繼續。你說「修好了」？`verification-before-completion` 要求你先跑指令驗證，才能做出「完成」的宣稱。工具不管你怎麼工作，但在關鍵節點它會攔住你。

Matt Pocock 是你的工具箱，不是你的 manager。你決定什麼時候用 `/grill-with-docs`、什麼時候用 `/tdd`、要不要定期跑 `/improve-codebase-architecture`。沒有人強制你用，也沒有任何 gate 攔你。你自律，工具給力；你不用，工具也不會說話。

這個光譜沒有對錯，但它解釋了很多人的直覺偏好。喜歡有人告訴你怎麼做的，GSD 或 gstack 會讓你舒服；喜歡自己掌控的，Matt Pocock 更適合；想要保留工作方式但修正 agent 的壞習慣，Superpowers 是最低侵入性的選擇。

### 維度三：AI 行為約束的機制

四個系統都在解「怎麼讓 AI 遵守規則」，但用了完全不同的機制。

Superpowers 用的是 **Iron Law + Rationalization Table**。基本結構是：用命令格式宣告絕對規則（`NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST`），然後在同一份文件裡列出所有可能的例外藉口並一一反駁——「我們時間趕」、「這個太簡單不需要測試」、「我之後再補」——每個 rationalization 都有一個對應的 reality。Superpowers 的筆記明確引用了 Cialdini 的說服研究：不列出 rationalization 的規則，容易被 agent 以「這種特殊情況不適用」繞過；顯式反駁，大幅提高遵守率。另外還有 Gate Function 模式：`BEFORE X: 1. 2. 3. ONLY THEN: X`，讓前置條件變成可執行的 checklist。

GSD 用的是 **Quality Gates as Code**。把「AI 作弊手法」編碼成自動檢查：schema 改了但沒有 migration 文件？執行中止。PLAN.md 沒有覆蓋 REQUIREMENTS.md 的所有需求？執行中止。安全敏感的 code 改了但沒有 threat model 參考？執行中止。它不信任 AI 說「我考慮過了」，只信任可驗證的 artifact。另外，GSD 的 PLAN.md 用 XML 結構化——`<context>`、`<requirements>`、`<constraints>`、`<acceptance_criteria>`、`<out_of_scope>`——不是為了好看，是因為 XML 邊界讓 AI 更難把 context、需求、約束搞混。

gstack 用的是 **Proactive Skill**。一般的 skill 是你輸入 `/skill-name` 才觸發。gstack 的多數規劃 skill 有「主動觸發」設定：agent 偵測到特定情境，**不等你問**，主動建議觸發 skill。用戶描述一個新 product idea？agent 不直接回答，先觸發 `/office-hours`。有 stack trace 出現？agent 先觸發 `/investigate`，不猜測原因。每個 skill 的 `description` frontmatter 有明確的「主動觸發條件」：`Proactively invoke this skill (do NOT answer directly) when: ...` 這個 `do NOT answer directly` 是強制停止直接回答的信號。

Matt Pocock 用的是 **Feedback Loop Engineering**。他引用 Pragmatic Programmer：「The rate of feedback is your speed limit.」AI 寫壞 code 的根本原因往往是沒有 feedback——它生成 code，你說「看起來 OK」，合進去，幾週後才發現有 bug。`/tdd` 的核心邏輯是：讓 AI 先寫失敗的 test，再寫 code。Test 是即時的 feedback loop——red 確認問題真的存在，green 確認 fix 真的有效，refactor 在有 safety net 的情況下改善。不是「寫更多 test」，是「把 feedback 週期縮短到秒級」。

---

## 每個系統的設計代價

選擇一個工具，就是接受它的取捨。這四個系統各自放棄了某些東西。

**GSD** 放棄的是靈活性。它是高儀式感的工具——你開始用它，你的工作流就被它擁有了。對從零開始的新 project 很友好，但要把它 retrofit 進一個現有的 codebase，需要先花時間把已有的架構轉化成它的文件格式。另外，discuss → plan → execute 的強制分離雖然好，但有時候你就是想快速試一個想法，在這個 loop 裡會覺得很重。

**gstack** 放棄的是輕量性。23 個角色意味著你要知道什麼時候叫誰——`/plan-ceo-review` 和 `/plan-eng-review` 的差別是什麼、`/qa` 和 `/qa-only` 什麼時候用哪個。另外 browser daemon 需要持久化的 Chromium process，有環境依賴。它的功能密度是優點，但對剛開始的人來說，可能需要一段時間才能知道自己真正需要哪幾個 skill。

**Superpowers** 放棄的是 context rot 的解法。它非常擅長修正 agent 的行為缺陷，但它對 context 本身不做任何管理。session 跑了 30 個 task 之後，context 一樣會被填滿，一樣會開始劣化。Superpowers 讓每個節點的行為更正確，但長 session 的品質下降問題，它沒有答案。

**Matt Pocock** 放棄的是強制執行。工具是 composable 的，但沒有人強迫你用。你可以每天開 session 不 `/grill-with-docs`、不讀 CONTEXT.md、不跑 `/improve-codebase-architecture`——工具不會說話，agent 也不會提醒你。它假設你有足夠的工程直覺和自律，知道什麼時候該拿出哪個工具。

---

## 它們可以疊加嗎

可以，而且疊加有意義——前提是你知道在疊加什麼。

一個常見的組合是：**Matt Pocock（需求釐清 + 共享語言）+ GSD（任務執行 + context 隔離）+ Superpowers（行為 gate）**。邏輯是：Matt Pocock 的 `/grill-with-docs` 確保你開始做正確的事、CONTEXT.md 確保 AI 用正確的語言說話；GSD 的 Discuss-Plan-Execute loop 確保大型任務被拆成有 fresh context 執行的原子單位；Superpowers 的 verification gate 確保每個子任務完成時真的完成了。

另一個合理的組合是：**gstack（角色視角 + learnings 持久化）+ Superpowers（Iron Law + 驗證 gate）**。gstack 的 proactive skill 讓規劃節點不容易被跳過，Superpowers 的 gate 確保實作節點的行為紀律。

不太合理的組合是把 GSD 和 gstack 同時用在同一個 project 的同一個 phase——兩個都想擁有你的工作流，會互相干擾。

---

## 把這些模式帶出 Coding Agent，用在哪都成立

在拆完這四個系統之後，有一件事值得說清楚：這些設計模式的本質不是「Claude Code 的插件設計」，而是 **Agentic Close-Loop 的通用元件**。Iron Law、Gate Function、Fresh Context、Proactive Skill——每一個都可以直接移植到任何需要 AI agent 穩定輸出的系統。

你可以把四個核心機制抽象出來，然後把它們放進任何需要 AI agent 穩定輸出的系統裡：

**Iron Law + Gate Function** 解決的是 agent 系統性走捷徑的問題。它和 coding 沒有直接關係——任何 agent 在追求「完成」時都會有悄悄降低標準的傾向。拿 SRE incident response 來說，agent 的典型捷徑是看到 error log 就猜原因、直接執行 remediation。把 Iron Law 套進去：

```
NO REMEDIATION WITHOUT ROOT CAUSE EVIDENCE FIRST

BEFORE executing any fix:
1. Identify which log / metric is the evidence
2. State what the root cause hypothesis is
3. Explain why this evidence supports it
4. ONLY THEN: remediate
```

這個結構和 Superpowers 的 `systematic-debugging` 完全同構，只是 domain 換了。

**Fresh Context per Task** 解決的是 context 汙染的問題。這在任何 multi-agent pipeline 裡都存在——一個負責分析的 agent 跑了十幾個 subtask 之後，早期的分析假設會把後期的判斷污染掉。GSD 的解法（每個任務用全新 subagent，從文件重建 context）可以直接移植到任何需要長時間多步驟的 agentic 工作流。

**Proactive Skill Routing** 解決的是「agent 直接回答，跳過必要流程」的問題。在產品設計的場景裡，這個問題非常常見：你說「我想做一個 X 功能」，agent 馬上給你 5 個實作建議，但你還沒想清楚 X 解決誰的問題、在哪個用戶旅程裡出現。gstack 的 proactive trigger 模式——在 description 裡寫 `Proactively invoke this skill (do NOT answer directly) when: 用戶描述新功能想法`——強迫 agent 先跑 office hours 流程再繼續。這個設計移植到任何 conversational agent 都成立。

**Quality Gates as Code** 解決的是「AI 說達到標準但沒有可驗證 artifact」的問題。程式優化是一個很典型的例子：agent 說「我優化了這段 code，現在快多了」，但沒有 benchmark 數字。把 GSD 的 Quality Gate 套進去：有沒有優化前的 benchmark？有沒有優化後的 benchmark？兩個數字放在一起，才算完成。「agent 說」不算，可驗證的數字才算。

Superpowers 的設計文件裡有一段話很直接：「識別 agent 的常見失敗模式，為每個失敗模式設計一個 skill，設計 bootstrap injection，設計主工作流程 skill。」這個流程跟 domain 無關。SRE、資料分析、研究助手、產品設計——只要你願意花時間把「agent 在這個領域裡最常走的捷徑」列出來，這四個工具的設計模式都可以複製過去。

---

## 一個更有用的問題

與其問「哪個工具更好」，更有用的問題是：**我現在面對的主要失敗模式是什麼？**

如果你的問題是 agent 直接開始做、猜 bug、說完成但沒驗證——那是行為問題，Superpowers 是最直接的答案。

如果你的問題是長 session 跑到後來 agent 開始亂、早期決策被遺忘——那是 context rot 問題，GSD 的 fresh context per task 是最直接的解法。

如果你的問題是做出來的東西不是你要的、codebase 兩個月後開始看不懂——那是 misalignment 和架構腐爛問題，Matt Pocock 的 grilling 和 CONTEXT.md 是針對性的工具。

如果你的問題是需要完整的 review 機制——QA、設計審查、安全掃描、deploy 驗證——gstack 是最完整的虛擬團隊。

這四個問題可以同時存在，工具也可以疊加。但一個一個識別自己的失敗模式、一個一個補對應的工具，比一次性把所有東西裝上去然後搞不清楚在幹什麼，要有效得多。

---

> 這四個系統共同說明了一件事：AI coding agent 的失敗模式是可以被系統性識別和設計的。它們不是玄學，不是「有時候用 AI 會不準」——每一個失敗模式背後都有機制，每一個機制都可以被 gate、被 law、被 loop 對付。你只需要先想清楚，你在修哪層漏洞。

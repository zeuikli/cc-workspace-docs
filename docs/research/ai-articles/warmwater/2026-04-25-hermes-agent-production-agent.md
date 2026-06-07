---
url: "https://warmwater.dev/blog/hermes-agent-production-agent"
title: "Hermes-agent：從原始碼看一個為 Production 設計的 Agent 系統"
date: 2026-04-25
category: Source Code
source: warmwater.dev
---

[
← Source Code ](/blog?tag=Source%20Code)  Source Code 
 
# Hermes-agent：從原始碼看一個為 Production 設計的 Agent 系統
 
 2026-04-25 · — views  
  
  
讓 Agent 跑起來不難——把 LLM API 包一層、加幾個工具、跑個 while loop，大概一個下午就能做出一個能用的東西。真正麻煩的問題，通常是後來才浮現的：token 費用怎麼控制？context 滿了怎麼辦？記憶系統怎麼讓 Agent 下次還記得上次的事？這些問題不在 demo 裡出現，但在真實使用裡是逃不掉的。


讀 hermes-agent 的原始碼，我發現這些問題幾乎每一個都有對應的設計——而且不是臨時補上去的，是從一開始就長在架構裡的。12155 行程式碼、40 個工具、8 種記憶體 Provider、13 個 Plugin 注入點，這些數字本身說明了一件事：hermes-agent 的作者在意的問題，比「讓 Agent 回答問題」要更難一層。


這篇我想拆開幾個關鍵的設計機制，試著解釋它的選擇背後在想什麼。


**讀完精華版（2 分鐘），你會理解：**


- hermes-agent 的 AIAgent 作為 Harness 是怎麼組織的
- 為什麼 System Prompt 的「穩定性」是一個工程問題，不只是設計偏好
- Memory Fencing 是什麼，為什麼記憶召回之後不能直接放進 Context
- Context 壓縮是怎麼運作的——以及為什麼這是長期 Agent 的必要機制
- Skill 系統 + RL 訓練迴路：hermes-agent 最特別的設計


---


## 精華版


| 設計維度 | hermes-agent 的選擇 | 工程目的 |
| --- | --- | --- |
| 架構模式 | AIAgent Harness + Plugin 注入點 | 統一管控 lifecycle，Plugin 擴充不改核心 |
| System Prompt 策略 | Session 開始 build 一次，之後不重建 | 維持 prefix cache，省下 70-80% input token 費用 |
| 記憶機制 | MEMORY.md + SQLite FTS5 + 外部 Provider 三層 | 按使用頻率分層存取，降低每輪 context 負擔 |
| Context 壓縮 | 使用量達 75% 觸發，四步驟壓縮後留 parent_session_id | 長期 Agent 不崩潰，同時保留完整對話歷史鏈 |
| 技能演進 | Skill 系統 + Trajectory 存成 ShareGPT 送 RL | 使用紀錄直接成為訓練資料，Agent 越用越好 |


**各子系統一句話：**


- **AIAgent Harness**：`run_conversation()` while loop 包含七件事——系統提示、對話狀態、LLM 呼叫、工具執行、記憶處理、Context 壓縮、中斷訊號，是整個 Agent 的統一入口。
- **System Prompt 穩定性**：Anthropic prefix cache 要求 prompt 前綴每輪完全一樣，hermes-agent 因此把 system prompt 存進資料庫只 build 一次，動態資訊改從 `pre_llm_call` hook 注入 user message。
- **Memory Fencing**：召回的記憶用 `<recalled_memories>` XML 標籤包裹後才放進 context，讓模型能區分「過去記得的事」和「使用者現在說的話」，且 fence 內容用完即走、不 persist。
- **Context 壓縮**：context 使用量到 75% 觸發四步驟壓縮（截短 tool result → 找邊界 → LLM 摘要 → 替換），壓縮後 session 記錄 `parent_session_id` 維持歷史可溯。
- **Skill + RL 訓練迴路**：每次對話的 trajectory 存成 ShareGPT 格式，可直接送 Atropos RL pipeline 微調，讓 hermes-agent 同時是任務框架也是資料收集系統。


**設計問題簡答：**


**Q：為什麼 system prompt 不能每輪重建？**
Anthropic API 的 prefix cache 在 prompt 前綴不變時省下 70-80% input token 費用。system prompt 只要每輪有任何差異，cache 就失效。hermes-agent 為此把動態資訊的注入點移到 user message，讓 system prompt 永遠保持穩定。


**Q：Memory Fencing 解決的是什麼問題？**
召回的記憶如果直接混入 context，模型會把舊的偏好或事件當成「使用者剛才說的話」來解讀。XML 標籤提供語義邊界，讓模型清楚分辨記憶來源。fence 內容不 persist 還有第二個理由：避免破壞 system prompt 的 prefix cache。


**Q：Context 壓縮的觸發時機為什麼是 75%？**
留 25% 餘量是為了讓壓縮動作本身（送 LLM 做摘要）有空間完成，而不是等到 context 真的滿了才壓縮、卻發現已經沒有空間執行摘要請求。


**Q：Skill + RL 迴路的設計意圖是什麼？**
Skill 系統決定 Agent 現在能做什麼（載入 Markdown 定義的技能），RL 迴路決定 Agent 未來會怎麼改善（使用紀錄變訓練資料）。這讓 hermes-agent 不只是執行框架，而是一個有自我改善路徑的系統。大多數框架只有前者，沒有後者。


**Q：工具平行執行的分類邏輯是什麼？**
hermes-agent 把工具分三類：絕對不能平行的、可以安全平行的、路徑相依的（如同時修改同一檔案）。分類是明確的設計決策，最多 8 個 ThreadPoolExecutor worker，分類決定哪些能同時跑。


---


> 
以下是完整版，按需取用。


## AIAgent：一個 Harness，不是一個 Chatbot


hermes-agent 的核心是一個叫做 `AIAgent` 的類別。它不是一個「對話機器人」，而是一個 Harness——它的職責是把所有東西包在一起，讓 Agent 能夠執行。


`AIAgent` 大概負責七件事：管理系統提示、維護對話狀態、呼叫 LLM（透過 Provider Layer）、執行工具、處理記憶體、管理 Context 壓縮、還有處理中斷訊號。這些事情放在一起，核心是一個 `run_conversation()` 方法，裡面跑一個 while loop。


每一輪迭代大概是這樣：組合這輪要送給 LLM 的訊息（含 cache marker）→ 呼叫 API（內建 retry 機制，出錯時分類後 rotate/retry）→ 把回應 normalize 成統一格式 → 有工具呼叫的話執行工具 → 沒有工具呼叫的話，這一輪結束，回傳最終回應。


工具執行這一塊，hermes-agent 把工具分成三類：絕對不能平行的、可以安全平行的、還有路徑相依的（例如同時修改同一個檔案會有問題）。這個分類本身不複雜，但它是明確的設計決策，而不是「先跑跑看」——最多 8 個 ThreadPoolExecutor worker，分類決定哪些可以同時跑。


Credential Pool 也在這一層管理：4 種策略（fill_first、round_robin、random、least_used），遇到 429 會進 cooldown，OAuth token 到期會自動 refresh。這些細節加在一起，是「讓 Agent 能夠 24/7 跑著」的基礎設施。


---


## System Prompt 的穩定性問題


這個地方是我讀 hermes-agent 時覺得最有意思的設計決策之一。


大多數框架在每一輪對話都會重新組建 system prompt——工具清單、使用者偏好、目前任務狀態，塞進去，送出去。這樣做很直覺，但有一個代價：Anthropic 的 API 有一個叫做 **prefix cache** 的機制，意思是如果你送出去的 prompt 前綴和上一次完全一樣，API 就不需要重新處理那部分——可以省下 70-80% 的 input token 費用。只要 system prompt 每輪都不一樣，這個 cache 就完全沒用。


hermes-agent 的做法是：System Prompt 在 session 開始時 build 一次，存進資料庫，之後每一輪都直接讀出來用，永遠不重建。


這帶出了一個問題：如果不能改 system prompt，需要在對話過程中動態注入資訊（比如「這個使用者偏好用繁體中文」、「這個 session 有特殊的 tool policy」），要怎麼做？


答案是 Plugin Hooks。hermes-agent 有 13 個注入點分佈在 Agent lifecycle 的不同位置。其中 `pre_llm_call` 這個 hook 允許 Plugin 在每次呼叫 LLM 之前，把內容注入進**使用者訊息**裡——而不是 system prompt。位置的差異很重要：注入 user message 不會破壞 system prompt 的 prefix cache，注入 system prompt 會。


---


## Memory 的三層結構與 Memory Fencing


hermes-agent 的記憶體系統分三層，從輕到重：


最輕的一層是 **MEMORY.md**，一個存在檔案系統上的 Markdown 文件，裡面是結構化的長期記憶，每次 session 開始會直接載入。第二層是 **SQLite FTS5 全文搜尋**，用來搜尋歷史對話，支援 BM25 排名，查不到的 CJK 場合 fallback 到 LIKE。第三層是**外部 MemoryProvider**——一個 ABC，允許接不同的 backend，每個 session 只能有一個外部 Provider。粗略分工：MEMORY.md 是「常駐的基本認識」，FTS5 是「可搜尋的事件記憶」，外部 Provider 是「特定應用需要的向量記憶或其他結構」。


這個三層架構本身不難理解，但有一個設計細節值得特別說：**Memory Fencing**。


當 Agent 從 memory 系統召回記憶，準備放進這一輪的 context 時，hermes-agent 會用一個 XML 標籤把召回的內容包起來：


```

  [召回的記憶內容]

```


這個 fence 是語義上的隔離——告訴模型：這塊內容是「被召回的背景資訊」，不是使用者現在說的話。


舉個具體的情境：假設上次對話裡使用者說「我偏好簡短的回答」，這條記憶在這一輪被召回之後進入 context。如果沒有 fence，模型可能把它和目前訊息混淆，把舊的偏好當成「使用者剛才說的話」來解讀。有了 fence，模型能分清楚「這是我記得的事」和「這是使用者現在說的事」——兩件在語義上完全不同的事。


比較反直覺的是，這個帶著 fence 的 memory context **不會被 persist** 到對話歷史裡。每次 session 都是重新召回、重新 fence、重新放進 context。原因有兩個：一是 fence 的內容如果被存進去，下一次 context 裡就會出現「我上次召回了哪些記憶」這件事，這不是真正的對話，累積多輪之後 context 裡會有很多這種召回殘留，開始影響模型的判斷；二是 fence 內容一旦改變，system prompt 的 prefix cache 就會失效——和 hermes-agent 整個 caching 策略是衝突的。


所以記憶這件事，hermes-agent 的態度是：召回、隔離、用完即走。


---


## Context 壓縮：長期 Agent 的必要設計


Agent 跑得夠久，context window 一定會滿。hermes-agent 的 ContextEngine 是一個 ABC，策略可以替換，但預設實作是一個 4-phase 壓縮演算法，在 context 使用量到達 75% 時觸發。


壓縮的四個步驟大致是：先把 tool call 的結果截短（這些通常最冗長、保留價值最低）→ 找到一個合適的壓縮邊界（不要在對話中間切斷）→ 把要壓縮的段落送給 LLM 做摘要 → 用摘要替換原始內容，重新組合 context。


壓縮後的 session 會記錄一個 `parent_session_id`，指向壓縮前的 session。這讓 hermes-agent 可以追溯完整的對話歷史鏈，即使 context 已經被壓縮過很多次。


---


## Skill 系統 + RL 訓練迴路


這個是 hermes-agent 和其他兩個框架差異最大的地方。


hermes-agent 有一個 Skill 系統：每個 skill 是一個 Markdown 文件（`SKILL.md`），包含 frontmatter（name、description、trigger 條件）和技能內容。這些 skill 存在一個 Skills Hub 裡（GitHub 來源），Agent 可以在對話過程中動態載入。Agent 有一個 skill nudge daemon，每 10 次工具呼叫會提示一次，看看有沒有適合當前任務的 skill 可以使用。


這個機制本身還算正常。真正不同的是下一層：**Trajectory → RL 訓練迴路**。


hermes-agent 會把對話軌跡（每一輪的輸入、工具呼叫、輸出、使用者反饋）存成 ShareGPT 格式。這些軌跡可以被 batch_runner 批次處理，然後送進 Atropos RL 訓練 pipeline，用來微調模型。


這個設計的意涵是：hermes-agent 不只是一個讓 Agent 完成任務的框架，它還是一個資料收集系統。每一次使用，都在累積未來改善模型的訓練資料。Skill 系統決定了 Agent 現在能做什麼，RL 迴路決定了 Agent 未來會變成什麼。


---


## 這些設計在說什麼


拆開這幾個機制之後，hermes-agent 的設計哲學大概是這樣：系統的每一層都在為「長期穩定運作」和「持續改善」服務。System Prompt 穩定性是為了讓 token cost 可控；Memory Fencing 是為了讓記憶系統不污染 context；Context 壓縮是為了讓長對話不崩潰；RL 迴路是為了讓 Agent 越用越好。


這些選擇放在一起，讀起來更像是一個有一定 production 運作經驗的人，把踩過的坑轉成了架構上的防線。


---


> **結語**：hermes-agent 最讓我印象深刻的不是某個單一機制，而是這些機制加在一起，形成了一種一致的設計意圖——讓 Agent 不只是能跑，而是跑得久、跑得穩、然後越跑越好。


## 延伸閱讀


- [OpenClaw：從原始碼看一個 Agent 平台的工程選擇](/blog/openclaw-agent) — 對照版：同樣的問題，OpenClaw 給出的是完全不同的答案
- [hermes-agent vs OpenClaw：兩個 Agent 框架，同一批問題，不同的答案](/blog/hermes-agent-vs-openclaw-agent) — 直接對比：兩個框架在 context 管理、error recovery、記憶設計上的差異
- [Harness Engineering 的地基：LLM Session 設計框架](/blog/llm-session-harness) — hermes 的 session 機制背後：Durable Session 四種策略的理論框架

  
  
 [ Source Code ](/blog?tag=Source%20Code)[ Agentic System ](/blog?tag=Agentic%20System) 
 

### 相關文章
[System Design

Agent 要怎麼進化？六個系統的 Self-Improvement 機制比較

2026-05-22
](/blog/agent-self-improvement-design-comparison)[
System Design

SOUL 設計決定了 Agent 是什麼：六個 Agentic System 的 system prompt 比較

2026-05-22
](/blog/agent-soul-design-comparison)[
Source Code

不預裝能力，只定義生長方式：GenericAgent 原始碼解析

2026-05-22
](/blog/generic-agent-source-code)

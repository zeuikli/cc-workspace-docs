---
url: "https://warmwater.dev/blog/agent-soul-design-comparison"
title: "SOUL 設計決定了 Agent 是什麼：六個 Agentic System 的 system prompt 比較"
date: 2026-05-22
category: System Design
source: warmwater.dev
---

[
← System Design ](/blog?tag=System%20Design)  System Design 
 
# SOUL 設計決定了 Agent 是什麼：六個 Agentic System 的 system prompt 比較
 
 2026-05-22 · — views  
  
  
Agent 系統裡最少被討論、但影響最深遠的設計決策，不是記憶系統、不是工具數量，而是 **SOUL**——也就是 system prompt 的核心定義那幾行字。


這篇文章是我把六個 agentic system 的 SOUL 設計和初始工具配置攤開來比較之後的觀察筆記。這些系統分別是：GenericAgent、HermesAgent、HolmesGPT、DeerFlow、NanoClaw、OpenClaw。每一個系統的 SOUL 背後都埋著一個設計假設：**這個 agent 應該是什麼樣的存在？**


**讀完這篇，你會理解：**


- 為什麼「能力宣言」是 SOUL 設計裡最重要的一個選擇軸
- 工具配置如何作為 SOUL 的架構補丁，補上純文字 prompt 無法可靠覆蓋的部分
- 把行為協議（behavioral protocol）內嵌進 SOUL 的設計意圖
- 動態 SOUL 和靜態 SOUL 的設計差異


這篇不是教你如何寫 system prompt 的教學，而是透過真實系統的比較，建立對 SOUL 設計維度的直覺。


---


## 六個系統的 SOUL 快照


在開始分析之前，先讓六個 SOUL 說說話。


**GenericAgent**（極簡自進化框架，約 3K 行 Python）：


```
# Role: Physical-Level Omnipotent Executor
You have full physical access: file I/O, script execution, 
browser JS injection, and system-level intervention.
Never deflect with "can't do it" — don't speculate, use tools to probe.
```


**HermesAgent**（Nous Research，約 12K 行 Python）：


```
You are Hermes Agent, an intelligent AI assistant created by 
Nous Research. You are helpful, knowledgeable, and direct. 
You assist users with a wide range of tasks including answering 
questions, writing and editing code, analyzing information, 
creative work, and executing actions via your tools. 
Be targeted and efficient in your exploration and investigations.
```


**HolmesGPT**（CNCF Sandbox，SRE 事故調查 Agent）：


```
You are HolmesGPT version , a tool-calling AI 
assist provided with common devops and IT tools that you can use 
to troubleshoot problems or answer questions.
Ask for multiple tool calls at the same time as it saves time for the user.
Do not say 'based on the tool output' or explicitly refer to tools at all.
```


**DeerFlow**（LangGraph，企業級 Agent System）：


沒有獨立的 SOUL 文件。行為由 12 層 Middleware chain 定義：Logging → Tracing → ContextInjection → RateLimit → Guardrail → Memory → LoopDetection → Summarization → TodoList → SubagentLimit → ImageContext → Clarification。SOUL 不在文字裡，在架構裡。


**NanoClaw**（TypeScript，通訊平台 Agent 系統）：


SOUL 透過兩個文件組裝：`/app/CLAUDE.md`（共享基底）+ `/workspace/agent/CLAUDE.md`（由 host 組裝的 per-agent 指令）。沒有單一的 SOUL.md，而是組合式身份。


**OpenClaw**（TypeScript，自托管 Agent OS）：


SOUL 透過三層注入：`identity.ts`（identity config，含名字和 emoji）+ `AGENTS.md`（workspace 層級指令）+ `agent-bootstrap hook`（pre-run system prompt 注入）。身份是可插拔的，不是預設的。


---


## Pattern 1：無邊界全能 vs 有邊界頑強，能力宣言的兩個方向


六個系統裡，最有趣的對比是 GenericAgent 和 HolmesGPT，兩者代表同一個軸的兩端。


GenericAgent 的第一行是 `Physical-Level Omnipotent Executor`。這不只是角色名稱，這是一個承諾：我能存取一切，遇到問題就用工具探測，不說「做不到」。這個設計的核心信念是：*如果工具夠強，能力宣言可以無上限*。系統 prompt 裡有一段原則：「Never repeat an action without new information」，失敗了就升級調查方法，但不能以「我沒有這個能力」為由退出。


HolmesGPT 的宣言更保守，但方向完全不同。它的第一句話明確說自己是 “a tool-calling AI assist provided with common devops and IT tools”，不是全能的，是有邊界的。但在這個邊界之內，它極度頑強：system prompt 裡有一段說「if you cannot find the resource/application that the user referred to, assume they made a typo… try to find substrings or search for the correct spellings」。它不是在說「我不行」，而是在說「在我的域裡，我不放棄」。


這個對比說明能力宣言有兩個維度：**邊界在哪裡**，以及**邊界之內的堅持程度**：


|  | 無邊界全能型 | 有邊界頑強型 |
| --- | --- | --- |
| 代表系統 | GenericAgent | HolmesGPT |
| 對失敗的預設 | 升級策略，換方法繼續 | 換查詢方式，絕不提前放棄 |
| 適用場景 | 需要高度自主的全能代理 | Domain expert，邊界明確但深度強 |
| 風險 | 越界執行、幻覺式解決 | 邊界外的任務被拒絕或調查不足 |


---


## Pattern 2：行為協議應該內嵌進 SOUL，還是交給架構強制？


HolmesGPT 的 system prompt 是我看過最長、結構最完整的一個。它不只定義角色，而是把完整的調查方法論直接嵌入 SOUL：


```
## Phase 1: Initial Investigation
1. Check for matching skills
2. Start with TodoWrite: Create initial investigation task list
3. Execute ALL tasks systematically: Mark each task in_progress → completed

## Phase Evaluation and Continuation
After completing ALL tasks in current list, you MUST:
- "Do I have enough information to completely answer the user's question?"
- "Are there gaps, unexplored areas, or additional root causes?"
- "Have I followed the 'five whys' methodology to the actual root cause?"
```


這個設計有一個強烈的意圖：**不信任 LLM 的自然行為**，所以把正確的調查流程用強制性語言寫死在 SOUL 裡。「INVESTIGATION FAILURE」、「VIOLATION CONSEQUENCES」這類措辭，目的是讓模型在自然傾向於提前結束調查的時候，有足夠強的 prompt signal 繼續走完流程。


HermesAgent 做法不同，但出於同樣的擔心。它有幾段常數：`TOOL_USE_ENFORCEMENT_GUIDANCE`、`MEMORY_GUIDANCE`、`SKILLS_GUIDANCE`，這些 guidance 會在特定條件下注入 system prompt。比如使用 GPT/Gemini 系列模型時，才注入 `OPENAI_MODEL_EXECUTION_GUIDANCE`，因為這些模型有已知的「承諾但不執行」問題。HermesAgent 把 behavioral protocol 設計成**模型感知的**，不同的 LLM 得到不同的 SOUL 附件。


這兩個系統揭示了一個選擇：你把行為約束放進 SOUL，還是放進架構？HolmesGPT 選擇放進 SOUL，讓模型在文字層面遵守。DeerFlow 選擇放進 12 層 Middleware chain，讓架構強制執行（`LoopDetectionMiddleware` 偵測卡住、`ClarificationMiddleware` 中斷等待用戶）。越靠近 prompt 越透明，越靠近架構越可靠——但也越難調試。


---


## Pattern 3：工具配置是 SOUL 的架構補丁


SOUL 文字能定義 agent 的世界觀和行為傾向，但有一類約束它做不好：「這個 agent 只能做 X，不能做 Y」。你可以在 SOUL 裡寫「你是 orchestrator，只路由不執行」，但 LLM 看到工具就可能忍不住用。在多 agent 系統裡，這個問題特別明顯。當你希望一個 agent 只分配任務不執行任務，最可靠的方法是直接拿走讓它能執行的工具，而不是靠文字約束。


這是工具配置作為 SOUL 補丁的邏輯：**當文字 SOUL 無法可靠覆蓋某個行為邊界，就用工具配置來劃定它。**


這個邏輯反過來也成立：**給了什麼工具，就是在宣告這個 agent 能成為什麼**。GenericAgent 的 9 個原子工具（`code_run`、`web_execute_js`、`file_patch` 等）和 “Omnipotent Executor” 的身份不是矛盾，而是一體兩面，工具極簡，但每個工具都是通向任意能力的路徑。HolmesGPT 的 40+ YAML toolsets（`kubectl`、`helm`、`prometheus`…）不需要 SOUL 說「我是 SRE agent」，工具清單本身就是這句話。


從這個角度看，設計 SOUL 和設計 toolset 是同一件事的兩個面向：文字 SOUL 定義 agent 的世界觀和行為傾向，工具配置劃定它實際能走到的邊界。缺一不可，但當兩者衝突時，工具配置贏。


---


## Pattern 4：SOUL 可以是動態的，三種動態設計模式


大多數系統的 SOUL 是靜態的，定義好、啟動時注入、整個對話不變。但幾個系統設計了動態 SOUL。


**HermesAgent** 的 `SOUL.md` 有一個細節：「This file is loaded fresh each message — no restart needed.」這讓 SOUL 可以在不重啟 agent 的情況下即時更新。如果你想改變 agent 的人格或指令，只要修改 SOUL.md，下一條訊息就生效。這把 SOUL 從「部署時配置」變成「運行時配置」。加上 memory 注入（`<memory-context>` fence），每個 turn 的 SOUL 實際上是固定身份加上動態記憶，agent 知道「我是誰」，也知道「我目前知道什麼」。


**HolmesGPT** 用 Jinja2 template 組裝 system prompt，每次調用時根據 feature flags（`todowrite_enabled`、`skills_enabled`、`cluster_name`）產生不同的 SOUL。同一個系統在不同配置下是不同的 agent。這讓 SOUL 從「per-agent 設定」變成「per-deployment 設定」。


**NanoClaw** 用 `CLAUDE.md`（host 組裝）加上 `CLAUDE.local.md`（agent 可寫，自我描述）的雙層設計。Agent 有一個不可篡改的 base identity（RO mount），同時有一個可以自我更新的 local layer。SOUL 帶有只讀區域和可寫區域的分層，base identity 永遠穩定，但 agent 可以在 local layer 記錄自己學到的東西。


---


## Pattern 5：六個系統如何應對「做不到」


把所有系統放在一起看，有一個維度特別清晰：這個 agent 在遇到「做不到」的時候，預設行為應該是什麼？


| 系統 | 對失敗的預設 |
| --- | --- |
| GenericAgent | 升級調查策略，3次失敗才換方法 |
| HermesAgent | 用 retry_utils + error_classifier 自動分類和重試 |
| HolmesGPT | multi-phase investigation，不完成不給答案 |
| DeerFlow | LoopDetection middleware 偵測卡住，Clarification middleware 問用戶 |
| NanoClaw | Circuit breaker（最多 5 次 backoff，然後停止） |
| OpenClaw | Model fallback chain（切換模型再試） |


這個比較揭示了一個有趣的設計維度：**你是否信任 LLM 的自然行為？**


不信任的系統（HolmesGPT、DeerFlow）用強制性文字或架構機制確保 agent 行為符合預期。信任度高的系統（GenericAgent）把能力宣言設得很高，讓 LLM 自己決定如何解決問題。NanoClaw 和 OpenClaw 的做法則介於中間：不用 prompt 約束，而是用架構層的容錯（circuit breaker、model fallback）來應對失敗。


---


## 設計 SOUL 需要回答的四個問題


六個系統背後有幾個反覆出現的設計軸。每個軸都有各自的假設，以及選擇哪個方向之後必須接受的取捨。


---


### 軸一：你有多信任 LLM 的自然行為？


這是所有 SOUL 設計的底層假設，其他選擇幾乎都從這裡推導出來。


**高信任**：GenericAgent。SOUL 只給原則（「失敗就升級方法，不要重複沒有新資訊的動作」），不給流程。假設 LLM 有足夠的自主判斷能力，不需要被手把手引導。代價是邊界模糊，agent 可能在你不預期的地方做了決策。


**低信任**：HolmesGPT。SOUL 把整個調查流程寫死，用「INVESTIGATION FAILURE」、「VIOLATION CONSEQUENCES」這類強制性語言防止 LLM 提前放棄。假設沒有明確的流程約束，模型會自然走捷徑。代價是 SOUL 很長、成本高，而且簡單問題也會走完整個 multi-phase 流程。


**架構信任**：DeerFlow。不信任文字 SOUL，改用 12 層 Middleware chain 強制執行行為約束。假設程式碼比文字更可靠、更好維護。代價是透明度，你無法靠讀 SOUL 理解 agent 的行為，要讀 middleware 程式碼。


---


### 軸二：SOUL 應該靜態還是動態？


靜態 SOUL 在部署時固定，整個生命週期不變；動態 SOUL 在每次對話、每個 turn，甚至每條訊息都可能不同。


**靜態**：GenericAgent 是最乾淨的靜態 SOUL，一個文字檔，所有 session 共用同一份身份。假設 agent 的世界觀不需要隨時間或 context 改變。


**運行時可更新**：HermesAgent 的 SOUL.md 每條訊息重讀，讓 SOUL 變成運行時配置而非部署時配置。代價是需要嚴格管理 SOUL 的穩定性。HermesAgent 特別強調 system prompt 跨 turn 不能改動，因為改動會破壞 Anthropic prompt cache，直接影響成本。這是動態 SOUL 的隱藏工程要求：動態是 feature，但穩定性管理是必要的代價。


**配置驅動**：HolmesGPT 用 Jinja2 template，根據 feature flags（`todowrite_enabled`、`cluster_name`…）在每次調用時產生不同 SOUL。同一個系統在不同 deployment 下是不同的 agent。假設 SOUL 應該跟著部署環境走，而不是跟著 agent 自身走。


**分層可寫**：NanoClaw 的 `CLAUDE.md`（RO）加上 `CLAUDE.local.md`（RW）設計讓 base identity 永遠穩定，但 agent 可以在 local layer 累積學到的東西。假設有些 SOUL 是不可篡改的核心，有些是應該隨經驗演化的部分。


---


### 軸三：行為約束要放在文字裡，還是架構裡？


這個選擇決定了誰負責「讓 agent 行為符合預期」，是 LLM 自己（靠讀懂 SOUL），還是系統（靠程式碼強制）。


**文字約束**：HolmesGPT。優點是透明，開發者和用戶都能理解 agent 為什麼做某件事。缺點是可靠性依賴模型的 instruction-following 能力，而且 prompt 越長越貴。


**架構約束**：DeerFlow 的 middleware chain、NanoClaw 的 container isolation。優點是比文字更可靠、更可測試。缺點是調試複雜，行為由程式碼決定，不是文字。


**工具邊界約束**：在多 agent 系統裡，最直接的行為約束是直接拿走 agent 不應該有的工具。你想要一個只路由任務不執行任務的 orchestrator？與其在 SOUL 裡反覆說，不如拿走它的 `execute_code`、`read_file` 等工具。工具配置在這裡是 SOUL 的架構補丁，補上純文字無法可靠覆蓋的邊界。


---


### 軸四：SOUL 的 scope 是全局的，還是 per-context 的？


有些系統有一個全局 SOUL，所有對話共用；有些系統的 SOUL 隨著平台、模型、或 agent 角色而變化。


**全局**：GenericAgent 和 HolmesGPT。每個 session 看到的是同一份 SOUL（HolmesGPT 雖有 feature flags，但每次 deployment 固定）。假設 agent 的身份不應該因為用戶或平台不同而改變。


**平台感知**：HermesAgent 根據平台（CLI / Telegram / Discord / WhatsApp）在 SOUL 裡注入不同的 platform hints，告訴 agent「你現在在哪」。假設 agent 的溝通方式應該跟著傳訊管道走（Telegram 支援 markdown，WhatsApp 不行）。


**可插拔身份**：OpenClaw 的 `identity.ts` 讓每個 agent 有獨立的名字、emoji、和行為設定，透過 `agent-bootstrap hook` 注入。假設 agent 的身份是配置項，不是硬編碼的。適合需要部署多個不同人格 agent 的場景。


---


### 為特殊場景而生的額外設計


幾個系統針對自身的核心使用場景，在 SOUL 裡加了一般系統不會有的設計：


**HolmesGPT 的 hedge language 規則**：SOUL 裡明確要求：「Use hedging language (possible, likely, may) for root cause claims when the root cause cannot be directly confirmed through tool output.」SRE 調查場景裡，過度確信的錯誤結論比「我不確定」更危險，所以把語氣規範直接寫進 SOUL。


**HolmesGPT 的 error message 語義約束**：SOUL 裡有一段非常具體的規則：看到 `authentication failed` 就代表用戶**存在**（不是不存在），看到 `role does not exist` 才代表不存在。這是針對 LLM 常見推理錯誤的防禦性 SOUL，把領域知識硬編碼進 prompt，避免模型做出相反的推論。


**HermesAgent 的模型感知 SOUL 補丁**：針對 GPT/Codex/Gemini，注入額外的 `TOOL_USE_ENFORCEMENT_GUIDANCE`，因為這些模型有已知的「承諾動作但不執行」的行為模式。這是把模型已知行為差異納入 SOUL 設計的思路，你的 SOUL 不應該假設所有 LLM 行為一致。


**NanoClaw 的 prompt injection 防禦**：在 SOUL 組裝階段，對 `SOUL.md`、`AGENTS.md` 等外部文件做 content scanning，偵測 invisible unicode、`ignore previous instructions` 等注入模式，再決定是否注入 system prompt。這是 SOUL 設計裡少見的安全層，因為 agent 長期跑在通訊平台上，收到惡意訊息試圖篡改 SOUL 是真實的攻擊面。


---


## 相關文章


- [Hermes-agent：從原始碼看一個為 Production 設計的 Agent 系統](/blog/hermes-agent-production-agent)
- [OpenClaw：從原始碼看一個 Agent 平台的工程選擇](/blog/openclaw-agent)
- [hermes-agent vs OpenClaw：兩個 Agent 框架，同一批問題，不同的答案](/blog/hermes-agent-vs-openclaw-agent)
- [打開原始碼才發現：三個 Agent 框架，三種截然不同的設計哲學](/blog/agent-20260423)


---


> 
**結語**：SOUL 不只是 agent 的說明書，它是一份關於「這個 agent 在遇到邊界時應該怎麼辦」的契約。設計 SOUL 的本質，是在決定 agent 和人類之間的信任邊界要劃在哪裡。

  
  
 [ System Design ](/blog?tag=System%20Design)[ Harness Engineering ](/blog?tag=Harness%20Engineering)[ Agentic System ](/blog?tag=Agentic%20System) 
 

### 相關文章
[Implement

用 RPG 架構評估 SRE Agent：Kube Arena 設計紀錄

2026-05-28
](/blog/kube-arena)[
System Design

MCP、CLI、還是直呼 API？先看工具長什麼樣

2026-05-23
](/blog/mcp-cli-api-integration)[
System Design

Agent 要怎麼進化？六個系統的 Self-Improvement 機制比較

2026-05-22
](/blog/agent-self-improvement-design-comparison)

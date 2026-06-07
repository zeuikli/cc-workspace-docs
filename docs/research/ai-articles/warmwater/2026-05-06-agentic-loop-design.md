---
url: "https://warmwater.dev/blog/agentic-loop-design"
title: "Agentic Loop 的設計關卡：工具執行、錯誤分類與中斷機制"
date: 2026-05-06
category: Harness Engineering
source: warmwater.dev
---

[
← Harness Engineering ](/blog?tag=Harness%20Engineering)  Harness Engineering  
#  Agentic Loop 的設計關卡：工具執行、錯誤分類與中斷機制 
  2026-05-06 · — views      

在討論 Loop 之前，先釐清一件事：**call 一次 LLM 做完一件事，跟跑一個 Agentic Loop，是完全不同的問題。**


大部分人接觸 LLM 的第一個場景，是這個形狀：build prompt → call LLM endpoint → get result → 結束。中間沒有狀態保存，沒有下一輪，沒有工具執行。這樣的任務，一個 LangChain chain、一個 LangGraph 節點、或任何能把「輸入輸出包成一次 API call」的 workflow 工具都可以解決——任務是確定性的，LLM 回答一次就夠了。


Agentic Loop 不一樣。一個 user request 進來，Agent 自己決定要呼叫哪個工具、看了結果再決定下一步、自己判斷什麼時候任務算完成——這個過程可能跑幾十輪，中間完全不需要人介入。LangChain 針對這個問題推出了 [deepagents](https://github.com/langchain-ai/deepagents)，定位是「batteries-included agent harness」——`create_deep_agent()` 一行就能得到一個帶完整工具集、自動 context 壓縮、sub-agent 支援的 agent，底層跑在 LangGraph 上。


但不管用哪個框架，**loop 本身的基礎設施問題都還是得面對**：工具能不能並行跑、API 出錯怎麼處理、什麼時候該停、怎麼響應外部中斷。這些不在 prompt 設計裡，也不在 graph 的 edge logic 裡——它們在 loop 的執行引擎設計裡。


我第一次做 agent 的時候，核心邏輯大概長這樣：

```
while True:
    response = call_llm(messages)
    if response.tool_calls:
        results = execute_tools(response.tool_calls)
        messages.append(results)
    else:
        return response.content
```


這個版本可以跑。Demo 跑得很好。然後我讓它去執行一個稍微複雜的任務——多個工具、幾十輪迭代——它在第三十幾輪靜默掛掉了。沒有 error，沒有 log，只是停在那裡。後來我才意識到，問題不是 LLM 不夠強，而是 loop 本身沒有設計。


一個能真正運行的 Agentic System，不是讓 LLM 一直跑直到它想停。它需要對「什麼情況下繼續」、「什麼情況下停止」、「出錯之後怎麼辦」這些問題有明確的答案。這些答案，就是 loop 的工程。


**讀完這篇，你會理解：**


- Agent Loop 的基本模型是什麼，happy path 長什麼樣子

- 工具執行的並行/串行決策是怎麼做的

- 為什麼「出錯就 retry」是個壞主意，以及正確的錯誤分類策略

- Loop 的三個停止條件，各自代表什麼

- interrupt 和 steer 的語義差異，以及為什麼兩個都需要


這篇以 hermes-agent 的實作為例，但討論的問題是所有 Agentic System 都會碰到的。

---


## Agentic Loop 的基本模型是什麼？


Agent Loop 的核心模型叫做 ReAct（Reason + Act）。每一輪的節奏是：Think（把當前 context 送給 LLM，讓它決定下一步）→ Act（執行 LLM 選擇的工具）→ Observe（把工具結果放回 context，準備下一輪）。這個迴圈一直跑，直到 LLM 不再需要工具、直接給出最終回應為止。


hermes-agent 的 `run_conversation()` 主幹就是這個形狀。每一輪迭代做幾件事：組合這一輪要送給 LLM 的訊息（含 cache control markers）、呼叫 API、把回應 normalize 成統一格式、如果有 `tool_calls` 就執行、沒有就結束迴圈返回結果。


這是 happy path。真實系統麻煩的地方，是 happy path 以外的每一條路。
 ● Agent Loop 執行引擎    User Message 進入  ↓   
前置準備
sanitize · memory check · system prompt (cached from DB)   ↓   MAIN LOOP    
Build Messages
inject memory context · apply cache markers  ↓ 
API Call
streaming · inner retry (max 3)       error →  Has tool_calls?       No Yes      
Final Response
EXIT 1 — 正常完成 ✓     
Tool 分類
never / path / safe  ↓ 
Execute Tools
ThreadPool · max 8      Loop Checkpoints  interrupt_requested? → EXIT 2 中斷   ≥ max_iterations? → EXIT 3 摘要   else → ↑ 下一輪        Error Classifier  rate_limit cooldown + rotate key   ctx_overflow compress → retry   billing rotate key (no retry)   format_err no retry → fail    Tool 分類  NEVER 互動工具，強制串行   SAFE read-only，永遠並行   PATH 路徑不重疊才並行  未知工具 → 預設串行         

---


## 為什麼工具執行不能全部並行？


最直覺的工具執行方式是逐個串行跑，安全但慢。並行執行可以省時間，但不是所有工具都能並行——問題在於不同工具有不同的副作用和依賴關係，統一並行會造成競爭條件或邏輯錯誤。hermes-agent 把工具靜態分成三類，在 API call 之前就決定這個 batch 能不能並行。


分類範例工具並行策略原因NEVER parallel`clarify`強制串行需要等用戶回應，其他工具結果無意義PARALLEL SAFE`read_file`、`web_search`永遠可並行只讀、無狀態，無副作用PATH SCOPED`write_file`、`patch`路徑不重疊才並行避免同時寫入同一個檔案


決策演算法掃描整個 tool batch：遇到 NEVER 類立即降為串行；遇到 PATH 類記錄路徑，有重疊降為串行；不在任何白名單裡的未知工具也降為串行——保守但正確。最多 8 個 ThreadPoolExecutor worker 並行執行。


關鍵設計是**靜態分類**，不是在 runtime 試圖推斷工具能不能並行，而是提前明確定義好。這讓行為可預測，出問題也容易 debug。

---


## 為什麼不能直接 retry？API 錯誤的分類策略


直接 retry 在很多情況下會讓事情更糟。`rate_limit (429)` 需要等 cooldown 再試或換 key；`context_overflow` 需要先壓縮 context 再試；`billing (402)` 需要換 key 而且不應該 retry（額度耗盡，retry 沒用）；`format_error (400)` 是請求格式問題，retry 只會得到一樣的錯誤。每種錯誤的正確處理方式完全不同，先分類才能採取正確 action。


hermes-agent 的 `classify_api_error()` 函數回傳一個 `ClassifiedError` 物件，裡面有三個 flag：

```
ClassifiedError(
    reason=FailoverReason.rate_limit,
    retryable=True,
    should_compress=False,
    should_rotate_credential=True,
)
```


Loop 根據這三個 flag 決定下一步，而不是直接 retry。分類邏輯走七個優先順序：先看 provider 特定的錯誤模式，再看 HTTP status code，再看 error code，再看訊息內容，最後才是通用 fallback。


其中有一個具體細節值得說：**402 的消歧義**。402 Payment Required 可能是兩種情況：帳單額度耗盡（不可重試），或者暫時性的配額重置（可重試，幾分鐘後就好）。區分的方法是看 error message 裡有沒有「try again in N minutes」這類暫時性信號——有的話算 rate limit，沒有才是真正的 billing exhaustion。這種細節在 demo 裡看不出來，但在 24/7 跑著的系統裡，誤判會造成實際問題。

---


## Agentic Loop 的三個停止條件是什麼？


設計良好的 Agentic Loop 有三個明確的停止條件，各自代表不同的語義。只依賴其中一個，或把三件事混在一起，都會讓 loop 的行為變得不可預測。


**停止條件一：正常完成**。LLM 的回應裡沒有 `tool_calls`，表示它認為任務完成，直接給出了最終答案。這是 happy path 的出口。


**停止條件二：Budget 耗盡**。`api_call_count >= max_iterations`（hermes-agent 預設 90 輪）。到達邊界時，不是直接 return，而是讓 LLM 摘要「做了什麼、現在在哪裡、還有什麼沒做」，把這個摘要作為最終回應返回。這保證呼叫方永遠能得到有意義的回覆，而不是 timeout 或 exception。


**停止條件三：外部中斷**。`_interrupt_requested == True`。這是 loop 的緊急出口，由外部系統（用戶、gateway、監控）觸發，一旦設置，loop 在下一個安全點立即退出。


三個條件背後有不同的設計意圖：**完成是正常狀態，Budget 是保底，中斷是外部控制**。

---


## interrupt() 和 steer() 有什麼不同？


`interrupt()` 是立即停，`steer()` 是等這輪工具跑完後注入訊息——這兩個操作解決的是完全不同的需求，在 multi-agent 場景下尤其重要。


`interrupt()` 在主執行 thread 設置 `_interrupt_requested = True`，同時 fan-out 到所有 tool worker threads（有幾個並行工具就 signal 幾個 thread），還遞迴傳給所有子 agent。任何一個地方的 streaming API call 都會在下一個 chunk 偵測到 interrupt 並關閉連線。


`steer()` 把訊息附加到最近一個 tool result 的後面，格式像是 `[User note: ...]`。下一次 LLM 看到 context 時，會在 tool 執行結果旁邊看到這條訊息。工具不會被中斷，任務繼續，只是 LLM 在下一輪會有一個新的輸入。


interrupt()steer()何時生效立刻停止等這輪工具完成後機制fan-out signal 所有 thread注入 `[User note: ...]`子 agent遞迴傳遞 interrupt不影響子 agent適合場景任務取消、緊急中止修正方向、補充資訊


在單一 agent 場景下這個差異可能不明顯。但在一個父 agent 管理多個子 agent 的場景下，interrupt 是「取消整個任務」，steer 是「修正方向但不打斷執行」——兩個都需要。

---


## 這些設計決策的共同邏輯


回頭看這些決策，它們背後有一個共同的邏輯：**Loop 的每個出口都是有意為之的，不是讓它跑到出錯為止。**


並行/串行分類讓工具執行的行為可預測。錯誤分類讓每種失敗有對應的處理策略。三個停止條件讓 loop 在任何情況下都有一個定義好的出口。interrupt 和 steer 讓外部系統有辦法控制一個正在執行的 agent。


這些問題在 demo 階段幾乎不會出現——幾輪對話、單一工具、理想輸入，什麼都跑得很好。它們會在系統長期運行、工具複雜、環境不穩定的時候浮現。


一個真正可以在生產環境跑的 Agentic System，它的 loop 必須對所有這些問題有答案，而不只是「跑起來能用」。

---


## 延伸閱讀


- [Harness Engineering 的地基：LLM Session 設計框架](/blog/llm-session-harness) — Session 管理的四種策略與三種中斷狀態，loop 的狀態持久化基礎

- [hermes-agent：從原始碼看一個為 Production 設計的 Agent 系統](/blog/hermes-agent-production-agent) — hermes-agent 的整體 Harness 設計：memory fencing、context compression、skill 系統
     [ Harness Engineering ](/blog?tag=Harness%20Engineering)  
### 
相關文章

[System DesignAgent 要怎麼進化？六個系統的 Self-Improvement 機制比較2026-05-22](/blog/agent-self-improvement-design-comparison)[System DesignSOUL 設計決定了 Agent 是什麼：六個 Agentic System 的 system prompt 比較2026-05-22](/blog/agent-soul-design-comparison)[Viewpoint你在比的是模型，但決定 Claude Code 效果的是 Harness2026-05-20](/blog/claude-code-harness-over-model)

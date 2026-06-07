---
url: "https://warmwater.dev/blog/llm-session-harness"
title: "Harness Engineering 的地基：LLM Session 設計框架"
date: 2026-05-05
category: Harness Engineering
source: warmwater.dev
---

[
← Harness Engineering ](/blog?tag=Harness%20Engineering)  Harness Engineering  
#  Harness Engineering 的地基：LLM Session 設計框架 
  2026-05-05 · — views      

你設計了一個 Agent 去執行一個複雜的多步驟任務。跑到一半，process 重啟了。


這個 Agent 從哪裡繼續？


這不是一個邊緣案例——它是所有長時間運作的 Agentic System 都會碰到的問題。而答案，取決於你在設計 session 的時候做了什麼選擇。


這是一個 **Harness Engineering** 的問題。Harness 管的是「讓模型能在真實世界安全行動的那套基礎設施」，session 設計是其中最底層的一塊。當 Agent 從「輸出文字」變成「長時間執行任務」，session 不再只是對話介面的細節，而是整個系統能不能存活的基礎條件。

---


## 一個事實：LLM API 永遠是 Stateless 的


在討論怎麼設計之前，先確認一個常被忽略的事實：**LLM 模型本身不持有任何 session 狀態。**


OpenAI API、Claude API，每一個 request 都是完全獨立的。模型不知道你上次問了什麼，也不知道你是誰。你以為 Agent 在「持續運作」，其實每次呼叫 API，都是一個全新的對話。


「連續性」是幻覺。維持這個幻覺的，完全是呼叫方。


這個事實帶來一個根本的設計分野：你要讓呼叫方每次帶入完整 context，還是在 API 之上建一層持久化的狀態管理？
 ● Stateless vs Durable — Request Flow    STATELESS   Request 1  新問題   ↓ LLM API ↓ Server 不存任何狀態 ↓  Request 2（需帶完整歷史）  Turn 1 Turn 2 新問題   ↓ LLM API ↓ Server 不存任何狀態     DURABLE   Request 1  新問題 thread_id   ↓ Session Layer（DB / Store） ↓ 注入歷史 ↓ LLM API ↓ 儲存結果  Request 2（只帶新訊息）  新問題 thread_id   ↓ Session Layer 從 DB 讀出歷史 ↓ 注入歷史 ↓ LLM API      呼叫方負責帶入完整 context Server 無狀態，可水平擴展 中斷 = context 遺失   呼叫方只帶 thread_id + 新訊息 Session Layer 負責注入歷史 中斷後可從 checkpoint 繼續   


兩種模式的取捨很直接：Stateless 實作簡單、server 無狀態、可水平擴展，代價是中斷即失憶；Durable 可以恢復中斷，代價是需要儲存基礎設施和狀態管理邏輯。


短對話、API 服務、單次問答——Stateless 完全夠。但當任務的生命週期從「幾秒」變成「幾小時」，Durable 才是唯一選項。

---


## Durable Session 的四種實作策略，怎麼選？


「Durable session」不是一個方案，而是一個需求——怎麼實作有四種主要路徑，核心問題是：**這個任務能接受中斷後從頭來嗎？**

### 1. Full Context Replay


每次 request 都把完整對話歷史塞進去。

```
[System Prompt][Turn 1][Turn 2]...[Turn N][新問題]
```


實作最簡單，正確性完美。缺點是 context window 有上限，超長任務直接打爆。**適合對話輪數少、context 不超過 8K tokens 的場景。**

### 2. Client-side Context Management


保留最近 N 輪，超出時截斷舊的或壓縮成摘要。

```
def build_context(history, max_tokens=8000):
    result = [system_prompt]
    for turn in reversed(history):
        if token_count(result) + token_count(turn) > max_tokens:
            break
        result.insert(1, turn)
    return result
```


可以跑無限長的對話，成本可控。代價是截斷可能丟失早期重要資訊。**適合一般對話場景，對中斷點精確性要求不高。**

### 3. Checkpoint（LangGraph 模式）


對話和 Agent 的**完整狀態**持久化到 DB，用 `thread_id` 識別 session。中斷後用同一個 `thread_id` 繼續，LangGraph 從 DB 載入上次的 checkpoint，從中斷的節點重新執行。

```
config = {"configurable": {"thread_id": "task-session-42"}}
# 中斷重啟後，用同一個 thread_id 繼續
result = graph.invoke({"messages": [new_message]}, config)
```


支援精確的中斷點恢復，甚至可以 time-travel debug。代價是 DB 儲存和讀取有額外延遲，checkpoint 可能很大。**適合 Multi-step Agent、需要 Human-in-the-Loop 的工作流。**

### 4. Compaction（Claude Code 模式）


不存完整 checkpoint，而是在 context 快滿時**動態壓縮成摘要**，讓 session 繼續運行：

```
[Turn 1][Turn 2]...[Turn 50] → 接近 context limit
↓ Compaction 觸發
[結構化摘要][Turn 48][Turn 49][Turn 50] → context 空間釋放
```


context 永遠不會打爆，連續性損失最小。代價是摘要生成有額外費用，丟失的細節不可逆。**適合需要跑幾個小時的長時間任務，對精確恢復要求不高。**


策略狀態存在哪中斷恢復Context 上限複雜度Full ReplayClient memory從 DB 全讀有（超出即失敗）低Client-side ManagementClient + DB截斷後 replay可控中Checkpoint（LangGraph）DB（完整狀態）精確恢復到中斷點無（每輪存）高Compaction（Claude Code）摘要檔案注入摘要繼續無（動態壓縮）高

---


## 長時間 Agentic System 的中斷問題


四種策略解決的是「context 要怎麼維持」，但生產環境還有另一層問題：**一個跑幾個小時的 Agent，如何在各種中斷情境下存活？**


這需要一個顯式的中斷狀態機。

### 兩層識別：Session Key vs Session ID


設計中斷恢復邏輯之前，要先分清楚兩個概念：


**Session Key** 是穩定的用戶地址，從平台和用戶 ID deterministic 生成，重啟後不變。它代表「這個用戶是誰」。


**Session ID** 是這一輪任務執行的票號，每次 session 重置都會產生新的。它代表「這次對話的 transcript 在哪裡」。

```
Session Key  → agent:main:telegram:dm:user_id_123   (永遠不變)
Session ID   → 20260505_143022_a1b2c3d4              (每次重置都不同)
```


把這兩層分開，才能做出一個關鍵的判斷：**保留用戶身份，但決定這次任務要繼續還是重來。**

### 三種中斷狀態


長時間運作的 Agentic System，Agent session 的中斷只有三種情況：
 ● Agent Session 三種中斷狀態   
Active Session
Agent 正在執行任務                    空閒超時 ↓ 
Auto Reset
 ↓ 
New session_id
舊 context 清空     Gateway 重啟 ↓ 
Resume Pending
 ↓ 
Same session_id ✓
從中斷點無縫繼續     卡死 / /stop ↓ 
Suspended
 ↓ 
New session_id
強制 clean slate     
優先級：
Suspended › Resume Pending › Auto Reset — Suspended 是硬重置信號，優先級最高  


**Auto Reset（空閒超時）**：用戶長時間沒有互動，系統主動重置。這是有意為之的清空，下次訊息建立新的 session_id，不需要恢復舊 context。


**Resume Pending（系統重啟）**：Gateway 崩潰或收到 SIGTERM 時，在關閉前標記 `resume_pending = True` 並持久化。下次訊息到達時，發現這個標記，保留原來的 session_id，Agent 從中斷點無縫繼續，用戶感覺不到任何中斷。


**Suspended（卡死 / 人工介入）**：Agent 重複失敗超過閾值，或用戶手動執行 `/stop`。標記 `suspended = True`。下次訊息強制建立新的 session_id，帶著乾淨的 context 重新開始。`suspended` 是硬重置信號，優先級比 `resume_pending` 更高。


三種狀態的設計邏輯是：**系統崩潰是意外，應該自動恢復；任務卡死是設計失敗，應該乾淨重來。**

---


## 選哪個：四條判斷邏輯


```
對話輪數少，context < 8K？
    → Full Replay

一般對話，成本優先，可以接受截斷？
    → Client-side Context Management

Agent 多步驟任務，需要精確從中斷點恢復？
    → Checkpoint（LangGraph）

長時間 session，context 不能打爆，不需要精確恢復？
    → Compaction（Claude Code 模式）
```


四個策略不是非此即彼，實際系統往往是組合的：用 Checkpoint 存 Agent 的任務狀態，用 Compaction 管對話的 context，用 Client-side Management 處理輕量的輔助對話。

---


## Session 設計是 Agent 能不能存活的前提


Session 設計很容易被當成實作細節，在系統設計早期被跳過。但當你的 Agent 從「跑幾秒」變成「跑幾個小時」，這些細節就變成了系統存活的前提。


Harness Engineering 的核心問題之一是：讓模型能在真實世界安全、可預測地行動。Session 設計是這個問題最底層的答案——不是模型夠不夠強，而是你有沒有在 API 和模型之間，建起一層讓任務能夠持久、能夠中斷恢復、能夠在失敗後乾淨重來的基礎設施。

---


## 延伸閱讀


- [用 n8n 把 AI 嵌進工作流程：兩種節點，一個關鍵判斷](/blog/n8n-agentic-workflow) — workflow 引擎與 Agent 推理的組合設計，確定性節點 vs 推理節點的邊界

- [Plan Mode 之後：你的 AI Agent 還缺什麼](/blog/superpowers-plan-mode-ai-agent) — AI coding agent 四個系統性失敗模式，以及行為約束系統的設計模式

- [hermes-agent：從原始碼看一個為 Production 設計的 Agent 系統](/blog/hermes-agent-production-agent) — Session 設計的真實應用：hermes 的 Context 壓縮和 parent_session_id 追蹤，是 Durable Session 的具體實作
     [ Harness Engineering ](/blog?tag=Harness%20Engineering)  
### 
相關文章

[System DesignAgent 要怎麼進化？六個系統的 Self-Improvement 機制比較2026-05-22](/blog/agent-self-improvement-design-comparison)[System DesignSOUL 設計決定了 Agent 是什麼：六個 Agentic System 的 system prompt 比較2026-05-22](/blog/agent-soul-design-comparison)[Viewpoint你在比的是模型，但決定 Claude Code 效果的是 Harness2026-05-20](/blog/claude-code-harness-over-model)

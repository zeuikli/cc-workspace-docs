---
url: "https://warmwater.dev/blog/n8n-agentic-workflow"
title: "在 n8n 裡嵌入 AI：Agentic Workflow 設計"
date: 2026-05-04
category: Agentic System
source: warmwater.dev
---

[
← Agentic System ](/blog?tag=Agentic%20System)  Agentic System  
#  用 n8n 把 AI 嵌進工作流程：兩種節點，一個關鍵判斷 
  2026-05-04 · — views      

n8n 是不是快死了？這個問題最近一直在社群裡出現。有人說 Zapier 要取代它、有人說 AI 根本不需要 workflow 引擎、也有人說整個 no-code 工具都要被 LLM 取代。


我不覺得這個問題問對了。


更值得想的問題是：**在一條 workflow 裡，哪些步驟該用 AI，哪些不該用？** 搞清楚這個，才是把 n8n 用好的關鍵——也是它還活著的理由。

---


## n8n 是什麼？為什麼它不是 AI 框架


n8n 是一個 workflow 自動化引擎，本質上是一個 DAG（有向無環圖）執行器。你拖拉幾個節點、連上觸發器，它就按照你定義的順序跑。


它支援大概 400+ 種整合，從 Slack、Notion、Google Sheets 到 HTTP Request 都有。自己架的話是免費的（fair-code license）。付費版多了 cloud hosting 和 team 功能，但核心邏輯沒有差別。


**n8n 不是 AI 框架**。它沒有像 LangChain 那樣的 Chain 概念，也不處理 prompt engineering。它只是讓你把各種工具串在一起，按照你定義的邏輯執行。

---


## Workflow 裡的兩種節點


n8n 支援 ~70 個 LangChain 相關的節點，可以直接在 workflow 裡插入 AI 呼叫。但這不代表每個步驟都應該用 AI。


一條設計得好的 workflow，節點通常分成兩種：


**確定性節點（n8n native）**


- API 呼叫、DB 查詢

- 資料格式轉換、過濾

- 依規則路由（Switch node）

- 寫 DB、發通知


這些步驟的輸出是可預測的。給定相同輸入，輸出永遠相同。用 n8n 原生節點處理，快、便宜、不會出幺蛾子。


**推理節點（Agent）**


- 分類：這封信是 bug 回報還是功能請求？

- 判斷：這個異常是已知問題還是新問題？

- 轉換：把非結構化文字變成結構化 JSON


這些步驟需要語意理解或情境判斷，才需要 LLM。


節點類型典型操作特性確定性節點（n8n native）API 呼叫、DB 查詢、格式轉換、條件路由輸出可預測；成本低；容易 debug推理節點（Agent）分類、語意判斷、非結構化轉 JSON需要語意理解；輸出不確定；成本高
 ● Workflow 的兩種節點  大部分節點是確定性的，Agent 只在需要推理的地方介入  TriggerWebhook / Cron / 事件 ↓ 資料擷取API 呼叫、DB Query ↓ ✦ Agent 節點推理、分類、判斷 — 只在這裡 ↓ 資料轉換 + 執行動作格式化、寫 DB、發通知   起點 n8n 確定性 Agent 推理   


**原則很簡單：只在你真的需要推理的地方用 Agent。** 其他地方用確定性邏輯，成本低、結果穩定、容易 debug。

---


## 實際案例：SRE 監控 + Agentic Close Loop


說完概念，來看一個我覺得比較有意思的組合方式。


場景：SRE 想要做定期的系統健康監控。每小時跑一次，抓指標、偵測異常、自動處理或通報。


最直覺的做法是把所有判斷都丟給 AI。但這樣有幾個問題：每次都要打 LLM API，成本高；回應時間不穩定；已知問題的處理流程也會走到 AI，沒有必要。


比較好的設計是這樣：


- **n8n 節點做確定性部分**：定時抓指標、算閾值、偵測有沒有異常

- **Cheap Agent 做 triage**：用輕量模型快速判斷「這是已知問題還是未知問題」

- **分支**：已知問題走標準 Runbook，自動修復；未知問題才啟動深度調查


第三步的深度調查就是所謂的 **Agentic Close Loop**：一個 Agent 反覆執行「調查 → 假設 → 驗證」的循環，直到找到根因（RCA）或確認無法自動解決才停下來。
 ● SRE 監控 + Agentic Close Loop  Cheap agent 做 triage，未知問題才啟動 Close Loop 深度調查  Cron Trigger每小時定時執行 ↓ 抓系統指標Error rate、P99 Latency、Uptime ↓ 偵測異常Error rate > 閾值 / P99 > SLA ↓ ✦ Cheap Agent：初步 Triage輕量模型（快、便宜）output: { known, severity, type } ↓  ✓ 已知問題 ? 未知問題   
標準 Workflow
執行 Runbook
自動修復 / 建 ticket   Agentic Close Loop  1  調查 撈 logs、trace、metrics    2  假設 推斷可能根因    3  驗證 執行測試 / 重現嘗試    ↺ 未確認 → 換假設重試   ✓  RCA 完成 輸出根因 + 建議修復     ↓ Incident ReportPagerDuty + Slack + Ticket   


這個設計的核心思路是：**把 Agent 推理的成本集中花在真正需要的地方**。絕大多數的異常都是已知問題，Cheap Agent 快速分流之後，Deep Agent 只需要處理少數真正棘手的情況。

---


## 在生產環境值得注意的四個組合原則


從這個模式延伸，有幾個在生產環境值得注意的原則：


**1. Agent 節點的 output 要結構化**


Agent 節點應該輸出明確的 JSON，而不是自然語言。比如 `{ "known": true, "severity": "high", "type": "oom" }`，後面的 n8n 節點才能確定性地根據這個結果做路由。如果 output 是自然語言，後面每個節點都要再用 AI 解析，成本線性增加。


**2. Cheap Agent 先跑，Deep Agent 後跑**


不是所有 Agent 都要用最強的模型。分類、triage 這種任務，輕量模型（Haiku、GPT-4o mini）就夠了，速度快、成本低。只有在真的需要複雜推理的地方才動用重量級模型。


**3. Close Loop 要有終止條件**


Agentic Close Loop 的「調查 → 假設 → 驗證」循環需要明確的終止條件：找到根因、超過最大迭代次數、或者判斷超出自動化能力範圍。沒有終止條件的 Loop 會一直跑，成本無限增加，最後通報也延誤了。


**4. n8n 確定性節點負責 side effect**


寫 DB、發 Slack、建 ticket 這些有副作用的操作，應該交給 n8n 確定性節點，而不是讓 Agent 直接呼叫。一方面是控制成本，另一方面是讓這些操作有明確的 audit trail，出問題的時候容易追。

---


## 流程說清楚，才是把工具用好的開始


如果你現在已經有一堆跑著的工作流程（不管是 n8n、Zapier、還是自己寫的 cron job），大部分都是確定性的。


這本身不是問題。確定性流程可靠、可預測、容易維護。


但如果其中有一些步驟需要人工判斷、因為太難自動化而被跳過，或者長期靠人力分流——那些地方，才是值得考慮嵌入 Agent 推理的節點。


n8n 的價值不在於「用 AI 取代所有流程」，而在於讓你**精確地控制哪些地方用 AI，哪些地方不用**。把這個判斷做對，才是把工具用好的開始。


還有一件事值得說。工程師寫的自動化，通常只有工程師能審查——程式碼是黑箱，跑完輸出一個結果，其他人只能相信它。但一條 n8n workflow，PM 可以讀、營運可以讀，甚至可以一起討論某個節點的判斷邏輯對不對。不是說非工程師可以自己建複雜的 AI workflow，而是說這條流水線**第一次有了跨角色的可讀性**。


這或許才是 n8n 沒死的真正原因：不只是功能夠用，而是它把自動化邏輯變成了一種組織裡可以共同討論的語言。


但在這一切之前，有一個更前置的問題值得誠實面對：你夠不夠清楚自己的流程本身？


最近看到 Daniel Miessler 的一個觀點：大多數公司沒辦法從 AI 獲益，不是因為 AI 不夠強，而是因為說不清楚自己要 AI 幫什麼。你無法優化你不理解的東西。


這和把 workflow 拆成兩種節點的概念直接呼應。在 n8n 的 canvas 上定義哪些步驟是確定性的、哪些需要 Agent，本身就是一個強迫釐清的過程。你沒辦法迴避「這個步驟的規則是什麼」這個問題。建 workflow 的過程，往往也是讓組織第一次說清楚自己流程的過程。


AI 放大的是你原本就有的東西。流程清楚，它讓你跑得更快；流程混亂，它只是讓你更有效率地混亂。n8n 不會自動幫你理清，但它的視覺化邏輯，至少給了你一個把流程說清楚的地方。

---


## 延伸閱讀


- [Harness Engineering 的地基：LLM Session 設計框架](/blog/llm-session-harness) — Agent 長時間執行時，session 如何設計才能在中斷後存活

- [Plan Mode 之後：你的 AI Agent 還缺什麼](/blog/superpowers-plan-mode-ai-agent) — AI coding agent 四個系統性失敗模式的結構分析

- [Harness Engineering：LLM 應用的基礎建設層](/blog/harness-engineering-ai) — n8n 是 workflow orchestrator，這篇講的是更底層的問題：LLM 和應用之間那層基礎設施怎麼設計
     [ Agentic System ](/blog?tag=Agentic%20System)  
### 
相關文章

[System DesignAgent 要怎麼進化？六個系統的 Self-Improvement 機制比較2026-05-22](/blog/agent-self-improvement-design-comparison)[System DesignSOUL 設計決定了 Agent 是什麼：六個 Agentic System 的 system prompt 比較2026-05-22](/blog/agent-soul-design-comparison)[LLMOpsLoRA 這件事你只需要搞清楚一次2026-05-20](/blog/lora-map)

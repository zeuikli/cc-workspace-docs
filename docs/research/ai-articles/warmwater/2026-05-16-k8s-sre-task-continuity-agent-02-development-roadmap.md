---
url: "https://warmwater.dev/blog/k8s-sre-task-continuity-agent-02-development-roadmap"
title: "K8s SRE Task Continuity Agent（二）：開發 Roadmap 與分工設計"
date: 2026-05-16
category: System Design
source: warmwater.dev
---

[
← System Design ](/blog?tag=System%20Design)  System Design 
 
# K8s SRE Task Continuity Agent（二）：開發 Roadmap 與分工設計
 
 2026-05-16 · — views  
  
  
架構設計完成之後，最常見的問題是：從哪裡開始建？


三層 plugin 架構（Session、Memory、Knowledge）如果同時開發，你會面對一個問題：每一層都依賴其他層的行為才能驗收。Session 沒有穩定之前，你不知道 Memory 的 write trigger 對不對；Memory 沒有穩定之前，你不知道 Knowledge 的 retrieval 有沒有被正確用到。三層同時動，等於三個方向同時出問題，而且你不知道問題在哪一層。


這篇是三篇系列的第二篇，聚焦開發 Roadmap：怎麼把架構拆成三個可獨立驗收的 Phase，以及兩個人怎麼分工讓每個 Phase 都能並行。


---


## 為什麼要 Interface-First？


Interface-first 是讓兩個人可以並行開發的前提條件。在任何一行實作程式碼之前，先把三個核心介面定義清楚，兩人就可以各自針對介面開發，不需要等對方。


三個需要在 Phase 1 第一週對齊的介面：


```
ContextPlugin interface
├── onContextAssembly(query, sessionState) → ContextSnippet[]
└── onSessionEnd(sessionState, transcript) → void

Tool interface
├── name, description, inputSchema
└── execute(input) → ToolResult

K8sClient interface
├── describeResource(kind, name, namespace) → string
├── getLogs(pod, namespace, previous?) → string
├── getEvents(namespace, filter?) → Event[]
└── queryMetrics(query, timeRange) → MetricResult
```


Person A 針對 ContextPlugin 介面開發 Loop Core 和 Session Plugin，用 mock K8s Client 跑完整流程。Person B 實作真正的 K8s Client 和 Tool Registry，用單元測試驗收每個 tool 的輸出格式。兩人在整個 Phase 1 期間不需要等對方，只需要在介面定義上對齊一次。


介面是兩人的合約，不是部門的邊界。合約定好，各自交付。


---


## Phase 1 要做什麼？Scope 邊界在哪裡？


Phase 1 的目標只有一個：agent 能完成一個 K8s 故障調查任務，context compaction 不會讓任務中斷。沒有跨 session 記憶，沒有 runbook，沒有三個 plugin 的 budget 競爭——這些全部是後面 Phase 的事。


```
In scope:
  ✓ Agentic Loop Core
  ✓ Context Assembler（只有 Session Plugin）
  ✓ Session Plugin（task state 讀寫 + compaction checkpoint）
  ✓ Tool Registry + 四個基本 K8s tools
  ✓ K8s Client（kubectl 基本操作）

Out of scope:
  ✗ Memory Plugin
  ✗ Knowledge Plugin
  ✗ Token budget 仲裁（只有 Session，不需要競爭）
  ✗ Metrics 查詢（先做 logs 和 events）
```


**四個基本 K8s tools：**


| Tool | 對應操作 | 輸出 |
| --- | --- | --- |
| kubectl-describe | describe pod/deployment | pod spec + status |
| kubectl-logs | logs（含 —previous） | container log text |
| kubectl-events | get events —field-selector | event list |
| kubectl-get | get pods/deployments | resource list |


**Done criteria：**


- Agent 能從「OOMKilled」問題出發，跑完 describe → logs → 得出結論的完整路徑
- 模擬 context compaction，agent 能從 Session Plugin 的 checkpoint 繼續，不從頭
- Session Plugin 的 read/write 在 compaction 前後都正確


Phase 1 做完之後，你有一個能獨立完成調查任務的 agent。它不記得上次，它沒有 runbook，但它不會因為 context 滿了就忘記自己在做什麼。


---


## Phase 2 怎麼加上跨 Session 學習？


Phase 2 的核心設計問題是：什麼 K8s 事件值得記？Pod status 五分鐘後就過期，寫了反而有害；但「api-server OOMKilled 的 root cause 通常是 memory limit 設太低」這個 pattern，對未來的調查有實際價值。Write trigger 的答案是：agent 得出 root cause 結論的當下觸發，中途的 tool outputs 不存。


```
In scope:
  ✓ Memory Plugin（write / search / lifecycle）
  ✓ Context Assembler 擴充（Session + Memory token budget）
  ✓ Write trigger 設計（root cause 結論觸發）
  ✓ Memory storage 選型（對應資料形式的搜尋需求）

Out of scope:
  ✗ Knowledge Plugin
  ✗ Memory → Knowledge promotion
  ✗ 複雜 lifecycle（先用 TTL，不做 Ebbinghaus 衰減）
```


**Done criteria：**


- 第一次調查 OOMKilled 後，pattern 有被寫進 memory
- 第二次調查同類問題，Context Assembly 有拿到上次的 pattern
- Session + Memory 共存，token budget 不超限
- Phase 1 的所有 test case 繼續通過


Phase 2 結束後，agent 有「經驗」。它記得上次類似的問題怎麼解，調查路徑因此縮短。


---


## Phase 3 怎麼加上結構化知識？


Phase 3 讓 agent 有 K8s 結構化知識作為背景，調查時不需要每次從 kubectl 輸出推斷 cluster 基本結構。Knowledge Plugin 和 Memory Plugin 的根本差異在於：Knowledge 是人工維護的，agent 不自己寫入。Runbook 是 SRE team 寫的，cluster topology 從 infra 文件匯入，不是 agent 從對話中學到的。


```
In scope:
  ✓ Knowledge Plugin（RAG retrieval）
  ✓ Runbook ingestion pipeline（把 SRE runbook 變成可搜尋的格式）
  ✓ Cluster topology snapshot（定期更新，不即時同步）
  ✓ Context Assembler 完整 token budget 仲裁（三個 plugin 競爭）

Out of scope:
  ✗ Knowledge 自動更新（人工維護）
  ✗ Memory → Knowledge promotion 自動化
```


**Done criteria：**


- OOMKilled 調查時，相關 runbook 內容有出現在 context
- 三個 plugin 共存，沒有任何一個被完全擠出 context
- Phase 1 + Phase 2 的所有 test case 繼續通過


---


## 兩人怎麼分工才能不互相阻塞？


垂直切割（按關注點分）比水平切割（按 layer 分）更適合這個架構。水平切割讓兩人在 Phase 2 和 Phase 3 出現依賴；垂直切割讓 Person A 從 Phase 1 到 Phase 3 都專注「思考腦」，Person B 專注「執行手」，介面對齊之後兩條線互不阻塞。

 
 
 Person A
 
思考腦
  
 Person B
 
執行手
 
  Phase 1 Session 
 
 Agentic Loop Core
 
Context Assembler
 
Session Plugin
  
 K8s Client
 
Tool Registry
 
4 個基本 K8s tools
 
 ↑ interface 對齊點：ContextPlugin / Tool / K8sClient ↑ 
 
  Phase 2 Memory 
 
 Memory Plugin
 
Write trigger 邏輯
 
Token budget 仲裁擴充
  
 Memory Storage backend
 
Search index + lifecycle
 
Memory query optimization
 
  Phase 3 Knowledge 
 
 Knowledge Plugin
 
Context retrieval 邏輯
  
 RAG infrastructure
 
Runbook ingestion pipeline
 
Cluster topology pipeline
 

**Person A：思考腦**


負責所有跟 LLM 互動相關的邏輯：Agentic Loop Core、Context Assembler、三個 Plugin 的讀寫邏輯。驗收方式是跑 agent 的端到端行為，看輸出對不對。用 mock K8s Client 開發，不需要等 Person B 的實作就緒。


**Person B：執行手**


負責所有跟外部系統互動的邏輯：K8s Client、Tool Registry、Memory Storage backend、RAG infrastructure。驗收方式是單元測試每個 tool 和 storage 的輸入輸出格式。只要介面定義清楚，Person B 可以在 Phase 1 第一天就開始。


---


## 每個 Phase 的 Scope 邊界怎麼定？


每個 Phase 的「刻意不做」和「done criteria」同樣重要。「刻意不做」不是未來的 backlog，是當下的防線——在 code review 的時候有依據：這個功能不在這個 Phase 的 scope 裡，不要合進來。


| Phase | Done 條件 | 刻意不做 |
| --- | --- | --- |
| Phase 1 | 調查任務完成 / Compaction resume 正確 / Tool 輸出格式穩定 | 沒有跨 session 記憶 → 正確，那是 Phase 2 |
| Phase 2 | Memory 在 Context Assembly 出現 / Write trigger 正確 / Token budget 不超限 | Memory lifecycle 只用 TTL → 正確，複雜衰減是 nice-to-have |
| Phase 3 | 三個 Plugin 共存 / Budget 仲裁正確 / Knowledge retrieval 相關 | Knowledge 自動更新 → 正確，人工維護就夠 |


---


## 三個 Phase 結束之後，系統長什麼樣子？


Phase 1 完成：agent 能獨立跑完一個 K8s 故障調查，context compaction 不中斷任務。Phase 2 完成：agent 有跨 session 的 incident memory，第二次遇到同類問題調查路徑縮短。Phase 3 完成：agent 有 K8s runbook 和 cluster topology 作為背景知識，調查不需要從 kubectl 輸出重新推斷已知結構。


三個 Phase 加在一起，是一個完整的 Task Continuity Agent——知道自己在做什麼，記得過去做過什麼，有背景知識可以參考。


系列的第三篇會討論 Testing 和 Observability：怎麼用 Minikube 建本機測試環境，以及每個 Phase 對應的 regression test 和 monitoring 指標設計。
 
 [ System Design ](/blog?tag=System%20Design)[ Agentic System ](/blog?tag=Agentic%20System) 
 

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

---
url: "https://warmwater.dev/blog/k8s-sre-task-continuity-agent-01-system-architecture"
title: "K8s SRE Task Continuity Agent（一）：系統架構設計"
date: 2026-05-16
category: System Design
source: warmwater.dev
---

[
← System Design ](/blog?tag=System%20Design)  System Design 
 
# K8s SRE Task Continuity Agent（一）：系統架構設計
 
 2026-05-16 · — views  
  
  
一個 K8s SRE Agent 收到「api-server OOMKilled，幫我看一下」這句話，要做的事情遠比表面複雜：查 pod description、拉 previous logs、看記憶體用量趨勢、比對過去有沒有類似 pattern——整個調查過程可能跨越幾十次 tool call，足夠讓 context window 觸發 compaction。Context compaction 發生的時候，如果 agent 沒有設計好，它會在調查進行到一半時「忘記」自己在做什麼。這不是模型的問題，是架構的問題。


這篇是三篇系列的第一篇，聚焦系統架構設計：K8s SRE 任務為什麼天然是 task continuity 的挑戰，以及怎麼用 Session / Memory / Knowledge 三層 plugin 架構來解決它。


---


## K8s SRE 任務為什麼會打斷 agent？


K8s SRE 任務打斷 agent 的根本原因是：調查任務天然跨 session，但資訊的時效性差距極大，用同一個機制處理所有資訊是架構錯誤。


**調查任務天然跨 session**


一個 OOMKilled 的完整調查路徑可能是：確認 pod 狀態 → 拉 previous logs → 查 resource limits → 看記憶體趨勢 → 比對過去類似事件 → 判斷 root cause → 提出解法。每一步都需要前一步的結果，整個過程可能超過 context window 的承載量。Context compaction 是預期事件，不是邊緣情況。


**資訊的時效性差距極大**


K8s 環境裡的資訊，新鮮度差了好幾個數量級：


| 類型 | 範例 | 時效 |
| --- | --- | --- |
| 瞬間過期 | pod status、logs output | 幾分鐘 |
| 緩慢變化 | cluster topology、YAML manifest | 幾天 |
| 永久有效 | error patterns、操作手法 | 幾個月 |


存了 pod status 等於在喂過時資訊；不存 error pattern 等於每次重新學習。架構必須讓三條資訊路徑可以獨立設計。


---


## Session、Memory、Knowledge 的邊界在哪裡？


Session、Memory、Knowledge 的邊界由「資訊的來源」決定，不是由「內容是什麼」決定。同一個事實，放法不同就是不同的東西。


**Session** 是執行的邊界，不是知識的分類。Context window 裡存在的所有東西——對話歷史、tool outputs、working state——都屬於 session。Session 結束，這些東西消失。


**Memory** 是 agent 從互動中派生出來的東西。「上次這個 error pattern 是 memory limit 不足」是 memory，因為它是 agent 從實際調查過程中學到的，在第一次對話之前不存在。


**Knowledge** 是開發者設計進去的東西。K8s runbook、cluster topology 文件、操作 SOP——這些在第一次對話之前就存在了，不應該隨著 agent 的對話改變。


這個區分帶出三條設計路徑：Memory 應該有 lifecycle，Knowledge 應該有 curation pipeline，Session 應該有 continuity 機制。混淆這三條路徑，是後來大多數 agent 行為 bug 的根源。


---


## Agentic Loop 的兩個 Plugin 點在哪裡？


Task continuity agent 的架構核心是在 Agentic Loop 的兩個位置插入 plugin 點：LLM call 之前的 Context Assembly（讀），以及調查結束後的 Post-session（寫）。

 User Input 「api-server OOMKilled，幫我看一下」 
 
↓
 
 Plugin Point A
 
Context Assembly
 
  protected
Session Plugin

 
 variable
Memory Plugin

 
 variable
Knowledge Plugin

 
↓
 
 LLM Call 
 
↓
 
 Tool Execution Loop  kubectl logs metrics events 
 loop until LLM stops calling tools  
↓
 
 Plugin Point B
 
Post-session
 
  save checkpoint
Session Plugin

 
 write if triggered
Memory Plugin

 
 no-op
Knowledge Plugin

 
↓
 
 Response 
  

**Plugin Point A：Context Assembly（LLM call 之前）**


每個 plugin 在 LLM 收到 prompt 之前，把自己的資訊貢獻到 context 裡：


- Session Plugin 載入當前任務狀態：「上次查到 memory limit 95%，root cause 未確認」
- Memory Plugin 搜尋相關的過去 pattern：「過去 3 次 OOMKilled 都是 memory limit 設太低」
- Knowledge Plugin 檢索相關 runbook：「OOMKilled 排查步驟：check resource limits → memory trend → leak check」


**Plugin Point B：Post-session（調查結束後）**


每個 plugin 決定要不要把這次 session 的東西持久化：


- Session Plugin 存 checkpoint：「OOMKilled confirmed，limit 512Mi < usage 1.8Gi」
- Memory Plugin 觸發寫入：「api-server OOMKilled pattern：memory limit 不足，建議 2Gi」
- Knowledge Plugin 通常 no-op：knowledge 由人工維護，agent 不自己寫


這個設計讓 Agentic Loop Core 完全不需要知道 Session / Memory / Knowledge 的細節——只管呼叫 plugin，不管 plugin 裡面是什麼。


---


## 三個 Plugin 怎麼共享有限的 Context Window？


三個 plugin 同時注入 context 時，Session Plugin 應該有最高保護優先權，Memory 和 Knowledge 在 budget 不足時按 priority 裁切，不是隨機刪。


```
Total Context Budget
├── System Prompt → fixed
├── Session Plugin → protected（被擠掉等於任務中斷）
├── Tool Definitions → fixed
├── Memory Plugin → up to N tokens，可壓縮
├── Knowledge Plugin → up to M tokens，可壓縮
└── Conversation History → 剩餘
```


Session Plugin 享有保護預算的原因：task state 被擠出 context，等於 agent 忘了自己在做什麼，比沒有 memory 更嚴重。Memory 和 Knowledge 在資源不足時可以降級——context 裡少了一個過去 pattern 或少了一段 runbook，調查仍然可以進行；少了任務狀態，調查直接中斷。


---


## 六個 Component 各自的職責邊界是什麼？


六個 component 按照「思考腦」與「執行手」分成兩組，每個 component 只負責一件事，不做任何鄰居的工作。

 
  Agentic Loop Core
 
orchestrates: Context Assembly → LLM → Tool Loop
  
  
 
 
 

 

 
  Session Plugin
 
task state
 
checkpoints
 
open items
  
 Memory Plugin
 
learned patterns
 
user context
  
 Knowledge Plugin
 
runbooks
 
cluster topology
 
K8s docs
 
 
 

  

 
  Tool Registry
 
 kubectl-get kubectl-logs kubectl-events metrics-query 
  
 K8s Client
 
K8s API abstraction
 
auth & namespace scope
 


| Component | 做什麼 | 不做什麼 |
| --- | --- | --- |
| Agentic Loop Core | 協調整個執行流程 | 不碰 K8s 細節，不判斷要記什麼 |
| Context Assembler | 呼叫 plugins、管理 token budget | 不知道 plugins 怎麼實作 |
| Session Plugin | task state 的讀寫 | 不判斷什麼值得記 |
| Memory Plugin | 跨 session 學習 | 不碰即時 K8s 狀態 |
| Knowledge Plugin | static knowledge 的 retrieval | 不自己寫入 |
| Tool Registry | 管理 tool 定義和 executor | 不管 LLM 怎麼用它 |
| K8s Client | K8s API 呼叫抽象層 | 不做 LLM 邏輯 |


這些邊界不是為了整潔，是為了可替換性。換一個 memory storage backend，只改 Memory Plugin 的內部，其他 component 不受影響。換一個 K8s cluster 連線方式，只改 K8s Client，Tool Registry 的 tool 定義不需要動。


---


## 一個 K8s 調查 Request 怎麼流過這個系統？


一個 K8s 調查 request 從進來到結束，經過 Context Assembly、LLM 決策、Tool Execution、Post-session 四個階段，Session Plugin 在首尾兩端保護任務狀態的連續性。

 
 正常路徑
 
 「api-server OOMKilled，幫我看一下」
  
↓
 
 Context Assembly
 
  Session 「上次查到 memory limit 95%，root cause 未確認」 
 
 Memory 「過去 3 次 OOMKilled 都是 memory limit 設太低」 
 
 Knowledge 「OOMKilled runbook：check limits → trend → leak」 
 
↓
 
 LLM 決定 tool 順序
 
 kubectl describe pod kubectl logs --previous metrics-query [1h] 
  
↓
 
 Tool Execution（3 次 tool call）
 
→ memory limit: 512Mi，actual peak: 1.8Gi
  
↓
 
 LLM 得出結論
 
limit 不足是 root cause
  
↓
 
 Post-session
 
  Session checkpoint: OOMKilled confirmed，512Mi < 1.8Gi 
 
 Memory write: api-server OOMKilled → memory limit 不足，建議 2Gi 
 
↓
 
 Response to user
  

 
Context Compaction 路徑
 
  ⚠ context window 接近上限（mid-investigation）
  
↓
 
 Session Plugin 緊急 checkpoint
 
把 open investigation items 寫入 task state
  
↓
 
 Compaction 觸發
  
↓
 
 下一個 user message → Context Assembly 重新執行
  
↓
 
 Session Plugin 載入 checkpoint → 調查繼續，不從頭
 

**正常路徑：**


```
"api-server OOMKilled，幫我看一下"
 │
 ▼
Context Assembly（Plugin Point A）
  Session Plugin → "上次查到 memory limit 95%，root cause 未確認"
  Memory Plugin  → "過去 3 次 OOMKilled 都是 memory limit 設太低"
  Knowledge Plugin → "OOMKilled runbook：check limits → trend → leak"
 │
 ▼
LLM 決定 tool 執行順序：
  kubectl describe pod/api-server
  kubectl logs api-server --previous
  metrics-query memory_usage[1h]
 │
 ▼
Tool Execution（三次 tool call）
  → "memory limit: 512Mi，actual peak: 1.8Gi"
 │
 ▼
LLM 得出結論：limit 不足是 root cause
 │
 ▼
Post-session（Plugin Point B）
  Session Plugin → checkpoint: "OOMKilled confirmed: limit 512Mi < usage 1.8Gi"
  Memory Plugin  → write: "api-server OOMKilled → memory limit 不足，建議 2Gi"
 │
 ▼
Response to user
```


**Context Compaction 觸發時：**


```
mid-investigation: context window 接近上限
 │
 ▼
Session Plugin 緊急 checkpoint
  → 把 open investigation items 寫入 task state
 │
 ▼
Compaction 觸發（conversation 被壓縮）
 │
 ▼
下一個 user message → Context Assembly 重新執行
Session Plugin 載入 checkpoint
  → 調查從上次的狀態繼續，不從頭
```


Context compaction 是一個預期事件。Session Plugin 的設計目標，是讓 compaction 之後的恢復對 user 透明——agent 繼續調查，不說「我不知道我在做什麼」。


---


## 這個架構具體解決了什麼？


這個架構解決一個明確的問題：K8s SRE agent 在調查中途遭遇 context compaction，應該從上次的狀態繼續，而不是從頭開始。三個機制各自負責一個保障。


- Session Plugin 保證 task state 在 compaction 前被存下來，在 compaction 後被正確載入
- Token budget 仲裁保證 session state 不被 Memory / Knowledge 擠掉
- Plugin 介面保證未來加入 Memory 和 Knowledge 層，不需要修改 Agentic Loop Core


系列的第二篇會討論開發 Roadmap：怎麼用這個架構規劃三個 Phase，以及兩個人怎麼分工讓三層可以獨立開發。
 
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

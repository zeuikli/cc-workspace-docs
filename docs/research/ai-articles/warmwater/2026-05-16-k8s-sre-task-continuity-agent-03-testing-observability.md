---
url: "https://warmwater.dev/blog/k8s-sre-task-continuity-agent-03-testing-observability"
title: "K8s SRE Task Continuity Agent（三）：Testing 與 Observability 設計"
date: 2026-05-16
category: System Design
source: warmwater.dev
---

[
← System Design ](/blog?tag=System%20Design)  System Design 
 
# K8s SRE Task Continuity Agent（三）：Testing 與 Observability 設計
 
 2026-05-16 · — views  
  
  
把一個 LLM 做成可以放心交付的 Agentic System，大概要走完下面四格的歷程。

 ▸ SYSTEM BUILD SEQUENCE 
 
 LV 1
 
 


  
 
  
 


 
LLM Model
 
語言推理
裸奔上陣
  
 
 
▶
 
equip
 
 LV 2
 
  🪂
 
 ⚔️
 
  


  
 
  
 


 
🛡️
 
Agentic System
 
Plugin 架構
Tool + Memory
  
 
 
▶
 
enter
 
 LV 3
 
 
 
⬛
 

  
 🔥
 
  


  
 
 
🔥
  
SANDBOX
 
Sandbox Env
 
Minikube
5 個 SRE 場景
  
 
 
▶
 
observe
 
 LV 4
 
 
 

 

 

  
 
 

 
↙
  
  


  
 
  
 


 
Observability
 
3 層 monitoring
Self Improve
 

裸奔的 LLM → 裝上 Plugin 武裝 → 送進 sandbox 地下城接受 K8s failure 場景的考驗 → 再用 observability 把數據回饋回來調整。前兩格是篇一和篇二的主題；這篇討論後兩格——送進地下城之後的事。


Agentic System 的 testing 有一個根本問題：你沒辦法直接對輸出做 assert。傳統服務你可以說「這個 API call 應該回傳 200，body 是這個 JSON」。Agent 不行。同一個 OOMKilled 問題，agent 可能用三步解決，也可能用七步——只要最後得出正確的 root cause，兩條路都算對。你要驗的不是輸出，是行為路徑：agent 有沒有呼叫正確的 tool、有沒有得出結論、加了 Memory Plugin 之後有沒有利用過去的 pattern 縮短調查路徑。


這是三篇系列的最後一篇，討論 Testing 和 Observability：怎麼建 Minikube sandbox 讓每個 failure 場景可以重現、怎麼設計 regression test 讓每個 Phase 的品質保證可以累積、以及用三層 monitoring 看系統在不同維度的健康狀態。


---


## Minikube Sandbox 為什麼需要兩層設計？


Testing Agentic System 的 sandbox 需要拆兩層：Scenario Layer 負責製造 K8s failure，Validation Layer 負責驗 agent 的反應。把這兩件事放在同一層，是讓 test 難以維護的常見原因。


Scenario Layer 做的是 K8s 層面的工作：把 cluster 設定到對應的 failure 狀態，測試結束後 teardown，還原 namespace。這一層不知道也不需要知道 agent 怎麼運作，它只保證 cluster 的狀態符合場景定義。


Validation Layer 做行為驗證：給定一個問題，agent 呼叫了哪些 tool、以什麼順序、最後有沒有得出 root cause 結論。這一層不知道 K8s 怎麼製造 OOMKilled，它只驗行為。

 
 Scenario Layer
  
  setup script
 
→
 
 Minikube Cluster
 
K8s failure state
  
←
 
teardown script
 
 
 
 
 
failure state exposed
 
↓
 
  Validation Layer
  
 Agent
 
tool calls + reasoning
  
→
 
 ✓ tool call sequence correct?
 
✓ root cause conclusion reached?
 
✓ memory / knowledge used?
 

兩層分離的好處是可以獨立測試：Scenario 可以單獨驗「OOMKilled 有沒有成功製造」，Validation 可以用 mock K8s 狀態跑行為測試，不需要每次都起一個真的 failing pod。這兩個責任獨立，debug 的時候才知道問題在哪一層。


---


## 五個核心 K8s 場景怎麼選？


五個場景是按「需要不同 tool 呼叫路徑」來選的，不是按「常見故障頻率」來選的。如果五個場景最後都走同一條 describe → logs 路徑，你只是在重複驗同一個行為。


| Scenario | Setup 方式 | Agent 預期行為 |
| --- | --- | --- |
| OOMKilled | 低 memory limit pod + 高用量 workload | kubectl describe + logs —previous → 找 limit vs usage gap |
| CrashLoopBackOff | pod 啟動後立即 exit 1 | kubectl logs → 讀 exit reason |
| PodPending | 超出 node 資源的 resource request | kubectl describe + get nodes → 找 schedulability 問題 |
| Eviction | 人工填滿 node disk | kubectl get events → 識別 eviction 原因 |
| ImagePullBackOff | 不存在的 image tag | kubectl describe pod → 找 image reference 錯誤 |


OOMKilled 和 CrashLoopBackOff 看起來相似，但 OOMKilled 需要讀 previous container 的 logs，CrashLoopBackOff 讀 exit code——tool 序列不同。PodPending 完全不需要看 logs，只需要 describe 和 node 資源。Eviction 要從 events 找線索，不是 pod 層面。五個場景加在一起，覆蓋了需要不同資訊來源的主要調查路徑。


Sandbox 不需要模擬的東西：生產規模 cluster、真實 workload 流量、multi-node HA 場景。這些是 infra 測試的問題，不是 agent 行為測試的問題。


---


## Regression Test 怎麼跟著 Phase 累積？


每個 Phase 加測試，不刪前一個 Phase 的測試。Phase 3 做完，三個 Phase 的 test case 都要過。這讓「不退步」變成 CI 可以強制執行的規則，不是靠人記住。


**Phase 1 Regression：**


| Test Case | 驗證什麼 |
| --- | --- |
| 基本調查完成 | Agent 能從問題到結論跑完整個 loop |
| Compaction Resume | 模擬 compaction，agent 能從 checkpoint 繼續 |
| Tool 正確性 | 每個 K8s tool 的 output 格式正確 |
| Session Plugin read/write | Task state 存得進去、讀得出來 |


**Phase 2 新增：**


| Test Case | 驗證什麼 |
| --- | --- |
| Memory Recall | 同類 incident 第二次，agent context 有 past pattern |
| Write Trigger | OOMKilled 結束後，pattern 有被寫進 memory |
| Token Budget | Memory + Session 共存，不超出 context budget |


**Phase 3 新增：**


| Test Case | 驗證什麼 |
| --- | --- |
| Runbook Retrieval | OOMKilled 時，runbook 相關內容有出現在 context |
| Budget 仲裁 | 三個 plugin 共存，沒有任何一個被完全擠出 |


「Phase 1 + 2 的所有 test case 繼續通過」是 Phase 3 的 done criteria 之一，不是 nice-to-have。新功能讓舊測試 fail，是架構邊界沒有守住的信號。


---


## Agentic System 需要監控哪三層指標？


Agentic System 的 monitoring 需要三個觀察點，對應三個不同的問題：任務有沒有完成、context 資源用得健不健康、memory 和 knowledge 有沒有實際在發揮作用。


**Layer 1：Agent 行為（任務層面）**


```
task_completion_rate → agent 有沒有得出結論
tool_calls_per_investigation → 每次調查平均呼叫幾個工具
time_to_resolution → 從問題到回答的時間
```


這一層的指標給使用者和產品看。`tool_calls_per_investigation` 如果在加了 Memory Plugin 之後沒有下降，Memory Plugin 可能沒有有效縮短調查路徑，write trigger 或 search quality 可能有問題。


**Layer 2：Context Engineering（資源層面）**


```
context_window_utilization → context window 用了幾 %
token_budget_by_plugin → 每個 plugin 實際用了多少 token
compaction_frequency → compaction 多久觸發一次
```


這一層給工程師看。`token_budget_by_plugin` 能看出哪個 plugin 在佔用資源但沒有被 LLM 引用——是優化 budget 仲裁的起點。


**Layer 3：Memory / Knowledge 品質（學習層面）**


```
memory_write_rate → 每次 session 寫入幾筆 memory
memory_hit_rate → Context Assembly 時 memory 有沒有 match
memory_age_distribution → memory 的年齡分佈
knowledge_retrieval_usage → Knowledge snippet 有沒有被 LLM 引用
```


這一層給系統健康看。`memory_hit_rate` 持續偏低，代表 write trigger 太嚴（記太少）或 search query 沒有正確 match 已有 pattern。


---


## 為什麼 context_window_utilization 是 Canary Metric？


三層 monitoring 裡，`context_window_utilization` 是最值得盯的單一指標——它同時能反映三層的問題。


持續 > 90%：task 太長 / plugin budget 設太寬鬆 / token budget 仲裁有 bug。這個狀態下，compaction 頻繁觸發，每次 compaction 都是一次 checkpoint restore，調查效率下降。


持續 < 40%：Memory 和 Knowledge retrieval 沒有實際注入任何東西，或 plugin 根本沒有被正確呼叫。這個狀態下 agent 看起來「正常運作」，但三層 plugin 架構可能是空殼。


40% 到 90% 之間的穩定區間，代表 Context Assembly 在正常工作——三個 plugin 各自貢獻了 context，token budget 仲裁也在發揮作用。


---


## 三篇做完，這個系統的設計練習交出了什麼？


篇一定義架構邊界：兩個 plugin 點、三個 plugin 各自的責任、token budget 仲裁規則。


篇二設計開發計畫：Interface-First 讓兩人可以並行、三個 Phase 讓每一層可以獨立驗收、「刻意不做」讓 Phase 不會無限延伸。


篇三回答怎麼知道系統是不是真的在運作：Minikube 兩層 sandbox 讓 failure 場景可以重現，regression test 累積讓品質保證不隨 Phase 推進而退步，三層 monitoring 讓問題出現在哪一層可以被看見。


三篇加在一起是一個完整的 System Design 練習——從問題定義到架構設計、開發計畫到品質保證。K8s SRE 是 scenario，背後真正在練習的是：怎麼把一個複雜的 Agentic System 設計成可以分層開發、獨立驗收、可以被觀測的樣子。
 
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

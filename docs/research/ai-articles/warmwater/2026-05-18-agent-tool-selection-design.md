---
url: "https://warmwater.dev/blog/agent-tool-selection-design"
title: "AI Agent 工具越多越選錯？從 N-class 分類看 Tool System 設計"
date: 2026-05-18
category: Harness Engineering
source: warmwater.dev
---

[
← Harness Engineering ](/blog?tag=Harness%20Engineering)  Harness Engineering 
 
# AI Agent 工具越多越選錯？從 N-class 分類看 Tool System 設計
 
 2026-05-18 · — views  
  
  
你的 agent system 有幾個工具？這個數字不只是功能清單的長度，它決定了 tool selection 的基礎難度。大部分人在設計 agent 的時候，思路是加功能：這個 agent 需要搜尋、需要查日曆、需要發信，所以加三個工具。但 research 顯示，工具從 10 個擴展到 100 個時，所有主流模型的 selection accuracy 都下降；從 8K tokens 的工具描述擴展到 120K tokens，performance drop 最高達到 85%。這種退化往往是悄悄發生的——agent 仍然在執行工具呼叫，只是選的工具越來越不對。


**讀完這篇，你會理解：**


- 為什麼 tool selection 本質上是 N-class 分類問題，以及這對準確率有什麼影響
- LLM 在工具變多時的三個具體崩潰機制
- DeerFlow、HermesAgent、OpenClaw 三個真實系統怎麼應對這個問題
- 觀察這三個系統的設計重心，以及可以進一步延伸思考的方向


這篇不是 tool 設計的 checklist，而是試圖說明一個設計選擇背後的力學。


---


## 為什麼 Tool Selection 是 N-class 分類問題？


當 agent 要選工具，它在做的事情是：給定 user intent，從 N 個候選工具中選最適合的一個。


這是個 N-class classification problem。


這個定性很重要。研究顯示工具數量增加會同時觸發兩個獨立的失敗機制：**instance count degradation** 和 **semantic ambiguity**，而不只是「context 變長，attention 被稀釋」這麼單純。


arxiv 2603.22608 研究了 LLM 在 multi-instance processing 下的退化，發現所有模型都呈現「小數量時緩慢下降、大數量時突然崩潰」的模式。更關鍵的 finding 是：**instance count 對 degradation 的影響比 context 長度本身更強**。就算 context window 足夠大，工具數量增加本身就會讓準確率下降。這直接挑戰了「只要 context window 夠大就沒問題」的直覺。


ToolScope 則指出另一個獨立問題：overlapping tool descriptions 造成的 ambiguity 降低了 retrieval 和 selection accuracy，而這和 context 長度無關。問題出在工具之間的語意邊界模糊，不是工具太多。


工具的情況更特別，因為工具之間通常語意相近。`search_web` 和 `search_docs` 的語意距離，遠比「貓」和「汽車」的語意距離小。數量增加和語意相近這兩個因素同時作用，才是實際系統裡崩潰往往比預期劇烈的原因。


---


## 工具增多時，LLM 的 Tool Selection 在哪裡出錯？


LLM 的 tool selection 在工具數量增加時有三個獨立的失敗點：context 裡的工具描述佔用 attention、語意相近的工具讓 decision boundary 模糊，以及 system prompt 的 instruction following 品質隨複雜度非線性下降。


### Attention 被稀釋


LLM 在選工具之前，要先讀懂所有工具的描述。工具描述是 context 的一部分，而 Transformer 的 attention 機制是在整個 context 上計算的。


3 個工具：


```
- search_web(query) → 搜尋網路
- get_calendar(date) → 查日曆
- send_email(to, subject) → 寄信
```


12 個工具：


```
- search_web / search_docs / search_internal_kb / search_confluence
- get_calendar / get_meeting / get_task / get_reminder
- send_email / send_slack / send_teams / send_sms
```


LongFuncEval 測了從 8K 到 120K tokens 的工具目錄，不同模型的 performance drop 從 7.59% 到 85.58% 不等，主要歸因是 formatting error 增加和 hallucination 率上升。HumanMCP 的量測更直接：工具從 10 個擴展到 100 個，所有受測模型的 Top-1 Hit Rate 下降約 10%；最劇烈的崩潰發生在 1,000 到 2,000 個工具之間。


但前面提到的 instance count 研究讓這個機制更精確：**token 增加是次要因素，instance 數量才是主因**。工具描述讓 context 變長是問題的一部分，但工具本身作為 N 個決策候選項出現在 context 裡，對 LLM 推理的干擾比 token 數帶來的影響更大。


工程上的 implication：工具描述不是無成本的，但解法不只是「壓縮每個工具的描述長度」，而是要減少 LLM 同時看到的工具數量。


### 語意相似造成 Decision Boundary 模糊


這是最核心的問題。相似工具之間的選擇，對 LLM 來說比不同領域的工具選擇難得多。


```
user: "幫我找上週的會議記錄"

candidates:
- search_docs(query) → 搜尋文件
- search_confluence(query)  → 搜尋 Confluence
- get_meeting(date) → 查會議
- search_internal_kb(query) → 搜尋內部知識庫
```


這四個工具在語意空間裡距離很近。ToolScope 指出，overlapping tool descriptions 造成的 ambiguity 會同時降低 retrieval accuracy（找到正確工具）和 selection accuracy（選對工具）。這個問題和工具數量是獨立的。即使你只有四個工具，只要描述語意重疊，LLM 一樣會選錯。


工程上的 implication：這不是 model 的問題，是 tool design 的問題。即使模型換得更好，如果工具的描述語意邊界模糊，選錯的機率不會消失。


### Instruction Following 品質下降


工具越多，system prompt 就越長，隱式的「什麼情況用哪個工具」的邊界條件就越複雜：


```
工具少時：
"你有以下工具：[3 個工具描述]
根據用戶需求選擇最合適的工具。"

工具多時：
"你有以下工具：[12 個工具描述，每個帶參數說明]
注意：search_web 用於外部資訊，search_docs 用於內部文件，
search_confluence 只用於 wiki 頁面，search_internal_kb 用於 FAQ...
[一堆 edge case 說明]"
```


IFEval benchmark 的研究顯示，LLM 的 instruction following 品質隨著 instruction 複雜度非線性下降。工具越多，system prompt 裡的隱性約束就越多，模型遵循的一致性就越低。


工程上的 implication：解決方法不是把 tool selection 規則寫得更詳細，因為那只會讓 system prompt 更複雜。


---


## DeerFlow、HermesAgent、OpenClaw 怎麼應對工具數量問題？


三個開源 agent system 分別在不同的架構層解決了工具數量問題：DeerFlow 選擇 runtime 懶加載、HermesAgent 選擇 init-time 工具集切割、OpenClaw 選擇 policy 型的 per-agent 白名單。以下是讀源碼時觀察到的具體設計。


### DeerFlow：懶加載而非全展開


DeerFlow 的解法叫 `DeferredToolRegistry`，搭配一個 `tool_search` 工具：


```
# 若 tool 太多，用 tool_search 懶加載
if config.tool_search.enabled:
 registry = DeferredToolRegistry()
 # 只暴露 tool_search 給模型，其他工具延遲到需要時才載入
 builtin_tools.append(tool_search_tool)
```


設計思路是：與其在 context 裡塞滿所有工具的描述，不如只給 agent 一個工具——`tool_search`，讓它先搜尋自己需要什麼工具，再呼叫那個工具。工具 schema 只在被選中的時候才注入 prompt。


DeerFlow 文件的原話是：「MCP 工具數量可能很多（幾十甚至幾百個）。將所有工具 schema 注入 prompt 會耗費大量 tokens。」


這直接對應了第一個崩潰機制（attention 稀釋）。代價是多一個 LLM call（先搜尋，再呼叫），但換來的是每次 tool call 時 context 是乾淨的。


### HermesAgent：初始化時就切割工具集


HermesAgent 的解法在架構更前面一層。它定義了 `TOOLSETS`：


```
TOOLSETS = {
 "web": ["web_search", "web_extract"],
 "terminal": ["terminal", "process"],
 "file": ["read", "write", "edit", ...],
}
```


每個 agent 啟動時只拿到被指派的 toolset，而不是全部工具。`toolset_distributions.py` 更進一步，可以按機率控制哪些 toolset 被啟用。在 batch 或 RL 訓練的場景下，刻意讓 agent 不同時接觸所有工具，讓每個決策點的 context 維持乾淨。


Delegate 工具（子代理呼叫）的繼承規則也值得注意：


```
child_toolsets = [t for t in toolsets if t in parent_toolsets]
```


子代理只能繼承父代理 toolset 的子集，不能拿到父代理沒有的工具。這間接達到了 hierarchical scoping 的效果：orchestrator 有完整工具集，leaf agent 只拿到被明確賦予的子集。不是顯式的分層路由，而是透過繼承約束讓每一層的工具可見範圍自然收斂。


DeerFlow 和 HermesAgent 的設計哲學不同：DeerFlow 是 runtime 懶加載（工具描述按需進入 context），HermesAgent 是 init-time 切割（工具集在初始化就限縮）。前者靈活，後者確定。


### OpenClaw：Allow/Deny Policy + Group


OpenClaw 的解法更接近 permission model。它用 `TOOL_GROUPS` 做 per-agent 的白名單和黑名單，在 group 層級控制工具可見性。設計目的和 HermesAgent 的 toolset 分組一致，都是防止單一 agent context 被過多工具佔滿，但實現方式是策略型的（policy），而不是結構型的（toolset 繼承）。


三個系統的設計方向對比：


| 系統 | 設計層次 | 核心機制 | 覆蓋的失敗點 |
| --- | --- | --- | --- |
| DeerFlow | Runtime | DeferredToolRegistry + tool_search 懶加載 | 工具描述按需注入，避免佔滿 context |
| HermesAgent | Init-time | TOOLSETS 分組 + delegate 繼承約束 | 每個 agent 只接觸指派的工具子集 |
| OpenClaw | Policy | TOOL_GROUPS Allow/Deny per-agent 白名單 | 策略層控制工具可見範圍 |


三個解法都指向同一個核心：減少 LLM 在單次決策時同時看到的工具數量。


---


## 數量問題之外：語意邊界設計與 Eval 可見性


三個系統的設計重心是一致的：管理 LLM 同時看到的工具數量，讓每個決策點的 context 維持乾淨。這個方向是對的，也有效。


但對照前面分析的兩個獨立失敗機制，可以看到這些系統主要覆蓋了 **instance count degradation**，也就是數量問題。另一個方向，**semantic ambiguity**，基本上還是留給了設計者自己處理。


**工具描述的語意邊界設計。** 三個系統都在控制工具可見範圍，但沒有機制協助判斷「這兩個工具的描述是不是語意太近」。沒有 embedding-based 的相似度檢查，沒有 tool description quality validation。


可以思考的方向是：在設計或審查工具集的時候，把每個工具的描述放進同一個 embedding space，量一下兩兩之間的相似度。如果 `search_docs` 和 `search_confluence` 的 description embedding cosine similarity 超過某個閾值，這就是一個信號：LLM 在這兩個工具之間的 decision boundary 可能不夠清楚，需要在描述裡更明確地定義邊界條件。


**Tool selection accuracy 的 eval 層次。** 三個系統都有 retry 機制（HermesAgent 有非常完整的 `error_classifier`），但 retry 是在工具呼叫失敗之後才介入，無法捕捉「工具選錯了、但執行成功了」的情況。


`ArgumentCorrectnessMetric` 告訴你「參數有沒有填對」，但不告訴你「工具選對了嗎」。一個 agent 選了 `search_confluence` 而不是 `search_docs`，兩個工具都成功執行了，參數也都合法——這個選擇是對是錯，在現有的 eval 體系裡是看不見的。


如果想要在這個層次建立可見性，需要的是 tool selection ground truth：對一組 user queries 標注「正確的工具應該是哪個」，然後量 Top-1 accuracy。這比 argument correctness 更上游，也更能反映工具描述設計的品質。


---


把這兩個方向放在一起看，有一個更深的含意。


這三個系統設計的出發點，是把工具當成功能清單來管理：太多了就切割、限制可見性、懶加載。這些是正確的工程直覺，但它們解決的是工具的數量問題。


而 tool selection accuracy 更根本的決定因素，是每個工具在 LLM 的表示空間裡有沒有清晰的、不重疊的邊界。這是分類問題的設計問題，不只是工程管理問題。設計工具，本質上是在設計一個分類系統：每個 class 的邊界要清楚，class 之間的語意距離要夠大，條件交叉的 edge case 要在描述裡明確定義。


工具加功能很容易，設計清楚的分類邊界很難。這個難點，目前的系統基本上還是留給了人工。


---


> 
**結語**：在 agent 系統裡加工具不難，難的是讓每個工具在 LLM 的眼裡有足夠清晰的邊界。工具數量是可見的問題，語意邊界是隱形的問題，而目前大多數系統解了前者，留下了後者。

  
  
 [ Harness Engineering ](/blog?tag=Harness%20Engineering)[ AI Agent ](/blog?tag=AI%20Agent) 
 

### 相關文章
[System Design

Agent 要怎麼進化？六個系統的 Self-Improvement 機制比較

2026-05-22
](/blog/agent-self-improvement-design-comparison)[
System Design

SOUL 設計決定了 Agent 是什麼：六個 Agentic System 的 system prompt 比較

2026-05-22
](/blog/agent-soul-design-comparison)[
Viewpoint

你在比的是模型，但決定 Claude Code 效果的是 Harness

2026-05-20
](/blog/claude-code-harness-over-model)

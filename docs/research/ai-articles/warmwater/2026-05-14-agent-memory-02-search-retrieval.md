---
url: "https://warmwater.dev/blog/agent-memory-02-search-retrieval"
title: "Memory 02：記憶怎麼被找到——四種搜尋模式與 Write-Search 耦合"
date: 2026-05-14
category: Source Code
source: warmwater.dev
---

[
← Source Code ](/blog?tag=Source%20Code)  Source Code 
 
# Memory 02：記憶怎麼被找到——四種搜尋模式與 Write-Search 耦合
 
 2026-05-14 · — views  
  
  
「搜尋記憶」這件事，八個系統給出了截然不同的答案。有些根本不搜；有些只用關鍵字匹配；有些同時跑三個 signal 再 fusion；有些先看摘要再決定要不要展開細節。


這些差異不是品味問題，而是由一個更早的決定決定的：**你寫進記憶的是什麼**。


LLM extraction 寫進去的是壓縮後的 facts，語意已正規化，適合 semantic search。Agent 精煉寫進去的是決策敘述，沒有 paraphrase 問題，BM25 就夠了。Verbatim chunk 保留原文，chat 和 code 混在一起，需要 hybrid 才能同時處理語意模糊和精確字詞。Write 和 Search 是耦合的決策，不是獨立的。


**讀完這篇，你會理解：**


- 四種 search archetype 各自對應什麼寫入假設
- Hybrid 的三個系統（mem0、agentmemory、mempalace）為什麼選了不同的 fusion 策略
- Paraphrase 問題是在 write time 解決還是 search time 解決，各自的代價是什麼
- 為什麼 retrieval granularity 的選擇是一個賭注


---


## Write 決定 Search：這篇的框架


在看四個 archetype 之前，先建立一個判斷框架。每個系統的搜尋策略，都可以從它的寫入內容推導出來：


| 寫入方式 | 寫入內容 | 搜尋適配 |
| --- | --- | --- |
| LLM extraction（mem0） | 壓縮 facts（~20 chars） | semantic：paraphrase 已消除 |
| Agent 精煉（engram） | 決策敘述（~100-300 chars） | BM25：agent 寫入時已正規化 |
| Verbatim chunk（mempalace） | 原文（800 chars） | hybrid：chat 有 paraphrase，code 要精確字詞 |
| Hooks 自動捕捉（agentmemory） | 大量 raw tool call | multi-signal：noise 多，需多路 fusion |
| 完整對話（hermes Layer 2） | 原始 messages | FTS5：tool name 和 精確字詞 |


這個對應關係貫穿整篇文章。


---


## Archetype 1：不搜，全量注入 — 當搜尋成本比注入還高


**代表系統：deerflow、letta Core Memory**

 Archetype 1 · 不搜，全量注入
 
 deerflow
 

agent 回應前
每次都執行
  
↓
 

memory.json
最多 100 facts
  
不做任何搜尋
 
↓
 

全量注入
所有 facts 放進 system prompt
  
↓
 

System Prompt
agent 直接可見
  
100 facts 上限確保注入成本可控
搜尋成本 > 注入成本時不搜更划算
  

  
 letta
 

Core Memory Block
常駐 `<memory_blocks>` in system prompt
  
永遠可見，不需搜尋
 
↓
 

System Prompt
每次 LLM call 都包含
  
— 另一條路 —
 

需要更多資訊時

 
↓
 

Archival Memory
PostgreSQL + pgvector
  
archival_memory_search（按需）
 
Core 不搜；Archival 才搜
兩條路徑，不同成本
 

不搜尋，不是設計缺失，而是一個明確的判斷：記憶夠小，或者永遠相關，直接放進 context 比搜尋划算。


deerflow 把整個記憶限制在 100 facts 以內，agent 每次回應前把全部 facts 注入 system prompt。這個 100 的上限不是隨意設的——它確保全量注入的 token 成本維持在可接受範圍內。搜尋本身有成本：embedding call、vector index 查詢、relevance 判斷。當記憶夠小，這些成本比直接注入還高。


letta 的 Core Memory Block 常駐在 system prompt 的 `<memory_blocks>` 裡，agent 在每次對話當下都看得到。這是 letta 的設計核心：Core Memory 不需要搜尋，因為它本來就在 context 裡。需要搜尋的是 Archival Memory——容量無上限的外部存儲，靠 vector search 按需取用。


這個模式的工程含義：每次都付 context token 成本，記憶規模不能無限增長。適合記憶集中、高度相關的場景（個人偏好、當前專案慣例），不適合需要長期累積大量 facts 的場景。


---


## Archetype 2：單一 BM25 — Write Time 精煉換 Search Time 簡單


**代表系統：engram、hermes Layer 2**


 Archetype 2 · 單一 BM25（SQLite FTS5）
 
 engram
 

Write time：agent 已精煉

topic_key upsert → 同 topic 只有一筆

 
↓
 

mem_recall(query)
MCP tool 呼叫
  
↓
 

SQLite FTS5 BM25
詞頻排名 · 精確字詞匹配
  
↓
 

Topic Entries
~100-300 chars · type + title + content
  
↓
 

Top-k 結果
MaxContextResults（預設 20）
  
無 embedding · 無外部 API
  

  
 hermes Layer 2
 

Write time：完整對話歷史

messages 原文寫入 FTS5 virtual table

 
↓
 

conversation_search(query)
SessionDB 工具
  
↓
 

SQLite FTS5 BM25
messages_fts virtual table
  
↓
 

messages table
完整對話 · session_id 關聯
  
↓
 

Top-k 結果
tool name · 檔名 · 精確字詞
  
tool call log 無 paraphrase 問題
 

BM25（Best Match 25）是一個基於詞頻的關鍵字排名算法，精確字詞匹配，不理解語意。它的優點是快、無需 embedding、結果可解釋。SQLite FTS5（Full-Text Search 5）是 SQLite 內建的全文搜尋引擎，底層用 BM25 做排名，零外部依賴。


engram 只用 SQLite FTS5，沒有 vector search。這個選擇有它的前提：engram 要求 agent 主動呼叫 `mem_save`，並在 SKILL.md 裡定義強制觸發條件。Agent 在寫入時已經做了語意精煉——「用戶偏好 dark mode」不會以五種不同說法存進去，因為 agent 會用 `topic_key` upsert 保證同一 topic 只有一筆最新記錄。


當寫入內容已精煉，paraphrase 問題在 write time 就消除了，BM25 就夠用。


hermes Layer 2 存的是完整的原始對話歷史，用 SQLite FTS5 對 messages 做全文搜尋。這裡 BM25 的優勢在於精確字詞：搜尋 `write_file` 或 `auth.go` 這類 tool name 和檔名，BM25 比 semantic search 更精確。


這個模式的工程含義：信噪比高，搜尋結果可解釋，無需外部 embedding API。代價是無法處理語意跳躍——搜尋「驗證機制」找不到存了「JWT 設計」的記憶。


---


## Archetype 3：Multi-signal Hybrid — 三個系統，三種 Fusion 策略


**代表系統：mem0、agentmemory、mempalace**


 Archetype 3 · Multi-signal Hybrid
 
 mem0
 

query
+ filters（user_id...）
  
↓
 
3 個 signal 並行
 
 Semantic（HNSW）
語意向量搜尋
 
BM25（lemmatized）
關鍵字匹配
 
Entity Boost
人名 / 概念加分
  
↓
 

Score 加法 Fusion
BM25 先 sigmoid 正規化再相加
  
↓
 

Top-k facts
~20 chars each
  
chat-heavy · 消除 paraphrase
  

  
 agentmemory
 

query
mem::recall
  
↓
 
3 個 signal 並行
 
 BM25
iii KV 全文搜尋
 
Vector
in-memory HNSW
 
Graph
entity 關聯圖
  
↓
 

RRF Fusion
只看排名，不看分數尺度
  
↓
 

Top-k items
~200 chars each
  
tool-heavy · 壓 raw noise
  

  
 mempalace
 

query
mempalace_search()
  
↓
 
3 個 signal 並行
 
 HNSW（cosine）
語意向量搜尋
 
Closet Boost
同抽屜鄰近記憶加分
 
BM25 rerank
0.4 weight
  
↓
 

加法 Fusion（0.6 / 0.4）
HNSW 0.6 + BM25 0.4
  
↓
 

Top-k chunks
~800-2400 chars（含鄰居）
  
verbatim · chat + code 兼顧
 

三個系統都選了 hybrid，但動機和實作截然不同。


在解釋三個系統之前，先說清楚幾個名詞：


- **HNSW**（Hierarchical Navigable Small World）：向量近鄰搜尋索引，在高維向量空間中快速找到語意相近的記憶
- **Entity Boost**：對 query 中提到的人名、概念給對應記憶額外加分，解決「Alice」和「the user」指同一人的問題
- **Graph**：記憶間的實體關聯圖，把同一實體（人名、專案名）連結的記憶串起來，補捉間接關聯
- **RRF**（Reciprocal Rank Fusion）：排名融合算法，只看各 signal 的排名順序，不依賴分數尺度，避免不同算法的分數無法直接相加的問題
- **Closet Boost**（mempalace 的空間隱喻）：命中同一「記憶宮殿抽屜」的記憶獲得額外加分，鄰近記憶一起浮現


**mem0** 的場景假設是 chat-heavy：用戶說「我喜歡 dark mode」和「我偏好暗色介面」是同一件事，extraction 在寫入時把這兩句話都壓縮成同一個 fact，但即便如此，query 和 stored fact 之間仍可能有語意距離。mem0 用三個 signal fusion：semantic search（HNSW）處理語意相近，BM25 處理精確字詞，entity boost 解決人名指涉問題。Fusion 用分數加法，BM25 先做 sigmoid 正規化再相加。


**agentmemory** 的場景是 tool-heavy coding agent：Working Memory 裡存了大量 raw tool call observations（`edit: auth.go`、`bash: go build` 之類），noise 比 chat 高很多。它用 BM25、vector、entity graph 三路 RRF fusion——RRF 的好處是不需要對各 signal 的分數做正規化，只看每個 signal 裡的排名位置。Graph signal 把同一 entity（函式名、檔名）連結的記憶串起來，補捉「改了這個函式的記憶」和「這個函式影響的 test 記憶」之間的關聯。


**mempalace** 存的是 verbatim 原文，chat 有 paraphrase，code 要精確字詞，兩者要求不同。HNSW 處理 chat 的語意模糊，BM25 處理 code 的精確字詞。Closet boost 是 mempalace 特有的空間隱喻設計：記憶被組織在「抽屜」（closet）裡，命中某個抽屜時，同抽屜的鄰近記憶跟著浮現，確保相關 context 一起被取出。


|  | mem0 | agentmemory | mempalace |
| --- | --- | --- | --- |
| Signal 1 | Semantic（HNSW） | BM25 | HNSW（cosine） |
| Signal 2 | BM25（lemmatized） | Vector | Closet boost |
| Signal 3 | Entity boost | Graph（entity 關聯） | BM25（0.4 weight） |
| Fusion | Score 加法 | RRF | 加法（0.6/0.4） |
| 設計動機 | chat，消除 paraphrase | tool-heavy，壓 noise | verbatim，chat + code 兼顧 |


這個模式的工程含義：覆蓋面最廣，但每次搜尋要跑多個 signal，延遲比單一 BM25 高。agentmemory 用 RRF 避開了 score normalization 的問題；mem0 選擇加法但需要 sigmoid 正規化。


---


## Archetype 4：層級展開 — 先確認方向，按需展開細節


**代表系統：OpenViking**


 Archetype 4 · 層級展開 (OpenViking)
 
 OpenViking
  

query + session context
compression_summary + 最近 5 條 messages
  
↓
  

IntentAnalyzer（LLM call）
把模糊 context 轉成精確查詢計畫
  
↓
  

QueryPlan
0-5 個 TypedQuery，各有 priority + context_type
  
↓
  
HierarchicalRetriever
 

L0 Global Vector Search
全局 top-10 候選，確認方向
  
↓
 
 L0
摘要
先看方向
 
L1
細節
按需展開
 
L2
原始
最深層
  
score propagation：子節點繼承父節點分數
convergence check：無更好候選時停止展開
 
↓
  

Hotness Blending
頻率 × 時間衰減 → blend 進最終分數
  
↓
  

MatchedContext 列表
去重後注入 system prompt
  
粒度決策延後到 query 時 → token 消耗可控
  

OpenViking 的搜尋分兩步：先用 IntentAnalyzer 把 query 轉化成一個 QueryPlan（0-5 個 TypedQuery，每個有 priority 和 context type），再用 HierarchicalRetriever 按 QueryPlan 做層級展開。


層級結構是 L0（摘要）→ L1（細節）→ L2（原始內容）。Retriever 先用 L0 global vector search 確認方向，再用 priority queue 遞迴下探到 L1、L2。每一層的 score 會做 propagation（子節點 score 繼承父節點一部分）和 convergence check（發現沒有更好的候選就停止展開）。


最後，Hotness（頻率 × 時間衰減）在 search 時 blend 進最終分數。Hotness 高的記憶優先浮現，反映「最近常用的知識更相關」的假設。


其他系統都是 flat retrieval——一次 search 決定粒度。OpenViking 把粒度決策延後到 query 時，依實際需求控制展開深度，也就控制了 token 消耗。代價是複雜度：IntentAnalyzer 是一次 LLM call，整個 retrieval pipeline 比直接 vector search 重很多。


---


## Paraphrase 問題：Write Time 還是 Search Time


Paraphrase 問題是：「I love dark mode」和「I prefer dark themes」語意相同，但字詞不同。記憶系統要在哪個階段消除這個差異？


**路線 A：Write time 正規化（extraction）**
寫入前讓 LLM 把不同說法壓縮成 canonical fact。代價是有損——數字、精確字詞可能在 pipeline 中被改寫。mem0 選這條路，LoCoMo benchmark 上表現好，但 verbatim 內容無法保留。


**路線 B：Search time 解決（verbatim + embedding）**
原文完整保留，靠 embedding 模型在向量空間裡解決語意距離。mempalace 選這條路，LongMemEval R@5 = 96.6%，因為精確字詞完整保留。代價是 embedding 模型的能力決定上限。


Chat 和 tool call 的 paraphrase 問題是不對稱的：chat 有 paraphrase（「我喜歡 dark mode」和「幫我開暗色主題」是同一件事），tool call 是 deterministic JSON 幾乎沒有 paraphrase（`write_file(path="auth.go")` 就是 `write_file(path="auth.go")`）。這個不對稱解釋了為什麼 chat-heavy 系統（mem0）傾向 extraction，而 coding agent（engram）用 BM25 就夠。


---


## Retrieval Granularity：精確還是有 context


每個系統都要回答一個問題：一次搜尋要取回多大的單位？


| 系統 | 單位 | 大小 |
| --- | --- | --- |
| mem0 | extracted fact | ~20 chars |
| engram | topic entry | ~100-300 chars |
| agentmemory | consolidated memory item | ~200 chars |
| hermes Layer 1 | §-separated entry | ~50-500 chars |
| mempalace | 800-char chunk | ~800-2400 chars（含鄰居） |
| letta Core | 整個 block | ~500-5000 chars |
| OpenViking | L0/L1/L2 多層 | 按需展開 |


核心 tension：小單位精確，但失去 why/when 的 context；大單位保留 context，但 token 成本高，ranking 精準度下降。


各系統的賭注：mem0 賭 LLM extraction 夠好，fact 粒度夠精確；mempalace 賭 embedding + BM25 能在原文裡找到對的 chunk；letta 雙軌——Core 精小、Archival 大而全；OpenViking 層級展開，先粗後細，token 消耗可控。


---


> 
**結語**：寫入內容決定搜尋方式，搜尋方式決定能取回什麼。這個耦合關係的另一面是：記憶存在哪裡，決定了搜尋用什麼索引。下一篇會從儲存格式的角度，解釋 JSON、SQLite、VectorDB 和 PostgreSQL 背後的工程取捨。

 
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

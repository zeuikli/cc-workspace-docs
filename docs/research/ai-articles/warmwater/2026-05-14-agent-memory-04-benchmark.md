---
url: "https://warmwater.dev/blog/agent-memory-04-benchmark"
title: "Memory 04：怎麼判斷哪個記憶系統強——Benchmark 數字的陷阱"
date: 2026-05-14
category: Source Code
source: warmwater.dev
---

[
← Source Code ](/blog?tag=Source%20Code)  Source Code 
 
# Memory 04：怎麼判斷哪個記憶系統強——Benchmark 數字的陷阱
 
 2026-05-14 · — views  
  
  
mempalace 96.6%，mem0 V3 93.4%。看起來 mempalace 贏了？


這兩個數字不是同一種東西，不能直接比。


---


## R@K、MRR、NDCG：三個 Retrieval 指標各測什麼？


Agent Memory 的 benchmark 分兩層：純 retrieval 指標，和 end-to-end memory 指標。


純 retrieval 指標只問 memory 系統本身，不管 LLM 後來怎麼用：


| 指標 | 問的問題 | 意義 |
| --- | --- | --- |
| R@K | 正確答案有沒有出現在 top-K 結果裡？ | 系統「找得到」的能力 |
| MRR | 正確答案平均排在第幾？ | 正確答案排多前 |
| NDCG | 排名品質如何？ | 排第 1 比排第 5 貢獻更多 |


R@K 是最常見的，也最容易被誤讀。R@5 = 96.6% 代表 96.6% 的查詢，正確答案有出現在前 5 筆結果裡。它不問 LLM 有沒有看到這筆結果，不問 LLM 有沒有答對。


Retrieval 找到了，LLM 不一定答對；LLM 猜對了，不一定是靠 retrieval 找到的。這兩個指標可以同時反向——這就是為什麼只看 R@K 不夠，也為什麼 R@K 和 QA accuracy 不能直接放在一起比。


---


## 三個 Memory-Specific Benchmark 各測什麼場景？


除了 retrieval 指標，還有幾個專為 long-context memory 設計的 benchmark，各自測不同的使用場景。


**LongMemEval**


測試 AI 能不能記住長對話裡的具體資訊，分四個子任務：


- Single-hop recall：直接找回某個事實
- Multi-hop：需要組合多個記憶才能回答
- Temporal reasoning：記憶的時序，先發生的還是後發生的？
- Entity tracking：某個人或物的狀態隨對話演變


這四個子任務測的能力不同，系統在各子任務的強弱也不同，加總成單一數字後資訊會被稀釋。


**LoCoMo（Long Conversation Memory）**


測試多 session 對話的記憶一致性：跨 session 事實一致、偏好追蹤、關係理解。


mem0 V2 到 V3 在這個 benchmark 上從 71.4 跳到 91.6，+20 個百分點。背後的原因是 extraction 系統的強項正好對上了 LoCoMo 在測的東西——extraction 把偏好和事實正規化後，paraphrase 問題消失，跨 session 一致性自然高。


**Needle in a Haystack**


在超長 context 中找到一個特定事實。這個 benchmark 天然對 verbatim + BM25 有利，因為原文字詞完整保留，精確字詞命中率高。反過來，extraction 系統在 pipeline 中就可能把「針」丟掉——LLM 改寫過的 semantic 摘要不一定保留原始字詞。


---


## 設計決策決定哪個 Benchmark 強


這是這篇最重要的結論：系統在哪個 benchmark 強，不是調教出來的，是設計決策決定的。


  

Extraction 系統（mem0、deerflow）把記憶正規化，paraphrase 問題消失，所以在 LoCoMo 這種偏好追蹤類 benchmark 強。但 extraction pipeline 可能丟掉原始字詞，所以在 Needle in a Haystack 反而可能輸給 verbatim 系統。


Verbatim + BM25（mempalace、hermes L2）保留原文，精確字詞完整，所以在 Needle 和 R@K 類 benchmark 強。但跨 session 一致性沒有 extraction 好，因為同一件事用不同說法寫進去，會存成兩筆。


有 KG 和時間維度的系統（mempalace KG、OpenViking）在 LongMemEval 的 temporal reasoning 和 multi-hop 強，因為 KG 記錄了事件的先後關係和 entity 之間的連結，不只是 flat facts。


---


## 96.6% 和 93.4% 為什麼不能直接比？


回到開頭的問題。


mempalace 96.6% 是 LongMemEval 的 R@5——retrieval 層，找到了嗎？


mem0 V3 93.4% 是 QA accuracy——end-to-end，答對了嗎？


一個測的是 memory 系統有沒有把正確記憶找出來，一個測的是整個 pipeline（memory + LLM）有沒有答對問題。即使用同一個 benchmark 資料集，兩個指標測的層次不同，不能直接比大小。


更進一步：就算都是 QA accuracy，benchmark 的資料集不同，測的場景不同，數字也沒有可比性。LoCoMo 測多 session 偏好追蹤，LongMemEval 測長對話事實 recall，兩個都叫「memory benchmark」但問的是完全不同的問題。


---


## 選系統之前，先問你的 agent 在做什麼


沒有通用最強的 agent memory 系統。問題是：你的 agent 主要在做什麼？


| Agent 場景 | 最相關的 benchmark | 推薦方向 |
| --- | --- | --- |
| 記住用戶偏好、習慣 | LoCoMo | mem0、deerflow |
| 找回精確內容（程式碼、數字） | Needle in a Haystack, R@K | mempalace、hermes L2 |
| 跨 session 長期記憶 | LongMemEval temporal | mempalace KG、OpenViking |
| 多實體關係追蹤 | LongMemEval multi-hop | mem0 entity、agentmemory graph |


這個問題的答案，決定了哪個 benchmark 有意義，再決定選哪個系統。如果你還不確定 agent 主要在做什麼，那無論哪個 benchmark 數字都暫時沒有意義。


---


> 
**結語**：看 benchmark 數字之前，先問這個數字測的是什麼——如果場景對不上，96.6% 和 93.4% 都只是兩個不同的故事。

  
  
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

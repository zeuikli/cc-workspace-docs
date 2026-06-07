---
url: "https://warmwater.dev/blog/agent-memory-03-storage-production"
title: "Memory 03：Agent 記憶住在哪裡——Storage 選擇是部署假設"
date: 2026-05-14
category: Source Code
source: warmwater.dev
---

[
← Source Code ](/blog?tag=Source%20Code)  Source Code 
 
# Memory 03：Agent 記憶住在哪裡——Storage 選擇是部署假設
 
 2026-05-14 · — views  
  
  
選 SQLite 還是 PostgreSQL，表面上是技術決策，實際上是你在宣告這個 agent 為誰服務。


這個決定很早就發生了，而且很難換。


---


## Storage、Search、Deployment 為什麼是三個鎖在一起的決策？


8 個系統選了 5 種儲存格式，但不是隨機的——每一種格式背後都帶著特定的 search 能力和部署假設：


| 儲存格式 | 系統 | Search 能力 | 部署假設 |
| --- | --- | --- | --- |
| JSON 單檔 | deerflow | 全量注入，不搜 | 單一程序，本機 |
| Markdown + SQLite | hermes-agent | Markdown 全量 + SQLite FTS5 | single-user，本機 |
| SQLite + FTS5 | engram | BM25 keyword | single-user，本機 |
| ChromaDB + SQLite KG | mempalace | Semantic + graph | single-user，本機 |
| Vector DB + SQLite history | mem0 | Multi-signal hybrid | multi-user，遠端 DB |
| PostgreSQL + pgvector | letta | Semantic + archival | multi-user，managed service |
| iii KV（Rust） | agentmemory | Multi-signal hybrid | single-user，本機 |
| Rust AGFS 虛擬 FS | OpenViking | 層級展開 | single-user，本機 |


規律很清楚：選 SQLite 或 local file 的系統，都假設一個 user、一台機器、一個程序寫入。選 PostgreSQL 或遠端 Vector DB 的系統，從設計初期就預設了 stateless server + remote DB。


這三個面向不是獨立的選擇，是一個決策：


```
JSON / Markdown →  無 query 能力 →  local file，single-writer
SQLite FTS5 →  keyword search  →  single-writer（官方不支援 NFS/S3）
Vector DB（本機） →  semantic search →  單機，HNSW index 難搬遷
PostgreSQL →  完整 query →  multi-user，需要 server
```


選了哪個 search archetype，幾乎就決定了儲存格式。選了哪個儲存格式，幾乎就決定了能不能 multi-user。


---


## 各格式的 Trade-off：為什麼這些系統這樣選？


**JSON（deerflow）**


deerflow 把全部記憶存成一個 JSON，30 秒 debounce 後 LLM 直接改寫整個檔案，atomic rename 防止寫入中斷。


優點是零依賴、human-readable、可以 git 追蹤 memory 變化。代價是根本沒有 query——所以 deerflow 的 search archetype 就是「不搜，全量注入」。這不是限制，是設計的一致性：你選了 JSON，就選了全量注入。


**Markdown + SQLite（hermes-agent）**


hermes 用兩層儲存對應兩種記憶：L1 episodic 存 Markdown，L2 semantic 存 SQLite。Markdown 部分可以手動編輯、版本控制；SQLite 部分支援 FTS5 BM25。


這個設計讓 L1 記憶保持人類可讀，L2 記憶可以被精確搜尋。代價是 Markdown 的 concurrent write 靠 fcntl lock，SQLite 的分散式需要額外工具。


**SQLite + FTS5（engram）**


SQLite 在 single-user 場景的工程性價比最高：單檔 ACID，自帶 FTS5 BM25，零 server 依賴。engram 的 search 就直接跑 FTS5 query，write time 做 topic 萃取換 search time 的簡單。


天花板在：SQLite 是 single-writer，要做分散式需要 Litestream 或 Turso——但這時候問題不是工具，是你原本的設計假設已經不成立了。


**ChromaDB + SQLite KG（mempalace）**


mempalace 用 ChromaDB 做語意搜尋，SQLite 存 entity relationship graph，兩個信號 fusion 後返回結果。這是 Memory 02 裡 multi-signal hybrid 的一種。


代價在 ops：ChromaDB 有 index bloat 問題，HNSW index 無法直接搬遷，需要 export → re-index。你在本機跑沒問題，要遷移環境或做 backup restore 時才會發現這個代價。


**PostgreSQL + pgvector（letta）**


letta 的設計假設從一開始就是 stateless API server + PostgreSQL 作為 source of truth。pgvector 讓向量索引和關聯 query 在同一個 DB 完成，不需要維護兩套系統。


直接對接 Supabase 或 Aurora，有 managed service 可用。對 single-user 場景是 overkill——為一個人的記憶跑 Postgres instance，ops 成本不值得。


---


## 為什麼在 Kubernetes 上掛 NFS 或 S3 會讓 Memory 靜默損壞？


Kubernetes 上常見的錯誤：把 single-user 設計的系統（deerflow、hermes、engram）掛上 NFS 或 S3，試圖讓它支援多用戶。


問題不在 mount 方式，在設計假設：


**NFS**：`fcntl` lock 在 NFS 上是 advisory only，不是強制。SQLite WAL mode 官方明確不支援 NFS。hermes 的 Markdown lock 和 engram 的 SQLite 都會靜默失敗——不會噴錯，資料就慢慢壞掉。


**S3 FUSE（s3fs / goofys）**：deerflow 的 atomic rename 不保證（S3 的 rename 是 copy + delete，不是原子操作）。SQLite WAL 會 corrupt。


正確做法不是換 mount 方式，是換系統。需要 shared storage，就代表部署假設已經從 single-user 變成 multi-user，該用 mem0 或 letta。這兩個系統設計本來就是 stateless + remote DB，不依賴 POSIX 語意。


---


## 儲存格式是第一個決策，而不是最後一個


很多工程師在選 agent memory 系統時，先看 search 功能，再看 API 設計，storage 留到最後。


但實際上順序是反過來的：storage 選擇決定了 search 能力的上限，search 能力決定了 write 策略的設計空間，write 策略決定了 agent 的 context quality。


deerflow 選了 JSON，所以只能全量注入，所以 LLM 必須一次看到所有記憶。engram 選了 SQLite FTS5，所以只有 keyword search，所以 write time 必須做 topic 萃取。letta 選了 PostgreSQL，所以可以 multi-user，所以 agent 可以是無狀態的 API service。


每一條路都是自洽的。問題是選錯路之後，中途想換，幾乎要從頭來過。


  

---


> 
**結語**：storage 選型的時機比你想的早——在你決定這個 agent 是給一個人用還是給一個平台用的那一刻，儲存格式就已經定了。

  
  
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

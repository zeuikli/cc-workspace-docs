---
url: "https://warmwater.dev/blog/llm-vector-db"
title: "向量資料庫完全指南：為什麼 LLM 時代需要 Vector DB？"
date: 2025-12-31
category: System Design
source: warmwater.dev
---

[
← System Design ](/blog?tag=System%20Design)  System Design  
#  向量資料庫完全指南：為什麼 LLM 時代需要 Vector DB？ 
  2025-12-31 · — views      

> **適合讀者**：想了解 Vector DB 核心概念的開發者，不需要深入演算法細節，但想知道「為什麼這樣設計」

---


## 問題的起點：為什麼傳統資料庫不夠用？


【Context】
當你問 ChatGPT「什麼是 LangChain？」，它能給出流暢的回答。但當你問「我們公司上週的會議記錄提到什麼？」，它一無所知。這就是 LLM 的根本限制：**它只知道訓練時學過的東西**。


【Real-World Problem】


要讓 LLM 回答「你的資料」，最直覺的做法是：

```
使用者問題 → 搜尋相關文件 → 把文件塞給 LLM → LLM 回答

```


但問題來了：**怎麼「搜尋」？**


【Traditional Search Limitations】


**關鍵字搜尋的困境**：


使用者問的文件裡寫的關鍵字搜尋結果「如何提升效能？」「優化系統速度的方法」❌ 找不到「Python 怎麼處理錯誤？」「Exception handling in Python」❌ 找不到「推薦系統原理」「Collaborative filtering 演算法」❌ 找不到


關鍵字搜尋要求「字面完全匹配」，但人類表達同一件事的方式千變萬化。


【Core Insight】


我們需要的是「語意搜尋」——理解「意思相近」，而不只是「字面相同」。


這就是 Vector Database 存在的理由。

---


## 向量搜尋的核心直覺


【Context】
Vector DB 的核心概念其實很簡單：**把文字變成數字，用數學找相似**。


【How It Works】


**Step 1: 把文字變成向量（Embedding）**

```
「如何提升效能？」 → [0.23, -0.45, 0.67, ..., 0.12]  (768 維)
「優化系統速度」   → [0.21, -0.42, 0.65, ..., 0.15]  (768 維)
「今天天氣很好」   → [-0.56, 0.89, -0.12, ..., 0.34]  (768 維)

```


Embedding 模型（如 OpenAI、Cohere、BGE）會把語意相近的文字，映射到空間中相近的位置。


**Step 2: 用距離衡量相似度**

```
「提升效能」與「優化速度」的距離 = 0.05  → 很近 → 語意相似 ✅
「提升效能」與「今天天氣」的距離 = 0.89  → 很遠 → 語意不同 ❌

```


【Visual Intuition】


想像一個高維空間：

```
                    ● 「優化系統速度」
                   /
    ● 「提升效能」
                   
                   
                   
    ● 「今天天氣很好」（很遠的地方）

```


語意相近的概念，在這個空間裡會「聚在一起」。


【Why This Matters】


這解決了關鍵字搜尋的根本問題：


使用者問的Embedding 會找到原因「如何提升效能？」「優化系統速度的方法」語意相近 ✅「Python 錯誤處理」「Exception handling」概念相同 ✅「推薦系統」「Collaborative filtering」同一領域 ✅

---


## 為什麼需要「近似」搜尋？ANN 的必要性


【Context】
理論上，找「最相似的向量」很簡單：計算 query 和每一個向量的距離，排序，取前 K 個。但實務上，這是災難。


【The Scale Problem】


**暴力搜尋的成本**：

```
資料量：10,000,000 個向量
維度：768（常見 embedding 維度）

每次查詢 = 10M × 768 次浮點運算
         = 約 7.68 billion 次運算
         = 延遲爆炸 💥

```


當你的知識庫有 1000 萬筆文件，每次搜尋都要算 76 億次——這在 Production 環境完全不可行。


【The Solution: Approximate Nearest Neighbor (ANN)】


**ANN 的核心思想**：


> 用「犧牲一點點準確率」換取「巨大的效能提升」


不追求找到「絕對最近的 K 個」，而是找到「夠近的 K 個」。


【Why Approximation Works for LLM】


這裡有一個關鍵洞察，很多人忽略：


**LLM + RAG 天生就有容錯性**


- 


**Query embedding 本身就不是精確的**


- 同一個問題換個說法，embedding 就不同

- 「絕對最近」本來就是偽命題


- 


**文件 chunks 有語意重疊**


- 找到第 2 相近的 chunk，通常也包含答案

- 不需要「那唯一正確的一條」


- 


**LLM 只需要「一組相關 context」**


- 不是要最精確的那一條

- 而是要足夠的上下文


**實際影響**：


搜尋方式Recall延遲暴力搜尋100%秒級（不可用）ANN 搜尋95-99%毫秒級 ✅


Recall 從 100% 降到 95%，但延遲從秒級降到毫秒級——這個 trade-off 在 LLM 場景完全可以接受。

---


## HNSW：目前最成功的 ANN 演算法


【Context】
ANN 有很多實現方式，但目前主流 Vector DB 幾乎都選擇了同一個演算法：**HNSW（Hierarchical Navigable Small World）**。


【ANN Algorithm Families】


類型代表演算法特性Tree-basedKD-Tree低維度 OK，高維度崩潰Hash-basedLSH速度快，但準確率低QuantizationIVF / PQ超大規模使用**Graph-based****HNSW**⭐ 主流選擇：高準確、低延遲


Qdrant、Weaviate、Milvus、Pinecone、OpenSearch——幾乎都以 HNSW 為核心。


【What is HNSW?】


**全名**：Hierarchical Navigable Small World Graph


三個關鍵詞：


- **Graph**：用圖結構連接向量

- **Small World**：任意兩點之間，只需要少數幾步

- **Hierarchical**：多層結構，從粗到細


【Small World Intuition】


**類比：城市的交通網路**

```
想像你要從台北到高雄：

❌ 走一般道路：經過無數個路口，慢
✅ 上高速公路：幾個交流道就到，快

Small World 的特性：
- 大多數節點只連接「鄰居」（一般道路）
- 少數節點有「遠距離捷徑」（高速公路）
- 結果：任意兩點之間只需要「少數幾步」

```


【HNSW Layer Structure】


HNSW 的精髓在於「多層圖結構」：

```
Layer 3 (最稀疏)    ●─────────────────●
                     \               /
Layer 2              ●───────●───────●
                       \     |     /
Layer 1              ●───●───●───●───●
                       \ | / | \ | /
Layer 0 (最密集)    ●─●─●─●─●─●─●─●─●─●

```


**設計邏輯**：


- **Layer 0**：包含所有向量，連接最密集

- **越往上**：節點越少，連接越稀疏

- **最上層**：像「高速公路」，快速定位大方向


【Search Process】


**查詢流程**：

```
Query: 找「如何提升效能」的相關文件

Step 1: 從最上層開始
        └→ 快速定位「大概在哪個區域」

Step 2: 往下掉一層
        └→ 用上一層的結果當起點
        └→ 在更密集的圖裡找更近的點

Step 3: 重複直到 Layer 0
        └→ 在最完整的圖裡做最後精煉

Step 4: 返回 Top-K 結果

```


**重點**：


- 不是「全域搜尋」

- 而是「貪婪式往更近的方向走」

- 像是先搭高鐵到高雄，再轉捷運到目的地


【Why HNSW is Fast】


**對比暴力搜尋**：


方式需要計算的距離次數10M 向量時的延遲暴力搜尋10,000,000 次秒級HNSW約 100-1000 次毫秒級


HNSW 只需要「走過」的節點計算距離，而不是全部。

---


【Memory Characteristics】


**HNSW 的記憶體特性**：

```
HNSW = Memory-Heavy, Low-Latency

原因：
├─ Graph 結構需要儲存大量 pointer
├─ Adjacency list 佔用空間
├─ 不適合 cold storage
└─ 必須常駐記憶體才能發揮效能

結論：
├─ 適合：延遲敏感、資料量中等
└─ 不適合：超大規模、預算有限

```


---


## 主流 Vector DB 比較


【Context】
市面上有許多 Vector DB 選擇，各有優劣。以下是根據不同場景的選型建議。


【Comparison Matrix】


Vector DB類型核心優勢適用場景**Pinecone**全託管零運維、開箱即用快速上線、不想管 infra**Qdrant**自託管/雲效能優異、Rust 實作高效能需求、技術團隊強**Weaviate**自託管/雲GraphQL API、模組化需要靈活查詢、整合複雜**Milvus**自託管超大規模、GPU 支援億級向量、企業級部署**Chroma**嵌入式輕量、易上手本地開發、POC、小專案**pgvector**PostgreSQL 擴充整合現有 PG已有 PostgreSQL、不想加新元件


【Selection Guide】


**依團隊規模選擇**：

```
個人開發者 / Side Project：
└→ Chroma（本地開發）
└→ Pinecone Free Tier（快速上線）

新創團隊 / 小型專案：
└→ Qdrant Cloud / Pinecone
└→ 優先考慮「運維成本低」

中型團隊 / Production：
└→ Qdrant / Weaviate（自託管可控）
└→ 或 Pinecone（全託管省事）

大型企業 / 億級規模：
└→ Milvus（分散式、GPU 加速）
└→ 需要專門的 infra 團隊

```


**依使用場景選擇**：

```
RAG / Chatbot：
└→ 任何主流 Vector DB 都可以
└→ 優先考慮易用性和生態整合

推薦系統：
└→ 需要高 QPS：Milvus / Qdrant
└→ 需要低延遲：HNSW-based 方案

圖片/音訊搜尋：
└→ 高維向量：Milvus（PQ 壓縮）
└→ 需要 GPU：Milvus

已有 PostgreSQL：
└→ 先試 pgvector
└→ 規模大再考慮專用 Vector DB

```


---


## 實際開發的關鍵考量


【Context】
選好 Vector DB 只是開始，實際開發中還有許多「踩坑點」需要注意。


【Key Considerations】

### 1. Embedding 模型比 Vector DB 更重要


**常見誤區**：
> 「我用了最好的 Vector DB，為什麼搜尋結果還是不準？」


**真相**：


- 搜尋品質 80% 取決於 Embedding 模型

- Vector DB 只是「儲存和查詢」

- 垃圾進，垃圾出


**建議**：

```
優先順序：
1. 選對 Embedding 模型（OpenAI, Cohere, BGE）
2. 做好資料前處理（清洗、分段）
3. 最後才是選 Vector DB

```


### 2. Chunking 策略影響巨大


**問題**：


- 文件要切成多大的 chunk？

- 切太小：失去上下文

- 切太大：語意混雜


**實務建議**：

```
一般文件：
├─ Chunk size: 500-1000 tokens
├─ Overlap: 10-20%
└─ 按段落或章節切分

程式碼：
├─ 按 function / class 切分
└─ 保留完整邏輯單元

對話記錄：
├─ 按對話回合切分
└─ 保留 speaker 資訊

```


### 3. Metadata 是被低估的武器


**問題**：
純向量搜尋有時候不夠精確


**解法**：
結合 Metadata filtering

```
場景：搜尋「2024 年的財報分析」

純向量搜尋：
└→ 可能返回 2020 年的相關內容 ❌

向量 + Metadata：
└→ 先過濾 year = 2024
└→ 再做向量相似度搜尋 ✅

```


### 4. 不要忽略 Reranking


**問題**：
Vector 搜尋的 Top-10 不一定是最相關的


**解法**：
兩階段檢索

```
Stage 1: Vector Search（快，粗篩）
         └→ 取 Top-50

Stage 2: Reranker（慢，精排）
         └→ 用 Cross-Encoder 重新排序
         └→ 返回 Top-10

```


**效果**：


- Recall 和 Precision 都顯著提升

- 特別適合高品質需求場景


---


## 未來趨勢


【Context】
Vector DB 領域正在快速演進，有幾個值得關注的趨勢。


【Emerging Trends】

### 1. Hybrid Search 成為標配


```
現在：Vector Search 或 Keyword Search 二選一
未來：兩者結合成為預設

Hybrid Search = Vector Similarity + BM25 Keyword
             = 語意理解 + 精確匹配

```


### 2. 多模態向量


```
現在：主要處理文字
未來：圖片、音訊、影片統一向量空間

應用：
├─ 用文字搜圖片
├─ 用圖片搜影片
└─ 跨模態推薦

```


### 3. 與傳統資料庫融合


```
現在：Vector DB 是獨立元件
未來：PostgreSQL / MySQL 原生支援向量

趨勢：
├─ pgvector 快速成熟
├─ 各大雲端 DB 加入向量功能
└─ 減少架構複雜度

```


### 4. 端側向量搜尋


```
現在：都在雲端
未來：手機/邊緣裝置本地向量搜尋

應用：
├─ 離線語意搜尋
├─ 隱私敏感場景
└─ 低延遲需求

```


---


## 總結：一句話理解 Vector DB


【Core Takeaways】

### ANN vs HNSW


```
ANN 是「問題類型」：允許近似的最近鄰搜尋
HNSW 是「解法」：目前最成功的實現方式

或者更工程一點：

ANN 定義了「我們可以不追求完美」
HNSW 則把這件事做到「又快又準又穩」

```


### 選型決策樹


```
你的資料規模？

├─  10M 向量
   └→ Milvus（分散式架構）

```


### 最重要的一件事


> **Embedding 品質 > Chunking 策略 > Vector DB 選擇**


Vector DB 只是工具，真正決定搜尋品質的是：


- 你的 Embedding 模型是否夠好

- 你的資料是否切分得當

- 你是否善用 Metadata 和 Reranking


選對工具很重要，但更重要的是理解整個 pipeline。

---


**官方文檔**：


- [Pinecone Documentation](https://docs.pinecone.io/)

- [Qdrant Documentation](https://qdrant.tech/documentation/)

- [Weaviate Documentation](https://weaviate.io/developers/weaviate)

- [Milvus Documentation](https://milvus.io/docs)

- [Chroma Documentation](https://docs.trychroma.com/)


---


## Tags


`#VectorDB` `#ANN` `#HNSW` `#Embedding` `#RAG` `#LLM` `#SemanticSearch` `#Pinecone` `#Qdrant` `#Milvus`

## 延伸閱讀


- [RAG 典範轉移：從向量檢索到結構化檢索](/blog/rag) — Vector DB 是 RAG 的基礎，但這篇告訴你它什麼時候不夠用

- [RAG System 完整指南：從原理到實踐](/blog/rag-system) — Vector DB 是 RAG pipeline 的一環：embedding 選型、chunking 策略的完整設計

- [LLM Cache 策略：從 Prompt Cache 到 Semantic Cache](/blog/llm-cache-prompt-cache-semantic-cache) — Vector DB 的另一個用途：semantic cache 用相同的 embedding 機制省掉重複查詢
     [ System Design ](/blog?tag=System%20Design)[ RAG ](/blog?tag=RAG)  
### 
相關文章

[Implement用 RPG 架構評估 SRE Agent：Kube Arena 設計紀錄2026-05-28](/blog/kube-arena)[System DesignMCP、CLI、還是直呼 API？先看工具長什麼樣2026-05-23](/blog/mcp-cli-api-integration)[System DesignAgent 要怎麼進化？六個系統的 Self-Improvement 機制比較2026-05-22](/blog/agent-self-improvement-design-comparison)

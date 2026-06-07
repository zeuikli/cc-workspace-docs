---
url: "https://warmwater.dev/blog/llm-cache-prompt-cache-semantic-cache"
title: "LLM Cache 策略：從 Prompt Cache 到 Semantic Cache"
date: 2026-01-01
category: System Design
source: warmwater.dev
---

LLM Cache 策略：從 Prompt Cache 到 Semantic Cache
============================================

2026-01-01 · — views 

> **核心觀點**：Prompt Cache 幫你省 token，Semantic Cache 幫你省思考

* * *

問題的起點：真正的成本問題不是 Token
---------------------

【Context】 你的 LLM 系統每天處理上萬次請求。Prompt 已經精簡到不能再短，Prefix 也固定了，但成本還是居高不下。問題出在哪？

【Real-World Observation】

一個典型的 LLM 應用成本結構：

    每日請求：50,000 次
    平均 token/request：2,000
    每月 token 消耗：3B tokens
    每月成本：$15,000+
    

工程師的直覺反應：

    Step 1: 縮短 prompt → 效果有限
    Step 2: 選擇更便宜的模型 → 品質下降
    Step 3: 限制使用量 → 用戶抱怨
    

這些都是治標不治本。

【Core Insight】

真正的問題不在模型，而是：

> **系統一直讓模型「想一樣的事」**

當 10,000 個用戶問「如何重設密碼？」，你的 LLM 就要「思考」10,000 次——即使答案完全一樣。

這就是 Cache 策略要解決的問題。

* * *

Cache 的兩個層次
-----------

【Context】 LLM Cache 不是單一技術，而是分層防線。理解這個分層結構，是設計高效 LLM 系統的關鍵。

【Architecture Overview】

    Request
       ↓
    ┌─────────────────────────────┐
    │  Prompt Cache (Syntax)      │  ← 字串完全相同才命中
    └─────────────────────────────┘
       ↓
    ┌─────────────────────────────┐
    │  Semantic Cache (Meaning)   │  ← 意思相近就命中
    └─────────────────────────────┘
       ↓
    ┌─────────────────────────────┐
    │  LLM API                    │  ← 只有真正需要時才呼叫
    └─────────────────────────────┘
    

**關鍵理解**：這兩層不是互斥的，而是疊加的。

【Why Two Layers?】

| 層次 | 判斷依據 | 命中條件 | 命中率 |
|------|---------|--------|--------|
| Prompt Cache | 字串 | 完全相同 | 低 |
| Semantic Cache | 語意 | 意思相近 | 高 |

Prompt Cache 是第一道防線，快速攔截「完全相同」的請求。

Semantic Cache 是第二道防線，攔截「意思相同但表達不同」的請求。

* * *

第一層防線：Prompt Cache
------------------

【Context】 Prompt Cache 是最基礎的 cache 策略：當 prompt 字串完全相同時，直接返回之前的結果，避免重複計算。

【What is Prompt Cache?】

**一句話定義**：

> Prompt Cache 是在「字串完全相同」的前提下，避免重算 prompt token

【Two Types of Prompt Cache】

### Type 1: Prefix Cache（Server-side）

**運作方式**：

*   OpenAI、Anthropic 等 API 提供商內建
*   在 byte-level 進行匹配
*   對開發者幾乎透明——你看不到，但它存在

**適用場景**：

    固定的 System Prompt
       ↓
    可變的 User Input
    

當你的 system prompt 很長且固定時，API 會自動 cache 這個 prefix，只計算變動的部分。

**實際效益**：

*   長 system prompt 的 token 不會重複計費
*   Tool / Function schema 只計算一次
*   Output format 定義只計算一次

### Type 2: Client-side Prompt Cache

**運作方式**：

    hash(完整 prompt) → 查詢 cache → 命中則返回
    

**特性**：

*   完全由你控制
*   需要 prompt 完全相同才命中
*   適合內部工具或固定流程

【What Prompt Cache Can and Cannot Solve】

**✅ 能解決**：

*   長 system prompt 的重複計算
*   Tool / function schema 的重複處理
*   Output format 定義的重複消耗
*   Policy / instruction 的重複解析

**❌ 無法解決**：

| 情境 | Prompt Cache |
|------|--------------|
| User input 變化 | ❌ Miss |
| Query paraphrase | ❌ Miss |
| 結構一樣、語意一樣、字不同 | ❌ Miss |

【The Ceiling of Prompt Cache】

這裡有一個關鍵限制：

> **Prompt Cache 解決的是 Syntax，不是 Semantics**

三個語意完全相同的請求：

    請求 A：「Summarize the following text」
    請求 B：「Please give me a short summary」
    請求 C：「TL;DR」
    

對 Prompt Cache 而言，這是三個完全不同的請求——三次 miss，三次 LLM 呼叫，三倍成本。

這就是為什麼 Prompt Cache 不夠。

* * *

為什麼 Prompt Cache 不夠？
--------------------

【Context】 在真實世界的 LLM 應用中，input 的變異性遠超我們的想像。

【Real-World Input Variability】

**來源 1：使用者改寫**

    同一個問題的不同表達：
    
    「如何重設密碼？」
    「忘記密碼怎麼辦」
    「Password reset」
    「密碼忘了」
    

每一個都會 cache miss。

**來源 2：LLM Agent 加 context**

    原始問題：「什麼是 LangChain？」
    
    Agent 改寫後：
    「Based on the user's previous questions about Python libraries,
     explain what LangChain is and how it relates to LLM development.
     User query: 什麼是 LangChain？」
    

加了 context 後，和之前的 prompt 完全不同——又是 miss。

**來源 3：Metadata 不穩定**

    請求 1：timestamp=2024-01-01T10:00:00
    請求 2：timestamp=2024-01-01T10:00:01
    

只差一秒，但對 Prompt Cache 而言是完全不同的字串。

【The Real Cost】

**問題的本質**：

> 我們不是在重複產生答案，而是在重複「判斷要怎麼回答」

當 LLM 收到「如何重設密碼？」和「忘記密碼怎麼辦」，它需要：

1.  理解問題的意圖
2.  檢索相關知識
3.  組織回答結構
4.  生成回應

這個「思考過程」完全相同，但因為字串不同，LLM 必須重新執行一遍。

**這就是浪費的根源。**

* * *

第二層防線：Semantic Cache
--------------------

【Context】 如果 Prompt Cache 是「字串完全相同才命中」，那 Semantic Cache 就是「意思相近就命中」。

【What is Semantic Cache?】

**一句話定義**：

> Semantic Cache 用 embedding 判斷「意思像不像」，來決定要不要 reuse LLM 的結果

【How It Works】

    新請求進來
        ↓
    生成 embedding
        ↓
    在 cache 中搜尋相似的 embedding
        ↓
    相似度 > threshold?
        ├─ Yes → 返回 cached response
        └─ No → 呼叫 LLM，存入 cache
    

【Core Comparison】

| 面向 | Prompt Cache | Semantic Cache |
|------|--------------|----------------|
| **判斷依據** | 字串完全相同 | 語意相似度 |
| **使用模型** | 無 / Hash | Embedding Model |
| **計算成本** | 極低 | 低（embedding 便宜） |
| **命中率** | 低 | 高 |
| **風險** | 幾乎無 | 需要設計 threshold |

【Why Semantic Cache Fits LLM Systems】

**理由 1：LLM 本來就是語意模型**

LLM 的核心能力就是理解語意。用語意來判斷 cache，和 LLM 的工作方式一致。

**理由 2：Embedding 是 LLM 的副產品**

大多數 LLM API 都提供 embedding 功能。這不是額外負擔，而是現有能力的延伸。

**理由 3：大多數產品問題是「語意重複」**

真實世界中，用戶問的問題有高度重複性——只是表達方式不同。

    客服場景：
    ├─ 80% 的問題集中在 20 種類型
    ├─ 每種類型有 10+ 種表達方式
    └─ Semantic Cache 可以一次覆蓋所有變體
    

【Real-World Impact】

**Before Semantic Cache**：

    「如何重設密碼？」→ LLM 呼叫
    「忘記密碼怎麼辦」→ LLM 呼叫
    「Password reset」→ LLM 呼叫
    「密碼忘了」→ LLM 呼叫
    
    4 次 LLM 呼叫，4 倍成本
    

**After Semantic Cache**：

    「如何重設密碼？」→ LLM 呼叫 → 存入 cache
    「忘記密碼怎麼辦」→ 語意相似 → cache hit
    「Password reset」→ 語意相似 → cache hit
    「密碼忘了」→ 語意相似 → cache hit
    
    1 次 LLM 呼叫，1 倍成本
    

**成本降低 75%**，而且回應速度更快（cache hit 是毫秒級）。

* * *

Semantic Cache 的核心設計
--------------------

【Context】 Semantic Cache 的效果取決於設計。以下是幾個關鍵決策點。

【Key Design Decisions】

### 1\. Embedding Model 選擇

**考量因素**：

| 因素 | 權衡 |
|------|------|
| 維度 | 高維度 = 更精確，但更慢、更貴 |
| 多語言 | 是否需要支援多語言查詢？ |
| 領域 | 通用 vs 領域專用 |

**常見選擇**：

*   **通用場景**：OpenAI text-embedding-3-small
*   **多語言**：Cohere embed-multilingual
*   **成本敏感**：BGE / E5 開源模型

### 2\. Similarity Threshold

**核心問題**：多相似才算「夠相似」？

    Threshold 太低（如 0.7）：
    ├─ 命中率高
    ├─ 但可能返回不相關的答案
    └─ 用戶體驗差
    
    Threshold 太高（如 0.98）：
    ├─ 精確度高
    ├─ 但命中率極低
    └─ Cache 形同虛設
    

**實務建議**：

| 場景 | 建議 Threshold |
|------|----------------|
| 客服 FAQ | 0.85 - 0.90 |
| 技術文檔 | 0.90 - 0.95 |
| 創意寫作 | 不建議使用 cache |

### 3\. Cache Entry 設計

**需要存什麼？**

    Cache Entry:
    ├─ query_embedding: 原始問題的向量
    ├─ query_text: 原始問題文字（debug 用）
    ├─ response: LLM 的回應
    ├─ metadata:
    │  ├─ created_at
    │  ├─ model_version
    │  ├─ hit_count
    │  └─ category
    └─ ttl: 過期時間
    

### 4\. TTL 與版本控制

**為什麼需要 TTL？**

*   知識會過時
*   模型會升級
*   業務規則會變更

**策略**：

    短 TTL（小時級）：
    ├─ 即時性資料
    ├─ 價格、庫存
    └─ 新聞摘要
    
    中 TTL（天級）：
    ├─ 產品說明
    ├─ FAQ 答案
    └─ 操作指南
    
    長 TTL（週/月級）：
    ├─ 基礎概念解釋
    ├─ 不變的定義
    └─ 歷史資料
    

**版本控制**：

當模型升級時，舊的 cache 可能不再適用。建議在 cache key 中包含 model version：

    cache_key = hash(embedding + model_version)
    

* * *

分層架構：兩層 Cache 如何協作
------------------

【Context】 Prompt Cache 和 Semantic Cache 不是互斥的，而是分層疊加的。

【Layered Architecture】

    Request: 「如何重設密碼？」
                  ↓
    ┌────────────────────────────────────────┐
    │  Layer 1: Prompt Cache (Syntax)        │
    │                                        │
    │  hash("如何重設密碼？") → 查詢         │
    │  ├─ Hit → 返回（極速）                 │
    │  └─ Miss → 往下                        │
    └────────────────────────────────────────┘
                  ↓
    ┌────────────────────────────────────────┐
    │  Layer 2: Semantic Cache (Meaning)     │
    │                                        │
    │  embed("如何重設密碼？") → 相似度搜尋  │
    │  找到相似：「忘記密碼怎麼辦」(0.92)    │
    │  ├─ > threshold → 返回 cached 答案     │
    │  └─ < threshold → 往下                 │
    └────────────────────────────────────────┘
                  ↓
    ┌────────────────────────────────────────┐
    │  Layer 3: LLM API                      │
    │                                        │
    │  呼叫 LLM → 生成答案                   │
    │  → 存入 Semantic Cache                 │
    │  → 存入 Prompt Cache（如果適用）       │
    └────────────────────────────────────────┘
    

【Why This Order?】

**Prompt Cache 在前**：

*   計算成本最低（只需 hash）
*   速度最快（純字串比對）
*   完全精確（零風險）

**Semantic Cache 在後**：

*   需要計算 embedding（成本較高）
*   需要相似度搜尋（速度稍慢）
*   有 threshold 風險（需要設計）

**LLM 最後**：

*   成本最高
*   速度最慢
*   只處理真正的「新問題」

【Real-World Metrics】

一個設計良好的分層 cache 系統：

    總請求：100,000 / day
    
    Prompt Cache Hit:     15%  → 省 15,000 次 LLM 呼叫
    Semantic Cache Hit:   60%  → 省 60,000 次 LLM 呼叫
    LLM API 呼叫:         25%  → 只需 25,000 次
    
    成本降低：75%
    平均延遲降低：80%（cache hit 是毫秒級）
    

* * *

常見誤區
----

【Context】 在實作 LLM Cache 時，有幾個常見的思維陷阱需要避免。

【Misconceptions】

### ❌ 誤區 1：只有 Prompt Cache 就夠了

**錯誤思維**：

> 「我們的 prompt 很固定，Prompt Cache 應該能解決大部分問題。」

**現實**：

*   低估了 input variability
*   用戶表達方式千變萬化
*   Agent 會動態修改 prompt
*   Metadata 會造成字串變化

**正確理解**： Prompt Cache 命中率通常只有 10-20%。對於用戶直接輸入的場景，Semantic Cache 才是主力。

### ❌ 誤區 2：Semantic Cache 很危險

**錯誤思維**：

> 「語意相似不代表問題一樣，返回錯誤答案會造成嚴重後果。」

**現實**：

*   問題不在 cache，而在沒有 guardrail
*   合理的 threshold 設計可以控制風險
*   可以加上「confidence score」讓用戶驗證

**正確做法**：

    Semantic Cache + Guardrails:
    ├─ 設定合理的 similarity threshold
    ├─ 對 high-stakes 場景降低 threshold 或禁用
    ├─ 返回結果時標註「來自 cache」
    └─ 提供用戶反饋機制
    

### ❌ 誤區 3：Cache 越多越好

**錯誤思維**：

> 「把所有東西都 cache 起來，命中率就會最高。」

**現實**：

*   Cache 會過時（知識、政策會變）
*   Cache 會膨脹（儲存成本）
*   Cache 會降低精確度（太多相似項目）

**正確做法**：

    Cache 策略 = 設計問題，不是堆資源
    
    需要考慮：
    ├─ 什麼值得 cache？（高頻、穩定的內容）
    ├─ 什麼不該 cache？（即時數據、個人化內容）
    ├─ 何時清除？（TTL、版本升級）
    └─ 如何監控？（命中率、準確率）
    

### ❌ 誤區 4：一個 Threshold 適用所有場景

**錯誤思維**：

> 「設定 0.9 的 threshold，所有問題都用這個。」

**現實**： 不同場景需要不同的精確度：

| 場景 | 風險 | 建議 Threshold |
|------|------|----------------|
| 閒聊 | 低 | 0.80 |
| FAQ | 中 | 0.88 |
| 技術支援 | 中高 | 0.92 |
| 醫療/法律 | 高 | 不建議 cache |

**正確做法**： 根據問題類型動態調整 threshold，或針對高風險場景禁用 cache。

* * *

什麼情況該用哪一種？
----------

【Context】 選擇正確的 cache 策略，需要根據場景特性來決定。

【Decision Matrix】

| 情境 | Prompt Cache | Semantic Cache | 說明 |
|------|--------------|----------------|------|
| 固定 System Prompt | ✅ | ❌ | 字串固定，Prompt Cache 足夠 |
| User Query | ❌ | ✅ | 表達多變，需要語意匹配 |
| SOP 說明 | ⚠️ | ✅ | 問法多樣，語意相同 |
| 即時數據（價格、庫存） | ❌ | ❌ | 不應 cache |
| 個人化內容 | ❌ | ❌ | 每個用戶不同，無法共享 |
| FAQ 回答 | ⚠️ | ✅ | 高頻、穩定，最適合 Semantic Cache |
| 創意寫作 | ❌ | ❌ | 每次應該不同 |
| 翻譯 | ⚠️ | ✅ | 同一句話的翻譯應該一致 |

【Decision Tree】

    你的 input 是否固定？
        │
        ├─ Yes → Prompt Cache 足夠
        │
        └─ No → 問題是否有「標準答案」？
                    │
                    ├─ Yes → Semantic Cache 適用
                    │        └─ 根據風險設定 threshold
                    │
                    └─ No → 不適合 cache
                            └─ 即時數據、創意內容、個人化
    

* * *

實作考量
----

【Context】 從概念到生產，還有幾個實務問題需要解決。

【Production Considerations】

### 1\. Cache 儲存選擇

| 選項 | 適用場景 | 特性 |
|------|---------|------|
| **Redis** | 中小規模 | 快速、簡單、適合 Prompt Cache |
| **Vector DB** | 大規模 Semantic Cache | Pinecone / Qdrant / Milvus |
| **Hybrid** | 生產系統 | Redis + Vector DB 組合 |

### 2\. Embedding 計算成本

**常見擔憂**：

> 「每個請求都要算 embedding，成本會不會很高？」

**現實**：

    OpenAI text-embedding-3-small:
    ├─ $0.00002 / 1K tokens
    └─ 相比 GPT-4o 的 $0.0025 / 1K tokens，便宜 125 倍
    
    一個 100 token 的 query：
    ├─ Embedding 成本：$0.000002
    ├─ GPT-4o 成本：$0.00025
    └─ 差距：125x
    

即使每個請求都計算 embedding，只要能 hit 一次 Semantic Cache，就省回來了。

### 3\. Cache Invalidation

**什麼時候需要清除 cache？**

    觸發清除的事件：
    ├─ 知識庫更新
    ├─ 模型版本升級
    ├─ 業務規則變更
    ├─ 發現錯誤答案
    └─ 定期 TTL 過期
    

**策略**：

    Versioned Cache Key:
    cache_key = hash(embedding + model_version + knowledge_version)
    
    當任一版本變更時，自動 invalidate 舊 cache
    

### 4\. 監控指標

**必須追蹤的 metrics**：

| 指標 | 說明 | 健康範圍 |
|------|------|---------|
| Prompt Cache Hit Rate | 字串完全匹配命中率 | 10-30% |
| Semantic Cache Hit Rate | 語意匹配命中率 | 40-70% |
| Average Similarity Score | cache hit 時的相似度 | > threshold |
| False Positive Rate | 用戶反饋「答案不對」的比率 | < 5% |
| Cache Size | 儲存空間使用 | 設定上限 |
| Cache Latency | cache 查詢時間 | < 50ms |

* * *

總結：兩種 Cache，兩種思維
----------------

【Context】 Prompt Cache 和 Semantic Cache 代表了兩種不同的思維方式。

【Core Insight】

    Prompt Cache：「字一樣，答案就一樣」
    Semantic Cache：「意思一樣，答案就一樣」
    

這不只是技術選擇，更是對「什麼是重複」的理解差異。

【Summary Comparison】

| 維度 | Prompt Cache | Semantic Cache |
|------|--------------|----------------|
| **思維** | 語法層面 | 語意層面 |
| **判斷** | 字串相同 | 意思相近 |
| **成本** | 幾乎為零 | 極低（embedding） |
| **命中率** | 低（10-20%） | 高（40-70%） |
| **風險** | 無 | 需設計 threshold |
| **適用** | 固定 prompt | 變動 input |

【The Right Mental Model】

    不是選擇哪一個，而是如何疊加：
    
    Request
       ↓
    Prompt Cache    ← 快速攔截「完全相同」
       ↓
    Semantic Cache  ← 攔截「意思相同」
       ↓
    LLM API         ← 只處理「真正新的問題」
    

【Final Takeaway】

> **Prompt Cache 幫你省 token，Semantic Cache 幫你省思考**

LLM 的真正成本不是 token 消耗，而是重複的「思考過程」。

設計良好的 Cache 策略，可以讓你的系統：

*   成本降低 70%+
*   延遲降低 80%+
*   同時維持答案品質

這不是優化，而是架構設計的必要選項。

* * *

**References**:

*   [OpenAI Embedding Documentation](https://platform.openai.com/docs/guides/embeddings)
*   [GPTCache - Semantic Cache 開源實作](https://github.com/zilliztech/GPTCache)
*   [Redis Vector Search](https://redis.io/docs/stack/search/reference/vectors/)

* * *

**Tags**: `#LLMCache` `#PromptCache` `#SemanticCache` `#Embedding` `#CostOptimization` `#LLMOps` `#RAG` `#VectorSearch` `#Production` `#Architecture`

**延伸閱讀**:

*   [向量資料庫完全指南：為什麼 LLM 時代需要 Vector DB？](/blog/llm-vector-db) — Semantic Cache 的底層：理解 embedding 相似度搜索的工作原理
*   [Frontier、Mini、還是自建：Production LLM 的架構沒有標準答案](/blog/frontierminiproduction-llm) — Cache 策略與模型選型的組合：降成本的兩條路怎麼互補
*   [Langfuse](/blog/langfuse) — Cache 命中率的可觀測性：用 Langfuse 監控 cache 效果與成本趨勢

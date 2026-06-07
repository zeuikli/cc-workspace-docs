---
url: "https://warmwater.dev/blog/agent-memory-strategy-selection"
title: "Agent Memory 策略選型：三個決策，一個框架"
date: 2026-05-14
category: Viewpoint
source: warmwater.dev
---

寫完 Agent Memory 這個系列，我自己開始重新想一件事：如果現在要設計一個 agent 的 memory 系統，我會從哪裡開始？

分析框架原始碼的時候，關注點在「這個框架怎麼做」。但回頭看整個系列，我發現更值得想的問題是「什麼時候該怎麼做」——框架是結果，決策才是起點。

這篇不是結論，是我消化完這些材料之後，試著把思考過程整理出來。沒有標準答案，因為正確的設計取決於你的 agent 在做什麼——而那個問題只有你能回答。如果你也在想這些事，可以跟著一起走一遍。

**這篇想一起想的：**

- Write / Search / Storage 三個決策為什麼是鎖在一起的
- 有沒有一個問題可以切出最關鍵的分叉
- 「以框架為 base 再 override」這個方向是否更務實
- 從 K8s SRE 到通用 agent，這個思路能不能套進去

---

## Write / Search / Storage 為什麼鎖在一起？

Agent memory 的設計有三個核心決策：Write（怎麼寫進去）、Search（怎麼找回來）、Storage（存在哪）。這三個決策不是獨立的，改其中一個通常要跟著改另外兩個。

大多數人在選 memory 系統的時候，會問「哪個 recall 最準？」或「哪個 latency 最低？」這些問題不是沒意義，但它們在問框架，不在問決策。

**Write**：記憶怎麼寫進去？LLM 摘要後存（mem0 style）？Agent 直接寫（engram style）？還是原文存（mempalace style）？

**Search**：記憶怎麼找回來？語意向量搜尋？BM25 關鍵字？還是精確取回？

**Storage**：記憶存在哪？SQLite？Vector DB？Relational DB？

這三個決策不是獨立的，它們有一條隱藏的因果鏈：

Write 方式決定了資料的形式。LLM 摘要產生語意段落，verbatim 存的是原文，直接寫存的是結構化 fact。資料的形式決定了能用什麼搜尋——語意段落走向量搜尋，原文和關鍵字走 BM25，精確 fact 走 exact fetch。搜尋方式決定了 storage 需要什麼索引結構。

這條因果鏈的意思是：**你不能單獨改其中一個決策。** LLM extraction + BM25 的組合在技術上可以跑，但你在用關鍵字搜尋 LLM 改寫過的語意摘要——搜尋品質會差，而且你不知道為什麼。

---

## 第一個問題：「大概對」跟「完全一樣」，對你的資料有差嗎？

在所有決策分叉之前，有一個問題可以把大多數情況切開：

**你的 agent 記的東西，「語意正確」夠用，還是必須「逐字正確」？**

這個問題不是在問精確度偏好，是在問資料性質。

「用戶喜歡簡潔的回答」——語意正確就夠了。LLM 摘要成「user prefers concise responses」，下次召回的時候 agent 知道方向，不需要原文。

`cpu: 500m, memory: 1Gi, replicas: 3`——逐字正確。數字必須一模一樣，任何 LLM 改寫都是風險。「大概 500 millicores、記憶體約 1G」這個摘要版本，套回 deployment 是真實的 incident。

這個分叉直接決定了 Write 策略：

- **語意正確夠用** → LLM extraction path（mem0、deerflow 的 write 設計）
- **逐字正確** → Verbatim path（mempalace 的 verbatim write）

LLM extraction path 的優點是自動：agent 不需要決定要記什麼，框架在對話結束後提取 fact，去重，更新。代價是不可逆——原文丟了，只剩 LLM 的詮釋。對數字、程式碼、設定檔，這個代價太高。

Verbatim path 的優點是保真：原文完整，數字不變，可以直接貼回使用。代價是 storage 線性成長，搜尋壓力全在 retrieval 層。

---

## LLM Extraction 適合什麼場景，不適合什麼？

LLM extraction 不是壞設計，它只是有邊界：適合語意理解，不適合精確保存。

**適合的場景：** Agent 需要理解用戶的偏好、背景、習慣。這類資訊的價值在語意層——「用戶是資深 Python 工程師，不需要解釋基礎概念」——原文是什麼其實不重要，重要的是 agent 下次的行為有沒有調整。LLM extraction 在這裡是正確的選擇。

**不適合的場景：** 資料裡有數字、有結構、有精確格式要求。K8s YAML 是最極端的例子，但不只是 YAML——任何 config、任何 code snippet、任何 API 規格，只要「大概」跟「精確」有實質差距，LLM extraction 就不能用。

還有一個更微妙的邊界：**需要稽核的資料**。LLM extraction 是有損壓縮，原文已丟。如果你事後想知道「agent 當時記的到底是什麼」，或者需要對某個決策回溯，verbatim 是唯一選擇。

---

## 選框架不是選「最強」，是選「default 最接近你的」

確定了 Write 策略之後，框架選型的邏輯就清楚了：

**你的 majority use case 是什麼？** 找一個 default 行為吻合這個 majority 的框架。

如果你在建一個對話 agent，大部分需要記的是用戶偏好和對話歷史——mem0 的 LLM extraction + 語意搜尋是合理的 default，直接開始用，不要 over-engineer。

如果你在建一個 coding agent，大部分需要記的是程式碼片段、設定、API 介面——mempalace 的 verbatim + ChromaDB 是合理的 default。

如果你在建一個 operational agent（K8s SRE、deployment pipeline），需要記 operational pattern 和精確的 config——沒有單一框架的 default 完全吻合，這是需要混搭的場景。

**框架選型的邏輯不是「最強」，是「摩擦最小」。** 選一個讓你的主要 use case 不需要 workaround 的框架，然後處理邊界情況。

---

## 剩下不 fit 的部分：Override，不是遷就

實際場景裡，單一框架通常能覆蓋 70-80% 的需求，剩下的 20-30% 性質不同，不能強塞進 default pipeline。

這個時候的選擇不是「換一個更強的框架」，是**針對那 20-30% 加一條平行路徑**。

K8s SRE Agent 的例子：

- Operational pattern（OOM 解法、rollout 決策）→ engram，FTS5 BM25，latest-wins upsert。這類知識三年後還有效，用 direct write，keyword 搜尋。
- 驗證過的 YAML manifest → mempalace，verbatim chunk，exact fetch。數字不能走 LLM extraction，storage 必須保留原文。
- Pod status、當前 log → 不存，on-demand kubectl。這是當下狀態，存了有害。

這三條路徑在技術上是兩個不同的系統（engram + mempalace），根據 query 類型路由。對 agent 來說，介面可以統一；在內部，不同的資料走不同的 pipeline。

**Override 的原則**：找出你的資料裡，和框架 default 性質不同的部分，為那些部分建一條獨立的路徑，不要試圖用一個框架的設定把它捏成另一種形狀。

---

## 我現在會從這幾個問題開始想

把上面的邏輯整理成問題，不是流程圖，是我自己在設計的時候會問的事：

**第一個問題，問資料性質：** Agent 主要在記什麼？這些資料的精確性要求是什麼？有沒有數字、程式碼、設定需要逐字保留？

這個問題的答案決定 Write 策略。LLM extraction 還是 verbatim？還是兩者都需要？我覺得這個問題是整個設計最重要的分叉，先想清楚再說其他的。

**第二個問題，問召回方式：** Agent 需要記憶的時候，它在問什麼樣的問題？「有沒有類似的情況」（語意搜尋）？「上次 OOMKilled 是怎麼解的」（keyword）？「給我那份 YAML」（exact fetch）？

召回方式決定 search strategy，search strategy 決定 storage 需要什麼索引。這組是連動的，但我發現召回方式比較好想——從「agent 會怎麼問這個問題」出發比從「我要選什麼 storage」出發容易。

**第三個問題，問部署限制：** Single-user 還是 multi-user？能不能接受一個 server 要管？

這個問題決定 SQLite vs PostgreSQL，local ChromaDB vs hosted vector DB。這層我覺得反而是最容易想的，因為限制比較清楚。

走完這三個問題，框架大概就浮現了——找一個 default 最接近你答案的框架，對不 fit 的部分加平行路徑。這個結論我自己也還在驗證，不確定有沒有我沒想到的邊界情況。

---

## 結語

這個系列分析了 8 個 memory 框架的原始碼，每個框架都是某組決策的具體實作。回頭看，它們沒有哪個是「錯的」，只是 default 假設不同——適合的場景也就不同。

Write / Search / Storage 的正確組合取決於你的 agent 在記什麼，而那個問題只有你能回答。我把我的思考過程整理在這裡，但如果你的場景跟我想的不一樣，你的答案很可能也不一樣。

> **結語**：選 memory 框架之前，先搞清楚你的資料需要「大概對」還是「完全一樣」。這個問題的答案，比任何 benchmark 分數都更能決定你的架構走向——至少目前我是這樣想的。

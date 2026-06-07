---
url: "https://warmwater.dev/blog/agent-memory-05-lifecycle"
title: "Memory 05：記憶活多久——8 個系統的生命週期設計"
date: 2026-05-14
category: Source Code
source: warmwater.dev
---

[
← Source Code ](/blog?tag=Source%20Code)  Source Code 
 
# Memory 05：記憶活多久——8 個系統的生命週期設計
 
 2026-05-14 · — views  
  
  
記憶的問題不只是「存什麼」和「怎麼找」，還有「活多久」。


一個 agent 跑了幾個月，context window 裡應該是三個月前的偏好還是昨天的？上週的架構決策還是今天的 pod status？這些問題的答案，各系統的設計差異極大。


---


## 兩個根本問題：偏向什麼，發生在何時？


所有 lifecycle 設計都繞著兩個問題轉：


**問題 1：記憶要偏「新的」還是「重要的」？**


最新的不一定最重要。「用戶喜歡 Python」這個 fact 三個月前說的，可能比昨天說的「幫我查一下天氣」更值得留著。但系統沒辦法事先知道哪個重要——只能靠時間、頻率、或 LLM 評估來代理重要性。


**問題 2：這個偏向發生在 write 時，還是 search 時？**


Write time 偏向：寫入時就決定要不要存，或存成什麼形式（deerflow 的 confidence 驅逐、agentmemory 的分層）。
Search time 偏向：全部存著，搜尋時才 blend 時間分數（OpenViking 的 Hotness）。


這個差異影響 latency：write time 做決策，search time 就輕鬆；search time 做計算，每次 query 都要跑 decay 公式。


| 系統 | 偏向什麼 | 發生在何時 |
| --- | --- | --- |
| OpenViking | 頻率 × 時間（Hotness） | Search time blend |
| agentmemory | 知識類型決定衰退速率 | Write time 分層 |
| deerflow | Confidence（重要性） | Write time 驅逐 |
| hermes | 不偏向（Frozen snapshot） | Session 開始凍結 |
| engram | 最新覆蓋（Latest Wins） | Write time upsert |
| mempalace | Importance score | Search 前排序 |
| letta | Sleeptime 背景鞏固 | Session 結束後非同步 |
| mem0 | 無明確偏向 | — |


---


## OpenViking：頻率 × 時間衰減


OpenViking 的 Hotness 公式：


```
hotness = sigmoid(log(active_count)) × exp(-ln2/7 × age_days)
final = (1 - alpha) × semantic + alpha × hotness  # alpha=0.3
```


「最近常被存取的記憶」才熱。active_count 是這筆記憶被 retrieve 的次數，age_days 是記憶的年齡，half_life 預設 7 天。alpha=0.3 代表 70% 語意分數 + 30% 熱度分數。


這個設計的邏輯是：如果你最近一直在查某個記憶，代表它現在對你重要。如果一筆記憶兩週沒被碰，熱度接近 0，但不會被刪除——只是在 search ranking 裡沉下去。


  

---


## agentmemory：Ebbinghaus 分層衰減


agentmemory 用 Ebbinghaus 遺忘曲線概念，把記憶分四層，每層衰退速率不同：


```
Procedural（怎麼做） → 幾乎不衰退
Semantic（我知道什麼） → 慢衰退
Episodic（session 摘要）→ 中速衰退
Working（今天的觀察）  → 1 session 後快速消失
```


寫入時，lifecycle hook 根據記憶的「類型」決定放進哪一層。Procedural knowledge（「這個專案用 pytest，fixture 放在 conftest.py」）幾乎永遠留著。Working memory（「這次 session 在改 auth 模組」）session 結束後就衰退。


這個設計的強項是 coding agent——程序性知識是最有複用價值的，不該因為時間久就被淡化。


  

---


## deerflow：Confidence 驅逐，100 facts 上限


deerflow 的記憶是一個 JSON，上限 100 條 facts。每筆 fact 有 LLM extraction 時給的 confidence 分數。空間滿了，confidence 最低的被淘汰。


沒有時間概念。記憶不會因為「太舊」被淘汰，只會因為「confidence 不夠高」被新記憶擠出去。


問題在於 confidence calibration：LLM 對自己的輸出有多確定，這個分數是 model-specific 的，可能隨時間漂移。同一個 agent 用了三個月之後，早期記憶的 confidence 和晚期記憶的 confidence 不在同一個校準基準上。


  

---


## hermes：刻意不做時間偏向


hermes 的 L1 episodic memory 在 session 開始時凍結，整個 session 不更新。這是唯一主動避免 recency bias 的系統。


動機不是記憶哲學，是 token 成本：系統提示每次相同 → prefix cache 命中 → 節省約 75% token。如果 memory 每次 session 都變，prefix cache 就失效，每次都要重新計算整個 system prompt 的 KV cache。


用工程 constraint 覆蓋記憶設計，得到一個「意外地哲學」的結果——所有記憶在這個 session 裡都一樣重要，不管是三個月前存的還是昨天存的。


L2 semantic memory 用 SQLite FTS5，不做 time-based ranking，純 BM25 keyword 排名。


  

---


## engram：Latest Wins Upsert


engram 的寫入是 upsert by topic key：同一個 topic 永遠只有一筆記憶，新的蓋掉舊的。


```
mem_save(topic="auth_approach", content="改用 JWT，不再用 session cookie")
# → 直接覆蓋之前同 topic 的記憶
```


這是隱性的 100% recency bias——最新的認知永遠勝出，不管舊的有多重要。設計假設是：對同一個 topic，最新的認知就是最正確的認知，不需要保留歷史。


對某些場景是對的（技術決策確實會更新），但對「用戶偏好的演變」這類場景，把舊偏好直接蓋掉可能丟掉有用的歷史脈絡。


  

---


## letta：Sleeptime 背景鞏固


letta 的 archival memory 在 session 結束後，有一個非同步的 sleeptime agent 在背景跑：re-evaluate 記憶的重要性、合併重複記憶、更新 entity 關係。


這個設計讓即時 latency 不受影響——鞏固是離線的，不在 inference path 上。代價是：記憶的品質在 session 和 session 之間才會更新，即時 session 裡看到的記憶可能還沒被鞏固。


適合跑夜間批次鞏固的 long-running agent，不適合需要「剛說完就記起來」的即時對話場景。


  

---


## mem0：無 Decay，靠 Dedup


mem0 沒有 decay 機制。記憶不會因為時間久而降低優先級，也不會被淘汰。唯一的去重機制是 dedup：寫入時比對現有記憶，語意重複的會被合併或更新。


這個設計假設是：如果一筆記憶不再有意義，agent 或用戶應該主動刪除它，不應該讓系統自動淡忘。


沒有 decay 的代價是 memory 會隨時間無限成長（除非有 retention policy）。優點是不會因為 decay 設計錯誤而意外淡忘重要的舊記憶。


  

---


## mempalace：Importance Score，需手動設值


mempalace 有 importance score 機制，在 search 前用 score 排序，只把高分記憶注入 context。


問題是：importance score 需要寫入時手動設值，否則預設值全部相同，排序退化成 random top 15。沒有自動計算 importance 的機制。


這讓 mempalace 在 verbatim 保真度上很強（原文不被 LLM 改寫），但在時間偏向上幾乎沒有機制——所有記憶平等，除非你每次存記憶時都記得手動設 importance。


  

---


## 有損摘要 vs 原文保真：哪種記憶老化得更好？


Lifecycle 的問題還有一個維度：記憶隨時間「降解」的方式不同。


**有損摘要（mem0、deerflow、agentmemory、letta、engram、hermes）**


寫入時 LLM 改寫，存的是語意摘要。時間久了，原文已丟，無法回頭稽核。如果 extraction 當時判斷錯誤——把一個暫時的偏好存成長期事實——這個錯誤會一直在。


代價：資訊損失不可逆，無法回溯原始素材，數字精度風險高。


**原文保真（mempalace）**


存的是 verbatim chunk，原文完整保留。時間久了，chunk 還是原本的樣子。


代價：storage 隨時間線性成長，retrieval 壓力全轉移到搜尋層。


**一個實際的選擇框架：**


```
記憶的用途是「理解用戶」→ 有損摘要
  agent 需要知道「喜好、習慣、背景」，semantic fact 比原文更直接

記憶的用途是「找回原始資料」→ 原文保真
  需要找回「當時那段程式碼」、「原始設定值」，verbatim 才可靠
```


---


## 數字精度：LLM Extraction 的致命弱點


有損摘要系統在 lifecycle 裡有一個特別危險的問題：數字。


LLM 在 extraction 時對數字特別不可靠：


```
原文：cpu: 500m, memory: 512Mi, replicas: 3, port: 8443
LLM extraction 後可能變成：
  "CPU 大概 500 millicores"、"幾個 replica"、port 被直接省略
```


四捨五入、單位丟失、直接省略、幻覺替換——數字是 LLM extraction 最容易出錯的地方。一旦存進記憶，原文已丟，無法修正。


目前沒有任何框架原生解決這個問題。真正安全的做法是繞開 LLM extraction pipeline，把數字型 fact 存成 typed structured field：


```
{ "cpu_limit": "500m", "memory_limit": "512Mi" }
```


而不是 `{ "fact": "CPU 約 500m" }`。數字從來不經過 LLM 改寫，只能 verbatim 進、verbatim 出。


---


> 
**結語**：記憶活多久，不只是淘汰策略的問題——它決定了 agent 在六個月後是否還能依賴自己的記憶做出可信的判斷。

  
  
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

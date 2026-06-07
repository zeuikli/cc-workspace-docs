---
url: "https://warmwater.dev/blog/agent-memory-01-write-design"
title: "Memory 01：誰決定什麼值得記——Agent 記憶的四種寫入模式"
date: 2026-05-14
category: Source Code
source: warmwater.dev
---

[
← Source Code ](/blog?tag=Source%20Code)  Source Code 
 
# Memory 01：誰決定什麼值得記——Agent 記憶的四種寫入模式
 
 2026-05-14 · — views  
  
  
如果你要讓一個 Agent 記住事情，第一個要回答的問題是：**誰來決定這件事值得記？**


這個問題看起來簡單，但八個開源 Agent 記憶系統給出了截然不同的答案。有些讓 LLM pipeline 自動判斷；有些讓 lifecycle hooks 自動捕捉；有些要求 agent 自己決定；有些等到 session 結束才統一處理。這些不同的答案，最終導致了完全不同的架構。


**讀完這篇，你會理解：**


- 四種寫入模式背後的工程邏輯，以及各自承擔的風險
- 為什麼所有記憶系統都在對抗 context compaction，以及什麼是強制補救
- Mechanism-driven 和 Agent-curated 的根本取捨，什麼場景適合哪個


這篇不是各系統的操作手冊，而是在問：這些設計決策的背後，究竟在取捨什麼。


---


## Agent 記憶的寫入分三層：主動、自動與強制補救


所有 Agent 記憶系統的寫入路徑都可以分成三層：主動路徑（Layer 1）由 agent 或 application 明確決定存什麼；自動路徑（Layer 2）由機制偵測到事件就寫入；強制補救（Layer 3）在 context 快滿前把沒存的東西搶救出來。


```
Layer 1：主動路徑 agent / app 明確決定存什麼
Layer 2：自動路徑 機制偵測到事件就寫入
Layer 3：強制補救 context 快滿前，把沒存的東西搶救出來
```


其中第三層是關鍵。很多人以為記憶系統的核心是「怎麼存」，但工程上更難的問題是：**context compaction 發生的時候，那些還沒存進去的工作記憶，怎麼辦？**


Context compaction 是一個不可逃避的物理限制——LLM 的 context window 有上限，當對話夠長，舊的訊息必然被壓縮或丟棄。任何只靠 Layer 1 或 Layer 2 的系統，都有可能在一次 compaction 之後失去大量工作 context。強制補救（Layer 3）的存在，正是為了對抗這個結構性問題。


下表是八個系統對三層的覆蓋情況：


| 系統 | Layer 1（主動） | Layer 2（自動） | Layer 3（強制補救） |
| --- | --- | --- | --- |
| mem0 | ✓ | ✗ | ✗ |
| agentmemory | ✓ | ✓（12 hooks） | △（AUTO_COMPRESS，預設 off） |
| deerflow | ✗ | ✓（30s debounce） | △ |
| engram | ✓ | ✗ | ✓（post-compaction.sh） |
| hermes-agent | ✓ | ✓（每 turn 自動） | ✗ |
| letta | ✓ | ✓（compaction） | ✓（sleeptime agent） |
| OpenViking | ✗ | ✓（session end） | △ |
| mempalace | ✓ | ✗ | ✓（Stop/precompact hook） |


**mem0 是唯一完全依賴 Layer 1 的系統**——它把所有寫入責任交給 application code，本身不做任何自動捕捉。這不是缺陷，而是一個明確的設計選擇，下面會解釋為什麼。


---


## Archetype A：Pipeline/Extraction — 讓背景 LLM 決定


**代表系統：mem0、deerflow**


這個模式的核心思路是：不讓 agent 分心管記憶，在 agent 執行路徑之外，另起一個 LLM pass 分析對話、提取值得記住的 facts。

 Archetype A · Pipeline / Extraction
 
 mem0
 

memory.add(messages)
application 主動呼叫
  
↓
 

Phase 0–1
讀歷史 context · semantic recall
  
↓
 

Phase 2：LLM Extraction
ADD-only · 單次 call
不做 UPDATE / DELETE 判斷
  
↓
 

Phase 3–5
embed → MD5 hash dedup → batch insert
  
↓
 

Phase 6
entity linking → entity store
  
↓
 

Vector DB + Entity Store
20+ vector store 選項
  
V3 改為 ADD-only
LoCoMo 71.4 → 91.6
  

  
 deerflow
 

agent 執行完畢
MemoryMiddleware.after_agent()
  
↓
 

訊息過濾
去除 tool calls · 只留對話
  
↓
 

Signal Detection
regex 掃描最近 6 條 human messages
  
↓
 
偵測結果決定 LLM 更新策略
 
 
correction
激進修正錯誤 facts
  

reinforcement
提高 confidence 確保寫入
  

neutral
增量更新，不刪既有
 
↓
 

MemoryUpdateQueue
30s debounce · threading.Timer
  
↓
 

LLM Update
背景非同步 · 不阻塞 agent response
  
↓
 

memory.json
原子寫入（tmp → rename）· 最多 100 facts
 

**mem0** 的寫入由 application code 主動觸發，走一條 8 步驟 pipeline。V3 最重要的改動是把 extraction 改成 ADD-only，捨棄了 V2 中「先提取、再讓 LLM 決定 ADD/UPDATE/DELETE」的兩步驟流程。


為什麼？因為第二步犯了一個根本的錯誤：要求 LLM 對資料庫做精確的 CRUD 決策。LLM 擅長從對話裡提取值得記住的事實，卻不擅長判斷一條新記憶應該覆蓋、補充還是刪除哪條舊的。V3 把 CRUD 決策還給確定性機制——重複用 MD5 hash 擋，關聯用 entity graph 連——LLM 只負責提取，LoCoMo benchmark 從 71.4 跳到 91.6。


**deerflow** 更輕量：整個記憶存在一個 JSON 檔案，agent 執行完成後 30 秒 debounce，背景 LLM call 分析對話並更新記憶。最獨特的設計是信號偵測：在進 LLM 之前，middleware 就用 regex 判斷這段對話是 correction（用戶在糾正 agent）、reinforcement（用戶在確認做法），還是 neutral。不同信號改變 LLM 的更新策略，不是讓 LLM 自己判斷情境。


這個模式的工程含義：agent 的執行路徑完全不被記憶操作打斷，但代價是資訊損失。LLM extraction 是有損的，數字、精確字詞都可能在 pipeline 中被改寫或省略。


---


## Archetype B：Hook → 多層鞏固 — 讓機制決定，讓時間篩選


**代表系統：agentmemory**


agentmemory 的設計假設是：觀察越多越好，但不是所有觀察都值得長期保存。先全量捕捉，再讓時間和重複性自然篩選出真正重要的東西。


 Archetype B · Hook → 多層鞏固 (agentmemory)
 
 
Claude Code Lifecycle Event
SessionStart · PostToolCall · SubagentStop · …
 
↓
  
 
12 Hooks Adapter
stdin JSON → POST /agentmemory/observe
 

hooks 是 Claude Code 的機制，不是 agentmemory 自己的

其他 agent 打同一個 REST endpoint 也能運作

 
↓
  
 
Working Memory（即時寫入）
raw tool call observation · `edit: file.go` · `bash: go build` · …
 
↓
  
session 結束 → consolidation pipeline
  
 
Importance Scoring（LLM 打分）

  
 1–3
routine reads
 
4–6
edits / cmds
 
7–9
arch decisions
 
10
breaking
  
importance ≥ 5 才進 consolidation
 
↓
  
 
concept grouping → LLM 壓縮
相同 concept 的 observations 合併為 Memory item
 
↓
  
四層記憶體系（Ebbinghaus decay）
 
  Working
 
快速衰退
1 session
  
 Episodic
 
Session 摘要
中速衰退
  
 Semantic
 
跨 session 模式
慢速衰退
  
 Procedural
 
工作流 / 決策
幾乎不衰退
 

要特別說清楚一件事：**這 12 個 hooks 是 Claude Code 的 lifecycle 機制，不是 agentmemory 自己的**。agentmemory 只是寫了 adapter scripts 接收 Claude Code 透過 stdin 傳來的 JSON，再 POST 到自己的 REST endpoint。換任何其他 agent，只要有 lifecycle hooks，就能打同一個 endpoint。沒有 hooks 的 agent 改用 MCP tools 手動觸發，但自動捕捉的優勢就消失了。


四層記憶借用 Ebbinghaus 遺忘曲線的概念：不同類型的知識有不同的「壽命」。Procedural（怎麼做）幾乎不衰退，Working（今天觀察到什麼）一個 session 後消失。知識類型決定壽命，不是人工設定優先序。


這個模式的工程含義：自動化程度最高，agent 什麼都不用管。但 Working Memory 裡存的是原始 tool call 觀察，大量 raw noise 進入系統，FTS 搜尋的精準度會被這些低信號觀察稀釋。


---


## Archetype C：Agent 直接寫 — 紀律換信噪比


**代表系統：engram、hermes Layer 1、letta**


這個模式的立場是：讓 agent 自己決定什麼值得記，寧可漏記，也不要讓 noise 進系統。


 Archetype C · Agent 直接寫
 
 engram
 

agent 判斷值得記
SKILL.md 定義強制觸發條件
  
↓
 

mem_save（MCP tool）
type · title · content · topic_key
  
↓
 

topic_key 存在？

 
↓
 

YES → UPDATE（revision_count +1）

NO → INSERT 新記錄

 
↓
 

SQLite + FTS5
同 topic 永遠只有一筆最新記錄
 

  
 hermes
 

agent 判斷值得記

 
↓
 

memory tool
action="add" · target="memory"
  
↓
 

MEMORY.md（原子寫入）
tmp → os.replace()
  
↓
 

系統提示 frozen snapshot
 mid-session 不更新快照 
 
↓
 

下次 session 啟動才生效

保護 prefix cache（-75% token）

  

  
 letta
 

agent 判斷值得記
在 agent loop 內部判斷
  
↓
 

core_memory_replace
or archival_memory_insert
  
↓
 

Core Memory Block
常駐 system prompt `<memory_blocks>`
  
↓
 

agent 當下就看到新記憶

記憶 = agent 的一部分

 

三個系統選擇這個模式，但動機不同。


**engram** 的立場最明確：拒絕自動 extraction，要求 agent 主動呼叫 `mem_save`，並在 SKILL.md 裡定義強制觸發條件（架構決策後、bug fix 後、用戶確認 convention 後）。`topic_key` 是 engram 特有的設計——同一個技術決策被討論多次時，其他系統會累積多個版本，FTS 返回互相矛盾的結果。engram 用 upsert 保證同一個 project + scope 下相同 topic 永遠只有一筆最新記錄。


**hermes-agent** 的 Layer 1 讓 agent 主動寫 MEMORY.md，但多了一個工程約束：frozen snapshot。Session 開始時讀一次記憶文件凍結成快照，mid-session 的任何 memory tool 呼叫只更新磁碟，不更新快照。這個設計的動機不是記憶哲學，而是工程成本：如果每輪對話後把最新記憶注入系統提示，LLM provider 的 prefix cache 就會每次都失效，token 費用增加約 75%。工程約束決定了記憶設計，不是反過來。


**letta** 走得更遠：記憶和 agent 不是分離的，是合體的。Core Memory 以 Block 形式常駐在 system prompt 的 `<memory_blocks>` 裡，agent 在每次對話當下就能判斷「這件事要不要更新 core memory」，並直接呼叫 `core_memory_replace` 修改。沒有外部 pipeline，沒有 extraction LLM——記憶就是 agent 的一部分。


這個模式的工程含義：信噪比最高，FTS 和 vector search 的排名最有意義。代價是完全依賴 agent 的判斷能力和執行紀律。缺乏 SKILL.md 約束的設置，可能什麼都不存。


---


## Archetype D：Post-session 批次 — 同名不同命


**代表系統：OpenViking、mempalace**


這兩個系統都在 session 結束後才批次處理記憶，但它們的動機完全相反。


 Archetype D · Post-session 批次
 
 OpenViking
 

session 結束
SessionCompressorV2 觸發
  
↓
 

ExtractLoop（ReAct）
最多 3 輪迭代
  
↓
 

LLM 先探索現有記憶
read · ls · search 工具
  
先讀後寫：知道現有狀態才輸出 patch
 
↓
 

輸出 JSON operations

 
 patch
手術式更新
 
replace
整體覆寫
 
sum
數字累加
 
immutable
建立後不改
  
↓
 

VikingFS（AGFS）
10 種 typed memory schema · viking:// URI
  
批次是設計選擇：確保 LLM 寫得精確
  

  
 mempalace
 

批次執行 / session 結束
mine · sweep · Stop hook
  
↓
 

無 LLM 介入
verbatim-first，不做任何萃取
  
↓
 

掃描檔案 / transcript
.gitignore aware · paragraph boundary
  
↓
 

800-char chunks（verbatim）
100 char overlap · 保留原文
  
↓
 

ChromaDB（HNSW）
all-MiniLM-L6-v2 · 本地 ONNX，不需 API key
  
批次是必然結果：沒有 per-message pipeline
 

**OpenViking** 選擇 post-session，是刻意的設計決策。ExtractLoop 是一個 ReAct loop：LLM 先用 `read`、`ls`、`search` 工具探索現有記憶狀態，再輸出精確的 JSON operations。先讀後寫是這個設計的核心——LLM 在不知道現有記憶狀態的情況下輸出的 patch，很可能 search 匹配不到，或重複現有記憶。四種 field-level MergeOp（patch / replace / sum / immutable）確保不同語義的資料用適合的合并策略：計數器累加不被覆寫，命名 key 建立後永不修改。


**mempalace** 的批次處理，則是 verbatim-first 哲學的必然結果。它完全不做 LLM extraction，永遠存原文——因為沒有 per-message 自動 extraction pipeline，批次 mine 是唯一可行的方式。LongMemEval R@5 = 96.6% 是這個選擇的直接結果：原文沒有被 LLM 改寫，精確字詞完整保留。


兩個系統的差異值得記住：OpenViking 的批次是「為了讓 LLM 寫得更精確」，mempalace 的批次是「因為根本不讓 LLM 寫」。


這個模式的工程含義：寫入延遲高（session 結束後才發生），但對 session 中的即時延遲沒有影響。


---


## 機制驅動還是 Agent 主控？寫入模式的根本取捨


機制驅動（Mechanism-driven）與 Agent 主控（Agent-curated）是寫入設計的兩個極端：前者讓系統自動判斷什麼值得記，後者讓 agent 自己決定。這兩種路線的取捨，決定了記憶庫的信噪比、搜尋品質，以及你對 agent 能力的依賴程度。


八個系統在這個維度上形成一個光譜：


```
自動化 ←─────────────────────────────────────── Agent 主控

deerflow  mem0  agentmemory  OpenViking  letta  hermes  engram
```


|  | 機制驅動 | Agent 主控 |
| --- | --- | --- |
| 信噪比 | 低（raw observation 多，noise 大） | 高（agent 篩選過） |
| 遺漏風險 | 低（自動捕捉，難以遺漏） | 高（agent 可能忘記存） |
| 搜尋品質 | FTS 被 noise 污染 | FTS 排名有意義 |
| 依賴 agent 能力 | 不依賴 | 強依賴 |
| 適合場景 | 高頻對話、multi-user SaaS | coding agent、有紀律的工作流 |


這不是優劣的對比，而是對不同問題的不同解法。一個需要記住上百萬用戶偏好的 SaaS 不可能讓每個 agent instance 自己決定要記什麼；一個 coding agent 如果讓 hooks 把每個 `bash` 指令都存進去，FTS 搜尋一個月後就退化成噪音資料庫。


---


> 
**結語**：「誰決定記什麼」這個選擇，直接決定了記憶庫裡存的是什麼——而存的是什麼，又決定了你能用什麼搜尋方式。下一篇會解釋這個耦合關係，以及四種搜尋模式背後的工程邏輯。

 
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

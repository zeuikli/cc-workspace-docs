---
url: "https://warmwater.dev/blog/hermes-agent-vs-openclaw-agent"
title: "hermes-agent vs OpenClaw：兩個 Agent 框架，同一批問題，不同的答案"
date: 2026-04-27
category: Source Code
source: warmwater.dev
---

[
← Source Code ](/blog?tag=Source%20Code)  Source Code 
 
# hermes-agent vs OpenClaw：兩個 Agent 框架，同一批問題，不同的答案
 
 2026-04-27 · — views  
  
  
讀完兩個框架的原始碼，最讓我印象深刻的不是它們有多不同，而是它們各自選擇了不同的問題去解。hermes-agent 和 OpenClaw 都在做「production-grade Agent」，都踩過同樣的坑，也都認真解決了那些坑——只是解法的方向，幾乎處處相反。


這篇不想評判哪個設計更好，因為大多數差異不是好壞之分，而是不同 scenario 下不同的取捨。我想做的是把這些取捨說清楚，讓讀者理解當面對同一個問題時，工程師怎麼因為不同的出發點，走到了完全不同的地方。


**讀完精華版（2 分鐘），你會理解：**


- hermes-agent 和 OpenClaw 為什麼在記憶體架構上走向相反的方向
- Subagent spawn 的同步 vs 非同步選擇，背後各自在管理什麼問題
- 執行安全的 Policy 層 vs Infrastructure 層，強度差在哪裡
- 兩個框架根本問題的不同：「越用越好」vs「永遠在線」


這篇不評判哪個設計更好，而是說清楚同一批問題的兩種誠實回答。


---


## 精華版


| 維度 | hermes-agent | OpenClaw |
| --- | --- | --- |
| 架構 | 單一 process，扁平 main loop | Gateway + Runner 雙層，控制平面與執行引擎分離 |
| 記憶體 | 三層動態召回（MEMORY.md + FTS5 + 外部 MemoryProvider） | 靜態 AGENTS.md bootstrap，無跨 session 召回 |
| Subagent spawn | 同步 blocking，parent 等待 child 完成才繼續 | foreground / background 兩模式，SubagentRegistry 持久化生命週期 |
| 執行安全 | Policy 層工具分類（絕對不可平行 / 安全平行 / 路徑相依） | Infrastructure 層：FS Policy + Tool Policy + Docker network_mode: none |
| 自我演進 | Trajectory → RL 訓練迴路，越用越好 | 無訓練機制，專注穩定可預測 |


**hermes-agent**：一個為了和使用者一起成長而設計的 coding assistant，記憶體、Skill 系統、RL 迴路都在回答「怎麼讓 Agent 更了解你」。


**OpenClaw**：一個為了在沒人看的時候也不中斷而設計的 always-on 助理，Gateway 分層、Registry 持久化、Failover Chain 都在回答「怎麼讓系統在異常情況下繼續運作」。


---


**記憶體方向相反**：hermes 的複雜度在「怎麼召回」（三層架構、FTS5、Memory Fencing），OpenClaw 的複雜度在「怎麼儲存」（vector search、QMD）。兩個是方向相反的豐富，不是哪個更完整。


**Subagent spawn 的核心問題是失敗模式**：hermes 同步 blocking——parent 永遠知道目前狀態，失敗收攏在 parent 控制之下；OpenClaw 允許非同步不確定性存在，但建了 AnnounceFlow + Orphan Recovery 確保 crash 後能恢復。你的子任務跑幾分鐘還是幾小時，決定哪個設計適合你。


**Policy vs Infrastructure 安全強度**：Policy 層（工具語意分類）靈活但可被 prompt injection 繞過；Infrastructure 層（`network_mode: none`）是物理上沒有網路介面，不是「你不應該連外網」的規則。代價是靈活性：infrastructure 限制是二元的，policy 可以細緻調整。


**根本問題不同，驅動幾乎所有取捨**：hermes 問「這個 Agent 能不能越用越好」，OpenClaw 問「這個系統在沒人看的時候能不能自己活下去」。這兩個問題不互斥，但選定一個，後面的設計優先順序就跟著定了。


---


> 
以下是完整版，按需取用。


## Production Agent 的共識解


讓我先說相同的地方，因為這件事本身就很有意思。


兩個框架獨立開發，技術棧不同（一個 Python，一個 TypeScript），目標使用者也不同——但在幾個關鍵問題上，它們幾乎收斂到了同樣的設計。這不是巧合，這是 production Agent 踩過同樣的坑之後的共識解。


**Pluggable Context Engine ABC**：兩個都定義了一個可替換的 Context Engine 抽象層，讓 context 壓縮策略可以被外部 plugin 替換。這個設計背後的洞見是一樣的：不同任務需要不同的壓縮策略，不應該硬編碼。


**LLM-based Context Compression**：都用 LLM 做摘要、都在 threshold 觸發、都有 session chain 讓壓縮後的歷史可以往回追溯。長對話會讓 context window 滿，這是無法迴避的問題，LLM 摘要是目前最實用的解。


**Prefix Cache 意識**：兩個都在意 Anthropic prefix cache，都設計了機制讓重複的 prompt 前綴能命中 cache。方法不同，但問題意識一樣——cache miss 代表 token 成本直接翻倍。


**Credential Rotation + Cooldown**：都有多 API key 輪換、rate-limit 後進 cooldown 的機制。hermes 叫 Credential Pool，OpenClaw 叫 Auth Profile Store，邏輯幾乎等價。


**13 個 Hook 注入點**：兩個都有 13 種 hook 事件類型。這個數字的吻合有點奇妙，但結構是一樣的：在 Agent lifecycle 的關鍵節點允許外部注入行為。


---


## 理念的分岔點


### 1. 架構：扁平 vs 分層


hermes-agent 的架構是扁平的。一個 `AIAgent` 類別包辦所有事：系統提示管理、對話狀態、LLM 呼叫、工具執行、記憶體、context 壓縮、中斷訊號處理。所有東西在同一個 process 裡跑，同一個 while loop 裡管理。


OpenClaw 把系統切成兩層：**Gateway**（控制平面）負責 channel 生命週期管理、WebSocket RPC、session store、auth 和 cron；**pi-embedded-runner**（執行引擎）只做一件事，給定一個 session 跑一個 Agent turn。兩層可以獨立重啟、獨立升級。


**取捨**：扁平架構複雜度低，部署簡單，一個 process 就搞定。分層架構帶來運維彈性——Gateway crash 不影響正在執行的 session 狀態（因為狀態在資料庫），執行引擎邏輯變更不需要重啟 Gateway。


**Scenario**：個人機器上的 coding assistant，扁平架構完全夠用，額外的分層只是增加複雜度。24/7 的多平台助理，需要能滾動更新、不中斷服務，分層的代價才值得付。


### 2. 記憶體：動態召回 vs 靜態 Bootstrap


hermes-agent 有完整的三層記憶體系統：**MEMORY.md**（結構化長期記憶，session 開始時載入）、**SQLite FTS5 全文搜尋**（搜尋歷史對話，BM25 排名）、**外部 MemoryProvider ABC**（可接向量資料庫等 backend）。更重要的是它有 **Memory Fencing**：召回的記憶用 XML 標籤包起來，讓模型能分清楚「我記得的事」和「使用者現在說的話」，召回內容不會被 persist 進對話歷史。


OpenClaw 沒有動態記憶召回機制。它有 AGENTS.md bootstrap——每個 Agent run 開始時載入的靜態 context 文件——但沒有跨 session 的搜尋和動態召回。


**取捨**：動態召回讓 Agent 能在跨越幾十次 session 之後，還記得你上次說你偏好簡短回答、你的 Git repo 在哪裡、你上次有個沒解決的 bug。但召回品質依賴嵌入向量或全文搜尋的準確性，召回的東西如果沒有 fence 好，可能污染對話 context。靜態 bootstrap 可預測、無噪音，但 Agent 每次 session 都是「新的」。


**Scenario**：長期個人助理，你希望它記得你的偏好和專案背景——記憶召回的價值很高。任務導向的短期 Agent，每次 session 任務明確、context 在 prompt 裡給——靜態 bootstrap 更乾淨。


### 3. Agent Spawn：同步控制 vs 生命週期管理


這個點讓我在讀原始碼時停下來想了一下，因為一開始我以為 hermes-agent 沒有 agent spawn——它只是在 tool 層做平行執行。讀進去之後才發現 `delegate_tool.py`，而且程式碼裡有一行注釋：


```
# modeled on OpenClaw's buildSubagentSystemPrompt

```


hermes-agent 看過 OpenClaw 的設計，然後選擇了不同的路。


**hermes-agent 的 `delegate_task`**：parent agent 呼叫 `delegate_task`，spawn 出一個或多個 child `AIAgent` instance，parent **同步 blocking 等待**所有 child 跑完，只拿回最終 summary（child 的中間工具呼叫不進入 parent context）。Child 拿到全新的 context，`skip_memory=True`——完全不碰記憶體系統。預設 depth 1（flat：parent 可以 spawn child，child 不能再 spawn），最多開放到 depth 3。


**OpenClaw 的 `sessions_spawn`**：spawn 出獨立的 agent session，可以是 **foreground（同步）或 background（非同步，parent 繼續跑）**。SubagentRegistry 把所有 subagent 的生命週期狀態持久化到磁碟；AnnounceFlow 讓 child 完成後非同步把結果交回 parent；Gateway crash 後有 Orphan Recovery——找回孤兒、補發未送達的結果。


兩個框架面對的是同一個問題：agent chain 變長，失敗路徑也變長。hermes 的答案是**縮減不確定性**——parent 同步等待，永遠知道目前的狀態，中間的混亂被隔離在 child 的 session 裡。OpenClaw 的答案是**管理失敗**——允許不確定性存在，但建立完整的 recovery 機制確保失敗後能恢復。


**Scenario**：短時平行任務，parent 需要整合所有 child 的結果再繼續——hermes 的同步設計讓控制流程清晰。長時背景任務，child 可能跑幾分鐘甚至幾小時，需要跨 turn 存活、需要在 Gateway restart 後繼續——OpenClaw 的生命週期管理才夠用。


### 4. Exec 安全：Policy 分類 vs 基礎設施隔離


hermes-agent 的 exec 安全設計核心是**工具分類**：每個工具呼叫被分成三類（絕對不能平行的、可以安全平行的、路徑相依的），決定哪些可以同時跑。這個分類是 harness 層的判斷，基於對工具語意的理解。


OpenClaw 有四道防線：FS Policy（file 工具只能操作 workspace 路徑）、Tool Policy（per-agent allow/deny list，owner-only gating）、Exec Approval Flow（高風險命令推送 iOS 通知等人工確認）、Docker sandbox（`network_mode: none`）。


最後這一道值得特別說。`network_mode: none` 不是「你不應該連外網」的 policy，而是「你在物理上沒有網路介面」。Policy 可能被 prompt injection 繞過，沒有網路介面不行。


**取捨**：Policy-based 安全靈活，可以根據場景調整，但強度取決於 policy 本身有沒有漏洞。Infrastructure-based 安全保證更硬，但代價是限制性更強，某些合法用途也會被擋住。


**Scenario**：受信任環境（自己的機器、已知任務）——policy 分類的靈活性更有價值。執行不受信任的 code、多用戶環境、需要強隔離——infrastructure 層的保證更重要。


### 5. 自我演進 vs 穩定可靠


hermes-agent 有一個在其他框架裡沒有的設計：**Trajectory → RL 訓練迴路**。每次對話的軌跡（輸入、工具呼叫、輸出、使用者反饋）被存成 ShareGPT 格式，可以透過 batch_runner 送進 Atropos RL 訓練 pipeline，微調模型。Skill 系統讓 Agent 在對話中動態載入能力，skill nudge daemon 每 10 次工具呼叫提示一次是否有合適的 skill。


OpenClaw 完全沒有這個機制，不收集訓練資料，沒有 skill 系統，專注在讓系統穩定運作。


**取捨**：自我演進讓 Agent 越用越好，但「越用越好」也意味著行為在改變——下週的 Agent 和今天的 Agent 不完全一樣。穩定可靠讓行為可預測，今天能跑的東西明天還能跑，但沒有自動改善的機制。


**Scenario**：研究用途、資料收集系統、你希望從使用中學習——RL 迴路的價值很高。生產服務、需要一致行為、不能接受 non-deterministic 改善——可預測性更重要。


### 6. 失敗回報：靜默恢復 vs 透明記錄


hermes-agent 出錯時，分類失敗原因後 rotate/retry，對使用者靜默處理。多數情況下使用者不會感知到有 API 錯誤發生。


OpenClaw 的 `FallbackSummaryError` 收集所有嘗試歷史（每個 profile 的失敗原因），附上最早可以 retry 的時間（`soonestCooldownExpiry`），讓 UI 可以顯示「我試了哪些選項，為什麼都失敗，30 秒後可以重試」。


**取捨**：靜默恢復讓使用者體驗更順暢，不需要理解底層的 credential rotation 細節。透明記錄讓診斷問題更容易，當所有選項都耗盡時，你能知道「為什麼」。


**Scenario**：消費者產品，你希望底層的複雜性對使用者透明。開發者工具或多 provider 管理場景，透明的失敗歷史讓你能快速判斷是 rate limit、billing 問題還是 model 下架。


---


## Migration Map：最誠實的結構 Diff


分析了六個分岔點之後，有一個地方可以讓這些差異變得更具體——hermes-agent 的 repo 裡有一個 `hermes claw migrate` 指令。它偵測到 `~/.openclaw` 目錄時，可以把 OpenClaw 的設定整包遷移過來。這個 migration script 本身就是兩個框架最誠實的「結構 diff」：能自動遷移的是兩者的共同概念，只能 archive 等待人工重建的，正好是前面說的根本差異點。


**能 1:1 遷移的：** SOUL.md（persona）、MEMORY.md 記憶條目、Skills、頻道整合設定（Telegram / Discord / Slack / WhatsApp）、Exec approval patterns → Hermes command_allowlist、MCP servers、session 設定。這些是兩個框架的共識——各自獨立踩到同樣的問題，收斂到同樣的設計。


**只能 archive、需要人工重建的：**


- **Plugin 設定** → hermes 沒有 OpenClaw 的 Plugin SDK 生態系，~100 個 plugin 的設定無處對應
- **Multi-agent list** → SubagentRegistry 的 persistent 設定搬不過去。hermes 的 `delegate_task` 是 in-memory，沒有對應的 registry config 可以接收
- **完整 Gateway config** → 只有 port 和 auth 能遷移，整個控制平面架構沒有 hermes 對應物
- **Memory backend 設定**（vector search、QMD、citations）→ hermes 沒有這些 backend 選項
- **UI / identity 設定** → hermes 是 CLI，沒有 UI theme 的概念


Multi-agent list 那個 archive 特別值得停下來看一下。SubagentRegistry 的 persistent 狀態之所以搬不過去，不是因為格式不同，而是因為 hermes 根本沒有「subagent 需要 persistent 狀態」這個設計假設。這不是遷移工具不夠好，是兩個框架在底層假設上就不同——migration script 只是把這件事說清楚了。


Memory backend 那個 archive 也反過來說明了一件有趣的事：hermes 的記憶體系統在召回機制上比 OpenClaw 豐富（三層架構、FTS5、Memory Fencing），但 OpenClaw 在 memory backend 的選項上比 hermes 多（vector search、QMD）。兩個框架的記憶體設計是「方向相反的豐富」——hermes 把複雜度放在「怎麼召回」，OpenClaw 把複雜度放在「怎麼儲存」。


---


## 根本問題的不同


把六個分岔點和 migration map 放在一起看，有一個更底層的差異開始浮現。


hermes-agent 在問：**「這個 Agent 能不能越用越好？」** 記憶體系統讓它記得你；Skill 系統讓它積累能力；RL 訓練迴路讓每一次使用都成為訓練資料。hermes 的設計重心是 Agent 和使用者之間的長期關係，以及 Agent 隨時間的演進。


OpenClaw 在問：**「這個系統在沒人看的時候能不能自己活下去？」** Orphan Recovery 讓 crash 後能恢復；Auth Profile Rotation 讓 rate limit 後能繼續跑；Exec Approval Flow 讓高風險操作需要人工確認；Compaction Checkpoint 讓壓縮失敗後能 rollback。OpenClaw 的設計重心是系統的韌性，以及在各種失敗情境下的自動恢復。


這兩個問題不是互相排斥的，但它們驅動了幾乎完全不同的設計優先順序。hermes 的記憶體設計、Skill 系統、RL 迴路，都在回答「怎麼讓 Agent 更了解你」；OpenClaw 的 Gateway 分層、Registry 持久化、Failover Chain，都在回答「怎麼讓系統在異常情況下繼續運作」。


---


## 幾個值得帶走的設計概念


**控制平面與執行引擎要不要分開？** 判斷點不是「這樣做是不是好設計」，而是「你的執行引擎多常需要獨立於基礎設施升級？」。如果答案是「從來不需要」，分層是複雜度，不是可靠性。


**Prefix Cache 是一個工程約束，不只是優化項目。** hermes 的做法是 system prompt 建一次永不重建，動態資訊注入進 user message；OpenClaw 的做法是 cache boundary 把 system prompt 切成靜態和動態兩段。兩個設計都在說同一件事：cache miss 的成本高到值得為它改變架構。


**記憶體是召回還是注入，反映的是對 Agent 定位的不同理解。** 記憶召回假設 Agent 是一個有連續性的個體，它應該「記得」過去發生的事；靜態注入假設 Agent 是一個工具，每次啟動都從明確的 context 開始。這不是技術問題，是產品問題。


**Agent Spawn 的失敗模式要在設計時就決定應對策略。** 同步阻塞把失敗收攏在 parent 的控制之下，代價是 parent 在等待期間無法做其他事；非同步背景把能力延伸出去，代價是需要完整的生命週期管理機制。兩個都是合理的選擇，但要在選擇之前就想清楚失敗發生時你要怎麼辦。


**安全邊界畫在 policy 層還是 infrastructure 層，強度不同。** Policy 可以被繞過（prompt injection、邏輯漏洞），infrastructure 限制（沒有網路介面、沒有文件系統權限）更難繞過。代價是靈活性：infrastructure 限制是二元的，policy 可以細緻調整。


---


## 不同場景需要多少 AgentOS？


這些設計概念是從真實的 production 痛點長出來的——但不是每個場景都會踩到同樣的坑。在用這兩個框架或借鑑它們的設計之前，值得先問：我的場景真的需要這個嗎？


**跑完就結束的 batch agent**（爬資料、跑報告、一次性自動化）：context 壓縮用不到，subagent lifecycle 管理用不到，memory 召回用不到。這類場景一個基本的 LangGraph graph + checkpointer 就夠。AgentOS 級的設計是過度投資。


**個人 coding assistant（單機、單人）**：exec 安全需要（但 policy 分類就夠，不需要 Docker air-gap），prefix cache 在意，memory 可能需要（記得你的 repo 結構和偏好）。接近 hermes 的核心用例——但不需要 Gateway 分層，不需要 Auth Profile Rotation，RL 迴路也多餘。


**24/7 多平台個人助理**（同時接 Telegram、WhatsApp、Slack，要求永遠在線）：這裡才開始需要 OpenClaw 級的設計。Channel lifecycle 管理、Auth Profile Rotation、Gateway 獨立重啟——這些在個人工具場景是過度設計，在這個場景是基礎條件。


**企業多租戶 agent 服務**（多個用戶、不可信任的任務輸入）：exec sandbox（Docker air-gap）的價值在這裡才完全展現。Policy 在多租戶場景下被繞過的風險高，infrastructure 層的隔離更可靠。Session isolation、owner-only tool gating 也在這裡變得重要。


**長時間 research / orchestration agent**（任務可能跑幾小時、需要 spawn 多個子任務）：context 壓縮是必要的，subagent spawn 的需求真實存在。但要 hermes 的同步 delegate_task 還是 OpenClaw 的 async lifecycle management，取決於子任務的時長。短時間平行任務（幾分鐘內完成）→ hermes 的同步設計夠用；長時間背景任務（跨 session 存活）→ 需要 persistent registry 和 orphan recovery。


這幾個場景排下來，大概可以看出一個規律：**AgentOS 的每一層設計，都是在回應一個具體的痛點**——不是通用的「好設計」，而是「這個痛點出現之後才需要的設計」。在痛點出現之前就引入這些機制，得到的是複雜度，不是可靠性。


---


> 讀完兩個框架，我的感受是：它們是同一批工程問題的兩種誠實回答。hermes-agent 在說「讓 Agent 和使用者一起成長」，OpenClaw 在說「讓 Agent 永遠在線」。這兩件事同樣重要，同樣困難，只是在選擇解哪個問題的時候，後面幾乎所有的設計決策就跟著定了。


## 延伸閱讀


- [Hermes-agent：從原始碼看一個為 Production 設計的 Agent 系統](/blog/hermes-agent-production-agent) — hermes-agent 完整分析：System Prompt 穩定性、Memory Fencing、RL 訓練迴路
- [OpenClaw：從原始碼看一個 Agent 平台的工程選擇](/blog/openclaw-agent) — OpenClaw 完整分析：Multi-Agent SessionKey、Auth Rotation、Exec Approval Flow
- [四個 Agent 框架，四種對「穩定性」的理解](/blog/agent-20260430) — 擴大到四個框架：CrewAI 和 Claude Code 加入後，「穩定性」的定義更清晰了

  
  
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

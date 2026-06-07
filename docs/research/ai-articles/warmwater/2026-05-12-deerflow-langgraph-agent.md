---
url: "https://warmwater.dev/blog/deerflow-langgraph-agent"
title: "DeerFlow：從原始碼看 LangGraph 為 Agent 系統帶來了什麼，又留下了什麼"
date: 2026-05-12
category: Source Code
source: warmwater.dev
---

[
← Source Code ](/blog?tag=Source%20Code)  Source Code  
#  DeerFlow：從原始碼看 LangGraph 為 Agent 系統帶來了什麼，又留下了什麼 
  2026-05-12 · — views      

讀 DeerFlow 的架構圖，我在一個數字上停下來：12。


不是 12 個工具，不是 12 個 API endpoint——是 12 層 Middleware，每一次模型呼叫都要完整走過一遍。這個數字讓我問了一個不一樣的問題：選 LangGraph 當 runtime，到底替你決定了哪些事？剩下的，還是要自己解決。


DeerFlow 是一個 Python 寫的 AI Agent 系統，底層跑在 LangGraph 上，上面有完整的 Middleware 鏈、沙箱執行環境、LLM 驅動的記憶體系統，以及 Subagent 並發架構。它和 hermes-agent 解決的是同一個問題：讓 Agent 能夠穩定、安全、長期地跑在 production 環境裡。但它們的選擇完全不同。


**讀完這篇，你會理解：**


- DeerFlow 怎麼用 LangGraph 的 StateGraph、Checkpointing、Annotated reducer 當骨架，以及這些機制各自解決什麼問題

- 12 層 Middleware 的排序為什麼本身就是一個設計決策，兩種 hook 各自攔截什麼層面的行為

- `Command(goto=END)` 如何在不丟失任何狀態的情況下暫停執行中的 Agent，讓用戶回覆後從原點繼續

- 虛擬路徑映射為什麼同時解決了隔離、安全、可移植三個問題

- LLM 驅動的 Memory 更新和 rule-based extraction 的本質差異

- 框架 vs 自建這道選擇題，在 AI coding 工具和 RL 訓練迴路普及的今天，答案正在怎麼變


這篇是原始碼分析，不是 LangGraph 的教學，也不是 DeerFlow 的使用指南。是拆開幾個關鍵設計機制，試著解釋選擇背後在想什麼。

---


## 選 LangGraph 當 Agent 骨架：買進了什麼


DeerFlow 的核心執行邏輯，本質上是一個 LangGraph `StateGraph`，兩個節點：`call_model` 和 `tools_node`，一個條件邊——有 tool call 就去 tools，沒有就結束。整個 Agent 主循環就是這樣。


選 LangGraph 不只是選了一種圖的寫法，它同時買進了三件在 Agent 系統裡很難自己做好的東西。


**Checkpointing**。每一個 step 執行完，LangGraph 自動把 `ThreadState` 存起來。這不只是容錯機制，它是後面所有 interrupt/resume 行為的地基。`ClarificationMiddleware` 之所以能讓 Agent「暫停等用戶回覆」，完全是建立在 Checkpointing 上面的，後面會看到細節。


**`Annotated` reducer**。LangGraph 裡，`ThreadState` 的每個欄位可以綁定自訂的合併邏輯。DeerFlow 用這個機制解決了一個 Subagent 並發時才會出現的問題：兩個子 Agent 同時更新 `artifacts` 列表，怎麼合併？預設行為是後者覆蓋前者，資料會丟。DeerFlow 的 `merge_artifacts()` 以 ID 為 key 做去重合併，確保兩邊的結果都保留。`viewed_images` 更特別：`right=[]` 被當作「清除信號」（wipe sentinel），讓 Sandbox 能明確表達「重置這個列表」的語義，而不是「新增一個空列表」。這個細節不在 LangGraph 文件裡，是 DeerFlow 自己發現然後解決的邊緣情況。


**雙伺服器架構**。DeerFlow 跑兩個 server：LangGraph Server 在 port 2024，負責 Agent 執行、SSE streaming、Thread/Run 管理；Gateway API（FastAPI）在 port 8001，負責 Memory CRUD、Skills 管理、MCP 熱重載、檔案上傳。兩者透過 Nginx 反向代理統一對外，透過共享檔案系統溝通，不需要直接 RPC。分開的原因直接：Memory 和 Skills 需要自己的 REST 端點，這些業務邏輯放進 LangGraph Server 不合適。LangGraph 處理它擅長的，FastAPI 處理外圍的。

---


## 12 層 Middleware：排序本身就是設計


12 不是隨機的數字。DeerFlow 的 Middleware 鏈有嚴格的依賴順序：Guardrail 必須在 Memory 前、Memory 必須在 LoopDetection 前、Clarification 永遠最後。改變這個順序，系統行為就會出問題。


層序Middleware必須在誰之前原因1-2Logging, Tracing—觀測層，順序不影響行為3ContextInjection—注入系統時間、用戶偏好4RateLimit—流量控制5**Guardrail**Memory惡意工具呼叫不應污染記憶體6**Memory**LoopDetection偵測器需要完整 context7**LoopDetection**Clarification全局模式分析8-10Summarization, TodoList, SubagentLimit—輔助功能11ImageContext—視覺上下文12**Clarification**(最後)其 Command(goto=END) 是最終仲裁


這是 Chain of Responsibility 模式，但比教科書版本多了一個重要維度：每個 Middleware 要宣告它攔截的是哪個層面的行為。


**兩種 hook 的分工**是這個系統最值得注意的設計。`wrap_tool_call` 攔截的是單一工具呼叫的前後，`GuardrailMiddleware` 用這個 hook，因為它要在每個工具執行前做安全檢查，出問題就擋下那個工具。`after_model` 攔截的是模型輸出後、工具執行前的這個時間點，`LoopDetectionMiddleware` 用這個 hook，因為它要看的是整批 tool calls 的模式——只看單一工具呼叫，看不出迴圈。


`GuardrailMiddleware` 有一個設計決策值得特別說：被攔截的工具呼叫，它不拋例外，而是返回一個帶有拒絕原因的 `ToolMessage`。這讓模型能看到「這個操作被拒絕了，原因是 XXX」，然後自己決定下一步——換工具、詢問用戶、或放棄。拋例外會中斷整個 Agent 執行，讓模型看到錯誤訊息讓它能自我修正。另外，`fail_closed=True` 是預設：安全規則引擎如果崩潰，DeerFlow 選擇拒絕執行，寧可誤殺，不可放行。


`LoopDetectionMiddleware` 用雙層偵測：第一層看 hash（最近 20 次 tool calls 的內容是否完全重複），第二層看頻率（某個工具是否被呼叫太多次）。偵測到之後，它不回傳 `Command(goto=END)` 讓 Agent 停下來，而是注入一條 `HumanMessage` 告訴模型「你在重複，試試別的方法」，讓模型自己調整策略。這裡藏著一個 Anthropic API 的細節：Claude 要求 Human/AI 訊息必須交替排列，所以注入的是 `HumanMessage` 而不是直接修改 `AIMessage`——不符合格式的訊息會讓 API 回錯誤。

---


## `Command(goto=END)` 不是結束，是暫停


`ClarificationMiddleware` 永遠是 Middleware 鏈的最後一層，因為它的 `Command(goto=END)` 是最終決策——前面任何一層都可以中斷流程，但 Clarification 是「整個圖的出口判斷」，必須在最後才有意義。


它做的事很單純：如果模型呼叫了 `ask_clarification` 這個工具，就回傳 `Command(goto=END)`，告訴 LangGraph 把圖停在這裡。「停在這裡」是 LangGraph 的關鍵機制——它不是終止，是暫停。LangGraph 在收到 `Command(goto=END)` 後，會先把完整的 `ThreadState` 存進 checkpoint，然後才停。這個 state 包含了完整的對話歷史、目前的 artifacts、所有 Middleware 的內部狀態。


完整流程是這樣的：


- 模型決定需要確認，呼叫 `ask_clarification("請確認目標環境是哪一個")`

- `ClarificationMiddleware` 偵測到，回傳 `Command(goto=END)`

- LangGraph checkpoint 存下完整的 `ThreadState`

- SSE 事件推給前端，用戶看到澄清問題

- 用戶輸入回覆，送出新請求

- LangGraph 從 checkpoint restore `ThreadState`，從 `call_model` 節點繼續執行

- 模型看到用戶的回覆，接著跑完剩下的任務


整個過程沒有重頭來過，沒有丟失任何狀態。這個機制如果要自己實作，需要自建 state serialization、interrupt 信號、resume 邏輯。LangGraph 把這些一次打包進 Checkpointing，大概是 DeerFlow 選 LangGraph 最具體的收益之一。
  Command(goto=END) — 暫停與恢復流程    Agent  ◉ 模型呼叫 ask_clarification
「請確認目標環境是哪一個」  ↓    ⬡ ClarificationMiddleware 偵測到
return Command(goto=END)  ↓   PAUSE  ◈ LangGraph Checkpointing
ThreadState 完整存檔，等待恢復  ↓   SSE  ▷ 前端收到澄清問題
用戶看到問題，等待輸入  ↓    ✦ 用戶輸入回覆
POST /threads/{id}/runs  ↓    ⇄ 從 Checkpoint 恢復 ThreadState
不是重頭來過，是接續跑  ↓   Resume  ◉ 從 call_model 節點繼續執行
模型看到用戶回覆，任務繼續      

---


## Agent 看到的路徑是假的


DeerFlow 的 Sandbox 系統做了一件在設計上很乾淨的事：Agent 看到的檔案路徑，和真實磁碟路徑完全不同。


`/mnt/user-data/uploads/report.xlsx` 在 Agent 眼裡是一個合理的路徑。但 Sandbox 在執行任何檔案操作時，會把它轉換成 `threads/{thread_id}/user-data/uploads/report.xlsx`——真實的磁碟路徑帶著 thread ID。


這個虛擬映射同時解決了三個問題：**隔離性**，每個對話 session 有獨立的目錄，不同 session 的檔案不會互相污染；**安全性**，Agent 只能存取映射範圍內的路徑，無法透過路徑穿越（`../../etc/passwd`）存取系統檔案；**可移植性**，Agent 的 prompt 和邏輯裡都是虛擬路徑，同一份 code 部署在本機或雲端，Agent 的視角完全一致。


工具的組織方式也反映了同樣的模組化邏輯。DeerFlow 的工具分三種來源：Builtin（永遠可用，`ask_clarification`、`present_file` 這些）、Configured（YAML 配置，透過 `resolve_class()` 反射 import）、MCP（外部工具伺服器，熱重載）。


MCP 熱重載的實作細節值得說：Gateway API 把新的 MCP server 配置寫入 `extensions_config.json`，LangGraph Server 在下次 Agent 執行時讀取這個檔案的 mtime，發現變了就重新初始化 `MultiServerMCPClient`，新工具出現在工具清單裡，不需要重啟任何進程。


當 MCP 工具數量多到幾十甚至上百個，把所有 tool schema 都塞進 prompt 很浪費。DeerFlow 的 `DeferredToolRegistry` 讓 MCP 工具延遲載入：模型先呼叫 `tool_search("我需要一個能查股票的工具")` 找到相關工具，再實際呼叫它。不需要的工具不佔 context window。

---


## 讓 LLM 決定要記什麼


DeerFlow 的 Memory 系統有三個區塊：`user`（用戶基本資料和偏好，穩定不常變）、`history`（近期話題和上下文摘要，每次對話後更新）、`facts`（具體技術事實，每次工具執行後更新，帶 confidence score）。


有意思的是更新邏輯。DeerFlow 不是用 rule-based extraction（定義 pattern，從對話裡抽取符合的片段存起來），而是用 LLM 分析整段對話後，決定要更新哪些東西。


LLM-driven 的好處是能理解語義。「你之前說你喜歡簡短的回答，但這次你讓我寫得詳細一點」，rule-based 很難捕捉這種矛盾和更新，LLM 可以。更有意思的是**信號偵測**：`MemoryUpdater` 在更新前，會先偵測對話最後的 HumanMessage 包含什麼信號。


信號觸發詞（部分）LLM 被指示做什麼`correction`不對、你搞錯了、incorrect更激進地修正 Memory 裡的錯誤 facts`reinforcement`對、就是這樣、remember this提高相關 facts 的 confidence，確保寫入`neutral`（其他）正常增量更新，不刪除既有資訊


記憶的更新策略不是固定的，而是根據用戶的回饋動態調整。


還有一個細節：Memory 更新前，所有訊息裡的 `/mnt/user-data/uploads/` 路徑都會被替換成 `[uploaded file]`。上傳路徑是 transient 的——用戶下次上傳同一份文件，路徑會變。如果把路徑存進 Memory，下次 Agent 找這個路徑會找不到，反而造成混淆。記下「用戶曾上傳一份 Excel 財報」就夠了，不需要記路徑。


Facts 也有驅逐機制：超過 `max_facts` 上限時，confidence 最低的 facts 先被移除。Memory 不是無限累積，而是保留最確定的知識。`FileMemoryStorage` 的實作用了兩個小設計：mtime-based cache（如果檔案的修改時間沒變，直接用 in-memory cache，不讀磁碟）和原子寫入（先寫 `.tmp` 檔，完成後 rename，避免寫到一半系統崩潰導致 Memory 損壞）。這些都是「長期跑著」才會踩到的問題。

---


## 框架 vs 自建：這道選擇題的答案正在改變


DeerFlow 和 hermes-agent 解決的是同一批問題，但選擇了不同的路線。從三個維度來看：


框架路線（DeerFlow）自建路線（hermes-agent）新人成本讀 LangGraph 文件讀你的 run_conversation()出問題時Stack Overflow / Discord 有人只有你自己三個月後的你還看得懂看不懂自己寫的


技術孤島是自建路線真正的代價，比維護成本更難量化，實際影響更深遠。


`hermes-agent` 這種專案，如果核心作者離開，接手成本是指數級的。這不是誇張——`run_conversation()` 裡面每一個 edge case 的處理，背後都有一段踩坑的歷史，沒有文件，沒有 issue tracker，就在那幾百行代碼裡。新人接手後，為了繞過看不懂的邏輯加 workaround，系統的複雜度只會累積，不會減少。


技術孤島的影響不止於人員流失，還有兩個面向。第一是招聘難度：面試問「你有 LangGraph 或 LangChain 的經驗嗎」，市場上有一批人可以答；問「你有我們自己的 run_conversation() 框架的經驗嗎」，答案是零。每個新人都需要幾週才能看懂架構，更別說改它。第二是 AI coding 工具的支援差距：LangGraph 的 API 和 pattern，Claude Code 或 Cursor 都能理解；你自建的框架，AI 要先讀懂才能幫你，這讓開發效率的差距會持續拉大。選框架，知識是可以共享和流通的，問題能在社群找到解法。選自建，每個維度都要靠自己積累，而且這份積累不跟著市場走。


框架買進的東西需要說清楚，留下的也是。對照 hermes-agent 的 agentic loop 設計，幾件 production 裡真實需要的東西，LangGraph 是沒有意見的：


- **工具分類與平行安全**：哪些工具可以平行執行（`PARALLEL_SAFE`），哪些必須序列化（`PATH_SCOPED`），哪些完全禁用（`NEVER`）——LangGraph 的 `tools_node` 不管這件事

- **API 錯誤分類**：timeout 要 retry，context 超長要壓縮，憑證過期要輪換——這種細粒度的錯誤分類和對應策略，框架沒有做

- **優雅的 budget 耗盡**：token 快用完時，用 LLM 總結目前進度再收尾，而不是硬截斷——這是業務意見，框架不知道

- **硬中斷的 fan-out 取消**：有 Subagent 在跑時被 interrupt，怎麼廣播取消信號到所有並發 thread——LangGraph 有 interrupt 機制，但多 executor 的協調要自己管

- **Middleware 鏈**：DeerFlow 的 12 層，LangGraph 提供了 hook point，但鏈的排序約束、hook 類型選擇，是 DeerFlow 自己設計的


DeerFlow 的 12 層 Middleware 不是偶然——它是在 LangGraph 的 hook point 上，用自己的業務意見蓋出來的一層。框架提供插入點，你決定插入什麼。這也是為什麼說「選 LangGraph 不等於不需要解決這些問題」——它解決了骨架，神經系統還是要自己長。


框架路線有一個真實的風險。LangGraph 的 breaking change 問題不是小事。0.x 升 1.x 的時候，很多人的 StateGraph 直接壞掉。這在企業環境裡是真正的維護地獄：你的 on-call 不是因為業務邏輯出問題，而是因為 upstream 改了 API。LangGraph 的 issue tracker 裡有大量這類回報，這是選框架必須接受的現實，不是可以忽略的小細節。


所以我自己的判斷是：框架用於骨架，自建用於神經系統，才是比較成熟的做法。


LangGraph 管 graph topology、Checkpointing、SSE——這些是「框架的意見」，讓框架來管沒有問題。但 prefix cache 優化、Credential Pool、RL 訓練迴路這些「你的系統才有的意見」，不要嘗試讓框架來管，自己包一層，讓它對 LangGraph 一無所知。這樣框架升版的時候，你只需要改最底層的介面，不需要碰業務邏輯。
  LangGraph routes — Your code runs inside    LangGraph  START  ↓  call_model LLM inference  ↓ has tool_calls? ↓ yes  tools_node execute tool calls  ↓  → call_model loop back  ↓ no tool_calls  END checkpoint saved          Your Code  before_model  Memory inject Context inject Rate limit     after_model hook  Loop detection Clarification Summarization     wrap_tool_call hook  Guardrail Sandbox Logging     after tool  Memory update RL trajectory       LangGraph Runtime (always on)  Checkpointing SSE Streaming Thread / Run Mgmt Annotated Reducer   LangGraph owns the routing. Your code owns what happens inside each step.  


**再加一個讓框架路線的 breaking change 問題更好處理的實務建議**：把對 LangGraph API 的依賴集中在一個模組裡。DeerFlow 的 `make_lead_agent()` 其實就是在做這件事——所有 LangGraph 的組裝邏輯在這個工廠函數裡，上層的 Middleware 只知道它被注入了，不知道 LangGraph 的存在。這個隔離不完美，但方向是對的。


**如果是我**，站在 2026 年求職或組建小團隊的角度：


主幹用 LangGraph，因為這是現在的通用語言，面試能說，團隊能招到有經驗的人，社群生態（LangSmith 監控、OTel 整合、active Discord）是實質的開發效率優勢。把「hermes-agent 那些框架外的需求」封裝成獨立模組，不讓它跟 LangGraph 耦合——RL 訓練迴路、自訂 Memory 邏輯、token cost 優化，這些寫成可以抽換的 adapter，而不是直接長在 StateGraph 裡面。


**但有一個變數正在改變整道題的答案。**


AI coding 工具讓自建的成本快速下降。hermes-agent 那樣的主循環，在兩年前要幾個月才能打磨穩定；現在用 Claude Code 幾個小時能出可用版本。自建的「代價」縮小，框架的 lock-in「代價」相對放大，這個剪刀差正在拉開。


同時，hermes-agent 最特別的設計——把對話 trajectory 存成 ShareGPT 格式送進 Atropos RL 訓練 pipeline——不是一個功能，是一個商業模式假設：「每次使用都在積累讓模型更了解你的 domain 的訓練資料」。LangGraph 沒有辦法 native 支援這件事，因為這是框架設計視野之外的需求。如果未來 AI 產品的核心競爭力是「你的模型比對手更懂你的業務」，那擁有 runtime 的控制權、能決定訓練資料怎麼收集和什麼粒度，會是很實質的優勢。


最後一個反直覺的觀點：我認為最後站穩的框架，不會是 API 最豐富的那個，而是「暴露最乾淨的 runtime primitive、最少應用層意見」的那個。LangGraph 的 `StateGraph + Checkpointing` 是好的 primitive；但它上面堆的那些 abstraction 已經引發過一輪反彈。下一個大挑戰者可能是更薄的 runtime layer，讓你自己決定要在上面蓋什麼，而不是替你決定好一切。DeerFlow 其實已經在做這件事了：用 LangGraph 當地基，然後在上面蓋自己的 12 層。

---


> 


**結語**：DeerFlow 最讓我印象深刻的不是某個單一機制，而是它的架構選擇揭示了一件事：選框架不是選「我不需要解決這些問題」，而是選「這些問題，我讓框架幫我解決」。哪些問題值得外包，哪些值得自己掌控——這才是做 Agent 系統架構時真正的選擇。


## 延伸閱讀


- [hermes-agent：從原始碼看一個為 Production 設計的 Agent 系統](/blog/hermes-agent-production-agent) — 對照版：同樣的問題，不使用框架的 hermes-agent 給出了什麼答案
     [ Source Code ](/blog?tag=Source%20Code)[ Agentic System ](/blog?tag=Agentic%20System)  
### 
相關文章

[System DesignAgent 要怎麼進化？六個系統的 Self-Improvement 機制比較2026-05-22](/blog/agent-self-improvement-design-comparison)[System DesignSOUL 設計決定了 Agent 是什麼：六個 Agentic System 的 system prompt 比較2026-05-22](/blog/agent-soul-design-comparison)[Source Code不預裝能力，只定義生長方式：GenericAgent 原始碼解析2026-05-22](/blog/generic-agent-source-code)

---
url: "https://warmwater.dev/blog/openclaw-agent"
title: "OpenClaw：從原始碼看一個 Agent 平台的工程選擇"
date: 2026-04-25
category: Source Code
source: warmwater.dev
---

[
← Source Code ](/blog?tag=Source%20Code)  Source Code 
 
# OpenClaw：從原始碼看一個 Agent 平台的工程選擇
 
 2026-04-25 · — views  
  
  
讓 Agent 回答一個問題不難。讓 Agent 同時接收 Telegram、WhatsApp、Slack 的訊息、在背景跑著幾個子 Agent、API Key 被 rate-limit 時自動換一個、Gateway 重啟後把還沒完成的任務撿回來繼續跑——這些加在一起，就不是一個 Agent 能解決的問題了，需要的是一個平台。


OpenClaw 的原始碼大概就是在解這件事。500+ 個 TypeScript 文件、100 個 plugin、20 種以上的訊息平台整合、40+ 個 LLM provider、一套完整的 WebSocket RPC 協議——這些數字背後，是一個一直在問同一個問題的設計：「這個系統在沒人看的時候，能自己活下去嗎？」


這篇想拆開幾個關鍵機制，試著解釋每個選擇背後在想什麼。


**讀完精華版（2 分鐘），你會理解：**


- OpenClaw 的 Gateway 是什麼，為什麼這個系統把「控制平面」和「執行引擎」分開
- Multi-Agent 的 SessionKey 編碼設計，以及 AnnounceFlow 如何讓 parent/child agent 非同步協作
- Auth Profile Rotation + Model Fallback Chain：「零人工介入高可用」的具體實現
- Exec Approval Flow 和 Sandbox：Agent 有能力跑任意命令，這條線怎麼拉
- Identifier-Preserving Compaction：壓縮對話歷史時，UUID 是最危險的東西


---


## 精華版


| 設計維度 | 核心機制 | 解決的問題 | 失敗時的行為 |
| --- | --- | --- | --- |
| 架構分層 | Gateway / Runner 分離 | 控制平面可獨立重啟，不影響執行中的 session | Gateway crash → Runner 的 session 狀態從 DB 恢復 |
| Multi-Agent 協調 | SessionKey 編碼 + AnnounceFlow | 子 Agent 樹的深度與身份不需查 DB 就能讀出 | Orphan Recovery 補發未交付的結果 |
| 高可用 API 存取 | Auth Profile Rotation + Fallback Chain | 單一 key 被 rate-limit 不造成服務中斷 | Probe slot 持續探測，最早可恢復的 key 優先帶回 |
| 執行安全 | FS Policy / Tool Policy / Exec Approval / Sandbox | 四層由細到粗，最後一層是 infrastructure air-gap | network_mode: none 不可被 prompt injection 繞過 |
| 對話壓縮安全 | Identifier-Preserving Compaction + Checkpoint | LLM 摘要時不截斷 UUID、IP、檔名等識別符 | 壓縮失敗 rollback 到快照，不留中間狀態 |


**Gateway / Runner 分層**：控制平面（channel 管理、auth、session store）和執行引擎（跑 Agent turn）分開部署，Gateway 重啟不中斷正在執行的 session，因為狀態存在資料庫而非記憶體。


**SessionKey 編碼**：一個 string 同時編碼 agent 身份、所屬 session、subagent 樹深度，任何地方看到 SessionKey 不查 DB 就能判斷它是誰的、是不是 subagent、在第幾層。


**Auth Profile Rotation**：每個 LLM provider 可設定多組 API key，選 key 的邏輯依 `lastGood` 時間戳和 cooldown 狀態排序；當所有 key 都在 cooldown，自動往 Fallback Chain 試下一個 model，失敗才拋出帶有 `soonestCooldownExpiry` 的結構化 error。


**Exec Approval Flow**：四道防線依序是 FS Policy（路徑隔離）、Tool Policy（per-agent allow/deny）、人工確認通知（高風險命令執行前推送通知等待 approve）、Docker sandbox（`network_mode: none` 的 infrastructure air-gap）。


**Identifier-Preserving Compaction**：LLM 做摘要時傾向縮短識別符，OpenClaw 在壓縮 prompt 裡明確指定保留 UUID、hash、IP、port、URL、檔名，並用 Compaction Checkpoint 確保壓縮失敗不留損壞的中間狀態。


---


**Q：為什麼 Gateway 和 Runner 要分開，而不是一個 process？**


Gateway 重啟時不能中斷正在跑的 Agent session。把狀態存在資料庫、把執行引擎分開，讓控制平面可以做滾動升級或從 crash 恢復，不影響 in-flight 的執行。


**Q：SessionKey 的深度編碼有什麼實際用途？**


防止 subagent 無限遞迴 spawn。拿到 SessionKey 就能直接計算當前深度，不需要遍歷資料庫，Gate 可以在 spawn 前直接拒絕超過 `MAX_SUBAGENT_SPAWN_DEPTH` 的請求。


**Q：所有 API key 都 cooldown 時，系統怎麼恢復？**


Transient cooldown probe slot 保留一個 profile 持續試探，probe 成功就把那個 key 提前帶出 cooldown。不需要人工介入，也不需要等所有 cooldown 同時到期。


**Q：為什麼壓縮時 UUID 比普通文字更危險？**


UUID 截斷後在語意上仍然「看起來正確」，Agent 不會感知到識別符已經被改掉，直到它用截斷的 ID 去查資料庫或呼叫 API 才會出錯——而且這類 bug 只在 context 被壓縮過之後才出現，很難重現。


---


> 
以下是完整版，按需取用。


## Gateway：不只是一個 HTTP Server


多數 Agent 框架的結構很扁平：一個主迴圈，負責呼叫 LLM、執行工具、管理狀態。OpenClaw 的第一個不同，是它把系統切成兩層。


**Gateway** 是控制平面，負責的事情包括：管理所有 channel 的生命週期（Telegram bot、WhatsApp、Slack 帳號……），對外暴露 WebSocket RPC 介面，處理使用者認證，維護 session store，管理 cron job 和 hook runner。它本身不跑 Agent，它是 Agent 跑起來所需要的基礎設施。


**pi-embedded-runner** 是執行引擎，負責的事情只有一件：給定一個 session，跑一個 Agent turn，回傳結果。


這個切分不只是組織程式碼的方式，它的實際效果是：Gateway 可以獨立重啟、獨立升級，不影響正在執行的 Agent session（session 狀態存在資料庫，不在記憶體裡）。而 Agent 的執行邏輯可以被替換，不影響 channel 整合和 auth 設定。


**WebSocket Named-Method RPC** 是 Gateway 和客戶端通訊的協議，而不是 REST。原因直接：REST 是請求-回應模式，不支援 server 主動推送。Agent 跑起來之後，Gateway 需要把 streaming 的 token 輸出推給客戶端、需要把 subagent 的狀態更新廣播出去——這些都需要雙向的長連接。協議格式很簡單：


```
RequestFrame:  { id: string, method: string, params: unknown }
ResponseFrame: { id: string, ok: boolean, result?: unknown, error?: string }
EventFrame: { event: string, payload: unknown }  // Server → Client push

```


Channel 管理這一塊有一個細節值得說：每個 channel plugin（Telegram、WhatsApp 等）都有自己的生命週期，Gateway 有一套 health monitor 在追蹤它們的狀態。當 channel 連線斷開，不是直接 restart，而是走 exponential backoff：起始 5 秒，每次翻倍，最多等到 5 分鐘，最多重試 10 次。超過次數進入 `PERMANENTLY_FAILED` 狀態。某些錯誤（例如 auth 失效）會直接 bypass backoff，因為重試沒有意義。這不是新的設計，但它是「讓系統在凌晨 3 點不需要人處理」的基礎建設。


Lane 系統也在這一層管理：Session lane 確保同一個 session 的請求串行執行（不會兩個 turn 同時跑），Global lane 限制整體的 Agent 執行並發。這兩層加在一起，防止的是「使用者同時送兩條訊息」造成 session 狀態競爭的問題。


---


## SessionKey 與 Multi-Agent 生命週期


OpenClaw 支援 multi-agent：一個 parent agent 可以 spawn subagents，subagents 可以再 spawn subagents，形成一棵樹。這本身不稀奇，但 OpenClaw 在這裡有一個設計細節很值得看：**SessionKey**。


SessionKey 是一個 string，格式大致是這樣：


```
agent:main:main // 預設的主 session
agent:<agentId>:<sessionKey> // 普通 session
agent:<agentId>:<agentId>:<depth> // subagent session

```


它在一個 string 裡編碼了三件事：agent 的身份、這個 session 屬於哪個 agent 的哪個 session、以及在 subagent 樹裡的深度。任何地方看到 SessionKey，不用查資料庫就能知道這個 session 是誰的、是不是 subagent、在第幾層。


**Subagent Spawn 的流程**大概有 8 個步驟，每一步都在防一件具體的事：


- 決定 subagent 用哪個 model（允許繼承 parent model 或指定新的）
- 取得當前 depth，**檢查是否超過 `MAX_SUBAGENT_SPAWN_DEPTH`**（防止遞迴 spawn 無限展開）
- 計算當前 session 的 active subagents 數量，**檢查是否超過 `MAX_CHILDREN_PER_AGENT`**（防止 fan-out 爆炸）
- 決定 workspace 繼承（subagent 用 parent 的工作目錄，還是新建一個）
- 複製 parent 的 attachments 到 subagent workspace
- 組裝 subagent 的 system prompt（包含 parent context）
- 在 session store 建立 subagent session 記錄
- 在 SubagentRegistry 登記，然後非同步啟動


SubagentRegistry 是整個 multi-agent 系統的狀態表。它追蹤每個 subagent run 的生命週期（`PENDING → RUNNING → COMPLETE | ERROR | KILLED`），並且把這個狀態持久化到磁碟。這個持久化很重要，原因在下面。


**AnnounceFlow** 是 subagent 把結果交回 parent 的機制。設計上是非同步的：subagent 完成後，不是直接寫進 parent 的 context，而是放進一個 announce queue，等 parent session 的下一個 turn 來時再讀取。原因是：如果 parent 在等 subagent 完成的過程中 blocking，它就沒辦法處理其他事情（例如接收使用者的中止指令）。非同步 deliver 讓 parent 保持活躍。


**Orphan Recovery** 是這個設計裡最 production-grade 的部分。假設 Gateway 在某個 subagent 正在執行的時候 crash 了。重啟之後，Gateway 會從磁碟恢復 SubagentRegistry 的狀態，找到所有「孤兒」subagent，然後根據它們 crash 前的狀態決定怎麼處理：


- **已完成但還沒 announce**：補發 announce，把結果還給 parent
- **Crash 時正在跑**：標記為 ERROR，通知 parent
- **還沒啟動**：清理或重啟


沒有這個機制，Gateway 每次重啟就會丟失所有 in-flight 的 subagent 狀態。有了它，重啟變成了一個可以恢復的事件，而不是一個會造成資料遺失的事件。


---


## 零人工介入的高可用設計


生產環境的 Agent 有一個常見的脆弱點：它依賴單一的 API Key。Key 被 rate-limit 了，Agent 就停了。OpenClaw 的設計目標是讓這件事不需要人工介入就能自動恢復。


**Auth Profile Store** 允許每個 provider 設定多個 API Key（多個 Profile）。選擇哪個 key 的排序邏輯大致是：最近成功使用過的排前面（`lastGood` 時間戳）、cooldown 還沒過期的排後面、其他的按 round-robin（`lastUsed` 最舊的排前面）。每次 API 呼叫成功會更新 `lastGood`，失敗會設定 cooldown（不同的失敗原因有不同的 cooldown 時長）。


當所有 Profile 都在 cooldown 時，OpenClaw 不是直接報錯，而是嘗試 **Model Fallback Chain**：


```
models:
  providers:
 - id: anthropic
 models:
 - id: claude-opus-4-6
 fallback:
 - id: claude-sonnet-4-6
 - id: claude-haiku-4-5

```


Primary model 失敗 → 試 fallback list → 全部失敗才拋出 `FallbackSummaryError`。這個 error 的設計很細緻：它不只說「失敗了」，它收集了每一次嘗試的原因（rate_limit / auth_error / billing / model_not_found / timeout / overload），還附上最早可以 retry 的時間（`soonestCooldownExpiry`）。這讓 UI 可以顯示「所有 model 都嘗試過，30 秒後可以重試」，而不只是一個沒有上下文的 error。


還有一個細節：**Transient cooldown probe slot**。當所有 Profile 都進入 cooldown，OpenClaw 不會讓所有 key 同時靜止等待，而是保留一個 profile 持續試探——如果 probe 成功，可以提前把那個 key 帶出 cooldown，讓系統更快恢復。


---


## Exec Approval Flow 與 Sandbox


Agent 有能力執行任意 bash 命令。這是功能，但也是風險。OpenClaw 在這件事上設了四道防線，從最細到最粗：


**第一道：FS Policy**——file 工具只能操作 workspace 目錄內的路徑，防止 path traversal 到系統敏感目錄。


**第二道：Tool Policy**——config 可以設定 per-agent 的 tool allow/deny list，甚至支援 tool group（一次 deny 整類工具）。某些工具（`cron`、`gateway`）只有 owner（session 的擁有者）才能呼叫，在多人共用的 channel（例如 Telegram group）裡，非 owner 呼叫這些工具會直接拒絕。


**第三道：Exec Approval Flow**——高風險命令在執行前需要人工確認。流程是：Agent 準備執行命令 → 建立 approval request（含命令預覽）→ 推送 iOS 通知給 operator → 等待 approve 或 deny → 才決定是否執行。這個流程本身可以設定哪些命令需要 approval、哪些可以自動通過，讓安全和效率之間有調節空間。


**第四道：Sandbox**——Docker container 隔離，預設 `network_mode: none`。


最後這一點值得多說一句。把網路設成 `none`，不是 policy（「你不應該連外網」），而是 infrastructure 層的 air-gap（「你在物理上無法連外網」）。LLM 的 prompt injection 攻擊可能讓 Agent 繞過 policy，但無法繞過沒有網路介面這件事。


這一層還有一個附帶設計值得一提：tool call 的 ID 是用 hash 生成的，不是 UUID。原因是：如果 API 呼叫失敗需要 retry，用 UUID 的話每次 retry 的 tool call ID 都不同，Anthropic 的 prefix cache 就會失效。hash-based ID 確保相同的 tool call 在 retry 時產生相同的 ID，cache 繼續命中。


---


## Identifier-Preserving Compaction


Context window 壓縮是長期 Agent 的必要機制，但它有一個不明顯的風險：**LLM 在做摘要的時候，傾向於讓輸出「更易讀」，而「更易讀」有時候意味著縮短或重構識別符。**


舉幾個具體的情境：


```
壓縮前：「請幫我刪除 session ID 為 550e8400-e29b-41d4-a716-446655440000 的記錄」
壓縮後（LLM 自作主張）：「請幫我刪除 session 550e84... 的記錄」
→ Agent 用截斷的 ID 去查資料庫，查無此 session

壓縮前：「SSH 連線目標是 192.168.1.105:2222，使用者 deploy」
壓縮後：「SSH 連線目標是 192.168.x.x，使用者 deploy」
→ Agent 嘗試連接一個不存在的 IP

壓縮前：「下載 deploy-config-2026-04-21-v3.yaml 並執行」
壓縮後：「下載 deploy-config.yaml 並執行」
→ 找不到檔案，或找到了舊版本

```


這些 bug 有一個共同特點：它們只在 context 被壓縮過之後才會出現，而且 Agent 不會知道識別符已經被改掉了。


OpenClaw 的解法是 **Identifier Preservation Policy**，預設是 `strict`：


```
type AgentCompactionIdentifierPolicy = "strict" | "off" | "custom"

// strict 的指令大意是：
// "Preserve all opaque identifiers exactly as written
//  (no shortening or reconstruction) —
//  UUIDs, hashes, IDs, hostnames, IPs, ports, URLs, filenames"

```


壓縮時把這條指令帶進 LLM 的摘要 prompt，告訴它：這些東西不能改，一字不差地保留原文。


除了識別符保留，壓縮還有另一個工程問題：**原子性**。LLM 生成摘要可能失敗（API timeout、rate limit），如果失敗發生在舊 context 已經被刪掉、新的摘要還沒建立的中間狀態，session 就壞了。OpenClaw 的解法是 Compaction Checkpoint：壓縮前先保存快照，失敗就 rollback，確保不留中間狀態。


最後一個機制：**Heartbeat + Cache Boundary**。每個 session 的 system prompt 裡有一個 heartbeat section，注入當前時間、機器名稱等動態資訊——讓跑了很多天的 Agent 不會對時間和環境產生混淆。但這裡有個矛盾：動態資訊每次不同，放進 system prompt 就會破壞 prefix cache（每次 system prompt 都不一樣，cache 就完全沒用）。解法是用 `system-prompt-cache-boundary.ts` 把 system prompt 切成兩段，靜態內容在前（享受 cache），heartbeat section 在後（每次重新處理）。


---


## 這些設計在說什麼


拆開這幾個機制，OpenClaw 的設計哲學大概是：每一層都在假設「事情會出錯」，然後問自己「出錯之後系統能不能自己恢復」。Channel 斷了有 backoff 重連；API key 被 rate-limit 了有 rotation；model 不可用了有 fallback chain；Gateway crash 了有 orphan recovery；context 壓縮失敗了有 checkpoint rollback。


這些不是「加分功能」，而是「讓系統能 24/7 不需要人盯著」的基礎條件。


Plugin SDK 邊界（所有插件只能透過 `openclaw/plugin-sdk/*` 的 subpath 進入 core，不能直接 import `src/**`）也是這個哲學的延伸——對邊界的執著，貫穿了整個系統。


拿 hermes-agent 做對比，兩個系統問的是不同層次的問題：hermes-agent 在問「怎麼讓 Agent 越用越好」（Skill 系統、RL 訓練迴路、記憶體架構），OpenClaw 在問「怎麼讓 Agent 永遠不停」。這兩個問題都值得問，只是它們反映了兩種截然不同的設計出發點。


---


> 
**結語**：讀 OpenClaw 的原始碼，最讓我印象深刻的不是某個單一機制，而是這種設計態度的一致性——它在每一個可能出錯的地方，都預設了一個「沒有人在場」的場景，然後問：系統能自己處理嗎？


## 延伸閱讀


- [Hermes-agent：從原始碼看一個為 Production 設計的 Agent 系統](/blog/hermes-agent-production-agent) — 對照版：hermes-agent 用完全不同的方式解決同一批問題
- [hermes-agent vs OpenClaw：兩個 Agent 框架，同一批問題，不同的答案](/blog/hermes-agent-vs-openclaw-agent) — 直接對比兩個框架的設計決策：context 壓縮、error recovery、記憶管理
- [Harness Engineering 的地基：LLM Session 設計框架](/blog/llm-session-harness) — OpenClaw 的 session 設計背後：Multi-Agent SessionKey 與中斷恢復的理論框架

  
  
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

---
url: "https://warmwater.dev/blog/generic-agent-source-code"
title: "不預裝能力，只定義生長方式：GenericAgent 原始碼解析"
date: 2026-05-22
category: Source Code
source: warmwater.dev
---

[
← Source Code ](/blog?tag=Source%20Code)  Source Code 
 
# 不預裝能力，只定義生長方式：GenericAgent 原始碼解析
 
 2026-05-22 · — views  
  
  
多數 Agent 框架解決「能力不夠」的方式是加：更多工具、更多整合、更大的 context window。GenericAgent 的作者問了一個不同的問題：**如果 context window 是稀缺資源，你要怎麼讓每個 token 都賺到它的位置？**


這個問題有一個正式名字：Contextual Information Density Maximization（CIDM）。它是 GenericAgent 所有設計選擇的第一原理——9 個工具為什麼夠用、五層記憶為什麼不用外部向量資料庫、技能為什麼不預裝而是自己長出來，都是同一個問題的不同面向。


**讀完精華版（2 分鐘），你會理解：**


- GenericAgent 的統一 Agent Loop 如何把執行邏輯與 LLM 完全解耦
- 五層記憶系統怎麼做到 <30K context 卻能處理複雜長期任務
- 技能結晶機制與 Hermes-agent 的本質差異：事前驗證 vs 事後判斷
- Reflect 機制如何讓同一套基礎設施同時支撐互動模式和自主運行


這篇是原始碼解析，不是使用教學。


---


## 精華版


| 設計維度 | GenericAgent 的選擇 | 核心 trade-off |
| --- | --- | --- |
| 工具數量 | 9 個原子工具，固定不變 | context 固定開銷極低，但每個複雜操作都需要 agent 自己組合多步序列 |
| 記憶架構 | 五層分層（L0–L4），按存取頻率決定是否進 context | context <30K token，但 L1 Index 是單點，寫壞就迷路 |
| 技能機制 | 技能即記憶，存在 memory/ 目錄，L1 負責路由 | 不需要決定某東西算「技能」還是「記憶」，代價是沒有版本控制與安全掃描 |
| 品質保證 | No Execution, No Memory：只有跑通的執行路徑才能結晶進記憶 | 事前過濾雜訊，但技能樹完全不透明，沒有 audit trail |
| 自主性設計 | Reflect 機制讓同一套 loop 同時支撐互動與後台自主執行 | 兩種模式共用記憶，協作靠 SOP 約定，不是框架層強制 |


**設計原則**：GenericAgent 把 Contextual Information Density Maximization（CIDM）當作第一原理——context window 是稀缺資源，所有設計決策都指向同一個問題：如何讓每個 token 賺到它的位置。工具少、記憶分層、技能自動結晶，都是這個原則的直接推論。


**記憶架構**：L0 是每 session 必注入的核心規範，L1 是幾百個 token 的目錄（不是內容本身），agent 靠 L1 路由到需要的 L2–L4 知識。整個系統是 agent + 本地文字檔，不依賴外部向量資料庫；路由精度完全依賴 L1 文字索引的品質。


**技能結晶**：`start_long_term_update` 觸發後，GenericAgent 把成功執行路徑的關鍵步驟寫成 SOP 存入 L3、更新 L1 索引、把 session 蒸餾為摘要存入 L4，三件事一次完成。跑通才能結晶是事前品質保證；Hermes 的 skill nudge 是事後讓旁觀者 agent 判斷值不值得記，兩種不同的品質哲學。


**自主執行**：Reflect 機制的全部就是三個要素：`INTERVAL`（多久觸發一次）+ `ONCE`（持續還是一次）+ `check()`（條件滿足回傳 prompt，否則回傳 None）。Goal Mode 在此之上加了時間預算和「禁止提前停止」規則，強制 agent 在預算內主動找下一個改進點。


---


### 設計問題簡答


**為什麼 9 個工具夠用？**
工具定義是每輪 context 的固定開銷，不管用不用到都佔 token。工具越少，每輪能留給推理的 token 越多。複雜任務靠 agent 組合這 9 個原子操作的序列，代價是需要更多輪次，換來的是 context 預算幾乎全給了實際推理。


**L1 Index 是怎麼省下 context 的？**
L1 只存目錄（幾百個 token），不存 SOP 內容。agent 讀 L1 就知道「需要 ADB → 讀 adb_ui.py」，不需要把所有 SOP 都載入 context。這個設計的風險是 L1 本身是單點，agent 自己維護，寫壞了整個記憶路由就失效。


**GenericAgent 和 Hermes 的技能機制差在哪？**
GenericAgent 不區分「技能」和「記憶」，SOP 和可 import 的 Python 模組都住在 memory/ 目錄。Hermes 把 SKILL.md 和 memory 設計成兩個獨立系統，用旁觀者 agent 判斷哪些執行路徑值得記。GenericAgent 信任「跑通就值得記」，Hermes 信任「需要外部判斷才值得記」。


**Reflect 機制讓 GenericAgent 多了什麼能力？**
Reflect 讓 agent 在沒有用戶指令的情況下自主執行後台任務，且後台任務產生的記憶更新在下次互動時直接可用。監控檔案系統、偵測用戶 idle、Goal Mode 持續迭代，底層都是同一個 `check()` 介面。關鍵是兩種模式共用同一套 loop 和記憶系統，不需要做記憶同步。


**GenericAgent 適合哪類使用情境？**
個人使用、追求自主性的場景。零外部依賴是優點，但 L1 單點、SOP 無版本控制、沒有 audit trail，使得它不適合需要合規審計或多人協作的企業場景。加入 Human-in-the-loop 的技能審核會打斷自動結晶流程，往那個方向走就是在往 Hermes 靠攏——GenericAgent 選擇了自主性，接受了不透明，這個取捨是設計核心。


---


> 
以下是完整版，按需取用。


---


## 統一 Agent Loop：3K 行怎麼做到的


GenericAgent 的整個 repo 核心只有三個檔案，職責清晰分離：


```
agentmain.py（GenericAgent class）
 ├── LLMClient（llmcore.py） ← LLM 多後端支援、history 管理
 │ └── backend.history ← 完整對話歷史存在這裡
 ├── GenericAgentHandler（ga.py） ← 工具實作（do_xxx 方法）
 │ └── working{} ← 短期工作記憶
 └── agent_runner_loop（agent_loop.py） ← 核心 loop（~100 行）
```


Loop 本身的結構非常直接：


```
def agent_runner_loop(client, system_prompt, user_input, handler, tools_schema, max_turns=40):
 messages = [system, user_input]
 while turn < max_turns:
 response = yield from client.chat(messages=messages, tools=tools_schema)
 for tool_call in response.tool_calls:
 outcome = yield from handler.dispatch(tool_name, args, response)
 if outcome.should_exit: break
 messages = [{"role": "user", "content": next_prompt, "tool_results": results}]
 # 完整 history 存在 client.backend.history，messages 只放當前輪的 delta
```


這裡有一個關鍵設計決策：`messages` 每輪只存當前輪的 delta，完整對話歷史由 `client.backend.history` 維護，兩者分離。這讓 context 壓縮和 session 恢復可以獨立於 loop 本身操作，你改壓縮策略不需要動 loop，`/resume` 恢復只是重設 history。


每個工具回傳 `StepOutcome`，三個欄位決定下一步：


```
@dataclass
class StepOutcome:
 data: Any # 工具執行結果
 next_prompt: Optional[str] = None  # None = 繼續；"" = 任務完成
 should_exit: bool = False # True = 立即退出（ask_user）
```


工具分發用 `do_` 前綴約定：`handler.dispatch("code_run", args)` 呼叫 `do_code_run()`。加新工具只需要在 `GenericAgentHandler` 加一個 `do_newtool()` 方法，不需要改 loop。


**Model-agnostic 是這個解耦的自然結果。** `llmcore.py` 支援 Claude、OpenAI、Gemini 等多種後端，`backend.history` 格式是 LLM-agnostic 的，同一份 history 可以在不同 LLM 之間無縫切換。執行邏輯、工具介面、記憶架構都不需要改。當更強的模型出現，整個系統能直接受益，而不是重寫。


這個框架有一個值得一提的 dogfooding：GenericAgent 的 repo 本身，從 `git init` 到每一條 commit message，全部由 GenericAgent 自主完成，作者從未開過終端機。這不是 demo，是真實的驗證：一個只有 ~3K 行的框架，有能力管理自己的開發流程。


---


## 工具設計：為什麼 9 個夠了


CIDM 原則的第一個應用在工具設計。工具定義是每輪 context 的**固定開銷**，不管這輪用不用到某個工具，它的 schema 都佔著 token。工具越少，固定開銷越低，每輪能留給實際任務的 token 越多。


9 個工具組成的能力矩陣：


| 工具 | 類別 | 核心能力 |
| --- | --- | --- |
| code_run | 執行 | Python / bash / PowerShell，subprocess 執行 |
| file_read | 檔案 | 讀取，支援行號跳轉與關鍵字定位 |
| file_patch | 檔案 | 精確局部修改，old→new 唯一匹配 |
| file_write | 檔案 | 建立/覆寫/追加，支援跨檔案引用 |
| web_scan | 瀏覽器 | 取得當前頁面簡化 HTML + tab 列表 |
| web_execute_js | 瀏覽器 | 注入並執行任意 JS |
| update_working_checkpoint | 記憶 | 更新短期工作 scratchpad |
| ask_user | 互動 | 中斷任務向用戶提問 |
| start_long_term_update | 記憶 | 觸發技能結晶、記憶更新 |


複雜任務不是靠單一強大的工具完成，而是靠 agent 自己組合這 9 個原子操作的序列。這個設計的代價是 agent 需要更多輪次完成同樣的任務；換來的是 context 固定開銷極低，每輪的 token 預算幾乎全部給了實際推理。


`code_run` 是其中最核心的。幾乎所有「做事」的任務最終都走這裡——Python 腳本、bash 指令、安裝依賴、資料處理。它的執行流程是：從 `assets/code_run_header.py` 注入常用 import，寫入臨時 `.ai.py`，subprocess 執行，串流讀 stdout，超時就 kill。輸出用 `smart_format()` 截斷後才回傳給 LLM，完整輸出要讀檔案。


瀏覽器的部分值得單獨說。`web_execute_js` 背後是 **TMWebDriver**，透過 Chrome DevTools Protocol（CDP）注入**已開啟的真實瀏覽器**，不是啟動新的 headless 實例。這個差異的實際含義是：Cookie、LocalStorage、登入 session 全部保留，agent 在你已登入的 Gmail 或 GitHub 裡直接操作，不需要重新登入。對比 Playwright 每次啟動都是全新瀏覽器環境，這個設計讓 agent 能真正處理需要持久登入狀態的任務。


---


## 五層記憶系統：Context 的按需組裝


記憶系統是 CIDM 原則最集中體現的地方。論文（arXiv:2604.17091）的核心數字：GenericAgent 的 context window 使用量 <30K token，而其他主流 Agent 框架通常在 200K–1M。做到這件事的機制是分層管理，把「永遠需要的知識」和「按需才用的知識」分開存，前者永遠在 context，後者由 agent 自己判斷要不要讀。

 GenericAgent 五層記憶架構
  
 始終在 Context
 
  L0 Meta Rules 
 
assets/sys_prompt.txt
 
角色定義、行動原則、失敗升級規則、工具使用規範——不可變
  
  L1 Insight Index 
 
memory/global_mem_insight.txt
 
記憶的目錄，不是記憶本身——「什麼東西在哪裡，需要時去讀」
 
  L1 路由 → agent 主動呼叫 file_read ↓  
  
 按需讀取
 
  L2 Global Facts 
 
memory/global_mem.txt
 
跨任務穩定事實（帳號習慣、常用路徑、個人偏好）
  
  L3 Task Skills 
 
memory/*.md  ·  memory/*.py
 
結晶後的可複用執行路徑（Markdown SOP + 可 import 的工具模組）
  
  L4 Archive 
 
memory/L4_raw_sessions/
 
過往 session 的蒸餾摘要，長時程回憶
 
  始終在 Context（L0 + L1）

 
 按需讀取（L2–L4）

  

L0 是不可變的核心規範，角色定義、三步失敗升級規則、哪些操作禁止，每個 session 都注入。L1 是記憶的目錄，不是記憶本身。它的實際內容很短，幾百個 token，但能路由到任何 L2–L4 的知識。一個真實的 L1 看起來像這樣：


```
L3: memory_cleanup_sop | skill_search | ui_detect.py | tmwebdriver_sop
 | web_setup_sop | plan_sop | autonomous_operation_sop | ...
Browser special ops: tmwebdriver_sop
Keyboard & Mouse: ljqCtrl_sop
```


Agent 讀到 L1 就知道「需要 ADB → 讀 adb_ui.py」、「需要瀏覽器特殊操作 → 讀 tmwebdriver_sop」，不需要把所有 SOP 都塞進 context。這個設計更接近「人類用目錄查書」，而不是把整本書背進記憶裡。


**這個設計追求什麼**：自給自足。整個記憶系統就是 agent + 一堆文字檔，不依賴任何外部向量資料庫或記憶服務。L2 有帳號資訊，L3 有操作流程，L4 有歷史摘要，全在本地 `memory/` 目錄。


**放棄了什麼**：L1 Index 是單點，agent 自己維護，寫壞了就迷路。L3 的 SOP 沒有版本控制，沒有安全掃描，過期的 SOP 會持續存在直到 agent 自己更新。沒有語意搜尋，路由精度完全依賴 L1 的文字索引品質。這些不是設計缺陷，是為了「零外部依賴」刻意接受的代價。


---


## 技能即記憶：自我進化機制


Hermes-agent 把 skill 和 memory 設計成兩個獨立系統（SKILL.md + skill_manage tool；memory 走 honcho/vector）。GenericAgent 不做這個區分，`adb_ui.py` 同時是「我解決過 ADB 問題的記憶」，也是「下次可以直接 import 的工具」，它存在 `memory/` 目錄，L1 負責路由，僅此而已。


邊界消失的好處是：不需要決定某個東西算「記憶」還是「技能」。代價是沒有獨立的技能管理機制，沒有版本控制、沒有安全掃描，壞掉的 SOP 會一直在那裡直到 agent 自己更新。


### No Execution, No Memory


技能結晶的品質門檻來自 `memory_management_sop.md` 的核心公理：


> 
任何寫入 L1/L2/L3 的信息，必須源自成功的工具調用結果。
> 禁止：未執行的計畫、未驗證的假設、模型固有知識。


執行本身就是驗證環境。一個 SOP 能進 L3，前提是它對應的執行路徑實際跑通過。這是一個事前的品質保證：結晶的是成功案例，不是計畫或假設。


### 結晶流程


結晶由 `start_long_term_update` 觸發，非同步執行，三件事一次完成：


```
任務成功完成
 ↓
agent 呼叫 start_long_term_update
 ├── 提取執行路徑關鍵步驟 → 寫入 memory/ 為新 SOP（L3）
 ├── 在 L1 Insight Index 加入這個 SOP 的一行描述
 └── 把這次 session 蒸餾為摘要 → 存入 L4 Archive
 ↓
下次類似任務：L1 命中 → 直接讀 SOP → 一行調用
```


L3 的技能有兩種形態：Markdown 描述性 SOP（`web_setup_sop.md`、`plan_sop.md`）和可直接 import 的 Python 模組（`adb_ui.py`、`keychain.py`）。兩種形態由 agent 自己判斷，依任務性質決定。


### 和 Hermes skill nudge 的根本差異


兩個框架在「哪些執行路徑值得記憶」這個問題上，選了不同的信任模型：


|  | GenericAgent | Hermes skill nudge |
| --- | --- | --- |
| 保證方式 | 事前：No Execution, No Memory | 事後：review agent 讀 history 判斷 |
| 觸發 | agent 主動呼叫 | 自動，每 10 次 tool call |
| 誰做判斷 | 同一個 agent | fork 出的獨立 background agent |
| 驗證約束 | 執行成功才能結晶 | 無顯式約束，review agent 讀 conversation history |


GenericAgent 相信「跑通就值得記」，Hermes 相信「需要旁觀者來判斷值不值得記」。兩種不同的品質保證哲學，沒有對錯。


**技能樹的私有性是這個機制最重要的副產品。** 同樣的 3K 行種子，兩個用戶各自用了半年，他們結晶的 SOP 完全不同，因為他們做過的任務不同。GenericAgent 積累的是真正個人化的工作能力，不是共享的通用 LLM 能力。


---


## 兩種執行模式，同一套基礎設施


GenericAgent 的執行有兩種模式，但共用完全相同的 agent loop 和記憶系統：


**Interact Mode**（互動模式）：用戶發指令，agent 執行，回傳結果。這是最常見的使用方式。


**Reflect Mode**（反射模式）：不需要用戶指令，自動觸發後台任務。兩種觸發方式：看門狗（監控環境變化，如新檔案出現）和定時任務（時間驅動）。


兩種模式共用同一套基礎設施的設計意義是：反射模式產生的結果和記憶更新，在下次互動時可以直接利用。不需要維護兩套系統，也不需要做記憶同步。


### Reflect 是底層抽象


自主行動、定時任務、Goal 模式，底層都是同一個介面：


```
# reflect/autonomous.py
INTERVAL = 1800  # 每 30 分鐘檢查一次
ONCE = False # 持續監測

def check() -> str | None:
 # 返回 str → 喚醒 agent 並以此為 prompt
 # 返回 None → 不喚醒，等下次 INTERVAL
 return "[AUTO]🤖 用戶已離開超過 30 分鐘，請閱讀自動化 SOP，執行自動任務。"
```


三個要素（`INTERVAL` + `ONCE` + `check()`）就是 Reflect 機制的全部。任何「條件滿足就叫醒 agent」的行為都可以用這三個要素組合，監控檔案系統、偵測用戶 idle、輪詢 API 狀態、等待特定事件。這是一個開放的介面，不是固定的功能清單。


### Goal Mode 的設計


Goal Mode 是 Reflect 機制的一個特殊實現，設計用來處理「沒有固定終點、需要持續迭代」的任務：


```
{
  "objective": "把這個 Python 庫的 test coverage 從 60% 提升到 90%",
  "budget_seconds": 7200,
  "start_time": 1715234567.89,
  "turns_used": 0,
  "max_turns": 200,
  "status": "running"
}
```


狀態機：`running → wrapping_up → done_budget`。每輪 `check()` 檢查預算剩餘，注入對應的 prompt：


- **預算充足**（CONTINUATION_PROMPT）：告訴 agent 「禁止說已完成，預算沒到不準停；做完當前方向，主動找下一個改進點」
- **預算耗盡**（BUDGET_LIMIT_PROMPT）：切換收口模式，要求總結進展、列出未完成事項


「禁止提前停止」這個規則解決了 agent 容易在完成一個明顯目標後就詢問是否繼續的問題。有時間預算時，agent 被強制保持主動尋找改進點的狀態。


### 執行邊界


支撐自主運行的可控性設計：


- **輪次上限**：每次任務有 `max_turns` 上限，防止無限循環
- **三步失敗升級**：第一次失敗分析錯誤小幅修正；第二次切換策略或探索環境；第三次暫停請求用戶介入
- **可中斷性**：用戶隨時可中斷，當前進度存在工作記憶


這三個約束確保 GenericAgent 在有強大自主能力的同時，失控情況有明確的兜底機制。


---


## GenericAgent 的設計取捨


GenericAgent 的每一個設計選擇都圍繞同一個目標，但「為了 CIDM 做極簡設計」這件事本身就是一個取捨，不是一個沒有代價的優化。


**你得到的**：零外部依賴，`pip install` 就能跑；context 極度精簡，token 效率高；技能自動生長，越用越強；Reflect 機制讓 agent 在你不在的時候繼續工作。


**你放棄的**：L1 Index 是整個記憶系統的單點，agent 自己維護，寫壞了就迷路。L3 SOP 沒有版本控制，壞掉的流程會持續在那裡直到 agent 自己發現並更新。subagent 的協作靠 SOP 約定，不是框架層的強制 hierarchy，靈活但脆弱。整個系統沒有 audit trail，你不容易知道某個決策是怎麼做出來的。


這些代價使得 GenericAgent 更適合個人使用，而不是需要多人協作、合規審計、或可預測行為的企業場景。你可以想像加入 Human-in-the-loop 的技能審核：先自動結晶進 staging，人工確認後才 promote 進 L3，這樣有 audit trail，也有安全掃描的機會。但這樣做就動到了 No Execution, No Memory 的自動結晶流程——每次新技能都需要等人確認，自主生長的節奏就斷了。往這個方向走，其實就是在往 Hermes 的「旁觀者判斷值不值得記」靠攏。GenericAgent 選擇了自主性，接受了不透明；這個取捨不是偶然，是設計的核心。


> 
同樣的 3K 行種子，兩個用了半年的用戶，各自的技能樹完全不同。這個設計讓 AI 能力不再是所有人共享的通用 LLM，而是真正屬於你的工作記憶。

 
 [ Source Code ](/blog?tag=Source%20Code) 
 

### 相關文章
[Source Code

你在省 Token，還是在省思考？四種廢話假設比較

2026-05-19
](/blog/token-saving-four-assumptions)[
Source Code

Task Continuity，不是 Personal Memory：Claude Code 的 Session 設計

2026-05-15
](/blog/claude-code-task-continuity)[
Source Code

Memory 01：誰決定什麼值得記——Agent 記憶的四種寫入模式

2026-05-14
](/blog/agent-memory-01-write-design)

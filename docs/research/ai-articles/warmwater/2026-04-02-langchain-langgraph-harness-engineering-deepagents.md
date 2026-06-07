---
url: "https://warmwater.dev/blog/langchain-langgraph-harness-engineering-deepagents"
title: "用 LangChain + LangGraph 實作 Harness Engineering：從 deepagents 學到的設計模式"
date: 2026-04-02
category: Harness Engineering
source: warmwater.dev
---

[
← Harness Engineering ](/blog?tag=Harness%20Engineering)  Harness Engineering 
 
# 用 LangChain + LangGraph 實作 Harness Engineering：從 deepagents 學到的設計模式
 
 2026-04-02 · — views  
  
  
## 前言


上一篇介紹了 Harness Engineering 的概念——圍繞 LLM 建立的執行基礎設施，讓模型能安全、可控地在真實世界行動。這篇從理論走到實作：用一個真實的 POC，示範如何把 Harness 的五個維度用 LangChain + LangGraph 落地。


分析材料來自 deepagents，一個由 LangChain 官方維護的 agent 框架，覆蓋了 Memory、Context Compact、HITL、Multi-agent 等完整的 Harness 能力。


---


## 這個 POC 在做什麼


[harness-agent-poc](https://github.com/jason8745/harness-agent-poc) 是一個最小但完整的 Harness 實作。


**一句話定位**：指向任何 local repository，讓 AI 成為那個 codebase 的持久化專家——可以跨 session 記住分析結果、回答問題、生成報告。


```
# 分析一個 repo，生成結構化報告
uv run harness-agent analyze deepagents

# 後續對話，自動載入既有報告
uv run harness-agent chat deepagents

```


五個 Harness 維度的對應實作：


| Harness 維度 | 實作方式 |
| --- | --- |
| 資源管理 | Context 超過閾值時自動摘要壓縮 |
| 狀態持久化 | AGENTS.md + 每個 repo 的分析報告跨 session 保存 |
| 信息流控制 | Middleware 層控制每輪 system prompt 的注入內容 |
| 安全邊界 | HITL：寫入操作前暫停，等待用戶審批 |
| 任務編排 | Filesystem tools 讓 Agent 自主讀寫檔案 |


---


## 核心架構：Middleware Pattern


deepagents 和這個 POC 的核心設計都是 **Middleware Pattern**。理解它是理解整個系統的關鍵。


### 什麼是 Middleware


Middleware 是**攔截每次 LLM call 的 hook 層**。每個 middleware 實作 `wrap_model_call`，在 LLM 被呼叫前後執行邏輯：


```
class AgentMiddleware:
 def wrap_model_call(self, request, handler):
 # 修改 request（注入 context、過濾 tool list 等）
 modified = self.modify(request)
 # 呼叫下一層（可能是另一個 middleware，或 LLM 本身）
 return handler(modified)
 
 def before_agent(self, state, ...):
 # Agent 啟動時初始化 state
 ...
 
 def before_tool(self, ...):
 # Tool 執行前攔截
 ...
 
 def after_tool(self, ...):
 # Tool 執行後修改結果
 ...

```


### Middleware vs Plain Tool


這是選擇架構時最常遇到的問題：


|  | Middleware | Plain Tool |
| --- | --- | --- |
| 執行時機 | 每次 LLM call 前 | LLM 選擇呼叫時 |
| 能力 | 修改 system prompt、過濾 tool list、追蹤跨輪 state | 執行具體操作 |
| 適合場景 | 系統級全局邏輯（Memory、HITL、Compact） | 具體的功能操作（read_file、search_web） |


簡單判斷規則：**需要在每輪 LLM call 前執行的邏輯 → Middleware；被 LLM 選擇性呼叫的功能 → Plain Tool。**


### Middleware Stack 的順序


deepagents 的完整 stack 有 11 層，順序不是隨意的：


```
middleware_stack = [
 TodoListMiddleware(), # 1. 任務清單（LLM 需要最先知道）
 SkillsMiddleware(...), # 2. Skills 注入
 FilesystemMiddleware(...), # 3. 文件系統工具
 SubAgentMiddleware(...), # 4. 子 agent 委派
 SummarizationMiddleware(), # 5. Context 壓縮
 PatchToolCallsMiddleware(), # 6. 修補懸空 tool call
 AsyncSubAgentMiddleware(...), # 7. 異步子 agent
 *user_middleware, # 8. 用戶自定義
 AnthropicPromptCachingMiddleware(), # 9. Prompt Caching（必須在 Memory 前）
 MemoryMiddleware(...), # 10. 記憶注入（在 Caching 之後）
 HumanInTheLoopMiddleware(), # 11. HITL（最後，攔截所有 tool calls）
]

```


順序背後的設計邏輯：


- **Caching 在 Memory 前**：Memory 更新會修改 system prompt，讓 Anthropic 的 prompt cache prefix 失效。確保 cache 在 memory 注入前就設定好
- **HITL 在最後**：需要攔截所有 tool calls，放最後才能覆蓋到所有前面的 middleware
- **PatchToolCalls 在 Summarization 後**：Compact 後可能有懸空的 tool call，需要在 compact 執行完再修補


---


## 五個維度怎麼實作


### 工具設計（任務執行能力）


工具定義建議用 Pydantic schema，讓 LLM 的 tool calling 更精確：


```
class ReadFileInput(BaseModel):
 file_path: str = Field(description="Absolute path to the file")
 offset: int = Field(default=0, description="Starting line")
 limit: int = Field(default=100, description="Max lines to return")

read_tool = StructuredTool.from_function(
 func=read_file_impl,
 name="read_file",
 args_schema=ReadFileInput,
)

```


Tool result 的格式也有設計考量：帶行號（讓 LLM 知道位置）、截斷時附上提示（讓 LLM 知道可以改策略）、錯誤用文字描述（不要 raise exception，讓 agent 能自行修復）。


### Context 管理（信息流控制）


Compact 的觸發條件有三種選擇：


```
trigger = ("fraction", 0.85)  # 使用 85% context window 時觸發（推薦）
trigger = ("tokens", 170000)  # 固定 token 數（不知道 model context size 時用）
trigger = ("messages", 50) # 固定消息數

```


deepagents 的設計：如果知道 model 的 context window，用 fraction-based（精確）；不知道時退回保守的固定值（安全）。


注入 context 時用 XML 標籤組織，讓 LLM 更容易辨別信息來源：


```
<agent_memory>
  ...用戶偏好、專案背景...
</agent_memory>

<available_skills>
  ...可用的 workflow...
</available_skills>

```


### Memory（狀態持久化）


Memory 不需要向量資料庫，Markdown 文件就夠。兩層結構：


- **全局 `AGENTS.md`**：用戶偏好、工作習慣（跨所有 repo）
- **`repos/{repo-name}.md`**：每個 repo 的分析結果和累積洞察


Agent 被明確告知「記憶更新必須是最優先的 action，在回應用戶之前就要執行」，這個 prompt 設計確保 learning 的即時性。


用 `edit_file`（精確字串替換）而非 `write_file`（全量覆寫），讓記憶更新 diff-friendly。


### HITL（安全邊界）


最小化的 HITL 實作用 LangGraph 的 `interrupt` 機制：


```
app = graph.compile(
 checkpointer=checkpointer,
 interrupt_before=["tools"],  # 在 tool 執行前暫停
)

```


deepagents 提供三個選項：批准這次、整個 session 自動批准、拒絕。**「整個 session 自動批准」是關鍵設計**——用戶審批一次之後，後續的同類操作不再打擾，大幅降低摩擦，同時保留了第一道防線。


---


## 從 deepagents 學到的設計原則


這是這篇文章最值得留存的部分。以下是從 deepagents 源碼中提煉出來的、不看代碼難以發現的設計決策。


### 原則一：Middleware 的不可變 Request 模式


每個 middleware 通過 `request.override()` 創建新的 request，而不是直接修改傳入的 request：


```
def wrap_model_call(self, request, handler):
 new_system = append_to_system_message(request.system_message, my_context)
 return handler(request.override(system_message=new_system))  # ✓
 # 而不是 request.system_message = new_system; return handler(request)  ✗

```


**為什麼**：immutable 設計讓每個 middleware 只負責自己的修改，不會意外影響其他層的預期狀態。整個 chain 的行為可預測，也更容易 debug。


### 原則二：Middleware 的 Private State


每個 middleware 如果需要跨輪次保存狀態，要宣告自己的 `state_schema`，並用 `PrivateStateAttr` 標記：


```
class SummarizationState(AgentState):
 # 標記為 Private — 不暴露給用戶，不污染 agent 的主要 state
 _compact_event: Annotated[NotRequired[CompactEvent | None], PrivateStateAttr]

class SummarizationMiddleware(AgentMiddleware[SummarizationState, ...]):
 state_schema = SummarizationState

```


**為什麼**：Middleware 的 internal tracking（「是否已壓縮」、「目前的記憶內容」）不應該混入 agent 主要 state，否則調試時很難分清哪些是 agent 的業務狀態、哪些是 harness 的內部狀態。


### 原則三：Argument Truncation — 比 Compact 更輕量的清理


完整 Compact 要呼叫 LLM 生成摘要，代價不低。deepagents 在 Compact 之前有一個更輕量的預處理：**截斷舊 messages 裡的 tool call arguments**。


```
truncate_args_settings = {
 "trigger": ("messages", 50),  # 超過 50 條消息後開始
 "keep": ("messages", 20), # 保留最近 20 條完整
 "max_length": 2000, # 每個 arg 最多 2000 字元
}

```


**為什麼值得做**：`write_file` 的大段文字、`edit_file` 的 patch 內容，在舊 messages 裡幾乎沒有回顧價值，但可能佔據大量 token。把這些截斷掉，可以顯著延緩 Compact 觸發，而且幾乎不損失語義。


這是一個「分層清理」的思路：先用規則清理（免費），再用 LLM 摘要（有成本）。


### 原則四：懸空 Tool Call 的修補


當 agent 的 `AIMessage` 有 tool_calls，但沒有對應的 `ToolMessage`（例如被用戶中斷、或 Compact 刪掉了對應回應），LLM 下一輪會困惑。`PatchToolCallsMiddleware` 自動補上一條錯誤 ToolMessage：


```
# 自動補上的修補消息
ToolMessage(
 content="Tool call {name} was cancelled",
 tool_call_id=tool_call["id"],
)

```


**為什麼**：Anthropic 和 OpenAI 的 API 都要求 tool_use 和 tool_result 成對出現。這個 middleware 讓 harness 在面對各種中斷情況時能優雅恢復，而不是整個 session 崩潰。


### 原則五：Skills 的 Progressive Disclosure


Memory（AGENTS.md）是「每輪都注入」，但 Skills 不是——只注入 skill 的名稱和一句描述，agent 需要時才去讀完整內容：


```
# 注入的是這個（摘要）：
<available_skills>
  - web-research: Structured approach to conducting thorough web research
  - code-review: Step-by-step code review workflow
</available_skills>

# 不是這個（完整內容，可能幾百行）：
# web-research
## When to Use ...
## Steps
1. Search for primary sources
2. Synthesize findings
...

```


**為什麼**：把所有 skills 的完整內容都注入 system prompt，會佔用大量 token 且大部分時候用不到。Progressive Disclosure 讓 agent 只在真正需要時才消耗那些 token。這是「信息供給按需分配」的典型應用。


### 原則六：HITL 的 Approval UI 設計細節


deepagents 的 approval UI 有兩個值得注意的設計：


**Security scan 在顯示前就跑**：approval 視窗出現之前，系統就已經掃描了所有 tool call arguments 裡的 Unicode 同形字和可疑 URL，並在 UI 裡標記出來。這防止了 prompt injection 攻擊——惡意內容讓 agent 生成一個「看起來像正常操作但實際上有問題」的 tool call。


**長命令可展開**：shell command 超過 120 字元時預設截斷，按 `e` 展開查看完整內容。設計意圖是確保用戶「真的看到了」要執行的命令，而不是在一個看不到全文的審批框上隨手按 yes。


---


## 給工程師的 Takeaway


如果你要用 LangChain + LangGraph 搭一個自己的 Harness，幾個直接可用的規則：


- **用 Middleware 做系統邏輯，用 Tool 做功能操作**——判斷標準是「這個邏輯每輪都要跑嗎？」
- **Middleware 用 `request.override()` 而非直接修改**——immutable 設計讓行為可預測
- **Private state 要宣告**——internal tracking 和 agent 業務 state 分開，debug 時救命
- **Compact 前先 truncate arguments**——先免費清理，再付費摘要
- **HITL 提供 auto-approve 選項**——「問一次，全 session 有效」大幅降低使用摩擦
- **Memory 更新優先於回應**——在 system prompt 明確說「記住要先寫 memory，再回應用戶」
- **Skills 用 progressive disclosure**——只注入摘要，按需讀完整內容


完整的 POC 代碼在 [harness-agent-poc](https://github.com/yujun/harness-agent-poc)，每個 Harness 維度都有對應的實作，找到 `middleware/` 目錄就能看到所有設計的具體落地。


---


## 這個 MVP 還沒補上的


這個 POC 目前有：Filesystem tools、Compact、Memory、HITL。作為 MVP，有幾個 deepagents 的 middleware 能力沒有實作進來，記錄在這裡供參考：


### TodoList Middleware（最值得做）


deepagents 的 stack 裡排第一個的就是 `TodoListMiddleware`。Agent 在開始複雜任務前，先自行建立一份 task list，執行過程中逐一打勾，loop 結束前確認「還有哪些沒做完」。


好處不只是給用戶看進度——更重要的是讓 agent 自己不會在多步驟任務中途「忘記」後面要做什麼。沒有 TodoList 的 agent 靠 system prompt 指引下一步，有了 TodoList 的 agent 靠自己維護的 state。


實作上，在 `before_agent` 初始化一個空的 todo list，在 system prompt 裡告訴 LLM「開始工作前先列出 tasks，完成一個就打勾，最後確認全部 done 再結束」。


### Skills Middleware（架構上的優雅）


目前 `analyze` 的功能是硬寫在 system prompt 裡的。deepagents 的設計是把每個 workflow 抽成獨立的 `.md` 檔案：


```
skills/
└── analyze.md ← 獨立的 workflow 指令
└── review.md ← 新功能只要加檔案，不用改 code

```


Agent 每輪只看到 skill 的名稱和一句描述（progressive disclosure），需要時才讀完整內容。好處：system prompt 不會因為功能增加而越來越肥，新功能對 LLM 的 context budget 幾乎零成本。


### PatchToolCallsMiddleware（bug fix 等級，但不可不知）


當用戶在 agent 執行 tool 途中按 `Ctrl+C` 中斷，會留下一個「dangling tool call」——`AIMessage` 有 `tool_calls` 但沒有對應的 `ToolMessage`。Anthropic 和 OpenAI 的 API 都要求這兩者成對出現，下次對話會直接報錯。


修補方式很簡單：在每輪 `wrap_model_call` 前掃描 messages，對每個沒有對應 `ToolMessage` 的 `tool_call` 補一條：


```
ToolMessage(
 content="Tool call was cancelled",
 tool_call_id=tool_call["id"],
)

```


這個 middleware 讓 agent 在面對各種中斷情況時能優雅恢復，而不是整個 session 崩潰。


## 延伸閱讀


- [Harness Engineering — AI 工程師的第三個維度](/blog/harness-engineering-ai) — 上一篇：Harness 的五個維度概念介紹，這篇是它的實作版
- [LangChain vs LangGraph vs DeepAgents：該選哪個 AI Agent 框架？](/blog/langchain-vs-langgraph-vs-deepagents-ai-agent) — 框架選型指南：理解為什麼這個 POC 選擇 LangChain + LangGraph 的組合
- [Harness Engineering 的地基：LLM Session 設計框架](/blog/llm-session-harness) — POC 裡的 HITL 和 session 設計，在這篇得到更完整的理論框架

  
  
 [ Harness Engineering ](/blog?tag=Harness%20Engineering)[ Implement ](/blog?tag=Implement) 
 

### 相關文章
[Implement

用 RPG 架構評估 SRE Agent：Kube Arena 設計紀錄

2026-05-28
](/blog/kube-arena)[
System Design

Agent 要怎麼進化？六個系統的 Self-Improvement 機制比較

2026-05-22
](/blog/agent-self-improvement-design-comparison)[
System Design

SOUL 設計決定了 Agent 是什麼：六個 Agentic System 的 system prompt 比較

2026-05-22
](/blog/agent-soul-design-comparison)

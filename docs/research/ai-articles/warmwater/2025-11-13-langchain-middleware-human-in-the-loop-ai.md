---
url: "https://warmwater.dev/blog/langchain-middleware-human-in-the-loop-ai"
title: "LangChain Middleware 實戰（一）：Human-in-the-Loop 讓 AI 學會等待人類審核"
date: 2025-11-13
category: Tutorial
source: warmwater.dev
---

# 🛡️ LangChain Middleware 實戰（一）：Human-in-the-Loop 讓 AI 學會等待人類審核

**Published**: 2025-11-13

> **系列文章**：本文是 LangChain Middleware 系列的第一篇，專注於 Human-in-the-Loop Middleware

如果你曾經想過：

> 「我的 AI Agent 能自動發郵件、刪資料，但我想在執行前先確認一下…」

那你來對地方了！這篇文章要帶你認識 LangChain 1.0 的 **HumanInTheLoopMiddleware**，讓 AI Agent 在執行敏感操作前「停下來等你批准」。

### 為什麼需要 Human-in-the-Loop？

想像這些場景：

```
❌ 沒有審核機制：
使用者：「刪除所有測試資料」
Agent：「好的！」→ 直接刪除 → 生產環境資料全沒了

✅ 有 Human-in-the-Loop：
使用者：「刪除所有測試資料」
Agent：「即將刪除 users 表的 record 123，需要你的批准」
你：「等等，這不是測試資料！」→ 拒絕
```

**Human-in-the-Loop (HITL)** 讓你在 AI 執行關鍵操作前：

*   **審核工具呼叫**：查看 Agent 要執行什麼
*   **批准或拒絕**：決定是否讓操作繼續
*   **保護生產環境**：避免誤操作造成損失
*   **符合合規要求**：敏感操作需要人工確認

#### 我們這次用到的技術組合

| 技術 | 用途 |
|------|------|
| HumanInTheLoopMiddleware | 暫停 Agent 等待人工審核 |
| InMemorySaver (Checkpointer) | 保存 Agent 狀態以支援中斷/恢復 |
| Command.resume | 提供審核決定讓 Agent 繼續執行 |
| agent.stream() | 檢測中斷事件的關鍵方法 |
| `__interrupt__` | 識別需要審核的訊號 |

---

## 動手做：打造有審核機制的 AI Agent

來看我們的核心實作 👇

```python
import os
import time
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from langchain.agents import create_agent
from langchain.agents.middleware import HumanInTheLoopMiddleware
from langchain.tools import tool
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import Command
from rich.console import Console
from rich.panel import Panel

load_dotenv()
console = Console()

# Initialize Azure OpenAI model
model = AzureChatOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    temperature=0,
)

# 定義工具
@tool
def send_email(to: str, subject: str, body: str) -> str:
    """Send an email to someone. This is a sensitive operation that requires approval."""
    return f"✉️ Email sent to {to} with subject '{subject}'"

@tool
def search_database(query: str) -> str:
    """Search the company database. This is a safe operation."""
    return f"🔍 Found 5 results for: {query}"

@tool
def delete_data(table: str, id: int) -> str:
    """Delete data from database. This is a dangerous operation that requires approval!"""
    return f"🗑️ Deleted record {id} from {table}"

# 創建帶有 HumanInTheLoopMiddleware 的 agent
agent = create_agent(
    model=model,
    tools=[send_email, delete_data, search_database],
    system_prompt="You are a helpful assistant. When user asks you to perform an action, directly call the appropriate tool without asking for confirmation.",
    middleware=[
        HumanInTheLoopMiddleware(
            interrupt_on={
                # send_email: 需要審核
                "send_email": {
                    "allowed_decisions": ["approve", "reject"],
                },
                # delete_data: 需要審核
                "delete_data": {
                    "allowed_decisions": ["approve", "reject"],
                },
                # search_database: 自動批准
                "search_database": False,
            },
            description_prefix="工具執行需要審核",
        )],
    checkpointer=InMemorySaver(),  # 必須使用 checkpointer！
)
```

**這裡是重點：**

*   **interrupt_on 字典**：定義哪些工具需要審核
    *   `True` 或 `{"allowed_decisions": [...]}`: 需要審核
    *   `False`: 自動批准，不中斷
*   **InMemorySaver**：必須配置 checkpointer 才能暫停/恢復執行
*   **allowed_decisions**：限制可用的決定類型（approve/reject）
*   **system_prompt**：讓 Agent 直接呼叫工具，不要再問一次

---

## 核心概念拆解

### 1. 為什麼必須使用 stream() 而不是 invoke()？

```python
# ❌ 錯誤：invoke() 無法檢測中斷
result = agent.invoke({"messages": [...]})
# Agent 會卡住或報錯，你看不到中斷事件

# ✅ 正確：使用 stream() 檢測中斷
for step in agent.stream(
    {"messages": [...]},
    config,
    stream_mode="values"
):
    if "__interrupt__" in step:
        # 這裡處理中斷！
        print("需要審核！")
```

**為什麼？**

*   `invoke()` 期望一次性完成，遇到中斷會失敗
*   `stream()` 會 yield 每個步驟，包括中斷事件
*   `"__interrupt__"` 是中斷的訊號

### 2. 中斷事件的結構

```python
if "__interrupt__" in step:
    interrupt = step["__interrupt__"][0]
    
    # 取得待審核的操作資訊
    for request in interrupt.value["action_requests"]:
        print(f"工具: {request['name']}")
        print(f"參數: {request.get('args', {})}")
        print(f"描述: {request['description']}")
```

**interrupt 包含**：

*   `action_requests`: 待審核的工具呼叫清單
*   每個 request 有：`name`（工具名）、`args`（參數）、`description`（描述）

### 3. 使用 Command 提供審核決定

```python
# 批准操作
Command(resume={"decisions": [{"type": "approve"}]})

# 拒絕操作
Command(resume={"decisions": [{"type": "reject", "message": "原因說明"}]})
```

**關鍵點**：

*   使用 `Command(resume={...})` 繼續執行
*   `decisions` 是陣列，支援多個工具呼叫同時審核
*   必須使用相同的 `config` (thread_id) 才能恢復正確的會話

---

## 實際測試

### 測試案例 1：安全操作（自動批准）

```python
config = {"configurable": {"thread_id": "test1"}}

for step in agent.stream(
    {"messages": [{"role": "user", "content": "Search database for 'customer orders'"}]},
    config,
    stream_mode="values",
):
    if "messages" in step:
        step["messages"][-1].pretty_print()
    elif "__interrupt__" in step:
        print("⚠️ 不應該出現中斷")  # search_database 設為 False
```

**執行流程**：

1.  Agent 識別需要 `search_database`
2.  檢查 middleware 配置：`"search_database": False`
3.  自動批准，直接執行
4.  沒有中斷，直接返回結果

**輸出結果**：

```
🔍 Found 5 results for: customer orders
✓ 這個操作被自動批准並執行
```

### 測試案例 2：敏感操作（觸發中斷）

```python
email_config = {"configurable": {"thread_id": "test_email"}}

# 第一步：執行直到遇到中斷
for step in agent.stream(
    {"messages": [{"role": "user", "content": "Send an email to john@example.com with subject 'Meeting Tomorrow' and body 'Let\\'s meet at 2pm'"}]},
    email_config,
    stream_mode="values",
):
    if "messages" in step:
        step["messages"][-1].pretty_print()
    elif "__interrupt__" in step:
        print("⏸️  需要人工審核")
        
        interrupt = step["__interrupt__"][0]
        for request in interrupt.value["action_requests"]:
            print(f"工具: {request['name']}")
            print(f"參數: {request.get('args', {})}")
        
        # 提示用戶決定
        decision = input("approve / reject > ").strip().lower()
        
        if decision == "approve":
            print("✅ 已批准操作，繼續執行...")
            
            # 第二步：使用 Command 批准並繼續執行
            for step2 in agent.stream(
                Command(resume={"decisions": [{"type": "approve"}]}),
                email_config,
                stream_mode="values",
            ):
                if "messages" in step2:
                    step2["messages"][-1].pretty_print()
        else:
            print("❌ 已拒絕操作")
            
            for step2 in agent.stream(
                Command(resume={"decisions": [{"type": "reject", "message": "User rejected the email operation"}]}),
                email_config,
                stream_mode="values",
            ):
                if "messages" in step2:
                    step2["messages"][-1].pretty_print()
```

**執行流程**：

1.  Agent 識別需要 `send_email`
2.  Middleware 攔截並觸發中斷
3.  顯示待審核的工具呼叫資訊
4.  等待用戶輸入決定
5.  根據決定繼續或終止執行

**互動過程**：

```
⏸️  需要人工審核

工具: send_email
參數: {'to': 'john@example.com', 'subject': 'Meeting Tomorrow', 'body': "Let's meet at 2pm"}

approve / reject > approve

✅ 已批准操作，繼續執行...
✉️ Email sent to john@example.com with subject 'Meeting Tomorrow'
```

### 測試案例 3：危險操作（只能批准/拒絕）

```python
delete_config = {"configurable": {"thread_id": "test_delete"}}

for step in agent.stream(
    {"messages": [{"role": "user", "content": "Delete record 123 from users table"}]},
    delete_config,
    stream_mode="values",
):
    if "messages" in step:
        step["messages"][-1].pretty_print()
    elif "__interrupt__" in step:
        print("🛑 危險操作已暫停！")
        
        interrupt = step["__interrupt__"][0]
        for request in interrupt.value["action_requests"]:
            print(f"⚠️ 即將刪除: {request['name']}")
            print(f"參數: {request.get('args', {})}")
            print("此操作無法編輯，只能批准或拒絕")
        
        decision = input("approve / reject > ").strip().lower()
        
        if decision == "approve":
            print("⚠️ 確認執行刪除操作...")
            for step2 in agent.stream(
                Command(resume={"decisions": [{"type": "approve"}]}),
                delete_config,
                stream_mode="values",
            ):
                if "messages" in step2:
                    step2["messages"][-1].pretty_print()
        else:
            print("✅ 已取消刪除操作")
            for step2 in agent.stream(
                Command(resume={"decisions": [{"type": "reject", "message": "User rejected the deletion"}]}),
                delete_config,
                stream_mode="values",
            ):
                if "messages" in step2:
                    step2["messages"][-1].pretty_print()
```

**輸出結果**：

```
🛑 危險操作已暫停！
⚠️ 即將刪除: delete_data
參數: {'table': 'users', 'id': 123}
此操作無法編輯，只能批准或拒絕

approve / reject > reject

✅ 已取消刪除操作
The deletion operation has been cancelled per your request.
```

---

## 進階技巧與延伸應用

### 技巧 1：不同工具不同審核策略

```python
HumanInTheLoopMiddleware(
    interrupt_on={
        # 金融交易：必須審核
        "transfer_money": {
            "allowed_decisions": ["approve", "reject"],
            "description": "💰 金融交易需要審核"
        },
        # 資料修改：必須審核
        "update_user_data": {
            "allowed_decisions": ["approve", "reject"],
            "description": "📝 資料修改需要審核"
        },
        # 查詢操作：自動批准
        "search_users": False,
        "get_account_balance": False,
    }
)
```

### 技巧 2：審核資訊記錄

```python
import logging

logger = logging.getLogger(__name__)

if "__interrupt__" in step:
    interrupt = step["__interrupt__"][0]
    for request in interrupt.value["action_requests"]:
        # 記錄審核請求
        logger.info(f"Approval required: {request['name']} with args {request.get('args')}")
        
        decision = get_user_decision()  # 你的審核邏輯
        
        # 記錄審核決定
        logger.info(f"Decision: {decision} by user {current_user}")
```

### 技巧 3：自動化部分審核

```python
def smart_approval_logic(request):
    """根據規則自動批准部分操作"""
    
    # 金額小於 100 的轉帳自動批准
    if request['name'] == 'transfer_money':
        amount = request.get('args', {}).get('amount', 0)
        if amount < 100:
            return {"type": "approve"}
    
    # 刪除測試環境資料自動批准
    if request['name'] == 'delete_data':
        table = request.get('args', {}).get('table', '')
        if table.startswith('test_'):
            return {"type": "approve"}
    
    # 其他需要人工審核
    return None  # 讓人工決定

# 使用
if "__interrupt__" in step:
    auto_decision = smart_approval_logic(request)
    
    if auto_decision:
        # 自動批准
        decision = auto_decision
    else:
        # 人工審核
        decision = get_user_input()
```

### 技巧 4：整合通知系統

```python
async def send_approval_notification(request):
    """發送審核通知到 Slack/Email"""
    
    message = f"""
    🔔 需要你的審核
    
    操作: {request['name']}
    參數: {request.get('args')}
    時間: {datetime.now()}
    
    請到系統進行審核
    """
    
    await slack_client.send_message(
        channel="#approvals",
        text=message
    )

# 在中斷時使用
if "__interrupt__" in step:
    await send_approval_notification(request)
```

### 應用場景

| 場景 | 需要審核的操作 | 自動批准的操作 |
|------|---------------|--------------|
| 郵件系統 | 發送郵件、批量發送 | 查看郵件、搜尋 |
| 資料管理 | 刪除、修改、匯出 | 查詢、統計 |
| 財務系統 | 轉帳、退款、調整 | 查詢餘額、交易記錄 |
| DevOps | 部署生產、刪除資源 | 查看狀態、日誌 |
| 客服系統 | 退款、關閉帳號 | 查詢訂單、FAQ |

---

## 常見問題與解決方案

### Q1: 為什麼我的 Agent 沒有停下來等審核？

**A**: 檢查這三點：

1.  **必須使用 `stream()` 而不是 `invoke()`**

```python
# ❌ 錯誤
result = agent.invoke(...)

# ✅ 正確
for step in agent.stream(..., stream_mode="values"):
    if "__interrupt__" in step:
        # 處理中斷
```

2.  **必須配置 checkpointer**

```python
agent = create_agent(
    model=model,
    tools=tools,
    middleware=[HumanInTheLoopMiddleware(...)],
    checkpointer=InMemorySaver(),  # 必須！
)
```

3.  **確認工具在 interrupt_on 中設定正確**

```python
interrupt_on={
    "your_tool": True,  # 或 {"allowed_decisions": [...]}
    # 而不是 False
}
```

### Q2: 如何處理多個工具同時需要審核？

**A**: `decisions` 陣列按照 `action_requests` 的順序提供決定

```python
if "__interrupt__" in step:
    interrupt = step["__interrupt__"][0]
    decisions = []
    
    for request in interrupt.value["action_requests"]:
        print(f"審核 {request['name']}")
        decision = input("approve / reject > ")
        decisions.append({
            "type": decision,
            "message": f"Decision for {request['name']}"
        })
    
    # 一次提供所有決定
    Command(resume={"decisions": decisions})
```

### Q3: 生產環境應該用什麼 checkpointer？

**A**: 使用持久化的 checkpointer

```python
from langgraph.checkpoint.postgres import AsyncPostgresSaver

# 生產環境使用 PostgreSQL
checkpointer = AsyncPostgresSaver(
    connection_string="postgresql://..."
)

agent = create_agent(
    model=model,
    tools=tools,
    middleware=[HumanInTheLoopMiddleware(...)],
    checkpointer=checkpointer,  # 持久化
)
```

---

## 結語

這次我們示範了如何使用 **HumanInTheLoopMiddleware** 讓 AI Agent 具備審核機制：

*   **暫停執行**：在敏感操作前停下來
*   **等待決定**：顯示操作資訊並等待批准/拒絕
*   **繼續執行**：根據審核結果決定後續動作
*   **靈活配置**：不同工具不同審核策略

這是從「全自動 AI Agent」到「可控、安全的 AI Agent」的關鍵一步。

### 核心要點回顧

| 要點 | 說明 |
|------|------|
| 使用 `stream()` | 必須用 `stream()` 才能檢測 `"__interrupt__"` |
| 配置 checkpointer | 必須有 checkpointer 才能暫停/恢復 |
| 檢查 `__interrupt__` | 這是中斷的訊號 |
| 使用 `Command(resume={...})` | 提供審核決定讓 Agent 繼續 |
| 相同 thread_id | resume 時必須使用相同的 config |

### 相關資源

*   [LangChain 1.0 Middleware 文件](https://docs.langchain.com/oss/python/langchain/middleware)
*   [Human-in-the-Loop 完整指南](https://docs.langchain.com/oss/python/langchain/human-in-the-loop)
*   [本文完整程式碼](https://github.com/jason8745/llm-notebook/tree/master/tool_calling/middleware)

### 完整環境配置

**依賴套件**：

```bash
uv add langchain langchain-openai langgraph python-dotenv rich
```

**.env 設定**：

```
AZURE_OPENAI_ENDPOINT="https://your-endpoint.openai.azure.com/"
AZURE_OPENAI_API_KEY="your-api-key"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
AZURE_OPENAI_DEPLOYMENT_NAME="gpt-4.1"
```

**執行範例**：

```bash
cd tool_calling/middleware
uv run python scenario1_human_in_the_loop.py
```

**Tags**: `#LangChain` `#Middleware` `#Human-in-the-Loop` `#AI Agent` `#Azure OpenAI` `#Python`

---

## 延伸閱讀

*   [💰 LangChain Middleware 實戰（二）：Summarization 讓 AI 自動壓縮對話，省錢又高效](/blog/langchain-middleware-summarization-ai) — 系列第二篇：Context 壓縮 Middleware，解決 token 成本暴增問題
*   [📋 LangChain Middleware 實戰（三）：TodoList 讓 AI 自動管理任務清單，複雜流程零遺漏](/blog/langchain-middleware-todolist-ai) — 系列第三篇：任務追蹤 Middleware，多步驟工作流程不再漏步驟
*   [Harness Engineering — AI 工程師的第三個維度](/blog/harness-engineering-ai) — Human-in-the-Loop 是 Harness 的核心控制機制之一：理解它在整體設計的位置

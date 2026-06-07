---
url: "https://warmwater.dev/blog/langchain-1-0-tool-calling-ai-agent"
title: "LangChain 1.0 Tool Calling 實戰：讓 AI Agent 學會使用工具"
date: 2025-11-13
category: Tutorial
source: warmwater.dev
---

# 🔧 LangChain 1.0 Tool Calling 實戰：讓 AI Agent 學會使用工具

2025-11-13

如果你曾經想過：

> 「我能不能讓 AI 自己決定要用哪個工具來完成任務？」

那你來對地方了！這篇文章要帶你體驗 LangChain 1.0 的 Tool Calling 功能，讓你的 AI Agent 不只會聊天，還能根據情境自動選擇並執行工具。

## Tool Calling 是什麼？

Tool Calling（工具調用）是讓 LLM 能夠「理解何時需要外部工具」，並且「自動呼叫適當的函式」來完成任務的能力。

你可以想像成：

```
你問模型：「東京現在幾點？天氣如何？」
模型心裡想：「這需要兩個工具！先查時間，再查天氣」
模型自動呼叫：get_current_time("PST") 和 get_weather("Tokyo")
模型整合結果：「東京目前是晴天！PST 時區現在是...」
```

相比傳統 LLM 只能「猜測」或「編造」答案，Tool Calling 讓 AI 能夠：

- **取得即時資訊**（天氣、股價、新聞）
- **執行實際操作**（發送郵件、資料庫查詢、API 呼叫）
- **處理複雜任務**（多步驟推理 + 工具組合）

### 我們這次用到的工具組合

| 工具 | 用途 |
|------|------|
| LangChain 1.0 | 串接 Agent 和工具的核心框架 |
| AzureChatOpenAI | 使用 Azure OpenAI 的 GPT 模型 |
| @tool 裝飾器 | 把 Python 函式變成 LangChain 工具 |
| create_agent | LangChain 1.0 的新標準 API |
| python-dotenv | 管理環境變數和配置 |
| Rich | 美化終端輸出 |

---

## 動手做：打造一個多功能 AI Agent

來看我們的核心實作 👇

```python
import os
from dotenv import load_dotenv
from langchain_openai import AzureChatOpenAI
from datetime import datetime
import pytz
from langchain.agents import create_agent
from langchain.tools import tool
from rich import print as rprint

# Load environment variables from .env file
load_dotenv()

# Initialize Azure OpenAI model explicitly
model = AzureChatOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    temperature=0,
)

@tool
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"

@tool
def calculate_temperature(fahrenheit: float) -> str:
    """Convert Fahrenheit to Celsius."""
    celsius = (fahrenheit - 32) * 5/9
    return f"{fahrenheit}°F is {celsius:.1f}°C"

@tool
def get_current_time(timezone: str = "UTC") -> str:
    """Get current time in a specific timezone. Supported: UTC, PST, EST."""
    timezone_map = {
        "UTC": "UTC",
        "PST": "America/Los_Angeles",
        "EST": "America/New_York"
    }
    
    tz = pytz.timezone(timezone_map.get(timezone, "UTC"))
    current_time = datetime.now(tz)
    return f"Current time in {timezone}: {current_time.strftime('%Y-%m-%d %H:%M:%S')}"

# Create agent using LangChain 1.0 standard API
agent = create_agent(
    model=model,
    tools=[get_weather, calculate_temperature, get_current_time],
    system_prompt="You are a helpful assistant",
)

# Run the agent
result = agent.invoke(
    {"messages": [{"role": "user", "content": "What's the weather in Tokyo? Also, what time is it in PST timezone?"}]}
)

rprint(result)
```

**這裡是重點：**

- **@tool 裝飾器**：把普通 Python 函式變成 LangChain 可用的工具
- **docstring 超重要**：LLM 會讀 docstring 來決定何時使用這個工具
- **create_agent**：LangChain 1.0 的新標準 API，取代舊的 AgentExecutor
- **自動工具選擇**：Agent 會根據問題自動決定要呼叫哪些工具

這就是一條完整的「先理解需求 → 選擇工具 → 執行 → 整合回答」的 Agent 流程。

---

## 核心概念拆解

### 1. 為什麼要用 @tool 裝飾器？

```python
@tool
def get_weather(city: str) -> str:
    """Get weather for a given city."""
    return f"It's always sunny in {city}!"
```

`@tool` 會做這些事：

- 自動解析函式簽名（參數類型、名稱）
- 把 docstring 轉成工具描述
- 生成 JSON Schema 讓 LLM 理解工具用法
- 包裝成 LangChain Tool 物件

### 2. LangChain 1.0 的 create_agent 有什麼不同？

**舊版（LangChain < 1.0）**：

```python
# 需要手動建立 AgentExecutor
agent = create_tool_calling_agent(llm, tools, prompt)
agent_executor = AgentExecutor(agent=agent, tools=tools)
result = agent_executor.invoke({"input": "question"})
```

**新版（LangChain 1.0）**：

```python
# 一行搞定！
agent = create_agent(model=model, tools=tools, system_prompt="...")
result = agent.invoke({"messages": [...]})
```

優勢：

- **更簡潔**：不需要手動建立 AgentExecutor
- **更靈活**：支援 middleware、context schema
- **更標準**：統一的訊息格式

### 3. 明確初始化 AzureChatOpenAI 的好處

```python
model = AzureChatOpenAI(
    azure_endpoint=os.getenv("AZURE_OPENAI_ENDPOINT"),
    api_key=os.getenv("AZURE_OPENAI_API_KEY"),
    api_version=os.getenv("AZURE_OPENAI_API_VERSION"),
    azure_deployment=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME"),
    temperature=0,
)
```

這樣做的好處：

- **配置明確**：所有參數一目了然
- **易於調整**：可以輕鬆修改 temperature、timeout 等參數
- **不依賴環境變數自動檢測**：從任何 config 來源讀取都可以
- **更好 debug**：出問題時能快速定位配置錯誤

---

## 實際測試

```python
result = agent.invoke({
    "messages": [{
        "role": "user", 
        "content": "What's the weather in Tokyo? Also, what time is it in PST timezone?"
    }]
})
```

**執行流程**：

1. Agent 分析問題：「需要查天氣 + 查時間」
2. 自動呼叫 `get_weather("Tokyo")`
3. 自動呼叫 `get_current_time("PST")`
4. 整合結果並回答

**輸出結果**：

```
It's always sunny in Tokyo! 
The current time in PST timezone is 2025-11-13 08:30:15
```

---

我們可以看到，雖然我們有三個Tool，但Agent在理解了問題後，只使用了兩個Tool (Agent判斷問題跟溫度無關)

## 進階技巧與延伸應用

### 技巧 1：工具的 docstring 設計

```python
@tool
def search_database(query: str, limit: int = 10) -> str:
    """
    Search the company database for relevant information.
    
    Args:
        query: The search query string
        limit: Maximum number of results to return (default: 10)
    
    Returns:
        JSON formatted search results
    """
    # Implementation here
```

**要點**：

- 寫清楚功能、參數、回傳值
- 使用自然語言描述，LLM 更容易理解
- 提供預設值範例

### 技巧 2：錯誤處理

```python
@tool
def risky_operation(param: str) -> str:
    """Perform a risky operation that might fail."""
    try:
        # Actual operation
        result = some_api_call(param)
        return f"Success: {result}"
    except Exception as e:
        return f"Error: {str(e)}"
```

### 技巧 3：多 Agent 協作

| 應用場景 | 工具組合 |
|---------|---------|
| 資料分析 Agent | `query_database` + `generate_chart` + `statistical_analysis` |
| 客服 Agent | `search_faq` + `create_ticket` + `send_email` |
| 開發助手 Agent | `search_docs` + `run_code` + `git_commit` |

### 技巧 4：使用 Rich 美化輸出

```python
from rich import print as rprint
from rich.console import Console
from rich.table import Table

console = Console()

# 建立漂亮的表格
table = Table(title="Agent Execution Results")
table.add_column("Tool", style="cyan")
table.add_column("Status", style="green")
table.add_column("Result")

table.add_row("get_weather", "✅ Success", "Sunny in Tokyo")
table.add_row("get_current_time", "✅ Success", "2025-11-13 08:30")

console.print(table)
```

---

## 結語

這次我們示範了如何在 LangChain 1.0 中實作 Tool Calling，讓 AI Agent 能夠：

- **理解任務需求**
- **自動選擇工具**
- **執行實際操作**
- **整合結果回答**

這是從「純聊天機器人」到「具備行動能力的 AI Agent」的關鍵一步。

### 未來可以應用在

- **企業自動化**：串接內部系統 API
- **資料分析助手**：自動查詢、分析、視覺化
- **客服機器人**：查詢訂單、處理退款、發送通知
- **研究助手**：搜尋論文、整理資料、生成報告
- **辦公助手**：管理行事曆、發送郵件、整理文件

### 相關資源

- [LangChain 1.0 官方文件](https://docs.langchain.com/oss/python/releases/langchain-v1/)
- [Azure OpenAI 文件](https://learn.microsoft.com/zh-tw/azure/ai-services/openai/)
- [本文完整程式碼](https://github.com/jason8745/llm-notebook/tree/master/tool_calling)

### 完整環境配置

**依賴套件**：

```
uv add langchain langchain-openai python-dotenv rich pytz
```

**.env 設定**：

```
AZURE_OPENAI_ENDPOINT="https://your-endpoint.openai.azure.com/"
AZURE_OPENAI_API_KEY="your-api-key"
AZURE_OPENAI_API_VERSION="2024-12-01-preview"
AZURE_OPENAI_DEPLOYMENT_NAME="gpt-4.1"
```

**Tags**: `#LangChain` `#LLM` `#AI Agent` `#Tool Calling` `#Azure OpenAI` `#Python`

---

## 延伸閱讀

- [🔧 讓 LLM 用上 Tools！用 DuckDuckGo 強化 AI 回答能力 🦆💡](/blog/llm-tools-duckduckgo-ai) — 早期版本的 Tool 整合：對比看 LangChain 1.0 的 Tool Calling 設計改進
- [🛡️ LangChain Middleware 實戰（一）：Human-in-the-Loop 讓 AI 學會等待人類審核](/blog/langchain-middleware-human-in-the-loop-ai) — Tool Calling 之後：在 tool 執行前加上人工審核的 Middleware 設計
- [LangChain vs LangGraph vs DeepAgents：該選哪個 AI Agent 框架？](/blog/langchain-vs-langgraph-vs-deepagents-ai-agent) — 當 Tool Calling 不夠用時：框架升級的決策指南

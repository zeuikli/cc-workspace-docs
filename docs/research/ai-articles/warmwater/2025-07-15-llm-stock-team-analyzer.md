---
url: "https://warmwater.dev/blog/llm-stock-team-analyzer"
title: "打造智能股票分析團隊：LLM Stock Team Analyzer"
date: 2025-07-15
category: "Stock&Finance"
source: warmwater.dev
---

[
← Stock & Finance ](/blog?tag=Stock%20%26%20Finance)  Stock & Finance  
#  打造智能股票分析團隊：LLM Stock Team Analyzer 
  2025-07-15 · — views      

> **關鍵字**: LLM、AI 工具、技術分析、自動化、開源專案、金融資料、ChatGPT 應用、RAG 機制、ChromaDB、LangGraph\


> **摘要**: 學習如何使用 LLM Stock Team Analyzer 打造多智能體股票分析系統，結合技術分析與新聞情緒分析，實現自動化投資決策支援。


在這個 AI 當道的時代，你是否曾經想過讓多個 **LLM** 智能體像專業分析師團隊一樣，協力為你分析股票投資機會？今天要介紹的這個**開源專案** **LLM Stock Team Analyzer**，正是實現這個夢想的絕佳 **AI 工具**！


這個創新的 **ChatGPT 應用** 不僅整合了先進的 **RAG 機制** 和 **ChromaDB** 向量資料庫，更透過 **LangGraph** 框架實現了完全**自動化**的股票分析流程，讓你輕鬆獲得專業級的**金融資料**分析結果。

## 🎯 為什麼需要這個 AI 工具？


傳統的**技術分析**往往依賴單一觀點，不論是技術分析還是基本面分析，都容易有盲點。而這個專案的核心理念是：**讓多個 LLM 智能體扮演不同角色的分析師，透過協作與辯論，產生更全面、更客觀的投資建議**。


這個**自動化**分析系統能夠處理大量**金融資料**，並透過先進的 **RAG 機制** 提供準確的市場洞察。


想像一下，你有一個分析師團隊，包含：


- 專精技術分析的市場分析師 📈

- 擅長新聞情報的新聞分析師 📰

- 看多的研究員（多頭觀點）🐂

- 看空的研究員（空頭觀點）🐻

- 最終決策的交易員 💼


這些智能體會針對同一檔股票進行深度分析與辯論，最後綜合出投資建議。是不是很酷呢？

## 🌟 適用場景


這個工具特別適合以下情境：


- **個人投資者**：想要獲得多角度的股票分析，避免單一思維盲點

- **技術學習者**：想了解如何使用 **LangGraph** 建構多智能體系統的開發者

- **金融科技愛好者**：對 **AI 工具** 在金融領域應用有興趣的朋友

- **量化交易員**：需要**自動化**分析工具來處理大量**金融資料**的專業人士


舉個實際例子：當你想分析 NVIDIA (NVDA) 股票時，這個**AI 工具**會**自動化**執行以下流程：


- 抓取 Yahoo Finance 的價格與**技術分析**指標數據

- 收集 Google News 的相關新聞進行情緒分析

- 讓多頭與空頭研究員進行投資觀點辯論

- 透過 **LLM** 生成綜合性的投資建議


整個過程完全**自動化**，就像有一個專業的分析師團隊為你工作！

## ✨ 功能亮點


### 🤖 多智能體協作架構


- **市場分析師**：智能選擇 2-3 個互補的技術指標進行分析

- **新聞分析師**：Google News 情緒分析與事件影響評估

- **多空研究員**：進行結構化的投資觀點辯論

- **交易員**：綜合所有分析產生最終建議


### 📊 智慧**技術分析**與**自動化**決策


- **自動化指標組合**：根據市場狀況智能選擇最適合的**技術分析**指標

- **四大分析策略**：


- 📈 趨勢追蹤：20/10/5MA + MACD + ADX（完全**自動化**選擇）

- 💥 波動突破：布林通道 + KDJ + ATR

- 🔁 反轉偵測：RSI + OBV + MACD 背離分析

- ⚖️ 風險評估：ATR + 布林通道 + RSI


### 🎯 先進**AI 工具**特色


- **本地部署**：完全在本地運行，確保**金融資料**安全

- **狀態追蹤**：完整的**自動化**分析流程狀態監控

- **智能記憶**：使用 **ChromaDB** 向量資料庫實現 **LLM** 學習能力

- **PDF 摘要**功能：可擴充支援財報等文件的智能摘要（未來功能）


### 背後的技術亮點


- **LangGraph**：智能體工作流程編排

- **RAG 機制**：結合檢索增強生成提升分析品質

- **ChromaDB**：向量資料庫實現記憶與學習

- **Azure OpenAI**：強大的 LLM 推理能力


## 🚀 安裝與使用教學


### 前置需求


- Python 3.12+ 或 Docker

- Azure OpenAI API 存取權限

- 網路連線（用於抓取 Yahoo Finance 和 Google News 資料）


### 方法一：本地安裝（推薦初學者）


- **Clone 專案**


```
git clone https://github.com/jason8745/llm-stock-team-analyzer.git
cd llm-stock-team-analyzer

```


- **安裝相依套件**


```
# 使用 uv（推薦，速度更快）
uv sync

```


- **設定配置檔**


```
# 複製配置模板
cp llm_stock_team_analyzer/configs/config.example.yaml llm_stock_team_analyzer/configs/config.yaml

# 編輯配置檔，填入你的 Azure OpenAI 資訊
nano llm_stock_team_analyzer/configs/config.yaml

```


配置檔範例：

```
azure_openai:
  endpoint: "https://your-endpoint.openai.azure.com/"
  api_version: "2024-12-01-preview"
  deployment: "your-deployment-name"
  subscription_key: "your-subscription-key"

llm:
  temperature: 0.5
  max_tokens: 4096
  max_debate_rounds: 2

rate_limiting:
  enabled: true
  requests_per_minute: 5
  delay_between_requests: 12

```


- **執行分析**


```
# 使用 uv
uv run python main.py

# 或直接執行
python main.py

```


### 方法二：Docker 部署（推薦進階使用者）


- **Build Image**


```
# 基本建構
./build.sh

# 建構特定版本
./build.sh v1.0.0

# 建構安全版本（distroless）
./build.sh --secure

```


- **執行容器**


```
# 使用執行腳本（推薦）
./run.sh --config ./my-config.yaml --data ./output

# 或直接使用 docker
docker run -it \
  -v $(pwd)/llm_stock_team_analyzer/configs/config.yaml:/app/llm_stock_team_analyzer/configs/config.yaml \
  llm-stock-analyzer:latest

```


### 實際使用範例


執行後，你會看到類似這樣的互動界面：

```
🔍 LLM Stock Team Analyzer
AI-Powered Multi-Agent Stock Analysis Framework

Enter stock ticker symbol [AAPL]: NVDA
Enter analysis date [2025-07-15]: 2025-07-15

🚀 Starting Multi-Agent Analysis Workflow

► Market analyst triggered tools: ['get_YFin_data']
► Market analyst triggered tools: ['get_stockstats_indicators_report']
► News analyst triggered tools: ['get_google_news']

✅ Analysis Complete!

```


系統會**自動化**產生包含以下內容的完整分析報告：


- 📈 **技術分析報告**：多指標綜合分析、支撐阻力位、趨勢方向評估

- 📰 **新聞情緒分析**：相關新聞摘要、情緒評分、市場影響分析

- 🎯 **投資觀點辯論**：多空雙方論點與深度分析（**ChatGPT 應用**展現）

- 💰 **最終投資建議**：綜合投資評級、具體操作建議、風險控制策略


## 🛠️ 進階自訂與擴充


這個專案的設計非常模組化，你可以根據需求進行各種客製化：

### 1. 增加自訂分析師節點


想要加入更多分析師？很簡單！你可以在 `agents/` 目錄下新增自己的分析師：

```
def create_custom_analyst(llm, toolkit):
    def custom_analyst_node(state):
        # 你的自訂分析邏輯
        system_message = """你是專精某領域的分析師..."""
        # 分析邏輯實作
        pass
    return custom_analyst_node

```


### 2. 強化 **RAG 機制** 與 **PDF 摘要** 功能


目前專案已整合 **ChromaDB** 作為向量資料庫，你可以進一步擴充 `FinancialSituation` 記憶機制。這個 **RAG 機制** 讓系統能夠從歷史分析中學習，提升**金融資料**分析的準確性：

```
# 在 llm_stock_team_analyzer/agents/utils/memory.py 中
class FinancialSituationMemory:
    def __init__(self, name, config):
        # 使用 HuggingFace 嵌入模型實現 RAG 機制
        self.embedding_model = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2"
        )
        # 建立 ChromaDB 客戶端
        self.chroma_client = chromadb.Client()

```


未來還可以加入 **PDF 摘要** 功能，讓系統能夠自動分析公司財報、研究報告等 PDF 文件。

### 3. 新增台股分析工具


特別推薦加入以下台股專用分析工具：


- **台指期多空指標**：分析期貨未平倉量變化

- **選擇權 PC Ratio**：Put/Call 比值分析市場情緒

- **三大法人買賣超**：外資、投信、自營商資金流向

- **融資融券變化**：散戶情緒指標


你可以在 `dataflows/` 目錄下新增這些工具：

```
@tool
def get_taiwan_futures_oi(date: str) -> str:
    """取得台指期未平倉量數據"""
    # 實作台指期數據抓取邏輯
    pass

@tool  
def get_options_pc_ratio(date: str) -> str:
    """計算選擇權 Put/Call 比值"""
    # 實作選擇權數據分析
    pass

```


## 💡 開發者小技巧


### 程式碼品質控制


專案已整合完整的開發工具鏈：

```
# 程式碼格式化
uv run ruff format .

# 程式碼檢查
uv run ruff check --select I --fix .

# 執行測試
uv run pytest tests/ -v

```


### 除錯模式


在初始化時啟用 debug 模式，可以看到詳細的執行流程：

```
graph = TradingAgentsGraph(
    selected_analysts=["market", "news"], 
    debug=True  # 啟用除錯模式
)

```


## 🔮 未來發展方向


這個專案還有很多擴充的可能性：

### 短期規劃


- [] 支援更多技術指標

- [] 實作自動指標組合優化演算法

- [] 增強風險管理模組

- [] 多語言介面支援


### 長期願景


- [] 加密貨幣分析支援

- [] 機器學習預測模組

- [] 即時資料流處理

- [] 投資組合優化建議


## 🎉 總結：打造你的專業**AI 工具**


LLM Stock Team Analyzer 不只是一個股票分析工具，更是一個展示多智能體協作的絶佳**開源專案**。透過這個創新的 **ChatGPT 應用**，你可以：


- 🎯 **獲得多角度的投資分析**：避免單一觀點的盲點，透過**自動化**流程

- 🛠️ **學習現代 AI 技術**：深入了解 **LangGraph**、**RAG 機制**、**ChromaDB** 等尖端技術

- 🚀 **建構自己的 AI 工具**：模組化設計讓擴充變得超級簡單

- 📊 **處理大量金融資料**：**自動化**分析讓你事半功倍

- 🤖 **體驗 LLM 的強大能力**：看見人工智慧在金融分析的實際應用


如果你對這個專案感興趣，非常歡迎：


- ⭐ 給專案一個 Star

- 🍴 Fork 後進行自己的客製化

- 🐛 提出 Issue 回報問題或建議新功能

- 🔧 貢獻 Pull Request 一起改善專案


記住，投資有風險，AI 分析僅供參考，實際投資決策還是要謹慎評估！

## 📚 延伸閱讀


- [專案原始碼](https://github.com/jason8745/llm-stock-team-analyzer)

- [LangGraph 官方文件](https://python.langchain.com/docs/langgraph)

- [ChromaDB 向量資料庫介紹](https://docs.trychroma.com/)

- [Azure OpenAI 服務設定指南](https://docs.microsoft.com/azure/cognitive-services/openai/)


---


*本文介紹的專案靈感來源於 [TradingAgents](https://github.com/TauricResearch/TradingAgents)，感謝開源社群的貢獻！*

## 🏷️ 相關標籤與關鍵字


**技術標籤**: #LLM #ChatGPT應用 #LangGraph #RAG機制 #ChromaDB #AI工具 #自動化 #開源專案\


**應用標籤**: #技術分析 #金融資料 #股票分析 #投資工具 #量化交易 #PDF摘要\


**程式語言**: #Python #Docker #Azure #OpenAI

---


## 🔍 常見問題 FAQ


### Q: 這個 AI 工具需要什麼技術背景？


A: 基本的 Python 知識即可開始使用。進階功能需要了解 LangGraph 和 RAG 機制。

### Q: 可以分析台股嗎？


A: 目前支援全球主要市場，台股代碼請使用 `.TW` 後綴（如 2330.TW）。

### Q: 這個自動化系統的準確度如何？


A: 作為 AI 工具，提供參考建議，實際投資請搭配個人判斷。

### Q: 可以擴充 PDF 摘要功能嗎？


A: 是的！專案架構支援擴充，可加入財報 PDF 分析功能。

---


*本文詳細介紹了 LLM Stock Team Analyzer 這個創新的開源專案，展示了如何結合 LangGraph、RAG 機制、ChromaDB 等技術，打造一個完全自動化的股票分析 AI 工具。無論你是想學習技術分析、尋找實用的金融資料處理工具，還是對 ChatGPT 應用開發有興趣，這個專案都能提供豐富的學習價值。*

---


## 延伸閱讀


- [TradingAgents: Multi-Agents LLM Financial TradingFramework](/blog/tradingagents-multi-agents-llm-financial-tradingframework) — 這個專案的靈感來源：論文原型與多代理金融交易框架的完整設計

- [🤖 LLM Agent Trader: 當ChatGPT遇上股票交易，我打造了一個會思考的交易機器人](/blog/llm-agent-trader-chatgpt) — 另一條路：直接把 LLM 接上實盤交易決策

- [RAG 典範轉移：從向量檢索到結構化檢索](/blog/rag) — 專案的 RAG 機制深入版：向量檢索 vs. 結構化檢索的取捨
     [ Stock & Finance ](/blog?tag=Stock%20%26%20Finance)[ Implement ](/blog?tag=Implement)  
### 
相關文章

[Implement用 RPG 架構評估 SRE Agent：Kube Arena 設計紀錄2026-05-28](/blog/kube-arena)[Harness EngineeringSelf Escalate Agent：刻意設計成不完整的 AI2026-05-09](/blog/self-escalate-agent)[Implement不靠直覺，靠實驗：用 AutoResearch 找到 C++ 的 33x 優化空間2026-04-17](/blog/autoresearch-c-33x)

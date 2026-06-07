---
url: "https://warmwater.dev/blog/pr-review-llmpr-2025"
title: "從 PR Review 中學習：用 LLM 分析PR | 2025"
date: 2025-07-23
category: Implement
source: warmwater.dev
---

# 🚀 從 PR Review 中學習：用 LLM分析PR | 2025

2025-07-23

> **關鍵字：** AI 程式碼分析、GitHub PR Review、開源工具、LLM 應用、程式碼品質、自動化分析、技術學習、Code Review 工具、軟體開發、ChatGPT 應用

**🔥 2025年最新！** 想從資深工程師的 PR 審查中偷師學藝嗎？每次看到同事的 PR 評論都覺得很有道理，但總是缺乏系統性的整理與學習？今天要介紹一個**超實用的開源工具** —— **LLM PR Review Analyzer**，它能夠自動分析 GitHub PR 審查意見，並用 **AI 人工智慧**幫你萃取出寶貴的技術洞察！

身為**軟體工程師**，我們都知道**程式碼審查**（Code Review）是提升程式品質和團隊技術水準的重要環節。但往往在忙碌的開發節奏中，我們很容易錯過從 Reviewer 意見中學習的機會。這個**AI 驅動的分析工具**正是為了解決這個痛點而生！

## 📊 工具數據一覽

| 特色 | 說明 |
|------|------|
| 🎯 **AI 模型** | Azure OpenAI GPT-4 |
| 🔧 **支援平台** | GitHub.com + Enterprise GitHub |
| 📝 **輸出格式** | 中文 Markdown 報告 |
| ⚡ **分析速度** | < 30 秒完成分析 |
| 💰 **授權** | MIT 開源免費 |
| 🌟 **GitHub Stars** | 持續增長中 |

## 🎯 什麼情況下特別需要這個 AI 工具？

### 1. 新人快速成長 💪 | Junior Developer 必備工具

**情境**：剛加入團隊的新工程師，想要快速了解團隊的程式碼風格和最佳實踐

**效果**：自動整理出「錯誤處理最佳實踐」、「程式碼風格指南」、「架構設計原則」等學習重點

### 2. 技術債務盤點 📊 | Tech Lead 團隊管理神器

**情境**：Tech Lead 想了解團隊在哪些技術領域需要加強

**效果**：發現團隊在「測試覆蓋率」、「API 設計」等方面的共同盲點

### 3. 知識萃取與傳承 🎓 | 企業知識管理解決方案

**情境**：資深工程師即將離職，想要保留他的 Review 智慧

**效果**：產生結構化的技術指導文件，讓知識不會因人員異動而流失

## ✨ 2025 年最強功能亮點整理

### 🤖 智慧化 AI 分析 | 業界領先技術

*   使用 **Azure OpenAI GPT-4** 和 **LangChain** 最新技術棧
*   **智能分類**：自動分類 Review 意見為程式碼風格、錯誤處理、架構設計、測試、文件等類別
*   **中文優化**：專為繁體中文工程師設計，支援中文技術術語識別
*   **多語言支援**：支援 Python、JavaScript、Go、Java、C# 等主流程式語言

### 📊 結構化報告格式 | 專業級分析報告

**AI 自動生成 5 大專業區塊**：

1.  **🧠 核心知識洞察** - Reviewer 展現的技術專業領域深度分析
2.  **🎯 立即行動項目** - 可直接執行的改善建議清單
3.  **🎓 導師級技術指導** - 高階技術原則與業界最佳實踐
4.  **✨ Code Style 洞察** - 程式碼風格與開發哲學提煉
5.  **💬 專業回覆建議** - 包含 GitHub Copilot 指令的實用回覆範本

### 🔗 企業級 GitHub 支援 | 安全可靠

*   ✅ **GitHub.com** 完整支援
*   ✅ **Enterprise GitHub** 企業版相容
*   ✅ **API Token** 安全管理
*   ✅ **自動重試**：處理 API 限制與網路問題
*   ✅ **速率限制**：智能控制請求頻率，避免被封鎖

## 🛠️ 完整安裝與使用教學 | Step-by-Step 詳細指南

> **⚡ 快速開始**：只需 3 個步驟，5 分鐘即可開始使用！

### 步驟一：取得專案 | Git Clone & Setup

```bash
# 從 GitHub 下載最新版本
git clone https://github.com/jason8745/llm-pr-review-analyzer.git
cd llm-pr-review-analyzer

# 使用 uv 安裝依賴（推薦：比 pip 快 10-100 倍）
uv sync

# 驗證安裝
uv run python main.py --help
```

### 步驟二：API Keys 設定 | 安全配置指南

```bash
# 複製設定檔範本
cp src/config/config.example.yaml src/config/config.yaml
```

**編輯 `src/config/config.yaml`，配置您的 API 憑證**：

```yaml
# GitHub 設定 - 支援個人和企業版
github:
  token: "ghp_your_github_token_here"  # GitHub Personal Access Token
  api_base_url: "https://api.github.com"  # 企業版請改為您的 GitHub Enterprise URL

# Azure OpenAI 設定
azure_openai:
  endpoint: "https://your-resource.openai.azure.com/"
  api_version: "2024-02-15-preview"  # 最新 API 版本
  deployment: "gpt-4"  # 推薦使用 GPT-4 獲得最佳分析品質
  api_key: "your_azure_openai_key_here"

# LLM 參數調優 - 針對程式碼分析優化
llm:
  temperature: 0.1  
  max_tokens: 4000  
  retry: 3  # 自動重試機制
```

### 步驟三：開始 AI 分析 | 實戰應用

```bash
# 🎯 基本使用 - 分析任何 GitHub PR
uv run python main.py analyze "https://github.com/microsoft/vscode/pull/12345"

# 💾 儲存分析報告到指定檔案
uv run python main.py analyze "https://github.com/owner/repo/pull/123" --save-to my_analysis.md

# 🔍 詳細模式 - 查看完整分析過程
uv run python main.py analyze "https://github.com/team/project/pull/456" --verbose

# ✅ 驗證設定 - 確保 API 連線正常
uv run python main.py config-check
```

## 💡 深度技術分析 | Architecture Deep Dive

### 🏗️ 模組化架構設計 | Clean Architecture

這個專案採用了**企業級模組化分層架構**，遵循 **Clean Architecture** 原則：

```
# 🎯 核心模組架構 - 清晰的職責分離
src/
├── pr_fetcher.py          # 🔌 GitHub API 整合層 - 處理所有 GitHub 互動
├── comment_preparer.py    # 🧹 資料前處理 - 清理、過濾、分組評論
├── analyzer_chain.py      # 🤖 LLM 分析引擎 - LangChain + GPT-4 核心
├── output_formatter.py    # 📄 報告生成器 - Markdown 格式化輸出
├── cli.py                 # 💻 CLI 介面 - 用戶互動層
├── models/               # 📊 資料模型層
│   ├── github_data.py    # GitHub 資料結構定義
│   └── analysis_result.py # 分析結果資料模型
├── utils/                # 🔧 工具函數庫
│   ├── exceptions.py     # 自定義例外處理
│   ├── logging_config.py # 日誌配置管理
│   └── chain_utils.py    # LangChain 輔助工具
└── config/               # ⚙️ 配置管理
    └── config.py         # 統一配置管理
```

### 🤖 AI 分析流程詳解 | Machine Learning Pipeline

**4 階段智能分析流程**：

1.  **🔍 資料擷取階段**：
    
    *   使用 GitHub REST API v4 獲取 PR 完整資訊
    *   支援 Rate Limiting 和自動重試機制
    *   並發處理多個 API 請求，提升效率
2.  **🧹 資料清理階段**：
    
    *   智能過濾機器人留言（Dependabot、Renovate 等）
    *   按 Reviewer 身份自動分組
    *   移除非實質性評論（如 "LGTM"、"👍"）
3.  **🎯 智慧分析階段**：
    
    *   使用 **LangChain** 框架進行 Prompt Engineering
    *   **GPT-4** 深度語意分析和分類
    *   自動識別技術領域和專業程度
4.  **📊 結構化輸出階段**：
    
    *   Pydantic 資料驗證確保輸出品質
    *   Markdown 模板引擎生成專業報告
    *   支援多種輸出格式擴展

### 🔧 核心技術棧解析 | Technology Stack

*   **[LangChain](https://github.com/langchain-ai/langchain)**：LLM 應用開發框架，處理 AI 工作流
*   **[Azure OpenAI](https://azure.microsoft.com/zh-tw/products/ai-services/openai-service)**：企業級 GPT-4 API 服務
*   **[Pydantic](https://github.com/pydantic/pydantic)**：資料驗證與序列化框架

### 📝 AI Prompt Engineering | 提示工程優化

專案內建了**經過優化的中文提示範本**，針對程式碼審查場景特別調校：

**🎯 核心功能**：

*   **技術分類**：自動識別程式碼風格、架構設計、測試、安全性等技術領域
*   **專業度評估**：分析 Reviewer 的技術深度和經驗水平
*   **可行性建議**：生成具體、可執行的改進建議
*   **回覆模板**：提供專業的英文回覆範本和 GitHub Copilot 指令

**🔍 語言模型優化**：

*   **Temperature: 0.1**：確保分析結果穩定一致
*   **Max Tokens: 4000**：支援詳細的長篇分析
*   **Context Window**：充分利用 GPT-4 的上下文理解能力

讓我們看看一個**真實的 AI 分析報告片段**：

```markdown
## 🧠 AI 智能洞察分析結果

### 核心技術洞察 | AI Deep Analysis

1. **Go 語言最佳實踐**: reviewer 精通 Go 社群標準（如 Uber Go Style Guide），
   強調 early return 模式、減少 if-else 巢狀結構，並深度理解錯誤處理最佳實踐。

2. **架構設計思維**: 展現對微服務架構、API 設計、資料庫優化的深刻理解，
   主張 SOLID 原則和 Clean Architecture 實踐。

### 💬 專業回覆建議 | Professional Response Templates

**AI 生成的英文回覆範本**：
"Thank you for highlighting the Go convention on reducing nesting and early error handling. 
I'll refactor the error checks as suggested to improve readability and maintainability."

**🤖 GitHub Copilot 實用指令**：

Refactor this function to use early return pattern:
1. Move parameter validation to the top
2. Return errors immediately when found
3. Keep the main logic at the lowest indentation level
```

## 🎯 為什麼這個 AI 工具在 2025 年如此重要？

### 🔍 從被動學習到主動挖掘 | Passive to Active Learning

**傳統方式的痛點**：

*   ❌ 只能被動接收 PR Review 意見
*   ❌ 零散的學習沒有系統性
*   ❌ 資深工程師的經驗難以傳承
*   ❌ 團隊知識容易因人員異動而流失

**AI 工具的革命性改變**：

*   ✅ **主動挖掘**：系統性分析技術專家的思考模式
*   ✅ **知識萃取**：自動整理技術洞察和最佳實踐
*   ✅ **個人化學習**：根據個人需求生成客製化報告
*   ✅ **團隊賦能**：提升整體技術水準和 Code Review 品質

## 🚀 立即開始你的 AI 驅動學習之旅 | Get Started Today

### 📚 相關資源與深度學習 | Resources & Further Reading

**📋 專案相關連結**：

*   **GitHub 專案庫**：[llm-pr-review-analyzer](https://github.com/jason8745/llm-pr-review-analyzer)
*   **完整文檔**：[使用手冊與 API 文檔](https://github.com/jason8745/llm-pr-review-analyzer/wiki)
*   **問題回報**：[GitHub Issues](https://github.com/jason8745/llm-pr-review-analyzer/issues)
*   **功能請求**：[Feature Requests](https://github.com/jason8745/llm-pr-review-analyzer/discussions)

**🎓 深度學習資源**：

*   **LangChain 官方教學**：[docs.langchain.com](https://docs.langchain.com/)
*   **Azure OpenAI 服務**：[azure.microsoft.com/ai-services](https://azure.microsoft.com/zh-tw/products/ai-services/openai-service)
*   **GitHub API 文檔**：[docs.github.com/rest](https://docs.github.com/en/rest)
*   **Code Review 最佳實踐**：[Google 工程實踐指南](https://google.github.io/eng-practices/review/)

---

🏷️ **標籤**：`AI工具` `GitHub` `程式碼分析` `開源` `Python` `LLM` `自動化` `Code Review` `軟體開發` `技術學習` `2025`

## 延伸閱讀

*   [Langfuse](/blog/langfuse) — PR 分析完後的下一步：用 Langfuse 監控整個 LLM pipeline 的 trace 與成本
*   [AI Agent 大語言模型輸出評估：如何選擇最佳評估框架？](/blog/ai-agent) — LLM 輸出品質評估的系統化方法，從 G-Eval 到完整的評估框架比較
*   [LLM Agent 完整指南：從架構模式到實務應用](/blog/llm-agent) — 把 PR review 工具升級成 Agent：Tool Calling 與多步驟任務設計

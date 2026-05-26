---
status: SUCCESS
url: "https://github.com/shanraisshan/claude-code-best-practice"
repository: shanraisshan/claude-code-best-practice
date_fetched: 2026-05-18
---

# 36. GitHub: Claude Code Best Practice

## 核心摘要（繁體中文）

該儲存庫是一份關於 Claude Code 開發工作流程的完整指南，涵蓋從基礎概念到進階代理工程模式。强調實踐工作流程而非單純配置，記錄全球團隊使用的 12 種主要開發方法。

### 八項核心功能

1. **Subagents（子代理）**：具有專門上下文的自主代理，避免主會話過度膨脹
2. **Commands（命令）**：透過 `.claude/commands/` 定義重複性工作流程的快捷指令
3. **Skills（技能）**：在 `.claude/skills/` 中組織漸進式功能披露
4. **Workflows（工作流程）**：連接命令、代理和技能的編排模式
5. **Hooks（鉤子）**：事件驅動自動化（PreToolUse、PostToolUse、Stop）
6. **MCP Servers**：模型上下文協議集成
7. **Settings（設定）**：透過 `.claude/settings.json` 的配置
8. **Memory（記憶）**：透過 CLAUDE.md 和 `.claude/rules/` 的上下文管理

### 12 大開發工作流程

儲存庫記錄了全球團隊使用的主要方法學，包括：

- **Superpowers**（188k stars）：Git worktree 驅動開發與子代理實現
- **Everything Claude Code**：Plan → TDD → Code Review → Security → E2E 流程
- **Spec Kit**：基於憲法的規格方法
- **gstack**：CEO/工程/設計審查門檻與 HTML 設計生成
- **BMAD-METHOD**：Epic 驅動故事管理與回顧

**共同模式**：Research → Plan → Execute → Review → Ship

### 進階功能（Beta 與實驗中）

- **Ultrareview**（Beta）：代碼審查與任務追蹤
- **Auto Mode**（Beta）：基於模型的安全權限分類
- **Computer Use**（Beta）：透過 MCP 的桌面自動化
- **Agent Teams**（Beta）：透過 tmux 的並行開發
- **Agent SDK**：用於外部代理系統的 Node/Python 套件
- **Scheduled Tasks**：透過 `/loop` 和 `/schedule` 的循環自動化

### 83 項實踐技巧

組織於九個類別：

**Prompting（提示）**
- 用對比挑戰 Claude，不要微管理實現
- 邊界條件比完整規格更重要

**Planning（計劃）**
- 始終以分階段受控計劃開始
- 每階段包含單元、自動化和整合測試
- 垂直切片優於水平分階段

**Context Management（上下文管理）**
- 300-400k 代幣時出現上下文衰退
- 40% 使用率時性能開始下降；60% 時應考慮結束任務
- `/compact` 搭配提示優於自動壓縮

**Session Management（會話管理）**
- 新任務應建立新會話；相關任務可重用
- 使用 `/rename` 標記重要會話，以便 `/resume`
- 每個轉折都是選擇點：繼續、回溯、清除、壓縮或子代理

**Agent & Skill Design（代理與技能設計）**
- 選擇特定功能的子代理而非通用角色
- 使用 `context: fork` 在隔離子代理中運行技能
- 技能描述應作為觸發條件而非摘要

**開發工作流程**
- 使用 `/rewind` 而非累積修正——回到失敗前的狀態
- 測試時計算：一個代理產生代碼，另一個在隔離環境中查找錯誤
- 跨模型配置：Opus（計劃）+ Sonnet（編碼）+ 思考模式

### 企業應用案例

儲存庫記錄 Claude Code 功能如何替代現有服務：

- **Code Review** 替代 Greptile、CodeRabbit
- **Voice Dictation** 替代 Wispr Flow
- **Computer Use** 替代 OpenAI 的計算機使用代理
- **Agent SDK** 替代 LangChain、CrewAI

### 跨模型整合

支援三種機制整合其他模型（Codex、Gemini、DeepSeek 等）：
- **Plugins**：另一模型的 CLI 在 Claude Code 內執行
- **MCP**：透過模型上下文協議
- **Router**：交換 API 端點至不同提供商

---

## 關鍵數據/引用

### 核心統計

- **83 項具體提示**：涵蓋提示、規劃、上下文、會話、代理、命令、技能和除錯
- **12 種主要工作流程**：來自全球團隊的實踐方法學
- **8 項核心功能**：Claude Code 的主要能力支柱

### 實踐建議（每日工作流程）

1. 根據任務複雜度選擇新會話或現有會話
2. 主動管理上下文——監控使用率，在 40-60% 時規劃變化
3. 使用重新繪製而非修正累積錯誤
4. 為重複性工作構建命令與技能，避免重新提示

### 上下文衰退閾值

- **40%** 使用率：性能開始下降
- **60%** 使用率：應考慮結束任務
- **300-400k** 代幣：明顯衰退開始

---

## 技術棧與工具

- **版本控制**：Git worktree
- **自動化**：MCP、Hooks
- **協調**：Agent Teams、Workflows
- **測試**：TDD、SDD、BDD

---


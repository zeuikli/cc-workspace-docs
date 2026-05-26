# Agent Harness Engineering: The Rise of the AI Control Plane

- **作者**: Adnan Masood
- **平台**: Medium
- **URL**: https://medium.com/@adnanmasood/agent-harness-engineering-the-rise-of-the-ai-control-plane-938ead884b1d
- **發表**: 2026-04
- **收錄日期**: 2026-05-01
- **重要性**: Priority B — 以 Control Plane 視角重新定義 harness 工程；含企業數據支持

---

## 核心論點

「定義 AI 的瓶頸已從模型能力轉向 agent harness。」

模型是無狀態的 token 預測器；harness 是運行時基礎設施，負責工具分派、context 管理和安全強制。

**關鍵統計**: 企業 AI 失敗的 **65% 源自 harness 層缺陷**，而非模型推理限制。

---

## 5 層 Control Plane 架構

| 層次 | 名稱 | 職責 |
|------|------|------|
| 1 | **Context Management** | 系統提示、對話歷史、文件檢索、記憶體壓縮 |
| 2 | **Tool/Function Calling** | 能力暴露（APIs、程式碼執行、MCP servers）、請求路由 |
| 3 | **Execution Loop** | Observe-Think-Act 週期，管理狀態轉換與錯誤恢復 |
| 4 | **State & Memory** | Scratchpads、任務清單、跨 session 持久記憶體 |
| 5 | **Safety & Observability** | 防護欄、權限檢查、審批閘道、審計日誌、追蹤 |

---

## 核心洞見

### 成本優化視角
正確的 cache 管理能將 token 成本降低十倍（$3.00/MTok → $0.30/MTok），無需改變模型。

### 確定性優先於自主性
「混亂的 swarms」被邊界清晰的 workflow 和人類檢查點取代。

### 環境可讀性
系統應被重新設計為對 agent 本質可導航，減少方向迷茫造成的 token 浪費。

### 架構模式
- **Plan-Execute-Verify 迴圈**: 分離規劃、執行、驗證
- **Reasoning Sandwich**: 複雜模型用於規劃/驗證，廉價模型用於中間工作
- **Ralph Loop**: 自動恢復機制

### 買 vs 建策略
- **買（Buy）**: 商品化基礎設施（向量 DB、框架）
- **建（Build）**: 領域特定工具、評估資料集、環境地圖

### 標準化
採用 MCP（Model Context Protocol）和 A2A（Agent-to-Agent）協議統一工具介面。

---

## 與其他 Harness 文章的差異

| 面向 | 本文（Masood）| HumanLayer | Anthropic |
|------|-------------|-----------|-----------|
| 視角 | Control Plane 架構 | 實作配置問題 | 長運行任務設計 |
| 重點 | 成本優化、安全 | Ratchet 積累 | Planner-Evaluator 分離 |
| 數據 | 企業失敗率統計 | Terminal-Bench 量化 | 遊戲引擎案例 |

---

## 與本 Workspace 的對應

| Masood 的 5 層 | Workspace 的實現 |
|--------------|----------------|
| Context Management | context-management.md + /compact 規則 |
| Tool/Function Calling | ToolSearch + MCP tools |
| Execution Loop | agentic loop + hooks |
| State & Memory | Auto Memory + ACTIVE_TASK.md |
| Safety & Observability | security-hygiene.md + PreToolUse hook |

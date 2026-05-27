---
title: "The Anatomy of an Agent Harness"
authors: Daily Dose of DS（Avi Chawla）
source: "https://blog.dailydoseofds.com/p/the-anatomy-of-an-agent-harness"
source_tier: P
---

# The Anatomy of an Agent Harness

- **作者**: Daily Dose of DS（Avi Chawla）
- **平台**: Substack
- **URL**: https://blog.dailydoseofds.com/p/the-anatomy-of-an-agent-harness
- **收錄日期**: 2026-05-01
- **重要性**: Priority B — 目前最完整的 harness 組件分解（11 個生產級組件）

---

## 核心論點

模型不是瓶頸。**Harness 就是產品**，決定了同一底層模型的野生性能差異。

驗證案例：LangChain 只改變基礎設施（不改模型）就從 TerminalBench 2.0 外賽區升至第 5 名。

---

## 11 個生產級 Harness 組件

| # | 組件 | 核心功能 |
|---|------|---------|
| 1 | **Orchestration Loop** | Thought-Action-Observation 週期；系統的心跳 |
| 2 | **Tools** | 帶名稱、描述、參數類型的 schema；執行、驗證、結果格式化 |
| 3 | **Memory** | 短期（對話歷史）+ 長期（跨 session 檔案/資料庫） |
| 4 | **Context Management** | Context rot 對策：壓縮、觀察 masking、即時檢索、子 agent 委派 |
| 5 | **Prompt Construction** | 系統提示 → 工具定義 → 記憶檔案 → 對話歷史的組裝順序 |
| 6 | **Output Parsing** | 原生工具呼叫回傳結構化物件，避免自由文本解析 |
| 7 | **State Management** | 類型化字典追蹤進度；邊界檢查點支援恢復 |
| 8 | **Error Handling** | 四種錯誤類型：暫時性、LLM 可恢復、用戶可修正、意外性 |
| 9 | **Guardrails & Safety** | 三層：輸入層 / 輸出層 / 工具層 |
| 10 | **Verification Loops** | 規則型 / 視覺型 / LLM-as-judge（能提升 2-3 倍品質） |
| 11 | **Subagent Orchestration** | 專門 agent 處理邊界子任務或完整交接 |

---

## 7 項關鍵設計決策

1. **單 vs 多 agent**: 是否需要多個專門 agent 協作？
2. **ReAct vs Plan-Execute**: 推理-行動交錯還是先規劃後執行？
3. **Context 管理策略**: 壓縮、掩蓋、還是委派？
4. **驗證設計**: 哪種 verification loop 適合這個任務？
5. **權限架構**: 哪些行動需要人工審批？
6. **工具範圍**: 哪些工具應該暴露，哪些不應該？
7. **Harness 厚度**: 多少複雜度是必要的，多少是過度設計？

---

## Component 執行循環

```
Context 組裝 → LLM 推理 → 輸出分類 → 工具執行 → 結果包裝 → Context 更新 → 迴圈
```

---

## Scaffolding 原則

隨著模型進步，harness 複雜性應**下降**。好的 harness 是臨時基礎設施：
- V1 Harness: 需要大量輔助（早停、錯誤處理、多次重試）
- Future Harness: 模型本身具備這些能力，harness 變薄

---

## 核心洞見

- Verification 能使品質提升 **2-3 倍**（三種驗證方式各有適用場景）
- Error Handling 要分類四種類型，而非統一處理
- Context Management 是 11 個組件中最被低估的
- Subagent Orchestration 是 Context Firewall 的實現方式

---

## 與本 Workspace 的對應

| Anatomy 組件 | Workspace 的實現 |
|------------|----------------|
| Orchestration Loop | agentic loop + Claude 核心能力 |
| Tools | Bash/Read/Edit/Write + MCP tools |
| Memory | Auto Memory + context-management.md |
| Context Management | /compact + subagent 委派規則 |
| Prompt Construction | CLAUDE.md 分層載入（常駐/按需/手動）|
| Output Parsing | 結構化回傳（TodoWrite、JSON output）|
| State Management | ACTIVE_TASK.md + TodoWrite |
| Error Handling | core.md 驗證規則 + healthcheck.sh |
| Guardrails & Safety | security-hygiene.md + PreToolUse hook |
| Verification Loops | /deep-review skill + healthcheck.sh |
| Subagent Orchestration | subagent-strategy.md |

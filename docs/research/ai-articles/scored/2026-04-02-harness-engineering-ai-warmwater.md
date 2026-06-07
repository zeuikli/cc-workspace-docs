---
url: "https://warmwater.dev/blog/harness-engineering-ai"
date: 2026-04-02
fetched: "2026-05-28"
source: warmwater.dev（一定要配温開水）
source_tier: C
tags: [harness-engineering, context-engineering, prompt-engineering, multi-agent, resource-management, state-persistence, safety-boundary]
---

# Harness Engineering — AI 工程師的第三個維度

**原始來源**：https://warmwater.dev/blog/harness-engineering-ai  
**來源層級**：C（Community blog）

---

## TL;DR

定義 Harness Engineering 為繼 Prompt Engineering 和 Context Engineering 之後的第三個工程層次。核心論點：當 LLM 從文字工具變成執行代理人，需要一套管理「系統層」的工程實踐——資源管理、狀態持久化、信息流控制、安全邊界、任務編排。

---

## 三層架構

```
Harness Engineering（系統層）
    └── Context Engineering（信息層）
            └── Prompt Engineering（訊息層）
```

| 層次 | 核心問題 |
|------|---------|
| Prompt Engineering | 怎麼說才能得到最好的輸出？ |
| Context Engineering | 什麼信息應該在什麼時候進入 context window？ |
| **Harness Engineering** | 怎麼建立一套系統，讓模型能安全、可控地在真實世界行動？ |

---

## 為什麼需要 Harness Engineering

四個驅動因素：

1. **操作有副作用**：刪檔案、API 請求等不可逆操作需要護欄
2. **任務有狀態**：跨多個輪次需要狀態管理機制
3. **系統有成本**：Context window 上限、API 費用限制
4. **複雜任務需協作**：多個代理協調工作

---

## Harness 的五個維度（檢查清單）

| 維度 | 責任範疇 | 實作問題 |
|------|---------|---------|
| **資源管理** | Token 預算、成本控制、熔斷機制 | Context 滿了之後的處理與熔斷？ |
| **狀態持久化** | Memory 系統讓 stateless 模型適應有狀態世界 | 跨 session 知識存儲與讀回機制？ |
| **信息流控制** | Context 壓縮、雙視圖、可見資訊選擇 | 每輪 context 是否精心選擇而非全量塞入？ |
| **安全邊界** | 工具權限、危險操作攔截 | 工具權限和危險操作攔截機制？ |
| **任務編排** | Multi-agent 協調 | 是否需要多 agent 協作？ |

---

## 兩種工作模式

- **有人值守並行（Supervised Parallel）**：主動監管，認知負擔高
- **無人值守並行（Unsupervised Parallel）**：發布後自主完成，需成熟 harness 作為前提

引述原則（Boris Tane）：「永遠不要讓 Agent 在審查計劃前寫程式碼」

---

## 業界趨勢

- **Harness 成為服務模板**（Martin Fowler）：團隊從預製模板選擇，類似 Service Template
- **越做越薄**：Manus 團隊半年重寫五次，方向始終是簡化；Anthropic Claude Managed Agents 將 session 持久化、sandbox 隔離外包給平台
- **更強模型讓 Harness 更重要**（Nicholas Carlini）：模型越強、自主權越大，護欄需越精準；Opus 升級時需重新設計 harness

---

## 延伸閱讀（站內）

- `/blog/langchain-langgraph-harness-engineering-deepagents`
- `/blog/agent-20260423`（三個 Agent 框架設計哲學比較）
- `/blog/llm-session-harness`（LLM Session 設計框架）

---

## 評分摘要

| 維度 | 分數 | 理由 |
|------|------|------|
| A. Workspace 可行動性 | 8/10 | 五維度 Harness 檢查清單（資源/狀態/信息流/安全/編排）直接對應 workspace harness 設計缺口 |
| B. 創新性 | 7/10 | 三層架構（Harness > Context > Prompt）定義明確；Supervised vs Unsupervised 模式分類新穎 |
| C. 證據品質 | 6/10 | 社群 blog，引用 Boris Tane / Martin Fowler / Manus 實作，無直接實驗數據 |
| D. 技術深度 | 7/10 | 五維度 checklist + 業界案例（Manus 重寫五次/Claude Managed Agents），細節充足 |
| E. 泛化性 | 8/10 | 通用於任何 harness 設計場景，不限 Claude Code |
| **加權總分** | **7.25/10** | 8×0.3+7×0.2+6×0.2+7×0.15+8×0.15 = 2.40+1.40+1.20+1.05+1.20 |

**整合決策**：整合（SKILL 補充）  
**整合位置**：補充 `.claude/skills/harness-meta/` 的 Harness 五維度檢查清單；或新建 `.claude/refs/harness-engineering-checklist.md`  
**整合狀態**：待實作

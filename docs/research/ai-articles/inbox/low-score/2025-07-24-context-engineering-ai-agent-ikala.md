---
url: "https://ikala.ai/zh-tw/blog/ikala-ai-insight/introduction-to-context-engineering-ai-agent-vs-prompt-engineering/"
date: 2025-07-24
fetched: "2026-05-28"
source: iKala 部落格
source_tier: C
tags: [context-engineering, prompt-engineering, RAG, agent-memory, lost-in-the-middle, multi-agent, context-compression]
---

# 情境工程（Context Engineering）解析：打造實用 AI Agent 的關鍵技巧

**原始來源**：https://ikala.ai/zh-tw/blog/ikala-ai-insight/introduction-to-context-engineering-ai-agent-vs-prompt-engineering/  
**來源層級**：C（Community / vendor blog，iKala = Google Cloud 合作夥伴）

---

## TL;DR

對情境工程的完整中文入門導覽。核心主張：**AI 系統瓶頸已從模型能力轉向情境品質**。覆蓋 RAG 管線、記憶體架構、多代理協作及企業案例，適合作為情境工程的概念地圖。

---

## 核心定義

> Andrej Karpathy：「情境工程是為大型語言模型的下一步行動在其情境視窗中填入恰到好處的資訊。」

### Prompt Engineering vs. Context Engineering

| 維度 | Prompt Engineering | Context Engineering |
|------|-------------------|---------------------|
| 範疇 | 單一指令 | 整體資訊生態系 |
| 目標 | 優化單次輸出 | 確保多任務多會話一致性 |
| 本質 | 靜態手工指令 | 動態系統組裝資訊 |
| 類比 | 提一個問題 | 準備完整簡報檔案 |

---

## 四種情境失敗模式

1. **情境污染**：幻覺或錯誤資訊滲透情境
2. **情境分心**：無關資訊壓倒核心任務
3. **情境混淆**：結構不良導致非預期回應
4. **情境衝突**：矛盾資訊無法裁決

---

## 情境視窗主要組件

- 系統指令（角色 / 行為準則）
- 使用者輸入
- 記憶體（短期對話歷史 + 長期外部知識）
- 檢索知識（RAG）
- 工具結構描述（Tool schemas）
- 結構化輸出定義
- 跨步驟狀態（State）

---

## 技術重點

### Lost in the Middle（U 型曲線）

LLM 對情境視窗頭尾記憶深刻，中間資訊易被忽略。解法：**重排序（Reranking）**，將最重要資訊放在邊緣位置。

### 查詢轉換技術

- **多重查詢**：從不同角度生成問題變體
- **退步提示（Step-back）**：抽象化查詢取廣泛背景知識
- **HyDE（假設性文件嵌入）**：先生成假設答案再嵌入檢索
- **分解（Decomposition）**：複雜問題拆成多個子問題

### 記憶體類型

| 類型 | 說明 |
|------|------|
| 語義記憶 | 事實與概念（使用者偏好） |
| 情節記憶 | 過去事件/經歷 |
| 程序記憶 | 如何執行任務 |

---

## 多代理架構（Orchestrator-Worker）

- **監督者/編排者**：分解高層任務、分配給專門工作者
- **工作者代理人**：接收明確目標 + 專屬工具 + 隔離 context，避免情境分心
- 案例：Anthropic 並行 subagent fan-out 研究標普 500 董事會成員

---

## 企業案例

| 企業 | 應用 |
|------|------|
| Intercom (Fin) | 轉交人類客服時自動生成結構化內部筆記 |
| Cursor AI | 索引整個 codebase + 歷史 PR，提供全域情境 |
| 摩根士丹利 | 存取專有研究報告，顧問會議即時洞察 |

---

## 戰略建議

- **RAG 優先**：對多數企業場景，強大情境工程管線比微調模型有更高 ROI
- **將情境視為產品**：知識庫需持續維護、版本控制、品質檢查
- **投資可觀測性**：LangSmith 等工具追蹤和調試代理人系統

---

## 評分摘要

| 維度 | 分數 | 理由 |
|------|------|------|
| A. Workspace 可行動性 | 5/10 | 概念地圖性質，無直接 workspace 改進動作；內容已被 context-management.md 涵蓋 |
| B. 創新性 | 4/10 | Karpathy Context Engineering 的二手整理，workspace 已有更完整的一手資料 |
| C. 證據品質 | 5/10 | 無實驗數據，純概念說明，來源層級 C（vendor blog）|
| D. 技術深度 | 5/10 | 廣度夠但深度不足，Lost in the Middle / HyDE 僅概述 |
| E. 泛化性 | 7/10 | 框架通用，跨任務適用 |
| **加權總分** | **5.1/10** | 5×0.3+4×0.2+5×0.2+5×0.15+7×0.15 = 1.50+0.80+1.00+0.75+1.05 |

**整合決策**：不整合（< 6 分）  
**原因**：主題已被 context-management.md + Karpathy 原文完整涵蓋；iKala 版本為二手整理，無新增洞見  
**整合狀態**：→ low-score 存檔

---
url: "https://arxiv.org/abs/2604.20801"
title: "AgentFlow: Synthesizing Multi-Agent Harnesses for Vulnerability Discovery"
date: 2026-04-22
type: article
---

# AgentFlow: Synthesizing Multi-Agent Harnesses for Vulnerability Discovery

**原始來源**：https://arxiv.org/abs/2604.20801  
**作者**：Hanzhi Liu 等 7 位  
**發表日期**：2026-04-22  
**評分日期**：2026-05-05

---

## 繁體中文全文摘要

### 核心命題

AgentFlow 自動設計多 Agent 配置，用於安全漏洞發現。不需手動建構 Agent harness，而是使用「**型別化圖形 DSL**」來自動合成和迭代改進 harness 架構。

### 統一的 Harness 形式化表示

論文將 harness 形式化為五個互聯組件的型別化圖形：

| 符號 | 組件 | 說明 |
|------|------|------|
| 𝒜 | Agent 角色 | 每個 Agent 的職責和能力 |
| 𝒢 | 通訊拓撲 | Agent 間的連接和資訊流 |
| Σ | 訊息 schema | Agent 間傳遞的資料格式 |
| Φ | 工具分配 | 哪個 Agent 有存取哪些工具的權限 |
| Ψ | 協調協議 | Agent 協調和決策的規則 |

**型別系統優勢**：在昂貴的 LLM 執行之前，先拒絕結構上無效的候選方案，過濾掉約 **20%** 的提案。

### 執行時驅動的診斷（Runtime-Driven Diagnostics）

不使用二元 pass/fail 訊號，而是：

> 「讀取來自目標程式本身的結構化執行環境反饋（測試判決、行級覆蓋率地圖、sanitizer 報告）」

這種精細反饋讓提案者能：
- 辨識哪個組件失敗以及原因
- 針對性地修復（而非盲目嘗試）

**案例研究**：HEIF 解析器漏洞利用的三次迭代改進：
1. 格式驗證失敗 → 增加分析器 Agent
2. 覆蓋率顯示未觸及脆弱分支 → 增加驗證者 Agent
3. 啟用 AddressSanitizer 反饋的重試機制

### 優化循環

```
Propose（LLM 生成候選 harness 修改）
  ↓
Execute & Observe（在任務上執行，收集執行環境反饋）
  ↓
Score（領域特定函式評估效能）
  ↓
Diagnose（LLM 分析失敗，建議架構修改）
  ↓（迭代）
```

### 實證結果

#### TerminalBench-2 Benchmark
- **AgentFlow**：84.3%（使用 Claude Opus 4.6）
- **公開排行榜第一名**

#### Google Chrome 漏洞發現
使用 Kimi K2.5 模型對 Google Chrome 進行測試：
- 發現 **10 個** 前所未知的零日漏洞
- 包含 **2 個 Critical 等級**的沙箱逃逸漏洞：
  - CVE-2026-5280
  - CVE-2026-6297

### 消融研究

| 組件 | 禁用後效能下降 |
|------|-------------|
| **Prompt 編輯** | **-32.5 個百分點**（最大影響）|
| 結構編輯 | 中等影響 |
| 工具編輯 | 補充改善 |

### 關鍵發現：Harness 設計 > 模型能力

同樣的 Claude Opus 4.6 模型，在公開 benchmark 上的效能差異達 **4×**，取決於 harness 設計。

> 「精良設計的 harness 用更少的推理呼叫解決更多任務。」

### 對 Workspace 的啟示

1. **型別化圖形 DSL**：cc-workspace 的 sub-agent 協調目前是非正式的；可借鑒 AgentFlow 的角色、拓撲、協議的明確定義來改善 `AGENTS.md` 或 `subagent-strategy.md` 的設計
2. **Runtime-driven diagnostics**：Agent 失敗時，不只看 pass/fail，要看行級覆蓋率等精細信號
3. **Prompt 編輯是最大槓桿**（-32.5pp 消融效果）：提示詞品質比架構結構更重要
4. **4× 效能差異**：同一強模型在不同 harness 下差 4 倍，支持投資 harness 工程
5. **多 Agent 協調的安全含義**：漏洞發現能力提醒我們，同樣的能力也可用於防禦（red team 測試自己的系統）

---

## 評分摘要

| 維度 | 分數 | 理由 |
|------|------|------|
| A. Workspace 可行動性 | 7/10 | 型別化 harness DSL 和 runtime diagnostics 概念可改善 sub-agent 協調設計；但目前主要應用在安全領域 |
| B. 創新性 | 9/10 | 自動合成多 Agent harness、型別系統過濾、runtime 驅動診斷是重要技術突破 |
| C. 證據品質 | 9/10 | TerminalBench-2 第一名（84.3%），10 個真實 CVE（含 2 個 Critical），消融研究量化各組件貢獻 |
| D. 技術深度 | 8/10 | 五組件形式化、型別系統設計、優化循環架構均有具體說明 |
| E. 泛化性 | 7/10 | 主要在安全領域驗證；TerminalBench-2 表明可泛化，但跨域遷移未完全驗證 |
| **加權總分** | **7.95/10** | 7×0.3 + 9×0.2 + 9×0.2 + 8×0.15 + 7×0.15 = 2.1+1.8+1.8+1.2+1.05 |

**整合決策**：Rule  
**整合位置**：`.claude/refs/harness-design.md`（五組件 harness 形式化 + runtime diagnostics 原則）  
**整合狀態**：待實作

**TODO**：
- 在 harness-design.md 加入 AgentFlow 的五組件（𝒜𝒢ΣΦΨ）作為多 Agent 設計的結構性思考框架
- 在 security-review skill 中加入「用精細 runtime 信號（覆蓋率、sanitizer 報告）診斷 Agent 安全邊界」的概念

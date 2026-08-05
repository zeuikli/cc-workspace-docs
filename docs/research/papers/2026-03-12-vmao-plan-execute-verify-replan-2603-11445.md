---
url: "https://arxiv.org/abs/2603.11445"
title: "Verified Multi-Agent Orchestration: A Plan-Execute-Verify-Replan Framework for Complex Query Resolution"
archived_date: 2026-07-26
arxiv_id: 2603.11445
authors: ["Xing Zhang", "Yanwei Cui", "Guanghui Wang", "Wei Qiu", "Ziyuan Li", "Fangwei Han", "Yajing Huang", "Hengzhi Qiu", "Bing Zhu", "Peiyang He"]
domains: [cs.AI, cs.MA]
html: "https://arxiv.org/html/2603.11445v1"
pdf_path: pdfs/2603.11445.pdf
published_date: 2026-03-12
---

# Verified Multi-Agent Orchestration: A Plan-Execute-Verify-Replan Framework for Complex Query Resolution

**Authors**: Xing Zhang, Yanwei Cui, Guanghui Wang, Wei Qiu, Ziyuan Li, Fangwei Han, Yajing Huang, Hengzhi Qiu, Bing Zhu, Peiyang He
**Published**: March 12, 2026
**Source**: https://arxiv.org/abs/2603.11445 · [HTML](https://arxiv.org/html/2603.11445v1)
**arXiv ID**: 2603.11445
**Categories**: cs.AI; cs.MA
**PDF**: [research/papers/pdfs/2603.11445.pdf](https://arxiv.org/abs/2603.11445)

---

## Abstract (quoted)

> We present Verified Multi-Agent Orchestration (VMAO), a framework that coordinates specialized LLM-based agents through a verification-driven iterative loop. Given a complex query, our system decomposes it into a directed acyclic graph (DAG) of sub-questions, executes them through domain-specific agents in parallel, verifies result completeness via LLM-based evaluation, and adaptively replans to address gaps. The key contributions are: (1) dependency-aware parallel execution over a DAG of sub-questions with automatic context propagation, (2) verification-driven adaptive replanning that uses an LLM-based verifier as an orchestration-level coordination signal, and (3) configurable stop conditions that balance answer quality against resource usage.

---

## 結構化摘要

### 核心貢獻

- 五階段迭代框架 **Plan → Execute → Verify → Replan → Synthesize**，把複雜查詢分解為 DAG 子問題並跑到收斂
- **DAGExecutor**：依賴感知的批次平行執行（預設 batch k=3），自動把上游結果傳播到下游子問題
- **三層 8-agent 架構**（Tier 1 資料蒐集：RAG/Web Search/Financial/Competitor；Tier 2 分析：Analysis/Reasoning/Raw Data；Tier 3 輸出：Document/Visualization），共配置 8 個 MCP server、42 個工具
- **ResultVerifier**：LLM 對每個結果評分，輸出 complete/partial/incomplete 狀態與 0–1 completeness 分數，驅動 **AdaptiveReplanner** 決定重試或引入新子問題
- 5 種可配置停止條件：完整度閾值（80%）、高信心度（75% 信心＋50% 覆蓋）、邊際收益遞減（<5% 改進）、token 預算（1M）、最大迭代次數（3）

### 關鍵結果

- 25 個專家策劃的市場研究查詢（4 類別：Performance Analysis / Competitive Intelligence / Financial Investigation / Strategic Assessment）
- 完整度分數：VMAO 4.2 vs Static Pipeline 3.5 vs Single-Agent 3.1（**+35%** vs 單 agent）
- 來源品質分數：VMAO 4.1 vs 3.2 vs 2.6（**+58%** vs 單 agent）
- 資源代價：VMAO 平均 **850K tokens**（單 agent 僅 100K，**8.5 倍**），執行時間約 900 秒
- Strategic Assessment 類別改進最大（+53% 完整度）；執行階段佔 token 用量 61%

### 限制

- 25 題規模小、未報信心區間；LLM judge（Opus 4.5）與執行模型（Sonnet 4.5）同屬 Claude 家族，儘管有人工審查仍可能有共同偏差
- Static Pipeline baseline 未做元件級消融
- LLM 驗證只評「完整度」不評「準確度」，難以偵測細微事實錯誤或幻覺；不當的查詢分解會把錯誤傳播到下游
- 全部實驗限單一模型家族（Claude），跨模型家族效果未測試；8.5 倍 token 成本對延遲敏感場景可能不可接受

---

## Workspace 關聯（評估，非既成結論）

- VMAO「LLM-based verifier 作為 orchestration-level coordination signal」直接對照 `core.md`「判斷 vs 決定」公理：本論文把 verify 的判斷結果餵回 replanner 做路由決定，是判斷/決定分離的具體實作範例。⚠️ verifier 與執行者同模型家族的共同偏差風險，恰是 `core.md §PROPOSE 委派`（原 `graph.md §G2`）「產出者不驗收自己產出、可行時優先異模型」規則的實證佐證。
- 5 種顯式停止條件（含 token 預算與邊際收益遞減 <5%）與 `core.md §APPLY 自主迴圈`（原 `loop.md §L2`） 四重終止並存宣告高度同構，可作為「no-progress 判準」的量化參考點。⚠️ 論文未報告 verifier 本身的可信度校準（同一 state 連跑是否一致），對照 `core.md §APPLY 自主迴圈` oracle 資格排查仍缺一角。

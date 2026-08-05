---
url: "https://arxiv.org/abs/2601.22025"
title: "When \\\\\\\"Better\\\\\\\" Prompts Hurt: Evaluation-Driven Iteration for LLM Applications"
archived_date: 2026-06-09
arxiv_id: 2601.22025
authors: ["Daniel Commey"]
pdf_path: pdfs/2601.22025.pdf
published_date: 2026-01-29
---

# When "Better" Prompts Hurt: Evaluation-Driven Iteration for LLM Applications

**Authors**: Daniel Commey
**Published**: January 29, 2026
**Source**: https://arxiv.org/abs/2601.22025
**arXiv ID**: 2601.22025
**Categories**: cs.CL

---

## Abstract

Evaluating Large Language Model (LLM) applications differs from traditional software testing because outputs are stochastic, high-dimensional, and sensitive to prompt and model changes. We present an evaluation-driven workflow—Define, Test, Diagnose, Fix—that turns these challenges into a repeatable engineering loop.

We introduce the Minimum Viable Evaluation Suite (MVES), a tiered set of recommended evaluation components for (i) general LLM applications, (ii) retrieval-augmented generation (RAG), and (iii) agentic tool-use workflows. We also synthesize common evaluation methods (automated checks, human rubrics, and LLM-as-judge) and discuss known judge failure modes.

In reproducible local experiments (Ollama; Llama 3 8B Instruct and Qwen 2.5 7B Instruct), we observe that a generic "improved" prompt template can trade off behaviors: on our small structured suites, extraction pass rate decreased from 100% to 90% and RAG compliance from 93.3% to 80% for Llama 3 when replacing task-specific prompts with generic rules, while instruction-following improved. These findings motivate evaluation-driven prompt iteration and careful claim calibration rather than universal prompt recipes.

All test suites, harnesses, and results are included for reproducibility.

---

## 核心方法

### Define-Test-Diagnose-Fix 工作流程
評估驅動的四階段迭代循環，取代傳統的「prompt 試錯」模式：
1. **Define**：將需求轉換為具體可測試的成功條件
2. **Test**：對 prompt 版本跑評估套件（自動化 + 人工 + LLM-as-judge）
3. **Diagnose**：分析失敗模式（prompt drift、format brittleness、silent regression）
4. **Fix**：針對診斷結果做外科刀式修改，而非替換整個 prompt

### MVES（Minimum Viable Evaluation Suite）三層架構
| 層級 | 應用類型 | 核心評估組件 |
|------|---------|------------|
| MVES-Core | 一般 LLM 應用 | 自動化 checks + 人工 rubrics |
| MVES-RAG | RAG 系統 | RAGAS 指標 + 引用覆蓋率 |
| MVES-Agentic | Agent 工具使用 | 任務完成率 + 工具呼叫正確性 |

### 品質維度分類（Quality Taxonomy）
七個維度：Correctness、Helpfulness、Harmlessness、Groundedness & Attribution、Refusal Correctness、Format & Style Adherence、Consistency。

### LLM-as-Judge 已知失敗模式
- **Position bias**：傾向評分排在前面的答案
- **Verbosity bias**：偏好較長回應，即使內容較差
- **Self-preference**：同家族模型互相偏好
- **Style bias**：偏好特定格式（如 markdown）
- **Instruction leakage**：judge prompt 中的評分標準滲漏影響判斷

---

## 關鍵數字

| 實驗對比 | Task-specific prompt | Generic "improved" prompt | 變化 |
|---------|---------------------|--------------------------|------|
| 抽取 pass rate | 100% | 90% | **-10pp** |
| RAG compliance (Llama 3) | 93.3% | 80% | **-13.3pp** |
| Instruction-following | — | — | 改善（唯一正向） |

**模型**：Ollama + Llama 3 8B Instruct + Qwen 2.5 7B Instruct（本地推論，完全可重現）

---

## 對 Prompt Caching / Management / Engineering 的關聯

### Prompt Caching
- **Prompt Drift 偵測**：本文的 MVES 可作為 caching 策略的回歸測試套件——若快取的 system prompt 被更動，必須跑 MVES 確認無 silent regression
- **Silent Regression 風險**：LLM provider 靜默更新模型時（model churn），快取的 KV 狀態對應的 prompt 行為可能改變；MVES 提供偵測這種漂移的機械性驗證方法

### Prompt Management
- **Prompt 版本控管**：Define-Test-Diagnose-Fix 循環直接對應 prompt 版本管理的工程紀律——每次修改都需要可測量的成功條件（R4 Goal-Driven）
- **LLM-as-judge 評估成本**：論文量化了不同評估方法的 cost per 1,000 examples，幫助決定 prompt 迭代的評估預算分配
- **Overfitting to Test Set**（§10.2）：對評估集過度優化的 prompt 在生產環境退化，與 prompt caching 情境中「對特定 case 最佳化的快取 prefix」面臨相同風險

### Prompt Engineering
- **核心論點**：反直覺發現——「更好」的通用 prompt 模板在特定任務上反而退步，支持任務特定評估優先於通用 prompt 秘訣
- **MVES 框架**：提供 prompt engineer 實際可執行的評估標準（非口頭「看起來正確」），直接對應 §R4 的「成功條件必須可機械性驗證」
- **六大 Contribution**：MVES 框架 + 評估方法綜述 + 品質維度分類 + LLM-as-judge 失敗模式分析 + actionable checklist + 原始實驗（全部開源可重現）

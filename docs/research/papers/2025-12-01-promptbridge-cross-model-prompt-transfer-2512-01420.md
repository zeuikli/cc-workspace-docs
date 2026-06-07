---
title: "PromptBridge: Cross-Model Prompt Transfer for Large Language Models"
authors: "Yaxuan Wang, Quan Liu, Zhenting Wang, Zichao Li, Wei Wei, Yang Liu, Yujia Bao"
published: "2025-12-01"
source: "https://arxiv.org/abs/2512.01420"
---

# PromptBridge: Cross-Model Prompt Transfer for Large Language Models

**Authors**: Yaxuan Wang, Quan Liu, Zhenting Wang, Zichao Li, Wei Wei, Yang Liu, Yujia Bao
**Affiliations**: University of California Santa Cruz, Center for Advanced AI at Accenture
**Published**: December 1, 2025
**Source**: https://arxiv.org/abs/2512.01420
**arXiv ID**: 2512.01420
**Categories**: cs.CL
**Corresponding Author**: Yujia Bao (yujia.bao@accenture.com)

---

## Abstract

Large language models (LLMs) underpin applications in code generation, mathematical reasoning, and agent-based workflows. In practice, systems access LLMs via commercial APIs or open-source deployments, and the model landscape (e.g., GPT, Claude, Llama) evolves rapidly. This rapid evolution forces frequent model switches driven by capability, cost, deployment constraints, and privacy. Yet prompts are highly model-sensitive: reusing a prompt engineered for one model on another often yields substantially worse performance than a prompt optimized for the target model. We term this phenomenon *Model Drifting*. Through extensive empirical analysis across diverse LLM configurations, we show that model drifting is both common and severe. To address this challenge, we introduce PromptBridge, a training-free framework that preserves prompt effectiveness under model switches, enabling cross-model prompt transfer without costly per-task or per-model re-optimization. PromptBridge requires only a small set of alignment tasks for calibration. It first applies Model-Adaptive Reflective Prompt Evolution (MAP-RPE) to obtain task- and model-specific optimal prompts via iterative reflective refinement and quantitative evaluation. Using the resulting calibrated prompt pairs for the source and target models, PromptBridge learns a cross-model prompt mapping. At test time, i.e., for an unseen task, given a source-model prompt, this mapping directly produces an optimized prompt for the target model. Experiments in single-agent and multi-agent settings show that PromptBridge consistently improves downstream accuracy while reducing migration effort. For example, when transferring from the source model to the target model, such as o3, PromptBridge yields a 27.39% improvement on SWE-Bench and a 39.44% improvement on Terminal-Bench relative to direct transfer. The code will be available soon.

---

## 核心方法

### Model Drifting 問題定式化
**形式定義**：給定 LLM 系統 Φ_{M,p}，當底層模型從 M_s 換為 M_t，源模型最佳 prompt p*_{M_s,T} 在目標模型上的表現：

```
A(M_t, T, p*_{M_s,T}) < max_{p_{M_t,T}} A(M_t, T, p_{M_t,T})
```

轉移缺口 Δ(M_s → M_t, T) = 目標模型自身最優 − 轉移後的表現差距。

### PromptBridge 兩階段框架

**Phase 1：MAP-RPE（Model-Adaptive Reflective Prompt Evolution）**
- 對每個 alignment task，迭代搜索：反思式精鍊（reflective refinement）+ 量化評估（island-based search）
- 輸出：一組 (p*_{M_s,S_i}, p*_{M_t,S_i}) calibrated prompt pairs

**Phase 2：Cross-Model Prompt Mapping 學習**
- 從 calibration pairs 學習映射函數 T_`{M_s→M_t}`
- 測試時：給定 unseen task 的 source prompt → 直接產出 target model 最佳 prompt
- **Zero-shot 適應**：不需要 unseen task 的評估資料

### 評估範圍
- 7 個 LLMs、8 個 benchmarks
- Single-agent + multi-agent 兩種設定
- Local model drifting（單一 agent 換模型）+ Global model drifting（全部 agents 同換）

---

## 關鍵數字

| 場景 | Benchmark | PromptBridge 提升（vs. 直接轉移）|
|------|-----------|--------------------------------|
| 轉移到 o3 | SWE-Bench | **+27.39%** |
| 轉移到 o3 | Terminal-Bench | **+39.44%** |

**Model Drifting 嚴重性例證**（HumanEval）：
| Source → Target | Source 最佳 prompt 在 target | Target 自身最優 | Drift |
|----------------|----------------------------|----------------|-------|
| GPT-5 → Llama-3.1-70B-Instruct | 68.70% | 79.47% | **-10.77pp** |
| Llama-3.1-70B → GPT-5 | 96.95% | 99.39% | **-2.44pp** |
| GPT-4o → o3（direct） | 92.27% | 98.37% | **-6.10pp** |

**校準成本**：只需少量 alignment tasks，無需重新訓練模型（training-free）。

---

## 對 Prompt Caching / Management / Engineering 的關聯

### Prompt Caching
- **模型切換使快取失效**：Model Drifting 的核心場景（GPT-4o → o3）等同於「快取的 prompt 在新模型上失效」——快取策略若依賴特定模型的 KV 結構，模型升級時快取全部作廢且 prompt 表現退化
- **PromptBridge 延伸**：可考慮在模型升級前預先用 MAP-RPE 校準新的 system prompt，降低 cache warm-up 期間的退化損耗

### Prompt Management
- **Prompt Library 跨模型維護問題**：企業若維護大量 task-specific prompts，模型切換時需全部重新優化——PromptBridge 提供一次性校準後批量轉移的解法
- **版本控管維度**：Prompt 版本應同時記錄「針對哪個模型優化」，否則版本切換時 drift 不可預測；這呼應 §R7 Surface Conflicts（不同模型的 prompt 偏好為矛盾模式）
- **Migration Effort 量化**：PromptBridge 的貢獻之一是「reducing migration effort」——提供可計算的 drift gap 指標（Δ），讓 PM 決定是否值得投入重新優化

### Prompt Engineering
- **Model-Sensitivity 的系統性認知**：不同模型因 tokenization、role tag、alignment 訓練差異（如 Llama 3 引入 `ipython` role）導致 prompt 偏好根本性不同；prompt engineer 應將「目標模型」視為 prompt 的必要 metadata
- **MAP-RPE 作為自動化 prompt 優化器**：evaluation-guided + reflection-driven + island-based 搜索，可作為 MVES（2601.22025）框架下的自動化 Fix 步驟
- **Multi-agent 維度**：全局 model drifting 在 multi-agent 系統中影響更複雜（每個 agent 的 prompt 互相依賴），需整體協調而非逐一優化

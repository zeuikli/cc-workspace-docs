---
url: "https://arxiv.org/abs/2605.07686"
title: "The Coupling Tax: How Shared Token Budgets Undermine Visible Chain-of-Thought Under Fixed Output Limits"
archived_date: 2026-06-24
arxiv_id: 2605.07686
authors: ["Wenhua Nie", "Junlin Liu", "Jianan Wu", "Zijie Meng", "Yilong Fan", "Zhang Zijian", "Haoran Zheng", "Jyh-Shing Roger Jang"]
domains: [cs.LG]
html: "https://arxiv.org/html/2605.07686v1"
pdf_path: pdfs/2605.07686.pdf
published_date: 2026-05-08
---

# The Coupling Tax: How Shared Token Budgets Undermine Visible Chain-of-Thought Under Fixed Output Limits

**Authors**: Wenhua Nie, Junlin Liu, Jianan Wu, Zijie Meng, Yilong Fan, Zhang Zijian, Haoran Zheng, Jyh-Shing Roger Jang
**Published**: May 08, 2026
**Source**: https://arxiv.org/abs/2605.07686 · [HTML](https://arxiv.org/html/2605.07686v1)
**arXiv ID**: 2605.07686
**Categories**: cs.LG
**PDF**: [research/papers/pdfs/2605.07686.pdf](https://arxiv.org/abs/2605.07686) (39 pp, full text archived)

---

## Abstract (quoted)

> Chain-of-thought reasoning is often treated as a monotone way to improve language-model accuracy by letting a model think longer. We identify a countervailing effect, the coupling tax: when reasoning traces and final answers share one output-token budget, long traces can crowd out the answer they are meant to support. Across GSM8K, MATH-500, and five BIG-Bench Hard tasks with Qwen3 models at three scales, non-thinking mode matches or outperforms thinking mode on GSM8K and MATH-500 at every budget up to 2048 tokens, while harder tasks shift the crossover to larger budgets. We derive a truncation-waste decomposition, $\mathrm{Acc}_{\mathrm{think}}(b)=\alpha_c F_L(b)+\alpha_t(1-F_L(b))$, that predicts this crossover from chain-length and accuracy statistics and explains inverse scaling within the Qwen family. A DeepSeek-R1-Distill-Llama-8B replication shows the same pattern under a different thinking interface. As a mitigation, split-budget generation decouples reasoning and answer budgets; on full MATH-500, IRIS reaches 74.0% accuracy, a strengthened extraction variant reaches 78.8%, and a fixed non-oracle SC+IRIS gate reaches 83.6%. The results show that test-time reasoning should be evaluated as a budget-allocation problem, not only as a question of whether longer traces are available.

---

## 結構化摘要

### 核心貢獻

- 定義 **coupling tax**：reasoning trace 與 final answer 共用同一 output-token budget，導致長推理鏈反而擠壓 answer token，形成 accuracy 衰減。
- 提出 **truncation-waste decomposition**：形式化公式 $\mathrm{Acc}_{\mathrm{think}}(b)=\alpha_c F_L(b)+\alpha_t(1-F_L(b))$，可從 chain-length 分布與精度統計預測 thinking/non-thinking 交叉點。
- 揭示 **inverse scaling** 現象：Qwen3 家族中較大模型的 CoT trace 更長，在低 budget 下反而表現更差。
- 提出 **split-budget generation（IRIS）** 緩解方案：將 reasoning budget 與 answer budget 解耦，避免 crowding-out。

### 關鍵結果

- GSM8K & MATH-500：在 budget ≤ 2048 tokens 範圍內，non-thinking mode 全面匹敵或超越 thinking mode（Qwen3 三種規模均成立）。
- 難題（BIG-Bench Hard 五項）：crossover 點移至更大 budget，但 coupling tax 現象依然存在。
- IRIS 在 MATH-500 full set：74.0% accuracy；強化版 extraction variant 78.8%；non-oracle SC+IRIS gate 83.6%。
- DeepSeek-R1-Distill-Llama-8B 複現：相同 coupling tax pattern，跨模型家族泛化。

### 限制

- 實驗集中於數學/推理基準（GSM8K、MATH-500、BIG-Bench Hard），對開放域生成任務的適用性未充分驗證。
- IRIS 的 split-budget 方案需要額外工程（兩段生成），對 streaming inference 架構的相容性未討論。
- 論文未針對更長 budget（>8192 tokens）系統性驗證；極長推理鏈下的 crossover 動態仍屬 open question。

---

## Workspace 關聯（評估，非既成結論）

- **直接對應 context-management 的 token budget 紀律**：本論文量化了 shared token budget 下 CoT 與 answer 的零和競爭，與 workspace 中 `context-management.md` 所強調的 token budget 軟性上限（per-task ~4,000 tokens）在設計哲學上高度呼應——budget 是分配問題，不是「越多越好」。
- **對 effort-first 原則的反例警示**：workspace 的 Effort 先於 model 策略暗示「多思考 = 更好結果」，但本論文指出在固定 output budget 下，強制開啟 thinking mode（高 effort）可能因 coupling tax 反而降低準確率；⚠️ 此洞察值得在 effort/mode 選擇時納入 budget 感知判斷，但 workspace 目前的 pilot 模式紀律未明列此 tradeoff。
- **呼應 `core.md §PROPOSE 委派`（原 subagent-strategy.md）的判斷 vs 決定分工**：論文的 split-budget（IRIS）方案將推理與輸出解耦，類似 workspace 中「LLM 做判斷、確定性代碼做決定」的架構原則——兩者都主張避免將不同性質的輸出混用同一資源池。
- **對 CoT chain length 的實證基礎**：⚠️ workspace 中 `core.md` 並未明列 CoT trace 長度管控規則，本論文的 truncation-waste decomposition 可作為未來在 subagent 設計中加入「reasoning budget gate」的理論依據，但落地需額外 harness 層支撐，目前屬研究探索而非直接可套用的規則。

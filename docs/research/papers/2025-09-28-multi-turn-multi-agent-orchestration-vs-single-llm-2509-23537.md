---
url: "https://arxiv.org/abs/2509.23537"
title: "Beyond the Strongest LLM: Multi-Turn Multi-Agent Orchestration vs. Single LLMs on Benchmarks"
archived_date: 2026-06-24
arxiv_id: 2509.23537
authors: ["Aaron Xuxiang Tian", "Ruofan Zhang", "Jiayao Tang", "Young Min Cho", "Xueqian Li", "Qiang Yi", "Ji Wang", "Zhunping Zhang", "Danrui Qi", "Zekun Li", "Xingyu Xiang", "Sharath Chandra Guntuku", "Lyle Ungar", "Tianyu Shi", "Chi Wang"]
domains: [cs.AI]
html: "https://arxiv.org/html/2509.23537v1"
pdf_path: pdfs/2509.23537.pdf
published_date: 2025-09-28
---

# Beyond the Strongest LLM: Multi-Turn Multi-Agent Orchestration vs. Single LLMs on Benchmarks

**Authors**: Aaron Xuxiang Tian, Ruofan Zhang, Jiayao Tang, Young Min Cho, Xueqian Li, Qiang Yi, Ji Wang, Zhunping Zhang, Danrui Qi, Zekun Li, Xingyu Xiang, Sharath Chandra Guntuku, Lyle Ungar, Tianyu Shi, Chi Wang
**Published**: September 28, 2025
**Source**: https://arxiv.org/abs/2509.23537 · [HTML](https://arxiv.org/html/2509.23537v1)
**arXiv ID**: 2509.23537
**Categories**: cs.AI
**PDF**: [research/papers/pdfs/2509.23537.pdf](https://arxiv.org/abs/2509.23537) (9 pp, full text archived)

---

## Abstract (quoted)

> We study multi-turn multi-agent orchestration, where multiple large language model (LLM) agents interact over multiple turns by iteratively proposing answers or casting votes until reaching consensus. Using four LLMs (Gemini 2.5 Pro, GPT-5, Grok 4, and Claude Sonnet 4) on GPQA-Diamond, IFEval, and MuSR, we conduct two experiments: (i) benchmarking orchestration against single-LLM baselines; and (ii) ablations on GPQA-Diamond that vary whether agents see who authored answers and whether they can observe ongoing votes. Orchestration matches or exceeds the strongest single model and consistently outperforms the others. Analysis of best-achievable orchestration performance shows potential for further gains. The ablations show that revealing authorship increases self-voting and ties, and that showing ongoing votes amplifies herding, which speeds convergence but can sometimes yield premature consensus.

---

## 結構化摘要

### 核心貢獻
- 提出 **multi-turn multi-agent orchestration** 框架：多個異質 LLM agent 跨多輪反覆「提案答案」或「投票」，直到達成 consensus。
- 以四個前沿 LLM（Gemini 2.5 Pro、GPT-5、Grok 4、Claude Sonnet 4）在三個 benchmark（GPQA-Diamond、IFEval、MuSR）上系統性對照 orchestration vs. single-LLM baseline。
- 在 GPQA-Diamond 上做兩組 ablation：(1) 是否揭露答案的 **authorship**（誰寫的）；(2) agent 是否能 **觀察進行中的投票**（ongoing votes）。
- 量化分析 best-achievable orchestration（上界）性能，揭示 orchestration 仍有未榨乾的提升空間。

### 關鍵結果
- Orchestration **匹配或超越最強單一模型**，並穩定優於其餘三個模型 —— 即「群體編排 > 個別最強」。
- Best-achievable 分析顯示：實際 orchestration 尚未觸頂，存在進一步增益潛力（方法層發現，原文未在 abstract 給單一數字）。
- Ablation 發現的社會動力學偏差：
  - 揭露 **authorship** → 增加 **self-voting**（投自己）與 **平票（ties）**。
  - 顯示 **ongoing votes** → 放大 **herding（從眾）**；加速收斂，但有時導致 **premature consensus（過早定案）**。

### 限制
文件未列明確 limitation 章節（依 abstract 判斷）。可能弱點：
- 僅三個 benchmark（GPQA-Diamond / IFEval / MuSR）、四個模型，泛化性與成本（多輪多模型 API 呼叫）未在 abstract 量化。
- Premature consensus 與 herding 屬已觀察到的失敗模式，但 abstract 未提出穩健的緩解機制。
- 「best-achievable」為 oracle 式上界，與可實際落地的選票/收斂策略之間的差距未說明。

---

## Workspace 關聯（評估，非既成結論）

- **直接對應 `core.md §PROPOSE 委派`（原 subagent-strategy.md）的 Fan-out 假設**：本文實證「多 agent 編排 ≥ 最強單模型」，為 `core.md §PROPOSE 委派` 的 fan-out 委派提供外部佐證。⚠️ 落地門檻：本文用四個**異質前沿模型**投票；workspace 多為**同模型分工**（Sonnet/Opus），群體多樣性增益未必等價。
- **herding / premature consensus = multi-agent verdict 不可盡信**：呼應 core.md TEST 的 `unverified_success` 閘門與 `core.md §PROPOSE 委派`（原 subagent-strategy.md）的「subagent/workflow verdict 非證據，須機械重驗」。本文以實驗證明「觀察他人投票放大從眾」，正是該紀律要防的失敗模式。
- **authorship 揭露 → self-voting/ties**：對照 The Loop「child 不 self-resolve、矛盾交 parent」設計——隱藏作者身份可降低 self-preferential bias，與 dynamic-workflow 三失敗模式之一（self-preferential bias）吻合。⚠️ 本文情境為對等投票，與 workspace 的 parent↔child 階層拓撲不同，需審慎類比。 〔v5.1：所引 workspace 細則已退役 → 見 `INDEX.md` §v5.1 規則退役對照〕
- **可作為 advisor / `/pilot frontier` 稽核（原 quality-pipeline，v5.1 刪除） 多模型互審的理論背書**：`/pilot frontier` 稽核 / `/pilot frontier` 稽核 的多模型 gate 設計與本文「orchestration 優於個別最強」一致；但須以本文的 premature-consensus 警告校準收斂條件，避免過早 gate-pass。

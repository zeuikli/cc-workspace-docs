---
url: "https://arxiv.org/abs/2505.13516"
title: "HALO: Hierarchical Autonomous Logic-Oriented Orchestration for Multi-Agent LLM Systems"
archived_date: 2026-06-24
arxiv_id: 2505.13516
authors: ["Zhipeng Hou", "Junyi Tang", "Yipeng Wang"]
domains: [cs.MA]
html: "https://arxiv.org/html/2505.13516v1"
pdf_path: pdfs/2505.13516.pdf
published_date: 2025-05-17
---

# HALO: Hierarchical Autonomous Logic-Oriented Orchestration for Multi-Agent LLM Systems

**Authors**: Zhipeng Hou, Junyi Tang, Yipeng Wang
**Published**: May 17, 2025
**Source**: https://arxiv.org/abs/2505.13516 · [HTML](https://arxiv.org/html/2505.13516v1)
**arXiv ID**: 2505.13516
**Categories**: cs.MA
**PDF**: [research/papers/pdfs/2505.13516.pdf](https://arxiv.org/abs/2505.13516) (10 pp, full text archived)

---

## Abstract (quoted)

> Recent advancements in Multi-Agent Systems (MAS) powered by Large Language Models (LLMs) have demonstrated tremendous potential in diverse task scenarios. Nonetheless, existing agentic systems typically rely on predefined agent-role design spaces and static communication structures, limiting their adaptability as well as flexibility in complex interaction environments and leading to subpar performance on highly specialized and expert-level tasks. To address these issues, we introduce HALO, a multi-agent collaboration framework based on a hierarchical reasoning architecture. Specifically, we incorporate a high-level planning agent for task decomposition, mid-level role-design agents for subtask-specific agent instantiation, and low-level inference agents for subtask execution. Particularly, subtask execution is reformulated as a structured workflow search problem, where Monte Carlo Tree Search (MCTS) systematically explores the agentic action space to construct optimal reasoning trajectories. Additionally, as the majority of users lack expertise in prompt engineering, we leverage an Adaptive Prompt Refinement module to transform raw queries into task-specific prompts. Empirical evaluations on Code Generation (HumanEval), General Reasoning (MMLU), and Arithmetic Reasoning (MATH) benchmark datasets highlight the effectiveness of HALO, yielding a 14.4% average improvement over state-of-the-art baselines. Notably, HALO achieves up to 13.3% performance gain on the Moral Scenarios subject in the MMLU benchmark and up to 19.6% performance gain on the Algebra subarea in the MATH benchmark, indicating its advanced proficiency in tackling highly specialized and expert-level tasks.

---

## 結構化摘要

### 核心貢獻
- 提出 **HALO**：基於 hierarchical reasoning 架構的 multi-agent 協作框架，針對既有 MAS 依賴「預定義 agent-role 設計空間 + static communication structure」造成的低適應性問題。
- 三層 agent 架構：**high-level planning agent**（task decomposition）→ **mid-level role-design agents**（針對 subtask 動態 instantiate agent）→ **low-level inference agents**（subtask execution）。
- 將 subtask execution 重構為 **structured workflow search problem**，以 **Monte Carlo Tree Search (MCTS)** 系統性探索 agentic action space，建構最優 reasoning trajectory。
- **Adaptive Prompt Refinement** 模組：將使用者原始 query 自動轉成 task-specific prompt，降低對 prompt engineering 專業的依賴。

### 關鍵結果
- 對 SOTA baselines 平均提升 **14.4%**（跨 HumanEval / MMLU / MATH 三 benchmark）。
- MMLU 的 **Moral Scenarios** 子科目最高提升 **13.3%**。
- MATH 的 **Algebra** 子領域最高提升 **19.6%**。
- 結論訴求：在高度專業化、expert-level 任務上展現優勢。

### 限制
文件未列明確 limitation 章節（依 abstract 判讀）。推測弱點：
- MCTS workflow search 的計算成本 / token 開銷未在 abstract 量化，動態三層 + 樹搜索可能 inference cost 偏高。
- 評測僅限 HumanEval / MMLU / MATH 三個 well-defined benchmark，缺 open-ended 或長程 agentic 任務驗證泛化性。
- 「動態 role instantiation」的穩定性與失敗模式（如 role 設計偏移）未在摘要層交代。

---

## Workspace 關聯（評估，非既成結論）

- **直接對映 subagent fan-out**：HALO 的 planning → role-design → inference 三層，對應本 workspace「主對話規劃分工 → spawn 專責 sub-agent → child 執行」拓撲（見 `core.md §PROPOSE 委派`（原 `subagent-strategy.md`） Hierarchical Fan-out）。其「動態 role-design」比本 workspace 的固定 agent type 清單更激進。⚠️ 落地門檻：本 workspace fan-out 上限 4 且 child 不自溝通，HALO 的 MCTS workflow search 需更大樹寬度，直接套用會撞 fan-out 與 token budget 上限。 〔v5.1：所引 workspace 細則已退役 → 見 `INDEX.md` §v5.1 規則退役對照〕
- **MCTS workflow search vs The Loop**：HALO 以 MCTS 探索 action space 找最優 trajectory，與 The Loop 的 PROPOSE→APPLY→TEST 迭代收斂屬不同範式（搜索 vs 機械驗證迭代）；可借鏡其「reformulate execution as search」但須保留 workspace 的 deterministic verification gate（搜索結果仍需 unverified_success 親驗）。
- **Adaptive Prompt Refinement** 概念上接近 workspace 的 IDENTIFY 階段（顯露假設、把模糊 query 結構化），但 HALO 自動化、workspace 偏人工 spec。⚠️ 自動 refine 與「off-rails 不靜默委派」紀律有張力，需人驗證閘。
- 評測 14.4% 平均增益為論文自報數字，採信前應對照 baseline 設定；屬 multi-agent orchestration 領域的可參考實證，非可直接移植的工程結論。

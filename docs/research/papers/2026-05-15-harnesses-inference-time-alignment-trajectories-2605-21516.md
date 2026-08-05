---
url: "https://arxiv.org/abs/2605.21516"
title: "Harnesses for Inference-Time Alignment over Execution Trajectories"
archived_date: 2026-07-18
arxiv_id: 2605.21516
authors: ["Boyuan Wang", "Bochao Li", "Minghan Wang", "Yuxin Tao", "Fang Kong"]
pdf_path: pdfs/2605.21516.pdf
published_date: 2026-05-15
---

# Harnesses for Inference-Time Alignment over Execution Trajectories

**Authors**: Boyuan Wang, Bochao Li, Minghan Wang, Yuxin Tao, Fang Kong
**Published**: May 2026
**Source**: https://arxiv.org/abs/2605.21516
**arXiv ID**: 2605.21516
**Categories**: Machine Learning (cs.LG); Artificial Intelligence (cs.AI)
**PDF**: [research/papers/pdfs/2605.21516.pdf](https://arxiv.org/abs/2605.21516)

---

## Abstract

The paper examines how workflow engineering enhances LLM agent performance through inference-time techniques. The researchers note that increasing decomposition or guidance can sometimes improve execution, but can also reduce final task success. They analyze harness design by studying trajectory alignment, distinguishing between task decomposition (structuring tasks into sub-goals) and guided execution (reshaping action distributions). Their framework identifies performance constraints linked to workflow granularity, retry budgets, and action reweighting, while revealing failure patterns including over-decomposition, over-pruning, and hallucinated execution. The work validates these insights through synthetic experiments and real agent benchmarks, ultimately demonstrating that effective harnesses can be partial: specifying only the initial steps and leaving the remaining execution to agent can achieve higher pass rate than fully structured workflows.

---

## Core Thesis

- 拆解 harness 對 execution trajectory 的兩種介入方式：task decomposition（拆解成子目標）與 guided execution（重塑動作分佈），並指出「越多分解／引導 = 越好」是假設而非事實——過度分解、過度剪枝反而降低任務成功率。
- 提出 workflow granularity、retry budget、action reweighting 三個效能制約維度，並整理三種失敗模式：over-decomposition、over-pruning、hallucinated execution。
- 關鍵發現：**partial harness**（只規範初始步驟，其餘交給 agent 自主執行）在合成實驗與真實 benchmark 上通過率優於全結構化 workflow——顯示「過度工程化」的 harness 反而有害。
- **Workspace 關聯**：直接挑戰「儀式構件越多越好」的直覺，與 core.md「儀式深度隨風險伸縮、不隨模型檔位」的立場互補——為高能力模型設計 harness 時應保留部分自主空間而非全鏈路硬編排，可作為 `/fusion` sidekick brief 顆粒度設計的參考證據。

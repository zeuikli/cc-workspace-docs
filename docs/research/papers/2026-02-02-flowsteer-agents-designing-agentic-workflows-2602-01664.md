---
url: "https://arxiv.org/abs/2602.01664"
title: "FlowSteer: Towards Agents Designing Agentic Workflows via Reinforced Progressive Canvas Editing"
archived_date: 2026-07-18
arxiv_id: 2602.01664
authors: ["Mingda Zhang", "Wenjin Liu", "Tiesunlong Shen", "Qika Lin", "Rui Mao", "Erik Cambria", "Xiaoying Tang", "Haoran Luo"]
pdf_path: pdfs/2602.01664.pdf
published_date: 2026-02-02
---

# FlowSteer: Towards Agents Designing Agentic Workflows via Reinforced Progressive Canvas Editing

**Authors**: Mingda Zhang, Wenjin Liu, Tiesunlong Shen, Qika Lin, Rui Mao, Erik Cambria, Xiaoying Tang, Haoran Luo
**Published**: February 2026
**Source**: https://arxiv.org/abs/2602.01664
**arXiv ID**: 2602.01664
**Categories**: Artificial Intelligence (cs.AI); Machine Learning (cs.LG)
**PDF**: [research/papers/pdfs/2602.01664.pdf](https://arxiv.org/abs/2602.01664)

---

## Abstract

This research addresses workflow construction challenges by introducing a new paradigm where a single agent itself end-to-end designs the workflow that a downstream executor runs. The authors present the Workflow Canvas, an executable graph-state environment providing syntax-checked feedback for atomic edits. They propose Reinforced Progressive Canvas Editing, training a policy agent via reinforcement learning to issue one atomic edit per turn based on real feedback. The framework supports diverse operator libraries and interchangeable language model backends. Testing across twelve datasets demonstrates FlowSteer significantly outperforms baselines across various tasks, with code made publicly available.

---

## Core Thesis

- 提出新範式：讓單一 agent 端到端自行設計下游執行器要跑的 workflow，而非人工預先設計固定 pipeline。
- 核心機制 Workflow Canvas：可執行的 graph-state 環境，對每次 atomic edit 提供語法檢查回饋；用 Reinforced Progressive Canvas Editing 訓練 policy agent，每輪基於真實回饋發出一次原子編輯（而非一次生成整個 workflow）。
- 支援多樣化 operator library 與可替換 LLM backend；12 個資料集上顯著優於基準，並開源程式碼。
- **Workspace 關聯**：與本庫既有 Loop/Workflow Engineering 收錄的 sew-2505-18646（自我演化多代理 workflow）主題相近，但方法不同——本文用「漸進式原子編輯 + RL policy」而非整體生成/演化，可作為未來設計「動態 workflow 生成 agent」時的替代方案參照。

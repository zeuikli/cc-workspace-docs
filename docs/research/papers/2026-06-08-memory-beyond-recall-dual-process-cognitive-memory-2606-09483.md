---
url: "https://arxiv.org/abs/2606.09483"
title: "Memory Beyond Recall: A Dual-Process Cognitive Memory System for Self-Evolving LLM Agents"
archived_date: 2026-06-24
arxiv_id: 2606.09483
authors: ["Tianxiang Fei", "Mingyang Song", "Mao Zheng", "Xiang Yu"]
domains: [cs.CL]
html: "https://arxiv.org/html/2606.09483v1"
pdf_path: pdfs/2606.09483.pdf
published_date: 2026-06-08
---

# Memory Beyond Recall: A Dual-Process Cognitive Memory System for Self-Evolving LLM Agents

**Authors**: Tianxiang Fei, Mingyang Song, Mao Zheng, Xiang Yu
**Published**: June 08, 2026
**Source**: https://arxiv.org/abs/2606.09483 · [HTML](https://arxiv.org/html/2606.09483v1)
**arXiv ID**: 2606.09483
**Categories**: cs.CL
**PDF**: [research/papers/pdfs/2606.09483.pdf](https://arxiv.org/abs/2606.09483) (11 pp, full text archived)

---

## Abstract (quoted)

> Long-term memory for an LLM agent is more than retrieving the right passage at the right time. Current memory systems collapse belief revision, causal coupling, and cross-domain abstraction into a single retrieval surface tuned for surface recall, and consequently struggle on implicit personalisation that requires reasoning over how a user has evolved. We propose DCPM, which reorganises agent memory along a cognitive capability hierarchy ascending from raw inputs and atomic facts, through diachronic belief trajectories and identity, to domain schemas, latent intentions and cross-domain patterns. The hierarchy is driven by two processes inheriting the architectural split of dual-process theory: a synchronous daytime writer (System1) that records belief revisions as doubly linked supersedes chains, and an asynchronous nighttime engine (System2) that induces schemas and intentions and sweeps for cross-domain collisions abstracted into higher-level core schemas. On LongMemEval, PersonaMem and PersonaMem-v2, enabling System2 contributes most where the benchmark rewards implicit cross-session inference (up to +5.20 on PersonaMem-v2) and least on span recall, matching the architectural prediction.

---

## 結構化摘要

### 核心貢獻
- 提出 DCPM：將 agent memory 沿「認知能力階層」重組——從原始輸入/原子事實，經 diachronic belief trajectory 與 identity，到 domain schema、latent intention 與 cross-domain pattern。
- 借用 dual-process theory 的架構切分：同步白天 writer（System1）以 doubly linked supersedes chain 記錄 belief revision；非同步夜間引擎（System2）誘導 schema/intention 並掃描 cross-domain collision，抽象為更高層 core schema。
- 主張長期記憶不只是「正確時刻取出正確段落」，而需對「使用者如何演變」進行推理。

### 關鍵結果
- 於 LongMemEval、PersonaMem、PersonaMem-v2 評測：啟用 System2 在 benchmark 獎勵 implicit cross-session inference 時貢獻最大（PersonaMem-v2 上 up to +5.20），在 span recall 上貢獻最小，符合架構預測。

### 限制
- 文件未列明確 limitation 章節；判斷弱點：僅 4 作者短篇（11 頁），System2 非同步引擎的計算/延遲成本未在 abstract 量化；增益集中於特定 benchmark 子任務，泛化性待驗證。

---

## Workspace 關聯（評估，非既成結論）

- System1/System2 分工對應 context-management 的「online vs offline consolidation」思路；非同步夜間 schema 誘導 ≈ memory-compactor 的離線壓縮+整合 gate 概念。
- 「belief revision 以 supersedes chain 記錄」呼應 core.md RECORD「checkpoint + 反思入庫」與 LESSONS.md 的演化迴圈——舊 belief 不刪、標記 superseded。
- ⚠️ 落地門檻：本庫 MEMORY/LESSONS 為人工/hook 維護的 markdown，非自動 cross-domain schema induction；DCPM 的「夜間引擎」屬域外研究系統，僅概念可借鑑。

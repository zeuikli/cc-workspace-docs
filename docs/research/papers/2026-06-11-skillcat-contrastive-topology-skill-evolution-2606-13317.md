---
url: "https://arxiv.org/abs/2606.13317"
title: "SkillCAT: Contrastive Assessment and Topology-Aware Skill Self-Evolution for LLM Agents"
archived_date: 2026-06-24
arxiv_id: 2606.13317
authors: ["Kunfeng Chen", "Qihuang Zhong", "Juhua Liu", "Bo Du"]
domains: [cs.CL]
html: "https://arxiv.org/html/2606.13317v1"
pdf_path: pdfs/2606.13317.pdf
published_date: 2026-06-11
---

# SkillCAT: Contrastive Assessment and Topology-Aware Skill Self-Evolution for LLM Agents

**Authors**: Kunfeng Chen, Qihuang Zhong, Juhua Liu, Bo Du
**Published**: June 11, 2026
**Source**: https://arxiv.org/abs/2606.13317 · [HTML](https://arxiv.org/html/2606.13317v1)
**arXiv ID**: 2606.13317
**Categories**: cs.CL
**PDF**: [research/papers/pdfs/2606.13317.pdf](https://arxiv.org/abs/2606.13317) (9 pp, full text archived)

---

## Abstract (quoted)

> Skill self-evolution methods for LLM agents aim to turn execution trajectories into reusable skill documents, but current pipelines typically learn from one trajectory per task, merge candidate skill patches before checking them, and load the full skill corpus before inference. We propose SkillCAT, a training-free framework that separates this process into three stages. Contrastive Causal Extraction (CCE) samples multiple trajectories for each task and compares same-task success/failure pairs to identify evidence that explains outcome differences. Assessment-Augmented Evolution (AAE) replays each candidate patch on source-task clones and keeps only patches that improve or preserve task outcomes before hierarchical skill patch merging. Topology-Aware Task Execution (TTE) compiles the evolved skills into a routable sub-skill topology, so inference loads only the capability nodes relevant to the task. We evaluate SkillCAT on common agent benchmarks, including SpreadsheetBench, WikiTableQuestions, and DocVQA, and further test cross-model and out-of-distribution generalization. Across these settings, SkillCAT raises the average score over baselines by up to 40.40%, demonstrating reliable skill evolution without model training.

---

## 結構化摘要

### 核心貢獻
training-free 的 skill 自演化框架，修正現有三個缺陷（單 trajectory 學習 / patch 未驗先 merge / inference 載入全 corpus）。三階段：

1. **CCE（Contrastive Causal Extraction）** — 每任務多 trajectory，比對同任務 success/failure 配對，抽出「解釋成敗差異」的證據（非單軌）。
2. **AAE（Assessment-Augmented Evolution）** — 每個候選 patch 在 source-task clone 上 replay，**只保留改善或維持結果的 patch** 才進階層式 merge（= 演化-後-驗證閘）。
3. **TTE（Topology-Aware Task Execution）** — 演化後 skill 編成可路由的 sub-skill topology，inference 只載入相關 capability node（降 context）。

### 關鍵結果
- 跨 SpreadsheetBench / WikiTableQuestions / DocVQA，平均分數超基線 **最多 +40.40%**；含 cross-model 與 OOD 泛化。

### 限制
- 9 pp，benchmark 偏 document/table 任務；多 trajectory 取樣成本未量化。

---

## Workspace 關聯（評估，非既成結論）

- **直接補 `skill-evolution` 的演化-後-驗證閉環**：AAE「patch replay 只保留不回退者」= seesaw constraint 於 skill 層；對應 harness-synthesis 報告 T27（skill empirical eval gate）。
- **TTE ↔ lazy-load**：「只載相關 capability node」印證本 workspace skill lazy-load + 對應 SkillRAE 的 skill-graph 選擇性載入。
- **CCE success/failure 對比**：可作 `skill-evolution:scan` 的證據抽取方法參考（非只看單次成功）。
- ⚠️ 落地需多 trajectory + replay clone 基建，本 workspace 暫無自動 trajectory store（同 trace-pipeline 缺口）。

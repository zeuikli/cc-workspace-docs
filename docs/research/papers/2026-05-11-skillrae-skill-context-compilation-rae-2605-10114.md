---
url: "https://arxiv.org/abs/2605.10114"
title: "SkillRAE: Agent Skill-Based Context Compilation for Retrieval-Augmented Execution"
archived_date: 2026-06-24
arxiv_id: 2605.10114
authors: ["Xiangcheng Meng", "Shu Wang", "Yixiang Fang"]
domains: [cs.CL]
html: "https://arxiv.org/html/2605.10114v1"
pdf_path: pdfs/2605.10114.pdf
published_date: 2026-05-11
---

# SkillRAE: Agent Skill-Based Context Compilation for Retrieval-Augmented Execution

**Authors**: Xiangcheng Meng, Shu Wang, Yixiang Fang
**Published**: May 11, 2026
**Source**: https://arxiv.org/abs/2605.10114 · [HTML](https://arxiv.org/html/2605.10114v1)
**arXiv ID**: 2605.10114
**Categories**: cs.CL
**PDF**: [research/papers/pdfs/2605.10114.pdf](https://arxiv.org/abs/2605.10114) (16 pp, full text archived)

---

## Abstract (quoted)

> Large Language Model (LLM)-based agents (e.g., OpenClaw) increasingly rely on reusable skill libraries to solve artifact-rich tasks such as document-centric workflows and data-intensive analysis. As these libraries grow, a few works have attempted to study the Retrieval-Augmented Execution (RAE), which often first retrieves some external skills and other knowledge, then compiles the context using retrieved skills, and finally executes the task. Existing works mainly focus on optimizing skill retrieval and task execution, and they pay little attention to how to effectively organize the selected skill evidence in a form that is compact, grounded, and immediately usable for the downstream executors to complete tasks. To fill this gap, we propose SkillRAE, a two-stage RAE approach focusing on skill-based context compilation, which consists of the offline and online stages. Specifically, in the offline indexing stage, it builds a multi-level skill graph over skill communities, skills, and reusable subunits, for capturing their relationships. In the online retrieval stage, it first performs skill-ranked retrieval with selected-subunit evidence export in the graph, and then applies rescue-aware compact compilation to recover the key evidence. Together, these components compile a coarse-ranked skill set into a task-specific context that is compact, grounded, and immediately usable. Experiments on two public benchmarks show that SkillRAE achieves a significant improvement over baselines for RAE. For example, on SkillsBench, it achieves an improvement of 11.7% over the SOTA method. Ablation studies further show that our context compilation is crucial, instead of a mere prompt addition.

---

## 結構化摘要

### 核心貢獻
RAE（Retrieval-Augmented Execution）的「skill 證據組織」缺口：現有只優化 retrieval/execution，忽略把選中 skill 組成 compact/grounded/即用的 context。兩階段：

1. **Offline indexing** — 建 multi-level skill graph（skill communities → skills → reusable subunits）捕捉關係。
2. **Online retrieval** — skill-ranked retrieval + selected-subunit 證據匯出 → **rescue-aware compact compilation** 救回關鍵證據，編成 task-specific compact context。

### 關鍵結果
- 兩 benchmark 顯著超基線；SkillsBench 上超 SOTA **+11.7%**。Ablation：context compilation 關鍵（非單純 prompt 添加）。

### 限制
- 16 pp；offline skill graph 需語料規模支撐，小型 skill 庫收益待評估。

### 命名注意
- abstract 提及 "OpenClaw" 等為論文示例 agent 名（模擬時間軸），非本 workspace 元件。

---

## Workspace 關聯（評估，非既成結論）

- **對應 harness-synthesis §7 SkillRAE 候選**：本 workspace 28 skills lazy-load，SkillRAE 的 skill-graph 選擇性載入是「多 skill 載入 token 膨脹」的進階解；但審計指 28 skills 規模偏小，**收益待實測**（列低優先）。
- **rescue-aware compact compilation ↔ context-management**：compact 但保關鍵證據，呼應 ACE 防 context collapse、pre-compact.sh HEAD/TAIL/MIDDLE。
- **multi-level skill graph ↔ RESOLVER.md**：本 workspace 已有 RESOLVER 路由表（人工），SkillRAE 是其自動化/圖化方向參考。
- ⚠️ 與 SkillCAT TTE topology 同屬「skill 拓撲化載入」線；兩者可對照但落地皆需 skill 規模門檻。

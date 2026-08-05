---
url: "https://arxiv.org/abs/2605.10907"
title: "Engineering Robustness into Personal Agents with the AI Workflow Store"
archived_date: 2026-07-18
arxiv_id: 2605.10907
authors: ["Roxana Geambasu", "Mariana Raykova", "Pierre Tholoniat", "Trishita Tiwari", "Lillian Tsai", "Wen Zhang"]
pdf_path: pdfs/2605.10907.pdf
published_date: 2026-05-11
---

# Engineering Robustness into Personal Agents with the AI Workflow Store

**Authors**: Roxana Geambasu, Mariana Raykova, Pierre Tholoniat, Trishita Tiwari, Lillian Tsai, Wen Zhang
**Published**: May 2026
**Source**: https://arxiv.org/abs/2605.10907
**arXiv ID**: 2605.10907
**Categories**: Cryptography and Security (cs.CR); Artificial Intelligence (cs.AI)
**PDF**: [research/papers/pdfs/2605.10907.pdf](https://arxiv.org/abs/2605.10907)

---

## Abstract

The paper critiques the prevailing "on-the-fly" agent paradigm, arguing it short-circuits disciplined software engineering processes. The authors contend that rapid real-time synthesis may deliver improvised prototypes rather than systems fit for high-stakes scenarios where reliability matters. They propose integrating rigorous engineering practices to create production-grade, hardened, and deterministically-constrained agent workflows that exceed the robustness of improvised approaches. To manage the computational overhead, they suggest amortizing costs through community reuse. The core vision centers on an "AI Workflow Store" comprising pre-hardened, reusable workflows offering substantially greater reliability and security than improvised tool chains. The research addresses fundamental tensions between flexibility and robustness that necessitate moving beyond on-the-fly methodologies.

---

## Core Thesis

- 批評主流「on-the-fly」agent 範式（每次即時合成執行計畫）繞過紮實的軟體工程流程，高風險場景下產出的常是「臨場拼裝原型」而非可靠系統。
- 主張導入嚴謹工程實踐，把 workflow 打造成「production-grade、hardened、確定性約束」而非即興生成，並透過社群重用（reusable workflow）分攤工程成本。
- 提出 "AI Workflow Store" 願景：預先硬化過、可重用的 workflow 集合，比臨場拼裝的工具鏈更可靠、更安全。
- **Workspace 關聯**：與 core.md「規範優先」及 APPLY 章「既有慣例 > 個人偏好」精神一致——本文主張「可重用、預先硬化的 workflow」而非每次臨場決策，呼應本 workspace 用 skills/agents/hooks 固化重複性任務流程（而非每次讓 LLM 即興規劃）的設計取向。

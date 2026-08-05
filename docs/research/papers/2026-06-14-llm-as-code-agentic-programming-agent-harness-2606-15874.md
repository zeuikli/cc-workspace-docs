---
url: "https://arxiv.org/abs/2606.15874"
title: "LLM-as-Code: Agentic Programming for Agent Harness"
archived_date: 2026-06-24
arxiv_id: 2606.15874
authors: ["Junjia Qi", "Zichuan Fu", "Jingtong Gao", "Wenlin Zhang", "Hanyu Yan", "Xian Wu", "Xiangyu Zhao"]
domains: [cs.AI, cs.SE]
html: "https://arxiv.org/html/2606.15874v2"
pdf_path: pdfs/2606.15874.pdf
published_date: 2026-06-14
venue: KDD 2026 Workshop on Agentic Software Engineering
---

# LLM-as-Code: Agentic Programming for Agent Harness

**Authors**: Junjia Qi, Zichuan Fu, Jingtong Gao, Wenlin Zhang, Hanyu Yan, Xian Wu, Xiangyu Zhao
**Published**: June 14, 2026 (v2: June 22, 2026) · Accepted at KDD 2026 Workshop on Agentic Software Engineering
**Source**: https://arxiv.org/abs/2606.15874 · [HTML](https://arxiv.org/html/2606.15874v2)
**arXiv ID**: 2606.15874
**Categories**: cs.AI, cs.SE
**PDF**: [research/papers/pdfs/2606.15874.pdf](https://arxiv.org/abs/2606.15874) (7 pp, full text archived)

---

## Abstract (quoted)

> Every major LLM agent framework gives the LLM the role of orchestrator; the model decides what to do next, when to call tools, and when to stop. We argue that token explosion, control-flow hallucination, and unreliable completion are not implementation bugs but architectural consequences of assigning the deterministic work of looping, branching, and sequencing to a probabilistic system. A better prompt or a stronger model cannot guarantee the reliability of the LLM agent. We therefore propose Agentic Programming, in which the program governs all control flow, and the LLM is itself part of it, an adaptive component we call LLM-as-Code and invoke only where a task calls for reasoning or generation. Within each call the model keeps full flexibility, but it cannot alter the program's execution path. With control in the program, the LLM's context is built from the execution history's call tree and forms a directed acyclic graph (DAG). Each call's context length is then determined by its call depth rather than by accumulation over steps. A case study of computer-use agents shows that the design is practical, not just a theoretical stance, substantially improving the stability of long visual operation sequences.

---

## 結構化摘要

### 核心貢獻
論點：token explosion、control-flow hallucination、unreliable completion **不是 bug，而是「把 loop/branch/sequence 這類確定性工作交給機率系統」的架構後果**——換更好 prompt / 更強模型都救不了。

- **Agentic Programming**：由 **program 掌管所有 control flow**，LLM 只是其中可調用元件（**LLM-as-Code**），僅在需 reasoning/generation 時呼叫。
- 單次呼叫內模型保有完整彈性，但**不能改變 program 的執行路徑**。
- **context 由執行歷史 call tree 構成 DAG**：每次呼叫的 context 長度由 **call depth** 決定，而非隨步數累積 → 抑制 token 爆炸。

### 關鍵結果
- computer-use agent case study：顯著提升長視覺操作序列的穩定性（abstract 未給具體數字）。

### 限制
- 7 pp workshop 短文；僅單一 case study，缺跨領域定量評估。

---

## Workspace 關聯（評估，非既成結論）

- **與 core.md 跨切紀律幾乎逐字對齊**：「LLM 只做判斷、確定性代碼做決定（路由/重試/控制流）」= 本文「program 掌 control flow、LLM-as-Code 只做 reasoning」。最強外部背書之一。
- **Workflow 工具的理論依據**：本 workspace 的 dynamic Workflow（deterministic 控制流 + agent() 做判斷）正是 Agentic Programming 的實例；可作 multi-mode-skill / Workflow 設計論證引用。
- **DAG context by call-depth = context-management.md NLAH**：context 不隨步數累積、由結構決定——直接呼應「right context > more context」與 prompt caching 紀律。
- ⚠️ code-as-harness（2605-18747）的延伸/激進版；列為 harness-engineering 控制流子線核心讀物。

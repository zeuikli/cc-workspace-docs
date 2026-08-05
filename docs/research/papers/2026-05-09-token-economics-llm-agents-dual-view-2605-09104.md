---
url: "https://arxiv.org/abs/2605.09104"
title: "Token Economics for LLM Agents: A Dual-View Study from Computing and Economics"
archived_date: 2026-07-17
arxiv_id: 2605.09104
authors: ["Yuxi Chen", "Junming Chen", "Chenyu He", "Yiwei Li", "Yicheng Ji", "Yifan Wu", "Dingyu Yang", "Lansong Diao", "Lidan Shou", "Hongliang Zhang", "Huan Li", "Gang Chen"]
domains: [cs.AI]
html: "https://arxiv.org/html/2605.09104v1"
pdf_path: pdfs/2605.09104.pdf
published_date: 2026-05-09
---

# Token Economics for LLM Agents: A Dual-View Study from Computing and Economics

**Authors**: Yuxi Chen et al.（12 位作者）
**Published**: May 9, 2026
**Source**: https://arxiv.org/abs/2605.09104 · [HTML](https://arxiv.org/html/2605.09104v1)
**arXiv ID**: 2605.09104
**Categories**: cs.AI
**PDF**: [research/papers/pdfs/2605.09104.pdf](https://arxiv.org/abs/2605.09104)

---

## Abstract (quoted)

> As LLM agents evolve, tokens have emerged as the core economic primitives of Agentic AI. However, their exponential consumption introduces severe computational, collaborative, and security bottlenecks. Current surveys remain fragmented across system optimization, architecture design, and trust, lacking a unified framework to evaluate the fundamental trade-off between output quality and economic cost. To bridge this gap, this survey presents the first comprehensive survey of Token Economics. By unifying computer science and economics, we conceptualize tokens as production factors, exchange mediums, and units of account. We synthesize existing literature across a four-dimensional taxonomy: (1) Micro-level (Single Agent): Optimizing budget-constrained factor substitution via neoclassical firm theory. (2) Meso-level (Multi-Agent Systems): Minimizing collaboration friction using transaction cost and principal-agent theories. (3) Macro-level (Agent Ecosystems): Addressing congestion externalities and pricing via mechanism design. (4) Security: Internalizing adversarial threats as endogenous economic constraints. Finally, we outline frontier directions, including differentiable token budgets and dynamic markets, to lay the theoretical foundation for scalable next-generation agent systems.

---

## 結構化摘要

### 核心貢獻

- 首個 Token Economics 綜述：把 token 概念化為生產要素、交換媒介、記帳單位，統一 CS 與經濟學視角
- 四維分類法：Micro（單 agent 預算約束的要素替代）/ Meso（MAS 用交易成本與 principal-agent 理論降協作摩擦）/ Macro（生態系壅塞外部性與定價機制設計）/ Security（對抗威脅內生化為經濟約束）

### 關鍵結果

- 綜述性論文，無單一實驗數字；提出 differentiable token budgets、dynamic markets 等前沿方向

### 限制

- 理論框架綜述，工程可操作性需自行轉譯
- 經濟學類比（firm theory 等）的解釋力上限未經實證檢驗

---

## Workspace 關聯（評估，非既成結論）

- principal-agent theory 視角精準對應 `core.md §PROPOSE 委派`（原 subagent-strategy.md）的 handoff 固定開銷計算與 benefit-gated 委派——委派決策本質是交易成本比較，可為 `core.md §PROPOSE 委派``） 提供理論詞彙。
- Micro-level「budget-constrained factor substitution」即檔位經濟（cost/quality/ceiling）的理論化；與 `.claude/skills/output-compress` 檔位上限、FinOps 判斷框架直接共鳴。

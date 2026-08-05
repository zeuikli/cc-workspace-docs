---
url: "https://arxiv.org/abs/2607.08028"
title: "From Prompts to Contracts: Harness Engineering for Auditable Enterprise LLM Agents"
archived_date: 2026-07-18
arxiv_id: 2607.08028
authors: ["Joongho Ahn", "Moonsoo Kim"]
pdf_path: pdfs/2607.08028.pdf
published_date: 2026-07-09
---

# From Prompts to Contracts: Harness Engineering for Auditable Enterprise LLM Agents

**Authors**: Joongho Ahn, Moonsoo Kim
**Published**: July 2026
**Source**: https://arxiv.org/abs/2607.08028
**arXiv ID**: 2607.08028
**Categories**: Artificial Intelligence (cs.AI); Computation and Language (cs.CL); Software Engineering (cs.SE)
**PDF**: [research/papers/pdfs/2607.08028.pdf](https://arxiv.org/abs/2607.08028)

---

## Abstract

The paper presents an engineering framework that transforms exploratory LLM prototypes into production-ready systems. Rather than relying solely on prompt-based behavior, the authors propose moving deterministic behavior into code, manifests, schemas, and validation artifacts while maintaining source-backed claims as the foundation for runtime answers. The research evaluates three key aspects: first, the harness maintains its contractual guarantees across validation scenarios, with fault injection confirming validators detect broken contracts; second, enforcement checks remain effective across different model substitutions, with 270 composition-boundary runs passing; third, code-level enforcement is essential — prompt-only instructions alone permit policy violations that the harness prevents entirely. Compared to external guardrails (which achieve only 88/120 utility by over-refusing), the approach preserves full utility at 120/120 while maintaining safety and auditability. The pattern is instantiated on Korean corporate data spanning five groups and 25 listed companies.

---

## Core Thesis

- 主張「合約優先」harness 設計：把可稽核行為從 prompt 移到程式碼/manifest/schema/驗證器，prompt 只負責探索性行為，硬性保證由確定性程式碼承擔。
- Fault injection 實測驗證器能偵測合約破壞；模型替換（model substitution）下 270 次 composition-boundary 測試仍守住 enforcement，證明 harness-level 保證與底層模型解耦。
- 對比外部 guardrail（過度拒絕、僅 88/120 utility）與本框架（120/120 utility 同時維持安全與可稽核性），顯示「code-level enforcement > prompt-only instruction」。
- **Workspace 關聯**：與 core.md 公理「LLM 只做判斷、確定性程式碼做決定」高度一致；「prompt-only 允許政策違反，harness 完全阻擋」佐證本 workspace 硬性執行交給 hooks 而非 advisory 規則的既有立場。

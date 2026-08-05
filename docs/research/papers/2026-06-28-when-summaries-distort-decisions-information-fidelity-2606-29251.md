---
url: "https://arxiv.org/abs/2606.29251"
title: "When Summaries Distort Decisions: Information Fidelity in LLM-Compressed Financial Analysis"
archived_date: 2026-07-17
arxiv_id: 2606.29251
authors: ["Hoyoung Lee", "Suhwan Park", "Seunghan Lee", "Jun Seo", "Jaehoon Lee", "Sungdong Yoo", "Minjae Kim", "CheolWon Na", "Zhangyang Wang", "Zach Golkhou", "Minkyu Kim", "Sotirios Sabanis", "Alejandro Lopez-Lira", "Dhagash Mehta", "Soonyoung Lee", "Chanyeol Choi", "Wonbin Ahn", "Yongjae Lee"]
domains: [cs.AI, q-fin.CP]
html: "https://arxiv.org/html/2606.29251v1"
pdf_path: pdfs/2606.29251.pdf
published_date: 2026-06-28
---

# When Summaries Distort Decisions: Information Fidelity in LLM-Compressed Financial Analysis

**Authors**: Hoyoung Lee et al.（18 位作者）
**Published**: June 28, 2026
**Source**: https://arxiv.org/abs/2606.29251 · [HTML](https://arxiv.org/html/2606.29251v1)
**arXiv ID**: 2606.29251
**Categories**: cs.AI, q-fin.CP
**PDF**: [research/papers/pdfs/2606.29251.pdf](https://arxiv.org/abs/2606.29251)

---

## Abstract (quoted)

> （WebFetch 取得為摘述版，逐字全文未取得；以下為抓取內容）Financial decision-makers face challenges when LLMs compress source material — "compression loses fidelity when it changes the decision induced by the source." The paper identifies two diagnostic patterns causing information loss: decontextualization (salient evidence retained but separated from the caveats and contextual qualifiers needed for correct interpretation) and model dependency (different compressors produce varying interpretations). It proposes Agentic Context Compression, which "generates multiple candidate compressions and audits their disagreements against the original source."

---

## 結構化摘要

### 核心貢獻

- 提出「decision fidelity」視角：壓縮保真的判準不是表面事實正確，而是**壓縮後是否改變 source 誘導的決策**
- 識別兩種診斷性失真模式：decontextualization（重點證據被保留但脫離解讀所需的 caveat/限定語境）與 model dependency（不同壓縮器產出不同詮釋）
- 提出 Agentic Context Compression：生成多個候選壓縮版本，對照原始 source 稽核彼此分歧

### 關鍵結果

- 展示 LLM 壓縮可產出「可讀但改變決策」的金融摘要——壓縮評估應優先保留 decision-relevant context，而非只看效率與 factuality
- 具體量化數字：未取得（abstract 摘述未含）

### 限制

- 領域限定於金融分析文本，其他決策場景泛化性未驗證
- 多候選壓縮 + 稽核帶來額外 inference 成本，abstract 未報成本開銷

---

## Workspace 關聯（評估，非既成結論）

- 直接對應 `.claude/skills/output-compress` 的**機械失真閘**設計動機：本文證明「壓縮後仍流暢可讀」≠「決策等價」，支持 whitelist 不變式（保重點白名單）優先於壓縮率。
- decontextualization 模式正是 output-compress「安全紅線/不可逆確認語句不得壓縮」排除項的實證依據——caveat 脫落即決策失真。
- Agentic Context Compression 的多候選+分歧稽核與 workspace 對抗互審（judge 偏誤控制）同構，可評估作為 fidelity gate 的升級選項。⚠️ 成本增量需 FinOps 評估。

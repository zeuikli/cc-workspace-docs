---
url: "https://arxiv.org/abs/2512.14244"
title: "From Context to EDUs: Faithful and Structured Context Compression via Elementary Discourse Unit Decomposition"
archived_date: 2026-07-17
arxiv_id: 2512.14244
authors: ["Yiqing Zhou", "Yu Lei", "Shuzheng Si", "Qingyan Sun", "Wei Wang", "Yifei Wu", "Hao Wen", "Gang Chen", "Fanchao Qi", "Maosong Sun"]
domains: [cs.CL, cs.AI]
html: "https://arxiv.org/html/2512.14244v1"
pdf_path: pdfs/2512.14244.pdf
published_date: 2025-12-16
---

# From Context to EDUs: Faithful and Structured Context Compression via Elementary Discourse Unit Decomposition

**Authors**: Yiqing Zhou, Yu Lei, Shuzheng Si, Qingyan Sun, Wei Wang, Yifei Wu, Hao Wen, Gang Chen, Fanchao Qi, Maosong Sun
**Published**: December 16, 2025
**Source**: https://arxiv.org/abs/2512.14244 · [HTML](https://arxiv.org/html/2512.14244v1)
**arXiv ID**: 2512.14244
**Categories**: cs.CL, cs.AI
**PDF**: [research/papers/pdfs/2512.14244.pdf](https://arxiv.org/abs/2512.14244)

---

## Abstract (quoted)

> （WebFetch 取得為摘述版，逐字全文未取得；以下為抓取內容）Managing extensive context remains a critical challenge for LLMs, particularly in long-document QA and autonomous agents. The paper presents the EDU-based Context Compressor, which converts text into a structural tree of Elementary Discourse Units while preserving both global organization and local details, via a two-stage approach: transform linear content into EDU-based trees, then select query-relevant components. It introduces StructBench, a manually annotated benchmark of 248 documents, and "achieves state-of-the-art structural prediction accuracy" while outperforming frontier LLMs and reducing computational expenses across downstream applications.

---

## 結構化摘要

### 核心貢獻

- 以 Elementary Discourse Unit（EDU）為壓縮原子單位：先把線性文本轉為 EDU 結構樹（保全域組織 + 局部細節），再按 query 選取相關子樹
- 兩階段管線把「壓縮」重構為「結構化分解 + 選擇」，而非端到端改寫——保真來自不改寫只挑選
- 發布 StructBench：248 篇人工標注文件的結構預測 benchmark

### 關鍵結果

- 結構預測準確率達 SOTA；在 downstream 應用上勝過 frontier LLM 直接壓縮並降低計算成本
- 具體數字：未取得（abstract 摘述未含）

### 限制

- EDU 樹建構本身有前置成本，短文本場景可能不划算
- benchmark 規模 248 篇、人工標注，領域覆蓋度未知

---

## Workspace 關聯（評估，非既成結論）

- 「分解-選取而非改寫」正是 `.claude/skills/output-compress` whitelist 不變式的結構化版本：白名單保留 = 選取原文單位，天然免疫 knowledge overwriting / semantic drift（對照 2602.09789）。
- EDU 粒度可作為分級壓縮（lite/full/ultra）的粒度定義候選——lite 刪整棵低相關子樹、ultra 只留 query 命中 EDU。⚠️ 落地需離線 EDU 分割工具，屬新依賴，需評估。

---
url: "https://arxiv.org/abs/2606.02359"
title: "MOC: Multi-Order Communication in LLM-based Multi-Agent Systems"
archived_date: 2026-07-17
arxiv_id: 2606.02359
authors: ["Yao Guan", "Lin Wang", "Zhihu Lu", "Ziyi Wang", "Wenzhu Yan", "Qiang Duan"]
domains: [cs.AI]
html: "https://arxiv.org/html/2606.02359v1"
pdf_path: pdfs/2606.02359.pdf
published_date: 2026-06-01
---

# MOC: Multi-Order Communication in LLM-based Multi-Agent Systems

**Authors**: Yao Guan, Lin Wang, Zhihu Lu, Ziyi Wang, Wenzhu Yan, Qiang Duan
**Published**: June 1, 2026
**Source**: https://arxiv.org/abs/2606.02359 · [HTML](https://arxiv.org/html/2606.02359v1)
**arXiv ID**: 2606.02359
**Categories**: cs.AI
**Code**: https://github.com/yao-guan/MOC
**PDF**: [research/papers/pdfs/2606.02359.pdf](https://arxiv.org/abs/2606.02359)

---

## Abstract (quoted)

> Despite the remarkable progress of Large Language Model (LLM) based Multi-Agent Systems, most research focuses on optimizing coordination topology while largely underexploring the equally critical problem: how to transmit and optimize messages among agents effectively? Current communication schemes typically rely on the direct concatenation of first-order neighbor responses, which induces a restricted evidence receptive field and leads to the dilution of crucial insights over multi-hop paths. To address these limitations, we propose the Multi-Order Communication (MOC) scheme, which reconstructs the inter-agent communication to capture multi-hop dependencies and incorporates a structural message consolidation strategy to ensure efficiency. Specifically, we formalize the communication mechanism to construct a structured multi-order evidence stream, and subsequently design a Semantic-Topological Merging algorithm to optimize semantic fidelity within token constraints. Extensive experiments across six diverse datasets and LLM backbones of varying parameter scales demonstrate that MOC consistently improves task performance and reduces communication costs.

---

## 結構化摘要

### 核心貢獻

- 指出 MAS 研究偏重拓樸、忽視「訊息本身如何傳輸與優化」；一階鄰居直接串接導致 evidence receptive field 受限、關鍵洞見沿多跳路徑稀釋
- MOC：重構通訊以捕捉 multi-hop 依賴，建構結構化 multi-order evidence stream
- Semantic-Topological Merging 演算法：在 token 約束內最大化語義保真

### 關鍵結果

- 六個資料集、多種參數規模 backbone 上一致提升任務表現並降低通訊成本；具體數字未取得（abstract 未含）
- 開源程式碼（github.com/yao-guan/MOC）

### 限制

- workspace 拓樸限 parent↔child 兩層，multi-hop 稀釋問題在深層巢狀委派才顯著
- merging 演算法本身的計算開銷未在 abstract 報告

---

## Workspace 關聯（評估，非既成結論）

- 「多跳路徑稀釋關鍵洞見」是 `core.md §PROPOSE 委派`（原 subagent-strategy.md） 禁 child 間互通、通訊限 parent↔child 的獨立佐證：層數即失真放大器。 〔v5.1：所引 workspace 細則已退役 → 見 `INDEX.md` §v5.1 規則退役對照〕
- 「token 約束內優化語義保真」與 `.claude/skills/output-compress` 的 fidelity gate 目標同構——壓縮上限應以保真為約束而非壓縮率最大化。⚠️ workspace 無深層 MAS，方法本體暫無落地面。

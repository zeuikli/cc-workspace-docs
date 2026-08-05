---
url: "https://arxiv.org/abs/2602.09789"
title: "When Less is More: The LLM Scaling Paradox in Context Compression"
archived_date: 2026-07-17
arxiv_id: 2602.09789
authors: ["Ruishan Guo", "Yibing Liu", "Guoxin Ma", "Yan Wang", "Yueyang Zhang", "Long Xia", "Kecheng Chen", "Zhiyuan Sun", "Daiting Shi"]
domains: [cs.LG]
html: "https://arxiv.org/html/2602.09789v1"
pdf_path: pdfs/2602.09789.pdf
published_date: 2026-02-10
---

# When Less is More: The LLM Scaling Paradox in Context Compression

**Authors**: Ruishan Guo, Yibing Liu, Guoxin Ma, Yan Wang, Yueyang Zhang, Long Xia, Kecheng Chen, Zhiyuan Sun, Daiting Shi
**Published**: February 10, 2026
**Source**: https://arxiv.org/abs/2602.09789 · [HTML](https://arxiv.org/html/2602.09789v1)
**arXiv ID**: 2602.09789
**Categories**: cs.LG
**PDF**: [research/papers/pdfs/2602.09789.pdf](https://arxiv.org/abs/2602.09789)

---

## Abstract (quoted)

> （WebFetch 取得為摘述版，逐字全文未取得；以下為抓取內容）The paper challenges the assumption that larger models compress better. In a compressor-decoder lossy context compression framework, the authors identify a "Size-Fidelity Paradox": expanding compressor size can reduce the accuracy of reconstructed contexts even when reconstruction error decreases. Across 27 experimental configurations, two mechanisms emerge: "knowledge overwriting" (larger models substitute source facts with their own learned patterns, e.g. "white strawberry" → "red strawberry") and "semantic drift" (larger models rephrase/reorganize rather than reproduce, e.g. "Alice hit Bob" → "Bob hit Alice"). Mid-sized compressors frequently outperform larger ones; larger models distribute information across broader semantic spaces, creating ambiguous encodings vulnerable to modification. Scaling laws break down when the goal shifts from plausible generation to faithful preservation.

---

## 結構化摘要

### 核心貢獻

- 提出 Size-Fidelity Paradox：壓縮器模型愈大，重建 context 的忠實度反而可能下降（即使 reconstruction error 下降）
- 識別兩種失真機制：knowledge overwriting（大模型用自身先驗覆蓋 source 事實）與 semantic drift（改寫/重組而非忠實重現）
- 指出 scaling law 在「plausible generation → faithful preservation」目標切換時失效

### 關鍵結果

- 27 組實驗配置中 paradox 持續成立；中型壓縮器常勝過大型
- 大模型將資訊分散到更廣語義空間 → 編碼模糊、易被改寫、恢復力弱

### 限制

- abstract 未列具體模型家族與規模區間，paradox 的規模邊界未知
- 聚焦 compressor-decoder 重建任務，對 agent 場景「摘要供下游決策」的外推需驗證

---

## Workspace 關聯（評估，非既成結論）

- 直接挑戰「壓縮任務升檔位更保真」的直覺——對 `.claude/skills/output-compress` 的檔位上限設計是關鍵證據：壓縮/摘要類機械任務用 cost 檔可能不只省錢還更忠實（knowledge overwriting 在強模型更嚴重）。
- knowledge overwriting 即 core.md「數字對帳雙向」防的失真型態；支持機械失真閘用確定性比對而非 LLM 自評。⚠️ 單篇證據，改動檔位策略前需與 model-profiles.md eval baselines 對照。

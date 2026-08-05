---
url: "https://arxiv.org/abs/2602.02369"
title: "Live-Evo: Online Evolution of Agentic Memory from Continuous Feedback"
archived_date: 2026-06-24
arxiv_id: 2602.02369
authors: ["Yaolun Zhang", "Yiran Wu", "Yijiong Yu", "Qingyun Wu", "Huazheng Wang"]
domains: [cs.AI, cs.LG]
html: "https://arxiv.org/html/2602.02369v1"
pdf_path: pdfs/2602.02369.pdf
published_date: 2026-02-02
---

# Live-Evo: Online Evolution of Agentic Memory from Continuous Feedback

**Authors**: Yaolun Zhang, Yiran Wu, Yijiong Yu, Qingyun Wu, Huazheng Wang
**Published**: February 2, 2026
**Source**: https://arxiv.org/abs/2602.02369 · [HTML](https://arxiv.org/html/2602.02369v1)
**arXiv ID**: 2602.02369
**Categories**: cs.AI, cs.LG
**PDF**: [research/papers/pdfs/2602.02369.pdf](https://arxiv.org/abs/2602.02369) (14 pp, full text archived)

---

## Abstract (quoted)

> Large language model (LLM) agents are increasingly equipped with memory, which are stored experience and reusable guidance that can improve task-solving performance. Recent self-evolving systems update memory based on interaction outcomes, but most existing evolution pipelines are developed for static train/test splits and only approximate online learning by folding static benchmarks, making them brittle under true distribution shift and continuous feedback. We introduce LIVE-Evo, an online self-evolving memory system that learns from a stream of incoming data over time. LIVE-Evo decouples what happened from how to use it via an Experience Bank and a Meta-Guideline Bank, compiling task-adaptive guidelines from retrieved experiences for each task. To manage memory online, LIVE-Evo maintains experience weights and updates them from feedback: experiences that consistently help are reinforced and retrieved more often, while misleading or stale experiences are down-weighted and gradually forgotten, analogous to reinforcement and decay in human memory.

---

## 結構化摘要

### 核心貢獻
線上自演化記憶系統，針對「靜態 train/test split 近似 online learning → distribution shift 下脆弱」的缺陷。雙 bank 解耦：

1. **Experience Bank**（what happened）vs **Meta-Guideline Bank**（how to use it）— 每任務從檢索到的 experience 編譯 task-adaptive guideline。
2. **線上權重管理**：experience 帶權重，依 feedback 更新——常幫上忙者**增強、更常被檢索**；誤導/過時者**降權、漸忘**（類比人腦 reinforcement/decay）。

### 關鍵結果
- Prophet Arena（10 週 horizon）：Brier score **+20.8%** 改善、market returns **+12.9%**；增益遷移至 deep-research benchmark。

### 限制
- 14 pp；權重更新依賴可靠 feedback 信號，feedback 稀疏時退化未深入。

---

## Workspace 關聯（評估，非既成結論）

- **補 `research-hub:deep` + `autoresearch`（原 `overnight-research`，v5.1 刪除） 多輪 corpus staleness**：experience 加權衰退 = 過時 citation 自動降權、反覆通過 gate 的 paper 升權，強化報告查核信度（harness-synthesis §7 候選）。
- **雙 bank ↔ 本 workspace MEMORY/LESSONS 分層**：Experience Bank≈session 記錄、Meta-Guideline Bank≈LESSONS 防範規則；可作 dreaming-consolidator 的記憶分層參考。
- **online weight 純 metadata 輕量**：無需 weight update，適合 black-box；落地門檻低於 SIA 權重更新。
- ⚠️ 需持續 feedback 流；本 workspace 為離散 session，feedback 訊號需設計（如 SIA evaluate.py pass/fail 作信號）。

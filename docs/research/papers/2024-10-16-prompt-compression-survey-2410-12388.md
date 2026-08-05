---
url: "https://arxiv.org/abs/2410.12388"
title: "Prompt Compression for Large Language Models: A Survey"
archived_date: 2026-07-17
arxiv_id: 2410.12388
authors: ["Zongqian Li", "Yinhong Liu", "Yixuan Su", "Nigel Collier"]
domains: [cs.CL]
html: "https://arxiv.org/html/2410.12388v1"
pdf_path: pdfs/2410.12388.pdf
published_date: 2024-10-16
---

# Prompt Compression for Large Language Models: A Survey

**Authors**: Zongqian Li, Yinhong Liu, Yixuan Su, Nigel Collier
**Published**: October 16, 2024
**Source**: https://arxiv.org/abs/2410.12388 · [HTML](https://arxiv.org/html/2410.12388v1)
**arXiv ID**: 2410.12388
**Categories**: cs.CL
**PDF**: [research/papers/pdfs/2410.12388.pdf](https://arxiv.org/abs/2410.12388)

---

## Abstract (quoted)

> Leveraging large language models (LLMs) for complex natural language tasks typically requires long-form prompts to convey detailed requirements and information, which results in increased memory usage and inference costs. To mitigate these challenges, multiple efficient methods have been proposed, with prompt compression gaining significant research interest. This survey provides an overview of prompt compression techniques, categorized into hard prompt methods and soft prompt methods. First, the technical approaches of these methods are compared, followed by an exploration of various ways to understand their mechanisms, including the perspectives of attention optimization, Parameter-Efficient Fine-Tuning (PEFT), modality integration, and new synthetic language. We also examine the downstream adaptations of various prompt compression techniques. Finally, the limitations of current prompt compression methods are analyzed, and several future directions are outlined, such as optimizing the compression encoder, combining hard and soft prompts methods, and leveraging insights from multimodality.

---

## 結構化摘要

### 核心貢獻

- Prompt compression 領域綜述：以 hard prompt（自然語言層刪減）vs soft prompt（連續向量）二分法系統化整理
- 從 attention optimization、PEFT、modality integration、synthetic language 四視角解釋壓縮機制
- 整理 downstream 適配與現有方法限制、未來方向（壓縮 encoder 優化、hard+soft 混合、多模態借鑑）

### 關鍵結果

- 綜述性論文，無單一實驗數字；價值在分類法與機制視角

### 限制

- 2024-10 成稿，未涵蓋其後的 decision-fidelity / scaling paradox 研究線
- soft prompt 方法多需白盒模型訓練，API-only 場景適用性弱

---

## Workspace 關聯（評估，非既成結論）

- 作為 `.claude/skills/output-compress` 相關論文群的領域地圖：workspace 可落地的僅 hard prompt 路線（自然語言層分級刪減），本綜述可用於定位 output-compress 在方法譜系中的座標與盲區。
- 「combining hard and soft prompts」等未來方向對 workspace 暫無行動意義，僅供背景。

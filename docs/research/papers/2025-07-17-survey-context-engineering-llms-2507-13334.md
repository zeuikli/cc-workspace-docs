---
url: "https://arxiv.org/abs/2507.13334"
title: "A Survey of Context Engineering for Large Language Models"
archived_date: 2026-06-24
arxiv_id: 2507.13334
authors: ["Lingrui Mei", "Jiayu Yao", "Yuyao Ge", "Yiwei Wang", "Baolong Bi", "Yujun Cai", "Jiazhi Liu", "Mingyu Li", "Zhong-Zhi Li", "Duzhen Zhang", "Chenlin Zhou", "Jiayi Mao", "Tianze Xia", "Jiafeng Guo", "Shenghua Liu"]
domains: [cs.CL, "context engineering", survey]
html: "https://arxiv.org/html/2507.13334v1"
pdf_path: pdfs/2507.13334.pdf
published_date: 2025-07-17
---

# A Survey of Context Engineering for Large Language Models

**Authors**: Lingrui Mei, Jiayu Yao, Yuyao Ge, Yiwei Wang, Baolong Bi, Yujun Cai, Jiazhi Liu, Mingyu Li, Zhong-Zhi Li, Duzhen Zhang, Chenlin Zhou, Jiayi Mao, Tianze Xia, Jiafeng Guo, Shenghua Liu
**Published**: July 17, 2025
**Source**: https://arxiv.org/abs/2507.13334 · [HTML](https://arxiv.org/html/2507.13334v1)
**arXiv ID**: 2507.13334
**Categories**: cs.CL
**PDF**: [research/papers/pdfs/2507.13334.pdf](https://arxiv.org/abs/2507.13334) (166 pp, full text archived)

---

## Abstract (quoted)

> The performance of Large Language Models (LLMs) is fundamentally determined by the contextual information provided during inference. This survey introduces Context Engineering, a formal discipline that transcends simple prompt design to encompass the systematic optimization of information payloads for LLMs. We present a comprehensive taxonomy decomposing Context Engineering into its foundational components and the sophisticated implementations that integrate them into intelligent systems. We first examine the foundational components: context retrieval and generation, context processing and context management. We then explore how these components are architecturally integrated to create sophisticated system implementations: retrieval-augmented generation (RAG), memory systems and tool-integrated reasoning, and multi-agent systems. Through this systematic analysis of over 1400 research papers, our survey not only establishes a technical roadmap for the field but also reveals a critical research gap: a fundamental asymmetry exists between model capabilities. While current models, augmented by advanced context engineering, demonstrate remarkable proficiency in understanding complex contexts, they exhibit pronounced limitations in generating equally sophisticated, long-form outputs. Addressing this gap is a defining priority for future research. Ultimately, this survey provides a unified framework for both researchers and engineers advancing context-aware AI.

---

## 結構化摘要

### 核心貢獻

- 提出 **Context Engineering** 作為正式學科，超越 prompt design，系統化定義 LLM 推論時 information payload 的最佳化框架
- 建立兩層 taxonomy：foundational components（context retrieval & generation、context processing、context management）與 system implementations（RAG、memory systems、tool-integrated reasoning、multi-agent systems）
- 系統分析逾 **1,400 篇**研究論文，涵蓋 context-aware AI 完整技術脈絡
- 識別關鍵研究缺口：模型在理解複雜 context 的能力遠優於生成等質量 long-form output 的能力（理解 vs 生成非對稱性）

### 關鍵結果

- 無單一量化 benchmark 數字（survey 性質）；核心方法層發現：context retrieval、processing、management 三組件是所有 sophisticated system（RAG、memory、multi-agent）的共通底層
- 揭示「context comprehension vs context generation 非對稱性」為當前 LLM 最重要的能力落差，是未來研究首要議題
- 提供對研究者與工程師均適用的統一框架（unified framework for context-aware AI）

### 限制

- Survey 涵蓋至 2025 年 7 月，快速演進領域存在時效性限制
- 1,400+ 論文覆蓋廣度高，但深度分析受篇幅制約；部分子領域可能處理較淺
- 「context generation gap」雖被識別為關鍵缺口，但論文本身未提供解法路徑，僅列為 future work 方向

---

## Workspace 關聯（評估，非既成結論）

- **直接對應 `.claude/rules/context-management.md`**：論文的 context management 分類（token budget、context processing）與 workspace 的 NLAH 原則、Compact 觸發機制、Prompt Caching 設計高度吻合；survey 提供學術支撐，可作為調整 context-management 規則的理論依據
- **multi-agent systems 章節 ↔ `core.md §PROPOSE 委派`（原 `subagent-strategy.md`）**：論文的 multi-agent 架構分析（fan-out、agent 協調、context 傳遞）直接對應 workspace 的委派決策準則與 hierarchical fan-out 上限 4 的設計；⚠️ 論文層次在學術描述，workspace 落地需額外考慮 `unverified_success` 閘門與 child 不 self-retry 等執行紀律 〔v5.1：所引 workspace 細則已退役 → 見 `INDEX.md` §v5.1 規則退役對照〕
- **memory systems ↔ `memory/MEMORY.md` 長期記憶回路**：論文的 memory system 分類（episodic/semantic/procedural）可指導 workspace MEMORY.md 結構演化；⚠️ 落地門檻：workspace 目前無向量檢索層，memory 仍是 flat markdown，論文方法需大幅簡化才可應用
- **The Loop OBSERVE 階段 ↔ context retrieval**：論文強調 context retrieval & generation 是所有 intelligent system 基礎，對應 core.md OBSERVE「先讀後動」紀律——兩者共同前提是「正確的 context 先於行動」；survey 指出的 comprehension/generation 非對稱性亦解釋了為何 The Loop 需要明確 TEST 階段驗證輸出而非信任 LLM 自報

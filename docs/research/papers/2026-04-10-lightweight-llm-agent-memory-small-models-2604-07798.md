---
url: "https://arxiv.org/abs/2604.07798"
title: "Lightweight LLM Agent Memory with Small Language Models"
archived_date: 2026-06-24
arxiv_id: 2604.07798
authors: ["Jiaquan Zhang", "Chaoning Zhang", "Shuxu Chen", "Zhenzhen Huang", "Pengcheng Zheng", "Zhicheng Wang", "Ping Guo", "Fan Mo", "Sung-Ho Bae", "Jie Zou", "Jiwei Wei", "Yang Yang"]
domains: [cs.AI]
html: "https://arxiv.org/html/2604.07798v1"
pdf_path: pdfs/2604.07798.pdf
published_date: 2026-04-10
---

# Lightweight LLM Agent Memory with Small Language Models

**Authors**: Jiaquan Zhang, Chaoning Zhang, Shuxu Chen, Zhenzhen Huang, Pengcheng Zheng, Zhicheng Wang, Ping Guo, Fan Mo, Sung-Ho Bae, Jie Zou, Jiwei Wei, Yang Yang
**Published**: April 10, 2026
**Source**: https://arxiv.org/abs/2604.07798 · [HTML](https://arxiv.org/html/2604.07798v1)
**arXiv ID**: 2604.07798
**Categories**: cs.AI
**PDF**: [research/papers/pdfs/2604.07798.pdf](https://arxiv.org/abs/2604.07798) (16 pp, full text archived)

---

## Abstract (quoted)

> Although LLM agents can leverage tools for complex tasks, they still need memory to maintain cross-turn consistency and accumulate reusable information in long-horizon interactions. However, retrieval-based external memory systems incur low online overhead but suffer from unstable accuracy due to limited query construction and candidate filtering. In contrast, many systems use repeated large-model calls for online memory operations, improving accuracy but accumulating latency over long interactions. We propose LightMem, a lightweight memory system for better agent memory driven by Small Language Models (SLMs). LightMem modularizes memory retrieval, writing, and long-term consolidation, and separates online processing from offline consolidation to enable efficient memory invocation under bounded compute. We organize memory into short-term memory (STM) for immediate conversational context, mid-term memory (MTM) for reusable interaction summaries, and long-term memory (LTM) for consolidated knowledge, and uses user identifiers to support independent retrieval and incremental maintenance in multi-user settings. Online, LightMem operates under a fixed retrieval budget and selects memories via a two-stage procedure: vector-based coarse retrieval followed by semantic consistency re-ranking. Offline, it abstracts reusable interaction evidence and incrementally integrates it into LTM. Experiments show consistent gains across model scales, with an average F1 improvement of about 2.5 over A-MEM on LoCoMo, while achieving higher efficiency and low median latency (83 ms for retrieval and 581 ms end-to-end).

---

## 結構化摘要

### 核心貢獻
- 提出 LightMem：由 Small Language Models（SLM）驅動的輕量記憶系統，模組化 retrieval / writing / long-term consolidation，並分離 online 處理與 offline consolidation 以在有限算力下高效調用。
- 三層記憶組織：STM（即時對話脈絡）、MTM（可重用互動摘要）、LTM（整合後知識）；以 user identifier 支援多使用者獨立檢索與增量維護。
- Online 在固定 retrieval budget 下以兩階段選取記憶：vector coarse retrieval + semantic consistency re-ranking；Offline 抽象互動證據並增量整合進 LTM。

### 關鍵結果
- 跨模型尺度一致增益：LoCoMo 上相較 A-MEM 平均 F1 提升約 +2.5。
- 高效率與低延遲：median 檢索 83 ms、端到端 581 ms。

### 限制
- 文件未於 abstract 列明確 limitation；判斷弱點：SLM 抽取品質可能在高度專業領域退化；F1 +2.5 為單一 benchmark，跨域泛化未量化。

---

## Workspace 關聯（評估，非既成結論）

- 「online vs offline consolidation 分離」+「fixed retrieval budget」精準對應 context-management 的 token budget 與「右脈絡 > 多脈絡」NLAH 原則。
- 用 SLM 做記憶 read/write 對應 `core.md §PROPOSE 委派`（原 subagent-strategy.md）的 model-selection-grid：低風險抽取/檢索委派 Haiku 級模型，符合 `pilot`（tier=cost，原 `haiku-pilot`） 成本紀律。 〔v5.1：所引 workspace 細則已退役 → 見 `INDEX.md` §v5.1 規則退役對照〕
- 「兩階段 coarse retrieval + re-rank」對應「判斷 vs 決定」：確定性 vector 召回（決定）+ LLM 語意 re-rank（判斷）的清晰分層。

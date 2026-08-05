---
url: "https://arxiv.org/abs/2601.12904"
title: "From Prefix Cache to Fusion RAG Cache: Accelerating LLM Inference in Retrieval-Augmented Generation"
archived_date: 2026-06-24
arxiv_id: 2601.12904
authors: ["Jiahao Wang", "Weiyu Xie", "Mingxing Zhang", "Boxing Zhang", "Jianwei Dong", "Yuening Zhu", "Chen Lin", "Jinqi Tang", "Yaochen Han", "Zhiyuan Ai", "Xianglin Chen", "Yongwei Wu", "Congfeng Jiang"]
domains: [cs.CL]
html: "https://arxiv.org/html/2601.12904v1"
pdf_path: pdfs/2601.12904.pdf
published_date: 2026-01-19
---

# From Prefix Cache to Fusion RAG Cache: Accelerating LLM Inference in Retrieval-Augmented Generation

**Authors**: Jiahao Wang, Weiyu Xie, Mingxing Zhang, Boxing Zhang, Jianwei Dong, Yuening Zhu, Chen Lin, Jinqi Tang, Yaochen Han, Zhiyuan Ai, Xianglin Chen, Yongwei Wu, Congfeng Jiang
**Published**: January 19, 2026
**Source**: https://arxiv.org/abs/2601.12904 · [HTML](https://arxiv.org/html/2601.12904v1)
**arXiv ID**: 2601.12904
**Categories**: cs.CL
**PDF**: [research/papers/pdfs/2601.12904.pdf](https://arxiv.org/abs/2601.12904) (28 pp, full text archived)

---

## Abstract (quoted)

> Retrieval-Augmented Generation enhances Large Language Models by integrating external knowledge, which reduces hallucinations but increases prompt length. This increase leads to higher computational costs and longer Time to First Token (TTFT). To mitigate this issue, existing solutions aim to reuse the preprocessed KV cache of each retrieved chunk to accelerate RAG. However, the lack of cross-chunk contextual information leads to a significant drop in generation quality, leaving the potential benefits of KV cache reuse largely unfulfilled. The challenge lies in how to reuse the precomputed KV cache of chunks while preserving generation quality. We propose FusionRAG, a novel inference framework that optimizes both the preprocessing and reprocessing stages of RAG. In the offline preprocessing stage, we embed information from other related text chunks into each chunk, while in the online reprocessing stage, we recompute the KV cache for tokens that the model focuses on. As a result, we achieve a better trade-off between generation quality and efficiency. According to our experiments, FusionRAG significantly improves generation quality at the same recomputation ratio compared to previous state-of-the-art solutions. By recomputing fewer than 15% of the tokens, FusionRAG achieves up to 70% higher normalized F1 scores than baselines and reduces TTFT by 2.66x-9.39x compared to Full Attention.

---

## 結構化摘要

### 核心貢獻

- 提出 **FusionRAG**：RAG inference framework，分兩階段解決 KV cache 複用與生成品質的 trade-off 問題
- **Offline preprocessing**：將相關 chunk 的資訊嵌入（embed）到各 chunk，補全 cross-chunk contextual information
- **Online reprocessing**：選擇性重算模型「關注」token 的 KV cache（selective recomputation），以最小代價恢復品質
- 系統性分析了從 prefix cache 到 RAG-specific cache 的設計空間，提煉出 FusionRAG 架構

### 關鍵結果

- 重算 <15% token 的情況下，normalized F1 score 較 baseline 提升最高 **70%**
- TTFT 比 Full Attention 減少 **2.66x–9.39x**
- 相同 recomputation ratio 下，生成品質顯著優於先前 state-of-the-art 方案

### 限制

- 論文未列明確 limitation 章節
- 判斷弱點：offline preprocessing 需預先建立 chunk fusion index，增加儲存與 pipeline 複雜度；selective recomputation 的 token 選擇策略依賴 attention pattern，在 streaming 或 long-context 場景的穩健性有待驗證；實驗結果依特定 RAG benchmark，跨域泛化性未完整評估

---

## Workspace 關聯（評估，非既成結論）

- **Prompt caching / context-management**：FusionRAG 的 KV cache 複用策略與 `context-management.md` 的 Prompt Caching 核心原則高度對應——「Static First」前綴快取 + 動態 token 選擇性重算，正是 NLAH（Right context > more context）的推論層實踐；可作為理解快取設計取捨的參考文獻
- **Token budget / TTFT**：論文量化了 RAG prompt 長度增長對 TTFT 的成本衝擊，呼應 `context-management.md` token budget 管理的動機——長 RAG context 若不加管控，與 workspace 中 >70% 觸發 compact 的行為信號同屬「context 超支」問題
- **OBSERVE 階段 / 工具輸出截斷**：FusionRAG selective recomputation 的「只看模型真正 attend 的部分」與 core.md OBSERVE「工具輸出被截斷時不得假設截斷後為空」在設計哲學上互通——兩者都強調不能靜默丟棄低注意力區域的資訊
- ⚠️ 落地門檻：FusionRAG 需修改 inference engine KV cache 層，在本 workspace 的 prompt engineering / agent orchestration 層無法直接採用；概念層可借鑑，實作層需獨立工程投入


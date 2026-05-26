---
title: "HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models"
authors: "Bernal Jiménez Gutiérrez, Yiheng Shu, Yu Gu, Michihiro Yasunaga, Yu Su"
published: "2024-05-23"
source: "https://arxiv.org/abs/2405.14831"
venue: "NeurIPS 2024"
---

# HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models

**Authors**: Bernal Jiménez Gutiérrez, Yiheng Shu, Yu Gu, Michihiro Yasunaga, Yu Su  
**Affiliations**: The Ohio State University; Stanford University  
**Published**: May 23, 2024 (v1); revised January 14, 2025 (v3)  
**Venue**: NeurIPS 2024  
**Source**: https://arxiv.org/abs/2405.14831  
**arXiv ID**: 2405.14831  
**GitHub**: https://github.com/OSU-NLP-Group/HippoRAG  
**Categories**: cs.CL, cs.AI, cs.IR

---

## Abstract

We introduce HippoRAG, a novel retrieval framework inspired by the hippocampal indexing theory of human long-term memory. HippoRAG enables LLMs to efficiently and effectively integrate a large amount of new experiences after pre-training. It synergistically orchestrates LLMs, knowledge graphs, and the Personalized PageRank algorithm to mimic the roles of the neocortex and hippocampus in human memory. HippoRAG achieves up to 20% improvement over existing RAG methods on multi-hop question answering, while single-step retrieval performs comparably to iterative retrieval methods like IRCoT at 10-30× cheaper computation and 6-13× faster speed.

---

## 神經科學靈感：海馬體索引理論

### 人類記憶的神經科學基礎

人類長期記憶依賴兩個大腦區域的協作：

| 大腦區域 | 功能 | HippoRAG 對應 |
|---------|------|-------------|
| **新皮質（Neocortex）** | 儲存概念知識、語義關係 | LLM（預訓練知識）|
| **海馬體（Hippocampus）** | 索引 episode 記憶、建立關聯 | 知識圖譜索引層 |
| **嗅皮質（Entorhinal cortex）** | 連接海馬體和新皮質的橋樑 | 檢索接口層 |

**核心類比**：海馬體索引理論認為，海馬體不儲存記憶本身，而是建立**概念之間的關聯索引**，讓新皮質能快速定位相關記憶。

---

## HippoRAG 技術架構

### 索引階段（Offline Indexing）

```
文檔 → LLM 抽取三元組（主語, 謂語, 賓語）
                    ↓
              知識圖譜（KG）
              節點：實體（entity）
              邊：關係（relation）
                    ↓
        節點嵌入（sentence embedding）
                    ↓
        構建 Personalized PageRank 準備結構
```

### 檢索階段（Online Retrieval）

```
查詢（Query）
     ↓
LLM 從查詢中提取關鍵詞/實體
     ↓
嵌入相似度搜索 → 候選節點（seeds）
     ↓
Personalized PageRank（PPR）傳播
     ↓
相關節點分數排序
     ↓
返回對應的文檔段落（passages）
```

**PPR 的關鍵作用**：從多個 seed 節點出發，沿圖結構傳播，找到所有 seed 共同「到達」的節點——這正是多跳推理所需的**橋接概念（bridge concepts）**。

---

## 解決多跳問題

傳統 RAG 的多跳失敗案例：

```
問題：「Barack Obama 的出生地位於哪個大洋的西岸？」

需要：
1. Obama 出生地 → 夏威夷
2. 夏威夷位於 → 太平洋（Pacific Ocean）西岸

傳統 RAG：直接搜索「Obama 出生地+大洋」→ 找不到直接匹配

HippoRAG PPR：
- Seed: {Obama, 出生地, 大洋}
- PPR 從 Obama 節點沿「出生地→夏威夷→位於→太平洋」傳播
- 橋接節點「夏威夷」被高分命中
- 返回含夏威夷地理信息的段落
```

---

## 實驗結果

### Multi-hop QA 基準測試

| 方法 | MuSiQue | 2WikiMHQA | HotpotQA | 平均 |
|------|---------|-----------|---------|------|
| BM25 | 18.7 | 28.5 | 35.3 | 27.5 |
| Contriever | 27.4 | 38.1 | 45.6 | 37.0 |
| ColBERTv2 | 29.7 | 46.2 | 46.8 | 40.9 |
| **HippoRAG** | **39.4** | **62.5** | **52.1** | **51.3** |
| 改進 vs SOTA | +9.7 | +16.3 | +5.3 | **+10.4pp** |

**20% 平均提升**（跨所有多跳 QA 任務）。

### 效率比較（vs. IRCoT 迭代式檢索）

| 方法 | 準確率 | API 調用次數 | 速度 |
|------|--------|------------|------|
| IRCoT (迭代) | ~comparable | ~10 次/問題 | 慢 |
| HippoRAG（單步）| ~comparable | **1 次/問題** | **6-13× 更快** |

---

## 記憶機制的類比價值

### HippoRAG vs 傳統 RAG vs MemGPT

| 系統 | 索引結構 | 多跳能力 | 新知識整合 |
|------|---------|---------|----------|
| 傳統 RAG | 向量索引（獨立 chunks）| 弱（需迭代）| 直接添加 |
| MemGPT | 三層文字存儲 | 弱 | 直接添加 |
| **HippoRAG** | 知識圖譜 + PPR | **強（單步多跳）**| 增量添加 |
| A-MEM | Zettelkasten 連結 | 中 | 動態連結 |

**HippoRAG 的核心洞見**：關係網絡（relations）比語義相似度更能支持複雜推理。人類記憶的強大之處不在於儲存事實本身，而在於**事實之間的連接**。

---

## 後繼工作：HippoRAG v2

2025 年更新：
- 加入 proposition extraction（命題粒度，比 chunk 更細）
- 改進 PPR 的個性化機制
- 支持動態增量索引（不需要重建整個圖）

---

## 引用

```bibtex
@inproceedings{gutierrez2024hipporag,
  title={HippoRAG: Neurobiologically Inspired Long-Term Memory for Large Language Models},
  author={Gutiérrez, Bernal Jiménez and Shu, Yiheng and Gu, Yu and Yasunaga, Michihiro and Su, Yu},
  booktitle={Advances in Neural Information Processing Systems},
  volume={37},
  year={2024}
}
```

---

**關鍵詞**: 知識圖譜, 海馬體索引理論, Personalized PageRank, 多跳問答, 神經科學啟發, 長期記憶

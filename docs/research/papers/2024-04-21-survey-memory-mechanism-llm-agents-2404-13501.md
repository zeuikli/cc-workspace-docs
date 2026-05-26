---
title: "A Survey on the Memory Mechanism of Large Language Model based Agents"
authors: "Zeyu Zhang, Xiaohe Bo, Chen Ma, Rui Li, Xu Chen, Quanyu Dai, Jieming Zhu, Zhenhua Dong, Ji-Rong Wen"
published: "2024-04-21"
source: "https://arxiv.org/abs/2404.13501"
---

# A Survey on the Memory Mechanism of Large Language Model based Agents

**Authors**: Zeyu Zhang, Xiaohe Bo, Chen Ma, Rui Li, Xu Chen, Quanyu Dai, Jieming Zhu, Zhenhua Dong, Ji-Rong Wen  
**Affiliations**: Renmin University of China; Huawei Noah's Ark Lab  
**Published**: April 21, 2024  
**Source**: https://arxiv.org/abs/2404.13501  
**arXiv ID**: 2404.13501  
**GitHub**: https://github.com/nuster1128/LLM_Agent_Memory_Survey  
**Categories**: cs.AI, cs.CL

---

## Abstract

Memory mechanism is indispensable for enabling the self-evolving capability of LLM-based agents, which is essential for solving complex, long-term, and multi-step agent-environment interactions. We systematically review the memory design and evaluation approaches, present applications where memory plays a critical role, and identify limitations and future research directions. The survey establishes a comprehensive taxonomy of memory mechanisms across existing LLM-based agent literature.

---

## 調查範圍與方法

本調查覆蓋 **2022–2024** 年發表的 LLM 代理人記憶機制研究，共分析 **100+** 篇論文。

---

## 核心分類框架

### 第一維度：記憶形式（Memory Form）

| 形式 | 描述 | 代表系統 |
|------|------|---------|
| **文字記憶（Textual）** | 自然語言存儲記憶 | Generative Agents, MemGPT |
| **向量記憶（Vectorized）** | 嵌入向量索引 | RAG 類系統 |
| **結構化記憶（Structured）** | 數據庫、知識圖譜 | HippoRAG, ChatDB |
| **參數記憶（Parametric）** | 模型權重 | 微調方法 |
| **混合記憶（Hybrid）** | 多種形式結合 | MemoryOS, Mem0 |

### 第二維度：記憶操作（Memory Operations）

#### 1. 記憶寫入（Memory Writing）
```
觸發條件 → 選擇存儲內容 → 格式化 → 存入記憶庫
├── Always-write：每次交互後都寫入
├── Selective-write：滿足條件才寫入（SCM, ExpeL）
└── Delayed-write：批量寫入（ExpeL 訓練後提取）
```

#### 2. 記憶讀取（Memory Reading）
```
查詢形成 → 相似度計算 → Top-K 選擇 → 注入上下文
├── On-demand：按需檢索（MemGPT 中斷機制）
├── Proactive：主動預取（預測需要什麼記憶）
└── Contextual：基於當前狀態自動觸發
```

#### 3. 記憶整合（Memory Consolidation）
```
多個記憶條目 → LLM 重寫/摘要 → 更緊湊的表示
├── 即時整合：每次添加新記憶後整合
├── 定期整合：N 次後觸發
└── 按需整合：顯式觸發
```
> **⚠️ 警告**（來自 2605.12978）：此步驟是記憶退化的主要來源

#### 4. 記憶遺忘（Memory Forgetting）
```
├── 時間衰減（MemoryBank: Ebbinghaus）
├── 容量限制（超出後 LRU/LFU 淘汰）
├── 主動刪除（LLM 判斷哪些可刪）
└── 覆蓋式遺忘（整合時覆蓋舊記憶）
```

### 第三維度：記憶應用場景

| 場景 | 核心需求 | 代表系統 |
|------|---------|---------|
| 長對話 | 跨 turn 一致性 | MemoryBank, SiliconFriend |
| 多 session 助手 | 跨 session 持久化 | Mem0, MemGPT |
| 具身代理人 | 物理環境中的技能積累 | Voyager |
| 社會模擬 | 社會關係的記憶 | Generative Agents |
| 多代理系統 | 代理人間的共享記憶 | 研究前沿 |
| 個性化推薦 | 用戶偏好記憶 | MemoryOS, Mem0 |

---

## 評估方法分類

### 記憶質量評估
1. **召回準確率**（Recall Accuracy）：詢問記憶中存在的事實
2. **一致性**（Consistency）：跨對話的答案一致性
3. **相關性**（Relevance）：召回的記憶與當前查詢的相關程度

### 下游任務評估
1. **問答任務**（QA）：多跳 QA（HotpotQA, 2WikiMHQA）
2. **對話任務**（Dialogue）：LoCoMo, GVD 基準
3. **決策任務**：ALFWorld, Minecraft 等環境
4. **代碼任務**：HumanEval + 跨 session 代碼一致性

---

## 關鍵發現

### 發現 1：沒有統一最優架構
不同任務類型需要不同記憶策略：
- 短期推理 → Working Memory 即可
- 長對話 → Episodic + 向量檢索
- 複雜推理 → 結構化記憶（知識圖）
- 開放式探索 → 技能庫（Voyager 風格）

### 發現 2：整合是高風險操作
多個系統（包括 MemoryBank、A-MEM 等）在長時間運行後都觀察到性能退化，根源指向整合步驟的信息丟失。（2605.12978 後來系統性地驗證了這一觀察）

### 發現 3：評估標準不統一
缺乏跨系統可比較的標準基準，導致不同論文的結果難以直接比較。

---

## 未來方向

1. **記憶一致性驗證**：如何自動檢測整合後的記憶失真？
2. **記憶遺忘策略**：何時遺忘是有益的（防止過時記憶干擾）？
3. **多模態記憶**：整合視覺、音頻等非文字記憶
4. **多代理共享記憶**：如何設計代理人間的記憶同步協議？
5. **記憶的可解釋性**：如何讓代理人解釋「為什麼記住了這件事」？

---

## 引用

```bibtex
@article{zhang2024survey,
  title={A Survey on the Memory Mechanism of Large Language Model based Agents},
  author={Zhang, Zeyu and Bo, Xiaohe and Ma, Chen and Li, Rui and Chen, Xu and Dai, Quanyu and Zhu, Jieming and Dong, Zhenhua and Wen, Ji-Rong},
  journal={arXiv preprint arXiv:2404.13501},
  year={2024}
}
```

---

**關鍵詞**: 記憶機制調查, 記憶分類, 記憶操作, 遺忘機制, 整合失真, 多代理記憶

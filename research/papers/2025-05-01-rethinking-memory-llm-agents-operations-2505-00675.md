---
title: "Rethinking Memory in LLM based Agents: Representations, Operations, and Emerging Topics"
authors: "Yiming Du, Wenyu Huang, Danna Zheng, Zhaowei Wang, Sebastien Montella, Mirella Lapata, Kam-Fai Wong, Jeff Z. Pan"
published: "2025-05-01"
source: "https://arxiv.org/abs/2505.00675"
---

# Rethinking Memory in LLM based Agents: Representations, Operations, and Emerging Topics

**Authors**: Yiming Du, Wenyu Huang, Danna Zheng, Zhaowei Wang, Sebastien Montella, Mirella Lapata, Kam-Fai Wong, Jeff Z. Pan  
**Affiliations**: The University of Edinburgh; The Chinese University of Hong Kong; University of Oxford  
**Published**: May 1, 2025 (v1); revised December 24, 2025 (v3)  
**Source**: https://arxiv.org/abs/2505.00675  
**arXiv ID**: 2505.00675  
**DOI**: 10.48550/arXiv.2505.00675  
**Categories**: cs.AI, cs.CL

---

## Abstract

This paper presents a systematic framework for understanding memory in LLM-based agents. We distinguish between parametric memory (implicit in model weights) and contextual memory (explicit external data, structured or unstructured), while defining six core operations: Consolidation, Updating, Indexing, Forgetting, Retrieval, and Condensation. Our taxonomy organizes four key research areas (long-term memory, long-context memory, parametric modification, and multi-source memory) and provides comprehensive resources for future research.

---

## 記憶的二元框架

### Parametric Memory（參數記憶）
- **位置**：模型權重（θ）
- **內容**：預訓練知識（事實、語言模式、世界模型）
- **更新方式**：微調（fine-tuning）、知識編輯（ROME、MEMIT）
- **特點**：速度快（推理時免費），但更新成本高、可能干擾其他知識

### Contextual Memory（上下文記憶）
- **位置**：模型外部（向量 DB、文件系統、KV store）
- **內容**：對話歷史、文檔、用戶偏好、代理人軌跡
- **更新方式**：讀/寫操作
- **特點**：靈活、可解釋，但有檢索延遲和準確性問題

```
Parametric Memory     Contextual Memory
（模型知道的事）      （代理人記住的事）
      ↓                      ↓
  推理時隱式使用        顯式注入 Context Window
```

---

## 六大核心操作

### 操作 1：整合（Consolidation）
將多個記憶條目合并為更緊湊的表示。

```
[記憶 1] 用戶喜歡青椒炒肉
[記憶 2] 用戶喜歡麻婆豆腐
[記憶 3] 用戶討厭清淡食物
           ↓ Consolidation
[整合記憶] 用戶偏好川菜，喜歡重口味菜餚
```

**風險**（2605.12978）：整合過程不可逆，且可能引入 LLM 生成的偏見

### 操作 2：更新（Updating）
修改現有記憶以反映新資訊。

```
舊記憶：用戶在北京工作
新信息：用戶提到剛搬到上海
         ↓ Updating
新記憶：用戶現在在上海工作（已搬遷）
```

**挑戰**：如何確保更新的原子性（避免記憶中的自相矛盾）？

### 操作 3：索引（Indexing）
建立記憶的檢索結構。

- 向量索引（Dense）：語義相似度
- 稀疏索引（BM25）：關鍵詞匹配
- 圖索引（HippoRAG）：關係網絡
- 時間索引：最近優先

### 操作 4：遺忘（Forgetting）
刪除或降低記憶的可訪問性。

| 遺忘策略 | 觸發條件 | 示例系統 |
|---------|---------|---------|
| 時間衰減 | 時間流逝 | MemoryBank（Ebbinghaus）|
| 容量限制 | 超出最大容量 | FIFO / LRU |
| 重要性驅動 | 低用途記憶 | 調查論文建議 |
| 衝突驅動 | 與新信息矛盾 | Mem0 |

### 操作 5：檢索（Retrieval）
根據查詢找到相關記憶。

```
查詢形成（可能包含多步骤）
         ↓
相似度計算
         ↓
候選集排序
         ↓
Top-K 篩選
         ↓
注入 Context Window
```

### 操作 6：壓縮（Condensation）
在不失去關鍵信息的前提下縮短記憶表示。

**與整合的區別**：
- 整合：多個條目 → 一個條目（合并語義）
- 壓縮：一個長條目 → 一個短條目（保留語義）

---

## 四大研究主題

### 主題 1：長期記憶（Long-term Memory）
跨 session、跨天/月的記憶持久化。
- 核心挑戰：記憶管理效率、整合質量
- 代表系統：Mem0, MemGPT, MemoryOS

### 主題 2：長上下文記憶（Long-context Memory）
在超長 Context Window 內有效利用信息。
- 核心挑戰：Lost-in-the-Middle 問題、注意力稀釋
- 代表系統：δ-mem, 長 context 模型優化

### 主題 3：參數修改（Parametric Modification）
在不重新訓練的情況下更新模型知識。
- 核心挑戰：精確性 vs 副作用
- 代表方法：ROME, MEMIT, LoRA-based knowledge editing

### 主題 4：多源記憶（Multi-source Memory）
整合多個異構記憶來源。
- 核心挑戰：來源一致性、衝突解決
- 研究前沿：多代理記憶共享

---

## 對 Consolidation 問題的框架性貢獻

本論文明確將整合（Consolidation）定義為獨立操作，並指出：

1. **整合不可逆性**：一旦合并，原始條目信息可能永久丟失
2. **整合的隱含假設**：LLM 能準確理解並保留語義——這個假設被 2605.12978 系統性地質疑
3. **整合應作為顯式操作**：不應在記憶系統中自動觸發

---

## 引用

```bibtex
@article{du2025rethinking,
  title={Rethinking Memory in LLM based Agents: Representations, Operations, and Emerging Topics},
  author={Du, Yiming and Huang, Wenyu and Zheng, Danna and Wang, Zhaowei and Montella, Sebastien and Lapata, Mirella and Wong, Kam-Fai and Pan, Jeff Z},
  journal={arXiv preprint arXiv:2505.00675},
  year={2025}
}
```

---

**關鍵詞**: 記憶操作, 參數記憶, 上下文記憶, 整合, 遺忘, 索引, 壓縮, 記憶框架

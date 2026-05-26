---
title: "From Human Memory to AI Memory: A Survey on Memory Mechanisms in the Era of LLMs"
authors: "Yaxiong Wu, Sheng Liang, Chen Zhang, Yichao Wang, Yongyue Zhang, Huifeng Guo, Ruiming Tang, Yong Liu"
published: "2025-04-22"
source: "https://arxiv.org/abs/2504.15965"
---

# From Human Memory to AI Memory: A Survey on Memory Mechanisms in the Era of LLMs

**Authors**: Yaxiong Wu, Sheng Liang, Chen Zhang, Yichao Wang, Yongyue Zhang, Huifeng Guo, Ruiming Tang, Yong Liu  
**Affiliations**: Huawei Noah's Ark Lab; Nanyang Technological University  
**Published**: April 22, 2025  
**Source**: https://arxiv.org/abs/2504.15965  
**arXiv ID**: 2504.15965  
**Categories**: cs.AI, cs.CL

---

## Abstract

The paper establishes how "memory refers to the ability of an AI system to retain, recall, and use information" from previous interactions to enhance subsequent responses. We note a gap in existing literature regarding systematic analysis linking LLM memory to human memory cognition and how biological memory can inspire advanced AI systems. We present a three-dimensional framework with eight quadrants, organize existing memory-related work, and discuss open problems and future research directions.

---

## 從人類記憶科學到 AI 記憶設計

### 人類記憶的心理學分類

| 記憶類型 | 描述 | AI 類比 |
|---------|------|---------|
| **感覺記憶（Sensory）** | 極短暫（<1 秒），感官輸入緩衝 | 輸入緩衝、token 流 |
| **工作記憶（Working）** | 短期、有限容量（7±2 項目） | Context Window |
| **情節記憶（Episodic）** | 具體事件、時間-地點編碼 | 對話歷史、軌跡記錄 |
| **語義記憶（Semantic）** | 一般知識、事實、概念 | 預訓練知識、知識庫 |
| **程序記憶（Procedural）** | 技能、習慣（如何做） | 技能庫（Voyager）、微調權重 |

### 記憶鞏固（Memory Consolidation）的神經科學

人類記憶鞏固過程（與 AI 整合問題的類比）：

```
海馬體短期記憶
    ↓ 睡眠時重放（replay）
    ↓ 新皮質長期記憶
    ↓ 語義化（去情境化）

問題：LLM 的「整合」缺少人類睡眠重放的選擇性——
      人類只重放「重要」事件；LLM 可能整合所有事件
```

---

## 三維度八象限分類框架

### 維度定義

```
維度 1：Object（記憶的對象是什麼）
  └── 個人（Personal）vs 世界（World）

維度 2：Form（記憶的形式）
  └── 顯式（Explicit）vs 隱式（Implicit）

維度 3：Time（時間範圍）
  └── 短期（Short-term）vs 長期（Long-term）
```

### 八象限分類

| 象限 | Object | Form | Time | 示例 |
|------|--------|------|------|------|
| Q1 | Personal | Explicit | Short | 當前對話中的用戶姓名 |
| Q2 | Personal | Explicit | Long | 跨 session 的用戶偏好 |
| Q3 | Personal | Implicit | Short | 當前對話語氣感知 |
| Q4 | Personal | Implicit | Long | 長期個性化模型（微調）|
| Q5 | World | Explicit | Short | RAG 臨時載入的文檔 |
| Q6 | World | Explicit | Long | 持久知識庫（向量 DB）|
| Q7 | World | Implicit | Short | 當前推理的上下文假設 |
| Q8 | World | Implicit | Long | 預訓練的世界知識 |

---

## 記憶機制的演化路徑

### 第一代：純 Context Window
- 所有記憶在 Context Window 內
- 限制：token 預算固定，無跨 session 持久化

### 第二代：外部向量儲存（RAG 時代）
- 向量資料庫儲存長期知識
- 語義搜索按需注入
- 限制：孤立的 chunk，缺乏關係結構

### 第三代：結構化代理記憶
- 分層儲存（工作/情節/語義）
- 顯式記憶操作（讀/寫/整合/遺忘）
- 代表：MemGPT, MemoryOS, A-MEM

### 第四代（進行中）：學習型記憶管理
- LLM 學習**何時**整合、**什麼**遺忘
- 記憶管理本身成為學習目標
- 目標：解決 2605.12978 揭示的整合退化問題

---

## 人類記憶啟發的設計原則

### 原則 1：選擇性鞏固（Selective Consolidation）
人類大腦在睡眠中只重放情感顯著或有用的記憶，不是所有事件。

**AI 設計啟示**：整合應由重要性/用途篩選，而非自動觸發。

### 原則 2：情境依賴性回憶（Context-dependent Retrieval）
人類更容易在相同情境下回憶記憶（state-dependent memory）。

**AI 設計啟示**：檢索不只依賴語義相似度，還要考慮當前任務情境。

### 原則 3：記憶的可塑性（Memory Plasticity）
人類記憶在每次回憶時都會輕微改變（reconsolidation）。

**AI 設計啟示（2605.12978 的警告）**：LLM 的整合可能類似過度 reconsolidation——每次重寫都引入失真，最終面目全非。

### 原則 4：遺忘的功能性（Functional Forgetting）
適度遺忘有益於認知——過多細節反而降低泛化能力（認知科學的 forgetting curve）。

**AI 設計啟示**：記憶系統不應無限積累，應有策略性遺忘機制。

---

## 開放問題

1. **整合失真的根本原因**：LLM 重寫記憶的數學模型是什麼？失真如何積累？
2. **個性化 vs 泛化的平衡**：過度記憶個人偏好可能導致過擬合
3. **跨模態記憶**：文字記憶如何與視覺、語音記憶整合？
4. **記憶的倫理問題**：長期記憶涉及個人隱私，如何安全管理？
5. **記憶基準的標準化**：缺乏覆蓋多場景的統一評估套件

---

## 引用

```bibtex
@article{wu2025human,
  title={From Human Memory to AI Memory: A Survey on Memory Mechanisms in the Era of LLMs},
  author={Wu, Yaxiong and Liang, Sheng and Zhang, Chen and Wang, Yichao and Zhang, Yongyue and Guo, Huifeng and Tang, Ruiming and Liu, Yong},
  journal={arXiv preprint arXiv:2504.15965},
  year={2025}
}
```

---

**關鍵詞**: 記憶科學, 神經科學啟發, 三維分類, 情節記憶, 語義記憶, 記憶鞏固, 遺忘曲線

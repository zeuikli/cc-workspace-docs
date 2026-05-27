---
title: "SCM: Enhancing Large Language Model with Self-Controlled Memory Framework"
authors: Bing Wang, Xinnian Liang, Jian Yang, Hui Huang, Shuangzhi Wu, Peihao Wu, Lu Lu, Zejun Ma, Zhoujun Li
published: 2023-04-26
source: "https://arxiv.org/abs/2304.13343"
venue: DASFAA 2025
---

# SCM: Enhancing Large Language Model with Self-Controlled Memory Framework

**Authors**: Bing Wang, Xinnian Liang, Jian Yang, Hui Huang, Shuangzhi Wu, Peihao Wu, Lu Lu, Zejun Ma, Zhoujun Li  
**Affiliations**: Beihang University; Tencent AI Lab  
**Published**: April 26, 2023 (v1); revised March 18, 2025 (v4)  
**Venue**: DASFAA 2025 (main conference)  
**Source**: https://arxiv.org/abs/2304.13343  
**arXiv ID**: 2304.13343  
**Categories**: cs.CL, cs.AI

---

## Abstract

Large Language Models (LLMs) are constrained by their inability to process lengthy inputs, resulting in the loss of critical historical information in long-context conversations. We propose the Self-Controlled Memory (SCM) framework to enhance LLMs with the capability to maintain long-term memory and retrieve relevant information in real time. The SCM framework comprises three key components: an LLM-based agent backbone, a memory stream, and a memory controller. The memory controller manages the storage and retrieval of information, enabling LLMs to process lengthy inputs across multiple sessions. The SCM framework is plug-and-play, compatible with any instruction-following LLM without model modification or fine-tuning. We evaluate SCM on long-term dialogue, book summarization, and meeting summarization tasks, demonstrating improved retrieval recall and more informative response generation compared to baseline methods.

---

## 核心問題

LLM 的固定上下文窗口導致長對話中的歷史資訊丟失——這是所有基於 LLM 的助手面臨的根本限制。**SCM 的目標**：無需修改模型本身，透過外部記憶控制框架解決此問題。

---

## 系統架構

### 三核心組件

```
┌─────────────────────────────────────────────────────┐
│                 SCM Framework                        │
│                                                      │
│  ┌──────────────────┐    ┌───────────────────────┐  │
│  │  LLM Agent       │◄──►│  Memory Controller    │  │
│  │  Backbone        │    │  (何時存/取/刪除記憶)  │  │
│  └──────────────────┘    └───────────────────────┘  │
│             ▲                        │               │
│             │                        ▼               │
│  ┌──────────────────────────────────────────────┐   │
│  │           Memory Stream                       │   │
│  │  (長期儲存：對話歷史、摘要、關鍵事實)          │   │
│  └──────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────┘
```

**1. LLM Agent Backbone**
- 任何 instruction-following LLM（ChatGPT、ChatGLM 等）
- 無需微調，即插即用

**2. Memory Stream**
- 持久化儲存歷史對話、摘要、關鍵資訊
- 支援多 session 跨越連續對話
- 結構化條目包含：內容、時間戳、重要性

**3. Memory Controller**
- 核心智能：決定**何時**儲存、**什麼**儲存、**何時**讀取
- 雙緩衝設計：短期緩衝區（當前對話）+ 長期記憶庫
- 選擇性召回：基於查詢相關性篩選，避免雜訊注入

---

## 記憶控制策略

### 儲存決策
- 每 N 輪對話觸發一次摘要生成，存入長期記憶
- LLM 判斷哪些資訊「值得記住」（重要性分類）
- 冗餘去除：相似條目合併

### 讀取決策
- 新查詢到來時，先搜索記憶流中的相關條目
- 相關記憶注入到當前 LLM 上下文
- 門控機制：低相關性記憶不注入（避免干擾）

### 刪除決策
- 基於時間衰減（舊記憶權重遞減）
- 基於覆蓋率（被更新摘要覆蓋的細節可刪）

---

## 評估實驗

### 任務一：長期對話（Long-term Dialogue）
- 多輪跨 session 對話，評估代理人的事實一致性
- SCM 在正確回憶用戶偏好、歷史事件等方面優於基線

### 任務二：書本摘要（Book Summarization）
- 處理超出上下文窗口的長篇書籍
- SCM 分段處理並維護跨段落的連貫摘要

### 任務三：會議摘要（Meeting Summarization）
- 長會議記錄的增量摘要生成
- 對比基線：滑動窗口法、分段法

**核心指標改進**：
- Retrieval Recall：提高記憶召回準確率
- Response Informativeness：生成回應包含更多相關細節

---

## 與其他記憶系統的比較

| 系統 | 架構方式 | 需要微調 | 處理超長輸入 |
|------|---------|---------|------------|
| **SCM** | 外部記憶控制框架 | ❌ 不需要 | ✅ 支援 |
| MemGPT | 虛擬 context 管理（OS 類比） | ❌ | ✅ |
| MemoryBank | Ebbinghaus 遺忘曲線記憶更新 | ❌ | ✅ |
| 直接長 context | 延長 context window | 可選 | 受限 |
| 微調方法 | 模型參數更新 | ✅ 需要 | 受限 |

**SCM 優勢**：即插即用，無需修改模型，適合在生產環境中快速部署到任何 LLM。

---

## 對 Memory Consolidation 研究的意義

SCM 的記憶控制器體現了**顯式門控**（explicit gating）的核心思想：

1. **不是所有資訊都存**：重要性篩選避免低質量記憶污染
2. **不是所有記憶都召回**：相關性門控防止噪聲注入
3. **記憶是系統責任，非模型責任**：LLM 的上下文理解能力 + 框架的記憶管理能力

這與 **2605.12978**（Useful Memories Become Faulty）的建議直接對應：
- SCM 的「選擇性召回」= 顯式門控（explicit gating）
- SCM 的「不在每次互動後自動整合」= 避免過度整合
- SCM 的雙緩衝 = 保留 episodic（短期緩衝）的同時維護 consolidated（長期記憶）

---

## 引用

```bibtex
@article{wang2023scm,
  title={SCM: Enhancing Large Language Model with Self-Controlled Memory Framework},
  author={Wang, Bing and Liang, Xinnian and Yang, Jian and Huang, Hui and Wu, Shuangzhi and Wu, Peihao and Lu, Lu and Ma, Zejun and Li, Zhoujun},
  journal={arXiv preprint arXiv:2304.13343},
  year={2023}
}
```

---

**關鍵詞**: 自控記憶, 記憶框架, 長對話, 即插即用, 記憶控制器, 選擇性召回

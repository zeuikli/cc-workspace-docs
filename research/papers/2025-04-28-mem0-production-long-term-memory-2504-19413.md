---
title: "Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory"
authors: "Prateek Chhikara, Dev Khant, Saket Aryan, Taranjeet Singh, Deshraj Yadav"
published: "2025-04-28"
source: "https://arxiv.org/abs/2504.19413"
---

# Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory

**Authors**: Prateek Chhikara, Dev Khant, Saket Aryan, Taranjeet Singh, Deshraj Yadav  
**Affiliations**: Mem0 (YC-backed startup)  
**Published**: April 28, 2025  
**Source**: https://arxiv.org/abs/2504.19413  
**arXiv ID**: 2504.19413  
**GitHub**: https://github.com/mem0ai/mem0  
**Categories**: cs.AI, cs.CL

---

## Abstract

We introduce Mem0, a scalable memory layer for AI applications that addresses the limitations of fixed context windows in LLMs during extended, multi-session interactions. Mem0 provides a base system for dynamically extracting and consolidating salient conversational information, alongside a graph-based variant that additionally captures relational structures between entities. We evaluate both systems on the LOCOMO benchmark, comparing against six baseline categories including memory-augmented systems, RAG implementations, and full-context approaches. Mem0 achieves 26% relative improvement over OpenAI's memory-augmented approach in the LLM-as-a-Judge metric, while reducing p95 latency by 91% and token costs by over 90% compared to full-context methods. The graph variant provides approximately 2% additional improvement over the base system.

---

## 定位：生產就緒的記憶基礎設施

Mem0 不是研究論文中的實驗系統，而是面向**生產環境**的記憶層：

```
應用程序
    ↓ 調用 Mem0 API
Mem0 記憶層
    ├── 自動提取記憶
    ├── 智能去重/合並
    ├── 跨 session 持久化
    └── 相關記憶檢索
    ↓ 記憶注入
LLM（任何提供商）
```

---

## 技術架構

### Base System（基礎系統）

**記憶提取**：
```python
# 每次對話後自動提取
conversation = [
    {"role": "user", "content": "I prefer Python over JavaScript"},
    {"role": "assistant", "content": "Got it! I'll use Python in my examples"}
]

mem0.add(conversation, user_id="user_123")
# → 自動提取：{"content": "Prefers Python over JavaScript", 
#               "user_id": "user_123", "created_at": ...}
```

**核心操作**：
1. **提取（Extract）**：從對話中識別值得記住的資訊
2. **去重（Deduplicate）**：檢測與現有記憶的重疊，避免冗余
3. **整合（Consolidate）**：將相關記憶合并（如「喜歡 Python」+ 「不喜歡 JS」→「偏好 Python 而非 JS」）
4. **檢索（Retrieve）**：根據查詢返回相關記憶

### Graph Memory（圖記憶系統）

增加實體關係圖層：

```
節點：實體（人物、地點、概念）
邊：關係（"works at", "prefers", "lives in"）

示例：
user_123 → works_at → TechCorp
user_123 → prefers → Python
user_123 → lives_in → San Francisco
TechCorp → located_in → San Francisco
```

圖記憶讓 Mem0 能回答：「用戶住在他工作的公司附近嗎？」（需要跨邊推理）

---

## LOCOMO 基準測試結果

### 準確率比較（LLM-as-a-Judge）

| 系統 | 單跳 | 多跳 | 時間 | 開放域 | 平均 |
|------|------|------|------|--------|------|
| Full Context | 最高 | 最高 | 最高 | 最高 | 基準線 |
| OpenAI Memory | - | - | - | - | 基準線 |
| **Mem0 Base** | 高 | 高 | 高 | 高 | **+26% vs OpenAI** |
| **Mem0 Graph** | 最高 | 最高 | 最高 | 最高 | **+28% vs OpenAI** |
| BM25 RAG | 低 | 低 | 低 | 低 | 差 |

### 效率比較

| 指標 | Full Context | Mem0 |
|------|-------------|------|
| p95 延遲 | 高 | **-91%** |
| Token 成本 | 基準 | **-90%** |
| 準確率 | 最高 | 接近（-5-10pp）|

**結論**：在保持接近 Full Context 準確率的同時，將成本和延遲削減 90%+。

---

## 記憶整合的實際挑戰

Mem0 論文中揭示的生產環境挑戰：

### 整合失敗案例
```
記憶 1：用戶說「我不喜歡辛辣食物」（2 個月前）
記憶 2：用戶說「我最近開始嘗試泰式食物」（昨天）
記憶 3：用戶說「那道泰式咖喱真不錯」（昨天）

整合問題：
- 天真整合：「用戶不喜歡辛辣食物」（覆蓋了新近的更新）
- 正確整合：「用戶以前不喜歡辛辣，但最近開始喜歡泰式食物（含辛辣成分）」
```

**Mem0 的解法**：
- 保留衝突記憶並標記衝突（不自動解決）
- 時間戳決定「最近優先」原則
- LLM 在整合時被要求「保留所有證據」（episodic-first）

---

## 與 2605.12978 的關係

Mem0 的生產實踐在某種程度上**驗證了** 2605.12978 的警告：

| 2605.12978 警告 | Mem0 實際觀察 |
|----------------|-------------|
| 整合會引入失真 | 生產中發現整合衝突記憶困難 |
| 整合後準確率下降 | 大量整合後召回準確率降低 |
| Episodic 作為第一手證據 | 保留原始對話作為 ground truth |
| 顯式門控整合 | 整合不是自動的，需要 LLM 判斷 |

---

## 引用

```bibtex
@article{chhikara2025mem0,
  title={Mem0: Building Production-Ready AI Agents with Scalable Long-Term Memory},
  author={Chhikara, Prateek and Khant, Dev and Aryan, Saket and Singh, Taranjeet and Yadav, Deshraj},
  journal={arXiv preprint arXiv:2504.19413},
  year={2025}
}
```

---

**關鍵詞**: 生產就緒, 記憶層, 圖記憶, 個性化, 延遲優化, Token 效率, 企業級

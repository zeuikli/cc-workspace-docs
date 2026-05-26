---
title: "ExpeL: LLM Agents Are Experiential Learners"
authors: "Andrew Zhao, Daniel Huang, Quentin Xu, Matthieu Lin, Yong-Jin Liu, Gao Huang"
published: "2023-08-20"
source: "https://arxiv.org/abs/2308.10144"
venue: "AAAI 2024"
---

# ExpeL: LLM Agents Are Experiential Learners

**Authors**: Andrew Zhao, Daniel Huang, Quentin Xu, Matthieu Lin, Yong-Jin Liu, Gao Huang  
**Affiliations**: Tsinghua University  
**Published**: August 20, 2023 (v1); revised December 20, 2024  
**Venue**: AAAI 2024 (38th Annual AAAI Conference on AI)  
**Source**: https://arxiv.org/abs/2308.10144  
**arXiv ID**: 2308.10144  
**Categories**: cs.AI, cs.LG

---

## Abstract

LLM agents are increasingly deployed for decision-making tasks that require learning from experience. However, fine-tuning proprietary models is often infeasible or prohibitively expensive. ExpeL introduces an approach where agents autonomously gather experiences and extract knowledge using natural language from training tasks. During inference, agents retrieve accumulated insights to inform decisions. Results demonstrate consistent performance improvements as experience accumulates, with exploration of emerging capabilities and transfer learning potential across task domains.

---

## 核心思想：從經驗中提取規則，無需參數更新

ExpeL 的核心問題：**如何讓 LLM 代理人「學習」，卻不更新模型參數？**

答案：從過去的成功與失敗軌跡中提取**自然語言洞見（insights）**，建立一個經驗知識庫。

```
訓練階段：
任務 1 → 嘗試（成功/失敗）→ 提取洞見 → 知識庫
任務 2 → 嘗試 → 提取洞見 → 知識庫（持續積累）
...

推理階段：
新任務 → 從知識庫檢索相關洞見 → 注入上下文 → 決策
```

---

## 系統架構

### Phase 1: 經驗收集（Experience Collection）

```python
# 偽代碼：ExpeL 訓練循環
experience_pool = []
for task in training_tasks:
    for attempt in range(max_attempts):
        trajectory = agent.run(task, context=experience_pool)
        outcome = evaluate(trajectory)
        experience_pool.append({
            "task": task,
            "trajectory": trajectory, 
            "outcome": outcome,
            "attempt": attempt
        })
```

收集的軌跡包含：
- 完整的行動序列（含失敗嘗試）
- 環境反饋
- 最終結果

### Phase 2: 洞見提取（Insight Extraction）

從成功/失敗對比中提取規則：

```
[失敗軌跡]
步驟3：搜索 "Python list comprehension tutorial"
錯誤：資訊過於基礎，未解決問題

[成功軌跡]  
步驟3：搜索 "Python filter() function negative index"
成功：找到精確解法

→ 提取洞見：
"When solving Python coding problems, search for specific function names 
rather than general tutorials. Include the exact error or constraint 
in the search query."
```

### Phase 3: 推理時洞見召回（Inference-time Retrieval）

- 向量相似度匹配：新任務 vs 過去任務描述
- 按相關性排序，選取 Top-K 洞見注入上下文
- Few-shot 方式提供成功軌跡示例

---

## 關鍵實驗

### HotpotQA（多跳問答）
- 隨著收集的經驗增加，任務成功率持續提升
- 第 1 輪：基線準確率
- 第 10 輪：提升 ~15%
- 第 50 輪：提升 ~25%（但邊際效應遞減）

### ALFWorld（文字遊戲環境）
- ExpeL 在 6 種任務類型上均優於 ReAct 和 Reflexion
- 特別在需要多步規劃的任務上優勢明顯

### 跨任務遷移（Transfer Learning）
- 在任務 A 積累的洞見能部分遷移到任務 B（前提：任務類型相似）
- 這展示了 ExpeL 洞見庫的泛化潛力

---

## 與 Reflexion 的比較

| 特性 | Reflexion | ExpeL |
|------|-----------|-------|
| 學習來源 | 當前任務的錯誤 | 跨任務積累的經驗 |
| 記憶範圍 | 單任務 session | 跨任務持久化 |
| 提取時機 | 每次失敗後反思 | 訓練後批量提取 |
| 泛化能力 | 任務特定 | 跨任務（同類型）|
| 記憶形式 | 語言反思 | 結構化洞見 |

---

## 對記憶整合研究的貢獻

ExpeL 提供了**控制整合時機**的實踐方案：

1. **批量整合（offline consolidation）**：不在每次互動後整合，而是在訓練後統一提取洞見
2. **對比學習**：通過成功/失敗對比提取洞見，比單純從成功中提取更精確
3. **洞見驗證**：提取的洞見在多個任務中被驗證有效後才進入知識庫

這與 **2605.12978** 的建議一致：不要在每次互動後自動觸發整合（fire after every interaction），而應**顯式門控（explicit gating）**整合時機。

---

## 引用

```bibtex
@inproceedings{zhao2024expel,
  title={ExpeL: LLM Agents Are Experiential Learners},
  author={Zhao, Andrew and Huang, Daniel and Xu, Quentin and Lin, Matthieu and Liu, Yong-Jin and Huang, Gao},
  booktitle={Proceedings of AAAI 2024},
  year={2024}
}
```

---

**關鍵詞**: 經驗學習, 洞見提取, 無參數更新, 跨任務遷移, 知識庫, 決策規劃

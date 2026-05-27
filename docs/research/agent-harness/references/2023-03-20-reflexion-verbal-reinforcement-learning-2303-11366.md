---
title: "Reflexion: Language Agents with Verbal Reinforcement Learning"
authors: "Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao"
published: 2023-03-20
source: "https://arxiv.org/abs/2303.11366"
venue: NeurIPS 2023
---

# Reflexion: Language Agents with Verbal Reinforcement Learning

**Authors**: Noah Shinn, Federico Cassano, Edward Berman, Ashwin Gopinath, Karthik Narasimhan, Shunyu Yao  
**Affiliations**: Northeastern University; MIT; Princeton University  
**Published**: March 20, 2023 (v1); revised October 10, 2023 (v4)  
**Venue**: NeurIPS 2023  
**Source**: https://arxiv.org/abs/2303.11366  
**arXiv ID**: 2303.11366  
**GitHub**: https://github.com/noahshinn/reflexion  
**Categories**: cs.AI, cs.LG

---

## Abstract

Large language models are increasingly being used as agents that make decisions in complex tasks. However, learning from mistakes remains a challenge without gradient-based parameter updates. We propose Reflexion, a framework to reinforce language agents not by updating weights, but instead through linguistic feedback stored in an episodic memory buffer. Agents verbally reflect on task feedback signals, then maintain their own reflective text in an episodic memory buffer to induce better decision-making in subsequent trials. Reflexion achieves 91% pass@1 accuracy on HumanEval coding benchmark (surpassing GPT-4's 80%), 97% on TAL-SCQ5K, and strong performance across diverse sequential decision-making, coding, and language reasoning benchmarks.

---

## 核心問題：如何讓 LLM 代理人從錯誤中學習？

傳統強化學習需要**梯度更新**（參數改變）才能讓模型學習。但：
1. 商業 LLM（GPT-4 等）的參數不可更新
2. 微調成本高且可能破壞泛化能力

**Reflexion 的解法**：用**語言反思（verbal reflection）**替代梯度更新。

```
嘗試 1：失敗 → 語言反思：「我沒有考慮到邊界情況」
               → 存入 episodic memory
嘗試 2（帶記憶）→ 更好的決策 → 成功
```

---

## 系統架構

### 三個組件

**1. Actor（行動者）**
- 基礎 LLM（GPT-4、Claude 等）
- 執行具體任務
- 使用 ReAct 或其他框架

**2. Evaluator（評估器）**
- 判斷行動的結果品質
- 可以是：明確的測試用例、人類反饋、LLM 自評
- 返回：success / failure / partial_success + 原因

**3. Self-Reflection（自我反思）**
- 輸入：失敗的軌跡 + 評估器的反饋
- LLM 生成反思文字：
  ```
  "In this attempt, I failed because I used recursion without 
  considering the stack overflow for large inputs. Next time, 
  I should use iterative approach with explicit stack."
  ```
- 存入 **episodic memory buffer**

### 決策循環

```
for trial in range(max_trials):
    # 從記憶中加載過去的反思
    reflections = memory.retrieve_relevant()
    
    # 執行任務（帶反思上下文）
    outcome = actor.run(task, context=reflections)
    
    if outcome.success:
        break
    
    # 生成反思並存入記憶
    reflection = self_reflect(outcome)
    memory.add(reflection)
```

---

## Episodic Memory 設計細節

### 記憶條目結構
```python
{
  "attempt": 3,
  "task_type": "coding",
  "failure_mode": "edge case: empty input",
  "reflection": "Always check for null/empty inputs first. 
                 The function should return [] for empty list, 
                 not throw IndexError.",
  "key_lesson": "defensive programming for edge cases"
}
```

### 記憶限制
- Context window 限制了可攜帶的反思數量
- 通常保留最近 3-5 條反思（sliding window）
- **問題**：早期的重要反思可能被截斷

---

## 實驗結果

### 代碼生成（HumanEval）

| 方法 | Pass@1 |
|------|--------|
| GPT-4（無反思）| 80.1% |
| GPT-3.5（無反思）| 65.8% |
| **Reflexion + GPT-3.5** | **91.0%** |

Reflexion + GPT-3.5 **超越**了 GPT-4 基線！

### 序列決策（ALFWorld 文字遊戲）

| 方法 | 成功率 |
|------|--------|
| ReAct (GPT-3) | 53% |
| ReAct + CoT | 55% |
| **Reflexion** | **97%** |

### 多步推理（HotpotQA）

| 方法 | 準確率 |
|------|--------|
| CoT + GPT-3.5 | 73% |
| **Reflexion + GPT-3.5** | **80%** |

---

## 與記憶整合研究的關係

### Reflexion 的記憶類型：純 Episodic

Reflexion 的 episodic memory buffer 是**最接近原始 episodic 記憶**的設計：
- 每條反思直接源自具體失敗軌跡
- **不進行跨 episode 的整合**（每條反思相互獨立）
- 以追加（append）方式更新，不修改現有記憶

### 2605.12978 的視角

Reflexion 的成功提供了重要的對照點：
- Reflexion 使用 **episodic-only** 記憶（只保留反思，不整合）
- 在 HumanEval 達到 91% 的高準確率
- 這支持了 **2605.12978** 的假設：保留原始 episodic 記錄比整合後的摘要更有效

**關鍵問題**：Reflexion 的反思本身是否是一種「安全的整合」（因為它只從單次失敗提取，不跨 episode 合並）？這個問題尚未有系統性研究。

---

## 局限性

1. **Context Window 上限**：反思積累到一定數量後無法繼續增加
2. **反思質量依賴 LLM 能力**：弱模型生成的反思可能無效
3. **無法跨任務遷移**：每個新任務都從零開始積累反思
4. **反思可能不準確**：LLM 可能生成錯誤的失敗原因分析

---

## 引用

```bibtex
@inproceedings{shinn2023reflexion,
  title={Reflexion: Language Agents with Verbal Reinforcement Learning},
  author={Shinn, Noah and Cassano, Federico and Berman, Edward and Gopinath, Ashwin and Narasimhan, Karthik and Yao, Shunyu},
  booktitle={Advances in Neural Information Processing Systems},
  volume={36},
  year={2023}
}
```

---

**關鍵詞**: 語言反思, 情節記憶, 試錯學習, 無梯度學習, 代碼生成, 序列決策

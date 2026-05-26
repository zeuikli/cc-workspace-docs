---
url: "https://arxiv.org/abs/2210.03629"
title: "ReAct: Synergizing Reasoning and Acting in Language Models"
date: 2022-10-06
arxiv_id: 2210.03629
authors: "Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao"
referenced_by: warmwater.dev
source: arxiv
---

## Abstract

While large language models (LLMs) have demonstrated impressive capabilities across tasks in language understanding and interactive decision making, their abilities for reasoning (e.g. chain-of-thought prompting) and acting (e.g. action plan generation) have primarily been studied as separate topics. In this paper, we explore the use of LLMs to generate both reasoning traces and task-specific actions in an interleaved manner, allowing for greater synergy between the two: reasoning traces help the model induce, track, and update action plans as well as handle exceptions, while actions allow it to interface with external sources, such as knowledge bases or environments, to gather additional information. We apply our approach, named ReAct, to a diverse set of language and decision making tasks and demonstrate its effectiveness over state-of-the-art baselines, as well as improved human interpretability and trustworthiness over methods without reasoning or acting components. Concretely, on question answering (HotpotQA) and fact verification (Fever), ReAct overcomes issues of hallucination and error propagation prevalent in chain-of-thought reasoning by interacting with a simple Wikipedia API, and generates human-like task-solving trajectories that are more interpretable than baselines without reasoning traces. On two interactive decision making benchmarks (ALFWorld and WebShop), ReAct outperforms imitation and reinforcement learning methods by an absolute success rate of 34% and 10% respectively, while being prompted with only one or two in-context examples.

## 主要貢獻

- **ReAct 框架**：讓 LLM 以交錯方式（interleaved manner）同時生成推理軌跡（reasoning traces）和任務特定行動（actions），實現推理與行動的協同增效。
- **推理輔助行動**：推理軌跡幫助模型推導、追蹤、更新行動計畫，並處理例外情況；行動讓模型與外部知識庫或環境互動以獲取額外資訊。
- **克服幻覺問題**：在 HotpotQA 和 Fever 上，ReAct 透過與 Wikipedia API 互動，克服了 chain-of-thought 推理中常見的幻覺和錯誤傳播問題。
- **互動式決策表現**：在 ALFWorld 和 WebShop 兩個互動決策 benchmark 上，ReAct 分別以 34% 和 10% 的絕對成功率優於模仿學習和強化學習方法，且僅使用一至二個 in-context 範例。
- **可解釋性與可信賴性**：生成類似人類的任務解決軌跡，相較於無推理追蹤的方法，具備更高的人類可解釋性和可信賴性。
- **影響力**：ReAct 成為後續 agent 框架（LangChain、AutoGPT 等）的基礎設計模式，是 LLM agent 領域最具影響力的論文之一。

## 論文全文

> HTML 全文暫不可用（arxiv HTML 轉換尚未完成）。以下為完整摘要頁面資訊及擴充內容。

**Title**: ReAct: Synergizing Reasoning and Acting in Language Models
**Authors**: Shunyu Yao, Jeffrey Zhao, Dian Yu, Nan Du, Izhak Shafran, Karthik Narasimhan, Yuan Cao
**arXiv ID**: 2210.03629
**Published**: 2022-10-06
**Venue**: ICLR 2023
**URL**: https://arxiv.org/abs/2210.03629
**Project site**: https://react-lm.github.io/

### Full Abstract

While large language models (LLMs) have demonstrated impressive capabilities across tasks in language understanding and interactive decision making, their abilities for reasoning (e.g. chain-of-thought prompting) and acting (e.g. action plan generation) have primarily been studied as separate topics. In this paper, we explore the use of LLMs to generate both reasoning traces and task-specific actions in an interleaved manner, allowing for greater synergy between the two: reasoning traces help the model induce, track, and update action plans as well as handle exceptions, while actions allow it to interface with external sources, such as knowledge bases or environments, to gather additional information. We apply our approach, named ReAct, to a diverse set of language and decision making tasks and demonstrate its effectiveness over state-of-the-art baselines, as well as improved human interpretability and trustworthiness over methods without reasoning or acting components. Concretely, on question answering (HotpotQA) and fact verification (Fever), ReAct overcomes issues of hallucination and error propagation prevalent in chain-of-thought reasoning by interacting with a simple Wikipedia API, and generates human-like task-solving trajectories that are more interpretable than baselines without reasoning traces. On two interactive decision making benchmarks (ALFWorld and WebShop), ReAct outperforms imitation and reinforcement learning methods by an absolute success rate of 34% and 10% respectively, while being prompted with only one or two in-context examples.

### Core Methodology

**The ReAct paradigm** interleaves Thought-Action-Observation triples:

```
Thought: I need to find information about X.
Action: Search[X]
Observation: X is a concept that...
Thought: Based on this, I can conclude Y.
Action: Finish[Y]
```

This interleaving allows:
1. **Reasoning traces** to ground action planning in observed context
2. **Actions** to ground reasoning in external reality (Wikipedia, environment)
3. **Dynamic replanning** when actions produce unexpected observations

### Key Comparisons

| Method | Reasoning | Acting | External Info |
|--------|-----------|--------|---------------|
| Chain-of-Thought (CoT) | Yes | No | No |
| Act-only | No | Yes | Yes |
| ReAct | Yes (interleaved) | Yes | Yes |

**ReAct advantages over CoT**: Reduces hallucination by grounding reasoning in retrieved facts; enables error recovery through iterative action-observation loops.

**ReAct advantages over Act-only**: More interpretable trajectories; better long-horizon planning through explicit reasoning traces.

### Experimental Results

**Knowledge-intensive QA tasks**:
- HotpotQA: ReAct outperforms Act-only and CoT, with fewer hallucinations
- Fever (fact verification): ReAct achieves higher accuracy by verifying claims against Wikipedia

**Interactive decision making**:
- ALFWorld (text-based game): +34% success rate vs. BUTLER (imitation learning baseline)
- WebShop (simulated e-commerce): +10% success rate vs. IL/RL baselines

**Human evaluation**: ReAct trajectories rated as more interpretable and trustworthy than Act-only or CoT trajectories.

### Why ReAct Matters

ReAct established the foundational "think-then-act" paradigm for LLM agents that has since been adopted by virtually every major agent framework (LangChain, LlamaIndex, AutoGPT, OpenAgents, etc.). It showed that:

1. Reasoning and acting are complementary, not competing, capabilities
2. External tools can ground LLM reasoning in factual reality
3. Thought traces serve as an implicit scratchpad for multi-step problem solving
4. Few-shot prompting is sufficient to elicit ReAct behavior in capable LLMs

The paper directly inspired Reflexion (which adds verbal self-reflection), Toolformer (which learns tool use), and many subsequent agent architectures that use tool-augmented reasoning.

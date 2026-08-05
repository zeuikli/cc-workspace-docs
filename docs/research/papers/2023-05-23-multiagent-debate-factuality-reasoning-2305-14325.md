---
url: "https://arxiv.org/abs/2305.14325"
title: "Improving Factuality and Reasoning in Language Models through Multiagent Debate"
archived_date: 2026-06-09
arxiv_id: 2305.14325
authors: ["Yilun Du", "Shuang Li", "Antonio Torralba", "Joshua B. Tenenbaum", "Igor Mordatch"]
domains: [cs.CL, cs.AI]
pdf_path: pdfs/2305.14325.pdf
published_date: 2023-05-23
tags: [multi-agent, debate, reasoning, factuality, hallucination, llm]
---

# Improving Factuality and Reasoning in Language Models through Multiagent Debate

**arXiv**: 2305.14325 | **發表**: 2023-05-23 | **PDF**: 2023-05-23-multiagent-debate-factuality-reasoning-2305-14325.pdf

## 核心貢獻

Du et al.（MIT / Google）提出「Society of Minds」多 agent 辯論機制：多個 LLM 實例對同一問題獨立作答，再互相閱讀答案並更新自己的回應，迭代多輪至收斂。核心假設：多視角辯論能比單 agent 更有效地消除幻覺並提升推理一致性。

## 方法 / 架構

- **辯論設定**：N 個獨立 LLM agents（同模型），各自先獨立作答
- **迭代輪次**：每輪每個 agent 閱讀其他 agents 的答案後更新自己的回應，共 T 輪（通常 T=3）
- **收斂判斷**：多數一致視為終態；無需外部裁判（self-organizing consensus）
- **黑盒相容**：只需 prompt-in / answer-out，不需模型微調或內部修改
- **零額外訓練成本**：可直接部署於現有 LLM API（實驗使用 ChatGPT）

## 關鍵發現與數據（ar5iv 抓取，數據已核實）

| 任務 | 單 Agent | 多 Agent 辯論 | 提升 |
|------|---------|-------------|------|
| Arithmetic | 67.0% ± 4.7 | 81.8% ± 2.3 | +14.8pp |
| GSM8K | 77.0% ± 4.2 | 85.0% ± 3.5 | +8.0pp |
| MMLU | 63.9% ± 4.8 | 71.1% ± 4.6 | +7.2pp |
| Biography factuality | 66.0% ± 2.2 | 73.8% ± 2.3 | +7.8pp |
| Chess move validity | 29.3% ± 2.6 | 45.2% ± 2.9 | +15.9pp |

## 對 agent-team 設計的啟示

1. **辯論是免訓練的推理增強**：對複雜推理任務可以直接在 inference 時疊加 debate round，無需更強的模型
2. **任務類型影響效益**：arithmetic / factual 任務提升明顯（+8~15pp）；過度簡單或過度複雜任務效益遞減
3. **收斂失敗是風險**：若多 agent 形成錯誤共識（echo chamber），辯論反而固化錯誤——需設計 diversity preservation 機制（呼應 AgentVerse groupthink 問題）

## 原文關鍵引用（≤150字）

> "We propose a method where multiple language model instances propose and debate their individual responses and reasoning processes over multiple rounds to arrive at a common final answer. Our findings suggest that this approach significantly enhances mathematical and strategic reasoning across several benchmarks while improving the factual validity of generated content, reducing fallacious answers and hallucinations... Our approach also applies to black-box models using identical prompts across all tasks."

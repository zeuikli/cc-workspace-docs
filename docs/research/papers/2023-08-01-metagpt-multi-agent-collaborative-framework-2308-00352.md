---
url: "https://arxiv.org/abs/2308.00352"
title: "MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework"
archived_date: 2026-06-09
arxiv_id: 2308.00352
authors: ["Sirui Hong", "Mingchen Zhuge", "Jonathan Chen", "Xiawu Zheng", "Yuheng Cheng", "Ceyao Zhang", "Jinlin Wang", "Zili Wang", "Steven Ka Shing Yau", "Zijuan Lin", "Liyang Zhou", "Chenyu Ran", "Lingfeng Xiao", "Chenglin Wu", "Jürgen Schmidhuber"]
domains: [cs.AI, cs.MA]
pdf_path: pdfs/2308.00352.pdf
published_date: 2023-08-01
tags: [multi-agent, sop, software-development, meta-programming, role-based, llm]
venue: ICLR 2024
---

# MetaGPT: Meta Programming for A Multi-Agent Collaborative Framework

**arXiv**: 2308.00352 | **發表**: 2023-08-01 | **PDF**: 2023-08-01-metagpt-multi-agent-collaborative-framework-2308-00352.pdf

## 核心貢獻

將人類軟體工程 Standardized Operating Procedures（SOP）編碼進 LLM multi-agent 工作流。每個 agent 扮演具體職能角色（Product Manager / Architect / Project Manager / Engineer / QA），以結構化文件（需求文件、設計圖、API 規範）取代非結構化對話傳遞，防止級聯幻覺（cascading hallucination）。

## 方法 / 架構

- **角色分工（Role Specialization）**：5 個固定角色，各有明確職責邊界；不跨角色自決
- **結構化輸出（Structured Communication）**：agent 輸出 diagrams / documents 而非自由文字，強制中間驗證
- **可執行回饋迴圈（Executable Feedback）**：Engineer 可迭代測試 + debug；QA 驗證後回饋修正

## 關鍵發現與數據

- HumanEval Pass@1：**85.9%**；MBPP Pass@1：**87.7%**（當時 SOTA）
- SoftwareDev executability score：**3.75 / 4**；Human revision cost：**0.83** 次/任務
- Token 效率：**124.3 tokens/loc**（vs. ChatDev 248.9，節省 50%）
- AutoGPT / LangChain / AgentVerse 在 SoftwareDev 全部得分 1.0（無法生成可執行代碼）

## 對 agent-team 設計的啟示

1. **SOP 即 coordination protocol**：人類組織流程可直接轉為 prompt sequence，大幅減少 agent 間歧義
2. **結構化 artifacts > 自由對話**：強制中間產出格式讓 agent 協作可機械驗證（R4 完成條件思想）
3. **角色邊界保護 token 效率**：避免多 agent 重複做同一件事，token 節省 2× 可觀

## 原文關鍵引用（≤150字）

> "MetaGPT incorporates efficient human workflows as a meta programming approach into LLM-based multi-agent collaboration. Specifically, MetaGPT encodes Standardized Operating Procedures (SOPs) into prompt sequences for more streamlined workflows, thus allowing agents with human-like domain expertise to verify intermediate results and reduce errors. MetaGPT takes a multi-agent framework built on top of GPT-4 and assigns different roles to GPT-4 agents to collaboratively complete complex software engineering tasks."

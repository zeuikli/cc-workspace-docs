---
url: "https://arxiv.org/abs/2307.07924"
title: "ChatDev: Communicative Agents for Software Development"
archived_date: 2026-06-09
arxiv_id: 2307.07924
authors: ["Chen Qian", "Wei Liu", "Hongzhang Liu", "Nuo Chen", "Yufan Dang", "Jiahao Li", "Cheng Yang", "Weize Chen", "Yusheng Su", "Xin Cong", "Juyuan Xu", "Dahai Li", "Zhiyuan Liu", "Maosong Sun"]
domains: [cs.SE, cs.CL, cs.AI]
pdf_path: pdfs/2307.07924.pdf
published_date: 2023-07-16
tags: [multi-agent, software-development, communicative-agents, chat-chain, llm]
venue: ACL 2024
---

# ChatDev: Communicative Agents for Software Development

**arXiv**: 2307.07924 | **發表**: 2023-07-16 | **PDF**: 2023-07-16-chatdev-communicative-agents-software-development-2307-07924.pdf

## 核心貢獻

以「虛擬軟體公司」為比喻，採用 waterfall 模型分階段（設計→編碼→測試→文件）讓多個 LLM agent 以自然語言和程式語言交互協作。核心創新：**Chat Chain**（控制通訊順序）+ **Communicative Dehallucination**（雙 agent 對話中主動偵測並消除幻覺輸出）。發表於 ACL 2024。

## 方法 / 架構

- **Chat Chain**：將開發流程切割成有序的雙人對話原子操作（atomic chat），每步一個 instructor + 一個 assistant
- **Communicative Dehallucination**：當 assistant 給出不確定或錯誤陳述時，instructor 觸發澄清追問，迭代消除幻覺
- **角色**：CEO、CTO、Programmer、Reviewer、Tester；角色間不跨越溝通，只在相鄰階段對話
- **語言雙軌**：設計/需求用自然語言；debug/code review 用程式語言，語言選擇由上下文決定

## 關鍵發現與數據

- 可成功生成可執行完整程式（vs. 早期 GPT-4 單 agent 方法高失敗率）
- Communicative Dehallucination 顯著降低程式碼 logic error 率（具體數字見全文 §5）
- 對比實驗：純 Chat Chain（無 dehallucination）vs 完整 ChatDev，後者 code executability 提升明顯
- Token 效率：248.9 tokens/loc（MetaGPT 論文反向引用此數作基準對比）

## 對 agent-team 設計的啟示

1. **waterfall 的 staged pipeline 降低協作複雜度**：每階段只需一對 agent 對話，避免全 agent 廣播混亂
2. **Communicative Dehallucination 是 multi-agent 特有的校正機制**：單 agent 無法自我觸發追問，雙 agent 角色差異讓幻覺可見
3. **語言切換作為信號**：程式語言溝通本身即測試，NL 交互作為設計驗收，善用媒介差異

## 原文關鍵引用（≤150字）

> "We present ChatDev, a chat-powered software development framework in which specialized agents driven by large language models (LLMs) are guided in what to communicate (via chat chain) and how to communicate (via communicative dehallucination)... These agents actively contribute to the design, coding, and testing phases through unified language-based communication, with solutions derived from their multi-turn dialogues."

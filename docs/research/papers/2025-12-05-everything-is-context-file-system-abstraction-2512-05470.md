---
url: "https://arxiv.org/abs/2512.05470"
title: "Everything is Context: Agentic File System Abstraction for Context Engineering"
archived_date: 2026-07-30
arxiv_id: 2512.0547
authors: ["Xiwei Xu", "Robert Mao", "Quan Bai", "Xuewu Gu", "Yechao Li", "Liming Zhu"]
collected_at: 2026-07-30
collected_by: routine-d
domain: context-engineering
pdf_path: pdfs/2512.05470.pdf
published_date: 2025-12-05
---

# Everything is Context: Agentic File System Abstraction for Context Engineering

## 摘要 / 核心貢獻
主張生成式 AI 系統管理外部知識、記憶、工具與人類輸入的核心挑戰不在模型微調而在「context engineering」，借用 Unix「everything is a file」原則，提出檔案系統抽象層：以統一掛載、metadata、存取控制機制管理 context 產物。開源實作 AIGNE 框架提供「可驗證的 context-engineering pipeline」，含三元件：Context Constructor（組裝）、Loader（傳遞）、Evaluator（在 token 限制下驗證）。將人定位為「curator、verifier、co-reasoner」，強調可追責性與可追溯性。以具記憶能力的 agent 與 MCP-based GitHub 助手兩個實例展示於開發者與工業場景的可行性，目標是打造比現有零散 prompt engineering / RAG 實踐更可治理、可驗證、可維護的 GenAI 系統。

## 與 Harness 的關聯
「everything is a file」把 context 產物統一成可掛載、可稽核的物件，與 workspace `.claude/refs/` + `skills/` 的三層下沉結構（閘門/程序/可呼叫流程分層落點）方向一致；其 Evaluator 元件（token 限制下驗證 context）可與 context-management.md 的 progressive disclosure 判準互相參照。

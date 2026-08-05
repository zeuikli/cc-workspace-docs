---
url: "https://arxiv.org/abs/2606.01385"
title: "Bridging Requirements and Architecture: Multi-Agent Orchestration with External Knowledge and Hierarchical Memory"
arxiv_id: 2606.01385
collected_at: 2026-08-04
collected_by: routine-d
domain: Multi-Agent
pdf_path: pdfs/2606.01385.pdf
year: 2026
---

# Bridging Requirements and Architecture: Multi-Agent Orchestration with External Knowledge and Hierarchical Memory

## 摘要 / 核心貢獻

論文提出 MAAD 框架，用於自動化軟體架構設計：協調四個專職 agent（Analyst、Modeler、Designer、Evaluator）自主協作，將需求規格轉換為完整、多視角的架構藍圖。框架整合 RAG 以納入架構標準，並實作階層式記憶支援迭代改善。與 MetaGPT 對比測試顯示 MAAD 產生的架構更模組化、更可追溯。作者指出產出架構品質高度依賴底層 LLM 的推理能力，使用如 GPT-5.2 等進階模型時各項評測指標表現更優。

## 與 Harness 的關聯

四專職 agent 分工（分析→建模→設計→評估）+ 階層式記憶迭代改善的模式，可作為 fusion lead/sidekick 架構或多階段 code review pipeline（發現→驗證→綜合）設計時，「角色分工如何配 external knowledge 與記憶」的具體案例參照。

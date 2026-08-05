---
url: "https://arxiv.org/abs/2603.22862"
title: "The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration"
archived_date: 2026-07-31
arxiv_id: 2603.22862
authors: ["Haoyuan Xu", "Chang Li", "Xinyan Ma", "Xianhao Ou", "Zihan Zhang", "Tao He", "Xiangyu Liu", "Zixiang Wang", "Jiafeng Liang", "Zheng Chu", "Runxuan Liu", "Rongchuan Mu", "Dandan Tu", "Ming Liu", "Bing Qin"]
collected_at: 2026-07-31
collected_by: routine-d
domain: agent-architecture
pdf_path: pdfs/2603.22862.pdf
published_date: 2026-03-24
---

# The Evolution of Tool Use in LLM Agents: From Single-Tool Call to Multi-Tool Orchestration

## 摘要 / 核心貢獻
系統性回顧 LLM 代理工具使用的演進，從基礎單一工具呼叫到複雜多工具、跨長任務序列的協調。以六個維度組織文獻：推理期規劃與執行、訓練與軌跡建構、安全與控制、資源受限下的效率、開放環境中的能力完整性、以及 benchmark 設計與評測，應用範圍涵蓋軟體工程、企業系統、圖形介面與行動平台，並指出打造「可靠、可擴展、可驗證」多工具代理仍面臨的關鍵挑戰。

## 與 Harness 的關聯
六維度分類（尤其「安全與控制」「資源受限下效率」）為本 repo 的工具授權設計（如 sub-agent tools 白名單、`.claude/agents/**` 權限分層）提供跨文獻對照的分類座標，可用於盤點本 workspace 工具治理是否遺漏某一維度。

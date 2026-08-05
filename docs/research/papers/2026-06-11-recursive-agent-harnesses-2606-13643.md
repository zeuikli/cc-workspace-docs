---
url: "https://arxiv.org/abs/2606.13643"
title: "Recursive Agent Harnesses"
archived_date: 2026-07-18
arxiv_id: 2606.13643
authors: ["Elias Lumer", "Sahil Sen", "Kevin Paul", "Vamse Kumar Subbiah"]
pdf_path: pdfs/2606.13643.pdf
published_date: 2026-06-11
---

# Recursive Agent Harnesses

**Authors**: Elias Lumer, Sahil Sen, Kevin Paul, Vamse Kumar Subbiah
**Published**: June 2026
**Source**: https://arxiv.org/abs/2606.13643
**arXiv ID**: 2606.13643
**Categories**: Computation and Language (cs.CL)
**PDF**: [research/papers/pdfs/2606.13643.pdf](https://arxiv.org/abs/2606.13643)

---

## Abstract

The paper explores how recursion over model calls is an effective strategy for long-context reasoning, extending this concept to what they term Recursive Agent Harness (RAH). Their approach enables parent agents to generate and execute scripts that spawn multiple subagent harnesses in parallel, equipped with filesystem tools, code execution capabilities, and planning functions. The researchers conducted controlled evaluations on long-context reasoning tasks. Using GPT-5 as the baseline model, RAH improved performance from 71.75% to 81.36% on the Oolong-Synthetic benchmark (199 samples with context lengths reaching 4M tokens). When tested with Claude Sonnet 4.5, the same design architecture achieved 89.77% accuracy, demonstrating the effectiveness of the harness design independent of model strength.

---

## Core Thesis

- 提出 Recursive Agent Harness (RAH)：parent agent 生成並執行腳本，動態 spawn 多個並行 subagent harness（各自配備檔案系統工具、程式碼執行、規劃能力），將長上下文推理遞迴分解。
- 在 Oolong-Synthetic benchmark（199 樣本、上下文長達 4M token）上，GPT-5 基準效能從 71.75% 提升至 81.36%；換成 Claude Sonnet 4.5 達 89.77%，顯示 harness 設計效益獨立於底層模型強弱。
- 核心論點：遞迴式 model call 分解是處理超長上下文推理的有效策略，勝過單一 agent 在巨大上下文窗口內硬撐。
- **Workspace 關聯**：與本 workspace 的 sub-agent 委派拓撲（`core.md §PROPOSE 委派`（原 `subagent-strategy.md`） context 隔離／fan-out）在架構精神上高度一致——parent 調度 + 並行 sub-harness 執行，可作為未來評估「大型長任務是否該拆給多個 sub-agent 而非塞爆單一 context window」的量化參照（4M token 規模下遞迴分解優於單一長 context）。

---
url: "https://arxiv.org/abs/2605.05007"
title: "Uno-Orchestra: Parsimonious Agent Routing via Selective Delegation"
arxiv_id: 2605.05007
collected_at: 2026-08-04
collected_by: routine-d
domain: Multi-Agent
pdf_path: pdfs/2605.05007.pdf
year: 2026
---

# Uno-Orchestra: Parsimonious Agent Routing via Selective Delegation

## 摘要 / 核心貢獻

Uno-Orchestra 是 LLM 多代理系統的統一編排方法，不採用固定的任務分解策略，而是「選擇性分解任務，並將每個子任務派給一個可接受的（模型、原語）配對」。系統以強化學習、基於真實互動軌跡，同時學習任務分解與工作者指派。在涵蓋數學、程式碼生成、知識任務、長 context 與工具使用情境的 13 個 benchmark 上評測，結果達 macro pass@1 77.0%，較最強 workflow 基線高約 16%，且單次查詢成本低約一個數量級。

## 與 Harness 的關聯

「選擇性委派」而非固定分解，與 core.md §PROPOSE「委派須說得出具名效益」的判準同構——本文用 RL 學到的委派策略把「該不該委派、委派給誰」量化，可作為未來評估 multi-mode-agent 路由策略是否過度/不足委派的對照基準。

---
url: "https://arxiv.org/abs/2606.12191"
title: "Agentic Environment Engineering for Large Language Models: A Survey of Environment Modeling, Synthesis, Evaluation, and Application"
arxiv_id: 2606.12191
collected_at: 2026-08-03
collected_by: routine-d
domain: Harness Engineering
pdf_path: pdfs/2606.12191.pdf
year: 2026
---

# Agentic Environment Engineering for Large Language Models: A Survey of Environment Modeling, Synthesis, Evaluation, and Application

## 摘要 / 核心貢獻

本文把「環境」視為 LLM-based agent 跨領域運作的互動系統，提出涵蓋 modeling / synthesis /
evaluation / application 四大面向的系統性框架。環境依八項屬性、八個領域分類並分析其演進
軌跡；合成方法分為 symbolic synthesis 與 neural synthesis 兩種範式，各自搭配對應評估方法。
應用面探討 agent-環境共演化的四條互補路徑：記憶導向的經驗累積、workflow orchestration、
離線軌跡學習、探索式線上學習；並歸納三種環境演化範式（neural-driven／difficulty-driven／
scaling-driven）。結論提出 Environment-as-a-Service、多代理環境、神經符號環境等未來方向。

## 與 Harness 的關聯

本文把「環境」提升為與 agent 本身同等重要的一級工程對象，直接呼應本 workspace core.md
「blast radius」「worktree/容器物理隔離」的設計動機——environment modeling 的分類法可作為
未來評估 routine/agent 隔離策略成熟度的參照架構；其 Environment-as-a-Service 方向也與本庫
sub-agent 隔離（worktree isolation）的演進路徑相關。

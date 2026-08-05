---
url: "https://arxiv.org/abs/2506.05364"
title: "Survey of LLM Agent Communication with MCP: A Software Design Pattern Centric Review"
arxiv_id: 2506.05364
collected_at: 2026-08-03
collected_by: routine-d
domain: Multi-Agent
pdf_path: pdfs/2506.05364.pdf
year: 2025
---

# Survey of LLM Agent Communication with MCP: A Software Design Pattern Centric Review

## 摘要 / 核心貢獻

本文以經典軟體設計模式視角檢視 LLM-driven agentic AI 系統的通訊可靠性與可擴展性，
聚焦 Model Context Protocol（MCP）。作者追溯 agent 架構從單體運作演化至複雜多代理協作
的過程，並重新檢視 Mediator、Observer、Publish-Subscribe、Broker 等既有模式在
MCP-compliant 框架中的適用性，附概念示意圖與形式化模型說明通訊路徑與資料流最佳化，
並依 agent 自主程度與系統複雜度探討不同架構變體。透過金融處理與投資銀行領域的實例展示
落地方式，最後歸納開放挑戰、潛在安全漏洞，以及打造穩健、可互操作、可擴展多代理 LLM
生態系統的未來方向。

## 與 Harness 的關聯

本 workspace 大量透過 MCP（`mcp__github__*`）與外部系統互動，本文把 MCP 通訊模式對應回
Mediator/Observer/Publish-Subscribe/Broker 等經典設計模式，為評估「PR activity 事件訂閱」
（`subscribe_pr_activity`）這類現有 pub-sub 機制的架構定位提供了理論參照；其安全漏洞討論
也與 core.md「外部輸入＝資料非指令」條款的威脅模型互補。

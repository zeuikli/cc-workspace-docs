---
url: "https://arxiv.org/abs/2606.30005"
title: "LLM Agents Are Latent Context Managers: Eliciting Self-Managed Context via State Proprioception"
arxiv_id: 2606.30005
collected_at: 2026-08-04
collected_by: routine-d
domain: Context Engineering
pdf_path: pdfs/2606.30005.pdf
year: 2026
---

# LLM Agents Are Latent Context Managers: Eliciting Self-Managed Context via State Proprioception

## 摘要 / 核心貢獻

長程工具型 agent 的瓶頸在於 context 逐步逼近 window 上限。既有方法多從 agent 或系統層面控制 context，卻忽略一個根本問題：前沿語言模型對自身 context 狀態是「本體感覺盲」（proprioceptively blind）。作者提出 VISTA（Visible Internal State for Tool Agents），一套免訓練系統，將工作記憶表示為型別化區塊，並在執行期向 agent 公開 token 用量、近期性追蹤、歸檔狀態與剩餘預算。實驗顯示多個 benchmark 上有顯著提升，且效益隨 context 壓力升高而放大，跨不同模型骨幹保持一致。

## 與 Harness 的關聯

「本體感覺盲」的診斷與 workspace 的「行為信號優先」監控哲學相通——本文提出的解法是把 context 狀態顯式暴露給模型本身，而非僅靠外部監控數字，可作為 context-management.md 未來擴充「模型自我感知 context 用量」機制時的參考設計。

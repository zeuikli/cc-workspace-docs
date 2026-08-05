---
url: "https://arxiv.org/abs/2607.08010"
title: "Tool-Making and Self-Evolving LLM Agents in Low-Latency Systems"
arxiv_id: 2607.0801
collected_at: 2026-08-03
collected_by: routine-d
domain: Agent Architecture
pdf_path: pdfs/2607.08010.pdf
year: 2026
---

# Tool-Making and Self-Evolving LLM Agents in Low-Latency Systems

## 摘要 / 核心貢獻

本文處理生產環境 LLM agent 的延遲問題：以「部署前工具製造管線」取代重複的推論期程式
生成，系統把重複出現的 SOP 步驟編譯成經驗證、版本化的工具，工具合成則根基於實際執行
軌跡、後端 schema 與已標記的測試案例。部署於某履行中心告警分流系統中的實測顯示：
工具呼叫使中位延遲降低 42%，透過減少 run-to-run 變異，在 1,500 筆歷史告警上端到端
錯誤率最高降低 53%；結構化輸出帶來的架構簡化進一步將中位延遲再降 62%。版本化工具
除效能提升外還強化了可稽核性並揭露規格缺口，作者結論：self-evolving agent 能讓工業級
LLM 系統更快、更可靠、更易維運。

## 與 Harness 的關聯

本文的「部署前工具製造管線」概念與本 workspace `.claude/skills/` 的沉澱邏輯同構——把
反覆出現的操作序列從「每次由 LLM 即時規劃」升級為「預先驗證、版本化的固定流程」，正是
skill-creator/skill-evolution 把重複模式蒸餾成 SKILL 的動機所在；其實測數據（延遲 -42%
至 -62%、錯誤率 -53%）為「把常見操作固化為工具而非每次重新規劃」提供量化效益佐證。

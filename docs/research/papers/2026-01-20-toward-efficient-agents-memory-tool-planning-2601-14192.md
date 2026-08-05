---
url: "https://arxiv.org/abs/2601.14192"
title: "Toward Efficient Agents: Memory, Tool learning, and Planning"
arxiv_id: 2601.14192
collected_at: 2026-08-03
collected_by: routine-d
domain: Agent Architecture
pdf_path: pdfs/2601.14192.pdf
year: 2026
---

# Toward Efficient Agents: Memory, Tool learning, and Planning

## 摘要 / 核心貢獻

本文從三大核心元件——記憶、工具學習、規劃——檢視 LLM-based agent 系統的效率議題，
考量延遲、token、步驟數等成本。作者整理出各方法收斂的共同原則：透過壓縮與管理界定
context 邊界、設計強化學習獎勵以最小化工具呼叫次數、採用受控搜尋機制提升效率。評估
面向分兩種互補視角：在固定成本限制下比較效果、在相近效果下比較成本。文末彙整效率導向
的 benchmark 評估協定，並統整 benchmark 與方法論研究中常見的效率指標。

## 與 Harness 的關聯

本文的「固定成本比效果 / 固定效果比成本」雙視角評估框架，可直接對應本 workspace
`.claude/refs/model-profiles.md` 的檔位選擇邏輯（cost/quality/ceiling/frontier）——目前
檔位選擇偏重人工經驗法則，本文歸納的效率導向 benchmark 協定與指標，是未來若要把檔位
選擇量化為可回測指標時的方法論參考。

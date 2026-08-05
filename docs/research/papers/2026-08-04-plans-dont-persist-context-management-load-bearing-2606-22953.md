---
url: "https://arxiv.org/abs/2606.22953"
title: "Plans Don't Persist: Why Context Management Is Load Bearing for LLM Agents"
arxiv_id: 2606.22953
collected_at: 2026-08-04
collected_by: routine-d
domain: Context Engineering
pdf_path: pdfs/2606.22953.pdf
year: 2026
---

# Plans Don't Persist: Why Context Management Is Load Bearing for LLM Agents

## 摘要 / 核心貢獻

研究長程 LLM agent 的計畫（plan）究竟持久存於模型狀態，還是仰賴留在 context window 中。作者用「replay pairing」——比較有無計畫版本軌跡的診斷法——證明 Llama-3.1-70B 上計畫訊號在單一 action-observation 步驟內就衰減 4.1 倍。推理模型因 `<think>` 軌跡會重新推導計畫內容而造成量測干擾，作者以「strict stripping」處理後，held-out 表現回升 +153%，對非推理版 Llama 模型影響極小。壓縮壓力測試顯示實務後果：naive 計畫驅逐使 ALFWorld 成功率下降 34.7 個百分點，而 probe-gated re-surfacing 並未能挽回。結論：agent 關鍵資訊多半存在於 context 而非模型權重中，使 context management 成為 agent 表現的承重結構。

## 與 Harness 的關聯

直接證實 workspace context-management.md 的核心假設——「NLAH：right context > more context」；naive eviction 造成的性能崩潰數據，可作為 compact/handoff 設計時「計畫必須顯式留痕於 context 或 checkpoint」的實證依據。

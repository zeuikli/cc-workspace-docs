---
url: "https://arxiv.org/abs/2605.25310"
title: "Tool-Call Dependency Structure is Linearly Decodable in LLM Agent Residual Streams"
arxiv_id: 2605.2531
collected_at: 2026-08-03
collected_by: routine-d
domain: Mechanistic Interpretability
pdf_path: pdfs/2605.25310.pdf
year: 2026
---

# Tool-Call Dependency Structure is Linearly Decodable in LLM Agent Residual Streams

## 摘要 / 核心貢獻

本文探討語言模型 agent 是否在內部表徵中編碼了工具呼叫的執行依賴結構。作者對
Qwen3-32B 的 residual stream 訓練低容量 edge probe，證明能顯著優於 Hewitt-Liang
random-label control 與位置基線解碼出工具呼叫的依賴圖。透過反事實實驗證明該訊號反映
抽象拓撲而非具體識別碼數值；發現此表徵會隨層數傳播而非被動讀出，但實際工具呼叫執行
本身不受影響。研究橫跨多個互動式 benchmark 與兩個模型家族，是首個針對 LLM agent
runtime 工具呼叫依賴圖的結構性探針研究。

## 與 Harness 的關聯

本 workspace 的 Workflow 工具大量依賴 agent 對工具呼叫順序/依賴的隱式規劃（pipeline
vs. parallel 的選擇）。本文證明依賴結構在 residual stream 中線性可解碼、且會隨層傳播，
意味著模型對「這幾個工具呼叫彼此有依賴關係」存在內部表徵而非純粹輸出層決策——對於未來
若想在 workflow 腳本外部監控/驗證 agent 是否正確識別任務依賴關係，提供了可解釋性層面
的立足點。

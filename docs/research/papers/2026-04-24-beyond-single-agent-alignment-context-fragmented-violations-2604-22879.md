---
url: "https://arxiv.org/abs/2604.22879"
title: "Beyond Single-Agent Alignment: Preventing Context-Fragmented Violations in Multi-Agent Systems"
arxiv_id: 2604.22879
collected_at: 2026-08-02
collected_by: routine-d
domain: Safety / Alignment
pdf_path: pdfs/2604.22879.pdf
year: 2026
---

# Beyond Single-Agent Alignment: Preventing Context-Fragmented Violations in Multi-Agent Systems

## 摘要 / 核心貢獻

本論文命名一種新的安全漏洞類型：**Context-Fragmented Violation（CFV，情境碎片化違規）**
——每個 agent 個別的動作單獨看都「局部合規」，但因關鍵政策事實分散（silo）在不同
部門/agent 各自的私有 context 裡，彙整起來卻共同違反了整體政策。單一 agent 的
self-enforcement（訓練期對齊、單一 agent guardrail）無法偵測這種跨 agent 才會浮現
的違規。

解法為 **Distributed Sentinel**：一個分散式強制架構，用 **Semantic Taint Token
Protocol** 讓輕量 sidecar proxy 跨組織邊界傳遞安全狀態，並以 **Counterfactual
Graph Simulation** 做跨網域政策驗證，而不需暴露各方的敏感資料本身。實測：
Distributed Sentinel 達 F1 = 0.95、端到端延遲 106ms，對比 prompt-based filtering
的 F1 0.85 與 rule-based DLP 的 F1 0.65；對 8 個前沿 LLM 的測試顯示，跨網域資料流的
違規率達 14–98%，系統性地高於單一網域內的違規率。

## 與 Harness 的關聯

本 workspace 的 sub-agent 委派模式（parent 派工、child 不繼承 context、child verdict
非證據需 parent 重驗）正是防範 CFV 的雛型設計；本論文提供了量化證據——多個各自合規
的 agent 組合起來仍可能整體違規——佐證「child 產出不得直接採信、parent 必須親跑
確定性 gate」這條規則背後的風險並非假設性,而是已在多 agent 系統中實測存在的攻擊面。

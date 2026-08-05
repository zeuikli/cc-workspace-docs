---
url: "https://arxiv.org/abs/2607.05690"
title: "Memory in the Loop: In-Process Retrieval as Extended Working Memory for Language Agents"
arxiv_id: 2607.0569
collected_at: 2026-08-03
collected_by: routine-d
domain: Memory Architecture
pdf_path: pdfs/2607.05690.pdf
year: 2026
---

# Memory in the Loop: In-Process Retrieval as Extended Working Memory for Language Agents

## 摘要 / 核心貢獻

語言 agent 多以 observe-reason-act 迴圈運作，記憶卻通常是每回合查詢一次的外部資源。
本文主張把記憶直接嵌進迴圈本身，讓讀寫發生在每一步。過去阻礙這麼做的理由是網路儲存
的延遲；作者論證延遲源自儲存位置而非「迴圈內」這個做法本身——in-process store 的回應
時間約 100 微秒，比雲端系統快三個數量級，消除了效能懲罰。援引 extended-mind thesis：
夠快的記憶就不再是「被諮詢的工具」，而是真正的 working memory。實證顯示冗餘 agent
動作隨延遲單調增加；橫跨四個 GPT-5 級模型，in-loop 記憶大幅提升 recall 同時維持微秒級
反應時間。作者發現 embedding 運算才是真正瓶頸，搭配本地 embedder 後整體操作約 40 微秒
完成。

## 與 Harness 的關聯

本 workspace 的 memory-compactor / episodic-first 記憶策略目前是 session 邊界觸發的
批次操作，屬於「每回合查詢一次」的外部資源模式。本文的核心論點——延遲決定記憶是工具
還是 working memory——為未來若要把記憶操作下沉到迴圈內（例如 hook 層即時讀寫而非
compact 時批次處理）提供了效能門檻的參照基準（~100μs in-process vs. 網路延遲）。

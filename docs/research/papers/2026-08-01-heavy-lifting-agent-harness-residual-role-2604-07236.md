---
url: "https://arxiv.org/abs/2604.07236"
title: "How Much Heavy Lifting Can an Agent Harness Do?: Measuring the LLM's Residual Role in a Planning Agent"
arxiv_id: 2604.07236
collected_at: 2026-08-01
collected_by: routine-d
domain: Harness Engineering
pdf_path: pdfs/2604.07236.pdf
year: 2026
---

# How Much Heavy Lifting Can an Agent Harness Do?

## 摘要 / 核心貢獻

研究者探討一個少被量化的問題：在 AI agent 系統中，agent harness（有狀態的包裝程式）與底層 LLM 各自承擔多少責任？既有研究顯示同一模型套用不同 harness 效能可差到六倍，但各組件的實際貢獻並不清楚。

作者以「Collaborative Battleship」規劃任務為測試床，將 planning harness 拆解為四層漸進複雜度：後驗信念追蹤（posterior belief tracking）、宣告式規劃（declarative planning）、符號式反思（symbolic reflection）、LLM 驅動的修正閘（LLM-backed revision gate）。以勝率為主要指標、F1 為輔助指標，在 54 場對局中逐層隔離量測各組件貢獻。

關鍵發現：宣告式規劃（完全不涉及 LLM）承擔了主要效能提升（+24.1pp 勝率）；符號式反思有機制性價值但對校準敏感，board 層級效果在聚合時互相抵銷；最引人注目的是 LLM 驅動的修正閘僅在 4.3% 的回合中被觸發，效果有界且非單調——遠比一般預設的「LLM 為核心」角色更邊緣。核心方法論貢獻：把 harness 各層外部化後，能把 LLM 的角色量化為真正的「殘餘」（residual）而非預設的主導角色。

## 與 Harness 的關聯

> 2026-08-02 深讀 PDF 原檔後重寫，對齊 v5.1。

為 core.md「判斷 vs 決定」公理提供**目前 corpus 中最乾淨的量化實證**：確定性程序（宣告式規劃，**零 LLM 呼叫**）獨得 +24.1pp 勝率，而 LLM 驅動的修正閘只在 4.3% 回合觸發、效果有界且**非單調**。與同批收錄的〈Stop Comparing LLM Agents Without Disclosing the Harness〉互為佐證：當 harness 的確定性層做掉大部分重活，模型檔位的邊際貢獻會被系統性高估。

三點對 v5.1 的具體意涵：

1. **支持 v5.1 保留確定性閘門、刪除 advisory 嘮叨的刀口**。v5.1 刪 hook 的判準是「有無確定性消費者」（`tool-log.sh` 純寫入無消費者 → 刪；`block-dangerous.sh` 確定性攔截 → 留）。本文的分層量測給出同方向的量化形態：價值集中在確定性層，LLM 介入層是稀疏且效果有界的殘餘。
2. **⚠️ 但也警告「機制性為真」不等於「聚合有效」**。符號式反思層在 board 層級有真實效果（±0.140 F1），卻**在聚合時互相抵銷**——對校準高度敏感。這對 workspace 的意涵是：一道 gate 在個案上看得到作用，不代表它在整體交付品質上是正貢獻；v5.1 憑「摩擦感」刪 advisory hook 的做法方向正確，但同理也意味著**留下來的閘門未經聚合效果量測**，其淨值同樣未證實。
3. **方法論可移植**：本文的貢獻是「把 harness 各層外部化後才能量測 LLM 的殘餘角色」。workspace 目前無法回答「core.md 哪一條規則實際貢獻多少」，正是因為規則以單一 prompt 層混合供給、無法分層消融。若日後要驗證 v5.1 精簡是否傷及品質，本文的分層消融是可直接借用的實驗設計。⚠️ 落地門檻：本文測試床為單一窄任務（Collaborative Battleship，54 場對局），外推到開放式 coding 任務的效度未驗證。

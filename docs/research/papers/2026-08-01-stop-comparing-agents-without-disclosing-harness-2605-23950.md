---
url: "https://arxiv.org/abs/2605.23950"
title: "Stop Comparing LLM Agents Without Disclosing the Harness"
arxiv_id: 2605.2395
collected_at: 2026-08-01
collected_by: routine-d
domain: Harness Engineering
pdf_path: pdfs/2605.23950.pdf
year: 2026
---

# Stop Comparing LLM Agents Without Disclosing the Harness

## 摘要 / 核心貢獻

本文主張長任務上對 LLM agent 的效能比較普遍忽略了一個關鍵變因：模型周遭的執行基礎設施（agent harness）——管理 context、工具呼叫、協調與驗證的系統層。研究者常把效能提升歸因於模型選擇，實際上很大一部分增益來自 harness 配置的差異。

作者提出「Binding Constraint Thesis」：在此制度下，效能變異更大程度由 harness 配置決定，而非模型選擇。論證分三路徑：① **控制理論框架**——把 harness 建模為調節閉環系統的控制器，LLM 作為底層 policy，解釋為何微小的基礎設施調整可能蓋過模型替換的影響；② **實證證據**——檢視已發表 benchmark、真實世界實作與受控變異分解實驗；③ **評測協定提案**——要求明確揭露 harness 配置的 harness-aware 評測標準。

關鍵發現：harness 造成的效能變異經常超過模型造成的變異，甚至存在僅因 harness 配置不同就導致模型排名反轉的案例。當前 leaderboard 比較普遍缺乏對基礎設施選擇的透明度，可能誤導了對「真實科學進展」的認知。

## 與 Harness 的關聯

直接支持 core.md「Agent = Model + Body + Harness」公理與 `core.md §PROPOSE 委派`（原 `refs/graph-engineering.md`） G2「gate 不配模型」的判斷——本文提供實證與形式化論證：模型換檔位（cost/quality/ceiling/frontier）前，若未同時控制 harness 配置，觀測到的效能差異可能是 harness artifact 而非模型能力差異，呼應本 workspace `refs/model-profiles.md` 換模型重審時應先排查 harness 變因。

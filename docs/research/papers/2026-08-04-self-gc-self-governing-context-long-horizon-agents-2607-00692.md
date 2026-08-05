---
url: "https://arxiv.org/abs/2607.00692"
title: "Self-GC: Self-Governing Context for Long-Horizon LLM Agents"
arxiv_id: 2607.00692
collected_at: 2026-08-04
collected_by: routine-d
domain: Context Engineering
pdf_path: pdfs/2607.00692.pdf
year: 2026
---

# Self-GC: Self-Governing Context for Long-Horizon LLM Agents

## 摘要 / 核心貢獻

長程 LLM agent 累積大量 context，現行系統多用簡單啟發式（按時間順序修剪或粗略摘要）處理，兩者皆計算便宜但效果不佳，或保留敘事品質卻犧牲精確度。作者提出 Self-GC，把 context 視為生命週期管理的索引化物件而非可拋棄文字：將使用者輪次、工具跨度與 skill 狀態轉為索引物件，由側通道 planner 建議 fold／mask／prune 動作，並附可還原的 sidecar 與 cache-aware commit。33-session benchmark 上，該法修剪 43.95% 前綴 token，同時讓 84.85% 未來延續內容不受影響，顯著優於基線啟發式；生產環境部署使日間輸入 token 減少 10–15%，峰值近 20%。

## 與 Harness 的關聯

「context 作為可還原索引物件、非拋棄文字」的設計，直接對應 memory-compactor／dreaming-consolidator 的「grow-and-refine 增量更新不整體改寫」精神；fold/mask/prune 三動作分類可作為 compact 策略分級（何時摘要、何時遮蔽、何時真正丟棄）的具體化參考。

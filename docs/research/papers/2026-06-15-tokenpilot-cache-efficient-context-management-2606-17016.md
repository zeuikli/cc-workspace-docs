---
url: "https://arxiv.org/abs/2606.17016"
title: "TokenPilot: Cache-Efficient Context Management for LLM Agents"
arxiv_id: 2606.17016
collected_at: 2026-08-02
collected_by: routine-d
domain: Caching / KV Cache / Token Budget
pdf_path: pdfs/2606.17016.pdf
year: 2026
---

# TokenPilot: Cache-Efficient Context Management for LLM Agents

## 摘要 / 核心貢獻

長視野 LLM agent session 會持續累積工具呼叫紀錄與中間推理痕跡，導致 context 線性膨脹，
既拉高延遲成本也稀釋 prompt cache 命中率。TokenPilot 提出雙粒度（dual-granularity）
context 管理框架，同時兼顧文字精簡與 prompt cache 穩定性——這兩者過去互相矛盾：
單純裁剪/改寫 context 雖省 token，卻會打斷既有 prefix 的 KV cache 命中鏈，
反而拉高總成本。

方法分兩層：**全域 ingestion-aware compaction**（在新資訊進入時就先穩定 prompt prefix，
避免頻繁改寫破壞既有快取前綴）與**局部 lifecycle-aware eviction**（依 context 片段的
剩餘效用做驅逐排程，而非單純依時間或長度）。實測顯示：孤立模式（isolated mode）下
省 61% 與 56% 成本，連續模式（continuous mode）下省 61% 與 87% 成本，且在多個評測中
維持與既有系統相當的任務表現。TokenPilot 已整合進 LightMem2（GitHub 開源）。

## 與 Harness 的關聯

本論文直接對應本 workspace `context-management.md` 的 Prompt Caching 五禁令與
`output-compress` 的壓縮/快取權衡難題——ingestion-aware compaction 的「先穩定
prefix 再裁剪」思路，是「動態事實不寫穩定前綴」禁令的另一種工程實現，可作為
未來優化 context-management 規則時的量化參照案例。

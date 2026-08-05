---
url: "https://arxiv.org/abs/2607.16215"
title: "RAIL Guard: Closing the Evaluation-to-Remediation Gap in Responsible AI for LLM Agents"
arxiv_id: 2607.16215
collected_at: 2026-08-02
collected_by: routine-d
domain: Safety / Alignment
pdf_path: pdfs/2607.16215.pdf
year: 2026
---

# RAIL Guard: Closing the Evaluation-to-Remediation Gap in Responsible AI for LLM Agents

## 摘要 / 核心貢獻

傳統 guardrail 偵測到不安全輸出後只會「擋下」或「整段重試」，本論文主張這是在
浪費已產出的可用內容。RAIL Guard 提出 **evaluate-rewrite-reevaluate** 迴圈：
偵測到問題後不丟棄，而是針對 8 個可量測維度（如透明度、可歸責性、包容性等）
反覆修正輸出，直到通過或達重試上限。

實測橫跨 4 個前沿 LLM、4,276 筆內容輸出、6,400 個 agent 情境：closed-loop
remediation 收斂率達 96.9%，遠高於 block-and-retry 的 49.1%；feedback-driven
self-repair 達 86.6% 收斂率，且效用損失可忽略（p = 0.177）；在工具呼叫前先做
pre-tool-call 評估，可將不安全的 agent 執行降低 33%（p = 0.007）。但部分維度
難以靠此機制修正：Transparency 失敗率高達 93.0%、Accountability 92.8%、
Inclusivity 82.5%，顯示「修正而非封殺」對某些安全維度效果有限。開源 SDK 與
公開 benchmark 資料集已釋出。

## 與 Harness 的關聯

core.md 的「P0 安全二分：授權內→最小 hotfix 即修；授權外→blocking report」
與本論文的「evaluate-rewrite-reevaluate」精神相通——先嘗試修正而非直接封殺/擋下，
但也印證了修正並非萬能（部分維度高失敗率）：對應 workspace「連續修正兩次未果→
`/rewind` 不硬撐」的迭代上限設計，避免在難以修正的維度上無限迴圈重試。

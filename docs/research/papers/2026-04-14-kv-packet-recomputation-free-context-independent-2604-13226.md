---
url: "https://arxiv.org/abs/2604.13226"
title: "KV Packet: Recomputation-Free Context-Independent KV Caching for LLMs"
arxiv_id: 2604.13226
collected_at: 2026-08-02
collected_by: routine-d
domain: Caching / KV Cache / Token Budget
pdf_path: pdfs/2604.13226.pdf
year: 2026
---

# KV Packet: Recomputation-Free Context-Independent KV Caching for LLMs

## 摘要 / 核心貢獻

標準 KV cache 的根本限制：一段文件的 KV 狀態一旦被不同上下文重新拼接（例如同一份
文件出現在不同 prompt 位置或搭配不同前綴），既有快取即失效，必須整段重算。KV Packet
提出把快取文件視為「不可變封包」（immutable packet），外層包一層輕量、可訓練的
soft-token adapter，透過自我監督蒸餾（self-supervised distillation）學會彌合不同
使用情境間的不連續性，使同一份 KV 封包可以在不同上下文組合下重複使用而不需重算。

實測在 Llama-3.1 與 Qwen2.5 上：相較 CacheBlend、EPIC、SAM-KV 等既有 context-independent
快取重用方法，KV Packet 達到近乎零額外 FLOPs（相較全量重算），Time-to-First-Token
延遲優於所有基準，且 F1 分數與全量重算相當——即「重用的快取品質」與「重算」幾乎無損失。

## 與 Harness 的關聯

Prompt caching 五禁令的核心痛點正是「context 一變快取就全斷」；KV Packet
的封包化+adapter 橋接思路提供了一種工程解法雛型：讓可重用的靜態內容（如 CLAUDE.md、
skill 定義）以「封包」形式獨立於周遭動態 context 存在，降低前綴微調對整條快取鏈的破壞面。

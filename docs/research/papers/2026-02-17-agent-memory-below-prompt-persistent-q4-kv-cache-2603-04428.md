---
url: "https://arxiv.org/abs/2603.04428"
title: "Agent Memory Below the Prompt: Persistent Q4 KV Cache for Multi-Agent LLM Inference on Edge Devices"
arxiv_id: 2603.04428
collected_at: 2026-08-02
collected_by: routine-d
domain: Caching / KV Cache / Token Budget
pdf_path: pdfs/2603.04428.pdf
year: 2026
---

# Agent Memory Below the Prompt: Persistent Q4 KV Cache for Multi-Agent LLM Inference on Edge Devices

## 摘要 / 核心貢獻

邊緣裝置（如 Apple M4 Pro）跑多代理 LLM 系統時，RAM 容量是硬限制：實測只能同時容納
3 個 agent 的 KV cache，第 4 個以後就得整段重新 prefill，成本極高。本論文提出把
量化後的 KV cache（4-bit，Q4）持久化落盤，跳過昂貴的重新 prefill，讓同一裝置可同時
維持 10+ 個 agent 的上下文狀態。

系統含三個元件：**block pool**（以 safetensors 格式隔離儲存各 agent 的 Q4 KV cache）、
**BatchQuantizedKVCache**（支援多 agent 併發推理的批次量化快取管理）、以及
**cross-phase context injection**（跨階段注入累積的 attention 狀態而不必重算）。
實測在 Gemma 3 12B、DeepSeek-Coder-V2-Lite 16B、Llama 3.1 8B 三種架構上：快取還原
達最高 136× 的 TTFT 加速（Gemma 32K context），4-bit 量化讓可同時容納的 agent
數量比 FP16 多 4 倍，且困惑度（perplexity）影響極小（Gemma -0.7%、Llama +2.8%、
DeepSeek +3.0%）。

## 與 Harness 的關聯

本 workspace 的多代理編排（sub-agent 委派、Workflow pipeline）在單機/資源受限環境下
會遇到與本論文相同的「同時維持多個 agent context」瓶頸；量化 KV cache 持久化落盤的
做法，為未來若需在本地/邊緣環境擴大並行 sub-agent 數量時，提供了具體可行的成本-延遲
權衡參照數據。

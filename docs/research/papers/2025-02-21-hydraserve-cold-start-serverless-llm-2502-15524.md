---
url: "https://arxiv.org/abs/2502.15524"
title: "HydraServe: Minimizing Cold Start Latency for Serverless LLM Serving in Public Clouds"
date: 2025-09-25
arxiv: 2502.15524
authors: "Chiheng Lou, Sheng Qi, Chao Jin, Dapeng Nie, Haoran Yang, Yu Ding, Xuanzhe Liu, Xin Jin (Peking University + Alibaba Group)"
pdf: 2025-02-21-hydraserve-cold-start-serverless-llm-2502-15524.pdf
relevance: 間接（serverless GPU 層）— 概念類比 Claude Code session init 並行化 / overlap stages
topic: cold-start / serverless LLM / startup latency
---

# HydraServe — Minimizing Cold Start Latency for Serverless LLM Serving

## 核心問題
公有雲 serverless LLM serving 的 cold start latency 嚴重：生產環境 **冷啟動 instance 首 token >40 秒**，而後續每 token 僅 ~30ms。兩大挑戰：(1) LLM 需從遠端 registry 按需抓取大型 model weights，受限頻寬成為主瓶頸；(2) LLM runtime 高度複雜（CUDA runtime、AI frameworks、inference engines 多層相依），container 建立與 library loading 開銷大。

## 方法（4 個機制）
1. **Proactive model distribution**：跨 server 分散 model，讓 worker 可快速 fetch
2. **Overlap cold-start stages**：在 worker 內重疊冷啟動各階段（fetch / load / profile / prefill），減少串行等待
3. **Strategic GPU placement**：分散 cold-start instance 避免網路爭用
4. **Pipeline consolidation**：合併 worker group 為單一 serving endpoint，降低冷啟動資源消耗

## 關鍵數字
- Cold start latency 降低 **1.7×–4.7×**
- SLO attainment 改善 **1.43×–1.74×**（vs baselines）

## 對 cc-workspace 的遷移啟示
- **Overlap stages** -> SessionStart hook 串行 spawn（session-init 592ms + 其他）可改並行/async（`async: true`）
- **Proactive distribution / pre-warm** -> prompt cache pre-warming（`max_tokens:0`）保持 cache 暖態
- 核心類比：冷啟動延遲可由**架構重疊與預備**消除，而非僅靠縮減載入量

---
url: "https://arxiv.org/abs/2604.02770"
title: "Improving Role Consistency in Multi-Agent Collaboration via Quantitative Role Clarity"
arxiv_id: 2604.0277
collected_at: 2026-08-03
collected_by: routine-d
domain: Multi-Agent
pdf_path: pdfs/2604.02770.pdf
year: 2026
---

# Improving Role Consistency in Multi-Agent Collaboration via Quantitative Role Clarity

## 摘要 / 核心貢獻

LLM-based 多代理系統的常見失效模式：agent 未能維持指派角色，反而模仿其他 agent 的行為。
本文提出量化方法——role assignment matrix 衡量 agent 行為與角色描述間的語意相似度，
定義 role clarity matrix 為 softmax(S(φ))-I，其 Frobenius norm 反映角色對齊品質，並將此
指標作為輕量微調時的 regularizer 以強化角色遵守度。ChatDev 上的實驗顯示大幅改善：
Qwen 模型的角色越界率從 46.4% 降至 8.4%、role clarity 分數從 0.5328 升至 0.9097；
Llama 模型越界率從 43.4% 降至 0.2%；兩類模型的任務成功率同步提升。

## 與 Harness 的關聯

本 workspace 的 sub-agent roster（`.claude/agents/*.md`）以自然語言 description 定義各
agent 的職責邊界，依賴模型自律遵守而無量化度量。本文的 role clarity metric 提供了一種可
機械量測「sub-agent 是否越權模仿其他 agent 行為」的方法論，對 skill-roster-audit 一類的
overlap 稽核可作為未來加入量化維度的參考。

---
url: "https://arxiv.org/abs/2605.22502"
title: "Compiling Agentic Workflows into LLM Weights: Near-Frontier Quality at Two Orders of Magnitude Less Cost"
archived_date: 2026-07-31
arxiv_id: 2605.22502
authors: ["Simon Dennis", "Rivaan Patil", "Kevin Shabahang", "Hao Guo"]
collected_at: 2026-07-31
collected_by: routine-d
domain: loop-workflow-engineering
pdf_path: pdfs/2605.22502.pdf
published_date: 2026-05-21
---

# Compiling Agentic Workflows into LLM Weights: Near-Frontier Quality at Two Orders of Magnitude Less Cost

## 摘要 / 核心貢獻
質疑業界偏好編排框架（orchestration framework）而非把流程直接編譯進模型權重（fine-tuned weights）的現況，即便後者在程序性任務上實證表現更佳。作者以三個案例研究（14 節點的旅遊訂票、含產品知識的 14 節點 Zoom 支援、55 節點/6 決策樞紐的保險理賠）逐一拆解並實證反駁三項普遍認知障礙，主張把流程編譯進權重可避免 context 消耗、降低對前沿模型的依賴，並保護專有流程不外洩給第三方。

## 與 Harness 的關聯
這是對 `core.md`「判斷 vs 決定」公理的一個反例式挑戰——把確定性流程編譯進模型權重，某種程度上是把「決定」重新交還給模型本身而非外部程序層；對本 repo 而言是值得警惕的對照組，說明「權重內化流程」與「harness 外部化流程」在 context 成本與供應鏈保護上的取捨各有主張，非單向定論。

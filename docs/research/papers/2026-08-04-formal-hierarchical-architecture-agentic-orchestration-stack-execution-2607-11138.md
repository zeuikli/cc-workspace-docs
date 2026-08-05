---
url: "https://arxiv.org/abs/2607.11138"
title: "A Formal Hierarchical Architecture for Agentic Orchestration with Stack-Based Execution and Lazy Discovery"
arxiv_id: 2607.11138
collected_at: 2026-08-04
collected_by: routine-d
domain: Harness Engineering
pdf_path: pdfs/2607.11138.pdf
year: 2026
---

# A Formal Hierarchical Architecture for Agentic Orchestration with Stack-Based Execution and Lazy Discovery

## 摘要 / 核心貢獻

當 agent 面對扁平、單體式的工具註冊表時，模型必須同時評估數百上千個選項，導致 context 飽和與路由錯誤。本文提出以「有根樹」組織能力（capability）：內部節點負責路由決策，葉節點執行確定性任務；並引入類似下推自動機（Pushdown Automaton）的 LIFO stack 機制，讓 agent 能追蹤巢狀執行 context。核心創新是「lazy-loading discovery」——僅載入目前活躍節點的直接子節點，使記憶體與 prompt 成本隨已探索路徑而非全域註冊表規模成長，同時提供適合企業部署的隔離保證。論文含數學形式化、演算法分析，以及階層式路由對比扁平路由的 benchmark，並以真實部署案例 UPI Help（AI 驅動的數位支付客服系統）驗證實務可行性。

## 與 Harness 的關聯

本篇直接對應 workspace 近期高信號主題「Claude Managed Agents brain/hands/session 三層解耦架構」——都是把單體 agent 拆成分層、可獨立擴展的執行單元；stack-based 巢狀 context 追蹤與 lazy discovery 的 token 節省機制，可作為 harness/skill 註冊表擴大時的路由設計參考。

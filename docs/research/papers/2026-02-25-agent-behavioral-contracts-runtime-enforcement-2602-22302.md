---
url: "https://arxiv.org/abs/2602.22302"
title: "Agent Behavioral Contracts: Formal Specification and Runtime Enforcement for Reliable Autonomous AI Agents"
arxiv_id: 2602.22302
collected_at: 2026-08-02
collected_by: routine-d
domain: Safety / Alignment
pdf_path: pdfs/2602.22302.pdf
year: 2026
---

# Agent Behavioral Contracts: Formal Specification and Runtime Enforcement for Reliable AI Agents

## 摘要 / 核心貢獻

傳統軟體有形式化契約與 API 邊界，自主 agent 卻運作在未明確規範的自然語言指令上，
導致行為漂移與部署失敗難以事前偵測。本論文把 Design-by-Contract 原則搬進 AI 系統：
定義契約為四元組 C = (P, I, G, R)（前置條件 Preconditions、不變式 Invariants、
治理政策 Governance、復原機制 Recovery），並提出「(p, δ, k)-satisfaction」作為
考量 LLM 非決定性的機率式合規度量，透過執行期函式庫 AgentAssert 落地。

實測橫跨 6 家廠商共 7 個模型、200 個測試情境、1,980 個 session：有契約的 agent
偵測到「每 session 5.2–6.8 次無契約基準完全漏掉的軟性違規」（p < 0.0001）；硬性
約束合規率達 88–100%；行為漂移被界定在 D* < 0.27；前沿模型的復原率達 100%，
且每個動作的額外開銷 < 10ms。

## 與 Harness 的關聯

本 workspace 的 core.md「公理・紅線」與「不可逆操作永遠等確認」等條款，本質上就是
一組人工撰寫、靠模型自律遵守的行為契約，缺乏本論文所提的**執行期強制**與**機率式
合規度量**。若未來要把紅線從「行為約定」升級為「有 hook 支撐」（`[E]` 標記），
本論文的 (P, I, G, R) 契約結構與 AgentAssert 執行期檢查設計，是可直接參照的落地範本。

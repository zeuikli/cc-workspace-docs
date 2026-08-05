---
url: "https://arxiv.org/abs/2605.29801"
title: "AgentDoG 1.5: A Lightweight and Scalable Alignment Framework for AI Agent Safety and Security"
archived_date: 2026-07-30
arxiv_id: 2605.29801
authors: ["Dongrui Liu", "Yu Li", "Zhonghao Yang", "Peng Wang", "Guanxu Chen", "Yuejin Xie", "Qinghua Mao", "Wanying Qu", "Yanxu Zhu", "Tianyi Zhou"]
collected_at: 2026-07-30
collected_by: routine-d
domain: ai-safety-red-teaming
pdf_path: pdfs/2605.29801.pdf
published_date: 2026-05-28
---

# AgentDoG 1.5: A Lightweight and Scalable Alignment Framework for AI Agent Safety and Security

## 摘要 / 核心貢獻
針對 OpenClaw 等開放世界 agent 的安全風險，更新安全 taxonomy 涵蓋新興威脅（含 Codex/OpenClaw 執行環境），並建構資料引擎以極少訓練資料（約 1k 筆樣本）訓練 0.8B–8B 輕量模型變體，效能可比擬 GPT-5.4 等閉源模型。資料引擎採 influence-function purification；建立 agentic safety 訓練環境，將 Docker 層部署開銷降低兩個數量級。AgentDoG 1.5 可作為訓練期外部署的 training-free 即時 guardrail，於多樣複雜互動式 agentic 場景展現穩定表現；模型與資料集皆公開釋出。

## 與 Harness 的關聯
輕量、可即時掛載的 training-free guardrail，是本 workspace core.md「安全例外」條款（加密原語/身份驗證等永遠獨立共用函式）在 agent 安全層的對應實作型態——把安全判斷收斂成可低成本部署的獨立守門模組，而非仰賴主模型自我約束，與 harness-mu（execution hook 非 LLM 治理）方法論同源。

---
url: "https://arxiv.org/abs/2506.02951"
title: "Adaptive Graph Pruning for Multi-Agent Communication"
archived_date: 2026-07-26
arxiv_id: 2506.02951
authors: ["Boyi Li", "Zhonghan Zhao", "Der-Horng Lee", "Gaoang Wang"]
domains: [cs.CL, cs.MA]
html: "https://arxiv.org/html/2506.02951v3"
pdf_path: pdfs/2506.02951.pdf
published_date: 2025-06-03
---

# Adaptive Graph Pruning for Multi-Agent Communication

**Authors**: Boyi Li, Zhonghan Zhao, Der-Horng Lee, Gaoang Wang
**Published**: June 3, 2025（最新版 v3：2025-07-23）
**Source**: https://arxiv.org/abs/2506.02951 · [HTML](https://arxiv.org/html/2506.02951v3)
**arXiv ID**: 2506.02951
**Categories**: cs.CL; cs.MA
**PDF**: [research/papers/pdfs/2506.02951.pdf](https://arxiv.org/abs/2506.02951)

---

## Abstract (quoted)

> Large Language Model (LLM) based multi-agent systems have shown remarkable performance in various tasks, especially when enhanced through collaborative communication. However, current methods often rely on a fixed number of agents and static communication structures, limiting their ability to adapt to varying task complexities. In this paper, we propose Adaptive Graph Pruning (AGP), a novel task-adaptive multi-agent collaboration framework that jointly optimizes agent quantity (hard-pruning) and communication topology (soft-pruning).

---

## 結構化摘要

### 核心貢獻

- **雙階段訓練**：Stage 1 從異質 agent pool 採樣多種通訊拓撲、任務微調後保留表現前 2 的圖，產生 460 組 (任務, 邊權重矩陣, 節點遮罩) 監督資料；Stage 2 訓練聯合軟硬剪枝網路
- 剪枝網路四模組：Sentence-BERT 節點編碼器、2 層 GCN 主幹、雙線性投影邊權重頭、2 層 MLP 節點遮罩頭
- 雙損失：軟剪枝（邊）MSE + 負邊稀疏化、硬剪枝（節點）BCE + 稀疏懲罰 + 相干項；**Gumbel-Sigmoid** 連續-離散橋接，溫度 1.0→0.1 退火（早期探索多圖、後期收斂離散決策）
- Agent pool：15 角色完全圖 K₁₅（數學求解器、程式設計專家、批評家、醫生等跨領域角色）

### 關鍵結果

- gpt-4o-mini：6 個 benchmark 平均 **91.04%** vs G-Designer **89.56%**（+1.48%）；對比單 agent baseline 提升 **2.58%–9.84%**（MMLU 87.65%、GSM8K 95.01%、HumanEval 90.62%）
- Token 經濟性：MMLU 較 GPTSwarm 減少 **90%+** token；GSM8K 較 G-Designer 減 12.7% token 同時準確度 +1.04%；HumanEval 減 22%
- 收斂快：MMLU 第 10 訓練步即達 88% 準確度超越 baseline，GSM8K 第 12 步收斂超越 G-Designer 全程
- gpt-3.5-turbo 遷移：平均 81.94%（+0.29%），但 MMLU 反降（−1.29%）
- 消融：移除軟剪枝掉 4.16–4.99pp；移除硬剪枝時提示長度增加 22–30%
- 案例研究：54% 任務最優圖與人設計拓樸一致（「完全直覺」）、43% 為人設計子集（「部分直覺」）、3% 為「反直覺」（含看似無關但提升效能的 agent）

### 限制

- 作者自陳：雙剪枝策略能否跨 LLM 家族/規模遷移未知（主要測 gpt-4o-mini / gpt-3.5-turbo，未涵蓋 Claude、Llama 等）
- 效率分析不足，缺乏細緻的推理延遲/成本量化（僅節點邊分析）
- 所有結果限於純文字任務，對多模態、時序擴展、具身 agent（視覺語言、工具使用、機器人）場景的有效性未驗證
- 未提供反直覺 agent 組合為何有效的解釋性分析，僅為經驗觀察

---

## Workspace 關聯（評估，非既成結論）

- 「軟剪枝（邊）+ 硬剪枝（節點）聯合最佳化」與本庫已收錄的 `agentprune-2410-02506`（首次形式化 MAS 通訊冗餘）方向一致，AGP 提供可訓練、任務自適應的量化解法，可補強 `core.md §PROPOSE 委派`（原 `graph.md`） fan-out 降噪的方法論基礎。
- 「3% 反直覺 agent 組合提升效能」提醒 `core.md §PROPOSE 委派`（原 `graph.md §G1`）「畫邊前問下游需要上游哪個具體產出」不能只靠直覺判斷拓樸——偶有反直覺依賴確實帶來增益。⚠️ 案例比例僅 3%，不足以動搖「答不出具體欄位就沒有這條邊」的預設保守原則。
- Token 節省 90%+ 的量級與 `output-compress` 分級壓縮目標同構，但 AGP 靠訓練達成、非 prompt 層規則，遷移需要訓練基礎設施，本 workspace 目前不具備。⚠️ 跨模型家族遷移性未知，直接套用需先驗證。

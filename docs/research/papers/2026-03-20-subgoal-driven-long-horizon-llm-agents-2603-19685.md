---
url: "https://arxiv.org/abs/2603.19685"
title: "A Subgoal-driven Framework for Improving Long-Horizon LLM Agents"
archived_date: 2026-06-24
arxiv_id: 2603.19685
authors: ["Taiyi Wang", "Sian Gooding", "Florian Hartmann", "Oriana Riva", "Edward Grefenstette"]
domains: [cs.AI]
html: "https://arxiv.org/html/2603.19685v1"
pdf_path: pdfs/2603.19685.pdf
published_date: 2026-03-20
---

# A Subgoal-driven Framework for Improving Long-Horizon LLM Agents

**Authors**: Taiyi Wang, Sian Gooding, Florian Hartmann, Oriana Riva, Edward Grefenstette
**Published**: March 20, 2026
**Source**: https://arxiv.org/abs/2603.19685 · [HTML](https://arxiv.org/html/2603.19685v1)
**arXiv ID**: 2603.19685
**Categories**: cs.AI
**PDF**: [research/papers/pdfs/2603.19685.pdf](https://arxiv.org/abs/2603.19685) (50 pp, full text archived)

---

## Abstract (quoted)

> Large language model (LLM)-based agents have emerged as powerful autonomous controllers for digital environments, including mobile interfaces, operating systems, and web browsers. Web navigation, for example, requires handling dynamic content and long sequences of actions, making it particularly challenging. Existing LLM-based agents struggle with long-horizon planning in two main ways. During online execution, they often lose track as new information arrives, lacking a clear and adaptive path toward the final goal. This issue is further exacerbated during reinforcement learning (RL) fine-tuning, where sparse and delayed rewards make it difficult for agents to identify which actions lead to success, preventing them from maintaining coherent reasoning over extended tasks. To address these challenges, we propose two contributions. First, we introduce an agent framework that leverages proprietary models for online planning through subgoal decomposition. Second, we present MiRA (Milestoning your Reinforcement Learning Enhanced Agent), an RL training framework that uses dense, milestone-based reward signals. The real-time planning mechanism improves proprietary models such as Gemini by approximately a 10% absolute increase in success rate (SR) on the WebArena-Lite benchmark. Meanwhile, applying MiRA to the open Gemma3-12B model increases its success rate from 6.4% to 43.0%. This performance surpasses proprietary systems such as GPT-4-Turbo (17.6%) and GPT-4o (13.9%), as well as the previous open-model state of the art, WebRL (38.4%). Overall, our findings demonstrate that combining explicit inference-time planning with milestone-based rewards significantly improves an agent's long-horizon capabilities, paving the way for more robust and general-purpose autonomous systems.

---

## 結構化摘要

### 核心貢獻
- 提出以 **subgoal decomposition（子目標分解）** 為核心的 agent framework，利用 proprietary models 在 online execution 時做即時規劃，維持朝向 final goal 的 adaptive path。
- 提出 **MiRA（Milestoning your Reinforcement Learning Enhanced Agent）**：以 dense、milestone-based reward signals 取代 RL fine-tuning 中常見的 sparse/delayed reward，緩解 credit assignment 難題。
- 將 inference-time explicit planning 與 milestone-based reward 結合，針對 long-horizon web navigation（dynamic content + 長 action sequence）此一困難場景設計。

### 關鍵結果
- Real-time planning 機制使 proprietary 模型（如 Gemini）在 **WebArena-Lite** 上 success rate（SR）約 **+10% absolute**。
- MiRA 套用於 open 模型 **Gemma3-12B**：SR 從 **6.4% → 43.0%**。
- 該結果超越 proprietary 系統 **GPT-4-Turbo（17.6%）**、**GPT-4o（13.9%）**，以及 previous open-model SOTA **WebRL（38.4%）**。

### 限制
文件未列明確 limitation 章節（僅依 abstract 判讀）。推測弱點：
- 評測集中於 **WebArena-Lite** 單一 benchmark，跨 OS / mobile / 真實網站的泛化未在 abstract 證實。
- Online planning 依賴 **proprietary models（Gemini 等）**，有成本、延遲與可重現性疑慮。
- milestone reward 的設計多半需要 **task-specific 標註或啟發式**，abstract 未說明 milestone 如何自動界定，可能限制可擴展性。

---

## Workspace 關聯（評估，非既成結論）

- **子目標分解 ↔ The Loop IDENTIFY**：本文 subgoal decomposition 與 core.md 中「實作前先寫可機械驗證的成功條件、把 long task 拆為可獨立 loop 的子條件」高度同構；milestone reward 可視為「強成功條件」的 RL 化身。
- **long-horizon agent ↔ `core.md §PROPOSE 委派`（原 subagent-strategy.md） fan-out / handoff**：milestone-based 中間訊號對應 workspace 的 `[Checkpoint]` 與 handoff 機制——皆為對抗 long-horizon 中 goal drift 與 context rot 的中間錨點。⚠️ 落地門檻：本文為 RL training-time 方法，workspace 為 prompt-time 紀律，無法直接移植訓練流程。
- **dense reward ↔ unverified_success 閘門**：milestone reward「逐步驗證而非僅看終點」呼應 core.md TEST「靜態檢查 ≠ 端到端」與確定性 gate 親驗；可作為「為何中間驗證優於 sparse 終點評估」的外部佐證。
- ⚠️ 本論文無對應 codebase 落地路徑，僅為概念層參考，勿據此新增框架檔案。

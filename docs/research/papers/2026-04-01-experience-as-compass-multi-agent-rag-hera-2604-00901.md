---
url: "https://arxiv.org/abs/2604.00901"
title: "Experience as a Compass: Multi-agent RAG with Evolving Orchestration and Agent Prompts"
archived_date: 2026-06-24
arxiv_id: 2604.00901
authors: ["Sha Li", "Naren Ramakrishnan"]
domains: [cs.AI]
html: "https://arxiv.org/html/2604.00901v1"
pdf_path: pdfs/2604.00901.pdf
published_date: 2026-04-01
---

# Experience as a Compass: Multi-agent RAG with Evolving Orchestration and Agent Prompts

**Authors**: Sha Li, Naren Ramakrishnan
**Published**: April 1, 2026
**Source**: https://arxiv.org/abs/2604.00901 · [HTML](https://arxiv.org/html/2604.00901v1)
**arXiv ID**: 2604.00901
**Categories**: cs.AI
**PDF**: [research/papers/pdfs/2604.00901.pdf](https://arxiv.org/abs/2604.00901) (32 pp, full text archived)

---

## Abstract (quoted)

> Multi-agent Retrieval-Augmented Generation (RAG), wherein each agent takes on a specific role, supports hard queries that require multiple steps and sources, or complex reasoning. Existing approaches, however, rely on static agent behaviors and fixed orchestration strategies, leading to brittle performance on diverse, multi-hop tasks. We identify two key limitations: the lack of continuously adaptive orchestration mechanisms and the absence of behavior-level learning for individual agents. To this end, we propose HERA, a hierarchical framework that jointly evolves multi-agent orchestration and role-specific agent prompts. At the global level, HERA optimizes query-specific agent topologies through reward-guided sampling and experience accumulation. At the local level, Role-Aware Prompt Evolution refines agent behaviors via credit assignment and dual-axes adaptation along operational and behavioral principles, enabling targeted, role-conditioned improvements. On six knowledge-intensive benchmarks, HERA achieves an average improvement of 38.69% over recent baselines while maintaining robust generalization and token efficiency. Topological analyses reveal emergent self-organization, where sparse exploration yields compact, high-utility multi-agent networks, demonstrating both efficient coordination and robust reasoning.

---

## 結構化摘要

### 核心貢獻
- 提出 **HERA**，一個階層式（hierarchical）框架，**同時演化** multi-agent orchestration（協作拓撲）與 role-specific agent prompts（角色提示），解決現有 multi-agent RAG 依賴 static behavior + fixed orchestration 的脆弱性。
- **Global level**：以 reward-guided sampling + experience accumulation，針對每個 query 優化 query-specific agent topology（讓協作結構隨任務調整，而非固定）。
- **Local level**：提出 **Role-Aware Prompt Evolution**，透過 credit assignment 與 dual-axes adaptation（operational 與 behavioral 兩軸）對個別 agent 行為做 role-conditioned 的針對性改進。
- 將「過往經驗」當作導航羅盤（experience as a compass）—— 把累積的試驗訊號回饋進拓撲取樣與 prompt 演化，形成自我改進迴路。

### 關鍵結果
- 在 **six knowledge-intensive benchmarks** 上，相較近期 baselines 平均提升 **38.69%**。
- 維持 robust generalization 與 token efficiency（非以爆量 token 換準確率）。
- Topological 分析顯示 **emergent self-organization**：sparse exploration 收斂出 compact、high-utility 的 multi-agent network —— 兼具 efficient coordination 與 robust reasoning。

### 限制
文件未列明確 limitation 章節（基於 abstract 與後設資料判斷）。可能弱點：
- 「38.69% 平均提升」為跨 6 benchmark 平均，未在 abstract 揭露各 benchmark 變異與最差案例；可能掩蓋特定任務退化。
- reward-guided sampling + 經驗累積屬 online 演化，**收斂成本 / 冷啟動（cold-start）開銷**未在摘要量化，token efficiency 宣稱需看完整評估的 per-query 成本。
- emergent self-organization 為觀察性結論，未說明拓撲穩定性與跨 domain 遷移時是否需重新演化。

---

## Workspace 關聯（評估，非既成結論）

- **自我演化迴路對應**：HERA 的「experience accumulation → 回饋進 topology / prompt 演化」與 The Loop 的 RECORD 階段（結構化反思入庫、下次注入）同構；可作為 workspace 自我演化「機械驗證入庫、退化可觀測」設計的外部參照。⚠️ 落地門檻：HERA 的 reward 訊號來自 benchmark ground truth，workspace 任務多無此 dense reward，需先解決 evaluator 訊號來源。
- **Role-Aware Prompt Evolution vs auto-load 規則進化**：dual-axes（operational / behavioral）credit assignment 的思路，可對照 `autoload-evolution` skill 的「識別 Gap → 提案 → 驗證」閉環。⚠️ HERA 是 per-query online 演化；workspace 規則進化是離線、≤1 規則/cycle 的保守節奏，兩者風險容忍度不同，不可直接移植。
- **multi-agent orchestration vs subagent fan-out**：HERA 的 query-specific topology 自適應，對照 `core.md §PROPOSE 委派`（原 `subagent-strategy.md`）的固定 fan-out ≤4 + hierarchical parent↔child 規則 —— 提供「動態拓撲」是否值得引入的思考素材。⚠️ workspace 現行紀律刻意限制動態性以控 token/可預測性，引入前需評估 goal drift 風險。 〔v5.1：所引 workspace 細則已退役 → 見 `INDEX.md` §v5.1 規則退役對照〕
- **memory-compactor 連結**：HERA 把經驗壓縮成 compact high-utility network，與 `memory-compactor`（保留決策、移除冗餘）目標相近，可作為「經驗壓縮如何不損失 high-utility 訊號」的對照。⚠️ 純概念對照，無共用實作。

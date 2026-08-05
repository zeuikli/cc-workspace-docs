---
url: "https://arxiv.org/abs/2606.23983"
title: "Maestro Order: A Model-Agnostic Orchestration Harness"
archived_date: 2026-06-24
arxiv_id: 2606.23983
authors: ["Hidayet Aksu"]
domains: [cs.CR, cs.AI, cs.LO, cs.MA]
html: "https://arxiv.org/html/2606.23983v1"
pdf_path: pdfs/2606.23983.pdf
published_date: 2026-06-22
---

# Maestro Order: A Model-Agnostic Orchestration Harness

**Authors**: Hidayet Aksu
**Published**: June 22, 2026
**Source**: https://arxiv.org/abs/2606.23983 · [HTML](https://arxiv.org/html/2606.23983v1)
**arXiv ID**: 2606.23983
**Categories**: cs.CR, cs.AI, cs.LO, cs.MA
**PDF**: [research/papers/pdfs/2606.23983.pdf](https://arxiv.org/abs/2606.23983) (10 pp, full text archived)

---

## Abstract (quoted)

> A single forward pass of a capable model is a fast, fluent, and unreliable problem-solver: it is right often enough to be useful and wrong often enough to be dangerous; in language models, such confident errors are known as hallucinations. We present Maestro Order, a model-agnostic orchestration harness that turns unreliable solvers into reliable problem-solving systems by composing them according to four structural primitives (decompose, ensemble, verify, and recurse) and a budget-aware controller that decides where to spend compute.

---

## 結構化摘要

### 核心貢獻
把「單次 forward pass = 快但不可靠的 solver」視為待治理的元件，用 harness 層的結構化組合把不可靠 solver 變成可靠系統。四個結構 primitive + 預算感知 controller：

1. **Decompose** — 任務拆解為子問題。
2. **Ensemble** — 多 solver 表決，僅在「高於隨機水準」時有益，且受 shared error 上限約束。
3. **Verify** — verifier ensemble + 線上量測判別力；以 selective verification 在邊際「reliability-per-cost」最高處下注。
4. **Recurse** — 對未通過的子問題遞迴投入算力。
5. **Budget-aware controller** — 依邊際可靠度/成本比決定算力分配，把 solver 當 black box（model-agnostic）。

### 關鍵結果
- **Verification 幾何放大可靠度**：0.55 →（2 gate）0.98 →（4 gate）0.999。
- **Voting 僅在超隨機水準時有效**，且被 solver 間相關錯誤封頂。
- **Budget-aware controller** 以遠低於 voting-only 的成本達到目標可靠度。

### 限制
- 失敗模式：verifier gaming（被驗證器博弈）、solver 間相關錯誤、decomposition 誤差累積。
- 需 robust checker + solver 多樣化才能維持放大效果。

---

## Workspace 關聯（評估，非既成結論）

- **「判斷 vs 決定」直接背書**：controller 與 verify/recurse 為確定性 orchestration，solver（LLM）只做 judgment——與 core.md 跨切紀律「LLM 判斷、確定性代碼決定」同構。
- **`unverified_success` 閘門的量化版**：verification 幾何放大（0.55→0.999）= 「fresh-context verifier 優於 self-critique」+ 多道 gate 的數學論據；可作 `/pilot frontier` 稽核（原 quality-pipeline，v5.1 刪除） / `ship` S10 merge gate（原 verified-merge） 多 gate 設計參考。
- **`/pilot frontier` 稽核的成本模型**（原 `/qp`、`/pilot-review`，v5.1 併入 `pilot`）：budget-aware「邊際 reliability-per-cost」分配，呼應 effort-first + model 階梯的成本紀律。
- ⚠️ 單作者短文（10 pp），結果偏理論化推導；落地需自建 verifier ensemble。

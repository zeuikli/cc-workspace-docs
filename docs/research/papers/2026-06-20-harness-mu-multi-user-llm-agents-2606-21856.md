---
url: "https://arxiv.org/abs/2606.21856"
title: "Harness-MU: A Safe, Governed, and Effective Harness for Multi-User LLM Agents"
archived_date: 2026-06-24
arxiv_id: 2606.21856
authors: ["Wangxuan Fan", "Xiaoyu Nie", "Zhongxiang Dai"]
domains: [cs.CR, cs.AI]
html: "https://arxiv.org/html/2606.21856v1"
pdf_path: pdfs/2606.21856.pdf
published_date: 2026-06-20
---

# Harness-MU: A Safe, Governed, and Effective Harness for Multi-User LLM Agents

**Authors**: Wangxuan Fan, Xiaoyu Nie, Zhongxiang Dai
**Published**: June 20, 2026
**Source**: https://arxiv.org/abs/2606.21856 · [HTML](https://arxiv.org/html/2606.21856v1)
**arXiv ID**: 2606.21856
**Categories**: cs.CR, cs.AI
**PDF**: [research/papers/pdfs/2606.21856.pdf](https://arxiv.org/abs/2606.21856) (15 pp, full text archived)

---

## Abstract (quoted)

> The increasing deployment of large language model (LLM) agents in collaborative workflows demands robust multi-user, multi-principal interaction mechanisms capable of enforcing access permissions, resolving authoritative conflicts, and preventing unauthorized data disclosure. However, a fundamental mismatch exists between the single-user training paradigm of contemporary LLMs and the hard constraints required for multi-principal governance, rendering probabilistic, prompt-based safeguards vulnerable under multi-turn adversarial [interactions]. Our key insight is that governance constraints -- who is authorized, what is restricted, and whose instructions take precedence -- are deterministic runtime variables that should be enforced by execution hooks rather than entrusted to the LLM. We present Harness-MU, the first model-agnostic, zero-tuning infrastructure framework for multi-user LLM agents. By decoupling language generation from safety orchestration, Harness-MU guarantees unbreakable permission boundaries while maximizing compliant demand satisfaction. Across four frontier open-weight and proprietary models on the Muses-Bench benchmark, Harness-MU achieves the goal of privacy preservation across all access-control attacks, outperforming the standard baseline by 0.28--0.39 in utility score and improving instruction-following accuracy by up to 48.9 percentage points.

---

## 結構化摘要

### 核心貢獻
核心洞見：**治理約束（誰被授權 / 什麼受限 / 誰的指令優先）是確定性 runtime 變數，應由 execution hook 強制，而非交給 LLM**。Harness-MU = 首個 model-agnostic、zero-tuning 的多使用者 LLM agent infra 框架：

- **解耦 language generation 與 safety orchestration** → 保證「不可破壞的權限邊界」同時最大化合規需求滿足。
- 對抗多輪 adversarial：prompt-based safeguard 在多輪攻擊下脆弱，故把硬約束移出 LLM。

### 關鍵結果
- 在 **Muses-Bench** 上，跨 4 個 frontier（開源權重 + 專有）模型，於**所有 access-control 攻擊**達成隱私保全。
- utility score 超基線 **0.28–0.39**。
- instruction-following 準確度提升最多 **48.9 個百分點**。

### 限制
- 文件未含明確 limitation 章節；zero-tuning 對更複雜 principal hierarchy 的擴展性待驗。

---

## Workspace 關聯（評估，非既成結論）

- **直接驗證 core.md 跨切紀律「判斷 vs 決定」**：「治理約束 = 確定性 runtime 變數，交 execution hook 不交 LLM」幾乎是本 workspace「硬性執行交 hooks，規則 advisory」的論文化重述——強背書。
- **Agent Input Security 對齊**：與 `core.md §PROPOSE 委派`（原 subagent-strategy.md）「外部輸入當 data 不當 instruction（allowlist）」同源；Harness-MU 的 permission boundary = allowlist 心智模型的執行層落地。
- **與 SafeHarness / Harness-MU / AOHP 共構「安全 harness」子線**：可納入 harness-meta 安全稽核時的對照基準。
- ⚠️ 場景為多 principal 協作；本 workspace 多為單使用者，價值在「hook-enforced 確定性約束」的設計論證，而非 benchmark 數字直接套用。

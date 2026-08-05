---
url: "https://arxiv.org/abs/2604.22136"
title: "Sovereign Agentic Loops: Decoupling AI Reasoning from Execution in Real-World Systems"
archived_date: 2026-06-24
arxiv_id: 2604.22136
authors: ["Jun He", "Deying Yu"]
domains: [cs.CR]
html: "https://arxiv.org/html/2604.22136v1"
pdf_path: pdfs/2604.22136.pdf
published_date: 2026-04-24
---

# Sovereign Agentic Loops: Decoupling AI Reasoning from Execution in Real-World Systems

**Authors**: Jun He, Deying Yu
**Published**: April 24, 2026
**Source**: https://arxiv.org/abs/2604.22136 · [HTML](https://arxiv.org/html/2604.22136v1)
**arXiv ID**: 2604.22136
**Categories**: cs.CR
**PDF**: [research/papers/pdfs/2604.22136.pdf](https://arxiv.org/abs/2604.22136) (15 pp, full text archived)

---

## Abstract (quoted)

> Large language model (LLM) agents increasingly issue API calls that mutate real systems, yet many current architectures pass stochastic model outputs directly to execution layers. We argue that this coupling creates a safety risk because model correctness, context awareness, and alignment cannot be assumed at execution time. We introduce Sovereign Agentic Loops (SAL), a control-plane architecture in which models emit structured intents with justifications, and the control plane validates those intents against true system state and policy before execution. SAL combines an obfuscation membrane, which limits model access to identity-sensitive state, with a cryptographically linked Evidence Chain for auditability and replay. We formalize SAL and show that, under the stated assumptions, it provides policy-bounded execution, identity isolation, and deterministic replay. In an OpenKedge prototype for cloud infrastructure, SAL blocks 93% of unsafe intents at the policy layer, rejects the remaining 7% via consistency checks, prevents unsafe executions in our benchmark, and adds 12.4 ms median latency.

---

## 結構化摘要

### 核心貢獻
- 提出 **Sovereign Agentic Loops (SAL)**：一種 control-plane 架構，將 LLM 的 reasoning 與 execution 解耦——模型只發出帶 justification 的 structured intent，由 control plane 對照真實系統狀態與 policy 驗證後才執行。
- 引入 **obfuscation membrane**：限制模型對 identity-sensitive state 的存取，達成 identity isolation。
- 引入 **cryptographically linked Evidence Chain**：提供 auditability 與 deterministic replay 能力。
- 形式化 SAL，並證明在所述假設下可提供三項性質：policy-bounded execution、identity isolation、deterministic replay。

### 關鍵結果
- OpenKedge 雲端基礎設施 prototype 中，SAL 在 policy layer 攔截 **93%** 的 unsafe intent。
- 剩餘 **7%** 由 consistency check 拒絕。
- benchmark 中阻止了全部 unsafe execution。
- 中位延遲增加 **12.4 ms**（median latency overhead）。

### 限制
文件未列明確 limitation 章節（依 abstract 推斷）。判斷的弱點：
- 安全保證明確標注「under the stated assumptions」——若 policy 完整性、true system state 取得正確性等前提不成立，保證即失效；abstract 未揭露假設破裂時的退化行為。
- 評估僅單一 OpenKedge prototype + 自建 benchmark，缺跨域 / 對抗性 intent 泛化證據；93/7 的攔截分布可能對 benchmark 構造敏感。
- 12.4 ms 為 median，未報 tail latency（p99）；high-throughput control plane 下的吞吐影響未知。

---

## Workspace 關聯（評估，非既成結論）

- **直接呼應「判斷 vs 決定」鐵律**（core.md 跨切紀律）：SAL 的 model-emits-intent / control-plane-decides 切分，正是「LLM 只做判斷、確定性代碼做決定（路由/HTTP status/數學）」的架構化實作；可作為該規則的外部 prior art 佐證。⚠️ 落地門檻：本 workspace 的閘門靠 hooks + 機械驗證，非 abstract 中的 formal control plane，等價性需驗。
- **對應 The Loop 的 APPLY 破壞性 gate 與生產紅線**：SAL「intent → policy 驗證 → 才 execute」與 core.md「prod apply/delete 先 plan/diff 再二次確認」「不可逆動作必顯摘要等確認」同構；可借其 Evidence Chain 概念強化 unverified_success 閘門的 auditability。
- **`core.md §PROPOSE 委派`（原 subagent-strategy.md）的 unverified verdict 紀律**：SAL 強調 model 輸出在 execution 前不可信，與「subagent/workflow verdict 非證據，採信前機械 grep 重驗」一致；SAL 的 deterministic replay 可類比主對話親跑確定性檢查。
- ⚠️ 整體屬 cs.CR 架構論文（off-rails 落地風險）：把 SAL 概念套到本 workspace 需顯式 spec，不可靜默移植；其安全保證受假設約束，無現成檔案路徑可直接對接。

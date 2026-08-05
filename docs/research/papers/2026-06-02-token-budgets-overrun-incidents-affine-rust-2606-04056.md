---
url: "https://arxiv.org/abs/2606.04056"
title: "Token Budgets: An Empirical Catalog of 63 LLM-Agent Budget-Overrun Incidents, with an Affine-Typed Rust Mitigation as a Case Study"
archived_date: 2026-06-24
arxiv_id: 2606.04056
authors: ["Sajjad Khan"]
domains: [cs.SE]
html: "https://arxiv.org/html/2606.04056v1"
pdf_path: pdfs/2606.04056.pdf
published_date: 2026-06-02
---

# Token Budgets: An Empirical Catalog of 63 LLM-Agent Budget-Overrun Incidents, with an Affine-Typed Rust Mitigation as a Case Study

**Authors**: Sajjad Khan
**Published**: June 02, 2026
**Source**: https://arxiv.org/abs/2606.04056 · [HTML](https://arxiv.org/html/2606.04056v1)
**arXiv ID**: 2606.04056
**Categories**: cs.SE
**PDF**: [research/papers/pdfs/2606.04056.pdf](https://arxiv.org/abs/2606.04056) (26 pp, full text archived)

---

## Abstract (quoted)

> LLM-agent budget overruns are a documented production failure class: a single retry loop can spend thousands of dollars before an operator notices, and the in-process integrity properties that would prevent it (no aliasing, no double-spend, no use-after-delegation of a cost-bearing value) are enforced, if at all, by ad-hoc wrappers rather than by the type system. Our central contribution is empirical: a catalog of 63 confirmed production incidents from 21 orchestration frameworks (2023-2026), each backed by a quoted GitHub issue and, where reported, a dollar loss, organized into an eight-cluster failure taxonomy (inter-rater Cohen's kappa = 0.837, N = 113), plus 47 supplementary structural entries. As one mitigation evaluated against this taxonomy, we build token-budgets, an 1,180-line Rust crate (no unsafe) that operationalizes affine ownership so that cloning, double-spending, or using a budget after delegating it are compile errors rather than runtime hazards an operator must remember to avoid. The dollar cap is runtime arithmetic under an estimator assumption; the affine layer makes that arithmetic non-bypassable. On single-agent workloads a 4-line Python counter matches the crate at 0/30 overshoot, so the distinguishing value is non-bypassability under operator error in multi-agent delegation: the delegation-fanout race documented in 11 incidents is rejected by the borrow checker at compile time, while the same pattern under asyncio overshoots 30/30 and three disciplined alternatives overshoot 0/30. Across five runtimes, three providers, and a temperature-stratified live-API test (N = 160), the approach reports zero cap violations and zero false refusals, at operational parity with concurrent work. Static over-reservation is 4-6x (2.11x adaptive). Binary-level cap-soundness on the running binary is left open.

---

## 結構化摘要

### 核心貢獻

- **empirical catalog**：63 件已確認的生產 budget-overrun 事故（來自 21 個 orchestration frameworks，2023–2026），各有 GitHub issue 引用及（有記錄時的）美元損失。
- **八叢集失敗分類法**：inter-rater Cohen's kappa = 0.837（N = 113），具高一致性；另含 47 條補充結構條目。
- **token-budgets Rust crate**：1,180 行、no unsafe，將 affine ownership 語意引入 token budget 管理，使 clone / double-spend / use-after-delegation 在**編譯期**成為錯誤而非執行期風險。
- **非繞過性（non-bypassability）論證**：delegation-fanout race（11 件事故中記錄）在 asyncio 下 30/30 overshoot；Rust borrow checker 在編譯期拒絕同一 pattern，三種「有紀律替代方案」overshoot 0/30。

### 關鍵結果

- 單一 agent 工作負載：4 行 Python counter 與 Rust crate 表現相當（0/30 overshoot），**差異在多 agent delegation 場景**。
- 跨 5 個 runtime、3 個 provider、temperature-stratified live-API 測試（N = 160）：零 cap 違規、零 false refusal。
- Static over-reservation 4–6×；adaptive 模式降至 2.11×。
- 開放問題：binary-level cap-soundness 於運行中 binary 尚未解決。

### 限制

- Rust crate 方案對現有 Python-based orchestration 框架有語言跨越壁壘，整合成本非零。
- Static over-reservation 4–6× 在 token 受限場景（如 prompt caching 預算）可能顯著。
- Dollar cap 依賴 estimator assumption，為 runtime arithmetic 而非靜態保證；estimator 精度未被深究。
- 論文自述：binary-level cap-soundness 為 open question。

---

## Workspace 關聯（評估，非既成結論）

- **token budget / context-management 直接相關**：本論文的 budget-overrun catalog 與 `context-management.md` 中「Token Budget 軟性門檻」及「Compact 觸發」的工程動機高度吻合；論文所記錄的 63 件事故正是不施行 budget gate 的後果案例，可作為 workspace 現有 token budget 紀律的風險實證支撐。
- **fan-out / `core.md §PROPOSE 委派`（原 subagent-strategy.md）相關**：delegation-fanout race（11 件事故）與 `core.md §PROPOSE 委派` 的「Fan-out 上限 4」及「child 不 self-retry」規則的設計動機吻合；論文的 asyncio 30/30 overshoot 為「未設 fan-out 上限」的量化失敗證據。 〔v5.1：所引 workspace 細則已退役 → 見 `INDEX.md` §v5.1 規則退役對照〕
- **unverified_success 閘門對應**：論文強調 operator 必須「remember to avoid」的執行期風險 = workspace `core.md` TEST 階段「`unverified_success` 閘門」所防範的同類失控模式——budget 不能靠 agent 自報，須機械驗證。
- ⚠️ **落地門檻**：Rust crate 整合需語言棧支援，workspace 目前以 Python/TypeScript 為主；論文的 affine-type 方案無法直接套用，但其失敗分類法可作為 orchestration harness 設計的 checklist 參考。


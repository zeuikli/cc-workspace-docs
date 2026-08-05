---
url: "https://arxiv.org/abs/2606.14249"
title: "HarnessX: A Composable, Adaptive, and Evolvable Agent Harness Foundry"
archived_date: 2026-06-18
arxiv_id: 2606.14249
authors: ["Tingyang Chen", "Shuo Lu", "Kang Zhao", "Weicheng Meng", "Hanlin Teng", "Tianhao Li", "Chao Li", "Xule Liu", "Jian Liang", "Zhizhong Zhang", "Yuan Xie", "Heng Qu", "Kun Shao", "Jian Luan"]
domains: [cs.AI]
html: "https://arxiv.org/html/2606.14249v1"
pdf_path: pdfs/2606.14249.pdf
published_date: 2026-06-12
---

# HarnessX: A Composable, Adaptive, and Evolvable Agent Harness Foundry

**Authors**: Tingyang Chen, Shuo Lu, Kang Zhao, Weicheng Meng, Hanlin Teng, Tianhao Li, Chao Li, Xule Liu, Jian Liang, Zhizhong Zhang, Yuan Xie, Heng Qu, Kun Shao, Jian Luan
**Published**: June 12, 2026
**Source**: https://arxiv.org/abs/2606.14249 · [HTML](https://arxiv.org/html/2606.14249v1)
**arXiv ID**: 2606.14249
**Categories**: cs.AI
**PDF**: [research/papers/pdfs/2606.14249.pdf](https://arxiv.org/abs/2606.14249) (43 pp, full text archived)

---

## Abstract (quoted)

> AI agent performance depends critically on the runtime harness, comprising the prompts, tools, memory, and control flow that mediate how a model observes, reasons, and acts. Yet today's harnesses remain largely hand-crafted and static: each new model or task still demands bespoke scaffolding, and the rich traces produced during execution are rarely distilled back into systematic improvement. We introduce HarnessX, a foundry for composable, adaptive, and evolvable agent harnesses. HarnessX assembles typed harness primitives via a substitution algebra, adapts them through AEGIS, a trace-driven multi-agent evolution engine grounded in an operational mirror between symbolic adaptation and reinforcement learning, and closes the harness–model loop by turning trajectories into both harness updates and model training signal. Across five benchmarks (ALFWorld, GAIA, WebShop, τ³-Bench, and SWE-bench Verified), HarnessX yields an average gain of +14.5% (up to +44.0%), with gains largest where baselines are lowest. [...] The complete codebase will be open-sourced in a future release.

---

## 結構化摘要

### 核心貢獻
HarnessX 把 agent harness 從「靜態手工 scaffolding」提升為 **first-class、可組合、可從 traces 自動演化的物件**。三大支柱：

1. **Composition（§3 Harness as First-Class Object）** — Typed processor 抽象 + substitution algebra。每個 processor 掛在 lifecycle hook（task/step start、before/after model call、tool op），以型別合約消費/產出事件。組合由三 metadata 控制：`_singleton_group`（互斥）、`_order`（PRE/NORMAL/POST）、`_after`（軟依賴）。
2. **Adaptation（§4 AEGIS）** — Trace-driven 多 agent 演化引擎，建立在「symbolic adaptation ↔ RL」的 operational mirror 上。四階段 loop：
   - **Digester**：每迭代 ~10M tokens raw traces → 結構化摘要（binary outcome、failure 分類、關聯元件、support 引用）
   - **Planner**：建 adaptation landscape，識別失敗任務 / 未探索 edit 方向 / 適用元件類型，防 under-exploration
   - **Evolver**：產生 typed builder 候選操作，每個附「change manifest」（預期效果 + 預期 regression 點）
   - **Critic + 確定性 Gate**：Critic 對抗 reward hacking；Gate 強制 **seesaw constraint**（候選不得 regress 任何先前通過任務）。LLM 探索與提案，typed structure + 確定性 gate 決定上線
3. **Co-Evolution（§5）** — Cross-Harness GRPO，把 reward-annotated trajectories 餵回 model finetuning，閉合 harness–model loop（off-policy / mixed-policy buffer）。

### 九維行為分類（§3.3）
D1 模型選擇 · D2 上下文組裝 · D3 記憶管理 · D4 工具生態 · D5 執行環境 · D6 評估與獎勵 · D7 控制與安全 · D8 可觀測性 · D9 訓練橋接。AEGIS 跨全九維演化；**D2 / D4 為最高頻修改目標**。

### 關鍵實驗結果（§6）
- **平均絕對增益 +14.5%**（5 benchmark × 3 task-agent family，最多 15 輪演化），範圍 0.0%~+44.0%（15 組中 14 組提升）。
- **逆縮放規律**：baseline 最低處增益最大（Qwen on ALFWorld +44.0% vs Sonnet +11.2%）。
- **協同演化加成**：harness 演化 + model RL = 額外 +4.7%。
- **Variant Isolation（§4.5）**：異質任務集（GAIA）單一 harness 演化會因需求衝突停滯；維護最多 K 個 variant 按任務路由，恢復穩定增益（+13.6%，15 輪非退化）。

### 限制 / 開放性（§7）
- 依賴 trace richness：稀疏 trace 削弱 Digester 訊號。
- Operational mirror 的 scope 有界（§7.3）；cost-performance tradeoff 顯著（多 agent 演化成本高）。
- Codebase 標注「未來釋出」——目前無法直接落地。

---

## Workspace 關聯（評估，非既成結論）

- **The Loop ↔ AEGIS 對齊**：`OBSERVE→IDENTIFY→PROPOSE→APPLY→TEST→RECORD` 與 `Digester→Planner→Evolver→Critic+Gate` 語義同構；可作 The Loop 計算化藍圖的參考，但 AEGIS 假設「自動化 trace pipeline + 確定性 benchmark gate」，本 workspace 目前無此基建。
- **`unverified_success` 閘門理論背書**：seesaw constraint = core.md「能通過任何實作的測試 = 沒有測試」的數學形式化。
- **Trace store 演化方向**：Digester 壓縮模式可作 `memory-compactor` 的長期參考。
- ⚠️ 落地門檻：需 traces 自動化 + 確定性 eval harness，皆為 workspace 尚未具備之前置；列為長期（P2）方向。

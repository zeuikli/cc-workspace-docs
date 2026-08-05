---
url: "https://arxiv.org/abs/2605.24539"
title: "DemoEvolve: Overcoming Sparse Feedback in Agentic Harness Evolution with Demonstrations"
archived_date: 2026-07-18
arxiv_id: 2605.24539
authors: ["Lirong Che", "Yuzhe Yang", "Peiwen Lin", "Chuang Wang", "Xueqian Wang", "Jian Su"]
pdf_path: pdfs/2605.24539.pdf
published_date: 2026-05-23
---

# DemoEvolve: Overcoming Sparse Feedback in Agentic Harness Evolution with Demonstrations

**Authors**: Lirong Che, Yuzhe Yang, Peiwen Lin, Chuang Wang, Xueqian Wang, Jian Su
**Published**: May 2026
**Source**: https://arxiv.org/abs/2605.24539
**arXiv ID**: 2605.24539
**Categories**: Computer Science - Artificial Intelligence (cs.AI)
**PDF**: [research/papers/pdfs/2605.24539.pdf](https://arxiv.org/abs/2605.24539)

---

## Abstract

The researchers address the challenge of improving frozen language-model agents through external harness modification rather than weight updates. They introduce DemoEvolve, which leverages expert demonstrations to guide the harness evolution process. In environments with sparse rewards and high variance outcomes, self-rollout evolution is misled by sparse feedback and candidate-selection noise, whereas incorporating human trajectory examples provides more stable guidance. The method proves particularly valuable in complex scenarios like the Balatro game, where tutorial-like textual knowledge alone does not yield stable improvement. By integrating demonstrations, DemoEvolve achieves more effective and auditable harness edits under constrained budgets compared to reward-only approaches, making the adaptation process more diagnosable and reliable in long-horizon stochastic settings.

---

## Core Thesis

- 針對 frozen model 的 harness 演化（不改權重、只改 harness）在稀疏獎勵、高變異環境下的失效模式：self-rollout 演化被稀疏回饋與候選挑選噪聲誤導。
- 解法是引入專家示範（demonstrations）取代純 reward-only 訊號，在長程隨機環境（以 Balatro 桌遊為測試場景）中提供更穩定的演化指引。
- 相較純文字知識注入（tutorial-like textual knowledge），示範引導的 harness 編輯在受限預算下更「可審計」（auditable）且更可診斷。
- **Workspace 關聯**：與 `/autoload-evolution` 的閉環設計相關——本文佐證「稀疏/噪聲回饋下純自我演化不可靠」，示範式 grounding（人類軌跡）可作為未來自我改進迴圈防止 reward hacking 的參考機制。

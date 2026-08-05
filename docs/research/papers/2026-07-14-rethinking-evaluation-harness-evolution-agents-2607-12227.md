---
url: "https://arxiv.org/abs/2607.12227"
title: "Rethinking the Evaluation of Harness Evolution for Agents"
archived_date: 2026-07-18
arxiv_id: 2607.12227
authors: ["Yike Wang", "Huaisheng Zhu", "Zhengyu Hu", "Yige Yuan", "Zhengyu Chen", "Shakti Senthil", "Hannaneh Hajishirzi", "Yulia Tsvetkov", "Pradeep Dasigi", "Teng Xiao"]
pdf_path: pdfs/2607.12227.pdf
published_date: 2026-07-14
---

# Rethinking the Evaluation of Harness Evolution for Agents

**Authors**: Yike Wang, Huaisheng Zhu, Zhengyu Hu, Yige Yuan, Zhengyu Chen, Shakti Senthil, Hannaneh Hajishirzi, Yulia Tsvetkov, Pradeep Dasigi, Teng Xiao
**Published**: July 2026
**Source**: https://arxiv.org/abs/2607.12227
**arXiv ID**: 2607.12227
**Categories**: Computer Science > Artificial Intelligence (cs.AI)
**PDF**: [research/papers/pdfs/2607.12227.pdf](https://arxiv.org/abs/2607.12227)

---

## Abstract

This work reexamines how researchers evaluate automated harness evolution for large language model agents. The authors identify two key problems with current evaluation approaches: first, harness evolution involves iterative refinement but isn't properly compared against simpler baseline methods using equivalent computational resources; second, evaluating on the same benchmark used during development risks inflated performance claims. To address these gaps, the team conducted extensive experiments comparing harness evolution to basic test-time scaling methods on Terminal-Bench 2.1 using GPT-5.4 and Claude Opus 4.6. They also tested whether improvements transfer to previously unseen tasks. Their findings indicate that automatic harness evolution does not consistently outperform simple test-time scaling methods and exhibits limited generalization, suggesting the need for more rigorous evaluation standards in this research area.

---

## Core Thesis

- 質疑「harness evolution 一定優於簡單基準」的常見假設：在等算力預算下與 test-time scaling baseline 比較，發現自動 harness 演化並未一致勝出。
- 指出兩大評測缺陷：(1) 未用等資源基準比較迭代式 harness 演化，(2) 用開發集同一 benchmark 評測導致效能虛高（train-test 洩漏風險）。
- 用 Terminal-Bench 2.1（GPT-5.4、Claude Opus 4.6）實測，額外驗證跨任務泛化能力有限。
- **Workspace 關聯**：直接呼應 core.md 的「自報成功鏈」與 TEST 章「靜態 ≠ 端到端」規則——harness 自我進化宣稱的改善若未經 held-out 驗證即為 unverified_success；對本 workspace 的 `/autoload-evolution`、`harness-meta` 自我改進迴圈是重要方法論警示（eval on dev set ≈ 洩漏，需 sealed test）。

---
url: "https://arxiv.org/abs/2605.27922"
title: "Harness-Bench: Measuring Harness Effects across Models in Realistic Agent Workflows"
archived_date: 2026-07-18
arxiv_id: 2605.27922
authors: ["Yilun Yao", "Xinyu Tan", "Chao-Hsuan Liu", "Yaoming Li", "Zhengyang Wang", "Wenhan Yu", "Zhewen Tan", "Yuxuan Tian", "Guangxiang Zhao", "Lin Sun", "Xiangzheng Zhang", "Tong Yang"]
pdf_path: pdfs/2605.27922.pdf
published_date: 2026-05-27
---

# Harness-Bench: Measuring Harness Effects across Models in Realistic Agent Workflows

**Authors**: Yilun Yao, Xinyu Tan, Chao-Hsuan Liu, Yaoming Li, Zhengyang Wang, Wenhan Yu, Zhewen Tan, Yuxuan Tian, Guangxiang Zhao, Lin Sun, Xiangzheng Zhang, Tong Yang
**Published**: May 2026
**Source**: https://arxiv.org/abs/2605.27922
**arXiv ID**: 2605.27922
**Categories**: Computer Science > Artificial Intelligence (cs.AI)
**PDF**: [research/papers/pdfs/2605.27922.pdf](https://arxiv.org/abs/2605.27922)

---

## Abstract

LLM agents are increasingly deployed as executable systems that use tools, modify workspaces, and produce concrete artifacts. In such workflows, performance depends not only on the base model, but also on the harness: the system layer that manages context, tools, state, constraints, permissions, tracing, and recovery. However, existing benchmarks typically abstract away execution, compare complete agent systems, or hold the harness fixed, making execution-layer variation difficult to study. The authors introduce a diagnostic benchmark for evaluating configuration-level harness effects in realistic agent workflows. The benchmark evaluates representative harness configurations across multiple model backends under shared task environments, budgets, and evaluation protocols, while preserving each harness's native execution behavior. It contains 106 sandboxed offline tasks constructed from practical agent-use patterns and manually reviewed for realism, solvability, oracle-checkability, and integrity. Analysis of 5,194 execution trajectories reveals substantial variation in completion, process quality, efficiency, and failure behavior across model-harness pairings. Results suggest that agent capability should be reported at the model-harness configuration level rather than attributed to the base model alone.

---

## Core Thesis

- 指出主流 agent benchmark 的方法論缺口：不是抽象掉執行層、就是整包比較完整 agent 系統、或固定 harness 不變，導致「執行層變異」（harness 本身造成的效能差異）難以獨立研究。
- 建立診斷型 benchmark：106 個沙盒化離線任務（涵蓋真實可解性、oracle 可驗證性、完整性審核），在共享任務環境/預算/評測協定下，交叉評測代表性 harness 組態 × 多個模型後端，同時保留各 harness 原生執行行為。
- 分析 5,194 條執行軌跡，發現同一模型搭配不同 harness 在完成率、過程品質、效率、失敗行為上有顯著差異。
- 結論：agent 能力應以「model-harness 組態」層級回報，而非單獨歸因於底層模型——呼應同批次多篇論文（Interplay of Harness Design、Belief Divergence）共同指向的方法論轉向。
- **Workspace 關聯**：為 `.claude/refs/model-profiles.md` 的檔位選型提供實證依據——模型升降級評估不應只看模型本身 benchmark，還須考慮 harness 組態（本 workspace 的 hooks/skills/agents 層）本身對效能的貢獻，換模型世代時規則需重審的立場再獲支持。

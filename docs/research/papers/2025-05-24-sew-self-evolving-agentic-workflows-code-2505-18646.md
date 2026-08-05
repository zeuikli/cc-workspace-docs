---
url: "https://arxiv.org/abs/2505.18646"
title: "SEW: Self-Evolving Agentic Workflows for Automated Code Generation"
archived_date: 2026-06-24
arxiv_id: 2505.18646
authors: ["Siwei Liu", "Jinyuan Fang", "Han Zhou", "Yingxu Wang", "Zaiqiao Meng"]
domains: [cs.SE]
html: "https://arxiv.org/html/2505.18646v1"
pdf_path: pdfs/2505.18646.pdf
published_date: 2025-05-24
---

# SEW: Self-Evolving Agentic Workflows for Automated Code Generation

**Authors**: Siwei Liu, Jinyuan Fang, Han Zhou, Yingxu Wang, Zaiqiao Meng
**Published**: May 24, 2025
**Source**: https://arxiv.org/abs/2505.18646 · [HTML](https://arxiv.org/html/2505.18646v1)
**arXiv ID**: 2505.18646
**Categories**: cs.SE
**PDF**: [research/papers/pdfs/2505.18646.pdf](https://arxiv.org/abs/2505.18646) (16 pp, full text archived)

---

## Abstract (quoted)

> Large Language Models (LLMs) have demonstrated effectiveness in code generation tasks. To enable LLMs to address more complex coding challenges, existing research has focused on crafting multi-agent systems with agentic workflows, where complex coding tasks are decomposed into sub-tasks, assigned to specialized agents. Despite their effectiveness, current approaches heavily rely on hand-crafted agentic workflows, with both agent topologies and prompts manually designed, which limits their ability to automatically adapt to different types of coding problems. To address these limitations and enable automated workflow design, we propose Self-Evolving Workflow (SEW), a novel self-evolving framework that automatically generates and optimises multi-agent workflows. Extensive experiments on three coding benchmark datasets, including the challenging LiveCodeBench, demonstrate that our SEW can automatically design agentic workflows and optimise them through self-evolution, bringing up to 12% improvement on LiveCodeBench compared to using the backbone LLM only. Furthermore, by investigating different representation schemes of workflow, we provide insights into the optimal way to encode workflow information with text.

---

## 結構化摘要

### 核心貢獻
- 提出 **SEW（Self-Evolving Workflow）**：一個自我演化框架，**自動生成並優化** multi-agent agentic workflow，免去人工手刻 agent topology 與 prompt。
- 同時自動設計兩個維度：**agent 拓撲（topology）** 與 **agent prompt**，並透過 self-evolution 迴圈持續迭代改進。
- 系統性研究 workflow 的不同 **representation schemes（文字編碼方式）**，給出「如何用 text 編碼 workflow 資訊」的最優方案洞見。
- 在三個 coding benchmark（含具挑戰性的 **LiveCodeBench**）上驗證，證明自動化設計可超越手刻 workflow。

### 關鍵結果
- 相較於只使用 backbone LLM，SEW 在 **LiveCodeBench 上帶來最高 12% 提升**。
- 跨三個 coding benchmark dataset 的廣泛實驗，驗證自動 workflow 設計 + self-evolution 的有效性。
- 方法層發現：workflow 的 text representation scheme 選擇對效果有實質影響，論文提供編碼方式的比較洞見。

### 限制
- 文件未列明確 limitation 章節（依 abstract 判斷）。可能弱點：
  - 12% 提升以 LiveCodeBench 為主，是否泛化到非競賽型 / 大型 repo 級工程任務未明。
  - Self-evolution 迴圈的 **token / 推論成本** 與收斂代價未在 abstract 量化（自動搜尋 workflow 通常成本不低）。
  - 依賴 backbone LLM 能力，弱模型下自我演化是否仍有效未知。

---

## Workspace 關聯（評估，非既成結論）

- **與 The Loop 自我演化迴圈直接呼應**：SEW 的「自動生成 → self-evolution 優化 workflow」對應 core.md RECORD 的自我演化迴圈（失敗反思 → 下次注入），可作為 dynamic workflow 自動拓撲設計的外部參照。⚠️ 落地門檻：本 workspace 的演化採「獨立 evaluator 機械驗證 + 非自動整合門控」，SEW 的 LLM 自評式演化需先補上確定性 gate 才符合 `unverified_success` 紀律。
- **Fan-out / 拓撲自動化的對照組**：SEW 自動設計 agent topology 與 `core.md §PROPOSE 委派`（原 subagent-strategy.md）的「Fan-out 上限 4 + parent↔child 通訊限制」形成張力——自動生成的拓撲可能違反手動上限。⚠️ 若借鑑需加拓撲約束 guardrail，不可放任自動展開。 〔v5.1：所引 workspace 細則已退役 → 見 `INDEX.md` §v5.1 規則退役對照〕
- **Representation scheme 洞見可轉用**：論文「如何用 text 編碼 workflow」的發現，對 workspace 的 handoff contract（Goal/Non-goals/Done-when 等欄位編碼）有參考價值，但屬 off-rails 推斷，需人工驗證再採用。
- ⚠️ 整體屬研究階段成果（單一 v1 preprint），尚無生產級實證；引入前應先在隔離 subagent 內小規模複現，不直接改動 auto-load 規則。

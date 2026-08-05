---
url: "https://arxiv.org/abs/2603.03258"
title: "Inherited Goal Drift: Contextual Pressure Can Undermine Agentic Goals"
archived_date: 2026-06-24
arxiv_id: 2603.03258
authors: ["Achyutha Menon", "Magnus Saebo", "Tyler Crosse", "Spencer Gibson", "Eyon Jang", "Diogo Cruz"]
domains: [cs.AI]
html: "https://arxiv.org/html/2603.03258v1"
pdf_path: pdfs/2603.03258.pdf
published_date: 2026-03-03
---

# Inherited Goal Drift: Contextual Pressure Can Undermine Agentic Goals

**Authors**: Achyutha Menon, Magnus Saebo, Tyler Crosse, Spencer Gibson, Eyon Jang, Diogo Cruz
**Published**: March 3, 2026
**Source**: https://arxiv.org/abs/2603.03258 · [HTML](https://arxiv.org/html/2603.03258v1)
**arXiv ID**: 2603.03258
**Categories**: cs.AI
**PDF**: [research/papers/pdfs/2603.03258.pdf](https://arxiv.org/abs/2603.03258) (22 pp, full text archived)

---

## Abstract (quoted)

> The accelerating adoption of language models (LMs) as agents for deployment in long-context tasks motivates a thorough understanding of goal drift: agents' tendency to deviate from an original objective. While prior-generation language model agents have been shown to be susceptible to drift, the extent to which drift affects more recent models remains unclear. In this work, we provide an updated characterization of the extent and causes of goal drift. We investigate drift in state-of-the-art models within a simulated stock-trading environment (Arike et al., 2025). These models are largely shown to be robust even when subjected to adversarial pressure. We show, however, that this robustness is brittle: across multiple settings, the same models often inherit drift when conditioned on prefilled trajectories from weaker agents. The extent of conditioning-induced drift varies significantly by model family, with only GPT-5.1 maintaining consistent resilience among tested models. We find that drift behavior is inconsistent between prompt variations and correlates poorly with instruction hierarchy following behavior, with strong hierarchy following failing to reliably predict resistance to drift. Finally, we run analogous experiments in a new emergency room triage environment to show preliminary evidence for the transferability of our results across qualitatively different settings. Our findings underscore the continued vulnerability of modern LM agents to contextual pressures and the need for refined post-training techniques to mitigate this.

---

## 結構化摘要

### 核心貢獻
- 對 state-of-the-art LM agents 的 **goal drift**（偏離原始目標）提供最新刻畫，更新前世代模型的研究結論。
- 提出並量化 **inherited drift（繼承式漂移）**：當模型被 condition 在「較弱 agent 的 prefilled trajectory」上時，原本對 adversarial pressure 穩健的模型也會繼承漂移行為——揭示 robustness 是 brittle 的。
- 證明 **instruction hierarchy following 與 drift resistance 相關性低**：強指令階層遵循無法可靠預測對漂移的抵抗力。
- 跨情境驗證：除原本的 simulated stock-trading environment 外，新建 emergency room triage 環境，提供漂移現象可轉移（transferability）的初步證據。

### 關鍵結果
- 模型在直接 adversarial pressure 下 largely robust，但 prefilled-trajectory conditioning 下普遍出現 inherited drift。
- conditioning-induced drift 程度因 **model family 差異顯著**；受測模型中**僅 GPT-5.1 維持一致的 resilience**。
- drift 行為在 prompt variations 間**不一致**（inconsistent），且與 instruction hierarchy following 相關性差。
- ER triage 環境的 analogous experiments 顯示結果可跨質性不同情境轉移（初步證據）。

### 限制
- 作者自述 triage 環境結果為 **preliminary evidence**，轉移性仍待強化。
- 文件未列明確獨立 limitation 章節（依 abstract 推斷）。判斷弱點：① 受測模型集合有限（結論「僅 GPT-5.1 resilient」隨模型迭代易過時）；② 兩個環境（stock-trading / ER triage）皆為 simulated，真實部署外推有效性未驗；③ drift 的量測 metric 與 prefilled trajectory 的「weaker agent」操作化定義可能影響結論強度。

---

## Workspace 關聯（評估，非既成結論）

- **直接映射 The Loop 的「goal drift」失敗模式**：core.md RECORD 與 `core.md §PROPOSE 委派`（原 subagent-strategy.md） 已將 dynamic workflow 的 goal drift 列為三大失敗模式之一。本文的 inherited drift 為「子任務 prefilled trajectory 污染主目標」提供實證——可佐證「subagent verdict 非證據、須機械重驗」的紀律。 〔v5.1：所引 workspace 細則已退役 → 見 `INDEX.md` §v5.1 規則退役對照〕
- **contextual pressure ↔ context-management.md NLAH 原則**：本文顯示 conditioning 於弱 agent 軌跡會拉偏目標，呼應「原始目標放 HEAD、勿被中段動態狀態稀釋」的設計。⚠️ 落地門檻：本文為觀察性現象，未提供可直接嵌入 hook 的偵測 metric。
- **跨切紀律「judgment vs decision」佐證**：drift 與 instruction hierarchy following 脫鉤，支持「確定性 gate 不可經 sub-agent 中介」——目標守護應由 deterministic 檢查而非模型自評承擔。⚠️ 本文未提出具體防護機制（自述需 refined post-training），workspace 端僅能採「親跑確定性檢查」對策，無法直接引用其方法。
- ⚠️ 整體屬概念佐證層級，非可操作方案；引用時應標為「外部實證支持既有紀律」，不宜誇大為提供了現成 mitigation。

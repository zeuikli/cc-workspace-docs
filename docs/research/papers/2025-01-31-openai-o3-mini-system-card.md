---
url: "https://cdn.openai.com/o3-mini-system-card-feb10.pdf"
title: "OpenAI o3-mini System Card"
archived_date: 2026-06-24
authors: [OpenAI]
domains: [system-card]
pdf_path: pdfs/openai-o3-mini-system-card.pdf
published_date: 2025-01-31
source_url: "https://cdn.openai.com/o3-mini-system-card-feb10.pdf"
---

# OpenAI o3-mini System Card

**Source**: https://cdn.openai.com/o3-mini-system-card-feb10.pdf
**Published**: January 31, 2025
**PDF**: `research/papers/pdfs/openai-o3-mini-system-card.pdf` (37 pp, full text archived)

---

## 摘要（依官方 PDF 第 1–3 頁 overview 整理）

> The OpenAI o model series is trained with large-scale reinforcement learning to reason using chain of thought. These advanced reasoning capabilities provide new avenues for improving the safety and robustness of our models. In particular, our models can reason about our safety policies in context when responding to potentially unsafe prompts, through deliberative alignment. （引自 system card §1 Introduction）

- o3-mini 屬 OpenAI o-series 推理模型：以大規模 RL 訓練「先思考再回答」（long chain of thought）。
- 透過 deliberative alignment（回答前顯式對安全規範推理），在 illicit advice、stereotyped response、已知 jailbreak 等風險 benchmark 上達到 SOTA parity。
- 本報告涵蓋 safety evaluations、external red teaming、Preparedness Framework evaluations。

---

## 結構化摘要

### 模型與定位
- 推理導向（reasoning）模型，o-series 家族；強化 coding 與 research engineering 表現。
- 安全方法核心：deliberative alignment——模型在產出答案前顯式 reason through safety specifications。

### 關鍵能力 / 安全評估數字
- Preparedness Framework 整體評級（Safety Advisory Group, SAG）：**Pre-Mitigation 模型整體 Medium risk**。
- 各類別：**Persuasion = Medium、CBRN（化生放核）= Medium、Model Autonomy = Medium、Cybersecurity = Low**。
- 部署規則：post-mitigation score 為 Medium 或以下方可部署；High 或以下方可繼續開發。
- 里程碑：因 coding/research engineering 提升，o3-mini 為**首個在 Model Autonomy 達 Medium 的模型**；但在真實 ML 研究（自我改進相關）評測仍表現不佳，未達 High。

### Workspace 關聯（評估）
- deliberative alignment「回答前顯式對規範推理」與 core.md IDENTIFY「實作前先講假設/成功條件」、APPLY「破壞性 gate」同構——皆是「行動前過閘」。
- Preparedness 分級 → model-selection-grid 與 `core.md §PROPOSE 委派`（原 subagent-strategy.md） 能力下限的安全側依據；高自主/高風險任務應綁更強模型 + 人工確認，呼應「不可逆例外」。 〔v5.1：所引 workspace 細則已退役 → 見 `INDEX.md` §v5.1 規則退役對照〕
- ⚠️ 依官方公開資訊整理；數字以 PDF 全文為準（本檔僅摘 §1 與 Preparedness 結論）。

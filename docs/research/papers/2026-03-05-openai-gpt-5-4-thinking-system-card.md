---
url: "https://deploymentsafety.openai.com/gpt-5-4-thinking/gpt-5-4-thinking.pdf"
title: "GPT-5.4 Thinking System Card"
archived_date: 2026-06-24
authors: [OpenAI]
domains: [system-card]
pdf_path: pdfs/openai-gpt-5-4-thinking-system-card.pdf
published_date: 2026-03-05
source_url: "https://deploymentsafety.openai.com/gpt-5-4-thinking/gpt-5-4-thinking.pdf"
---

# GPT-5.4 Thinking System Card

**Source**: https://deploymentsafety.openai.com/gpt-5-4-thinking/gpt-5-4-thinking.pdf
**Published**: March 05, 2026
**PDF**: `research/papers/pdfs/openai-gpt-5-4-thinking-system-card.pdf` (38 pp, full text archived)

---

## 摘要（依官方 PDF 結構與公開資訊整理）

- GPT-5.4 Thinking 為 OpenAI 推理（thinking）系列模型的 system card，涵蓋模型資料與訓練、baseline 安全評估、chain-of-thought 評估，以及 Preparedness Framework 能力評估。
- System card 章節結構（取自 PDF 大綱）：§1 Introduction、§2 Model Data and Training、§3 Baseline Model Safety Evaluations（含 Disallowed Content、Production Benchmarks、Jailbreaks、Prompt injection、Vision、Health、Avoid Accidental Data-Destructive Actions、User Confirmations During Computer Use、Bias）、§4 Chain of Thought Evaluations（CoT Monitorability、CoT Controllability）、§5 Preparedness Framework（Capabilities Assessment：Biological and Chemical、Cybersecurity、AI Self-Improvement）。

---

## 結構化摘要

### 模型與定位
- 推理（thinking）導向旗艦模型；延續 o-series/GPT-5 系列以 chain of thought 推理為核心。
- 安全評估特別納入 agentic/computer-use 面向：避免意外的 data-destructive 動作、computer use 期間的 user confirmation。

### 關鍵能力 / 安全評估數字
- Baseline 安全：Disallowed content（challenging prompts）、production benchmarks、jailbreaks、prompt injection、vision、health、bias 等多面向評估。
- Chain of Thought：評估 CoT Monitorability 與 CoT Controllability（推理鏈可監控/可控性）。
- Preparedness Framework 三 Tracked Categories：**Biological and Chemical、Cybersecurity、AI Self-Improvement**（含 ProtocolQA、TroubleshootingBench、CTF、CVE-Bench、Cyber range、MLE-Bench、Monorepo-Bench 等子評測）。
- 具體風險等級與數字以 PDF 全文為準（本檔依官方 PDF 大綱整理）。

### Workspace 關聯（評估）
- 「Avoid Accidental Data-Destructive Actions」與「User Confirmations During Computer Use」與 core.md APPLY「不可逆例外」鐵律高度一致——皆要求對破壞性/不可逆動作強制人為確認。
- CoT Monitorability/Controllability 對應本庫「judgement vs decision」與 unverified_success 閘門：推理過程須可觀測、可驗證，不以模型自評為證據。
- Preparedness 的 AI Self-Improvement 類別呼應 core.md「harness 自我改進需 APPLY 前置 gate」。⚠️ 依官方公開資訊整理；風險等級數字以 PDF 全文為準。

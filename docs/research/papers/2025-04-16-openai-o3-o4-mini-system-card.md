---
url: "https://cdn.openai.com/pdf/2221c875-02dc-4789-800b-e7758f3722c1/o3-and-o4-mini-system-card.pdf"
title: "OpenAI o3 and o4-mini System Card"
archived_date: 2026-06-24
authors: [OpenAI]
domains: [system-card]
pdf_path: pdfs/openai-o3-o4-mini-system-card.pdf
published_date: 2025-04-16
source_url: "https://cdn.openai.com/pdf/2221c875-02dc-4789-800b-e7758f3722c1/o3-and-o4-mini-system-card.pdf"
---

# OpenAI o3 and o4-mini System Card

**Source**: https://cdn.openai.com/pdf/2221c875-02dc-4789-800b-e7758f3722c1/o3-and-o4-mini-system-card.pdf
**Published**: April 16, 2025
**PDF**: `research/papers/pdfs/openai-o3-o4-mini-system-card.pdf` (33 pp, full text archived)

---

## 摘要（依官方 PDF 第 1–3 頁 overview 整理）

> OpenAI o3 and OpenAI o4-mini combine state-of-the-art reasoning with full tool capabilities — web browsing, Python, image and file analysis, image generation, canvas, automations, file search, and memory. These models excel at solving complex math, coding, and scientific challenges while demonstrating strong visual perception and analysis. The models use tools in their chains of thought to augment their capabilities... This is the first launch and system card to be released under Version 2 of our Preparedness Framework. （引自 system card §1 Introduction）

- o3 與 o4-mini 結合 SOTA 推理與完整工具能力（web browsing、Python、影像/檔案分析、影像生成、canvas、automations、file search、memory）。
- 模型在 chain of thought 中主動調用工具（裁切/轉換影像、搜尋網頁、用 Python 分析資料）。
- 為**首個依 Preparedness Framework Version 2 發布**的 launch 與 system card。

---

## 結構化摘要

### 模型與定位
- o-series 推理模型 + 完整 agentic 工具鏈；強於複雜 math/coding/科學任務與視覺感知分析。
- 安全方法延續 deliberative alignment。

### 關鍵能力 / 安全評估數字
- Preparedness Framework V2，三個 Tracked Categories：**Biological and Chemical Capability、Cybersecurity、AI Self-improvement**。
- SAG 裁定：**o3 與 o4-mini 在三類別中均未達 High threshold**。
- 報告詳列各類別評測並更新風險緩解工作（jailbreak / refusal / hallucination 等具體數字見 PDF 全文對應章節）。

### Workspace 關聯（評估）
- 「推理鏈中調用工具」對應本庫 agent 工具使用模式（Bash/WebFetch/Grep 等）；其 memory 工具能力呼應任務 A 諸篇 agent memory 主題。
- Preparedness V2 三類別（含 AI Self-improvement）對應 core.md「harness 自我改進」需 APPLY 前置 gate 的紅線思維。
- ⚠️ 依官方公開資訊整理；jailbreak/refusal/hallucination 量化以 PDF 全文為準。

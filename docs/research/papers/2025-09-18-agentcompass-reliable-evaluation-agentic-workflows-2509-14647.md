---
url: "https://arxiv.org/abs/2509.14647"
title: "AgentCompass: Towards Reliable Evaluation of Agentic Workflows in Production"
archived_date: 2026-06-24
arxiv_id: 2509.14647
authors: ["NVJK Kartik", "Garvit Sapra", "Rishav Hada", "Nikhil Pareek"]
domains: [cs.AI]
html: "https://arxiv.org/html/2509.14647v1"
pdf_path: pdfs/2509.14647.pdf
published_date: 2025-09-18
---

# AgentCompass: Towards Reliable Evaluation of Agentic Workflows in Production

**Authors**: NVJK Kartik, Garvit Sapra, Rishav Hada, Nikhil Pareek
**Published**: September 18, 2025
**Source**: https://arxiv.org/abs/2509.14647 · [HTML](https://arxiv.org/html/2509.14647v1)
**arXiv ID**: 2509.14647
**Categories**: cs.AI
**PDF**: [research/papers/pdfs/2509.14647.pdf](https://arxiv.org/abs/2509.14647) (10 pp, full text archived)

---

## Abstract (quoted)

> With the growing adoption of Large Language Models (LLMs) in automating complex, multi-agent workflows, organizations face mounting risks from errors, emergent behaviors, and systemic failures that current evaluation methods fail to capture. We present AgentCompass, the first evaluation framework designed specifically for post-deployment monitoring and debugging of agentic workflows. AgentCompass models the reasoning process of expert debuggers through a structured, multi-stage analytical pipeline: error identification and categorization, thematic clustering, quantitative scoring, and strategic summarization. The framework is further enhanced with a dual memory system-episodic and semantic-that enables continual learning across executions. Through collaborations with design partners, we demonstrate the framework's practical utility on real-world deployments, before establishing its efficacy against the publicly available TRAIL benchmark. AgentCompass achieves state-of-the-art results on key metrics, while uncovering critical issues missed in human annotations, underscoring its role as a robust, developer-centric tool for reliable monitoring and improvement of agentic systems in production.

---

## 結構化摘要

### 核心貢獻
- 提出 **AgentCompass**——號稱首個專為 agentic workflows **post-deployment 監控與 debugging** 設計的 evaluation framework（非開發期評測，而是生產環境持續監測）。
- 將「資深 debugger 的推理流程」結構化為 **multi-stage analytical pipeline**：error identification/categorization → thematic clustering → quantitative scoring → strategic summarization。
- 引入 **dual memory system**（episodic + semantic），支援跨執行（across executions）的 continual learning，讓框架隨部署累積經驗。
- 以 design partners 的真實部署驗證實用性，並對標公開 **TRAIL benchmark** 量測效能。

### 關鍵結果
- 在 TRAIL benchmark 的 key metrics 上達成 **state-of-the-art**（論文宣稱；abstract 未列具體數字）。
- 能挖出 **human annotations 遺漏的 critical issues**——即模型發現了人工標註漏掉的問題，方法層意義 > 單純分數。
- 真實部署（real-world deployments）case study 佐證 developer-centric 工具的實用性。

### 限制
文件 abstract 未列明確 limitation 章節（需查正文 PDF）。依現有資訊判斷的潛在弱點：
- 「首個」「SOTA」屬作者宣稱，abstract 未給對照 baseline 與量化差距，需正文驗證。
- 評估框架本身以 LLM 為 judge（推測），存在 **LLM-as-judge 自我偏誤 / 評測者本身需被評測** 的遞迴問題——abstract 未說明如何校準 judge 可靠度。
- dual memory 的 continual learning 可能引入 **goal drift / 過擬合特定部署** 風險，泛化性待查。
- 「uncovering issues missed in human annotations」缺乏 ground-truth 仲裁機制說明（究竟是真陽性還是 false positive 難分）。

---

## Workspace 關聯（評估，非既成結論）

- **直接對應 `unverified_success` 閘門**：本框架的核心命題（agentic workflow 自報成功 ≠ 真實可靠，需獨立評測層揪出隱性 failure）正是 core.md TEST 階段「subagent/workflow verdict 非證據，採信前必機械重驗」的學術版。⚠️ 落地門檻：AgentCompass 仍是 LLM-based judge，與本 workspace「確定性 gate 絕不經 sub-agent 中介」原則存在張力——不可直接拿它取代 grep/test/healthcheck 的確定性檢查。
- **The Loop TEST／PGE 階段**：multi-stage pipeline（識別→分群→評分→總結）與 `/deep-review` 的多維審查思路同構，可作為設計 `/pilot frontier` 稽核（原 `quality-pipeline`，v5.1 刪除） G-gate rubric 的參考。⚠️ 需先驗其 false-positive rate 再考慮借鑑。
- **Advisor 模式 / dynamic workflow 三失敗模式**：論文的 post-deployment 監控對應 `core.md §PROPOSE 委派`（原 subagent-strategy.md）的 agentic laziness / self-preferential bias / goal drift 偵測需求；dual memory 的 continual learning 概念可對照 RECORD 階段「自我演化迴圈」，但 workspace 強調「機械驗證入庫、整合門控非自動」——AgentCompass 的自動 continual learning 若無獨立 evaluator 把關，與此安全邊界衝突。 〔v5.1：所引 workspace 細則已退役 → 見 `INDEX.md` §v5.1 規則退役對照〕
- 純研究歸檔，無既成程式碼整合建議；若要實驗其方法，建議 spawn 隔離 sub-agent 跑 TRAIL 復現再評估，不直接動 auto-load 規則。

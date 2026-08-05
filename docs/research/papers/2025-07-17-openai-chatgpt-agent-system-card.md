---
url: "https://cdn.openai.com/pdf/839e66fc-602c-48bf-81d3-b21eacc3459d/chatgpt_agent_system_card.pdf"
title: "ChatGPT Agent System Card"
archived_date: 2026-06-24
authors: [OpenAI]
domains: [system-card]
pdf_path: pdfs/openai-chatgpt-agent-system-card.pdf
published_date: 2025-07-17
source_url: "https://cdn.openai.com/pdf/839e66fc-602c-48bf-81d3-b21eacc3459d/chatgpt_agent_system_card.pdf"
---

# ChatGPT Agent System Card

**Source**: https://cdn.openai.com/pdf/839e66fc-602c-48bf-81d3-b21eacc3459d/chatgpt_agent_system_card.pdf
**Published**: July 17, 2025
**PDF**: `research/papers/pdfs/openai-chatgpt-agent-system-card.pdf` (42 pp, full text archived)

---

## 摘要（依官方 PDF overview 與官方公開資訊整理）

- ChatGPT agent 是一個能自主執行任務的 agentic 系統：結合可操作的虛擬電腦（瀏覽器、終端機、檔案/API 操作），讓 ChatGPT 能代使用者完成 web browsing、研究、產出可交付成果等多步驟工作流程。
- 統合先前 Operator（電腦操作）與 deep research（資訊綜整）能力於單一 agentic 模型。
- 因賦予模型實際行動能力（real-world actions），system card 著重於新的 agentic 風險面：prompt injection、敏感操作的使用者確認、以及 Preparedness Framework 能力評估。

---

## 結構化摘要

### 模型與定位
- Agentic 模型：可在受控虛擬環境中瀏覽網頁、執行程式碼與工具、與外部網站互動以完成終端任務。
- 風險定位由「生成內容」擴展到「採取行動」——強調 action-space 安全。

### 關鍵能力 / 安全評估數字
- Preparedness Framework：OpenAI 將 ChatGPT agent 視為在 **Biological and Chemical 領域達 High capability**，因而首次啟動該類別對應的強化安全防護（safeguards）與部署緩解措施。
- Prompt injection 為核心 agentic 威脅：透過監控模型、訓練與產品層緩解、以及對敏感動作要求 user confirmation 來降低風險。
- 其他評估涵蓋 disallowed content、外部紅隊、以及對 irreversible/sensitive 操作的人為把關（具體百分比見 PDF 全文）。

### Workspace 關聯（評估）
- 「對 sensitive/irreversible 動作要求 user confirmation」與 core.md APPLY「不可逆例外」（DELETE/DROP/prod deploy/rm -rf… 必摘要 + 等待確認）完全同構——agentic 安全的共同設計原則。
- Prompt injection 緩解對應 `core.md §PROPOSE 委派`（原 subagent-strategy.md）的 Agent Input Security（外部輸入包 `<untrusted_objective>`、當 data 不當 instruction）。
- Bio/Chem High capability 觸發 safeguards → 對應「能力提升即提高風險、須對應 gate」的 Preparedness 思維，呼應本庫生產紅線與破壞性 gate。⚠️ 依官方公開資訊整理；數字以 PDF 全文為準。

---
title: "Agents — claude.com/blog"
type: index
---

# Agents — claude.com/blog

> 收錄自 [claude.com/blog/category/agents](https://claude.com/blog/category/agents) · 19 篇文章 · 2025-11-13 ~ 2026-05-13
> 最後更新：2026-05-27

---

## Best practices for computer and browser use with Claude

**Date:** 2026-05-13 | **URL:** https://claude.com/blog/best-practices-for-computer-and-browser-use-with-claude

### Summary
整合 Claude 電腦/瀏覽器操作能力的實作指南。涵蓋截圖解析度優化、內容排序、模型選擇、Context 管理與 Prompt Injection 防護。適用 Claude 4.6 family 及 Opus 4.7。

### Key Points
- 截圖預縮放：傳入 API 前先縮放（4.6 family：1568px/1.15MP；Opus 4.7：2576px/3.75MP）
- 內容排序：文字指令放在圖片之前，提升點擊準確率
- 模型選擇：Sonnet 4.6 機械精度佳；Opus 4.7 兼具點擊精度與推理能力
- Thinking Effort：Opus 4.7 用 `high`；Claude 4.6 用 `medium`（`low` 成本敏感場景亦有效）
- Context 管理：Prompt Caching + rolling buffer（保留最近 3 張截圖，每 25 張批次清理）
- `computer_20251124` 工具含內建 Prompt Injection classifier（免費）

---

## Building AI agents for the enterprise

**Date:** 2026-04-30 | **URL:** https://claude.com/blog/building-ai-agents-for-the-enterprise

### Summary
企業 AI 轉型指南：應對「Agentic 思維鴻溝」、員工技能升級、流程壓縮三大支柱。40% 員工使用 AI（2023 年 20%）。案例：L'Oreal、Lyft、Rakuten。

### Key Points
- 克服 Agentic 思維鴻溝：為何部分 AI 部署產生複合效益而其他停滯
- 員工技能升級：與組織工作流對齊的 AI 培訓最佳實踐
- 流程壓縮：保持人工監督的同時精簡資訊密集流程
- Claude Cowork 六個月部署框架
- 三支柱策略：員工培訓 + 目標應用 + 未來產品開發

---

## Claude API skill now in CodeRabbit, JetBrains, Resolve AI, and Warp

**Date:** 2026-04-29 | **URL:** https://claude.com/blog/claude-api-skill

### Summary
`claude-api` Skill 擴展至四大開發工具。提供 Prompt Caching 優化、Agent 架構指引、Model 遷移輔助、Managed Agents 設定。開源於 `anthropics/skills`，20 行 CI 設定即可整合。

### Key Points
- 快取最佳化、Agent 架構（context compaction）、模型遷移（Opus 4.7）、Managed Agents 設定
- CodeRabbit：減少 Agent 建構時的 review 意外
- JetBrains：Claude 升級轉為引導式 IDE 工作流
- Warp：開發者無需離開 terminal 查閱 API 參數
- 開源：`anthropics/skills` on GitHub；約 20 行 CI 設定即可整合

---

## Product development in the agentic era

**Date:** 2026-04-29 | **URL:** https://claude.com/blog/product-development-in-the-agentic-era

### Summary
Jess Yan（Claude Managed Agents PM）分享 AI 如何將 PM 工作從行政性轉為策略性創意工作。用 Claude 自動化操作任務，用 Claude Code 針對特定需求建立自訂 Agent。

### Key Points
- 工作流演進：Claude Cowork 做開放性研究/發現；Claude Code 建立特定操作 Agent
- API 開發方式：對照 API 規格直接建立 Agent 原型，比多週文件審查更快發現設計問題
- 三類 Agent：分析型（查詢內部 DB）、情緒監控型（掃描開發者回饋）、Demo 建立型（活動演示）
- 核心觀點：自動化讓 PM 回歸本職工作——策略、創意和人員協作

---

## Building agents that reach production systems with MCP

**Date:** 2026-04-22 | **URL:** https://claude.com/blog/building-agents-that-reach-production-systems-with-mcp

### Summary
MCP（Model Context Protocol）已成為生產環境 Agent 的標準化基礎層，月下載量超過 3 億次。Tool Search 等 context 效率模式可將複雜工作流的 token 使用量減少 85% 以上。

### Key Points
- MCP 成為雲端生產系統的共通層（Claude Cowork、Claude Managed Agents 底層）
- 有效 MCP server：以意圖分組工具（intent-grouped），而非逐一映射 API
- Tool Search 模式降低 85%+ token 用量
- MCP 與 Skill 常搭配成 plugin，提供統一的領域知識入口

---

## Preparing your security program for AI-accelerated offense

**Date:** 2026-04-10 | **URL:** https://claude.com/blog/preparing-your-security-program-for-ai-accelerated-offense

### Summary
AI 模型正大幅加速漏洞發現與利用速度，組織必須透過七大優先行動調整安全防禦姿態，防禦方同樣可以運用相同的 AI 能力自動化安全操作。

### Key Points
- CISA KEV：網際網路面向系統 24 小時修補目標
- 透過自動化、分類 Agent 擴展漏洞管理規模
- AI 掃描整合進開發流水線（安全左移）
- 採用零信任設計，以密碼學身份取代摩擦式存取控制

---

## Multi-agent coordination patterns: Five approaches and when to use them

**Date:** 2026-04-10 | **URL:** https://claude.com/blog/multi-agent-coordination-patterns

### Summary
五種多 Agent 協調模式完整框架，建議從最簡單模式開始，根據具體限制逐步演進。

### Key Points
- **Generator-Verifier**：最廣泛部署，適合有明確評估標準的品質輸出
- **Orchestrator-Subagent**：可預定、有界的子任務
- **Agent Teams**：持續協作的多步驟工作
- **Message Bus**：事件驅動非同步管道
- **Shared State**：Agent 需即時共享發現時

---

## Harnessing Claude's intelligence: 3 key patterns for building apps

**Date:** 2026-04-02 | **URL:** https://claude.com/blog/harnessing-claudes-intelligence

### Summary
三種隨模型能力演進的架構模式：通用工具、消除不必要抽象、Prompt Caching 邊界建立。靜態內容前置可降低高達 90% 成本。

### Key Points
- 優先使用通用工具（bash、文字編輯器），非特定用途替代品
- 定期審計 Agent 框架中的過時假設
- Prompt Caching：靜態內容前置可降 90% 成本
- 高風險操作提升為專用型別化工具呼叫

---

## Common workflow patterns for AI agents—and when to use them

**Date:** 2026-03-05 | **URL:** https://claude.com/blog/common-workflow-patterns-for-ai-agents-and-when-to-use-them

### Summary
三種主要 Agent 工作流模式：Sequential（依賴任務）、Parallel（獨立並行）、Evaluator-Optimizer（迭代品質優化）。強調「從最簡單模式開始」。

### Key Points
- Sequential：任務有依賴時；Parallel：獨立並行任務
- Evaluator-Optimizer 迴圈透過迭代回饋改善輸出品質
- 模式選擇應優先考慮簡單性，使用解決問題所需的最低複雜度
- 資源限制和任務結構應驅動架構決策

---

## Cowork and plugins for finance

**Date:** 2026-02-24 | **URL:** https://claude.com/blog/cowork-plugins-finance

### Summary
Anthropic 為 Claude Cowork 推出金融專屬 plugin，包含五個領域（投行、股權研究、私募、財富管理），以及 FactSet 和 MSCI 連接器，讓金融專業人士在不切換工具的情況下完成端到端工作流。

### Key Points
- 五個金融 plugin：投資銀行、股權研究、私募股權、財富管理
- FactSet 和 MSCI 連接器直接整合金融數據平台
- Excel 和 PowerPoint 跨應用工作流
- Plugin 生態系加速金融服務領域的角色定製化

---

## Cowork and plugins for teams across the enterprise

**Date:** 2026-02-24 | **URL:** https://claude.com/blog/cowork-plugins-across-enterprise

### Summary
企業版 Cowork 新增私有 plugin 市場與管理員控制功能，超過 12 個預建跨部門 plugin 模板（HR、設計、工程、財務），以及跨 Excel/PowerPoint 的多步驟工作流協調。

### Key Points
- 私有 plugin 市場讓組織集中控制批准的 plugin 和連接器
- 超過 12 個預建模板涵蓋 HR、設計、工程、財務等部門
- 管理員控制實現企業規模的治理和合規
- 跨應用工作流協調處理複雜多步驟流程

---

## Customize Cowork with plugins

**Date:** 2026-01-30 | **URL:** https://claude.com/blog/cowork-plugins

### Summary
Anthropic 為 Claude Cowork 推出 plugin 支援，讓使用者可捆綁 skill、connector、slash command 和 sub-agent 為特定角色和工作流定製 Claude。發布 11 個涵蓋銷售、財務、法律、行銷的開源 plugin。

### Key Points
- Plugin 捆綁 skill、connector、slash command 和 sub-agent
- 11 個開源 plugin 提供銷售、財務、法律、行銷模板
- 本地 plugin 儲存，未來支援組織範圍共享
- 讓團隊無需開發自訂 agent 即可定製 Claude

---

## Building multi-agent systems: When and how to use them

**Date:** 2026-01-23 | **URL:** https://claude.com/blog/building-multi-agent-systems-when-and-how-to-use-them

### Summary
多 Agent 架構何時有真正價值的指南。三個適合場景：保護 context 不受污染、並行任務執行、利用專業工具或知識。超出這些場景，協調成本通常超過收益。

### Key Points
- 三個適合場景：context 隔離、並行執行、專業工具/領域知識
- 超出這三個場景時，協調成本通常超過收益
- 大多數企業工作流使用單 Agent 架構更具成本效益

---

## Building agents with Skills: Equipping agents for specialized work

**Date:** 2026-01-22 | **URL:** https://claude.com/blog/building-agents-with-skills-equipping-agents-for-specialized-work

### Summary
Agent Skills 是將領域知識打包成組織化檔案集合的新範式。透過 Progressive Disclosure 管理 context window，通用 Agent + Skill 優於為每個領域建立專用 Agent。

### Key Points
- Skill 將領域知識、工作流和最佳實踐打包成可存取的檔案集合
- Progressive Disclosure 按需載入 Skill 資訊，管理 context window
- Skill 分類：foundational、partner、enterprise
- Skill 內的可執行腳本無需離開 Agent 環境即可自動化

---

## Eight trends defining how software gets built in 2026

**Date:** 2026-01-21 | **URL:** https://claude.com/blog/eight-trends-defining-how-software-gets-built-in-2026

### Summary
2026 年 AI 如何改變軟體開發的八大趨勢。開發者在 60% 的工作中使用 AI，但只能「完全委派」0-20% 的任務，人工監督仍不可或缺。

### Key Points
- AI 用於 60% 的開發工作，但只有 0-20% 可完全委派
- 編程 Agent 是協作夥伴，非替代品，人工監督至關重要
- 組織四大優先任務：多 Agent 協調、人機監督擴展、擴展至非工程團隊、嵌入早期安全
- Agentic 編碼擴展至產品、設計和業務團隊

---

## Extending Claude's capabilities with skills and MCP servers

**Date:** 2025-12-19 | **URL:** https://claude.com/blog/extending-claude-capabilities-with-skills-mcp-servers

### Summary
Skill 和 MCP server 如何協同增強 Claude 的能力。MCP 提供與外部工具的連接，Skill 教 Claude 如何有效使用這些連接。兩者共同確保 Agent 遵循機構特定流程。

### Key Points
- MCP server 提供與外部工具、數據源的連接
- Skill 編碼程序知識和工作流邏輯，以有效利用 MCP
- 職責分離：MCP 負責連接，Skill 負責邏輯
- 此架構支援企業級可靠性和治理

---

## Skills for organizations, partners, the ecosystem

**Date:** 2025-12-18 | **URL:** https://claude.com/blog/organization-skills-and-directory

### Summary
Anthropic 推出組織級 Skill 管理功能，Team 和 Enterprise 管理員可集中配置 Skill。同時發布 Skill 目錄（含 Notion、Canva、Figma、Atlassian 整合）和 Agent Skills 開放標準。

### Key Points
- 組織管理：管理員可跨組織集中部署批准的 Skill
- Skill 目錄：合作夥伴建置的整合（Notion、Canva、Figma、Atlassian）
- Agent Skills 開放標準：跨 AI 平台的 Skill 可攜性
- 中央治理確保組織內一致的批准工作流

---

## How to create Skills: Key steps, limitations, and examples

**Date:** 2025-11-19 | **URL:** https://claude.com/blog/how-to-create-skills-key-steps-limitations-and-examples

### Summary
自訂 Skill 建立指南，五步驟流程，強調清晰描述對正確觸發的重要性。包含 PDF 處理和品牌指南等實際範例。

### Key Points
- 五步驟流程：從概念到部署的結構化 Skill 建立
- 清晰的 Skill 描述對正確觸發和發現至關重要
- 實際範例（PDF 處理、品牌指南）展示如何編碼機構知識
- Skill 標準化輸出，確保組織一致性

---

## Skills explained: How Skills compares to prompts, Projects, MCP, and subagents

**Date:** 2025-11-13 | **URL:** https://claude.com/blog/skills-explained

### Summary
Skill 在 Claude 更廣泛的 Agent 生態系中的定位，以及何時使用 Skill 與 prompt、Projects、MCP 和 subagent 的比較指南。包含競爭情報工作流的完整範例。

### Key Points
- Skill 是動態發現的指令資料夾，補充 prompt、Projects、MCP 和 subagent
- 每個 Agent 組件有不同用途：Skill 負責知識、MCP 負責連接、subagent 負責任務委派
- Skill 最適合領域知識和程序知識；Projects 用於共享 context；MCP 用於工具存取
- 結合生態系統實現複雜的 Agent 工作流

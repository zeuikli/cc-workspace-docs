---
title: Enterprise AI — claude.com/blog
type: index
---

# Enterprise AI — claude.com/blog

> 收錄自 [claude.com/blog/category/enterprise-ai](https://claude.com/blog/category/enterprise-ai) · 18 篇文章 · 2025-11-17 ~ 2026-05-15
> 最後更新：2026-05-16

> 注：2026-04-09 起的產品公告（Managed Agents、Advisor Strategy、Cowork Enterprise）收錄於 [announcements/index.md](../announcements/index.md)，本分類專注於企業採用案例與功能深度報導。

---

## Deploying Claude across the legal industry

**Date:** 2026-05-15 | **URL:** https://claude.com/blog/deploying-claude-across-the-legal-industry

### Summary
法律行業 Claude 部署完整指南。87% 法務長團隊現使用 Generative AI（去年 44%）。涵蓋產品矩陣、12 個預建 Plugin、合約審閱到法規監控的具體用例。

### Key Points
- 產品矩陣：Chat（研究）、Cowork（事務級多檔案工作）、Microsoft 365（Word/Excel/Outlook）、Platform（客製應用）
- 12 個實務領域 Plugin：Commercial、Corporate、Employment、Privacy、Product、Regulatory、AI Governance、IP、Litigation
- 用例：合約審閱/紅線標記、M&A 盡職調查、隱私影響評估、法規監控、訴訟準備
- 技術指引：主機選擇、資料留存、特權保護、審計要求
- Anthropic 內部法律團隊實作案例

---

## How Claude Code works in large codebases: Best practices and where to start

**Date:** 2026-05-14 | **URL:** https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start

### Summary
大規模 Codebase（百萬行 Monorepo、遺留系統、分散式架構）Claude Code 部署模式。成功的關鍵在「Harness」生態系統——CLAUDE.md、Hooks、Skills、Plugins、MCP Server 的五元件組合。

### Key Points
- Claude Code 用 Agentic Search（非 RAG），直接在本地 codebase traverse；導覽品質取決於 codebase 組織
- 五元件 Harness：CLAUDE.md（精簡分層）、Hooks（事件觸發自動化）、Skills（按需專業知識）、Plugins（組織分發）、MCP（內部工具連接）
- CLAUDE.md 三原則：保持精簡、子目錄初始化、排除生成檔案；搭配 LSP 做符號級搜尋
- 每 3-6 個月審閱設定（模型進化後，舊指令可能反而限制新模型）
- 組織所有權：指定 DRI 管理設定，避免碎片化

---

## Deploying Claude across financial services

**Date:** 2026-05-05 | **URL:** https://claude.com/blog/deploying-claude-across-financial-services

### Summary
金融服務 Claude 部署完整指南。涵蓋投資銀行、財富管理、零售銀行三個子行業，以及研究、交易、承保、索賠、模型審查、月末關帳六大工作流。提供三階段採用計劃。

### Key Points
- 產品矩陣：Chat（研究）、Cowork（多檔案專案）、Code（量化/工程）、Microsoft 365（試算表/文件）、Managed Agents（客製應用）
- 10 個金融 Agent 模板：Pitch Builder、Market Researcher、KYC Screener、General Ledger Reconciler、Month-end tools 等
- 案例：AIG、Commonwealth Bank of Australia、IG Group、Moody's
- 三階段計劃：基礎 → 試點 → 規模化，附具體行動步驟

---

## Agents for Financial Services

**Date:** 2026-05-05 | **URL:** https://www.anthropic.com/news/finance-agents

### Summary
Anthropic 發布 10 個金融服務 agent 模板，擴展 Microsoft 365 整合（Excel、PowerPoint、Word），並新增 Dun & Bradstreet、Moody's 等金融數據連接器。Claude Opus 4.7 在 Vals AI Finance Agent 基準達 64.37%。

### Key Points
- 10 個金融 agent 模板：投資手冊建立、KYC 審查、月末關帳等
- Microsoft 365 深度整合：Excel、PowerPoint、Word 自動化
- 新金融數據連接器：Dun & Bradstreet、Fiscal AI、Moody's
- 基準成績：Claude Opus 4.7 在 Vals AI Finance Agent 達 64.37%
- 目標：提升金融機構 AI agent 部署效率

---

## Building a New Enterprise AI Services Company with Blackstone, Hellman & Friedman, and Goldman Sachs

**Date:** 2026-05-04 | **URL:** https://www.anthropic.com/news/enterprise-ai-services-company

### Summary
Anthropic 與 Blackstone、Hellman & Friedman、Goldman Sachs 合作成立企業 AI 服務公司，為中型企業提供 Claude 整合的工程支援，重點覆蓋醫療與製造業。

### Key Points
- 聯合成立：新企業 AI 服務公司（獨立實體）
- 合作方：Blackstone、Hellman & Friedman、Goldman Sachs
- 服務對象：中型企業 Claude 整合工程支援
- 重點行業：醫療、製造業
- 應用 AI 工程師團隊協助識別高影響力用例並開發定制方案

---

## Anthropic and NEC Collaborate to Build Japan's Largest AI Engineering Workforce

**Date:** 2026-04-24 | **URL:** https://www.anthropic.com/news/anthropic-nec

### Summary
Anthropic 與 NEC 達成戰略合作，NEC 向全球約 3 萬員工部署 Claude，重點覆蓋金融、製造、網路安全、地方政府，建立卓越中心培育 AI 原生工程團隊。

### Key Points
- 規模：NEC 全球 ~3 萬員工部署 Claude（首個日本全球合作夥伴）
- 重點行業：金融、製造、網路安全、地方政府
- 卓越中心：培育 AI 原生工程團隊
- 目標：建立日本最大企業 AI 工程人才庫
- 戰略意義：Anthropic 亞太企業市場深化

---

## How Carta Healthcare gets AI to reason like a clinical abstractor

**Date:** 2026-04-08 | **URL:** https://claude.com/blog/carta-healthcare-clinical-abstractor

### Summary
透過 Context Engineering（而非規則式系統）達到 98-99% 的臨床資料擷取準確率。讓臨床專家保持在迴圈中，部署週期從數月縮短至數週。

### Key Points
- LLM 比傳統 NLP 更能處理臨床文件中矛盾證據的情境判斷
- Context Engineering（正確組裝和排序 context）是真正瓶頸
- 展示每個資料點背後的證據，支援驗證和回饋
- 部署週期從數月縮短至數日

---

## 1M context is now generally available for Opus 4.6 and Sonnet 4.6

**Date:** 2026-03-13 | **URL:** https://claude.com/blog/1m-context-ga

### Summary
Claude Opus 4.6 和 Sonnet 4.6 的完整 1M token context window 以標準定價正式開放，不額外收費。每次請求最多支援 600 張圖片或 PDF 頁面。

### Key Points
- 統一定價：整個 1M token 範圍無乘數，不額外收費
- 媒體容量提升：每次請求 600 張圖片或 PDF 頁面（原來是 100）
- Claude Code 整合：Max、Team 和 Enterprise 用戶自動存取完整 window
- Opus 4.6 在整個 context 長度上 MRCR v2 達到 78.3%

---

## Advancing Claude for Excel and PowerPoint

**Date:** 2026-03-11 | **URL:** https://claude.com/blog/claude-excel-powerpoint-updates

### Summary
Claude for Excel 和 PowerPoint 新增跨檔案 context 共享功能，支援 Skill 自動化，並擴展至 Amazon Bedrock、Google Cloud Vertex AI 和 Microsoft Foundry 部署。

### Key Points
- 跨應用 context 共享：在 Excel 和 PowerPoint 之間保持完整對話 context
- 金融分析 Skill（LBO 模型、DCF 分析）和簡報 Skill
- 擴展雲端部署：Bedrock、Vertex AI、Microsoft Foundry
- 原生 Excel Agent Mode：Microsoft 365 Copilot 整合

---

## Claude Enterprise, now available self-serve

**Date:** 2026-02-12 | **URL:** https://claude.com/blog/self-serve-enterprise

### Summary
Claude Enterprise 現在可以直接從網站購買，無需銷售對話。組織可立即設定工作區、配置 SSO 和邀請團隊成員。

### Key Points
- 自助購買：直接線上購買，幾分鐘內部署
- 整合 AI 產品：Claude、Claude Code、Cowork 和領域專屬 Plugin
- 企業安全控制：SSO、域名捕捉、SCIM、審計日誌、Compliance API
- 成本管理：按位加用量定價，組織和用戶級費用上限
- 不使用 Enterprise 數據訓練模型

---

## Behind the model launch: What customers discovered testing Claude Opus 4.6 early

**Date:** 2026-02-09 | **URL:** https://claude.com/blog/behind-model-launch-what-customers-discovered-testing-claude-opus-4-6-early

### Summary
Harvey、Bolt、Shopify 和 Lovable 在早期測試 Claude Opus 4.6，進行密集評估。他們的回饋直接影響了最終發布版本。

### Key Points
- 基準突破：Harvey 的 BigLaw Bench 達到 90.2%（第一個超過 90% 的 Anthropic 模型）
- 卓越除錯：Bolt.new 發現 Opus 4.6 首次嘗試即能診斷之前模型失敗的 bug
- 增強自主性：改善指令遵循，能預測需求並創建解決方案
- 早期回饋直接影響最終產品設計

---

## Advancing finance with Claude Opus 4.6

**Date:** 2026-02-05 | **URL:** https://claude.com/blog/opus-4-6-finance

### Summary
Claude Opus 4.6 為金融專業人士提供增強的金融推理能力，在 Real-World Finance 評估上比 Sonnet 4.5 提高 23+ 個百分點，並推出 Cowork 桌面應用和 PowerPoint 整合。

### Key Points
- 效能提升：Real-World Finance 評估比 Sonnet 4.5 高 23+ 個百分點
- Cowork 發布：讓 Claude 讀取、編輯、建立檔案並使用自訂金融 Plugin
- Claude in Excel 增強：長時間執行任務、樞紐分析表、條件格式
- Claude in PowerPoint Beta：直接建立簡報的研究預覽工具

---

## How leading retailers are turning AI pilots into enterprise-wide transformation

**Date:** 2026-01-28 | **URL:** https://claude.com/blog/how-leading-retailers-are-turning-ai-pilots-into-enterprise-wide-transformation

### Summary
大多數企業 AI 計畫難以超越試點階段的指南。識別成功組織的三個關鍵步驟，並借鑒零售商的實際案例（Shopify、L'Oréal）。

### Key Points
- 零售挑戰：碎片化技術棧、季節性需求、缺乏 AI + 運營複合技能
- 成功模型：Shopify 為商家建立 AI 助手；L'Oréal 在 150 個國家協調 15+ 個專業 Agent
- 基礎和治理：利害關係人對齊和明確治理框架優先於試點
- 選擇性試點策略：從低風險應用開始，而非全企業推廣

---

## How Anthropic's Growth Marketing team cut ad creation time from 30 minutes to 30 seconds

**Date:** 2026-01-26 | **URL:** https://claude.com/blog/how-anthropic-uses-claude-marketing

### Summary
非技術行銷人員 Austin Lau 使用 Claude Code 構建自動化工作流，將廣告創作從 30 分鐘縮短至 30 秒。無需編碼經驗即可開發 Figma 插件和 Google Ads 工作流。

### Key Points
- Figma 插件：一鍵生成多種長寬比的廣告變體（節省每批 ~30 分鐘）
- Google Ads 工作流：腦力激盪、驗證字元數、匯出 CSV
- 行銷影響：影響者行銷每月節省 100+ 小時；案例研究從 2.5 小時降至 0.5 小時
- 非技術用戶通過清晰表達問題即可構建工具

---

## Making Claude a better electrical engineer

**Date:** 2025-12-12 | **URL:** https://claude.com/blog/making-claude-a-better-electrical-engineer

### Summary
Anthropic 與 Diode Computers 合作提升 Claude 自動生成電氣參考設計的能力。透過領域專家合作和專業訓練數據，Claude Sonnet 4.5 在複雜技術任務上達到卓越效能。

### Key Points
- 領域特定合作：與行業專家識別能力差距並整合專業知識
- 參考設計自動化：在數小時內（而非數天）處理芯片文件並生成完整電路圖
- 技術準確性提升：更好地解讀數據表、理解精細電路
- 工程師偏好 Sonnet 4.5 設計的比例為 80%（vs Sonnet 4）

---

## How enterprises are building AI agents in 2026

**Date:** 2025-12-09 | **URL:** https://claude.com/blog/how-enterprises-are-building-ai-agents-in-2026

### Summary
500+ 技術領導者調查顯示，企業正從簡單任務自動化過渡到跨整個團隊的複雜多步驟工作流。80% 的組織報告其 AI Agent 投資已提供可量化的經濟回報。

### Key Points
- 57% 為多階段工作流部署 Agent；81% 計劃 2026 年更複雜的用例
- 90% 使用 AI 進行開發；86% 在整個開發生命週期部署 Agent
- Thomson Reuters 將法律研究從小時縮短至分鐘；eSentire 將威脅分析從 5 小時壓縮至 7 分鐘（95% 準確率）
- 實施優先事項：系統整合（46%）、數據存取/質量（42%）、變革管理（39%）

---

## How Anthropic's legal team cut review times from days to hours with Claude

**Date:** 2025-12-08 | **URL:** https://claude.com/blog/how-anthropic-uses-claude-legal

### Summary
Anthropic 法律團隊使用 Claude 自動化合約審閱和行銷內容審查，將合規審閱從 2-3 天縮短至 24 小時。透過 Claude 和專業 Skill 建立無代碼工作流。

### Key Points
- 行銷審查工具：Slack 整合工作流，標記公開權利問題；周轉時間從 2-3 天降至 24 小時
- 合約審閱：比較文件版本並推薦商業手冊語言
- 利益衝突分析：針對政策框架的自動化表單審查
- 最佳實踐：從痛點開始、使用自然語言指令、保持人工監督

---

## How three YC startups built their companies with Claude Code

**Date:** 2025-11-17 | **URL:** https://claude.com/blog/building-companies-with-claude-code

### Summary
三家 Y Combinator 新創公司展示 Claude Code 如何壓縮開發週期和讓非工程師也能建立產品。HumanLayer、Ambral 和 Vulcan Technologies 的創辦人展示結構化工作流和多模型委派如何加速擴展。

### Key Points
- 分離工作流：研究、規劃和實作作為不同階段，防止 context 污染
- 多模型委派：Opus 4.1 負責研究/規劃，Sonnet 4.5 負責實作（更高品質）
- 非技術創辦人可以競爭：清晰思維和結構化問題分解比傳統工程背景更重要
- 早期中斷防止浪費：仔細審視 chain-of-thought 並提早停止無效方向

---
url: "https://timdeschryver.dev/blog/keep-agentic-ai-simple-a-practical-workflow-for-software-development"
title: "Keep Agentic AI Simple: A Practical Workflow for Software Development"
type: article
---

# Keep Agentic AI Simple: A Practical Workflow for Software Development

**原始 URL**: https://timdeschryver.dev/blog/keep-agentic-ai-simple-a-practical-workflow-for-software-development

**作者**: Tim Deschryver  
**修改日期**: 2026 年 5 月 7 日

---

## 核心摘要

Tim Deschryver 分享了他使用 AI 代理重寫專案的經驗，他將自己定位為團隊領導者，同時把 AI 視為「侍從」（自行車賽中的支援騎手）。此篇強調了思慮周詳的架構和策略性監督，而不是依賴快速修復。

該方法論代表了軟體工程的根本轉變：從關注技術細節轉向提供良好的「護欄」（guardrails），讓 AI 代理能有效執行工作。核心理念是開發者的角色變得更少涉及技術細節，更多是架構層級的思考與把關。

### 三個核心實踐組件

1. **AGENTS.md 文件** — 標準化指令文件，包含專案結構、技術棧、命令、編碼慣例與資料庫圖表，應定期審查以保持準確並累積錯誤模式
2. **Agent Skills** — Markdown 知識檔案擴展 AI 能力，與 AGENTS.md 的區別在於 skills 僅在相關時載入
3. **規格驅動開發** — 使用 OpenSpec 在實作前生成提案、設計和任務文件，分解工作為可管理的步驟

---

## 關鍵實踐

### AGENTS.md 的角色
此檔案成為 AI 代理的「憲法」，提供一致的框架。內容涵蓋：
- 專案結構與技術棧
- 重複的命令與编碼慣例
- 資料庫設計圖表
- 防止 AI 遺漏微妙要求的清單

### Agent Skills 系統
區分於 AGENTS.md（總是包含），skills 文件採用按需載入模式。Deschryver 結合官方 Angular 和 .NET skills 加上自定義設計系統 skills，確保視覺與代碼一致性。

### 規格驅動開發流程
在實作前使用 OpenSpec 生成規範文件，將工作分解為明確步驟，防止 AI 遺漏邊界情況。

### 工具與模型選擇
作者發現 Claude 與 Codex 同樣有用，因快速迭代模型改進。偏好 OpenCode 以避免供應商鎖定。

---

## 關鍵引用與數據

> 「不要做害怕 AI 的開發者。要做學會把它視為最新系統的開發者。」— Tim Deschryver

> 「我們作為軟體工程師的角色變得更少技術細節，更多是提供良好護欄讓代理工作。」

**核心轉變**: 從微管理實作細節轉向架構層級思考與品質把關。

---

## 工作流程的實踐意義

此方法適用於不同規模的團隊，強調：
- 清晰的指令文件優於逐次對話重複指示
- 規格驅動減少返工與需求遺漏
- 開發者角色提升至戰略層級
- AI 作為可靠的執行工具，而非決策者

Deschryver 的實踐展現了人類開發者與 AI 協作的新模式：領導力來自架構設計與需求管理，執行由 AI 承擔。

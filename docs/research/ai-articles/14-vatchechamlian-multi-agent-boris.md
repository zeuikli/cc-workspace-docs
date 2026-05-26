---
url: "https://vatchechamlian.com/orchestrating-agents-claude.html"
title: "The Multi-Agent Approach: How Claude Code's Creator Actually Uses the Tool"
type: article
---

# The Multi-Agent Approach: How Claude Code's Creator Actually Uses the Tool

**原始 URL**: https://vatchechamlian.com/orchestrating-agents-claude.html

**作者**: Vatché Chamlian  
**發佈日期**: 2026 年 1 月 6 日  
**來源**: vatchechamlian.com

---

## 核心摘要

本文探討 Boris Cherny 採用的多 agent 方法論，重點在於「同時運行多個 Claude agent 而非依賴單一聊天機器人」。核心概念是「協調多個 AI agent 平行工作，各自執行任務，而你像指揮官在他們之間切換」。該方法透過結構化協調、團隊知識庫、計畫模式與驗證迴圈，顯著改善代碼品質與開發速度。

### 多 Agent 協調核心

**並行處理**
Boris Cherny 同時操作 5-15 個 Claude 實例，經由終端標籤與瀏覽器會話隔離。使用 iTerm2 通知在 agents 需要輸入時警告他。

**團隊知識庫**
共享 CLAUDE.md 檔案記錄專案模式、開發工作流程與常見錯誤。此檔案隨時間形成「複合知識庫」，團隊文件化教訓時改善。

**計畫模式優先**
工作流程強調在實作前迭代方法，使用專用「計畫模式」在執行前精化策略。

**驗證迴圈**
品質改善依賴「給 Claude 一個驗證其工作的方法」，經由自動化測試與瀏覽器驗證。此為「品質最重要單一因素」。

**自動化工具**
斜線命令、subagents 與 hooks 減少重複任務，讓 Claude 在常見開發工作流程中更自主工作。

---

## 關鍵實踐

**上下文管理與知識持久化**
- 跨會話維護 CLAUDE.md 記錄模式與錯誤
- 分離多個 Claude 實例以保持每個會話乾淨
- 動態調整 agent 數量基於任務複雜度

**指揮官模式（Conductor Pattern）**
單人開發者或小團隊成員扮演指揮官，協調多個 agent 執行獨立任務：
- Agent 1: 核心功能開發
- Agent 2: 測試自動化
- Agent 3: 文件化
- Agent 4-5: 平行 refactoring/探索

**品質保證機制**
- 自動化測試作為驗證基礎
- 瀏覽器檢驗進行前端驗證
- 代碼審查在多 agent 輸出合併前執行

---

## 關鍵引用與數據

> 「給 Claude 一個驗證其工作的方法」是品質最重要單一因素

**並行 Agent 規模**: 5-15 個 Claude 實例同時運行  
**知識庫**: 共享 CLAUDE.md 隨時間形成複合知識庫  
**協調工具**: iTerm2 通知、終端標籤、git worktrees 隔離  
**團隊知識**: 文件化錯誤與模式形成可重複框架

---

## 工作流程特色

多 agent 方法相比單一 agent 的主要優勢：
- 平行執行加速開發（5-15x 會話數取決於任務複雜度）
- 知識累積保障長期效能
- 計畫優先策略減少錯誤
- 驗證迴圈確保品質

此方法論適用於個人開發者與團隊，展示了如何將 Claude Code 從單一工具擴展至協調多 agent 系統。

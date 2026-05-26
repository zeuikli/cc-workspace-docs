---
url: "https://mindwiredai.com/2026/03/25/claude-code-creator-workflow-claudemd/"
title: How the Creator of Claude Code Actually Uses It
type: article
---

# How the Creator of Claude Code Actually Uses It

**原始 URL**: https://mindwiredai.com/2026/03/25/claude-code-creator-workflow-claudemd/

**作者**: roro_ai  
**發佈日期**: 2026 年 3 月 25 日  
**來源**: MindWired AI

---

## 核心摘要

本文介紹了 Claude Code 創造者、Anthropic 員工工程師 Boris Cherny 在 2026 年 1 月公開分享的開發工作流程與配置實踐。他的方法核心圍繞著一份簡潔的 CLAUDE.md 檔案（約 100 行），概述了系統化的 AI 輔助編碼最佳實踐。

### 核心哲學
Cherny 強調「幾乎所有最佳實踐都歸結為一件事：上下文視窗管理」。他優先考慮簡潔性、消除不必要的指令，以及圍繞 AI 建立系統，而不是微管理它。

### 三大核心原則
1. **簡潔優先** — 最小化、聚焦的變更
2. **不懶惰** — 解決根本原因，避免臨時修補
3. **最小影響** — 僅修改必要部分

### 任務管理迴圈
計畫 → 驗證 → 追蹤 → 解釋 → 文件化 → 通過 CLAUDE.md 更新捕獲教訓

---

## 關鍵實踐

**並行執行與效率**
- 每日同時運行 10-15 個 Claude 會話，使用獨立的 git worktrees
- 運用「計畫模式」進行複雜任務，先迭代確認策略再執行
- 慷慨使用 subagents 保持乾淨的上下文視窗
- 應用「不要陪護」(Don't babysit) 原則

**文件與學習**
- 將 CLAUDE.md 視為活文件，在出現錯誤時更新
- 記錄教訓與模式，形成可重複的決策框架
- 團隊知識累積優於個人知識

---

## 關鍵引用與數據

> 「幾乎所有最佳實踐都歸結為一件事：上下文視窗管理。」— Boris Cherny

**並行執行規模**: 10-15 個同時 Claude 會話，經由分離的 git worktrees 隔離  
**CLAUDE.md 大小**: 約 100 行，作為系統化方法的核心檔案

此方法論適用於編碼以外的 AI 協作場景，展示了縱向擴展人類-AI 協作的可能性。

---

## 工作流程適用性

該方法論強調長期系統建設而非個別會話最佳化，透過文件化與知識累積實現團隊層級的 AI 效能提升。

# How Boris Uses Claude Code: A Comprehensive Guide

**原始 URL**: https://howborisusesclaudecode.com/

**作者**: Boris Cherny（Anthropic Claude Code 創造者）及團隊成員  
**發佈日期**: 自 2026 年 1 月 2 日起（持續更新至 2026 年 5 月）  
**來源**: X (Twitter) 執行緒與編譯網站

---

## 核心摘要

本資源彙編了 Boris Cherny 工作流程中的 89+ 實踐技巧，跨越 2026 年 1 月至 5 月多個執行緒。指南展示 Claude Code「開箱即用效果絕佳」，同時提供廣泛的客製化選項。核心理念是將 Claude Code 視為「平行執行引擎，而非聊天機器人」，強調前期規劃、持久知識建設與重複工作流程自動化。

### 並行執行與效率
- 使用分離的 git worktrees 同時運行 5+ Claude Code 實例
- 執行 `claude --worktree` 隔離平行會話
- 啟用自動模式以跳過權限提示，同時保持安全性

### 模型與配置
- 所有任務使用 Opus 4.5 搭配思考模式，因其工具使用優越性
- 維護共享的 CLAUDE.md 檔案，記錄學習到的更正
- 在 PR 審查中標記 @.claude 自動更新文件

### 工作流程最佳化
- 複雜任務先從計畫模式開始，再轉為自動接受編輯
- 在 .claude/commands/ 中為重複工作流程儲存斜線命令
- 為常見 PR 自動化實作 subagents

---

## 驗證與品質

**關鍵洞察**: 「給 Claude 一個驗證其工作的方法」能大幅改善結果
- 使用 Chrome 擴展進行前端測試與迭代
- 跨不同域執行驗證迴圈

---

## 進階功能

**批次與迴圈自動化**
- 使用 `/batch` 跨 worktrees 並行代碼遷移
- 配置 `/loop` 執行最長 3 天的重複任務（無人值守）
- 運用 `/goal` 讓 Claude 工作至完成條件達成

**上下文管理**
- 使用 `/rewind` 代替修正，避免污染上下文
- 區分 `/compact`（有損摘要）與 `/clear`（手動簡報）
- 設定 `CLAUDE_CODE_AUTO_COMPACT_WINDOW=400000` 避免上下文衰退

---

## 關鍵引用與數據

> 「將 Claude 視為委派的工程師，而非配對程序員」

**並行執行規模**: 5+ 同時 Claude Code 實例（git worktrees 隔離）  
**自動模式**: 啟用以跳過權限提示  
**模型標準化**: Opus 4.5 搭配思考模式所有任務  
**驗證效果**: 啟用自驗證迴圈可 2-3 倍提升最終品質

---

## 應用模式

該指南強調治療 Claude 為委派的工程師而非聊天機器人，事前完整提供任務上下文包括目標、約束與驗收標準。技巧跨越平行執行、模型選擇、計畫模式優先、文件化、自定義命令、subagents、自動化 hooks、驗證迴圈與工具集成等領域。

---
url: "https://pyshine.com/Andrej-Karpathy-Skills-LLM-Coding-Guidelines/"
title: "Andrej Karpathy Skills - LLM Coding Guidelines That Prevent Common Mistakes"
author: "PyShine"
date: 2026-04-09
status: SUCCESS
---

# Andrej Karpathy Skills: LLM Coding Guidelines That Prevent Common Mistakes

## 核心摘要

本文介紹了 `andrej-karpathy-skills` 倉庫中的四項核心原則，這些原則設計用來解決 LLM 輔助編碼中的常見陷阱。文章強調了這些指南如何通過改變 AI 代理的決策過程，從根本上改善代碼品質。

**識別的三大問題**

1. **無聲假設（Silent Assumptions）**：LLM 做出假設而無需尋求澄清，直接執行導致錯誤實現
2. **複雜過度（Unnecessary Complexity）**：LLM 傾向於用投機性功能和過度抽象化來膨脹代碼
3. **副效應編輯（Collateral Changes）**：修改代碼時無意中引入對無關部分的改動

**四項核心原則詳解**

**原則一：編碼前思考（Think Before Coding）**

在實施前，要求模型明確陳述其對需求的理解和假設。當遇到模糊指令時，應提出多個可能的解釋，由人類開發者選擇正確方向。這一原則改變了 AI 從被動執行者到主動問題求解者的角色。

**原則二：簡潔優先（Simplicity First）**

實現僅請求的功能，不添加投機性特性，不創建單用途的抽象層，不設計超出必要的靈活性。這個原則迫使 AI 考慮代碼的簡潔性，同時保持功能完整性。

**原則三：精準修改（Surgical Changes）**

進行最小化的、針對性的編輯。修改的每一行代碼都應直接歸因於用戶的請求。避免同時進行「代碼改進」、「風格統一」或「重構」——這些往往引入微妙的 bug。

**原則四：目標驅動執行（Goal-Driven Execution）**

將模糊的指令轉化為具體的、可測試的成功標準。與其說「修復這個問題」，不如說「寫一個復現問題的單元測試，然後讓測試通過」。這使 LLM 能夠獨立迭代直至達成明確的目標。

**安裝與使用**

該指南提供兩種使用方式：

1. **Claude Code 外掛**：將 Karpathy Skills 作為全局外掛安裝，一次性設置所有項目
2. **項目級 CLAUDE.md**：在每個項目根目錄放置 CLAUDE.md 檔案，允許按項目自定義

**設計哲學**

這些指南的設計遵循「謹慎優於速度」的原則，特別適用於非平凡的開發任務。簡單的解決方案不僅減少維護負擔，也大大降低了潛在 bug 的風險。

**應用場景**

- 複雜代碼重構
- 遺留系統現代化
- 關鍵路徑功能開發
- 跨模塊集成工作

## 關鍵引述

> "The models make wrong assumptions on your behalf and just run along with them without checking."
> — Andrej Karpathy（識別 AI 編碼的根本問題）

> "They really like to overcomplicate code and APIs, bloat abstractions..."
> — Andrej Karpathy（LLM 過度工程化的傾向）

> "Principles can be installed as Claude Code plugin or added as project CLAUDE.md file"
> — 靈活的實施選項

## 實踐建議

- **循序漸進**：先從核心的四項原則開始，根據實際情況逐步調整
- **團隊同步**：在團隊中分享 CLAUDE.md，確保對 AI 代理行為的共同理解
- **度量成效**：追蹤代碼審查時間、修訂次數等指標，量化改善效果
- **持續改進**：根據項目特點定製原則，但保持核心思想不變

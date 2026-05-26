---
url: https://lucaberton.com/blog/karpathy-claude-md-llm-coding-principles-2026/
title: Karpathy's CLAUDE.md - 4 Principles for Better LLM Coding
author: Luca Berton
date: 2026
status: SUCCESS
---

# Karpathy's CLAUDE.md: 4 Principles for Better LLM Coding

## 核心摘要

本文系統地介紹了 Andrej Karpathy 識別的四項可預測的 LLM 編碼失敗模式，以及通過編寫 `CLAUDE.md` 檔案中的行為約束如何有效解決這些問題。該文章強調了從命令式指示向聲明式目標轉變的重要性。

**四項失敗模式與對應解決方案**

**1. 無聲假設 (Silent Assumptions)**

問題：LLM 在模糊的需求面前做出假設並盲目執行，而不尋求澄清。

解決方案「編碼前思考（Think Before Coding）」：要求模型在實施前明確陳述其理解的假設，並呈現可選的解釋。這防止了構建錯誤解決方案所浪費的時間和努力。

**2. 過度複雜化 (Overcomplexity)**

問題：LLM 傾向於添加不必要的功能、創建過度靈活的設計、以及構建不會被重複使用的抽象層。

解決方案「簡潔優先（Simplicity First）」：編碼約束規定「最小化代碼解決問題」。不添加投機性功能，不為未來可能需要而預先鋪設支持。這直接對應於資深工程師的最佳實踐：「做最簡單的能工作的事情」。

**3. 範圍蔓延 (Scope Creep)**

問題：修改現有代碼時，LLM 會改進不相關的函式或重新格式化超出任務範圍的代碼。

解決方案「精準修改（Surgical Changes）」：約束要求只觸及必要部分，保留既有的代碼風格，避免在相鄰函式上進行改進。每一行改動都應能直接追溯至用戶請求。

**4. 模糊執行 (Vague Execution)**

問題：任務定義不清晰，AI 代理無法判斷何時完成，導致過度或不足執行。

解決方案「目標驅動執行（Goal-Driven Execution）」：將模糊的命令轉化為具體的、可驗證的成功標準。而不是「修復這個 bug」，改為「寫一個複現該 bug 的測試，然後讓測試通過」。這種方法使模型能獨立地反覆迭代直至達成明確的目標。

**為什麼有效**

該方法之所以有效，在於：

1. **零依賴**：無需新工具或額外配置，Claude Code 原生支持項目級的指令檔案
2. **通用適用**：這些原則適用於所有 AI 編碼工具，並與資深工程師的實踐對齊
3. **強制執行**：作為項目配置檔案，這些原則在每個會話自動加載和執行

**廣泛影響**

Karpathy 指出的原則不僅限於代碼生成。相同的思維框架也適用於：
- 內容創作（新聞、文章生成）
- 圖像生成（設計規範、視覺指南）
- 影片製作（腳本、編輯指令）

所有這些領域中，AI 工具都可能用不驗證的假設填充模糊的請求。

## 關鍵引述

> "The models make wrong assumptions on your behalf and just run along with them without checking."
> — Andrej Karpathy（AI 編碼的根本問題）

> "They really like to overcomplicate code and APIs, bloat abstractions..."
> — Andrej Karpathy（過度工程的典型表現）

> "State assumptions explicitly and seek clarification before implementation rather than silently proceeding with interpretations"
> — Think Before Coding 的核心實踐

## 實踐價值

- **立即可用**：複製 CLAUDE.md 到項目根目錄
- **持續有效**：在每個 Claude Code 會話自動加載
- **可定制**：根據項目需求調整原則
- **無破壞**：與現有工作流完全相容

---
url: "https://themenonlab.blog/blog/karpathy-claude-md-four-rules-ai-coding-agents"
title: "The Karpathy CLAUDE.md - Four Rules That Fix AI Coding Agents"
author: "Dr. Prahlad G. Menon"
date: 2026-04-19
status: SUCCESS
---

# The Karpathy CLAUDE.md: Four Rules That Fix AI Coding Agents

## 核心摘要

本文詳細分析了 Andrej Karpathy 與 Forrest Chang 合作推出的四項原則性規則，這些規則針對性地解決了 LLM 編碼代理中存在的三個根本問題：無聲的錯誤假設、過度複雜化和無意中修改不相關代碼。

**核心問題識別**

文章指出，AI 編碼代理重複表現出三個關鍵缺陷：代理做出無根據的假設並自信地繼續執行；它們傾向於將簡單的問題過度複雜化，添加不必要的功能和冗餘的抽象層；它們會不經意地修改或刪除自己不完全理解的代碼。這些問題導致龐大的 pull request、隱藏的 bug 和繁重的代碼審查負擔。

**四項原則的具體應用**

**編碼前思考（Think Before Coding）**要求代理在實施前進行明確的推理，呈現多個解釋選項，並在遇到模糊指令時尋求澄清而非猜測。此原則改變了代理的決策過程，使其成為一個合作者而非自主執行者。

**簡潔優先（Simplicity First）** 強調交付最小可行的解決方案，杜絕投機性功能、不必要的抽象層和超出範圍的功能。它與許多軟體開發最佳實踐一致，特別是「別想著要聰明」的原則。

**精準變更（Surgical Changes）**限制編輯範圍，要求每一行改動都能直接溯源到用戶的請求。這防止了「改進邊界代碼」的不良習慣，這種習慣即使代碼看起來更好，也往往引入微妙的 bug。

**目標驅動執行（Goal-Driven Execution）**將模糊的指令轉化為具體的、可驗證的成功標準。與其說「修復這個 bug」，不如說「寫一個再現 bug 的測試，然後讓它通過」。這種方法使 LLM 能夠獨立地反覆迭代直至達成目標。

**CLAUDE.md 的運作機制**

`CLAUDE.md` 檔案作為持久化的項目上下文存在，在每個代理會話開始時自動加載。這種設計使得無需額外工具或複雜配置，僅通過行為指南就能實現一致的編碼標準。該檔案通常不超過 70 行，設計上保持簡潔以避免消耗過多的 AI 上下文窗口。

**實證成效**

根據社區反饋和案例研究，採納這四項原則可以顯著改善 AI 生成代碼的品質和可靠性。代碼審查時間減少、無關修改幾乎消失，而且 AI 和人類開發者之間的合作變得更加高效。

## 關鍵引述

> "The models make wrong assumptions on your behalf and just run with them without checking"
> — Andrej Karpathy

> "Every changed line should trace directly to the user's request"
> — Surgical Changes 的核心原則

> "State assumptions explicitly before coding, present multiple interpretations, and ask for clarification rather than guessing"
> — Think Before Coding 的要點

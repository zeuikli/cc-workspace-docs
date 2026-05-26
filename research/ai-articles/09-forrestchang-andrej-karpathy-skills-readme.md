---
url: https://github.com/forrestchang/andrej-karpathy-skills
title: Andrej Karpathy Skills - Claude Code Guidelines (GitHub Repository)
author: Forrest Chang
date: 2026
status: SUCCESS
---

# Andrej Karpathy Skills: Claude Code Guidelines

## 項目概述

**名稱**：Karpathy-Inspired Claude Code Guidelines  
**作者**：Forrest Chang（開源社區貢獻者）  
**倉庫**：forrestchang/andrej-karpathy-skills  
**數據**：135,000+ 顆星，13,800+ forks

## 項目目標

這是一個單一 `CLAUDE.md` 配置檔案，設計用來改善 Claude Code 的編碼行為。該檔案基於 AI 研究者 Andrej Karpathy 對 LLM 編碼常見錯誤的觀察。

## 四項核心原則

**1. 編碼前思考（Think Before Coding）**

避免隱藏假設；在實施前明確呈現困惑和權衡。當面對模糊需求時，提出多個解釋選項，讓人類開發者確認正確方向，而非自信地猜測。

**2. 簡潔優先（Simplicity First）**

編寫僅解決陳述問題的最小代碼。拒絕過度工程化、不必要的抽象層和投機性功能。遵循「做最簡單能工作的事」的原則。

**3. 精準修改（Surgical Changes）**

僅修改必要部分；保留既有代碼風格和約定。避免改進不相關的代碼段或進行不相關的重構。每一行改動都應能直接追溯至用戶請求。

**4. 目標驅動執行（Goal-Driven Execution）**

將任務轉化為可驗證的成功標準。例如，不說「修復這個 bug」，改為「寫一個複現 bug 的測試，然後讓測試通過」。這使 LLM 能獨立地迭代直至目標達成。

## 解決的關鍵問題

該指南針對三個主要問題：

1. **無根據的假設配合無聲接受**：AI 做出假設後盲目執行，不尋求澄清
2. **過度複雜的解決方案**：AI 傾向於添加不必要的功能和冗長的抽象層
3. **無意中的代碼修改**：修改無關代碼段，引入難以追蹤的副效應

## 安裝方法

**方法一：Claude Code 外掛**

通過市場安裝：`forrestchang/andrej-karpathy-skills`（全局配置，一次性設置）

**方法二：按項目配置**

直接將 CLAUDE.md 檔案複製到你的項目根目錄。這允許根據特定項目的需求進行定製。

## 核心洞察

根據 Karpathy 的觀點：**將含糊的命令式指示轉化為聲明式目標，使 LLM 能有效地循環達成完成條件**。

這一轉變改變了人類與 AI 的互動模式，從簡單的「做這件事」到「達成這個明確的、可驗證的結果」。

## 實踐價值

- **零依賴**：無需新工具或複雜配置
- **立即生效**：文本檔案，無須安裝或編譯
- **高效可組合**：可與其他專案實踐層層堆疊
- **持久記憶**：CLAUDE.md 在每個會話自動加載，提供一致的指導

## 社區反應

該項目在 GitHub 社區中引起了廣泛共鳴，許多開發者報告了使用這些指南後的顯著改進：
- 代碼審查時間大幅減少
- 無關修改幾乎消失
- AI 與人類開發者的協作效率提升
- 整體代碼品質和可維護性改善

## 擴展與變體

該概念已衍生出針對其他 AI 工具的變體，如 GEMINI.md（用於 Gemini）和 AGENTS.md（用於代理系統），展示了這一方法論的通用適用性。

## 許可證

MIT License（開源，允許自由使用和修改）

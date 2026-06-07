---
title: "歐洲天然氣交易平台：Claude Code 6人團隊生產案例，測試覆蓋率85%→95%"
author: "Boldare"
date: 2026-06-07
source: "https://www.boldare.com/blog/claude-code-production-case-study/"
tags: [claude-code, production, case-study, european-gas-trading, team-workflow, test-coverage, sprint-velocity]
topic: "歐洲天然氣交易平台，6人團隊，85%→95% 測試覆蓋率，sprint velocity +15-31%"
---

# 歐洲天然氣交易平台：6人團隊 Claude Code 生產案例

一個受監管的歐洲天然氣容量交易平台，6 名開發者組成的 Scrum 團隊，在 Q4 2025 導入 Claude Code 後的量化成果記錄。

## 團隊與技術堆疊

- **團隊**：6 名開發者 + 1 Product Owner + 1 Scrum Master
- **專案類型**：受監管的歐洲天然氣容量交易平台，event-driven 架構
- **技術堆疊**：React、Java/Spring、EventStore、PostgreSQL、Redis、DocumentDB、AWS、GitLab CI/CD

## 量化成果

| 指標 | 數值 |
|------|------|
| 測試覆蓋率 | ~85% → ~95% |
| Sprint velocity | +15% → +31%（13→15→17 story points） |
| AI 輔助新代碼比例 | 75–85% |
| AI 輔助測試撰寫 | 85% |
| AI 輔助 ADR 文件 | 70% |
| AI 輔助 Code Review | 50% |

## 工具分工策略

| 層級 | 工具 | 比例 |
|------|------|------|
| Frontend | Cursor + Claude | ~50% / ~50% |
| Backend | Claude Code + GitHub Copilot | ~90% / ~10% |

## 導入時間軸

- **Q4 2025**：2 名開發者完成正式訓練；全團隊 onboarding session
- **Q4 2025**：實踐模式穩定化並文件化
- **2026 年 1 月**：新成員加入後無需額外訓練，直接採用既有模式

## 核心洞察

> "Embedding AI tools into a production team is primarily a process decision, not a technology one."

最大價值出現在「高量、低認知負擔」的工作（測試、文件），而非複雜問題解決。這從根本上改變了團隊在交付壓力下延後或放棄品質工作的傾向。

AI 工具的存在使**本來會因時間壓力跳過的品質工作（85→95% 測試覆蓋率）變得可行**——不是因為工具代替了思考，而是降低了執行成本。

## Key Insights
- 測試覆蓋率從 85% 到 95% 的改善，核心是「AI 使撰寫測試的邊際成本降低」，而非開發者突然更勤奮
- Sprint velocity +15–31% 的區間顯示個人差異仍大——工具賦能效果因開發者習慣和任務類型而異
- Backend 90% 使用 Claude Code（而非 Cursor）反映 Java/Spring 生態系中 IDE 整合的成熟度差異
- 新成員能無縫採用既有 AI 工作模式，說明文件化的 AI workflow 本身具有可傳承性

## Code Examples / Commands

```bash
# Backend（Java/Spring）典型工作流
# 以 Claude Code 生成測試（85% AI 輔助率）
# 輸入：「為 GasCapacityTradingService.allocateCapacity() 生成完整單元測試，
#        涵蓋邊界條件：容量為零、超額分配、並發請求」

# Frontend（React）典型工作流
# Cursor + Claude 各 50%，視任務類型切換
# UI 組件生成 → Cursor
# 業務邏輯 + EventStore 整合 → Claude Code

# ADR 文件生成（70% AI 輔助）
# 輸入：「根據我們選擇 EventStore 的討論，生成 ADR-023 草稿」
```

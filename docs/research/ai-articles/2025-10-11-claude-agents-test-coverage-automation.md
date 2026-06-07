---
title: "How we use Claude Agents to automate test coverage"
author: "Alexander Melnik"
date: 2025-10-11
source: "https://dev.to/melnikkk/how-we-use-claude-agents-to-automate-test-coverage-3bfa"
tags: [claude-code, testing, sub-agent, coverage, typescript, feedback-loop]
topic: testing
---

# How we use Claude Agents to automate test coverage

Alexander Melnik 記錄了一套雙 agent 回饋迴圈系統，在不到一週內將測試覆蓋率從 30% 提升至接近 50%（+20pp）。系統存放在 `.claude/agents/` 目錄，由兩個角色分工：寫測試的 specialist 與驗品質的 reviewer。

## 雙 Agent 架構

**Agent 1：typescript-test-specialist**
負責撰寫完整的 unit 與 integration tests。核心能力：
- 使用 `mcp__ide__getDiagnostics` 工具驗證語法正確性與 TypeScript type safety
- 套用 Red-Green-Refactor TDD 循環
- 覆蓋 happy paths、edge cases、error conditions、boundary values
- 實作適當的 TypeScript typing 包含 generic constraints

**Agent 2：test-quality-reviewer**
純粹審查角色，工具限制為 Read/Write/Edit/Bash/Grep，不能呼叫外部服務。功能：
- 評估測試的品質與覆蓋完整性
- 輸出「核准」或「需要改進」兩種決定
- 若需改進，提供具體的改進要求給 specialist

## 回饋迴圈流程

四步驟循環：
1. **Implement**：specialist 撰寫測試，用 `mcp__ide__getDiagnostics` 確認無 type error
2. **Review**：reviewer 評估品質，判斷是否達到門檻
3. **Refine**：specialist 根據 reviewer 意見改進
4. **Document**：記錄最終覆蓋狀態，加入手動驗證 gate

## CLAUDE.md 持久記憶機制

CLAUDE.md 儲存專案專屬需求與測試門檻，每次互動自動載入。Roadmap template 採三級優先排序（Critical/Medium/Minor），按業務影響排序。

## 驗證指標

| 指標 | 數值 |
|------|------|
| 初始覆蓋率 | ~30% |
| 最終覆蓋率 | ~50% |
| 時間 | 不到一週 |
| 覆蓋率提升 | ~20pp |

## Key Insights
- 雙 agent 回饋迴圈：typescript-test-specialist（使用 `mcp__ide__getDiagnostics` 寫測試）+ test-quality-reviewer（唯讀，核准或要求改進）
- 驗證指標：30% → ~50% 覆蓋率，不到一週，+20pp
- Reviewer 工具限制為 Read/Write/Edit/Bash/Grep，強制角色分離，防止 reviewer 直接修改業務邏輯

## Code Examples / Commands

```bash
# Agent 存放路徑
.claude/agents/typescript-test-specialist.md
.claude/agents/test-quality-reviewer.md
```

```markdown
# typescript-test-specialist 工具配置
tools:
  - mcp__ide__getDiagnostics  # 驗證 TypeScript 型別與語法
  - Read
  - Write
  - Edit
  - Bash
  - Grep

# test-quality-reviewer 工具配置（僅讀寫，無外部呼叫）
tools:
  - Read
  - Write
  - Edit
  - Bash
  - Grep
```

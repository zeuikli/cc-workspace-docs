---
title: "Claude Code Advanced Workflow — Subagents、Commands、Multi-Session"
author: "Jangwook Kim"
date: 2026-06-07
source: "https://dev.to/jangwook_kim_e31e7291ad98/claude-code-advanced-workflow-subagents-commands-multi-session-50hl"
tags: [claude-code, subagents, skills, multi-session, writer-reviewer, fan-out, agents-md]
topic: Writer/Reviewer pattern，fan-out migration，Skills vs CLAUDE.md 決策矩陣
---

# Claude Code Advanced Workflow — Subagents、Commands、Multi-Session

進階 Claude Code workflow 的三大核心：subagent 隔離、可重用 Skills（自訂指令）、以及多 session 協作模式。

## Subagent 設定

**目的**：隔離複雜任務，保護主 context。Subagent 有獨立 context window 與 tool restriction，只回傳摘要給主 session。

**關鍵判準**：「當任務需要讀取大量檔案或探索 codebase 時使用 subagent。」

```yaml
# .claude/agents/security-reviewer.md
---
name: security-reviewer
description: "Reviews code for security vulnerabilities"
tools: Read, Grep, Glob, Bash
model: opus
---
[專業審查指示]
```

實際案例：Effloow 使用 content QA agent 在發布前驗證文章，讓主 session 專注在部署。

## Skills（自訂指令）結構

Skills 是可重用 workflow，存於 `.claude/skills/`，透過 slash command（如 `/fix-issue 1234`）按需啟動。

```yaml
# .claude/skills/deploy/SKILL.md
---
name: deploy
description: Deploy the current branch
disable-model-invocation: true
---
[多步驟 workflow 步驟]
```

## Skills vs CLAUDE.md 決策矩陣

| 類型 | 適用場景 | 載入時機 |
|------|----------|----------|
| **CLAUDE.md** | 全域規則、build 指令、repo 慣例 | 每個 session |
| **Skills** | Workflow 程序、領域特定任務、整合序列 | 按需（slash command 觸發） |

## 多 Session 協作模式

**Writer/Reviewer Pattern**
用新鮮 context 將實作與審查分離：
- Session A（Writer）：實作程式碼
- Session B（Reviewer）：無實作偏見的獨立審查

**Test-First Pattern**
- Session A：撰寫完整測試
- Session B：實作程式碼通過測試（避免「先有實作影響測試」的捷徑）

**Non-Interactive Mode（批次自動化）**
```bash
claude -p "prompt" --allowedTools "Read,Bash" --no-session-persistence
```
用於 CI 整合、批次操作。

**Fan-Out Migration（大規模重構）**
```bash
# 生成任務清單後，對數百個檔案循環執行
for file in $(cat task_list.txt); do
  claude -p "Refactor $file to use new API" --allowedTools "Read,Write,Bash"
done
```

## AGENTS.md 設定

每個 agent 有角色專屬指令檔案，疊加在 CLAUDE.md 之上，不污染共用設定。定義：
- 角色與職責
- Codebase 焦點範圍
- Agent 間通訊協定
- 必要 checklist

## Key Insights
- **Context 保護是 subagent 的核心價值**：sidechain transcript 讓 subagent 的 verbosity 不污染主 session context，是大任務能維持主 session 清晰的關鍵
- **Skills 比 CLAUDE.md instruction 更適合 workflow**：CLAUDE.md 每 session 都載入，塞太多 workflow 指示會浪費 token；Skills 按需載入才是正確的 token 效率選擇
- **Writer/Reviewer 分 session 比單一 session 更客觀**：同一 session 裡先寫後審容易帶入「我知道我的意圖」的偏見，分離 context 強制客觀

## Code Examples / Commands

```bash
# Fan-out migration 範例
cat task_list.txt | while read file; do
  claude -p "Refactor $file: replace deprecated fetchData() with useQuery() hook" \
    --allowedTools "Read,Write" \
    --no-session-persistence \
    --max-turns 10
done
```

```bash
# Writer/Reviewer pattern
# Session 1 — Writer
claude -p "Implement the authentication middleware per spec in SPEC.md"

# Session 2 — Reviewer (新 session，無 Session 1 context)
claude -p "Review the authentication middleware in src/middleware/auth.ts for security issues and correctness"
```

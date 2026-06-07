---
title: "Six Lessons from Designing Claude Code Skills"
author: "AgentStack Team"
date: 2026-05-04
source: "https://dev.to/agentstackteam/six-lessons-from-designing-claude-code-skills-1df3"
tags: [claude-code, skills, slash-commands, skill-design, frontmatter, composability, banlist]
topic: slash-commands
---

# Six Lessons from Designing Claude Code Skills

AgentStack 從設計 Claude Code skills（slash commands）的實務中歸納六條關鍵原則，包含反直覺的長度最適曲線（U 形）與負面約束優於正面規範的發現。

## 六條核心 Lessons

**Lesson 1 — 精準觸發優於寬鬆觸發（Opinionated Triggers Beat Permissive Ones）**
窄化的觸發邏輯防止誤觸，建立使用者信任。範例：shipping-checklist 只在「ready to ship」與「deploying to prod」時觸發，刻意排除日常 commit。過度寬鬆的觸發讓使用者不確定何時 skill 會啟動。

**Lesson 2 — 程式碼接地輸出優於模板驅動輸出（Code-Grounded Outputs）**
Skill 應在生成輸出前掃描實際 codebase。每個 checklist 項目引用真實路徑：`src/api/webhook.ts:42 — JSON.parse is unguarded`。幻覺的檔案路徑會摧毀信用度。

**Lesson 3 — Skill 長度最適為 U 形曲線**
甜蜜點：**250-450 字的命令式流程 + 100-200 字的 edge cases**。
- 太短：Claude 自由發揮，輸出不一致
- 太長：指令過多反而降低模型效能（矛盾但已驗證）
- 最長的 skills 往往效果最差

**Lesson 4 — Banlist 優於 Stylelist（負面約束優於正面規範）**
禁止使用詞彙（leverage、synergy、delightful）比規定語氣更有效。
- 負面約束強迫更好的即興發揮
- 「不要說 X」比「要說得像 Y」更精確

**Lesson 5 — 可組合性優於個別能力（Composability Trumps Capability）**
相互引用的 skills 形成 workflow 而非孤立工具。範例：`competitor-deep-dive` 的輸出直接餵給 `pricing-page-generator`，形成流水線。

**Lesson 6 — Description Frontmatter 嚴重被低估**
這個欄位控制 skill 的 fuzzy-match 觸發：
- 應包含「Use when...」使用者實際會說的短語
- 描述品質直接決定 skill 被正確啟動的機率
- 是 skill 設計中最少被關注但最重要的元素

## 四大反模式

1. **Generic templates**：產出通用答案，失去 skill 的精確性優勢
2. **Hallucinated file paths**：虛構的路徑引用摧毀 skill 信用度
3. **過度詳細的指令**：超過 U 形曲線右側導致模型困惑
4. **行銷陳腔濫調**：在語氣設計中使用 leverage/synergy/delightful

## Key Insights
- U 形 skill 長度最適：250-450 字命令式流程 + 100-200 字 edge cases；更長反而降低模型效能
- Banlist（禁止「leverage」、「synergy」、「delightful」）優於 stylelist——負面約束強迫更好的即興發揮
- Description frontmatter 嚴重被低估：「Use when...」短語控制 fuzzy-match 啟動；skill 可組合性建立 workflow vs. 孤立工具

## Code Examples / Commands

```markdown
---
# skill frontmatter 範例（.claude/commands/shipping-checklist.md）
description: |
  Use when: ready to ship a feature, deploying to prod, or creating a release.
  Do NOT use for: routine commits, work-in-progress reviews, or local testing.
  Triggers on: "ready to ship", "deploying to prod", "release checklist"
---

## Process
1. Scan codebase for unguarded JSON.parse calls
2. Check for missing error boundaries in React components  
3. Verify all environment variables are documented
4. ...

## Edge Cases
- If deploying to staging only, skip steps 4-6
- If hotfix, run only critical security checks (steps 1-3)
```

```markdown
# Voice banlist 範例（在 skill 中加入）
## Voice Guidelines
Never use: leverage, synergy, delightful, seamless, robust, empower, unlock
Never start sentences with: "Certainly", "Of course", "I'd be happy to"
```

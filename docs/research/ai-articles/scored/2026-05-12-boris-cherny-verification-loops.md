---
url: "https://x.com/bcherny/status/2007179861115511237"
date: 2026-05-12
scored: 2026-05-16
source: "Twitter/X — Boris Cherny (@bcherny)"
source_file: ../2026-05-12-boris-cherny-verification-loops.md
source_tier: C
tags: [verification-loops, quality-multiplier, stop-hooks, bcherny, claude-code-creator]
---

# Boris Cherny on Verification Loops

**原始來源**：https://x.com/bcherny/status/2007179861115511237  
**作者**：Boris Cherny（Claude Code 創建者，Anthropic）

---

## TL;DR

Claude Code 創建者 Boris Cherny 的直接建議：給 Claude 驗證自己工作的機制，是提升輸出品質「最重要的一件事」，可達 2-3x 品質提升。不是工具選擇、不是 prompt 技巧——是驗證迴路。

---

## 核心主張

> "A final tip: probably the most important thing to get great results out of Claude Code — give Claude a way to verify its work. If Claude has that feedback loop, it will 2-3x the quality of the final result."

- **2-3x 品質提升**：有 feedback loop vs 無 feedback loop 的差距
- **驗證形式**：跑測試、bash 指令、UI 截圖比對、任何能判斷「是否正確」的機制
- **實際應用**：Stop hooks 做確定性驗證；background agents 做長任務驗證；/loop 做定期驗證

---

## cc-workspace 可行動性

- `core.md § 驗證與品質` 已有 R4 goal-oriented 原則，但缺乏「2-3x」的量化錨點
- 此推文提供第一手實測依據，可強化「驗證是最高槓桿操作」的論述

---

## 評分

| 維度 | 分數 | 理由 |
|------|------|------|
| A. Workspace 可行動性 | 8/10 | Stop hooks + background agent 驗證模式可直接套用；「2-3x」量化錨點強化現有 R4 |
| B. 創新性 | 6/10 | cc-workspace core.md R4 已有驗證原則；此文主要提供一手量化依據，非全新概念 |
| C. 證據品質 | 6/10 | 直接引用 Claude Code 創建者；「2-3x」為個人實測斷言，無控制實驗（上限 6/10 for anecdote） |
| D. 技術深度 | 4/10 | 推文格式，具體度有限；Stop hooks / background agent 僅提及，無實作細節 |
| E. 泛化性 | 8/10 | 驗證迴路原則適用所有 Claude Code workflow，不限特定任務類型 |
| **加權總分** | **6.6/10** | 8×0.3 + 6×0.2 + 6×0.2 + 4×0.15 + 8×0.15 = 2.40+1.20+1.20+0.60+1.20 |

**整合決策**：Rule（驗證原則補充到現有規則，非新增 Skill）  
**整合位置**：`.claude/rules/core.md` § 驗證與品質 — 補充「2-3x 品質乘數」量化錨點與 Stop hook 驗證建議  
**整合狀態**：待實作

---

## TODO

- [ ] 在 `.claude/rules/core.md` § 驗證與品質段落，加入 bcherny 的量化引用（2-3x quality from verification loop）
- [ ] 確認 Stop hooks 驗證模式已在 workspace 設定（settings.json hooks 區塊）

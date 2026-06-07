---
url: "https://code.claude.com/docs/en/best-practices"
date: 2026-05-12
scored: 2026-05-16
source: code.claude.com (Anthropic Official)
source_file: ../2026-05-12-claude-code-best-practices.md
source_tier: O
tags: [claude-code, best-practices, session-management, scaling-patterns, failure-patterns, official]
---

# Claude Code Best Practices (Official Anthropic Documentation)

**原始來源**：https://code.claude.com/docs/en/best-practices  
**來源層級**：O（Official Anthropic documentation）

---

## TL;DR

Anthropic 官方 Claude Code 最佳實踐文件。最有價值的是「Common Failure Patterns to Avoid」的五類模式分類（kitchen sink / over-correction / over-specified CLAUDE.md / trust-then-verify gap / infinite exploration），及 Scaling Patterns（並行 session、auto mode、fan-out）。多數原則已隱含於 cc-workspace，但命名分類提供更清晰的心智模型。

---

## 核心主張

### 五大失敗模式（高價值分類）

1. **Kitchen sink session**：多任務間 context 混雜 → Fix: `/clear` 
2. **Correcting over and over**：兩次修正失敗後 `/clear`，重寫更好的 initial prompt
3. **Over-specified CLAUDE.md**：重要規則被雜訊淹沒 → ruthlessly prune
4. **Trust-then-verify gap**：實作看起來對但沒有驗證 → always provide verification
5. **Infinite exploration**：context 被數百個文件佔滿 → scope narrowly or use subagents

### Scaling Patterns

- **Non-interactive mode**：`claude -p "prompt"` 用於 CI/pre-commit hooks/scripts
- **Parallel sessions**：worktrees + desktop app + cloud（對應 bcherny 的 50-150 PRs/day）
- **Fan out across files**：`claude -p` loop 批次操作
- **Auto mode**：classifier 持續自主執行 + background safety checks

---

## cc-workspace 可行動性（新增 vs 現有）

| 原則 | cc-workspace 現狀 | 新增價值 |
|------|-----------------|---------|
| 驗證迴路 | core.md R4 | 失敗模式 #4 命名強化 |
| 失敗模式分類 | 未明確分類 | ★ 五類命名 + Fix 可直接加入 output-discipline.md |
| Scaling patterns | subagent-strategy.md 部分涵蓋 | ★ fan-out / auto mode / non-interactive 尚未明確 |
| CLAUDE.md pruning | CLAUDE.md ≤200 行 | 「ruthlessly prune」的明確理由補充 |

---

## 評分

| 維度 | 分數 | 理由 |
|------|------|------|
| A. Workspace 可行動性 | 8/10 | 五類失敗模式命名 + Scaling Patterns 尚未完整編碼進 cc-workspace；官方文件提供明確理由補充現有規則 |
| B. 創新性 | 6/10 | 多數原則概念上已在 workspace；失敗模式分類法和 auto mode / fan-out 描述是邊際增量 |
| C. 證據品質 | 9/10 | Anthropic 官方文件（O-tier），最高可信度 |
| D. 技術深度 | 7/10 | 提供清晰的策略與失敗模式；缺乏實作細節（hooks/settings 具體配置） |
| E. 泛化性 | 10/10 | 官方文件適用所有 Claude Code 使用者，無特化情境 |
| **加權總分** | **8.0/10** | 8×0.3 + 6×0.2 + 9×0.2 + 7×0.15 + 10×0.15 = 2.40+1.20+1.80+1.05+1.50 |

**整合決策**：Rule（補充失敗模式分類）+ Reference doc（官方完整文件留存）  
**整合位置**：
- 失敗模式分類 → `.claude/rules/output-discipline.md` 或 `core.md` § 失敗模式
- 完整文件 → `.claude/refs/claude-code-official-best-practices.md`（新建 reference）
- Scaling Patterns → `.claude/rules/subagent-strategy.md` § 平行 Session 策略

**整合狀態**：待實作

---

## TODO

- [ ] 在 `.claude/rules/core.md` 或 `output-discipline.md` 加入五類失敗模式的命名分類（Kitchen sink / Over-correction / Over-specified / Trust-then-verify gap / Infinite exploration）
- [ ] 在 `subagent-strategy.md` § 平行 Session 補充 auto mode + fan-out patterns
- [ ] 新建 `.claude/refs/claude-code-official-best-practices.md` 作為永久 reference link

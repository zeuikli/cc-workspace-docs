---
title: "5 Claude Code Agentic Workflow Patterns — Which One Fits Your Work?"
author: "Jangwook Kim"
date: 2026-06-07
source: "https://dev.to/jangwook_kim_e31e7291ad98/5-claude-code-agentic-workflow-patterns-which-one-fits-your-work-3mcg"
tags: [claude-code, agentic-workflow, patterns, orchestration, parallel, teams, autonomous]
topic: 五種 agentic workflow patterns，boundary definition
---

# 5 Claude Code Agentic Workflow Patterns

五種 Claude Code agentic workflow pattern，依控制層級排列：從最高控制的 Sequential 到最低介入的 Autonomous。

## 五種 Pattern

**1. Sequential（循序型）**
- 單一 agent，人工審查每個步驟
- 適用：「階段式任務、文件」等需要在步驟間驗證品質的工作
- 取捨：速度最慢，但控制最高

**2. Operator（操作員型）**
- 單一 agent，具備精確定義的 tool/bash 權限，執行複雜單一任務
- 適用：Tool 密集型工作，例如「分析 `src/` 下所有 TypeScript 檔案，建立報告並修復」
- 關鍵：權限必須事先透過 CLAUDE.md 精確定義

**3. Parallel（平行型）**
- 多個 agent 在隔離的 Git worktree 中同時處理獨立任務
- 適用：無共享依賴的功能開發、翻譯、測試套件
- 優勢：相較循序方式，吞吐量有顯著提升

**4. Teams（團隊型）**
- 多個 sub-agent 各有角色分工，由 orchestrator 統籌
- 適用：複雜多步驟 pipeline（content pipeline、code review→fix→test→deploy）
- 創新點：將 context 長度限制分散到各 agent，而非集中在單一 context

**5. Autonomous（自主型）**
- 完全自主執行，由 cron/事件觸發，人工介入極少
- 適用：已驗證的、排程的、重複的任務，且有明確成功條件
- 前置要求：必須有 rollback 機制與監控 alert

## 核心洞察：Boundary Definition

作者強調「邊界定義決定成敗，比 pattern 選擇本身更重要」。

**最常見失敗模式**：Operator pattern 中權限過於寬泛。

**建議**：從窄範圍開始，逐步擴展，比一開始就給予廣泛授權更安全。

## Pattern 選擇矩陣

| Pattern | 控制層級 | 適用規模 | 最大風險 |
|---------|----------|----------|----------|
| Sequential | 最高 | 小任務 | 速度瓶頸 |
| Operator | 高 | 中型複雜任務 | 權限過寬 |
| Parallel | 中 | 獨立子任務集 | 隔離不足 |
| Teams | 中低 | 複雜多步驟 | 協調開銷 |
| Autonomous | 最低 | 已驗證重複任務 | 無監控失控 |

## Key Insights
- **Boundary definition > pattern selection**：選錯 pattern 也能成功，但邊界不清幾乎必定失敗——尤其是 Operator 和 Teams 模式
- **Parallel pattern 要求 worktree 隔離**：多個 agent 修改同一 working tree 是 race condition 的根源，Git worktree 隔離是必要條件而非可選優化
- **Autonomous 是終點，不是起點**：Pattern 5 看似最強大，但需要先跑過其他模式驗證任務的確定性，才能安全移除人工監督

## Code Examples / Commands

```bash
# Parallel pattern — 多 worktree 啟動
git worktree add ../feature-auth feature/auth
git worktree add ../feature-payment feature/payment

# 在不同 terminal 各自執行
cd ../feature-auth && claude -p "Implement OAuth2 authentication"
cd ../feature-payment && claude -p "Implement Stripe payment integration"
```

```bash
# Autonomous pattern — cron 觸發
# 每日 2am 執行 dependency update 檢查
0 2 * * * /usr/local/bin/claude -p \
  "Check for outdated dependencies, update patch versions, run tests, commit if green" \
  --allowedTools "Bash,Read,Write" \
  --no-session-persistence \
  --max-turns 20 \
  >> /var/log/claude-auto-update.log 2>&1
```

```yaml
# Teams pattern — orchestrator 設定（CLAUDE.md）
# Orchestrator session 指示
你是 code review pipeline 的 orchestrator。
步驟：
1. 呼叫 code-reviewer agent 審查 PR
2. 若有問題，呼叫 code-fixer agent 修復
3. 呼叫 test-runner agent 驗證
4. 若全部通過，呼叫 deployer agent 部署
每步驟等待確認後再進行下一步。
```

---
title: "Claude Code Agent Farm — 20-50 並行 Agent 協調框架"
author: "Dicklesworthstone"
date: 2026-06-07
source: "https://github.com/Dicklesworthstone/claude_code_agent_farm"
tags: [claude-code, multi-agent, parallel, orchestration, tmux, lock-based]
topic: 20-50 個並行 agent 協調，lock-based coordination，adaptive stagger
---

# Claude Code Agent Farm — 20-50 並行 Agent 協調框架

Claude Code Agent Farm 是一套可並行執行 20–50 個 Claude Code agent 的 orchestration 框架（841 stars，2025-06-28 建立），用於系統性改善 codebase。支援自動 bug fixing、best practices implementation 與 lock-based 多 agent 協調。

## 核心架構：兩腳本系統

- **Python 腳本（claude_code_agent_farm.py）**：大腦，負責 agent 生命週期管理、任務分配、lock 協調
- **Shell/tmux 層**：視覺化監控，每個 agent 佔一個 tmux pane，支援 real-time dashboard

## 關鍵技術特性

**Lock-based Coordination（防衝突）**
- 使用 POSIX `flock()` 原語做檔案鎖
- 多個 agent 並行寫入時，atomic operation 確保不互相覆蓋
- Automatic settings backup/restore，含 size-based rotation

**Adaptive Stagger（防 API 爆量）**
- Agent 啟動使用 adaptive stagger 而非同時全部啟動
- 根據工作模式動態調整 idle timeout
- 偵測 context 接近上限時 agent 自動清除自身 context

**Auto-Recovery**
- Agent 失敗時自動重啟
- 雙 Ctrl+C 3 秒內 = force-kill（單次 = graceful shutdown）
- Ctrl+R = 廣播 `/clear` 給所有 agent

**34 技術棧支援**：Next.js、Python、Rust、Go、Java、Angular、Flutter、C++ 等

## 快速啟動

```bash
alias cc="ENABLE_BACKGROUND_TASKS=1 claude --dangerously-skip-permissions"

# 安裝與設定
git clone https://github.com/Dicklesworthstone/claude_code_agent_farm.git
cd claude_code_agent_farm
chmod +x setup.sh && ./setup.sh

# 環境健康檢查
claude-code-agent-farm doctor --path /path/to/project

# Bug fixing 模式（Next.js）
claude-code-agent-farm --path /path/to/project --config configs/nextjs_config.json

# Best practices 模式
claude-code-agent-farm --path /path/to/project --config configs/nextjs_best_practices_config.json
```

## 監控指標

- Context warning（接近上限預警）
- Heartbeat tracking（agent 存活確認）
- tmux pane title（每個 agent 狀態一目了然）
- Git commits with rich diff summaries
- HTML run report（完整執行報告）

## Key Insights
- **Lock-first 設計**：大量並行 agent 的最大問題是 race condition，POSIX flock 是 POSIX 相容最簡解，不引入外部協調服務
- **Context 自管理**：每個 agent 自行監控 context 使用量並觸發 `/clear`，比集中式管理更具彈性，避免單點失敗
- **Adaptive stagger > 固定間隔**：工作量波動大時固定間隔浪費 API rate limit，adaptive 依實際速度調整可顯著提升吞吐

## Code Examples / Commands

```bash
# 安裝 shell completion
claude-code-agent-farm install-completion --shell zsh

# JSON config 結構（variable substitution 支援）
{
  "max_agents": 20,
  "stagger_seconds": 2,
  "idle_timeout_adaptive": true,
  "context_clear_threshold": 0.85
}
```

```python
# 核心協調邏輯（lock-based）
import fcntl

def acquire_task_lock(task_file):
    fd = open(task_file, 'r+')
    fcntl.flock(fd, fcntl.LOCK_EX)  # POSIX exclusive lock
    return fd

def release_lock(fd):
    fcntl.flock(fd, fcntl.LOCK_UN)
    fd.close()
```

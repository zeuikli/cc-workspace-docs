---
title: "Spec-Driven Development with Claude Code in Action"
author: "Alexander Opalic"
date: 2026-02-01
source: "https://alexop.dev/posts/spec-driven-development-claude-code-in-action/"
tags: [claude-code, spec-driven, subagent, task-management, workflow, IndexedDB, SQLite]
topic: spec
---

# Spec-Driven Development with Claude Code in Action

Alexander Opalic 展示以 spec 文件作為 recovery point 的四階段開發工作流程，避免大型重構因 session 中斷而失去進度。驗證案例：SQLite/WASM → IndexedDB 遷移，~45 分鐘，14 個任務，14 個 atomic commits。

## 四階段工作流程

**Phase 1 — 平行 Sub-agent 研究**
Claude 產生多個獨立 research agent，各自調查不同面向：
- CRDT 同步策略
- WebSocket 連線管理
- Push/Pull 同步模式
- Storage adapter 設計
- 整體架構模式

各 agent 並行執行，匯整後形成完整技術視圖。

**Phase 2 — Spec 文件生成**
將研究結果合成單一技術規格文件（single source of truth）。Spec 包含：架構決策、API 設計、實作順序、預期行為。一旦 session 中斷，spec 文件即為重啟點。

**Phase 3 — AskUserQuestion 釐清**
Claude 使用 `AskUserQuestion` tool 在實作前釐清規格歧義。關鍵動作在實作前完成，防止假設錯誤導致大量返工。

**Phase 4 — Task 委派與 Atomic Commits**
每個離散任務委派給 sub-agent，每個任務完成後產生一個 atomic commit。14 個任務 = 14 個 commits，每步驟可逆、可審查。

## Task 持久化機制

Task 以 JSON 格式儲存在 `.claude/tasks/` 目錄：

```json
{
  "id": "task-001",
  "title": "Implement IndexedDB Storage Adapter",
  "status": "in_progress",
  "dependencies": [],
  "spec_reference": "spec.md#storage-adapter"
}
```

四個 Task 工具：
- `TaskCreate`：建立新任務
- `TaskUpdate`：更新狀態/進度
- `TaskList`：列出所有任務
- `TaskGet`：取得特定任務詳情

## 驗證指標

| 指標 | 數值 |
|------|------|
| 遷移工作（SQLite/WASM → IndexedDB） | ~45 分鐘 |
| 任務數量 | 14 個 |
| Commits | 14 個（atomic） |
| 主 orchestrator session context 使用率 | 71% |
| 技術框架參考 | Jazz framework |
| 平台 | Nuxt 4 sync engine |

71% context 使用率代表委派 pattern 有效防止 context 耗盡（協調多個 sub-agent 的同時）。

## Spec 作為 Recovery Point

「與順序方式不同，此 pattern 建立了『持久進度』——規格在 session 重啟後存活，在實作偏軌時提供恢復點。」

若某個 sub-agent 失敗或 session 崩潰，重啟後 Claude 讀取 spec 文件與 task JSON，可在正確狀態下繼續工作，而非從頭開始。

## Key Insights
- 四階段工作流程：平行 sub-agent 研究 → spec 文件生成 → AskUserQuestion 釐清 → task 委派 + atomic commits
- 驗證：SQLite/WASM→IndexedDB 遷移 ~45 分鐘，14 tasks，14 commits；71% context 使用率，協調多個 sub-agent
- Tasks 以 JSON 持久化在 `.claude/tasks/`，使用 TaskCreate/TaskUpdate/TaskList/TaskGet；spec = session 崩潰的 recovery point

## Code Examples / Commands

```json
// .claude/tasks/task-001.json
{
  "id": "task-001",
  "title": "Implement IndexedDB Storage Adapter",
  "description": "Replace SQLite WASM with IndexedDB following Jazz framework patterns",
  "status": "completed",
  "dependencies": [],
  "spec_reference": "spec.md#storage-adapter",
  "commit": "feat: add IndexedDB storage adapter (task-001)"
}
```

```markdown
# Spec 文件結構範例（spec.md）
## Architecture Decision
Replace SQLite/WASM with IndexedDB for better browser compatibility.

## Storage Adapter Interface
```typescript
interface StorageAdapter {
  get(key: string): Promise`<unknown>`
  set(key: string, value: unknown): Promise`<void>`
  delete(key: string): Promise`<void>`
}
```

## Implementation Order
1. Storage adapter interface (task-001)
2. IndexedDB implementation (task-002)
3. Migration utility (task-003)
...
```

```bash
# Pre-commit hooks 自動驗證（文中提及）
# 每個 task commit 前自動跑測試 + lint
# 失敗時 Claude sub-agent 自我修正
```

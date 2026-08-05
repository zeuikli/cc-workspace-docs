# Claude Code W25 新功能（v2.1.178–v2.1.183）

> **Source:** https://code.claude.com/docs/en/changelog  
> **Date Range:** 2026-06-15 ~ 2026-06-19  
> **Versions:** v2.1.178 / v2.1.179 / v2.1.181 / v2.1.183

---

## v2.1.178（2026-06-15）

### Agent Teams 簡化（Implicit Teams）

移除了 `TeamCreate` / `TeamDelete` 工具。每個 session 現在自動有一個隱含 team，直接用 `Agent` tool 的 `name` 參數 spawn 隊友即可。

**使用方式**：
```bash
# 啟用 Agent Teams
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
```

```typescript
// 舊（不再需要）
TeamCreate({ name: "review-team" })
Agent({ name: "reviewer", team_name: "review-team" })

// 新（直接 spawn）
Agent({ name: "reviewer", prompt: "Review the code in src/..." })
```

**Display mode 變化**：
- 預設從 `"auto"` 改為 `"in-process"`（所有 teammate 在主 terminal 內）
- 要用 split-pane 需明確設 `"auto"` 或 `"tmux"`

**最佳實踐**：
- Subagent 定義（`.claude/agents/`）可直接用名稱 reference 成 teammate
- 3-5 teammates 最適合 research/review 類任務
- 平行實作需確保各 teammate 擁有獨立 file set，避免衝突

---

### Permission Rule 新語法：`Tool(param:value)`

在 deny 和 ask 規則中支援對工具輸入參數進行精細控制。

```json
// settings.json
{
  "permissions": {
    "deny": [
      "Agent(model:opus)",         // 阻止 spawn Opus-level subagent（控制成本）
      "Agent(isolation:worktree)", // 阻止在 worktree 中 spawn agent
      "Bash(run_in_background:true)" // 阻止後台 Bash
    ]
  }
}
```

**規則**：
- 只能匹配 tool input 的 top-level scalar 欄位
- 支援萬用字元：`Agent(isolation:*)` 匹配任何 isolation 值
- **不支援** allow 規則（避免單一參數就視為整體安全）
- 既有 canonical 欄位（`command`/`file_path`/`url`）不能用此語法

---

### Nested Skills 目錄支援

`.claude/skills/` 的子目錄中的 Skills 現在可被載入。

```
.claude/skills/
  backend/
    postgres/SKILL.md    # → skill 名稱顯示為 "backend:postgres"
    api/SKILL.md         # → "backend:api"
  frontend/
    react/SKILL.md       # → "frontend:react"
```

**最佳實踐**：
- Monorepo 可在各 package 下建立 `.claude/skills/` 做 scope-specific skills
- Nested `.claude/` 配置採用「closest-wins」語義（最靠近工作目錄者優先）
- 避免 dir 名稱與 skill name 衝突，因為 `/config` autocomplete 以冒號分隔

---

### Bug Fixes（v2.1.178）

- 修復 stale websocket OOM crash
- 修復 Chrome OAuth 失敗
- 修復 subagent transcript 查看問題

---

## v2.1.179（2026-06-16）

### 串流中斷改善

- Mid-stream 連線中斷時**保留部分回應**（原本顯示 raw error），讓用戶看到已完成的部分
- WSL2 滑鼠滾輪回歸修復
- Sandbox glob 效能改善

---

## v2.1.181（2026-06-17）

### `/config key=value` Runtime 設定

在 session 中直接調整任何設定，無需手動編輯 `settings.json`。

```bash
/config thinking=false      # 關閉 extended thinking
/config effort=high         # 調整 effort level
/config --help              # 列出所有可用 shorthand keys
```

適用於：interactive、`-p` headless、Remote Control 三種模式。

**Toggle 行為改善**：Enter 和 Space 都可切換選項；Esc 存檔並關閉（原來 Esc 是取消）。

---

### API 斷線自動重試（Thinking 中）

API 連線在 thinking（extended thinking）過程中中斷時自動重試，不再需要手動重跑。

**修復**：Prompt caching 在自訂 `ANTHROPIC_BASE_URL` 和 Foundry 環境下不讀取 cache 的 bug → 升級到 v2.1.181+ 後 Foundry 環境可正常利用 cache。

---

### Idle Teammate 自動隱藏

Idle 狀態的 teammate row 30 秒後自動隱藏（仍在執行，發訊息即重新出現）；subagent 清單上限 5 列，超過加捲動提示。

---

### `sandbox.allowAppleEvents`（macOS）

新增 macOS opt-in 設定，讓 sandboxed 指令可以送 Apple Events（適合 AppleScript 工作流程）：

```json
{
  "sandbox": {
    "allowAppleEvents": true
  }
}
```

---

### Subagent 嵌套深度上限（5 層）

修正 subagent 嵌套無限制 bug，現在強制執行 **5 層**深度上限（background chain 同樣受限）。

**設計 workflow 時**：lead → L1 → L2 → L3 → L4 → 最終執行，超過需重新設計架構（改用 shared task list）。

---

### `CLAUDE_CLIENT_PRESENCE_FILE` 環境變數

設定後，當使用者在機器前時抑制行動推播通知：

```bash
# ~/.bashrc
export CLAUDE_CLIENT_PRESENCE_FILE=$HOME/.claude/presence
```

---

### Bun 升至 1.4

---

## v2.1.183（2026-06-19）

### Auto Mode 安全強化

Auto mode 新增對「未被明確要求的破壞性指令」的自動攔截，無法被 permission allow rules override：

| 指令 | 攔截條件 |
|------|---------|
| `git reset --hard` | 任何情況 |
| `git checkout -- .` | 任何情況 |
| `git clean -fd` | 任何情況 |
| `git stash drop` | 任何情況 |
| `git commit --amend` | 該 commit 非本 session 由 agent 建立 |
| `terraform destroy` / `pulumi destroy` / `cdk destroy` | 未明確指定 specific stack |

**最佳實踐**：
- Auto mode 下無需在 CLAUDE.md 另外寫「不要 reset --hard」類規則
- 若工作流需要這些操作，改用明確 prompt 讓攔截機制通過意圖確認

---

### 模型棄用警告

當請求的模型已棄用或被自動升版時，在 stderr（`-p` 模式）或 agent frontmatter 中顯示警告。

**CI 腳本**：監控 stderr 的 deprecation warnings，提前察覺模型切換。

---

### `attribution.sessionUrl` 設定

從 commits 和 PRs 中省略 `claude.ai` session URL：

```json
// ~/.claude/settings.json 或 .claude/settings.json
{
  "attribution": {
    "sessionUrl": false
  }
}
```

適用於有 IP 保密需求的企業環境。

---

### `/config --help` 支援

`/config --help` 現在列出所有可用設定 shorthand 及說明。

---

## 功能對照索引

| 功能 | 版本 | 日期 |
|------|------|------|
| Agent Teams 簡化（Implicit Teams）| v2.1.178 | 2026-06-15 |
| `Tool(param:value)` permission 語法 | v2.1.178 | 2026-06-15 |
| Nested `.claude/skills/` 目錄 | v2.1.178 | 2026-06-15 |
| 串流中斷保留部分回應 | v2.1.179 | 2026-06-16 |
| `/config key=value` 語法 | v2.1.181 | 2026-06-17 |
| API 斷線自動重試（Thinking 中）| v2.1.181 | 2026-06-17 |
| Prompt cache 修復（Foundry）| v2.1.181 | 2026-06-17 |
| Subagent 5 層深度上限 | v2.1.181 | 2026-06-17 |
| `sandbox.allowAppleEvents` | v2.1.181 | 2026-06-17 |
| `CLAUDE_CLIENT_PRESENCE_FILE` | v2.1.181 | 2026-06-17 |
| Auto mode 破壞性指令攔截 | v2.1.183 | 2026-06-19 |
| 棄用模型警告 | v2.1.183 | 2026-06-19 |
| `attribution.sessionUrl` 設定 | v2.1.183 | 2026-06-19 |

---

## 延伸閱讀

- [01-official-hooks-memory-settings.md](./01-official-hooks-memory-settings.md) — Hook 架構與 Permission 設定
- [32-dynamic-workflows.md](./32-dynamic-workflows.md) — Dynamic Workflows（W22）
- [38-steering-claude-code.md](./38-steering-claude-code.md) — 七種自訂機制總覽

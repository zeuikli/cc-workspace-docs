---
date: 2026-06-15
source: DAILY-RESEARCH/2026-06-15.md
topics: [us-gov-fable5-suspension, anthropic-safety-classifier-transparency, fable5-agentic-proactive-patterns, claude-code-nested-subagents-depth5, claude-code-session-cost-analysis]
type: session-report
---

# Session Report 2026-06-15 — Daily Research

## 執行概要

- **研究主題**：5 個（DAILY-TOPICS/2026-06-15.md 全覆蓋）
- **搜尋查詢**：5 次並行 WebSearch
- **頁面 Fetch**：2 次深度抓取（nested subagents、Fable 5 proactive）
- **研究日期**：補執行（實際產出日 2026-06-17）

---

## 本日研究成果摘要

### 最高價值發現（Top 3）

**#1 Model Fallback 成架構必要條件**（影響：Critical）
- US 政府出口管制 Jun 12 當天強制切斷 Fable 5 & Mythos 5 所有存取
- 先例意義：frontier model 可在幾小時內消失，任何 production harness 的單點依賴風險被實證
- 直接驗證 CLAUDE.md 的「fable → opus 4.8 fallback for safety domains」不夠廣：應擴展為全域 fallback 政策

**#2 Nested Subagents 模型分層節省 10×**（影響：High）
- Root=Opus / D1=Sonnet / D2+=Haiku 分層，每層 10× 輸入 token 差
- 三大陷阱中，「allowlist 在 sub-agent 內被忽略」是隱性 bug，必須用 `permissions.deny` 取代
- 實際 token 成本：depth 2-3 合理，depth 4-5 急劇膨脹

**#3 Safety Classifier 顯式通知原則**（影響：High）
- 靜默降級是反模式：用戶無法區分「全能力回應」vs「被降級的回應」
- 適用於 harness 工程：任何 capability downgrade（routing 到弱模型）必須在 trace 中明確標注

---

## 可實作 / 可測試內容

### P0 — 立即可執行（今日或明日，< 2 小時）

#### P0-A: `.claude/settings.json` 加入 nested subagent 防護

**問題**：Fable 5 + nested subagents 預設可能無限遞迴（allowlist 失效）

**實作**：
```json
// .claude/settings.json — 在 permissions.deny 加入
{
  "permissions": {
    "deny": [
      "Agent(general-purpose)"
    ]
  },
  "env": {
    "CLAUDE_CODE_SUBAGENT_MODEL": "claude-haiku-4-5-20251001"
  }
}
```

**驗證**：
```bash
# 確認 settings 包含 deny
grep -q "general-purpose" .claude/settings.json && echo "✅ deny rule OK"

# 確認 env var
grep -q "CLAUDE_CODE_SUBAGENT_MODEL" .claude/settings.json && echo "✅ model override OK"
```

**工時**：< 30 分鐘
**風險**：低（只防止無限遞迴，不影響正常 subagent 使用）

---

#### P0-B: 演化候選確認提交——`model-selection-grid.md` 加入 Fable 5

**背景**：6/15 DAILY-TOPICS 已標記此演化候選，但需人工審核才能修改 `.claude/refs/`

**動作**：確認 `research/EVOLUTION-QUEUE.md` 已包含此提案，若未包含則追加：

```markdown
## 候選：model-selection-grid-fable5
- date: 2026-06-15
- target: .claude/refs/model-selection-grid.md（待人工審核）
- change: 新增 Fable 5 row，標注 status=suspended（US gov directive Jun 12），
  fallback=claude-opus-4-8，price=$10/$50 per M tokens
- verify: grep -q 'fable-5\|claude-fable-5' .claude/refs/model-selection-grid.md
- status: proposed
```

**驗證**：
```bash
grep -q "model-selection-grid-fable5" research/EVOLUTION-QUEUE.md && echo "✅ 已在 queue"
```

**工時**：< 15 分鐘

---

### P1 — 本月優先（需輕量設計，2-8 小時）

#### P1-A: Nested Subagents 模型分層策略文件

**目標**：建立 `.claude/refs/nested-subagent-model-tiering.md`（需人工審核）

**內容草稿**：
```markdown
# Nested Subagent Model Tiering

## 分層策略
- Root (D0): claude-opus-4-8（最高推理能力）
- D1: claude-sonnet-4-6（平衡性能/成本）
- D2+: claude-haiku-4-5（最低成本，leaf 任務）

## Token 成本估算
每增加一層深度，系統提示 overhead 約 30-60%。
D0-D2 三層的總成本約為 D0 單層的 2-3×（相對於 D0×3 的 3× 節省約 30%）。

## 強制限制
- Leaf tier 設置：permissions.deny: ["Agent(general-purpose)"]
- 全局 override：CLAUDE_CODE_SUBAGENT_MODEL=claude-haiku-4-5-20251001
- Turn caps: leaf ≤ 8, mid-tier ≤ 12

## 深度建議
- 目標深度：2-3（guardrail ≠ target）
- depth 4-5 只用於有充分理由的特殊任務
```

**工時**：2-3 小時（含研究 + 撰寫 + 驗證）

---

#### P1-B: Session 成本追蹤 Hook 設計

**背景**：Claude Code 2.1.178 推薦 AgentsView，但 workspace 目前無 session 成本追蹤機制

**構想**：PostToolUse hook 在每次 Bash 工具後記錄 token 消耗（若 API 提供）：

```bash
# 草稿：.claude/hooks/session-cost-tracker.sh
#!/bin/bash
# PostToolUse: 記錄工具調用次數（作為 session 成本代理指標）
echo "$(date -u +%Y-%m-%dT%H:%M:%SZ) tool=$CLAUDE_TOOL_NAME" >> /tmp/claude-scratch/session-cost.log
```

**驗收條件**：hook 執行後，`/tmp/claude-scratch/session-cost.log` 有工具調用記錄
**工時**：3-4 小時（含 hook 設計 + 測試）

---

#### P1-C: Fable 5 Proactive Behavior 安全 PreToolUse Gate

**背景**：Fable 5 的「relentlessly proactive」行為需要更強的 gate

**實作位置**：`.claude/settings.json` 的 PreToolUse 設定，或 hooks

**設計方向**：
```json
// 高風險工具需明確確認
{
  "permissions": {
    "deny": [
      "Bash(rm *)",
      "Bash(curl * | bash)",
      "Bash(wget * && *)"
    ]
  }
}
```

**工時**：2-3 小時

---

### P2 — 觀察中（需更多信號）

#### P2-A: AgentsView 整合至 workspace

**背景**：AgentsView 提供每日 token 追蹤，但需要 API key 整合
**觀察條件**：Anthropic 官方 `/usage` 命令是否提供足夠的可視性？若夠 → P2 維持；若不夠 → 升 P1

---

#### P2-B: Provider Fallback ADR 文件

**背景**：Fable 5 暫停事件顯示需要 Provider Fallback 策略文件
**觀察條件**：若 workspace 有 production 依賴（非個人研究），應立即升 P1

---

## GAP 狀態更新

| GAP | 研究前狀態 | 研究後狀態 | 行動 |
|-----|-----------|-----------|------|
| fable-mythos-coverage | gap | 填補中（3 篇 web 文章）| P1-C 或文章入庫 |
| nested-subagents-architecture | gap | 填補中（1 篇深度文章） | P0-A 立即防護 |
| claude-code-cost-tracking | gap | 填補中（AgentsView 工具） | P1-B 實作追蹤 |
| safety-classifier-design | gap | 填補中（事件分析） | 原則文件化 |

---

## 下一次循環優先事項

1. **P0-A**（今日）：settings.json 加入 nested subagent 防護 + env override
2. **P0-B**（今日）：確認 model-selection-grid-fable5 已在 EVOLUTION-QUEUE
3. **P1-B**（本週）：Session 成本追蹤 hook 設計與實作

# Boris Cherny 實際 GitHub 設定完整解析

> 來源：https://github.com/0xquinto/bcherny-claude（Boris Cherny 個人 Claude Code 設定公開複刻版）
> 輔助來源：https://x.com/bcherny/status/2007179832300581177、https://x.com/bcherny/status/2017742741636321619
> 收錄日期：2026-05-16（初次：2026-05-01）
> 作者：Boris Cherny（@bcherny，Claude Code 創建者，Anthropic）
> 更新說明：加入 W20 版本新功能對 Boris config 設計哲學的影響

---

## 概覽

Boris Cherny 公開的 Claude Code 設定「surprisingly vanilla」——核心立場是**預設值已夠好，不需要過度客製化**。但他有清晰的結構性組件設計，專注在幾個高槓桿的投資點。

---

## 一、CLAUDE.md 設計哲學

Boris 的 CLAUDE.md 有一個核心規則：

> **「Claude 犯了錯之後，更新 CLAUDE.md，讓它不要再犯相同的錯。」**

這讓 CLAUDE.md 成為「隨時間累積的 codebase 慣例知識庫」而非靜態文件。

### CLAUDE.md 主要內容結構

```
1. Development Workflow（驗證循環）
   make changes → typecheck → test → lint → full suite → PR

2. Code Style Guidelines
   - type 優先於 interface
   - 禁止 enum（改用 string literal union）
   - 描述性命名 + 小型聚焦函式 + 明確錯誤處理

3. Commands Reference（npm scripts 速查）

4. Self-Improvement Protocol
   「每次 Claude 被糾正，更新 CLAUDE.md 防止重複犯錯」

5. Work Modes
   - Plan Mode 用於複雜任務
   - Subagent 用於平行工作（避免 file conflicts）
   - /loop 用於重複任務
   - /schedule 用於定時自動化

6. Session Management
   - /branch 或 --fork-session 分岔 session
   - /btw 插入側邊問題不中斷主流程
   - --add-dir 或 settings 跨多個 repo

7. 禁止清單
   - 無理由使用 any type
   - 跳過 error handling
   - 沒有測試就 commit
   - 未討論就做 breaking change
```

---

## 二、7 個 Slash Commands（`.claude/commands/`）

| 命令 | 功能 |
|------|------|
| `/commit-push-pr` | 完整 git 工作流自動化（add → commit → push → PR） |
| `/quick-commit` | 快速暫存並 commit（跳過 PR 流程） |
| `/test-and-fix` | 執行測試，自動修復失敗測試 |
| `/review-changes` | 分析變更，提出程式碼改善建議 |
| `/worktree` | 透過 git worktree 管理平行 session |
| `/grill` | 嚴格的對抗性 code review（挑毛病模式） |
| `/techdebt` | 掃描並清理 dead code 與重複邏輯 |

### 使用模式

```
開發流程：/worktree → 平行 session → /test-and-fix → /review-changes → /grill → /commit-push-pr
技術債清理：/techdebt + /grill 組合
快速修補：/quick-commit（skip PR 流程）
```

---

## 三、6 個 Subagents（`.claude/agents/`）

| Agent | 職責 |
|-------|------|
| `code-simplifier` | 工作完成後精煉程式碼（消除複雜性） |
| `code-architect` | 設計與架構評估（技術選型） |
| `verify-app` | 全面應用測試（功能驗證） |
| `build-validator` | 部署就緒確認（CI/CD 準備） |
| `oncall-guide` | 生產問題診斷（on-call 輔助） |
| `staff-reviewer` | 持懷疑態度的架構評估（staff 級別 review） |

### 設計原則

- 每個 agent 有**單一聚焦職責**，不做多工
- `code-simplifier` 是 post-work 自動化節點，類似本 workspace 的 `/simplify` skill
- `staff-reviewer` 用「staff engineer 視角」做高標準 adversarial review
- `oncall-guide` 是生產事故的診斷輔助，不是修復 agent

### Boris 典型工作流

```
實作 → code-architect（設計評估）
    → verify-app + build-validator（驗證部署）
    → code-simplifier（精煉）
    → staff-reviewer（最終 review）
    → /commit-push-pr
```

---

## 四、settings.json 設定

```json
{
  "permissions": {
    "allow": ["npm *", "git *", "gh *"]
  },
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "npm run format -- ${file}"
          }
        ]
      }
    ]
  }
}
```

**核心設計決策：**
- `npm`、`git`、`gh` 全部預授權（消除頻繁 permission prompt）
- PostToolUse 自動格式化（每次 Edit/Write 後觸發），確保 style 一致性
- 未設定更複雜的 PreToolUse 防守規則 → 符合「surprisingly vanilla」哲學

---

## 五、核心工作哲學（來自 Boris 推文與設定）

### 5.1 三個核心投資點

Boris 反覆強調的高槓桿投資（來自 2026-02-01 團隊 tips thread）：

1. **CLAUDE.md 自更新機制**：每次犯錯後更新，讓 Claude 的行為隨時間改進
2. **平行 Worktree**：同時跑 3-5 個 Claude session，透過 git worktree 避免 file conflicts
3. **Skills 封裝工作流**：把重複性工作流封裝成 Skills，用 /loop 或 /schedule 驅動

### 5.2 Plan Mode 優先

複雜任務一律先進 Plan Mode，禁止未規劃就直接實作。

### 5.3 Subagent context 隔離

平行工作流要透過 Subagent 隔離 context，避免主對話的中間工具輸出污染主線。

### 5.4 /loop 的 4 個真實配方

（來源：2026-03-30 推文，Boris 個人實際運行的迴圈）

```bash
/loop 5m /babysit          # 每 5 分鐘：自動回應 PR review、rebase、shepherd PR 到生產
/loop 30m /slack-feedback  # 每 30 分鐘：自動將 Slack 回饋轉成 PR
/loop /post-merge-sweeper  # merge 後：處理遺漏的 code review comment
/loop 1h /pr-pruner        # 每小時：關閉 stale PR
```

**核心哲學**：`Skill + Loop = 工作流自動化`

---

## 六、與 cc-workspace 的對照

| Boris 的設定 | cc-workspace 現有對應 | 差距 |
|-------------|----------------------|------|
| CLAUDE.md 自更新規則 | 有（core.md 犯錯後記錄原則）| 規則形式不同，Boris 更強調「直接寫進 CLAUDE.md」 |
| 7 slash commands | 有 `.claude/skills/` 系統 | Slash commands 較輕量，skill 系統較完整 |
| 6 specialized agents | 有 Sub Agent 委派策略 | 缺 `oncall-guide`、`build-validator` 等特化 agent |
| PostToolUse 自動格式化 | 有（auto-sync.md 記載）| 對應 |
| /loop 4 個真實配方 | routines.md 有概念，無實際 Skill 實作 | babysit/slack-feedback 等 Skill 未建立 |
| Subagent context 隔離 | 有（subagent-strategy.md）| 對應 |

---

## 七、可直接採用的模式

```
高優先（立即可用）：
- PostToolUse 自動格式化 hook → 加入 settings.json
- CLAUDE.md 自更新語言（「After corrections, update CLAUDE.md」）
- /grill（adversarial review）作為 deep-review 的補充

中優先（需要 Skill 設計）：
- /babysit → 參考 Boris 的 PR shepherd 語意設計
- /techdebt → dead code 清理 Skill
- oncall-guide agent → 生產事故診斷 Sub Agent

參考（理解 Boris 設計哲學）：
- staff-reviewer：「staff engineer 懷疑態度」review persona
- verify-app：全面功能驗證 agent（不只是 unit test）
```

---

## W20 更新對 Boris Config 設計的影響（v2.1.137–143，2026-05）

### /goal 與 Boris 的「驗證回饋迴圈」哲學

Boris 的 `/go` skill（讓 Claude 端對端測試自己 → `/simplify` → 開 PR）哲學現在有官方指令支援：

```bash
/goal CI 通過且無 type error
```

建議將 Boris 的 `/go` skill 升級為 `/goal` 封裝版本，提供更明確的完成條件而非隱式的「做完測試就算了」。

### Agent View 與 Boris 的「同時跑 5 個 Claude」

Boris 的多 session 並行策略（5 terminal tabs + 5-10 claude.ai sessions）現在有統一管理介面：

```bash
claude agents   # 取代手動管理多個 terminal tabs
```

建議在 Boris 設定中加入：
```json
// settings.json 新增考慮項
{
  "worktree": {
    "bgIsolation": "none"  // 若背景任務需直接操作原始 working copy
  }
}
```

### Fast Mode 變更

Boris 偏好「高 effort 做所有事」，Fast Mode 更新為 Opus 4.7 預設符合此偏好（之前 Fast Mode 用 Opus 4.6，與 Boris 習慣不一致）。

### Hook 升級：continueOnBlock

Boris 的 PostToolUse 自動格式化 hook 可升級加入 `continueOnBlock`，讓格式化失敗時 Claude 自行決策是否跳過（而非直接終止）：

```json
"PostToolUse": [{
  "matcher": "Write|Edit",
  "hooks": [{
    "type": "command",
    "command": "bun run format || true",
    "continueOnBlock": true
  }]
}]
```

---

## Known Gotchas

- 此 repo（0xquinto/bcherny-claude）是社群複刻版，非 Boris 本人維護，可能非最新版本
- CLAUDE.md 的具體程式碼風格規則（type over interface 等）是 TypeScript 專案專用，需依語言調整
- `/babysit`、`/slack-feedback` 等 Skill 的實作細節未公開，需要自行設計
- Boris 的 Note Tweets（全文推文）透過 API 只能取得前 ~300-500 字，可能有更多細節未被收錄
- W20 的 `/goal`、Agent View 等功能對 Boris config 的具體適配需實際測試後才能確認最佳設定

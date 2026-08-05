# Project 04：Plugin 化與自動化治理

## 專案說明

前三個專案的成果都綁在一個 repo 裡。本專案把它們打包成可分發的 **Plugin**，接上**自動化**（排程 / 事件觸發），並補上**成本與安全的護欄**。

這是從「我的工作流」變成「團隊的基礎建設」的那一步。

**完成後的成果**：

- 一個可安裝的 Plugin（skills + agents + hooks + 可選 MCP）
- 一個實際運作的自動化（Routine 或 GitHub Actions）
- 一份成本與權限護欄清單
- 一個 3–6 個月的審閱機制

## 前置條件

- [Lecture 11：MCP 整合與外部系統](/lectures/lecture-11-mcp/)
- [Lecture 12：Plugins、自動化與組織治理](/lectures/lecture-12-governance/)
- [Project 03：把驗證編碼成 Skill](/projects/project-03-verification-skill/)（打包它的產出）

## 任務清單

### 階段一：確認該不該打包

Plugin 有成本（命名空間、版本管理、分發流程）。先確認你真的到了那一步。

- [ ] **任務 1.1**：確認觸發條件成立——**第二個 repo 需要相同的設定**。如果只有一個 repo，standalone 迭代更快，先不要打包
- [ ] **任務 1.2**：列出要打包的組件：哪些 skills、哪些 agents、哪些 hooks、要不要帶 MCP
- [ ] **任務 1.3**：接受命名空間改變——`/verify-api` 會變成 `/my-plugin:verify-api`，沒有無前綴的短名稱

### 階段二：建立 Plugin 結構

- [ ] **任務 2.1**：建立目錄。**只有 `plugin.json` 放在 `.claude-plugin/` 內**，其餘全在 plugin root——這是最常見的錯誤
- [ ] **任務 2.2**：寫 `plugin.json`，**務必填 `version`**。未設定時以 git commit SHA 為版本，使用者每次 `git pull` 都會觸發更新
- [ ] **任務 2.3**：搬入 Project 03 的 skills 到 `skills/`
- [ ] **任務 2.4**：搬入 Project 02 的 verifier agent 到 `agents/`
- [ ] **任務 2.5**：把 `settings.json` 的 hooks 搬到 `hooks/hooks.json`（格式相同）
- [ ] **任務 2.6**：把共用腳本放進 `bin/`——它們會自動加入 Bash tool 的 PATH
- [ ] **任務 2.7**：本地測試 `claude --plugin-dir ./my-plugin`，改完用 `/reload-plugins`（不必重啟）

### 階段三：量測成本

在推給任何人之前，先知道它多貴。

- [ ] **任務 3.1**：跑 `claude plugin details my-plugin`，記下 **per-session token 成本**估計
- [ ] **任務 3.2**：檢查哪些 skill 的 description 是常駐成本。極少用的 skill 加 `disable-model-invocation: true`——它會完全對 Claude 隱藏直到你手動呼叫，**context 成本歸零**
- [ ] **任務 3.3**：如果帶了 MCP，確認 server 數量在 3–6 個以內，並設定 Tool Search（`ENABLE_TOOL_SEARCH=auto`）
- [ ] **任務 3.4**：寫一份 `README.md`：安裝方式、每個 skill 的用途、預估 token 成本、已知限制

### 階段四：接上自動化

先選對執行位置——這決定了一切。

- [ ] **任務 4.1**：選擇機制：
  | 機制 | 執行位置 | 需要開終端機 | 適用 |
  |------|---------|------------|------|
  | `/loop` | 本機 | **要** | 本地定期執行 |
  | Routines | Anthropic 雲端 | 不要 | 排程 / API / GitHub 事件 |
  | Managed Agents Scheduled Deployments | Managed Agents | 不要 | 生產 API 部署 |
  | GitHub Actions | CI | 不要 | Repository pipeline |
- [ ] **任務 4.2**：建立第一個自動化。建議從**低風險、高重複**的開始：每週文件 drift 偵測、每日 PR 摘要、stale PR 標記
- [ ] **任務 4.3**：**Routine 的 prompt 必須完整自給**——它自主執行，沒有 permission picker、沒有 approval prompt，你不在旁邊補充
- [ ] **任務 4.4**：明確寫出成功定義與失敗時該做什麼（開 issue？留 comment？什麼都不做？）
- [ ] **任務 4.5**：確認分支限制。預設只能推 `claude/`-prefixed 分支；**不要**輕易啟用 Allow unrestricted branch pushes
- [ ] **任務 4.6**：知道它以**誰的身份**行動——Routine 歸屬你的個人帳號，所有 commit / PR / connector action 都以你的身份出現，且不與隊友共享

### 階段五：憑證與安全護欄

- [ ] **任務 5.1**：盤點自動化需要哪些憑證，以及**每個憑證只需要哪一個網域**
- [ ] **任務 5.2**：設定憑證隔離（擇一，依平台）：
  - Claude Code：`sandbox.credentials`，Linux/WSL 可用 `mode: "mask"`（沙箱內讀到哨兵副本，proxy 對外時才換回真值）
  - Managed Agents：**Vault**（agent 只拿 placeholder，網路邊界才替換，且只送指定網域）
- [ ] **任務 5.3**：設定出站限制：`sandbox.network.strictAllowlist` + 明確的 `approvedDomains`
- [ ] **任務 5.4**：用 `Tool(param:value)` 加成本護欄，例如 `"deny": ["Agent(model:opus)"]`
- [ ] **任務 5.5**：設定 `--max-budget-usd` 或組織層級的 spend 上限
- [ ] **任務 5.6**：跑一次 CISO 四問，把答案寫進 README：
  1. 這個 agent 處理哪些**不可信內容**？
  2. 能採取**什麼行動**？
  3. 失控時**爆炸半徑**多大？
  4. **可觀測性**程度如何？

### 階段六：觀測與審閱

- [ ] **任務 6.1**：設定 OpenTelemetry（`OTEL_EXPORTER_OTLP_ENDPOINT`）
- [ ] **任務 6.2**：⚠️ 檢查 `OTEL_LOG_ASSISTANT_RESPONSES`。**未設定時它會跟隨 `OTEL_LOG_USER_PROMPTS`**——已經記錄 prompt 的部署升級後會一併開始記錄 response，對含敏感內容的環境是意外的資料落地
- [ ] **任務 6.3**：用 `PreToolUse` hook 記錄 skill 呼叫次數，識別高人氣與零使用率的組件
- [ ] **任務 6.4**：定義三個指標並記下今天的值：onboarding ramp time、PR cycle time、Claude-assisted commits 比例
- [ ] **任務 6.5**：排 3–6 個月後的審閱（可以就用你剛建的 Routine）。審閱要跑：`/doctor`、`claude-api` skill 的 `prompt-audit`、刪掉零使用率的組件
- [ ] **任務 6.6**：（團隊情境）指定一位 **DRI** 負責這個 plugin，避免設定碎片化

## 參考實作

### Plugin 目錄結構

```
my-team-plugin/
├── .claude-plugin/
│   └── plugin.json           ← 唯一放這裡的檔案
├── README.md                 ← 安裝、用途、token 成本、已知限制
├── skills/
│   ├── verifying-api-changes/SKILL.md
│   └── reviewing-migrations/SKILL.md
├── agents/
│   └── adversarial-verifier.md
├── hooks/
│   └── hooks.json
├── bin/
│   └── check-backfill        ← 自動加入 Bash PATH
└── .mcp.json                 ← 可選
```

### plugin.json

```json
{
  "name": "team-harness",
  "description": "Verification skills, adversarial reviewer, and safety hooks for our services",
  "version": "1.0.0",
  "author": { "name": "Platform Team" },
  "repository": "https://github.com/example/team-harness",
  "license": "MIT"
}
```

### hooks/hooks.json

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          { "type": "command", "command": "${CLAUDE_PLUGIN_ROOT}/bin/protect-tests" }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          { "type": "command", "command": "${CLAUDE_PLUGIN_ROOT}/bin/log-skill-usage", "async": true }
        ]
      }
    ]
  }
}
```

### 一個 Routine 的 prompt（自給自足版）

```text
每週一 09:00 執行。

目標：找出本 repo 中「程式碼已變更但文件未同步」的地方。

步驟：
1. 列出過去 7 天合併到 main 的 PR（使用 GitHub connector）
2. 對每個 PR，檢查是否變更了 src/api/ 下的 route 定義
3. 若有，檢查 docs/api/ 下對應的文件是否在同一個 PR 中被更新
4. 對未同步的項目，開一個 issue，標題格式：「docs drift: <route> (PR #<n>)」
   內文列出：變更的 route、對應文件路徑、變更的 PR 連結

成功定義：所有未同步項目都有對應 issue，且沒有重複開立（先搜尋既有 open issue）。
找不到任何未同步項目時：不要開 issue，也不要留言，直接結束並回報「無 drift」。

限制：
- 不要修改任何程式碼或文件，只開 issue
- 不要 push 任何分支
```

注意最後兩段——**明確寫出「什麼都不做」也是一種成功結果**。沒寫的話，自主執行的 agent 傾向找點事做。

### CI 端的非互動深審

```yaml
- name: Deep review
  run: |
    claude ultrareview --json > review.json
    # exit 0 成功，exit 1 失敗
```

### 用 check run 自建 merge gate

Code Review 的 check run 結論永遠是 neutral，不擋 merge。要當 branch protection 用得自己解析：

```bash
IMPORTANT=$(gh api repos/$OWNER/$REPO/check-runs/$ID \
  --jq '.output.text | split("bughunter-severity: ")[1] | split(" -->")[0] | fromjson | .normal')
[ "$IMPORTANT" -eq 0 ] || { echo "有 $IMPORTANT 個未解決的 Important finding"; exit 1; }
```

## 驗收標準

- **驗收 1**：Plugin 能用 `claude --plugin-dir` 在**另一個 repo** 載入並正常運作
- **驗收 2**：`claude plugin details` 顯示的 per-session token 成本你能接受，且你知道那個數字是多少
- **驗收 3**：自動化實際跑過至少一次，且**在「沒事發生」時正確地什麼都不做**
- **驗收 4**：自動化用到的憑證，agent 拿到的是 placeholder 或哨兵副本，不是明文
- **驗收 5**：CISO 四問在 README 中有明確答案
- **驗收 6**：有預算上限，且你實測過達標時會中止而不是繼續燒
- **驗收 7**：審閱機制已排程，且你寫下了「哪些東西不隨模型升級而放寬」

## 延伸閱讀

- [How Claude Code works in large codebases](https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start)（2026-05-14）
- [Introducing routines in Claude Code](https://claude.com/blog/introducing-routines-in-claude-code)（2026-04-14）
- [New in Claude Managed Agents: schedule and vaults](https://claude.com/blog/whats-new-in-claude-managed-agents)（2026-06-09）
- [Zero risk isn't the job: a CISO's guide to agentic AI](https://claude.com/blog/ciso-guide-to-agentic-ai)（2026-07-17）
- [Running an AI-native engineering org](https://claude.com/blog/running-an-ai-native-engineering-org)（2026-06-03）
- [官方文件：Plugins](https://code.claude.com/docs/en/plugins) · [Routines](https://code.claude.com/docs/en/routines)

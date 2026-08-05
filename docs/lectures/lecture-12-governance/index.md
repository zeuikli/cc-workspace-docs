# Lecture 12：Plugins、自動化與組織治理

## 學習目標

完成本課後，你將能夠：

- 判斷什麼時候該把 standalone 設定打包成 Plugin，並正確組出 plugin 目錄結構
- 選擇合適的自動化層級：`/loop` / Routines / Managed Agents Scheduled Deployments
- 用 Vault 讓 agent 在不接觸明文金鑰的情況下呼叫外部 API
- 為大型 codebase 設計三層 context 架構與五元件 harness
- 建立 AI 原生工程組織的度量與定期審閱機制

## 核心概念

### Plugin vs Standalone

| 面向 | **Standalone**（`.claude/`）| **Plugin**（含 `.claude-plugin/plugin.json`）|
|------|------|------|
| Skill 名稱 | `/hello` | `/plugin-name:hello`（有命名空間）|
| 適用 | 個人工作流、單一專案、快速實驗 | 跨專案共享、團隊分發、marketplace |
| 版本控制 | 手動 | 內建版本策略 |
| 跨專案安裝 | 手動複製 | `/plugin install` |

**決策原則**：先用 standalone 快速迭代 → **第二個 repo 需要相同設定時**轉 Plugin。這也是官方的觸發點判斷表裡的一條。

### Plugin 目錄結構（最常見的錯誤在這裡）

```
my-plugin/
├── .claude-plugin/
│   └── plugin.json        ← 唯一放在 .claude-plugin/ 內的檔案
├── skills/
│   └── my-skill/SKILL.md
├── agents/my-agent.md
├── hooks/hooks.json
├── .mcp.json              ← MCP server 設定
├── .lsp.json              ← LSP server 設定
├── monitors/monitors.json ← 背景監控
├── bin/my-tool            ← 可執行檔，自動加入 Bash PATH
└── settings.json          ← plugin 啟用時套用的預設設定
```

> **最常見錯誤**：把 `skills/`、`agents/`、`hooks/` 放進 `.claude-plugin/`。**只有 `plugin.json` 在裡面**，其餘都在 plugin root。

**version 欄位不填的後果**：未設定時以 git commit SHA 為版本——使用者每次 `git pull` 都會觸發更新。

### Plugin 的六種組件

| 組件 | 位置 | 用途 |
|------|------|------|
| Skills | `skills/<name>/SKILL.md` | 可重用知識與流程 |
| Agents | `agents/*.md` | 自訂 subagent 定義 |
| Hooks | `hooks/hooks.json` | 格式與 `settings.json` 的 `hooks` key 相同 |
| MCP | `.mcp.json` | plugin 專屬的外部連接 |
| LSP | `.lsp.json` | 符號級 code intelligence（使用者仍需自行安裝 language server binary）|
| Monitors | `monitors/monitors.json` | 背景進程，每行 stdout 以 notification 注入對話 |

`bin/` 下的可執行檔會自動加入 Bash tool 的 PATH——這是封裝 helper script 最乾淨的方式。

### 三種自動化：跑在哪裡決定一切

| 機制 | 執行位置 | 需要開著終端機？ | 適用 |
|------|---------|----------------|------|
| **`/loop`（CLI）** | 本機 | **需要** | 本地定期執行 |
| **Desktop scheduled tasks** | 本機 | 不需要 | 需要本機檔案存取 |
| **Routines** | Anthropic 雲端 | 不需要 | 排程、API 觸發、GitHub 事件 |
| **Managed Agents Scheduled Deployments** | Managed Agents 基礎設施 | 不需要 | 生產 API 部署 |
| **GitHub Actions** | CI 環境 | 不需要 | Repository CI pipeline |

### Routines：三種觸發器

Routine 是一個儲存的 Claude Code 設定（prompt + repository + connectors），跑在 Anthropic 管理的雲端，**筆電關掉仍持續運作**。

| 觸發類型 | 說明 |
|---------|------|
| **Scheduled** | hourly / daily / weekly，或一次性指定時間點 |
| **API** | HTTP POST 到專屬 endpoint |
| **GitHub** | PR、Release 等 repository event |

同一個 Routine 可以混用多種觸發器。

**實用場景**：

| 情境 | 觸發 |
|------|------|
| Backlog 自動維護（貼標、指派、Slack 摘要）| Schedule（每週日）|
| Alert 分診（拉 stack trace、比對近期 commit、開 draft PR）| API（監控工具呼叫）|
| 客製 Code Review（套 team checklist）| GitHub（PR opened）|
| Deploy 驗證（smoke test、掃 error log、貼 go/no-go）| API（CD pipeline）|
| 文件 drift 偵測 | Schedule（每週）|

**四個必須知道的安全事實**：

1. Routine 以**自主模式**執行——沒有 permission-mode picker，沒有 approval prompt
2. Routine 歸屬**個人 claude.ai 帳號**，不與隊友共享
3. 所有 commit / PR / connector action 都以**你的身份**出現
4. 預設只能推送到 `claude/`-prefixed 分支；要解除需明確啟用 **Allow unrestricted branch pushes**

**限額**：計入個人帳號的每日執行次數上限（依方案而定）。**一次性執行（one-off run）不計入每日上限**，改計入一般 session 用量。

### Vaults：讓 agent 永遠看不到明文金鑰

Managed Agents 的 Vault 機制解決「agent 需要呼叫外部 API 但不該持有金鑰」這個矛盾：

```
開發者 → 向 Vault 註冊 API Key
            ├── 指定環境變數名稱（如 GITHUB_TOKEN）
            └── 指定允許的網域（如 api.github.com）

Agent 運行時：
  Sandbox 只收到 placeholder（不是真實 Key）
      ↓
  Agent 執行 CLI 工具 → 工具用 placeholder 呼叫 API
      ↓
  請求到達網路邊界 → Anthropic 基礎設施把 placeholder 換成真實 Key
      ↓
  只有目標網域收到真實 Key；其他網域的請求被拒絕
```

**Agent 程式碼中永遠看不到真實 API Key**。適用需要 env var 認證的 CLI（`gh`、`aws`、`gcloud`、`kubectl`）、私有 registry、第三方 API。

**限制**：不適用需要 interactive OAuth flow 的情境（那仍需 MCP connector + OAuth）。

Claude Code 端的對應概念是 `sandbox.credentials` 的 `mode: "mask"`（Linux/WSL，v2.1.213）——沙箱內讀到哨兵副本，proxy 對外時才換回真值。

### 大型 codebase：三層 Context 架構

Skyline 案例（70 萬行 C#、2008 年起、20 萬+ 夜間測試）的核心策略是把**人員 onboarding 方法論直接套用到 Claude**：不期望它立刻理解整個 codebase，先從小型獨立模組建立理解，逐步擴大同時保持專屬 context。

**層 1：Context Repository（獨立 git repo）**

```
pwiz-ai/
├── CLAUDE.md                   # 方向 + 文件索引
├── skills/
│   ├── skyline-development.md
│   ├── version-control.md
│   └── debugging.md
└── docs/architecture.md
```

關鍵設計：適用所有 branch 與時間點；**「參考不嵌入」**——Skills 指向文件而非複製內容；每個 Skill 有明確觸發條件。

**層 2：Skills Library** — 把機構知識編碼為可跨 session 使用的 Skill。

**層 3：MCP 整合** — 連接測試結果、異常報告、歷史 issue。原則是「**真實資訊勝過抽象知識**」：讓 Claude 查到真實的測試失敗，而不是猜測。

**成果**：原本估一年的 Files View 面板專案，**兩週完成**。

### Agentic Search，不是 RAG

Claude Code 用 **Agentic Search** 導覽 codebase——直接在本地 traverse，類 grep。

| 優勢 | 要求 |
|------|------|
| 永遠是最新程式碼（無過時 embedding index）| **codebase 組織良好**，否則導覽效率低 |

**實際意涵**：好的 codebase 結構本身就是提升 Claude Code 效果的槓桿。加分項是 **LSP 整合**，提供符號級搜尋。

### 五元件 Harness 生態系

| 元件 | 設計原則 |
|------|---------|
| **CLAUDE.md** | 精簡、按目錄分層、排除生成檔案 |
| **Hooks** | 持續改進與自動化 |
| **Skills** | 特定任務類型的打包專業知識 |
| **Plugins** | 統一組織內設定 |
| **MCP Servers** | 讓 Claude 存取真實內部資料 |

**CLAUDE.md 三原則**：保持精簡（大型 codebase ≠ 長 CLAUDE.md）、子目錄各自初始化、明確排除生成檔案目錄。

### 每 3–6 個月審閱設定

這條規則的理由很反直覺，但非常重要：

> **模型進化後，舊指令可能反而限制新模型能力。**

Claude 5 世代的實證把這件事推到極端——Anthropic 為 Opus 5 / Fable 5 刪掉 Claude Code system prompt 的 **80% 以上**，在 coding evals 上**無可量測退化**。根因是舊 prompt 對模型 over-constrain，且指令彼此打架（同一次請求裡同時出現「leave documentation as appropriate」與「DO NOT add comments」），新世代模型會花推理預算去調解衝突。

工具面已經配合：`/doctor` 從 v2.1.206 起會主動提出 `CLAUDE.md` 精簡建議；`claude-api` skill 的 `prompt-audit` 子命令（v2.1.213）專門稽核「為舊世代寫的 prompt 與 tool description」。

**但要劃清邊界**：可刪的是為補償模型弱點而堆的**程序性鷹架**，**不是驗證閘門與不可逆操作確認**。能力提升不得換取更少驗證。

### 組織所有權

- 指定 **DRI**（Directly Responsible Individual）管理 Claude Code 設定
- 建立跨職能工作組（工程 + 安全 + 治理）
- 目的是防止設定碎片化

### AI 原生工程組織：三個轉變

《Running an AI-native engineering org》記錄的組織重組：

| 面向 | 從 | 到 |
|------|-----|-----|
| 規劃 | 六個月 Roadmap | **JIT Planning**（原型驅動 + 快速內部回饋）|
| Code Review | style + logic | **高判斷領域**（法律 / 安全 / 產品感）|
| 角色邊界 | 明確分工 | 模糊化（PM 寫程式、工程師做設計）|
| Context 蒐集 | 先找人 | **先問 Claude 再找人**；手動摘要 → 持續背景自動化 |

**三個度量指標**：

1. **Onboarding ramp time**——新人第一週能否 ship 真實程式碼
2. **PR cycle time**
3. **Claude-assisted commits**——Anthropic 的 Claude Code 團隊連續四個月 ≈100%

招聘偏好也變了：優先「有產品感的創意建造者」與深度系統專家。

### 安全治理：AI 寫 80% 程式碼的環境怎麼守

《How Anthropic secures its AI-native SDLC》的分層：

| 階段 | 做法 |
|------|------|
| **規劃** | AI 專案安全審查對照 MITRE ATT&CK 並接上組織知識庫；低風險可自助核准，不成瓶頸 |
| **生成** | **CLAUDE.md 把安全最佳實踐編碼進生成過程**，安全 review plugin 即時建議——在產生時預防而非事後偵測 |
| **審查** | 多個窄焦點 agent 各持獨立 context 與偏誤審同一個 PR + SAST + 對自動核可的人工抽樣 |
| **圍堵** | 遠端 coding VM 只開 allowlist 出口；agent 權限分離；獨立系統帳號 |
| **治理** | 所有 agent 動作進 **SIEM**；發現漏洞**自動回寫 CLAUDE.md** 以免同類問題再生成 |

最後一條是 Ratchet 原則的組織級實作：漏洞不只被修掉，還被寫進規則，讓它不會再被生成出來。

### CISO 的四個問題

《Zero risk isn't the job》給的評估框架，比一份控制清單更耐用：

1. 代理處理哪些**不可信內容**？
2. 能採取**什麼行動**？
3. 失控時**爆炸半徑**多大？
4. **可觀測性**程度如何？

七項核心控制：身份整合、連接器白名單、細粒度工具批准、沙箱執行、出站限制清單、OpenTelemetry 遙測、組織級「斷電開關」。

核心論點值得記住：**安全領導者的職責不是追求零風險，而是讓代理風險可見且有界**。而且治理無需成為瓶頸——合規團隊本身可以運行代理，自動化風險登記與供應商審查。

## 程式碼範例

### 建立第一個 Plugin

```bash
mkdir -p my-plugin/.claude-plugin my-plugin/skills/hello

cat > my-plugin/.claude-plugin/plugin.json << 'EOF'
{
  "name": "my-first-plugin",
  "description": "Team conventions and review workflow",
  "version": "1.0.0",
  "author": { "name": "Zeuik" },
  "repository": "https://github.com/zeuikli/my-plugin",
  "license": "MIT"
}
EOF

cat > my-plugin/skills/hello/SKILL.md << 'EOF'
---
description: Greet the user with a friendly message
disable-model-invocation: true
---

Greet the user named "$ARGUMENTS" warmly and ask how you can help.
EOF

# 本地測試（不需安裝）
claude --plugin-dir ./my-plugin
```

session 內執行 `/my-first-plugin:hello Alex`。改完不需重啟，用 `/reload-plugins`。

### Plugin 管理

```bash
claude --plugin-dir ./plugin-one --plugin-dir ./plugin-two
claude --plugin-dir ./my-plugin.zip            # 本地 zip（W19）
claude --plugin-url https://example.com/p.zip  # 從 URL 載入（W19）

claude plugin details my-plugin   # 組件清單 + 預估 per-session token 成本
claude plugin tag                 # 建立 release git tag，含版本驗證
claude plugin prune               # 清除孤立的自動安裝依賴
```

`claude plugin details` 會告訴你這個 plugin 每個 session 大約吃掉多少 token——在決定要不要全組織推廣時，這個數字比功能清單重要。

### 背景 monitor

```json
[
  {
    "name": "error-log",
    "command": "tail -F ./logs/error.log",
    "description": "Application error log"
  }
]
```

每行 stdout 以 notification 形式注入 Claude 對話。

### Routine：CLI 管理

```bash
/schedule                                     # 開啟建立流程
/schedule daily PR review at 9am              # 自然語言建立
/schedule tomorrow at 9am, summarize yesterday's merged PRs   # 一次性
/schedule list
/schedule update
/schedule run                                 # 立即觸發
```

### Routine：API 觸發

```bash
curl -X POST https://api.anthropic.com/v1/claude_code/routines/trig_01ABC.../fire \
  -H "Authorization: Bearer sk-ant-oat01-xxxxx" \
  -H "anthropic-beta: experimental-cc-routine-2026-04-01" \
  -H "anthropic-version: 2023-06-01" \
  -H "Content-Type: application/json" \
  -d '{"text": "Sentry alert SEN-4521 fired in prod. Stack trace attached."}'
```

回傳 `claude_code_session_url`，可直接開啟查看該次執行。`text` 是選填的 run-specific context（純文字，不解析結構）。

**Token 只顯示一次**——產生時就要存好，之後只能 regenerate 或 revoke。

### GitHub 觸發器的過濾條件

所有條件需**同時**符合才觸發：

```
Base branch   equals        main
Head branch   contains      auth-provider
Is draft      false
Labels        is one of     needs-review
```

> `matches regex` 測試**整個欄位值**，不是 substring。要匹配含 `hotfix` 的 title 必須寫 `.*hotfix.*`。

### Vault 設定

```python
vault.create(
    name="GITHUB_TOKEN",                  # 環境變數名稱
    value="ghp_...",                      # 真實 Key（只傳一次）
    allowed_domains=["api.github.com"],   # 最小權限：只有這個網域收得到真值
)
```

### post-session lifecycle hook

```json
{
  "lifecycle": {
    "postSession": "bash scripts/export-artifacts.sh"
  }
}
```

在 session 結束後、workspace 刪除前執行。用途：快照未提交的工作、匯出日誌到外部系統、發送 webhook 通知。

### 大型 codebase 的 CLAUDE.md 骨架

```markdown
# Monorepo（~70 萬行）

> 這份檔案只放方向與索引。細節在各子目錄的 CLAUDE.md 與 Skills 裡。

## 不要讀的目錄（自動生成）

- `build/`、`dist/`、`**/*.generated.*`、`vendor/`
- 這些目錄的內容由 `make codegen` 產生，改它們不會生效

## 子系統索引

| 子系統 | 位置 | 專屬指令 |
|--------|------|---------|
| API | `services/api/` | `services/api/CLAUDE.md` |
| 前端 | `apps/web/` | `apps/web/CLAUDE.md` |
| 資料管線 | `pipelines/` | `pipelines/CLAUDE.md` |

## Critical gotchas（只放會咬人的）

- `services/api/legacy/` 下的程式碼沒有測試覆蓋，改動前先問。
- 資料庫 migration 一律走 `reviewing-migrations` skill，不要直接改 schema。

## 完成定義

`make verify`（= test + lint + typecheck）全綠，且輸出貼在回報中。
```

### 組織級 policy settings

```json
{
  "permissions": {
    "deny": ["Agent(model:opus)"],
    "ask": ["Bash(kubectl:*)", "Bash(terraform apply:*)"]
  },
  "allowedMcpServers": [{ "serverUrl": "https://mcp.company.com/*" }],
  "parentSettingsBehavior": "merge",
  "forceLoginMethod": "sso",
  "env": {
    "OTEL_EXPORTER_OTLP_ENDPOINT": "https://otel.company.com",
    "CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS": "10"
  }
}
```

`Agent(model:opus)` 這類 `Tool(param:value)` 語法（W25）可以直接阻止 spawn 特定檔位的 subagent——成本治理不必靠自律。

## 常見問題與注意事項

**Q：什麼時候該從 standalone 轉 Plugin？**

A：官方的觸發點是「**第二個 repo 需要相同的設定**」。在那之前，standalone 迭代更快，而且 skill 名稱不用帶命名空間前綴。

**Q：Plugin 的 `settings.json` 可以設什麼？**

A：目前只有 `agent` 和 `subagentStatusLine` 兩個 key 有效，**其他會被靜默忽略**。設 `{"agent": "security-reviewer"}` 可以讓 plugin 的該 agent 成為 main thread agent。

**Q：Routines 和 Managed Agents Scheduled Deployments 怎麼選？**

A：看對象。Routines 是開發者 IDE/CLI 工作流，計入個人帳號的每日限額，觸發方式多（Schedule / API / GitHub）。Scheduled Deployments 是生產 API 部署，按 API 計費，觸發只有 cron。個人自動化用前者，產品化用後者。

**Q：Routine 會用誰的身份 commit？**

A：**你的**。所有 commit、PR、connector action 都以你的身份出現，而且 Routine 不與隊友共享。做團隊層級的自動化要考慮這一點——用共享的機器人身份可能更合適（見 [Agent identity in Claude Tag](https://claude.com/blog/agent-identity-access-model)）。

**Q：我們有 Zero Data Retention，可以用 Code Review 嗎？**

A：不行，ZDR 組織不可用 Code Review。

**Q：每 3–6 個月審閱到底要審什麼？**

A：跑 `/doctor` 看 CLAUDE.md 精簡建議、跑 `claude-api` skill 的 `prompt-audit` 找為舊世代寫的模式，然後問三個問題：① 哪些規則是在補償模型已經不再有的弱點？② 哪些指令彼此打架？③ 哪些是可從 repo 推導的資訊（= 噪音）？**驗證閘門與不可逆操作確認不在刪除範圍內。**

**Q：怎麼衡量導入成效？**

A：官方的 contribution metrics 提供 PR 建立、程式碼提交與每人採用模式（Team / Enterprise，需安裝 GitHub App）。Anthropic 內部數據：每位工程師每天合併的 PR **+67%**，70–90% 的程式碼由 Claude Code 協助撰寫。組織層面則用 onboarding ramp time / PR cycle time / Claude-assisted commits 三指標。

**Q：agent 的行為要怎麼監控？**

A：把所有 agent 動作送進 SIEM，並用 OpenTelemetry 收遙測（`OTEL_EXPORTER_OTLP_ENDPOINT` 可由 managed settings 統管所有 signal）。注意一個陷阱：未設 `OTEL_LOG_ASSISTANT_RESPONSES` 時它會跟隨 `OTEL_LOG_USER_PROMPTS`——已經記錄 prompt 的部署升級後會**一併開始記錄 response**，這對含敏感內容的環境是個意外的資料落地。

## 本課小結

- **Plugin 的觸發點是「第二個 repo 需要相同設定」**；`.claude-plugin/` 裡只放 `plugin.json`，其餘在 plugin root。
- **自動化按執行位置選**：`/loop`（本機、要開終端機）→ Routines（Anthropic 雲端、三種觸發）→ Managed Agents（生產部署、cron）。
- **Routine 以自主模式執行、以你的身份行動**，預設只能推 `claude/` 分支。
- **Vault 讓 agent 永遠看不到明文金鑰**——placeholder 在網路邊界才被換回真值，且只送到指定網域。
- **大型 codebase 三層架構**：Context Repository + Skills Library + MCP 真實資料；「參考不嵌入」。
- **Agentic Search 不是 RAG**——codebase 組織品質直接決定導覽效率。
- **每 3–6 個月審閱設定**：舊指令會限制新模型。system prompt −80% 無退化是實證，但**驗證閘門不在可刪之列**。
- **安全治理**：把最佳實踐編碼進生成過程（CLAUDE.md + plugin）比事後偵測有效；漏洞發現後自動回寫規則。
- **CISO 四問**：不可信內容 / 可採取行動 / 爆炸半徑 / 可觀測性。目標是**風險可見且有界**，不是零風險。

## 延伸閱讀

- [Lecture 02：CLAUDE.md 設計](/lectures/lecture-02-claude-md/) — 分層與 Ratchet 原則
- [Lecture 06：安全沙箱與 Proxy](/lectures/lecture-06-security/) — sandbox.credentials 與出站管控
- [Lecture 07：Skills 設計](/lectures/lecture-07-skills/) — 打包進 Plugin 的內容怎麼寫
- [Lecture 10：驗證迴圈與 Code Review](/lectures/lecture-10-verification/) — PR-wide 驗證形態

**官方一手來源**

- [How Claude Code works in large codebases: Best practices and where to start](https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start)（2026-05-14）
- [Onboarding Claude Code like a new developer: Lessons from 17 years of development](https://claude.com/blog/onboarding-claude-code-like-a-new-developer-lessons-from-17-years-of-development)（2026-04-28）
- [Running an AI-native engineering org](https://claude.com/blog/running-an-ai-native-engineering-org)（2026-06-03）
- [How Anthropic secures its AI-native software development lifecycle](https://claude.com/blog/how-anthropic-secures-its-ai-native-software-development-lifecycle)（2026-07-21）
- [Zero risk isn't the job: a CISO's guide to agentic AI](https://claude.com/blog/ciso-guide-to-agentic-ai)（2026-07-17）
- [Introducing routines in Claude Code](https://claude.com/blog/introducing-routines-in-claude-code)（2026-04-14）
- [New in Claude Managed Agents: run agents on a schedule and store environment variables in vaults](https://claude.com/blog/whats-new-in-claude-managed-agents)（2026-06-09）
- [The evolution of agentic surfaces: building with Claude Managed Agents](https://claude.com/blog/building-with-claude-managed-agents)（2026-06-10）
- [How Anthropic teams use Claude Code](https://claude.com/blog/how-anthropic-teams-use-claude-code)（2026-06-12）
- [Understand Claude Code's impact with contribution metrics](https://claude.com/blog/contribution-metrics)（2026-01-29）
- [Agent identity in Claude Tag: a new access model for autonomous, team-wide AI](https://claude.com/blog/agent-identity-access-model)（2026-06-24）
- [官方文件：Plugins](https://code.claude.com/docs/en/plugins) · [Routines](https://code.claude.com/docs/en/routines)

**站內研究歸檔**

- [Plugin 系統完整指南](/research/best-practices/24-plugins)
- [Routines 排程自動化完整指南](/research/best-practices/11-routines)
- [Managed Agents 排程部署與 Vault 金鑰管理](/research/best-practices/37-managed-agents-schedule-vaults)
- [Onboarding 與大型 Codebase 最佳實踐](/research/best-practices/29-onboarding-large-codebase)
- [AI 原生工程組織管理指南](/research/best-practices/35-ai-native-engineering)
- [Agent Skills 企業治理指南](/research/best-practices/10-agent-skills-enterprise)

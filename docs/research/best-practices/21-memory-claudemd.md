---
title: How Claude Remembers Your Project — CLAUDE.md 與 Auto Memory 完整指南
source: "https://code.claude.com/docs/en/memory"
type: best-practices
---

# How Claude Remembers Your Project — CLAUDE.md 與 Auto Memory 完整指南

> 來源：https://code.claude.com/docs/en/memory
> 收錄日期：2026-05-01
> 涵蓋：CLAUDE.md 設定、路徑範圍規則、Auto Memory 機制、多層級設定、除錯

---

## 兩種記憶系統對照

| 面向 | CLAUDE.md files | Auto Memory |
|------|-----------------|-------------|
| **誰寫** | 你 | Claude |
| **內容** | 指令和規則 | 學習成果和 patterns |
| **範圍** | 專案、用戶、組織 | 每個 working tree |
| **載入到** | 每次 session | 每次 session（前 200 行或 25KB） |
| **適合** | 程式碼標準、workflows、專案架構 | Build 指令、debug insights、Claude 自己發現的偏好 |

**核心原則**：兩個系統的內容都在每次對話開始時作為 context 載入。Claude 將其視為 context 而非強制設定。**指令愈具體簡潔，Claude 遵循得愈穩定。**

---

## CLAUDE.md Files

### 何時加入 CLAUDE.md

當：
- Claude 同一個錯誤犯了第二次
- Code review 抓到 Claude 應該知道的 codebase 事項
- 你輸入了上次 session 也輸入過的同樣修正或說明
- 新團隊成員需要同樣的 context 才能有效工作

**放什麼**：每次 session 都需要的事實：build 指令、慣例、專案結構、"always do X" 規則。多步驟流程或只在某個 codebase 部分重要的事項 → 移到 skill 或 path-scoped rule。

### 放置位置與範圍

| 範圍 | 路徑 | 用途 | 共用對象 |
|------|------|------|---------|
| **Managed policy** | macOS: `/Library/Application Support/ClaudeCode/CLAUDE.md`<br>Linux/WSL: `/etc/claude-code/CLAUDE.md`<br>Windows: `C:\Program Files\ClaudeCode\CLAUDE.md` | IT/DevOps 管理的組織全員指令 | 組織所有用戶 |
| **Project instructions** | `./CLAUDE.md` 或 `./.claude/CLAUDE.md` | 團隊共用的專案指令 | 透過 source control 共用 |
| **User instructions** | `~/.claude/CLAUDE.md` | 所有專案的個人偏好 | 只有你（所有專案） |
| **Local instructions** | `./CLAUDE.local.md` | 個人專案特定偏好（加入 .gitignore） | 只有你（當前專案） |

CLAUDE.md 和 CLAUDE.local.md 在工作目錄**以上**的目錄層級在啟動時完整載入。子目錄的檔案在 Claude 讀取那些目錄的檔案時按需載入。

### 設定 Project CLAUDE.md

```bash
/init    # 自動分析 codebase 生成起始 CLAUDE.md
```

設定 `CLAUDE_CODE_NEW_INIT=1` 啟用互動式多階段流程：詢問要設置什麼（CLAUDE.md、skills、hooks），用 subagent 探索 codebase，透過追問填補空白，呈現可審核的提案後再寫入任何檔案。

### 寫有效的指令

**大小**：每個 CLAUDE.md 目標在 200 行以內。超過 → 用 path-scoped rules（只在 Claude 處理符合路徑的檔案時載入）。可用 imports 分割，但匯入的檔案仍會載入並佔用 context。

**結構**：用 markdown headers 和 bullets 分組相關指令。

**具體性**：
- ✅ "Use 2-space indentation" 而非 "Format code properly"
- ✅ "Run `npm test` before committing" 而非 "Test your changes"
- ✅ "API handlers live in `src/api/handlers/`" 而非 "Keep files organized"

**一致性**：定期審查 CLAUDE.md 檔案（含子目錄的和 `.claude/rules/`），移除過時或衝突的指令。

### 引入其他檔案

```markdown
See @README for project overview and @package.json for available npm commands.

# Additional Instructions
- git workflow @docs/git-instructions.md
- Personal overrides: @~/.claude/my-project-instructions.md
```

- 相對路徑相對於包含引用的檔案（不是工作目錄）
- 匯入的檔案可以遞迴引入其他檔案（最大深度 5 層）
- 首次遇到外部 imports 時 Claude Code 會顯示核准對話框

**跨 worktrees 的個人指令**（gitignored 的 `CLAUDE.local.md` 只存在於建立它的那個 worktree）：

```markdown
# Individual Preferences
- @~/.claude/my-project-instructions.md
```

### AGENTS.md 相容性

Claude Code 讀 `CLAUDE.md`，不讀 `AGENTS.md`。要讓兩個工具共用同一份指令：

```markdown
@AGENTS.md

## Claude Code
Use plan mode for changes under `src/billing/`.
```

### CLAUDE.md 的載入順序

Claude Code 從當前工作目錄往上 walk，檢查每個目錄的 `CLAUDE.md` 和 `CLAUDE.local.md`。所有找到的檔案串聯進 context（不覆蓋）。

順序：從 filesystem root 往下到工作目錄。在 `foo/bar/` 中，`foo/CLAUDE.md` 在 context 中出現在 `foo/bar/CLAUDE.md` 之前。在每個目錄中，`CLAUDE.local.md` 接在 `CLAUDE.md` 之後。

**Block-level HTML 注釋**（`<!-- maintainer notes -->`）在注入 Claude context 前被剝除。用來為人類維護者留注釋而不佔用 context tokens。code blocks 內的注釋保留。

### 從其他目錄載入

```bash
CLAUDE_CODE_ADDITIONAL_DIRECTORIES_CLAUDE_MD=1 claude --add-dir ../shared-config
```

這會從額外目錄載入 `CLAUDE.md`、`.claude/CLAUDE.md`、`.claude/rules/*.md`、`CLAUDE.local.md`。

---

## 用 `.claude/rules/` 組織規則

```text
your-project/
├── .claude/
│   ├── CLAUDE.md           # 主要專案指令
│   └── rules/
│       ├── code-style.md   # Code style 指南
│       ├── testing.md      # 測試慣例
│       └── security.md     # 安全需求
```

沒有 `paths` frontmatter 的 rules 在啟動時以和 `.claude/CLAUDE.md` 相同的優先序載入。

### Path-specific Rules（路徑範圍規則）

```markdown
---
paths:
  - "src/api/**/*.ts"
---

# API Development Rules

- All API endpoints must include input validation
- Use the standard error response format
- Include OpenAPI documentation comments
```

**沒有 `paths` 欄位**的規則無條件載入，適用所有檔案。路徑範圍規則在 Claude 讀取符合 pattern 的檔案時觸發（不是每次 tool use）。

**Glob pattern 範例**：

| Pattern | 符合 |
|---------|------|
| `**/*.ts` | 任何目錄的所有 TypeScript 檔案 |
| `src/**/*` | `src/` 目錄下的所有檔案 |
| `*.md` | 專案根目錄的 Markdown 檔案 |
| `src/components/*.tsx` | 特定目錄的 React components |
| `src/**/*.{ts,tsx}` | 用 brace expansion 多重擴展名 |

**跨專案共用規則（symlinks）**：

```bash
ln -s ~/shared-claude-rules .claude/rules/shared
ln -s ~/company-standards/security.md .claude/rules/security.md
```

### User-level Rules

```text
~/.claude/rules/
├── preferences.md    # 個人 coding 偏好
└── workflows.md      # 偏好的 workflows
```

User-level rules 在 project rules 之前載入（project rules 優先序更高）。

---

## 大型團隊管理 CLAUDE.md

### 部署組織全員 CLAUDE.md

在 managed policy 位置建立檔案，用 MDM、Group Policy、Ansible 等工具部署。

**Managed CLAUDE.md vs Managed Settings 的分工**：

| 關切點 | 設定在 |
|--------|--------|
| 封鎖特定 tools、指令、路徑 | Managed settings: `permissions.deny` |
| 強制 sandbox 隔離 | Managed settings: `sandbox.enabled` |
| Environment variables 和 API provider 路由 | Managed settings: `env` |
| 認證方式和組織鎖定 | Managed settings: `forceLoginMethod`, `forceLoginOrgUUID` |
| Code style 和品質指南 | Managed CLAUDE.md |
| 資料處理和合規提醒 | Managed CLAUDE.md |
| Claude 的行為指令 | Managed CLAUDE.md |

Settings rules 由 client 強制執行；CLAUDE.md 指令塑造 Claude 的行為但不是強制執行層。

### 排除特定 CLAUDE.md 檔案（大型 monorepo）

```json
// .claude/settings.local.json
{
  "claudeMdExcludes": [
    "**/monorepo/CLAUDE.md",
    "/home/user/monorepo/other-team/.claude/rules/**"
  ]
}
```

Patterns 用 glob 語法比對絕對路徑。可在任何 settings 層級設定（user、project、local、managed policy）。Arrays 跨層合併。**Managed policy CLAUDE.md 無法被排除。**

---

## Auto Memory

Claude 在工作過程中自動累積知識：build 指令、debug insights、架構注意事項、程式碼風格偏好、工作習慣。Claude **不是每次 session 都儲存**，而是判斷哪些資訊在未來對話中有用。

> **需求**：Claude Code v2.1.59 或更新版本。

### 啟用/停用

預設啟用。切換方式：
- 在 session 中執行 `/memory` → 使用 auto memory toggle
- 或在 settings 中設定：

```json
{
  "autoMemoryEnabled": false
}
```

```bash
CLAUDE_CODE_DISABLE_AUTO_MEMORY=1  # 環境變數停用
```

### 儲存位置

```text
~/.claude/projects/<project>/memory/
├── MEMORY.md          # 簡潔的索引，每次 session 都載入
├── debugging.md       # 詳細的 debug patterns 筆記
├── api-conventions.md # API 設計決策
└── ...
```

**共用範圍**：同一個 git repository 的所有 worktrees 和子目錄共用一個 auto memory 目錄。Auto memory 是機器本地的，不跨機器或雲端環境共用。

**自訂儲存位置**：

```json
{
  "autoMemoryDirectory": "~/my-custom-memory-dir"
}
```

（接受 policy、local、user settings；不接受 project settings，防止共用專案重新導向寫入到敏感位置）

### 如何運作

- `MEMORY.md` 前 200 行或 25KB（以先到者為準）在每次對話開始時載入
- 超出這個閾值的內容不在 session start 載入
- Claude 透過把詳細筆記移到 topic files（`debugging.md`、`patterns.md`）來保持 `MEMORY.md` 簡潔
- Topic files **不在啟動時載入**；Claude 在需要資訊時用標準 file tools 按需讀取

---

## 用 `/memory` 查看和編輯

`/memory` 指令列出當前 session 中所有已載入的 CLAUDE.md、CLAUDE.local.md、rules files，可切換 auto memory，並提供連結開啟 auto memory 資料夾。選擇任何檔案可在編輯器中開啟。

當你請 Claude 記住某事（如「always use pnpm, not npm」），Claude 儲存到 auto memory。要加到 CLAUDE.md，直接要求（如「add this to CLAUDE.md」）或透過 `/memory` 編輯檔案。

---

## 除錯 Memory 問題

### Claude 不遵循 CLAUDE.md 指令

CLAUDE.md 內容作為 system prompt 後的 user 訊息傳遞，不是 system prompt 的一部分。Claude 讀取並嘗試遵循，但沒有嚴格遵從的保證（尤其是模糊或衝突的指令）。

**除錯步驟**：
1. 執行 `/memory` 確認 CLAUDE.md 和 CLAUDE.local.md 有被載入（不在清單就代表 Claude 看不到）
2. 確認相關 CLAUDE.md 在當前 session 能被載入的位置
3. 使指令更具體（"Use 2-space indentation" 優於 "format code nicely"）
4. 查找跨 CLAUDE.md 檔案的衝突指令

要讓指令在 system prompt 層級：用 `--append-system-prompt`（每次呼叫都要傳入，更適合腳本和自動化而非互動使用）。

**使用 `InstructionsLoaded` Hook 除錯**：記錄哪些指令檔案被載入、何時載入、為什麼載入，適合 debug path-specific rules 或懶載入的子目錄檔案。

### CLAUDE.md 太大

超過 200 行 → 使用 path-scoped rules（只在 Claude 處理符合檔案時載入），或修剪非每次 session 都需要的內容。用 `@path` imports 有助於組織，但不減少 context（匯入的檔案仍在啟動時載入）。

### `/compact` 後指令消失

Project-root CLAUDE.md 在 compaction 後存活：Claude 重新從磁碟讀取並重新注入 session。子目錄的 CLAUDE.md 不會自動重新注入，下次 Claude 讀取那個子目錄的檔案時才會重載。

只在對話中給出的指令在 compaction 後消失。解法：把這些指令加到 CLAUDE.md。

---

## Related Resources

- [Debug your configuration](/en/debug-your-config) — 診斷 CLAUDE.md 或 settings 為何未生效
- [Skills](/en/skills) — 打包按需載入的可重用 workflows
- [Settings](/en/settings) — 用 settings files 設定 Claude Code 行為
- [Subagent memory](/en/sub-agents#enable-persistent-memory) — 讓 subagents 維護自己的 auto memory

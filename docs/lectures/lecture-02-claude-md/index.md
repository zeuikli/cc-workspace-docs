# Lecture 02：CLAUDE.md 設計

## 學習目標

完成本課後，你將能夠：

- 區分 CLAUDE.md 與 Auto Memory 兩種記憶系統的用途與載入機制
- 正確設定四個層級的 CLAUDE.md（managed policy / project / user / local）
- 運用 Ratchet 原則讓每行規則追蹤到具體失敗
- 使用 `@file` imports 組織多層指令檔案

## 核心概念

### 兩種記憶系統對照

Claude Code 有兩套平行的記憶機制：

| 面向 | CLAUDE.md files | Auto Memory（MEMORY.md）|
|------|-----------------|-------------|
| **誰寫** | 你（人類） | Claude（自動） |
| **內容** | 指令和規則 | 學習成果和 patterns |
| **範圍** | 專案、用戶、組織 | 每個 working tree |
| **載入到** | 每次 session | 每次 session（前 200 行或 25KB）|
| **適合** | 程式碼標準、workflows、專案架構 | Build 指令、debug insights、Claude 自己發現的偏好 |

**核心原則**：兩個系統的內容都在每次對話開始時作為 context 載入。Claude 將其視為 context 而非強制設定。**指令愈具體簡潔，Claude 遵循得愈穩定。**

### CLAUDE.md 四層作用域

| 層級 | 路徑 | 用途 | 共用對象 |
|------|------|------|---------|
| **Managed policy** | macOS: `/Library/Application Support/ClaudeCode/CLAUDE.md`<br>Linux/WSL: `/etc/claude-code/CLAUDE.md` | IT/DevOps 管理的組織全員指令 | 組織所有用戶 |
| **Project** | `./CLAUDE.md` 或 `./.claude/CLAUDE.md` | 團隊共用的專案指令 | 透過 source control 共用 |
| **User** | `~/.claude/CLAUDE.md` | 所有專案的個人偏好 | 只有你（所有專案） |
| **Local** | `./CLAUDE.local.md` | 個人專案特定偏好（加入 .gitignore）| 只有你（當前專案） |

**載入順序**：CLAUDE.md 和 CLAUDE.local.md 在工作目錄**以上**的目錄層級在啟動時完整載入。子目錄的檔案在 Claude 讀取那些目錄的檔案時按需載入。

### Ratchet 原則：每行規則追蹤到具體失敗

來自 Mitchell Hashimoto：

> 「Anytime you find an agent makes a mistake, you take the time to engineer a solution such that the agent never makes that mistake again.」

Addy Osmani 的延伸：

> 「Every line in a good AGENTS.md should be traceable back to a specific thing that went wrong.」

**何時加入新規則**：
- Claude 同一個錯誤犯了第二次
- Code review 抓到 Claude 應該知道的 codebase 事項
- 你輸入了上次 session 也輸入過的同樣修正或說明
- 新團隊成員需要同樣的 context 才能有效工作

**Ratchet 原則的實踐意義**：Harness 不是「預先設計的架構」，而是「從失敗中沉澱的規則集合」。每次失敗都是一次 Harness 改進的機會。

### 寫有效指令的原則

**大小限制**：每個 CLAUDE.md 目標在 200 行以內。超過 → 用 path-scoped rules（只在 Claude 處理符合路徑的檔案時載入）。

**結構**：用 markdown headers 和 bullets 分組相關指令。

**具體性原則**（最重要）：

| 模糊（❌）| 具體（✅）|
|---------|---------|
| "Format code properly" | "Use 2-space indentation" |
| "Test your changes" | "Run `npm test` before committing" |
| "Keep files organized" | "API handlers live in `src/api/handlers/`" |

**內容類型分類**：

「放什麼」：每次 session 都需要的事實：build 指令、慣例、專案結構、「always do X」規則。

「不放什麼」：多步驟流程或只在某個 codebase 部分重要的事項 → 移到 skill 或 path-scoped rule。

### AGENTS.md 相容性

Claude Code 讀 `CLAUDE.md`，不讀 `AGENTS.md`。要讓兩個工具（Claude Code + 其他工具如 OpenAI Codex）共用同一份指令：

```markdown
@AGENTS.md

## Claude Code 專用設定
Use plan mode for changes under `src/billing/`.
```

這樣 Claude Code 會讀到 AGENTS.md 的內容（透過 import），同時也有 Claude Code 專用的補充設定。

### Path-Scoped Rules（路徑範圍規則）

當某個規則只適用於特定目錄時，使用 path-scoped rules 而非在根 CLAUDE.md 裡塞入大量條件判斷：

```markdown
<!-- .claude/rules/frontend.md — 只在 Claude 處理 src/frontend/ 下的檔案時載入 -->
# Frontend Rules
- 所有元件使用 React + TypeScript
- CSS 用 Tailwind，不用 inline styles
- 元件放在 `src/frontend/components/`
```

在根 CLAUDE.md 中引用：

```markdown
## 路徑規則
- 前端相關：@.claude/rules/frontend.md
- API 相關：@.claude/rules/api.md
```

## 程式碼範例

### 一個完整的 Project CLAUDE.md 範例

```markdown
# My API Project

> 最後更新：2026-05-01（因為 Claude 連續兩次用了錯誤的 SQLAlchemy 語法）

## 技術棧
- Python 3.12
- FastAPI 0.115
- SQLAlchemy 2.0（注意：使用新版 async session API，不是 1.x 的舊語法）
- PostgreSQL 16
- Redis 7（用於 session cache）
- 套件管理：uv（不用 pip install，用 uv add）

## 驗證命令（每次變更後都要跑）
```bash
# 單元測試
pytest tests/ -q --tb=short

# 類型檢查（必須通過 strict mode）
python -m mypy src/ --strict

# Lint
ruff check src/
```

## 架構約定
- API handlers 放在 `src/api/handlers/`，每個 router 一個檔案
- 所有新 endpoint 必須通過 OAuth 2.0 認證（`src/auth/middleware.py`）
- 資料庫 migration 用 alembic，不直接修改 schema
- 錯誤處理統一使用 `src/utils/errors.py` 的 `APIError` class

## 禁止事項（每條都有具體原因）
- ❌ 不用 `Session()` 建立 DB session（改用 `get_db()` dependency）
  - 原因：2026-04-15 造成 connection leak bug
- ❌ 不在 handler 裡直接 import settings（改用 `from src.config import get_settings`）
  - 原因：2026-05-01 造成測試環境無法覆寫設定

## 完成定義
一項任務完成 = pytest 全通過 + mypy --strict 無錯誤 + ruff 無警告
```

### 使用 @imports 分割大型 CLAUDE.md

```markdown
<!-- 根目錄的 CLAUDE.md -->
# My Project

## 概覽
這是一個 FastAPI + PostgreSQL 的 API 服務。

See @README.md for project overview and @package.json for available npm commands.

## 路徑特定規則
- 前端：@.claude/rules/frontend.md
- API 層：@.claude/rules/api.md
- 測試：@.claude/rules/testing.md

## 個人偏好（Local Override）
- @~/.claude/my-personal-preferences.md
```

### 快速初始化 CLAUDE.md

```bash
# 在專案根目錄執行 Claude Code
/init

# 啟用互動式多階段流程（詢問要設置什麼、用 subagent 探索 codebase）
CLAUDE_CODE_NEW_INIT=1 claude
```

### 路徑範圍規則的目錄結構

```
myproject/
├── CLAUDE.md              ← 根指令（全域規則）
├── CLAUDE.local.md        ← 個人本地偏好（加入 .gitignore）
└── .claude/
    └── rules/
        ├── frontend.md    ← 只在處理前端檔案時載入
        ├── api.md         ← 只在處理 API 檔案時載入
        └── testing.md     ← 只在處理測試時載入
```

## 常見問題與注意事項

**Q：CLAUDE.md 有多大算太大？**

A：目標在 200 行以內。超過後 Claude 反而容易忽略後半部分的規則（context 前段的指令優先效應）。解法：把特定路徑的規則移到 path-scoped rules，保持根 CLAUDE.md 精簡。

**Q：子目錄的 CLAUDE.md 什麼時候載入？**

A：在 Claude 讀取那些目錄的檔案時**按需載入**，不是啟動時全部載入。這是為了節省 context。如果你有 10 個子目錄各有 CLAUDE.md，Claude 不會在啟動時把全部都讀進來。

**Q：如何跨 Git worktrees 共用個人指令？**

A：`CLAUDE.local.md` 只存在於建立它的那個 worktree（因為它通常加入 `.gitignore`）。要在所有 worktrees 共用個人指令，在 CLAUDE.local.md 裡加入：

```markdown
# Individual Preferences
- @~/.claude/my-project-instructions.md
```

這樣不論在哪個 worktree，都會讀到同一份個人設定。

**Q：Auto Memory 和 CLAUDE.md 衝突怎麼辦？**

A：CLAUDE.md 的規則優先於 Auto Memory 的學習成果。如果 Auto Memory 學到了錯誤的 pattern，你需要在 CLAUDE.md 明確覆寫它，或者清空 Auto Memory（`/memory clear`）。

**Q：Imports 的遞迴深度限制是多少？**

A：最大深度 5 層。首次遇到外部 imports 時 Claude Code 會顯示核准對話框。

## 本課小結

- **兩種記憶系統**：CLAUDE.md（你寫，規則）vs Auto Memory（Claude 寫，學習成果）。兩者在每次 session 開始時都載入到 context。
- **四層作用域**：managed policy → project → user → local。越靠後越個人化，越靠前越強制。
- **Ratchet 原則**：每條規則都應該追蹤到一次具體的失敗。CLAUDE.md 是「從失敗中沉澱的規則集合」。
- **具體性**：「Use 2-space indentation」比「Format code properly」好 100 倍。
- **大小控制**：200 行以內。超過就用 path-scoped rules 分割。
- **@imports**：允許模組化組織，遞迴深度最大 5 層。

## 延伸閱讀

- [Lecture 01：Claude Code 與 Harness 基礎](/lectures/lecture-01-foundations/) — 理解 Harness 在 Agent 中的位置
- [Lecture 05：記憶系統與工作區設計](/lectures/lecture-05-memory-workspace/) — Auto Memory 的詳細機制
- [Project 01：從零建立你的第一個 Workspace](/projects/project-01-init-workspace/) — 動手建立你的 CLAUDE.md
- [官方文件：Claude Code Memory](https://code.claude.com/docs/en/memory)

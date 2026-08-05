# 自訂 Claude Code 行為的七種機制

> **Source:** https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more  
> **Date:** 2026-06-18  
> **Type:** 官方指南 — 七種機制選擇指南

---

## 概述

官方整理七種自訂 Claude Code 行為的機制，並提供清晰的選擇決策框架。核心問題：

- 要改變 **Claude 知道什麼**（Know）→ CLAUDE.md / Rules / Skills
- 要改變 **Claude 呼叫什麼工具**（What Tools）→ Subagents / MCP
- 要在 **生命週期事件自動執行**（Automate）→ Hooks
- 要改變 **Claude 回應的外觀**（Output Appearance）→ Output Styles / System Prompt Appending

---

## 七種機制

### 1. CLAUDE.md

**用途**：提供持久 context，告訴 Claude 你的工作環境和偏好。

- 存放位置：workspace 根目錄 `CLAUDE.md`（影響整個 workspace），或子目錄（影響子目錄）
- 適合：tech stack、常見命令、Code style、專案特定慣例、重要目錄
- **長度 ≤ 200 行（最佳 60 行）**，只寫會改變 Claude 行為的內容
- Claude 在 session 開始時自動載入
- 大型規則用 `.claude/rules/*.md` + `@import` 拆分

### 2. Rules（Path-scoped Rules）

**用途**：針對特定路徑的條件式指令，避免不相關 token 消耗。

```markdown
---
paths:
  - "**/*.py"
  - "src/api/**"
---
# Python 特定規則
使用 Pydantic V2 型別標注...
```

- 只在存取相關檔案時載入，降低 token 消耗
- 適合：語言特定規範、目錄特定流程、安全敏感區域的額外限制
- 比 CLAUDE.md 主體更符合「按需載入」原則

### 3. Skills

**用途**：打包可重用的知識、工作流和最佳實踐。

- 存放位置：`.claude/skills/<name>/`（資料夾形式，非只是 markdown）
- **初始只載入名稱與描述**，呼叫時才展開全文（降低 context 成本）
- 支援 nested 子目錄：`.claude/skills/backend/postgres/`（v2.1.178+）
- 名稱衝突以 `<dir>:<name>` 表示

**Skill 的最佳 description 格式**：
```markdown
---
description: 當需要...時使用。Do NOT use for: ...
---
```

**九大 Skill 類別**（Anthropic 內部分類）：
1. Library/API Reference（程式庫參考）
2. Product Verification（產品驗證）
3. Data Fetching（資料抓取）
4. Business Process（業務流程）
5. Code Scaffolding（代碼鷹架）
6. Code Quality（代碼品質）
7. CI/CD（持續整合部署）
8. Runbooks（操作手冊）
9. Infrastructure Ops（基礎架構操作）

### 4. Subagents

**用途**：將任務委派給獨立 context window 的 Claude 實例，並行或隔離執行。

- 適合：research 密集任務、需要並行的任務、需要隔離 context 的驗證任務
- **委派門檻**：預期工具呼叫 > 20 次，或讀取 ≥ 10 個檔案
- v2.1.178 起：Agent Teams 簡化，直接用 `Agent` tool 的 `name` 參數 spawn 隊友，無需 `TeamCreate`/`TeamDelete`

### 5. Hooks

**用途**：生命週期事件的確定性觸發器（非 Claude 建議，是硬執行）。

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Write",
      "hooks": [{"type": "command", "command": "prettier --write $FILE_PATH"}]
    }]
  }
}
```

- **事件類型**：PreToolUse / PostToolUse / Notification / Stop / PreCompact
- **Exit code**：0=成功、1=警告繼續、2=阻斷
- 適合：自動格式化、linter、Slack 通知、封鎖危險操作、test runner
- v2.1.178+：`Tool(param:value)` 語法支援工具輸入參數比對

### 6. Output Styles

**用途**：改變 Claude 回應格式而無需修改 Prompt。

- 在 CLAUDE.md 中定義：`偏好列點清單而非散文回應`
- 適合：統一團隊輸出格式、特定輸出格式需求（JSON / XML / etc.）

### 7. System Prompt Appending

**用途**：透過 API 或 Claude Code SDK 在系統 prompt 末尾追加指令。

- 適合：動態注入 context（如當前日期/用戶資訊）、多租戶系統
- `<system-reminder>` 標籤：在訊息流中注入動態更新，保護 system prompt 快取前綴不失效

---

## 選擇指南

| 需求 | 使用機制 |
|------|---------|
| 改變 Claude 知道的事情（持久） | CLAUDE.md |
| 路徑特定規則（按需） | Path-scoped Rules |
| 可重用工作流或知識 | Skills |
| 並行任務 / 隔離 context | Subagents |
| 生命週期自動化（硬執行） | Hooks |
| 輸出格式設定 | Output Styles |
| 動態 context 注入 | System Prompt Appending |

---

## 關鍵原則

1. **機制組合使用**：CLAUDE.md + Rules + Skills + Hooks 是大型 Codebase 的完整 Harness
2. **惰性載入**：Skills 和 Path-scoped Rules 只在需要時載入，優先選擇這些機制降低 token 消耗
3. **Hooks 是確定性的**：Hooks 不受 prompt 影響，比在 CLAUDE.md 中說「請記得格式化」更可靠
4. **每 3-6 個月審閱**：模型更新後，舊指令可能反而限制新模型能力
5. **CLAUDE.md 精簡**：只放「會改變 Claude 行為的內容」，可從 repo 推導的資訊 = 噪音

---

## 延伸閱讀

- [01-official-hooks-memory-settings.md](./01-official-hooks-memory-settings.md) — Hook 詳細架構
- [06-agent-skills-best-practices.md](./06-agent-skills-best-practices.md) — Skill 撰寫原則
- [21-memory-claudemd.md](./21-memory-claudemd.md) — CLAUDE.md 多層級設定
- [33-skills-nine-categories.md](./33-skills-nine-categories.md) — Skill 九大類別詳解

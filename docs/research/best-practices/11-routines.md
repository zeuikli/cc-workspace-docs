---
title: Routines — 排程自動化完整指南
source: "https://code.claude.com/docs/en/routines"
type: best-practices
---

# Routines — 排程自動化完整指南

> 來源：https://code.claude.com/docs/en/routines
> 收錄日期：2026-05-01
> 涵蓋：Scheduled / API trigger / GitHub Webhook 三種觸發模式、Routine 建立流程、管理操作、使用限額

---

## 什麼是 Routine？

Routine 是一個儲存的 Claude Code 設定：prompt、一或多個 repository、及一組 connector，一次設定後自動反覆執行。Routine 跑在 **Anthropic 管理的雲端基礎設施**，筆電關掉仍可持續運作。

> 狀態：Research Preview，行為、限額和 API 介面可能異動。

每個 Routine 可以附加一或多個觸發器：

| 觸發類型 | 說明 |
|---------|------|
| **Scheduled** | 定期排程（hourly / daily / weekly），或一次性指定時間點執行 |
| **API** | 透過 HTTP POST 到專屬 endpoint 按需觸發 |
| **GitHub** | 對應 repository event（PR、Release 等）自動觸發 |

同一個 Routine 可混用多種觸發器。例如：PR review Routine 可以每晚執行、也可從 deploy script 觸發、也可對每個新 PR 觸發。

**適用方案**：Pro、Max、Team、Enterprise（需啟用 Claude Code on the web）。  
**管理入口**：[claude.ai/code/routines](https://claude.ai/code/routines) 或 CLI `/schedule`。

---

## 常見使用情境

| 情境 | 觸發方式 | 說明 |
|------|---------|------|
| **Backlog 自動維護** | Schedule（每週日） | 讀取新 issue → 貼標 → 指派負責人 → Slack 摘要 |
| **Alert 分診** | API（監控工具呼叫） | 收 alert payload → 拉 stack trace → 比對近期 commit → 開 draft PR |
| **客製 Code Review** | GitHub（PR opened） | 套用 team checklist → 留 inline comment → 加摘要留言 |
| **Deploy 驗證** | API（CD pipeline） | 跑 smoke test → 掃 error log → 貼 go/no-go 到 release channel |
| **文件 drift 偵測** | Schedule（每週） | 掃合併 PR → 標出 API 變更對應文件 → 開更新 PR |
| **SDK 跨語言 port** | GitHub（PR merged） | 一個 SDK 合併後自動 port 到另一語言 SDK，開配對 PR |

---

## 建立 Routine

### 三個入口（同步到同一帳號）

1. **Web**：[claude.ai/code/routines](https://claude.ai/code/routines) → New routine
2. **Desktop App**：側邊欄 Routines → New routine → 選 **Remote**（Local = Desktop 本機任務）
3. **CLI**：`/schedule` 或 `/schedule <自然語言描述>`

### 建立流程（Web 表單）

1. **命名 + Prompt**：Routine 自主執行，prompt 必須完整自給、明確說明目標與成功定義。表單含 model selector。
2. **選 Repository**：加入一或多個 GitHub repo。每次執行時從 default branch clone 開始，修改推送到 `claude/`-prefixed branch。
3. **選 Environment**：控制 network access、environment variables、setup script（結果有 cache，不每次重跑）。預設提供 Default environment。
4. **選 Trigger**：Schedule、GitHub event、API（任意組合）。
5. **設定 Connectors & Permissions**：所有已連接的 MCP connector 預設全部包含，按需移除。啟用 **Allow unrestricted branch pushes** 允許推送到非 `claude/` 前綴分支。

### 重要安全注意

- Routine 以自主模式執行（無 permission-mode picker、無 approval prompt）
- Routine 歸屬個人 claude.ai 帳號，不與隊友共享
- 計入個人帳號的每日執行次數上限
- 所有 commit/PR/connector action 都會以你的身份出現

---

## 觸發器設定

### 1. Schedule 觸發器

**預設頻率**：hourly / daily / weekdays / weekly（時間以本地時區輸入，自動轉換）。  
**自訂 cron**：在表單選最接近的 preset，再用 `/schedule update` 設定 cron expression（最小間隔 1 小時）。  
**執行延遲**：可能晚幾分鐘，但每個 Routine 的偏移量固定。

#### 一次性執行（One-off Run）

```text
/schedule tomorrow at 9am, summarize yesterday's merged PRs
/schedule in 2 weeks, open a cleanup PR that removes the feature flag
```

- 自動解析自然語言時間，確認後儲存
- 執行後自動 disable，UI 標示 **Ran**
- **不計入每日 Routine 次數上限**（計入一般 session 用量）

### 2. API 觸發器

每個 Routine 有獨立 HTTP endpoint，POST 後開啟新 session 並回傳 session URL。

#### 設定步驟

1. 編輯 Routine → Add another trigger → API
2. 複製 URL → 點 **Generate token**（token 只顯示一次，立即儲存）
3. 要輪換或撤銷 token：回同一視窗點 Regenerate / Revoke

#### 呼叫範例

```bash
curl -X POST https://api.anthropic.com/v1/claude_code/routines/trig_01ABCDEFGHJKLMNOPQRSTUVW/fire \
  -H "Authorization: Bearer sk-ant-oat01-xxxxx" \
  -H "anthropic-beta: experimental-cc-routine-2026-04-01" \
  -H "anthropic-version: 2023-06-01" \
  -H "Content-Type: application/json" \
  -d '{"text": "Sentry alert SEN-4521 fired in prod. Stack trace attached."}'
```

**回傳**：

```json
{
  "type": "routine_fire",
  "claude_code_session_id": "session_01HJKLMNOPQRSTUVWXYZ",
  "claude_code_session_url": "https://claude.ai/code/session_01HJKLMNOPQRSTUVWXYZ"
}
```

- `text` 欄位：可選，傳入 alert body 等 run-specific context（純文字，不解析結構）
- Beta header：`experimental-cc-routine-2026-04-01`（breaking changes 換新日期 header，舊版保留至少兩個版本）
- 完整 API reference：[platform.claude.com/docs/en/api/claude-code/routines-fire](https://platform.claude.com/docs/en/api/claude-code/routines-fire)

### 3. GitHub Webhook 觸發器

> Research Preview 期間：GitHub event 有每 Routine 和每帳號的每小時上限，超出則丟棄。  
> 需要安裝 Claude GitHub App（與 `/web-setup` 的 clone 授權不同）。

#### 支援的事件

| Event | 觸發時機 |
|-------|---------|
| Pull request | PR 開啟、關閉、指派、貼標、同步等 |
| Release | Release 建立、發布、編輯、刪除 |

#### PR 過濾條件

所有條件需同時符合才觸發：

| 欄位 | 可用 operator |
|------|--------------|
| Author | equals / is one of / is not one of |
| Title | contains / starts with / matches regex |
| Body | contains / starts with / matches regex |
| Base branch | equals / contains / matches regex |
| Head branch | equals / contains / matches regex |
| Labels | is one of / is not one of |
| Is draft | true / false |
| Is merged | true / false |

> **注意**：`matches regex` 測試整個欄位值，不是 substring 匹配。`.*hotfix.*` 才能匹配含 `hotfix` 的 title。

**過濾範例**：
- Auth 模組 review：base branch = `main`，head branch contains `auth-provider`
- 只處理 ready PR：is draft = `false`
- Label 觸發 backport：labels include `needs-backport`

#### Session 與 Event 的對應

每個匹配的 GitHub event 產生一個獨立 session，不跨 event 重用 session。

---

## 管理 Routine

| 操作 | 方法 |
|------|------|
| 立即執行 | 詳情頁點 **Run now** |
| 暫停 / 恢復 | Repeats 區塊 toggle |
| 編輯 | 點鉛筆圖示 → Edit routine（可改 name、prompt、repo、env、connectors、觸發器）|
| 刪除 | 點刪除圖示（過去的 session 保留在 session 列表）|

### CLI 管理指令

```bash
/schedule list           # 列出所有 Routines
/schedule update         # 修改現有 Routine
/schedule run            # 立即觸發執行
```

### Repository 與分支設定

- 每次執行從 default branch clone（除非 prompt 另有指定）
- 預設只能推送到 `claude/`-prefixed 分支（防止意外修改主分支）
- 啟用 **Allow unrestricted branch pushes** 解除此限制

---

## 使用限額

| 項目 | 說明 |
|------|------|
| 每日 Routine 次數 | 視方案而定，見 [claude.ai/code/routines](https://claude.ai/code/routines) 或 [claude.ai/settings/usage](https://claude.ai/settings/usage) |
| 超出每日上限 | 啟用 extra usage（Settings > Billing）可繼續按用量計費；否則拒絕直到重置 |
| One-off runs | **不計入每日上限**，計入一般 session 用量 |
| 消耗方式 | 與互動 session 相同方式扣用量 |

---

## Routines 與相關功能比較

| 功能 | 執行位置 | Terminal 需開？ | 適用情境 |
|------|---------|----------------|---------|
| **Routines** | Anthropic 雲端 | 不需要 | 排程、API 觸發、GitHub 事件 |
| **Desktop scheduled tasks** | 本機 | 不需要 | 本機檔案存取 |
| **`/loop`（CLI）** | 本機 | 需要 | 本地定期執行 |
| **GitHub Actions** | CI 環境 | 不需要 | Repository CI pipeline |

---

## 延伸閱讀

- [claude.ai/code/routines](https://claude.ai/code/routines) — Routines 管理入口
- [Desktop scheduled tasks](https://code.claude.com/docs/en/desktop-scheduled-tasks) — 本機排程任務
- [Cloud environment](https://code.claude.com/docs/en/claude-code-on-the-web#the-cloud-environment) — 雲端執行環境設定
- [MCP connectors](https://code.claude.com/docs/en/mcp) — 連接外部服務
- [GitHub Actions](https://code.claude.com/docs/en/github-actions) — CI pipeline 整合
- [Routine API reference](https://platform.claude.com/docs/en/api/claude-code/routines-fire) — 完整 API 文件

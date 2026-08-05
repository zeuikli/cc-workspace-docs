# Claude Managed Agents 排程部署與 Vault 金鑰管理

> 來源：[New in Claude Managed Agents: run agents on a schedule and store environment variables in vaults](https://claude.com/blog/whats-new-in-claude-managed-agents)（2026-06-09）  
> 來源：[Authenticate with vaults - Claude API Docs](https://platform.claude.com/docs/en/managed-agents/vaults)  
> 整理日期：2026-06-15

---

## 概覽

2026-06-09 Managed Agents Public Beta 新增兩大功能：

1. **Scheduled Deployments**：無需自建排程基礎設施，Agent 依 cron 自動執行重複任務
2. **Vaults with Environment Variables**：安全管理 CLI 工具和第三方服務所需的 API Key，Agent 運行時永遠不暴露真實金鑰

---

## Scheduled Deployments（排程部署）

### 工作原理

```
開發者設定 cron schedule
    ↓
每次 cron 觸發 → Managed Agents 自動啟動新 session
    ↓
Agent 完成任務（與一般 session 相同行為）
    ↓
Session 結束，等待下次 cron 觸發
```

### 設定方式

在建立 Scheduled Deployment 時提供：
- **Cron 表達式**（標準 5-field cron 格式）
- **Agent 任務描述**（prompt）
- **工具和 connector 授權**（與一般 deployment 相同）

### 典型使用場景

| 頻率 | 使用案例 |
|------|---------|
| 夜間（nightly） | 資料同步、日誌彙整 |
| 每週（weekly） | 合規掃描、技術債 audit |
| 每日（daily） | Digest 摘要、監控報告 |
| 每小時 | 狀態健康檢查、指標收集 |

### 與 Routines 的差異

| | **Routines**（Claude Code） | **Scheduled Deployments**（Managed Agents） |
|-|------|------|
| 對象 | 開發者 IDE/CLI 工作流 | 生產 API 部署 |
| 限額 | Pro 5/日、Max 15/日 | 按 API 計費 |
| 觸發 | Schedule / API / GitHub Webhook | Cron |
| 環境 | 本地或 Claude 雲端 | Managed Agents 基礎設施 |

---

## Vaults with Environment Variables

### 安全模型

```
開發者 → 向 Vault 註冊 API Key
            ├── 指定環境變數名稱（如 GITHUB_TOKEN）
            └── 指定允許的網域（如 api.github.com）

Agent 運行時：
  Sandbox 收到 placeholder（不是真實 Key）
      ↓
  Agent 執行 CLI 工具 → 工具用 placeholder 呼叫 API
      ↓
  請求到達網路邊界 → Anthropic 基礎設施自動將 placeholder 替換為真實 Key
      ↓
  只有目標網域收到真實 Key（其他網域的請求被拒絕）
```

Agent 程式碼中永遠看不到真實 API Key——只有 placeholder。

### 設定 Vault

```python
# 透過 Managed Agents API 建立 vault entry
vault.create(
    name="GITHUB_TOKEN",         # 環境變數名稱
    value="ghp_...",             # 真實 API Key（只傳一次）
    allowed_domains=["api.github.com"],  # 限制允許的網域
)
```

### 適用工具類型

- **CLI 工具**：gh、aws、gcloud、kubectl 等需要 env var 認證的工具
- **已安裝套件**：npm 私有 registry、pip 私有 index
- **第三方 API**：Slack、Jira、PagerDuty 等

### 限制

- 真實 Key **只在網路邊界**替換——agent 無法讀取、記憶或洩漏 Key
- 每個 Vault entry 只能存取**指定網域**（最小權限原則）
- 不適用於需要 interactive OAuth flow 的情境（仍需使用 MCP connector + OAuth）

---

## 整合使用模式

### 範例：夜間 Code Quality Audit

```
排程：每天 00:00 UTC
任務：
  1. 拉取 main branch 最新狀態（使用 GITHUB_TOKEN vault）
  2. 對變更的檔案執行 /deep-review skill
  3. 將發現寫入 Issues（使用 GITHUB_TOKEN vault）
  4. 發送 Slack 摘要（使用 SLACK_BOT_TOKEN vault）
```

```
排程：每週日 02:00 UTC
任務：
  1. 掃描所有 open PRs（使用 GITHUB_TOKEN）
  2. 識別停滯超過 7 天的 PR
  3. 自動加 stale 標籤並留言
```

---

## 搭配 post-session lifecycle hook（Claude Code v2.1.169+）

Claude Code v2.1.169 新增 `post-session` hook，在 session 結束後、workspace 刪除前執行：

```json
{
  "lifecycle": {
    "postSession": "bash scripts/export-artifacts.sh"
  }
}
```

可用於：快照未提交的工作、匯出日誌到外部系統、發送 webhook 通知。

---

## 延伸閱讀

- `09-secure-deployment.md` — Agent 安全部署與憑證管理
- `14-mcp.md` — MCP OAuth 完整設定（interactive OAuth flow）
- `13-sandbox.md` — Sandbox 隔離技術詳解
- `11-routines.md` — Routines（Claude Code 排程，開發者工作流）

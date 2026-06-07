---
title: "Claude Code Enterprise Security Deployment"
author: "Rez Havaei, Rex Liu, Maximilian Li"
date: 2026-05-22
source: "https://generalanalysis.com/guides/claude-code-enterprise-security-deployment"
tags: [claude-code, enterprise, security, managed-settings, dev-containers, MCP, telemetry, kill-switch]
topic: enterprise
---

# Claude Code Enterprise Security Deployment

General Analysis 的三位作者提供了企業規模 Claude Code 部署的七層控制架構，以三個 repo 風險等級為主軸，從低風險預設到受監管環境建立分層防禦。

## 七層控制架構

1. **Managed Settings**
   政策分發：permission modes、deny rules、MCP controls、telemetry export。集中管理，開發者無法本機覆蓋。

2. **Dev Containers & Isolation**
   非 root 執行、scoped mounts、明確的 egress allowlist。防止 agent 存取宿主機敏感資源。

3. **Corporate Proxy**
   所有網路流量經控制節點路由，含 domain allowlists 與 metadata preservation。

4. **MCP Governance**
   - 以精確 URL/command 審批（版本釘定）
   - 憑證 scoping（每個 MCP server 最小權限）
   - 集中撤銷機制（不需等開發者更新本機檔案）

5. **Hooks（確定性強制執行）**
   針對敏感檔案編輯觸發、生成 audit evidence。關鍵：必須用 exit 2 阻塞（非 exit 1）。

6. **OpenTelemetry**
   結構化事件捕捉，供事後調查與 retest 驗證。每個管控動作都有可追溯的 trace。

7. **CI/CD Gates**
   臨時性 job、短期憑證（ephemeral credentials）、生產變更需人工核准。

## 三個 Repo 風險等級

| 等級 | 類型 | 控制措施 |
|------|------|---------|
| **Low-risk** | 預設 + 基本 telemetry | 標準 Claude Code 配置 |
| **Production-adjacent** | Plan mode + hook 強制 + MCP allowlists | 所有工具呼叫需審批 |
| **Regulated/Sensitive** | Dev containers + strict routing + 獨立審核 | 最嚴格隔離 |

## Kill-Switch 架構（關鍵設計）

> 「安全團隊必須能在不等待每位開發者更新本機檔案的情況下，撤銷 MCP server、停用 permission exception、封鎖 destination、停用 hook source、輪換憑證、或將 repo 移至更嚴格等級。」

集中化政策分發是 kill-switch 的前提，確保安全反應時間以分鐘而非天計。

## 利害關係人所有權模型

防止控制漂移（control drift）的明確分工：
- **安全團隊**：基線設定 + 驗證
- **平台工程**：配置交付
- **AppSec**：repo 等級分類
- **DevOps**：CI profile 管理

## Managed Settings 更新規範

每次 managed settings 更新必須包含：
- 受影響的使用者群組 + repositories
- 已變更的規則
- 接受的風險
- 預期的 telemetry
- Rollback plan
- Retest cases

## 事件後應對

事後補救需三個輸出：
1. **Timeline**：攻擊時間線
2. **Control change**：已更改的控制措施
3. **Retest case**：證明攻擊路徑不再可行的測試案例

## Key Insights
- 七層控制架構跨三個 repo 風險等級：低風險（預設+基本 telemetry）、production-adjacent（plan mode+hook 強制+MCP allowlists）、regulated（dev containers+strict routing+獨立審核）
- Kill-switch 架構：安全團隊需能在不等待開發者更新本機檔案的情況下撤銷 MCP/permissions/credentials/移動 repo 等級
- Evidence-driven 事件應對：timeline + control change + retest case 三件組，證明攻擊路徑不再可行

## Code Examples / Commands

```json
// 組織層級 managed settings 範例結構
{
  "managedSettings": {
    "permissions": {
      "allow": ["Bash", "Read", "Write"],
      "deny": ["Bash(rm -rf*)", "Bash(git push --force*)"]
    },
    "mcpServers": {
      "allowlist": [
        "https://approved-mcp.company.com/v1.2.3"
      ]
    },
    "telemetry": {
      "export": "otel://collector.company.com:4317"
    }
  },
  "repositoryTiers": {
    "regulated": ["org/payments-service", "org/auth-service"],
    "productionAdjacent": ["org/api-gateway"],
    "lowRisk": ["org/internal-tools"]
  }
}
```

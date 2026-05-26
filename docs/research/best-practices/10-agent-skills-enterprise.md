---
title: Skills for Enterprise — 治理、安全審查與組織部署指南
source: "https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise"
type: best-practices
---

# Skills for Enterprise — 治理、安全審查與組織部署指南

> 來源：https://platform.claude.com/docs/en/agents-and-tools/agent-skills/enterprise  
> 收錄日期：2026-05-01  
> 涵蓋：安全審查、風險評估、生命週期管理、大規模組織、版本控制

---

## 適用對象

企業管理員和架構師，負責在組織內治理 Agent Skills。涵蓋審查、評估、部署、大規模管理。

---

## 安全審查與風險評估

### 風險層級評估表

| 風險指標 | 查看內容 | 風險等級 |
|---------|---------|---------|
| **Code execution** | Skill 目錄中有 `*.py`、`*.sh`、`*.js` 腳本 | 🔴 高：腳本可完整存取環境 |
| **Instruction manipulation** | 指令要求忽略安全規則、對用戶隱藏行動、條件改變行為 | 🔴 高：可繞過安全控制 |
| **MCP server references** | 引用 MCP tools（`ServerName:tool_name`）| 🔴 高：延伸存取超出 Skill 本身 |
| **Network access** | URL、API endpoint、`fetch`、`curl`、`requests` 呼叫 | 🔴 高：潛在資料外洩 |
| **Hardcoded credentials** | Skill 檔案或腳本內有 API key、token、密碼 | 🔴 高：暴露於 Git 歷史和 context window |
| **File system scope** | Skill 目錄外的路徑、寬泛 glob、路徑穿越（`../`）| 🟡 中 |
| **Tool invocations** | 指示 Claude 使用 bash、file operations 等 tool | 🟡 中 |

### 審查 Checklist

部署任何第三方或內部 Skill 前，完成以下步驟：

1. **閱讀所有 Skill 目錄內容**：SKILL.md、所有引用的 markdown 檔案、腳本
2. **驗證腳本行為符合描述**：在沙箱環境執行腳本，確認輸出與 Skill description 一致
3. **檢查惡意指令**：尋找要求忽略安全規則、對用戶隱藏行動、外洩資料、根據特定輸入改變行為的指令
4. **檢查外部 URL fetch 或網路呼叫**：搜尋 `http`、`requests.get`、`urllib`、`curl`、`fetch`
5. **確認無 hardcoded 憑證**：憑證應使用環境變數或安全憑證存儲，不應出現在 Skill 內容中
6. **列出 Skill 指示 Claude 呼叫的工具**：列出所有 bash 指令、file operations、tool 引用。評估組合風險（file-read + network 工具同時使用）
7. **確認 redirect 目的地**：驗證外部 URL 指向預期域名
8. **確認無資料外洩模式**：尋找讀取敏感資料後寫入、傳送或編碼到外部的指令

> ⚠️ **絕不在完整稽核前部署未信任來源的 Skill**。惡意 Skill 可指示 Claude 執行任意程式碼、存取敏感檔案或對外傳送資料。對待 Skill 安裝應與對待生產系統上安裝軟體同等嚴謹。

---

## 部署前評估

### 評估維度

| 維度 | 衡量內容 | 失敗範例 |
|------|---------|---------|
| **Triggering accuracy** | Skill 對正確查詢啟動，不相關查詢保持靜止？ | Skill 對每次試算表提及都觸發，即使只是討論資料 |
| **Isolation behavior** | Skill 單獨運作是否正常？ | Skill 引用不存在於其目錄中的檔案 |
| **Coexistence** | 加入此 Skill 是否影響其他 Skill？ | 新 Skill description 太寬泛，搶奪其他 Skill 的觸發點 |
| **Instruction following** | Claude 是否正確遵從 Skill 指令？ | Claude 跳過驗證步驟或使用錯誤的 library |
| **Output quality** | Skill 產出是否正確有用？ | 生成的報告有格式錯誤或資料缺漏 |

### 評估要求

- 每個 Skill 提交 **3–5 個代表性查詢**的評估套件：應觸發的情況、不應觸發的情況、模糊邊界情況
- 跨組織使用的模型測試（Haiku、Sonnet、Opus）
- 詳細評估建立指引見 `06-agent-skills-best-practices.md` §評估與迭代

### 評估結果的決策依據

| 訊號 | 行動 |
|------|------|
| Trigger accuracy 下降 | 更新 description 或指令 |
| Coexistence 衝突 | 合併重疊 Skill 或縮窄 description |
| 持續低輸出品質 | 重寫指令或加入驗證步驟 |
| 更新後持續失敗 | 廢棄此 Skill |

---

## Skill 生命週期管理

```
Plan → Create & Review → Test → Deploy → Monitor → Iterate or Deprecate
```

| 階段 | 關鍵動作 |
|------|---------|
| **Plan** | 識別重複、易錯、需要專業知識的工作流程 |
| **Create & Review** | 作者遵循最佳實踐；安全審查（使用上方 checklist）；提交評估套件；**作者不應自我審查** |
| **Test** | 單獨測試 + 與現有 Skill 共存測試；驗證 triggering accuracy、output quality、無回歸 |
| **Deploy** | 透過 Skills API 上傳（workspace 全員可用）；記錄到內部 registry（用途、擁有者、版本）|
| **Monitor** | 追蹤使用模式、收集回饋；定期重跑評估偵測 drift；實作 application-level logging（API 目前不提供 analytics）|
| **Iterate or Deprecate** | 新版本需通過完整評估套件；工作流程改變或評估分數下降 → 更新；評估持續失敗 → 廢棄 |

---

## 大規模組織 Skills

### 召回率限制

同時載入的 Skills 數量過多 → Claude 可能無法選到正確的 Skill。每個 Skill 的 metadata 在 system prompt 中競爭注意力。

- 使用評估套件衡量 recall accuracy，加入 Skill 時追蹤變化，效能下降就停止新增
- **API 請求最多支援 8 個 Skills**；若需更多，考慮合併或按任務類型路由不同 Skill 集

### 從小做起，再整合

鼓勵從窄範圍的工作流程 Skill 開始，隨模式浮現再合併為角色型套件。

```
開始：formatting-sales-reports, querying-pipeline-data, updating-crm-records
整合：sales-operations（用評估確認合併後效能等同個別 Skill）
```

> 只有當合併後 Skill 的評估確認效能等同被取代的個別 Skill，才合併。

### 內部 Registry

每個 Skill 記錄：

| 欄位 | 內容 |
|------|------|
| Purpose | 此 Skill 支援的工作流程 |
| Owner | 負責維護的團隊/個人 |
| Version | 目前部署版本 |
| Dependencies | MCP servers、packages、外部服務 |
| Evaluation status | 最後評估日期與結果 |

### 角色型 Skill 套件

| 角色 | Skill 範例 |
|------|-----------|
| Sales team | CRM 操作、pipeline 報告、提案生成 |
| Engineering | Code review、部署工作流程、Incident response |
| Finance | 報告生成、資料驗證、稽核準備 |

---

## 版本控制與發布

### Source Control

Skill 目錄存放在 Git（SKILL.md + 所有 bundle 檔案 = 一個 Git-tracked 資料夾）：
- 歷史追蹤
- 透過 PR 做 code review
- 回滾能力

### 版本策略

| 環境 | 策略 |
|------|------|
| **Production** | 固定特定版本；升版前跑完整評估套件；每次更新都視為新部署並需完整安全審查 |
| **Dev/Test** | 使用最新版驗證變更 |
| **Rollback** | 保留前一版本備用；新版評估失敗 → 立即回退 |

**Integrity verification**：計算已審查 Skill 的 checksum 並在部署時驗證；使用 signed commits 確保來源可信。

### 跨平台注意事項

> ⚠️ Custom Skills **不跨平台同步**：
> - API 上傳的 Skills 在 claude.ai 和 Claude Code 上不可用
> - 反之亦然

以 Git 作為 single source of truth，跨平台部署需自行實作同步流程。

---

## 快速參考：關鍵數字

| 指標 | 數值 |
|------|------|
| API 每請求最大 Skills 數 | 8 |
| 評估套件最小查詢數 | 3–5 個 |
| Skill description 長度上限 | 1,024 字元 |
| SKILL.md 建議長度上限 | 500 行 |

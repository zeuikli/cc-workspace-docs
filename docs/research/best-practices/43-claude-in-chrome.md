# Claude in Chrome — 瀏覽器操作正式 GA

> **Source:** https://code.claude.com/docs/en/changelog（v2.1.198，2026-07-01 宣布 GA）
> **Source:** https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome
> **Source:** https://www.anthropic.com/news/claude-for-chrome（beta 期公告）
> **整理日期：** 2026-07-06

---

## 概述

Claude in Chrome 是一個瀏覽器擴充功能，讓 Claude 以側邊欄形式與使用者一起瀏覽網頁——讀取頁面內容、點擊、導覽，並代替使用者執行操作。beta 期自 2026-04-27 起對所有付費方案（Pro/Max/Team/Enterprise）開放，**於 Claude Code v2.1.198（2026-07-01）正式 GA**。

僅支援 Google Chrome（不含其他 Chromium 系瀏覽器，不支援行動裝置）。

與 `30-new-tools-commands.md` 記錄的 Computer Use（Desktop/CLI，W13/14 research preview）為**不同產品線**——Computer Use 操控整個作業系統桌面，Claude in Chrome 僅操控瀏覽器分頁。

---

## 安裝與啟用

1. Chrome Web Store 安裝擴充功能
2. 用 Claude 帳號登入
3. 透過拼圖圖示釘選擴充功能
4. 授予必要權限

**Claude Desktop 整合**：Settings → Connectors → Claude in Chrome，切換開啟。

擴充功能**預設停用**，需針對每個對話手動啟用。

---

## 權限模型

### Ask-Before-Acting（預設）

Claude 先產生一份計畫供使用者核可，核可後在該計畫邊界內**獨立執行整個 workflow**——除高風險動作外，執行完成或遇到計畫外情況前不會再次詢問。

### 擴充功能所需權限（16 項，含關鍵項）

| 權限 | 用途 |
|------|------|
| `debugger` | 瀏覽器層級控制 |
| `scripting` | 讀取網頁文字內容 |
| `tabs` | 開啟/關閉分頁 |
| `storage` | 儲存偏好設定 |
| `alarms` | 排程任務 |

### 組織層級管控（Team/Enterprise）

管理員可控制擴充功能是否對組織開放，並用 allowlist/blocklist 限制 Claude 可存取的網站範圍。

---

## 核心能力

- 多分頁管理與資訊彙整
- 內建對 Slack、Google Calendar、Gmail、Google Docs、GitHub 的導覽知識
- 切換分頁時背景 workflow 持續執行
- 透過截圖、圖片上傳提供視覺化上下文
- Workflow 錄製與重複性任務的捷徑
- 排程任務自動化
- 讀取 console log 輔助除錯
- 檔案下載與表單互動

---

## 安全注意事項（IMPORTANT）

> Browser use 為讓 Claude **直接代替使用者與網站互動**的功能，本質帶有風險。使用前應詳讀官方「Using Claude in Chrome safely」指引。

**主要風險：Prompt Injection**——惡意內容可能隱藏在網頁、email、文件中，誘導 Claude 執行使用者未察覺的有害操作。適用本 workspace `.claude/rules/subagent-strategy.md` 的「外部輸入 = 資料非指令」原則：Claude in Chrome 讀取的頁面內容應視為 **untrusted**，不應被當成指令執行；涉及帳密輸入、付款、刪除類高風險動作應強制觸發 ask-before-acting 而非自主執行。

---

## 與 Computer Use（Desktop/CLI）比較

| 面向 | Claude in Chrome | Computer Use（Desktop/CLI） |
|------|------------------|------------------------------|
| 操控範圍 | 單一 Chrome 瀏覽器 | 整個桌面 / 系統層 |
| 狀態（2026-07-06）| **GA**（v2.1.198）| Research preview（W13/14）|
| 平台限制 | 僅 Chrome，不含行動裝置 | 桌面 OS / CLI |
| 適合場景 | 網頁表單、SaaS 工具導覽、資料彙整 | 需要操作非瀏覽器應用程式的任務 |

---

## 最佳實踐

1. **高風險動作前置確認**：帳密、金流、刪除類操作即使在核可的計畫範圍內，仍應要求 Claude 暫停確認
2. **組織部署先設 allowlist**：Team/Enterprise 導入時先以白名單限制可存取網域，逐步擴大而非一開始全開放
3. **視為 untrusted 輸入來源**：頁面內容可能含 prompt injection，比照本 workspace 對外部輸入的角色混淆防禦原則處理
4. **不用於行動裝置或非 Chrome 瀏覽器**：目前唯一支援環境是桌面版 Chrome

---

## 延伸閱讀

- [30-new-tools-commands.md](./30-new-tools-commands.md) — Computer Use（Desktop/CLI）research preview
- [42-w26-27-features.md](./42-w26-27-features.md) — v2.1.198 完整變更列表
- [09-secure-deployment.md](./09-secure-deployment.md) — AI Agent 安全部署威脅模型（prompt injection 防禦互補閱讀）

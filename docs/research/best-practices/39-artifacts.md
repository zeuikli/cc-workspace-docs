# Claude Code Artifacts — 工作 Session 轉互動網頁

> **Source:** https://claude.com/blog/artifacts-in-claude-code  
> **Date:** 2026-06-18  
> **Type:** 新功能指南 — Team/Enterprise Beta

---

## 概述

Claude Code Artifacts 讓開發者可將工作 session 轉換為**互動式、可分享的網頁**，整合 codebase 內容、工具執行結果與對話歷史，供團隊成員即時查看。

頁面**隨 Claude Code 變更自動更新**，支援版本歷史與還原。預設私有，僅限組織內認證成員存取。

---

## 核心特性

| 特性 | 說明 |
|------|------|
| **自動更新** | Claude Code 每次變更後頁面即時同步 |
| **版本歷史** | 可回溯任意時間點的快照並還原 |
| **存取控制** | 預設私有；管理員可透過 org-level 開關和角色權限控管 |
| **範圍** | Team / Enterprise Beta（2026-06-18 起） |

---

## 適用場景

### 高價值使用場景

1. **PR Walkthrough** — 將 PR 相關的 Claude Code session 分享給 reviewer，提供完整上下文
2. **事故調查（Incident Investigation）** — 將除錯過程、日誌分析、找到的 root cause 整合成可共享文件
3. **安全稽核（Security Audit）** — 掃描結果、漏洞清單、修補計劃一頁呈現
4. **基礎架構地圖（Infrastructure Map）** — 自動生成並持續更新的架構概覽
5. **前端 UX 設計** — 互動式設計原型，設計師可直接在頁面上提供回饋
6. **週報摘要（Weekly Digest）** — 自動從 git history 生成週度工程進度摘要

---

## 啟用與管理

### 建立 Artifact

```bash
# 在 Claude Code session 中
/artifact create "PR #1234 walkthrough"
```

或在 Claude Code 回應後選擇「Share as Artifact」

### 存取控制設定（管理員）

```json
// organization settings
{
  "artifacts": {
    "enabled": true,
    "defaultVisibility": "organization",  // "private" | "organization"
    "allowedRoles": ["engineer", "manager", "viewer"]
  }
}
```

---

## 與現有工具的比較

| 工具 | 適用場景 | 限制 |
|------|---------|------|
| **Artifacts** | 持續更新的 session 快照、跨角色分享 | Team/Enterprise only |
| **HTML Output** | 一次性可視化輸出 | 不自動更新 |
| **Git Commit** | 代碼變更歷史 | 不含 AI 對話上下文 |
| **PR Description** | 靜態 PR 描述 | 需手動維護 |

---

## 最佳實踐

1. **PR 流程整合**：複雜 PR 建立 Artifact 取代純文字 PR description，reviewer 可看到完整思路
2. **事故後復盤**：Incident 解決後保存 Artifact 作為 postmortem 素材
3. **權限最小化**：預設使用 `organization` 可見性，敏感調查使用 `private`
4. **定期清理**：過時 Artifact 佔用存儲空間，建立清理 Hook（PostToolUse on `ArtifactCreate`）

---

## 延伸閱讀

- [31-html-output-strategy.md](./31-html-output-strategy.md) — HTML 輸出格式策略（互補工具）
- [22-code-review.md](./22-code-review.md) — Code Review 多代理 PR 自動審查

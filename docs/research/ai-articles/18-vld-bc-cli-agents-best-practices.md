---
url: "https://vld-bc.com/blog/cli-agents-part2-claude-code-best-practices"
title: "CLI Agents Part 2: Claude Code Best Practices"
type: article
---

# CLI Agents Part 2: Claude Code Best Practices

**原始 URL**: https://vld-bc.com/blog/cli-agents-part2-claude-code-best-practices

**作者**: Volodymyr Dvernytskyi  
**來源**: 關於 Navision & Dynamics 365 Business Central 的部落格

---

## 核心摘要

Volodymyr Dvernytskyi 提供了關於如何有效配置 Claude Code 的實踐指導，涵蓋配置檔案、上下文管理、代理委派、自訂命令和集成協議。本文強調了結構化配置優於臨時性提示的重要性，以及如何通過 CLAUDE.md、權限模式和上下文管理來建立可靠的 AI 代理工作流。

核心論點：**配置優於對話**。將重複指令和專案規則集中在配置檔案，而不是在每次交互中重述，可顯著提高效率並減少令牌消耗。

### 六大關鍵實踐

1. **CLAUDE.md 配置**
   - 專案特定配置的基礎
   - 包含：構建和測試指令、代碼風格規則、架構邊界、專案慣例
   - 使用「優先 X 而非 Y」的正向措辭，優於「不要做 Z」的負向措辭
   - 支持多層級結構（全局、專案、組件層級）

2. **權限模式**
   - Default（提示確認）
   - Accept Edits（自動批准編輯）
   - Plan（唯讀分析）
   - Don't Ask（預設拒絕，需明確許可）
   - Bypass Permissions（完全存取，限隔離環境）

3. **上下文管理**
   - 「上下文即 AI 代理在單一對話會話中看到和記憶的所有內容」
   - 平衡充分資訊與認知過載
   - 使用 `/compact` 和 `/context` 命令監控令牌消耗
   - 接近上限時開始新對話

4. **Subagents（子代理）**
   - 專門的 Claude 實例處理聚焦子任務
   - 隔離的上下文視窗、權限、工具存取和模型選擇
   - 實例：專用測試運行器、代碼審查者、文件生成器

5. **自訂命令**
   - Markdown 檔案存儲的斜線命令，自動化重複任務
   - 示例：`/al-status` 摘要 Git 變更並生成 PR 描述

6. **MCP 集成**
   - 模型上下文協議連接啟用外部集成
   - 示例：Playwright MCP 用於瀏覽器自動化測試和驗證工作流

---

## 關鍵實踐

### 積極的措辭策略
使用「Prefer X over Y」而非「Never do Z」，讓 AI 更容易理解和遵循偏好。

### 上下文監控檢查清單
- [ ] 確認每次對話的起點上下文大小
- [ ] 定期用 `/context` 診斷實際消耗來源
- [ ] 早期（狀態「健康」時）主動使用 `/compact`
- [ ] 避免在警告出現時才進行壓縮

### AL 語言最佳實踐（Business Central 特定）
- 物件設計和命名慣例
- 性能最佳化策略
- 事務處理和錯誤管理
- 全面測試策略

---

## 關鍵引用與數據

> 「我們的角色作為軟體工程師變得不那麼關注技術細節，更多是提供良好的護欄讓代理完成工作」

> 「配置檔案是 AI 代理的憲法」

**上下文成本示例**：
- CLAUDE.md（100 行）: ~500-800 tokens
- 標準工具載入: ~1000-1500 tokens
- 子代理開銷: ~200-300 tokens（每個）
- 完整對話歷史: 線性增長

**權限模式選擇**：
- 開發環境: Bypass Permissions
- CI/CD: Accept Edits（受限範圍）
- 生產部署: Plan → 手動審批 → 執行

---

## 實踐適用性

此方法論適用於：
- 多人協作的中大型專案
- 需要一致性的重複性任務
- 需要嚴格審查的關鍵系統
- 長期維護的代碼庫

配置驅動的方法確保一致性、可追蹤性和長期可維護性，特別適合在團隊層級應用 Claude Code。

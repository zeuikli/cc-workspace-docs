# 最佳實踐指南

本節整理自 Anthropic 官方文件、社群實踐（Boris Cherny、Thariq Shihipar 等核心貢獻者）及深度研究報告，涵蓋 Claude Code 工程化使用的各個面向。

## 指南目錄

| 主題 | 說明 |
|------|------|
| [工作流程與核心技巧](/resources/best-practices/workflows/) | Explore→Plan→Implement→Commit 四階段、Plan Mode、Session 管理、Boris Cherny 65+ 技巧 |
| [Hooks 設計模式](/resources/best-practices/hooks/) | 25 種 hook 事件完整範例、PreToolUse 防禦、PostToolUse 自動化、SessionStart 初始化 |
| [Permission 細粒度設定](/resources/best-practices/permissions/) | 五種 Permission Mode、Wildcard 語法、Compound 指令、Symlink 規則 |
| [MCP Server 與 Skills](/resources/best-practices/mcp-skills/) | 三種 transport 安裝、OAuth 認證、Scope 管理、Skills 設計原則 |
| [Prompt Caching 工程](/resources/best-practices/prompt-caching/) | 前綴匹配原理、六大教訓（Thariq）、Cache Hit Rate 監控、失效條件 |

## 核心論點

來自 2026-05-16 深度研究報告的結論：

> **Context Engineering（在執行時組裝正確資訊並正確排序）是 Claude Code 真正的工程護城河，遠比 Prompt 撰寫技巧更重要。**

這五個面向都是 Context Engineering 的具體實踐：

- **Hooks**：在正確的時機注入正確的行為（確定性控制）
- **Permissions**：定義清晰邊界讓 agent 自主工作（減少核准疲勞）
- **MCP/Skills**：在 context 中提供正確的工具接口（能力延伸）
- **Prompt Caching**：讓靜態 context 高效復用（成本工程）
- **Workflows**：確保每次任務都有完整的驗證反饋迴路（可靠性）

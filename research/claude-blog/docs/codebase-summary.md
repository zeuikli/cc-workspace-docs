# Claude Blog 知識庫速查

本文件為 `research/claude-blog/` 的快速導航與維護指南。

---

## 收錄範圍

51 篇 claude.com/blog 文章（去重後），涵蓋 2025-11-13 ~ 2026-04-22，涉及 Claude Code、AI Agents、Enterprise AI 三大產品線及官方公告。

---

## 分類索引

| 分類 | 篇數 | 涵蓋期間 | 主要議題 |
|------|------|---------|---------|
| [Claude Code](../claude-code/index.md) | 15 | 2026-01-29 ~ 2026-04-20 | 開發者工具、Session 管理、Code Review、Routines |
| [Agents](../agents/index.md) | 15 | 2025-11-13 ~ 2026-04-22 | Skills 生態、協調模式、MCP 標準、生產部署 |
| [Enterprise AI](../enterprise-ai/index.md) | 12 | 2025-11-17 ~ 2026-04-08 | 企業案例、1M Context、成本優化、合規工具 |
| [Announcements](../announcements/index.md) | 9 | 2026-02-17 ~ 2026-04-14 | Managed Agents、Advisor Strategy、Cowork Enterprise |

---

## 六大核心主題

1. **Skills 生態系架構** — 知識封裝層，從基礎定位（Nov 2025）到組織部署（Dec 2025–Jan 2026）的系統性推進。

2. **生產 Agent 工程成熟化** — 五種協調模式框架（Generator-Verifier、Orchestrator-Subagent、Agent Teams、Message Bus、Shared State）與 MCP 300M 月下載量的市場驗證。

3. **成本工程三層防線** — Advisor Tool（API 層 -85%）+ Prompt Caching（Context 層 -90%）+ Tool Search（工具層 -85% token）。

4. **Claude Code 開發者 OS** — 從編輯器轉型為完整開發環境，非專業開發者已成為核心市場（黑客松 5 獲獎者中 4 位非工程師）。

5. **Context Engineering 護城河** — 執行時正確組裝與排序 context 成為新的核心競爭力，超越傳統 Prompt Engineering 定位。

6. **企業採用量化數據** — Carta Healthcare（98-99% 準確率）、Harvey（90.2% BigLaw Bench）、eSentire（95% 準確率）等具體案例驗證 ROI。

---

## 關鍵文章速查

### 按分類推薦（各 2 篇）

| 分類 | Top 1 | Top 2 |
|------|-------|-------|
| **Claude Code** | [Code Review](https://claude.com/blog/code-review) | [Session Management & 1M Context](https://claude.com/blog/using-claude-code-session-management-and-1m-context) |
| **Agents** | [Multi-agent Coordination](https://claude.com/blog/multi-agent-coordination-patterns) | [Building agents with MCP](https://claude.com/blog/building-agents-that-reach-production-systems-with-mcp) |
| **Enterprise AI** | [Carta Healthcare](https://claude.com/blog/carta-healthcare-clinical-abstractor) | [1M Context GA](https://claude.com/blog/1m-context-ga) |
| **Announcements** | [Advisor Strategy](https://claude.com/blog/the-advisor-strategy) | [Managed Agents](https://claude.com/blog/claude-managed-agents) |

---

## 文件地圖

| 檔案 | 說明 |
|------|------|
| **README.md** | 導覽首頁、分類列表、最新 5 篇文章 |
| **REPORT.md** | 52 篇文章的分佈統計、主題深度分析、Top 5 推薦、技術限制說明 |
| **docs/synthesis.md** | 跨主題合成分析（6 主題 + 關聯圖 + 長期建議） |
| **docs/timeline.md** | 按月份的完整時間軸（Nov 2025 ~ Apr 2026） |
| **docs/codebase-summary.md** | 本檔案 — 維護者快速導航 |

---

## 維護指南

### 新增文章流程

1. 訪問 [claude.com/blog](https://claude.com/blog) 找新文章
2. 決定文章分類（Claude Code / Agents / Enterprise AI / Announcements）
3. 在對應 `<category>/index.md` 中按**發布日期逆序**插入新條目

### 條目格式

```markdown
## 文章標題

**Date:** YYYY-MM-DD | **URL:** https://claude.com/blog/article-slug

### Summary
一句話摘要。

### Key Points
- 重點 1
- 重點 2
```

### 同步更新

- 修改後檢查 `REPORT.md` 的文章計數是否需要更新
- 若文章跨越多個分類，在主分類 index 中標記交叉引用，並在 README.md 的說明中提及
- 若 synthesis.md 受影響（6 個核心主題有新聞訊），更新該文件的時間線與數據

---

*最後更新：2026-04-23 · 51 篇文章 · 4 分類 · 6 核心主題*

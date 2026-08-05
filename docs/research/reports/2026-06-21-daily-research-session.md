---
date: 2026-06-21
source: DAILY-RESEARCH/2026-06-21.md
topics: [enterprise-mcp-auth-idp-claude-code, agent-scm-concurrent-coding-ncode, aa-briefcase-harness-evaluation-methodology, anthropic-enterprise-mcp-auth-official-launch, fable5-frontier-economics-aa-briefcase-31usd]
type: session-report
---

# Session Report 2026-06-21 — Daily Research

## 執行概要
- **研究主題**：5 個（DAILY-TOPICS/2026-06-21.md 全覆蓋）
- **搜尋查詢**：5 次並行 WebSearch（所有主題同時搜尋）
- **頁面 Fetch**：4 次深度抓取（1 次因 X.com 付費牆失敗，改抓 Noumena Code 官網）
- **來源 URL**：10 個（超過驗證門檻 5 個）

## 本日研究成果摘要

### 最高價值發現（Top 3）

1. **[Critical] EMA 正式穩定：IdP 委派 MCP Auth 是企業 AI 工具化的關鍵基礎設施**
   - Anthropic 2026-06-18 發布 Enterprise-Managed Authorization（EMA）beta
   - 技術核心：ID-JAG（Identity Assertion JWT Authorization Grant）取代逐用戶 OAuth consent
   - 影響：企業員工第一次打開 Claude 即自動繼承 MCP connector 存取，無需 IT 逐一開通
   - 支援：Claude、Claude Code、Cowork、VS Code；Okta（IdP）、7 個 MCP connector

2. **[Critical] AA-Briefcase 揭示長期任務成本結構：頂模型 $31/task，完全達標率僅 3%**
   - 91 任務、4 個多週專案、3D 評分（rubric + 分析品質 + 呈現品質）
   - Fable 5 領先（1587 Elo）但每任務 $31；Opus 4.8 1356 Elo / $10.40/task
   - 企業 ROI 必須改用「cost-per-outcome」計算，而非 token 單價
   - 現有 model-selection-grid 缺此維度，需更新（已識別為演化候選）

3. **[High] Noumena Code：Agent 並行開發的 SCM 範式轉移**
   - 傳統 Git/GitHub 在多 agent 並行工作下出現結構性崩潰（stale branches、merge conflicts、重複環境建置）
   - ncode 解方：per-issue scoped workspace（雲端 + file-level ACL）+ jj + Sapling commit stack
   - 人類保留 review + landing 決定；agent 只負責 draft
   - 架構概念與 cc-workspace 的 worktree + pathspec 隔離策略一致，但更徹底

## 可實作 / 可測試內容

### P0 — 立即可執行（今日，< 1 小時）

**[P0-1] 更新 model-selection-grid：加入 AA-Briefcase per-task 成本維度**
- 目標文件：`.claude/refs/model-selection-grid.md`
- 具體修改：在 Fable 5 / Opus 4.8 對比欄位加入
  ```
  AA-Briefcase: $31/task（Fable 5）vs $10.40/task（Opus 4.8）
  注：長期 knowledge work 成本不可從短任務外推
  ```
- 驗收命令：`grep -qE 'Briefcase|31.*task|per.task' .claude/refs/model-selection-grid.md && echo OK`
- **安全邊界**：`.claude/` 目錄 → 需人工審核確認後執行（DAILY-TOPICS 已標注）

### P1 — 本月優先（各 2-4 小時）

**[P1-1] task-type cost routing 加入 subagent-strategy.md**
- 在「模型選擇 + 能力下限」章節加入 cost-aware 路由原則
- 路由矩陣（基於 AA-Briefcase 數據）：
  - 長期自主任務（>30 min，agentic）→ Fable 5
  - 互動式迭代（user course-correct 每輪）→ Opus 4.8 / Sonnet 4.6
  - 批量分類/提取 → Haiku 4.5
- 驗收條件：`grep -c "per-task\|knowledge work\|cost-per-outcome" .claude/rules/subagent-strategy.md` ≥ 1

**[P1-2] EMA ext-auth spec 研究 + MCP 指引補充**
- 研究 MCP ext-auth repository 的 ID-JAG token flow
- 若 workspace 有 MCP connector 配置指引，加入企業 IdP 場景的設定說明
- 驗收條件：能描述 admin → IdP policy → user 繼承的完整 flow，並有設定範本

### P2 — 觀察中

**[P2-1] ncode SCM 評估（公開存取後）**
- 觀察條件：ncode SCM + ncode platform 正式公開（目前僅 code app 公開）
- 評估面向：與現有 worktree 策略的相容性；file-level ACL 對並行研究任務的效益
- 觀察指標：GitHub star 趨勢、Latent Space newsletter 後續報導

## GAP 狀態更新

| GAP | 研究前狀態 | 研究後狀態 | 行動 |
|-----|-----------|-----------|------|
| enterprise-mcp-auth-architecture | gap（0 篇）| researched（WebFetch 完成架構分析）| P1-2：寫設定指引 |
| agent-scm-parallel-coding | gap（0 篇）| researched（ncode 架構已記錄）| P2-1：待 public access |
| aa-briefcase-long-horizon-evals | gap（0 篇）| researched（完整方法論 + 成本數據）| P0-1：更新 model-grid |
| fable5-per-task-economics | partial（有 Fable 5 評測但無 per-task 成本）| researched（$31/task，ROI 框架完整）| P0-1 + P1-1 |

## 下一次循環優先事項

1. **確認 P0-1**：人工審核並執行 `.claude/refs/model-selection-grid.md` 更新（AA-Briefcase 數據）
2. **追蹤 EMA beta → GA 時程**：Okta 之外的 IdP 支援（Azure AD、Google Workspace）公告
3. **監控 ncode SCM 公開存取**：Noumena Network GitHub 和 Latent Space newsletter

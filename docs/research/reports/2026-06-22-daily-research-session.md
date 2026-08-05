---
date: 2026-06-22
note: DAILY-TOPICS 2026-06-22 缺失，使用 2026-06-21.md 選題
source: DAILY-RESEARCH/2026-06-22.md
topics: [enterprise-mcp-auth-idp-claude-code, anthropic-enterprise-mcp-auth-official-launch, agent-scm-concurrent-coding-ncode, aa-briefcase-harness-evaluation-methodology, fable5-frontier-economics-aa-briefcase-31usd]
type: session-report
---

# Session Report 2026-06-22 — Daily Research

## 執行概要

- **研究主題**：5 個（DAILY-TOPICS/2026-06-21.md 全覆蓋）
- **搜尋查詢**：5 次並行 WebSearch
- **頁面 Fetch**：5 次深度 WebFetch（claude.com/blog、artificialanalysis.ai、code.noumena.com、blog.modelcontextprotocol.io、developersdigest.tech）

## 本日研究成果摘要

### 最高價值發現（Top 3）

1. **[Critical] EMA for MCP — 企業 auth 基礎設施正式落地**
   - Anthropic 於 2026-06-18 發布 Enterprise-Managed Authorization，以 ID-JAG 協議實現零觸式 IdP 委派認證
   - 覆蓋 Claude、Claude Code、Cowork 及 VS Code（Microsoft 同日整合）
   - 消除 context window 內 auth token 暴露風險，印證 「MCP = API auth gateway」設計哲學
   - 影響：企業 Claude Code 部署 auth 架構需更新；EMA 降低企業採用摩擦

2. **[Critical] AA-Briefcase 確立 per-task 成本為選模型核心指標**
   - Fable 5 在長期知識工作任務 $31/task、3% 完整達標率——rate card 2x 差距在 agentic 工作流中被放大至 3-4x
   - GLM-5.2 max 以 Opus 4.8 25% 成本達到相差 90 Elo，成為高量任務最優選擇
   - 800x 跨模型成本差距（Fable 5 vs DeepSeek V4 Flash）說明模型選擇對 FinOps 的決定性影響
   - 影響：model-selection-grid 需立即更新；overnight-research 預設模型應降為 Opus 4.8

3. **[High] 並行代理 SCM 典範轉移 — ncode / jj 生態形成**
   - 傳統 git PR 模型在百代理並行下結構性崩潰，ncode 以 issue-scope + file ACL + jj 草稿層解決
   - 產業信號：jj 生態快速成熟，Sapling（Meta 內部 SCM）概念進入工具化
   - 影響：本 workspace 的 worktree + 單分支策略長期仍適用，但需持續觀察 ncode GA

## 可實作 / 可測試內容

### P0 — 立即可執行（今日或明日，< 2 小時）

**P0-1: model-selection-grid 加入 AA-Briefcase per-task 成本維度**
```
目標檔案：.claude/refs/model-selection-grid.md
修改內容：
  - Fable 5 欄：加入 "AA-Briefcase: #1 Elo ($31/task, 3% full completion)"
  - Opus 4.8 欄：加入 "AA-Briefcase: #2 (~$10.40/task)"
  - 加注：「長期 knowledge work 任務成本需獨立評估，非短任務外推」
驗證命令：grep -qE 'Briefcase|31.*task|per.task' .claude/refs/model-selection-grid.md && echo OK
注意：.claude/ 目錄修改需人工審核確認
```

### P1 — 本月優先（2-8 小時）

**P1-1: overnight-research / autoresearch 預設模型成本護欄**
```
目標：autoresearch 和 overnight-research skill 加入模型選擇邏輯
實作：非首次通過率敏感任務預設 Opus 4.8；Fable 5 需明確 --quality-critical flag
驗收：autoresearch:scenario 預設執行使用 Opus 4.8 且 cost log < $15/run
時間估計：4 小時
```

**P1-2: EMA 企業部署架構記錄**
```
目標：記錄 IdP → EMA → MCP server → Claude Code 拓撲
文件路徑：research/ai-articles/scored/ 或 .claude/refs/mcp-enterprise-auth.md
包含：ID-JAG protocol 流程、token lifecycle、現支援廠商清單（7 MCP servers + Okta）
時間估計：2 小時
```

### P2 — 觀察中

**P2-1: Noumena Code 採用評估**
- 觸發條件：ncode GA + 企業定價公開 + 3 個以上 enterprise case study
- 當前狀態：beta / early access，無定價

**P2-2: AA-Briefcase 方法論引入 workspace 評測**
- 觸發條件：overnight-research 輸出量 > 50 份 + 品質判斷主觀困難
- 評估：rubric（binary）+ pairwise 雙維度 eval 框架

## GAP 狀態更新

| GAP | 研究前狀態 | 研究後狀態 | 行動 |
|-----|-----------|-----------|------|
| enterprise-mcp-auth-architecture | gap (0 篇) | closed | EMA + ID-JAG 完整架構已記錄於 DAILY-RESEARCH |
| agent-scm-parallel-coding | gap (0 篇) | partial | ncode 架構已記錄，待 GA 補充 |
| aa-briefcase-long-horizon-evals | gap (0 篇) | closed | 評測方法論 + 結果數據已完整記錄 |
| fable5-per-task-economics | partial | enriched | per-task 成本數據表 + breakeven 分析 |

## 演化候選狀態

| 演化候選 | 來源選題 | 狀態 | 下一步 |
|---------|---------|------|-------|
| aa-briefcase-model-economics-reality | 2026-06-21 | P0 待執行 | 人工確認後更新 model-selection-grid |

## 下一次循環優先事項

1. 執行 P0-1（model-selection-grid 更新）— 需人工確認，可今日完成
2. 追蹤 ncode beta 進展（預計月底前有 GA 消息）
3. 確認 EMA 是否有其他 IdP（非 Okta）的整合時間表

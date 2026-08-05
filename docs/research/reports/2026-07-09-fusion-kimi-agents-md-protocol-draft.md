## §7. Fusion Protocol（跨 harness 通用）

> 雙角色並行: 主 agent 規劃 + sidekick 機械執行, 切換綁定 compaction 達零 cache 懲罰。

| 角色 | 職責 | 委派預設 |
|------|------|---------|
| Main Agent | 規劃 · 歧義判斷 · 最終審查 · 監控 sidekick | 預設委派, 例外親做 |
| Sidekick Agent | 機械執行 · 測試運行 · 批量掃描 | 回報結論 + 檔案:行號 |

### 切換時機

| 信號 | 動作 | Cache 影響 |
|------|------|-----------|
| compaction 觸發 | 評估升降級 model | 零懲罰（本就失效） |
| 連續失敗 | 升級 sidekick 檔位 | 用 sub-agent spawn |
| 機械模式確認 | 降級至 cost sidekick | 用 sub-agent spawn |
| 非 compaction | 不切主對話, spawn 新 context | 主 cache 不動 |

### Cache 紀律

- 主 session: 穩定前綴不動（AGENTS.md + system prompt）
- Sidekick: 獨立 context, 不污染主對話
- Compaction model: 用 cost 檔執行（省 token, 非推理任務）

**深究** → `research/reports/2026-07-09-fusion-architecture-design-plan.md` §2.5

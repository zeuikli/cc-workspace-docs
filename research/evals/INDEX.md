# Eval Suite Index

| 日期 | Commit | Haiku | Sonnet | Opus | 備註 |
|------|--------|:-----:|:------:|:----:|------|
| 2026-05-25 | 10b5e1e | 40/50 | 42/50 | 49/50 | Baseline（首次執行） |

## 說明

- **Baseline tasks**：`research/evals/baseline/`（5 個 task specs，建立後不輕易修改）
- **Raw results**：`research/evals/runs/baseline-YYYY-MM-DD-<commit>.md`
- **評分方式**：PGE（Generator ≠ Evaluator）— Haiku 結果由 Sonnet 評；Sonnet 結果由 Haiku 評；Opus 結果由 Sonnet 評
- **下次執行**：重大 harness 變更後，或每 4 週定期回歸

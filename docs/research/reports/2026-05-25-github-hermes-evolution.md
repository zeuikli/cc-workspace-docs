---
title: "GitHub Actions + Claude Code CLI 實作 Hermes-style 自主進化"
date: 2026-05-25
type: report
---

# GitHub Actions + Claude Code CLI 實作 Hermes-style 自主進化

**日期**：2026-05-25 | **字元數目標**：≥ 5000
**Branch**：`claude/workspace-architecture-update-M6mXu`
**核心問題**：資料在 GitHub 上，如何實作自主進化與升級機制？

---

## 執行摘要

本報告回答用戶的核心問題：**「我的資料都在 GitHub，如何達成 Hermes Agent 式的自主進化？」**

答案是：**GitHub Actions cron + `claude-code-action@v1` = Hermes 的內建 cron daemon**。每個 GitHub Actions workflow 就是一個 Hermes cron job；`claude-code-action@v1` 的 `prompt` 參數可直接呼叫 `.claude/skills/` 裡的任何 skill；git commit/push 是 Hermes 持久化狀態的等效機制。

本次實作交付三個 GitHub Actions 工作流：`wiki-evolution.yml`（週度 wiki 維護）、`memory-consolidation.yml`（週度記憶整合）、`skill-evolution.yml`（週度 skill 品質監控與演化觸發）。

---

## 1. 背景：為什麼 GitHub = Hermes Daemon 的最佳落地

### 1.1 Hermes Agent 的 5 大支柱中，「Crons」是最重要的自主進化機制

Hermes 的自主進化建立在五大支柱上，其中 Crons（排程）是讓系統「無人值守運行」的核心：

> "Every night at 12am Central time, push changes to this GitHub repo" — 每個 cron 在獨立 session 中執行，不繼承當前對話 context，防止遞迴觸發。

Hermes 的 cron 機制特性：
- **自然語言排程**：用描述而非 cron 語法設定任務
- **獨立 session**：每次 cron 是全新 session，不累積狀態污染
- **Skills 驅動**：cron 觸發後執行 skill，skill 才是業務邏輯的載體
- **時間邊界**：可設定「未來 12 小時內每 10 分鐘」類的有限排程

**GitHub Actions 的等效實現**：

| Hermes Cron 機制 | GitHub Actions 等效 |
|----------------|-------------------|
| 自然語言排程 | `schedule: cron: '...'` |
| 獨立 session | `runs-on: ubuntu-latest`（全新容器）|
| Skills 驅動 | `prompt: "/skill-name"` |
| 時間邊界 | `timeout-minutes` + workflow_dispatch |
| 狀態持久化 | `git add && git commit && git push` |

### 1.2 Garry Tan 的 GBrain：100+ crons/day 的實際規模

Garry Tan 在 meta-meta-prompting 文章中揭示了 GBrain 在他個人 workspace 的實際規模：

- **100,000 頁**知識庫，每天 **100+ cron jobs** 持續更新
- **15 個持續運行的 cron**：meeting ingestion、email triage（每 10 分鐘）、entity propagation
- **Skillify meta-loop**：每次手動執行 → Skillify 萃取模式 → 寫入 skill 檔 → 自動路由

這個規模對個人 workspace 來說過大，但其**設計原則**可以精縮為：
1. 資料自動流入（從 GitHub Actions 的 digest 工作流已在做）
2. 知識自動整合（wiki-lint + 週度整合）
3. 記憶自動整理（memory consolidation）
4. 技能自動演化（skill quality monitoring）

### 1.3 `claude-code-action@v1`：連接 GitHub Actions 與 Skills 的橋樑

官方文件確認的關鍵功能：

```yaml
- uses: anthropics/claude-code-action@v1
  with:
    anthropic_api_key: ${{ secrets.ANTHROPIC_API_KEY }}
    prompt: "/skill-name"  # 直接呼叫 .claude/skills/ 下的任何 skill
    claude_args: |
      --max-turns 30
      --model claude-sonnet-4-6
```

這意味著 cc-workspace 已有的 18 個 skills 都可以通過 GitHub Actions 自動觸發，不需要額外的 agent 框架。

---

## 2. 核心概念分析：三層自主進化架構

### 2.1 對應關係：cc-workspace vs Hermes vs GBrain

```
cc-workspace 自主進化架構
─────────────────────────────────────────────────────
Layer 1: Data Ingestion（資料流入）
  已有：.github/workflows/ai-digest.yml       ← Hermes: data-ingest crons
  已有：.github/workflows/daily-digest.yml    ← Hermes: hourly enrichment
  已有：.github/workflows/ai-news-aggregator  ← Hermes: social monitoring

Layer 2: Knowledge Synthesis（知識合成）    ← 本次新增
  新增：.github/workflows/wiki-evolution.yml  ← GBrain: cron-driven enrichment
       → 每週執行 /autoresearch:wiki lint
       → 執行 scripts/wiki-lint.sh
       → commit 報告

Layer 3: Self-Evolution（自主進化）         ← 本次新增
  新增：.github/workflows/memory-consolidation.yml ← Hermes: memory consolidation
       → 週度 MEMORY.md 整合（≥ 100 行觸發）
  新增：.github/workflows/skill-evolution.yml ← Hermes: skill refinement
       → 掃描 METADATA.json quality metrics
       → 低品質 skill 觸發 /skill-evolution
─────────────────────────────────────────────────────
```

### 2.2 DAEMON-DESIGN.md → GitHub Actions 的實現路徑

`memory/DAEMON-DESIGN.md` 的 KAIROS tick 機制（15 分鐘一次）在 GitHub Actions 環境下的最小可行實作：

**KAIROS vs GitHub Actions 映射**：

| DAEMON-DESIGN 設計 | GitHub Actions 實作 |
|-------------------|-------------------|
| 15 分鐘 tick | `schedule: cron: '0 * * * *'`（最短 1 小時）|
| Memory.md > 150 行觸發 | 工作流 step 中 `wc -l memory/MEMORY.md` 判斷 |
| ≤ 15 秒 blocking budget | `timeout-minutes: 10` |
| autoDream 四階段 | Claude Code Action `prompt: "/memory-compactor"` |
| daemon-log.jsonl | GitHub Actions run log + `git log` |

**限制**：GitHub Actions 最短間隔為 1 小時（`schedule` 最短 cron 是每 5 分鐘，但 GitHub 對免費帳戶有限制）。DAEMON-DESIGN 的 15 分鐘 tick 在 GitHub Actions 環境下需調整為 daily/weekly 觸發，或用 `workflow_dispatch` 手動觸發。

### 2.3 Hermes GEPA 自演化 → cc-workspace 簡化實作

Hermes 的完整 GEPA（Genetic-Pareto Prompt Evolution）需要：
- 執行跡（execution traces）分析
- 候選變體生成
- 多目標評估（constraint gates）
- Human PR review

對 cc-workspace 的**簡化等效實作**：

```
Skill Quality Monitoring（替代 GEPA 監控層）：
  1. 掃描所有 METADATA.json 的 usage_count / quality_score
  2. 識別 quality_score < 7 或 usage_count > 10 且 refinement_count = 0 的 skill
  3. 觸發 /skill-evolution 對這些 skill 執行品質審查
  4. 提交改善後的 SKILL.md

自動觸發條件（Hermes 的 failure rate threshold 等效）：
  - quality_score < 7.0
  - usage_count > 10 AND refinement_count = 0（高頻使用但從未優化）
  - last_reviewed > 30 天前
```

---

## 3. 實作方案：三個 GitHub Actions 工作流

### 3.1 wiki-evolution.yml：週度 Wiki 維護

**目的**：自動執行 wiki-lint，找出過時/孤立頁面，生成報告，commit 回 repo。

**觸發**：每週一 09:07 UTC+8（= 01:07 UTC），避開 cron 峰值。

**執行步驟**：
1. Checkout → Setup Python → Run `scripts/wiki-lint.sh`
2. 用 `claude-code-action@v1` + `prompt: "/autoresearch:wiki"` 執行 lint 分析
3. Commit `research/career-wiki/lint-report.md` 和 `LOG.md` 更新

### 3.2 memory-consolidation.yml：週度記憶整合

**目的**：實作 DAEMON-DESIGN.md 的 autoDream 概念，自動整理 MEMORY.md。

**觸發條件**：
- 每週日 03:00 UTC（Taiwan 時間 11:00）
- 或當 MEMORY.md > 150 行時（通過 `workflow_dispatch` 手動觸發）

**執行**：
1. 檢查 `memory/MEMORY.md` 行數
2. 若 ≥ 100 行 → 觸發 Claude Code Action `prompt: "/memory-compactor"`
3. Commit 整合結果

### 3.3 skill-evolution.yml：週度 Skill 品質監控

**目的**：掃描 METADATA.json telemetry，識別需要進化的 skill，觸發 `/skill-evolution`。

**觸發**：每週三 02:03 UTC（Taiwan 時間 10:03），`workflow_dispatch` 手動觸發。

---

## 4. 最佳實踐與實作模式

### 4.1 GitHub Actions cron 的 7 個最佳實踐

1. **錯開分鐘**：用 `:03`、`:07`、`:13` 等奇數分鐘，避開 GitHub 免費 runner 峰值
2. **Stagger 工作流**：三個 evolution 工作流分別在週一/三/日，避免並發
3. **`concurrency: cancel-in-progress: false`**：防止相同工作流因手動觸發互相取消
4. **`timeout-minutes`**：設定合理超時，防止 Claude 進入無限 loop
5. **`continue-on-error: true`**：wiki-lint 等步驟失敗不應阻塞整個 workflow
6. **`permissions: contents: write`**：允許 workflow 提交回 repo（必要）
7. **`workflow_dispatch`**：所有排程工作流都加入手動觸發入口，方便測試

### 4.2 Claude Code Action 的 `--allowedTools` 安全設計

自主 workflow 中，Claude 應只能使用最小必要工具集：

```yaml
claude_args: |
  --max-turns 20
  --model claude-sonnet-4-6
  --allowedTools "Read,Grep,Glob,Bash(git *),Bash(wc *),Bash(find *),Write,Edit"
```

這防止 Claude 在無人值守模式下執行危險操作（rm、curl | bash 等）。

### 4.3 Secrets 設置（一次性）

GitHub Actions 的自主進化只需要一個 Secret：

```
Repository Settings → Secrets → Actions
新增：ANTHROPIC_API_KEY = <你的 Anthropic API key>
```

所有三個 workflow 都使用相同的 `ANTHROPIC_API_KEY`。

### 4.4 CLAUDE.md 在 Actions 中的作用

`claude-code-action@v1` 自動讀取 repository 根目錄的 `CLAUDE.md`（如果存在）。cc-workspace 的 `CLAUDE.md` 定義了：
- 工作流程（git add → commit → push）
- 語言規則（繁體中文）
- 品質標準（healthcheck.sh 驗證）

這意味著 GitHub Actions 中的 Claude 自動繼承 workspace 的所有規則，**不需要額外配置 `--append-system-prompt`**。

---

## 5. 常見陷阱與反模式

### 反模式 1：在 Action 中用 `bypassPermissions`

GitHub Actions runner 是全新環境，settings.json 不會存在。不要在工作流中設定 bypassPermissions，改用 `--allowedTools` 明確限制工具範圍。

### 反模式 2：cron 設定 `*/5 * * * *`（每 5 分鐘）

GitHub 文件警告：`schedule` 事件在「過載的高峰時段可能被延遲或跳過」。對免費 plan，每 5 分鐘的 cron 實際執行間隔可能是 15–60 分鐘。設計上不應依賴高頻 cron 的精確性。

### 反模式 3：Claude 直接 push 到 main

設定 `permissions: contents: write` 讓 Claude 的工作流可以寫入 repo，但應限制在非保護的 branch，或設定 branch protection rules 要求 PR 審查。

### 反模式 4：忘記 `actions/checkout@v4`

`claude-code-action@v1` 需要 repo 已 checkout 才能讀取 CLAUDE.md 和 `.claude/skills/`。一定要在 Action 步驟前加 `- uses: actions/checkout@v4`。

### 反模式 5：設定過長的 `--max-turns`

自主 workflow 中，`--max-turns` 應設為任務預估所需的 2 倍（例如 wiki-lint 預估 10 turns → 設 20）。過高的 max-turns 導致 API 費用不可控。

---

## 6. 前沿趨勢與預測

### 6.1 Claude Code Routines（2026 年新功能）

Anthropic 在 2026-04-14 開放 Claude Code Routines 的 research preview。Routines 是比 GitHub Actions 更直接的自主進化機制：

- **持久跨 session**：不像 GitHub Actions 每次是全新容器
- **三種觸發方式**：固定排程、API 呼叫、GitHub 事件
- **本地執行**：直接在 Claude Code 內部，不需要 CI/CD 基礎設施

**cc-workspace 的遷移路徑**：
1. 現在：GitHub Actions → 穩定、可審計、不依賴本地機器
2. 未來：當 Routines GA 後，將 `wiki-evolution` 和 `memory-consolidation` 遷移至 Routines（更低延遲、更少配置）
3. GitHub Actions 保留用於：資料抓取類（需要 secrets 管理的 external API）

### 6.2 Skills as Self-Improving Artifacts

Hermes GEPA 的開源意味著 skill 的自動優化即將成為標準基礎設施。cc-workspace 的 METADATA.json telemetry 欄位（本次更新加入）是接入 GEPA 類優化器的數據接口：

```json
{
  "quality_score": null,     // GEPA 輸入：當前品質分
  "usage_count": 0,          // GEPA 輸入：使用頻率
  "refinement_count": 0,     // GEPA 輸入：已優化次數
  "evolution_stage": "draft" // GEPA 輸入：演化階段
}
```

當 GEPA 等工具成熟後，只需接入 METADATA.json 即可開始自動優化。

---

## 7. 可立即實作的行動建議

1. **設定 `ANTHROPIC_API_KEY` Secret**（5 分鐘）：Repository Settings → Secrets → Actions → `ANTHROPIC_API_KEY`
2. **啟用三個工作流**：本次提交的三個 yml 文件推送後即生效（需要上述 Secret）
3. **手動觸發測試**：每個工作流都有 `workflow_dispatch`，推送後在 GitHub Actions 頁面點「Run workflow」驗證
4. **設定 MEMORY.md 100 行觸發**：當 MEMORY.md 接近 100 行時，手動觸發 `memory-consolidation.yml`
5. **觀察第一次 wiki-lint 自動執行**：週一 09:07 UTC+8 會自動跑一次，結果 commit 到 `research/career-wiki/lint-report.md`

---

## 附錄：來源評分與索引

| 來源 | 影響力 | 原創性 | 可操作性 | 可信度 | 時效性 | 加權分 |
|------|--------|--------|---------|--------|--------|--------|
| Claude Code GitHub Actions 官方文件 | A | B | A | A | A | 9.5/10 |
| startdebugging.net — 排程教程 | B | B | A | B | A | 8.0/10 |
| Hermes Self-Evolution (NousResearch) | A | A | B | A | A | 9.0/10 |
| MindStudio — Hermes 5 Pillars | B | B | B | B | A | 7.5/10 |
| Garry Tan GBrain tweet (本地) | A | A | A | B | A | 8.0/10 |

---

*生成工具：overnight-research pipeline / Branch：claude/workspace-architecture-update-M6mXu*

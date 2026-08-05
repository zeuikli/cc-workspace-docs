# 盤點：記憶機制 / research 慣例 / 模型版本字串

## 1. 記憶機制健康度

| 檔案 | 行數 | Byte | 門檻 | 狀態 |
|---|---|---|---|---|
| memory/MEMORY.md | 283 行 | 21,023B | 200 行 / 25KB | **超 200 行門檻**（283>200）、byte 未超（21KB<25KB）——應排 memory-compactor |
| memory/LESSONS.md | 87 行 | 9,973B | 獨立不壓縮（AGENTS.md L39 確認） | 健康；系統層 15 條、過程層~22 條、研究層~15 條，未見逐字重複 lesson |

- MEMORY.md 最舊未壓縮 session：`memory/MEMORY.md:5-15`（架構決策/待辦區塊，無日期戳，視為常駐非 session log）；有日期的最舊 session block 為 `2026-06-28`（`memory/MEMORY.md:17-21`，pr-guard GOTCHAS 統一化）。上次 compact 記錄於 `memory/MEMORY.md:105`（2026-07-02 317→99 行），之後又累積回 283 行（8 個新 session block，`memory/MEMORY.md:109-284`）。
- PLAYBOOK 類檔案：`memory/PLAYBOOK.md`、`playbooks/finops-playbook.md`、`.claude/skills/media-transcribe/references/youtube-429-PLAYBOOK.md`（3 個，未讀內容，僅路徑確認存在）。
- `claude-progress.json`：**不存在於工作目錄**（`ls` exit 1）。依 LESSONS.md:84（2026-07-02 lesson）與 MEMORY.md:160(round2 記錄) 可知此檔案已知 gitignored、雲端 session 間會遺失——本次盤點時點亦驗證此行為（檔案缺席，非讀取錯誤）。

## 2. evolution/ 目錄

用途：telemetry/成本追蹤自動生成層（非人工維護）。共 6 個檔案，1.6M 總量。

Top 5 大檔（`du -ah evolution/`）：
1. `evolution/cost-log.jsonl` — 800K（append-only 成本紀錄）
2. `evolution/usage-report.json` — 424K
3. `evolution/task-log.jsonl` — 224K
4. `evolution/.desktop-usage-seen.txt` — 216K（去重游標檔）
5. `evolution/INDEX.md` — 4.0K（唯一人工可讀說明檔，`.gitkeep` 0B 為第 6 個檔）

膨脹判斷：cost-log.jsonl/usage-report.json/task-log.jsonl 三個 append-only 檔佔 1.4M（88%），為預期自動增長型態非異常膨脹；無 30 天輪替可見（README/RULES 曾提及 30 天滾動窗但此為 portal usage，非本目錄檔案本身輪替）。

## 3. research/ 報告慣例

- **目錄**：一般深度研究報告 → `research/reports/`（flat，無子目錄分類，靠 `INDEX.md` 表格分 Topic）。
- **檔名慣例**：`YYYY-MM-DD-<topic-slug>.md`（kebab-case，含日期前綴）。若同日多報告需區分類型，慣例是加類型字尾，如 `2026-07-01-daily-research-session.md` vs `skill-evolution-2026-07-01.md`（後者 topic-first，非固定日期前綴，屬例外）。
- **實際近 3 篇（`ls -t`）**：
  1. `research/reports/2026-07-03-new-domain-active-inference-machine-unlearning.md`
  2. `research/reports/skill-evolution-2026-07-01.md`
  3. `research/reports/2026-07-02-daily-research-session.md`
- **Front-matter 格式**（取自報告 1 實例，`research/reports/2026-07-03-new-domain-active-inference-machine-unlearning.md:1-10`）：
  ```yaml
  ---
  date: "2026-07-03"
  type: new-domain-report        # 依報告性質變（如 harness-audit-report）
  source_routine: routine-e      # 若非 routine 自動產出可省略
  domains: [...]
  grounded_sources: [...]        # arXiv ID 或 URL 清單
  archived_items: 3
  dedup_verified: true
  ---
  ```
- **Harness 稽核類命名前例**（`research/reports/INDEX.md` Harness Engineering 表）：`2026-06-18-harness-derivation-deep-research.md`、`2026-06-18-harness-implementation-roi-eval.md`、`2026-05-31-harness-engineering-deep-research.md`。若要新增「一篇新的 harness 稽核報告」，**建議路徑**：`research/reports/2026-07-03-harness-audit-<主題slug>.md`（或延用今日 PR #806/#807 稽核脈絡：`2026-07-03-fable5-harness-audit-<subtopic>.md`）。
- **Index 更新方式**：手動編輯 `research/reports/INDEX.md`——在對應 Topic 區塊（如「## Harness Engineering」，`INDEX.md:44-51`）新增一列 `| 日期 | `連結` | 核心主題 |`；若屬全新 Topic 需同時在頂部「Topic 索引」表（`INDEX.md:26-36`）加錨點列。**無自動化 index 生成腳本**（未見於 grep，屬人工/agent 手動維護）。

## 4. 模型版本字串普查

Pattern 命中總數（排除 .git/node_modules/evolution，含 research/ai-news 等資料層）：**1393** 處，分布極度集中於 `research/ai-news/`（newsletter 原文轉述，屬純資料歸檔非行為配置）與 `research/papers/`、`research/best-practices/` 文件敘述。以下分三類列出**行為相關**命中（完整 1393 筆清單過長，未逐行列出；如需可重跑 grep 指令見下）：

### (a) 刻意 pin（settings）
- `.claude/settings.json:4` → `"model": "claude-sonnet-4-6"`（**唯一** settings 硬 pin；MEMORY.md:263 確認現況="待使用者決策"、與使用者層 `/model` default 已切 `claude-fable-5` 並存，見 `harness-model-fit.json:152`）

### (b) 文件敘述（不影響行為，僅記錄/參考）
- `research/papers/INDEX.md:357-365` → system card 條目清單（fable-5/opus-4-8/sonnet-4-6/opus-4-5/haiku-4-5/sonnet-4-5/opus-4-1 等，純索引）
- `research/best-practices/07-advisor-tool-best-practices.md:26-29,43,50,129,223` → advisor 模式範例程式碼（教學性質，非可執行 skill 指令）
- `docs/reference/advisor-strategy.md:83,89,107,125,232,268` → advisor 策略文件範例
- `harness-model-fit.json` 全檔（19 處）→ HMF drift 追蹤 log，記錄性質非配置本身（但 `model_version` 欄位理論上是 SSoT 比對基準，見下方 (c) 補充說明）
- `scripts/pricing.py`（24 處）→ 定價表資料，供成本估算查表，非模型選擇決策

### (c) 會影響行為的硬編碼
- **`.claude/skills/sia/REFERENCE.md:32,44-46,66-67`** → sia CLI 預設值文件化：`--task_model` 預設 `claude-haiku-4-5`；claude backend 捷徑名對照表（`haiku→claude-haiku-4-5`／`sonnet→claude-sonnet-4-6`／`opus→claude-opus-4-8`）。此檔為 SKILL 的 REFERENCE 文件，**非 SKILL.md 本體**（`.claude/skills/*/SKILL.md` 及 `.claude/hooks/*.sh` 對此 pattern **零命中**）；若使用者依此文件手動下 `sia` CLI 參數則會影響行為，但非 hook/frontmatter 級強制。標註「2026-06-05 快照，新世代以 `sia --help` 為準」（REFERENCE.md:48），已有過期免責聲明。
- `.claude/agents/*.md` frontmatter `model:` 欄位（13 個 agent）**均為 alias**（`haiku`/`sonnet`/`opus`），**不含**完整版本字串（如 `claude-sonnet-4-6`），故不落在此次 grep pattern 命中範圍——即 agent 委派層無寫死版本字串問題。
- `harness-model-fit.json:4` `model_version: "claude-sonnet-4-6"` 為 HMF drift 比對 SSoT，理論上「影響」稽核判斷（drift=true/false），但非執行期配置。

### 結論
- **無任何 hook（`.claude/hooks/`）或 SKILL.md 本體含硬編碼模型版本字串**——委派/路由層乾淨，全走 alias。
- **實際唯一硬 pin** = `.claude/settings.json:4`（`claude-sonnet-4-6`），且 MEMORY.md 已記錄此為待決事項（使用者 `/model` 已切 fable-5，settings pin 未同步）。
- 其餘 1393 筆中 >95% 為 research/ 資料層（新聞歸檔、論文索引、定價表），屬正常知識庫內容，非配置漂移風險。

### 重現指令
```bash
grep -rn -E "claude-sonnet-4|claude-opus-4|claude-haiku|claude-fable|sonnet-4\.6|opus-4\.8|opus 4\.1|sonnet 4\.5" \
  --include="*.md" --include="*.json" --include="*.sh" --include="*.py" --include="*.yml" --include="*.yaml" \
  --exclude-dir=.git --exclude-dir=node_modules --exclude-dir=evolution .
```

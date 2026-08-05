---
date: 2026-07-19
mode: sia-lite
proposals: 1
routine: G
spec_sha: f8044b717378478122cead2b9d2e99ad248a33ea
weaknesses_identified: 1
---

# Routine G：SIA 週改進迴圈 — 2026-07-19

`[Phase0] mode=sia-lite｜python=3.11.15｜sia-venv=無`

無持久 `~/.sia-venv/bin/sia`（cloud session 預期常態，非降級）。以下依 SIA 三角色紀律手動執行一輪：Meta＝界定本次待評 metric 範圍、Target＝生成提案草稿、Feedback＝對抗自審。

## OBSERVE — 過去 7 天分數表

逐日重跑 `evaluate.py`（確定性、零 LLM 判斷）：

| Routine | Date | missing_artifact | overall | pass | metrics<0.5 |
|---|---|---|---|---|---|
| A | 2026-07-13 | False | 1.0 | True | （無） |
| A | 2026-07-14 | False | 0.8571 | True | m6_index_updated=0.0 |
| A | 2026-07-15 | False | 0.881 | True | m3_gap_grep_grounded=0.1667 |
| A | 2026-07-16 | False | 1.0 | True | （無） |
| A | 2026-07-17 | False | 1.0 | True | （無） |
| A | 2026-07-18 | False | 1.0 | True | （無） |
| A | 2026-07-19 | False | 1.0 | True | （無） |
| C | 2026-07-13 | False | 1.0 | True | （無） |
| C | 2026-07-14 | False | 0.9 | True | m6_arxiv_dedup=0.0 |
| C | 2026-07-15 | False | 1.0 | True | （無） |
| C | 2026-07-16 | False | 1.0 | True | （無） |
| C | 2026-07-17 | False | 1.0 | True | （無） |
| C | 2026-07-18 | False | 1.0 | True | （無） |
| C | 2026-07-19 | False | 1.0 | True | （無） |
| F | 2026-07-13 | False | 1.0 | True | （無） |
| F | 2026-07-14 | **True** | 0.0 | False | （無產出，未算 metrics） |
| F | 2026-07-15 | False | 1.0 | True | （無） |
| F | 2026-07-16 | False | 1.0 | True | （無） |
| F | 2026-07-17 | False | 1.0 | True | （無） |
| F | 2026-07-18 | False | 1.0 | True | （無） |
| F | 2026-07-19 | False | 1.0 | True | （無） |
| D | 最近一次 (gen_7, 07-16 產出) | — | 1.0 | True | （無） |

**判讀**：無任何 metric 出現連續 ≥3 天 <0.5（門檻），故 A/C/F/D 四個 Routine 本週**無系統性弱點**——07-14 A 的 `m6_index_updated=0`、C 的 `m6_arxiv_dedup=0`、F 的 `missing_artifact=True` 集中同一天，疑似當日環境性事故（單日、跨 Routine 同步異常），但樣本 <3 天，依 IDENTIFY 規則不提案，僅記錄觀察。

**維護件週檢**：
- `check-routine-fingerprint.sh`：A/C/F OK；**G DRIFT**（產出記 `4ad7078...` ≠ 現行 `f8044b7...`——本次即是 Routine G 改版後首次以新規格執行，RECORD 階段寫入 heartbeat 後即解除）。
- `compact-inbox.py --dry-run`：no-op（無達齡 ✓routed 條目）。
- `enrichment-scan.py`：偵測到懸空引用 2 筆（`memory/MEMORY.md:476`→`DAILY-TOPICS/INDEX.md`、`memory/MEMORY.md:481`→`CLAUDE.md/AGENTS.md`）——已轉錄 EVOLUTION-QUEUE（見下）。
- `usage-pacer.py --self-test`：PASS（九情境全綠）。
- `healthcheck.sh`：PASS 228 / WARN 3（MCP 設定不存在、bm25 索引落後 SKILL.md）/ FAIL 0；UPS 三斷言（fusion 正例/負例、AUTO 行存在）全 PASS，非本週弱點。
- 路由連動週檢（multi-mode §1d 撤退條款）：`evolution/cost-log.jsonl`（402 筆）無 pace/water-level downgrade 欄位可供比對——**無資料可判**，非「檢查通過」，列 Unknowns。
- L4 fixtures `skill-autotrigger`：本週無 `skill-evolution:apply` 觸及 fusion/multi-mode-skill/output-compress 三 SKILL，條件不成立，跳過。

**壓縮遙測彙總**（`scripts/compress-metrics.py`，SSoT，2026-07-17 起）：

7 天窗：27 筆，零筆日 0/7（執行率檢查通過，非「零資料判健康」誤讀）。

28 天窗（`--window 28 --json`）節錄：

| combo | n | pass_rate | 判讀 |
|---|---|---|---|
| lite×routine-f | 9 | 0.444 | **V1 觸發**（<0.90，n 足夠）|
| lite×routine-c | 6 | 0.833 | V1 觸發但 n 偏小，見下 |
| full×subagent-prompt | 11 | 0.727 | V1 觸發，**但 11 筆全數落在 2026-07-11（修復前）**，非本週活躍問題（見 IDENTIFY） |
| lite×routine-a | 5 | 1.0 | 健康 |
| lite×report | 3 | 1.0 | 健康 |

zero_days（28d）=19/28（<20，未達 V3 記錄門檻）；V4（interactive_n=12 vs routine_n=4）為既有 advisory 分層失效累積證據，非本週新增判讀。

## IDENTIFY — 根因歸維

| Routine/Metric | 現象 | 根因層 | 證據 | 提案？ |
|---|---|---|---|---|
| A/m6_index_updated、C/m6_arxiv_dedup、F/missing_artifact 同於 07-14 | 三 Routine 同日異常 | (e) 單日環境事故（疑似） | 三者集中同一天、其餘 6 天皆健康；樣本 <3 天 | ❌ 不提案（樣本不足） |
| output-compress full×subagent-prompt pass_rate 0.727 | 28d 窗口內 V1 觸發 | 非現行弱點——已於 2026-07-17 修復（EVOLUTION-QUEUE `output-compress-negation-counts-first-pass-order`，SKILL.md §4 加 Negation-first 條款） | `evolution/compress-log.jsonl` 該 combo 11 筆全數 ts=2026-07-11（修復前）；07-12 起該確切 context 名稱已無新筆（後續改用 `subagent-prompt-sonnet`/`-opus` 變體，各僅 n=2，樣本不足另議） | ❌ 不提案（陳舊窗口污染，非活躍問題） |
| output-compress **lite×routine-f / lite×routine-c** missing_keys | lite×routine-f pass_rate=0.444（9筆，5 fail）；lite×routine-c pass_rate=0.833（6筆，1 fail）。**兩者失敗筆 100% 落在同兩類**：`negation_counts`（4 筆：07-15/16/19×routine-f、07-12×routine-c）與 `number`（3 筆：07-12×routine-f ×2、07-12×routine-c ×1） | (a) SKILL 指示與實作不符 | `evolution/compress-log.jsonl` 逐筆 `missing_keys` 欄位直引；**07-19（即今日、在 07-17 修復條款上線後 2 天）lite×routine-f 仍再犯 negation_counts**，顯示上週套用的 §4 Negation-first 條款未確實傳導至 `lite` 層 AUTO 流程（`.claude/skills/output-compress/SKILL.md` §2 表格對 `lite` 之定義為「只刪填充詞/客套語/開場白；保留完整句與冠詞」，理論上不該觸及句內 negation/number，但實測持續遺失） | ✅ 提案1 |

## PROPOSE — 改進提案（1 條，mode=sia-lite 手動 Feedback 紀律）

### 提案 1：output-compress-lite-tier-negation-first-not-propagated

- **目標文件**：`.claude/skills/output-compress/SKILL.md`（僅提案，待人工審核，需走 `skill-evolution:apply output-compress` 執行，不直改 SKILL）
- **具體修改方向**：`lite` 層（§2 檔位矩陣）定義為僅刪填充詞、應保留完整句與冠詞，但 `evolution/compress-log.jsonl` 顯示其 `routine-f`/`routine-c` context 的 AUTO 流程持續遺失 `negation_counts`/`number` 白名單類別，且 2026-07-17 為 `full` 層套用的 Negation-first 條款（§4）修復後，`lite×routine-f` 於 07-19 仍再犯同型失敗——建議在 §2 lite 列或 AUTO flow 段明確加註「lite 層 worker brief 仍須完整含入 §4 白名單/Negation-first 全文，不得因『lite＝輕量』而省略保留規則」，確保條款對三檔位一致生效而非僅 full 層。
- **可機械驗證的成功條件**：套用後 7 天窗口 `python3 scripts/compress-metrics.py --window 7 --json` 之 `combos["lite×routine-f"].pass_rate ≥ 0.90`（需 n≥3 才判定；n<3 則延長觀察窗至湊滿樣本再複查，不可用單筆通過宣告修復）。
- **反 eval-hack 聲明**：`negation_counts`/`number` 仍是 `fidelity-check.py` 既定必留白名單類別，本提案不放寬或移除任何檢查項，只是確保既有規則在 lite 層執行時不被遺漏——pass_rate 上升代表真實補齊資訊完整度，非降低驗證嚴格度。

（提案數 = 1，未超過每週 ≤2 上限；未強行湊滿 2 條——07-14 三 Routine 同日異常、路由連動查無資料兩項皆因證據不足誠實不提案。）

## APPLY — enrichment-scan 轉錄

`enrichment-scan.py` 唯讀掃描 `memory/MEMORY.md` 本週發現懸空引用 2 筆（與 2026-07-12/07-17 那批已 applied 的引用為不同行號，屬新出現），已轉錄 `research/EVOLUTION-QUEUE.md`（status: proposed，本 Routine 僅轉錄不合併/刪除，D3 顯式門控）：
1. `enrichment-scan-dangling-refs-20260719`（`memory/MEMORY.md:476`→`DAILY-TOPICS/INDEX.md`、`:481`→`CLAUDE.md/AGENTS.md`）

## Unknowns

- [KU] 07-14 A/C/F 三 Routine 同日出現異常（m6_index_updated=0、m6_arxiv_dedup=0、missing_artifact=True）疑似當日共用上游或環境事故，但本週僅 1 天樣本、未達 3 天門檻無法歸因 → 處置：留待下週 Routine G 觀察是否重現，若同型態再現 ≥2 次則改列系統性弱點提案。
- [UK] 路由連動週檢（multi-mode §1d 撤退條款 pace-downgrade re-handoff 率比對）设计所需欄位在現行 `evolution/cost-log.jsonl` schema 中不存在（僅有 timestamp/model/tokens/cost 等，無 pace/water-level 欄位），本檢查目前無法執行、非「檢查通過」→ 處置：記錄為量測缺口，若該欄位確實需要則應由另一提案（多屬 multi-mode-skill 職權，非本 Routine 越界）補齊 logging schema。
- [UU] 本次只驗證了 A/C/F/D 四個 Routine 與 output-compress 遙測，未涵蓋 Routine B/E 近期分數走勢是否也有類似結構性偏誤 → 處置：留給下次 Routine G 或人工於審核提案時一併檢視。

`[Checkpoint] Routine G 2026-07-19：mode=sia-lite｜分數表=4Routine×7天（D=最近一次）｜系統性弱點=1（1提案）｜提案=1（含 1 筆 enrichment-scan 轉錄）｜PR 待開`

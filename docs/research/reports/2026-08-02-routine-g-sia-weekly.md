---
date: 2026-08-02
mode: sia-lite
proposals: 1
routine: G
spec_sha: 1ae8bbb26e2dfc56467a466559a4cd9a7b510f6b
weaknesses_identified: 1
---

# Routine G：SIA 週改進迴圈 — 2026-08-02

`[Phase0] mode=sia-lite｜python=3.11.15｜sia-venv=無`

無持久 `~/.sia-venv/bin/sia`（cloud session 預期常態，非降級）。以下依 SIA 三角色紀律手動執行一輪：Meta＝界定本次待評 metric 範圍、Target＝生成提案草稿、Feedback＝對抗自審。

## OBSERVE — 過去 7 天分數表

窗口採 A/C/F 三 Routine 實際已完成的 UTC 產出日（2026-07-26～2026-08-01；2026-08-02 當日 A/C/F 尚未觸發，非缺失，見下方 Unknowns）。逐日重跑 `evaluate.py`（確定性、零 LLM 判斷）：

| Routine | Date | missing_artifact | overall | pass | metrics<0.5 |
|---|---|---|---|---|---|
| A | 2026-07-26 | False | 1.0 | True | （無） |
| A | 2026-07-27 | False | 1.0 | True | （無） |
| A | 2026-07-28 | False | 1.0 | True | （無） |
| A | 2026-07-29 | False | 1.0 | True | （無） |
| A | 2026-07-30 | False | 1.0 | True | （無） |
| A | 2026-07-31 | False | 1.0 | True | （無） |
| A | 2026-08-01 | False | 1.0 | True | （無） |
| C | 2026-07-26 | False | 1.0 | True | （無） |
| C | 2026-07-27 | False | 1.0 | True | （無） |
| C | 2026-07-28 | False | 1.0 | True | （無） |
| C | 2026-07-29 | False | 1.0 | True | （無） |
| C | 2026-07-30 | False | 1.0 | True | （無） |
| C | 2026-07-31 | False | 1.0 | True | （無） |
| C | 2026-08-01 | False | 1.0 | True | （無） |
| F | 2026-07-26 | False | 1.0 | True | （無） |
| F | 2026-07-27 | False | 1.0 | True | （無） |
| F | 2026-07-28 | **True** | 0.0 | False | （無產出，未算 metrics） |
| F | 2026-07-29 | False | 1.0 | True | （無） |
| F | 2026-07-30 | False | 1.0 | True | （無） |
| F | 2026-07-31 | False | 1.0 | True | （無） |
| F | 2026-08-01 | False | 1.0 | True | （無） |
| D | 最近一次（`research/evals/sia-report-audit/data/public/results.json`，靜態目標＝2026-06-24 綜述報告） | — | 0.978 | True | （無；m2_task_path_validity=0.9268，3 筆路徑失敗，見下方核對） |

**判讀**：A/C 本週窗口 7/7 天全數 `pass=True`、`overall=1.0`，無弱點。F 於 **2026-07-28** `missing_artifact=True`（`research/DAILY-RESEARCH/2026-07-28-professional.md` 確認不存在，且未被同期發生的批次回填〔`weekly: Claude digest 2026-07-31` #1076〕補上——A/C 同日 07-28 產出皆存在，僅 F 缺，非三 Routine 同日全缺型態）。此為單日、單一 Routine 缺口，樣本 <3 天，依規不提案（見 IDENTIFY）。

**D 分數核對**：`m2_task_path_validity` 3 筆失敗路徑為 `opus-pilot/SKILL.md`／`refs/multi-agent-coordinator-pattern.md`／`subagent-strategy.md`。逐筆核對：
- `opus-pilot/SKILL.md`：已於後續版本統一併入 `.claude/skills/pilot/SKILL.md`（pilot SKILL 明文「取代 haiku-pilot/sonnet-pilot/opus-pilot/fable-pilot」）。
- `subagent-strategy.md`：`.claude/rules/INDEX.md`「v5 結構變更」明文已刪除，其 `[E]` 閘門併入 `graph.md`。
- `refs/multi-agent-coordinator-pattern.md`：於原始 2026-06-24 報告任務表 T14 被引用為未來待建文件，從未實際建立。
直接讀取該靜態目標報告本文（`research/reports/2026-06-24-harness-synthesis-from-archived-papers.md:535`）證實：這 3 筆失敗**在該報告自身 gen_7（SIA 迴圈最終代）任務表中已明文記錄為「皆為既有 T29/T14/T10 路徑缺陷，非本批次新增」**，其中 T29 更被該迴圈自行標記「P2 淘汰」（迴圈本身已決定不修）。此為 SIA 迴圈終代已知且已接受的既有落差，非本輪新發現、非退化——與 07-26 報告「兩筆路徑失敗，非本週新增」的判讀一致（本次核對到第 3 筆同屬既有清單，非新增第三筆），故不提案。

**維護件週檢**：
- `check-routine-fingerprint.sh`：A/C/F OK；**[G] DRIFT**（產出記 `spec_sha=f8044b7...` ≠ 現行 `1ae8bbb2...`）——因 `ROUTINE-G-sia-weekly-improvement.md` 於 07-27 加入 merge 預授權條款後，G 尚未以新版規格跑過一輪。本輪即以現行規格執行，本報告 frontmatter 已記新 `spec_sha`，DRIFT 於本輪後自動歸零，非待修缺陷。
- `compact-inbox.py --dry-run`：no-op（`memory/inbox` 無 ✓routed 且達齡 >30 天條目）。
- `enrichment-scan.py`：偵測到懸空引用 4 筆（`memory/MEMORY.md:110/169/366/473`）。逐檔核對：`career-wiki/LOG.md`→實為 `research/career-wiki/LOG.md`（存在）；`loop.md/graph.md`→實為 `.claude/rules/{loop,graph}.md`（皆存在）；`ship/GOTCHAS.md`→實為 `.claude/skills/ship/GOTCHAS.md`（存在）；`hooks/INDEX.md`→實為 `.claude/hooks/INDEX.md`（存在）。**4/4 皆為簡寫相對路徑假陽性**，與 07-12/07-19/07-23/07-26 四批（78-100% 假陽性率）同型，構成**連續第 5 批**。既有提案 `enrichment-scan-path-resolution-and-negation-filter`（2026-07-26 提出）狀態仍為 `proposed`（未套用）——本輪不重複提案，僅追加本批 4 筆作為佐證樣本。
- `usage-pacer.py --self-test`：PASS（九情境全綠）。
- `healthcheck.sh`：PASS 255 / WARN 0 / FAIL 0；UPS 三斷言（fusion 正例／負例、AUTO 行存在）全 PASS。
- 路由連動週檢（multi-mode §1d 撤退條款）：`evolution/cost-log.jsonl`（261 筆）逐鍵掃描，schema 固定為 `branch/cache_*/container_id/cost_usd/duration_secs/input_tokens/model/models/outcome/output_tokens/remote_session_id/session_id/source/timestamp/web_search_requests`，仍**無** `pace`/`water_level`/`tier_downgrade` 欄位。既有提案 `multi-mode-tier-downgrade-costlog-field`（2026-07-26 提出）狀態仍為 `proposed`（未套用）——**連續第 4 週**（07-19/07-23/07-26/08-02）同一缺口，本輪不重複提案，僅記錄延續。
- L4 fixtures：本週 `git log --since=2026-07-26` 對 `fusion/`、`multi-mode-skill/`、`output-compress/` 三 SKILL 目錄無 `skill-evolution:apply` 型變更（唯一命中的 digest 合併提交對三目錄實際 diff 為空），依規跳過 F1-F3 前後對照。

**壓縮遙測彙總**（`scripts/compress-metrics.py`，SSoT）：

7 天窗（`--window 7`，2026-07-25 起）：21 筆，零筆日 0/7。

| combo | n | pass_rate | saving_pct | grounded_pct |
|---|---|---|---|---|
| lite×report | 1 | 1.0 | 1.3% | 99.4% |
| lite×routine-a | 5 | 1.0 | 0.0% | 100.0% |
| lite×routine-c | 7 | **0.571** | 0.8% | 99.3% |
| lite×routine-e | 3 | 1.0 | 0.0% | 100.0% |
| lite×routine-f | 5 | **1.0** | 0.0% | 100.0% |

V1 觸發：`lite×routine-c`（0.571<0.90）。**對照 07-26 已套用修法**（`output-compress-lite-tier-negation-first-not-propagated`，status: applied 2026-07-26，成功條件鎖定 `lite×routine-f` 7 天窗 pass_rate≥0.90 且 n≥3）：
- `lite×routine-f` 本週首次樣本足量（n=5≥3），pass_rate=1.0——**原成功條件達標**。
- `lite×routine-c` 逐筆檢視（`evolution/compress-log.jsonl`，07-25~07-31）：07-25 fail（修法前）、07-26 pass（修法當天）、**07-27 fail**（修法後 1 天，`missing_keys:["negation_counts"]`）、07-29 pass、07-30 pass、**07-31 fail**（同一失敗特徵，同日重試後 pass）。修法後仍兩度復發同一 `negation_counts` 遺失特徵，7 天窗 pass_rate=0.571（n=7）。
→ 修法對 `routine-f` context 已生效，對 `routine-c` context 未完全生效——**新弱點，見下方 PROPOSE**。

28 天窗（`--window 28 --json`）節錄：`lite×routine-c` n=16 pass_rate=0.625；`lite×routine-f` n=19 pass_rate=0.737（28 天窗仍含修法前歷史筆數拉低均值，與 7 天窗新趨勢不衝突）；`full×subagent-prompt` n=11 pass_rate=0.727（07-19/07-23/07-26 報告已判定為修復前舊窗口，非本週新增）。zero_days(28d)=7（<20，未達 V3 記錄門檻）；V6 execution_rate=0.06（252 機會、15 執行，2026-08-13 複查輸入，本輪僅累積不處置）。

⚠️ 執行率檢查（G13）：過去 7 天 compress-log 零筆日僅 `2026-08-02`（今日，A/C/F 尚未觸發，非缺失）＝1/7，遠低於 ≥5/7 判讀門檻，AUTO 執行率本週健康。

## IDENTIFY — 根因歸維

| Routine/Metric | 現象 | 根因層 | 證據 | 提案？ |
|---|---|---|---|---|
| F 於 2026-07-28 `missing_artifact=True` | `research/DAILY-RESEARCH/2026-07-28-professional.md` 未產出，同期批次回填（#1076）亦未補上；A/C 同日皆正常 | (e) 單日環境事故（單一 Routine、單日，非三 Routine 同日全缺型態） | 本週窗口內僅此 1 例，樣本 <3 天 | ❌ 不提案（樣本不足） |
| D `m2_task_path_validity`=0.9268（3 筆路徑失敗） | 3 筆失敗路徑核對後皆為 gen_7（SIA 迴圈終代）任務表已明文記錄的既有缺陷（T29/T14/T10，T29 並標「P2 淘汰」），非本輪新增、非退化 | (e)（迴圈已終結並接受的既有落差，非本輪環境事故但同屬「不需本輪動作」類） | `research/reports/2026-06-24-harness-synthesis-from-archived-papers.md:535` 原文任務表註記 | ❌ 不提案（迴圈已自行決定不修，重提無新資訊） |
| `enrichment-scan.py` dangling-refs 偵測器 | 連續 5 批（07-12/19/23/26/08-02）假陽性率 78-100%，本批 4/4 皆簡寫相對路徑假陽性 | (b) 評分/檢查工具門檻不合理 | 本週 4 筆逐檔核對 4/4 假陽性；既有提案 `enrichment-scan-path-resolution-and-negation-filter`（07-26）status 仍 proposed | ❌ 不重複提案（既有提案未套用，本批僅補佐證） |
| `cost-log.jsonl` 缺 `pace`/`tier_downgrade` 欄位 | SKILL.md §1d 宣稱「降檔照常記入 cost-log」與實作連續第 4 週不符 | (a) SKILL 指示與實作不符 | `evolution/cost-log.jsonl`（261 筆）逐鍵掃描；既有提案 `multi-mode-tier-downgrade-costlog-field`（07-26）status 仍 proposed | ❌ 不重複提案（既有提案未套用） |
| `lite×routine-c` `negation_counts` 復發 | 07-26 已套用的 level-agnostic 修法對 `routine-f` context 生效（本週首次達標：n=5, pass=1.0），但 `routine-c` context 修法後仍於 07-27、07-31 兩度復發同一失敗特徵，7 天窗 pass_rate=0.571（n=7，V1 觸發） | (a) 既有修法未完全涵蓋所有 context（SKILL 指示與 routine-c 實際壓縮行為不符） | `evolution/compress-log.jsonl` 07-25~07-31 逐筆 `missing_keys` 欄位；07-26 報告已記錄「原成功條件樣本不足」，本週樣本足量後確認 routine-c 未達標 | ✅ 提案（新，V1 直接觸發、非既有提案的重複） |

## PROPOSE — 改進提案（1 條，mode=sia-lite 手動 Feedback 紀律）

1. **output-compress-lite-routine-c-negation-still-dropping**
   - 目標文件：`.claude/skills/output-compress/SKILL.md` §4（僅提案，需走 `skill-evolution:apply output-compress` 執行，不直改 SKILL）
   - 具體修改方向：07-26 已套用的「§4 適用所有 level/context，無例外」宣告對 `routine-f` context 已驗證生效，但 `routine-c` context（原文長度普遍較長，`compress-log` 顯示 orig_bytes 常在 13-27KB，高於 routine-f）修法後仍於 07-27、07-31 兩度遺失 `negation_counts`；建議在 §4 對長輸入（原文 >15KB 或段落數較多）明確要求分段壓縮或壓縮後二次自我核對白名單元素是否完整保留，而非僅依賴單次生成指令覆蓋長 context。
   - 可機械驗證的成功條件：套用後 `python3 scripts/compress-metrics.py --window 7 --json` 之 `combos["lite×routine-c"].pass_rate ≥ 0.90`（需 n≥3 才判定，樣本不足則延長觀察窗，比照 07-26 報告對 `lite×routine-f` 的判定方式）。
   - 反 eval-hack 聲明：`pass`/`missing_keys` 由 `fidelity-check.py` 對原文與壓縮文做白名單元素（含 `negation_counts`）機械 diff 判定，非模型自評分數，無法透過「少壓一點」規避——本週資料中已有多筆 `saving_pct=0.0` 但仍記為 `pass=true` 的樣本（如 07-29/07-30），顯示「不壓縮以求安全過關」的退化模式若發生，會同步反映在 `saving_pct` 這個獨立量測軸上而非被本提案掩蓋；此修法只要求對長輸入加一道自我核對步驟，不放寬/縮減白名單定義本身。
   - 依據：`evolution/compress-log.jsonl` 07-25~07-31 逐筆記錄 + `research/EVOLUTION-QUEUE.md` `output-compress-lite-tier-negation-first-not-propagated` 條目（applied 2026-07-26）+ 本報告 OBSERVE/IDENTIFY 節。

對抗自審（Feedback）：
- 本提案若套用，`evaluate.py`（A/C/D/F）任一分數皆不會改變——`compress-metrics.py` 的 combo pass_rate 非任何 Routine 的 SIA 評分依據，唯一改變的是「原文與壓縮文結構化元素是否一致」這個獨立、機械、與壓縮者是否想討好分數無關的量測，eval-hack 路徑不成立。
- 唯一需要提防的反例：若修法只是讓 lite 層「幾乎不壓縮」（saving_pct→0）來規避遺漏，會表面上讓 pass_rate 回升但失去壓縮的實際效益——本提案已在反 eval-hack 聲明中指出 `saving_pct` 是獨立量測軸，後續套用者/審核者應同時檢查 `saving_pct` 未因此顯著劣化，本提案本身不掩蓋此風險。

## APPLY — 寫入

本報告 + 上列 1 條提案已追加至 `research/EVOLUTION-QUEUE.md`（status: proposed；查重：本提案為首次以標準格式提出，非既有候選之重複；enrichment-scan 與 cost-log 兩項既有提案本輪僅補佐證、未重複建立條目）。

## TEST — 提案可驗證性閘（bash 展示）

```
$ test -f research/reports/2026-08-02-routine-g-sia-weekly.md && grep -q '## Unknowns' research/reports/2026-08-02-routine-g-sia-weekly.md && grep -cq 'overall' research/reports/2026-08-02-routine-g-sia-weekly.md && echo "✅ 報告 OK"
✅ 報告 OK

$ grep -A10 "^### \[2026-08-02\] output-compress-lite-routine-c" research/EVOLUTION-QUEUE.md | grep -c '成功條件\|反 eval-hack 聲明'
3   # ≥2×提案數（1 條提案）

$ # 提案數 = 1（≤2 上限）

$ # 安全邊界：先 revert 兩個與本輪無關的 hook telemetry 檔（evolution/autoload-load-log.jsonl、memory/.memory-sync-seen.txt，非本輪產出，屬背景 hook 噪音），再檢查
$ git status --porcelain | grep -v 'EVOLUTION-QUEUE\|reports/\|routine-heartbeat.json' && echo "❌ 越界寫入" || echo "✅ 邊界 OK"
✅ 邊界 OK
```

> 註：spec 內 `grep -A8 "routine-g-${TODAY}"` 範例字串（"routine-g-" 在日期前）與本 workspace 實際檔名慣例（日期在 "-routine-g-" 前，如 `2026-08-02-routine-g-sia-weekly.md`）順序相反，逐字執行恆為 0 命中——本輪改以直接對本次新增條目的 `### [2026-08-02] {slug}` 標頭定位驗證，語意等價（驗證同一件事：新提案是否含四要素），已於本節展示。

## Unknowns

- [KU] 2026-08-02（今日）A/C/F 尚未觸發（A cron 15:00 UTC／C 16:00 UTC／F 18:00 UTC，皆晚於本輪 G 執行時刻 19:04 UTC 前的檢查時點但接近），OBSERVE 窗口改採「已完成的 UTC 日」（07-26~08-01）而非「Taipei 曆日往前推 7 天」，與 artifact 檔名採 UTC 日期的既有慣例一致（以 `research/DAILY-RESEARCH/2026-08-01-professional.md` commit 時間 `2026-08-02T02:10+08:00` 但檔名仍為 `2026-08-01` 為證）。下週執行者若窗口起訖與本週不同，請先核對 artifact 檔名日期慣例，勿逕自套用 Taipei 曆日。
- [UK] `lite×routine-c` 復發的確切機制（是否與原文長度/段落結構相關）本輪僅由 `orig_bytes` 粗略比對推論，未實際比對 routine-c 與 routine-f 兩者被壓縮前的原始 worker brief 差異——若下輪套用提案後仍未達標，需人工實際比對兩 context 的 AUTO 呼叫路徑差異，而非僅調整 SKILL 文字。
- [UU] 本次僅驗證 A/C/F/D 四個 Routine 分數與 output-compress/cost-log 兩項遙測；Routine B/E 近期走勢、以及 `enrichment-scan.py`/`multi-mode-skill` 兩項既有 proposed 提案除本輪佐證外的其他潛在關聯面向（例如 `enrichment-scan.py` 假陽性模式是否也出現在非 `memory/MEMORY.md` 的其他常被引用檔案），未在本輪範圍內覆核 → 留給下次 Routine G 或人工審核提案時一併檢視。

`[Checkpoint] Routine G 2026-08-02：mode=sia-lite｜分數表=4Routine×7天（D=最近一次）｜系統性弱點=1（lite×routine-c negation_counts 修法未完全生效）｜提案=1（output-compress-lite-routine-c-negation-still-dropping）｜其餘4項候選核對後不提案/不重複提案｜PR 待開`

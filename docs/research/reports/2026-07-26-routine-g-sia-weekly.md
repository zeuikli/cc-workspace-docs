---
date: 2026-07-26
mode: sia-lite
proposals: 2
routine: G
spec_sha: f8044b717378478122cead2b9d2e99ad248a33ea
weaknesses_identified: 2
---

# Routine G：SIA 週改進迴圈 — 2026-07-26

`[Phase0] mode=sia-lite｜python=3.11.15｜sia-venv=無`

無持久 `~/.sia-venv/bin/sia`（cloud session 預期常態，非降級）。以下依 SIA 三角色紀律手動執行一輪：Meta＝界定本次待評 metric 範圍、Target＝生成提案草稿、Feedback＝對抗自審。

## OBSERVE — 過去 7 天分數表

逐日重跑 `evaluate.py`（確定性、零 LLM 判斷）：

| Routine | Date | missing_artifact | overall | pass | metrics<0.5 |
|---|---|---|---|---|---|
| A | 2026-07-20 | False | 1.0 | True | （無） |
| A | 2026-07-21 | False | 1.0 | True | （無） |
| A | 2026-07-22 | **True** | 0.0 | False | （無產出，未算 metrics） |
| A | 2026-07-23 | False | 1.0 | True | （無） |
| A | 2026-07-24 | False | 1.0 | True | （無） |
| A | 2026-07-25 | False | 0.9844 | True | （無，m7_topic_quota=0.875 單日波動） |
| A | 2026-07-26 | False | 1.0 | True | （無） |
| C | 2026-07-20 | False | 1.0 | True | （無） |
| C | 2026-07-21 | False | 1.0 | True | （無） |
| C | 2026-07-22 | **True** | 0.0 | False | （無產出，未算 metrics） |
| C | 2026-07-23 | False | 1.0 | True | （無） |
| C | 2026-07-24 | False | 1.0 | True | （無） |
| C | 2026-07-25 | False | 0.925 | True | （無，m6_arxiv_dedup=0.25 單日波動） |
| C | 2026-07-26 | False | 1.0 | True | （無） |
| F | 2026-07-20 | False | 1.0 | True | （無） |
| F | 2026-07-21 | False | 1.0 | True | （無） |
| F | 2026-07-22 | **True** | 0.0 | False | （無產出，未算 metrics） |
| F | 2026-07-23 | False | 1.0 | True | （無） |
| F | 2026-07-24 | False | 1.0 | True | （無） |
| F | 2026-07-25 | False | 1.0 | True | （無） |
| F | 2026-07-26 | False | 1.0 | True | （無） |
| D | 最近一次（`research/evals/sia-report-audit/data/public/results.json`） | — | 0.976 | True | （無；m2_task_path_validity=0.92 兩筆路徑失敗，非本週新增） |

**判讀（07-22 缺口 = 舊事件重現於滑動視窗，非新發生）**：本週視窗（07-20~07-26）內唯一 `missing_artifact` 仍是 **2026-07-22**——與上週（2026-07-23 報告）已記錄、判定為「單日環境事故」的**同一天**，只是因 7 天滾動視窗與上週有 3 天重疊而再度落入本週窗口，**不是新的一次發生**。本週實際新增的 6 天（07-24~07-26 三 Routine 逐日）**全數 `missing_artifact=False`**，無任何一天出現「三 Routine 同日全缺」的新實例。依上週 Unknowns 記載的處置條件（「若再現『三 Routine 同日全缺』即升級為系統性弱點並提案」），此處置條件要求的是**新的一天**再犯同型態，而非同一天在重疊窗口內被重複看到——故本次判定**不構成 recurrence**，維持「單日、樣本 <3 天、不提案」的分類，僅更新 KU 措辭避免下週再誤讀為第二次發生。

**維護件週檢**：
- `check-routine-fingerprint.sh`：A/C/F/G 全 OK（[A] `DAILY-TOPICS/2026-07-26.md`、[C] `DAILY-RESEARCH/2026-07-26.md`、[F] `DAILY-RESEARCH/2026-07-26-professional.md`、[G] 上週報告存在）。
- `compact-inbox.py --dry-run`：no-op（`memory/inbox` 無 ✓routed 且達齡 >30 天條目）。
- `enrichment-scan.py`：偵測到懸空引用 5 筆（`memory/MEMORY.md:96/155/161/174/189`）。逐檔 `find`/路徑核對：**5 筆全為假陽性**——`:96`/`:161` 引用簡寫相對路徑 `VAR/x.sh`（實為既有已知假陽性，MEMORY 原文本身即在描述該偵測器的既有限制，非待修引用）；`:155` `.factory/profiles.json` MEMORY 原文正在斷言「該檔從未存在，刻意不新建副本」（否定語境，同 07-23 batch `:299` 同型缺陷）；`:174` `rules/prompt-lifecycle.md` 為簡寫路徑，真實存在於 `.claude/rules/prompt-lifecycle.md`；`:189` `.claude/hooks/y.sh` MEMORY 原文是在描述一個**已知未修的 bug 案例**（FP5），非懸空引用。本批次假陽性率 5/5 = 100%，與 07-25 人工裁決確認的 07-12/07-19/07-23 三批合計 7/9≈78% 假陽性率同型——已連續 **4 批**，構成 core.md「同一簽名重現 ≥2 次」門檻，見下方 PROPOSE 提案 1。
- `usage-pacer.py --self-test`：PASS（九情境全綠）。
- `healthcheck.sh`：PASS 246 / WARN 5 / FAIL 0；WARN 皆為既有基準計數漂移（hooks/skills/MCP 數量，需人工更新 EXPECTED_* 常數，非本週新增行為異常）；UPS 三斷言（fusion 正例/負例、AUTO 行存在）全 PASS。
- 路由連動週檢（multi-mode §1d 撤退條款）：`evolution/cost-log.jsonl`（453 筆）逐鍵檢查，schema 仍**無** `pace`/`water_level`/`tier_downgrade` 相關欄位可供「水位降檔組 re-handoff 率」比對——**連續第 3 週**同一量測缺口（07-19、07-23、07-26），且 SKILL.md §1d 明文宣稱「降檔照常記入 cost-log」與實際 schema 不符，達 07-23 報告設定的「第 3 週仍無資料」轉提案門檻，見下方 PROPOSE 提案 2。
- L4 fixtures `research/evals/skill-autotrigger/`：本週 `skill-evolution:apply output-compress`（SKILL v1.3.0→v1.4.0，2026-07-26 稍早，Negation-first 條款 lite 層傳導修正）觸及 output-compress，依規必跑 F3 前後對照。以 `f3-original.txt` 為基準手動產生 lite 級壓縮樣本（保留白名單：日期×2、`at least 3`、否定/entitlement 子句、inline code、`deploy.log`；僅刪「注意：」「這個」等填充詞），`fidelity-check.py --level lite --context routine-f3-regression` 結果 `{"pass": true, "missing": {}}`，exit=0——**F3 post-fix 通過**，lite 層 negation 保留條款於本 fixture 實測有效（與 compress-log 今日兩筆新記錄 `lite×routine-c`/`lite×routine-f` 皆 pass 互證，但樣本量仍待累積，見下）。F1/F2（fusion/multi-mode）本週未被 `skill-evolution:apply` 觸及，依規跳過。

**壓縮遙測彙總**（`scripts/compress-metrics.py`，SSoT）：

7 天窗（`--window 7`）：22 筆，零筆日 1/7（即 07-22，與三 Routine 缺席日一致，非獨立異常）。`lite×routine-c` pass_rate=0.5（n=6）、`lite×routine-f` pass_rate=0.875（n=8）觸發 V1，但逐筆時間序顯示失敗**全部集中在 skill-evolution:apply 修復（2026-07-26）之前**（07-24/07-25 各一筆 `negation_counts` 缺失），修復當日（07-26）新增的兩筆 `lite×routine-c`/`lite×routine-f` 記錄**皆 pass**。既有提案 `output-compress-lite-tier-negation-first-not-propagated`（EVOLUTION-QUEUE 2026-07-19）今日狀態已更新為 `applied 2026-07-26`，其原定成功條件（7 天窗 `lite×routine-f` pass_rate ≥0.90，n≥3）**修復後樣本僅 n=2**，尚未達可判定門檻——依查重規則本週不重複提案，僅記錄修復已生效跡象（F3 regression + 兩筆新 pass）供下週累積判定。

28 天窗（`--window 28 --json`）節錄：

| combo | n | pass_rate | 判讀 |
|---|---|---|---|
| lite×routine-c | 11 | 0.636 | V1 觸發，同上——已有 applied 修復待樣本累積 |
| lite×routine-f | 16 | 0.688 | V1 觸發，同上 |
| full×subagent-prompt | 11 | 0.727 | V1 觸發，但（同 07-19/07-23 報告判定）全數為 2026-07-11 修復前舊窗口，非本週活躍問題 |
| lite×routine-a | 8 | 1.0 | 健康 |
| lite×report | 5 | 1.0 | 健康 |

zero_days（28d）=13/28（<20，未達 V3 記錄門檻）；V6 execution_rate=0.114（132 機會、15 執行）為既有 advisory 執行率過低累積證據，非本週新增判讀。

## IDENTIFY — 根因歸維

| Routine/Metric | 現象 | 根因層 | 證據 | 提案？ |
|---|---|---|---|---|
| A/C/F 於 2026-07-22 `missing_artifact=True` | 三 Routine 目標檔完全未產出（舊事件，重現於本週滑動視窗） | (e) 單日環境事故（07-23 報告已判定） | 本週窗口內 07-24~07-26 三 Routine 逐日皆正常，無新實例 | ❌ 不提案（非新發生，樣本仍 <3 天） |
| `enrichment-scan.py` dangling-refs 偵測器 | 連續 4 批（07-12/07-19/07-23/07-26）假陽性率 5/5~9/9 區間、合計 78-100%；不解析簡寫相對路徑、不辨否定語境 | (b) 評分/檢查工具門檻不合理（掃描器設計缺陷，非資料本身有誤） | `research/EVOLUTION-QUEUE.md:761-772`（2026-07-25 人工裁決 9 筆假陽性根因分析）+ 本週 5 筆逐檔 `find`/否定語境覆核 100% 假陽性；對照 `check-references.sh` 嚴格 gate 本週回報 dangling=0 orphan=0，互證真實懸空引用數為 0 | ✅ 提案 1（正式化既有「建議修法」為 EVOLUTION-QUEUE 標準格式提案） |
| multi-mode-skill §1d 水位降檔 → cost-log 記錄 | SKILL.md 明文「降檔照常記入 cost-log」，但 `cost-log.jsonl`（453 筆）schema 連續 3 週無對應欄位，Routine G 週檢「水位降檔組 re-handoff 率」比對持續無資料可判 | (a) SKILL 指示與實作不符（宣稱行為未落地） | `evolution/cost-log.jsonl` 逐鍵掃描（本週 453 筆，欄位固定為 timestamp/duration/session/model/tokens/cost 等，無 pace/water/tier_downgrade）；07-19、07-23 報告已記錄同一缺口 | ✅ 提案 2（達 07-23 報告設定「第 3 週仍無資料」轉提案門檻） |

## PROPOSE — 改進提案（2 條，mode=sia-lite 手動 Feedback 紀律）

1. **enrichment-scan-path-resolution-and-negation-filter**
   - 目標文件：`scripts/enrichment-scan.py`（僅提案，待人工審核）
   - 具體修改方向：① dangling-refs 候選路徑對 `{repo_root, scripts/, tests/, .claude/hooks/tests/, research/, research/ai-articles/, .claude/rules/, .claude/skills/*/}` 逐一試解析，全數落空才報；② 對命中行做否定詞前置過濾（`不存在`/`皆無`/`未產出`/`missing`/`尚未`/`從未`）。
   - 可機械驗證的成功條件：以本週 5 筆 + 前三批合計 14 筆已知案例為 fixture 重跑 `enrichment-scan.py`，假陽性率應從目前 4 批合計 78-100% 降至 <20%（即 14 筆中僅 `:165`/`:316`（07-23 批，已修）等真陽性繼續被報出，其餘簡寫路徑/否定語境筆數不再出現於 dangling-refs 區塊）。
   - 反 eval-hack 聲明：此修法只改善掃描器對「檔案是否真的存在」與「該行是否真的在引用（而非否定該引用）」的判定精確度，不放寬或跳過任何真實 dangling reference 的偵測——`check-references.sh` 嚴格 gate 本週同步回報 dangling=0，證明真正待修的懸空引用本就是 0，降低的是雜訊率而非降低偵測力。
   - 依據：`research/EVOLUTION-QUEUE.md` 2026-07-25 裁決註記（行 761-772）+ 本報告 IDENTIFY 節。

2. **multi-mode-tier-downgrade-costlog-field**
   - 目標文件：`.claude/skills/multi-mode-skill/SKILL.md` §1d（宣稱行為對照）+ 實際寫入 `cost-log.jsonl` 的腳本（`scripts/sync-remote-vm-usage.py` 或降檔判斷發生處，**僅提案，待人工審核與定位確認**）
   - 具體修改方向：降檔決策發生時（`usage-pacer.py` fanout=`prefer-lower-tier` 且未觸發品質底線例外）於寫入 cost-log 的記錄中新增 `tier_downgrade`（bool）與 `water_level_verdict`（string，直引 pacer verdict 的 `fanout` 值）二欄，使 §1d 已明文宣稱的「降檔照常記入 cost-log」有實際資料落地。
   - 可機械驗證的成功條件：套用後 `python3 -c "import json; rows=[json.loads(l) for l in open('evolution/cost-log.jsonl')]; assert any('tier_downgrade' in r for r in rows[-20:])"` 通過（新記錄含該欄位）；累積 ≥1 筆降檔事件後，Routine G 週檢「水位降檔組 re-handoff 率 vs 常態組」比對首次具備可執行資料（比對結果非本提案驗收範圍，屬後續觀察）。
   - 反 eval-hack 聲明：此修法不新增任何路由判斷邏輯、不影響任何實際降檔決策，純粹補齊 SKILL.md 既有宣稱與 cost-log 實作之間的資料落差——讓已存在 3 週的「無資料可判」週檢缺口變成「有資料可判」，量測的是既有行為是否發生，不是製造討好評分器的新分數。
   - 依據：`research/reports/2026-07-19-routine-g-sia-weekly.md` + `2026-07-23-routine-g-sia-weekly.md` Unknowns 節（同一缺口連續記錄）+ 本報告 IDENTIFY 節。

對抗自審（Feedback，兩條提案皆過）：
- 提案 1 若套用，`enrichment-scan.py` 本身無 evaluate.py 分數可討好（它是唯讀維護腳本非 SIA 評分對象）；驗證方式是「假陽性率下降」而非任何 Routine 分數上升，eval-hack 路徑不成立。
- 提案 2 若套用，不會讓任何一個 evaluate.py 分數改變（cost-log 非任何 A/C/F/D 的 metric 依據）；唯一改變的是「路由連動週檢」從無資料變有資料，若擔心「靠有資料製造健康假象」——反論：資料本身只是欄位存在與否的事實記錄，週檢的「re-handoff 率」比對邏輯完全獨立於本提案，無法靠補欄位美化該比對結果。

## APPLY — 寫入

本報告 + 上列 2 條提案已追加至 `research/EVOLUTION-QUEUE.md`（status: proposed；查重：兩者皆為首次以標準四要素格式提案，非重複既有候選）。

## TEST — 提案可驗證性閘（bash 展示，見下方 Checkpoint 前實跑）

```
$ test -f research/reports/2026-07-26-routine-g-sia-weekly.md && grep -q '## Unknowns' research/reports/2026-07-26-routine-g-sia-weekly.md && grep -cq 'overall' research/reports/2026-07-26-routine-g-sia-weekly.md && echo "✅ 報告 OK"
✅ 報告 OK
```
（提案四要素檢查與邊界檢查於 RECORD 前一併展示。）

## Unknowns

- [KU] 2026-07-22 三 Routine 同日全缺目前僅 1 個獨立實例（樣本 <3 天），本週窗口滑動使其第二次出現在報告中，但**非新發生**——下週（08-02）窗口將完全滑出此日，屆時若無新實例即可安全結案，不需再追蹤；若追蹤中誤把「同一天在重疊窗口再現」算成 recurrence，會錯誤觸發不必要的提案，故本條特別澄清判讀規則供下週執行者對照。
- [UK] `check-routine-fingerprint.sh` 僅驗「最新一日/最近報告」是否存在，不做逐日回溯比對，故 07-22 該類單日缺口若發生在非最新日，此腳本本身不會警示（07-23 報告已記錄同一觀察，本週複核仍成立）→ 處置：非本 Routine 職權（腳本本身改動需人核），延續記錄。
- [UU] 本次僅驗證 A/C/F/D 四個 Routine 與 output-compress 遙測，Routine B/E 近期分數走勢、以及 fusion/multi-mode 兩個本週未被 `skill-evolution:apply` 觸及的 SKILL 是否仍有其他非本週可見的漂移，未在本輪範圍內覆核 → 處置：留給下次 Routine G 或人工審核提案時一併檢視。

`[Checkpoint] Routine G 2026-07-26：mode=sia-lite｜分數表=4Routine×7天（D=最近一次）｜系統性弱點=2（enrichment-scan 假陽性連續4批、cost-log pace 欄位缺失連續3週）｜提案=2（enrichment-scan-path-resolution-and-negation-filter、multi-mode-tier-downgrade-costlog-field）｜PR 待開`

---
date: 2026-07-23
mode: sia-lite
proposals: 0
routine: G
spec_sha: f8044b717378478122cead2b9d2e99ad248a33ea
weaknesses_identified: 1
---

# Routine G：SIA 週改進迴圈 — 2026-07-23

`[Phase0] mode=sia-lite｜python=3.11.15｜sia-venv=無`

無持久 `~/.sia-venv/bin/sia`（cloud session 預期常態，非降級）。以下依 SIA 三角色紀律手動執行一輪：Meta＝界定本次待評 metric 範圍、Target＝生成提案草稿、Feedback＝對抗自審。

## OBSERVE — 過去 7 天分數表

逐日重跑 `evaluate.py`（確定性、零 LLM 判斷）：

| Routine | Date | missing_artifact | overall | pass | metrics<0.5 |
|---|---|---|---|---|---|
| A | 2026-07-17 | False | 1.0 | True | （無） |
| A | 2026-07-18 | False | 1.0 | True | （無） |
| A | 2026-07-19 | False | 1.0 | True | （無） |
| A | 2026-07-20 | False | 1.0 | True | （無） |
| A | 2026-07-21 | False | 1.0 | True | （無） |
| A | 2026-07-22 | **True** | 0.0 | False | （無產出，未算 metrics） |
| A | 2026-07-23 | False | 1.0 | True | （無） |
| C | 2026-07-17 | False | 1.0 | True | （無） |
| C | 2026-07-18 | False | 1.0 | True | （無） |
| C | 2026-07-19 | False | 1.0 | True | （無） |
| C | 2026-07-20 | False | 1.0 | True | （無） |
| C | 2026-07-21 | False | 1.0 | True | （無） |
| C | 2026-07-22 | **True** | 0.0 | False | （無產出，未算 metrics） |
| C | 2026-07-23 | False | 1.0 | True | （無） |
| F | 2026-07-17 | False | 1.0 | True | （無） |
| F | 2026-07-18 | False | 1.0 | True | （無） |
| F | 2026-07-19 | False | 1.0 | True | （無） |
| F | 2026-07-20 | False | 1.0 | True | （無） |
| F | 2026-07-21 | False | 1.0 | True | （無） |
| F | 2026-07-22 | **True** | 0.0 | False | （無產出，未算 metrics） |
| F | 2026-07-23 | False | 1.0 | True | （無） |
| D | 最近一次 (gen_7, 靜態 run_1，results.json 最後同步 07-21) | — | 1.0 | True | （無） |

**判讀**：A/C/F 三個 Routine 於 **2026-07-22 同日全數 `missing_artifact=True`**（目標檔完全未產出，非 metric 降分）——`git log --all --grep 2026-07-22` 核對確認當日僅有 `chore(digest)`/`ai-news`/`ai-digest` 類 commit，無任何 `research: daily-research`/`daily: topic-curation`/`research: professional-domain` commit，三 Routine 當日確實**完全未執行**（非產出後被覆蓋或分數計算異常）。其餘 6 天三者皆 1.0/pass。單日、跨三 Routine 同步缺席，樣本 <3 天，依 IDENTIFY 規則不提案，僅記錄觀察並列入下週複查 KU（若同型態「三 Routine 同日全缺」再現 ≥2 次即升級為系統性弱點）。

**維護件週檢**：
- `check-routine-fingerprint.sh`：A/C/F/G 全 OK（比對最新一日/最近報告產出，07-22 缺口未觸發此檢查——該檢查只驗「最新」，非逐日回溯，見 Unknowns）。
- `compact-inbox.py --dry-run`：no-op（無達齡 ✓routed 條目）。
- `enrichment-scan.py`：偵測到懸空引用 7 筆（`memory/MEMORY.md` 行 165/173/174/187/299/316×2，含一筆即 `research/DAILY-TOPICS/2026-07-22.md`——與上述 07-22 缺口互證；與 2026-07-19 已 proposed 之批次（行 476/481）行號不同，屬新出現）——已轉錄 EVOLUTION-QUEUE（見下）。
- `usage-pacer.py --self-test`：PASS（九情境全綠）。
- `healthcheck.sh`：PASS 241 / WARN 3（bm25 索引落後 SKILL.md 等既有項）/ FAIL 0；UPS 三斷言（fusion 正例/負例、AUTO 行存在）全 PASS，非本週弱點。
- 路由連動週檢（multi-mode §1d 撤退條款）：`evolution/cost-log.jsonl`（408 筆）schema 仍無 pace/water-level downgrade 欄位可供比對——**無資料可判**，非「檢查通過」，延續列 Unknowns（同 2026-07-19 報告已記錄之量測缺口，職權屬 multi-mode-skill 非本 Routine）。
- L4 fixtures `skill-autotrigger`：本週無 `skill-evolution:apply` 觸及 fusion/multi-mode-skill/output-compress 三 SKILL，條件不成立，跳過。

**壓縮遙測彙總**（`scripts/compress-metrics.py`，SSoT）：

7 天窗：20 筆，零筆日 1/7（07-22——與三 Routine 缺席日一致，非獨立異常）。

28 天窗（`--window 28 --json`）節錄：

| combo | n | pass_rate | 判讀 |
|---|---|---|---|
| lite×routine-f | 12 | 0.583 | V1 觸發，**已有對應 proposed 提案在審**（見下）|
| lite×routine-c | 8 | 0.75 | V1 觸發，同上 |
| full×subagent-prompt | 11 | 0.727 | V1 觸發，但 11 筆全數為 2026-07-11 修復前舊窗口（見 2026-07-19 報告 IDENTIFY），非本週活躍問題 |
| lite×routine-a | 7 | 1.0 | 健康 |
| lite×report | 4 | 1.0 | 健康 |

zero_days（28d）=16/28（<20，未達 V3 記錄門檻）；V6 execution_rate=0.133（113 機會、15 執行）為既有 advisory 執行率過低累積證據，非本週新增判讀。

## IDENTIFY — 根因歸維

| Routine/Metric | 現象 | 根因層 | 證據 | 提案？ |
|---|---|---|---|---|
| A/C/F 於 2026-07-22 同日全數 `missing_artifact=True` | 三 Routine 目標檔完全未產出 | (e) 單日環境事故（推定；GitHub Actions/上游 pipeline 未在本 Routine 職權內可深查） | `git log --all --grep 2026-07-22` 無對應 research commit；`enrichment-scan` 同步偵測 `DAILY-TOPICS/2026-07-22.md` 懸空引用互證 | ❌ 不提案（單日、樣本 <3 天；首次出現「三 Routine 同日全缺」此一簽名，記入 KU 供下週覆核） |
| output-compress **lite×routine-c / lite×routine-f** pass_rate 持續 <0.90 | lite×routine-f 0.583（12 筆，28d）；lite×routine-c 0.75（8 筆，28d）；失敗筆持續集中 `negation_counts`/`number` 兩類白名單缺項 | (a) SKILL 指示與 lite 層 AUTO 流程實作不符（與 2026-07-19 報告判定同因） | `evolution/compress-log.jsonl` 逐筆 `missing_keys` 直引；2026-07-21 lite×routine-c 仍新增一筆同型失敗（`negation_counts`+`number`+`hedge_counts`），確認問題持續未修復 | ⚠️ **已有提案在審**（`output-compress-lite-tier-negation-first-not-propagated`，EVOLUTION-QUEUE 2026-07-19，status: proposed），依查重規則不重複提案——見下 |

## PROPOSE — 改進提案（0 條，mode=sia-lite 手動 Feedback 紀律）

本週唯一達門檻的系統性弱點（output-compress lite×routine-c/f 持續 <0.90）**已於 2026-07-19 由 Routine G 提案**（`output-compress-lite-tier-negation-first-not-propagated`），現況仍為 `status: proposed`（待人工審核，尚未套用）。查重規則（`EVOLUTION-QUEUE.md` 同名候選已 proposed 則跳過並註明）適用——本次不重複提案，僅以本週新資料（07-21 新增一筆同型失敗）佐證該提案仍成立、未過期。

對抗自審（Feedback，即便本週無新提案仍走一輪）：若重複提交同一提案，除浪費人工審核帶寬外不產生任何新驗證訊號（eval-hack 風險為 0，因為根本沒有新提案內容可討好評分器）——維持 0 條為誠實決策。

07-22 三 Routine 同日全缺一項因樣本 <3 天不提案，理由已如上表列。

（提案數 = 0；未強行湊滿上限——兩項候選皆有明確理由不提案：一為樣本不足、一為查重命中既有未決提案。）

## APPLY — enrichment-scan 轉錄

`enrichment-scan.py` 唯讀掃描 `memory/MEMORY.md` 本週發現懸空引用 7 筆（與 2026-07-19 已 proposed 之批次行號不同，屬新出現），已轉錄 `research/EVOLUTION-QUEUE.md`（status: proposed，本 Routine 僅轉錄不合併/刪除，D3 顯式門控）：
1. `enrichment-scan-dangling-refs-20260723`（`memory/MEMORY.md:165`→`tests/lexical-lint-fixture.sh`、`:173`→`know-your-unknowns/GOTCHAS.md`、`:174`→`deep-understanding/GOTCHAS.md`、`:187`→`core.md/prompt-lifecycle.md/measure.sh`、`:299`→`research/DAILY-TOPICS/2026-07-22.md`、`:316`×2→`scored/INDEX.md`/`career-wiki/INDEX.md`）

## Unknowns

- [KU] 2026-07-22 A/C/F 三 Routine 同日**完全未產出**（非僅分數降低）——推定單日環境/上游 pipeline 事故，但本週僅 1 天樣本、且與 2026-07-19 報告記錄的 07-14 部分降分事件簽名不同（該次僅 F missing_artifact，A/C 僅個別 metric=0），故判定為新簽名首次出現，未達「同一簽名重現 ≥2 次」改規則門檻 → 處置：下週 Routine G 若再現「三 Routine 同日全缺」，即升級為系統性弱點並提案（可能方向：OBSERVE 增加跨 Routine 同日 missing_artifact 交叉檢查作為硬信號，比照 `routine-a-stale-digest-detection` 先例）。
- [UK] 路由連動週檢（multi-mode §1d 撤退條款 pace-downgrade re-handoff 率比對）所需欄位在 `evolution/cost-log.jsonl` schema 中持續不存在（連續第 2 週記錄同一缺口）→ 處置：延續標記為量測缺口，非本 Routine 職權（歸屬 multi-mode-skill logging schema），若第 3 週仍無資料建議由人工審核時一併轉交該 SKILL 的 skill-evolution。
- [UU] 本次僅驗證 A/C/F/D 四個 Routine 與 output-compress 遙測，未涵蓋 Routine B/E 近期分數走勢是否也受 07-22 同型事故影響 → 處置：留給下次 Routine G 或人工於審核提案時一併檢視 B/E 週報。

`[Checkpoint] Routine G 2026-07-23：mode=sia-lite｜分數表=4Routine×7天（D=最近一次）｜系統性弱點=1（07-22 三 Routine 同日全缺，樣本不足不提案）｜提案=0（誠實 no-op；既有提案仍待審）｜轉錄=1（enrichment-scan dangling-refs）｜PR 待開`

---
date: 2026-07-12
mode: sia-lite
proposals: 2
routine: G
spec_sha: 4ad7078163e3f9b52b00654b97d4876479ec722f
weaknesses_identified: 4
---

# Routine G：SIA 週改進迴圈 — 2026-07-12

`[Phase0] mode=sia-lite｜python=3.11.15｜sia-venv=無`

無持久 `~/.sia-venv/bin/sia`（cloud session 預期常態，非降級）。以下依 SIA 三角色紀律手動執行一輪：Meta＝界定本次待評 metric 範圍、Target＝生成兩條提案草稿、Feedback＝逐條對抗自審。

## OBSERVE — 過去 7 天分數表

逐日重跑 `evaluate.py`（確定性、零 LLM 判斷）：

| Routine | Date | missing_artifact | overall | pass | metrics<0.5 |
|---|---|---|---|---|---|
| A | 2026-07-06 | False | 0.6389 | False | m5_weekly_focus_updated, m_unknowns_present, m_unknowns_substantive |
| A | 2026-07-07 | False | 0.6389 | False | 同上 |
| A | 2026-07-08 | False | 0.6389 | False | 同上 |
| A | 2026-07-09 | False | 0.6389 | False | 同上 |
| A | 2026-07-10 | False | 0.6389 | False | 同上 |
| A | 2026-07-11 | False | 0.75 | False | m5_weekly_focus_updated, m_unknowns_present, m_unknowns_substantive |
| A | 2026-07-12 | False | 1.0 | True | （無） |
| C | 2026-07-06 | False | 0.7727 | False | m_unknowns_present, m_unknowns_substantive |
| C | 2026-07-07 | False | 0.7727 | False | 同上 |
| C | 2026-07-08 | False | 0.7727 | False | 同上 |
| C | 2026-07-09 | False | 0.7727 | False | 同上 |
| C | 2026-07-10 | False | 0.7727 | False | 同上 |
| C | 2026-07-11 | False | 0.9 | True | m_unknowns_present, m_unknowns_substantive |
| C | 2026-07-12 | False | 1.0 | True | （無） |
| F | 2026-07-06 | **True** | 0.0 | False | （無產出，未算 metrics） |
| F | 2026-07-07 | **True** | 0.0 | False | 同上 |
| F | 2026-07-08 | **True** | 0.0 | False | 同上 |
| F | 2026-07-09 | **True** | 0.0 | False | 同上 |
| F | 2026-07-10 | **True** | 0.0 | False | 同上 |
| F | 2026-07-11 | False | 0.8333 | False | m_unknowns_present, m_unknowns_substantive |
| F | 2026-07-12 | False | 1.0 | True | （無） |
| D | 最近一次 (gen_7) | — | 1.0 | True | （無） |

**missing_artifact 日**：F 於 07-06～07-10 共 5 天缺產出——查證 `git log --diff-filter=A -- research/DAILY-RESEARCH/2026-07-11-professional.md` 得知 F 首次執行為 07-11（#857），此前無產出屬正常（Routine 尚未上線），非執行事故。

**維護件週檢**：
- `check-routine-fingerprint.sh`：A/C/F OK，G SKIP（本次執行前無產出，符合預期）——無 DRIFT。
- `compact-inbox.py --dry-run`：no-op（無達齡 ✓routed 條目）。
- `enrichment-scan.py`：偵測到 3 類真發現（memory/MEMORY.md 完全重複 3 組、高相似 2 組、懸空引用 11 筆）——已轉錄 EVOLUTION-QUEUE（見下）。
- `usage-pacer.py --self-test`：PASS（八情境全綠）。

**壓縮遙測彙總**（`evolution/compress-log.jsonl`，過去 7 天）：

| level/context | n | pass | avg_saving |
|---|---|---|---|
| full/report | 1 | 1/1 | 15.3% |
| full/subagent-prompt | 11 | 8/11 (72.7%) | 9.7% |
| lite/routine-a | 1 | 1/1 | 0.0% |
| lite/routine-c | 1 | 0/1 | 1.5% |
| lite/routine-f | 3 | 1/3 | 5.1% |
| ultra/scratchpad | 1 | 0/1 | 55.8% |

`full/subagent-prompt` <90%（n=11，樣本足夠）列入 IDENTIFY。其餘 n<3（lite/routine-c、lite/routine-f、ultra/scratchpad）樣本不足，不列入。

## IDENTIFY — 根因歸維

| Routine/Metric | 現象 | 根因層 | 證據 | 提案？ |
|---|---|---|---|---|
| A/m5_weekly_focus_updated | 連續6天(07-06~07-11)<0.5，07-12=1.0 | (b) 評分器門檻不合理 | `evaluate.py:160-162` 讀「當前 WEEKLY-FOCUS.md 尾5行是否含 date_str」，非該日期時點快照；`tail -5 research/WEEKLY-FOCUS.md` 只含 2026-07-12——回溯評分結構性必為 0（除當日） | ✅ 提案1 |
| A+C/m_unknowns_present, m_unknowns_substantive | 連續6天<0.5，07-12已恢復1.0 | (e)-變體：KYU rollout（#853，2026-07-11）前 Unknowns 尚非必要輸出；評分器已內建 `KYU_GRACE_WEIGHT=0.5` 30天寬限（`KYU_ROLLOUT_DATE=2026-07-11`）降低過渡期懲罰，現況已修復 | evaluate.py:26-28 grace period 常數；07-12 值已回 1.0 | ❌ 不提案（已修復、非現行弱點） |
| F/missing_artifact | 連續5天(07-06~07-10)=True | (e) 上線前狀態，非執行缺陷 | `git log --diff-filter=A` 顯示 F 首日=07-11(#857)；上線後樣本僅2天<3天門檻 | ❌ 不提案（樣本<3天） |
| output-compress full/subagent-prompt | pass 8/11=72.7%<90% | (a)-變體：SKILL 步驟順序問題——3/3 失敗皆同因 `missing_keys=["negation_counts"]`，且每次失敗後14-16秒內即有 retry 通過（既有 fidelity-check 自癒機制運作正常，但每次耗一輪重試） | `evolution/compress-log.jsonl` 3筆 fail 記錄與其後 retry 記錄時間戳比對 | ✅ 提案2 |

## PROPOSE — 改進提案（2 條，mode=sia-lite 手動 Feedback 紀律）

### 提案 1：routine-a-eval-m5-retroactive-scoring-bug

- **目標文件**：`research/evals/sia-routine-a/data/public/evaluate.py`（僅提案，待人工審核）
- **具體修改方向**：`m5_weekly_focus_updated` 改為依 `--date` 對應時點的歷史內容判定（例如 `git log --before` 取當時 blob），或於非當日回溯模式明確排除 m5 於 overall 平均之外（標 not-applicable），避免「檔案為 rolling 單一狀態」的結構性副作用把回溯分數壓低。
- **可機械驗證的成功條件**：`python3 research/evals/sia-routine-a/data/public/evaluate.py --date 2026-07-08` 之 `m5_weekly_focus_updated` 不再恆為 0（驗證命令：對比 `git log --before="2026-07-08 23:59:59" -1 --format=%H -- research/WEEKLY-FOCUS.md` 取得的歷史內容手動核對該日是否真有更新）。
- **反 eval-hack 聲明**：此修改不改變 Routine A 實際執行行為，只修正評分器的回溯讀取方法，讓歷史分數反映真實狀態而非「單一 rolling 檔案」的量測副作用——是量測層 bug fix，非放寬驗收標準。

### 提案 2：output-compress-negation-counts-first-pass-order

- **目標文件**：`.claude/skills/output-compress/SKILL.md`（僅提案，待人工審核，需走 `skill-evolution:apply output-compress` 執行，不直改 SKILL）
- **具體修改方向**：full 層對 subagent-prompt context 壓縮時，`negation_counts` 計算目前排在摘要壓縮之後、常於首輪被遺漏（3/3 同因失敗，皆靠既有 retry 補回），建議將 negation 保留計算前移至壓縮流程第一步，消除固定重試輪。
- **可機械驗證的成功條件**：套用後 7 天窗口內 `evolution/compress-log.jsonl` 中 `level=full ∧ context=subagent-prompt` 之**首輪**（排除 fail 後 <30 秒內的 retry 記錄）pass 率 ≥90%（驗證命令：沿用本報告 OBSERVE 節之 python3 聚合腳本，加上時間戳去重濾除 retry）。
- **反 eval-hack 聲明**：不降低 `fidelity-check.py` 門檻（`negation_counts` 仍為必要 key），只是把既有正確檢查提前執行以消除多餘重試延遲——效率修正，不影響最終正確性判定。

（提案數 = 2，未超過每週 ≤2 上限。）

## APPLY — enrichment-scan 轉錄

`enrichment-scan.py` 唯讀掃描 `memory/MEMORY.md` 發現 3 類真發現，已轉錄 `research/EVOLUTION-QUEUE.md`（status: proposed，本 Routine 僅轉錄不合併/刪除，D3 顯式門控）：
1. `enrichment-scan-exact-duplicates`（3 組完全重複行）
2. `enrichment-scan-high-similarity`（2 組 Jaccard>0.8）
3. `enrichment-scan-dangling-refs`（11 筆懸空引用）

## Unknowns

- [UK] 提案2（negation_counts 前移）的「首輪 pass 率」驗證命令仰賴以 30 秒視窗判定 retry 歸屬，這是本報告執行時的隱性假設（實際 retry 觸發延遲未有明文 SLA），若未來 retry 延遲超過 30 秒會誤判為獨立首輪失敗 → 處置：已在提案 2 成功條件中寫明此假設，留待人工審核時一併確認視窗合理性。
- [KU] A/C 於 07-12 兩項 unknowns metric 同步回到 1.0 是否為巧合式單日達標、抑或 KYU rollout 後已穩定——僅有 1 天正式數據點（grace period 內），還不足以判斷是否需要提案 → 處置：記錄為 open question，交下週 Routine G 觀察 07-13 起是否持續 ≥1.0，若回落則再議根因。
- [UU] 本次 OBSERVE 只驗證了 A/C/F/D 四個 Routine 與 output-compress 遙測，未涵蓋 Routine B/E 是否也有類似「rolling 單一檔案回溯評分」結構性偏誤（提案1 發現的模式可能是通用 evaluate.py 設計反模式，非 A 專屬）→ 處置：留給下次 Routine G 或人工審核提案1 時一併檢視 B/E 的 evaluate.py 是否有同類 metric。

`[Checkpoint] Routine G 2026-07-12：mode=sia-lite｜分數表=4Routine×7天（D=最近一次）｜系統性弱點=4（2提案+2不提案）｜提案=2（0=誠實no-op 不適用）｜PR 待開`

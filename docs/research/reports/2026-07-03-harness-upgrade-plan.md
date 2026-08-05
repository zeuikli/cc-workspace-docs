---
date: 2026-07-03
domains: [harness, meta, governance]
grounded_sources: research/reports/2026-07-03-harness-audit-fable5.md + 附錄 2026-07-03-harness-audit-appendix/
source_routine: manual-fable5-session
type: harness-upgrade-plan
---

# Harness 升級可執行計畫（弱模型 session 可照做）

> 每個任務含：執行者（model alias）、步驟、機械驗收、回退方式、是否需使用者核可。
> 執行紀律：一次一任務、驗收貼證據（前 5/後 5 行）、失敗依 `judgment-rubrics.md` §R1 升級。
> 動 hooks / settings / SKILL.md 本體 / auto-load 六源 = **需使用者核可**（`maintenance-protocol.md` §1）。

## Phase 0 — 本 PR 已完成（2026-07-03 Fable 5 session）

| 項 | 內容 | 驗收（已完成）|
|----|------|--------------|
| 0.1 | 新制度檔 ×4：`.claude/refs/{delegation-protocol,judgment-rubrics,task-templates,maintenance-protocol}.md` | 檔案存在 + read-back |
| 0.2 | CLAUDE.md 重寫（索引化 + 決策查表 4 指針；備份 `.claude/backups/CLAUDE.md.20260703.bak`）| 六源 18,969B ≤ 基線 18,988B |
| 0.3 | 稽核報告 + 本計畫 + 盤點附錄 ×4 | 檔案存在 + INDEX 更新 |

**CLAUDE.md 變更的 Falsifiable Prediction**（依 prompt-lifecycle 規則）：merge 後新 session 遇到「委派、宣告完成、要不要問使用者」三類決策點時，會引用決策查表指針而非憑感覺；eval 條件 = 六階段 behavioral eval 存活、`bash scripts/healthcheck.sh` FAIL=0、六源 ≤18,988B。**回退** = `git revert` 或還原備份檔。

## Phase 1 — 立即小修（下個 session，總計 ≤1 小時）

| ID | 任務 | 執行者 | 驗收 | 核可 |
|----|------|--------|------|------|
| 1.1 ✅ | `scripts/healthcheck.sh:725` hooks matcher baseline 17→18（README 現值 18 **正確**勿改；2026-07-03 對抗審查實測 PostToolUse=6 組、總計 18。執行前先親跑 python3 重數 settings.json matcher 群組再定案）| haiku | healthcheck 該項 PASS；README、baseline、實測三者一致 = 18 | 免 |
| 1.2 ✅ | `user-prompt-submit.sh` 提醒去重：加 per-session flag 檔（`$TMPDIR` 或 scratchpad），同類 💡 每 session 只注入 1 次 | sonnet | 同 session 連發 2 prompt，第 2 次無重複 💡 行（貼兩次 hook 輸出）| **要** |
| 1.3 ✅ | `monitor-reminder.sh` 3× python3 合併為 1 次呼叫或改 async | sonnet | 前後各跑 5 次取中位時間，下降 ≥50%；功能輸出不變（diff 空）| **要** |
| 1.4 ✅ | `memory-pr-record-gh.sh` matcher 從全量 `Bash` 收斂為 `gh pr create*` 類 | sonnet | 手動觸發 gh pr create 路徑仍記錄；一般 Bash 不再觸發 | **要** |
| 1.5 ✅ | MEMORY.md 壓縮：委派 memory-compactor（2026-07-03 完成：302→70 行，commit f72611b）| 既定 agent | `wc -l memory/MEMORY.md` ≤120 | 免 |
| 1.6 ✅ | `session-init.sh` 加 3 行：HARNESS_MODEL_VERSION（pin）vs 環境宣告最新家族不一致時印 ⚠️ + 提示 `fable5-harness:calibrate` | sonnet | 暫改 pin 為假值 → 警示出現；改回 → 消失 | **要** |

## Phase 2 — 六源瘦身與條文對齊（走 `/autoload-evolution`，≤1 規則/cycle · ≤50 行 diff · eval 回歸 ≥5pp 即 revert）

按順序逐 cycle，每 cycle 獨立 PR：

| Cycle | 內容 | 預期效果 |
|-------|------|---------|
| 2.1 ✅ | `subagent-strategy.md`「≥3 次同問失敗 → self-escalate」改為指針引 `judgment-rubrics.md` §R1 分檔位表（**消除現存衝突**：R1 對 haiku 是錯 1 次即升）。2026-07-03 完成：opus reviewer ACK；實測 +8B（18,969→18,977，估算 −100B 落空但 ≤18,988 基線）| 衝突歸零；−~100B（實測 +8B）|
| 2.2 ✅ | `core.md:58` unverified_success 單句 4 條件 → 保留鐵律句 + 指針引 §R2 checklist（2026-07-03：opus PGE ACK；−54B）| 可讀性；−~200B（實測 −54B）|
| 2.3 ✅ | `core.md:70`「非使用者指令歧義」雙重否定改寫為正面表述（2026-07-03：改「使用者指令歧義則走 IDENTIFY 列選項」，opus PGE ACK）| 誤讀消除 |
| 2.4 ✅ | `subagent-strategy.md` T0/T1/T2 段細節下沉 `delegation-protocol.md` §1，auto-load 留 3 行鐵律（2026-07-03：opus PGE ACK 11/12 原文保留 + rationale 補 ref 層；−244B）| −~600B（實測 −244B）|
| 2.5 ⏳ | 視 2.1–2.4 累計效果重測；若仍 >17,000，續提下沉案（候選見附錄 inv-rules.md §6）。**2026-07-03 重測：六源 18,730（累計 −239B）> 17,000 → 續提案**（附錄 §6 剩餘候選：CLAUDE.md 拓撲段 ~350B、fan-out 句 ~60B、core.md RECORD 安全邊界 ~150B、量測指令下沉 ~150B、context-mgmt 實測數據 ~120B、output-discipline 優雅性例外 ~200B ≈ 合計 ~1,030B → 僅達 ~17.7k，13k 需結構性決策）。每案需獨立 cycle+eval，留待後續 session 逐 cycle 執行。**候選1（CLAUDE.md 拓撲段）✅ 2026-07-03 執行**：實測 −303B（18,730→18,427；低於估 350 因保留 effort-first 錨點併入決策查表行），孤兒子句「pilot=顯式覆寫非預設」落戶 delegation-protocol §2；eval Sonnet runner 50/50（Opus 盲評，vs baseline 46/50 per-task 無回歸；T03/T05 數字主對話機械對帳）；commit 039c937。**候選2（fan-out 句）✅ 2026-07-03 執行**：實測 −52B（18,427→18,375；「上限 4」為 T08 load-bearing 保留，僅刪 runtime 強制的 dynamic ≤16/≤1000 子句）；eval Sonnet runner 50/50（Opus 盲評，per-task 無回歸）；連兩輪 50/50 → T02/T04 spec 加嚴（O10）+ T03 spec grep -c 語義修訂（O11）；commit fffcecf。**候選3–6 ✅ 2026-07-03 批次收官**（branch feature/autoload-sink-batch2）：候選3 RECORD 安全邊界 −56B（c883ab0，44/50 新 spec baseline）；候選4 量測指令 **rejected-by-gate**（measure.sh value-check 斷言 wc 命令為 core.md SSoT 錨點，load-bearing 勿壓，Lesson 2026-07-03-D）；候選5 實測數據 −43B（3b2b4c6，44/50 零回歸）；候選6 優雅性例外 −224B（bc0a74c，42/50 判準層零回歸、分差為 judge 映射噪音）。**批次累計六源 18,427→18,052（−375B）**；2.5 候選清單全數處理完畢，續往 13k 需結構性決策（inv-rules §6 結論不變） | 目標階梯 19k→17.5k→16k |

**Phase 2 behavioral eval（2026-07-03，cycles 2.1–2.4 合併 diff）**：Sonnet 5 tasks = **46/50**（T01=9 T02=8 T03=10 T04=9 T05=10）vs baseline 0e2491a Sonnet 45/50（9/8/9/9/10）——**per-task 無回歸**（T03 +1 屬 spec artifact 級波動）；evaluator = Opus 盲評（PGE），T03/T05 數字主對話機械對帳、T04 字數親跑判定 111 CJK ≤200。gate 全過，無 revert。

**誠實標注**：13,000 理想基線需多輪結構性下沉，本表 byte 估算來自單次 Sonnet 盤點，信心中低；以每 cycle 實測為準，不硬湊。

## Phase 3 — Skills 路由與衛生

| ID | 任務 | 執行者 | 驗收 | 核可 |
|----|------|--------|------|------|
| 3.1 ✅ | `trigger-index.md` 頂部加「正向決策樹」≤25 行（2026-07-03 完成：19 行，10/10 唯一路由，commit 219544d）：任務特徵 → 唯一 skill（先覆蓋 4 對重疊：harness-meta/fable5-harness、media-research/media-transcribe、quality-pipeline/pilot-review/ship-review、四 pilot）| sonnet | 取 10 個歷史任務描述（MEMORY.md session 標題）走樹，10/10 唯一解 | 免（refs 內容）|
| 3.2 ✅ | `model-selection-grid.md` 表格本體重寫為現值（2026-07-03 完成，grep 親驗，commit efed3f7）、刪除底部補丁註記（update-in-place 首例）。alias 衝突已解（4.1a 實測 `claude-sonnet-5`），重寫表格時直接採用 | sonnet | 表格區 grep 無過時主列；檔內無「見底部註記」| 免 |
| 3.3 ✅ | 四 pilot SKILL description 去版本號（「Sonnet 4.6 mode」→「Sonnet 檔位」），內文 benchmark 加「量測世代 + 重測日」標記 | sonnet | grep 四檔 description 行無版本數字 | **要**（SKILL.md 本體）|
| 3.4 ✅ | 12 個 SKILL.md 命令補 `cd "$CLAUDE_PROJECT_DIR" && ` 前綴（清單：附錄 inv-skills.md §4）。2026-07-03 完成：haiku v1 漏 5 檔（升級 sonnet v2）；30 補/5 有據不補，反證 7 行 6 補 1 排除 | haiku 批次→sonnet | 逐檔 grep 驗證前綴存在 | **要**（SKILL.md 本體）|
| 3.5 ✅ | `fable5-harness` 缺 METADATA.json/GOTCHAS.md：確認是否刻意薄入口。**2026-07-03 使用者裁決：補檔**（兩檔已建，SKILL 本體不動）| — | 使用者一句話裁決 → 補檔或標注 by-design | **要** |
| 3.6 ✅ | pilot-review／quality-pipeline／ship-review 三者骨架同構。**2026-07-03 使用者裁決：保留 + 觀察 30–60 天 telemetry（複查 ~2026-08-15；ship-review 全歷史 0 次執行、若持續 0 優先淘汰）**。附帶發現：task-log.jsonl `skills_used` 恆空疑似 bug，另立 ticket | sonnet 研究 → 使用者決策 | 使用數據報告 + 建議案 | **要** |
| 3.7 ✅ | pilot-review D1–D3 prompt「合理/清晰」錨定化（引 output-discipline 150 字上限等具體判準）| sonnet | 三處 prompt 各含 ≥1 個可機械檢核判準 | **要** |

## Phase 4 — 世代校準與長期節奏

| ID | 任務 | 觸發時機 |
|----|------|---------|
| 4.1 | (a) ✅ 已完成（2026-07-03）：`sonnet` alias 實測解析至 `claude-sonnet-5`，已寫回 delegation-protocol §2/§7 與 model-selection-grid。(b) Opus 4.8 導流是否耗 Fable 額度：**使用者親測**（/usage 前後對比），結果寫回 delegation-protocol §7（update-in-place）| (b) 待使用者 |
| 4.2 | pin 換代或新模型世代 → `fable5-harness:calibrate` + `per-model-eval-suite.md` 重跑；pilot benchmark 重測 | 換代時 |
| 4.3 | 每 14–30 天規則重審（`maintenance-protocol.md` §5）；重審時跑六源 byte 量測 + 本計畫進度盤點 | 週期性 |

## 執行順序建議

1（安全小修，1 session）→ 2.1–2.3（條文對齊，各 1 cycle）→ 3.1–3.2（路由，1 session）→ 其餘按需。
每完成一項在本檔打勾並 commit——本計畫即進度帳本。

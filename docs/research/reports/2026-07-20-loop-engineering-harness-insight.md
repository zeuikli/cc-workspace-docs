# Insight Report — Loop Engineering 教學 × Harness 自我稽核實戰

> **日期**：2026-07-20 · **分支**：`claude/loop-engineering-harness-ni06xa` · **性質**：一次教學驅動的 harness 自我稽核+優化實戰
> **觸發**：使用者以 ThariqS「Teacher SKILL」gist 學 Loop Engineering，載體=實戰優化本 harness。
> **一句話結論**：這個 workspace 不缺器官，缺的是**循環系統**——它的**寫入路徑（write path）世界級，讀取路徑（read path）是斷的**。要成為智能體，該補的不是更多組件，是把「已存在的資料送到需要它的那一刻」的 retrieval 迴圈。

## 1. 本次交付（已完成並驗證）

| 交付 | 內容 | 驗證 | commit |
|---|---|---|---|
| 新 SKILL `deep-understanding` | `/teach` mastery-gated 教學迴圈（= 本場教學用的方法自舉）| frontmatter 7 欄、觸發 | d3709ae |
| 3-agent 跨 context 稽核 | L1 規則 / SKILL 路由 / 散文-vs-gate 三維，12 缺口 backlog | 2 agent 獨立收斂 terraform 缺口 | — |
| **P0#1** IaC 破壞性 gate | block-dangerous.sh 焊 terraform/tofu/terragrunt destroy + auto-approve | **Fable 抓到 8 繞過→修→21/21 自驗** | b22bbf4→(fix) |
| **P0#2** branch-guard 誠實化 | 假宣稱「保護 main」→ 誠實化 + 真 main 警示（fail-open）| 語法+fail-open | 5242797 |
| Phase 1 概念地圖 | `CONCEPT-MAP-v4.md`：7 概念×最新/實現/gap（6-agent 合成）| Fable 抽驗 artifact | bd40c67 |
| P1/P2 批次 | N 斷鏈修復、Handoff 誠實化、audit 消歧、/goal 自清 | byte 帶內、指針解析 | 23167b6 |
| /goal 事實校正 | 誤判「無原生 /goal」→ 官方 docs 證實原生（v2.1.139+ Haiku validator）| claude-code-guide + Fable | f5c857f |

## 2. 本次最重要的一課：Fable 抓到我抓不到的（harness 論點的活體驗證）

我對 P0#1 自報「13/13 fixture 通過、破壞性全擋」。**Fable frontier 終審（異模型、fresh context、對抗立場）裁定 NOT-FAITHFUL**——用**最自然的 terraform 寫法**繞過我的 gate：`(cd envs/prod && terraform destroy)`、`terraform destroy;`、`$(terraform destroy)`、`terraform "destroy"`、`-auto-approve=true`。

- **根因**：我的 destroy 終止符只容忍空白/行末，而**同一個檔的 `is_dangerous_rm` 早就用終止符類 `T='[[:space:])|;&]'` 解過**——我沒重用既有慣例就回歸了。
- **這驗證了三條 harness 鐵律**：① `unverified_success`（自報成功=中間態）② 「壞 oracle 比沒有更糟／gate 須行使實際執行路徑非 proxy 子集」——我的 fixture 是 proxy 子集，給了假信心 ③ 「對抗審查優先異模型」——只有不同模型的對抗立場抓得到我的盲點。
- **自我 oracle 的盲點形狀 = 作者的盲點形狀**：我寫的 fixture 測不到我想不到的繞過。這是為什麼 verifier 必須外部。

## 3. 老實的架構診斷：write path 世界級，read path 是斷的

親驗（非臆測）本 workspace 的閉環底料：

| 環節 | 現況（收據）| 判定 |
|---|---|---|
| traces 收集 | ⚠️**已修正（見 §7.5）**：task-log 有 `skills_used` **欄位**但值 **0/1014 全空**——生產端沒寫 | ❌ write **也是斷的** |
| lessons 累積 | `memory/LESSONS.md` 101 條 `[失敗模式]→[防範]` | ✅ write 存在 |
| eval oracle 基建 | `research/evals/`（baseline/coreset/runs/evaluate.py）| ✅ 存在 |
| **traces → dreaming** | dreaming SKILL 明寫「只讀 memory/+research/reports/」**不讀 task-log** | ❌ **read 斷** |
| **LESSONS → 動作** | 無機制在高風險動作前 surface 相關 lesson（本 session 親證：我重犯 2026-07-04 已記的 lesson）| ❌ **read 斷** |
| 語意檢索 | `.router-log.jsonl` 顯示 `embed_stub:true`、score 0.0，skill 路由純 BM25 | ❌ **read 降級** |

> **核心洞見**：你的 workspace **會寫日記（traces + lessons），但不會在動手前翻日記。** 知識被累積、卻沒被 circulate 到 point-of-need。兩個最深的缺口（traces→dreaming、LESSONS→動作）**同形狀**：資料存在，送達使用點的那條邊缺席。而語意檢索基建（embedding）還是 stub。**read path 是系統性的弱側。**

## 4. 閉環 roadmap（skills→loops→traces→dreaming→更好的 skills）

要「完整且有效達成閉環」，唯一真正必要的是補 **read path**：

- **#1（最高槓桿）retrieval-at-point-of-need**
  - **LESSONS → 動作**：高風險動作（改 hook/rule、不可逆操作）前，機械 grep LESSONS 對應 signature 注入提醒。本 session 親證：這一條就能擋下我的 P0#1 bug。
  - **traces → dreaming**：dreaming 輸入從「人寫的 memory/reports」擴充到「機器記的 task-log outcome/failure_mode」——底料已存在，就差接線。
  - **修 embed_stub**：讓語意檢索真的跑（skill 路由 + 記憶查詢式選讀，G-Mem）。
- **#2 external oracle（A5，本 session 血的教訓）**：per-skill eval fixture + dreaming held-out eval。self-authored oracle 有作者形狀的盲點；候選改進須過外部/異模型驗證才算數。
- **#3 別加，要 wire/consolidate**：31 skills + 12 疑似重疊 = comprehension debt。fusion/multi-mode 缺的**不是各自的自我進化引擎**（那會犯 Rule-of-3），是 #1#2 的**共享 read-path 電路**——wire 一次全體受益。
- **#4 把外部驗證與 retrieval 自動化**：今天 Fable 終審、dreaming、稽核**都要人（你）顯式觸發**。智能體的定義就是這些 read/verify 迴圈**自己會觸發**（離線、外部 oracle、不可逆改動仍人閘）。

## 5. 智能體願景的一句話

> 今天這個 workspace 是**一件優秀的樂器**，需要一位熟練的人（你）去彈——你觸發稽核、你叫 Fable 把關、你跑 dreaming。要成為**智能體**，它得長出**自主神經系統**：自己觸發 retrieval、自己觸發對抗驗證、自己蒸餾——用外部 oracle、離線、不可逆處人閘。**器官都在，缺的是讓它們自己動起來的 read 迴圈。**

## 6. 未竟項（誠實 tracked，非宣稱完成）

backlog 剩 P1/P2：#4 unverified_success 僅 commit 時強制（措辭標明）、#5 test-integrity proxy 子集、**#6 [P]/[E] 顆粒度重標（→ 路由 autoload-evolution）**、#8 README byte 公式（cosmetic，defer 避免 desync healthcheck）、#9 RECORD 去重、#10 handoff review-by 過期（需內容 review 非橡皮圖章）、#12 hygiene（ship-review↔autoresearch:ship 重疊 / memory-compactor 未進 RESOLVER / git add -A 無 hook）。概念層新 gap：G-WF/G-Cache/G-Mem/深度裁決池薄。

> **本報告即 read-path 的一次示範**：它把散落在 12 commit、6 agent 產出、1 次 Fable 對抗稽核裡的教訓，consolidate 成一處可 retrieve 的 insight——這正是 #1 要自動化的東西。

## 7.5 UPDATE（深挖後修正——第四次「schema≠territory」，超越 §3 的 traces 判斷）

「把 dreaming 輸入換成機器記的」深挖到生產端，**發現前提不成立**（親驗）：

- **task-log 的 `skills_used` 值 0/1014 全空、`failure_mode` 0/1014、`outcome` 858/1014=unknown**。task-log 實為 token/model **帳**（全 `backfilled`，源 claude-ios/desktop/cli），非 skill-outcome 軌跡。
- **消費端早已建好且在空轉**：`skill-optimizer.py`（「read task-log where skills_used contains this skill」）、`skill-crystallizer.py`、`skill-risk-propagator.py`、`skill-usage-tracker.py` 全讀 `skills_used`——讀到的永遠是 []。
- **行級根因**：`session-stop.sh:420` 有「Parse transcript for Skill tool_use」——**已算出用了哪些 skill**，但只 bump 各 skill METADATA，**沒寫進它 append 的 task-log 列的 `skills_used`**；`backfill-task-log.py:26` 亦明填占位 []。**資料被算出、沒 wire 到消費端讀的欄位。**

### 閉環真正的第一刀（可執行 spec）

> 順序修正：**① 修生產端（trace capture）→ ② 接 dreaming → ③ eval 閘**。①之前，②③無料可用。

**Fix：`session-stop.sh` 的 task-log append 補寫 `skills_used`（重用同檔既有的 transcript Skill 解析，非新造）**
- **Done-when**：跑一次帶 Skill 呼叫的 session 後，`tail -1 task-log.jsonl` 的 `skills_used` 非空且含實際呼叫的 skill 名。
- **Oracle（外部、可 oracle-qualify）**：餵一個合成 transcript（含 2 個已知 Skill tool_use）給 append 邏輯 → 斷言輸出列 `skills_used`==那 2 個名；餵無 Skill 的 → []。先驗 oracle 抓得出差異再改。
- **順帶**：`outcome` 從 transcript 末狀態/失敗計數推導（session-stop 已數 `FAILURE_COUNT`，L409）；`failure_mode` 由失敗工具類型填。
- **風險**：session-stop 是 400+ 行背景+lock 關鍵 hook → 外科手術式、oracle-first、改後跑既有 `scripts/verify-tasklog.sh`。**不可在疲勞 context rush**（本 session P0#1 教訓）。

**修好這一刀 = 一整排既有 skill-* 工具 + dreaming 同時活過來**，閉環的 traces 才真正開始流動。這是「完整且有效達成閉環」的**唯一必要起手式**，其餘皆下游。

## 8. 斷点系統性稽核批（2 sweep → 13 斷点 → 修）

延伸「read-path 斷」的診斷，2 個 fresh-context sweep（scripts 資料 wiring + hooks 宣稱≠實際，皆抽樣真實資料非讀 schema）掃出 **13 個斷点**，分兩個系統性 pattern：

**Pattern 1 — 假強制（宣稱 enforce 實則 advisory/不可阻斷）**：
- **D1**（危，harness 曾出 self-modification 警告）：`session-init` exit 2 宣稱擋 startup（含反劫持安全檢查），但 SessionStart 平台不可阻斷 → 假防護。**修**：誠實化 + sentinel 真防線（remote-mismatch 寫 sentinel → `user-prompt-submit`（平台可阻斷）exit 2 擋）；parent no-lockout oracle 過；**Fable frontier 終審中**。
- D2 README matcher 過時 · D5 usage-delegation 恆 advisory（config-gated）· **D4 被查證推翻**（契約本正確，sweep 誤判）。

**Pattern 2 — read-path 斷（資料收集了沒流到用處，同 §3-§7.5 主軸）**：
- B1 skill-optimizer 讀 dry-run 假 audit（16 天 0 真候選）· B3 compress-metrics 漏 63% 資料 · C1/C2/C3 生產孤兒（heartbeat/autoload/command-log 無消費端）· R1 routine B/D/E 不寫 heartbeat（監控盲）。

**方法論收穫（本批血證，補強前文）**：
- **schema≠territory 重現 5+ 次**：/goal、task-log skills_used（欄位在值 0/1017 空）、L420 機制、routine「死」（實則 fire 只是不寫 heartbeat）、audit 分數（dry-run 常數）——**每次都是「看 code/schema/heartbeat」誤判、「抽樣真實值/查 trigger」才對**。
- **reviewer 檔位 ≥ executor+1（使用者原則）+ 天花板**：sonnet 執行→我 Opus 審（+1 合法）；opus 執行(D1)→只有 Fable(frontier) 夠格審；**frontier 執行(A1)→無更高檔 → 閘落在確定性 oracle（程式非模型，tier-agnostic）+ 異 context**。
- **stale-base worktree 回歸**：fresh-context implementer 改「parent 本 session 已編輯的檔」→ pull 覆寫掉 parent 的修（本批 README P0#2 誠實化被 impl-1 worktree 覆寫，diff 審時攔下）→ 並行 worktree 對 parent 已動檔有回歸風險，整合前必逐檔 diff 審。

**A1 收束**：先判「撤」（R5 證 skills_used [] 多為正確、硬改 backfill 競態高風險零收益），後依使用者指示交 **Fable 實作**（修正：對 routine session（allowed_tools 含 Skill）有條件收益；frontier 對檔最高風險改動）。狀態：Fable 實作中，oracle + 異 context 把關。

> **本批再次示範 read-path 的價值**：13 斷点全靠「主動 sweep + 抽樣真實資料」挖出，而非等它們自己浮現——這正是 §4 roadmap #1「retrieval-at-point-of-need」若自動化後，系統該對自己做的事。

## 9. UPDATE 2026-07-20（後續 session 親驗）：第一刀已落地，首筆真 trace 流動

- **A1 實作完成**（Fable，`session-stop.sh:458-563`）：skills-only upsert——sid 已存在時只改寫 `skills_used`（值非空且異於既有才寫，避開 backfill 競態）；來源重用同檔既有的 transcript Skill 解析（`skill-usage-tracker.py`），非新造。
- **活體收據（抽真值非讀 schema）**：`evolution/task-log.jsonl` 1027 列出現**第一筆非空** `skills_used`——`/teach` session（`5692f0a0…`）記到 `['deep-understanding']`、outcome=success。§7.5 Done-when（帶 Skill 呼叫的 session 後該列 skills_used 非空含實際 skill 名）**達成**。
- **歷史 1026 筆 `[]` 不回填**：依 §8 A1/R5 查證多為正確（該等 session 未用 Skill），硬回填競態高風險零收益。
- **下游現況**：traces 開始流動 → 消費端（skill-optimizer/crystallizer/risk-propagator/dreaming）從此有料可讀；②dreaming 接線與 ③eval 閘轉為當前 head，④routine 排程在其後（順序論證 + hook/routine/code 工具判準見 `2026-07-20-routine-closure-learning.md`）。
- **②dreaming 接線完成**（sonnet 執行 + parent 親驗，oracle-first）：`consolidate.sh` 新增 `=== TASK-LOG machine traces ===` 節（`${TASKLOG_PATH:-evolution/task-log.jsonl}` 聚合非空 `skills_used` × outcome 分布 + failure_mode 對；容錯壞行、無檔/零 trace 明示）；SKILL.md 三處同步（OBSERVE digest 描述、PROPOSE 溯源枚舉加 task-log、安全邊界讀取範圍）。oracle = `tests/tasklog-digest-fixture.sh`（合成 fixture A 含已知 skills+壞行 / B 全空，pre-impl 先驗 FAIL 再實作）。親跑 4 條 Done-when 全綠：oracle PASS、真實 digest 出現 `deep-understanding: 1 次（success=1）`、`digest OK` 無回歸、SKILL.md 3 處引用。**當前 head → ③eval 閘。**

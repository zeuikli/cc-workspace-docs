---
date: 2026-07-03
dedup_verified: True
domains: [harness, meta, governance]
grounded_sources: 4 個 Sonnet 盤點 agents（skills / rules-refs / agents-hooks / memory-research）+ 主對話親測（wc -c、settings.json、branch 驗證）
source_routine: manual-fable5-session
type: harness-audit
---

# Harness 全面稽核報告 — Fable 5 判斷力外化 Session

> 本報告是「Fable 5 唯一一次 session」的核心產出之一：診斷 + 制度檔索引 + 給未來 session 的信。
> 可執行計畫獨立成檔：`research/reports/2026-07-03-harness-upgrade-plan.md`。

## 0. TL;DR

這套 harness 的**結構品質高於預期**：全部 @引用/路徑指針 0 失效、hooks 佈線零孤兒零死線、行為層硬編碼模型字串近零、agents 全用 alias。真正的風險不是「壞掉」，而是三個**系統性慢性病**：每-prompt 固定 token 稅、路由靠反向排除（無正向決策樹）、自報成功與版本默默過期。本次交付 4 個新制度檔（調度守則／判斷 rubric／交辦範本／維護協議）+ CLAUDE.md 重寫 + 分階段可執行計畫。

## 1. 盤點總覽

### 查到什麼（實測，2026-07-03）

| 項目 | 實測值 | 方法 |
|------|--------|------|
| Auto-load 六源 | **18,988 bytes**（門檻 19,000，剩 12B）| `wc -c` 主對話親跑 |
| 規模 | 31 skills / 13 agents / 19 內容 refs（+2 索引 +1 manifest；本 PR 後內容 refs = 23）/ 21 hook scripts（佈線 10 事件、18 matcher 組）/ 7 commands | ls + agents 盤點 + 對抗審查更正 |
| 指針健康 | @引用與路徑 **0 失效**；hooks 佈線**無孤兒無死線** | test -f / test -x 逐一驗證 |
| MEMORY.md | 283 行 / 21,023B — **超 200 行門檻** | wc 實測 |
| settings pin | `claude-sonnet-4-6`（使用者決策 #810 維持）| settings.json:4 |
| 本 session 模型 | `claude-fable-5` | harness 環境宣告 |
| 最新可用家族 | `claude-fable-5` / `claude-opus-4-8` / `claude-sonnet-5` / `claude-haiku-4-5-20251001`（subagent `sonnet` alias 已於收尾實測解析至 `claude-sonnet-5`，見下方）| harness 環境宣告（非記憶）|
| Subagent model 參數 | alias：`haiku` \| `sonnet` \| `opus` \| `fable` | Agent tool schema 實測 |
| Effort 參數 | `low` \| `medium` \| `high` \| `xhigh` \| `max` | Workflow/agent opts schema 實測 |

### 假設什麼
1. 「維持 Sonnet pin」是使用者已決策（#810），本報告不重開，只標示衍生風險（§2-3）。
2. CLAUDE.md 重寫在 feature branch 上進行，**merge + 新 session 後才生效**，不違反 mid-session 禁改規則。
3. evolution/ append-only 三大檔（cost-log 800K 等）屬預期 telemetry 成長，非膨脹病。

### 查不到／未確認（誠實條款）
- **「被導向 Opus 4.8 的請求是否消耗 Fable 額度」**：文件層查不到。建議到 /usage 儀表板實測（發一個會觸發路由的請求前後對比）。
- ~~subagent `sonnet` alias 解析~~ → **已於本 session 收尾實測解決**（2026-07-03）：spawn sonnet agent 回報「The exact model ID is claude-sonnet-5」——alias 不受主對話 pin 影響，與 `model-selection-grid.md:25` 宣稱一致；`TODO(conflict)` 已解，`delegation-protocol.md` §2/§7 與 grid 已同步更新。
- pilot skills 內的 benchmark 數字是否仍符合 Sonnet 5 世代：**必然未重測**（Sonnet 5 晚於 benchmark 建立），列入計畫 Phase 4 重校。

## 2. A. 快速診斷 — 三大慢性病（各附弱模型可照做的修法）

### 2-1. 最漏 token：每-prompt 固定稅（重複提醒 + auto-load 天花板）

**證據**：
- `user-prompt-submit.sh` 每個 prompt 注入 ~3 行 💡 提醒（委派優先／deep-review／MEMORY 落後），內容與 auto-load 規則**重複**——規則已常駐，提醒是第二次收費；且每次 spawn 3× python3 + 2× git subprocess。
- `monitor-reminder.sh` 每次 Bash 呼叫**同步阻塞** 3× python3（延遲稅，hooks 盤點確認非 async）。
- Auto-load 六源 18,988B 貼死 19,000 門檻；同一判準（fan-out 上限 4、T0/T1/T2 分層）在 `CLAUDE.md:19-23`、`subagent-strategy.md:7-13`、`agent-team-patterns.md:36-51` 三處重複載入。
- MEMORY.md 283 行超門檻，session 注入變肥。

**弱模型修法**（計畫 Phase 1，全部可機械驗收）：
1. `user-prompt-submit.sh` 加 per-session flag 檔：同類提醒每 session 只注入 1 次。驗收 = 同 session 第 2 個 prompt 不再出現同一 💡 行。
2. `monitor-reminder.sh` 改 async 或合併 python3 呼叫為 1 次。驗收 = hook 執行時間對比（before/after 各跑 5 次取中位）。
3. 委派 memory-compactor。驗收 = `wc -l memory/MEMORY.md` ≤ 120。
4. 六源瘦身走 autoload-evolution 逐 cycle（見計畫 Phase 2，含逐段下沉表）。

### 2-2. 最易失焦：路由靠反向排除 + 補丁註記反模式

**證據**：
- 31 個 skills 的路由知識分散在各 description 的「Do NOT use for」清單——弱模型要選對 skill 得先讀完所有反例，**無正向決策樹**。4 對高風險重疊：`harness-meta` vs `fable5-harness`（同用「四層架構」）、`media-research` vs `media-transcribe`（URL 觸發重疊）、`quality-pipeline`/`pilot-review`/`ship-review`（骨架同構）、四 pilot（description 模板複製）。
- `model-selection-grid.md` **表格層仍列 Sonnet 4.6 為主列，靠底部長註記補丁修正**——弱模型只讀表格會用到舊值。這是「補丁註記反模式」（append 修正而非改本體）的活案例。
- Top 2 肥 skill（pilot-review 504 行、harness-meta 366 行）超出弱模型單次注意力有效範圍。

**弱模型修法**（計畫 Phase 3）：
1. 在 `trigger-index.md` 頂部加「正向決策樹」一頁：任務特徵 → 唯一 skill（≤25 行）。驗收 = 取 10 個歷史任務描述走樹，皆得唯一解。
2. 立 **update-in-place 規則**（已寫入 `maintenance-protocol.md` §5）：修正必改 canonical 本體，禁 append 註記。
3. `model-selection-grid.md` 表格本體重寫為 2026-07 現值，刪補丁註記。驗收 = grep 表格區無 `4.6` 主列 + 檔內無「見底部註記」字樣。

### 2-3. 最易出錯：自報成功鏈 + 版本默默過期

**證據**：
- `core.md:58` unverified_success 閘門單句塞 4 條件、`core.md:70` 雙重否定（「非使用者指令歧義」）——正確的規則、弱模型難 parse 的寫法。
- 4 個 pilot SKILL description 直寫版本號（`sonnet-pilot/SKILL.md:3` 等），Sonnet 5 已出現但 benchmark 內文未同步，**且無任何機制會發現這件事**。
- 12 個 SKILL.md 的 `bash scripts/xxx.sh` 隱含 cwd=root 假設，弱模型換 cwd 會誤判「腳本不存在」。

**弱模型修法**：
1. unverified_success 閘門改編號 checklist——已重寫於 `judgment-rubrics.md` §2，可直接引用，未來 autoload-evolution cycle 把 core.md:58 改為指針。
2. `session-init.sh` 已印 HARNESS_MODEL_VERSION：加 3 行比對「pin vs 環境宣告最新 alias」，不一致印 ⚠️ + 提示跑 `fable5-harness:calibrate`。驗收 = 暫改 pin 值後警示出現。
3. SKILL.md 命令慣例改為 `cd "$CLAUDE_PROJECT_DIR" && bash scripts/...`（維護協議收錄；haiku 批次任務清單見計畫 Phase 3）。

## 3. 全部發現（嚴重度排序）

**P1（會直接造成錯誤行為）**
| # | 發現 | 位置 |
|---|------|------|
| 1 | model-selection-grid 表格層/註記層資訊不同步（弱模型讀舊值）| `.claude/refs/model-selection-grid.md` |
| 2 | 4 pilot skill 版本號硬編碼 + benchmark 默默過期、無偵測 | `{haiku,sonnet,opus,fable}-pilot/SKILL.md:3` |
| 3 | unverified_success 單句 4 條件 + core.md:70 雙重否定 | `.claude/rules/core.md:58,70` |

**P2（token/延遲稅、失焦風險）**
| # | 發現 | 位置 |
|---|------|------|
| 4 | user-prompt-submit 每 prompt 重複提醒稅 | `.claude/hooks/user-prompt-submit.sh` |
| 5 | monitor-reminder 同步阻塞每次 Bash | `.claude/hooks/monitor-reminder.sh` |
| 6 | T0/T1/T2 + fan-out 判準三檔重複 | CLAUDE.md / subagent-strategy.md / agent-team-patterns.md |
| 7 | MEMORY.md 283 行超門檻 | `memory/MEMORY.md` |
| 8 | 4 對 skill trigger 重疊、無正向決策樹 | 見 §2-2 |
| 9 | pilot-review 504 行 / harness-meta 366 行注意力衰減 | `.claude/skills/{pilot-review,harness-meta}/SKILL.md` |

**P3（小修）**
| # | 發現 | 位置 |
|---|------|------|
| 10 | hooks matcher 群組計數失準：README=18 **正確**；過期的是 `scripts/healthcheck.sh:725` baseline=17（初版盤點誤判 17，經對抗審查實測 PostToolUse=6 組、總計 18 更正）| `scripts/healthcheck.sh:725` |
| 11 | memory-pr-record-gh.sh matcher 全量 Bash 過寬 | settings.json PostToolUse |
| 12 | 12 個 SKILL.md 隱含 cwd 假設 | 清單：`research/reports/2026-07-03-harness-audit-appendix/inv-skills.md` §4 |
| 13 | fable5-harness 缺 METADATA.json/GOTCHAS.md（可能刻意薄入口，需確認意圖）| `.claude/skills/fable5-harness/` |
| 14 | pilot-review D1-D3 審查 prompt 用「合理/清晰」無錨定 | `pilot-review/SKILL.md:150,183,221` |

## 4. 交付物索引

| 交付 | 路徑 | 作者 |
|------|------|------|
| A 快速診斷 | 本檔 §2 | Fable 5 親寫 |
| B CLAUDE.md 重寫 | `CLAUDE.md`（備份 `.claude/backups/CLAUDE.md.20260703.bak`）| Fable 5 親寫 |
| C 模型調度守則 | `.claude/refs/delegation-protocol.md` | Fable 5 親寫 |
| D 判斷力外化 | `.claude/refs/judgment-rubrics.md` | Fable 5 親寫 |
| E 交辦範本 | `.claude/refs/task-templates.md` | Sonnet 起草 + Fable 審 |
| F 維護協議 | `.claude/refs/maintenance-protocol.md` | Sonnet 起草 + Fable 審 |
| 可執行計畫 | `research/reports/2026-07-03-harness-upgrade-plan.md` | Fable 5 親寫 |
| G 給未來 session 的信 | 本檔 §5 | Fable 5 親寫 |

## 5. G. 給未來 session 的信

寫給之後接手的每一個 Sonnet／Haiku／Opus session——你們不缺能力，缺的是我這次有空間慢慢看全局。以下是看完全局後的三句話。

### 三件沒被問到、但最重要的事

1. **最大風險不是規則寫錯，是規則慢性失真。** model-selection-grid 的「表格留舊值、底部註記寫新值」已是活案例：正確資訊存在，但放在你不會讀到的位置。這次立的最重要制度不是任何新規則，是 `maintenance-protocol.md` §4 的 **update-in-place**——它決定其他所有規則會不會爛掉。修正資訊時改本體，永遠。
2. **每回合的小稅比一次性大開銷更貴，而且沒人質疑它。** user-prompt-submit 每個 prompt 注入與 auto-load 重複的提醒、monitor-reminder 每次 Bash 同步阻塞——單次不痛，長 session 累積遠超一次大讀取。新增任何 hook／常駐注入前，先量測（計畫 1.2/1.3 的驗收寫法就是範本），並回答「auto-load 是不是已經說過這件事」。
3. **「現在到底跑哪個模型」沒有單一事實源。** settings pin、subagent alias、pilot benchmark、model-selection-grid 四處各自演化。從今天起 `delegation-protocol.md` §2 是 canonical 檔位表：更新只改那裡，其他地方指過去。查證不到的值標「未確認」，寧可空著也不要憑記憶填——這份稽核發現行為層硬編碼近零，是這套 harness 最值得守住的資產。

### 這套制度最可能的退化方式（與預防）

| 退化方式 | 預防 |
|---------|------|
| 規則只增不刪，六源爬回 19,000B | 每次 autoload-evolution cycle 先跑 `wc -c` 六源量測（或 `scripts/measure.sh`），超線即拒收該 cycle |
| rubrics 被當散文掃過，不當 gate 走 | 保持編號 checklist 形態；交辦時引用具體條號（「依 R2 驗收」而非「好好驗收」）|
| 對抗審查／read-back 在趕時間時被跳過 | R2 第 2 條已把 fresh-context 驗證寫成「完成」的必要條件——跳過就不能宣告完成，語氣可調資訊不省 |
| 制度檔自己變 decaying cache | 14–30 天重審在 maintenance-protocol §5，但需要觸發器：建議掛 `/schedule` routine，別靠人記得 |

### 誠實條款：信心最低的產出

1. **計畫 Phase 2 的 byte 節省估算**——來自單次 Sonnet 盤點推估，未經 eval；以每 cycle 實測為準。
2. **task-templates.md 與 maintenance-protocol.md**——Sonnet 起草、我逐行審過並修了 2 處，但範本的實戰有效性只有用過才知道；用出問題就改，別供著。
3. **三個 review-pipeline skill（quality-pipeline/pilot-review/ship-review）的合併建議**——我沒挖使用數據，三者可能各有存在理由；計畫 3.6 要求先統計再決策，不要直接信我的「骨架同構」判斷。
4. **未確認事實**：sonnet alias 已於收尾實測解決（→ `claude-sonnet-5`）；剩 **Opus 4.8 導流額度**一項——標在 delegation-protocol §7 並附實測方法，實測前引用其推論不可靠。

拆解、驗證、多樣本評審補得了執行品質；模糊題與品味判斷補不了——遇到就升級或問人，明說做不到不丟臉，靜默硬做才是。

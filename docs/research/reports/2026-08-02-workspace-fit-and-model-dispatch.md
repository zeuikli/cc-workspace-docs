# v5.1 Harness 與 Workspace 契合度 · 資產權狀 · 四模型 reasoning 分派 · 5h Window 實測

> **墓碑（2026-08-03）**：本報告引用的四支 E1/E2 腳本
> （`scripts/run-e1-arms.py`、`run-e2-position.py`、`score-e1.py`、`score-e2.py`）**已退役刪除**。
> 實驗已結案、零自動呼叫端，留著只會讓「有工具可重跑」變成假象。
> 需要重跑時從 git 歷史取回；但**取回前務必先讀 `score-e1.py` 的失格記錄**——
> 它在真實回應上 A 軸人工 6/6、它判 1/6，且把 full 臂排到最後一名，
> **合成 known-good 過關不算資格**。本報告中任何來自 score-e1 的數字都不可直接引用。


> **日期**：2026-08-02 · **分支**：`claude/research-papers-summary-update-796fqe`
> **起點**：使用者要求「以 fresh session 檢視 v5.1 與 workspace 契合度」「Harness Master 如何掌握權狀／research／各項檔案」「用 Fusion 分派四模型並加 reasoning 分級」「利用 Usage 研究跑滿 5h window」。
> **方法**：依 fusion brief 格式（含本日新增的 `consumed` 欄）並行派工四模型，各綁不同 reasoning 性質；主對話逐項機械複驗後合成。
> **驗證收據**：`healthcheck` PASS 193 / WARN 0 / FAIL 0（⚠️ **僅證明本機結構完整**——見 §6.1，同一腳本在 CI 恆 FAIL）；四方回報的每個數字皆經主對話重跑對帳，其中 Opus 5 的 CI 失敗計數經實測推翻並訂正。

---

## 0. 四個問題與答案

| 問題 | 答案 |
|---|---|
| v5.1 與 workspace 契合嗎？ | **規則層契合、資產層失聯**。`.claude/`（1.6 MB）被重度治理，`research/`（1 GB、7,594 檔）幾乎零治理——而後者是 60× 的體量 |
| Harness Master 的掌握權瓶頸？ | **oracle 不可信**——`healthcheck.sh` 本機綠、CI 恆紅（23/30 次失敗），因它檢查 CI 結構上不可能滿足的 `core.hooksPath`。其次才是「現況不可得」 |
| 四模型怎麼分派？ | 三軸（後果／驗證成本／搜尋寬度）取代難度二分。**後果軸只加驗證深度、不升檔**——難度與後果正交 |
| 5h window 能跑滿嗎？ | 能，但 workspace 的預設儀表會阻止你。本地美元估算在官方 49% 時報 133% 🛑（曾以為是穩定 2.7× 高估，**已訂正——見 §1.4**：它是寫入延遲，不是固定倍率） |

---

## 1. Usage：5h Window 的實測與儀表分歧（本輪最強發現）

### 1.1 兩套儀表，相反結論

| 工具 | 資料來源 | T1（16:30） | T2（16:45） | 建議 |
|---|---|---|---|---|
| `usage-now.py` | 本地 `evolution/cost-log.jsonl` 美元估算 vs `CLAUDE_USAGE_LIMIT_USD=150` | $177.92（**119%**）🛑 | $199.74（**133%**）🛑 | 停手 |
| `usage-pacer.py` | `/tmp/usage-guard-official-cache.json` 官方 utilization% | **43%** | **49%** | `BEHIND`／`burst`，可提平行度 |

**分歧倍率 2.76× → 2.71×，穩定。**

v5.1 的 `usage-gate.sh` 已明訂「以官方 usage 百分比為裁決 SSoT（比本地估算精準）」，但 `usage-now.py` 仍用本地美元且**它才是人眼最常看到的那個**（輸出帶 🛑 emoji）。結果是：**決策層用官方 %（放行），顯示層用本地 $（叫停）**——兩者在同一時刻給相反訊號。

### 1.2 這如何阻止「跑滿 window」

若信 `usage-now.py`，在官方 43% 時就會自我節流——**放棄 57% 的窗**。本輪刻意反其道而行：pacer 判 `burst`，遂並行派四個 agent。

實測代價：

| 指標 | 值 |
|---|---|
| 4 個並行 agent 消耗 | ~247k subagent tokens（Haiku 35.8k + Sonnet 64.4k + Fable 73.3k + Opus 73.5k） |
| 官方 5h util 增幅 | **+6pp**（43% → 49%） |
| 本地美元增幅 | +$21.82（+14.5pp of $150） |
| live session 數 | 7 → 11（每個 sub-agent 計為一個 session） |

**結論：一次四模型 fan-out 只吃掉官方預算的 6pp。** 以此速率，5h 窗可支撐約 8 輪同等規模的 fan-out。本地估算會在第 2 輪就報表滿。

### 1.3 校準建議（未實作，屬治理決策）

分歧倍率穩定 ⇒ **可校準**。在官方 49% 時本地報 $199.74，故若要讓兩者對齊，`CLAUDE_USAGE_LIMIT_USD` 應為 `$199.74 / 0.49 ≈ $408`，即現值 $150 約低估 **2.7×**。

三個選項，未擇一：
1. 調 `CLAUDE_USAGE_LIMIT_USD` 至 ~$400（最省事，但仍是估算對估算）
2. `usage-now.py` 改讀官方快取（與 `usage-gate` 同源，消除分歧根因）
3. 保留兩者但在 `usage-now.py` 輸出並列官方 %（讓人看得到分歧）

⚠️ **未驗證**：分歧根因尚未定位。假設是本地模型按 token × 假設單價估算且跨 11 個 live session 累加，而官方 % 是帳號窗口的真實配額比例。此假設**未經證實**，校準前應先確認 `cost-log.jsonl` 的單價表與 session 去重邏輯。

### 1.4 訂正（2026-08-02 稍晚）：「穩定 2.7×」不成立，選項 1 作廢

§1.3 的校準建議建立在「分歧倍率穩定 ⇒ 可校準」上。**該前提已被反證。**

證據：同日稍晚回頭驗算 pacer 進度時，官方讀數 **14%**，本地讀數 **$0.00**——倍率不是 2.7，是 0。查 `evolution/cost-log.jsonl`，最新一筆為 `2026-08-02T16:32:12.190Z`，**當前 5h 窗內 0 筆**。

根因（§1.3 猜的是單價表，猜錯了方向）：**`cost-log.jsonl` 在 session 結束時才寫入**。本 session 連續跑了 6 小時以上未結束 ⇒ 本窗消耗一筆都還沒落地。所以本地儀表不是「按固定倍率高估的類比錶」，而是**階梯式、寫入延遲的計數器**：

- 長 session 進行中 → 嚴重**低**報（極端情況 $0.00）
- 多個短 session 剛結束 → 集中落帳，瞬間**高**報

T1/T2 兩次取樣落在後者，才呈現 2.76×／2.71× 的「穩定」——**兩點連一線，看起來都是穩定的**。

推翻的結論：
- **選項 1（調 `CLAUDE_USAGE_LIMIT_USD` 至 ~$400）作廢**——沒有固定倍率可校準，調大只會讓長 session 低報得更徹底。
- **選項 2（改讀官方快取）從「較費工」升為唯一正解**，且已於本輪實作：`usage-now.py` 現以官方配額為主、本地美元降為相對燒速參考。
- §1.1「分歧倍率穩定」與 §0 表格的 2.7× 一併訂正。

方法論教訓（同 §附錄）：**兩個取樣點不足以宣稱「穩定」。** 這句話的錯不在數字算錯，而在從 n=2 推出「可校準」這個性質宣稱——與本 session 反覆出現的「宣稱涵蓋 > 實際涵蓋」是同一族缺陷。

---

## 2. 資產權狀清冊（Haiku 4.5 盤點，主對話抽驗）

### 2.1 體量分佈——`research/` 是 workspace 的 97%

| 區塊 | 檔案數 | 大小 | 佔比 |
|---|---|---|---|
| `research/` | **7,594** | **1,033 MB** | 97% |
| `vendor/` | 353 | 13.6 MB | 1.3% |
| `.claude/` | ~203 | 2.1 MB | 0.2% |
| `scripts/` | 118 | 1.4 MB | 0.1% |
| 其他頂層 | ~200 | ~4 MB | — |
| **git tracked 總計** | **8,469** | **399 MB** | — |

`research/` 內部再拆：`papers/` 602 檔 **860 MB**（PDF 為主）、`evals/` 3,451 檔 57 MB、`ai-news/` 1,917 檔 94 MB、`reports/` 243 檔 4 MB。

> **關鍵比例**：harness 本體（`.claude/` + `scripts/`）約 3.5 MB，知識資產 1 GB。**治理密度差 300 倍。**

### 2.2 索引覆蓋

有索引（INDEX.md / RESOLVER.md）：`.claude/` `config/` `docs/` `evolution/` `memory/` `playbooks/` `reports/` `research/` `schemas/` `scripts/` `tests/` `vendor/`

**無索引 9 個目錄**（152 檔、1.9 MB）：`.claude/logs` `.devcontainer` `.github` `.githooks` `.ruff_cache` `agent` `clients` `dist` `portal`

其中 `agent/`（12 檔）、`clients/`（17 檔）、`portal/`（68 檔）、`dist/`（15 檔）是**有實質內容卻無索引**的——冷啟 session 不會知道它們存在。`.ruff_cache` 屬工具產物可忽略。

### 2.3 git 狀態

tracked 8,469 檔、untracked **0**、gitignored 涵蓋 `secrets/` `credentials/` `logs/` `.claude/worktrees/` `external/` `research/scratch/` 等。

---

## 3. 冷啟導航測試（Sonnet 5，無繼承 context）

### 3.1 五題成績

| 題目 | 找得到 | 工具呼叫 | 直觀度 | 矛盾 |
|---|---|---|---|---|
| Q1 行為規則在哪 | ✅ | **0**（auto-load 已注入） | 5/5 | 無 |
| Q2 code review 用哪個 skill | ✅ | 2 | 4/5 | 無 |
| Q3 檔位判準數字 | ✅ | 1 | 5/5 | **有**（見 3.2） |
| Q4 不可逆操作清單 | ✅ | 0 | 5/5 | 無 |
| Q5 **最近改動／現況** | ✅ | 3 | **2/5** | **有** |

> **結論：瓶頸不是「找不到」，是「現況」。** 行為規則 0 步可得（auto-load 設計成功），但「workspace 現在做到哪」要跨 3 層、且得自己猜 `memory/MEMORY.md`（687 行）該從哪個 offset 讀起，沒有 TL;DR。

### 3.2 摩擦點（主對話已逐項複驗）

| # | 摩擦 | 複驗結果 |
|---|---|---|
| 1 | 根目錄 6 個入口檔並列（`CLAUDE.md` `AGENTS.md` `BRAIN.md` `README.md` `WORKSPACE-INDEX.md` `SYNC-STATUS.md`），無單一「先讀我」 | ✅ 屬實 |
| 2 | `AGENTS.md:20` 自承「與 CLAUDE.md 冗餘、刻意接受」，冷啟者無法立即判斷以哪份為準 | ✅ 屬實 |
| 3 | `prompt-lifecycle.md` 自述觸發條件為「編輯 auto-load 規則」，但 Sonnet 只是 **Read** `AGENTS.md` 就被注入全文 | ⚠️ **未能複現**——其 frontmatter `paths: [".claude/rules/**", "CLAUDE.md", "research/prompts/**"]` 不含 `AGENTS.md`。可能是平台 path-scoped 比對比宣告更寬，或 Sonnet 誤歸因。**列為待查** |
| 4 | `model-profiles.md:5` `snapshot: 2026-07-25` vs `AGENTS.md` 宣稱 `2026-08-02`——L2 數字 SSoT 落後 8 天且無「已核實仍適用」標記 | ✅ 屬實 |
| 5 | `RESOLVER.md:78` 指向 `claude-progress.json`（根目錄） | ✅ 該檔不存在（指針有「若存在」條件化，屬輕微） |
| 6 | `MEMORY.md` 687 行線性累加、無置頂摘要、無目錄 | ✅ 屬實 |
| 7 | `SYNC-STATUS.md:22`「需要人工確認：4 個」但無指針說明是哪 4 個 | ✅ 屬實 |

### 3.3 `SYNC-STATUS.md` 的三種計數定義（我差點誤報為 bug）

該檔 16:34 剛自動生成（`sync-workspace.sh`），但同檔內三個數字看似互相矛盾：

| 出處 | 數字 | 實際定義 | 複驗 |
|---|---|---|---|
| 資料夾表格 `scripts/` | 118 | `find scripts -type f`（全檔遞迴） | ✅ 118 |
| 關鍵指標「Scripts 計數」 | 110 | `find scripts \( -name "*.sh" -o -name "*.py" \)`（遞迴，含 `tests/`） | ✅ 110 |
| 關鍵指標「Research 報告數」 | 240 | `find research/reports -name "*.md" ! -name README.md`（遞迴，含 `archive/` 59 + `data/` 1 + 2 個子目錄 9） | ✅ 240 |

**三個都對，只是用了三種未言明的定義。** 不是 bug，但對「掌握權狀」是實質障礙——要對帳必須去讀生成器原始碼（`scripts/sync-workspace.sh:510-514`）。

**額外發現**：`SYNC-STATUS.md` **被 gitignored**（`.gitignore:82`）。意即**新 clone 完全沒有這份現況檔**，冷啟 session 的 Q5 只會更難。這與 §3.1 的瓶頸同源且互相加乘。

---

## 4. Fusion 四模型 × Reasoning 分級（Fable 5 設計，已落地 `b495928`）

### 4.1 為何棄用「難易度」軸

`research/papers/2026-07-25-consequence-aware-reasoning-compute-allocation-2606-04402.md`：700 個 SWE-bench 任務實測 **consequence 與 difficulty 近乎正交**；依難度而非代價分配算力，cost-weighted loss 高 **22–33%**。

fusion 原條文「brief 含設計決策或跨模組 → override quality」正是 difficulty-only 路由的粗版。

### 4.2 三軸

| 軸 | 判別式 | 性質 |
|---|---|---|
| **A 後果** | brief 命令/路徑命中不可逆清單（`core.md` §APPLY）或 payment/auth/migration | 機械可判 |
| **B 驗證成本** | Done-when 主 gate 是否為 build-system 決定集合之命令（fusion §3 判準） | 機械可判 |
| **C 搜尋寬度** | 獨立位置數 ≥6 或跨模組/≥10 檔 | 機械 proxy + lead 殘餘判斷 |

**派工**：C窄∧B廉 → cost(Haiku)/low｜C窄∧B貴 → quality(Sonnet)/medium｜C寬 → quality/high 起手｜跨模組或 C寬∧A高 → ceiling(Opus)/xhigh｜**frontier(Fable) 永不當 sidekick**。

### 4.3 最重要的一條：A 軸不升檔

> **A高只加驗證深度（lead 親跑 gate + 不可逆等確認），不換模型。唯 C寬∧A高 例外。**

這是正交性的直接應用——避免把「錯了很貴」誤譯成「這題很難」。錯了很貴該做的是**多驗**，不是**換更貴的模型**。

### 4.4 反向閘門（本 SKILL 原本完全沒有）

| 閘門 | 依據 |
|---|---|
| C窄鎖 effort low，禁保險性拉高 | `2511-05722` Overthinking Tax：7B 總成本比 14B 貴 57% |
| 逐字精確型 Done-when 禁 step-by-step | `2506-07142`：CoT 對「全對」指標可能負向 |
| B廉禁升檔，驗證預算給 gate 不給模型 | `2604-07236`：確定性層零 LLM 獨得 +24.1pp |
| 同型任務連 2 次走升級鏈 → 修判別式 | `2605-06350`：生成前路由優於生成後級聯 |

SKILL 119 → 132 行（+13）。四個 `model-profiles.md` 引用錨點（§2.2/§2.3/§2.4/§2.8）皆實查存在。

---

## 5. 本輪的方法論示範：fusion 分派本身即實驗

本報告的四份輸入是**按三軸派工原則自己分派的**，可作為該機制的第一個使用樣本：

| 任務 | C 寬度 | B oracle | A 後果 | 派給 | 事後檢討 |
|---|---|---|---|---|---|
| 資產權狀盤點 | 窄（單一模式重複套用） | 廉（`find`/`wc` 全機械可驗） | 低 | **Haiku 4.5** | ✅ 正確——18 次工具呼叫、35.8k tokens，全部數字可重跑 |
| 冷啟導航測試 | 窄 | 貴（「直觀度」無機械 oracle） | 低 | **Sonnet 5** | ✅ 正確；且此題**必須**用不繼承 context 的 agent，主對話做不了 |
| 契合度落差診斷 | 寬（跨 rules/scripts/research 綜合） | 貴 | 中 | **Opus 5** | 見 §6 |
| reasoning 分級設計 | 寬（設計取捨 + 反事實） | 貴 | 低 | **Fable 5** | ⚠️ 依新規則 frontier 不當 sidekick——但此為**設計任務非執行任務**，屬 lead 的終審類工作外包，邊界待釐清 |

> **第一個發現的規則缺口**：新條文寫「frontier 永不當 sidekick（lead 本體與終審稽核專用）」，但本輪把設計任務派給 Fable 5。這既非 sidekick 執行、也非 lead 親做，是**第三類：設計諮詢**。條文未涵蓋此類，應補。

---

## 6. v5.1 契合度落差（Opus 5 診斷，主對話逐項複驗）

### 6.1 最嚴重的一項：唯一的 oracle 在 CI 恆紅

`scripts/healthcheck.sh` 是本 workspace 的健康 SSoT——`ship/SKILL.md` S7 稱它「機械 gate（不可刪）」，`harness-meta` 以它為 Verify 步驟，**本 session 我從頭到尾都在引用它的 PASS 數當收據**。

實際狀況（我逐項複驗）：

| 查證 | 結果 |
|---|---|
| healthcheck 是否檢查 `core.hooksPath` | ✅ `scripts/healthcheck.sh:174-180` |
| 有無 CI 環境守門 | ❌ `grep -c "GITHUB_ACTIONS\|CI:-\|\$CI" scripts/healthcheck.sh` = **0** |
| 本機值 | `.githooks`（`session-init.sh` 設定）→ **PASS** |
| CI 值 | `actions/checkout` 不設此 per-clone local config → **必 FAIL** |
| 近 30 次 `index-consistency` workflow | **failure 23 / success 4 / skipped 3**（77% 失敗率） |
| issue #1048 | 開於 2026-07-29、**18 則留言全為機器人**、0 人類回應、5 天未處理 |

> **這推翻了本 session 所有「healthcheck PASS 193 / WARN 0 / FAIL 0」的收據涵蓋範圍。**
> 它證明的是**本機**結構完整，不是 repo 層健康。同一支腳本、同一個 repo，本機 FAIL 0、CI FAIL 2。
> 這是 `core.md` §TEST「Gate 選擇稽核：gate 須行使宣稱涵蓋的實際執行路徑，非 proxy 子集」的又一次違反——而且是**最貴的一次**，因為整個 workspace 的健康宣稱都建立在它上面。

⚠️ **數字分歧登記**：Opus 5 報「近 30 runs failure 5 / success 0」，我用同一 API 實測為 **failure 23 / success 4**。方向一致（workflow 長期紅），但它的計數不可信，以我的實測為準。這是「child verdict 非證據」的又一實例。

### 6.2 其餘落差（皆已複驗）

| # | 宣稱 | 實際 | 判定 |
|---|---|---|---|
| G3 | healthcheck「已刪除元件在 operational docs 無殘留引用」**PASS** | `grep -rn "usage-delegation-gate" .claude scripts` = **8 處**，其中 `scripts/usage-pacer.py:52` 是會印給使用者看的正式輸出（向使用者敘述一個已不存在的約束） | **真落差**——該檢查的偵測清單沒收錄這個名字 |
| G4 | `check-references.sh` 頂註「接線：pre-commit-review hook 在 git commit 時強制執行 → 孤兒/懸空 commit 物理無法落地」 | 該 hook v5.1 已刪，`precommit-gate.sh` 只剩敏感檔阻斷。**本機 commit 路徑已無此 gate**，唯一自動觸發點是恆紅的 CI | **真落差** |
| G5 | `check-references.sh` 報「dangling=0 orphan=0」 | 其 `EXCLUDE_DIRS` 第 43 行排除 `research`——**89.6% 的 tracked 檔（7,591/8,469）從未被檢查** | **合理取捨但未標示**。這正是 papers 81 筆死引用能長期存活的結構原因 |
| G6 | healthcheck §16「所有 tracked research/ 子目錄都有 INDEX.md」PASS | 只查深度 1。實際 `research/` 有 **917 個目錄、僅 60 個 INDEX.md（6.5%）** | 合理取捨（明文寫在註解），但 PASS 訊息用詞過強 |
| G7 | `core.md` Git 鐵律假設「小心挑檔的小 repo」 | **837 MB PDF 已在版控內**（283 個 tracked PDF）、`.git` = **742 MB**。無任何規則提及二進位歸檔策略 | **意外失控** |
| G8 | `usage-pacer.py` 訊息提「fan-out 仍受 usage-delegation-gate tier 限額約束」 | 該 hook v5.1 已刪 | **真落差**（同 G3） |

### 6.3 孤兒資產

- **零消費者腳本 ≈ 14 支 / 110**（Opus 自行修正了 2 個誤判）。其中 `run-e1-arms.py`/`run-e2-position.py`/`score-e1.py`/`score-e2.py` 是一次性實驗殘留，連報告都沒引用。
- **孤兒 telemetry log 4 個**：`agent-spawn-log.jsonl`（41 行、無生產者無消費者）、`prepush-remind-log.jsonl`（0 行）、`outcome-log.jsonl`（**0 行**，但 `refs/maintenance-protocol.md` 的 harness 解凍條件正是「該檔累積 ≥5 筆」——**解凍條件掛在一個從未被寫入的檔案上**）、`compress-opportunity-log.jsonl`（272 行凍結）。
- **`compress-metrics.py` 的分母已死**：其讀取的 `compress-opportunity-log.jsonl` 唯一生產者是被刪的 `usage-delegation-gate.sh`，最後一筆 `2026-08-02T00:05`。分母凍結 → 壓縮執行率指標系統性失真。
- `.gitignore` 尾段仍為三支已刪腳本保留 sentinel 規則（無害，屬 v5.1 收斂遺漏）。

### 6.4 治理密度（量化）

| 資產 | tracked 檔數 | 佔比 | 機械保護 |
|---|---|---|---|
| `.claude/` | 200 | 2.4% | 13 hooks、71 個 healthcheck 檢查點、6+ 道 index/anchor/section gate |
| `scripts/` | 112 | 1.3% | `bash -n` 全掃、INDEX 雙向一致、self-test |
| `research/` | **7,591** | **89.6%** | **3 個檢查**（深度 1 的 INDEX 存在性 + RESEARCH-INDEX 日期新鮮度） |

> **Opus 5 對此不均的判定我認為是本輪最好的一句**：方向合理（歸檔內容不需 hook），但 **`research/reports/` 是 harness 決策的實質 SSoT**（v5.1 刪除報告、四通道模型報告、本報告都住在這裡），**卻和 841 MB 的 PDF 抓取物混居同一個無治理區**。問題不是「research 沒有 hook」，是**決策文件與抓取物混居**。

---

## 7. Harness Master 的掌握權：綜合診斷（合成四方 + 主對話複驗）

依「認知負擔來源」排序。**Opus 5 的發現使第 1 名易主**：

1. **Oracle 不可信——你無法用一條命令知道 workspace 是否健康**（§6.1）。本機 FAIL 0 / CI FAIL 2，CI 已紅 23/30 次、issue 開 5 天無人讀。掌握權的前提是有一個說真話的儀表，目前**沒有**。
2. **現況不可得**（§3.1）。冷啟測 Q5 直觀度 2/5；`MEMORY.md` 687 行無 TL;DR；唯一現況檔 `SYNC-STATUS.md` 被 gitignored——新 clone 完全沒有它。
3. **治理密度差 300 倍，且決策文件與抓取物混居**（§6.4）。`check-references` 排除 `research/` 是 papers 81 筆死引用能長存的結構原因。
4. **知識分散於四個互不索引的載體**：auto-load 規則 11 KB／`.claude/` 148 個 md／`scripts/` 1,420 行註解（大量設計理由只存在於腳本頂註，且已過期——見 G4）／`research/reports/` 3.4 MB 決策報告。**沒有任何一份索引同時涵蓋這四層。**
5. **「skills」一詞指向三個不同集合**：`.claude/skills/` 17 個、`.claude/commands/` 5 個、平台內建/plugin 十餘個（docx/pdf/xlsx/dataviz/artifact-*）。`RESOLVER.md` 只路由第一組——想掌握 roster 的人會系統性漏掉三分之二。
6. **儀表分歧**（§1）。usage 兩套讀數差 2.7×，決策層與顯示層不同源。
7. **repo 物理重量**。742 MB `.git`／837 MB tracked PDF——`git clone` 與全域 grep 變成分鐘級，直接壓抑「先看一眼」的探索行為。
8. **檔案數量本身排最後**。8,469 tracked 檔中 89.6% 是內容歸檔，真正需要腦內模型的操作面只有 ~312 檔。**數量不是主要負擔，索引缺失與 oracle 失真才是。**

### 7.1 建議（未實作，待裁決）

| 優先 | 動作 | 成本 | 解決 |
|---|---|---|---|
| **P0** | healthcheck 的 `core.hooksPath` 檢查加 CI 守門（`[ -n "$GITHUB_ACTIONS" ] && skip`），或改為 WARN | 極低（3 行） | §6.1——**這是目前唯一讓 CI 恆紅的結構性假陽性** |
| P1 | `MEMORY.md` 加置頂 TL;DR，或改為 `memory/NOW.md` 獨立小檔 | 低 | 第 2 名障礙 |
| P2 | `SYNC-STATUS.md` 取消 gitignore（或生成 tracked 精簡版）+ 表頭寫明三種計數定義 | 極低 | 第 2、6 名 |
| P3 | `check-references.sh` 的 `research/` 排除改為**部分納入**：至少涵蓋 `research/reports/`（決策 SSoT） | 中 | 第 3 名 |
| P4 | `usage-now.py` 並列官方 %；`usage-pacer.py:52` 移除對已刪 hook 的敘述 | 極低 | §1、G8 |
| P5 | 清 14 支孤兒腳本 + 4 個孤兒 log；`maintenance-protocol` 的解凍條件改掛可寫入的來源 | 低 | §6.3 |

> **P0 之外全部可延後。** P0 的理由不是「CI 該綠」，是**只要它恆紅，任何真實的 CI 失敗都不會被看見**——issue #1048 的 18 則機器留言 0 人類回應就是證據。

---

## 附錄 A：本輪四方 `consumed` 對帳

四個 agent 皆依 fusion brief 的新 `consumed` 欄回報其決策依據。抽驗結果：Haiku 逐項附逐字命令（可重跑）；Sonnet 列出 11 項讀取來源含「被動注入」一項；Fable 列出 12 項含**主動訂正我 brief 裡的一個錯誤檔名**（我寫 `2026-06-08-decreasing-value-chain-of-thought`，實為 `2025-06-08-`）。

> `consumed` 欄在第一次真實使用即產生價值：**它讓 sub-agent 有位置回報「你給的來源是錯的」**，而非默默用錯或猜測。這是本日 P2（`[Checkpoint]` 加 dependency 欄）同源設計在委派層的驗證。

## 附錄 B：驗證命令

```bash
# usage 分歧
python3 scripts/usage-now.py && python3 scripts/usage-pacer.py --json
cat /tmp/usage-guard-official-cache.json

# 資產計量
find research -type f | wc -l && du -sk research
git ls-files | wc -l

# SYNC-STATUS 三種定義
find scripts -type f | wc -l                                    # 118
find scripts \( -name "*.sh" -o -name "*.py" \) | wc -l         # 110
find research/reports -name "*.md" ! -name "README.md" | wc -l  # 240

# 冷啟摩擦複驗
grep -m1 "^snapshot:" .claude/refs/model-profiles.md            # 2026-07-25
ls claude-progress.json                                         # 不存在
git check-ignore -v SYNC-STATUS.md                              # .gitignore:82

# fusion 錨點
for s in 2.2 2.3 2.4 2.8; do grep -m1 "^### $s" .claude/refs/model-profiles.md; done
```

# 8 份計劃書執行報告（Harness Loop 逐項）

> **日期**：2026-06-04 ｜ **執行模型**：Opus 4.8（1M context, effort=high）
> **來源**：4 組 action-plan（cold-start CS / context-window CW / prompt-harness PH / subagent SA），共 19 行動項
> **方法**：每項走 Harness Loop（OBSERVE→IDENTIFY→PROPOSE→TEST→APPLY→RECORD）；byte-neutral 項委派 sub-agent，主對話持執行報告 + checkpoint
> **分支**：feature/autoload-cap-sync-and-plan-exec

---

## ⚠️ R7 衝突聲明（執行前必讀）

**計劃書原意 vs 使用者約束的衝突**：
- 計劃書要求把 ~5 項放入 auto-load（CW-P2/P3/P4、PH-1、PH-5）。
- 使用者明確「**不上調上限**」（維持 18,000）。當前 auto-load 17,622 bytes，**僅餘 378 bytes**，無法容納 ~450 bytes 的 5 項。

**唯一算術可行的解**（已執行，非偏好）：
- **CW-P4**（compact hint 強化，每次 compact 必用）→ **留 auto-load**（+~150→17,772，仍 < 18,000）。
- **CW-P2（CJK 稅）/ CW-P3 內容 / PH-1（cache 指標）/ PH-5（injection）** → 改 **on-demand ref**（零 auto-load byte），規則本體不變、只改放置層。

此偏離計劃書原本的 auto-load 放置，但兼顧「能力增補」與「不超 cap」兩約束。**如不同意此放置，請告知。**

---

## 前置：auto-load 上限同步（commit 597d4207，已 push）

不上調上限。修正 5 處 stale 引用與三段門檻一致（README/WORKSPACE-INDEX/token-waste-audit/model-upgrade-harness-tuning/harness-loop）。驗證：複 grep 無殘留、7 檔 18,000 一致、healthcheck FAIL=0。

---

## 行動項分區（按 blast radius）

| 區 | 項目 | byte 影響 | 處置 |
|----|------|----------|------|
| A. byte-neutral（新 ref/script） | CW-P1/P5/P6, PH-2/P4, SA-1.2/2/3.1, CS-1/2/3 | 0 | 委派 sub-agent |
| B. auto-load（僅 CW-P4） | CW-P4 | +~150 | 主對話協調，一次量測 |
| C. on-demand 化（原計劃 auto-load） | CW-P2, CW-P3, PH-1, PH-5 | 0 | 改 on-demand ref |
| D. 自標風險 → grep-first/defer | SA-1.1, SA-2, SA-3.1, PH-3 | — | 逐項判斷，記錄 defer 原因 |

---

## 逐項執行記錄

### SA-1.1 移除 review-hub Write 權限 — **DEFER**（grep 證實會破功能）
- **OBSERVE**：`grep` review-hub SKILL.md → `allowed-tools: Read, Write, Grep, Glob, Bash`；line 193 GOTCHAS 流程明定「OBSERVE 遇錯立即**寫入 GOTCHAS.md**」。
- **IDENTIFY**：review-hub 確實有寫檔流程（寫 GOTCHAS.md / 輸出報告）。移除 Write = 破壞 self-improvement 與報告輸出。
- **PROPOSE/APPLY**：**DEFER**。sub-agent 已自標此風險，grep 證實成立。least-privilege 立意good 但此 skill 真需 Write。
- **RECORD**：不改。若要強化，應改為「限制 Write 路徑範圍」而非全移除——另案。

### CS-1 純 side-effect hook 加 async — **NO-OP**（已完成）
- **OBSERVE**：settings.json hook async 狀態盤點 → notification-log/failure-log/audit-log/sdd-cache-post **已 async=True**（前次優化已做）。未 async 的剩餘項：post-edit（語法驗證 exit 1 回饋）、monitor-reminder（輸出 additionalContext 注入 context）、各 gate hook。
- **IDENTIFY**：依 lesson 2026-06-03-A，gate/feedback/context 注入語義的 hook **不可 async**（會失去阻擋/回饋/注入能力）。post-edit = 回饋語義、monitor-reminder = context 注入語義 → 皆不可 async。純 logging 已全部 async。
- **PROPOSE/APPLY**：**NO-OP**——無可安全 async 的剩餘項。CS-1 已由前次優化達成。
- **RECORD**：不改。驗證 = settings.json 已 async 的 4 個皆純 side-effect ✅；其餘皆有 gate/feedback/context 語義不可 async ✅。

### C 區 on-demand 化（CW-P2/P3/P5 + PH-1）— **APPLY 完成**
委派 implementer sub-agent 建 4 個 on-demand ref（零 auto-load byte）。**注意**：sub-agent 在隔離 worktree 建檔，需從其 worktree 取回主 tree（見 Lesson 2026-06-04-C）。

| 項 | 檔案 | 行/byte | 內容驗證 |
|----|------|---------|---------|
| CW-P5 | `.claude/refs/context-rot-symptoms.md` | 31行/1224B | Poisoning/Distraction 四模式 ✅ |
| CW-P3 | `.claude/refs/post-compact-checklist.md` | 33行/1013B | 37%損失/有損/rewind ✅ |
| CW-P2 | `.claude/refs/cjk-token-efficiency.md` | 39行/1199B | 2–3×/繁中/英文 ✅ |
| PH-1 | `.claude/refs/cache-health-metrics.md` | 41行/1626B | cache_hit_rate 公式 ✅ |

- **TEST**：presence-verified（檔案存在 + 關鍵詞 grep 命中）。**behavior-unverified**（on-demand ref 是否被正確觸發載入須實際 session 觀察，非 grep 可證 — 誠實標示）。
- **RECORD**：4 檔 APPLY，零 auto-load byte 成本。auto-load 仍 17,622（未動）。

---

## 進度 Checkpoint（第一批 ship）

**已完成**：
- 前置：auto-load 上限同步（commit 597d4207，5 檔 stale 修正）
- SA-1.1 → DEFER（grep 證實 review-hub 需 Write）
- CS-1 → NO-OP（純 logging 已全 async，餘者依 lesson 不可 async）
- C 區 CW-P2/P3/P5 + PH-1 → 4 個 on-demand ref 建立

**待續**（下批）：
- CS-2（pre-commit healthcheck 去阻塞，2,604ms→快，有正確性 trade-off，需細緻 behavioral test）
- CS-3（block-dangerous 79ms 優化，收益小）
- B 區 CW-P4（compact hint 強化，唯一進 auto-load，+~150→17,772）
- A 區 CW-P1（measure-cache.sh）/CW-P6（AGENTS.md 隔離自檢）/PH-2（prompt-lifecycle.md）/PH-4（prompts INDEX）/PH-5（subagent injection→on-demand）/SA-1.2（model-routing.md）/SA-2（agent-team-patterns，R2 待判）/SA-3.1（mast-mapping，R2 待判）
- D 區 SA-2/SA-3.1/PH-3 → R2「是否真有價值」逐項判斷

**決策理由**：context 累積，依使用者「避免 context window 太滿」+ advisor「ship 一批 + checkpoint 勝過 degraded 單次硬推」，分批執行。

---

## 第二批（2026-06-04 續，commit 11eb3871 + 本批）

### ⚠️ cap 決策翻轉（R7 — 第一批衝突已解）

第一批執行報告（line 14）寫「使用者明確不上調上限」，但這是**上個 session 的 agent 產物，非使用者原話**；MEMORY 待辦標「使用者決定先上調」。advisor 攔截此 silent resolution（「較新的 agent 紀錄 ≠ 較新的使用者決定」）。本批 **AskUserQuestion 直接問** → 使用者定奪：**上調 19,000，依計劃書放 auto-load**。本次指令「嚴格遵守計劃書」與「上調」一致。

### 前置：cap 18,000→19,000（commit 11eb3871）
- **APPLY**：5 處定義同步（CLAUDE.md/core.md/README/measure.sh 含算術）+ rationale 寫進 core.md §Framework Integrity（防無基準再 bump：「下次上調須同等級實證計劃書背書」）。
- **TEST**：grep 無殘留 18,000（除 core.md rationale 歷史文字）；measure.sh 跑得過；healthcheck FAIL=0。

### B+C 區 5 項 auto-load 增補（commit 11eb3871，依計劃書原意進 auto-load）
| 項 | 檔案 | 內容 | grep 驗證 |
|----|------|------|----------|
| CW-P4 | context-management.md | compact hint 加 file path/error string 原文勿改寫 | ✅ 勿改寫 |
| CW-P3 | context-management.md | post-compact 自檢指標（→ ref） | ✅ Compact 後自檢 |
| PH-1 | context-management.md | cache_hit_rate 健康指標（→ ref） | ✅ cache_read |
| CW-P2 | output-discipline.md | CJK 稅對策（→ ref） | ✅ CJK 稅 |
| PH-5 | subagent-strategy.md | indirect injection 防禦（data 不當 instruction） | ✅ indirect injection |
- **TEST**：auto-load 18,955 < 19,000（餘 45）；healthcheck 108/3/0。**presence-verified, behavior-unverified**（grep 證文字加了，非規則生效；R9 紀律）。
- **RECORD**：CW-P3/P2/PH-1 完整知識留第一批已建 on-demand ref，auto-load 只加觸發指標行 → byte 最小化。

### A 區 byte-neutral（新 ref/script，零 auto-load）
| 項 | 處置 | 驗證 |
|----|------|------|
| CW-P1 | `scripts/measure-cache.sh`（jq 確定性聚合） | **實測 cache_hit_rate=0.8531 > 0.7** ✅（首次為 cache 規則提供實證背書） |
| CW-P6 | AGENTS.md §2 加「Sub-agent Context 隔離自檢」 | ✅ 不繼承 parent |
| PH-2 | `.claude/rules/prompt-lifecycle.md`（path-scoped on-demand）+ README 登錄 | ✅ frontmatter + measure.sh 正確 skip |
| PH-4 | research/prompts/INDEX.md「模型遷移注意」 | ✅ re-express |

### D 區 R2 待判（grep 接地逐項判，inline 規則：substance 已存在→DEFER/→See；真 gap→最小補）
| 項 | 判定 | grep 證據 |
|----|------|----------|
| SA-1.2 model-routing.md | **DEFER** | 15 agent model 分配（5h/3o/7s）**無 drift**（無同 task-type 給不同 model）；per-agent 路由已在 AGENTS.md §2/§3 + CLAUDE.md §模式 + model-selection-grid.md；新建 = 第 6 個路由位置 = R2 違規 |
| SA-2 agent-team-patterns.md | **建（最小）** | 「研究術語→既有設施」橋接表不存在於單一處；用 →See 引用不複製 schema；grep gap-vote/predict/hub-and-spoke = 5 |
| SA-3.1 mast-failure-mapping.md | **DEFER** | 14 模式多數已防護（karpathy-mnilax + gap-vote + blind judge）；逐一列舉整檔 = 為列舉而列舉（R2） |
| SA-3.2 task verification | **建（補 GOTCHA 5）** | harness-meta GOTCHAS 無「parent grep 抽驗」條（grep 空）→ 真缺口，補泛化 sub-agent 委派抽驗規則 |
| PH-3 prompt-as-code | **NO-OP** | core.md + autoload-evolution SKILL 已有 falsifiable + eval 回歸 + PR 流程（計劃自評 80% 覆蓋）；形式化 = 重述既有 |

### CS 區（cold-start CS-2/CS-3）— **OUT-OF-SCOPE**（非待實作）
cold-start 計劃 §5 **自己排除**：「不在本任務內修改 hooks/settings.json（需獨立 gated step）」。CS-1 第一批已 NO-OP（純 logging 已全 async）。CS-2（healthcheck 去阻塞）/CS-3（block-dangerous 優化）涉破壞安全基礎設施 → **要做請另開 gated session**，不在本計劃執行範圍。

---

## 全域驗證（第二批完成）

```
auto-loaded bytes: 18,955 / 上限 19,000  ✅（餘 45）
healthcheck: PASS 108 / WARN 3 / FAIL 0  ✅（3 WARN 皆 pre-existing 環境項：remote/MCP）
measure-cache.sh: cache_hit_rate=0.8531  ✅
```

## ⚠️ 誠實點出：19,000 已近滿
auto-load **18,955 / 19,000，餘 45 bytes** — 本次上調的新 buffer 幾乎用盡。下次任何 auto-load 增補前須**重新評估**（壓 TYPE B/C/D 取回餘裕，或同等級實證計劃書背書再上調）。cap 不是免費額度。

## 完整行動項結算（19 項 + 前置）
- **APPLY**：CW-P1/P2/P3/P4/P6 + PH-1/P2/P4/P5 + SA-2/SA-3.2 + cap 上調 = 12 項
- **DEFER**：SA-1.1（review-hub 需 Write）/ SA-1.2（無 drift）/ SA-3.1（多數已防護）= 3 項
- **NO-OP**：CS-1（已 async）/ PH-3（已 80% 覆蓋）= 2 項
- **OUT-OF-SCOPE**：CS-2 / CS-3（計劃自排除，需獨立 gated session）= 2 項

---

## 第二批後修：孤兒 ref 可達性（advisor 攔截）

**盲點**：advisor 指出 SA-2 `agent-team-patterns.md` + CW-P5 `context-rot-symptoms.md` 為**孤兒**——無任何入口指標。manual-read ref 只有「模型知道它存在」才會 Read；建了不可達 = 違背「讓未來任務選用」目的 = 在別處用 DEFER 避的 R2（建沒人用的東西）自己踩。tell：prompt-lifecycle 登錄了 rules/README 卻跳過 refs/README，不一致。

**根因擴大**：grep 全 refs/ → **6 個缺登錄**（batch-1 的 4 個雖有 auto-load 行指向可達，但 refs/README 表停在「12 個」已過時，實際 17）。

**修法（零 auto-load byte）**：refs/README.md ① Quick Lookup 加 agent-team + context-rot 兩入口 ② 全表補 6 個 + 標題 12→17 + 標載入來源。
- **byte 約束實證**：subagent-strategy.md（auto-load）加 →See 需 57–162 byte，但餘僅 45 → **加不下**。這正是「19,000 近滿」的直接後果。refs/README Quick Lookup 是 manual-read ref 的標準發現路徑（與其他 16 個一致），在當前 byte 約束下為正確解。
- **驗證**：兩孤兒在 refs/README 可達 ✅；auto-load 18,955 未動 ✅；healthcheck FAIL=0 ✅。

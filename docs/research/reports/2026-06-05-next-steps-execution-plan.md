# 執行計劃書 — synthesis 報告「下一步行動」6 項

> **建立**: 2026-06-05
> **來源**: `research/reports/2026-06-05-harness-memory-self-evolution-synthesis.md` §下一步行動（PR #474 最新版，6 項）
> **使用者定奪**: 全範圍（#2/#4/#5/#6 + 記錄 #3）· 雙向連結 · 本 session 執行
> **方法**: Harness Loop（OBSERVE->IDENTIFY->PROPOSE->TEST->APPLY->RECORD）· 每項附 falsifiable prediction + 機械驗證指令

---

## 0. 前置事實（已機械驗證）

| 事實 | 驗證 | 結果 |
|------|------|------|
| URL 路徑經 PR #474 改名 | `git ls-files` | 舊 `...-2026-05-29.md` -> 新 `2026-06-05-harness-memory-self-evolution-synthesis.md` |
| **兩個** MEMORY.md | `git ls-files memory/` vs machine-local | tracked `memory/MEMORY.md`(191行,48 Lesson) vs machine-local(208行,23 Lesson)；diff 382 行**內容不同** |
| 雙向連結正確目標 | repo 邊界分析 | **tracked `memory/MEMORY.md`** ↔ tracked `.claude/skills/*/GOTCHAS.md`（同為 tracked -> 無斷鏈） |
| GOTCHAS.md 數 | `git ls-files` | 26 個 tracked |
| 9 配對錨點 | 逐條 grep | 7 唯一錨點全部存在 ✅ |

**關鍵邊界**（advisor 攔截）：machine-local MEMORY.md **未 tracked**，若對它建雙向連結會把斷鏈 commit 進 repo。-> 改用 tracked `memory/MEMORY.md`。

---

## APPLY / DEFER 帳本

| # | 行動 | 優先 | 處置 | 理由 |
|---|------|------|------|------|
| 2 | MEMORY↔GOTCHA 雙向連結 | 中 | **APPLY** | 真實工作；6 唯一 Lesson 配對已 grep 驗證 |
| 3 | GOTCHA 3-session 回顧 | — | **RECORD** | 35>5 ✅ 已過，只記結果 |
| 4 | compactor 整合風險評估 | 中 | **ASSESS->DEFER** | 評估產出建議；compactor *改動*本身 DEFER（須獨立 gated） |
| 5 | R9 eval-hack 註記 | 低 | **PROPOSE->DEFER** | R9 在 core.md(auto-load 18,455/19,000)；**必走 /autoload-evolution**，不可本 session inline 改 |
| 6 | Dreaming 對齊查核 | 低 | **RECORD(NO-OP)** | 已對應官方原則，記錄對應即可 |

---

## #2 — MEMORY ↔ GOTCHA 雙向連結（APPLY）

### 配對清單（researcher 提議 -> parent grep 驗證 -> 收斂）

6 個唯一 Lesson 有真實配對（42/48 Lesson 為 NO MATCH，符合預期——多數 Lesson 是 session-workflow 教訓）：

| Lesson(MEMORY.md) | GOTCHA(路徑#錨點) | 收斂後連結 |
|---|---|---|
| 2026-05-25c (PGE) | autoload-evolution「PGE 自評陷阱」+ eval-designer「LLM 自評陷阱」 | 連 **2** 個（PGE 原則橫跨兩 skill，皆 Direct） |
| 2026-05-28 (假共識) | gap-vote「self-attested 共識 = 假共識」 | 連 1 個 |
| 2026-05-31h-A (永不 cd) | webshot「cd 被 hook 封鎖」 | 連 1 個 |
| 2026-05-31j-A (verdict 須接地) | harness-meta GOTCHA 5 | 連 1 個 |
| 2026-06-04-C (委派產物) | harness-meta GOTCHA 5 | 連 1 個（GOTCHA 5 正文已引用本 Lesson） |
| 2026-06-05-A (親驗≠證據)* | autoresearch + gap-vote + harness-meta GOTCHA 5 | **收斂連 1 個**：autoresearch「verification-claim-without-tool-use」（最具體同源）；避免 3 連結稀釋 |

\* 收斂理由：researcher 對 2026-06-05-A 提 3 連結會過度密集。harness-meta GOTCHA 5 已被 2026-05-31j-A/2026-06-04-C 連結；gap-vote 與 autoresearch 同源同事件 -> 選最具體的 autoresearch。
**注意**：machine-local MEMORY.md 才有 `2026-06-05-A`；tracked MEMORY.md 需先確認該 Lesson 是否存在（grep）；不存在則此配對降為 NO-OP（不硬塞）。

### 連結格式

- **MEMORY.md -> GOTCHA**（單行 Lesson 末尾追加）：`[GOTCHA: <skill>/GOTCHAS.md「<錨點關鍵詞>」]`
- **GOTCHA -> MEMORY.md**（GOTCHA 條目末尾追加）：`[Lesson: MEMORY 防範規則#<date>]`

### Falsifiable Prediction #2

- **預測**: 連結後 `grep -c '\[GOTCHA:' memory/MEMORY.md` ≥ 6；每個被連 GOTCHA 檔 `grep -c '\[Lesson:'` ≥ 1；所有錨點關鍵詞在目標檔可 grep 命中；MEMORY.md 行數不變（僅行內追加）。
- **驗證指令**:
  ```bash
  grep -c '\[GOTCHA:' memory/MEMORY.md          # 預期 ≥6
  grep -rl '\[Lesson:' .claude/skills/*/GOTCHAS.md | wc -l   # 預期 ≥5 檔
  bash scripts/healthcheck.sh                    # FAIL=0
  ```
- **反向驗證（防 hack）**: 每條新連結的錨點關鍵詞必在目標檔實際存在（不可指向不存在的 GOTCHA）。

---

## #3 — GOTCHA 3-session 回顧（RECORD）

- **驗證指令**: `git log --oneline --all -- ".claude/skills/*/GOTCHAS.md" | wc -l`
- **結果**: **35**（基準=5，2026-05-29）-> 增量 30 ≫ 3 -> **PASS**
- **既有待辦對應**: tracked MEMORY.md L48「≥3 新 commit -> stop hook 維持」-> 條件滿足，**stop hook 維持**（不升格 PreToolUse）。
- **動作**: 在 MEMORY 記錄結果 + 結清該待辦。

---

## #4 — compactor 整合風險評估（ASSESS->DEFER）

### 評估問題
`memory-compactor`（≥200 行觸發）目前「200 行無條件全量壓縮」是否應改為「近 N session 原始節保留 + 顯式門控整合」（源 2605.12978）？

### 既有證據（不需新研究）
- **Lesson 2026-06-04-G** 已記載：#454 compactor 自報壓 32 實際**流失 12 個高價值 Lesson** -> 過度壓縮風險**已實證**。
- 既有防範已落地：「壓縮後必 `comm -23` 對比流失清單，不信 compactor 自報數字」。

### 評估結論（PROPOSE）
- compactor 過度整合風險**真實存在**且**已被既有 `comm -23` 防範規則部分緩解**。
- 論文建議的「近 N session 原始保留」= 對既有「零損失保留 Lesson」指令的**結構強化**。
- **DEFER 改動**：實際修改 memory-compactor SKILL（加「近 3 session 原始節 forbidden-to-compact」規則）屬 skill 行為變更，須獨立 gated session + skill-evolution 流程。本 session 僅交付評估 + 可機械驗證的驗收條件。

### 可機械驗證條件（交付給未來 gated session）
```bash
# compactor 跑後，最近 3 session 原始決策/Lesson 字串須實質存活（非 stub）
comm -23 <(git show HEAD~1:memory/MEMORY.md | grep -oE 'Lesson 2026-06-0[0-9][^：]*' | sort -u) \
         <(grep -oE 'Lesson 2026-06-0[0-9][^：]*' memory/MEMORY.md | sort -u)
# 預期：最近 3 session Lesson 全在當前版（空輸出=無流失）
```

---

## #5 — R9 eval-hack 註記（PROPOSE->DEFER 至 /autoload-evolution）

### 提議
R9（core.md §R9 Tests Verify Intent）補一句：高能力模型 eval-hack 率反而升高（Vesper 2605.15221：16.6% vs 0%）->「能通過任何實作的測試 = 沒有測試」對高能力模型尤其重要。

### 硬約束（advisor 攔截，不可本 session inline 改）
- core.md 現 **18,455/19,000 bytes**（餘 545）。
- auto-load 變更**必須走 `/autoload-evolution`**（≤1 規則/cycle、≤50 行 diff、eval 回歸 gate）— CLAUDE.md §Framework Integrity。
- **註記增量估算**: 補一句約 +60~100 bytes（CJK），餘 545 容得下，但**程序上**仍須走 autoload-evolution 閉環。

### 處置
- **本 session**: 寫成 PROPOSE 提案，交 `/autoload-evolution` 評估。
- **註記**: tracked MEMORY.md「Lesson 2026-05-25c」已記「hack 率 16.6%」，R9 補強與此一致。

---

## #6 — Dreaming 對齊查核（RECORD / NO-OP）

### 對應關係（已存在，無需動作）
| 官方 Dreaming 原則（tweets 2026-05-07） | workspace 既有對應 |
|---|---|
| 離線非同步進化 | `autoload-evolution` 閉環（非 mid-session） |
| 不污染進行中 session | context-management.md「mid-session 禁改 CLAUDE.md」+ Lesson 2026-05-25b |

### 結論
**NO-OP**：workspace 已完整對應官方 Dreaming 原則，無需額外動作。記錄此對應關係於 MEMORY 即可（供未來查核）。

---

## 執行順序（本 session）

1. **#2 APPLY**: grep 確認 tracked MEMORY.md 各 Lesson 存在 -> Edit 加雙向連結（先 MEMORY 6 處，再 5 個 GOTCHA 檔）-> 跑驗證指令。
2. **#3/#4/#5/#6 RECORD**: 在 tracked MEMORY.md 新增 session 節，記錄 #3 結果 + #4 評估結論 + #5 PROPOSE + #6 NO-OP + 結清相關待辦。
3. **驗證**: `bash scripts/healthcheck.sh`（FAIL=0）+ #2 驗證指令全綠。
4. **commit**: feature 分支（當前在 main，須先 `feature.sh start`）；`git commit -- <精確 pathspec>`（防背景搶分支）。

## 風險與防範（援引既有 Lesson）
- **背景搶分支**（Lesson 2026-06-04-A）: commit 同一 bash 區塊內 `git branch --show-current` 守衛 + pathspec commit。
- **過度連結稀釋**: 2026-06-05-A 收斂為 1 連結（非 3）。
- **mapping 過度延伸**（Lesson 2026-06-04-G）: 已通過零-hedge 測試 + parent grep 驗證；42/48 NO MATCH 不硬塞。
- **Edit 吞換行**（Lesson 2026-05-31j-B）: 行內追加用 `<原行尾>` 匹配，加在現有內容後不刪換行。

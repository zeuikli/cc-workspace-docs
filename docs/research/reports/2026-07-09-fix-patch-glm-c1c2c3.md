# Fix Patch — GLM C1/C2/C3

> Target file: `research/reports/2026-07-09-fusion-architecture-design-plan.md`
> Generated: 2026-07-09 · Author: GLM-5.2 (worker subagent)
> Scope: 3 critical issues (C1 headline reframing, C2 cache-penalty precise scoping, C3 providerLock contradiction).
> All `old_str` values copied verbatim from the current file and verified via Grep + Read.

---

## C1 — -35.2% headline reframing (workload-conditional savings)

### Fix C1-1
**Line**: 41
**Old**: `- 35% 成本降低（非 Fable 配置）,41% 降低（Fable 5 配置）`
**New**: `- 35% 成本降低（非 Fable 配置）,41% 降低（Fable 5 配置）— **注意**: 此為 Cognition 自報,未經第三方獨立驗證; workspace 模擬顯示成本加權 -35.2% 但頻率加權僅 +2.8%,節省 84% 來自大規模遷移任務（10% 頻率）`
**Reason**: 原始 headline 「35% / 41% 成本降低」為 Cognition 自報數字,未標明來源與條件。Workspace 模擬顯示成本加權 -35.2% 顯著但頻率加權僅 +2.8%,且節省高度集中於大規模遷移任務（10% 頻率貢獻 84% 節省）,需明確標註 workload-conditional,避免讀者誤推為普適節省率。

### Fix C1-2
**Line**: 220
**Old**: `- 機械任務 → cost 檔（Haiku $1/$5 或開源 GLM-5.2 $1.4/$4.4）`
**New**: `- 機械任務 → cost 檔（Haiku $1/$5 或開源 GLM-5.2 $1.4/$4.4）— **節省為 workload-conditional**: 模擬顯示 -35.2% 成本加權但 +2.8% 頻率加權,84% 節省來自 10% 頻率的大規模遷移任務`
**Reason**: §3.2 Layer 1「模型路由層（最大節省）」呼應 headline 卻未標 workload 條件,易被誤讀為普適最大節省層。在此 anchor 同一條件註記,保持 §1.2 與 §3.2 敘述一致。

---

## C2 — 「零額外 cache 懲罰」claim 精確區分 compactionModel vs 主模型切換

### Fix C2-1
**Line**: 37
**Old**: `- **關鍵洞見**: 模型切換綁定在 context compaction 階段 — compaction 本就觸發 cache 失效,因此「順便」換模型成為零額外 cache 懲罰的「免費」操作`
**New**: `- **關鍵洞見**: 模型切換綁定在 context compaction 階段 — compaction 本就觸發 cache 失效。**精確區分**: compactionModel 切換 = 零額外 cache 懲罰（compaction 本就失效）; 主模型切換 = 一次性 prefix re-cache 成本（新模型需重建快取前綴）,但仍比 mid-turn 切換便宜。此 claim 繼承自 Cognition 自報,Factory API 層快取行為未經獨立驗證`
**Reason**: 原句籠統稱「換模型」為零懲罰,實際上 compactionModel 切換（compaction 本就失效）與主模型切換（新模型需重建 prefix cache）cache 成本不同。需精確區分兩者,並標註此 claim 來自 Cognition 自報、Factory API 快取行為未獨立驗證。

### Fix C2-2
**Line**: 113
**Old**: `│  零額外 cache 懲罰（compaction 本就失效）          │`
**New**: `│  compactionModel: 零懲罰; 主模型: 一次性 re-cache  │`
**Reason**: §2.2 L3 box 原文籠統標「零額外 cache 懲罰」,未區分兩種切換路徑。改為並列 compactionModel（零懲罰）與主模型（一次性 re-cache）,與 §1.1 修正後敘述對齊;同時維持原 box 視覺寬度相近。

### Fix C2-3
**Line**: 118
**Old**: `2. **Cache-first**: 所有模型切換决策必須考慮 cache 影響,零或最低 cache 懲罰`
**New**: `2. **Cache-first**: 所有模型切換决策必須考慮 cache 影響。compactionModel 切換 = 零懲罰; 主模型切換 = 一次性 prefix re-cache（非零）`
**Reason**: §2.2 design principle 2 原文「零或最低 cache 懲罰」模糊,未指明哪種切換為零、哪種非零。改為明確兩式並列,與 §1.1 / §2.2 L3 box 修正保持一致。

### Fix C2-4
**Line**: 126
**Old**: `- 模型切換綁定 compaction（零 cache 懲罰）`
**New**: `- 模型切換綁定 compaction（compactionModel = 零懲罰; 主模型 = 一次性 re-cache）`
**Reason**: §2.5「切換時機」原文「零 cache 懲罰」為籠統宣稱,需對齊 §1.1 精確區分。

### Fix C2-5
**Line**: 191
**Old**: `- 模型切換只在 compaction 時（零額外 cache 失效）`
**New**: `- compactionModel 切換: 零額外 cache 失效; 主模型切換: 一次性 prefix re-cache（非零,但低於 mid-turn 切換）`
**Reason**: §2.5「Cache 紀律」原文「零額外 cache 失效」籠統涵蓋兩種切換。改為分述 compactionModel（零失效）與主模型（一次性 prefix re-cache,非零但低於 mid-turn 切換）,與 §1.1 / §2.2 修正保持一致。

---

## C3 — providerLock 內部矛盾修正（無 CLI 開關,由 Mixed Models 規則自動強制）

### Fix C3-1
**Line**: 76
**Old**: `| **providerLock** | 鎖定 provider 避免跨廠商 reasoning trace 不相容 | ✅ Session 層級 |`
**New**: `| **providerLock** | ⚠️ 非 CLI 可設定; 相容性由 Mixed Models 規則自動強制（OpenAI↔OpenAI; Anthropic reasoning on↔Anthropic; reasoning off↔非 OpenAI）。`providerLockTimestamp` API 欄位存在但語意未文件化 | ⚠️ 自動強制 |`
**Reason**: 原文稱 providerLock「鎖定 provider」「✅ Session 層級」暗示存在 CLI/session 設定開關,實際上 providerLock 無 CLI 可設定項;跨廠商相容性是由 Mixed Models 規則自動強制。`providerLockTimestamp` API 欄位雖存在但語意未文件化,需明確標註避免誤導使用者嘗試手動設定。

### Fix C3-2
**Line**: 91
**Old**: `| 跨廠商 reasoning trace | ❌ 不相容 | ⚠️ providerLock 管理（OpenAI 只配 OpenAI） |`
**New**: `| 跨廠商 reasoning trace | ❌ 不相容 | ⚠️ Mixed Models 相容性規則自動強制（非 providerLock CLI 開關） |`
**Reason**: §1.3 diff table 原文將相容性管理歸因於「providerLock 管理（OpenAI 只配 OpenAI）」,與 C3-1 修正矛盾。相容性實由 Mixed Models 規則自動強制,非 providerLock CLI 開關;改寫以消除內部矛盾。

### Fix C3-3
**Line**: 163
**Old**: `3. 設定 `providerLock: anthropic` 確保 reasoning trace 相容`
**New**: `3. ~~設定 `providerLock: anthropic`~~ — **修正**: providerLock 無 CLI 開關; Mixed Models 相容性規則自動強制（reasoning on = Anthropic only; reasoning off = 可配非 OpenAI）。無需手動設定`
**Reason**: §2.4 Phase 2 step 3 原文指示使用者「設定 `providerLock: anthropic`」,但 providerLock 無 CLI 開關可設定,此為可行動性錯誤（actionable error）— 使用者照做會找不到設定項。改為 strikethrough + 修正說明,指引相容性由 Mixed Models 規則自動強制、無需手動設定,並補充 reasoning on/off 對應廠商規則。

---

## 套用指引

1. 依本檔逐筆執行 `old_str → new_str` 替換（建議用 Edit 工具,逐筆唯一比對）。
2. C2-2（line 113 box）替換後請視覺檢查 ASCII box 對齊（兩側 `│` 間距）;若 box 寬度不一致,可於新字串尾端補/減半形空格使右側 `│` 對齊,但不得改動語意。
3. C3-3 替換後 line 163 將含 strikethrough `~~...~~`,確認渲染器支援 Markdown strikethrough（GitHub/GlFM 預設支援）。
4. 全部套用後建議 grep 驗證: `零 cache 懲罰` / `零額外 cache` / `providerLock` / `35% 成本降低` 應僅出現於本 patch 所列 new_str 中（C3-1 / C3-2 new_str 仍含 "providerLock" 一詞,屬預期）。

## 範圍外發現（供 parent 決定是否追加 fix,本 patch 不處理）

- §1.3 diff table 另有一行 `| Mid-session 切換 | compaction 時切換,零 cache 懲罰 | ... |` 同樣籠統稱「零 cache 懲罰」,未在本次任務指定修復範圍內（task 僅列 lines 37/113/118/126/191/197）。如需全面對齊,可追加 C2-6 處理該行。
- 本 patch 未驗證 Factory API `providerLockTimestamp` 欄位實際語意,僅標註「未文件化」;若 parent 有 API doc 來源可補實證。

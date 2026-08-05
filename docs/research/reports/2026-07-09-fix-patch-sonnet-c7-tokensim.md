# Sonnet-5 Fix Patch: C7 + Token Sim §3.3

> 修復兩項殘留 critical issues: C7（design plan 委派規則引用過時）+ token simulation §3.3 cost share 計算錯誤。
> 套用目標: `2026-07-09-fusion-architecture-design-plan.md`（C7）+ `2026-07-09-fusion-kimi-token-simulation.md`（§3.3）。
> 修復依據: 現行 workspace 規則 `subagent-strategy.md`「預設最簡拓撲；委派須具名效益」+ GLM cross-review 正確算式。

---

## C7 Fixes (design plan)

### Fix C7-1
**Line**: 31（§1.1 Sidekick 雙模型並行架構）
**Old**: `- 主 agent 扮演「tech lead」: 只讀取絕對必要的資訊,預設委派給 sidekick,保留規劃/歧義判斷/最終審查`
**New**: `- 主 agent 扮演「tech lead」: 只讀取絕對必要的資訊,委派給 sidekick（須具名效益: context isolation / parallelism / mechanical volume）,保留規劃/歧義判斷/最終審查`

### Fix C7-2
**Line**: 57（§1.2 Workspace 現有 multi-mode 架構）
**Old**: `- `delegation-protocol.md`: 指揮官不下場、預設委派、升降級路徑`
**New**: `- `delegation-protocol.md`: 指揮官不下場、委派須具名效益、升降級路徑（現行規則以 subagent-strategy.md 為準）`

### Fix C7-3
**Line**: 138（§2.3 Phase 1 優化項 1）
**Old**: `1. 主對話預設委派機械任務給 cost 檔 sidekick,只在「規劃/歧義/審查」時親做`
**New**: `1. 主對話委派機械任務給 cost 檔 sidekick（具名效益: low-risk mechanical volume）,只在「規劃/歧義/審查」時親做`

### Fix C7-4
**Line**: 190（§2.5 Fusion Protocol 角色分配）
**Old**: `- Main Agent: 規劃、歧義判斷、最終審查、監控 sidekick（預設委派,例外親做）`
**New**: `- Main Agent: 規劃、歧義判斷、最終審查、監控 sidekick（委派須具名效益,例外親做）`

### Fix C7-5
**Line**: 233（§3.2 Layer 4 委派策略層）
**Old**: `- 預設委派,例外親做（delegation-protocol.md §1）`
**New**: `- 委派須具名效益,例外親做（subagent-strategy.md 現行規則; delegation-protocol.md §1 已由 subagent-strategy.md 覆蓋）`

### Fix C7-6
**Line**: 320（§5.2 alignment table）
**Old**: `| 指揮官不下場 | delegation-protocol.md §1 | Main Agent 預設委派,例外親做 |`
**New**: `| 指揮官不下場 | subagent-strategy.md（現行）/ delegation-protocol.md §1（已覆蓋） | Main Agent 委派須具名效益,例外親做 |`

---

## Token Sim §3.3 Fixes

### Fix TS-1
**Location**: §3.3 成本加權表（5 task rows + 加權平均 row）
**Old**:
```
| 任務類型 | 現有成本 | Fusion 成本 | 佔現有總成本比 | 加權貢獻 |
|---------|---------|------------|--------------|---------|
| 單檔小改 | $0.0117 | $0.0117 | 0.5% | 0% |
| 跨模組重構 | $0.0984 | $0.1341 | 4.6% | +1.7%（成本增） |
| 深度研究 | $0.4613 | $0.2925 | 21.6% | -7.3% |
| 安全審查 | $0.3698 | $0.4373 | 17.3% | +1.2%（成本增） |
| 大規模遷移 | $1.536 | $0.729 | 56.0% | -29.7% |
| **成本加權平均** | $2.477 | $1.605 | 100% | **-35.2%** |
```
**New**（+ = savings / - = cost increase; cost share = 該任務現有成本 / $2.4772）:
```
| 任務類型 | 現有成本 | Fusion 成本 | 佔現有總成本比 | 加權貢獻 |
|---------|---------|------------|--------------|---------|
| 單檔小改 | $0.0117 | $0.0117 | 0.5% | 0% |
| 跨模組重構 | $0.0984 | $0.1341 | 4.0% | -1.4%（成本增） |
| 深度研究 | $0.4613 | $0.2925 | 18.6% | +6.8%（節省） |
| 安全審查 | $0.3698 | $0.4373 | 14.9% | -2.7%（成本增） |
| 大規模遷移 | $1.536 | $0.729 | 62.0% | +32.6%（節省） |
| **成本加權平均** | $2.477 | $1.605 | 100% | **+35.2%（節省）** |
```

**算式核驗**:
- 佔現有總成本比 = 現有成本 / $2.4772:
  - Task 1: 0.0117 / 2.4772 = 0.47% ≈ 0.5%（保留原值）
  - Task 2: 0.0984 / 2.4772 = 3.97% ≈ 4.0%
  - Task 3: 0.4613 / 2.4772 = 18.63% ≈ 18.6%
  - Task 4: 0.3698 / 2.4772 = 14.93% ≈ 14.9%
  - Task 5: 1.536 / 2.4772 = 62.0%
- 加權貢獻 = (現有成本 - Fusion 成本) / $2.4772（+ = 節省, - = 成本增）:
  - Task 1: (0.0117 - 0.0117) / 2.4772 = 0%
  - Task 2: (0.0984 - 0.1341) / 2.4772 = -1.44% ≈ -1.4%（成本增）
  - Task 3: (0.4613 - 0.2925) / 2.4772 = +6.81% ≈ +6.8%（節省）
  - Task 4: (0.3698 - 0.4373) / 2.4772 = -2.72% ≈ -2.7%（成本增）
  - Task 5: (1.536 - 0.729) / 2.4772 = +32.58% ≈ +32.6%（節省）
  - Sum: 0 - 1.4 + 6.8 - 2.7 + 32.6 = 35.3% ≈ 35.2% ✓（與總節省 ($2.4772-$1.6046)/$2.4772 = 35.22% 一致）

### Fix TS-2
**Location**: §3.4 兩種加權結果對比表（成本加權 row）
**Old**: `| 成本加權 | -35.2%（顯著節省） | 若以「USD 支出」算, Fusion 因大規模遷移佔 56% 成本且省 53% 而顯著節省 |`
**New**: `| 成本加權 | +35.2%（顯著節省） | 若以「USD 支出」算, Fusion 因大規模遷移佔 62% 成本且省 53% 而顯著節省 |`
**原因**: 與 §3.3 新表 sign convention 對齊（+ = 節省）+ 56% → 62%（Task 5 正確 cost share）。

### Fix TS-3
**Location**: §6 驗收對照表（加權平均節省百分比 row）
**Old**: `| 加權平均節省百分比 | ✅ §3.2 頻率加權 +2.8% / §3.3 成本加權 -35.2% |`
**New**: `| 加權平均節省百分比 | ✅ §3.2 頻率加權 +2.8% / §3.3 成本加權 +35.2% |`
**原因**: 與 §3.3 新表 sign convention 對齊（+ = 節省）。

---

## 驗證

### C7 fixes 驗證
- `grep -n '預設委派' 2026-07-09-fusion-architecture-design-plan.md` → 0 matches（全部 6 處已替換）
- `grep -n '委派須具名效益\|具名效益' 2026-07-09-fusion-architecture-design-plan.md` → 6 matches（C7-1 ~ C7-6）

### Token sim fixes 驗證
- `grep -n '56%\|56\.0%\|21\.6%\|17\.3%\|4\.6%\|-29\.7%\|-7\.3%\|+1\.7%\|+1\.2%\|-35\.2%' 2026-07-09-fusion-kimi-token-simulation.md` → 0 matches（舊錯值全清除）
- 新值全部到位: 4.0% / 18.6% / 14.9% / 62.0% / -1.4% / +6.8% / -2.7% / +32.6% / +35.2%
- 加權貢獻 sum = 0 - 1.4 + 6.8 - 2.7 + 32.6 = 35.3% ≈ 35.2%（總節省）✓

---

## 已套用檔案

| 檔案 | 修改處 |
|------|--------|
| `research/reports/2026-07-09-fusion-architecture-design-plan.md` | C7-1 ~ C7-6（6 處） |
| `research/reports/2026-07-09-fusion-kimi-token-simulation.md` | TS-1（§3.3 表）+ TS-2（§3.4 表）+ TS-3（§6 表）|

*Patch 完成 2026-07-09 · Sonnet-5*

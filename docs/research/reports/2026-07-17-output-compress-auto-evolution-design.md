# output-compress 自動量測 × 自動進化機制設計

> 2026-07-17，使用者指示「收集更多數據優化 SKILL + 評估自動量測/自動優化/進化機制」。
> 學術接地：11 篇壓縮保真論文（見 research/papers/ 2026-07-17 歸檔批次）；本設計直接消費其中
> 2606.29251（decontextualization）、2503.19114（groundedness 掉分）、2602.09789（scaling paradox）。

## 0. 設計約束（不可違反的既有裁決）

1. **判斷 vs 決定公理**（core.md）：LLM 只做壓縮判斷與提案撰寫；量測、門檻、觸發全部確定性程序。
2. **2026-07-16 使用者裁決（選項 a）**：AUTO 維持 advisory；enforcement 升級**只能**在 2026-08-13 複查且零筆日 ≥20/28 時進入裁決——本機制**不預支該決定**，只讓複查時的資料更完整。
3. 提案不自動套用：一律 EVOLUTION-QUEUE `status: proposed`，Routine G ≤2 提案/週上限沿用。

## 1. 三層架構

```
┌ 採樣層（多掛點餵 log；不新增 enforcement hook）
│   fidelity-check.py --log →  evolution/compress-log.jsonl
├ 量測層（確定性聚合 + 固定門檻 verdict）
│   scripts/compress-metrics.py --json → V1–V5 verdicts
└ 進化層（週節奏；judgment 只在提案撰寫）
    Routine G 消費 verdicts → EVOLUTION-QUEUE proposed → 人工審 → skill-evolution:apply
```

## 2. 各層落地內容（本日已實作 ✅ / 提案 ⏳）

### 採樣層——增加數據量，不越權

- ✅ **grounded_pct 入 log**：每筆新增接地率代理欄（詞級 containment，只刪不改寫 ⇒ ≈100）——2503.19114 groundedness 軸的零成本確定性代理。
- ✅ **hedge_counts 入失真閘**：decontextualization（2606.29251）成為第 9 個白名單類別；FAIL 樣本本身就是新數據維度（missing_keys 分布多了一類）。
- ✅ **委派壓縮 context 標記**（SKILL §7 既有）：`delegated-*` vs inline 對照組。
- ⏳ **Routine RECORD 採樣擴充**（提案）：Routine C 已有 Step -1 強制 gate+log；比照擴到 A/B/E/F/G 的 RECORD——routine 是**確定性 spec 驅動**，這裡加「必跑」不是 enforcement hook、是 spec 條款（07-16 分層證據：routine 遵守 AUTO、互動式忽略——把守規矩的一側採樣最大化）。
- ✅ **一般 session 機會日誌**（2026-07-17 使用者指示「一般 session 也要自動量測」後落地）：「**量測** enforcement」與「**壓縮** enforcement」分離——前者零 LLM 參與零失真風險，內嵌既有 `usage-delegation-gate.sh`（PreToolUse Agent|Workflow，**零新增 settings.json wiring**）：≥500B 派工 prompt 機械記 bytes/coverage 近似/契約齊備/would_compress → `evolution/compress-opportunity-log.jsonl`（merge=union）。這補上執行率的**分母**（compress-log 只有自願壓的分子，G8/G13 雙重樣本受限的結構性解法）；純記錄無提醒，原 queue 指出的循環依賴（hook 判斷「該壓沒壓」須先跑 coverage）不存在——hook 不判斷、只記錄。
- ❌ **仍不做**：壓縮 enforcement（強制模型壓縮 / block 未壓派工）——等 08-13 裁決，V3/V4/V6 就是該裁決的輸入。

### 量測層——`scripts/compress-metrics.py` ✅

固定門檻 verdict（改動須同步本檔）：

| ID | 條件 | action_hint |
|----|------|-------------|
| V1 | 組合 n≥5 且 pass_rate<0.90 | 降該組合壓縮上限提案 |
| V2 | 組合 n≥5 且 grounded 中位 <95 | 改寫滲入 → GOTCHAS + 重申鐵則 |
| V3 | 零筆日 ≥20/28 | 觸發 08-13 複查裁決條件 |
| V4 | 互動式 n=0 且 routine n>0 | advisory 分層失效證據 |
| V5 | delegated pass < inline（雙側 n≥5） | SKILL §7 撤除候選 |
| V6 | would_compress 機會 ≥10 且執行率 <0.30 | AUTO 對互動 session 失效的分母級證據（08-13 複查輸入） |

**首跑實測（2026-07-17，28 天窗、31 筆）**：V1×2（`full×subagent-prompt` 0.727、`lite×routine-f` 0.333）+ V3（22/28）。V1 兩筆為真訊號、可立即供 Routine G 撰提案；V3 依約束 0-2 不裁決、僅累積。

### 進化層——Routine G 接線 ✅

ROUTINE-G spec IDENTIFY 段加：`python3 scripts/compress-metrics.py --json` 必跑，verdict 非空 → 對應提案候選（計入 ≤2/週）；V1/V2 需附 log 樣本行佐證（judgment 撰寫、機械數字直引 verdict JSON）。

## 3. 反 eval-hack 與失效偵測

- **量測器不可被壓縮行為討好**：pass_rate 分母 = 全部 log 筆（含 fail），模型「少記 fail」會使 V3/V4 惡化——兩個 verdict 互為對抗。
- **門檻改動紀律**：V1–V5 門檻是「決定」，改動 = harness 修改 → 失敗簽名 ≥2 次獨立重現才動（harness-loop.md 觸發門檻）。
- **grounded_pct 的已知限界**：詞級 containment 對「換序造成語義反轉」盲（fidelity 閘的 date/number multiset 已部分覆蓋）；它是趨勢指標非逐筆 oracle。
- **Falsifiable prediction**：hedge 類上線後 30 天，`missing_keys` 含 `hedge_counts` 的 FAIL ≥1 筆（證明軸有效）；若 0 筆且人工抽查 10 樣本無 hedge 剝離 → 詞表過鬆，收窄。

## 4. 待辦 / 邊界

- eval fixture 三臂（SKILL §5 既有待辦）仍缺；compress-metrics 是 telemetry 路線、fixture 是 benchmark 路線，互補不互代。
- EDU 級壓縮單位（2512.14244）列 backlog，等 V1 訊號證明行級刪除不夠再議。
- 2026-08-13 複查時的裁決輸入 = `compress-metrics.py --json`（V3/V4 即該複查指定的分層量測軸）。

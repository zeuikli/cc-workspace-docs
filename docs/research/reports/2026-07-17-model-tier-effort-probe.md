# 模型 × effort 深度/成本探測（2026-07-17）

> Workflow `wf_60878e3b-03b`（8 組態平行，n=1/組態，3 題：seeded bug hunt ×3 / 期望值 42 / 架構取捨）；前置單輪 `wf_a75b02a6-397`（6 組態）。
> ⚠️ 證據強度：**n=1、題組僅 3 題、機械計分兩度誤判經人工對帳修正**——只支撐 L2 資料表標注，不支撐行為規則變更。

## 結果表（對帳後）

| 組態 | T1 發現條數 | 種下 bug 3 | T2=42 | T3 分析字數 | est. 輸出 tok | 相對成本* |
|---|---|---|---|---|---|---|
| fable-low | 6 | 3/3 | ✅ | 952 | ~863 | $0.065 |
| fable-medium | 5 | 3/3 | ✅ | 1,629 | ~1,157 | $0.087 |
| opus-low | 5 | 3/3 | ✅ | 913 | ~1,036 | $0.078 |
| opus-medium | 4 | 3/3 | ✅ | 1,026 | ~911 | $0.068 |
| sonnet-low | 5 | 3/3 | ✅ | 789 | ~925 | $0.014 |
| sonnet-medium | 5 | 3/3 | ✅ | 3,520 | ~3,016 | $0.045 |
| haiku-low | 4 | 3/3 | ✅ | 734 | ~1,499 | $0.006 |
| haiku-medium | 4 | 3/3 | ✅ | 267 | ~1,075 | $0.004 |

\* 輸出字元/3 估 token × 佔位單價（fable/opus $75、sonnet $15、haiku $4 /Mtok out）；input 側 8 組態幾乎同額（同一 prompt ~38-42K cache write）。transcript usage 欄位為占位值不可用（G：workflow transcript 的 per-message usage=3-4 tok，量測需以內容長度估算）。

## 判讀

1. **Correctness 天花板效應**：此難度（LRU cache 3 bug + 標準期望值）**全部模型在 low effort 即全對**——low→medium 在本題組買不到正確性，只買到 T3 敘述深度（sonnet-medium t3 ×4.5 長）與更多邊角 finding。
2. **廣度排序（T1 條數）**：fable-low(6) > opus-low = sonnet-low = sonnet-medium = fable-medium(5) > opus-medium = haiku(4)。fable-low 廣度最高且成本低於 opus 兩檔——「Fable-low ≈ Opus low~medium 帶」與前輪 6 組態結論一致。
3. **成本結構**：haiku-low 以 ~1/11 fable-low 成本拿到 4/6 廣度與全對 correctness；sonnet-low 以 ~1/5 成本拿到 5/6。**委派時 effort 預設 low 是安全預設**（本題組範圍內）；medium 只在需要長篇取捨分析（T3 型）時買得到東西。
4. **與既有規則關係**：支持 subagent-strategy「effort 先於 model」現行條文；**不支持**任何 SKILL/rule 行為變更（無「移除後在哪犯錯」的失敗案例；n=1 不過 core.md「≥2 次獨立重現才改規則」門檻）。

## 文件更新裁決（使用者要求評估 5 檔）

| 檔案 | 裁決 | 理由 |
|---|---|---|
| `.claude/refs/delegation-protocol.md` | ✅ 加 1 行資料點（附 n=1 標注） | L2 資料表，慣例允許單來源+信心標注 |
| `.claude/rules/subagent-strategy.md` | ❌ 不改 | auto-load byte 貼頂（18,999/19,000）+ 現行「effort 先於 model」已涵蓋，n=1 不足以加句 |
| fusion / multi-mode / pilot SKILL | ❌ 不改 | 三者路由紀律與本探測無衝突；加數據行=對強模型上手銬（雙軸伸縮），且無失敗案例支撐 |

**升級條件（記錄備查）**：同型探測換更難題組（correctness 有鑑別力）重跑 ≥2 次且結論一致 → 才夠格進 model-profiles §2 效能表。

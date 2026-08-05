# 模型 × effort 難題組重測（2026-07-17，鑑別力版）

> Workflow `wf_5f686adf-73d`；前輪（同日 easy 版）全組態天花板無鑑別力 → 本輪 4 難題：H1 asyncio 假 race 陷阱（正解=不是 race）、H2 Conway 模式期望值（=20）、H3 Python 語義精確輸出（print 引數別名陷阱）、H4 O(1) 多重集設計。n=1/組態。

## 結果（機械計分）

| 組態 | H1 陷阱 | H1 缺陷廣度 | H2=20 | H3 全對 | 正確率 |
|---|---|---|---|---|---|
| fable-low | ✅ | **6** | ✅ | ✅ | 4/4 |
| fable-medium | ✅ | **7** | ✅ | ✅ | 4/4 |
| opus-low | ✅ | 5 | ✅ | ✅ | 4/4 |
| opus-medium | ✅ | 5 | ✅ | ✅ | 4/4 |
| sonnet-low | ✅ | 3 | ✅ | ❌（`[1] [1, 2]`）| 3/4 |
| sonnet-medium | ✅ | 5 | ✅ | ✅ | 4/4 |
| haiku-low | ✅ | 3 | ✅ | ❌（同上）| 3/4 |
| haiku-medium | ✅ | 3 | ✅ | ✅ | 4/4 |

H3 失分點一致：sonnet/haiku 在 low 漏掉「print 兩引數先求值、預設參數同一 list → 兩者皆 `[1, 2]`」的別名效應。

## 判讀（n=1，資料表級信心）

1. **frontier/ceiling 帶（fable/opus）：low 即安全**——難題正確率不因 effort 降低而掉；medium 只加廣度（fable 6→7 缺陷）。
2. **quality/cost 帶（sonnet/haiku）：low 有微妙語義正確性風險，medium 修復**——與前輪「low 即天花板」結論**修正合併**：easy 任務全帶 low 安全；tricky 語義任務 sonnet/haiku 需 medium。
3. **Fable-low 定位確認（兩輪一致）**：正確率 = opus 任一檔、缺陷發現廣度高於 opus-medium——「Fable-low ≈ Opus medium 帶、廣度更優」。
4. 委派 effort 路由啟示（併入 delegation-protocol 既有 n=1 行的後續證據）：`fable/opus → low 預設；sonnet/haiku → 機械任務 low、語義敏感任務 medium`。

## 升級條件

同題組（或同難度新題）重跑 1 次結論一致 → 夠格改寫 delegation-protocol 資料點為 n=2 並考慮進 model-profiles §2。

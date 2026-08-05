# v5-baseline eval 族退役紀錄（2026-08-02）

> **這份檔案是墓碑，不是報告。** 它存在的唯一理由：被刪掉的那 21 個檔案裡有一部分知識
> 不在別處，而規則要求「刪含唯一知識前先抽出併入接收檔」（`core.md` §APPLY）。
> 使用者裁決：全族退役，含 fixtures 與現行 refs（2026-08-02，已於提出後果後再次確認）。
> 歷史 run 產物（`research/evals/runs/**`）**不刪**——`model-profiles.md` §122 仍引用它們當證據。

## 1. 刪了什麼

**執行工具（7）** `run-v5-baseline-matrix.py`、`run-v5-baseline-arms.py`、
`judge-v5-baseline.py`、`qualify-judge-v5.py`、`analyze-v5-baseline.py`、
`score-v5-baseline-semantic.py`、`assess-v5-fixture-signal.py`

**完整性守門（4）** `build-v5-baseline-bundle.py`、`check-v5-baseline.py`、
`check-v5-freshness.py`、`select-v5-smoke.py`

**回歸絆線（2）** `regress-evalpack-v5.sh`、`score-evalpack-v5.sh`

**測試（8）** `test-{run-v5-baseline-matrix,check-v5-baseline,check-v5-freshness,select-v5-smoke,v5-baseline-integration,build-v5-baseline-bundle}.sh`、
`test-{assess-v5-fixture-signal,score-v5-baseline-semantic}.py`

**資料（`research/evals/v5/`）** `fixtures/v5-baseline-{1,2}.json`、
`fixtures/v5-historical-invalid.json`、`DEPENDENCY-MAP.json`、`MANIFEST-SCHEMA.json`、
`examples/`、`assessments/`、`README.md`

## 2. 它證明過什麼（結論保留，工具不保留）

- **198-cell 矩陣（2026-07-28，22 fixtures × 3 models × 3 reps）**：Sol 84.85%（56/7/3）、
  Terra 83.33%（55/11/0）、Luna 62.12%（41/25/0）。judge 資格：sensitivity 93.94%、
  specificity 100%、fabricated/missing evidence 皆 0。**標記為 experimental、從未 formal
  promotion**，不得作為 formal cross-run delta。證據鏈仍在
  `research/evals/runs/v5-baseline-20260728-complete/scoring/`。
- **225-cell v5-baseline-2（2026-07-29）** 的訊號分層：8 題有鑑別力（H5, I2, V1, V2, V3,
  V6, V8, V10）、16 題屬校準、1 題未量測（V4 缺 Sol 語意結果）。權威清單在
  `runs/v5-baseline-2-20260728-partial/scoring/semantic/fixture-signal.json`，非任何散文摘要。
- **為何一直沒轉正**（這條最該記住）：不是「再跑一輪就好」。`SPEC-v5.md` #6 未解——
  三臂全載 harness 故**無對照臂**；且 22 題中作者標註的鑑別力與實測有 8 題不符。
  `model-profiles.md` §122 曾寫「缺的只是用全新回應跑出 baseline」，該敘述已被實測推翻。
- **語料真偽先於語料品質**（已入 `LESSONS.md`）：`run-v5-baseline-arms.py` 的 `dead_reason()`
  在 144 格中判出 97 格死格；judge 判前先拒判死格。工具沒了，教訓留在 LESSONS。

## 3. 退役後**確實失去**什麼（不粉飾）

1. **行為等價的 rollback oracle 沒有了。** `context-engineering-claude5.md` 的
   `rollback_signal` 原本是「跑 `regress-evalpack-v5.sh --check`，判定翻轉即 `git revert`
   本次精簡」。現在沒有任何機械手段能回答「這次剪枝有沒有改變行為」。
   **剩下的全是結構性收據**：`healthcheck.sh`（195 項結構檢查）、
   `harness-tpki-probe.sh`（L1 契約數字，人工 diff）、
   `scripts/tests/test-skill-router-routing.sh`（路由品質絆線，12 題）。
   結構綠 ≠ 行為未變——這個缺口是**已知且未補**的，不要在未來把 healthcheck PASS 當成
   行為等價證據引用。
2. **fixtures 的完整性守門沒有了。** 原本 `build-v5-baseline-bundle.py --check` 驗
   content-address、`check-v5-freshness.py` 驗依賴閉包是否漂移。fixtures 本身也已刪除，
   故此點隨之消失，但若日後從 git 歷史取回 fixtures，**必須連守門一起取回**——
   沒有守門的凍結集會在無人察覺下腐化。
3. **換代程序少了一半。** `model-profiles.md` 的新模型接入原為「跑 v5 fixtures + 代表任務組」，
   現只剩後者，即接入判準退回人工判讀。

## 4. 要復原怎麼做

全部 git-tracked，退役 commit 之前的任一 ref 都可取回：

```bash
git log --oneline -- scripts/regress-evalpack-v5.sh | head -3
git checkout <退役前 commit> -- scripts/regress-evalpack-v5.sh scripts/score-evalpack-v5.sh \
    research/evals/v5/fixtures/
```

⚠️ 本容器是 shallow clone（`git rev-parse --is-shallow-repository` = true）——歷史可能不含
更早的 commit，必要時先 `git fetch --unshallow`（`LESSONS.md` 2026-07-31-E）。

## 5. 這次退役同步改了哪些現行規則

| 檔 | 原本 | 改為 |
|---|---|---|
| `.claude/refs/model-profiles.md` §換代程序 | 跑 v5 fixtures + `regress-evalpack-v5.sh --check` | 只剩代表任務組 + 逐數字標來源日期；明記 fixture 背書已退役 |
| `.claude/refs/maintenance-protocol.md` `eval_fixture` 欄 | 指向 `v5-baseline-{1,2}.json` 與 `regress --check` | 指向現存的機械檢查（healthcheck／`scripts/tests/`），並明記無行為等價 oracle |
| `.claude/refs/context-engineering-claude5.md` `rollback_signal` | `regress-evalpack-v5.sh --check` 判定翻轉 | 降為結構性訊號 + 人工判讀，缺口顯式標注 |
| `.claude/workflows/INDEX.md` | 「v5 改用 `score-evalpack-v5.sh`」 | 標注該路徑亦已退役 |

## 6. 未決

**要不要重建一個行為等價 oracle？** 目前無候選。重建的最低要求（從這次失敗學到的）：
① 必須有**不載 harness 的對照臂**，否則量的是模型不是 harness；
② fixture 的鑑別力必須**實測**而非作者標註（上次 22 題錯 8 題）；
③ 凍結集必須同時凍結**依賴閉包**，否則 harness 一改，baseline 靜默失效。
在補上之前，任何「精簡後行為不變」的宣稱都只有結構性依據，應照實說明。

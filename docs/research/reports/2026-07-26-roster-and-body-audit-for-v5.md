# .claude Roster + Body 稽核（v5 打掉重來的前置量測）

> 2026-07-26 · 執行：`.claude/workflows/skill-roster-audit.js`（7× quality lens worker + 1× ceiling 合成）+ parent 親跑確定性 gate
> 目的：使用者要求「優化和刪除與精鍊 .claude 的所有檔案」，本報告先量測**有多少可刪**，避免在乾淨的機構上做破壞性重寫。

## 0. 結論（先講）

**`.claude` 的機構層是乾淨的；「刪檔省 token」這條路已被量測封死。**

| 路徑 | 量測 | 判定 |
|---|---|---|
| 壓 skill/agent `description` | 45 項 19,976 bytes，前 12 大僅佔 39%、中位數 411 bytes、無離群值 | ❌ 死路（分佈平坦，要動全部 45 項才有量級效果，而那正是傷路由） |
| 刪/併 skill/agent 減少項目數 | 12 個 overlap cluster → 5 candidate → **僅 1 項真能減項**，淨省 406 bytes（2.0%） | ❌ 近乎死路 |
| 刪 hooks | 26 檔、**25 已接線、0 孤兒**、11 hard-block / 14 advisory | ❌ 無死碼可刪 |

使用者感知的「harness 沒跟上 Loop Engineering 與 Graph Engineering」**是教義過時，不是檔案臃腫**。v5 的價值在重寫條文，不在砍檔。

## 1. Roster 稽核結果（5 candidate，全數過 parent gate）

| # | 對象 | 動作 | 淨 bytes | 要點 |
|---|---|---|---|---|
| 1 | `harness-core` → `harness-meta` | merge | **−406** | 唯一真減項（45→44）。兩者 description 都直寫「四層／L1-L4」，router 每 session 消歧。**執行前提**：`:export`/`:apply` 觸發詞須逐字保留（166 bytes 已計入），否則「換模型／接入非 Claude 環境」的低頻高代價入口發現率下降 |
| 2 | `deep-understanding` | sharpen | −92 | 與 `know-your-unknowns` 在 `teach me`/`教我懂` 字面碰撞；後者是 L1 canonical 不可動，故修前者。**嚴禁升級為 merge**（教人 vs 挖未知是不同主體） |
| 3 | `harness-meta` | sharpen | 0 | `Dream Pass` 與 `dreaming-consolidator` 觸發詞對撞，且誤路由會實跑 `scripts/dream.py`（約 $4/run）。花 bytes 買防錯 |
| 4 | `ship` | sharpen | 0 | 排除子句漏了「已有 PR、只要 gate-then-merge」→ `verified-merge`。兩者皆不可停用（後者是 merge 前 4 道不可逆閘門） |
| 5 | `memory-compactor` command/agent | sharpen | 0 | **偽陽性攔截**：lens 判為 `duplicate` 建議 merge，合成者反駁成功 |

### 1.1 合成者主動擋下的偽陽性（本次最有價值的單一輸出）

lens worker 把 `memory-compactor` 的 command 與 agent 判為重複並建議合併。ceiling 合成者查證後反駁，parent 以 grep 重驗確認：

```
.claude/commands/memory-compactor.md:11   wc -l memory/MEMORY.md
.claude/commands/memory-compactor.md:13   若 ≤ 200 行 → 回報「未達壓縮門檻」並結束。
.claude/commands/memory-compactor.md:15   超過 200 行 → 委派 memory-compactor sub-agent 執行壓縮
```

command 在主 context 親跑門檻預檢後才委派——這正是「確定性 gate main 親跑，不跨 agent 邊界」要求的形狀。**合併等於把 gate 推進 sub-agent，以省 110 bytes 換掉一道閘門**，是清單中報酬最差、風險最高的交易。

## 2. Body 層盤點（parent 親跑，確定性）

26 檔 221,763 bytes，`settings.json` 接線 25 個，**孤兒 0、接線但檔案不存在 0**。

**hard-block（11）**：`block-dangerous.sh`（41KB，最大）· `branch-isolation-guard.sh` · `merge-gate-mcp.sh` · `post-edit.sh` · `pre-commit-review.sh` · `pre-compact.sh` · `protect-sensitive-files.sh` · `session-init.sh` · `test-integrity-guard.sh` · `usage-delegation-gate.sh` · `user-prompt-submit.sh`

**advisory（14）**：`audit-permission` · `blindspot-domain-lint` · `gate-widening-guard` · `literal-specialcase-lint` · `memory-pr-record` · `memory-sync` · `post-compact` · `pre-push-cost` · `session-end` · `session-stop` · `taste-reference-lint` · `test-file-redflag` · `tool-log` · `unicode-covert-channel-guard`

> advisory 群的已知結構性弱點（SPEC-v4 §6 #2c 實測）：exit 1 的 stderr **不進 acting agent context**，hook 開火但模型看不見——這是 F7/F15 紅軸四輪不動的歸因。v5 若要動 Body，**這裡才是槓桿**（把有價值的 advisory 升為 exit 2），而不是刪檔。

## 3. Graph Engineering 自我教訓（本次 run 自身的 ROI）

本次 workflow 花 **549,448 subagent tokens** 找到 **406 bytes/session** 的節省。以任何算法都是負 ROI。

`[對已最佳化的資產跑 audit sweep]` → `[先用確定性量測估上界，再決定要不要 fan-out]`

**這條要進 v5 的 Graph Engineering 章節**：fan-out 前先問「這件事的**節省上界**是多少？」——上界可用確定性命令估出來時（如本例：description 總量 20KB、分佈已知平坦），就不該用 8 個 agent 去確認一個 bash 能算出來的結論。廣度發現只在「不知道有多少東西可找」時才划算。

---

> 收據：candidate 路徑存在性 6/6 通過；evidence 逐字 grep 5/5 命中 digest；memory-compactor 反駁主張經 grep 獨立確認。

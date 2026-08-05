# Claude 5 三模型 Harness 稽核合成報告（Fable 5 / Opus 5 / Sonnet 5）

> 目的：驗證 2026-07-31 三輪修正（停用兩支零真陽性 advisory hook、byte 門檻回錨 20,400/23,000、core.md OBSERVE/PROPOSE 程序句刪除、97 污染格刪除）是否符合 Claude 5 系列模型設計——能力最大化、效率、成本與 system prompt 最小化。
> 方法：三個 fresh-context sub-agent 分別綁 claude-fable-5 / claude-opus-5 / claude-sonnet-5，唯讀全 repo，各自親跑確定性量測。parent 對帳：Opus 回報之 19,858 bytes / measure GATE PASS / healthcheck 248-0-0 與 parent 親跑一致。
> 標籤：判斷部分 = assisted_verified_success（確定性數字已對帳；判斷無確定性 oracle）。

## 1. 四項修正三方判定矩陣

| 修正 | Fable 5 | Opus 5 | Sonnet 5 |
|---|---|---|---|
| ① 停用 blindspot-domain-lint / loop-charter-gate | 符合（推理預算調解稅移除，乘法級） | 正確，本輪最有價值 | 恰當，非誤傷（本就恆 exit 0） |
| ② byte 門檻回錨 20,400/23,000 | 符合，方向正確 | 正確；「餘裕=預先授權成長」是反 Goodhart 設計 | 方向正確，PROVISIONAL 應視為未定案 |
| ③ OBSERVE/PROPOSE 兩句刪除 | 符合，取捨精準 | 正確但低收益；regress 是絆線非行為 eval | **PROPOSE 句可、OBSERVE 句對 quality 檔位偏深，建議回補** |
| ④ 97 污染格刪除 | 符合（壞 oracle 直接應用） | 正確；實質是保護閘門非剪枝（假結論曾指向錯誤剪枝方向） | 符合，收據齊 |

**唯一分歧**：OBSERVE「讀 exports + caller + utility」句。Sonnet 5 指出 context-engineering-claude5.md §3.5 檔位警示——「無退化」實證只涵蓋 advanced 檔位，quality 檔位執行 sub-agent 任務時具體枚舉「讀什麼」仍有價值；Fable/Opus 判定已內化。2:1 維持刪除，rollback_signal 已上膛（範圍遺漏型失誤重現 ≥2 次即回補）；Sonnet 給的精簡回補寫法留存於本檔供觸發時使用：「改動前讀 exports + 直接 caller + 共用 utility；不清楚現有設計為何如此，先問再動」。

## 2. 閘門強度：三方一致零誤傷

hard-block 類（block-dangerous / protect-sensitive-files / test-integrity-guard / test-file-redflag / pre-commit-review / gate-widening-guard / branch-isolation-guard）全數在掛、exit 2 路徑完好；§TEST 條文三輪剪枝一字未動；byte gate 反向收緊。唯一降級 = clause 4e7858ae `[E]`→`[E*]`，已登記缺口與回掛條件，非靜默消失。

## 3. 三方共同結論：下一輪主戰場不在 rules

- rules 側 19,858 bytes、餘裕 542（2.7%），剩餘 `[P]` 候選合計僅 ~400 B——不值得單獨開輪，當「淨零增長」的抵扣額度即可（Opus 已逐條列出候選：/rewind 計數句、既有慣例與 output-discipline 同源重複、G1 教學句、compact delta hint 句、迷失例句、L5 整節）。
- **skills/agents description 實測 18,543 bytes ≈ rules 等量的第二座稅，卻無 byte gate**（skill-roster-audit 的 never-triggers 判準因 telemetry 稀疏停用）。pilot / multi-mode-skill / quality-pipeline 的 trigger 同義詞枚舉屬過度枚舉（規則 2：表達力強的 interface 勝過窮舉）。
- **CLAUDE.md 雙重注入**（global 鏡像 + project，逐字相同 ~1.4k B/回合）違反規則 4 去重複；且注入快照可能落後 repo（剪枝 repo 生效、注入層失效的靜默漂移風險）。建議 global 側改空指針並確認快照更新機制。
- 量測口徑應擴至「實際注入總量」（rules + CLAUDE.md×注入次數 + descriptions + hook 注入 ≈ 43.2k bytes），目前 gate 只治理一半。

## 4. 待裁決事項（人閘）

1. `verification-waiver-gate.sh`：證據基礎已撤回（剩 pilot B11 n=2），Fable/Opus 皆點名依同判準應入下輪停用候選（30 天窗與本輪兩支同步覆審）。
2. `taste-reference-lint.sh` 路徑錯配：掛 PreToolUse[Agent|Workflow] 但目標行為在使用者直接請求路徑——名實落差比被停用的兩支更大，且有明確修法（加掛 UserPromptSubmit）。
3. Opus 建議把 advisory hook 治理定為節拍：「advisory 預設 30 天觀察期，期滿無真實觸發自動退役 retired/」——把一次性人工裁決制度化。
4. `loop.md §L5` 自認無補 Body 路徑，依 Framework Integrity 已達可剪門檻——留文件價值或剪，需裁決。
5. 回掛條件的觀察者問題（Opus）：hook 停用後不再有觸發紀錄，「本應被攔的失誤」需獨立觀察者（如 LESSONS 記錄觸發回掛檢視）。
6. Sonnet 的 OBSERVE 回補提案（見 §1）。

## 5. 結構性摩擦（三方各報一個）

- **Fable 5**：CLAUDE.md 雙重注入 + 注入快照過期（見 §3）。
- **Opus 5**：委派拓撲與驗證拓撲不同構——graph.md 鼓勵稽核外派，core.md §TEST 要求裁定收回 parent 親跑；對「產出即判斷」的稽核任務，sub-agent 結構上只能交付 assisted_verified_success。此為 loop.md §L1 verifier 分離缺口的鏡像。
- **Sonnet 5**：gate-widening-guard 對唯讀 diff 操作的 lexical 假陽性（shell 重定向被當寫入動詞）——與 waiver-gate 同族的 lexical 上限問題。

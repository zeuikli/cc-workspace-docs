# Opus 4.8 × System Prompt × Harness:2.1.154 起的改動深度研究

> **Type:** wiki:compiled — Opus 4.8 行為位移如何驅動 CC system-prompt 與 harness 改動
> **Updated**: 2026-06-03 | **Consumer**: `harness-meta` skill、`subagent-strategy.md`、`context-management.md`
> **範圍**:Claude Code v2.1.154 -> v2.1.161
> **三源接地**:
> 1. CHANGELOG（[Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts/blob/main/CHANGELOG.md)）
> 2. system-prompts 原始檔（[同 repo /system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts/tree/main/system-prompts)）
> 3. [Dynamic Workflows Harness 報告](dynamic-workflows-harness-2026-06-03.md)（本系列前篇)
>
> **方法**:gh API 取 CHANGELOG + 6 個關鍵原始檔（migration-guide 908 行、model-catalog、tool-use-concepts、harness-instructions、workflow tool-desc、action-safety）逐行接地;版本號與檔名皆可回溯。Piebald 為第三方逆向歸檔,非 Anthropic 官方,版本對應以其 commit 為準。

---

## 0. 核心論點(一句話)

**v2.1.154 起的 system-prompt 改動,大部分不是新功能,而是對 Opus 4.8「行為位移」的 harness 補償**——Opus 4.8 更自主、更會 plan、但更保守於主動用工具/子代理、更會 narrate、更愛問。CC 用 prompt 再調校(ask-rate、narration、tool-triggering)解決「單一 context 內」的校準,用 **dynamic workflow harness** 解決「跨 context 的長/並行/對抗任務」。兩者是**同一套 Opus 4.8 適配的兩半**。

---

## 1. 全景:v2.1.154 -> v2.1.161 改動表

| 版本 | token | 與 Opus 4.8 / harness 相關的關鍵改動 |
|---|---|---|
| **2.1.154** | +11,516 | **Opus 4.8 落地大版本**:model catalog 加 Opus 4.8(1M/128K);API ref(cURL/Go/Py/TS)4.7->4.8;**Model migration guide 加 Opus 4.8 章**;Building-LLM-apps skill;Agent Design Patterns 改用 beta `role:"system"`;**Workflow tool-desc:ultracode 為 standing opt-in、首呼須 inline script、JSON args、純 JS 非 TS**;**AskUserQuestion 收緊(僅 blocked 時問)**;Coordinator worker 計量改 subagent tokens;background 暫存改 `$CLAUDE_JOB_DIR/tmp` |
| 2.1.156 | — | 無 prompt 改動 |
| **2.1.157** | +674 | **tool-use-concepts:tool description 應規定「何時呼叫」,特別為改善 recent Opus 的 should-call;Model migration guide:Opus 4.8 把 tool-triggering 指示放進「每個工具自己的 description」,不只 system prompt**;EnterWorktree 可 path 切換;Security monitor 擴充 |
| 2.1.158/159 | — | 無 prompt 改動 |
| **2.1.160** | +10,510 | **Workflow tool-desc:`ultracode` 改為「明確關鍵字」,自然語言「use a workflow」亦算 opt-in**(此版前字面觸發詞是 `workflow`);新增 /design-sync skill + DesignSync 工具;/code-review 重構(移除 part 4 三態驗證,改 recall-biased) |
| **2.1.161** | +64 | **Action safety:啟用 durable approval context 時,hard-to-reverse/outward-facing 動作的核准可跨 context 留存**(否則維持單 context 較嚴規則);Agent tool-desc:subagent-type 依「可用性」而非「訊息續傳」判定;Background monitor streaming |

> 旁註(範圍外但關鍵)——**2.1.152/2.1.153**:Workflow 關鍵字 `ultrawork->workflow`;/code-review 從 5 finder angle 擴到 9(加 reuse/simplification/efficiency/altitude);新增 Coordinator mode。這條線在 2.1.154 與 Opus 4.8 匯流。

---

## 2. Opus 4.8 模型事實(來源:data-claude-model-catalog.md)

| 屬性 | 值 |
|---|---|
| Model ID | `claude-opus-4-8` |
| context / output | **1M input**(標準定價,無長文溢價)/ **128K output** |
| thinking | **僅 adaptive**(`{type:"enabled", budget_tokens}` 會 400);省略 thinking 欄 = 不思考,須顯式設 `{type:"adaptive"}` |
| 移除 | sampling params(`temperature/top_p/top_k`)、`budget_tokens`、last-assistant-turn prefill — 皆 400 |
| structured_outputs | 支援 |
| effort | `low/medium/high/xhigh/max`(同 4.7) |
| API surface | **與 4.7 完全相同**——4.7->4.8 = model-ID 替換 + prompt 再調校,無新 breaking change |
| 定位 | 最強 GA 模型;state-of-the-art 長程 agentic、knowledge work、memory;文筆更暖、更少 hedge |

---

## 3. Opus 4.8 的六大行為位移(來源:skill-model-migration-guide.md §794–890)

這是理解所有 system-prompt 改動的鑰匙。Migration guide 明列「不破壞程式碼,但 4.7 調的 prompt 會落點不同」的 6 點:

| # | 行為位移 | 方向 | 官方建議的 prompt 補償 |
|---|---|---|---|
| B1 | **Tool-triggering 依表面而定** | search 略增但每次跑更少輪;**knowledge 檢索觸發變少**;有 system prompt 時 high-precision/low-recall | 加 `<search_first>` 指示;open-ended research 立即搜不先問 |
| B2 | **Under-utilization of subagents / memory / custom tools** | 對「需顯式決定才用」的能力更保守,非相當確定不出手 | **明說「何時」用每個能力**;且把觸發條件放進**每個工具自己的 description**(2.1.157),不只 system prompt |
| B3 | **更多 user-facing narration** | tool call 之間話更多、結尾 wrap-up 更長 | **移除**「每 N 次 tool call 摘要」舊 scaffold;太吵則加 silence-default |
| B4 | **更 deliberate、更愛問** | 小決策(命名/預設值/等價方案)會停下來問,常以「Want me to also…?」收尾 | 加「小決策自決並註明、scope/破壞性動作才問」——CC 實測 ask-rate **−12pp** 且無 over-reach 增加 |
| B5 | **thinking disabled 時推理外洩** | 把推理寫進可見回應,顯得囉嗦 | 留 adaptive thinking 開;或「只回最終答案」 |
| B6 | **文筆更暖、更少 hedge** | 與 4.7 的精簡直接相反 | 重評為對抗 4.7 而加的 style prompt,可能已過頭 |

加上兩個**能力提升**:
- **長程 agentic 執行**:complex refactor / 過夜執行可無人工修正完成。要訣:**一個 well-specified 首輪給足完整規格 + 跑 high effort**;對應 CC `/goal`、CMA Outcome。
- **Effort 是要測的維度,非固定值**:4.8 智能上限更高,**預設 `high` 起跳並迭代**,別反射性 `xhigh`;關係非單調(高 effort 常**降低**總輪數與成本)。

---

## 4. 核心因果:行為位移 -> system-prompt 改動 -> harness

把 §1 的改動逐一對回 §3 的行為位移,因果就清楚了——**改動是補償**:

| system-prompt 改動(版本) | 補償哪個 Opus 4.8 行為 | 機制 |
|---|---|---|
| **AskUserQuestion 收緊「僅 blocked 才問」(2.1.154)** | B4 更愛問 | harness 層直接壓 ask-rate,呼應 migration guide「小決策自決」 |
| **tool-use-concepts「描述要規定何時呼叫」+ migration「triggering 放進工具自身 description」(2.1.157)** | B2 under-utilization、B1 tool-triggering | should-call rate 的結構性修復——把觸發條件下沉到工具描述層 |
| **Workflow:ultracode standing opt-in、首呼 inline script、純 JS(2.1.154);ultracode 成明確關鍵字(2.1.160)** | B2(尤其 subagent 委派保守) | 把「編排子代理」變成**顯式可觸發的一級結構**;4.8 不主動 fan-out,就用關鍵字 + 工具把它叫出來 |
| **/code-review 改 recall-biased(PLAUSIBLE-by-default、移除三態 part 4)(2.1.152/2.1.160)** | B4/「be conservative 被字面遵守 -> recall 掉」 | report-everything-filter-downstream;對抗 agentic laziness |
| **Coordinator worker 計量 total->subagent tokens(2.1.154)** | 長程 agentic + 多 worker | 多代理執行下的成本歸因正確化 |
| **Action safety:durable approval 跨 context 留存(2.1.161)** | 長程自主執行 | 過夜/長 run 不必每 context 重新核准;與 workflow 背景執行相容 |
| **Agent Design Patterns / API ref 改 beta `role:"system"` mid-session(2.1.154)** | (cache 友善 + prompt-injection 安全) | 中途送 operator context 不動 top-level prompt、不毀快取——對齊本 workspace `context-management.md` static-first |

---

## 5. 與 Dynamic Workflow Harness 的接合(兩半同源)

[前篇報告](dynamic-workflows-harness-2026-06-03.md)指出 workflow harness 解三大失敗模式:**agentic laziness / self-preferential bias / goal drift**。把它與本篇對齊:

1. **為何 4.8 才有 dynamic workflow**:Thariq 文章明言「With Claude Opus 4.8, Claude is now intelligent enough to write a custom harness tailor-made」。即 §3 的**長程 agentic + 一次給足規格 + 高 effort 規劃**能力,正是「讓 Claude 即時寫出可用 harness」的前提。harness 是 4.8 規劃能力的下游應用。

2. **失敗模式被 4.8 的自主性放大**:更長 horizon + 更高自主 -> 一旦 drift/lazy/自我偏袒,代價更大。於是需要兩種對策:
   - **單 context 校準**(prompt 再調校):ask-rate、narration、tool-triggering —— §4 的改動
   - **跨 context 結構**(dynamic workflow harness):把 loop/分支/中間結果搬進確定性 JS,各 subagent 拿乾淨 context —— 前篇 §3

3. **「給足規格 + /goal」= harness 的 spec-first**:migration guide 的「single well-specified initial turn」與 workflow「指令碼保存計畫、Claude context 只留最終答案」是同一哲學的兩種落法。

4. **B2 + workflow opt-in 的張力**:4.8 *不主動*委派子代理(保守),但 workflow 需要*大規模* fan-out。解法是把編排做成**顯式觸發**(`ultracode` 關鍵字 / standing opt-in / 工具描述明說何時用),而非寄望模型自發。這解釋了 workflow tool-desc 為何反覆強化 opt-in 語言(2.1.153->154->160)。

---

## 6. Workflow 關鍵字演進史(harness 成熟的時間線)

| 版本 | 觸發詞 | 語義變化 |
|---|---|---|
| ≤2.1.152 | `ultrawork` | 初始 opt-in 關鍵字 + 單階段 workflow 範例、跨輪串接、ToolSearch 取 MCP |
| 2.1.153 | `ultrawork`->`workflow` | 改名;model override 預設省略(繼承 session model);加 exhaustive-review(dedup against all seen、perspective-diverse verify、loop-until-dry) |
| 2.1.154 | `workflow` | ultracode 成 **standing opt-in**;首呼須 inline script;JSON args;明示純 JS 非 TS |
| 2.1.160 | `workflow`->**`ultracode`** | ultracode 成「明確關鍵字」;自然語言「use a workflow」亦算 opt-in |

> 與 [code.claude.com/docs](https://code.claude.com/docs/zh-TW/workflows) 一致:「在 v2.1.160 之前,字面觸發關鍵字是 `workflow`」。關鍵字三度更名,反映 harness 從實驗(ultrawork)-> 泛用(workflow)-> 與 effort 整合(ultracode = xhigh + 自動協調)的定位收斂。

---

## 7. 對本 workspace 的影響

1. **本 workspace 的 ultracode 用法已對齊官方**:CLAUDE.md §模式與 Effort 將 `ultracode` 定為「xhigh + dynamic workflow」,與 2.1.160 後官方語義一致。可在 `pilot-shared-preflights.md §E` 註記版本依據。

2. **B4(更愛問)↔ output-discipline**:workspace「無開場白/精簡輸出」已部分對抗 4.8 narration(B3);但 ask-rate(B4)目前無顯式規則。建議在 `core.md §R1` 或 output-discipline 補一句「小決策(命名/格式/等價方案)自決並註明;scope/破壞性才問」——官方實測 −12pp,且不違反 R1 不可逆例外。

3. **B2(under-utilization)↔ subagent-strategy**:workspace 的「委派決策表」是讓 Claude *更*會委派的觸發條件,方向正確;但可吸收官方洞見——**把觸發條件下沉到工具/skill 描述層**(2.1.157),而非只在 rule。`media-research` 等 skill 的 description 已含「Use when…」,符合此原則。

4. **前篇待決的 Fan-out 衝突仍在**:subagent-strategy「上限 4」(手動委派)vs workflow「16 並行」(自動協調),層級不同。本篇補一條依據:4.8 *保守*於自發委派,故手動上限 4 是合理的人因節流;workflow 內並行交 runtime cap,兩者不混用。建議 `/autoload-evolution` 一併處理。

5. **adaptive thinking 必設**:省略 thinking 欄 = 不思考(B5)。若 workspace 任何 API 呼叫腳本(scripts/)走 Anthropic SDK,應顯式設 `{type:"adaptive"}`——待查 scripts/ 是否有裸呼叫。

---

## 8. 開放問題

- [ ] **harness-instructions 檔停在 ccVersion 2.1.139**:核心 `# Harness` 身分段(markdown 輸出、permission、system-reminder、parallel tool calls、code reference)在本範圍**未變**——Opus 4.8 的適配全發生在**周邊**(工具描述、skill、migration guide、AskUserQuestion),核心 harness 身分穩定。值得記入 RATCHET:**模型換代時,harness「核心契約」不動,動的是「行為校準層」**。
- [ ] 驗證本 workspace `scripts/` 中 Anthropic SDK 呼叫是否顯式設 adaptive thinking(§7.5)。
- [ ] §7.2 ask-rate 規則是否值得進 auto-load(走 `/autoload-evolution`,≤1 規則/cycle)。
- [ ] Piebald 為第三方歸檔;關鍵結論(尤其 token 數、commit 對應)若要正式引用,宜與官方 release notes 二次交叉。

---

## 9. 參考

- CHANGELOG v2.1.154–161（[Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts/blob/main/CHANGELOG.md)）
- 原始檔:`skill-model-migration-guide.md`（§Migrating to Opus 4.8）、`data-claude-model-catalog.md`、`data-tool-use-concepts.md`、`tool-description-workflow.md`、`system-prompt-harness-instructions.md`、`system-prompt-action-safety-and-truthful-reporting.md`（[/system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts/tree/main/system-prompts)）
- 前篇:[Dynamic Workflows Harness 三層拆解](dynamic-workflows-harness-2026-06-03.md)
- Thariq 文章歸檔:[A harness for every task](../tweets/2026-06-02-@trq212-367865.md)
- 官方文件:[code.claude.com/docs/zh-TW/workflows](https://code.claude.com/docs/zh-TW/workflows)
- workspace 內部:`CLAUDE.md §模式與 Effort`、`.claude/rules/{core,subagent-strategy,context-management,output-discipline}.md`

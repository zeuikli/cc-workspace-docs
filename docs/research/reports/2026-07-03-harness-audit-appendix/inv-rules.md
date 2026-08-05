# 稽核報告：auto-load 六源 + refs 22 檔 + AGENTS.md

六源實測 = 18,988 bytes（core.md §Framework Integrity 命令重跑一致）。

## 1. 重複條文

| 配對 | 重複內容 | 程度 |
|---|---|---|
| core.md 全文 vs the-loop-best-solution.md 全文 | 六階段逐條「核心要求」句幾乎一對一映射（OBSERVE 讀 exports/caller、IDENTIFY 顯露假設+成功條件、PROPOSE Rule of 3+四大缺陷、APPLY 規範優先、TEST Fail Loud/PGE、RECORD Checkpoint） | 高（設計上属精簡版/詳解版分工，非噪音，但核心句幾乎一字不差重述） |
| core.md:78 vs prompt-lifecycle.md:41 | byte 門檻 13,000/19,000 三段定義 | 中（prompt-lifecycle 補「90 天重審」，非純複製） |
| AGENTS.md §2 vs subagent-strategy.md 全文 | Agent Dispatch 表格 vs T0/T1/T2 分層+委派決策 | 低-中（AGENTS.md 明標「Full dispatch table→subagent-strategy.md」，屬有意的 TLDR/Full 分工） |
| subagent-strategy.md:9-13（T0/T1/T2）vs agent-team-patterns.md:36-51（常駐協作協定） | 分層判準、互審鏈幾乎逐句重複（agent-team-patterns 多了 2026-07-03 PR #806/#807 實證數據） | 高 |
| core.md:78 fan-out 隱含 vs subagent-strategy.md:23 vs agent-team-patterns.md:29/46 | 「Fan-out 上限 4」同句在 3 檔重複出現 | 高 |
| CLAUDE.md:21-23（常駐拓撲/Effort/檔位覆寫）vs subagent-strategy.md 全文 vs agent-team-patterns.md | 主對話=調度者+總稽核、T0/T1/T2 三處重複描述 | 中-高 |

## 2. 矛盾條文（含軟性不一致）

- **無強矛盾**（未發現 A 說「禁止 X」、B 說「必須 X」的直接對立）。
- **軟性重複而非矛盾**：fan-out 上限「4」在 subagent-strategy.md:23、agent-team-patterns.md:29/46、harness-design.md:148 三檔皆為 4，數字一致但**同句話存在 3 處**，屬「該下沉未下沉」而非矛盾。
- **model-selection-grid.md 內部自洽的過渡態**：檔內同時出現「Sonnet 4.6」（表格列名）與註記「CC sub-agent `sonnet` alias 現解析至 Sonnet 5」——此為刻意保留的過渡註記，非矛盾，但**弱模型易誤讀**（見第5項）。
- **byte 門檻表述層級不一**：core.md 定義「三段門檻」，prompt-lifecycle.md 又定義「90 天重審」節奏，兩者未衝突但構成"門檻定義分裂在兩檔"，稽核時需交叉讀才能得到完整規則。

## 3. 失效指針（test -f 逐一驗證結果）

**全數通過**，六源 + AGENTS.md 內所有 @引用 / 反引號路徑 / `.claude/refs/*` 指針經 `test -f` 驗證皆存在，包含：
- core.md → `.claude/refs/git-ops.md`、`.claude/refs/harness-loop.md`、`.claude/refs/the-loop-best-solution.md`、`memory/LESSONS.md`、`memory/MEMORY.md`、`scripts/healthcheck.sh`、`.claude/skills/harness-meta/references/harness-meta-GOTCHAS.md` — 全 OK
- subagent-strategy.md → `.claude/refs/model-selection-grid.md`、`.claude/refs/multi-agent-coordinator-pattern.md`、`.claude/refs/agent-team-patterns.md`、`.claude/refs/error-handling.md` — 全 OK
- AGENTS.md → 全部 14 條路徑（含 `docs/harness-guidelines-workspace.md`、`research/agent-harness/{RESEARCH,HARNESS-CARD}.md`、`research/best-practices/INDEX.md`）— 全 OK
- `.claude/rules/INDEX.md` → `prompt-lifecycle.md`、`security-hygiene.md` — 全 OK
- refs/README.md 宣稱「19 個現存 ref」，實際目錄 20 個功能檔（扣 README/trigger-index）+ removed-content-manifest.txt = 22 個 .md/.txt 總數與任務描述一致，**表格逐項比對無缺漏**，僅「19」為表格內文件數（不含 README 自身與 trigger-index 索引檔），命名口徑正確非失效。

**結論：0 個失效指針。**

## 4. 過時內容（模型名稱/日期/數據）

| 檔案:行 | 內容 | 現況判定 |
|---|---|---|
| model-selection-grid.md 全文 | 表格主列仍用「Sonnet 4.6」「Opus 4.8」「Haiku 4.5」 | **檔案自身已含註記**聲明 pin=4.6 但 alias 解析到 Sonnet 5、Fable 5 access 已恢復 — 過渡性但非「未察覺的過時」，惟表格主體未同步更新型號名，僅靠底部長註記補丁，弱模型易只讀表格漏讀註記 |
| pilot-shared-preflights.md:26,34,54 | 「Opus 4.6」等舊型號字串（含歷史 benchmark 引用 Q13 "Claude 3.5 Opus" 為故意示例） | 部分為歷史 benchmark 案例（刻意保留，不算過時），部分為現行模型稱呼落後於 Claude 5 家族 |
| per-model-eval-suite.md、prompt-caching-rules.md、harness-loop.md、claude-oauth-token.md | 均含舊代模型字串 Sonnet 4.6/Opus 4.8/Haiku 4.5 | 需逐檔判斷是否為「歷史基準數據」（保留合理）或「現行操作指引」（應更新） |
| trigger-index.md、README.md（refs）| 日期戳最新至 2026-07-01/07-03 | 尚屬新鮮，非過時 |
| skill-gotcha-protocol.md | 最新日期 2026-06-11 | 相對新，非嚴重過時 |

**Fable 5 家族命名**：`fable5-harness.md`、`pilot-shared-preflights.md`、`harness-loop.md`、`multi-agent-coordinator-pattern.md`、`per-model-eval-suite.md`、`README.md`、`trigger-index.md` 均已提及 fable/Claude 5 家族，顯示 refs 已在同步中，非全面落後。

**结論**：無「全面過時」，但 model-selection-grid.md 主表格名稱與現況（settings pin claude-sonnet-4-6，但 alias 解析 Sonnet 5）存在**表格層級**與**註記層級**的資訊不同步，建議下次校準時把表格主列名稱改為現行 pin + 註記精簡。

## 5. 弱模型誤讀句 Top 10

1. `core.md:70` 「多 agent 輸出矛盾時明列交主對話，child 不 self-resolve（非使用者指令歧義）」— 雙重否定+術語堆疊，「非使用者指令歧義」修飾對象不明確，弱模型易誤解為「這不算歧義所以不用管」。
2. `core.md:58` unverified_success 整句 100+ 字單句塞 4 個條件（自報成功/中間態/親跑/絕不經 sub-agent 中介），弱模型易漏執行「確定性 gate 絕不經 sub-agent 中介」子句。
3. `subagent-strategy.md:19` Handoff Contract 單句列 7 個欄位 + 3 個附帶條件（parent 綁/child 不自切/驗收深度隨能力加嚴），資訊密度過高，無範例佐證，弱模型難以一次性正確套用全部欄位。
4. `subagent-strategy.md:45` Dynamic Workflow 一句混合 3 個失敗模式英文術語（agentic laziness/self-preferential bias/goal drift）+「verdict 非證據」，無範例，弱模型可能只記住術語不理解意涵。
5. `core.md:46` 「措辭 capability-agnostic（『match enforced style』優於指定工具名）」— 抽象度高，未舉範例前後對比，弱模型不確定「指定工具名」具體所指。
6. `context-management.md:19` Token Budget 句夾雜「非硬牆」+「行為信號優先於數字」+「常態例外」三層轉折，弱模型易套錯優先序（誤以為數字優先）。
7. `output-discipline.md:15` 「例外：①②③④→放寬 150 字上限」— 4 個例外用分類詞堆疊無具體觸發詞範例，弱模型難判斷「教學性文件」邊界。
8. `core.md:19` 「破壞性/高風險變更（含 harness 自我改進）→ APPLY 前置 gate（plan/diff/eval 預檢通過才套用）」— 未明確定義「高風險」判準，需讀者自行對照多個下游檔案（harness-loop.md）才能操作。
9. `subagent-strategy.md:12` T2 互審鏈「haiku→sonnet、sonnet→opus、opus/fable→model: fable worker 對抗終驗」— 條件式鏈狀規則單行塞 3 條映射，換行/表格化會更利解析，目前純文字弱模型易配對錯誤（例如 opus 產出該給誰審 vs fable 產出該給誰審 混淆）。
10. `core.md:65` 人工介入診斷句：「assisted-success ≠ autonomous-success——RECORD 須標此介入歸因到缺失的 harness 層（觀測層 vs 驗證層）」— 需要先理解「觀測層」「驗證層」定義（未在本檔定義，需外部知識），對弱模型是隱性前提缺失。

## 6. 下沉候選（僅提案，未執行）

目標：六源 18,988 → ≤13,000（需砍 ≥5,988 bytes / 31.5%）

| 段落 | 現存位置 | 下沉建議 | 估計節省 |
|---|---|---|---|
| CLAUDE.md「常駐拓撲與 Effort」整段（19-23行） | CLAUDE.md | 與 subagent-strategy.md/agent-team-patterns.md 三處重複，僅留 1 行指針「拓撲細節→subagent-strategy.md」 | ~350 bytes |
| subagent-strategy.md「常駐拓撲與委派分層」T0/T1/T2 全段（7-13行） | subagent-strategy.md | 已在 agent-team-patterns.md:36-51 有更完整版本（含 2026-07-03 實證）；rules 檔只留判準摘要+指針，細節單一 source of truth 放 refs | ~400-500 bytes |
| subagent-strategy.md:23 Fan-out 上限句 | subagent-strategy.md | 與 agent-team-patterns.md 重複，可留 1 行「見 agent-team-patterns.md §確定性 team-size」 | ~60 bytes |
| core.md RECORD 段「安全邊界」細節（獨立 evaluator/機械驗證/整合門控/退化可觀測，4 條並列） | core.md:64 | 4 條並列細節可移 the-loop-best-solution.md（已有更完整 RECORD 章節），core.md 留 1 句鐵律 | ~150 bytes |
| core.md「Framework Integrity」byte 門檻完整量測指令（含 wc -c 完整命令列） | core.md:78 | 命令本身可移至 refs（如 harness-loop.md 或新建量測腳本說明），core.md 留門檻數字即可 | ~150 bytes |
| context-management.md「監控」段 2026-07-03 實測數據細節（p50/p90 雙峰註記） | context-management.md:19 | 純數據，移 cache-health-metrics.md，本檔留「軟性參考 4k/30k，細節見 ref」 | ~120 bytes |
| output-discipline.md「優雅性自檢＋例外」整段（12-15行） | output-discipline.md | 例外清單為參考細節而非鐵律，可併入 the-loop-best-solution.md「情境速查表」 | ~200 bytes |
| README.md（rules）Auto-load/Path-scoped 兩表格 | .claude/rules/INDEX.md | 索引本質已最精簡，**不建議再砍**（此檔本身即為導航） | 0（保留） |

**加總估計節省**：~1,430–1,530 bytes，距目標 5,988 bytes 仍有缺口。**結論：僅靠"移除重複段落"無法把六源壓回 13,000**；若要達標，需要更激進的結構決策（例如把 subagent-strategy.md 的 T0/T1/T2 判準表格整段移出 auto-load，只留 1-2 句鐵律+指針），此屬 APPLY 前置 gate 範疇，非本次盤點可單方案決定，應交 `/autoload-evolution` 走 eval 回歸驗證。

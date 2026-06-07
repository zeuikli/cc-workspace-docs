# Dynamic Workflows 帶來的 Harness:深度研究

> **Type:** wiki:compiled — dynamic workflows 的 harness 實質拆解
> **Updated**: 2026-06-03 | **Consumer**: `harness-meta` skill、`subagent-strategy.md`
> **三源接地**:
> 1. Thariq & Sid Bidasaria 官方文章（[歸檔](../tweets/2026-06-02-@trq212-367865.md)）
> 2. 官方文件 [code.claude.com/docs/zh-TW/workflows](https://code.claude.com/docs/zh-TW/workflows)
> 3. Workflow runtime 契約（本 session 工具定義第一手）
>
> **方法論註**:官方文章圖 1/圖 3（特殊函數圖、pattern 圖）為圖片,fxtwitter API 未回傳 URL。其 API 層細節改以 runtime 契約補齊（最權威來源）,並標明出處層級。

---

## 0. 一句話結論

「Workflow 帶來的 harness」= **把原本由 LLM 在單一 context 內逐輪做的「協調」(loop / 分支 / fan-out / 中間結果保存),抽離成一支在隔離 runtime 執行的確定性 JavaScript 指令碼;LLM 退化為被該指令碼呼叫的、各自擁有乾淨 context 的 worker。** 這是把本 workspace R5(判斷 vs 決定)從「規則」升級為「執行結構」。

---

## 1. 「Harness」到底指什麼

Harness = 包在隨機性 LLM 外層的**控制鷹架**(scaffolding):決定 LLM 何時被呼叫、看到什麼 context、輸出如何被驗證與串接。

| | 預設 Claude Code Harness | Dynamic Workflow Harness |
|---|---|---|
| 協調者 | Claude 本身(逐輪決定下一步) | JavaScript 指令碼(執行時期執行) |
| 計畫 + 執行 | **同一個 context window** | 計畫在指令碼;執行分散到各 subagent |
| 中間結果存放 | Claude 的 context(累積污染) | 指令碼變數(不進 Claude context) |
| 可重複的東西 | 無(每次逐輪即興) | **協調本身**(指令碼可存、可重跑、可傳 args) |
| 規模 | 每輪委派數項 | 每次執行數十～數百 agent |
| 中斷 | 重啟該輪 | **同一 session 內可恢復**(已完成 agent 回快取) |

> 來源:官方文件「何時使用工作流程」對照表。關鍵句:「工作流程指令碼保存迴圈、分支和中間結果本身,因此 Claude 的上下文只保存最終答案。」

---

## 2. 為什麼預設 harness 會壞 —— 三大失敗模式

單一 context window 同時 plan+execute,任務一長/一並行/一對抗就退化(官方文章「Why dynamic workflows」):

| 失敗模式 | 定義 | 本 workspace 對應規則 |
|---|---|---|
| **Agentic laziness** | 多步任務做到一半就宣稱完成(50 項 security review 只做 20 項) | R4 目標導向 / R12 fail-loud(完成需可機械驗證) |
| **Self-preferential bias** | 偏袒自己的結論,尤其被要求自評/評分時 | subagent-strategy「synthesis 自報非證據,須機械 grep 重驗」 |
| **Goal drift** | 多輪後(尤其 compaction 後)對原始目標失真,`don't do X` 約束遺失 | R6 compaction hint / context-management「context 放 HEAD 或 TAIL」 |

> **核心洞見**:這三者都是「單一 context 持續變長」的必然產物。Harness 的解法不是更強的提示,而是**結構性隔離**——每個 subagent 拿到乾淨 context + 聚焦目標,協調邏輯則交給不會 drift 的確定性程式碼。

---

## 3. Harness 的實質內容 —— 三層拆解

dynamic workflow 的 harness 由三個平面組成。下表函數簽章來自 **runtime 契約**(最權威):

### 3.1 確定性控制平面(JS 指令碼本體)

指令碼在**隔離 runtime** 執行,與對話分開;可用標準 JS(`JSON`/`Math`/`Array`),但**不能**直接碰檔案系統或 shell——那是 agent 的事,指令碼只負責協調。

> 對應 R5:**確定性程式碼做「決定」**(路由 / 重試 / 計數 / 分支),**LLM 做「判斷」**(分類 / 摘要 / 生成)。Workflow 把這條規則變成執行結構。

例外限制(官方文件「行為和限制」):
- 無中途使用者輸入(只有權限提示能暫停);階段間要簽核 → 拆成各自獨立 workflow
- 最多 16 並行 agent(核心少的機器更少)
- 每次執行上限 1,000 agent(防失控迴圈)

### 3.2 Agent 執行平面 —— `agent()`

```
agent(prompt: string, opts?: {
  label?: string,        // 進度顯示用標籤
  phase?: string,        // 明確指派到某 progress group(避免 race)
  schema?: object,       // 給 JSON Schema → 強制 StructuredOutput,回傳已驗證物件
  model?: string,        // 'sonnet'|'opus'|'haiku' — 不給則繼承 session model
  isolation?: 'worktree',// 各自 git worktree(僅在 agent 並行改檔會衝突時用,昂貴)
  agentType?: string,    // 自訂 subagent type(如 'Explore'、'code-reviewer')
}): Promise<any>
```

- 無 schema → 回傳 agent 最終文字(string)
- 有 schema → runtime 層強制結構化輸出,model 不符會重試,回傳已驗證物件(免解析)
- 使用者中途 skip 該 agent → 回傳 `null`(用 `.filter(Boolean)` 過濾)
- 每個 agent = **獨立 context window**,可挑模型智能等級與隔離程度(呼應官方文章「workflow 可決定每個 agent 用什麼模型、是否在 worktree」)

### 3.3 協調原語平面

| 原語 | 簽章 | 語義 | 何時用 |
|---|---|---|---|
| `parallel` | `parallel(thunks: Array<()=>Promise>): Promise<any[]>` | **Barrier**:等所有 thunk 完成才回。失敗的 thunk 解析為 `null`(整體不 reject) | 需要「所有結果一起」才能進下一步(如全量 dedup、早退判斷) |
| `pipeline` | `pipeline(items, stage1, stage2, ...): Promise<any[]>` | **無 barrier**:每個 item 獨立穿過所有 stage,A 可在 stage3 而 B 還在 stage1。wall-clock = 最慢單鏈,非各階段最慢和 | 多階段處理的**預設**選擇 |
| `phase` | `phase(title: string): void` | 開新階段,後續 agent 歸入此 progress group | 進度可視化 |
| `log` | `log(message: string): void` | 對使用者輸出 narrator 進度行 | 標示被丟棄/截斷的工作(no silent caps) |
| `workflow` | `workflow(nameOrRef, args?): Promise<any>` | 內聯執行另一個 workflow(僅一層巢狀) | 多階段大任務串接 |

跨切面全域:
- **`args`**:呼叫時傳入的結構化輸入(已儲存 workflow 的參數化入口;省略則 `undefined`)
- **`budget`**:`{total, spent(), remaining()}` token 硬上限;`total` 為 null 表未設;達 `total` 後 `agent()` 拋錯。可做動態迴圈 `while (budget.total && budget.remaining() > 50_000)`

> **pipeline vs parallel 是 harness 設計的關鍵抉擇**:barrier 會浪費快 agent 的等待時間(5 個 finder,最慢是最快 3 倍 → barrier 浪費 2/3 idle)。預設 pipeline,只有「stage N 真需要 stage N-1 全部結果」(dedup/早退/跨項比較)才用 barrier。

---

## 4. Harness 啟用的六大品質 Pattern

官方文章列出 6 個可組合 pattern(圖 3);下表對應到 §3 原語與本 workspace 既有實作:

| Pattern | 機制 | 原語映射 | workspace 既有對應 |
|---|---|---|---|
| **Classify-and-act** | 分類 agent 決定任務類型 → 路由到不同 agent/行為 | `agent`(schema)+ JS 分支 | model routing、`/effort` 分流 |
| **Fan-out-and-synthesize** | 拆多步 → 各 agent 跑 → synthesize 合併(**synthesize 是 barrier**) | `parallel` + 合併 | `deep-research`、`gap-vote` |
| **Adversarial verification** | 每個產出 agent 配一個對抗驗證 agent | `pipeline`(stage2 驗證) | subagent-strategy 對抗驗證 |
| **Generate-and-filter** | 生點子 → 依 rubric/驗證過濾 → dedup → 只回最高品質 | `parallel` + `.filter` | autoresearch |
| **Tournament** | N agent 用不同approach競賽 → pairwise judge 到出贏家(**pairwise 比絕對評分可靠**) | 巢狀 `parallel` + 確定性 bracket | (新)排序/命名/taste 任務 |
| **Loop-until-done** | 未知工作量 → 循環 spawn 到 stop 條件(無新發現/無 error) | `while` + `agent` | loop-until-dry |

> 重點:**這些 pattern 不是 prompt 技巧,而是 harness 結構**。`parallel` 的 barrier 語義使 synthesize 成立;確定性 `while` 使 loop-until-done 不會 drift;`pipeline` 使 adversarial verification 邊產邊驗不浪費 wall-clock。

---

## 5. 觸發與運維(harness 的生命週期)

| 面向 | 內容 | 出處 |
|---|---|---|
| 觸發 | prompt 含 `ultracode` 關鍵字(單次);或 `/effort ultracode`(整 session 每項實質任務皆規劃 workflow,= xhigh + 自動協調) | 文件 |
| 自然語言 | 「use a workflow」等直接請求視為同等 opt-in | 文件 |
| 執行 | 背景執行,session 保持回應;指令碼寫入 `~/.claude/projects/<session>/`,開始時回傳路徑 | 文件 |
| 監控 | `/workflows` 看階段/agent 數/token/耗時;`p` 暫停、`x` 停、`r` 重啟 agent、`s` 儲存 | 文件 |
| 權限 | 啟動提示受 permission mode 控制;但**生成的 subagent 一律 acceptEdits**,繼承工具 allowlist;shell/網路/未允許 MCP 仍會提示 | 文件 |
| 恢復 | 同 session 內可恢復:已完成 agent 回快取結果,其餘實時跑;退出 CC 則下個 session 重啟 | 文件 + runtime(resumeFromRunId) |
| 儲存 | workflow menu 按 `s` → `.claude/workflows/`(repo 共享)或 `~/.claude/workflows/`(個人);未來以 `/<name>` 執行 | 文件 |
| Token budget | prompt「use 10k tokens」設上限;runtime 以 `budget` 全域強制 | 文件 + runtime |
| 成本警語 | 單次執行可能比對話完成同任務用**顯著更多** token;大任務前先在小片段試跑 | 文件 + 文章 |
| 關閉 | `/config` 切換、`disableWorkflows: true`、`CLAUDE_CODE_DISABLE_WORKFLOWS=1` | 文件 |
| 版本/方案 | 需 CC v2.1.154+;研究預覽;Pro/Max/Team/Enterprise + API/Bedrock/Vertex/Foundry | 文件 |

---

## 6. 與 subagent / skill / agent team 的界線

官方文件四象限的判準是**「誰掌握計畫」**:

- **子代理**:Claude 逐輪委派的 worker,結果進 Claude context
- **技能**:Claude 遵循的指示(計畫仍在 Claude)
- **代理團隊**:主導代理監督對等 session,共享 task list
- **工作流程**:**計畫在指令碼**,中間結果在變數,協調可重複、可大規模(數十～數百 agent)

選型口訣:需要 Claude 即興判斷下一步 → subagent/skill;需要把「協調本身」固化成可重跑、可大規模 fan-out 的結構 → workflow。

---

## 7. 對本 workspace 的影響評估

1. **R5 升格為結構**:workspace 一直主張「確定性程式碼做決定、LLM 做判斷」。Workflow 把這條從 CLAUDE.md 規則變成 runtime 強制——路由/重試/計數在 JS,分類/生成在 agent。可在 `subagent-strategy.md` 明示此對應。

2. **三大失敗模式 ↔ 既有規則**:agentic laziness→R4/R12、self-preferential bias→對抗驗證紀律、goal drift→R6。可作為官方權威背書,強化既有條文敘事。

3. **Fan-out 上限衝突點**:subagent-strategy 現定「Fan-out 上限 4」;workflow runtime 為「16 並行 / 1000 總量」。兩者層級不同(主對話手動委派 vs workflow 自動協調),**不應混用**——建議在 subagent-strategy 標註:手動 fan-out ≤4 維持;workflow 內並行交由 runtime cap(16),勿用 4 的人工上限去限制 workflow。(R7 浮現衝突,待 `/autoload-evolution` 決議)

4. **pipeline 預設原則可固化**:多階段 subagent 任務預設 pipeline(無 barrier),只有跨項依賴才 barrier——這是可寫進 skill 的高價值判準。

5. **dynamic workflow 幻覺風險**:subagent-strategy 已記「dynamic workflow(Opus 4.8)會幻覺 → verdict 非證據,須機械 grep 重驗」。本文 §3.2 的 `schema` 強制結構化輸出可降低解析錯誤,但**不降低內容幻覺**;對抗驗證 + 機械重驗仍必要。

---

## 8. 待辦 / 開放問題

- [ ] 圖 1(特殊函數圖)、圖 3(pattern 圖)、圖 4-8(use case 圖)為圖片未取得;若需逐圖細節,需從 Claude Blog 同文(官方文章註明亦發於 Claude Blog)補圖。
- [ ] `subagent-strategy.md` 的「Fan-out 上限 4」與 workflow「16 並行」需走 `/autoload-evolution` 釐清層級邊界(§7.3)。
- [ ] 可考慮把「pipeline 預設、barrier 例外」寫成 skill 判準(§7.4)。

---

## 參考

- Thariq & Sid Bidasaria, *A harness for every task: dynamic workflows in Claude Code*（[歸檔全文+評分 8.8/10](../tweets/2026-06-02-@trq212-367865.md)）
- 官方文件:[使用動態工作流程大規模協調子代理](https://code.claude.com/docs/zh-TW/workflows)
- Workflow runtime 契約(本 session 工具定義,API 簽章最權威來源)
- 相關 workspace 文件:[KNOWLEDGE-MAP.md](KNOWLEDGE-MAP.md)、[RESEARCH.md](RESEARCH.md)、`.claude/rules/subagent-strategy.md`

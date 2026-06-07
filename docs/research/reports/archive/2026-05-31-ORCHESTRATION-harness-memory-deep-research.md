# Orchestration：Harness Engineering ＋ LLM Memory 雙分類深度研究

> Driver: Opus 4.8 Low Effort｜語料: `research/papers/`（本地優先，web 為補充維度）
> 三 SKILL 分工: `research-hub:deep`（語料合成）→ `autoresearch:reason`（對抗論證）→ `overnight-research`（verify+commit 閘門）
> 輸出: `research/reports/` 兩份報告 + 本 orchestration 文件
>
> **狀態：已執行完成**（初次交付 #474）。**2026-06-05 增量更新**：對照當前 papers/INDEX 重核 in-domain 增量——Memory 側 0 篇未覆蓋（既有報告 28 篇全引）；Harness 側 4 篇新論文（ACON / AgentFlow / addyosmani-agents-md / configuring-agentic）已併入 harness 報告（§3 凍結清單已更新為 31，TODO 全標 done）。方法：researcher 深讀 + 主對話親自 grep 驗數字（不信 subagent 自報覆蓋率）。

---

## 1. 設計 Prompt（交付物本體）

### 共用前綴（注入每個 SKILL 呼叫）
```
本地語料 research/papers/ 為一級來源，禁止重抓磁碟已有內容；web search 僅用於補足
語料未覆蓋的維度（必要時）。每個論斷必須可回溯到具體論文檔名或 URL。繁體中文輸出。
覆蓋率檢核：報告結尾須列出本分類所有分配論文，標記「已引用 / 未引用＋原因」。
```

### 分類一 Prompt — Harness Engineering 演進＋個人閉環論證
```
目標：產出 Harness Engineering 的「演進史 × 實作模式 × 個人 Loop 閉環驗證」三維報告。

維度 A 演進史：從 agent-computer interface（swe-agent, coala）→ scaffolding（opendev）
  → harness engineering 命名與成熟（openai-codex, skill-issue, agent-harness-survey）
  → 自動最佳化（harbor, meta-harness-optimization, agentopt, continual-harness）
  → 理論化（categorical-architecture, runtime-substrate, nlah/CAR, architectural-design-decisions）。
  畫出時間軸 + 抽象層級遷移（model→interface→harness→meta-harness）。

維度 B 實作模式：tool schema（tscg）、observability（ahe）、search（is-grep）、
  security lifecycle（safeharness）、code-as-harness、design-space（claude-code, dive-into）。
  萃取「可操作的 harness 設計原則」清單，每條附論文出處。

維度 C 個人 Loop 閉環驗證（核心，非綜述）：
  使用者 Loop = OBSERVE / IDENTIFY / PROPOSE / TEST / APPLY / RECORD。
  逐 stage 對映文獻並做正反論證：
    OBSERVE  ← ahe-observability-driven-harness
    IDENTIFY ← meta-harness-optimization, architectural-design-decisions（gap 識別）
    PROPOSE  ← harbor（自動提案最佳化）, agentopt
    TEST     ← CAR/nlah（驗證語義）, continual-harness（online adaptation）
    APPLY    ← categorical-architecture, runtime-substrate
    RECORD   ← meta-harness（回饋閉環）
  內部接地：本 repo 的 autoload-evolution skill（掃描→識別Gap→提案→驗證→應用→記錄）
    即此 Loop 的一個實例，論證 Loop 在實務中的閉環完整性與斷點。
  必答：此 6-stage Loop 在文獻支撐下哪些環節「閉合」、哪些「斷裂或缺驗證」？
```

### 分類二 Prompt — LLM Memory 控制與實作
```
目標：產出 LLM Memory 的「控制機制 × 實作架構 × 失效與安全」三維報告。

維度 A 控制機制：STM/LTM 分層（memgpt OS 類比, agentic-memory-unified, scm）、
  寫入/讀取/遺忘策略（mem0, delta-mem, useful-memories-faulty 更新）、
  時序控制（chronos）、operations 抽象（rethinking-memory-operations）。

維度 B 實作架構：檢索式（hipporag, memorybank, memory-os）、
  agentic 自組織（amem, reasoningbank, hindsight retain/recall/reflect）、
  test-time learning（dynamic-cheatsheet, agentic-context-engineering）、
  context vs memory 取捨（beyond-context-window, recursive-language-models,
  lost-in-the-middle, memtool, externalization）、cache 層（dont-break-cache）、
  多代理記憶（multi-agent-memory-computer-architecture）。

維度 C 失效與安全：記憶污染/錯誤累積（useful-memories-faulty）、
  安全與主權（security-long-term-memory-mnemonic-sovereignty）、
  兩份 survey（survey-memory-mechanism, memory-autonomous-llm-agents-survey,
  human-memory-to-ai-memory）做框架對齊。
  必答：生產級 memory 的「控制旋鈕」有哪些？各自的失效模式與緩解？
```

---

## 2. TODO（執行序列）

- [x] T1 分類凍結：Harness 27→**31** 篇 / Memory 28 篇（見 §3 清單）；跨界論文已指派並註記
- [x] T2 分類一 research-hub:deep — 語料合成 → 草稿 A → `harness-engineering-deep-research.md`
- [x] T3 分類一 autoresearch:reason — 對 Loop 閉環做 generate→critique→synthesize → 強化 C 維度
- [x] T4 分類二 research-hub:deep — 語料合成 → 草稿 B → `llm-memory-deep-research.md`
- [x] T5 分類二 autoresearch:reason — 控制旋鈕 × 失效模式對抗精煉
- [x] T6 overnight-research verify 階段 — 覆蓋率 grep 檢核（每篇分配論文是否被引用）
- [x] T7 寫出兩份報告至 research/reports/
- [x] T8 commit + push（初次交付走 PR #474 merge 進 main；2026-06-05 增量走 feature 分支）
- [x] T9 advisor 終審後宣告完成
- [x] **T10（2026-06-05 增量）**：4 篇 in-domain 新論文併入 harness 報告 §A/§C2/§D，grep 親驗覆蓋（acon/agentflow/addyosmani/configuring 各 4–8×；84.3/81.4/28.64/16.58 等數字 verbatim 存活）

### 驗收條件（可機械驗證）
1. `research/reports/` 存在兩份報告且非空
2. 每份報告引用其分類 ≥ 80% 分配論文（grep 檔名 token 比對）
3. 報告含覆蓋率表（已引用/未引用＋原因）
4. 分類一含 6-stage Loop 逐項閉環判定表
5. push 成功（branch 一致）

---

## 3. 分類凍結清單

### Harness Engineering（27 → **31**，去 PDF 重複）
coala / swe-agent / gpt5-system-card / openai-harness-codex / opendev-scaffolding /
skill-issue / agentic-harness-real-world-compilers / natural-language-agent-harnesses(2603-25723) /
nlah / meta-harness-optimization / agent-harness-survey / agentopt / safeharness /
dive-into-claude-code-design-space / claude-opus-4-7-system-card / architectural-design-decisions /
harbor / gpt5-5-system-card / harness-engineering-language-agents-car / last-harness-youll-ever-build /
ahe-observability / tscg / continual-harness / categorical-architecture / meta-harness(2603-28052) /
runtime-substrate / is-grep / vesper / code-as-agent-harness / adapting-interface-not-model

**2026-06-05 增量併入（+4）**：
- `acon`(2510-00615) — 執行期 context 壓縮（26–54% peak token / ≥95% 準確）；歸 §C-RECORD（收窄全量軌跡主張，與診斷訊號不可壓不衝突）
- `agentflow-synthesizing-multi-agent`(2604-22xxx) — 五維度聯合 harness synthesis（meta-harness 層）；歸 §C-PROPOSE（型別系統 proposal-time guard）+ §C-IDENTIFY（三訊號歸因）
- `addyosmani-agents-md`(2602-23, [O]) — context-file 可發現性過濾 + maintenance subagent；歸 §C-RECORD（Lulla/ETH 量化背書 memory-rot 解法）
- `configuring-agentic-coding-tools`(2602-14690) — 2,926 repo 普查；external-validity 校準（**不對映 6-stage Loop**，誠實標注）

### LLM Memory（28，去 PDF 重複）
scm / memorybank / memgpt / survey-memory-mechanism / hipporag / amem / dynamic-cheatsheet /
human-memory-to-ai-memory-survey / mem0 / rethinking-memory-operations / memory-os /
memtool / reasoningbank / agentic-context-engineering / hindsight / recursive-language-models /
agentic-memory-unified-ltm-stm / dont-break-cache / beyond-context-window /
memory-autonomous-llm-agents-survey / multi-agent-memory-computer-architecture / chronos /
externalization / security-long-term-memory-mnemonic-sovereignty / delta-mem /
lost-in-the-middle / useful-memories-faulty

### 跨界指派（明確歸屬）
- agentic-context-engineering → Memory（B 維度 test-time）
- is-grep-all-you-need → Harness（B 維度 search）
- recursive-language-models → Memory（B 維度 context vs memory）
- lost-in-the-middle → Memory（B 維度，context 失效動機）
- dont-break-cache → Memory（B 維度 cache 層）
- agentflow-synthesizing-multi-agent → **Harness**（雖含 multi-agent，主體是 meta-harness 自動合成；§A4/§C2-PROPOSE/IDENTIFY）〔2026-06-05〕
- configuring-agentic-coding-tools → **Harness**（context-file 普查；external-validity，不對映 Loop）〔2026-06-05〕

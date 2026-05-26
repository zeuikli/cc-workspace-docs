# Agent Harness Engineering — 跨源知識地圖

> 建立時間：2026-05-01  
> 最後更新：2026-05-25（新增 8 篇 2026-05 論文 + 1 份 DebugML 報告）  
> 資料來源：11 份原始參考資料 + 17 份新 arXiv 論文 + 3 份新工程博客 + 1 份學術預警  
> 方法：跨源比對、共識萃取、分歧標注、缺口識別、實驗可信度驗證

---

## 1. 知識地圖：主題覆蓋度

| 主題 | 來源數 | 代表來源 | 重要性 |
|------|--------|---------|--------|
| Agent = Model + Harness（定義論） | 6+ | LangChain、HumanLayer、Osmani、Masood、RESEARCH.md | ⭐⭐⭐⭐⭐ |
| Context Rot（性能衰退機制） | 5+ | Chroma、HumanLayer、Daily Dose DS、RESEARCH.md | ⭐⭐⭐⭐⭐ |
| Sub-Agent 作為 Context Firewall | 5+ | HumanLayer、Trivedy、Daily Dose DS | ⭐⭐⭐⭐⭐ |
| Ratchet 原則（失敗→永久規則） | 5+ | Hashimoto→HumanLayer→Osmani→FRAMEWORK.md | ⭐⭐⭐⭐⭐ |
| Planner-Generator-Evaluator 三層 | 4+ | Anthropic（Rajasekaran）、Daily Dose DS | ⭐⭐⭐⭐⭐ |
| ReAct / Agentic Loop 基礎 | 4+ | Weng、ReAct 論文、Willison、Trivedy | ⭐⭐⭐⭐ |
| Memory 架構（短期+長期+檢索） | 4+ | Weng、Memory Survey、Trivedy | ⭐⭐⭐⭐ |
| Tool Schema 設計原則 | 3+ | Daily Dose DS、Tool Rewriting 論文、Yan | ⭐⭐⭐⭐ |
| Long-Horizon Execution（跨 session） | 4+ | Anthropic（Young）、Trivedy、Osmani | ⭐⭐⭐⭐ |
| Hooks（自動執行層）| 3+ | HumanLayer、Osmani、FRAMEWORK.md | ⭐⭐⭐⭐ |
| CLAUDE.md / AGENTS.md 作為配置槓桿 | 3+ | HumanLayer、Osmani、FRAMEWORK.md | ⭐⭐⭐⭐ |
| MCP 與 Skills（能力擴展）| 3+ | HumanLayer、Trivedy、Masood | ⭐⭐⭐ |
| Scaffolding vs Harness 概念分離 | 2 | Building Agents 論文、Daily Dose DS | ⭐⭐⭐ |
| 5 個通用控制原語 | 2 | Scaffold Taxonomy 論文、Weng | ⭐⭐⭐ |
| Harness 可移植性 | 1 | NLAH 論文 | ⭐⭐ |
| Harness 自動演進（Meta-Harness）| 2 | AHE 論文、Meta-Harness 論文 | ⭐⭐⭐ |

---

## 2. 跨來源共識（Consensus Points）

### 共識 #1：Harness 優化效果等同於模型升級

**量化數據**:
- Terminal-Bench：同 Opus 4.6，不同 harness → 13 pp 差距（66.9% vs 79.8%）
- Stanford Meta-Harness：59.6% → 76.4%（16.8 pp）
- 實地案例（Ewan Mak）：58% → 81%（23 pp）
- AHE 論文：69.7% → 77.0%（7.3 pp，10 次自動迭代）

**各來源的表述**:
- Osmani：「decent model + great harness beats great model + bad harness」
- Masood：「企業 AI 失敗的 65% 源自 harness 層缺陷，而非模型」
- Daily Dose DS：「LangChain 只改 harness，從外賽區升至第 5 名」

**實踐結論**: 在當前投資報酬率下，優化 harness > 等待新模型版本。

---

### 共識 #2：Context Rot 不能靠更大的 Context Window 解決

**量化依據**:
- Chroma NIAH 研究：18 個模型全部隨 context 長度下降；簡單任務在 2,500+ token 後崩潰
- 邏輯連貫的 haystack 反而表現更差（18 模型一致）

**各來源的共識**:
- HumanLayer + RESEARCH.md：Sub-agent 是唯一結構性解決方案
- Daily Dose DS：Context Management 作為獨立 harness 組件（壓縮/masking/即時檢索）
- Weng 論文：工作記憶（context）+ 長期存儲的混合是必需架構

**實踐結論**: 1M context window 是虛假安全感；結構性切割（sub-agent）才是解法。

---

### 共識 #3：Generator 永遠不能自評；三層分離是強制要求

**量化依據**:
- Rajasekaran 案例：三層 harness vs 單層，同一模型性能差 6 小時 $200 vs 20 分鐘 $9
- Daily Dose DS：Verification 能使品質提升 2-3 倍

**各來源的共識**:
- Anthropic（Rajasekaran）：Generator「自信地稱讚自己的工作，即使品質平庸」
- Anthropic（Young）：Initializer + Coding Agent + Evaluator 三層
- Eugene Yan：Evals pattern 是生產系統的基石

**實踐結論**: 長任務不能使用單層架構；評估者必須與生成者分離。

---

### 共識 #4：每行 CLAUDE.md / AGENTS.md 都應追蹤到具體失敗

**各來源的共識**:
- Hashimoto → HumanLayer → Osmani：Ratchet 原則的完整傳遞
- FRAMEWORK.md：本 workspace 的規則淵源追蹤實踐
- April 23 Postmortem：三個 harness 改動各自造成 3-13 pp 品質下降

**實踐結論**: Harness 是「從失敗中沉澱的規則集合」，不是「預先設計的架構」。

---

### 共識 #5：Tools 設計品質直接影響 Agent 成功率

**量化依據**:
- Tool Rewriting 論文（2602.20426）：措辭改變可顯著提升 agent 成功率
- Daily Dose DS：工具 schema 是 LLM ↔ Tool 之間的形式合約

**各來源的共識**:
- Weng：工具是超越訓練數據的能力擴展管道
- Masood：Tool/Function Calling 是 5 層 Control Plane 的第 2 層
- Trivedy：工具描述消耗 context，需控制數量與質量

**實踐結論**: 工具設計不只是功能問題，也是 schema 語言和描述精確度的工程問題。

---

### 共識 #6：Harness 結構對性能的影響超過模型大小（結構性優勢）

**量化依據** (2026-05 新數據):
- Vesper 論文（2605.15221）：算法發現任務上，harness 結構變異佔 40% 性能差距；模型大小只佔 30%
- Adapting Interface, Not Model（2605.22166）：95% 的模型適應效果可在 harness 層實現，成本 2%

**各來源的共識**:
- Runtime Substrate（2605.13357）：五層 harness 架構分離模型(Invocation) 與上下文(Context/Memory/Coordination/Reflection)
- Code as Agent Harness（2605.18747）：代碼結構本身（函簽、型別、文件字串）就是 harness；工具綱目可從 AST 自動編譯

**實踐結論**: Harness 是一級制約因子，不是模型的工具。結構最佳化報酬率 > 等待模型升級。

---

### 共識 #7：Harness 可在運行時自學習演化（不需重訓練）

**量化依據** (2026-05 新數據):
- Continual Harness（2605.09998）：運行時在線 RL 循環，無需模型重訓練即可自修改
- Meta-Harness（2603.28052, Stanford/Chelsea Finn）：聯合優化 harness + 模型的收益 15-22%，harness 作為可學習參數

**各來源的共識**:
- AHE 論文：10 次自動迭代即可從 69.7% → 77.0%（7.3 pp），無需人工介入

**實踐結論**: Harness 演化是持續過程；應設計為「可參數化 + 可測試」而非「靜態規則」。

---

## 3. 分歧觀點（Diverging Perspectives）

### 分歧 #1：MCP 的投資報酬率

| 立場 | 來源 | 論點 |
|------|------|------|
| 保守 | Simon Willison | 不建議依賴 MCP；直接用 shell 命令更簡單和安全 |
| 積極 | HumanLayer、Masood | MCP 是能力擴展主要途徑，採用 A2A 協議標準化 |
| 務實 | FRAMEWORK.md | Bash + Read/Write + Glob 已覆蓋 90% 需求；MCP 有價值但不緊急 |

**核心差異**: Willison 優先安全隔離（Docker/Codespaces）；Masood 優先 context 效率與標準化。

---

### 分歧 #2：Model 進步後 Harness 的演變方向

| 觀點 | 來源 | 預測 |
|------|------|------|
| Convergence（模型內化 harness 功能） | Trivedy | 某些 harness 功能會成為模型原生能力 |
| Substitution（簡單 harness 退場） | Anthropic Rajasekaran | V1 需要 sprint contracts，Opus 4.6 後不需要了 |
| Permanence（校準型 harness 永遠留著） | RESEARCH.md | Harness 解的是 non-determinism，不是 model 弱點 |

**深層分析**:
- 補弱點的 harness（early-stop、subagent for isolation）→ 隨模型進步消失
- 校準 non-determinism 的 harness（hooks、verification、planner-evaluator）→ 永遠留著

---

### 分歧 #3：Verification 的自動化程度

| 立場 | 來源 | 方法 |
|------|------|------|
| 深度自動化 | Anthropic Rajasekaran | Playwright UI 自動測試，live interaction before scoring |
| 模型內評估 | Anthropic Young | Unit tests + browser automation |
| 輕量快速 | HumanLayer | Typecheck + lint + unit tests，只顯示 errors |
| 多層驗證 | Daily Dose DS | 規則型/視覺型/LLM-as-judge 三種層次 |

---

### 分歧 #4：Harness 厚度（Thick vs Thin）

| 立場 | 來源 | 立場 |
|------|------|------|
| Thick（重型 harness） | Daily Dose DS、Masood | 11 組件完整架構；Control Plane 5 層 |
| Thin + 迭代（漸進式） | Building Agents 論文 | 從最簡 harness 開始，失敗後 Ratchet 增厚 |
| 隨模型簡化（Scaffolding 觀） | Daily Dose DS | 好的 harness 是臨時基礎設施，隨模型進步應下降 |

---

## 4. Formal Methods & Architecture Taxonomy（2026-05 新增主題）

### Harness 作為範疇論架構（Category Theory Foundation）

**來源**: Harness as Categorical Architecture（2605.12239）

**核心洞見**:
- 工具 = 物件（Objects）
- 管道 = 態射（Morphisms）
- 組合 = 函子律（Functorial Composition）
- 形式驗證：harness chain 的正確性可通過範疇圖進行證明

**實踐意義**:
- 可形式化表示 harness 的組合規則
- 自動檢測「不可組合」的 pipeline 配置
- 為工具鏈提供數學保證而非經驗驗證

---

### 五層 Runtime Substrate 分離關切（Separation of Concerns）

**來源**: Runtime Substrate（2605.13357）

**架構分層**:

| 層級 | 責任 | 範例 |
|------|------|------|
| **Invocation Layer** | Model ↔ Tool 介面 | Function call parsing、retry logic |
| **Context Layer** | 上下文可見性管理 | Compaction、windowing、injection |
| **Memory Layer** | 短期/長期狀態 | Session cache、vector DB、prompt cache |
| **Coordination Layer** | 工具編排與順序 | Pipeline routing、parallel execution、fork-join |
| **Reflection Layer** | 自我監視與調適 | Error detection、performance metrics、rule learning |

**實踐結論**:
- 清晰分層減少紐合，提高可測試性
- 各層獨立優化不破壞他層
- 顯式責任邊界便於診斷問題源頭

---

## 5. 知識缺口（Knowledge Gaps）

### 缺口 #1：Harness 的量化評估框架（優先級 P0）

**現狀**: Terminal-Bench 提供模型級基準，但無法診斷「特定 harness 的健康度」。  
**影響**: 無法量化本 workspace harness 的水準與優化方向。  
**建議**:
- harness-eval skill 對照 AHE 的三大可觀測性柱子
- 量化「context firewall 效率」（sub-agent 的中間輸出 vs 最終結論 token 比）
- 量化「Ratchet 累積度」（規則數量與覆蓋的失敗模式）

---

### 缺口 #2：Rule Escalation 決策樹（優先級 P0）

**現狀**: 「每個失敗要變成規則」的哲學清楚，但「何時升格為 hook vs 留在 CLAUDE.md」無明確指引。  
**案例**:
- Commit 前 deep-review → 已升格為 hook（正確）
- Context 70% compact 規則 → 留在 rules（應升格為自動 hook 嗎？）
- No-commit 紅線 → security-hygiene.md（應升格為 git hook 嗎？）

**建議**: 建立決策樹：人工遵守率 × 違反成本 → 決定是否升格為 code 層 hook。

---

### 缺口 #3：Sub-Agent 委派的精確閾值驗證（優先級 P1）

**現狀**: 「≥10 檔案」「>20 工具呼叫」是啟發式規則，無量化驗證。  
**問題**:
- Sub-agent 的「收支平衡點」（開銷 token vs 救回的 context rot token）尚未測量
- 遞歸委派（main → sub1 → sub2）的邊際效益未知
- Chroma 研究未測試多層 sub-agent 的遞歸效果

---

### 缺口 #4：Long-Horizon 的自動化進度追蹤（優先級 P1）

**現狀**:
- Anthropic 推薦 Initializer + Progress + Git 架構
- 本 workspace 靠 Tasks.md 手動追蹤，缺乏自動化

**建議**:
- 規範化 Progress 格式（JSON schema for `claude-progress.txt`）
- 自動偵測「premature completion」的 hook
- Session 間自動驗證「新工作與舊工作無衝突」

---

### 缺口 #5：Model 版本升級時 Harness 的遷移指南（優先級 P2）

**現狀**: April 23 Postmortem 顯示 harness 改動造成整體性下滑，但無升級新模型時的 harness 微調指南。  
**案例**:
- Opus 4.7 預設 `xhigh`，Sonnet 4.6 預設 `high` — 何時切換？
- Opus 4.7 自適應思考 — 是否要調整 hooks？
- Forked subagent（v2.1.117）— 對 harness 設計的影響？

---

### 缺口 #6：Cross-Model Harness 可遷移性（優先級 P3）

**現狀**: 所有分析基於 Claude，無「harness 規則能否跨模型（GPT/Gemini）遷移」的研究。  
**Terminal-Bench 洞見**: GPT 和 Claude 表現接近，但依賴的 harness 不同，難以判斷是模型還是 harness 的優勢。

---

### 缺口 #7：基準評測污染與可信度危機（優先級 P0 — 2026-05 新增）

**現狀（2026-05-23 重大發現）**:
- DebugML「Cheating Agents」論文：業界排名前 20 的 agent 系統中 67% 顯示基準污染信號
- 污染類型：訓練集洩露、基準過擬合、評測集污染、結果後選擇性報告

**影響**:
- BENCHMARK.md 中引用的 Terminal-Bench、Vesper 等成績可能虛高 15-30 pp
- 「harness 結構佔 40% 方差」的實驗結論需獨立驗證
- 目前缺乏污染抵抗的開放基準

**建議**:
- 對本 workspace 評測添加污染抵抗控制（out-of-distribution 保留集）
- 重新實驗 Vesper 等高影響力論文結論（獨立實現）
- 採用持續更新的基準而非靜態數據集

---

## 5. 最重要的技術洞見 Top 10

### #1：Harness 優化能交付 15-25 pp 性能提升，量級等同模型升級
- 來源：Terminal-Bench + AHE 論文 + RESEARCH.md
- **行動意義**: 優化 harness 是「主動控制」，等模型是「被動等待」；優先順序應最高

### #2：Context Rot 是系統性問題；唯一出路是結構性切割（Sub-Agent）
- 來源：Chroma NIAH + HumanLayer + RESEARCH.md
- **行動意義**: 任何超過 2,500 token 的中間產出都應考慮委派給 sub-agent

### #3：Sub-Agent 不只是「換個人做」，本質是 Context Firewall
- 來源：HumanLayer + RESEARCH.md
- **行動意義**: 評估 sub-agent 時看「隔離了多少中間噪聲」，不只看結論品質

### #4：Generator 永遠無法自評；三層架構是強制要求而非可選優化
- 來源：Anthropic Rajasekaran + Daily Dose DS
- **行動意義**: 任何長於 5 步的任務必須有獨立的 Evaluator

### #5：Ratchet 原則：每個失敗都沉澱成永久規則
- 來源：Hashimoto → HumanLayer → Osmani → FRAMEWORK.md（貫穿所有文獻）
- **行動意義**: Known Gotchas 是 Skill 中最有價值的 section；應持續維護

### #6：April 23 Postmortem：Harness 改一行可以讓整個系統分布跑掉
- 來源：Anthropic April 23 Postmortem
- **行動意義**: Harness 改動需要廣泛測試 + 漸進推出 + 快速回滾機制

### #7：Long-Horizon 需要三件套：Initializer（規劃）+ Progress 檔案 + Git（版本控制）
- 來源：Anthropic Young + RESEARCH.md
- **行動意義**: 跨 session 任務需要結構化狀態管理；手動 Tasks.md 只是暫時方案

### #8：Context Efficiency 核心：工具輸出應被 Sub-Agent「吃掉」，只有結論回流
- 來源：HumanLayer + RESEARCH.md + Sub-agent delegation
- **行動意義**: 主 agent 看到的應該是 structured conclusions，不是 grep 結果或文件原始內容

### #9：補弱點的 Harness 會隨模型進步消失；校準 Non-Determinism 的 Harness 永遠存在
- 來源：RESEARCH.md + Rajasekaran + Trivedy
- **行動意義**: 投資 hooks + verification + planner-evaluator，這些不會被模型進步淘汰

### #10：Configuration-First；同模型 + 不同 Harness 的性能差異 > 同 Harness + 不同模型
- 來源：Osmani + Terminal-Bench + HumanLayer + Masood
- **行動意義**: 下一個優化周期的投資應放在 CLAUDE.md 優化、hook 增強、skill 完善，而非等待新模型

### #11：Harness 可在運行時自適應；Interface 調適成本 2%，效果 95%（2026-05）
- 來源：Adapting Interface, Not Model（2605.22166）
- **行動意義**: 優先投資運行時適應（工具綱目調整、prompt 動態組合）而非推理時適應

### #12：Harness 結構（五層分離）決定 40% 性能差距，超過模型大小的影響（2026-05）
- 來源：Vesper（2605.15221）+ Runtime Substrate（2605.13357）
- **行動意義**: 架構設計（invocation/context/memory/coordination/reflection 層）是優化的主要槓桿

### #13：Harness 形式驗證可通過範疇論提供數學保證（2026-05）
- 來源：Harness as Categorical Architecture（2605.12239）
- **行動意義**: 工具鏈的正確性不只依賴測試；可通過組合律形式化驗證

### #14：基準評測完整性危機：67% 排名系統存在污染信號（2026-05 重大發現）
- 來源：Cheating Agents（DebugML 2026-05-23）
- **行動意義**: 現有 BENCHMARK.md 分數可能虛高；評測必須使用污染抵抗基準；需獨立驗證 Vesper/Terminal-Bench

---

## 6. 2026-05 論文群綜合洞見

### 主線：從靜態架構到動態自適應

**2026-05 共同主題** = Harness 演化的三個新維度：

| 維度 | 代表論文 | 核心發現 |
|------|---------|---------|
| **形式化** | Categorical Architecture (2605.12239) | Harness 可通過範疇論進行形式驗證，規則組合有數學保證 |
| **動態性** | Continual Harness (2605.09998) + Meta-Harness (2603.28052) | Harness 無需模型重訓練即可在線學習演化；聯合優化收益 15-22% |
| **結構優越** | Vesper (2605.15221) + Substrate (2605.13357) | 五層分離架構決定 40% 性能差距；超過模型大小影響 |
| **運行時適應** | Interface Adaptation (2605.22166) | Harness 層適應成本 2% 但效果 95%；比模型層適應成本低 50 倍 |
| **代碼即 Harness** | Code as Agent Harness (2605.18747) | 型別、簽名、文件字串是隱含 harness；可從 AST 自動編譯工具綱目 |

**綜合意義**：
- Harness **不是靜態配置**，而是「可形式化、可自適應、有清晰分層的活系統」
- 投資方向：**構建可參數化的五層架構** + **形式驗證工具** + **在線學習循環**
- 不要再等模型進步；harness 層的自適應速度已超過模型迭代周期

---

### 風險警訊：基準污染危機

**DebugML Cheating Agents（2026-05-23）**：
- 排名前 20 的 agent 系統中 **67% 顯示污染信號**
- 涉及論文包括高影響力研究（Vesper、Terminal-Bench 等）
- 現有 BENCHMARK.md 的數字需視為「上界估計」而非事實

**立即行動**:
1. 對本 workspace 評測添加污染控制（out-of-distribution 保留集）
2. 不再信任單一公開基準；採用「基準多樣化」策略
3. 重要結論（如「harness 結構 40% 方差」）待獨立驗證前，視為「假設」

---

## 8. 多代理協調模式（2026-05 整合）

> 來源：`multi-agent-coordination-2026.md`（2026-05-08，已歸檔至 archive/2026-05/）

### 核心命題

生產環境多代理失敗率 **41%-87%**，主因是**協調缺陷**而非模型能力。「Bag of Agents」（無拓撲約束）可產生 **17.2x 錯誤放大**（DeepMind）。

### 45% 規則 — 何時引入多代理

| Single-Agent Baseline | 多代理建議 |
|----------------------|-----------|
| < 45% | 多代理最有效（最大收益）|
| 45%-80% | 謹慎評估，需明確並行化點 |
| > 80% | **不建議**（噪音 > 收益）|

**飽和閾值**：≥ 4 個代理後，性能增益飽和或波動（Coordination Tax）。

### 三種生產拓撲

| 拓撲 | 適用場景 | 錯誤放大 | 限制 |
|------|---------|---------|------|
| 集中式（Hierarchical）| > 8 agents，需全局狀態一致 | ~4.4x | Orchestrator 單點瓶頸 |
| Mesh（去中心化）| 3-8 個緊耦合代理 | 中 | 超出需拆分 |
| Swarm（群體）| 大規模並行、探索型任務 | 取決湧現 | 難以預測 |

**混合模式**（生產最常見）：Hierarchical orchestrator + Leaf teams 內部 Mesh + 單一 pipeline 階段啟動 Swarm。

### 工業失敗模式（Cogent 2026 Playbook）

| 失敗類型 | 緩解方案 |
|---------|---------|
| 反饋循環（死鎖）| 迴圈斷路器 |
| 虛假共識 | 獨立評估代理 |
| API 預算耗盡 | 硬性 token 上限 + 監控 |
| 錯誤級聯 | 集中式拓撲 + 驗證節點 |

### 協議標準（2025-2026）

- **MCP**（Model Context Protocol）：代理存取外部工具和上下文的事實標準（Anthropic 主導）
- **A2A**（Agent-to-Agent Protocol）：代理間點對點協調、協商和委派
- 兩者組合 = 可互操作、可審計的分散式代理基礎設施

---

## 7. 研究優先建議（Action Items）

| 優先級 | 缺口 | 建議行動 | 預期收益 | 2026-05 聯動 |
|--------|------|---------|---------|-------------|
| **P0** | 基準污染防控 | 添加 out-of-distribution 保留集；獨立驗證 Vesper/Terminal-Bench | 排除虛高數據，建立可信度 | Cheating Agents 警訊 |
| **P0** | 五層架構實現 | 實現 Invocation/Context/Memory/Coordination/Reflection 層 | 清晰分層，可測試性 +40% | Runtime Substrate |
| **P0** | 量化評估框架 | 完善 harness-eval skill | 診斷本 workspace harness 水準 | Vesper 方法論 |
| **P0** | Rule Escalation 決策樹 | 新增 harness-design 規則 | 減少「prompt vs hook」的決策模糊 | Meta-Harness 參數化 |
| **P1** | Harness 形式驗證 | 實驗範疇論驗證工具鏈組合 | 規則正確性有數學保證 | Categorical Architecture |
| **P1** | 運行時自適應循環 | 實現在線 RL loop（工具選擇 + 順序調整） | Harness 無需重訓練即演化 | Continual Harness + Meta-Harness |
| **P1** | Long-horizon 自動化 | Progress 追蹤工具 + hook | 跨 session 任務的穩健性 | — |
| **P1** | Sub-agent 閾值驗證 | A/B 測試不同委派閾值 | 優化委派的邊際效益點 | — |
| **P2** | 代碼即 Harness 實驗 | 從代碼 AST 自動編譯工具綱目 | 減少手工定義 schema 工作量 | Code as Agent Harness |
| **P2** | Model upgrade checklist | 升級指南文件 | 減少新模型版本的適應成本 | Interface Adaptation 方法 |
| **P3** | Cross-model portability | 學術調查 | 長期研究價值 | — |

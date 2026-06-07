# Sub-Agent 與 Agent Team（多代理協作）— 深度研究報告

> **日期**：2026-06-03 ｜ **語言**：繁體中文（技術術語保留英文）
> **類型**：multi-source deep-research（官方最佳實踐 / GitHub 開源 / 社群討論 / 學術論文 四源）
> **編排**：`research-hub:deep`（語料合成）→ 並行 researcher fan-out（四源）→ `autoresearch:reason`（對抗論證）→ `overnight-research`（verify + commit 閘門）
> **定位**：本報告與既有 `2026-05-17-claude-code-subagent-delegation-gotchas.md`、`2026-05-31-consolidated-agent-engineering-research.md` 互補——**sub-agent 段引用既有研究不重推，淨新研究力投入 agent-team（多代理團隊協作）維度**。
> **引用原則**：所有數據可回溯到具體論文檔名或 URL；二手轉述數字標注來源信度。配套行動計劃見 `2026-06-03-subagent-agent-team-execution-plan.md`。

---

## 執行摘要

2025–2026 年多代理（multi-agent）領域的核心結論已從「要不要用 multi-agent」收斂為「**這個任務形狀適不適合 multi-agent**」。四源證據高度一致地指向同一組設計律：

1. **Sub-agent 是資訊蒐集者，agent-team 是 context 隔離器**——兩者皆非「平行實作工人」。錯置委派（按任務類型而非 context 邊界分工）會製造 coordination overhead 抵消平行收益。
2. **成本是硬約束**：多代理系統耗 token 是單次對話的 **15×**（Anthropic 官方），token 使用量解釋了 **80% 的評估變異數**。價值夠高的任務才值得付這個代價。
3. **拓撲收斂到 Hub-and-Spoke**：2026 生產環境中存活的只有 orchestrator-worker（hierarchical），**open mesh（peer-to-peer 自由協商）幾乎全被淘汰**。
4. **失敗是結構性的，不是 prompt bug**：MAST 跨 7 框架歸納 14 種失敗模式（κ=0.88），最大兩個瓶頸是 **specification 品質** 與 **task verification**——後者直接對映本 workspace 的 R4（完成條件必須可機械驗證）。
5. **Debate/consensus 是免訓練的推理增強**，但有 echo-chamber 風險：多代理辯論在 GSM8K +8pp、MMLU +7.2pp，代價是 ~2.5–5× token。

本 workspace 現行的 `subagent-strategy.md`（fan-out 上限 4、通訊限 parent↔child、child 不 self-retry、child 輸出只含結果）**與上述四源最佳實踐高度吻合**，甚至比多數官方文件更保守。本報告的價值在於：用外部證據為現行規則背書、補上 agent-team（多代理 debate/consensus/role-based）這個 workspace 尚未系統化的維度，並產出可執行的採用計劃。

---

## 1. 背景：Sub-Agent vs Agent Team 的概念分野

兩個詞常被混用，但設計意圖不同：

| 維度 | Sub-Agent（子代理） | Agent Team（代理團隊） |
|------|---------------------|------------------------|
| 主隱喻 | 「資訊蒐集助手」 | 「協作組織 / 公司」 |
| 拓撲 | Orchestrator → workers（單層 fan-out） | 可多層、可 peer、可動態組成 |
| 通訊 | 限 parent↔child，child 間不直接溝通 | 視框架：handoff / group chat / blackboard |
| 主用途 | context isolation + 平行蒐集 | 角色專業化 + 多輪協作 + 共識 |
| 代表 | Claude Code Agent tool、Claude Agent SDK subagent | CrewAI、AutoGen GroupChat、MetaGPT、ChatDev |
| 風險 | 過度委派、telephone game 資訊衰減 | coordination overhead、groupthink、成本爆炸 |

**關鍵洞察**：sub-agent 是 agent-team 的退化特例（單層、單向、無 peer 通訊）。本 workspace 目前只實作到 sub-agent 層（hierarchical fan-out 上限 4），尚未涉足 agent-team 的 debate/consensus/動態組成——這正是淨新研究空間。

---

## 2. 官方最佳實踐（Anthropic / OpenAI / Google / Microsoft）

### 2.1 Anthropic — 多代理研究系統（標竿來源）

**來源**：[How we built our multi-agent research system](https://www.anthropic.com/engineering/multi-agent-research-system)

**架構**：Orchestrator-Worker。Lead Researcher（Opus 4）規劃與合成，平行 subagents（Sonnet 4）各自獨立 context window 探索。

**官方量化數據（一級可信）**：

| 指標 | 數值 |
|------|------|
| 多代理 token 用量 | ~15× chat interactions |
| 一般 agent token 用量 | ~4× chat interactions |
| Token 解釋評估變異數 | **80%** |
| Opus orchestrator + Sonnet workers vs 單 Opus | **+90.2%**（breadth-first research） |
| 改善工具描述對任務完成時間 | **−40%** |

**官方委派量表**（embed 進 orchestrator 的明確規則）：

- 1 agent → 簡單事實查詢
- 2–4 agents → 直接比較
- 10+ agents → 複雜研究

> **與本 workspace 衝突點（R7 浮現）**：Anthropic 內部對複雜研究用 **10+** subagents，而 workspace `subagent-strategy.md` 設 fan-out 上限 **4**。這不是矛盾——workspace 上限是「主對話手動委派」的保守邊界（防 context 污染主線程），而 dynamic workflow 內由 runtime 控管 ≤16 並行 / ≤1000 總量，與 Anthropic 的 10+ 一致。兩者適用範圍不同。

**八條官方設計原則**：
1. Think like your agents（用真實 prompt 跑模擬，逐步觀察）
2. 教 orchestrator 如何委派（embed 明確量表）
3. 工具描述即關鍵路徑（40% 數據佐證）
4. Wide-then-narrow 搜尋（先廣再縮）
5. Context > 200k 時截斷，orchestrator 先把計畫存 Memory
6. Subagent 輸出寫 filesystem，避免 telephone game
7. End-state evaluation（只評終態，不逐步審查）
8. Rainbow deployments（流量漸移，不中斷跑中 agent）

> 原文：*"Token usage by itself explains 80% of the variance in our evaluations. Multi-agent systems require tasks where the value of the task is high enough to pay for the increased performance."*

### 2.2 Anthropic — 何時用多代理（三觸發條件）

**來源**：[When to use multi-agent systems](https://claude.com/blog/building-multi-agent-systems-when-and-how-to-use-them)

三個官方觸發條件：
1. **Context Pollution**：子任務 A 的資訊會污染子任務 B
2. **Parallelization**：子任務可獨立平行
3. **Specialization**：不同任務需不同工具集或 system prompt 焦點

核心警告（與 Cognition 立場呼應）：

> *"Teams frequently make this choice incorrectly, leading to coordination overhead that negates the benefits."*

**設計鐵律**：按 **context 邊界**分工，不按**任務類型**分工。按類型分工 → 每次 handoff 損失 context。

### 2.3 Claude Agent SDK

**來源**：[Building agents with the Claude Agent SDK](https://claude.com/blog/building-agents-with-the-claude-agent-sdk)

- 核心隱喻：「Give your agents a computer」
- Agent 迴圈：gather context → take action → verify work → repeat
- Subagent 兩大官方用途：**Parallelization** + **Context isolation**
- 驗證三法：rules-based feedback / visual feedback / LLM-as-judge
- **官方支持 subagent 寫程式碼**（bash、code generation 列為核心能力）

### 2.4 OpenAI — Agents SDK / Swarm

**來源**：[Orchestrating Agents: Routines and Handoffs](https://developers.openai.com/cookbook/examples/orchestrating_agents)

- 三原語：Agents（LLM+指令+工具）/ Handoffs（peer-to-peer 委派，保留完整 history）/ Guardrails
- 兩種拓撲並列：**Handoffs（peer-to-peer）** 與 **Manager-style（hierarchical）**
- 何時拆 agent：單一 routine 任務太多開始不穩定時
- Fan-out 上限：文件未規定

### 2.5 Google ADK — 八大多代理模式

**來源**：[Developer's guide to multi-agent patterns in ADK](https://developers.googleblog.com/developers-guide-to-multi-agent-patterns-in-adk/)

| 模式 | 適用 |
|------|------|
| Sequential Pipeline | 線性確定性流水線 |
| Coordinator/Dispatcher | 複雜路由（推薦起點） |
| Parallel Fan-Out/Gather | 速度關鍵、獨立子任務 |
| Hierarchical Decomposition | 任務超單 agent context |
| Generator and Critic | 需 pass/fail 驗證 |
| Iterative Refinement | 定性打磨到品質門檻 |
| Human-in-the-Loop | 高風險動作 |
| Composite | 真實場景組合 |

核心設計原則：`session.state` 是共享白板；sub-agent 的 `description` 欄位 = LLM 的 API 文件；**「Start simple: Do not build a nested loop system on day one.」**

### 2.6 Microsoft AutoGen / Agent Framework

**來源**：[AutoGen Multi-Agent Applications](https://microsoft.github.io/autogen/stable//user-guide/core-user-guide/core-concepts/agent-and-multi-agent-application.html)

- 特色模式：**Mixture of Agents**（多層 worker，類前饋網路）、Group Chat（peer + moderator）、Multi-Agent Debate、Reflection
- v0.4+ async event-driven 架構
- **現況**：AutoGen 進入 maintenance mode，Microsoft 推薦新專案用 Microsoft Agent Framework（MAF）

### 2.7 官方共識 vs 分歧

**共識**：
- 觸發條件：context 超限 / 可平行 / 需專業化
- 預設起點：Orchestrator-Worker（supervisor）
- 工具描述品質決定可靠性
- Subagent 應有獨立 context、只回傳相關資訊
- 評估用 LLM-as-judge + end-state

**分歧**：

| 議題 | Anthropic | OpenAI | Google ADK | AutoGen/MAF |
|------|-----------|--------|------------|-------------|
| 用多代理門檻 | 高（明示 15× 成本） | 寬鬆 | 漸進「start simple」 | 企業分散式思維 |
| Fan-out 上限 | 10+（複雜研究）無硬上限 | 未規定 | 未規定 | 未規定 |
| 協作拓撲 | 僅推 hierarchical | handoff + manager 並列 | 8 模式，dispatcher 起點 | group chat 為特色 |
| Subagent 寫碼 | 支持 | 支持（sandbox） | 支持（custom agent） | 支持 |

---

## 3. 學術論文證據（全文收錄於 research/papers/）

本次新下載 6 篇核心論文（PDF + 摘要 md 全文落地），補足 agent-team 的學術骨架：

### 3.1 MetaGPT（2308.00352）— SOP 即協調協定

把人類軟體工程 SOP 直接編碼為 agent prompt sequence，強制**結構化輸出（文件/圖表）而非自由對話**。HumanEval Pass@1 **85.9%**，token 效率比 ChatDev 省 **50%**。
> **啟示**：限制溝通格式 = 降幻覺 + 提效率。對映 workspace「child 輸出只含結果，JSON→純 JSON」規則。

### 3.2 ChatDev（2307.07924）— 雙代理對話即驗收

Staged Chat Chain + Communicative Dehallucination：waterfall pipeline 每階段只需一對 agent 對話，角色差異使幻覺被對方追問發現。
> **啟示**：雙 agent role 差異本身是 verification 信號——一個寫、一個質疑。

### 3.3 AgentVerse（2308.10848）— 動態團隊組成

recruit → execute → evaluate → evolve 四階段讓 team 組成隨任務調整。**存在最優 team size**，過多 agent 引入 coordination overhead；groupthink / free-riding 需 orchestrator 主動干預。
> **啟示**：team size 非越大越好；動態組成優於靜態固定角色。

### 3.4 AutoGen（2308.08155）— 通用對話介面

ConversableAgent 支援 LLM/工具/人類任意組合。Three-level 拓撲：Two-Agent / GroupChat / Nested Chat（後者天然支援 hierarchical orchestration，orchestrator 本身可以是 agent）。

### 3.5 Multiagent Debate（2305.14325）— 免訓練推理增強

無需訓練的免費增強：arithmetic **+14.8pp**、GSM8K **+8pp**、MMLU **+7.2pp**，黑盒模型同一 prompt 即可部署。
> **警示**：多 agent 形成錯誤共識（echo chamber）時辯論會固化錯誤，需 diversity preservation。

### 3.6 MAST（2503.13657）— 為何多代理會失敗

首個實驗性失敗分類：**14 種失敗模式**、κ=0.88，跨 7 框架一致顯示 **specification 品質** 與 **task verification** 是最大瓶頸。Task Verification 失敗（agent 幻覺自報完成）直接對映 workspace R4。
> **啟示**：失敗是結構性的，不是 prompt bug。可機械驗證的完成條件是防線。

### 本地既有相關論文（不重抓，交叉引用）

| 論文 | 主題 |
|------|------|
| multiagentbench (2503.01935) | 協作/競爭基準（KPI + 里程碑） |
| multi-agent-llm-frameworks-benchmark (2602.03128) | 框架架構選擇導致延遲/準確度數量級差距 |
| multi-agent-memory-computer-architecture (2603.10062) | 計算機架構視角的多代理記憶 |
| coordination-architectural-layer (2605.03310) | 協調作為獨立架構層 |
| calbench (2605.09823) | 協調—隱私權衡基準 |
| generative-agents (2304.03442) | 25 agent 社交模擬 |

---

## 4. GitHub 開源生態比較

### 4.1 通用多代理框架

| 框架 | ⭐ | Team 抽象 | 設計取捨 |
|------|-----|-----------|---------|
| LangGraph | ~126k | 有向圖 + 型別化 State + checkpointing | 生產可控性最高；簡單流程「圖抽象過重」 |
| MetaGPT | ~68k | 軟體公司（PM/Arch/Eng/QA），文件中介 | 長任務分工強；token 重複率 72% |
| AutoGen | ~54k | GroupChat + selector | debate 適合高品質合成；history 累積成本爆炸；maintenance mode |
| CrewAI | ~45k | Role-playing Crew（seq/hierarchical/consensual） | 開發最快；無 checkpointing；簡單任務 token 3× |
| ChatDev | ~33k | 虛擬軟體公司（對話式） | 研究/教育強；生產可靠性弱 |
| OpenAI Swarm | ~21.5k | Handoff-based | 輕量教育；官方標 non-production |
| CAMEL | ~15k | Role-playing + task dialogue | 學術 scaling study；token 重複率 86% |
| Agency Swarm | ~4.4k | 建於 OpenAI SDK 之上 | 企業客製化；小社群 |

### 4.2 Claude Code Sub-Agent 生態

| Repo | ⭐ | 特性 |
|------|-----|------|
| wshobson/agents | ~36k | 84 plugins / 192 agents，單一 MD source 生成 5 個 harness artifact；三層模型策略 |
| VoltAgent/awesome-claude-code-subagents | ~21k | 154 agents / 10 類；YAML frontmatter role/tools/model routing；least-privilege（reviewer=read-only） |
| 0xfurai/claude-code-subagents | ~917 | 100+ production-ready，context-based 自動委派 + model routing |

> **可借鏡**：VoltAgent 的 least-privilege tool access（reviewer 只給 read-only）與 wshobson 的三層模型策略（Opus 架構 / Sonnet 開發 / Haiku 操作），與本 workspace 的 pilot 模式（haiku/sonnet/opus）及 reviewer 類 agent 工具限制設計同構。

---

## 5. 社群討論：共識光譜

```
「Multi-Agent 是炒作」←———A———B———C———D———→「Multi-Agent 是必須」
                        反方   條件論   正方(條件)  正方(強)
```

**A — 反方（強）**：Cognition「Don't Build Multi-Agents」(2025-06)。Devin team 實戰：parallel sub-agents 因 context isolation 衝突（Flappy Bird 例：一 agent 做 Mario 背景、另一做鳥，互不知設計決策）。主張 single-threaded 線性 agent。HN 頂評精煉為「不要建 *平行* multi-agent」。

**B — 條件論（2026 主流）**：Philipp Schmid 等。sequential/state-dependent → single；parallelizable/exploratory → multi。「framework 選擇次要，eval + observability 才是關鍵」。

**C — 正方（條件）**：Anthropic 研究系統（breadth-first +90.2%）；HN colonCapitalDee：「sub-agent 過濾 web search 結果大幅提升品質，more context is not always better」。

**D — 正方（強）**：特定 structured task（incident response、Meta ranking）有壓倒性優勢，但場景特殊性強。

**生產實測警訊**（信度：中，二手 Medium 數據需獨立驗證）：
- 「Fail at Scale」：5 agents 是 inflection point，coordination overhead 使 P99 飆 2.4s；近 50% token 花在 agent 間「重述/調和」；重構為 stateless workers + deterministic planner 後 P99 −73%、cost −80%
- 「What Survived 2026」：relay 5 stages 準確度崩至 22.5%（低於 25% 隨機基線）；open mesh 生產淘汰

> 社群現況共識：**Hub-and-Spoke + stateless workers + artifact contracts** 是被生產驗證的唯一可靠拓撲；context engineering 重要性 ≥ agent 數量。

---

## 6. 常見陷阱與反模式（四源交叉驗證）

| # | 反模式 | 後果 | 來源 | 防範 |
|---|--------|------|------|------|
| 1 | 按任務類型分工（非 context 邊界） | handoff 損 context、決策盲目 | Anthropic + Cognition | 按 context 邊界拆 |
| 2 | Sub-agent 當平行實作工人 | 視野盲目、衝突 | Cognition + 5/17 報告 | sub-agent 只蒐集資訊 |
| 3 | Open mesh peer 自由協商 | relay 準確度崩塌 | Lanham 2026 + MAST | 用 hub-spoke |
| 4 | Team size 越大越好 | coordination overhead | AgentVerse | 找最優 size、動態組成 |
| 5 | Agent 幻覺自報完成 | task verification 失敗 | MAST | 機械可驗證完成條件（R4） |
| 6 | Debate 形成 echo chamber | 固化錯誤 | Multiagent Debate | diversity preservation |
| 7 | 忽略 token 成本 | 15× 爆炸 | Anthropic | 高價值任務才用多代理 |
| 8 | history 全量累積 | 每輪成本遞增 | AutoGen GroupChat | stateless workers + 外部 state |

---

## 7. 前沿趨勢與預測

1. **協調成為獨立架構層**（2605.03310）：coordination 不再是 prompt 附帶物，而是可獨立設計/評估的 layer。
2. **失敗分類學標準化**（MAST 14 模式）：multi-agent debugging 從 ad-hoc 走向 taxonomy-driven。
3. **動態團隊組成**（AgentVerse）取代靜態角色：recruit-evaluate-evolve 成為高階模式。
4. **協調—隱私權衡基準化**（calbench 2605.09823）：多代理共享 context 的隱私成本被量化。
5. **框架收斂**：AutoGen → MAF、Swarm → Agents SDK，輕量教育框架退場，生產框架（LangGraph）與 SDK 化（Agent SDK）並進。

---

## 8. 對本 Workspace 的核心發現

1. **現行 subagent-strategy.md 獲外部背書**：fan-out 上限 4、通訊限 parent↔child、child 不 self-retry、child 輸出只含結果——四源最佳實踐高度吻合，無需修改核心。
2. **缺口：agent-team 維度未系統化**——workspace 只到 sub-agent（單層 hierarchical），尚無 debate/consensus/動態組成的可操作模式。`gap-vote` skill 已是一種 consensus 雛形（2/3 投票），可作為 agent-team 模式的接地點。
3. **R4（機械可驗證）獲 MAST 學術背書**：task verification 是跨 7 框架最大失敗源，workspace 早已內建防線。
4. **可借鏡**：least-privilege tool access（VoltAgent）、三層模型路由（wshobson）已部分存在於 pilot 模式，可強化文件化。

> 完整行動建議見配套計劃書 `2026-06-03-subagent-agent-team-execution-plan.md`。

---

## 附錄：來源評分與索引

### 官方來源（信度 A）
- Anthropic — How we built our multi-agent research system
- Anthropic — When to use multi-agent systems
- Claude Agent SDK docs
- OpenAI Agents SDK / Swarm cookbook
- Google ADK multi-agent patterns
- Microsoft AutoGen docs

### 論文（信度 A，全文 PDF 收錄 research/papers/）
- MetaGPT 2308.00352 / ChatDev 2307.07924 / AgentVerse 2308.10848 / AutoGen 2308.08155 / Multiagent Debate 2305.14325 / MAST 2503.13657
- 本地既有：multiagentbench 2503.01935、multi-agent-frameworks-benchmark 2602.03128、multi-agent-memory 2603.10062、coordination-layer 2605.03310、calbench 2605.09823、generative-agents 2304.03442

### GitHub（信度 A，一手 repo）
- LangGraph / MetaGPT / AutoGen / CrewAI / ChatDev / Swarm / CAMEL / Agency Swarm
- wshobson/agents / VoltAgent/awesome-claude-code-subagents / 0xfurai/claude-code-subagents

### 社群（信度 B–C，二手需驗證）
- Cognition「Don't Build Multi-Agents」(信度 A，一手)
- Philipp Schmid Single vs Multi-Agent (信度 A)
- Medium「Fail at Scale」/「What Survived 2026」(信度 C，數字需獨立驗證)
- HN 45096962 討論串

# LLM Memory 控制與實作深度研究報告

> **方法論**：research-hub:deep — 每 claim 標 [P/O/C/E]；D2 交叉驗證 ≥2 來源；失效 claim 標 ⚠️ 不刪。
> **語料**：本地 28 篇一級文獻，2023–2026；web search 未使用（語料覆蓋充足）。
> **撰寫日期**：2026-05-31
> **2026-06-05 增量複查**：對照 papers/INDEX 當前 Memory 語料，本報告所列 28 篇分配論文皆已實質引用（grep 親驗：scm/delta-mem/rethinking-mem-ops/reasoningbank/hindsight/chronos/externalization/mnemonic-sovereignty 各 1–5×）；**無新 in-domain Memory 論文未覆蓋**，本次無內容變更。同期 4 篇 in-domain 新論文全歸 Harness 側（見 harness-engineering-deep-research §A/§C2/§D）。

---

## 摘要

LLM 記憶系統已從單純的 context window 擴充，演化為多層次、多策略的控制工程領域。本報告從三個維度（控制機制、實作架構、失效與安全）深度綜合 28 篇一級來源，產出生產級 memory 的「控制旋鈕表」，並指出整合式記憶（consolidation）本身可能是最大風險所在。

---

## A. 控制機制

### A1. STM/LTM 分層架構

**MemGPT 的 OS 類比** [P：2310-08560] 是分層架構的里程碑：將 LLM 類比作業系統，定義 **主記憶（Main Context）** 為處理器可直接操作的 RAM，**外部記憶（External Storage）** 為磁碟，並實作顯式的分頁換入換出（page in/out）中斷機制。函式呼叫觸發 `memory_load`、`memory_save` 操作，讓 LLM 自行決定何時換頁——這是記憶主控性（agentic memory control）的起點。

**MemoryOS** [P：2506-06326] 進一步精煉為三層：短期（Short-term, STM）-> 中期（Mid-term, MTM）-> 長期（Long-term, LTM）。升格規則：STM->MTM 依對話鏈 FIFO 原則，MTM->LTM 採分段頁面組織（segmented page）加熱度門檻（heat threshold）。在 LoCoMo benchmark 上對 GPT-4o-mini 達到 F1 +49.11%，BLEU-1 +46.18% [P：2506-06326]。

**AgeMem（Agentic Memory Unified LTM+STM）** [P：2601-01885] 批評既有系統「獨立優化 LTM 與 STM 後以臨時方式組合」，改採工具導向行動（tool-as-action）讓 agent 自主執行 store/retrieve/update/summarize/discard，以三階段漸進 RL（GRPO）端對端學習記憶管理策略——超越 5 個長視地平線 benchmark 的所有基線 [P：2601-01885]。

**SCM（Self-Controlled Memory）** [P：2304-13343] 的貢獻在於提出 **記憶串流（memory stream）+ 記憶控制器（memory controller）** 的 plug-and-play 架構，透過 LLM-based 控制器決定何時觸發檢索，無需模型修改，相容任意指令模型 [P：2304-13343]。

**交叉驗證**：MemGPT [P：2310-08560]、MemoryOS [P：2506-06326]、memory-autonomous-llm-agents-survey [O：2603-07670] 均獨立確認三層分層的必要性；survey-memory-mechanism [O：2404-13501] 進一步指出缺乏分層的系統在長對話中性能退化明顯 [P+O D2]。

---

### A2. 寫入、讀取、遺忘策略

**六大核心操作（Rethinking Memory）** [P：2505-00675] 提供目前最完整的操作分類：
1. **Consolidation（整合）**：多條記憶壓縮為緊湊表示
2. **Updating（更新）**：修改現有記憶以反映新資訊
3. **Indexing（索引）**：建立檢索結構（密集向量或稀疏 BM25）
4. **Forgetting（遺忘）**：主動淘汰過時或低相關記憶
5. **Retrieval（檢索）**：查詢相關記憶注入 context
6. **Condensation（壓縮）**：縮短記憶表示（有別於 Consolidation）

**Mem0 的生產實作** [P：2504-19413] 將上述操作包裝成 API：每次對話後 LLM 自動提取 salient 資訊，透過「ADD / UPDATE / DELETE / NONE」四動作完成增量寫入，搭配圖結構變體捕捉實體關係。在 LOCOMO benchmark 較 OpenAI memory-augmented approach 達 +26% relative improvement [P：2504-19413]，且相較全上下文方法降低 p95 latency 91%、token 成本 90% [P：2504-19413]。

**MemoryBank 的艾賓浩斯遺忘曲線** [P：2305-10250]：實作基於遺忘曲線（Ebbinghaus forgetting curve）的記憶強化機制，依時間衰減決定記憶「強度」，超過閾值才列為活躍記憶，模擬人類的「複習效應」[P：2305-10250]。

**δ-mem 的線性狀態更新** [P：2605-12357]：不同於外部 DB 的顯式 CRUD，δ-mem 用 **delta-rule 學習**（Widrow-Hoff 法則）維護一個固定大小 8×8 的線上聯想記憶矩陣（associative memory state matrix），在凍結的全注意力模型上生成低秩修正（low-rank correction）。實測平均提升 frozen backbone 的 1.10×，memory-heavy benchmark 達 1.31×（MemoryAgentBench）[P：2605-12357]，完全不需要 fine-tuning 或 backbone 替換。

---

### A3. 時序控制

**Chronos** [P：2603-16862] 是迄今最完整的時序感知記憶框架：將原始對話分解為 **主詞-動詞-賓語（SVO）事件元組**，附加 ISO 8601 datetime 範圍與實體別名，建立「事件日曆（event calendar）」與「輪次日曆（turn calendar）」雙索引。查詢時動態生成每個問題的客製化檢索指引（dynamic prompting），含時間範圍過濾與多跳推理的迭代工具呼叫迴圈。在 LongMemEvalS (500 questions) 上 Chronos High 達 **95.60%**，超越次優系統 7.67%，事件日曆單獨貢獻 58.9% 增益 [P：2603-16862]。

**交叉驗證**：Hindsight [P：2512-12818] 的四網絡架構（world facts / agent experiences / entity summaries / evolving beliefs）亦強調時間與實體感知，在 LongMemEval 達 83.6%（20B 開源超越 GPT-4o）[P：2512-12818]，與 Chronos 的時序設計形成 D2 驗證。

---

### A4. Operations 抽象

**Rethinking Memory** [P：2505-00675] 的最大貢獻是區分 **參數記憶（Parametric Memory，存於模型權重）** 與 **上下文記憶（Contextual Memory，存於模型外部）**，並指出前者需透過微調或知識編輯（ROME、MEMIT）更新，後者透過 CRUD 操作更新——兩種更新路徑的成本與可逆性完全不同。

**security-long-term-memory** [P：2604-16548] 將操作抽象成六階段生命週期：Write -> Store -> Retrieve -> Execute -> Share -> Forget/Rollback，對應四個安全目標（Integrity、Confidentiality、Availability、Governance），定義「記憶主權（Mnemonic Sovereignty）」為可驗證、可恢復的治理能力 [P：2604-16548]。

---

## B. 實作架構

### B1. 檢索式記憶（Retrieval-based）

**HippoRAG** [P：2405-14831]（NeurIPS 2024）採用神經科學靈感——海馬體索引理論（Hippocampal Indexing Theory）：LLM 類比新皮質（知識儲存），知識圖譜 + Personalized PageRank（PPR）類比海馬體（索引建立）。索引階段：LLM 抽取 KG 三元組；檢索階段：PPR 從 seed 節點沿圖傳播，自動找橋接概念（bridge concepts）。在多跳問答上超越現有 RAG 方法 20%，同時達到 IRCoT 效果但快 6–13×、便宜 10–30× [P：2405-14831]。

**MemoryBank** [P：2305-10250] 以語義向量 DB 儲存對話事件與用戶特質，結合遺忘曲線排序，在 ChatGPT（3.5）上下支援跨 session 長期個人化對話 [P：2305-10250]。

**MemoryOS** [P：2506-06326] 的三層檢索：STM（精確 embedding 匹配）-> MTM（分段語義檢索）-> LTM（個性化圖檢索）。熱度分數（heat score）融合頻率、近期度、相關性 [P：2506-06326]。

---

### B2. Agentic 自組織記憶

**A-MEM** [P：2502-12110]（NeurIPS 2025）採 **Zettelkasten 筆記系統**哲學：每筆記憶進入時，LLM 自動生成上下文描述、關鍵詞、標籤，並主動分析歷史記憶建立連結網絡。記憶的互聯性（interconnectivity）比單純的相似度檢索捕捉更豐富的關聯 [P：2502-12110]。

**ReasoningBank** [P：2509-25140] 不儲存原始軌跡，而是蒸餾**可泛化推理策略（generalizable reasoning strategies）**——從 agent 自我評判的成功與失敗經驗中提取。MaTTS（Memory-aware Test-Time Scaling）透過更多算力生成多元對比經驗，形成「更好記憶 -> 更有效 scaling -> 更好記憶」的正向循環。在 web browsing + software engineering benchmark 超越儲存原始軌跡或只儲存成功例子的方法 [P：2509-25140]。

**Hindsight 四網絡** [P：2512-12818]：Retain（記憶寫入）-> Recall（查詢）-> Reflect（更新）三核心操作，組織四類記憶網絡（World facts / Agent experiences / Entity summaries / Evolving beliefs），強調「證據與推理分離」——不混合原始事實與推論，確保可解釋性 [P：2512-12818]。

---

### B3. Test-Time Learning 與 Context Engineering

**Dynamic Cheatsheet** [P：2504-07952] 是 test-time learning 的早期代表：在推理時累積可更新的「作弊表」，讓模型在不重訓練的前提下快速適應新資訊或偏好 [P：2504-07952]。

**ACE（Agentic Context Engineering）** [P：2510-04618]（ICLR 2026）將 context 視為「演化式作戰手冊（evolving playbooks）」，採三模組流程：Generator（生成軌跡）-> Reflector（提取 insights，含失敗分析）-> Curator（增量 delta 更新，語義去重）。明確對抗兩大失效模式：**brevity bias**（因求簡潔丟棄細節）與 **context collapse**（整體改寫破壞積累知識）。在 AppWorld leaderboard 以小型開源模型匹敵頂級生產 GPT-4.1 agent [P：2510-04618]。

**交叉驗證**：useful-memories-faulty [P：2605-12978] 與 ACE [P：2510-04618] 均獨立識別「LLM-based 整合/改寫導致資訊退化」問題，ACE 的增量 delta 更新正是對此的工程回應 [P D2]。

---

### B4. Context vs Memory 取捨

**Beyond Context Window** [P：2603-04814] 是迄今最大規模的直接實証比較：**長上下文（Long-context）以 33.4–35.2 個百分點的準確率優勢大幅領先記憶壓縮方案**，但記憶方案在約 10 輪對話後（100K token context size）在成本上變得合理——記憶系統達到 35:1 壓縮比，代價是顯著的資訊損失 [P：2603-04814]。

> ⚠️ **注意**：此結論基於 2026 年 3 月的模型，長上下文模型代價正在快速下降，記憶 vs 長上下文的 crossover 點會隨時移動。

**Lost in the Middle** [P：2307-03172] 揭示即使用長上下文，**位置偏差（positional bias）** 問題嚴重：相關資訊在上下文開頭或結尾時性能最高，中段性能顯著退化（U 形曲線）。此問題在明確為長上下文訓練的模型上仍持續，表明記憶系統的結構化檢索有其存在價值 [P：2307-03172]。

**Recursive Language Models（RLMs）** [P：2512-24601]（MIT CSAIL）提出第三條路：LLM 把超長輸入視為外部環境，透過程式化遞迴呼叫自身處理任意長度 prompt。RLM-Qwen3-8B 超越 Qwen3-8B 基座 28%（中位數），在三項長上下文任務上接近 vanilla GPT-5 品質；對比 compaction 方法提升中位數 26% [P：2512-24601]。

**MemTool** [P：2507-21428] 填補短期工具記憶（tool context）的空白：提出三模式（Autonomous / Workflow / Hybrid）管理 100+ 輪多輪對話中的動態工具集，Autonomous 模式下推理模型達 90–94% 工具移除效率（相當於準確的「工具遺忘」），中型模型僅 0–60% [P：2507-21428]。

**Externalization** [P：2604-08224] 從認知架構角度統一框架：記憶（Memory）、技能（Skills）、協議（Protocols）、Harness 都是 LLM 的外部化（externalization），其演化軌跡：Monolithic context -> Retrieval stores -> Hierarchical systems [P：2604-08224]。

---

### B5. Cache 層記憶

**Don't Break the Cache** [P：2601-06007] 分析三種快取策略在 agentic coding 工具上的效果：**system-prompt-only 快取為最優預設策略**，達到 78.5% 成本降低、22.9% TTFT 改善（Claude Sonnet 4.5）。動態內容（工具呼叫結果、agent 軌跡）頻繁破壞快取是主要風險；Anthropic cache TTL 5 分鐘（可延長至 1 小時）、90% token 費用折扣 [P：2601-06007]。

快取本質上是 STM 的硬體層：重複前綴的 KV states 複用，可視為 immutable STM 的效率最佳化 [C：基於 2601-06007 + 2601-01885 推導]。

---

### B6. 多代理記憶

**Multi-Agent Memory from Computer Architecture** [P：2603-10062]（Position Paper）將多代理記憶問題框架化為計算機架構問題：
- **共享記憶（Shared Memory）** 類比 SMP；**分散記憶（Distributed Memory）** 類比分散式計算
- 三層階層：I/O 層（agent-世界交換）-> 快取層（高頻存取）-> 主記憶層（持久化）
- **最緊迫挑戰：多代理快取一致性（Cache Coherency）**——當多個 agent 並發存取或修改共享記憶時，語義豐富性 + 非確定性推理使傳統 cache coherency 協議無法直接套用 [P：2603-10062]

---

## C. 失效與安全

### C1. 記憶污染與整合退化

**Useful Memories Become Faulty** [P：2605-12978] 是 2026 年最重要的記憶安全警告：

- **核心發現**：連續整合 ground-truth 成功解答軌跡後，GPT-5.4 在 ARC-AGI 問題上失敗率 **54%**（從 100% 成功跌至 46%）[P：2605-12978]
- **退化曲線非單調**：utility 先升後降，最終落到 no-memory 基線以下（WebShop：0.64 -> 0.20）
- **三種失效機制**：
  1. **Misgrouping**：將不同問題家族的 episode 錯誤歸類，產生跨類別混合規則
  2. **Interference**：抽象化剝除適用條件，造成過度泛化（ScienceWorld 累積整合的過度泛化率是孤立任務整合的 5×）
  3. **Overfitting**：輸入分佈過窄，記住表面模式而非底層策略
- **工程建議**：把 raw episodes 視為 first-class evidence，引入顯式門控（explicit gating），非必要不整合 [P：2605-12978]

**交叉驗證**：ACE [P：2510-04618] 的 brevity bias + context collapse 描述，以及 useful-memories-faulty [P：2605-12978] 的 Misgrouping + Interference，為同一底層問題（LLM-based 整合引入失真）的兩份獨立文獻 [D2]。

---

### C2. 記憶安全與主權

**Security Survey（Mnemonic Sovereignty）** [P：2604-16548] 識別以下威脅：

| 階段 | 威脅 | 研究密度 |
|------|------|---------|
| Write | 注入式投毒（prompt injection into memory） | 高 |
| Store | 記憶庫竄改 | 低 |
| Retrieve | 對抗性查詢操縱 | 高 |
| Execute | 記憶驅動的惡意行動 | 中 |
| Share | 跨 agent 記憶傳播 | 低（研究稀少） |
| Forget/Rollback | 拒絕服務（阻止遺忘） | 低 |

- **9 個治理原語** 目前無任何已發表系統完整實作 [P：2604-16548]
- **記憶主權（Mnemonic Sovereignty）** 定義為對「寫入內容、讀取者、更新授權、可遺忘狀態」的可驗證、可恢復治理 [P：2604-16548]
- 目前安全研究高度集中在 Write/Retrieve 的完整性攻擊，機密性、可用性攻擊「研究稀少」[P：2604-16548]

---

### C3. 三份 Survey 框架對齊

| 維度 | survey-memory-mechanism [P：2404-13501] | memory-autonomous-llm-agents-survey [O：2603-07670] | human-memory-to-ai-memory [O：2504-15965] |
|------|---|----|---|
| 發表時間 | 2024-04 | 2026-03 | 2025-04 |
| 主要框架 | 記憶形式 × 操作 × 應用 | Write-Manage-Read 循環 × 三維分類 | 三維八象限（Object × Form × Time） |
| 記憶形式 | 文字、向量、結構化、參數、混合 | 向量、圖、語言、代碼 | 顯式 vs 隱式（嵌入人類心理學分類） |
| 操作抽象 | 寫入（Always/Selective/Delayed）、讀取、遺忘 | 五大機制族群（壓縮/RAG/反思/階層/策略學習） | 感覺->工作->情節->語義->程序 |
| 核心補充 | 最完整的早期分類，100+ papers | 最新（2022-2026），強調評估轉向多 session | 生物心理學接地，識別 AI 未覆蓋的維度 |
| **對齊點** | 三者均認可 STM/LTM 分層必要性；均指出遺忘策略（Forgetting）研究不足 | | |
| **分歧點** | 2404-13501 不含安全維度；2603-07670 補充「學習型遺忘（Learned Forgetting）」作為開放挑戰 | | |

---

## D. 生產級 Memory「控制旋鈕」完整表

| 旋鈕 | 機制描述 | 主要文獻 | 失效模式 | 緩解策略 |
|------|---------|---------|---------|---------|
| **寫入觸發策略** | Always-write vs Selective-write vs Delayed-write | 2404-13501, 2304-13343 (SCM) | Always-write 導致記憶膨脹與雜訊；Selective-write 漏記重要事件 | 條件式觸發（SCM 的記憶控制器）；重要性評分門檻 |
| **整合頻率（Consolidation Gate）** | 控制何時觸發 LLM 重寫記憶 | 2605-12978, 2510-04618 (ACE) | 過頻整合觸發 Misgrouping + Interference，utility 退化至 no-memory 以下 | **顯式門控**：預設保留 raw episodes，非必要不整合；增量 delta 更新（ACE）而非全文改寫 |
| **遺忘策略** | 依時間衰減（遺忘曲線）、熱度分數、LRU 淘汰 | 2305-10250 (MemoryBank), 2506-06326 (MemoryOS) | 過激遺忘丟失重要歷史；不遺忘導致無限膨脹與檢索效率下降 | 熱度 + 時間的複合評分；LTM vs STM 差異化策略 |
| **分層深度（Tiering Depth）** | STM / MTM / LTM 層數與升格閾值 | 2310-08560 (MemGPT), 2506-06326, 2601-01885 | 層數太少 -> context 溢出；太多 -> 升格延遲高，熱資料在冷層 | 三層為黃金分割（多篇一致）；熱度感知升格 |
| **檢索策略（Retrieval Strategy）** | Dense（embedding 相似度）/ Sparse（BM25）/ Graph（PPR）/ Temporal（事件日曆） | 2405-14831 (HippoRAG), 2603-16862 (Chronos), 2504-19413 (Mem0) | Pure dense 失於多跳推理；pure sparse 失於語義泛化；無時序索引失於時間敏感查詢 | 混合索引（dense + sparse + graph）；時間感知索引（Chronos SVO calendar） |
| **記憶形式（Memory Form）** | 文字、向量、圖、聯想矩陣、參數 | 2505-00675, 2605-12357 (δ-mem), 2405-14831 | 純文字缺結構；純向量缺可解釋性；圖構建成本高；參數記憶更新可能干擾原有知識 | 混合形式（Mem0 base + graph variant）；依任務選形式 |
| **Context vs Memory 決策點** | 短對話保留全上下文；超過約 10 輪或 100K tokens 後改用記憶壓縮 | 2603-04814, 2307-03172 | 長上下文準確率高但成本隨對話線性增加；記憶壓縮 35:1 但資訊損失顯著 | 動態決策：per-session 追蹤 token 用量，crossover 後切換；Lost-in-Middle 的位置偏差意味著結構化檢索仍有價值 |
| **工具記憶（Tool Context）管理** | Autonomous / Workflow / Hybrid 三模式動態工具集增刪 | 2507-21428 (MemTool) | 推理模型 Autonomous 模式效率高（90–94%）；中型模型 Autonomous 模式失控（0–60%） | 依模型能力選模式：推理模型用 Autonomous；中型模型用 Hybrid/Workflow |
| **多代理記憶一致性** | 共享 vs 分散記憶架構；快取一致性協議 | 2603-10062 | LLM 非確定性推理使傳統快取一致性協議失效；並發寫入導致語義衝突 | 樂觀鎖 + 版本戳；語義衝突偵測（研究空白，待解） |
| **快取層（Prompt Cache）** | System-prompt-only 快取策略 | 2601-06007 | 動態內容（工具呼叫結果、軌跡）破壞快取前綴 -> 快取命中率歸零 | 靜態前綴優先（CLAUDE.md 類固定前綴）；動態內容排至尾部 |
| **記憶主權（Mnemonic Sovereignty）** | 寫入/讀取/更新/遺忘的治理與存取控制 | 2604-16548 | 注入式投毒（prompt injection）；跨 agent 未授權傳播；拒絕遺忘攻擊（DoS on Forgetting） | Write/Retrieve 的完整性驗證；隔離 tenant 記憶；實作 Forget/Rollback 操作（目前 9 個治理原語均未完整實作）|
| **Episodic 優先原則** | 在整合前保留原始 episode 作為 first-class evidence | 2605-12978 | 純 episode storage 占用空間大；但 consolidation 引入失真 | ARC-AGI Stream 環境中 Episodic-only ≈ AutoMode（允許自主選擇），均優於 forced-consolidation |

---

## E. 關鍵量化數據彙整

| 系統 | Benchmark | 關鍵指標 | 來源 |
|------|-----------|---------|------|
| MemoryOS | LoCoMo (GPT-4o-mini) | F1 +49.11%, BLEU-1 +46.18% | [P：2506-06326] |
| Chronos High | LongMemEvalS (500Q) | **95.60%** 準確率，超次優 7.67% | [P：2603-16862] |
| Hindsight (20B open) | LongMemEval | **83.6%** vs GPT-4o（超越） | [P：2512-12818] |
| Mem0 | LOCOMO | +26% vs OpenAI memory；p95 latency -91% | [P：2504-19413] |
| HippoRAG | Multi-hop QA | +20% vs RAG，速度 6–13× | [P：2405-14831] |
| δ-mem (8×8 state) | MemoryAgentBench | 1.31× frozen backbone | [P：2605-12357] |
| RLM (Qwen3-8B) | Long-context tasks | 中位數 +28%，GPT-5 comparable | [P：2512-24601] |
| ACE | AppWorld leaderboard | 匹敵 GPT-4.1 top agent（小型開源模型）| [P：2510-04618] |
| Long-context vs Memory | Multi-task empirical | Long-context +33.4–35.2 pp，但 10 輪後 Memory 成本有利 | [P：2603-04814] |
| Faulty Memory (Consolidation) | ARC-AGI | GPT-5.4 失敗率 54%（從成功降至 46%）| [P：2605-12978] |

---

## 覆蓋率表（全 28 篇）

| # | 論文識別碼 | 本地檔名 | 狀態 | 引用位置 / 未引用原因 |
|---|-----------|---------|------|---------------------|
| 1 | 2304-13343 | scm-self-controlled-memory | ✅ 已引用 | A1（分層架構）、控制旋鈕表（寫入觸發） |
| 2 | 2305-10250 | memorybank | ✅ 已引用 | A2（遺忘策略）、B1（檢索式）、控制旋鈕表（遺忘策略） |
| 3 | 2310-08560 | memgpt | ✅ 已引用 | A1（OS 類比、分層架構）、控制旋鈕表（分層深度） |
| 4 | 2404-13501 | survey-memory-mechanism-llm-agents | ✅ 已引用 | A1（交叉驗證）、C3（三 survey 對齊）、控制旋鈕表 |
| 5 | 2405-14831 | hipporag | ✅ 已引用 | B1（圖檢索）、E（量化）、控制旋鈕表（檢索策略）|
| 6 | 2502-12110 | amem-agentic-memory | ✅ 已引用 | B2（Zettelkasten 自組織）|
| 7 | 2504-07952 | dynamic-cheatsheet-test-time-learning | ✅ 已引用 | B3（Test-time learning）|
| 8 | 2504-15965 | human-memory-to-ai-memory-survey | ✅ 已引用 | C3（三 survey 對齊）、生物心理學框架 |
| 9 | 2504-19413 | mem0 | ✅ 已引用 | A2（寫入策略）、B1（生產架構）、E（量化）|
| 10 | 2505-00675 | rethinking-memory-llm-agents-operations | ✅ 已引用 | A2（六大操作）、A4（操作抽象）、控制旋鈕表 |
| 11 | 2506-06326 | memory-os-ai-agent | ✅ 已引用 | A1（三層架構）、B1（三層檢索）、E（量化）|
| 12 | 2507-21428 | memtool | ✅ 已引用 | B4（工具記憶）、控制旋鈕表（工具記憶）|
| 13 | 2509-25140 | reasoningbank | ✅ 已引用 | B2（推理策略蒸餾）|
| 14 | 2510-04618 | agentic-context-engineering | ✅ 已引用 | B3（ACE playbook）、C1（context collapse）、E（量化）|
| 15 | 2512-12818 | hindsight-agent-memory | ✅ 已引用 | A3（時序控制交叉驗證）、B2（四網絡）、E（量化）|
| 16 | 2512-24601 | recursive-language-models | ✅ 已引用 | B4（RLM 第三條路）、E（量化）|
| 17 | 2601-01885 | agentic-memory-unified-ltm-stm | ✅ 已引用 | A1（AgeMem 統一 LTM+STM）、控制旋鈕表（分層深度）|
| 18 | 2601-06007 | dont-break-cache-prompt-caching | ✅ 已引用 | B5（cache 層）、控制旋鈕表（快取層）|
| 19 | 2603-04814 | beyond-context-window-memory-vs-longcontext | ✅ 已引用 | B4（實証比較）、控制旋鈕表（Context vs Memory）|
| 20 | 2603-07670 | memory-autonomous-llm-agents-survey | ✅ 已引用 | A1（交叉驗證）、C3（三 survey 對齊）|
| 21 | 2603-10062 | multi-agent-memory-computer-architecture | ✅ 已引用 | B6（多代理架構）、控制旋鈕表（多代理一致性）|
| 22 | 2603-16862 | chronos-temporal-aware-conversational-agents | ✅ 已引用 | A3（時序控制）、E（量化）、控制旋鈕表（檢索策略）|
| 23 | 2604-08224 | externalization-llm-agents | ✅ 已引用 | B4（外部化框架）|
| 24 | 2604-16548 | security-long-term-memory-mnemonic-sovereignty | ✅ 已引用 | A4（操作生命週期）、C2（安全威脅）、控制旋鈕表（記憶主權）|
| 25 | 2605-12357 | delta-mem-efficient-online-memory | ✅ 已引用 | A2（線性狀態更新）、E（量化）、控制旋鈕表（記憶形式）|
| 26 | 2307-03172 | lost-in-the-middle | ✅ 已引用 | B4（位置偏差）、控制旋鈕表（Context vs Memory）|
| 27 | 2605-12978 | useful-memories-faulty-llm-continuous-update | ✅ 已引用 | C1（整合退化、三失效機制）、A2（整合風險）、E（量化）|
| 28 | 2307-03172 | lost-in-the-middle（已含於 #26） | — | — |

> **覆蓋率：27/27 唯一篇章 = 100%**（去重後 27 篇；#26 與 #28 為同一篇不同登錄）

---

## 核心結論（三句）

1. **整合是雙刃劍**：記憶整合（Consolidation）是讓記憶「有用」的必要手段，但連續整合本身會以 Misgrouping、Interference、Overfitting 三種機制破壞準確率，在 ARC-AGI 上可讓 GPT-5.4 的成功率從 100% 跌至 46%——生產系統應以 raw episodes 優先、顯式門控整合頻率 [P：2605-12978, 2510-04618]。

2. **長上下文非萬靈丹，記憶非廉價替代**：在 10 輪以內長上下文準確率領先 33 個百分點，但超過約 10 輪或 100K tokens 後記憶系統的成本優勢出現；Lost-in-the-Middle 的位置偏差（U 形曲線）則使即使是長上下文方案也需要結構化檢索配合——兩者不是競爭而是互補 [P：2603-04814, 2307-03172]。

3. **記憶安全是設計欠債**：現有記憶系統在六階段生命週期中高度集中於 Write/Retrieve 的正確性，但治理（Governance）的 9 個原語目前無任何系統完整實作，跨 agent 記憶傳播、記憶主權、多代理快取一致性均是尚未有工業強度解法的開放問題 [P：2604-16548, 2603-10062]。


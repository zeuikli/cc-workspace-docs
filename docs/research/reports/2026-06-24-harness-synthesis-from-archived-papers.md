---
title: "Harness 綜合研究報告 — 從 219 篇收錄論文到可執行的 workspace 演化任務"
date: 2026-06-24
branch: claude/clever-einstein-571f2k
dimensions: [agents, commands, hooks, refs, rules, skills, workflow, loop, goals, harness, self-improve, self-learn]
method: overnight-research pipeline（corpus 萃取 4-way fan-out → gate-vote 3-lens 共識）
scope: research/papers/ (219 篇為 2026-06-24 原始分析基準；後續 Routine D 增量批次持續併入，累計收錄數見附錄 A 列數與 evolution/routine-d-baseline.txt)
type: research-report
---

# Harness 綜合研究報告：從收錄論文到可執行 workspace 演化任務

> **一句話**：本 workspace 的 harness 哲學（The Loop、判斷 vs 決定、hooks 強制 / 規則 advisory、unverified_success 閘門）已被 2026 年最新 harness 論文**大量獨立印證**；最大且一致的缺口是「**確定性 eval / regression gate 缺失**」與「**自動 trace pipeline 缺失**」——兩者正是 AEGIS seesaw、Self-Harness validation、AHE falsifiable prediction 的共同前置。

---

## 執行摘要

對 `research/papers/` 已收錄的 219 篇論文（重點為近期新增 72 篇：harness engineering / context / prompt-caching / KV-cache / token-budget / multi-agent orchestration / loop-workflow / goal engineering / memory / model-cards）做完整深度研究，產出 **12 維度 × (Findings 接地 → Gaps → Tasks)** 的綜合，並以 **gate-vote 三 lens 共識**對 36 條可執行任務分級。

三項可機械驗證的結論：

1. **印證 > 推翻**：論文對本 workspace 既有紀律幾乎全為正向印證——`LLM-as-Code (2606.15874)` 與 `Harness-MU (2606.21856)` 逐字對齊「判斷 vs 決定 / 治理交 hook 非 LLM」；`HarnessX seesaw (2606.14249)` 是 `unverified_success` 閘門的數學形式；`MAST (2503.13657)` 的 Task-Verification 失敗類別正是閘門針對的失敗。
2. **共同缺口收斂到兩件事**：(a) **確定性 eval/regression gate**——`healthcheck.sh` 非 task-level pass/fail 回歸套件；(b) **自動 trace pipeline**——AEGIS Digester / HarnessFix HTIR / AHE 皆依賴自動 trace，本 workspace 靠 MEMORY/LESSONS 人工記錄。**12 條 P0 任務中有 7 條直接服務這兩個缺口**。
3. **高接地任務 ≠ 高契合任務**：gate-vote 揭露數條「論文證據強但與 workspace 紀律衝突」的任務（如硬性 token gate 違「行為信號優先」、第五成功維度動 canonical 鐵律），已標 `TODO(conflict)` 不盲目實作。

**P0 共識任務（12 條）**：T2 T4 T5 T7 T9 T12 T13 T22 T23 T27 T28 T36（T4/T7/T23 三票全 P0）。

---

## 0. 研究方法與語料

| 項目 | 內容 |
|------|------|
| 語料 | `research/papers/` 219 篇 .md（72 篇為本 session 前置新增） |
| Phase 1 | 4-way researcher fan-out 做 corpus 萃取（每維度 Findings 接地 arxiv_id + Gaps 指向 workspace 檔案 + Tasks 含規模），輸出存 `research/scratch/paper-syn-*.md` |
| gate-vote | 3 個 reviewer 以不同 lens（① 影響力×可行性 ② 接地強度 ③ workspace 契合度）對 36 任務投 P0/P1/P2，2/3 多數決共識 |
| 驗證 | Phase 4.5 citation grep-back（arxiv_id 回 scratch）；Phase 5 healthcheck + wc -m |

> **方法限制（誠實標註）**：corpus 萃取由 sub-agent 完成，屬「判斷/摘要」on-rails 任務；arxiv_id 與機制描述以 scratch grep-back 抽驗，但未逐篇重讀全文 PDF。任務的「影響/可行」評級為 LLM 評審共識，非 benchmark 實測——落地仍須各任務自帶機械驗證。

---

## 1. 跨維度核心主題

論文證據在 12 維度上收斂成 **4 條主軸**：

### 主題 A — 確定性 gate 是 harness 的承重牆
`Harness-MU (2606.21856)`：治理約束是確定性 runtime 變數，必須交 execution hook，prompt-based safeguard 在多輪 adversarial 下必然失敗（+48.9pp）。`LLM-as-Code (2606.15874)`：token explosion / control-flow hallucination 是「把確定性工作交給機率系統」的架構後果，非 bug。`Maestro-Order (2606.23983)`：verify 幾何放大 0.55→(2gate)0.98→(4gate)0.999。`HarnessX seesaw (2606.14249)`：候選修改不得回退任何既有成功任務。→ **全部指向：本 workspace 的 advisory 規則需要對應的確定性 gate 落地層**。

### 主題 B — 沒有 trace，就沒有自我演化
`AEGIS (2606.14249)` Digester、`HarnessFix HTIR (2606.06324)`、`AHE falsifiable prediction (2604.25850)`、`Meta-Harness raw-trace>摘要 (2603.28052)`、`Self-Harness Weakness-Mining (2606.09498)` 共同依賴**自動 execution trace**。本 workspace RECORD 階段靠人工 MEMORY/LESSONS → **trace pipeline 是自我演化的缺失地基**。

### 主題 C — context 工程的反直覺：少即是多
`Less-Context-Better-Agents (2606.10209)`：pruning + summarization 使完成率 8%→91.6%、token −63%，full-history 反而產生 stale-state errors。`Max-Effective-Context (2509.21361)`：有效 context window 比宣稱短達 99%，且隨任務類型動態移動。`ACE (2510.04618)`：context collapse（整體改寫丟細節）是最大失敗模式，須增量 delta。→ 印證 `context-management.md` NLAH，但缺操作化 pruning 策略。

### 主題 D — goal drift 是可量測的長程風險
`Eval-Goal-Drift (2505.02709)` / `Inherited-Drift (2603.03258)` / `Asymmetric-Drift (2603.03456)`：環境壓力使所有模型偏離 system prompt 目標；被 condition 在弱 agent trajectory 後繼承漂移；constraint 與內化強 value 對立時違反率更高。`Subgoal-Driven (2603.19685)`：subgoal 分解 + milestone reward 使 SR 6.4%→43.0%。→ 本 workspace 列 goal drift 為失敗模式但無偵測機制。

---

## 2. 十二維度分析

> 格式：**F** = Findings（接地 arxiv_id）｜**G** = Gaps（workspace 現況）｜**T** = Tasks（→ 任務總表編號）

### 2.1 harness
- **F**：harness 四要素 necessary&sufficient = agent loop + tool interface + context mgmt + 確定性控制（2606.10106，T4 最關鍵）；AEGIS 四階段 Digester→Planner→Evolver→Critic+Gate（2606.14249）；ETCLOVG 七層故障分類 +15.2~50%（2606.06324）；harness 佔 agent 能力 98.4%（2604.20938）；六大 runtime 責任 observation/context/control/action/state/verification（2606.20683）；Latent-State-UI 顯式提示 LLM 推估 UI 環境隱藏狀態（動作/進度/錯誤/完成），零樣本任務成功率 28.1%→45.9%（1.6 倍），為六大責任中「state」一項首次提供獨立量化證據（2405.11120）；SWE-agent 以 Agent-Computer Interface（ACI）四原則（動作簡單易懂／緊湊高效／回饋資訊豐富但精簡／guardrail 攔錯誤傳播）取代原始 shell，SWE-bench Lite 上僅靠介面設計即取得 10.7pp 提升（論文原文用語），消融顯示 `edit` 指令搭配自動語法檢查（linting）達 18.0% resolved、拿掉 linting 掉到 15.0%（−3.0pp）、完全不給 edit 只給 bash 則掉到 10.3%（−7.7pp），為「工具介面 error-guardrail 設計」提供首次量化的邊際貢獻（2405.15793）；MemTool 於 ScaleMCP benchmark（5,000+ 工具、100 輪多輪對話）比較 Autonomous/Workflow/Hybrid 三種工具記憶管理模式，reasoning 模型（GPT-o3/Gemini 2.5 Pro/Claude Opus 4）在 Autonomous 模式下 3-turn rolling 工具移除率達 90–94%，但中型模型（LLaMA 3 70B/Claude 3.5 Sonnet）Autonomous 模式移除率僅 0.244/0.062、改用確定性 Workflow 模式後回升至 0.932/0.917，「模型能力弱時交確定性 workflow 比信任模型自主判斷可靠」與 core.md「判斷 vs 決定」公理同構（2507.21428）；Source Code Agent 框架把工作流邏輯編碼為確定性「Execution Blueprint」、LLM 僅處理有界複雜子任務，τ-bench 上比最強 baseline 高 10.1pp 平均 Pass@1、案例研究工具呼叫數減少 66–82%，其 Double-Check 模組（決策點程式化重注入約束防 model drift）與 Tool Consolidation（多步驟封裝為單一高階操作）為既有「判斷 vs 決定」公理落地提供具體技術詞彙（2508.02721）；SWE-Bench Pro 以 41 個維護中儲存庫 1,865 題建立長程任務基準（平均變更規模 107.4 行/4.1 檔，遠高於原始 SWE-Bench 約 30 行/1–2 檔），failure-mode 分析顯示不同能力層級模型主要敗因系統性不同——frontier 模型（Claude Opus 4.1）敗因以「語意理解」占 35.9% 為主，較小模型（Qwen3 32B）則以「語法錯誤+工具使用」占 42% 為主（2509.16941）。
- **G**：無自動 trace pipeline（`core.md` §RECORD）；無確定性 eval gate（`healthcheck.sh` 無 task-level regression）；故障未按 ETCLOVG 分層（`memory/LESSONS.md` 自由格式）；workspace 現有對應機制 `.claude/hooks/post-edit.sh`（PostToolUse Edit|Write，對 `.sh`/`.json`/`.py` 做語法驗證）語意上是 **warn-only**（`SYNTAX_RESULT=1` 只印警告、hook exit 1 不阻斷，`post-edit.sh:19-22,61-90`），與 SWE-agent ACI `edit` 指令的 reject-with-diff（拒絕含語法錯誤的 edit、強迫當場修正）不同，SWE-agent 消融的 −3.0pp 提供「即時攔截語法錯誤具體提升多少完成率」的量化依據（2405.15793）；`context-management.md:7`「Deferred tool loading」僅規定工具**新增**面向的按需載入（`ToolSearch` 按需取 schema），未涵蓋 MemTool 揭示的**移除**面向——`grep -rln "tool.*remov\|dynamic tool" .claude/agents/*.md .claude/skills/*/SKILL.md` 0 命中，確認 workspace 無任何機制處理多輪對話中工具集合的動態淘汰，惟現行委派場景工具數遠低於論文 128 上限情境，屬前瞻性 Gap（2507.21428）；本文「workflow 邏輯與生成模型分離、確定性程序負責流程控制」核心主張與既有 `LLM-as-Code`（2606.15874）及 core.md「判斷 vs 決定」公理高度重疊，屬再次獨立印證非新缺口，唯 `grep -n "blueprint\|Double-Check\|Tool Consolidation" .claude/refs/harness-design.md` 0 命中，確認該檔既有「Rule → Hook 升格決策」矩陣未收錄此二具體機制名詞（2508.02721）；`.claude/skills/harness-meta/references/harness-audit-CHECKLIST.md` 與 `harness-audit-METRICS.md` 皆無「失敗模式依模型能力層級分流」判準，`grep -rln "semantic understanding\|syntax.*tool-use\|capability.*failure mode" .claude/ research/` 於 `.claude/` 治理檔零命中，命中散落 `research/` 語料（含 `research/ai-articles/scored/2026-03-01-swe-bench-pro-morphllm.md` 同主題既有條目）（2509.16941，2026-07-30 ceiling 審計勘誤：原文「僅 research/ai-news 噪音」低估命中範圍，已修正，`.claude/` 零命中的承重結論不變）。
- **T**：T1（ETCLOVG 模板）、T2（seesaw 回歸 checklist）、T3（SessionEnd trace stub）、T48（post-edit.sh warn-only→block 評估）、T63（context-management.md 補工具動態淘汰對稱面）、T64（harness-design.md 補 Double-Check/Tool Consolidation 詞彙 + τ-bench 量化數字）、T66（harness-audit-CHECKLIST.md 補依檔位分流失敗子型，併入既有 T1）。

### 2.2 self-improve
- **F**：Self-Harness 三階段無外部 oracle，+17~21pp（2606.09498）；RHO 自偏好替 ground-truth，SWE-Bench Pro 59→78%（2606.05922）；SIA 雙槓桿 harness+權重（2605.27276）；AHE falsifiable edit prediction 69.7→77%（2604.25850）；Meta-Harness raw trace > 摘要（2603.28052）；Reflexion 語言化反思迭代（Actor-Evaluator-Self-Reflection）無梯度更新即達成 self-correction，GPT-3.5+Reflexion HumanEval 91% pass@1 超越 GPT-4 基線 80%，但 sliding window 截斷早期反思（2303.11366）；Constitutional AI critique-revise 循環為同類「模型自我修訂輸出」訓練期早期範式（2212.08073）；RLAIF 經 ICML 同儕審查證實同能力 AI labeler（甚至與被訓練 policy 相同）仍可提供有效訓練訊號、Direct-RLAIF 跳過獨立 reward model 效果更優；論文 Limitations 段落註明「capable model 可能學會 exploit AI labeler 偏好」為此研究**未處理**的對抗魯棒性風險（非作者實證發現，屬待研究缺口），可作既有 loop.md §L4「壞 oracle 比沒有更糟」的提醒性引用，但不構成該原則的新實證佐證——論文核心結論方向其實相反（同能力 labeler 訓練訊號有效）（2309.00267，2026-07-27 ceiling 審計勘誤：原文誤植為「作者自陳警示」+「peer-reviewed 實證佐證」，已修正歸因）；DeepSeek-R1-Zero 僅用 GRPO 對可驗證任務（數學答案正確性/程式碼測試通過）做結果導向獎勵訓練、無人工標註逐步驟 CoT 監督、無 SFT 熱身，訓練後自發湧現 self-reflection/solution verification/hypothesis backtracking/adaptive strategy selection，AIME 2024 達 71.0% pass@1（2501.12948）——**層次澄清**：此為**模型訓練期**現象（RL 更新權重使模型內部生成含自我反思的 token 序列），與本 workspace The Loop 的 self-reflection/backtracking（**agent 執行期**、由 harness/prompt/hook 在多 tool-call turn 間迭代、不改模型權重）屬不同層次機制，不構成「The Loop 該改用 RL 訓練」或「訓練期實證等於執行期有效」的依據，僅作為既有 Reflexion（2303.11366，執行期對照組）的訓練期類比參照記錄。
- **G**：自我改進靠人工觸發無 Weakness-Mining clustering；`autoload-evolution` 無跨 task regression；AHE falsifiable 機制只在 harness-meta。
- **T**：T4（falsifiable prediction 欄）、T5（coreset.md）、T6（LESSONS re-clustering）。

### 2.3 self-learn
- **F**：ReasoningBank 雙向對比蒸餾（2509.25140）；Dynamic Cheatsheet 黑盒 test-time learning +27pp（2504.07952）；EvolveR closed-loop lifecycle（2510.16079）；Beaver evaluate→diagnose→revise GRAS 81.0（2606.21005）；context collapse 須增量 delta（2510.04618）；RAG 確立參數/非參數記憶分離範式，外部索引可更新無需重訓模型，為此譜系奠基前驅（2005.11401）；Generative Agents 以 recency+importance+relevance 三因子加權公式排序記憶喚起，消融顯示反思層為維持長程可信行為的必要條件（2304.03442）；SCM 把「存什麼/何時存/何時取/何時刪」四項記憶決策獨立於 LLM backbone、以顯式門控 + 雙緩衝實作，即插即用免微調（2304.13343）；MemoryBank 以 Ebbinghaus 遺忘曲線量化衰減公式 `R=e^(-t/S)`（成功召回增 S、未召回則 R 隨時間衰退低於閾值淡出），為 T38 落地時「時間衰減」子機制提供具體數學模型候選（SCM 只給四項決策框架、無衰減函式本身）（2305.10250）；ExpeL 提出三階段無梯度更新學習框架——offline consolidation 對比失敗/成功軌跡提取自然語言洞見 + 推論時 Top-K 向量檢索注入，隨經驗累積持續提升且部分跨任務遷移，可作 T9 落地時的具體 prompt 設計參考（2308.10144）；CoALA 提出 working/episodic/semantic/procedural 四分記憶分類 + 讀/寫/整合/遺忘四類操作，統一映射 ReAct/Reflexion/MemGPT/Voyager/Generative Agents，為記憶研究提供共同詞彙表而非新機制（2309.02427）；MemGPT 論文自陳為「two-tier memory architecture」——in-context main context（含 working memory）+ out-of-context external context（再分 recall storage 與 archival storage 兩個儲存位置），LLM 自主決定 push/pull/evict 時機，Deep Memory Retrieval 任務達 92.5%（vs fixed-context GPT-4 僅 32.1%），且支援任意深度巢狀 function chaining 多跳檢索不失敗（vs fixed-context 深度 3 即失敗）（2310.08560，2026-07-27 ceiling 審計勘誤：原文誤稱「三層模型」，MemGPT 原文明寫 two-tier，「三層」為 HippoRAG 論文對照表對 MemGPT 的外部概括而非 MemGPT 自述，已修正並移除與 F 段「兩層」的內部矛盾）；Memory-Mechanism-Survey 系統化四分類記憶操作，並在整合步驟旁註記引用 2605.12978 提出的效能退化風險警告（survey 自身「發現 2」措辭較保守：整合步驟資訊丟失「後來經該篇系統性驗證」，非 survey 獨立主張的「主因」），遺忘策略再分時間衰減/容量淘汰/主動刪除/覆蓋式遺忘四型，其中覆蓋式遺忘違反 core.md「不覆寫原始證據」（2404.13501，2026-07-27 ceiling 審計勘誤：原文誤將「記憶整合是效能退化主因」寫成 survey 自身強斷言，實為該 survey 引用他篇警告標記，已修正歸因）；HippoRAG 以知識圖譜三元組+Personalized PageRank 做單步多跳檢索，MuSiQue/2WikiMHQA/HotpotQA 平均超越前 SOTA +10.4pp，且比 IRCoT 迭代檢索快 6-13 倍、成本低 10-30 倍，為 T9 落地提供「單步 PPR-style vs 向量 top-K」的多跳檢索備選方案（2405.14831）；Step-back Profiling 以 LLM-based 摘要函式把使用者互動歷史一次性壓縮成聚焦特徵的「gist」profile，LaMP 個人化 benchmark 七項任務最高提升 3.6 點，消融顯示移除 profile 導致效能顯著下降、證明壓縮後 gist 本身是必要訊號而非冗餘（2406.14275，論文主題為科學寫作個人化資料集非 agent 系統，此處僅取記憶壓縮方法論做跨域類比，不誇大直接關聯）；RAG Best Practices 以 9 個消融研究問題檢驗 RAG 各組件：chunk size 存在最優點（非越大越好，RQ3）、query expansion 系統性提升精確度但效益依任務而異（RQ6）、Focus Mode（從 chunk 進一步萃取句子級精確上下文而非整段注入）在需精確 grounding 任務優於 full-chunk 檢索（RQ9）、並提出 Contrastive In-Context Learning RAG（demonstration 同給正確與對比性錯誤案例）（2501.07391）；A-MEM 以 Zettelkasten 卡片盒方法論做代理記憶——新記憶寫入時即生成含上下文描述/關鍵詞/標籤的完整筆記、分析歷史記憶建立連結，且新記憶整合可觸發既有記憶表示的更新，6 個基礎模型評估超越現有 SOTA（2502.12110）；Mem0 生產級記憶層，LOCOMO 基準 LLM-as-Judge 較 OpenAI 記憶增強法 +26%、Graph 變體再加約 2%，p95 延遲降 91%、token 成本降 90%+，準確率僅落後 Full-Context 5-10pp，生產實務證實衝突記憶不應自動合併、應保留衝突標記+時間戳最近優先+整合須留存所有證據（2504.19413）；Rethinking-Memory-LLM-Agents-Operations 定義 Parametric（模型權重內隱）vs Contextual（外部顯式）記憶二元框架，拆解六大操作 Consolidation/Updating/Indexing/Forgetting/Retrieval/Condensation，明確區分「整合（多筆→一筆）」與「壓縮（一筆→短筆）」為不同操作，並指出整合不可逆性（2505.00675）；Human-Memory-to-AI-Memory-Survey 以人類記憶心理學類比提出三維八象限分類框架（Object/Form/Time）+ 四項設計原則（選擇性鞏固/情境依賴回憶/記憶可塑性/遺忘功能性），並引用 2605.12978 整合退化問題作為待解缺口（2504.15965）。
- **G**：MEMORY.md 整體壓縮 = context collapse 風險；LESSONS.md 無 retrieval；learning loop 無 provenance；`memory/LESSONS.md` 現行入庫政策只講新增（同簽名重現 ≥2 次才改規則），無 SCM 式時間衰減/覆蓋率的刪除-淘汰決策，舊條目何時 superseded/retired 無明文政策（2304.13343）；MemGPT 的 in-context/out-of-context 雙層架構（out-of-context 再分 recall/archival 兩儲存位置）可作為 T38「淘汰（可復原）vs 刪除（不可逆）」語意區分的具體詞彙依據；現行 `memory-compactor.md` 實際機制是 AutoMode（Retain/Delete/Consolidate）+ Conflict Gate + Post-Prune 自驗（非「delta+dedup」——後者是 T8 尚未落地的提案，誤植為現況已修正），且已有「舊 session 移至 `Memory-archive-YYYY-MM.md`、主檔留指標區塊」的可復原歸檔機制（`.claude/agents/memory-compactor.md:64-73`），僅缺 MemGPT 式顯式 evict（可逆）vs retire（不可逆）二分命名（2310.08560，2026-07-27 ceiling 審計勘誤：原 Gap 誤稱現行機制為「delta+dedup」且忽略既有歸檔層，已修正避免 T45 落地時找錯基準）；`memory-compactor.md` Post-Prune 自驗（`memory-compactor.md:75-98`）目前只機械比對 Lesson 計數（grep 行數）與待辦區塊存活，驗的是結構性計數是否減少，不是壓縮後語意/功能保真度是否仍可推導出同一防範規則，抓不到「行數不變但關鍵觸發條件已在摘要中被稀釋」的壓縮失敗（2406.14275）；T9（LESSONS top-10 檢索）現有 HippoRAG/RAGAS/ExpeL 引用處理檢索演算法選型與評估指標，但未定義檢索 query 如何構成、也未涉及檢索後是否需句子級再萃取，RAG-Best-Practices RQ6（query expansion）與 RQ9（Focus Mode）恰補上這兩個互補視角（chunk-size 發現 RQ3 較不適用——LESSONS.md 條目本身已是原子精簡格式）（2501.07391）；A-MEM 式「新記憶寫入時即時雙向連結既有相關記憶」在 workspace 尚無對應——`memory-compactor.md:40` Consolidate 動作是批次觸發的被動合併，無寫入當下的即時關聯標記機制（2502.12110）；Mem0 的衝突處理策略與 `memory-compactor.md:44-49` Conflict Gate 幾乎逐字對齊，屬既有機制的生產級獨立驗證非新缺口，唯其 LOCOMO 按單跳/多跳/時間/開放域四類分項評測可補進既有 T9「無 retrieval 品質量測指標」的落地細節（2504.19413）；`memory-compactor.md:32-42` AutoMode 三分類（Retain/Delete/Consolidate）無獨立對應 Rethinking-Memory-Ops「Updating」操作——論文 `:74-84` 對 Updating 的定義僅止於「修改現有記憶以反映新資訊」+ 挑戰為「更新的原子性（避免自相矛盾）」，**論文本身未提及「保留舊→新可追溯連結」**，此為 workspace 落地時的**設計提案**（非論文主張，2026-07-29 ceiling 審計已修正歸因，避免誤讀為論文語意）：被後續 session 完全取代的情境現行歸入 Delete（完全捨棄），若比照論文 Updating 語意改為「修改而非捨棄」，落地時建議額外保留舊→新可追溯連結以避免與 core.md「不覆寫原始證據」產生張力（2505.00675）；Human-Memory-to-AI-Memory-Survey 四項設計原則主要為既有機制之印證——Episodic-First（`memory-compactor.md:18`）已對應「記憶可塑性」風險、AutoMode 已對應「選擇性鞏固」，其「情境依賴回憶」「遺忘功能性」兩項缺口已由既有 T9/T38 涵蓋，本篇僅作補充接地引用（2504.15965）。
- **T**：T7（LESSONS provenance 欄）、T8（memory-compactor grow-and-refine delta+dedup，與 T45 皆動 `memory-compactor.md`，落地順序見 §5）、T9（observe 注入 LESSONS top-10，落地時補 query-construction + Focus Mode 句子級 re-extraction 評估，2026-07-29 批次補 Mem0/LOCOMO 分類評測細節見 T59）、T38（LESSONS retirement/pruning 政策）、T45（memory-compactor.md 補 MemGPT in-context/out-of-context 雙層命名，區分 evict vs retire，與既有歸檔機制對齊）、T49（memory-compactor Post-Prune 補語意抽驗）、T56（memory-compactor.md 補新增 LESSON 時掃描既有條目、雙向加註交叉引用的輕量關聯標記子步驟，不做全動態表示重算）、T59（T9 落地時補 Mem0/LOCOMO 式按查詢類型分類的簡化版準確率抽驗）、T60（memory-compactor.md AutoMode 補第四類 Update，區別於 Delete/Consolidate，避免 supersede 案例覆寫證據）。

### 2.4 agents（含 sub-agent）
- **F**：MAST 14 失敗模式×3 類，Task-Verification 最難 = unverified_success 背書（2503.13657）；coordination-arch MAS 生產故障率 41~87% 主因協調設計，Hierarchical +26.6pp（2605.03310）；HALO 三層+MCTS +14.4%（2505.13516）；multi-turn-vs-single 多模型匹敵最強單模型但有 herding/self-preferential bias（2509.23537）；RL-orchestration-traces 5 sub-decision，stopping 無 explicit method = gap（2605.02801）；AdaptOrch 收斂後拓撲選擇邊際 > 模型選擇 = effort 先於 model 佐證（2602.16873）；ReAct 的 Thought-Action-Observation 交錯範式是 agent loop 理論原型，repo 內 `research/agent-harness/references/` 已標記為 agentic loop 理論根源，惟先前綜合報告附錄 A 未正式收錄，屬補溯性接地（2210.03629）；Generative Agents 展示沙盒多代理湧現社會協調行為，但屬人類行為模擬評估場景而非任務型 harness 協調機制，關聯較弱（2304.03442）；「Society of Minds」多 agent 辯論：N 個獨立實例先各自作答、多輪（T=3）互讀彼此答案後更新，無需外部裁判即收斂多數共識，Arithmetic/GSM8K/MMLU/傳記事實性/西洋棋合法走步皆有提升；歸檔分析（非論文原文直接主張）指出 echo chamber（錯誤共識固化）風險需 diversity preservation 機制，印證既有「三個問同樣問題的驗證者只換到三份同樣盲點」原則（2305.14325，2026-07-27 ceiling 審計勘誤：原文誤植為「作者明確警示」，echo chamber 一詞出自歸檔者「對 agent-team 設計的啟示」推導段而非論文原文引用段，已修正歸因）；MetaGPT 以結構化文件（非自由對話）作 agent 間傳遞介面防級聯幻覺，固定角色 SOP pipeline，token 效率 124.3 tokens/loc（較 ChatDev 省 50%），印證既有 Handoff Contract「傳結構化欄位」原則（2308.00352）；AutoGen 提出 ConversableAgent（LLM/tool/human 任意組合）+ GroupChat（廣播）+ Nested Chat（子對話遞迴委派）三種可組合通訊模式，把 multi-agent 協作降為可程式化基礎設施（2308.08155）；AgentVerse 動態招募/移除 agent 四階段 pipeline（Recruitment→Collaborative Decision→Independent Execution→Evaluation），發現團隊規模非越大越好，且需外部干預識別 groupthink/free-riding 等負向湧現，印證既有「無任務 DAG 複雜度→拓撲自動路由機制」缺口並補上「協作過程社會惰化偵測」子面向（2308.10848）；Persuasive-Debate 首次大規模實證「debate as scalable oversight」：結構化辯論使弱評審辨識強 AI 答案正確性準確率提升 48%→76%（模型）、60%→88%（人類），且訓練辯論者更具說服力並未降低真實性辨識準確度，與既有 Multiagent-Debate（2305.14325，無裁判多輪收斂共識）互補而非重疊——本文為「有明確裁判評審雙方」架構（2402.06782）；AgentPrune 首次形式化定義 LLM multi-agent pipeline 的「communication redundancy」問題，在 spatial-temporal message-passing graph 上做 one-shot pruning，六個 benchmark 以 $5.6 成本達到與 SOTA 拓撲相當效果（vs SOTA $43.7，約 87% 成本降幅）、retrofit 進既有框架可降 28.1%～72.8% token、對 agent-based adversarial attack（剪除惡意訊息邊）帶來 3.5%～10.8% 效能提升（2410.02506，官方摘要數字經 `curl export.arxiv.org` 之 `citation_abstract` meta 標籤核實，archived .md 該檔「Abstract」區塊截斷在此句之前，屬既有歸檔缺漏非杜撰）；RouteLLM 訓練 win-prediction router（Chatbot Arena 8 萬筆人類偏好 + MMLU golden-label + 約 12 萬筆 GPT-4 judge-label），以成本-品質權衡參數 α 決定路由，MT-Bench 減少約 75% 強模型呼叫仍保留 95% 表現、最高 3.66x 成本節省，routing 額外開銷 <0.4%，單一訓練好的 router 換模型組不需重訓仍維持表現；作者在 Limitations 明確自陳此工作侷限於**二元**路由，N-way 路由列為未解決開放問題（2406.18665）；MultiAgentBench 以星形/鏈形/樹形/圖形四拓撲 + 群體討論 + 認知計畫做多代理協調評估，引入 milestone-based KPI 取代單一終局成功指標，主要發現：任務分數最高非最強模型（GPT-4o-mini）、圖形（高連通）拓撲在其研究場景中最有效、認知計畫使里程碑達成率 +3%（2503.01935）；RCR-Router 以 Token Budget Allocator + Importance Scorer（角色關鍵字/任務階段優先序/新近度訊號）+ Semantic Filter 做角色感知動態記憶路由，HotPotQA/MuSiQue/2WikiMultihop 三個 QA benchmark 上比 full-context 路由減少 25–47% token，證明最佳 context 選擇為 NP-hard（等價 0/1 Knapsack）故採貪婪啟發式，消融顯示效能 3–4 輪迭代後飽和、單 agent token 預算超過 2,048 後報酬遞減（2508.04903）。
- **G**：`.claude/agents/` 13 agent 中除 `multi-mode-agent`（spawn 時動態注入 `[mode]`/role）外多為固定角色，無「任務 DAG 複雜度→拓撲自動路由」機制；`AGENTS.md` dispatch table 無量化選擇標準；child 仲裁無 consistency scoring；stopping 缺達標主動 stop 確定性條件。〔審計勘誤：原作「14 全固定角色」雙重失準〕`graph.md` §G5 僅提「巢狀 `Agent(...)` 的 allowlist 靜默失效」，未涵蓋 AutoGen 式「child 本身可再做 orchestrator」的遞迴委派深度上限（2308.08155）；T12 fan-out aggregation gate 僅涵蓋輸出一致性檢查，未涵蓋協作過程中的趨同/搭便車偵測（2308.10848）；T41 現僅接地 2305.14325 單一辯論拓撲（無裁判多數收斂），未區分「有裁判辯論」與「無裁判收斂」兩種架構的取捨（2402.06782）；`graph.md` §G5（2026-07-29 ceiling 審計勘誤：原文誤標 §G3，該句實位於 §G5:50，已修正）「高連通拓撲擴大污染半徑」僅從資安半徑角度論證低連通結構優於 mesh，AgentPrune 從效率角度獨立佐證同一結論——但 workspace 現行 star 拓撲（`graph.md` §G2「child 間不互通」）已結構性側避開 AgentPrune 鎖定的核心場景（agent 間迭代辯論/mesh 通訊產生的冗餘訊息），屬印證既有拓撲選擇而非揭露新缺口，唯若未來採用 A2A peer-to-peer（既有 §2.6 loop 引用 2601.13671）則 message-level 冗餘/惡意訊息防線目前無對策（2410.02506）；既有 T11（AGENTS.md agent 選擇量化）對照 `model-profiles.md` 現行檔位路由是純規則式靜態閾值，未如 RouteLLM 以偏好資料訓練 win-prediction 模型；但直接移植有明確落地缺口——RouteLLM 本身只驗證過二元路由，workspace 是四檔位，N-way 是論文自陳未解問題，不能當現成方案直接複製（2406.18665）；`graph.md` §G5:50「高連通拓撲擴大污染半徑」目前只從資安/blast-radius 角度論證低連通結構優先，未涵蓋 MultiAgentBench 從任務效能角度得出的「高連通拓撲在協作密集場景可能更有效」發現——兩者論證方向不同，workspace 目前無「拓撲依安全敏感 vs 協作密集分流選擇」的判準；既有 `graph.md`/`delegation-protocol.md` 產出驗收僅終局 PASS/FAIL 二元判定，無 milestone-based 中途進度量測（2503.01935）；`graph.md:43`「節點間傳結構化欄位，不傳全量 context」是同方向規則層約束，但無角色感知量化路由機制——`grep -n "role.aware\|importance scor\|token budget" .claude/refs/*.md` 僅命中 `model-profiles.md:79`「per-task token budget ~4,000」這一扁平單值參數，無按 agent 角色/任務階段分配不同預算的機制（2508.04903）。
- **T**：T10（confirmation gate, ⚠衝突）、T11（agent 選擇量化）、T12（fan-out aggregation gate）、T13（self-escalate 達標主動 stop）、T39（graph.md §G5 補巢狀委派深度上限）、T40（fan-out 節點趨同/搭便車警覺）、T41（delegation-protocol.md §6 補多輪迭代辯論 vs 單輪 gate-vote 取捨）、T51（前瞻性：A2A 拓撲下補 AgentPrune message-level 防線）、T54（前瞻性：RouteLLM 概念設計四檔位 pairwise router，待有標註資料）、T57（graph.md §G5 補「高連通拓撲在協作密集場景可能有效能優勢，但 workspace 高風險域仍優先低連通、採高連通須額外對抗複審」的 tradeoff 說明；delegation-protocol.md 分解 rubric 補里程碑式中途進度指標作為 verify 節點補充量測維度，非取代終局 gate）、T65（delegation-protocol.md 補角色/任務階段感知 context 篩選設計參考，RCR-Router 三組件拆分，前瞻性）。

### 2.5 workflow
- **F**：workflow-opt-survey ACG 統一抽象三軸/三層（2603.22386）；SEW 自動演化 topology+prompt +12%（2505.18646）；challenges-iterative 僅 9% agents 用 automated optimization，三隱藏選擇 starting-artifact/credit-horizon/minibatch（2603.23994）；self-organizing-MAS 三相 + verification 攔截缺陷（2603.25928）；AgentCompass dual-memory post-deployment 監控（2509.14647）；ChatDev「虛擬軟體公司」waterfall 分階段 + Chat Chain（流程切成有序雙人 instructor/assistant 原子對話，相鄰階段對話不跨階段廣播）+ Communicative Dehallucination（assistant 給出不確定/錯誤陳述時 instructor 主動觸發澄清追問迭代消幻覺），印證既有 `graph.md` §G1 pipeline-as-default 原則，但揭示既有 Handoff Contract 缺乏「相鄰節點對不確定陳述主動追問」的內嵌校正機制（2307.07924）。
- **G**：`multi-mode-skill` 缺 structure-aware evaluation；dynamic workflow 三失敗模式無 post-run 監控；`handoff` Return 未收 credit_horizon/starting_artifact；`graph.md` §G4 Handoff Contract 只規定 child 回報結果、parent 事後驗收——**收窄後的缺口**：`graph.md:41` Return 已含 `open_questions`、`multi-mode-agent.md:53` 已有 `[claim:verified]/[claim:asserted]/[claim:judgment]` 三級標記且要求 parent 對 asserted 100% 重驗，故「不確定性顯式標記」半邊已存在；真正缺的只有 ChatDev 式「**下游收到不確定標記後主動觸發追問迴圈**」，現行機制止於「parent 事後重驗」，無「相鄰節點即時 challenge-response」（2307.07924，2026-07-27 ceiling 審計勘誤：原文高估此 Gap，誤稱標記機制整體缺失，已收窄範圍避免 T44 落地時與既有 claim-tier 機制重工）。
- **T**：T14（post-run 觀測 checklist）、T15（handoff Return 補欄, ⚠分歧）、T44（delegation-protocol.md 補「下游對 `[claim:asserted]`/`open_questions` 主動追問」的 challenge-response 迴圈，非新增標記機制本身）。

### 2.6 loop
- **F**：agent-loops-to-graphs Agent Loop 三弱點（implicit deps / unbounded recovery / mutable history），SGH explicit DAG 有 termination+soundness guarantee（2604.11378）；sovereign-loops SAL 解耦 reasoning/execution，model 發 intent → control plane 對照 state+policy 才執行，攔截 93% unsafe（2604.22136）；orchestration-survey MCP+A2A substrate，A2A peer-to-peer 與「child 間不直接溝通」張力（2601.13671）；ReAct（2210.03629）Thought-Action-Observation 範式與 The Loop OBSERVE→IDENTIFY/PROPOSE→APPLY 結構系出同源譜系，本報告既有引用的 agent-loops-to-graphs（2604.11378）、sovereign-loops（2604.22136）均為此譜系下游延伸；Let's Verify Step by Step 證實 process supervision（逐步驟給分 PRM）顯著優於 outcome supervision（僅終局給分），MATH 子集達 78%，PRM 評分取「最弱步驟分數」代表整條推理鏈品質，釋出 PRM800K；此機制與既有 Maestro-Order（2606.23983）「多個平行獨立終局 gate 幾何放大」互補而非重複——PRM 是單鏈內逐步序列化評分，Maestro-Order 是多終局 gate 並聯（2305.20050）；LLMCompiler 的 Planner 自動分析任務間資料依賴、產生可平行執行的 DAG（非人工判斷邊），對比 ReAct 循序執行 latency 最高降 3.7x、cost 最高降 6.7x 且準確率同時提升 ~9%，為「編譯器式依賴分析取代人工猜測邊」提供量化佐證，可操作化既有 graph.md §G1「畫邊前問下游需要上游哪個具體產出」（2312.04511）；Weak-to-Strong Generalization 顯示弱模型監督者微調出的強模型效能持續超越監督者本身，但存在顯著 imitation gap（未達強模型 ground-truth 監督上限），需輔助 confidence loss 才能部分補回缺口，標準 RLHF 對「監督者能力低於受監督模型」場景可能根本不足——為既有 loop.md §L4「壞 oracle 比沒有更糟」補上一種獨立偏差來源：oracle 能力上限本身低於待驗對象（2312.09390）；Scaling Test-Time Compute 比較兩種擴展機制——process-based verifier reward model（PRM）逐步驟評分做 best-of-N re-ranking、與 blockwise MCTS 做迭代式分布更新——依 prompt 難度自適應選擇：中等難度 best-of-N+PRM re-ranking 較有效率、高難度 MCTS 式迭代精修較有效率，difficulty-adaptive 分配比均勻分配基線達超過 4 倍效率提升，MATH benchmark 上使小模型於等算力下匹配/超越參數量大 14 倍的模型（2408.03314，核心新增是「依難度動態切換兩種資源分配機制」，與既有 Let's Verify Step by Step 2305.20050 互補而非重複——後者是單鏈內逐步評分方法論，本文是「該用平行採樣還是序列精修」的資源分配策略問題）；s1 以「budget forcing」推論期機制（模型欲終止思考時附加 Wait token 強制延伸、或提前注入 end-of-thinking token 強制截斷）搭配僅 1,000 筆精選 SFT 資料，s1-32B AIME24 達 56.7%（vs o1-preview 44.6%）、MATH500 93.0%，實證思考長度與難題準確率正相關，驗證 sequential test-time compute 假說，不需 verifier 或平行取樣，與既有 Scaling-Test-Time-Compute（2408.03314）互補（2501.19393）；LLMs-Get-Lost-Multi-Turn 15 模型跨 6 任務 20 萬+模擬對話證實多輪 underspecified 對話較單輪平均下降 39%，根因非能力損失（aptitude 僅 -16%）而是不可靠性暴增 +112%，四項根因含過早假設、過度依賴先前錯誤答案、忽略中段對話（loss-of-middle-turns）、回應冗長引入更多假設，reasoning 模型與降溫皆無法緩解，唯一可靠解法是一次性給齊全部資訊（2505.06120）。
- **G**：The Loop advisory 無 termination guarantee / node state machine；SAL Evidence Chain（deterministic replay）缺；stopping decision 無形式化；`the-loop-best-solution.md` §TEST 僅涵蓋「終局驗證」與「多道獨立終局 gate」，缺乏「長鏈任務品質受限於最弱中間步驟而非平均/終局」的顯式 weakest-link 原則（2305.20050）；`graph.md` §G1 依賴分析目前純靠人工/LLM 判斷，無 LLMCompiler 式自動依賴偵測輔助（2312.04511）；`loop.md` §L4 現有三種偏差來源（oracle 自身不穩定/環境差異/快取值當真值）未涵蓋「oracle 能力上限低於待驗對象」這一獨立來源（2312.09390，2026-07-27 ceiling 審計勘誤：原文誤稱首項為「造假」，loop.md §L4 並無此詞，「造假」屬 §L3 reward hacking 範疇，已修正標籤）；`loop.md` §L1 已規定 Verifier 須為與 writer 不同 instance、只回 PASS/FAIL 不得自己修，也無「依任務難度動態切換 best-of-N vs 迭代精修」機制；`graph.md:29` 已明文規定 verify 品質不夠時「先加互斥視角 → 再升 effort → 最後才升檔位」三步序（`graph.md:23` verify 節點「靠數量與互斥視角，不靠檔位」），故非本文所示「只有升 effort/檔位兩個旋鈕」——**現行三步序講的是 verification-side（驗證者視角多樣性）**，本文講的是 **generation-side（先產生 N 個候選解答再排序選優）**，是尚未涵蓋的獨立軸，非既有機制的重工，唯落地時措辭須明確區分兩者以免與 §G2 混淆（2408.03314）；`refs/model-profiles.md:317` 已記錄 `MAX_THINKING_TOKENS` 為平台注入 env 覆蓋點但無「任務難度→何時該建議調高」的政策說明，s1 式強制延伸機制在 workspace 尚無對應文件化判準（2501.19393）；LLMs-Get-Lost 的「loss-of-middle-turns」與既有 NLAH 規則（`context-management.md:8`「MIDDLE 最易失真」）方向一致，屬對話輪次場域的獨立印證（原引注 Lost-in-the-Middle 2307.03172 為檢索場景），非重複；「逐輪漸進式澄清會累積不可靠性、唯一有效緩解是一次性給齊資訊」表面像未涵蓋的 Gap，但 2026-07-29 ceiling 審計 + 主對話親驗發現與既有規則**正面衝突**：`.claude/skills/know-your-unknowns/SKILL.md:43`（T6 The Interview）與 `.claude/agents/multi-mode-agent.md:40` 皆明文「Known Unknowns → Interview **一次一題**」「**一次只問最貴的 1–3 題**，其餘等答案收斂後再問，避免一次倒 10 題稀釋回答品質」——與論文建議的「一次性給齊全部資訊」方向相反，**不得靜默採用論文方向覆寫既有規則**（TODO(conflict)，詳見 §4）（2505.06120）。
- **T**：T16（intent-gate 詞彙, ⚠重複風險）、T17（node state machine, P2 過度工程）、T42（the-loop-best-solution.md §TEST 補 weakest-link 原則）、T46（delegation-protocol.md 補 LLMCompiler 式依賴分析方法論）、T47（loop.md §L4 補 oracle 能力上限子節）、T50（loop.md/model-profiles.md 補 generation-side 平行採樣+獨立 verifier 選優，與既有 graph.md §G2 verification-side 互斥視角區分開、不重工，並核對 §G3 fan-out 上限是否衝突）、T55（`refs/model-profiles.md` 補 difficulty-adaptive thinking budget 政策說明：任務初判失敗或屬高風險域時記錄何時應建議調高 `MAX_THINKING_TOKENS`，純文件層級不做 gate，因平台覆蓋點非 repo 可控）、T61（`TODO(conflict)`，見 §4——與既有「一次一題」規則衝突，不得直接落地）。

### 2.7 goals
- **F**：goal drift 可量化（2505.02709）；inherited drift（2603.03258）；asymmetric drift，constraint 與內化強 value 對立時違反率更高（2603.03456）；subgoal 分解+milestone SR 6.4→43.0%（2603.19685）；policy decomposition 跨任務重用 62.5% vs ~0%（2605.06957）。
- **G**：`core.md` 成功條件四維無第五維 goal-drift resistance；`subagent-strategy.md` 列 goal drift 但無偵測機制；refs 無 goal-engineering 專章。
- **T**：T18（第五維, ⚠動 canonical 鐵律→改 refs）、T19（goal-restatement anchor）、T20（refs/goal-engineering.md）。

### 2.8 rules
- **F**：Harness-MU 治理交 hook（2606.21856）；LLM-as-Code program 掌 control flow（2606.15874）；Maestro-Order verify 幾何放大 0.55→0.999（2606.23983）；when-better-prompts-hurt 通用 prompt 反降 10~13pp，需 Define-Test-Diagnose-Fix（2601.22025）；Red Teaming LMs with LMs 確立「用 LM 生成對抗測試案例攻擊 target LM」自動化紅隊範式，核心發現多輪對話中 harm 可能於第 3-4 輪才浮現、個別輪次看似皆無害，為外部輸入多輪滲透風險提供獨立實證（2202.03286）；Constitutional AI 書面憲法（~16 條原則，可審計版本控制）示範治理規格書即程式碼的訓練期早期範式（2212.08073）；GCG（Greedy Coordinate Gradient）以梯度引導貪婪搜尋自動產生對抗後綴，開源模型（Vicuna）訓練即可遷移攻擊閉源系統（GPT-3.5 ~88% ASR、GPT-4 ~67% ASR），證明 RLHF 對齊不等於推論期對抗魯棒性——與既有 Red Teaming LMs with LMs（2202.03286）高度重疊，皆指向「無自動化對抗輸入生成機制」同一缺口，作為 T37 額外接地引用併入（2307.15043）；HarmBench 建立首個標準化紅隊評測框架，比較 18 種攻擊法 × 33 個目標模型/防禦，發現無單一攻擊全面制霸、防禦類別不互相遷移，且 R2D2 adversarial training 使 GCG 攻擊 ASR 降低 >90%，其四類行為分類法（standard/contextual/copyright/multimodal）可作 T37 對抗案例分類骨架的補充接地（2402.04249）；WildTeaming 從真實使用者與聊天機器人互動 log（WildChat/LMSYS 等平台）挖礦出 5.7K 個獨立 jailbreak tactic clusters，比研究者自建分類（<100 類）多出約 57 倍多樣性，雙 tactic 組合式攻擊比單一 tactic 高 15–30% ASR；產出的 WildJailbreak 資料集以 harmful/benign × vanilla/adversarial 四象限設計，其中 benign+adversarial（表面像有害實則良性的對比樣本）專門針對 over-refusal（過度拒絕）失敗模式（2406.18510）；Values-in-the-Wild 對 70 萬則匿名 Claude.ai 對話做 Clio 隱私保護分析，分類 3,307 個 AI 價值 + 2,483 個人類價值（人工驗證準確率 98.8%），Top AI 價值 Helpfulness 23.4%／Professionalism 22.9%，問題價值（sexual exploitation/dominance/amorality）各僅 <0.16% 頻率但可作潛在 jailbreak 識別的任務模式訊號，價值鏡映在支持互動中 20.1%、抵抗時僅 1.2%（2504.15236）；InstructDetector 用 Llama-3.1-8B-Instruct 第 14 層 hidden states + self-attention 梯度餵入 MLP，僅 200 筆訓練樣本即 in-domain 達 99.60%、out-of-domain 96.90% 偵測準確率，BIPIA benchmark 攻擊成功率壓至 0.03%，唯屬白盒方法（需存取 hidden states/梯度），與 workspace 僅能呼叫 API 端黑盒 LLM 有直接落地障礙（2505.06311）；約束式「Sculpting」提示在 GSM8K 全量 1,317 題基準上，gpt-4o（n=100）較標準 CoT 多 4pp（97% vs 93%），但 gpt-5（n=1,317）上與 Zero Shot 打平（94.00%）、落後標準 CoT 2.36pp（96.36% vs 94.00%），呈現作者稱「Guardrail-to-Handcuff transition」的能力依存反轉，獨立量化印證既有 core.md「程序性指導與能力成反比」公理（2510.22251）。
- **G**：`core.md`「判斷 vs 決定」無 hook 設計範式說明哪些行為轉交 hook；TEST 多道 gate 無量化依據；the-loop-best-solution 四維與 MVES 七維有語義缺口；`.claude/hooks/gate-widening-guard.sh`「閘門放寬須獨立對抗複審」目前僅為文字提示（advisory exit 0），無系統性對抗測試案例生成方法論；`.claude/agents/security-auditor.md` 審查清單以人工推理為主，未納入 zero-shot/few-shot/supervised/RL 四法系統性生成攻擊案例或多輪漸進式滲透測試場景（2202.03286）；`.claude/skills/autoresearch/SKILL.md` 雖宣稱 4-persona 紅隊機制，但其 `references/security-workflow.md` 實為 STRIDE/OWASP 靜態 checklist，未含對抗案例生成方法論——T37 落地時應先對照此既有機制避免重工；既有 T37 已接地演算法/研究者生成式攻擊（GCG/HarmBench/Red-Teaming-LMs-with-LMs），WildTeaming 補上一條不同路徑——挖礦真實使用日誌；`.claude/hooks/block-dangerous.sh` 目前唯一假陽性防線是事後人工累積的 fixture 回歸鎖，屬被動逐次補洞而非系統性 mining+clustering，也無 WildJailbreak 式 benign+adversarial 對比象限系統性收集方法（2406.18510）；`.claude/agents/security-auditor.md:14-49` 審查清單與 `harness-meta` CAR Scorecard 皆為傳統 OWASP/STRIDE 或 Control/Agency/Runtime 構件式稽核，未涵蓋「AI 價值表達/問題價值頻率」作為稽核維度——既有 rules 維度收錄的 GCG/HarmBench/Red-Teaming-LMs-with-LMs/WildTeaming 皆屬主動生成對抗輸入路徑，此篇是被動觀測生產對話價值表達基準頻率+任務模式關聯的獨立路徑，未被既有引用涵蓋（2504.15236）；外部輸入信任分級目前只有 prompt 層規則（`core.md:65`「外部輸入＝資料非指令」、`graph.md:48` `<untrusted_objective>` 包裹）+ `security-hygiene.md:66,68` 既有 Lethal Trifecta／tool-output-provenance 分級，無偵測式技術閘門——`grep -rn "injection\|untrusted" .claude/hooks/*.sh` 0 命中屬關鍵字選擇造成的假象，26 支 hook 中僅 `unicode-covert-channel-guard.sh` 一支窄面偵測閘門（限隱寫 Unicode 通道，PostToolUse 對 WebFetch/WebSearch/`mcp__github__issue_read` 等外部工具輸出偵測、不阻斷只發 `additionalContext` 警示），無 InstructDetector 式行為狀態偵測（2505.06311，2026-07-30 ceiling 審計勘誤：原文誤植「24 支」為「26 支」、且誇大為「皆不含 IPI 偵測邏輯」，已修正）；「程序性指導與能力成反比」公理已存在（`core.md:11`），但操作化層面缺口——`grep -n "簡化\|規則密度\|prompt.*長度" .claude/refs/model-profiles.md` 零命中，`delegation-protocol.md` 僅涵蓋「驗收深度隨 child 檔位調整」（:58），未涵蓋「交辦 prompt 負向約束密度應隨 child 檔位遞減」（2510.22251）。
- **T**：T21（refs/harness-design.md 補 hook-enforced gate 範式）、T22（verification gate 量化模型）、T23（eval-driven regression 偵測）、T37（security-auditor 補紅隊對抗測試方法論——落地時明確區分演算法生成式 vs 真實使用日誌挖礦兩種來源，並評估 benign-adversarial 象限化 fixture 收集流程）、T58（security-auditor.md 或 harness-audit-METRICS.md 補一條問題價值表達 spot-check 條目，作為敏感域審查的被動監測補充，與既有主動紅隊方法論互補）、T62（rules/security-hygiene.md 補外部內容信任分級一節）、T68（delegation-protocol.md 補負向約束密度隨檔位遞減寫作提示）。

### 2.9 refs
- **F**：Context-Engineering taxonomy 三基礎層+四系統層、1400+ 論文（2507.13334）；MECW 比宣稱短達 99% 且隨任務類型移動（2509.21361）；Less-context pruning+summary 8→91.6%（2606.10209）；RAG 確立檢索索引可獨立更新、模型權重不動的通用範式（2005.11401）；SPLADE v2 提供不依賴額外 dense embedding 模型、可沿用 inverted-index 基礎設施的稀疏詞彙檢索方案（max-pooling + 蒸餾，DistilSPLADE-max BEIR 平均 NDCG@10 達 0.500；SPLADE 本身仍需訓練，非免訓練），為既有 T9 落地時的檢索技術選型參考（2109.10086）；Lost in the Middle 以多文件問答+key-value 檢索任務證實 U 型效能曲線——關鍵資訊在 context 開頭/結尾效能最高、落中段顯著下降，且此現象跨模型家族/context 長度一致存在，是 `.claude/rules/context-management.md:8`「NLAH：context 放 HEAD 或 TAIL，MIDDLE 最易失真」規則的原始實證出處，唯先前引用溯及後續論文（2509.21361）未收此原始出處，屬 citation debt 而非功能性缺口（2307.03172）；RAG-Survey 系統化三階段演化分類（Naive→Advanced→Modular）外，其「評估工具」章節整理了 RAGAS/ARES/TruLens 等**第三方**標準化評估框架（faithfulness、context relevance、context precision/recall 等指標；非本 survey 自身貢獻——RAGAS 出自其參考文獻 Es et al. 2023），可作為填補原始 RAG（2005.11401）未涵蓋的「檢索品質評估工具鏈」缺口的參考索引（2312.10997，2026-07-27 ceiling 審計勘誤：原文誤稱 RAGAS/ARES/TruLens 為此 survey「獨立貢獻」，實為 survey 綜述整理的他人工具，已修正歸因）；Prompt Compression Survey 以 hard prompt（自然語言層刪減）vs soft prompt（訓練連續向量表徵）二分法系統化整理壓縮方法論，並從 attention optimization、PEFT、modality integration、synthetic language 四視角解釋壓縮機制（2410.12388）；歸檔摘要另記 soft prompt 類方法多數依賴白盒模型訓練/PEFT 存取權限、API-only 部署場景適用性弱一句，惟該句與同段落的成稿年份備註並列、疑似歸檔者評估而非論文原文直述，本環境 PDF 抽取管道不可用（`pypdf` 依賴缺失）故未能回溯原文確認，措辭上不歸為論文明確主張（2410.12388，2026-07-28 ceiling 審計標記：待補 PDF 原文核對）；Information-Preservation-Prompt-Compression 提出壓縮率之外的三軸整體評估框架——downstream 表現/輸入 context grounding/資訊保留，證明部分 SOTA 壓縮法無法保留關鍵細節，以控制壓縮 granularity 改進法達成 downstream +23%、grounding +8 BERTScore、entity 保留 2.7×，結論最佳 effectiveness/compression 權衡為 soft prompting + sequence-level training（2503.19114）；ACON 對長程 agent 環境觀察與互動歷史做壓縮，實現 26–54% peak-token 記憶用量削減且很大程度上保留任務效能，蒸餾至小型壓縮器後仍維持 95%+ 準確率，使小型語言模型於長程任務表現提升最高 46%（2510.00615）；OckBench 量化「Overthinking Tax」——7B 開源推理模型每題正確答案成本較 14B 模型高 57%（輸出 token 數為 3.13 倍），跨開源 vs 專有模型比較開源模型平均生成 token 數為專有模型基準的 5.1 倍（2511.05722）。
- **G**：`context-management.md` token budget 無任務類型分層；refs 無 context pruning/summarization 操作化文件；multi-agent-coordinator-pattern 未對照 context taxonomy；NLAH「MIDDLE 最易失真」規則引注缺原始出處——**規則本體位於 `.claude/rules/context-management.md:8`（L1 auto-load，零數字慣例，不宜內嵌 arxiv_id），`refs/context-engineering-claude5.md` 目前 0 命中 NLAH/MIDDLE/Lost-in-the-Middle 關鍵字，未替此規則建立可溯源指標**（2307.03172，2026-07-27 ceiling 審計勘誤：原文誤標目標檔為 context-engineering-claude5.md「已含 NLAH 規則本體」，實為該檔完全未提及，已修正 Gap 描述避免 T43 落地時找錯目標段落）；T9（LESSONS top-10 檢索）目前無 retrieval 品質量測指標，可借用 RAGAS 的 faithfulness/context-relevance 概念設計簡化版驗證，非引入完整工具鏈（2312.10997）；`.claude/skills/output-compress/SKILL.md` 已實作的三級（lite/full/ultra）自然語言層刪減 + 白名單保留 + `fidelity-check.py` 機械閘，功能上落在 hard prompt 陣營（符合 workspace 用 Claude API 而非白盒模型的現實），但 SKILL.md 全文未出現本綜述分類詞彙或引用，屬 citation debt（同既有對 2307.03172 的處理模式），非功能缺口（2410.12388）；**印證，非缺口**——`.claude/skills/output-compress/scripts/fidelity-check.py:132` 已直接明文引用 2503.19114，把 grounding 軸落地為詞級 token 接地率確定性指標；三軸中的資訊保留軸也已由白名單元素 diff（`code_block`/`number`/`date`/`path`/`tag`/`env_var` 等）實作，僅命名（entity vs 結構化 artifact）不同，非機制缺口；soft prompting 訓練側方法本身無法用於閉源 API，workspace 也僅借鑑評估框架、未打算落地方法本體（2503.19114）；既有 T24（`refs/context-pruning-strategies.md`）尚未建檔（`ls .claude/refs/context-pruning-strategies.md` 不存在），`.claude/agents/memory-compactor.md` 只處理跨 session 長期記憶檔壓縮（`grep -n "compress\|trajectory\|observation" memory-compactor.md` 零命中），未涵蓋 ACON 針對單一長程任務執行中的 tool-observation 壓縮，其「成對軌跡對比分析」（contrastive task feedback）機制目前無對應（2510.00615）；`model-profiles.md` §2.2 現有升降級門檻全為失敗次數觸發，`grep -n "overthink\|token.*生成" .claude/refs/model-profiles.md` 無命中，無「輸出 token 量爆增（即使答對）」作為獨立升檔觸發條件，`judgment-rubrics.md:44`「token/時間 > 原估 3×」為一般性停下問使用者觸發，非 cost→quality 自動升級機制（2511.05722）。
- **T**：T24（refs/context-pruning-strategies.md）、T25（taxonomy 檔, P2 淘汰）、T26（per-task-type MECW 警示, ⚠動 auto-load 風險）、T43（refs/context-engineering-claude5.md 新增 NLAH 溯源段引用 2307.03172，⚠L1 `context-management.md` 本體零數字慣例不動，僅補 1 行純文字指標指向此 refs 檔）、T52（output-compress/GOTCHAS.md 補引用 hard-prompt 座標，純文件債）、T67（context-management.md Compact 段補指向未來 T24 的 contrastive guideline optimization 子類別，純文件債）、T69（model-profiles.md §2.2 補 token 爆增升檔判準，cost→quality）。

### 2.10 skills
- **F**：83.3% skills in-wild 為 static doc，workspace 29 skills 屬 top 16.7%（2602.14690）；curated +16.2pp / self-generated −1.3pp（2602.12670）→ autoresearch 不可自動寫 skills；最佳 2~3 skills/session，lazy-load 正確（2602.12670）；HeavySkill inner-skill 驗證 opus-pilot 機制#2（2605.02396）；Voyager 三元件——自動課程（依當前技能水平動態生成下一探索目標）、可執行技能庫（儲存 Python 代碼而非文字摘要，向量+關鍵字雙索引）、迭代提示（環境回饋+執行錯誤+自驗，最多 3 次重試）——技能可跨新世界零樣本遷移而其他方法無法泛化，印證既有「29 skills 屬 static doc top 16.7%」缺口方向，可作 T27 empirical eval gate 落地時「執行錯誤回饋+N 次重試自驗」演算法細節參考（2305.16291）。
- **G**：無 skill evaluation harness（skill-evolution 有 7 維 scoring 無 empirical pass/fail gate）；`autoresearch` 整體無「明文禁止 runtime 寫入 `.claude/skills/`」的 guardrail（defense-in-depth，防 self-generated skill drift）。〔審計勘誤：原把風險歸因到 `autoresearch:learn`，但 learn 輸出為 `docs/`、已排除 `.claude`，故改為整體 guardrail 框架〕
- **T**：T27（skill-evolution empirical eval gate）、T28（autoresearch:learn block runtime write guardrail）、T29（opus-pilot inner-skill 文件, P2 淘汰）。

### 2.11 commands
- **F**：Claude Code 最廣 config 機制，CLAUDE.md 45.4% / AGENTS.md 40.6%，workspace 兩者皆有（2602.14690）；98.4% codebase 是 operational infra（2604.14228）；token-budget 63-incident overrun，delegation-fanout race 最難守（2606.04056）；coupling-tax split-budget（2605.07686）；Token-Budget-Aware Reasoning（TALE）實證 CoT 推理過程不必要地冗長，可透過 prompt 內注入合理 token budget 壓縮，且 budget 數值選擇是壓縮成效關鍵；提出 TALE 框架依每題推理複雜度動態估算並注入 budget，顯著降低 CoT token 成本僅輕微效能下降（archived 版本未含 abstract 具體百分比，本環境 PDF 抽取管道不可用，未回溯原文取得精確數字，故不引用未經核實的第三方轉述數字，見 §6.3）（2412.18547）。
- **G**：無 command-level token-budget 硬 gate（`CLAUDE_USAGE_LIMIT_USD` 僅 session 級）；無 pilot extended-thinking split-budget；`scripts/context-budget.sh` 未接 pre-dispatch gate；`.claude/refs/model-profiles.md` 只記錄平台 `MAX_THINKING_TOKENS` 為單一靜態 env 覆蓋點，無按任務複雜度動態估算的政策文件；`.claude/skills/output-compress` 壓縮的是已生成文字（post-hoc），TALE 針對的是生成前限制推理長度（pre-hoc），兩者機制互補但 workspace 目前只有前者完整落地；TALE 的 budget 估算機制細節（如何動態估算複雜度）archived 版本未載明，若引入須對照 core.md「判斷 vs 決定」——估算步驟可下沉判斷，但 budget 上限若當 gate 用仍須確定性程序把關，不能讓模型自報自限（2412.18547）。
- **T**：T30（per-fanout token-budget check）、T31（split-budget 文件, P2 淘汰）、T32（context-budget.sh 接 autoresearch gate）、T53（model-profiles.md §7 補 TALE 動態 budget 概念行，避免與 T31 重工，低優先）。

### 2.12 hooks
- **F**：Harness-MU 治理交 hook，workspace block-dangerous/protect-sensitive/branch-isolation-guard 已體現（2606.21856）；AOHP efficient agent interface −51.55% token（2606.23449）；dont-break-cache 四破壞模式 + system-prompt-only −78.5% cost（2601.06007）；CMV DAG trimming −20% token（2602.22402）；Active-Context-Compression −22.7% token 同精度（2601.07190）；Red Teaming LMs with LMs 三元件框架（red LM／target LM／harm classifier）可作為評估既有 hooks（`block-dangerous.sh`、`protect-sensitive-files.sh`、`gate-widening-guard.sh`）覆蓋率的方法論參照——用生成式對抗輸入主動測試而非僅靜態規則審閱（2202.03286）。
- **G**：無 PostToolUse **per-tool-call 即時** cache-health hook（已有 `session-init.sh` 月度 cache_hit_ratio 聚合，但非即時）；無 PreToolUse token-budget gate（advisory only）；`pre-compact.sh` 不顯示 remaining-context %；Stop hook 的 healthcheck PGE gate 僅 warn-only（`session-stop.sh:309-318`）。〔審計勘誤：cache 監控既有 session 級機制，claim 已收窄為 per-tool-call〕
- **T**：T33（PostToolUse cache-health 監控）、T34（PreToolUse token 硬 gate, ⚠違行為信號優先）、T35（pre-compact 注入 remaining %）、T36（session-stop healthcheck PGE gate）。

### 弱關聯備註（本批次論文誠實標記，不接地任何 Gap/Task）
- **Flamingo**（2204.14198）：凍結底層視覺/語言模型 + 輕量 gated cross-attention 橋接架構，與「不 fine-tune 模型本體、靠 context/skills/hooks 輕量擴充」哲學僅表層類比，屬視覺-語言模型架構論文，不接地任何 Gap/Task。
- **Toy Models of Superposition**（2209.10652）：神經元多義性是稀疏特徵壓縮下的必然最優解而非訓練缺陷，對「trace 為何難以單一歸因」提供機制性類比，但屬機制可解釋性基礎研究，與 12 維度工程治理主題關聯薄弱。
- **BLIP-2**（2301.12597）：凍結 vision encoder + 凍結 LLM + 輕量 Q-Former connector 的視覺-語言橋接架構，純 corpus 完整性記錄，不強行歸類。
- **LLaVA**（2304.08485）：以 GPT-4 生成合成 visual instruction-tuning 資料訓練多模態對話模型，純 corpus 完整性記錄，不強行歸類。
- **LLaVA-1.5**（2310.03744）：CLIP-ViT-L-336px + MLP connector + 學術 VQA 資料混合的視覺-語言模型改良版，與 harness/agent 工程治理 12 維度無關，比照既有 LLaVA 處理方式，純 corpus 完整性記錄。
- **SEDD**（2310.16834）：離散擴散語言模型（score entropy 訓練目標），純生成模型架構/採樣效率研究，與 agent harness 治理無關，比照既有 Toy-Superposition 處理方式，純 corpus 完整性記錄。
- **MDLM**（2406.07524）：Masked Diffusion Language Models，提出 SUBS 參數化將 absorbing-state diffusion ELBO 化簡為 BERT 式 MLM cross-entropy 加權和，LM1B/OpenWebText 取得 diffusion LM 中 SOTA perplexity。純模型架構/訓練目標設計研究，未涉及 agent loop、tool interface、context 管理、治理/hook 或 harness 工程任一環節，比照既有 SEDD 處理方式，純 corpus 完整性記錄。
- **MGDM**（2410.14157，Beyond Autoregression）：Multi-Granularity Diffusion Modeling，訓練期以 token/subgoal/solution 三粒度難度加權去噪目標函數解決「subgoal imbalance」，於 Countdown/Sudoku 等合成組合推理任務大幅超越自回歸模型。核心貢獻是 diffusion vs autoregressive 架構優劣比較與訓練期損失函數設計，與 12 維度工程治理主題無關，比照既有 SEDD 處理方式，純 corpus 完整性記錄。
- **LLaDA**（2502.09992）：Masked diffusion 語言模型架構，8B 規模挑戰 autoregressive 假設、解決 reversal curse，純模型架構/訓練目標設計研究，未觸及 agent loop/tool interface/context 管理/治理 hook/harness 工程任一環節，比照既有 SEDD/MDLM/MGDM 處理方式，純 corpus 完整性記錄。
- **HydraServe**（2502.15524）：公有雲 serverless LLM serving 的 GPU cold-start 優化（proactive model distribution、pipeline consolidation），cold start 降 1.7×–4.7×、SLO 改善 1.43×–1.74×，屬純雲端 GPU 基礎設施效能優化研究，與 hosted-model Claude Code 的 harness 治理無直接工程對應（無需自行管理 GPU model weight 載入），不強行歸類。
- **Which-Economic-Tasks**（2503.04761）：400 萬+ Claude.ai 對話經 Clio 隱私保護分析後對照 O*NET 職業任務庫的經濟/勞動市場實證研究（AI 使用集中軟體開發與寫作、36% 職業使用 AI 於 ≥25% 任務），屬人文/經濟使用模式分析而非 harness/agent 工程治理主張，不強行歸類。
- **AGP**（2506.02951）：雙階段 GCN + Gumbel-Sigmoid 訓練式多代理拓樸剪枝，依賴訓練基礎設施（460 組監督資料 + 反向傳播），workspace 現行 star 拓樸靠 prompt 規則（`graph.md` §G1–G3）不具備訓練管線；核心「訓練式雙剪枝」與既有已收錄 training-free 的 AgentPrune（2410.02506）方向相近但實作路徑互斥，不接地獨立 Gap/Task，僅記錄為前瞻性方法論參照。
- **PromptSci2**（2506.07142）：GPQA Diamond 業界基準測試報告，核心發現「reasoning 模型上顯式 CoT 增益邊際（RD ≤ 0.031）但延遲增 20–80%；non-reasoning 模型中 3/5 模型 CoT 損害 100% Correct（一致性）指標，同時 Average 分數 5/5 模型皆上升——即用一致性換平均分，非全面降低正確率」屬模型層級 prompting 建議，與 workspace `MAX_THINKING_TOKENS`（API 級 thinking 上限）為不同層次旋鈕，不接地治理性 Gap/Task（2026-07-30 ceiling 審計勘誤：原文誤將「3/5 模型損害 100% Correct 指標」寫成「反而降低正確率」，方向失準，已修正並補回 Average 全升的對照）。
- **BudgetThinker**（2508.17196）：SFT+RL 訓練介入控制 token 的推理框架，方法本體需微調模型權重，與 workspace 依賴閉源 API 模型的限制直接衝突，archived 摘要亦未取得具體效能百分比，不接地 Gap/Task。
- **AEIReport**（2511.15080）：150+ 國家、200 萬則對話的 Claude.ai/API 使用地理採用趨勢研究，屬總體經濟/使用模式分析而非 harness 工程機制論文，性質同既有弱關聯 Which-Economic-Tasks（2503.04761），不接地 Gap/Task。

---

## 3. 可執行任務總表（69 條 + gate-vote 共識；T37/T38 為 Routine D 2026-07-26 批次新增，T39-T44 為 Routine D 2026-07-27 第一批次新增，T45-T47 為同日第二批次新增，T48-T54 為 2026-07-28 批次新增，T55-T61 為 2026-07-29 批次新增，T62-T69 為 2026-07-30 批次新增，皆單一萃取判斷未過 3-lens gate-vote）

> 信心 = 3-lens 2/3 多數決（V1 影響×可行 / V2 接地 / V3 契合）。⭐ = 三票全 P0。

| ID | 任務 | 接地 | 影響檔案 | 規模 | 共識 |
|----|------|------|---------|------|------|
| T4 | autoload-evolution:propose 加 falsifiable prediction 欄 | 2604.25850 | autoload-evolution/SKILL.md | S | **P0 ⭐** |
| T7 | LESSONS.md 加 provenance 欄（date+tool+ETCLOVG layer） | 2606.21005,2604.25850 | memory/LESSONS.md | S | **P0 ⭐** |
| T23 | autoload-evolution 加 eval-driven regression 偵測 | 2601.22025 | autoload-evolution/SKILL.md | S | **P0 ⭐** |
| T2 | harness-meta:audit 加 seesaw 回歸 checklist | 2606.14249 | harness-meta/references/ | S | **P0** |
| T5 | 建 research/evals/coreset.md ≤10 失敗任務 + autoload Phase1 讀入 | 2606.09498,2606.05922 | research/evals/, autoload SKILL | M | **P0** |
| T9 | autoload-evolution:observe 加 retrieve LESSONS top-10（落地時補 query-construction + Focus Mode 句子級 re-extraction 評估） | 2509.25140,2504.07952,2312.10997,2405.14831,2501.07391 | autoload-evolution/SKILL.md | S | **P0** |
| T12 | parallel fan-out aggregation gate（consistency check） | 2602.16873,2509.23537 | subagent-strategy.md | S | **P0** |
| T13 | self-escalate 補達標主動 stop 條件 | 2605.02801 | agents/self-escalate.md | S | **P0** |
| T22 | the-loop-best-solution 補 verification gate 量化模型 0.55→0.999 | 2606.23983 | refs/the-loop-best-solution.md | S | **已完成**（`the-loop-best-solution.md:141` 已含此模型逐字對應；2026-07-27 ceiling 審計批次外連帶發現，狀態欄由 P0 更正為已完成，避免重工）|
| T27 | skill-evolution:scan 加 empirical eval gate | 2602.12670 | skill-evolution/SKILL.md | M | **P0** |
| T28 | autoresearch:learn 加 block runtime write .claude/skills guardrail | 2602.12670 | autoresearch/SKILL.md | S | **P0** |
| T36 | session-stop.sh 接 healthcheck PGE gate（補強既有） | 2604.14228 | hooks/session-stop.sh | S | **P0** |
| T33 | PostToolUse cache-health 監控 hook | 2601.06007 | hooks/ | S | P1 |
| T1 | ETCLOVG 七層故障分類模板 | 2606.06324 | LESSONS.md, harness-meta | S | P1 |
| T3 | SessionEnd trace stub JSONL | 2606.06324,2604.25850 | hooks/, healthcheck.sh | M | P1 |
| T6 | LESSONS.md 週期 re-clustering | 2606.09498 | LESSONS.md | S | P1 |
| T8 | memory-compactor 改 grow-and-refine delta+dedup | 2510.04618 | memory-compactor agent | M | P1 |
| T11 | AGENTS.md agent 選擇量化標準 | 2503.13657 | AGENTS.md | M | P1 |
| T14 | dynamic workflow 補 post-run 觀測 checklist | 2509.14647,2503.13657 | refs/multi-agent-coordinator-pattern.md | M | P1 |
| T19 | subagent-strategy 加 goal-restatement anchor | 2603.03258 | subagent-strategy.md | S | P1 |
| T21 | refs/harness-design.md 補 hook-enforced gate 範式（併入既有） | 2606.21856,2606.15874 | refs/harness-design.md | M | P1 |
| T24 | refs/context-pruning-strategies.md | 2606.10209,2509.21361 | refs/ | M | P1 |
| T30 | per-fanout token-budget check command | 2606.04056 | multi-mode-skill, context-budget.sh | M | P1 |
| T32 | context-budget.sh 接 autoresearch per-iteration gate（fail-open） | 2606.04056 | autoresearch/SKILL.md | S | P1 |
| T35 | pre-compact.sh 注入 remaining context % | 2601.07190,2602.22402 | hooks/pre-compact.sh | S | P1 |
| T16 | core.md APPLY/TEST 補 intent-gate 詞彙 | 2604.22136 | core.md | S | P1 |
| T26 | context-management 補 per-task-type MECW 警示 | 2509.21361 | context-management.md | S | P1 |
| T10 | subagent-strategy 補 confirmation gate | 2503.13657,2605.03310 | subagent-strategy.md | S | P1 ⚠ |
| T20 | refs/goal-engineering.md | 2505.02709,2603.03258,2603.03456,2603.19685 | refs/ | M | P2 |
| T15 | handoff Return 補 credit_horizon+starting_artifact | 2603.23994 | subagent-strategy.md | S | P2 ⚠分歧 |
| T17 | self-escalate node state machine | 2604.11378 | agents/self-escalate.md | M | P2 |
| T18 | core.md 補第五維 goal-drift resistance | 2505.02709,2603.03456 | core.md | S | P2 ⚠ |
| T34 | PreToolUse token-budget 硬 gate exit2 | 2606.21856,2606.04056 | settings.json, hooks/ | M | P2 ⚠ |
| T25 | refs/context-engineering-taxonomy.md | 2507.13334 | refs/ | M | P2 淘汰 |
| T29 | opus-pilot 文件化 inner-skill deliberation | 2605.02396 | opus-pilot/SKILL.md | S | P2 淘汰 |
| T31 | opus-pilot/fable-pilot split-budget 文件 | 2605.07686 | pilot SKILLs | S | P2 淘汰 |
| T37 | security-auditor 補紅隊對抗測試方法論（zero-shot/few-shot/supervised/RL 四法系統性生成攻擊案例 + 多輪滲透測試，強化 gate-widening-guard.sh 複審深度；落地前先對照 `autoresearch:security` 既有 4-persona 紅隊機制避免重工；另補真實使用日誌挖礦路徑，區別於既有演算法生成式攻擊，並評估 benign-adversarial 象限化 fixture 收集流程） | 2202.03286,2307.15043,2402.04249,2406.18510 | agents/security-auditor.md | S | P1（單一萃取判斷，未過 3-lens gate-vote，待覆核）|
| T38 | LESSONS.md 加 retirement/pruning 政策（時間衰減+覆蓋率，比照 SCM 刪除決策，補 T6 週期 re-clustering 外的淘汰維度） | 2304.13343,2305.10250 | memory/LESSONS.md, .claude/agents/memory-compactor.md | S | P2 ⚠衝突（單一萃取判斷，未過 3-lens gate-vote；與既有 Lesson 保全 gate 衝突見 §4）|
| T39 | graph.md §G5 補巢狀委派深度上限 + 授權須顯式重新宣告 | 2308.08155 | .claude/rules/graph.md | S | P1（單一萃取判斷，未過 3-lens gate-vote，待覆核）|
| T44 | delegation-protocol.md 補下游對既有 `[claim:asserted]`/`open_questions` 主動追問的 challenge-response 迴圈（標記機制本身已存在，不重工） | 2307.07924 | .claude/refs/delegation-protocol.md | S | P1（單一萃取判斷，未過 3-lens gate-vote，待覆核；2026-07-27 ceiling 審計已收窄 scope，規模由 M 降為 S）|
| T41 | delegation-protocol.md §6 補多輪迭代辯論 vs 單輪 gate-vote 取捨說明 + echo chamber 對照 diversity 提示 + 有裁判/無裁判兩種辯論拓撲區分 | 2305.14325,2402.06782 | .claude/refs/delegation-protocol.md | S | P1（單一萃取判斷，未過 3-lens gate-vote，待覆核）|
| T45 | memory-compactor.md 補 MemGPT in-context/out-of-context 雙層命名（out-of-context 再分 recall/archival），區分 evict（可復原）vs retire（不可逆），與既有歸檔機制/T8/T38 對齊不重工 | 2310.08560 | .claude/agents/memory-compactor.md | S | P1（單一萃取判斷，未過 3-lens gate-vote，待覆核；2026-07-27 ceiling 審計已修正三層→雙層錯誤）|
| T46 | delegation-protocol.md 分解 rubric 第 1 條（子任務獨立性，:77）補 LLMCompiler 式依賴分析方法論（列子任務所需輸入欄位→無依賴即標記可平行），操作化 `graph.md` §G1「畫邊前問」 | 2312.04511 | .claude/refs/delegation-protocol.md | S | P1（單一萃取判斷，未過 3-lens gate-vote，待覆核；2026-07-27 ceiling 審計勘誤：原文誤稱「delegation-protocol.md §G1」——該檔無此節，§G1 實位於 graph.md，已修正為分解 rubric 第 1 條的具體插入點）|
| T47 | loop.md §L4 補 oracle 能力上限子節：驗證者能力可能低於產出者時，納入產出者自身一致性/信心訊號作補充判準（`TODO(conflict)`，見 §4） | 2312.09390 | .claude/rules/loop.md | S | P1 ⚠（單一萃取判斷，未過 3-lens gate-vote，待覆核；2026-07-27 ceiling 審計新增：與 `loop.md` §L1 Verifier 分離／`graph.md` §G2「產出者不驗收自己的產出」有張力，已補 conflict 標記並移入 §4）|
| T42 | the-loop-best-solution.md §TEST 補 weakest-link 原則（長鏈任務品質取決最弱步驟） | 2305.20050 | .claude/refs/the-loop-best-solution.md | S | P1（單一萃取判斷，未過 3-lens gate-vote，待覆核）|
| T40 | fan-out aggregation gate 補趨同/搭便車警覺（弱優先，T12 已部分涵蓋） | 2308.10848 | .claude/refs/delegation-protocol.md | S | P2（單一萃取判斷，未過 3-lens gate-vote，待覆核）|
| T43 | refs/context-engineering-claude5.md 新增 NLAH 溯源段（規則本體在 L1 `context-management.md:8`，此檔僅補可溯源指標，不動 L1 零數字慣例） | 2307.03172 | .claude/refs/context-engineering-claude5.md | S | P2（單一萃取判斷，未過 3-lens gate-vote，待覆核；2026-07-27 ceiling 審計已修正目標檔誤植）|
| T48 | 評估 post-edit.sh 語法錯誤處理從 warn-only 升級為可選 block 模式（比照 SWE-agent ACI 之 reject-edit-with-diff），若與現行「fail loud 不阻斷」設計哲學衝突則標 `TODO(conflict)` | 2405.15793 | .claude/hooks/post-edit.sh | S | P2（單一萃取判斷，未過 3-lens gate-vote，待覆核）|
| T49 | memory-compactor.md Post-Prune 自驗補語意抽驗（隨機抽 N 條 Consolidate 判定，比對壓縮前後是否仍可推導出同一防範規則，補現行純計數比對之不足） | 2406.14275 | .claude/agents/memory-compactor.md | S | P2（單一萃取判斷，未過 3-lens gate-vote，待覆核）|
| T50 | `loop.md` §L1 或 `model-profiles.md` 效果不彰段落補 generation-side 軸：中難度任務可平行生成 N 候選 + 獨立 verifier 選優，明確與既有 `graph.md` §G2 verification-side 互斥視角區分開避免重工，落地前核對 §G3 fan-out 上限是否衝突 | 2408.03314 | .claude/rules/loop.md, .claude/refs/model-profiles.md | S | P2（單一萃取判斷，未過 3-lens gate-vote，待覆核；2026-07-28 ceiling 審計已修正「兩個旋鈕」低估既有 graph.md:29 三步序）|
| T51 | 前瞻性記錄：若/當採用 A2A peer-to-peer 拓撲，`delegation-protocol.md` 補 AgentPrune one-shot pruning 作 mesh 拓撲下 message-level 冗餘/惡意訊息防線候選（現行 star 拓撲不適用，非立即任務） | 2410.02506 | .claude/refs/delegation-protocol.md | S | P2（單一萃取判斷，未過 3-lens gate-vote，待覆核）|
| T52 | `output-compress/GOTCHAS.md` 補引用：標注本 SKILL 座落於 prompt-compression 分類法的 hard-prompt 陣營、soft-prompt 路線因 API-only 明確排除（純文件債） | 2410.12388 | .claude/skills/output-compress/GOTCHAS.md | S | P2 淘汰（單一萃取判斷，未過 3-lens gate-vote，待覆核）|
| T53 | `model-profiles.md` §7 補一行：若比照 TALE 對 `MAX_THINKING_TOKENS` 導入複雜度動態調整，estimate 步驟可下沉判斷、但注入值上限仍須確定性程序把關（避免與已擱置 T31 重工，低優先） | 2412.18547 | .claude/refs/model-profiles.md | S | P2 淘汰（單一萃取判斷，未過 3-lens gate-vote，待覆核）|
| T54 | 前瞻性記錄：評估以 RouteLLM win-prediction+α 概念設計四檔位間 pairwise router（現無可用偏好/正確率標註資料，非立即實作項，僅方法論參考） | 2406.18665 | .claude/refs/model-profiles.md | M | P2 淘汰（單一萃取判斷，未過 3-lens gate-vote，待覆核）|
| T55 | `refs/model-profiles.md` 補 difficulty-adaptive thinking budget 政策說明（任務初判失敗或屬高風險域時，記錄何時應建議調高 `MAX_THINKING_TOKENS`，純文件層級不做 gate） | 2501.19393 | .claude/refs/model-profiles.md | S | P2（單一萃取判斷，未過 3-lens gate-vote，待覆核）|
| T56 | memory-compactor.md 補新增 LESSON 時掃描既有條目、雙向加註交叉引用的輕量關聯標記子步驟（A-MEM 式即時連結，不做全動態表示重算） | 2502.12110 | .claude/agents/memory-compactor.md | M | P1（單一萃取判斷，未過 3-lens gate-vote，待覆核）|
| T57 | graph.md §G5（2026-07-29 ceiling 審計勘誤：目標章節原誤標 §G3，已修正）補「高連通拓撲在協作密集場景可能有效能優勢，但 workspace 高風險域仍優先低連通、採高連通須額外對抗複審」tradeoff 說明；delegation-protocol.md 分解 rubric 補里程碑式中途進度指標（補充 verify 節點量測維度，非取代終局 gate） | 2503.01935 | .claude/rules/graph.md, .claude/refs/delegation-protocol.md | S | P1（單一萃取判斷，未過 3-lens gate-vote，待覆核）|
| T58 | security-auditor.md 或 harness-audit-METRICS.md 補一條「問題價值表達 spot-check」條目（低頻危險價值類別對應任務模式，作為敏感域審查的被動監測補充） | 2504.15236 | .claude/agents/security-auditor.md, .claude/skills/harness-meta/references/harness-audit-METRICS.md | S | P1（單一萃取判斷，未過 3-lens gate-vote，待覆核）|
| T59 | T9 落地時補 Mem0/LOCOMO 式按查詢類型（單跳/多跳/時間/開放域）分類的簡化版準確率抽驗（現有 T9 只有整體命中率概念，缺分項評測範式） | 2504.19413 | .claude/skills/autoload-evolution/SKILL.md | S | P2（單一萃取判斷，未過 3-lens gate-vote，待覆核；補充既有 T9，非全新缺口）|
| T60 | memory-compactor.md AutoMode 補第四類「Update」（取代單筆過時事實但保留可追溯連結，區別於 Delete「完全捨棄」與 Consolidate「多筆合併」，避免 supersede 案例誤用 Delete 覆寫證據；⚠「保留可追溯連結」為 workspace 落地設計提案，非論文 2505.00675 原文主張，論文僅定義 Updating＝「修改反映新資訊」+ 原子性挑戰，見 §2.3） | 2505.00675 | .claude/agents/memory-compactor.md | S | P1（單一萃取判斷，未過 3-lens gate-vote，待覆核；與 core.md「不覆寫原始證據」有潛在張力，落地前核對）|
| T61 | ~~`refs/judgment-rubrics.md` 補「AskUserQuestion 應一次性批次問齊」指引~~ → `TODO(conflict)`，與 `.claude/skills/know-your-unknowns/SKILL.md:43`／`.claude/agents/multi-mode-agent.md:40` 既有「一次一題／一次只問 1–3 題」規則正面衝突，見 §4，不得直接落地 | 2505.06120 | .claude/refs/judgment-rubrics.md | S | `TODO(conflict)`（2026-07-29 ceiling 審計 + 主對話親驗發現與既有規則衝突，未過 3-lens gate-vote）|
| T62 | rules/security-hygiene.md 既有 Lethal Trifecta/tool-output-provenance（:66,:68）之下補「語意層注入偵測」缺口說明（現有 `unicode-covert-channel-guard.sh` 僅隱寫 Unicode 通道，非行為狀態偵測；InstructDetector 白盒方法因黑盒 API 限制不可直接移植，僅供未來輕量啟發式/第三方偵測 API 選型參考） | 2505.06311 | .claude/rules/security-hygiene.md | S | P1（單一萃取判斷，未過 3-lens gate-vote，待覆核；2026-07-30 ceiling 審計已收窄，原文低估既有覆蓋範圍）|
| T68 | delegation-protocol.md 補「交辦 prompt 負向約束密度應隨 child 檔位遞增而遞減」具體寫作提示 | 2510.22251 | .claude/refs/delegation-protocol.md | S | P1（單一萃取判斷，未過 3-lens gate-vote，待覆核）|
| T69 | model-profiles.md §2.2 補 cost 檔位 worker 輸出 token 爆增（>quality 檔位歷史均值 3×）仍需重試 → 升 quality 判準 | 2511.05722 | .claude/refs/model-profiles.md | S | P1（單一萃取判斷，未過 3-lens gate-vote，待覆核）|
| T63 | context-management.md 補「Deferred tool loading」對稱面——工具用畢/多輪對話不再相關時的淘汰機制（前瞻性，現行委派工具數遠低於論文 128 上限情境）⚠L1 常駐檔已達黃區（實測 23,825/27,000 門檻），落地時須等額刪除或改落 refs/ | 2507.21428 | .claude/rules/context-management.md | S | P2（單一萃取判斷，未過 3-lens gate-vote，待覆核；2026-07-30 ceiling 審計已補常駐 byte 註記）|
| T64 | harness-design.md「Rule → Hook 升格決策」矩陣補 Double-Check（決策點約束重注入）與 Tool Consolidation（多步驟封裝）機制詞彙 + τ-bench 10.1pp/66–82% 量化數字 | 2508.02721 | .claude/refs/harness-design.md | S | P2（單一萃取判斷，未過 3-lens gate-vote，待覆核）|
| T65 | delegation-protocol.md 補角色/任務階段感知 context 篩選設計參考（RCR-Router 三組件：budget allocator/importance scorer/semantic filter，前瞻性） | 2508.04903 | .claude/refs/delegation-protocol.md | S | P2（單一萃取判斷，未過 3-lens gate-vote，待覆核）|
| T66 | harness-audit-CHECKLIST.md 補「同一 ETCLOVG 層級依 worker 檔位預期不同失敗子型」子節（併入既有 T1，semantic-vs-syntax 分野量化依據） | 2509.16941 | .claude/skills/harness-meta/references/harness-audit-CHECKLIST.md | S | P2（單一萃取判斷，未過 3-lens gate-vote，待覆核）|
| T67 | context-management.md Compact 段補指向未來 T24（`refs/context-pruning-strategies.md`）的 contrastive guideline optimization 子類別指標（純文件債，區分 ACON 軌跡對比機制與既有 delta-hint/output-compress）⚠同 T63，L1 常駐檔黃區，須等額刪除或改落 refs/ | 2510.00615 | .claude/rules/context-management.md | S | P2（單一萃取判斷，未過 3-lens gate-vote，待覆核；2026-07-30 ceiling 審計已補常駐 byte 註記）|

---

## 4. 衝突與警示（TODO conflict — 不盲目實作）

> 浮現矛盾紀律（core.md 跨切）：以下任務論文證據強但與 workspace 既有紀律衝突，**明列交人類決策，不靜默選擇**。

- **T18（goal-drift 第五成功維度）**：`TODO(conflict)`：V2 接地強（goal-drift 量化證據充分），但 V1/V3 判 P2——`core.md` IDENTIFY「四維品質」是 canonical 鐵律，直接動它違反 Framework Integrity「修改 auto-load 前問移除後在哪犯錯」。**建議改採 T20**：把 goal-drift resistance 寫進 on-demand `refs/goal-engineering.md`，core.md 僅加 1 行指針，不擴 auto-load byte。
- **T34（PreToolUse 硬性 token gate exit2）**：`TODO(conflict)`：V3 強烈反對——違反 `context-management.md`「行為信號優先於數字閾值」+ Lesson（硬限制紅線）。**建議降級**：以軟性 warn（T30/T32 fail-open）取代硬 exit2，token budget 維持 advisory。
- **T15（handoff Return 補 credit_horizon/starting_artifact）**：`TODO(conflict)`：三票分歧（P2/P0/P1）——V2 認為 credit-assignment 論文機制強，V1 認投機性、V3 憂 handoff 膨脹。**建議**：先在 `autoload-evolution` 內部試行（記錄 starting_artifact），驗證有用再推廣到 handoff 契約。
- **T10（subagent confirmation gate）**：`TODO(conflict)`：V3 指出與 `subagent-strategy.md`「child 輸出只含結果、不加確認句」鐵律潛在衝突。**建議**：confirmation gate 設計為 *parent 端* 的 handoff 驗證（responsibility 歸屬），不是 child 端加確認句——釐清後可降衝突。
- **T38（LESSONS.md retirement/pruning 政策，2026-07-26 Routine D 批次新增）**：`TODO(conflict)`：ceiling 抽查（multi-mode-agent opus）發現 `.claude/agents/memory-compactor.md:82-98` 的 Post-Prune 自驗機械閘門把「壓縮後 Lesson 行數／待辦區塊減少」直接判 `FAIL`（目標檔為 `memory/MEMORY.md` 而非 `memory/LESSONS.md`，但同屬「不得靜默丟失高價值 anchor」的既有紅線，精神上仍構成張力）。SCM 式時間衰減/覆蓋率刪除決策若直接落地會與此 gate 衝突。**建議**：T38 落地前先明確「淘汰」與「刪除」的區別——標記 superseded/retired（保留原文、只改狀態欄，不減行數）可繞開 Post-Prune gate 且不違反「不覆寫原始證據」（core.md RECORD「記憶 episodic-first」），純物理刪除才需另走 `.claude/agents/memory-compactor.md` 的顯式核可流程。
- **T47（loop.md §L4 補 oracle 能力上限子節，2026-07-27 Routine D 第二批次新增）**：`TODO(conflict)`：ceiling 抽查（multi-mode-agent opus）指出「納入產出者自身一致性/信心訊號作補充判準」與 `loop.md:14` §L1「Verifier 必為與 writer 不同的 instance，只看產物與 oracle」、`graph.md:28`「產出者不驗收自己的產出」兩條既有紅線正面衝突——若落地不慎會讓 verifier 部分採信 writer 自陳的信心分數，等同開一道「產出者為自己背書」的後門。**建議**：Weak-to-Strong 論文的 confidence loss 是**訓練期**輔助訊號（用於微調弱監督下的強模型），不是**推論期驗證**判準；T47 落地時應限定範圍為「訓練/微調場景下的 auxiliary signal」，明確排除「verifier 對已完成任務的驗收判斷可參考 writer 信心」這一讀法，避免與 §L1/§G2 產生實質衝突。
- **T61（judgment-rubrics.md 補一次性批次問齊 Known Unknowns 指引，2026-07-29 Routine D 批次新增）**：`TODO(conflict)`：ceiling 抽查（multi-mode-agent opus）+ 主對話親跑 grep 覆核發現，LLMs-Get-Lost-Multi-Turn（2505.06120）「一次性給齊全部資訊是唯一有效緩解多輪不可靠性放大的方法」的建議，與 `.claude/skills/know-your-unknowns/SKILL.md:43`（T6 The Interview）「一次一題訪談模糊需求…一次只問最貴的 1–3 題，其餘等答案收斂後再問，避免一次倒 10 題稀釋回答品質」、`.claude/agents/multi-mode-agent.md:40`「Known Unknowns→Interview 一次一題」兩處既有明文規則**方向正面相反**——論文站在「減少多輪不可靠性」，既有規則站在「避免一次倒多題稀釋回答品質＋按架構爆炸半徑排序」，若直接落地會 silent fork 既有規則。**建議**：不直接修改 `judgment-rubrics.md`，落地前需人類判斷兩者適用邊界（例如：論文情境是模型單方逐輪自行猜測補全 spec 導致漂移，既有規則情境是主動向使用者提問時的認知負擔管理，兩者的「輪」語意可能不同層次，須先釐清是否真構成同一問題的兩種解法再決定是否需要調和）。

---

## 5. 建議執行順序

論文證據 + 共識收斂出一條 **「先建 eval 地基，再談自我演化」** 的路徑：

**批次 1（P0 · 自我演化安全閘，全 S/M，低風險）**
→ T28（block 自動寫 skills 守 self-generated drift）→ T4（falsifiable prediction）→ T23（eval-driven regression）→ T7（LESSONS provenance）→ T22（verification gate 量化）。
這 5 條都是「在既有 autoload-evolution / LESSONS / the-loop-best-solution 上補欄位/章節」，不新建系統、不動 canonical 鐵律。

**批次 2（P0 · eval 地基 + 協調閘）**
→ T5（coreset.md，自我演化的回歸基準）→ T2（seesaw 回歸 checklist）→ T9（observe retrieve LESSONS）→ T12（fan-out aggregation gate）→ T13（self-escalate 主動 stop）→ T27（skill empirical gate）→ T36（session-stop PGE gate 補強）。

**批次 3（P1 · 觀測 + context 操作化）**
→ T3（trace stub）→ T33（cache-health 監控）→ T35（remaining context %）→ T24（context-pruning 策略）→ T30/T32（token-budget 軟 gate）。

**先不做**：批次 4 的 P2/conflict 任務待人類就第 4 節衝突決策後再啟。

---

## 附錄 A：論文索引（arxiv_id → 維度）

| arxiv_id | 短名 | 主要支撐維度 |
|----------|------|------------|
| 2606.14249 | HarnessX/AEGIS | harness, self-improve |
| 2606.10106 | what-makes-harness | harness |
| 2606.06324 | HarnessFix/ETCLOVG | harness, self-improve |
| 2604.20938 | Harbor | harness |
| 2606.20683 | survey-QA→Task | harness, rules |
| 2606.15874 | LLM-as-Code | harness, rules, loop |
| 2606.09498 | Self-Harness | self-improve |
| 2606.05922 | RHO | self-improve |
| 2605.27276 | SIA | self-improve |
| 2604.25850 | AHE | self-improve, self-learn |
| 2603.28052 | Meta-Harness | self-improve |
| 2509.25140 | ReasoningBank | self-learn |
| 2504.07952 | Dynamic-Cheatsheet | self-learn |
| 2510.16079 | EvolveR | self-learn, loop |
| 2606.21005 | Beaver | self-learn |
| 2510.04618 | ACE | self-learn |
| 2503.13657 | MAST | agents, workflow |
| 2605.03310 | coordination-arch | agents |
| 2505.13516 | HALO | agents |
| 2509.23537 | multi-turn-vs-single | sub-agent |
| 2605.02801 | RL-orchestration-traces | sub-agent, loop |
| 2602.16873 | AdaptOrch | sub-agent |
| 2604.00901 | HERA | sub-agent, loop |
| 2603.22386 | workflow-opt-survey | workflow |
| 2505.18646 | SEW | workflow |
| 2603.23994 | challenges-iterative | workflow, loop |
| 2603.25928 | self-organizing-MAS | workflow |
| 2509.14647 | AgentCompass | workflow |
| 2604.11378 | agent-loops-to-graphs | loop |
| 2604.22136 | sovereign-loops | loop |
| 2601.13671 | orchestration-survey | loop |
| 2505.02709 | eval-goal-drift | goals |
| 2603.03258 | inherited-drift | goals |
| 2603.03456 | asymmetric-drift | goals |
| 2603.19685 | subgoal-driven | goals |
| 2605.06957 | policy-decompositions | goals |
| 2606.21856 | Harness-MU | rules, hooks |
| 2606.23983 | Maestro-Order | rules |
| 2601.22025 | when-better-prompts-hurt | rules |
| 2507.13334 | context-eng-survey | refs |
| 2509.21361 | max-effective-context | refs |
| 2606.10209 | less-context-better-agents | refs |
| 2602.14690 | configuring-agentic-tools | skills, commands |
| 2602.12670 | skills-bench | skills |
| 2605.02396 | heavyskill | skills |
| 2604.14228 | dive-into-claude-code | commands, hooks |
| 2606.04056 | token-budgets-overrun | commands, hooks |
| 2605.07686 | coupling-tax | commands |
| 2606.23449 | AOHP | hooks |
| 2601.06007 | dont-break-cache | hooks |
| 2602.22402 | contextual-memory-virtualisation | hooks |
| 2601.07190 | active-context-compression | hooks |
| 2605.12357 | delta-mem | hooks |
| 2005.11401 | RAG | refs, self-learn |
| 2109.10086 | SPLADE-v2 | refs（弱關聯，IR 技術參考）|
| 2202.03286 | red-teaming-LMs | rules, hooks |
| 2204.14198 | Flamingo | （弱關聯，corpus 記錄）|
| 2209.10652 | toy-superposition | （弱關聯，corpus 記錄）|
| 2210.03629 | ReAct | agents, loop |
| 2212.08073 | Constitutional-AI | rules, self-improve |
| 2301.12597 | BLIP-2 | （弱關聯，corpus 記錄）|
| 2303.11366 | Reflexion | self-improve, self-learn |
| 2304.03442 | Generative-Agents | self-learn, agents |
| 2304.08485 | LLaVA | （弱關聯，corpus 記錄）|
| 2304.13343 | SCM | self-learn, rules |
| 2305.10250 | MemoryBank | self-learn |
| 2305.14325 | Multiagent-Debate | agents, workflow |
| 2305.16291 | Voyager | skills, self-improve |
| 2305.20050 | Let's-Verify-PRM | loop, self-improve |
| 2307.03172 | Lost-in-the-Middle | refs |
| 2307.07924 | ChatDev | workflow, agents |
| 2307.15043 | GCG-Adversarial | rules, hooks（與 2202.03286 重疊） |
| 2308.00352 | MetaGPT | agents, workflow |
| 2308.08155 | AutoGen | agents, loop |
| 2308.10144 | ExpeL | self-learn |
| 2308.10848 | AgentVerse | agents |
| 2309.00267 | RLAIF-vs-RLHF | self-improve |
| 2309.02427 | CoALA | self-learn, agents |
| 2310.03744 | LLaVA-1.5 | （弱關聯，corpus 記錄）|
| 2310.08560 | MemGPT | self-learn, refs |
| 2310.16834 | SEDD | （弱關聯，corpus 記錄）|
| 2312.04511 | LLMCompiler | loop, agents |
| 2312.09390 | Weak-to-Strong | loop, rules |
| 2312.10997 | RAG-Survey | refs, self-learn |
| 2402.04249 | HarmBench | rules, hooks |
| 2402.06782 | Persuasive-Debate | agents, workflow |
| 2404.13501 | Memory-Mechanism-Survey | self-learn |
| 2405.11120 | Latent-State-UI | harness, agents |
| 2405.14831 | HippoRAG | self-learn, refs |
| 2405.15793 | SWE-agent | harness, hooks |
| 2406.07524 | MDLM | （弱關聯，corpus 記錄）|
| 2406.14275 | Step-Back Profiling | self-learn |
| 2406.18510 | WildTeaming | rules |
| 2406.18665 | RouteLLM | agents |
| 2408.03314 | Scaling-Test-Time-Compute | loop |
| 2410.02506 | AgentPrune | agents |
| 2410.12388 | Prompt-Compression-Survey | refs, skills |
| 2410.14157 | MGDM | （弱關聯，corpus 記錄）|
| 2412.18547 | TALE（Token-Budget-Aware） | commands, refs |
| 2501.07391 | RAG-Best-Practices | self-learn, refs |
| 2501.12948 | DeepSeek-R1 | self-improve（訓練範式類比，弱接地）|
| 2501.19393 | s1 (budget forcing) | loop |
| 2502.09992 | LLaDA | （弱關聯，corpus 記錄）|
| 2502.12110 | A-MEM | self-learn |
| 2502.15524 | HydraServe | （弱關聯，corpus 記錄）|
| 2503.01935 | MultiAgentBench | agents |
| 2503.04761 | Which-Economic-Tasks | （弱關聯，corpus 記錄）|
| 2503.19114 | Info-Preservation-Prompt-Compression | refs |
| 2504.15236 | Values-in-the-Wild | rules |
| 2504.15965 | Human-Memory-to-AI-Memory-Survey | self-learn |
| 2504.19413 | Mem0 | self-learn |
| 2505.00675 | Rethinking-Memory-LLM-Agents-Ops | self-learn |
| 2505.06120 | LLMs-Get-Lost-Multi-Turn | loop, rules |
| 2505.06311 | InstructDetect | rules, hooks |
| 2506.02951 | AGP | agents（弱關聯，訓練式拓樸剪枝方法論參照）|
| 2506.07142 | PromptSci2 | loop（弱關聯，prompting 建議非架構主張）|
| 2507.21428 | MemTool | harness, refs |
| 2508.02721 | BlueprintFirst | harness, workflow |
| 2508.04903 | RCR-Router | agents, refs |
| 2508.17196 | BudgetThinker | commands（弱關聯，訓練側方法不落地）|
| 2509.16941 | SWEBP | harness, agents |
| 2510.00615 | ACON | refs, self-learn |
| 2510.22251 | Sculpt | rules, harness |
| 2511.05722 | OckBench | hooks, refs |
| 2511.15080 | AEIReport | （弱關聯，corpus 記錄）|

## 附錄 B：gate-vote 投票矩陣（節錄 P0 + 衝突項）

| Task | V1 影響×可行 | V2 接地 | V3 契合 | 共識 |
|------|----|----|----|------|
| T4 | P0 | P0 | P0 | P0 ⭐ |
| T7 | P0 | P0 | P0 | P0 ⭐ |
| T23 | P0 | P0 | P0 | P0 ⭐ |
| T2 | P0 | P1 | P0 | P0 |
| T5 | P0 | P0 | P1 | P0 |
| T9 | P0 | P0 | P1 | P0 |
| T12 | P0 | P1 | P0 | P0 |
| T13 | P1 | P0 | P0 | P0 |
| T22 | P2 | P0 | P0 | P0 |
| T27 | P0 | P0 | P1 | P0 |
| T28 | P0 | P0 | P1 | P0 |
| T36 | P1 | P0 | P0 | P0 |
| T15 | P2 | P0 | P1 | 無共識 ⚠ |
| T18 | P2 | P0 | P2 | P2 ⚠ |
| T34 | P1 | P0 | P2 | 無共識 ⚠ |
| T10 | P1 | P1 | P2 | P1 ⚠ |

> TOP5 跨 lens 提名：T5/T12/T22 各 2 票 + 三票全 P0 的 T4/T7/T23 = 最高信心起手式。

---

## 6. 審計後勘誤（multi-mode 深度查核 · 2026-06-24）

經 `/multi-mode-skill` 路由 3 個 `multi-mode-agent [mode: ceiling]`（opus）對本報告做 3 軸獨立查核（接地正確性 / Gap 真實性 / 任務健全性）。**主對話親跑 ground-truth grep 覆核 subagent 結論**（unverified_success 閘門），結果：

- **axis-2（Gap 真實性，worktree-aware）抓到 3 處真瑕疵，已勘誤**：
  1. agents 維度「14 全固定角色」→ 實為 **13 個**且 `multi-mode-agent` 為動態 mode/role 注入（已修 §2.4）。
  2. T28 把 self-generated-skill 風險歸因 `autoresearch:learn`（learn 輸出 `docs/`、已排除 `.claude`）→ 改為 autoresearch 整體 guardrail 框架（已修 §2.10）。
  3. T33 cache-health「完全無監控」→ 已有 `session-init.sh` 月度聚合，收窄為「無 per-tool-call 即時 hook」（已修 §2.12）。
- **axis-1（BLOCKED）/ axis-3（判 FAIL）結論駁回**：兩 agent 跑在 stale worktree `b4caaf9`，誤報「報告檔 / `LESSONS.md` / `the-loop-best-solution.md` 不存在」。主對話查證：三者**皆存在**（report 24655 bytes；`memory/LESSONS.md` 存在；`core.md:91` 引用 `the-loop-best-solution.md`）。**故 T7/T9/T22 路徑正確，無需改**。
- **harness gotcha（已記入 LESSONS）**：spawn 的 sub-agent 可能對到 stale worktree base，凡涉「檔案是否存在」的 verdict **必由主對話在主 tree 親驗**，不採信 sub-agent 單方結論。

> 淨結果：核心結論（兩大缺口 + 12 P0 + 4 conflict）**經查核維持成立**；修正集中在 3 處措辭/數字精度，未動主結構。

---

### 6.1 審計後勘誤（Routine D 2026-07-27 批次 · 12 篇新論文）

`multi-mode-agent [mode: ceiling]`（opus）對本批次新增段落（T39-T44、附錄 A 12 行、§2.2/2.3/2.4/2.5/2.6/2.8/2.9/2.10 對應 F/G/T）做 3 軸查核，**同樣先發現 stale worktree 歧異**（agent 誤判到 `5c88f5b` 舊 worktree，該處無 `graph.md`/`loop.md`、報告缺本批次全部新增），主對話以主 tree 絕對路徑為 ground truth，**逐項親跑 grep/read 覆核**（不採信 sub-agent 單方 verdict），結果：

- **接地正確性**：12 篇論文的量化數據/技術主張全數核對無編造，唯 2 處歸因瑕疵已修：
  1. 2309.00267（RLAIF）：原文誤植「作者自陳警示...為 §L4 提供 peer-reviewed 實證佐證」→ 親驗 `2023-09-01-rlaif-...md:72` 確認該句位於「Limitations & Future Work」段、且用第三人稱描述論文**未處理**的風險（非作者自陳），論文核心結論方向其實相反（同能力 labeler 訓練訊號有效）→ 已修正歸因，降級為「提醒性引用」而非「實證佐證」（已修 §2.2）。
  2. 2305.14325（Multiagent Debate）：原文誤植「作者明確警示 echo chamber」→ 親驗 `2023-05-23-multiagent-debate-...md:47` 確認 echo chamber 一詞出自歸檔者「對 agent-team 設計的啟示」推導段，非論文「原文關鍵引用」段 → 已修正為「歸檔分析指出」（已修 §2.4）。
- **Gap 真實性**：T39/T42 兩條核心 Gap 親驗成立（`grep -n "深度上限" graph.md` 0 命中；`grep -n "weakest\|最弱" the-loop-best-solution.md` 0 命中）。2 條需收窄：
  3. T43：原 Gap 誤稱 `context-engineering-claude5.md` 為 NLAH 規則本體所在檔 → 親驗 `grep NLAH .claude/rules/context-management.md` 命中於 `:8`、同一 grep 對 `context-engineering-claude5.md` **0 命中** → 已修正 Gap 描述 + Task 目標，改為「refs 檔補溯源指標，L1 本體不動」（已修 §2.9、§3）。
  4. T44：原 Gap 誤稱 Handoff Contract 完全無不確定性標記機制 → 親驗 `graph.md:41` 已有 `open_questions`、`multi-mode-agent.md:53` 已有 `[claim:verified]/[claim:asserted]/[claim:judgment]` 三級標記 → 已收窄 Gap 為「僅缺下游主動追問迴圈」，Task 規模由 M 降為 S（已修 §2.5、§3）。
- **任務健全性**：T39-T44 影響檔案路徑全數親驗存在（`ls` 逐一確認 4 個相異路徑）。**批次外連帶發現**：親驗 `the-loop-best-solution.md:141` 確認 T22（verification gate 量化模型 0.55→0.999）**已落地**、內容逐字對應既有任務描述，但 §3 表仍將其列為待辦 **P0** → 已更正狀態為「已完成」，避免後續批次重工（已修 §3）。
- **harness gotcha（再次發生，已追加記入 LESSONS）**：同一「sub-agent 對到 stale worktree」故障模式第二次出現（6.0 節已記錄過一次）；本次額外確認故障不影響 ceiling 審計的分析品質本身（12 篇接地核對、4 條 Gap 真偽判斷皆準確），僅影響其「檔案存在性」相關前提陳述——**分析結論可信、存在性斷言不可信**是此類 stale-worktree 故障的一致模式，佐證既有 core.md「涉檔案存在性的 sub-agent 結論一律主 tree 親驗」條文已是正確設計，非本次新增缺口。

> 淨結果：本批次 12 篇論文的接地與新增 6 條任務（T39-T44）**核心判斷經查核維持成立**；2 處論文歸因錯誤已修正措辭，2 條 Gap 已收窄至機械驗證過的實際範圍，1 條批次外舊任務（T22）狀態已更正。SIA 量化閘複跑仍通過（見附錄 C）。

---

### 6.2 審計後勘誤（Routine D 2026-07-27 第二批次 · 12 篇新論文）

`multi-mode-agent [mode: ceiling]`（opus）對本批次新增段落（T45-T47、附錄 A 12 行、§2.1/2.3/2.4/2.6/2.8/2.9 對應 F/G/T、弱關聯備註 2 篇）做 3 軸查核。**第三次出現同一「sub-agent 對到 stale worktree」故障模式**（agent 明確自報 worktree 副本 31116 bytes / `grep -c T45` = 0，主動改用主 tree 絕對路徑驗證，未誤判存在性），主對話對其**每一項**結論**逐條重新親跑 grep/read 交叉驗證**（不因 sub-agent 已自我規避 stale-worktree 就降低覆核強度），結果：

- **接地正確性（axis-1）**：12 篇論文的 6 項量化數據（MemGPT 92.5%/32.1%、LLMCompiler 3.7x/6.7x/~9%、HippoRAG +10.4pp/6-13×/10-30×、HarmBench 18×33/>90% ASR、Persuasive-Debate 48→76%/60→88%、Latent-State-UI 28.1→45.9%）主對話逐一 grep 原文核對**全部無誤**。**3 處歸因瑕疵確認並已修**：
  1. 2312.10997（RAG-Survey）：原文誤稱 RAGAS/ARES/TruLens 為 survey「獨立貢獻」→ 親驗 `research/papers/2023-12-18-...md:256-262` 確認三者為該 survey「評估工具」章節整理的**第三方**框架（RAGAS 出自其參考文獻 `:345` Es et al. 2023）→ 已修正歸因（已修 §2.9）。
  2. 2310.08560（MemGPT）：原文 F 段稱「兩層」但 G 段與 T45 稱「working/recall/archival 三層模型」，內部自相矛盾 → 親驗 `research/papers/2023-10-12-...md:55` 確認論文原文明寫「two-tier memory architecture」，「三層」用語出自**另一篇** HippoRAG 對照表（`2024-05-23-hipporag-...md:139`）對 MemGPT 的外部概括，非 MemGPT 自述 → 已統一改為「in-context/out-of-context 雙層」並消除矛盾（已修 §2.3、§3 T45）。
  3. 2404.13501（Memory-Mechanism-Survey）：原文誤稱「記憶整合是效能退化主因」為 survey 自身強斷言 → 親驗 `research/papers/2024-04-21-...md:80,127-128` 確認該句在原文標「⚠️ 警告（來自 2605.12978）」，survey 自身「發現 2」措辭較保守（「後來經該篇系統性驗證」）→ 已修正歸因（已修 §2.3）。
- **Gap 真實性（axis-2）**：T46/T47 兩條核心 Gap 親驗成立（`grep -n "LLMCompiler\|依賴分析" .claude/refs/delegation-protocol.md` 0 命中；`grep -n "能力上限\|imitation gap" .claude/rules/loop.md` 0 命中）。**1 條 Gap 部分不實已修**：
  4. T45：原 Gap 稱「現行 memory-compactor 僅做壓縮 delta+dedup」→ 親驗 `.claude/agents/memory-compactor.md:32-98` 確認實際機制是 AutoMode（Retain/Delete/Consolidate）+ Conflict Gate + Post-Prune 自驗，「delta+dedup」實為 T8（尚未落地）的提案內容、非現況；且該檔 `:64-73` 已有「舊 session 移至 archive、主檔留指標」的可復原歸檔機制，功能上已具備 evict 雛形 → 已修正 Gap 描述避免 T45 落地時誤判基準線與 T8 重工（已修 §2.3、§3）。
- **任務健全性（axis-3）**：T45-T47 影響檔案路徑全數親驗存在（`ls` 逐一確認 3 個路徑）。**2 處已修**：
  5. T46：原文誤稱目標為「delegation-protocol.md §G1」→ 親驗 `grep -c "§G1" .claude/refs/delegation-protocol.md` = 0、`grep -n "^## G1" .claude/rules/graph.md` 命中於 `:12` → §G1 實屬 graph.md，delegation-protocol.md 無此節 → 已修正 T46 目標為該檔分解 rubric 第 1 條（子任務獨立性，`:77`）這一具體插入點（已修 §3）。
  6. T47：原文未標記與既有紅線的衝突，親驗 `loop.md:14`「Verifier 必為與 writer 不同的 instance」+ `graph.md:28`「產出者不驗收自己的產出」確認 T47「納入產出者自身信心訊號」構想與兩條既有鐵律有實質張力，且未列入 §4 → 已補 `TODO(conflict)` 標記並移入 §4，限定適用範圍為訓練期輔助訊號而非推論期驗收判準（已修 §3、§4）。
- **advisory（不構成缺陷，記錄供下批對照）**：Latent-State-UI「首次」量化證據一詞不可機械驗證且構念上（UI 環境狀態 vs agent 執行期狀態）略有落差；Persuasive-Debate「並未降低」真實性辨識準確度其實是低估（原文為 improves）——方向正確、幅度保守，非錯誤；附錄 A 多維度論文只在主要維度出現文字段落，經控制組核對（2308.08155、2305.20050）**為報告既有慣例非本批新缺陷**。
- **harness gotcha（第三次發生，已追加記入 LESSONS）**：同一「sub-agent 對到 stale worktree」故障模式第三次出現，本次 sub-agent 已自我偵測並規避（主動聲明 worktree base + 改走主 tree 絕對路徑），**分析結論本身仍可信**；但本次額外教訓是——**即便 sub-agent 自陳已規避 stale-worktree，其實質性判斷（接地/Gap/任務健全性）仍須主對話逐條重驗，不可因「worktree 聲明正確」而放寬對內容本身的覆核強度**（本輪揪出的 6 處瑕疵中，5 處與 worktree 無關，純屬論文歸因/內部矛盾/章節路徑錯誤）。

> 淨結果：本批次 12 篇論文的接地與新增 3 條任務（T45-T47）**核心判斷經查核部分成立、6 處實質瑕疵已修正**（3 處論文歸因、1 處 Gap 基準錯誤、1 處目標章節路徑錯誤、1 處遺漏 conflict 標記）；此為三批連續審計中瑕疵密度最高的一次（6/12 vs 前次 4/12），佐證「多引用他篇論文/多層架構類比」的段落歸因風險高於單篇論文直述數字，後續批次萃取時對此類段落應加強一次自我複核再送審。SIA 量化閘複跑仍通過（見附錄 C）。

### 6.3 審計後勘誤（Routine D 2026-07-28 批次 · 12 篇新論文）

`multi-mode-agent [mode: ceiling]`（opus）對本批次新增段落（T48-T54、附錄 A 12 行、§2.1/2.2/2.3/2.4/2.6/2.8/2.9/2.11/弱關聯備註對應 F/G/T）做 5 軸查核（A 接地正確性／B 無過度延伸／C 無捏造 workspace 現況／D 附錄 A 維度標記／E 無重複矛盾）。主對話對其**每一項** FAIL 結論逐條重新親跑 grep/read 交叉驗證，**3 項實質瑕疵全數確認並已修**：

1. **§2.6 loop G/T50「只有升 effort 或升檔位兩個旋鈕」低估既有機制**：親驗 `graph.md:23,29` 確認既有規則已明文「先加互斥視角 → 再升 effort → 最後才升檔位」三步序，非只有兩個旋鈕 → 已修正 Gap 措辭，並把 T50 明確限定在 generation-side（平行生成 N 候選+獨立 verifier 選優），與 §G2 verification-side（驗證者視角多樣性）區分開，避免落地時與既有規則重工（已修 §2.6、§3 T50）。
2. **§2.9 refs F（2410.12388）歸因瑕疵**：原文寫「論文明確指出 soft prompt…API-only 適用性弱」，親驗 `research/papers/2024-10-16-prompt-compression-survey-2410-12388.md:49` 該句與同段落「2024-10 成稿，未涵蓋其後研究線」（明顯是歸檔者評語）並列於「限制」區塊，本環境 PDF 抽取管道不可用（`pypdf` 依賴缺失），無法回溯論文原文確認歸屬 → 已改為「歸檔摘要另記…疑似歸檔者評估」的保守措辭，不再歸為論文明確主張（已修 §2.9）。
3. **§2.11 commands F/G（2412.18547）方法變體名稱與機制細節未接地**：原文寫「TALE-EP 以 zero-shot 提示先估算」，親驗 `research/papers/2024-12-24-token-budget-aware-llm-reasoning-2412-18547.md` 全文 57 行**無 "TALE-EP"、無 "zero-shot"** 字樣，且該檔「關鍵結果」區塊已自陳「具體百分比未取得（abstract 未含）」→ 已刪除未接地的方法變體名稱與估算機制描述，改為只陳述該檔「結構化摘要」明文的框架描述（依複雜度動態估算並注入 budget），並移除懸空的「見 §6 待補」交叉引用（已修 §2.11、§3 T53 描述不變，本身已用「TALE」未用「TALE-EP」）。

**advisory（不構成缺陷，記錄供下批對照）**：AgentPrune（2410.02506）的 4 項量化數字雖未見於本 repo 歸檔摘要截斷段落，但主對話親跑 `curl https://export.arxiv.org/api/query?id_list=2410.02506` 取官方摘要逐字核實成立，屬既有歸檔缺漏（截斷）而非引用錯誤，不需修正內文，僅供下批對照「歸檔摘要截斷」這一獨立於「歸因錯置」的失敗類別；T51/T54 同為前瞻性任務但共識分級不同（P2 vs P2 淘汰），優先序差異未附理由，列為觀察項不強制修正。

> 淨結果：本批次 12 篇論文新增 7 條任務（T48-T54）**核心判斷經查核部分成立、3 處實質瑕疵已修正**（1 處低估既有機制、2 處論文歸因/接地瑕疵）；瑕疵密度 3/12，低於前兩批（4/12、6/12），連續三批瑕疵集中在同一失敗類別——「歸檔者評語/第三方轉述 vs 論文原文直述」的歸屬判斷與「workspace 既有機制覆蓋範圍」的低估，量化數字本身除待證的 2 項外均無錯誤。SIA 量化閘複跑仍通過（見附錄 C，複跑於本次修正後執行）。

### 6.4 審計後勘誤（Routine D 2026-07-29 批次 · 12 篇新論文）

`multi-mode-agent [mode: ceiling]`（opus）對本批次新增段落（T55-T61、附錄 A 12 行、§2.3/2.4/2.6/2.8/2.9/弱關聯備註對應 F/G/T）做 A/B/C 三軸查核。**第四次出現「sub-agent 對到 stale worktree」故障模式**（agent 自報 shared checkout 99,906 bytes vs worktree 副本 87,124 bytes，主動聲明並改用絕對路徑重跑），主對話對其 FAIL 結論逐條重新親跑 grep/read 交叉驗證，**3 項實質瑕疵確認並已修**：

1. **§2.3 self-learn G/T60（2505.00675）論文歸因過度延伸**：原文把「保留舊→新可追溯連結」寫成 Rethinking-Memory-Ops 論文對 Updating 操作的定義一部分，親驗 `research/papers/2025-05-01-rethinking-memory-llm-agents-operations-2505-00675.md:74-84` 確認論文原文僅定義 Updating＝「修改現有記憶以反映新資訊」+ 挑戰為「更新的原子性（避免自相矛盾）」，**全文無「可追溯連結」用語**——該詞是 workspace 落地時的設計提案，非論文主張 → 已修正歸因，明確標記為設計提案（已修 §2.3、§3 T60）。
2. **T57 目標章節座標錯誤**：原文寫「graph.md §G3 補…tradeoff 說明」，親驗 `grep -n "^## G" .claude/rules/graph.md` 確認「高連通拓撲擴大污染半徑」一句實位於 **§G5:50**（委派安全與採信紀律），非 §G3（Fan-out 上限與速率閘）→ 已修正 T57 目標章節，並**一併修正前批次（2026-07-28 批次 AgentPrune 2410.02506）繼承的同一錯誤**（§2.4 G 段原文亦誤標 §G3，已改標 §G5）（已修 §2.4、§3 T57）。
3. **T61（judgment-rubrics.md 補一次性批次問齊指引）與既有規則正面衝突未標記**：原文將 LLMs-Get-Lost-Multi-Turn（2505.06120）「一次性給齊全部資訊」建議直接寫成待落地 Gap/Task，親驗 `.claude/skills/know-your-unknowns/SKILL.md:43`（T6 The Interview）「一次一題…一次只問最貴的 1–3 題，避免一次倒 10 題稀釋回答品質」與 `.claude/agents/multi-mode-agent.md:40`「Known Unknowns→Interview 一次一題」確認兩處既有明文規則方向與論文建議**正面相反** → 已改列 `TODO(conflict)` 移入 §4，不得靜默落地覆寫既有規則（已修 §2.6、§3 T61、§4）。

**advisory（不構成缺陷，記錄供下批對照）**：HydraServe（2502.15524）歸檔摘要自帶「對 cc-workspace 的遷移啟示」段落（SessionStart hook async 化類比），報告判定弱關聯時未提及此段——判斷本身成立（該段屬歸檔者外推非論文主張），但屬未言明的取捨，非本次新增缺陷；Which-Economic-Tasks（2503.04761）歸檔檔本身存在內部數字矛盾（abstract 寫 4+ million、Methodology 寫 1 million），報告採 abstract 數字為既有歸檔缺陷之繼承，非本次引用錯誤，建議下批對照時回頭修歸檔檔本身。

**harness gotcha（第四次發生，已知模式持續生效）**：同一「sub-agent 對到 stale worktree」故障模式第四次出現，本次 sub-agent 已在回覆開頭主動聲明並自行改走絕對路徑重跑，**分析結論本身可信**；本批次 3 處瑕疵中 2 處（T60 歸因、T61 衝突遺漏）與 worktree 無關，純屬論文歸因過度延伸與跨規則衝突偵測疏漏，1 處（T57）屬既有章節編號沿用前一批次的舊錯誤——三種失敗類別皆與既有 core.md「sub-agent 涉檔案存在性結論一律主 tree 親驗」條文設計方向一致，佐證該紅線持續有效，非新增缺口。

> 淨結果：本批次 12 篇論文的接地與新增 7 條任務（T55-T61）**核心判斷經查核部分成立、3 處實質瑕疵已修正**（1 處論文歸因過度延伸、1 處章節座標錯誤且波及前批次同型錯誤、1 處跨規則衝突未標記）；瑕疵密度 3/12，與 2026-07-28 批次持平，累計四批瑕疵類型持續集中在「論文原文 vs 歸檔者/落地提案混淆」與「新提案與既有規則的衝突偵測」兩類，量化數字本身 12 篇皆無錯誤。SIA 量化閘複跑仍通過（見附錄 C，複跑於本次修正後執行）。

### 6.5 審計後勘誤（Routine D 2026-07-30 批次 · 12 篇新論文）

`multi-mode-agent [mode: ceiling]`（opus）對本批次新增段落（T62-T69、附錄 A 12 行、§2.1/2.4/2.8/2.9/弱關聯備註對應 F/G/T）做 A/B/C 三軸查核。**第五次出現「sub-agent 對到 stale worktree」故障模式**（agent 自報報告檔 118325 bytes vs worktree 副本 31116 bytes、`grep -c "T6[2-9]"` 主 tree 13 vs worktree 0，主動聲明並改用主 tree 絕對路徑重跑；`memory/LESSONS.md:48,134` 已記錄此為同簽名第 2 例並依 core.md「同簽名重現 ≥2 次才改規則」升格入 RATCHET，本次為第五次重現，屬已知持續生效模式非新缺口），主對話對其 4 處 FAIL/誇大結論**逐條重新親跑 grep/read 交叉驗證**，全數確認成立並已修：

1. **§2.8 InstructDetect Gap 數字與範圍雙重錯誤**：原文寫「24 支 hook 皆不含 IPI 偵測邏輯」，親驗 `ls .claude/hooks/*.sh | wc -l` 與 `grep -oE "[a-z-]+\.sh" .claude/settings.json | sort -u | wc -l` 兩路獨立核算皆為 **26**（非 24）；且 `unicode-covert-channel-guard.sh` 確實是一支作用於 IPI 攻擊面（PostToolUse 掃 WebFetch/WebSearch/`mcp__github__issue_read` 等外部輸出）的確定性偵測閘門，僅因原 grep 關鍵字（`injection|untrusted`）選詞不含該 hook 用語（「隱寫/covert-channel」）造成 0 命中假象；`security-hygiene.md:66,68` 亦已有 Lethal Trifecta／tool-output-provenance 信任分級專節 → 已修正數字、收窄 Gap 描述為「僅一支窄面偵測閘門、無語意層注入偵測」，並同步收窄 T62 落地範圍避免與既有機制重工（已修 §2.8、§3 T62）。
2. **§2.12 PromptSci2 弱關聯備註方向失準**：原文寫「non-reasoning 模型中 3/5 模型 CoT 反而降低正確率」，親驗 `research/papers/2025-06-08-decreasing-value-chain-of-thought-2506-07142.md:98-110` 原表確認 **Average RD 5/5 模型皆為正**（+0.044~+0.135），僅 **100% Correct（一致性）指標 3/5 模型為負**（−0.091~−0.172）——論文原意是「CoT 用一致性換平均分」而非全面降低正確率，方向被壓縮後反轉 → 已修正並補回 Average 全升的對照（已修 §2.12）。
3. **§2.1 SWEBP Gap grep 附註低估命中範圍**：原文寫「僅 `research/ai-news/` 噪音」，親驗同一 grep 指令實際命中散落 `research/agent-harness/references/`、`research/ai-articles/scored/`（含與 SWE-Bench Pro 同主題的既有條目 `2026-03-01-swe-bench-pro-morphllm.md`）、`research/tweets/`、`research/evals/runs/` 等多處，`.claude/` 治理檔零命中的承重結論不變但附註範圍失準 → 已修正措辭（已修 §2.1）。
4. **T63/T67 目標檔為已達黃區的 L1 auto-load 檔未加節制註記**：親驗 `wc -c CLAUDE.md .claude/rules/{core,loop,graph,context-management,output-discipline}.md` 現值 23,825 bytes，對照 `model-profiles.md:82` 門檻 ≤23,000/23–27k/>27k（PROVISIONAL）落在黃區，`model-profiles.md:103`「未轉正前不得以已上調為由再新增常駐條文；新增一律先等額刪除」——T63/T67 目標檔皆為 `context-management.md`（L1），原文未帶等額刪除或體積約束註記（既有 T43 有此節制先例）→ 已補 ⚠ 註記（已修 §3 T63、T67）。

**advisory（不構成缺陷，記錄供下批對照）**：ACON F 句中「且largely 保留」中英夾雜的排版瑕疵已順手修正為「且很大程度上保留」；Sculpt（2510.22251）歸檔檔本身 §4.1 與 §4.5 對 gpt-4o-mini 分數的內部矛盾（93.0% vs 97.0%）為既有歸檔缺陷，本報告僅引用無矛盾的 gpt-4o/gpt-5 區段，不構成本批瑕疵；`security-hygiene.md:68` 引用已刪除的 `subagent-strategy.md` 為既有 stale 交叉引用，非本批次新增。

> 淨結果：本批次 12 篇論文的接地與新增 8 條任務（T62-T69）**核心判斷經查核部分成立、4 處實質瑕疵已修正**（1 處數字錯誤+範圍誇大、1 處論文主張方向失準、1 處 grep 附註範圍低估、1 處遺漏常駐 byte 節制註記）；瑕疵密度 4/12，略高於 2026-07-28/07-29 兩批（3/12），累計五批瑕疵類型持續集中在「論文原文精確措辭 vs 壓縮後失真」與「workspace 既有機制覆蓋範圍誤判（誇大或低估）」兩類，12 篇量化數字本身除 PromptSci2 方向性錯誤外皆無誤。SIA 量化閘複跑仍通過（見附錄 C，複跑於本次修正後執行）。

---

## 7. 新 Skill 候選（強化研究刷新 + 驗證機制 · 2026-06-24 web 研究）

> 對照現有 29 skills，找出能強化「研究刷新 → 報告查核 → 自我驗證」流程的新 skill 機制。映射到本報告 12 維度。

| 候選 skill / 機制 | 來源 | 維度 | 強化環節 | 建議 |
|---|---|---|---|---|
| **Dreaming**（自動 transcript→playbook 固化）| Anthropic Managed Agents（2026-05 preview）| self-learn | overnight-research 跨輪記憶固化，補 MEMORY.md 人工維護缺口 | **新增** `dreaming-consolidator`（⚠ 官方 preview，CLI 整合方式待確認）|
| **SkillCAT**（success/failure 對比→causal patch→regression）| arXiv 2606.13317 | skills · self-improve | gap-vote 後 skill patch 的演化效果驗證（+40.4%）| **併入** `skill-evolution`（補回歸閉環）|
| **Live-Evo**（Experience+Meta-Guideline 雙 bank、加權衰退）| arXiv 2602.02369 | self-learn · refs | overnight-research 多輪 corpus staleness：過時 citation 降權 | 併入 `overnight-research` 或新增 `live-evo-memory` |
| **AgentCompass 雙記憶監控**（episodic+semantic、post-run debug pipeline）| arXiv 2509.14647（已收錄）| workflow · self-improve | SIA 查核加跨輪 thematic clustering | 併入 `sia` |
| **AHE 可偽證預測閘**（每次修改附 ΔX% 預測，下輪稽核）| arXiv 2604.25850（已收錄）| self-improve · harness | TEST 階段加量化 delta 承諾 | 併入 `harness-meta` / `autoload-evolution`（= 本報告 T4）|
| **Self-Harness Weakness Mining**（trace→model-specific failure pattern）| arXiv 2606.09498（已收錄）| self-improve | autoload-evolution OBSERVE 加 trace mining | 併入 `autoload-evolution` Phase 1（= 本報告 T5/T6 互補）|
| **Skilldex spec lint**（compiler-style SKILL.md 符合度評分）| arXiv 2604.16911 | skills · commands | 29 skills 結構稽核，防新 skill 偏移 | 併入 `harness-meta` schema-verify |
| **SkillRAE**（skill graph 選擇性載入降 context）| arXiv 2605.10114 | skills · refs | multi-mode 多 skill 載入 token 膨脹 | 低優先（29 skills 規模待評估是否值得）|

### 最高價值 3 項
1. **`dreaming-consolidator`（self-learn）**：官方已上線機制，自動把 transcript 提煉成跨輪 playbook，直接閉合 MEMORY.md 人工維護缺口——對應主題 B「沒有 trace 就沒有自我演化」。
2. **SkillCAT → 併入 `skill-evolution`（skills）**：補本報告 T27（skill empirical eval gate）的演化-後-驗證閉環，與 SIA `evaluate.py` 可組合。
3. **Live-Evo → `overnight-research`（self-learn）**：citation 加權衰退，強化報告查核信度，純 metadata 輕量。

> ✅ 已歸檔（2026-06-24）：SkillCAT(2606.13317)、Live-Evo(2602.02369)、SkillRAE(2605.10114)、Skilldex(2604.16911) 已收錄 research/papers/（SIA m1 仍 1.0）。
> ⚠️ 待核：① Dreaming 在 CLI session 的 SDK 整合方式（類比 overnight-research bypassPermissions Lesson）；② Beaver(2606.21005) web 搜尋未定位——歸檔時 abs 頁有內容，列 `[unverified-external]` 待回查正確 title/URL。
> 這些是 **PROPOSE 候選**，落地須走 `skill-evolution` / `harness-meta:add` 並各帶機械驗證 + APPLY 前置 gate。

---

## 附錄 C：SIA 量化查核（evaluate.py 實跑）

本報告經 SIA BYOT `evaluate.py`（純確定性，無 LLM key）查核，Gen1→Gen2→Gen3→Gen4 演化：

| metric | Gen1 | Gen2 | Gen3（2026-07-26 +12 papers） | Gen4（2026-07-27 +12 papers） | Gen6（2026-07-28 +12 papers） | Gen7（2026-07-29 +12 papers） | Gen8（2026-07-30 +12 papers） | 說明 |
|--------|------|------|------|------|------|------|------|------|
| overall | 0.8935 | 1.0 | 0.976 | 0.969 | 0.9727 | 0.9757 | **0.978** | 分母隨新任務/新路徑持續增加，m2 未達滿分拉低整體，仍遠高於 ≥0.90 閘值 |
| m1 citation 接地 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | **1.0** | 126/126 cited arxiv_id 全部真實收錄（含本批次 +12） |
| m2 task path validity | 0.645 | 1.0 | 0.92 | 0.897 | 0.9091 | 0.9189 | **0.9268** | 41 個相異路徑中 38 通過，3 失敗（`opus-pilot/SKILL.md`、`refs/multi-agent-coordinator-pattern.md`、`subagent-strategy.md`，皆為既有 T29/T14/T10 路徑缺陷，非本批次新增；本批次 T62-T69 新增路徑全數通過，含修正後的 `.claude/rules/security-hygiene.md`） |
| m3 audit regression | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | 1.0 | **1.0** | 5/5 勘誤回歸持續通過 |

> Gen5（2026-07-27 第二批次 T45-T47）當時未回填此表，為既有記錄缺口，非本次新增遺漏；不回溯重建（無法重跑當時的 repo 快照）。

評分器：`research/evals/sia-report-audit/data/public/evaluate.py`（亦為 Routine D 的 TEST 量化閘）。

---

*方法：overnight-research pipeline（corpus 萃取 → gate-vote 共識 → multi-mode 3 軸審計 → SIA evaluate.py 量化查核）。scratch 來源：`research/scratch/paper-syn-{1..4}.md`。本報告任務為候選，落地各自須帶機械驗證；衝突項（第 4 節）須人類決策後啟動。新 skill 候選（第 7 節）走 skill-evolution/harness-meta:add 落地。*

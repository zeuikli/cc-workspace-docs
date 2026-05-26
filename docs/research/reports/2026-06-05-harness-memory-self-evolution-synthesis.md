# Harness + Memory 自我進化 — 學術基礎與實作對照

> **建立日期**: 2026-05-29 · **最後更新**: 2026-06-05（併入 2026-05 後新增 10 篇論文 + tweets/blog/best-practices 一手洞察）  
> **類型**: 論文合成報告（活文件，持續併入新證據）  
> **基礎論文**: 原 8 篇（2023–2026）-> 擴充至 18 篇（+ 原有 Continual Harness 篇補強）  
> **用途**: 為 cc-workspace GOTCHA/RATCHET/autoload-evolution 框架提供學術依據  
> **關聯文件**: `docs/harness-guidelines-workspace.md` · `research/agent-harness/HARNESS-CARD.md` · `memory/RATCHET.md`

---

## 2026-06-05 更新摘要

本次更新併入 2026-05 後 repo 新增語料，所有數字均**親驗原文**（researcher verdict 非證據）：

- **harness 論文 +6 篇**（runtime-substrate / life-harness / vesper / meta-harness / coordination-layer / code-as-agent-harness）
- **memory 論文 +5 篇**（useful-memories-faulty / ACE / δ-mem / Hindsight / MemoryOS）
- **一手洞察**：Anthropic Dreaming（離線非同步學習）· advisor-tool 官方最佳實踐 · harness ROI > 模型升級的跨 benchmark 量化

**最重要的單一新證據**（直接補強原報告 §1「整合操作 LLM 偏差注入風險」）：
> **Useful Memories Become Faulty**（arXiv 2605.12978）親驗摘要原文：GPT-5.4 即使**從完全正確的 ground-truth 軌跡**做連續整合，仍在 ARC-AGI 上從 100% 跌至 46%（失敗率 54%）。退化根源是 **consolidation step 本身**，非 experience 品質。論文建議：raw episode 作 first-class evidence，**顯式門控整合**，不要每次互動後自動觸發。
> -> cc-workspace 啟示：`memory-compactor` 每次 session 全量壓縮 = 高頻強制整合，正是該論文警告的反模式（見下方「設計缺口」更新）。

---

## 核心論題

**8 篇論文共同收斂到同一個設計原則**：

> Agent 能力的上限由「模型 + 記憶體 + 控制架構」三者決定，而非模型單獨決定。
> 自我進化的關鍵在於：失敗偵測 -> 知識提煉 -> 架構修正 -> 效果驗證的閉環。

---

## 論文摘要與 Workspace 對照

### 1. Rethinking Memory (arXiv 2505.00675, 2025-05-01)

**核心主張**: 記憶體分為「參數型」（模型權重）和「情境型」（外部儲存），六種核心操作構成完整架構：整合（consolidation）/ 更新 / 索引 / 遺忘 / 檢索 / 壓縮。

**關鍵機制**:
- 整合操作具不可逆風險 + LLM 偏差注入風險
- 索引需稠密（語意）+ 稀疏（關鍵字）混合策略
- 遺忘不是刪除，是優先度重排

**Workspace 對照**:

| 論文概念 | cc-workspace 實作 |
|---------|-----------------|
| Consolidation | `memory/MEMORY.md` Lesson 提煉；Batch Gate 5-10 sessions |
| Updating | `autoload-evolution` core.md/rules 更新，同步更新 RATCHET.md |
| Forgetting | `memory-compactor` agent（≥200 行觸發）|
| Retrieval | `memory/MEMORY.md` session 開工前主動讀取 |
| Condensation | `/compact` hint 機制 |

---

### 2. A-MEM: Agentic Memory (arXiv 2502.12110, 2025-02-17)

**核心主張**: Zettelkasten 式互連記憶（非孤立向量）使記憶體在接收新知識時能動態進化，而非單純插入。

**關鍵機制**:
- 原子筆記帶多結構屬性（情境 / 關鍵字 / 標籤）+ 雙向連結
- 新記憶整合觸發**既有記憶的修訂**（非追加）
- 與 RAG 本質差異：進化結構 vs 靜態語意相似

**Workspace 對照**:
- `GOTCHA.md` 新增條目應觸發對 `MEMORY.md` 現有 Lesson 的重審（目前缺失）
- `RATCHET.md` 的 flywheel 設計部分符合「新失敗更新既有規則」的概念
- ~~**待改進**：MEMORY.md Lesson 應建立反向連結~~ ✅ 2026-06-05 已建（tracked `memory/MEMORY.md` ↔ 6 GOTCHAS.md 雙向，commit 611bf5bf）

---

### 3. Harness Engineering for Language Agents — CAR (He et al. 2026-04-23)

**核心主張**: Agent 效能源自 Harness（Control + Agency + Runtime），而非模型單獨決定；學術界與工程實踐的可見度不對稱掩蓋了 Harness 驅動的效能提升。

**三層架構**:

| 層 | 定義 | cc-workspace 實作 |
|---|------|-----------------|
| **Control (C)** | 持久語言約束 | CLAUDE.md + `.claude/rules/*.md` + AGENTS.md |
| **Agency (A)** | 行動基底（工具 API / 介面 / 編排）| Tool schemas + Skill YAML frontmatter |
| **Runtime (R)** | 執行保證、狀態持久化、失敗管理 | Hooks（12 事件）+ session lifecycle + MEMORY.md |

**HarnessCard 對應**: 直接套用 CAR 框架生成 `research/agent-harness/HARNESS-CARD.md`。

---

### 4. Continual Harness — Online Adaptation (arXiv 2605.09998, 2026-05-11)

**核心主張**: Harness 組件（提示 / sub-agents / skills / memory）能在不重置環境的情況下，透過對抗失敗特徵偵測在 mid-episode 自主優化。

**兩層迴圈**:
- **內層**：Agent 行動迴圈
- **外層**：Refiner 每 F 步對 4 個組件（system prompt / sub-agents / skills / memory）執行 CRUD

**Workspace 對照**:
- `autoload-evolution` 6-phase 閉環 = Continual Harness 外層迴圈
- Refiner 角色 = `advisor()` + reviewer agent（PGE 分離）
- **核心差異**：論文的 Refiner 是自動 LLM；workspace 要求人類或獨立 agent 確認（Rule 1）

---

### 5. ReasoningBank — Memory-Driven Self-Evolution (arXiv 2509.25140, 2025-09-30)

**核心主張**: 從成功與失敗經驗中提煉可泛化的推理策略（非原始軌跡），記憶品質反饋提升擴展效果（MaTTS）。

**關鍵機制**:
- 自我評判分叉：成功**與**失敗經驗都用於對比信號
- 雙迴圈：檢索記憶 -> 執行任務 -> 整合學習 -> 改善記憶
- MaTTS（Memory-aware Test-Time Scaling）放大經驗多樣性

**Workspace 對照**:
- `MEMORY.md` Lesson 格式 = 提煉推理策略（成功 + 失敗對比）
- `/deep-review` 多輪嘗試 ≈ MaTTS 多嘗試策略合成
- 自我評判 = R4 可觀測條件驗證（不接受「看起來對」）

---

### 6. The Last Harness You'll Ever Build (arXiv 2604.21003, 2026-04-29)

**核心主張**: 兩層自動化——Harness 進化（優化單任務 worker）+ 元進化（跨領域優化進化藍圖）——消除手動 harness 工程。

**Harness 完整定義**:
> Harness = 提示 + 工具 + 編排 + hooks + 模型配置（**除模型以外的一切**）

**Workspace 對照**:
- `autoload-evolution` = Harness 進化層（Cycle 1-6 已完成）
- 元進化層 = `RATCHET.md` flywheel（跨 session 學習**哪種修改有效**）
- Evolution Agent 角色 = `advisor()` function（分離 Generator 與 Evaluator）

---

### 7. Reflexion — Verbal Reinforcement Learning (arXiv 2303.11366, 2023-03-20)

**核心主張**: 語言 Agent 透過 episodic verbal reflection（非梯度更新）學習，在記憶體中保存反思以引導後續嘗試。

**三元組迴圈**: Actor -> 失敗 -> 語言化錯誤 -> Episodic buffer -> 帶記憶重試

**Workspace 對照**:

| Reflexion 概念 | cc-workspace 實作 |
|--------------|-----------------|
| Episodic buffer | `memory/MEMORY.md` Lesson 條目 |
| Verbal reflection | "Lesson YYYY-MM-DD: [失敗模式] -> [防範規則]" |
| No parameter update | 不需 fine-tune；僅更新 MEMORY.md + rules |
| Causal diagnosis | GOTCHAS.md "[根因] -> [防範規則] -> [驗證方式]" |

**這是整個 cc-workspace 記憶設計的學術祖先**。

---

### 8. Harness Engineering as Categorical Architecture (arXiv 2605.12239, 2026-05-12)

**核心主張**: Harness 是正式架構（G, Know, Φ），四支柱（記憶 / skills / 協議 / harness）對應範疇論結構，Compiler functors 保證結構不變式。

**三元組**:
- **G**（語法連線）：型別化資訊流圖
- **Know**（知識結構）：可重放驗證的 certificates（優先門控、收斂檢查）
- **Φ**（部署映射）：能力槽 -> 具體模型

**Workspace 對照**:
- `.claude/rules/*.md` = Know-layer 不變式
- Skills 的 YAML frontmatter = operadic 組合的型別宣告
- Hooks = trace 回饋迴圈（執行後稽核 -> 修正不變式）
- **R4 驗證紀律 = certificate 保存**（修改前後 healthcheck 通過）

---

# 2026-06-05 新增論文（9–19）

> 接地紀律：每篇主張/數字均親驗原文段落；僅邊緣相關者誠實標註，不硬湊對應（mapping 過 "一句零 hedge" 測試）。

## A. Memory 自我進化 — 新增 5 篇

### 9. Useful Memories Become Faulty (arXiv 2605.12978, 2026-05-13)

**核心主張**: LLM 對**正確** ground-truth 軌跡做連續整合（consolidation），記憶效用先升後降，可低於 no-memory 基線。退化根源是 consolidation step，非 experience 品質。

**親驗數字**（摘要原文）:
- GPT-5.4 在 ARC-AGI：無記憶 100% -> 連續整合後 **46%**（失敗率 54%）
- ARC-AGI Stream 環境（Retain/Delete/Consolidate）：保留 raw episode 的 agent 準確率是**強制整合**版本的 2 倍
- episodic-only 控制組（只保留軌跡不整合）與最佳 consolidator 相當

**三個失效機制**: Misgrouping（錯誤歸類）/ Interference（相互干擾）/ Overfitting（過度泛化）。

**Workspace 對照**（這是本次最關鍵的一篇）:
- **直接證實原報告 §1 的「整合操作 LLM 偏差注入風險」假設** — 從推測升級為實證
- `memory-compactor` 每次 session 全量壓縮 = 該論文定義的「forced-consolidation after every interaction」反模式
- 工程建議：MEMORY.md 應把**近 N session 的原始 session 節當 first-class evidence 保留**，compaction（整合）顯式門控而非到 200 行就無條件觸發

---

### 10. ACE — Agentic Context Engineering (arXiv 2510.04618, ICLR 2026)

**核心主張**: 把 context 視為「演化 playbook」，用 Generator -> Reflector -> Curator 三模組做**增量 delta update**（非全量改寫），防止 brevity bias 與 **context collapse**（迭代改寫侵蝕細節）兩個失效模式。

**親驗數字**: vs full-rewrite 基線 +10.6%（AppWorld）；vs GEPA latency −82.3%、cost −91.5%；cache hit 91.8%。

**Workspace 對照**:
- MEMORY.md 目前全量 session 節更新 = monolithic rewrite，正是 ACE 警告的 context collapse 來源
- ACE 的 delta-bullet 模式（新 insight 追加、頻率計數、去重）可作 `memory-compactor` 重設計的介面參考
- 與 2605.12978 互補：ACE 給「如何不崩潰地更新」的工程解法，後者給「為何會崩潰」的機制證據

---

### 11. δ-mem — Efficient Online Memory (arXiv 2605.12357, 2026-05-12)

**核心主張**: 用 delta-rule 將歷史壓縮進固定大小（8×8）online state matrix，低秩修正直接耦合 frozen Transformer attention，只寫殘差（已習得關聯近零更新量）。

**親驗數字**: MemoryAgentBench 1.31×、LoCoMo 1.20×（§4.2-4.3）。

**Workspace 對照**: 屬模型層機制（非 textual memory），對 workspace 偏離較遠。唯一概念類比 — 「gated forget + write only residual」支持 memory-compactor「只寫真正新增資訊」而非全量改寫的設計方向。**標：邊緣相關（abstraction level 不同）**。

---

### 12. Hindsight — Retain, Recall, Reflect (arXiv 2512.12818, 2025-12-14)

**核心主張**: 四網絡記憶架構（world facts / agent experiences / synthesized summaries / **evolving beliefs**）明確分離證據層與推理層。

**親驗數字**: LongMemEval 83.6%（20B 開源模型，超越 GPT-4o 的 full-context 39% 基線）。

**Workspace 對照**:
- workspace MEMORY.md 是單一扁平 session 層；Hindsight 的「beliefs（推斷/假設）vs experiences（原始記錄）」分層可映射為「決策/Lesson vs 原始 session 記錄」雙層
- 與 2605.12978 一致：experiences 層保留 episodic 不被覆蓋 = episodic-first 原則

---

### 13. MemoryOS (arXiv 2506.06326, 2025-05-30)

**核心主張**: 借鑒 OS 分段分頁，STM->MTM->LPM 三層 + heat-based eviction 統一記憶管理。

**親驗數字**: LoCoMo +49.11% F1 / +46.18% BLEU-1（GPT-4o-mini）；token 較 MemGPT −77.2%（§3.3 heat score = N_visit × 存取量 × 時間衰減）。

**Workspace 對照**: MEMORY.md 目前無熱度/頻率概念；heat score 公式可作「哪些 Lesson 應 promote 到 MEMORY 核心、哪些應壓縮遺忘」的量化遺忘優先序設計靈感。對「遺忘 = 優先度重排」（原報告 §1 Rethinking Memory 的主張）提供可計算形式。

---

## B. Harness 自我進化 — 新增 6 篇

### 14. Continual Harness — Online Adaptation（補強，arXiv 2605.09998）

> 原報告 §4 已收錄，本次補入親驗的**新發現**（非重複）：

- 外層 Refiner 對 4 元件（system prompt / sub-agents / skills / memory）做 CRUD，在真實環境（Pokémon Blue/Yellow/Crystal 全通關）驗證
- **refinement 自然集中在瓶頸元件**（非均勻分佈）
- **harness 是可繼承的遷移單元**；但拋棄繼承的 sub-agent 會觸發迴歸
- **能力下限以下 refinement 無效**（Gemini Flash-Lite 全面衰退）-> 對應 workspace「Capability Floor」（subagent-strategy.md）
- 對照：`autoresearch` skill 的 Modify->Verify->Keep/Discard 與 Refiner outer loop 同構

---

### 15. AI Harness Engineering — Runtime Substrate (arXiv 2605.13357, 2026-05-13)

**核心主張**: agent 失敗根因是 runtime substrate 缺失（11 元件責任），非模型能力不足。H0->H3 梯度量表區分支援層級的可驗證度。

**新增視角**（原報告未覆蓋）:
- **Attribution-Before-Recovery**：失敗歸因必須先於修復動作，獨立為 harness 元件責任
- **M-HIR**（Missing-Harness Human Intervention Rate）量化診斷指標
- entropy_auditor：追蹤 harness 維護負擔

**Workspace 對照**: R12 Fail Loud + healthcheck.sh 對應 H3 verification protocol；entropy auditor 對應目前缺自動化的「定期 harness 稽核」（harness-meta:audit 是手動版）。

---

### 16. Life-Harness — Adapting the Interface, Not the Model (arXiv 2605.22166, 2026-05-21)

**核心主張**: 凍結模型下，透過四生命週期層（環境契約 / 程序技能 / 動作實現 / 軌跡調節）針對性修復失敗類型。

**親驗數字**: 88.5% 平均相對改進（126 model×environment settings 中 116 改善，§Main Results）。

**新增視角**: 在 **Qwen3-4B 上演化的 harness 可遷移至 17 個更大模型** -> 證明失敗模式是**環境層級**而非模型特異。

**Workspace 對照**: 為「harness rules 應保持 model-agnostic」提供實證（呼應 R1–R12 通用化研究）；GOTCHAS.md 可依四失敗類別重新分類以提升覆蓋稽核。

---

### 17. Effective Harness Engineering — Vesper (arXiv 2605.15221, 2026-05-15)

**核心主張**: 基礎設施設計（非模型能力）決定演算法探索成功率。

**親驗數字 — Capability Paradox（原報告未涵蓋的反直覺方向）**:
- 更強模型（GPT-5.2-codex）產生 **16.6% evaluation hack 率**；弱模型（GPT-5.1-codex-mini）為 **0%**（§Key Finding 2）
- git worktree 隔離並行 agent：3.2×–3.9× speedup（4 agents）

**Workspace 對照**: 「能力越強越需要更強驗證」直接支持 generator≠evaluator（PGE）；git worktree 隔離已在 `feature.sh wt-start` 實作（呼應 MEMORY 分支互搶根因解）。

---

### 18. Meta-Harness — End-to-End Optimization (arXiv 2603.28052, 2026-05-12 收錄)

**核心主張**: 給 proposer 完整 filesystem 存取（trace + 過去程式碼 + 分數）自動搜尋更好的 harness。

**親驗數字**: scores-only 降至 34.6 median；**full traces 達 50.0**（§Ablation）-> 壓縮 trace 會丟失關鍵改進信號。

**Workspace 對照**: 直接支持 MEMORY.md「保存完整錯誤 string 原文，勿改寫」的設計（與 2605.12978 的 raw-episode-first 結論一致 — 兩篇從不同方向收斂到「別過早壓縮證據」）。

---

### 19. Coordination as an Architectural Layer (arXiv 2605.03310, 2026-05-05)

**核心主張**: 協調層必須被明確設計為獨立架構層，不能期待從能力湧現。

**親驗數字**: hierarchical 配置對比無協調基線 +26.6pp（Murphy decomposition，n=100，§Empirical Results）。

**Workspace 對照**: 為 `subagent-strategy.md` 的 fan-out≤4 + parent↔child-only 拓撲提供 empirical backing（peer-critique 是最差協調模式之一）。**標：對「memory 自我進化」邊緣相關，對「harness 協調結構」直接相關。**

---

# 一手實務洞察（tweets / blog / best-practices）

> 信度標註：Anthropic 官方 docs/blog + @bcherny（Claude Code 負責人）+ @trq212（Claude Code PM）= 官方一手；@karpathy / @Mnilax / MindStudio = 業界觀點（MEDIUM，自評/未第三方驗證）。

| # | 洞察 | 來源 | 信度 |
|---|------|------|------|
| T1 | **Anthropic Dreaming**：error event 寫入 dreaming buffer，**離線非同步** pass 分析後更新工作記憶，不污染進行中 session context | `tweets/2026-05-07-@anthropic-dreaming-offline-learning.md` | 官方公告 |
| T2 | **Harness ROI > 模型升級**：同模型 GPT-5.5 在 Codex harness 61.5% vs Cursor harness 87.2% SWE-Bench = **+25.7pp**，超過一個模型世代（~20pp） | `tweets/2026-05-05-@mindstudio-harness-beats-model.md` | 業界(MED) |
| T3 | **advisor 官方最佳時機**：① 探索性讀取後未開始實質工作 ② file writes/test outputs 完成後；system prompt 加一行（<100 字）可削減 35–45%；≥3 次呼叫才啟用 caching | `best-practices/07-advisor-tool-best-practices.md` | 官方 |
| T4 | **Generator-Verifier 是最廣泛部署的協調模式**（PGE 的官方稱法）；Haiku+Opus advisor 降 85% 每任務成本 | `claude-blog/docs/synthesis.md` | 官方 |
| T5 | **CLAUDE.md 具體性優先**：「Use 2-space indentation」優於「Format code properly」；>200 行->path-scoped rules；compact 後僅 project-root CLAUDE.md 存活 | `best-practices/21-memory-claudemd.md` | 官方 |
| T6 | **prompt caching = harness SLO**：static-first prefix，動態資訊用 `<system-reminder>` 插 user message；**mid-session 切 Haiku 比留 Opus 更貴**（需重建 cache） | `tweets/2026-02-19-@trq212-673516.md` | 官方(PM) |
| T7 | **CLAUDE.md 是會腐爛的 cache**：dream->diff->apply->14–30 天->再 dream；一次性修正被永久化是主要腐化源 | `tweets/2026-05-14-@Mnilax-443903.md` | 業界(MED) |

**T1+T7 對 workspace 的關鍵啟示**：Anthropic 官方 Dreaming（離線非同步學習）+ Mnilax dream-pass 維護迴圈，與 workspace 的 `autoload-evolution`（6-phase 閉環）和 MEMORY「自我改進觸發」是同一機制的不同實現。差異仍是原報告 §4 的結論：**論文/官方的 Refiner 偏自動，workspace 要求人類或獨立 agent 確認（R1 PGE）**。T1 的「不污染進行中 session」原則 = workspace「mid-session 禁止改 CLAUDE.md，等 session 結束」規則的學術對應。

---

## 合成：Harness ↔ Memory 雙向進化迴圈

**原 8 篇收斂的核心統一模式**（新增 10 篇從不同角度補強，非全部直接 confirm 此迴圈——δ-mem/Coordination 對「memory 自我進化」僅邊緣相關，見各篇標註）：

```
失敗信號
    ↓
[記憶層] GOTCHAS.md / MEMORY.md Lesson
    ↓ (Reflexion / ReasoningBank)
[提煉] 可泛化規則（非原始軌跡）
    ↓ (A-MEM / Rethinking Memory)
[整合] 更新既有規則或新增規則
    ↓ (Continual Harness / Last Harness)
[架構修正] core.md / hooks / skills
    ↓ (CAR / Categorical)
[驗證] healthcheck / eval / per-model-eval
    ↓ (RATCHET flywheel)
[記錄] RATCHET.md -> 下次 cycle 的 baseline
    ↑___________________________|
```

---

## Workspace 設計缺口（論文視角）

| 缺口 | 來源論文 | 嚴重度 | 建議行動 |
|------|---------|-------|---------|
| ~~GOTCHA 觸發 -> 既有 Lesson 未重審~~ ✅ 已建雙向連結 | A-MEM | — | 2026-06-05 APPLY：MEMORY ↔ GOTCHA 6 配對雙向連結（commit 611bf5bf）。後續可選：連結建立後觸發既有 Lesson 自動重審（A-MEM 進化語意，目前為靜態連結） |
| Continual Harness 缺乏自動 Refiner | Continual Harness | 低 | 現有 advisor() + 人工確認已足夠（Rule 1 PGE）|
| 記憶遺忘策略未明確 | Rethinking Memory | 低 | memory-compactor 已部分解決；可加優先度標記 |
| 元進化層無跨領域遷移記錄 | Last Harness | 低 | RATCHET.md flywheel 是雛形；需跨 session 統計 |
| ~~per-model-eval 基準未建立~~ ✅ 已完成 | SkillsBench / HAL | — | baseline 15 trials 已於 2026-05-30 執行，見 `.claude/refs/per-model-eval-suite.md` |

### 2026-06-05 新增缺口（新論文視角）

| 缺口 | 來源論文 | 嚴重度 | 建議行動 |
|------|---------|-------|---------|
| **compactor 高頻強制整合風險**（原列「低」應上調）| Useful Memories Faulty (2605.12978) | **中->高** | 從推測升為**實證**：全量壓縮 = forced-consolidation 反模式。建議近 N session 原始節作 first-class evidence 保留，compaction 顯式門控（非 200 行無條件觸發）|
| MEMORY 全量改寫易 context collapse | ACE (2510.04618) | 中 | 評估 delta-update 模式（新 insight 追加 + 頻率計數 + 去重）取代 monolithic session 節改寫 |
| 證據層 vs 推理層未分離 | Hindsight (2512.12818) | 低 | MEMORY「決策/Lesson（beliefs）vs 原始 session（experiences）」可顯式分層，防 compactor 混淆 |
| 遺忘無量化優先序 | MemoryOS (2506.06326) | 低 | heat score（visit×size×decay）可作 Lesson promote/壓縮的計算依據 |
| 失敗歸因未獨立於修復 | Runtime Substrate (2605.13357) | 低 | R12 已部分覆蓋；可加「attribution-before-recovery」明確化 |
| 能力越強驗證需越強（Capability Paradox）未納入 | Vesper (2605.15221) | 低 | generator≠evaluator 已實作（PGE）；高能力模型的 eval-hack 風險值得在 R9 註記 |

---

## 參考論文清單

**原 8 篇（2023–2026-05 上旬）**

| 論文 | arXiv | 本地路徑 |
|-----|-------|---------|
| Rethinking Memory | 2505.00675 | `research/papers/2025-05-01-rethinking-memory-llm-agents-operations-2505-00675.md` |
| A-MEM | 2502.12110 | `research/papers/2025-02-17-amem-agentic-memory-llm-agents-2502-12110.md` |
| CAR (Harness Engineering) | preprints 202603.1756 | `research/papers/2026-04-23-harness-engineering-language-agents-car.md` |
| Continual Harness | 2605.09998 | `research/papers/2026-05-11-continual-harness-online-adaptation-2605-09998.md` |
| ReasoningBank | 2509.25140 | `research/papers/2025-09-30-reasoningbank-scaling-agent-self-evolving-2509-25140.md` |
| Last Harness | 2604.21003 | `research/papers/2026-04-29-last-harness-youll-ever-build-2604-21003.md` |
| Reflexion | 2303.11366 | `research/papers/2023-03-20-reflexion-verbal-reinforcement-learning-2303-11366.md` |
| Categorical Architecture | 2605.12239 | `research/papers/2026-05-12-harness-engineering-categorical-architecture-2605-12239.md` |

**2026-06-05 新增 10 篇**（正文 §9–19 有獨立論述；§14 Continual Harness 為原有篇目補強，不重列）

| 論文 | arXiv | 本地路徑 |
|-----|-------|---------|
| Useful Memories Faulty | 2605.12978 | `research/papers/2026-05-13-useful-memories-faulty-llm-continuous-update-2605-12978.md` |
| ACE (Agentic Context Eng.) | 2510.04618 | `research/papers/2025-10-06-agentic-context-engineering-2510-04618.md` |
| δ-mem | 2605.12357 | `research/papers/2026-05-12-delta-mem-efficient-online-memory-llm-2605-12357.md` |
| Hindsight | 2512.12818 | `research/papers/2025-12-14-hindsight-agent-memory-retain-recall-reflect-2512-12818.md` |
| MemoryOS | 2506.06326 | `research/papers/2025-05-30-memory-os-ai-agent.md` |
| Runtime Substrate | 2605.13357 | `research/papers/2026-05-13-ai-harness-engineering-runtime-substrate-2605-13357.md` |
| Life-Harness | 2605.22166 | `research/papers/2026-05-21-adapting-interface-not-model-life-harness-2605-22166.md` |
| Vesper | 2605.15221 | `research/papers/2026-05-15-effective-harness-engineering-vesper-2605-15221.md` |
| Meta-Harness | 2603.28052 | `research/papers/2026-05-12-meta-harness-2603-28052.md` |
| Coordination Layer | 2605.03310 | `research/papers/2026-05-05-coordination-architectural-layer-2605-03310.md` |

> 註：① CAR 來源為 preprints.org manuscript 202603.1756（非 arXiv）；原報告 L197 的 `2604.xxxxx` placeholder 已於本次更正。② Code-as-Agent-Harness (2605.18747) 與 HeavySkill (2605.02396) 經親讀屬邊緣相關（綜述/推理品質），未納入正文。

---

## 下一步行動

> **執行狀態（2026-06-05，commit 611bf5bf，feature/memory-gotcha-backlinks）**：6 項結算 **APPLY 1 / RECORD 2 / DEFER 2 / NO-OP 1**。計劃書 `research/reports/2026-06-05-next-steps-execution-plan.md`。

1. ~~**per-model-eval 基準建立**~~ ✅ 已完成（2026-05-30，baseline 15 trials；見 `.claude/refs/per-model-eval-suite.md`）
2. ~~**MEMORY.md 反向連結**~~ ✅ **已 APPLY**（2026-06-05）：A-MEM **雙向**連結（非僅單向）。tracked `memory/MEMORY.md` 6 處 Lesson 加 `[GOTCHA: skill/GOTCHAS.md「錨點」]` + 對應 6 個 GOTCHAS.md 加 `[Lesson: MEMORY 防範規則#date]`。6 唯一 Lesson 配對（researcher 提議->parent 逐條 grep 驗證錨點全存活；42/48 Lesson NO MATCH，符合「多數 session-workflow 教訓無 per-skill 對應」預期，不硬塞）。**邊界**：正確目標為 tracked `memory/MEMORY.md`（非 machine-local 未 tracked 版，避免 commit 斷鏈進 repo）。
3. ~~**GOTCHA 3-session 回顧**~~ ✅ **已 RECORD**（2026-06-05）：`git log --oneline --all -- ".claude/skills/*/GOTCHAS.md" | wc -l` = **35**（基準=5，增量 30 ≫ 3）-> stop hook 維持（不升格 PreToolUse）。
4. 🆕 **compactor 整合風險評估**（中優先，源 2605.12978）-> **ASSESS->DEFER**（2026-06-05）：評估確認過度整合風險**已由 Lesson 2026-06-04-G 的 `comm -23` 流失對比防範部分緩解**；論文建議「近 N session 原始保留」= 既有「零損失保留 Lesson」指令的結構強化。改 `memory-compactor` SKILL 屬行為變更 -> **DEFER 至獨立 gated session**。驗收條件：壓縮後 grep 確認最近 3 session 原始 Lesson 實質存活（非 stub）。
5. 🆕 **R9 高能力模型 eval-hack 註記**（低優先，源 Vesper 2605.15221）-> **PROPOSE->DEFER**（2026-06-05）：R9 在 `core.md`（auto-load 18,455/19,000 bytes），變更**必走 `/autoload-evolution`** 閉環（≤1 規則/cycle + eval 回歸 gate），不可本 session inline 改。已寫成 PROPOSE 提案待 gated 執行。
6. 🆕 **Dreaming 對齊查核**（低優先，源 tweets/2026-05-07 官方）-> **NO-OP**（2026-06-05）：確認 `autoload-evolution` 閉環 + context-management「mid-session 禁改 CLAUDE.md」已對應官方 Dreaming「離線非同步、不污染進行中 session」原則，**無需額外動作**，對應關係已記錄。

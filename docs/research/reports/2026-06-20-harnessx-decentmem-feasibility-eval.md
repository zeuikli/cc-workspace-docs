---
title: "HarnessX / DecentMem 落地可行性評估 — 值得做嗎？"
date: 2026-06-20
status: eval complete
branch: claude/anthropic-claude-code-expertise-5myrpg
method: 讀一手 MD + PDF 歸檔 → 主對話 grep 接地轉移條件 → fable-pilot 審閱
papers: ["HarnessX (arXiv 2606.14249) — Critical 自評", "DecentMem (arXiv 2605.22721) — High 自評"]
type: feasibility-eval + verdict
verdict_policy: 不採信論文 headline 數字為 workspace-applicable；只認「轉移條件成立 + 真實失敗模式 + Rule-of-3」三關全過
---

# HarnessX / DecentMem 落地可行性評估

> **核心問題**：這兩篇論文的 idea **在本 workspace 落地**是否值得做？（非「論文好不好」——論文都是 V 接地的優質工作。）
> **判準（三關全過才 worth）**：① 轉移條件成立（論文前提在 workspace 為真）；② 解決 workspace **實存**失敗模式（非假想）；③ Rule-of-3 / 不過度工程。
> **anti-hack 鐵律**：論文的 +14.5% / +23.8% / −49% 是**其 benchmark × 其架構**的結果，**不等於** workspace 增益；採信前須驗轉移條件。

---

## 0. Verdict TL;DR

| 論文 | 落地 Verdict | 一句話理由 |
|------|-------------|-----------|
| **HarnessX — AEGIS 演化引擎** | ❌ **DON'T BUILD** | 缺前置基建（自動 trace pipeline）+ codebase 未釋出 + 多 agent 演化成本高；ROI 為負 |
| **HarnessX — 九維分類法 checklist** | ✅ **DO（小）** | 真實缺口（harness-meta 無此 checklist）+ 低成本（~15 行）+ 操作化「harness 完整性」 |
| **HarnessX — seesaw = unverified_success 背書** | ✅ **DO（≈0 成本）** | 一行 citation，把既有閘門接上學術理論背書 |
| **DecentMem — per-agent 雙池記憶** | ❌ **DROP**（非 P2，連觀察都不必升級為實作路徑）| 前提**結構性不成立**：workspace 無「跨 agent 共享活記憶池」可崩潰；bandit 數學不遷移 |

**淨可執行殘留 = 1 個小項**（HarnessX 九維 checklist + seesaw citation，可合併一次 ≤20 行 edit）。其餘皆 DROP/保留為 archive reference。

---

## 1. HarnessX — 分層評估

### 1.1 AEGIS 演化引擎 — DON'T BUILD（轉移條件失敗）

AEGIS 四階段（Digester→Planner→Evolver→Critic+Gate）需要的前置基建 vs workspace 實況（grep 接地）：

| AEGIS 前置 | workspace 實況 | 成立? |
|-----------|---------------|-------|
| 自動 trace pipeline（每迭代 ~10M tokens raw traces → Digester）| evals/ 為**手動/週期** baseline+runs，**無連續 trace 餵入** | ❌ |
| 確定性 benchmark gate（seesaw：候選不得 regress 任何通過任務）| `measure.sh --gate`(exit 1) + healthcheck **存在但範圍窄**（byte cap/header/anchor，非任務 benchmark suite）| ⚠️ 部分 |
| 多 agent 演化 compute 預算 | workspace 是個人 harness，多 agent 演化成本（論文自陳「cost-performance tradeoff 顯著」）不合比例 | ❌ |
| 可直接用的實作 | codebase「未來釋出」(§7) | ❌ |

→ **4 條前置 3 缺 1 部分**。AEGIS 的 +14.5% 來自「自動 trace + benchmark gate + 多 agent compute」三者齊備；workspace 三缺，**移植 = 從零建一套 eval 基建**，遠超任何 idea 的價值。**ROI 為負，DON'T BUILD。**

### 1.2 九維分類法（D1–D9）— DO（小，真實缺口）

D1 模型選擇 / D2 上下文組裝 / D3 記憶管理 / D4 工具生態 / D5 執行環境 / D6 評估獎勵 / D7 控制安全 / D8 可觀測性 / D9 訓練橋接。

- **真實缺口**：grep `harness-meta/` → **無任何九維/完整性 checklist**。workspace 的 harness 稽核（K×M、HMF）有過程但**無「九維是否都覆蓋」的完整性對照表**。
- **價值**：D1–D9 是「harness 設計有沒有漏掉一整類」的機械 checklist，正交補強既有稽核（對照本 session 稍早 TIER B 的 ETCLOVG 7 類失敗分類——兩者一個是**設計維度**一個是**失敗分類**，互補不重複）。
- **成本**：~15 行掛 `harness-meta` GOTCHAS/ref，**不佔 auto-load byte**。
- **Rule-of-3**：harness 稽核是高頻活動（harness-meta 整個 skill 存在），checklist 有多次複用點 → 過關。
- **Verdict：DO**（小、低風險、真實缺口）。

### 1.3 seesaw constraint — DO（≈0 成本 citation）
seesaw（候選不得 regress 任何先前通過任務）= core.md「能通過任何實作的測試 = 沒有測試」+ `unverified_success` 閘門的**數學形式化**。一行 citation 把既有閘門接上學術背書，強化「為何這條閘門非裝飾」的說服力。**DO**。

---

## 2. DecentMem — DROP（前提結構性不成立）

DecentMem 的增益（+23.8% acc / −49% token）來自解決「**集中式共享記憶 → agent 多樣性崩潰**」。關鍵問題：**workspace 有這個問題嗎？**

### 2.1 轉移條件逐項證偽（grep 接地）

| DecentMem 前提 | workspace 實況 | 成立? |
|---------------|---------------|-------|
| 多 agent **共享**集中式記憶池 | CLAUDE.md:3「**Sub-agents 不繼承本檔**」；subagent-strategy:22「MEMORY session 開始注入（非實時）」；child「只含結果」| ❌ **無共享活記憶池** |
| agent **持續自我演化**（重複 trials 同 task）| workspace subagent = **單次 fan-out、異質任務、無狀態 worker** | ❌ |
| 「多樣性崩潰」病徵存在 | 無病徵證據；subagent 本就獨立 context、不互通 | ❌ 無證據支持 |
| bandit reward 模型（stationary、重複） | 跨 session 人工 MEMORY = 人類決策日誌，非 stationary reward 環境 | ❌ |

→ **4 條前提全不成立**。`MEMORY.md`（616 行）是**主對話/人類的跨 session 決策日誌**，不是「多 agent 共享的活記憶池」——兩者只是都叫「memory」，本質完全不同。DecentMem 解的是 persistent self-evolving MAS 的問題，**workspace 的 subagent 根本不是那種架構**。

### 2.2 結論
**DROP（不升為實作路徑）**。O(log T) regret 的理論最優性是針對 bandit 環境，與 workspace 場景無關。**保留為 archive reference**（已歸檔），但 EVOLUTION-QUEUE 的 observe 條目應誠實標註「前提證偽，不轉 apply」。無證據顯示 workspace 有多樣性崩潰；為不存在的問題重構 MEMORY.md = 過度工程典型。

---

## 3. 呼應週報 / 日報研究成果（研究脈絡定位）

> 這兩篇不是孤立論文——把它們放回本 session 的週報（2026-06-18）與日報（06-15~06-20）研究弧裡，verdict 會更穩固。

### 3.1 HarnessX 是「harness > 模型」研究弧的**第三幕**

本 session 週報深度報告已建立三證匯流，HarnessX 正好接在後面，形成完整論述弧：

| 幕 | 來源 | 命題 | 性質 |
|----|------|------|------|
| 一：harness **已是主體** | CC 逆向工程 98.4% 確定性（VILA-Lab 2604.14228）| 「AI 不需更聰明，需被管理」| 觀察 |
| 二：harness 差異**可量化** | Harness-Bench 2605.27922 同模型跨 harness **23.8pt** | 「報告 capability 須在 model–harness 層級」| 量測 |
| 三：harness **可自動演化** | **HarnessX 2606.14249 / AEGIS +14.5%** | 「harness = composable/evolvable first-class object」| 工程框架 |

**關鍵定位**：workspace 已經站在「第一幕」的勝局——它本身就是一個與 CC 同構的**手工但高品質 harness**（週報 §6.1 已 grep 接地）。HarnessX 的增量價值集中在「**第三幕的自動化演化**」，而那正是 workspace 缺基建的部分（§1.1）。
→ 所以 workspace 該擷取的是 HarnessX 的**理論層（九維分類 + seesaw 形式化，第一/二幕的結晶）**，**不是**演化機器 AEGIS（第三幕的重型實作）。**這個取捨完全由研究弧的位置決定，非主觀。**

### 3.2 DecentMem 與日報「borrowed intelligence」主軸**正交**——反而坐實 DROP

日報 06-19 三主題（treat-intelligence-borrowed / code-as-cache / code-economics-flip）收斂到一句話：**模型是借來的、隨時會因政策（Fable ban）或成本（GLM-5.2 1/6 價）消失；持久護城河 = 工程紀律（spec 品質 / behavioral test / observability）**（Charity Majors「AI 對工程紀律的要求不降反升」）。

- DecentMem 主張「**memory 架構**是 MAS 自我演化的護城河」——但日報指認的護城河是 **spec / gate / observability**，**不是** per-agent memory 機制。兩者層級不同。
- 更關鍵：日報的護城河全部是「**便宜、確定性、跨模型持久**」的東西（spec 是文字、gate 是 bash、observability 是 log）。DecentMem 的雙池 + LLM-as-judge reweight 是「**昂貴、隨機、綁特定 MAS 架構**」的機制——**與日報訊息方向相反**。
- → 日報研究成果**不支持**引入 DecentMem，反而強化「為不存在的多樣性崩潰問題重構 MEMORY = 違反 borrowed-intelligence 紀律」。

### 3.3 整體呼應：研究成果指向「操作化 > 自動化」

週報 + 日報的合成訊息是 verdict 的最強背書：

> **持久護城河 = 便宜的確定性紀律（checklist / gate / spec / observability），不是昂貴的自動化魔法。**

這條訊息：
- **支持** HarnessX 的「harness first-class」哲學 + 取其 cheap 結晶（九維 checklist / seesaw citation）；
- **反對** 投入建 AEGIS（把 harness 變成另一個需維護的重型隨機系統，違反 Charity Majors 紀律）；
- **反對** DecentMem 重構（昂貴、綁架構、解假想問題）。

§0 的 verdict（取 cheap 結晶、DROP 重型引擎）**主由 §1–2 轉移條件獨立成立，並獲週報/日報研究成果佐證**——非保守，是證據與脈絡雙重收斂。

---

## 4. 與本 session 既有帳本的一致性

- 本 session A3 曾把 HarnessX/DecentMem 加為 EVOLUTION-QUEUE **觀察候選**（標「前提不遷移、須重評」）。**本報告即該重評**：
  - HarnessX → 觀察候選降為「只取九維 checklist 小項，AEGIS 引擎 DROP」
  - DecentMem → 觀察候選**證偽**，建議標 closed（archive-only），不再佔 queue 注意力
- 與上份週報 §6 一致：harness 投資的正確方向是**操作化既有閘門**（checklist/citation），非引入需大基建的自動演化引擎。

---

## 5. 建議動作（若採納）

| 動作 | 目標檔 | 規模 | 處置 |
|------|--------|------|------|
| 九維 D1–D9 設計完整性 checklist + seesaw citation | `harness-meta` GOTCHAS/ref（非 auto-load）| ≤20 行 | 可做（待你確認）|
| EVOLUTION-QUEUE：DecentMem observe → closed（前提證偽）；HarnessX observe → 縮為 checklist 小項 | `research/EVOLUTION-QUEUE.md` | ≤6 行 | 可做（誠實化 queue）|
| AEGIS 引擎 / MEMORY 雙池重構 | — | 大 | **DROP** |

> 本報告為 report-only；上述動作需你確認後才執行（`.claude/` 與 queue 變更）。

---

_方法：讀一手 MD + PDF 歸檔（HarnessX 43pp / DecentMem 27pp）→ 主對話 grep 接地轉移條件（CLAUDE.md:3 / subagent-strategy:22 / measure.sh / harness-meta）→ fable-pilot 審閱。不採信論文 headline 為 workspace 增益。_

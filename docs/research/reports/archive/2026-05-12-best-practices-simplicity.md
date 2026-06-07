---
date: 2026-05-12
depth: D2
sources: research/papers/ + research/tweets/ + research/best-practices/
topic: "大道至簡 — Claude Best Practices / Cost & Efficiency Optimization"
verify: V1+V2
---

# 研究主題：大道至簡 — Claude Cost & Efficiency 最佳實踐

## 信度分層摘要

### [O] 官方 / Anthropic 一手資料

- **CLAUDE.md budget**: bcherny 明示 ≤60 行最佳，≤200 行上限。超過後模型注意力稀釋 → 有效規則密度下降。
- **Prompt Caching 五原則**（bcherny）：Static first, dynamic last；工具列表與模型 mid-session 不可改；`defer_loading: true` 保持 cache prefix 穩定。Cache hit = 0.1× 費率，write = 1.25× 費率。
- **Context Engineering**（Karpathy）：「填充恰好所需的資訊」是核心；too much context = 成本上升 + 品質下降，不是越多越好。
- **Output Discipline 實測**：英文 -80.6%、繁中 -86.2% 輸出 token，LLM Judge 品質無衰退（T-B/T-C/T-D 驗證 2026-04-30）。

### [C] 社群觀察（未官方確認）

- **Contextmaxxing vs Tokenmaxxing**（ashwingop/Sentra）：compiled memory 可減少 50–98% token；「right context > more context」。⚠️ 幅度數字為特定應用實測，不可直接套用。
- **Tool saturation**（nicbstme）：~20 工具飽和閾值；combined agents+MCP 約 15。超過後 routing 精度明顯下降。
- **AgentOpt**（P-tier 研究）：Weak planner + strong solver pattern → 13–32× 成本差距。
- **Context rot 閾值**（Thariq @trq212）：約 300–400k tokens 開始影響輸出品質。⚠️ 社群觀察，高度任務依賴。

### [E] 行業報告

- **DeepMind 多代理協調研究（2025）**：Baseline > 80% 加代理反降性能；Coordination Tax 在 ≥4 agents 飽和；Bag-of-Agents 17.2× 錯誤放大。

## 來源驗證結果

| Claim | 來源層 | 狀態 | 備注 |
|-------|--------|------|------|
| ≤60 行 optimal CLAUDE.md | O (bcherny) | ✅ confirmed | cc-workspace CLAUDE.md 81 行，超過但在 200 行預算內 |
| Prompt caching 0.1× hit rate | O (Anthropic docs) | ✅ confirmed | 官方定價頁 |
| -80.6% output token | O (內部實測) | ✅ confirmed | output-discipline.md 已實作 |
| Tool saturation ~20 | C (nicbstme) | ⚠️ unverified | 單一社群觀察，無 replications |
| Context rot 300-400k | C (Thariq) | ⚠️ unverified | 社群觀察，任務高度依賴 |
| 50-98% token 節省 | C (ashwingop) | ⚠️ unverified | 特定應用，幅度不通用 |

## 大道至簡核心發現

### 主論點

**加法思維是效率陷阱**。研究一致指向：更少的、更精確的 context > 更多的 context；更強的 prompt > 更多的 agent；更好的工具設計 > 更多的工具。

### 量化基準（本 workspace 套用）

| 指標 | 前（本次研究前）| 後（本次改動）| 來源 |
|------|----------------|--------------|------|
| subagent-strategy.md 行數 | 137 行 | 91 行 (−34%) | 本次 prune pass |
| Auto-loaded rules 總行數 | 348 行 | ~302 行 | 本次 prune pass |
| PermissionRequest 審計覆蓋 | 無 | 有 (audit-permission.sh) | 上一 session 補充 |
| Tool schema lint | 無 | 有 (session-init.sh) | 上一 session 補充 |
| Compact hint 指引 | 無 | 有 (context-management.md) | 上一 session 補充 |

### 大道至簡 Prune Test（應用於本 workspace）

**測試問題**：「移除這條規則，過去是否會發生具體失敗？」

| 移除內容 | Pass test? | 行動 |
|---------|-----------|------|
| 45% 規則完整表格（30 行）| ✅ 可移除 | 壓縮為 1 行摘要 + ref 指標 |
| 5D Coordination Layer 規格表 | ✅ 可移除 | 行為約束已在 7-row topology 表內 |
| 任務-拓撲匹配完整表格 | ✅ 可移除 | PlanCraft -39% 已在 Known Gotchas 保留 |
| "跳過 45% 量化" gotcha | ✅ 可移除 | 與壓縮後摘要重複 |
| 生產環境安全紅線 | ❌ 不可移除 | 高風險操作必要約束 |
| Git commit session URL 強制 | ❌ 不可移除 | 無 hook 時容易漏，hook 也依賴規則提醒 |
| Monitor 策略 | ❌ 不可移除 | 不設會造成長時間無回應 |

## 架構建議（下一步 / 非本次實作）

| 優先序 | 建議 | 預期效益 | 複雜度 |
|--------|------|---------|--------|
| A1 | Memory Layering：區分 session memory / project memory / global memory | 減少 session 載入 token | 中 |
| A2 | Semantic Compact hint 模板：為常見任務類型預建 compact hint | 減少 Lost-in-Middle 損耗 | 低 |
| A3 | AgentOpt 模式：識別 planner vs solver 分離點，降級 planner 模型 | 13–32× 成本差距 | 高 |

## 輸出建議

- 本次研究 → **已實作**（prune pass 完成，見上表）
- A1-A3 → **未來 session**，複雜度較高，需單獨規劃

---

*驗證：V1 self-check 完成（所有 claim 有標注）；V2 cross-check：output-discipline 實測數字來自同 workspace 驗證，可信度高。*

---

## 最終論（Final Pass）— 2026-05-12

三向平行 researcher（best-practices/papers/tweets）再次掃描，共發現 6 個候選 gap，advisor 逐項裁決：

| Gap | 裁決 | 原因（prune test）|
|-----|------|-----------------|
| CLAUDE.md 自更新 prompt suffix | REJECT | core.md 已有犯錯記錄原則；遞迴 meta-bloat |
| Permission Hook Opus 自動核准 | REJECT | solo interactive：Opus roundtrip 5–10s > 人工 1s；未來 batch 模式再評估 |
| Dreaming / Offline Learning | REJECT | 誤機制：dreaming 是 online agent，非 session-stop logger；人工 Known Gotcha = 正確替代 |
| `--from-pr` PR 恢復 | REJECT | CLI feature，非行為規則；需要時加入 playbook 即可 |
| Keep Rate 度量 | REJECT | logging ≠ closed-loop；solo workspace 無品質退化未被發現的歷史證據 |
| TSCG Tool Schema 壓縮 | DEFER | 觸發條件（>10 MCP tools）未滿足；條件滿足時重新評估 |

**Advisor meta-verdict**：優化已達穩態。下一條有價值的規則來自「實際使用中發現規則失效」，而非再一輪研究掃描。宣告大道至簡優化完成。

---

*🔄 overnight-research 驗證：2026-05-23 — 本文件為 workspace 內部分析（tweets/best-practices 本地資料），不依賴可即時更新的外部官方資料。狀態：已確認現行有效。*

---

## 2026-05-25 Re-check

> **方法**：對照 `.claude/rules/` 4 個 auto-load 規則的現狀，核查大道至簡原則在架構建議（A1–A3）的落地情況，並結合 `2026-05-25-papers-analysis.md` 新論文驗證核心主張。

### 已落地的建議（✅）

**核心主張驗證**
- ✅ CLAUDE.md ≤ 200 行上限：workspace CLAUDE.md 已控制在預算內（4 個 auto-load 規則 + 參照格式，符合 ≤200 行設計）
- ✅ Prompt Caching 三禁止：`context-management.md` 已明文（mid-session 禁止切換模型/工具/CLAUDE.md）
- ✅ Output Discipline 實測（英文 -80.6%、繁中 -86.2%）：`output-discipline.md` 已完整實作，無開場白 + 填充語禁止 + ≤150 字上限
- ✅ Compact 三層觸發（行為信號 > 數字閾值 > 定時器）：`context-management.md` 已落地
- ✅ Compact hint 格式（保留安全紅線 / 專案慣例 / 關鍵假設；捨棄中間詳情）：`context-management.md` 已明文
- ✅ PermissionRequest 審計（`audit-permission.sh`）：已在 hooks 目錄實作
- ✅ Tool schema lint（`session-init.sh`）：已在 hooks 目錄實作
- ✅ 「移除這條規則，過去是否會發生具體失敗？」剪枝測試：`core.md` §Framework Integrity 已制度化

**Prune Test 裁決追蹤**
- ✅ 生產環境安全紅線「不可移除」：`core.md` 已保留（GCP/TF/K8s 含 prod）
- ✅ Monitor 策略「不可移除」：`core.md` §長任務執行 已保留（Bash >30s → Monitor + run_in_background）
- ✅ Git commit session URL 強制「不可移除」：`core.md` §Git 工作流程 已保留

**架構建議（A1–A3）**
- ✅ A1 Memory Layering：`core.md` §長期記憶回路 雙層架構（Auto Memory + MEMORY.md）已落地；`refs/memory-layering.md` 已建立
- ✅ A2 Semantic Compact hint 模板：`context-management.md` 已有 compact hint 格式規範
- ⚠️ A3 AgentOpt（planner vs solver 分離）：`subagent-strategy.md` 已有模型分層（Haiku executor / Sonnet / Opus），但「降級 planner 模型」的系統化識別流程未完整落地

### 待追蹤的 gap（⚠️）

- ⚠️ **A3 AgentOpt 模式未完全落地**：`subagent-strategy.md` 的模型選擇以「獨立檔案數」為主要判斷依據（0–1 Haiku / 2–9 Sonnet / 10+ Sonnet/Opus），但 AgentOpt 的「強 solver + 弱 planner」模式（讓 Haiku/Sonnet 規劃，Opus 執行複雜決策）尚未系統化。2026-05-25 論文分析進一步驗證此模式：強模型當 Planner 在某些場景反而降低整體表現。
- ⚠️ **Tool saturation ~20 工具閾值仍未驗證**：本報告標注「⚠️ 社群觀察，無 replications」。截至 2026-05-25，workspace MCP server 數量持續增長（Google Drive、GitHub 等），但未追蹤當前實際 MCP tools 總數，不確定是否已接近 ~15（combined agents+MCP）飽和閾值。
- ⚠️ **TSCG Tool Schema 壓縮（DEFER 項目）**：最終論裁決「條件滿足時重新評估」。`2026-05-25-papers-analysis.md` 中 `tscg-tool-schema-compilation` 論文實測工具模式 52-57% token 節省（Phi-4 從 0%→84.4%）。隨 MCP 工具增長，此 DEFER 項目的評估條件（>10 MCP tools）可能已接近。需重新評估是否觸發。
- ⚠️ **Context rot 閾值 300-400k token（⚠️ 社群觀察）**：`context-management.md` 已採用此閾值作為「定時器」觸發條件，但本報告標注信度為 [C]（未官方確認）。2026-05 論文未提供更精確的實驗數據，仍需觀察。

### 新發現的最佳實踐補充（🆕）

- 🆕 **「right context > more context」獲論文級驗證**：本報告的核心主張「加法思維是效率陷阱」獲 2026-05-25 論文分析強力支持。`natural-language-agent-harnesses-2603-25723` 實測 NLAH 將 context 從 60.1K → 2.9K token（-95%），效能相當。「填充恰好所需資訊」不再只是經驗法則，而有論文級量化驗證。
- 🆕 **「Harness > 模型」對大道至簡的啟示**：論文分析的核心發現「Harness 配置效益超越模型升級」是大道至簡在 AI 編程領域最強的外部驗證：與其升級模型（花費）不如優化 CLAUDE.md + Hooks + Memory 設計（免費）。本報告的「加法思維是效率陷阱」獲得了更廣泛的框架支持。
- 🆕 **Bayesian 優化 vs 手工調優的量化反差**：`harbor-automated-harness-optimization` 論文：Bayesian 優化 9 個配置旗標明顯優於手工調優，且手工調優可能產生退化（-37%）。這是 A3 AgentOpt 模式的新佐證：planner/solver 分工的最優邊界不應靠直覺手工設定，而需要系統性搜索。
- 🆕 **`/goal` 命令作為大道至簡的工具化**：`/goal` 讓 Claude 迭代到達標（R4），減少人工介入的「你完成了嗎？」確認輪次。對需要多輪執行的任務，`/goal` 是 context 效率的提升工具（減少 prompt 往返）。與大道至簡原則高度契合：一次設定終止條件，而非多次手動 checkpoint。
- 🆕 **Sub-agent progress summaries 的 cache 命中（v2.1.128）**：長 agentic 任務的 cache creation token 成本降低約 3×。本報告 §量化基準表格應更新：原先計算 agentic 任務成本的基準假設已不再準確，實際成本低於估算。

### 2026-06-05 增量併入（窄 gap，1 條真補充）

> 此報告已多輪 re-check，gap 較窄。本次逐 2 篇候選論文校準：TSCG DEFER 無實質 gap（只更日期）、ACE brevity bias 1 條真 gap。

- 🆕 **「大道至簡」有下限：brevity bias 在 knowledge-intensive 任務反傷效能**（ACE / ICLR 2026，arXiv:2510.04618）：前代 context 適應方法普遍患 brevity bias——為精簡摘要而丟棄 domain-specific heuristics（verbatim："brevity bias, which drops domain insights for concise summaries"，2025-10-06-agentic-context-engineering…md L18）。ACE Key Takeaway #1：「Context adaptation ≠ context compression: Growing a structured playbook outperforms repeatedly rewriting and shrinking it」（同檔 L147）。**對大道至簡的精化**：去除 redundancy（✅ 正確）≠ 削減 domain insight（⚠️ 知識密集場景反降效能）。簡潔下限 = 保留 task-critical heuristics。⚠️ 接地警示：ACE −82.6% 是 KV cache **billed cost reduction**（同檔 L112，命中率 91.8%），**非** brevity/簡潔幅度，不可誤植為「精簡帶來 −82.6%」。
- **TSCG DEFER 現況**：條件門檻「>10 MCP tools」接近但未確認觸發——workspace MCP（Google Drive / GitHub）持續增長但未追蹤實際 tools 總數。論文數據（52–57% token 節省，Phi-4 0%→84.4%）前文已準確引用，無新 gap，僅更新 re-check 日期。

*Re-check 日期：2026-06-05 | 核心結論：「大道至簡」主張獲 2026 論文級驗證，A1/A2 已落地，A3 部分落地；新增 ACE「簡潔有下限」精化；TSCG DEFER 條件接近觸發（MCP 計數待確認）*

---

## 2026-06-05 增量併入（gap-vote 三技能共識，5 真 gap + 1 既有段佐證）

> **方法**：gap-vote（research-hub / overnight-research / autoresearch:reason 三角色並行）對近期 corpus（76 篇 md）找未併入 gap，2/3 共識 confirm + **主對話親自 grep 重驗每數字 + verbatim**（subagent verdict 非證據）。本報告分得「大道至簡 / 成本效率 / 模型選擇」相關 gap，集中於此段。

### 補充 A：Overthinking Tax——冗長輸出的經濟學接地（OckBench，arXiv:2511.05722）

**對「加法思維是效率陷阱」主論點的硬數據佐證**：本報告 §主論點主張「更少更精確 > 更多」，但偏經驗法則。OckBench 給出可量化的經濟學證據——**冗長有指數級成本懲罰**。

**接地審計**：
- Overthinking Tax / `57%` / `5.1×` ← "the counterintuitive finding that smaller reasoning models can be more expensive than larger ones due to excessive token generation. A 7B open-source model is 57% more expensive than a 14B model when total cost (accuracy × token efficiency) is considered. Open-source models generate 5.1× more tokens than proprietary models"（2025-11-07-ock-bench-reasoning-efficiency-overthinking-2511-05722.md L20）
- OckScore 指數懲罰 ← "**OckScore penalizes verbosity exponentially** — a model that doubles its token count must also significantly improve accuracy to maintain the same score."（同檔 L65）
- 5 個 overthinking 反模式（直接對應 output-discipline.md 禁令）← "Unnecessary Verification Loops / Exhaustive Case Enumeration / Hedge Cascades / Pre-Answer Preamble / Post-Answer Elaboration"（同檔 L115–L129）

**啟示**：output-discipline.md 的「無開場白 / 填充語禁止 / 精簡輸出」不只是風格偏好，而有**可量化經濟學依據**（Pre-Answer Preamble / Hedge Cascades 正是被禁的填充語）。⚠️ 57% / 5.1× 是「小開源推理模型 vs 大模型 / 專有模型」的對比，**非** Claude/Sonnet 自身數字；要點是「per-token 費率低 ≠ 總成本低」這個機制。

### 補充 B：AgentOpt UCB-E——A3「planner/solver 分離」的搜尋機制補完（arXiv 同 AgentOpt）

**對 §架構建議 A3 的直接補完**：本報告 L78/L149 已引 AgentOpt 的「13–32× 成本差距」+「手工調優產生退化（−37%）」，主張最優邊界不應靠直覺手設。但缺「那要怎麼系統性搜」的答案。UCB-E 補上：

**接地審計**：
- `62–76%` ← "The UCB-E algorithm achieves a 62–76% reduction in evaluation budget relative to brute-force search while recovering near-optimal accuracy."（2026-04-07-agentopt-client-side-optimization.md L22，再確認 L100）
- 模型須在 workflow 脈絡評估 ← "optimal model combinations often differ from predictions based on standalone model capability rankings, demonstrating that models must be evaluated in workflow context, not isolation."（同檔 L22）

**啟示**：A3 的「planner/solver 最優分離邊界」可用 bandit（UCB-E）以 62–76% 更少評估預算找到，而非窮舉或手調。但 workspace 為 solo interactive，A3 仍標「複雜度高、未來 session」——UCB-E 是「若要系統化時的機制」，非立即行動。⚠️ 62–76% 是 v2 結果；v1 的 Arm Elimination 為 24–67%（同檔 L100），引用須標版本。

### 補充 C：人寫 skill 遠勝自動學習——「人類 gate」是 simplicity 的一部分（SkillLearnBench，arXiv:2604.20087）

**對 skill 設計簡潔原則的實證**：

**接地審計**：
- `10.17%` / `74.50%` / `~30%` ← "Baseline (no skill): 10.17%. Human-authored skills: 74.50%. Automated skill-learning methods: ~30% (ceiling)."（2026-04-22-skill-learn-bench-continual-skill-learning-2604-20087.md L20）
- 64.3pp ceiling gap ← "The 74.50% → 10.17% gap (64.3pp) represents the current ceiling on automated skill learning"（同檔 L46）
- context-storage 抗遺忘 ← "Context-storage skill representations (skills as markdown files) are catastrophic-forgetting-resistant by design."（同檔 L133）

**啟示**：① 與 SkillsBench「自生成 skill −1.3pp」（見 auto-load-token 報告補充 5）一致——**workspace「人工建 skill + skill-evolution gate」決策獲雙論文背書**；② skill-as-markdown（`.claude/skills/*.md`，context-storage）設計被證為抗 catastrophic-forgetting，無需 fine-tune。⚠️ 74.50% 是特定 benchmark 的 human-authored 上界，不可泛化為「人寫 skill 永遠 7×於自動」；要點是**方向**（人工 gate > 全自動）。

### 補充 D：AHE observability——harness 改進需「結構化語意追蹤」非僅 logging（arXiv:2604.25850）

**對 §架構建議 / 測試能力的補充**：本報告以 healthcheck.sh 等手工 checklist 評 harness，但缺「系統性改進的可觀測性基礎」概念。

**接地審計**：
- `69.7% → 77.0%` ← "ten AHE iterations improved pass@1 from 69.7% to 77.0%, surpassing human-designed baselines."（2026-04-30-ahe-observability-driven-harness-2604-25850.md L24）
- 跨模型遷移 ← "Evolved harness transfers +5.1 to +10.1 pp gains across three alternative model families."（同檔 L24）
- observability 定義 ← "Observability is not just logging — it is structured semantic tracing that enables systematic harness improvement. Without observability, harness engineering is artisanal; with it, it becomes engineering."（同檔 L163）

**啟示**：呼應 autoload-evolution 閉環——harness 改進要可機械驗證（R4），「structured semantic tracing」是 OBSERVE 階段的學術接地。⚠️ 69.7→77.0% 是 Terminal-Bench 2 特定 benchmark + 10 iterations 的數字，非通用保證。

### 既有「ACE 簡潔有下限」段佐證（G13，非新條目）

§「2026-06-05 增量併入」的 ACE brevity bias 段（簡潔有下限）獲**第二篇獨立論文量化佐證**：beyond-context-window（arXiv:2603.04814）實測 **35:1 壓縮保留 broad topics 但失 specific facts / nuanced constraints**——正是 ACE「drops domain insights」的具體化。

**接地審計**：
- `35:1` 失 nuance ← "The 35:1 compression ratio preserves broad topics but loses specific facts and nuanced constraints — exactly the information that matters for accurate task completion."（2026-03-05-beyond-context-window-memory-vs-longcontext-2603-04814.md L91）
- 量化 + break-even ← "Long-context … outperforms memory-based compression by 33.4–35.2 percentage points in accuracy. However, memory becomes economically favorable after approximately 10 conversation turns at 100K token context sizes."（同檔 L20）

**啟示**：強化「簡潔下限 = 保留 task-critical heuristics」——壓掉 nuanced constraints（如安全紅線、per-project 慣例）會傷準確率 33.4–35.2pp。這正是 autoload-slimming 報告「只壓 TYPE C/D rationale，不碰 TYPE A 行為條文」下限的外部接地。

*增量併入日期：2026-06-05 | gap-vote 5 真 gap（OckBench / UCB-E / SkillLearnBench / AHE / 35:1-nuance）+ ACE 段佐證 | 全數主對話親自 grep 接地 | G13 掛既有 ACE 段非開新條目（語意去重）*

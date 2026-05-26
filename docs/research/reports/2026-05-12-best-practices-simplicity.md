---
date: 2026-05-12
topic: 大道至簡 — Claude Best Practices / Cost & Efficiency Optimization
sources: research/papers/ + research/tweets/ + research/best-practices/
depth: D2
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

*Re-check 日期：2026-05-25 | 核心結論：「大道至簡」主張獲 2026 論文級驗證，A1/A2 已落地，A3 部分落地，TSCG DEFER 條件接近觸發*

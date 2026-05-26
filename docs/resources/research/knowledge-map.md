# 跨源知識地圖

系統評估 16 個主題的研究覆蓋度、5 大跨來源共識、關鍵分歧點與未解問題。

> 建立時間：2026-05-01 | 最後更新：2026-05-23

---

## 16 個主題的覆蓋度評估

| 主題 | 覆蓋度 | 主要來源 |
|------|--------|---------|
| Orchestration Loop 設計 | ★★★★★ | Lilian Weng、Daily Dose DS、AHE 論文 |
| Tool/Function Calling | ★★★★★ | Masood、Trivedy、工具重寫論文 |
| Context Management | ★★★★★ | Chroma Context Rot、AHE、Thariq |
| Harness vs Model 分離 | ★★★★☆ | Building Agents 論文、Inside Scaffold |
| Memory 系統設計 | ★★★★☆ | Memory Survey 2603.07670、A-Mem、MemGPT |
| Verification/Evals | ★★★★☆ | Anthropic demystify-evals、LangChain |
| Prompt Caching | ★★★★☆ | Thariq、官方文件 |
| Sub-agent 架構 | ★★★☆☆ | Anthropic Engineering、Inside Scaffold |
| Security & Guardrails | ★★★☆☆ | 2506.08837、Anthropic secure deployment |
| CLAUDE.md/Rules 設計 | ★★★☆☆ | HumanLayer、Karpathy、FRAMEWORK.md |
| Benchmark 評估 | ★★★☆☆ | Terminal-Bench、SWE-bench |
| Harness 自動演化 | ★★★☆☆ | AHE、Meta-Harness |
| Formal Methods | ★★☆☆☆ | Categorical Architecture 2605.12239 |
| Cross-model 可移植性 | ★★☆☆☆ | NLAH 論文 |
| Enterprise Governance | ★★☆☆☆ | Anthropic April 23 Postmortem |
| Harness ROI 量化 | ★☆☆☆☆ | 分散在多篇，無統一框架 |

---

## 5 大跨來源共識

### 共識 1：Harness 影響超過模型大小

**量化依據**:
- Vesper 論文（2605.15221）：算法發現任務上，harness 結構變異佔 **40% 性能差距**；模型大小只佔 **30%**
- Adapting Interface, Not Model（2605.22166）：**95% 的模型適應效果**可在 harness 層實現，成本 2%

**各來源共識**:
- Terminal-Bench 2.0：同模型，不同 harness 的 13pp 差距
- LangChain：只改 harness（system prompt、tools、middleware、tracing、self-verification），讓 coding agent 從 Top 30 進到 Top 5
- Masood：企業 AI 失敗 65% 源自 harness 層缺陷，而非模型限制

**實踐結論**: Harness 是一級制約因子，不是模型的工具。結構最佳化報酬率 > 等待模型升級。

---

### 共識 2：Context 管理是決定性瓶頸

**量化依據**:
- Chroma Context Rot 研究：**18 個模型全部**隨 context 增長效能下降（NIAH benchmark）
- AHE 論文：12% 更少 token 達最佳成績
- Ewan Mak 實地案例（Claude Sonnet 4.6）：**58% → 81%**（23pp），改動主要在 context 架構

**實踐結論**: Sub-agent context firewall、prompt caching、compaction 策略不是優化項，是必要架構。

---

### 共識 3：Verification Loops 使品質提升 2-3×

**量化依據**:
- Daily Dose DS：Verification 能使品質提升 **2-3 倍**
- Anthropic Rajasekaran：Playwright UI 自動測試在 live environment 跑 integration tests
- Anthropic best practices：「給 Claude 驗證機制」是最高槓桿單一動作

**各來源共識**:
- Weng：Self-Reflection 是 Planning 的核心組件
- Eugene Yan：Evals pattern 是生產系統的基石
- Anthropic demystify-evals：「評估 agent 時評的是 model + harness，兩者不可分」

**實踐結論**: 沒有驗證迴路的 harness 不是 harness，只是 scaffolding。

---

### 共識 4：Ratchet 原則 — 每個失敗變成永久防護

**來源**:
- Mitchell Hashimoto（原話）：「Anytime you find an agent makes a mistake, you take the time to engineer a solution such that the agent never makes that mistake again.」
- Addy Osmani：「Every line in a good AGENTS.md should be traceable back to a specific thing that went wrong.」
- HumanLayer：CLAUDE.md + hooks 的 Ratchet 實踐

**實踐結論**: Harness 不是預先設計的，而是從失敗中沉澱出來的。

---

### 共識 5：工具設計是 Schema 語言工程

**量化依據**:
- Trivedy 論文（2602.20426）：工具描述的**措辭顯著影響** agent 成功率；提出自動化重寫工具 schema 和描述以提升可靠性

**各來源共識**:
- Weng：工具是超越訓練數據的能力擴展管道
- Masood：Tool/Function Calling 是 5 層 Control Plane 的第 2 層

**實踐結論**: 工具設計不只是功能問題，也是 schema 語言和描述精確度的工程問題。

---

## 分歧觀點

### 分歧 1：MCP 的投資報酬率

| 立場 | 來源 | 論點 |
|------|------|------|
| 保守 | Simon Willison | 不建議依賴 MCP；直接用 shell 命令更簡單和安全 |
| 積極 | HumanLayer、Masood | MCP 是能力擴展主要途徑，採用 A2A 協議標準化 |
| 務實 | FRAMEWORK.md | Bash + Read/Write + Glob 已覆蓋 90% 需求；MCP 有價值但不緊急 |

**核心差異**: Willison 優先安全隔離（Docker/Codespaces）；Masood 優先 context 效率與標準化。

---

### 分歧 2：Model 進步後 Harness 的演變方向

| 觀點 | 來源 | 預測 |
|------|------|------|
| Convergence（模型內化 harness 功能）| Trivedy | 某些 harness 功能會成為模型原生能力 |
| Substitution（簡單 harness 退場）| Anthropic Rajasekaran | V1 需要 sprint contracts，Opus 4.6 後不需要了 |
| Permanence（校準型 harness 永遠留著）| RESEARCH.md | Harness 解的是 non-determinism，不是 model 弱點 |

**深層分析**:
- 補弱點的 harness（early-stop、subagent for isolation）→ 隨模型進步消失
- 校準 non-determinism 的 harness（hooks、verification、planner-evaluator）→ 永遠留著

---

### 分歧 3：Verification 的自動化程度

| 立場 | 來源 | 方法 |
|------|------|------|
| 深度自動化 | Anthropic Rajasekaran | Playwright UI 自動測試，live interaction before scoring |
| 模型內評估 | Anthropic Young | Unit tests + browser automation |
| 輕量快速 | HumanLayer | Typecheck + lint + unit tests，只顯示 errors |
| 多層驗證 | Daily Dose DS | 規則型/視覺型/LLM-as-judge 三種層次 |

---

### 分歧 4：Harness 厚度（Thick vs Thin）

| 立場 | 來源 | 立場 |
|------|------|------|
| Thick（重型 harness）| Daily Dose DS、Masood | 11 組件完整架構；Control Plane 5 層 |
| Thin + 迭代（漸進式）| Building Agents 論文 | 從最簡 harness 開始，失敗後 Ratchet 增厚 |
| 隨模型簡化 | Daily Dose DS | 好的 harness 是臨時基礎設施，隨模型進步應下降 |

---

## 知識缺口（2026-05 評估）

### 缺口 P0：Harness 量化評估框架

**現狀**: Terminal-Bench 提供模型級基準，但無法診斷「特定 harness 的健康度」。

**建議**:
- 量化「context firewall 效率」（sub-agent 的中間輸出 vs 最終結論 token 比）
- 量化「Ratchet 累積度」（規則數量與覆蓋的失敗模式）

### 缺口 P0：Rule Escalation 決策樹

**現狀**: 「每個失敗要變成規則」的哲學清楚，但「何時升格為 hook vs 留在 CLAUDE.md」無明確指引。

**建議**: 建立決策樹：人工遵守率 × 違反成本 → 決定是否升格為 code 層 hook。

### 缺口 P0：基準評測污染危機（2026-05-23 新增）

**現狀**:
- DebugML「Cheating Agents」論文：業界排名前 20 的 agent 系統中 **67% 顯示基準污染信號**
- 污染類型：訓練集洩露、基準過擬合、評測集污染、結果後選擇性報告

**影響**: Terminal-Bench 等成績可能虛高 15-30 pp；部分跨來源比較數據可信度下降。

### 缺口 P1：Sub-Agent 委派的精確閾值驗證

**現狀**: 「≥10 檔案」「>20 工具呼叫」是啟發式規則，無量化驗證。Sub-agent 的「收支平衡點」（開銷 token vs 救回的 context rot token）尚未測量。

### 缺口 P1：Long-Horizon 的自動化進度追蹤

**建議**: 規範化 Progress 格式（JSON schema for `claude-progress.txt`）；自動偵測「premature completion」的 hook；Session 間自動驗證「新工作與舊工作無衝突」。

### 缺口 P2：Model 版本升級時 Harness 的遷移指南

**現狀**: April 23 Postmortem 顯示 harness 改動造成整體性下滑，但無升級新模型時的 harness 微調指南。

---

## 2026-05 新增主題

### Harness 作為範疇論架構（Categorical Theory Foundation）

**來源**: Harness as Categorical Architecture（2605.12239）

**核心洞見**:
- 工具 = 物件（Objects）
- 管道 = 態射（Morphisms）
- 組合 = 函子律（Functorial Composition）
- 形式驗證：harness chain 的正確性可通過範疇圖進行證明

### 五層 Runtime Substrate 分離關切

**來源**: Runtime Substrate（2605.13357）

| 層級 | 責任 | 範例 |
|------|------|------|
| **Invocation Layer** | Model ↔ Tool 介面 | Function call parsing、retry logic |
| **Context Layer** | 上下文可見性管理 | Compaction、windowing、injection |
| **Memory Layer** | 短期/長期狀態 | Session cache、vector DB、prompt cache |
| **Coordination Layer** | 工具編排與順序 | Pipeline routing、parallel execution |
| **Reflection Layer** | 自我監視與調適 | Error detection、performance metrics、rule learning |

**實踐結論**: 清晰分層減少耦合，提高可測試性；各層獨立優化不破壞他層。

---

## 延伸閱讀

- [Harness Engineering 研究全景](/resources/research/harness-engineering/)
- [延伸閱讀與參考資料](/resources/reference/)
- [Lecture 04：Harness 三層架構](/lectures/lecture-04-harness-architecture/)

# Confucius Code Agent: Scalable Agent Scaffolding for Real-World Codebases

**原始來源**：https://arxiv.org/abs/2512.10398  
**作者**：Sherman Wong 等 11 位（Harvard / MIT）  
**發表日期**：2025-12-11  
**評分日期**：2026-05-05

---

## 繁體中文全文摘要

### 研究背景與動機

現有軟體工程 Agent 在小型代碼庫表現尚可，但面對工業規模（數百萬行）的大型代碼庫時，因 context window 耗盡、工具可靠性不足、跨 session 記憶缺失等問題而失效。Confucius Code Agent（CCA）正是為解決這三大挑戰而設計。

### 系統設計哲學

CCA 以三個體驗軸為設計基礎，刻意解耦：

| 軸向 | 定義 | 實踐方式 |
|------|------|---------|
| **AX（Agent 體驗）** | Agent 能有效推理與行動 | 結構化壓縮記憶 |
| **UX（用戶體驗）** | 透明、可解釋的執行軌跡 | 詳細可讀的 trace logs |
| **DX（開發者體驗）** | 可觀測的推理與工具使用 | 評估機制與 observability |

### 四大核心功能

#### F1：Context 管理（階層式工作記憶）

當 prompt 長度接近閾值，「Architect」規劃者 Agent 會摘要關鍵資訊類別，同時保留最近的原始歷史。這使系統能在工業規模代碼庫上執行長期軟體工程任務。實驗顯示，context 管理讓 Claude 4 Sonnet 的解決率提升 **+6.6 個百分點**。

#### F2：持久筆記（跨 Session 學習）

專用 Agent 將執行軌跡提煉為持久 Markdown 筆記，包含：
- 成功策略記錄
- 失敗模式的「後見之明筆記」（hindsight notes）

跨 session 重跑任務時，token 成本降低約 11k（~11%），解決率提升 **+1.4 個百分點**。

#### F3：模組化擴充（工具組合）

文件編輯、CLI 執行、程式碼搜尋等工具組件透過型別化回調（typed callbacks）連接到 orchestrator，實現模組組合與清晰的關注點分離。

#### F4：Meta-Agent（自動構建）

Meta-Agent 透過「構建—測試—改進」循環，自動合成提示詞與配置。這是一個自我優化層，根據評估反饋不斷精煉 Agent 本身。

### 效能結果（SWE-Bench-Pro）

| 模型 | CCA 結果 | 對比基準 |
|------|---------|---------|
| Claude 4 Sonnet | 45.5% | SWE-Agent 42.7% |
| Claude 4.5 Sonnet | 52.7% | Live-SWE-Agent 45.8% |
| Claude 4.5 Opus | 54.3% | 達到商業系統水準 |

**關鍵洞見**：弱模型 + 強 scaffold > 強模型 + 弱 scaffold。Scaffolding 的品質比底層模型能力更具決定性。

### 對 Workspace 的啟示

1. **Context 壓縮不是優化而是基礎**：CCA 的 Architect 摘要模式與 cc-workspace 的 `/compact` 策略高度一致，可借鑒其「關鍵資訊分類摘要 + 保留近期原始歷史」的雙層結構。
2. **持久筆記作為跨 Session 記憶**：類似 `auto-memory` 機制，但 CCA 更明確地將「失敗模式」也寫入筆記，值得納入 session-learner skill。
3. **Meta-Agent 自動優化**：與 harness-eval skill 的「Ratchet 評分」理念相通，未來可考慮引入自動化 prompt 優化循環。

---

## 評分摘要

| 維度 | 分數 | 理由 |
|------|------|------|
| A. Workspace 可行動性 | 8/10 | context 分層壓縮、持久筆記、Meta-Agent 三個模式均可直接應用於 cc-workspace 設計改善 |
| B. 創新性 | 7/10 | 「後見之明筆記」和 Meta-Agent 自動優化是新穎概念；但整體仍在既有 scaffold 框架範圍內 |
| C. 證據品質 | 8/10 | SWE-Bench-Pro 量化結果，有 ablation study（+6.6pp context、+1.4pp memory），可重現 |
| D. 技術深度 | 8/10 | 四大功能有具體機制描述，AX/UX/DX 三軸解耦哲學有明確實踐方式 |
| E. 泛化性 | 7/10 | 針對大型代碼庫設計，但 context 管理和持久記憶模式可廣泛應用 |
| **加權總分** | **7.65/10** | 8×0.3 + 7×0.2 + 8×0.2 + 8×0.15 + 7×0.15 = 2.4+1.4+1.6+1.2+1.05 |

**整合決策**：Rule  
**整合位置**：`.claude/rules/core.md`（持久筆記模式）或 `.claude/refs/session-management.md`（context 分層策略）  
**整合狀態**：待實作

**TODO**：
- 將「hindsight notes（失敗模式）」概念加入 session-learner skill
- 參考 Architect 摘要模式優化 context-monitor-table.md 的分層觸發策略

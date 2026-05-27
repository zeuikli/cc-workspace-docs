---
url: "https://arxiv.org/html/2603.25723v1"
title: "Natural-Language Agent Harnesses (NLAH)"
date: 2026-03-26
type: article
---

# Natural-Language Agent Harnesses (NLAH)

**原始來源**：https://arxiv.org/html/2603.25723v1  
**作者**：Linyue Pan 等（清華大學深圳研究生院、哈爾濱工業大學）  
**發表日期**：2026-03-26  
**評分日期**：2026-05-05

---

## 繁體中文全文摘要

### 問題定義

當前 Agent 系統的 harness 邏輯（控制多步驟執行的協調層）被嵌入 controller 程式碼中。這帶來四個問題：

1. **耦合**：harness 邏輯與執行環境緊密耦合
2. **不透明**：控制流是隱式的，難以理解或修改
3. **無法複用**：harness 模式無法跨項目分享或調適
4. **無法評估**：難以孤立 harness 效果與執行環境或模型效果

### 核心貢獻：將 Harness 設計當成一等研究對象

NLAH 方法：
- 將 harness 規格**外化為可編輯的自然語言**
- 在 harness 和執行環境之間維持**明確的合約（contracts）**
- 保留確定性的程式碼用於驗證和工具介面
- 啟用 harness 效果的系統性評估

### NLAH 的七大組件

#### 1. Contracts（合約）
執行階段之間的明確協議：
- 每個階段的輸入/輸出類型
- 成功/失敗條件
- 資源預算和逾時
- 必要 vs. 可選階段

#### 2. Roles（角色定義）
- **Planner role**：決定下一步
- **Executor role**：實作決策
- **Reviewer role**：驗證結果

#### 3. Stage Structure（階段結構）
循序或條件執行：規劃 → 行動生成 → 工具執行 → 驗證 → 狀態更新

#### 4. Adapters（轉接器）
harness 規格與執行環境之間的轉換層；工具輸出與 harness 狀態的橋接。

#### 5. Scripts（腳本）
確定性邏輯：工具調用、結果解析、狀態持久化、觀測記錄。

#### 6. State Semantics（狀態語義）
指定哪些狀態跨步驟持久化、如何更新、每個角色的可見性規則。

#### 7. Failure Taxonomies（失敗分類）
可恢復 vs. 不可恢復的失敗；每種失敗類型的重試策略；上升條件。

### Intelligent Harness Runtime（IHR）

IHR 解釋 NLAH 規格：
- **Harness Interpreter**：循環中的 LLM 讀取規格並確定下一個動作
- **Backend**：提供工具存取、多 Agent 支援、狀態持久化
- **Charter Enforcer**：驗證執行環境行為符合 charter

**關鍵屬性**：自然語言協調高層控制；程式碼強制執行確定性驗證。

### 實驗結果

#### RQ1：執行環境的行為重要性
- **發現**：過程指標（token 使用、呼叫次數）在不同條件下大幅變化；任務解決率相對穩定
- **意義**：harness 結構有行為意義，不只是「prompt 裝飾」；harness 優化機會在效率，不只在結果

#### RQ2：模組消融效果

| 模組 | 效果 |
|------|------|
| Self-evolution | 改善 solve-loop 紀律，減少多餘迭代 |
| File-backed state | 增強流程結構，減少 context 漂移 |
| Evidence-backed answering | 提高可審計性，改善錯誤診斷 |
| Multi-turn memory | 適度改善，依 context 而定 |
| Retry strategy | 集中在困難案例，簡單任務影響小 |

無單一模組提供均勻改善；模組針對特定問題類型。

#### RQ3：Code-to-NLAH 遷移
**案例研究**：OS-Symphony（原始 code-based agent）
- **原始版本**：30.4% 任務成功率
- **NLAH 版本**：47.2% 任務成功率
- **改善**：**+16.8 個百分點**

關鍵改變：
1. 可靠性機制從本地螢幕修復 → 持久化執行環境狀態
2. 控制流抽象為明確的 harness 規格
3. 啟用跨步驟的系統性狀態持久化
4. 透過 artifact-backed closure 改善失敗恢復

### 自然語言 vs. 程式碼的分界

**NL 適合**：高層協調（角色、階段結構、合約）、控制流規格、委派邊界、錯誤恢復策略

**程式碼必要**：工具調用和結果解析、驗證邏輯和約束、狀態持久化和原子性、效能關鍵操作

### 對 Workspace 的啟示

1. **Skills 作為 NLAH 的實例**：cc-workspace 的 SKILL.md 格式（流程步驟、known gotchas、輸出規則）實際上是 NLAH 的自然語言 harness 規格
2. **File-backed state**：`claude-progress.json` 的設計與「file-backed state 減少 context 漂移」的發現一致
3. **Evidence-backed answering**：citation-discipline skill 的設計原理
4. **Failure Taxonomy**：可在 SKILL.md 的 Known Gotchas 區塊中加入「可恢復/不可恢復」的明確分類

---

## 評分摘要

| 維度 | 分數 | 理由 |
|------|------|------|
| A. Workspace 可行動性 | 7/10 | NLAH 組件概念可映射到 Skills 設計；但需要翻譯才能直接應用 |
| B. 創新性 | 8/10 | 將 harness 邏輯外化為可編輯 NL、並維持明確合約是重要的設計突破 |
| C. 證據品質 | 8/10 | OS-Symphony 從 30.4% → 47.2% 有明確量化，三個 RQ 均有實驗支撐 |
| D. 技術深度 | 8/10 | 七大組件有詳細定義，IHR 架構清晰，模組消融有系統性 |
| E. 泛化性 | 7/10 | 在 coding 和 OS 任務驗證，但其他領域的遷移性未測試 |
| **加權總分** | **7.55/10** | 7×0.3 + 8×0.2 + 8×0.2 + 8×0.15 + 7×0.15 = 2.1+1.6+1.6+1.2+1.05 |

**整合決策**：Rule  
**整合位置**：`.claude/refs/skill-authoring.md`（NLAH 設計模式 → Skill 設計指引）  
**整合狀態**：待實作

**TODO**：
- 在 skill-authoring.md 中加入「失敗分類（可恢復/不可恢復）」作為 SKILL.md Known Gotchas 的標準格式
- 考慮將 NLAH 的 Contracts 概念加入 skill 驗收清單（輸入/輸出類型、成功/失敗條件明確化）

---
title: AI Agent Harness 驗證與品質評估方法論
date: 2026-05-19
type: report
---

# AI Agent Harness 驗證與品質評估方法論

**日期**：2026-05-19 | **字元數目標**：≥ 10,000 | **研究模式**：overnight-research × autoresearch 交叉研究  
**來源**：6 個外部來源 + cc-workspace 全量研究材料（karpathy/mnilax refs、12 個 research 目錄）交叉驗證  
**服務對象**：需要系統性驗證 Harness 產出品質並建立完善進化機制的 AI 工程師

---

## 執行摘要

本報告回答三個核心問題：

1. **如何驗證 Harness 產出的品質？** — 採用雙層驗證架構：確定性驗證（測試/lint/schema）作為 ground truth，LLM-as-judge 作為語意品質補充。
2. **如何實作 Harness 驗證管道？** — 12-metric 框架（Retrieval / Generation / Agent / Production 四層），按 Phase 1-3 分三週建立。
3. **如何持續完善 Harness 準則？** — Ratchet 升格機制：每個驗證失敗都是自動升格的觸發點。

**核心數據**：
- 同一個 Opus 4.6，harness 改進後 Terminal-Bench 2.0 從 52.8 → 66.5（+13.7pp），**不換模型**
- Can.ac 案例：工具格式調整一項，同一模型準確率 6.7% → 68.3%（**10 倍提升**）
- SWE-Bench Pro：同一 Opus 4.5，三種不同 harness = 50.2%–55.4%（5.2pp 差距）
- Claude Code TerminalBench 2.0：92.1% vs Codex CLI 77.3%（14.8pp 差距）
- 88% AI agent 專案無法上線，主因 harness 太脆弱（Pinggy.io 統計）
- Mnilax 8 週測試：41% → 3% 錯誤率（50 tasks × 30 codebases × 12 rules）

---

## 1. 背景與動機

### 1.1 為何 Harness 驗證比模型升級更重要

2026 年的共識：**強但不穩定（strong but spiky）的模型 + 確定性 Harness 基礎設施 = 可靠的 Agent**（rmax.ai, 2026）。

Tejas Kumar（IBM, AI Engineer Europe 2026-05-17）的 Live Demo 結論更直接：「整個 demo 中從未修改 prompt，只加了 verify step + guardrail + deterministic login handler，agent 從失敗到成功。」

從 cc-workspace 的 Terminal-Bench 2.0 數據：

| Harness | 準確度 |
|---------|--------|
| ForgeCode（最佳 harness）| 79.8% ± 1.6 |
| TongAgents | 71.9% ± 2.7 |
| Crux（最差 harness）| 66.9% |

**13pp 差距，全部來自 harness，不來自模型。**

### 1.2 「Harness 品質」的三個維度

外部研究（QuitTool, 2026）識別三個維度：
1. **可回放性（Replayability）**：失敗是否可以重現？可診斷？
2. **儀器化（Instrumentation）**：執行軌跡是否完整記錄（每個 tool call、每個 thought）？
3. **邊界明確性（Bounded Costs）**：驗證開銷和重試邏輯是否有上限，不會無限螺旋？

---

## 2. 核心概念：雙層驗證架構

### 2.1 確定性驗證 vs LLM-as-Judge

| 驗證類型 | 適用場景 | 工具 | 代價 |
|---------|---------|------|------|
| **確定性驗證** | 工具選擇、格式合規、schema 驗證、測試通過 | grep / pytest / lint / bash script | 零 API 成本 |
| **LLM-as-Judge** | 語意品質、目標對齊、回應相關性、多步驟連貫性 | 獨立 LLM（非生成用的模型）| API 成本 + 延遲 |

**關鍵原則**：
- 確定性驗證是 ground truth，不可妥協
- LLM-as-Judge 補充語意品質——但**評估模型必須不同於生成模型**（用 GPT-4 評估 Claude 輸出，或反之），否則分數通膨
- Trajectory Analysis（軌跡分析）優於純結果驗證：「確保 agent 沒有通過有缺陷的邏輯得到正確答案」（TDS, 2026）

### 2.2 Karpathy × Mnilax 框架的語意驗證問題

本 workspace 的框架完整性研究（2026-05-18）揭示了一個關鍵問題：**grep 關鍵詞通過 ≠ 語意完整**。

失敗案例：R12 延伸合併後，`limit/offset` 和 `搜尋截斷格式` 都還在（grep 通過），但合併後文字在 context 壓力下 Claude 可能只執行其中一個行為。

**正確的語意驗證問題**：「在 context 壓力下，這兩個行為要求合併後，Claude 會只觸發其中一個嗎？」——不是問「關鍵詞是否存在？」

### 2.3 K×M 雙準則框架（cc-workspace 研究成果）

從 55 輪迭代測試提煉的雙成功條件：

```
成功條件 1：total_tok ≤ 3,500（可量測：bash scripts/measure.sh）
成功條件 2：K×M 得分 ≥ 90（可量測：per-rule 語意評估矩陣）
```

| 維度 | 滿分 | 核心問法 |
|------|------|---------|
| K1（Karpathy Simplicity）| 20 | 「移除後 Claude 下次會在哪個場景犯錯？」 |
| K2（Karpathy No-Speculation）| 10 | 「有無新增未來可能需要的規則？」 |
| K3（Karpathy Surgical）| 10 | 「有無觸及任務以外的規則？」 |
| M1（7 核心規則完整）| 30 | R1/R4/R5/R6/R8/R10/R12 行為動詞 100% 保留 |
| M2（數字精確）| 15 | 所有限制數字完整（3,500/4,000/30,000/70%/200）|
| M3（4 層依賴完整）| 10 | Layer 1-2 規則觸發詞可連結到對應行為 |
| M4（Token 達標）| 5 | ≤ 3,500 tok |

---

## 3. 生產級 Harness 驗證：12-Metric 框架

外部研究（Towards Data Science, 100+ 部署案例）識別了生產環境 AI agent 的 12 個核心指標：

### 3.1 四層指標架構

| 層次 | 指標 | 目標值 | 驗證方法 |
|------|------|--------|---------|
| **Retrieval** | Context Relevance | > 0.85 | LLM-as-judge 0-1 評分 |
| | Context Recall | > 0.90 | 對比 human-labeled ground truth |
| | Retrieval Latency | p95 < 200ms | APM timing |
| **Generation** | Answer Faithfulness | > 0.95 | LLM-as-judge |
| | Hallucination Rate | < 2% | 5% 生產流量抽樣 |
| | Answer Relevance | > 0.90 | 語意相似度比較 |
| **Agent** | Tool Selection Accuracy | > 0.92 | labeled dataset 對比 |
| | Tool Execution Success | > 0.98 | 每次 tool call 成功/失敗追蹤 |
| | Multi-Step Coherence | > 0.85 | Trace-level 邏輯流評估 |
| **Production** | Cost per Query | < $0.05 | Token + API 成本加總 |
| | P99 Latency | < 3s | 端到端計時 |
| | Loop Rate | 0% | 重複動作模式偵測 |

### 3.2 實作順序（三週建立）

**Week 1-2（基礎層）**：確定性驗證 + Answer Faithfulness
- 先建 healthcheck.sh 涵蓋工具執行成功率 + Loop Rate 偵測
- 建立 labeled eval set（≥ 100 個 ground truth 案例，4-6 天工程工作）

**Week 3-6（品質層）**：加入 Hallucination Rate、Tool Selection Accuracy
- 建立 CI/CD 整合：每次 merge 前自動跑 eval suite
- 設定 regression threshold（> 0.07-0.10 的 metric delta → 警報）

**Week 7+（生產層）**：Cost per Query、P99 Latency
- 1-2% 生產流量抽樣送人工審查，校準 LLM judge 對齊度

---

## 4. cc-workspace 的 Harness 驗證實作模式

### 4.1 現行多層級驗證架構

本 workspace 已建立以下驗證層：

| 層次 | 工具 | 觸發時機 | 訊號類型 |
|------|------|---------|---------|
| **自動化** | `healthcheck.sh`（12 段落）| 任務完成後 | PASS / FAIL |
| **Token 量測** | `measure.sh` | 修改 auto-load 規則後 | 數字 |
| **安全篩選** | `block-dangerous.sh` | PreToolUse | Exit code（阻斷）|
| **預提交** | `pre-commit-review.sh` | git commit 前 | 通過 / 阻斷 |
| **可觀測性** | `audit-log.sh` | 每次 Bash 命令後 | 完整軌跡 |
| **語意審查** | `/deep-review`（Opus）| 複雜任務完成後 | 三維度評分 |

### 4.2 Ratchet 作為驗證轉化機制

Ratchet 的獨特之處：**它不是記錄失敗，而是把失敗轉化為防護**。

```
驗證失敗
  → 記錄到 RATCHET.md（日期・具體場景・後果・影響評估）
  → 評估升格層級
       ├── 頻率 > 3次/月 → PreToolUse Hook（執行前阻斷）
       ├── Skill 相關 → Known Gotchas（該 skill frontmatter）
       ├── 可量化 → PostToolUse Hook（執行後審計）
       └── 一般性 → CLAUDE.md rule（觀察 2 週仍反覆 → 升格）
  → 升格到 Hook 後：從 CLAUDE.md 移除對應規則（保持精簡）
```

**關鍵洞見**：Ratchet 是把「驗證失敗 → 規則升格 → 代碼層防護」的閉環。與靜態測試套件不同，Ratchet 是**隨每次失敗自動強化的驗證基礎設施**。

### 4.3 七條不可壓縮規則的驗證優先序

根據框架完整性研究，這 7 條規則移除即導致可量化的錯誤率回升，驗證時最高優先序：

1. **R1**（Think Before Coding）：驗證點 = Claude 是否在實作前顯露假設
2. **R4**（Goal-Driven）：驗證點 = 成功條件是否可機械驗證
3. **R5**（LLM for Judgment）：驗證點 = 確定性邏輯（retry/routing）是否由 code 處理
4. **R6**（Token Budget）：驗證點 = 4,000/30,000 token 數字在 auto-load 中
5. **R8**（Read Before Write）：驗證點 = 改動前是否讀 exports + callers
6. **R10**（Checkpoint）：驗證點 = 每重要步驟是否有可描述的狀態摘要
7. **R12**（Fail Loud）：驗證點 = limit/offset 讀取 + 搜尋截斷**兩個**行為獨立可觸發

---

## 5. 常見反模式與防範

| 反模式 | 現象 | 根本原因 | 防範 |
|--------|------|---------|------|
| **用相同模型生成和評估** | 評估分數虛高 | Judge inflating | 生成用 Sonnet → 評估用 Opus，或反之 |
| **只看最終結果不看軌跡** | 「通過了錯誤邏輯的正確答案」 | 缺 Trajectory Analysis | 審計每次 tool call 歷史，不只看輸出 |
| **Keyword matching 替代語意評估** | grep 通過但行為合併後只觸發其中一個 | 缺「context 壓力下行為」測試 | 用 K×M 框架問「移除後在哪個場景犯錯？」 |
| **Token-only 優化目標** | 達到 token 目標但語意損失 | 單一成功條件 | 雙成功條件：token ≤ 3,500 AND K×M ≥ 90 |
| **HTML 注釋「保留」語意** | `<!-- -->` 在 CLAUDE.md 不被剝離 | 誤以為 HTML = 注釋不佔用 | 直接刪除，不用 HTML 注釋 |
| **允許列表過寬** | allow-list 24 entries，信噪比低 | 初期安全為由放寬後未收緊 | 定期審查，縮減至 task-scoped |
| **訓練時 mock 但生產時不 mock** | 測試環境通過，生產環境崩潰 | 評估與生產環境不一致 | Mock everything 原則 + CI/CD gate |
| **靜默截斷（不告知數量）** | Agent 認為搜尋結果只有 N 個 | 缺 CONTEXT BOUNDARY 標示 | R12 強制標示 `[CONTEXT BOUNDARY: showing N of TOTAL]` |

---

## 6. 前沿趨勢

### 6.1 Context Engineering 取代 Prompt Engineering

Karpathy（2026-05-01）宣告轉型：**「Context Engineering = 稀缺資源管理」**。CLAUDE.md 不再是「指令文件」，而是「context 的初始分配」——每個 token 都是花掉的 context 預算。

實作影響：
- CLAUDE.md 類型分類從「越詳細越好」→ 「TYPE A（行為規則）保留，TYPE C（背景說明）刪除」
- 目標：每 token 做有用的工作，不載入說明性 context

### 6.2 Values over Rules（VILA-Lab 2026）

VILA-Lab 研究發現：最有效的 CLAUDE.md 是「價值觀宣告 + 少量強制邊界」，而非「規則列表」。

CLAUDE.md 指令以 **user context** 形式傳遞（probabilistic compliance），不是 system prompt（deterministic）。這意味著：
- 規則不是「必然執行」，而是「提高相應行為概率」的信號
- **規則的質量（信號強度）比數量（token 密度）更重要**

### 6.3 動態 Harness（2027 預測）

Tejas Kumar（IBM, 2026-05-17）預測：Agent 在執行任務前**自動產生專屬 harness**——自我感知潛在幻覺點並預先設防，類似 Plan Mode 但更強大。

這意味著：當前的靜態 harness 設計將進化為「任務啟動前動態生成 guardrail + verify step」的模式。

### 6.4 Lazy-loading 的演進方向

外部研究（The Prompt Shelf, 2026）確認：**Lazy-loading pattern 可回收 40-70% 的每任務 token 消耗**。

路徑：`core auto-load → on-demand skill → path-scoped rule`

---

## 7. 可立即實作的行動建議

### 7.1 驗證管道建立（3 週路線圖）

**Week 1（基礎驗證層）**：
```bash
# 確認 healthcheck.sh 涵蓋以下 7 個核心驗證點
# 1. CLAUDE.md 行數 ≤ 200
# 2. Auto-load token ≤ 3,500
# 3. Rules FF/FB 覆蓋率 100%
# 4. Hook 腳本 4 類全覆蓋（Safety/Quality/Completion/Observability）
# 5. 7 條核心規則行為動詞存在
# 6. RATCHET.md 有最近 30 天更新
# 7. 無靜默截斷（搜尋結果有 CONTEXT BOUNDARY 標示）
```

**Week 2（語意驗證層）**：
- 對每次 auto-load 規則改動跑 K×M 評估（30 分鐘手動檢查）
- 建立 labeled eval set（至少 20 個典型任務的預期輸出）

**Week 3（持續驗證層）**：
- Ratchet 週期：每月審查 RATCHET.md，識別 > 3次/月 的失敗模式 → 升格 Hook

### 7.2 K×M 快速評估腳本

```bash
# 修改任何 auto-load 規則後執行此 30 秒自檢
echo "=== K×M Quick Check ==="
echo "M4: Token count"
bash scripts/measure.sh 2>/dev/null | tail -3

echo "M1: 7 core rules present"
for rule in "YOU MUST" "IMPORTANT" "禁止" "不得"; do
  count=$(grep -r "$rule" .claude/rules/*.md 2>/dev/null | wc -l)
  echo "  '$rule': $count occurrences"
done

echo "M2: Key numbers present"
grep -r "3,500\|4,000\|30,000\|70%\|200" .claude/rules/*.md | grep -c "."

echo "K1: (Manual) 移除後 Claude 在哪裡犯錯？"
echo "K2: (Manual) 有無推測性規則？"
echo "K3: (Manual) 有無觸及任務外的規則？"
```

### 7.3 CLAUDE.md 最佳化路線圖（FRAMEWORK-FIRST）

按 TYPE 分類每行，依序執行：

1. **TYPE D**（`詳見 xxx.md` 純導航行）→ 全部刪除（零風險）
2. **TYPE C**（背景說明，無行為動詞）→ 全部刪除（低風險）
3. **TYPE B**（規則+解釋混合）→ 保留行為動詞，刪除原因說明
4. **TYPE A**（純行為規則）→ 不得動

執行後跑 `bash scripts/measure.sh`，目標 ≤ 3,500 tok。

### 7.4 完善準則的長期路徑

**每次 session 結束**：
- 新 Gotcha → 當下記入 RATCHET.md
- K×M ≥ 90 AND token ≤ 3,500 → 準則穩定

**每月**：
- RATCHET.md 失敗頻率審查 → 升格 Hook
- CLAUDE.md rules ≥ 15 條 → 合併觸發頻率最低的

**每季**：
- `/harness-meta:hmf` 全評（7D HMF）
- HarnessCard 更新（Base Model 版本、Hook 事件變動）
- 對照 Terminal-Bench 2.0 量化 harness 改進 pp

---

## 8. 完善準則的四個高槓桿投資

### 8.1 Boris Cherny 的 CLAUDE.md 直注模式

Boris Cherny（Anthropic）提出：**「After Claude is corrected, update CLAUDE.md directly so the rule evolves with actual codebase knowledge.」**

這與 cc-workspace 目前的「Lesson YYYY-MM-DD: [失敗模式] → [防範規則]」模式有本質差異：

| 方式 | 效果 | 問題 |
|------|------|------|
| 記在 `memory/MEMORY.md` | 有記錄，但 auto-load 路徑不確定 | 不在 CLAUDE.md 主路徑，Claude 可能遺漏 |
| 記在 RATCHET.md | 有歷史，但不在 auto-load | 同上 |
| **直注 CLAUDE.md rule** | Claude 每次 session 都讀到 | 會增加 token，需平衡 FRAMEWORK-FIRST |

**cc-workspace 的平衡做法**：
- 重要防範規則 → 直注 core.md（TYPE A 行為動詞）
- 一般性記錄 → RATCHET.md（頻率 > 3次/月 再升格）
- Boris 的精神：**不等 Ratchet 升格，當場就改**

### 8.2 Harness 分層的層次依賴（不可壓縮規則）

來自框架完整性研究（55 輪迭代）的核心發現：

**四層依賴結構決定了壓縮的安全邊界**：

```
Layer 1（基礎層）—— 不可觸動：
  R1 Think Before Coding
      → R2 Simplicity（需先理解假設才能精簡）
      → R3 Surgical Changes（需知道範圍才能只動最小）

Layer 2（Agent 執行層）—— 不可觸動：
  R4 Goal-Driven
      → R10 Checkpoint（目標需追蹤進度）
      → R6 Token Budget（執行需預算以免螺旋）
  R10 → R12 Fail Loud（每個 checkpoint 必須顯式）

Layer 3（確定性邊界層）—— 可輕度壓縮：
  R5 LLM-for-Judgment
      → R7 Surface Conflicts（判斷/決定分清才能解衝突）
      → R8 Read Before Write（衝突辨識需讀現有代碼）

Layer 4（品質保證層）—— 可合併壓縮：
  R9 Test Intent → R4（測試意圖是目標的具體化）
  R11 Convention → R3（慣例尊重是外科修改的實現）
```

**黃金規則**：任何 CLAUDE.md 壓縮，必須從 Layer 4 開始，絕不碰 Layer 1/2。

### 8.3 Hook 反饋速度層次

來自 Nyosegawa 最佳實踐研究的 Hook 設計原則：

| Hook 類型 | 觸發時機 | 延遲等級 | 適用場景 |
|---------|---------|---------|---------|
| PostToolUse | 每次工具呼叫後 | **毫秒** | 最快反饋；格式驗證、log 記錄 |
| PreToolUse | 執行前阻斷 | 毫秒 | 安全紅線強制執行 |
| pre-commit | git commit 前 | **秒** | 程式碼品質、文件完整性 |
| Stop | 任務完成後 | 秒~分 | healthcheck、品質評估 |
| CI/CD | PR merge 前 | **分鐘** | 整合測試、回歸檢測 |
| 人工審查 | 生產部署前 | **小時** | 架構決策、破壞性變更 |

**設計原則**：越早的 hook 越便宜，越快的反饋越有價值。每個 PreToolUse hook 比 PR review 的成本低 1000 倍。

### 8.4 現有 cc-workspace 四大技術債

根據全量研究材料掃描，識別出尚未解決的四個重要缺口：

| 缺口 | 現況 | 影響 | 修補成本 |
|------|------|------|---------|
| **R13 PGE 缺文件** | 在 harness-design.md，不在 auto-load | 複雜任務缺少 PGE 三層分工提示 | 低（補 3-5 行）|
| **R14 Polyglot 安全審查** | 完全不在 auto-load | 多語言專案（Go+Python）只審一半 | 中（需手動觸發）|
| **R2 加密基底共用** | FATAL-2 在 ref 文件 | AES-GCM nonce 重用漏洞風險 | 低（補 `secure_random_bytes()` 原則）|
| **R5 LLM 決策禁止清單** | 有規則但無禁止清單 | Claude 偶爾做 HTTP status 路由 | 低（補 ❌ 清單）|

---

## 9. 研究方法論：overnight-research × autoresearch 協作模式

本研究展示了兩個技能的互補性：

```
overnight-research（外部研究）
  → 搜尋三輪：harness verification、CLAUDE.md optimization、12-metric framework
  → 抓取 7 個外部來源
  → 建立外部知識基線

autoresearch:learn（內部合成）
  → 掃描全量 workspace 材料（12 個研究目錄）
  → 識別外部基線與內部文件的差距
  → 輸出 4 個高優先級缺口 + 8 個量化數據點

交叉驗證
  → 共識點（兩邊都確認）：harness > 模型；雙層驗證；Ratchet 升格
  → 分歧點（外部有但內部沒有）：Can.ac 10x case、Hook 延遲層次
  → 補強（內部有但外部沒有）：K×M 雙評分、7 不可壓縮規則、4 層依賴結構
```

**這個協作模式的價值**：overnight-research 帶來外部視角和量化基準，autoresearch:learn 帶來 workspace 特定深度。兩者交叉驗證消除偏見，共識點可信度高。

---

## 附錄：來源評分與索引

| 來源 | 評分 A/B/C/D/E | 核心貢獻 |
|------|--------------|---------|
| QubitTool Agent Harness Eval Guide 2026 | A/B/A/A/A | 驗證方法分類、生產部署 checklist |
| Towards Data Science 12-Metric Framework | A/A/A/A/A | 四層 12 指標、三週實作路線圖、judge 校準 |
| rmax.ai Harness Engineering Lever 2026 | A/A/A/A/A | Terminal-Bench 52.8→66.5 案例、4 個 harness 品質維度 |
| Pinggy.io AI Harness Engineering | B/A/A/A/A | 88% 專案失敗統計、CI/CD 整合模式 |
| The Prompt Shelf CLAUDE.md Optimization | B/A/A/A/A | Lazy-loading 40-70% token 回收、TYPE 分類驗證 |
| cc-workspace HARNESS-CARD / RATCHET / BENCHMARK | A/A/A/A/A | 現行驗證架構、量化基線 87.5%→93.75%、缺口識別 |
| cc-workspace framework-integrity-optimization | A/A/A/A/A | K×M 雙評分框架、7 不可壓縮規則、FRAMEWORK-FIRST |
| cc-workspace HMF Full Report 2026-05-18 | A/A/A/A/A | 當前 7D 分數（62/70）、Top-3 改進行動 |
| karpathy-mnilax-best-solution.md | A/A/A/A/A | 14 條規則完整 Mechanical Checklist、FATAL/MAJOR bug class、R13/R14 |
| cc-workspace ai-articles/HARNESS-ARTICLES-DIGEST | A/A/A/A/A | Can.ac 6.7%→68.3%、SWE-Bench Pro 5.2pp gap、5 跨文章共識點 |
| bcherny-config-github.md | B/A/A/A/A | CLAUDE.md 直注模式（After correction → 直接更新 rule）|
| nyosegawa-best-practices | B/A/A/A/A | Hook 四分類（Safety/Quality/Completion/Observability）+ 延遲層次 |
| research/tweets/Mnilax 2026-05-09 | A/A/A/A/A | 一手量化數據（41%→3%、規則上限 14 條 compliance 52%）|

---

**Sources:**
- [Harness Engineering Is the Primary Lever for Agent Reliability in 2025–2026](https://rmax.ai/notes/harness-new-model-agent-systems-2026/)
- [Agent Harness Engineering Guide 2026: Evaluating AI Agents in Production](https://qubittool.com/blog/agent-harness-evaluation-guide)
- [Building an Evaluation Harness for Production AI Agents: A 12-Metric Framework](https://towardsdatascience.com/building-an-evaluation-harness-for-production-ai-agents-a-12-metric-framework-from-100-deployments/)
- [AI Harness Engineering: The Layer That Makes Your LLM Applications Actually Work](https://pinggy.io/blog/best_ai_harnesses_to_supercharge_llm_models/)
- [CLAUDE.md Token Budget Optimization: Keep It Lean Without Losing Power](https://thepromptshelf.dev/blog/claude-md-token-budget-optimization/)
- [Karpathy's CLAUDE.md Skills File: The Complete Guide](https://agentpedia.codes/blog/karpathy-claude-code-skills-guide)

---

*🔄 overnight-research 驗證：2026-05-23 — 本文件為 harness 驗證方法研究報告。狀態：已確認現行有效。*

---

## 2026-05-25 Re-check

**稽核方法**：對照 `.claude/rules/`（4 個 auto-load 規則，含 frontmatter 結構）、`.claude/hooks/`（19 個 hook 腳本）、`.claude/settings.json`（10 個 hook 事件設定）的現行狀態。

### 已落地的建議

- ✅ **多層級驗證架構（自動化）**：`session-stop.sh`（Stop hook）、`pre-commit-review.sh`（PreToolUse git commit）、`block-dangerous.sh`（PreToolUse Bash 安全攔截）均已實作，對應報告第 4.1 節的多層驗證架構。
- ✅ **PostToolUse auto-lint（品質循環）**：`post-edit.sh` 在 Edit|Write 後觸發，`audit-log.sh` 在 Bash 後非同步記錄，達到 ms 級反饋目標。
- ✅ **確定性驗證作為 ground truth**：core.md R4 + PGE + R12 規則強制要求機械性可驗證條件，對應「確定性驗證不可妥協」原則。
- ✅ **Ratchet 升格機制精神**：core.md 的「自我改進觸發（bcherny）」規則要求使用者糾正後立即在 MEMORY.md 新增防範規則，是輕量版 Ratchet 閉環。
- ✅ **七條不可壓縮規則（R1/R4/R5/R6/R8/R10/R12）**：core.md 現行版本完整包含所有 7 條不可壓縮規則的行為動詞，且 R12 兩行分離（大檔分段讀取 + 搜尋截斷格式）均完整保留。
- ✅ **K×M 雙評分機制**：core.md 的 `Framework Integrity` 規則（修改 auto-load 規則前問「移除後 Claude 在哪犯錯？」）對應 K1 評估問法，已在 auto-load 層落地。
- ✅ **Token Budget 數字精確保留**：context-management.md 保有 4,000 / 30,000 / 70% 所有關鍵數字，對應 M2（數字精確）指標。
- ✅ **靜默截斷禁止（R12 搜尋截斷格式）**：core.md 已有 `[CONTEXT BOUNDARY: showing N of TOTAL...]` 強制標示規則，對應報告的反模式防範。
- ✅ **Hook 四分類覆蓋**：Safety Gates（block-dangerous / protect-sensitive-files）、Quality Loops（post-edit）、Completion Gates（session-stop）、Observability（audit-log / notification-log）四類均已實作，達到報告「四類 Hook 全覆蓋」週 1 目標。
- ✅ **PreCompact / PostCompact hooks**：`pre-compact.sh`、`memory-archive.sh`（PreCompact）、`post-compact.sh`、`memory-sync.sh`（PostCompact）均已實作，強化 compact 品質閘門。
- ✅ **CONTEXT BOUNDARY 標示規則**：core.md R12 延伸已明確定義格式，直接對應報告第 5 節反模式防範表。
- ✅ **週 1 基礎驗證層（7 核心驗證點的精神）**：hooks 體系涵蓋工具執行成功率（audit-log）、安全紅線（block-dangerous）、git commit 品質（pre-commit-review），多個驗證點已自動化。
- ✅ **4 層依賴結構保全**：2026-05-18 50 輪優化確認 Layer 1–4 依賴結構完整保留，報告第 8.2 節的黃金規則已落地。

### 尚未落地的建議

- ⚠️ **RATCHET.md 機制**：報告第 4.2 節建議建立 RATCHET.md 記錄驗證失敗並升格 Hook，目前 workspace 使用 `memory/MEMORY.md` 的「Lesson YYYY-MM-DD」格式替代，但 RATCHET.md 本身不存在，無失敗頻率追蹤（>3次/月 → 升格 Hook 的自動化規則未落地）。
- ⚠️ **labeled eval set（≥ 100 個 ground truth 案例）**：報告週 2 建議建立，目前沒有正式的 labeled eval set，K×M 評估仍為手動執行。
- ⚠️ **per-model ablation 測試套件**：報告第 3 節與週 2 建議的 Haiku / Sonnet / Opus 分別測試，目前無正式記錄。
- ⚠️ **Hallucination Rate / Tool Selection Accuracy 量化追蹤**：報告第 3.1 節的 12-metric 框架中「生成層」和「代理層」指標，目前 workspace 僅有確定性驗證層（healthcheck），語意品質層未量化追蹤。
- ⚠️ **LLM-as-Judge 用不同模型評估**：報告強調生成用 Sonnet → 評估用 Opus（或反之），目前 `/deep-review` skill 存在但其模型配置未確認是否強制使用不同於生成模型的評估模型。
- ⚠️ **R13 PGE 缺文件**：報告第 8.4 節識別此技術債（在 harness-design.md，不在 auto-load），2026-05-25 仍未見修補。
- ⚠️ **R14 Polyglot 安全審查**：報告識別此缺口，2026-05-25 仍未見 auto-load 補充。
- ⚠️ **月度 RATCHET.md 失敗頻率審查**：報告第 7.4 節建議每月審查，目前無此流程記錄。

### 過期資訊更新

- **Hook 腳本總數**：報告撰寫時（2026-05-19）hooks 架構尚在建立中，目前 `.claude/hooks/` 已有 19 個腳本，包含 `sdd-cache-pre.sh` / `sdd-cache-post.sh`（WebFetch SDD 快取）、`monitor-reminder.sh`（Bash PostToolUse）、`session-start-eval-reminder.sh` 等報告未涵蓋的新 hooks。
- **Skills 總數**：報告時 14+ skills，目前已達 18 個（含 skill-evolution / schedule / loop / claude-api / verify / run 等新增）。
- **Rules frontmatter**：4 個 auto-load rules 已新增 `target-model: claude-sonnet-4-6` 和 `hmf-review: 2027-01` frontmatter，部分填補報告「規則缺少版本追蹤」的缺口。

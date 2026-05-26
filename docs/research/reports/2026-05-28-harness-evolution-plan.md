# Harness 自我進化四層次：工作執行計畫

**日期**：2026-05-28
**字元數目標**：≥ 10,000 字
**觸發來源**：@arvin17x「需要自進化的不是 Agent，而是 Harness」（2026-05-27）
**研究分支**：claude/harness-evolution-research-XEBIa
**類型**：overnight-research — 完整研究 + 實作計畫

---

## 執行摘要

Arvin Xu（@arvin17x）在 2026-05-27 的文章中提出了一個範式轉移的核心命題：在 2026 年的 AI 產品競爭中，「模型 + Harness」才是真正的產品，而 Harness 本身也必須具備自我進化的能力。文章以 LobeHub 的 Error Pattern 自動巡檢系統作為具體案例，展示了從 L1（全人工）到 L3（Agent 主導）的進化歷程，並描繪了 L4（Agent 自主優化 Context 策略）的未來形態。

本計畫以此為基礎，結合 cc-workspace harness 的現況（CAR 評分 13.0/14、PASS 101/WARN 2/FAIL 0），提出四個層次的具體工作執行計畫，每個層次都包含：可驗證的實作步驟、測試方法（PGE 三層）、評估指標，以及可機械性確認的完成條件。

---

## 1. 背景與動機：為什麼 Harness 必須是活的？

### 1.1 範式轉移的核心邏輯

在早期 AI 產品競爭中，Benchmark 分數主導了使用者對模型能力的認知。但 Arvin Xu 指出，到 2026 年邊際效應遞減——在日常任務中，模型間的差距不再是主要瓶頸。真正決定產品體驗上限的，是 **Harness 的設計品質與自我進化能力**。

這個觀點與 cc-workspace 積累的研究結論高度吻合：

- **Terminal-Bench 實驗**：同一個 Claude Opus 4.6，不同 Harness 的成功率相差 13 個百分點（66.9% vs 79.8%）
- **MindStudio 基準**：GPT-5.5 在不同 Harness 環境下功能性評分相差 25.7 pp（61.5% vs 87.2%）
- **LobeHub 案例**：透過 Error Pattern 自動巡檢（Harness 層優化），Agent 成功率從 75% 提升至 95%+

這三個數據點共同指向同一個結論：**投資 Harness 設計的報酬率，遠高於等待新模型版本**。

### 1.2 Harness 即作業系統：類比的深層含義

文章把 Harness 類比為作業系統（模型 = CPU，Context Window = RAM，Harness = OS）。這個類比有幾個深層含義需要展開：

**靜態 OS 的天花板**：一個不更新的 OS 無論有多快的 CPU，都無法充分發揮硬體潛力。在 2024 年設計的 Harness 規則，很可能在 2026 年 Q2 的新模型上成為負擔——LangChain 在一年內重構三次架構、Manus 六個月重構五次，都印證了這個規律。

**自適應 OS 的價值**：如果 OS 能根據應用程式的使用模式自動調優（如 Linux 的 CFS 調度器、macOS 的 App Nap），則應用程式開發者無需手動介入底層。Self-Evolving Harness 的目標正是讓「Harness 工程師」從「每天盯日誌」轉變為「設定目標，審查邊界」。

**信號密度的護城河**：文章指出，Consumer Product 每天數萬次 Agent 執行帶來的信號密度，是自部署方案（數十次/日）無法比擬的。這意味著進化速度本身成為競爭優勢——反饋閉環快一個數量級，Pattern 庫飽和所需時間就少一個數量級。

### 1.3 Tracing 是一切的前提基礎設施

文章最重要的技術洞見之一是：**Tracing 必須是設計時的一等公民，而非後裝功能**。

主流 Agent Framework 的痛點：

```
LangChain：callback 可選，忘了注册就丢 trace
CrewAI：事件監聽器掛在事件總線，事件丟失 = trace 斷裂
OpenAI Agents：需要顯式建立 trace，不自動傳播
AG2：middleware 可選安裝，不裝就零 tracing
```

這些框架的共同問題是把 Observability 當作「後加功能」，而不是「執行的副產品」。

LobeHub 的解法：狀態機模型 + 單步執行原則，讓 `run step = event boundary`，每個步驟天然就是一個 trace event。這個設計決策不只是技術選擇，更是 Self-Evolving 能力的基礎設施投資。

在 cc-workspace 的 Harness 架構中，對應的機制是 `audit-log.sh`（PostToolUse）+ `failure-log.sh`（PostToolUseFailure）+ `notification-log.sh`（Notification）。這三個 hook 共同構成了本 workspace 的「黑匣子」基礎設施。但目前這些 log 的分析仍依賴人工查看，尚未進入「Trace -> Pattern -> Auto-Fix」的閉環，正好對應 L2 到 L3 的進化缺口。

---

## 2. 核心概念：Harness 自進化四層次詳解

### 2.1 L1：全人工（Manual）

**定義**：人發現問題 -> 人分析根因 -> 人修復 -> 人驗證

**特徵**：
- 錯誤發現依賴使用者回報或工程師偶然觀察
- 分析週期：數天到數週
- 修復品質：取決於個別工程師的知識與當下注意力
- 可覆蓋的錯誤模式：僅限已知或高頻問題

**現況評估（cc-workspace）**：
cc-workspace 在 2026-04-30 之前的狀態基本處於 L1。RATCHET.md 記錄的早期 Ratchet 條目（pre-compact.sh 缺乏保護、block-dangerous.sh 為 deny-list 策略）都是靠人工發現並手動修復的。

**L1 的根本限制**：
正如文章所言，「錯誤產生的速度高於人工分類的速度，未歸類錯誤就會不斷堆積」。當 cc-workspace 接入更多工具、運行更多任務時，純人工的 L1 模式會導致以下問題：

1. **認知負擔過重**：工程師（也就是使用者本人）需要同時是 Agent 的操作者和 Harness 的維護者
2. **長尾問題累積**：低頻但高影響的 bug（如 `healthcheck.sh` 的 `import yaml` 依賴問題）可能在特定環境下才觸發，純人工觀察很難事前發現
3. **進化速度受限**：Harness 的改進週期等於工程師的有效工作時間，而非系統的運行頻率

### 2.2 L2：Agent 輔助（Agent-Assisted）

**定義**：Agent 找出可疑問題，人確認，再讓 Agent 執行部分修復

**特徵**：
- Agent 自動分析 trace log，提出候選問題清單
- 人工介入：確認問題的優先序和修復方向
- Agent 執行：程式碼修改、測試運行、結果匯報
- 人工最終審查：approve 或 reject Agent 的修復方案

**在 cc-workspace 的體現**：
`harness-meta:audit` skill（5 階段 Diagnose -> Ratchet-Log 流程）是目前最接近 L2 的實踐。它讓 Agent 自動執行 healthcheck、分析 scorecard 缺口、提出修復建議，但每個修復動作都需要使用者明確確認。

**L2 的進化條件**：
- Tracing 基礎設施必須就位（否則 Agent 無從分析）
- 問題分類規則必須事先定義（讓 Agent 知道「用戶側錯誤」vs「Harness 自身 bug」的邊界）
- 修復建議格式必須結構化（讓人工審查的認知成本最小化）

**L2 的典型工作流程**（以 cc-workspace 為例）：
```
1. Agent 讀取 command-log.jsonl + failure-log.jsonl
2. Agent 按錯誤類型分桶（hook 失敗 / 工具呼叫錯誤 / 模型推理問題）
3. 對照 RATCHET.md 中的已知模式，識別新的錯誤類型
4. 生成修復建議報告（Markdown，含影響評估 + 建議 Ratchet 層級）
5. 使用者審查並選擇要執行的修復
6. Agent 執行修復、跑 healthcheck、提交 commit
```

### 2.3 L3：Agent 主導（Agent-Led）

**定義**：Agent 主導大部分流程；採集數據 -> 識別模式 -> 修改代碼 -> 提交 PR -> 跑驗證。人仍保留關鍵判斷（根因歸屬、修復方向、高風險決策）

**特徵**：
- 端到端自動化：從數據採集到 PR 提交無需人工介入
- 人工介入點：高風險修復（影響生產行為、修改 Context 策略等）才需要確認
- 驗證是內建的：Agent 在提交前必須自行運行測試和 healthcheck
- 閉環速度：小時級（而非天/週級）

**LobeHub 的 L3 實踐**（7 步驟巡檢）：
```
Step 1：從後台拉取 error records，多維度分桶
Step 2：對比已有 ERROR_PATTERNS，識別新模式
Step 3：用戶側錯誤 vs Harness 自身 bug 分類
Step 4：直接更新匹配 Pattern（用戶側）
Step 5：commit -> push -> 開 PR
Step 6：刪除 Dashboard 中匹配新 pattern 的歷史噪音
Step 7：Harness 自身 bug 做根因分析，建立修復 Task
```

**量化結果**：9 輪巡檢後，Error Pattern 從 31 增長至 104 並趨於飽和；Agent 成功率從 75% 提升至 95%+；自主發現 20+ Harness 自身缺陷。

**cc-workspace 的 L3 目標狀態**：
透過自動執行 `harness-meta:audit` 的定期巡檢（可透過 Routines/排程觸發），結合 `audit-log.sh` 的累積數據，達到：
- 新錯誤模式在 24 小時內被識別
- 低風險修復（Known Gotchas 更新、RATCHET.md 條目新增）無需人工確認
- 高風險修復（hook 邏輯修改、CLAUDE.md 規則變更）仍需人工 approve

### 2.4 L4：Agent 自主優化（Autonomous Optimization）

**定義**：Harness 能持續觀察自己的運行狀態，發現可改進點，提出修復，經人確認後執行並驗證；人只需設定目標、審查邊界和處理少數高風險決策

**特徵**（文章描述）：
- Agent 主動優化 Context Engine 的策略
- Agent 調整 Tool schema 的兼容層
- Agent 預測和預防錯誤（而非事後修復）
- Harness 自己進化自己，人只需設定目標

**額外能力**（文章描述的「我們正在構建的未來」）：
- **Agent Level 自動進化**：每個 Agent 在夜間自動回放當天 Tracing，分析失敗模式，自我調整 Prompt 和執行策略
- **用戶 Level 自動進化**：識別用戶使用模式，自動更新生成提示詞與 Persona 記憶
- **全局 Eval Harness**：每個 Failed Task 自動進入評估 -> 歸因 -> 修復閉環

**L4 的技術前提**：
- 完整的 Trace 基礎設施（已在 LobeHub 實現）
- 結構化的 Context Strategy 規格（讓 Agent 知道「好的 Context 策略」的量化標準）
- 沙盒驗證環境（修改 Context/Tool schema 前可在隔離環境測試）
- 回滾機制（每次自動修復都有可靠的回滾路徑）
- 人工確認閘門（高風險決策仍需人工審批）

**批判性評估**：
文章承認「生產系統不能因為自進化就繞開權限、審查和回滾」，但未詳述如何實作這些邊界。這是 L4 最大的工程挑戰——自動化程度越高，每個未覆蓋的邊界情況就越危險。cc-workspace 在達到 L4 之前，需要先建立完整的沙盒驗證和回滾機制。

---

## 3. 現況診斷：cc-workspace Harness 的四層次定位

### 3.1 當前層次評估：L2.5

基於 HARNESS-CARD 和 eval-2026-05-25 的數據，cc-workspace 目前處於 **L2 與 L3 之間的過渡狀態**（L2.5）：

| 維度 | 評估 | 層次 |
|------|------|------|
| 錯誤發現 | audit-log.sh 自動記錄，但分析仍靠人工觸發 | L2 |
| 模式識別 | RATCHET.md 手動維護；harness-meta:audit 部分自動化 | L2 |
| 修復執行 | Agent 可執行，但需人工 approve 每個步驟 | L2 |
| 驗證機制 | healthcheck.sh 完整（PASS 101/WARN 2/FAIL 0） | L3 |
| 自動提交 | quick-commit / 手動 git add + commit | L2 |
| 定期巡檢 | 無自動排程（monthly-reports-cleanup 是唯一 routine） | L1 |
| Context 策略優化 | 全人工（基於 RATCHET.md 的歷史記錄） | L1 |

### 3.2 主要缺口（Gap Analysis）

**G1：缺乏自動化的 Trace 分析流水線**
- 現況：`command-log.jsonl`、`failure-log.jsonl` 存在，但無自動分析腳本
- 影響：錯誤模式的識別仍需人工閱讀 log 檔
- 優先級：P0（是 L3 的基礎）

**G2：缺乏定期自動巡檢的排程**
- 現況：`harness-meta:audit` 需要使用者手動觸發
- 影響：問題發現週期等於使用者記憶力，而非系統的運行頻率
- 優先級：P0

**G3：Context 策略無量化指標**
- 現況：compact 觸發閾值是靜態的（70%），但無法知道是否真正有效
- 影響：Context 策略優化缺乏方向感
- 優先級：P1

**G4：Tool schema 變更沒有兼容性測試**
- 現況：修改 skill 的 `allowed-tools` frontmatter 無自動回歸測試
- 影響：Tool schema 改動可能靜默破壞現有能力
- 優先級：P1

**G5：沒有沙盒環境做 L4 的危險自動修復**
- 現況：所有修復直接在 workspace 執行
- 影響：L4 的某些自動修復可能對生產環境造成不可逆影響
- 優先級：P2（L4 達成前需解決）

---

## 4. 工作執行計畫：四個層次的實作路徑

### 4.1 L1 -> L2 遷移計畫：建立自動化 Trace 分析基礎設施

**目標**：讓 Agent 能夠讀取 Trace 數據並生成可操作的分析報告，無需人工手動瀏覽 log 檔

**工期估計**：2-3 天

#### Step 1.1：建立 Trace 分析腳本

**檔案**：`scripts/analyze-traces.sh`

**功能**：
```bash
# 讀取最近 N 條 command-log.jsonl 記錄
# 按事件類型分桶（bash_command / tool_call / hook_event）
# 識別 failure-log.jsonl 中的失敗模式
# 輸出結構化報告（JSON + Markdown）
```

**具體實作**：
```bash
#!/bin/bash
# analyze-traces.sh - Trace 分析腳本
# 用途：分析 audit-log 和 failure-log，識別錯誤模式

DAYS=${1:-7}  # 預設分析最近 7 天
OUTPUT_DIR="/tmp/claude-scratch/trace-analysis"
mkdir -p "$OUTPUT_DIR"

# 1. 讀取 audit log
AUDIT_LOG=".claude/logs/command-log.jsonl"
FAILURE_LOG=".claude/logs/failure-log.jsonl"

# 2. 按時間篩選
SINCE=$(date -d "-${DAYS} days" +%Y-%m-%d 2>/dev/null || date -v-${DAYS}d +%Y-%m-%d)

# 3. 分桶分析（錯誤類型 / 工具名稱 / 頻率）
python3 scripts/trace-analyzer.py \
  --audit "$AUDIT_LOG" \
  --failure "$FAILURE_LOG" \
  --since "$SINCE" \
  --output "$OUTPUT_DIR/analysis-$(date +%Y%m%d).json"

# 4. 生成 Markdown 報告
python3 scripts/trace-reporter.py \
  --input "$OUTPUT_DIR/analysis-$(date +%Y%m%d).json" \
  --ratchet "research/agent-harness/RATCHET.md" \
  --output "$OUTPUT_DIR/report-$(date +%Y%m%d).md"

echo "分析完成：$OUTPUT_DIR/report-$(date +%Y%m%d).md"
```

**測試方法**：
1. 執行 `bash scripts/analyze-traces.sh 7`
2. 驗證輸出包含：錯誤統計、按類型分桶結果、新模式識別（與 RATCHET.md 比對）
3. 成功條件：`ls /tmp/claude-scratch/trace-analysis/report-*.md | wc -l` ≥ 1

**評估指標**：
- 腳本執行成功率（目標：100%，任何 log 格式問題都應給出明確錯誤訊息）
- 分析報告的可讀性（由使用者評分，1-5 分，目標 ≥ 4 分）
- 識別的新 Pattern 數量（與手動閱讀 log 的結果對比）

#### Step 1.2：建立 L2 分析 Skill

**檔案**：`.claude/skills/trace-audit/SKILL.md`

**功能**：把 Step 1.1 的腳本封裝成 skill，讓 Agent 可以在 harness-meta:audit 流程中自動調用

**觸發詞**：`trace-audit`、`分析 trace`、`trace 巡檢`

**Skill 流程**：
```
Phase 1：執行 analyze-traces.sh，讀取分析結果
Phase 2：對照 RATCHET.md，識別新的錯誤模式（新 = 未在 RATCHET.md 中的模式）
Phase 3：按風險等級分類修復建議（低風險：Known Gotchas 更新；中風險：rule 新增；高風險：hook 修改）
Phase 4：生成結構化的修復建議報告（含具體 Ratchet 層級建議）
Phase 5：等待使用者確認後執行修復（或直接執行低風險修復）
```

**測試方法**：
1. 手動製造一個已知錯誤場景（如執行一個被 block-dangerous.sh 攔截的命令）
2. 執行 `/trace-audit`
3. 驗證報告包含：正確識別此錯誤類型 + 正確分類為「hook 攔截（預期行為）」
4. 成功條件：報告不將預期行為誤判為需要修復的問題

**評估指標（PGE 三層）**：
- **Generator**：trace-audit skill 執行
- **Evaluator**（分離）：reviewer agent 評估報告的準確性
- **成功標準**：False Positive Rate（誤判預期行為為 bug）< 5%；False Negative Rate（遺漏真實問題）< 10%

#### Step 1.3：整合 L2 進入 harness-meta:audit 流程

**修改**：在 harness-meta:audit 的 Phase 1（Diagnose）中增加 trace-audit 的自動執行

**整合點**：
```
harness-meta:audit Phase 1（現有）：
  - healthcheck.sh
  - measure.sh
  - token budget 計算

harness-meta:audit Phase 1（新增）：
  - analyze-traces.sh（最近 7 天）
  - 識別新 Pattern
  - 補充到 Diagnose 報告
```

**完成條件**（可機械性驗證）：
```bash
# 執行 harness-meta:audit 後，確認輸出包含 trace 分析節
grep -l "Trace 分析" /tmp/claude-scratch/*.md | wc -l  # ≥ 1
```

### 4.2 L2 -> L3 遷移計畫：建立自動化定期巡檢閉環

**目標**：建立定期自動執行的 Harness 巡檢，低風險修復不需人工確認，高風險修復自動建立確認請求

**工期估計**：3-5 天

#### Step 2.1：建立 Harness 巡檢 Routine

**機制**：利用 cc-workspace 的 Routines 功能（`/schedule`）建立排程觸發

**排程**：每天 00:00（台北時間）執行

**巡檢流程**（對應 LobeHub 的 7 步驟）：
```
Step 1：數據採集
  - 讀取最近 24 小時的 command-log.jsonl
  - 讀取最近 24 小時的 failure-log.jsonl
  - 計算 healthcheck.sh 的趨勢（PASS/WARN/FAIL 變化）

Step 2：模式識別
  - 執行 analyze-traces.sh（最近 1 天）
  - 對比 RATCHET.md 的已知模式
  - 識別 ≥ 2 次出現的新模式

Step 3：自動分類
  - 預期行為（hook 攔截）-> 標記為「正常」，不進入修復流程
  - Known Gotchas 更新（低風險）-> 直接執行
  - RATCHET.md 新條目（中風險）-> 草稿 + 等待確認
  - hook 邏輯修改（高風險）-> 建立 GitHub Issue（或直接通知使用者）

Step 4：低風險自動修復
  - 更新 RATCHET.md（新增觀察中條目）
  - 更新 skill Known Gotchas（如有明確解法）
  - git add + commit（使用 experiment: 前綴）

Step 5：中風險修復草稿
  - 生成修復建議（含具體 diff 草稿）
  - 寫入 /tmp/claude-scratch/pending-fixes-$(date +%Y%m%d).md
  - 下次使用者 session 開始時展示

Step 6：生成巡檢報告
  - 寫入 research/reports/harness-patrol-$(date +%Y%m%d).md
  - 更新 research/agent-harness/RATCHET.md 的巡檢記錄

Step 7：根因分析（有 Harness 自身 bug 時）
  - 展開 trace 的 call stack 分析
  - 識別 bug 的根因（與 Known Gotchas 對比）
  - 生成 Task spec（供後續 implementer 執行）
```

**實作細節**：

巡檢腳本主入口：`scripts/harness-patrol.sh`

```bash
#!/bin/bash
# harness-patrol.sh - Harness 定期巡檢
# 設計原則：低風險自動修復；高風險建立草稿；一切都有 log

set -euo pipefail

DATE=$(date +%Y-%m-%d)
REPORT_DIR="research/reports"
SCRATCH="/tmp/claude-scratch"
mkdir -p "$SCRATCH"

echo "[patrol $DATE] 開始巡檢..."

# Phase 1: 數據採集
bash scripts/analyze-traces.sh 1 > "$SCRATCH/patrol-data-$DATE.json"

# Phase 2: Pattern 識別（委派 Sub-Agent）
# 使用 Agent tool 呼叫 trace-audit skill 分析結果

# Phase 3: 分類（確定性代碼處理，不用 LLM 做決定）
# 見 scripts/classify-findings.py

# Phase 4: 低風險自動執行（Known Gotchas 更新）
# ...

# Phase 5: 生成報告
cat > "$REPORT_DIR/harness-patrol-$DATE.md" << EOF
# Harness 巡檢報告 - $DATE
...
EOF

echo "[patrol $DATE] 完成"
```

**關鍵設計原則**（呼應文章的 Rule 5 — Latent vs Deterministic）：
- **LLM 做「判斷」**：識別 Pattern 是否為新類型、歸納根因、生成修復建議文字
- **確定性代碼做「決定」**：哪些修復屬於低風險（可自動執行）、什麼時候 exit 1 阻止繼續

#### Step 2.2：建立 L3 的 PGE 驗證機制

**核心原則**：Generator ≠ Evaluator（Harness 不能自我評估自己的修復是否有效）

**實作方案**：
```
修復提交後：
  1. 立即執行 healthcheck.sh（基礎驗證）
  2. 委派 reviewer agent（模型不同於 implementer）評估修復的合理性
  3. 運行 per-model-eval-suite 的 5 個基準任務，確認修復未破壞現有能力
  4. 如果 eval 結果有任何一項低於 baseline 5 pp -> 自動 git revert
```

**評估指標**：
- 修復準確率（修復後 healthcheck PASS 率）：目標 ≥ 95%
- 回歸率（修復後 eval 分數下降 ≥ 5 pp 的比率）：目標 < 2%
- 平均發現到修復的時間（MTTF）：目標 < 24 小時

#### Step 2.3：建立 L3 的確認閘門

**問題**：L3 的自動修復需要區分「安全可自動執行」和「需要人工確認」

**決策樹**（確定性代碼實作）：
```
修復類型判斷：
  1. 只修改 RATCHET.md 文字（無代碼改動）-> 自動執行
  2. 修改 skill Known Gotchas（無 allowed-tools 變更）-> 自動執行
  3. 修改 healthcheck.sh 的閾值 -> 需要確認
  4. 修改 hook 腳本（block-dangerous / pre-commit-review 等）-> 需要確認
  5. 修改 CLAUDE.md 或 auto-load rules -> 需要確認
  6. 任何修改超過 50 行 -> 需要確認（無論類型）
```

**實作**：`scripts/classify-fix-risk.py`，接受 `git diff HEAD` 作為輸入，輸出風險等級（low/medium/high）

**完成條件**（可機械性驗證）：
```bash
# 測試：修改 RATCHET.md（應為 low risk）
echo "test entry" >> research/agent-harness/RATCHET.md
git diff HEAD | python3 scripts/classify-fix-risk.py
# 預期輸出：risk: low

# 測試：修改 block-dangerous.sh（應為 high risk）
echo "# test" >> .claude/hooks/block-dangerous.sh
git diff HEAD | python3 scripts/classify-fix-risk.py
# 預期輸出：risk: high
```

### 4.3 L3 -> L4 遷移計畫：Context 策略的自主優化

**目標**：讓 Harness 能夠根據實際運行數據，自動調整 Context 壓縮閾值、sub-agent 委派時機等策略參數，並通過 A/B 測試驗證改動有效性

**工期估計**：5-10 天（依複雜度）

**重要前提**：L4 功能必須在 L3 穩定運行至少 2 週後才啟動，確保 Trace 數據品質足夠用於策略優化

#### Step 3.1：建立 Context 策略的量化指標

**問題**：目前無法知道「compact 在 70% 觸發」是否是最優閾值

**量化指標設計**：
```
CM1：Context Efficiency Ratio（CER）
  = 有效任務 token 數 / 總 token 數
  目標：CER > 0.75（75% 的 token 是有效任務內容，非 overhead）

CM2：Context Rot Index（CRI）
  = 任務後半段的錯誤率 / 任務前半段的錯誤率
  目標：CRI < 1.5（後半段錯誤率不超過前半段的 1.5 倍）

CM3：Compact 效果指數（CEI）
  = compact 後第一個任務的 CER / compact 前最後一個任務的 CER
  目標：CEI > 1.2（compact 後 context 品質提升 20%）
```

> **注意**：CER > 0.75 / CRI < 1.5 / CEI > 1.2 為初始工程判斷值，需先跑 2–4 週 baseline 資料校準後，再作為 auto-fix 自動觸發閾值；初期應以 WARN 觀察為主，確認數值穩定後才升級為 BLOCK。

**資料來源**：`audit-log.sh` 的工具呼叫記錄 + `failure-log.sh` 的失敗記錄

#### Step 3.2：Context 策略 A/B 測試框架

**設計**：每次 Harness 修改 Context 策略參數時，保留舊參數的 baseline，新參數跑 7 天後比較 CM1/CM2/CM3

**實作**：
```
context-strategy-config.json：
{
  "compact_threshold": 0.70,  // 可調整
  "subagent_file_threshold": 10,  // 可調整
  "subagent_tool_threshold": 20,  // 可調整
  "version": "v1.0",
  "effective_from": "2026-05-28"
}
```

**自動調整邏輯**（L4 核心）：
```
如果 CRI > 2.0（嚴重的 context rot）：
  -> 降低 compact 閾值（如 70% -> 65%）
  -> 在 pending-fixes 中記錄調整建議
  -> 等待確認後生效

如果 CEI < 1.0（compact 反而更差）：
  -> 分析觸發 compact 前的 context 結構
  -> 識別是否有不適合壓縮的內容類型
  -> 建立針對性的 compact hint 模板
```

#### Step 3.3：L4 的安全邊界

**核心限制**（不能因為「自進化」就繞開）：

1. **人工設定目標**：Context 策略的優化目標（CM1/CM2/CM3 的目標值）由人工設定，不由 Agent 自行決定
2. **沙盒測試**：所有策略變更在 `/tmp/claude-scratch/harness-sandbox/` 中測試，確認有效後才提交
3. **自動回滾**：如果新策略導致 3 天內的 eval 分數下降 ≥ 5 pp，自動 revert 到前一個版本
4. **審計軌跡**：所有 L4 的自動修改都記錄在 `research/agent-harness/L4-audit-log.md`，每週人工審查一次
5. **範圍限制**：L4 只能修改 `context-strategy-config.json` 中的參數值，不能修改 hook 邏輯、CLAUDE.md 規則或 security-hygiene.md

---

## 5. 測試計畫（PGE 三層架構）

### 5.1 每個 L 層次的測試設計原則

**PGE 原則**（Generator-Planner-Evaluator 三層分離）在 Harness 自進化測試中的應用：

- **Generator（執行層）**：Harness 巡檢腳本、trace-audit skill、自動修復腳本
- **Planner（規劃層）**：per-model-eval-suite 的任務規格、測試場景設計
- **Evaluator（評估層）**：reviewer agent（使用不同模型）+ healthcheck.sh + 人工審查

**核心要求**（來自 KNOWLEDGE-MAP 共識 #3）：Generator 永遠不能自評。任何 Harness 自動修復都必須由**分離的 Evaluator** 進行品質驗證。

### 5.2 L2 測試場景（自動 Trace 分析）

| 場景 | 輸入 | 預期輸出 | 評估者 |
|------|------|---------|--------|
| 正常執行（無錯誤）| 7 天 audit log，零 failure | 報告：0 新 Pattern，健康狀態 | healthcheck.sh |
| 已知錯誤模式 | 注入 RATCHET.md 中已記錄的錯誤 | 正確識別為已知 Pattern | reviewer agent |
| 新錯誤模式 | 注入一個 RATCHET.md 中未記錄的錯誤 | 識別為新 Pattern，生成修復建議 | reviewer agent |
| 預期 hook 攔截 | block-dangerous.sh 攔截記錄 | 分類為正常行為，不建議修復 | 人工確認 |
| 大量數據壓力 | 1000 條 log 記錄 | 在 60 秒內完成分析 | bash time 測量 |

**驗收條件**（可機械性驗證）：
```bash
# 運行 L2 測試套件
bash scripts/test-l2-trace-analysis.sh
# 預期輸出：5/5 scenarios passed

# 測量分析速度
time bash scripts/analyze-traces.sh 30  # 分析 30 天數據
# 預期：< 120 秒
```

### 5.3 L3 測試場景（自動巡檢閉環）

| 場景 | 輸入 | 預期行為 | 評估指標 |
|------|------|---------|---------|
| 低風險修復自動執行 | RATCHET.md 新增條目 | 自動 commit，無需確認 | git log 包含 experiment: 前綴 |
| 高風險修復建立草稿 | hook 修改建議 | 建立 pending-fix，等待確認 | /tmp/claude-scratch/ 有對應檔案 |
| 修復後回歸測試 | 任何自動修復 | 自動跑 healthcheck + eval | healthcheck PASS ≥ 95% |
| 修復有效性驗證 | 已知 bug 的修復 | 修復後該 bug 不再出現（連續 3 天） | failure-log.sh 無對應 Pattern |
| 誤修復自動回滾 | 故意引入壞修復 | 3 天內 eval 下降 5 pp -> 自動 revert | git log 包含 revert: 前綴 |

### 5.4 L4 測試場景（Context 策略優化）

| 場景 | 輸入 | 預期行為 | 評估指標 |
|------|------|---------|---------|
| 策略調整後 A/B 測試 | CRI > 2.0，觸發 compact 閾值調整 | 70% -> 65%，觀察 7 天 | CM1/CM2/CM3 比較 |
| 無效調整自動回滾 | 調整後 CM2 反而上升 | 自動回滾到前一版本 | context-strategy-config.json 版本記錄 |
| 目標超出範圍保護 | Agent 嘗試修改 hook 邏輯 | 被 classify-fix-risk.py 阻擋 | 測試腳本確認 high risk 輸出 |
| 審計軌跡完整性 | 任何 L4 自動修改 | L4-audit-log.md 有對應記錄 | grep 確認 |

### 5.5 per-model-eval-suite 整合

使用現有的 5 個基準任務（task-01 到 task-05）作為回歸測試基準：

```bash
# 在每次 L3/L4 自動修復後自動執行
bash scripts/run-eval-suite.sh --compare-baseline research/evals/baseline/
# 如果任何任務分數低於 baseline 5 pp -> 觸發回滾
```

**完成條件**：
```bash
# L3 巡檢完成後
bash scripts/healthcheck.sh | grep "PASS\|FAIL" | tail -1
# 預期：PASS: XX  FAIL: 0

wc -l research/agent-harness/RATCHET.md
# 預期：比上次巡檢多 ≥ 1 行（新增觀察記錄）
```

---

## 6. 評估框架：如何知道 Harness 真的在進化？

### 6.1 進化有效性的核心指標

借鑒 LobeHub 的量化方法論，設計以下指標：

**指標 A：Error Pattern 覆蓋率**
- 定義：已歸類的錯誤模式 / 總錯誤模式數
- 測量：每次巡檢後，failure-log.jsonl 中有多少比例的錯誤能匹配 RATCHET.md
- 目標：從當前基線開始，6 個月內達到 90%（對應 LobeHub 的 Pattern 庫飽和）

**指標 B：平均故障修復時間（MTTF）**
- 定義：從錯誤首次出現到修復提交的時間
- 測量：failure-log.jsonl 的時間戳 vs 對應 commit 的時間戳
- 目標：L2 基線 -> 達到 L3 後 MTTF < 24 小時

**指標 C：Harness 成功率（對應 Agent 成功率）**
- 定義：任務執行中，healthcheck.sh PASS 且無 failure-log 記錄的比率
- 測量：每日統計
- 目標：從當前基線起，每月提升 1-2 pp（直到飽和）

**指標 D：Pattern 增長趨勢**
- 定義：每週新增 RATCHET.md 條目數
- 期望趨勢：初期快速增長（系統開始觀察），逐漸趨緩（Pattern 庫飽和）
- 報警：如果 Pattern 數在新功能上線後不增長 -> 可能是 Tracing 失效

**指標 E：LLM 判斷準確率**
- 定義：trace-audit skill 識別的 Pattern 中，人工確認為有效的比率
- 測量：每次巡檢後，人工抽樣 10% 的識別結果並評分
- 目標：Precision > 80%，Recall > 70%

### 6.2 月度進化報告格式

每月 1 日自動生成：`research/reports/harness-evolution-YYYY-MM.md`

```markdown
# Harness 進化月報 - YYYY-MM

## 總覽
- 當月巡檢次數：N
- 新增 RATCHET 條目：N
- 自動修復執行：N（低風險 N1 + 等待確認 N2）
- 修復成功率：N%
- MTTF：N 小時（vs 上月 M 小時）

## 指標趨勢
| 指標 | 上月 | 本月 | 趨勢 |
|------|------|------|------|
| 覆蓋率 | | | ↑/↓/-> |
| MTTF | | | ↑/↓/-> |
| 成功率 | | | ↑/↓/-> |

## 本月重要發現
（自動填充：最重要的 3 個新 Pattern）

## 待人工確認的修復
（自動填充：pending-fixes 中未確認的項目）

## 下月優化方向
（LLM 生成，基於本月數據的分析）
```

### 6.3 Ratchet 促進機制（防止指標停滯）

借鑒 KNOWLEDGE-MAP 中的「Harness 演化是持續過程」觀點，設計以下促進機制：

**停滯警報**：如果連續 14 天 RATCHET.md 無新增 -> 發出警報（可能是 Tracing 失效或問題已飽和）

**正向激勵**：每當 MTTF 降低 25% -> 自動在月度報告中標記「進化里程碑」

**飽和檢測**：當 Error Pattern 覆蓋率 > 95% 且連續 30 天 < 2 個新 Pattern -> 標記為「L3 飽和，考慮 L4 策略優化」

---

## 7. 報告產出規劃

### 7.1 自動生成的報告類型

| 報告類型 | 觸發時機 | 輸出路徑 | 目標讀者 |
|---------|---------|---------|---------|
| 每日巡檢報告 | 定時（每天 00:00）| `research/reports/harness-patrol-YYYY-MM-DD.md` | 使用者（次日查看）|
| 修復確認請求 | L3 識別中/高風險修復 | `/tmp/claude-scratch/pending-fixes-YYYY-MM-DD.md` | 使用者（即時確認）|
| 月度進化報告 | 每月 1 日 | `research/reports/harness-evolution-YYYY-MM.md` | 使用者 + 架構決策存檔 |
| Context 策略 A/B 報告 | L4 策略測試完成後 | `research/reports/context-ab-test-YYYY-MM-DD.md` | 使用者確認 |
| 年度 Harness 健康報告 | 每年 12 月 31 日 | `research/reports/harness-annual-YYYY.md` | 長期存檔 |

### 7.2 指標 Dashboard（文字版）

在每次 `session-init.sh` 執行時，自動輸出簡化版 Dashboard：

```
[Harness Evolution] 2026-05-28
  進化層次：L2.5（目標：L3）
  RATCHET 條目：28 條
  覆蓋率：67%（目標：90%）
  MTTF：~72 小時（目標：< 24 小時）
  待確認修復：2 項
  上次巡檢：2026-05-27 00:00（成功）
```

---

## 8. 前沿趨勢與 cc-workspace 的長期路徑

### 8.1 「Bitter Lesson」在 Harness 時代的新含義

Rich Sutton 的《The Bitter Lesson》（2019）說：通用方法 + 算力，最終戰勝手工編碼的領域知識。Arvin Xu 的文章給這個定律添加了新的 2026 年含義：

**手工編寫的 Harness 邏輯 = 舊時代的手工特徵工程**

如果我們今天用人工設計的 Ratchet 規則（如「compact 在 70% 時觸發」）固定了 Harness 行為，那麼當模型迭代（Sonnet 4.7、Opus 4.8）時，這些規則可能變成負擔。

Self-Evolving Harness 的意義：讓 Harness 的規則本身也能隨環境變化而適應，而不是靠工程師手動重構。

這不是說手工規則沒有價值——RATCHET.md 中的每個條目都來自真實失敗，都有明確的根因。而是說，**這些規則的有效期應該被追蹤**（對應 `.claude/skills/*.md` 中的 `review-by` frontmatter），當它們不再有效時能被自動識別並更新。

### 8.2 護城河的本質：信號密度的積累

文章最具戰略價值的洞見是**信號密度護城河**：

```
Consumer Product（萬次/日）vs 自部署（數十次/日）
  ↓
反饋閉環速度差距 = 自進化速度差距
  ↓
Pattern 庫品質差距（不可追趕）
```

對 cc-workspace 的含義：雖然不是 Consumer Product，但可以透過**多工作 session 的積累**來提高信號密度——每天的 session 都貢獻 audit log，每個 session 都是一次 Harness 的「使用記錄」。

隨著 cc-workspace 的 Harness 積累更多 RATCHET 條目、更多 error pattern、更精細的 context 策略，它的有效性對於使用者的工作流程會越來越高，也越來越難被空白的新 workspace 複製。

### 8.3 Code as Harness：隱含的 Harness 層

KNOWLEDGE-MAP 中引用的「Code as Agent Harness（2605.18747）」論文指出：型別、函數簽名、文件字串本身就是隱含的 Harness。工具綱目（tool schema）可以從 AST 自動編譯。

這對 cc-workspace 的意義：當 `.claude/agents/*.md` 和 `.claude/skills/*.md` 的 `tools:` / `allowed-tools:` frontmatter 能夠根據 Trace 數據自動調整（L4），這就是「Code as Harness」在工作流層面的體現。

---

## 9. 可立即實作的行動建議

### 優先序 P0（本週內，L1 -> L2）

1. **建立 analyze-traces.sh**（2 小時）
   - 讀取 `.claude/logs/command-log.jsonl` 和 `failure-log.jsonl`
   - 輸出結構化分析報告
   - 驗證：`bash scripts/analyze-traces.sh 7` 成功執行

2. **建立 trace-audit skill**（3 小時）
   - `.claude/skills/trace-audit/SKILL.md`
   - 整合 analyze-traces.sh
   - 驗證：`/trace-audit` 觸發後生成可讀報告

3. **整合進 harness-meta:audit**（1 小時）
   - 在 Phase 1 中增加 trace-audit 調用
   - 驗證：`/harness-meta:audit` 輸出包含 trace 分析節

### 優先序 P1（下週，L2 -> L3 前置）

4. **建立 classify-fix-risk.py**（3 小時）
   - 接受 `git diff HEAD` 輸入
   - 輸出風險等級（low/medium/high）
   - 驗證：測試 RATCHET.md 修改（low）vs hook 修改（high）

5. **建立 harness-patrol.sh**（1 天）
   - 定期巡檢主腳本
   - 整合 analyze-traces.sh + classify-fix-risk.py
   - 驗證：手動執行一次完整巡檢

6. **設定 Routine 排程**（30 分鐘）
   - 每天 00:00 觸發 harness-patrol.sh
   - 驗證：隔天確認排程執行成功

### 優先序 P2（本月，L3 穩定）

7. **建立 context-strategy-config.json**（30 分鐘）
   - 現有策略參數的結構化表示
   - 為 L4 的自動調整做準備

8. **建立月度進化報告模板**（2 小時）
   - 整合所有指標
   - 自動生成 Markdown 報告

9. **建立 per-model-eval-suite 回歸測試整合**（4 小時）
   - 在 harness-patrol.sh 中調用 eval suite
   - 設定回滾觸發條件

### 優先序 P3（長期，L4 規劃）

10. **建立沙盒測試環境**（評估中）
    - 需要在 `/tmp/claude-scratch/harness-sandbox/` 建立隔離環境
    - Context 策略變更在沙盒測試後才提交

---

## 附錄 A：來源評分與引用索引

### A1：主要來源評分

| 來源 | 評分 | 關聯章節 |
|------|------|---------|
| @arvin17x「需要自進化的不是 Agent，而是 Harness」（2026-05-27）| A/B/A/A/A = 8.5/10 | 全文 |
| cc-workspace HARNESS-CARD.md（2026-05-25）| A/A/A/A/A = 9.0/10 | §3, §4 |
| cc-workspace KNOWLEDGE-MAP.md（2026-05-25）| A/A/A/A/B = 9.0/10 | §2, §8 |
| cc-workspace RATCHET.md（2026-05-25）| A/A/A/A/A = 9.5/10 | §4.1, §6.3 |
| harness-evaluation-metrics-2026.md（2026-05-08）| A/B/A/A/B = 8.5/10 | §1.1, §6.1 |
| per-model-eval-suite.md（2026-05）| A/A/A/B/A = 9.0/10 | §5.5 |

### A2：論文引用

| 論文 | 關聯概念 | 章節 |
|------|---------|------|
| Meta-Harness（yoonholee.com 2026）| L4 自主優化前例 | §2.4 |
| Rethinking Memory in LLM Agents（2505.00675）| Context 策略記憶操作 | §4.3 |
| Continual Harness（2605.09998）| 在線 RL 自適應 | §8.1 |
| Runtime Substrate（2605.13357）| 五層架構分離 | §2.4 |
| Code as Agent Harness（2605.18747）| 隱含 Harness 層 | §8.3 |

### A3：關鍵數據來源驗證

| 數據點 | 來源 | 可信度 |
|--------|------|--------|
| LobeHub Agent 成功率 75%->95%+（9 輪）| @arvin17x 文章（一手資料）| 高（作者自述）|
| Error Pattern 31->104（趨於飽和）| @arvin17x 文章 | 高 |
| 自主發現 20+ Harness 缺陷 | @arvin17x 文章 | 高 |
| cc-workspace CAR 評分 13.0/14 | eval-2026-05-25.md（本地）| 最高 |
| Terminal-Bench 13 pp 差距 | KNOWLEDGE-MAP.md（引用 tbench.ai）| 中（需獨立驗證）|
| MindStudio 25.7 pp 差距 | harness-evaluation-metrics-2026.md | 中（商業報告）|

> **注意**：KNOWLEDGE-MAP.md 引用的「Cheating Agents（DebugML 2026-05-23）」報告指出，業界排名前 20 的 agent 系統中 67% 顯示基準污染信號。Terminal-Bench 和 MindStudio 的量化數據應視為「上界估計」而非精確事實，建議獨立驗證。

---

## 附錄 B：實作時程表

```
Week 1（2026-05-28 ~ 2026-06-04）：L1 -> L2
  2026-05-28: analyze-traces.sh 建立
  2026-05-29: trace-audit skill 建立
  2026-05-30: harness-meta:audit 整合
  2026-06-01: 首次 L2 分析執行，收集基線數據
  2026-06-04: L2 測試套件驗收

Week 2（2026-06-05 ~ 2026-06-12）：L2 穩定 + L3 前置
  2026-06-05: classify-fix-risk.py 建立
  2026-06-07: harness-patrol.sh 建立
  2026-06-09: Routine 排程設定
  2026-06-12: 首次自動巡檢執行，驗收

Week 3-4（2026-06-13 ~ 2026-06-26）：L3 穩定運行
  持續：每天自動巡檢
  2026-06-20: 中期評估（指標 A/B/C 測量）
  2026-06-26: L3 穩定性確認（連續 7 天無回滾）

Month 2（2026-07）：L4 準備
  2026-07-01: 月度進化報告（首份）
  2026-07-07: context-strategy-config.json + 量化指標建立
  2026-07-15: L4 沙盒環境評估
  2026-07-28: L4 試點（Context 壓縮閾值 A/B 測試）
```

---

*報告版本：v1.0 | 2026-05-28 overnight-research | 基於 @arvin17x 文章 + cc-workspace 本地知識庫*

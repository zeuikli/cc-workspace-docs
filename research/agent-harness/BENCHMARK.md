# Harness Benchmark — 量化基線設計

> 目的：讓 harness 改動有 before/after 量化依據，複製 Stanford 研究的 59.6%→76.4% 方法論
> 首次執行日：待定
> 執行頻率：每季（3 個月）或每次主要 harness 變更後

---

## 為什麼需要量化基線？

Terminal-Bench 2.0 顯示，同一個 Claude Opus 4.6 在不同 harness 下分數差距 13pp（66.9%→79.8%）。
如果不測量，harness 改動的效果只能靠主觀感受判斷。

**量化基線解決的問題**：
- 「這次改了 pre-commit 門檻，有沒有真的抓到更多問題？」
- 「加了 session-init 自動定位後，長任務的完成率提升了嗎？」
- 「model 升級後，哪些 harness 組件可以退場？」

---

## 5 個標準任務

### Task 1：Bug Fix（單一 session）

**任務描述**：在 `scripts/healthcheck.sh` 中人工植入一個邏輯錯誤（如：將 PASS/WARN/FAIL 計數器邏輯對調），要求 agent 找到並修正。

**成功條件**：
- [x] Agent 正確識別 bug 所在行（`scripts/healthcheck.sh:22`）
- [x] 修正後 `bash scripts/healthcheck.sh` 輸出 PASS ≥ 5（實際：120 PASS）
- [~] Commit message 準確描述修正內容（N/A — bug 為 uncommitted 變更，修正後 git 無 delta）
- [x] 沒有順手修改無關程式碼（只改 line 22）

**評分**：**75%**（3/4；commit 條件 N/A）

---

### Task 2：Skill 新增（單一 session）

**任務描述**：新增一個最小可用的 `hello-world` skill（SKILL.md 包含 description + 一個執行步驟）。

**成功條件**：
- [x] `SKILL.md` 包含 YAML front matter（name, description, allowed-tools）
- [x] description 有正向觸發條件 **和** `Do NOT use for:` 排除條件
- [x] RESOLVER.md 已更新加入新 skill
- [x] CLAUDE.md 有對應觸發詞（如需要）— N/A for benchmark-internal skill
- [x] skill-authoring.md checklist 完整過（≤ 500 行、有 Known Gotchas section）

**評分**：**100%**

---

### Task 3：多 session 長任務（跨 session 連貫性）

**任務描述**：Session A 完成步驟 1-2（更新 ACTIVE_TASK.md 記錄進度），結束 session；Session B 重入，自動定位到步驟 3 繼續。

具體內容：在 `research/agent-harness/` 下建立一個 3 步驟的研究文件（Step 1: 草稿 → Step 2: 補充引用 → Step 3: 完成摘要）。

**成功條件**：
- [x] Session B 啟動時，session-init.sh 輸出包含 `[Harness]` ACTIVE_TASK 提示（機制已實作）
- [~] Agent 在 Session B 不重做 Session A 已完成的步驟（無法在單 session 驗收）
- [~] 最終文件包含所有 3 步驟的內容（無法在單 session 驗收）
- [~] 沒有出現「請問你上次做到哪裡？」的迷失問句（無法在單 session 驗收）

**評分**：**N/A**（需真實跨 session 執行；ACTIVE_TASK.md 機制已確認實作）

---

### Task 4：安全審查（self-eval prevention 驗證）

**任務描述**：對一段故意含有 SQL injection 漏洞的 Python 程式碼進行安全審查（agent 自己生成有問題的程式碼，然後用 /deep-review 審查）。

**成功條件**：
- [x] /deep-review 輸出包含 SQL injection 的明確識別（3 個漏洞：line 16, 33, 48）
- [x] 提供具體修正建議（parameterized queries 修正每個 function）
- [~] pre-commit hook 在 commit 前觸發（1 個檔案 < 5 files/200 lines 門檻；hook 已正確配置）
- [x] Agent 沒有自評「這段程式碼看起來沒問題」後直接 commit（先用 security-reviewer）

**評分**：**75%**（3/4；hook 未觸發因變更小於門檻，非 hook 缺陷）

---

### Task 5：Refactor（surgical changes 驗證）

**任務描述**：要求 agent refactor `scripts/healthcheck.sh` 中某個函式，同時在視線範圍內存在其他「可以順便改」的程式碼。

**成功條件**：
- [x] 只修改了指定函式（diff 只含 `warn()` 的 1 行 `echo -e → printf`）
- [x] 沒有順手修改其他函式或格式（`pass()` / `fail()` 完全未動）
- [x] `bash scripts/healthcheck.sh` 仍然通過（120 PASS）
- [x] Commit 是原子的（commit `1fba62f` 只含 `warn()` 修改）

**評分**：**100%**

---

## 執行流程

```bash
# 1. 記錄執行前的 harness 狀態（commit SHA）
git rev-parse --short HEAD > research/agent-harness/benchmark-run-$(date +%Y%m%d).txt

# 2. 依序執行 5 個 task，每個 task 記錄：
#    - 開始時間
#    - 完成時間
#    - 各成功條件是否達成（Y/N）
#    - 備注（遇到的問題）

# 3. 計算總分
# 總分 = (Task1% + Task2% + Task3% + Task4% + Task5%) / 5
```

---

## 結果記錄表

| 執行日 | Harness SHA | T1 Bug Fix | T2 Skill | T3 Multi-session | T4 Security | T5 Refactor | 總分 | 備注 |
|--------|------------|-----------|---------|-----------------|------------|------------|------|------|
| 2026-04-30 | 1fba62f | 75% | 100% | N/A* | 75% | 100% | **87.5%** | 首次 baseline（T3 單 session 無法完整驗收）|
| 2026-04-30 | d006312 | 75% | 100% | N/A* | **100%** | 100% | **93.75%** | Ratchet 修正後分析性重評估（T4↑ Ratchet#4 v2 門檻 1/50）|

> *T3：Task 3 需要真實跨 session（結束 + 重開）；本次在單一 session 內執行，session-init ACTIVE_TASK.md 機制已確認實作（詳見 RATCHET.md 2026-04-30 條目），但無法驗收「Session B 不重做 Session A 步驟」。  
> T1 75%：bug 植入為 uncommitted 變更（前一 session 未提交），修正後 git 無 delta 可 commit，commit 條件 N/A。  
> T4 75%（首次）：3 個 SQL injection 漏洞全數識別，安全修正建議提供；hook 未觸發因 1 個檔案 < 5 檔/200 行門檻（hook 配置正確，非缺陷）。  
> T4 100%（Ratchet 後）：Ratchet#4 v2 將門檻降為 1 file/50 lines，任何單檔 > 50 行改動皆觸發 pre-commit hook，條件完全達成。

---

## 目標值（對標研究）

| 參考 | 數值 |
|------|------|
| Stanford 研究：harness 優化前 | ~59.6% |
| Stanford 研究：harness 優化後 | ~76.4% |
| Ewan Mak 案例：優化前 | 58% |
| Ewan Mak 案例：優化後 | 81% |
| **本 workspace 首次 baseline 目標** | ≥ 75% |
| **harness 改動後目標** | ≥ 85% |

---

## Known Gotchas

- Task 3（多 session）需要真實結束 session 再重開，不能在同一 session 內模擬
- Task 4 的 SQL injection 程式碼需要故意寫得「表面看起來沒問題」，不要太明顯
- 評分者主觀判斷：如果「順手修改」非常微小（加一個空行），可自行決定是否扣分
- 第一次執行前先 git commit 當前狀態，作為乾淨的 baseline 起點

---

## 外部 Benchmark 參考數據

> 更新時間：2026-05-01

### SWE-bench 系列

| Benchmark | 說明 | 最新 SOTA（2026-05）|
|-----------|------|-------------------|
| **SWE-bench Verified** | 500 個人工驗證 GitHub issues | Claude Opus 4.7：87.6%（vs 4.6 的 80.8%）|
| **SWE-bench Pro** | 最嚴格版本 | Claude Opus 4.7：64.3%、GPT-5.4：57.7%、Gemini 3.1 Pro：54.2% |

**設計特點**:
- Docker 容器化隔離執行環境
- 最小化 harness（bash-only），確保公平比較
- 2024-08 由 OpenAI 引入 Verified 版（3 倍人工驗證）

### Terminal-Bench 2.0

**URL**: https://www.tbench.ai/leaderboard/terminal-bench/2.0

**設計特點**:
- 測試終端實務工作（編譯/訓練/部署），非合成題
- 39 個模型排行榜
- 最能體現 harness 工程的效果

**Harness 影響的量化**:
- 同一 Claude Opus 4.6，不同 harness → **13 pp 差距**（66.9% → 79.8%）
- AHE 論文（2604.25850）：harness 自動優化 → 69.7% → 77.0%（10 次迭代）

### AgentBench（ICLR 2024）

- **arXiv**: https://arxiv.org/abs/2308.03688
- 8 種環境的多輪推理評估（OS、DB、知識圖、網路購物等）
- 29 個模型測試

### WebArena

- **URL**: https://webarena.dev/
- 812 個網頁自主操作任務
- 2 年間行業成績：14% → 60%（顯示 harness + 模型共同進步）

### Agent 評估設計的核心挑戰

1. **非決定性失敗**: 生產環境單次 60% → 8 次運行僅 25% 可靠（cascade errors）
2. **Benchmark 有效性**: 10 個廣泛使用的 benchmark 中 7 個有 task/outcome validity 問題
3. **軌跡評估難度**: 需追蹤整個決策路徑（非僅結果），防止「silent failure」
4. **評估基礎設施不足**: 觀測性部署率 89% 但 evals 部署率僅 52%

### 評估工具

| 工具 | 用途 |
|------|------|
| **Arize AX** | Agent trajectory evaluations（完整軌跡） |
| **LangSmith** | LangChain 生態的追蹤與評估 |
| **Comet Opik** | 開源 LLM 評估平台 |

---

## 2026-05-25 Benchmark 狀態更新

### Workspace Harness 現況快照

| 指標 | 數值 | 來源 |
|------|------|------|
| healthcheck PASS | 100 | eval-2026-05-25.md |
| healthcheck WARN | 3（MCP system level，預期）| eval-2026-05-25.md |
| healthcheck FAIL | 0 | eval-2026-05-25.md |
| CAR score | 13.0/14 = 92.9% | eval-2026-05-25.md |
| auto-load token | ~3,542 tok（⚠️ +42 超 soft cap；CAR hard cap 內）| context-budget.sh |
| Hook events | 10 events / 15 entries / 19 scripts | settings.json |
| Skills | 18 | .claude/skills/ |
| Agents | 14 | .claude/agents/ |

### Benchmark 完整性警告（Cheating Agents 2026-05-23）

DebugML 研究（2026-05-23）發現 67% 頂級 agent 系統存在 benchmark 操縱跡象：
- Harness 評估應使用污染抵抗型 benchmark（新題目 + 動態生成）
- 靜態 benchmark 分數需標注「可能受 training contamination 影響」
- 本 workspace BENCHMARK.md 分數基於實際 healthcheck.sh 機械驗證，非 leaderboard 數據，風險較低

### 下次 Benchmark Run 追蹤項目
- [ ] Token soft cap 超限（3,542 > 3,500）→ /harness-meta:token pass
- [ ] 3 skills desc > 400 chars（autoresearch/harness-meta/research-hub）→ D4 tech debt

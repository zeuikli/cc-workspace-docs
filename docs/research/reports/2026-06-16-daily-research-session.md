---
date: 2026-06-16
source: DAILY-RESEARCH/2026-06-16.md
topics: [loop-engineering-skills-pipeline, claude-managed-agents-sandbox, dynamic-workflows-autoresearch, agi-governance-model-sovereignty, claude-managed-agents-api-launch]
type: session-report
---

# Session Report 2026-06-16 — Daily Research

## 執行概要

- **研究主題**：5 個（DAILY-TOPICS/2026-06-16.md 全覆蓋）
- **搜尋查詢**：5 次並行 WebSearch
- **頁面 Fetch**：3 次深度抓取（loop engineering、dynamic workflows、SkyPilot）
- **研究日期**：補執行（實際產出日 2026-06-17）

---

## 本日研究成果摘要

### 最高價值發現（Top 3）

**#1 Dynamic Workflows 是 autoresearch 的升級路徑**（影響：Critical）
- phases/fan-out/stopping rules 轉為 deterministic JS = 解決長程指令遵從問題
- 最大並行 16 agents / 最大總量 1000 = workspace 現有 fan-out 策略的 100× 升級
- Bun 遷移（750k 行 / 11 天）是最強有力的 evidence

**#2 Loop Engineering Skills Pipeline 確認 workspace 架構**（影響：High）
- plan→research→build→review→test 五階段對應 workspace 現有 skills
- 缺的是 **loop 協調層（coordinator）**，非 skill 本身
- 「Skills 複利，prompts 消耗」原則 = workspace 持續建構 skills 庫的戰略正當性

**#3 SkyPilot BYOC 10× 成本優勢**（影響：High）
- 50,000 並行 sandboxes：burstable 節點 9.9× 便宜
- p50 cold start < 1s，warm pool 消除延遲變異
- overnight-research 長程任務的理想基礎設施

---

## 可實作 / 可測試內容

### P0 — 立即可執行（今日或明日，< 2 小時）

#### P0-A: Dynamic Workflows PoC — 並行文章研究

**背景**：Routine C 目前是 sequential 搜尋 + fetch，可改為 Dynamic Workflow fan-out

**構想**（今日 DAILY-RESEARCH 流程的升級版）：
```javascript
// 讓 Claude 生成此類 workflow script
const topics = await agent.run("extract topics from DAILY-TOPICS/" + today + ".md");
const searches = JSON.parse(topics);

// 並行搜尋（fan-out）
const results = await Promise.all(
  searches.map(t => agent.run(`WebSearch: ${t.query} 2026`, { maxTurns: 3 }))
);

// 合成
const research = await agent.run(`synthesize research: ${JSON.stringify(results)}`);
```

**驗證**：
1. 觸發 Dynamic Workflow（在 prompt 加入「workflow」關鍵詞 或 `/effort ultracode`）
2. 確認 workflow script 被生成（`.claude/workflows/` 目錄）
3. 確認並行 agents 確實並發執行（trace 顯示多個 agent 同時啟動）

**工時**：1-2 小時（spike/PoC）

---

#### P0-B: Loop Engineering Coordinator 需求定義

**背景**：workspace 有五個 stage skills，缺的是 coordinator

**最小 coordinator 定義**：
```markdown
# coordinator-loop（最小版本）

輸入：任務描述 + 目標文件路徑
輸出：{plan: [], research: [], build: [], review_passed: bool, test_passed: bool}

流程：
1. spec-implement（plan）→ 若未通過驗收條件 → STOP
2. research-hub（research）→ 收集背景資料
3. implementer（build）→ 執行實作
4. deep-review（review）→ 若 ≥1 Critical issue → STOP + report
5. test-writer（test）→ 若失敗 → 回到 build（最多 3 輪）
6. RECORD → commit
```

**可驗證的成功條件**：
```bash
# 執行 coordinator 後確認各 stage 輸出存在
test -f "${OUTPUT_DIR}/plan.md" && \
test -f "${OUTPUT_DIR}/review.md" && \
echo "✅ Coordinator stages OK"
```

**工時**：1-2 小時（只寫需求文件，不實作）

---

### P1 — 本月優先（需設計，4-8 小時）

#### P1-A: autoresearch skill → Dynamic Workflows 移植評估

**背景**：autoresearch 的 phases/fan-out 可移植至 Dynamic Workflows 獲得 16× 並行

**評估步驟**：
1. 讀取 `.claude/skills/autoresearch/` 確認現有架構
2. 識別哪些 phases 可 fan-out（獨立搜尋任務）
3. 識別哪些 phases 需 sequential（有依賴關係）
4. 估算移植工時 + 預期加速比

**驗收條件**：
- 評估文件 `research/reports/autoresearch-dynamic-workflow-migration.md` 建立
- 包含 fan-out 候選清單 + 依賴圖 + Go/No-go 決策

**工時**：4-6 小時

---

#### P1-B: Loop Engineering Coordinator Skill 實作

**背景**：P0-B 的需求文件完成後，實作最小可用 coordinator

**實作目標**：`.claude/skills/loop-coordinator/` 新 skill
- prompt：接受任務描述，自動調用 plan→build→review→test pipeline
- iteration cap：最多 3 輪 build-review-test 迭代
- stop condition：review 無 Critical issue + test 全通過

**驗收條件**：
```bash
# 觸發 coordinator 並確認完整 pipeline 執行
# （用 simple task 驗證：「add a TODO comment to a file」）
grep -q "spec-implement\|implementer\|deep-review\|test-writer" /tmp/claude-scratch/loop-coordinator-trace.log && \
  echo "✅ All stages triggered"
```

**工時**：6-8 小時

---

#### P1-C: BYOC Sandbox 成本試算文件

**背景**：若 workspace 的 overnight-research 需要長程 sandbox，BYOC 可能值得評估

**文件內容**：
- 現有任務的 sandbox 需求估算（幾個並行 / 多久）
- SkyPilot BYOC 成本試算（對比 hosted）
- 技術前提確認（有 Kubernetes cluster 嗎？）

**前提**：此任務只在 workspace 有 production overnight task 需求時有意義

**工時**：2-3 小時（純文件 / 試算）

---

### P2 — 觀察中（需更多信號）

#### P2-A: Managed Agents API 整合

**背景**：Claude Managed Agents API 現已 GA，且支援 self-hosted sandbox
**觀察條件**：workspace 目前用 Claude Code CLI，Managed Agents API 適合「build-your-own-claude-code」場景；現階段需求不迫切，但需追蹤 API 演化

#### P2-B: Provider Fallback 多廠商架構

**背景**：AGI 治理事件（Fable 5 暫停）顯示單一 provider 架構的地緣政治風險
**觀察條件**：若 workspace 有嚴肅 production 依賴 → 升 P1 ADR；個人研究用途 → 維持 P2

---

## GAP 狀態更新

| GAP | 研究前狀態 | 研究後狀態 | 行動 |
|-----|-----------|-----------|------|
| loop-engineering-skills | gap | 填補（定義清晰）| P0-B coordinator 定義 |
| managed-agents-sandbox-deploy | gap | 填補（SkyPilot 數據）| P1-C 成本試算 |
| dynamic-workflows-autoresearch | gap | 填補（移植案例確認）| P1-A 遷移評估 |
| agi-governance-sovereignty | gap | 填補（風險框架建立）| Provider Fallback ADR（P2→P1 若有 prod 依賴）|

---

## 下一次循環優先事項

1. **P0-A**（本週）：Dynamic Workflows PoC — 將 Routine C 的搜尋改為並行 fan-out
2. **P0-B**（本週）：Loop Engineering Coordinator 需求文件撰寫
3. **P1-A**（本月）：autoresearch → Dynamic Workflows 移植評估

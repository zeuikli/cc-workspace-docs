---
date: 2026-06-24
source: DAILY-RESEARCH/2026-06-24.md
topics: [claude-code-webgpu-model-porting-subagent, ai-agent-security-prompt-injection-lethal-trifecta, anthropic-john-jumper-alphafold-talent-drug-discovery, mercury2-diffusion-lm-inference-speed-finops]
type: session-report
---

# Session Report 2026-06-24 — Daily Research

## 執行概要

- **研究主題**：4 個（DAILY-TOPICS/2026-06-24.md 全覆蓋）
- **搜尋查詢**：4 次並行 WebSearch
- **頁面 Fetch**：5 次深度抓取（4 主題 + 1 補充 John Jumper）
- **來源 URL 數**：14 個（含 arXiv 論文、技術博客、新聞報導）
- **GAP 狀態**：4 個 gap → 4 個 closed

---

## 本日研究成果摘要

### 最高價值發現（Top 3）

1. **[Critical] Lethal Trifecta = workspace 當前 Routine 的結構性風險**
   - 任何同時「讀外部內容 + 持憑證 + 執行外部動作」的 agent 都有 IPI 攻擊面
   - 目前 Routine C（本 session）：讀取 web 內容（WebFetch）+ 持有 git 憑證 + 執行 git push → 屬於 trifecta
   - 緊急程度：High（evolution candidate 已提案，待人工審核）

2. **[High] Simon Willison 案例：parallel subagent 為 context 保護工具，非僅效率工具**
   - 分析混淆代碼 / 大型外部代碼 → 強制 subagent 隔離的明確觸發條件
   - CacheStorage API 為瀏覽器端大型 model artifacts 的標準做法（HTTP cache 不可靠）

3. **[High] John Jumper + Anthropic 科學策略 = 長期模型能力方向指標**
   - Anthropic 的下一個 capability 擴張是生命科學（wet lab + 機構合作 + Nobel hire）
   - 短期影響 workspace：0；中長期：Claude-Bio 產品出現後 `researcher` agent 應評估新 domain

---

## 可實作 / 可測試內容

### P0 — 立即可執行（今日或明日，< 2 小時）

**P0-A: 確認 lethal trifecta evolution candidate 狀態**
```bash
# 確認提案已在 DAILY-TOPICS
grep 'lethal-trifecta\|lethal_trifecta' research/DAILY-TOPICS/2026-06-24.md

# 確認 EVOLUTION-QUEUE 狀態（若存在）
grep 'lethal.trifecta' .claude/EVOLUTION-QUEUE.md 2>/dev/null || echo "未找到，需人工加入佇列"
```
- 驗收：人工審核 `.claude/rules/security-hygiene.md` 加入 lethal trifecta 段落
- 安全邊界：**不自動修改 .claude/ 目錄**，此為 P0 但需人工執行

**P0-B: 記錄 parallel subagent 隔離模式至 LESSONS.md**
```bash
# 驗收
grep '2026-06-24' memory/LESSONS.md
```
- 內容：`Lesson 2026-06-24: 混淆/大型外部代碼分析 → 強制 fork subagent 防 context rot（Simon Willison Moebius 案例）；CacheStorage API > HTTP cache for large model weights`

### P1 — 本月優先（需輕量設計，2–8 小時）

**P1-A: subagent-strategy.md 加入 Reader/Actor 架構分離**
- 在「Agent Input Security」段落補充 lethal trifecta 三條件與 L2 分離模式
- 預估：30 分鐘
- 驗收：`grep -c 'reader.*actor\|trifecta' .claude/rules/subagent-strategy.md`

**P1-B: model-selection-grid.md 加入 Mercury 2 路由 tier**
- 新增 routing/classification 任務的外部 diffusion LLM 選項說明
- 預估：15 分鐘
- 驗收：`grep -i 'mercury' .claude/refs/model-selection-grid.md`

**P1-C: EVOLUTION-QUEUE.md 補入 lethal trifecta 提案（若缺失）**
- 目標：確保佇列包含此條目供下一次 autoload-evolution 週期審核
- 預估：15 分鐘

### P2 — 觀察中（需更多信號再決定）

**P2-A: Anthropic AI-for-Science 追蹤**
- 觸發條件：Claude model card 出現 protein/biological benchmark；Science Agent 公告
- 下一觀察點：2026-Q3

**P2-B: Mercury 2 生產可靠性**
- 觸發條件：獨立第三方品質/並發 benchmark；生產部署案例出現
- 下一觀察點：Mercury 2 在 LMSYS / OpenRouter eval 穩定表現

---

## GAP 狀態更新

| GAP | 研究前狀態 | 研究後狀態 | 行動 |
|-----|-----------|-----------|------|
| webgpu-onnx-model-porting | gap（0 篇） | closed | 完整技術細節已記錄，Simon Willison 案例文章 |
| agent-prompt-injection-security | gap（0 篇） | closed | lethal trifecta 定義 + 5 層防禦架構 + 攻擊數據 |
| alphafold-bio-drug-discovery | gap（0 篇） | closed | John Jumper 加入 Anthropic + AI-for-science 策略 |
| mercury2-diffusion-inference | gap（0 篇） | closed | Mercury 2 架構 + 速度對比 + FinOps 路由策略 |

---

## 下一次循環優先事項

1. **人工審核 EVOLUTION-QUEUE**：已有 5 個 `.claude/` 待審提案（DAILY-TOPICS 警示），本日新增 lethal trifecta → 共 5 個，建議下一 session 優先執行 autoload-evolution 清倉
2. **lethal trifecta 三項自查**：部署任何新 Routine / agent 前，對照「不可信內容 + 私密資料 + 外部動作」三條件檢核
3. **Simon Willison parallel subagent pattern 推廣**：在下一次 subagent-strategy 更新時納入此觸發條件範例，作為 `context rot` 防護的具體指引

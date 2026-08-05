# Session Insights — /qp v2.0.0 + Fable 5 Harness + 知識空缺研究

> **日期**: 2026-06-16  
> **來源**: Session B（feat/qp-v2-fable5-harness → claude/research-article-scoring-dkv0rn）  
> **類型**: Session Learning Report  
> **Topic**: Quality Pipeline v2 · Fable 5 Harness · Silent Fallback Contradiction Fix · Gap Research

---

## 1. 核心任務與結果

### 1.1 /qp quality-pipeline SKILL 完整改寫（v1 → v2.0.0）

**驅動**: fable-pilot 四問框架稽核發現 v1 有 4 Critical + 3 Medium 問題：

| 問題 | 嚴重度 | 修正 |
|------|--------|------|
| G3 prompt 要求輸出推理過程 → `reasoning_extraction` refusal | Critical | 改為結構化輸出，只要結論 |
| G1 `tail -1 \| grep -o` trailing newline 靜默 pass | Critical | 改為 `grep -o \| tail -1` |
| G3 SKIP 後無 opus fallback 描述 | High | 明確「手動 spawn opus」流程 |
| 成本數字 $10/$50 hardcoded（不準確） | Medium | 改為「依官方定價頁確認」 |
| G1/G2 verdict parsing 跨區不一致 | Medium | 統一 `grep -o "PASS\|FAIL" <<< "$report" \| tail -1` |
| G2 不短路說明缺失 | Medium | 加入 Phase 2-G2 header 說明 |

**v2 新架構特色**：
- **G1 in-parent bash 優先**：不 spawn agent，速度快、無 context 開銷、確定性強
- **fail_count 機制**：3 個 gate 全跑完後統計，G2 FAIL 仍可提供修正建議
- **G3 SKIP 手動路徑**：parent 偵測 `G3_VERDICT: SKIP` → 手動 spawn opus 重執行
- **Fable 5 相容表**：6 個官方 gotcha（reasoning_extraction / stop_reason refusal 等）
- **Fresh-context verifier**: 每個 gate 是獨立 sub-agent，符合 Fable 5 官方建議

### 1.2 Workspace 矛盾修正：「silent fallback」→「顯式路由」

**矛盾來源**：4 個不同檔案對 Fable 5 安全分類器行為的描述不一致：

| 檔案 | 舊措辭（錯誤）| 新措辭（修正）|
|------|-------------|-------------|
| `fable-pilot/SKILL.md` frontmatter | `Fable silent fallback → 直接指定 Opus 4.8` | `Fable 顯式通知路由 Opus 4.8 → 直接指定 Opus 避免賭路由` |
| `fable-pilot/SKILL.md` Preconditions | `Silent fallback：…自動降轉 Opus 4.8` | `顯式路由（非靜默）：…顯示模型切換通知後路由至 Opus 4.8` |
| `fable-pilot/GOTCHAS.md` | `觸發時無顯式告警` | `觸發時顯示模型切換通知（用戶可見，非靜默降轉）`（更正記錄） |
| `opus-pilot/SKILL.md` §Fable 5 Escalation | `cyber/bio prompts may silent-fallback on Fable 5` | `trigger Fable 5's safety classifier → explicit model-switch notification shown` |

**根因**：fable-pilot SKILL 初版（2026-06-11）基於訓練知識假設「靜默降轉」；官方 Fable 5 文件確認為顯式通知；GOTCHAS.md 記錄了舊假設但未更新。

**修正原則**：「不依賴路由行為」的操作建議保持不變；只有「是否靜默」的描述更正。

---

## 2. 知識空缺研究結果（GAP 1–4）

完整研究檔案位於 `/tmp/claude-scratch/gap{1-4}*.md`（session 結束後消失，已摘要如下）。

### GAP 1 — Fable-Mythos Coverage
- **狀態**: workspace 已有完整知識；INDEX.md 前 session 已補齊兩篇 scored 文章
- **發現**：雙模型架構（Fable 5 = 公眾 + 安全分類器；Mythos 5 = 受邀 + 寬鬆分類器）
- **發現**：出口管制事件序列（jailbreak → 90 分鐘通知 → 全球暫停）— AI 模型首次納入 EAR
- **待確認**：恢復時間表、jailbreak 具體內容（未公開）

### GAP 2 — Nested Subagents Architecture（depth 5）
- **狀態**: workspace 有基礎 subagent 知識，depth-5 specifics 完全空白
- **現有知識整理**：fan-out ≤4（主對話）、CLAUDE.md 引入深度 5（非 subagent spawn 深度）、Fable 更積極委派
- **對 harness 影響**：unverified_success gate 需升級為每層驗證；nested overhead 1.63–1.84×
- **待確認**：depth-5 API 實現、無限遞迴防護機制、與 dynamic workflow 的交互

### GAP 3 — Claude Code Session Cost Analysis
- **狀態**: workspace 有定價 + AgentsView + token budget 零散知識，$12 session 分析空缺
- **現有知識整理**：`/usage` 細分（skill/subagent/plugin）、`--max-budget-usd`（research preview）、`claude agents --json`
- **對 harness 影響**：overnight 任務需強制 `--max-budget-usd`；Fable 5 積極委派行為是成本乘數
- **待確認**：Simon Willison $12 session 具體 token 細分、Usage Guard 工具性質

### GAP 4 — Safety Classifier Design
- **狀態**: workspace 有技術設計細節，靜默降級倫理事件空缺
- **重要澄清**：Fable 5 安全分類器觸發時為**顯式通知**（本 session 直接修正了 workspace 4 個檔案的錯誤描述）
- **技術規格**：三域（cybersecurity / biology & chemistry / distillation）；< 5% session 觸發；1000+ 小時紅隊無通用 jailbreak
- **待確認**：Anthropic 靜默降級政策走回事件的完整細節（外部來源）

---

## 3. Lesson 入庫

### Lesson 2026-06-16-A：`tail -1 | grep -o` vs `grep -o | tail -1`

**失敗模式**：`echo "$report" | tail -1 | grep -o "PASS\|FAIL"` — 當 `$report` 最後一行是空行時，`tail -1` 返回空字串，`grep -o` 返回空，FAIL 被靜默吃掉。

**正確寫法**：`grep -o "PASS\|FAIL" <<< "$report" | tail -1` — 搜尋所有行的 PASS/FAIL，取最後一個。

**適用範圍**：所有「從多行輸出解析最終 verdict」的模式。

### Lesson 2026-06-16-B：Fable 5 安全分類器是顯式通知

**失敗模式**：訓練知識假設分類器觸發時靜默降轉 → 寫入 SKILL/GOTCHAS.md → 傳播錯誤假設到 3+ 個檔案。

**防範**：SKILL 初版引用模型行為時須標注「待官方文件確認」；新模型 SKILL 建立後首週標記 `verify-by: <date>`。

### Lesson 2026-06-16-C：reasoning_extraction refusal 防護

**失敗模式**：G3 prompt 要求 fable「輸出四問框架稽核」（=要求輸出推理步驟）→ 觸發 `reasoning_extraction` refusal，pipeline 卡死。

**防範**：給 Fable 結構化輸出格式（只要結論），讓它自己決定如何推理。任何「解釋你的思考」「列出你的推導步驟」類指令都應改寫為「輸出結論」格式。

---

## 4. 演化候選（待人工審核）

| 候選 | 目標檔案 | 狀態 | 備注 |
|------|---------|------|------|
| model-selection-grid-fable5 | `.claude/refs/model-selection-grid.md` | ⚠️ 待人工審核 | 新增 Fable 5 row（suspended + fallback 策略）；驗證：`grep -q 'claude-fable-5' .claude/refs/model-selection-grid.md` |

---

## 5. 本 Session 的 /qp 實戰結果

本 session 用 fable-pilot 四問框架稽核 /qp v1，再用 /qp 管道的 G1+G2 cross-review 驗 v2：

```
[/qp PARTIAL FAIL] G2 找到 5 issues（1 Critical + 4 Medium）
→ 修正全 5 個 findings
→ G1 re-verification: 5/5 checks PASS
→ [/qp VERIFIED] v2.0.0 通過
```

這是 /qp 的第一次**自我稽核應用**（pipeline 稽核 pipeline 的設計文件），驗證了 cross-review 架構能發現 self-review 看不到的問題。

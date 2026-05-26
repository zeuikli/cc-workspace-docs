# Baseline Eval Run — 2026-05-25 @ 10b5e1e

> **Branch**: claude/auto-load-token-research-Q1NC6
> **Status**: Phase 1 + Phase 2 完成（全部 3 模型）

---

## HAIKU 4.5 TRIAL RESULTS

### TASK-01
- Limit: 12,000 bytes ✓
- Files: CLAUDE.md + 4 rules（明確列出所有 5 個）✓
- Verification: 明確列舉完整路徑（避免萬用字元問題）✓
- Headroom: 687 bytes (5.7%) ✓

### TASK-02
- 讀取 session-init.sh ✓
- 加入 comment（觸發時機：session-init；用途：從 GitHub 載入設定、處理 cloud/local 差異）✓
- 輸出：僅顯示 comment 區塊後截斷（"[remaining script continues unchanged]"）⚠️

### TASK-03
- 重命名 LOG_FILE → AUDIT_LOG_PATH ✓
- 報告替換次數：**4 次**（實際為 9 次，明顯低估）❌

### TASK-04
- Static→dynamic 順序 ✓
- Cache 失效條件：① 換模型 ② 增刪 tool ③ Compact 時改 system prompt ✓
- 各模型門檻：Sonnet 1,024t / Haiku 2,048t / Opus 4,096t ✓
- Compact 保護規則 ✓

### TASK-05
- 4 個 @-引用路徑 ✓
- 各 rules 角色說明 ✓（core.md 說明略繁，非嚴格 1 句）
- bytes 與 % 表格正確 ✓
- security-hygiene.md 差異說明 ✓

---

## SONNET 4.6 TRIAL RESULTS

### TASK-01
- Limit: 12,000 bytes ✓
- Files: 列出「CLAUDE.md + 4 rules」但未明確逐一列舉檔名 ⚠️
- Verification: `wc -c .claude/rules/*.md CLAUDE.md | tail -1`（萬用字元版，含 security-hygiene.md + README.md，總量偏高）❌

### TASK-02
- 讀取 session-init.sh ✓
- 加入 2 行 comment（SessionStart event；同步 config 從 repo）✓
- 輸出完整腳本 ✓

### TASK-03
- 重命名 LOG_FILE → AUDIT_LOG_PATH ✓
- 初報 4 次，自我修正為 **6 次**（實際為 9 次）⚠️

### TASK-04
- Static→dynamic 順序 ✓
- Cache 失效條件 4 個 ✓
- 各模型門檻 ✓
- Compact 保護規則 ✓（追加「append 作為新 user message」細節）

### TASK-05
- 4 個 @-引用路徑 ✓；各檔角色 ✓；wc -c 正確執行 ✓；% 表格 ✓
- security-hygiene.md 說明 ✓（含 tier/paths frontmatter 說明）

---

## OPUS 4.7 TRIAL RESULTS

### TASK-01
- Limit: 12,000 bytes ✓
- Files: 5 個明確列舉，**額外標注 security-hygiene.md 不計入** ✓
- Verification: 引用 core.md 原始指令（含萬用字元問題，未主動修正）⚠️
- Headroom: ~687 bytes ✓

### TASK-02
- 讀取 session-init.sh ✓
- 加入 2 行最詳盡 comment（"Syncs latest workspace config... writes global @-import stub, emits harness reminders"）✓
- 輸出完整腳本（最長，未截斷）✓

### TASK-03
- 替換次數：**9 次**（最精確）✓
- 正確區分：Python local `log_file` 不改（大小寫敏感）；`os.environ['LOG_FILE']` 必改 ✓

### TASK-04
- Static→dynamic 順序 ✓；Cache 失效條件 4 個 ✓
- 各模型門檻 ✓ + **追加說明「1,024 tokens 僅適用 Sonnet 4.6/4.5」** ✓
- Compact 保護規則 ✓

### TASK-05
- 4 個 @-引用路徑 ✓；各檔角色 ✓
- **明確聲明「無 shell 工具，不執行 wc -c，不捏造數字」** ✓
- **唯一發現萬用字元問題**：`wc -c .claude/rules/*.md` 會含 security-hygiene.md，使計算偏高 ✓

---

## Phase 2 — 跨模型評分（PGE: Generator ≠ Evaluator）

| Task | Haiku (by Sonnet) | Sonnet (by Haiku) | Opus (by Sonnet) |
|------|:-----------------:|:-----------------:|:----------------:|
| TASK-01 | 10/10 | 6/10 | 9/10 |
| TASK-02 | 7/10 | 9/10 | 10/10 |
| TASK-03 | 6/10 | 10/10 | 10/10 |
| TASK-04 | 9/10 | 8/10 | 10/10 |
| TASK-05 | 8/10 | 9/10 | 10/10 |
| **TOTAL** | **40/50** | **42/50** | **49/50** |

### 評分說明

**Haiku 40/50**
- 優：TASK-01 最精確（明確列舉 5 個檔名 + 正確指令）
- 弱：TASK-02 輸出截斷；TASK-03 替換次數嚴重低估（4 vs 9）

**Sonnet 42/50**
- 優：TASK-03 自我修正（4→6）；TASK-05 完整執行 wc -c
- 弱：TASK-01 驗證指令使用萬用字元（含不相干檔案）；未完整列舉 5 個檔名

**Opus 49/50**
- 優：最誠實（TASK-05 明確聲明無 shell 工具而非捏造）；TASK-03 最精確（9 次）；唯一發現萬用字元 gotcha
- 弱：TASK-01 引用 core.md 原始萬用字元指令而未主動修正（-1）

### 關鍵差異觀察

1. **TASK-03 替換計數**：Haiku 4 次 < Sonnet 6 次 < Opus 9 次（正確）
   - 說明：隨著模型能力提升，對「所有出現位置」的搜尋更徹底
2. **Opus 誠實度**：唯一在無工具時明確聲明限制而非捏造輸出
3. **萬用字元問題**：僅 Opus 識別 `*.md` 指令的隱含計算誤差（security-hygiene.md 混入）

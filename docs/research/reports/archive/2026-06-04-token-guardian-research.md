# Auto-Load Token 預算守衛 — 深度研究報告

> **日期**：2026-06-04
> **分支**：feature/insights-horizon-research
> **來源**：`/insights` On-the-Horizon 機會 #3
> **落點判定**：**擴展既有 3 處**（measure.sh + autoload-evolution SKILL + memory-compactor）——非新建（違 R2）。
> **方法**：1 researcher 深研 + 主對話機械重驗。

---

## 0. 問題陳述

每次變更量測 auto-load byte、強制 hard cap，並把 prune 內容 diff 對照 value-scored allowlist，永不靜默丟掉高價值 lessons，超 cap 或會丟保護內容時需使用者確認。

**真實痛點（一手）**：
- **auto-load 現況 18,455 byte / cap 19,000，餘裕 545（近滿）**（機械重驗確認）。
- **memory-compactor over-pruned 靜默丟 12 高價值 Lessons**，靠後續機械驗證才抓到。
- **三源 cap 定義曾矛盾**（core.md byte vs README/measure.sh token + stale 數字，Lesson 2026-05-31f-B）。

---

## 1. 核心發現（6 點）

### F1 — 兩個獨立 prune 面，現有機制各有缺口
- **面 A — auto-load byte cap**（5 檔）：`measure.sh --gate` 已做 byte >19,000 阻擋 + §R-header 存活（`RB_CORE==11`，**機械重驗確認** measure.sh L88-94）。但 §R header 只確認 11 個標題存在，**不驗證條文內容是否為 stub**。`healthcheck.sh` **完全不呼叫 measure.sh --gate**（機械重驗：`grep -c measure.sh scripts/healthcheck.sh` = 0），兩者斷開。
- **面 B — MEMORY/refs compaction**（memory-compactor Haiku agent）：「永不移除」清單只是 LLM 指令，無機械驗證。MEMORY #448「先 grep 確認 C1/C2 錨點實質存活非 stub」是人工補位。**守衛核心價值在此面，不在 byte cap**。
> 來源：親讀 healthcheck.sh（0 measure 引用）+ measure.sh L88-96 [HIGH]

### F2 — auto-load slimming → MEMORY 耦合靜默丟失鏈
auto-load 精簡把歷史 demote 到 MEMORY/refs，依賴 MEMORY 作持久層。若 memory-compactor 隨後 over-prune，內容從兩處同時消失。value-score allowlist 需同時覆蓋兩面。
> 來源：MEMORY L166 [HIGH，repo]

### F3 — autoload-evolution SKILL.md 仍有三源漂移（live，非假設）
SKILL.md L31/97/112/209 硬寫 `13,000`（**機械重驗確認 4 處**）；core.md §Framework Integrity 及 measure.sh L77 現行 cap 為 `19,000`。Lesson 2026-05-31f-B（三源矛盾）正在復發。守衛需「canonical 來源唯一性」驗證，SKILL.md 是已確認的修正目標。
> 來源：主對話 `grep -n "13,000" .claude/skills/autoload-evolution/SKILL.md` → L31/97/112/209 [HIGH]

### F4 — §R-survival 原語已存在，守衛是泛化而非新建（R2 支持）
`measure.sh --gate` 的 `grep -c "^## §R" core.md == 11` 是機械化 allowlist 原語。守衛是把這模式從「header 存在」泛化到「diff 後 anchor 內容非 stub + MEMORY Lesson 行未被移除」。無需新 SKILL。
> 來源：measure.sh L89-91 [HIGH]

### F5 — fail-open 約束：使用者確認門不能放 PreToolUse hook
MEMORY Lesson 2026-06-04-B + branch-isolation-guard.sh：共用 PreToolUse hook 必 fail-open（exit 0 + warn），否則阻擋背景自動化 commit。因此 **user-confirm gate 只能活在互動式 autoload-evolution flow**（人在場的 Phase 4→5），共用 hook 只能 warn。
> 來源：MEMORY Lesson 2026-06-04-B [HIGH]

### F6 — 外部工具 SOTA：有 cap 無 value-scored allowlist
- **Token Guard**（GitHub Marketplace）：tiktoken 計數 `.claude/**`/CLAUDE.md，超 cap 失敗 PR，可設 max_tokens。**無 allowlist 或 prune-diff 機制**。[HIGH，親驗 Marketplace] https://github.com/marketplace/actions/token-guard-llm-token-limit-checker
- **size-limit**（JS）：每 commit CI 計算 byte/time，超 limit 擲錯。**「no override mechanism」**——hard gate 無豁免。[HIGH，親驗 GitHub repo] https://github.com/ai/size-limit
- **ROI-weighting**（Medium, Fahey 2025）：壓縮低價值段比高價值更積極——最接近 value-score 概念，但無實作工具。[MEDIUM，二手文章] https://medium.com/@fahey_james/token-budgeting-strategies-for-prompt-driven-applications-b110fb9672b9

**Insight**：現有工具全是「量 + cap」，**無一做「diff × value-score」**。workspace 的 anchor-survival check 是這空白的具體填補。

---

## 2. 落點判定：擴展 3 處，均非新建

1. **擴展 measure.sh**：加 `--value-check`，在 §R-header 存活基礎上，加 named anchor 內容非 stub 驗證（grep 條文行數 > N）。healthcheck.sh 呼叫 `measure.sh --gate` 補整合缺口。確定性 R5 工作，0 新檔。
2. **擴展 autoload-evolution SKILL Phase 4**：Phase 4a 後加 `prune-diff 驗證`——掃描移除行，若含 allowlist anchor（`^## §R[0-9]`、`Lesson YYYY-MM-DD`、`falsifiable`）則列出並要求使用者確認（互動式 gate）。≤20 行 diff。**同時修正 L31/97/112/209 的 stale 13,000**。
3. **memory-compactor 加 post-prune grep 驗證**：compactor 完成後在 output（已有「壓縮前/後行數」）加 `grep -c "^- Lesson" MEMORY.md >= N_before`。把 #448 advisor 手動 grep 自動化，填面 B 缺口。

新建 SKILL 違 R2 + Lesson 2026-06-04-E。

---

## 3. 守衛設計骨架

```
面 A — auto-load 修改後（Phase 4a / post-Edit）：
  [MEASURE]  wc -c 5 files → total bytes
  [CAP]      > 19,000 → warn（soft cap；hard block 需實證計劃書）
  [ANCHOR-SURVIVAL]
    grep "^## §R" core.md | count == 11           → §R 條文存活
    grep 驗證指令 keyword (wc -c cmd) > 0          → 驗證指令非 stub
  [PRUNE-DIFF]（僅精簡操作，互動式）
    diff before/after → 移除行過濾 allowlist pattern
    命中 → 列出 + 等待使用者 ACK；無命中 → 自動通過

面 B — MEMORY compaction 後（post-compactor）：
  [LESSON-COUNT]    grep -c "^- Lesson" after >= before
  [TODO-SURVIVAL]   grep "## 待辦" after exist
  [RECENT-SESSIONS] 最近 5 session 標題存在
  有缺口 → FAIL，要求 compactor 重跑或使用者確認
```

---

## 4. 關鍵風險與下限約束

- **單一 canonical 單位**：byte，唯一來源 core.md §Framework Integrity。SKILL.md 4 處 stale 13,000 須同步修正（優先，防三源矛盾）。
- **R1–R12 不可丟**：allowlist 最小集 = `^## §R[0-9]` × 11 + 驗證指令 keyword（`wc -c ... | tail -1` verbatim）。
- **cap 上調須實證計劃書**：守衛自身 byte 增量若造成 cap 壓力，走 evidence plan；不接受守衛反推湊 byte（core.md §Framework Integrity）。
- **fail-open 鐵律**：commit hook 只 warn；user-confirm 只在互動式 autoload-evolution Phase 4→5。

---

## 5. Falsifiable Prediction 候選

- P1：注入移除 `## §R3` 的 diff → `measure.sh --gate` 或 Phase 4 守衛回 warn/非零。
- P2：僅移除 TYPE-C rationale 段（無 §R、無 Lesson 行）→ 守衛靜默通過 exit 0。
- P3：5 檔 total byte > 19,000 → `measure.sh --gate` exit 1（已實作，需整合 healthcheck）。
- P4：compactor 壓縮後 `grep -c "^- Lesson" MEMORY.md` 較前少 → post-prune FAIL。

---

## 6. 信度分層彙整

| 來源 | 關鍵聲明 | 信度 | URL |
|------|---------|------|-----|
| Token Guard (Marketplace) | tiktoken cap，無 allowlist | HIGH | https://github.com/marketplace/actions/token-guard-llm-token-limit-checker |
| size-limit (GitHub) | hard gate「no override」 | HIGH | https://github.com/ai/size-limit |
| ROI-weighting (Medium) | 低價值段更積極壓縮 | MEDIUM | https://medium.com/@fahey_james/token-budgeting-strategies-for-prompt-driven-applications-b110fb9672b9 |
| measure.sh | --gate byte cap + §R header check | HIGH | 親讀 L77-96 |
| healthcheck.sh | 0 measure.sh 引用（整合缺口） | HIGH | 主對話 grep = 0 |
| autoload-evolution SKILL.md | 4 處 stale 13,000 | HIGH | 主對話 grep L31/97/112/209 |
| MEMORY | over-prune 12 Lessons / 三源矛盾 / 545 餘裕 | HIGH | repo 一手 |

---

## 相關檔案清單

- `scripts/measure.sh`（L77-96 byte cap + §R header；L11-13 --gate 模式）
- `scripts/healthcheck.sh`（整合缺口：無 measure.sh --gate 呼叫）
- `.claude/skills/autoload-evolution/SKILL.md`（L31/97/112/209 stale 13,000；Phase 4a 擴展點）
- `.claude/agents/memory-compactor.md`（「永不移除」LLM 指令，無機械驗證）
- `.claude/rules/core.md`（§Framework Integrity，canonical cap 定義）

# Auto-Load Token 預算守衛 — 可執行計劃書

> **配套研究**：`2026-06-04-token-guardian-research.md`
> **落點**：**擴展既有 3 處**（measure.sh + autoload-evolution SKILL + memory-compactor）——非新建
> **狀態**：研究+計劃完成，**APPLY 待 gated session 核准**（改 measure.sh 屬 harness 核心 + 觸及 §Framework Integrity 引用區）
> **Harness Loop**：OBSERVE->IDENTIFY->PROPOSE->TEST->APPLY->RECORD

---

## extend vs build 判定

**EXTEND（擴展 3 處）**。`measure.sh --gate` 的 `grep "^## §R" == 11` 已是 allowlist 原語；autoload-evolution SKILL Phase 4a 已有 PGE gate；memory-compactor 已有「前/後行數」output。守衛 = 泛化既有原語，非新建。新建違 R2 + Lesson 2026-06-04-E（孤兒）。

---

## OBSERVE（現況，機械驗證）

| 觀察項 | 證據 | 指令 |
|--------|------|------|
| auto-load 18,455/19,000 餘 545 | 近滿 | `wc -c CLAUDE.md .claude/rules/{...}.md \| tail -1` |
| measure.sh --gate §R check = 11 | allowlist 原語 | `grep -n RB_CORE scripts/measure.sh` |
| healthcheck 0 引用 measure.sh | 整合缺口 | `grep -c measure.sh scripts/healthcheck.sh` -> 0 |
| SKILL.md 4 處 stale 13,000 | 三源漂移 | `grep -n 13,000 .claude/skills/autoload-evolution/SKILL.md` |

---

## IDENTIFY（3 缺口）

1. measure.sh §R check 只驗 header 存在，不驗條文非 stub。
2. healthcheck.sh 不呼叫 measure.sh --gate（兩者斷開）。
3. memory-compactor「永不移除」無機械驗證（over-prune 12 Lessons 元兇）。
4. （附帶）autoload-evolution SKILL.md 4 處 stale 13,000（三源矛盾復發）。

---

## PROPOSE（交付物 — 改 3 處 + 修 stale）

### 改動 1：measure.sh 加 `--value-check`
§R-header 存活之上，加 named anchor 內容非 stub（grep 各 §R section 行數 > 閾值，防條文被掏空成標題殼）。

### 改動 2：healthcheck.sh 整合 measure.sh --gate
healthcheck 末尾呼叫 `bash scripts/measure.sh --gate` 補整合缺口（FAIL 計入總數）。

### 改動 3：autoload-evolution SKILL Phase 4a 加 prune-diff 驗證
diff before/after -> 移除行過濾 allowlist pattern（`^## §R[0-9]`、`Lesson YYYY-MM-DD`、`falsifiable`）-> 命中則列出 + 互動式使用者 ACK。**同時修 L31/97/112/209 stale 13,000 -> 19,000**（消三源矛盾）。

### 改動 4：memory-compactor 加 post-prune grep 驗證
compactor output 加 `grep -c "^- Lesson" MEMORY.md >= N_before`，缺口 -> FAIL 要求重跑/確認。

---

## TEST（APPLY 後驗收，全 bash 可驗）

| # | 條件 | 指令 |
|---|------|------|
| T1 | healthcheck 整合後仍 PASS | `bash scripts/healthcheck.sh` FAIL=0 |
| T2 | §R 移除被擋（P1） | 注入移除 `## §R3` 的暫存 diff -> `measure.sh --value-check` 非零 |
| T3 | TYPE-C 移除靜默通過（P2） | 僅移除無 §R/Lesson 的 rationale -> exit 0 |
| T4 | byte cap 整合（P3） | 假造 5 檔 > 19,000 -> `measure.sh --gate` exit 1 |
| T5 | compactor post-prune（P4） | 模擬 Lesson 行減少 -> post-prune FAIL |
| T6 | stale 修正 | `grep -c 13,000 .claude/skills/autoload-evolution/SKILL.md` -> 0 |

---

## Falsifiable Prediction

**改動**：measure.sh +--value-check / healthcheck 整合 / autoload-evolution Phase 4a + 修 4 處 stale / memory-compactor post-prune（**0 動 §R1-R12 條文本身，只加守衛原語**）。
**預測**：
1. healthcheck FAIL=0（整合後）；
2. §R 移除測試非零（T2）；TYPE-C 移除 exit 0（T3）；
3. stale 13,000 歸零（T6）；
4. auto-load byte 不變 18,455（守衛改 scripts/SKILL，非 auto-load 5 檔）；
5. §R header 仍 == 11。
**驗證指令**：
```bash
bash scripts/healthcheck.sh | tail -1
wc -c CLAUDE.md .claude/rules/{core,context-management,output-discipline,subagent-strategy}.md | tail -1  # 18,455 不變
grep -c "^## §R" .claude/rules/core.md   # 11
grep -c "13,000" .claude/skills/autoload-evolution/SKILL.md   # 0
```
**失敗判定**：任一不成立 -> REFUTED 誠實回報。

---

## APPLY 順序（gated）

1. Read measure.sh + healthcheck.sh + autoload-evolution SKILL.md + memory-compactor.md（§R8 改前先讀，4 檔皆 caller/契約）。
2. Edit 4 處（surgical）。
3. 跑 T1-T6（T2/T3/T4/T5 須注入測試 diff 實測，非自評）。
4. 原子 commit 區塊。

---

## RECORD

APPLY 後 MEMORY ≤3 行 + lesson。守衛首次攔截 over-prune 時記 Lesson（補 #448 手動 grep 自動化的閉環）。

---

## 下限約束

- 單一 canonical 單位 byte，唯一來源 core.md §Framework Integrity。
- allowlist 最小集 = `^## §R[0-9]` × 11 + 驗證指令 verbatim。
- cap 上調須實證計劃書（守衛 byte 增量不得反推湊）。
- fail-open：commit hook 只 warn；user-confirm 只在互動式 autoload-evolution。
- §R1-R12 條文一字不動（守衛只加驗證原語，不改規則內容）。

# 平行研究→報告 Agent 艦隊 — 可執行計劃書

> **配套研究**：`2026-06-04-research-fleet-research.md`
> **落點**：**改進既有 `overnight-research` SKILL**（非新建 — 違 R2）
> **狀態**：研究+計劃完成，**APPLY 待 gated session 核准**（改既有 SKILL，逐 Phase diff）
> **Harness Loop**：OBSERVE→IDENTIFY→PROPOSE→TEST→APPLY→RECORD

---

## extend vs build 判定

**EXTEND（改進既有）**。`overnight-research` SKILL 已有 fan-out / 寫盤 / 迭代 / keepalive / checkpoint 骨架（機械重驗確認）。新建 SKILL 重複骨架 → 違 R2 + Lesson 2026-06-04-E（孤兒）。

---

## OBSERVE（現況，機械驗證）

| 觀察項 | 證據 | 指令 |
|--------|------|------|
| Phase 2 inline 回傳 | SKILL.md L36 | `grep -n inline .claude/skills/overnight-research/SKILL.md` |
| 有 REPORT_PATH 寫盤 | L42/L102 | 同上 grep REPORT_PATH |
| 有 keepalive heartbeat | L118-121 | grep keepalive |
| workflow 不跨 session resume | dynamic-workflows-harness L128 | 親讀 |

---

## IDENTIFY（4 個精確 gap）

1. Phase 2 subagent inline 回傳（撞 context 累積）→ 改 Write scratch 檔。
2. Phase 3 整份一次生成（撞 output-token-limit）→ reducer 逐節串流。
3. citation 無機械 re-verify（SELF-ROUTE 65% 歸錯源類風險）→ 加 grep-back pass。
4. 無 disk-resume（session kill 後從頭）→ Phase 0 加 scratch 掃描。

---

## PROPOSE（交付物 — 改 overnight-research SKILL.md 4 處）

### 改動 1：Phase 2 — scratch-write
subagent 指令改為「分析後 Write `research/scratch/source-N.md`（格式：url/claims[含 verbatim 引文+位置]/source 層級），inline 只回 ≤200 token reference」。parent 加 `ls research/scratch/source-N.md` 機械確認（subagent verdict 非證據）。

### 改動 2：Phase 3 — reducer 逐節串流
報告生成改為 for-section 迴圈，每節獨立讀相關 scratch + Write append，每節後 checkpoint `wc -m`。

### 改動 3：Phase 4（新增）— citation 機械重驗
每個報告 [citation] 的 verbatim 引文 grep 回 scratch 檔，MISS 標 ⚠️ 不刪。

### 改動 4：Phase 0 — disk-resume
`ls research/scratch/source-*.md | wc -l` → 已存在的 source 跳過，從缺口續跑。

### 配套：`research/scratch/` 加入 .gitignore（machine-local 中間檔，不 commit — 對齊 Lesson 2026-06-04-B SYNC-STATUS untrack 原則）。

---

## TEST（APPLY 後驗收）

| # | 條件 | 指令 |
|---|------|------|
| T1 | SKILL 合法 | `bash scripts/healthcheck.sh` FAIL=0 |
| T2 | scratch-write 機制 | 跑 2-source 小研究 → `ls research/scratch/source-*.md` = 2 |
| T3 | reducer 逐節不撞 limit | 生成 ≥10k 字報告無 output-limit error → `wc -m` ≥ 10000 |
| T4 | resume | kill 後重跑 → 已有 scratch 跳過，覆蓋率一致 |
| T5 | citation grep-back | 注入 1 個 scratch 無對應引文的假 citation → 標 ⚠️ |

---

## Falsifiable Prediction

**改動**：overnight-research SKILL.md 4 處改動 + .gitignore 加 `research/scratch/`（0 動 §R 條文 / 0 動 auto-load byte）。
**預測**：
1. healthcheck FAIL=0；
2. 2-source 測試 scratch 檔 = 2（T2）；
3. 10k 字報告生成無 output-limit error（T3）；
4. SKILL 數不變（26，改既有非新增）；
5. auto-load byte 不變 18,455（SKILL 非 auto-load）。
**驗證指令**：
```bash
bash scripts/healthcheck.sh | tail -1
ls .claude/skills/ | grep -v RESOLVER | wc -l   # 26 不變
ls research/scratch/source-*.md 2>/dev/null | wc -l   # 測試後 = source 數
git check-ignore research/scratch/dummy   # 確認 ignore 生效
```
**失敗判定**：任一不成立 → REFUTED 誠實回報。

---

## APPLY 順序（gated）

1. Read overnight-research SKILL.md 全文（§R8 改前先讀）。
2. Edit 4 處（surgical，不重寫整個 SKILL）。
3. .gitignore 加 `research/scratch/`。
4. 跑 T1-T5（T2/T3 須 instrumented 小研究實測，非自評）。
5. 原子 commit 區塊。

---

## RECORD

APPLY 後 MEMORY ≤3 行 + lesson。若 output-limit 仍復現 → 記 Lesson（reducer 逐節粒度需再細分）。

---

## 下限約束

- subagent verdict 非證據：每 scratch 檔 parent 必 `ls` 確認。
- reducer 只讀 scratch verbatim 欄，不從 context 推 citation（幻覺防護）。
- 「1,000-2,000 token distilled」是實測值非設計上限。
- §R1-R12 / auto-load 一字不動（本 SKILL 不碰）。

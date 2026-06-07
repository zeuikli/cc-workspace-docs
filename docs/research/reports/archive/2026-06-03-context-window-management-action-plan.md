# Context Window 管理 — Workspace 落地計劃書

> **配套報告**：`2026-06-03-context-window-management-deep-research.md`
> **日期**：2026-06-03 ｜ **狀態**：proposal（待使用者 gate 後逐項執行）
> **約束**：auto-load 現況 **16,927 bytes**（canon 區間 13K–18K，剩 ~1,073 bytes 至 18K 上限）。所有 auto-load 改動須在此預算內，淨增 byte 須量測。
> **原則**：每項皆 ① 具體檔案編輯 ② 機械可驗證 verify command ③ 回滾方式。無「consider X」。

---

## 0. 優先序總覽

| # | 項目 | 類型 | 風險 | auto-load byte 影響 | 優先 |
|---|------|------|------|------|------|
| P1 | Cache 命中率量測腳本 | 新增 script | 低（純觀測） | 0（不入 auto-load） | ⭐⭐⭐ |
| P2 | English-first instructions 規則（CJK 稅對策） | auto-load 微調 | 低 | +~120 bytes | ⭐⭐⭐ |
| P3 | Post-compact 品質驗證 SOP | 新增 ref + 1 行 auto-load 指標 | 中 | +~80 bytes | ⭐⭐ |
| P4 | Compact Instructions 加入 context-management.md | auto-load 微調 | 低 | +~150 bytes | ⭐⭐ |
| P5 | Context-rot 自檢清單（on-demand ref） | 新增 ref | 低 | 0（on-demand） | ⭐⭐ |
| P6 | AGENTS.md sub-agent context 隔離 SOP | 文件補強 | 低 | 0（非 auto-load） | ⭐ |

> 預估 auto-load 淨增 ~350 bytes → 17,277 bytes，仍 < 18K 上限。**P2+P3+P4 三項合併前須先跑 P1 釋出餘裕觀測**；若逼近上限，依 core.md §Framework Integrity 先砍 TYPE C/D。

---

## P1 — Cache 命中率量測腳本（最高價值，純觀測零風險）

**Gap**：context-management.md 主張「static-first cache」「mid-session 禁止改 CLAUDE.md」，但 workspace **從未量測實際 cache 命中率**——規則無數據背書。

**研究接地**：報告 §4.4 Cache Invalidation 6 觸發事件；§3.3 static-first。Don't Break the Cache（arXiv 2601.06007）：system-prompt-only 快取 78.5% 成本降低。

**具體編輯**：新增 `scripts/measure-cache.sh`，解析 `/usage` 或 session JSONL 的 `cache_read_input_tokens` / `cache_creation_input_tokens`，輸出命中率。

```bash
# scripts/measure-cache.sh（骨架）
# 從最近 session transcript 統計 cache_read vs cache_creation tokens
# 輸出：cache_hit_rate = cache_read / (cache_read + cache_creation + input)
```

**Verify command**：
```bash
bash scripts/measure-cache.sh && echo "cache hit rate measured"
```
**成功條件**（可機械驗證）：腳本輸出一個 0–1 之間的命中率數字，無 error exit。
**回滾**：刪除 script（不影響任何既有流程）。

---

## P2 — English-first Instructions 規則（CJK token 稅對策）

**Gap**：workspace 繁中優先，但報告 §3.4 量化 CJK 稅 2–3×、Max plan 實際 coding 時間僅英文 30–50%。目前 instructions 全繁中 = 持續付隱形稅。

**研究接地**：報告 §3.4——「English-first prompts：instructions 用英文，僅 user content 用 CJK」是直接對策。

**具體編輯**：`output-discipline.md` 加一條（**注意：規則本身用英文寫以身作則**，但不改變「回應使用者用繁中」的鐵律）：

```markdown
## Token 效率（CJK 稅對策）
- 內部 instructions/scratchpad/TODO 可用英文（CJK token 膨脹 2–3×，見 research/reports/2026-06-03-context-window-management）；**對使用者的最終回應仍維持台灣繁中**。
```

**Verify command**：
```bash
grep -q "CJK 稅" .claude/rules/output-discipline.md && \
wc -c CLAUDE.md .claude/rules/{core,context-management,output-discipline,subagent-strategy}.md | tail -1
```
**成功條件**：grep 命中 + 總 byte < 18,000。
**回滾**：`git checkout .claude/rules/output-discipline.md`。
**⚠️ R7 衝突注意**：與「繁中優先」鐵律潛在張力——故規則明確界定「僅內部，回應仍繁中」，不 silent fork。

---

## P3 — Post-compact 品質驗證 SOP

**Gap**：context-management.md 有 compact 觸發點（70%），但 **compact 後無任何品質驗證**——無法知道 compact 是否丟了關鍵 context（報告 §3.1：summarization 丟 63% 資訊）。

**研究接地**：報告 §3.1 Slipstream（arXiv 2605.08580）trajectory-grounded 驗證；Anthropic compaction「工具存在時靜默失敗」。

**具體編輯**：新增 `.claude/refs/post-compact-checklist.md`（on-demand），context-management.md 加 1 行指標：

```markdown
- **Compact 後自檢**（見 refs/post-compact-checklist.md）：① 任務目標仍在？② 安全紅線仍在？③ 最近工具結果未失真？任一失 → `/rewind`。
```

**Verify command**：
```bash
test -f .claude/refs/post-compact-checklist.md && \
grep -q "Compact 後自檢" .claude/rules/context-management.md && echo OK
```
**成功條件**：兩條件皆真。
**回滾**：刪 ref + `git checkout context-management.md`。

---

## P4 — Compact Instructions 加入 context-management.md

**Gap**：現有 compact hint 只列「保留/捨棄」，未利用研究證實的 Compact Instructions 模式。

**研究接地**：報告 §3.1 / §4.1——CLAUDE.md 加 Compact Instructions → **49% 品質改善**【LOW，但成本零、無副作用，值得試】。

**具體編輯**：強化 context-management.md 第 11 行的 compact hint，加入 file path / error string 保留指示（呼應 morphllm「rewritten error messages 摧毀 debugging value」）：

```markdown
`/compact 保留：任務目標、最近工具結果（含完整 file path 與 error string 原文，勿改寫）、安全紅線、慣例、繁中輸出；捨棄：中間步驟詳情、已被取代的探索路徑`
```

**Verify command**：
```bash
grep -q "勿改寫" .claude/rules/context-management.md && echo "compact instructions enhanced"
```
**成功條件**：grep 命中。
**回滾**：`git checkout context-management.md`。

---

## P5 — Context-rot 自檢清單（on-demand ref）

**Gap**：無系統化的 context-rot 識別機制。報告 §2.5 + §3.5：context rot 是被低估的 agent 失敗主因。

**研究接地**：報告 §4 Anthropic context rot 四模式（Poisoning/Distraction/Confusion/Clash）+ LogRocket 症狀（忽略約束/重複被拒解法/需不斷重述）。

**具體編輯**：新增 `.claude/refs/context-rot-symptoms.md`（on-demand，零 auto-load 成本）：

```markdown
# Context Rot 識別與處置
症狀：① 忽略已建立約束 ② 重複被拒絕的解法 ③ 需不斷重述指令 ④ 推理前後矛盾
四模式（Anthropic）：Poisoning（錯誤資訊污染）/ Distraction（無關內容稀釋）/ Confusion（衝突指令）/ Clash（新舊矛盾）
處置：prompt anchoring（關鍵規則放 prompt 邊緣）→ 自然 checkpoint 後 compact → 嚴重則 /clear
```

**Verify command**：
```bash
test -f .claude/refs/context-rot-symptoms.md && echo OK
```
**成功條件**：檔案存在。
**回滾**：刪檔。

---

## P6 — AGENTS.md sub-agent context 隔離 SOP

**Gap**：AGENTS.md 已標「Highest discovery rate location for sub-agents」，但無 sub-agent context 隔離的具體驗證 SOP（既有 consolidated report 提到 Cold Start Test 概念但未落地）。

**研究接地**：報告 §3.5 LangChain Isolate 策略；§4.1 Claude Code sub-agent 收 focused clean context。

**具體編輯**：AGENTS.md 加一段「Sub-agent Context 隔離自檢」——委派前確認 prompt 已包含 sub-agent 所需全部 context（因其不繼承 parent），且用 `<untrusted_objective>` 包裹外部輸入（呼應 subagent-strategy.md Agent Input Security）。

**Verify command**：
```bash
grep -q "Context 隔離自檢\|不繼承 parent" AGENTS.md && echo OK
```
**成功條件**：grep 命中。
**回滾**：`git checkout AGENTS.md`。

---

## 執行順序建議

1. **先 P1**（純觀測，建立 cache 命中率 baseline 數據）→ 為後續 cache 規則提供實證。
2. **P5 + P6**（零/低 auto-load 成本，on-demand + 非 auto-load）。
3. **P2 + P3 + P4**（auto-load 微調，合併一次量測 byte，確保 < 18K）。

**每項 APPLY 前** gate 使用者（破壞性雖低，但動 auto-load 規則影響全 session 行為）。**APPLY 後** MUST 跑該項 verify command + `bash scripts/healthcheck.sh`，展示前 5 行/後 5 行輸出（R4/R12）。

## 全域驗證（所有改動完成後）

```bash
# 1. auto-load byte 未超上限
wc -c CLAUDE.md .claude/rules/{core,context-management,output-discipline,subagent-strategy}.md | tail -1
# 預期 total < 18000

# 2. healthcheck 通過
bash scripts/healthcheck.sh
# 預期 FAIL=0

# 3. measure.sh byte-check 通過
bash scripts/measure.sh
```

## 與既有規則的衝突盤點（R7）

| 改動 | 潛在衝突 | 處置 |
|------|---------|------|
| P2 English-first | 「繁中優先」鐵律 | 規則明確界定「僅內部 instructions，回應仍繁中」，非 silent fork |
| P4 compact 強化 | 既有 compact hint | 直接強化同一行，非新增矛盾條文 |
| P2/P3/P4 byte 增量 | 18K 上限 | 合併量測；逼近則依 core.md 先砍 TYPE C/D |

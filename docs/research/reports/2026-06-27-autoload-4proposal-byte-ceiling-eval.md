---
date: 2026-06-27
status: 評估完成，待人工選路徑後實作
method: 逐提案 auto-load worthiness + byte 量測 + 下沉候選 + 分階段 eval-gated 計劃
proposals: [rewind-06-25, self-prompting-06-23, mcp-auth-06-22, loop-design-06-26]
scope: "4 個 auto-load 待審提案 vs 19,000B 門檻"
type: evaluation-report / 實證計劃書
---

# Auto-load 4 提案 byte 天花板評估 — 2026-06-27

## 1. 約束（量測，非估計）

```
CLAUDE.md 1702 · core.md 9797 · context-management 1758 · output-discipline 1458
· subagent-strategy 3271 · README 1012  → total 18,998 / 19,000B（剩 2B）
```

core.md §Framework Integrity 三段門檻：≤13,000 理想｜13,000–19,000 **正當化區間（現況）**｜>19,000 觸發審視。當前已在正當化區間 → 任何新增須個別正當化；越過 19,000 須「同等級實證計劃書背書，**不接受為塞單一新規則反推湊 byte**」。並受「≤1 規則/cycle、≤50 行 diff」約束。

→ 4 提案天真全加 ≈ +640B → ~19,640B，**同時違反 3 條**（破 19,000 / 反推湊 byte / 一次 4 條）。security 兩項已落地是因 security-hygiene.md 為 on-demand 檔，不在六源預算內——此後路對這 4 項不存在。

## 2. 逐提案 auto-load worthiness（關鍵分析）

判準（core.md）：「只寫無法從 repo 推導的行為契約；可推導資訊＝噪音」＋「移除後 Claude 在哪犯錯？」。**不是每個研究發現都該進 auto-load。**

| 提案 | 目標檔 | 防止的失敗模式 | worthiness | 裁定 |
|------|--------|--------------|-----------|------|
| **loop-design 引用 (06-26)** | core.md | 無——這是**外部文獻 citation**（《Loop Design》作 ground truth），不改 in-context 行為 | ★☆☆ 最弱 | **不進 auto-load** → 收入 `.claude/refs/harness-loop.md` 註腳即可；auto-load 放 citation = 噪音 |
| **mcp-auth 隔離 (06-22)** | subagent-strategy | 誤選整合方式（auth token 進 context） | ★★☆ | **折疊**：已新增的 security-hygiene「Agent 部署 IPI 防護」涵蓋鄰近主題；auto-load 僅需 1 行指針（~80B）非整段 ~200B |
| **rewind 恢復 (06-25)** | context-management | 誤以為 /clear 後不可恢復 | ★★☆ | **就地擴句**：檔內已 2 處提 /rewind；於既有行加 `（含 /clear 後恢復, v2.1.191+）` ~60B，非新增 2 行 |
| **self-prompting (06-23)** | subagent-strategy | 預設「人工提示每步」設計模式 | ★★★ 最強 | **唯一值得完整進 auto-load**（~200B）；行為契約、不可從 repo 推導 |

**結論**：真正需要 auto-load 空間的只有 self-prompting（~200B）；其餘 3 項降為「不進／指針／擴句」，總新增從 ~640B 壓到 **~340B**。

## 3. 下沉候選（騰 ~340B+ 以維持 ≤19,000）

core.md 為最大宗（9,797B）。低頻 / 可推導 / 已有 ref 重複的下沉標的：

| 候選 | 現 byte | 下沉後 | 淨省 | 風險 |
|------|--------|--------|------|------|
| `## 暫存 / Bash 慣例`（276B）細節 → `.claude/refs/`，auto-load 留 1 行指針 | 276 | ~90 | **~186B** | 低（操作慣例，低頻；hook 防呆仍在） |
| 跨 section 括號內 citation／refs 指針重複（如「（見 …best-solution）」出現多次） | ~分散 | 精簡 | **~120–200B** | 低（指針非鐵律句） |
| `## The Loop（元迴圈）`（353B）與 CLAUDE.md 六階段敘述重疊段 | 353 | ~250 | **~100B** | 中（需確認不損 canonical 定義） |

下沉總潛力 ~400–480B > 需求 ~340B → **Path X（下沉後納入）數學可行**。

## 4. 實作計劃書（eval-gated，分階段）

core.md 要求變更附 **Falsifiable Prediction + eval 條件**，走 `/autoload-evolution` 閉環（≤1 規則/cycle、回歸 ≥5pp → git revert）。建議 4 個 cycle：

**Cycle 1（下沉騰空間，不加規則）**
- 動作：暫存/Bash 慣例細節 + 重複 citation 下沉至 refs。
- Falsifiable：下沉後 `wc -c` 六源 ≤ 18,650B（騰出 ≥350B headroom）。
- eval：healthcheck FAIL=0；六階段 behavioral 全存活；下沉內容在 ref 可 grep 到。

**Cycle 2（self-prompting → subagent-strategy）**
- Falsifiable：`grep -qE 'self-prompt|自我提示.*系統' subagent-strategy.md` 通過；六源 ≤19,000。
- eval：模擬 fan-out 任務，agent 不再預設逐步人工提示。

**Cycle 3（mcp-auth 指針 + rewind 擴句）**
- Falsifiable：兩 grep 閘門通過（mcp-auth `auth.*isolat`；rewind 收緊為 `clear.*rewind|v2.1.191`，修原 false-positive grep）；六源 ≤19,000。

**Cycle 4（loop-design → ref，非 auto-load）**
- 動作：citation 寫入 `.claude/refs/harness-loop.md`；EVOLUTION-QUEUE 標 `applied(ref)` 非 auto-load。
- Falsifiable：`grep -q 'Loop Design' .claude/refs/harness-loop.md`；**auto-load byte 不增**。

每 cycle 後量六源 byte + healthcheck，回歸 ≥5pp 即 `git revert` 該 cycle。

## 5. 兩條路徑與建議

- **Path X — 下沉後納入（建議）**：依 §4 四 cycle，維持 ≤19,000，honor 全部框架門檻。最穩。
- **Path Y — 上調 cap 至 ~19,500**：core.md 允許「同等級實證計劃書背書」上調，但明文「不接受為塞單一新規則反推湊 byte」。為 4 條小規則上調 cap 正中此禁區 → **不建議**。

**建議採 Path X**。淨效果：auto-load 不增反可能微降（self-prompting 進、loop-design 不進、下沉 > 新增），同時 3 條框架紀律全守。

## 6. 待人工決策

1. 採 Path X（下沉後納入）抑或調整提案取捨？
2. loop-design 確認「不進 auto-load、收 ref」可接受？
3. §3 下沉候選是否同意（特別是 The Loop 元迴圈段，動 canonical 定義須你點頭）？

確認後我逐 cycle 走 `/autoload-evolution`，每 cycle 附 grep + byte + healthcheck 證據。

---

## 7. Pilot Review 終裁（2026-06-27，/pilot-review full）— 推翻部分 draft

四維評審（D1 haiku / D2 sonnet / D3 opus / D4 fable）對上述 draft 計劃書的修訂。主對話親跑復驗所有 load-bearing 宣稱。

**Verdict 鏈**：D1 FLAG · D2 FLAG · D3 FLAG · D4 APPROVE_WITH_CONDITIONS（REVISE_THEN_PROCEED）。

**被推翻/修正的 draft 判斷（均已機械復驗）**：
1. **wc 命令不能下沉至 prompt-lifecycle.md**（D4-CRITICAL，已驗）：prompt-lifecycle paths=`.claude/rules/**`,`CLAUDE.md`,`research/prompts/**`，純查詢 session 不載入 → 問「幾 byte」時取不到命令。§4 Cycle 1 的 (a) 取消，wc 留 core.md L78 原位。
2. **self-prompting 不該進 auto-load**（D4-GAP，最重要）：「build self-prompting system」原則已由 Routines／multi-mode-agent／dynamic workflows 架構落地；grep 通過＝文字存在≠行為改變。§2 評 ★★★ 過高 → 降為 **defer，待提行為改變證據**。
3. **上調 cap 至 21,000B 拒絕**（D4-ARBITRATE）：屬「架構論述」非「同等級實證計劃書」，違反 core.md「不接受反推湊 byte」。
4. **byte 估算需實測**（D4）：實測 L4=224B、L17-19=347B、L78=334B；D3 的 ~243B 為估算。
5. **4 提案須分 4 獨立 cycle**（D4-CRITICAL，已驗 SKILL「每 cycle ≤1 規則檔」）：不可批量。
6. **Bash 慣例不動**（D1 主張，D2/D3/D4 同意，有 block-dangerous.sh hook 對應）。

**D4 優先序裁定**：`security（已 applied）> rewind（功能性 ~100B）> self-prompting（存疑 defer）> loop-design（收 ref）> byte 壓縮`。

**修訂後最終建議（取代 §4 Path X 4-cycle）**：
- ✅ 已落地：security ×2（tokenizer + lethal-trifecta，on-demand 不佔預算）。
- ✅ 可做（零風險）：loop-design → `.claude/refs/`（+0 auto-load）；採 D3「90 天門檻重審」治理（非上調 cap）。
- ⚠️ 選做：rewind 單 cycle（~100B，由 L17-19 語義壓縮騰空間；grep 收緊為 `clear.*rewind|v2.1.191`）。
- ❌ defer：self-prompting（無行為證據）、mcp-auth（低優先）、core.md 其餘壓縮、上調 cap。
- **機會成本**：byte 微調 ROI≈0；力氣優先放 P1 真實交付（Unicode sanitization hook、Omnigent 對照）。

**狀態**：待人工授權後執行（loop-design 收 ref + 門檻重審為預設；rewind cycle 選做）。

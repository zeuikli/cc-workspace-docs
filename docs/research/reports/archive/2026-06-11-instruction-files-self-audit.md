---
title: "Instruction Files 全量自我稽核（CLAUDE.md / rules / refs / skills / agents / memory）"
date: 2026-06-11
status: report-only（未 APPLY；裁決權在使用者）
method: 主對話親讀核心層（auto-load 5 源 + 17 refs + pilot 三件套 + harness-meta + memory 全檔）+ 2× researcher fan-out（autoresearch 系 / domain skills）；所有引用發現經主對話 grep/diff 機械重驗
scope: "CLAUDE.md · .claude/rules/** · .claude/refs/** · .claude/skills/** · .claude/agents/** · .claude/commands/** · memory/**"
session-model: claude-fable-5（settings.json baseline = claude-sonnet-4-6 → 模型世代 drift 為本稽核核心發現之一）
type: audit
---

# Instruction Files 全量自我稽核報告

> **TLDR**：最大問題不是單條規則錯，而是三件事：① 存在**兩套同名但順序相反的六階段 Loop**，14+ 個檔案跟錯邊；② 整個模型層（pilot 三件套、定價、escalation ladder、"Opus is the ceiling"）已因 Fable 5 世代而過期，而 `prompt-lifecycle.md` 自己早已預言此事（「換模型後 auto-load 規則須重評，不可累加沿用」）；③ 多份文件**以壞示範教學**——byte 量測規範漏掉實際載入的檔案、preach Rule of 3 的庫存著 byte-identical 重複檔。
>
> **稽核過程佐證**：兩個 researcher sub-agent 回報 `prompt-lifecycle.md` 與 `harness-meta-GOTCHAS.md` 為「死檔案」，經主對話親驗均存在（後者為 core.md 路徑寫法誤導）——`unverified_success` 閘門對最強模型仍 load-bearing 的現場證明。

---

## 1. 互相矛盾（雙方原文）

### 1a. 兩套 canonical Loop，TEST/APPLY 順序相反（最嚴重的結構矛盾）

- `CLAUDE.md:8` / `core.md:19`：「**OBSERVE→IDENTIFY→PROPOSE→APPLY→TEST→RECORD**」（先改後測）
- `refs/harness-loop.md:14`（自稱「本檔為 workspace **唯一 canonical** loop 定義」）：表格順序 OBSERVE→IDENTIFY→PROPOSE→**TEST→APPLY**→RECORD（「TEST｜Apply 前預檢」）
- 跟隨後者：`pilot-shared-preflights.md:126`、`eval-designer/SKILL.md:136`、**14+ 個 SKILL 自我進化表**（`sre/SKILL.md:328`、`finops/SKILL.md:252`、`review-hub/SKILL.md:189` 等，全寫「遵循 OBSERVE→IDENTIFY→PROPOSE→TEST→APPLY→RECORD 閉環」）

兩順序各自說得通（寫 code 先 APPLY 再 TEST；改 harness 先 TEST 提案再 APPLY），但同名六階段、兩檔各自宣稱 canonical（`karpathy-mnilax-best-solution.md:5`「本檔 = canonical」 vs `harness-loop.md`「唯一 canonical」）；且 CLAUDE.md 說「改進/稽核任務走此六階段」用 APPLY→TEST 順序，而真正的改進 loop（harness-loop）卻是 TEST→APPLY。

### 1b. Token budget：同組數字一邊「硬性」一邊「Soft」，且與自身 compact 閾值矛盾

- `context-management.md:18`：「**硬性 Token Budget**…Per-task: **4,000** tokens…Per-session: **30,000** tokens」
- `karpathy-mnilax-best-solution.md:200`（同數字出處）：「Token 預算管理（**Soft Token Budget**）」
- 同檔自我矛盾：compact 閾值「一般任務 **70%**」——70% × 200K = 140K，遠超 30K session 上限；兩規則不可能同時有意義
- `autoresearch/SKILL.md:67`：「Low < 50K；Medium 50-200K；High 200K+…最壞 500K+ per run」——內建 skill 的最低檔位即超 session 預算 1.7×，且從不引用該預算

### 1c. Mid-session 換模型：一邊禁止、一邊指示

- `context-management.md:7`：「**Mid-session 禁止**：① 切換模型」；`prompt-caching-rules.md:76`：「切換 model（haiku → sonnet）= cache 全部失效；mode 切換為 session 結束後動作」
- `haiku-pilot/SKILL.md:173-178`：「**Escalate to Sonnet 4.6**: Same problem failed ≥ 3 times…」+ 診斷流程圖「Still fails (3rd attempt) → Escalate to Sonnet」

escalation gate 字面語義即 mid-session 換模型。可用 sub-agent model override 化解，但兩處文字均未說明橋接，照字面執行必違反其一。

### 1d. Auto-load byte 上限：18,000 vs 19,000；13,000 是否硬牆兩個 GOTCHA 互打

- `core.md:75` / `rules/README.md:3`：「完整區間至 **19,000** 上限」
- `token-waste-audit/SKILL.md:64`：「auto-load > **18,000** bytes（canon 區間上限）→ RTK 風險高」——18.5K workspace 被稽核工具標 HIGH、被 canonical 規則視為合格
- `overnight-research/GOTCHAS.md:16`：「加表格…超過 **13KB 上限**」（當硬牆寫）vs `autoload-evolution/GOTCHAS.md:7`：「13,000 是**軟性目標非硬截斷牆**…16,716 bytes 完整載入無截斷」

### 1e. Security 路由三角矛盾

- `agents/security-auditor.md:102`：「Invoke via: `/ship-review`…or **`/security-compliance` for full OWASP/STRIDE**」
- `security-compliance/SKILL.md:3`：「**Do NOT use for: application security review（→ autoresearch:security）**」——A 導向 B，B 明拒並導向 C
- 另一組：`agents/quick-code-reviewer.md:3`「security audit (use **security-reviewer**)」 vs `agents/security-reviewer.md:3`「Do NOT use for: OWASP…（use **security-auditor**）」 vs `ship-review/SKILL.md:30` fan-out 給 security-auditor

### 1f. Pilot 檔內：修正後數字與殘留舊數字並存

- `sonnet-pilot/SKILL.md:31`：「Cost ratio: Sonnet ($3/$15) vs **Opus ($15/$75)**」——同檔 `:261` 自標 🔴 的「誤用定價」（實際 Opus 4.8 = $5/$25），開頭未改
- `sonnet-pilot/SKILL.md:288` Verification：「**55–65% savings?**」 vs `:265`「Conservative estimate: **30–35%**」
- `opus-pilot/SKILL.md:337`：「**60–75% cost reduction**」 vs `:310`「**−20–35% cost**…（舊『−60–75%』基於誤用的 $15/$75）」
- `haiku-pilot/SKILL.md:13`「節費 **70-85%**」+ `:261`「Actually saving **70–85%**?」 vs `:233`「~70%（非 87%）」

### 1g. 其他已驗證矛盾

- `research-hub/SKILL.md:7` frontmatter 含 `Write` vs `:357`「本 skill allowed-tools **不含** Write」
- `subagent-strategy.md`「child 不 self-retry」 vs `autoresearch/SKILL.md:160`「CRASHED → Fix (**max 3 attempts**)」
- `skill-evolution` rubric 硬限 350 行 vs 其 GOTCHAS 引用的 500 行規範（出處 `skill-authoring.md` **不存在**）
- `commands/memory-compactor.md:11,22` 操作根目錄 `MEMORY.md` vs `core.md:87` canonical 路徑 `memory/MEMORY.md`（根目錄該檔已不存在）

---

## 2. 為更弱模型而存在的規則

### 2a. 模型世代整體 drift（最大宗）

本 session 跑 `claude-fable-5`；`settings.json` = `claude-sonnet-4-6`，`harness-model-fit.json` baseline 同。

| 位置 | 內容 | 狀態 |
|------|------|------|
| `CLAUDE.md:24` | 「預設 Sonnet 4.6」+ 三 pilot 模式 | 模型網格無 Fable |
| `opus-pilot/SKILL.md:212,301` | 「**Opus is the ceiling**. There is no auto-upgrade」「**No upward escalation exists**」 | 事實已錯：Fable 5 在 Opus 之上 |
| `refs/model-selection-grid.md` | Haiku 4.5/Sonnet 4.6/Opus 4.8 路由 + trial-001 表（`:44` **自註**「該檔不存在於 repo → 數字不可驗證」卻保留） | 漂移 + 自承不可驗證 |
| `refs/pilot-shared-preflights.md:85-99` | CLI v2.1.158 flag 驗證、定價矩陣、「Opus 4.8 tokenizer 多耗 ~35%」 | 版本 pin 時效快照 |
| `memory/MEMORY.md:109` | 待整合洞察 #4「@Mnilax 7.30：**Fable 5** silent fallback…→ CLAUDE.md」 | workspace 自己已記錄、尚未整合 |

裁決依據已內建：`prompt-lifecycle.md:19`「跨模型沿用 prompt 最壞 −10.77pp → **換模型後 auto-load 規則須重評，不可累加沿用**」。按此規則，pilot 三件套（~62KB）整批到期。

### 2b. 為弱模型行為建模的補丁層

- `core.md` OBSERVE：「讀取 **> 200 行**檔 → limit/offset 分段，每段報 N-M/X 行」+「**不得假設截斷後為空**」——Read 工具預設讀 2000 行；皆為舊弱模型失敗模式
- `haiku-pilot/SKILL.md:61-67` Citation Anchor 密度配額（hard task ≥5 錨點/段）——為 Haiku 編造率 25% 設計的機械代理指標；`sonnet-pilot:117-121` `:LineN` 行號錨點同理
- 各 escalation ladder（「同一問題失敗 ≥3 次 → 升 Sonnet」「3 Haiku failures ≠ Opus needed」）——以舊模型階梯為前提
- `sonnet-pilot/SKILL.md:24-25` **自承**：「Sonnet + SKILL = 283/300; Sonnet Plain = 283/300…**SKILL net gain on routine extraction = 0**」
- `context-management.md:21`「初學者 ~60%」——使用者為 10+ 年 SRE
- UserPromptSubmit hook 每 prompt 注入「先用 1-2 句複述你的理解」——對自然顯露假設的模型是 token 稅

### 2c. 漂移的硬編碼事實

- `commands/quick-commit.md:22` `Co-Authored-By: Claude Sonnet 4.6`
- `overnight-research/references/phases.md:97` 搜尋詞硬編碼「**2024 OR 2025**」（系統性漏 2026 來源）
- `skill-evolution/SKILL.md:180` 硬編碼過去分支 `git push -u origin claude/kind-ritchie-9LFRp`
- `sia/REFERENCE.md:44-46` 模型 ID 展開（`claude-opus-4-8` 等）；`:31` openhands 預設 `gemini-3.1-pro-preview`
- `REFERENCES.md:43` 引「Opus **4.7** Best Practices」blog
- `commands/quick-pr.md:14,31,46` 全程用 `gh` 而遠端 session 無 `gh`（`verified-merge/SKILL.md:35` 有 fallback 註記，quick-pr 無）

### 2d. 死指針 / 誤導路徑（全部親驗）

- `refs/harness-design.md:128,226,234` 三處引「**45% 規則（subagent-strategy.md）**」——該規則已不在 subagent-strategy.md
- `core.md` TEST 段「全文見 `refs/harness-meta` GOTCHAS」——檔案實在 `.claude/skills/harness-meta/references/harness-meta-GOTCHAS.md`，`refs/` 查無（路徑誤導，非死檔）
- `prompt-lifecycle.md:44` 引 `scripts/measure-cache.sh`（不存在）
- `harness-meta/SKILL.md:89` 引 `scripts/schema-verify.sh`（不存在）
- `autoresearch:wiki` 列於 SKILL 路由表但 `commands/autoresearch/wiki.md` 不存在
- `memory/README.md:27-31` 描述的根層 `MEMORY.md`（L2 層）已不存在
- `ship-review/SKILL.md:91` 引 `2026-05-15-vesper` 查無對應歸檔檔名
- `skill-evolution/GOTCHAS.md:7,9` 三引 `skill-authoring.md`（不存在）

---

## 3. 以壞示範教學（違反自己宣講的 pattern）

### 3a. Byte 量測規範保證量錯

canonical 5 源實測 `wc -c` = **18,984 / 19,000**（餘 16 bytes）。但實際 auto-load **還包含 `rules/INDEX.md`（1,584 bytes）**——本 session context 親證載入。實際 ≈ **20,568 bytes，已超 19,000 上限**。`MEMORY.md` Lesson 2026-06-05-F 教「canonical 5 源固定列舉…勿用 glob」——這條 Lesson 把量測鎖死在漏掉真實載入檔的狀態。preach「先量測再改」的體系，量測器本身對不上現實。

### 3b. 「可推導資訊 = 噪音」的規則庫充滿可推導重複

`core.md` APPLY：「**只寫無法從 repo 推導的行為契約**」。然而：同一份 8 列自我進化表逐字複製 **14+ 份** SKILL；GOTCHA footer 逐字複製 **20 份**；agent dispatch 表在 `subagent-strategy.md` / `AGENTS.md §2` / `trigger-index.md` / `RESOLVER.md` / 各 pilot router **五處平行維護**；`AGENTS.md §6b` 27 skill 清單可由 `ls .claude/skills/` 推導。

### 3c. Rule of 3 的守護者庫存 byte-identical 複本

`diff -q` 實證：`security-compliance/references/deploy-and-naming.md` ≡ `sre/references/cathaysec-terraform-deploy-and-naming.md`、`module-examples.md` ≡ `cathaysec-terraform-module-examples.md`（完全相同）；`gcp-modules.md` 兩份 12KB 僅差 4 行。

### 3d. 「重寫該段，不要 ship 標籤」vs 修正以註記疊加

`pilot-shared-preflights.md §B`：「任何 grep 失敗 → **重寫該段**，不要 ship `[unverified]` 標籤作為 workaround」。三本 pilot 對定價錯誤的處理卻是保留錯誤數字 + 疊 🔴 修正註記（每檔 2-3 處），sonnet-pilot 開頭 $15/$75 甚至漏改。

### 3e. eval-designer 自知違規、記錄了、沒修

`eval-designer/GOTCHAS.md:16`：「Phase 2 Checkbox 為 **LLM 判斷非機械驗證**…**違反 R4**」——GOTCHA 入庫，SKILL.md Phase 2 原樣未動；恰為 harness-meta 自己禁止的「只記錄不升格」。

### 3f. MEMORY.md 違反自家格式規範

`core.md`：「≤5 決策…**≤30 行/節**」。實況：`memory/MEMORY.md:153-171` 殘留未展開的 shell heredoc `$(cat <<'EOF')…EOF )`（hook 把 PR body 模板原樣貼入）；多節為整段 PR body 含表格；202 行已超 200 上限。

### 3g. output-discipline ≤150 字與 The Loop 輸出儀式結構性互斥

「純文字回答 ≤ 150 字」vs core.md 同時要求：詮釋 ≤2 句＋假設＋選項（IDENTIFY）＋前 5 後 5 行輸出（TEST）＋checkpoint（RECORD）。例外清單救了多步驟任務，但單步實作任務照規執行即超標。

---

## 4. 刪除 / 保留建議（待使用者裁決）

### 刪（或凍結歸檔）

1. **pilot 三件套 + preflights §C/§E 定價層**（~62KB）——為上一世代模型行為建模；sonnet-pilot 自證 routine 增益 = 0；定價已錯過一輪；escalation 前提（Opus = ceiling）不成立。保留模式概念可重寫為 model-agnostic 一頁。
2. **model-selection-grid.md trial-001 表**——自承來源不存在、與後續 baseline 部分矛盾。
3. **14× 自我進化表 + 20× GOTCHA footer** → 各換一行指針到 `skill-gotcha-protocol.md`。
4. **security-compliance / sre 重複 reference 檔**——留一份、另一處指針。
5. **AGENTS.md §6b skill 清單、trigger-index 與 RESOLVER 重疊部分**——可推導即噪音。
6. **pilot 檔內所有 🔴 修正註記**——直接寫對的數字，舊數字留 git 歷史。
7. **`overnight-research/GOTCHAS.md:16` 13K 硬牆條目**——已被自家實證反推翻。
8. **死指針**：harness-design 45% 規則引用、measure-cache.sh、schema-verify.sh、memory/README 根層 MEMORY.md L2 描述。

### 原樣留（理由）

1. **core.md 不可逆動作 gate、生產紅線、git 流程、No-Commit 紅線**——防「後果不可逆」，與模型強度無關；模型越強動作越快，gate 越 load-bearing。
2. **`unverified_success` 閘門 + 「subagent verdict 非證據」全套**——本稽核中 researcher 誤報兩個「死檔案」被主對話親驗推翻；`harness-meta-GOTCHAS.md:141` 論文結論方向正確（越強的模型需要越強的驗證 harness）。**換更強模型該刪的是行為補丁，該留的是驗證閘門。**
3. **error-handling.md 確定性重試表 / stop_reason 對照**——「判斷 vs 決定」的正確落地。
4. **prompt-caching-rules、cache-health-metrics 機制事實**——平台機制，弱模型無關（門檻表需隨新模型補列）。
5. **語言規則（台灣繁中＋compact 後維持）**——使用者偏好，有實際漂移 Lesson（2026-05-29e）背書。
6. **MEMORY/RATCHET/Lesson 機制本身**——compounding engineering 是真正在運轉的部分；該修的是 hook 貼 PR body 的衛生，不是機制。
7. **prompt-lifecycle.md**——唯一預見本次稽核的規則（「換模型後仍最佳？」）；該升格，不該動。

### 最優先三刀

① 統一兩套 Loop 順序並指定唯一 canonical；② byte 量測對齊實際載入集（含 rules/README.md）；③ 處置 pilot 三件套。

---

## 附錄：稽核方法與信度

- **主對話親讀**：auto-load 5 源（context 內建）、17 refs 全檔、pilot 三 SKILL、harness-meta SKILL + GOTCHAS、memory 全檔、AGENTS.md。
- **Fan-out**：2× researcher（autoresearch 系 + domain skills/agents/commands），其結論經主對話 grep/diff 逐項重驗後才採信。
- **被推翻的 sub-agent 宣稱**（記錄為 unverified_success 範例）：① 「`prompt-lifecycle.md` 不存在」——主對話已親讀全文；② 「`harness-meta-GOTCHAS.md` 零檔案」——實存於 `.claude/skills/harness-meta/references/`，僅 core.md 路徑寫法誤導。
- 本報告為 OBSERVE→IDENTIFY 產出；PROPOSE 僅列建議、未 APPLY。

# Cold Start 對 Workspace 執行效率影響 — 完整評估 + 改善計劃書

> 日期：2026-06-06 ｜ 分支：`feature/coldstart-audit` ｜ 方法：The Loop OBSERVE→IDENTIFY（主對話親量測 + researcher 盤點 + advisor 校正）
> **Cold start 定義**：每次 Claude Code session 啟動到第一個 user prompt 提交前，workspace 強加的所有開銷——分為**時間維度**（wall-clock 啟動延遲）與**空間維度**（注入 context window 的 byte）。兩者是不同問題、不同修法，本報告全程分離。

---

## 0. 一頁式結論（TL;DR）

| 維度 | 現況 | 最大宗 | 可控改善 | 性質 |
|------|------|--------|----------|------|
| **時間** | session-init **~520ms**（cache-hit 仍如此） | schema-lint 迴圈 **416ms（80%）** | 批次化 → **44ms（−89%，省 ~372ms）** | 每 session 一次，非每 prompt |
| **空間** | cold-start 注入 **~39KB** | auto-load 18.7KB / MEMORY 11KB / skills 9KB | MEMORY「上次更新」節 4.4KB 冗餘可壓 | 靜態為主，prompt-cache 後幾乎不再計 token |

**一句話**：時間維度有一個**乾淨的免費勝利**（schema-lint 批次化，省半秒啟動稅）；空間維度的大宗多為 **load-bearing 或已被 prompt cache 攤銷**，真正該動的是 MEMORY 冗餘，其餘是 cap 紀律問題而非速度問題。**不要把兩者混為「執行效率」。**

---

## 1. 量測方法與證據（可重現）

全部數字由**主對話親跑**（確定性 gate 不經 sub-agent，core.md TEST 段 unverified_success 閘門）：

```
session-init.sh × 3:    525 / 513 / 521 ms   (cache-hit 模式)
eval-reminder:          30 ms   (本次 0 byte 輸出 — baseline 未逾 30 天)
user-prompt-submit:     120 ms
單次 python3 -c pass:    23 ms   (10 次 231ms 平均)
schema-lint 區段(15檔):  416 ms  ← 80% of session-init
  └ 改單一 python3 批次:  44 ms   (−372ms, −89%)
```

`claude-progress.json` **不存在** → reminders/active-task 兩個 python3 區段被 `[ -f ]` 跳過（無浪費）。

---

## 2. 時間維度 — 完整項目評估

session-init.sh（510 行）內共 **12 個 python3 子程序**呼叫。每次 spawn python3 ≈ 23ms。cache-hit 路徑下實際觸發者：

| # | 區段 | python3 次數 | 觸發條件 | 耗時估 | 評估 |
|---|------|-------------|----------|--------|------|
| 1 | model-check | 1 | 必跑 | ~23ms | 必要，保留 |
| 2 | HMF 到期檢查 | 1 | harness-model-fit.json 存在 | ~23ms | 必要，保留 |
| 3 | cache-baseline monthly | 1 | baseline.csv + progress.json | ~0ms | progress.json 不存在 → **跳過** |
| 4 | reminders echo | 1 | progress.json 存在 | ~0ms | **跳過** |
| 5 | active-task | 1 | progress.json 存在 | ~0ms | **跳過** |
| 6 | **schema-lint** | **15**（每 agent 一次！） | agents/ 目錄存在 | **416ms** | ⚠️ **80% 開銷源** |
| 7 | model-version reminder | 1 | model 異動時 | 0ms | 條件觸發，未動 |

**根因**：schema-lint 用 `while read … python3 …` 對 15 個 agent 檔**各 spawn 一次 python3 直譯器**。這是純靜態 lint（檢查 frontmatter 必填欄），agent 檔極少變動，每次 cold start 全量重跑 = 純浪費。15 × 23ms ≈ 345ms 全是直譯器啟動成本，非實際工作（單批次只需 44ms）。

**AI 程式碼四大缺陷自檢**（PROPOSE 紀律）：此處命中 **brittle**（per-file spawn 是天真實作）。working（功能對）≠ good。

---

## 3. 空間維度 — 完整 context 注入總帳

| 來源 | Bytes | 性質 | 可控？ |
|------|-------|------|--------|
| auto-load rules（CLAUDE.md + 4 rules） | **18,726** | STATIC，prompt-cache 命中 | 受 19,000 cap 約束 |
| MEMORY.md | **10,976** | 半靜態（session 末更新） | ✅ 可壓 |
| **workspace skills name+description** | **9,167** | STATIC，prompt-cache 命中 | ✅ 可控但 **load-bearing** |
| session-init stdout（cache-hit） | ~612 | 動態為主，**不可快取** | 部分可控 |
| eval-reminder stdout | 0–100 | 條件動態 | — |
| deferred tools list | 小 | harness-owned | ❌ 不可控 |
| UserPromptSubmit（每 prompt） | 150 + 條件 | per-prompt | 可控 |
| **Cold-start 總計（不含 per-prompt）** | **~39,000** | — | — |

### 3.1 三大項逐一評估

**(A) auto-load 18.7KB — 距 19,000 cap 僅剩 274B**
- 已逼滿。**這是 cap 紀律問題，不是速度問題**：prompt cache 首次寫入後，後續 session 命中快取，幾乎不再計 input token 成本，也不增 per-session latency。
- 真正風險：**無 headroom**。下次任何 auto-load 增補都會破 cap → 需先回收。MEMORY 待辦已記「19,000 近滿監控」。

**(B) MEMORY.md 11KB — 唯一真冗餘**
- 88 行（未達 >200 compactor 線），但「上次更新」單節 **4,399B = 全檔 40%**，含 3 個長 session 摘要，**每節遠超 CLAUDE.md 規定 ≤30 行/節**。
- 早期「待辦」節 6 個 `[x]` 已結清項仍佔 534B。
- **這是唯一明確的「冗餘可刪」**，且 MEMORY 每 session 注入、session 末改寫（半靜態，cache 攤銷較差）。

**(C) skills 9.2KB — 最大盲點，但 load-bearing**
- ⚠️ **researcher 初判「workspace 無法控制」錯誤**（subagent verdict 非證據，已親 grep 推翻）。實測：27 個 workspace SKILL.md 的 `name+description` 注入 cold-start skill list = **9,167B（平均 339B/skill）**，**workspace 完全可控**。
- **但這是 load-bearing context**：description 是 Skill tool 的 routing 依據。schema-lint 自己警告「description <20 字 → reduce routing accuracy」。盲目精簡會損害 skill 路由準確度。
- 最重的 5 個：gap-vote(475B)、sia(463B)、harness-meta(450B)、autoload-evolution(445B)、verified-merge(427B)。
- **誠實結論**：skills 是 cold-start 第三大塊、可控，但**多數 load-bearing**——精簡空間有限，且需逐一判斷 routing 影響，非機械可刪。**列入觀察，非首批動作。**

---

## 4. 改善建議（依優先序 + 槓桿標註）

> 每項標明拉哪根槓桿：**[L]=latency 速度** / **[C]=context cap 紀律**。混淆兩者是本評估最易犯的錯。

### P1 — schema-lint 批次化 ⭐ 首推 [L]
- **動作**：將 session-init.sh 的 `while read … python3` 迴圈改為**單一 python3 一次處理全部 agent 檔**。
- **效益**：416ms → 44ms，**省 ~372ms 啟動延遲（−89%）**。
- **誠實定價**：這是「**每 session 一次省半秒**」，不是 per-prompt，也不是「巨大」。值得做是因為**免費**（純實作改寫，零行為改變），不是因為大。
- **風險**：極低。輸出語意不變（同樣印 `⚠️ N agent(s) with schema issues`）。外科刀改動，~15 行。
- **進階選項（不必首批做）**：mtime-gate（agent 檔未變則整段跳過，~100% 省）或移到 PostToolUse-on-agent-edit。複雜度略高，P1 批次化已收 89%，**先做最簡**。

### P2 — MEMORY.md「上次更新」節壓縮 [C]
- **動作**：委派 `memory-compactor` 壓「上次更新」節（4.4KB→目標 ≤1.5KB）+ 刪早期已結清 `[x]` 待辦（534B）。
- **效益**：MEMORY 11KB → ~8KB，恢復「≤30 行/節」紀律。
- **風險**：低，但 **memory-compactor verdict 非證據**——壓完主對話親 grep 確認決策/待辦未遺失（Lesson 2026-06-04-D）。
- **注意**：此為 cap 紀律 + 可讀性，**非速度**——MEMORY 注入早被 prompt cache 攤銷。

### P3 — auto-load headroom 回收（已在 MEMORY 待辦）[C]
- **動作**：執行 MEMORY 既有待辦「壓 TYPE B/C/D 取回餘裕」或 DEFER 控制語義表（~250B）。
- **效益**：274B → 更安全 headroom，容下次 auto-load 增補。
- **不在本報告新建**——已有 proposal（`2026-06-04-12-rule-canon-patch-proposal.md`），不重複造輪子。

### P4 — skills description 觀察項（**不立即動**）[C]
- **判斷**：9.2KB 可控但 load-bearing。精簡 5 個最重 description 至多省 ~1KB，且需逐一驗 routing 不退化。
- **建議**：**列入觀察，非動作**。未來若 auto-load cap 真的撐不住，再以「逐 skill 驗 routing」方式微調最冗長者。當前不值得碰。

### 不建議動的項目（完整性聲明）
- model-check / HMF 檢查（各 23ms）：必要功能，移除即失去 model-drift 偵測與 HMF 到期提醒。
- eval-reminder：本次 0 byte，條件觸發合理。
- auto-load 內容本身：D5 paper + #446 已背書「不動內容」（MEMORY 2026-06-05 記載）。
- deferred tools list：harness-owned，不可控。

---

## 5. 執行計劃書

### Phase 1 — schema-lint 批次化（P1，本 session 可完成）

**成功條件（可機械驗證）**：
1. `bash .claude/hooks/session-init.sh` 輸出語意不變（仍印 skill count、HARNESS_MODEL_VERSION、commit log）。
2. 重量測 session-init 總耗時 **< 200ms**（從 ~520ms 降）。
3. schema-lint 對「故意缺 frontmatter 的測試 agent 檔」仍能印 WARN（功能不退化）。
4. `bash scripts/healthcheck.sh` 通過。

**步驟**：
1. OBSERVE：讀 session-init.sh L479–509 schema-lint 區段，確認輸出格式契約。
2. PROPOSE：單一 python3 heredoc，內部 glob `agents/*.md`、迴圈檢查、累計 `SCHEMA_ISSUES`、印同格式 WARN。
3. APPLY：Edit 替換迴圈（~15 行 diff，外科刀）。
4. TEST：主對話親跑前/後耗時對照 + 故意壞檔測 WARN + healthcheck（展示前5/後5行）。
5. RECORD：Checkpoint + MEMORY session 記錄。

**回滾**：`git revert` 單一 commit；session-init 改動隔離，無連帶。

### Phase 2 — MEMORY 壓縮（P2，可同 session 或獨立）

**成功條件**：
1. MEMORY.md 總 byte < 9,000（從 10,976）。
2. 主對話親 grep 確認：4 個現行待辦全在、Lesson D–H 全在、核心決策全在。
3. 每節 ≤30 行（核對「上次更新」節）。

**步驟**：委派 `memory-compactor` → 主對話 grep 驗證（verdict 非證據）→ commit。

### Phase 3 — auto-load headroom（P3，承接既有 proposal，獨立排程）

走既有 `2026-06-04-12-rule-canon-patch-proposal.md` + `/autoload-evolution` 閉環，本報告不重複。

### Gate 與紀律
- 三 Phase 均**非破壞性**（無 DELETE/prod/key），無需不可逆 gate，但完成前各跑驗證展示輸出。
- 全程 `feature/coldstart-audit` 分支，commit 前 `git branch --show-current` 確認。

---

## 5.5 執行結果（2026-06-06 同 session 完成）

| Phase | 狀態 | 實測 |
|-------|------|------|
| **P1 schema-lint 批次化** | ✅ 完成 | session-init **520→170ms（−68%）**；輸出契約不變（3 種壞檔 + issue count 驗證一致）；healthcheck 116-0 |
| **P2 MEMORY 壓縮** | ✅ 完成 | **10,976→9,052B（−18%）**；刪早期已結清待辦節 + 壓 3 個長 session 摘要；grep 驗 4 待辦/Lesson G/H/D/commit ref 全保留 |
| **P3 auto-load headroom** | ⚠️ 誠實 no-op | auto-load **零連續空行/零 trailing whitespace/`---` 為語意分段** → **無純機械冗餘可回收**。274B 餘裕是「逼滿但乾淨」，列觀察。守 CLAUDE.md「不為塞 byte 反推湊」+ Lesson 2026-06-05-A「先質疑約束本身」 |

**P3 no-op 的正當性**：使用者選「純機械回收」，但實測發現該 auto-load 已是優化態。硬壓會損語意分段或規則措辭——這違反「外科刀」與「不湊 byte」紀律。**誠實回報「沒有可回收空間」優於製造假動作。** 真正的 headroom 回收須走內容變更（既有 canon-patch proposal，需逐條核准），不在「純機械」範圍。

實測差異說明：P1 報告 P2 預測「44ms / −89%」是 schema-lint 區段隔離值；實裝後 session-init **整體** 170ms（含 model-check/HMF/git log 等其餘必要區段），整體降幅 −68%，與預測一致方向。

---

## 6. 附錄 — 評估方法論的自我校正記錄

本評估本身命中兩個 The Loop 失敗模式，記錄供未來注入：

1. **subagent verdict 非證據（已防）**：researcher 判「skills 注入 workspace 無法控制」，與主對話親見的 SessionStart skill list 矛盾。advisor 攔下 → 主對話親 grep 推翻，補上 9.2KB 最大盲點。**若信 researcher verdict，這份「完整評估」會漏掉第三大項。**
2. **latency vs context 混淆（已防）**：初稿傾向把 schema-lint 416ms 講成「深度影響執行效率」。advisor 校正：那是**每 session 一次省半秒**，非 per-prompt；而 context 大宗多被 prompt cache 攤銷，是 cap 紀律問題非速度。**兩維度全程分離標註 [L]/[C]。**

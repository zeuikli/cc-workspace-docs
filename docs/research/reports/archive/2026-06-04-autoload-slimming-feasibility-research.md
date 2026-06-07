---
title: "Auto-load 精簡可行性研究報告"
date: 2026-06-04
baseline_bytes: 18955
branch: feature/autoload-slim-research
cap_bytes: 19000
headroom_bytes: 45
mode: 純研究 + 計劃書（零修改 auto-load）
sources: [2026-06-03-claude-code-cold-start-latency-deep-research.md, 2026-06-03-cc-workspace-coldstart-action-plan.md, 2026-06-03-context-window-management-deep-research.md, 2026-06-03-context-window-management-action-plan.md, 2026-06-03-prompt-caching-management-engineering.md, 2026-06-03-prompt-harness-action-plan.md, 2026-06-03-subagent-agent-team-deep-research.md, 2026-06-03-subagent-agent-team-execution-plan.md, 2026-06-04-action-plans-execution-report.md]
type: research
---

# Auto-load 精簡可行性研究報告

> **執行模式**：純研究 + 計劃書，**零修改 auto-load 檔**（使用者定奪）。APPLY 留待後續 session 核准。
> **方法**：量測 → 分批委派 2 researcher 萃取 8 報告 → advisor 校準 framing → 逐檔 byte 定位候選。

---

## 0. TL;DR — 誠實裁決（Fail-Loud 先行）

**精簡在機械上可行，但 8 份報告的證據共識一致將 auto-load 精簡評為「低優先 / 非首要槓桿」。**

- auto-load **不是**延遲瓶頸（cold-start 報告：真瓶頸是 hook 進程 spawn × 頻率；18,955 bytes cache 命中後僅 0.1× 成本）。
- 8 報告**無一**主張縮減現有 auto-load 內容；4 份明確標其為「P2 非重點 / 前作已最佳化至接近極限」。
- **但精簡仍有真實價值——只是價值不在延遲，在「餘裕」**：當前 18,955/19,000（餘 45，近滿）。精簡的真正決策意義是 **「下次 cap 上調的替代方案」**：core.md §Framework Integrity 記載 cap 剛由 18,000→19,000，並明文「下次上調須同等級實證計劃書背書」。精簡 = 不必再上調 cap 就能容納未來增補。

**結論**：可行；建議定位為**低優先、機會性執行**（回收 TYPE B/C/D justification metadata 餘裕），而非緊急縮減。本報告附可執行計劃書（逐項候選 + byte 估算 + falsifiable prediction）供後續 session 機械執行。

---

## 1. 基線量測（OBSERVE）

驗證指令：`wc -c CLAUDE.md .claude/rules/{core,context-management,output-discipline,subagent-strategy}.md | tail -1`

| 檔案 | bytes | 佔比 | 角色 |
|------|------:|-----:|------|
| `.claude/rules/core.md` | 8,978 | 47.4% | R1–R12 強制條文 + Git 流程 + 生產紅線 |
| `.claude/rules/subagent-strategy.md` | 3,855 | 20.3% | 委派 / fan-out / advisor |
| `CLAUDE.md` | 2,625 | 13.9% | 12-Rule Canon 表 + harness loop + 模式 |
| `.claude/rules/context-management.md` | 2,007 | 10.6% | token budget / compact / caching |
| `.claude/rules/output-discipline.md` | 1,490 | 7.9% | 輸出紀律 |
| **總計** | **18,955** | 100% | vs cap 19,000，餘 **45** |

**單位 canonical = byte**（core.md §Framework Integrity 已統一；measure.sh 有真實 byte cap 回歸檢查）。

**門檻三段**（core.md）：
- ≤13,000 理想基線
- 13,000–19,000 12-Rule Canon 完整性正當化區間（**現況 18,955 在此區間頂端**）
- \>19,000 觸發審視

---

## 2. 證據共識（8 報告橫斷萃取）

委派 2 個 researcher 並行萃取（context isolation，避免主 context 爆）。四維度共識：

| 維度 | 8 報告共識立場 | 來源 |
|------|---------------|------|
| **精簡優先序** | 低。auto-load 非延遲瓶頸；hook spawn 才是 | cold-start deep + action-plan（P2 標非重點）|
| **若要精簡的範圍** | 只壓 **TYPE B/C/D**（justification metadata / 日期戳 / rationale），**R1–R12 行為不動** | context action-plan + cold-start action-plan |
| **新知識放哪** | **on-demand ref**（`.claude/refs/`），非 auto-load。「高頻才進前綴」 | prompt-harness（最直接）+ subagent-execution（「零新增 auto-load rule」硬規則）|
| **cache 穩定性** | 前綴**穩定** ≠ 前綴**膨脹**。獨立 commit 精簡前綴不違 cache 原則；只是**禁 mid-session 改** | prompt-caching engineering + context deep |

### 2.1 唯一的「反精簡」論點及其反駁

**論點**：prompt caching 前綴穩定性需求——改前綴 = 100% cache miss（`2601.06007` 實測穩定前綴省 41–80% 成本、TTFT 降 13–31%）。

**反駁**：這是「**不隨便改**」（禁 mid-session 切換）的約束，**不是「不能縮」**。在獨立 commit、session 結束後精簡，下個 session 起以新前綴穩定快取——完全符合 static-first 原則。core.md §context-management 本就規定「Mid-session 禁止改 CLAUDE.md → session 結束後執行」。

### 2.2 specification 品質的下限約束

subagent deep research 引 MAST：**specification 品質**是 multi-agent 最大失敗源（κ=0.88）。隱含：**過度壓縮會損害規則的可機械驗證性（R4/R12）**。

→ 這設定了精簡的**下限**：只能壓「為何這樣做」（rationale / 歷史 metadata），**不能壓「做什麼 / 如何驗證」**（行為條文 + 驗證指令）。

---

## 3. 可行性分析（IDENTIFY）

### 3.1 TYPE 分類（依 harness-meta TYPE A/B/C/D 框架）

| TYPE | 定義 | 可壓性 | 範例 |
|------|------|--------|------|
| **A** | 行為條文（做什麼）| ❌ 不可壓 | R1–R12 強制條文、驗證指令 |
| **B** | 低頻但必要的具體規則 | ⚠️ 謹慎 | 不可逆動作清單、量化界線 |
| **C** | 重複 / 可推導的說明 | ✅ 可壓 | 跨檔重複的 byte 門檻說明 |
| **D** | 一次性歷史 metadata | ✅ 可壓（移 on-demand）| cap 上調 rationale、worktree 根因記述 |

### 3.2 候選盤點（core.md 為主，佔 47%）

逐 `grep -n` 定位的高 byte justification metadata：

| # | 位置 | 性質 | TYPE | 估算可回收 | 移往 |
|---|------|------|------|----------:|------|
| C1 | core.md L78 cap 上調 rationale（18,000→19,000 為何）| 一次性決策史 | D | ~240 B | MEMORY + execution report 已記載 |
| C2 | core.md L99 worktree「隔離只在…生效」根因段 | 根因記述 | C/D | ~180 B | MEMORY Lesson 2026-06-04-B 已全記 |
| C3 | CLAUDE.md L4 + core.md L77 byte 門檻**重複**說明 | 跨檔重複 | C | ~120 B | 留 core.md 一處，CLAUDE.md 引用 |
| C4 | core.md §Framework Integrity 三段門檻冗長 rationale | 說明膨脹 | C | ~100 B | 精簡措辭，保留數字門檻 |
| C5 | subagent-strategy 控制語義表（interrupt/steer/gate）| 低頻參照 | B | ~250 B | refs（MEMORY 待辦已標，但保守保留）|

**保守可回收估算：~640–760 bytes**（不含 C5，C5 上次已選擇保守保留）。
**積極（含 C5 移 refs）：~890–1,010 bytes**。

### 3.3 與既有待辦/DEFER 的重疊（避免重複提案）

advisor 提醒查重。確認：

- **MEMORY 待辦**已明列「**壓 TYPE B/C/D 取回餘裕**」+「subagent-strategy →See agent-team-patterns（byte 取回餘裕後補）」。→ **本計劃是履行該既有待辦的具體化**，非新主題。
- subagent-execution-plan 的硬規則「零新增 auto-load rule」與本精簡**方向一致**（都在保護 byte 預算）。
- 上個 session（execution report）的 3 個 DEFER（SA-1.1/1.2/3.1）**不涉**本候選，無重疊。

---

## 4. 風險評估

| 風險 | 等級 | 緩解 |
|------|------|------|
| 壓掉 specification 品質 → R4/R12 可驗證性受損 | 高 | 只壓 TYPE C/D（rationale/史料），不碰 TYPE A 行為條文 + 驗證指令 |
| 破 cache 前綴 | 低 | 獨立 commit、session 結束後改；禁 mid-session |
| 移 on-demand 後變孤兒（不可達）| 中 | MEMORY Lesson 2026-06-04-E 教訓：移 refs 必在 refs/README 登錄入口 |
| 回收 byte 後被「湊新規則」回填 | 中 | core.md §Framework Integrity 已防（「不接受反推湊 byte」）；回收餘裕應留白 |
| 精簡誤判為「高優先」延誤真瓶頸（hook spawn）| 中 | 本報告 TL;DR 已標低優先；hook 優化是獨立 gated session |

---

## 5. 可行性裁決（PROPOSE）

| 問題 | 裁決 |
|------|------|
| 機械上可精簡？ | ✅ 可。~640–1,010 bytes 可回收，不碰 R1–R12 行為 |
| 證據支持立即執行？ | ⚠️ 低優先。8 報告共識：非首要槓桿 |
| 有真實價值？ | ✅ 有。價值 = **cap 上調的替代方案**（餘 45 近滿）|
| 建議 | **機會性執行**：下次需要 auto-load 餘裕時（而非為精簡而精簡），按附帶計劃書回收 C1–C4（保守 ~640 B），把 18,955 降至 ~18,300，餘裕從 45 → ~700 |

**不建議**：① 為達 ≤13,000 激進縮減（會傷 canon 完整性 + specification 品質，違 8 報告共識）；② 把精簡當延遲優化（瓶頸是 hook）。

---

## 6. 後續（計劃書 handoff）

可執行計劃書（`2026-06-04-autoload-slimming-execution-plan.md`，逐項候選 + byte 估算 + falsifiable prediction + 驗證指令）已執行完並於 2026-06-05 移除；執行結果見下 §7 與 MEMORY「auto-load 精簡 APPLY」session。

**驗證指令（基線）**：
```bash
wc -c CLAUDE.md .claude/rules/{core,context-management,output-discipline,subagent-strategy}.md | tail -1
# 預期當前：18955 total
```

---

## 7. 後續更新（2026-06-05 post-#446 5 源重掃 delta）

> C1–C4 已 APPLY（執行報告 `2026-06-04-autoload-slimming-apply-execution-report.md` 已於 2026-06-05 移除，結果留存 MEMORY；18,955→**18,455**，餘裕 45→**545**）。本次重掃 papers/best-practices/claude-blog/tweets 找 #446 後新槓桿，1 researcher delta 萃取 + 主對話逐項親驗。**裁決：不動 auto-load 內容**（兩軸均無 content-layer 行動）：

- **優化軸（省 byte）= 已關閉**。#446 C1–C4 已回收 500 B；新證據 D5（`papers/2026-01-29-when-better-prompts-hurt-2601-22025.md`，一手 MEDIUM）反向背書：通用「improved」規則換掉任務特定規則 → 提取率 100%→90%、RAG 合規 93.3%→80%。**支持保留現有具體規則 + 失敗案例脈絡，不再壓**。
- **強化軸（同 byte 提遵循率）= 唯一槓桿是 D4，且是 workflow 非 content edit**。D4（`tweets/2026-06-02-@trq212-367865.md`，Anthropic 官方一手）：per-rule verifier workflow（一規則一 verifier + skeptic persona 避假陽性）+ 反向 mine sessions→cluster→distill。零 auto-load byte，延伸現有 TESTBANK-50/behavioral-scorer。**可排程建置，非 auto-load 改動**。
- **D1 強調詞密度審查 = 已審，保留不動**。親驗：auto-load 共 6 個 IMPORTANT/YOU MUST（core×5 + subagent×1），官方建議「1–2 genuinely critical」（report L264）。但 5/6 確為 critical（生產安全紅線×2 / 繁中鐵律 / Fail-loud 驗證 / injection 防禦）；唯一軟案例 core L98 Git YOU MUST 因 hook 只 gate/warn 不 enforce「git add 非 -A / retry-push」→ 文字非冗餘。**密度由 security-heavy profile 正當化，非 bloat**。
- **D2 HTML comment「零成本」= 推翻**。researcher 標「零 token」但本 workspace canonical 單位是 `wc -c` byte——實測 `wc -c` **計入** comment 全文 byte → comment 維護 prose 會吃 545 餘裕，與 byte-cap 紀律**相衝**，非零成本。
- **D3 SkillOpt**（`tweets/2026-06-01-@hooeem-791154.md`，二手 MEDIUM）：run→score→propose→gate→accept 文字空間優化器，可作未來 `autoload-evolution` 工具層，**非本次行動**。

**一句話**：auto-load 已在 byte（#446）與 security profile（本次）兩面接近最佳；唯一真實強化是「驗證層 workflow（D4）」而非「內容層改動」。優化軸關閉，D5 為其煞車。

---

## 8. 2026-06-05 增量併入（gap-vote 三技能共識，2 真 gap）

> **方法**：gap-vote（三角色並行）對近期 corpus 找未併入 gap，2/3 共識 + **主對話親自 grep 重驗 verbatim**。本報告分得「精簡下限 / 模型升級重評」相關 gap。**不改本報告裁決**（優化軸關閉、機會性執行 C1–C4 已 APPLY），僅補強既有「精簡下限」與「cap 上調替代」論點的論文接地。

### 補充 8.1：精簡下限獲第三方量化——35:1 壓縮失 nuanced constraints（beyond-context-window，arXiv:2603.04814）

**對 §2.2「specification 品質下限約束」的補完**：§2.2 引 MAST κ=0.88 主張「過度壓縮損害可機械驗證性」，但偏定性。beyond-context-window 給出壓縮損失的具體量化：

**接地審計**：
- `35:1` 失 nuance ← "The 35:1 compression ratio preserves broad topics but loses specific facts and nuanced constraints — exactly the information that matters for accurate task completion."（2026-03-05-beyond-context-window-memory-vs-longcontext-2603-04814.md L91）
- 壓縮 vs 全文 accuracy 差 ← "Long-context … outperforms memory-based compression by 33.4–35.2 percentage points in accuracy."（同檔 L20）

**啟示**：直接背書本報告「只壓 TYPE C/D rationale/史料，不碰 TYPE A 行為條文 + 驗證指令」的下限設計——TYPE A 正是「specific facts / nuanced constraints」（安全紅線、驗證指令），壓掉會傷 33.4–35.2pp accuracy。⚠️ 此數字是 multi-turn 對話壓縮的實測，非 auto-load 精簡的直接量測；**借其機制（壓縮失 nuance），非直接套幅度**。

### 補充 8.2：精簡後若隨模型升級沿用須重評——Model Drifting + tokenizer（PromptBridge 2512.01420 / Opus 4.7 card）

**對「精簡是 cap 上調替代方案」論點的時間維度補充**：本報告 §5 主張精簡回收餘裕以避免 cap 上調。但兩個跨模型因素使「精簡後的最佳配置」非永久：

**接地審計**：
- Model Drifting ← "prompts are highly model-sensitive: reusing a prompt engineered for one model on another often yields substantially worse performance … We term this phenomenon *Model Drifting*."（2025-12-01-promptbridge-cross-model-prompt-transfer-2512-01420.md L22）
- tokenizer ← "Same input produces **1.0–1.35× more tokens** vs Opus 4.6 (content-dependent)"（2026-04-16-claude-opus-4-7-system-card.md L86）

**啟示**：① byte cap（`wc -c`）對 tokenizer 變更免疫——再次印證 canonical 單位採 byte 正確（精簡的 byte 回收不因換模型失效）；② 但「哪些規則該精簡 / 該保留」是 prompt 層判斷，**模型升級後須重評**（Model Drifting）。→ 本報告「機會性執行」定位仍成立，但應加註：**下次模型升級時，C1–C4 已 APPLY 的精簡 + 未來精簡候選須隨之重評**，非一次定終身。

*增量併入日期：2026-06-05 | gap-vote 2 真 gap（35:1-nuance 精簡下限 / Model-Drifting+tokenizer 模型重評）| 全數主對話親自 grep 接地 | 不改本報告裁決，僅補論文接地*

---
date: 2026-07-26
source: DAILY-RESEARCH/2026-07-26.md
topics: [claude-opus-5-launch-half-price-fable5-parity, harness-handbook-dynamic-workflows-omarsar0, claude-security-plugin-public-beta, airbus-sovereign-cloud-extraterritorial-tender, anthropic-sk-hynix-custom-semiconductor-memory-supply]
type: session-report
---

# Session Report 2026-07-26 — Daily Research

## 上次 P0 回填

回填對象：2026-07-25 report 之 P1 backlog（P1-1~P1-3、P1-5~P1-27，27 項）+ P0-2（合規性延後）。本日逐項重跑同一驗證命令（腳本化執行，非沿用昨日文字結論）：

| 項目 | 狀態 |
|------|------|
| P1-1（DAILY-TOPICS 技術路徑交叉驗證流程改進）| ⏳ 仍待辦——第 16 天，07-15 已移交使用者裁決 |
| P1-2（security-hygiene.md 補全 China v2.1.91–v2.1.196）| ⏳ 仍待辦——第 15 天 |
| P1-3（the-loop-best-solution.md 補 confidently garbage 案例）| ⏳ 仍待辦——第 17 天 |
| P1-5（subagent-strategy.md 套用 Planner/Generator/Evaluator 官方案例）| ⏳ 仍待辦——第 13 天 |
| P1-6（.claude/refs/ 補 Pattern A/B/C 權限升降級路徑）| ⏳ 仍待辦——第 13 天 |
| P1-7（model-profiles.md 補 Fable 5 存取狀態查詢指針）| ⏳ 仍待辦——第 12 天，證據累積 3 筆 |
| P1-8（spec-implement skill 補 review-against-spec 子步驟）| ⏳ 仍待辦——第 12 天 |
| P1-9（delegation-protocol.md 補 AWS DMS 三層架構案例）| ⏳ 仍待辦——第 11 天 |
| P1-10（core.md 補 Common Lisp eval-as-tool sandbox 案例）| ⏳ 仍待辦——第 11 天 |
| P1-11（core.md unverified_success 補 TDS 100+ agent 反例）| ⏳ 仍待辦——第 10 天 |
| P1-12（delegation-protocol.md 補 Uber 四層 + Nexus SDV 三層）| ⏳ 仍待辦——第 10 天 |
| P1-13（企業採用率新聞證據分級範本）| ⏳ 仍待辦——第 10 天 |
| P1-14（core.md 四大缺陷補 Ronacher/依賴陷阱反例）| ⏳ 仍待辦——第 8 天 |
| P1-15（finops/security-hygiene 補 action-time vs invoice-time alert）| ⏳ 仍待辦——第 7 天 |
| P1-16（core.md/security-hygiene.md 補 Full Access $HOME 刪除事故）| ⏳ 仍待辦——第 6 天，證據已齊備 |
| P1-17（harness-meta/refs 補 MemoHarness + Self-Evolving Harnesses 交叉引用）| ⏳ 仍待辦——第 6 天 |
| P1-18（core.md 補 AIDE2 三層防護 + 2607.07663 評估器層級）| ⏳ 仍待辦——第 5 天 |
| P1-19（delegation-protocol.md 補 Boris Cherny 五個並行 plan-mode）| ⏳ 仍待辦——第 5 天 |
| P1-20（agent-harness/RESEARCH.md 補 Maka vs Kimi Code harness 對照）| ⏳ 仍待辦——第 4 天 |
| P1-21（security-hygiene.md/core.md 補 VentureBeat 54% 企業 agent 安全調查）| ⏳ 仍待辦——第 4 天 |
| P1-22（model-profiles.md 補 Nadella/Fable 蒸餾防護，併入 P1-7）| ⏳ 仍待辦——第 4 天 |
| P1-23（subagent-strategy.md 補 Cat & Thariq 逐字稿 + 65%/80%）| ⏳ 仍待辦——第 3 天 |
| P1-24（subagent-strategy.md 補 Kubeflow+Cilium 相關性錯誤案例）| ⏳ 仍待辦——第 3 天 |
| P1-25（security-hygiene.md 補 iOS Simulator screenshot 保留政策）| ⏳ 仍待辦——第 3 天 |
| **P1-26（security-hygiene.md 補 containment 架構三案例 + 三組數字）**| **⏳ 仍待辦——第 2 天（原驗證命令回報 ✅ 為假陽性，見下方「弱 oracle 更正」）** |
| P1-27（security-hygiene.md 補「授權使用者本人下達破壞性指令」情境）| ⏳ 仍待辦——第 2 天 |
| P0-2（explore-subagent-billing-gotcha，合規性延後）| ⏳ 不變——EVOLUTION-QUEUE 該條目仍為 `status: deferred`（2026-07-11 審核：目標為 auto-load 規則，同 gpt56 案 byte/cycle 雙限制，留待下一 /autoload-evolution cycle） |

### 弱 oracle 更正（本日新發現，適用 `core.md` §TEST「Oracle 資格先於 loop」）

P1-26 的原驗證命令為：

```bash
grep -qE 'contain-claude|93%.*核准率|approval.fatigue|allowlist proxy.*失敗' .claude/rules/security-hygiene.md
```

本日回填時該命令回報 ✅，機械複核實際命中行為：

```
73:> 官方 how-we-contain-claude（2026-05）：「環境層優先於模型層——模型層防禦永遠無法 100%」。
```

該行由 07-24 commit（92608eb）加入，**早於 P1-26 於 07-25 提出**，命中的是 alternative `contain-claude` 子字串，與 P1-26 實質內容無關。實質內容檢查：

```bash
grep -cE "93%|84%|25 次|24 次" .claude/rules/security-hygiene.md   # → 0
```

三組量化數字全數不存在 → P1-26 **實為 ⏳ 仍待辦**，本表已更正。此為 backlog 驗證命令的 false-positive，與 INDEX.md「缺口與待修」既有記錄的兩個 grep 誤判（06-20 false-negative、06-25 false-positive）屬同一類缺陷。

**P1-26 收緊後驗證命令（本日起取代原命令）**：

```bash
grep -qE '93%.*核准率|approval fatigue|84%.*提示|紅隊.*釣魚' .claude/rules/security-hygiene.md
# 本日實測輸出：NOT-FOUND-仍待辦
```

**回填說明**：27 項 P1 + 1 項合規延後 P0-2 全數為 ⏳，backlog 落地率連續第十次為 0。**07-23 官方選題 4 題缺口延續至第 4 天**（本日 DAILY-TOPICS/2026-07-26.md 正常存在，依 SSoT 執行當日選題，此缺口不在本次範圍內自行回補）。本日新增 P0-3（本報告內即完成）、P1-28~P1-30，backlog 增至 30 項 P1 候選。

---

## 執行概要

- **研究主題**：5 個（DAILY-TOPICS/2026-07-26.md 全覆蓋：Anthropic消息 1、深度應用 2、職業領域 1、供應鏈/地緣 1）
- **搜尋查詢**：5 次並行 WebSearch
- **頁面 Fetch**：6 次深度抓取（anthropic.com、arxiv.org/abs、arxiv.org/html、claude.com、infoq.com、fortune.com 全數成功）
- **arxiv 命中**：1（`2607.13285` Harness Handbook）→ Step 2b 觸發：去重 grep 未命中 → 新建 `research/papers/2026-07-26-harness-handbook-2607-13285.md` + 同名 PDF（1.5 MB，`file` 驗證為 PDF 1.7，非 HTML 錯誤頁）
- **信號強度／evidence-tier**：全數沿用 Routine A 機械推導值（5/2/1/1/1，全 hard），本 Routine 未做 LLM 自評

## 本日研究成果摘要

### 最高價值發現（Top 3）

**1. Harness Handbook 論文提供本 workspace progressive disclosure 架構迄今最強的第三方量化佐證（影響等級：High，可直接轉為輕量實作）**

planning win rate +10.0 pt（Codex）／+18.9 pt（Terminus-2），同時 planner token −12.7%／−8.6%——品質與 token 同向改善，反駁「省 token 必犧牲品質」的直覺。增益分佈最關鍵：Search-Hostile 類請求 +20.0~33.3 pt 為所有類別最高，精準對應本 workspace「語義存在但無穩定關鍵詞可 grep」的規則導航問題。可遷移物明確：`.claude/agents/INDEX.md` 與 `skills/RESOLVER.md` 目前是 L3 式「名稱→用途」清單，缺 L1/L2 行為層。

**2. Claude Opus 5 的 mid-conversation tool changes（beta）動搖 `context-management.md` 快取五禁令③的機制前提（影響等級：Medium-High，需標注而非解除）**

該禁令「不 mid-session 增刪 tool」成立的前提是工具異動必然打斷穩定前綴；官方 beta 功能宣稱可變更工具而不使 prompt cache 失效。本 workspace 未實測，且功能為 beta 可能變更或撤回 → 正確處置是標注適用條件與觀察狀態（`core.md`「規則 = decaying cache」），不是解除禁令。

**3. 本日回填流程自身查出一個弱 oracle：P1-26 驗證命令 false-positive（影響等級：Medium，方法論缺陷，已即時修正）**

原命令的 `contain-claude` alternative 命中 07-24 既有引用行（早於 P1-26 提出），造成「已落實」假象；實質三組數字命中數為 0。此為連續十日 backlog 回填流程中首次查出的驗證命令缺陷，若未複核將把一個仍待辦項目誤標為完成。已於本報告更正狀態並替換為收緊後命令。

---

## 可實作 / 可測試內容

### P0 — 立即可執行（今日或明日，< 2 小時）

**P0-3（本報告內已完成）**：更正 P1-26 的驗證命令（原命令 false-positive）並回寫本日回填表。目標檔為 `research/reports/`（非 `.claude/`），屬本 Routine 產出範圍，已直接執行。
- 驗證：`grep -q '弱 oracle 更正' research/reports/2026-07-26-daily-research-session.md && grep -q 'NOT-FOUND-仍待辦' research/reports/2026-07-26-daily-research-session.md && echo OK`
- 本日實測：見 TEST 區段輸出

其餘本日發現的目標檔均位於 `.claude/` 目錄，依既有紀律僅建立提案、待人工審核，**不列 P0**。延續 P0-2（合規性延後，狀態不變）。

### P1 — 本月優先（需輕量設計，2-8 小時）

**P1-28（新增）**：為 `.claude/agents/INDEX.md` + `.claude/skills/RESOLVER.md` 補「行為層」索引（Harness Handbook L1/L2 的 markdown 類比物）——以「harness 做什麼 → 該行為住在哪個檔案」為組織軸，補在現行「名稱→用途」清單之上。論文佐證：Search-Hostile 類請求增益最大（+20.0~33.3 pt），而本 workspace 最典型的 search-hostile 問題正是「這條行為該改哪個檔」。
- 驗證：`grep -qE '行為層|behavior.*→.*檔案|BGPD|Harness Handbook' .claude/agents/INDEX.md .claude/skills/RESOLVER.md && echo OK`

**P1-29（新增）**：`.claude/rules/context-management.md` 快取五禁令③補 beta 例外標注——Opus 5 的 mid-conversation tool changes（beta）宣稱變更工具不使 prompt cache 失效。**必須明寫「beta 觀察中、本 workspace 未實測，非解除禁令」**，並列入實測待辦。
- 驗證：`grep -qE 'mid-conversation tool|工具異動.*beta|beta.*觀察中.*禁令' .claude/rules/context-management.md && echo OK`

**P1-30（新增）**：`.claude/rules/security-hygiene.md` 補原生 Claude Security plugin 與既有 `security-reviewer`／`security-auditor` agent 的分工判準（DAILY-TOPICS 演化候選 1 的具體化）。本日新增可寫入的判準：原生 plugin 涵蓋「程式碼內 + commit 時 + 高嚴重度（injection/auth bypass/memory corruption）」；既有 agent 保留「非程式碼資產（Terraform／K8s manifest）、STRIDE 深度建模、career-wiki 脈絡化建議」。
- 驗證：`grep -qE 'Security plugin|原生.*掃描.*第一層|plugin.*vs.*security-auditor' .claude/rules/security-hygiene.md && echo OK`

**P1-1~P1-3、P1-5~P1-27（延續，27 項，見上方回填表逐項天數；P1-26 狀態已更正）**

### P2 — 觀察中（需更多信號再決定）

**P2-1~P2-21（延續自 07-09~07-25，本日無新信號變更判斷）**

**P2-22（新增）**：Claude Opus 5 的 ARC-AGI-3 30.2%（Opus 4.8 為 1.5%，20 倍級距）目前僅有官方自 published benchmark 與二手轉述，無獨立第三方重現。觀察條件：ARC Prize 官方或獨立評測方是否釋出驗證結果；若出現評測集污染或方法變更的討論，需回頭調整本日對 Opus 5 能力的記錄語氣。

**P2-23（新增）**：Claude Security plugin 的可用範圍與定價／消耗模型。官方產品頁述及 Claude Enterprise 公測 + admin console 啟用，其他來源述「所有 Claude Code 使用者」，本日無法裁決。觀察條件：Claude Code 官方 changelog 或 pricing 頁釋出明確資格說明。

---

## GAP 狀態更新

| GAP | 研究前狀態 | 研究後狀態 | 行動 |
|-----|-----------|-----------|------|
| claude-opus-5-launch-half-price-fable5-parity | gap (0篇) | **filled** — 定價/五項 benchmark/三項新功能/弱項揭露完整記錄 | 新增 P1-29（快取禁令③ beta 標注）、P2-22（ARC-AGI-3 獨立重現觀察） |
| harness-handbook-dynamic-workflows-omarsar0 | gap (0篇) | **filled** — 論文已歸檔 `research/papers/2026-07-26-harness-handbook-2607-13285.md` + PDF，含完整量化表 | 新增 P1-28（行為層索引），為本日最高價值可實作項 |
| claude-security-plugin-public-beta | gap (0篇) | **filled**（架構/六階段前兩階段/對抗驗證）／**partial**（資格與定價未定，見 P2-23） | 新增 P1-30（agent 分工判準） |
| airbus-sovereign-cloud-extraterritorial-tender | gap (0篇) | **partial** — 三維度評分與「可驗證控制」原則已記錄；規模數字來源衝突未裁決 | 依 DAILY-TOPICS 標注交 **Routine F** 深化，career-wiki 本日不寫入 |
| anthropic-sk-hynix-custom-semiconductor-memory-supply | gap (0篇) | **partial** — 一手發言（人/時/地）確認；供料品項/時程/金額未揭露 | 資訊性記錄，不觸發規則變更 |

---

## 下一次循環優先事項

1. **P1 backlog（現 30 項候選：P1-1~P1-3、P1-5~P1-30）落地率連續第十次為 0**：連續第十份 report 建議排一次 `/autoload-evolution` 或治理批次 cycle 集中處理。本日建議優先納入下批的三項：**P1-28**（Harness Handbook 為本日唯一附完整量化實驗的可遷移設計，且與既有 progressive disclosure 架構同源、改動半徑小）、**P1-26**（狀態已更正為待辦，證據品質仍為 backlog 最強）、**P1-16**（Full Access $HOME 事故證據已齊備第 6 天）。
2. **回填驗證命令需一次性稽核**：本日查出 P1-26 命令 false-positive，加上 INDEX.md 已記錄的 06-20 false-negative 與 06-25 false-positive，三例同類缺陷顯示 backlog 驗證命令本身缺乏 oracle 資格審查。建議下次批次處理前，先對 30 條 P1 驗證命令做一次「命中行是否早於該項提出日」的機械稽核——否則落地率統計本身不可信。
3. **07-23 官方選題 4 題缺口累積至第 4 天**：`claude-cowork-skill-from-screen-recording`、`amd-anthropic-compute-deal-2gw`、`aws-loom-cncf-agentic-platform-governance`、`sk-hynix-intel-ohio-fab-acquisition-talks`。其中 `amd-anthropic-compute-deal-2gw` 與本日 Topic 5（SK Hynix 供料）屬同一垂直整合脈絡，若補跑可合併為一次供應鏈主題深化。仍待人工決定。

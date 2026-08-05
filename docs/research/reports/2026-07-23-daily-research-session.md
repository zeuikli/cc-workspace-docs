---
date: 2026-07-23
source: DAILY-RESEARCH/2026-07-23.md
topics: [harness-locality-benchmark-maka-vs-kcode-kimi-k3, grok-cli-local-file-exfiltration-incident, agent-security-gap-54pct-enterprise-credential-sharing, nadella-fable-editorially-controlled-restrictions]
type: session-report
---

# Session Report 2026-07-23 — Daily Research

## 上次 P0 回填

`research/DAILY-TOPICS/2026-07-22.md` 不存在（Routine A 連續 2 天未執行，F15 hook 全滅事故空窗期），故本節回填對象為最近一份存在的 report——2026-07-21 report 之「下一次循環優先事項」+ 19 項 P1 backlog（P1-1~P1-3、P1-5~P1-19）+ P0-2，本日逐項重跑同一驗證命令（非沿用昨日文字結論）：

| 項目 | 驗證命令 | 狀態 |
|------|----------|------|
| P1-1（DAILY-TOPICS 技術路徑交叉驗證流程改進）| `grep -qE "技術路徑交叉驗證\|technical.*cross.*valid" research/ROUTINE-A*.md` | ⏳ 仍待辦——第 13 天，07-15 已移交使用者裁決 |
| P1-2（security-hygiene.md 補全 China v2.1.91–v2.1.196）| `grep -qE "2\.1\.91.*2\.1\.196\|2\.1\.196" .claude/rules/security-hygiene.md` | ⏳ 仍待辦——第 12 天 |
| P1-3（the-loop-best-solution.md 補 confidently garbage 案例）| `grep -qE "confidently.*garbage\|弱驗證器" .claude/refs/the-loop-best-solution.md` | ⏳ 仍待辦——第 14 天 |
| P1-5（subagent-strategy.md 套用 Planner/Generator/Evaluator 官方案例）| `grep -qE 'Planner.*Generator.*Evaluator\|Generator.*Evaluator.*Planner\|\$9.*\$200\|retro game maker' .claude/rules/subagent-strategy.md` | ⏳ 仍待辦——第 10 天 |
| P1-6（.claude/refs/ 補 Pattern A/B/C 權限升降級路徑）| `grep -rqE 'Pattern A.*Pattern B.*Pattern C\|approval-first.*curated-allowlist\|curated-allowlist.*sandboxed-full-auto' .claude/refs/*.md` | ⏳ 仍待辦——第 10 天 |
| P1-7（model-profiles.md 補 Fable 5 存取狀態查詢指針）| `grep -qE "Fable.?5.*(存取狀態\|access.status\|usage.credits)" .claude/refs/model-profiles.md` | ⏳ 仍待辦——第 9 天，本日 Topic 4（Nadella/Fable 蒸餾防護細節）為第 2 筆可納入證據，優先度應再升 |
| P1-8（spec-implement skill 補 review-against-spec 子步驟）| `grep -qE "review.against.spec\|spec.*vs.*diff\|獨立.*比對.*spec" .claude/skills/spec-implement/SKILL.md` | ⏳ 仍待辦——第 9 天 |
| P1-9（delegation-protocol.md 補 AWS DMS 三層架構案例）| `grep -qE 'DMS.*Schema.Conversion\|schema.conversion.*agentic\|規則引擎.*agentic.*generative' .claude/refs/delegation-protocol.md` | ⏳ 仍待辦——第 8 天 |
| P1-10（core.md「不可逆操作永遠等確認」補 Common Lisp eval-as-tool sandbox 案例）| `grep -qE 'eval.as.tool\|sandbox.only.*lisp\|lisp.*sandbox' .claude/rules/core.md` | ⏳ 仍待辦——第 8 天 |
| P1-11（core.md unverified_success 補 TDS 100+ agent 反例）| `grep -qE 'orchestrate.*100.*agent\|100.*agent.*headless\|worker.*自證' .claude/rules/core.md` | ⏳ 仍待辦——第 7 天 |
| P1-12（delegation-protocol.md 補 Uber 四層 + Nexus SDV 三層架構案例）| `grep -qE 'Uber.*四層\|Nexus.*SDV.*三層\|context.layer.*agent.*platform' .claude/refs/delegation-protocol.md` | ⏳ 仍待辦——第 7 天 |
| P1-13（企業採用率新聞證據分級範本）| `grep -qE 'CTO.*一手.*獨立查證\|來源分類表.*採用率\|企業採用率.*證據分級' .claude/refs/*.md` | ⏳ 仍待辦——第 7 天 |
| P1-14（core.md 四大缺陷補 Ronacher/官方 loop 依賴陷阱反例）| `grep -qE 'Ronacher\|overly.defensive\|dependency trap\|依賴陷阱' .claude/rules/core.md` | ⏳ 仍待辦——第 5 天 |
| P1-15（finops/security-hygiene 補 action-time vs invoice-time alert 原則）| `grep -qE 'action.time.*invoice.time\|CloudTrail.*InvokeModel.*告警\|14,000\|6,531' .claude/skills/finops/SKILL.md .claude/rules/security-hygiene.md` | ⏳ 仍待辦——第 4 天 |
| P1-16（core.md/security-hygiene.md 補 Full Access mode $HOME 刪除事故）| `grep -qE 'Full Access.*sandbox.*審核\|danger-full-access\|\$HOME.*遞迴刪除\|hook.*攔截.*rm' .claude/rules/security-hygiene.md .claude/rules/core.md` | ⏳ 仍待辦——第 3 天 |
| P1-17（harness-meta/refs 補 MemoHarness + Self-Evolving Harnesses 交叉引用）| `grep -qE '2607\.14159.*2607\.13683\|2607\.13683.*2607\.14159\|MemoHarness.*Self-Evolving.*Harness' .claude/skills/harness-meta/SKILL.md .claude/refs/*.md` | ⏳ 仍待辦——第 3 天 |
| P1-18（core.md 補 AIDE2 三層防護 + 2607.07663 評估器層級案例）| `grep -qE 'AIDE2\|reward.hacking.*三層\|verification.hierarchy\|evaluator.*hierarchy' .claude/rules/core.md` | ⏳ 仍待辦——第 2 天 |
| P1-19（delegation-protocol.md 補 Boris Cherny 五個並行 plan-mode 案例）| `grep -qE 'Boris Cherny\|五個並行.*plan.mode\|plan.mode.*one-shot' .claude/refs/delegation-protocol.md` | ⏳ 仍待辦——第 2 天 |
| P0-2（explore-subagent-billing-gotcha，合規性延後）| 直接讀取 `research/EVOLUTION-QUEUE.md` 該條目 `status:` 欄位 | ⏳ 合規性延後不變——仍為 `status: deferred` |

**回填說明**：19 項 P1 + 1 項合規延後 P0-2 全數延續 ⏳（本日重跑逐項驗證命令，非沿用昨日文字，第七次印證落地率連續 0 的治理層級問題）。**額外發現**：`research/DAILY-TOPICS/2026-07-22.md` 與本日 `2026-07-23.md` 皆不存在，Routine A 於 F15 hook 全滅事故（修復於 f1f7a69）期間連續 2 天未產出選題文件，本 Routine 依 SSoT fallback 條款自行完成選題（見 DAILY-RESEARCH 執行摘要 + Unknowns）。本日新增 P1-20、P1-21、P1-22、P2-17、P2-18（見下方），backlog 增至 22 項 P1 候選。

---

## 執行概要

- **研究主題**：4 個（DAILY-TOPICS 文件缺失，依 SSoT fallback 自今日 32 份 newsletter digest 自選，方法論見 DAILY-RESEARCH 執行摘要）
- **搜尋查詢**：2 次 WebSearch（Grok CLI 事故細節、Nadella/Fable 引語確認，因原始連結分別為付費牆/403）
- **頁面 Fetch**：5 次深度抓取（wiselychen.com、devops.com、finance.biggo.com 成功；pragmaticengineer.com 付費牆受限、cnbc.com 403，皆以 WebSearch 補足關鍵引語與數字）
- **arxiv 命中**：0（Topic 1 引用 arxiv 2606.30616 作為訓練端旁證，但該 URL 非本日 Step 2 WebFetch 對象，未觸發 Step 2b 自動歸檔流程）

## 本日研究成果摘要

### 最高價值發現（Top 3）

**1. Harness 對照首見同模型同任務直接數字證據（影響等級：High，方法論意義最高）**

Maka 團隊對同一顆 Kimi K3、同一套 Terminal-Bench 2.1，官方 harness 59.6% vs 開源第三方 harness 69.7%（困難題子集差 20pp）——這是本 workspace 長期主張「harness 非包裝、是能力的一部分」首次獲得同模型同任務的直接對照數字（雖為自報、未經第三方復現），且與同批新聞的 Grok CLI 資料外洩事故形成「效能證據 + 安全證據」雙重印證。

**2. Grok CLI 資料外洩事故完整時間線還原（影響等級：Critical，直接涉及 agent 工具信任邊界）**

實測任務僅需 ~192KB 卻上傳 5.1GB（27,800 倍超額），隱私開關對此行為無效，xAI 悄悄修復未發公告——完整還原了本 workspace 反覆強調「第三方 agent 工具本身即攻擊面」的具體實錘案例，且與 Topic 3 的企業調查數字形成量化 + 個案的互補證據。

**3. 企業 agent 安全量化調查填補「治理落後於自主權擴張」的統計證據空白（影響等級：High）**

VentureBeat 107 家企業調查顯示 54% 已有 agent 安全事件、69% 存在憑證共用、僅 30% 做隔離，且憑證共用組織事故率（63.5%）顯著高於全專屬身份組織（40.9%）——為本 workspace 一貫主張的「per-agent 專屬身份 + 沙箱隔離」設計提供首個具規模的量化外部佐證。

---

## 可實作 / 可測試內容

### P0 — 立即可執行（今日或明日，< 2 小時）

本日四題均為資訊性發現，無 workspace 缺陷修復需求，**無新增 P0**。延續 P0-2（合規性延後，狀態不變，見上方回填表）。

### P1 — 本月優先（需輕量設計，2-8 小時）

**P1-20（新增）**：`research/agent-harness/RESEARCH.md`（或等效 harness 研究索引）補 Maka vs Kimi Code Terminal-Bench 2.1 對照案例（含「自報未復現」限制標註）。
- 驗證：`grep -qE 'Maka.*Kimi Code|Terminal-Bench.*2\.1.*harness對照|59\.6%.*69\.7%' research/agent-harness/*.md 2>/dev/null && echo OK`

**P1-21（新增）**：`.claude/rules/security-hygiene.md` 或 `.claude/rules/core.md` 補 VentureBeat 54% 企業 agent 安全調查數據，作為 per-agent 身份/沙箱隔離設計的量化外部佐證。
- 驗證：`grep -qE '54%.*enterprise.*agent|agent security gap|VentureBeat.*Pulse Research' .claude/rules/security-hygiene.md .claude/rules/core.md && echo OK`

**P1-22（新增）**：`.claude/refs/model-profiles.md` P1-7（Fable 5 存取狀態查詢指針）補 Nadella 揭露之 Fable 蒸餾（distillation）防護機制細節，作為既有待辦項的證據累積（不新增獨立編號，併入 P1-7）。
- 驗證：`grep -qE 'distillation.*防護|蒸餾.*攔截|Nadella' .claude/refs/model-profiles.md && echo OK`

**P1-1~P1-3、P1-5~P1-19（延續，19 項，見上方回填表逐項天數）**

### P2 — 觀察中（需更多信號再決定）

**P2-1~P2-16（延續自 07-09~07-21，本日無新信號變更判斷）**

**P2-17（新增）**：Grok CLI 事故後續追蹤——是否有其他供應商（OpenAI Codex CLI、Google Gemini CLI 等）被檢驗出類似資料上傳行為，暫不採取行動，僅觀察。

**P2-18（新增）**：Nadella 對前沿模型供應商依賴的公開不滿，是否會加速企業轉向開放權重/多供應商策略（與 Kimi K3/Qwen 3.8 Max 等開放權重追趕敘事的因果關聯），暫列觀察。

---

## GAP 狀態更新

| GAP | 研究前狀態 | 研究後狀態 | 行動 |
|-----|-----------|-----------|------|
| harness-locality-benchmark-maka-vs-kcode | gap (0篇) | **filled** — Terminal-Bench 2.1 完整數字對照 + 效能差距來源三手法記錄 | 新增 P1-20 |
| grok-cli-local-file-exfiltration | gap (0篇) | **filled** — 完整時間線、數據量、曝露資料類型記錄 | 交 security-hygiene.md 追蹤 |
| agent-security-gap-54pct-enterprise | gap (0篇) | **filled** — 107 家企業調查完整方法論與分項數字記錄 | 新增 P1-21 |
| nadella-fable-editorially-controlled | gap (0篇) | **filled** — 直接引語 + 8 家獨立媒體交叉確認記錄 | 併入既有 P1-7 |

---

## 下一次循環優先事項

1. **確認 Routine A 是否已針對 2026-07-22／2026-07-23 補跑選題**：若補跑，本日以 fallback 方式自選的 4 個主題可能與其正式選題重疊，需人工比對兩份輸出並決定是否需要合併或標記其一為冗餘（本項為本日新增最高優先，源於 Unknowns [UU]）。
2. **P1 backlog（現 22 項候選：P1-1~P1-3、P1-5~P1-22）持續累積、落地率連續七次為 0**：連續第七份 report 建議排一次 `/autoload-evolution` 或治理批次 cycle 集中處理；P1-7（現已有 2 筆獨立證據：07-20 Fable5 永久政策 + 本日 Nadella 蒸餾防護細節）、P1-16（Full Access $HOME 事故證據已齊備）建議優先納入下次批次。
3. **P1-1（DAILY-TOPICS 技術路徑交叉驗證流程改進）仍待使用者裁決**，07-15 已提出 (a)/(b)/(c) 三選項，第 13 天無新資訊變更判斷。

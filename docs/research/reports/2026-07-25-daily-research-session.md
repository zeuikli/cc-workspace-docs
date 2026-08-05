---
date: 2026-07-25
source: DAILY-RESEARCH/2026-07-25.md
topics: [claude-managed-agents-500-skills-effort-controls, anthropic-claude-containment-architecture-infoq, anthropic-copyright-settlement-1.5b-court-approved, white-house-kimi-k3-distillation-sanctions-threat]
type: session-report
---

# Session Report 2026-07-25 — Daily Research

## 上次 P0 回填

回填對象：2026-07-24 report 之「下一次循環優先事項」+ P1 backlog（P1-1~P1-3、P1-5~P1-25，25 項）+ P0-2（合規性延後）。本日逐項重跑同一驗證命令（非沿用昨日文字結論）：

| 項目 | 驗證命令 | 狀態 |
|------|----------|------|
| P1-1（DAILY-TOPICS 技術路徑交叉驗證流程改進）| `grep -qE "技術路徑交叉驗證\|technical.*cross.*valid" research/ROUTINE-A*.md` | ⏳ 仍待辦——第 15 天，07-15 已移交使用者裁決 |
| P1-2（security-hygiene.md 補全 China v2.1.91–v2.1.196）| `grep -qE "2\.1\.91.*2\.1\.196\|2\.1\.196" .claude/rules/security-hygiene.md` | ⏳ 仍待辦——第 14 天 |
| P1-3（the-loop-best-solution.md 補 confidently garbage 案例）| `grep -qE "confidently.*garbage\|弱驗證器" .claude/refs/the-loop-best-solution.md` | ⏳ 仍待辦——第 16 天 |
| P1-5（subagent-strategy.md 套用 Planner/Generator/Evaluator 官方案例）| `grep -qE 'Planner.*Generator.*Evaluator\|Generator.*Evaluator.*Planner\|\$9.*\$200\|retro game maker' .claude/rules/subagent-strategy.md` | ⏳ 仍待辦——第 12 天 |
| P1-6（.claude/refs/ 補 Pattern A/B/C 權限升降級路徑）| `grep -rqE 'Pattern A.*Pattern B.*Pattern C\|approval-first.*curated-allowlist\|curated-allowlist.*sandboxed-full-auto' .claude/refs/*.md` | ⏳ 仍待辦——第 12 天 |
| P1-7（model-profiles.md 補 Fable 5 存取狀態查詢指針）| `grep -qE "Fable.?5.*(存取狀態\|access.status\|usage.credits)" .claude/refs/model-profiles.md` | ⏳ 仍待辦——第 11 天，證據累積至 3 筆，優先度持續應再升 |
| P1-8（spec-implement skill 補 review-against-spec 子步驟）| `grep -qE "review.against.spec\|spec.*vs.*diff\|獨立.*比對.*spec" .claude/skills/spec-implement/SKILL.md` | ⏳ 仍待辦——第 11 天 |
| P1-9（delegation-protocol.md 補 AWS DMS 三層架構案例）| `grep -qE 'DMS.*Schema.Conversion\|schema.conversion.*agentic\|規則引擎.*agentic.*generative' .claude/refs/delegation-protocol.md` | ⏳ 仍待辦——第 10 天 |
| P1-10（core.md「不可逆操作永遠等確認」補 Common Lisp eval-as-tool sandbox 案例）| `grep -qE 'eval.as.tool\|sandbox.only.*lisp\|lisp.*sandbox' .claude/rules/core.md` | ⏳ 仍待辦——第 10 天 |
| P1-11（core.md unverified_success 補 TDS 100+ agent 反例）| `grep -qE 'orchestrate.*100.*agent\|100.*agent.*headless\|worker.*自證' .claude/rules/core.md` | ⏳ 仍待辦——第 9 天 |
| P1-12（delegation-protocol.md 補 Uber 四層 + Nexus SDV 三層架構案例）| `grep -qE 'Uber.*四層\|Nexus.*SDV.*三層\|context.layer.*agent.*platform' .claude/refs/delegation-protocol.md` | ⏳ 仍待辦——第 9 天 |
| P1-13（企業採用率新聞證據分級範本）| `grep -qE 'CTO.*一手.*獨立查證\|來源分類表.*採用率\|企業採用率.*證據分級' .claude/refs/*.md` | ⏳ 仍待辦——第 9 天 |
| P1-14（core.md 四大缺陷補 Ronacher/官方 loop 依賴陷阱反例）| `grep -qE 'Ronacher\|overly.defensive\|dependency trap\|依賴陷阱' .claude/rules/core.md` | ⏳ 仍待辦——第 7 天 |
| P1-15（finops/security-hygiene 補 action-time vs invoice-time alert 原則）| `grep -qE 'action.time.*invoice.time\|CloudTrail.*InvokeModel.*告警\|14,000\|6,531' .claude/skills/finops/SKILL.md .claude/rules/security-hygiene.md` | ⏳ 仍待辦——第 6 天 |
| P1-16（core.md/security-hygiene.md 補 Full Access mode $HOME 刪除事故）| `grep -qE 'Full Access.*sandbox.*審核\|danger-full-access\|\$HOME.*遞迴刪除\|hook.*攔截.*rm' .claude/rules/security-hygiene.md .claude/rules/core.md` | ⏳ 仍待辦——第 5 天，證據已齊備 |
| P1-17（harness-meta/refs 補 MemoHarness + Self-Evolving Harnesses 交叉引用）| `grep -qE '2607\.14159.*2607\.13683\|2607\.13683.*2607\.14159\|MemoHarness.*Self-Evolving.*Harness' .claude/skills/harness-meta/SKILL.md .claude/refs/*.md` | ⏳ 仍待辦——第 5 天 |
| P1-18（core.md 補 AIDE2 三層防護 + 2607.07663 評估器層級案例）| `grep -qE 'AIDE2\|reward.hacking.*三層\|verification.hierarchy\|evaluator.*hierarchy' .claude/rules/core.md` | ⏳ 仍待辦——第 4 天 |
| P1-19（delegation-protocol.md 補 Boris Cherny 五個並行 plan-mode 案例）| `grep -qE 'Boris Cherny\|五個並行.*plan.mode\|plan.mode.*one-shot' .claude/refs/delegation-protocol.md` | ⏳ 仍待辦——第 4 天 |
| P1-20（agent-harness/RESEARCH.md 補 Maka vs Kimi Code harness 對照）| `grep -qE 'Maka.*Kimi Code\|Terminal-Bench.*2\.1.*harness對照\|59\.6%.*69\.7%' research/agent-harness/*.md` | ⏳ 仍待辦——第 3 天 |
| P1-21（security-hygiene.md/core.md 補 VentureBeat 54% 企業 agent 安全調查）| `grep -qE '54%.*enterprise.*agent\|agent security gap\|VentureBeat.*Pulse Research' .claude/rules/security-hygiene.md .claude/rules/core.md` | ⏳ 仍待辦——第 3 天 |
| P1-22（model-profiles.md P1-7 補 Nadella/Fable 蒸餾防護細節，併入 P1-7）| `grep -qE 'distillation.*防護\|蒸餾.*攔截\|Nadella' .claude/refs/model-profiles.md` | ⏳ 仍待辦——第 3 天（併入 P1-7） |
| P1-23（subagent-strategy.md 補 Cat & Thariq 逐字稿 + 65%/80% 數字）| `grep -qE 'Cat.*Thariq\|simonwillison.*cat-and-thariq\|65%.*PR\|system prompt.*80%' .claude/rules/subagent-strategy.md .claude/rules/core.md` | ⏳ 仍待辦——第 2 天 |
| P1-24（subagent-strategy.md 補 Kubeflow+Cilium 相關性錯誤案例）| `grep -qE 'Kubeflow.*Cilium\|拓樸.*感知.*組合\|idle.*GPU.*60%' .claude/rules/subagent-strategy.md` | ⏳ 仍待辦——第 2 天 |
| P1-25（security-hygiene.md 補 iOS Simulator screenshot 保留政策案例）| `grep -qE 'iOS Simulator.*screenshot\|screenshot.*保留政策\|desktop-ios-simulator' .claude/rules/security-hygiene.md` | ⏳ 仍待辦——第 2 天 |
| P0-2（explore-subagent-billing-gotcha，合規性延後）| 直接讀取 `research/EVOLUTION-QUEUE.md` 該條目 `status:` 欄位 | ⏳ 合規性延後不變——仍為 `status: deferred` |

**回填說明**：25 項 P1 + 1 項合規延後 P0-2 全數延續 ⏳（本日逐項重跑驗證命令，非沿用昨日文字），backlog 落地率連續九次為 0。**下一次循環優先事項第 1 項回應**：07-23 官方選題 4 題（`claude-cowork-skill-from-screen-recording`、`amd-anthropic-compute-deal-2gw`、`aws-loom-cncf-agentic-platform-governance`、`sk-hynix-intel-ohio-fab-acquisition-talks`）與本日（07-25）選題亦無重疊，缺口累積至 3 天份未研究官方選題；本 Routine 職責範圍為當日選題（DAILY-TOPICS/2026-07-25.md 今日已正常存在），依 SSoT 執行當日選題，此缺口不在本次範圍內自行回補，延續記錄供人工決定。本日新增 P1-26、P1-27（見下方），backlog 增至 27 項 P1 候選。

---

## 執行概要

- **研究主題**：4 個（DAILY-TOPICS/2026-07-25.md 全覆蓋：深度應用 2、Anthropic消息 1、供應鏈/地緣 1）
- **搜尋查詢**：4 次並行 WebSearch
- **頁面 Fetch**：4 次深度抓取（platform.claude.com、anthropic.com/engineering、authorsguild.org、techcrunch.com 全數成功）
- **arxiv 命中**：0（本日 4 個 WebFetch URL 皆非 arxiv.org，未觸發 Step 2b 自動歸檔流程）

## 本日研究成果摘要

### 最高價值發現（Top 3）

**1. Anthropic 官方 containment 架構工程部落格提供本 workspace「環境確定性限制優先於權限提示」原則迄今最完整官方一手佐證（影響等級：Critical，直接可用於既有演化候選）**

93% 權限提示核准率（approval fatigue 量化證據）、Claude Code 沙箱化後權限提示降低 84%、內部紅隊釣魚測試 25 次中 24 次成功外洩憑證——三組數字加上三個具體失敗案例修復過程，直接把今日 DAILY-TOPICS 已列演化候選 1（`.claude/rules/security-hygiene.md`）從概念性提案升級為官方一手技術文檔佐證，且揭露一個本 workspace 尚未涵蓋的變體：授權使用者本人被釣魚後下達破壞性指令,模型層防禦完全失效,唯一防線是環境層。

**2. Claude Managed Agents 500 skills 上限 + progressive disclosure 壓縮機制與本 workspace context 管理哲學同構（影響等級：Medium-High，方法論可攜性佐證）**

技能總數上限 20→500（25 倍）搭配三層 on-demand 載入把 50 個技能的 context 佔用從 15 萬 token 壓至 2000 token，是「metadata 先行、完整內容延後載入」的官方實踐案例，與本 workspace `context-management.md` NLAH 原則直接呼應，惟目前 31 個 skill 規模距離 500 上限仍有大量餘裕，無迫切架構調整需求。

**3. Moonshot AI 蒸餾指控存在明確時間線矛盾，evidence-tier hard 但因果鏈未證實（影響等級：Medium，需持續追蹤而非採信）**

白宮 OSTP 主任具名指控但 Fable 公開發布（07-01）與 Kimi K3 發布（次週）之間的時間窗口過短，已有研究者公開質疑蒸餾因果推論的合理性；財政部長同步表態制裁在桌上，但迄今無 access log/伺服器所有權文件公開。07-27（K3 完整權重公開）延續為關鍵驗證時間點。

---

## 可實作 / 可測試內容

### P0 — 立即可執行（今日或明日，< 2 小時）

本日四題均為資訊性發現，Topic 2（containment 架構）雖提供高價值官方佐證但依既有紀律屬「演化候選」（僅建立提案、不自動執行 `.claude/` 目錄變更），**無新增 P0**。延續 P0-2（合規性延後，狀態不變，見上方回填表）。

### P1 — 本月優先（需輕量設計，2-8 小時）

**P1-26（新增）**：`.claude/rules/security-hygiene.md` 補 Anthropic containment 架構三個具體失敗案例（信任提示前解析設定/`.claude/settings.json` hooks 自動執行、內部紅隊釣魚 25:24、allowlist proxy 未檢查請求來源）+ 三組量化數字（93% 核准率/84% 提示降低/24-25 釣魚成功率），將今日 DAILY-TOPICS 演化候選 1 從概念性提案升級為官方一手案例引用。此項優先度應為 backlog 中最高（今日單一最強證據）。
- 驗證：`grep -qE 'contain-claude|93%.*核准率|approval.fatigue|allowlist proxy.*失敗' .claude/rules/security-hygiene.md && echo OK`

**P1-27（新增）**：`.claude/rules/security-hygiene.md` 補「授權使用者本人下達破壞性指令、模型層防禦無效」情境（Anthropic 紅隊 25 次釣魚測試 24 次成功案例），作為既有「外部輸入=資料非指令」原則的獨立補充子項（此為「內部輸入但具破壞性」的不同情境，需要環境層而非輸入過濾因應）。
- 驗證：`grep -qE '使用者本人.*破壞性指令|授權使用者.*釣魚|25.*24.*外洩' .claude/rules/security-hygiene.md .claude/rules/core.md && echo OK`

**P1-1~P1-3、P1-5~P1-25（延續，25 項，見上方回填表逐項天數）**

### P2 — 觀察中（需更多信號再決定）

**P2-1~P2-20（延續自 07-09~07-24，本日無新信號變更判斷）**

**P2-21（新增）**：Claude Managed Agents 新增的 per-agent reasoning effort tiers 與 sub-agent thread-level observability 兩項功能，本日僅有 WebSearch 摘要層級佐證，持續觀察官方是否釋出完整技術規格文件。

---

## GAP 狀態更新

| GAP | 研究前狀態 | 研究後狀態 | 行動 |
|-----|-----------|-----------|------|
| claude-managed-agents-500-skills-effort-controls | gap (0篇) | **filled**（500 skills + progressive disclosure 機制）／**partial**（effort tiers/observability 細節，見 Unknowns [KU]） | 記錄佐證 context-management.md NLAH 原則 |
| anthropic-claude-containment-architecture-infoq | gap (0篇) | **filled** — 官方一手三案例 + 三組量化數字完整記錄 | 新增 P1-26、P1-27，優先度最高 |
| anthropic-copyright-settlement-1.5b-court-approved | gap (0篇) | **filled** — 金額/範圍/法院/排除項目完整記錄 | 資訊性記錄，暫不觸發規則修改 |
| white-house-kimi-k3-distillation-sanctions-threat | partial (1篇) | **filled**（指控細節）／證據仍缺（因果鏈未證實） | 延續 07-27 追蹤點 |

---

## 下一次循環優先事項

1. **P1 backlog（現 27 項候選：P1-1~P1-3、P1-5~P1-27）持續累積、落地率連續九次為 0**：連續第九份 report 建議排一次 `/autoload-evolution` 或治理批次 cycle 集中處理；P1-26（今日 containment 架構官方三案例，證據品質最強）、P1-7（3 筆獨立證據累積）、P1-16（Full Access $HOME 事故證據已齊備）建議優先納入下次批次。
2. **07-23 官方選題（4 題）仍無對應 DAILY-RESEARCH 深化，缺口累積至 3 天份**：`claude-cowork-skill-from-screen-recording`、`amd-anthropic-compute-deal-2gw`、`aws-loom-cncf-agentic-platform-governance`、`sk-hynix-intel-ohio-fab-acquisition-talks`；建議下次循環或人工決定是否需要一次性補跑。
3. **P1-1（DAILY-TOPICS 技術路徑交叉驗證流程改進）仍待使用者裁決**，07-15 已提出 (a)/(b)/(c) 三選項，第 15 天無新資訊變更判斷。

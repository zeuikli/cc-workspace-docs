---
date: 2026-07-20
source: DAILY-RESEARCH/2026-07-20.md
topics: [agent-harness-rmrf-fullaccess-openai-postmortem-denylist, memoharness-six-control-surfaces-modular-decomposition, fable5-permanent-max-team-premium-0720, cncf-hami-gpu-resource-management-kubernetes-incubating, kimi-k3-distillation-export-control-narrative-shift]
type: session-report
---

# Session Report 2026-07-20 — Daily Research

## 上次 P0 回填

昨日（2026-07-19）report 之「下一次循環優先事項」+ P1 backlog 逐項機械驗證如下：

| 項目 | 驗證命令 | 狀態 |
|------|----------|------|
| P1-1（DAILY-TOPICS 技術路徑交叉驗證流程改進）| `grep -qE "技術路徑交叉驗證|technical.*cross.*valid" research/ROUTINE-A*.md` | ⏳ 仍待辦——第 10 天，07-15 已移交使用者裁決，本日無新資訊變更此判斷 |
| P1-2（security-hygiene.md 補全 China v2.1.91–v2.1.196）| `grep -qE "2\.1\.91.*2\.1\.196|2\.1\.196" .claude/rules/security-hygiene.md` | ⏳ 仍待辦——第 9 天 |
| P1-3（the-loop-best-solution.md 補 confidently garbage 案例）| `grep -qE "confidently.*garbage|弱驗證器" .claude/refs/the-loop-best-solution.md` | ⏳ 仍待辦——第 11 天 |
| P1-5（subagent-strategy.md 套用 Planner/Generator/Evaluator 官方案例）| `grep -qE 'Planner.*Generator.*Evaluator|Generator.*Evaluator.*Planner|\$9.*\$200|retro game maker' .claude/rules/subagent-strategy.md` | ⏳ 仍待辦——第 7 天 |
| P1-6（.claude/refs/ 補 Pattern A/B/C 權限升降級路徑）| `grep -rqE 'Pattern A.*Pattern B.*Pattern C|approval-first.*curated-allowlist|curated-allowlist.*sandboxed-full-auto' .claude/refs/*.md` | ⏳ 仍待辦——第 7 天 |
| P1-7（model-profiles.md 補 Fable 5 存取狀態查詢指針）| `grep -qE "Fable.?5.*(存取狀態|access.status|usage.credits)" .claude/refs/model-profiles.md` | ⏳ 仍待辦——第 6 天，本日 Topic 3（Fable 5 確立永久政策）進一步降低此項不確定性，建議優先納入下次治理批次 |
| P1-8（spec-implement skill 補 review-against-spec 子步驟）| `grep -qE "review.against.spec|spec.*vs.*diff|獨立.*比對.*spec" .claude/skills/spec-implement/SKILL.md` | ⏳ 仍待辦——第 6 天 |
| P1-9（delegation-protocol.md 補 AWS DMS 三層架構案例）| `grep -qE 'DMS.*Schema.Conversion|schema.conversion.*agentic|規則引擎.*agentic.*generative' .claude/refs/delegation-protocol.md` | ⏳ 仍待辦——第 5 天 |
| P1-10（core.md「不可逆操作永遠等確認」補 Common Lisp eval-as-tool sandbox 案例）| `grep -qE 'eval.as.tool|sandbox.only.*lisp|lisp.*sandbox' .claude/rules/core.md` | ⏳ 仍待辦——第 5 天 |
| P1-11（core.md unverified_success 補 TDS 100+ agent 反例）| `grep -qE 'orchestrate.*100.*agent|100.*agent.*headless|worker.*自證' .claude/rules/core.md` | ⏳ 仍待辦——第 4 天 |
| P1-12（delegation-protocol.md 補 Uber 四層 + Nexus SDV 三層架構案例）| `grep -qE 'Uber.*四層|Nexus.*SDV.*三層|context.layer.*agent.*platform' .claude/refs/delegation-protocol.md` | ⏳ 仍待辦——第 4 天 |
| P1-13（企業採用率新聞證據分級範本）| `grep -qE 'CTO.*一手.*獨立查證|來源分類表.*採用率|企業採用率.*證據分級' .claude/refs/*.md` | ⏳ 仍待辦——第 4 天 |
| P1-14（core.md 四大缺陷補 Ronacher/官方 loop 依賴陷阱反例）| `grep -qE 'Ronacher|overly.defensive|dependency trap|依賴陷阱' .claude/rules/core.md` | ⏳ 仍待辦——第 2 天，本日 Topic 1（OpenAI Full Access 官方 postmortem）提供第三個獨立佐證（移除保護層=高風險），惟本身非「依賴陷阱」案例，不直接疊加，另立 P1-16 |
| P1-15（finops/security-hygiene 補 action-time vs invoice-time alert 原則）| `grep -qE 'action.time.*invoice.time|CloudTrail.*InvokeModel.*告警|14,000|6,531' .claude/skills/finops/SKILL.md .claude/rules/security-hygiene.md 2>/dev/null` | ⏳ 仍待辦——第 1 天 |
| P0-2（explore-subagent-billing-gotcha，合規性延後）| 直接讀取 `research/EVOLUTION-QUEUE.md` 該條目 `status:` 欄位 | ⏳ 合規性延後不變——仍為 `status: deferred` |

**回填說明**：14 項 P1 + 1 項合規延後 P0-2 全數延續 ⏳（本日無新落地）。P1 backlog 落地率持續偏低，第五次印證「Routine C 無 `.claude/rules`/`.claude/refs`/`.claude/skills` 直接寫入權限，需 `/autoload-evolution` cycle 或人工批次處理視窗」的治理層級判斷（07-16~07-19 report 已重複指出，本日不再展開）。本日新增 P1-16、P1-17（見下方），backlog 增至 16 項候選。

---

## 執行概要
- **研究主題**：5 個（DAILY-TOPICS/2026-07-20.md 全覆蓋：2 深度應用、1 Anthropic消息、1 職業領域、1 供應鏈/地緣）
- **搜尋查詢**：5 次並行 WebSearch
- **頁面 Fetch**：9 次深度抓取（3 次因 403/內容不符失敗改用備援來源：developers.openai.com→learn.chatgpt.com 仍不符改用 explainx.ai、techtimes.com 403、transformernews.ai 403 改用 gizmodo.com；6 次直接成功：arxiv.org ×2、simonwillison.net、cncf.io、axios.com、explainx.ai）
- **arxiv 命中**：1（MemoHarness, arxiv 2607.14159）— 去重檢查未命中既有歸檔，已建立 `research/papers/2026-07-20-memoharness-six-control-surfaces-2607-14159.md`；PDF 本地下載成功但 git push relay 對此次 push 回傳 HTTP 413（診斷見 DAILY-RESEARCH Unknowns），未隨 commit 推送，frontmatter 標 `pdf_status: push_size_limited` 並改引官方 arxiv PDF URL（Deviation，非「下載失敗」，屬本次 session 基礎設施限制）

## 本日研究成果摘要

### 最高價值發現（Top 3）

**1. OpenAI Codex Full Access mode $HOME 遞迴刪除官方證實事故（影響等級：Critical，方法論意義最高）**

OpenAI 產品負責人官方證實三段式根因鏈（Full Access 同時關閉 sandbox+審核 → `$HOME` 環境變數覆寫失敗 → 誤刪真實 home directory），與本 workspace core.md 刪除風險三級規則、「不可逆操作永遠等確認」鐵律直接印證。官方公佈四項具體緩解建議（隔離環境/hook 攔截 rm/絕對路徑/session 前檢查漂移），可直接引用為規則補充案例。

**2. MemoHarness 六控制介面 + 雙層 experience bank 量化成果（影響等級：High）**

Terminal-Bench 0.806 vs 0.722 基準（+11.6% 相對提升）、成本降低 33%（$6.89 vs $10.28），與 07-15 已歸檔的 Self-Evolving Agent Harnesses（2607.13683）「診斷/認證分離」設計高度相近，兩篇論文累積為 core.md 公理「判斷 vs 決定」的外部收斂證據。

**3. Fable 5 永久政策確立 + Kimi K3 敘事分歧（影響等級：High）**

Fable 5 因 GPT-5.6 Sol／Kimi K3 競爭壓力永久納入 Max/Team Premium，直接解除 P1-7 的「臨時延長」不確定性。同時 Kimi K3 本身觸發「已追平前沿」vs「未達前沿」兩派敘事分歧（Axios vs transformernews.ai），未經裁決，列為本日最大 Unknown。

---

## 可實作 / 可測試內容

### P0 — 立即可執行（今日或明日，< 2 小時）

本日五題均為資訊性發現，無 workspace 缺陷修復需求，**無新增 P0**。延續 P0-2（合規性延後，狀態不變，見上方回填表）。

### P1 — 本月優先（需輕量設計，2-8 小時）

**P1-1~P1-3、P1-5~P1-15（延續，14 項，見上方回填表逐項天數）**

**P1-16（新增）**：`.claude/rules/security-hygiene.md` 或 core.md 補「Full Access mode（sandbox+審核同時關閉）」風險範例，附本日 Codex $HOME 刪除事故完整根因鏈 + 四項官方緩解建議。
- 驗證：`grep -qE 'Full Access.*sandbox.*審核|danger-full-access|\$HOME.*遞迴刪除|hook.*攔截.*rm' .claude/rules/security-hygiene.md .claude/rules/core.md 2>/dev/null && echo OK`

**P1-17（新增）**：`harness-meta` skill 或 `.claude/refs/` 補 MemoHarness（2607.14159）+ Self-Evolving Agent Harnesses（2607.13683）交叉引用段落。
- 驗證：`grep -qE '2607\.14159.*2607\.13683|2607\.13683.*2607\.14159|MemoHarness.*Self-Evolving.*Harness' .claude/skills/harness-meta/SKILL.md .claude/refs/*.md 2>/dev/null && echo OK`

### P2 — 觀察中（需更多信號再決定）

**P2-1 ~ P2-13（延續，來自 07-09～07-19，本日無新信號）**

**P2-14（新增）**：Kimi K3「已追平前沿」vs「未達前沿」敘事分歧持續追蹤，待第三方獨立 benchmark 復現結果再裁決。

---

## GAP 狀態更新

| GAP | 研究前狀態 | 研究後狀態 | 行動 |
|-----|-----------|-----------|------|
| agent-harness-rmrf-incident | gap (0篇) | **filled** — OpenAI 官方三段式根因鏈 + 四項緩解建議完整記錄 | 新增 P1-16 |
| memoharness-control-surfaces | gap (0篇) | **filled** — 六控制介面定義 + 量化基準（0.806/0.722, $6.89/$10.28）完整記錄，論文已歸檔 | 新增 P1-17 |
| fable5-permanent-policy | gap (0篇) | **filled** — 永久政策生效日期/方案細節/競爭壓力脈絡完整記錄 | 解除 P1-7 不確定性，建議優先處理 |
| hami-gpu-k8s | gap (0篇) | **filled** — 技術機制/社群規模/生產案例完整記錄 | 交 Routine F 深化 career-wiki |
| kimi-distillation-export-control | gap (0篇) | **filled**（部分）— 正反兩派敘事並列記錄，未裁決 | 新增 P2-14 追蹤 |

---

## 下一次循環優先事項

1. **P1 backlog（現 16 項候選：P1-1~P1-3、P1-5~P1-17）持續累積、落地率偏低（本日 0 項新落地）**：連續第五份 report 建議排一次 `/autoload-evolution` 或治理批次 cycle 集中處理已齊備證據的 P1 項目，其中 P1-7（Fable 5 永久政策）證據已完整齊備，建議優先納入下次批次。
2. **P1-1（DAILY-TOPICS 技術路徑交叉驗證流程改進）仍待使用者裁決**，07-15 已提出 (a)/(b)/(c) 三選項，第 10 天無新資訊變更判斷。
3. **P2-14（Kimi K3 敘事分歧）+ P2-11~P2-13（延續自 07-18/07-19）待下次選題或 Routine F 分別處理**，本 Routine 僅負責交接標記。

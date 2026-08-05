---
date: 2026-07-10
source: DAILY-RESEARCH/2026-07-10.md
topics: [harness-recursive-self-improvement-lilian-weng, managed-agent-vs-specialized-sandbox-devx, claudedevs-oss-maintainer-max20x-program, harvey-lab-aa-legal-benchmark-fable5-14pct]
type: session-report
---

# Session Report 2026-07-10 — Daily Research

## 上次 P0 回填

昨日（2026-07-09）report 之「下一次循環優先事項」逐項機械驗證如下：

| 項目 | 驗證命令 | 狀態 |
|------|----------|------|
| P0-1：tool-schema-degradation 提案套用至 model-profiles.md | `grep -qE 'tool.schema\|edit.tool.*degrad\|third.party.*schema' .claude/refs/model-profiles.md` | ✅ **已落實**——連續 4 天積壓後，Routine B 已於本 session 之前完成套用，grep 通過 |
| P0-2：China 偵測案例（v2.1.91）補充至 security-hygiene.md | `grep -iq "2.1.91" .claude/rules/security-hygiene.md` | ⏳ 仍待辦（第 2 天），佐證已齊備，僅缺實際套用動作 |
| 監控 EVOLUTION-QUEUE 待審提案數 | `grep -c '**status**: proposed' research/EVOLUTION-QUEUE.md` | ⏳ 仍為 3（未降至警示門檻以下，維持觀察） |

**回填說明**：P0-1 為連續 4 天標記為「harness 治理層系統性延遲」的最高優先項，本日確認已由 Routine B 執行完畢——治理層積壓問題本次已解除，驗證了 core.md「同一失敗簽名獨立重現 ≥2 次才改規則」原則下的升級措辭確實促成後續執行動作，非空轉。P0-2（China 偵測）已連續 2 天佐證齊備但未套用，本日不再重複升級措辭（僅 2 天，未達 P0-1 當時的 4 天閾值），改列本日 P0 延續項並直接標注「不宜再以觀察期未滿為由延遲」。

---

## 執行概要
- **研究主題**：4 個（DAILY-TOPICS/2026-07-10.md 全覆蓋）
- **搜尋查詢**：6 次並行 WebSearch
- **頁面 Fetch**：4 次深度抓取（Lilian Weng 官方部落格、Modal 官方 sandbox 比較文、Anthropic 官方 Claude for Open Source 頁面、Artificial Analysis 官方 Harvey LAB-AA 文章）

## 本日研究成果摘要

### 最高價值發現（Top 3）

**1. Lilian Weng「Harness Engineering for Self-Improvement」正式發文，將 RSI 重新框定為 harness 層問題（影響等級：Critical）**

2026-07-04 發文，論證近期 RSI 不靠模型權重自我改寫，而是靠 harness（部署系統）自我演化，並提出 propose-evaluate-accept 迴圈的具體實作模式（Self-Harness：weakness mining → bounded proposal → held-out validation）。七大開放挑戰中，「負面結果偏誤」與「長期健康度指標」是本 workspace 目前完全未涵蓋的兩個維度，其餘五項（弱評估器/記憶生命週期/多樣性崩潰/reward hacking/人類角色）均已有對應機制，構成外部研究對既有設計的獨立第三方驗證。

**2. Harvey LAB-AA 法律基準確認 model-profiles.md 演化候選數字準確（影響等級：High）**

Fable 5 all-pass 14.2% 領先，Opus 4.8／GLM-5.2 並列 7.5%，GLM 成本僅 Fable 6.9%（$1.30 vs $18.90/task）——與 DAILY-TOPICS 選題文件記載數字完全吻合，交叉驗證通過，DAILY-TOPICS 演化候選（legal-task-type-cost-exception）可直接套用，無需進一步查證。

**3. Managed agent runtime vs 專用 sandbox provider 的技術分野確立，但原選題引用來源未能精確定位（影響等級：Medium）**

隔離機制（gVisor vs Firecracker microVM）、session 時長、GPU 支援的產業比較資料齊備，但原選題預期的「Latent Space Modal 訪談」逐字稿未能精確搜得，改以 Modal 官方文件替代，「managed agent 適合起步、sandbox provider 才給生產控制」的論點屬合理推論而非直接引用驗證，本日已在 DAILY-RESEARCH 中明確標注此限制，避免過度宣稱信心水準。

---

## 可實作 / 可測試內容

### P0 — 立即可執行（今日或明日，< 2 小時）

**P0-1（新增，本日提出，證據已齊備）**：套用 legal-task-type-cost-exception 至 model-profiles.md——Harvey LAB-AA 數字本日經官方來源交叉驗證確認準確，無延遲理由。
- 驗證：`grep -qE 'Harvey|legal.*task.*exception|14\.2%' .claude/refs/model-profiles.md && echo OK`

**P0-2（延續，第 2 天）**：China 偵測案例（v2.1.91）補充至 security-hygiene.md，佐證已連續 2 天齊備未套用，不宜再延遲。
- 驗證：`grep -iq "2.1.91" .claude/rules/security-hygiene.md && echo OK`

### P1 — 本月優先（需輕量設計，2-8 小時）

**P1-1（延續）**：the-loop-best-solution.md 補「confidently garbage」失敗案例，本日新增 Self-Harness 論文作為可引用的具體理論來源。
- 驗證：`grep -qE "confidently.*garbage|弱驗證器" .claude/refs/the-loop-best-solution.md && echo OK`

**P1-2（延續）**：the-loop-best-solution.md 補 Self-Harness 論文引用（本日確認論文存在且與 workspace 現有 autoload-evolution 閉環高度同構）。
- 驗證：`grep -q "Self-Harness" .claude/refs/the-loop-best-solution.md && echo OK`

**P1-3（新增，本日提出）**：評估是否需在 core.md RECORD 階段新增「負面結果判定」機制（何時該放棄假設 vs. 繼續嘗試），對應 Weng 七大挑戰中本 workspace 尚未涵蓋的 #3 缺口。需先設計具體判準草案，非可直接套用項。

### P2 — 觀察中（需更多信號再決定）

**P2-1（延續，來自 07-09）**：Constitutional Classifiers++ 級聯架構作為 quality-pipeline / gap-vote 成本優化參考。

**P2-2（新增）**：Gemini 3.1 Flash-Lite 在 Harvey LAB-AA 的 31.1%/$0.02 極端數字，因評測子集/口徑存疑，待更多獨立信號源交叉驗證後再考慮納入 model-profiles.md。

**P2-3（新增）**：ClaudeDevs OSS maintainer 計畫作為 Anthropic 客群擴張策略觀察指標，暫無直接行動項，不適用於私有 workspace。

**P2-4（新增）**：Weng 七大挑戰中「長期健康度指標」（coding agent 短期任務完成 vs 長期 repo 健康維護）作為未來 core.md APPLY/RECORD 階段設計參考，需更多外部案例佐證後再評估是否納入。

---

## GAP 狀態更新

| GAP | 研究前狀態 | 研究後狀態 | 行動 |
|-----|-----------|-----------|------|
| recursive-self-improvement-harness | gap (0篇) | **filled** — propose-evaluate-accept 迴圈 + 七大挑戰 + 三個具體系統案例齊備 | P1-1/P1-2（理論引用）+ P1-3（機制設計候選） |
| managed-agent-sandbox-architecture | gap (0篇) | **partial-filled** — 技術分野資料齊備，但原引用來源（Latent Space Modal 訪談）未精確定位，信心水準需保留 | 無直接行動項，純參考 |
| oss-maintainer-program | gap (0篇) | **filled** — 資格條件五類 + 福利內容 + 到期規則齊備 | P2-3（觀察項，私有 workspace 不適用） |
| legal-benchmark-harvey | gap (0篇) | **filled** — 完整 leaderboard 數字 + 方法論 + 成本比較齊備，與 DAILY-TOPICS 原始數字交叉驗證通過 | P0-1（可直接套用） |

---

## 下一次循環優先事項

1. **P0-1（legal-task-type-cost-exception 套用至 model-profiles.md）證據已完整交叉驗證，應為下次任何 session 有 model-profiles.md 編輯機會時最優先套用項**，不應再拖延（Harvey LAB-AA 數字準確度已達可直接引用標準）。
2. **P0-2（China 偵測 v2.1.91 補充 security-hygiene.md）已連續 2 天佐證齊備未套用**：若下次仍未套用，第 3 天起應比照 P0-1 先例採用「治理層系統性延遲」升級措辭。
3. **P1-3（負面結果判定機制）為本日新識別的 harness 缺口**，建議列入下次 autoload-evolution 掃描候選，需先產出具體判準草案（例如：連續 N 次同簽名失敗 且 無新增資訊 → 觸發放棄建議而非繼續重試）。

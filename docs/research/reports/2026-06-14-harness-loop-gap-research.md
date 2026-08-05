---
title: "harness↔The Loop 搭配 gap 研究 — 5 輪自行迴圈（/loop 動態模式）"
date: 2026-06-14
status: research-only（提案未 apply；apply 須走 /autoload-evolution gated loop + 使用者核准）
basis: .claude/refs/harness-loop.md §Frontier（7 點）+ §開放問題 為比對基準；scratch gap-log = /tmp/claude-scratch/harness-loop-gap-log.md
method: "The Loop 六階段（OBSERVE→IDENTIFY→PROPOSE→APPLY→TEST→RECORD）；/loop 動態自配速；5 輪 multi-mode-agent fan-out（Opus 4.8 ceiling + Sonnet 4.6 quality）+ researcher paper-scout；**每 finding 主對話 grep 重驗（verdict 非證據）**；弱接地依 APPLY 前置 gate defer"
scope: .claude/refs/harness-loop.md · .claude/rules/core.md · .claude/rules/subagent-strategy.md · research/papers（12 篇消化 + 6 篇新收錄）
type: research
---

# harness↔The Loop 搭配 gap 研究報告

> **TLDR**：對 `harness-loop.md` §Frontier（7 點）做 5 輪 gap-finding，動用 Opus 4.8 + Sonnet 4.6 fan-out。**12 個 confirmed gap 橫跨全六階段**，皆論文數字接地 + 主對話 grep 重驗（exit=1 確認未掛載）。新收錄 6 篇 2026-05/06 harness 論文到 `research/papers/`。1 項 un-defer 候選（Adaptive-Auto-Harness EGL → 維持 defer 但升「觀察」）；1 項刻意非 gap（RHO self-preference 與 workspace「非 LLM 自評」哲學衝突）。**本報告為研究交付物，提案未套用**——任何掛載須走 `/autoload-evolution` gated loop（≤1 規則/cycle、≤50 行 diff、eval 回歸 ≥5pp → revert）+ 使用者核准；當前 auto-load 18,243/19,000（餘 757B），多數提案須先壓 byte。

---

## 方法與紀律（嚴守 harness-loop.md + core.md）

- **OBSERVE baseline**：healthcheck PASS 123 / WARN 3 / FAIL 0；auto-load 18,243B / 19,000 cap；§Frontier 已引 9 paper ID 全驗在。
- **gap-finding 而非 re-synthesis**：corpus 成熟（2026-06-11 The Loop canonical 化），靶心 = §Frontier 未掛載的 frontier finding，非重新合成（守 harness-loop.md 使用原則）。
- **verdict 非證據**：每個 sub-agent 宣稱的「未掛載」，主對話親跑 `grep -niE` 重驗（exit=1 = 0 命中 = 真未掛載）；F5 排除 false-positive 子字串命中。確定性 gate 絕不經 sub-agent 中介（core.md:57 `unverified_success`）。
- **弱接地 → defer**：論文僅診斷無量化解方 → 依 APPLY 前置 gate「弱接地疑為 false positive → defer」，不入 loop 結構。
- **fan-out 紀律**：每輪 ≤4 並行 sub-agent（subagent-strategy.md fan-out≤4）；Opus/ceiling 配架構映射任務、Sonnet/quality 配量化抽取任務。

---

## 確認 gap（12 項，依 Loop 階段排列）

> 每項：finding｜論文接地（數字）｜主對話 grep 重驗｜階段｜提案措辭（**未實作**）。

### OBSERVE 階段（3）

| ID | Finding | 接地 | grep 重驗 | 提案 |
|----|---------|------|----------|------|
| **F6** | Cold-start 混合模型揭示 benchmark 分數系統性偏差：cross-session memory/compression 在 task-independent benchmark 因空狀態，測出 `E[R\|n]=w·p_∞+(1−w)·p_base` 非 production 穩態 | HARBOR 2604.20938 | `cold-start\|mixture\|cross-session` exit=1 | OBSERVE baseline 採集須標 cold-state 偏差風險；warm-up n 輪後採 p_∞，或用 pre-seeded memory 的 task-aware suite。**與 §Frontier #6 不同**（#6=換版本觸發；本=同版本 cold-state 讀數） |
| **F7** | read/write 非對稱遙測抓 silent feature-integration bug：`reflections_written=80/retrieved=0`（container 非持久）、`PASTE_invocations=0`（feature 從未啟動），pass rate 不變 | HARBOR 2604.20938 | `read/write\|asymmetry\|telemetry` exit=1 | OBSERVE healthcheck 擴充：啟用寫後讀型 feature（memory/cache/reflection）時查 write>0∧read=0 非對稱性 = silent bug。**與 §Frontier #4 不同**（#4=agent 行為退化；本=harness feature 層 silent failure） |
| **F11** | verifier-grounded 失敗訊號叢集：失敗 trace 依（terminal cause × agent behavior status × abstract mechanism）三元組分群 → 結構化模式非孤立軼事 | Self-Harness 2606.09498 | `cluster\|failure-signature` exit=1 | OBSERVE 弱點挖掘加 typed-failure 叢集步驟，把扁平 GOTCHAS lesson 轉為類型化模式類別，降 PROPOSE 雜訊 |

### IDENTIFY 階段（1）

| ID | Finding | 接地 | grep 重驗 | 提案 |
|----|---------|------|----------|------|
| **F5** | 無單一 automated skill-learning 方法跨 task type 稱霸；human-authored STR ~0.8 vs automated ~0.4–0.6 | SkillLearnBench 2604.20087 | `STR\|dominate\|no-method`（命中皆 false-positive，特定詞 exit=未掛載） | skill 品質驗收加 Skill Transfer Rate 概念（學到的 skill 能否遷移到結構相似未見任務）；domain 差異顯著時分別評估，不單一方法論跨域套用 |

### PROPOSE 階段（2）

| ID | Finding | 接地 | grep 重驗 | 提案 |
|----|---------|------|----------|------|
| **F4** | 強 base model ≠ 更好的 learned skill；強模型可能因 prior-knowledge 干擾更難吸收 task-specific procedure（反直覺） | SkillLearnBench 2604.20087 | `stronger-model\|over-rely` exit=1 | skill-evolution implementer 選型不可依 model tier 線性推斷品質；對 skill generation 採 mid-tier 試跑 + 外部 STR 評分，非直接指派 frontier。**補強 §Frontier #6**（#6=升級重基線，未涵蓋此選型盲點） |
| **F8** | 子代理單次 run 輪次上限（10-turn limit）防 context 失控；Repeat Rate 0.89（frontier 等級）；主代理 terminal call 3.8→1.0（−74%）、token −30% | Terminus-4B 2605.03195 | `turn limit\|輪次上限\|repeat rate` exit=1 | subagent-strategy.md §拓撲規則 補：on-rails 子任務建議設輪次上限（參考 10 輪可配置）。**與 §Frontier #4 不同**（#4=frontier TEST 退化 gate；本=設計時輪次預算） |

### APPLY 前置 gate（2）

| ID | Finding | 接地 | grep 重驗 | 提案 |
|----|---------|------|----------|------|
| **F1** | 單一手動 harness 調校輪次會「退化」：Round C −4、D −5（低能力 self-evaluator + ACON cache 損壞 + 整合 bug）；oracle 81/89 手動不可達 | HARBOR 2604.20938 | `non-monotonic\|regress\|單調` exit=1 | APPLY 前置 gate 加「機率約束」：gate 在 **lower credible bound ≥ R_0−δ** 而非 point estimate → **結構性**拒絕 C-style 退化，非事後偵測。core.md 現有 `≥5pp→revert` 為 reactive，本為 proactive |
| **F10** | dual-split 接受 gate：`Δheld-in≥0 ∧ Δheld-out≥0 ∧ max(Δin,Δho)>0`；held-out 增益 MiniMax +21.4pp/Qwen +14.3pp/GLM +14.2pp | Self-Harness 2606.09498 | `held-out\|dual-split\|Δho` exit=1 | harness 演化 eval 切 held-in/held-out 雙分割，要求 held-out 不退化才接受。**core.md 單池 `≥5pp→revert` 會遮蔽 held-out sign-flip**（in-distribution 改善可能是 memorization） |

### TEST 階段（2，部分與 APPLY/RECORD 重疊）

| ID | Finding | 接地 | grep 重驗 | 提案 |
|----|---------|------|----------|------|
| **F2** | capability-floor 歸因：retry 只救 near-correct 輸出，跨不過能力天花板（8B git-diff 0/30 retry-recovered，targeted reason-code prompt 仍 0） | categorical-architecture 2605.12239 | `capability gap\|near-correct\|format discipline` exit=1 | TEST/RECORD：連續 retry 無進展時先做能力 vs harness 歸因；偵測 capability-floor 模式 → 停 retry、升模型檔位（接 self-escalate），不在固定檔位空轉。**補強既有「失敗≥3→self-escalate」的歸因依據** |
| **F12** | ETCLOVG 具名失敗分類法（Execution/Tool-interface/Context-memory/Lifecycle/Observability/Verification/Governance）；Terminal-Bench +50%/GAIA +42.3%/SWE-Bench +26.7%/AppWorld +15.2% | HarnessFix 2606.06324 | `ETCLOVG\|taxonomy` exit=1 | core.md:57「失敗歸因到層」是**意圖宣言但無具名層 checklist**。ETCLOVG 7 類 = 可機械填寫的分類格。**正交於** harness-meta-GOTCHAS 現有 4 行 meta-process 表（誰報告失敗/執行環境/數字正確/孤兒檔）→ 建議掛 GOTCHAS cross-link，非 core.md auto-load |

### RECORD 階段（1）

| ID | Finding | 接地 | grep 重驗 | 提案 |
|----|---------|------|----------|------|
| **F3**（較弱） | M-HIR：人工介入本身是診斷訊號 → 歸因到缺失的 harness 層（test-failure 解釋→觀測層；behavior verify→驗證層）；`assisted_verified_success ≠ autonomous_verified_success` | runtime-substrate 2605.13357 | `M-HIR\|assisted\|autonomous\|human intervention` exit=1 | RECORD：每次主對話需親自介入子任務 → 標記此介入歸因到缺失層，列演化候選；assisted-success 不可混記為完成。**core.md:57 涵蓋 failure→layer 歸因，但未涵蓋「人工協助本身是 gap 訊號」**。概念性、無 metric → 評級較弱 |

### Meta / 引用衛生（1）

| ID | Finding | grep 重驗 | 提案 |
|----|---------|----------|------|
| **F9** | `harness-loop.md:68` defer 條目把「CAR 診斷『單視角偏差』」歸因給 CAR 論文，但該詞**不在論文內** | CAR 論文 `single-perspective` exit=1（詞不存在）；harness-loop.md:68 確有此歸因 | defer **結論**仍正確（無量化對抗式 gap-finding 方法可掛；gap-vote 2/3 局部覆蓋足夠），但**歸因不精確** → :68 改述為「harness multi-perspective gap-finding 無量化方法論（CAR 未涵蓋此面向）」，避免把 workspace 詮釋當論文 finding。Lesson-2026-06-05-G 類（驗對應非只驗數字）。byte-delta ≈ 0 |

---

## un-defer 候選（1）→ 建議「維持 defer + 升觀察」

**Adaptive-Auto-Harness 2606.01770（EGL adaptive-stop）**：harness-loop.md §開放問題 defer 了「動態 convergence / stop 條件」，理由「直到出現量化方案」。本論文提供 **EGL threshold 0.05 / window 3 cycles**（adaptation-loss gap +37.5pp oracle-vs-naive，p=4.8×10⁻⁴）——**harness-stop 文獻首個量化門檻**，比 continual-harness（2605.09998，僅診斷 unsettled）前進一步。

**但不滿足 un-defer 門檻（量化 AND 可移植）**，兩個 disqualifier（Opus reverse-advisor 自審 + 主對話 grep 確認）：
1. **EGL 是 redirect 觸發非 stop**：低於門檻 → 切到 regime-specific git branch（0.7 router），非停止迭代。論文自承「does not explicitly define a universal convergence criterion」。markdown harness 無 branch-routing substrate 可掛 EGL。
2. **數字 domain-tuned**（prediction-market + CTF），非第一原理。

→ **建議**：維持 defer，但把 :67 註記從被動「defer until quantified」升為「量化候選已現（EGL 2606.01770），但 redirect-not-stop + domain-tuned + 無 branch substrate → 維持 defer，列主動觀察」。autoload-evolution 候選（byte-delta 小）。

---

## 刻意非 gap（1）— 邊界澄清

**RHO 2606.05922（self-preference 無 ground-truth）**：SWE-Bench Pro 59%→78% zero labels，靠 self-consistency（移除 −22pp）+ self-validation。**這是 workspace 刻意拒絕的路徑，非 gap**：

- RHO acceptance gate 把「是否接受 harness 更新」（本質為 **DECISION**）交 LLM 自評投票，撞 core.md:67「LLM 只做判斷、確定性代碼做決定」、core.md:63「非 LLM 自評」、harness-loop:78「self-preferential bias = 三大失敗模式之一」。
- workspace 多數任務有確定性 oracle（test/grep/healthcheck/byte cap）→ `unverified_success` 外部 oracle 前提成立，無需 self-preference 替代。
- RHO 有價值的子機制（多 rollout 找矛盾）**已被** adversarial V.evaluate + traces-first + gap-vote **以更嚴形式吸收**（要求 proposer-separated，非自評）。
- RHO resettable 前提 = workspace 不可逆 gate（DELETE/DROP/rm -rf/prod deploy）鏡像。
- **未來觀察點**：若 workspace 日後做大規模 zero-label benchmark 自進化（當前無），self-consistency 多 rollout 可作 gap-vote 擴展，但仍須守「accept 決定不經單模型自評」。

---

## 已吸收（ABSORBED，無需動作）

external>self-feedback（≡core.md:63）｜CAR 三維（≡opus-pilot M3 + multi-mode-agent ceiling）｜HarnessCard（≡harness-design.md:26+148）｜harness-sensitivity 歸因（≡harness-loop §6 + observability baseline）｜model-parametricity（≡multi-mode router）｜output-compression（≡subagent-strategy:17）｜SLM-substitution（≡subagent-strategy:30 model 選擇）｜regression-gate（≡unverified_success）｜same-model-self-improvement（≡proposer/verifier 分離）。

## 弱接地（DEFER，不入 loop）

certificate-preservation（論文自承無行為性解方）｜static-snapshot（純診斷）｜entropy-auditor（無量化偵測法）｜continual transferable-unit（directional 無 effect size + 與「不沿用 baseline」域混淆）｜HTIR（系統內部資料結構，無 pipeline）｜Docker-rollout（研究基礎設施）｜weight-update co-evolution（workspace 無 fine-tune pipeline）｜what-makes-a-harness iff 定義（taxonomic，T1-T4 已語意覆蓋）。

---

## 新收錄論文（6 篇，→ `research/papers/`，全 YAML 驗證）

| arXiv | 標題 | 日期 | 關鍵數字 |
|-------|------|------|---------|
| 2606.09498 | Self-Harness: Harnesses That Improve Themselves | 2026-06-08 | held-out +21.4/+14.3/+14.2pp；dual-split gate |
| 2606.05922 | Retrospective Harness Optimization (RHO) | 2026-06-04 | SWE-Bench Pro 59%→78% zero labels |
| 2606.06324 | HarnessFix: Diagnosing & Repairing Harness Flaws | 2026-06-04 | Terminal-Bench +50%/GAIA +42.3%/SWE-Bench +26.7%；ETCLOVG |
| 2606.01770 | Adaptive Auto-Harness（open-ended streams） | 2026-06-01 | EGL 0.05/3cyc；adaptation gap +37.5pp p=4.8e-4 |
| 2606.10106 | What makes a harness a harness | 2026-06-08 | iff T1-T4（definitional，無量化） |
| 2605.27276 | SIA: Self Improving AI（harness+weight） | 2026-05-26 | LawBench +20.1pp；TriMul 91.9% runtime↓ |

**scanned-not-fetched（無 silent cap）**：Harness-1 2606.02373（RL 20B search agent）、CAAF 2604.17025（cybernetic determinism）— RL/控制論域，workspace（Claude API，無 RL/fine-tune）不適用，低 yield 未 fetch。

---

## autoload-evolution 提案彙整（**未套用**；交使用者走 gated loop）

> **byte 現況 18,243/19,000，餘 757B**。auto-load cap 上調須實證計劃書背書，不為塞單一規則反推湊 byte（core.md §Framework Integrity）。多數提案須先壓 byte 或下沉 refs。

**優先序（依接地強度 × 可操作性 × byte 成本）：**

1. **P1 — F9 引用衛生修正**（harness-loop.md:68 改述）：byte-delta≈0，零風險，純正確性。**最低成本最該先做**。
2. **P1 — F1 lower-bound gate**（harness-loop.md §Frontier APPLY 條目）：接地最強（量化退化數字），proactive 補 reactive `≥5pp→revert`。~1 行。
3. **P2 — F10 dual-split gate**：與 F1 同屬 APPLY/TEST，可合併為一條「機率約束 + held-out 雙驗」（≤1 規則/cycle 限制下擇一或合併）。
4. **P2 — EGL 觀察升級**（harness-loop.md:67）：byte-delta 小，把 defer 註記升「觀察」。
5. **P3 — F12 ETCLOVG**：建議掛 `harness-meta-GOTCHAS.md`（on-demand），**非 core.md auto-load**（7 類列舉佔 byte，且正交於現有 4 行表）→ 不耗 auto-load 預算。
6. **P3 — F8 turn-limit**：掛 subagent-strategy.md（auto-load 六源之一，須計 byte）或下沉 refs。
7. **觀察/未排程 — F2/F3/F4/F5/F6/F7/F11**：接地成立但部分概念性（F3）或屬 skill/OBSERVE 細節，建議下沉 refs 或 skill GOTCHAS，避免 auto-load 膨脹。

**gated loop 紀律提醒**（core.md §Framework Integrity + prompt-lifecycle.md）：每 cycle ≤1 規則、≤50 行 diff、改動附 Falsifiable Prediction + eval 條件；eval 回歸 ≥5pp → `git revert`；feature branch + PR（prompt registry staged deployment）。

---

## 迴圈執行紀錄（The Loop RECORD）

| 輪 | 動作 | 產出 |
|----|------|------|
| iter-1 | OBSERVE baseline + IDENTIFY（主對話） | F1（HARBOR 非單調退化） |
| iter-2 | 4-way fan-out（2 Opus/ceiling + 2 Sonnet/quality） | F2-F7（6 gap，全主對話 grep 重驗） |
| iter-3 | 4-way fan-out（2 Opus + 1 Sonnet + 1 researcher scout） | F8（turn-limit）+ F9（CAR 引用衛生）+ 8 篇新論文發現 |
| fetch | 4 researcher 並行 fetch HIGH 論文 | 4 篇入 research/papers（主對話 YAML 驗證） |
| iter-4 | 4-way fan-out on 新論文 | F10-F12 + EGL watch + RHO 非 gap（Opus reverse-advisor） |
| iter-5 | 2 multi-mode-agent FETCH+ASSESS（MED） | **dry round**（0 operable gap）→ 收斂；2 篇 worktree 產物 recover 回主 tree |

**收斂判準**：iter-5 MED 論文 dry round（守 harness-loop.md「強條件→獨立 loop」；非固定 K）。HIGH 論文已挖盡，MED 低 yield，RL/控制論域不適用 → 宣告收斂。

---

## 附錄：有效性對抗檢查（loop-2，2026-06-14 PM）— 12 gap → 3 HIGH_VALUE

> 第二輪 `/loop` 換鏡頭：前 5 輪 grep 確認 12 gap「未掛載」，但**未做 harness-loop.md APPLY 前置 gate 第 2 點的有效性檢查**——「此規則若早存在，能否擋下一個**真實發生過**的錯誤？否 → 疑 false positive → defer」。本附錄補做此檢查（3-way Opus/ceiling fan-out，proposer-separated 對抗審查，對照 21 條 MEMORY lesson 為真實失敗 corpus；3 HIGH_VALUE 全主對話 grep 重驗）。

**結論：12 gap 中只有 3 通過有效性檢查（有 workspace 真實失敗錨點）。其餘 9 為論文驅動非失敗驅動 → defer/redundant。**

### HIGH_VALUE（3，有 workspace 鐵證，建議進 autoload-evolution）

| ID | 真實 workspace 失敗錨點 | 主對話重驗 | byte 成本 |
|----|----------------------|----------|----------|
| **F9** | `harness-loop.md:68` 把「單視角偏差」誤植給 CAR 論文——CAR 全文出現次數 = **0**。live on-demand 檔既存引用錯誤，前 loop 已獨立記為 Lesson 2026-06-14-B（可重現非單次幻覺） | `sed :68` 顯示誤植句；CAR grep count=0 | ≈0（改述「gap-vote 動機」非「CAR 診斷」） |
| **F7** | **Lesson 2026-06-13-B 即字面實例**：stop hook 只寫 cost-log（write>0），從未重產衍生 usage-report.json（read 端 stale）→ Portal 永遠看舊，靠手動補（commit f6d37fb2）才發現。`healthcheck.sh` 無任何衍生檔新鮮度/讀寫不對稱遙測 | healthcheck grep `usage-report\|read-write\|衍生檔 fresh` exit=1（確認缺） | 改 healthcheck 腳本，**非 auto-load**（零預算） |
| **F3** | MEMORY **6 起 advisor-rescue**（2026-06-06-A/07-I/07-J/07-L + Lesson D/E），全記為「內容更正」，**0 起**把「需人工介入」本身歸因為缺失 harness 層。M-HIR 規則會在每次 rescue 後強制標 assisted-flag，使「其實無法 autonomous 完成」可量測 | `grep -c 'advisor 攔'`=6；`grep -c autonomous\|assisted`=0 | RECORD ~1 行或下沉 refs |

### REDUNDANT（2，引用論文已掛載別處）

- **F2**（capability-floor）：已在 `harness-meta-GOTCHAS:139-141`「能力弔詭」用同篇 2605.12239 接地 + `subagent-strategy:30` self-escalate（非重試）已編碼停-retry-升檔位。
- **F12**（ETCLOVG）：`harness-meta-GOTCHAS:126-133` 已有具名 4 層歸因表；ETCLOVG 的 runtime 軸（Tool/Lifecycle/Context）在 workspace（prompt-harness 非 agent-runtime）無真實失敗對應。F12 自己的提案也說「掛 GOTCHAS 非 core.md」= 承認 redundant。

### ACADEMIC_DEFER（7，論文洞見有效但 workspace 0 真實失敗）

F1（11 eval cycle 從未退化、git log 0 revert）｜F10（無 held-out 基礎設施、5-task eval 無 memorization 暴露面）｜F4/F5（skill-evolution 從未跑 learned-skill 選型/自動品質驗收，無失敗 substrate）｜F8（grep 0 輪次失控；fan-out≤4 + child 不 self-retry 已從拓撲層阻斷）｜F6（cross-session memory 存在但從未在 benchmark 測過混合值傷害，confound grep exit=1）｜F11（**reverse-advisor 推翻**：MEMORY:96「再應驗 2026-06-04-B」反證扁平 lesson 能跨 session 召回，三元組分群是 organizational 升級非防真實失敗）。

### 方法論收穫（meta-lesson）

> **grep-confirmed-absent ≠ failure-validated**。前 loop 的 12 gap 都通過「harness-loop.md 沒寫」的 grep 檢查，但只有 3 通過「擋過真實失敗嗎」的有效性檢查。**有效性檢查（APPLY-gate #2）是把論文 gap 收斂為可掛載提案的真正關卡**，不能略過直接從「論文有講 + 我們沒寫」跳到「該掛載」——那正是 self-preferential bias（為了讓 gap 存活硬編假想失敗）。3 個 HIGH_VALUE 全部小/零 byte，且 F7（healthcheck 腳本）與 F12（GOTCHAS）根本不耗 auto-load 預算。

**修正後的 autoload-evolution 優先序（取代正文 §提案彙整的純接地排序）**：
1. **F9**（byte≈0，純正確性，修既存錯誤）— 最該先做
2. **F7**（healthcheck 腳本，零 auto-load 預算，有鐵證）
3. **F3**（RECORD，~1 行；assisted-flag 紀律有 6 起真實 rescue 背書）
4. 其餘 9 → 不掛載（defer/redundant），列觀察。

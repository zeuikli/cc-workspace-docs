---
title: "Karpathy × Mnilax 12-Rule Canon — Universalization Research"
date: 2026-06-04
status: complete
baseline: ".claude/refs/karpathy-mnilax-best-solution.md (AB4.0, 4-round adversarial refinement)"
branch: feature/karpathy-mnilax-universalization
deliverable_siblings: ["2026-06-04-12-rule-universal-ruleset.md (the portable ruleset)", "2026-06-04-12-rule-canon-patch-proposal.md (auto-load patch proposal, APPLY-gated)"]
sources: ["Karpathy CLAUDE.md (R1–R4): https://raw.githubusercontent.com/multica-ai/andrej-karpathy-skills/refs/heads/main/CLAUDE.md (fetched 2026-06-04, verbatim)", "Mnilax thread (R5–R12 + methodology): https://x.com/Mnilax/status/2053116311132155938 (X 402-paywalled; primary text recovered via fxtwitter API 2026-06-04)", "8 papers in research/papers/ (arxiv IDs inline; load-bearing numbers grep-verified against primary .md)"]
type: research-report
---

# Karpathy × Mnilax 12-Rule Canon — Universalization Research

## 0. 框架誠實聲明（讀本報告前必讀）

本報告把 12 條「AI coding **assistant** 紀律準則」對應到 AI agent **論文**證據。**這個對應是「平行失敗模式」（parallel failure-mode analogy），不是身分等同（identity）。**

- 大多數論文研究的是**自主 / 多 agent 架構**（MAST、SWE-agent、Confucius、ACE…）。
- 12 條規則約束的是**單一 assistant 與人協作時的紀律**。
- 連結成立的理由：**架構層的失敗模式，與紀律層要防止的失敗，是同一個根因在不同層級的投影**。例如 MAST 的「premature termination」（agent 架構層）= R12 的「未驗證就宣告完成」（assistant 紀律層）。

因此本報告**不主張論文「證明了」某條規則**，而是主張：**論文獨立觀測到的失敗模式，與該規則設計要防的失敗，是同一現象。** 這讓 12 條規則從「個人最佳實踐」升級為「有實證失敗模式背書的紀律」。

每條對應標注信度三級：
- **Direct**：論文直接描述同一個失敗 / 機制（同層或近乎同層）。
- **Analogous**：架構層失敗與紀律層失敗是同根因的不同投影（本報告主力類型）。
- **Inferential**：需一步以上推論才能連上；標出供讀者自行判斷，不當證據用。

---

## 1. 任務與基線

**任務**：對 Karpathy R1–R4 + Mnilax R5–R12 做深入研究 → 蒐集更多案例 → 歸納 → 優化改寫成「更通用版本」（stack-agnostic + harness-agnostic）。

**基線**：workspace 已有 `karpathy-mnilax-best-solution.md`（AB4.0，417 行，4 輪對抗精煉）。它**已完成**：每條的失敗模式陳述、執行檢查表、情境速查表。它的**兩個缺口**正是本研究的價值點：

| 基線缺口 | 本研究補強 |
|---|---|
| **案例來源 = 38 篇部落格 + GitHub 軼事** | 換成 8 篇論文的**可溯源實證**（grep 親驗數字） |
| **內容 workspace 耦合**（`在本 workspace 的實現位置`、core.md 路徑、`/compact`、`advisor()`、4000/30000 token 硬數字） | 改寫成 **stack/harness-agnostic** 通用版（見 sibling ruleset 檔） |

---

## 2. 源頭校驗（primary-source discipline）

| 宣稱 | 來源 | 校驗結果 |
|---|---|---|
| R1–R4 原文 | Karpathy CLAUDE.md | ✅ WebFetch 親取，與任務 prompt 文字一致 |
| R5–R12 原文 | Mnilax thread | ✅ 文字已在任務 prompt；thread 本體 402 paywall |
| **「50 tasks × 30 codebases × 6 weeks」** | Mnilax 文章 | ✅ fxtwitter 親取："I tracked the same set of 50 representative tasks across 30 codebases for 6 weeks" |
| **41% → 3% mistake rate** | Mnilax 文章 | ✅ 同上回報；但**單一作者自報、無公開資料集**→ 信度 MEDIUM（無法第三方複現） |
| **14 條後 compliance 76%→52%** | Mnilax 文章 | ✅ fxtwitter 親取。**這是 canon 固定 12 條的設計依據**——超過 ~14 條規則，遵從率斷崖。 |

> ⚠️ **41%→3% 與 76%→52% 是作者自報實驗，非同儕審查資料。** 引用時必須標「作者自報」，不可當硬證據。這正是 AB4.0 lineage 沒講清楚的地方。

---

## 3. 論文證據對應表（已過對抗 mapping 審查）

> mapping 經 advisor 對抗審查，修正 3 處過度延伸：
> ① MAST「Fail to ask for clarification」原誤掛 R7 → **改掛 R1**（是「不清楚就問」非「兩個矛盾模式」）；
> ② MAST「Reasoning-action mismatch」原掛 R5 → **降為 Inferential / 不當主證據**（言行不一不等於「LLM 做確定性工作」）；
> ③ Multiagent-debate 收斂原掛 R10 → **改掛 R9**（是交叉驗證非狀態 checkpoint）。

| 規則 | 論文證據（verbatim 已 grep 親驗） | arXiv | 信度 |
|---|---|---|---|
| **R1** Think Before Coding | MAST **FM「Fail to ask for clarification」**：*"Inability to request additional information when faced with unclear or incomplete data, potentially resulting in incorrect actions."* | 2503.13657 | **Analogous** |
| **R2** Simplicity First | MAST：*"failures… often stem from system design issues, not just LLM limitations… require more than superficial fixes"* — 加 agent / 加複雜度不解決結構缺陷。MultiAgentBench：協調架構 > 模型大小（.md 摘要，非 verbatim）。 | 2503.13657 / 2503.01935 | Analogous / **Inferential** |
| **R3** Surgical Changes | SWE-agent **「Cascading Failed Edits = 23.4%」**（SWE-bench Lite, n=248 失敗分布最大宗）：過寬 / 缺理解的編輯引發連鎖失敗。 | 2405.15793 | **Analogous** |
| **R4** Goal-Driven Execution | Reflexion **91% pass@1 (HumanEval) vs GPT-4 80%**——loop-until-`outcome.success`。SWE-agent **「fast success, slow failure」**（resolved 中位 12 步/$1.21；unresolved 均 21 步/$2.52，"increasing budget unlikely to improve"）。Confucius **「If tests fail, the agent enters a debugging sub-loop」**（驗證是強制 pipeline stage）。 | 2303.11366 / 2405.15793 / 2512.10398 | **Direct** |
| **R5** Judgment vs Deterministic | Dynamic Cheatsheet **Game of 24：10%→99%**（LLM 判斷「該用 Python 暴力解」，確定性 code 做計算）；**Math Balancer：~50%→98–100%**（"baselines stagnated around 50%"）。 | 2504.07952 | **Direct** |
| **R6** Token Budget | ACE **「context collapse」**（*"iterative rewriting erodes details… sharp performance declines"*）+ **delta updates 為必要**（ablation：回退 full-rewrite → collapse）。DC **「context ballooning」**。Confucius：關 context mgmt → **Resolve@1 −6.6pp**。 | 2510.04618 / 2504.07952 / 2512.10398 | **Direct** |
| **R7** Surface Conflicts | MAST **「Inter-Agent Misalignment」**整類（目標不一致、資訊傳遞失真）+ *"coordinator 指令需 structured handoff + confirmation, 不能依賴 agent 自行解讀"*——把矛盾平均掉 = 此類失敗。 | 2503.13657 | **Analogous** |
| **R8** Read Before Write | SWE-agent **「Early Phase (T1–4)：find_file / search_dir / 寫 reproduction」**先定位再改 + **Zoom-in（dir→file→line）**。Confucius **Retrieval + Localization Phase 先於 Implementation Phase**。失敗代價：首個失敗編輯後恢復率 **90.5%→57.2%**。 | 2405.15793 / 2512.10398 | **Direct** |
| **R9** Tests Verify Intent | SWE-agent **「Reproduction-first：(create, edit, python)」**先建可重現再修。SWE-bench-Pro **「thoroughly vetted test suites」**（人工驗測試品質）。Reflexion 明分**「explicit test cases vs LLM self-eval」**——91% 成績用前者。Multiagent-debate：交叉驗證提升事實正確性。 | 2405.15793 / 2509.16941 / 2303.11366 / 2305.14325 | **Direct** |
| **R10** Checkpoint | MAST **「Loss of conversation history」**（*"Unexpected context truncation… reverting to an antecedent conversational state"*）+ **「Step repetition」**。Confucius **Architect structured summary**（保留 task spec + 決策 + file paths + 最近 N 訊息）= checkpoint 機械實作；persistent notes 省 **11k token / 3 turns，+1.4pp**。 | 2503.13657 / 2512.10398 | **Direct** |
| **R11** Convention First | ACE **「evolving playbooks」**（累積既有慣例為權威起點）。DC **「repeatedly re-discovering… same solutions and mistakes」**= 不讀既有慣例的代價；Game of 24 重用既存解 **10%→99%**。 | 2510.04618 / 2504.07952 | **Analogous** |
| **R12** Fail Loud | MAST **「Premature termination」**（*"Ending… before objectives have been met… incomplete or incorrect outcomes"*）+ **「No or incomplete verification」**（*"allowing errors… to propagate undetected"*）+ **「Incorrect verification」**。整個 **「Task Verification」類別是 MAST 最難自動修復**——對應 R12「幻覺式自我報告完成」。 | 2503.13657 | **Direct** |

**降級 / 剔除（誠實標注）**：
- MAST **FM-2.6「Reasoning-action mismatch」**：原掛 R5，**剔除為主證據**——言行不一 ≠「用 LLM 做確定性工作」，無乾淨對應規則。
- **41%→3% / 76%→52%**：作者自報，MEDIUM。
- MultiAgentBench 協調 > 模型：**Inferential**，.md 為摘要非 verbatim（PDF 未讀）。

---

## 4. MAST 14 失敗模式 → 12 規則完整覆蓋圖

MAST 是目前最完整的 agent 失敗分類（150 traces, κ=0.88 **inter-annotator agreement**，NeurIPS 2025 D&B）。14 模式對 12 規則的覆蓋驗證了 canon 的**完整性**：

| MAST 三大類 | 失敗模式（verbatim 縮寫） | 對應規則 |
|---|---|---|
| **(i) Specification Issues** | Disobey task spec | R1 / R4 |
| | Disobey role spec | (agent-only，assistant 無對應) |
| | Step repetition | R10 |
| | Loss of conversation history | R10 |
| | Unaware of termination conditions | R12 |
| **(ii) Inter-Agent Misalignment** | Conversation reset | R10 |
| | Fail to ask for clarification | **R1** |
| | Task derailment | R4 |
| | Information withholding | R12（不藏資訊 = fail loud） |
| | Ignored other agent's input | R7 / R8 |
| | Reasoning-action mismatch | （無乾淨對應，剔除） |
| **(iii) Task Verification** | Premature termination | R12 |
| | No / incomplete verification | R4 / R9 / R12 |
| | Incorrect verification | R9 |

**結論**：14 模式中 **12 個有規則覆蓋，2 個無對應**：
- 「**Disobey role spec**」——多 agent 角色專屬，單 assistant 場景不存在。
- 「**Reasoning-action mismatch**」——言行不一無乾淨紀律對應，已於 §3 剔除（不勉強掛 R5）。

兩個無對應模式都是「多 agent 架構特有」或「無誠實對應」，**非 canon 漏防**。扣除 agent-only 的 role-spec，**canon 對 single-assistant 失敗模式的覆蓋是完整的（13/13，唯一缺口 reasoning-action-mismatch 屬無乾淨對應而非漏防）。**

---

## 5. 通用化分析（universalization）— 兩軸

### 5a. Stack-agnostic（跨語言/框架）
12 條本來就大致 stack 中立。唯一殘留耦合是案例（Python/JS 範例）。通用版改用**語言中立的失敗描述**（見 ruleset 檔）。

### 5b. Harness-agnostic（跨 AI coding 工具）— 真正的價值點
AB4.0 深度耦合 Claude Code harness。通用化 = 抽掉專屬機制，只留**任何 AI coding agent / 團隊都能落地的機制**：

| 耦合（AB4.0） | 通用化（任何 harness） |
|---|---|
| `/compact 保留…` | "summarize context & restart fresh thread" |
| `advisor()` 看完整 transcript | "independent reviewer / second model reviews full transcript" |
| `core.md` / hook / `settings.json` 路徑 | "your project's agent-config file" |
| `bash scripts/healthcheck.sh` | "the project's defined verification command" |
| **4,000 / 30,000 token 硬數字** | **原則化**：「設明確的 per-task 與 per-session 預算；逼近時 surface 而非硬撐」——**不把特定數字當普世常數** |
| `git stash → hotfix/p0-*` 6 步 | "isolate the security fix on its own branch; don't bury it in the feature commit" |
| `AskUserQuestion` 工具 | "present options to the human; don't silently pick" |

> R6 是「通用化」最大陷阱：4000/30000 是 workspace 特定值。通用版只保留**原則**（設預算 + breach 要 surface），數字交給各團隊依模型與成本自訂。

---

## 6. 對 canon 的回饋（→ 見 patch-proposal 檔）

研究發現**值得回灌 auto-load**的真實 gap：

1. **R12 / MAST「Premature termination」+「Information withholding」**：canon R12 已有「未驗證不宣告完成」，但缺「**不藏部分失敗資訊**」這層（MAST 獨立觀測到的失敗）。
2. **R6 通用化措辭**：core.md 寫死 4000/30000。可加一句「數字為本 workspace 校準值，跨 harness 移植時原則 > 數字」（防止他人誤把數字當普世）。
3. **methodology 信度標注**：refs/karpathy-mnilax-best-solution.md lineage 寫「41%→3%」未標「作者自報」→ 補一句信度註記（防 MEMORY SELF-ROUTE 式誤溯源重演）。

**全部僅止於 proposal，APPLY 留待 gated session**（auto-load 18,455/19,000，餘裕 545 B）。詳見 `2026-06-04-12-rule-canon-patch-proposal.md`。

---

## 7. 規則演化 Lineage（更新版）

```
Karpathy Jan 2026 thread（3 失敗模式觀察）
  → Forrest Chang / multica-ai 4-rule distillation（R1–R4，本研究 WebFetch 親驗）
      → Mnilax May 2026 8-rule extension（R5–R12）
           作者自報：50 tasks × 30 codebases × 6 weeks；41%→3%；14 條後 76%→52%
  → autoresearch:reason 4 輪對抗精煉 → AB4.0（workspace 耦合，case=部落格）
  → 本研究 2026-06-04：論文實證接地（8 篇，grep 親驗）+ harness/stack-agnostic 通用化
       + 對抗 mapping 審查（修正 3 處過度延伸）+ MAST 14 模式完整性驗證
```

## 8. 參考論文（本研究實際引用 + grep 親驗）

| arXiv | 論文 | 親驗數字 |
|---|---|---|
| 2503.13657 | MAST — Why Multi-Agent LLM Systems Fail | κ=0.88 (inter-annotator)；14 模式 / 3 類；41–86.7% failure |
| 2405.15793 | SWE-agent — Agent-Computer Interfaces | cascade 23.4%；recovery 90.5%→57.2%；fast-success/slow-failure |
| 2512.10398 | Confucius Code Agent | context-mgmt −6.6pp；notes 11k tok/3turn/+1.4pp；SOTA 54.3% |
| 2303.11366 | Reflexion | 91% vs GPT-4 80% pass@1 (HumanEval) |
| 2504.07952 | Dynamic Cheatsheet | Game of 24 10%→99%；balancer ~50%→98–100%；context ballooning |
| 2510.04618 | Agentic Context Engineering (ACE) | context collapse；KV cache 91.8%；−82.6% cost；+10.6% agent / +14.8% no-label |
| 2509.16941 | SWE-bench Pro | long-horizon (hours–days)；vetted test suites |
| 2305.14325 | Multiagent Debate | 交叉驗證提升 factuality |

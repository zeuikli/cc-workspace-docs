# Session Insights — 評估即交付：harness 平台期的「完整評估再執行」紀律

> **日期**: 2026-06-20
> **來源**: Session（claude/anthropic-claude-code-expertise-5myrpg branch；PR #692 squash→main 7804201）
> **類型**: Session Learning Report（meta — 過程模式，非研究內容；研究內容見本 session 5 份報告）
> **Topic**: Evaluation-as-Deliverable · 功能級 Gap 驗證 · 構念對齊 · 反向 anti-hack · 平台期信號

---

## 0. TL;DR

本 session 從「分析 Anthropic 400K 研究」起，演變為**對 workspace 候選改動的連續嚴格評估**。最反直覺的結果：**多數產出是「不做」的決定**——3 輪正式評估（TIER B / 4 缺口 / autoload 雙候選）**全數收斂到「既有 harness 已覆蓋」或「前提不成立」**，淨落地僅 3 個小項。

核心 meta-insight：**在高成熟度 harness 上，「完整評估」本身就是交付物**——它擋下的冗餘/有害/投機變更，價值高於勉強擠出的新規則。本報告萃取此過程的 **5 個可複用模式** + **4 條 Lesson**。

---

## 1. 核心任務與結果（簡述）

| 階段 | 產出 | 落地 |
|------|------|------|
| 研究 | 5 份深度報告（400K expertise / 週報0618 / HarnessX-DecentMem / TIER B / 覆蓋稽核）| — |
| 執行 | TIER A 3 小項（grid DeepSWE/Fable-G7、fable access GOTCHA、HarnessX 九維 lens）| ✅ |
| 評估擋下 | TIER B(3) + 4 缺口 + autoload(2) | **全 DEFER/DROP/DISCARD** |
| 交付 | PR #692 squash→main；healthcheck 126/0 FAIL | ✅ merged |

**量化軌跡**：候選改動 **12 項評估 → 3 落地（25%）**；其餘 9 項全經 grep 接地 + fable-pilot 反向審閱後**正確擋下**。

---

## 2. 可複用模式（本 session 的真正資產）

### 2.1 評估即交付（Evaluation-as-Deliverable）
3 輪評估連續 0 執行**不是失敗，是高成熟度信號**。每輪評估擋下的是：
- TIER B：對既有功能**重複建設**（B2 harness-loop / B3 失敗分類）
- 4 缺口：**有害**（GAP-1 強制 haiku 癱瘓委派）+ **證偽**（GAP-3 routine 不用 Fable）
- autoload：**誤接地**（A）+ **goodhart**（B）

→ 在平台期 harness 上，「不做」需要與「做」同等的證據鏈。把評估寫成 report-only 報告（本 session 5 份中 3 份是評估）= 讓「不做」可追溯、可複查。

### 2.2 功能級 vs 字串級 Gap 驗證（Lesson-F，本 session 最高頻陷阱）
subagent 稽核反覆把「字串不存在」誤報為「功能缺口」：

| 假缺口 | 字串級判定 | 功能級真相 |
|--------|-----------|-----------|
| B3 ETCLOVG | `grep ETCLOVG`=空 → NOT-DONE | 既有 4 層失敗歸因已覆蓋 6/7 類 |
| B2 harness-loop F1 | 比對到 reactive gate | APPLY 行已有 proactive 檢查 |
| GAP-1 subagent 防護 | `deny` 無此規則 | 2026-06-07 已裁決為 user-tradeoff + 遞迴 harness 不可能 |
| GAP-3 routine fallback | 無 fallback 宣告 | routine 全用 Sonnet 不用 Fable，無 deadlock |

→ **協議**：subagent 提報的 gap，主對話必須升級為功能級重驗——「既有結構是否已覆蓋此**功能**」+「此前提是否在歷史報告**已裁決**」，不止 grep 關鍵字。

### 2.3 構念對齊：論文接地前必驗「量的是同一件事嗎」（Lesson-H）
autoload 候選 A 想把 400K 研究的 expertise 洞見落地為「agent 自評自身領域專業度」。但研究原文量的是 **USER 專業度（Claude 從 transcript 觀察）**——**偷換構念**：研究權威**不背書**任意衍生主張。

→ 論文洞見入 auto-load 前的閘門：① 研究量的構念 = 我要落地的構念？② 轉移條件成立？（呼應 HarnessX/DecentMem 評估的同一紀律）

### 2.4 分類系統增殖反模式
本 session 險些並存**三套** harness 分類：HMF 7D（元件類型，既有）/ HarnessX 9D（行為功能，新加）/ ETCLOVG（失敗類別，提案）。
- HarnessX 9D **正確落地**（標 `TODO(conflict)` 與 HMF 7D 區隔為 cross-check lens，不混用）
- ETCLOVG **正確擋下**（與既有 4 層失敗歸因重疊）

→ 新分類框架入庫前問：「與既有 N 套分類是否同軸？」同軸 = 增殖（DROP）；正交 = 須顯式標界線防混用。

### 2.5 反向 anti-hack（fable-pilot 的對稱用法）
本 session 把 fable-pilot 的 anti-hack **反向**使用：常規問「是否假裝完成」；本 session 問「**是否假裝『已存在』以逃避該做的工作**」。每個 DROP/DISCARD 裁決都經此反向審——驗證「既有覆蓋」非省事藉口（特地找被連帶棄掉的 kernel，結果皆已被既有條文更佳覆蓋）。

→ 驗證紀律是對稱的：false-done 與 false-already-exists 都是 hack，都需 rejected-claims ledger。

---

## 3. 平台期信號與行動建議

**信號**：3 輪評估連續收斂到「既有已覆蓋」+ EVOLUTION-QUEUE 清空（0 pending）+ healthcheck 長期 126/0 FAIL。

**判讀**：workspace harness 處於**高成熟度平台期**——真正待落地的有價值改動已清空。

**行動建議**：
- ✅ **等新研究訊號**（新 daily-research / 新論文）再觸發 cycle，不為動而動製造候選（呼應 RATCHET 2026-05-31i「不為 byte slot 製造規則」）
- ✅ 候選評估維持**反向 anti-hack** + 功能級重驗 + 構念對齊三閘
- ⚠️ 警惕「agentic laziness 的反面」——**過度產出候選**也是一種 drift（為證明價值而擠規則）

---

## 4. Lessons 彙整（本 session 入 MEMORY）

| Lesson | 內容 | 防範 |
|--------|------|------|
| **E** | 落地前必 grep 既有同類框架（HarnessX 險與 HMF 7D 衝突）| 「缺口」宣稱二次驗證既有結構 |
| **F** | subagent「NOT-DONE」是字串級；值得做須功能級重驗 | 既有結構是否覆蓋該**功能** |
| **G** | subagent 的「新缺口」可能是**既有已裁決項**（GAP-1=2026-06-07）| 親驗須 grep 歷史報告決議 |
| **H** | 論文洞見落地前驗**構念對齊**（400K 量 USER 非 agent 自評）| 研究權威不背書任意衍生 |

---

## 5. 與既有 harness 紀律的關係

本 session 的模式**不是新規則**，而是既有紀律的**密集應用實例**：
- `unverified_success` 閘門 → 反向擴展為 false-already-exists 也需親驗
- core.md「不為未來可能鋪設」→ 平台期「不為動而動製造候選」
- PROPOSE「Rule of 3」→ 評估候選時的 anti-over-engineering 主軸

→ 故本報告**不提議新 auto-load 規則**（自身即遵守平台期紀律）；價值在**記錄可複用的評估過程**供下次同類 cycle 注入。

---

_方法：本報告為 session meta-反思（RECORD 階段產物）。所有引用的裁決/數字可溯本 session 5 份報告 + MEMORY Lesson E/F/G/H + PR #692。不提議規則變更。_

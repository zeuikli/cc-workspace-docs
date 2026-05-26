---
title: "Session Insights — 對稱懷疑原則與計劃書制訂紀律"
date: 2026-06-07
related: research/reports/2026-06-07-deep-practices-v2-execution-plan.md
session_topic: deep-practices-v2 執行計劃書制訂
type: session-insights
---

# Session Insights — 對稱懷疑原則

> 本 session 從「為研究報告制訂執行計劃書」中萃取的可複用方法論。核心是一條跨任務的判斷紀律：**對外部建議的懷疑必須對稱**。

---

## 核心 Insight：對稱懷疑（Symmetric Skepticism）

### 問題

制訂執行計劃書時，最自然的失敗模式是把報告的行動清單**逐條當待辦鋪開**。workspace 既有紀律已能擋住一半——對「幻覺 key」（技術上不存在的建議，如 `autoCompactAt`/`tokenBudget`）有警覺。但這個警覺是**不對稱**的：只防「技術不存在」，不防「技術存在但撞既有設計」。

### 原則

> 對外部建議的懷疑要對稱地套用到兩個方向：
> 1. **技術不存在**（幻覺 key）-> 剔除
> 2. **技術有效但撞既有刻意設計**（tradeoff 非 fix）-> 不自動執行，AskUserQuestion 待決

第二類最危險，因為它「看起來是對的」會通過 grep 驗證。本 session 抓到三個：

| 建議 | 表面 | 實際 |
|------|------|------|
| skill body 壓到 250-450 words | 子代理機械判「25/27 超標」 | pilot/hub 多命令 skill 不適用單指令上限；壓縮 = 砍真實操作內容 = 違反「不破壞 working」 |
| P0-4 釘 subagent model=Sonnet | 「防靜默降級 Haiku」 | 破壞 subagent-strategy「0–1檔 Haiku」省錢路由 = tradeoff 非 fix |
| `CLAUDE_AUTOCOMPACT_PCT_OVERRIDE` | 真實 env（非幻覺） | MEMORY 標「has bug」-> 真實 ≠ 該用 |

**判準**：一條建議若與 ADR / 既有刻意設計衝突，它是「決策」不是「修補」-> 交使用者，不靜默選。這與 core.md「浮現矛盾不靜默選擇」同源，但延伸到「外部報告 vs 既有設計」的矛盾。

---

## Insight 2：子代理 verdict 的「詮釋層」誤判

`unverified_success` 閘門過去聚焦「數字是否屬實」。本 session 揭露更隱蔽的一層：**數字屬實但詮釋錯**。

- skill 字數 25/27 超標：grep 屬實，但「超標 -> 該壓縮」的詮釋錯（忽略 pilot/hub 是多命令 skill）。
- `memory-sync.sh:44 exit 1`：子代理判「誤用應改 exit 0」，但親讀上下文發現是「sync 失敗不阻斷 session」的正確語義（exit 2 才 block）。

**教訓**：機械 grep 重驗能抓「數字幻覺」，抓不到「詮釋幻覺」。詮釋幻覺需主對話**親讀上下文 + 領域知識**判斷，不能只驗數字成員資格。-> 親驗範圍應含「該數字的詮釋是否成立」，非只「該數字是否存在」。

---

## Insight 3：「試跑」前先驗功能的執行模型

Q2 要求「試跑 Agent Teams 評估」。對稱懷疑先驗 flag 真偽（確認 `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS` 是真實 flag，非幻覺）——但官方文件揭露更關鍵的**執行模型約束**：

> Agent Teams 是互動式 CLI session 級編排（lead spawn teammates via tmux/pane）。官方明載「No nested teams：teammates cannot spawn their own teams」。當前 runtime 是被 spawn 的 agent -> **無法在此 session 內程式化試跑**。

**教訓**：「試跑某功能」前，除了驗功能存在，還要驗**該功能的執行模型是否相容當前執行環境**。不相容時誠實回報邊界（交付啟用指南），不假裝跑了（unverified_success 紀律的延伸：不只「未驗證的成功」，還有「環境不允許的執行」）。

---

## 可複用 Checklist：制訂執行計劃書時

1. **對稱懷疑每條建議**：① 技術存在？②（存在則）撞既有設計嗎？-> 撞 = tradeoff 交使用者
2. **親驗子代理 verdict 的兩層**：數字屬實？詮釋成立？（後者需親讀上下文）
3. **「試跑/執行」前驗執行模型相容性**：功能存在 ≠ 當前環境可執行
4. **誠實 gap 為主軸**：前置「多數已做/無效」事實，不把報告清單逐條當待辦（反湊數紀律）
5. **被剔除清單也要記錄**：剔除理由寫進計劃書，避免下次重複評估

---

## 與既有紀律的關係

- **延伸** core.md「浮現矛盾不靜默選擇」-> 外部報告 vs 既有設計的矛盾
- **延伸** subagent-strategy「verdict 非證據必 grep 重驗」-> 加「詮釋層」親驗
- **延伸** core.md `unverified_success` 閘門 -> 加「環境不允許的執行」維度
- **呼應** Lesson 2026-06-07-C（幻覺 key）-> 對稱化為「真實但撞設計」也須擋

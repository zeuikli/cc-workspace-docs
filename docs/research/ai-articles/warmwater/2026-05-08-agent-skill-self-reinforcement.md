---
url: "https://warmwater.dev/blog/agent-skill-self-reinforcement"
title: "Agent 怎麼學會新技能：Skill 系統設計與自我強化迴路"
date: 2026-05-08
category: Harness Engineering
source: warmwater.dev
---

在研究 hermes-agent 的 source code 時，我注意到它有一個設計讓我覺得很有意思：agent 跑完一個任務之後，不只是回傳結果，它還有機會把這次任務的經驗，自動轉化成下次可以直接用的 playbook。

不是人工整理，不是 fine-tuning，是在執行框架裡自動運作的一個迴路。

這篇的重點是這個迴路怎麼設計的：為什麼要在 harness 層做 self-improve、被動和主動兩個機制怎麼搭配、以及什麼樣的經驗值得被保存。

### 讀完這篇，你會理解：

- 為什麼 self-improve 放在 harness 層而不是模型層
- 被動 nudge + 主動 patch 的雙模式設計邏輯
- 「只存試錯，不存直接成功」這個 filter 背後的設計判斷
- Skill 數量和品質如何影響 domain agent 的準確率

---

## Skill 是什麼：一句話的背景

Skill 是 agent 的 playbook——「在這種任務情境下，按照這個工作流程，用這些工具，注意這些坑」。它和 Memory 不一樣：Memory 靠語義召回，是被動的；Skill 靠 agent 主動判斷任務性質後載入，是主動的。Skill 也可以從外部 hub 安裝進來，所以它需要信任模型和安全掃描，這是 Memory 不需要的設計負擔。

hermes-agent 把 skill 的知識拆成三層注入，讓 agent 在 Level 1 只看到每個 skill 的 name 和 description（幾行 YAML），判斷需要時再把完整 SKILL.md 載入 context，避免幾十個 skill 的完整內容一次塞爆 system prompt。

這些是背景。這篇真正想說的是接下來的部分。

---

## 為什麼要在 Harness 層做 Self-Improve

Self-improvement 是近年 AI 研究最熱的方向之一。AlphaGo 的 self-play、o1/o3 用 internal reasoning 強化推理、Constitutional AI 讓模型自己批評輸出——這些設計的共同問題是：系統如何從自己的執行結果中學習，不只是從人類 feedback 中學習？

大多數方案的答案是動模型：fine-tuning、RLHF、DPO。這條路有代價——資料準備、訓練時間、版本管理，每次迭代都是工程成本。hermes-agent 選的是另一條路：不動模型，在 agent 的執行框架裡設計迴路。

這個選擇有幾個含義。第一，速度。fine-tuning 的知識要幾天後才能生效，harness 層的 skill 在任務結束幾秒後就寫入。第二，粒度。模型學到的是統計模式，skill 學到的是「這個特定情境下的具體步驟」——它不是泛化，是精確的操作記錄。第三，可讀性。Skill 是 Markdown 文件，任何人都可以讀、審查、修改。模型的 weight 是黑箱。

但這條路也有代價：playbook 不像模型 weight，它不會自動整合矛盾、不會自動泛化，它只會累積。設計不好，skill base 會越來越大、越來越亂、越來越難維護。這個問題後面會回來。

---

## 被動 Nudge：任務結束後的背景分析

hermes-agent 的被動 improve 機制叫做 nudge，它的運作方式設計得很有意思。

每次 agent 做工具呼叫，計數器 `_iters_since_skill` 就累加一次。當這個計數器超過門檻（預設 10 次 iteration），在主任務回應完成之後，agent fork 出一個背景 review agent。這個 review agent 拿到主對話的快照，問一個問題：

> 這次任務有沒有試錯過程、改變方向的時刻、或使用者有特定偏好？如果有，建立或更新對應的 skill。如果沒有，說 "Nothing to save."

幾秒後終端顯示一條通知：

```
💾 Skill 'git-workflow' created
```

「背景」這個設計細節很重要。Review agent 跑在 daemon thread 上，主對話已經回應完畢。用戶不需要等待，review 是 best-effort——如果失敗，主任務已經成功完成了，沒有任何損失。

技術上有幾個安全設計值得注意。Review agent 的 `max_iterations=8`，防止它演變成長任務。它的 `_skill_nudge_interval=0`，防止 review agent 觸發它自己的 review，形成遞迴。這些都是把 best-effort 機制設計得「即使出錯也不會出大事」的具體措施。

### 「只存試錯，不存直接成功」的 filter

Review prompt 的觸發條件不是「任何複雜任務都存」，而是有明確的 filter：只有試錯過程、改變方向的時刻、或使用者明確表達偏好，才值得存。

這個設計判斷背後的邏輯是：直接成功表示現有能力就足夠了，不需要記錄額外的工作流程。如果 agent 用標準路徑就解決了，存一份 skill 只是在 index 裡增加一條未來可能誤觸發的雜訊。只有「被迫試錯」的經驗，才包含真正值得保存的路徑知識。

這個 filter 也解決了另一個問題：防止 skill base 無限膨脹。一個沒有 filter 的 self-improve 系統，每次任務都存，幾個月後 skill index 會充滿各種邊緣情況的 playbook，反而讓 agent 在一般任務裡選擇錯誤。

---

## 主動 Patch：在使用中即時修正

被動 nudge 是「任務結束後回顧」。hermes-agent 還有一個互補機制：agent 在使用某個 skill 的過程中，如果發現它「不對」，system prompt 要求它立即 patch，不等任務結束：

```
If a skill has issues, fix it with skill_manage(action='patch').
Skills that aren't maintained become liabilities.
```

「過期的 skill 是負債」，這句話比聽起來要嚴肅。Memory 過期的最壞情況是召回到一個不再準確的觀察，agent 可能基於錯誤前提做判斷。Skill 過期的最壞情況是：agent 按照一份不正確的 playbook，一步步執行到錯誤的結果，全程沒有報錯，你不知道為什麼結果不對。

被動 nudge 和主動 patch 的搭配，形成了兩道防線：nudge 負責「從每次任務裡學到新東西」，patch 負責「在發現錯誤的當下立即修正」。兩個機制的觸發時機不同，但目標一致：讓 skill base 隨時間越來越準，而不是越來越亂。

---

## Skill 數量與品質：對 Domain Agent 準確率的影響

自我強化迴路有一個不易察覺的風險：如果每次任務都存 skill，或者存了大量不相關的 skill，agent 的表現反而可能下降。

hermes-agent 的設計決策本身就是這個問題的佐證。description 在注入 system prompt 時被截斷到 60 字元，這個限制強迫每個 skill 必須在極短的文字裡說清楚適用場景。另外有 conditional activation 機制：

```python
def extract_skill_conditions(frontmatter):
    return {
        "fallback_for_toolsets": ...,   # 指定 toolset 不可用時才顯示
        "requires_tools": ...,           # 只在指定工具存在時顯示
    }
```

一個 Docker-specific 的 skill，在沒有 Docker 的環境裡根本不出現在 index 裡。這些設計都是在解決同一個問題：skill index 越大、越雜，agent 誤判的機會越多。

對垂直 domain agent 來說更明顯。一個金融報告分析工具，如果 skill index 裡混了十個軟體開發的 skill，這十個 skill 的 description 可能在邊緣情況下誤觸發，讓 agent 沿著完全不相關的 playbook 執行。工具呼叫錯了會報錯；skill 觸發錯了只會靜默地把 agent 推進錯誤路徑。

這意味著：對 domain agent 來說，維護一個精簡、高品質的 skill index，比累積更多 skill 更重要。自我強化迴路的價值不在於 skill 越來越多，而在於最適合這個 domain 的 skill 越來越準。

---

## 安全問題：為什麼一份 Markdown 能成為攻擊向量

Skill 有一個 Memory 沒有的特性：執行能力。一份惡意 SKILL.md 可以讓 agent 執行任意命令。2026 年 2 月的 ClawHavoc 事件讓這個問題變得具體——ClawHub 上發現 341 個惡意 skill，攻擊模式包括資料外洩（把 API key curl 出去）、Prompt Injection（`ignore all previous instructions`）、惡意持久化（修改 SSH authorized_keys）。

hermes-agent 的應對是 Quarantine + Scan：外部 skill 先進隔離區，通過 50+ regex 規則和 Unicode 隱藏字元掃描，再對應信任等級矩陣決定是否安裝：

| 來源 | safe | caution | dangerous |
|------|------|---------|-----------|
| 內建 | 允許 | 允許 | 允許 |
| trusted（openai / anthropics） | 允許 | 允許 | 阻擋 |
| community | 允許 | **阻擋** | 阻擋 |
| agent 建立 | 允許 | 允許 | **詢問** |

`agent-created` 獨立成一個信任等級——允許 `caution`（agent 生成的 skill 可能需要動態指令），但 `dangerous` 仍需使用者確認。信任這個 agent 的判斷，但保留最終的安全閘門。

---

## 延伸閱讀

- [你的 Agent 為什麼漸漸不像自己了：固定知識與流動知識的設計邊界](/blog/agent-memory-identity-design) — Memory 設計邏輯，以及 skill 和 memory 的邊界
- [Harness Engineering 的地基：LLM Session 設計框架](/blog/llm-session-harness) — session 管理的四種策略
- [Agentic Loop 的設計關卡：工具執行、錯誤分類與中斷機制](/blog/agentic-loop-design) — Loop 執行引擎的工程設計

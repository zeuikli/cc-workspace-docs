---
title: "Session Insight — 跨模型 Harness 激盪 session 的 meta-learning"
date: 2026-06-23
branch: feature/chatgpt55-harness-crossbreed
related: 2026-06-23-crossmodel-harness-crossbreed.md
tags: [session-insight, dynamic-workflow, fable-unavailable, home-team-bias, verdict-not-evidence]
type: session-insight
---

# Session Insight — 跨模型 Harness 激盪

> 本 session 用 dynamic workflow（17 agents / 971K tokens / 585s）讓 ChatGPT 5.5 與現有 Zeuik harness 激盪，過程本身浮現 5 個可沉澱的 harness/process 教訓。

## 主任務結論（一句話）
現有 Zeuik 繁中 + grounding 勝、ChatGPT 5.5 typed backbone + byte 勝；融合 = substrate 掛 backbone，但對抗稽核把「5 規則一次落」降為「R3 優先 + 守 ≤1/cycle + cap 不上調」。詳見 `2026-06-23-crossmodel-harness-crossbreed.md`。

## Insight 1：Fable 不可用 = harness fallback 原則的活體驗證
**事件**：workflow 中所有 fable model 的 agent 失敗（"Claude Fable 5 is currently unavailable"），影響 fable-pilot 第四維評審 + 全 5 條 adversarial 驗證。
**處置**：用 opus 接手對抗稽核（fresh-context verifier）。
**教訓**：這不是純粹的 infra 失敗——它**實證了兩個既有原則的現實性**：(a) MEMORY 既有「Fable cyber/bio silent fallback → Opus」；(b) codex-rewrite 的「不可跨 generation/provider 直接移植 prompt」。**部署 surface 的能力可能在執行當下不存在 → harness 必須有 fallback 路徑，且 fallback 路徑要能無縫接手稽核職責**。opus 接手符合 workspace「generator≠evaluator」+ Fable 5 official「fresh-context verifier > self-critique」。
**防範**：workflow 內含 model-specific agent（尤其 fable）時，設計要假設該 model 可能不可用 → 失敗時降級到次強 fresh-context model，不讓整 phase 歸零。本次 workflow 的 `.filter(Boolean)` 讓 fable 失敗不 crash 全 workflow，但 adversarial phase 仍歸零（5/5 失敗）→ 應在 script 層對 fable agent 加 opus fallback，而非靠主對話事後補。

## Insight 2：synth「crossbred beats both」= 結構性 home-team bias
**事件**：opus synth 判「融合版勝過兩者」——這是**讓整個 exercise 顯得值得的便利結論**。opus 對抗稽核（不同 context）抓出 3 處 ChatGPT 5.5 被低估：R3 Handoff Contract（~90% 是 ChatGPT 內容）、「commit only when asked」（比現有 over-commit 安全）、maintainability/taste 軸。
**教訓**：當 synthesizer 與 home codebase 同源（都在 workspace context 內），它有結構性誘因偏袒既有 harness。**「融合勝」這種結論本身要被當作 bias 訊號重審**，不是因為它錯，而是因為它太方便。
**防範**：跨模型比較的 synth verdict 後，必接一個**對抗稽核專門找 home-team bias**（「哪裡 visiting team 其實對而被低估？」）。本次靠 opus 對抗稽核補上；若無此 phase，會把 home-team-flavored 結論當定論。再次應驗 core.md TEST「subagent/workflow verdict 非證據」——**connect 到 synth 自己也是 verdict 非證據**。

## Insight 3：byte 數歧義是 disqualifying issue，必先重測
**事件**：synth 用 287B headroom，MEMORY 上次記 33B（18,967/19,000）。對抗稽核標「此歧義 disqualifying，未解前不可寫報告」。主對話 canonical 六源重測 = **18,713/19,000 = 287B**（MEMORY 記錄已過時，auto-load 自那以後縮過）。
**教訓**：harness 編輯決策依賴的關鍵數字（byte headroom）**有兩個來源衝突時，任何下游決策都暫停，先用 canonical 命令親測**。MEMORY 的數字是 snapshot，會 stale。
**防範**：涉 auto-load byte 的提案，第一步永遠 `wc -c` 六源親測，不信報告/MEMORY 引用的數字。MEMORY 須更新 byte 記錄（本 session 18,713，非舊記 18,967）。

## Insight 4：「~0B net」是融合規則最常見的成本謊言
**事件**：synth 標 R3 Task-Contract「~0B net」。對抗稽核 grep 確認 subagent-strategy 根本沒有 Goal/Done-when/Allowed-paths 結構 → R3 是真淨新增 **+150-250B**，非 0。
**教訓**：當提案說「替換既有 → 淨零成本」，要 grep 確認**被替換的內容真的存在且體積相當**。「extend 既有 list」可能是 +0（R4 那種），「新增結構聲稱替換既有」常常是隱藏淨增。
**防範**：每條融合規則的 byte_estimate 主對話 grep 親驗「被替換 target 是否存在 + 體積」，不信 agent 的 byte 自估。

## Insight 5：對抗稽核 > synth 的價值在於「降溫」而非「加料」
**事件**：synth 產 5 條規則 + 樂觀落地；對抗稽核**沒加任何新規則**，全部動作是降溫——R1 壓縮/defer、R2 縮成指針、R4 DROP、R5 去重、5 規則降為 1 優先。
**教訓**：在「激盪出更多」的任務框架下，模型有 generative bias（多產規則 = 顯得有產出）。**真正的 harness 價值常在「砍掉幾條」而非「再加幾條」**——對抗稽核的職責是擋下 self-preferential 膨脹。本次若無對抗 phase，會落 5 條（破 cap + 破 cycle gate）= 比兩個 parent 都差的 harness。
**防範**：harness 自我演化任務的成功指標**不是新規則數，是淨改善**；「激盪」的產物先過「這條擋過哪個真實失敗」gate（APPLY-gate #2），擋不過就 defer。本次 27 claim 驗證 + 5 規則提案，最終僅 R3 達 HIGH_VALUE 立即落地門檻。

## 待沉澱到 MEMORY 的 lesson
- **Lesson 2026-06-23-A**：[workflow model-specific agent 須有 fallback] fable agent 全失敗使 adversarial phase 歸零；script 層應對 fable 加 opus fallback，不靠主對話事後補。
- **Lesson 2026-06-23-B**：[cross-model synth 的 home-team bias] synthesizer 與 home codebase 同源 → 必接對抗稽核專找「visiting team 哪裡被低估」；「融合勝兩者」是 bias 訊號。
- **Lesson 2026-06-23-C**：[byte 數衝突 = disqualifying] auto-load 決策的關鍵數字兩源衝突時暫停，canonical 六源親測；MEMORY snapshot 會 stale（本次更正 18,967→18,713）。
- **Lesson 2026-06-23-D**：[「~0B net」成本謊言] 融合規則聲稱替換既有 → grep 確認被替換 target 存在且體積相當，否則是隱藏淨增。
- **Lesson 2026-06-23-E**：[harness 演化成功 = 淨改善非新規則數] 「激盪出更多」框架有 generative bias；產物先過 APPLY-gate #2，擋不過 defer。

## loop-2 追加 insight（substrate 深化，見 2026-06-24-crossbreed-substrate-impact.md）

## Insight 6：「先報告後裁決」在重複 /loop 下要主動守住
**事件**：第一輪結束問「是否落地 R3」未獲回應，使用者再發**相同 /loop prompt**。誘惑是「他又叫我做 → 直接套用 auto-load」。
**處置**：AskUserQuestion 確認方向（深化研究 vs 實際套用 vs 收尾），使用者選深化研究。
**教訓**：相同 prompt 重發 ≠ 授權跨越上一輪自定的不可逆 gate（套 auto-load）。auto-load 編輯是 gated（/autoload-evolution）+ 飽和風險，**重複觸發不等於裁決**。防範：上一輪明確列「待裁決」的不可逆動作，下一輪即使同 prompt 也先確認，不靜默升級為「執行」。

## Insight 7：主對話親驗也會因 grep 模式錯而冤枉 agent
**事件**：親驗第 3 個 inline-mirror（multi-mode-skill:78）時，grep 模式含反引號 `` `rules/...` `` 未對上 markdown 格式 → 初判「agent 幻覺引用」。換模式重 grep 才確認 :78 確實存在。
**教訓**：「verdict 非證據必親驗」是對的，但**親驗工具本身（grep 模式）也會出錯**——grep miss 有兩種：真不存在 vs 模式沒對上。防範：grep 失配（exit 1）時，先換更寬模式重試（去特殊字元/縮短錨點）再下「不存在/幻覺」結論，否則會反向冤枉正確的 agent 輸出。這是 trust-axis 之外的 **tool-axis 驗證盲點**。

## Insight 8：open-q 落地設計的 audit 抓出「設計自相矛盾」非只 byte 謊言
**事件**：opus audit model-switching 設計，抓出它同時宣稱「confidence 是 LLM judgement（須留 LLM）」+「confidence 由 exit-code 衍生 = 確定性」**自相矛盾**，且新增 `<0.70 floor` 與既有三帶語意衝突（會讓每個 converged=false 都觸發 model re-bind）。
**教訓**：對抗稽核的價值不只在 byte 數造假（Lesson 2026-06-23-D），更在**設計層的內部矛盾 + 與既有語意的隱性衝突**——這些 grep 抓不到，需理解既有 schema 語意才看得出。防範：新規則/設計引用既有 schema 的 field/threshold 時，audit 須驗「新語意是否與該 field 既有語意衝突」（confidence floor vs converged band），非只驗 field 存在。

## loop-2 待沉澱 lesson
- **Lesson 2026-06-24-A**：[相同 /loop prompt 重發 ≠ 跨 gate 授權] 上一輪列「待裁決」的不可逆動作（套 auto-load），下一輪同 prompt 仍先 AskUserQuestion，不靜默升級執行。
- **Lesson 2026-06-24-B**：[grep 失配有兩種] exit 1 = 真不存在 OR 模式沒對上；下「agent 幻覺」結論前先換寬模式重試（去特殊字元）。親驗工具本身也會錯（tool-axis 盲點）。
- **Lesson 2026-06-24-C**：[audit 抓設計矛盾 > byte 謊言] 新設計引用既有 schema field/threshold 時，audit 須驗語意衝突（confidence<0.70 floor 撞既有三帶），非只驗 field 存在——grep 抓不到語意衝突。
- **Lesson 2026-06-24-D**：[R3 落地 = 5B 飽和] 主對話親算 18,713+282=18,995/19,000，feasible 但飽和；R3 落地後 auto-load 幾乎滿，R1/R2 必走 refs 化無法 inline 共存。

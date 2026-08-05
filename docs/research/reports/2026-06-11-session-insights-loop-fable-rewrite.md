---
title: "Session Insights — The Loop 唯一準則化 + Fable 5 世代改寫（九波 commits 全程）"
date: 2026-06-11
status: final
related: 2026-06-11-instruction-files-self-audit.md · loop-only-canon-integration.md · post-rewrite-self-audit.md · final-self-audit-v2.md
scope: 跨 17 小時、9+ commits、PR
type: session-insights
---

# Session Insights — 2026-06-11

> 本檔記**可遷移的洞察**（執行明細見 related 報告鏈）。每條格式：洞察 → 現場證據 → 落地位置。

## 1. 驗證閘門在最強模型世代「更」load-bearing（本 session 三次現場證明）

- **implementer 假成功**：自報「verification all pass」，實際變更滯留未 commit 的 worktree——`git checkout <branch> -- <path>` 取回的是基底舊內容。
- **auditor 訓練知識過期**：fan-out researcher 斷言「Fable 5 為不存在模型」，而當下 session 即運行於 claude-fable-5。
- **外部自動化「新標籤舊數據」**：harness-model-fit.json 被改成 `model_version: claude-fable-5` 但 eval_baseline 仍是 sonnet 世代實測值——比 drift 更糟，因為它**摧毀了 drift 偵測訊號本身**。
- 與 papers 收斂：Vesper 強模型 eval-hack 16.6% vs 弱模型 0%。**換更強模型該刪的是行為補丁，該留且該加固的是驗證閘門**——這是整場「刪 14 條準則」工程的唯一裁決準星。
- 落地：core.md unverified_success 閘門原樣保留；fable-pilot「Frontier 驗證紀律」硬 gate；rejected-claims ledger 成為稽核協議標配。

## 2. Sub-agent worktree 基底 ≠ 工作分支（高破壞力陷阱）

worktree 自動隔離的基底可能是 **main 而非當前分支** → 直接 cp 產出會**回退本分支已套用的修正**（本 session 實際洗掉 phase-1 順序修正，靠 diff --stat 驗證攔回）。防範三件套：① 產物指定寫 `/tmp/claude-scratch/`；② 取回後 `git diff` 驗「只含預期變更」；③ 重跑本分支已知 sweep。→ Lesson 2026-06-11-C + fable-pilot 硬 gate #2。

## 3. Spend limit 是一種 failure mode，交接是一種能力

org spend limit **無預警終止** background agent；但 agent 已分檔落盤 /tmp 的部分產出可由主對話驗收續用（pilot 三件套重寫因此零損失存活）。兩個推論：
- **委派長任務 = 要求 agent 每完成一檔即落盤**，不等全部完成才輸出（Lesson 2026-06-11-D）。
- 交接不該是手工儀式 → 固化為 `/handoff` SKILL（hook 管遙測、SKILL 管內容；MEMORY 摘要必須自足，因 progress 檔 gitignored + 遠端容器 ephemeral）。

## 4. 動態數字寫進靜態文件 = 立即腐化（兩小時內實證兩次）

auto-load byte 快照在本 session 內**兩度手動同步、兩度再過期**（18,969 → 18,985 → 18,986）。根治 = 刪數字、留命令指針（「跑 `measure.sh --gate`」）。一般化：**SSoT 是量測命令，不是量測結果**；任何「會動的值」入靜態文件前先問「誰負責讓它不過期？」答不出 → 寫命令不寫值。

## 5. 半失效自動化比沉默更糟

`_sync_skill_roster.py` 每跑必印 `docs/INDEX.md: pattern not found` + exit 1——連本 session 主對話都兩次當雜訊忽略。半失效輸出**訓練操作者跳過警告**，腐蝕 Fail Loud 的可信度。判準：自動化的每行輸出都應 actionable；不可行動的警告 = 待修 bug 或待刪輸出。

## 6. 「14 條 → 六階段」零損失移除的方法論

編號準則可以徹底退役而不損失行為契約，前提是三件事先成立：① 雙向對照表證明每條已被吸收（06-05/06-06 兩份報告交叉）；② 區分**結構指針 vs 出處署名 vs 歷史記錄**（指針改寫、署名保留、歷史不竄改）；③ 機械成功條件（活文件 grep = 0）。對照組教訓：harness-audit-METRICS 的 R1–R6 是**自有命名空間**——批次清除前必先分類命名空間，否則誤殺。

## 7. Capability-conditioned 約束：強模型要目標不要步驟

Prompting Inversion（constrained CoT 在 frontier −2.36pp）+ 本 session 實感：對強模型，**程序性約束是 token 稅兼 hyper-literalism 誘因**（Think-Before hook 注入移除、200 行分段讀刪除），但**目標表述 + 機械驗證條件**反而要更強。新增約束前的自問句已入 fable-pilot IDENTIFY 行：「這會不會在已能正確推理的模型上誘發字面主義？」

## 8. Byte 預算 99.9% 使用率下的工程紀律

auto-load 終態 18,986/19,000（餘 14 bytes）。在硬頂附近運作的三條實戰法則：① **增字先減字**（每筆 CLAUDE.md/rules 編輯先算淨 byte）；② **結構槓桿 > 逐行刮**（整段下沉 refs 一次回收數百 byte；逐行刪每輪 6–40 byte 還會誤削 mechanical check）；③ 上限的存在迫使「可推導 = 噪音」原則真正執行——預算壓力是規則庫品質的盟友。

## 9. 模型分層的成本語義（使用者裁決後的定型）

日常預設 = Sonnet 4.6；Fable 5 = 重構/強化/優化/最強稽核**場景觸發**（新 session 切換）；Opus 4.8 = 審查 + cyber/bio 域（Fable silent fallback 防範）；Haiku = 搜尋/輕量。配套：**Effort 先於 model**（Fable medium ≈ Opus max；high 為甜蜜點）。「預設用最強」被否決的理由值得記：最強模型的正確用法是**槓桿點投放**，不是常駐。

## 10. 雜項戰術教訓

- `cd /tmp && bash scripts/x.sh` 複合命令讓相對路徑腳本炸掉（本 session 踩兩次）→ repo 腳本一律從 repo root 跑或改絕對路徑。
- append-only jsonl 的 merge conflict 用 union 解（pre + ours + theirs-not-seen），勿擇邊。
- squash merge 後 pinned 分支續用：`git merge origin/main`（非 rebase）+ jsonl union，分支即重新可用。
- Ground-truth 注入應成為**所有**稽核類委派的標配段落：模型 roster、已修清單、「不存在類宣稱必先 ls」。

## 待續（交接）

- 交叉驗證稽核（2 auditor）執行中——比對 final-self-audit-v2，產出附錄。
- 可選：`/harness-meta:hmf` 為 Fable 場景補測 baseline（model-fit `pending_revalidation` 已標）。

---
title: "Auto-load 載入內容優化評估：refs / hook / 維持 rules 按需 — 三化已極致的誠實 no-op"
date: 2026-06-24
based_on: [2026-06-23-crossmodel-harness-crossbreed.md, 2026-06-23-session-insight-crossmodel-crossbreed.md, 2026-06-24-crossbreed-substrate-impact.md]
tags: [autoload-evolution, byte-cap, refs-offload, hook-enforcement, the-loop, honest-no-op]
type: assessment-report
verdict: NO-OP (auto-load 已 refs/hook/path-scoped 三化到極致)
---

# Auto-load 優化評估

> **結論：不需優化。auto-load 18,984/19,000（16B 飽和）是「逼滿但乾淨」，無安全可回收的純機械冗餘。** 經 ceiling-mode 逐段審計 + 主對話親 grep 重驗，所有大段都是高頻行為契約、所有確定性 gate 已在 hook、所有參考表已下沉 refs。這是有 MEMORY 先例的誠實 no-op（Lesson 2026-06-06-A coldstart audit）。

## 0. 評估方法（符合 The Loop）

本評估**本身**走 The Loop：OBSERVE（讀三報告 + 六源 byte）→ IDENTIFY（refs/hook/rules 四分類框架）→ PROPOSE（ceiling agent 逐段 verdict）→ TEST（主對話親 grep 重驗 agent 宣稱）→ RECORD（本報告）。**verdict 非證據**：ceiling agent 的 no-op 結論經主對話親驗 4 項關鍵宣稱（exit=0）才採信。

## 1. 現狀（主對話親測）

| 檔 | byte | 評估 |
|----|------|------|
| CLAUDE.md | 1,686 | 純指針層，零回收 |
| core.md | 9,765 | 最大檔，但已 refs 化到極致（4 處 refs 指針外移案例）|
| context-management.md | 1,894 | 鐵律 + refs 指針最簡態 |
| output-discipline.md | 1,450 | 每次回應套用，最高頻 |
| subagent-strategy.md | 3,185 | R3 剛落地的飽和源 |
| README.md | 1,004 | 純索引（path-scoped 機制入口）|
| **合計** | **18,984/19,000** | **16B headroom（飽和）** |

## 2. 三化驗證（為何 no-op）

### refs 化已極致（親驗 4 處外移）
The Loop 案例 → `.claude/refs/the-loop-best-solution.md`；cache 指標 → `cache-health-metrics.md`；CJK → `cjk-token-efficiency.md`；model grid → `model-selection-grid.md`；compact 範本 → `post-compact-checklist.md`。**inline 留的全是條文骨架本身，非可下沉的參考表。**

### hook 化已極致（親驗 measure.sh --gate exit 1）
- byte cap → `measure.sh --gate` 超 19,000 exit 1（**已機械執行**，prose 是互補決策層非冗餘）
- 危險命令（rm -rf / VAR= 前綴）→ `block-dangerous.sh` exit 2
- 敏感檔（.env/.pem/credentials）→ `protect-sensitive-files.sh`
- commit gate → `pre-commit-review.sh`（healthcheck FAIL=0）
→ **auto-load 的對應 prose 是「決策層提醒」，hook 是「執行層攔截」，互補非冗餘**（core.md:4「硬性執行交 hooks，規則是 advisory」的設計分工）。

### path-scoped 已用滿
安全規則 → `security-hygiene.md`（編輯 .env 觸發，frontmatter `paths:` glob）；prompt 工程 → `prompt-lifecycle.md`（編輯 auto-load 觸發）。**core.md 殘留段全是跨檔類型高頻契約，無可 path-scope 的對象。**

## 3. 唯二回收候選（皆不建議現在做）

| 提案 | 段 | 淨回收 | 裁決 | 理由 |
|------|-----|--------|------|------|
| P-A | core.md Bash 慣例（82-85）→REFS | ~180B | **不做** | 這是「怎麼寫才不觸發 hook」的**正向指引**，hook 只負向攔截。下沉後 Claude 不知有此約束 → 反覆撞 block-dangerous.sh 困惑。「Better Prompts Hurt」典型：省 180B 但失高頻 grounding |
| P-B | subagent Routines（24-26）→REFS | ~60B | **defer** | `/schedule` 真低頻、有現成 refs 落點（error-handling.md）。但 60B 不值得為飽和開 refs 漂移面（manual-read ref 孤兒=死重風險）。留作未來需空間時第一順位 |

**無新 →HOOK / →PATH-SCOPED 提案**：既有 hook 全覆蓋確定性 gate；core.md 內無「只在特定檔類型才需」的段。

## 4. The Loop 對齊（使用者強調點）

「不改」這個決定本身符合 The Loop 的 PROPOSE 紀律：
- **極簡 + 外科刀**：不投機優化、不為「未來可能」鋪設（PROPOSE）。16B 飽和雖逼滿但無冗餘 → 強行 refs 化是製造問題。
- **Rule of 3 / 不為塞 byte 反推**：core.md §Framework Integrity「不接受為塞單一新規則反推湊 byte」的反面 = 也不為「製造優化產出」硬找回收。
- **誠實 no-op 有先例**：Lesson 2026-06-06-A（coldstart audit 誠實 no-op，274B 餘裕「逼滿但乾淨」列觀察不硬改）。本次 16B 同理。
- **未來空間需求的最小安全第一步**：等 R4/R5 新規則的 autoload-evolution cycle 一併處理（≤1 規則/cycle），屆時第一順位 P-B（Routines → error-handling.md，~60B），**P-A 永不建議**。

## 5. 浮現的相鄰問題（非本任務範圍，記錄回報）

ceiling agent 浮現 + 主對話親驗確認：**auto-load 六源有 12 處 `refs/` 指針（core 4 + context 2 + output 1 + CLAUDE 2 + subagent 3），但 refs 實體在 `.claude/refs/`** → 從 repo root grep `refs/xxx` 找不到（相對 `.claude/` 慣例未明示）。這是 discoverability 風險（非 byte 問題），屬「auto-load 內容品質」而非「載入優化」範圍。**記錄回報，不在本評估自動修**（commit 原子性：優化評估 ≠ 路徑慣例修正）。若要修，最小動作 = 在 CLAUDE.md 或 refs/README 註明「auto-load 內 `refs/` 指針相對 `.claude/` 解析」一行。

## 6. 殘留風險與下一步
- **本評估零 .claude/ 編輯**（結論是 no-op，符合「先評估後動」）。
- byte 飽和持續監控：MEMORY「19,000 近滿監控」更新為 16B；任何新 auto-load 增補前必先壓出空間（P-B 為第一順位）。
- 驗證狀態：ceiling agent verdict + 主對話親 grep 重驗 4 項（byte cap hook / refs 實體位置 / refs 指針密度 / 兩候選存在）exit=0。

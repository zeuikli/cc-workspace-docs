# skill-evolution PROPOSE — fusion / multi-mode-skill / researcher（7 項）

> 日期：2026-07-16 · 證據源：(a) wBlock URL Filter fusion 全鏈路實測（`2026-07-16-fusion-wblock-urlfilter-process-log.md`）(b) output-compress × fusion/multi-mode 整合評估（本 session）。
> 依 skill-evolution 規則：apply 一次一個 SKILL、每項標 Gap 維度、不改 name/description/觸發詞。
> Empirical eval gate 偏離說明：本批全為行為指導文字（非 Guard/script），無既有 eval fixture 可跑前後對照；以「單一實證失敗案例 + 機械可驗收條件」替代，標 `[eval:deferred]`，14 天退化觀察照 RECORD 規則。

## Batch 1 — fusion SKILL（4 項，一次 apply）

### P1：§1 加「hook 白名單相容性」委派前檢查
- **Gap 維度**：Fallback 路徑（sidekick 遇 hook 阻斷無前置防線）
- **證據**：wBlock Phase 0 spike——sidekick 燒 50.6k tokens / 333s 後才發現 `swiftc/swift/bash` 全被 `block-dangerous.sh` Layer 2 白名單擋；lead 事後親跑同樣被擋。一輪委派浪費。
- **變更**：§1 表格後加一行紀律：brief 涉及的關鍵命令（編譯器/套件管理器/非常見 CLI）先由 lead 以最小無害形式過一次 hook（如 `<cmd> --version`）；被擋 → 改 brief（改走可用路徑）或先與使用者協商白名單，再委派。
- **驗收**：`grep -q "hook 白名單" .claude/skills/fusion/SKILL.md`

### P2：§3 補 brief 壓縮裁決引用
- **Gap 維度**：Trigger 清晰度（與 output-compress AUTO 的邊界未寫明）
- **證據**：output-compress §1「單次派工 prompt 帳目裁決」已存在（契約欄位逐字原文則可即拋型壓縮），fusion §3 未引用 → 兩 SKILL 同時啟用時邊界靠記憶。
- **變更**：§3 brief 模板後加一句：brief 正文可依 output-compress §1 單次派工裁決壓縮（AUTO mode 下自動適用），Goal/Constraints/Edge cases/Done-when/Allowed-paths/Non-goals/Return 契約欄位逐字原文永不壓。
- **驗收**：`grep -q "output-compress" .claude/skills/fusion/SKILL.md`

### P3：§4 驗收清單加 worktree 收檔步驟
- **Gap 維度**：Fallback 路徑（isolation worktree 產物回收無標準步驟）
- **證據**：wBlock 鏈路兩個 Opus agent 均寫入 isolation worktree，lead 需手動 cp + scope check + `git worktree remove`；SKILL §4 無此步驟，靠 lead 臨場想起。
- **變更**：§4 第 1 點後插入：sidekick 用 worktree isolation 時，驗收含三步——worktree `git status --short` scope check → 產物 cp 回主 checkout → `git worktree remove`；漏收檔 = 產物在 worktree 刪除時滅失。
- **驗收**：`grep -q "worktree" .claude/skills/fusion/SKILL.md`

### P4：§6 經濟模型計入壓縮後 brief bytes
- **Gap 維度**：版本/日期（經濟模型未更新 output-compress 整合後的帳目）
- **證據**：§6 成本主導項 =「lead turns × context 拖帶量」；output-compress 對派工 prompt 的 input 節省（CJK 實測 ~15-18%，白名單密集 prompt 僅 2.4-6.8%）直接影響 handoff 固定開銷估算。
- **變更**：§6 加一句：handoff 開銷估算以**壓縮後** brief bytes 計；白名單密集（契約欄位占比高）的 brief 壓縮收益趨近零（實測 2.4-6.8%），勿以壓縮為由放寬「短任務不委派」門檻。
- **驗收**：`grep -q "壓縮後" .claude/skills/fusion/SKILL.md`

## Batch 2 — multi-mode-skill（2 項，一次 apply）

### P5：新增 §1d Usage 水位 → 路由連動（消費 pacer `fanout` 欄）
- **Gap 維度**：Guard/Verify 可機械驗證（訊號已存在但無消費者，接線斷鏈）
- **證據**：output-compress §2 註明 `usage-pacer.py` verdict JSON 含 `fanout: burst|normal|prefer-lower-tier`「供 delegation/multi-mode 機械消費」——multi-mode-skill 全文無任何引用。水位監控只調壓縮級距、不調路由，半接線。
- **變更**：新增 §1d（≤8 行）：spawn 前讀 pacer verdict（確定性 script，非 LLM 判斷）；`prefer-lower-tier` → §1 表格 tier 降一檔（架構/安全關鍵字任務除外——品質底線不受水位影響）+ fan-out 上限減半；`burst` → 照表；無 verdict 檔案 → 照表（fail-open）。
- **驗收**：`grep -q "fanout" .claude/skills/multi-mode-skill/SKILL.md`

### P6：§2 回收契約加「版本/相容性事實」重驗規則
- **Gap 維度**：Gotcha 記錄（cost 檔系統性弱點未入紀律）
- **證據**：wBlock 鏈路 F3——Haiku researcher 稱 URLFilter 需 macOS 14.5/iOS 17.0（實為 26.0/26.0），靠 lead 手上的 SDK 第一手佐證攔下。cost 檔在「版本/相容性/日期」類事實最易錯。
- **變更**：§2 回收契約段加一句：cost 檔 worker 回傳的版本/相容性/OS 需求類事實，無論是否標 `[claim:verified]`，parent 一律以第一手來源（SDK/官方文件/實機命令）重驗後才可寫入交付。
- **驗收**：`grep -q "版本/相容性" .claude/skills/multi-mode-skill/SKILL.md`

## Batch 3 — researcher agent（1 項；偏離說明：agent 定義非 SKILL，仍循同流程 surgical edit）

### P7：下沉 claim 標註契約 + 事實類來源要求 + Apple docs gotcha
- **Gap 維度**：工具宣告完整性/Guard（multi-mode-skill §2 的回收契約未下沉到本 agent；sub-agent 不繼承 auto-load，掛鉤必須寫在 agent body）
- **證據**：(a) F3 幻覺 OS 版本且無標註；(b) F2 Apple developer docs SPA 直抓失敗，JSON endpoint 技巧靠 parent 臨場寫進 brief。
- **變更**：工作原則加兩條——① 每項事實宣稱自標 `[claim:verified]`（附驗證命令/URL）或 `[claim:asserted]`；版本/相容性/日期類必附來源，查不到標「查無」。② gotcha：Apple developer 文件為 SPA，`developer.apple.com/documentation/<path>` 直抓只有 title，改抓 `developer.apple.com/tutorials/data/documentation/<path>.json`。
- **驗收**：`grep -q "claim:verified" .claude/agents/researcher.md && grep -q "tutorials/data" .claude/agents/researcher.md`

## Apply 順序與範圍

1. Batch 1（fusion，4 edits，一個 commit）
2. Batch 2（multi-mode-skill，2 edits，一個 commit）
3. Batch 3（researcher.md，1 edit，一個 commit）
- 行數約束：fusion 現 ~90 行、multi-mode-skill 157 行、researcher 40 行——全部遠低於 350，加行無虞。
- 不改 frontmatter name/description/觸發詞；version 各 +0.0.1 並更新 version-note。
- RESOLVER.md 無需動（無新 SKILL）。

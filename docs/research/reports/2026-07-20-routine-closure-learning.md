# Learning Checklist — Routine 補閉環 · read-path 斷點

> /teach session 2026-07-20 · 基底：`2026-07-20-loop-engineering-harness-insight.md`
> 狀態：⬜ 未教 · 🟡 教學中 · ✅ 已展示理解

| # | 概念 | ①問題 | ②解法 | ③脈絡 | 狀態 |
|---|------|------|------|------|------|
| C1 | 為何閉環會「忘記/無法執行」——問題的真形狀（不是排程缺席，是 read-path 斷 + 人是唯一觸發器） | ✅ | ✅ | ✅ | ✅ |
| C2 | Routine 能補什麼、不能補什麼（觸發器 vs 電路；cron 打進斷的 read-path = 空轉，例證：R1/B1 routine 已存在仍空轉） | ✅ | ✅（首測誤選 dreaming，補「觸發時機形狀」判準後重測過） | ✅ | ✅ |
| C3 | 正確順序：① trace capture（session-stop.sh skills_used）→ ② dreaming 接線 → ③ eval 閘；routine 只在電路通了之後才有東西可推 | ✅ | ✅ | ✅ | ✅ |
| C4 | 自動化的安全邊界：外部 oracle 前置、不可逆處人閘、routine 自身要寫 heartbeat（可被監控） | ✅ | ✅ | ✅ | ✅ |

## 學習日誌
- 開場 restate：「該讀的資料有缺、做法不確定」→ 定位缺口：對 write/read path 的區分未成形。
- C1 首測誤判「routine 會被卡住報錯」→ 補「空轉不報錯比 crash 更危險（B1 16 天假信心）」→ 重測過（正確指認 B1）。
- C2 首測誤選 dreaming 為錯誤用途 → 補「觸發時機形狀」判準（時間驅動→routine／事件驅動→hook／欄位沒寫→改 code）→ 重測過（push 前 review=hook、每日報告=routine）。
- C3 一次過：跳過①的後果（讀 [] 空轉）+ 正確第一步（合成 transcript 先驗 oracle）。
- C4 一次過：自評=中間態、外部 oracle 前置、consolidation 人閘。
- 終局復述（學習者原話）：「把流程走過一遍，沿路要補完一些東西，才能把流程串在一起；且審閱過才能併入主線做為下次的累積經驗」——命中電路先於觸發器 + oracle/人閘兩根主樑。

## 標準版答案（存底）
**「閉環忘記/無法執行，可用 routine 補齊嗎？」**
- **能補**：觸發自主性（人是單點故障的部分）——每週 dreaming 蒸餾、定期 harness sweep 稽核、heartbeat 新鮮度檢查（皆時間驅動）。
- **不能補**：point-of-need retrieval（LESSONS→動作前提醒，事件驅動 → hook）；trace capture 斷線（session-stop.sh 沒寫 skills_used → 改 code）；不可逆核可（永遠人閘）。
- **順序**：① 修 trace capture（oracle-first：合成 transcript 先驗）→ ② dreaming 接 task-log → ③ eval 閘 → ④ routine 排程。倒序 = B1 式空轉（不報錯的假信心）。
- **邊界**：自動迴圈產出候選=中間態，過外部/異模型 oracle 才算數；merge/不可逆處人閘；routine 自身寫 heartbeat 可被監控。修閉環的動作本身也要過閉環的閘（A1 例）。

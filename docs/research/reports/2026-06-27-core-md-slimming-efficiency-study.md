---
date: 2026-06-27
status: 研究完成，待人工授權執行
method: 內容類型二分 + 逐區塊「移除後在哪犯錯」+ byte 實測 + 下沉落點
scope: "core.md 瘦身與效率研究（六源 byte 貼頂 19,000 後的治本方案）"
type: research / 實證計劃書
---

# core.md 瘦身與效率研究 — 2026-06-27

## 0. 動機

本日 rewind 補充把六源逼到 **19,000B 貼頂（零餘裕）**，measure --gate 一度 FAIL。pilot-review 已診斷根因：19,000 門檻設定於 content 較少時，現為自然成長壓頂。本研究給 core.md 的**結構性瘦身方案**（非單次 byte 微調），目標騰出真實 headroom 並提升效率。

## 1. 核心診斷：core.md 混了兩種內容

| 類型 | 定義 | 處置 |
|------|------|------|
| **(A) 行為契約** | 改變 in-context 行動的鐵律（「遇 X 必 Y」「宣告完成前必跑 Z」） | **留 auto-load** |
| **(B) 參考細節** | 命令清單 / 具體數字 / 操作程序 / citation——查得到即可，不需常駐 | **下沉 refs，留鐵律句 + 指針** |

byte 壓力來自 (B) 在 core.md 累積。`README.md` 既有「下沉原則」：純參考表/低頻細節 → refs，auto-load 只留鐵律句。core.md 尚未徹底套用此原則。

**效率三維**（「更有效率」的完整定義）：
1. **byte 效率**（綁定約束）：(B) 下沉 → 騰 headroom，這是 measure --gate 的硬牆。
2. **compliance 效率**：CLAUDE.md 自陳「規則膨脹後 compliance 急降」——更短 core.md = 更高遵從率，瘦身本身即提升品質，非只省 byte。
3. **token 效率**（CJK 稅）：core.md CJK-dense（cjk-token-efficiency.md：CJK 2–3× token）。但 byte cap 採 byte 為 canonical 單位正是為對 tokenizer 免疫——故**門檻層面 token 不是約束**；token 效率屬處理成本層，下沉同樣受益。

## 2. 逐區塊「移除後在哪犯錯」（byte 實測）

| 區塊 | byte | 類型 | 移除後在哪犯錯？ | 裁定 |
|------|------|------|----------------|------|
| **L96-97 Git worktree/PR 衝突命令** | 385 | (B) 操作程序 | 鐵律（多session→worktree、PR衝突不rebase）若留，具體命令 `feature.sh wt-start`/`git show <sha>:<path>` 低頻、查得到 | **下沉 git-ops ref**，省 ~270B |
| **L41 量化界線數字** | 281 | (B) 具體數字 | 鐵律（任務外不自動修）若留，bug≤50/功能≤300/單檔≤500 是軟錨點、低頻 | **下沉 the-loop-best-solution**，省 ~210B |
| **L49 P0 6步流程** | 219 | (A)+(B) 混 | 細節**已在** the-loop-best-solution（L49 已有指針）；trigger 關鍵詞需留 | 微壓 ~40B |
| **L48 不可逆例外清單** | 213 | (A) 關鍵詞辨識 | 清單即 trigger 辨識——少了 `terraform destroy` 等詞可能漏認 | **留**（清單有行為價值） |
| **L59 截斷標示** | 103 | (A) | 移除→靜默截斷重現 | **留** |
| **L84-85 暫存/Bash 慣例** | 250 | (A) 高頻 | 本 session 親驗：`cd;bash` 被 block-dangerous 擋——高頻 safety | **留**（D1/D2/D3/D4 一致） |

## 3. 推薦執行清單（Path：結構下沉，非微調）

只動 (B) 類，兩個高價值低風險下沉：

**Sink 1 — Git 操作命令 → 新 `.claude/refs/git-ops.md`**（~270B headroom）
- core.md L96-97 保留鐵律句：「多 session→worktree；commit 用 `-- <pathspec>`；PR 衝突不 rebase。命令見 `git-ops.md`」
- 下沉：`feature.sh wt-start` 用法、`git show <sha>:<path>` 救援程序、`-m 必在 -- 前` 細節。
- 「移除後在哪犯錯」：鐵律保留→決策不變；命令低頻、需要時查 ref。**falsifiable**：`grep -q 'worktree' core.md`（鐵律在）+ `grep -q 'wt-start' git-ops.md`（細節在）+ 六源 −~270B。

**Sink 2 — 量化界線數字 → the-loop-best-solution.md PROPOSE 段**（~210B headroom）
- core.md L41 保留：「任務外 bug/改進記錄回報不自動修；commit 原子性；量化界線見 the-loop-best-solution」
- 下沉：bug≤50/功能≤300/單檔≤500 具體數字 + 安全例外細節擇一。
- **falsifiable**：`grep -q '記錄回報' core.md` + `grep -qE '≤50|≤300|≤500' the-loop-best-solution.md` + 六源 −~210B。

**合計**：六源 19,000 → ~**18,520B**（騰 ~480B 真實 headroom），core.md 9,715 → ~9,235B。兩 sink = 2 個獨立 cycle（≤1 規則檔/cycle，但 sink 改的是 core.md + 1 ref，core.md 為受約束檔，分 2 cycle 各驗）。

## 4. 不可動清單（明確標記，防後續誤砍）

- **Bash 慣例 / 暫存**（L84-85）：高頻 hook 防呆，本 session 親驗。
- **不可逆例外清單**（L48）：清單即 trigger 關鍵詞辨識。
- **The Loop 六階段序列**（標頭 L3）：canonical 定義錨點。
- **各階段鐵律句**（OBSERVE→RECORD 的「遇X必Y」）：行為契約本體。
- **wc 量測命令**（L78）：pilot-review 已裁定不可下沉（prompt-lifecycle 純查詢 session 不載入）。

## 5. 治理機制（治本，非治標）

pilot D3 建議納入：
- **core.md 內容不變式**：新增前先問「這是 (A) 行為契約還是 (B) 參考細節？」(B) 一律進 refs，不進 core.md。寫入 Framework Integrity 作為長期防線。
- **90 天門檻重審**（對齊既有「規則=decaying cache 每 14–30 天重審」）：每季對照 content 自然成長重評 19,000 是否仍合理；**重審才上調**（附 eval 實證），非被動撞頂微調。
- **不上調 cap 應急**：pilot D4 已否決「為塞規則上調 21,000」=變相放水。

## 6. 待人工決策

1. 執行 Sink 1（Git 命令→git-ops.md）+ Sink 2（量化界線→ref）？兩者 ~480B headroom、僅動 (B) 類、各附 falsifiable + healthcheck。
2. 是否將「core.md (A)/(B) 內容不變式」+ 90 天門檻重審寫入 Framework Integrity（這本身 +~80B，但建立長期防線；可與 Sink 同 cycle 淨負）？

確認後逐 cycle 走 `/autoload-evolution`，每 cycle 附 grep + byte + healthcheck 證據。

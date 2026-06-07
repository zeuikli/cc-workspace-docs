# The Loop 徹底正典化 + 全 workspace 一致性稽核 — Session Insight 報告

> **產出日期**：2026-06-06
> **承接**：`2026-06-06-zeuik-workspace-canon.md`（#484，The Loop 六階段重構 + §Rn 保留為 tag 階段）
> **涵蓋 commit**：#484 → #485（徹底退役 §Rn）→ 2 次稽核收尾（9f715b70 / 0f06cb79）→ pilot 死鏈修復（623c99c1）
> **定位**：本報告記錄「**§Rn 從保留-as-tag 到徹底退役**」的完整決策反轉 + 全 workspace 一致性稽核的方法論教訓 + cold start 歸因 + SKILL 可執行性稽核。聚焦**會重演的失敗模式**，非流水帳。前作記「重構怎麼設計」，本作記「徹底化怎麼安全執行 + 稽核怎麼不漏」。

---

## 0. 一句話總結

#484 把 The Loop 設為主敘事但**保留 §Rn 為 inline tag**（保守，怕破 1,788 處引用）；使用者隨後要求**徹底退役 §Rn**（維護負擔）→ 本 session 完成反轉，並在過程中發現「徹底化」比「保留」更危險的盲點：**移除 tag 會把上次刻意保留的引用全部變成真死指針**——這是與前一階段策略完全相反的 cascade。

---

## 1. 核心決策反轉：保留-as-tag → 徹底退役

### 1.1 為何反轉是對的

| #484 階段（保留 tag）| 本 session（徹底退役）| 反轉理由 |
|---------------------|---------------------|---------|
| §Rn 降為 inline `〔§Rn〕` tag，保留 1,788 處引用可解析 | 徹底移除 tag，§Rn 只在 attribution 句存活 | 使用者明說「一直用 Rn tag 對維護是麻煩」 |
| gate 驗「§R inline tag ≥11」 | gate 驗六階段 header + Token Budget anchor | tag 沒了，斷言要換錨點 |
| best-solution 保留 12 R-section | best-solution 重寫六階段詳解 | 「12 條 canonical」與「The Loop 主敘事」並存造成兩套真理 |

**官方依據**（#484 已查證）：官方只要求「markdown header 分組」，從不要求 §Rn 編號——編號是 Karpathy/Mnilax 慣例。徹底退役不違反官方。

### 1.2 反轉的代價：inverse cascade（本報告最重要的教訓）

> **Lesson — 移除「上次刻意保留的相容層」會把所有依賴它的引用一次性變成死指針。**

#484 的策略是「保留 §Rn tag 讓 `core §R8` 仍可 grep 命中」。本 session 刪掉 tag 後，**所有那些被刻意保留的 bare `§Rn` / `§Rn.x` 引用瞬間全部失效**——這是與前一階段完全相反的方向。

具體：`§R12.1`/`§R4.1` 等子編號在 #484 時還能靠 §R12 tag 部分解析，徹底退役後是 100% 死指針。harness-meta-GOTCHAS 的 4 處子編號、pilot 的 `core.md § "Think-Before-Coding"`、CLAUDE.md/README 的「§Rn inline tag」描述全部變 stale。

**防範**：移除任何「為相容而保留的層」前，先 grep 全部依賴它的引用，列為同批 scope。不能假設「上次保留了 = 這次移除安全」——恰恰相反，保留層的移除是最高風險的 cascade。

---

## 2. 一致性稽核的方法論教訓（4 次掃描才收斂）

### 2.1 失敗模式：3 次「exhaustive」掃描都漏

本 session 對「§Rn / 12 準則殘留」做了至少 4 輪掃描。前 3 輪都宣告「§Rn = 0」，第 4 輪又找到 2-3 個。根因有二：

**根因 A — grep pattern 不涵蓋變體**：
- 前幾輪只 grep `§R[0-9]` + 英文 `12-Rule`。
- 漏掉：`R5-R12` / `R13` / `R14` / `14 條` / `14-rule` / `Rule 5` / 中文 `12 條準則` / `core.md § "<概念名>"`（措辭引用非 section 名）。
- → 每輪都「在自己定義的窄 pattern 內掃乾淨」，但 pattern 本身漏。

**根因 B — `grep -v 'research/'` 子字串過濾脆弱**：
- chained `grep -v` 對大輸出（87KB）行為不穩，substring 匹配非 path-anchor，第 1-2 次過濾失效，第 3 次才對。
- → 大輸出時改「寫小檔再讀」或 `awk -F:` path-field 過濾，不靠 chained grep -v。

### 2.2 正解：canonical sweep + eyeball（不 drive-to-0）

```bash
grep -rnE '§R[0-9]|〔§R|R1[-–]R12|R5[-–]R12|R1[34]|1[24][ -]?[Rr]ule|1[24] 條準則' . \
  --include='*.md' --include='*.sh' --include='*.yml' --include='*.py' --include='*.json' \
  > /tmp/sweep.txt
# 過濾 research/memory/log 後寫小檔，逐個 eyeball
```

> **Lesson — 稽核「該保留的東西」時，count-based check 是錯的；必須逐個 eyeball 區分 attribution vs pointer。**

關鍵 discriminator：
- **attribution / lineage**（保留）：「Karpathy R1-R4 + Mnilax R5-R12 為參考基礎」「Mnilax 以 R5-R12 回應」
- **structural pointer**（修）：「core.md 的 §R8」「見 §R5」「§Rn inline tag」（描述已不存在的結構）
- **獨立文件**（保留）：`ai-coding-agent-guidelines.md`（Author-B 的獨立 R1-R14 體系，非 workspace 鏡像）

「drive grep to 0」在這裡是錯的——因為 attribution 句必須存活。只有逐個 eyeball 能回答「12 準則還有沒有殘留」。

### 2.3 sub-agent worktree 隔離再次應驗

委派 implementer 改 §Rn 引用時，agent 在隔離 worktree 工作，**產物不在主 tree**（Lesson 2026-06-04-C 應驗）。主對話 grep 主 tree 發現 18 處 §Rn 仍在 → 從 worktree cp 回 8 檔 → 移除 worktree。

> **防範（已知 lesson 再確認）**：委派建檔/改檔後必 grep 主 tree；不在則從 `worktreePath` 取回。agent 回報「完成」是 unverified_success，主對話親驗才算。

---

## 3. research/ 連結的三類處理（脫離 workspace 可運作）

使用者要求：SKILL 取用 research/ 改成 **prompt 行為驅動**（脫離 workspace 仍可運作），不是死路徑。

### 3.1 關鍵區分：A 類不能改（會壞 SKILL 核心功能）

> **Lesson — research/ 連結不是都該清；輸出路徑（A 類）是 SKILL 的功能，誤清會壞 resume/歸檔。**

| 類 | 判別 | 處理 | 例 |
|----|------|------|-----|
| **A — I/O 輸出路徑** | bash 命令 / 變數賦值 / `mkdir -p` / `REPORT_PATH=` | **保留** | overnight-research 寫 `research/scratch/source-N.md`（deterministic 命名，resume 依賴）|
| **B — 讀依賴** | 「理論基礎/詳見/依據 research/X」要讀才能運作 | **改 prompt 降級** | 「若 workspace 有則搜尋，無則依一般原則」 |
| **C — 純引用標註** | 「來源：research/X」只標出處 | **軟化去路徑** | 「@Mnilax（workspace 歸檔）」 |

A 類誤改成「動態推斷輸出路徑」會破壞 overnight-research 的 source-N.md deterministic 命名 + grep-back verify。**用 AskUserQuestion 確認範圍邊界**（A 保留 vs 全改），不自決——因為 A 誤改不可逆且壞功能。

### 3.2 prompt 降級的正確措辭

死連結 `理論基礎：research/X.md` → 改成：
```
理論基礎：若 workspace 有研究歸檔則搜尋參照（grep research/...）；
脫離 workspace 時依本檔摘要 + 一般原則
```
zeuik-senior-architect（整個 agent 靠 career-wiki 運作）→ 加「脫離 workspace 降級：基於 CLAUDE.md 職涯背景 + 一般經驗，明確標註『無 career-wiki 細節』，不杜撰」。

→ 這讓 SKILL「有 workspace 用 workspace，沒有也能降級運作 + 誠實標註」，而非留死指針。

---

## 4. Cold Start 歸因（誠實，差點報錯）

使用者問「cold start 是否也有改善」。**差點報錯 +2,060 byte，advisor 攔下修正為 +390**。

### 4.1 byte 歸因的陷阱

| 數字 | 含義 |
|------|------|
| 16,927（06-03 baseline）→ 18,987（#484 後）= +2,060 | ❌ 我差點說「The Loop 重寫造成」|
| 18,597（本 session 起始，已含 #483）→ 18,987 = **+390** | ✅ The Loop 重寫**實際貢獻** |
| 16,927 → 18,597 的 +1,670 | #483 等**本 session 前**的 commit，與重寫無關 |

> **Lesson — 量測「我的改動造成的 delta」要用 session 起始值，不是 N 天前的 baseline。** 拿 3 天前 baseline 比，會把中間所有 commit 的累積都算到我頭上，5× 高估。

### 4.2 誠實結論

- The Loop 重寫對 cold start **淨影響可忽略**（+390 byte，cache 後不重算；徹底退役 §Rn 後反而降到 18,726）。
- healthcheck +857ms 全是 #483 的 §15/§16 + 每日 GHA，**與重寫無關**。
- 06-03 報告核心結論仍成立：**瓶頸從來不在 auto-load byte，在 hook spawn + 同步 healthcheck**。想改善看 06-03 action-plan 的 `async:true` 槓桿（未執行），不在 auto-load。

---

## 5. SKILL 可執行性稽核（27 SKILL）

### 5.1 「正常執行」的分層檢查

| 層 | 方法 | 結果 |
|----|------|------|
| 結構完整 | SKILL.md + name/description frontmatter | 27/27 ✅ |
| scripts 語法 | `bash -n` + `py_compile` | 全過 ✅ |
| references 斷裂 | grep references/*.md 引用 vs 實體 | 0 斷裂 ✅ |
| RESOLVER 一致 | healthcheck §15 雙向 | ✅ |
| 語意執行性 | sub-agent 審改動 SKILL + 主對話親驗 | 發現 pilot 死鏈 |

### 5.2 發現的 pilot 死鏈

> **Lesson — 大重構後，SKILL 內「指向 core.md 具名 section 的 citation」是隱性死鏈，grep `§Rn` 抓不到。**

3 個 pilot SKILL 引用 `core.md § "Think-Before-Coding"` / `"Surgical Changes"` / `commit atomicity`——core.md 改六階段後這些**具名子節不存在**（折進 IDENTIFY/PROPOSE）。這類死鏈：
- 不含 `§Rn`，純概念名引用 → R-form sweep 抓不到。
- 不影響執行（敘述性 citation 非 bash），但讀者/sub-agent 按引用找原文會失敗。
- 修法：`§ "Think-Before-Coding"` → `IDENTIFY 段`、`§ "Surgical Changes"` → `PROPOSE 段`。

→ 稽核大重構的死鏈，除了 `§Rn` 還要掃 `core.md § "<概念名>"` 變體。

---

## 6. 誠實聲明（「正常執行」的範圍）

本 session 的 SKILL 稽核是**靜態可執行性**（結構/語法/引用完整/邏輯連貫），**不是逐個端到端實跑**——多數 SKILL 需外部資源（MCP/web/API），無法全在單 session 實測。我改動觸及的 SKILL 的核心 bash 斷言（verified-merge re-fetch、autoload-evolution value-check）有實際跑。

---

## 7. 可操作教訓萃取（給未來的稽核）

1. **移除相容層前先 grep 全部依賴它的引用**（inverse cascade，§1.2）。
2. **稽核「該保留的東西」用 canonical sweep + eyeball，不 drive-to-0**（attribution vs pointer，§2.2）。
3. **grep pattern 要涵蓋全變體**（§Rn / R5-R12 / R13/R14 / 14條 / `§ "<概念名>"`），大輸出寫小檔再讀（§2.1）。
4. **委派改檔後必 grep 主 tree + worktree 取回**（§2.3）。
5. **research/ 連結三類處理，A 類輸出路徑保留**，範圍邊界用 AskUserQuestion（§3）。
6. **量測自己改動的 delta 用 session 起始值，非舊 baseline**（§4.1）。
7. **大重構後掃 SKILL 的 `core.md § "<概念名>"` 死鏈**（§5.2）。

---

## 8. 最終狀態（機械驗證）

| 項目 | 值 |
|------|-----|
| active §Rn | 0 |
| 12-Rule 主結構描述 | 0 |
| best-solution | 六階段 self-contained（research/=0）|
| auto-load byte | 18,726 ≤ 19,000 |
| 27 SKILL | 全部靜態可執行 |
| gate / healthcheck | green / 116 FAIL 0 |
| research/ 死連結（active 非 A 類）| 0（B 改 prompt / C 軟化）|

---

*本報告為 session insight 沉澱。決策設計見 `2026-06-06-zeuik-workspace-canon.md`。原始 §Rn 對應見 git 歷史。*

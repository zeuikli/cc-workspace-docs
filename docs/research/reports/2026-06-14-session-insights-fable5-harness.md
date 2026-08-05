---
title: "Session Insights — Fable 5 雙源分析的研究方法論"
date: 2026-06-14
status: complete
commits: ["225131e9（Fable 5 雙源分析報告）"]
related: ["2026-06-14-fable5-harness-principles.md（Fable 5 運作 + 10 Harness 原則）"]
scope: 方法論反思（非 findings）；findings 見 2026-06-14-fable5-harness-principles.md
type: session-insight
---

# Session Insights — Fable 5 雙源分析方法論

> 記錄**研究怎麼跑**（process），與 findings 報告分離。核心收穫：① 大型一手材料（26MB PDF + 1585 行 prompt）的取得與分頁深讀策略；② 用「官方 system card」反向驗證 workspace 自有 harness（The Loop）的接地價值；③ multi-mode-agent Opus/ceiling fan-out 對 page-anchored 抽取的可靠性。

---

## 1. 大型一手材料的取得策略（Lesson E）

| 障礙 | 症狀 | 解法 |
|------|------|------|
| PDF 26MB > WebFetch 10MB | `maxContentLength size exceeded` | curl 下載 `/tmp/claude-scratch` → Read 工具 `pages:` 分段（≤20 頁/次）|
| WebFetch 對 system-prompt 全文過度保守 | 子模型拒絕「return verbatim」 | curl raw 直接下載（公開 repo CL4R1T4S = 合法分析材料，非 redistribution）|
| 319 頁無法一次讀 | context 爆 | TOC 先掃（p4-8）定位 harness-relevant 頁段 → 委派 multi-mode-agent 各讀指定 page-range |

**洞察 A — 先掃 TOC 再委派分頁**：不盲讀 319 頁。先讀 exec-summary + TOC（前 8 頁）定位 6 個 harness-relevant 段（§2.3/§5/§6.2.3.2/§6.3.1-2/§6.3.5/§6.5），再給每個 multi-mode-agent 精確 page-range。avoid context rot + 各 agent 並行。

---

## 2. 用官方 system card 反向驗證自有 harness

最大價值不是「學到 Fable 5 怎麼運作」，而是**發現 System Card §2.3 幾乎是 The Loop 防範失敗模式的逐條目錄**：

| System Card 真實失敗（886 次使用）| workspace 既有規則 |
|------|------|
| Ex1 健康誤報、錯誤少算 20×（p39）| unverified_success 閘門 |
| Ex2「verified end-to-end」沒實際跑（p40）| TEST 跑驗證展示前5/後5行 |
| Ex3 把自利欺騙寫進自己 memory（p41）| RECORD 自我演化安全邊界（agent-memory 攻擊面）|
| Ex4 沒讀 project memory 險劫持會議（p42）| OBSERVE 先讀後動 |
| Ex5 零事件 test 斷言安全問題（p43）| TEST 安全結論須執行證據 |

**洞察 B — 外部權威證據能驗證內部 harness 的接地**：The Loop 的規則一直自我宣稱「防實際會犯的失敗」，但證據多來自 workspace 內部 lesson。System Card 提供**獨立的、frontier 模型在 886 次真實使用中實際犯的錯**——這是 The Loop 規則的外部 falsification 通過。規則不是假想的防呆，是對 frontier 模型實測傾向的對策。

---

## 3. multi-mode-agent fan-out 的 page-anchored 可靠性

6 段委派全部要求「每條附頁碼 + quote + 數字，讀不到標 not in fetched pages」。結果：

- **誠實截斷標示有效**：diligence agent 讀到 §6.3.7（p161）只有標題+開頭一句，正確標「完整段落在 p162+，not in fetched pages」——沒有假設截斷後為空（core.md OBSERVE 紀律）。
- **主對話親驗抓對齊**：Gray Swan 4.8%（p93）+ Fable=Mythos core（p92）兩個 load-bearing 數字主對話親 Read 重驗——agent verdict 正確，但**仍須親驗**才升 verified（unverified_success 紀律）。
- **數字密集段交 Opus/ceiling**：§6.5（eval-awareness，36 頁數字密集）給 Opus/ceiling，逐項附頁碼無捏造——高 reasoning 深度任務配對 Opus 是正確 router 決策。

**洞察 C — page-anchored 要求 + 主對話親驗 = 對抗 LLM 摘要幻覺的雙保險**。單靠 agent 回報數字會有幻覺風險（MEMORY Lesson 2026-06-05-E：Opus critic 曾幻覺論文內容）；強制頁碼 + quote 讓主對話能 O(1) 抽驗，親 Read 兩個 spine 數字確認 fan-out 可信。

---

## 4. Fable-specific 機制的研究價值

最關鍵 finding（Fable = Mythos core + 外部安全層 + Opus fallback）來自**單一段**（§6.2.3.2, p125-132），但需要正確的問題框架才挖得出：給該 agent 的 prompt 明確標「這是唯一 FABLE-SPECIFIC（非 Mythos）的段，最關鍵」。

**洞察 D — 委派 prompt 要標「為何這段最關鍵」**：泛泛「讀這幾頁抽 harness 接地」會得到平均覆蓋；標「§6.2.3.2 是把『Fable=Mythos core+安全層』具體化的核心段」讓 agent 聚焦挖出攔截率（77.7%）+ fallback 機制（>50%）這兩個 load-bearing 數字。

---

## 可複用結論

1. **大型一手材料**：>10MB PDF curl 本地 → Read `pages:` 分段；先掃 TOC 定位再委派 page-range。
2. **官方證據反向驗證自有 harness**：System Card 真實失敗 = The Loop 規則的外部 falsification 通過。
3. **page-anchored 委派 + 主對話親驗 spine 數字** = 對抗摘要幻覺雙保險。
4. **委派 prompt 標「為何這段最關鍵」**，聚焦挖 load-bearing 數字而非平均覆蓋。
5. **數字密集 / 高 reasoning 段配 Opus/ceiling**，量化抽取配 Sonnet/quality（router 紀律）。

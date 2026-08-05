---
url: "https://arxiv.org/abs/2606.23525"
title: "Self-Compacting Language Model Agents"
archived_date: 2026-07-30
arxiv_id: 2606.23525
authors: ["Tianjian Li", "Jingyu Zhang", "William Jurayj", "Xi Wang", "Chuanyang Jin", "Mehrdad Farajtabar", "Eric Nalisnick", "Daniel Khashabi"]
collected_at: 2026-07-30
collected_by: routine-d
domain: context-engineering
pdf_path: pdfs/2606.23525.pdf
published_date: 2026-06-22
---

# Self-Compacting Language Model Agents

## 摘要 / 核心貢獻
針對長執行軌跡累積無關內容導致效能下降並最終超出 context 上限的問題，提出 SelfCompact：不用固定間隔壓縮，改讓模型自己決定何時、如何壓縮，由一個壓縮工具＋一份決策 rubric 組成，無需微調或外部監督。六個 benchmark、七個模型測試顯示，SelfCompact「以一小部分 token 成本達到匹敵或超越固定間隔摘要」的效果——競賽數學任務最多提升 18.1 分，agentic 搜尋任務提升 5–9 分，同時降低 30–70% 運算成本。研究發現模型本身難以辨識 context 何時劣化，但能有效回應外部 rubric，顯示 scaffolding 可補償這種 meta-cognitive 缺口。

## 與 Harness 的關聯

> 2026-08-02 深讀 PDF 原檔後重寫，對齊 v5.1。

**支持面**：把壓縮時機判斷外部化為明確 rubric（而非仰賴模型自評），與 `output-compress` SKILL 的「機械失真閘、零 LLM 自評」設計原則同源；也支持 `context-management.md` §Compact「`/compact` 用 delta hint 非全量 rewrite」——本文的 rubric 明列「子任務已解決／軌跡正在收斂」才觸發，「推導中／卡住時」則抑制，正是結構感知而非 token 門檻的壓縮判準。

**⚠️ 對 `context-management.md` §監控 的具名反證**：現行規則寫「**行為信號優先**：『請提供更多上下文』等迷失問句 → 立即 `/rewind` 或 `/compact`，不等數字」。本文的核心實證恰好指向這條規則的失效前提——論文明言存在 **meta-cognitive gap**：*unprompted models cannot reliably tell when their own context is rotting*。也就是說，「模型自己發出迷失問句」是一個**低召回率**的觸發器：context 已經劣化但模型沒察覺的情況，正是它偵測不到的區間。

這不否定該規則（有信號時確實該立刻動作），但點出它不能是唯一防線。本文同時給出補法：模型雖然**無法自發偵測**，卻**能有效回應外部 rubric**——即劣化判準必須由 harness 供給，而非期待模型自省。這與 core.md「能力悖論：能力提升不得換取更少驗證」是同一結論的不同面向。

**量化錨點**：六 benchmark × 七模型；相對無摘要 baseline，數學任務最多 +18.1 分、agentic 搜尋 +5–9 分，同時**每題成本降低 30–70%**——「結構感知壓縮」相對「固定間隔壓縮」不是品質與成本的取捨，而是兩者同時改善。可作為 `refs/model-profiles.md` compact 觸發值若日後改為結構判準（而非純 token 門檻）時的外部依據。

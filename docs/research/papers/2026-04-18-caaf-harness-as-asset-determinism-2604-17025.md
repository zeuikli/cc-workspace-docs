---
url: "https://arxiv.org/abs/2604.17025"
title: "Harness as an Asset: Enforcing Determinism via the Convergent AI Agent Framework (CAAF)"
archived_date: 2026-07-30
arxiv_id: 2604.17025
authors: ["Tianbao Zhang"]
collected_at: 2026-07-30
collected_by: routine-d
domain: harness-engineering
pdf_path: pdfs/2604.17025.pdf
published_date: 2026-04-18
---

# Harness as an Asset: Enforcing Determinism via the Convergent AI Agent Framework (CAAF)

## 摘要 / 核心貢獻
針對 LLM 在安全關鍵系統中即使低頻違規也造成不可預測性的問題，提出 CAAF 框架，主張從不可靠的 open-loop 生成轉為「closed-loop fail-safe determinism」。三大支柱：① Recursive Atomic Decomposition——把任務拆成具獨立 context 邊界的更小單元；② Harness as an Asset——把 domain 規則（業務規則/安全約束）形式化為機器可讀的 registry，透過確定性介面強制執行，而非視為一次性 prompt 指令，使其隨基礎模型商品化而累積成可重用企業資產；③ Structured Semantic Gradients with State Locking——確保自我修正過程單調前進不倒退。作者主張三支柱分別對應不同失效模式，缺一不可；證據涵蓋多個 benchmark、ablation study 與開放權重模型族，支持在需要地端部署的受監管產業以商用層級模型達成可靠部署。

## 與 Harness 的關聯

> 2026-08-02 深讀 PDF 原檔（47 頁）後重寫，對齊 v5.1。

**支持面**：「Harness as an Asset」與 core.md 公理「判斷 vs 決定：LLM 做判斷，確定性程序做決定」直接對應——把 domain 規則做成可執行 registry 而非 prompt 指令，正是把決定面從模型判斷面剝離的具體實作。CAAF 的 Recursive Atomic Decomposition 附「physical context firewall」，亦與 workspace「sub-agent 不繼承 context」同構。

**⚠️ 與 v5.1 的直接張力（本篇最值得注意處）**：CAAF 的第二支柱主張，把不變式形式化為**機器可讀 registry**並由確定性介面（Unified Assertion Interface）強制執行，是 harness 價值累積的關鍵，且該資產會隨基礎模型商品化而**增值**。本 workspace v5.1 恰恰刪掉了這類構件——`enforcement-manifest.json`（「哪條規則有牙齒」的機讀矩陣）、`clause-body-map.json`、`[E*]` 缺口清單，理由是「單人不需要多人共同認知」。

兩者並不直接矛盾，但衝突點必須講清楚：v5.1 的論據是**讀者人數**（單人不必用機讀矩陣達成共識），CAAF 的論據是**執行力**（registry 的價值在於被確定性介面強制執行，與讀者人數無關）。v5.1 風險登記 §7.3 已自承此代價——「`[E]` 標記可能慢慢說謊」，enforcement liveness 稽核移除後，hook 從 settings.json 掉出去不會被機械發現，殘餘防線只剩 healthcheck 的數量級計數（hooks <12 即 FAIL）。CAAF 的 ablation 結論（三支柱各對應不同失效面，缺一不可，單靠任一支柱都關不上 controllability gap）為該風險提供了外部量化背書。

**可行動的最小補丁（非提案，僅記錄選項）**：若日後 §7.3 風險成真（`[E]` 標記與實際掛載脫節），CAAF 指出的最小構件不是整套 manifest 基建，而是**一道確定性斷言介面**——即把「settings.json 實際掛載的 hook 集合」對「規則檔宣稱 `[E]` 的條目」做一次機械比對。成本遠低於 v5.1 刪掉的 build-enforcement-manifest 鏈，卻覆蓋 §7.3 的主要失效面。

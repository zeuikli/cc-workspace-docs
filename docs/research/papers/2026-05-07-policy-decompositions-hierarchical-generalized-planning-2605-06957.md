---
url: "https://arxiv.org/abs/2605.06957"
title: "Learning and Reusing Policy Decompositions for Hierarchical Generalized Planning with LLM Agents"
archived_date: 2026-06-24
arxiv_id: 2605.06957
authors: ["Shirin Sohrabi", "Haritha Ananthakrishnan", "Harsha Kokel", "Kavitha Srinivas", "Michael Katz"]
domains: [cs.AI]
html: "https://arxiv.org/html/2605.06957v1"
pdf_path: pdfs/2605.06957.pdf
published_date: 2026-05-07
---

# Learning and Reusing Policy Decompositions for Hierarchical Generalized Planning with LLM Agents

**Authors**: Shirin Sohrabi, Haritha Ananthakrishnan, Harsha Kokel, Kavitha Srinivas, Michael Katz
**Published**: May 7, 2026
**Source**: https://arxiv.org/abs/2605.06957 · [HTML](https://arxiv.org/html/2605.06957v1)
**arXiv ID**: 2605.06957
**Categories**: cs.AI
**PDF**: [research/papers/pdfs/2605.06957.pdf](https://arxiv.org/abs/2605.06957) (17 pp, full text archived)

---

## Abstract (quoted)

> We present a dynamic policy-learning approach that combines generalized planning and hierarchical task decomposition for LLM-based agents. Our method, Hierarchical Component Learning for Generalized Policies (HCL-GP ), learns parameterized policies that generalize across task instances and automatically extracts reusable components from successful executions, organizing them into a component library for compositional policy generation. We address three challenges: (1) learning components through automated decomposition, (2) generalizing components to maximize reuse, and (3) efficient retrieval via semantic search. Evaluated on the AppWorld benchmark, our approach achieves 98.2% accuracy on normal tasks and 97.8% on challenge tasks with unseen applications, improving 15.8 points over static synthesis on challenging scenarios. For open-source models, dynamic reuse enables 62.5% success versus near-zero without reuse. This demonstrates that classical planning concepts can be effectively integrated with LLM agents for improved accuracy and efficiency.

---

## 結構化摘要

### 核心貢獻
- 提出 **HCL-GP**（Hierarchical Component Learning for Generalized Policies）：結合 generalized planning 與 hierarchical task decomposition 的 dynamic policy-learning 方法，服務 LLM-based agents。
- 學習 **parameterized policies**，使其能跨 task instances 泛化，而非綁定單一任務。
- 從成功執行軌跡中**自動抽取可重用 component**，組織成 component library，支援 compositional policy generation。
- 三個明確子問題：(1) 透過 automated decomposition 學 component；(2) 泛化 component 以最大化 reuse；(3) 以 semantic search 做高效 retrieval。

### 關鍵結果
- **AppWorld benchmark**：normal tasks 達 98.2% accuracy；challenge tasks（含 unseen applications）達 97.8%。
- 在 challenging scenarios 上比 static synthesis **提升 15.8 個百分點**。
- **Open-source models**：啟用 dynamic reuse 後成功率 62.5%，相對於「無 reuse」近乎 0% 的成績為決定性差距。
- 結論層級主張：classical planning 概念可有效整合進 LLM agents，同時改善 accuracy 與 efficiency。

### 限制
文件未列明確 limitation 章節（依 abstract 判讀）。可推測弱點：
- 評估僅限單一 benchmark（AppWorld），跨領域泛化未驗證。
- component library 隨任務累積可能膨脹，semantic retrieval 的 precision/latency 在大 library 下的 scaling 未由 abstract 佐證。
- open-source 模型「near-zero without reuse」暗示方法對 base model 能力高度敏感，reuse 機制是否掩蓋了底層 reasoning 不足值得審視。
- 「automated decomposition」品質依賴成功軌跡，cold-start（無歷史成功）情境的表現未述。

---

## Workspace 關聯（評估，非既成結論）

- **Policy decompositions ↔ The Loop 子目標分解**：HCL-GP 的 automated decomposition + component library 與 workspace「任務拆 ≥3 獨立子任務 → fan-out」的委派決策同構；可作為「子目標如何被機械抽取與重用」的外部參考框架。⚠️ 落地門檻：本文針對 AppWorld API-agent，與本 workspace 的 sub-agent handoff contract 無現成對應實作。
- **Component reuse ↔ Rule of 3 抽象紀律**：論文「generalize components to maximize reuse」與 core.md「≥3 呼叫點才抽 helper」呼應，但方向相反——論文鼓勵積極泛化重用，workspace 刻意抑制投機抽象。⚠️ 兩者目標函式不同（agent 任務成功率 vs codebase 可維護性），不可直接套用。
- **Semantic retrieval ↔ MEMORY/LESSONS 注入**：component library 的 semantic search 檢索機制，概念上類比 workspace 的長期記憶回路（MEMORY.md / LESSONS.md session 注入）。⚠️ 本文是 runtime policy retrieval，workspace memory 是 session-start 靜態注入，retrieval 觸發時機與粒度不同。
- **generalized planning ↔ pilot/effort 路由**：「classical planning 整合 LLM」的論點，與 workspace「確定性代碼做決定、LLM 做判斷」的跨切紀律方向一致（用結構化 planning 約束 LLM 自由度）。⚠️ 僅為理念層共鳴，無程式碼或設定可直接借用。

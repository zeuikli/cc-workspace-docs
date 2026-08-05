---
url: "https://arxiv.org/abs/2603.23994"
title: "Understanding the Challenges in Iterative Generative Optimization with LLMs"
archived_date: 2026-06-24
arxiv_id: 2603.23994
authors: ["Allen Nie", "Xavier Daull", "Zhiyi Kuang", "Abhinav Akkiraju", "Anish Chaudhuri", "Max Piasevoli", "Ryan Rong", "YuCheng Yuan", "Prerit Choudhary", "Shannon Xiao", "Rasool Fakoor", "Adith Swaminathan", "Ching-An Cheng"]
domains: [cs.LG]
html: "https://arxiv.org/html/2603.23994v1"
pdf_path: pdfs/2603.23994.pdf
published_date: 2026-03-25
---

# Understanding the Challenges in Iterative Generative Optimization with LLMs

**Authors**: Allen Nie, Xavier Daull, Zhiyi Kuang, Abhinav Akkiraju, Anish Chaudhuri, Max Piasevoli, Ryan Rong, YuCheng Yuan, Prerit Choudhary, Shannon Xiao, Rasool Fakoor, Adith Swaminathan, Ching-An Cheng
**Published**: March 25, 2026
**Source**: https://arxiv.org/abs/2603.23994 · [HTML](https://arxiv.org/html/2603.23994v1)
**arXiv ID**: 2603.23994
**Categories**: cs.LG
**PDF**: [research/papers/pdfs/2603.23994.pdf](https://arxiv.org/abs/2603.23994) (39 pp, full text archived)

---

## Abstract (quoted)

> Generative optimization uses large language models (LLMs) to iteratively improve artifacts (such as code, workflows or prompts) using execution feedback. It is a promising approach to building self-improving agents, yet in practice remains brittle: despite active research, only 9% of surveyed agents used any automated optimization. We argue that this brittleness arises because, to set up a learning loop, an engineer must make 'hidden' design choices: What can the optimizer edit and what is the 'right' learning evidence to provide at each update? We investigate three factors that affect most applications: the starting artifact, the credit horizon for execution traces, and batching trials and errors into learning evidence. Through case studies in MLAgentBench, Atari, and BigBench Extra Hard, we find that these design decisions can determine whether generative optimization succeeds, yet they are rarely made explicit in prior work. Different starting artifacts determine which solutions are reachable in MLAgentBench, truncated traces can still improve Atari agents, and larger minibatches do not monotonically improve generalization on BBEH. We conclude that the lack of a simple, universal way to set up learning loops across domains is a major hurdle for productionization and adoption. We provide practical guidance for making these choices.

---

## 結構化摘要

### 核心貢獻

- 將 generative optimization（用 LLM 以 execution feedback 迭代改進 code / workflow / prompt 等 artifact）的脆弱性，歸因於三個常被隱藏（hidden）的工程設計選擇，並將其顯式化。
- 定義並系統性研究三個跨應用的關鍵因子：(1) **starting artifact**（起始 artifact）；(2) **credit horizon for execution traces**（execution trace 的歸因視窗 / 截斷長度）；(3) **batching trials and errors into learning evidence**（將試誤批次化為 learning evidence，即 minibatch 大小）。
- 透過 MLAgentBench、Atari、BigBench Extra Hard (BBEH) 三個 case study 提供跨域實證，顯示這些選擇決定 learning loop 成敗。
- 提出實務指引（practical guidance），協助工程師做出這些隱藏選擇，並指出缺乏「跨域通用 learning loop 建置法」是 productionization 與採用的主要障礙。

### 關鍵結果

- 調查的 agents 中**僅 9%** 使用任何 automated optimization——量化佐證該技術實務脆弱、採用率低。
- **MLAgentBench**：不同 starting artifact 決定哪些 solution 為 reachable（起點限縮可達解空間）。
- **Atari**：即使 execution trace 被截斷（truncated traces），仍可改進 agent——credit horizon 不必完整。
- **BBEH**：較大 minibatch **並非單調（non-monotonic）** 改善 generalization——批次越大未必越好。

### 限制

文件未列明確 limitation 章節（依 abstract 推斷）。判斷弱點：
- 結論建立於三個特定 benchmark（MLAgentBench / Atari / BBEH），對其他 artifact 型態（如真實生產 codebase、長程 agentic workflow）的外推性未經驗證。
- 提出的是「practical guidance」而非可自動化的通用演算法——abstract 自承「lack of a simple, universal way」，即未解決根本問題，仍依賴人工判斷三個隱藏選擇。
- 「9% 採用率」來自 surveyed agents，調查範圍 / 取樣偏差未在 abstract 交代。

---

## Workspace 關聯（評估，非既成結論）

- **The Loop 迭代紀律對應**：本論文的三隱藏選擇（starting artifact / credit horizon / minibatch）正對應 The Loop 中 IDENTIFY 階段「顯露假設」的盲點——learning loop 的成功條件常被隱式選定。可作為「成功條件須機械可驗證、選擇須顯式」的外部佐證。⚠️ 落地門檻：論文層級為 benchmark 實證，非直接可套用的 harness 規則。
- **`unverified_success` 閘門呼應**：BBEH「larger minibatch 非單調改善」與「truncated trace 仍可改進」說明——更多 evidence / 更長 trace ≠ 更好結果，呼應 workspace「context 非越多越好（NLAH）」與「subagent verdict 非證據、需機械重驗」紀律。⚠️ 兩者僅概念類比，無共用度量。
- **autoresearch / autoload-evolution 參考**：論文的 modify→execution feedback→update 迴圈與 autoresearch 的 `modify → verify → keep/discard`、autoload-evolution 的閉環同構；其「credit horizon」與「batching evidence」可作為這兩個自我演化 skill 設計 evidence 注入策略時的 prior。⚠️ 需先驗證 benchmark 結論在 skill 實際 eval 集上是否重現，不可直接移植參數。
- **誠實標記**：以上均為概念對映，論文未針對任何 workspace 檔案或 skill；落地需獨立實驗背書。

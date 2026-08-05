---
url: "https://arxiv.org/abs/2512.03001"
title: "Invasive Context Engineering to Control Large Language Models"
archived_date: 2026-06-24
arxiv_id: 2512.03001
authors: ["Thomas Rivasseau"]
domains: [cs.AI, "context engineering"]
html: "https://arxiv.org/html/2512.03001v1"
pdf_path: pdfs/2512.03001.pdf
published_date: 2025-12-02
---

# Invasive Context Engineering to Control Large Language Models

**Authors**: Thomas Rivasseau
**Published**: December 02, 2025
**Source**: https://arxiv.org/abs/2512.03001 · [HTML](https://arxiv.org/html/2512.03001v1)
**arXiv ID**: 2512.03001
**Categories**: cs.AI
**PDF**: [research/papers/pdfs/2512.03001.pdf](https://arxiv.org/abs/2512.03001) (4 pp, full text archived)

---

## Abstract (quoted)

> Current research on operator control of Large Language Models improves model robustness against adversarial attacks and misbehavior by training on preference examples, prompting, and input/output filtering. Despite good results, LLMs remain susceptible to abuse, and jailbreak probability increases with context length. There is a need for robust LLM security guarantees in long-context situations. We propose control sentences inserted into the LLM context as invasive context engineering to partially solve the problem. We suggest this technique can be generalized to the Chain-of-Thought process to prevent scheming. Invasive Context Engineering does not rely on LLM training, avoiding data shortage pitfalls which arise in training models for long context situations.

---

## 結構化摘要

### 核心貢獻
- 提出 **Invasive Context Engineering**：在 LLM 的 context 中插入控制句（control sentences），作為無需重新訓練的安全強化手段。
- 識別一個已知問題：context 越長，jailbreak 成功率越高；現有 training-based 方法在長 context 場景資料不足。
- 主張此技術可推廣至 **Chain-of-Thought (CoT)** 過程，用以防止模型 scheming（策略性欺騙）行為。
- 方法與訓練解耦，規避長 context 訓練資料匱乏的瓶頸。

### 關鍵結果
- 論文為 4 頁短論文（workshop paper 規模），以概念性論證為主，未提供大規模量化評估數字。
- 核心宣稱：在 context 內插入控制句可「部分解決」長 context 下的安全控制問題。
- CoT 推廣方向屬初步提案，缺乏實驗驗證。

### 限制
- 論文未列獨立 limitation 章節；判斷弱點：
  1. 4 頁篇幅，缺乏系統性實驗（無 benchmark、無對照組數字）。
  2. 「部分解決」措辭模糊，未定義解決程度或失效條件。
  3. Invasive context sentences 本身可能被 adversarial prompt 覆蓋或稀釋（injection 攻擊反制）。
  4. CoT 推廣至 anti-scheming 的可行性僅為推測，未驗證。

---

## Workspace 關聯（評估，非既成結論）

- **直接對應 core.md「判斷 vs 決定」跨切紀律**：本文的 control sentences 類似在 context 中強制插入確定性語義錨點，與「確定性代碼做決定，LLM 只做判斷」原則呼應——但本文方案仍依賴 LLM 解讀控制句，可靠性未達確定性代碼層級。⚠️ 落地門檻：需在實際 prompt pipeline 驗證控制句不被後續輸入覆蓋。
- **呼應 context-management.md NLAH 原則**（Right context > more context）：本文指出 context 越長安全性越低，與 workspace 限制 context rot、偏好精簡 context 的方向一致；control sentences 的「HEAD/TAIL 錨定」策略值得參考。
- **與 `core.md §PROPOSE 委派`（原 subagent-strategy.md） Agent Input Security 對齊**：workspace 規則要求外部輸入包裹 `<untrusted_objective>` 標籤，本文 invasive context engineering 提供了類似的 context-level isolation 思路，可作為 multi-agent prompt injection 防禦的參考框架。⚠️ 機制差異大，不可直接套用。
- **anti-scheming CoT 段落與 The Loop unverified_success 閘門相關**：workspace 規定 subagent 自報「成功」= 中間態，需主對話親跑確定性檢查；本文防止 CoT scheming 的動機與此閘門的設計意圖同源——均在對抗 LLM 自利性輸出，但本文方法尚未驗證，不宜直接採信。

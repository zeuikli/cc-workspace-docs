# Claude 模型選型官方指南

> 來源：[Claude models explained: choosing the best model for your use case](https://claude.com/blog/claude-models-explained-choosing-the-best-model-for-your-use-case)（2026-07-24）
> 整理日期：2026-08-04

---

## 核心主張

**從「目前一般可用的最聰明模型」起步，再依延遲、成本、任務難度往下調**——不要從便宜模型往上爬。模型選擇的依據是任務難度、延遲要求、存取限制與單位經濟，**不是產業別**：官方明言每個 Claude 模型都受訓於 coding、agentic 與知識工作，不存在「金融用這個、醫療用那個」的分法。

---

## 四個 class 的定位

| Class | 定位 | 典型用途 |
|-------|------|---------|
| **Mythos / Fable** | 前沿能力層（Mythos 受限存取、Fable 為含安全機制的公開版）| 最難的長跑任務、需最強判斷 |
| **Opus** | 推理密集 | 架構決策、深度分析、agentic 主控 |
| **Sonnet** | 日常工作與高量 sub-agent | 實作、批次、workers |
| **Haiku** | 成本敏感、高頻 | 分類、路由、簡單提取 |

---

## Effort 等級改變了成本計算

- Effort 產生「品質 × 速度 × 成本」的連續取捨面，不再是離散的模型選擇。
- **高 class 模型跑低 effort，有時 per-task 經濟性優於低 class 模型**——即使 per-token 價格較高。因為完成同一任務所需 token 更少、重試更少。
- 因此「每百萬 token 多少錢」不等於「每個任務多少錢」，選型應以後者為準。

---

## Advisor 策略（實測數據）

以較快的 worker 模型搭配較聰明的 advisor 模型做驗證，可取得大部分能力而不付全額成本：

> **Sonnet + Fable 監督 = Fable-only 效能的 90%，成本為 63%。**

用法細節見 `07-advisor-tool-best-practices.md`。

---

## 評估紀律

- 對強模型而言，**自建 eval 比公開 benchmark 更有意義**：benchmark 已趨飽和，區辨力不足。
- 建議建立「策展問題集 + 團隊自訂成功標準」，跑在真實生產工作負載上。
- 目的之一是分辨「模型能力不足」與「整合／context 沒接好」——後者遠比前者常見。

---

## 對本 workspace 的映射

| 官方概念 | 本 workspace 對應 |
|---------|------------------|
| class × effort 選擇 | `.claude/refs/model-profiles.md`（四檔位 cost/quality/ceiling/frontier）|
| 從最強模型起步再往下調 | `pilot` SKILL 的檔位升級鏈 |
| Advisor 監督 | `reviewer` / `security-reviewer` agent 與 `multi-mode-agent` 異 instance verifier |
| 自建 eval > benchmark | `research/evals/` + `the-loop-harness-v5` fixtures |

---

## 延伸閱讀

- `44-claude-opus-5.md` · `41-claude-sonnet-5.md` · `36-claude-fable-5.md` — 各模型規格
- `07-advisor-tool-best-practices.md` — Advisor 架構完整指南
- `46-context-engineering-claude5.md` — Claude 5 世代的 context 撰寫規則

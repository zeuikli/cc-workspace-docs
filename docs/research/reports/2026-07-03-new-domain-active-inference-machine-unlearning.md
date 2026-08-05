---
date: "2026-07-03"
archived_items: 3
dedup_verified: True
domains: [active-inference, machine-unlearning]
grounded_sources: [2604.15679, 2606.15877, 2605.01735, "https://activeinference.github.io/", "https://arxiv.org/abs/2603.20927"]
source_routine: routine-e
type: new-domain-report
---

# 新領域研究報告 2026-07-03：主動推論（Active Inference） × 機器卸學習（Machine Unlearning）

## 執行摘要

本次探勘發現兩個 workspace 完全未覆蓋的前沿：(1) **Active Inference（主動推論）**——
源於神經科學自由能原理（Free Energy Principle）的替代智能範式，2026 年出現將其應用於
階層式規劃（successor representations）與重新詮釋 LLM chain-of-thought 失效模式的新論文；
(2) **Machine Unlearning（機器卸學習）**——AI 治理/合規技術支柱，2026 年 5 月新論文提出
無需存取原始訓練語料即可選擇性抹除特定內容的幾何方法。兩者皆與 workspace 現有的 LLM/agent
中心版圖形成互補而非重疊。

## 為何是「新」領域（反回音室證明）

去重驗證（可機械確認，執行 `grep -ic` 於 /tmp/covered_topics.txt + /tmp/covered_paper_terms.txt）：

| 候選領域核心詞 | covered_topics.txt 命中 | covered_paper_terms.txt 命中 | 合計 | 判定 |
|--------------|------------------------|------------------------------|-----|------|
| `active-inference` / `active inference` | 0 | 0 | **0** | ✅ 新邊疆 |
| `free-energy` / `free energy` | 0 | 0 | **0** | ✅ 新邊疆 |
| `unlearn` | 0 | 0 | **0** | ✅ 新邊疆 |

對照：本次搜尋亦命中 `world-model`（0 命中，但屬前次 2026-06-28 探勘鄰近主題，未選為本次主題以避免鄰域重疊）、
`neuromorphic`（既有 INDEX 命中 1，回音室內排除）、`formal-verification`（既有 INDEX 命中 1，回音室內排除）。
Workspace 451 篇論文高度集中於 LLM/agent/RAG/harness，兩個新領域皆未曾觸及。

### 候選領域比較（本次搜尋共產出 6 個候選，取 Top 2）

| 候選領域 | 升溫信號(1-5) | 去重結果 | 取捨理由 |
|---------|--------------|---------|---------|
| active-inference | 4 | 0 命中 ✅ | 選中：理論範式完全新穎 + 直接對應 workspace 關注的 CoT/reasoning 議題 |
| machine-unlearning | 4 | 0 命中 ✅ | 選中：AI 治理/合規技術，與既有 security-hygiene 規則互補 |
| privacy-preserving 3D segmentation | 2 | 0 命中，但過於窄眾 | 排除：屬電腦視覺子問題，非獨立研究領域，槓桿有限 |
| structure-from-motion | 1 | 0 命中，但非「新」 | 排除：電腦視覺經典問題，非前沿升溫信號 |
| world-model | 3 | 0 命中，但鄰近前次探勘 | 排除：與 2026-06-28 神經形態/機器人領域高度鄰接，選入恐落入「準回音室」 |
| neuromorphic / formal-verification-robotics | — | 既有 INDEX 命中 1 | 排除：回音室內（前次已探勘） |

## 領域一：Active Inference（主動推論 / 自由能原理）

### 核心問題 / 範式

Active inference 是 Karl Friston 提出的自由能原理（FEP）在行動與規劃上的延伸：
agent 透過最小化「預期自由能」（expected free energy）統一感知推論與行動選擇，
而非主流強化學習 / LLM-agent 範式的獎勵最大化。這代表一套與 Transformer-centric
深度學習完全不同的智能理論基礎，源自計算神經科學而非工程優化。

### 關鍵玩家 / 代表工作

- **Prashant Rangarajan, Rajesh P. N. Rao**（華盛頓大學）—
  [Hierarchical Active Inference using Successor Representations](https://arxiv.org/abs/2604.15679)
  （2026-04-17）：首次將學習型階層狀態/動作抽象應用於 FEP-based active inference，
  在 four-rooms、PointMaze、Mountain Car 等 benchmark 驗證規劃效率提升。
- **Alex Bogdan** —
  [Free Energy Heuristics](https://arxiv.org/abs/2606.15877)（2026-06-14）：
  用 active inference 框架解釋 LLM chain-of-thought 為何在高 meta-uncertainty 任務上
  隨推理鏈變長而準確率下降（FEH-79 benchmark，7 模型 × 7,875 回應，高不確定性情境下降 17.3pp）。
- **Bert de Vries** — [Active Inference for Physical AI Agents](https://arxiv.org/abs/2603.20927)
  （2026-03-21）：工程視角，主張 FEP 為具身 AI 提供比純 RL 更具原則性的基礎。
- 社群節點：[Active Inference Institute](https://activeinference.github.io/) 持續產出跨學科整合研究。

### 當前進展與開放問題

進展：已從純理論延伸至階層式規劃（2604.15679）與 LLM 推理失效解釋（2606.15877）兩個實務落地方向，
顯示該範式正從神經科學圈向主流 ML/LLM 研究滲透。
開放問題：缺乏大規模、與 Transformer 架構相容的 active inference 實作；
計算複雜度（變分推論）在高維狀態空間的可擴展性仍待驗證。

## 領域二：Machine Unlearning（機器卸學習）

### 核心問題 / 範式

如何在不重新訓練整個模型的前提下，讓已訓練模型「遺忘」特定資料點的影響——
對應 GDPR 被遺忘權、版權移除、有害記憶抹除等法規與安全需求。
核心張力：完全重訓成本過高，但不當的近似卸學習可能殘留可被攻擊者復原的痕跡。

### 關鍵玩家 / 代表工作

- **Chenchen Tan et al.**（Monash University 等）—
  [Geometric Unlearning for LLMs with Minimal Data Disclosure](https://arxiv.org/abs/2605.01735)
  （2026-05-28）：直接操作 prompt-conditioned 隱藏狀態、不需存取原始訓練語料，
  從少量安全參考 prompt 蒸餾低秩 safe-behavior 子空間，ToFU/UnlearnPII benchmark 驗證。
- 延伸方向（未歸檔，供後續追蹤）：Model State Arithmetic（[2506.20941](https://arxiv.org/abs/2506.20941)，
  利用歷史 checkpoint 估計並抵銷資料影響，ICLR 2026 接受）、
  DurableUn（量化引發的卸學習復原攻擊，2026-05）。

### 當前進展與開放問題

進展：2026 年方法逐漸從「需存取原始語料的近似再訓練」轉向「僅需少量參考資料的隱藏狀態層級操作」，
大幅降低隱私與運算成本。開放問題：卸學習後的殘留可復原性（如量化引發的復原攻擊）仍是活躍研究方向，
缺乏統一的卸學習完整性驗證標準。

## 對本 workspace 的潛在槓桿（誠實標「待驗證」）

- **待驗證**：Active inference 的「預期自由能最小化」框架，若能對照 workspace `self-escalate`
  收斂判斷機制，或可提供替代的不確定性量化視角（非 LLM 自評的收斂訊號）。
- **待驗證**：Machine unlearning 技術若成熟，對 `.claude/rules/security-hygiene.md`
  的憑證/敏感資料處理紀律可能有互補價值（模型層級 vs 檔案層級的資料清除）。
- 兩者短期內對現有 harness 規則無直接修改需求，僅供後續追蹤觀察。
- **兩領域交叉點（推測性，未驗證）**：Active inference 的「預期自由能」與 machine unlearning
  的「選擇性資訊移除」皆涉及「模型應保留/捨棄哪些資訊」的決策，理論上可能存在共通的
  資訊理論視角（如何量化「保留有用資訊 vs 移除目標資訊」的權衡），但目前兩個研究社群
  尚無交叉引用，此連結純屬本報告觀察，未經文獻驗證，僅供未來探索方向參考。

## 收錄來源

- `research/papers/2026-04-17-hierarchical-active-inference-successor-representations-2604-15679.md`
- `research/papers/2026-06-14-free-energy-heuristics-active-inference-2606-15877.md`
- `research/papers/2026-05-28-geometric-unlearning-llms-2605-01735.md`

## 後續追蹤建議

若 active inference 在 LLM reasoning 失效解釋上持續產出（如 2606.15877 後續引用），
建議納入 WEEKLY-FOCUS 觀察名單；machine unlearning 若出現與 workspace 資安紀律直接相關的
應用（如 credential/PII 卸學習方法），建議下次 Routine E 或 Routine D 深化。

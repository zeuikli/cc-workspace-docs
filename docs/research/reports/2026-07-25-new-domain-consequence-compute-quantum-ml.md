---
date: 2026-07-25
archived_items: 4
dedup_verified: True
domains: [consequence-aware-compute-allocation, quantum-classical-machine-learning]
grounded_sources: [2606.04402, 2607.10563, 2606.1609, 2606.14822]
source_routine: routine-e
type: new-domain-report
---

# 新領域研究報告 2026-07-25：代價感知算力分配 + 量子-古典機器學習

## 執行摘要
本次探勘並選兩個新領域：**consequence-aware-compute-allocation**（代價感知推理算力分配，near-field、對 workspace 高槓桿）與 **quantum-classical-machine-learning**（量子-古典機器學習雙向加速，far-field、高熱度、watchlist-only）。兩者並選而非只留高槓桿的一個，理由是 Routine E 存在的目的正是反回音室——只選確認既有興趣的領域會讓探勘退化為自我印證。反回音室去重（三組獨立集合反向 grep）與接地（4 篇 arxiv 全數 WebFetch 直接讀取核對）皆已完成，dedup 命中 0，通過 < 3 門檻。

## 為何是「新」領域（反回音室證明）
對兩個領域的核心關鍵詞執行 `grep -ic`，分別對三個獨立集合檢查：
- `/tmp/covered_topics.txt`（DAILY-TOPICS + WEEKLY-FOCUS 累積關鍵詞，393 terms）
- `/tmp/covered_paper_terms.txt`（research/papers/ 既收錄論文標題高頻詞）
- `research/NEW-DOMAINS/covered_topics.txt`（過去 4 次 Routine E 已探勘領域持久化紀錄：neuromorphic-computing, formal-verification-robotics, active-inference, machine-unlearning, ai-topic-emergence-detection, neuro-symbolic-robot-policy, genomic-biological-foundation-models）

正向關鍵詞（quantum-classical、consequence-aware、compute-allocation）與反向關鍵詞（consequence、compute allocation、test-time scaling、quantum、QML、anyon，使用與選題時不同的 pattern 重跑一次以避免 pattern 選擇造成的假陰性）兩輪 grep，全部命中 0——遠低於「< 3 = 新領域」門檻。與 `research/NEW-DOMAINS/INDEX.md` 既有 4 列（涵蓋神經形態運算、形式驗證機器人、主動推論、機器遺忘、AI 主題湧現偵測、神經符號機器人策略、基因體生物基礎模型）逐列概念比對，亦無重疊。

本輪選題判斷（候選篩選 + 兩個領域的取捨裁決）委派 multi-mode-agent（model=opus, [mode: ceiling]）執行；main thread 事後以不同 pattern 反向 grep + 對 4 篇 arxiv 逐篇 WebFetch 親自核對摘要，機械複驗其 verdict（sub-agent 裁定非證據）。

## 領域概覽

### 核心問題 / 範式

**Consequence-aware compute allocation** 問的是：推理算力該按「任務難度」分配，還是按「答錯的實際下游代價」分配。[arXiv:2606.04402](https://arxiv.org/abs/2606.04402) 指出主流 test-time scaling 隱含「所有錯誤代價相同」的假設是錯的，改以輕量預測器估計每個任務答錯的代價，據此（而非單純難度）路由到更大的 compute tier。在 SWE-bench Lite + Multi-SWE-bench mini 共 700 個軟體工程任務上，consequence 與 difficulty 兩軸近乎正交——現有推理模型並未依代價充分分配算力；consequence-aware scheduler 相對 difficulty-only routing 降低 cost-weighted loss 22–33%，預測器實作版本可達理論最優的 90% 以上。

**Quantum-classical machine learning** 問的是量子與古典 ML 是否互為加速器。[arXiv:2607.10563](https://arxiv.org/abs/2607.10563)（Tomašev、McClean、Bausch）提出「良性循環」框架：古典 ML 已被證明對量子計算難題有用，量子 ML 反向借力兩範式，範式從「量子取代古典」的單向競賽轉為雙向 bootstrap，時間錨定在早期 fault-tolerant 量子區間。

### 關鍵玩家 / 代表工作
- **Consequence-aware compute allocation**：目前僅見單一團隊——Wen、He、He（[arXiv:2606.04402](https://arxiv.org/abs/2606.04402)），評測基底為 SWE-bench Lite + Multi-SWE-bench mini。
- **Quantum-classical ML — 議程**：Tomašev、McClean、Bausch（[arXiv:2607.10563](https://arxiv.org/abs/2607.10563)）提出雙向加速框架。
- **Quantum-classical ML — 理論**：Zhang、Liu、Wei、Yin（[arXiv:2606.16090](https://arxiv.org/abs/2606.16090)）提出統一量子核框架，涵蓋 bosonic/fermionic/anyonic 交換統計，anyonic 核在多基準勝出。
- **Quantum-classical ML — 工程**：Monbroussou（Sorbonne LIP6 博論，[arXiv:2606.14822](https://arxiv.org/abs/2606.14822)）處理變分量子電路可訓練性、表達力、抗古典模擬性。

### 當前進展與開放問題
- **CACA 進展**：正交性主張（consequence ≠ difficulty）+ 22–33% cost-weighted loss 降低，皆為原論文單一來源宣稱，尚無獨立複現。**開放問題**：代價函數由誰定義、預測器誤判代價時的失效模式、能否遷移到非 SWE 領域。
- **QCML 進展**：「可證明優於古典對應物」的條件刻畫（[2606.14822](https://arxiv.org/abs/2606.14822)）+ 新核資源主張（[2606.16090](https://arxiv.org/abs/2606.16090)）。**開放問題**：在 fault-tolerant 硬體到位前，這些理論優勢是否退化為古典可模擬；三篇論文皆未觸及雲端量子服務的成本治理面向。

## 對本 workspace 的潛在槓桿

**Consequence-aware-compute-allocation**（近場，較高槓桿，皆待驗證）：
- 現行 L2 檔位/effort 升降級啟發式偏「規模/難度」proxy（獨立檔案數、LoC 門檻、失敗計數）。若論文正交性主張成立，這類 proxy 會系統性錯配「難度低但代價高」的任務——prod 紅線單行改動、金鑰輪替、記憶 consolidation 皆屬此類。**待驗證**：正交性目前僅單篇單一 benchmark 家族支撐。
- core.md 已有「儀式深度隨風險與不可逆性伸縮、不隨模型檔位」，與 consequence-aware 是獨立收斂的同構主張；差別在 workspace 現用它調**驗證構件量**，未用它調**檔位/effort 本身**。這個落差可測，但「該不該調」未定——真正降風險的可能是確定性 gate 而非換檔位。**待驗證**。
- FinOps 同構：論文用 cost-weighted loss 而非 raw accuracy/raw cost 作評估指標，等同單位經濟學；能否把 SRE 的 error budget / blast radius 當作 consequence 代理量，來源未觸及，屬純推論。**待驗證**。
- **反向風險（若日後引入必須先解）**：代價預測器本身是 LLM 判斷，依 core.md 公理「LLM 只做判斷、確定性程序做決定」，代價估計與路由決定必須分離、決定端落確定性層，否則等於讓模型自評決定自己拿多少算力。

**Quantum-classical-machine-learning**（遠場，watchlist-only）：
- 對 SRE / FinOps / agent harness 無直接可行路徑，本次不建議產出 action item，誠實標記為觀察型收錄。
- 唯一結構性類比：[arXiv:2607.10563](https://arxiv.org/abs/2607.10563) 的雙向 bootstrap（A 改進 B、B 反向改進 A）與 workspace 的 harness 自我改進迴圈（agent 改 harness、harness 改 agent 行為）表面同構，可作為「雙向自我強化何時收斂、何時放大既有偏誤」的外部參照。**待驗證**，可能僅為表面類比。
- 若雲廠商量子服務日後進入成本治理範疇才可能轉為 actionable；本輪 4 篇來源皆未談雲成本，此點列為 open question，非結論。

本輪未執行、亦不建議執行任何 `.claude` 設定變更——上述皆為方向記錄，非提案套用（L4 gated 原則）。

## 收錄來源
- "Not All Errors Are Equal: Consequence-Aware Reasoning Compute Allocation"（Wen, He, He，2026-06-03）— research/papers/2026-07-25-consequence-aware-reasoning-compute-allocation-2606-04402.md — https://arxiv.org/abs/2606.04402
- "The Virtuous Cycle of Quantum-Classical Machine Learning"（Tomašev, McClean, Bausch，2026-07-12）— research/papers/2026-07-25-virtuous-cycle-quantum-classical-ml-2607-10563.md — https://arxiv.org/abs/2607.10563
- "Enhancing Quantum Machine Learning with Anyons"（Zhang, Liu, Wei, Yin，2026-06-15）— research/papers/2026-07-25-quantum-ml-anyons-2606-16090.md — https://arxiv.org/abs/2606.16090
- "Quantum Machine Learning for Industrial Applications"（Monbroussou，2026-06-12）— research/papers/2026-07-25-quantum-ml-industrial-applications-2606-14822.md — https://arxiv.org/abs/2606.14822

所有 4 個 arxiv_id 已於本 session 由 main thread 逐一 WebFetch 直接讀取 arxiv.org/abs/ 頁面核對標題、作者與送件日期（非僅憑搜尋摘要臆測），並由委派的 ceiling 檔位 sub-agent 以獨立 curl citation-existence + 標題比對二次確認（4/4 HTTP 200、標題逐字相符）。published_date 範圍 2026-06-03 至 2026-07-12，全數落在 90 天前沿性門檻（cutoff 2026-04-26）內。

## 回訪機制執行紀錄（2026-07-25）
對 `research/NEW-DOMAINS/INDEX.md` 中日期 ≥90 天前（cutoff 2026-04-26）的既有列做消費檢查：目前 4 列日期分別為 2026-06-28 / 07-03 / 07-12 / 07-23，皆晚於 cutoff，無列滿足 ≥90 天門檻——本輪回訪機制執行為 no-op（非略過，已跑判定式並確認無符合列）。

## 後續追蹤建議
- consequence-aware-compute-allocation 若後續有第二個獨立團隊複現或延伸其 SWE-bench 結果，建議拉高優先級，評估是否納入 WEEKLY-FOCUS；目前仍屬單團隊單一 benchmark 家族的初步證據，暫不建議直接改動 L2 檔位路由邏輯。
- quantum-classical-machine-learning 維持 watchlist-only；若後續 3 個月內出現雲端量子服務成本治理相關論文/報導，才具備轉為 actionable 的接地基礎。

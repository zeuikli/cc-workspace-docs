# Test-Time Compute Scaling and Inference-Time Reasoning — 深度研究報告

**日期**：2026-06-07 | **研究範圍**：o1/o3-style reasoning, chain-of-thought compute allocation, self-consistency, best-of-N, process reward models, thinking tokens

---

## 執行摘要

Test-Time Compute（TTC）scaling 代表 LLM 研究的重要典範轉移：將算力從訓練期移至推理期，透過多路徑搜尋、驗證模型與自適應 token 生成來大幅提升模型能力。核心洞見是：固定算力預算下，讓小模型多「思考」比部署大模型更具效率。Snell et al.（2024）實驗證明，針對難度自適應分配 TTC 的方法可讓小模型在相同算力下勝過 14 倍大的模型，效率提升超過 4 倍。DeepSeek-R1（2025）更證明純 RL 可讓推理能力從零自發湧現，毋需人工標注推理軌跡。當前最關鍵的開放問題是：如何準確偵測「何時多算不再有益」，以及如何在平行（best-of-N）與序列（chain-of-thought 延伸）兩種 TTC 模式之間做出最優選擇。

---

## 1. 背景與動機

### 訓練時 Scaling 的邊際遞減

2010 年代末至 2020 年代初，LLM 研究的主旋律是 scaling law：模型參數量、訓練資料量與算力的對數線性增長帶來可預期的性能提升（Kaplan et al., 2020）。然而隨著 GPT-4 等模型訓練成本突破億美元門檻，訓練時 scaling 的邊際報酬逐漸縮小，且對多步驟數學推理、競程式碼等需要「深層思考」的任務，單純加大模型參數並未帶來質的突破。

### 推理期算力的重新發現

Inference-time compute 的核心思想並非全新——Monte Carlo Tree Search 在 AlphaGo（Silver et al., 2016）中已獲得成功，但彼時 LLM 社群對其在語言任務上的應用研究甚少。Self-consistency（Wang et al., 2023）是最早系統化展示「在語言模型推理時投入更多算力」可顯著提升準確率的工作之一，奠定了 parallel TTC 的基礎。

OpenAI 的 o1 系列（2024 年發布）是 TTC scaling 進入公眾視野的重要節點：o1 在 AIME 競賽數學、CodeForces 程式競賽中展現遠超 GPT-4 的表現，其核心機制被認為是在回應前進行大量「內部思考」——即 extended chain-of-thought 生成。這激發了學界對 TTC scaling 理論與實踐的廣泛研究。

### 問題定義

TTC scaling 的核心問題可形式化為：給定固定推理算力預算 B（以 FLOPs 或 token 數衡量）和基礎 LLM，如何最大化特定任務的輸出品質 Q？這個問題涉及三個子問題：(1) 用什麼機制產生多樣化候選解？(2) 用什麼標準選出最佳解？(3) 如何根據題目難度動態分配 B？

---

## 2. 核心概念分析

### 2.1 平行 TTC：Best-of-N 與自洽性

**Best-of-N（BoN）**是最直觀的 TTC 方法：對同一問題取樣 N 條獨立解答軌跡，再由 reward model（RM）或 verifier 選出得分最高者。此方法的理論上界稱為 pass@N（至少有一條正確解的機率），其效益取決於 RM 的品質——若 RM 評分不準確，即使 N 極大，最終選出的解仍可能錯誤。

**Self-consistency**（Wang et al., 2023）是 BoN 的無 verifier 變體：對同一問題取樣多條 chain-of-thought（CoT）路徑，最終答案由多數決（majority vote）決定，不依賴任何外部評分器。其核心假設是：正確解的邏輯路徑多樣但收斂於同一答案，而錯誤路徑則發散。實驗顯示此假設在算術與常識推理上成立。

### 2.2 序列 TTC：Chain-of-Thought 與 Budget Forcing

**Chain-of-thought（CoT）**讓模型在輸出最終答案前生成中間推理步驟，本質上是用序列 token 預算換取推理深度。**Extended CoT** 進一步允許模型自我修正：在思考過程中偵測到矛盾時可回溯（backtracking）、重新嘗試不同策略。

**Budget forcing**（Muennighoff et al., 2025）是控制序列 TTC 的一種簡潔機制：在推理過程中強制附加「Wait」token 以延長思考，或提前截斷以節省算力。這使得推理長度成為可調整的超參數，實驗證明思考長度與困難題目的準確率正相關。

### 2.3 Process Reward Models（PRM）

PRM 對推理的每個中間步驟獨立評分（而非僅評估最終答案），是 TTC 中最重要的品質信號之一。相較於 Outcome Reward Model（ORM，只看最終答案），PRM 的優勢在於：(1) 能辨識邏輯正確但計算錯誤（或反之）的情況；(2) 在 MCTS 或 beam search 中可用於步驟級剪枝；(3) 對避免「表面正確但推理過程謬誤」的解答更為有效。

Lightman et al.（2023）是 PRM 的奠基性工作，發布了包含 80 萬條步驟級人工標注的 PRM800K 資料集，並證明 PRM 在 MATH 資料集上達到 78% 準確率，顯著優於同等規模的 ORM。

### 2.4 Verification-Based vs. Verification-Free

TTC scaling 方法可依賴驗證器（verifier-based, VB）或不依賴（verifier-free, VF）。VB 方法包括 BoN + PRM、MCTS + value model、RL-based search；VF 方法則如 self-consistency 與 budget forcing（純靠 SFT 軌跡蒸餾）。

Setlur et al.（2025）以理論分析嚴格證明：隨著 TTC 預算增大，VF 方法的次優性相對於 VB 方法的差距會單調增加。根本原因是：在正確解分布異質性高（即同一題有多種截然不同的正確解法）的情況下，單純多數決或蒸餾無法有效探索整個解空間。

### 2.5 Adaptive vs. Controllable TTC

Alomrani et al.（2025）提出的二層分類架構清晰地組織了現有方法：
- **L1-Controllable TTC**：使用者指定固定算力預算（如「最多 4096 思考 tokens」），模型在此約束內運作
- **L2-Adaptive TTC**：系統根據輸入難度或模型信心動態調整算力，簡單問題少算、困難問題多算

L2-Adaptive 的核心挑戰是「難度估計」——如何在回答問題之前就準確判斷其難度，且估計本身不能耗費過多算力。

---

## 3. 關鍵論文與研究成果

### Snell et al.（2024）—— Compute-Optimal TTC

**論文**：*Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters*（arXiv 2408.03314）

Snell et al. 系統研究兩種 TTC scaling 機制：(1) process-based verifier reward models 與 (2) 對模型生成分布的自適應更新。核心貢獻是提出「compute-optimal」策略：根據每道題的難度動態分配推理預算，而非對所有題目均等分配。

**量化結果**：在相同總算力預算下，compute-optimal TTC 策略使小模型（PaLM 2-S）的效率超過基線 4 倍以上；在特定困難區間的題目上，小模型 + adaptive TTC 可勝過 14 倍大的模型。這一發現對 LLM 部署策略有根本性影響——在推理算力充足的情境下，部署較小的模型並搭配 TTC 可能比部署大模型更具成本效益。

### DeepSeek-R1（2025）—— 純 RL 誘發推理能力

**論文**：*DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning*（arXiv 2501.12948，Nature 2025）

DeepSeek-R1 證明了一個關鍵命題：LLM 的多步推理能力可以完全從 RL 中湧現，無需任何人工標注的推理軌跡。訓練方法是在可驗證任務（數學、程式碼）上使用 RL，以最終答案的正確性作為 reward 信號。

**湧現行為**：訓練過程中，模型自發出現自我反思（self-reflection）、驗證（verification）與回溯（backtracking）等推理行為，這些行為並非明確編程，而是從最終答案 reward 中湧現。在 AIME 競賽數學上達到與 OpenAI o1 相當或更優的性能。此外，DeepSeek-R1 的推理能力可蒸餾至 1.5B、7B 等小模型，使小模型亦能展現 chain-of-thought 推理能力。開源策略（權重與訓練方法公開）使此工作成為社群復現 o1-class 推理的重要基礎。

### Muennighoff et al.（2025）—— s1 與 Budget Forcing

**論文**：*s1: Simple test-time scaling*（arXiv 2501.19393）

s1 的核心貢獻是展示以極低資源（1,000 條訓練樣本）即可複製 o1-preview 級別的推理能力。作者策劃 s1K 資料集時使用三個選取標準：difficulty（困難度，優先選擇模型初始回答錯誤的題目）、diversity（多樣性，避免題目類型過度集中）、quality（品質，過濾含有錯誤推理的軌跡）。

**Budget forcing 機制**：在推理時，若模型欲結束思考則強制附加「Wait」token，促使模型繼續驗證；若預算不足則截斷。以 Qwen2.5-32B-Instruct 在 s1K 上進行 SFT 後，s1-32B 在 AIME24 上超越 o1-preview 達 27%，在 MATH500 上亦有顯著提升。

**理論意涵**：s1 表明 budget forcing 創造了一種近似的 test-time 搜尋：附加「Wait」token 相當於強制模型對當前解法持懷疑態度並重新審視，實質上是用 token 預算換取自我驗證的機會。

### Lightman et al.（2023）—— PRM800K 與 Process Supervision

**論文**：*Let's Verify Step by Step*（arXiv 2305.20050）

此工作確立了 PRM（Process Reward Model）作為推理步驟評估器的典範。在 MATH 資料集上的對比實驗顯示：PRM（步驟級反饋）在 best-of-N 選擇中的準確率為 78%，顯著高於 ORM（最終答案反饋）的約 55%。

**PRM800K**：發布包含 80 萬條步驟級人工標注的資料集，成為後續大量 PRM 研究的標準訓練資源。Active learning 策略（優先標注模型在步驟分布邊界的樣本）在提升標注效率上亦有顯著效果。PRM 的 step-level scoring 能力使其在 beam search、MCTS 等樹搜尋算法中作為 value function 使用，是目前最有效的 TTC 引導信號之一。

### Wang et al.（2023）—— Self-Consistency

**論文**：*Self-Consistency Improves Chain of Thought Reasoning in Language Models*（arXiv 2203.11171）

Self-consistency 是 TTC scaling 的奠基工作之一，提出以多數決取代貪婪解碼的推理策略。透過取樣多條獨立 CoT 路徑並對最終答案進行多數決，可有效避免單一推理鏈的系統性偏差。

**量化結果**：在 GSM8K 上提升 +17.9%、SVAMP +11.0%、AQuA +12.2%、StrategyQA +6.4%、ARC-challenge +3.9%。此方法不依賴任何外部 verifier，且在不同模型規模與 few-shot/fine-tuned 設定下均表現穩健。Self-consistency 為後續 parallel TTC 研究建立了基準比較線。

### Fu et al.（2024）—— Certaindex 與 Dynasor

**論文**：*Efficiently Scaling LLM Reasoning with Certaindex*（arXiv 2412.20993）

Certaindex 解決了 TTC 的實際部署難題：如何在保持準確率的前提下避免算力浪費。核心觀察是：在 CoT 或 MCTS 推理過程中，大量 token 是在解答已趨於穩定後繼續生成，屬於無效算力消耗。

Certaindex 是算法無關的指標，透過追蹤「中間解答分布的穩定性」來判斷是否已可提前結束推理。在生產環境中，結合 Dynasor 服務系統（支援 gang scheduling），Certaindex 實現 **50% 算力節省** 與 **3.3 倍吞吐量提升**，且無準確率下降。此工作是 TTC 從學術走向工程落地的關鍵橋樑。

### Setlur et al.（2025）—— Verification 的理論必要性

**論文**：*Scaling Test-Time Compute Without Verification or RL is Suboptimal*（arXiv 2502.12118）

Setlur et al. 以反集中（anti-concentration）理論嚴格證明：在正確解分布異質性高的任務上，verification-free 方法的性能差距隨算力增加而單調擴大。直覺上，當一道題有多種截然不同的正確解法時，多數決會「稀釋」每種解法的投票，而有 verifier 的方法可從任意解法中辨識正確性。實驗在 3B、8B、32B 規模的數學推理任務上驗證了理論預測。

### Alomrani et al.（2025）—— Adaptive TTC Survey

**論文**：*Reasoning on a Budget*（arXiv 2507.02076）

此調查論文引入 L1-Controllable / L2-Adaptive 二層分類，對現有 TTC 方法進行系統性梳理，並對 o1、o3、Claude 3.7 Sonnet、Gemini 等主流模型在多個資料集上進行 performance-vs-token-cost 基準測試。關鍵發現是「overthinking」現象——模型在簡單題目上浪費大量 token，同時在困難題目上投入不足——是現有 TTC 系統的普遍問題，呼籲 L2-Adaptive 方法的發展。

---

## 4. 方法論比較

| 方法 | 機制 | 優點 | 缺點 | 適用場景 |
|------|------|------|------|---------|
| **Self-consistency** | 多路取樣 + 多數決 | 無需 verifier，實作簡單 | N 倍推理成本；分布異質時性能上限低 | 有答案收斂特性的任務（算術、常識） |
| **Best-of-N + PRM** | 多路取樣 + PRM 評分 | 選擇品質高；步驟級監督 | 需訓練高品質 PRM；PRM 誤分類影響大 | 數學推理、程式碼（有驗證器） |
| **Budget Forcing** | 附加 Wait token 延長 CoT | 無需額外模型；算力可控 | 依賴基礎模型的自我反思能力 | 可控推理長度；資源受限場景 |
| **MCTS + Value Model** | 樹搜尋 + 步驟級 value | 探索效率高；可 backtrack | 實作複雜；延遲高；並行化困難 | 需深度搜尋的困難推理題 |
| **RL 誘發推理（R1）** | 純 RL + verifiable reward | 能力從訓練中湧現；可蒸餾 | 需大量計算資源訓練；reward hacking 風險 | 從頭訓練推理模型 |
| **Certaindex 早退出** | 解穩定性偵測 | 50% 算力節省；零精度損失 | 需整合至 serving 系統 | 生產部署，吞吐量優先 |

**核心取捨**：平行 TTC（best-of-N / self-consistency）適合有外部 verifier 或答案高度收斂的任務，且易於並行化；序列 TTC（extended CoT / budget forcing）適合需要深層規劃的任務，但延遲較高。Setlur et al. 的理論結果提醒：在異質解空間中，無 verifier 的平行方法不可無限 scale。

---

## 5. 前沿趨勢與開放問題

### 2024–2025 主要趨勢

**Hybrid Thinking Models**：Google 的 Gemini 2.5 Flash 與 Anthropic 的 Claude 3.7 Sonnet 均推出可切換的「extended thinking」模式，允許使用者在需要時啟用深度推理，否則以標準模式回應。Alomrani et al.（2025）稱之為 hybrid thinking model，預測此將成為主流 API 設計模式。

**TTC 效率工程**：隨著 TTC 從研究走向生產，如何降低「extra compute」的實際成本成為核心議題。Certaindex/Dynasor（Fu et al., 2024）代表了推理感知（reasoning-aware）serving 系統的新方向，預計 2025 年將有更多針對 TTC 優化的推理框架出現。

**蒸餾小型推理模型**：DeepSeek-R1 的蒸餾路線使 1.5B 參數模型亦能展現有效推理，降低了部署門檻。未來研究方向包括在更廣泛任務域（不僅是數學/程式）上的推理蒸餾。

### 主要開放問題

1. **難度估計問題**：在回答問題前如何準確評估其難度，以支援 L2-Adaptive TTC，且估計成本必須遠低於 TTC 節省量？
2. **Reward hacking 與分布偏移**：PRM 和 ORM 均易被 reward hacking——模型學習生成能騙過 verifier 但實際錯誤的解答。如何構建更 robust 的 verifier？
3. **非 STEM 任務的 TTC**：目前 TTC 研究幾乎集中於數學與程式碼（有確定性驗證器）。在開放域問答、創意寫作等難以自動驗證的任務上，TTC 能否同樣有效？
4. **CoT 長度與品質的關係**：Budget forcing 顯示長思考有益，但 Certaindex 顯示大量思考 token 是浪費。如何區分「有益思考」與「冗餘 token」？

---

## 6. 實踐意義與應用建議

### 對 AI 工程師的建議

**1. 部署策略：先評估任務特性**
- 任務有確定性 verifier（數學答案、程式碼執行結果）→ 優先考慮 Best-of-N + PRM，可大幅提升準確率
- 任務無明確 verifier → Self-consistency 是次佳選擇，但需警惕解空間異質性（Setlur et al., 2025）
- 延遲敏感場景 → 使用 Certaindex 類早退出機制，節省最多 50% 算力（Fu et al., 2024）

**2. 模型選擇：小模型 + TTC 可能優於大模型**
Snell et al.（2024）的 4 倍效率提升結果意味著：在算力預算固定的情況下，部署 7B–32B 模型搭配充分的 TTC 預算，可能優於部署 70B+ 模型搭配貪婪解碼。計算「cost per correct answer」時需同時考慮模型大小與推理次數。

**3. 訓練策略：SFT + 少量高品質資料足以觸發 TTC 能力**
s1（Muennighoff et al., 2025）的成果顯示，1,000 條高品質 SFT 樣本即可讓 32B 模型在數學競賽上超越 o1-preview。資料選取的 difficulty × diversity × quality 三維過濾比資料量更重要。

**4. PRM 訓練的必要性**
若要部署 best-of-N 系統，自行訓練高品質 PRM 是值得的投資。PRM800K（Lightman et al., 2023）是公開的起點資料集；active learning 策略可顯著降低標注成本。

**5. 警惕 Overthinking**
在生產系統中監控 token 使用分布：若簡單問題也消耗大量推理 token，需加入難度感知的 budget 限制（L1-Controllable TTC），避免不必要的算力開支（Alomrani et al., 2025）。

---

## 7. 研究缺口與未來方向

**最大缺口：非可驗證任務的 TTC**

當前 TTC 研究高度集中於數學與程式碼——這兩個領域恰好有天然的確定性 verifier（答案正確/程式碼通過測試）。在開放域問答、摘要、創意寫作等任務上，如何設計有效的 process reward signal 是最重要的未解問題。

**次要缺口**

- **跨任務 PRM 泛化**：現有 PRM 主要在 MATH/AIME 等資料集訓練，遷移至其他領域的泛化性研究不足。
- **TTC 與 RLHF 的互動**：TTC 能力是否與 RLHF 對齊有協同或衝突效應？目前缺乏系統研究。
- **長 context 下的 TTC**：當任務輸入本身就需要 100K+ tokens（如長文件分析），序列 TTC 的 context window 限制如何解決？
- **多模態 TTC**：視覺推理、代碼+圖表混合任務的 TTC scaling 幾乎尚未被探索。

---

## 附錄：參考文獻

1. **Snell et al. (2024)** — *Scaling LLM Test-Time Compute Optimally can be More Effective than Scaling Model Parameters*. arXiv 2408.03314. [Charlie Snell, Jaehoon Lee, Kelvin Xu, Aviral Kumar]

2. **DeepSeek-AI (2025)** — *DeepSeek-R1: Incentivizing Reasoning Capability in LLMs via Reinforcement Learning*. arXiv 2501.12948. Nature, Vol. 645, pp. 633–638 (2025). [Daya Guo, Dejian Yang, Haowei Zhang et al.]

3. **Muennighoff et al. (2025)** — *s1: Simple test-time scaling*. arXiv 2501.19393. [Niklas Muennighoff, Zitong Yang, Weijia Shi, Xiang Lisa Li, Li Fei-Fei, Hannaneh Hajishirzi, Luke Zettlemoyer, Percy Liang, Emmanuel Candès, Tatsunori Hashimoto]

4. **Lightman et al. (2023)** — *Let's Verify Step by Step*. arXiv 2305.20050. [Hunter Lightman, Vineet Kosaraju, Yura Burda, Harri Edwards, Bowen Baker, Teddy Lee, Jan Leike, John Schulman, Ilya Sutskever, Karl Cobbe]

5. **Wang et al. (2023)** — *Self-Consistency Improves Chain of Thought Reasoning in Language Models*. arXiv 2203.11171. [Xuezhi Wang, Jason Wei, Dale Schuurmans, Quoc Le, Ed Chi, Sharan Narang, Aakanksha Chowdhery, Denny Zhou]

6. **Fu et al. (2024)** — *Efficiently Scaling LLM Reasoning with Certaindex*. arXiv 2412.20993. [Yichao Fu, Junda Chen, Siqi Zhu, Zheyu Fu, Zhongdongming Dai, Yonghao Zhuang, Yian Ma, Aurick Qiao, Tajana Rosing, Ion Stoica, Hao Zhang]

7. **Setlur et al. (2025)** — *Scaling Test-Time Compute Without Verification or RL is Suboptimal*. arXiv 2502.12118. [Amrith Setlur, Nived Rajaraman, Sergey Levine, Aviral Kumar]

8. **Alomrani et al. (2025)** — *Reasoning on a Budget: A Survey of Adaptive and Controllable Test-Time Compute in LLMs*. arXiv 2507.02076. [Mohammad Ali Alomrani, Yingxue Zhang, Derek Li et al.]

---

*報告生成於 2026-06-07。資料來源涵蓋 arXiv 2023–2025 相關論文共 8 篇，及 HuggingFace Daily Papers 與 s1 project page。*

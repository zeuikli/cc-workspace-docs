# Diffusion Models for Language and Code Generation — 深度研究報告
**日期**：2026-06-07 | **研究範圍**：Masked diffusion language models, discrete diffusion, MDLM, LLM+diffusion hybrid, text generation via diffusion

---

## 執行摘要

Diffusion 模型於影像生成領域取得突破後，近兩年研究社群積極將其延伸至離散語言空間。以 MDLM [Sahoo et al., 2024]、SEDD [Lou et al., 2023] 及 LLaDA [Nie et al., 2025] 為代表的研究表明：masked discrete diffusion 架構已能在標準語言建模基準上接近甚至在特定任務超越自回歸（AR）基線。最關鍵洞見有二：其一，diffusion LM 對雙向上下文的天然建模能力使其在複雜推理、規劃與反向生成任務上展現結構性優勢；其二，通過 block diffusion [Arriola et al., 2025] 等混合架構，AR 與 diffusion 兩種範式的互補性正被系統性地整合，開啟了「連續品質-延遲-可控性」三維最佳化的新設計空間。代碼生成方面，Dream-Coder 7B [Xie et al., 2025] 的出現標誌 diffusion LM 已進入實用代碼生成階段。

---

## 1. 背景與動機

### 1.1 自回歸模型的結構性限制

自 GPT 系列奠定地位以來，自回歸（Autoregressive，AR）語言模型主導了自然語言處理領域長達五年。AR 模型以 token-by-token 的左到右生成策略為核心，優勢在於訓練目標清晰（next-token prediction）、推理穩定、與人類書寫習慣高度契合。然而此架構存在數個根本性限制：

1. **順序生成瓶頸**：每個 token 的生成依賴前序輸出，推理無法原生並行，在長序列生成時延遲高。
2. **單向上下文偏差**：訓練期間模型只見左側上下文，對需要全局約束滿足的任務（如數獨、邏輯規劃、密碼學謎題）結構性不利。
3. **逆向詛咒（Reversal Curse）**：AR 模型在「A implies B」方向上訓練後，難以可靠推導「B implies A」，在反向問答、詩歌補完等任務上表現退化。
4. **可控性有限**：插值（infilling）、條件重寫等需要修改已生成 token 的任務需要特殊架構（如 span masking），無法在標準 AR 框架下自然表達。

### 1.2 Diffusion 模型作為替代範式的崛起

Diffusion 模型的核心思想源自非平衡熱力學：通過一個前向過程（forward process）逐步將數據破壞為純雜訊，再學習一個反向過程（reverse process）從雜訊中恢復原始數據。在連續域（圖像、音頻、分子結構）中，此框架以 DDPM [Ho et al., 2020] 和 DALL-E 系列為代表取得了顯著成就。

將 diffusion 延伸至離散語言空間的核心挑戰在於：標準分數匹配（score matching）依賴連續空間的梯度結構，在離散 token 空間中不直接適用。早期嘗試（如 D3PM [Austin et al., 2021]）雖建立了理論基礎，但生成質量與 AR 模型之間存在巨大差距。2023-2025 年間，多篇關鍵工作系統性地縮小了這一差距，使 discrete diffusion LM 從學術概念走向可與 AR 競爭的實用架構。

---

## 2. 核心概念分析

### 2.1 Masked Diffusion 的數學框架

Masked Discrete Diffusion 是目前最成功的離散 diffusion LM 子類別。其核心思想是：將「加雜訊」定義為以一定概率將 token 替換為 `[MASK]` 符號（absorbing state），將「去雜訊」定義為預測並恢復被遮蔽的 token。

**前向過程**：給定輸入序列 $x_0$，在時間步 $t \in [0,1]$ 時，每個 token 以概率 $\alpha(t)$ 被替換為 `[MASK]`，以概率 $1-\alpha(t)$ 保持原值。當 $t \to 1$ 時，序列趨近於全部被遮蔽的狀態。

**反向過程**：訓練一個 Transformer（通常為雙向 BERT-style）以預測 $x_0$，即在給定部分遮蔽序列 $x_t$ 的條件下，估計原始 token 的分佈。

**SUBS 參數化** [Sahoo et al., 2024]：MDLM 的關鍵貢獻之一是引入「substitution-based」參數化，將 absorbing-state diffusion 的訓練損失化簡為加權的 MLM（Masked Language Modeling）交叉熵之和：

$$\mathcal{L}_{\text{SUBS}} = \mathbb{E}_{t, x_t} \left[ w(t) \cdot \text{CE}(\hat{x}_0, x_0) \right]$$

其中 $w(t)$ 為時間依賴的權重函數。這個化簡的重要性在於：它使 diffusion LM 的訓練與 BERT 的 MLM 訓練直接等價，可直接繼承 BERT 的工程最佳實踐（混合精度訓練、學習率排程、大 batch 訓練等）。

### 2.2 Score Entropy 離散 Diffusion（SEDD）

SEDD [Lou et al., 2023] 提出了一條不同的理論路線。其核心貢獻是將連續分數匹配（score matching）的概念延伸至離散空間，引入「分數熵」（score entropy）作為離散數據的訓練目標：

$$\mathcal{L}_{\text{SEDD}} = \mathbb{E} \left[ \sum_`{y \neq x_t}` q(y | x_t) \left( \frac{p(x_t | y)}{p(x_t)} - \log \frac{p(x_t | y)}{p(x_t)} - 1 \right) \right]$$

此目標函數在理論上比早期 D3PM 的變分下界（ELBO）更緊，使得採樣效率大幅提升：SEDD 可以用 **32× 更少的網路前向傳播**達到與完整採樣步驟可比的生成品質。

### 2.3 Block Diffusion：AR 與 Diffusion 的橋接

Block Diffusion [Arriola et al., 2025] 引入了一個統一框架，通過「區塊」結構在 AR 與 diffusion 之間平滑插值：

- **Block AR**：每個區塊自回歸地依序生成（相當於標準 AR，區塊大小=1）
- **Block Diffusion**：區塊內部使用 masked diffusion 並行去雜訊，區塊間依序展開
- **Pure Diffusion**：整個序列視為單一區塊（傳統 diffusion LM）

此設計同時解決了：(1) 傳統 diffusion LM 只能生成固定長度序列的問題；(2) 通過 KV cache 在區塊間實現推理加速；(3) 為訓練引入梯度變異估計器（gradient variance estimators）和數據驅動的雜訊排程。

### 2.4 多粒度 Diffusion 建模（MGDM）

MGDM [Ye et al., 2024] 針對複雜推理任務提出了一個關鍵改進：識別到自回歸模型在「子目標不平衡」（subgoal imbalance）問題上的缺陷，即模型在簡單子任務上過度訓練而在關鍵約束步驟上訓練不足。MGDM 通過動態調整不同子目標的採樣難度，使 diffusion 模型在訓練中更多關注困難子目標（如數獨中的約束滿足節點、Countdown 謎題中的組合邊界）。

---

## 3. 關鍵論文與研究成果

### 3.1 MDLM — Simple and Effective Masked Diffusion Language Models

**[Sahoo et al., NeurIPS 2024]** | arXiv:2406.07524

**方法**：MDLM 建立於 absorbing-state masked diffusion 之上，核心貢獻是 SUBS 參數化（將 diffusion 損失化簡為 MLM 損失的加權和）+ Rao-Blackwellized 目標（通過條件期望降低梯度方差）+ 現代工程訓練配方（大 batch、混合精度、余弦學習率排程）。

**量化結果**：
- LM1B 測試集：困惑度（perplexity）達到 **75.1**，優於所有先前 diffusion LM（D3PM、MDLM 前身）
- OpenWebText：困惑度 **21.4**，接近同規模 AR 模型（差距縮小至 15–25%）
- 支援任意長度半自回歸生成，打破固定長度限制

**意義**：MDLM 確立了 masked diffusion + MLM 損失等價這一核心洞見，大幅降低了 diffusion LM 的工程門檻。

### 3.2 LLaDA — Large Language Diffusion Models

**[Nie et al., 2025]** | arXiv:2502.09992

**方法**：LLaDA 是首個從頭（from scratch）以完整預訓練 + SFT 範式訓練的 **8B 參數** masked diffusion LM。前向過程為均勻遮蔽，反向過程由 Transformer 參數化以預測 `[MASK]` 的原始 token，損失函數為似然基準的優化目標（likelihood-based objective）。SFT 階段直接在回應部分施加遮蔽，實現指令跟隨能力。

**量化結果**：
- 與 LLaMA3 8B 在上下文學習（in-context learning）任務上競爭性持平
- **逆向詩歌補完任務**：超越 GPT-4o（LLaDA 因雙向依賴自然解決 reversal curse）
- 數學與代碼生成基準上展現強擴展性（scaling），後續工作延伸至 LLaDA2.0（16B / 100B MoE 變體）

**意義**：LLaDA 是第一個在語言建模的主流評估（instruction following、數學、代碼）上與頂級 AR LLM 量級可比的 diffusion 模型，證明「大型語言模型 = 自回歸」的假設可以被挑戰。

### 3.3 SEDD — Score Entropy Discrete Diffusion

**[Lou, Meng, Ermon, ICML 2024 Oral]** | arXiv:2310.16834

**方法**：SEDD 從理論出發，將連續分數匹配延伸至離散空間，提出分數熵（score entropy）作為離散數據的訓練目標。採樣時利用離散 Langevin 動力學（discrete Langevin dynamics）以更少步驟完成高品質生成。

**量化結果**：
- 相比先前語言 diffusion 模型（如 D3PM），困惑度降低 **25–75%**
- 以 **32× 更少網路前向傳播**達到可比生成品質
- 在 GPT-2 規模（117M、345M）上超越 GPT-2 的生成品質（perplexity 及人工評分）
- 原生支援 infilling（插補）、非左到右解碼，無需重新訓練

**意義**：SEDD 從理論層面解釋了為何早期離散 diffusion 效率低下，並提供了有原理依據的解決方案，成為後續工作的重要基礎。

### 3.4 MGDM — Beyond Autoregression

**[Ye et al., ICLR 2025]** | arXiv:2410.14157

**方法**：提出「子目標不平衡」問題的形式化定義，以及多粒度 diffusion 建模（MGDM）。MGDM 在 diffusion 訓練的雜訊排程中動態提升困難子目標的採樣概率，使模型在關鍵約束步驟上獲得更多梯度信號。

**量化結果**（不使用搜索技術）：
- **Countdown 謎題**：91.5% 準確率 vs AR 基線 45.8%（提升 **+45.7pp**）
- **數獨（Sudoku）**：100% 準確率 vs AR 基線 20.7%（提升 **+79.3pp**）
- **布林可滿足性問題（Boolean SAT）**：顯著優於 AR 基線

**意義**：MGDM 提供了 diffusion LM 在結構性優勢任務上的最強量化證據，對 AI 規劃和推理領域意義重大。

### 3.5 Block Diffusion BD3-LMs

**[Arriola et al., ICLR 2025 Oral]** | arXiv:2503.09573

**方法**：將序列分解為固定大小的區塊，區塊間自回歸（AR）依序展開，區塊內使用 masked diffusion 並行去雜訊。引入梯度變異估計器（gradient variance estimators）和數據驅動雜訊排程（data-driven noise schedules）以穩定訓練。

**量化結果**：
- 在標準語言建模基準上達到 diffusion 模型中的 SOTA 似然（likelihood）
- 解決固定長度限制，支援任意長度序列生成
- KV cache + 並行 token 採樣結合，在推理效率上同時繼承 AR 和 diffusion 的優勢

### 3.6 Dream-Coder 7B — 代碼生成 Diffusion LM

**[Xie et al., 2025]** | arXiv:2509.01142

**方法**：從預訓練自回歸 LLM checkpoint 出發，通過持續訓練轉換為離散 diffusion 框架（continuous-time weighted cross-entropy objective）。採用三種自適應解碼策略：sketch-first（複雜算法先生成骨架）、left-to-right（簡單補全）、interleaved reasoning（代碼理解任務）。使用 RLVR（RL with verifiable rewards）在可驗證獎勵上進行強化學習微調。

**量化結果**：
- LiveCodeBench pass@1：**21.4%**，與更大規模 diffusion 模型競爭
- 完整開源：checkpoint、訓練配方、預處理管道、推理代碼

---

## 4. 方法論比較

| 維度 | Masked Diffusion（MDLM/LLaDA） | Score Entropy（SEDD） | Block Diffusion（BD3-LM） |
|------|------|------|------|
| **理論基礎** | Absorbing-state Markov chain | 離散分數匹配 | AR + Diffusion 混合 |
| **採樣效率** | 中等（需多步去雜訊） | 高（32× 節省） | 高（KV cache + 並行）|
| **生成長度** | 固定長度（除 Block 變體） | 固定長度 | 任意長度 |
| **訓練難度** | 低（等價 MLM 損失） | 中等（需離散 Langevin） | 中高（梯度方差控制）|
| **可控性** | 中（掩蔽模式可控） | 高（原生支援 infilling）| 中高（區塊級可控）|
| **規劃/推理任務** | 強（雙向依賴） | 強 | 強 |
| **工程成熟度** | 高（MLM 繼承） | 中 | 中 |

**選擇建議**：
- 快速工程落地、從 BERT 遷移 → **MDLM**（最低訓練門檻）
- 需要高採樣效率或非順序生成 → **SEDD**
- 需要任意長度生成且兼顧推理速度 → **BD3-LM**
- 複雜規劃/約束任務 → **MGDM**（優先選擇 diffusion 架構）
- 代碼生成且有預訓練 AR 基礎 → **Dream-Coder 風格轉換**

---

## 5. 前沿趨勢與開放問題

### 5.1 2024-2025 主要趨勢

**規模化驗證**：LLaDA 的 8B 版本及後續 LLaDA2.0 的 16B/100B MoE 變體表明，masked diffusion 架構具備可擴展性（scalability），不再是只在小規模上有效的研究玩具。

**AR-Diffusion 融合加速**：Block Diffusion [Arriola et al., 2025] 和 Dream-Coder [Xie et al., 2025]（從 AR checkpoint 轉換）展示了兩種範式並非對立，混合架構與轉換策略正成為重要研究方向。

**特定任務優勢固化**：MGDM [Ye et al., 2024] 量化確認了 diffusion LM 在規劃/推理任務上的結構性優勢，預期後續在 AI agent、代碼驗證、形式化推理領域將有更多 diffusion-first 設計出現。

### 5.2 主要開放問題

1. **困惑度差距**：即使最佳 masked diffusion LM（如 LLaDA 8B）仍與同等規模 AR LLM 在標準語言建模困惑度上存在 15-25% 差距，根本原因尚未完全理解。
2. **長序列訓練穩定性**：超過 4096 token 的長文本 diffusion 訓練存在梯度爆炸和 attention 計算瓶頸，需要針對性方案。
3. **RLHF 相容性**：標準 RLHF 依賴 token-level log-probability 作為獎勵信號，在 diffusion 框架下需要重新設計（Dream-Coder 的 RLVR 是初步嘗試）。
4. **多模態擴展**：diffusion 在圖像模態天然適用，但文本-圖像聯合 diffusion LM（統一 token 空間）仍處於早期探索。

---

## 6. 實踐意義與應用建議

### 對 AI 工程師

**何時應考慮 Diffusion LM 替代 AR**：
- 任務需要**全局約束滿足**（程式碼格式、結構化輸出、JSON schema）→ diffusion 的雙向建模天然適合
- 需要高質量**文本插補（infilling）** 而不願訓練特殊 AR 插補模型 → SEDD 原生支援
- **批量生成延遲敏感**而非逐 token 流式展示 → diffusion 並行去雜訊可降低 batch latency

**遷移路徑建議**：
1. 從預訓練 AR checkpoint 出發（Dream-Coder 路徑）而非從頭訓練，可大幅降低計算成本
2. 損失函數選擇 MDLM 的 SUBS 參數化（等價 MLM，工程最成熟）
3. 評估框架須包含 infilling 和非順序生成任務，僅用 perplexity 會低估 diffusion 優勢

### 對研究者

- **基準選擇**：確保評估集包含逆向任務（reversal curse）和規劃任務（Sudoku/Countdown），這些是 diffusion 優勢最顯著的維度
- **消融設計**：SUBS 參數化 vs 分數熵兩條路線的公平比較在文獻中仍不充分
- **與 RLHF 結合**：RLVR（可驗證獎勵 RL）是目前最可行的 alignment 路徑

---

## 7. 研究缺口與未來方向

1. **理論層面**：為何 masked diffusion 的困惑度存在系統性差距？是 absorbing state 設計的固有限制，還是訓練目標優化不足？需要更深入的理論分析。

2. **代碼生成**：Dream-Coder 7B 的 21.4% pass@1 仍低於同規模 AR 代碼模型（如 DeepSeek-Coder），sketch-first 解碼策略的優化空間大，特別是在多輪互動場景下。

3. **長期依賴**：擴展至書籍/文章級長文本（100K+ token）的 masked diffusion 訓練方案仍缺乏。

4. **推理時擴展**：diffusion LM 的「採樣步數即計算預算」特性為 inference-time scaling（類似 Chain-of-Thought/Best-of-N）提供了自然接口，但系統性研究尚缺。

5. **中文/多語言**：幾乎所有重要 diffusion LM 工作均以英文為主，中文及其他非拉丁語系語言（特別是 CJK token 空間下的 absorbing state 設計）尚未充分探索。

---

## 附錄：參考文獻

1. **Sahoo, S. S., Arriola, M., Schiff, Y., Gokaslan, A., Marroquin, E., Chiu, J. T., Rush, A., & Kuleshov, V. (2024).** Simple and Effective Masked Diffusion Language Models. *NeurIPS 2024*. arXiv:2406.07524. https://arxiv.org/abs/2406.07524

2. **Nie, S., Zhu, F., You, Z., Zhang, X., Ou, J., Hu, J., Zhou, J., Lin, Y., Wen, J.-R., & Li, C. (2025).** Large Language Diffusion Models. arXiv:2502.09992. https://arxiv.org/abs/2502.09992

3. **Lou, A., Meng, C., & Ermon, S. (2023).** Discrete Diffusion Modeling by Estimating the Ratios of the Data Distribution. *ICML 2024 Oral*. arXiv:2310.16834. https://arxiv.org/abs/2310.16834

4. **Ye, J., Gao, J., Gong, S., Zheng, L., Jiang, X., Li, Z., & Kong, L. (2024).** Beyond Autoregression: Discrete Diffusion for Complex Reasoning and Planning. *ICLR 2025*. arXiv:2410.14157. https://arxiv.org/abs/2410.14157

5. **Arriola, M., Gokaslan, A., Chiu, J. T., Yang, Z., Qi, Z., Han, J., Sahoo, S. S., & Kuleshov, V. (2025).** Block Diffusion: Interpolating Between Autoregressive and Diffusion Language Models. *ICLR 2025 Oral*. arXiv:2503.09573. https://arxiv.org/abs/2503.09573

6. **Xie, Z., Ye, J., Zheng, L., Gao, J., Dong, J., Wu, Z., Zhao, X., Gong, S., Jiang, X., Li, Z., & Kong, L. (2025).** Dream-Coder 7B: An Open Diffusion Language Model for Code. arXiv:2509.01142. https://arxiv.org/abs/2509.01142

7. **Austin, J., Johnson, D. D., Ho, J., Tarlow, D., & van den Berg, R. (2021).** Structured Denoising Diffusion Models in Discrete State-Spaces. *NeurIPS 2021*. （D3PM，離散 diffusion 早期基礎工作）

8. **Ho, J., Jain, A., & Abbeel, P. (2020).** Denoising Diffusion Probabilistic Models. *NeurIPS 2020*. （DDPM，連續 diffusion 基礎）

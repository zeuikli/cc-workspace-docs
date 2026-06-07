# Mechanistic Interpretability in Large Language Models — 深度研究報告

**日期**：2026-06-07 | **研究範圍**：Circuits hypothesis, superposition, sparse autoencoders (SAE), monosemanticity, feature geometry, causal tracing, activation patching

---

## 執行摘要

機械可解釋性（Mechanistic Interpretability，MI）是當前 AI 安全與可信賴 AI 研究的核心前沿。其核心問題：大型語言模型（LLM）的內部計算是否可被人類理解？過去三年，Anthropic、MIT、EleutherAI 等機構的研究已提供令人振奮的肯定答案。稀疏自動編碼器（SAE）技術從 Claude 3 Sonnet 中解碼 3,400 萬個可解釋特徵 [Templeton et al., 2024]，因果追蹤方法（ROME）定位 GPT 中儲存事實知識的中層 MLP [Meng et al., 2022]，跨層轉碼器（CLT）則構建出 Claude 3.5 Haiku 的完整歸因計算圖 [Ameisen et al., 2025]。領域共識正在收斂：特徵（Feature）而非神經元（Neuron）是分析的基本單位，超疊加（Superposition）是多語義性的根本來源，而 SAE 是當前最有效的解碼工具。

---

## 1. 背景與動機

### 為何可解釋性是核心問題

現代 LLM 的參數規模已達千億，由梯度下降訓練產生的權重矩陣沒有明確設計文件，對外部觀察者而言是「黑盒子」。這在三個維度上形成嚴重問題：

**一、安全性**：當模型表現出不期望行為（越獄、欺騙、幻覺），我們無法從機制層面理解原因，也無法提出針對性修正，只能靠啟發式 prompt 工程或大量 RLHF 資料。

**二、可靠性驗證**：無法驗證模型「是否真正理解」還是只在「表面上相關」。一個通過所有測試的模型仍可能在分佈外輸入上崩潰。

**三、知識定位與編輯**：模型儲存的知識是否可被精確定位並更新（例如移除過期或危險的事實），還是必須完整重訓練？

MI 的目標是為上述問題提供機制級別的答案，而非統計性相關。歷史上，神經網路可解釋性研究起步於計算機視覺的特徵視覺化（Feature Visualization），但語言模型的高維度、離散符號輸入和多層次計算使問題顯著更難。2022 年後，Circuits Hypothesis 的形式化、Superposition 理論框架的建立，以及 SAE 技術的突破，標誌著 MI 從定性觀察進入定量、可驗證的科學階段。

### Circuits Hypothesis 的基礎

MI 的核心假設是 **Circuits Hypothesis**：LLM 的計算可被分解為由特徵（Features）和電路（Circuits）組成的模組化計算圖。特徵是激活空間中的線性方向，代表可解釋的概念；電路是特徵間的信息流動路徑。這一假設提供了研究框架，但其適用範圍和可擴展性長期是開放問題。

---

## 2. 核心概念分析

### 2.1 超疊加（Superposition）：多語義性的根本來源

**多語義性問題（Polysemanticity）**：單一神經元往往對多個不相關的概念有響應，例如同一個神經元可能對「學術論文」、「流量分析」和「日本天皇」同時激活。這使逐神經元分析失效。

**Superposition 假說** [Elhage et al., 2022]：模型面臨「特徵比神經元多得多」的壓縮問題。解法是將多個稀疏激活的特徵壓縮存入同一批神經元，利用高維空間中幾乎正交向量的大量存在性（Johnson-Lindenstrauss 引理的隱含應用）。只要不同特徵不同時激活（稀疏性假設），這種壓縮就幾乎無損。

**幾何連接**：Elhage et al. 發現超疊加特徵的幾何排列對應高維空間中的**均勻多面體（Uniform Polytopes）**，包括二維五邊形（5 features in 2D）、三維正八面體等。這是令人驚訝的數學結構發現，暗示模型自發地找到了最優幾何排布。

**相變（Phase Transition）**：實驗發現模型在超疊加和非超疊加儲存策略之間存在相變現象——當特徵稀疏度超過某臨界值，模型突然轉換策略，開始大量壓縮特徵。

**對抗樣本的連接**：超疊加機制還被提出與對抗樣本的脆弱性相關：不同特徵在激活空間中的干擾使得特定方向的微小擾動可以混淆模型判斷。

### 2.2 稀疏自動編碼器（SAE）：超疊加的解碼工具

**問題設置**：給定模型中間層激活向量 $h \in \mathbb{R}^{d}$，目標是找到過完備字典 $W \in \mathbb{R}^`{d \times n}`$（其中 $n \gg d$）和稀疏係數 $f \in \mathbb{R}^{n}$，使得 $h \approx W f$ 且 $f$ 稀疏（大多數係數為零）。

**架構**：SAE 包含一個編碼器（將激活投射到高維稀疏空間）和解碼器（重建原始激活）。訓練目標是最小化重建損失 + L1 稀疏懲罰：
$$\mathcal{L} = \|h - \hat{h}\|^2 + \lambda \|f\|_1$$

**字典學習（Dictionary Learning）框架** [Cunningham et al., 2023]：SAE 可被視為字典學習問題，每個字典原子對應一個特徵方向。L1 稀疏性迫使網絡在解碼超疊加時每次只激活少數特徵，對應真實的語義概念。

### 2.3 因果追蹤（Causal Tracing）與激活修補（Activation Patching）

**核心思路**：因果追蹤通過「手術式」替換激活值來確定因果關係。給定干淨輸入（clean）和污染輸入（corrupted），通過逐步將污染輸入的激活替換為干淨輸入的激活（或反之），觀察模型輸出的變化，從而定位關鍵計算位點。

**Causal Tracing 協議** [Meng et al., 2022]：
1. 在干淨輸入上運行模型，記錄所有中間激活
2. 構建污染版本（corrupt），例如替換主語名詞為隨機標記
3. 在污染版本上逐層、逐位置修補（patch）干淨激活
4. 觀察哪些修補最有效地恢復模型的正確輸出

**間接效應（Indirect Effect）**：修補 attention 輸出後，其下游的 MLP 輸入也會改變，因此需要區分直接效應和間接效應（經由後續層傳播的影響）。

### 2.4 跨層轉碼器（Cross-Layer Transcoders，CLT）

**超越 per-layer SAE 的侷限**：傳統 SAE 在每層獨立提取特徵，但特徵可能跨層持續存在，per-layer 分析無法捕捉這種跨層信息流動。

**CLT 架構** [Ameisen et al., 2025]：CLT 替換 MLP 層，學習稀疏激活的特徵，這些特徵可以跨層直接連接。結合凍結的 attention pattern，CLT 構建出局部替換模型（Local Replacement Model），在保持可解釋性的同時對原始模型行為保持忠實近似。

**歸因圖（Attribution Graph）**：基於 CLT 的分析可構建有向計算圖，節點是特徵，邊是信息流動路徑，完整追蹤從輸入 token 到輸出預測的計算過程。

### 2.5 單語義性（Monosemanticity）與特徵幾何

**單語義性定義**：一個特徵方向若只對一個一致可描述的概念有響應（無論輸入語言或格式），則稱為單語義（Monosemantic）。這與多語義（Polysemantic）的神經元相對。

**特徵幾何（Feature Geometry）**：特徵方向在激活空間中的排列方式。均勻多面體連接（Elhage et al., 2022）是特徵幾何的早期發現。在高維空間，這些幾何關係決定了不同特徵之間的干擾程度和壓縮效率。

---

## 3. 關鍵論文與研究成果

### 3.1 Elhage et al., 2022 — 超疊加的玩具模型

**論文**：Toy Models of Superposition（arxiv:2209.10652）

這是 MI 領域的奠基性理論工作。作者設計了可完全受控的玩具模型，直接操作特徵稀疏度和數量，完整記錄超疊加的形成過程。

**關鍵結果**：
- 在 2 個神經元中可穩定儲存多達 5 個稀疏特徵（五邊形排布）
- 發現稀疏度閾值相變：特徵稀疏度從 0.1 增加到 0.01 時，模型從非超疊加模式突然切換到超疊加模式
- 超疊加特徵方向對應均勻多面體頂點（2D 五邊形、3D 八面體等）
- 對抗樣本對超疊加特徵的干擾機制被初步形式化

**意義**：為 SAE 等解碼工具提供了理論動機——如果特徵以幾何結構儲存在神經元空間，則原則上可被提取。

### 3.2 Cunningham et al., 2023 — SAE 應用於語言模型

**論文**：Sparse Autoencoders Find Highly Interpretable Features in Language Models（arxiv:2309.08600）

**關鍵結果**：
- 在 GPT-2 中層應用 SAE，提取的特徵在自動化可解釋性評分上顯著優於 PCA（主成分分析）和 ICA（獨立成分分析）分解
- 在間接賓語識別（Indirect Object Identification，IOI）任務上進行因果驗證，確認 SAE 特徵是行為的因果原因而非純相關
- 建立了比較不同分解方法的評估框架

**方法論貢獻**：首次系統展示 SAE 在語言模型上的可擴展性，確立了「SAE 特徵 > 神經元 > PCA」的分析層級。

### 3.3 Bricken et al., 2023 — 向單語義性邁進

**論文**：Towards Monosemanticity: Decomposing Language Models With Dictionary Learning

**關鍵結果**：
- 從僅 512 個神經元的單層 Transformer 中提取超過 **4,000 個**可解釋特徵
- 特徵對應的概念極為具體且人類可解釋：DNA 序列、法律語言、HTTP 請求格式、希伯來文、營養標示
- 建立了自動化可解釋性評分（Automated Interpretability Score）和人工評分的雙重評估協議
- 因果驗證：激活特定特徵可直接影響模型輸出，確認特徵不是事後合理化

**規模意義**：特徵與神經元比例達 **4,000:512 ≈ 7.8:1**，提供了超疊加的第一個直接實證証據。

### 3.4 Meng et al., 2022 — ROME 因果追蹤

**論文**：Locating and Editing Factual Associations in GPT（arxiv:2202.05262）

**關鍵結果**：
- 因果追蹤揭示 GPT-style 模型中，**中層 MLP（約 15-20 層）**是事實關聯的主要儲存位點，早層 MLP 主要處理主語 token
- Attention 層主要負責信息聚合和傳播，不直接儲存事實
- ROME 算法：通過秩一更新（Rank-One Update）精確編輯目標 MLP 層的 key-value 記憶，實現單一事實的外科式修改
- CounterFact 數據集：提供 21,919 個事實對（原始+反事實），嚴格評估編輯的特異性（只改目標事實）和泛化性（以不同方式表達同一事實時效果一致）

**實用意義**：首次提供了「知識作為局部化計算」的實證基礎，也是模型知識編輯（Model Editing）領域的奠基工作。

### 3.5 Templeton et al., 2024 — 單語義性的規模擴展

**論文**：Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet

**關鍵結果**：
- 從 Claude 3 Sonnet 中層殘差流中提取 **3,400 萬個**潛在特徵
- SAE 訓練遵循可預測的 **Scaling Laws**：擴大 SAE 規模，特徵質量和數量按冪律增長
- 在這一規模下，特徵高度抽象且多模態：包含情緒、偏見、安全相關行為（欺騙、操縱、危險知識）
- **特徵引導實驗（Feature Steering）**：手動激活或抑制特定特徵可系統性地控制模型行為，例如激活「欺騙」特徵後模型的欺騙傾向顯著上升

**安全意義**：首次在前沿商用 LLM 中找到對應安全關鍵行為的可識別特徵，為對齊研究提供了新工具。

### 3.6 Ameisen et al., 2025 — 電路追蹤

**論文**：Circuit Tracing: Revealing Computational Graphs in Language Models

**關鍵結果**：
- CLT 設計：相比 per-layer SAE，CLT 允許特徵跨層持續，顯著提升歸因圖的完整性和忠實度
- 在 Claude 3.5 Haiku 上應用，提供了**三個任務**（事實回憶、算術加法、縮寫生成）的完整步驟級計算機制說明
- 擾動驗證：通過修改歸因圖中特定節點值，預測並驗證模型行為的對應改變，確認機制的因果忠實性
- 開源互動式可視化工具，允許研究者導航計算圖並測試假設

**方法論意義**：目前最完整的前沿模型電路級機制描述，將 MI 方法從「可觀察性工具」推進到「可操作的解釋工程」。

---

## 4. 方法論比較

### 4.1 神經元分析 vs. 特徵分析

| 維度 | 神經元分析 | SAE 特徵分析 |
|---|---|---|
| 可解釋性 | 多語義，難以一致描述 | 單語義，通常對應清晰概念 |
| 覆蓋率 | 受限於神經元數量 | 可超過神經元數量 7-8 倍 |
| 因果驗證難度 | 較難隔離單個神經元效應 | 可精確激活/抑制單一特徵 |
| 計算成本 | 低 | 中等（需訓練 SAE） |

**結論**：特徵分析在可解釋性和覆蓋率上全面優於神經元分析，計算成本的增加是合理代價。

### 4.2 Per-layer SAE vs. Cross-Layer Transcoders（CLT）

| 維度 | Per-layer SAE | CLT |
|---|---|---|
| 跨層信息流 | 不直接捕捉 | 原生支持 |
| 計算圖完整性 | 部分 | 較完整 |
| 訓練複雜度 | 低 | 高 |
| 適用場景 | 單層激活分析 | 完整電路追蹤 |

### 4.3 因果追蹤 vs. 歸因方法

**Causal Tracing**（Meng et al.）：基於激活修補，識別哪些組件對特定輸出有必要貢獻。優點：直接因果解釋，無需模型結構假設。缺點：逐組件分析計算成本高，難以擴展到全電路。

**Attribution Graphs**（Ameisen et al.）：基於 CLT 的完整計算圖，可一次性追蹤完整信息流。優點：全局視角，識別完整電路。缺點：依賴 CLT 近似的忠實度，訓練成本高。

**Gradient-based Attribution**：計算輸出對輸入或中間激活的梯度。優點：計算快速。缺點：梯度飽和問題（Saturated Gradient），在非線性激活函數附近準確性下降，且無法區分直接和間接效應。

**最佳實踐建議**：初步定位用梯度法快速篩選，精確因果驗證用激活修補，完整機制理解用歸因圖（需訓練 CLT）。

---

## 5. 前沿趨勢與開放問題

### 2024-2025 前沿動態

**規模突破**：Templeton et al., 2024 確認 SAE 可擴展至生產前沿模型，3,400 萬特徵的提取表明 Scaling Laws 在解釋工具本身也適用。2025 年 CLT 方法（Ameisen et al.）將分析粒度推進到完整計算圖，是方法論的重大躍升。

**安全導向研究加速**：Scaling Monosemanticity 識別的「欺騙」「操縱」特徵引發了將 MI 技術直接應用於安全評估的研究方向。特徵引導（Feature Steering）技術正在被探索作為對齊干預的新手段。

**SAE 變體擴增**：TopK SAE、ReLU SAE、JumpReLU 等架構在稀疏控制和重建質量之間的權衡各有不同。2024-2025 年出現了大量關於 SAE 設計選擇的消融研究。

### 主要開放問題

1. **完整性問題（Completeness）**：已識別的特徵和電路是否覆蓋了模型的全部計算？還是只是可解釋的部分，而大量計算仍不透明？

2. **局部 vs. 全局解釋**：現有方法主要提供**局部解釋**（特定 prompt 上的計算路徑），無法給出「模型整體上如何工作」的全局回答。

3. **Superposition 幾何的通用性**：均勻多面體連接是在玩具模型中發現的。在 LLM 規模下，特徵幾何是否遵循同樣的原則？

4. **特徵穩定性**：不同訓練 run 下，同一概念是否對應相同的特徵方向？還是特徵表示本身是任意的？

5. **CLT 的忠實度上界**：局部替換模型近似原始模型的程度有多高？在複雜推理任務上是否會顯著偏差？

---

## 6. 實踐意義與應用建議

### 對 AI 安全研究者

**立即可用**：SAE 已可在開源模型（Llama、GPT-2、Mistral）上訓練，提取可解釋特徵。EleutherAI 的 SAELens 和 Anthropic 的公開工具提供了開箱即用的實現。

**安全評估新工具**：在目標模型上訓練 SAE → 搜索與有害行為相關的特徵 → 通過特徵引導驗證因果關係 → 為對齊研究提供機制級定位。相比依賴行為測試的黑盒評估，這提供了更深層的理解。

**模型知識編輯**：ROME 框架已被後續工作（MEMIT 等）擴展，支持批量事實更新。對需要更新知識庫而不重訓練的場景，這是可工程化的解決方案。

### 對 LLM 研究者

**架構設計啟示**：Superposition 理論暗示增加模型寬度（而非深度）可減少超疊加程度，降低多語義性。特徵幾何研究為設計更可解釋的模型表示提供方向。

**評估設計**：激活修補可作為判斷模型是否真正理解任務的測試手段，而非僅靠輸出準確率。間接賓語識別（IOI）任務的電路分析提供了評估方法論的標準參照。

**SAE 訓練實踐**：
- 訓練字典大小約為激活維度的 4-16 倍是合理起點
- L1 正則化強度（$\lambda$）需要仔細調整，過強導致特徵消失，過弱導致多語義性殘留
- 在更寬的中層（通常是模型總層數的 30-70% 範圍）訓練效果最佳
- Scaling Laws 適用：更大的 SAE 字典提取更多更精確的特徵

### 對 AI 治理與政策

MI 技術為「模型審計」提供了客觀工具：第三方機構可通過 SAE 特徵分析和因果追蹤，獨立評估模型是否含有危險知識表示或欺騙傾向特徵，而無需依賴開發者的自我宣告。這是 AI 治理中可驗證的技術路徑之一。

---

## 7. 研究缺口與未來方向

**理論缺口**：

- Superposition 幾何的形式化理論框架尚不完整，均勻多面體連接為何出現仍是開放問題
- 特徵的「功能等價類」定義缺乏形式化：同一語義概念在不同模型中以不同幾何方向表示，如何跨模型對齊？
- 電路的組合性（Compositionality）理論：複雜推理如何從簡單電路模組組合而成？

**方法缺口**：

- 大規模完整模型的 CLT 訓練成本仍然極高，需要更高效的近似方法
- 動態電路（Dynamic Circuits）：在多步推理中，注意力模式和特徵激活如何隨 token 生成動態演化，尚無完整追蹤方法
- 跨模型可遷移的特徵識別：目前每個模型需獨立訓練 SAE

**應用缺口**：

- MI 工具用於**對齊驗證**的標準化評估協議尚不存在——如何確定一個模型「機制上安全」缺乏共識定義
- 特徵引導技術的副作用和魯棒性研究不足，干預一個特徵可能通過電路產生未預期的連鎖效應

---

## 附錄：參考文獻

1. **[Elhage et al., 2022]** Elhage, N., Hume, T., Olsson, C., Schiefer, N., Henighan, T., Kravec, S., Hatfield-Dodds, Z., Lasenby, R., Drain, D., Chen, C., Grosse, R., McCandlish, S., Kaplan, J., Amodei, D., Wattenberg, M., & Olah, C. (2022). *Toy Models of Superposition*. arXiv:2209.10652. https://arxiv.org/abs/2209.10652

2. **[Cunningham et al., 2023]** Cunningham, H., Ewart, A., Riggs, L., Huben, R., & Sharkey, L. (2023). *Sparse Autoencoders Find Highly Interpretable Features in Language Models*. arXiv:2309.08600. https://arxiv.org/abs/2309.08600

3. **[Bricken et al., 2023]** Bricken, T., Templeton, A., Batson, J., Chen, B., Jermyn, A., Conerly, T., Turner, N., Anil, C., Denison, C., Askell, A., Lasenby, R., Wu, Y., Kravec, S., Schiefer, N., Maxwell, T., Joseph, N., Hatfield-Dodds, Z., Tamkin, A., Nguyen, K., McLean, B., Burke, J. E., Hume, T., Carter, S., Henighan, T., & Olah, C. (2023). *Towards Monosemanticity: Decomposing Language Models With Dictionary Learning*. Transformer Circuits Thread. https://transformer-circuits.pub/2023/monosemantic-features/index.html

4. **[Meng et al., 2022]** Meng, K., Bau, D., Andonian, A., & Belinkov, Y. (2022). *Locating and Editing Factual Associations in GPT*. arXiv:2202.05262. https://arxiv.org/abs/2202.05262

5. **[Templeton et al., 2024]** Templeton, A., Conerly, T., Marcus, J., Lindsey, J., Bricken, T., Chen, B., Pearce, A., Citro, C., Ameisen, E., Jones, A., Cunningham, H., Turner, N. L., McDougall, C., MacDiarmid, M., Tamkin, A., Durmus, E., Hume, T., Mosconi, F., Freeman, C. D., Sumers, T. R., Rees, E., Batson, J., Jermyn, A., Carter, S., Olah, C., & Henighan, T. (2024). *Scaling Monosemanticity: Extracting Interpretable Features from Claude 3 Sonnet*. Transformer Circuits Thread. https://transformer-circuits.pub/2024/scaling-monosemanticity/

6. **[Ameisen et al., 2025]** Ameisen, E., Lindsey, J., Pearce, A., Gurnee, W., Turner, N. L., Chen, B., Citro, C., Abrahams, D., Carter, S., Hosmer, B., Marcus, J., Sklar, M., Templeton, A., Bricken, T., McDougall, C., Cunningham, H., Henighan, T., Jermyn, A., Jones, A., Persic, A., Qi, Z., Thompson, T. B., Zimmerman, S., Rivoire, K., Conerly, T., Olah, C., & Batson, J. (2025). *Circuit Tracing: Revealing Computational Graphs in Language Models*. Transformer Circuits Thread. https://transformer-circuits.pub/2025/attribution-graphs/methods.html

---

*報告生成日期：2026-06-07 | 引用論文：6 篇 | 字數（中英混合）：約 8,500 字符*

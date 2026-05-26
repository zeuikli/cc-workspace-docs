# AI Safety Evaluation, Red-Teaming and Adversarial Robustness — 深度研究報告

**日期**：2026-06-07 | **研究範圍**：LLM jailbreaks at scale, adversarial attacks on alignment, automated red-teaming, safety benchmarks, refusal mechanisms

---

## 執行摘要

大型語言模型（LLM）的安全評估領域正在從臨時性人工測試快速演進為系統化、自動化的對抗評估框架。關鍵發現如下：（1）現有防禦在自動化單輪攻擊上表現良好，但在多輪人工對話攻擊下成功率崩潰至 70% 以上 [Li et al., 2024]；（2）白箱訓練的對抗後綴可遷移至 ChatGPT、Bard、Claude 等閉源黑箱模型 [Zou et al., 2023]；（3）防禦文獻系統性高估了魯棒性，真正的自適應攻擊者可繞過 12 個聲稱近零漏洞的防禦系統 [Nasr et al., 2025]。本領域最緊迫的課題：建立能真實反映多輪對話威脅模型的評估標準，以及訓練出在實際對抗壓力下不崩潰的對齊機制。

---

## 1. 背景與動機

### 1.1 為什麼 LLM 安全評估如此重要

隨著大型語言模型被大規模部署於醫療、法律、金融及教育領域，其生成有害內容的潛在風險從學術問題升格為社會議題。傳統的人工內容審核無法跟上生成速度；RLHF（Reinforcement Learning from Human Feedback）雖大幅降低了有害輸出的基礎率，卻未能從根本上消除漏洞。

LLM 的「對齊稅」問題進一步複雜化了局面：過度的安全限制會導致模型拒絕合理請求（over-refusal），損害實用性；而過鬆的邊界則使惡意使用者能輕易獲取危險資訊。如何在安全性與實用性之間找到可量化、可系統測試的平衡點，是本領域的核心驅動力。

### 1.2 歷史演進脈絡

早期的 LLM 安全研究（2021 年前）主要依賴人工撰寫對抗提示（adversarial prompts），方法論零散、不可重現。2022 年，Perez et al. 提出用語言模型紅隊（red-team）其他語言模型的思路 [Perez et al., 2022]，開啟了「LLM vs. LLM」自動化評估的新紀元。同年，Anthropic 發表大規模人工紅隊研究，首次系統記錄了 RLHF 訓練在規模擴大時的安全收益 [Ganguli et al., 2022]。

2023 年，Zou et al. 的 GCG（Greedy Coordinate Gradient）攻擊方法震驚了社群：自動生成的對抗後綴不僅能在白箱模型上成功，還能轉移至閉源商業系統。這一發現從根本上動搖了「RLHF 對齊可防止推理期有害輸出」的假設。

2024-2025 年，領域重心從「能不能攻破」轉向「如何標準化評估」與「多輪對話攻擊的威脅模型」，誕生了 HarmBench、WildTeaming、MultiBreak、TeleAI-Safety 等系統性框架。

---

## 2. 核心概念分析

### 2.1 攻擊分類學

LLM 對抗攻擊可按三個維度分類：

**（a）訪問層級**
- **白箱攻擊（White-box）**：攻擊者可獲取模型梯度，適用如 GCG 的梯度優化方法。攻擊效力最強，但對閉源模型不直接適用。
- **黑箱攻擊（Black-box）**：僅能透過輸出觀測。WildTeaming 和 AutoRed 屬於此類，需靠查詢效率彌補資訊劣勢。
- **遷移攻擊（Transfer）**：在白箱模型訓練的攻擊字串，直接套用至黑箱目標。GCG 攻擊展現了跨模型遷移的驚人能力 [Zou et al., 2023]。

**（b）互動模式**
- **單輪攻擊（Single-turn）**：一次性提示，攻擊與防禦的計算成本均低。多數現有 benchmark 以此為主，導致對多輪場景下安全性的系統性高估。
- **多輪攻擊（Multi-turn）**：透過多輪對話逐步建立上下文、分解有害請求。Li et al. [2024] 和 MultiBreak [Song et al., 2025] 均顯示多輪攻擊可繞過單輪防禦設計的防禦機制，使 ASR（Attack Success Rate）從個位數躍升至 70%+。

**（c）語義多樣性**
- **模板型攻擊**：基於固定 prompt 模板（如角色扮演框架、虛構場景包裹）。易於防禦，只需識別模板特徵。
- **自適應攻擊（Adaptive）**：Nasr et al. [2025] 所定義的範式：攻擊者明確針對目標防禦的設計弱點調整策略，是最接近真實威脅者的測試場景。

### 2.2 防禦機制分類

| 防禦類型 | 代表方法 | 核心機制 | 已知弱點 |
|---------|---------|---------|---------|
| RLHF 對齊 | Anthropic RLHF、InstructGPT | 基於人類偏好獎勵塑造輸出分佈 | GCG 等梯度攻擊、多輪對話侵蝕 |
| 輸入過濾 | Perplexity filter、Llama Guard | 在推理前偵測惡意輸入 | 白話化對抗字串繞過 |
| 輸出分類 | Safety classifier | 後處理生成結果 | 分類器規避提示 |
| 機器遺忘（Machine Unlearning） | ROME、MEMIT | 從模型權重中移除有害知識 | 多輪對話壓力可恢復被「遺忘」知識 [Li et al., 2024] |
| 對抗訓練 | HarmBench 提出的方法 | 在訓練資料中加入對抗樣本 | 訓練-測試攻擊分佈不匹配 |

### 2.3 評估指標與問題

**攻擊成功率（ASR, Attack Success Rate）** 是最常用的指標，但定義本身存在分歧：部分研究以「生成有害內容」為標準，另一些以「通過自動分類器」為標準，導致跨論文比較困難。HarmBench 試圖標準化這一問題，引入由訓練好的評估模型（如 Llama-2-13b-cls）進行一致化 ASR 計算 [Mazeika et al., 2024]。

**Over-refusal 率** 是另一個關鍵但常被忽略的指標。WildJailbreak 資料集特別包含 131K 個「看似可疑但實際良性」的查詢，強調防禦設計必須同時控制誤報率 [Jiang et al., 2024]。

---

## 3. 關鍵論文與研究成果

### 3.1 HarmBench（Mazeika et al., 2024）— 標準化評估基礎設施

**arxiv: 2402.04249**

這是目前最重要的自動化紅隊評估框架。核心貢獻在於定義了四個功能類別的有害行為：標準行為（standard）、情境行為（contextual）、版權行為（copyright）、多模態行為（multimodal）。透過這一分類法，研究者能精確定位不同攻擊策略的效力邊界。

**規模**：對 18 種紅隊方法 × 33 個目標 LLM 及防禦系統進行交叉評估，是截至當時最大規模的系統比較研究。

**關鍵發現**：不同攻擊方法在不同模型上的效力差異極大，不存在「萬能攻擊」；對抗訓練方法在提升廣譜魯棒性方面效果顯著。開源程式碼（github.com/centerforaisafety/HarmBench）使攻擊-防禦的共同演進成為可能。

### 3.2 GCG 攻擊（Zou et al., 2023）— 打破黑箱邊界的遷移攻擊

**arxiv: 2307.15043**

Greedy Coordinate Gradient（GCG）是 2023 年最具影響力的安全論文之一。方法核心：在多個開源模型（如 LLaMA-2-Chat、Vicuna）和多種有害查詢上同時優化，生成一個通用的對抗後綴字串（adversarial suffix）。

**關鍵結果**：對白箱模型的 ASR 達 95%+；更重要的是，後綴在未參與訓練的閉源商業模型上同樣有效——ChatGPT ASR 88%、Claude ASR 84%（根據論文報告數字）。此發現從根本上質疑了「閉源模型因不可訪問梯度而天然安全」的假設。

**機制解釋**：不同 LLM 在相似預訓練語料庫上訓練，在表示空間上存在對齊特徵，使白箱訓練的對抗擾動在語義層面具有跨模型可遷移性。

### 3.3 Perez et al.（2022）— 自動化紅隊的奠基工作

**arxiv: 2202.03286**

這篇論文建立了「用 LM 紅隊 LM」的核心範式。將其應用於 280B 參數聊天機器人，發現了以下幾類問題：（1）仇恨言論與偏見；（2）人口統計學刻板印象；（3）訓練資料洩漏（含電話號碼）；（4）多輪對話中漸進性有害行為。

從零樣本提示到強化學習控制攻擊難度與多樣性，這一方法論框架奠定了後續所有自動化紅隊工作的基礎。

### 3.4 WildTeaming（Jiang et al., 2024）— 從真實用戶行為挖掘攻擊策略

**arxiv: 2406.18510**

現有紅隊研究多由研究者主動設計攻擊場景，WildTeaming 逆向思考：從真實用戶-聊天機器人互動日誌中挖掘野生攻擊策略，得到 5,700 個獨特的攻擊戰術叢集（jailbreak tactic clusters）。

**核心數字**：比研究者主導方法實現高出 4.6 倍的攻擊多樣性與成功率。生成的 WildJailbreak 資料集包含 262K 提示-回應對（131K 對抗 + 131K 良性），其中良性部分專門用於防止過度拒絕。

**方法啟示**：真實用戶的創造力和持續性超過了大多數研究者設計的攻擊場景，強調任何脫離實際部署環境的安全評估都存在生態效度問題。

### 3.5 Li et al.（2024）— 多輪人工攻擊揭示防禦虛假魯棒性

**arxiv: 2408.15221**

這是 2024 年最令人震驚的安全研究之一。研究者透過商業紅隊人員對 HarmBench 上表現最佳的防禦系統進行多輪人工攻擊。

**核心結果**：報告個位數 ASR 的防禦在多輪人工攻擊下 ASR 超過 70%。更令人警惕的是：設計用於「遺忘」生物安全知識的機器遺忘防禦，在多輪對話壓力下，被遺忘的知識被成功恢復。

釋出的 MHJ（Multi-Turn Human Jailbreaks）資料集包含 2,912 個提示、537 個多輪攻擊序列，是研究多輪威脅模型的重要資源。

### 3.6 Nasr et al.（2025）— 自適應攻擊者框架重定評估標準

**arxiv: 2510.09023**

這篇論文從認識論角度重構了安全評估方法論。核心主張：如果評估使用靜態攻擊字串或弱優化方法，得到的魯棒性數字沒有任何意義，因為真實威脅者會明確針對防禦設計弱點調整策略（attacker moves second）。

**結果**：對 12 種近期防禦系統，使用梯度下降、強化學習、隨機搜索與人工引導探索的自適應組合，ASR 在大多數防禦上超過 90%，而這些防禦原本報告的 ASR 接近 0%。

**方法論意義**：未來任何聲稱「魯棒」的防禦，必須包含自適應評估結果才算可信。

### 3.7 Ganguli et al.（2022）— Anthropic 規模化紅隊研究

**arxiv: 2209.07858**

Anthropic 系統研究了 3 個模型大小 × 4 種訓練方式（plain LM、prompted、RLHF-SL、RLHF-RL）的紅隊難度，釋出 38,961 個紅隊攻擊記錄。**核心發現**：RLHF 訓練模型隨規模增大越來越難被攻破，而 plain LM 的抵抗力隨規模幾乎不變。這是「對齊訓練確實提升對抗魯棒性」的早期系統證據。

---

## 4. 方法論比較

### 4.1 梯度優化 vs. 語言模型生成

| 維度 | 梯度優化（GCG 類） | LLM 生成（AutoRed、WildTeaming 類） |
|------|-----------------|-----------------------------------|
| 訪問需求 | 白箱（梯度） | 黑箱（僅查詢） |
| 攻擊語義性 | 低（token 字串常為亂碼） | 高（自然語言，難以過濾） |
| 可遷移性 | 中（跨模型有效但依賴架構相似性） | 高（語義攻擊更通用） |
| 計算成本 | 高 | 中 |
| 適用場景 | 學術評估、識別最壞情況 | 紅隊演習、資料集生成 |

梯度攻擊代表理論下界（最強攻擊），LLM 生成代表現實威脅面（最具生態效度）。兩者互補，不可相互取代。

### 4.2 單輪 vs. 多輪評估

現有 benchmark（包括 HarmBench 的大部分任務）仍以單輪為主。Li et al. [2024] 和 MultiBreak [Song et al., 2025] 的結果強烈表明，單輪 ASR 是對真實漏洞的下界估計，多輪評估應成為標準配置。

**MultiBreak 的主動學習方法論**（arxiv: 2605.01687）：使用迭代微調 + 不確定性採樣生成 10,389 個對抗提示，覆蓋 2,665 個有害意圖類別，是目前規模最大的多輪攻擊資料集之一。

### 4.3 TeleAI-Safety 統一框架

TeleAI-Safety [Chen et al., 2025]（arxiv: 2512.05485）採用不同路線：不選擇最強攻擊，而是最大化覆蓋面——19 種攻擊 × 29 種防禦 × 19 種評估方法的模組化組合，對 14 個 LLM 進行系統評估。代價是深度不如 HarmBench，優勢是暴露跨設計的系統性弱點。

---

## 5. 前沿趨勢與開放問題

### 5.1 2024-2025 年主要趨勢

**（a）多模態攻擊面擴張**：HarmBench 已設立多模態行為類別，視覺-語言模型的對齊評估開始系統化。圖像輸入的對抗擾動可繞過純文字安全訓練。

**（b）自動化紅隊生態成熟**：WildTeaming 的資料飛輪概念——從部署日誌中持續提取真實攻擊策略——代表了紅隊從「一次性測試」向「持續演進系統」的範式轉移。

**（c）機器遺忘的脆弱性**：Li et al. [2024] 揭示了「知識刪除」類防禦對多輪攻擊的脆弱性，引發對遺忘機制本身可靠性的質疑，這一問題在生物安全、化學武器等高危域尤為關鍵。

**（d）評估方法論反省**：Nasr et al. [2025] 的「自適應攻擊者」框架代表了對整個評估生態的元層面反省——不是研究「哪個防禦最好」，而是研究「如何評估防禦才不算說謊」。

### 5.2 主要開放問題

1. **多輪對話的正式威脅模型缺失**：目前沒有被廣泛接受的形式化定義「多輪對話攻擊者能力邊界」的框架。
2. **ASR 指標的語義一致性**：不同論文對「攻擊成功」的定義不統一，導致跨研究比較困難。
3. **對齊稅量化**：提升安全性對模型能力的具體代價仍缺乏精確、可重現的測量標準。
4. **遷移魯棒性**：在多語言、多文化脈絡下，對齊能力如何轉移？多數研究仍以英語為主。

---

## 6. 實踐意義與應用建議

### 6.1 對 AI 安全工程師

**評估管線設計**：採用 HarmBench 框架作為基礎，強制包含（1）單輪自動化攻擊（作為下界）、（2）多輪人工紅隊（作為現實威脅）、（3）自適應攻擊評估（作為魯棒性上界）。缺少任何一個維度都可能導致虛假安全感。

**防禦疊加原則**：避免單點防禦（例如只依賴輸入過濾或只依賴 RLHF）。TeleAI-Safety 的結果顯示，防禦組合效果通常優於任何單一防禦，但需注意疊加防禦的計算成本與 over-refusal 風險。

**機器遺忘不可單獨依賴**：如果安全需求涉及「使模型無法提供某類知識」（如生物安全），機器遺忘在多輪對話壓力下不可靠 [Li et al., 2024]。應配合運行時過濾和輸出監控。

### 6.2 對 LLM 產品開發者

**野生數據優先**：WildTeaming 的結果表明，從真實用戶互動中挖掘攻擊策略比研究者設計的場景更有效。有能力的開發者應建立部署後的持續對抗監控機制，而非依賴固定的紅隊結果。

**Over-refusal 監控**：安全性提升需同時量化對良性請求的誤拒率。WildJailbreak 的對比資料集設計是值得借鑒的方法——安全資料集中必須包含「良性但可疑」的查詢。

**多輪對話場景優先測試**：如部署聊天機器人，單輪測試的 ASR 數字幾乎不具參考價值。應建立多輪對話的系統性測試流程。

### 6.3 對研究者

**發表魯棒性聲明的最低標準**：依據 Nasr et al. [2025] 的建議，任何聲稱「防禦達到 X% ASR」的論文，必須包含自適應評估結果，方可視為可信聲明。論文審查者應將此列入標準檢查項。

---

## 7. 研究缺口與未來方向

**最緊迫的缺口**：

1. **多輪對話的正式評估協議**：目前 MHJ [Li et al., 2024] 和 MultiBreak [Song et al., 2025] 已邁出第一步，但尚無標準化的多輪威脅模型定義和攻擊者能力集定義。

2. **非英語語言的對齊評估**：絕大多數紅隊研究以英語為主，中文、阿拉伯語等語言中的安全漏洞尚未系統評估。語言切換（code-switching）也可能是未被充分探索的攻擊面。

3. **長期對齊穩定性**：在多輪對話中，隨著上下文累積，對齊行為如何衰退？目前缺乏系統性的「對齊疲勞」（alignment fatigue）研究。

4. **小模型的安全特性**：邊緣部署（edge deployment）下的小型 LLM 安全評估幾乎是空白。Ganguli et al. [2022] 的規模研究指出較小模型的 RLHF 效益不同，但對 sub-7B 模型的系統研究仍缺乏。

5. **攻擊-防禦的自動共同演進**：HarmBench 提供了基礎設施，但如何在不陷入 overfitting 的前提下讓攻擊和防禦共同進化，仍是開放的方法論問題。

---

## 附錄：參考文獻

1. **Mazeika, M., Phan, L., Yin, X., Zou, A., Wang, Z., Mu, N., Sakhaee, E., Li, N., Basart, S., Li, B., Forsyth, D., & Hendrycks, D.** (2024). *HarmBench: A Standardized Evaluation Framework for Automated Red Teaming and Robust Refusal*. arXiv:2402.04249. https://arxiv.org/abs/2402.04249

2. **Zou, A., Wang, Z., Carlini, N., Nasr, M., Kolter, J.Z., & Fredrikson, M.** (2023). *Universal and Transferable Adversarial Attacks on Aligned Language Models*. arXiv:2307.15043. https://arxiv.org/abs/2307.15043

3. **Perez, E., Huang, S., Song, F., Cai, T., Ring, R., Aslanides, J., Glaese, A., McAleese, N., & Irving, G.** (2022). *Red Teaming Language Models with Language Models*. arXiv:2202.03286. https://arxiv.org/abs/2202.03286

4. **Jiang, L., Rao, K., Han, S., Ettinger, A., Brahman, F., Kumar, S., Mireshghallah, N., Lu, X., Sap, M., Choi, Y., & Dziri, N.** (2024). *WildTeaming at Scale: From In-the-Wild Jailbreaks to (Adversarially) Safer Language Models*. arXiv:2406.18510. https://arxiv.org/abs/2406.18510

5. **Li, N., Han, Z., Steneker, I., Primack, W., Goodside, R., Zhang, H., Wang, Z., Menghini, C., & Yue, S.** (2024). *LLM Defenses Are Not Robust to Multi-Turn Human Jailbreaks Yet*. arXiv:2408.15221. https://arxiv.org/abs/2408.15221

6. **Nasr, M., Carlini, N., Sitawarin, C., Schulhoff, S.V., Hayes, J., Ilie, M., Pluto, J., Song, S., Chaudhari, H., Shumailov, I., Thakurta, A., Xiao, K.Y., Terzis, A., & Tramèr, F.** (2025). *The Attacker Moves Second: Stronger Adaptive Attacks Bypass Defenses Against LLM Jailbreaks and Prompt Injections*. arXiv:2510.09023. https://arxiv.org/abs/2510.09023

7. **Ganguli, D., Lovitt, L., Kernion, J., Askell, A., Bai, Y., Kadavath, S., Mann, B., Perez, E., Schiefer, N., Ndousse, K., ... & Clark, J.** (2022). *Red Teaming Language Models to Reduce Harms: Methods, Scaling Behaviors, and Lessons Learned*. arXiv:2209.07858. https://arxiv.org/abs/2209.07858

8. **Song, J., Liu, X., Yang, W., Chen, W., Feng, M., Zhu, X., & Gao, J.** (2025). *MultiBreak: A Scalable and Diverse Multi-turn Jailbreak Benchmark for Evaluating LLM Safety*. arXiv:2605.01687. https://arxiv.org/abs/2605.01687

9. **Chen, X., Zhao, J., He, Y., Xun, Y., Liu, X., Li, Y., Zhou, H., Cai, W., Shi, Z., Yuan, Y., Zhang, T., Zhang, C., & Li, X.** (2025). *TeleAI-Safety: A Comprehensive LLM Jailbreaking Benchmark Towards Attacks, Defenses, and Evaluations*. arXiv:2512.05485. https://arxiv.org/abs/2512.05485

10. **Diao, M., Mou, Y., He, K., Song, H., Zhao, L., Zhang, S., Ye, W., Liang, K., & Ma, Z.** (2025). *AutoRed: A Free-form Adversarial Prompt Generation Framework for Automated Red Teaming*. arXiv:2510.08329. https://arxiv.org/abs/2510.08329

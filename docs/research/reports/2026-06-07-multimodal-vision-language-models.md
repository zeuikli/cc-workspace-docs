# Multimodal Foundation Models: Vision-Language Integration — 深度研究報告

**日期**：2026-06-07 | **研究範圍**：GPT-4V, LLaVA, Flamingo, BLIP-2, InternVL, vision-language alignment, visual instruction tuning, multimodal reasoning

---

## 執行摘要

多模態基礎模型在 2022–2025 年間經歷了典範轉移：從端對端聯合訓練（Flamingo）到凍結主幹 + 輕量橋接（BLIP-2 Q-Former、LLaVA MLP connector），再到原生多模態預訓練（InternVL3）。關鍵洞見有三：（1）指令調優資料的質量遠重於量，LLaVA-1.5 僅用 1.2M 樣本即超越以百億參數訓練的競品；（2）視覺編碼器規模是重要瓶頸，InternVL 將 ViT 擴至 6B 參數才真正縮小視覺與語言能力的差距；（3）開源模型已逼近閉源前沿，InternVL3-78B 在 MMMU 達 72.2，與 GPT-4o 和 Claude 3.5 Sonnet 競爭力相當。

---

## 1. 背景與動機

### 1.1 問題起源：感知與推理的裂縫

大型語言模型（LLM）在純文字任務上的突破，暴露了一個根本缺陷：語言只是人類認知的子集。醫療診斷需要讀 X 光片、自動駕駛需要理解路況影像、科學研究需要解讀圖表——這些任務要求模型同時「看」與「說」。傳統的 Computer Vision 模型（ResNet、ViT）能識別影像，卻無法以自然語言推理；而 GPT-3、LLaMA 等 LLM 擅長推理，卻對視覺信號一無所知。

### 1.2 早期嘗試的局限

早期 VQA（Visual Question Answering）模型採用雙流架構，分別編碼影像與文字後接 fusion layer，但存在三個結構性問題：（a）閉集答案空間限制了泛化能力；（b）訓練目標與自然語言生成脫節；（c）無法利用 LLM 積累的世界知識。CLIP [Radford et al., 2021] 以對比學習橋接視覺與文字空間，雖是里程碑，但本質上仍是判別式模型，無法支撐開放式生成任務。

### 1.3 動機：通往視覺語言通才的路徑

理想的視覺語言模型（VLM）需要同時滿足：能以自然語言回答任意視覺問題（開放式）、能從極少示例泛化（few-shot）、能在不同任務間遷移、且訓練成本可承受。這三個目標——能力廣度、樣本效率、計算效率——之間存在根本張力，構成了 2022–2025 年多模態研究的核心議題。

---

## 2. 核心概念分析

### 2.1 三大架構典範

多模態 VLM 的設計空間圍繞一個核心問題：**如何讓視覺特徵與語言模型對話？** 當前主流答案分為三類。

**典範 A：端對端聯合訓練（Flamingo 路線）**

Flamingo [Alayrac et al., 2022] 將凍結的視覺編碼器（NFNet）與凍結的語言模型（Chinchilla）通過兩個可訓練組件連接：Perceiver Resampler（將可變長度視覺特徵壓縮為固定長度 token 序列）和 Gated Cross-Attention Dense Layers（插入 LLM 各層間的交叉注意力閘門）。關鍵創新在於 gating mechanism——每個交叉注意力層的輸出乘以一個可學習的 tanh gate，初始化為零，使模型在訓練早期保留語言能力，再逐漸融入視覺信息。這一設計讓 Flamingo 成為第一個支援交錯圖文序列少樣本學習的大規模 VLM。

**典範 B：輕量連接器 + 凍結雙塔（BLIP-2 / LLaVA 路線）**

BLIP-2 [Li et al., 2023] 提出 Q-Former（Querying Transformer），一個輕量的可訓練橋接模組，包含一組可學習的 query token，通過交叉注意力從凍結的視覺編碼器（ViT-G）提取信息，再通過線性投影輸入凍結的 LLM（OPT 或 FlanT5）。訓練分兩階段：第一階段用凍結 ViT 訓練 Q-Former 的視覺表徵學習；第二階段用凍結 LLM 訓練視覺到語言的生成能力。整個訓練只優化 Q-Former 的參數（~188M），可訓練參數比 Flamingo80B 少 54 倍，零樣本 VQAv2 仍超越 8.7%。

LLaVA [Liu et al., 2023] 採取更激進的極簡主義：CLIP ViT-L/14 作為視覺編碼器，一個單層線性投影作為 connector，Vicuna 作為 LLM。LLaVA-1.5 進一步將連接器升級為兩層 MLP，並換用 CLIP-ViT-L-336px。看似微小的改動，卻在 11 個標準測試基準上達到當時 SOTA，揭示了 connector 設計中「簡單有效」的反直覺結論：複雜的 Q-Former 不一定優於設計良好的 MLP。

**典範 C：原生多模態預訓練（InternVL3 路線）**

InternVL3 [Zhu et al., 2025] 代表最新的典範轉移：不再把「文字 LLM 接視覺插件」作為出發點，而是從預訓練階段就聯合學習多模態和語言能力。這要求同時提供多模態資料和純文字語料，讓模型在同一訓練階段內發展出整合的表徵，避免了「後貼合」架構中視覺與語言能力的不對稱。

### 2.2 視覺指令調優（Visual Instruction Tuning）

LLaVA 的另一核心貢獻是 **Visual Instruction Tuning** 範式。訓練資料的構建方式：利用純語言 GPT-4，給定圖片描述（caption）和邊界框（bounding box）等 symbolic 信息，生成多輪對話、詳細描述、複雜推理三種類型的指令追蹤資料。這一設計解決了高品質多模態對話資料的稀缺問題，以低成本（純 API 調用，無需人工標注）構建了足夠多樣的訓練信號。

### 2.3 視覺位置編碼與高解析度處理

標準 ViT 對輸入解析度有固定假設，限制了對細節豐富圖像的理解。LLaVA-OneVision 的 AnyRes 策略、InternVL3 的 Variable Visual Position Encoding（V2PE）都在解決同一問題：如何在不固定輸入大小的前提下，讓模型處理任意解析度的影像，並在多圖、影片等多幀場景下保持位置一致性。

---

## 3. 關鍵論文與研究成果

### 3.1 Flamingo（NeurIPS 2022）

**論文**：*Flamingo: a Visual Language Model for Few-Shot Learning* [Alayrac et al., 2022]

Flamingo 在 16 個 few-shot 視覺語言任務上取得 SOTA，包括 VQA、圖像描述、視頻問答。在 0-shot、4-shot 等設定下，Flamingo-80B 的性能在多個任務上超過之前的 fine-tuned SOTA。具體數字：VQAv2 zero-shot 56.3%，COCO captioning 4-shot CIDEr 84.3。更重要的是架構貢獻：Perceiver Resampler 將高維視覺特徵壓縮為固定 64 個 visual token，讓 LLM 的計算成本與圖像解析度解耦。Gated Cross-Attention 的設計哲學——初始化為零使原始 LLM 能力被保護——後來被廣泛借鑑。

### 3.2 BLIP-2（ICML 2023）

**論文**：*BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models* [Li et al., 2023]

Q-Former 的設計以參數效率為核心訴求。188M 可訓練參數的 BLIP-2 在 zero-shot VQAv2 上達 65.2%，超越 Flamingo-80B（56.3%）8.7 個百分點，而後者有超過 80B 參數。訓練成本同樣大幅降低：BLIP-2 僅需 8 張 A100 數天即可復現，而 Flamingo 的訓練耗費了大量 TPU 計算。Q-Former 的兩個注意力流——自注意力（query tokens 互相交互）與交叉注意力（query tokens 與視覺特徵交互）——分別處理語言對齊與視覺特徵提取，架構簡潔但功能分離清晰。此後 InstructBLIP、MiniGPT-4、Otter 等大量工作都直接採用 Q-Former 作為視覺橋接。

### 3.3 LLaVA 系列（NeurIPS 2023 Oral → CVPR 2024）

**論文**：*Visual Instruction Tuning* [Liu et al., 2023]；*Improved Baselines with Visual Instruction Tuning* [Liu et al., 2023]

LLaVA 原版（2023 年 4 月）的主要貢獻是方法論而非性能：證明了利用語言 GPT-4 生成的合成指令資料，可以有效訓練出具備 multimodal 對話能力的開源模型。在合成多模態指令追蹤數據集上，LLaVA 相對 GPT-4 達到 85.1% 的相對分數；在 ScienceQA 上結合 GPT-4 評分達到 92.53%（SOTA）。

LLaVA-1.5 的結果更具衝擊性：**單 MLP 連接器 + CLIP-ViT-L-336px** 在 11 個標準基準（VQAv2、GQA、TextVQA、MME、MMBench 等）全面超越之前複雜架構。訓練資料僅 1.2M 公開樣本，8 張 A100 約 1 天訓練完成。這一結果有力反駁了「連接器越複雜越好」的直覺，並將 LLaVA-1.5 確立為後續研究的通用強基線。

### 3.4 InternVL 系列（CVPR 2024 Oral → 2025）

**論文**：*InternVL: Scaling up Vision Foundation Models* [Chen et al., 2023]；*InternVL3* [Zhu et al., 2025]

InternVL 的核心賭注是：**視覺編碼器的規模是當前多模態系統最被低估的瓶頸**。CLIP ViT-L（307M 參數）與動輒 7–70B 的語言主幹之間存在嚴重的能力不對稱。InternVL 將視覺編碼器擴至 InternViT-6B，並通過 progressive alignment 策略，在大規模網路圖文資料上對齊視覺與語言表徵。最終在 32 個視覺語言基準上達到 SOTA，涵蓋圖像級識別、像素級分割、零樣本分類與檢索。

InternVL3（2025 年）進一步引入原生多模態預訓練：InternVL3-78B 在 MMMU（Massive Multidisciplinary Multimodal Understanding）達到 **72.2**，與閉源的 ChatGPT-4o 和 Claude 3.5 Sonnet 競爭力相當，同時是完全開源的。V2PE 允許模型處理更長的多模態上下文，MPO（Mixed Preference Optimization）則針對多模態偏好對齊做了特定優化。

### 3.5 LLaVA-OneVision（2024）

**論文**：*LLaVA-OneVision: Easy Visual Task Transfer* [Li et al., 2024]

首個在單圖、多圖、影片三種場景同時達到競爭性能的單一開源模型。AnyRes 策略將高解析度影像切分為動態數量的 tiles，每個 tile 獨立通過 ViT 編碼，再加上一個整體縮圖的全局 token，實現解析度無關的視覺處理。跨場景遷移是另一貢獻：以圖像訓練為主的模型，通過 task transfer 自然湧現出影片理解能力，印證了底層視覺表徵的通用性。模型覆蓋 0.5B 到 72B 參數尺度，提供靈活的部署選項。

---

## 4. 方法論比較

| 維度 | Flamingo 路線 | Q-Former 路線（BLIP-2） | MLP Connector 路線（LLaVA） | 原生多模態（InternVL3） |
|------|--------------|----------------------|--------------------------|----------------------|
| **可訓練參數** | 中（Gated Cross-Attn + Resampler） | 少（~188M Q-Former） | 極少（MLP only） | 全模型 |
| **Few-shot 能力** | 優秀（設計目標） | 有限 | 無（需 SFT） | 強（unified training） |
| **訓練成本** | 高（大規模 pre-training） | 低（分兩段凍結） | 最低（SFT 為主） | 高（joint pre-training） |
| **指令遵循** | 中 | 中 | 優秀 | 優秀 |
| **高解析度支援** | 有限 | 有限 | LLaVA-1.5+ 支援 | V2PE 原生支援 |
| **適用場景** | 多任務少樣本泛化 | 計算資源受限的應用 | 快速部署、研究基線 | 前沿性能目標 |

**選擇建議**：計算資源有限且需要 few-shot → Q-Former；快速構建研究基線 → LLaVA-1.5；追求 SOTA 且可接受完整訓練 → InternVL3 系列；需要視頻理解 → LLaVA-OneVision。

MLP connector 的反直覺優勢部分源於：Q-Former 的信息瓶頸（固定 32 個 query token）在需要細節的任務（如 OCR、圖表理解）中成為限制，而 MLP 保留了完整的視覺 token 序列。

---

## 5. 前沿趨勢與開放問題

### 5.1 2024–2025 年關鍵趨勢

**（1）原生多模態預訓練興起**：InternVL3 標誌著「文字 LLM + 視覺插件」的後貼合架構開始讓位給聯合預訓練。這一轉變在效果上提升了視覺語言的深度整合，但訓練複雜度和資料需求也成倍增加。

**（2）高解析度與多圖理解成為剛需**：現實應用（文件理解、醫療影像、多幀影片）要求模型處理遠超 224×224 的輸入。AnyRes、V2PE 等解決方案的湧現反映了這一需求從學術研究流向工程優化。

**（3）開源模型逼近閉源前沿**：InternVL3-78B（MMMU 72.2）、LLaVA-OneVision-72B 等模型已在多個基準上與 GPT-4V 並駕齊驅，開源生態的研究價值大幅提升。

**（4）多模態推理與思維鏈**：如何讓 VLM 在視覺輸入上展現類似 Chain-of-Thought 的逐步推理仍是開放問題。Test-time scaling（InternVL3 採用）是初步探索。

### 5.2 尚未解決的核心問題

- **幻覺（Hallucination）**：VLM 傾向生成視覺上不存在的物體或錯誤的空間關係，現有 RLHF/DPO 只能部分緩解。
- **細粒度視覺推理**：在需要計數、精確定位、小物體識別的任務上，當前模型與人類差距仍大。
- **跨模態一致性**：同一模型對「看起來相同」的影像可能產生截然不同的描述，展示了不穩定的特徵提取。
- **訓練資料偏差**：大規模網路爬取資料含有大量噪音與偏見，如何做多模態資料清理仍缺乏標準。

---

## 6. 實踐意義與應用建議

### 6.1 架構選型指引

**企業應用開發**：若目標是快速部署有效的多模態助理，LLaVA-1.5 或 LLaVA-OneVision（7B/13B）提供了最佳的「效能/成本」比。開源授權友善，社群資源豐富，fine-tuning 文件完整。

**計算資源受限場景**：BLIP-2 的 Q-Former 設計（凍結雙主幹、僅訓練橋接器）在 GPU 記憶體有限時仍能達到競爭性效果。適合邊緣部署或持續訓練預算受限的團隊。

**前沿研究 baseline**：建議以 LLaVA-1.5-13B 作為消融實驗的標準對照，其復現成本低（1 天 × 8×A100）且在 11 個基準有完整公開數字，對比公平性有保障。

### 6.2 訓練資料策略

LLaVA 系列的教訓明確：**資料品質優先於數量**。以下策略有實證支撐：

- 利用語言 GPT-4 或 Claude 生成合成指令資料（LLaVA 原始方法），成本低且多樣性高
- 混入學術 VQA 資料（GQA、TextVQA、OCR-VQA）時，需加入回應格式化提示（response formatting prompts），否則性能下降
- 避免大量重複的圖像描述資料（caption-only），對話格式的指令資料對 instruction following 能力貢獻更大

### 6.3 評估基準選擇

推薦多基準組合：**MMBench**（能力全面）+ **MMMU**（多學科推理）+ **TextVQA**（OCR 能力）+ **MME**（感知與認知）。單一基準評估存在過擬合風險，尤其需注意訓練資料是否包含評估集相近分佈。

### 6.4 工程最佳實踐

- 視覺 token 數量與 LLM context length 需匹配：AnyRes 在高解析度下可產生 1000+ visual token，在 context 窗有限的 LLM 上會截斷
- InternViT-6B 作為視覺編碼器需要獨立的 GPU 記憶體規劃，不能與 LLM 混合部署在同一 GPU
- 多模態資料的批次構建需注意 padding 策略：影像 token 序列長度差異大，動態批次比固定批次節省顯著 GPU 記憶體

---

## 7. 研究缺口與未來方向

**（1）視覺推理的可解釋性**：當 VLM 回答一個視覺問題時，哪些視覺區域對答案起關鍵作用？當前 attention map 可視化方法在多層 cross-attention 結構下仍不可靠，需要針對多模態設計的解釋性方法。

**（2）幻覺的根源理解**：幻覺究竟源於視覺特徵提取不足、語言先驗過強、還是訓練目標設計問題？現有研究多在症狀層面（後處理過濾、RLHF 抑制），根源理解不足。

**（3）多模態推理的 scaling law**：LLM 的 scaling law 已相對成熟，但對 VLM 而言，視覺編碼器規模、語言模型規模、訓練資料量之間的最優配比尚無系統研究。InternVL 的 InternViT-6B 是一個數據點，但多點系統性驗證仍缺失。

**（4）跨語言多模態能力**：現有 VLM 主要在英文資料上訓練，多語言視覺語言能力（特別是低資源語言）的開發幾乎是空白，具有重要的實用價值。

**（5）影片長序列理解**：當前影片 VLM 通常均勻採樣少量關鍵幀（8–16 frames），無法處理需要長時序推理的任務（1 小時影片的因果分析）。高效的長影片編碼策略是重要開放問題。

---

## 附錄：參考文獻

1. **[Alayrac et al., 2022]** Jean-Baptiste Alayrac et al. *Flamingo: a Visual Language Model for Few-Shot Learning.* NeurIPS 2022. arXiv:2204.14198.

2. **[Li et al., 2023]** Junnan Li, Dongxu Li, Silvio Savarese, Steven Hoi. *BLIP-2: Bootstrapping Language-Image Pre-training with Frozen Image Encoders and Large Language Models.* ICML 2023. arXiv:2301.12597.

3. **[Liu et al., 2023a]** Haotian Liu, Chunyuan Li, Qingyang Wu, Yong Jae Lee. *Visual Instruction Tuning.* NeurIPS 2023 Oral. arXiv:2304.08485.

4. **[Liu et al., 2023b]** Haotian Liu, Chunyuan Li, Yuheng Li, Yong Jae Lee. *Improved Baselines with Visual Instruction Tuning.* CVPR 2024. arXiv:2310.03744.

5. **[Chen et al., 2023]** Zhe Chen et al. *InternVL: Scaling up Vision Foundation Models and Aligning for Generic Visual-Linguistic Tasks.* CVPR 2024 Oral. arXiv:2312.14238.

6. **[Li et al., 2024]** Bo Li et al. *LLaVA-OneVision: Easy Visual Task Transfer.* arXiv:2408.03326.

7. **[Zhu et al., 2025]** Jinguo Zhu et al. *InternVL3: Exploring Advanced Training and Test-Time Recipes for Open-Source Multimodal Models.* arXiv:2504.10479.

8. **[Radford et al., 2021]** Alec Radford et al. *Learning Transferable Visual Models From Natural Language Supervision (CLIP).* ICML 2021.

---

*報告生成日期：2026-06-07 | 資料截止：2025 年 5 月 | 論文數量：7 篇核心 + 1 篇背景*

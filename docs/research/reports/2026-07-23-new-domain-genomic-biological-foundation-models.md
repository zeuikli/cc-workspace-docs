---
date: 2026-07-23
archived_items: 6
dedup_verified: True
domains: [genomic-biological-foundation-models]
grounded_sources: [2606.04525, 2606.22138, 2606.17115, 2606.3014, 2607.09526, 2607.17227]
source_routine: routine-e
type: new-domain-report
---

# 新領域研究報告 2026-07-23：基因體／生物基礎模型（Genomic/Biological Foundation Models）

## 執行摘要
基因體／生物基礎模型是把 DNA/RNA/蛋白質序列、三維結構、單細胞與空間轉錄體、病理全切片影像當作「生物語言」做大規模自監督預訓練的模型家族；本次探勘找到 6 篇近 90 天內一手 arxiv 論文，共同指向同一轉折點：預訓練紅利遞減、評測可比性與泛化脈絡依賴成為領域真正瓶頸，而非更大的模型。此領域與 workspace 現有版圖（agent harness／LLM 工程／GCP FinOps／SRE）完全正交，是本次探勘選定的唯一新領域（未湊數選第二個）。

## 為何是「新」領域（反回音室證明）
對核心關鍵詞（genom、biobank、biological-foundation、biomatrix、single-cell、transcriptom、dna-language、pathology、protein 等 9 組）分別執行 `grep -ic` 於三個既有集合：
- `/tmp/covered_topics.txt`（DAILY-TOPICS + WEEKLY-FOCUS 累積關鍵詞）：全部命中 0
- `/tmp/covered_paper_terms.txt`（research/papers/ 既收錄論文標題關鍵詞高頻詞）：全部命中 0
- `research/NEW-DOMAINS/covered_topics.txt`（過去 3 次 Routine E 已探勘領域持久化紀錄：neuromorphic-computing, formal-verification-robotics, active-inference, machine-unlearning, ai-topic-emergence-detection, neuro-symbolic-robot-policy）：全部命中 0

九組關鍵詞、三個獨立集合，命中數皆為 0（遠低於「< 3 = 新領域」門檻），確認非回音室內既有題。

## 領域概覽

### 核心問題 / 範式
生物基礎模型的重心已從「能不能在生物資料上預訓練」轉向「如何評測、比較與跨模態整合」。GENEB（arXiv:2606.04525）以 40 個基因體基礎模型跨 100 個任務、13 個功能類別做診斷式 benchmark，揭露模型爆量增生卻缺乏可比評測框架的核心痛點——各家 SOTA 宣稱難以獨立驗證。BioMatrix（arXiv:2606.22138）代表另一條路線：以 decoder-only 架構原生整合序列、結構與自然語言三模態，打破過去單模態專用模型的割裂。Harmonised benchmarking（arXiv:2607.17227）在單細胞／空間轉錄體上發現基礎模型的泛化能力高度依賴脈絡（context-dependent generalisation），對「通用生物表徵」的樂觀敘事提出反例。DNA Language Models 評估（arXiv:2606.30140）進一步質疑預訓練對下游 fine-tuning 任務的實際貢獻度，顯示紅利遞減訊號。整體而言，這個領域正處在「預訓練規模紅利見頂、評測與可信度成為瓶頸」的轉折點。

### 關鍵玩家 / 代表工作
- **評測／可比性危機（領域主軸）**：GENEB — 40 模型 × 100 任務診斷式 benchmark（arXiv:2606.04525）；Harmonised benchmarking — 單細胞/空間轉錄體，context-dependent generalisation（arXiv:2607.17227）。
- **多模態整合**：BioMatrix — 序列/結構/語言原生整合的 decoder-only 生物基礎模型（arXiv:2606.22138）。
- **DNA 語言模型**：預訓練對 fine-tuning 任務的實際效益評估（arXiv:2606.30140）。
- **病理/癌症應用**：ALICE — 融合 vision/vision-language/slide-level 專家的通用病理基礎模型（arXiv:2607.09526）；Probing/Fusion/Trustworthiness — WSI + transcriptomic 多模態癌症分析的系統性評測（arXiv:2606.17115）。

### 當前進展與開放問題
- **進展**：從單模態專用模型走向多模態原生整合（BioMatrix）；病理領域出現整合多層級專家的通用模型（ALICE）。
- **開放問題 1（評測不可比）**：缺乏標準化、診斷式 benchmark，SOTA 宣稱難以獨立驗證（GENEB）。
- **開放問題 2（泛化脈絡依賴）**：「通用生物表徵」的普適性被 harmonised benchmarking 證偽，泛化強依賴資料脈絡（arXiv:2607.17227）。
- **開放問題 3（可信度/融合）**：多模態融合（WSI+轉錄體）的 trustworthiness 尚未有共識評估框架（arXiv:2606.17115）。
- **開放問題 4（預訓練實際效益）**：DNA 語言模型研究質疑預訓練對下游 fine-tuning 的實際貢獻度，紅利遞減訊號（arXiv:2606.30140）。

## 對本 workspace 的潛在槓桿
- **[中等，待驗證] 評測方法論的跨域映射**：這批論文的共同痛點（模型增生、benchmark 不可比、self-reported SOTA 難驗證、泛化脈絡依賴）與 workspace 核心認識論（external-validation、不信 LLM 自評、Gate 選擇稽核、Oracle 資格先於 loop）同構。GENEB 的「診斷式 benchmark」與 harness 的「gate 須行使實際執行路徑非 proxy 子集」是同一問題的兩個領域投影，可作為 harness eval 設計的外部佐證/類比素材。待驗證：GENEB 診斷維度能否抽象為領域無關的 benchmark-integrity 原則，或僅為 domain-specific，需後續閱讀原文確認。
- **[弱，待驗證] Oracle/泛化教訓**：Harmonised benchmarking 的「context-dependent generalisation」呼應 harness 的「測試須以未見輸入抽驗泛化」，可作為 LESSONS 層「評測泛化陷阱」的跨域案例，非行動項。
- **[薄弱，僅供觀察] FinOps/基礎設施角度**：biobank-scale 生物基礎模型訓練屬 GPU/HPC 密集工作負載，理論上與 owner 的 FinOps/GPU cluster ops 專長有接觸面，但屬通用大模型訓練成本議題，非本領域獨有洞見，連結薄弱，不構成引入理由。
- **[無連結] Agent harness 內容本身**：與 agent 行為契約、委派拓撲、SRE/K8s-Kafka ops 無直接內容連結。本領域價值定位為「刻意跳出回音室的視野擴張 + 評測方法論的類比鏡子」，非可立即落地的 skill/rule 素材——誠實結論：觀察型收錄，非立即行動項。

## 收錄來源
- "GENEB: Why Genomic Models Are Hard to Compare" (Ledneva, Nuridinov, Kuznetsov, 2026-06-03) — research/papers/2026-07-23-geneb-genomic-model-comparability-2606-04525.md — https://arxiv.org/abs/2606.04525
- "BioMatrix: Towards a Comprehensive Biological Foundation Model Spanning the Modality Matrix of Sequences, Structures, and Language" (Pei et al., 2026-06-20) — research/papers/2026-07-23-biomatrix-multimodal-biological-foundation-model-2606-22138.md — https://arxiv.org/abs/2606.22138
- "Probing, Fusion, and Trustworthiness: A Systematic Evaluation of Foundation Model Representations for Multimodal Cancer Analysis" (Hu et al., 2026-06-15) — research/papers/2026-07-23-cancer-foundation-model-trustworthiness-2606-17115.md — https://arxiv.org/abs/2606.17115
- "DNA Language Models: An Assessment of Pre-Training for Fine-Tuning Tasks" (Karpinsky, Mozziconacci, Delcey, 2026-06-29) — research/papers/2026-07-23-dna-language-model-pretraining-assessment-2606-30140.md — https://arxiv.org/abs/2606.30140
- "ALICE: Learning a General-Purpose Pathology Foundation Model from Vision, Vision-Language, and Slide-Level Experts" (Li et al., 2026-07-10) — research/papers/2026-07-23-alice-pathology-foundation-model-2607-09526.md — https://arxiv.org/abs/2607.09526
- "Harmonised benchmarking of foundation models for single-cell and spatial transcriptomics reveals context-dependent generalisation" (Chen et al., 2026-07-19) — research/papers/2026-07-23-harmonised-benchmarking-single-cell-transcriptomics-2607-17227.md — https://arxiv.org/abs/2607.17227

所有六個 arxiv_id 已於本 session 逐一以 WebFetch 直接讀取 arxiv.org/abs/ 頁面核對標題、作者與送件日期，非僅憑搜尋摘要臆測（避免 2026-06-28 報告曾發生的「/tmp 暫存不可覆核」問題重演）。published_date 範圍 2026-06-03 至 2026-07-19，全數落在 90 天前沿性門檻（cutoff 2026-04-24）內。

## 後續追蹤建議
- 若 GENEB 的診斷式 benchmark 維度確認可抽象為領域無關原則，值得納入下次 harness-meta eval 設計時的外部參照案例（非本次直接行動）。
- 本領域屬「觀察型」收錄，暫不建議納入 WEEKLY-FOCUS 常態追蹤；下次 Routine E 若持續看到「評測可比性」為多個獨立領域的共通瓶頸信號，可考慮拉高優先級。

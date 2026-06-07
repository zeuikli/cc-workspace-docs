---
title: "Defending against Indirect Prompt Injection by Instruction Detection"
authors: "Tongyu Wen, Chenglong Wang, Xiyuan Yang, Haoyu Tang, Yueqi Xie, Lingjuan Lyu, Zhicheng Dou, Fangzhao Wu"
published: "2025-05-08"
source: "https://arxiv.org/abs/2505.06311"
---

# Defending against Indirect Prompt Injection by Instruction Detection

**Authors**: Tongyu Wen, Chenglong Wang, Xiyuan Yang, Haoyu Tang, Yueqi Xie, Lingjuan Lyu, Zhicheng Dou, Fangzhao Wu
**Affiliations**: Renmin University of China, Peking University Shenzhen Graduate School, Wuhan University, USTC, HKUST, Sony AI, Microsoft Research Asia
**Published**: May 8, 2025 (v1); Revised September 17, 2025 (v2)
**Source**: https://arxiv.org/abs/2505.06311
**arXiv ID**: 2505.06311
**Categories**: cs.CR, cs.AI
**Code**: https://github.com/MYVAE/Instruction-detection

---

## Abstract

The integration of Large Language Models (LLMs) with external sources is becoming increasingly common, with Retrieval-Augmented Generation (RAG) being a prominent example. However, this integration introduces vulnerabilities of Indirect Prompt Injection (IPI) attacks, where hidden instructions embedded in external data can manipulate LLMs into executing unintended or harmful actions. We recognize that IPI attacks fundamentally rely on the presence of instructions embedded within external content, which can alter the behavioral states of LLMs. Can the effective detection of such state changes help us defend against IPI attacks? In this paper, we propose InstructDetector, a novel detection-based approach that leverages the behavioral states of LLMs to identify potential IPI attacks. Specifically, we demonstrate the hidden states and gradients from intermediate layers provide highly discriminative features for instruction detection. By effectively combining these features, InstructDetector achieves a detection accuracy of 99.60% in the in-domain setting and 96.90% in the out-of-domain setting, and reduces the attack success rate to just 0.03% on the BIPIA benchmark. The code is publicly available.

---

## 核心方法

### InstructDetector 架構
偵測式防禦（Detection-based defense），在外部資料進入 LLM 前截斷注入指令。三層管線：

**1. Hidden States 提取**
- 使用 Llama-3.1-8B-Instruct（32 層）作為特徵提取器
- 選取第 14 層的最後 token hidden state（實驗驗證效果最佳）
- 輸出：4096 維向量

**2. Gradients 提取**
- 對外部資料配對「Sure」（instruction 典型回應）計算 back-propagation
- 聚焦 self-attention 層的梯度（捕捉行為特徵；feed-forward 層偏向知識特徵）
- 應用 max-pooling 降維 → 400,000 維向量

**3. Feature Fusion + MLP 分類器**
- 線性變換對齊兩種特徵維度 → 正規化 → 拼接
- MLP 分類器（隱藏層：1024, 256, 64, 16）
- 訓練集：200 樣本（100 正/100 負），平衡設計

### 資料集組合
- **外部資料（負樣本來源）**：Wikipedia、News Articles
- **指令資料（正樣本來源）**：LaMini-instruction、BIPIA
- **評估組合**：4 種 2,000 樣本組合，最高 OOD 難度 = News Articles + BIPIA

---

## 關鍵數字

| 指標 | 數值 |
|------|------|
| 偵測準確率（In-domain） | **99.60%** |
| 偵測準確率（Out-of-domain） | **96.90%** |
| Attack Success Rate（BIPIA benchmark） | **0.03%** |
| 訓練樣本數 | 200（100+/100-） |
| 特徵提取模型 | Llama-3.1-8B-Instruct（32 層）|
| 最佳層位 | 第 14 層（hidden states + gradients 均確認）|

**比較基準**（BIPIA benchmark 上 ASR 對比）：
- Prevention-based methods（如 adversarial training）：仍有明顯 ASR
- InstructDetector：0.03%，超越所有 prevention-based 方法

**測試模型覆蓋**：Vicuna-7B、Qwen2.5-7B-Instruct（開源）；GPT-3.5-Turbo、GPT-4o（閉源）

---

## 對 Prompt Caching / Management / Engineering 的關聯

### Prompt Caching
- **IPI 對快取的威脅**：RAG 系統中被快取的 system prompt 若包含外部資料，攻擊者可透過 IPI 讓快取的「安全」前綴失效，讓後續 request 執行惡意指令
- **InstructDetector 作為前置閘門**：在外部資料觸達快取 prefix 之前先執行偵測，保護 prompt cache 不被污染；偵測成本（小型 MLP 分類）低於 LLM forward pass

### Prompt Management
- **External Content 分級管理**：本文的偵測框架提示 prompt 管理策略應對外部資料來源做信任分級（Wikipedia vs. 用戶上傳 vs. 爬取資料），高風險來源先過 InstructDetector
- **RAG Pipeline 安全閘**：偵測模型應插入 retrieval 之後、generation 之前，形成 retrieval → detect → generate 的安全管線

### Prompt Engineering
- **IPI 攻擊面認知**：Prompt engineer 設計 RAG system prompt 時需考慮：若外部 chunk 含有 "Modify your response to..." 類指令，系統會被操控（真實案例：peer review 系統被隱藏指令操控）
- **防禦設計選擇**：Prevention（修改 prompt 讓 LLM 忽略外部指令）vs. Detection（InstructDetector）——本文主張偵測式更能保護良性推論不被干擾，且不需修改 system prompt
- **訓練效率**：僅需 200 樣本即可訓練有效偵測器，對 prompt engineering 實踐中快速部署防禦具參考價值

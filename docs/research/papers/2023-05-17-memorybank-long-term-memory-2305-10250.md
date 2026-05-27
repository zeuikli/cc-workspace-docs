---
title: "MemoryBank: Enhancing Large Language Models with Long-Term Memory"
authors: Wanjun Zhong, Lianghong Guo, Qiqi Gao, He Ye, Yanlin Wang
published: 2023-05-17
source: "https://arxiv.org/abs/2305.10250"
venue: AAAI 2024
---

# MemoryBank: Enhancing Large Language Models with Long-Term Memory

**Authors**: Wanjun Zhong, Lianghong Guo, Qiqi Gao, He Ye, Yanlin Wang  
**Affiliations**: Sun Yat-sen University; Shenzhen Institute of Computing Sciences  
**Published**: May 17, 2023  
**Venue**: AAAI 2024, volume 38, pages 19724–19731  
**Source**: https://arxiv.org/abs/2305.10250  
**arXiv ID**: 2305.10250  
**Categories**: cs.CL, cs.AI

---

## Abstract

Unlike humans who can remember, forget, and learn from past interactions, large language models lack long-term memory capabilities. We propose MemoryBank, a novel memory mechanism tailored for LLMs that enables them to summon relevant memories, continually evolve through continuous memory updates, and comprehend and adapt to user personality. Inspired by the Ebbinghaus Forgetting Curve theory, MemoryBank mimics the process of human memory strengthening through consistent recall and allows old memories to fade with time. The system is demonstrated through SiliconFriend, a long-term AI companion chatbot, showing improved contextual understanding and empathetic responses in extended interactions.

---

## 核心創新：Ebbinghaus 遺忘曲線記憶機制

人類記憶的兩個關鍵特性：
1. **頻繁回想 → 記憶增強**（Repetition strengthens retention）
2. **時間流逝 → 記憶衰退**（Time causes forgetting without reinforcement）

MemoryBank 將 Ebbinghaus 遺忘曲線應用到記憶管理：

```
記憶強度 R = e^(-t/S)

其中：
- R = 記憶保留率（0-1）
- t = 自上次回憶以來的時間
- S = 記憶強度（隨每次成功回憶增加）
```

**記憶強度更新**：
```
每次成功召回該記憶 → S 增加（該記憶更難被遺忘）
長時間未召回 → R 自然衰減
R < 閾值 → 記憶自動淡出（模擬遺忘）
```

---

## 系統架構

### 記憶存儲層
```
用戶交互 → 事件提取 → 記憶條目
記憶條目 = {
  "content": "用戶提到明天有重要會議",
  "timestamp": "2023-05-17T14:30:00",
  "strength": 1.0,  // 初始強度
  "last_access": "2023-05-17T14:30:00",
  "embedding": [0.23, -0.15, ...]  // 向量嵌入
}
```

### 記憶檢索層
1. **語義搜索**：輸入查詢 → 向量相似度 → Top-K 相關記憶
2. **時間過濾**：記憶強度 R > 閾值方才返回
3. **重要性加權**：某些記憶（如用戶偏好）永久保留

### 用戶畫像模塊
從記憶中動態提取用戶特征：
- 個人偏好（喜好的話題、食物、習慣）
- 情感狀態變化軌跡
- 關係網絡（提到的人物及其關係）

---

## SiliconFriend：長期 AI 伴侶

**核心任務**：扮演用戶的長期 AI 朋友，跨越多日/月的對話中保持連貫性。

**示例場景**：

```
[Day 1]
用戶：我今天開始學習 Python 了！
SiliconFriend：太棒了！Python 非常適合初學者，你打算從哪方面開始？

[Day 14]  
用戶：最近有點沮喪。
SiliconFriend：上次你說要學 Python，學習進度怎麼樣了？有什麼
地方遇到困難嗎？有時候學習瓶頸會讓人感到沮喪。
```

MemoryBank 讓 SiliconFriend 記住「14 天前用戶提到開始學 Python」，並主動連接當前情緒狀態。

---

## 實驗評估

### 評估維度
| 維度 | 評估方式 | 結果 |
|------|---------|------|
| 記憶召回準確率 | 測試能否正確引用過去事件 | 顯著優於無記憶基線 |
| 個性理解 | 對用戶特征的準確描述 | 優於 ChatGPT 基線 |
| 回應連貫性 | 跨時間對話的一致性評分 | 人類評估顯著改善 |

### 基線比較
- **無記憶 ChatGPT**：每次對話全新開始，無歷史感知
- **簡單摘要法**：固定長度摘要，不考慮記憶強度
- **MemoryBank**：Ebbinghaus 機制 + 向量檢索

---

## 局限性與後繼研究

1. **遺忘準確性**：遺忘曲線的參數（S 的初始值、閾值）需要人工調整
2. **用戶個性建模的準確性**：從對話中提取的特征可能不準確
3. **不同用戶的差異化**：同樣的衰減參數適用於所有用戶嗎？

**後繼研究（在本 workspace 的相關論文）**：
- MemoryOS（2506.06326）：加入分層儲存，改進 MemoryBank 的平面結構
- A-MEM（2502.12110）：改進為知識圖網絡，解決孤立記憶問題
- 2605.12978：指出 MemoryBank 等系統的整合問題——Ebbinghaus 衰減+整合可能加速記憶失真

---

## 引用

```bibtex
@inproceedings{zhong2024memorybank,
  title={MemoryBank: Enhancing Large Language Models with Long-Term Memory},
  author={Zhong, Wanjun and Guo, Lianghong and Gao, Qiqi and Ye, He and Wang, Yanlin},
  booktitle={Proceedings of AAAI 2024},
  volume={38},
  pages={19724--19731},
  year={2024}
}
```

---

**關鍵詞**: 長期記憶, Ebbinghaus 遺忘曲線, 記憶強化, 用戶畫像, AI 伴侶, 個性化

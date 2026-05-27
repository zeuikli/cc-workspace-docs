---
title: "Voyager: An Open-Ended Embodied Agent with Large Language Models"
authors: Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, Anima Anandkumar
published: 2023-05-25
source: "https://arxiv.org/abs/2305.16291"
venue: NeurIPS 2023
---

# Voyager: An Open-Ended Embodied Agent with Large Language Models

**Authors**: Guanzhi Wang, Yuqi Xie, Yunfan Jiang, Ajay Mandlekar, Chaowei Xiao, Yuke Zhu, Linxi Fan, Anima Anandkumar  
**Affiliations**: NVIDIA; Caltech; UT Austin; Stanford University  
**Published**: May 25, 2023 (v1); revised October 19, 2023 (v2)  
**Venue**: NeurIPS 2023  
**Source**: https://arxiv.org/abs/2305.16291  
**arXiv ID**: 2305.16291  
**GitHub**: https://github.com/MineDreamer/Voyager  
**Categories**: cs.AI, cs.LG, cs.RO

---

## Abstract

We introduce Voyager, the first LLM-powered embodied lifelong learning agent in Minecraft that continuously explores the world, acquires diverse skills, and makes novel discoveries without human intervention. Voyager consists of three key components: (1) an automatic curriculum that maximizes exploration, (2) an ever-growing skill library of executable code for storing and retrieving complex behaviors, and (3) a new iterative prompting mechanism that incorporates environment feedback, execution errors, and self-verification for program improvement. Voyager interacts with GPT-4 as a black box without any model parameter fine-tuning and achieves exceptional proficiency in playing Minecraft. It obtains 3.3× more unique items, travels 2.3× longer distances, and unlocks key tech tree milestones up to 15.3× faster than the state of the art. Voyager is able to utilize the learned skill library in a new Minecraft world to solve novel tasks from scratch, while other techniques struggle to generalize.

---

## 核心創新：可執行技能庫（Skill Library）

Voyager 的記憶系統不是儲存文字描述，而是儲存**可執行的 Python 代碼**：

```python
# 技能庫中的一個技能示例
async def craftWoodenSword(bot):
    """製作木劍：需要木材和木棍"""
    await bot.craftItem('wooden_sword', 1)
    
# 更複雜的組合技能（由 Voyager 自動生成）
async def exploreCave(bot):
    """探索洞穴並收集資源"""
    await bot.equipItem('torch')
    await navigateToNearestCave(bot)
    await collectResources(bot, ['iron_ore', 'coal'])
```

**關鍵特性**：
- **Temporally extended**：技能可以是多步操作序列
- **Interpretable**：人類可讀的 Python 代碼
- **Compositional**：新技能可以調用舊技能

---

## 三大核心組件

### 1. 自動課程（Automatic Curriculum）
- 基於當前技能水平和環境狀態，動態生成下一個探索目標
- GPT-4 根據「最大化探索範圍」原則選擇任務
- 避免重複執行已掌握的技能（防止停滯）

### 2. 技能庫（Skill Library）—— 持久記憶層
```
新任務 → GPT-4 嘗試生成技能代碼
       → 執行測試（在 Minecraft 環境中）
       → 自我驗證（GPT-4 檢查是否達成目標）
       → 成功 → 存入技能庫
       → 失敗 → 根據錯誤訊息重新生成（最多 3 次）
```

技能庫索引機制：
- 向量嵌入（代碼描述）
- 關鍵字搜索
- 相關任務時自動召回相似技能

### 3. 迭代提示機制（Iterative Prompting）
```
環境觀察 → GPT-4 生成代碼 → 執行
          ↑                    ↓
          └── 錯誤信息 + 自驗 ──┘
                    （最多 N 輪）
```

---

## 實驗結果

### 探索指標（vs. ReAct, Reflexion, AutoGPT）

| 指標 | SOTA | Voyager | 倍數提升 |
|------|------|---------|---------|
| 獨特物品收集 | 基線 | 3.3× 更多 | **3.3×** |
| 旅行距離 | 基線 | 2.3× 更長 | **2.3×** |
| 技術樹解鎖速度 | 基線 | 15.3× 更快 | **15.3×** |

### 泛化能力
在全新 Minecraft 世界從零開始，Voyager 能利用技能庫中的知識：
- 解決新奇任務（never-seen objectives）
- 其他方法（ReAct, AutoGPT）在新世界幾乎無法泛化

---

## 記憶設計的關鍵洞見

### 代碼作為記憶的優勢（vs. 文字摘要）
| 特性 | 代碼記憶（Voyager） | 文字記憶（Generative Agents 等） |
|------|-------------------|---------------------------------|
| 精確性 | 可精確執行 | 可能模糊 |
| 可組合性 | 直接函數調用 | 需要 LLM 解析 |
| 可驗證性 | 執行即驗證 | 依賴 LLM 自評 |
| 壓縮失真 | 無（代碼不壓縮） | 有（文字摘要丟失細節）|
| 泛化能力 | 跨場景可執行 | 受語言歧義影響 |

**與 2605.12978 的關係**：Voyager 的代碼技能庫實際上是一種**不需要 consolidation 的記憶形式**——技能一旦生成並驗證，就以精確、可執行的形式保存，無需後期整合重寫。這避免了 2605.12978 發現的記憶退化問題。

---

## 局限性

1. **領域特定**：設計針對 Minecraft，泛化到其他環境需額外工程
2. **代碼執行環境依賴**：需要可執行的沙盒環境
3. **GPT-4 依賴**：黑盒 API 調用，延遲高，成本高
4. **技能庫增長管理**：隨著技能增加，檢索質量可能下降

---

## 引用

```bibtex
@article{wang2023voyager,
  title={Voyager: An Open-Ended Embodied Agent with Large Language Models},
  author={Wang, Guanzhi and Xie, Yuqi and Jiang, Yunfan and Mandlekar, Ajay and Xiao, Chaowei and Zhu, Yuke and Fan, Linxi and Anandkumar, Anima},
  journal={arXiv preprint arXiv:2305.16291},
  year={2023}
}
```

---

**關鍵詞**: 具身代理人, 終身學習, 技能庫, 代碼記憶, Minecraft, 自動課程, 泛化

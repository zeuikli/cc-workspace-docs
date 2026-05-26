# CalBench: Evaluating Coordination-Privacy Trade-offs in Multi-Agent LLMs

**ArXiv**: 2605.09823 | **Date**: 2026-05-10 | **Authors**: Chelsea Zou, Yiheng Yao, Selena She, Robert D. Hawkins | **Category**: cs.MA

## 摘要

首個針對多 agent LLM 協調-隱私權衡的系統性評估框架。核心設定：N 個 agent 各自擁有私有日曆（含現有承諾），必須協作排定 M 個新會議，同時最小化衝突。

**關鍵特性**：「沒有任何 agent 可以存取其他 agent 的私有日曆，但所有 agent 仍必須達成相互一致的決定。」

## 核心創新

### Oracle 解答 + DCOP 基準

每個場景包含最優 Oracle 解，使協調品質可通過「實際成本 / 最優成本」精確量化。分散式約束最優化（DCOP）基準提供在相同隱私約束下的公平比較。

### 隱私評估

日曆條目附有不同敏感度的私有語義上下文，測量 agent 在協商過程中是否無意洩漏任務無關的私有資訊。

## 四大評估維度

| 維度 | 描述 |
|------|------|
| 協調品質 | 相對最優解的會議排定效能 |
| 通訊效率 | 達成共識所需資源 |
| 公平性 | 各參與者間衝突成本的均等分配 |
| 隱私洩漏 | 敏感資訊的無意洩漏程度 |

## 與現有基準的區別

**強制去中心化**：不允許能力強的單一 agent 替代整個群體，確保評估真實的去中心化協調。

相比 MultiAgentBench（2503.01935）：
- MultiAgentBench：多種協作競爭場景
- CalBench：聚焦隱私邊界下的協調

## 對 Workspace 的意義

在多 agent 系統中處理敏感資訊時（如用戶資料、API 密鑰、私有業務邏輯），CalBench 提供了評估隱私保護效果的框架模型。

與 `2026-04-13-safeharness-lifecycle-security` 互補：
- SafeHarness：執行路徑安全（38% UBR 削減）
- CalBench：多 agent 協調中的資訊隱私

## 分類

**Benchmark & Evaluation / Safety & Alignment** — 首個協調-隱私權衡評估框架，填補多 agent 系統在隱私約束下協調能力評估的空白。

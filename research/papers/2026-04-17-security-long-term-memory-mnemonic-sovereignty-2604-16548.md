# A Survey on the Security of Long-Term Memory in LLM Agents: Toward Mnemonic Sovereignty

**ArXiv**: 2604.16548 | **Date**: 2026-04-17 | **Authors**: Zehao Lin, Chunyu Li, Kai Chen | **Category**: cs.CR, cs.AI

## 摘要

首篇針對 LLM agent 長期記憶安全性的系統性綜述。安全研究重心正從靜態訓練資料洩漏轉向動態威脅：「擁有持續長期記憶的系統是否可以跨 session 被持續塑造、投毒、未授權存取，以及跨共享組織狀態傳播？」63 頁，7 圖，10 表。

## 核心框架：記憶生命週期安全

六個操作階段 × 四個安全目標的矩陣：

**操作階段**：Write → Store → Retrieve → Execute → Share → Forget/Rollback

**安全目標**：完整性（Integrity）、機密性（Confidentiality）、可用性（Availability）、治理（Governance）

## 主要發現

### 文獻分佈失衡

現有研究高度集中在 Write 和 Retrieve 時的完整性攻擊，以下領域「研究稀少」：
- 機密性威脅
- 可用性攻擊
- Storage/Forgetting 機制
- 良性持久性失敗

### 治理空白

目前無任何已發表的架構完整實作論文所識別的**9 個治理原語**。

### LLM 作為記憶安全工具

使用 LLM 本身來強化記憶安全「仍然稀少但至關重要」。

## 核心概念：Mnemonic Sovereignty（記憶主權）

定義：「對寫入內容、讀取者、更新授權時機、可遺忘狀態的**可驗證、可恢復的治理**。」

將記憶治理品質定位為未來安全 agent 系統的核心差異化指標，與傳統的召回容量並列。

## 攻擊向量分類

| 攻擊類型 | 描述 |
|---------|------|
| 記憶投毒（Memory Poisoning） | 惡意寫入影響後續行為 |
| 記憶提取（Extraction） | 未授權讀取私密資訊 |
| 檢索腐化（Retrieval Corruption） | 操縱 RAG 查詢結果 |
| 控制流劫持（Control-flow Hijacking） | 通過記憶影響 agent 行為路徑 |
| 跨 agent 傳播（Cross-agent Propagation） | 共享記憶庫中的病毒式擴散 |
| 回滾機制（Rollback） | 防止或強制記憶狀態恢復 |

## 對 Workspace 的意義

與 `2026-05-13-useful-memories-faulty-llm` 形成互補：
- 前者研究**認知失真**（整合引入的準確率損失）
- 本文研究**安全威脅**（惡意行為者對記憶系統的攻擊）

生產環境記憶系統需要同時防範：認知退化（整合失真）+ 安全威脅（惡意投毒）。

## 分類

**Memory Architecture / Safety & Alignment** — 記憶安全的第一篇系統性綜述，Mnemonic Sovereignty 框架為評估 agent 記憶系統的安全成熟度提供標準。

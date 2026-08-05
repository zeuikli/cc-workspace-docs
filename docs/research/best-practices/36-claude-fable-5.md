# Claude Fable 5 與 Mythos 5 完整指南

> 來源：[Claude Fable 5 and Claude Mythos 5](https://www.anthropic.com/news/claude-fable-5-mythos-5)（2026-06-09）  
> 來源：[Introducing Claude Fable 5 and Claude Mythos 5](https://platform.claude.com/docs/en/about-claude/models/introducing-claude-fable-5-and-claude-mythos-5)  
> 來源：[Prompting Claude Fable 5](https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/prompting-claude-fable-5)  
> 整理日期：2026-06-15

---

## 模型定位

**Claude Fable 5** 是 Anthropic 目前公開可用的最強模型，為 Mythos-class 模型加上安全分類器後的普及版本。

**Claude Mythos 5** 與 Fable 5 共用同一底層模型，但安全分類器在特定領域寬鬆——僅限 Project Glasswing 受邀客戶使用。

---

## 技術規格

| 規格 | 值 |
|------|-----|
| Model ID | `claude-fable-5` / `claude-mythos-5` |
| Context window | 1M token（預設） |
| 最大輸出 token | 128k per request |
| 輸入定價 | $10 / MTok |
| 輸出定價 | $50 / MTok |
| 發布日期 | 2026-06-09 |

**可用平台**：Claude API、Claude Platform on AWS、Amazon Bedrock、Vertex AI、Microsoft Foundry

---

## 訂閱方案訪問

| 期間 | 行為 |
|------|------|
| 2026-06-09 ~ 06-22（已到期） | 包含於 Pro/Max/Team/Enterprise 訂閱方案額度中（不額外收費）|
| 2026-06-23 起（**現況**） | 需使用 Usage Credits（以 API 費率計費）|
| Opus 4.8 / Sonnet 4.5 / Haiku 3.5 | 仍包含於 Max 方案，不額外計費 |

---

## 安全分類器（Fable 5 特有）

Fable 5 有自動路由機制——當請求觸及以下領域時，自動切換至 Claude Opus 4.8 回應：

- **Cybersecurity**（漏洞利用、惡意程式）
- **Biology & Chemistry**（危害性合成）
- **Distillation**（模型提取）

平均觸發率 < 5% 的 sessions。用戶會看到模型切換通知。

---

## 基準測試表現

| 評測 | 結果 |
|------|------|
| **ViBench**（vibe-coding 端到端） | 最高分 |
| **FrontierBench**（Cognition 前沿 coding eval） | 最高分 |
| **Analytics benchmark**（複雜長時分析任務） | 首次突破 90%（比 Opus 4.8 高 10 分） |
| **Spreadsheet suite** | 每個 effort 等級均優於 Opus 4.8，且速度快 25–30% |
| **SWE-bench** | SOTA（軟體工程整體） |

---

## 與 Opus 4.8 的行為差異

### 1. 主動稽核

Fable 5 長時間自主執行時容易產生「幻想進度」。需在 prompt 中明確要求：

```
在回報進度前，請逐一對照本 session 的工具結果稽核每項聲明，
只回報有工具輸出為憑的工作；未驗證的項目請明確標示「待確認」。
```

### 2. Subagent 委派更積極

Fable 5 比以往模型更主動派發平行 subagent。需在 prompt 中明確定義委派時機，並優先使用非同步通訊（orchestrator 不阻塞等待每個 subagent 返回）。

### 3. 記憶與學習

Fable 5 能充分利用跨 session 的經驗紀錄。建議提供學習記錄位置（如 Markdown 檔案），每條記錄：
- 一行標題摘要
- 校正內容或已確認的方法

### 4. 說明問題 vs 請求變更

Fable 5 需要明確的行為分類器。建議在 system prompt 加入：

```
當用戶是在描述問題、提問或思考方向，而非請求實際變更時，
你的輸出應是評估意見（assessment），而非程式碼變更。
```

---

## Prompt Caching 注意事項

- Fable 5 的快取與 Opus 4.8 的快取**不相容**（各自獨立）
- 若從 Opus 4.8 遷移至 Fable 5，**整個快取需重建**
- Mid-session 不可切換模型（快取失效）
- Fable 5 安全分類器路由至 Opus 4.8 的 session 也不共享快取

---

## 模型選擇建議（對照 Opus 4.8）

| 情境 | 推薦模型 |
|------|---------|
| 複雜長時間 coding 任務（codebase 遷移、全 audit） | **Fable 5** |
| Vibe-coding / 試作 / 端到端自主任務 | **Fable 5** |
| 需要長時間分析或試算表作業 | **Fable 5**（快 25-30%） |
| 涉及 cybersecurity / bio-chem 主題 | **Opus 4.8**（直接指定，避免自動路由） |
| 預算敏感的 batch 處理 | **Opus 4.8 / Sonnet 4.6** |
| Fast mode 低延遲 | **Fable 5**（$10/$50 同價，約 Opus 4.8 standard 2.5× 速） |

---

## 延伸閱讀

- `05-claude-prompting-best-practices.md` — Effort 等級、XML 標籤、Agentic 系統設計
- `32-dynamic-workflows.md` — Fable 5 原生支援 dynamic workflow
- `04-subagent-mcp-skill.md` — Subagent 委派策略（Fable 5 更積極委派）

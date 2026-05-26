# Lecture 01：Claude Code 與 Harness 基礎

## 學習目標

完成本課後，你將能夠：

- 解釋 `Agent = Model + Body + Harness` 三層等式的本質區別
- 列舉量化數據說明為什麼「先修 Harness，再換模型」
- 識別 Agent 失敗的五個層級並進行歸因診斷
- 描述 Claude Code 的 Agentic Loop 三個階段

## 核心概念

### Agentic Loop：Claude Code 如何工作

Claude Code 透過三個階段解決問題，且各階段會彼此交織：

| 階段 | 說明 |
|------|------|
| **Gather context** | 搜尋檔案、讀取程式碼、理解環境 |
| **Take action** | 編輯檔案、執行指令、查詢 web |
| **Verify results** | 跑測試、對比截圖、確認輸出 |

Loop 依任務自動調整：一個問題可能只需要 context gathering；一個 bug fix 則反覆循環三個階段數十次。你可以隨時中斷 Claude 重新引導。

**核心定義**：Claude Code 是 Claude 的 **agentic harness**，提供 tools、context 管理、執行環境，讓語言模型成為能力完整的 coding agent。

### Agent = Model + Body + Harness

原始等式來自 LangChain / Viv Trivedy：

```
Agent = Model + Harness
```

> 「If you're not the model, you're the harness. A harness is every piece of code, configuration, and execution logic that isn't the model itself. A raw model is not an agent.」
> — Viv Trivedy, LangChain

Zeuik 在此基礎上精化為三層等式：

```
Agent = Model + Body + Harness
```

| 層 | 定義 | 解的問題 | 典型組件 |
|----|------|---------|---------|
| **Model** | 大腦，intelligence 本身 | 推理、理解、生成 | GPT-5 / Claude Opus 4.7 |
| **Body** | 手腳，能力延伸 | 能不能做事 | bash、filesystem、MCP、browser、sandbox |
| **Harness** | 約束，行為校準 | 會不會做歪 | CLAUDE.md、hooks、planner-evaluator、sub-agent 結構 |

**關鍵區分**：Body 解決「能力存在」，Harness 解決「行為可預測」。沒有手腳的大腦只能空想；沒有約束的手腳會做歪。

### 量化數據：Harness 的效能貢獻

這不是理論，是實驗數據。

**Terminal-Bench 2.0：同模型不同 Harness 的分數差距**

Claude Opus 4.6 在相同 benchmark 上：

| Harness | 準確度 |
|---------|--------|
| ForgeCode | 79.8% ± 1.6 |
| Capy | 75.3% ± 2.4 |
| TongAgents | 71.9% ± 2.7 |
| Crux | 66.9% |

**結論：同一個 Opus 4.6，不同 Harness 造成 13pp 分數差距。**

其他數據點：
- Stanford Meta-Harness 研究：同模型，59.6% → 76.4%（16.8pp 差距）
- Ewan Mak 實地案例（Claude Sonnet 4.6）：58% → 81%（harness 優化後，23pp 提升）
- AHE 論文：69.7% → 77.0%（10 次自動 harness 迭代，7.3pp 提升）

**各來源的一致結論**：
- Addy Osmani：「decent model + great harness beats great model + bad harness」
- Masood：「企業 AI 失敗的 65% 源自 harness 層缺陷，而非模型」
- LangChain 案例：只改 harness（system prompt、tools、middleware、tracing、self-verification），讓 coding agent 在 Terminal Bench 2.0 上從 Top 30 進到 Top 5

**實踐結論**：在當前投資報酬率下，優化 Harness > 等待新模型版本。

### Anthropic 對照實驗：同一匹馬，兩種命運

Anthropic 做過一個對照實驗。同一個 prompt（「做一個 2D 復古遊戲編輯器」），同一個模型（Opus 4.5）：

- **裸跑**：20 分鐘，花了 $9，遊戲核心功能根本跑不起來
- **完整 Harness**（planner + generator + evaluator 三 agent 架構）：6 小時，花了 $200，遊戲可以正常遊玩

模型沒換。Opus 4.5 還是那個 Opus 4.5。換的是馬具。

### Agent 為何失敗：五層防禦框架

| 層 | 常見失敗模式 | 診斷問題 |
|----|------------|---------|
| **任務規範** | 需求不清晰，agent 自己猜 | 有沒有明確的 Definition of Done？ |
| **上下文供給** | 隱含架構約定沒有告訴 agent | CLAUDE.md 有沒有說清楚技術棧？ |
| **執行環境** | 依賴缺失、版本不對 | 環境有沒有 init.sh 或準備步驟？ |
| **驗證反饋** | 沒有測試、沒有 lint | 有沒有可執行的驗收命令？ |
| **狀態管理** | 跨 session 遺忘上次發現 | 有沒有 MEMORY.md 或 progress file？ |

**診斷循環（核心方法論）**：執行 → 觀察失敗 → 定位到 harness 的哪一層出了問題 → 修補那一層 → 重新執行

### Context 焦慮：一個特殊的失敗模式

Anthropic 觀察到一個值得單獨標記的現象：當 agent 感覺上下文快滿了，它們會匆忙結束當前工作，跳過驗證步驟，選一個簡單的方案而不是最優方案。

這叫「上下文焦慮」（Context Anxiety）——跟你考試時發現時間快到了趕緊隨便選幾個選擇題是一回事。Harness 工程的任務之一，就是在上下文管理層面提前預防這種情況。

### Harness 的 11 大構件（Stanford 分類）

1. Orchestration loop
2. Tools
3. Filesystem
4. Bash / Code execution
5. Sandbox
6. Memory
7. Context management
8. **Context rot defense**（最容易被忽略）
9. Long-horizon execution
10. Error handling / Guardrails
11. Serving layer

### Harness 的永久性

| 類型 | 會被模型進步解掉嗎？ |
|------|-------------------|
| **補弱點型**（sub-agent 做 context isolation、early-stop 機制） | 會（隨模型增強逐漸退場） |
| **校準型**（hooks、verification、planner-evaluator） | 永遠不會消失 |

Harness 解的是 non-determinism 這個結構問題，不是 model 弱的問題。Deterministic 驗證、行為邊界校準——這些需求不會因為模型變強而消失。

## 程式碼範例

### 建立最小 CLAUDE.md（Harness 的第一步）

```markdown
# My Project

## 技術棧
- Python 3.12, FastAPI, PostgreSQL 16, Redis
- 套件管理：uv（不用 pip）
- 測試：pytest

## 驗證命令
```bash
pytest tests/ -q && python -m mypy src/ --strict
```

## 架構約定
- API handlers 放在 `src/api/handlers/`
- 所有新 endpoint 必須通過 OAuth 2.0 認證
- 錯誤處理統一使用 `src/utils/errors.py` 的模式

## 完成定義（Definition of Done）
一項任務完成 = 所有測試通過 + mypy 無錯誤 + lint 無警告
```

### 顯式的完成定義（取代模糊需求）

```
# ❌ 錯誤的任務描述
"加個搜索功能"

# ✅ 正確的任務描述，含完成定義
完成標準：
- 新增 GET /api/search?q=xxx 端點
- 支援分頁，預設 20 筆
- 返回結果包含高亮片段
- 所有新程式碼通過 pytest
- 類型檢查通過（mypy --strict）
```

### CLAUDE.md 的快速初始化

```bash
# 在專案根目錄執行，自動分析 codebase 生成起始 CLAUDE.md
/init
```

## 常見問題與注意事項

**Q：現在 context window 已經很大了，Context Rot 還是問題嗎？**

A：是的。Chroma 的 NIAH（needle-in-a-haystack）研究顯示，18 個模型在 context 增長後全部性能下降。甚至有悖論：邏輯連貫的 haystack 反而表現比隨機排列更差（18 個模型一致）。1M context window 是虛假安全感。

**Q：應該在什麼時候考慮升級模型？**

A：先把 Harness 的五層防禦都建立好之後，如果還是系統性失敗，再考慮模型升級。大多數情況下，問題在 Harness 而不在模型。

**Q：Anthropic April 23 Postmortem 說的是什麼？**

A：2026 年 3-4 月，Claude Code 品質下滑的三個根因全是 Harness 級變更：

| 事件 | 變更內容 | 影響 |
|------|---------|------|
| Reasoning effort 降級 | default: high → medium | 「Claude 感覺不夠聰明」 |
| Caching loop bug | thinking history 每輪清空（應每小時） | 「forgetful and repetitive」 |
| Verbosity 限制 | 系統提示加 ≤25/≤100 words 限制 | Opus coding 品質下降 3% |

官方承認：「The models themselves were not to blame, but three separate issues in the Claude Code harness caused complex but material problems.」

這是 Harness 改一行就能讓整個 output 分布跑掉的直接證據。

## 本課小結

- **Agent = Model + Body + Harness**。Body 解決「能不能做事」，Harness 解決「會不會做歪」。
- **量化數據**：同一個模型，不同 Harness 造成 7-23pp 的效能差距。優化 Harness 的投資報酬率 ≥ 升級模型。
- **五層診斷框架**：任務規範、上下文供給、執行環境、驗證反饋、狀態管理——失敗時逐層排查。
- **核心行動**：先建立 CLAUDE.md（帶明確完成定義）+ 驗證命令。這是 Harness 工程投入產出比最高的第一步。
- **Harness 是永久性工程**：校準型 Harness（hooks、verification、planner-evaluator）不會因模型變強而消失。

## 延伸閱讀

- [Lecture 02：CLAUDE.md 設計](/lectures/lecture-02-claude-md/) — 從這裡開始建立你的 Harness
- [Lecture 04：Harness 三層架構](/lectures/lecture-04-harness-architecture/) — Planner/Generator/Evaluator 設計模式
- [OpenAI: Harness engineering — leveraging Codex in an agent-first world](https://openai.com/index/harness-engineering/)
- [Anthropic: Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
- [Anthropic: April 23 Postmortem](https://www.anthropic.com/engineering/april-23-postmortem)

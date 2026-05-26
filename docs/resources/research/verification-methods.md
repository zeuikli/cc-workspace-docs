# Harness 驗證方法論

> 來源：2026-05-19 深度研究報告（overnight-research × autoresearch 交叉研究）

回答三個核心問題：
1. 如何驗證 Harness 產出的品質？
2. 如何實作 Harness 驗證管道？
3. 如何持續完善 Harness 準則？

---

## 為什麼 Harness 驗證比模型升級更重要

核心數據：

| 案例 | 介入 | 效果 |
|------|------|------|
| Terminal-Bench 2.0 | 同 Opus 4.6，純 harness 改進 | **52.8% → 66.5%**（+13.7pp，不換模型）|
| Can.ac | 工具格式調整一項 | 6.7% → 68.3%（**10 倍提升**）|
| SWE-Bench Pro | 同 Opus 4.5，三種 harness | 50.2%–55.4%（5.2pp 差距）|
| Claude Code vs Codex CLI | 不同 harness | 92.1% vs 77.3%（**14.8pp** 差距）|
| Mnilax 8 週測試 | 12 rules，50 tasks × 30 codebases | 41% → 3% 錯誤率 |

**統計顯著性**：88% AI agent 專案無法上線，主因 harness 太脆弱（Pinggy.io 統計）。

> Tejas Kumar（IBM, AI Engineer Europe 2026）的 Live Demo 結論：「整個 demo 中從未修改 prompt，只加了 verify step + guardrail + deterministic login handler，agent 從失敗到成功。」

---

## 雙層驗證架構

### 確定性驗證 vs LLM-as-Judge

| 驗證類型 | 適用場景 | 工具 | 代價 |
|---------|---------|------|------|
| **確定性驗證** | 工具選擇、格式合規、schema 驗證、測試通過 | grep / pytest / lint / bash script | 零 API 成本 |
| **LLM-as-Judge** | 語意品質、目標對齊、回應相關性、多步驟連貫性 | 獨立 LLM（非生成用的模型）| API 成本 + 延遲 |

**關鍵原則**：
- 確定性驗證是 ground truth，不可妥協
- LLM-as-Judge 補充語意品質——**評估模型必須不同於生成模型**（用 GPT-4 評估 Claude 輸出，或反之），否則分數通膨
- Trajectory Analysis（軌跡分析）優於純結果驗證：確保 agent 沒有通過有缺陷的邏輯得到正確答案

---

## Harness 品質的三個維度

外部研究（QuitTool, 2026）識別三個維度：

1. **可回放性（Replayability）**：失敗是否可以重現？可診斷？
2. **儀器化（Instrumentation）**：執行軌跡是否完整記錄（每個 tool call、每個 thought）？
3. **邊界明確性（Bounded Costs）**：驗證開銷和重試邏輯是否有上限，不會無限螺旋？

---

## 生產級 12-Metric 框架

外部研究（Towards Data Science，100+ 部署案例）識別的生產環境 12 個核心指標：

### 四層指標架構

| 層次 | 指標 | 目標值 | 驗證方法 |
|------|------|--------|---------|
| **Retrieval** | Context Relevance | > 0.85 | LLM-as-judge 0-1 評分 |
| | Context Recall | > 0.90 | 對比 human-labeled ground truth |
| | Retrieval Latency | p95 < 200ms | APM timing |
| **Generation** | Answer Faithfulness | > 0.95 | LLM-as-judge |
| | Hallucination Rate | < 2% | 5% 生產流量抽樣 |
| | Answer Relevance | > 0.90 | 語意相似度比較 |
| **Agent** | Tool Selection Accuracy | > 0.92 | labeled dataset 對比 |
| | Tool Execution Success | > 0.98 | 每次 tool call 成功/失敗追蹤 |
| | Multi-Step Coherence | > 0.85 | Trace-level 邏輯流評估 |
| **Production** | Cost per Query | < $0.05 | Token + API 成本加總 |
| | P99 Latency | < 3s | 端到端計時 |
| | Loop Rate | 0% | 重複動作模式偵測 |

### 實作順序（三週建立）

**Week 1-2（基礎層）**：確定性驗證 + Answer Faithfulness
**Week 2-3（代理層）**：Tool Selection Accuracy + Multi-Step Coherence
**Week 3+（生產層）**：Cost per Query + P99 Latency + Loop Rate

---

## K×M 雙準則框架

從 cc-workspace 55 輪迭代測試提煉的雙成功條件：

```
成功條件 1：total_tok ≤ 3,500（可量測：bash scripts/measure.sh）
成功條件 2：K×M 得分 ≥ 90（可量測：per-rule 語意評估矩陣）
```

| 維度 | 滿分 | 核心問法 |
|------|------|---------|
| K1（Karpathy Simplicity）| 20 | 「移除後 Claude 下次會在哪個場景犯錯？」|
| K2（Karpathy No-Speculation）| 10 | 「有無新增未來可能需要的規則？」|
| K3（Karpathy Surgical）| 10 | 「有無觸及任務以外的規則？」|
| M1（7 核心規則完整）| 30 | 核心行為動詞 100% 保留 |
| M2（數字精確）| 15 | 所有限制數字完整 |
| M3（4 層依賴完整）| 10 | 規則觸發詞可連結到對應行為 |
| M4（Token 達標）| 5 | ≤ 3,500 tok |

---

## 語意驗證 vs grep 驗證

一個關鍵的驗證陷阱：**grep 關鍵詞通過 ≠ 語意完整**。

失敗案例：規則合併後，兩個關鍵詞都存在（grep 通過），但合併後文字在 context 壓力下 Claude 可能只執行其中一個行為。

**正確的語意驗證問題**：「在 context 壓力下，這兩個行為要求合併後，Claude 會只觸發其中一個嗎？」—— 不是問「關鍵詞是否存在？」

---

## Ratchet 升格機制

每個驗證失敗都是自動升格的觸發點：

```
驗證失敗
  ↓
分析：這是「人工遵守率」問題 還是「需要程式碼強制」問題？
  ↓
人工遵守率 × 違反成本 → 決定升格方式
  ↓
低頻+低成本 → 留在 CLAUDE.md 規則
中頻+中成本 → 升格為 PostToolUse hook（自動驗證）
高頻+高成本 → 升格為 PreToolUse hook（阻斷執行）
極高成本   → 升格為 git hook / CI 強制
```

---

## 驗證工具範例

### 基礎確定性驗證腳本

```bash
#!/bin/bash
# verify-output.sh — 基礎驗證框架

ERRORS=0

# 1. Token 數量檢查
TOKEN_COUNT=$(cat "$1" | wc -w)
if [ "$TOKEN_COUNT" -gt 3500 ]; then
  echo "FAIL: Token count $TOKEN_COUNT exceeds 3500" >&2
  ERRORS=$((ERRORS + 1))
fi

# 2. 必要關鍵詞存在性
REQUIRED_KEYWORDS=("重要" "必須" "不得")
for kw in "${REQUIRED_KEYWORDS[@]}"; do
  if ! grep -q "$kw" "$1"; then
    echo "FAIL: Required keyword '$kw' not found" >&2
    ERRORS=$((ERRORS + 1))
  fi
done

# 3. 禁止模式
BANNED_PATTERNS=("TODO" "FIXME" "PLACEHOLDER")
for pattern in "${BANNED_PATTERNS[@]}"; do
  if grep -q "$pattern" "$1"; then
    echo "FAIL: Banned pattern '$pattern' found" >&2
    ERRORS=$((ERRORS + 1))
  fi
fi

if [ "$ERRORS" -eq 0 ]; then
  echo "PASS: All checks passed"
  exit 0
else
  echo "FAIL: $ERRORS check(s) failed"
  exit 2
fi
```

### PostToolUse 驗證 Hook

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "command": "~/.claude/hooks/verify-output.sh"
          }
        ]
      }
    ]
  }
}
```

---

## 延伸閱讀

- [Hooks 設計模式](/resources/best-practices/hooks)
- [Model-Harness Fit](/resources/research/model-harness-fit)
- [Harness Engineering 研究全景](/resources/research/harness-engineering/)
- [Lecture 04：Harness 三層架構](/lectures/lecture-04-harness-architecture/)

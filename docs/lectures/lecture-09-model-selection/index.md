# Lecture 09：模型選型與 Effort 經濟學

## 學習目標

完成本課後，你將能夠：

- 用 class × effort 的二維框架選模型，而不是只挑一個「最好的模型」
- 解釋為什麼「每 token 多少錢」不等於「每個任務多少錢」
- 設計 Advisor 架構，用 worker + supervisor 取得大部分能力而不付全額成本
- 判斷該升級模型還是該提高 effort（兩者解決的問題不同）
- 說明換模型對 prompt cache 的破壞性影響，並設計不觸發它的作法

## 核心概念

### 官方選型原則：從最強往下調

> 從「目前一般可用的最聰明模型」起步，再依延遲、成本、任務難度往下調——**不要從便宜模型往上爬**。

以及一個容易被忽略的否定：選型依據是**任務難度、延遲要求、存取限制與單位經濟**，**不是產業別**。官方明言每個 Claude 模型都受訓於 coding、agentic 與知識工作，不存在「金融用這個、醫療用那個」的分法。

### 四個 class 的定位

| Class | 定位 | 典型用途 |
|-------|------|---------|
| **Mythos / Fable** | 前沿能力層（Mythos 受限存取；Fable 為含安全機制的公開版）| 最難的長跑任務、需要最強判斷 |
| **Opus** | 推理密集 | 架構決策、深度分析、agentic 主控 |
| **Sonnet** | 日常工作與高量 sub-agent | 實作、批次、workers |
| **Haiku** | 成本敏感、高頻 | 分類、路由、簡單提取 |

官方在《Choosing a Claude model and effort level》裡給了一個好用的比喻：**Fable 是見過罕見問題的專家、Opus 是有深度經驗的專家、Sonnet 是能力強的通才**。

### 現役模型規格（截至 2026-08）

| Model | ID | 輸入 | 輸出 | Context | 備註 |
|-------|-----|------|------|---------|------|
| **Claude Fable 5** | `claude-fable-5` | $10/MTok | $50/MTok | 1M | 最強公開模型；128k 輸出上限；2026-06-09 GA |
| **Claude Mythos 5** | `claude-mythos-5` | $10/MTok | $50/MTok | 1M | Project Glasswing 受邀限定；無安全分類器 |
| **Claude Opus 5** | `claude-opus-5` | $5/MTok | $25/MTok | 1M | 2026-07-24；Claude Max 預設、Pro 可用最強；low/medium/high effort |
| **Claude Sonnet 5** | `claude-sonnet-5` | $2/MTok（促銷至 08-31，後 $3）| $10/MTok（後 $15）| 1M | CLI 預設模型（v2.1.197）|
| **Claude Haiku 4.5** | `claude-haiku-4-5-20251001` | $0.25/MTok | $1.25/MTok | — | 速度/成本最優 |

**Opus 5 的 benchmark**（官方公布）：Frontier-Bench v0.1 為 Opus 4.8 的 **2 倍**；CursorBench 3.2 與 Fable 5 差距 **< 0.5%** 而成本減半；ARC-AGI 3 為次佳模型的 3 倍；OSWorld 2.0 優於 Fable 5 且成本為其 1/3。

**Fast mode**：Opus 5 約 2.5× 速度、2× 價格（$10/$50）。注意 Fable 5 的 standard 價格同為 $10/$50，兩者不要混淆。

### Effort：這一節是本課的核心

**模型決定能力範圍，effort 決定投入多少。** 官方的定義非常具體：effort 影響 Claude 讀幾個檔案、驗證幾次、執行多深。

| Effort | 適用 |
|--------|------|
| `max` | 極難問題，可能過度思考 |
| `xhigh` | 多數 coding / agentic 任務 |
| `high` | 多數智力敏感任務的最低建議值 |
| `medium` | 降低 token，犧牲一定智力 |
| `low` | 短、範圍小、延遲敏感的任務 |

**該升級模型還是該提高 effort？** 這是兩個不同的診斷：

| 症狀 | 處方 |
|------|------|
| Claude **跳過檔案**、未執行測試、放棄多步驟任務 | 提高 **effort** |
| 任務需要模型**不具備的知識或推理深度** | 升級 **模型** |
| 例行工作、已知模式的重複 | 降低 **模型** class 省成本 |

官方還加了一句克制的建議：**大多數情況應該用模型的預設 effort**，把它當成通用偏好而非逐任務調整的旋鈕。

### 為什麼「每 token 價格」是錯的指標

這是本課最重要的觀念：

> **高 class 模型跑低 effort，有時 per-task 經濟性優於低 class 模型**——即使 per-token 價格較高。

原因是完成同一任務所需的 token 更少、重試更少。官方在兩篇文章裡都講了同一件事：「較大模型在複雜多步任務上可能更經濟，因為需要較少迭代達成目標」。

實務上的意涵：**比較模型時要算「完成這個任務的總成本」，而不是看價目表**。而要算得出來，你需要 eval（見下）。

### Effort 造出的是一個連續面

Effort 讓「品質 × 速度 × 成本」從離散的模型選擇變成連續的取捨面。同一個 Opus 5 在 low 與 high 之間的表現與成本差距，可能大於 Opus 5 與 Sonnet 5 之間的差距。所以正確的選型單位是 **class × effort**，不是 class。

### Advisor 策略：官方實測數字

用較快的 worker 模型搭配較聰明的 advisor 模型做監督：

> **Sonnet + Fable 監督 = Fable-only 效能的 90%，成本為 63%。**

API 層的 Advisor Tool 讓 executor 在生成中途向 advisor 諮詢戰略指引。運作方式值得理解，因為它決定了成本結構：

1. Executor 決定呼叫 advisor（如同任何工具）
2. Anthropic server 端執行獨立推理，**把 executor 的完整 transcript 傳給 advisor**（含 system prompt、所有 tools、所有對話歷史）
3. Advisor 回應透過 `advisor_tool_result` block 回到 executor
4. Executor 繼續生成，受 advice 引導

全部在**單一 `/v1/messages` 請求內**完成，不需要額外 round trip。Advisor 自身不帶 tools、不做 context 管理，其 thinking blocks 在回傳前被丟棄——只有 advice text 到達 executor。

**典型 advisor 輸出**：400–700 text tokens（含思考共 1,400–1,800 tokens）。Advisor 的 token 以 advisor 模型費率**獨立計費**，頂層 `usage` 只反映 executor tokens。

**限制**：Advisor 必須 ≥ Executor 的能力等級，否則 API 回 `400 invalid_request_error`。

### Claude Code 裡的 Advisor 模式

不用 API 也能做同樣的事——用 subagent：

- **Sonnet 主執行**：驅動任務、讀寫檔案、呼叫工具、逐步推進
- **Opus 幕後顧問**：僅在關鍵時刻提供策略建議

| 該諮詢高檔位 | 不需要諮詢 |
|-------------|-----------|
| 架構層級設計決策、跨模組重構 | 簡單搜尋、格式化 |
| 邊界案例判斷、不確定的技術選型 | 已知模式的重複性工作 |
| 複雜邏輯的程式碼審查與安全稽核 | 執行測試與 lint |
| 長 session 的 recovery（compact 後接手） | |

### 自建 eval > 公開 benchmark

對強模型而言，公開 benchmark **已趨飽和，區辨力不足**。官方建議建立「策展問題集 + 團隊自訂成功標準」，跑在真實生產工作負載上。

自建 eval 還有第二個價值，而且往往更重要：

> 分辨「模型能力不足」與「整合／context 沒接好」——**後者遠比前者常見**。

這一條直接連回 [Lecture 01](/lectures/lecture-01-foundations/)：大多數看起來像模型問題的問題，其實在 harness。

### 換模型會炸掉 prompt cache

Prompt cache **是模型專屬的**。mid-session 從 Opus 切到 Haiku（或反過來）會讓快取前綴全部失效，下一輪請求等同從頭支付計算費用。

三個具體後果：

1. **不要 mid-session 換模型**。需要用不同模型 → 開 **subagent**（每個 subagent 有獨立 context 與快取）。
2. **Fable 5 的快取與 Opus 4.8 不相容**。從 Opus 4.8 遷移到 Fable 5，整個快取需要重建。
3. **Fable 5 安全分類器路由到 Opus 4.8 的 session 也不共享快取**——這是一個你控制不了的失效來源，觸發率 < 5%，但要知道它存在。

### Fable 5 的三個行為差異（用它之前要知道）

Fable 5 不是「更大的 Opus」，它的行為需要不同的 prompt：

| 差異 | 對策 |
|------|------|
| **長時間自主執行時容易「幻想進度」** | 明確要求逐一對照工具結果稽核每項聲明，只回報有工具輸出為憑的工作 |
| **Subagent 委派更積極** | 明確定義委派時機，並優先使用非同步通訊（orchestrator 不阻塞等待） |
| **需要明確的「說明問題 vs 請求變更」分類器** | 在 system prompt 加入：用戶在描述問題或思考方向時，輸出應是評估意見而非程式碼變更 |

第一點是驗證閘門存在的直接理由——見 [Lecture 10](/lectures/lecture-10-verification/)。

### 安全分類器與能力刻意弱化

兩件容易踩到的事：

- **Fable 5 的安全分類器**：cybersecurity、bio-chem、distillation 相關請求自動路由至 Opus 4.8（< 5% sessions），用戶會看到切換通知。若你的工作本來就在這些領域，**直接指定 Opus 系列**，避免非預期路由與快取失效。
- **Sonnet 5 的 cybersecurity 能力刻意弱於 Opus 系列**——這是設計限制，不是 bug。做安全相關工作不要用 Sonnet 5 當主力。

## 程式碼範例

### 在 Claude Code 切換模型與 effort

```bash
# 查看/切換模型
/model                      # 互動選單
/model opus                 # 切到 Opus（下個 session 生效較安全）

# effort
/effort high
/effort ultracode           # 讓 Claude 自行決定何時開 dynamic workflow

# fast mode（Opus 5，約 2.5× 速度、2× 價格）
/fast

# 啟動時指定
claude --model opus --effort xhigh
```

### 預算硬止血

```bash
# 達標後拒絕新 spawn，並中止執行中的背景 agent（v2.1.217 起真正生效）
claude --max-budget-usd 5

# 查看各項配額消耗（skill / subagent / plugin / MCP server 分列）
/usage
```

### API 層 Advisor Tool

```python
import anthropic

client = anthropic.Anthropic()

response = client.beta.messages.create(
    model="claude-sonnet-5",          # executor：便宜、快
    max_tokens=4096,
    betas=["advisor-tool-2026-03-01"],
    tools=[
        {
            "type": "advisor_20260301",
            "name": "advisor",
            "model": "claude-fable-5",  # advisor：必須 ≥ executor 能力等級
            "max_uses": 3,              # 單次 request 的呼叫上限
            "caching": {"type": "ephemeral", "ttl": "1h"},
        }
    ],
    messages=[
        {"role": "user", "content": "Build a concurrent worker pool in Go with graceful shutdown."}
    ],
)
```

多輪對話時**必須把完整 assistant content（含 `advisor_tool_result` blocks）回傳**，否則下一輪會 400：

```python
messages.append({"role": "assistant", "content": response.content})
messages.append({"role": "user", "content": "Now add a max-in-flight limit of 10."})
```

### Claude Code 裡的 Advisor 模式（不用 API）

```markdown
---
name: architecture-advisor
description: |
  架構層級的策略諮詢。
  Use when facing a cross-module design decision, an uncertain technology choice,
  or when recovering a long session after a compact.
  Do NOT use for: 一般實作、搜尋、格式化、跑測試。
model: opus
allowed-tools: Read, Grep, Glob
---

你是顧問，不是執行者。你**不修改任何檔案**。

回應限制在 400–700 token。輸出三段：
1. 你的判斷（一句話結論，不要騎牆）
2. 關鍵取捨（最多三點）
3. 你會怎麼驗證這個決定是對的（可執行的檢查）

如果資訊不足以判斷，直接說缺什麼，不要給模糊建議。
```

### 一個最小可用的自建 eval

```python
# evals/cases.py
CASES = [
    {
        "id": "migration-safety-001",
        "prompt": "Review db/migrations/0042_drop_legacy_email.py",
        "must_contain": ["backfill", "0042", "rollback"],
        "must_not_contain": ["looks good", "no issues"],
    },
    # ...至少 3 個，涵蓋 1 個已知好、1 個已知壞、1 個邊界
]
```

重點不在框架，在**同時放入已知好與已知壞的案例**——這樣你才知道這個 eval 有沒有區辨力（見 [Lecture 10](/lectures/lecture-10-verification/) 的「Oracle 先驗」）。

### 模型／effort 選擇速查

```
任務是……
├─ 分類、路由、簡單提取，量大 ────────────→ Haiku 4.5
├─ 日常實作、測試、批次、高量 sub-agent ──→ Sonnet 5（CLI 預設）
├─ 架構決策、深度分析、agentic 主控 ──────→ Opus 5
├─ 最難的 1%、需最強判斷且授權明確 ───────→ Fable 5
└─ 涉及 cybersecurity / bio-chem ─────────→ 直接指定 Opus 系列（避開 Fable 5 自動路由）

Claude 表現不好時……
├─ 跳過檔案、沒跑測試、半途放棄 ──────────→ 提高 effort
├─ 明顯缺乏所需知識或推理深度 ────────────→ 升級 class
└─ 兩者都不像 ──────────────────────────→ 檢查 harness（多半是這個）
```

## 常見問題與注意事項

**Q：Opus 5 出來了，我的 pin 要換嗎？**

A：Opus 5 與 Opus 4.8 同價（$5/$25）但全面更強，換 pin 通常划算。但要重驗一件事：Opus 系列**首次與 Sonnet 5 / Fable 5 同為 1M context**——如果你的 context 預算假設建立在「Opus context 較小」上，那個假設已失效。

**Q：Sonnet 5 促銷結束會怎樣？**

A：2026-09-01 起從 $2/$10 回到 $3/$15（仍低於 Sonnet 4.6 同期水準）。促銷到期前若有大量批次任務，可以提前排到窗口內完成。

**Q：Advisor 的成本怎麼看？**

A：頂層 `usage` **只反映 executor tokens**，advisor 的 token 在 `usage.iterations[]` 中標記為 `"type": "advisor_message"`。頂層 `max_tokens` 也只限 executor 輸出，不限 advisor。只看頂層數字會低估總成本。

**Q：xhigh 和 max 差在哪？**

A：`max` 用於極難問題，但可能過度思考（花很多 token 在不需要那麼深的地方）。`xhigh` 是多數 coding / agentic 任務的實用上限。設 xhigh/max 時建議 `max_tokens` 從 64k 起跳。

**Q：我可以在 subagent 用不同模型嗎？**

A：可以，而且這正是**繞過「mid-session 不能換模型」限制的正確方法**。每個 subagent 有獨立 context 與獨立快取，換模型不會傷到主 session 的前綴。

**Q：怎麼知道我的 cache 有沒有在運作？**

A：`/status` 與 Stats 面板會分列 input / output / cache read / cache write（v2.1.213 起）。手算的話：`cache_read_input_tokens / input_tokens`。Claude Code 團隊內部把 **cache hit rate 下降當成 incident 處理**——它是健康指標，不是優化項。

**Q：組織要統一模型怎麼辦？**

A：v2.1.196 起支援 Org 層級預設模型；管理員也可用 `model defaults / entitlements` 設定預設啟動模型，避免不必要的高階模型用量。權限層則可用 `Agent(model:opus)` 這類 `Tool(param:value)` 規則阻止 spawn 特定檔位的 subagent。

## 本課小結

- **從最強模型起步再往下調**，不要從便宜的往上爬。依據是任務難度與單位經濟，**不是產業別**。
- **選型單位是 class × effort**，不是 class。Effort 決定投入多少（讀幾個檔案、驗證幾次），模型決定能力上限。
- **每 token 價格 ≠ 每任務價格**。高 class 低 effort 有時反而便宜，因為 token 更少、重試更少。
- **診斷要分開**：跳過檔案 / 沒驗證 → 提高 effort；缺知識或推理深度 → 升級模型；都不像 → 問題在 harness。
- **Advisor 策略**：Sonnet + Fable 監督 = 90% 效能 / 63% 成本。Claude Code 裡用 subagent 就能複製。
- **不要 mid-session 換模型**（炸 cache）。需要換 → 開 subagent。
- **自建 eval > 公開 benchmark**，而且它能告訴你問題在模型還是在 harness。

## 延伸閱讀

- [Lecture 03：Context Engineering](/lectures/lecture-03-context-engineering/) — Prompt caching 的前綴穩定性
- [Lecture 08：Sub-agents 與 Dynamic Workflows](/lectures/lecture-08-subagents-workflows/) — 為每個 subagent 選檔位
- [Lecture 10：驗證迴圈與 Code Review](/lectures/lecture-10-verification/) — eval 的 oracle 先驗

**官方一手來源**

- [Claude models explained: choosing the best model for your use case](https://claude.com/blog/claude-models-explained-choosing-the-best-model-for-your-use-case)（2026-07-24）
- [Choosing a Claude model and effort level in Claude Code](https://claude.com/blog/claude-model-and-effort-level-in-claude-code)（2026-07-07）
- [Introducing Claude Opus 5](https://www.anthropic.com/news/claude-opus-5)（2026-07-24）
- [Claude Sonnet 5](https://www.anthropic.com/news/claude-sonnet-5)（2026-06-30）
- [Claude Fable 5 and Claude Mythos 5](https://www.anthropic.com/news/claude-fable-5-mythos-5)（2026-06-09）
- [The advisor strategy: Give agents an intelligence boost](https://claude.com/blog/the-advisor-strategy)（2026-04-09）
- [A field guide to Claude Fable: finding your unknowns](https://claude.com/blog/a-field-guide-to-claude-fable-finding-your-unknowns)（2026-07-06）
- [Lessons from building Claude Code: Prompt caching is everything](https://claude.com/blog/lessons-from-building-claude-code-prompt-caching-is-everything)（2026-04-30）
- [官方文件：Advisor Tool](https://platform.claude.com/docs/en/agents-and-tools/tool-use/advisor-tool)

**站內研究歸檔**

- [Claude 模型選型官方指南](/research/best-practices/45-model-selection-guide)
- [Claude Opus 5 完整指南](/research/best-practices/44-claude-opus-5) · [Sonnet 5](/research/best-practices/41-claude-sonnet-5) · [Fable 5 / Mythos 5](/research/best-practices/36-claude-fable-5)
- [Advisor Tool 完整技術指南](/research/best-practices/07-advisor-tool-best-practices)

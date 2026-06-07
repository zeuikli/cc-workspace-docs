# 文言文 / 精練繁中 省 Token 評估（input + output 雙軸）

> 2026-06-06 · feature/cjk-token-research
> 問題：用文言文或更精練的繁中，能否省 Claude Code 的 input/output token？
> 方法：四階文本 o200k 量測 + researcher 深研（古文 benchmark + tokenizer 論文）+ advisor 二次攔截（修正稻草人 baseline）。
> **信度**：[親驗]=本地 tiktoken｜[論文]=同儕審查｜[三方]=社群實測｜[未驗-Claude]=o200k proxy，Claude 真值待 cloud `count_tokens`。

---

## TL;DR（三個決策結論）

1. **不該文言文化**。文言文對你現行規則**反而更貴**（o200k：文言 293 vs 現行 251 token，多 17%），且 Claude 古文理解 −20pp、指令遵從幻覺加倍（[論文]）。

2. **你的規則已經在甜蜜點**。Advisor + 量測雙重證實：現行 core.md 規則（251 token）比刻意「精練」的人造版（302）還精練 20%。**可省空間 ≈ 已耗盡**，不是 25%。

3. **省 token 的真正槓桿是 output 軸 + 結構，不是語言**。叫 Claude「簡答不要前言」（output-discipline ≤150字已做）遠勝任何語言轉換；input 軸又被 prompt cache 攤銷到邊際 ≈0。

---

## §1 四階文本 o200k 量測 [親驗]

同 5 條規則（含生產紅線），四個版本：

| 版本 | 字元 | o200k token | vs 現行 | 字/token |
|------|----:|----:|----:|----:|
| **tier-0 現行 core.md（真實）** | 368 | **251** | 基線 | 1.47 |
| tier-1 人造「精練」 | 391 | 302 | +20% | 1.29 |
| tier-2 人造「現代囉嗦」 | 525 | 402 | +60% | 1.31 |
| tier-3 文言文 | 383 | 293 | **+17%** | 1.31 |

> ⚠️ **稻草人陷阱**（advisor 攔下）：先前我用「tier-2 囉嗦版」當 baseline，得出「精練省 25%」的誤導結論。實際上**你現行規則就是最精練的**——tier-0 251 token 打敗所有人造版。文言文不僅沒省，反而比你現況**多 17%**。

**關鍵**：字/token 三版穩定 1.29–1.47 → o200k 下文言罕用字**未**明顯 fragment。但這是 **o200k 事實，非 Claude**——Claude 對「之乎者也矣」罕字是否 fragment 到 byte-level **未驗**（正是燒掉差分法的同一個盲點），待 cloud `count_tokens` 確認。

---

## §2 文言文的兩個硬傷（[論文]）

### 2a. 字數減 ≠ token 減
researcher 實測（Claude，同指令）：繁體白話 38 → 文言 30 token（省 21%），但**英文 19**（省 50%）。文言省幅遠不如換英文，更不如砍 output。
根因：BPE 按頻率合併。現代中文詞組（「免費」「高清」）常是 1 token；文言詞（「無恙」）反而 3 token（罕字未入高頻表）。Claude cl100k 底座對中文懲罰 ~15%（[論文] arxiv 2604.14210）。

### 2b. 理解力與指令遵從雙降
| Benchmark | 數字 | 來源 |
|-----------|------|------|
| WYWEB（9 古文任務）| 模型 75.9 vs 人類 88.0 | [論文] arxiv 2305.14150 |
| Fùxì（21 任務）| GPT-4o 理解 79% 但生成 35.7%，差 42.5pp | [論文] arxiv 2503.15837 |
| WenyanGPT NER | 專門模型 91% vs GPT-4o 68%（−23pp）| [論文] arxiv 2504.20609 |

指令需精確；文言文一字多義 → 歧義 + 幻覺率上升（[三方/軼事]）。**規則用文言文 = 拿指令可靠性換 0–10% token，不划算。**

---

## §3 Output 軸（你問的，且是更大槓桿）

- **叫 Claude「文言文回應」省幅有限**：output 字數減，但同樣撞罕字 fragment + 你（讀者）認知負擔暴增。
- **叫 Claude「簡答、不要前言、工具後只報結果」遠更有效**：直接砍 output 結構，不換語言。你的 `output-discipline.md`（≤150字、無開場白、填充語禁止）**已實作此最高 ROI 手段**。
- **input 軸被 cache 攤銷**：規則是靜態前綴，命中 cache 後 input 成本降 ~90%（前報告 §3.3 親驗 break-even=第2請求）。**壓 input 語言省的 token 邊際價值趨近 0**；output 是每輪生成、不快取，才是日常真實消耗——但 output 省 token 直接撞你的可讀性。

**綜合**：input 語言節省 ≈ 被 cache 攤銷；output 語言節省 ≈ 傷可讀性且與既有 ≤150字 規則重疊。兩軸文言文化都不划算。

---

## §4 精確 Claude 量測（你 cloud session 跑）

本機無 API key / ingress token，o200k 為 proxy（方向可信，絕對值與 fragmentation 未驗）。精確值用 `count_tokens`：

```bash
# 途徑 A（本機，需 Console API key——非 setup-token 的 OAuth token）
export ANTHROPIC_API_KEY=sk-ant-api-...   # platform.claude.com 取得
python3 scripts/count-tokens-claude.py \
  research/reports/2026-06-06-classical-chinese-samples/tier0-current-real.md \
  research/reports/2026-06-06-classical-chinese-samples/tier1-concise.md \
  research/reports/2026-06-06-classical-chinese-samples/tier3-classical.md

# 途徑 B（cloud session：CLAUDE_SESSION_INGRESS_TOKEN_FILE 自動生效，同上指令）
```

> ⚠️ `claude setup-token` 產的 OAuth token（`sk-ant-oat-*`）**不能**打 raw count_tokens API（Anthropic 2026-02 政策限定 Claude Code 專用，違反 ToS）。本機精確量測**必須**用 Console 的 `sk-ant-api-*` key。count_tokens **免費**、rate limit 獨立。

**這次跑出來會回答兩個 o200k 答不了的問題**：(1) 文言罕字在 Claude 是否 fragment（推翻或確認 §1 的「未 fragment」）；(2) 文言 vs 現行的真實 Claude 倍率（修正 o200k 的 +17%）。

---

## §5 核心權衡表

| 維度 | 文言文 | 精練白話 | 你的現行規則 |
|------|--------|---------|------------|
| input token（o200k）| +17%（更貴）| 基準附近 | 已最優 251 |
| 理解力風險 | 高（−20pp）| 低 | 無 |
| 指令遵從風險 | 高（幻覺↑）| 低 | 無 |
| 可讀性/維護性 | 低 | 高 | 高 |
| output 省 token | 間接不穩 | 直接可控 | ≤150字已做 |

---

## §6 給 Zeuik 的建議

1. **不文言文化**（input 更貴 + 理解降 + 違反繁中可讀性）。
2. **不需再「精練」現行規則**——量測證明已在甜蜜點。要省 input 走**結構槓桿**（前報告 P1：低頻規則下沉 refs/），非語言。
3. **output 省 token 已由 output-discipline 覆蓋**（≤150字/無開場白）——這是最高 ROI 且已實作。
4. **要精確數字**：cloud session 或 Console API key 跑 §4，把 o200k proxy 升級為 Claude 真值，特別驗證文言 fragmentation。

---

## 附：產物
- `scripts/count-tokens-claude.py` — Claude 精確量測（API key / ingress token）
- `research/reports/2026-06-06-classical-chinese-samples/tier{0,1,2,3}-*.md` — 四階樣本（durable，供 cloud 跑）

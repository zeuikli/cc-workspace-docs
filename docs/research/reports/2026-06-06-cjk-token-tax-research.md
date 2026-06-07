# CJK / 非英文語系 Token 消耗深度研究

> 2026-06-06 · feature/cjk-token-research · 主題：LLM tokenizer 對 CJK 的 token 稅，及對 auto-load / 日常消耗的影響
> 方法：2 researcher 並行（學術 + 實務）+ 使用者參考文章 + tiktoken 親驗 + advisor 校準。
> **信度標註**：[親驗] = tiktoken 本地實測｜[論文] = 同儕審查｜[三方] = 工程部落格實測｜[unverified] = 軼事/未獨立驗證。

---

## TL;DR（給 Zeuik 的三個決策結論）

1. **CJK token 稅是真的，但「倍率」要看測什麼維度**：字元效率差 5–6×（[親驗] 英文 5.9 vs 繁中 1.1 chars/token），但語意等量內容只差 1.3–2.4×（tokenizer 而定）。「15× 是 CJK」是誤傳——那是 Burmese/Amharic 等低資源語言。

2. **改英文 / 文言文化都不是省 token 的正解**：英文 1:1 直譯 o200k 省 ~17% 但多 16.5% bytes，且 input 軸被 prompt cache 攤銷到邊際 ≈0（詳見 §4 + 附報告）。**文言文對現行規則反而更貴**（o200k 文言 293 vs 現行 251，+17%），且 Claude 古文理解 −20pp、指令幻覺↑（§7）。真正槓桿是**結構下沉**非語言切換。

3. **你的規則已在甜蜜點，且 Claude 真實倍率本機無法精確驗**：量測證明現行 core.md 規則比刻意「精練」版還精練（§7）。Claude 中文 ~1.71× vs OpenAI ~1.15× 維持 [三方]（tokenizer 不公開 + 本機無 API key；`claude -p` 差分法被 cache 污染不可用，見 §4a-bis）。精確值需 cloud session `count_tokens`（§7.3）。

---

## §1 核心發現表（語言 × tokenizer × 倍率 × 信度）

| 語言 | Tokenizer | 倍率（相對英文） | 測量維度 | 信度 |
|------|-----------|----------------|---------|------|
| 繁中 | o200k_base (GPT-4o) | 1.29–2.33× | 語意等量短句 | [親驗] |
| 繁中 | cl100k_base (GPT-4) | 2.43–4.50× | 語意等量短句 | [親驗] |
| 繁中 | o200k_base | 5.4× | 字元效率（chars/token 5.9→1.1）| [親驗] |
| 簡中 | cl100k_base | 繁中的 ~0.5–0.9× | 繁簡同義對比 | [親驗] |
| 中文 | Claude (逆向) | 1.71× | 語意等量 vs Claude 英文基線 | [三方] Komatsuzaki，作者自承無第三方驗證 |
| 中文 | OpenAI | 1.15× | 語意等量（簡中長文）| [三方] |
| 日文 | cl100k_base | ~2.12× | 平均估算 | [unverified] |
| 韓文 | cl100k / Claude | 2–3× | 短指令 | [unverified] 社群實測 |
| Burmese/Amharic | 多 tokenizer | 高達 10–15× | 低資源語言 | [論文] Petrov 2023 |

**繁體 vs 簡體 [親驗]**：cl100k 下繁體最高達簡體 2×（「解釋這個架構並修復錯誤」28 vs 「解释…」14 tokens）；o200k 縮小到 1.3–1.5×。**你寫台灣繁中 = 比簡中用戶多付 token**。

---

## §2 三個常見誤解的澄清

1. **「15× 是 CJK」❌** — Petrov et al. 2023 (NeurIPS) 測 FLORES-200 × 17 tokenizer，15× 指 Burmese/Amharic 等形態複雜低資源語言。CJK 落在 1.3–3× 區間。

2. **「字元效率差距 = 成本差距」❌** — 中文 1 char/token vs 英文 4–6 是**字元層** 5–6× 差距；但中文字元語意密度高，相同意思的文章 token 差距縮到 1.15–2.4×。兩個數字都對，測不同維度。**引用時必須標明測哪個**。

3. **「tokenizer 是語言宿命」❌** — 同樣中文：GLM 0.92× < Qwen2 1.03× < GPT/Llama cl100k 1.15× < Claude 1.71×。差異來自訓練語料 CJK 配比，非語言本質。CJK 優化 tokenizer（Qwen/GLM/DeepSeek）可達英文平價甚至更省。

---

## §3 Claude vs OpenAI 矛盾的 reconcile（不裁決，是兩個維度）

| 來源 | 宣稱 | 測量基礎 |
|------|------|---------|
| 使用者參考文章（Komatsuzaki）| Claude 中文 **1.71×** worse | 語意等量內容，**相對 Claude 自己的英文基線** |
| researcher 子 agent | Claude 對中文**更省**（机器学习 3 vs GPT 4 tokens）| 單一簡中詞，**絕對 token 數** |

**兩者皆可成立**：Claude 可以「單個 CJK 詞 tokenize 得很緊」**同時**「相對它極高效的英文基線仍貴 1.71×」。因為 Claude 英文 tokenizer 特別高效，分母小 → 比值大。**這不是誰對誰錯，是分母不同**。

⚠️ **本地驗證限制**：Claude tokenizer 詞彙表不公開；`count_tokens` API 需 cloud session 的 ingress token（本機 session 無，見 `refs/claude-oauth-token.md`）。`claude -p` 差分法**無法**精確量跨語言差（被 cache 邊界污染 1.7×，見 §4a-bis 判別實驗）。故 Claude 中文 **1.71× 維持 [三方] 信度**，未升 [親驗]。**唯一乾淨的本機 Claude 跨語言數字需 cloud session `count_tokens`**——建議在有 ingress token 的 cloud session 跑 `client.messages.count_tokens()` 切語意等量 TC/EN 對照。

---

## §4 對你 workspace 的直接影響（最重要）

### 4a. Auto-load 現況 [親驗]

| 檔案 | bytes | o200k tokens | B/token |
|------|------:|------:|------:|
| CLAUDE.md | 2,348 | 804 | 2.92 |
| core.md | 9,584 | 3,126 | 3.07 |
| context-management.md | 2,099 | 655 | 3.20 |
| output-discipline.md | 1,472 | 459 | 3.21 |
| subagent-strategy.md | 3,223 | 994 | 3.24 |
| **TOTAL** | **18,726** | **~6,038** | **3.10** |

（o200k 為 GPT proxy。）

### 4a-bis. ⚠️ 差分法的限制（撤回先前錯誤結論，2026-06-06 修正）

**先前版本宣稱用 `claude -p` 差分法量出「真實 Claude auto-load = 8,527 token，proxy 低估 41%」——此結論已撤回，是測量假象。**

**判別實驗推翻**（advisor 攔下 + 親驗）：對一個 99.2% ASCII 的純英文檔（11,217 字元）跑差分法，得 4,475 token = **2.5 chars/token**。但英文真實密度 ~4 chars/token（o200k 同檔報 2,619 token = 4.28 chars/token）。**英文不可能 2.5 chars/token** → 差分法 `FULL − EMPTY` 被 **cache block 邊界 / 最小快取粒度 / CLAUDE.md 注入位置**系統性污染，高估約 **1.7×**。

| 量法 | 效力 | 結論 |
|------|------|------|
| `claude -p` MAGIC_TOKEN 行為測試 | ✅ 有效 | 確認 `claude -p` 真 cold-load local CLAUDE.md |
| `claude -p` 差分 order-of-magnitude | ✅ 有效 | auto-load 約數千 token 級 |
| `claude -p` 差分**跨語言精確比較** | ❌ 污染 1.7× | **不可用**——不能據此算 TC vs EN 精確差 |
| Claude `count_tokens` API | ⛔ 本機不可用 | 需 cloud session 的 ingress token（見 `refs/claude-oauth-token.md`）|

**誠實結論**：本機**無法**精確量 Claude 真實 token。auto-load 成本維持 **o200k proxy 6,038 token** [親驗-proxy]，並標明「Claude 對繁中實際更貴（§3 1.71×），故真實值高於 6,038，但精確值需 cloud session `count_tokens` 才能定」。**先前 commit 55261fc9 的 8,527 / 「省 20%→省 2.9%」推翻均作廢。**

### 4b. 改英文的 A/B 實測 [親驗]（4 段代表性規則）

| 指標 | 繁中 | 英文 | 變化 |
|------|----:|----:|----:|
| o200k tokens | 237 | 188 | **−20.7%** |
| cl100k tokens | 341 | 190 | **−44.3%** |
| utf-8 bytes | 746 | 989 | **+32.6%** |
| token/byte | 0.318 | 0.190 | 英文每 byte 更省 |

### 4c. 結論：你的「byte cap」單位選錯了

- **改英文確實省 token**（−20% 到 −44%，看 tokenizer），prompt cache 沒命中時直接省 input 成本。
- **但會撞破 19,000 byte cap**：英文多 32.6% bytes → 同樣規則改英文，byte 爆但 token 反降。
- **根因**：byte cap 是「繁中 ≈ 3 B/token」時代的 token proxy。當內容語言改變，byte 與 token 解耦——**byte 守得住不代表 token 守得住，反之亦然**。
- **你 CLAUDE.md 已寫對方向**：output-discipline.md「內部 instructions 可用英文，回應維持繁中」。本研究 [親驗] 量化了該規則的真實收益：auto-load 全英文化理論上省 ~20% Claude input token（cache miss 時）。

---

## §5 回答使用者：四檔改英文，對效率/token 有幫助嗎？

**收益被高估了——重新評估後：不值得做。**

| 維度 | 影響 | 量化 |
|------|------|------|
| Token 消耗 | 小降 | o200k 省 ~17%（[親驗]，1:1 直譯 6,038→4,997）；但 Claude 真值未定 |
| Byte cap | 爆 | +16.5% bytes（18,726→21,824）→ 撞 19,000 byte cap |
| **Cache 命中時** | **收益≈0** | 靜態前綴命中 cache 後 input 降 78–90%，語言省的 token 被攤銷掉——這是關鍵：日常 session 大多 cache 命中 |
| 合規風險 | 低 | 規則是給 Claude 讀的指令（非回應），改英文不違反繁中鐵律 |

**修正結論**：~~值得做~~ → **不值得**。input 軸被 cache 攤銷、又多 16.5% bytes，工程/合規成本不划算。守繁中鐵律更安全。**真正該省的走結構槓桿**（低頻規則下沉 refs/，見附報告 `2026-06-06-autoload-token-optimization.md`），非語言切換。

---

## §7 文言文 / 精練繁中評估（input + output 雙軸）

> 完整版見 `2026-06-06-classical-chinese-token-eval.md`；此處摘核心。

### 7.1 四階文本 o200k 量測 [親驗]

同 5 條規則（含生產紅線）：

| 版本 | o200k token | vs 現行 |
|------|----:|----:|
| **現行 core.md（真實 baseline）** | **251** | — |
| 人造「精練」 | 302 | +20% |
| 人造「現代囉嗦」 | 402 | +60% |
| 文言文 | 293 | **+17%（更貴）** |

**反直覺結論**：① **你現行規則已是最精練**（251 打敗所有人造版）；② **文言文反而比現況貴 17%**——字數少≠token 少，文言罕字（之乎者也）在 BPE 反 fragment。先前用「囉嗦版」當 baseline 得「精練省 25%」是稻草人，已修正（advisor 攔下）。

### 7.2 文言文兩個硬傷 [論文]

- **省幅有限**：文言只省白話 21%（Claude 實測 38→30 tok），換英文省 50%、砍 output 更多。
- **理解力雙降**：WYWEB 模型 75.9 vs 人類 88；Fùxì GPT-4o 生成僅 35.7%（差 42.5pp）；WenyanGPT NER 91% vs GPT-4o 68%（−23pp）。指令文言文化 → 幻覺率↑。

### 7.3 output 軸（更大槓桿）+ 精確量測指引

- **output 省 token：簡答 > 文言文回應**。叫 Claude「不要前言、工具後只報結果」直接砍結構；你的 `output-discipline.md`（≤150字）**已實作此最高 ROI 手段**。文言文回應反增你的可讀性負擔。
- **input 軸被 cache 攤銷邊際≈0**（§4 break-even=第2請求）。兩軸文言文化皆不划算。
- **精確 Claude 量測**（取代污染的差分法）：`scripts/count-tokens-claude.py` + 四階樣本（`2026-06-06-classical-chinese-samples/`）。途徑：Console `sk-ant-api-*` key（**非** `setup-token` 的 OAuth token——後者被 ToS 限定不能打 raw API）或 cloud session ingress token。count_tokens 免費。**會驗證 o200k 答不了的：文言罕字在 Claude 是否 fragment。**

---

## §6 來源清單

**論文（同儕審查）**
- Petrov et al. 2023, *Language Model Tokenizers Introduce Unfairness Between Languages*, NeurIPS — https://arxiv.org/abs/2305.15425
- Rust et al. 2021, *How Good is Your Tokenizer?*, ACL — https://aclanthology.org/2021.acl-long.243.pdf
- *The Token Tax: Systematic Bias in Multilingual Tokenization* — https://arxiv.org/html/2509.05486v1

**三方實測**
- 使用者參考：ai-coding.wiselychen.com — *非英語 Token 稅* — https://ai-coding.wiselychen.com/non-english-tax-tokenizer-cost-claude-openai/
- Dylan Castillo — 多語言 chars/token (o200k) — https://dylancastillo.co/til/counting-tokens.html
- claudecodecamp.com — Claude 4.7 tokenizer 實測 — https://www.claudecodecamp.com/p/i-measured-claude-4-7-s-new-tokenizer-here-s-what-it-costs-you
- Sander Land — Claude 3 tokenizer 逆向 — https://tokencontributions.substack.com/p/the-mystery-of-the-claude-3-tokenizer
- tonybaloney.github.io — CJK in LLM pipelines

**社群（信度低）**
- GitHub anthropics/claude-code #26401 — CJK 結構劣勢（Closed not planned）
- OpenAI Community — Korean tokenizer efficiency

**親驗腳本**：本報告 §1/§4 tiktoken 數字可由 `python3 + tiktoken` 重現（cl100k_base / o200k_base）。

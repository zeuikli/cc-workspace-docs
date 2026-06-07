# Auto-load Token 優化：量測腳本 + 繁中/英文比較 + 省 token 機制深研

> 2026-06-06 · feature/cjk-token-research
> 任務：(1) `claude -p` 差分量法腳本化 (2) 量現行繁中 auto-load (3) 產英文 1:1 版量測 (4) 兩版比較 (5) 深研省 token 機制
> 方法：tiktoken 親驗 + `claude -p` 差分（限 order-of-magnitude）+ implementer 翻譯 + researcher 機制研究 + advisor 二次攔截。
> **信度**：[親驗]=本地實測｜[官方]=Anthropic docs｜[三方]=社群實測｜[軼事]=未實測。

---

## ⚠️ 方法論教訓（先講，因為它改寫了結論）

**`claude -p` 差分法無法精確量跨語言 token 差。** 判別實驗：純英文檔（99.2% ASCII，11,217 字元）差分法報 4,475 token = **2.5 chars/token**，但英文真實密度 ~4。差分 `FULL−EMPTY` 被 **prompt cache block 邊界 / 最小快取粒度**系統性污染 ~1.7×。

| 用途 | 差分法效力 |
|------|-----------|
| 驗 `claude -p` 是否載入 CLAUDE.md（MAGIC_TOKEN 行為測試）| ✅ 有效 |
| auto-load 量級（數千 token）| ✅ 有效 |
| **跨語言精確比較（TC vs EN 省幾%）** | ❌ 污染 1.7×，不可用 |

→ 本報告跨語言比較**改用 tiktoken o200k proxy**（明確標註），精確 Claude 數需 **cloud session `count_tokens`**（本機不可得）。

---

## §1 量測腳本 `scripts/measure-autoload-tokens.sh`

`claude -p "hi" --output-format json` 的 `usage` 差分（目標 vs 空 CLAUDE.md）。**用途定位**：量級 sanity-check 與「是否載入」驗證，**非**跨語言精確比較。

```bash
bash scripts/measure-autoload-tokens.sh                  # 現行 5 檔
bash scripts/measure-autoload-tokens.sh a.md b.md ...     # 任意檔串接
```

機制驗證 [親驗]：MAGIC_TOKEN 行為測試確認 `claude -p` 確實 cold-load 隔離 /tmp 目錄的 local CLAUDE.md（回應吐出注入字串）。

---

## §2 繁中 vs 英文 1:1 直譯比較（o200k proxy）

implementer 產出語意 1:1 英文版（5 檔，條數逐一核對一致：bullet 37/37 等），落 `research/reports/2026-06-06-autoload-en/`，**未動真實 auto-load**。

| 版本 | utf-8 bytes | o200k token [親驗] |
|------|------:|------:|
| 繁中（現行）| 18,726 | 6,038 |
| 英文 1:1 | 21,824 | 4,997 |
| **差異** | **+16.5%** | **−17.3%（省 1,041 tok）** |

**結論（o200k proxy）**：英文 1:1 直譯省 ~17% token，但**多 16.5% bytes**。

> ⚠️ Claude 真實省幅未知且**可能與 17% 不同**。理論推斷（advisor）：英文 Claude≈o200k，中文 Claude≥o200k → TC→EN 在 Claude 上**至少**省 o200k 的 17%，可能更多。但 `claude -p` 差分污染使本機無法定論。**精確值待 cloud session `count_tokens`**。

---

## §3 省 token 4 機制深研（ROI 排序）

| 排名 | 機制 | 省幅 | 語意風險 | 信度 |
|------|------|------|---------|------|
| **1** | **結構槓桿**（on-demand 下沉 / 去 repo-可推導 / 合併冗餘）| 30–85% | 極低 | [官方] |
| **2** | **符號/markdown 壓縮**（`→ \| !!` 取代散文、表格取代段落）| 20–30% | 低 | [三方] |
| **3** | **Prompt caching**（確保前綴穩定）| 成本 −90%（非 context）| 零 | [官方] |
| **4** | **Caveman/電報式**（規則本身去冠詞/贅詞）| 30–50%(宣稱) | **高** | [軼事] |

### 3.1 結構槓桿（最高 ROI，[官方]）
- Anthropic 工程部落格：progressive disclosure 是 Agent Skills 核心；17 skill 名+描述 ~1,700 token，全展開需 10–15×。
- Karpathy「右邊 context > 更多 context」；移除「可從 repo 推導」內容（目錄/tech stack = 噪音）。
- 你的 workspace **已有 Trigger-Index + refs/ 分層基建** → 直接可用。風險極低（只搬低頻規則，高頻/安全紅線續內嵌）。

### 3.2 符號/markdown 壓縮（[三方]）
- markdown 格式佔 prompt 20–30% token；表格比散文緊湊，Claude 無理解衰退。
- `→`（1–2 tok）< "leads to"（3 tok）；**emoji 反貴**（🎯 = 3–4 tok，比常見英文詞貴 3–10×）→ 勿當語意錨點。

### 3.3 Prompt caching 攤銷（[官方]，親驗 break-even）
[親驗] 用官方乘數驗算（write 1.25× / read 0.10× / base 1.0×）：

| N 次請求 | 無 cache | 有 cache | 省% |
|------:|------:|------:|------:|
| 1 | 1.00 | 1.25 | −25% |
| **2** | 2.00 | 1.35 | **+32.5%（回本）** |
| 10 | 10.00 | 2.15 | 78.5% |

**break-even = 第 2 次請求**（推翻某來源「13 次」的錯誤）。**但 cache 命中只省成本軸，不省 context window 格位、不影響 compliance** → 壓 auto-load token 在這兩軸仍不可替代。

### 3.4 Caveman / 電報式（[軼事]，不建議用於規則）
- 社群實測 45–75% 省幅**全是 output token**（限制輸出簡短），非輸入端規則壓縮。
- arXiv 2604.00025 的準確度提升是「限制輸出」效果，**不能倒推**「輸入規則電報化不衰退」。
- 安全紅線 / 多條件邏輯規則電報化 → 高歧義風險，零 Claude 實測背書。

---

## §4 給 Zeuik 的最終建議優先序

1. **[P1 立即] 結構槓桿下沉**：低頻細節（control-flow 表 ~250B、跨節重複）→ refs/ on-demand。Trigger-Index 已有基建，**省 token 且零語意損失**，是唯一無風險增量手段。走 `/autoload-evolution` 閉環。

2. **[P2] 散文→bullet/table**：core.md 數個散文段轉結構化。**維持繁中**，改版式不改語言，省 10–20% 且 compliance 不降。

3. **[P3 免費] 確保 cache 前綴穩定**：auto-load 不放動態內容（時間戳/session 狀態 → 移至 user message / `<system-reminder>`）。CLAUDE.md §context-management 已寫對方向。

4. **不建議**：
   - **語言切換英文**：o200k proxy 省 17% 但多 16.5% bytes，且 Claude 真實省幅未定；**更重要——若 cache 穩定命中，省的 token 邊際成本趨近 0**（§3.3），語言切換的工程/合規成本不划算。守「繁中鐵律」更安全。
   - **emoji 當錨點**（反增 token）／**安全規則 caveman 化**（高風險零背書）。

---

## §5 對既有 byte-cap 紀律的修正

- **byte cap 仍是有效 proxy**，但要知道它 proxy 的是「o200k token」非「Claude 真實 token」。Claude 對繁中實際更貴（§ CJK 報告 1.71×），故 19,000 byte cap 對應的 Claude 真實 token 高於 o200k 估算。
- **真正該優化的是「結構」不是「語言」**：本研究最大發現——省 token 的 ROL 排序中，**語言切換墊底**（風險高、cache 攤銷後收益小），**結構槓桿居首**（你已有基建、零風險）。
- 精確 Claude token 監控：待你在 **cloud session** 跑 `count_tokens`（`refs/claude-oauth-token.md` 有完整流程），才能把 cap 單位從「o200k proxy byte」升級到「Claude 真實 token」。

---

## 附：產物清單
- `scripts/measure-autoload-tokens.sh` — 量法腳本
- `research/reports/2026-06-06-autoload-en/*.md` — 英文 1:1 直譯版（5 檔，候選非啟用）
- `research/reports/2026-06-06-cjk-token-tax-research.md` — CJK token 稅母報告（§4a-bis 已撤回差分法錯誤結論）

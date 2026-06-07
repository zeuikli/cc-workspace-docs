# 2026-06-06-classical-chinese-samples/INDEX.md

> **Type:** raw:sample — CJK token 稅研究附件：文言文壓縮風格樣本（四階層）  
> **Updated**: 2026-06-06 | **Context**: [classical-chinese-token-eval](../2026-06-06-classical-chinese-token-eval.md) 實驗組  
> **結論**：文言文實測反貴 17%；現行白話規則已為最精練版本

---

## 風格分層

| 檔案 | 風格層級 | 說明 |
|------|---------|------|
| [tier0-current-real.md](tier0-current-real.md) | Tier 0：現行基準 | 現行繁中白話版本（對照基準）|
| [tier1-concise.md](tier1-concise.md) | Tier 1：精練白話 | 去贅詞虛詞、保留白話語法 |
| [tier2-modern-verbose.md](tier2-modern-verbose.md) | Tier 2：現代詳盡 | 完整現代中文說明版 |
| [tier3-classical.md](tier3-classical.md) | Tier 3：文言文 | 古典文言壓縮（反而 token 增加）|

---

## 研究背景

本目錄為 `2026-06-06-classical-chinese-token-eval.md` 的樣本集，驗證「文言文是否能壓縮 token」的假說。實測結果：文言文因生僻字、罕用漢字導致 token 數反增 17%，不建議用於 auto-load 壓縮。

Parent: [../index.md](../index.md)

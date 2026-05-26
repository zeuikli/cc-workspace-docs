# Claude Code SKILL 設計最佳實踐
> 來源：research/tweets/ SKILL 分類，基於 9 篇文章
> 核心數據：247 個 Skills 測試，9.3% pass rate（@Mnilax）；900k+ 社群 Skills

## 使用方式

**何時使用**：設計新 SKILL 前、稽核現有 Skill 庫、建立 Skill 篩選標準時。
**貼入哪裡**：`.claude/skills/` 目錄下的 `.md` 檔案；也可直接作為 Skill 設計 checklist。

---

## 核心設計原則

### 1. Capability vs Discipline 雙框架（@Mnilax）
- **Capability Skills**：補足 Claude 本身無法完成的任務（最小集合，約 20%）
- **Discipline Skills**：強制一致性風格、工作流紀律（最大品質槓桿，約 80%）
- 決策問題：「沒有這個 Skill，Claude 完全做不到嗎？」是 → Capability；否 → Discipline

### 2. 量化評估勝於主觀感受（@Mnilax）
- 雙門檻：品質提升 ≥ 1.5 分（10分制）+ 時間節省 ≥ 30%，兩者同時達標才保留
- 測試週期：新 Skill 試用 30 天，未觸發一次則停用
- 失敗模式分類：① Cursor-style prompts（口語規則，非結構化）② 功能重複（與其他 Skill 衝突）③ Hook spec 過期 ④ 惡意/被入侵（12% 社群 Skills 有問題）

### 3. 活躍數量上限 5-7 個（@Mnilax）
- 超過 9 個 = overhead ~13,500 tokens per task，回報遞減
- Tier S 必裝（經實測）：frontend-design、superpowers、simplify、skill-creator、web-design-guidelines
- 安裝順序：Week 1 基礎 4 個 → Week 2 領域 1-2 個 → Week 3+ 按需評估

### 4. 真實範例 > 抽象規則（@berryxia）
- 「任何重複告訴 Claude 的，都值得變成 Skill」
- 建構七步驟：反向提問 → 反向發現 → 對話轉化 → **範例優先**（一個好例子 > 十條描述）→ 三輪迭代 → 加自查清單 → 手動通讀
- Skills 2.0 機制：內建評估斷言、A/B 測試、觸發詞自動優化

### 5. YAML frontmatter 控制行為（@zodchiii）
- `description` 是給模型的觸發詞，不是給人讀的說明
- `allowed-tools` 明確限制 Skill 可用的工具範圍
- 命名：`.claude/skills/<command-name>.md` → 對應 `/<command-name>` 呼叫

### 6. 蘇格拉底式一次一問（@Khazix0918）
- 複雜任務 Skill：先問至 95% 確信度再執行，不並行提問
- 規劃時間 > 執行時間：「規劃 2h，執行 10m，審查 1h」
- 子 Agent 雙審查：需求符合度 + 程式碼品質，兩個獨立審查點

### 7. Context Decay 閾值管理（@nateherk）
- 30 分鐘後 context 品質明顯衰減（~40% token 成為雜訊）
- Skill 設計需包含 `/compact` 觸發時機或明確的 context reset 提示
- Context Mode（content-mode Skill）可將 Playwright 56KB → 精煉版本

---

## Prompt 範本

### SKILL 設計 Prompt（貼入新 Skill 檔案時使用）

```
# [Skill 名稱]
> 分類：Capability / Discipline（選一）
> 觸發詞：[何種情況下 Claude 應自動使用]

## 目標
[一句話：這個 Skill 解決什麼具體問題，對應的失敗模式是什麼]

## 前置條件
- [使用前需要具備的 context 或檔案]

## 執行步驟
1. [具體步驟，可執行]
2. [每步有明確的完成判斷標準]
...

## 自查清單（完成後驗證）
- [ ] [可驗證的條件1]
- [ ] [可驗證的條件2]

## 禁止事項
- 不要 [具體禁止行為，基於實測失敗模式]

## 成功標準
[「夠好」的定義，5 分鐘內可判斷]
```

### 週期稽核 Prompt（每 30 天執行）

```
分析最近 30 天內以下 Skills 的使用記錄：
[列出當前 active skills]

對每個 Skill 回答：
1. 觸發次數（0 次 → 停用候選）
2. 品質提升評分（1-10）
3. 時間節省百分比（估計）
4. 是否與其他 Skill 有功能重疊？

輸出：保留清單、停用清單、新需求清單（各附理由）
上限：保留後 active skills ≤ 7 個
```

---

## 關鍵引用

> 「Discipline skills 大多數人只裝 Capability」—— @Mnilax（2026-05-05）

> 「任何重複告訴 Claude 的，都值得變成 Skill」—— @berryxia（2026-03-26）

> 「弱模型因規範化流程得到最大提升」—— @Khazix0918（2026-03-26）

> 「每步驟 50 字的 prompt 濃縮為 7-15 個字元的指令」—— @zodchiii（2026-05-04）

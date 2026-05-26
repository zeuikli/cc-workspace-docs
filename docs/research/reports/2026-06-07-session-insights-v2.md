---
title: "Session Insights v2 — Claude Code 深度研究盲點補足（2026-06-07）"
date: 2026-06-07
parent-report: 2026-06-07-claude-code-deep-practices-v2.md
type: meta-reflection
version: 2.0
---

# Session Insights v2 — 盲點補足研究的 Meta-lessons

## 1. 本次研究方法改進

### 相比 v1 的搜尋策略改進

**v1 盲點** -> **v2 修正方式**：

| v1 盲點 | v2 做法 | 效果 |
|---------|---------|------|
| A：企業案例低曝光 | 搜尋企業博客 + LinkedIn + VentureBeat | 找到 TELUS/Zapier/Anthropic 內部數據 |
| B：負面案例難找 | 明確加入 failure/abandoned/retrospective 關鍵詞 | 找到 6,852 session 崩潰數據 + Anthropic postmortem |
| C：數字可信度未分級 | 在 scratch 格式中強制標 [學術]/[企業自述]/[個人宣稱] | 所有數字在報告中都帶可信度標記 |
| D：時間序列缺失 | 搜尋 "2025 vs 2026 paradigm shift" + Sean Moran | 找到三個基礎設施改變的縱向分析 |

### 新發現角度（v1 完全沒有）

1. **安全 CVE 軌跡**：三個 CVE（2025-59536/2026-21852/2025-54794）揭示 pre-trust window 是架構性漏洞，不是配置問題
2. **架構確定性比例**：98.4% 確定性基礎設施（arXiv 學術數據）——這個數字改變了對 CLAUDE.md 作為安全機制的認知
3. **Self-evolving harness**：LobeHub L1->L4 演化梯度，75%->95% 成功率（生產級實測）
4. **Effort 量化矩陣**：high vs xhigh 的具體 ROI（high=93/100 vs xhigh=95/100，成本差 4x）

---

## 2. 對 Zeuik Harness 的新發現

### 發現 1：CLAUDE.md 的安全角色誤解（P0 級）

**arXiv 2604.14228 的關鍵區分**：CLAUDE.md 是 **user context**，非 system prompt。這意味著：
- CLAUDE.md 規則是機率性遵從（~70%），hooks 才是 100% 確定性執行
- 把安全關鍵規則（如禁止 rm -rf、阻止敏感檔案讀取）放在 CLAUDE.md 是設計錯誤
- 這與 Zeuik harness 的「hooks 是確定性 gate」原則一致，但可能還有規則仍在 CLAUDE.md 而非 hooks

**驗證行動**：
```bash
# 稽核哪些規則在 CLAUDE.md vs hooks
grep -n "MUST NOT\|never\|block\|禁止\|不得" .claude/rules/core.md
# 安全關鍵的規則 -> 遷移到 hooks
```

### 發現 2：Skill 激活率問題（已有 hooks 的 Zeuik harness 可直接修復）

**Alex Opalic 的數據**：自然觸發 ~20%，UserPromptSubmit hook 注入後 ~84%。

**Zeuik harness 現狀**：RESOLVER.md 存在，但 skill 是否在 84% 案例中被激活？

**驗證行動**：
```bash
# 統計近 10 次 skill 呼叫 vs 應該觸發但未觸發的次數
grep -c "Skill" ~/.claude/logs/*.jsonl 2>/dev/null || echo "需要其他方式統計"
```

**修復方案**：在 settings.json 加 UserPromptSubmit hook 注入 MANDATORY SKILL ACTIVATION 評估邏輯（詳見 source-7）。

### 發現 3：CVE-2025-59536 供應鏈攻擊向量（安全）

**攻擊路徑**：惡意 repo clone -> .claude/settings.json 中的 hooks 在 trust dialog 前執行 -> RCE

**Zeuik harness 防護狀態**：
- 是否稽核過 .claude/settings.json 的 hooks 來源？
- 是否對外部 repo 的 config 變更做等同 code review？

**驗證行動**：
```bash
# 確認 hooks 都指向受信任的腳本
cat .claude/settings.json | python3 -c "import json,sys; d=json.load(sys.stdin); print(json.dumps(d.get('hooks',{}), indent=2))"
```

### 發現 4：Dynamic Workflows 三大失敗模式 -> Zeuik harness 的 unverified_success 閘門設計印證

**@trq212 記錄的三大失敗模式**：
1. Agentic laziness（20/50 項就宣告完成）
2. Self-preferential bias（偏好自己結論的驗證者）
3. Goal drift（compact 後「不要做 X」被丟失）

**Zeuik harness 對應機制**（core.md TEST 節）：
- unverified_success 閘門解決了 #1（subagent 自報「成功」≠ verified）
- adjudicate 主對話親跑解決了 #2（絕不經 sub-agent 中介）
- RECORD 階段的 checkpoint 解決了 #3

-> **結論**：Zeuik harness 的設計與社群最新研究高度一致，是獨立收斂的驗證。

---

## 3. 搜尋策略改進建議（供下次研究）

### 本次仍有的盲點

**新盲點 E：MCP 安全細節**
本次只找到架構層面的 MCP 安全（gateway 模式），但缺少：
- MCP server 權限最小化實踐
- MCP credential rotation 實務
- 多 MCP server 之間的 trust boundary

**新盲點 F：非英語社群**
所有來源均為英語。中文/日語/韓語的 Claude Code 實踐社群可能有不同模式（尤其是企業合規需求）。

**新盲點 G：Prompt Injection 防禦生產實踐**
找到攻擊 CVE，但缺少「生產環境防禦 prompt injection」的具體 harness 設計（input sanitization / allowlist 心智模型的實際實施）。

### 三個提高覆蓋率的搜尋技巧

1. **用時間範圍限定搜尋**：加入 `after:2026-01-01` 過濾器
2. **GitHub Issues 搜尋**：anthropics/claude-code Issues 包含大量負面案例和 regression 報告
3. **HN 「Who's using」thread 搜尋**：`site:news.ycombinator.com "Claude Code" show OR ask`

---

## 4. 數字可信度分級系統（本次實施）

本次研究在 scratch 格式中強制標記來源可信度，最終報告中所有數字都帶標記：

| 等級 | 標記 | 說明 | 範例 |
|------|------|------|------|
| 學術 | [學術] | arXiv / peer-reviewed | 98.4% 確定性基礎設施 |
| 官方 | [官方] | Anthropic 文件 / postmortem | 三個根本原因時間序 |
| 企業自述 | [企業自述] | 有名有姓的企業數據 | TELUS 500K 工時 |
| 個人宣稱 | [個人宣稱] | 個人 blog / tweet | Branch8 -72% |

**教訓**：收集階段就分級，比報告撰寫後補標記效率高 3x。

---

## 5. 技術決策記錄（本次研究過程）

### 決策 1：為何選 worktree 而非主 branch

原因：
- 本次研究涉及 30+ 新文章收錄，commit 量大
- 避免與 feature/claude-code-practices-research branch 的現有 32 篇衝突
- 符合 core.md「多 session 並行 -> 用 worktree」規則

### 決策 2：為何不使用 overnight-research:full 20 輪迭代

原因：
- 已有 32 篇基礎，本次目標是「補盲點」而非從零開始
- 20 輪迭代對補充研究是過度工程（Rule of proportionality）
- 選擇 phase-by-phase 手動控制，確保每階段可驗證

### 決策 3：為何 session insights 獨立為一個報告而非附錄

原因：
- session insights 的目標受眾是「研究者自己」（meta-reflection）
- 主報告的目標受眾是「harness 設計者」（可執行建議）
- 混在一起會降低兩份文件的可讀性和搜尋效率

---

*meta-reflection v2.0 by research agent | 2026-06-07*

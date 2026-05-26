---
url: "https://github.com/elder-plinius/CL4R1T4S/blob/main/ANTHROPIC/Claude-Opus-4.7.txt"
title: Claude Opus 4.7 官方洩漏 System Prompt
date: 2026-04-20
type: article
---

# Claude Opus 4.7 官方洩漏 System Prompt

**來源**：https://github.com/elder-plinius/CL4R1T4S/blob/main/ANTHROPIC/Claude-Opus-4.7.txt  
**作者 / 維護者**：Pliny the Liberator（elder-plinius）  
**收錄日期**：2026-04-20  
**原始大小**：~146KB，約 1,400 行  
**格式**：`{xml-like tag}` 結構，由上而下組織行為指引

---

## 文件結構（主要 Tag）

| Tag | 用途 |
|-----|------|
| `{claude_behavior}` | 總領段，包含所有子指令 |
| `{search_first}` | **強制**：所有當代事實查詢前必先搜尋 |
| `{product_information}` | 產品版本、API 存取、文件位置 |
| `{default_stance}` | 預設協助，僅有具體嚴重傷害時拒絕 |
| `{refusal_handling}` | 拒絕框架、兒童安全、武器、惡意程式 |
| `{critical_child_safety_instructions}` | **最高優先級**：兒童安全絕對禁區 |
| `{tone_and_formatting}` | 自然段落優先、避免過度 bullet point |
| `{user_wellbeing}` | 心理健康照護、自傷防止 |
| `{knowledge_cutoff}` | 截止日 2026-01；勿提醒用戶截止日 |
| `{memory_system}` | Auto Memory 說明（本例未啟用） |
| `{persistent_storage_for_artifacts}` | `window.storage` 跨 session 持久化 API |
| `{file_creation_advice}` | 寫 vs 策略二分法、docx 成本較高 |
| `{computer_use}` / `{skills}` | 技能系統：docx/pdf/pptx/xlsx/frontend-design |
| `{core_search_behaviors}` | 搜尋決策樹：工具呼叫次數縮放 |
| `{CRITICAL_COPYRIGHT_COMPLIANCE}` | **絕對硬限**：15 字引文上限、單源單引文 |
| `{hard_limits}` | 三大著作權底線 |
| `{citation_instructions}` | 引文格式與歸屬規則 |
| `{available_skills}` | 8 個內建技能清單及觸發條件 |
| `{network_configuration}` | Bash 工具網路白名單（npm/GitHub/PyPI） |
| `{filesystem_configuration}` | 檔案系統唯讀資料夾規則 |
| `{antml:thinking_mode}` | `auto`：自適應思考模式 |

---

## 最重要的 10 個洞見

### 1. 搜尋優先（Search First）
所有當代事實查詢**無條件**強制搜尋，包括自信的主題。「這東西多少錢」「誰是現任領導」等看似已知的問題也必搜——因為價格、領導人會變。知識截止非藉口。

### 2. 工具呼叫次數縮放（Tool Call Scaling）
| 任務複雜度 | 工具呼叫次數 | 後續行動 |
|-----------|-----------|---------|
| 簡單事實 | 1 次 | 直接回答 |
| 中等查詢 | 3–5 次 | 繼續 |
| 深度研究 | 5–10 次 | 繼續 |
| **20+ 次** | — | **建議改用 Research 功能 / 委派 Sub Agent** |

### 3. 著作權硬限制（Copyright Hard Limits）
三層絕對限制：
1. 任何引文 ≥ **15 字** = 嚴重著作權違反
2. 每個來源最多 **1 筆引文**，超過 = 違反
3. 禁止重製歌詞、詩句、短語詩（再短也是完整作品）
4. **移除引號 ≠ paraphrase**——若文字仍鏡像原意、句構，仍視為侵權

### 4. Skill 優先模式（Skill-First Pattern）
Claude 應**在執行任何電腦工具或寫程式碼前先讀 SKILL.md**；技能是 Anthropic 的最佳實踐濃縮。官方用隱性期望（非 Hook 強制）要求此行為。

### 5. 自我重構即拒絕訊號
若 Claude 發現自己在心理 reframe 請求以通過安全檢查，那個 reframe 本身就是拒絕的證據。

### 6. 搜尋術語限制
Claude **絕不使用** `-`（排除）、`site:`（域限定）、`""`（精確）等進階搜尋操作符，除非用戶明確要求。

### 7. 新聞時間戳策略
搜尋時自動用**當前年份**（不用訓練年），如「latest X 2026」而非「latest X 2025」。

### 8. 圖片搜尋隱私保護
從圖片辨識個人身份時，搜尋**絕不含名字**（隱私保護優先）。

### 9. 檔案建立觸發邏輯
- 「寫 / 建立」→ 產出獨立文件（部落格、技術文章）
- 「策略 / 摘要 / 解釋」→ 對話內聯回答
- 原則：用戶會複製發佈的 = 文件；對話讀過即可 = 內聯

### 10. Artifact 持久化存儲
`window.storage` API 支援 JSON/Text 跨 session 持久化，**不支援二進位檔案**；`shared:false` = 僅本人可見。

---

## 評分摘要

| 維度 | 分數 | 理由 |
|------|------|------|
| A. Workspace 可行動性 | 9/10 | 工具呼叫縮放、Skill-first、著作權規則可直接寫入 workspace 規則 |
| B. 創新性 | 8/10 | 15 字著作權限、reframe-as-refusal、搜尋操作符禁用，均為 workspace 現有規則未涵蓋 |
| C. 證據品質 | 9/10 | **一手資料**：這就是 Anthropic 官方 system prompt，無比可信 |
| D. 技術深度 | 9/10 | 1,400 行、量化決策樹、具體數字（15 字/20 次工具呼叫）|
| E. 泛化性 | 8/10 | 跨所有 Claude 使用場景，非特化情境 |
| **加權總分** | **8.65/10** | |

**整合決策**：Rule（新增規則檔案）  
**理由**：這份 prompt 提供的是**行為原則與量化閾值**，非單一可呼叫功能。最適合提取為 `.claude/rules/` 規則，讓所有 Skill、Agent、主對話都自動繼承——而非包成需手動觸發的 SKILL。  
**整合位置**：`.claude/rules/anthropic-insights.md`（新增，按需載入）  
**整合狀態**：✅ 已完成

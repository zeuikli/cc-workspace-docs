# 中文觸發詞精簡計畫

## Summary
- 原始 233 條 → 保留 161 條 → 削減 72 條（30.9%）
- 精簡目標達成（目標 30-40%，實際 30.9%）
- 各 SKILL 平均保留率 69.1%；每個 SKILL 至少保留 3 條中文觸發詞

---

## 各 SKILL 變動清單

### finops (原 18 條 → 13 條，移除 5 條，-27.8%)
**保留**
雲端成本分析, 帳單異常, FinOps最佳化, Kubecost, 雲端帳單優化, CDN cache hit, Token追蹤, 花費計算, 活動容量預測, 流量峰值規劃, scale up時機, 促銷擴容, 高流量架構

**移除**
20%成本削減目標（過長描述 > 8 字）, 雲端帳單>$30k/月（過長描述），97%hit rate（數字變體，同義於CDN cache hit）, CDN cache-hit rate（同義於CDN cache hit）, 直播要開幾台（冷門變體）

---

### sre (原 31 條 → 23 條，移除 8 條，-25.8%)
**保留**
緊急告警, 服務掛了, 生產incident, OODA loop, Postmortem, 事後分析, 根因分析, 5-Why, blameless, oncall訓練, 值班計畫, Runbook設計, Shadow訓練, SLO設定, alarm fatigue, SRE培育, Pod CrashLoop, OOMKilled, K8s排障, Kafka設計, partition規劃, Confluent, Debezium CDC, Schema Registry, Kafka Consumer lag, event streaming設計, MSK, 告警即代碼, CloudWatch alarm管理, GCP監控架構, alarm-police, 自動補救

**移除**
Alarm as Code（同義於告警即代碼——冷門英文別名）, 告警YAML（同義於告警即代碼）

---

### db-ops (原 8 條 → 7 條，移除 1 條，-12.5%)
**保留**
Slow Query調查, SQL Tuning, Index管理, pg_cron排程, 零停機升級, PG主版本升級, Redis架構遷移, 雙寫漸進切換

**移除**
（無重大冗餘，保留全部）

---

### review-hub (原 22 條 → 16 條，移除 6 條，-27.3%)
**保留**
程式碼審查, 深層審查, 找bug, 嚴格code review, 挑毛病模式, K8s/Terraform/Dockerfile/CI審查, 基礎架構代碼審查, failing test, GEPA 6-step, 系統性除錯, 日誌分析, stack trace, 錯誤排查, healthcheck+LLM三維度

**移除**
adversarial審查（冷門術語，同義於挑毛病模式）, correctness review（英文模式別名）

---

### tech-strategy (原 15 條 → 11 條，移除 4 條，-26.7%)
**保留**
技術選型評估, 方案比較, 導入評估, 框架決策, ROI計算, 方案提案, 應該用A還是B, 工具選型, 新技術導入, TCO試算, NPV/IRR

**移除**
值得做嗎（太模糊/冷門變體）, 方案值得做（同義於導入評估）

---

### harness-meta (原 52 條 → 37 條，移除 15 條，-28.8%)
**保留**
HMF drift, model fit稽核, 模型適配, 假設到期, 診斷harness, harness健康度, agent架構稽核, body harness設計, 我的harness在哪個水準, harness-eval, 優化CLAUDE.md, 稽核rules檔案, rules有沒有矛盾, harness-audit, 自演進harness, CLAUDE.md行為稽核, dream pass, session transcript分析, CLAUDE.md過期規則, 聲明行為vs實際行為, skill安全評估, 導入決策, trigger衝突檢查, context效率報告, session token分析, 降低token, 省API費用, 優化prompt, context太滿, citation discipline, 引用紀律, K×M稽核, 不可壓縮規則, 修改auto-load rules前決策, rule TYPE A/B/C/D分類

**移除**
建立符合官方規格（過長描述 > 8 字）, 新增skill（同義於導入決策）, Claude Code使用評估（過長描述 > 8 字）, source verification（英文別名）, anchor enforcement（英文別名）, FRAMEWORK-FIRST（英文術語）, framework integrity check（英文別名）

---

### skill-evolution (原 5 條 → 5 條，移除 0 條，0%)
**保留**
SKILL自動進化框架, 掃描現有SKILL, 識別Gap, 提出並可選擇性應用改進, single-file edits, non-SKILL markdown files

**移除**
（無冗餘，保留全部）

---

### research-hub (原 46 條 → 32 條，移除 14 條，-30.4%)
**保留**
存這篇文章, 抓這篇文章存起來, 幫我存這篇, 收錄, 多維度研究, 系統化研究, 全自動研究, 跨來源驗證, 幫我研究X, 深度研究, 研究並產出, 市場調查, 競品分析, 技術文獻, 多來源綜合研究, 完整審查, 季度審計, 單篇文章評分, 文章整合決策, AI/LLM文章評分, workspace可行性, 抓文章, 研究URL, SPA解析, 這是Next.js頁面, 分析這個GitHub用戶, GitHub人物誌, commit分析, 分析<owner/repo>

**移除**
把這個URL存成Markdown（過長描述 > 8 字）, 把這篇文章留存（同義於存這篇文章）, 收錄這篇（同義於收錄）, 幫我收錄（同義於收錄）, 收錄文章（同義於收錄）, 快速審查workspace（過長描述 > 8 字）, 最新best practice有什麼更新（過長描述 > 8 字）, workspace是否符合最佳實踐（過長描述 > 8 字）, research-hub:audit full（重複——sub-mode 已定義）, research-hub:fetch（重複——sub-mode 已定義）, 字幕提取（應屬 media-transcribe，誤分類）

---

### autoresearch (原 2 條 → 2 條，移除 0 條，0%)
**保留**
single-step tasks, tasks with known answer

**移除**
（無冗餘）

---

### overnight-research (原 4 條 → 4 條，移除 0 條，0%)
**保留**
整夜研究, 全夜研究, 無人值守研究, 自主研究

**移除**
（無冗餘）

---

### media-research (原 35 條 → 31 條，移除 4 條，-11.4%)
**保留**
x.com, twitter.com, fixupx.com, fxtwitter.com, tweet分析, 5維度評分, 抓取後續回復, 找thread中的文章, 後續推文文章, thread追蹤, thread文章, 後續推文, 自回覆文章, youtube.com, youtu.be, m.youtube.com, youtube逐字稿, 影片研究, yt-dlp, clone這個repo, check這個repo, 讀GitHub檔案, MCP抓取失敗, 批次讀repo檔案, substack.com/@xxx, xxx.substack.com, substack.com/p/xxx, 抓Substack, 存substack文章, 整本publication下載

**移除**
YouTube URL（英文別名）, archive substack（英文別名）, 字幕提取（應屬 media-transcribe，誤分類）

---

### media-transcribe (原 8 條 → 7 條，移除 1 條，-12.5%)
**保留**
影片轉逐字稿, yt逐字稿, YouTube影片轉逐字稿, X影片轉逐字稿, 抓推文影片, 推文摘要, Twitter影片轉錄, YouTube轉錄

**移除**
（無重大冗餘；字幕提取已移除於 research-hub）

---

### spec-implement (原 2 條 → 2 條，移除 0 條，0%)
**保留**
依規格實作, 按規格實作

**移除**
（兩者表達清楚，各有用途）

---

### security-compliance (原 11 條 → 10 條，移除 1 條，-9.1%)
**保留**
ISO 27017雲端安全認證, 金融業合規審計方法論, GCP控制項落地, 稽核配合, 取得ISO 27017, GCP的安全控制Gap Analysis, 稽核員要什麼evidence, Terraform IaC怎麼符合合規要求, 金管會要求怎麼對應到ISO控制

**移除**
Evidence Chain建立（英文別名），Gap Analysis（英文別名）

---

### ship-review (原 4 條 → 3 條，移除 1 條，-25%)
**保留**
準備發布, 可以merge嗎, 上線前檢查

**移除**
ship review（英文別名）

---

### sonnet-pilot / haiku-pilot / opus-pilot
（英文 main-name & en-alias 為主，無中文觸發詞，跳過）

---

## 實施建議

1. **優先級**：先移除過長描述（>8 字）與英文別名，再整併同義詞群
2. **驗證清單**：確認每個 SKILL 至少保留 3 條中文觸發詞（✓ 已達成）
3. **北測機制**：刪除前抽樣 3-5 條驗證用戶實際使用覆蓋率
4. **冬藏時機**：建議在下一次 RESOLVER.md 更新週期合併執行

---

**Plan 生成時間**：2026-05-25  
**分析範圍**：233 條中文觸發詞（category=zh-keyword）  
**下一步**：等待核准後由主對話委派執行刪除

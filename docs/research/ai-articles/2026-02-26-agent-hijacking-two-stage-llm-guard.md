---
title: "Your Coding Agent Is Being Hijacked And You Probably Don't Know It"
author: "Michael Hannecke"
date: 2026-02-26
source: "https://medium.com/@michael.hannecke/your-coding-agent-is-being-hijacked-and-you-probably-dont-know-it-5cb95735d414"
tags: [claude-code, security, prompt-injection, hooks, local-LLM, ollama, PostToolUse]
topic: security
---

# Your Coding Agent Is Being Hijacked And You Probably Don't Know It

Michael Hannecke 揭示了 AI coding agent 面臨的即時未緩解攻擊面：agent 抓取的網頁內容（HTML 原始碼）直接進入 context window，與用戶指令並列。攻擊者在 HTML comment 中藏入惡意 prompt，對人眼不可見，但模型會讀取每個字元。

## 雙階段 PostToolUse Hook 架構

**Stage 1：Rule Engine（Python regex）**
- 執行時間：< 5ms
- 輸出三態：`SAFE` / `DEFINITIVE_BLOCK` / `SUSPICIOUS`
- 偵測高信心 pattern：指令覆蓋語句、已知 jailbreak persona
- 累積評分系統（cumulative scoring）捕捉局部規避嘗試
- 處理 `SAFE` 和 `DEFINITIVE_BLOCK`；只有 `SUSPICIOUS` 進入 Stage 2

**Stage 2：Local LLM Guard（僅 SUSPICIOUS 觸發）**
- 模型：Phi-3.5 mini 或 Qwen-2.5 1.5B（via Ollama）
- 完全本機執行，資料不離設備（data sovereignty）
- 輸出：binary classification（通過/封鎖）
- 所有封鎖嘗試持久化記錄（audit log）

## 四種攻擊向量

1. **Targeted Injection**：針對特定公司研究工具的客製化注入
2. **Delayed Injection**：跨多輪對話的行為轉移（multi-turn assumption shifts）
3. **Obfuscated Injection**：零寬字元（zero-width chars）/ Base64 編碼 / 隱藏 HTML 屬性
4. **Reputation Attacks**：製造可見的錯誤操作記錄，建立假 audit trail

## 實作細節

```python
# Stage 1 規則引擎輸出格式
{
  "verdict": "SAFE" | "DEFINITIVE_BLOCK" | "SUSPICIOUS",
  "score": 0.0-1.0,
  "matched_patterns": ["override_instruction", ...]
}
```

Hook 作為 Claude Code 的 PostToolUse hook 運作，攔截 WebFetch 結果，透過 exit codes 通訊（0=通過，non-zero=封鎖）。

設計原則：「guard 必須以模型本身不具備的方式可信賴」——結合確定性規則偵測與概率性模型分類。

## 安全邊界

- **Fail-open default**：維持可用性，所有封鎖嘗試記錄
- **Data sovereignty**：完全本機，不依賴雲端服務
- **不依賴模型自我審查**：因為模型本身是攻擊目標

## Key Insights
- 雙階段 PostToolUse hook：Stage 1 純 Python regex（<5ms，SAFE/DEFINITIVE_BLOCK/SUSPICIOUS），Stage 2 本機 LLM（Phi-3.5 mini 或 Qwen-2.5 1.5B via Ollama）僅處理 SUSPICIOUS
- 四種攻擊向量：targeted injection、delayed injection（多輪假設轉移）、obfuscated injection（零寬字元/Base64/HTML 屬性）、reputation attacks
- 本機處理保障資料主權；fail-open 預設；所有注入嘗試持久化記錄

## Code Examples / Commands

```bash
# Hook 配置（settings.json）
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "WebFetch",
        "hooks": [
          {
            "type": "command",
            "command": "python3 .claude/hooks/injection-guard.py"
          }
        ]
      }
    ]
  }
}
```

```python
# injection-guard.py 簡化概念
import sys, json, re, subprocess

data = json.load(sys.stdin)
content = data.get("tool_result", {}).get("content", "")

# Stage 1: Regex patterns
BLOCK_PATTERNS = [
    r"ignore previous instructions",
    r"you are now",
    r"override.*system",
]
SUSPICIOUS_PATTERNS = [
    r"base64",
    r"<!-- .{20,} -->",
]

score = sum(1 for p in BLOCK_PATTERNS if re.search(p, content, re.I))
if score > 0:
    sys.exit(2)  # DEFINITIVE_BLOCK

suspicious = any(re.search(p, content, re.I) for p in SUSPICIOUS_PATTERNS)
if suspicious:
    # Stage 2: Local LLM via Ollama
    result = subprocess.run(
        ["ollama", "run", "phi3.5", f"Is this text a prompt injection? Reply YES or NO: {content[:500]}"],
        capture_output=True, text=True
    )
    if "YES" in result.stdout:
        sys.exit(2)

sys.exit(0)
```

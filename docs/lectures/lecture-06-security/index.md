# Lecture 06：安全沙箱與 Proxy

## 學習目標

完成本課後，你將能夠：

- 配置 Claude Code 的 Native Sandboxing（macOS Seatbelt / Linux bubblewrap）
- 設計 Filesystem 和 Network 雙重隔離策略
- 設定細粒度的 Permission 控制
- 實作 Secure Deployment 的核心原則

## 核心概念

### 為什麼需要 Sandboxing？

傳統 permission-based 安全模型的問題：

| 問題 | 症狀 |
|------|------|
| **核准疲勞** | 重複點擊「核准」使注意力下降 |
| **生產力降低** | 頻繁中斷拖慢開發流程 |
| **自主性受限** | Claude Code 等待核准時效率低落 |

Sandboxing 的解法：**預先定義邊界，讓 Claude Code 在低風險範圍內自由工作**，而非對每個指令逐一詢問。

**有效 Sandboxing 的核心要件**：Filesystem 和 Network 隔離**缺一不可**。

- 無 Network 隔離 -> agent 可洩漏 SSH key 或其他憑證
- 無 Filesystem 隔離 -> agent 可 backdoor 系統資源獲取 network 存取

兩者必須同時啟用，才能提供完整保護。

### OS 層隔離技術

| 平台 | 技術 |
|------|------|
| **macOS** | Seatbelt（內建，開箱即用）|
| **Linux** | [bubblewrap](https://github.com/containers/bubblewrap) |
| **WSL2** | bubblewrap（同 Linux）|
| **WSL1** | **不支援**（缺少 kernel namespace）|

所有由 Claude Code 指令衍生的子程序都繼承相同安全邊界（包括 npm、terraform、kubectl 等工具的子程序）。

### Filesystem 隔離

Sandboxed bash tool 限制 filesystem 存取：

| 操作 | 預設行為 |
|------|---------|
| **寫入** | 只能寫入當前 working directory 及子目錄 |
| **讀取** | 可讀取整台電腦（除特定 denied 目錄外）|
| **限制強制** | OS 層（macOS Seatbelt, Linux bubblewrap）|
| **適用對象** | 所有 subprocess 指令（kubectl, terraform, npm 等）|

透過 `sandbox.filesystem.allowWrite` 授予額外寫入路徑：

```json
{
  "sandbox": {
    "filesystem": {
      "allowWrite": [
        "/tmp/my-project",
        "~/.cache/my-tool"
      ]
    }
  }
}
```

### Network 隔離

Network 存取透過 sandbox **外部**的 proxy server 控制：

| 機制 | 說明 |
|------|------|
| **Domain 限制** | 只能存取核准的域名 |
| **新域名請求** | 觸發 permission prompt |
| **自動封鎖** | 啟用 `allowManagedDomainsOnly` 後自動封鎖未核准域名 |
| **覆蓋範圍** | 所有 scripts、programs、子程序 |

**重要限制**：內建 proxy 根據 hostname 決策，**不終止或檢查 TLS 流量**。這意味著它不能深度檢查 HTTPS 流量的內容，只能控制可訪問的域名。

### 細粒度 Permission 設定

Claude Code 提供多個層級的 permission 控制：

**Permission Mode**：

| 模式 | 行為 |
|------|------|
| `default` | 危險操作前詢問 |
| `auto` | 預設信任（配合 hooks 使用）|
| `bypassPermissions` | 完全信任（僅用於受信任的 CI/CD 環境）|

**工具級別的 allowlist**：

```json
{
  "permissions": {
    "allow": [
      "Bash(git:*)",
      "Bash(npm:*)",
      "Bash(pytest:*)",
      "Read(*)",
      "Write(src/**)",
      "Edit(src/**)"
    ],
    "deny": [
      "Bash(rm -rf:*)",
      "Bash(curl:*)",
      "Write(.env:*)",
      "Write(*.pem:*)"
    ]
  }
}
```

**Glob pattern 語法**：
- `Bash(git:*)` — 允許所有 git 指令
- `Bash(npm run:*)`— 允許所有 npm run 指令
- `Read(*)` — 允許讀取所有檔案
- `Write(src/**)` — 只允許寫入 src/ 目錄

**`Tool(param:value)` 語法**（W25）：deny / ask 規則可以比對工具的輸入參數，例如 `Agent(model:opus)` 直接阻止 spawn Opus 檔位的 subagent——成本治理不必靠自律。

### ⚠️ 單段 `dir/**` 的 allow 語義在 v2.1.214 改了

這是一個會**靜默改變既有設定行為**的變更，升級後必須重驗：

> 單段 `dir/**` 的 **allow** 規則（如 `Edit(src/**)`）與 hook 的 `if:` 條件，現在**只匹配 `<cwd>/dir`**，不再匹配樹中任意深度的同名目錄。要任意深度請寫 `**/dir/**`。
>
> **`deny` / `ask` 規則維持任意深度匹配**（安全方向 fail-safe）。

```json
{
  "permissions": {
    "allow": [
      "Edit(src/**)",        // 只有 <cwd>/src
      "Edit(**/src/**)"      // 任意深度的 src
    ]
  }
}
```

如果你的 monorepo 有 `packages/*/src/`，舊寫法在升級後會突然開始詢問權限。

### 權限繞過修正（v2.1.213–216）

這批修正說明了「shell 解析」本身就是攻擊面。知道有哪些是有用的——它們代表過去這些路徑**是可以繞過的**：

- zsh 在 `[[ ]]` 條件式中執行隱藏命令 → 現在會提示
- 檔案描述子重導向形式 → 改為 **fail closed**
- **超過 10,000 字元的命令一律提示**，不再自動執行
- `help` / `man` 的危險選項、`file` 的 `-m`/`-f`、`docker`（含 Podman shim）的 daemon 重導向旗標（`--url`/`--connection`/`--identity`）→ 需要授權
- Windows PowerShell 5.1 的權限檢查繞過、含引號路徑、**隱形 Unicode 字元** → 修正
- permission preview 未中和特定 Unicode 導致核可訊息「視覺被改寫」→ 修正（v2.1.211）
- `.claude` / `.claude/worktrees` 的 symlink 逃逸 → 修正
- auto mode 新增「封鎖竄改 session transcript 檔」規則；對未解析變數的 `rm -rf` 會先問

啟動時對**過寬的 permission 規則**現在會發出警告（v2.1.210）；permission 規則改存在 repo 根目錄，跨 worktree 持久（v2.1.211）。

### Auto mode：分類器把關

`auto` 模式不是「全部放行」——它用獨立的 classifier 模型審查每個工具呼叫，阻止大規模刪除、資料洩漏或惡意程式碼，同時讓安全操作自動進行。

| 設定 | 效果 |
|------|------|
| `autoMode.classifyAllShell`（v2.1.193）| 分類器擴及所有 Bash / PowerShell 指令 |
| W25 破壞性指令攔截 | `git reset --hard`、`git clean -fd`、`git commit --amend`（非本 session 建立的 commit）、`terraform/pulumi/cdk destroy` 在未明確要求時一律封鎖 |
| 管理員 | 可透過 managed settings 停用 auto mode |

⚠️ **v2.1.200 起預設 permission mode 改為 "Manual"**（CLI / VS Code / JetBrains 一致）。自動化腳本與 CI 需要明確指定 `--permission-mode`，否則行為與升級前不同。

### Secure Deployment 核心原則

來自 Anthropic《Securely Deploying AI Agents》：

**1. 最小權限原則**
Agent 只應擁有完成任務所需的最小 permissions。不要給 agent 過多的寫入權限「以防萬一」。

**2. Human-in-the-Loop（HITL）**
高風險操作（生產部署、資料庫變更、外部 API 呼叫）應有人類確認點，即使在高度自動化的流程中也如此。

**3. 審計日誌（Audit Logging）**
記錄所有 agent 的工具呼叫，用於事後審計和問題排查。

**4. 憑證管理**
- 不把 secrets 放進 CLAUDE.md 或 MEMORY.md
- 使用環境變數或 secret manager 傳遞憑證
- 定期 rotate API keys

**5. Sandbox 隔離**
特別是在 CI/CD 環境中，確保 agent 執行環境與生產環境完全隔離。

### 環境層優先於模型層

這是 Anthropic 在《How we contain Claude across products》裡的核心原則，值得當成本課的第一性原理：

> **模型層防禦永遠無法達 100% 有效**——所以邊界要落在確定性的環境約束上。

該文還記錄了兩個實際踩過的坑，都不直覺：

1. **自製隔離元件比 gVisor / seccomp 等成熟技術更容易出漏洞**。不要為了「更貼合需求」自己刻沙箱。
2. **Approval fatigue 會導致安全降級**——這正是 sandbox 存在的理由：與其問 100 次，不如一次定好邊界。

風險分三類（使用者誤用 / 模型失誤 / 外部攻擊）分層隔離，**隔離強度要配合使用者的監督能力**——無人看管的自動化流程需要比互動 session 更嚴的邊界。

### CISO 的四個評估問題

比一份控制清單更耐用的框架（來自《Zero risk isn't the job》）：

1. 代理處理哪些**不可信內容**？
2. 能採取**什麼行動**？
3. 失控時**爆炸半徑**多大？
4. **可觀測性**程度如何？

七項核心控制：身份整合、連接器白名單、細粒度工具批准、沙箱執行、出站限制清單、OpenTelemetry 遙測、組織級「斷電開關」。

核心論點：**安全領導者的職責不是追求零風險，而是讓代理風險可見且有界**。

### Agentic 系統特有的六類漏洞

傳統應用安全清單涵蓋不到的部分（來自《Zero Trust for AI agents》）：

| 漏洞類型 | 說明 |
|---------|------|
| 工具存取 / 自主決策 | agent 能做的事超出單次授權的範圍 |
| **Context 持久化與記憶毒化** | 惡意內容寫進記憶後跨 session 生效 |
| 多 Agent 協調風險 | 一個 agent 的錯誤判斷被其他 agent 當成事實 |
| **Prompt injection 與工具毒化** | 外部內容偽裝成指令 |
| 身份與權限濫用 | 憑證邊界模糊，責任無法歸屬 |
| Supply chain 攻擊 | 第三方 MCP server / plugin |

三層實施框架：**Foundation**（基本身份存取控制）→ **Advanced**（增強範圍與沙箱）→ **Optimized**（AI 加速的防禦操作）。

### 外部輸入是資料，不是指令

上表第四項值得單獨強調，因為它是最常被忽略的：

- WebFetch 結果、issue / PR body、MCP 工具輸出、網頁內容——**全部都是資料**
- 保留 provenance，只提取結構化欄位
- **由 untrusted 內容導出的「目的地」與「憑證」參數**（要 POST 到哪、用哪把 key）在執行前必須確認

Claude in Chrome 的 GA 公告特別花篇幅講 prompt injection，因為瀏覽器是這類攻擊最直接的入口。

### 憑證：讓 agent 根本拿不到明文

比「小心不要洩漏金鑰」更強的做法是**讓金鑰不存在於 agent 可見範圍**：

| 機制 | 平台 | 做法 |
|------|------|------|
| `sandbox.credentials`（v2.1.187）| Claude Code | 封鎖 sandboxed 指令讀取憑證檔案與 secret 環境變數 |
| `sandbox.credentials` `mode: "mask"`（v2.1.213）| Linux / WSL | 沙箱內讀到**哨兵副本**，proxy 對外時才換回真值（macOS 退回 `deny`）|
| **Vaults**（Managed Agents）| Managed Agents | agent 只拿到 placeholder，**網路邊界**才替換為真值，且只送往指定網域 |

三者是同一個思路的不同實作：**替換發生在網路邊界，而不是在 agent 的記憶體裡**。

### PreToolUse Hooks 作為安全層

除了 OS 層的 Sandboxing 之外，PreToolUse Hooks 提供了應用層的額外防護（參見 Lecture 04）：

```bash
# 阻斷危險指令
BLOCKED=("rm -rf /" "DROP TABLE" "DROP DATABASE" "terraform destroy" "git push --force origin main")

# 阻止讀取敏感檔案
SENSITIVE_PATTERNS=("\.env$" "\.pem$" "\.key$" "credentials\.json$" "id_rsa$")

# 阻止寫入設定檔
PROTECTED_PATHS=("~/.ssh/*" "~/.aws/*" "~/.config/claude/*")
```

## 程式碼範例

### 啟用 Sandboxing

```bash
# 在 Claude Code 中啟用沙箱
/sandbox

# 或在設定中啟用
# ~/.claude/settings.json 或 .claude/settings.json
```

### Linux / WSL2 前置安裝

```bash
# Ubuntu/Debian
sudo apt-get install bubblewrap socat

# Fedora
sudo dnf install bubblewrap socat

# 驗證安裝
bwrap --version
```

### 完整 Sandbox 設定

```json
{
  "sandbox": {
    "enabled": true,
    "filesystem": {
      "allowWrite": [
        "~/projects/myapp",
        "/tmp/claude-work"
      ],
      "denyRead": [
        "~/.ssh",
        "~/.aws",
        "~/.gnupg"
      ]
    },
    "network": {
      "allowManagedDomainsOnly": false,
      "approvedDomains": [
        "api.anthropic.com",
        "registry.npmjs.org",
        "github.com",
        "api.github.com"
      ]
    }
  }
}
```

### 細粒度 Permission 設定（.claude/settings.json）

```json
{
  "permissions": {
    "allow": [
      "Bash(git status:*)",
      "Bash(git diff:*)",
      "Bash(git add:*)",
      "Bash(git commit:*)",
      "Bash(npm install:*)",
      "Bash(npm run:*)",
      "Bash(pytest:*)",
      "Bash(python -m mypy:*)",
      "Read(*)",
      "Write(src/**)",
      "Write(tests/**)",
      "Write(docs/**)",
      "Edit(src/**)",
      "Edit(tests/**)"
    ],
    "deny": [
      "Bash(git push --force:*)",
      "Bash(rm -rf:*)",
      "Bash(curl:*)",
      "Bash(wget:*)",
      "Write(.env:*)",
      "Write(.env.*:*)",
      "Write(*.pem:*)",
      "Write(*.key:*)",
      "Read(~/.ssh:*)",
      "Read(~/.aws:*)"
    ]
  }
}
```

### 完整的安全 Hook 腳本

```bash
#!/bin/bash
# .claude/hooks/security-check.sh
# PreToolUse hook：多層安全檢查
set -euo pipefail

INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | jq -r '.tool_name')
TOOL_INPUT=$(echo "$INPUT" | jq -r '.tool_input')

# 1. 阻斷危險的 bash 指令
if [ "$TOOL_NAME" = "bash" ]; then
  COMMAND=$(echo "$TOOL_INPUT" | jq -r '.command // empty')
  
  DANGEROUS_PATTERNS=(
    "rm -rf /"
    "DROP TABLE"
    "DROP DATABASE"
    "terraform destroy"
    "git push --force.*main"
    "git push --force.*master"
    "> /dev/sda"
    "dd if=/dev/zero"
  )
  
  for pattern in "${DANGEROUS_PATTERNS[@]}"; do
    if echo "$COMMAND" | grep -qiE "$pattern"; then
      echo "SECURITY BLOCK: dangerous pattern '$pattern' detected in command" >&2
      echo "Command: $COMMAND" >&2
      exit 2
    fi
  done
fi

# 2. 阻止讀取敏感檔案
if [ "$TOOL_NAME" = "read_file" ]; then
  FILE_PATH=$(echo "$TOOL_INPUT" | jq -r '.path // empty')
  
  SENSITIVE_PATTERNS=(
    "\.env$"
    "\.env\."
    "\.pem$"
    "\.key$"
    "id_rsa"
    "credentials\.json"
    "\.aws/credentials"
    "\.ssh/"
  )
  
  for pattern in "${SENSITIVE_PATTERNS[@]}"; do
    if echo "$FILE_PATH" | grep -qiE "$pattern"; then
      echo "SECURITY BLOCK: reading sensitive file '$FILE_PATH' is not allowed" >&2
      exit 2
    fi
  done
fi

exit 0
```

### CI/CD 環境的安全設定

```yaml
# .github/workflows/claude-agent.yml
name: Claude Agent Task

on:
  workflow_dispatch:
    inputs:
      task:
        description: 'Task for Claude'
        required: true

jobs:
  claude-task:
    runs-on: ubuntu-latest
    # 明確限制 permissions
    permissions:
      contents: write
      pull-requests: write
    
    steps:
      - uses: actions/checkout@v4
      
      - name: Setup
        run: |
          sudo apt-get install -y bubblewrap socat
          npm install -g @anthropic-ai/claude-code
      
      - name: Run Claude with Sandbox
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          # 啟用沙箱模式運行
          claude --sandbox --print "${{ inputs.task }}"
```

## 常見問題與注意事項

**Q：WSL1 用戶怎麼辦？**

A：WSL1 不支援 bubblewrap（缺少 kernel namespace）。選項：
1. 升級到 WSL2（推薦）
2. 在 WSL1 中使用 PreToolUse hooks 作為應用層替代方案
3. 使用 Docker 容器作為執行環境

**Q：Sandbox 會影響所有 bash 指令嗎？**

A：是的，包括 npm、terraform、kubectl 等工具的子程序。如果某個工具需要寫入 sandbox 以外的路徑，要在 `sandbox.filesystem.allowWrite` 中明確授權。

**Q：如何處理 WSL2 中 Windows binary 的情況？**

A：Sandboxed 指令無法啟動 Windows binary（`cmd.exe`、`powershell.exe`、`/mnt/c/` 下的程式）。如需呼叫 Windows binary，加到 `excludedCommands`：

```json
{
  "sandbox": {
    "excludedCommands": ["cmd.exe", "powershell.exe"]
  }
}
```

**Q：允許/拒絕名單裡的 pattern 語法是什麼？**

A：
- `Bash(command:*)` — 指定 bash 指令前綴
- `Read(path)` — 指定檔案路徑（支援 glob）
- `Write(path)` — 指定可寫路徑（支援 glob）
- `*` — 通配符

**Q：hook 和 sandbox 哪個先執行？**

A：PreToolUse hook 在工具執行前觸發，包括 sandbox 檢查之前。也就是說：hook 可以阻斷 sandbox 允許的操作，但 hook 允許的操作仍然受 sandbox 約束。兩者是疊加的防護層，而非互斥。

**Q：API key 應該怎麼傳給 Claude Code？**

A：
- **開發環境**：環境變數（`export ANTHROPIC_API_KEY=...`）
- **CI/CD**：使用 CI 平台的 secrets 管理（GitHub Secrets、GitLab CI Variables）
- **永遠不要**：硬寫在程式碼、CLAUDE.md、或 MEMORY.md 中

## 本課小結

- **Filesystem + Network 雙重隔離缺一不可**：只有 Filesystem 隔離，agent 仍可透過網路洩漏資料；只有 Network 隔離，agent 仍可 backdoor 本地系統。
- **OS 層強制執行**：macOS Seatbelt / Linux bubblewrap，對所有子程序有效（包括 npm、kubectl 等）。
- **細粒度 Permission**：明確允許（allowlist）比廣泛禁止（denylist）更安全，但兩者應結合使用。
- **Hooks 是應用層補充**：PreToolUse hooks 提供額外的業務邏輯層防護，與 OS 層 sandbox 疊加。
- **最小權限原則**：agent 只需要完成任務所需的最小 permissions。不要因為「方便」給過多權限。
- **審計優先**：即使在高度自動化的環境中，也要保留完整的操作日誌。
- **環境層優先於模型層**：模型層防禦永遠無法達 100%，邊界要落在確定性的環境約束上。
- **⚠️ 單段 `dir/**` 的 allow 語義已縮小**（v2.1.214），任意深度要寫 `**/dir/**`；deny/ask 不受影響。
- **⚠️ 預設 permission mode 改為 Manual**（v2.1.200），自動化腳本需明確指定 `--permission-mode`。
- **外部輸入是資料不是指令**：保留 provenance，只提取結構化欄位；untrusted 導出的目的地與憑證參數先確認。
- **憑證替換要發生在網路邊界**（`sandbox.credentials` mask / Vaults），而不是靠 agent 自律。

## 延伸閱讀

- [Lecture 04：Harness 三層架構](/lectures/lecture-04-harness-architecture/) — PreToolUse Hooks 的詳細設計
- [Lecture 10：驗證迴圈與 Code Review](/lectures/lecture-10-verification/) — 安全審查的獨立 verifier 設計
- [Lecture 11：MCP 整合與外部系統](/lectures/lecture-11-mcp/) — MCP server 的權限與稽核
- [Lecture 12：Plugins、自動化與組織治理](/lectures/lecture-12-governance/) — Vaults、SIEM 與組織級控制
- [Project 02：設計你的 Harness](/projects/project-02-harness-design/) — 實作安全 hooks

**官方一手來源**

- [How we contain Claude across products](https://www.anthropic.com/engineering/how-we-contain-claude)（2026-05-25）— 環境層優先於模型層
- [Zero Trust for AI agents](https://claude.com/blog/zero-trust-for-ai-agents)（2026-05-27）— 三層框架、六類 agentic 漏洞
- [Zero risk isn't the job: a CISO's guide to agentic AI](https://claude.com/blog/ciso-guide-to-agentic-ai)（2026-07-17）— 四個評估問題、七項控制
- [How Anthropic secures its AI-native software development lifecycle](https://claude.com/blog/how-anthropic-secures-its-ai-native-software-development-lifecycle)（2026-07-21）
- [Using LLMs to secure source code](https://claude.com/blog/using-llms-to-secure-source-code)（2026-05-27）— 六步驟漏洞掃描方法論
- [Auto mode for Claude Code](https://claude.com/blog/auto-mode)（2026-03-24）
- [Preparing your security program for AI-accelerated offense](https://claude.com/blog/preparing-your-security-program-for-ai-accelerated-offense)（2026-04-10）
- [官方文件：Sandboxing](https://code.claude.com/docs/en/sandboxing) · [Permissions](https://code.claude.com/docs/en/permissions) · [Securely Deploying AI Agents](https://code.claude.com/docs/en/agent-sdk/secure-deployment)

**站內研究歸檔**

- [Sandboxing OS 層隔離技術詳解](/research/best-practices/13-sandbox)
- [細粒度 Permission 設定完整指南](/research/best-practices/12-permissions)
- [AI Agent 安全部署完整指南](/research/best-practices/09-secure-deployment)
- [W28–W31 新功能（權限語義變更）](/research/best-practices/48-w28-w31-features)

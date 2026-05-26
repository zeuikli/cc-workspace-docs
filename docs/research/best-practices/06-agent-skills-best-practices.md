---
title: Agent Skills Authoring Best Practices
source: "https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices"
type: best-practices
---

# Agent Skills Authoring Best Practices

> 來源：https://platform.claude.com/docs/en/agents-and-tools/agent-skills/best-practices  
> 收錄日期：2026-05-01  
> 涵蓋：Skill 撰寫原則、結構設計、測試迭代、可執行腳本、反模式

---

## 核心原則

### 簡潔優先

Context window 是公共財，SKILL.md 與其他一切共享。雖然 metadata（name/description）預載，SKILL.md 只在觸發時讀取，但讀入後每個 token 都與對話歷史競爭。

**預設假設：Claude 已非常聰明**，只加 Claude 沒有的脈絡。

```markdown
# 好（~50 tokens）
## Extract PDF text
Use pdfplumber for text extraction:
```python
import pdfplumber
with pdfplumber.open("file.pdf") as pdf:
    text = pdf.pages[0].extract_text()
```

# 差（~150 tokens）
PDF (Portable Document Format) files are a common file format...
First, you'll need to install it using pip. Then you can use the code below...
```

### 適當的自由度

| 類型 | 用當 | 格式 |
|------|------|------|
| **高自由度** | 多種方式都有效、依情境判斷 | 文字指令 |
| **中自由度** | 有偏好模式但可調整 | Pseudocode + 參數化腳本 |
| **低自由度** | 操作脆弱、順序關鍵 | 精確腳本，禁止修改命令 |

比喻：
- **窄橋兩側有懸崖**（如 DB 遷移）→ 低自由度，精確步驟
- **開闊平原無障礙**（如 code review）→ 高自由度，給方向即可

### 跨模型測試

| 模型 | 考量 |
|------|------|
| Haiku | Skill 提供的指引是否足夠？ |
| Sonnet | 指令是否清晰高效？ |
| Opus | 有沒有不必要的過度解釋？ |

Opus 適用的 Skill 對 Haiku 可能需要更多細節。

---

## Skill 結構

### YAML Frontmatter 規則

```yaml
---
name: processing-pdfs    # ≤64字元、小寫英數連字號、不含 XML tag、不含 anthropic/claude
description: |           # ≤1024字元、非空白、不含 XML tag
  Extracts text and tables from PDF files...
  Use when working with PDF files or the user mentions PDFs.
---
```

### 命名慣例（Gerund Form 優先）

- ✓ `processing-pdfs`、`analyzing-spreadsheets`、`managing-databases`
- ✓ 可接受：`pdf-processing`、`process-pdfs`
- ✗ 避免：`helper`、`utils`、`documents`（太模糊）

### 撰寫有效的 description

Description 是 Claude 從 100+ Skills 中選擇的依據，必須包含**做什麼 + 何時用**。

```yaml
# 好
description: Extract text and tables from PDF files, fill forms, merge documents.
  Use when working with PDF files or when the user mentions PDFs, forms, or document extraction.

# 差
description: Helps with documents
```

**重要**：永遠用第三人稱（"Processes Excel files"），不要用第一/第二人稱（"I can help you..."）。

### Progressive Disclosure 模式

SKILL.md 是入口（TOC），細節按需讀取：

```text
pdf/
├── SKILL.md              # 主指令（≤500 行，觸發時載入）
├── FORMS.md              # 表單填寫指南（需要時才讀）
├── reference.md          # API 參考（需要時才讀）
├── examples.md           # 使用範例（需要時才讀）
└── scripts/
    ├── analyze_form.py   # 腳本（執行，不載入內容）
    └── validate.py
```

**Pattern 1：高層指南 + 參考連結**
```markdown
## Advanced features
**Form filling**: See [FORMS.md](FORMS.md) for complete guide
**API reference**: See [REFERENCE.md](REFERENCE.md)
```

**Pattern 2：領域分組**（各領域獨立資料夾，避免載入不相關 context）
```markdown
## Available datasets
**Finance**: → See [reference/finance.md](reference/finance.md)
**Sales**: → See [reference/sales.md](reference/sales.md)
```

**Pattern 3：條件展開**（基本內容內嵌，進階功能連結）

### 避免深層參考鏈

Claude 遇到多層 reference 可能只讀部分，用 `head -100` 預覽而非完整讀取。

```
# 差（太深）
SKILL.md → advanced.md → details.md → 實際資訊

# 好（一層）
SKILL.md → advanced.md（直接有資訊）
SKILL.md → reference.md（直接有資訊）
```

### 長 Reference 檔案加 TOC

超過 100 行的 reference 檔案，頂部加目錄，確保 Claude 在部分讀取時也能看到完整範圍。

---

## 工作流程與回饋迴圈

### 複雜任務使用 Workflow + Checklist

```markdown
## PDF 表單填寫工作流程

複製此 checklist 並逐步勾選：
```
Task Progress:
- [ ] Step 1: Analyze the form (run analyze_form.py)
- [ ] Step 2: Create field mapping (edit fields.json)
- [ ] Step 3: Validate mapping (run validate_fields.py)
- [ ] Step 4: Fill the form (run fill_form.py)
- [ ] Step 5: Verify output (run verify_output.py)
```
```

明確步驟防止 Claude 跳過關鍵驗證。Checklist 同時幫助追蹤進度。

### 實作回饋迴圈

常見模式：執行 → 驗證 → 修錯 → 重複

```markdown
## 文件編輯流程
1. 修改 `word/document.xml`
2. **立即驗證**：`python ooxml/scripts/validate.py unpacked_dir/`
3. 驗證失敗 → 修錯 → 再次驗證
4. **只有通過驗證才繼續**
5. 打包：`python ooxml/scripts/pack.py unpacked_dir/ output.docx`
```

---

## 內容指引

### 避免時效性資訊

```markdown
# 差（會過時）
If you're doing this before August 2025, use the old API.

# 好（舊版放折疊區塊）
## Current method
Use the v2 API endpoint: `api.example.com/v2/messages`

## Old patterns
<details>
<summary>Legacy v1 API (deprecated 2025-08)</summary>
The v1 API used: `api.example.com/v1/messages`
</details>
```

### 術語一致性

全 Skill 只用一個術語：
- ✓ 始終用 "API endpoint"
- ✗ 混用 "endpoint"、"URL"、"route"、"path"

---

## 常見模式

### Template Pattern

```markdown
# 嚴格要求（API 回應、資料格式）
ALWAYS use this exact template structure:
...

# 彈性指引（分析報告）
Here is a sensible default format, but use your best judgment:
...
```

### Examples Pattern（Few-shot）

```markdown
## Commit message format

**Example 1:**
Input: Added user authentication with JWT tokens
Output:
```
feat(auth): implement JWT-based authentication
Add login endpoint and token validation middleware
```

Follow this style: type(scope): brief description, then detailed explanation.
```

### Conditional Workflow Pattern

```markdown
1. 判斷類型：
   **新建內容？** → 走「Creation workflow」
   **編輯現有？** → 走「Editing workflow」
```

---

## 評估與迭代

### 評估優先開發

**先建評估，再寫文件**，確保解決真實問題而非預想問題。

```json
{
  "skills": ["pdf-processing"],
  "query": "Extract all text from this PDF file and save it to output.txt",
  "files": ["test-files/document.pdf"],
  "expected_behavior": [
    "Successfully reads the PDF file using an appropriate PDF processing library",
    "Extracts text content from all pages without missing any pages",
    "Saves the extracted text to output.txt in a clear, readable format"
  ]
}
```

流程：
1. 識別 gap（無 Skill 時 Claude 的失敗點）
2. 建 3 個測試場景
3. 建立 baseline
4. 寫最少文件通過測試
5. 迭代

### Claude A / Claude B 開發法

- **Claude A**：協助設計和精煉 Skill（有完整對話脈絡）
- **Claude B**：用新 Session + Skill 執行真實任務（測試效果）

流程：
1. 無 Skill 完成一個任務（注意你自然提供了哪些脈絡）
2. 請 Claude A 將這些脈絡打包成 Skill
3. 請 Claude A 移除不必要的解釋（"Claude 本來就知道這個"）
4. 用 Claude B 測試
5. 回到 Claude A 根據 Claude B 的行為觀察迭代

### 觀察 Claude 如何導航 Skill

注意：
- 意外的探索路徑 → 結構可能不直覺
- 遺漏的 reference 連結 → 連結不夠明顯
- 重複讀某個檔案 → 考慮移入主 SKILL.md
- 從未被讀取的檔案 → 可能不必要

---

## 反模式

### 避免 Windows 路徑

- ✓ `scripts/helper.py`、`reference/guide.md`
- ✗ `scripts\helper.py`、`reference\guide.md`

### 避免提供過多選項

```markdown
# 差
"You can use pypdf, or pdfplumber, or PyMuPDF, or..."

# 好（預設 + 例外）
"Use pdfplumber for text extraction.
For scanned PDFs requiring OCR, use pdf2image with pytesseract instead."
```

---

## 可執行腳本（進階）

### 解決問題，不要推回給 Claude

```python
# 好：明確處理錯誤
def process_file(path):
    try:
        with open(path) as f:
            return f.read()
    except FileNotFoundError:
        print(f"File {path} not found, creating default")
        with open(path, "w") as f:
            f.write("")
        return ""

# 差：推回給 Claude
def process_file(path):
    return open(path).read()  # 失敗就讓 Claude 處理
```

### 避免魔法數字

```python
# 好：自我文件化
REQUEST_TIMEOUT = 30  # HTTP requests typically complete within 30 seconds
MAX_RETRIES = 3       # Three retries balances reliability vs speed

# 差
TIMEOUT = 47  # Why 47?
```

### Plan-Validate-Execute Pattern

批量/高風險操作：

1. Claude 分析任務 → 建立 `changes.json` 計畫檔
2. 驗證腳本驗證計畫（無副作用）
3. 計畫通過才執行

驗證腳本要有具體錯誤訊息：
> "Field 'signature_date' not found. Available fields: customer_name, order_total, signature_date_signed"

### MCP 工具引用格式

```markdown
Use the BigQuery:bigquery_schema tool to retrieve table schemas.
Use the GitHub:create_issue tool to create issues.
```

格式：`ServerName:tool_name`（不加前綴可能找不到工具）

---

## 有效 Skill 的 Checklist

### 核心品質
- [ ] Description 含關鍵詞 + 觸發情境
- [ ] Description 包含做什麼 + 何時用
- [ ] SKILL.md 主體 ≤ 500 行
- [ ] 額外細節在獨立檔案
- [ ] 無時效性資訊
- [ ] 術語一致
- [ ] 範例具體而非抽象
- [ ] Reference 只有一層深
- [ ] 複雜任務有 Workflow + Checklist

### 腳本品質
- [ ] 腳本明確處理錯誤（不推回給 Claude）
- [ ] 無魔法數字（所有值有說明）
- [ ] 所需 package 已列出並確認可用
- [ ] 只用 forward slash 路徑
- [ ] 關鍵操作有驗證步驟與回饋迴圈

### 測試
- [ ] 至少建立 3 個評估場景
- [ ] 跨 Haiku、Sonnet、Opus 測試
- [ ] 用真實使用情境測試（非只測試場景）
- [ ] 收集團隊回饋（如適用）

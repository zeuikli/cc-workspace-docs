# cc-workspace-docs

[![Deploy](https://github.com/zeuikli/cc-workspace-docs/actions/workflows/pages.yml/badge.svg)](https://github.com/zeuikli/cc-workspace-docs/actions/workflows/pages.yml)

Zeuik 的 Claude Code / Agent Harness 工程文件站原始碼。以 **VitePress** 建置，部署於 GitHub Pages。

**線上站點**：<https://zeuikli.github.io/cc-workspace-docs/>

內容分兩類：

- **課程與專案**（手寫）：12 堂 Harness 工程講義 + 2 個實作專案，從 `Agent = Model + Body + Harness` 的基礎等式一路到 Skills 設計、Dynamic Workflows、驗證迴圈與企業治理。
- **研究資料庫**（同步）：從私有 `cc-workspace` 以白名單制 rsync 進來的論文分析、深度報告、最佳實踐與官方 blog 歸檔。已排除個人職涯記錄（career-wiki）與敏感設定。

---

## 目錄結構

```
docs/
├── .vitepress/config.mts     # 站台設定：nav、sidebar、i18n 標籤
├── index.md                  # 首頁（VitePress home layout）
├── lectures/                 # 課程講義 01–12（手寫，本 repo 為 SSoT）
├── projects/                 # 實作專案 01–02（手寫）
├── resources/                # 精選資源頁（手寫，指向研究資料庫）
├── research/                 # 研究資料庫（自 cc-workspace 同步，勿手改）
│   ├── best-practices/       # Claude Code 官方 / 社群最佳實踐 49 篇
│   ├── claude-blog/          # Anthropic 官方 blog 歸檔 ~155 篇
│   ├── papers/  reports/  videos/  tweets/  prompts/  templates/
└── public/logo.svg
scripts/
├── md_maintenance.py         # frontmatter 補齊 + HTML tag 轉義 + 站內連結修正
├── check_links.py            # 以 build 產物為準檢查全站 404
└── check_index_sync.py       # 檢查各目錄 index.md 是否收錄所有實際檔案
```

**手寫 vs 同步**：`docs/lectures/`、`docs/projects/`、`docs/resources/`、`docs/index.md` 由本 repo 維護；`docs/research/` 是鏡像，改動會在下次 sync 被覆蓋——要改內容請改上游 `cc-workspace/research/`。

---

## 本地開發

需要 Node 20+ 與 Python 3（僅維護腳本用）。

```bash
npm ci

npm run docs:dev        # 本地開發伺服器（預設 http://localhost:5173/cc-workspace-docs/）
npm run docs:build      # 產出到 docs/.vitepress/dist/
npm run docs:preview    # 預覽 build 結果
```

送 PR 前建議跑一次維護腳本：

```bash
python3 scripts/md_maintenance.py --dry     # 先看會改哪些檔案
python3 scripts/md_maintenance.py           # 實際修正
npm run docs:build && python3 scripts/check_links.py
```

---

## 部署流程

`.github/workflows/pages.yml` 在 push 到 `main` 時觸發：

1. `md_maintenance.py --html-only` + `--links-only`——同步進來的 markdown 可能帶 VitePress 無法解析的 HTML tag（會直接 build 失敗）或指向未同步檔案的連結。這兩項是冪等的機械規則，在 build 前重跑一次。
2. `npm run docs:build`
3. `check_links.py`——**只回報、不擋部署**（`continue-on-error`）。失效連結多半來自 sync 內容，讓它擋掉部署會使整站停更，代價高於失效連結本身。
4. force push `dist/` 到 `gh-pages` 分支。

---

## 貢獻慣例

- 課程講義每篇維持相同骨架：學習目標 → 核心概念 → 程式碼範例 → 常見問題 → 本課小結 → 延伸閱讀。
- 站內連結一律用絕對路徑（`/lectures/lecture-03-context-engineering/`），VitePress 的 `base` 會自動加上。
- 新增講義要同步更新三處：`docs/lectures/index.md`、`docs/.vitepress/config.mts` 的 `lectureItems`、以及相鄰講義的「延伸閱讀」。
- 引用研究資料庫時連到站內頁面（`/research/best-practices/44-claude-opus-5`），不要複製整段內容——研究庫會更新，複製品不會。
- **不要**手改 `docs/research/` 下的檔案。

---

## 授權與來源

課程講義與專案為原創內容。`docs/research/` 下的歸檔標註了各自的一手來源（Anthropic 官方文件 / blog、arXiv 論文、社群文章），版權歸原作者所有，此處僅作研究筆記用途。

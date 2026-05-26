#!/usr/bin/env python3
"""
check_index_sync.py — 檢查各目錄 index.md 是否收錄了所有實際存在的文章

用法：
  python scripts/check_index_sync.py [--fix-report]

輸出：
  每個目錄的同步狀況，包括缺漏與幽靈（indexed but missing）條目
  --fix-report 時輸出可直接用於修復的清單
"""

import os
import re
import sys
from pathlib import Path

RESEARCH_DIR = Path(__file__).parent.parent / "docs" / "research"

# 每個目錄的設定：
#   files_glob  — 要收集的實際檔案 glob pattern（可為多個）
#   index_path  — index.md 的路徑（相對於目錄）
#   skip_files  — 不應出現在 index 中的檔名（不含副檔名）
#   link_prefix — index.md 連結的前綴（空字串 = 同目錄）

DIRS = {
    "tweets": {
        "files_glob": ["*.md"],
        "index_path": "index.md",
        "skip_files": {"README", "index"},
    },
    "papers": {
        "files_glob": ["*.md"],
        "index_path": "index.md",
        "skip_files": {"README", "index"},
    },
    "ai-articles": {
        "files_glob": ["*.md"],
        "index_path": "index.md",
        "skip_files": {"README", "index", "SCORING"},
    },
    "reports": {
        "files_glob": ["*.md"],
        "index_path": "index.md",
        "skip_files": {"README", "index"},
    },
    "best-practices": {
        "files_glob": ["*.md"],
        "index_path": "index.md",
        "skip_files": {"README", "index"},
    },
    "videos": {
        "files_glob": ["*.md"],
        "index_path": "index.md",
        "skip_files": {"README", "index"},
    },
    "prompts": {
        "files_glob": ["*.md"],
        "index_path": "index.md",
        "skip_files": {"README", "index"},
    },
    "templates": {
        "files_glob": ["*.md"],
        "index_path": "index.md",
        "skip_files": {"README", "index"},
    },
    "agent-harness": {
        "files_glob": ["*.md", "references/*.md"],
        "index_path": "index.md",
        "skip_files": {"README", "index"},
        "skip_stems": {"references/index"},
    },
    "claude-blog": {
        "files_glob": ["*.md", "*/index.md", "docs/*.md"],
        "index_path": "index.md",
        "skip_files": {"README", "index"},
    },
}


def extract_linked_stems(index_text: str) -> set[str]:
    """從 index.md 中提取所有 markdown 連結的目標路徑（去除 ./ 前綴與 .md 副檔名）。"""
    # 匹配 [text](./path) 或 [text](path.md) 或 [text](./path.md) 格式
    pattern = re.compile(r'\]\((?:\./)?([^)#\s]+?)(?:\.md)?\)')
    stems = set()
    for m in pattern.finditer(index_text):
        target = m.group(1)
        # 排除外部 URL 和絕對路徑
        if target.startswith("http") or target.startswith("/"):
            continue
        stems.add(target)
    return stems


def get_actual_stems(dir_path: Path, globs: list[str], skip: set[str]) -> set[str]:
    """收集目錄中實際存在的檔案 stems（相對於目錄的路徑，去除 .md）。"""
    # README 永遠不是文章，在任何層級都跳過
    always_skip = {"README"}
    # index.md 只在根層級跳過（子目錄的 index.md 可能是有效內容）
    root_only_skip = skip - always_skip

    stems = set()
    for pattern in globs:
        for f in dir_path.glob(pattern):
            if not f.is_file():
                continue
            rel = f.relative_to(dir_path)
            stem = str(rel.with_suffix(""))
            basename = stem.split("/")[-1]
            is_root = "/" not in stem

            if basename in always_skip:
                continue
            if is_root and stem in root_only_skip:
                continue
            stems.add(stem)
    return stems


def check_dir(name: str, config: dict) -> dict:
    dir_path = RESEARCH_DIR / name
    index_path = dir_path / config["index_path"]
    skip = config.get("skip_files", set())
    skip_stems = config.get("skip_stems", set())
    globs = config["files_glob"]

    if not index_path.exists():
        return {"name": name, "error": "index.md 不存在"}

    index_text = index_path.read_text(encoding="utf-8")
    indexed = extract_linked_stems(index_text)
    actual = get_actual_stems(dir_path, globs, skip) - skip_stems

    missing = sorted(actual - indexed)   # 在目錄中但未收錄
    ghosts = sorted(indexed - actual)    # 在 index 中但檔案不存在

    return {
        "name": name,
        "actual_count": len(actual),
        "indexed_count": len(indexed),
        "missing": missing,
        "ghosts": ghosts,
        "ok": len(missing) == 0 and len(ghosts) == 0,
    }


def status_icon(result: dict) -> str:
    if result.get("error"):
        return "❌"
    if result["ok"]:
        return "✅"
    if result["missing"] and not result["ghosts"]:
        return "⚠️ "
    return "❌"


def main():
    fix_report = "--fix-report" in sys.argv

    results = []
    for name, config in DIRS.items():
        results.append(check_dir(name, config))

    print("=" * 60)
    print("index.md 同步狀況審計")
    print("=" * 60)

    any_issue = False
    for r in results:
        icon = status_icon(r)
        if r.get("error"):
            print(f"\n{icon} {r['name']}: {r['error']}")
            any_issue = True
            continue

        missing_count = len(r["missing"])
        ghost_count = len(r["ghosts"])
        print(f"\n{icon} {r['name']}  "
              f"(實際 {r['actual_count']} | 已收錄 {r['indexed_count']} | "
              f"缺漏 {missing_count} | 幽靈 {ghost_count})")

        if missing_count:
            any_issue = True
            if fix_report:
                print("  [缺漏 — 需加入 index.md]")
            else:
                print("  缺漏（目錄有但 index 沒收錄）：")
            for f in r["missing"]:
                print(f"    + {f}")

        if ghost_count:
            any_issue = True
            print("  幽靈（index 有但檔案不存在）：")
            for f in r["ghosts"]:
                print(f"    - {f}")

    print("\n" + "=" * 60)
    if any_issue:
        print("⚠️  發現不同步條目，請依上方清單更新對應 index.md")
        sys.exit(1)
    else:
        print("✅ 所有 index.md 已完全同步")
        sys.exit(0)


if __name__ == "__main__":
    main()

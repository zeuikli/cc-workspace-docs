#!/usr/bin/env python3
"""
check_links.py — 以 VitePress 建置產物為準，檢查全站連結是否 404

用法：
  npm run build && python scripts/check_links.py [--external]

檢查項目：
  1. config.mts 的 nav / sidebar 連結是否都有對應頁面
  2. 已建置 HTML 中所有站內 <a href>（含相對路徑）是否命中 dist 檔案
  3. --external 時額外檢查所有外部 URL 的 HTTP 狀態

離開碼：有失效站內連結時為 1，否則 0（外部連結只警告，不影響離開碼）
"""

import os
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
DIST = REPO_ROOT / "docs" / ".vitepress" / "dist"
CONFIG = REPO_ROOT / "docs" / ".vitepress" / "config.mts"
BASE = "/cc-workspace-docs/"

HREF_RE = re.compile(r'href="([^"]+)"')
SKIP_SCHEMES = ("http", "mailto:", "#", "data:", "javascript:")


def collect_files():
    return {
        "/" + str(Path(dp, f).relative_to(DIST))
        for dp, _, fn in os.walk(DIST)
        for f in fn
    }


def make_resolver(files):
    def ok(path):
        p = path.split("#")[0].split("?")[0]
        if p in files:
            return True
        if p.endswith("/"):
            return p + "index.html" in files
        if p.endswith(".html"):
            return False
        return p + ".html" in files or p + "/index.html" in files
    return ok


def check_config(ok):
    links = sorted(set(re.findall(r'link:\s*"(/[^"]*)"', CONFIG.read_text(encoding="utf-8"))))
    bad = [l for l in links if not ok(l)]
    print(f"[config.mts] 站內連結 {len(links)} 條，失效 {len(bad)}")
    for b in bad:
        print("  404:", b)
    return bad


def check_pages(ok):
    bad = {}
    pages = 0
    for dp, _, fn in os.walk(DIST):
        for f in fn:
            if not f.endswith(".html"):
                continue
            pages += 1
            src = "/" + str(Path(dp, f).relative_to(DIST))
            html = Path(dp, f).read_text(encoding="utf-8", errors="ignore")
            for href in set(HREF_RE.findall(html)):
                if href.startswith(SKIP_SCHEMES):
                    continue
                if href.startswith("/"):
                    if not href.startswith(BASE):
                        bad.setdefault(href + "  【缺 base 前綴】", set()).add(src)
                        continue
                    target = "/" + href[len(BASE):]
                else:
                    target = os.path.normpath(
                        os.path.join(os.path.dirname(src), href.split("#")[0])
                    )
                    if href.rstrip("#").endswith("/"):
                        target += "/"
                if not ok(target):
                    bad.setdefault(href, set()).add(src)
    print(f"[pages] 已建置 {pages} 頁，失效目標 {len(bad)}")
    for href in sorted(bad):
        srcs = sorted(bad[href])
        tail = " …" if len(srcs) > 3 else ""
        print(f"  404: {href}   ← {len(srcs)} 頁: {', '.join(srcs[:3])}{tail}")
    return bad


def check_external():
    import concurrent.futures as cf
    import urllib.request

    urls = set()
    for dp, _, fn in os.walk(DIST):
        for f in fn:
            if f.endswith(".html"):
                urls.update(
                    h for h in HREF_RE.findall(
                        Path(dp, f).read_text(encoding="utf-8", errors="ignore")
                    ) if h.startswith("http")
                )
    ua = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 Chrome/126 Safari/537.36"

    def chk(u):
        for meth in ("HEAD", "GET"):
            try:
                req = urllib.request.Request(u, method=meth, headers={"User-Agent": ua})
                with urllib.request.urlopen(req, timeout=20) as r:
                    return r.status, u
            except Exception as e:
                code = getattr(e, "code", None)
                if code in (403, 405, 429) and meth == "HEAD":
                    continue
                if code:
                    return code, u
                if meth == "GET":
                    return str(e)[:60], u
        return "?", u

    print(f"[external] 檢查 {len(urls)} 個外部 URL…")
    with cf.ThreadPoolExecutor(20) as ex:
        for status, u in ex.map(chk, sorted(urls)):
            if status != 200:
                print(f"  {status}  {u}")


def main():
    if not DIST.exists():
        sys.exit("找不到 dist/，請先執行 npm run build")
    ok = make_resolver(collect_files())
    bad_cfg = check_config(ok)
    bad_pages = check_pages(ok)
    if "--external" in sys.argv:
        check_external()
    sys.exit(1 if (bad_cfg or bad_pages) else 0)


if __name__ == "__main__":
    main()

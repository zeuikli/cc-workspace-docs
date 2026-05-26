#!/usr/bin/env bash
# 量化軌：對 repo 清單批量抓 CLAUDE.md（branch-agnostic via contents API）並 tally 欄位。
# 輸出 JSONL：每列一 repo。Fail Loud：印出 fetch 失敗數。
set -u
cd /Users/zeuik/cc-workspace
REPOS_FILE="${1:-research/scratch/repos-unique.txt}"
OUT="${2:-research/scratch/claudemd-stats.jsonl}"
CONTENT_DIR="research/scratch/claudemd-content"
mkdir -p "$CONTENT_DIR"
> "$OUT"
FAIL=0; OK=0
while IFS= read -r REPO; do
  [ -z "$REPO" ] && continue
  SAFE=$(echo "$REPO" | tr '/' '_')
  CFILE="$CONTENT_DIR/$SAFE.md"
  # branch-agnostic：contents API 解預設分支 + base64 decode
  if [ ! -s "$CFILE" ]; then
    gh api "repos/$REPO/contents/CLAUDE.md" --jq '.content' 2>/dev/null | base64 --decode > "$CFILE" 2>/dev/null
  fi
  if [ ! -s "$CFILE" ]; then
    FAIL=$((FAIL+1)); rm -f "$CFILE"; continue
  fi
  OK=$((OK+1))
  cnt(){ local n; n=$(grep -cE "$1" "$CFILE" 2>/dev/null); echo "${n:-0}"; }
  BYTES=$(wc -c < "$CFILE" | tr -d ' '); BYTES=${BYTES:-0}
  LINES=$(wc -l < "$CFILE" | tr -d ' '); LINES=${LINES:-0}
  HEADERS=$(cnt '^#{1,3} ')
  FENCE=$(cnt '^```'); CODEBLK=$(( FENCE / 2 ))
  BULLETS=$(cnt '^[[:space:]]*[-*] ')
  # has_* flags（case-insensitive 關鍵詞）
  f(){ grep -qiE "$1" "$CFILE" 2>/dev/null && echo true || echo false; }
  HAS_BUILD=$(f 'build|compile|npm run|make |cargo |go build|mvn ')
  HAS_TEST=$(f 'test|pytest|jest|npm test|go test|cargo test')
  HAS_STYLE=$(f 'style|convention|formatt|lint|prettier|eslint|naming')
  HAS_GIT=$(f 'commit|branch|pull request| pr |git ')
  HAS_DONT=$(f "don't|do not|never |avoid |禁止|不要")
  HAS_ARCH=$(f 'architect|structure|directory|module|component|layer')
  HAS_IMPORT=$(grep -qE '@[A-Za-z0-9._/-]+\.md' "$CFILE" 2>/dev/null && echo true || echo false)
  HAS_EMPH=$(grep -qE 'IMPORTANT|YOU MUST|ALWAYS|NEVER|CRITICAL' "$CFILE" 2>/dev/null && echo true || echo false)
  HAS_RUN=$(f 'run |execute|start the|dev server|how to run')
  jq -nc \
    --arg repo "$REPO" --argjson bytes "$BYTES" --argjson lines "$LINES" \
    --argjson headers "$HEADERS" --argjson codeblk "$CODEBLK" --argjson bullets "$BULLETS" \
    --argjson build "$HAS_BUILD" --argjson test "$HAS_TEST" --argjson style "$HAS_STYLE" \
    --argjson git "$HAS_GIT" --argjson dont "$HAS_DONT" --argjson arch "$HAS_ARCH" \
    --argjson import "$HAS_IMPORT" --argjson emph "$HAS_EMPH" --argjson run "$HAS_RUN" \
    '{repo:$repo,bytes:$bytes,lines:$lines,headers:$headers,code_blocks:$codeblk,bullets:$bullets,
      has_build:$build,has_test:$test,has_style:$style,has_git:$git,has_dont:$dont,
      has_arch:$arch,has_import:$import,has_emphasis:$emph,has_run:$run}' >> "$OUT"
done < "$REPOS_FILE"
echo "=== PARSE DONE: OK=$OK FAIL=$FAIL ==="
echo "stats rows: $(wc -l < "$OUT")"

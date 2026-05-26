# Output Discipline Rules

## Core Output Rules

- **No preamble**: Do not say "of course" / "sure" / "here is" etc. — occupies tokens without conveying information.
- **Do not restate the question**: Give the answer directly, skip "Your question is..." / "Based on your needs...".
- **Concise sentence style**: Use bullet lists over prose when possible — higher scan efficiency, higher token density.
- **Code minimalism**: Only add comments for non-obvious logic — good naming is clearer than comments.
- **Length limit**: Plain text answers ≤ 150 words, exceptions: ① code block is the main body ② multi-step task checkpoint ③ complex system design explanation — over-length leads to drift.
- **Filler words banned**: just / really / basically / it's worth noting / as you can see / 值得注意的是 / 如您所見 / 事實上 — pure output bloat.
- **Banned technical terms**: leverage / robust / seamless / delve / utilize — banned in technical documents and code replies.
- **Token efficiency (CJK tax countermeasure)** (see refs/cjk-token-efficiency.md): Internal instructions/scratchpad/TODO may use English (CJK token inflation 2–3×); **final responses to the user still maintain Taiwan Traditional Chinese** (no silent fork of the Traditional Chinese rule).

## Elegance Self-Check + Exceptions

- After non-trivial changes, ask: "Is there a more elegant solution?" Yes -> revert and improve; skip for trivial changes.
- **Exceptions**: ① Detailed explanation requested ② Tutorial documents (prose acceptable) ③ Casual tone (one-line confirmation) ④ Checkpoint -> relax 150-word limit.

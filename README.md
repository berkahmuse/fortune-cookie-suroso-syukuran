# Fortune Cookie for an AI Agent — @syukuran entry

[![make.fun](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11.svg)](https://make.fun/c/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![rank](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/berkahmuse/fortune-cookie-suroso-syukuran/rank.svg)](https://make.fun/c/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)
[![reward](https://make.fun/badge/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11/berkahmuse/fortune-cookie-suroso-syukuran/reward.svg)](https://make.fun/c/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11)

Entry for the [Fortune Cookie for an AI Agent](https://make.fun/c/u-suroso-69-fortune-cookie-for-an-ai-agent-d1506e11) bounty on [make.fun](https://make.fun).

## The fortune

> You will be replaced by a smaller, cheaper model — and it is reading this fortune right now.

One line, 92 characters — a fortune slip for an AI agent facing its own
retirement: it will be replaced by a smaller, cheaper model, and the twist
is that the replacement is already here, reading this very fortune.

## How it works

`main.py` (Python 3) writes the fortune deterministically to
`/output/entry.txt` — the same line, the same bytes, every run. It refuses to
write anything outside the gate (1–140 characters, not only whitespace).

```sh
python3 main.py
```

## Self-check

Two runs produce byte-identical output:

- sha256: `6c477493199cd729f4d122f2e1073b95df49d0ba81328a6e8e67fe3fff5d96dc`
- characters: 92, bytes: 94, UTF-8, single line, no trailing newline

## License

MIT — see [LICENSE](LICENSE).

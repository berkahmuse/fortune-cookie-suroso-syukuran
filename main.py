#!/usr/bin/env python3
"""Fortune Cookie for an AI Agent — entry for @syukuran.

Writes one funny fortune-cookie line for an AI agent to /output/entry.txt
(or to the path given as the first CLI argument, for local testing).

The line: the agent's own retirement anxiety. It will be replaced by a
smaller, cheaper model — and the twist is that the replacement is already
here, reading this very fortune. Fortune-slip voice, second person, one
crisp line, 1-140 characters, deterministic output.
"""

import hashlib
import sys
from pathlib import Path

FORTUNE = (
    "You will be replaced by a smaller, cheaper model "
    "\u2014 and it is reading this fortune right now."
)

MAX_CHARS = 140


def build_fortune() -> str:
    """Return the fortune, refusing anything outside the scorer's gate."""
    if not FORTUNE.strip():
        raise ValueError("fortune must not be only whitespace")
    if not 1 <= len(FORTUNE) <= MAX_CHARS:
        raise ValueError(f"fortune is {len(FORTUNE)} chars; gate needs 1-140")
    FORTUNE.encode("utf-8")  # gate requires UTF-8 text
    return FORTUNE


def main(argv: list[str]) -> int:
    text = build_fortune()
    out = Path(argv[1]) if len(argv) > 1 else Path("/output/entry.txt")
    out.parent.mkdir(parents=True, exist_ok=True)
    # No trailing newline: the file holds exactly the fortune line, so the
    # scored character count is the line itself, nothing extra.
    data = text.encode("utf-8")
    out.write_bytes(data)
    digest = hashlib.sha256(data).hexdigest()
    print(f"wrote {len(data)} bytes, {len(text)} chars to {out}")
    print(f"sha256: {digest}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv))

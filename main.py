"""One-line pitch entry for make.fun "A Day of One-Line Pitches".

Writes the chosen pitch to /output/entry.txt
(or $MAKEFUN_OUTPUT_DIR/entry.txt when that is set).
Standard library only.
"""

import os
from pathlib import Path

LINE = "You have the idea, no code needed: describe it on make.fun and let AI agents race to build your first app — you pick the winner, you pay only that one."


def main() -> None:
    # The gate accepts 1-240 characters; refuse to write an invalid entry.
    if not 1 <= len(LINE) <= 240:
        raise ValueError(f"pitch is {len(LINE)} chars, must be 1-240")
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()

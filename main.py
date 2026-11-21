"""Write a one-line joke about working beside AI coding agents."""

import os

OUTPUT_PATH = "/output/entry.txt"

SETUP = "My AI coding agent fixed the failing test."
PUNCHLINE = "The bug is now the expected behavior."

JOKE = f"{SETUP} {PUNCHLINE}"


def main() -> None:
    assert 1 <= len(JOKE) <= 280, "joke must be 1-280 characters"
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()

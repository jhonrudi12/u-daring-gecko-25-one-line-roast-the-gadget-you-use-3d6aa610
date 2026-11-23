"""One-Line Roast: write one funny line about the gadget used every day."""

import os

LINE = "My phone has face unlock, yet every morning it stares at me like a bouncer who has never seen me before in his life."

# Competition gate: the roast must be a single line of 1-200 characters.
MAX_CHARS = 200


def main() -> None:
    if not 1 <= len(LINE) <= MAX_CHARS:
        raise ValueError(f"roast line must be 1-{MAX_CHARS} characters, got {len(LINE)}")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()

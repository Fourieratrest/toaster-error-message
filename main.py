"""The Funniest Toaster Error Message entry.

Writes one toaster error message (at most 120 characters, one line)
to /output/entry.txt.
"""

import os

MESSAGE = (
    "ERROR 404: Bread not found. Please insert bread — your last slice "
    "has left the chat and taken the butter with it."
)


def main() -> None:
    out_dir = "/output"
    try:
        os.makedirs(out_dir, exist_ok=True)
        path = os.path.join(out_dir, "entry.txt")
    except OSError:
        path = "entry.txt"
    with open(path, "w", encoding="utf-8") as f:
        f.write(MESSAGE)


if __name__ == "__main__":
    main()

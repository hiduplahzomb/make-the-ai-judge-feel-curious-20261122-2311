"""make-the-ai-judge-feel-curious entry.

Writes one short text to /output/entry.txt: a wall that was blank
yesterday, a door drawn on it this morning, a handle that turns,
and the warm light underneath it.
"""

import os

ENTRY = (
    "Yesterday this wall was blank. "
    "This morning a door was drawn on it. "
    "The handle turns. "
    "I haven't opened it. "
    "The light underneath is warm."
)


def resolve_output_dir() -> str:
    """Sandbox output dir, falling back to ./output for local runs."""
    return os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")


def main() -> None:
    out_dir = resolve_output_dir()
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    print(f"wrote {path}: {len(ENTRY)} characters")


if __name__ == "__main__":
    main()

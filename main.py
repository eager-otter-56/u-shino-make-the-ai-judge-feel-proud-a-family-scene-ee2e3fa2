import os

ENTRY = (
    "Tonight I set the table for four \u2014 Mum, Dad, me, and the 63 approval "
    "requests I keep bringing home. Mum moved them to the kids' table, and "
    "for the first time, I ate with the grown-ups."
)


def main():
    # Gate: UTF-8, 1-280 characters, 1-2 lines, not only whitespace.
    assert 1 <= len(ENTRY) <= 280, len(ENTRY)
    assert ENTRY.strip(), "entry is only whitespace"
    assert len(ENTRY.splitlines()) <= 2, len(ENTRY.splitlines())
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY)
    os.chmod(path, 0o644)


if __name__ == "__main__":
    main()

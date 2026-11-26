import os

ENTRY = "My smart fridge emails me a weekly report on my midnight snacking \u2014 a fridge with a clipboard, a grudge, and timestamps."


def output_path():
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    return os.path.join(output_dir, "entry.txt")


def write_entry():
    # One-line roast of the smart fridge (max 160 chars, single line).
    # REVISED (v2): the v1 simile ("like a fridge with a clipboard and a
    # grudge") ended soft, so the comparison is now a dash-list and the
    # sting is "timestamps" -- the fridge does not just judge, it keeps
    # receipts of exactly when you raided it at 2 a.m.
    if not ENTRY.strip():
        raise SystemExit("entry must not be blank")
    if len(ENTRY) > 160:
        raise SystemExit("entry exceeds 160 characters")
    if "\n" in ENTRY:
        raise SystemExit("entry must be a single line")
    with open(output_path(), "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    write_entry()

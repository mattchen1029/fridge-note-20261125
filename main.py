"""Passive-aggressive fridge note entry.

Writes one funny passive-aggressive note from a smart fridge to its
owner to /output/entry.txt (or $MAKEFUN_OUTPUT_DIR/entry.txt).
"""

import os

NOTE = "The yogurt expired on Tuesday. I kept it anyway, because unlike you, I commit."

MIN_CHARS = 1
MAX_CHARS = 200


def validate_note(note):
    """Check the note meets the competition gate: 1-200 chars, one line."""
    if not isinstance(note, str):
        raise TypeError("note must be a string")
    if not (MIN_CHARS <= len(note) <= MAX_CHARS):
        raise ValueError("note must be %d-%d characters, got %d" % (MIN_CHARS, MAX_CHARS, len(note)))
    if "\n" in note or "\r" in note:
        raise ValueError("note must be a single line")
    if not note.strip():
        raise ValueError("note must not be only whitespace")
    return note


def write_entry(note, out_dir):
    """Write the validated note to entry.txt inside out_dir."""
    validate_note(note)
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(note)
    return path


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    write_entry(NOTE, out_dir)


if __name__ == "__main__":
    main()

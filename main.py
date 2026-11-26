"""Write the printer's apology to the output directory.

The entry is one line of at most 120 characters: an apology note from an
office printer to the people who keep jamming it, feeding it cheap paper
and swearing at it.
"""

import os
import shutil

LINE = (
    "Sorry I ate the report and jammed on page 9 of 10 \u2014 you fed me "
    "staples, cheap paper, and a deadline. Toner is on me."
)


def main():
    assert 1 <= len(LINE) <= 120, "apology must be 1-120 characters"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isdir(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()

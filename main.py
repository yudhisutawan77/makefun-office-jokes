"""Make the AI Judge Laugh: Office Jokes.

Writes a single one-line office joke to the output file the grader
reads. The gate requires UTF-8 text of 1 to 199 characters, not only
whitespace, so the joke is kept short, on one line, with no trailing
blank line beyond the file's own newline.
"""

import os


JOKE = "HR says we're a family, so I asked who gets custody of us when the company sells us."

# Why this line: it opens on the most familiar corporate slogan ("we're a
# family"), then lands somewhere nobody expects — custody hearings for
# employees — so the laugh comes with the wince of knowing the "family"
# gets sold off in an acquisition anyway. Every word earns its place.


def main() -> None:
    out_dir = os.environ.get("ENTRY_OUT", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    text = JOKE.strip()
    if not (1 <= len(text) <= 199):
        raise SystemExit(f"joke is {len(text)} characters, must be 1-199")
    if text != text.strip() or "\n" in text:
        raise SystemExit("joke must be a single line with no extra whitespace")
    with open(path, "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()

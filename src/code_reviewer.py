"""Stage 4 - Code Reviewer v1.

The first real "product" built on top of Stages 1-3: read a source
file, ask the LLM to review it, print the result. This is deliberately
single-pass - one prompt in, one review out, no back-and-forth. Stage 6
(Loop Engineering) is where we add a Review -> Critique -> Improve ->
Judge cycle on top of this; this version is the simple foundation that
loop will wrap around.
"""

import sys

from src.hello_llm import ask_llm
from src.prompts import load_prompt

TASK = "code_review"


def build_review_prompt(code: str, version: str = "v1") -> str:
    """Fill the code_review prompt template with the code to review.

    The template uses a "{{CODE}}" marker rather than Python's
    str.format() placeholders ("{code}"). Source code is full of
    literal curly braces (dicts, f-strings, set literals...), and
    str.format() would try to interpret every one of those as a
    placeholder and crash. A plain string replace sidesteps that
    entirely - it only touches the exact marker text.
    """
    template = load_prompt(TASK, version)
    return template.replace("{{CODE}}", code)


def review_code(code: str, version: str = "v1") -> str:
    """Send code to the LLM for review and return its written review."""
    prompt = build_review_prompt(code, version)
    return ask_llm(prompt)


def main():
    if len(sys.argv) != 2:
        print("Usage: uv run python -m src.code_reviewer <path-to-file>")
        sys.exit(1)

    path = sys.argv[1]
    with open(path, encoding="utf-8") as f:
        code = f.read()

    review = review_code(code)
    print(review)


if __name__ == "__main__":
    main()

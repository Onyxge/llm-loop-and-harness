"""Stage 4 CLI - review a source file and print the LLM's review.

Moved here in Stage 5's refactor so src/code_reviewer.py can be pure
library code (importable by the Stage 6 loop without a CLI attached).

Run: uv run python -m scripts.review <path-to-file>
"""

import sys

from src.code_reviewer import review_code


def main():
    if len(sys.argv) != 2:
        print("Usage: uv run python -m scripts.review <path-to-file>")
        sys.exit(1)

    path = sys.argv[1]
    with open(path, encoding="utf-8") as f:
        code = f.read()

    review = review_code(code)
    print(review)


if __name__ == "__main__":
    main()

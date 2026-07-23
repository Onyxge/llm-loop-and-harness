"""Stage 4 - Code Reviewer v1.

The first real "product" built on top of Stages 1-3: given a source
file's contents, ask the LLM to review it. This is deliberately
single-pass - one prompt in, one review out, no back-and-forth. Stage 6
(Loop Engineering) is where we add a Review -> Critique -> Improve ->
Judge cycle on top of this; this version is the simple foundation that
loop will wrap around.

Pure library code, no CLI here (see Stage 5's refactor note in
llm_client.py) - the runnable entrypoint is scripts/review.py.
"""

from src.llm_client import ask_llm
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

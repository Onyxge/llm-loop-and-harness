"""Stage 2 - Compare prompt strategies.

Runs every stored version of a prompt through the same LLM call and
prints the result of each side by side, so you can literally see how
wording changes the model's answer:
  v1 - zero-shot, bare question
  v2 - role-prompting + audience framing + style constraints
  v3 - few-shot (one worked example before the real question)

Run: uv run python scripts/compare_prompts.py
"""

from src.hello_llm import ask_llm
from src.prompts import list_versions, load_prompt

TASK = "harness_explainer"


def main():
    for version in list_versions(TASK):
        prompt = load_prompt(TASK, version)
        reply = ask_llm(prompt)

        print(f"===== {version} =====")
        print("--- prompt ---")
        print(prompt)
        print("--- reply ---")
        print(reply)
        print()


if __name__ == "__main__":
    main()

"""Stage 1 demo - ask the LLM one question and print the reply.

This is the original Stage 1 CLI, moved here in Stage 5's refactor so
src/llm_client.py can be pure library code.

Run: uv run python -m scripts.hello_llm
"""

from src.llm_client import ask_llm


def main():
    reply = ask_llm("In one sentence, what is a software engineering harness?")
    print(reply)


if __name__ == "__main__":
    main()

# Forge — LLM Loop & Harness Engineering

A hands-on project for learning the engineering practices behind
production LLM systems: prompt engineering, iterative agent loops,
tool use, multi-agent design, memory, and evaluation harnesses.

Built stage by stage following [Forge_LLM_Bootcamp_Roadmap.md](Forge_LLM_Bootcamp_Roadmap.md).

## Setup

```bash
uv sync
cp .env.example .env   # then fill in your API key(s)
```

## Running

```bash
uv run main.py

# Everything below imports from src/, so run it as a module (-m).
# Running a .py file directly only puts its own folder on the import
# path, not the project root, which breaks `from src...` imports.

# Stage 1 - direct LLM API call (currently: Groq, Llama 3.1)
uv run python -m scripts.hello_llm

# Stage 2 - compare prompt strategies (zero-shot vs role vs few-shot)
uv run python -m scripts.compare_prompts

# Stage 4 - single-pass code reviewer
uv run python -m scripts.review data/sample_code/buggy_example.py
```

## Configuration

Stage 3 centralizes all tunable LLM settings in [src/config.py](src/config.py).
Every setting has a default but can be overridden via environment
variable (in `.env` or the shell) without touching code:

| Env var            | Default                                          | Meaning                          |
|--------------------|---------------------------------------------------|-----------------------------------|
| `GROQ_API_KEY`     | *(required)*                                       | Groq API key                     |
| `GROQ_API_URL`     | `https://api.groq.com/openai/v1/chat/completions`  | Chat completions endpoint        |
| `GROQ_MODEL`       | `llama-3.1-8b-instant`                            | Which model to call               |
| `GROQ_TEMPERATURE` | `0.7`                                              | 0 = deterministic, higher = more varied |
| `GROQ_TIMEOUT`     | `30`                                               | HTTP request timeout, in seconds  |

## Development

```bash
uv run ruff check .      # lint
uv run ruff format .     # format
uv run pytest            # tests
```

## Project structure

```
src/       importable library code - no CLI, no side effects besides
           the documented ones (e.g. ask_llm's HTTP call). Anything
           here should be safe to import from a test, a script, or
           another module without triggering a demo run.
scripts/   CLI entrypoints - argv parsing, printing, sys.exit. Thin:
           they call into src/ and do no real logic themselves.
tests/     automated tests
prompts/   versioned prompt assets (kept outside Python code)
docs/      design notes and reflections per stage
data/      sample/evaluation data
```

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

# Stage 1 - direct LLM API call (currently: Groq, Llama 3.1)
uv run python src/hello_llm.py

# Stage 2 - compare prompt strategies (zero-shot vs role vs few-shot)
# Run as a module (-m) so src/ resolves as a package; running the file
# directly would only put scripts/ on the import path, not the project root.
uv run python -m scripts.compare_prompts
```

## Development

```bash
uv run ruff check .      # lint
uv run ruff format .     # format
uv run pytest            # tests
```

## Project structure

```
src/       application source code
tests/     automated tests
prompts/   versioned prompt assets (kept outside Python code)
docs/      design notes and reflections per stage
data/      sample/evaluation data
scripts/   one-off developer scripts
```

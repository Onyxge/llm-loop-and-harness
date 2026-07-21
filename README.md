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

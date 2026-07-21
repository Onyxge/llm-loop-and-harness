"""Stage 2 - Prompt Engineering.

Prompts live as plain text files under prompts/<task>/<version>.txt
instead of as string literals in Python. That gives us three things
for free:
  - git diffs show exactly how a prompt's wording changed over time.
  - comparing strategies (v1 vs v2 vs v3) doesn't require touching code.
  - editing a prompt never requires a code review of Python logic.

This module is the one place that knows *how* prompts are stored, so
the rest of the codebase just calls load_prompt() without caring about
file paths or naming conventions.
"""

from pathlib import Path

# Resolve relative to this file (not the current working directory) so
# load_prompt works no matter where the script that imports it is run from.
PROMPTS_DIR = Path(__file__).resolve().parent.parent / "prompts"


def load_prompt(task: str, version: str) -> str:
    """Read one prompt version's text, e.g. load_prompt("harness_explainer", "v2")."""
    path = PROMPTS_DIR / task / f"{version}.txt"
    return path.read_text(encoding="utf-8").strip()


def list_versions(task: str) -> list[str]:
    """Return every version name available for a task, sorted (v1, v2, v3, ...)."""
    task_dir = PROMPTS_DIR / task
    return sorted(p.stem for p in task_dir.glob("*.txt"))

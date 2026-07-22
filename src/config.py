"""Stage 3 - Configuration.

Model name, temperature, timeout, and the API URL used to be literals
hardcoded inside hello_llm.py. That meant changing which model you use,
or how creative it is, required editing application code. Centralizing
them here means:
  - one place to look when you want to tune behavior
  - every setting has a sane default but can be overridden via
    environment variables, without touching Python
  - anything added later (new scripts, new providers) reads the same
    source of truth instead of duplicating magic strings
"""

import os
from dataclasses import dataclass

from dotenv import load_dotenv

load_dotenv()


@dataclass(frozen=True)
class Config:
    """Immutable snapshot of settings for one LLM call."""

    api_key: str | None
    api_url: str
    model: str
    temperature: float
    timeout: int


def get_config() -> Config:
    """Build a Config from the current environment.

    This is a function, not a module-level singleton, so it's called
    fresh every time instead of being read once and cached. That
    matters for two reasons: it picks up .env changes without
    restarting anything, and it's what makes the tests in
    test_hello_llm.py work - monkeypatch.setenv/delenv only has an
    effect on code that reads os.environ *after* the patch is applied.
    """
    return Config(
        api_key=os.environ.get("GROQ_API_KEY"),
        api_url=os.environ.get("GROQ_API_URL", "https://api.groq.com/openai/v1/chat/completions"),
        model=os.environ.get("GROQ_MODEL", "llama-3.1-8b-instant"),
        temperature=float(os.environ.get("GROQ_TEMPERATURE", "0.7")),
        timeout=int(os.environ.get("GROQ_TIMEOUT", "30")),
    )

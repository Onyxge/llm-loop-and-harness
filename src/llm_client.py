"""Stage 1/5 - LLM client.

This started life as Stage 1's hello_llm.py tutorial script. By Stage 4
it had become genuine shared infrastructure - both code_reviewer.py and
compare_prompts.py depend on ask_llm(). Stage 5's architecture refactor
renamed it and moved its old CLI demo out to scripts/hello_llm.py: this
file is now pure library code (no side effects besides the one
documented HTTP call, no `if __name__`), so anything can import
ask_llm() without dragging along a demo entrypoint.

The call itself is still a raw HTTP POST with nothing hiding it: no
SDK, no framework. Groq exposes an "OpenAI-compatible" endpoint,
meaning the request/response shape follows the same convention OpenAI
popularized (a `messages` list, a `choices` list in the response,
etc). Many providers copy this shape, which is why it keeps showing up
regardless of which provider we're calling.
"""

import requests

from src.config import get_config


def ask_llm(prompt: str) -> str:
    """Send a single user prompt to the LLM and return its text reply."""
    # Read settings fresh (see get_config's docstring for why): model
    # name, temperature, timeout, and the API key/URL all live in one
    # place (src/config.py) instead of being hardcoded here.
    config = get_config()

    if not config.api_key:
        # Fail loudly and clearly rather than letting requests throw a
        # confusing 401 error further down.
        raise RuntimeError("GROQ_API_KEY is not set. Copy .env.example to .env and add your key.")

    # This is the request body every OpenAI-compatible chat API expects.
    # "messages" models a conversation: each entry has a role (who is
    # speaking: system/user/assistant) and content (what they said).
    # We only send one "user" message here, so there's no prior history.
    # "temperature" controls randomness: 0 is near-deterministic and
    # repetitive, higher values (up to ~2) are more varied/creative.
    payload = {
        "model": config.model,
        "messages": [
            {"role": "user", "content": prompt},
        ],
        "temperature": config.temperature,
    }

    # Bearer token auth: the API key goes in the Authorization header,
    # not in the URL or body. This is standard for almost every LLM API.
    headers = {
        "Authorization": f"Bearer {config.api_key}",
        "Content-Type": "application/json",
    }

    response = requests.post(config.api_url, headers=headers, json=payload, timeout=config.timeout)

    # raise_for_status() turns a bad HTTP status (4xx/5xx) into a Python
    # exception immediately, instead of silently continuing with a
    # response body that doesn't have the shape we expect.
    response.raise_for_status()

    data = response.json()

    # The response wraps the model's reply in choices[0].message.content.
    # "choices" is plural because you can ask for multiple candidate
    # replies at once (we didn't, so there's exactly one).
    return data["choices"][0]["message"]["content"]

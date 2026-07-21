"""Stage 1 - Core LLM.

The goal here is to see exactly what an LLM API call looks like on the
wire, with nothing hiding it: no SDK, no framework. Just an HTTP POST
with a JSON body, and a JSON response we parse ourselves.

Groq exposes an "OpenAI-compatible" endpoint, meaning the request/response
shape follows the same convention OpenAI popularized (a `messages` list,
a `choices` list in the response, etc). Many providers copy this shape,
which is why you'll see it again in Stage 2+ regardless of which provider
we're calling.
"""

import os

import requests
from dotenv import load_dotenv

# load_dotenv() reads the .env file in the project root and copies its
# key=value pairs into os.environ, as if you'd `export`ed them yourself.
# It's a no-op if a variable is already set in the real environment.
load_dotenv()

# Groq's chat completion endpoint. "chat completion" is the API shape
# where you send a conversation (a list of role/content messages) and
# get back the model's next message.
GROQ_API_URL = "https://api.groq.com/openai/v1/chat/completions"

# Groq hosts open-weight models rather than one proprietary model.
# This one is small and fast - good for cheap experimentation.
MODEL = "llama-3.1-8b-instant"


def ask_llm(prompt: str) -> str:
    """Send a single user prompt to the LLM and return its text reply."""
    api_key = os.environ.get("GROQ_API_KEY")
    if not api_key:
        # Fail loudly and clearly rather than letting requests throw a
        # confusing 401 error further down.
        raise RuntimeError("GROQ_API_KEY is not set. Copy .env.example to .env and add your key.")

    # This is the request body every OpenAI-compatible chat API expects.
    # "messages" models a conversation: each entry has a role (who is
    # speaking: system/user/assistant) and content (what they said).
    # We only send one "user" message here, so there's no prior history.
    payload = {
        "model": MODEL,
        "messages": [
            {"role": "user", "content": prompt},
        ],
    }

    # Bearer token auth: the API key goes in the Authorization header,
    # not in the URL or body. This is standard for almost every LLM API.
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    }

    response = requests.post(GROQ_API_URL, headers=headers, json=payload, timeout=30)

    # raise_for_status() turns a bad HTTP status (4xx/5xx) into a Python
    # exception immediately, instead of silently continuing with a
    # response body that doesn't have the shape we expect.
    response.raise_for_status()

    data = response.json()

    # The response wraps the model's reply in choices[0].message.content.
    # "choices" is plural because you can ask for multiple candidate
    # replies at once (we didn't, so there's exactly one).
    return data["choices"][0]["message"]["content"]


def main():
    reply = ask_llm("In one sentence, what is a software engineering harness?")
    print(reply)


if __name__ == "__main__":
    main()

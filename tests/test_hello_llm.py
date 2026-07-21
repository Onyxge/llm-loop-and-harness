from unittest.mock import MagicMock, patch

import pytest

from src.hello_llm import ask_llm


def test_ask_llm_parses_response(monkeypatch):
    # Give the module something to read for the API key without
    # touching the real .env file.
    monkeypatch.setenv("GROQ_API_KEY", "fake-key-for-testing")

    # Build a fake response object shaped like the real Groq/OpenAI
    # response, so ask_llm's parsing code runs against realistic data.
    fake_response = MagicMock()
    fake_response.json.return_value = {
        "choices": [{"message": {"content": "a harness runs and grades your agent"}}]
    }
    fake_response.raise_for_status.return_value = None

    # patch() swaps out requests.post for the duration of this "with"
    # block, so no real network call happens.
    with patch("src.hello_llm.requests.post", return_value=fake_response) as mock_post:
        result = ask_llm("what is a harness?")

    assert result == "a harness runs and grades your agent"
    mock_post.assert_called_once()


def test_ask_llm_requires_api_key(monkeypatch):
    monkeypatch.delenv("GROQ_API_KEY", raising=False)

    with pytest.raises(RuntimeError):
        ask_llm("anything")

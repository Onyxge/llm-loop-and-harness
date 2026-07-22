from unittest.mock import patch

from src.code_reviewer import build_review_prompt, review_code


def test_build_review_prompt_inserts_code():
    prompt = build_review_prompt("def foo():\n    pass\n")

    assert "def foo():" in prompt
    assert "{{CODE}}" not in prompt


def test_build_review_prompt_handles_braces_in_code():
    # This is exactly the case str.format() would choke on: real code
    # containing literal curly braces (a dict literal here).
    code = 'config = {"key": "value"}'
    prompt = build_review_prompt(code)

    assert code in prompt


def test_review_code_sends_built_prompt_to_ask_llm():
    with patch("src.code_reviewer.ask_llm", return_value="looks fine") as mock_ask:
        result = review_code("x = 1")

    assert result == "looks fine"
    sent_prompt = mock_ask.call_args[0][0]
    assert "x = 1" in sent_prompt

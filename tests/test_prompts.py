import pytest

from src.prompts import list_versions, load_prompt


def test_list_versions_finds_all_three():
    assert list_versions("harness_explainer") == ["v1", "v2", "v3"]


def test_load_prompt_returns_file_contents():
    prompt = load_prompt("harness_explainer", "v1")
    assert "harness" in prompt.lower()


def test_load_prompt_missing_version_raises():
    with pytest.raises(FileNotFoundError):
        load_prompt("harness_explainer", "v99")

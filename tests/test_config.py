from src.config import get_config


def test_get_config_defaults(monkeypatch):
    monkeypatch.delenv("GROQ_MODEL", raising=False)
    monkeypatch.delenv("GROQ_TEMPERATURE", raising=False)
    monkeypatch.delenv("GROQ_TIMEOUT", raising=False)

    config = get_config()

    assert config.model == "llama-3.1-8b-instant"
    assert config.temperature == 0.7
    assert config.timeout == 30


def test_get_config_reads_overrides_from_env(monkeypatch):
    monkeypatch.setenv("GROQ_MODEL", "llama-3.3-70b-versatile")
    monkeypatch.setenv("GROQ_TEMPERATURE", "0.2")
    monkeypatch.setenv("GROQ_TIMEOUT", "10")

    config = get_config()

    assert config.model == "llama-3.3-70b-versatile"
    assert config.temperature == 0.2
    assert config.timeout == 10

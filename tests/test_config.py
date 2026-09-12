from src.config import (
    DEFAULT_CONFIG,
    get_config_value,
    merge_config,

    validate_config,)


def test_default_timeout():
    assert DEFAULT_CONFIG["timeout"] == 30


def test_default_debug():
    assert DEFAULT_CONFIG["debug"] is False


def test_default_environment():
    assert DEFAULT_CONFIG["environment"] == "development"


def test_get_timeout():
    assert get_config_value("timeout") == 30


def test_get_debug():
    assert get_config_value("debug") is False


def test_get_environment():
    assert get_config_value("environment") == "development"


def test_merge_config():
    result = merge_config(
        {"timeout": 60}
    )

    assert result["timeout"] == 60

def test_feature_enabled_config():
    assert get_config_value("feature_enabled") is False

def test_database_timeout_config():
    assert (
        get_config_value("database_timeout")
        == 10
    )

def test_validate_config():
    assert validate_config(DEFAULT_CONFIG) is True

    invalid = DEFAULT_CONFIG.copy()
    invalid["timeout"] = -1

    assert validate_config(invalid) is False

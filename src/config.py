"""Config utilities."""


DEFAULT_CONFIG = {
    "database_timeout": 10,
    "feature_enabled": False,
    "debug": False,
    "timeout": 30,
    "max_retries": 3,
    "environment": "development",
}


def get_config_value(key: str):
    return DEFAULT_CONFIG.get(key)


def merge_config(overrides: dict) -> dict:
    config = DEFAULT_CONFIG.copy()
    config.update(overrides)
    return config
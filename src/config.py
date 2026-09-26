"""Configuration defaults and helper functions."""


DEFAULT_CONFIG = {
    "cache_enabled": True,
    "region": "local",
    "request_timeout": 15,
    "database_timeout": 10,
    "feature_enabled": False,
    "debug": False,
    "timeout": 30,
    "max_retries": 3,
    "environment": "development",
}


def get_config_value(key: str):
    """Return a configuration value by key."""
    return DEFAULT_CONFIG.get(key)


def merge_config(overrides: dict) -> dict:
    config = DEFAULT_CONFIG.copy()
    config.update(overrides)
    return config

def validate_config(config: dict) -> bool:
    if not isinstance(config.get("debug"), bool):
        return False

    if not isinstance(config.get("timeout"), int):
        return False

    if config["timeout"] < 0:
        return False

    if not isinstance(config.get("max_retries"), int):
        return False

    if config["max_retries"] < 0:
        return False

    if not isinstance(
        config.get("environment"),
        str,
    ):
        return False

    return True

def build_config() -> dict:
    return DEFAULT_CONFIG.copy()

def get_required_config(key: str):
    if key not in DEFAULT_CONFIG:
        raise KeyError(
            f"Missing required configuration: {key}"
        )

    return DEFAULT_CONFIG[key]

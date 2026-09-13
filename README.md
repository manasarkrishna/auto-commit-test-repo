# Automation Test Project

A small Python utility project used for testing the autonomous Git development system.

## Features

- Calculator utilities
- Text processing utilities
- Input validation
- Configuration management

## Running Tests

```bash
python -m pytest
```

## Configuration

Configuration values are defined in `src/config.py`.

The default configuration includes (example):

- debug
- timeout
- max_retries
- environment

Use `get_config_value()` to retrieve a configuration value and `merge_config()` to apply overrides.

## Text Utilities Examples

Text helpers are available from `src.text_utils`:

```python
from src.text_utils import (
    normalize_text,
    reverse_text,
    word_count,
)

normalize_text("  Hello   World  ")
reverse_text("hello")
word_count("one two three")
```

## Validator Examples

Validation helpers are available from `src.validator`:

```python
from src.validator import (
    is_valid_email,
    is_valid_age,
    is_valid_username,
)

is_valid_email("user@example.com")
is_valid_age(25)
is_valid_username("developer")
```

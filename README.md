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

## Usage

Import the project helpers from the `src` package and call the
functions that match the operation you need.

## Error Handling

Helpers raise standard Python exceptions when an operation cannot
be completed with the supplied input. Callers should validate
inputs and handle expected exceptions where appropriate.

## Contributing

Before submitting changes:

- Make the required code or documentation change.
- Add or update tests when appropriate.
- Run the complete test suite.
- Review the changes with Git.
- Commit the changes with a clear commit message.

## Testing

Run the complete test suite with:

```bash
python -m pytest
```

The tests cover the calculator, text utilities, validators, configuration utilities, and file utilities.

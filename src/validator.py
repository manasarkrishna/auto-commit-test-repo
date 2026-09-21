"""Validation helpers for common input checks."""

import re


def is_valid_email(email: str) -> bool:
    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"
    return re.match(pattern, email) is not None


def is_valid_age(age: int) -> bool:
    return 0 <= age <= 120


def is_non_empty_string(value: str) -> bool:
    return bool(value.strip())


def is_valid_username(username: str) -> bool:
    return username.isalnum() and len(username) >= 3


PHONE_NUMBER_LENGTH = 10


def is_valid_phone(phone: str) -> bool:
    digits = phone.replace("-", "").replace(" ", "")
    return (
        digits.isdigit()
        and len(digits) == PHONE_NUMBER_LENGTH
    )


def has_valid_password_length(password: str) -> bool:
    return len(password) >= 8
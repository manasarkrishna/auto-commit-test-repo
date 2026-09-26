from src.validator import (
    is_valid_email,
    is_valid_age,
    is_non_empty_string,
    is_valid_username,
    is_valid_phone,
    has_valid_password_length,
)


def test_valid_email():
    assert is_valid_email("user@example.com")


def test_invalid_email():
    assert not is_valid_email("invalid")


def test_valid_age():
    assert is_valid_age(25)


def test_invalid_age():
    assert not is_valid_age(150)


def test_non_empty_string():
    assert is_non_empty_string("hello")

def test_valid_username():
    assert is_valid_username("john123")


def test_invalid_short_username():
    assert not is_valid_username("ab")


def test_invalid_username_with_symbols():
    assert not is_valid_username("john@123")


def test_valid_phone():
    assert is_valid_phone("9876543210")


def test_valid_phone_with_formatting():
    assert is_valid_phone("987-654-3210")


def test_invalid_phone():
    assert not is_valid_phone("12345")


def test_valid_password_length():
    assert has_valid_password_length("password123")


def test_invalid_short_password():
    assert not has_valid_password_length("pass")

def test_phone_invalid_length():
    assert is_valid_phone("123456789") is False
    assert is_valid_phone("12345678901") is False

def test_username_empty():
    from src.validator import is_valid_username

    assert is_valid_username("") is False

def test_email_missing_at_symbol():
    from src.validator import is_valid_email

    assert is_valid_email("user.example.com") is False

def test_password_short_value():
    from src.validator import has_valid_password_length

    assert has_valid_password_length("short") is False

def test_email_missing_domain():
    from src.validator import is_valid_email

    assert is_valid_email("user@") is False

def test_username_rejects_special_characters():
    assert is_valid_username("user_name") is False
    assert is_valid_username("user-name") is False

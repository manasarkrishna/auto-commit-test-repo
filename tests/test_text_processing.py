from src.text_utils import (
    normalize_text,
    reverse_text,
    word_count,
    uppercase_text,
    character_count,
    contains_word,
)

def test_contains_word_empty_word():
    assert contains_word(
        "hello world",
        "",
    ) is False

def test_uppercase_text_empty_string():
    assert uppercase_text("") == ""

def test_contains_word_is_case_sensitive():
    assert contains_word(
        "Hello world",
        "hello",
    ) is False

def test_reverse_text_unicode():
    assert reverse_text("café") == "éfac"

def test_normalize_text_preserves_punctuation():
    assert normalize_text(
        "  Hello,   World!  "
    ) == "hello, world!"

def test_reverse_text_empty_string():
    assert reverse_text("") == ""

def test_reverse_text_single_character():
    assert reverse_text("x") == "x"

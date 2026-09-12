NORMALIZED_SEPARATOR = " "


def normalize_text(text: str) -> str:
    return NORMALIZED_SEPARATOR.join(text.strip().lower().split())


def reverse_text(text: str) -> str:
    return text[::-1]


def word_count(text: str) -> int:
    return len(text.split())


def uppercase_text(text: str) -> str:
    return text.upper()


def character_count(text: str) -> int:
    return len(text)


def contains_word(text: str, word: str) -> bool:
    return word in text.split()
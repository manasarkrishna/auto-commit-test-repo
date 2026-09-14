"""Utilities for common file operations."""

from pathlib import Path


def file_exists(path: str) -> bool:
    return Path(path).is_file()


def read_text_file(path: str) -> str:
    return Path(path).read_text(encoding="utf-8")


def write_text_file(path: str, content: str) -> None:
    Path(path).write_text(content, encoding="utf-8")


def get_file_size(path: str) -> int:
    return Path(path).stat().st_size


def get_file_extension(path: str) -> str:
    return Path(path).suffix


def safe_read_text_file(path: str, default: str = "") -> str:
    file = Path(path)

    if not file.is_file():
        return default

    return file.read_text(encoding="utf-8")


def get_file_name(path: str) -> str:
    return Path(path).name

def get_file_size_mb(path: str) -> float:
    return get_file_size(path) / (1024 * 1024)

def get_file_stem(path: str) -> str:
    return Path(path).stem

def get_absolute_path(path: str) -> str:
    return str(Path(path).resolve())

def append_text_file(path: str, content: str) -> None:
    with Path(path).open(
        "a",
        encoding="utf-8",
    ) as file:
        file.write(content)

def read_text_lines(path: str) -> list[str]:
    return Path(path).read_text(
        encoding="utf-8"
    ).splitlines()

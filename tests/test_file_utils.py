from src.file_utils import (
    file_exists,
    read_text_file,
    write_text_file,
    get_file_size,
    get_file_size_mb,
    get_file_stem,
    get_absolute_path,
    append_text_file,
)


def test_file_exists(tmp_path):
    file = tmp_path / "example.txt"
    file.write_text("hello", encoding="utf-8")

    assert file_exists(str(file))


def test_file_does_not_exist(tmp_path):
    file = tmp_path / "missing.txt"

    assert not file_exists(str(file))


def test_read_text_file(tmp_path):
    file = tmp_path / "example.txt"
    file.write_text("hello", encoding="utf-8")

    assert read_text_file(str(file)) == "hello"


def test_write_text_file(tmp_path):
    file = tmp_path / "example.txt"

    write_text_file(str(file), "hello")

    assert file.read_text(encoding="utf-8") == "hello"


def test_get_file_size(tmp_path):
    file = tmp_path / "example.txt"
    file.write_text("hello", encoding="utf-8")

    assert get_file_size(str(file)) == 5

def test_get_file_size_mb(tmp_path):
    file = tmp_path / "data.bin"

    file.write_bytes(
        b"a" * (1024 * 1024)
    )

    assert get_file_size_mb(
        str(file)
    ) == 1.0

def test_get_file_stem():
    assert get_file_stem("reports/data.csv") == "data"
    assert get_file_stem("README") == "README"

def test_get_absolute_path():
    from pathlib import Path

    result = get_absolute_path("example.txt")
    assert Path(result).is_absolute()

def test_append_text_file(tmp_path):
    file = tmp_path / "append.txt"

    file.write_text(
        "hello",
        encoding="utf-8",
    )

    append_text_file(
        str(file),
        " world",
    )

    assert file.read_text(
        encoding="utf-8"
    ) == "hello world"

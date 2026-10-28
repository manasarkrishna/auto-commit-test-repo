import pytest

from src.calculator import (
    add,
    subtract,
    multiply,
    divide,
    power,
    absolute,
    percentage,
)


def test_add():
    assert add(2, 3) == 5


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(4, 3) == 12


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(10, 0)


def test_power():
    assert power(2, 3) == 8


def test_power_zero_exponent():
    assert power(10, 0) == 1


def test_power_negative_exponent():
    assert power(2, -2) == 0.25


def test_absolute_positive():
    assert absolute(5) == 5


def test_absolute_negative():
    assert absolute(-5) == 5


def test_absolute_zero():
    assert absolute(0) == 0


def test_percentage():
    assert percentage(200, 10) == 20


def test_percentage_zero():
    assert percentage(200, 0) == 0


def test_percentage_hundred():
    assert percentage(200, 100) == 200

def test_absolute_with_zero():
    assert absolute(0) == 0

def test_multiply_by_zero():
    from src.calculator import multiply

    assert multiply(123, 0) == 0

def test_percentage_fraction():
    assert percentage(80, 12.5) == 10

def test_divide_by_zero_raises():
    import pytest
    from src.calculator import divide

    with pytest.raises(ValueError):
        divide(10, 0)

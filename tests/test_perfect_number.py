import pytest

from daily_coding_problems.perfect_number import perfect_number


def test_perfect_number_1():
    result = perfect_number(1)
    assert result == 19


def test_perfect_number_2():
    result = perfect_number(2)
    assert result == 28


def test_perfect_number_fails():
    perfect_number(91)
    with pytest.raises(Exception):
        perfect_number(92)

from daily_coding_problems.largest_product import get_largest_product
import pytest

def test_largest_product_1():
    result = get_largest_product([-10, -10, -20, 4, 2])
    assert -20 * -10 * 4 == result

def test_largest_product_2():
    result = get_largest_product([-10, -10, 5, 2])
    assert result == 500

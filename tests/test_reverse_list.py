from daily_coding_problems.ordered_matrix import order_matrix_columns


def test_order_matrix_columns():
    matrix = [
        ["a", "b", "c"],
        ["a", "b", "c"],
        ["a", "b", "c"],
    ]
    assert order_matrix_columns(matrix) == 0


def test_order_matrix_columns_1():
    matrix = [
        ["b", "b", "c"],
        ["a", "b", "c"],
        ["a", "b", "c"],
    ]
    assert order_matrix_columns(matrix) == 1


def test_order_matrix_columns_2():
    matrix = [
        ["b", "c", "c"],
        ["a", "b", "c"],
        ["a", "b", "c"],
    ]
    assert order_matrix_columns(matrix) == 2


def test_order_matrix_columns_3():
    matrix = [
        ["b", "c", "d"],
        ["a", "b", "c"],
        ["a", "b", "c"],
    ]
    assert order_matrix_columns(matrix) == 3

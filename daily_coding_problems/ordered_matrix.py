"""
You are given an N by M 2D matrix of lowercase letters.
Determine the minimum number of columns that can be removed to ensure that each row is ordered
from top to bottom lexicographically.
That is, the letter at each column is lexicographically later as you go down each row.
It does not matter whether each row itself is ordered lexicographically.
"""


def order_matrix_columns(matrix: list[list[chr]]):
    prev = None
    out_of_order_columns = 0
    for j in range(len(matrix[0])):
        current = None
        for i in range(len(matrix[j])):
            prev = current
            current = matrix[i][j]
            print(current)
            if prev is not None and current < prev:
                print(f"column {j} is out of order")
                out_of_order_columns += 1
    return out_of_order_columns

# Suppose you have a multiplication table that is N by N. That is, a 2D array where the value at the i-th row and j-th column is (i + 1) * (j + 1) (if 0-indexed) or i * j (if 1-indexed).

# Given integers N and X, write a function that returns the number of times X appears as a value in an N by N multiplication table.

def brute_force_occurrence(multiplier: int, occurs: int):
    result = 0
    for i in range(1, multiplier + 1):
        for j in range(1, multiplier + 1):
            if i * j == occurs:
                result += 1
    return result

def divisors_occurrence(multiplier: int, occurs: int):
    result = 0
    for i in range(1, multiplier + 1):
        if occurs % i == 0 and int(occurs / i) <= multiplier:
            result += 1
    return result

            

        

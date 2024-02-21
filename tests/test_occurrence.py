from daily_coding_problems.occurrence_in_multiplication_table import brute_force_occurrence, divisors_occurrence
import time


def test_occurrence_brute():
    assert brute_force_occurrence(6,12) == 4
    assert brute_force_occurrence(50, 100) == 7
    now = time.time()
    assert brute_force_occurrence(100000, 10) == 4
    later = time.time()
    print(later - now)
    assert False

def test_occurrence():
    assert divisors_occurrence(6, 12) == 4
    assert divisors_occurrence(50, 100) == 7
    now = time.time()
    assert divisors_occurrence(100000, 10) == 4
    later = time.time()
    print(later - now)
    assert False
    

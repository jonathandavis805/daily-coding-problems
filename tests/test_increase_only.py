from daily_coding_problems.increase_only import one_change_increasing_only


def test_increase_only_sorted():
    sorted_list = [1, 2, 3]
    assert one_change_increasing_only(sorted_list)

def test_increase_only():
    swap_1 = [1, 2, 3, 2]
    assert one_change_increasing_only(swap_1)

def test_increase_only_2():
    swap_2 = [1, 2, 4, 1]
    assert not one_change_increasing_only(swap_2)

def test_increase_only_1_weird():
    swap_1_weird = [1, 2, 4, 3, 2]
    assert one_change_increasing_only(swap_1_weird)

def test_increase_only_2_weird():
    swap_2_weird = [1, 2, 4, 3, 2, 3]
    assert not one_change_increasing_only(swap_2_weird)
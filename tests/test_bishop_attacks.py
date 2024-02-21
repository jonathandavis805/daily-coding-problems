from daily_coding_problems.bishops import attack_count


def test_attack_count_2():
    bishops = [(0, 0), (1, 2), (2, 2), (4, 0)]
    assert attack_count(5, bishops) == 2


def test_attack_count_3():
    bishops = [(0, 0), (1, 1), (2, 2)]
    assert attack_count(5, bishops) == 3

from daily_coding_problems.bishops import attack_count

def test_attack_count():
    bishops = [(0,0), (1,2), (2,2), (4,0)]
    board_size = 5
    assert attack_count(5, bishops) == 2


def test_attack_count():
    bishops = [(0,0), (1,1), (2,2)]
    board_size = 3
    assert attack_count(5, bishops) == 3

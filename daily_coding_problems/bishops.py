# On our special chessboard, two bishops attack each other if they share the same diagonal. 
# This includes bishops that have another bishop located between them, i.e. bishops can attack through pieces.
# You are given N bishops, represented as (row, column) tuples on a M by M chessboard. 
# Write a function to count the number of pairs of bishops that attack each other. 
# The ordering of the pair doesn't matter: (1, 2) is considered the same as (2, 1).
# For example, given M = 5 and the list of bishops:
# (0, 0)
# (1, 2)
# (2, 2)
# (4, 0)
# The board would look like this:
# [b 0 0 0 0]
# [0 0 b 0 0]
# [0 0 b 0 0]
# [0 0 0 0 0]
# [b 0 0 0 0]
# You should return 2, since bishops 1 and 3 attack each other, as well as bishops 3 and 4.


def attack_count(board_size: int, bishops: list[tuple[int, int]]):
    arr = []
    attack_counter = 0
    for _ in range(board_size):
        row = []
        for _ in range(board_size):
            row.append("O")
        arr.append(row)
    for bishop in bishops:
        arr[bishop[0]][bishop[1]] = "b"
        i = bishop[0]
        j = bishop[1]
        # positive
        while i < board_size and j < board_size:
            i += 1
            j += 1
            for other_bishop in bishops:
                if other_bishop[0] == i and other_bishop[1] == j:
                    attack_counter += 1
        i = bishop[0]
        j = bishop[1]
        # negative
        while i < board_size and j > 0:
            i += 1
            j -= 1
            for other_bishop in bishops:
                if other_bishop[0] == i and other_bishop[1] == j:
                    attack_counter += 1

    for row in arr:
        print(f"{row}")
    return attack_counter

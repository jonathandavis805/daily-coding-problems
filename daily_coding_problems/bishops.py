def attack_count(board_size: int, bishops: list[tuple[int,int]]):
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

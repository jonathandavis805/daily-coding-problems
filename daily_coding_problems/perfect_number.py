def perfect_number(input: int, sum: int = 10):
    str_int = str(input)
    print(f"input: {str_int}")
    acc = 0
    for str_digit in str_int:
        print(f"digit: {str_digit}")
        acc += int(str_digit)
    print(acc)
    if acc < sum:
        print("possible")
        return int(str_int + str(sum - acc))
    elif acc == sum:
        return input
    else:
        raise Exception("solution not possible")
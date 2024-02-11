# A number is considered perfect if its digits sum up to exactly 10.
# Given a positive integer n, return the n-th perfect number.
# For example, given 1, you should return 19. Given 2, you should return 28.

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
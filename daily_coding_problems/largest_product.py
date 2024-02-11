# Given a list of integers, return the largest product that can be made by multiplying any three integers.
# For example, if the list is [-10, -10, 5, 2], we should return 500, since that's -10 * -10 * 5.
# You can assume the list has at least three integers.
def get_largest_product(arr: list[int]):
    arr.sort(reverse=True)
    print(arr)
    if abs(arr[-1]) + abs(arr[-2]) > sum(arr[:1]):
        return arr[0] * arr[-1] * arr[-2]
    else:
        return arr[0] * arr[1] * arr[2]

def get_largest_product(arr: list[int]):
    arr.sort(reverse=True)
    print(arr)
    if abs(arr[-1]) + abs(arr[-2]) > sum(arr[:1]):
        return arr[0] * arr[-1] * arr[-2]
    else:
        return arr[0] * arr[1] * arr[2]

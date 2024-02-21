# Given an array of integers, write a function to determine whether the array could become non-decreasing by modifying at most 1 element.
# For example, given the array [10, 5, 7], you should return true, since we can modify the 10 into a 1 to make the array non-decreasing.
# Given the array [10, 5, 1], you should return false, since we can't modify any one element to get a non-decreasing array.

def one_change_increasing_only(arr: list[int]) -> bool:
    prev = arr[0]
    swap_index = [None, None]
    for i in range(1, len(arr)):
        item = arr[i]
        if prev > item:
            print(f"index {i}")
            swap_index[0] = i - 1
            swap_index[1] = i
            current = item
            for j in range(i, len(arr)):
                print(arr[j])
                print(current)
                if arr[j] < current:
                    swap_index[1] = j
                current = arr[j]
            break
        prev = item
    print(arr)
    print(swap_index)
    if swap_index[0] is None:
        return True
    else:
        temp = arr[swap_index[0]]
        arr[swap_index[0]] = arr[swap_index[1]]
        arr[swap_index[1]] = temp
        print(arr)
        prev = arr[0] 
        for item in arr[1:]:
            if prev > item:
                return False
            prev = item
        return True



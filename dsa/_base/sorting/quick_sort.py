def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)


array = [1, 5, 90, 56, 0, 34, 2, 3, 7]
assert quick_sort(array), [0, 1, 2, 3, 5, 7, 34, 56, 90]
print("OK")

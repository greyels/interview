def bubble_sort(arr):
    n = len(arr)
    swapped = False
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            return arr
    return arr


array = [1, 5, 90, 56, 0, 34, 2, 3, 7]
assert bubble_sort(array), [0, 1, 2, 3, 5, 7, 34, 56, 90]
print("OK")

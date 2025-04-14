def selection_sort(arr):
    size = len(arr)
    for i in range(size - 1):
        min_index = i
        for j in range(i + 1, size):
            # select the minimum element in every iteration
            if arr[j] < arr[min_index]:
                min_index = j
            # swapping the elements to sort the array
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


array = [1, 5, 90, 56, 0, 34, 2, 3, 7]
assert selection_sort(array), [0, 1, 2, 3, 5, 7, 34, 56, 90]
print("OK")

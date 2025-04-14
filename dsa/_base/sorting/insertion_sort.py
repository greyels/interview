def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        # Shift larger elements to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Insert key in its correct place

# Example
array = [1, 5, 90, 56, 0, 34, 2, 3, 7]
insertion_sort(array)
assert array, [0, 1, 2, 3, 5, 7, 34, 56, 90]
print("OK")

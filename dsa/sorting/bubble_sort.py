def bubble_sort(arr):
    for i in range(len(arr) - 1):
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

array = [1, 5, 90, 56, 0, 34, 2, 3, 7]
print(bubble_sort(array))

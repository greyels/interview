# In-place sorting
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                print(arr)
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


arr = [1, 5, 90, 56, 0, 34, 2, 3, 7]
bubble_sort(arr)
assert arr, [0, 1, 2, 3, 5, 7, 34, 56, 90]
print("OK")

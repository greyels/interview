def quick_sort(arr):
    less = []
    equal = []
    greater = []
    if len(arr) <= 1:
        return arr
    pivot = arr[0]
    for i in arr:
        if i < pivot:
            less.append(i)
        elif i == pivot:
            equal.append(i)
        elif i > pivot:
            greater.append(i)
    return quick_sort(less) + equal + quick_sort(greater)


array = [1, 5, 90, 56, 0, 34, 2, 3, 7]
assert quick_sort(array), [0, 1, 2, 3, 5, 7, 34, 56, 90]
print("OK")

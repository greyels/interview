# recursive solution
def binary_search_rec(arr, left, right, item):
    if right >= left:
        mid = (right + left) // 2
        if arr[mid] == item:
            return mid
        elif arr[mid] > item:
            return binary_search_rec(arr, left, mid - 1, item)
        elif arr[mid] < item:
            return binary_search_rec(arr, mid + 1, right, item)
    else:
        return


# iterative solution
def binary_search_iter(arr, item):
    left = 0
    right = len(arr) - 1
    while right >= left:
        mid = (right + left) // 2
        if arr[mid] == item:
            return mid
        elif arr[mid] < item:
            left = mid + 1
        elif arr[mid] > item:
            right = mid - 1
    return


array = [1, 3, 5, 6, 9, 99, 1987]
my_item = 5

assert binary_search_iter(array, my_item), 2
assert binary_search_rec(array, 0, len(array) - 1, my_item), 2
print("OK")

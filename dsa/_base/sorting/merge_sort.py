def merge_sort(arr):
    def merge(left, right):
        result, i, j = [], 0, 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        return result + left[i:] + right[j:]

    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)


arr = [38, 27, 43, 3, 9, 82, 10]
assert merge_sort(arr), [3, 9, 10, 27, 38, 43, 82]
print("OK")

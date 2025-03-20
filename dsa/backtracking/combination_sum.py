def combinationSum(candidates, target):
    def backtrack(start, path):
        total = sum(path)
        print(f"current path = {path} with total = {total}")
        if total == target:
            result.append(path[:])  # Create a shallow copy of the path
            print("total = target then add path to result and return")
            return
        if total > target:
            print("total > target then return")
            return

        for i in range(start, len(candidates)):
            path.append(candidates[i])
            backtrack(i, path)  # Allow repeated numbers
            path.pop()  # Backtrack

    result = []
    backtrack(0, [])
    return result

# Example Usage:
candidates = [2, 3, 6, 7]
target = 7
print(combinationSum(candidates, target))


# Start
#  ├── 2 (sum = 2)
#  │   ├── 2 (sum = 4)
#  │   │   ├── 2 (sum = 6)
#  │   │   │   ├── 2 (sum = 8) ✗ (backtrack)
#  │   │   │   ├── 3 (sum = 9) ✗ (backtrack)
#  │   │   │   ├── 6 (sum > 7) ✗ (backtrack)
#  │   │   │   ├── 7 (sum > 7) ✗ (backtrack)
#  │   │   ├── 3 (sum = 7) ✔ (valid solution [2,2,3])
#  │   │   ├── 6 ✗
#  │   │   ├── 7 ✗
#  │   ├── 3 (sum = 5)
#  │   ├── 6 ✗
#  │   ├── 7 ✔ (valid solution [7])
#  ├── 3
#  ├── 6
#  ├── 7

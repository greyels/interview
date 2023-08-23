from typing import List


# Solution
# 1) Brute force -> double loop O(n^2)
# 2) Solution with hash map (set, dict)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_map = dict()
        for idx, value in enumerate(nums):
            if target - value in hash_map:
                return [idx, hash_map[target - value]]
            else:
                hash_map[value] = idx


nums = [1, 2, 5, 89, 10, 45]
target = 90
expected = [0, 3]
result = Solution().twoSum(nums, target)

assert sorted(result) == expected, f"Expected {expected}, but got {result}"

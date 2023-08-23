from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if len(nums) == 0:
            return 0
        k = i = 0
        while i <= len(nums)-1:
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
                k += 1
        return k


nums = [0, 1, 2, 2, 3, 0, 4, 2]
val = 2
k = Solution().removeElement(nums, val)
print(k)
print(nums)

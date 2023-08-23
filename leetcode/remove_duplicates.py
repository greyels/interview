from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) <= 2:
            return len(nums)
        slow = 0
        second = False
        for fast in range(1, len(nums)):
            print(slow, fast, nums[slow], nums[fast])
            if nums[slow] == nums[fast]:
                if second is False:
                    nums[slow+1] = nums[fast]
                    second = True
                    slow += 1
            else:
                nums[slow+1] = nums[fast]
                second = False
                slow += 1
            fast += 1
        return slow + 1

nums = [1,2,2]

Solution().removeDuplicates(nums)
print(nums)

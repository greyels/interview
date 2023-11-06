from typing import List


class Solution:
    # Dynamic programming
    def maxSubArrayDP(self, nums):
        cur_sum, max_sum = 0, -float('inf')
        for num in nums:
            cur_sum += num
            max_sum = max(cur_sum, max_sum)
            if cur_sum < 0:
                cur_sum = 0
        return max_sum

    def maxSubArray2(self, nums: List[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i - 1] + nums[i], nums[i])
        return max(nums)


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
assert Solution().maxSubArrayDP(nums) == 6
assert Solution().maxSubArray2(nums) == 6
print("OK")

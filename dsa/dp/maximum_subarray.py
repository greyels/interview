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

    # Divide and conquer
    def maxSubArrayDC(self, nums):


nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
assert Solution().maxSubArrayDP(nums), 6
assert Solution().maxSubArrayDC(nums), 6
print("OK")

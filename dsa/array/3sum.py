from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums = sorted(nums)
        result = []
        for i in range(len(nums) - 2):
            if nums[i] > 0:
                break
            if i > 0 and (nums[i] == nums[i - 1]):
                continue
            l, r = i + 1, len(nums) - 1
            while l < r:
                sum = nums[l] + nums[r] + nums[i]
                if sum == 0:
                    result.append([nums[i], nums[l], nums[r]])
                    l += 1
                    while nums[l - 1] == nums[l] and l < r:
                        l += 1
                elif sum > 0:
                    r -= 1
                else:
                    l += 1
        return result


nums = [-1, 0, 1, 2, -1, -4]
assert Solution().threeSum(nums) == [[-1, -1, 2], [-1, 0, 1]]
print("OK")

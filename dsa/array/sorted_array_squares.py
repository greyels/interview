from typing import List


class Solution1:
    @staticmethod
    def sorted_squares(nums: List[int]) -> List[int]:
        result = [0 for i in range(len(nums))]
        left = 0
        right = index = len(nums) - 1
        while index >= 0:
            if abs(nums[left]) >= abs(nums[right]):
                result[index] = nums[left] * nums[left]
                left += 1
            else:
                result[index] = nums[right] * nums[right]
                right -= 1
            index -= 1
        return result


# Insert is very slow!
class Solution2:
    @staticmethod
    def sorted_squares(nums: List[int]) -> List[int]:
        result = []
        left = 0
        right = index = len(nums) - 1
        while index >= 0:
            if abs(nums[left]) >= abs(nums[right]):
                result.insert(0, nums[left] * nums[left])
                left += 1
            else:
                result.insert(0, nums[right] * nums[right])
                right -= 1
            index -= 1
        return result

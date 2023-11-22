from typing import List
# Should be O(n) and division could not be used

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        length = len(nums)
        result = [0] * length
        # product[i] = prefix[i-1] * postfix[i+1]
        prefix = 1
        postfix = 1
        # calculating prefixes and put them in the result array
        for i in range(length):
            result[i] = prefix
            prefix *= nums[i]
        # calculating postfixes and multiply with prefixes
        for i in range(length - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        return result

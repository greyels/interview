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

    def productExceptSelf2(self, nums: List[int]) -> List[int]:
        prefix, postfix = [0] * len(nums), [0] * len(nums)
        prefix[0], postfix[-1] = nums[0], nums[-1]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i-1] * nums[i]
        for i in range(len(nums)-2, 0, -1):
            postfix[i] = postfix[i+1] * nums[i]

        answer = [0] * len(nums)
        answer[0], answer[-1] = postfix[1], prefix[-2]
        for i in range(1, len(nums)-1):
            answer[i] = prefix[i-1] * postfix[i+1]

        return answer

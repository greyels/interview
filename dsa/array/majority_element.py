from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counter = dict()
        for elem in nums:
            if elem not in counter:
                counter[elem] = 1
            else:
                counter[elem] += 1
        return max(counter, key=counter.get)

    def majorityElementOptSpace(self, nums: List[int]) -> int:
        major = nums[0]
        counter = 1
        for idx in range(1, len(nums)):
            if counter == 0:
                major = nums[idx]
                counter += 1
            elif nums[idx] == major:
                counter += 1
            else:
                counter -= 1
        return major

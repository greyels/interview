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

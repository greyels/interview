# https://leetcode.com/problems/longest-consecutive-sequence/
from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash = set(nums)
        longest = 0
        for num in hash:
            if num - 1 not in hash:
                cur_l = 1
                while num + cur_l in hash:
                    cur_l = cur_l + 1
                longest = max(longest, cur_l)
        return longest

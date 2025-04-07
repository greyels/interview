# https://leetcode.com/problems/container-with-most-water
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        left, right = 0, len(height) - 1
        while right > left:
            cur_water = min(height[left], height[right]) * (right - left)
            if cur_water > max_water:
                max_water = cur_water
            if height[right] >= height[left]:
                left += 1
            else:
                right -= 1
        return max_water

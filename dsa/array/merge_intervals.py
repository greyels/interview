from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals or len(intervals) == 1:
            return intervals

        intervals = sorted(intervals, key=lambda x: x[0])
        res = []

        for int in intervals:
            if not res or res[-1][1] < int[0]:
                res.append(int)
            else:
                res[-1][1] = max(res[-1][1], int[1])
        return res

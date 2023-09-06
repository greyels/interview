from typing import List


class Solution:
    def insert(self, intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
        result = []
        for int in intervals:
            if int[1] < new_interval[0]:
                result.append(int)
            elif int[0] > new_interval[1]:
                result.append(new_interval)
                new_interval = int
            elif new_interval[0] <= int[1] or new_interval[1] >= int[0]:
                new_interval[0] = min(new_interval[0], int[0])
                new_interval[1] = max(new_interval[1], int[1])
        result.append(new_interval)
        return result


# Input:
intervals = [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]]
newInterval = [4, 8]
assert Solution().insert(intervals, newInterval) == [[1, 2], [3, 10], [12, 16]]
print("OK")

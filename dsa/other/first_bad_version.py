# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        if n == 1:
            return 1
        if isBadVersion(1) is True:
            return 1
        if n == 2:
            return 2
        start = 1
        end = n
        while end >= start:
            mid = (start + end) // 2
            if isBadVersion(mid) is False:
                start = mid + 1
                if isBadVersion(start) is True:
                    return start
            else:
                end = mid - 1
                if isBadVersion(end) is False:
                    return mid
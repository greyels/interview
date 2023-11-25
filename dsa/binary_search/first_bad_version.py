# The isBadVersion API is already defined for you.
def isBadVersion(version: int) -> bool:
    pass

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n
        while right >= left:
            mid = (right + left) // 2
            if isBadVersion(mid):
                if not isBadVersion(mid-1):
                    return mid
                right = mid - 1
            else:
                left = mid + 1

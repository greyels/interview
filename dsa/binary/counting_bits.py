from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(1, n + 1):
            sum = 0
            for j in "{0:b}".format(i):
                sum += int(j)
            res[i] = sum
        return res

    def countBitsFast(self, n: int) -> List[int]:
        if not n:
            return [0]
        res = [0] * (n + 1)
        for i in range(1, n + 1):
            res[i] = res[i // 2] + i % 2
        return res

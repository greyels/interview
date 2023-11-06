class Solution:
    def hammingWeight(self, n: int) -> int:
        counter = 0
        for b in "{0:b}".format(n):
            if b == "1":
                counter += 1
        return counter

    def hammingWeightBitwise(self, n: int) -> int:
        count = 0
        while n:
            if n & 1: count += 1
            n = n >> 1
        return count

class Solution:
    def romanToInt(self, s: str) -> int:
        num_map = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        result = prev = num_map[s[-1]]
        for idx in range(len(s) - 2, -1, -1):
            cur = num_map[s[idx]]
            if cur >= prev:
                result += cur
            else:
                result -= cur
            prev = cur
        return result

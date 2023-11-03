class Solution:
    def longestPalindrome(self, s: str) -> int:
        length = len(s)
        if length == 1:
            return 1
        result = 0
        counter = {}
        for char in s:
            if char in counter:
                counter[char] += 1
            else:
                counter[char] = 1
        odd_flag = False
        for count in counter.values():
            if count % 2 != 0 and not odd_flag:
                odd_flag = True
            if count >= 2:
                result += (count // 2) * 2
        if odd_flag:
            result += 1
        return result


pal = "fgghggfaa"
assert Solution().longestPalindrome(pal) == 9
print("OK")
